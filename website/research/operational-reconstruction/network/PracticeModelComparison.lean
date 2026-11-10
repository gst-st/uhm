import Std
set_option autoImplicit false

namespace OperationalNetwork.PracticeModelComparison

/-- Reverse chronological public records before the next action. -/
abbrev Past (Action : Type) := List (Action × Bool)

/-- An operational law on binary transcripts with a common finite probability
    denominator. Each *chosen* next action partitions precisely the same incoming
    mass. There is no prior distribution on a researcher's later action. -/
structure TranscriptLaw (Action : Type) where
  mass : Past Action → Nat
  positiveRoot : 0 < mass []
  consistent : ∀ h a, mass ((a,false)::h) + mass ((a,true)::h) = mass h

/-- The machine draws one uniform ticket at the root. No random bits from the
    future and no future query are available to this transition. -/
def respond {A : Type} (w : TranscriptLaw A) (h : Past A) (a : A) (ticket : Nat) : Bool × Nat :=
  let split := w.mass ((a,false)::h)
  if ticket < split then (false,ticket) else (true,ticket-split)

theorem responsePreservesTicket {A : Type} (w : TranscriptLaw A) (h : Past A) (a : A)
    (t : Nat) (live : t < w.mass h) :
    let r := respond w h a t
    r.2 < w.mass ((a,r.1)::h) := by
  have partition := w.consistent h a
  dsimp only [respond]
  split <;> dsimp <;> omega

/-- One transcript of an adaptive policy. Each next action is obtained from the
    recorded past alone. An arbitrary fixed finite prefix can be queried. -/
def follows {A : Type} (w : TranscriptLaw A) (policy : Past A → A)
    (h : Past A) (ticket : Nat) : List Bool → Prop
  | [] => True
  | bit :: rest =>
    let a := policy h
    let r := respond w h a ticket
    r.1 = bit ∧ follows w policy ((a,bit)::h) r.2 rest

/-- A path through the operational table corresponds to an interval of root
    tickets. The first field is its left endpoint, the second its size. -/
def interval {A : Type} (w : TranscriptLaw A) (policy : Past A → A) (h : Past A) :
    List Bool → Nat × Nat
  | [] => (0,w.mass h)
  | b :: bs =>
    let a := policy h
    let sub := interval w policy ((a,b)::h) bs
    ((if b then w.mass ((a,false)::h) else 0) + sub.1, sub.2)

def record {A : Type} (policy : Past A → A) (h : Past A) : List Bool → Past A
  | [] => h
  | b :: bs => record policy ((policy h,b)::h) bs

theorem intervalFits {A : Type} (w : TranscriptLaw A) (p : Past A → A)
    (h : Past A) (bits : List Bool) :
    (interval w p h bits).1 + (interval w p h bits).2 ≤ w.mass h := by
  induction bits generalizing h with
  | nil => simp [interval]
  | cons b bs ih =>
    have sub := ih ((p h,b)::h)
    have partition := w.consistent h (p h)
    cases b <;> simp only [interval, Bool.false_eq_true, ↓reduceIte, Nat.zero_add] <;> omega

theorem intervalMass {A : Type} (w : TranscriptLaw A) (p : Past A → A)
    (h : Past A) (bits : List Bool) : (interval w p h bits).2 = w.mass (record p h bits) := by
  induction bits generalizing h with
  | nil => rfl
  | cons b bs ih => exact ih ((p h,b)::h)

/-- Exact membership, including impossible (zero mass) outcomes. A cutoff
    or a randomized action independent of the ticket can be handled by
    reading prefixes or conditioning on the policy's independent coins. -/
