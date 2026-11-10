import Std

/-!
A one-preparation experiment in real quantum theory, restricted here to two
two-level ports. Matrix pairing, real local instruments, a fair source of
classical randomness, local X/Z eigenstate preparations and measurements,
and the coherent controlled-NOT permutation are laboratory inputs.

Matrices are stored as signed integer numerators. Each local X projector
has denominator two, each Z projector denominator one, each preparation
denominator four, and each parity effect denominator two. A joint Born score
has denominator eight. Clear independent positive common denominators to
apply the matrix results to all rationally specified instruments.
No imaginary unit, Bell-state source or primitive entangled measurement is
used. The output of the preparation excludes its private random bit.
-/
namespace OperationalNetwork.Rebit
open Lean.Grind

abbrev Pair := Bool × Bool
abbrev Mat (R : Type) (ι : Type) := ι → ι → R

private abbrev zz : Pair := (false, false)
private abbrev zo : Pair := (false, true)
private abbrev oz : Pair := (true, false)
private abbrev oo : Pair := (true, true)

def product {R : Type} [Mul R] (a b : Mat R Bool) : Mat R Pair :=
  fun i j => a i.1 j.1 * b i.2 j.2

def sumFour {R : Type} [Add R] (f : Pair → R) : R :=
  f zz + f zo + f oz + f oo

def born {R : Type} [Mul R] [Add R] (e s : Mat R Pair) : R :=
  sumFour fun i => sumFour fun j => e i j * s j i

def compose {R : Type} [Mul R] [Add R] (a b : Mat R Pair) : Mat R Pair :=
  fun i j => sumFour fun k => a i k * b k j

def sgn (b : Bool) : Int := if b then -1 else 1

/-- Both X eigenprojectors are stored at denominator two. -/
def xState (minus : Bool) : Mat Int Bool :=
  fun i j => if i == j then 1 else sgn minus

def zState (bit : Bool) : Mat Int Bool :=
  fun i j => if i == bit && j == bit then 1 else 0

def cnot (i : Pair) : Pair := (i.1, xor i.1 i.2)

/-- Conjugation by the coherent permutation matrix. CNOT is its own inverse,
    so the same relabelling acts on preparations and on measurement effects. -/
def interact {R : Type} (a : Mat R Pair) : Mat R Pair :=
  fun i j => a (cnot i) (cnot j)

theorem cnotInvolution (i : Pair) : cnot (cnot i) = i := by
  rcases i with ⟨a,b⟩; cases a <;> cases b <;> rfl

/-- Draw one fair bit t. Prepare the X eigenstate labelled t on the first port
    and the Z eigenstate labelled t xor minus on the second. Forget t. -/
def localMix (minus : Bool) : Mat Int Pair := fun i j =>
  (product (xState false) (zState minus) i j +
   product (xState true) (zState (!minus)) i j)

def prepare (minus : Bool) := interact (localMix minus)

/-- Measure X on the first port and Z on the second. Combine the two outcomes
    into their parity. Both terms below are ordinary product outcomes with denominator two. -/
def readParity (minus : Bool) : Mat Int Pair := fun i j =>
  product (xState false) (zState minus) i j +
  product (xState true) (zState (!minus)) i j

def analyser (minus : Bool) := interact (readParity minus)

def ident (i j : Pair) : Int := if i == j then 1 else 0
def jForm : Mat Int Bool
  | false, true => -1
  | true, false => 1
  | _, _ => 0

/-- Entrywise certificate tying the circuit to (I ± J ⊗ J)/4 and its
    two projectors (I ± J ⊗ J)/2. -/
theorem circuitMatrices (minus : Bool) (i j : Pair) :
    prepare minus i j = ident i j + sgn minus * product jForm jForm i j ∧
    analyser minus i j = prepare minus i j := by
  rcases i with ⟨a,b⟩; rcases j with ⟨c,d⟩
  cases minus <;> cases a <;> cases b <;> cases c <;> cases d <;> decide +kernel

