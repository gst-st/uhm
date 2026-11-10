import RebitExperiment
set_option autoImplicit false

namespace ReferenceOrientation
/-- Exact matrix numerators. Common positive denominators do not affect equivalence. -/
def delta (i j : Bool) : Int := if i = j then 1 else 0
def jEntry : Bool → Bool → Int
  | false, true => -1
  | true, false => 1
  | _, _ => 0

/-- Four times the common denominator times the preparation rho(t), where t=u/d. -/
def block (d u : Int) (a c b e : Bool) : Int :=
  d * delta a c * delta b e + u * jEntry a c * jEntry b e

theorem block_flip (d u : Int) (a c b e : Bool) :
    block d (-u) a c b e = block d u c a b e := by
  cases a <;> cases c <;> cases b <;> cases e <;> simp [block, delta, jEntry]

def Axis : Nat → Type
  | 0 => Unit
  | n+1 => Bool × Axis n

/-- Separate local laboratories hold respectively all the A wires and all the B wires.
    Ratios may differ from source to source. Empty product is the unit experiment. -/
def batch : (s : List (Int × Int)) →
    Axis s.length → Axis s.length → Axis s.length → Axis s.length → Int
  | [], _, _, _, _ => 1
  | (d,t)::s, a,c,b,e => block d t a.1 c.1 b.1 e.1 * batch s a.2 c.2 b.2 e.2

def reversedBatch : (s : List (Int × Int)) →
    Axis s.length → Axis s.length → Axis s.length → Axis s.length → Int
  | [], _, _, _, _ => 1
  | (d,t)::s, a,c,b,e => block d (-t) a.1 c.1 b.1 e.1 * reversedBatch s a.2 c.2 b.2 e.2

theorem batch_flip (s : List (Int × Int)) (a c b e : Axis s.length) :
    reversedBatch s a c b e = batch s c a b e := by
  induction s with
  | nil => rfl
  | cons x s ih =>
    cases x
    simp only [reversedBatch, batch, block_flip, ih]

private def total {α : Type} (xs : List α) (f : α → Int) : Int :=
  (xs.map f).sum

private theorem plus {α : Type} (xs : List α) (f g : α → Int) :
    total xs (fun i => f i + g i) = total xs f + total xs g := by
  induction xs with
  | nil => rfl
  | cons x xs ih =>
    change (f x + g x) + total xs _ = (f x + total xs f) + (g x + total xs g)
    rw [ih]; omega

private theorem swap {α β : Type} (xs : List α) (ys : List β) (f : α → β → Int) :
    total xs (fun i => total ys (f i)) = total ys (fun j => total xs (fun i => f i j)) := by
  induction xs with
  | nil =>
    induction ys with
    | nil => rfl
    | cons y ys ih => simpa [total] using ih
  | cons x xs ih =>
    change total ys (f x) + total xs (fun i => total ys (f i)) =
      total ys (fun j => f x j + total xs (fun i => f i j))
    rw [plus, ih]

/-- Enumeration of the real product basis in each laboratory, at any finite copy count. -/
def basis : (n : Nat) → List (Axis n)
  | 0 => [()]
  | n+1 => (basis n).map (fun x => (false,x)) ++ (basis n).map (fun x => (true,x))

def record {α : Type} (xs : List α) (w : α → α → α → α → Int)
    (p q : α → α → Int) : Int :=
  total xs (fun a => total xs (fun c => total xs (fun b => total xs (fun e =>
    p a c * q b e * w a c b e))))

/-- Any real symmetric collective effect on A is blind to simultaneous reversal;
    B may use any matrix. Applies termwise to finite sums of product effects.
    Integer matrices represent rational effects after clearing common denominators. -/
theorem localBatchBlind (s : List (Int × Int)) (p q : Axis s.length → Axis s.length → Int)
    (sym : ∀ a c, p a c = p c a) :
    record (basis s.length) (reversedBatch s) p q = record (basis s.length) (batch s) p q := by
  unfold record
  simp only [batch_flip]
  rw [swap (basis s.length) (basis s.length) (fun a c => total _ (fun b => total _
    (fun e => p a c * q b e * batch s c a b e)))]
  congr 1; funext a; congr 1; funext c
  rw [sym c a]

/-- Contraction of a pair of J's, performed in each lab, with two independent sources.
    Correlation is the sign product; normalized, it is (u/d)(v/h). -/
def pairContrast (d u h v : Int) : Int :=
  let xs := basis 2
  let effect := fun (i j : Axis 2) => jEntry i.1 j.1 * jEntry i.2.1 j.2.1
  record xs (batch [(d,u),(h,v)]) effect effect

private def four (f : Axis 2 → Int) := f (false,false,()) + (f (false,true,()) +
    (f (true,false,()) + (f (true,true,()) + 0)))

theorem pairResponse (d u h v : Int) : pairContrast d u h v = 16*u*v := by
  let op (i j : Axis 2) := jEntry i.1 j.1 * jEntry i.2.1 j.2.1
  change four (fun a => four (fun c => four (fun b => four (fun e =>
    op a c * op b e * batch [(d,u),(h,v)] a c b e)))) = _
  simp [four, op, batch, block, jEntry, delta, Int.mul_assoc, Int.neg_mul, Int.mul_neg]
  omega

/-- The endpoint states used in the multi-copy theorem are exactly the states
    made by the coherent one-gate preparation, in the same bit/basis convention. -/
theorem wiredEndpoint (b : Bool) (a c j e : Bool) :
    block 1 (OperationalNetwork.Rebit.sgn b) a c j e =
      OperationalNetwork.Rebit.prepare b (a,j) (c,e) := by
  cases b <;> cases a <;> cases c <;> cases j <;> cases e <;> decide +kernel

private def outcome (b : Bool) (i j : Axis 2) : Int :=
  OperationalNetwork.Rebit.analyser b (i.1,i.2.1) (j.1,j.2.1)

/-- Born numerator of two local, physically wired parity effects. The omitted
    common positive denominator is 64*d*h: two state and two effect scales.
    The complete four-outcome law gives fair single-side records. -/
theorem wiredPairLaw (d u h v : Int) (left right : Bool) :
    record (basis 2) (batch [(d,u),(h,v)]) (outcome left) (outcome right) =
      16 * (d*h + (if left = right then u*v else -(u*v))) := by
  change four (fun a => four (fun c => four (fun b => four (fun e =>
    outcome left a c * outcome right b e * batch [(d,u),(h,v)] a c b e)))) = _
  cases left <;> cases right <;>
    simp [four, outcome, OperationalNetwork.Rebit.analyser, OperationalNetwork.Rebit.interact,
      OperationalNetwork.Rebit.readParity, OperationalNetwork.Rebit.product,
      OperationalNetwork.Rebit.cnot, OperationalNetwork.Rebit.xState, OperationalNetwork.Rebit.zState,
      OperationalNetwork.Rebit.sgn, batch, block, jEntry, delta, Int.neg_mul, Int.mul_neg] <;>
    omega

end ReferenceOrientation
