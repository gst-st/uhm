import Std
set_option autoImplicit false
namespace OperationalNetwork

/-- Changes of coordinates at a vertex; restricting these to unitary frames
    yields the Hilbert-space application. -/
structure Frame (V : Type) where
  f : V → V
  inv : V → V
  cancel : ∀ x, inv (f x) = x
  reverse : ∀ x, f (inv x) = x

def sameFrame (V : Type) : Frame V := ⟨id, id, fun _ => rfl, fun _ => rfl⟩
def thenFrame {V : Type} (a b : Frame V) : Frame V where
  f := b.f ∘ a.f
  inv := a.inv ∘ b.inv
  cancel x := by simp [Function.comp, b.cancel, a.cancel]
  reverse x := by simp [Function.comp, a.reverse, b.reverse]

def link {V : Type} (a b : Frame V) (u : V → V) := b.f ∘ u ∘ a.inv

theorem composeChanges {V : Type} (a b c d : Frame V) (u : V → V) :
    link c d (link a b u) = link (thenFrame a c) (thenFrame b d) u := rfl

theorem distinctEndpointsCommute {V : Type} (a b : Frame V) (u : V → V) :
    link a (sameFrame V) (link (sameFrame V) b u) =
    link (sameFrame V) b (link a (sameFrame V) u) := rfl

theorem pathCovariant {V : Type} (a b c : Frame V) (u v : V → V) :
    link b c v ∘ link a b u = link a c (v ∘ u) := by
  funext x
  simp [link, Function.comp, b.cancel]

/-- Transporters on a tree can all be gauged to identity, when the allowable
    frames include the inverses and composites of the transporters. -/
def inverse {V : Type} (a : Frame V) : Frame V := ⟨a.inv, a.f, a.reverse, a.cancel⟩
theorem pathTrivialization {V : Type} (u v : Frame V) :
    let b := inverse u
    let c := inverse (thenFrame u v)
    link (sameFrame V) b u.f = id ∧ link b c v.f = id := by
  dsimp [link, inverse, thenFrame, sameFrame]
  constructor <;> funext x <;> simp [Function.comp, u.cancel, v.cancel]

/-- An exact invariant encoding cannot turn a noncommuting pair into independent
    commuting actions; auxiliary states do not help under the stated intertwinings. -/
theorem commuteDescends {V W : Type} (encode : V → W) (faithful : ∀ x y, encode x = encode y → x = y)
    (u v : V → V) (U' V' : W → W) (hu : ∀ x, encode (u x) = U' (encode x))
    (hv : ∀ x, encode (v x) = V' (encode x))
    (hc : ∀ x, U' (V' x) = V' (U' x)) (x : V) : u (v x) = v (u x) := by
  apply faithful
  rw [hu, hv, hc, hv, hu]

inductive Mode where | zero | left | middle | right deriving DecidableEq
open Mode
def hop01 : Mode → Mode | left => middle | middle => left | _ => zero
def hop12 : Mode → Mode | middle => right | right => middle | _ => zero
theorem incompatibleHops : hop12 (hop01 left) ≠ hop01 (hop12 left) := by decide

/-- Independent path doublets on distinguishable link registers. At the shared
    vertex the two incident ports are distinct degrees of freedom. -/
theorem separatePorts {V W : Type} (u : V → V) (v : W → W) (x : V × W) :
    Prod.map u id (Prod.map id v x) = Prod.map id v (Prod.map u id x) := rfl

#print axioms pathCovariant
#print axioms pathTrivialization
#print axioms commuteDescends
#print axioms incompatibleHops
#print axioms separatePorts
end OperationalNetwork
