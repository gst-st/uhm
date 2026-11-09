import Transport

set_option autoImplicit false
namespace OperationalNetwork

/-- Reversible traversal of a declared link. Parallel edges and self-loops retain
    their identity. A backward step uses the inverse of the *same* transport. -/
inductive LinkStep {N : Type} (E : N → N → Type) : N → N → Type where
  | forward {i j} (e : E i j) : LinkStep E i j
  | backward {i j} (e : E i j) : LinkStep E j i

inductive LinkWalk {N : Type} (E : N → N → Type) : N → N → Type where
  | idle (i : N) : LinkWalk E i i
  | next {i j k} (s : LinkStep E i j) (tail : LinkWalk E j k) : LinkWalk E i k

variable {N X : Type} {E : N → N → Type}
structure Connection (E : N → N → Type) (X : Type) where
  on : ∀ {i j}, E i j → Frame X

def stepTransport (u : Connection E X) {i j} : LinkStep E i j → Frame X
  | .forward e => u.on e
  | .backward e => inverse (u.on e)

def walkTransport (u : Connection E X) {i j} : LinkWalk E i j → Frame X
  | .idle _ => sameFrame X
  | .next s p => thenFrame (stepTransport u s) (walkTransport u p)

def appendWalk {i j k} (p : LinkWalk E i j) (q : LinkWalk E j k) : LinkWalk E i k :=
  match p with
  | .idle _ => q
  | .next s tail => .next s (appendWalk tail q)

def reverseStep {i j} : LinkStep E i j → LinkStep E j i
  | .forward e => .backward e
  | .backward e => .forward e

def reverseWalk {i j} : LinkWalk E i j → LinkWalk E j i
  | .idle n => .idle n
  | .next s p => appendWalk (reverseWalk p) (.next (reverseStep s) (.idle _))

theorem appendTransport (u : Connection E X) {i j k} (p : LinkWalk E i j) (q : LinkWalk E j k)
    (x : X) : (walkTransport u (appendWalk p q)).f x =
    (walkTransport u q).f ((walkTransport u p).f x) := by
  induction p generalizing x with
  | idle => rfl
  | next s p ih => exact ih q _

theorem reverseTransport (u : Connection E X) {i j} (p : LinkWalk E i j) (x : X) :
    (walkTransport u (reverseWalk p)).f x = (walkTransport u p).inv x := by
  induction p generalizing x with
  | idle => rfl
  | next s p ih =>
    simp only [reverseWalk, appendTransport, ih]
    cases s <;> rfl

/-- A site action is compatible precisely when it intertwines every declared edge. -/
def FitsConnection (u v : Connection E X) (g : N → Frame X) : Prop :=
  ∀ {i j} (e : E i j) (x : X), (g j).f ((u.on e).f x) = (v.on e).f ((g i).f x)

theorem stepIntertwines (u v : Connection E X) (g : N → Frame X)
    (h : FitsConnection u v g) {i j} (s : LinkStep E i j) (x : X) :
    (g j).f ((stepTransport u s).f x) = (stepTransport v s).f ((g i).f x) := by
  cases s with
  | forward e => exact h e x
  | backward e =>
    have he := congrArg (v.on e).inv (h e ((u.on e).inv x))
    simpa [stepTransport, inverse, Frame.reverse, Frame.cancel] using he.symm

theorem walkIntertwines (u v : Connection E X) (g : N → Frame X)
    (h : FitsConnection u v g) {i j} (p : LinkWalk E i j) (x : X) :
    (g j).f ((walkTransport u p).f x) = (walkTransport v p).f ((g i).f x) := by
  induction p generalizing x with
  | idle => rfl
  | next s p ih =>
    simp only [walkTransport, thenFrame, Function.comp_apply, ih, stepIntertwines u v g h s]

/-- A loop for an oriented edge uses any two chosen access walks from the root.
    No enumeration of all closed walks or finiteness assumption is needed. -/
def edgeLoop {r : N} (access : ∀ n, LinkWalk E r n) {i j} (e : E i j) : LinkWalk E r r :=
  appendWalk (access i) (.next (.forward e) (reverseWalk (access j)))

