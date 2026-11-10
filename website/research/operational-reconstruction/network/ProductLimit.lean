import CircleLimit
set_option autoImplicit false
namespace OperationalNetwork.ProductGeometry
open OperationalNetwork.Continuum

/-- A primitive step acts in exactly one coordinate (idling in that
    coordinate is allowed if supplied by its own passage relation). -/
def serialEdges {X Y : Type} (e : Passage X) (f : Passage Y) : Passage (X × Y) :=
  fun x y t => (e x.1 y.1 t ∧ x.2=y.2) ∨ (x.1=y.1 ∧ f x.2 y.2 t)

private theorem splitSerialTrip {X Y : Type} {e : Passage X} {f : Passage Y}
    {x y : X × Y} {c n} (h : Itinerary (serialEdges e f) x y c n) :
    ∃ a b j k, a+b=c ∧ Itinerary e x.1 y.1 a j ∧ Itinerary f x.2 y.2 b k := by
  induction h with
  | stay => exact ⟨0,0,0,0,rfl,.stay _,.stay _⟩
  | @step x y z t c n edge _ ih =>
    obtain ⟨a,b,i,j,rfl,one,two⟩ := ih
    rcases edge with ⟨h,hy⟩|⟨hx,h⟩
    · exact ⟨t+a,b,i+1,j,by omega,.step h one,hy ▸ two⟩
    · exact ⟨a,t+b,i,j+1,by omega,hx ▸ one,.step h two⟩

private theorem joinSerialTrips {X Y : Type} {e : Passage X} {f : Passage Y}
    {x y : X} {u v : Y} {a b i j} (h : Itinerary e x y a i) (k : Itinerary f u v b j) :
    Itinerary (serialEdges e f) (x,u) (y,v) (a+b) (i+j) := by
  have left : Itinerary (serialEdges e f) (x,u) (y,u) a i := by
    induction h with
    | stay => exact .stay _
    | @step _ mid _ _ _ _ edge _ ih => exact .step (y:=(mid,u)) (Or.inl ⟨edge,rfl⟩) ih
  have right : Itinerary (serialEdges e f) (y,u) (y,v) b j := by
    clear left
    induction k with
    | stay => exact .stay _
    | @step _ mid _ _ _ _ edge _ ih => exact .step (y:=(y,mid)) (Or.inr ⟨rfl,edge⟩) ih
  exact joinTrips left right

theorem serialReach {X Y : Type} (e : Passage X) (f : Passage Y) (s d : X × Y) (b : Nat) :
    CanReach (serialEdges e f) s d b ↔ ∃ i j, i+j ≤ b ∧ CanReach e s.1 d.1 i ∧ CanReach f s.2 d.2 j := by
  constructor
  · rintro ⟨c,n,le,h⟩
    obtain ⟨a,b,i,j,rfl,one,two⟩ := splitSerialTrip h
    exact ⟨a,b,le,⟨a,i,Nat.le_refl _,one⟩,⟨b,j,Nat.le_refl _,two⟩⟩
  · rintro ⟨a,b,le,⟨i,n,hi,one⟩,⟨j,m,hj,two⟩⟩
    exact ⟨i+j,n+m,by omega,joinSerialTrips one two⟩

def serialLinks {X Y : Type} (l : X → List X) (r : Y → List Y) (v : X × Y) :=
  ((l v.1).map (fun x => (x,v.2))) ++ ((r v.2).map (fun y => (v.1,y)))

theorem physicalSerialEdges {X Y : Type} (l : X → List X) (r : Y → List Y) :
    SignalNetwork.unitPassages (serialLinks l r) =
      serialEdges (SignalNetwork.unitPassages l) (SignalNetwork.unitPassages r) := by
  funext x y t
  apply propext
  rcases x with ⟨x,u⟩; rcases y with ⟨y,v⟩
  simp only [SignalNetwork.unitPassages,serialLinks,serialEdges,List.mem_append,List.mem_map,Prod.mk.injEq]
  constructor
  · rintro ⟨h,rfl⟩
    rcases h with ⟨z,h,rfl,rfl⟩|⟨z,h,rfl,rfl⟩
    · exact Or.inl ⟨⟨h,rfl⟩,rfl⟩
    · exact Or.inr ⟨rfl,h,rfl⟩
  · rintro (⟨⟨h,rfl⟩,rfl⟩|⟨rfl,h,rfl⟩)
    · exact ⟨Or.inl ⟨_,h,rfl,rfl⟩,rfl⟩
    · exact ⟨Or.inr ⟨_,h,rfl,rfl⟩,rfl⟩

