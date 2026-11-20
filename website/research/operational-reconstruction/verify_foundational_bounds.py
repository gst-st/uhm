#!/usr/bin/env python3
"""
Exact symbolic & numerical verifier for operational foundational bounds:
  1. Local-tomography defect pinch (r in {0, 2}), 3-node bilocal witness (6*sqrt(2) > 7.6605),
     and PG(2, q) binary incidence rank uniqueness at N = 7.
  2. 3D palindromic Strang split-step Weyl QCA isotropic IR Minkowski cone vs asymmetric chiral anomaly.
  3. Full-space coherence-preserving Autogeny Choi spectrum (d=2: m=3,4 fail, m=5 PSD),
     Frobenius-content balanced-partition law m_W(d) = (d-2)*d^2, and unconditional 3-copy SWAP CPTP channel.
  4. Non-abelian Q8 4-node plaquette Wilson-loop curvature invariance across all 4,096 gauge frames.
"""
import math
import numpy as np
import sympy as sp


def verify_tomography_bilocal_and_pg2q():
    r, N, M = sp.symbols("r N M", integer=True)
    D = lambda n: n + r * n * (n - 1) / 2
    defect = sp.factor(sp.expand(D(N) * D(M) - D(N * M)))
    assert defect == sp.Rational(1, 4) * r * (r - 2) * N * (N - 1) * M * (M - 1)

    X = np.array([[0, 1], [1, 0]], dtype=complex)
    Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    Z = np.array([[1, 0], [0, -1]], dtype=complex)
    psi_minus = np.array([0, 1, -1, 0], dtype=complex) / np.sqrt(2)
    rho_1234 = np.outer(np.kron(psi_minus, psi_minus), np.kron(psi_minus, psi_minus).conj())

    bell_vecs = [
        np.array([1, 0, 0, 1], dtype=complex) / np.sqrt(2),
        np.array([1, 0, 0, -1], dtype=complex) / np.sqrt(2),
        np.array([0, 1, 1, 0], dtype=complex) / np.sqrt(2),
        np.array([0, 1, -1, 0], dtype=complex) / np.sqrt(2),
    ]
    bell_labels = [(0, 0), (0, 1), (1, 0), (1, 1)]
    A_obs = {1: Z, 2: X, 3: Y}
    C_obs = {
        1: (Z + X) / np.sqrt(2),
        2: (Z - X) / np.sqrt(2),
        3: (Z + Y) / np.sqrt(2),
        4: (Z - Y) / np.sqrt(2),
        5: (X + Y) / np.sqrt(2),
        6: (X - Y) / np.sqrt(2),
    }

    def corr(x_idx, z_idx, sign_fn):
        op_B = sum(sign_fn(b0, b1) * np.outer(bv, bv.conj()) for (b0, b1), bv in zip(bell_labels, bell_vecs))
        return float(np.real(np.trace(np.kron(A_obs[x_idx], np.kron(op_B, C_obs[z_idx])) @ rho_1234)))

    s_zx = corr(1, 1, lambda b0, b1: (-1)**b0) + corr(1, 2, lambda b0, b1: (-1)**b0) \
           + corr(2, 1, lambda b0, b1: (-1)**b1) - corr(2, 2, lambda b0, b1: (-1)**b1)
    s_zy = corr(1, 3, lambda b0, b1: (-1)**b0) + corr(1, 4, lambda b0, b1: (-1)**b0) \
           - corr(3, 3, lambda b0, b1: (-1)**(b0 ^ b1)) + corr(3, 4, lambda b0, b1: (-1)**(b0 ^ b1))
    s_xy = corr(2, 5, lambda b0, b1: (-1)**b1) + corr(2, 6, lambda b0, b1: (-1)**b1) \
           - corr(3, 5, lambda b0, b1: (-1)**(b0 ^ b1)) + corr(3, 6, lambda b0, b1: (-1)**(b0 ^ b1))
    total_score = s_zx + s_zy + s_xy
    assert abs(total_score - 6 * np.sqrt(2)) < 1e-10
    assert total_score > 7.6605

    ranks = {}
    for q in [2, 3, 5, 7]:
        pts = [
            (a, b, c)
            for a in range(q) for b in range(q) for c in range(q)
            if (a, b, c) != (0, 0, 0) and next(x for x in (a, b, c) if x != 0) == 1
        ]
        n_pts = len(pts)
        mat = np.array([[(u[0]*p[0] + u[1]*p[1] + u[2]*p[2]) % q == 0 for p in pts] for u in pts], dtype=int)
        A = mat.copy() % 2
        rk = 0
        for col in range(n_pts):
            piv = next((row for row in range(rk, n_pts) if A[row, col] == 1), None)
            if piv is not None:
                A[[rk, piv]] = A[[piv, rk]]
                for row in range(n_pts):
                    if row != rk and A[row, col] == 1:
                        A[row] ^= A[rk]
                rk += 1
        ranks[q] = (n_pts, rk, n_pts - rk)
    assert ranks == {2: (7, 4, 3), 3: (13, 12, 1), 5: (31, 30, 1), 7: (57, 56, 1)}


