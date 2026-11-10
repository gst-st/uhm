import Std
set_option autoImplicit false
namespace OperationalNetwork.PracticeOverlap

/-- Raw integer weights; probabilities divide the Born weight by the two
    preparation masses. Gaussian-rational amplitudes are represented by
    clearing denominators, so normalization need not take square roots. -/
structure Spinor where
  a : Int
  b : Int
  c : Int
  d : Int
deriving DecidableEq

structure Vec where
  x : Int
  y : Int
  z : Int
deriving DecidableEq

def dot (u v : Vec) := u.x*v.x + u.y*v.y + u.z*v.z
def mass (s : Spinor) := s.a*s.a+s.b*s.b+s.c*s.c+s.d*s.d
def weight (s t : Spinor) :=
  let re := s.a*t.a+s.b*t.b+s.c*t.c+s.d*t.d
  let im := s.a*t.b-s.b*t.a+s.c*t.d-s.d*t.c
  re*re+im*im

def bloch (s : Spinor) : Vec :=
  ⟨2*(s.a*s.c+s.b*s.d),2*(s.a*s.d-s.b*s.c),s.a*s.a+s.b*s.b-s.c*s.c-s.d*s.d⟩

def opposite (s : Spinor) : Spinor := ⟨-s.c,s.d,s.a,-s.b⟩

private theorem bornIdentity (s t : Spinor) :
    2*weight s t = mass s * mass t + dot (bloch s) (bloch t) := by
  have twice (u : Int) : u*2=u+u := by omega
  simp only [weight,mass,bloch,dot,twice,Int.mul_add,Int.mul_sub,Int.mul_comm,Int.mul_left_comm]
  omega

theorem sameIfBothNegative (s t : Spinor) :
    weight (opposite s) (opposite t)=weight s t ∧ mass (opposite s)=mass s := by
  constructor
  · simp [weight,opposite,Int.mul_add,Int.mul_sub,Int.mul_neg,Int.mul_comm,Int.mul_left_comm] <;> omega
  · simp [mass,opposite,Int.neg_mul,Int.mul_neg,Int.add_comm,Int.add_left_comm,Int.add_assoc]

theorem otherOutcome (s t : Spinor) : weight s t + weight s (opposite t) = mass s * mass t := by
  simp [weight,mass,opposite,Int.mul_add,Int.mul_sub,Int.mul_neg,Int.mul_comm,Int.mul_left_comm] <;> omega

/-- After either outcome has prepared its eigenstate, the same readout
    repeated with identity evolution agrees with probability one. -/
theorem repeatAgreement (s : Spinor) : weight s s = mass s * mass s := by
  simp [weight,mass,Int.mul_comm]

private theorem blochLength (s : Spinor) : dot (bloch s) (bloch s) = mass s * mass s := by
  have born := bornIdentity s s
  rw [repeatAgreement] at born
  omega

/-- The nonnegative squared length of 5u - 8v + 5w, written one coordinate
    at a time. This tangent at adjacent agreement 0.90 stays linear when
    participants with different directions are mixed using common weights. -/
private theorem squareWitness (a b c : Int) :
    0 ≤ 25*(a*a)+64*(b*b)+25*(c*c)+50*(a*c)-80*(a*b+b*c) := by
  have scale (k l x y : Int) : (k*x)*(l*y)=(k*l)*(x*y) := by ac_rfl
  have pos := Int.sq_nonneg (5*a-8*b+5*c)
  rw [Int.pow_succ,Int.pow_one] at pos
  simp only [Int.add_mul,Int.sub_mul,Int.mul_add,Int.mul_sub] at pos
  simp only [scale 5 5 a a,scale 5 8 a b,scale 5 5 a c,scale 8 5 b a,scale 8 8 b b,scale 8 5 b c,
    scale 5 5 c a,scale 5 8 c b,scale 5 5 c c] at pos
  rw [Int.mul_comm b a,Int.mul_comm c a,Int.mul_comm c b] at pos
  omega

private def scale (k : Int) (v : Vec) : Vec := ⟨k*v.x,k*v.y,k*v.z⟩

private theorem dotScales (k l : Int) (u v : Vec) :
    dot (scale k u) (scale l v) = (k*l)*dot u v := by
  simp only [dot,scale,Int.mul_add]
  ac_rfl

private theorem vecWitness (u v w : Vec) :
    80*(dot u v+dot v w) ≤ 25*dot u u+64*dot v v+25*dot w w+50*dot u w := by
  have x := squareWitness u.x v.x w.x
  have y := squareWitness u.y v.y w.y
  have z := squareWitness u.z v.z w.z
  simp only [dot]; omega

/-- Common denominator L=mass a * mass b * mass c. Cross-multiply each
    observed agreement separately. The three raw spinors can have different
    lengths and complex entries. No fit of the outer pair occurs. -/
