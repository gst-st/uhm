import Response
set_option autoImplicit false
namespace OperationalNetwork
open Lean.Grind AddCommGroup AddCommMonoid

/-- Binary physical switches. A link may share a switch with other links
    or receive signs from several independently toggled switches. -/
inductive EdgeMask : Nat → Type where
  | nil : EdgeMask 0
  | cons {n : Nat} (bit : Bool) (tail : EdgeMask n) : EdgeMask (n+1)
deriving DecidableEq

def clearMask : (n : Nat) → EdgeMask n
  | 0 => .nil
  | n+1 => .cons false (clearMask n)

def toggleMask : {n : Nat} → EdgeMask n → EdgeMask n → EdgeMask n
  | _, .nil, .nil => .nil
  | _, .cons a x, .cons b y => .cons (a ^^ b) (toggleMask x y)

def parityAt : {n : Nat} → EdgeMask n → EdgeMask n → Bool
  | _, .nil, .nil => false
  | _, .cons a u, .cons b v => (a && b) ^^ parityAt u v

private theorem clearParity {n : Nat} (u : EdgeMask n) : parityAt u (clearMask n) = false := by
  induction u with
  | nil => rfl
  | cons b u ih => simp [clearMask, parityAt, ih]

private theorem xorParity {n : Nat} (u x y : EdgeMask n) :
    parityAt u (toggleMask x y) = (parityAt u x ^^ parityAt u y) := by
  induction u with
  | nil => cases x; cases y; rfl
  | cons a u ih =>
    cases x with | cons b x =>
     cases y with | cons c y =>
      simp only [toggleMask, parityAt, ih]
      cases a <;> cases b <;> cases c <;> cases parityAt u x <;> cases parityAt u y <;> rfl

def polarity {V : Type} [Neg V] (flip : Bool) (a : V) := if flip then -a else a

private theorem pairPolarity {V : Type} [AddCommGroup V] (u v : Bool) (a : V) :
    polarity u (polarity v a) = polarity (u ^^ v) a := by
  cases u <;> cases v <;> simp [polarity, neg_neg]

def walkSignature {E : Type} {n : Nat} (control : E → EdgeMask n) : List E → EdgeMask n
  | [] => clearMask n
  | e :: rest => toggleMask (control e) (walkSignature control rest)

/-- Each encountered edge acts on the signal; the signature is computed
    from those encounters, so a second traversal toggles the same sign again. -/
def switchedWalk {E V : Type} [Neg V] {n : Nat} (control : E → EdgeMask n) (u : EdgeMask n)
    (a : V) : List E → V
  | [] => a
  | e :: rest => polarity (parityAt u (control e)) (switchedWalk control u a rest)

theorem walkPhase {E V : Type} [AddCommGroup V] {n : Nat} (control : E → EdgeMask n) (u : EdgeMask n)
    (a : V) (walk : List E) :
    switchedWalk control u a walk = polarity (parityAt u (walkSignature control walk)) a := by
  induction walk with
  | nil => simp [switchedWalk, walkSignature, clearParity, polarity]
  | cons e rest ih => rw [switchedWalk, walkSignature, ih, xorParity, pairPolarity]

def walshRead {V : Type} [Add V] [Neg V] : {n : Nat} → (EdgeMask n → V) → EdgeMask n → V
  | _, f, .nil => f .nil
  | _, f, .cons b u => walshRead (fun s => f (.cons false s)) u +
      polarity b (walshRead (fun s => f (.cons true s)) u)

private theorem walshZero {V : Type} [AddCommGroup V] {n : Nat} (u : EdgeMask n) : walshRead (fun _ => (0 : V)) u = 0 := by
  induction u with
  | nil => rfl
  | cons b u ih => cases b <;> simp [walshRead, ih, polarity, add_zero, neg_zero]

private theorem walshAdd {V : Type} [AddCommGroup V] {n : Nat} (u : EdgeMask n) (f g : EdgeMask n → V) :
    walshRead (fun s => f s + g s) u = walshRead f u + walshRead g u := by
  induction u with
  | nil => rfl
  | cons b u ih =>
    simp only [walshRead, ih]
    cases b <;> simp only [polarity, Bool.false_eq_true, ↓reduceIte, neg_add] <;>
      simp only [add_assoc, add_left_comm]

