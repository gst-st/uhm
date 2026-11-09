import Std
set_option autoImplicit false
namespace OperationalNetwork

/-- Exact additive separability for a crossed observation design in integer
    ticks (signed offsets are allowed). Choose one registered reference cell. -/
theorem reportSeparates {S M : Type} (t : S → M → Int) (r : S) (c : M) :
    (∀ s m, t s m + t r c = t s c + t r m) ↔
    (∃ event : S → Int, ∃ report : M → Int, ∀ s m, t s m = event s + report m) := by
  constructor
  · intro h
    refine ⟨fun s => t s c, fun m => t r m - t r c, ?_⟩
    intro s m
    have := h s m
    change t s m = t s c + (t r m - t r c)
    omega
  · rintro ⟨a,b,h⟩ s m
    rw [h s m,h r c,h s c,h r m]
    omega

theorem offsetFreedom {S M : Type} (a a' : S → Int) (b b' : M → Int) (r : S) (c : M)
    (same : ∀ s m, a s + b m = a' s + b' m) :
    ∃ k : Int, (∀ s, a' s = a s + k) ∧ (∀ m, b' m = b m - k) := by
  refine ⟨a' r-a r,?_,?_⟩
  · intro s; have := same s c; have := same r c; omega
  · intro m; have := same r m; omega

def witnessedTable (interaction : Bool) (s m : Bool) : Int :=
  (if s then 2 else 1) + (if m then 4 else 0) + (if interaction && s && m then 1 else 0)

theorem additiveWitness : ∀ s m, witnessedTable false s m + witnessedTable false false false =
    witnessedTable false s false + witnessedTable false false m := by decide

theorem interactionWitness :
    witnessedTable true true true + witnessedTable true false false ≠
      witnessedTable true true false + witnessedTable true false true := by decide

#print axioms reportSeparates
#print axioms offsetFreedom
#print axioms additiveWitness
#print axioms interactionWitness
end OperationalNetwork
