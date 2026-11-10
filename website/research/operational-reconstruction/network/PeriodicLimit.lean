import SignalNetwork
set_option autoImplicit false

namespace OperationalNetwork.Periodic

/-- Two arcs on a circle of circumference C. The coordinates used below are
    the cumulative physical tick counts of successive links. -/
def gap (x y : Nat) := x-y + (y-x)
def arc (C x y : Nat) := min (gap x y) (C-gap x y)

theorem arcSym (C x y : Nat) : arc C x y = arc C y x := by
  simp only [arc,gap,Nat.add_comm]

theorem arcSeparates (C x y : Nat) (hx : x<C) (hy : y<C) :
    arc C x y=0 ↔ x=y := by
  constructor
  · intro eq
    unfold arc gap at eq
    omega
  · rintro rfl
    simp [arc,gap]

theorem arcTriangle (C a b c : Nat) (ha : a<C) (hb : b<C) (hc : c<C) :
    arc C a c ≤ arc C a b + arc C b c := by
  unfold arc gap
  omega

/-- Primitive undirected steps only to the successor/predecessor and through
    the closing seam. Their costs are the supplied arc lengths, not all-pairs
    distances. The n=1 case can have two different parallel passages. -/
def ringStep {n : Nat} (C : Nat) (pos : Fin (n+1) → Nat) : Passage (Fin (n+1)) :=
  fun x y t =>
    ((x.val+1=y.val ∨ y.val+1=x.val) ∧ t=gap (pos x) (pos y)) ∨
    (((x.val=0 ∧ y.val=n) ∨ (y.val=0 ∧ x.val=n)) ∧ t=C-gap (pos x) (pos y))

private theorem stepReversed {n C : Nat} {pos : Fin (n+1) → Nat} {x y t}
    (h : ringStep C pos x y t) : ringStep C pos y x t := by
  have g : gap (pos y) (pos x)=gap (pos x) (pos y) := Nat.add_comm _ _
  rcases h with ⟨p,v⟩|⟨p,v⟩
  · exact Or.inl ⟨p.symm,g ▸ v⟩
  · exact Or.inr ⟨p.symm,g ▸ v⟩

private theorem reverseReach {n C : Nat} {pos : Fin (n+1) → Nat} {x y b}
    (h : CanReach (ringStep C pos) x y b) : CanReach (ringStep C pos) y x b := by
  obtain ⟨t,m,le,trip⟩ := h
  suffices back : CanReach (ringStep C pos) y x t by
    obtain ⟨v,j,ht,r⟩ := back
    exact ⟨v,j,Nat.le_trans ht le,r⟩
  clear le
  induction trip with
  | stay => exact ⟨0,0,Nat.le_refl _,.stay _⟩
  | step e _ ih => simpa only [Nat.add_comm] using reachViaRelay ih (reachByStep (stepReversed e))

private theorem forwardReach {n C : Nat} {pos : Fin (n+1) → Nat}
    (mono : ∀ x y : Fin (n+1), x.val ≤ y.val → pos x ≤ pos y)
    (x y : Fin (n+1)) (le : x.val ≤ y.val) :
    CanReach (ringStep C pos) x y (pos y - pos x) := by
  obtain ⟨j,hj⟩ := y
  induction j with
  | zero =>
    have eq : x=⟨0,hj⟩ := Fin.ext (Nat.eq_zero_of_le_zero le)
    subst x
    exact ⟨0,0,by simp,.stay _⟩
  | succ j ih =>
    by_cases atEnd : x.val=j+1
    · obtain rfl : x=⟨j+1,hj⟩ := Fin.ext atEnd
      exact ⟨0,0,by simp,.stay _⟩
    · have low : x.val ≤ j := by change x.val≤j+1 at le; omega
      let mid : Fin (n+1) := ⟨j,by omega⟩
      let last : Fin (n+1) := ⟨j+1,hj⟩
      have prev := ih mid.isLt low
      have mx := mono x mid low
      have ml := mono mid last (Nat.le_succ j)
      have edge : ringStep C pos mid last (pos last-pos mid) :=
        Or.inl ⟨Or.inl rfl,by unfold gap; omega⟩
      have trip := reachViaRelay prev (reachByStep edge)
      change CanReach _ x mid (pos mid-pos x) at prev
      change CanReach _ x last (pos last-pos x)
      change CanReach _ x last ((pos mid-pos x)+(pos last-pos mid)) at trip
      rwa [show (pos mid-pos x)+(pos last-pos mid)=pos last-pos x by omega] at trip

