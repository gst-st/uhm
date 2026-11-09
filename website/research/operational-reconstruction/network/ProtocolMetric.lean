import Std
set_option autoImplicit false
namespace OperationalNetwork

/-- Exhaust an observed or decidable protocol table through a witnessed
    attainable bound. No metric or graph is an input. -/
def scan (p : Nat → Bool) : Nat → Nat
  | 0 => 0
  | n+1 => if p (scan p n) then scan p n else n+1

theorem scanBound (p : Nat → Bool) (n : Nat) : scan p n ≤ n := by
  induction n with
  | zero => exact Nat.le_refl _
  | succ n ih => unfold scan; split <;> omega

theorem scanWitness (p : Nat → Bool) (b t : Nat) (ht : t≤b) (pass : p t=true) :
    p (scan p b)=true ∧ scan p b ≤ t := by
  induction b with
  | zero => have e : t=0 := by omega
            subst t; exact ⟨pass,Nat.le_refl _⟩
  | succ b ih =>
    unfold scan
    by_cases early : t ≤ b
    · have ans := ih early
      rw [ite_eq_left ans.1]
      exact ans
    · have e : t=b+1 := by omega
      subst t
      split
      · rename_i h; exact ⟨h,Nat.le_trans (scanBound p b) (Nat.le_succ _)⟩
      · exact ⟨pass,Nat.le_refl _⟩

structure Experiment (X : Type) where
  hit : X → X → Nat → Bool
  bound : X → X → Nat
  witnessed : ∀ x y, hit x y (bound x y)=true
  idle : ∀ x, hit x x 0=true
  separates : ∀ x y, hit x y 0=true → x=y
  compose : ∀ x y z a b, hit x y a=true → hit y z b=true →
      ∃ k, k ≤ a+b ∧ hit x z k=true

def cost {X : Type} (e : Experiment X) (x y : X) := scan (e.hit x y) (e.bound x y)

theorem attains {X : Type} (e : Experiment X) (x y : X) :
    e.hit x y (cost e x y)=true :=
  (scanWitness _ _ _ (Nat.le_refl _) (e.witnessed x y)).1

theorem leastCost {X : Type} (e : Experiment X) (x y : X) (t : Nat)
    (hit : e.hit x y t=true) : cost e x y ≤ t := by
  by_cases h : t ≤ e.bound x y
  · exact (scanWitness _ _ _ h hit).2
  · exact Nat.le_trans (scanBound _ _) (by omega)

theorem triangleFromRelay {X : Type} (e : Experiment X) (x y z : X) :
    cost e x z ≤ cost e x y + cost e y z := by
  obtain ⟨k,hk,h⟩ := e.compose x y z _ _ (attains e x y) (attains e y z)
  exact Nat.le_trans (leastCost e x z k h) hk

def Reciprocal {X : Type} (e : Experiment X) : Prop :=
  ∀ x y t, e.hit x y t=true → ∃ k, k≤t ∧ e.hit y x k=true

theorem symmetricIffReciprocal {X : Type} (e : Experiment X) :
    (∀ x y, cost e x y=cost e y x) ↔ Reciprocal e := by
  constructor
  · intro h x y t ok
    exact ⟨_,h x y ▸ leastCost e x y t ok,attains e y x⟩
  · intro h
    have le (x y : X) : cost e y x ≤ cost e x y := by
      obtain ⟨k,hk,ok⟩ := h x y _ (attains e x y)
      exact Nat.le_trans (leastCost e y x k ok) hk
    intro x y; exact Nat.le_antisymm (le y x) (le x y)

theorem zeroIffSame {X : Type} (e : Experiment X) (x y : X) :
    cost e x y=0 ↔ x=y := by
  constructor
  · intro h; exact e.separates x y (h ▸ attains e x y)
  · rintro rfl; exact Nat.eq_zero_of_le_zero (leastCost e x x 0 (e.idle x))

/-- Observational simulation, pointwise with a cost witness. -/
def Covers {X : Type} (e f : Experiment X) : Prop :=
  ∀ x y t, f.hit x y t=true → ∃ k, k≤t ∧ e.hit x y k=true

