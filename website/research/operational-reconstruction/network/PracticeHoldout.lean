import PracticeOverlap

set_option autoImplicit false
namespace OperationalNetwork.PracticeHoldout

structure Amplitude where
  matchAxis : Int
  otherAxis : Int
deriving DecidableEq

def energy (z : Amplitude) := z.matchAxis*z.matchAxis + z.otherAxis*z.otherAxis

/-- Homogeneous real amplitudes: divide by sqrt(a²+b²) for a normalized
    rotation. No divisions occur in any of the probability comparisons. -/
def turn (a b : Int) (z : Amplitude) : Amplitude :=
  ⟨a*z.matchAxis - b*z.otherAxis,b*z.matchAxis + a*z.otherAxis⟩

def initial : Amplitude := ⟨1,0⟩

theorem energyScales (a b : Int) (z : Amplitude) :
    energy (turn a b z) = (a*a+b*b)*energy z := by
  simp only [energy,turn,Int.mul_add,Int.mul_sub,
    Int.mul_comm,Int.mul_left_comm]
  omega

def overlap (x y : Amplitude) := x.matchAxis*y.matchAxis + x.otherAxis*y.otherAxis

/-- The neighboring-axis match probability really is the same at both
    steps: for any nonzero starting ray it equals a²/(a²+b²).
    The statement cross-multiplies the probability denominators. -/
theorem identicalAdjacentMatch (a b : Int) (z : Amplitude) :
    (a*a+b*b)*(overlap z (turn a b z)*overlap z (turn a b z)) =
      (a*a)*(energy z*energy (turn a b z)) := by
  have dotLaw : overlap z (turn a b z) = a*energy z := by
    simp only [overlap,turn,energy,Int.mul_add,Int.mul_sub,Int.mul_comm,Int.mul_left_comm]
    omega
  rw [dotLaw,energyScales]
  ac_rfl

/-- The intermediate axis is passed with no intermediate measurement. For
    adjacent numerator m=a², n=b², the two-turn match probability is
    (m−n)²/(m+n)². This assumes the SAME signed turn twice. -/
theorem coherentReadout (a b : Int) :
    let first := turn a b initial
    let last := turn a b first
    first.matchAxis*first.matchAxis = a*a ∧ energy first = a*a+b*b ∧
      last.matchAxis = a*a-b*b ∧ energy last = (a*a+b*b)*(a*a+b*b) := by
  dsimp only
  have first : energy (turn a b initial) = a*a+b*b := by simp [energy,turn,initial]
  exact ⟨by simp [turn,initial],first,by simp [turn,initial],by rw [energyScales,first]⟩

theorem reversedSecondTurn (a b : Int) :
    turn a (-b) (turn a b initial) = ⟨a*a+b*b,0⟩ := by
  simp [turn,initial,Int.mul_comm,Int.mul_neg] <;> omega

/-- Cover *every* rational adjacent probability m/(m+n), even if m/n is
    not a square of a rational amplitude ratio. Coordinates (x,y) describe
    the real vector (x,sqrt(m*n)*y); for m,n>0 this is a nondegenerate
    orthogonal chart. Under that embedding, this is one and the same real
    turn with coefficients (m,sqrt(m*n)), up to normalization. -/
def weightedEnergy (m n : Int) (z : Amplitude) := z.matchAxis*z.matchAxis + (m*n)*(z.otherAxis*z.otherAxis)
def rationalTurn (m n : Int) (z : Amplitude) : Amplitude :=
  ⟨m*z.matchAxis-(m*n)*z.otherAxis,z.matchAxis+m*z.otherAxis⟩

theorem rationalTurnScales (m n : Int) (z : Amplitude) :
    weightedEnergy m n (rationalTurn m n z) = (m*(m+n))*weightedEnergy m n z := by
  simp only [weightedEnergy,rationalTurn,Int.mul_add,Int.mul_sub,Int.mul_left_comm,
    Int.mul_comm]
  omega

