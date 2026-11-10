import Std
set_option autoImplicit false

namespace OperationalNetwork.PracticeChannels

/-- Counts of opposite history answers within one class a reader can actually
    distinguish, e.g. phase alone or phase together with elapsed time. -/
structure Cell where
  even : Nat
  odd : Nat
deriving DecidableEq

def Cell.total (c : Cell) := c.even + c.odd
def Cell.ambiguity (c : Cell) := min c.even c.odd
def Cell.imbalance (c : Cell) := c.even - c.odd + (c.odd - c.even)
def Cell.merged (c d : Cell) : Cell := ⟨c.even+d.even,c.odd+d.odd⟩

/-- For equal-weight trials and an odd-response probability k / denom. The
    random draw is conditionally independent of the hidden answer in a cell. -/
def correctTickets (c : Cell) (denom k : Nat) := c.even*(denom-k) + c.odd*k

private theorem ticketsBound (c : Cell) (denom k : Nat) (hk : k≤denom) :
    correctTickets c denom k ≤ max c.even c.odd * denom := by
  unfold correctTickets
  have parts := Nat.add_le_add
    (Nat.mul_le_mul_right (denom-k) (Nat.le_max_left c.even c.odd))
    (Nat.mul_le_mul_right k (Nat.le_max_right c.even c.odd))
  rwa [← Nat.mul_add,Nat.sub_add_cancel hk] at parts

def totalWith {Z : Type} (f : Z → Nat) (cells : List Z) := (cells.map f).sum

theorem exactClassCeiling {Z : Type} (table : Z → Cell) (cells : List Z) (denom : Nat) :
    (∀ guess : Z → Nat, (∀ c, guess c ≤ denom) →
      totalWith (fun c => correctTickets (table c) denom (guess c)) cells ≤
        denom * totalWith (fun c => max (table c).even (table c).odd) cells) ∧
    (∃ guess : Z → Nat, (∀ c, guess c ≤ denom) ∧
      totalWith (fun c => correctTickets (table c) denom (guess c)) cells =
        denom * totalWith (fun c => max (table c).even (table c).odd) cells) := by
  constructor
  · intro guess h
    induction cells with
    | nil => simp [totalWith]
    | cons c cs ih =>
      simp only [totalWith,List.map_cons,List.sum_cons,Nat.mul_add] at *
      exact Nat.add_le_add (by simpa [Nat.mul_comm] using ticketsBound (table c) denom (guess c) (h c)) ih
  · let g := fun c : Z => if (table c).even < (table c).odd then denom else 0
    refine ⟨g,fun c => by dsimp [g]; split <;> omega, ?_⟩
    induction cells with
    | nil => simp [totalWith]
    | cons c cs ih =>
      simp only [totalWith,List.map_cons,List.sum_cons,Nat.mul_add] at *
      rw [ih]
      by_cases h : (table c).even < (table c).odd
      · simp [g,h,correctTickets,Nat.max_eq_right (Nat.le_of_lt h),Nat.mul_comm]
      · simp [g,h,correctTickets,Nat.max_eq_left (by omega : (table c).odd ≤ (table c).even),Nat.mul_comm]

theorem ambiguityBudget (cells : List Cell) :
    totalWith (fun c => max c.even c.odd) cells + totalWith Cell.ambiguity cells =
      totalWith Cell.total cells ∧
    2 * totalWith (fun c => max c.even c.odd) cells =
      totalWith Cell.total cells + totalWith Cell.imbalance cells := by
  induction cells with
  | nil => simp [totalWith]
  | cons c cs ih =>
    obtain ⟨a,b⟩ := ih
    simp only [totalWith,List.map_cons,List.sum_cons] at *
    simp only [Cell.total,Cell.ambiguity,Cell.imbalance] at *
    constructor <;> omega

/-- Strict head-to-head separation against even the best class reader iff
    the other reader makes fewer errors than the total unavoidable ambiguity. -/
theorem gapIffErrors (cells : List Cell) (hits errors : Nat)
    (scored : hits+errors=totalWith Cell.total cells) :
    totalWith (fun c => max c.even c.odd) cells < hits ↔ errors < totalWith Cell.ambiguity cells := by
  have budget := (ambiguityBudget cells).1
  constructor <;> intro h <;> omega

/-- Refining a channel by an additional cue strictly improves its best score
    exactly when the two revealed classes have opposite strict majorities. -/
theorem cueHelpsIff (c d : Cell) :
    (max (c.merged d).even (c.merged d).odd < max c.even c.odd + max d.even d.odd) ↔
      (c.even<c.odd ∧ d.odd<d.even) ∨ (c.odd<c.even ∧ d.even<d.odd) := by
  simp only [Cell.merged]
  constructor
  · intro h
    by_cases a : c.even<c.odd
    · left; exact ⟨a,by omega⟩
    · right; exact ⟨by omega,by omega⟩
  · rintro (⟨_,_⟩|⟨_,_⟩) <;> omega

theorem timingLeakControl :
    let early : Cell := ⟨3,0⟩
    let late : Cell := ⟨0,3⟩
    max (early.merged late).even (early.merged late).odd = 3 ∧
      max early.even early.odd + max late.even late.odd = 6 := by decide

end OperationalNetwork.PracticeChannels