theorem projectiveMeasurement (i j : Pair) (b : Bool) :
    analyser b i j = analyser b j i ∧
    compose (analyser b) (analyser b) i j = 2 * analyser b i j ∧
    compose (analyser b) (analyser (!b)) i j = 0 ∧
    analyser false i j + analyser true i j = 2 * ident i j := by
  rcases i with ⟨a,b₁⟩; rcases j with ⟨c,d⟩
  cases b <;> cases a <;> cases b₁ <;> cases c <;> cases d <;> decide +kernel

theorem preparedTrace (b : Bool) : sumFour (fun i => prepare b i i) = 4 := by
  cases b <;> decide +kernel

/-- The first and second bits in each parity are measured locally only after
    the interaction. Omitting CNOT from the analyser removes its advantage. -/
theorem measuredDistributions (b : Bool) :
    born (analyser b) (prepare b) = 8 ∧
    born (analyser (!b)) (prepare b) = 0 ∧
    born (readParity false) (prepare b) = 4 ∧
    born (readParity true) (prepare b) = 4 := by
  cases b <;> decide +kernel

/-- The ten independent entries of a symmetric two-port matrix in the
    computational basis 00,01,10,11. Used for states or differences of states. -/
structure Sym4 (R : Type) where
  d00 : R
  d01 : R
  d10 : R
  d11 : R
  a01 : R
  a02 : R
  a03 : R
  a12 : R
  a13 : R
  a23 : R

def Sym4.entry {R : Type} (s : Sym4 R) : Mat R Pair
  | (false,false), (false,false) => s.d00
  | (false,true),  (false,true)  => s.d01
  | (true,false),  (true,false)  => s.d10
  | (true,true),   (true,true)   => s.d11
  | (false,false), (false,true)  | (false,true),  (false,false) => s.a01
  | (false,false), (true,false)  | (true,false),  (false,false) => s.a02
  | (false,false), (true,true)   | (true,true),   (false,false) => s.a03
  | (false,true),  (true,false)  | (true,false),  (false,true)  => s.a12
  | (false,true),  (true,true)   | (true,true),   (false,true)  => s.a13
  | (true,false),  (true,true)   | (true,true),   (true,false)  => s.a23

structure Sym2 (R : Type) where
  lo : R
  cross : R
  hi : R

def Sym2.entry {R : Type} (s : Sym2 R) : Mat R Bool
  | false, false => s.lo
  | true, true => s.hi
  | _, _ => s.cross

private theorem mulTwo (x : Int) : x * 2 = x + x := by rw [Int.mul_comm, Int.two_mul]

/-- Integer distributivity and canonical product ordering suffice after clearing
    denominators. Omega checks the remaining additive cancellation. -/
