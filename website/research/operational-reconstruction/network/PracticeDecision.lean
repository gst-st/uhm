import Std
set_option autoImplicit false
namespace OperationalNetwork.PracticeDecision

/-- Recorded hits have known count h. A completion assigns b of the u missing
    slots a hit, without changing the participant's fixed denominator. -/
def Completion (h u total : Nat) := ∃ b, b≤u ∧ total=h+b

theorem allCompletions (h u t : Nat) : Completion h u t ↔ h≤t ∧ t≤h+u := by
  constructor
  · rintro ⟨b,bound,rfl⟩; exact ⟨by omega,by omega⟩
  · rintro ⟨lo,hi⟩; exact ⟨t-h,by omega,by omega⟩

/-- The possible numerator for an arm difference with equal denominators.
    Losses in the two arms may have opposite causes and opposite outcomes. -/
theorem differenceEndpoints (a missingA b missingB : Nat) :
    (∀ ca cb, Completion a missingA ca → Completion b missingB cb →
      (a:Int)-(b+missingB) ≤ (ca:Int)-cb ∧ (ca:Int)-cb ≤ (a+missingA:Int)-b) ∧
    (Completion a missingA a ∧ Completion b missingB (b+missingB)) ∧
    (Completion a missingA (a+missingA) ∧ Completion b missingB b) := by
  constructor
  · intro ca cb ha hb
    obtain ⟨x,hx,rfl⟩ := ha
    obtain ⟨y,hy,rfl⟩ := hb
    constructor <;> omega
  · exact ⟨⟨⟨0,by omega,rfl⟩,⟨missingB,Nat.le_refl _,rfl⟩⟩,
           ⟨⟨missingA,Nat.le_refl _,rfl⟩,⟨0,by omega,rfl⟩⟩⟩

/-- Integer units can represent any common fixed precision for reported
    effect intervals. Simultaneous inclusion supplied by the statistical
    procedure implies the interaction bound for the underlying two effects. -/
theorem interactionFromJoint (phase history pl pu hl hu margin : Int)
    (p : pl≤phase ∧ phase≤pu) (h : hl≤history ∧ history≤hu)
    (support : pu<margin ∧ margin<hl) :
    0 < history-phase ∧ hl-pu ≤ history-phase ∧ history-phase ≤ hu-pl := by
  obtain ⟨_,_⟩ := p
  obtain ⟨_,_⟩ := h
  obtain ⟨_,_⟩ := support
  constructor
  · omega
  · constructor <;> omega

/-- In any shared fixed-point units the width of the phase-difference
    interval includes both missing fractions and both sampling radii.
    A supported equivalence interval has both endpoints strictly inside the
    margins, so exterior clipping to [-1,1] cannot rescue it. -/
theorem equivalenceRequiresPrecision (a b missingA missingB radius margin : Int)
    (lo : -margin < a-(b+missingB)-radius) (hi : a+missingA-b+radius < margin) :
    missingA+missingB+2*radius < 2*margin := by omega

end OperationalNetwork.PracticeDecision