theorem allRationalDirect (m n : Int) :
    let one := rationalTurn m n initial
    let two := rationalTurn m n one
    one.matchAxis*one.matchAxis*(m+n) = m*weightedEnergy m n one ∧
    two.matchAxis*two.matchAxis*((m+n)*(m+n)) = ((m-n)*(m-n))*weightedEnergy m n two := by
  let u := m*(m+n)
  have w : weightedEnergy m n (rationalTurn m n initial) = u := by
    rw [rationalTurnScales]; simp [weightedEnergy,initial,u]
  have v : (rationalTurn m n (rationalTurn m n initial)).matchAxis=m*(m-n) := by
    simp [rationalTurn,initial,Int.mul_sub]
  dsimp only
  constructor
  · rw [w]; simp only [u,rationalTurn,initial,Int.mul_one,Int.mul_zero,Int.sub_zero]; ac_rfl
  · rw [v,rationalTurnScales,w]; dsimp only [u]; ac_rfl

/-- Independent Bernoulli ticket counts for the two adjacent comparisons.
    In SAME outcomes both transitions match or both mismatch; OPPOSITE counts
    their two distinct orders. Total mass is the Cartesian product. -/
structure PairTable where
  yesYes : Nat
  yesNo : Nat
  noYes : Nat
  noNo : Nat
deriving DecidableEq

def independent (m n u v : Nat) : PairTable := ⟨m*u,m*v,n*u,n*v⟩
def total (t : PairTable) := t.yesYes+t.yesNo+t.noYes+t.noNo
def equalBits (t : PairTable) := t.yesYes+t.noNo
def productScore (t : PairTable) := (t.yesYes:Int)+t.noNo-t.yesNo-t.noYes

theorem independentReadout (m n u v : Nat) :
    total (independent m n u v) = (m+n)*(u+v) ∧
    equalBits (independent m n u v) = m*u+n*v ∧
    productScore (independent m n u v) = ((m:Int)-n)*((u:Int)-v) := by
  constructor
  · simp only [total, independent, Nat.mul_add,Nat.add_mul]; omega
  · exact ⟨rfl,by simp only [productScore,independent,Int.natCast_mul,Int.sub_mul,Int.mul_sub]; omega⟩

/-- Exact gap of competing direct-match probabilities in a homogeneous
    subject, with denominator (m+n)². A live denominator is required when
    interpreting this as a probability. -/
theorem rivalGap (m n : Nat) :
    (equalBits (independent m n m n) : Int) - ((m:Int)-n)*((m:Int)-n) = 2*(m:Int)*n := by
  rw [show 2*(m:Int)*n=(m:Int)*n+(m:Int)*n by rw [Int.mul_assoc]; omega]
  simp only [equalBits,independent,Int.natCast_add,Int.natCast_mul,Int.mul_sub,Int.mul_comm]
  omega

theorem rivalEqualityIff (m n : Nat) :
    ((equalBits (independent m n m n) : Int) = ((m:Int)-n)*((m:Int)-n)) ↔ m=0 ∨ n=0 := by
  have h := rivalGap m n
  constructor
  · intro eq
    rw [eq,Int.sub_self] at h
    have zero : (2*(m:Int))*(n:Int)=0 := h.symm
    rcases Int.mul_eq_zero.mp zero with hm | hn
    · left; omega
    · right; omega
  · rintro (rfl|rfl) <;> simp_all <;> omega

/-- Finite mixture with a common within-person trial denominator, or after
    clearing all rational denominators. Weight refers to participants, not
    to a reweighted frequency of answered trials. Within-person product
    scores survive heterogeneity; squaring a pooled mean need not. -/
structure Participant where
  weight : Nat
  matchTickets : Nat
  otherTickets : Nat

def weighted (read : Participant → Int) : List Participant → Int
  | [] => 0
  | p::ps => (p.weight:Int)*read p+weighted read ps

def personTable (p : Participant) := independent p.matchTickets p.otherTickets p.matchTickets p.otherTickets
def scaledScore (p : Participant) := ((p.matchTickets:Int)-p.otherTickets)*((p.matchTickets:Int)-p.otherTickets)

