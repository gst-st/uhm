---
sidebar_position: 2
title: "Gap Characterisation and Identifiability"
description: "What a phase profile determines: exact factorisation criteria, counterexamples, readout stability and coding boundaries"
slug: /consciousness/hierarchy/gap-characterization
---

# Gap Characterisation and Identifiability

The 21 pairwise Gap values describe a frame-referenced phase statistic. They do not reconstruct the matrix, its canonical capability gate or its calibrated self-model. This page replaces the former level-signature and Hamming-opacity claims with explicit identifiability and stability results.

:::info Status of the revision
The former unconditional Gap-injection theorem and “at least three opaque channels” conclusion are **retracted [✗]**. The algebra, counterexamples and conditional error bounds below are **[T]**. Proposed associations between phase patterns and biological L-levels are **[H]** and need independently labelled data.
:::

## 1. Gap profile: definition {#gap-профиль}

For $i<j$, let $z_{ij}=\gamma_{ij}$. In the native semantic frame define

$$
g(z):=\frac{|\operatorname{Im}z|}{|z|}=|\sin\arg z|\quad(z\ne0),\qquad g(0):=0.
$$

The profile is $\mathbf G(\Gamma)=(g(z_{ij}))_{i<j}\in[0,1]^{21}$ **[D]**. The zero convention does not mean a missing connection is transparent. A measured profile therefore carries a support mask and amplitudes:

$$
\mathsf{PhaseRecord}(\Gamma)=(\gamma_{ii},\ |\gamma_{ij}|,\ \mathbf1_{|\gamma_{ij}|>\eta},\ g(\gamma_{ij})),
$$

where the detection floor $\eta$ is declared. Even this record loses the sign of the imaginary part and distinctions such as $\theta$ versus $\pi-\theta$.

“Transparency” or “opacity” is an interpretation **[I]**. Algebraically $g=0$ includes both phase $0$ and phase $\pi$; $g=1$ means a purely imaginary nonzero coherence. Neither value by itself proves conscious access.

### Frame and invariant phase data

Under diagonal rephasing $D=\operatorname{diag}(e^{i\chi_i})$,

$$
\gamma_{ij}\mapsto e^{i(\chi_i-\chi_j)}\gamma_{ij},
$$

so pairwise Gap generally changes while $P,R,\Phi$ and the canonical E-weight do not. The triangle product

$$
\gamma_{ij}\gamma_{jk}\gamma_{ki}
$$

is invariant under this rephasing; its phase is defined only when the product is nonzero. Triangle holonomy is not claimed invariant under general $G_2$ rotations. A named pairwise profile is not a $G_2$ invariant either. Fix the frame, or state precisely which transformations and statistic are used.

### Relation to the imaginary operator

For $\mathcal G:=\operatorname{Im}\Gamma$, a real skew-symmetric matrix,

$$
\|\mathcal G\|_F^2=2\sum_{i<j}|\gamma_{ij}|^2g(\gamma_{ij})^2.
$$

This identity is exact **[T]**. Unweighted phase averages omit amplitudes and cannot replace this norm.

## 2. Level signatures: hypothesis, not consequence {#сигнатуры}

Scalar predicates constrain squared moduli and populations. They do not force phase alignment on $(A,E)$, $(L,E)$ or any other named channel. The previous Theorem 1.1 deriving specific phase signatures from L0–L4 is **retracted [✗]**.

A possible empirical programme **[H]** asks whether independently classified systems have reproducible distributions of $\mathbf G$, triangle phases or weighted imaginary power. It must fix the measurement frame, detection floor, probe protocol and labels; reserve independent test data; and compare phase-free amplitude baselines. Any useful signature may be probabilistic. It is not a necessary property of a level without a separate bridge theorem.

If an individual phase is assumed uniformly distributed on $[0,2\pi)$, then

$$
\mathbb E g=2/\pi,\qquad\mathbb E g^2=1/2,
$$

by integration. This is a consequence of an explicit distributional assumption, not a theorem about L0, absence of consciousness, or arbitrary positive matrices. Matrix positivity couples the allowable phases.

### No forced opacity at L4 {#граница-хэмминга}

Equality between actual and modelled phase profiles does not require either zero Gap or nonzero Gap. Fault tolerance is a property of encoding, noise and recovery maps. The number of nonzero pairwise phases is a different quantity.

## 3. E-sector profiles {#e-секторные}

The E-sector has six pairwise phase coordinates. Record its amplitude weight separately:

$$
W_{E,\mathrm{off}}:=\frac{2\sum_{i\ne E}|\gamma_{Ei}|^2}{P}.
$$

The canonical quantity is $\mathrm{Coh}_E=\gamma_{EE}^2/P+W_{E,\mathrm{off}}$; it includes diagonal E-population. Thus $\mathrm{Coh}_E>0$ does not imply a nonzero E-sector phase or off-diagonal coupling. No L2 scalar inequality distinguishes the phases of the attention or logic channels without extra data.

## 4. Relation to the phase diagram {#фазовая-диаграмма}

A projection of a high-dimensional state onto two order parameters loses information. If the chosen parameters depend only on moduli, all diagonally rephased states have the same projected point and can have different pairwise Gaps. An observed change of profile or threshold crossing is not automatically a dynamical phase transition. A bifurcation claim needs the [normal-form conditions](/docs/proofs/consciousness/interiority-hierarchy#бифуркационные-критерии).

## 5. Meta-Gap and model accuracy {#мета-gap}

For a specified state-valued model $\varphi$, $\mathbf G(\varphi(\Gamma))$ is simply the model's phase statistic. It exists at every order where the iterates are valid states, including models with no metacognitive capability. Neither existence nor finiteness of this vector certifies L3.

### Theorem: readout stability with an amplitude floor [T] {#стабильность-считывания}

Let $\Gamma,\widehat\Gamma$ be valid matrices with

$$
\|\Gamma-\widehat\Gamma\|_F\le\delta<m,
$$

and suppose $|\gamma_{ij}|\ge m$ for each observed pair. Then

$$
\max_{(i,j)\ \mathrm{observed}}|g(\gamma_{ij})-g(\widehat\gamma_{ij})|\le\frac{2\delta}{m}.
$$

Consequently the Euclidean error on $k$ observed pairs is at most $2\sqrt{k}\delta/m$; the bound can be clipped to the range of the statistic.

**Proof.** For $z\ne0,w\ne0$,

$$
\left|\frac{|\operatorname{Im}z|}{|z|}-\frac{|\operatorname{Im}w|}{|w|}\right|
\le\frac{|z-w|}{|z|}+\frac{|\operatorname{Im}w|}{|w|}\frac{\big||w|-|z|\big|}{|z|}
\le\frac{2|z-w|}{|z|}.
$$

The matrix error bounds every entry error, while $|w|\ge m-\delta>0$. Substitute $|z|\ge m$.

**Why the floor is necessary.** Let $\Gamma_\epsilon$ have diagonal $1/7$ and only the coherence $\gamma_{12}=\epsilon$ and its conjugate. Let $\widehat\Gamma_\epsilon$ replace this coherence by $i\epsilon$. For $0<\epsilon<1/7$ both matrices are positive, their Frobenius distance is $2\epsilon\to0$, but the selected Gap changes from $0$ to $1$. There is no global continuity at a missing coherence.

A bound on $R=1/(7P)$ controls distance to $I/7$, not distance to $\varphi(\Gamma)$. Therefore it does not supply $\delta$, and no universal $2/3$ perceived-Gap error follows from $R\ge1/3$.

## 6. Rank of the imaginary operator {#ранг-непрозрачности}

**Theorem [T].** A real skew-symmetric $7\times7$ matrix has rank $0,2,4$ or $6$. There exists a real orthogonal matrix bringing it to

$$
\operatorname{diag}(J(\lambda_1),J(\lambda_2),J(\lambda_3),0),\qquad
J(\lambda)=\begin{pmatrix}0&\lambda\\-\lambda&0\end{pmatrix}.
$$

The number of nonzero two-dimensional blocks is at most three; this number is **half the rank**, not the rank itself. The singular values occur in equal pairs.

The former rank-by-level table is **retracted [✗]**. The matrices $\Gamma(t)$ below all have imaginary rank zero but cross the reflection gate. Conversely, $\Gamma=I/7+i\epsilon A$ is positive for real skew $A$ and sufficiently small $\epsilon$, and has the rank of $A$ while staying near minimal purity. Imaginary rank is neither a consciousness classifier nor a measure of self-model recursion.

## 7. What the Hamming bound actually says {#граница-хэмминга-подробно}

For a binary length-$n$ code of minimum distance at least three, radius-one Hamming balls are disjoint, giving

$$
|C|(n+1)\le2^n.
$$

For a linear code with $r=n-k$ check bits this becomes $n+1\le2^r$. Thus a seven-position single-error-correcting code requires $r\ge3$, and the $[7,4,3]$ Hamming code attains equality. This is coding mathematics **[T]**. Primary source: [Hamming, Error Detecting and Error Correcting Codes (1950)](https://onlinelibrary.wiley.com/doi/10.1002/j.1538-7305.1950.tb00463.x).

It does **not** establish three nonzero Gaps among 21 matrix pairs. Check bits, syndrome coordinates, physical communication channels and pairwise phases have different types. A bridge needs an explicit encoding, error model, phase observable and recovery operation. Even in the code, a valid uncorrupted word has zero syndrome while the code remains error-correcting. Redundancy is not the same as a permanently nonzero error signal.

For $\Gamma(t)$ below every Gap is zero, but the canonical $\varphi_{\mathrm{coh}}$ generally changes the state. Hence “zero Gap makes $\varphi$ the identity and prevents correction” is also false. The former Theorem 5.1 on mandatory opacity is **retracted [✗]**; a proposed coding bridge has status **[Pr]** until defined and proved.

## 8. Summary of what can be inferred {#сводная-таблица}

| Given | Valid conclusion | Missing for a stronger conclusion |
|---|---|---|
| Pairwise $g$ | Absolute relative imaginary phase in the fixed frame | Amplitude, diagonal, sign, model certificate |
| $\mathcal G$ | Weighted imaginary power and even rank | Capability/phenomenal bridge |
| $P,R,\Phi,D,A_1$ | Canonical L2 predicate | L3 metamodel probes; phenomenal validation |
| Matrix model error and amplitude floor | Explicit Gap-readout error bound | Calibrated relation to awareness |
| Binary $[7,4,3]$ code | Three check coordinates | A code-to-phase bridge |

## 8a. Exact numerical examples {#количественные-примеры}

Let $u=(1,\ldots,1)/\sqrt7$ and $\Gamma(t)=(1-t)I/7+tuu^\dagger$, $0<t<1$. Its eigenvalues are $(1+6t)/7$ and $(1-t)/7$ with multiplicity six. It is positive, trace one, and every nonzero coherence is $t/7>0$. Therefore

$$
\mathbf G=0,\quad\operatorname{rank}\mathcal G=0,\quad P=\frac{1+6t^2}{7},\quad R=\frac1{1+6t^2},\quad\Phi=6t^2.
$$

### Comparison with an identical Gap profile {#сравнение-gap-профилей}

| $t$ | $P$ | $R$ | $\Phi$ | Scalar gate |
|---|---:|---:|---:|---|
| $0.45$ | $0.316429$ | $0.451467$ | $1.215$ | Passed |
| $0.65$ | $0.505000$ | $0.282885$ | $2.535$ | Reflection fails |

The differentiation mode and operational certificate are stated separately; these examples alone do not assign empirical phenomenal levels. They are sufficient to refute phase-only identification of the scalar gate. At $t=0$, the zero-coherence convention gives the same vector while all phases are absent, illustrating why a support mask is essential.

## 9. Exact replacement for Gap injection {#gap-инъекция}

**Theorem (fibre criterion) [T].** For a statistic $s:\mathcal Z\to\mathcal Y$ and a classification $L:\mathcal Z\to\mathcal L$, a function $\ell:s(\mathcal Z)\to\mathcal L$ with $L=\ell\circ s$ exists if and only if

$$
s(z)=s(z')\implies L(z)=L(z').
$$

The proof is the universal property of the quotient by equal-statistic fibres: define $\ell(s(z))=L(z)$; this is well-defined exactly under the displayed condition.

A richer statistic can determine the **defined** hierarchy if it carries the canonical scalar gates, the typed L1/differentiation data and the required higher-order certificates. That sufficiency follows from the definition and must not be presented as an independent proof of consciousness. General $G_2$ quotienting cannot manufacture the amplitudes lost by a phase-only statistic.

The old statement that Gap is a finer invariant than the L-level is **retracted [✗]**. A useful empirical phase predictor remains possible **[H]**, but its accuracy, domain and uncertainty must be measured.

## Related documents

- [Canonical typed hierarchy](./interiority-hierarchy#типизированный-вход)
- [Formal proofs and counterexamples](/docs/proofs/consciousness/interiority-hierarchy)
- [Gap operator](/docs/core/dynamics/gap-operator)
- [Native-frame phase and triangle holonomy](/docs/consciousness/phenomenology/qualia-structure#язык-качества)
- [Measurement protocol](/docs/applied/research/measurement-protocol)
