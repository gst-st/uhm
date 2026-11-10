import ClockNormalization
import ClockRefinement

set_option autoImplicit false
namespace OperationalNetwork.Drift
open Continuum SignalNetwork

/-- At physical scale t, the calibration interval is the dyadic epoch
    containing t+1. During one epoch, the observable interval length slowly
    rises from 1 to 2 and falls back. -/
def width (t : Nat) := 2^(t+1).log2
def count (w r : Nat) := w + 2*min r (w-r)
def sample (t : Nat) : ClockReading :=
  ⟨count (width t) (t+1-width t),width t,Nat.pow_pos (by decide)⟩

private theorem inEpoch (t : Nat) : width t ≤ t+1 ∧ t+1 < width t + width t := by
  have high := Nat.lt_log2_self (n:=t+1)
  rw [Nat.pow_succ,Nat.mul_two] at high
  exact ⟨Nat.log2_self_le (Nat.succ_ne_zero _),high⟩

private theorem epochWidth {t e : Nat} (lo : 2^e ≤ t+1) (hi : t+1 < 2^e+2^e) : width t=2^e := by
  unfold width
  have eq : (t+1).log2=e := (Nat.log2_eq_iff (Nat.succ_ne_zero _)).2
    ⟨lo,by simpa only [Nat.pow_succ,Nat.mul_two] using hi⟩
  rw [eq]

theorem boundedRate (t : Nat) : (sample t).unit ≤ (sample t).ticks ∧
    (sample t).ticks ≤ 2*(sample t).unit := by
  dsimp only [sample,count]
  have ⟨lo,hi⟩ := inEpoch t
  constructor <;> omega

private theorem sameUnit {a b w : Nat} (wpos : 0<w) (k : Nat) :
    Within k ⟨a,w,wpos⟩ ⟨b,w,wpos⟩ ↔ 2^k*a ≤ 2^k*b+w := by
  simp only [Within,←Nat.add_mul]
  exact ⟨fun h => Nat.le_of_mul_le_mul_right h wpos,Nat.mul_le_mul_right _⟩

/-- Independent equal-time samples use clock w or its double at the epoch
    seam. The normalized change is at most 2/w, including across that seam. -/
theorem adjacentQuiet : ClockDominated sample (fun n => sample (n+1)) ∧
    ClockDominated (fun n => sample (n+1)) sample := by
  suffices both : ∀ k, ∃ N, ∀ t, N ≤ t →
      Within k (sample t) (sample (t+1)) ∧ Within k (sample (t+1)) (sample t) by
    exact ⟨fun k => (both k).imp (fun _ h t ht => (h t ht).1),
           fun k => (both k).imp (fun _ h t ht => (h t ht).2)⟩
  intro k
  refine ⟨2^(k+1),?_⟩
  intro t ht
  let w := width t
  have hw : 0<w := (sample t).live
  have ⟨lo,hi⟩ := inEpoch t
  change w ≤ t+1 at lo
  change t+1 < w+w at hi
  have large : 2^k+2^k ≤ w := by
    have le := (Nat.le_log2 (Nat.succ_ne_zero t)).2 (Nat.le_trans ht (Nat.le_succ _))
    change 2^k+2^k ≤ 2^(t+1).log2
    simpa only [Nat.pow_succ,Nat.mul_two] using Nat.pow_le_pow_right (n:=2) (by decide) le
  by_cases jump : t+2=w+w
  · have nxt : width (t+1) = w+w := by
      have h := epochWidth (t:=t+1) (e:=(t+1).log2+1)
      simp only [Nat.pow_succ,Nat.mul_two] at h
      exact h (by change w+w ≤ t+2; omega) (by change t+2 < (w+w)+(w+w); omega)
    let a := (sample t).ticks
    have ad : w ≤ a ∧ a ≤ w+2 := by
      change w ≤ count w (t+1-w) ∧ count w (t+1-w) ≤ w+2
      unfold count
      constructor <;> omega
    have nextCount : (sample (t+1)).ticks = w+w := by
      simp only [sample,nxt,show t+1+1=w+w from jump,Nat.sub_self,count,Nat.zero_min,Nat.mul_zero,Nat.add_zero]
    have one : 2^k*a ≤ 2^k*w+w := by
      have h := Nat.mul_le_mul_left (2^k) ad.2
      rw [Nat.mul_add,Nat.mul_two] at h
      omega
    have two : 2^k*w ≤ 2^k*a + w := Nat.le_trans (Nat.mul_le_mul_left _ ad.1) (Nat.le_add_right _ _)
    change 2^k*a*(sample (t+1)).unit ≤ 2^k*(sample (t+1)).ticks*w+w*(sample (t+1)).unit ∧
      2^k*(sample (t+1)).ticks*w ≤ 2^k*a*(sample (t+1)).unit+(sample (t+1)).unit*w
    rw [nextCount]
    change 2^k*a*width (t+1) ≤ _ + w*width (t+1) ∧ _ ≤ 2^k*a*width (t+1)+width (t+1)*w
    rw [nxt,Nat.mul_comm (w+w) w]
    have eq : 2^k*(w+w)*w = 2^k*w*(w+w) := Nat.mul_right_comm _ _ _
    rw [eq,←Nat.add_mul,←Nat.add_mul]
    exact ⟨Nat.mul_le_mul_right _ one,Nat.mul_le_mul_right _ two⟩
  · have nxt : width (t+1)=w := epochWidth (e:=(t+1).log2) (by change w≤t+2; omega)
        (by change t+2<w+w; omega)
    let a := count w (t+1-w)
    let b := count w (t+2-w)
    have ab : a ≤ b+2 ∧ b ≤ a+2 := by dsimp only [a,b,count]; constructor <;> omega
    have lower := Nat.mul_le_mul_left (2^k) ab.1
    have upper := Nat.mul_le_mul_left (2^k) ab.2
    simp only [Nat.mul_add,Nat.mul_two] at lower upper
    have e : sample (t+1) = ⟨b,w,hw⟩ := by
      unfold sample
      simp only [nxt,b]
    rw [e]
    change Within k ⟨a,w,hw⟩ ⟨b,w,hw⟩ ∧ Within k ⟨b,w,hw⟩ ⟨a,w,hw⟩
    rw [sameUnit,sameUnit]
    constructor <;> omega

