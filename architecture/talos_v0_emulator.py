#!/usr/bin/env python3
"""
TALOS V0 Reference Emulator — verified executable kernel for D(C^7).

Implements the exact mathematical primitives specified in the TALOS architecture
paper (architecture/main.tex):
  1. Canonical Singer cyclic Fano plane PG(2,2) on [A, S, D, L, E, U, O] (0..6):
       LINES = (0,1,3), (1,2,4), (2,3,5), (3,4,6), (4,5,0), (5,6,1), (6,0,2).
  2. Binary coding duality over F_2:
       - 7x7 Fano incidence matrix M (rank 4) generates the Hamming [7,4,3] code.
       - 3x7 parity-check matrix H (rank 3, rows = 3 independent weight-4 line
         complements spanning the dual simplex code [7,3,4]) satisfies H M^T = 0
         (mod 2) and uniquely decodes all 7 single-sector fault syndromes.
  3. Genuine Fano pinching channel P_Fano(rho) = (1/3) sum_l Pi_l rho Pi_l and
     Fano Lindblad dissipator D_Fano[rho] = gamma * (P_Fano(rho) - rho):
       - preserves all diagonal populations,
       - attenuates every off-diagonal by 1/3 (exact Phi contraction 1/9),
       - decays off-diagonals at uniform rate 2*gamma/3 (D_Fano = (2/3) D_atom),
       - covariant under discrete PSL(2,7) collineations and U(1)^7 diagonal phases
         (NOT under continuous G_2 rotations of the basis).
  4. Canonical nonlinear anchored self-model
       phi_J(rho) = (1 - R(rho)) * P_Fano(rho) + R(rho) * |psi><psi|,
     explicitly distinguished from linear relaxation toward a fixed target.
  5. Exact canonical observables:
       P = Tr(rho^2), P_diag = sum(diag(rho)^2), Phi = (P - P_diag) / P_diag,
       R = 1 / (7*P), C = Phi * R,
       Coh_E = (rho[4,4]^2 + 2 * sum_{j!=4} |rho[4,j]|^2) / P,
       D_diff_7D = 1 + 6 * Coh_E,
       S_bits = -Tr(rho log2 rho) <= log2(7) ~ 2.807355 bits.
  6. Strang-split CPTP tick + optional depolarizing thermalization for power-port
     severance experiments + vectorized SIMT ecology batch.

Honest scope: this V0 CPU emulator verifies logical correctness, invariants,
syndromes, and thermodynamic bit accounting. It does NOT achieve physical
Landauer energy bounds (digital CMOS moves data and dissipates switching power),
and the dynamics are BQP-bounded (no complexity-class speed-up).

Dependencies: numpy only.
Run: PYTHONDONTWRITEBYTECODE=1 python3 -B architecture/talos_v0_emulator.py
"""
import math
import numpy as np

# ----------------------------------------------------------------- constants
N = 7
MODES = ("A", "S", "D", "L", "E", "U", "O")
A, S_, D_, L, E, U, O = range(N)

# Canonical Singer cyclic Fano lines {k, k+1, k+3} mod 7 on [A,S,D,L,E,U,O]
LINES = (
    (0, 1, 3),  # {A, S, L}
    (1, 2, 4),  # {S, D, E}
    (2, 3, 5),  # {D, L, U}
    (3, 4, 6),  # {L, E, O}
    (4, 5, 0),  # {E, U, A}
    (5, 6, 1),  # {U, O, S}
    (6, 0, 2),  # {O, A, D}
)

I7 = np.eye(N, dtype=complex) / N
LOG2_7 = math.log2(N)
LN2 = math.log(2.0)
KB = 1.380649e-23
T_ROOM = 300.0
LANDAUER_BIT_J = KB * T_ROOM * LN2
LANDAUER_MAX_STATE_J = KB * T_ROOM * math.log(N)  # k_B T ln 7 = log2(7) * k_B T ln 2

# Rank-3 Fano line projectors Pi_l = sum_{k in l} |k><k|
LINE_PROJECTORS = tuple(
    np.diag([1.0 if idx in line else 0.0 for idx in range(N)]).astype(complex)
    for line in LINES
)

