import LimitMetric
import CycleDelays
set_option autoImplicit false
namespace OperationalNetwork.Refinement
open OperationalNetwork.Continuum

theorem inverseTrip {X} {e : Passage X} {x y c n} (path : Itinerary e x y c n) :
    Itinerary (fun i j => e j i) y x c n := by
  induction path with
  | stay => exact .stay _
  | @step x y _ t _ _ edge _ back =>
    have leg : Itinerary (fun i j => e j i) y x t 1 := by simpa using Itinerary.step edge (.stay x) (e:=fun i j => e j i)
    simpa only [Nat.add_comm] using joinTrips back leg

def reverseNetwork {X} (g : TimedNetwork X) : TimedNetwork X where
  passage i j := g.passage j i
  first i j := g.first j i
  attained i j := by obtain ⟨_,r⟩ := g.attained j i; exact ⟨_,inverseTrip r⟩
  minimal path := g.minimal (inverseTrip path)

def reverseLevel {T} (l : Level T) : Level T := ⟨l.Site,reverseNetwork l.graph,l.port⟩

theorem observedDomination {f g err : Nat → Nat} (small : Sublinear err)
    (h : ∀ n, f n ≤ g n + err n) : Dominated f g := by
  intro k
  obtain ⟨N,hN⟩ := small k
  refine ⟨N,?_⟩
  intro n hn
  have le := Nat.mul_le_mul_left (2^k) (h n)
  rw [Nat.mul_add] at le
  exact Nat.le_trans le (Nat.add_le_add_left (hN n hn) _)

/-- Local path replacements on the actual probes. They can have different
    interior sites, links and minimizing routes. Errors are end-to-end. -/
structure MutualReadout {T : Type} (f g : Nat → Level T) where
  error : Nat → Nat
  small : Sublinear error
  forward : ∀ n, PortTranslation (f n) (g n) 1 1 (error n)
  backward : ∀ n, PortTranslation (g n) (f n) 1 1 (error n)

theorem simulatedClose {T} {f g : Nat → Level T} (h : MutualReadout f g) (x y : T) :
    Close (fun n => ticks (f n) x y) (fun n => ticks (g n) x y) :=
  ⟨observedDomination h.small (fun n => by simpa using portTimeBound (h.backward n) x y),
   observedDomination h.small (fun n => by simpa using portTimeBound (h.forward n) x y)⟩

/-- A second way to certify the same comparison on a common support: measure
    directed loop delays and the endpoint oscillation of their access clocks. -/
theorem cycleClocksClose {T} {X : Nat → Type} {e : ∀ n, PairedLinks (X n)}
    (a b : ∀ n, TimedNetwork (X n)) (port : ∀ n, T → X n)
    (ha : ∀ n, (a n).passage=probeLeft (e n)) (hb : ∀ n, (b n).passage=probeRight (e n))
    {root : ∀ n, X n} (r : ∀ n, LoopAccess (e n) (root n))
    (balanced : ∀ n u v, PairedRun (e n) (root n) (root n) u v → u=v)
    (err : Nat → Nat) (small : Sublinear err)
    (drift : ∀ n x y, (r n).a (port n x) + (r n).b (port n y) ≤
        (r n).b (port n x) + (r n).a (port n y) + err n) (x y : T) :
    Close (fun n => (a n).first (port n x) (port n y)) (fun n => (b n).first (port n x) (port n y)) := by
  have compare (n : Nat) := firstClockIdentity (a n) (b n) (ha n) (hb n)
    (loopLaw (r n) (balanced n)) (port n x) (port n y)
  constructor <;> apply observedDomination small <;> intro n
  · have := compare n; have := drift n y x; omega
  · have := compare n; have := drift n x y; omega

/-- Every closed excursion through a labelled destination has a measurable
    first possible return. On a shared support balanced cycles fix its value
    even when the endpoint correction grows as fast as the clock unit. -/
theorem equalFirstReturn {X} (g h : TimedNetwork X) {e : PairedLinks X} {root}
    (access : LoopAccess e root) (balanced : ∀ a b, PairedRun e root root a b → a=b)
    (left : g.passage=probeLeft e) (right : h.passage=probeRight e) (x y : X) :
    g.first x y + g.first y x = h.first x y + h.first y x := by
  have law := loopLaw access balanced
  have f := firstClockIdentity g h left right law x y
  have r := firstClockIdentity g h left right law y x
  omega