/-- The working product detector reads the sum of independently measured
    first ticks. A too-short joint horizon returns none. The splitting
    theorem above also excludes joint delivery if either target is unreachable. -/
theorem serialFirstTick {X Y : Type} [DecidableEq X] [DecidableEq Y] (l : X → List X)
    (r : Y → List Y) (s d : X × Y) {i j h₁ h₂ : Nat}
    (hl : SignalNetwork.firstTick? l s.1 d.1 h₁ = some i)
    (hr : SignalNetwork.firstTick? r s.2 d.2 h₂ = some j) (budget : Nat) :
    SignalNetwork.firstTick? (serialLinks l r) s d budget =
      if i+j≤budget then some (i+j) else none := by
  obtain ⟨_,⟨n,one⟩,min₁⟩ := (SignalNetwork.firstTickSpec _ _ _ _ _).1 hl
  obtain ⟨_,⟨m,two⟩,min₂⟩ := (SignalNetwork.firstTickSpec _ _ _ _ _).1 hr
  have lower {c k} (trip : Itinerary (SignalNetwork.unitPassages (serialLinks l r)) s d c k) :
      i+j ≤ c := by
    rw [physicalSerialEdges] at trip
    obtain ⟨_,_,_,_,rfl,a,b⟩ := splitSerialTrip trip
    exact Nat.add_le_add (min₁ _ _ a) (min₂ _ _ b)
  split
  · rename_i fits
    apply (SignalNetwork.firstTickSpec _ _ _ _ _).2
    refine ⟨fits,⟨n+m,?_⟩,fun _ _ trip => lower trip⟩
    rw [physicalSerialEdges]
    exact joinSerialTrips one two
  · rename_i short
    cases obs : SignalNetwork.firstTick? (serialLinks l r) s d budget with
    | none => rfl
    | some t =>
      obtain ⟨bound,⟨_,trip⟩,_⟩ := (SignalNetwork.firstTickSpec _ _ _ _ _).1 obs
      exact False.elim (short (Nat.le_trans (lower trip) bound))

private theorem regroup (a b c d : Value) :
    add (add a b) (add c d) = add (add a c) (add b d) := by
  induction a,b using Quotient.inductionOn₂ with
  | _ a b =>
    induction c,d using Quotient.inductionOn₂ with
    | _ c d =>
      apply Quotient.sound
      constructor
      · apply dominatesPointwise
        intro n
        change a.value n+b.value n+(c.value n+d.value n) ≤ a.value n+c.value n+(b.value n+d.value n)
        omega
      · apply dominatesPointwise
        intro n
        change a.value n+c.value n+(b.value n+d.value n) ≤ a.value n+b.value n+(c.value n+d.value n)
        omega

private theorem addMonoPair {a b c d : Value} (ac : valueLE a c) (bd : valueLE b d) :
    valueLE (add a b) (add c d) := by
  induction a,c using Quotient.inductionOn₂ with
  | _ a c =>
    induction b,d using Quotient.inductionOn₂ with
    | _ b d => exact dominatesSum ac bd

private theorem coordinateBounds (a b : Value) : valueLE a (add a b) ∧ valueLE b (add a b) := by
  induction a,b using Quotient.inductionOn₂ with
  | _ a b =>
    exact ⟨dominatesPointwise (fun _ => Nat.le_add_right _ _),dominatesPointwise (fun _ => Nat.le_add_left _ _)⟩

def serialLimit {X Y : Type} (l : LimitMetric X) (r : LimitMetric Y) : LimitMetric (X × Y) where
  dist a b := add (l.dist a.1 b.1) (r.dist a.2 b.2)
  nonnegative a b := valueTransitive _ _ _ (l.nonnegative a.1 b.1) (coordinateBounds _ _).1
  self a := by rw [l.self,r.self,addZero]
  symmetric a b := by rw [l.symmetric a.1 b.1,r.symmetric a.2 b.2]
  triangle a b c := by
    rw [regroup]
    exact addMonoPair (l.triangle a.1 b.1 c.1) (r.triangle a.2 b.2 c.2)
  separates a b eq := by
    have h := coordinateBounds (l.dist a.1 b.1) (r.dist a.2 b.2)
    rw [eq] at h
    exact Prod.ext (l.separates _ _ (valueAntisymmetric _ _ h.1 (l.nonnegative _ _)))
                   (r.separates _ _ (valueAntisymmetric _ _ h.2 (r.nonnegative _ _)))