private theorem pairScaled (a b : Spinor) (t : Int) :
    dot (scale (mass b*t) (bloch a)) (scale (mass a*t) (bloch b)) +
      (mass a*mass b*t)*(mass a*mass b*t) =
      2*((mass a*mass b*t)*(weight a b*t)) := by
  rw [dotScales]
  have h := congrArg (fun v => ((mass b*t)*(mass a*t))*v) (bornIdentity a b).symm
  rw [Int.mul_add] at h
  calc
    _ = ((mass b*t)*(mass a*t))*(mass a*mass b) +
        ((mass b*t)*(mass a*t))*dot (bloch a) (bloch b) := by ac_rfl
    _ = _ := h
    _ = _ := by ac_rfl

theorem bornTangent (a b c : Spinor) (ha : 0<mass a) (hb : 0<mass b) (hc : 0<mass c) :
    40*(weight a b*mass c+weight b c*mass a) ≤
      25*(weight a c*mass b)+56*(mass a*mass b*mass c) := by
  let L := mass a*mass b*mass c
  let u := scale (mass b*mass c) (bloch a)
  let v := scale (mass a*mass c) (bloch b)
  let w := scale (mass a*mass b) (bloch c)
  have len (p : Spinor) (k : Int) : dot (scale k (bloch p)) (scale k (bloch p)) = (k*mass p)*(k*mass p) := by
    rw [dotScales,blochLength]; ac_rfl
  have hu : dot u u=L*L := by dsimp [u,L]; rw [len]; ac_rfl
  have hv : dot v v=L*L := by dsimp [v,L]; rw [len]; ac_rfl
  have hw : dot w w=L*L := by dsimp [w,L]; rw [len]
  have ab : dot u v + L*L = 2*(L*(weight a b*mass c)) := pairScaled a b (mass c)
  have bc : dot v w + L*L = 2*(L*(weight b c*mass a)) := by
    simpa only [u,v,w,L,Int.mul_comm,Int.mul_assoc,Int.mul_left_comm] using pairScaled b c (mass a)
  have ac : dot u w + L*L = 2*(L*(weight a c*mass b)) := by
    simpa only [u,v,w,L,Int.mul_comm,Int.mul_assoc,Int.mul_left_comm] using pairScaled a c (mass b)
  have cert := vecWitness u v w
  rw [hu,hv,hw] at cert
  apply Int.le_of_mul_le_mul_left (a:=L) _ (Int.mul_pos (Int.mul_pos ha hb) hc)
  change L*(40*(_+_)) ≤ L*(25*_+56*L)
  simp only [Int.mul_add,Int.mul_left_comm L 25,Int.mul_left_comm L 56,Int.mul_left_comm L 40]
  omega

/-- The lower bound 16/25 holds when each adjacent agreement is at least
    9/10, in calibrated trials with both outcomes retained. -/
theorem heldOutLowerBound (a b c : Spinor) (ha : 0<mass a) (hb : 0<mass b) (hc : 0<mass c)
    (ab : 9*(mass a*mass b) ≤ 10*weight a b) (bc : 9*(mass b*mass c) ≤ 10*weight b c) :
    16*(mass a*mass c) ≤ 25*weight a c := by
  have h := bornTangent a b c ha hb hc
  have one := Int.mul_le_mul_of_nonneg_right ab (Int.le_of_lt hc)
  have two := Int.mul_le_mul_of_nonneg_right bc (Int.le_of_lt ha)
  rw [Int.mul_assoc 9,Int.mul_assoc 10] at one two
  rw [show mass b*mass c*mass a=mass a*mass b*mass c by ac_rfl] at two
  apply Int.le_of_mul_le_mul_left (a:=mass b) _ hb
  rw [Int.mul_left_comm (mass b) 16,Int.mul_left_comm (mass b) 25,
    show mass b*(mass a*mass c)=mass a*mass b*mass c by ac_rfl,
    Int.mul_comm (mass b) (weight a c)]
  omega

theorem tightTriple :
    let a : Spinor := ⟨3,0,1,0⟩
    let b : Spinor := ⟨1,0,0,0⟩
    let c : Spinor := ⟨3,0,-1,0⟩
    10*weight a b = 9*(mass a*mass b) ∧ 10*weight b c = 9*(mass b*mass c) ∧
      25*weight a c = 16*(mass a*mass c) := by decide

/-- The passive-record rival. Each trial carries a single pre-existing
    triple; the pair order/asking has no effect. This is pointwise and
    therefore holds after any nonnegative common mixture over triples. -/
theorem passiveTriangle (a b c : Bool) :
    (if a=b then 1 else 0) + (if b=c then 1 else 0) ≤
      1+(if a=c then 1 else 0 : Nat) := by cases a <;> cases b <;> cases c <;> decide

end OperationalNetwork.PracticeOverlap