theorem firstReturnIsAttained {X} (g : TimedNetwork X) (x y : X) :
    (∃ n m, Itinerary g.passage x y (g.first x y) n ∧ Itinerary g.passage y x (g.first y x) m) ∧
      ∀ a b n m, Itinerary g.passage x y a n → Itinerary g.passage y x b m →
        g.first x y + g.first y x ≤ a+b := by
  obtain ⟨n,u⟩ := g.attained x y
  obtain ⟨m,v⟩ := g.attained y x
  exact ⟨⟨n,m,u,v⟩,fun _ _ _ _ h₁ h₂ => Nat.add_le_add (g.minimal h₁) (g.minimal h₂)⟩

private theorem outwardBound {f r g s : Nat → Nat} (fr : Dominated f r)
    (sg : Dominated s g) (total : Dominated (fun n => f n+r n) (fun n => g n+s n)) :
    Dominated f g := by
  intro k
  obtain ⟨A,h₁⟩ := fr (k+1)
  obtain ⟨B,h₂⟩ := sg (k+1)
  obtain ⟨C,h₃⟩ := total (k+1)
  refine ⟨max A (max B C),?_⟩
  intro n hn
  have u := h₁ n (by omega)
  have v := h₂ n (by omega)
  have w := h₃ n (by omega)
  simp only [Nat.pow_succ,Nat.mul_add,Nat.mul_right_comm (2^k) 2] at u v w
  have combined := Nat.add_le_add (Nat.add_le_add u v) w
  clear u v w
  apply Nat.le_of_not_lt
  intro impossible
  have opposite := Nat.mul_lt_mul_of_pos_left impossible (show 0 < 4 by decide)
  have weaker := Nat.le_trans combined (Nat.le_add_right _ (2^n))
  clear combined impossible
  omega

/-- In a common clock, agreement of round trips plus asymptotic reciprocity
    implies agreement of one-way times. No bound on endpoint potentials enters.
    The converse requires agreement of both directed observations. -/
theorem outwardFromReturn {f r g s : Nat → Nat} (first : Close f r) (second : Close g s)
    (total : Close (fun n => f n+r n) (fun n => g n+s n)) : Close f g :=
  ⟨outwardBound first.1 second.2 total.1,outwardBound second.1 first.2 total.2⟩

def towerGeometry {T} {l : Nat → Level T} {err R} (h : CostedTower l err)
    (pays : ∀ n, err n + R (n+1) ≤ 2*R n) (small : Sublinear R)
    (reciprocal : ∀ x y, Close (fun n => ticks (l n) x y) (fun n => ticks (l n) y x)) :
    LimitPseudometric T :=
  fromReadings (fun n => ticks (l n)) (fun x y => envelopeCauchy (observedBounds h pays x y) small)
    (fun n x => firstIdle (l n).graph ((l n).port x)) reciprocal
    (fun n x y z => firstRelay (l n).graph ((l n).port x) ((l n).port y) ((l n).port z))

/-- After measuring the first time at a single resolution, the certified
    reserve gives an explicit closed interval for the constructed real limit. -/
theorem certifiedInterval {f R : Nat → Nat} (step : NestedBounds f R) (small : Sublinear R) (n : Nat) :
    let distance := limit f (envelopeCauchy step small)
    valueLE (dyadic (f n-R n) n) distance ∧ valueLE distance (dyadic (f n+R n) n) := by
  constructor
  · apply dominatesEventually (N:=n)
    intro m hm
    obtain ⟨d,rfl⟩ := Nat.exists_eq_add_of_le hm
    change 2^(n+d-n)*(f n-R n) ≤ f (n+d)
    rw [Nat.add_sub_cancel_left,Nat.mul_sub]
    have lower := (refinementEnvelope step n d).2
    omega
  · apply dominatesEventually (N:=n)
    intro m hm
    obtain ⟨d,rfl⟩ := Nat.exists_eq_add_of_le hm
    change f (n+d) ≤ 2^(n+d-n)*(f n+R n)
    rw [Nat.add_sub_cancel_left]
    have upper := (refinementEnvelope step n d).1
    omega