private theorem ringLower {n C : Nat} {pos : Fin (n+1) → Nat}
    (inside : ∀ i, pos i < C) {x y t m} (trip : Itinerary (ringStep C pos) x y t m) :
    arc C (pos x) (pos y) ≤ t := by
  induction trip with
  | stay => simp [arc,gap]
  | @step x y z a b m edge tail ih =>
    have direct : arc C (pos x) (pos y) ≤ a := by
      rcases edge with ⟨_,rfl⟩|⟨_,rfl⟩
      · exact Nat.min_le_left _ _
      · exact Nat.min_le_right _ _
    exact Nat.le_trans (arcTriangle C _ _ _ (inside x) (inside y) (inside z))
      (Nat.add_le_add direct ih)

private theorem sortedReach {n C : Nat} {pos : Fin (n+1) → Nat}
    (mono : ∀ x y : Fin (n+1), x.val ≤ y.val → pos x ≤ pos y)
    (inside : ∀ i, pos i < C) (x y : Fin (n+1)) (le : x.val ≤ y.val) :
    CanReach (ringStep C pos) x y (arc C (pos x) (pos y)) := by
  let lo : Fin (n+1) := 0
  let hi : Fin (n+1) := Fin.last n
  have ordered := mono x y le
  have low := mono lo x (Nat.zero_le _)
  have high := mono y hi (Nat.le_of_lt_succ y.isLt)
  have bound := inside hi
  have major : CanReach (ringStep C pos) x y (C-(pos y-pos x)) := by
    have left := reverseReach (C:=C) (forwardReach mono lo x (Nat.zero_le _))
    have right := reverseReach (C:=C) (forwardReach mono y hi (Nat.le_of_lt_succ y.isLt))
    have seam : ringStep C pos lo hi (C-gap (pos lo) (pos hi)) :=
      Or.inr ⟨Or.inl ⟨rfl,rfl⟩,rfl⟩
    have run := reachViaRelay left (reachViaRelay (reachByStep seam) right)
    have price : (pos x - pos lo) + (C-gap (pos lo) (pos hi) + (pos hi-pos y)) = C-(pos y-pos x) := by
      unfold gap; omega
    rwa [price] at run
  have easy := forwardReach (C:=C) mono x y le
  have g : gap (pos x) (pos y)=pos y-pos x := by unfold gap; omega
  unfold arc
  rw [g]
  by_cases h : pos y-pos x ≤ C-(pos y-pos x)
  · simpa [Nat.min_eq_left h] using easy
  · simpa [Nat.min_eq_right (Nat.le_of_lt (Nat.lt_of_not_ge h))] using major

/-- The least arrival cost follows from the two physical arc traversals and a
    lower bound for every walk, including paths that wind or change direction. -/
theorem ringArrivesIff {n C : Nat} {pos : Fin (n+1) → Nat}
    (mono : ∀ x y : Fin (n+1), x.val ≤ y.val → pos x ≤ pos y)
    (inside : ∀ i, pos i < C) (x y : Fin (n+1)) (b : Nat) :
    CanReach (ringStep C pos) x y b ↔ arc C (pos x) (pos y) ≤ b := by
  constructor
  · rintro ⟨t,m,le,trip⟩; exact Nat.le_trans (ringLower inside trip) le
  · intro budget
    have best : CanReach (ringStep C pos) x y (arc C (pos x) (pos y)) := by
      rcases Nat.le_total x.val y.val with le|le
      · exact sortedReach mono inside x y le
      · rw [arcSym]
        exact reverseReach (sortedReach mono inside y x le)
    obtain ⟨t,m,le,trip⟩ := best
    exact ⟨t,m,Nat.le_trans le budget,trip⟩

