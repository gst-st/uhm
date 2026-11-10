import SignalNetwork
set_option autoImplicit false
namespace OperationalNetwork.Refinement

/-- Bind the reported first cost to attained itineraries and exclude unobserved
    shortcuts. No metric or limiting space occurs in this contract. -/
structure TimedNetwork (X : Type) where
  passage : Passage X
  first : X → X → Nat
  attained : ∀ x y, ∃ n, Itinerary passage x y (first x y) n
  minimal : ∀ {x y c n}, Itinerary passage x y c n → first x y ≤ c

def fromPulse {X : Type} [DecidableEq X] (inputs : X → List X)
    (bound : X → X → Nat) (hit : ∀ x y, CanReach (SignalNetwork.unitPassages inputs) x y (bound x y)) :
    TimedNetwork X where
  passage := SignalNetwork.unitPassages inputs
  first x y := cost (SignalNetwork.experiment inputs bound hit) x y
  attained x y := by
    have run := (SignalNetwork.firstTickSpec inputs x y _ _).1
      (SignalNetwork.costIsMeasuredFirstTick inputs bound hit x y)
    exact run.2.1
  minimal := by
    intro x y c n path
    exact (SignalNetwork.firstTickSpec inputs x y _ _).1
      (SignalNetwork.costIsMeasuredFirstTick inputs bound hit x y) |>.2.2 c n path

theorem firstIdle {X : Type} (g : TimedNetwork X) (x : X) : g.first x x = 0 :=
  Nat.eq_zero_of_le_zero (g.minimal (.stay x))

theorem firstRelay {X : Type} (g : TimedNetwork X) (x y z : X) :
    g.first x z ≤ g.first x y + g.first y z := by
  obtain ⟨_,a⟩ := g.attained x y
  obtain ⟨_,b⟩ := g.attained y z
  exact g.minimal (joinTrips a b)

/-- A local clock reading may increase by at most the duration of a passage.
    The condition is directed; no reciprocal propagation is assumed. -/
def Causal {X : Type} (g : TimedNetwork X) (read : X → Nat) :=
  ∀ x y t, g.passage x y t → read y ≤ read x + t

theorem itineraryClock {X : Type} {g : TimedNetwork X} {read : X → Nat} (legal : Causal g read)
    {x y t n} (path : Itinerary g.passage x y t n) : read y ≤ read x + t := by
  induction path with
  | stay => exact Nat.le_refl _
  | step edge _ ih => have h := legal _ _ _ edge; omega

theorem arrivalClock {X : Type} (g : TimedNetwork X) (source : X) : Causal g (g.first source) := by
  intro x y t edge
  have le := g.minimal (Itinerary.step edge (.stay y))
  have triangle := firstRelay g source x y
  omega

/-- Dual certificate: the earliest time is the greatest possible increase of
    a causal register; the wavefront clock at the source attains the bound. -/
theorem separatesByClock {X : Type} (g : TimedNetwork X) (x y : X) (threshold : Nat) :
    threshold < g.first x y ↔ ∃ r, Causal g r ∧ r x + threshold < r y := by
  constructor
  · intro h
    exact ⟨g.first x,arrivalClock g x,by simpa [firstIdle] using h⟩
  · rintro ⟨r,legal,h⟩
    obtain ⟨_,run⟩ := g.attained x y
    have h' := itineraryClock legal run
    omega

/-- Each actual source passage admits a target itinerary. Credits are attached
    to vertices and telescope on any finite walk, including repeated cycles.
    Units p,q compare ticks by integer cross-multiplication. -/
structure Translation {X Y : Type} (g : TimedNetwork X) (h : TimedNetwork Y) (p q : Nat) where
  map : X → Y
  credit : X → Nat
  realize : ∀ x y t, g.passage x y t → ∃ c n,
    Itinerary h.passage (map x) (map y) c n ∧ p*c + credit y ≤ q*t + credit x