theorem edgeLoopValue (u : Connection E X) {r : N} (access : ∀ n, LinkWalk E r n)
    {i j} (e : E i j) (x : X) : (walkTransport u (edgeLoop access e)).f x =
      (walkTransport u (access j)).inv ((u.on e).f ((walkTransport u (access i)).f x)) := by
  simp [edgeLoop, appendTransport, walkTransport, stepTransport, thenFrame, reverseTransport]

/-- The site frames are explicitly reconstructed from one base frame and the
    measured reference transports. Distinct loops must use the same base frame. -/
theorem edgeLoopsClassify (u v : Connection E X) {r : N} (access : ∀ n, LinkWalk E r n) :
    (∃ g, FitsConnection u v g) ↔ ∃ base : Frame X, ∀ {i j} (e : E i j) (x : X),
      base.f ((walkTransport u (edgeLoop access e)).f x) =
        (walkTransport v (edgeLoop access e)).f (base.f x) := by
  constructor
  · rintro ⟨g,h⟩
    exact ⟨g r, fun e x => walkIntertwines u v g h (edgeLoop access e) x⟩
  · rintro ⟨base,h⟩
    let g (i : N) := thenFrame (inverse (walkTransport u (access i)))
      (thenFrame base (walkTransport v (access i)))
    refine ⟨g, ?_⟩
    intro i j e x
    have he := congrArg (walkTransport v (access j)).f
      (h e ((walkTransport u (access i)).inv x))
    simpa only [edgeLoopValue, Frame.reverse, g, thenFrame, inverse,
      Function.comp_apply] using he

theorem allLoopsClassify (u v : Connection E X) {r : N} (access : ∀ n, LinkWalk E r n) :
    (∃ g, FitsConnection u v g) ↔ ∃ base : Frame X, ∀ (p : LinkWalk E r r) (x : X),
      base.f ((walkTransport u p).f x) = (walkTransport v p).f (base.f x) := by
  constructor
  · rintro ⟨g,h⟩
    exact ⟨g r, fun p x => walkIntertwines u v g h p x⟩
  · rintro ⟨base,h⟩
    exact (edgeLoopsClassify u v access).mpr ⟨base, fun e x => h (edgeLoop access e) x⟩

def trivialConnection (E : N → N → Type) (X : Type) : Connection E X :=
  ⟨fun _ => sameFrame X⟩

theorem trivialWalk {i j} (p : LinkWalk E i j) (x : X) :
    (walkTransport (trivialConnection E X) p).f x = x := by
  induction p generalizing x with
  | idle => rfl
  | next s p ih =>
    simp only [walkTransport, thenFrame, Function.comp_apply, ih]
    cases s <;> rfl

theorem flatIffTrivial (u : Connection E X) {r : N} (access : ∀ n, LinkWalk E r n) :
    (∃ g, FitsConnection u (trivialConnection E X) g) ↔
      ∀ {i j} (e : E i j) (x : X), (walkTransport u (edgeLoop access e)).f x = x := by
  rw [edgeLoopsClassify u (trivialConnection E X) access]
  constructor
  · rintro ⟨base,h⟩ i j e x
    have he := congrArg base.inv (h e x)
    simpa only [trivialWalk, Frame.cancel] using he
  · intro h
    exact ⟨sameFrame X, fun e x => by rw [h e x, trivialWalk]⟩

/-- A declared spatial aggregation maps each fine link to a coarse walk.
    A link hidden inside one cell may map to the idle walk there. Conversely a
    macro link can be expanded into a physically specified fine path by using
    this construction in the other direction. -/
structure WalkMap (E : N → N → Type) {M : Type} (F : M → M → Type) where
  site : N → M
  route : ∀ {i j}, E i j → LinkWalk F (site i) (site j)

variable {M : Type} {F : M → M → Type}

def mapStep (t : WalkMap E F) {i j} : LinkStep E i j → LinkWalk F (t.site i) (t.site j)
  | .forward e => t.route e
  | .backward e => reverseWalk (t.route e)

def mapWalk (t : WalkMap E F) {i j} : LinkWalk E i j → LinkWalk F (t.site i) (t.site j)
  | .idle i => .idle (t.site i)
  | .next s p => appendWalk (mapStep t s) (mapWalk t p)

