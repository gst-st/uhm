import DynamicRefinement
set_option autoImplicit false
namespace OperationalNetwork.Refinement

/-- A physical passage carries both probes' measured ticks; parallel links need
    not agree. Both entries refer to the same passage and preparation. -/
abbrev PairedLinks (X : Type) := X → X → Nat → Nat → Prop

inductive PairedRun {X : Type} (e : PairedLinks X) : X → X → Nat → Nat → Prop
  | stay (x) : PairedRun e x x 0 0
  | step {x y z a b c d} : e x y a b → PairedRun e y z c d → PairedRun e x z (a+c) (b+d)

def probeLeft {X} (e : PairedLinks X) : Passage X := fun x y a => ∃ b, e x y a b
def probeRight {X} (e : PairedLinks X) : Passage X := fun x y b => ∃ a, e x y a b

theorem joinPaired {X} {e : PairedLinks X} {x y z a b c d}
    (u : PairedRun e x y a b) (v : PairedRun e y z c d) : PairedRun e x z (a+c) (b+d) := by
  induction u with
  | stay => simpa using v
  | step link _ ih => simpa only [Nat.add_assoc] using PairedRun.step link (ih v)

theorem observePaired {X} {e : PairedLinks X} {x y a b} (r : PairedRun e x y a b) :
    (∃ n, Itinerary (probeLeft e) x y a n) ∧ (∃ n, Itinerary (probeRight e) x y b n) := by
  induction r with
  | stay => exact ⟨⟨_,.stay _⟩,⟨_,.stay _⟩⟩
  | step edge _ ih =>
    obtain ⟨⟨_,u⟩,⟨_,v⟩⟩ := ih
    exact ⟨⟨_,.step ⟨_,edge⟩ u⟩,⟨_,.step ⟨_,edge⟩ v⟩⟩

theorem accompanyLeft {X} {e : PairedLinks X} {x y a n} (r : Itinerary (probeLeft e) x y a n) :
    ∃ b, PairedRun e x y a b := by
  induction r with
  | stay => exact ⟨_,.stay _⟩
  | step edge _ ih => obtain ⟨_,h⟩ := ih; obtain ⟨_,p⟩ := edge; exact ⟨_,.step p h⟩

theorem accompanyRight {X} {e : PairedLinks X} {x y b n} (r : Itinerary (probeRight e) x y b n) :
    ∃ a, PairedRun e x y a b := by
  induction r with
  | stay => exact ⟨_,.stay _⟩
  | step edge _ ih => obtain ⟨_,h⟩ := ih; obtain ⟨_,p⟩ := edge; exact ⟨_,.step p h⟩

/-- Two physical access/return paths at each station provide an executable
    finite test on finite graphs. No reverse traversal with a fictitious
    negative duration is used. -/
structure LoopAccess {X} (e : PairedLinks X) (root : X) where
  a : X → Nat
  b : X → Nat
  retA : X → Nat
  retB : X → Nat
  out : ∀ x, PairedRun e root x (a x) (b x)
  back : ∀ x, PairedRun e x root (retA x) (retB x)

def CalibratedEdges {X} (e : PairedLinks X) (a b : X → Nat) : Prop :=
  ∀ x y u v, e x y u v → a x + u + b y = b x + v + a y

theorem clockAlongRun {X} {e : PairedLinks X} {p q : X → Nat} (law : CalibratedEdges e p q)
    {x y a b} (r : PairedRun e x y a b) : p x + a + q y = q x + b + p y := by
  induction r with
  | stay => omega
  | step edge _ ih => have h := law _ _ _ _ edge; omega

/-- Only the access/return loop of each vertex and one physical loop per edge
    are tested. They suffice to certify every directed return and determine
    the endpoint correction for every open route. -/
theorem finiteLoopsIffAllLoops {X} {e : PairedLinks X} {root : X} (r : LoopAccess e root) :
    ((∀ x, r.a x + r.retA x = r.b x + r.retB x) ∧
     (∀ x y a b, e x y a b → r.a x + a + r.retA y = r.b x + b + r.retB y)) ↔
    (∀ a b, PairedRun e root root a b → a=b) := by
  constructor
  · rintro ⟨v,edge⟩ a b run
    have law : CalibratedEdges e r.a r.b := by
      intro x y u w link
      have one := v y
      have two := edge x y u w link
      omega
    have h := clockAlongRun law run
    omega
  · intro all
    constructor
    · intro x; exact all _ _ (joinPaired (r.out x) (r.back x))
    · intro x y a b link
      simpa only [Nat.add_assoc] using all _ _ (joinPaired (r.out x) (.step link (r.back y)))

