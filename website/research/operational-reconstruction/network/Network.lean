import RandomProcess
import Matter
import Reports
import BreathPractice
import PracticeChannels
import PracticeDecision
import PracticeOverlap
import PracticeHoldout
import PracticeModelComparison
import SevenReadout
import ProtocolMetric
import Response
import BoundaryMemory
import CircleLimit
import ClockNormalization
import MeshControl
import ProductLimit
import DriftControl
import CommonGeometry
import ClockRefinement
import CyclicTransport
import NetworkScale
import RouteReadout
import ScaleObstruction
import TerminalNetwork
set_option autoImplicit false

namespace OperationalNetwork

/-- The entire impulse transforms covariantly even with a different change
    of frame at every cell. The physical vacuum is common to all local frames. -/
def inFrames {V : Type} (r : Rule V) (g : Int → Frame V)
    (zero : ∀ j, (g j).f r.quiet = r.quiet) : Rule V where
  quiet := r.quiet
  update n j a b c := (g j).f (r.update n j ((g (j-1)).inv a)
    ((g j).inv b) ((g (j+1)).inv c))
  silent n j := by
    have z (k : Int) : (g k).inv r.quiet = r.quiet := by
      rw [← zero k, (g k).cancel, zero k]
    simp only [z, r.silent, zero]

theorem impulseCovariant {V : Type} (r : Rule V) (g : Int → Frame V)
    (z : ∀ j, (g j).f r.quiet = r.quiet) (o : Int) (p : V) (n : Nat) :
    ∀ j, impulse (inFrames r g z) o ((g o).f p) n j = (g j).f (impulse r o p n j) := by
  induction n with
  | zero =>
    intro j; by_cases eq : j=o
    · subst j; simp [impulse]
    · simp [impulse, eq, inFrames, z]
  | succ n ih =>
    intro j
    simp only [impulse, ih]
    simp only [inFrames, Frame.cancel]

/-- Time reversal here means reflecting the coordinate of the propagation
    test; it puts no time-reversal symmetry assumption on the dynamics. -/
def mirror {V : Type} (r : Rule V) : Rule V where
  quiet := r.quiet
  update n j a b c := r.update n (-j) c b a
  silent n j := r.silent n (-j)

theorem mirrorSignal {V : Type} (r : Rule V) (o : Int) (p : V) (n : Nat) :
    ∀ j, impulse (mirror r) (-o) p n j = impulse r o p n (-j) := by
  induction n with
  | zero => intro j; by_cases h : j = -o
            · subst j; simp [impulse]
            · simp [impulse,h,show -j ≠ o by omega,mirror]
  | succ n ih =>
    intro j
    simp only [impulse, ih]
    simp only [mirror, show -(j+1) = -j-1 by omega, show -(j-1) = -j+1 by omega]

theorem measuredReturn {V : Type} (r : Rule V) (o : Int) (p : V) (n : Nat)
    (visible : front (mirror r) (-o) p n ≠ r.quiet) :
    FirstAt r.quiet (fun k => impulse r o p k (o-n)) n := by
  have eq := measuredArrival (mirror r) (-o) p n visible
  change FirstAt r.quiet _ _ at eq
  simpa only [FirstAt, mirrorSignal, show -(-o + (n:Int)) = o-n by omega] using eq

/-- A receiver for the two phase settings: if both readouts are quiet,
    each of the tied routes had zero amplitude. This is a linear-amplitude
    claim; a detector must distinguish a nonzero amplitude from zero. -/
theorem twoPhase {V : Type} [Zero V] [Add V] [Sub V]
    (same : ∀ a b : V, a-b=0 → a=b)
    (noTwoTorsion : ∀ a : V, a+a=0 → a=0)
    (a b : V) (plus : a+b=0) (minus : a-b=0) : a=0 ∧ b=0 := by
  have h := same a b minus
  subst b
  exact ⟨noTwoTorsion _ plus,noTwoTorsion _ plus⟩

theorem twoPhaseOnAmplitudes {I : Type} (a b : I → Int)
    (plus : ∀ i, a i + b i = 0) (minus : ∀ i, a i - b i = 0) :
    (∀ i, a i=0) ∧ (∀ i, b i=0) := by
  have h (i : I) := twoPhase (V:=Int) (fun _ _ h => by omega)
    (fun _ h => by omega) (a i) (b i) (plus i) (minus i)
  exact ⟨fun i => (h i).1, fun i => (h i).2⟩

inductive Station where | A | B | C deriving DecidableEq
open Station
def distances (l r : Nat) : Station → Station → Nat
  | A,B | B,A => l
  | B,C | C,B => r
  | A,C | C,A => l+r
  | _,_ => 0

theorem reconstructedMetric {l r : Nat} (hl : 0<l) (hr : 0<r) (i j k : Station) :
    (distances l r i j = 0 ↔ i=j) ∧ distances l r i j = distances l r j i ∧
    distances l r i k ≤ distances l r i j + distances l r j k := by
  constructor
  · constructor
    · intro h; cases i <;> cases j <;> first | rfl | (simp only [distances] at h; omega)
    · intro h; subst j; cases i <;> rfl
  · constructor
    · cases i <;> cases j <;> rfl
    · cases i <;> cases j <;> cases k <;> simp only [distances] <;> omega

def atCell (l r : Nat) : Station → Int
  | A => 0 | B => l | C => (l+r : Nat)

/-- The path metric is obtained at the same positions and times at which the
    impulse experiment actually reads the receiver, for all nine ordered pairs. -/
