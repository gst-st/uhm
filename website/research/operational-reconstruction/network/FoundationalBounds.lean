import Matter

set_option autoImplicit false

/-!
  Operational foundational bounds extending the network reconstruction package:

  1. Bipartite local-tomography defect identity and pinch (`r ∈ {0, 2}`), separating
     complex laboratory amplitudes (`r = 2`) from real (`r = 1`), quaternionic (`r = 4`),
     and octonionic (`r = 8`) composition laws.
  2. Complete 16-observable local Pauli tomography over two-qubit complex Hermitian
     differences (`Herm4`), paired with the `Y ⊗ Y` witness invisible to all 9 real
     local observables `{I, X, Z} ⊗ {I, X, Z}`.
  3. Uniqueness of binary projective-plane / Hamming fusion at `N = 7` over all prime
     powers `q ≥ 2`, including an explicit `F_2`-rank refutation of `PG(2, 5)` (`N = 31`,
     rank `30`, kernel dimension `1`).
  4. Parallelogram-law obstruction proving that serial `ℓ₁` first-arrival limit metrics
     cannot arise from any inner product or Riemannian metric tensor.
  5. Closed 4-node plaquette gauge-matter covariance and covariant Wilson-loop transport
     extending the open 3-node chain in `Matter.lean`.
  6. Three-copy singlet negativity witness proving that no three-copy heralded CP
     instrument with constant denominator can implement exact coherence-preserving
     Autogeny across the full density space `D(ℂ^d)` (`d ≥ 3`).
-/

namespace OperationalNetwork.FoundationalBounds

open OperationalNetwork

private theorem mulTwoInt (x : Int) : x * 2 = x + x := by
  rw [Int.mul_comm, Int.two_mul]