theorem loopLaw {X} {e : PairedLinks X} {root : X} (r : LoopAccess e root)
    (all : ∀ a b, PairedRun e root root a b → a=b) : CalibratedEdges e r.a r.b := by
  obtain ⟨v,edge⟩ := (finiteLoopsIffAllLoops r).2 all
  intro x y a b h
  have u := v y
  have w := edge x y a b h
  omega

/-- The clock correction survives taking the first delivery; minimizers are
    allowed to be selected independently for the two probes. -/
theorem firstClockIdentity {X} (g h : TimedNetwork X) {e : PairedLinks X}
    (left : g.passage = probeLeft e) (right : h.passage = probeRight e)
    {p q : X → Nat} (law : CalibratedEdges e p q) (x y : X) :
    p x + g.first x y + q y = q x + h.first x y + p y := by
  obtain ⟨_,u⟩ := g.attained x y
  obtain ⟨_,v⟩ := h.attained x y
  rw [left] at u
  rw [right] at v
  obtain ⟨b,r⟩ := accompanyLeft u
  obtain ⟨a,s⟩ := accompanyRight v
  obtain ⟨_,hr⟩ := (observePaired r).2
  obtain ⟨_,hs⟩ := (observePaired s).1
  rw [← right] at hr
  rw [← left] at hs
  have rb := h.minimal hr
  have sa := g.minimal hs
  have rEq := clockAlongRun law r
  have sEq := clockAlongRun law s
  omega

/-- Two opposing physical links. One probe takes two units each way;
    the second probe takes three units outward and one on return. -/
def biasedLinks (u : Nat) : PairedLinks Bool := fun x y a b =>
  x ≠ y ∧ a = 2*u ∧ b = if x then u else 3*u

theorem balancedButDirected (u : Nat) :
    (∀ x a b, PairedRun (biasedLinks u) x x a b → a=b) ∧
    (∀ t, CanReach (probeLeft (biasedLinks u)) false true t ↔ 2*u ≤ t) ∧
    (∀ t, CanReach (probeRight (biasedLinks u)) false true t ↔ 3*u ≤ t) ∧
    (∀ t, CanReach (probeRight (biasedLinks u)) true false t ↔ u ≤ t) := by
  have law : CalibratedEdges (biasedLinks u) (fun _ => 0) (fun x => if x then u else 0) := by
    intro x y a b h
    obtain ⟨ne,rfl,rfl⟩ := h
    cases x <;> cases y <;> simp_all <;> omega
  constructor
  · intro x a b path; have eq := clockAlongRun law path; omega
  have outward : biasedLinks u false true (2*u) (3*u) := ⟨by decide,rfl,rfl⟩
  have inward : biasedLinks u true false (2*u) u := ⟨by decide,rfl,rfl⟩
  have direct {t c x y} {e : Passage Bool} (link : e x y c) (le : c≤t) : CanReach e x y t :=
    ⟨c,1,le,by simpa using Itinerary.step link (.stay y)⟩
  have firstLeg {E : Passage Bool} {x y : Bool} {b : Nat} (ne : x≠y)
      (lower : ∀ z a, E x z a → b ≤ a) {t} (path : CanReach E x y t) : b ≤ t := by
    obtain ⟨c,n,le,run⟩ := path
    cases run with
    | stay => exact False.elim (ne rfl)
    | step edge _ => have h := lower _ _ edge; omega
  exact ⟨fun t => ⟨firstLeg (by decide) (fun _ _ ⟨_,h⟩ => Nat.le_of_eq h.2.1.symm),
                      direct (e:=probeLeft _) ⟨_,outward⟩⟩,
         fun t => ⟨firstLeg (by decide) (fun _ _ ⟨_,h⟩ => Nat.le_of_eq h.2.2.symm),
                      direct (e:=probeRight _) ⟨_,outward⟩⟩,
         fun t => ⟨firstLeg (by decide) (fun _ _ ⟨_,h⟩ => Nat.le_of_eq h.2.2.symm),
                      direct (e:=probeRight _) ⟨_,inward⟩⟩⟩

end OperationalNetwork.Refinement
