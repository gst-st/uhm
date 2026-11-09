import MathFoundations.ToposUHM.DimensionPinch
import Std

/-!
Check from the built math-foundations/lean4-mf-kernel checkout with
`lake env lean /absolute/path/to/AddressFusion.lean`.

The two physical premises are a calibrated unital signed-XOR fusion branch
and a decoder reading that branch's address alphabet. Both are explicit.
-/
set_option autoImplicit false

namespace ReconstructionAudit.AddressFusion
open MathFoundations.Hypermath MathFoundations.ToposUHM

/-- Output on (e_p + e_(p+h)) and (e_r + t e_(r+h)), t = ±1.
    The two coefficients occur at p+r and p+r+h, distinct when h ≠ 0.
    The sign bits are ordered (p,r), (p+h,r+h), (p,r+h), (p+h,r).
    A uniform success amplitude multiplies both outputs by the same scalar. -/
def probeOutput (a d b c : F2) (t : Int) : Int × Int :=
  (a.toSign + t * d.toSign, t * b.toSign + c.toSign)

def bothVisible (a d b c : F2) : Prop :=
  probeOutput a d b c 1 ≠ (0, 0) ∧ probeOutput a d b c (-1) ≠ (0, 0)

theorem visible_iff_odd (a d b c : F2) :
    bothVisible a d b c ↔ a + d + b + c = 1 := by
  unfold bothVisible
  cases a <;> cases d <;> cases b <;> cases c <;> decide

def NoDarkPairs {k : Nat} (f : Cochain k) : Prop :=
  ∀ h p r : Cube k, h ≠ zeroCube k →
    bothVisible (f p r) (f (cubeXor p h) (cubeXor r h))
      (f p (cubeXor r h)) (f (cubeXor p h) r)

/-- Includes overlapping input supports. The rectangle at p=r=0 forces the
    negative squares, and p=r=a, h=a+b forces skewness for a ≠ b. -/
theorem viable_of_noDark {k : Nat} {f : Cochain k}
    (unit : IsNormalized k f) (visible : NoDarkPairs f) : IsViableCochain k f := by
  have odd (h p r : Cube k) (hh : h ≠ zeroCube k) :=
    (visible_iff_odd _ _ _ _).mp (visible h p r hh)
  have diag (a : Cube k) (ha : a ≠ zeroCube k) : f a a = 1 := by
    simpa only [zero_cubeXor, unit.1, unit.2, F2.zero_add, F2.add_zero] using
      odd a (zeroCube k) (zeroCube k) ha
  refine ⟨unit, diag, ?_, fun h p r hh _ _ => odd h p r hh⟩
  intro a b ha hb hab
  have different : cubeXor a b ≠ zeroCube k := fun h => hab (cubeXor_eq_zero_iff.mp h)
  have pair := odd (cubeXor a b) a a different
  simpa only [cubeXor_cancel_left, diag a ha, diag b hb, F2.add_self, F2.zero_add] using pair

private def addresses : (k : Nat) → List (Cube k)
  | 0 => [PUnit.unit]
  | k + 1 =>
    (addresses k).map (fun x => (x, F2.zero)) ++ (addresses k).map (fun x => (x, F2.one))

private theorem addressCount (k : Nat) : (addresses k).length = 2 ^ k := by
  induction k with
  | zero => rfl
  | succ k ih =>
    change ((addresses k).map (fun x => (x, F2.zero)) ++
      (addresses k).map (fun x => (x, F2.one)) : List (Cube k × F2)).length = _
    rw [List.length_append, List.length_map, List.length_map, ih, Nat.pow_succ, Nat.mul_two]

private theorem addressListed : ∀ {k : Nat} (x : Cube k), x ∈ addresses k
  | 0, .unit => List.Mem.head _
  | _ + 1, (x, .zero) => List.mem_append_left _ (List.mem_map.mpr ⟨x, addressListed x, rfl⟩)
  | _ + 1, (x, .one) => List.mem_append_right _ (List.mem_map.mpr ⟨x, addressListed x, rfl⟩)

