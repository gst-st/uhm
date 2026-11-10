import Std
set_option autoImplicit false

namespace OperationalNetwork.SevenReadout

/-- Unnormalized Gaussian integer amplitudes; positive rational mixtures and
    rank-one effects with a common denominator can be represented by repeated
    terms and clearing positive denominators. -/
structure G where
  re : Int
  im : Int
deriving DecidableEq

def total {X : Type} (xs : List X) (f : X → Int) := (xs.map f).sum

private theorem sumAdd {X : Type} (xs : List X) (f g : X → Int) :
    total xs (fun x => f x + g x) = total xs f + total xs g := by
  induction xs with
  | nil => rfl
  | cons x xs ih => simp only [total,List.map_cons,List.sum_cons] at *; omega

private theorem sumScale {X : Type} (xs : List X) (k : Int) (f : X → Int) :
    total xs (fun x => k*f x) = k*total xs f := by
  induction xs with
  | nil => simp [total]
  | cons x xs ih => simp only [total,List.map_cons,List.sum_cons,Int.mul_add] at *; omega

private theorem sumScaleRight {X : Type} (xs : List X) (f : X → Int) (k : Int) :
    total xs (fun x => f x*k) = total xs f*k := by
  simpa only [Int.mul_comm k] using sumScale xs k f

private theorem sumMono {X : Type} (xs : List X) (f g : X → Int) (h : ∀ x, f x ≤ g x) :
    total xs f ≤ total xs g := by
  induction xs with
  | nil => exact Int.le_refl _
  | cons x xs ih => exact Int.add_le_add (h x) ih

private theorem sumZero {X : Type} (xs : List X) : total xs (fun _ => 0) = 0 := by
  induction xs with
  | nil => rfl
  | cons x xs ih => simpa only [total,List.map_cons,List.sum_cons,Int.zero_add] using ih

private theorem exchange {X Y : Type} (xs : List X) (ys : List Y) (f : X → Y → Int) :
    total xs (fun x => total ys (f x)) = total ys (fun y => total xs (fun x => f x y)) := by
  induction xs with
  | nil => exact (sumZero ys).symm
  | cons x xs ih =>
    change total ys (f x) + total xs (fun v => total ys (f v)) =
      total ys (fun y => f x y + total xs (fun v => f v y))
    rw [sumAdd, ih]

def sq (a : G) := a.re*a.re + a.im*a.im
def innerRe (a b : G) := a.re*b.re + a.im*b.im
def innerIm (a b : G) := a.re*b.im - a.im*b.re

/-- The squared modulus of a two-coordinate minor certifies the inequality.
    This permits arbitrary phases, including destructive cross terms. -/
private theorem minor (a b c d : G) :
    2*(innerRe a b*innerRe c d + innerIm a b*innerIm c d) ≤ sq a*sq d + sq c*sq b := by
  have h₁ := Int.sq_nonneg (a.re*d.re-a.im*d.im-c.re*b.re+c.im*b.im)
  have h₂ := Int.sq_nonneg (a.re*d.im+a.im*d.re-c.re*b.im-c.im*b.re)
  rw [Int.pow_succ,Int.pow_one] at h₁ h₂
  have h := Int.add_le_add h₁ h₂
  rw [Int.two_mul]
  simp only [sq,innerRe,innerIm,Int.mul_add,Int.mul_sub,
             Int.mul_comm,Int.mul_left_comm] at h ⊢
  omega

def energy {X : Type} (xs : List X) (v : X → G) := total xs (fun x => sq (v x))
def overlap {X : Type} (xs : List X) (a b : X → G) :=
  let r := total xs (fun x => innerRe (a x) (b x))
  let i := total xs (fun x => innerIm (a x) (b x))
  r*r+i*i

theorem bornCauchy {X : Type} (xs : List X) (a b : X → G) :
    overlap xs a b ≤ energy xs a * energy xs b := by
  let r x := innerRe (a x) (b x)
  let i x := innerIm (a x) (b x)
  let p x := sq (a x)
  let q x := sq (b x)
  have bound := sumMono xs _ _ (fun x => sumMono xs _ _ (fun y => minor (a x) (b x) (a y) (b y)))
  change total xs (fun x => total xs (fun y => 2*(r x*r y+i x*i y))) ≤
    total xs (fun x => total xs (fun y => p x*q y+p y*q x)) at bound
  simp only [sumScale,sumAdd,sumScaleRight] at bound
  change total xs r * total xs r + total xs i * total xs i ≤ total xs p * total xs q
  omega

