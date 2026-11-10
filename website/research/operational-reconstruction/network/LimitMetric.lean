import ProtocolMetric

set_option autoImplicit false
namespace OperationalNetwork.Continuum

/-- A tick count f n has value f n / 2^n in a common unit. Cauchy accuracy
    2^-k is required on an entire tail; every comparison uses exact naturals.
    Positive dyadic tolerances are cofinal among positive real tolerances. -/
def Cauchy (f : Nat → Nat) : Prop :=
  ∀ k : Nat, ∃ N, ∀ n m, N ≤ n → n ≤ m →
    2^k*f m ≤ 2^k*(2^(m-n)*f n)+2^m ∧ 2^k*(2^(m-n)*f n) ≤ 2^k*f m+2^m

def Dominated (f g : Nat → Nat) : Prop :=
  ∀ k : Nat, ∃ N, ∀ n, N ≤ n → 2^k*f n ≤ 2^k*g n + 2^n

def Close (f g : Nat → Nat) : Prop := Dominated f g ∧ Dominated g f

def PositiveTail (f : Nat → Nat) : Prop :=
  ∃ k N : Nat, ∀ n, N ≤ n → 2^n ≤ 2^k*f n

theorem dominatesPointwise {f g : Nat → Nat} (h : ∀ n, f n ≤ g n) : Dominated f g := by
  intro k
  exact ⟨0,fun n _ => Nat.le_trans (Nat.mul_le_mul_left _ (h n)) (Nat.le_add_right _ _)⟩

private theorem double (a k : Nat) : 2^(k+1)*a = 2^k*a+2^k*a := by
  rw [Nat.pow_succ,Nat.mul_comm (2^k) 2,Nat.mul_assoc,Nat.two_mul]

theorem dominatesTrans {f g h : Nat → Nat} (fg : Dominated f g) (gh : Dominated g h) :
    Dominated f h := by
  intro k
  obtain ⟨a,ha⟩ := fg (k+1)
  obtain ⟨b,hb⟩ := gh (k+1)
  refine ⟨max a b, ?_⟩
  intro n hn
  have one := ha n (Nat.le_trans (Nat.le_max_left _ _) hn)
  have two := hb n (Nat.le_trans (Nat.le_max_right _ _) hn)
  simp only [double] at one two
  omega

theorem dominatesSum {f g u v : Nat → Nat} (fg : Dominated f g) (uv : Dominated u v) :
    Dominated (fun n => f n+u n) (fun n => g n+v n) := by
  intro k
  obtain ⟨a,ha⟩ := fg (k+1)
  obtain ⟨b,hb⟩ := uv (k+1)
  refine ⟨max a b, ?_⟩
  intro n hn
  have one := ha n (Nat.le_trans (Nat.le_max_left _ _) hn)
  have two := hb n (Nat.le_trans (Nat.le_max_right _ _) hn)
  simp only [double] at one two
  simp only [Nat.mul_add]
  omega

theorem cauchySum {f g : Nat → Nat} (hf : Cauchy f) (hg : Cauchy g) :
    Cauchy (fun n => f n+g n) := by
  intro k
  obtain ⟨a,ha⟩ := hf (k+1)
  obtain ⟨b,hb⟩ := hg (k+1)
  refine ⟨max a b, ?_⟩
  intro n m hn hm
  obtain ⟨u,v⟩ := ha n m (Nat.le_trans (Nat.le_max_left _ _) hn) hm
  obtain ⟨p,q⟩ := hb n m (Nat.le_trans (Nat.le_max_right _ _) hn) hm
  simp only [double] at u v p q
  simp only [Nat.mul_add]
  constructor <;> omega

structure Name where
  value : Nat → Nat
  convergent : Cauchy value

instance names : Setoid Name where
  r a b := Close a.value b.value
  iseqv := ⟨fun _ => ⟨dominatesPointwise (fun _ => Nat.le_refl _),
                       dominatesPointwise (fun _ => Nat.le_refl _)⟩,
            fun h => ⟨h.2,h.1⟩,fun h k => ⟨dominatesTrans h.1 k.1,dominatesTrans k.2 h.2⟩⟩