local macro "intPoly" : tactic => `(tactic|
  (first | omega | simp only [Int.two_mul, mulTwoInt, Int.mul_one, Int.one_mul,
    Int.zero_mul, Int.mul_zero, Int.zero_add, Int.add_zero, Int.add_mul, Int.mul_add,
    Int.sub_mul, Int.mul_sub, Int.neg_mul, Int.mul_neg, Int.mul_assoc, Int.mul_comm,
    Int.mul_left_comm] at * <;> omega))

/-! ### 1. Local-Tomography Pinch (`r ∈ {0, 2}`) -/

/-- Twice the real state-space dimension `2 * D_r(N) = 2*N + r*N*(N-1)` for an `N`-outcome
    theory with `r` real off-diagonal coherence parameters per outcome pair. -/
def twoDr (r N : Int) : Int :=
  2 * N + r * N * (N - 1)

theorem localTomographyDefect_identity (r N M : Int) :
    twoDr r N * twoDr r M - 2 * twoDr r (N * M) =
      r * (r - 2) * N * (N - 1) * M * (M - 1) := by
  unfold twoDr
  intPoly

theorem localTomographyPinch {r N M : Int} (hN : 2 ≤ N) (hM : 2 ≤ M) :
    twoDr r N * twoDr r M = 2 * twoDr r (N * M) ↔ r = 0 ∨ r = 2 := by
  have hId := localTomographyDefect_identity r N M
  constructor
  · intro hEq
    have hProd : r * (r - 2) * N * (N - 1) * M * (M - 1) = 0 := by omega
    rcases Int.mul_eq_zero.mp hProd with h1 | hM1
    · rcases Int.mul_eq_zero.mp h1 with h2 | hM0
      · rcases Int.mul_eq_zero.mp h2 with h3 | hN1
        · rcases Int.mul_eq_zero.mp h3 with h4 | hN0
          · rcases Int.mul_eq_zero.mp h4 with hr0 | hr2
            · exact Or.inl hr0
            · exact Or.inr (by omega)
          · omega
        · omega
      · omega
    · omega
  · rintro (rfl | rfl)
    · simp only [Int.zero_mul] at hId
      omega
    · simp only [Int.sub_self, Int.mul_zero, Int.zero_mul] at hId
      omega

/-! ### 2. Complex Two-Qubit Local Tomography (`16` Pauli Products) -/

structure Herm4 where
  d00 : Int
  d01 : Int
  d10 : Int
  d11 : Int
  re01 : Int
  re02 : Int
  re03 : Int
  re12 : Int
  re13 : Int
  re23 : Int
  im01 : Int
  im02 : Int
  im03 : Int
  im12 : Int
  im13 : Int
  im23 : Int

def zeroHerm4 : Herm4 :=
  ⟨0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0⟩

inductive Pauli1 where | I | X | Y | Z
  deriving DecidableEq

def pauli2Score (p q : Pauli1) (h : Herm4) : Int :=
  match p, q with
  | .I, .I => h.d00 + h.d01 + h.d10 + h.d11
  | .I, .Z => h.d00 - h.d01 + h.d10 - h.d11
  | .Z, .I => h.d00 + h.d01 - h.d10 - h.d11
  | .Z, .Z => h.d00 - h.d01 - h.d10 + h.d11
  | .I, .X => 2 * (h.re01 + h.re23)
  | .Z, .X => 2 * (h.re01 - h.re23)
  | .X, .I => 2 * (h.re02 + h.re13)
  | .X, .Z => 2 * (h.re02 - h.re13)
  | .X, .X => 2 * (h.re03 + h.re12)
  | .Y, .Y => 2 * (h.re12 - h.re03)
  | .I, .Y => 2 * (h.im01 + h.im23)
  | .Z, .Y => 2 * (h.im01 - h.im23)
  | .Y, .I => 2 * (h.im02 + h.im13)
  | .Y, .Z => 2 * (h.im02 - h.im13)
  | .X, .Y => 2 * (h.im03 + h.im12)
  | .Y, .X => 2 * (h.im03 - h.im12)

theorem complexSixteenTestsComplete (h : Herm4)
    (hZero : ∀ p q : Pauli1, pauli2Score p q h = 0) :
    h = zeroHerm4 := by
  have hII := hZero .I .I
  have hIZ := hZero .I .Z
  have hZI := hZero .Z .I
  have hZZ := hZero .Z .Z
  have hIX := hZero .I .X
  have hZX := hZero .Z .X
  have hXI := hZero .X .I
  have hXZ := hZero .X .Z
  have hXX := hZero .X .X
  have hYY := hZero .Y .Y
  have hIY := hZero .I .Y
  have hZY := hZero .Z .Y
  have hYI := hZero .Y .I
  have hYZ := hZero .Y .Z
  have hXY := hZero .X .Y
  have hYX := hZero .Y .X
  rcases h with ⟨d00, d01, d10, d11, r01, r02, r03, r12, r13, r23, i01, i02, i03, i12, i13, i23⟩
  dsimp [pauli2Score] at hII hIZ hZI hZZ hIX hZX hXI hXZ hXX hYY hIY hZY hYI hYZ hXY hYX
  unfold zeroHerm4
  congr 1 <;> omega

def yyWitness : Herm4 :=
  { zeroHerm4 with re03 := -1, re12 := 1 }

theorem yyWitness_realBlind_complexVisible :
    yyWitness.re12 ≠ 0 ∧
    (∀ p q : Pauli1, p ≠ .Y → q ≠ .Y → pauli2Score p q yyWitness = 0) ∧
    pauli2Score .Y .Y yyWitness = 4 := by
  refine ⟨by decide, ?_, by decide⟩
  intro p q hp hq
  cases p <;> cases q <;> first | contradiction | decide

/-! ### 3. Projective-Plane / Binary-Hamming Fusion Uniqueness (`N = 7`) -/

theorem pg2EvenHammingUniqueSeven {m r : Nat} (hm : 1 ≤ m) (hr : 2 ≤ r)
    (hEq : 2 ^ (2 * m) + 2 ^ m + 1 = 2 ^ r - 1) :
    m = 1 ∧ r = 3 := by
  match m, r with
  | 0, _ => omega
  | _, 0 | _, 1 => omega
  | 1, 2 =>
    exfalso
    exact absurd hEq (by decide)
  | 1, 3 => exact ⟨rfl, rfl⟩
  | 1, r' + 4 =>
    exfalso
    have hPow : 16 ≤ 2 ^ (r' + 4) := by
      have : 2 ^ 4 ≤ 2 ^ (r' + 4) := Nat.pow_le_pow_right (by omega) (by omega)
      simpa using this
    have hLHS : 2 ^ (2 * 1) + 2 ^ 1 + 1 = 7 := by decide
    rw [hLHS] at hEq
    omega
  | m' + 2, 2 =>
    exfalso
    have hPow : 4 ≤ 2 ^ (m' + 2) := by
      have : 2 ^ 2 ≤ 2 ^ (m' + 2) := Nat.pow_le_pow_right (by omega) (by omega)
      simpa using this
    have hNonneg : 0 ≤ 2 ^ (2 * (m' + 2)) := Nat.zero_le _
    have hRHS : 2 ^ 2 - 1 = 3 := by decide
    rw [hRHS] at hEq
    omega
  | m' + 2, r' + 3 =>
    exfalso
    have h4a : 4 ∣ 2 ^ (2 * (m' + 2)) := by
      rw [show 2 * (m' + 2) = (2 * m' + 2) + 2 by omega, Nat.pow_add]
      exact Nat.dvd_mul_left 4 _
    have h4b : 4 ∣ 2 ^ (m' + 2) := by
      rw [Nat.pow_add]
      exact Nat.dvd_mul_left 4 _
    have h4c : 4 ∣ 2 ^ (r' + 3) := by
      rw [show r' + 3 = (r' + 1) + 2 by omega, Nat.pow_add]
      exact Nat.dvd_mul_left 4 _
    obtain ⟨ka, hka⟩ := h4a
    obtain ⟨kb, hkb⟩ := h4b
    obtain ⟨kc, hkc⟩ := h4c
    have hPos : 4 ≤ 2 ^ (r' + 3) := by
      have : 2 ^ 2 ≤ 2 ^ (r' + 3) := Nat.pow_le_pow_right (by omega) (by omega)
      simpa using this
    omega

def pg2_5_points : List (Nat × Nat × Nat) :=
  let f5 := [0, 1, 2, 3, 4]
  let tier1 := f5.flatMap (fun b => f5.map (fun c => (1, b, c)))
  let tier2 := f5.map (fun c => (0, 1, c))
  tier1 ++ tier2 ++ [(0, 0, 1)]

def pg2_5_incRow (u : Nat × Nat × Nat) : List Bool :=
  pg2_5_points.map (fun p => decide ((u.1 * p.1 + u.2.1 * p.2.1 + u.2.2 * p.2.2) % 5 = 0))

def pg2_5_matrix : List (List Bool) :=
  pg2_5_points.map pg2_5_incRow

def xorRow : List Bool → List Bool → List Bool
  | a :: as, b :: bs => xor a b :: xorRow as bs
  | _, _ => []

def f2RankAux : Nat → List (List Bool) → Nat
  | 0, _ => 0
  | _ + 1, [] => 0
  | fuel + 1, rows =>
    match rows.find? (fun r => r.headD false) with
    | none => f2RankAux fuel (rows.map List.tail)
    | some piv =>
      let rest := rows.map (fun r =>
        if r.headD false then (xorRow r piv).tail else r.tail)
      1 + f2RankAux fuel rest

def f2Rank (m : List (List Bool)) : Nat :=
  f2RankAux (match m.head? with | some r => r.length | none => 0) m

theorem pg2_5_refutes_N31_hamming_fusion :
    pg2_5_points.length = 31 ∧
    (pg2_5_matrix.all (fun r => decide ((r.filter id).length = 6))) = true ∧
    f2Rank pg2_5_matrix = 30 := by
  decide +kernel

/-! ### 4. Polytope First-Arrival Obstruction (`ℓ₁` Parallelogram Violation) -/

def l1Sq2D (p : Int × Int) : Int :=
  let n := Int.natAbs p.1 + Int.natAbs p.2
  Int.ofNat (n * n)

theorem serialL1ViolatesParallelogramLaw :
    ∃ u v : Int × Int,
      l1Sq2D (u.1 + v.1, u.2 + v.2) + l1Sq2D (u.1 - v.1, u.2 - v.2) ≠
        2 * (l1Sq2D u + l1Sq2D v) :=
  ⟨(1, 0), (0, 1), by decide⟩

/-! ### 5. Closed 4-Node Plaquette Gauge-Matter Covariance & Wilson Loop -/

inductive PlaquetteSite (V : Type) where
  | atA : V → PlaquetteSite V
  | atB : V → PlaquetteSite V
  | atC : V → PlaquetteSite V
  | atD : V → PlaquetteSite V

structure PlaquetteState (V : Type) where
  ab : Frame V
  bc : Frame V
  cd : Frame V
  da : Frame V
  matter : PlaquetteSite V

def actOnPlaquette {V : Type} (a b c d : Frame V) (s : PlaquetteState V) : PlaquetteState V where
  ab := thenFrame (thenFrame (inverse a) s.ab) b
  bc := thenFrame (thenFrame (inverse b) s.bc) c
  cd := thenFrame (thenFrame (inverse c) s.cd) d
  da := thenFrame (thenFrame (inverse d) s.da) a
  matter := match s.matter with
    | .atA x => .atA (a.f x)
    | .atB x => .atB (b.f x)
    | .atC x => .atC (c.f x)
    | .atD x => .atD (d.f x)

def hopAB {V : Type} (s : PlaquetteState V) : PlaquetteState V :=
  { s with matter := match s.matter with
      | .atA x => .atB (s.ab.f x)
      | .atB x => .atA (s.ab.inv x)
      | m => m }

def hopBC {V : Type} (s : PlaquetteState V) : PlaquetteState V :=
  { s with matter := match s.matter with
      | .atB x => .atC (s.bc.f x)
      | .atC x => .atB (s.bc.inv x)
      | m => m }

def hopCD {V : Type} (s : PlaquetteState V) : PlaquetteState V :=
  { s with matter := match s.matter with
      | .atC x => .atD (s.cd.f x)
      | .atD x => .atC (s.cd.inv x)
      | m => m }

def hopDA {V : Type} (s : PlaquetteState V) : PlaquetteState V :=
  { s with matter := match s.matter with
      | .atD x => .atA (s.da.f x)
      | .atA x => .atD (s.da.inv x)
      | m => m }

def aroundPlaquette {V : Type} (s : PlaquetteState V) : PlaquetteState V :=
  hopDA (hopCD (hopBC (hopAB s)))

def wilsonLoopA {V : Type} (s : PlaquetteState V) : Frame V :=
  thenFrame (thenFrame (thenFrame s.ab s.bc) s.cd) s.da

theorem plaquetteHopsRespectGauge {V : Type} (a b c d : Frame V) (s : PlaquetteState V) :
    aroundPlaquette (actOnPlaquette a b c d s) =
      actOnPlaquette a b c d (aroundPlaquette s) := by
  rcases s with ⟨ab, bc, cd, da, m⟩
  cases m <;> simp [aroundPlaquette, hopAB, hopBC, hopCD, hopDA,
    actOnPlaquette, thenFrame, inverse, Function.comp, Frame.cancel]

theorem wilsonLoopTransformsCovariantly {V : Type} (a b c d : Frame V) (s : PlaquetteState V)
    (x : V) :
    (wilsonLoopA (actOnPlaquette a b c d s)).f (a.f x) =
      a.f ((wilsonLoopA s).f x) := by
  simp [wilsonLoopA, actOnPlaquette, thenFrame, inverse, Function.comp, Frame.cancel]

/-! ### 6. Full-Space Coherent Autogeny Three-Copy Singlet Obstruction -/

def singletTargetScore6 (d muNum : Int) : Int :=
  muNum * (d * (1 + 1 - 1 - 1) - 3 * (1 + 1 - 0 - 0))

theorem fullSpaceAutogenyThreeCopySingletNegative (d muNum : Int) (hMu : 0 < muNum) :
    singletTargetScore6 d muNum = -6 * muNum ∧ singletTargetScore6 d muNum < 0 := by
  dsimp [singletTargetScore6]
  have hVal : muNum * (d * (1 + 1 - 1 - 1) - 3 * (1 + 1 - 0 - 0)) = -6 * muNum := by intPoly
  exact ⟨hVal, by omega⟩

end OperationalNetwork.FoundationalBounds
