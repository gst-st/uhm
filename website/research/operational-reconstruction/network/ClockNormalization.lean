import LimitMetric
set_option autoImplicit false
namespace OperationalNetwork.Continuum

/-- Raw positive clock calibration. All obligations below use natural
    cross-products; neither rational normalization nor a real limit is assumed. -/
structure ClockReading where
  ticks : Nat
  unit : Nat
  live : 0 < unit

def roundUp (a : ClockReading) (n : Nat) : Nat := (2^n*a.ticks + a.unit - 1) / a.unit

theorem roundUpBudget (a : ClockReading) (n b : Nat) :
    roundUp a n ≤ b ↔ 2^n*a.ticks ≤ b*a.unit := by
  have opposite := Nat.le_div_iff_mul_le (x:=b+1) (y:=2^n*a.ticks+a.unit-1) a.live
  rw [Nat.succ_mul] at opposite
  change (2^n*a.ticks+a.unit-1)/a.unit ≤ b ↔ _
  have hu := a.live
  constructor
  · intro h
    by_cases bound : 2^n*a.ticks ≤ b*a.unit
    · exact bound
    · have wrong := opposite.mpr (by omega)
      omega
  · intro h
    by_cases bound : (2^n*a.ticks+a.unit-1)/a.unit ≤ b
    · exact bound
    · have wrong := opposite.mp (by omega)
      omega

/-- The dyadic upper reading is at least the exact fraction and overshoots
    by strictly less than one unit of its last place, including at zero. -/
theorem roundUpError (a : ClockReading) (n : Nat) :
    2^n*a.ticks ≤ roundUp a n*a.unit ∧ roundUp a n*a.unit < 2^n*a.ticks+a.unit := by
  refine ⟨(roundUpBudget a n _).1 (Nat.le_refl _),?_⟩
  have h := Nat.div_mul_le_self (2^n*a.ticks+a.unit-1) a.unit
  change (2^n*a.ticks+a.unit-1)/a.unit*a.unit < _
  have hu := a.live
  omega

theorem roundedRelay (a b c u n : Nat) (hu : 0 < u) (relay : c ≤ a+b) :
    roundUp ⟨c,u,hu⟩ n ≤ roundUp ⟨a,u,hu⟩ n + roundUp ⟨b,u,hu⟩ n := by
  apply (roundUpBudget _ _ _).2
  have one := (roundUpError ⟨a,u,hu⟩ n).1
  have two := (roundUpError ⟨b,u,hu⟩ n).1
  have h := Nat.mul_le_mul_left (2^n) relay
  change 2^n*c ≤ (_+_)*u
  rw [Nat.add_mul]
  exact Nat.le_trans h (by simpa only [Nat.mul_add] using Nat.add_le_add one two)

theorem roundZero (u n : Nat) (hu : 0<u) : roundUp ⟨0,u,hu⟩ n = 0 :=
  Nat.eq_zero_of_le_zero ((roundUpBudget _ _ 0).2 (by simp))

/-- Flooring each reading may already violate the triangle on a unit path
    with two successive edges, measured in units of two ticks. -/
theorem floorBreaksRelay : ¬ (2/2 : Nat) ≤ 1/2+1/2 := by decide

/-- These are respectively a one-sided dyadic tolerance, its vanishing on
    the sequence of measurements, the Cauchy tail and robust positivity. -/
def Within (k : Nat) (a b : ClockReading) :=
  2^k*a.ticks*b.unit ≤ 2^k*b.ticks*a.unit+a.unit*b.unit

def ClockDominated (a b : Nat → ClockReading) : Prop :=
  ∀ k, ∃ N, ∀ n, N≤n → Within k (a n) (b n)

def ClockCauchy (a : Nat → ClockReading) : Prop :=
  ∀ k, ∃ N, ∀ n m, N≤n → n≤m → Within k (a m) (a n) ∧ Within k (a n) (a m)

def ClockPositive (a : Nat → ClockReading) : Prop :=
  ∃ k N : Nat, ∀ n, N≤n → (a n).unit ≤ 2^k*(a n).ticks

