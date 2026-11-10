import Std
set_option autoImplicit false

namespace PhenomenalAccess
universe u v w

/-- A proposed attribution is a function of accessible classes exactly when
    no indistinguishable pair gets different attributions. Quot.lift constructs
    the decoder. No sections, choice of representative or finite search. -/
theorem descendsExactly {S : Type u} {L : Type v} (indist : S → S → Prop)
    (label : S → L) :
    (∃ decode : Quot indist → L, ∀ s, decode (Quot.mk indist s) = label s) ↔
      ∀ s t, indist s t → label s = label t := by
  constructor
  · rintro ⟨decode,h⟩ s t eq
    exact (h s).symm.trans ((congrArg decode (Quot.sound eq)).trans (h t))
  · intro respect
    exact ⟨Quot.lift label (fun s t h => respect s t h),fun _ => rfl⟩

theorem decoderUnique {S : Type u} {L : Type v} (indist : S → S → Prop)
    (f g : Quot indist → L) (h : ∀ s, f (Quot.mk indist s) = g (Quot.mk indist s)) :
    ∀ q, f q = g q := by
  intro q; exact Quot.inductionOn q h

/-- Each name in a calibrated catalogue has an actual example.
    The section is supplied as experimental data rather than chosen as an axiom. -/
structure Catalogue (S : Type u) (L : Type v) where
  name : S → L
  exampleOf : L → S
  realizes : ∀ l, name (exampleOf l) = l

theorem sameDistinctions {S : Type u} {A : Type v} {B : Type w}
    (a : Catalogue S A) (b : Catalogue S B)
    (agree : ∀ s t, a.name s = a.name t ↔ b.name s = b.name t) :
    ∃ f : A → B, ∃ g : B → A,
      (∀ s, f (a.name s) = b.name s) ∧ (∀ s, g (b.name s) = a.name s) ∧
      (∀ x, g (f x) = x) ∧ (∀ y, f (g y) = y) ∧
      (∀ f' : A → B, (∀ s, f' (a.name s) = b.name s) → ∀ x, f' x = f x) := by
  let f := fun x => b.name (a.exampleOf x)
  let g := fun y => a.name (b.exampleOf y)
  have hf (s) : f (a.name s) = b.name s := (agree _ _).mp (a.realizes _)
  have hg (s) : g (b.name s) = a.name s := (agree _ _).mpr (b.realizes _)
  refine ⟨f,g,hf,hg,fun x => (hg (a.exampleOf x)).trans (a.realizes x),
    fun y => (hf (b.exampleOf y)).trans (b.realizes y),?_⟩
  intro f' h x
  exact (congrArg f' (a.realizes x)).symm.trans (h (a.exampleOf x))

/-- Even an exact catalogue of equality comparisons cannot identify names:
    identity and complement differ at each input, but induce the same relation. -/
theorem inversion (s t : Bool) : (s=t ↔ (!s)=(!t)) ∧ (s ≠ !s) := by
  cases s <;> cases t <;> decide

/-- Direct and indirect translations can be compared on held-out episodes.
    Truth of an edge means agreement with the recorded target name, not that an
    arbitrary hidden quality has been measured. The three alphabets may differ. -/
def errors {S : Type u} (bad : S → Bool) (episodes : List S) : Nat :=
  match episodes with
  | [] => 0
  | e :: es => (if bad e then 1 else 0) + errors bad es

theorem transferTriangle {S A B C : Type} [DecidableEq B] [DecidableEq C]
    (a : S → A) (b : S → B) (c : S → C)
    (ab : A → B) (bc : B → C) (ac : A → C) (episodes : List S) :
    errors (fun e => decide (bc (ab (a e)) ≠ ac (a e))) episodes ≤
    errors (fun e => decide (ab (a e) ≠ b e)) episodes +
    errors (fun e => decide (bc (b e) ≠ c e)) episodes +
    errors (fun e => decide (ac (a e) ≠ c e)) episodes := by
  induction episodes with
  | nil => simp [errors]
  | cons e es ih =>
    have point : (if bc (ab (a e)) ≠ ac (a e) then 1 else 0) ≤
        (if ab (a e) ≠ b e then 1 else 0) + (if bc (b e) ≠ c e then 1 else 0) +
        (if ac (a e) ≠ c e then 1 else 0) := by
      by_cases h₁ : ab (a e) = b e <;> by_cases h₂ : bc (b e) = c e <;>
        by_cases h₃ : ac (a e) = c e <;> simp_all <;> split <;> omega
    simp only [errors, decide_eq_true_eq]
    omega

end PhenomenalAccess
