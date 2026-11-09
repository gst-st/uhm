import Std
set_option autoImplicit false

namespace ReconstructionAudit

-- Ascending integer coefficients. Horner-form multiplication by x keeps
-- leading zeros; test equalities use lists of the same maximum degree.
abbrev Poly := List Int
def add : Poly → Poly → Poly
  | [], q => q
  | p, [] => p
  | a :: p, b :: q => (a + b) :: add p q
def scale (a : Int) (p : Poly) : Poly := p.map (a * ·)
def mul : Poly → Poly → Poly
  | [], _ => []
  | a :: p, q => add (scale a q) (0 :: mul p q)

def binomialMass (a b c d : Int) : Poly :=
  -- 7p = 1+6y, 7(1-p) = 6-6y. Multiply the branches by 7^3
  -- to remove the common denominator.
  let u : Poly := [1, 6]
  let v : Poly := [6, -6]
  let term := fun (x z w : Poly) => mul x (mul z w)
  add (add (scale a (term v v v)) (scale (3*b) (term u v v)))
      (add (scale (3*c) (term u u v)) (scale d (term u u u)))

def targetRows : List Nat := [165,74,228,1656]
def successRows : List Nat := [294,98,588,1764]
theorem legalRows : (targetRows.zip successRows).all
    (fun (a,s) => decide (a ≤ s ∧ s ≤ 1764)) = true ∧
    targetRows.length = 4 ∧ successRows.length = 4 := by decide

theorem denominator :
    binomialMass 294 98 588 1764 = scale (343*252) [1,0,6,0] := by decide
theorem numerator :
    binomialMass 165 74 228 1656 = scale (343*36) [4,0,24,18] := by decide
#print axioms legalRows
#print axioms denominator
#print axioms numerator
end ReconstructionAudit