theorem translateTrip {X Y : Type} {g : TimedNetwork X} {h : TimedNetwork Y} {p q : Nat}
    (s : Translation g h p q) {x y t n} (path : Itinerary g.passage x y t n) :
    ∃ c m, Itinerary h.passage (s.map x) (s.map y) c m ∧ p*c + s.credit y ≤ q*t + s.credit x := by
  induction path with
  | stay => exact ⟨0,0,.stay _,by simp⟩
  | step edge _ ih =>
    obtain ⟨a,_,first,ha⟩ := s.realize _ _ _ edge
    obtain ⟨b,_,tail,hb⟩ := ih
    exact ⟨a+b,_,joinTrips first tail,by simp only [Nat.mul_add]; omega⟩

theorem translatedFirst {X Y : Type} {g : TimedNetwork X} {h : TimedNetwork Y} {p q : Nat}
    (s : Translation g h p q) (x y : X) :
    p*h.first (s.map x) (s.map y) + s.credit y ≤ q*g.first x y + s.credit x := by
  obtain ⟨_,path⟩ := g.attained x y
  obtain ⟨_,_,run,le⟩ := translateTrip s path
  exact Nat.le_trans (Nat.add_le_add_right (Nat.mul_le_mul_left _ (h.minimal run)) _) le

/-- A level consists of actual timed transfers and named observable ports.
    Names may agree at some finite resolutions. -/
structure Level (T : Type) where
  Site : Type
  graph : TimedNetwork Site
  port : T → Site

def ticks {T : Type} (level : Level T) (x y : T) := level.graph.first (level.port x) (level.port y)

structure PortTranslation {T : Type} (a b : Level T) (p q K : Nat) where
  sim : Translation a.graph b.graph p q
  ports : ∀ x, sim.map (a.port x) = b.port x
  oscillation : ∀ x y, sim.credit (a.port x) ≤ sim.credit (a.port y) + K

theorem portTimeBound {T : Type} {a b : Level T} {p q K : Nat} (s : PortTranslation a b p q K)
    (x y : T) : p*ticks b x y ≤ q*ticks a x y + K := by
  have h := translatedFirst s.sim (a.port x) (a.port y)
  rw [s.ports,s.ports] at h
  have hc := s.oscillation x y
  unfold ticks
  omega

/-- Measured local passage replacements between successive dyadic instrument
    resolutions. The per-completed-transfer error may vary with the level. -/
structure CostedTower {T : Type} (l : Nat → Level T) (error : Nat → Nat) where
  refine : ∀ n, PortTranslation (l n) (l (n+1)) 1 2 (error n)
  project : ∀ n, PortTranslation (l (n+1)) (l n) 2 1 (error n)

abbrev Tower {T : Type} (l : Nat → Level T) (K : Nat) := CostedTower l (fun _ => K)

def Sublinear (err : Nat → Nat) := ∀ k, ∃ N, ∀ n, N ≤ n → 2^k*err n ≤ 2^n

theorem exponentDominates (k : Nat) : k ≤ 2^k := by
  induction k with
  | zero => decide
  | succ k ih => have h := Nat.two_pow_pos k; rw [Nat.pow_succ]; omega

theorem boundedSublinear (K : Nat) : Sublinear (fun _ => K) := by
  intro k
  refine ⟨k+K,?_⟩
  intro n hn
  calc
    2^k*K ≤ 2^k*2^K := Nat.mul_le_mul_left _ (exponentDominates K)
    _ = 2^(k+K) := (Nat.pow_add ..).symm
    _ ≤ 2^n := Nat.pow_le_pow_right (by decide) hn

/-- R n/2^n is a certified remaining error on the ENTIRE tail. Each pair
    of successive error intervals nests, as follows from costed passage lifts. -/
def NestedBounds (f R : Nat → Nat) := ∀ n,
  f (n+1)+R (n+1) ≤ 2*(f n+R n) ∧ 2*f n+R (n+1) ≤ f (n+1)+2*R n

