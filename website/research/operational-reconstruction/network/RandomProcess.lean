import OperationalProcess

set_option autoImplicit false
namespace OperationalNetwork.Process

/-- A nonnegative, subunit rational, before identifying changes of denominator. -/
structure CountRatio where
  hits : Nat
  trials : Nat
  positive : 0 < trials
  bounded : hits ≤ trials

namespace CountRatio

abbrev same (a b : CountRatio) := a.hits * b.trials = b.hits * a.trials

def proportional : Setoid CountRatio where
  r := same
  iseqv := ⟨fun _ => rfl, fun h => h.symm, by
    intro a b c ab bc
    apply Nat.eq_of_mul_eq_mul_right b.positive
    change _ = _ at ab bc
    calc
      a.hits * c.trials * b.trials = (a.hits * b.trials) * c.trials := by ac_rfl
      _ = (b.hits * c.trials) * a.trials := by rw [ab]; ac_rfl
      _ = c.hits * a.trials * b.trials := by rw [bc]; ac_rfl⟩

def average (a b : CountRatio) : CountRatio where
  hits := a.hits * b.trials + b.hits * a.trials
  trials := 2 * (a.trials * b.trials)
  positive := Nat.mul_pos (by decide) (Nat.mul_pos a.positive b.positive)
  bounded := by
    have ha := Nat.mul_le_mul_right b.trials a.bounded
    have hb := Nat.mul_le_mul_right a.trials b.bounded
    simpa only [Nat.two_mul, Nat.mul_comm b.trials a.trials] using Nat.add_le_add ha hb

private theorem averageRespects {a b c d : CountRatio} (ac : same a c) (bd : same b d) :
    same (average a b) (average c d) := by
  change a.hits * c.trials = c.hits * a.trials at ac
  change b.hits * d.trials = d.hits * b.trials at bd
  unfold same average
  simp only [Nat.add_mul]
  calc
    _ = (a.hits*c.trials)*(2*(b.trials*d.trials)) +
        (b.hits*d.trials)*(2*(a.trials*c.trials)) := by ac_rfl
    _ = _ := by rw [ac,bd]; ac_rfl

end CountRatio

abbrev Chance := Quotient CountRatio.proportional

namespace Chance

def never : Chance := Quotient.mk _ ⟨0,1,by decide,by decide⟩
def sure : Chance := Quotient.mk _ ⟨1,1,by decide,by decide⟩

def mean : Chance → Chance → Chance :=
  Quotient.lift₂ (fun a b => Quotient.mk _ (a.average b))
    (fun _ _ _ _ ac bd => Quotient.sound (CountRatio.averageRespects ac bd))

theorem endpointsDiffer : never ≠ sure :=
  fun h => (by decide : ¬ CountRatio.same ⟨0,1,by decide,by decide⟩
    ⟨1,1,by decide,by decide⟩) (Quotient.exact h)

private theorem meanZero : mean never never = never :=
  Quotient.sound (by decide : CountRatio.same _ _)

private theorem meanExchange (a b c d : Chance) :
    mean (mean a b) (mean c d) = mean (mean a c) (mean b d) := by
  induction a using Quotient.inductionOn with | _ a =>
   induction b using Quotient.inductionOn with | _ b =>
    induction c using Quotient.inductionOn with | _ c =>
     induction d using Quotient.inductionOn with | _ d =>
      apply Quotient.sound
      change CountRatio.same ((a.average b).average (c.average d))
        ((a.average c).average (b.average d))
      simp only [CountRatio.same,CountRatio.average,Nat.add_mul]
      ac_rfl

end Chance

/-- Independent fair-coin branches. A stopped branch contributes zero to
    the selected event; its weight stays in the total population. -/
inductive Sample (A : Type) where
  | stop
  | yield (x : A)
  | coin (left right : Sample A)

namespace Sample

def bind {A B : Type} (p : Sample A) (k : A → Sample B) : Sample B :=
  match p with
  | .stop => .stop
  | .yield x => k x
  | .coin l r => .coin (l.bind k) (r.bind k)

def expect {A : Type} (p : Sample A) (f : A → Chance) : Chance :=
  match p with
  | .stop => Chance.never
  | .yield x => f x
  | .coin l r => Chance.mean (l.expect f) (r.expect f)

/-- Every expectation admits an exact rational representative in [0,1]. -/
theorem probability {A : Type} (p : Sample A) (f : A → Chance) :
    ∃ r : CountRatio, p.expect f = Quotient.mk _ r ∧ 0 < r.trials ∧ r.hits ≤ r.trials := by
  induction p.expect f using Quotient.inductionOn with
  | _ r => exact ⟨r,rfl,r.positive,r.bounded⟩

