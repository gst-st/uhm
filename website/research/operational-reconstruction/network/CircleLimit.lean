import PeriodicLimit
import LimitMetric
set_option autoImplicit false
namespace OperationalNetwork.Periodic
open OperationalNetwork.Continuum

abbrev Angle := Nat → Bool

/-- The first n binary digits name a physical cell in the 2^n-station ring.
    No real-valued coordinates or preexisting real circle are inputs. -/
def cellNumber (x : Angle) : Nat → Nat
  | 0 => 0
  | n+1 => 2*cellNumber x n + if x n then 1 else 0

theorem validPrefix (x : Angle) (n : Nat) : cellNumber x n < 2^n := by
  induction n with
  | zero => exact Nat.zero_lt_one
  | succ n ih => rw [cellNumber,Nat.pow_succ]; split <;> omega

private theorem nestedPrefixes (x : Angle) (n k : Nat) :
    2^k * cellNumber x n ≤ cellNumber x (n+k) ∧ cellNumber x (n+k) < 2^k * (cellNumber x n+1) := by
  induction k with
  | zero => simp
  | succ k ih =>
    simp only [Nat.add_succ,cellNumber.eq_2,Nat.pow_succ, Nat.mul_comm (2^k) 2]
    simp only [Nat.mul_assoc,Nat.add_zero,Nat.succ_eq_add_one]
    split <;> constructor <;> omega

def angularTicks (x y : Angle) (n : Nat) := arc (2^n) (cellNumber x n) (cellNumber y n)

private theorem arcRefinement (x y : Angle) (n k : Nat) :
    angularTicks x y (n+k) ≤ 2^k * angularTicks x y n + 2*2^k ∧
    2^k * angularTicks x y n ≤ angularTicks x y (n+k)+2*2^k := by
  let r := 2^k
  have bounds (z : Angle) : gap (cellNumber z (n+k)) (r*cellNumber z n) ≤ r := by
    obtain ⟨lo,hi⟩ := nestedPrefixes z n k
    rw [Nat.mul_succ] at hi
    dsimp [r]; unfold gap; omega
  have scale : r*2^n = 2^(n+k) := by dsimp [r]; rw [← Nat.pow_add,Nat.add_comm]
  have inside (z : Angle) : r * cellNumber z n < 2^(n+k) := by
    rw [← scale]; exact Nat.mul_lt_mul_of_pos_left (validPrefix z n) (Nat.pow_pos (by decide))
  have both := arcPortError (validPrefix x (n+k)) (validPrefix y (n+k)) (inside x) (inside y)
    (bounds x) (bounds y)
  rw [← scale,arcDilation,scale] at both
  change _ ≤ r * _ + 2*r ∧ r * _ ≤ _ + 2*r
  unfold angularTicks
  constructor <;> omega

private theorem powMatch {n m : Nat} (le : n≤m) : 2^(m-n)*2^n=2^m := by
  rw [← Nat.pow_add, Nat.sub_add_cancel le]

theorem anglesCauchy (x y : Angle) : Cauchy (angularTicks x y) := by
  intro k
  refine ⟨k+1,?_⟩
  intro n m hn hm
  have step := arcRefinement x y n (m-n)
  rw [Nat.add_sub_of_le hm] at step
  have allowance : 2^k * (2*2^(m-n)) ≤ 2^m := by
    have small : 2^(k+1) ≤ 2^n := Nat.pow_le_pow_right (by decide) hn
    calc
      2^k*(2*2^(m-n)) = 2^(m-n)*2^(k+1) := by rw [Nat.pow_succ]; ac_rfl
      _ ≤ 2^(m-n)*2^n := Nat.mul_le_mul_left _ small
      _ = 2^m := powMatch hm
  have one := Nat.mul_le_mul_left (2^k) step.1
  have two := Nat.mul_le_mul_left (2^k) step.2
  rw [Nat.mul_add] at one two
  constructor <;> omega

def angularPseudometric : LimitPseudometric Angle :=
  fromReadings (fun n x y => angularTicks x y n) anglesCauchy
    (fun n x => (arcSeparates _ _ _ (validPrefix x n) (validPrefix x n)).2 rfl)
    (fun x y => ⟨dominatesPointwise (fun n => Nat.le_of_eq (arcSym _ (cellNumber x n) (cellNumber y n))),
                  dominatesPointwise (fun n => Nat.le_of_eq (arcSym _ (cellNumber y n) (cellNumber x n)))⟩)
    (fun n x y z => arcTriangle _ _ _ _ (validPrefix x n) (validPrefix y n) (validPrefix z n))

abbrev AnglePoint := Quotient (observationalEq angularPseudometric)
def anglePoint (x : Angle) : AnglePoint := Quotient.mk _ x
def angularMetric : LimitMetric AnglePoint := operationalMetric angularPseudometric

/-- A finite witnessed separation of three grid ticks implies positive
    separation in the limit, with a computable lower tail. -/
