import Std
set_option autoImplicit false

namespace OperationalNetwork.BreathPractice

/-- Histories start at the external anchor. Each constructor appends an event.
    A completion belongs to the physical respiratory trace. Its flag belongs
    to the hypothesized internal observer and is not measured by the belt. -/
inductive History where
  | anchor
  | exhaled (before : History) (registered : Bool)
  | extra (before : History)
  | restart (before : History)
  deriving DecidableEq

def breaths : History → Nat
  | .anchor => 0
  | .exhaled h _ => breaths h + 1
  | .extra h | .restart h => breaths h

/-- The raw internal count since its own most recent reset. -/
def held : History → Nat
  | .anchor | .restart _ => 0
  | .exhaled h false => held h
  | .exhaled h true | .extra h => held h + 1

def missed : History → Nat
  | .anchor => 0
  | .exhaled h false => missed h + 1
  | .exhaled h true | .extra h | .restart h => missed h

def invented : History → Nat
  | .anchor => 0
  | .extra h => invented h + 1
  | .exhaled h _ | .restart h => invented h

/-- Counts discarded on resets. This includes any false increments already
    stored at the moment of that reset. -/
def discarded : History → Nat
  | .anchor => 0
  | .restart h => discarded h + held h
  | .exhaled h _ | .extra h => discarded h

/-- Cyclic register, zero at the external anchor. After a positive multiple
    of ten advances, residue zero denotes the silently counted numeral ten. -/
def advance (i : Fin 10) : Fin 10 := ⟨(i.val+1)%10, Nat.mod_lt _ (by decide)⟩

def counter : History → Fin 10
  | .anchor | .restart _ => 0
  | .exhaled h false => counter h
  | .exhaled h true | .extra h => advance (counter h)

theorem runModuloTen (h : History) : (counter h).val = held h % 10 := by
  induction h with
  | anchor => rfl
  | exhaled p registered ih =>
    cases registered
    · exact ih
    · simp only [counter,advance,held,ih]; omega
  | extra p ih => simp only [counter,advance,held,ih]; omega
  | restart p ih => rfl

theorem accounting (h : History) :
    breaths h + invented h = held h + missed h + discarded h := by
  induction h with
  | anchor => rfl
  | exhaled p registered ih => cases registered <;> simp [breaths,invented,held,missed,discarded] <;> omega
  | extra p ih => simp [breaths,invented,held,missed,discarded]; omega
  | restart p ih => simp [breaths,invented,held,missed,discarded]; omega

def oddCount (n : Nat) : Bool := decide (n%2=1)
def actualOdd (h : History) := oddCount (breaths h)
def recordedOdd (h : History) := oddCount (counter h).val

/-- Observing the counter residue loses no parity information because 2 divides
    10. Reporting can still fail even when a live internal count is correct. -/
theorem parityUnderWrap (h : History) : recordedOdd h = oddCount (held h) := by
  simp only [recordedOdd,oddCount,runModuloTen,Nat.mod_mod_of_dvd _ (by decide : 2 ∣ 10)]

theorem parityCorrectIff (h : History) :
    recordedOdd h = actualOdd h ↔ (missed h + invented h + discarded h)%2 = 0 := by
  have law := accounting h
  rw [parityUnderWrap]
  unfold actualOdd oddCount
  by_cases a : held h % 2 = 1 <;> by_cases b : breaths h % 2 = 1
  · rw [decide_eq_true a,decide_eq_true b]; constructor <;> intro _ <;> first | rfl | omega
  · rw [decide_eq_true a,decide_eq_false b]; constructor <;> intro e <;> first | contradiction | omega
  · rw [decide_eq_false a,decide_eq_true b]; constructor <;> intro e <;> first | contradiction | omega
  · rw [decide_eq_false a,decide_eq_false b]; constructor <;> intro _ <;> first | rfl | omega

private theorem flipOdd (n : Nat) : (!oddCount n) = oddCount (n+1) := by
  unfold oddCount
  by_cases h : n%2=1
  · rw [decide_eq_true h,decide_eq_false (show ¬(n+1)%2=1 by omega)]
    rfl
  · rw [decide_eq_false h,decide_eq_true (show (n+1)%2=1 by omega)]
    rfl

/-- One unregistered completion leaves the running count unchanged and flips
    the physical parity. An extra private increment flips the running parity. -/
theorem missedFlipsAgreement (h : History) :
    (recordedOdd (.exhaled h false) = actualOdd (.exhaled h false)) ↔ recordedOdd h ≠ actualOdd h := by
  change (recordedOdd h = oddCount (breaths h + 1)) ↔ recordedOdd h ≠ oddCount (breaths h)
  rw [← flipOdd]
  cases recordedOdd h <;> cases oddCount (breaths h) <;> decide

inductive Phase where | inhaling | exhaling deriving DecidableEq

/-- The terminal partial phase is supplied separately from the already
    completed exhalations, just as in the online probe. -/
structure Trial where
  before : History
  phase : Phase

inductive Query where | phase | parity deriving DecidableEq

def phaseLabel : Phase → Bool
  | .inhaling => false
  | .exhaling => true

def truth (t : Trial) : Query → Bool
  | .phase => phaseLabel t.phase
  | .parity => actualOdd t.before

def countState (t : Trial) := (t.phase,counter t.before)

def countAnswer (s : Phase × Fin 10) : Query → Bool
  | .phase => phaseLabel s.1
  | .parity => oddCount s.2.val

/-- Projection of the terminal state forgets the running count. Applying
    the same observation/reporting channel preserves all
    current-phase responses, including noise or abstention encoded by it. -/