theorem expectBind {A B : Type} (p : Sample A) (k : A → Sample B) (f : B → Chance) :
    (p.bind k).expect f = p.expect (fun x => (k x).expect f) := by
  induction p with
  | stop | yield => rfl
  | coin _ _ il ir => simp only [bind,expect,il,ir]

def product {A B : Type} (p : Sample A) (q : Sample B) : Sample (A × B) :=
  p.bind (fun x => q.bind (fun y => .yield (x,y)))

theorem expectProduct {A B : Type} (p : Sample A) (q : Sample B) (f : A × B → Chance) :
    (p.product q).expect f = p.expect (fun x => q.expect (fun y => f (x,y))) := by
  simp only [product,expectBind,expect]

private theorem expectMean {A : Type} (p : Sample A) (f g : A → Chance) :
    p.expect (fun x => Chance.mean (f x) (g x)) = Chance.mean (p.expect f) (p.expect g) := by
  induction p with
  | stop => exact Chance.meanZero.symm
  | yield => rfl
  | coin _ _ il ir =>
    change Chance.mean _ _ = _
    rw [il,ir]
    exact Chance.meanExchange _ _ _ _

private theorem zeroResponse {A : Type} (p : Sample A) :
    p.expect (fun _ => Chance.never) = Chance.never := by
  induction p with
  | stop | yield => rfl
  | coin _ _ il ir => simpa only [expect,il,ir] using Chance.meanZero

theorem independentOrder {A B : Type} (p : Sample A) (q : Sample B) (f : A → B → Chance) :
    p.expect (fun a => q.expect (f a)) = q.expect (fun b => p.expect (fun a => f a b)) := by
  induction p with
  | stop => exact (zeroResponse q).symm
  | yield => rfl
  | coin _ _ il ir =>
    change Chance.mean _ _ = _
    rw [il,ir]
    exact (expectMean q _ _).symm

end Sample

abbrev coinLab (n : Nat) : Lab where
  Wire := Wire
  unit := .empty
  pair := .pair
  Proc a b := values n a → Sample (values n b)
  after p q x := (p x).bind q
  alongside p q x := (p x.1).product (q x.2)
  Record := Chance
  read p := (p ()).expect (fun _ => Chance.sure)

/-- A closed experiment with one successful branch and one failed selection.
    The recorded probability includes both original branches. -/
def halfSelection {n : Nat} : (coinLab n).Proc .empty .empty :=
  fun _ => .coin (.yield ()) .stop

theorem closedHalf (n : Nat) :
    (coinLab n).read halfSelection = Quotient.mk _ ⟨1,2,by decide,by decide⟩ := by
  apply Quotient.sound
  change (1 * 2 : Nat) = 1 * 2
  rfl

def certain {n : Nat} (x : Fin n) : (coinLab n).Proc .empty .cell := fun _ => .yield x
/-- The same apparatus reports the full output symbol on every run.
    A later event selection can coarse-grain the returned pointer value. -/
def symbolPointer {n : Nat} : (coinLab n).Proc .cell .cell :=
  fun x => .yield x

def pointerRecord {n : Nat} (p : (coinLab n).Proc .empty .cell) : Sample (Fin n) :=
  (coinLab n).after p symbolPointer ()

theorem pointerPreserves {n : Nat} (p : (coinLab n).Proc .empty .cell) :
    pointerRecord p = p () := by
  change (p ()).bind Sample.yield = p ()
  induction p () with
  | stop | yield => rfl
  | coin _ _ hl hr => simp only [Sample.bind,hl,hr]

theorem pointerDecodes {n : Nat} (x : Fin n) :
    pointerRecord (certain x) = .yield x := rfl

def eventFilter {n : Nat} (keep : Fin n → Bool) : (coinLab n).Proc .cell .empty :=
  fun y => if keep y then .yield () else .stop

theorem pointerEvent {n : Nat} (p : (coinLab n).Proc .empty .cell) (keep : Fin n → Bool) :
    observe (.thenDo (L:=coinLab n) symbolPointer (.thenDo (eventFilter keep) .closed)) p =
      (pointerRecord p).expect (fun y => if keep y then Chance.sure else Chance.never) := by
  change ((pointerRecord p).bind (fun y : Fin n => if keep y then (Sample.yield () : Sample Unit) else .stop)).expect (fun _ => Chance.sure) = _
  rw [Sample.expectBind]
  apply congrArg (Sample.expect (pointerRecord p))
  funext y
  change (if keep y then Sample.yield () else .stop).expect (fun _ => Chance.sure) = _
  split <;> rfl

def equalityFilter {n : Nat} (z : Fin n) : (coinLab n).Proc .cell .empty :=
  fun (y : Fin n) => if y=z then .yield () else .stop