/-- Nonnegative Cauchy reals from dyadic observations. A finite precision
    record never picks a representative of a quotient class. -/
abbrev Value := Quotient names
def limit (f : Nat → Nat) (hf : Cauchy f) : Value := Quotient.mk _ ⟨f,hf⟩

theorem limitEq {f g : Nat → Nat} (hf : Cauchy f) (hg : Cauchy g) :
    limit f hf = limit g hg ↔ Close f g :=
  ⟨fun h => Quotient.exact h,fun h => @Quotient.sound _ names ⟨f,hf⟩ ⟨g,hg⟩ h⟩

private theorem cauchyZero : Cauchy (fun _ => 0) := by
  intro k
  exact ⟨0,fun _ _ _ _ => by simp⟩

def zero : Value := limit _ cauchyZero

def valueLE (x y : Value) : Prop := Quotient.liftOn₂ x y (fun a b => Dominated a.value b.value)
  (fun _ _ _ _ h k => propext ⟨fun ab => dominatesTrans h.2 (dominatesTrans ab k.1),
                                 fun ab => dominatesTrans h.1 (dominatesTrans ab k.2)⟩)

def add (x y : Value) : Value := Quotient.liftOn₂ x y
  (fun a b => limit (fun n => a.value n+b.value n) (cauchySum a.convergent b.convergent))
  (fun _ _ _ _ h k => Quotient.sound ⟨dominatesSum h.1 k.1,dominatesSum h.2 k.2⟩)

private theorem positiveMoves {f g : Nat → Nat} (fg : Dominated f g) (pos : PositiveTail f) :
    PositiveTail g := by
  obtain ⟨k,N,hN⟩ := pos
  obtain ⟨M,hM⟩ := fg (k+1)
  refine ⟨k+1,max N M,?_⟩
  intro n hn
  have one := hN n (Nat.le_trans (Nat.le_max_left _ _) hn)
  have two := hM n (Nat.le_trans (Nat.le_max_right _ _) hn)
  simp only [double] at two ⊢
  omega

def Positive (x : Value) : Prop := Quotient.liftOn x (fun a => PositiveTail a.value)
  (fun _ _ h => propext ⟨positiveMoves h.1,positiveMoves h.2⟩)

theorem positiveLimitIff {f : Nat → Nat} (hf : Cauchy f) :
    Positive (limit f hf) ↔ PositiveTail f := Iff.rfl

theorem zeroNotPositive : ¬Positive zero := by
  rintro ⟨k,N,hN⟩
  have h := hN N (Nat.le_refl _)
  have pos : 0 < 2^N := Nat.pow_pos (by decide)
  change 2^N ≤ 2^k*0 at h
  omega

theorem dominatesEventually {f g : Nat → Nat} {N : Nat} (h : ∀ n, N ≤ n → f n ≤ g n) :
    Dominated f g := by
  intro k
  exact ⟨N,fun n hn => Nat.le_trans (Nat.mul_le_mul_left _ (h n hn)) (Nat.le_add_right _ _)⟩

private theorem powerDiff {a b : Nat} (h : a ≤ b) : 2^a*2^(b-a) = 2^b := by
  rw [← Nat.pow_add,Nat.add_sub_of_le h]

private theorem refineExtend {a b t : Nat} (ab : a ≤ b) (bt : b ≤ t) :
    2^(t-b) * 2^(b-a) = 2^(t-a) := by
  rw [← Nat.pow_add,show (t-b)+(b-a)=t-a by omega]

private theorem fixedPrecision (a k : Nat) : Cauchy (fun n => 2^(n-k)*a) := by
  intro _
  refine ⟨k,?_⟩
  intro n m kn nm
  rw [← Nat.mul_assoc (2^(m-n)),refineExtend kn nm]
  exact ⟨Nat.le_add_right _ _,Nat.le_add_right _ _⟩

/-- Exact nonnegative dyadic a/2^k as a limit value. -/
def dyadic (a k : Nat) : Value := limit _ (fixedPrecision a k)

def Near (k : Nat) (x y : Value) : Prop :=
  valueLE x (add y (dyadic 1 k)) ∧ valueLE y (add x (dyadic 1 k))

