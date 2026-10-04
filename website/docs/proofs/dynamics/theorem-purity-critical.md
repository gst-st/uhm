---
title: Structural Majority and Critical Purity
sidebar_position: 1
description: Exact threshold theorem, operational discrimination and explicit biological bridge
---

# Structural majority and critical purity

The revision of 2026-10-03 separates an exact matrix theorem from its interpretation as survival. The number $2/N$ is retained as the canonical structural-majority cut [D]. It is not a universal threshold of distinguishability, symmetry breaking or biological life.

## Exact theorem {#теорема-фробениусова-различимость}

Let $\rho\in D_N$, $P=\operatorname{Tr}\rho^2$ and $\Delta=\rho-I/N$. Since $\operatorname{Tr}\Delta=0$,

$$
\langle I/N,\Delta\rangle_F=0,\qquad P=1/N+\|\Delta\|_F^2.
$$

**Structural-majority theorem [T].**

$$
\|\Delta\|_F^2>\|I/N\|_F^2\quad\Longleftrightarrow\quad P>2/N.
$$

**Proof.** $\|I/N\|_F^2=1/N$. Substitute into the orthogonal decomposition. Equality occurs at $P=2/N$. For $N=1$ the cut is unattainable; for $N=2$ strict majority is unattainable ($P\le1$); for $N>2$ it is nonempty. $\square$

Choosing majority is a definition, not a consequence of the uniqueness of $I/N$. More generally a prescribed structural share $s=\|\Delta\|_F^2/P>c$ gives $P>1/[N(1-c)]$ for $0<c<1$. Majority selects $c=1/2$. A parameter-free convention still needs an operational justification.

For UHM, $P_{\mathrm{crit}}=2/7$. The bridge (V-majority) says that an operational survival criterion corresponds to this cut. It is a hypothesis [H], separately from the exact theorem. Its test must reconstruct states without imposing the cut in the estimator.

## Ordinary discrimination has no positive purity cut

For equally likely $\rho$ and $I/N$, the Holevo–Helstrom theorem gives

$$
p_{\mathrm{succ}}=\frac12+\frac14\|\rho-I/N\|_1.
$$

Thus every $\rho\ne I/N$ is distinguishable with advantage. For

$$
\rho=\operatorname{diag}(1/7+0.1,1/7-0.1,1/7,1/7,1/7,1/7,1/7)
$$

we have $P=1/7+0.02<2/7$ and $p_{\mathrm{succ}}=0.55$. This counterexample withdraws the former reading “$P\le2/7$ is indistinguishable from chaos” [✗]. The trace-distance and Frobenius criteria answer different questions.

## Haar probes: a conditional operational realization

For a Haar-random unit vector $\psi$ and a traceless Hermitian $\Delta$,

$$
\mathbb E\langle\psi|\Delta|\psi\rangle=0,\qquad\mathbb E\langle\psi|\Delta|\psi\rangle^2=\frac{\operatorname{Tr}\Delta^2}{N(N+1)}.
$$

**Proof.** $\mathbb E(|\psi\rangle\langle\psi|)^{\otimes2}=(I+\mathrm{Swap})/[N(N+1)]$; contract with $\Delta\otimes\Delta$. This is a second moment of a *probability shift*. It is not the noise variance of a Bernoulli single-shot outcome. Comparing it to a stipulated reference variance can implement a chosen majority rule; it does not independently select $2/N$.

## Sharp spectral bound {#34-путь-4-спектральное-условие-характеристика-не-независимый-вывод}

For $N\ge2$, let $a=\lambda_{\max}(\rho)$. Cauchy–Schwarz for the other $N-1$ eigenvalues gives

$$
P\ge a^2+\frac{(1-a)^2}{N-1},\qquad a\le\frac{1+\sqrt{(N-1)(NP-1)}}N.
$$

Equality holds exactly when the remaining eigenvalues are equal. At $P=2/N$ the upper bound is $(1+\sqrt{N-1})/N$. This is the **largest possible** eigenvalue at that purity, not the eigenvalue of every threshold state. Purity does not determine a spectrum.

For $N=7$ the uniform-ray family

$$
\rho_t=(1-t)I/7+t\,uu^\dagger,\quad u=(1,\ldots,1)/\sqrt7
$$

has $P=(1+6t^2)/7$ and crosses the majority boundary at $t=1/\sqrt6$. In particular $t=0.3$ gives $P=0.22$, not a viable state under the structural-majority definition.

## Entropy and symmetry {#путь-6-октонионная-норма}

$$
D(\rho\|I/N)=\log N-S(\rho).
$$

Its quadratic expansion near $I/N$ is $\tfrac N2\operatorname{Tr}\Delta^2$; that expansion is not exact at the majority boundary and purity alone does not determine entropy. The former universal “one bit” interpretation is withdrawn [✗].

$I/N$ is the unique state invariant under all $U(N)$ conjugations [T]: commuting with every matrix forces a scalar, and trace one fixes it. Every $\rho\ne I/N$ has a smaller stabilizer; symmetry breaking therefore starts at $P>1/N$, not only at $2/N$. Octonionic norm multiplicativity does not select a purity cut by itself.

## Integration and reflexive access

In a fixed frame let $d=\sum_i\rho_{ii}^2$, $\Phi=P/d-1$ and $R=1/(NP)$. Then

$$
d\ge1/N,\quad\Phi\le NP-1,\quad\Phi\ge1\Rightarrow P\ge2/N.
$$

Equality in the last implication requires both uniform diagonal and $\Phi=1$. The converse is false: a diagonal pure state has $P=1$ and $\Phi=0$. For $N=7$, $P>2/7$ and the chosen access threshold $R\ge1/3$ give $(2/7,3/7]$; the integration and differentiation conditions remain additional conjuncts. Neither the interval nor $\Phi R\ge1/3$ alone establishes consciousness. See the [typed kernel](/docs/reference/mathematical-kernel#thresholds).

## Dynamical viability

A static majority predicate differs from forward invariance or survival under disturbances. For a chosen dynamics and region $V$, viability requires an admissible trajectory staying in $V$; robust viability also quantifies over an explicitly stated disturbance class. A stationary state with $P>2/7$ is sufficient for an unperturbed constant trajectory, but stability and persistence under perturbations need separate estimates.

For $\dot\rho=\mathcal L_0\rho+a(\rho)(M(\rho)-\rho)$,

$$
\dot P=2\operatorname{Tr}(\rho\mathcal L_0\rho)+2a(\rho)\bigl(\operatorname{Tr}(\rho M(\rho))-P\bigr).
$$

The regeneration contribution can have either sign. Its sign is not fixed by an imported free-energy scalar alone. If $a(\rho)=0$ below the threshold, autonomous genesis from $I/N$ is impossible under a unital linear part: an external preparation/non-unital environment is required. Existence of viable sinks for specific anchors and rate regimes is a conditional dynamical result, not a consequence of the static cut.

## Verification and primary sources

The counterexamples and identities are checked by `website/scripts/check_mathematical_kernel.py`; original spectral and dynamical tests remain in `check_core_numbers.py`.

- John Watrous, [The Theory of Quantum Information, chapter 3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.double.3.pdf): optimal discrimination.
- Petz and Sudár, [Geometries of Quantum States](https://www.esi.ac.at/preprints/esi204.pdf): monotone quantum geometry, distinct from a biological majority bridge.
- [Measurement protocol](/docs/applied/research/measurement-protocol): frozen reconstruction and empirical test conditions.
