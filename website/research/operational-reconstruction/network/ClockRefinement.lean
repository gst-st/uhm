import SignalNetwork
set_option autoImplicit false

namespace OperationalNetwork.SignalNetwork

/-- Each original station is the zero phase of a physical line of k+1 unit
    stages. Interior stages receive from their predecessor; the receiver at
    zero gets the *last* stage of each original neighbour. -/
def clockLinks {X : Type} (links : X → List X) (k : Nat) :
    X × Fin (k+1) → List (X × Fin (k+1))
  | (y,j) => if j.val = 0 then (links y).map (fun z => (z,⟨k,by omega⟩))
    else [(y,⟨j.val-1,by have := j.isLt; omega⟩)]

variable {X : Type} [DecidableEq X]

/-- At an internal stage, there is only one predecessor; at a station,
    signals arrive from all adjacent final stages on the same tick. -/
def ClockPhase (links : X → List X) (s : X) (k t r m : Nat) : Prop :=
  ∀ y (j : Fin (k+1)), pulse (clockLinks links k) (s,0) t (y,j) =
    if j.val = r then pulse links s m y else false

theorem initialClockPhase (links : X → List X) (s : X) (k : Nat) :
    ClockPhase links s k 0 0 0 := by
  intro y j
  by_cases h : j.val = 0
  · have hj : j = 0 := Fin.ext h
    simp [hj,pulse]
  · have hj : (0 : Fin (k+1)) ≠ j := fun eq => h (congrArg Fin.val eq.symm)
    simp [h,pulse,hj]

theorem interiorClockStep (links : X → List X) (s : X) {k t r m}
    (prev : ClockPhase links s k t r m) (hr : r < k) : ClockPhase links s k (t+1) (r+1) m := by
  unfold ClockPhase at prev
  intro y j
  by_cases hj : j.val = 0
  · have away : j.val ≠ r+1 := by omega
    simp only [pulse, clockLinks, ite_eq_left hj, ite_eq_right away, List.any_map, List.any_eq_false,
      Function.comp_apply, prev, ite_eq_right (Nat.ne_of_gt hr), Bool.false_eq_true, not_false_eq_true, implies_true]
  · have shift : j.val - 1 = r ↔ j.val = r+1 := by
      obtain ⟨a,ha⟩ := Nat.exists_eq_succ_of_ne_zero hj
      rw [ha]
      exact ⟨congrArg Nat.succ,Nat.succ.inj⟩
    simp [pulse, clockLinks, hj, prev, shift]

theorem finalClockStep (links : X → List X) (s : X) {k t m}
    (prev : ClockPhase links s k t k m) : ClockPhase links s k (t+1) 0 (m+1) := by
  unfold ClockPhase at prev
  intro y j
  by_cases hj : j.val = 0
  · simp [pulse, clockLinks, hj, prev, Function.comp_def]
  · have hjk := j.isLt
    have diff : j.val-1 ≠ k := by omega
    simp [pulse, clockLinks, hj, prev, diff]

private theorem fillClockStages (links : X → List X) (s : X) {k t m}
    (zero : ClockPhase links s k t 0 m) {r} (bound : r ≤ k) :
    ClockPhase links s k (t+r) r m := by
  induction r with
  | zero => exact zero
  | succ r ih =>
    exact interiorClockStep links s (ih (by omega)) (by omega)

theorem allClockPhases (links : X → List X) (s : X) (k m r : Nat) (bound : r ≤ k) :
    ClockPhase links s k (m*(k+1)+r) r m := by
  suffices zero : ClockPhase links s k (m*(k+1)) 0 m from fillClockStages links s zero bound
  clear r bound
  induction m with
  | zero => simpa using initialClockPhase links s k
  | succ m ih =>
    have last := fillClockStages links s ih (Nat.le_refl k)
    simpa only [Nat.succ_mul, Nat.add_assoc] using finalClockStep links s last

theorem stationPulseAtMultiple (links : X → List X) (s y : X) (k m : Nat) :
    pulse (clockLinks links k) (s,0) (m*(k+1)) (y,0) = pulse links s m y := by
  simpa using allClockPhases links s k m 0 (Nat.zero_le _) y 0

theorem refinedHitIff (links : X → List X) (s y : X) (k t : Nat) :
    pulse (clockLinks links k) (s,0) t (y,0) = true ↔
      ∃ m, t = m*(k+1) ∧ pulse links s m y = true := by
  constructor
  · intro hit
    have bound : t % (k+1) ≤ k := by have := Nat.mod_lt t (y := k+1) (by omega); omega
    have phase := allClockPhases links s k (t/(k+1)) (t%(k+1)) bound y 0
    rw [Nat.div_add_mod', hit] at phase
    by_cases exactTick : 0 = t%(k+1)
    · refine ⟨t/(k+1), ?_, ?_⟩
      · have h := Nat.div_add_mod' t (k+1)
        omega
      · simpa [exactTick] using phase.symm
    · simp [exactTick] at phase
  · rintro ⟨m,rfl,active⟩
    rwa [stationPulseAtMultiple]

theorem firstTickFromSignal (links : X → List X) (s y : X) (b t : Nat) :
    firstTick? links s y b = some t ↔ t ≤ b ∧ pulse links s t y = true ∧
      ∀ c, pulse links s c y = true → t ≤ c := by
  rw [firstTickSpec]
  constructor
  · rintro ⟨hb,trip,least⟩
    refine ⟨hb,(pulseIffTrip _ _ _ _).2 trip,?_⟩
    intro c hit
    obtain ⟨n,walk⟩ := (pulseIffTrip _ _ _ _).1 hit
    exact least c n walk
  · rintro ⟨hb,hit,least⟩
    exact ⟨hb,(pulseIffTrip _ _ _ _).1 hit,fun c n walk =>
      least c ((pulseIffTrip _ _ _ _).2 ⟨n,walk⟩)⟩

/-- Exact finite-window equality at the *ordinary* receivers, including
    unreachable targets and budgets ending midway through a delay line. -/
theorem clockFirstTick (links : X → List X) (s y : X) (k budget : Nat) :
    firstTick? (clockLinks links k) (s,0) (y,0) budget =
      (firstTick? links s y (budget/(k+1))).map (fun m => m*(k+1)) := by
  apply Option.ext
  intro t
  rw [firstTickFromSignal, Option.map_eq_some_iff]
  constructor
  · rintro ⟨hb,hit,least⟩
    obtain ⟨m,rfl,signal⟩ := (refinedHitIff _ _ _ _ _).1 hit
    refine ⟨m,(firstTickFromSignal _ _ _ _ _).2 ⟨(Nat.le_div_iff_mul_le (by omega)).2 hb,
      signal,?_⟩,rfl⟩
    intro c hc
    have h := least (c*(k+1)) ((refinedHitIff _ _ _ _ _).2 ⟨c,rfl,hc⟩)
    exact Nat.le_of_mul_le_mul_right h (by omega)
  · rintro ⟨m,hm,rfl⟩
    obtain ⟨hb,hit,least⟩ := (firstTickFromSignal _ _ _ _ _).1 hm
    refine ⟨(Nat.le_div_iff_mul_le (by omega)).1 hb,(refinedHitIff _ _ _ _ _).2 ⟨m,rfl,hit⟩,?_⟩
    intro t ht
    obtain ⟨c,rfl,hc⟩ := (refinedHitIff _ _ _ _ _).1 ht
    exact Nat.mul_le_mul_right _ (least c hc)

end OperationalNetwork.SignalNetwork
