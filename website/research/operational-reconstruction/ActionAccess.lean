import MathFoundations.Autogeny.ActionObservation
import PhenomenalAccess
import Lean
set_option autoImplicit false

namespace UHM.ActionAccess
open MathFoundations.Autogeny.ActionObservation
universe u v w z l
variable {S : Type u} {A : Type v} {O : Type w} {V : Type z} {L : Type l}

/-- A decoder exists on the actual Autogeny action-observation quotient iff
    the proposed attribution agrees whenever all declared finite probes do. -/
theorem finiteProbeCriterion (m : System S A O V) (q : S → L) :
    (∃ d : Quot (Equivalent m) → L, ∀ s, d (Quot.mk _ s) = q s) ↔
    ∀ s t, (∀ o w, m.read o (run m w s) = m.read o (run m w t)) → q s = q t := by
  rw [PhenomenalAccess.descendsExactly]
  constructor <;> intro h s t he
  · exact h s t ((equivalent_iff_all_words m s t).mpr he)
  · exact h s t ((equivalent_iff_all_words m s t).mp he)

/-- Add a proposed internal distinction that has no causal path to the declared
    readouts, without changing any actions of the original system. -/
def silentExtension (m : System S A O V) : System (S × Bool) A O V where
  step a p := (m.step a p.1, p.2)
  read o p := m.read o p.1

theorem projectedRun (m : System S A O V) (w : List A) (s : S) (b : Bool) :
    run (silentExtension m) w (s,b) = (run m w s,b) := by
  induction w generalizing s with
  | nil => rfl
  | cons a w ih => exact ih (m.step a s)

theorem noHiddenDecoder (m : System S A O V) (s : S) :
    ¬ ∃ d : Quot (Equivalent (silentExtension m)) → Bool,
      ∀ p, d (Quot.mk _ p) = p.2 := by
  intro dec
  have impossible := (finiteProbeCriterion (silentExtension m) Prod.snd).mp dec
      (s,false) (s,true) (fun o w => by simp only [projectedRun]; rfl)
  exact Bool.noConfusion impossible

open Lean Elab Command in
run_cmd
  for decl in [``finiteProbeCriterion, ``projectedRun, ``noHiddenDecoder] do
    for ax in ← collectAxioms decl do
      unless [`propext, ``Quot.sound].contains ax do
        throwError "{decl} depends on {ax}"

#print axioms finiteProbeCriterion
#print axioms noHiddenDecoder
end UHM.ActionAccess