theorem separatedAngles {x y : Angle} (n : Nat) (visible : 3 ≤ angularTicks x y n) :
    Positive (angularPseudometric.dist x y) := by
  refine ⟨n,n,?_⟩
  intro m hm
  have step := (arcRefinement x y n (m-n)).2
  rw [Nat.add_sub_of_le hm] at step
  have raw := Nat.mul_le_mul_left (2^(m-n)) visible
  have low : 2^(m-n) ≤ angularTicks x y m := by omega
  rw [← powMatch hm,Nat.mul_comm (2^(m-n))]
  exact Nat.mul_le_mul_left _ low

/-- The quotient can be checked without already knowing equality in the
    unknown limiting metric: two complete digit histories co-name a point iff
    they stay within two grid steps at *every* precision. -/
theorem sameAngleIff (x y : Angle) : anglePoint x=anglePoint y ↔
    ∀ n, angularTicks x y n ≤ 2 := by
  constructor
  · intro same n
    have closed : angularPseudometric.dist x y=zero := Quotient.exact same
    by_cases h : angularTicks x y n ≤ 2
    · exact h
    · have pos := separatedAngles n (show 3 ≤ angularTicks x y n by omega)
      exact False.elim (zeroNotPositive (closed ▸ pos))
  · intro small
    apply Quotient.sound
    change limit (angularTicks x y) (anglesCauchy x y) = zero
    apply (limitEq _ _).2
    refine ⟨?_,dominatesPointwise (fun _ => Nat.zero_le _)⟩
    intro k
    refine ⟨k+1,?_⟩
    intro n hn
    have upper := Nat.mul_le_mul_left (2^k) (small n)
    have cmp : 2^(k+1) ≤ 2^n := Nat.pow_le_pow_right (by decide) hn
    rw [Nat.pow_succ] at cmp
    change 2^k*angularTicks x y n ≤ 2^k*0+2^n
    omega

/-- A probe may change its microscopic delay at every scale and every cell.
    Each cell has four ticks in total; offset 0 measures its left boundary. -/
abbrev CellProbe := Nat → Nat → Fin 4
def probePosition (p : CellProbe) (x : Angle) (n : Nat) :=
  4*cellNumber x n + (p n (cellNumber x n)).val

private theorem fourTicks (n : Nat) : 2^(n+2) = 4*2^n := by
  rw [Nat.pow_add,Nat.mul_comm]

private theorem insideProbe (p : CellProbe) (x : Angle) (n : Nat) :
    probePosition p x n < 2^(n+2) := by
  rw [fourTicks]
  have h := validPrefix x n
  have off := (p n (cellNumber x n)).isLt
  unfold probePosition; omega

/-- Stages 0,1 use the original coarse readers. Afterwards there are
    2^(n−2) cells of four unit relays, so one tick is still exactly 2^-n. -/
def measuredAngle (p : CellProbe) (x y : Angle) : Nat → Nat
  | 0 => angularTicks x y 0
  | 1 => angularTicks x y 1
  | n+2 => arc (2^(n+2)) (probePosition p x n) (probePosition p y n)

theorem measuredAngularPulse (p : CellProbe) (x y : Angle) (n budget : Nat) :
    let C := 2^(n+2)
    let ix (z : Angle) : Fin (C-1+1) := ⟨probePosition p z n,by have := insideProbe p z n; dsimp [C]; omega⟩
    SignalNetwork.firstTick? (unitLinks (C-1)) (ix x) (ix y) budget =
      if measuredAngle p x y (n+2) ≤ budget then some (measuredAngle p x y (n+2)) else none := by
  dsimp only
  rw [unitRingFirst]
  have pos := insideProbe p x n
  simp only [show 2^(n+2)-1+1=2^(n+2) by omega,measuredAngle]
  rfl

theorem measuredAngleError (p : CellProbe) (x y : Angle) (n : Nat) :
    angularTicks x y n ≤ measuredAngle p x y n + 6 ∧
    measuredAngle p x y n ≤ angularTicks x y n + 6 := by
  match n with
  | 0 | 1 => exact ⟨Nat.le_add_right _ _, Nat.le_add_right _ _⟩
  | n+2 =>
    have err (a : Angle) : gap (probePosition p a n) (cellNumber a (n+2)) ≤ 3 := by
      obtain ⟨lo,hi⟩ := nestedPrefixes a n 2
      have off := (p n (cellNumber a n)).isLt
      change 4*cellNumber a n ≤ _ at lo
      change _ < 4*(cellNumber a n+1) at hi
      unfold gap probePosition; omega
    have comp := arcPortError (insideProbe p x n) (insideProbe p y n)
      (validPrefix x (n+2)) (validPrefix y (n+2)) (err x) (err y)
    unfold angularTicks
    simp only [measuredAngle]
    constructor <;> omega