def Converges (f : Nat → Nat) (x : Value) : Prop :=
  ∀ k, ∃ N, ∀ n, N ≤ n → Near k (dyadic (f n) n) x

private theorem removeScale {a b k m : Nat} (km : k ≤ m) (h : 2^k*a ≤ 2^k*b+2^m) :
    a ≤ b+2^(m-k) := by
  apply Nat.le_of_mul_le_mul_left _ (show 0 < 2^k from Nat.pow_pos (by decide))
  rwa [Nat.mul_add,powerDiff km]

/-- The measured dyadic sequence converges to its constructed class in the
    order-interval topology. No Cauchy limit in a given metric is presumed. -/
theorem nameConverges (f : Nat → Nat) (hf : Cauchy f) : Converges f (limit f hf) := by
  intro k
  obtain ⟨M,hM⟩ := hf k
  refine ⟨max M k,?_⟩
  intro n hn
  have mn := Nat.le_trans (Nat.le_max_left _ _) hn
  have kn := Nat.le_trans (Nat.le_max_right _ _) hn
  constructor
  · apply dominatesEventually (N:=n)
    intro t nt
    simpa only [Nat.mul_one] using removeScale (Nat.le_trans kn nt) (hM n t mn nt).2
  · apply dominatesEventually (N:=n)
    intro t nt
    simpa only [Nat.mul_one] using removeScale (Nat.le_trans kn nt) (hM n t mn nt).1

theorem valueReflexive (x : Value) : valueLE x x := by
  induction x using Quotient.inductionOn with
  | _ a => exact dominatesPointwise (fun _ => Nat.le_refl _)

theorem valueTransitive (x y z : Value) : valueLE x y → valueLE y z → valueLE x z := by
  induction x using Quotient.inductionOn with
  | _ a =>
    induction y using Quotient.inductionOn with
    | _ b =>
      induction z using Quotient.inductionOn with
      | _ c => exact dominatesTrans

theorem valueAntisymmetric (x y : Value) : valueLE x y → valueLE y x → x=y := by
  induction x, y using Quotient.inductionOn₂ with
  | _ a b => exact fun h k => @Quotient.sound _ names a b ⟨h,k⟩

theorem addRightMonotone (x y z : Value) : valueLE x y → valueLE (add x z) (add y z) := by
  induction x using Quotient.inductionOn with
  | _ a =>
    induction y using Quotient.inductionOn with
    | _ b =>
      induction z using Quotient.inductionOn with
      | _ c => exact fun h => dominatesSum h (dominatesPointwise (fun _ => Nat.le_refl _))

private theorem doubleRadius (y : Value) (k : Nat) :
    add (add y (dyadic 1 (k+1))) (dyadic 1 (k+1)) = add y (dyadic 1 k) := by
  induction y using Quotient.inductionOn with
  | _ a =>
    have eq (n : Nat) (hn : k+1 ≤ n) : a.value n+2^(n-(k+1))*1+2^(n-(k+1))*1 =
        a.value n+2^(n-k)*1 := by
      have ex := show n-k=(n-(k+1))+1 by omega
      rw [ex,Nat.pow_succ,Nat.mul_two]; simp only [Nat.mul_one,Nat.add_assoc]
    exact Quotient.sound ⟨dominatesEventually (fun n h => Nat.le_of_eq (eq n h)),
                           dominatesEventually (fun n h => Nat.le_of_eq (eq n h).symm)⟩

private theorem withinEveryTolerance (x y : Value) :
    (∀ k, valueLE x (add y (dyadic 1 k))) → valueLE x y := by
  induction x, y using Quotient.inductionOn₂ with
  | _ a b =>
    intro h k
    obtain ⟨M,hM⟩ := h (k+1) (k+1)
    refine ⟨max M (k+1),?_⟩
    intro n hn
    have le := hM n (Nat.le_trans (Nat.le_max_left _ _) hn)
    change 2^(k+1)*a.value n ≤ 2^(k+1)*(b.value n+2^(n-(k+1))*1)+2^n at le
    simp only [Nat.mul_one,Nat.mul_add,powerDiff (Nat.le_trans (Nat.le_max_right _ _) hn),double] at le
    omega