abbrev Index := Fin 7
abbrev State := Index → G
def basis : List Index := List.finRange 7

/-- Each vector is an unnormalized pure component of the prepared mixture,
    or an unnormalized positive rank-one component of an effect. -/
def mixtureMass (prep : List State) := total prep (energy basis)
def effectTrace (effect : List State) := total effect (energy basis)
def outcomeWeight (prep effect : List State) :=
  total prep (fun v => total effect (fun w => overlap basis v w))

theorem outcomeBound (prep effect : List State) :
    outcomeWeight prep effect ≤ mixtureMass prep * effectTrace effect := by
  have bound := sumMono prep _ _ (fun v => sumMono effect _ _ (fun w => bornCauchy basis v w))
  simpa only [outcomeWeight,mixtureMass,effectTrace,sumScale,sumScaleRight] using bound

def axis (j : Index) : State := fun k => if j=k then ⟨1,0⟩ else ⟨0,0⟩

private def occurrences {X : Type} [DecidableEq X] (xs : List X) (k : X) : Int :=
  total xs (fun i => if k=i then 1 else 0)

private theorem sumSingle {X : Type} [DecidableEq X] (xs : List X) (k : X) (f : X → Int) :
    total xs (fun i => if k=i then f i else 0) = occurrences xs k*f k := by
  induction xs with
  | nil => simp [occurrences,total]
  | cons a as ih =>
    change (if k=a then f a else 0) + total as (fun i => if k=i then f i else 0) =
      ((if k=a then 1 else 0) + occurrences as k)*f k
    rw [ih,Int.add_mul]
    cases (inferInstance : Decidable (k=a)) with
    | isTrue h => simp [h]
    | isFalse h => simp [h]

private theorem axisOverlap (j : Index) (w : State) : overlap basis (axis j) w = sq (w j) := by
  have count (k : Index) : occurrences basis k=1 := by revert k; decide
  have re (k : Index) : innerRe (axis j k) (w k) = if j=k then (w k).re else 0 := by
    cases (inferInstance : Decidable (j=k)) with
    | isTrue h => simp [axis,innerRe,h]
    | isFalse h => simp [axis,innerRe,h]
  have im (k : Index) : innerIm (axis j k) (w k) = if j=k then (w k).im else 0 := by
    cases (inferInstance : Decidable (j=k)) with
    | isTrue h => simp [axis,innerIm,h]
    | isFalse h => simp [axis,innerIm,h]
  simp only [overlap,re,im,sumSingle,count,Int.one_mul,sq]

abbrev Label := Fin 8
def labels : List Label := List.finRange 8

/-- Only the diagonal consequence of POVM completeness is needed: a
    calibration on each unit axis distributes its full weight. -/
def calibrated (effects : Label → List State) (D : Int) :=
  ∀ j : Index, total labels (fun i => total (effects i) (fun w => overlap basis (axis j) w)) = D

theorem traceBudget (effects : Label → List State) (D : Int) (h : calibrated effects D) :
    total labels (fun i => effectTrace (effects i)) = 7*D := by
  have grouped : total labels (fun i => effectTrace (effects i)) =
      total basis (fun j => total labels (fun i => total (effects i) (fun w => sq (w j)))) := by
    rw [exchange]
    apply congrArg (total labels)
    funext i
    exact exchange (effects i) basis _
  rw [grouped]
  simp only [calibrated,axisOverlap] at h
  rw [show (fun j => total labels (fun i => total (effects i) (fun w => sq (w j)))) = fun _ => D from funext h]
  change D+(D+(D+(D+(D+(D+(D+0))))))=7*D
  omega

/-- N is a common reporting denominator, p i/N the conditional correct
    probability for label i. mass i may differ between preparations. Reports
    follow the normalized Born rule, cross-multiplied without rounding. The
    uniform eight-label success is therefore at most 7/8. -/