theorem phaseProjection {Output : Type} (read : Phase → Output) (t : Trial) :
    read (countState t).1 = read t.phase := rfl

theorem countObservation (t : Trial) :
    countAnswer (countState t) .phase = truth t .phase ∧
    (countAnswer (countState t) .parity = truth t .parity ↔
      (missed t.before + invented t.before + discarded t.before)%2=0) :=
  ⟨rfl,parityCorrectIff t.before⟩

/-- A distribution of reports with integer weights. All probabilities with
    a common finite denominator are represented. Blank/missed is a third
    response and is scored as incorrect. -/
structure Votes where
  no : Nat
  yes : Nat
  blank : Nat

def total (v : Votes) := v.no + v.yes + v.blank
def correct (v : Votes) (label : Bool) := if label then v.yes else v.no

/-- Applies to any retained representation: if both histories produce the
    same representation and the two ground truths differ, a shared readout
    must split its total correct weight. -/
theorem pairedBlindScore {H O : Type} (read : O → Votes) (view : H → O)
    (label : H → Bool) (x y : H) (same : view x = view y) (opposite : label y = !label x) :
    correct (read (view x)) (label x) + correct (read (view y)) (label y) +
      (read (view x)).blank = total (read (view x)) := by
  rw [← same,opposite]
  cases label x <;> simp [correct,total,Nat.add_comm]

def accurate : Nat → History
  | 0 => .anchor
  | n+1 => .exhaled (accurate n) true

theorem accurateInvariant (n : Nat) :
    breaths (accurate n) = n ∧ held (accurate n) = n := by
  induction n with
  | zero => exact ⟨rfl,rfl⟩
  | succ n ih => simp [accurate,breaths,held,ih]

/-- Constructed opposite-parity histories at the same current phase.
    Constructing them as mathematical inputs does not certify that real
    subjects also have matched elapsed-time or other side information. -/
theorem historiesAtSamePhase (phase : Phase) (n : Nat) :
    let x : Trial := ⟨accurate n,phase⟩
    let y : Trial := ⟨accurate (n+1),phase⟩
    x.phase = y.phase ∧ truth y .parity = !truth x .parity ∧
      countAnswer (countState x) .parity = truth x .parity ∧
      countAnswer (countState y) .parity = truth y .parity := by
  dsimp only
  have ok (m : Nat) : recordedOdd (accurate m) = actualOdd (accurate m) := by
    rw [parityUnderWrap]
    simp only [actualOdd, (accurateInvariant m).1, (accurateInvariant m).2]
  refine ⟨rfl,?_,ok n,ok (n+1)⟩
  simp only [truth,actualOdd,oddCount,(accurateInvariant _).1]
  by_cases h : n%2=1 <;> simp [h] <;> omega

/-- Following can retain incidental history. A one-bit observer is sufficient
    to answer both questions on accurate traces without representing the
    ten-position ordinal; the instruction alone cannot force divergence. -/
def bitUpdate : History → Bool
  | .anchor | .restart _ => false
  | .exhaled h true | .extra h => !bitUpdate h
  | .exhaled h false => bitUpdate h

theorem oneBitSuffices (h : History) : bitUpdate h = recordedOdd h := by
  rw [parityUnderWrap]
  induction h with
  | anchor => rfl
  | restart => rfl
  | exhaled p flag ih =>
    cases flag
    · exact ih
    · exact (congrArg Bool.not ih).trans (flipOdd _)
  | extra p ih =>
    exact (congrArg Bool.not ih).trans (flipOdd _)

/-- The actions a completed/lost/invented count or a private restart
    presents to the internal register. Applying the same future actions
    in the two states tests dynamical congruence for this report. -/
inductive CountAction where | keep | tick | reset

def nextCounter (state : Fin 10) : CountAction → Fin 10
  | .keep => state
  | .tick => advance state
  | .reset => 0

def nextBit (bit : Bool) : CountAction → Bool
  | .keep => bit
  | .tick => !bit
  | .reset => false

theorem parityIntertwines (s : Fin 10) (action : CountAction) :
    oddCount (nextCounter s action).val = nextBit (oddCount s.val) action := by
  cases action with
  | keep => rfl
  | reset => rfl
  | tick =>
    change oddCount ((s.val+1)%10) = (!oddCount s.val)
    rw [flipOdd]
    unfold oddCount
    rw [Nat.mod_mod_of_dvd _ (by decide : 2 ∣ 10)]

theorem futureReports (s : Fin 10) (steps : List CountAction) :
    oddCount (steps.foldl nextCounter s).val = steps.foldl nextBit (oddCount s.val) := by
  induction steps generalizing s with
  | nil => rfl
  | cons a rest ih => simp only [List.foldl_cons,ih,parityIntertwines]

/-- Equality of every future answer has exactly two classes on this
    register. A common future is essential: differently timed private
    resets are different inputs to the observer. -/
theorem observationalParityIff (s r : Fin 10) :
    (∀ steps : List CountAction, oddCount (steps.foldl nextCounter s).val =
      oddCount (steps.foldl nextCounter r).val) ↔ oddCount s.val = oddCount r.val := by
  constructor
  · intro h; exact h []
  · intro eq steps; simp only [futureReports,eq]

theorem bothClassesReachable :
    oddCount (counter (accurate 1)).val = true ∧ oddCount (counter (accurate 2)).val = false := by decide

theorem negativeControls :
    recordedOdd (.restart (accurate 3)) ≠ actualOdd (.restart (accurate 3)) ∧
    recordedOdd (.exhaled (.exhaled (accurate 3) false) false) =
      actualOdd (.exhaled (.exhaled (accurate 3) false) false) := by decide

end OperationalNetwork.BreathPractice