theorem uniqueLimit {f : Nat → Nat} {x y : Value} (hx : Converges f x) (hy : Converges f y) :
    x=y := by
  have direction {a b : Value} (ha : Converges f a) (hb : Converges f b) : valueLE a b := by
    apply withinEveryTolerance
    intro k
    obtain ⟨A,hA⟩ := ha (k+1)
    obtain ⟨B,hB⟩ := hb (k+1)
    have hitA := (hA (max A B) (Nat.le_max_left _ _)).2
    have hitB := (hB (max A B) (Nat.le_max_right _ _)).1
    rw [← doubleRadius b k]
    exact valueTransitive _ _ _ hitA (addRightMonotone _ _ _ hitB)
  exact valueAntisymmetric _ _ (direction hx hy) (direction hy hx)

structure LimitPseudometric (X : Type) where
  dist : X → X → Value
  nonnegative : ∀ x y, valueLE zero (dist x y)
  self : ∀ x, dist x x = zero
  symmetric : ∀ x y, dist x y = dist y x
  triangle : ∀ x y z, valueLE (dist x z) (add (dist x y) (dist y z))

/-- All the metric laws descend from the actual tables. Reciprocity is only
    required asymptotically. Finite-scale separation is intentionally absent. -/
def fromReadings {X : Type} (f : Nat → X → X → Nat) (hc : ∀ x y, Cauchy (fun n => f n x y))
    (idle : ∀ n x, f n x x=0) (rev : ∀ x y, Close (fun n => f n x y) (fun n => f n y x))
    (relay : ∀ n x y z, f n x z ≤ f n x y + f n y z) : LimitPseudometric X where
  dist x y := limit (fun n => f n x y) (hc x y)
  nonnegative _ _ := dominatesPointwise (fun _ => Nat.zero_le _)
  self x := (limitEq _ _).2 ⟨dominatesPointwise (fun n => Nat.le_of_eq (idle n x)),
                              dominatesPointwise (fun _ => Nat.zero_le _)⟩
  symmetric x y := (limitEq _ _).2 (rev x y)
  triangle x y z := dominatesPointwise (fun n => relay n x y z)

/-- A probe needs no independent Cauchy assumption if it tracks one Cauchy
    probe to vanishing calibrated error. -/
theorem cauchyOfClose {f g : Nat → Nat} (hf : Cauchy f) (hg : Close f g) : Cauchy g := by
  intro k
  obtain ⟨a,ha⟩ := hf (k+2)
  obtain ⟨b,hb⟩ := hg.1 (k+2)
  obtain ⟨c,hc⟩ := hg.2 (k+2)
  refine ⟨max a (max b c),?_⟩
  intro n m hn nm
  have an : a ≤ n := Nat.le_trans (Nat.le_max_left _ _) hn
  have bn : b ≤ n := Nat.le_trans (Nat.le_max_left b c) (Nat.le_trans (Nat.le_max_right _ _) hn)
  have cn : c ≤ n := Nat.le_trans (Nat.le_max_right b c) (Nat.le_trans (Nat.le_max_right _ _) hn)
  obtain ⟨fm,fn⟩ := ha n m an nm
  have gm := hc m (Nat.le_trans cn nm)
  have gf := hb m (Nat.le_trans bn nm)
  have scale {u v : Nat} (h : 2^(k+2)*u ≤ 2^(k+2)*v+2^n) :
      2^(k+2)*(2^(m-n)*u) ≤ 2^(k+2)*(2^(m-n)*v)+2^m := by
    have le := Nat.mul_le_mul_left (2^(m-n)) h
    rwa [Nat.mul_add,Nat.mul_left_comm (2^(m-n)) (2^(k+2)),Nat.mul_left_comm (2^(m-n)) (2^(k+2)),
        Nat.mul_comm (2^(m-n)) (2^n),powerDiff nm] at le
  have gn := scale (hc n cn)
  have fg := scale (hb n bn)
  simp only [show k+2=k+1+1 from rfl,double] at fm fn gm gf gn fg
  constructor <;> omega

theorem commonReading {f g : Nat → Nat} (hf : Cauchy f) (agreement : Close f g) :
    Converges g (limit f hf) := by
  let hg := cauchyOfClose hf agreement
  rw [(limitEq hf hg).2 agreement]
  exact nameConverges g hg