private theorem walshPoint {V : Type} [AddCommGroup V] {n : Nat} (u s : EdgeMask n) (a : V) :
    walshRead (fun t => if t=s then a else 0) u = polarity (parityAt u s) a := by
  induction u with
  | nil => cases s; rfl
  | cons b u ih =>
    cases s with | cons c s =>
     cases c <;> cases b <;>
       simp [walshRead, parityAt, walshZero, ih, polarity, add_zero, zero_add, neg_zero] <;>
       split <;> simp_all [neg_neg]

/-- The signed amplitude of each route is added only after its physical switches
    have acted. Amplitudes may include the entire ordered transfer along the
    walk, projected onto this readout channel. -/
def switchedResponse {E V : Type} [AddCommGroup V] {n : Nat} (control : E → EdgeMask n) (u : EdgeMask n) :
    List (List E × V) → V
  | [] => 0
  | (walk,a) :: rest => switchedWalk control u a walk + switchedResponse control u rest

def bucketAmplitude {E V : Type} [AddCommGroup V] {n : Nat} (control : E → EdgeMask n) :
    List (List E × V) → EdgeMask n → V
  | [], _ => 0
  | (walk,a) :: rest, s => (if s=walkSignature control walk then a else 0) +
      bucketAmplitude control rest s

theorem switchedResponseWalsh {E V : Type} [AddCommGroup V] {n : Nat} (control : E → EdgeMask n)
    (u : EdgeMask n) (routes : List (List E × V)) :
    switchedResponse control u routes = walshRead (bucketAmplitude control routes) u := by
  induction routes with
  | nil => exact (walshZero u).symm
  | cons wa rest ih =>
    rcases wa with ⟨walk,a⟩
    change switchedWalk control u a walk + switchedResponse control u rest =
      walshRead (fun s => (if s=walkSignature control walk then a else 0) +
        bucketAmplitude control rest s) u
    rw [walkPhase, ih, walshAdd, walshPoint]

private theorem walshKernel {V : Type} [AddCommGroup V] (twice : ∀ a : V, a+a=0 → a=0)
    {n : Nat} (f : EdgeMask n → V) :
    (∀ u, walshRead f u = 0) ↔ ∀ s, f s = 0 := by
  constructor
  · induction n with
    | zero => intro h s; cases s; exact h .nil
    | succ n ih =>
      intro h s
      have both (u : EdgeMask n) :
          walshRead (fun t => f (.cons false t)) u = 0 ∧
          walshRead (fun t => f (.cons true t)) u = 0 := by
        have p := h (.cons false u)
        have q := h (.cons true u)
        simp only [walshRead, polarity, Bool.false_eq_true, ↓reduceIte] at p q
        rw [← sub_eq_add_neg, sub_eq_zero_iff] at q
        exact ⟨q.trans (twice _ (q ▸ p)), twice _ (q ▸ p)⟩
      cases s with | cons b s =>
       cases b
       · exact ih _ (fun u => (both u).1) s
       · exact ih _ (fun u => (both u).2) s
  · intro h u; rw [show f = fun _ => 0 from funext h]; exact walshZero u

/-- Complete visibility criterion for arbitrary finite walk families. Nothing
    is assumed about disjoint paths, node degrees, acyclicity, or independent
    control of all links. All binary switch settings must be implementable. -/
theorem routeControlKernel {E V : Type} [AddCommGroup V] (twice : ∀ a : V, a+a=0 → a=0)
    {n : Nat} (control : E → EdgeMask n)
    (routes : List (List E × V)) :
    (∀ u, switchedResponse control u routes = 0) ↔
      ∀ s, bucketAmplitude control routes s = 0 := by
  simpa only [switchedResponseWalsh] using walshKernel twice (bucketAmplitude control routes)

/-- Try implementable settings until a nonquiet registration is found.
    The upper bound on the number of settings is exponential in the number of
    independent switches; early termination does not compromise completeness. -/
def findSwitch : {n : Nat} → (EdgeMask n → Bool) → Option (EdgeMask n)
  | 0, register => if register .nil then some .nil else none
  | n+1, register =>
    match findSwitch (n:=n) (fun u => register (.cons false u)) with
    | some u => some (.cons false u)
    | none => (findSwitch (n:=n) (fun u => register (.cons true u))).map (.cons true)

