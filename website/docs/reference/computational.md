---
slug: /reference/computational
sidebar_position: 5
title: Computational Implementation
description: State-preserving reference model, diagnostic predicates and computational limits
---

# Computational Implementation

This page specifies an executable NumPy reference model. It implements a **chosen** seven-dimensional state evolution and its diagnostics. It does not reconstruct a biological state from uncalibrated features, certify experience, or implement every categorical construction. The earlier Verum listings mixed an unfinished API with mathematical guarantees; a Verum port must reproduce these specified maps and pass its own compiler and numerical checks. See the [implementation status](/docs/applied/coherence-cybernetics/implementation#быстрый-старт).

## Computational complexity of UHM operations

For a dense $N\times N$ Hermitian state, $P=\sum_{ij}|\gamma_{ij}|^2$ costs $O(N^2)$, as do $\Phi$, $R=1/(NP)$ and row-mask coherence. Entropy and generic matrix diagonalization cost $O(N^3)$ in the standard dense arithmetic model. A dense unitary conjugation costs $O(N^3)$; the selected uniform dephasing and frozen replacement maps cost $O(N^2)$. A general Kraus family of size $M$ costs $O(MN^3)$ without exploitable structure. Entropy of a lifted experiential readout uses the dimension of that lift, not automatically seven.

Fixed $N=7$ makes these costs independent of a variable matrix dimension; it gives no universal wall-clock time or problem-complexity bound. Report hardware, precision, batch size and benchmarks before quoting runtimes. A general $k$-partite state has $7^{2k}-1$ real parameters; factorized storage is cheap only under a stated factorization or controlled approximation.

## Holon type

The state contract is Hermitian, PSD and trace one. The chosen dynamics is

$$
\dot\Gamma=-i[H,\Gamma]-\gamma\operatorname{offdiag}\Gamma+a(\Gamma)(\varphi(\Gamma)-\Gamma),\qquad a=\kappa g_V(P),\quad g_V=\operatorname{clamp}(7P-2,0,1).
$$

Here $H$, $\gamma\ge0$, a nonnegative rate model and a state-valued self-model are inputs [D/P]. The threshold and gate are [choices](/docs/reference/mathematical-kernel#thresholds), not uniquely forced by Landauer or category theory. Rates have reciprocal physical-time units; $H$ is expressed in frequency units (or divided by $\hbar$).

For the specified two-state kinetic cycle, $J=ac/(a+b+c)$ is exact for its steady flux [T under the model]; choosing those rates and identifying $J$ with a regenerative coefficient is [D/H]. The product $ac/b$ is an approximation only when $b>0$ and $(a+c)/b\ll1$, with relative overestimate $(a+c)/b$. The code takes physical rates directly and does not infer them from matrix amplitudes. Positive bootstrap $\omega_0/7$ is a selected rate, not a universal categorical constant.

## State-preserving reference code {#reference-code}

The following complete listing requires NumPy only. The validator reports an error for residuals above a stated tolerance; it does not project an invalid update back into a state. Tiny residual eigenvalues are clipped only when evaluating entropy or a matrix square root, so these numerical results carry the reported tolerance. No eigenvalue cutoff silently discards positive entropy contributions.

```python
import numpy as np

N, E = 7, 4
I7 = np.eye(N, dtype=complex) / N
TOL = 1e-10


def density(g, n=None):
    g = np.asarray(g, dtype=complex)
    if g.ndim != 2 or g.shape[0] != g.shape[1]:
        raise ValueError("square matrix required")
    if n is not None and g.shape != (n, n):
        raise ValueError("wrong state dimension")
    if not np.isfinite(g).all():
        raise ValueError("finite entries required")
    if np.linalg.norm(g - g.conj().T, 'fro') > TOL:
        raise ValueError("Hermiticity residual exceeds tolerance")
    if abs(np.trace(g) - 1) > TOL:
        raise ValueError("trace residual exceeds tolerance")
    if np.linalg.eigvalsh(g).min() < -TOL:
        raise ValueError("negative eigenvalue exceeds tolerance")
    return g


def entropy(g):
    ev = np.linalg.eigvalsh(density(g))
    ev = np.maximum(ev, 0)  # only residual negatives accepted above
    pos = ev[ev > 0]
    return float(-np.sum(pos * np.log(pos)))


def metrics(g, rho_e=None):
    g = density(g, N)
    diag = np.real(np.diag(g))
    d = float(np.sum(diag**2))
    off = g - np.diag(np.diag(g))
    q = float(np.sum(np.abs(off)**2))
    p = d + q
    # rho_e = g is a selected readout [D], not a partial trace of E.
    readout = g if rho_e is None else density(rho_e)
    r, phi, diff = 1 / (N * p), q / d, np.exp(entropy(readout))
    coh_e = (diag[E]**2 + 2 * np.sum(np.abs(off[E])**2)) / p
    stress = np.clip(1 - N * diag, 0, 1)  # selected score [D]
    cap2 = p > 2/N and r >= 1/3 and phi >= 1 and diff >= 2
    return dict(P=p, R=r, Phi=phi, D_diff=float(diff),
                Coh_E=float(coh_e), C=phi*r, Cap2=bool(cap2),
                full_window=bool(cap2 and np.max(stress) < 1),
                margins=(p-2/N, r-1/3, phi-1, diff-2),
                stress=stress)


def kinetic_flux(a, b, c):
    # Chosen two-state cycle: flux J=ac/(a+b+c), rates in 1/time.
    rates = np.array([a, b, c], dtype=float)
    if not np.isfinite(rates).all() or np.any(rates < 0):
        raise ValueError("finite nonnegative physical rates required")
    scale = float(np.max(rates))
    if scale == 0:
        return 0.0
    aa, bb, cc = rates / scale
    return float(scale * aa * cc / (aa + bb + cc))


def chosen_phi(g, anchor):
    g, anchor = density(g, N), density(anchor, N)
    r = metrics(g)['R']
    fano = np.diag(np.diag(g)) + (g-np.diag(np.diag(g))) / 3
    return density((1-r)*fano + r*anchor, N)


def split_step(g, hamiltonian, dt, dephasing_rate, rate_model, phi):
    # Freeze all feedback at the SAME input state, then compose subflows.
    g = density(g, N)
    if not np.isfinite(dt) or dt <= 0:
        raise ValueError("finite positive time step required")
    if not np.isfinite(dephasing_rate) or dephasing_rate < 0:
        raise ValueError("finite nonnegative rate required")
    target = density(phi(g), N)
    kappa = float(rate_model(g))
    if not np.isfinite(kappa) or kappa < 0:
        raise ValueError("finite nonnegative regenerative rate required")
    a = kappa * np.clip(7*metrics(g)['P']-2, 0, 1)
    h = np.asarray(hamiltonian, dtype=complex)
    if h.shape != (N, N) or not np.isfinite(h).all():
        raise ValueError("finite 7x7 Hamiltonian required")
    if np.linalg.norm(h-h.conj().T, 'fro') > TOL:
        raise ValueError("Hermitian Hamiltonian required")
    energies, vectors = np.linalg.eigh(h)
    u = (vectors * np.exp(-1j*energies*dt)) @ vectors.conj().T
    x = u @ g @ u.conj().T
    retain = np.exp(-dephasing_rate*dt)
    x = retain*x + (1-retain)*np.diag(np.diag(x))
    alpha = -np.expm1(-a*dt)
    result = (1-alpha)*x + alpha*target
    return density(result, N)  # detects residuals; no PSD projection


def external_injection(g, sigma, beta):
    if not np.isfinite(beta) or not 0 <= beta <= 1:
        raise ValueError("beta must be in [0,1]")
    return density(beta*density(g, N)+(1-beta)*density(sigma, N), N)


def sqrt_psd(g):
    g = density(g)
    ev, v = np.linalg.eigh(g)
    return (v*np.sqrt(np.maximum(ev, 0))) @ v.conj().T


def bures_distance(g, sigma):
    g, sigma = density(g), density(sigma)
    if g.shape != sigma.shape:
        raise ValueError("equal dimensions required")
    sg = sqrt_psd(g)
    sandwich = sg @ sigma @ sg
    ev = np.linalg.eigvalsh((sandwich+sandwich.conj().T)/2)
    if np.min(ev) < -TOL:
        raise ValueError("sandwich PSD residual exceeds tolerance")
    f = float(np.sum(np.sqrt(np.maximum(ev, 0))))
    if f > 1 + TOL:
        raise ValueError("fidelity residual exceeds tolerance")
    return float(np.sqrt(max(0, 2*(1-min(1, f)))))


u = np.ones(N, dtype=complex) / np.sqrt(N)
sigma = np.outer(u, u.conj())
g = (1-0.45)*I7 + 0.45*sigma
h = np.diag(np.linspace(-0.2, 0.2, N))
omega0 = 1.0  # calibrated reciprocal time; h and rates use this unit
rate_model = lambda x: omega0/7 + kinetic_flux(.2, .8, .1)*metrics(x)['Coh_E']
phi = lambda x: chosen_phi(x, sigma)
for _ in range(100):
    g = split_step(g, h, .01, 2/3, rate_model, phi)
print(metrics(g))  # diagnostics, not a phenomenal verdict

```

## Usage example

The final lines evolve one explicit state with one Hamiltonian, one calibrated time unit and one anchor. Changing any of these changes the model. Record the parameter values, step size and numerical residuals with every result. A density-matrix simulation is classical numerical data and has no automatic Holevo capacity bound on its software memory.

## Isospectral demonstration

Unitary conjugation preserves a spectrum and purity [T]. Eigenvectors depend on the frame, are phase-ambiguous, and are nonunique inside degenerate eigenspaces. The conjecture that eigenframe differences change phenomenal quality requires an independently calibrated readout [H/I]; a simulation supplies no experimental evidence for it.

## Bootstrap example

For the gated isolated model, $I/7$ remains fixed under unitary motion and unital dephasing: $g_V(I/7)=0$ even when $\kappa_{\mathrm{bootstrap}}>0$. Genesis can instead be an explicitly external state injection. The code's `external_injection` chooses

$$
\Gamma_{n+1}=\beta\Gamma_n+(1-\beta)\sigma,\quad \Gamma_0=I/7,\quad
P_n=\frac17+(1-\beta^n)^2\left(P(\sigma)-\frac17\right).
$$

For $0\le\beta<1$ it crosses $2/7$ at finite $n$ iff $P(\sigma)>2/7$; crossing this single cut does not imply Cap₂ or dynamic viability. Dephasing changes the criterion, as in [T-148](/docs/proofs/consciousness/substrate-closure#t-148).

## Extended implementation: Consciousness measures

`metrics` computes $P,R,\Phi$, a row-mask $\mathrm{Coh}_E\in[0,1]$, and a **declared** readout for differentiation. The default $\rho_E=\Gamma$ is a model convention [D], since a one-dimensional $E$ summand in $\mathbb C^7$ is not a tensor subsystem with a nontrivial partial trace. A different lifted readout must be supplied and validated separately. The earlier lower clamp $\mathrm{Coh}_E\ge1/7$ was false: a state supported outside the $E$ row has zero coherence by this score ([T-128](/docs/proofs/consciousness/operationalization#t-128), [T-154](/docs/proofs/consciousness/substrate-closure#t-154)).

### Classification example

`Cap2` is the conjunction $P>2/7$, $R\ge1/3$, $\Phi\ge1$, $D_{\mathrm{diff}}\ge2$; `C=Phi*R` is a summary and cannot replace it. `full_window` adds the selected population-stress criterion $\max\sigma_k<1$. The returned margins are numerical diagnostics. Near a boundary, or with reconstructed data, classify a calibrated confidence set as passing, failing or undetermined; do not treat a floating-point boolean as a statistical certificate. Cognitive depth needs independent probes; historical attenuated purity scores do not establish SAD or levels L3/L4.

## Constructive algorithms from L-unification {#конструктивные-алгоритмы-из-l-унификации}

### Characteristic morphism χ_S

A numerical predicate on states is a chosen subset test. It is not automatically the characteristic morphism into a topos subobject classifier, which requires a named topos, subobject and naturality at every stage. Identifying a classifier $\Omega$ with a dissipative generator remains an additional construction [D/H].

### Temporal modality ▷

A step map defines discrete iteration; a delayed array realizes a chosen shift. A categorical later modality requires the presheaf/base category and its action on morphisms. Neither fixes the physical step duration or establishes a Page–Wootters clock. Keep physical time, acquisition sampling and integration accuracy separate ([T-131](/docs/proofs/consciousness/operationalization#t-131)).

### Lindblad operators L_k from Ω

Seven Fano incidence projectors are one selected dephasing family [D]. Its linear GKSL semigroup is CPTP [T]; complete positivity does not force that family or exactly seven jumps. On equal-rate inputs it attenuates coherences uniformly. For general fixed jumps one can exponentiate the $N^2\times N^2$ Liouville superoperator or use proved CPTP splitting. Plain forward Euler for GKSL is not universally positive.

### Self-modelling operator φ via ℒ_Ω

`chosen_phi` mixes the selected Fano channel and a declared anchor with the state-dependent weight $R$. Freezing the weight/anchor produces a linear CPTP channel; updating the weight with the input usually produces a nonlinear state map. Long-time convergence, uniqueness and idempotence require additional hypotheses and are not supplied by terminality. The [φ_J attractor results](/docs/core/dynamics/evolution#теорема-живой-аттрактор-в-окне) apply to their specified model.

### Example: Full L-unification

A valid integration step is not an implementation of all categorical bridges. In the reference code, the unitary and dephasing maps are exact subflows and the replacement coefficient is $\alpha=1-e^{-a\Delta t}\in[0,1]$. Their composition preserves states in exact arithmetic for every positive step. For feedback frozen at the same input, its derivative at $\Delta t=0$ is the specified vector field. It is a first-order scheme under locally Lipschitz feedback on the trajectory region; state preservation does not ensure adequate accuracy, stability or staying inside the full window. Halving the step and comparing trajectories measures convergence; it is not a proof for a different model.

## Grothendieck topology algorithms {#алгоритмы-топологии}

### Bures metric

`bures_distance` computes $d_B=\sqrt{2(1-f)}$ with root fidelity $f=\operatorname{Tr}\sqrt{\sqrt\Gamma\sigma\sqrt\Gamma}$. Equal-purity states need not have equal distance to $I/7$. An affine replacement is not generally the exact Bures gradient of squared distance; see [evolution geometry](/docs/core/dynamics/evolution#почему-эта-геометрия).

### Bures coverings

Metric balls and finite point clouds are not automatically covering sieves of a Grothendieck topology. A model must specify its category, sieves, pullbacks and the maximality, stability and transitivity axioms. A metric sample alone verifies only the declared finite sample's coverage.

### Atomic coverings and the Ω classifier

Selecting nonzero entries or Fano lines defines a finite incidence algorithm. Its interpretation as atomic covering data must be checked in the specified site. No list of seven matrix projectors by itself supplies a topos, its subobject classifier, or a unique physical dissipator.

## Dependencies

This reference listing uses Python and NumPy. Verum implementation claims remain limited to the [documented implementation status](/docs/applied/coherence-cybernetics/implementation#быстрый-старт); the former listings were not a compiled proof artifact. Biological use additionally needs the [observation model and reconstruction protocol](/docs/applied/research/reconstruction-identifiability), frozen calibration and all relevant modalities.

## Computational Bound: $\mathcal{R}$ and BQP {#вычислительное-ограничение}

The former universal BQP upper bound is withdrawn [✗]. An ideal nonlinear oracle can change complexity, as illustrated by [Abrams & Lloyd](https://arxiv.org/abs/quant-ph/9801041), but this does not prove that the selected regenerative ODE solves SAT with polynomial physical resources. Such a result needs a uniform encoding for growing inputs, allowed operations, input preparation, dimension, rate bounds, precision, readout, noise and total physical cost. Amplifying an exponentially small initial difference may cost exponentially precise preparation or parameters. A fixed $7\times7$ simulator does not resolve this question. See the [conditional computation analysis](/docs/proofs/physics/physics-correspondence#86-вычислительное-ограничение).

### Entropy rates and physical power

For a full-rank differentiable state, $\dot S=-\operatorname{Tr}(\dot\Gamma\log\Gamma)$ [T-271 under that domain]. Unital dephasing contributes nonnegative entropy change; strict positivity and the sign of the regenerative contribution are not universal. At stationarity the **sum** is zero, not each contribution. Boundary entropy derivatives need separate regularity assumptions.

A physical erasure process in a thermal-bath model gives $\dot Q\ge k_BT\dot s_{\mathrm{erase}}$ when a positive erased/exported entropy rate in nats per physical second is established [T-273 conditional]. With bits the factor is $k_BT\ln2$. This is not a bound in terms of purity alone or the number of simulation ticks. A physical mapping of state, bath, Hamiltonian, rates, reversibility and stored correlations is required; the stronger finite-bath equality is given by [Reeb & Wolf](https://arxiv.org/abs/1306.4352). Cosmological rates and universe-as-holon identification remain [T-266: H](/docs/physics/gravity/cosmological-constant#теорема-стадия-вселенной).