theorem addZero (x : Value) : add x zero=x := by
  induction x using Quotient.inductionOn with
  | _ a => rfl

theorem zeroAdd (x : Value) : add zero x=x := by
  induction x using Quotient.inductionOn with
  | _ a =>
    exact Quotient.sound ⟨dominatesPointwise (fun n => Nat.le_of_eq (Nat.zero_add (a.value n))),
      dominatesPointwise (fun n => Nat.le_of_eq (Nat.zero_add (a.value n)).symm)⟩

structure LimitMetric (X : Type) extends LimitPseudometric X where
  separates : ∀ x y, dist x y=zero → x=y

/-- Equality on a label type is stable when double negation can be removed
    from equality. This holds for decidable labels and many represented spaces. -/
def StableEquality (X : Type) := ∀ x y : X, (¬x ≠ y) → x=y

theorem decidableEqualityStable (X : Type) [DecidableEq X] : StableEquality X := by
  intro x y h
  by_cases e : x=y
  · exact e
  · exact (h e).elim

def LimitPseudometric.onLabels {X : Type} (p : LimitPseudometric X) (stable : StableEquality X)
    (gap : ∀ x y, x ≠ y → Positive (p.dist x y)) : LimitMetric X where
  toLimitPseudometric := p
  separates x y h := stable x y (fun ne => zeroNotPositive (h ▸ gap x y ne))

/-- Equality after calibration is the operational equivalence on arbitrary
    labels, including labels equipped with no stable or decidable equality. -/
def observationalEq {X : Type} (p : LimitPseudometric X) : Setoid X where
  r x y := p.dist x y=zero
  iseqv := ⟨p.self,fun {a b} h => (p.symmetric b a).trans h,by
    intro x y z xy yz
    have h := p.triangle x y z
    rw [xy,yz,addZero] at h
    exact valueAntisymmetric _ _ h (p.nonnegative _ _)⟩

private theorem sameLeftPort {X : Type} (p : LimitPseudometric X) {x y : X} (h : p.dist x y=zero)
    (z : X) : p.dist x z=p.dist y z := by
  have one := p.triangle x y z
  have two := p.triangle y x z
  rw [h,zeroAdd] at one
  rw [p.symmetric y x,h,zeroAdd] at two
  exact valueAntisymmetric _ _ one two

def collapsedDist {X : Type} (p : LimitPseudometric X) (x y : Quotient (observationalEq p)) : Value :=
  Quotient.liftOn₂ x y p.dist (fun a b c d ac bd => by
    rw [sameLeftPort p ac b,p.symmetric c b,sameLeftPort p bd c,p.symmetric d c])

/-- The measured quotient is a genuine metric without adding a classical
    separation axiom, including when distinct declared labels collapse. -/
def operationalMetric {X : Type} (p : LimitPseudometric X) : LimitMetric (Quotient (observationalEq p)) where
  dist := collapsedDist p
  nonnegative x y := Quotient.inductionOn₂ x y p.nonnegative
  self x := Quotient.inductionOn x p.self
  symmetric x y := Quotient.inductionOn₂ x y p.symmetric
  triangle x y z := by
    induction x using Quotient.inductionOn with
    | _ x =>
      induction y using Quotient.inductionOn with
      | _ y =>
        induction z using Quotient.inductionOn with
        | _ z => exact p.triangle x y z
  separates x y := Quotient.inductionOn₂ x y fun _ _ h => Quotient.sound h

/-- SignalNetwork.experiment supplies these fields from actual arrivals on a
    directed graph with cycles; symmetry is needed only for limiting readings. -/
def fromExperiments {X : Type} (e : Nat → Experiment X)
    (hc : ∀ x y, Cauchy (fun n => cost (e n) x y))
    (rev : ∀ x y, Close (fun n => cost (e n) x y) (fun n => cost (e n) y x)) :
    LimitPseudometric X :=
  fromReadings (fun n => cost (e n)) hc (fun n x => (zeroIffSame (e n) x x).2 rfl) rev
    (fun n => triangleFromRelay (e n))

