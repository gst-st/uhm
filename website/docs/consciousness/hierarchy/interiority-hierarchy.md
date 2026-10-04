---
sidebar_position: 1
title: "Interiority Hierarchy"
description: "Typed, cumulative capability predicates L0–L4; scalar gates, measurement certificates and explicit limits"
slug: /consciousness/hierarchy/interiority-hierarchy
---

# Interiority Hierarchy: L0 → L4 {#уровни-интериорности}

The hierarchy separates an ontological interpretation, an operational classification, and the mathematical consequences of that classification. A density matrix does not by itself establish phenomenal consciousness. The identification of the operational L2 predicate with cognitive qualia remains the [two-aspect bridge](/docs/consciousness/foundations/two-aspect-monism) **[I]**.

:::info Canonical definition and revision
This page is the canonical definition of the hierarchy. The revision of 2026-10-03 replaces incompatible definitions of L3/L4 and the false Gap-injection theorem. Definitions have status **[D]**; algebraic consequences **[T]**; statements about organisms or phenomenal access **[H]/[I]**. The detailed proofs and counterexamples are in [Formal specification](/docs/proofs/consciousness/interiority-hierarchy).
:::

## Typed input {#типизированный-вход}

Classification uses an augmented record

$$
z=(\Gamma,\mathsf E,\mathsf M,\mathsf Q),\qquad \Gamma\in\mathcal D(\mathbb C^7),
$$

not merely a matrix. Here $\mathsf E$ specifies the experiential realisation, $\mathsf M$ the implemented self-model/readout, and $\mathsf Q$ the probes and calibration used to test higher-order predictions. Missing components are reported as **unknown**, rather than inferred from phase or purity.

Two experiential modes are kept distinct:

| Mode | L1 predicate $A_1$ | Differentiation $D(z)$ |
|---|---|---|
| **7D proxy** [D] | $\mathrm{Coh}_E(\Gamma)>0$ | $D^{7D}:=1+6\,\mathrm{Coh}_E(\Gamma)$ |
| **Specified extension** | $\operatorname{rank}(\rho_E)>1$ | $D^{\mathrm{ext}}:=\exp S_{vN}(\rho_E)$ |

