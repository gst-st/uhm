#!/usr/bin/env python3
"""Toy model: neutral Wright-Fisher already sits at a=1 (natural gradient).

The claim, in three lines of algebra and one simulation:

  1. A population of M individuals over d types, resampled multinomially each
     generation (neutral Wright-Fisher), has per-generation increment noise
         Cov(dp) = (diag p - p p^T) / M            -- exactly.
  2. The matrix diag p - p p^T is the INVERSE of the Fisher-Rao metric on the
     simplex (restricted to the tangent space sum dx = 0).
  3. Hence kappa^{upup} = (1/M) g^{-1}: Vanchurin's own a=1 criterion
     (arXiv:2603.15198, Eq. 7.5), holding identically, with 1/M as the sole
     rate constant. Nothing is chosen and nothing is fitted; the exponent is
     computed from the noise mechanism.

  Discriminator (same source, the a=1/2 degeneracy of Eq. 7.5): a=1/2 predicts
  a SPHERICAL kappa^{upup} on the tangent space; multinomial resampling
  predicts the fully anisotropic diag p - p p^T. One simulated covariance
  decides.

No seven dimensions, no Fano plane, no UHM anywhere in this file.

Run: python3 wf_toy_a1.py     (numpy only, deterministic seed)
"""

import numpy as np

rng = np.random.default_rng(20260809)

d, M, T = 3, 100_000, 5_000
p0 = np.array([0.6, 0.3, 0.1])

# --- simulate neutral Wright-Fisher ---------------------------------------
p = p0.copy()
inc = np.empty((T, d))          # increments dp_t
theo = np.zeros((d, d))         # pooled conditional covariance, theory
for t in range(T):
    counts = rng.multinomial(M, p)
    q = counts / M
    inc[t] = q - p
    theo += (np.diag(p) - np.outer(p, p)) / M
    p = q
theo /= T
emp = inc.T @ inc / T           # pooled empirical second moment (mean is 0)

# --- 1. shape identity: emp vs (diag p - p p^T)/M --------------------------
rel = np.linalg.norm(emp - theo) / np.linalg.norm(theo)
print(f"d={d}  M={M}  T={T}  final p = {np.round(p, 4)}")
print(f"[1] ||Cov_emp - (diag p - p p^T)/M||_F / ||.||_F = {rel:.4f}")

# --- 2. the pointwise a=1 identity, on a quasi-static window ----------------
# kappa(p) = (1/M) g^{-1}(p) is a POINTWISE claim; the pooled check above is
# its path integral. Here it is read off directly: the first 500 generations
# drift by sigma ~ sqrt(500 * 0.25 / M) ~ 0.035, so p is nearly p0, and the
# window covariance must equal the inverse Fisher metric at p0, divided by M.
Pi = np.eye(d) - np.ones((d, d)) / d
T0 = 500
emp0 = inc[:T0].T @ inc[:T0] / T0
g_inv_p0 = np.diag(p0) - np.outer(p0, p0)     # pinv of Pi diag(1/p0) Pi on T
rel_a1 = np.linalg.norm(M * emp0 - g_inv_p0) / np.linalg.norm(g_inv_p0)
print(f"[2] quasi-static window (T0={T0}): ||M*kappa - g^(-1)(p0)||/||g^(-1)|| "
      f"= {rel_a1:.4f}   (a=1, rate constant 1/M)")
mean_step = np.abs(inc.mean(axis=0)).max()
sigma_step = np.sqrt(0.25 / M)
print(f"[2b] centred noise: max |mean increment| = {mean_step:.2e} "
      f"= {mean_step / sigma_step:.3f} of one step's sigma (his Eq. 7.4 is centred)")

# --- 3. the discriminator: spherical (a=1/2) vs multinomial (a=1) ----------
# Eigenvalues of the projected covariance: a=1/2 says equal; a=1 says the
# spectrum of diag p - p p^T.
ev_emp = np.sort(np.linalg.eigvalsh(Pi @ emp @ Pi))[1:]   # drop the zero mode
ev_theo = np.sort(np.linalg.eigvalsh(Pi @ theo @ Pi))[1:]
ratio_emp = ev_emp[-1] / ev_emp[0]
ratio_theo = ev_theo[-1] / ev_theo[0]
print(f"[3] tangent eigenvalue ratio: empirical {ratio_emp:.3f}, "
      f"multinomial theory {ratio_theo:.3f}, spherical (a=1/2) 1.000")

# Mauchly sphericity statistic against chi^2 with df = d(d-1)/2 + d/... for
# the 2x2 tangent block: df = 2. Whitened by the spherical null.
A = Pi @ emp @ Pi
tr = np.trace(A) / (d - 1)
lam = np.linalg.eigvalsh(A)[1:]
W = np.prod(lam) / (np.mean(lam) ** (d - 1))
T_stat = -(T - 1) * np.log(W)
print(f"[4] Mauchly T against sphericity = {T_stat:.1f}  "
      f"(chi^2_2 5% critical = 5.99; a=1/2 rejected iff T >> 6)")

# --- 4. his Eq. 4.7 as a bonus: the static covariance has the same shape ---
# The single-draw static covariance at p is diag p - p p^T -- the SAME matrix
# as M*kappa. Measured on the same window: one shape, one scalar (1/M) apart.
static0 = np.diag(p0) - np.outer(p0, p0)
rel_c = np.linalg.norm(M * emp0 - static0) / np.linalg.norm(static0)
print(f"[5] ||M*kappa - c_static(p0)||/||c_static|| = {rel_c:.4f} "
      f"(dynamic noise = static covariance / M)")