/-- Physical unit relays. Each receiver reads only its cyclic neighbours. -/
def unitLinks (n : Nat) (y : Fin (n+1)) : List (Fin (n+1)) :=
  (List.finRange (n+1)).filter fun x =>
    x.val+1=y.val ∨ y.val+1=x.val ∨ (x.val=0 ∧ y.val=n) ∨ (y.val=0 ∧ x.val=n)

theorem unitRingPassages (n : Nat) :
    SignalNetwork.unitPassages (unitLinks n) = ringStep (n+1) Fin.val := by
  funext x y t
  apply propext
  have hx := x.isLt
  have hy := y.isLt
  simp only [SignalNetwork.unitPassages,unitLinks,List.mem_filter,List.mem_finRange,
    true_and,decide_eq_true_eq,ringStep,gap]
  constructor
  · rintro ⟨h,rfl⟩
    rcases h with f|r|f|r
    · exact Or.inl ⟨Or.inl f,by omega⟩
    · exact Or.inl ⟨Or.inr r,by omega⟩
    · exact Or.inr ⟨Or.inl f,by omega⟩
    · exact Or.inr ⟨Or.inr r,by omega⟩
  · rintro (⟨p,rfl⟩|⟨p,rfl⟩)
    · rcases p with h|h
      · exact ⟨Or.inl h,by omega⟩
      · exact ⟨Or.inr (Or.inl h),by omega⟩
    · exact ⟨Or.inr (Or.inr p),by rcases p with h|h <;> omega⟩

/-- A first arrival in the working Boolean unit-delay detector, including
    correct behavior when the calibrated observation window is too short. -/
theorem unitRingFirst {n : Nat} (x y : Fin (n+1)) (b : Nat) :
    SignalNetwork.firstTick? (unitLinks n) x y b =
      if arc (n+1) x.val y.val ≤ b then some (arc (n+1) x.val y.val) else none := by
  have reach (t : Nat) : CanReach (SignalNetwork.unitPassages (unitLinks n)) x y t ↔
      arc (n+1) x.val y.val ≤ t := by
    rw [unitRingPassages]
    exact ringArrivesIff (fun _ _ h => h) (fun i => i.isLt) x y t
  split
  · rename_i hb
    apply (SignalNetwork.firstTickSpec _ _ _ _ _).2
    obtain ⟨c,m,le,trip⟩ := (reach _).2 (Nat.le_refl _)
    have low := (reach c).1 ⟨_,m,Nat.le_refl _,trip⟩
    obtain rfl := Nat.le_antisymm le low
    exact ⟨hb,⟨_,trip⟩,fun c n w => (reach c).1 ⟨c,n,Nat.le_refl _,w⟩⟩
  · rename_i beyond
    cases h : SignalNetwork.firstTick? (unitLinks n) x y b with
    | none => rfl
    | some v =>
      have obs : (SignalNetwork.firstTick? (unitLinks n) x y b).isSome = true := by rw [h]; rfl
      exact False.elim (beyond ((reach b).1 ((SignalNetwork.detectionIffReach _ _ _ _).1 obs)))

theorem arcDilation (k C x y : Nat) : arc (k*C) (k*x) (k*y) = k * arc C x y := by
  have g : gap (k*x) (k*y) = k*gap x y := by simp only [gap,Nat.mul_add,Nat.mul_sub]
  simp only [arc, g, ← Nat.mul_sub]
  rcases Nat.le_total (gap x y) (C-gap x y) with h|h
  · rw [Nat.min_eq_left h,Nat.min_eq_left (Nat.mul_le_mul_left k h)]
  · rw [Nat.min_eq_right h,Nat.min_eq_right (Nat.mul_le_mul_left k h)]

/-- The circular distance moves by at most the sum of the coordinate
    errors. All four coordinates lie in a single unwrapped fundamental interval. -/