theorem threeStationReadout {V : Type} (rule : Rule V) (pulse : V) (l r : Nat)
    (rightVisible : ∀ o n, front rule o pulse n ≠ rule.quiet)
    (leftVisible : ∀ o n, front (mirror rule) o pulse n ≠ rule.quiet)
    (i j : Station) :
    FirstAt rule.quiet
      (fun k => impulse rule (atCell l r i) pulse k (atCell l r j)) (distances l r i j) := by
  let o := atCell l r i
  let n := distances l r i j
  have reach : atCell l r j = o+n ∨ atCell l r j = o-n := by
    dsimp [o,n]
    cases i <;> cases j <;> simp only [atCell,distances] <;> omega
  rcases reach with h | h
  · simpa only [← h] using measuredArrival rule o pulse n (rightVisible o n)
  · simpa only [← h] using measuredReturn rule o pulse n (leftVisible (-o) n)

#print axioms threeStationReadout

theorem firstUnique {V : Type} {zero : V} {signal : Nat → V} {m n : Nat}
    (hm : FirstAt zero signal m) (hn : FirstAt zero signal n) : m=n := by
  rcases Nat.lt_trichotomy m n with h | h | h
  · exact False.elim (hm.1 (hn.2 _ h))
  · exact h
  · exact False.elim (hn.1 (hm.2 _ h))

/-- Arrival is an observable (quotiented by local changes of basis). -/
theorem firstFrameInvariant {V : Type} (g : Frame V) (z : V) (hz : g.f z = z)
    (signal : Nat → V) (n : Nat) :
    FirstAt z (fun k => g.f (signal k)) n ↔ FirstAt z signal n := by
  have eq (v : V) : g.f v = z ↔ v=z := by
    constructor
    · intro h
      have b := congrArg g.inv (h.trans hz.symm)
      simpa only [g.cancel] using b
    · intro h; rw [h,hz]
  simp only [FirstAt,Ne,eq]

/-- Two settings of one registered physical arm. An observation is quiet if
    both settings are quiet. An indivisible record is a pair of amplitudes. -/
theorem firstTwoSettings {I : Type} (direct via : Nat → I → Int) (t : Nat)
    (before : ∀ k, k<t → ∀ i, direct k i=0 ∧ via k i=0)
    (lit : ∃ i, direct t i ≠ 0 ∨ via t i ≠ 0) :
    FirstAt (fun _ : I => ((0,0) : Int × Int))
      (fun k i => (direct k i + via k i, direct k i - via k i)) t := by
  constructor
  · intro h
    obtain ⟨i,hi⟩ := lit
    have e := congrFun h i
    have p := congrArg Prod.fst e
    have m := congrArg Prod.snd e
    change direct t i + via t i = 0 at p
    change direct t i - via t i = 0 at m
    omega
  · intro k hk
    funext i
    obtain ⟨a,b⟩ := before k hk i
    simp [a,b]

/-- Interferometric quadratures over Gaussian integers (and Gaussian rationals
    by clearing denominators). Each coordinate identity adds over a detector. -/
def intensity (x y : Int) := x*x+y*y
theorem fourPhaseReadout (a b c d : Int) :
    intensity (a+c) (b+d) - intensity (a-c) (b-d) = 4*(a*c+b*d) ∧
    intensity (a+d) (b-c) - intensity (a-d) (b+c) = 4*(a*d-b*c) := by
  constructor <;>
    simp only [intensity,Int.add_mul,Int.mul_add,Int.sub_mul,Int.mul_sub,Int.mul_comm] <;> omega

theorem middleIdentified {l r : Nat} (hl : 0<l) (hr : 0<r) :
    distances l r A B < distances l r A C ∧
    distances l r B C < distances l r A C := by
  constructor <;> simp only [distances] <;> omega

-- Sum intensities over all resolved real and imaginary components. The
-- sign setting must be global across the components of an optical arm.
def power (read : Int → Int → Int) : List (Int × Int) → Int
  | [] => 0
  | (a,b)::xs => read a b + power read xs

def plusI (a b : Int) := (a+b)*(a+b)
def minusI (a b : Int) := (a-b)*(a-b)
def separateI (a b : Int) := a*a+b*b

theorem sumPower (xs : List (Int × Int)) :
    power plusI xs + power minusI xs = 2*power separateI xs := by
  induction xs with
  | nil => rfl
  | cons ab rest ih =>
    rcases ab with ⟨a,b⟩
    simp only [power,plusI,minusI,separateI,Int.add_mul,Int.mul_add,Int.sub_mul,Int.mul_sub] at *
    omega

theorem oneSettingBright (xs : List (Int × Int)) :
    power separateI xs ≤ power plusI xs ∨ power separateI xs ≤ power minusI xs := by
  have h := sumPower xs
  omega

theorem sharpTwoSettingBound :
    let inputs : List (Int × Int) := [(1,0),(0,1)]
    power plusI inputs = 2 ∧ power minusI inputs = 2 ∧ power separateI inputs = 2 := by decide

#print axioms oneSettingBright
#print axioms sharpTwoSettingBound
#print axioms firstTwoSettings
#print axioms fourPhaseReadout
#print axioms firstFrameInvariant
#print axioms impulseCovariant
#print axioms measuredReturn
#print axioms twoPhaseOnAmplitudes
#print axioms reconstructedMetric
#print axioms firstUnique
end OperationalNetwork
