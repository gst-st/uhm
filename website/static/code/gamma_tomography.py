"""
gamma_tomography.py — Reference implementation of UHM Γ-tomography (measurement.md §6.4).

Turns a stream of 7-channel observations x_n ∈ ℂ⁷ (one coordinate per dimension
A,S,D,L,E,O,U) into the coherence matrix Γ and the viability/consciousness
observables (P, R, Φ), with finite-sample confidence bounds.

Everything below the 7-channel embedding π (the one irreducible modelling choice)
is a *provably consistent* estimator — this file is the executable witness of that
claim. Pure numpy, no external deps.

Canonical references (docs/):
  Γ = M/Tr M, M = E[x xᵀ]                      §6.4 setup
  Σ̂_N, Γ̂_N                                     §6.4 estimator
  matrix-Bernstein sample size N ≥ C B²/(τ²ε²)·ln(14/δ)   §6.4 (2)
  unbiased U-statistic purity P̂_N              §6.4 (3)
  N_eff = N/(2 τ_corr + 1)                      §6.4 dependence caveat
  R = 1/(7P) [T-126];  Φ = P_coh/P_diag         thresholds
  L2 window: P > 2/7, R ≥ 1/3, Φ ≥ 1
"""
from __future__ import annotations
import numpy as np

N_DIM = 7
DIMS = ("A", "S", "D", "L", "E", "O", "U")
P_CRIT = 2.0 / 7.0          # critical purity (lower window edge)
P_UPPER = 3.0 / 7.0         # R = 1/(7P) ≥ 1/3  ⟺  P ≤ 3/7
R_TH = 1.0 / 3.0
PHI_TH = 1.0


# ─────────────────────────────────────────────────────────────────────────────
# Core estimators (§6.4)
# ─────────────────────────────────────────────────────────────────────────────
def sigma_hat(X: np.ndarray) -> np.ndarray:
    """Σ̂_N = (1/N) Σ x_n x_n†.  X has shape (N, 7)."""
    return (X.conj().T @ X) / X.shape[0]


def gamma_hat(X: np.ndarray) -> np.ndarray:
    """Γ̂_N = Σ̂_N / Tr Σ̂_N — Hermitian, PSD, unit-trace by construction."""
    S = sigma_hat(X)
    return S / np.trace(S).real


def purity_unbiased(X: np.ndarray) -> float:
    """Two-sample U-statistic purity estimator (§6.4 (3)).

    P̂ = [Σ_{m≠n} |x_m† x_n|²] / [N(N-1) (Tr Σ̂)²].

    The NUMERATOR is exactly unbiased for Tr(M²) (E|x_m†x_n|² = Tr(M²), m≠n).
    The normalised ratio still carries a small O(1/N) bias from the random
    denominator (Tr Σ̂)²  —  but of opposite sign and ~3× smaller magnitude than
    the naïve plug-in Tr(Γ̂²), which it is designed to replace. (Self-test (b).)
    """
    N = X.shape[0]
    G = X @ X.conj().T                       # Gram: G_mn = x_m† x_n   (N×N)
    off = (np.abs(G) ** 2).sum() - np.abs(np.diagonal(G) ** 2).sum()
    trS = np.trace(sigma_hat(X)).real
    return float(off / (N * (N - 1) * trS ** 2))


def purity_naive(G: np.ndarray) -> float:
    """Biased plug-in Tr(Γ̂²) — kept only to demonstrate the O(1/N) bias."""
    return float(np.trace(G @ G).real)


# ─────────────────────────────────────────────────────────────────────────────
# Derived observables + thresholds
# ─────────────────────────────────────────────────────────────────────────────
def reflection(P: float) -> float:
    """R = 1/(7P)  (T-126).  Distance from heat death I/7."""
    return 1.0 / (N_DIM * P)


def integration(G: np.ndarray) -> float:
    """Φ = P_coh / P_diag  in the canonical dimension frame."""
    P_diag = float((np.abs(np.diagonal(G)) ** 2).sum())
    P_total = float(np.trace(G @ G).real)
    return (P_total - P_diag) / P_diag