The canonical normalisation is $\mathrm{Coh}_E^{\max}=1$. The proxy is a stipulated statistic, not an equality to extension entropy. In the extension $\rho_E$ must be a **normalised density matrix** on a declared space. A genuine tensor factor permits a partial trace. The 42D Page–Wootters E-axis is a summand of the six-dimensional system factor: its clock block must be normalised by its trace when nonzero. The lift and conditioning are part of $\mathsf E$. See [7D/42D typing](/docs/core/structure/dimension-e#rho-e-7d-42d).

Because the canonical E-projection includes $\gamma_{EE}$,

$$
\mathrm{Coh}_E=\frac{\gamma_{EE}^2+2\sum_{i\ne E}|\gamma_{Ei}|^2}{P},
$$

$\mathrm{Coh}_E>0$ is equivalent to $\gamma_{EE}>0$ for a positive matrix. It does not establish nonzero E coupling or a literal multidimensional experiential state. In particular $I/7$ passes this L1 proxy and has $D^{7D}=13/7<2$. Use the separate off-diagonal weight $2\sum_{i\ne E}|\gamma_{Ei}|^2/P$ when the question concerns coupling.

## Cumulative capability predicates

Write $A_k(z)$ for possession of capability $k$, and define the exclusive level as the greatest satisfied capability. The nesting is explicit:

$$
A_4\Rightarrow A_3\Rightarrow A_2\Rightarrow A_1\Rightarrow A_0.
$$

| Capability | Operational definition | Interpretation |
|---|---|---|
| **L0** | $A_0$: a valid state $\Gamma\in\mathcal D(\mathbb C^7)$ | Interiority [I] |
| **L1** | $A_1$: the declared experiential test above | Phenomenal geometry/proxy [D/I] |
| **L2** | $A_2:=A_1\land \mathsf{Cap}_2$; $\mathsf{Cap}_2$ is the four-gate predicate below | Cognitive qualia bridge [I] |
| **L3** | $A_3:=A_2\land\mathsf{MetaCert}_2$ | Tested metamodel capability [D] |
| **L4** | $A_4:=A_3\land\bigwedge_{n\ge3}\mathsf{MetaCert}_n\land\mathsf{Compatible}$ | Ideal coherent tower [D] |

The predicates organise the chosen model. They do not assign an electron, bacterium, mammal, meditator or network a measured level. Such assignments require independently calibrated data and retain status **[H]**.

## L0: Interiority {#уровень-0-интериорность-interiority}

<a id="определение-l0"></a>
**Definition L0 [D].** $A_0(z)$ holds for every valid state in the model. Calling its inner aspect “interiority” is an ontological interpretation. Its universality is a definitional consequence, not a theorem establishing experience in every physical object. The matrix need not be close to $I/7$, and L0 does not impose $R\approx0$.

## L1: Phenomenal geometry {#уровень-1-феноменальная-геометрия-phenomenal-geometry}

<a id="определение-l1"></a>
**Definition L1 [D].** Use exactly one of the typed tests in the input table. A one-dimensional basis axis of $\mathbb C^7$ is not a tensor subsystem: $\operatorname{rank}(\gamma_{EE})>1$ is impossible. No equivalence between the literal rank test and $P>2/7$ is asserted.

For a declared experiential space $\mathcal H_E$, its pure-state rays form $\mathbb P(\mathcal H_E)$. With normalised representatives the Fubini–Study distance is

$$
d_{FS}([\psi],[\chi])=\arccos|\langle\psi|\chi\rangle|.
$$

The bounded quantity $1-|\langle\psi|\chi\rangle|^2$ is a squared chordal distinguishability, not the finite-distance formula for the line element. See [metric definition](/docs/proofs/consciousness/interiority-hierarchy#определение-12-метрика-фубини-штуди).

<a id="уровень-2-когнитивные-квалиа-cognitive-qualia"></a>
## L2: canonical capability gate {#l2-когнитивные-квалиа}

<a id="определение-l2"></a>
Define in the fixed semantic frame:

$$
P=\operatorname{Tr}\Gamma^2,\quad Q=\sum_i\gamma_{ii}^2,\quad R=\frac1{7P},\quad \Phi=\frac{P-Q}{Q}.
$$

The canonical gate is

$$
\mathsf{Cap}_2(z):=(P>2/7)\land(R\ge1/3)\land(\Phi\ge1)\land(D(z)\ge2).
$$

**Theorem (scalar window) [T].** Given this gate,

$$
2/7<P\le3/7,\qquad 1/3\le R<1/2,\qquad 1\le\Phi\le2.
$$

Proof: $R\ge1/3\iff P\le3/7$; $Q\ge1/7$ gives $\Phi\le7P-1\le2$.

The equality $R=1-\|\Gamma-I/7\|_F^2/P$ measures proximity to $I/7$. It is **not** the accuracy of an implemented self-model. Keep $R$ separate from $R_\varphi:=1-\|\Gamma-\varphi(\Gamma)\|_F^2/P$ and from fidelity. Neither metric monotonicity nor a count of three dynamical terms establishes these identifications.

| Choice | Mathematical consequence | Additional bridge |
|---|---|---|
| HS majority criterion | $P>2/7$ | Majority as physical viability [H] |
| Canonical $R\ge1/3$ | $P\le3/7$ | $R$ as calibrated reflective competence [H/I] |
| $\Phi\ge1$ | Off-diagonal HS weight at least diagonal weight | Cognitive integration interpretation [I] |
| $D\ge2$ | For the extension, $S_{vN}\ge\log2$ | Minimal phenomenal differentiation [H/I] |

The thresholds are exact within these definitions. Their universal empirical interpretation requires independent tests; adopting them does not prove that every gated state has conscious experience. Additional [full viability constraints](/docs/core/dynamics/viability#полная-жизнеспособность), such as stress bounds or sustained dynamics, are recorded separately rather than silently added to this instantaneous gate.

## L3: tested metamodel capability {#l3-сетевое-сознание}

<a id="определение-l3"></a>
**Definition L3 [D].** L3 requires L2 and a second-order predictive certificate. For a preregistered probe family $\mathsf Q_2$, compare the implemented metamodel prediction $\widehat\rho_2(q)$ with an independently measured target $\rho_2(q)$ describing the first model's response:

$$
\mathsf{MetaCert}_2:=\left[\sup_{q\in\mathsf Q_2}d_B(\widehat\rho_2(q),\rho_2(q))\le\varepsilon_2\right]\land
\left[\sup_{q,q'}d_B(\rho_2(q),\rho_2(q'))\ge a_2>2\varepsilon_2\right].
$$

Both states must lie in the same declared output space. For empirical data the supremum is over the stated finite test set; generalisation beyond it requires a model or statistical guarantee. The parameters $a_2,\varepsilon_2$ and probe family are calibration data, fixed independently of test outcomes. They are not universal constants derived from septicity. A constant prediction cannot pass both conditions by the triangle inequality.

### Status of the former $K=4$ argument {#теорема-l3-k4}

The previous unconditional T-67 proof is **retracted [✗]**. Three summands in a generator and one coherence modification do not imply four independent information channels. A nonzero differential is not necessarily injective; being CPTP does not repair that inference. The diagnostic $f(\varphi\Gamma,\varphi^2\Gamma)\ge1/4$ may be recorded, but does not certify L3: it equals $1$ at a trivial fixed point.

Metastability of a certified metamodel is a dynamical question. It requires an attractor, perturbation class, and spectral/escape estimates. The formula $1/[\kappa(1-R^{(2)})]$ is not a universal retention time, and L2 itself is not automatically stable.

## L4: ideal compatible tower

<a id="определение-l4"></a>
**Definition L4 [D].** Require certificates at every order, using declared probe/target spaces and forgetting maps connecting successive models. $\mathsf{Compatible}$ means that predicting at order $n+1$ and forgetting gives the declared order-$n$ prediction, exactly in the ideal model or within a stated error budget in an approximation. Each order retains the nontrivial-response condition $a_n>2\varepsilon_n$.

The former clause $P>6/7$ is **retracted [✗]**: it contradicts $P\le3/7$ inherited from L2. A fixed point $\varphi(\Gamma)=\Gamma$ or a limit of successive fidelities equal to $1$ does not establish a nontrivial compatible tower.

### Categorical typing and the Postnikov tower {#теорема-l4-категориальная}

The former universal T-86 proof is **retracted [✗]**. For an **object** $X$ of an $\infty$-topos, the Postnikov tower is an inverse system

$$
\cdots\to\tau_{\le3}X\to\tau_{\le2}X\to\tau_{\le1}X\to\tau_{\le0}X.
$$

The comparison is $X\to\varprojlim_n\tau_{\le n}X$, not a colimit along a canonical forward tower. Reconstruction requires the appropriate convergence hypothesis. A truncation permits homotopy through degree $n$; it does not force $\pi_n\ne0$. An $m$-truncated object already stabilises for $n\ge m$.

L-levels are operational predicates; $n$-truncations are categorical constructions. Identifying them requires an explicit experiential object and a bridge theorem. No Bures distance between a topos and its truncation is defined here. Standard references: [Kerodon, Postnikov towers](https://kerodon.net/tag/055L), [Lurie, Higher Topos Theory, §§5.5.6, 7.2.1](https://www.math.ias.edu/~lurie/papers/HTT.pdf).

### Finite resources and the ideal limit {#теорема-l4-недостижимость}

**Conditional resource bound [C].** If every independently implemented order consumes at least $c>0$ of a declared resource and the system has budget $B<\infty$, at most $\lfloor B/c\rfloor$ such orders can be realised simultaneously. This follows from $nc\le B$. The per-order cost and independence assumptions must be established for the proposed implementation. Finite-dimensional state space, incompleteness, or contraction alone do not supply them. A finite algorithm can describe an infinite family symbolically; finite experimental observations alone cannot certify all of it.

## Feasible gate profiles {#профиль-ворот}

<a id="двенадцать-режимов"></a>
The four gate tests reduce to three scalar quantities $P,\Phi,D$, since $R$ is determined by $P$. Their formal Boolean enumeration has twelve labels. They are **not twelve guaranteed nonempty physical regions**.

**Theorem (feasibility restriction) [T].** $\Phi\le7P-1$. Thus:

| Purity range | Allowed integration |
|---|---|
| $P<2/7$ | $\Phi<1$ necessarily |
| $P=2/7$ | $\Phi\le1$; equality requires a uniform diagonal |
| $2/7<P\le3/7$ | Both sides of $\Phi=1$ can occur; the L2 scalar window |
| $P>3/7$ | Reflection gate fails; integration alone does not certify L2 |

The former “flooded” and “white-out” examples combining $P<2/7$ with $\Phi\ge1$ are **retracted [✗]**. Naming gate failures does not measure a clinical or psychedelic state.

<a id="две-грани"></a>
At the lower boundary $R\to1/2$, and at the upper boundary $R\to1/3$. These are algebraic facts. Their subjective interpretation requires empirical calibration.

<a id="схождение-с-энтропийным-мозгом"></a>
A two-sided window in a neuroscience model is not quantitative confirmation of these thresholds. Neural signal entropy and $\operatorname{Tr}\Gamma^2$ require a validated measurement bridge. Even von Neumann entropy is not uniquely determined by purity in dimension seven.

## Gap profiles and identifiability {#gap-характеристика-уровней-l0l4}

The frame-referenced statistic is $\mathrm{Gap}(i,j)=|\operatorname{Im}\gamma_{ij}|/|\gamma_{ij}|$ for nonzero coherences; zero at zero is a convention. Its interpretation as conscious “opacity” is **[I]**. A profile contains phases without amplitudes or calibration, so scalar gate thresholds do not force particular opaque channels.

**Theorem (conditional readout stability) [T].** If a self-model approximates the actual matrix with $\|\Gamma-\widehat\Gamma\|_F\le\delta<m$, and every observed actual coherence has modulus at least $m>0$, then the per-channel Gap error is at most $2\delta/m$. A bound on canonical $R$ alone is not a self-model error bound. Proof and the essential amplitude-floor condition: [Gap characterisation](./gap-characterization#стабильность-считывания).

At an exact fixed point actual and computed profiles coincide tautologically. This equality does not prove phenomenal access. No Hamming theorem forces three nonzero Gap channels; a code-to-observable bridge would be an additional premise.

## Replacement for Gap injection {#теорема-gap-инъекция}

The former theorem “different L-levels imply different Gap profiles” is **retracted [✗]**.

**Theorem (factorisation criterion) [T].** A classification $L:\mathcal Z\to\mathcal L$ is computable from a statistic $s:\mathcal Z\to\mathcal Y$ exactly when it is constant on every fibre of $s$. Equivalently, a map $\ell:s(\mathcal Z)\to\mathcal L$ with $L=\ell\circ s$ exists. Necessity follows by substitution; sufficiency defines $\ell(y)$ using any representative of the fibre. This is factorisation, not an injection from levels into profiles.

**Counterexample to phase-only gate identification [T].** Let $u=(1,\ldots,1)/\sqrt7$ and

$$
\Gamma(t)=(1-t)I/7+tuu^\dagger,\quad 0<t<1.
$$

All 21 pairwise Gaps are zero, while $P=(1+6t^2)/7$, $R=1/(1+6t^2)$, and $\Phi=6t^2$.

| $t$ | $P$ | $R$ | $\Phi$ | Purity/reflection/integration gates |
|---|---:|---:|---:|---|
| $0.45$ | $0.316429$ | $0.451467$ | $1.215$ | Pass |
| $0.65$ | $0.505000$ | $0.282885$ | $2.535$ | Reflection fails |

This establishes failure to identify the scalar capability gate; it does not assert a full empirical L2 assignment without the differentiation/readout certificate. The joint record $(P,R,\Phi,D,A_1,\mathsf{MetaCert}_n,\mathsf{Compatible})$ determines the defined hierarchy. The phase profile alone does not. General $G_2$ rotations do not preserve a frame-indexed pairwise profile, so quotienting it by $G_2$ does not repair the failure.

## Threshold crossing versus bifurcation {#теорема-a4-бифуркация}

The former unconditional T-41 identification of all L-transitions with a swallowtail is **retracted [✗]**. A threshold may be crossed along a smooth trajectory with no change in the number or stability of attractors. Three control parameters do not establish a codimension-three singularity.

In the standard potential convention, $A_k$ has germ $x^{k+1}$: $A_2$ is the fold, $A_3$ the cusp ($x^4$), and $A_4$ the swallowtail ($x^5$). A claimed normal form needs a smooth centre-manifold reduction, the appropriate degeneracy, parameter transversality and an explicit relation to the gate. See [formal criteria](/docs/proofs/consciousness/interiority-hierarchy#бифуркационные-критерии).

## Classification algorithm {#алгоритм-level}

```text
Input: Gamma, mode E, declared self-models and certificates
Validate Hermiticity, positivity and trace = 1.
P = sum_ij abs(Gamma_ij)^2
Q = sum_i Gamma_ii^2
R = 1 / (7*P)
Phi = (P-Q) / Q
If mode is proxy: A1 = Coh_E > 0; D = 1 + 6*Coh_E.
If mode is extension: require a normalised rho_E; A1 = rank(rho_E) > 1;
                     D = exp(-Tr(rho_E log rho_E)).
If required data are missing: return the evaluated gates and UNKNOWN entries.
A2 = A1 and P > 2/7 and R >= 1/3 and Phi >= 1 and D >= 2.
A3 = A2 and independently verified MetaCert_2.
A4 = A3 and a proof/certificate of the compatible all-order tower.
Return the greatest satisfied A_k; retain uncertainty at unverified orders.
```

Computing $P,Q,R,\Phi,\mathrm{Coh}_E$ costs $O(N^2)$. Positivity validation and extension eigendecomposition have their own costs; higher-order certificates are not obtained by a few matrix operations. With measurement uncertainty, report gate intervals and require a margin from each boundary. The L2 scalar certificate is a model classification; the phenomenal interpretation remains a separate claim.

## Related documents

- [Formal specification and proofs](/docs/proofs/consciousness/interiority-hierarchy)
- [Gap identifiability, stability and rank](./gap-characterization)
- [Self-observation and distinct reflection measures](/docs/consciousness/foundations/self-observation)
- [Experiential realisation](/docs/core/structure/dimension-e#rho-e-7d-42d)
- [Depth tower](./depth-tower): its channel-based score is not automatically an L-level certificate.