theorem pointerSingleton {n : Nat} (p : (coinLab n).Proc .empty .cell) (z : Fin n) :
    observe (.thenDo (L:=coinLab n) (equalityFilter z) .closed) p =
      (pointerRecord p).expect (fun y => if y=z then Chance.sure else Chance.never) := by
  rw [pointerPreserves]
  let seen : Sample (Fin n) := p ()
  change (seen.bind (fun y : Fin n => if y=z then (Sample.yield () : Sample Unit) else .stop)).expect (fun _ => Chance.sure) = seen.expect _
  rw [Sample.expectBind]
  apply congrArg (Sample.expect seen)
  funext y
  change (if y=z then Sample.yield () else .stop).expect (fun _ => Chance.sure) = _
  split <;> rfl

theorem readSymbol {n : Nat} (x z : Fin n) :
    observe (.thenDo (L:=coinLab n) (equalityFilter z) .closed) (certain x) =
    if x=z then Chance.sure else Chance.never := by
  change (if x=z then Sample.yield () else .stop).expect (fun _ => Chance.sure) = _
  split <;> rfl

def kernelEq {n : Nat} {a b : Wire} (p q : (coinLab n).Proc a b) :=
  ∀ x (f : values n b → Chance), (p x).expect f = (q x).expect f

theorem kernelSubstitution {n : Nat} {a b : Wire} {p q : (coinLab n).Proc a b}
    (h : kernelEq p q) : equivalent (coinLab n) p q := by
  apply coarsest (@kernelEq n) _ _ _ _ _ h
  · intro p q e; exact e () (fun _ => Chance.sure)
  · intro a b c p q r e x f
    change ((p x).bind r).expect f = ((q x).bind r).expect f
    simpa only [Sample.expectBind] using e x (fun y => (r y).expect f)
  · intro a b c p q r e x f
    change ((r x).bind p).expect f = ((r x).bind q).expect f
    simp only [Sample.expectBind]
    exact congrArg (Sample.expect (r x)) (funext (fun y => e y f))
  · intro a b c d p q r e x f
    change values n a × values n c at x
    change values n b × values n d → Chance at f
    change ((p x.1).product _).expect f = ((q x.1).product _).expect f
    simp only [Sample.expectProduct]
    apply e
  · intro a b c d p q r e x f
    change values n c × values n a at x
    change values n d × values n b → Chance at f
    change ((r x.1).product _).expect f = ((r x.1).product _).expect f
    simp only [Sample.expectProduct]
    apply congrArg (Sample.expect (r x.1))
    funext u
    apply e

theorem coinAssociative {n : Nat} {a b c d : Wire}
    (p : (coinLab n).Proc a b) (q : (coinLab n).Proc b c) (r : (coinLab n).Proc c d) :
    equivalent (coinLab n) ((coinLab n).after ((coinLab n).after p q) r)
      ((coinLab n).after p ((coinLab n).after q r)) := by
  apply kernelSubstitution
  intro x f
  change (((p x).bind q).bind r).expect f = ((p x).bind (fun y => (q y).bind r)).expect f
  simp only [Sample.expectBind]

theorem coinInterchange {n : Nat} {a b c d e g : Wire}
    (p : (coinLab n).Proc a b) (q : (coinLab n).Proc b c)
    (r : (coinLab n).Proc d e) (s : (coinLab n).Proc e g) :
    equivalent (coinLab n)
      ((coinLab n).after ((coinLab n).alongside p r) ((coinLab n).alongside q s))
      ((coinLab n).alongside ((coinLab n).after p q) ((coinLab n).after r s)) := by
  apply kernelSubstitution
  intro x f
  change values n a × values n d at x
  change values n c × values n g → Chance at f
  rcases x with ⟨u,v⟩
  change (((p u).product (r v)).bind (fun z => (q z.1).product (s z.2))).expect f =
    (((p u).bind q).product ((r v).bind s)).expect f
  simp only [Sample.expectBind,Sample.expectProduct]
  apply congrArg (Sample.expect (p u))
  funext y
  exact Sample.independentOrder (r v) (q y) _

theorem symbolStates {n : Nat} {x z : Fin n} :
    (Quotient.mk _ (certain x) : State (coinLab n) .cell)=Quotient.mk _ (certain z) ↔ x=z := by
  constructor
  · intro h
    let t : Test (coinLab n) .empty .cell := .thenDo (equalityFilter z) .closed
    have e := congrArg (outcome t) h
    change observe t (certain x) = observe t (certain z) at e
    simp only [t,readSymbol,ite_true] at e
    by_cases same : x=z
    · exact same
    · simp [same] at e
      exact False.elim (Chance.endpointsDiffer e)
  · rintro rfl; rfl

end OperationalNetwork.Process