# Canonical collineation-invariant equal-superposition anchor |psi><psi|
PSI_UNIFORM = np.ones(N, dtype=complex) / math.sqrt(N)
ANCHOR_UNIFORM = np.outer(PSI_UNIFORM, PSI_UNIFORM.conj())

# Non-degenerate diagonal effective Hamiltonian (commutes with diagonal populations)
H_DEFAULT = np.diag([0.0, 0.4, 0.8, 1.2, 2.0, 1.5, 1.7]).astype(complex)


# ----------------------------------------------------------- Fano & Hamming code
def fano_incidence_matrix():
    """7x7 binary incidence matrix M over F_2 (rank 4): generates Hamming [7,4,3]."""
    M = np.zeros((N, N), dtype=int)
    for row, line in enumerate(LINES):
        for col in line:
            M[row, col] = 1
    return M


def hamming_parity_check_matrix():
    """3x7 binary parity-check matrix H over F_2 (rank 3) dual to Singer Fano M.

    Rows are the weight-4 complements of the first three non-concurrent lines
    (L_0, L_1, L_2), spanning the dual simplex code [7,3,4]. Satisfies
    H @ M.T = 0 (mod 2), and its 7 columns are the 7 distinct nonzero vectors
    of F_2^3.
    """
    M = fano_incidence_matrix()
    complements = 1 - M
    return complements[:3].copy()


M_FANO = fano_incidence_matrix()
H_PARITY = hamming_parity_check_matrix()
SYNDROME_TO_SECTOR = {
    tuple(int(b) for b in H_PARITY[:, j]): j for j in range(N)
}


def gf2_rank(mat):
    """Exact matrix rank over F_2 via Gaussian elimination."""
    A_mat = (np.array(mat, dtype=int) % 2).copy()
    rows, cols = A_mat.shape
    rk = 0
    for c in range(cols):
        piv = None
        for r in range(rk, rows):
            if A_mat[r, c] == 1:
                piv = r
                break
        if piv is None:
            continue
        A_mat[[rk, piv]] = A_mat[[piv, rk]]
        for r in range(rows):
            if r != rk and A_mat[r, c] == 1:
                A_mat[r] ^= A_mat[rk]
        rk += 1
    return rk


def mediator(i, j):
    """Unique third sector k*(i, j) completing the Fano line through (i, j)."""
    if i == j:
        raise ValueError("Mediator requires two distinct sectors.")
    for line in LINES:
        if i in line and j in line:
            return next(k for k in line if k != i and k != j)
    raise RuntimeError("Invalid Fano incidence.")


def hamming_syndrome(word_bits):
    """3-bit Hamming [7,4,3] syndrome s = H @ word (mod 2)."""
    vec = np.asarray(word_bits, dtype=int) % 2
    if vec.shape != (N,):
        raise ValueError(f"Expected length-{N} binary vector, got {vec.shape}.")
    return tuple(int(b) for b in (H_PARITY @ vec) % 2)


def decode_single_fault(syndrome_bits):
    """Map a 3-bit syndrome tuple to None (no fault) or sector index 0..6."""
    s = tuple(int(b) % 2 for b in syndrome_bits)
    if s == (0, 0, 0):
        return None
    return SYNDROME_TO_SECTOR[s]


def sector_fault_syndrome(rho, threshold=1e-3):
    """Diagnose single-sector coherence loss via Fano line activity + H projection.

    If sector j is completely decoupled (all off-diagonals in row/col j below
    threshold), the 3 lines containing j drop their j-coherences; flagging any
    sector whose incident off-diagonal norm falls below threshold produces a
    binary sector-fault indicator vector e_j whose 3-bit syndrome H e_j uniquely
    identifies j.
    """
    fault_indicator = np.zeros(N, dtype=int)
    for j in range(N):
        off_norm = math.sqrt(
            sum(abs(rho[j, k]) ** 2 for k in range(N) if k != j)
        )
        if off_norm < threshold:
            fault_indicator[j] = 1
    return hamming_syndrome(fault_indicator), fault_indicator


# ----------------------------------------------------------- linear algebra utils
def expm_hermitian_unitary(H, dt):
    """Exact unitary U = exp(-i * H * dt) via Hermitian eigendecomposition."""
    H_herm = 0.5 * (H + H.conj().T)
    w, V = np.linalg.eigh(H_herm)
    return (V * np.exp(-1j * w * dt)) @ V.conj().T