def verify_weyl_qca_cone():
    kx, ky, kz, eps = sp.symbols("kx ky kz eps", real=True)
    I2 = sp.eye(2)
    sx = sp.Matrix([[0, 1], [1, 0]])
    sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    sz = sp.Matrix([[1, 0], [0, -1]])

    Ux = sp.cos(kx) * I2 - sp.I * sp.sin(kx) * sx
    Uy = sp.cos(ky) * I2 - sp.I * sp.sin(ky) * sy
    Uz = sp.cos(kz) * I2 - sp.I * sp.sin(kz) * sz
    ht_xyz = sp.trigsimp(sp.trace(Ux * Uy * Uz) / 2)

    Ux2 = sp.cos(kx / 2) * I2 - sp.I * sp.sin(kx / 2) * sx
    Uy2 = sp.cos(ky / 2) * I2 - sp.I * sp.sin(ky / 2) * sy
    ht_strang = sp.trigsimp(sp.trace(Ux2 * Uy2 * Uz * Uy2 * Ux2) / 2)
    assert sp.trigsimp(ht_strang - sp.cos(kx) * sp.cos(ky) * sp.cos(kz)) == 0

    u_xyz = sp.series(1 - ht_xyz.subs({kx: eps*kx, ky: eps*ky, kz: eps*kz}), eps, 0, 5).removeO()
    w2_xyz = sp.expand(sp.series(2 * u_xyz + sp.Rational(2, 3) * u_xyz**2, eps, 0, 5).removeO())
    u_str = sp.series(1 - ht_strang.subs({kx: eps*kx, ky: eps*ky, kz: eps*kz}), eps, 0, 5).removeO()
    w2_str = sp.expand(sp.series(2 * u_str + sp.Rational(2, 3) * u_str**2, eps, 0, 5).removeO())

    quartic = sp.Rational(1, 12) * eps**4 * (kx**4 + ky**4 + kz**4 - 2*(kx**2*ky**2 + ky**2*kz**2 + kz**2*kx**2))
    assert sp.expand(w2_xyz - (eps**2 * (kx**2 + ky**2 + kz**2) + 2*eps**3*kx*ky*kz + quartic)) == 0
    assert sp.expand(w2_str - (eps**2 * (kx**2 + ky**2 + kz**2) + quartic)) == 0


