import MathFoundations.Metatheory.RealArithmeticPA

open MathFoundations.Category MathFoundations.Metatheory.RealPA

namespace ReconstructionAudit

/-- Negative regression control for the November 9 interface: a concrete model
    of the coding record would identify disjoint syntax constructors. -/
theorem noRealCodingAtAuditedRevision {Sys : Type} [Category.{0,0} Sys]
    (coding : RealArithGodelCoding Sys) : False := by
  have h := coding.conForm_eq_realConSentence coding.PAObj
  change ArithForm.imp _ ArithForm.bot = ArithForm.allForm _ at h
  cases h

#print axioms noRealCodingAtAuditedRevision
end ReconstructionAudit
