import Std
set_option autoImplicit false

namespace ComparisonNetwork
/-- An observed sign on a pair; multiple incompatible outcomes are allowed in the data. -/
abbrev Edge (V : Type) := V → V → Bool → Prop
inductive Walk {V : Type} (e : Edge V) (i : V) : V → Bool → Prop where
  | zero : Walk e i i false
  | step {j k : V} {s b : Bool} : Walk e i j s → e j k b → Walk e i k (s ^^ b)

def Fits {V : Type} (e : Edge V) (labels : V → Bool) : Prop :=
  ∀ i j s, e i j s → s = (labels i ^^ labels j)

theorem integrate {V : Type} {e : Edge V} {x : V → Bool} (fits : Fits e x)
    {i j : V} {s : Bool} (p : Walk e i j s) : s = (x i ^^ x j) := by
  induction p with
  | zero => simp
  | @step j k t b _ edge ih =>
    rw [ih, fits _ _ _ edge]; cases x i <;> cases x j <;> cases x k <;> rfl

theorem append {V : Type} {e : Edge V} {i j k : V} {s t : Bool}
    (p : Walk e i j s) (q : Walk e j k t) : Walk e i k (s ^^ t) := by
  induction q with
  | zero => simpa using p
  | @step j k t b _ edge ih =>
    rw [← Bool.xor_assoc]; exact .step ih edge

theorem back {V : Type} {e : Edge V} (rev : ∀ i j s, e i j s → e j i s)
    {i j : V} {s : Bool} (p : Walk e i j s) : Walk e j i s := by
  induction p with
  | zero => exact .zero
  | @step j k t b _ edge ih =>
    have one : Walk e k j b := by simpa using Walk.step (Walk.zero (e:=e) (i:=k)) (rev _ _ _ edge)
    rw [Bool.xor_comm]; exact append one ih

/-- A spanning calibration supplies one recorded path from the root to each vertex.
    No cycle-consistency or edge fit is assumed of its readings. -/
theorem cycleCriterion {V : Type} (e : Edge V) (root : V)
    (rev : ∀ i j s, e i j s → e j i s)
    (base : V → Bool) (paths : ∀ v, Walk e root v (base v)) :
    (∃ x, Fits e x) ↔ ∀ s, Walk e root root s → s = false := by
  constructor
  · rintro ⟨x,hx⟩ s p; simpa using integrate hx p
  · intro h
    refine ⟨base, fun i j s edge => ?_⟩
    have c := h _ (append (Walk.step (paths i) edge) (back rev (paths j)))
    cases hi : base i <;> cases hj : base j <;> cases s <;> simp_all

theorem onlyGlobalSign {V : Type} {e : Edge V} (root : V)
    (connected : ∀ v, ∃ s, Walk e root v s) {x y : V → Bool}
    (hx : Fits e x) (hy : Fits e y) : ∀ v, y v = ((x root ^^ y root) ^^ x v) := by
  intro v
  obtain ⟨s,p⟩ := connected v
  have eq := (integrate hx p).symm.trans (integrate hy p)
  cases h1 : x root <;> cases h2 : y root <;> cases h3 : x v <;> cases h4 : y v <;> simp_all

/-- A test of the independent source response on four different preparations; no division
    or fitted scale is needed, so zero responses remain defined. Common cleared scale. -/
theorem tetrad (a b c d : Int) : (a*b)*(c*d) = (a*c)*(b*d) := by
  ac_rfl

end ComparisonNetwork