theorem eightLabelsSeven (prep effects : Label → List State) (D N : Int)
    (hd : 0<D) (hn : 0<N) (hm : ∀ i, 0<mixtureMass (prep i)) (measure : calibrated effects D)
    (p : Label → Int) (born : ∀ i, mixtureMass (prep i)*(p i*D) = N*outcomeWeight (prep i) (effects i)) :
    total labels p ≤ 7*N := by
  have point (i : Label) : p i*D ≤ N*effectTrace (effects i) := by
    apply Int.le_of_mul_le_mul_left (a:=mixtureMass (prep i)) _ (hm i)
    rw [born, Int.mul_left_comm (mixtureMass (prep i))]
    exact Int.mul_le_mul_of_nonneg_left (outcomeBound (prep i) (effects i)) (Int.le_of_lt hn)
  have bound := sumMono labels _ _ point
  rw [sumScaleRight,sumScale,traceBudget _ _ measure] at bound
  apply Int.le_of_mul_le_mul_right (a:=D) _ hd
  simpa only [Int.mul_assoc,Int.mul_left_comm,Int.mul_comm] using bound



private theorem totalMap {X Y : Type} (xs : List X) (g : X → Y) (f : Y → Int) :
    total (xs.map g) f = total xs (fun x => f (g x)) := by
  simp [total,List.map_map,Function.comp_def]

private theorem totalAppend {X : Type} (xs ys : List X) (f : X → Int) :
    total (xs++ys) f = total xs f + total ys f := by
  simp [total,List.sum_append]

private theorem totalFlat {X Y : Type} (xs : List X) (g : X → List Y) (f : Y → Int) :
    total xs (fun x => total (g x) f) = total (xs.flatMap g) f := by
  induction xs with
  | nil => rfl
  | cons a as ih =>
    change total (g a) f + total as (fun x => total (g x) f) =
      total (g a ++ as.flatMap g) f
    rw [totalAppend,ih]

private theorem overlapAxis (v : State) (j : Index) : overlap basis v (axis j) = sq (v j) := by
  have count (k : Index) : occurrences basis k=1 := by revert k; decide
  have re (k : Index) : innerRe (v k) (axis j k) = if j=k then (v k).re else 0 := by
    cases (inferInstance : Decidable (j=k)) with
    | isTrue h => simp [axis,innerRe,h]
    | isFalse h => simp [axis,innerRe,h]
  have im (k : Index) : innerIm (v k) (axis j k) = if j=k then -(v k).im else 0 := by
    cases (inferInstance : Decidable (j=k)) with
    | isTrue h => simp [axis,innerIm,h]
    | isFalse h => simp [axis,innerIm,h]
  simp [overlap,re,im,sumSingle,count,sq,Int.neg_mul,Int.mul_neg]

def normalized (effects : Label → List State) (D : Int) :=
  ∀ v : State, total labels (fun i => total (effects i) (fun w => overlap basis v w)) = energy basis v * D

private theorem axisEnergy : ∀ j : Index, energy basis (axis j) = 1 := by decide

theorem normalizedIsCalibrated (effects : Label → List State) (D : Int) (h : normalized effects D) :
    calibrated effects D := by
  intro j
  simpa only [axisEnergy,Int.one_mul] using h (axis j)

private def decoded (i : Label) : List Index := if h : i.val<7 then [⟨i.val,h⟩] else []
def sharpEffects (i : Label) := (decoded i).map axis
def sharpPrep (i : Label) : List State := [axis ⟨i.val%7, Nat.mod_lt _ (by decide)⟩]
def sharpScore (i : Label) : Int := if i.val<7 then 1 else 0

/-- Seven orthogonal preparations and a duplicate, with the eighth measurement
    effect zero. This measurement normalizes on *every* vector. -/
theorem sharpNormalized : normalized sharpEffects 1 := by
  intro v
  simp only [sharpEffects,totalMap,overlapAxis,totalFlat,Int.mul_one]
  have all : labels.flatMap decoded = basis := by decide
  rw [all]
  rfl

theorem eightLabelsSharp :
    (∀ i : Label, mixtureMass (sharpPrep i) = 1 ∧ outcomeWeight (sharpPrep i) (sharpEffects i) = sharpScore i) ∧
    total labels sharpScore = 7 := by decide

def threeBits (i : Label) := (i.val.testBit 0,i.val.testBit 1,i.val.testBit 2)
def decodeBits (b : Bool × Bool × Bool) : Nat :=
  (if b.1 then 1 else 0) + (if b.2.1 then 2 else 0) + (if b.2.2 then 4 else 0)

theorem classicalReadout :
    (∀ i : Label, decodeBits (threeBits i) = i.val) ∧
    total labels (fun i => if decodeBits (threeBits i) = i.val then 1 else 0) = 8 := by decide