def routeConnection (t : WalkMap E F) (v : Connection F X) : Connection E X :=
  ⟨fun e => walkTransport v (t.route e)⟩

theorem mapWalkTransport (t : WalkMap E F) (v : Connection F X) {i j} (p : LinkWalk E i j) (x : X) :
    (walkTransport v (mapWalk t p)).f x = (walkTransport (routeConnection t v) p).f x := by
  induction p generalizing x with
  | idle => rfl
  | next s p ih =>
    simp only [mapWalk, appendTransport, ih, walkTransport, thenFrame, Function.comp_apply]
    cases s with
    | forward => rfl
    | backward => simp only [mapStep, reverseTransport]; rfl

/-- Exact transport descent to a given coarse connection can be decided on its
    rooted edge loops. The network metric alone does not enter this criterion. -/
theorem scaleTransportCriterion (u : Connection E X) (v : Connection F X) (t : WalkMap E F)
    {r : N} (access : ∀ n, LinkWalk E r n) : (∃ g, FitsConnection u (routeConnection t v) g) ↔
      ∃ base : Frame X, ∀ {i j} (e : E i j) (x : X),
        base.f ((walkTransport u (edgeLoop access e)).f x) =
          (walkTransport v (mapWalk t (edgeLoop access e))).f (base.f x) := by
  simp only [mapWalkTransport, edgeLoopsClassify u (routeConnection t v) access]

theorem erasedLoopMustBeTrivial (u : Connection E X) (v : Connection F X) (t : WalkMap E F)
    {g : N → Frame X} (h : FitsConnection u (routeConnection t v) g) {i}
    (p : LinkWalk E i i) (erased : mapWalk t p = .idle (t.site i)) (x : X) :
    (walkTransport u p).f x = x := by
  have hp := walkIntertwines u (routeConnection t v) g h p x
  rw [← mapWalkTransport, erased] at hp
  have hi := congrArg (g i).inv hp
  simpa only [walkTransport, sameFrame, id_eq, Frame.cancel] using hi

/-- A two-generator control which cannot be detected by checking generator
    conjugacy classes individually. The first system has two identical swaps;
    the second system has swaps of distinct pairs. -/
inductive LoopColor where | a | b | c deriving DecidableEq
private def swapAB : LoopColor → LoopColor | .a => .b | .b => .a | .c => .c
private def swapBC : LoopColor → LoopColor | .a => .a | .b => .c | .c => .b
private def rotate : LoopColor → LoopColor | .a => .b | .b => .c | .c => .a
private def unrotate : LoopColor → LoopColor | .a => .c | .b => .a | .c => .b
private def changeSwap : Frame LoopColor :=
  ⟨rotate,unrotate,fun x => by cases x <;> rfl, fun x => by cases x <;> rfl⟩
private def abFrame : Frame LoopColor :=
  ⟨swapAB,swapAB,fun x => by cases x <;> rfl, fun x => by cases x <;> rfl⟩
private def bcFrame : Frame LoopColor :=
  ⟨swapBC,swapBC,fun x => by cases x <;> rfl, fun x => by cases x <;> rfl⟩

abbrev TwinLoop (_ _ : Unit) := Bool
def identicalSwaps : Connection TwinLoop LoopColor := ⟨fun _ => abFrame⟩
def distinctSwaps : Connection TwinLoop LoopColor := ⟨fun e => if e then bcFrame else abFrame⟩

theorem separateLoopFitsMislead :
    (∀ e : Bool, ∃ b : Frame LoopColor, ∀ x,
      b.f ((identicalSwaps.on (i := ()) (j := ()) e).f x) =
        (distinctSwaps.on (i := ()) (j := ()) e).f (b.f x)) ∧
    ¬ (∃ g, FitsConnection identicalSwaps distinctSwaps g) := by
  constructor
  · intro e
    cases e with
    | false => exact ⟨sameFrame _,fun _ => rfl⟩
    | true => exact ⟨changeSwap,fun x => by cases x <;> rfl⟩
  · rintro ⟨g,h⟩
    have ha := h (i := ()) (j := ()) false ((g ()).inv .a)
    have hb := h (i := ()) (j := ()) true ((g ()).inv .a)
    rw [Frame.reverse] at ha hb
    exact LoopColor.noConfusion (ha.symm.trans hb)