def dyadicObservation (f : Nat → Nat) (n : Nat) : ClockReading := ⟨f n,2^n,Nat.pow_pos (by decide)⟩
def encodeClock (a : Nat → ClockReading) (n : Nat) := roundUp (a n) n

private theorem withinWeaken {a b : ClockReading} {k : Nat} (h : Within (k+1) a b) :
    Within k a b := by
  unfold Within at *
  rw [Nat.pow_succ,Nat.mul_comm (2^k) 2,Nat.two_mul] at h
  simp only [Nat.add_mul] at h
  omega

private theorem withinCompose {a b c : ClockReading} {k : Nat}
    (ab : Within (k+1) a b) (bc : Within (k+1) b c) : Within k a c := by
  unfold Within at *
  have ab' := Nat.mul_le_mul_right c.unit ab
  have bc' := Nat.mul_le_mul_right a.unit bc
  apply Nat.le_of_mul_le_mul_right _ b.live
  rw [Nat.pow_succ,Nat.mul_comm (2^k) 2,Nat.two_mul] at ab' bc'
  simp only [Nat.add_mul] at ab' bc' ⊢
  simp only [Nat.mul_left_comm,Nat.mul_comm] at ab' bc' ⊢
  omega

private theorem threeHops {a b c d : ClockReading} {k : Nat}
    (ab : Within (k+2) a b) (bc : Within (k+2) b c) (cd : Within (k+2) c d) : Within k a d :=
  withinCompose (withinCompose ab bc) (withinWeaken cd)

theorem clockRoundingClose (a : Nat → ClockReading) :
    ClockDominated a (dyadicObservation (encodeClock a)) ∧
      ClockDominated (dyadicObservation (encodeClock a)) a := by
  constructor
  · intro k
    refine ⟨0,?_⟩
    intro n _
    have h := Nat.mul_le_mul_left (2^k) (roundUpError (a n) n).1
    unfold Within; dsimp only [dyadicObservation,encodeClock]
    simp only [Nat.mul_assoc,Nat.mul_left_comm,Nat.mul_comm] at h ⊢
    omega
  · intro k
    refine ⟨k,?_⟩
    intro n kn
    have h := Nat.mul_le_mul_left (2^k) (Nat.le_of_lt (roundUpError (a n) n).2)
    have p := Nat.mul_le_mul_right (a n).unit (Nat.pow_le_pow_right (by decide : 0<2) kn)
    unfold Within; dsimp only [dyadicObservation,encodeClock]
    simp only [Nat.mul_add,Nat.mul_assoc,Nat.mul_left_comm,Nat.mul_comm] at h p ⊢
    omega

private theorem transferClockCauchy {a b : Nat → ClockReading} (h : ClockCauchy a)
    (ab : ClockDominated a b) (ba : ClockDominated b a) : ClockCauchy b := by
  intro k
  obtain ⟨A,hA⟩ := h (k+2)
  obtain ⟨B,hB⟩ := ab (k+2)
  obtain ⟨C,hC⟩ := ba (k+2)
  refine ⟨max A (max B C),?_⟩
  intro n m hn nm
  have aN : A≤n := Nat.le_trans (Nat.le_max_left _ _) hn
  have bN : B≤n := Nat.le_trans (Nat.le_max_left B C) (Nat.le_trans (Nat.le_max_right _ _) hn)
  have cN : C≤n := Nat.le_trans (Nat.le_max_right B C) (Nat.le_trans (Nat.le_max_right _ _) hn)
  obtain ⟨one,two⟩ := hA n m aN nm
  exact ⟨threeHops (hC _ (Nat.le_trans cN nm)) one (hB _ bN),
         threeHops (hC _ cN) two (hB _ (Nat.le_trans bN nm))⟩