abbrev Entry := Index × Index
abbrev Matrix := Index → Index → G
def hermitian (m : Matrix) := ∀ i j, (m j i).re = (m i j).re ∧ (m j i).im = -(m i j).im
def entries : List Entry := basis.flatMap (fun i => basis.map (fun j => (i,j)))
def upper := entries.filter (fun ij => ij.1.val < ij.2.val)
private def grouped := basis.map (fun i => (i,i)) ++ (upper ++ upper.map Prod.swap)

private theorem regroupEntries (f : Entry → Int) : total entries f = total grouped f := by
  have oneL : ∀ i j, occurrences entries (i,j) = 1 := by decide
  have oneR : ∀ i j, occurrences grouped (i,j) = 1 := by decide
  let delta (t k : Entry) := if t=k then f k else 0
  have row (t : Entry) : total grouped (delta t) = f t := by
    rcases t with ⟨i,j⟩
    simp only [delta,sumSingle,oneR,Int.one_mul]
  have col (k : Entry) : total entries (fun t => delta t k) = f k := by
    have swap (t : Entry) : delta t k = if k=t then f t else 0 := by
      cases (inferInstance : Decidable (t=k)) with
      | isTrue h => subst t; simp [delta]
      | isFalse h => simp [delta,h,Ne.symm h]
    rcases k with ⟨i,j⟩
    simp only [swap,sumSingle,oneL,Int.one_mul]
  calc
    total entries f = total entries (fun t => total grouped (delta t)) :=
      congrArg (total entries) (funext row).symm
    _ = total grouped (fun k => total entries (fun t => delta t k)) := exchange _ _ _
    _ = total grouped f := congrArg (total grouped) (funext col)

/-- The trace of the ordinary matrix product, with no symmetry assumptions in
    its definition. -/
def termRe (r e : Matrix) (t : Entry) :=
  (r t.1 t.2).re*(e t.2 t.1).re - (r t.1 t.2).im*(e t.2 t.1).im
def termIm (r e : Matrix) (t : Entry) :=
  (r t.1 t.2).re*(e t.2 t.1).im + (r t.1 t.2).im*(e t.2 t.1).re
def productTrace (r e : Matrix) : G := ⟨total entries (termRe r e), total entries (termIm r e)⟩

inductive Coord where
  | diag (i : Index)
  | real (ij : Entry)
  | imag (ij : Entry)
  deriving DecidableEq
def coords := basis.map Coord.diag ++ (upper.map Coord.real ++ upper.map Coord.imag)
def trimmed := basis.tail.map Coord.diag ++ (upper.map Coord.real ++ upper.map Coord.imag)
def stateCoord (r : Matrix) : Coord → Int
  | .diag i => (r i i).re
  | .real (i,j) => (r i j).re
  | .imag (i,j) => (r i j).im
def queryCoord (e : Matrix) : Coord → Int
  | .diag i => (e i i).re
  | .real (i,j) => 2*(e i j).re
  | .imag (i,j) => 2*(e i j).im

theorem coordinateCounts : upper.length = 21 ∧ coords.length = 49 ∧ trimmed.length = 48 := by decide

private theorem diagIm (r : Matrix) (h : hermitian r) (i : Index) : (r i i).im = 0 := by
  have eq := (h i i).2
  omega

private theorem regroup (f : Entry → Int) :
    total entries f = total basis (fun i => f (i,i)) + total upper (fun t => f t + f t.swap) := by
  rw [regroupEntries,grouped,totalAppend,totalAppend,totalMap,totalMap,sumAdd]

private theorem pairRe (r e : Matrix) (hr : hermitian r) (he : hermitian e) (t : Entry) :
    termRe r e t + termRe r e t.swap =
    stateCoord r (.real t)*queryCoord e (.real t) + stateCoord r (.imag t)*queryCoord e (.imag t) := by
  rcases t with ⟨i,j⟩
  simp only [termRe,Prod.swap,stateCoord,queryCoord]
  rw [(hr i j).1,(hr i j).2,(he i j).1,(he i j).2]
  simp only [Int.two_mul,Int.mul_add,Int.mul_neg,Int.neg_mul]
  omega

private theorem pairIm (r e : Matrix) (hr : hermitian r) (he : hermitian e) (t : Entry) :
    termIm r e t + termIm r e t.swap = 0 := by
  rcases t with ⟨i,j⟩
  simp only [termIm,Prod.swap]
  rw [(hr i j).1,(hr i j).2,(he i j).1,(he i j).2]
  simp only [Int.mul_neg,Int.neg_mul]
  omega