theorem mixedLoopDistinguishes :
    let p : LinkWalk TwinLoop () () := .next (j := ()) (.forward false) (.next (.forward true) (.idle ()))
    (∀ x, (walkTransport identicalSwaps p).f x = x) ∧
      (walkTransport distinctSwaps p).f .a = .c := by
  dsimp only
  exact ⟨fun x => by cases x <;> rfl,rfl⟩

/-- The quotient graph retains the identity of each crossing (including
    parallel ports); every within-cell edge is contracted. -/
inductive Crossing {C : Type} (cell : N → C) (E : N → N → Type) : C → C → Type where
  | port {i j} (e : E i j) (different : cell i ≠ cell j) : Crossing cell E (cell i) (cell j)

variable {C : Type}

def withinCells (cell : N → C) {i j} : LinkWalk E i j → Prop
  | .idle _ => True
  | .next (j := k) _ p => cell i = cell k ∧ withinCells cell p

def cellPullback [DecidableEq C] (cell : N → C) (v : Connection (Crossing cell E) X) :
    Connection E X where
  on := fun {i j} e => if eq : cell i = cell j then sameFrame X else v.on (.port e eq)

theorem cellInteriorIsIdle [DecidableEq C] (cell : N → C) (v : Connection (Crossing cell E) X)
    {i j} (p : LinkWalk E i j) (inside : withinCells cell p) (x : X) :
    (walkTransport (cellPullback cell v) p).f x = x := by
  induction p generalizing x with
  | idle => rfl
  | next s p ih =>
    obtain ⟨eq,hp⟩ := inside
    change (walkTransport _ p).f ((stepTransport _ s).f x) = x
    rw [ih hp]
    cases s with
    | forward => simp [stepTransport, cellPullback, eq, sameFrame]
    | backward => simp [stepTransport, cellPullback, eq.symm, inverse, sameFrame]

/-- A positive existence criterion for discarding internal edges. The test
    normalizes each measured internal link by two *internal* access paths from
    the representative of its cell. With ports retained the criterion is exact.
    The proof constructs the quotient transport on every crossing edge. -/
theorem cellQuotientExistsIff [DecidableEq C] (cell : N → C) (root : C → N)
    (access : ∀ n, LinkWalk E (root (cell n)) n) (internal : ∀ n, withinCells cell (access n))
    (u : Connection E X) :
    (∃ (v : Connection (Crossing cell E) X) (g : N → Frame X), FitsConnection u (cellPullback cell v) g) ↔
      ∀ {i j} (e : E i j), cell i = cell j → ∀ x,
        (walkTransport u (access j)).inv ((u.on e).f ((walkTransport u (access i)).f x)) = x := by
  constructor
  · rintro ⟨v,g,h⟩ i j e eq x
    have accessEq (k : N) (y : X) :
        (g k).f ((walkTransport u (access k)).f y) = (g (root (cell k))).f y := by
      rw [walkIntertwines u (cellPullback cell v) g h, cellInteriorIsIdle cell v _ (internal k)]
    have across := h e ((walkTransport u (access i)).f x)
    simp only [cellPullback, eq, dite_eq_left, sameFrame, id_eq, accessEq] at across
    have norm := accessEq j ((walkTransport u (access j)).inv ((u.on e).f ((walkTransport u (access i)).f x)))
    rw [Frame.reverse, across] at norm
    have undo := congrArg (g (root (cell j))).inv norm.symm
    simpa only [Frame.cancel] using undo
  · intro h
    let v : Connection (Crossing cell E) X := ⟨fun port => match port with
      | .port (i := i) (j := j) e _ => thenFrame (walkTransport u (access i))
          (thenFrame (u.on e) (inverse (walkTransport u (access j))))⟩
    let g (i : N) := inverse (walkTransport u (access i))
    refine ⟨v,g,?_⟩
    intro i j e x
    by_cases eq : cell i = cell j
    · have he := h e eq ((walkTransport u (access i)).inv x)
      simpa only [Frame.reverse, g, inverse, cellPullback, dite_eq_left eq, sameFrame, id_eq] using he
    · simp [g, inverse, cellPullback, eq, v, thenFrame, Frame.reverse]

end OperationalNetwork
