import Response
set_option autoImplicit false
namespace OperationalNetwork
open Lean.Grind AddCommMonoid

/-- Additive transfer between potentially different boundary and interior registers. -/
structure AdditiveTransfer (X Y : Type) [AddCommMonoid X] [AddCommMonoid Y] where
  send : X → Y
  silent : send 0 = 0
  distribute : ∀ x y, send (x+y) = send x + send y

structure BoundaryNetwork (V H : Type) [AddCommMonoid V] [AddCommMonoid H] where
  direct : AdditiveTransfer V V -- A
  exit : AdditiveTransfer H V -- B
  enter : AdditiveTransfer V H -- C
  inside : AdditiveTransfer H H -- D

variable {V H : Type} [AddCommMonoid V] [AddCommMonoid H]

/-- Full hidden-to-boundary release B D^k; retaining this term accounts for
    the preparation of the interior before the first recorded boundary tick. -/
def release (s : BoundaryNetwork V H) : Nat → H → V
  | 0, h => s.exit.send h
  | k+1, h => release s k (s.inside.send h)

private theorem releaseZero (s : BoundaryNetwork V H) (k : Nat) : release s k 0 = 0 := by
  induction k with
  | zero => exact s.exit.silent
  | succ k ih => rw [release,s.inside.silent,ih]

private theorem releaseAdd (s : BoundaryNetwork V H) (k : Nat) (x y : H) :
    release s k (x+y) = release s k x + release s k y := by
  induction k generalizing x y with
  | zero => exact s.exit.distribute _ _
  | succ k ih => rw [release,s.inside.distribute,ih]; rfl

/-- Delayed transfer B D^k C; the first port contributes a two-tick delay
    (one tick to enter and one to exit) between the original input and output. -/
def echoKernel (s : BoundaryNetwork V H) (k : Nat) (v : V) := release s k (s.enter.send v)

private theorem echoZero (s : BoundaryNetwork V H) (k : Nat) : echoKernel s k 0 = 0 := by
  simp only [echoKernel,s.enter.silent,releaseZero]

/-- Histories are newest first. The age of the latest entry in a complete
    history is zero; there is no initial-state contribution in this sum. -/
def delayedSum (s : BoundaryNetwork V H) (age : Nat) : List V → V
  | [] => 0
  | v::vs => echoKernel s age v + delayedSum s (age+1) vs

def interiorAfter (s : BoundaryNetwork V H) (h₀ : H) : List V → H
  | [] => h₀
  | b::older => s.enter.send b + s.inside.send (interiorAfter s h₀ older)

theorem interiorUnroll (s : BoundaryNetwork V H) (h₀ : H) (history : List V) (k : Nat) :
    release s k (interiorAfter s h₀ history) =
      release s (k + history.length) h₀ + delayedSum s k history := by
  induction history generalizing k with
  | nil => simp [interiorAfter, delayedSum, add_zero]
  | cons b older ih =>
    rw [interiorAfter,releaseAdd]
    change echoKernel s k b + release s (k+1) (interiorAfter s h₀ older) = _
    rw [ih]
    simp only [delayedSum,List.length_cons,show k+(older.length+1)=(k+1)+older.length by omega,
      add_left_comm]

def coupledRun (s : BoundaryNetwork V H) (b₀ : V) (h₀ : H) : Nat → V × H
  | 0 => (b₀,h₀)
  | t+1 =>
    let (b,h) := coupledRun s b₀ h₀ t
    (s.direct.send b + s.exit.send h, s.enter.send b + s.inside.send h)

/-- Executable evolution on the boundary alone, with its previously observed
    values and the release from the declared initial interior preparation. -/
def boundaryReplay (s : BoundaryNetwork V H) (b₀ : V) (h₀ : H) : Nat → V × List V
  | 0 => (b₀,[])
  | t+1 =>
    let (b,older) := boundaryReplay s b₀ h₀ t
    (s.direct.send b + (release s t h₀ + delayedSum s 0 older), b::older)