private theorem boundedTicksAgree (f g : Nat → Nat) (h : ∀ n, f n ≤ g n + 6) : Dominated f g := by
  intro k
  refine ⟨k+3,?_⟩
  intro n hn
  have upper := Nat.mul_le_mul_left (2^k) (h n)
  rw [Nat.mul_add] at upper
  have sys : 2^(k+3) ≤ 2^n := Nat.pow_le_pow_right (by decide) hn
  rw [Nat.pow_add] at sys
  change 2^k*8 ≤ 2^n at sys
  omega

/-- Every independently timed microprobe has the same limit, for any two
    *infinite* angular histories, read through the public pulse detector. -/
theorem fullAngleLimit (p : CellProbe) (x y : Angle) :
    Converges (measuredAngle p x y) (angularMetric.dist (anglePoint x) (anglePoint y)) := by
  exact commonReading (anglesCauchy x y) ⟨boundedTicksAgree _ _ (fun n => (measuredAngleError p x y n).1),
    boundedTicksAgree _ _ (fun n => (measuredAngleError p x y n).2)⟩

/-- The finite-stage bound verifies two expected identifications and one
    strictly separated pair. At a dyadic cut, the two binary expansions of
    one half agree. The all-ones stream approaches the all-zero seam. -/
theorem circleSeamAndAntipodes :
    let o : Angle := fun _ => false
    let endPoint : Angle := fun _ => true
    let rightHalf : Angle := fun n => decide (n=0)
    let leftHalf : Angle := fun n => decide (n≠0)
    anglePoint o = anglePoint endPoint ∧ anglePoint rightHalf = anglePoint leftHalf ∧
      Positive (angularMetric.dist (anglePoint o) (anglePoint rightHalf)) := by
  dsimp only
  have zeroCell (n : Nat) : cellNumber (fun _ => false) n = 0 := by
    induction n with
    | zero => rfl
    | succ n ih => simp [cellNumber,ih]
  have ones (n : Nat) : cellNumber (fun _ => true) n + 1 = 2^n := by
    induction n with
    | zero => rfl
    | succ n ih => simp only [cellNumber,↓reduceIte,Nat.pow_succ]; omega
  have halves (n : Nat) : cellNumber (fun j => decide (j≠0)) (n+1) + 1 =
      cellNumber (fun j => decide (j=0)) (n+1) := by
    induction n with
    | zero => rfl
    | succ n ih =>
      rw [cellNumber.eq_2, cellNumber.eq_2 (fun j => decide (j=0))]
      have left : decide (n+1≠0) = true := decide_eq_true (Nat.succ_ne_zero _)
      have right : decide (n+1=0) = false := decide_eq_false (Nat.succ_ne_zero _)
      simp only [left,right,↓reduceIte,Bool.false_eq_true]; omega
  refine ⟨(sameAngleIff _ _).2 ?_,(sameAngleIff _ _).2 ?_,separatedAngles 3 (by decide)⟩
  · intro n
    have h := ones n
    simp only [angularTicks,gap,arc,zeroCell]
    omega
  · intro n
    cases n with
    | zero => decide
    | succ n =>
      have h := halves n
      unfold angularTicks arc gap
      omega

/-- The dyadic station selected by the first p observations. -/
def truncateAngle (x : Angle) (p : Nat) : Angle := fun i => if i<p then x i else false

private theorem sameInitialCells (x : Angle) (p n : Nat) (h : n≤p) :
    cellNumber (truncateAngle x p) n = cellNumber x n := by
  induction n with
  | zero => rfl
  | succ n ih =>
    simp only [cellNumber,truncateAngle,ite_eq_left (show n<p by omega),ih (by omega)]

private theorem frozenCell (x : Angle) (p k : Nat) :
    cellNumber (truncateAngle x p) (p+k) = 2^k * cellNumber x p := by
  induction k with
  | zero => simp [sameInitialCells]
  | succ k ih =>
    simp only [Nat.add_succ,cellNumber.eq_2,truncateAngle,ite_eq_right (show ¬p+k<p by omega),
      Bool.false_eq_true,↓reduceIte,Nat.add_zero,Nat.pow_succ,ih]
    ac_rfl

/-- Every infinite address admits explicit approximating boundary stations.
    Their angular error is at most 2^-p in the constructed Value order. -/
theorem dyadicMeshDense (x : Angle) (p : Nat) :
    valueLE (angularMetric.dist (anglePoint x) (anglePoint (truncateAngle x p))) (dyadic 1 p) := by
  apply dominatesEventually (N:=p)
  intro m h
  change angularTicks x (truncateAngle x p) m ≤ 2^(m-p)*1
  have hi := (nestedPrefixes x p (m-p)).2
  have lo := (nestedPrefixes x p (m-p)).1
  have center := frozenCell x p (m-p)
  rw [Nat.add_sub_of_le h] at center lo hi
  rw [Nat.mul_succ] at hi
  calc
    angularTicks x (truncateAngle x p) m ≤ gap (cellNumber x m) (cellNumber (truncateAngle x p) m) :=
      Nat.min_le_left _ _
    _ ≤ 2^(m-p)*1 := by rw [center]; unfold gap; omega

end OperationalNetwork.Periodic