def verify_coherent_autogeny_and_swap():
    d, mu = 2, 0.5
    s0 = np.array([[1.0, 0.0], [0.0, 0.0]])
    E_arr = np.zeros((4, 2, 2))
    for idx in range(4):
        E_arr[idx, idx // 2, idx % 2] = 1.0

    def choi_min_eig_d2(m, H_fn):
        num_configs = 4 ** m
        codes = np.zeros((num_configs, m), dtype=int)
        tmp = np.arange(num_configs)
        for k in range(m - 1, -1, -1):
            codes[:, k] = tmp % 4
            tmp //= 4
        A_all = E_arr[codes]
        acc = np.zeros((num_configs, 2, 2), dtype=float)
        for mask in range(1, 1 << m):
            bits = np.array([(mask >> k) & 1 for k in range(m)], dtype=float)
            sign = -1.0 if ((m - int(bits.sum())) % 2 == 1) else 1.0
            M = np.einsum("k,nkij->nij", bits, A_all)
            tr1 = M[:, 0, 0] + M[:, 1, 1]
            tr2 = np.einsum("nij,nji->n", M, M)
            z = M[:, 0, 0]
            F = ((1 - mu) * d * tr2 + mu * tr1**2)[:, None, None] * M + (mu * (d * tr2 - tr1**2) * tr1)[:, None, None] * s0[None, :, :]
            acc += sign * (H_fn(tr1, tr2, z)[:, None, None] * F)
        acc /= math.factorial(m)
        powers = 2 ** np.arange(m - 1, -1, -1)
        idx1 = (codes // 2) @ powers
        idx2 = (codes % 2) @ powers
        J = np.zeros((2**m * 2, 2**m * 2), dtype=float)
        for r_idx in range(2):
            for c_idx in range(2):
                J[idx1 * 2 + r_idx, idx2 * 2 + c_idx] = acc[:, r_idx, c_idx]
        return float(np.linalg.eigvalsh(J).min())

    assert choi_min_eig_d2(3, lambda t1, t2, z: np.ones_like(t1)) < -0.8
    assert choi_min_eig_d2(4, lambda t1, t2, z: t1) < -0.24
    assert choi_min_eig_d2(5, lambda t1, t2, z: t1**2) > -1e-12

    for d_val in range(3, 8):
        t = d_val - 1
        m_star = (d_val - 2) * d_val * d_val
        for m, should_pass in [(m_star - 1, False), (m_star, True)]:
            q, rem = divmod(m, t)
            lam = [q + 1] * rem + [q] * (t - rem)
            csum = sum((j - i) for i, row in enumerate(lam) for j in range(row))
            eig = d_val * csum / (m * (m - 1) / 2) - 1.0
            assert (eig >= -1e-12) == should_pass

    d7 = 7
    rng = np.random.default_rng(123)
    G = rng.normal(size=(d7, d7)) + 1j * rng.normal(size=(d7, d7))
    rho = G @ G.conj().T
    rho /= np.trace(rho)
    P_pur = float(np.real(np.trace(rho @ rho)))
    Theta7 = np.zeros((d7, d7), dtype=complex); Theta7[0, 0] = 1.0
    S12 = np.zeros((d7 * d7, d7 * d7), dtype=complex)
    for i in range(d7):
        for j in range(d7):
            S12[i * d7 + j, j * d7 + i] = 1.0
    rho2 = np.kron(rho, rho)
    out = np.trace(0.5 * (np.eye(d7 * d7) + S12) @ rho2) * rho + np.trace(0.5 * (np.eye(d7 * d7) - S12) @ rho2) * Theta7
    assert np.allclose(out, 0.5 * (1 + P_pur) * rho + 0.5 * (1 - P_pur) * Theta7)


def verify_q8_plaquette():
    I2 = np.eye(2, dtype=complex)
    ix = 1j * np.array([[0, 1], [1, 0]], dtype=complex)
    iy = 1j * np.array([[0, -1j], [1j, 0]], dtype=complex)
    iz = 1j * np.array([[1, 0], [0, -1]], dtype=complex)
    Q8 = [I2, -I2, ix, -ix, iy, -iy, iz, -iz]
    flat_links = (ix, iy, -iy, -ix)
    vortex_links = (ix, iy, -ix, -iy)
    for ga in Q8:
        for gb in Q8:
            for gc in Q8:
                for gd in Q8:
                    for links, target_tr in [(flat_links, 2.0), (vortex_links, -2.0)]:
                        ab, bc, cd, da = links
                        W = (ga.conj().T @ ab @ gb) @ (gb.conj().T @ bc @ gc) @ (gc.conj().T @ cd @ gd) @ (gd.conj().T @ da @ ga)
                        assert abs(np.trace(W) - target_tr) < 1e-12


if __name__ == "__main__":
    verify_tomography_bilocal_and_pg2q()
    verify_weyl_qca_cone()
    verify_coherent_autogeny_and_swap()
    verify_q8_plaquette()
    print("verify_foundational_bounds: all 4 suites passed.")