private theorem missingSwitch {n : Nat} (register : EdgeMask n → Bool) :
    findSwitch register = none ↔ ∀ u, register u = false := by
  induction n with
  | zero =>
    constructor
    · intro missing u
      cases u
      cases h : register .nil
      · rfl
      · simp only [findSwitch, h, ↓reduceIte, reduceCtorEq] at missing
    · intro quiet; simp only [findSwitch, quiet .nil, Bool.false_eq_true, ↓reduceIte]
  | succ n ih =>
    simp only [findSwitch]
    split
    · rename_i u found
      constructor
      · intro h; cases h
      · intro allQuiet
        have e := (ih _).2 (fun m => allQuiet (.cons false m))
        simp [found] at e
    · rename_i missing
      have quietFalse := (ih _).1 missing
      simp only [Option.map_eq_none_iff, ih]
      constructor
      · intro quietTrue u
        cases u with | cons b m => cases b
                                   · exact quietFalse m
                                   · exact quietTrue m
      · exact fun allQuiet m => allQuiet (.cons true m)

private theorem foundSwitch {n : Nat} (register : EdgeMask n → Bool) (u : EdgeMask n)
    (found : findSwitch register = some u) : register u = true := by
  induction n with
  | zero => cases u; cases h : register .nil <;> simp [findSwitch, h] at *
  | succ n ih =>
    simp only [findSwitch] at found
    split at found
    · rename_i m h
      cases found
      exact ih _ m h
    · rename_i h
      obtain ⟨m, hm, rfl⟩ := Option.map_eq_some_iff.mp found
      exact ih _ m hm

/-- With decidable zero a nonzero signature bucket gives an actual setting
    returned by the finite search and a certificate of its measured response. -/
theorem visibleSwitchWitness {E V : Type} [AddCommGroup V] [DecidableEq V]
    (twice : ∀ a : V, a+a=0 → a=0) {n : Nat} (control : E → EdgeMask n)
    (routes : List (List E × V)) (s : EdgeMask n) (bright : bucketAmplitude control routes s ≠ 0) :
    let register := fun u => decide (switchedResponse control u routes ≠ 0)
    ∃ u, findSwitch register = some u ∧ switchedResponse control u routes ≠ 0 := by
  dsimp only
  let register := fun u => decide (switchedResponse control u routes ≠ 0)
  cases h : findSwitch register with
  | none =>
    have dark := (missingSwitch register).mp h
    have quiet (u : EdgeMask n) : switchedResponse control u routes = 0 := by
      simpa [register] using dark u
    exact False.elim (bright ((routeControlKernel twice control routes).mp quiet s))
  | some u => exact ⟨u,rfl,of_decide_eq_true (foundSwitch register u h)⟩

/-- Here a record contains the responses in every switch setting. Paths and
    their unperturbed amplitudes must be reproducible across repeated trials. -/
theorem routeFirstArrival {E V : Type} [AddCommGroup V] (twice : ∀ a : V, a+a=0 → a=0)
    {n : Nat} (control : E → EdgeMask n)
    (routes : Nat → List (List E × V)) (t : Nat) :
    FirstAt (fun _ => 0) (fun k u => switchedResponse control u (routes k)) t ↔
    (¬ ∀ s, bucketAmplitude control (routes t) s = 0) ∧
      ∀ k, k < t → ∀ s, bucketAmplitude control (routes k) s = 0 := by
  have quiet (k : Nat) : (fun u => switchedResponse control u (routes k)) = (fun _ => 0) ↔
      ∀ s, bucketAmplitude control (routes k) s = 0 :=
    ⟨fun h => (routeControlKernel twice control _).mp (fun u => congrFun h u),
     fun h => funext ((routeControlKernel twice control _).mpr h)⟩
  simp only [FirstAt, ne_eq, quiet]

private theorem clearControlParity {n : Nat} (s : EdgeMask n) :
    parityAt (clearMask n) s = false := by
  induction s with
  | nil => rfl
  | cons b s ih => simp [clearMask, parityAt, ih]

/-- Regroup a selected fine class by the buckets actually read by the coarse
    controls. The mask predicate only has to classify the walks in this record. -/