theorem observedBounds {T} {l : Nat → Level T} {err R : Nat → Nat}
    (tower : CostedTower l err) (pays : ∀ n, err n + R (n+1) ≤ 2*R n) (x y : T) :
    NestedBounds (fun n => ticks (l n) x y) R := by
  intro n
  have a := portTimeBound (tower.refine n) x y
  have b := portTimeBound (tower.project n) x y
  have budget := pays n
  dsimp only
  constructor <;> omega

theorem refinementEnvelope {f R} (step : NestedBounds f R) (n d : Nat) :
    f (n+d)+R (n+d) ≤ 2^d*(f n+R n) ∧ 2^d*f n+R (n+d) ≤ f (n+d)+2^d*R n := by
  induction d with
  | zero => simp
  | succ d ih =>
    obtain ⟨ha,hb⟩ := step (n+d)
    obtain ⟨left,right⟩ := ih
    rw [Nat.pow_succ,show n + (d+1) = (n+d)+1 by omega]
    simp only [Nat.mul_right_comm (2^d) 2]
    constructor <;> omega

theorem envelopeCauchy {f R} (step : NestedBounds f R) (small : Sublinear R) (k : Nat) :
    ∃ N, ∀ n m, N ≤ n → n ≤ m →
      2^k*f m ≤ 2^k*(2^(m-n)*f n)+2^m ∧ 2^k*(2^(m-n)*f n) ≤ 2^k*f m+2^m := by
  obtain ⟨N,tail⟩ := small k
  refine ⟨N,?_⟩
  intro n m hn hm
  obtain ⟨d,rfl⟩ := Nat.exists_eq_add_of_le hm
  rw [Nat.add_sub_cancel_left]
  obtain ⟨a,b⟩ := refinementEnvelope step n d
  rw [Nat.mul_add] at a
  have err : 2^k*(2^d*R n) ≤ 2^(n+d) := by
    rw [Nat.pow_add,Nat.mul_left_comm,Nat.mul_comm (2^n) (2^d)]
    exact Nat.mul_le_mul_left _ (tail n hn)
  have u : f (n+d) ≤ 2^d*f n + 2^d*R n := by omega
  have v : 2^d*f n ≤ f (n+d) + 2^d*R n := by omega
  constructor
  · exact Nat.le_trans (Nat.mul_le_mul_left _ u) (by rw [Nat.mul_add]; exact Nat.add_le_add_left err _)
  · exact Nat.le_trans (Nat.mul_le_mul_left _ v) (by rw [Nat.mul_add]; exact Nat.add_le_add_left err _)

theorem finiteScaleGap {f R} (step : NestedBounds f R) (small : Sublinear R) :
    (∃ k N, ∀ n, N ≤ n → 2^n ≤ 2^k*f n) ↔ ∃ n, R n < f n := by
  constructor
  · rintro ⟨k,N,h⟩
    obtain ⟨M,tail⟩ := small (k+1)
    let n := max N M
    refine ⟨n,?_⟩
    have lo := h n (Nat.le_max_left ..)
    have hi := tail n (Nat.le_max_right ..)
    rw [Nat.pow_succ,Nat.mul_right_comm] at hi
    have pos := Nat.two_pow_pos n
    exact Nat.lt_of_not_ge (fun bad => by have le := Nat.mul_le_mul_left (2^k) bad; omega)
  · rintro ⟨n,h⟩
    refine ⟨n,n,?_⟩
    intro m hm
    obtain ⟨d,rfl⟩ := Nat.exists_eq_add_of_le hm
    have right := (refinementEnvelope step n d).2
    have gap := Nat.mul_le_mul_left (2^d) (show R n+1 ≤ f n by omega)
    rw [Nat.mul_add,Nat.mul_one] at gap
    have one : 2^d ≤ f (n+d) := by omega
    rw [Nat.pow_add]
    exact Nat.mul_le_mul_left _ one

theorem observedDoubles {T} {l : Nat → Level T} {K} (tower : Tower l K) (x y : T) :
    NestedBounds (fun n => ticks (l n) x y) (fun _ => K) :=
  observedBounds tower (fun _ => by omega) x y

end OperationalNetwork.Refinement
