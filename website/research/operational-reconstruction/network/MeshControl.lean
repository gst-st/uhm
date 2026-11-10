import CommonGeometry
set_option autoImplicit false
namespace OperationalNetwork.Refinement

/-- A labelled net. Both access and return are measured; directed networks
    cannot replace the two inequalities by an untested symmetry convention. -/
structure ObservedNet {T} (l : Level T) (radius : Nat) where
  covers : ∀ x : l.Site, ∃ t, l.graph.first x (l.port t) ≤ radius ∧ l.graph.first (l.port t) x ≤ radius

def Nearby {T} (l : Level T) (r : Nat) (x : l.Site) (t : T) :=
  l.graph.first x (l.port t) ≤ r ∧ l.graph.first (l.port t) x ≤ r

def Correspond {T} (a b : Level T) (ra rb : Nat) (x : a.Site) (y : b.Site) :=
  ∃ t, Nearby a ra x t ∧ Nearby b rb y t

theorem fullCoverage {T} {a b : Level T} {ra rb} (ca : ObservedNet a ra) (cb : ObservedNet b rb) :
    (∀ x, ∃ y, Correspond a b ra rb x y) ∧ (∀ y, ∃ x, Correspond a b ra rb x y) := by
  have named (l : Level T) (r : Nat) (t : T) : Nearby l r (l.port t) t := by
    simp [Nearby,firstIdle]
  exact ⟨fun x => by obtain ⟨t,h⟩ := ca.covers x; exact ⟨b.port t,t,h,named b rb t⟩,
         fun y => by obtain ⟨t,h⟩ := cb.covers y; exact ⟨a.port t,t,named a ra t,h⟩⟩

private theorem endpointError {T} {l : Level T} {r x y i j} (hi : Nearby l r x i) (hj : Nearby l r y j) :
    l.graph.first x y ≤ ticks l i j + 2*r ∧ ticks l i j ≤ l.graph.first x y + 2*r := by
  obtain ⟨a,b⟩ := hi
  obtain ⟨c,d⟩ := hj
  have ac := firstRelay l.graph x (l.port i) y
  have bd := firstRelay l.graph (l.port i) (l.port j) y
  have df := firstRelay l.graph (l.port i) x (l.port j)
  have fg := firstRelay l.graph x y (l.port j)
  unfold ticks
  constructor <;> omega

/-- A distortion bound for every pair in an explicit covering correspondence,
    including stations which have no individual label. In calibrated common
    ticks one pays at most two radii at each end of the comparison. -/
theorem allSiteDistortion {T} {a b : Level T} {ra rb err x y u v}
    (ports : ∀ i j, ticks a i j ≤ ticks b i j + err ∧ ticks b i j ≤ ticks a i j + err)
    (xu : Correspond a b ra rb x u) (yv : Correspond a b ra rb y v) :
    a.graph.first x y ≤ b.graph.first u v + err + 2*(ra+rb) ∧
    b.graph.first u v ≤ a.graph.first x y + err + 2*(ra+rb) := by
  obtain ⟨i,c,d⟩ := xu
  obtain ⟨j,f,g⟩ := yv
  obtain ⟨h1,h2⟩ := endpointError c f
  obtain ⟨h3,h4⟩ := endpointError d g
  obtain ⟨h5,h6⟩ := ports i j
  constructor <;> omega

/-- An unobserved branch can never be matched at zero distortion by a network
    containing just a single station, no matter which relation is chosen. -/
theorem hiddenBranchLowerBound {X} (g : TimedNetwork X) (one : TimedNetwork Unit)
    (rel : X → Unit → Prop) (surj : ∀ x, ∃ y, rel x y) (err : Nat)
    (distort : ∀ x y u v, rel x u → rel y v → g.first x y ≤ one.first u v + err) (x y : X) :
    g.first x y ≤ err := by
  obtain ⟨⟨⟩,hx⟩ := surj x
  obtain ⟨⟨⟩,hy⟩ := surj y
  simpa [firstIdle] using distort _ _ _ _ hx hy

end OperationalNetwork.Refinement