theorem coversIffCosts {X : Type} (e f : Experiment X) :
    Covers e f ↔ ∀ x y, cost e x y ≤ cost f x y := by
  constructor
  · intro h x y
    obtain ⟨k,hk,ok⟩ := h x y _ (attains f x y)
    exact Nat.le_trans (leastCost e x y k ok) hk
  · intro h x y t ok
    exact ⟨_,Nat.le_trans (h x y) (leastCost f x y t ok),attains e x y⟩

theorem sameMetricIffCoverBoth {X : Type} (e f : Experiment X) :
    (∀ x y, cost e x y=cost f x y) ↔ Covers e f ∧ Covers f e := by
  constructor
  · intro h
    exact ⟨(coversIffCosts _ _).2 (fun x y => by rw [h x y]; exact Nat.le_refl _),
           (coversIffCosts _ _).2 (fun x y => by rw [h x y]; exact Nat.le_refl _)⟩
  · rintro ⟨h,k⟩ x y
    exact Nat.le_antisymm ((coversIffCosts _ _).1 h x y) ((coversIffCosts _ _).1 k x y)

/-- Uniform overhead per completed transmission. With one bound in each
    direction this yields an error bar on every reconstructed distance. -/
theorem overheadIffCosts {X : Type} (e f : Experiment X) (slack : Nat) :
    (∀ x y t, f.hit x y t=true → ∃ k, k≤t+slack ∧ e.hit x y k=true) ↔
    (∀ x y, cost e x y ≤ cost f x y + slack) := by
  constructor
  · intro sim x y
    obtain ⟨k,hk,run⟩ := sim x y _ (attains f x y)
    exact Nat.le_trans (leastCost e x y k run) hk
  · intro h x y t ok
    exact ⟨_,Nat.le_trans (h x y) (Nat.add_le_add_right (leastCost f x y t ok) _),attains e x y⟩

#print axioms overheadIffCosts

-- A one-tick crossbar on any decidable register, with optional waiting.
def crossbar (X : Type) [DecidableEq X] : Experiment X where
  hit x y t := decide (x=y ∨ 0<t)
  bound _ _ := 1
  witnessed _ _ := decide_eq_true (Or.inr (by decide))
  idle x := decide_eq_true (Or.inl rfl)
  separates _ _ h := by simpa using h
  compose x y z a b hx hy := by
    refine ⟨a+b,Nat.le_refl _,decide_eq_true ?_⟩
    rcases of_decide_eq_true hx with eq|lt <;> rcases of_decide_eq_true hy with eq'|lt'
    · exact Or.inl (eq.trans eq')
    all_goals exact Or.inr (by omega)

theorem crossbarReciprocal (X : Type) [DecidableEq X] : Reciprocal (crossbar X) := by
  intro x y t h
  refine ⟨t,Nat.le_refl _,?_⟩
  change decide (y=x ∨ 0<t)=true
  rcases of_decide_eq_true h with eq|lt
  · exact decide_eq_true (Or.inl eq.symm)
  · exact decide_eq_true (Or.inr lt)

-- A directional two-state switch needs one tick going out and a second tick
-- for the return handshake. Both transitions admit waiting.
def handshakeTime : Bool → Bool → Nat
  | false,true => 1
  | true,false => 2
  | _,_ => 0

def handshake : Experiment Bool where
  hit x y t := decide (handshakeTime x y ≤ t)
  bound := handshakeTime
  witnessed _ _ := decide_eq_true (Nat.le_refl _)
  idle x := by cases x <;> decide
  separates x y h := by cases x <;> cases y <;> first | rfl | (contradiction)
  compose x y z a b ha hb := by
    have ab := of_decide_eq_true ha
    have bc := of_decide_eq_true hb
    refine ⟨a+b,Nat.le_refl _,decide_eq_true ?_⟩
    cases x <;> cases y <;> cases z <;> simp only [handshakeTime] at * <;> omega

theorem asymmetricWitness :
    cost handshake false true=1 ∧ cost handshake true false=2 := by decide

#print axioms asymmetricWitness
#print axioms triangleFromRelay
#print axioms symmetricIffReciprocal
#print axioms zeroIffSame
#print axioms sameMetricIffCoverBoth
#print axioms crossbarReciprocal
end OperationalNetwork
