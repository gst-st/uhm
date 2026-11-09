import PortQuotient
import ProtocolMetric
set_option autoImplicit false

namespace OperationalNetwork.SignalNetwork

/-- Each directed link takes one tick. Vertices may be infinite in number;
    each receiver has a finite list of incoming links. Parallel links and
    self-loops are permitted. -/
def unitPassages {X : Type} (incoming : X → List X) : Passage X :=
  fun x y c => x ∈ incoming y ∧ c = 1

/-- Inject a single pulse at tick zero. Every receiver emits at the next tick
    iff an incoming link was active. Signals add by Boolean union (no
    interference or congestion). There is no implicit waiting or local latch. -/
def pulse {X : Type} [DecidableEq X] (incoming : X → List X) (source : X) :
    Nat → X → Bool
  | 0, y => decide (source = y)
  | t+1, y => (incoming y).any (pulse incoming source t)

theorem pulseHasTrip {X : Type} [DecidableEq X] {incoming : X → List X} {s y : X}
    {t : Nat} (active : pulse incoming s t y = true) :
    ∃ n, Itinerary (unitPassages incoming) s y t n := by
  induction t generalizing y with
  | zero =>
    obtain rfl : s = y := of_decide_eq_true active
    exact ⟨0,.stay s⟩
  | succ t ih =>
    obtain ⟨z, link, signal⟩ := List.any_eq_true.mp active
    obtain ⟨n, prior⟩ := ih signal
    have edge : unitPassages incoming z y 1 := ⟨link,rfl⟩
    have last : Itinerary (unitPassages incoming) z y 1 1 := .step edge (.stay y)
    exact ⟨_,joinTrips prior last⟩

/-- An actual pulse at any time travels along the supplied itinerary; this also
    handles return walks whose length exceeds the number of vertices. -/
theorem tripTransmits {X : Type} [DecidableEq X] {incoming : X → List X}
    {source x z : X} {c n t : Nat} (trip : Itinerary (unitPassages incoming) x z c n)
    (active : pulse incoming source t x = true) : pulse incoming source (t+c) z = true := by
  induction trip generalizing t with
  | stay => exact active
  | @step x y z w c n edge _ ih =>
    obtain ⟨link,rfl⟩ := edge
    have next : pulse incoming source (t+1) y = true := List.any_eq_true.mpr ⟨x,link,active⟩
    simpa only [Nat.add_assoc] using ih next

theorem pulseIffTrip {X : Type} [DecidableEq X] (incoming : X → List X) (s y : X) (t : Nat) :
    pulse incoming s t y = true ↔ ∃ n, Itinerary (unitPassages incoming) s y t n := by
  constructor
  · exact pulseHasTrip
  · rintro ⟨_,trip⟩
    have start : pulse incoming s 0 s = true := by simp [pulse]
    simpa only [Nat.zero_add] using tripTransmits trip start

/-- An observer who watched until the finite horizon b. none distinguishes
    absence throughout the observation window from a first tick of zero. -/
def firstTick? {X : Type} [DecidableEq X] (incoming : X → List X) (s y : X) (b : Nat) :
    Option Nat :=
  let p := fun t => pulse incoming s t y
  let t := scan p b
  if p t then some t else none

theorem firstTickSpec {X : Type} [DecidableEq X] (incoming : X → List X) (s y : X) (b t : Nat) :
    firstTick? incoming s y b = some t ↔ t ≤ b ∧
      (∃ n, Itinerary (unitPassages incoming) s y t n) ∧
      ∀ c n, Itinerary (unitPassages incoming) s y c n → t ≤ c := by
  let p := fun k => pulse incoming s k y
  change (if p (scan p b) then some (scan p b) else none) = some t ↔ _
  constructor
  · intro observed
    split at observed
    · rename_i hit
      cases observed
      refine ⟨scanBound p b, (pulseIffTrip _ _ _ _).1 hit, ?_⟩
      intro c n walk
      by_cases hc : c ≤ b
      · exact (scanWitness p b c hc ((pulseIffTrip _ _ _ _).2 ⟨n,walk⟩)).2
      · exact Nat.le_trans (scanBound p b) (by omega)
    · contradiction
  · rintro ⟨ht,trip,minimal⟩
    obtain ⟨found,le⟩ := scanWitness p b t ht ((pulseIffTrip _ _ _ _).2 trip)
    obtain ⟨m,w⟩ := (pulseIffTrip _ _ _ _).1 found
    rw [ite_eq_left found,Nat.le_antisymm le (minimal _ m w)]

