import Std
set_option autoImplicit false
namespace OperationalNetwork

/-- A directed physical passage with its measured cost. Multiple passages,
    loops and disconnected components are permitted. -/
abbrev Passage (X : Type) := X → X → Nat → Prop

inductive Itinerary {X : Type} (e : Passage X) : X → X → Nat → Nat → Prop
  | stay (x) : Itinerary e x x 0 0
  | step {x y z t c n} : e x y t → Itinerary e y z c n → Itinerary e x z (t+c) (n+1)

def CanReach {X : Type} (e : Passage X) (x y : X) (budget : Nat) : Prop :=
  ∃ c n, c ≤ budget ∧ Itinerary e x y c n

theorem joinTrips {X : Type} {e : Passage X} {x y z : X} {a b n m : Nat}
    (first : Itinerary e x y a n) (second : Itinerary e y z b m) :
    Itinerary e x z (a+b) (n+m) := by
  induction first with
  | stay => simpa using second
  | step edge _ ih =>
    simpa only [← Nat.succ_eq_add_one,Nat.succ_add,Nat.add_succ,Nat.add_zero,Nat.add_assoc] using Itinerary.step edge (ih second)

theorem reachViaRelay {X : Type} {e : Passage X} {x y z : X} {a b : Nat}
    (first : CanReach e x y a) (second : CanReach e y z b) : CanReach e x z (a+b) := by
  obtain ⟨_,_,ha,one⟩ := first
  obtain ⟨_,_,hb,two⟩ := second
  exact ⟨_,_,Nat.add_le_add ha hb,joinTrips one two⟩

theorem reachByStep {X : Type} {e : Passage X} {x y : X} {c : Nat}
    (h : e x y c) : CanReach e x y c :=
  ⟨_,_,Nat.le_refl _,by simpa using Itinerary.step h (.stay y)⟩

/-- Free merging erases which port in a block terminated the previous step. -/
def blockEdge {X B : Type} (block : X → B) (e : Passage X) : Passage B :=
  fun i j c => ∃ x y, block x=i ∧ block y=j ∧ e x y c

theorem projectTrip {X B : Type} (block : X → B) {e : Passage X} {x y : X} {c n : Nat}
    (h : Itinerary e x y c n) : Itinerary (blockEdge block e) (block x) (block y) c n := by
  induction h with
  | stay => exact .stay _
  | step edge _ ih => exact .step ⟨_,_,rfl,rfl,edge⟩ ih

/-- A test with quantifiers over every possible *arrival port*: one promised
    coarse step must be executable starting at that actual fine port. -/
def PortLift {X B : Type} (block : X → B) (e : Passage X) : Prop :=
  ∀ x j t, blockEdge block e (block x) j t → ∃ y, block y=j ∧ CanReach e x y t

theorem liftTrip {X B : Type} {block : X → B} {e : Passage X} (lift : PortLift block e)
    {i j : B} {c n : Nat} (trip : Itinerary (blockEdge block e) i j c n) :
    ∀ x, block x=i → ∃ y, block y=j ∧ CanReach e x y c := by
  induction trip with
  | stay =>
    intro x hx
    exact ⟨x,hx,0,0,Nat.le_refl _,.stay _⟩
  | step edge _ ih =>
    intro x hx
    obtain ⟨y,hy,first⟩ := lift x _ _ (hx ▸ edge)
    obtain ⟨z,hz,rest⟩ := ih y hy
    exact ⟨z,hz,reachViaRelay first rest⟩

/-- From each fine start the image of the reachable ball equals the coarse
    reachable ball at every budget exactly when the single-edge port tests pass. -/
theorem reachableBallsIffPortLift {X B : Type} (block : X → B) (e : Passage X) :
    (∀ x j b, CanReach (blockEdge block e) (block x) j b ↔
      ∃ y, block y=j ∧ CanReach e x y b) ↔ PortLift block e := by
  constructor
  · intro allBalls x j t edge
    exact (allBalls x j t).1 (reachByStep edge)
  · intro lift x j b
    constructor
    · rintro ⟨c,n,le,trip⟩
      obtain ⟨y,hy,k,m,hk,run⟩ := liftTrip lift trip x rfl
      exact ⟨y,hy,k,m,Nat.le_trans hk le,run⟩
    · rintro ⟨y,rfl,c,n,le,trip⟩
      exact ⟨c,n,le,projectTrip block trip⟩