local macro "integerPolynomial" : tactic => `(tactic|
  (first | omega | simp only [Int.pow_succ, Int.pow_zero, Int.two_mul, mulTwo, Int.mul_one, Int.one_mul, Int.zero_mul,
    Int.mul_zero, Int.zero_add, Int.add_zero, Int.add_mul, Int.mul_add, Int.sub_mul,
    Int.mul_sub, Int.neg_mul, Int.mul_neg, Int.mul_assoc, Int.mul_comm,
    Int.mul_left_comm] at * <;> omega))

section Tomography

def localValue {R : Type} [Mul R] [Add R] (s : Sym4 R) (a b : Sym2 R) :=
  born (product a.entry b.entry) s.entry

/-- Zero is the score of an unnormalized signed difference. -/
def locallyBlind (s : Sym4 Int) := ∀ a b, localValue s a b = 0

/-- The blind difference is exactly t J ⊗ J. -/
def hiddenLine (s : Sym4 Int) : Prop :=
  s.d00 = 0 ∧ s.d01 = 0 ∧ s.d10 = 0 ∧ s.d11 = 0 ∧
  s.a01 = 0 ∧ s.a02 = 0 ∧ s.a13 = 0 ∧ s.a23 = 0 ∧ s.a12 = -s.a03

private def loProbe : Sym2 Int := ⟨1,0,0⟩
private def hiProbe : Sym2 Int := ⟨0,0,1⟩
private def plusProbe : Sym2 Int := ⟨1,1,1⟩

/-- These are nine unnormalized joint yes/yes weights of the three local
    rank-one projectors |0><0|, |1><1|, |+><+|. -/
def nineDark (s : Sym4 Int) : Prop :=
  ∀ a ∈ [loProbe, hiProbe, plusProbe], ∀ b ∈ [loProbe, hiProbe, plusProbe],
    localValue s a b = 0

theorem nineTestsComplete (s : Sym4 Int) : nineDark s ↔ hiddenLine s := by
  constructor
  · intro h
    have h00 := h loProbe (by simp) loProbe (by simp)
    have h01 := h loProbe (by simp) hiProbe (by simp)
    have h10 := h hiProbe (by simp) loProbe (by simp)
    have h11 := h hiProbe (by simp) hiProbe (by simp)
    have h0x := h loProbe (by simp) plusProbe (by simp)
    have hx0 := h plusProbe (by simp) loProbe (by simp)
    have h1x := h hiProbe (by simp) plusProbe (by simp)
    have hx1 := h plusProbe (by simp) hiProbe (by simp)
    have hxx := h plusProbe (by simp) plusProbe (by simp)
    simp only [localValue,born,sumFour,product,Sym2.entry,Sym4.entry,
      loProbe,hiProbe,plusProbe] at h00 h01 h10 h11 h0x hx0 h1x hx1 hxx
    refine ⟨?_,?_,?_,?_,?_,?_,?_,?_,?_⟩ <;> integerPolynomial
  · rintro ⟨h0,h1,h2,h3,h4,h5,h6,h7,h8⟩ a _ b _
    simp only [localValue,born,sumFour,product,Sym2.entry,Sym4.entry,
      h0,h1,h2,h3,h4,h5,h6,h7,h8]
    integerPolynomial

theorem allProductTestsComplete (s : Sym4 Int) : locallyBlind s ↔ hiddenLine s := by
  constructor
  · intro h
    exact (nineTestsComplete s).1 (fun a _ b _ => h a b)
  · rintro ⟨h0,h1,h2,h3,h4,h5,h6,h7,h8⟩ a b
    simp only [localValue,born,sumFour,product,Sym2.entry,Sym4.entry,
      h0,h1,h2,h3,h4,h5,h6,h7,h8]
    integerPolynomial

/-- Criterion for a new symmetric joint observable to see the remaining
    parameter. If its two opposite-corner entries differ, its score on the
    blind line is a nonzero multiple of the unknown signed difference. -/
theorem jointResponse (s e : Sym4 Int) (h : hiddenLine s) :
    born e.entry s.entry = 2 * (e.a03 - e.a12) * s.a03 := by
  rcases h with ⟨h0,h1,h2,h3,h4,h5,h6,h7,h8⟩
  simp only [born,sumFour,Sym4.entry,h0,h1,h2,h3,h4,h5,h6,h7,h8]
  integerPolynomial

/-- If a signed difference is invisible to the nine physical local tests,
    one extra joint test with unequal opposite-corner entries suffices to
    reconstruct the full symmetric matrix. -/
theorem tenthTestComplete (s e : Sym4 Int) (hne : e.a03 ≠ e.a12)
    (localData : nineDark s) (joint : born e.entry s.entry = 0) :
    ∀ i j, s.entry i j = 0 := by
  have h := (nineTestsComplete s).1 localData
  rw [jointResponse s e h] at joint
  rcases h with ⟨h0,h1,h2,h3,h4,h5,h6,h7,h8⟩
  have nonzero : 2 * (e.a03 - e.a12) ≠ 0 := by omega
  have hz : s.a03 = 0 := (Int.mul_eq_zero.mp joint).resolve_left nonzero
  rintro ⟨a,b⟩ ⟨c,d⟩
  cases a <;> cases b <;> cases c <;> cases d <;>
    simp only [Sym4.entry,h0,h1,h2,h3,h4,h5,h6,h7,h8,hz] <;> integerPolynomial

/-- Heisenberg pullback of a terminal observable along one real local Kraus
    branch. The symmetry of Kᵀ E K is the step needed for adaptive protocols. -/
def pullEntry {R : Type} [Semiring R] (k : Mat R Bool) (e : Sym2 R) (i j : Bool) : R :=
  k false i * (e.lo * k false j + e.cross * k true j) +
  k true i * (e.cross * k false j + e.hi * k true j)

def pull {R : Type} [Semiring R] (k : Mat R Bool) (e : Sym2 R) : Sym2 R :=
  ⟨pullEntry k e false false, pullEntry k e false true, pullEntry k e true true⟩

theorem pullSymmetric (k : Mat Int Bool) (e : Sym2 Int) (i j : Bool) :
    (pull k e).entry i j = pullEntry k e i j := by
  cases i <;> cases j <;> simp only [pull,Sym2.entry,pullEntry] <;> integerPolynomial

/-- A finite event of a local adaptive protocol. Branches after different
    recorded outcomes may use different subsequent filters. Unobserved Kraus
    indices and unions of disjoint records are represented by 'merge'.
    We allow arbitrary symmetric terminal scores and scalar coefficients:
    the blindness theorem therefore covers their normalized physical subset.
    The two parties share classical records, not an entangled ancilla. -/
inductive LocalEvent (R : Type)
  | terminal (left right : Sym2 R)
  | onLeft (kraus : Mat R Bool) (next : LocalEvent R)
  | onRight (kraus : Mat R Bool) (next : LocalEvent R)
  | merge (a b : LocalEvent R)
  | weight (w : R) (next : LocalEvent R)

/-- The preceding history pulls a future effect back to the input. -/
def eventScore {R : Type} [Semiring R] (s : Sym4 R) (event : LocalEvent R)
    (left right : Sym2 R → Sym2 R) : R :=
  match event with
  | .terminal a b => localValue s (left a) (right b)
  | .onLeft k next => eventScore s next (fun a => left (pull k a)) right
  | .onRight k next => eventScore s next left (fun b => right (pull k b))
  | .merge a b => eventScore s a left right + eventScore s b left right
  | .weight w next => w * eventScore s next left right

private theorem eventBlind {R : Type} [Semiring R] (s : Sym4 R)
    (h : ∀ a b, localValue s a b = 0) (event : LocalEvent R) :
    ∀ left right, eventScore s event left right = 0 := by
  induction event with
  | terminal => exact fun left right => h _ _
  | onLeft _ _ ih => exact fun left right => ih _ _
  | onRight _ _ ih => exact fun left right => ih _ _
  | merge _ _ a b =>
    intro left right; simp only [eventScore,a,b,Semiring.add_zero]
  | weight _ _ ih =>
    intro left right; simp only [eventScore,ih,Semiring.mul_zero]

theorem localEventsComplete (s : Sym4 Int) :
    (∀ event, eventScore s event id id = 0) ↔ hiddenLine s := by
  constructor
  · intro h
    exact (allProductTestsComplete s).1 (fun a b => h (.terminal a b))
  · intro h event
    exact eventBlind s ((allProductTestsComplete s).2 h) event id id

end Tomography

/-- Pack a matrix into its ten upper-triangular coordinates. -/
def coordinates {R : Type} (m : Mat R Pair) : Sym4 R :=
  ⟨m zz zz, m zo zo, m oz oz, m oo oo, m zz zo, m zz oz,
   m zz oo, m zo oz, m zo oo, m oz oo⟩

theorem coordinatesComplete {R : Type} (m : Mat R Pair)
    (sym : ∀ i j, m i j = m j i) (i j : Pair) :
    (coordinates m).entry i j = m i j := by
  rcases i with ⟨a,b⟩; rcases j with ⟨c,d⟩
  cases a <;> cases b <;> cases c <;> cases d <;>
    simp only [coordinates,Sym4.entry] <;> apply sym

def preparedDifference := coordinates fun i j => prepare false i j - prepare true i j

theorem realisedHiddenLine :
    hiddenLine preparedDifference ∧ preparedDifference.a03 = 2 ∧
    (coordinates (analyser false)).a03 ≠ (coordinates (analyser false)).a12 := by
  unfold hiddenLine preparedDifference coordinates
  decide +kernel

theorem localHistoriesBlind (event : LocalEvent Int) :
    eventScore preparedDifference event id id = 0 :=
  (localEventsComplete preparedDifference).2 realisedHiddenLine.1 event

private theorem actualEntries (i j : Pair) :
    preparedDifference.entry i j =
      (coordinates (prepare false)).entry i j - (coordinates (prepare true)).entry i j := by
  rcases i with ⟨a,b⟩; rcases j with ⟨c,d⟩
  cases a <;> cases b <;> cases c <;> cases d <;> rfl

private theorem localScoreDifference (a b : Sym2 Int) :
    localValue preparedDifference a b =
      localValue (coordinates (prepare false)) a b - localValue (coordinates (prepare true)) a b := by
  simp only [localValue,born,sumFour,actualEntries]
  integerPolynomial

private theorem historyDifference (event : LocalEvent Int) :
    ∀ left right, eventScore preparedDifference event left right =
      eventScore (coordinates (prepare false)) event left right -
      eventScore (coordinates (prepare true)) event left right := by
  induction event with
  | terminal => exact fun _ _ => localScoreDifference _ _
  | onLeft _ _ ih => exact fun _ _ => ih _ _
  | onRight _ _ ih => exact fun _ _ => ih _ _
  | merge _ _ a b =>
    intro left right; simp only [eventScore,a,b]; integerPolynomial
  | weight _ _ ih =>
    intro left right; simp only [eventScore,ih]; integerPolynomial

/-- Every event, including a full adaptive transcript, has the same score
    on the two actual prepared states with only the local quantum devices. -/
theorem equalLocalRecords (event : LocalEvent Int) :
    eventScore (coordinates (prepare false)) event id id =
      eventScore (coordinates (prepare true)) event id id := by
  have h := historyDifference event id id
  have z := localHistoriesBlind event
  omega

/-- An explicit sum-of-squares certificate of positivity of each preparation
    as a real density matrix. All coefficients in the certificate are rational. -/
theorem preparationSquares (minus : Bool) (v : Pair → Int) :
    (sumFour fun i => sumFour fun j => v i * prepare minus i j * v j) =
      ((v zz + sgn minus * v oo)^2 + (v zo - sgn minus * v oz)^2) := by
  have entry := fun i j => (circuitMatrices minus i j).1
  cases minus <;> simp [sumFour,entry,ident,product,jForm,sgn,zz,zo,oz,oo] <;> integerPolynomial

/-- A classical control implementation first reads the control bit in Z
    and forgets it. This gives I/4 for *both* labelled preparations. -/
def readControlFirst (m : Mat Int Pair) : Mat Int Pair :=
  fun i j => if i.1 == j.1 then m i j else 0

theorem classicalControlErases (b : Bool) (i j : Pair) :
    interact (readControlFirst (localMix b)) i j = ident i j := by
  rcases i with ⟨a,c⟩; rcases j with ⟨d,e⟩
  cases b <;> cases a <;> cases c <;> cases d <;> cases e <;> decide +kernel

/-- Every finite classical mixture of independently prepared real states
    lies in this (larger) linear span; the statement makes no positivity or
    normalization assumption about its coefficients. -/
inductive ProductSpan : Mat Int Pair → Prop
  | prod (a b : Sym2 Int) : ProductSpan (product a.entry b.entry)
  | add {a b} : ProductSpan a → ProductSpan b → ProductSpan (fun i j => a i j + b i j)
  | scale (w : Int) {a} : ProductSpan a → ProductSpan (fun i j => w * a i j)

theorem productSpanCorners {m : Mat Int Pair}
    (h : ProductSpan m) : m zz oo = m zo oz := by
  induction h with
  | prod => rfl
  | add _ _ ha hb => simp only [ha,hb]
  | scale _ _ ha => simp only [ha]

theorem notLocallyPrepared (b : Bool) : ¬ProductSpan (prepare b) := by
  intro h
  have eq := productSpanCorners h
  cases b with
  | false => exact (by decide +kernel : prepare false zz oo ≠ prepare false zo oz) eq
  | true => exact (by decide +kernel : prepare true zz oo ≠ prepare true zo oz) eq

section ArbitraryDimensions
variable {A B R : Type} [Semiring R]

private local instance : Std.Associative (fun a b : R => a+b) := ⟨AddCommMonoid.add_assoc⟩
private local instance : Std.Commutative (fun a b : R => a+b) := ⟨AddCommMonoid.add_comm⟩

/-- Physical closure under arbitrary real local Kraus branches: the two
    nonzero opposite-corner coefficients of a signed difference cancel. This
    theorem is scalar-generic, including filters with irrational entries. -/
theorem oppositeCornersBlind (t u : R) (opposite : t+u=0) (event : LocalEvent R) :
    eventScore (⟨0,0,0,0,0,0,t,u,0,0⟩ : Sym4 R) event id id = 0 := by
  apply eventBlind
  intro a b
  simp only [localValue,born,sumFour,product,Sym2.entry,Sym4.entry,
    Semiring.mul_zero,Semiring.add_zero,AddCommMonoid.zero_add]
  let w := a.cross*b.cross
  calc
    _ = (w*t+w*u) + (w*t+w*u) := by dsimp only [w]; ac_rfl
    _ = 0 := by rw [← Semiring.left_distrib,opposite,Semiring.mul_zero,Semiring.add_zero]

/-- x+x=0 implies x=0 over the real numbers and every field of
    characteristic other than two. This is the only scalar cancellation
    needed by the kernel proof. -/
def DoubleCancel (R : Type) [Semiring R] := ∀ x : R, x+x=0 → x=0

/-- Unnormalized expectation at e_i+e_k. Repeating an index yields four
    times its diagonal entry. For distinct indices it is twice the physical
    plus-projector score. -/
def plusValue {I : Type} (m : Mat R I) (i k : I) :=
  m i i + m i k + m k i + m k k

def rectangleValue (d : A → A → B → B → R) (i k : A) (j l : B) :=
  plusValue (fun a c => plusValue (d a c) j l) i k

private theorem polarize {I : Type} (cancel : DoubleCancel R) (m : Mat R I) :
    (∀ i k, plusValue m i k = 0) ↔ (∀ i k, m i k + m k i = 0) := by
  constructor
  · intro h
    have diag (i : I) : m i i = 0 := by
      apply cancel
      apply cancel
      calc
        _ = plusValue m i i := by unfold plusValue; ac_rfl
        _ = 0 := h i i
    intro i k
    simpa only [plusValue,diag,AddCommMonoid.zero_add,Semiring.add_zero] using h i k
  · intro h i k
    have hi := cancel _ (h i i)
    have hk := cancel _ (h k k)
    simp only [plusValue,hi,hk,AddCommMonoid.zero_add,Semiring.add_zero,h]

private theorem plusAdd {I : Type} (f g : Mat R I) (i k : I) :
    plusValue (fun a b => f a b + g a b) i k =
    plusValue f i k + plusValue g i k := by
  simp only [plusValue]
  ac_rfl

/-- A jointly symmetric difference D_{ij,kl} is blind to all local product
    plus-projectors exactly when its partial transpose in the first port
    negates it. Joint symmetry gives the same statement on the second port.
    Double polarization proves this for any two index types. -/
theorem productKernelIffPartialTranspose (cancel : DoubleCancel R)
    (d : A → A → B → B → R) (sym : ∀ i k j l, d i k j l = d k i l j) :
    (∀ i k j l, rectangleValue d i k j l = 0) ↔
      (∀ i k j l, d i k j l + d k i j l = 0) := by
  constructor
  · intro dark i k j l
    have first (b v : B) :=
      (polarize cancel (fun a c => plusValue (d a c) b v)).1 (fun a c => dark a c b v) i k
    have second := (polarize cancel (fun b v => d i k b v + d k i b v)).1
      (fun b v => (plusAdd (d i k) (d k i) b v).trans (first b v)) j l
    apply cancel
    calc
      _ = (d i k j l + d k i j l) + (d i k l j + d k i l j) := by
        rw [sym i k l j, ← sym i k j l]
        ac_rfl
      _ = 0 := second
  · intro skew i k j l
    apply (polarize cancel (fun a c => plusValue (d a c) j l)).2 _ i k
    intro a c
    rw [← plusAdd]
    simp only [plusValue,skew,AddCommMonoid.zero_add]

private def sumOn {I : Type} (xs : List I) (f : I → R) : R :=
  match xs with
  | [] => 0
  | x :: rest => f x + sumOn rest f

private theorem sumOnAdd {I : Type} (xs : List I) (f g : I → R) :
    sumOn xs (fun i => f i + g i) = sumOn xs f + sumOn xs g := by
  induction xs with
  | nil => simp only [sumOn,AddCommMonoid.zero_add]
  | cons x xs ih => simp only [sumOn,ih]; ac_rfl

private theorem sumOnZero {I : Type} (xs : List I) (f : I → R)
    (h : ∀ i, f i = 0) : sumOn xs f = 0 := by
  induction xs with
  | nil => rfl
  | cons x xs ih => simp only [sumOn,ih,h,AddCommMonoid.zero_add]

private theorem alternatingSum {I : Type} (cancel : DoubleCancel R)
    (xs : List I) (f : I → I → R) (skew : ∀ i k, f i k + f k i = 0) :
    sumOn xs (fun i => sumOn xs (f i)) = 0 := by
  induction xs with
  | nil => rfl
  | cons x xs ih =>
    change f x x + sumOn xs (f x) +
      sumOn xs (fun i => f i x + sumOn xs (f i)) = 0
    rw [sumOnAdd,ih,cancel _ (skew x x),AddCommMonoid.zero_add,Semiring.add_zero,← sumOnAdd]
    exact sumOnZero xs _ (fun i => skew x i)

/-- Entrywise matrix pairing on lists enumerating each local basis. -/
def productScore (as : List A) (bs : List B) (d : A → A → B → B → R)
    (e : Mat R A) (f : Mat R B) :=
  sumOn bs fun j => sumOn bs fun l =>
    sumOn as fun i => sumOn as fun k => e i k * f j l * d i k j l

/-- Darkness on the physical coordinate and superposition probes suffices
    for darkness on every product of real symmetric local measurements. -/
theorem arbitraryProductsBlind (cancel : DoubleCancel R) (as : List A) (bs : List B)
    (d : A → A → B → B → R) (sym : ∀ i k j l, d i k j l = d k i l j)
    (dark : ∀ i k j l, rectangleValue d i k j l = 0)
    (e : Mat R A) (f : Mat R B) (eSym : ∀ i k, e i k = e k i) :
    productScore as bs d e f = 0 := by
  have skew := (productKernelIffPartialTranspose cancel d sym).1 dark
  apply sumOnZero
  intro j
  apply sumOnZero
  intro l
  apply alternatingSum cancel
  intro i k
  change e i k * f j l * d i k j l + e k i * f j l * d k i j l = 0
  rw [eSym i k,← Semiring.left_distrib,skew,Semiring.mul_zero]

end ArbitraryDimensions
end OperationalNetwork.Rebit