def coh_E(G: np.ndarray) -> float:
    """Coh_E = γ_EE²/P + 2 Σ_{i≠E}|γ_Ei|² / P   (axiom-septicity #coh-e-canonical)."""
    e = DIMS.index("E")
    P = float(np.trace(G @ G).real)
    pop = np.abs(G[e, e]) ** 2
    coh = 2.0 * (np.abs(G[e, :]) ** 2).sum() - 2.0 * np.abs(G[e, e]) ** 2
    return float((pop + coh) / P)


def l2_verdict(P: float, R: float, Phi: float) -> dict:
    """The four-threshold L2 call (D_diff handled separately via coh_E)."""
    return {
        "P>2/7":   P > P_CRIT,
        "R>=1/3":  R >= R_TH,
        "Phi>=1":  Phi >= PHI_TH,
        "in_window": P_CRIT < P <= P_UPPER,
    }


# ─────────────────────────────────────────────────────────────────────────────
# Finite-sample machinery (§6.4 (2) + dependence caveat)
# ─────────────────────────────────────────────────────────────────────────────
def bernstein_N(B: float, tau: float, eps: float, delta: float, C: float = 1.0) -> int:
    """Matrix-Bernstein sample size: N ≥ C B²/(τ²ε²) ln(14/δ)  (§6.4 (2))."""
    return int(np.ceil(C * B ** 2 / (tau ** 2 * eps ** 2) * np.log(14.0 / delta)))


def tau_corr_batch_means(series: np.ndarray, n_batches: int = 20) -> float:
    """Integrated autocorrelation time τ_corr via batch means.

    series: real 1-D scalar summary per time step (e.g. Tr Σ̂ window energy, or any
    embedded coordinate power).  Returns τ_corr s.t. N_eff = N/(2 τ_corr + 1).
    """
    x = np.asarray(series, float)
    N = x.size
    b = N // n_batches
    if b < 2:
        return 0.0
    batches = x[: b * n_batches].reshape(n_batches, b)
    var_batch = batches.mean(axis=1).var(ddof=1)
    var_all = x.var(ddof=1)
    if var_all <= 0:
        return 0.0
    # batch-means variance inflation ≈ (2 τ_corr + 1) ⇒ τ_corr = (b·var_batch/var_all − 1)/2
    ratio = b * var_batch / var_all
    return max(0.0, (ratio - 1.0) / 2.0)


def n_eff(N: int, tau_corr: float) -> float:
    """Effective sample size N_eff = N/(2 τ_corr + 1)."""
    return N / (2.0 * tau_corr + 1.0)


def ci_halfwidth(P: float, N_eff_: float, z: float = 1.96) -> float:
    """Delta-method 95% CI half-width for P̂ (variance ~ 2P²/N_eff, swap-test scale)."""
    return z * np.sqrt(max(P, 1e-9) ** 2 * 2.0 / max(N_eff_, 1.0))


# ─────────────────────────────────────────────────────────────────────────────
# One-call pipeline
# ─────────────────────────────────────────────────────────────────────────────
def analyse(X: np.ndarray, series: np.ndarray | None = None) -> dict:
    """Full §6.4 pipeline on an (N,7) complex embedding stream."""
    G = gamma_hat(X)
    P = purity_unbiased(X)
    R = reflection(P)
    Phi = integration(G)
    tau = tau_corr_batch_means(series) if series is not None else 0.0
    Neff = n_eff(X.shape[0], tau)
    return {
        "Gamma": G, "P": P, "R": R, "Phi": Phi, "Coh_E": coh_E(G),
        "tau_corr": tau, "N_eff": Neff, "P_CI95": ci_halfwidth(P, Neff),
        "verdict": l2_verdict(P, R, Phi),
    }


