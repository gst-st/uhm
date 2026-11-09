import ProtocolMetric
set_option autoImplicit false
namespace OperationalNetwork

/-- Hide observation stations. Protocols between the retained ports can still use
    all original relays. Removing relays would define a different experiment. -/
def terminalExperiment {X T : Type} (e : Experiment X) (port : T → X)
    (distinct : ∀ i j, port i = port j → i = j) : Experiment T where
  hit i j := e.hit (port i) (port j)
  bound i j := e.bound (port i) (port j)
  witnessed i j := e.witnessed (port i) (port j)
  idle i := e.idle (port i)
  separates i j h := distinct i j (e.separates _ _ h)
  compose i j k := e.compose (port i) (port j) (port k)

theorem terminalCost {X T : Type} (e : Experiment X) (p : T → X)
    (inj : ∀ i j, p i = p j → i = j) (i j : T) :
    cost (terminalExperiment e p inj) i j = cost e (p i) (p j) := rfl

/-- One-sided comparison in calibrated ticks. The slack is charged once per
    *completed* experiment, in the common units of the two sides. -/
def PricedCover {T : Type} (e f : Experiment T) (p q slack : Nat) : Prop :=
  ∀ i j t, f.hit i j t = true → ∃ s, e.hit i j s = true ∧ p*s ≤ q*t + slack

theorem pricedCoverIff {T : Type} (e f : Experiment T) (p q slack : Nat) :
    PricedCover e f p q slack ↔
    ∀ i j, p * cost e i j ≤ q * cost f i j + slack := by
  constructor
  · intro cover i j
    obtain ⟨s,hit,hs⟩ := cover i j _ (attains f i j)
    exact Nat.le_trans (Nat.mul_le_mul_left p (leastCost e i j s hit)) hs
  · intro bound i j t hit
    exact ⟨_,attains e i j,Nat.le_trans (bound i j)
      (Nat.add_le_add_right (Nat.mul_le_mul_left q (leastCost f i j t hit)) _)⟩

theorem commonCalibratedScale {T : Type} (e f : Experiment T) (p q : Nat) :
    (∀ i j, p * cost e i j = q * cost f i j) ↔
      PricedCover e f p q 0 ∧ PricedCover f e q p 0 := by
  simp only [pricedCoverIff,Nat.add_zero]
  constructor
  · intro h
    exact ⟨fun i j => Nat.le_of_eq (h i j),fun i j => Nat.le_of_eq (h i j).symm⟩
  · rintro ⟨h,k⟩ i j
    exact Nat.le_antisymm (h i j) (k i j)

/-- Compose calibrations and absolute errors without rounding ratios or
    assuming that an error on each leg bounds an entire transmission. -/
theorem composePricedCover {T : Type} {e f g : Experiment T} {p q r s a b : Nat}
    (ef : PricedCover e f p q a) (fg : PricedCover f g r s b) :
    PricedCover e g (r*p) (q*s) (r*a+q*b) := by
  intro i j t hit
  obtain ⟨u,hu,hut⟩ := fg i j t hit
  obtain ⟨v,hv,hvu⟩ := ef i j u hu
  refine ⟨v,hv,?_⟩
  have left := Nat.mul_le_mul_left r hvu
  have right := Nat.mul_le_mul_left q hut
  rw [Nat.mul_add,← Nat.mul_assoc,← Nat.mul_assoc] at left right
  rw [Nat.mul_comm r q] at left
  omega

/-- Equality up to rational clock units can be tested against one calibrated,
    nonzero baseline on the same registered ports, without division. -/