def project_psd(rho):
    """Project onto nearest physical density matrix: Hermitian, PSD, trace 1."""
    rho_h = 0.5 * (rho + rho.conj().T)
    w, V = np.linalg.eigh(rho_h)
    w = np.clip(w, 0.0, None)
    tr = float(np.sum(w))
    if tr <= 0.0:
        return I7.copy()
    return (V * (w / tr)) @ V.conj().T


def check_invariants(rho, tol=1e-9):
    """Assert Hermiticity, unit trace, and positive-semidefiniteness."""
    assert np.allclose(rho, rho.conj().T, atol=tol), "Not Hermitian"
    assert abs(np.trace(rho).real - 1.0) < tol, f"Trace != 1: {np.trace(rho)}"
    assert abs(np.trace(rho).imag) < tol, f"Imaginary trace: {np.trace(rho)}"
    min_eig = float(np.min(np.linalg.eigvalsh(0.5 * (rho + rho.conj().T))))
    assert min_eig > -tol, f"Not PSD: min eigenvalue = {min_eig}"
    return True


# ----------------------------------------------------- canonical observables
def purity(rho):
    """Purity P = Tr(rho^2) in [1/7, 1]."""
    return float(np.real(np.trace(rho @ rho)))


def diagonal_purity(rho):
    """Diagonal purity P_diag = sum_k rho_{kk}^2 in [1/7, 1]."""
    d = np.real(np.diag(rho))
    return float(np.sum(d * d))


def integration_phi(rho):
    """Exact canonical integration Phi = (P - P_diag) / P_diag.

    Reduces to Phi = 7*P - 1 ONLY when diag(rho) = (1/7, ..., 1/7).
    """
    P = purity(rho)
    P_d = diagonal_purity(rho)
    return float((P - P_d) / P_d)


def reflection_r(rho):
    """Canonical reflection score R = 1 / (7*P). Note R >= 1/3 <=> P <= 3/7."""
    return float(1.0 / (N * purity(rho)))


def coh_e(rho):
    """Canonical E-mode coherence: (rho[E,E]^2 + 2 * sum_{j!=E} |rho[E,j]|^2) / P."""
    P = purity(rho)
    diag_e = float(np.real(rho[E, E]))
    off_e = float(sum(abs(rho[E, j]) ** 2 for j in range(N) if j != E))
    return float((diag_e * diag_e + 2.0 * off_e) / P)


def d_diff_7d(rho):
    """Canonical 7D differentiation observable D_diff_7D = 1 + 6 * Coh_E."""
    return float(1.0 + 6.0 * coh_e(rho))


def entropy_bits(rho):
    """Exact von Neumann entropy S(rho) = -Tr(rho log2 rho) in bits (<= log2 7)."""
    w = np.linalg.eigvalsh(0.5 * (rho + rho.conj().T))
    w = w[w > 1e-15]
    return float(-np.sum(w * np.log2(w)))


def observables(rho):
    """Compute the full canonical observable suite for one holon state."""
    P = purity(rho)
    P_d = diagonal_purity(rho)
    Phi = (P - P_d) / P_d
    R = 1.0 / (N * P)
    C = Phi * R
    ce = coh_e(rho)
    D_diff = 1.0 + 6.0 * ce
    S_b = entropy_bits(rho)
    viable = (P > 2.0 / 7.0) and (R >= 1.0 / 3.0) and (Phi >= 1.0) and (D_diff >= 2.0)
    return {
        "P": P,
        "P_diag": P_d,
        "Phi": Phi,
        "R": R,
        "C": C,
        "Coh_E": ce,
        "D_diff_7D": D_diff,
        "S_bits": S_b,
        "viable_full": viable,
    }


# ----------------------------------------- Fano pinching, dissipator, self-model
def fano_pinch(rho):
    """Genuine Fano pinching channel P_Fano(rho) = (1/3) sum_{l=0}^6 Pi_l rho Pi_l.

    Preserves all diagonal populations and multiplies every off-diagonal element
    by exactly 1/3, contracting Phi by exactly 1/9 for every rho in D(C^7).
    """
    out = np.zeros_like(rho, dtype=complex)
    for Pi in LINE_PROJECTORS:
        out += Pi @ rho @ Pi
    return out / 3.0