private theorem regroupBuckets {E V : Type} [AddCommGroup V] {n m : Nat}
    (fine : E → EdgeMask n) (coarse : E → EdgeMask m) (s : EdgeMask n)
    (selects : EdgeMask m → Bool) (routes : List (List E × V))
    (classifies : ∀ w a, (w,a) ∈ routes →
      (selects (walkSignature coarse w) = true ↔ s = walkSignature fine w)) :
    bucketAmplitude fine routes s =
      walshRead (fun t => if selects t then bucketAmplitude coarse routes t else 0) (clearMask m) := by
  induction routes with
  | nil =>
    simp [bucketAmplitude, walshZero]
  | cons wa rest ih =>
    rcases wa with ⟨w,a⟩
    have splitBucket : (fun t => if selects t then bucketAmplitude coarse ((w,a)::rest) t else 0)
        = (fun t => (if t=walkSignature coarse w then (if selects (walkSignature coarse w) then a else 0) else 0) +
            (if selects t then bucketAmplitude coarse rest t else 0)) := by
      funext t
      by_cases h : t=walkSignature coarse w
      · subst t; cases selects (walkSignature coarse w) <;> simp [bucketAmplitude, add_zero]
      · cases selects t <;> simp [bucketAmplitude, h, zero_add, add_zero]
    rw [splitBucket, walshAdd, walshPoint, clearControlParity]
    have hs := classifies w a List.mem_cons_self
    have tailClassifies w' a' (h : (w',a') ∈ rest) := classifies w' a' (List.mem_cons_of_mem _ h)
    simp only [bucketAmplitude, polarity, Bool.false_eq_true, ↓reduceIte, ih tailClassifies]
    simp only [hs]

/-- Uniform visibility survives a change of controls on a catalogue exactly
    when the new settings still distinguish every previously distinct route
    signature. This is the one-sided preservation law; taking both directions
    characterizes identical observable partitions. -/
theorem controlResolution {E V : Type} [AddCommGroup V]
    (twice : ∀ a : V, a+a=0 → a=0) (witness : V) (nonzero : witness ≠ 0)
    {n m : Nat} (fine : E → EdgeMask n) (coarse : E → EdgeMask m) (allowed : List E → Prop) :
    (∀ routes : List (List E × V), (∀ w a, (w,a) ∈ routes → allowed w) →
      (∀ u, switchedResponse coarse u routes = 0) →
       ∀ u, switchedResponse fine u routes = 0) ↔
    ∀ p q, allowed p → allowed q → walkSignature coarse p = walkSignature coarse q →
      walkSignature fine p = walkSignature fine q := by
  constructor
  · intro keep p q hp hq merged
    by_cases same : walkSignature fine p = walkSignature fine q
    · exact same
    · let pair := [(p,witness), (q,-witness)]
      have admitted : ∀ w a, (w,a) ∈ pair → allowed w := by
        intro w a h; simp only [pair, List.mem_cons, List.not_mem_nil, or_false] at h
        rcases h with h|h <;> cases h <;> assumption
      have lost : ∀ u, switchedResponse coarse u pair = 0 := by
        apply (routeControlKernel twice coarse pair).mpr
        intro s
        by_cases h : s = walkSignature coarse q <;>
          simp [pair, bucketAmplitude, merged, h, add_neg_cancel, add_zero]
      have h := (routeControlKernel twice fine pair).mp (keep pair admitted lost) (walkSignature fine p)
      simp [pair, bucketAmplitude, same, add_zero] at h
      exact False.elim (nonzero h)
  · intro refines routes admitted dark
    have coarseSilent := (routeControlKernel twice coarse routes).mp dark
    apply (routeControlKernel twice fine routes).mpr
    intro s
    let selects (t : EdgeMask m) := routes.any fun r =>
      decide (s = walkSignature fine r.1 ∧ t = walkSignature coarse r.1)
    have classifies (w : List E) (a : V) (member : (w,a) ∈ routes) :
        selects (walkSignature coarse w) = true ↔ s = walkSignature fine w := by
      simp only [selects, List.any_eq_true, decide_eq_true_eq]
      constructor
      · rintro ⟨⟨v,b⟩, hv, matchFine, matchCoarse⟩
        exact matchFine.trans (refines w v (admitted _ _ member) (admitted _ _ hv) matchCoarse).symm
      · intro matchFine; exact ⟨(w,a),member,matchFine,rfl⟩
    rw [regroupBuckets fine coarse s selects routes classifies]
    simp only [coarseSilent, ite_self, walshZero]

/-- Reproducible recordings across scales have the same first visible tick
    if the observable partitions agree on the actual walks at every tick.
    The partitions can differ on walks which do not arrive together. -/