theorem ticketIffTranscript {A : Type} (w : TranscriptLaw A) (p : Past A → A)
    (h : Past A) (bits : List Bool) (t : Nat) (live : t < w.mass h) :
    follows w p h t bits ↔ (interval w p h bits).1 ≤ t ∧
      t < (interval w p h bits).1 + (interval w p h bits).2 := by
  induction bits generalizing h t with
  | nil => simp [follows,interval,live]
  | cons b bs ih =>
    let a := p h
    have bound := intervalFits w p ((a,b)::h) bs
    have balanced := w.consistent h a
    change ((respond w h a t).1 = b ∧ follows w p ((a,b)::h) (respond w h a t).2 bs) ↔ _
    by_cases low : t < w.mass ((a,false)::h)
    · simp only [respond,ite_eq_left low]
      cases b with
      | false =>
        simpa only [interval,Bool.false_eq_true,↓reduceIte,Nat.zero_add,true_and] using
          ih ((a,false)::h) t low
      | true =>
        constructor
        · rintro ⟨bad,_⟩; contradiction
        · rintro ⟨lo,_⟩
          change w.mass ((a,false)::h) + _ ≤ t at lo
          exact False.elim (by omega)
    · have high : t - w.mass ((a,false)::h) < w.mass ((a,true)::h) := by omega
      simp only [respond,ite_eq_right low]
      cases b with
      | false =>
        constructor
        · rintro ⟨bad,_⟩; contradiction
        · rintro ⟨_,hi⟩
          change 0 + (interval w p ((a,false)::h) bs).1 +
            (interval w p ((a,false)::h) bs).2 > t at hi
          exact False.elim (by omega)
      | true =>
        simp only [eq_self,true_and,ih ((a,true)::h) (t-w.mass ((a,false)::h)) high]
        let pair := interval w p ((a,true)::h) bs
        change (pair.1 ≤ t-w.mass ((a,false)::h) ∧ t-w.mass ((a,false)::h) < pair.1 + pair.2) ↔
          (w.mass ((a,false)::h) + pair.1 ≤ t ∧ t < w.mass ((a,false)::h) + pair.1 + pair.2)
        constructor <;> rintro ⟨_,_⟩ <;> constructor <;> omega

/-- Every operational transcript is realized by exactly the designated mass
    of consecutive, distinct classical tickets, for every adaptive policy.
    At the root the probability is that mass divided by w.mass []. -/
theorem classicalReplay {A : Type} (w : TranscriptLaw A) (p : Past A → A) (bits : List Bool) :
    ∃ lower : Nat, lower + w.mass (record p [] bits) ≤ w.mass [] ∧
      ∀ t, t < w.mass [] →
        (follows w p [] t bits ↔ lower ≤ t ∧ t < lower + w.mass (record p [] bits)) := by
  refine ⟨(interval w p [] bits).1, ?_, ?_⟩
  · simpa only [← intervalMass w p [] bits] using intervalFits w p [] bits
  · intro t live
    simpa only [← intervalMass w p [] bits] using ticketIffTranscript w p [] bits t live

/-- An instrument's conditional binary outcome can be implemented with the
    same fresh random seed in two models. A seed may have any type or law.
    Copies of the result are observationally identical for any distribution
    of the supplied seeds independent of the future action choices. -/
abbrev Instrument (State Action Seed : Type) := State → Action → Seed → Bool × State

def run {A S R : Type} (instrument : Instrument S A R) (policy : Past A → A)
    (h : Past A) (state : S) : List R → List Bool
  | [] => []
  | u :: us =>
    let a := policy h
    let (b,next) := instrument state a u
    b :: run instrument policy ((a,b)::h) next us

/-- A memory holds either the initial preparation or one of the labels
    (last query, last answer). The conditional table stores the chance
    generator for each new question from each of these preparations. -/
def decode {A S : Type} (initial : S) (prepared : A → Bool → S) : Option (A × Bool) → S
  | none => initial
  | some (a,b) => prepared a b

def lastEventMachine {A S R : Type} (f : Instrument S A R) (initial : S)
    (prepared : A → Bool → S) : Instrument (Option (A × Bool)) A R :=
  fun memory a u =>
    let b := (f (decode initial prepared memory) a u).1
    (b,some (a,b))

/-- If *both* outcomes really reset the active sector, arbitrary adaptive
    continuations can be replayed by an ordinary last-event memory. The
    result holds seed for seed and hence is not confined to rational odds.
    Three binary questions use six post-measurement memory labels. -/
theorem lastEventReplay {A S R : Type} (f : Instrument S A R) (initial : S)
    (prepared : A → Bool → S)
    (reset : ∀ x a u, (f x a u).2 = prepared a ((f x a u).1))
    (policy : Past A → A) (h : Past A) (memory : Option (A × Bool)) (coins : List R) :
    run f policy h (decode initial prepared memory) coins =
      run (lastEventMachine f initial prepared) policy h memory coins := by
  induction coins generalizing h memory with
  | nil => rfl
  | cons u us ih =>
    let a := policy h
    let x := decode initial prepared memory
    let b := (f x a u).1
    change b :: run f policy ((a,b)::h) (f x a u).2 us =
      b :: run (lastEventMachine f initial prepared) policy ((a,b)::h) (some (a,b)) us
    rw [reset x a u]
    exact congrArg (List.cons b) (ih ((a,b)::h) (some (a,b)))

inductive Third where | early | middle | late deriving DecidableEq

/-- Pairwise symmetry and exact same-query repetition can hold while a
    classical six-state attention register violates the geometric overlap
    restriction: adjacent questions retain the last answer, the outer pair
    flips it. -/
def serialAnswer (old new : Third) (last : Bool) : Bool :=
  match old,new with
  | .early,.late | .late,.early => !last
  | _,_ => last