def fano_dissipator(rho, gamma=1.0):
    """Fano Lindblad dissipator D_Fano[rho] = gamma * (P_Fano(rho) - rho).

    Preserves all populations (diag = 0) and decays every off-diagonal coherence
    at uniform rate 2*gamma/3: D_Fano = (2/3) * gamma * (diag(rho) - rho).
    """
    return gamma * (fano_pinch(rho) - rho)


def depolarizing_dissipator(rho, gamma_dep=0.2):
    """Optional isotropic depolarizing channel gamma_dep * (I/7 - rho).

    Used when modeling full thermalization to I/7 upon power-port severance.
    """
    return gamma_dep * (I7 - rho)


def phi_J(rho, anchor=ANCHOR_UNIFORM):
    """Canonical nonlinear anchored self-model:
        phi_J(rho) = (1 - R(rho)) * P_Fano(rho) + R(rho) * |psi><psi|,
    where R(rho) = 1 / (7 * P(rho)).
    """
    R = reflection_r(rho)
    return (1.0 - R) * fano_pinch(rho) + R * anchor


def regeneration_anchored(rho, kappa=12.0, anchor=ANCHOR_UNIFORM):
    """Nonlinear anchored regeneration R_phiJ[rho] = kappa * (phi_J(rho) - rho)."""
    return kappa * (phi_J(rho, anchor=anchor) - rho)


def regeneration_linear(rho, rho_target, kappa=1.0):
    """Linear relaxation toward a static target R_lin[rho] = kappa * (rho_target - rho).

    Provided explicitly to contrast linear relaxation with canonical nonlinear phi_J.
    """
    return kappa * (rho_target - rho)


# ------------------------------------------------------------- Strang-split tick
def tick(
    rho,
    dt=0.005,
    gamma_fano=1.0,
    kappa=12.0,
    gamma_dep=0.0,
    H=H_DEFAULT,
    anchor=ANCHOR_UNIFORM,
    mode="anchored",
    rho_target=None,
):
    """Advance one holon state by one CPTP-safe Strang-split tick.

    mode="anchored" uses canonical nonlinear phi_J(rho);
    mode="linear" uses linear relaxation toward static rho_target.
    Returns (rho_next, syndrome_bits).
    """
    U_half = expm_hermitian_unitary(H, 0.5 * dt)
    rho1 = U_half @ rho @ U_half.conj().T

    syn, _ = sector_fault_syndrome(rho1)

    d_rho = fano_dissipator(rho1, gamma=gamma_fano)
    if gamma_dep > 0.0:
        d_rho = d_rho + depolarizing_dissipator(rho1, gamma_dep=gamma_dep)
    if kappa > 0.0:
        if mode == "anchored":
            d_rho = d_rho + regeneration_anchored(rho1, kappa=kappa, anchor=anchor)
        elif mode == "linear":
            if rho_target is None:
                raise ValueError("rho_target required when mode='linear'.")
            d_rho = d_rho + regeneration_linear(rho1, rho_target=rho_target, kappa=kappa)
        else:
            raise ValueError(f"Unknown regeneration mode: {mode}")

    rho2 = project_psd(rho1 + dt * d_rho)
    rho3 = U_half @ rho2 @ U_half.conj().T
    return project_psd(rho3), syn


def tick_batch_simt(batch, dt=0.005, gamma_fano=1.0, kappa=12.0, H=H_DEFAULT, anchor=ANCHOR_UNIFORM):
    """Vectorized SIMT tick over a batch of shape (B, 7, 7) using exact P_Fano & phi_J."""
    U_half = expm_hermitian_unitary(H, 0.5 * dt)
    U_dag = U_half.conj().T

    # Unitary half-step
    b1 = np.einsum("ij,bjk,kl->bil", U_half, batch, U_dag)

    # Exact Fano pinching: diagonal preserved, off-diagonals scaled by 1/3
    eye_mask = np.eye(N, dtype=bool)
    p_fano = b1 / 3.0
    p_fano[:, eye_mask] = b1[:, eye_mask]

    # Exact purity & R(rho) = 1/(7*P)
    P_vec = np.real(np.einsum("bij,bji->b", b1, b1))
    R_vec = 1.0 / (N * P_vec)

    # Canonical phi_J(rho)
    phi_j_batch = (1.0 - R_vec)[:, None, None] * p_fano + R_vec[:, None, None] * anchor[None, :, :]

    # D_Fano + R_phiJ step
    b2 = b1 + dt * (gamma_fano * (p_fano - b1) + kappa * (phi_j_batch - b1))

    # Second unitary half-step + vectorized PSD projection
    b3 = np.einsum("ij,bjk,kl->bil", U_half, b2, U_dag)
    b3 = 0.5 * (b3 + np.swapaxes(b3.conj(), -1, -2))
    w, V = np.linalg.eigh(b3)
    w = np.clip(w, 0.0, None)
    w /= np.sum(w, axis=-1, keepdims=True)
    return np.einsum("bij,bj,bkj->bik", V, w, V.conj())