/-- The low endpoint and midpoint of every sufficiently late epoch still
    have normalized durations 1 and 2 respectively. -/
theorem driftingTail : ¬ClockCauchy sample := by
  intro h
  obtain ⟨N,hN⟩ := h 1
  let v := 2^(N+1)
  let w := 2^(N+2)
  have vw : w = v+v := Nat.pow_succ 2 (N+1) |>.trans (Nat.mul_two _)
  have vp : 0<v := Nat.pow_pos (by decide)
  have Nv : N<v := Nat.lt_trans (Nat.lt_succ_self N) Nat.lt_two_pow_self
  let t := w-1
  let m := w+v-1
  have ht : t+1=w := by dsimp [t]; omega
  have hm : m+1=w+v := by dsimp [m]; omega
  have wt : width t=w := epochWidth (e:=N+2) (by rw [ht]; exact Nat.le_refl _)
      (by change t+1<w+w; omega)
  have wm : width m=w := epochWidth (e:=N+2) (by change w ≤ m+1; omega)
      (by change m+1<w+w; omega)
  have lo : sample t = ⟨w,w,by omega⟩ := by
    unfold sample; simp only [wt,ht,Nat.sub_self,count,Nat.zero_min,Nat.mul_zero,Nat.add_zero]
  have hi : sample m = ⟨w+w,w,by omega⟩ := by
    unfold sample
    simp only [wm,hm,Nat.add_sub_cancel_left,count]
    have sub : w-v=v := by omega
    rw [sub,Nat.min_self,Nat.two_mul,←vw]
  have bad := (hN t m (by omega) (by omega)).1
  rw [lo,hi,sameUnit] at bad
  simp only [Nat.pow_one,Nat.two_mul] at bad
  omega

theorem noMeasuredLimit : ¬∃ x : Value, Converges (encodeClock sample) x :=
  fun h => driftingTail ((arbitraryClockCauchy sample).1 ((limitExistsIffCauchy _).1 h))

/-- A two-station directed return cycle with H actual one-tick pipeline
    stages at each site. Both probes can be read by exactly the same Boolean
    receiver; it still has no limiting distance for this calibration series. -/
def returnRing (x : Bool) := [!x]

theorem driftingPhysicalTime (n : Nat) (x : Bool) :
    let ticks := (sample n).ticks
    firstTick? (clockLinks returnRing (ticks-1)) (x,0) (!x,0) ticks = some ticks := by
  dsimp only
  let H := (sample n).ticks
  have high := (boundedRate n).1
  have live := (sample n).live
  have pos : 0<H := Nat.lt_of_lt_of_le live high
  have eq : H-1+1=H := by omega
  rw [clockFirstTick]
  change (firstTick? returnRing x (!x) (H/(H-1+1))).map (fun m => m*(H-1+1)) = some H
  rw [eq,Nat.div_self pos]
  cases x <;> simp [firstTick?,scan,pulse,returnRing]

end OperationalNetwork.Drift
