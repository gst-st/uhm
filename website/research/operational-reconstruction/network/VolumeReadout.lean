import Std
set_option autoImplicit false
namespace VolumeReadout

/-- Exact signed readings in common integer units. A common energy offset
    cannot be measured by a contrast, regardless of how the two states were found. -/
theorem shiftBlind {S : Type} (v : S → Int) (c : Int) (s t : S) :
    (v s + c) - (v t + c) = v s - v t := by omega

def reading (base volume : Int) (coefficient : Int) := base + coefficient * volume

/-- Equality of contrasts is equivalent to equality of the coefficients OR
    zero contrast of calibrated volumes, with other contributions fixed. -/
theorem identifiable (b₁ b₂ v₁ v₂ k l : Int) :
    reading b₁ v₁ k - reading b₂ v₂ k = reading b₁ v₁ l - reading b₂ v₂ l ↔
      k = l ∨ v₁ = v₂ := by
  have h (x : Int) : reading b₁ v₁ x - reading b₂ v₂ x =
      (b₁-b₂) + x*(v₁-v₂) := by
    simp only [reading,Int.mul_sub]; omega
  rw [h k,h l,Int.add_right_inj]
  constructor
  · intro eq
    by_cases vol : v₁-v₂ = 0
    · right; omega
    · exact Or.inl (Int.eq_of_mul_eq_mul_right vol eq)
  · rintro (rfl | rfl) <;> simp

end VolumeReadout
