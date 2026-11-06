"""Conditional UHM moment estimation; see measurement.md section 6.4.

By default analyse() reports descriptive statistics, without confidence claims.
An optional Bernstein region requires independent observations of a fixed
embedding, a declared population bound ||x||^2 <= B, and positive population
trace. Observed norms can falsify that bound, but cannot establish it.

Same-sample centering targets normalized covariance and makes residuals
dependent. No iid region is attached to those residuals. The former heuristic
CI, energy-based effective sample size and universal debiasing claims are
withdrawn. Embedding semantics and clinical interpretations require independent
validation; positive semidefiniteness and the model thresholds do not supply it.
"""
from __future__ import annotations

import math
import numpy as np

N_DIM = 7
DIMS = ("A", "S", "D", "L", "E", "O", "U")
P_CRIT = 2.0 / 7.0
P_UPPER = 3.0 / 7.0
R_TH = 1.0 / 3.0
PHI_TH = 1.0


def _samples(X: np.ndarray, minimum: int = 1) -> np.ndarray:
    X = np.asarray(X, dtype=np.complex128)
    if X.ndim != 2 or X.shape[1] != N_DIM or X.shape[0] < minimum:
        raise ValueError(f"Expected at least {minimum} observations with {N_DIM} channels")
    if not np.isfinite(X).all():
        raise ValueError("Observations must be finite")
    return X


def sigma_hat(X: np.ndarray) -> np.ndarray:
    """Mean of x x-dagger, with one observation x per ROW of X."""
    X = _samples(X)
    # X.conj().T @ X would conjugate the intended matrix for complex channels.
    return (X.T @ X.conj()) / X.shape[0]


def gamma_hat(X: np.ndarray) -> np.ndarray:
    """Normalized second moment; undefined at zero observed trace."""
    S = sigma_hat(X)
    trace = float(np.trace(S).real)
    if not math.isfinite(trace) or trace <= 0:
        raise ValueError("A finite positive observed trace is required")
    return S / trace


def purity_pair_ratio(X: np.ndarray) -> float:
    """Off-diagonal pair statistic divided by the estimated trace squared.

    The pair average in the NUMERATOR is unbiased for Tr(M^2) only for iid
    embedded observations. The ratio is not generally unbiased and its bias
    has no universal sign. Same-sample centering also removes the numerator's
    iid guarantee. Values outside [1/7, 1] are not clamped or treated as the
    purity of the constructed density matrix.
    """
    X = _samples(X, minimum=2)
    count = X.shape[0]
    trace = float(np.trace(sigma_hat(X)).real)
    if not math.isfinite(trace) or trace <= 0:
        raise ValueError("A finite positive observed trace is required")
    X = X / math.sqrt(trace)
    # Direct off-diagonal accumulation avoids an N-by-N Gram allocation and
    # cancellation against the diagonal.
    off = 0.0
    for i in range(count - 1):
        dots = X[i + 1:] @ X[i].conj()
        off += 2.0 * float(np.vdot(dots, dots).real)
    return off / (count * (count - 1))


def purity_plugin(G: np.ndarray) -> float:
    """Tr(G^2) of the constructed Hermitian state; no unbiasedness claim."""
    return float(np.trace(G @ G).real)


def reflection(P: float) -> float:
    """Model functional R=1/(7P), not a clinical assessment."""
    return 1.0 / (N_DIM * P)


def integration(G: np.ndarray) -> float:
    """Model functional Phi=P_coh/P_diag in the declared channel basis."""
    diagonal = float((np.abs(np.diagonal(G)) ** 2).sum())
    return (purity_plugin(G) - diagonal) / diagonal


def coh_E(G: np.ndarray) -> float:
    e = DIMS.index("E")
    population = np.abs(G[e, e]) ** 2
    coherence = 2.0 * ((np.abs(G[e, :]) ** 2).sum() - population)
    return float((population + coherence) / purity_plugin(G))


def model_thresholds(P: float, R: float, Phi: float) -> dict:
    """Point comparisons inside the model, not real-world classifications."""
    return {
        "P>2/7": P > P_CRIT,
        "R>=1/3": R >= R_TH,
        "Phi>=1": Phi >= PHI_TH,
        "purity_in_model_window": P_CRIT < P <= P_UPPER,
    }


def _bound_parameters(B: float, delta: float) -> None:
    if not math.isfinite(B) or B <= 0:
        raise ValueError("B must be a finite positive population norm-squared bound")
    if not math.isfinite(delta) or not 0 < delta < 1:
        raise ValueError("delta must lie strictly between zero and one")


