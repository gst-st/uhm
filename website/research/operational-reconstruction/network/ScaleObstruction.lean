import PortQuotient
set_option autoImplicit false
namespace OperationalNetwork

/-- A reciprocal strip of two-port cells. Physical links span at most three
    ticks and cost at least their displacement. Consecutive triples contain cycles. -/
def portPosition (x : Nat × Bool) := 2*x.1 + if x.2 then 1 else 0
def stripPassage (x y : Nat × Bool) (t : Nat) : Prop :=
  t ≤ 3 ∧ portPosition x ≤ portPosition y + t ∧ portPosition y ≤ portPosition x + t

private theorem stripWithin (x y : Nat × Bool) (h : x.1 = y.1) : CanReach stripPassage x y 1 := by
  apply reachByStep
  obtain ⟨a,u⟩ := x
  obtain ⟨b,v⟩ := y
  change a=b at h
  subst b
  cases u <;> cases v <;> simp [stripPassage,portPosition] <;> omega

theorem stripTripCannotOutrun {x y : Nat × Bool} {c n : Nat}
    (trip : Itinerary stripPassage x y c n) : portPosition y ≤ portPosition x + c := by
  induction trip with
  | stay => omega
  | step edge _ ih => have h := edge.2.2; omega

private theorem stripCoarseTrip (a n : Nat) :
    Itinerary (blockEdge Prod.fst stripPassage) a (a+n) n n := by
  induction n generalizing a with
  | zero => exact .stay a
  | succ n ih =>
    have edge : blockEdge Prod.fst stripPassage a (a+1) 1 := by
      refine ⟨(a,true),(a+1,false),rfl,rfl,?_⟩
      simp [stripPassage,portPosition,Nat.mul_add] <;> omega
    simpa [Nat.add_comm,Nat.add_left_comm,Nat.add_assoc] using Itinerary.step edge (ih (a+1))

private theorem stripCoarseLower {a b c n : Nat}
    (trip : Itinerary (blockEdge Prod.fst stripPassage) a b c n) : b ≤ a+c := by
  induction trip with
  | stay => omega
  | step edge _ ih =>
    obtain ⟨⟨i,u⟩,⟨j,v⟩,rfl,rfl,h⟩ := edge
    have inc := h.2.2
    cases u <;> cases v <;> simp [portPosition] at inc <;> dsimp at * <;> omega

/-- For any n, the first and last block are n+1 coarse ticks apart, while
    *every* selection of fine endpoints costs at least 2n+1. This realizes
    the upper bound with one unit of interior diameter for every join. -/
theorem sharpJoinLoss (n : Nat) :
    (∀ b, CanReach (blockEdge Prod.fst stripPassage) 0 (n+1) b ↔ n+1 ≤ b) ∧
    (∀ b, (∃ x y : Nat × Bool, x.1=0 ∧ y.1=n+1 ∧ CanReach stripPassage x y b) ↔ 2*n+1 ≤ b) := by
  have coarse := stripCoarseTrip 0 (n+1)
  simp only [Nat.zero_add] at coarse
  constructor
  · intro b
    constructor
    · rintro ⟨c,m,le,trip⟩
      have h := stripCoarseLower trip
      omega
    · intro h; exact ⟨_,_,h,coarse⟩
  · intro b
    constructor
    · rintro ⟨⟨i,u⟩,⟨j,v⟩,rfl,rfl,c,m,le,trip⟩
      have h := stripTripCannotOutrun trip
      cases u <;> cases v <;> simp [portPosition,Nat.mul_add] at h <;> omega
    · intro h
      obtain ⟨x,y,hx,hy,c,m,le,trip⟩ := freeEndsJoinBound stripWithin coarse
      exact ⟨x,y,hx,hy,c,m,by omega,trip⟩

end OperationalNetwork
