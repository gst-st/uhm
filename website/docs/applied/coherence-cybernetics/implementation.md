---
sidebar_position: 8
title: Computational Implementation
description: State-preserving discretisation, reconstruction uncertainty, and explicit model inputs
---

# Computational Implementation

A simulator implements a **specified dynamical model [D]**. It does not infer that model, reconstruct a physical state, or establish consciousness merely by producing a positive matrix. The [mathematical kernel](/docs/reference/mathematical-kernel), [evolution](/docs/core/dynamics/evolution), and [identifiability protocol](/docs/applied/research/reconstruction-identifiability) specify these separate obligations.

## State and configuration {#быстрый-старт}

Use a Hermitian positive semidefinite matrix $\rho$ with $\operatorname{Tr}\rho=1$. Store the frame, Hamiltonian, dissipator, feedback target, rates, physical time calibration, experiential extension, and measurement model alongside it. The seven-axis model has 48 real state coordinates; a joint state of $n$ such factors has dimension $7^n$ and $7^{2n}-1$ coordinates. Seven coordinates for an aggregate require an explicit reduction map and discard joint information.

A Cholesky parametrisation $\rho=TT^\dagger/\operatorname{Tr}(TT^\dagger)$ is useful for estimation when $T\ne0$. It does not make the measurement model identifiable. Confidence sets belong to the measurement likelihood, with subject and intervention structure retained.

## A state-preserving step {#from-formula-to-code}

For the selected Fano dephasing family and a density-valued target $B$ consider

$$
\dot\rho=-i[H,\rho]+\gamma(\mathcal F\rho-\rho)+a(\rho)(B(\rho)-\rho),\qquad \gamma\ge0,\quad a\ge0,
$$

where $\mathcal F\rho=\operatorname{diag}\rho+\tfrac13(\rho-\operatorname{diag}\rho)$. The following first-order scheme freezes $a$ and $B$ at the initial state of each step. The array index of $E$ is explicitly set to 4 in the convention $(A,S,D,L,E,O,U)$.

```python
import numpy as np
from scipy.linalg import expm

def diagnostics(rho, e=4):
    p = float(np.trace(rho @ rho).real)
    d = float(np.sum(np.real(np.diag(rho)) ** 2))
    q_e = rho[e, e].real ** 2 + 2 * (
        np.sum(np.abs(rho[e, :]) ** 2) - abs(rho[e, e]) ** 2)
    return p, p / d - 1, float(q_e / p)

def step(rho, h, gamma, dt, rate, target):
    # rate and target are frozen at the beginning of this step.
    a = float(rate(rho))
    sigma = np.asarray(target(rho), dtype=complex)
    if dt < 0 or gamma < 0 or a < 0:
        raise ValueError("Rates and dt must be nonnegative")
    assert np.allclose(h, h.conj().T)
    assert np.allclose(sigma, sigma.conj().T)
    assert np.isclose(np.trace(sigma), 1)
    assert np.linalg.eigvalsh(sigma).min() >= -1e-12
    u = expm(-1j * h * dt)
    x = u @ rho @ u.conj().T
    diag = np.diag(np.diag(x))
    x = diag + np.exp(-2 * gamma * dt / 3) * (x - diag)
    w = np.exp(-a * dt)
    return w * x + (1 - w) * sigma
```

**Why positivity holds [T].** The first map is unitary conjugation. The second is the convex combination $c x+(1-c)\operatorname{diag}x$, $c=e^{-2\gamma\Delta t/3}\in[0,1]$. The third is a convex combination with a valid density matrix. Their composition preserves positivity and trace for **every nonnegative step size** in exact arithmetic. With frozen coefficients each map is CPTP. The full algorithm can be nonlinear because its coefficients depend on the initial state; calling it one CPTP map is incorrect.

**Accuracy is a separate question.** For bounded smooth coefficients on the region traversed, freezing and splitting give a local error $O(\Delta t^2)$ and a first-order global error over fixed finite time. A Lipschitz drift with constant $L$ and a local defect bound $C\Delta t^2$ gives a global bound of the form $C'\Delta t(e^{LT}-1)/L$, interpreted continuously at $L=0$. The constants depend on the model and region. Step doubling estimates error; a fixed rule such as $\Delta t\le0.01$ cannot guarantee accuracy across physical scales. Nonsmooth gates require the corresponding weaker error analysis or event handling.

## Numerical checks {#pitfalls}