theorem firstTickAcrossScales {E V : Type} [AddCommGroup V]
    (twice : ∀ a : V, a+a=0 → a=0) (witness : V) (nonzero : witness ≠ 0)
    {n m : Nat} (fine : E → EdgeMask n) (coarse : E → EdgeMask m)
    (routes : Nat → List (List E × V))
    (catalog : Nat → List E → Prop)
    (admitted : ∀ k w a, (w,a) ∈ routes k → catalog k w)
    (partition : ∀ k p q, catalog k p → catalog k q →
      (walkSignature fine p = walkSignature fine q ↔ walkSignature coarse p = walkSignature coarse q))
    (t : Nat) :
    FirstAt (fun _ => 0) (fun k u => switchedResponse fine u (routes k)) t ↔
      FirstAt (fun _ => 0) (fun k u => switchedResponse coarse u (routes k)) t := by
  have quiet (k : Nat) : (fun u => switchedResponse fine u (routes k)) = (fun _ => 0) ↔
      (fun u => switchedResponse coarse u (routes k)) = (fun _ => 0) := by
    constructor
    · intro h
      apply funext
      apply (controlResolution twice witness nonzero coarse fine (catalog k)).mpr
        (fun p q hp hq => (partition k p q hp hq).mp) (routes k) (admitted k)
      exact fun u => congrFun h u
    · intro h
      apply funext
      apply (controlResolution twice witness nonzero fine coarse (catalog k)).mpr
        (fun p q hp hq => (partition k p q hp hq).mpr) (routes k) (admitted k)
      exact fun u => congrFun h u
  simp only [FirstAt, ne_eq, quiet]

/-- A port marked e transmits the accumulated field linearly. Different
    ports may implement operators which do not commute. -/
structure RouteLink (V : Type) [AddCommGroup V] where
  send : V → V
  onZero : send 0 = 0
  onAdd : ∀ a b, send (a+b) = send a + send b
  onNeg : ∀ a, send (-a) = -(send a)

private theorem linkPolarity {V : Type} [AddCommGroup V] (L : RouteLink V) (b : Bool) (a : V) :
    L.send (polarity b a) = polarity b (L.send a) := by
  cases b <;> simp [polarity, L.onNeg]

private theorem sendSwitched {E V : Type} [AddCommGroup V] {m : Nat} (L : RouteLink V)
    (control : E → EdgeMask m) (u : EdgeMask m) (walk : List E) (a : V) :
    switchedWalk control u (L.send a) walk = L.send (switchedWalk control u a walk) := by
  rw [walkPhase, walkPhase, linkPolarity]

private theorem responseAppend {E V : Type} [AddCommGroup V] {m : Nat} (control : E → EdgeMask m)
    (u : EdgeMask m) (p q : List (List E × V)) :
    switchedResponse control u (p++q) = switchedResponse control u p + switchedResponse control u q := by
  induction p with
  | nil => simp [switchedResponse, zero_add]
  | cons wa p ih =>
    rcases wa with ⟨w,a⟩
    simp [switchedResponse, ih, add_assoc]

def throughPort {E V : Type} [AddCommGroup V] (e : E) (L : RouteLink V)
    (routes : List (List E × V)) := routes.map fun (walk,a) => (e :: walk, L.send a)

private theorem responseThrough {E V : Type} [AddCommGroup V] {m : Nat} (control : E → EdgeMask m)
    (u : EdgeMask m) (e : E) (L : RouteLink V) (routes : List (List E × V)) :
    switchedResponse control u (throughPort e L routes) =
      polarity (parityAt u (control e)) (L.send (switchedResponse control u routes)) := by
  induction routes with
  | nil =>
    simp [switchedResponse, throughPort, L.onZero, polarity, neg_zero]
  | cons wa rest ih =>
    rcases wa with ⟨w,a⟩
    change switchedWalk control u (L.send a) (e::w) +
      switchedResponse control u (throughPort e L rest) =
        polarity (parityAt u (control e)) (L.send (switchedWalk control u a w + switchedResponse control u rest))
    rw [switchedWalk, sendSwitched, ih, L.onAdd]
    cases parityAt u (control e) <;> simp [polarity, neg_add]

/-- Station set X may be infinite; only incoming port families must be finite.
    A summand is (predecessor, edge); parallel edges, feedback and loops are
    allowed. A visit crosses one port per tick. -/
def graphSignal {X E V : Type} [DecidableEq X] [AddCommGroup V] {m : Nat}
    (incoming : X → List (X × E)) (links : E → RouteLink V)
    (control : E → EdgeMask m) (u : EdgeMask m) (source : X) (pulse : V) : Nat → X → V
  | 0, x => if x=source then pulse else 0
  | k+1, x => (incoming x).foldr (fun (y,e) a =>
      polarity (parityAt u (control e))
        ((links e).send (graphSignal incoming links control u source pulse k y)) + a) 0