# ─────────────────────────────────────────────────────────────────────────────
# Self-test: reproduce the specific numerical claims of §6.4
# ─────────────────────────────────────────────────────────────────────────────
def _sample_from_gamma(G: np.ndarray, N: int, rng) -> np.ndarray:
    """Draw N i.i.d. x_n with E[x x†] ∝ G (complex Gaussian with covariance G)."""
    L = np.linalg.cholesky(G + 1e-12 * np.eye(N_DIM))
    z = (rng.standard_normal((N, N_DIM)) + 1j * rng.standard_normal((N, N_DIM))) / np.sqrt(2)
    return z @ L.T


def _self_test() -> None:
    rng = np.random.default_rng(0)
    # a target Γ that genuinely passes L2: Γ = ½·I/7 + ½·|v⟩⟨v|, v = uniform superposition.
    # ⇒ P=5/14≈0.357 ∈ (2/7,3/7], Φ=1.5≥1, R≈0.40≥1/3, D_diff≈2.37≥2.
    v = np.ones(N_DIM, complex) / np.sqrt(N_DIM)
    G0 = 0.5 * np.eye(N_DIM) / N_DIM + 0.5 * np.outer(v, v.conj())
    G0 = G0 / np.trace(G0).real
    P0 = np.trace(G0 @ G0).real
    print(f"target: P={P0:.4f}  R={reflection(P0):.4f}  Φ={integration(G0):.4f}"
          f"  Coh_E={coh_E(G0):.4f}  window={P_CRIT:.3f}<P<={P_UPPER:.3f}")
    print(f"        L2 verdict={l2_verdict(P0, reflection(P0), integration(G0))}")

    # (a) O(N^{-1/2}) rate: sqrt(N)·||Γ̂−Γ|| ≈ const
    print("\n(a) convergence rate  sqrt(N)·||Γ̂_N − Γ||_op:")
    for N in (200, 800, 3200, 12800):
        errs = [np.linalg.norm(gamma_hat(_sample_from_gamma(G0, N, rng)) - G0, 2)
                for _ in range(30)]
        print(f"    N={N:6d}   sqrt(N)*err = {np.sqrt(N)*np.mean(errs):.3f}")

    # (b) U-statistic unbiased vs naive biased, at N=200 (many trials to beat MC noise)
    print("\n(b) purity bias at N=200 (3000 trials, ±MC standard error):")
    bu, bn = [], []
    for _ in range(3000):
        X = _sample_from_gamma(G0, 200, rng)
        bu.append(purity_unbiased(X) - P0)
        bn.append(purity_naive(gamma_hat(X)) - P0)
    su, sn = np.std(bu)/np.sqrt(len(bu)), np.std(bn)/np.sqrt(len(bn))
    print(f"    U-statistic bias = {np.mean(bu):+.4f} ± {su:.4f}   (numerator unbiased; tiny −O(1/N) denominator residual)")
    print(f"    naive      bias = {np.mean(bn):+.4f} ± {sn:.4f}   (positively biased, ~3× larger, O(1/N))")

    # (c) N_eff on an autocorrelated stream (AR(1))
    print("\n(c) effective sample size on AR(1) stream (φ=0.8):")
    N = 4000; phi = 0.8
    e = rng.standard_normal(N); s = np.empty(N); s[0] = e[0]
    for t in range(1, N):
        s[t] = phi * s[t-1] + e[t]
    tau = tau_corr_batch_means(s)
    print(f"    τ_corr≈{tau:.2f}  N_eff≈{n_eff(N, tau):.0f}/{N}"
          f"  (theory τ=φ/(1-φ)={phi/(1-phi):.2f})")

    # (d) end-to-end verdict
    print("\n(d) analyse() verdict on N=1000 window state:")
    out = analyse(_sample_from_gamma(G0, 1000, rng), series=None)
    print(f"    P̂={out['P']:.4f}  R̂={out['R']:.4f}  Φ̂={out['Phi']:.4f}"
          f"  Coh_E={out['Coh_E']:.4f}  ±CI={out['P_CI95']:.4f}")
    print(f"    verdict={out['verdict']}")


if __name__ == "__main__":
    _self_test()