def bernstein_N(B: float, tau_lower: float, eps: float, delta: float) -> int:
    """Sufficient iid budget for normalized operator error <= eps.

    Premises: ||x||^2 <= B almost surely, Tr(M) >= tau_lower > 0.
    Set t=tau_lower*eps/(d+1). The normalization bound and v^2 <= B^2
    give N >= log(2d/delta)*(2B^2+(4B/3)t)/t^2.
    tau_lower is a population premise, not the empirical trace. The budget
    is not necessary and does not describe quantum Chernoff discrimination.
    """
    _bound_parameters(B, delta)
    if not math.isfinite(tau_lower) or not 0 < tau_lower <= B:
        raise ValueError("Require 0 < population trace lower bound <= B")
    if not math.isfinite(eps) or not 0 < eps <= 1:
        raise ValueError("eps must lie in (0, 1]")
    t = tau_lower * eps / (N_DIM + 1)
    if t == 0:
        raise ValueError("Requested precision is below floating-point range")
    ratio = B / t
    need = (math.log(2 * N_DIM) - math.log(delta)) * (2 * ratio * ratio + 4 * ratio / 3)
    if not math.isfinite(need):
        raise ValueError("Sample budget exceeds floating-point range")
    return math.ceil(math.nextafter(need, math.inf))


def iid_confidence_region(X: np.ndarray, B: float, delta: float = 0.05) -> dict:
    """Conditional finite-sample region for a fixed iid embedding.

    Independence and the population bound are caller-supplied premises.
    The region concerns the population normalized SECOND MOMENT and its
    purity, not the pair ratio. No diary/estimated-baseline coverage claim.
    Floating-point evaluation is not an interval-arithmetic proof certificate.
    """
    X = _samples(X)
    _bound_parameters(B, delta)
    if np.any(np.sum(np.abs(X) ** 2, axis=1) > B):
        raise ValueError("An observed norm violates the declared population bound")
    trace = float(np.trace(sigma_hat(X)).real)
    L = math.log(2 * N_DIM) - math.log(delta)
    a = B * (2 * L / (3 * X.shape[0]))
    # Positive root of N*t^2 = L*(2B^2+(4B/3)t).
    t = a + math.hypot(a, B * math.sqrt(2 * L / X.shape[0]))
    if not math.isfinite(t):
        raise ValueError("Confidence radius exceeds floating-point range")
    trace_lower = max(0.0, trace - N_DIM * t)
    if trace == 0:
        # Cover the whole target space rather than invent a matrix center or
        # silently condition coverage on having returned an estimate.
        return {
            "confidence_level": 1.0 - delta,
            "assumptions": "fixed iid embedding; population norm bound B; Tr(M)>0",
            "moment_operator_radius": t,
            "population_trace_lower": 0.0,
            "gamma_operator_radius": None,
            "purity_interval": (1.0 / N_DIM, 1.0),
            "state_available": False,
        }
    G = gamma_hat(X)
    radius = (min(1.0, (N_DIM + 1) * t / trace_lower)
              if trace_lower > 0 else 1.0)
    P = purity_plugin(G)
    return {
        "confidence_level": 1.0 - delta,
        "assumptions": "fixed iid embedding; population norm bound B; Tr(M)>0",
        "moment_operator_radius": t,
        "population_trace_lower": trace_lower,
        "gamma_operator_radius": radius,
        "purity_interval": (max(1.0 / N_DIM, P - 2 * radius),
                            min(1.0, P + 2 * radius)),
        "state_available": True,
    }


def analyse(X: np.ndarray, *, center: bool = False,
            iid_norm2_bound: float | None = None, delta: float = 0.05) -> dict:
    """Descriptive statistics; a confidence region is explicitly opt-in.

    center=True uses this sample's mean and targets normalized covariance.
    It cannot request the fixed-iid region. Already centered/dependent inputs
    likewise do not satisfy that contract, even if the flag is omitted.
    Constant centered data raise ValueError: no normalized covariance exists.
    """
    X = _samples(X)
    if center and iid_norm2_bound is not None:
        raise ValueError("Same-sample centering is outside the fixed-iid confidence contract")
    if center:
        X = X - X.mean(axis=0)
    G = gamma_hat(X)
    P = purity_plugin(G)
    R = reflection(P)
    Phi = integration(G)
    return {
        "target": "normalized_covariance" if center else "normalized_second_moment",
        "Gamma": G,
        "P_plugin": P,
        "P_pair_ratio": purity_pair_ratio(X) if len(X) >= 2 else None,
        "R_plugin": R,
        "Phi_plugin": Phi,
        "Coh_E_plugin": coh_E(G),
        "model_thresholds": model_thresholds(P, R, Phi),
        "confidence": (iid_confidence_region(X, iid_norm2_bound, delta)
                       if iid_norm2_bound is not None else None),
    }


def _self_test() -> None:
    # Deterministic regression witness, not a coverage simulation or proof.
    ratings = np.vstack((np.eye(N_DIM), np.eye(N_DIM))) + 2
    out = analyse(ratings, center=True)
    shifted = analyse(ratings + 5, center=True)
    assert np.allclose(out["Gamma"], shifted["Gamma"])
    assert np.isclose(out["P_plugin"], 1 / 6)
    assert np.isclose(out["P_pair_ratio"], 4 / 39)
    assert out["confidence"] is None
    print("Same-sample centering: P_plugin=1/6, P_pair_ratio=4/39; no automatic CI.")
    print("Regression checks: scripts/verify_measurement_tomography.py")


if __name__ == "__main__":
    _self_test()