theorem arcPortError {C a b a' b' e f : Nat}
    (ha : a<C) (hb : b<C) (ha' : a'<C) (hb' : b'<C)
    (ea : gap a a' ≤ e) (eb : gap b b' ≤ f) :
    arc C a b ≤ arc C a' b' + e+f ∧ arc C a' b' ≤ arc C a b + e+f := by
  have step (x y : Nat) : arc C x y ≤ gap x y := Nat.min_le_left _ _
  have lift (x y z w : Nat) (hx : x<C) (hy : y<C) (hz : z<C) (hw : w<C) :
      arc C x y ≤ arc C z w + gap x z + gap y w := by
    have first := arcTriangle C x z y hx hz hy
    have rest := arcTriangle C z w y hz hw hy
    have left := step x z
    have right := step y w
    rw [arcSym C w y] at rest
    omega
  have u := lift a b a' b' ha hb ha' hb'
  have v := lift a' b' a b ha' hb' ha hb
  have x : gap a' a = gap a a' := Nat.add_comm _ _
  have y : gap b' b = gap b b' := Nat.add_comm _ _
  rw [x,y] at v
  constructor <;> omega

/-- The physical boundary and interior reader in cell i are reached after
    w*i and w*i+s(i) unit transmissions. Their local delays s(i), w-s(i)
    may vary independently for each probe and each cell. -/
def portClock (w : Nat) (offset : Nat → Nat) (j : Nat) :=
  w*(j/2) + if j%2=0 then 0 else offset (j/2)

theorem portClockBounds {w : Nat} {s : Nat → Nat} (_hw : 0<w) (hs : ∀ i, s i < w) (j : Nat) :
    w*(j/2) ≤ portClock w s j ∧ portClock w s j < w*(j/2+1) := by
  have := hs (j/2)
  simp only [portClock,Nat.mul_succ]
  split <;> constructor <;> omega

private theorem clockOrdered {w : Nat} {s : Nat → Nat} (hw : 0<w) (hs : ∀ i, s i < w)
    (x y : Nat) (xy : x≤y) : portClock w s x ≤ portClock w s y := by
  by_cases q : x/2=y/2
  · unfold portClock
    rw [q]
    split <;> split <;> first | omega | (rename_i h; omega)
  · have next : x/2+1 ≤ y/2 := by omega
    have upper := (portClockBounds hw hs x).2
    have lower := (portClockBounds hw hs y).1
    exact Nat.le_trans (Nat.le_of_lt upper) (Nat.le_trans (Nat.mul_le_mul_left w next) lower)

private theorem clockInside {n w : Nat} {s : Nat → Nat} (hw : 0<w) (hs : ∀ i, s i < w)
    (j : Fin (2*n+1+1)) : portClock w s j.val < w*(n+1) := by
  have h := j.isLt
  have mid : j.val/2+1 ≤ n+1 := by omega
  exact Nat.lt_of_lt_of_le (portClockBounds hw hs _).2 (Nat.mul_le_mul_left w mid)

theorem periodicDelivery {n w : Nat} {s : Nat → Nat} (hw : 0<w) (hs : ∀ i, s i < w)
    (x y : Fin (2*n+1+1)) (b : Nat) :
    CanReach (ringStep (w*(n+1)) (fun j => portClock w s j.val)) x y b ↔
      arc (w*(n+1)) (portClock w s x.val) (portClock w s y.val) ≤ b :=
  ringArrivesIff (fun i j => clockOrdered hw hs i.val j.val) (clockInside hw hs) x y b

/-- The weighted ring's budget test agrees with a physical Boolean first
    detector on the corresponding fully expanded unit relay ring. -/
theorem periodicMeasured {n w : Nat} {s : Nat → Nat} (hw : 0<w) (hs : ∀ i, s i < w)
    (x y : Fin (2*n+1+1)) (b : Nat) :
    let C := w*(n+1)
    let ix (z : Fin (2*n+1+1)) : Fin (C-1+1) :=
      ⟨portClock w s z.val,by have hc := clockInside hw hs z; dsimp [C]; omega⟩
    SignalNetwork.firstTick? (unitLinks (C-1)) (ix x) (ix y) b =
      if arc C (portClock w s x.val) (portClock w s y.val) ≤ b then
        some (arc C (portClock w s x.val) (portClock w s y.val)) else none := by
  dsimp only
  rw [unitRingFirst]
  have pos := clockInside hw hs x
  have eq : w*(n+1)-1+1=w*(n+1) := by omega
  simp only [eq]