/-- A finite, local, checkable obstruction to identifying the pair at infinity.
    With a certified remaining error R, a single registered
    potential rising by more than its local reserve suffices, and some such witness is necessary. -/
theorem noncollapseIffFiniteClock {T} {l : Nat → Level T} {err R} (h : CostedTower l err)
    (pays : ∀ n, err n + R (n+1) ≤ 2*R n) (small : Sublinear R) (rev) (x y : T) :
    Positive ((towerGeometry h pays small rev).dist x y) ↔ ∃ (n : Nat) (p : (l n).Site → Nat),
      Causal (l n).graph p ∧ p ((l n).port x) + R n < p ((l n).port y) := by
  change PositiveTail (fun n => ticks (l n) x y) ↔ _
  unfold PositiveTail
  rw [finiteScaleGap (observedBounds h pays x y) small]
  exact exists_congr (fun n => separatesByClock (l n).graph _ _ (R n))

/-- Deliver a common separated metric together with convergence of every probe
    to its distances. The target metric is constructed from transfers.
    Only the reference probe needs an interscale tower. -/
theorem commonMetricFromDynamics {T S : Type} (stable : StableEquality T)
    (reference : Nat → Level T) (probes : S → Nat → Level T) {err R} (h : CostedTower reference err)
    (pays : ∀ n, err n + R (n+1) ≤ 2*R n) (small : Sublinear R)
    (reverse : MutualReadout reference (fun n => reverseLevel (reference n)))
    (matchProbe : ∀ s x y, Close (fun n => ticks (reference n) x y) (fun n => ticks (probes s n) x y))
    (clocks : ∀ x y, x ≠ y → ∃ (n : Nat) (p : (reference n).Site → Nat),
      Causal (reference n).graph p ∧ p ((reference n).port x)+R n < p ((reference n).port y)) :
    ∃ d : LimitMetric T, (∀ x y, x ≠ y → Positive (d.dist x y)) ∧
      (∀ x y, Converges (fun n => ticks (reference n) x y) (d.dist x y)) ∧
      (∀ s x y, Converges (fun n => ticks (probes s n) x y) (d.dist x y)) := by
  let rev := simulatedClose reverse
  let ps := towerGeometry h pays small rev
  have gap : ∀ x y, x ≠ y → Positive (ps.dist x y) :=
    fun x y ne => (noncollapseIffFiniteClock h pays small rev x y).2 (clocks x y ne)
  exact ⟨ps.onLabels stable gap,gap,fun x y => nameConverges (fun n => ticks (reference n) x y) _,
    fun s x y => commonReading (envelopeCauchy (observedBounds h pays x y) small) (matchProbe s x y)⟩

/-- An end-to-end criterion using only round-trip comparisons between probes;
    each probe's forward/return bias must wash out in its calibrated units. -/
theorem commonMetricFromRoundTrips {T S : Type} (stable : StableEquality T)
    (ref : Nat → Level T) (probes : S → Nat → Level T) {err R} (h : CostedTower ref err)
    (pays : ∀ n, err n + R (n+1) ≤ 2*R n) (small : Sublinear R)
    (reverse : MutualReadout ref (fun n => reverseLevel (ref n)))
    (probeReciprocity : ∀ s x y, Close (fun n => ticks (probes s n) x y) (fun n => ticks (probes s n) y x))
    (returns : ∀ s x y, Close (fun n => ticks (ref n) x y + ticks (ref n) y x)
      (fun n => ticks (probes s n) x y + ticks (probes s n) y x))
    (clocks : ∀ x y, x ≠ y → ∃ (n : Nat) (p : (ref n).Site → Nat),
      Causal (ref n).graph p ∧ p ((ref n).port x)+R n < p ((ref n).port y)) :
    ∃ d : LimitMetric T, (∀ x y, x ≠ y → Positive (d.dist x y)) ∧
      (∀ x y, Converges (fun n => ticks (ref n) x y) (d.dist x y)) ∧
      (∀ s x y, Converges (fun n => ticks (probes s n) x y) (d.dist x y)) :=
  commonMetricFromDynamics stable ref probes h pays small reverse (fun s x y =>
    outwardFromReturn (simulatedClose reverse x y) (probeReciprocity s x y) (returns s x y)) clocks

end OperationalNetwork.Refinement