theorem positiveGeometryIff {X : Type} (e : Nat → Experiment X)
    (hc : ∀ x y, Cauchy (fun n => cost (e n) x y))
    (rev : ∀ x y, Close (fun n => cost (e n) x y) (fun n => cost (e n) y x)) :
    (∀ x y, x ≠ y → Positive ((fromExperiments e hc rev).dist x y)) ↔
      ∀ x y, x ≠ y → PositiveTail (fun n => cost (e n) x y) := Iff.rfl

private theorem dyadicAtLater {p m : Nat} (a : Nat) (pm : p ≤ m) :
    dyadic a p = dyadic (2^(m-p)*a) m := by
  have eq (n : Nat) (mn : m ≤ n) : 2^(n-p)*a = 2^(n-m)*(2^(m-p)*a) := by
    rw [← Nat.mul_assoc,refineExtend pm mn]
  exact Quotient.sound ⟨dominatesEventually (fun n h => Nat.le_of_eq (eq n h)),
                          dominatesEventually (fun n h => Nat.le_of_eq (eq n h).symm)⟩

private theorem sameDyadicSum (a b m : Nat) : add (dyadic a m) (dyadic b m) = dyadic (a+b) m := by
  exact Quotient.sound ⟨dominatesPointwise (fun n => Nat.le_of_eq (Nat.mul_add (2^(n-m)) a b).symm),
                        dominatesPointwise (fun n => Nat.le_of_eq (Nat.mul_add (2^(n-m)) a b))⟩

theorem dyadicOrder (a b m : Nat) : valueLE (dyadic a m) (dyadic b m) ↔ a ≤ b := by
  constructor
  · intro h
    obtain ⟨N,hN⟩ := h (m+1)
    let t := max N m
    have mt : m ≤ t := Nat.le_max_right _ _
    have bound := hN t (Nat.le_max_left _ _)
    change 2^(m+1)*(2^(t-m)*a) ≤ 2^(m+1)*(2^(t-m)*b)+2^t at bound
    simp only [double,← Nat.mul_assoc,powerDiff mt] at bound
    have hmul : 2^t*(a+a) ≤ 2^t*(b+b+1) := by
      simpa only [Nat.mul_add,Nat.add_mul,Nat.mul_one] using bound
    have small := Nat.le_of_mul_le_mul_left hmul (Nat.pow_pos (n:=t) (by decide))
    omega
  · intro h; exact dominatesPointwise (fun n => Nat.mul_le_mul_left (2^(n-m)) h)

private theorem unpackTolerance {a b m k : Nat} (km : k ≤ m)
    (h : valueLE (dyadic a m) (add (dyadic b m) (dyadic 1 k))) : 2^k*a ≤ 2^k*b+2^m := by
  rw [dyadicAtLater 1 km,Nat.mul_one,sameDyadicSum,dyadicOrder] at h
  simpa only [Nat.mul_add,powerDiff km] using Nat.mul_le_mul_left (2^k) h

/-- The Cauchy criterion is necessary for convergence to *any* Cauchy real,
    as well as sufficient for the value constructed above. -/
theorem limitExistsIffCauchy (f : Nat → Nat) : (∃ x : Value, Converges f x) ↔ Cauchy f := by
  constructor
  · rintro ⟨x,conv⟩ k
    obtain ⟨N,hN⟩ := conv (k+1)
    refine ⟨max N k,?_⟩
    intro n m hn nm
    have kn := Nat.le_trans (Nat.le_max_right _ _) hn
    have knm := Nat.le_trans kn nm
    have ln := hN n (Nat.le_trans (Nat.le_max_left _ _) hn)
    have lm := hN m (Nat.le_trans (Nat.le_max_left _ _) (Nat.le_trans hn nm))
    have step {a b : Value} (u : Near (k+1) a x) (v : Near (k+1) b x) :
        valueLE a (add b (dyadic 1 k)) := by
      rw [← doubleRadius]
      exact valueTransitive _ _ _ u.1 (addRightMonotone _ _ _ v.2)
    have one := step lm ln
    have two := step ln lm
    rw [dyadicAtLater (f n) nm] at one two
    exact ⟨unpackTolerance knm one,unpackTolerance knm two⟩
  · intro h; exact ⟨_,nameConverges f h⟩

end OperationalNetwork.Continuum
