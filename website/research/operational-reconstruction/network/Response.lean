import Std
set_option autoImplicit false
namespace OperationalNetwork

/-- F reads the previous tick at the left neighbour, the receiving cell and
    the right neighbour, in this order. Away from the front its action is free. -/
structure Rule (V : Type) where
  quiet : V
  update : Nat → Int → V → V → V → V
  silent : ∀ n j, update n j quiet quiet quiet = quiet

def impulse {V : Type} (r : Rule V) (origin : Int) (pulse : V) : Nat → Int → V
  | 0, j => if j = origin then pulse else r.quiet
  | n+1, j => r.update n j (impulse r origin pulse n (j-1))
      (impulse r origin pulse n j) (impulse r origin pulse n (j+1))

theorem ahead {V : Type} (r : Rule V) (o : Int) (p : V) (n : Nat) :
    ∀ j, o + (n : Int) < j → impulse r o p n j = r.quiet := by
  induction n with
  | zero => intro j h; simp [impulse, show j ≠ o by omega]
  | succ n ih =>
    intro j h
    rw [impulse, ih (j-1) (by omega), ih j (by omega), ih (j+1) (by omega), r.silent]

/-- The first transmitted signal can change polarization at each bond. -/
def front {V : Type} (r : Rule V) (o : Int) (p : V) : Nat → V
  | 0 => p
  | n+1 => r.update n (o+n+1) (front r o p n) r.quiet r.quiet

theorem frontValue {V : Type} (r : Rule V) (o : Int) (p : V) (n : Nat) :
    impulse r o p n (o+n) = front r o p n := by
  induction n with
  | zero => simp [impulse, front]
  | succ n ih =>
    rw [impulse, front]
    rw [show o + (↑(n+1) : Int) - 1 = o+n by omega, ih,
        ahead r o p n _ (by omega), ahead r o p n _ (by omega)]
    congr 1 <;> omega

def FirstAt {V : Type} (quiet : V) (signal : Nat → V) (n : Nat) : Prop :=
    signal n ≠ quiet ∧ ∀ k, k < n → signal k = quiet

theorem measuredArrival {V : Type} (r : Rule V) (o : Int) (p : V) (n : Nat)
    (visible : front r o p n ≠ r.quiet) :
    FirstAt r.quiet (fun k => impulse r o p k (o+n)) n := by
  constructor
  · simpa only [frontValue] using visible
  · intro k hk; apply ahead; omega

theorem losslessFront {V : Type} (r : Rule V) (o : Int) (p : V) (hp : p ≠ r.quiet)
    (transmit : ∀ k v, v ≠ r.quiet → r.update k (o+k+1) v r.quiet r.quiet ≠ r.quiet)
    (n : Nat) : front r o p n ≠ r.quiet := by
  induction n with
  | zero => exact hp
  | succ n ih => exact transmit _ _ ih

/-- Distinct probes can have arbitrarily different local dynamics and internal carriers. -/
theorem commonTick {V W : Type} (r : Rule V) (s : Rule W) (o : Int) (p : V) (q : W)
    (n : Nat) (hr : front r o p n ≠ r.quiet) (hs : front s o q n ≠ s.quiet) :
    FirstAt r.quiet (fun k => impulse r o p k (o+n)) n ∧
    FirstAt s.quiet (fun k => impulse s o q k (o+n)) n :=
  ⟨measuredArrival r o p n hr, measuredArrival s o q n hs⟩

/-- Normalized times are rational ratios represented without division.
    L and R are separately measured times on two reciprocal bonds.
    A common pair of positive lengths permits a probe-specific clock unit. -/
theorem commonShape {S : Type} (ref : S) (L R : S → Nat)
    (hL : ∀ s, 0 < L s) (hR : ∀ s, 0 < R s) :
    (∃ a b : Nat, 0<a ∧ 0<b ∧ ∀ s, L s * b = R s * a) ↔
    (∀ s, L s * R ref = R s * L ref) := by
  constructor
  · rintro ⟨a,b,_,hb,h⟩ s
    apply Nat.eq_of_mul_eq_mul_right hb
    calc
      (L s * R ref) * b = R ref * (L s*b) := by ac_rfl
      _ = R ref * (R s*a) := by rw [h s]
      _ = R s * (R ref*a) := by ac_rfl
      _ = R s * (L ref*b) := by rw [h ref]
      _ = (R s * L ref)*b := by ac_rfl
  · intro h; exact ⟨L ref, R ref, hL ref, hR ref, h⟩

-- A bidirectional example with two polarization modes. The second probe
-- flips polarization across either bond. Opposite travelling pulses can meet.
def shift (twist : Bool) : Rule (Int × Int) where
  quiet := (0,0)
  update _ _ a _ b := if twist then (a.2+b.2,a.1+b.1) else (a.1+b.1,a.2+b.2)
  silent _ _ := by cases twist <;> rfl

theorem twoSignalModels (n : Nat) :
    FirstAt (0,0) (fun k => impulse (shift false) 0 (1,0) k n) n ∧
    FirstAt (0,0) (fun k => impulse (shift true) 0 (1,0) k n) n := by
  rw [← Int.zero_add (n : Int)]
  apply commonTick (shift false) (shift true) 0 (1,0) (1,0) n <;>
    apply losslessFront <;> try decide
  · intro _ v h hv; apply h
    rcases v with ⟨x,y⟩
    simp [shift] at hv
    exact Prod.ext hv.1 hv.2
  · intro _ v h hv; apply h
    rcases v with ⟨x,y⟩
    simp [shift] at hv
    exact Prod.ext hv.2 hv.1

#print axioms measuredArrival
#print axioms commonTick
#print axioms commonShape
#print axioms twoSignalModels
end OperationalNetwork