/-- Edge lists store most recent port first. The walk amplitude is generated
    in physical order by the same link maps as the update above. -/
def graphWalks {X E V : Type} [DecidableEq X] [AddCommGroup V]
    (incoming : X → List (X × E)) (links : E → RouteLink V) (source : X) (pulse : V) :
    Nat → X → List (List E × V)
  | 0, x => if x=source then [([],pulse)] else []
  | k+1, x => (incoming x).flatMap fun (y,e) =>
      throughPort e (links e) (graphWalks incoming links source pulse k y)

theorem networkPathExpansion {X E V : Type} [DecidableEq X] [AddCommGroup V] {m : Nat}
    (incoming : X → List (X × E)) (links : E → RouteLink V)
    (control : E → EdgeMask m) (u : EdgeMask m) (source : X) (pulse : V) (k : Nat) (x : X) :
    graphSignal incoming links control u source pulse k x =
      switchedResponse control u (graphWalks incoming links source pulse k x) := by
  induction k generalizing x with
  | zero =>
    by_cases h : x=source <;> simp [graphSignal, graphWalks, h, switchedResponse, switchedWalk, add_zero]
  | succ k ih =>
    simp only [graphSignal, graphWalks]
    generalize incoming x = ports
    induction ports with
    | nil => rfl
    | cons port tail ht =>
      rcases port with ⟨y,e⟩
      simp only [List.foldr_cons, List.flatMap_cons, responseAppend, responseThrough]
      rw [ht, ih y]

theorem networkArrivalCriterion {X E V : Type} [DecidableEq X] [AddCommGroup V]
    (twice : ∀ a : V, a+a=0 → a=0) {m : Nat}
    (incoming : X → List (X × E)) (links : E → RouteLink V)
    (control : E → EdgeMask m) (source detector : X) (pulse : V) (t : Nat) :
    let routes := fun k => graphWalks incoming links source pulse k detector
    FirstAt (fun _ => 0) (fun k u => graphSignal incoming links control u source pulse k detector) t ↔
      (¬ ∀ s, bucketAmplitude control (routes t) s = 0) ∧
      ∀ k, k < t → ∀ s, bucketAmplitude control (routes k) s = 0 := by
  dsimp only
  simp only [networkPathExpansion]
  exact routeFirstArrival twice control _ t

/-- Two distinct parallel edges, traversed once with opposite amplitudes.
    Sharing a switch hides both transfers; controlling just one reveals them. -/
theorem mergedSwitchHidesPulse :
    let routes : List (List Bool × Int) := [([false],1),([true],-1)]
    let off : EdgeMask 1 := .cons false .nil
    let onS : EdgeMask 1 := .cons true .nil
    (∀ u : EdgeMask 1, switchedResponse (fun _ => onS) u routes = 0) ∧
       switchedResponse (fun e => if e then onS else off) onS routes = 2 := by
  dsimp only
  constructor
  · intro u; cases u with | cons b r => cases r; cases b <;> decide
  · decide

/-- Two outward ports (one reverses polarity) and one return port close a
    feedback loop. Both outward paths have the same one-tick travel time. -/
private def echoPorts (x : Bool) : List (Bool × Option Bool) :=
  if x then [(false,some false),(false,some true)] else [(true,none)]

private def echoLink (e : Option Bool) : RouteLink Int where
  send := if e = some true then fun a => -a else id
  onZero := by split <;> decide
  onAdd a b := by split <;> dsimp <;> omega
  onNeg a := by split <;> rfl

private def echoControl (split : Bool) (e : Option Bool) : EdgeMask 1 :=
  .cons (if split then decide (e = some true) else true) .nil

/-- A counterexample on the local graph update itself. Merging phase controls
    makes the receiver permanently dark even though both ports transmit. -/
theorem cyclicSwitchObstruction :
    (∀ k u, graphSignal echoPorts echoLink (echoControl false) u false 1 k true = 0) ∧
    FirstAt 0 (fun k => graphSignal echoPorts echoLink (echoControl true) (.cons true .nil) false 1 k true) 1 := by
  constructor
  · intro k u
    cases k with
    | zero => rfl
    | succ k =>
      cases u with | cons b u =>
        cases u
        cases b <;> simp [graphSignal, echoPorts, echoControl, echoLink, parityAt, polarity] <;> omega
  · constructor
    · decide
    · intro k h
      have hk : k=0 := by omega
      subst k; rfl

end OperationalNetwork