theorem detectionIffReach {X : Type} [DecidableEq X] (incoming : X → List X) (s y : X)
    (b : Nat) : (firstTick? incoming s y b).isSome = true ↔
      CanReach (unitPassages incoming) s y b := by
  constructor
  · intro detected
    cases h : firstTick? incoming s y b with
    | none => simp [h] at detected
    | some t =>
      obtain ⟨ht,⟨n,trip⟩,_⟩ := (firstTickSpec _ _ _ _ _).1 h
      exact ⟨t,n,ht,trip⟩
  · rintro ⟨c,n,hc,walk⟩
    obtain ⟨hit,_⟩ := scanWitness (fun t => pulse incoming s t y) b c hc
      ((pulseIffTrip _ _ _ _).2 ⟨n,walk⟩)
    simp only [firstTick?, hit, ite_true, Option.isSome_some]

/-- An actual observed impulse determines the coarse reachable ball exactly
    under the port-lifting test. A detector may be placed at any fine terminal
    in the specified block; the actual fine start is fixed. -/
theorem groupedDetectionIffPortLift {X B : Type} [DecidableEq X] (incoming : X → List X)
    (block : X → B) :
    (∀ x j b, CanReach (blockEdge block (unitPassages incoming)) (block x) j b ↔
      ∃ y, block y = j ∧ (firstTick? incoming x y b).isSome = true) ↔
      PortLift block (unitPassages incoming) := by
  simp only [detectionIffReach]
  exact reachableBallsIffPortLift _ _

/-- A known reachability bound for every ordered pair turns the working
    receivers into an experiment for the general metric/scale theorems.
    Disconnected receivers instead retain the optional first-tick semantics. -/
def experiment {X : Type} [DecidableEq X] (incoming : X → List X) (bound : X → X → Nat)
    (available : ∀ s y, CanReach (unitPassages incoming) s y (bound s y)) : Experiment X where
  hit s y b := (firstTick? incoming s y b).isSome
  bound := bound
  witnessed s y := (detectionIffReach _ _ _ _).2 (available s y)
  idle s := (detectionIffReach _ _ _ _).2 ⟨0,0,Nat.le_refl _,.stay s⟩
  separates s y h := by
    obtain ⟨c,n,hc,walk⟩ := (detectionIffReach _ _ _ _).1 h
    obtain rfl : c = 0 := Nat.eq_zero_of_le_zero hc
    exact of_decide_eq_true ((pulseIffTrip _ _ _ _).2 ⟨n,walk⟩)
  compose s y z a b left right := by
    refine ⟨a+b,Nat.le_refl _,(detectionIffReach _ _ _ _).2 ?_⟩
    exact reachViaRelay ((detectionIffReach _ _ _ _).1 left)
      ((detectionIffReach _ _ _ _).1 right)

theorem costIsMeasuredFirstTick {X : Type} [DecidableEq X] (incoming : X → List X)
    (bound : X → X → Nat) (available : ∀ s y, CanReach (unitPassages incoming) s y (bound s y))
    (s y : X) : firstTick? incoming s y (bound s y) =
      some (cost (experiment incoming bound available) s y) := by
  let e := experiment incoming bound available
  obtain ⟨c,n,hc,trip⟩ := (detectionIffReach _ _ _ _).1 (attains e s y)
  have least (k m : Nat) (walk : Itinerary (unitPassages incoming) s y k m) :
      cost e s y ≤ k :=
    leastCost e s y k ((detectionIffReach _ _ _ _).2 ⟨k,m,Nat.le_refl _,walk⟩)
  have eq := Nat.le_antisymm hc (least c n trip)
  exact (firstTickSpec _ _ _ _ _).2 ⟨scanBound _ _, ⟨n,eq ▸ trip⟩, least⟩

end OperationalNetwork.SignalNetwork
