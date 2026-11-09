import Transport
set_option autoImplicit false
namespace OperationalNetwork

inductive Particle (V : Type) where | atA : V → Particle V | atB : V → Particle V | atC : V → Particle V
structure FieldState (V : Type) where
  ab : Frame V
  bc : Frame V
  particle : Particle V

def actAtSites {V : Type} (a b c : Frame V) (s : FieldState V) : FieldState V where
  ab := thenFrame (thenFrame (inverse a) s.ab) b
  bc := thenFrame (thenFrame (inverse b) s.bc) c
  particle := match s.particle with
    | .atA x => .atA (a.f x)
    | .atB x => .atB (b.f x)
    | .atC x => .atC (c.f x)

theorem siteIdentity {V : Type} (s : FieldState V) :
    actAtSites (sameFrame V) (sameFrame V) (sameFrame V) s = s := by
  rcases s with ⟨u,v,p⟩
  cases p <;> rfl

theorem siteActionLaw {V : Type} (a b c a' b' c' : Frame V) (s : FieldState V) :
    actAtSites a' b' c' (actAtSites a b c s) =
      actAtSites (thenFrame a a') (thenFrame b b') (thenFrame c c') s := by
  rcases s with ⟨u,v,p⟩
  cases p <;> rfl

theorem neighbouringSiteActionsCommute {V : Type} (a b : Frame V) (s : FieldState V) :
    actAtSites a (sameFrame V) (sameFrame V) (actAtSites (sameFrame V) b (sameFrame V) s) =
      actAtSites (sameFrame V) b (sameFrame V) (actAtSites a (sameFrame V) (sameFrame V) s) := by
  rw [siteActionLaw,siteActionLaw]
  rfl

def moveAB {V : Type} (s : FieldState V) : FieldState V :=
  { s with particle := match s.particle with
      | .atA x => .atB (s.ab.f x)
      | .atB x => .atA (s.ab.inv x)
      | .atC x => .atC x }

def moveBC {V : Type} (s : FieldState V) : FieldState V :=
  { s with particle := match s.particle with
      | .atA x => .atA x
      | .atB x => .atC (s.bc.f x)
      | .atC x => .atB (s.bc.inv x) }

theorem movesRespectGauge {V : Type} (a b c : Frame V) (s : FieldState V) :
    moveAB (actAtSites a b c s) = actAtSites a b c (moveAB s) ∧
    moveBC (actAtSites a b c s) = actAtSites a b c (moveBC s) := by
  rcases s with ⟨u,v,m⟩
  cases m <;> simp [moveAB,moveBC,actAtSites,thenFrame,inverse,Function.comp,Frame.cancel]

theorem movesInvolutive {V : Type} (s : FieldState V) :
    moveAB (moveAB s) = s ∧ moveBC (moveBC s) = s := by
  rcases s with ⟨u,v,m⟩
  cases m <;> simp [moveAB,moveBC,Frame.cancel,Frame.reverse]

theorem pathOrderMatters {V : Type} (u v : Frame V) (x : V) :
    moveBC (moveAB ⟨u,v,.atA x⟩) ≠ moveAB (moveBC ⟨u,v,.atA x⟩) := by
  intro e
  have h := congrArg FieldState.particle e
  change Particle.atC _ = Particle.atB _ at h
  cases h

#print axioms movesRespectGauge
#print axioms movesInvolutive
#print axioms pathOrderMatters
end OperationalNetwork