theorem repeatabilityAndSymmetry :
    (∀ q : Third, ∀ b, serialAnswer q q b = b) ∧
      (∀ i j : Third, ∀ b, serialAnswer i j b = serialAnswer j i b) := by
  exact ⟨fun q b => by cases q <;> rfl,fun i j b => by cases i <;> cases j <;> rfl⟩

theorem outerPairBreaksComposition (b : Bool) :
    serialAnswer .early .middle b = b ∧ serialAnswer .middle .late b = b ∧
      serialAnswer .early .late b ≠ b := by cases b <;> decide

/-- A coupling pairs ordinary trials with and without the optional probe, at
    common preparation. State can include private history. Readers include
    shared response noise; the intervention may also change the reader. -/
structure Trial (State : Type) where
  weight : Nat
  withoutProbe : State
  afterProbe : State
  mark : Bool
  reader0 : State → Bool
  reader1 : State → Bool

def massOf {S : Type} (p : Trial S → Bool) : List (Trial S) → Nat
  | [] => 0
  | x::xs => (if p x then x.weight else 0) + massOf p xs

def plain {S : Type} (r : Trial S) := r.reader0 r.withoutProbe
def masked {S : Type} (r : Trial S) := r.reader1 r.afterProbe
def stateChanged {S : Type} [DecidableEq S] (r : Trial S) := decide (r.withoutProbe ≠ r.afterProbe)
def readerChanged {S : Type} (r : Trial S) := decide (r.reader0 r.withoutProbe ≠ r.reader1 r.withoutProbe)

theorem marginalizeMark {S : Type} (xs : List (Trial S)) :
    massOf masked xs = massOf (fun r => r.mark && masked r) xs +
                       massOf (fun r => !r.mark && masked r) xs := by
  induction xs with
  | nil => rfl
  | cons x xs ih => cases mk : x.mark <;> cases h : masked x <;> simp_all [massOf] <;> omega

private theorem mismatchExplained {S : Type} [DecidableEq S] (r : Trial S)
    (h : plain r ≠ masked r) : stateChanged r = true ∨ readerChanged r = true := by
  by_cases diff : r.withoutProbe = r.afterProbe
  · right
    apply decide_eq_true
    simpa only [plain,masked,← diff] using h
  · left; exact decide_eq_true diff

private theorem boundByExceptions {T : Type} (p q a b : Trial T → Bool)
    (law : ∀ x, p x ≠ q x → a x = true ∨ b x = true) (xs : List (Trial T)) :
    massOf p xs ≤ massOf q xs + massOf a xs + massOf b xs := by
  induction xs with
  | nil => simp [massOf]
  | cons r rs ih =>
    cases hp : p r <;> cases hq : q r
    all_goals simp only [massOf,hp,hq,↓reduceIte,Bool.false_eq_true]
    all_goals first | omega | skip
    have bad := law r (by simp [hp,hq])
    rcases bad with ha | hb
    · simp only [ha,↓reduceIte]; omega
    · simp only [hb,↓reduceIte]; omega

/-- In common denominator units, a two-sided observable gap is bounded by
    possible state disturbance plus reader mismatch. A calibration on an
    incomplete proxy does not itself bound stateChanged. -/
theorem maskedGapBound {S : Type} [DecidableEq S] (xs : List (Trial S)) :
    let error := massOf stateChanged xs + massOf readerChanged xs
    massOf masked xs ≤ massOf plain xs + error ∧ massOf plain xs ≤ massOf masked xs + error := by
  constructor
  · simpa only [Nat.add_assoc] using boundByExceptions masked plain stateChanged readerChanged
      (fun x h => mismatchExplained x (Ne.symm h)) xs
  · simpa only [Nat.add_assoc] using boundByExceptions plain masked stateChanged readerChanged
      mismatchExplained xs

def proxyControl (visible : Bool) : Trial (Bool × Bool) :=
  ⟨1,(visible,false),(visible,true),visible,Prod.snd,Prod.snd⟩

/-- Both values of a measured calibration bit are represented equally and
    unchanged. A plain binary memory register changed by the intermediate
    probe generates maximal marginal order disturbance after hiding its mark. -/
theorem hiddenDisturbance :
    let xs := [proxyControl false,proxyControl true]
    (∀ v, (proxyControl v).withoutProbe.1 = (proxyControl v).afterProbe.1) ∧
    massOf plain xs = 0 ∧ massOf masked xs = 2 ∧
    massOf stateChanged xs = 2 ∧ massOf readerChanged xs = 0 := by
  dsimp only
  exact ⟨fun _ => rfl,by decide⟩

end OperationalNetwork.PracticeModelComparison