# ------------------------------------------------------------ random state helper
def random_density_matrix(rng, rank=N):
    """Sample a general complex density matrix with non-uniform diagonal."""
    X = rng.standard_normal((N, rank)) + 1j * rng.standard_normal((N, rank))
    rho = X @ X.conj().T
    return rho / float(np.trace(rho).real)


# --------------------------------------------------------------- verification suite
def run_self_tests():
    rng = np.random.default_rng(2026)

    # [1] Canonical Singer cyclic Fano plane & Hamming [7,4,3] duality
    assert len(LINES) == 7
    for idx in range(N):
        incident = [line for line in LINES if idx in line]
        assert len(incident) == 3, f"Mode {MODES[idx]} not on 3 lines"
    for i in range(N):
        for j in range(i + 1, N):
            common = [line for line in LINES if i in line and j in line]
            assert len(common) == 1, f"Pair ({i},{j}) not on unique line"
            k = mediator(i, j)
            assert {i, j, k} == set(common[0])

    assert gf2_rank(M_FANO) == 4, "Fano incidence matrix M must have F_2-rank 4"
    assert gf2_rank(H_PARITY) == 3, "Parity-check matrix H must have F_2-rank 3"
    assert np.all((H_PARITY @ M_FANO.T) % 2 == 0), "H M^T != 0 (mod 2)"

    # Enumerate all 16 codewords generated by M_FANO (Hamming [7,4,3])
    codewords = set()
    for mask in range(1 << 7):
        v = np.array([(mask >> b) & 1 for b in range(7)], dtype=int)
        c = tuple(int(x) for x in (v @ M_FANO) % 2)
        codewords.add(c)
    assert len(codewords) == 16, f"Expected 16 Hamming codewords, got {len(codewords)}"
    for c in codewords:
        assert hamming_syndrome(c) == (0, 0, 0), f"Codeword {c} has nonzero syndrome"
        wt = sum(c)
        assert wt in (0, 3, 4, 7), f"Unexpected codeword weight {wt}"
    assert min(sum(c) for c in codewords if sum(c) > 0) == 3

    # Verify all 7 single-bit error syndromes are distinct, nonzero, and uniquely decode
    seen_syndromes = set()
    for j in range(N):
        err = np.zeros(N, dtype=int)
        err[j] = 1
        syn = hamming_syndrome(err)
        assert syn != (0, 0, 0) and syn not in seen_syndromes
        seen_syndromes.add(syn)
        assert decode_single_fault(syn) == j
    assert len(seen_syndromes) == 7

    # Also verify single-sector coherence decoupling diagnosis on density matrices
    rho_healthy = 0.5 * I7 + 0.5 * ANCHOR_UNIFORM
    syn_ok, _ = sector_fault_syndrome(rho_healthy)
    assert decode_single_fault(syn_ok) is None
    for j in range(N):
        rho_bad = rho_healthy.copy()
        for k in range(N):
            if k != j:
                rho_bad[j, k] = 0.0
                rho_bad[k, j] = 0.0
        syn_bad, _ = sector_fault_syndrome(rho_bad)
        assert decode_single_fault(syn_bad) == j

    print("[1] Canonical Singer Fano & Hamming [7,4,3] duality (M rank 4, H rank 3, H M^T=0): PASS")
    print("    Single-sector syndrome map:", {MODES[j]: "".join(map(str, H_PARITY[:, j])) for j in range(N)})

    # [2] Genuine Fano pinching & Fano Lindblad dissipator + PSL(2,7)xU(1)^7 covariance
    for _ in range(10):
        rho = random_density_matrix(rng)
        pf = fano_pinch(rho)
        check_invariants(pf)
        assert np.allclose(np.diag(pf), np.diag(rho), atol=1e-13)
        off_mask = ~np.eye(N, dtype=bool)
        assert np.allclose(pf[off_mask], rho[off_mask] / 3.0, atol=1e-13)
        assert abs(integration_phi(pf) - integration_phi(rho) / 9.0) < 1e-12

        # Verify three equivalent forms of D_Fano[rho]
        d1 = fano_dissipator(rho, gamma=1.5)
        d2 = 1.5 * (2.0 / 3.0) * (np.diag(np.diag(rho)) - rho)
        d3 = np.zeros_like(rho)
        for Pi in LINE_PROJECTORS:
            comm1 = Pi @ rho - rho @ Pi
            comm2 = Pi @ comm1 - comm1 @ Pi
            d3 += -(1.5 / 6.0) * comm2
        assert np.allclose(d1, d2, atol=1e-13)
        assert np.allclose(d1, d3, atol=1e-13)
        assert np.allclose(np.diag(d1), 0.0, atol=1e-13)

    # Verify discrete PSL(2,7) collineations (Singer shift k->k+1, Frobenius k->2k)
    # + U(1)^7 diagonal phase covariance of P_Fano and D_Fano
    rho_test = random_density_matrix(rng)
    for perm in ([(k + 1) % N for k in range(N)], [(2 * k) % N for k in range(N)]):
        # Verify perm is a genuine collineation preserving the Singer line set
        line_set = {frozenset(line) for line in LINES}
        assert {frozenset(perm[i] for i in line) for line in LINES} == line_set
        P_perm = np.zeros((N, N), dtype=complex)
        for col_i, row_i in enumerate(perm):
            P_perm[row_i, col_i] = 1.0
        phases = np.diag(np.exp(1j * rng.uniform(0, 2 * math.pi, size=N)))
        V_sym = phases @ P_perm
        lhs = fano_pinch(V_sym @ rho_test @ V_sym.conj().T)
        rhs = V_sym @ fano_pinch(rho_test) @ V_sym.conj().T
        assert np.allclose(lhs, rhs, atol=1e-13)

    # Verify continuous G_2 = Aut(O) rotations do NOT preserve P_Fano or Phi:
    # construct an explicit g_2 derivation from the Singer octonionic 3-form phi_ijk
    phi3 = np.zeros((N, N, N), dtype=float)
    for i, j, k in LINES:
        for a, b, c in ((i, j, k), (j, k, i), (k, i, j)):
            phi3[a, b, c] = 1.0
            phi3[b, a, c] = -1.0
    so7_basis = []
    for a in range(N):
        for b in range(a + 1, N):
            T = np.zeros((N, N), dtype=float)
            T[a, b], T[b, a] = 1.0, -1.0
            so7_basis.append(T)
    dphi_cols = [
        (
            np.einsum("il,ljk->ijk", T, phi3)
            + np.einsum("jl,ilk->ijk", T, phi3)
            + np.einsum("kl,ijl->ijk", T, phi3)
        ).reshape(-1)
        for T in so7_basis
    ]
    _, sv_g2, Vt_g2 = np.linalg.svd(np.array(dphi_cols).T)
    g2_null = Vt_g2[np.sum(sv_g2 > 1e-9):]
    assert g2_null.shape[0] == 14
    X_g2 = sum(c * T for c, T in zip(g2_null[0], so7_basis))
    U_g2 = expm_hermitian_unitary(1j * X_g2, 0.35)
    assert np.allclose(U_g2 @ U_g2.conj().T, np.eye(N), atol=1e-12)
    assert np.linalg.norm(
        fano_pinch(U_g2 @ rho_test @ U_g2.conj().T) - U_g2 @ fano_pinch(rho_test) @ U_g2.conj().T
    ) > 1e-2

    print("[2] Genuine P_Fano (Phi -> Phi/9) & D_Fano (rate 2g/3, pop-preserving, PSL(2,7)xU(1)^7, non-G2): PASS")

    # [3] Exact canonical observables on uniform AND non-uniform diagonal states
    # Non-uniform diagonal test: pure state with unequal amplitudes
    psi_nonunif = np.array([0.65, 0.45, 0.35, 0.30, 0.25, 0.22, 0.2539685], dtype=complex)
    psi_nonunif /= np.linalg.norm(psi_nonunif)
    rho_nu = 0.65 * np.outer(psi_nonunif, psi_nonunif.conj()) + 0.35 * np.diag(
        [0.40, 0.15, 0.12, 0.10, 0.09, 0.08, 0.06]
    )
    rho_nu /= float(np.trace(rho_nu).real)
    ob_nu = observables(rho_nu)
    phi_wrong = 7.0 * ob_nu["P"] - 1.0
    assert abs(ob_nu["Phi"] - phi_wrong) > 0.2, "Non-uniform state must separate exact Phi from 7P-1"
    assert abs(ob_nu["Phi"] - (ob_nu["P"] - ob_nu["P_diag"]) / ob_nu["P_diag"]) < 1e-13

    # Uniform diagonal test: Phi == 7*P - 1 holds EXACTLY
    rho_u = 0.5 * I7 + 0.5 * ANCHOR_UNIFORM
    ob_u = observables(rho_u)
    assert abs(ob_u["P"] - 5.0 / 14.0) < 1e-13
    assert abs(ob_u["Phi"] - (7.0 * ob_u["P"] - 1.0)) < 1e-13
    assert abs(ob_u["Phi"] - 1.5) < 1e-13
    assert abs(ob_u["R"] - 0.4) < 1e-13
    assert abs(ob_u["C"] - 0.6) < 1e-13
    assert ob_u["viable_full"] is True

    # Diagonal-only state with P in (2/7, 3/7]: must FAIL full viability (Phi=0, Coh_E != enough)
    rho_diag_only = np.diag([0.5] + [1.0 / 12.0] * 6).astype(complex)
    ob_do = observables(rho_diag_only)
    assert abs(ob_do["P"] - 7.0 / 24.0) < 1e-13
    assert abs(ob_do["Phi"] - 0.0) < 1e-13
    assert abs((7.0 * ob_do["P"] - 1.0) - 25.0 / 24.0) < 1e-13  # 7P-1 falsely says > 1!
    assert ob_do["viable_full"] is False

    # Check R >= 1/3 <=> P <= 3/7 across random states
    for _ in range(30):
        r_s = random_density_matrix(rng)
        ob_s = observables(r_s)
        assert (ob_s["R"] >= 1.0 / 3.0 - 1e-12) == (ob_s["P"] <= 3.0 / 7.0 + 1e-12)
        assert 0.0 <= ob_s["S_bits"] <= LOG2_7 + 1e-12

    # Exact von Neumann entropy bounds in bits
    assert abs(entropy_bits(I7) - LOG2_7) < 1e-13
    assert abs(entropy_bits(ANCHOR_UNIFORM) - 0.0) < 1e-13

    print(
        f"[3] Exact observables (non-uniform Phi={ob_nu['Phi']:.4f} vs 7P-1={phi_wrong:.4f}; "
        f"S_max={entropy_bits(I7):.6f} bits = log2(7)): PASS"
    )

    # [4] Canonical nonlinear phi_J fixed point, dynamical attractor, unitary check, & power-port severance
    # Exact analytic fixed point of phi_J: rho* = 0.5*I/7 + 0.5*|psi><psi|
    assert np.allclose(phi_J(rho_u), rho_u, atol=1e-13), "rho_u must be exact fixed point of phi_J"

    # Distinguish nonlinear phi_J from linear static-target relaxation
    rho_lin_a = random_density_matrix(rng)
    rho_lin_b = random_density_matrix(rng)
    mid = 0.5 * (rho_lin_a + rho_lin_b)
    nonlin_gap = np.linalg.norm(phi_J(mid) - 0.5 * (phi_J(rho_lin_a) + phi_J(rho_lin_b)))
    assert nonlin_gap > 1e-3, "phi_J must be genuinely nonlinear in rho"

    # Converge to viable attractor under canonical anchored tick (H=0 + diagonal H test)
    rho_dyn = random_density_matrix(rng)
    for _ in range(600):
        rho_dyn, _ = tick(rho_dyn, dt=0.005, gamma_fano=1.0, kappa=12.0, H=np.zeros((N, N), complex))
    check_invariants(rho_dyn)
    ob_dyn = observables(rho_dyn)
    assert ob_dyn["viable_full"] is True, f"Anchored attractor failed viability: {ob_dyn}"

    # Verify unitary half-step preserves spectrum, purity, and entropy to machine precision
    U_step = expm_hermitian_unitary(H_DEFAULT, 0.05)
    rho_u0 = random_density_matrix(rng)
    rho_u1 = U_step @ rho_u0 @ U_step.conj().T
    dP_u = abs(purity(rho_u1) - purity(rho_u0))
    dS_u = abs(entropy_bits(rho_u1) - entropy_bits(rho_u0))
    assert dP_u < 1e-13 and dS_u < 1e-13

    # Power-port severance test (kappa=0, depolarizing rate d=0.4): exact analytical exit time
    d_dep = 0.4
    rho_cut = rho_dyn.copy()
    P0_cut = purity(rho_cut)
    t_off_analytic = math.log((P0_cut - 1.0 / 7.0) / (2.0 / 7.0 - 1.0 / 7.0)) / (2.0 * d_dep)
    dt_cut = 0.002
    t_cross = None
    for step in range(1, 3000):
        rho_cut, _ = tick(rho_cut, dt=dt_cut, gamma_fano=0.0, kappa=0.0, gamma_dep=d_dep, H=H_DEFAULT)
        if t_cross is None and purity(rho_cut) <= 2.0 / 7.0:
            t_cross = step * dt_cut
    assert t_cross is not None and abs(t_cross - t_off_analytic) < 0.01
    assert abs(purity(rho_cut) - 1.0 / 7.0) < 1e-2

    print(
        f"[4] Canonical phi_J attractor (P={ob_dyn['P']:.4f}, R={ob_dyn['R']:.4f}, "
        f"Phi={ob_dyn['Phi']:.4f}, Coh_E={ob_dyn['Coh_E']:.4f}, D_diff={ob_dyn['D_diff_7D']:.4f}) "
        f"& severance (t_off={t_cross:.3f} vs analytic {t_off_analytic:.3f}): PASS"
    )

    # [5] Thermodynamics in bits: unitary dS=0, Fano dissipator dS/dt > 0, frequency-independent rate
    rates = []
    for dt_probe in (0.02, 0.005, 0.001):
        rho_after = project_psd(rho_dyn + dt_probe * fano_dissipator(rho_dyn, gamma=1.0))
        sdot_bits = (entropy_bits(rho_after) - entropy_bits(rho_dyn)) / dt_probe
        assert sdot_bits > 0.0
        rates.append(sdot_bits)
    assert abs(rates[-1] - rates[-2]) / rates[-1] < 0.02, f"Rate not dt-independent: {rates}"
    P_meta_W = LANDAUER_BIT_J * rates[-1]
    print(
        f"[5] Thermodynamics in bits: dS_unitary={dS_u:.1e}, "
        f"Sdot_Fano={rates[-1]:.4f} bits/tau (dt-independent), "
        f"P_meta_floor={P_meta_W:.3e} W*tau, max state floor kT ln 7={LANDAUER_MAX_STATE_J:.3e} J: PASS"
    )

    # [6] Vectorized SIMT ecology batch (N_ecol = 1000 holons)
    N_ecol = 1000
    batch = np.stack([random_density_matrix(rng) for _ in range(N_ecol)], axis=0)
    for _ in range(80):
        batch = tick_batch_simt(batch, dt=0.005, gamma_fano=1.0, kappa=12.0, H=np.zeros((N, N), complex))
    # Verify invariants on sample and mean purity in viable window
    for idx in (0, N_ecol // 2, N_ecol - 1):
        check_invariants(batch[idx])
    mean_P = float(np.mean([purity(batch[i]) for i in range(N_ecol)]))
    assert 2.0 / 7.0 < mean_P <= 3.0 / 7.0
    footprint_mb = (N_ecol * 784) / 1e6
    print(
        f"[6] Vectorized SIMT ecology ({N_ecol} holons, {footprint_mb:.3f} MB): "
        f"mean P={mean_P:.4f} in (2/7, 3/7]: PASS"
    )
    print("\nALL TALOS V0 SELF-TESTS PASSED.")


if __name__ == "__main__":
    run_self_tests()