theorem boundaryReplayExact (s : BoundaryNetwork V H) (b₀ : V) (h₀ : H) (t : Nat) :
    (coupledRun s b₀ h₀ t).1 = (boundaryReplay s b₀ h₀ t).1 ∧
    (coupledRun s b₀ h₀ t).2 = interiorAfter s h₀ (boundaryReplay s b₀ h₀ t).2 ∧
    (boundaryReplay s b₀ h₀ t).2.length = t := by
  induction t with
  | zero => exact ⟨rfl,rfl,rfl⟩
  | succ t ih =>
    obtain ⟨visible,hidden,steps⟩ := ih
    simp only [coupledRun,boundaryReplay,List.length_cons,steps,visible,hidden]
    constructor
    · rw [show s.exit.send (interiorAfter s h₀ (boundaryReplay s b₀ h₀ t).2) =
          release s 0 (interiorAfter s h₀ (boundaryReplay s b₀ h₀ t).2) from rfl,
        interiorUnroll, Nat.zero_add, steps]
    · exact ⟨rfl,True.intro⟩

theorem boundaryFirstAt {Z : Type} (s : BoundaryNetwork V H) (b₀ : V) (h₀ : H)
    (observe : V → Z) (quiet : Z) (t : Nat) :
    FirstAt quiet (fun n => observe (coupledRun s b₀ h₀ n).1) t ↔
      FirstAt quiet (fun n => observe (boundaryReplay s b₀ h₀ n).1) t := by
  simp only [fun n => (boundaryReplayExact s b₀ h₀ n).1]

private theorem matchingHistory {J : Type} [AddCommMonoid J] (p : BoundaryNetwork V H)
    (q : BoundaryNetwork V J) (transfer : ∀ k v, echoKernel p k v = echoKernel q k v)
    (history : List V) (k : Nat) : delayedSum p k history = delayedSum q k history := by
  induction history generalizing k with
  | nil => rfl
  | cons v older ih => rw [delayedSum,delayedSum,transfer,ih]

/-- The hidden registers and interior operators of the two probes can differ.
    Agreement of direct response, delayed response kernels and prepared-state
    release preserves every boundary reading and hence every arrival time. -/
theorem matchedBoundaryProbes {J : Type} [AddCommMonoid J]
    (p : BoundaryNetwork V H) (q : BoundaryNetwork V J) (h : H) (j : J) (b : V)
    (direct : ∀ v, p.direct.send v = q.direct.send v)
    (transfer : ∀ k v, echoKernel p k v = echoKernel q k v)
    (prepared : ∀ k, release p k h = release q k j) (t : Nat) :
    (coupledRun p b h t).1 = (coupledRun q b j t).1 := by
  have traces (n : Nat) : boundaryReplay p b h n = boundaryReplay q b j n := by
    induction n with
    | zero => rfl
    | succ n ih => simp only [boundaryReplay, ih, direct, prepared, matchingHistory p q transfer]
  rw [(boundaryReplayExact p b h t).1, (boundaryReplayExact q b j t).1, traces]

private theorem sumBeyond (s : BoundaryNetwork V H) (age : Nat) (hist : List V)
    (quiet : ∀ k, age ≤ k → ∀ b, echoKernel s k b = 0) : delayedSum s age hist = 0 := by
  induction hist generalizing age with
  | nil => rfl
  | cons b older ih =>
    rw [delayedSum, quiet _ (by omega), ih (age+1) (fun k hk => quiet k (by omega)),add_zero]

private theorem truncatedHistory (s : BoundaryNetwork V H) (age L : Nat) (hist : List V)
    (quiet : ∀ k, age + L ≤ k → ∀ b, echoKernel s k b = 0) :
    delayedSum s age hist = delayedSum s age (hist.take L) := by
  induction hist generalizing age L with
  | nil => cases L <;> rfl
  | cons b older ih =>
    cases L with
    | zero => exact sumBeyond s age _ (fun k hk => quiet k (by omega))
    | succ L =>
      simp only [List.take_succ_cons,delayedSum]
      rw [← ih (age+1) L (fun k hk => quiet k (by omega))]