private theorem dyadicTailTest (f : Nat → Nat) {k n m : Nat} (nm : n≤m) :
    (Within k (dyadicObservation f m) (dyadicObservation f n) ∧
     Within k (dyadicObservation f n) (dyadicObservation f m)) ↔
    (2^k*f m ≤ 2^k*(2^(m-n)*f n)+2^m ∧ 2^k*(2^(m-n)*f n) ≤ 2^k*f m+2^m) := by
  have powers : 2^n*2^(m-n) = 2^m := by rw [← Nat.pow_add,Nat.add_sub_of_le nm]
  have hr : 2^k*f n*2^m = 2^k*(2^(m-n)*f n)*2^n := by rw [←powers]; ac_rfl
  simp only [Within,dyadicObservation,hr,Nat.mul_comm (2^n) (2^m),← Nat.add_mul]
  have pos : 0 < 2^n := Nat.pow_pos (by decide)
  exact and_congr ⟨fun h => Nat.le_of_mul_le_mul_right h pos,Nat.mul_le_mul_right _⟩
    ⟨fun h => Nat.le_of_mul_le_mul_right h pos,Nat.mul_le_mul_right _⟩

private theorem dyadicCauchy (f : Nat → Nat) : ClockCauchy (dyadicObservation f) ↔ Cauchy f := by
  constructor <;> intro h k <;> obtain ⟨N,hN⟩ := h k <;> refine ⟨N,?_⟩ <;> intro n m hn nm
  · exact (dyadicTailTest f nm).1 (hN n m hn nm)
  · exact (dyadicTailTest f nm).2 (hN n m hn nm)

/-- Equivalence in BOTH directions with the raw cross-multiplied Cauchy
    condition. Neither bounded clock ratios nor commensurate clocks are needed. -/
theorem arbitraryClockCauchy (a : Nat → ClockReading) : Cauchy (encodeClock a) ↔ ClockCauchy a := by
  obtain ⟨toCode,fromCode⟩ := clockRoundingClose a
  rw [←dyadicCauchy]
  exact ⟨fun h => transferClockCauchy h fromCode toCode,fun h => transferClockCauchy h toCode fromCode⟩

private theorem clockDominatesTrans {a b c : Nat → ClockReading}
    (ab : ClockDominated a b) (bc : ClockDominated b c) : ClockDominated a c := by
  intro k
  obtain ⟨N,hN⟩ := ab (k+1)
  obtain ⟨M,hM⟩ := bc (k+1)
  exact ⟨max N M,fun n hn => withinCompose (hN n (Nat.le_trans (Nat.le_max_left _ _) hn))
    (hM n (Nat.le_trans (Nat.le_max_right _ _) hn))⟩

private theorem dyadicDom (f g : Nat → Nat) : ClockDominated (dyadicObservation f) (dyadicObservation g) ↔
    Dominated f g := by
  have point (k n : Nat) : Within k (dyadicObservation f n) (dyadicObservation g n) ↔
      2^k*f n ≤ 2^k*g n + 2^n := by
    simp only [Within,dyadicObservation,← Nat.add_mul]
    exact ⟨fun h => Nat.le_of_mul_le_mul_right h (Nat.pow_pos (by decide)),Nat.mul_le_mul_right _⟩
  constructor <;> intro h k <;> obtain ⟨N,hN⟩ := h k <;> refine ⟨N,?_⟩ <;> intro n hn
  · exact (point k n).1 (hN n hn)
  · exact (point k n).2 (hN n hn)

theorem arbitraryClockComparison (a b : Nat → ClockReading) :
    Dominated (encodeClock a) (encodeClock b) ↔ ClockDominated a b := by
  obtain ⟨ac,ca⟩ := clockRoundingClose a
  obtain ⟨bc,cb⟩ := clockRoundingClose b
  rw [←dyadicDom]
  exact ⟨fun h => clockDominatesTrans ac (clockDominatesTrans h cb),
         fun h => clockDominatesTrans ca (clockDominatesTrans h bc)⟩

private theorem withinPositive {a b : ClockReading} {k : Nat} (sep : a.unit ≤ 2^k*a.ticks)
    (ab : Within (k+1) a b) : b.unit ≤ 2^(k+1)*b.ticks := by
  apply Nat.le_of_mul_le_mul_right _ a.live
  have lift := Nat.mul_le_mul_right b.unit sep
  unfold Within at ab
  rw [Nat.pow_succ,Nat.mul_comm (2^k) 2,Nat.two_mul] at ab ⊢
  simp only [Nat.add_mul] at ab ⊢
  rw [Nat.mul_comm b.unit a.unit]
  omega