theorem allPairsClockTest {T : Type} (e f : Experiment T) (i₀ j₀ : T)
    (positiveE : 0 < cost e i₀ j₀) (positiveF : 0 < cost f i₀ j₀) :
    (∃ p q : Nat, 0 < p ∧ 0 < q ∧ ∀ i j, p * cost e i j = q * cost f i j) ↔
    (∀ i j, cost f i₀ j₀ * cost e i j = cost e i₀ j₀ * cost f i j) := by
  constructor
  · rintro ⟨p,q,hp,_,h⟩ i j
    apply Nat.eq_of_mul_eq_mul_left hp
    calc
      p * (cost f i₀ j₀ * cost e i j) = cost f i₀ j₀ * (p * cost e i j) := Nat.mul_left_comm _ _ _
      _ = cost f i₀ j₀ * (q * cost f i j) := by rw [h i j]
      _ = (q * cost f i₀ j₀) * cost f i j := by rw [Nat.mul_left_comm, Nat.mul_assoc]
      _ = (p * cost e i₀ j₀) * cost f i j := by rw [h i₀ j₀]
      _ = p * (cost e i₀ j₀ * cost f i j) := Nat.mul_assoc _ _ _
  · intro h
    exact ⟨_,_,positiveF,positiveE,h⟩

/-- A genuine merge cannot preserve every fine point-to-point distance as a
    pullback of a separated coarse metric, even when all terminal tests agree. -/
theorem exactPullbackInjective {X Y : Type} (fine : Experiment X) (coarse : Experiment Y)
    (block : X → Y) (p q : Nat) (hp : 0 < p)
    (exactCost : ∀ x y, p * cost fine x y = q * cost coarse (block x) (block y))
    (x y : X) (same : block x = block y) : x = y := by
  have h := exactCost x y
  rw [same,(zeroIffSame coarse _ _).2 rfl,Nat.mul_zero] at h
  exact (zeroIffSame fine x y).1 ((Nat.mul_eq_zero.mp h).resolve_left (by omega))

/-- When unit n is the positive number of common ticks per macroscopic unit,
    this expresses uniform vanishing normalized discrepancy on the named ports.
    The reference array may itself vary with scale (e.g. rounded observations). -/
def MacroscopicAgreement {T : Type} (unit : Nat → Nat) (f g : Nat → T → T → Nat) : Prop :=
  ∀ k : Nat, ∃ start : Nat, ∀ n, start ≤ n → ∀ i j,
    k*f n i j ≤ k*g n i j + unit n ∧ k*g n i j ≤ k*f n i j + unit n

theorem largeScaleProtocols {T : Type} (unit : Nat → Nat) (e f : Nat → Experiment T) :
    MacroscopicAgreement unit (fun n => cost (e n)) (fun n => cost (f n)) ↔
      ∀ k, ∃ start, ∀ n, start ≤ n →
        PricedCover (e n) (f n) k k (unit n) ∧ PricedCover (f n) (e n) k k (unit n) := by
  simp only [pricedCoverIff]
  constructor
  · intro h k
    obtain ⟨start,h⟩ := h k
    exact ⟨start,fun n hn => ⟨fun i j => (h n hn i j).1, fun i j => (h n hn i j).2⟩⟩
  · intro h k
    obtain ⟨start,h⟩ := h k
    exact ⟨start,fun n hn i j => ⟨(h n hn).1 i j,(h n hn).2 i j⟩⟩

theorem transferMacroscopicAgreement {T : Type} {unit : Nat → Nat} {f g ref : Nat → T → T → Nat}
    (one : MacroscopicAgreement unit f g) (two : MacroscopicAgreement unit g ref) :
    MacroscopicAgreement unit f ref := by
  intro k
  obtain ⟨a,ha⟩ := one (k+k)
  obtain ⟨b,hb⟩ := two (k+k)
  refine ⟨max a b,?_⟩
  intro n hn i j
  obtain ⟨u,v⟩ := ha n (Nat.le_trans (Nat.le_max_left _ _) hn) i j
  obtain ⟨s,t⟩ := hb n (Nat.le_trans (Nat.le_max_right _ _) hn) i j
  simp only [Nat.add_mul] at u v s t
  clear hn ha hb one two
  constructor <;> omega

/-- Uniform indistinguishability at macroscopic scale allows collapse: a
    constant one-tick separation has zero normalized limit at unit n = n+1. -/
theorem unitSeparationCollapses : MacroscopicAgreement (fun n => n+1)
    (fun _ (i j : Bool) => if i=j then 0 else 1) (fun _ _ _ => 0) := by
  intro k
  refine ⟨k,?_⟩
  intro n hn i j
  by_cases h : i=j <;> simp [h] <;> omega

end OperationalNetwork