/-- A constructive cardinality bound by removing one occupied address at a time. -/
private theorem countDistinct {α : Type} {xs ys : List α}
    (unique : xs.Nodup) (covered : xs ⊆ ys) : xs.length ≤ ys.length := by
  induction xs generalizing ys with
  | nil => exact Nat.zero_le _
  | cons x xs ih =>
    obtain ⟨fresh, rest⟩ := List.nodup_cons.mp unique
    obtain ⟨left, right, rfl⟩ := List.append_of_mem (covered (List.mem_cons_self (a := x) (l := xs)))
    have smaller : xs ⊆ left ++ right := by
      intro y hy
      have different : y ≠ x := fun e => fresh (e ▸ hy)
      have inAll := covered (List.mem_cons_of_mem x hy)
      simpa only [List.mem_append, List.mem_cons, different, false_or] using inAll
    have bound := ih rest smaller
    simp only [List.length_cons, List.length_append] at bound ⊢
    omega

/-- The fault-free case and each single fault have distinct readouts whenever
    one decoder recovers their labels from the algebra register alone. -/
theorem syndromeCapacity {N k : Nat} (encode : Fin (N + 1) → Cube k)
    (decode : Cube k → Fin (N + 1)) (reads : ∀ i, decode (encode i) = i) :
    N + 1 ≤ 2 ^ k := by
  have fresh : ((List.finRange (N + 1)).map encode).Nodup :=
    (List.nodup_finRange _).map encode (fun a b ne h => ne (by
      simpa only [reads] using congrArg decode h))
  have bound := countDistinct (ys := addresses k) fresh (fun {x} _ => addressListed x)
  simpa only [List.length_map, List.length_finRange, addressCount] using bound

/-- N and k are independent inputs. Exact readout plus packing and fusion force
    both dimensions. The hypotheses do not require N = 2^k − 1. -/
theorem reconstructAddressSize {N k c : Nat} {f : Cochain k}
    (unit : IsNormalized k f) (visible : NoDarkPairs f)
    (packing : IsPerfectSingleFaultPacking N c)
    (encode : Fin (N + 1) → Cube k) (decode : Cube k → Fin (N + 1))
    (reads : ∀ i, decode (encode i) = i) : k = 3 ∧ N = 7 := by
  have upper := viable_register_le_3 ⟨f, viable_of_noDark unit visible⟩
  have lower := perfectSingleFault_ge_7 packing
  have capacity := syndromeCapacity encode decode reads
  match k with
  | 0 | 1 | 2 | 3 => simp_all <;> omega
  | k + 4 => omega

/-- Positive control over all displacements and both polarities of the
    octonionic three-bit table. The input uses the kernel's Cayley–Dickson order. -/
theorem octonionPasses : NoDarkPairs (cdCochain 3) := by
  unfold NoDarkPairs bothVisible
  decide

/-- A negative control for every normalized four-bit sign table. -/
theorem fourBitCannotPass (f : Cochain 4) (unit : IsNormalized 4 f) : ¬ NoDarkPairs f :=
  fun visible => hm9_no_viable_cochain_4 f (viable_of_noDark unit visible)

/-- Label 0 represents the fault-free word. Label i+1 uses exactly the
    parity-check column of fault i from the kernel's seven-bit code. -/
def encodeHamming : Fin 8 → Cube 3 := Fin.cases (zeroCube 3) fun i =>
  let col := hammingCol7 i
  c3 col.1 col.2.1 col.2.2

def decodeHamming : Cube 3 → Fin 8
  | (((_, b₀), b₁), b₂) =>
    ⟨b₀.toNat + 2 * b₁.toNat + 4 * b₂.toNat,
      by cases b₀ <;> cases b₁ <;> cases b₂ <;> decide⟩

/-- A single model realizes all premises of reconstructAddressSize. Both
    directions of the readout bijection are checked on their actual carriers. -/
theorem hammingOctonionWitness :
    IsNormalized 3 (cdCochain 3) ∧ NoDarkPairs (cdCochain 3) ∧
    IsPerfectSingleFaultPacking 7 16 ∧
    (∀ i, decodeHamming (encodeHamming i) = i) ∧
    (∀ x, encodeHamming (decodeHamming x) = x) :=
  ⟨cdCochain_normalized 3, octonionPasses, perfectSingleFault_attained_7, by decide, by decide⟩

#print axioms visible_iff_odd
#print axioms viable_of_noDark
#print axioms syndromeCapacity
#print axioms reconstructAddressSize
#print axioms octonionPasses
#print axioms fourBitCannotPass
#print axioms hammingOctonionWitness
end ReconstructionAudit.AddressFusion