/-- Sample a circular address a/q using either reader in its containing
    cell. The floor is taken in cell units, independently of a probe's delays. -/
def samplePort (n : Nat) {q : Nat} (a : Fin (q+1)) (interior : Bool) : Fin (2*n+1+1) :=
  let N := n+1
  let j := N*a.val/(q+1)
  ⟨2*j + if interior then 1 else 0,by
    have bound : j < N := (Nat.div_lt_iff_lt_mul (Nat.succ_pos _)).2 (by
      dsimp only [N]; exact Nat.mul_lt_mul_of_pos_left a.isLt (Nat.succ_pos _))
    dsimp only [N] at bound
    split <;> omega⟩

private theorem sampledCoordinate {n q w : Nat} {s : Nat → Nat} (hw : 0<w) (hs : ∀ i, s i < w)
    (a : Fin (q+1)) (side : Bool) :
    gap ((q+1)*portClock w s (samplePort n a side).val) ((w*(n+1))*a.val) ≤ (q+1)*w := by
  let j := (n+1)*a.val/(q+1)
  have ix : (samplePort n a side).val/2 = j := by
    dsimp only [samplePort,j]; split <;> omega
  have bounds := portClockBounds hw hs (samplePort n a side).val
  rw [ix] at bounds
  obtain ⟨lo,hi⟩ := bounds
  have qlo : j*(q+1) ≤ (n+1)*a.val := Nat.div_mul_le_self _ _
  have qhi : (n+1)*a.val < (j+1)*(q+1) :=
    (Nat.div_lt_iff_lt_mul (Nat.succ_pos _)).1 (Nat.lt_succ_self j)
  have wlo := Nat.mul_le_mul_left w qlo
  have whi := Nat.mul_lt_mul_of_pos_left qhi hw
  have plo := Nat.mul_le_mul_left (q+1) lo
  have phi := Nat.mul_lt_mul_of_pos_left hi (Nat.succ_pos q)
  have rearr (u : Nat) : w*(u*(q+1)) = (q+1)*(w*u) := by ac_rfl
  rw [rearr] at wlo whi
  have top : (q+1)*(w*(j+1))=(q+1)*(w*j)+(q+1)*w := by
    rw [Nat.mul_succ,Nat.mul_add]
  rw [top] at whi phi
  rw [Nat.mul_assoc]
  apply (show ∀ (a b lo hi : Nat), lo≤a → lo≤b → a<lo+hi → b<lo+hi → gap a b≤hi by
    intro a b lo hi; unfold gap; omega) _ _ _ _ plo wlo phi whi

/-- Inputs a/q,b/q on the rational circle have reference distance
    arc q a b / q. With N cells and w ticks per cell the discrepancy between
    the measured first time divided by w*N and that distance is ≤ 2/N.
    The bound is uniform over port addresses, endpoint choice and probe. -/
theorem periodicUniformEstimate {n q w : Nat} {s : Nat → Nat} (hw : 0<w) (hs : ∀ i, s i < w)
    (a b : Fin (q+1)) (left right : Bool) :
    let N := n+1
    let Q := q+1
    let T := arc (w*N) (portClock w s (samplePort n a left).val)
                       (portClock w s (samplePort n b right).val)
    let d := arc Q a.val b.val
    Q*T ≤ (w*N)*d + 2*(Q*w) ∧ (w*N)*d ≤ Q*T + 2*(Q*w) := by
  dsimp only
  have wN := Nat.mul_pos hw (Nat.succ_pos n)
  let T := w*(n+1)
  have compare := arcPortError (C := (q+1)*T)
    (Nat.mul_lt_mul_of_pos_left (clockInside hw hs (samplePort n a left)) (Nat.succ_pos q))
    (Nat.mul_lt_mul_of_pos_left (clockInside hw hs (samplePort n b right)) (Nat.succ_pos q))
    (show T*a.val<(q+1)*T by rw [Nat.mul_comm (q+1) T]; exact Nat.mul_lt_mul_of_pos_left a.isLt wN)
    (show T*b.val<(q+1)*T by rw [Nat.mul_comm (q+1) T]; exact Nat.mul_lt_mul_of_pos_left b.isLt wN)
    (sampledCoordinate hw hs a left) (sampledCoordinate hw hs b right)
  rw [arcDilation, Nat.mul_comm (q+1) T, arcDilation] at compare
  exact ⟨by dsimp [T] at compare; omega,by dsimp [T] at compare; omega⟩