/-- If calibrated tables for two probes agree in each coordinate, the
    physically serial sum converges to the product metric. -/
theorem serialCommonLimit {f g u v : Nat → Nat} (hf : Cauchy f) (hg : Cauchy g)
    (one : Close f u) (two : Close g v) :
    Converges (fun n => u n+v n) (add (limit f hf) (limit g hg)) :=
  commonReading (cauchySum hf hg) ⟨dominatesSum one.1 two.1,dominatesSum one.2 two.2⟩

theorem sumConverges {u v : Nat → Nat} {a b : Value}
    (ua : Converges u a) (vb : Converges v b) : Converges (fun n => u n+v n) (add a b) := by
  have hu := (limitExistsIffCauchy u).1 ⟨a,ua⟩
  have hv := (limitExistsIffCauchy v).1 ⟨b,vb⟩
  rw [uniqueLimit ua (nameConverges u hu),uniqueLimit vb (nameConverges v hv)]
  exact nameConverges _ (cauchySum hu hv)

open OperationalNetwork.Periodic

/-- The two-angle space uses the actual sum geometry selected by serial local
    moves. Probes may set different internal delays in every row and column
    factor (one independent profile per angular factor). -/
def angularProduct : LimitMetric (AnglePoint × AnglePoint) := serialLimit angularMetric angularMetric

theorem torusProbeLimit (p q : CellProbe) (x y : Angle × Angle) :
    Converges (fun n => measuredAngle p x.1 y.1 n + measuredAngle q x.2 y.2 n)
      (angularProduct.dist (anglePoint x.1,anglePoint x.2) (anglePoint y.1,anglePoint y.2)) :=
  sumConverges (fullAngleLimit p x.1 y.1) (fullAngleLimit q x.2 y.2)

private def torusPort (p : CellProbe) (x : Angle) (n : Nat) : Fin (2^(n+2)-1+1) :=
  ⟨probePosition p x n,by
    have inside := validPrefix x n
    have offset := (p n (cellNumber x n)).isLt
    have power : 2^(n+2)=4*2^n := by rw [Nat.pow_add,Nat.mul_comm]
    unfold probePosition
    omega⟩

/-- The sum sequence in torusProbeLimit is the *measured* first arrival of
    the 2D locally updated network at all n+2. The finite horizon may expire. -/
theorem torusFirstTick (p q : CellProbe) (x y : Angle × Angle) (n budget : Nat) :
    let L := unitLinks (2^(n+2)-1)
    let receiver (z : Angle × Angle) := (torusPort p z.1 n,torusPort q z.2 n)
    let t := measuredAngle p x.1 y.1 (n+2) + measuredAngle q x.2 y.2 (n+2)
    SignalNetwork.firstTick? (serialLinks L L) (receiver x) (receiver y) budget =
      if t ≤ budget then some t else none := by
  dsimp only
  have left := measuredAngularPulse p x.1 y.1 n (measuredAngle p x.1 y.1 (n+2))
  have right := measuredAngularPulse q x.2 y.2 n (measuredAngle q x.2 y.2 (n+2))
  simp only [Nat.le_refl,ite_true] at left right
  exact serialFirstTick _ _ _ _ left right budget

/-- Adding a genuine diagonal actuator leaves both isolated one-coordinate
    distances unchanged but halves the first delivery to the opposite corner. -/
theorem diagonalChangesGeometry :
    let wire : Bool → List Bool := fun x => [!x]
    let serial := serialLinks wire wire
    let diagonal := fun v : Bool × Bool => (!v.1,!v.2)::serial v
    let time := fun (g : Bool × Bool → List (Bool × Bool)) v =>
      SignalNetwork.firstTick? g (false,false) v 2
    time serial (true,false) = some 1 ∧ time diagonal (true,false) = some 1 ∧
    time serial (false,true) = some 1 ∧ time diagonal (false,true) = some 1 ∧
    time serial (true,true) = some 2 ∧ time diagonal (true,true) = some 1 := by decide

end OperationalNetwork.ProductGeometry
