import Lean

/-! Conditional operational readouts, independent of dimension and morphology.
The supplied section is data, not inferred invertibility or phenomenal meaning.
No finite experiment proves the universally quantified premises below. -/
namespace ReadoutDescent
set_option warningAsError true

structure Readout (X Y : Type) where
  read : X → Y
  lift : Y → X
  read_lift : ∀ y, read (lift y) = y

def Respects (q : X → Y) (f : X → X) : Prop :=
  ∀ x x', q x = q x' → q (f x) = q (f x')

def induced (r : Readout X Y) (f : X → X) : Y → Y :=
  fun y => r.read (f (r.lift y))

theorem induced_commutes (r : Readout X Y) (f : X → X)
    (h : Respects r.read f) (x : X) :
    induced r f (r.read x) = r.read (f x) :=
  h _ _ (r.read_lift _)

theorem existence_iff (r : Readout X Y) (f : X → X) :
    Respects r.read f ↔ ∃ g : Y → Y, ∀ x, g (r.read x) = r.read (f x) := by
  constructor
  · intro h
    exact ⟨induced r f, induced_commutes r f h⟩
  · intro ⟨g, h⟩ x x' same
    rw [← h x, ← h x', same]

theorem descended_unique (r : Readout X Y) (f : X → X) (g h : Y → Y)
    (hg : ∀ x, g (r.read x) = r.read (f x))
    (hh : ∀ x, h (r.read x) = r.read (f x)) : g = h := by
  funext y
  have a := hg (r.lift y)
  have b := hh (r.lift y)
  rw [r.read_lift] at a b
  exact a.trans b.symm

theorem respects_identity (q : X → Y) : Respects q id := by
  intro x x' same
  exact same

theorem respects_composition (q : X → Y) (f g : X → X)
    (hf : Respects q f) (hg : Respects q g) : Respects q (g ∘ f) := by
  intro x x' same
  exact hg _ _ (hf _ _ same)

theorem induced_identity (r : Readout X Y) : induced r id = id := by
  funext y
  exact r.read_lift y

theorem induced_composition (r : Readout X Y) (f g : X → X)
    (hg : Respects r.read g) : induced r (g ∘ f) = induced r g ∘ induced r f := by
  funext y
  exact (induced_commutes r g hg (f (r.lift y))).symm

-- None includes action unavailability/refusal, so it cannot be silently merged
-- with an enabled action returning a representative of the same fibre.
def PartialRespects (q : X → Y) (f : X → Option X) : Prop :=
  ∀ x x', q x = q x' → (f x).map q = (f x').map q

def inducedPartial (r : Readout X Y) (f : X → Option X) : Y → Option Y :=
  fun y => (f (r.lift y)).map r.read

theorem partial_commutes (r : Readout X Y) (f : X → Option X)
    (h : PartialRespects r.read f) (x : X) :
    inducedPartial r f (r.read x) = (f x).map r.read :=
  h _ _ (r.read_lift _)

theorem partial_existence_iff (r : Readout X Y) (f : X → Option X) :
    PartialRespects r.read f ↔ ∃ g : Y → Option Y,
      ∀ x, g (r.read x) = (f x).map r.read := by
  constructor
  · intro h
    exact ⟨inducedPartial r f, partial_commutes r f h⟩
  · intro ⟨g, h⟩ x x' same
    rw [← h x, ← h x', same]

theorem partial_domain_preserved (q : X → Y) (f : X → Option X)
    (h : PartialRespects q f) (x x' : X) (same : q x = q x') :
    (f x = none ↔ f x' = none) := by
  have mapped := h x x' same
  cases a : f x <;> cases b : f x' <;> simp_all

def Square (q : X → Y) (r : Z → W) (t : X → Z) (u : Y → W) : Prop :=
  ∀ x, r (t x) = u (q x)

theorem square_composition (q : X → Y) (r : Z → W) (s : V → U)
    (t : X → Z) (u : Y → W) (v : Z → V) (w : W → U)
    (first : Square q r t u) (second : Square r s v w) :
    Square q s (v ∘ t) (w ∘ u) := by
  intro x
  exact (second (t x)).trans (congrArg w (first x))

theorem transported_action (q : X → Y) (r : Z → W) (t : X → Z) (u : Y → W)
    (f : X → X) (g : Z → Z) (square : Square q r t u)
    (dynamics : ∀ x, g (t x) = t (f x)) (x : X) :
    r (g (t x)) = u (q (f x)) := by
  rw [dynamics x]
  exact square (f x)

-- Explicit separating states; no benchmark labels or physical interpretation.
def first : Bool × Bool → Bool := Prod.fst
def swap : Bool × Bool → Bool × Bool := fun x => (x.2, x.1)
def conditional : Bool × Bool → Option (Bool × Bool) :=
  fun x => if x.2 then some x else none
def projection : Readout (Bool × Bool) Bool :=
  ⟨first, fun b => (b, false), fun _ => rfl⟩

theorem readout_alias_witness :
    first (false, false) = first (false, true) ∧
    first (swap (false, false)) ≠ first (swap (false, true)) := by decide

theorem alias_prevents_descent : ¬ Respects first swap := by
  intro h
  have impossible := h (false, false) (false, true) rfl
  cases impossible

theorem varying_availability_prevents_descent : ¬ PartialRespects first conditional := by
  intro h
  have impossible := h (false, false) (false, true) rfl
  cases impossible

theorem a_section_does_not_repair_aliasing :
    induced projection swap (first (false, true)) ≠ first (swap (false, true)) := by
  decide

end ReadoutDescent

#print axioms ReadoutDescent.induced_commutes
#print axioms ReadoutDescent.existence_iff
#print axioms ReadoutDescent.descended_unique
#print axioms ReadoutDescent.respects_identity
#print axioms ReadoutDescent.respects_composition
#print axioms ReadoutDescent.induced_identity
#print axioms ReadoutDescent.induced_composition
#print axioms ReadoutDescent.partial_commutes
#print axioms ReadoutDescent.partial_existence_iff
#print axioms ReadoutDescent.partial_domain_preserved
#print axioms ReadoutDescent.square_composition
#print axioms ReadoutDescent.transported_action
#print axioms ReadoutDescent.readout_alias_witness
#print axioms ReadoutDescent.alias_prevents_descent
#print axioms ReadoutDescent.varying_availability_prevents_descent
#print axioms ReadoutDescent.a_section_does_not_repair_aliasing