private theorem emptyHistory (s : BoundaryNetwork V H) (k n : Nat) :
    delayedSum s k (List.replicate n 0) = 0 := by
  induction n generalizing k with
  | zero => rfl
  | succ n ih => rw [List.replicate_succ,delayedSum,echoZero,ih,add_zero]

private theorem delayedImpulse (s : BoundaryNetwork V H) (k n : Nat) (b : V) :
    delayedSum s k (List.replicate n 0 ++ [b]) = echoKernel s (k+n) b := by
  induction n generalizing k with
  | zero => simp [delayedSum,add_zero]
  | succ n ih =>
    simp only [List.replicate_succ,List.cons_append,delayedSum,echoZero,zero_add,ih]
    rw [show k+(n+1) = (k+1)+n by omega]

/-- Retaining the most recent L past readings suffices to reproduce the history
    contribution for all independently prescribed boundary histories iff the
    tail B D^k C vanishes for k ≥ L. The prepared-interior term B D^t h₀
    is still included separately in boundaryReplay. -/
theorem exactMemoryCutoff (s : BoundaryNetwork V H) (L : Nat) :
    (∀ hist, delayedSum s 0 hist = delayedSum s 0 (hist.take L)) ↔
    ∀ k, L ≤ k → ∀ b, echoKernel s k b = 0 := by
  constructor
  · intro cutoff k hk b
    have h := cutoff (List.replicate k 0 ++ [b])
    rw [delayedImpulse,Nat.zero_add,List.take_append_of_le_length (by simpa using hk),
      List.take_replicate,emptyHistory] at h
    exact h
  · intro tail hist; exact truncatedHistory s 0 L hist (by simpa using tail)

/-- Three stations in a directed loop. The boundary sees one station; two
    successive equal readings in a *single*, fully prepared trajectory lead
    to different next readings. -/
private structure TwoCells where
  near : Int
  far : Int
private theorem twoCellCongr {a b c d : Int} (one : a=c) (two : b=d) :
    TwoCells.mk a b = TwoCells.mk c d := by cases one; cases two; rfl
private instance : AddCommMonoid TwoCells where
  zero := ⟨0,0⟩
  add x y := ⟨x.near+y.near, x.far+y.far⟩
  add_zero x := by cases x with | mk a b =>
    exact twoCellCongr (Int.add_zero a) (Int.add_zero b)
  add_comm x y := twoCellCongr (Int.add_comm x.near y.near) (Int.add_comm x.far y.far)
  add_assoc x y z := twoCellCongr (Int.add_assoc x.near y.near z.near)
    (Int.add_assoc x.far y.far z.far)

private def threeCycle : BoundaryNetwork Int TwoCells where
  direct := ⟨fun _ => 0,rfl,fun _ _ => rfl⟩
  exit := ⟨TwoCells.far,rfl,fun _ _ => rfl⟩
  enter := ⟨fun v => ⟨v,0⟩,rfl,fun _ _ => rfl⟩
  inside := ⟨fun h => ⟨0,h.near⟩,rfl,fun _ _ => rfl⟩

theorem loopRequiresHistory :
    let seen := fun t => (coupledRun threeCycle 1 0 t).1
    seen 1 = 0 ∧ seen 2 = 0 ∧ seen 3 = 1 ∧
    ¬ ∃ f : Int → Int, ∀ t, seen (t+1) = f (seen t) := by
  dsimp only
  refine ⟨rfl,rfl,rfl,?_⟩
  rintro ⟨f,law⟩
  have h := law 1
  have j := law 2
  change 0 = f 0 at h
  change 1 = f 0 at j
  omega

end OperationalNetwork