theorem conditionalCalibration (people : List Participant) :
    weighted (fun p => productScore (personTable p)) people = weighted scaledScore people ∧
    2 * weighted (fun p => (equalBits (personTable p):Int)) people =
      weighted (fun p => (total (personTable p):Int)) people + weighted scaledScore people := by
  have signed (p : Participant) : productScore (personTable p) = scaledScore p :=
    (independentReadout _ _ _ _).2.2
  have eqCount (t : PairTable) : 2*(equalBits t:Int) = (total t:Int)+productScore t := by
    simp only [equalBits,total,productScore,Int.natCast_add]; omega
  induction people with
  | nil => decide
  | cons p ps ih =>
    have h := eqCount (personTable p)
    have newTerm := congrArg (fun x => (p.weight:Int)*x) h
    rw [signed] at newTerm
    simp only [Int.mul_add,Int.mul_left_comm (p.weight:Int) 2] at newTerm
    obtain ⟨one,two⟩ := ih
    constructor
    · simp only [weighted,signed]
    · simp only [weighted]; omega

/-- Equal adjacent marginals (9 out of 10 in each epoch) do not certify
    independent calibration. In the correlated table a common latent
    nuisance makes the two success indicators identical. -/
theorem correlatedCalibrationControl :
    let p := independent 9 1 9 1
    let correlated : PairTable := ⟨90,0,0,10⟩
    total p = 100 ∧ total correlated = 100 ∧
      p.yesYes+p.yesNo = correlated.yesYes+correlated.yesNo ∧
      p.yesYes+p.noYes = correlated.yesYes+correlated.noYes ∧
      productScore p = 64 ∧ productScore correlated = 100 := by decide

theorem heterogeneousControl :
    let mix : List Participant := [⟨1,1,0⟩,⟨1,0,1⟩]
    weighted (fun p => (p.matchTickets:Int)-p.otherTickets) mix = 0 ∧
      weighted (fun p => productScore (personTable p)) mix = 2 := by decide

/-- One exact equal-mass realization in the very spinor model of the overlap
    bound. B=(3+i)(3,1) represents a real ray with a common phase chosen to
    clear denominators. Raw Born probabilities divide weights by 100². -/
theorem heldOutNinety :
    let a : PracticeOverlap.Spinor := ⟨10,0,0,0⟩
    let b : PracticeOverlap.Spinor := ⟨9,3,3,1⟩
    let c : PracticeOverlap.Spinor := ⟨8,0,6,0⟩
    PracticeOverlap.mass a=100 ∧ PracticeOverlap.mass b=100 ∧ PracticeOverlap.mass c=100 ∧
      PracticeOverlap.weight a b=9000 ∧ PracticeOverlap.weight b c=9000 ∧
      PracticeOverlap.weight a c=6400 ∧ equalBits (independent 9 1 9 1)=82 ∧
      (turn 3 (-1) (turn 3 1 initial))=⟨10,0⟩ := by decide

/-- Six equiprobable late-cue tickets: three request the whole word and
    one requests each bit. Centering and inverse selection weights recover
    the whole-word loss and the shared-word contrast for any raw loss
    vector, even one which depends on all earlier trials. No trial quotas. -/
theorem sixTicketReadout (whole first middle last : Int) :
    3*(1-2*whole) + 1+1+1 = 6*(1-whole) ∧
    3*(-2*whole) + 6*first + 6*middle + 6*last = 6*(first+middle+last-whole) := by
  constructor <;> omega

/-- Pointwise, a misreported full word must contain at least one bad bit
    when all four readouts come from a common prediction. -/
theorem sharedWordLoss (a b c : Bool) :
    (if a || b || c then (1:Int) else 0) ≤
    (if a then 1 else 0)+(if b then 1 else 0)+(if c then 1 else 0) := by
  cases a <;> cases b <;> cases c <;> decide

end OperationalNetwork.PracticeHoldout