/-- Distinct rational addresses remain quantitatively separated at *all*
    sufficiently fine scales. This lower bound holds uniformly over the
    reader selected, the ticks per cell and all internal budgets. -/
theorem periodicSeparation {n q w : Nat} {s : Nat → Nat} (hw : 0<w) (hs : ∀ i, s i < w)
    (a b : Fin (q+1)) (different : a ≠ b) (left right : Bool) (fine : 4*(q+1) ≤ n+1) :
    let T := arc (w*(n+1)) (portClock w s (samplePort n a left).val)
                            (portClock w s (samplePort n b right).val)
    (w*(n+1))*arc (q+1) a.val b.val ≤ 2*((q+1)*T) := by
  have dpos : 0<arc (q+1) a.val b.val := by
    have ne : a.val≠b.val := fun e => different (Fin.ext e)
    exact Nat.pos_of_ne_zero (fun zero => ne ((arcSeparates _ _ _ a.isLt b.isLt).mp zero))
  obtain ⟨_,low⟩ := periodicUniformEstimate (n:=n) hw hs a b left right
  have lower : 4*((q+1)*w) ≤ (w*(n+1))*arc (q+1) a.val b.val := by
    calc
      4*((q+1)*w) = w*(4*(q+1)) := by ac_rfl
      _ ≤ w*(n+1) := Nat.mul_le_mul_left w fine
      _ ≤ (w*(n+1))*arc (q+1) a.val b.val := by
        simpa only [Nat.mul_one] using Nat.mul_le_mul_left (w*(n+1)) dpos
  dsimp only
  omega

/-- Rational labels survive choice of common denominator. The quantitative
    triangle and separation theorems for the limiting metric are arcTriangle
    and arcSeparates in the common denominator. -/
theorem rationalSubdivision (k q a b : Nat) :
    arc (k*q) (k*a) (k*b) = k*arc q a b := arcDilation k q a b

/-- On two probes with the same full-turn duration, quarter-arc readings
    may disagree even after any single clock calibration. Both measured
    configurations use 8N physical unit relays and the same four named ports.
    The quarter-link budgets are (2N,2N,2N,2N) and (N,N,3N,3N). -/
theorem equalTurnDoesNotFixArcs (n : Nat) :
    let N := n+1
    let C := 8*n+7+1
    let read (x y : Fin C) := SignalNetwork.firstTick? (unitLinks (8*n+7)) x y C
    read 0 ⟨2*N,by dsimp [C,N]; omega⟩ = some (2*N) ∧
    read ⟨4*N,by dsimp [C,N]; omega⟩ ⟨6*N,by dsimp [C,N]; omega⟩ = some (2*N) ∧
    read 0 ⟨N,by dsimp [C,N]; omega⟩ = some N ∧
    read ⟨2*N,by dsimp [C,N]; omega⟩ ⟨5*N,by dsimp [C,N]; omega⟩ = some (3*N) ∧
    ¬ ∃ p q : Nat, 0<p ∧ 0<q ∧ p*(2*N)=q*N ∧ p*(2*N)=q*(3*N) := by
  dsimp only
  simp only [unitRingFirst, Fin.val_zero,arc,gap]
  refine ⟨?_,?_,?_,?_,?_⟩
  case refine_1 | refine_2 | refine_3 | refine_4 =>
    apply (show ∀ (v b t : Nat), v≤b → v=t → (if v ≤ b then some v else none) = some t by
      intro v b t h e; rw [ite_eq_left h,e])
    all_goals omega
  rintro ⟨p,q,_,hq,h1,h2⟩
  have eq := Nat.eq_of_mul_eq_mul_left hq (h1.symm.trans h2)
  omega

end OperationalNetwork.Periodic