private theorem clockPositiveMoves {a b : Nat → ClockReading} (ab : ClockDominated a b)
    (pos : ClockPositive a) : ClockPositive b := by
  obtain ⟨k,A,hA⟩ := pos
  obtain ⟨B,hB⟩ := ab (k+1)
  exact ⟨k+1,max A B,fun n hn => withinPositive (hA n (Nat.le_trans (Nat.le_max_left _ _) hn))
    (hB n (Nat.le_trans (Nat.le_max_right _ _) hn))⟩

theorem arbitraryClockPositivity (a : Nat → ClockReading) : PositiveTail (encodeClock a) ↔ ClockPositive a := by
  obtain ⟨ac,ca⟩ := clockRoundingClose a
  change ClockPositive (dyadicObservation (encodeClock a)) ↔ _
  exact ⟨clockPositiveMoves ca,clockPositiveMoves ac⟩

/-- A dyadic encoding of the ordinary transfer costs in any positive clocks.
    Exact relay inequalities hold after rounding at *every* finite scale. -/
def fromClocks {X : Type} (e : Nat → Experiment X) (u : Nat → Nat) (hu : ∀ n, 0<u n)
    (hc : ∀ x y, ClockCauchy (fun n => ⟨cost (e n) x y,u n,hu n⟩))
    (rev : ∀ x y, ClockDominated (fun n => ⟨cost (e n) x y,u n,hu n⟩)
                                  (fun n => ⟨cost (e n) y x,u n,hu n⟩)) :
    LimitPseudometric X :=
  let raw (x y : X) (n : Nat) : ClockReading := ⟨cost (e n) x y,u n,hu n⟩
  fromReadings (fun n x y => encodeClock (raw x y) n)
    (fun x y => (arbitraryClockCauchy _).2 (hc x y))
    (fun n x => by change roundUp ⟨cost (e n) x x,u n,hu n⟩ n=0
                   rw [(zeroIffSame _ x x).2 rfl,roundZero])
    (fun x y => ⟨(arbitraryClockComparison _ _).2 (rev x y),(arbitraryClockComparison _ _).2 (rev y x)⟩)
    (fun n x y z => roundedRelay _ _ _ _ _ (hu n) (triangleFromRelay (e n) x y z))

/-- A joint positive limiting reading exists iff ONE probe has a Cauchy tail
    and a macroscopic lower bound, and both raw calibrated records simulate
    each other's costs to vanishing error. All four tests use finite ticks. -/
theorem commonPositiveClockLimitIff (a b : Nat → ClockReading) :
    (∃ x : Value, Converges (encodeClock a) x ∧ Converges (encodeClock b) x ∧ Positive x) ↔
      ClockCauchy a ∧ ClockDominated a b ∧ ClockDominated b a ∧ ClockPositive a := by
  constructor
  · rintro ⟨x,hx,hy,pos⟩
    have ha := (limitExistsIffCauchy _).1 ⟨x,hx⟩
    have hb := (limitExistsIffCauchy _).1 ⟨x,hy⟩
    have ex := uniqueLimit (nameConverges _ ha) hx
    have ey := uniqueLimit (nameConverges _ hb) hy
    have agree := (limitEq ha hb).1 (ex.trans ey.symm)
    exact ⟨(arbitraryClockCauchy _).1 ha,(arbitraryClockComparison _ _).1 agree.1,
           (arbitraryClockComparison _ _).1 agree.2,(arbitraryClockPositivity _).1
           ((positiveLimitIff ha).1 (ex.symm ▸ pos))⟩
  · rintro ⟨raw,ab,ba,pos⟩
    let ha := (arbitraryClockCauchy _).2 raw
    have close : Close (encodeClock a) (encodeClock b) :=
      ⟨(arbitraryClockComparison _ _).2 ab,(arbitraryClockComparison _ _).2 ba⟩
    exact ⟨_,nameConverges _ ha,commonReading ha close,
           (positiveLimitIff ha).2 ((arbitraryClockPositivity _).2 pos)⟩

end OperationalNetwork.Continuum