/-- The error per internal transfer is not an error per itinerary. Starting
    at a specified port requires at most one intra-block transfer per leg. -/
theorem liftTripWithDiameter {X B : Type} {block : X → B} {e : Passage X} {diam : Nat}
    (within : ∀ x y, block x=block y → CanReach e x y diam)
    {i j : B} {c n : Nat} (trip : Itinerary (blockEdge block e) i j c n) :
    ∀ x, block x=i → ∃ y, block y=j ∧ CanReach e x y (c+n*diam) := by
  induction trip with
  | stay =>
    intro x hx
    exact ⟨x,hx,0,0,by simp,.stay _⟩
  | @step i j k t c n edge _ ih =>
    intro x hx
    obtain ⟨u,v,hu,hv,pass⟩ := edge
    obtain ⟨y,hy,tail⟩ := ih v hv
    have run := reachViaRelay (within x u (hx.trans hu.symm)) (reachViaRelay (reachByStep pass) tail)
    exact ⟨y,hy,by simpa only [Nat.succ_mul,Nat.add_assoc,Nat.add_comm,Nat.add_left_comm] using run⟩

/-- If the initial port may be selected, exactly the n−1 joins require a
    bound. Endpoint preparation at a fixed destination must be costed separately. -/
theorem freeEndsJoinBound {X B : Type} {block : X → B} {e : Passage X} {diam : Nat}
    (within : ∀ x y, block x=block y → CanReach e x y diam)
    {i j : B} {c n : Nat} (trip : Itinerary (blockEdge block e) i j c (n+1)) :
    ∃ x y, block x=i ∧ block y=j ∧ CanReach e x y (c+n*diam) := by
  cases trip with
  | step edge tail =>
    obtain ⟨u,v,hu,hv,pass⟩ := edge
    obtain ⟨y,hy,rest⟩ := liftTripWithDiameter within tail v hv
    exact ⟨u,y,hu,hy,by simpa only [Nat.add_assoc] using reachViaRelay (reachByStep pass) rest⟩

/-- Contract twice, or use the composite block map: the same concrete fine
    edge witnesses either result. Distances can still shrink in both. -/
theorem nestedBlockEdges {X B C : Type} (f : X → B) (g : B → C) (e : Passage X) :
    blockEdge g (blockEdge f e) = blockEdge (g ∘ f) e := by
  funext i j t
  apply propext
  constructor
  · rintro ⟨_,_,hi,hj,x,y,rfl,rfl,edge⟩
    exact ⟨x,y,hi,hj,edge⟩
  · rintro ⟨x,y,hi,hj,edge⟩
    exact ⟨_,_,hi,hj,x,y,rfl,rfl,edge⟩

theorem nestedPortLift {X B C : Type} (f : X → B) (g : B → C) (e : Passage X)
    (hf : PortLift f e) (hg : PortLift g (blockEdge f e)) : PortLift (g ∘ f) e := by
  intro x j t edge
  rw [← nestedBlockEdges] at edge
  obtain ⟨b,hb,trip⟩ := hg (f x) j t edge
  obtain ⟨y,hy,run⟩ := ((reachableBallsIffPortLift _ _).2 hf _ _ _).1 trip
  exact ⟨y,(congrArg g hy).trans hb,run⟩

/-- Two probes with identical reachable fine balls have identical coarse
    balls at observable starts if both satisfy the physical lifting check. -/
theorem commonBallsAcrossScale {X B : Type} (block : X → B) (e f : Passage X)
    (sameFine : ∀ x y b, CanReach e x y b ↔ CanReach f x y b)
    (he : PortLift block e) (hf : PortLift block f) (x : X) (j : B) (b : Nat) :
    CanReach (blockEdge block e) (block x) j b ↔ CanReach (blockEdge block f) (block x) j b := by
  rw [(reachableBallsIffPortLift _ _).2 he,(reachableBallsIffPortLift _ _).2 hf]
  exact exists_congr (fun y => and_congr_right (fun _ => sameFine x y b))

end OperationalNetwork