/-- Bilinear factorization of the *actual* trace in 49 real coordinates, and
    vanishing imaginary part. Clearing positive denominators gives its rational
    version, without approximating phases. -/
theorem traceFactors (r e : Matrix) (hr : hermitian r) (he : hermitian e) :
    productTrace r e =
      ⟨total coords (fun c => stateCoord r c * queryCoord e c), 0⟩ := by
  have diagR (i : Index) : termRe r e (i,i) = stateCoord r (.diag i)*queryCoord e (.diag i) := by
    simp [termRe,diagIm _ hr i,stateCoord,queryCoord]
  have diagI (i : Index) : termIm r e (i,i) = 0 := by simp [termIm,diagIm _ hr i,diagIm _ he i]
  unfold productTrace
  simp only [regroup,diagR,pairRe _ _ hr he,diagI,pairIm _ _ hr he,sumZero,Int.zero_add,
    coords,totalAppend,totalMap,sumAdd]

private theorem sumSub {X : Type} (xs : List X) (f g : X → Int) :
    total xs (fun x => f x - g x) = total xs f - total xs g := by
  induction xs with
  | nil => rfl
  | cons x xs ih => simp only [total,List.map_cons,List.sum_cons] at *; omega

def matrixTrace (r : Matrix) := total basis (fun i => (r i i).re)
def originEffect (e : Matrix) : Coord → Int
  | .diag _ => (e 0 0).re
  | _ => 0
def centeredQuery (e : Matrix) (c : Coord) := queryCoord e c - originEffect e c

/-- Fixing the trace leaves 48 variable real coordinates; the affine offset is
    explicit, so it cancels when preparation rows with equal mass are differenced. -/
theorem centeredTrace (r e : Matrix) (hr : hermitian r) (he : hermitian e) :
    (productTrace r e).re = matrixTrace r*(e 0 0).re +
      total trimmed (fun c => stateCoord r c*centeredQuery e c) := by
  rw [traceFactors _ _ hr he]
  change (r 0 0).re*(e 0 0).re + total trimmed (fun c => stateCoord r c*queryCoord e c) = _
  have origin : total trimmed (fun c => stateCoord r c*originEffect e c) =
      total basis.tail (fun i => (r i i).re)*(e 0 0).re := by
    simp only [trimmed,totalAppend,totalMap,stateCoord,originEffect,Int.mul_zero,sumZero,
      Int.add_zero,sumScaleRight]
  simp only [centeredQuery,Int.mul_sub,sumSub,origin]
  change _ = ((r 0 0).re + total basis.tail (fun i => (r i i).re))*(e 0 0).re + _
  rw [Int.add_mul]
  omega

/-- Every linear relation on the coordinate rows passes to all query columns.
    No relation on the observed table is assumed. -/
theorem relationTransfer {X : Type} (xs : List X) (w : X → Int) (r : X → Matrix)
    (hr : ∀ x, hermitian (r x))
    (relation : ∀ c ∈ coords, total xs (fun x => w x*stateCoord (r x) c) = 0)
    (e : Matrix) (he : hermitian e) :
    total xs (fun x => w x*(productTrace (r x) e).re) = 0 := by
  have eq (x : X) := congrArg G.re (traceFactors (r x) e (hr x) he)
  change ∀ x, (productTrace (r x) e).re = total coords (fun c => stateCoord (r x) c*queryCoord e c) at eq
  simp only [eq,← sumScale]
  rw [exchange]
  have collapse (cs : List Coord) (hcs : ∀ c ∈ cs, c ∈ coords) :
      total cs (fun c => total xs (fun x => w x*(stateCoord (r x) c*queryCoord e c))) = 0 := by
    induction cs with
    | nil => rfl
    | cons c cs ih =>
      change total xs (fun x => w x*(stateCoord (r x) c*queryCoord e c)) + _ = 0
      have head : total xs (fun x => w x*(stateCoord (r x) c*queryCoord e c)) = 0 := by
        simp only [← Int.mul_assoc,sumScaleRight,relation c (hcs c (by simp)),Int.zero_mul]
      rw [head,Int.zero_add]
      exact ih (fun y hy => hcs y (by simp [hy]))
  exact collapse coords (fun _ h => h)

end OperationalNetwork.SevenReadout