At every reported step check Hermiticity, trace, the smallest eigenvalue, and $1/7\le P\le1$. A small tolerance is a statement about floating point error. A substantial violation indicates a defective input or algorithm; clipping a reported scalar does not repair the state. A projection onto the density cone changes the numerical trajectory and must be included in the error budget. Generic explicit Euler and Runge–Kutta methods do not guarantee positivity.

For a valid density matrix $P\ge1/7$ and $d=\sum_i\rho_{ii}^2\ge1/7$, so the purity and integration denominators cannot approach zero. $\mathrm{Coh}_E\in[0,1]$ is a Hilbert–Schmidt share, not a universal viable-state lower bound. In particular $I/7$ has $\mathrm{Coh}_E=1/7$ and zero off-diagonal E-coherence; viable states with an empty E-sector exist. The former universal T-38a claim is withdrawn; see [the conditional balance theorem](./theorems#теорема-81-условная-необходимость-интериорности-no-zombie).

Meaningful verification includes an analytic diagonal example, a noncommuting Hamiltonian, a boundary state, finite-step positivity, convergence under step refinement, and an independently computed counterexample to any universal claim used by the model. [The executable kernel checks](/docs/reference/mathematical-kernel#verification) cover these mathematical properties without certifying the entire theory.

## Environmental coupling {#canonical-decomposition-f-ext}

A positive sum of GKSL generators is again a GKSL generator. Additional dissipative terms are permitted; the old T-57 and T-102 three-type completeness claims are withdrawn. Writing controls as changes to $H$, dissipators, and a replacement target is an engineering convention [D]. It needs a representation of the actual admissible controls and does not prove their exhaustive uniqueness. A signed correction need not be a GKSL generator by itself; validate the **full** generator or channel.

For joint systems use the tensor state and explicitly defined local channels or a joint Hamiltonian. A nonlinear single-state feedback has no automatic tensor extension: specify how its coefficients are evaluated from local marginals and use a linear local channel with those frozen coefficients. Feature-to-state reconstruction is an estimator, not an environmental quantum channel.

## Bootstrap and closed gates {#bootstrap-resolution}

The selected baseline $\kappa_b=\omega_0/7$ is a model convention [D]. A positive rate alone cannot generate coherence. If the feedback gate $g(P)$ vanishes at $P=1/7$, then $a=\kappa g(P)=0$ at $I/7$; unitary and unital dissipative terms leave $I/7$ fixed. A start from this state requires a specified preparation, a nonunital input, or a revised gate, each with its own energetic and physical model. It cannot be proved by adding a positive scalar called bootstrap.

The bounded kinetic approximation for $\kappa_0$ has stated timescale assumptions; it is not a norm of a categorical natural transformation. Use the regularised rate family in [septicity](/docs/core/foundations/axiom-septicity#категориальный-вывод-kappa0) when boundary continuity is needed.

## Monitoring and control {#пороговые-значения}

Report the four margins $P-2/7$, $R-1/3$, $\Phi-1$, and $D_{\rm diff}-2$. Only the first cut is strict; the other three include equality. The full verdict requires the specified experiential extension and readout. A scalar $C=\Phi R$, a stress score, or matrix purity alone is insufficient. With a reconstruction confidence set $K$, certify a criterion only if it holds for every admissible record in $K$; otherwise report it as unresolved. A proxy based on the E-row must be named as a proxy.

The cut $2/7$ is an exact consequence of a **chosen majority convention** for Hilbert–Schmidt differentiation, not a universal survival or detection threshold. The self-observation and differentiation cuts are selected conventions; the operational interpretation requires calibration. Dynamic viability requires a specified domain, disturbances, admissible controls, and an invariant or viability-kernel argument.

For a finite action set, evaluate the specified loss for each action. For compact controls and a continuous loss a minimiser exists. Uniqueness, convexity, and efficient global optimisation each require additional assumptions. Do not infer any of them from compactness or from the former universal stress-window equivalence.

## Cost and reproducibility {#debugging-coherent-systems}

Dense multiplication and diagonalisation cost $O(N^3)$ and memory $O(N^2)$; a fixed Hamiltonian permits precomputing its unitary step. A joint tensor state incurs the corresponding exponential growth in the number of factors. Sparse approximations and aggregate models require an error bound for the observables of interest.

Publish the chosen frame, model parameters, target and gate, step rule and tolerance, random seed, preparation, measurement likelihood, and uncertainty set. Distinguish a simulated mathematical example from a calibrated physical prediction. Numerical success verifies the implemented instance; physical identification and the phenomenal interpretation remain separate inputs.

<a id="conclusion"></a>
<a id="further-reading"></a>
<a id="what-we-learned-implementation"></a>
