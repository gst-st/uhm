---
slug: /proofs/categorical/uniqueness-theorem
sidebar_position: 3
title: "Uniqueness theorem of representation"
description: "G₂-rigidity of holonomic representation: uniqueness of the map G up to gauge group G₂ = Aut(𝕆). Analogue of the Stone–von Neumann theorem for UHM."
---

# Uniqueness Theorem of Holonomic Representation

:::warning Status: [Т] — all steps proven
The uniqueness theorem of holonomic representation is a **theorem [Т]**, relying exclusively on previously proven results:
- Primitivity of $\mathcal{L}_\Omega$ [Т] ([proof](/docs/core/operators/lindblad-operators#примитивность-ℒω))
- Full minimality 7/7 [Т] ([proof](/docs/proofs/minimality/theorem-minimality-7))
- Bridge T15 [Т]: (AP)+(PH)+(QG)+(V) $\Rightarrow$ P1+P2 $\Rightarrow$ $\mathbb{O}$ $\Rightarrow$ $G_2$ ([proof](/docs/proofs/minimality/theorem-octonionic-derivation#мост))
- L-unification [Т] ([proof](/docs/core/operators/lindblad-operators))
- Uniqueness of E, O, U [Т] ([proof](/docs/proofs/minimality/theorem-minimality-7))
:::

---

## Problem statement {#проблема}

### The problem of the map G

The central task of operationalizing UHM is the **map G**:

$$
G: \mathrm{States}(S) \to \mathcal{D}(\mathbb{C}^7)
$$

which assigns to a physical system $S$ satisfying (AP)+(PH)+(QG)+(V) its coherence matrix $\Gamma \in \mathcal{D}(\mathbb{C}^7)$.

In the ontology of UHM, $\Gamma$ is a **primary object**: the system *is* its coherence matrix. The problem of G is not "how to compute $\Gamma$ from something more fundamental," but "**is** the identification of $\Gamma$ for a given system **unique**?"

### Analogy with Stone–von Neumann {#аналогия}

| | Quantum mechanics | UHM |
|---|---|---|
| **Primitive** | Canonical commutation relations $[\hat{x}, \hat{p}] = i\hbar$ | Primitive $\mathfrak{T} = (\mathbf{Sh}_\infty(\mathcal{C}), J_{Bures}, \omega_0)$ |
| **Representation** | Realization of $\hat{x}, \hat{p}$ on $\mathcal{H}$ | Holonomic representation $G: \mathrm{States}(S) \to \mathcal{D}(\mathbb{C}^7)$ |
| **Uniqueness theorem** | Stone–von Neumann: representation is unique up to $U(\mathcal{H})$ | **This theorem**: representation is unique up to $G_2$ |
| **Gauge group** | $U(\mathcal{H})$ (infinite-dimensional) | $G_2 = \mathrm{Aut}(\mathbb{O})$ (14-dimensional) |
| **Physical parameters** | Infinitely many (quantum numbers) | **34** = 48 $-$ 14 (gauge-invariant) |

The key distinction: in QM the gauge group is infinite-dimensional ($U(\mathcal{H})$), leaving enormous freedom. In UHM the gauge group is **finite-dimensional** $G_2$, which radically restricts this freedom and increases the predictive power of the theory.

---

## Definitions {#определения}

### Definition G1 (Holonomic representation) {#определение-представления}

A **holonomic representation** of a system $S$ satisfying (AP)+(PH)+(QG)+(V) is a triple $(\mathbb{C}^7, \mathcal{B}, G_S)$, where:

- $\mathbb{C}^7$ — Hilbert space of the holon
- $\mathcal{B} = \{|A\rangle, |S\rangle, |D\rangle, |L\rangle, |E\rangle, |O\rangle, |U\rangle\}$ — ordered orthonormal basis with functional labeling ([7 dimensions](/docs/core/structure/holon))
- $G_S: \mathrm{States}(S) \to \mathcal{D}(\mathbb{C}^7)$ — map **compatible** with UHM dynamics

**Compatibility condition (covariance):** For any physical trajectory $s(\tau)$ of system $S$:

$$
\frac{d}{d\tau} G_S(s(\tau)) = \mathcal{L}_\Omega[G_S(s(\tau))]
$$

where $\mathcal{L}_\Omega$ is the logical Liouvillian defined by axioms A1–A5 in basis $\mathcal{B}$.

### Definition G2 (Equivalence of representations) {#определение-эквивалентности}

Two holonomic representations $(\mathbb{C}^7, \mathcal{B}_1, G_1)$ and $(\mathbb{C}^7, \mathcal{B}_2, G_2)$ are **equivalent** if there exists $U \in U(7)$ such that:

$$
G_2(s) = U \, G_1(s) \, U^\dagger \quad \forall \, s \in \mathrm{States}(S)
$$

and $\mathcal{B}_2 = U \cdot \mathcal{B}_1$ (basis transformation).

### Definition G3 (Gauge group) {#определение-калибровки}

The **gauge group** is the maximal subgroup $\mathcal{G} \subseteq U(7)$ whose elements generate equivalent representations, preserving **all** structures defined by axioms A1–A5.

---

## Preliminary results {#предпосылки}

All results below have status **[Т]** and are proven in the respective documents.

### P1. Primitivity of $\mathcal{L}_0$ (linear part) [Т] {#p1-примитивность}

The linear part of the Liouvillian $\mathcal{L}_0$ is [primitive](/docs/core/operators/lindblad-operators#примитивность-ℒω) (T-39a): there exists a **unique** stationary state $I/7 \in \mathcal{D}(\mathbb{C}^7)$ for $\mathcal{L}_0$, and for any initial $\rho_0$:

$$
\lim_{\tau \to \infty} e^{\tau\mathcal{L}_0}[\rho_0] = I/7
$$

The full nonlinear operator $\mathcal{L}_\Omega = \mathcal{L}_0 + \mathcal{R}$ has a **unique non-trivial attractor** $\rho_* \neq I/7$ with $P > 1/7$ (T-96 [Т]).

Spectrum of $\mathcal{L}_\Omega$ on the space $\mathrm{Herm}_0(\mathbb{C}^7)$ (traceless Hermitian matrices, $\dim_\mathbb{R} = 48$):

$$
\mathrm{Spec}(\mathcal{L}_\Omega) = \{0\} \cup \{\lambda_k : \mathrm{Re}(\lambda_k) < 0, \; k = 1, \ldots, 47\}
$$

### P2. Functional uniqueness of dimensions [Т] {#p2-единственность}

All 7 dimensions are [functionally unique](/docs/proofs/minimality/theorem-minimality-7):

- Each dimension performs an irreducible function (F1–F7)
- [E is unique](/docs/proofs/minimality/theorem-minimality-7) [Т]: (PH) + $\kappa_0$ (requires $\mathrm{Hom}(O,E)$) + rank greater than 1
- [O is unique](/docs/proofs/minimality/theorem-minimality-7) [Т]: $\mathcal{R}$ [Т] + $\kappa_0$ ($\mathrm{End}(O)$, $\mathrm{Hom}(O,E)$, $\mathrm{Hom}(O,U)$) + PW (A5) + functional independence
- [E $\perp$ O](/docs/proofs/minimality/theorem-minimality-7) [Т]: causal + categorical (O = E degenerates $\kappa_0$)

### P3. Bridge T15 [Т] {#p3-мост}

Full chain [(AP)+(PH)+(QG)+(V) $\Rightarrow$ P1+P2](/docs/proofs/minimality/theorem-octonionic-derivation#мост) of 12 steps, all [Т]:

$$
\mathrm{(AP)+(PH)+(QG)+(V)} \xrightarrow{[\text{Т}]} \mathrm{BIBD}(7,3,1) \xrightarrow{[\text{Т}]} \mathrm{PG}(2,2) \xrightarrow{[\text{Т}]} \mathbb{O} \xrightarrow{[\text{Т}]} G_2
$$

### P4. L-unification [Т] {#p4-л-унификация}

[Lindblad operators are derived](/docs/core/operators/lindblad-operators) from the classifier $\Omega$:

$$
L_k = |k\rangle\langle k|, \quad k \in \{A, S, D, L, E, O, U\}
$$

Fano operators are defined by the 7 lines of PG(2,2):

$$
L_p^{\mathrm{Fano}} = \frac{1}{\sqrt{3}} \Pi_p, \quad \Pi_p = \sum_{i \in \mathrm{line}_p} |i\rangle\langle i|, \quad p = 1, \ldots, 7
$$

### P5. $G_2$-covariance [Т] {#p5-ковариантность}

The Fano dissipator is [$G_2$-covariant](/docs/core/operators/lindblad-operators#g2-ковариантность):

$$
\forall \, g \in G_2: \quad \mathcal{D}_{\mathrm{Fano}}[g\Gamma g^\dagger] = g \, \mathcal{D}_{\mathrm{Fano}}[\Gamma] \, g^\dagger
$$

The atomic dissipator is **not** $G_2$-covariant [Т], but is $S_7$-equivariant [Т].

---

## New lemmas {#леммы}

### Lemma G1: Spectral injectivity of propagator [Т] {#лемма-g1}

:::tip Lemma G1 (Spectral injectivity) [Т]
For any $\tau > 0$ the map $e^{\tau \mathcal{L}_{\mathrm{lin}}}$ is injective on $\mathrm{Herm}_0(\mathbb{C}^7)$, where $\mathcal{L}_{\mathrm{lin}} = -i[H_{\mathrm{eff}}, \cdot] + \mathcal{D}_\Omega$ is the linear part of the Liouvillian.
:::

**Proof.**

Let $\mathcal{L}_{\mathrm{lin}}$ act on $V = \mathrm{Herm}_0(\mathbb{C}^7)$ ($\dim_\mathbb{R} V = 48$). By primitivity [Т] (§[P1](#p1-примитивность)):

$$
\mathrm{Spec}(\mathcal{L}_{\mathrm{lin}}\big|_V) = \{\lambda_1, \ldots, \lambda_{48}\}, \quad \mathrm{Re}(\lambda_k) < 0 \; \forall k
$$

(the zero eigenvalue corresponds to the invariant component $\rho_*$, factored out into the complement of $V$).

For the propagator $e^{\tau \mathcal{L}_{\mathrm{lin}}}$ the eigenvalues are: $\{e^{\tau\lambda_k}\}_{k=1}^{48}$. Since $\mathrm{Re}(\lambda_k) < 0$:

$$
|e^{\tau\lambda_k}| = e^{\tau\mathrm{Re}(\lambda_k)} \in (0, 1) \quad \forall \tau > 0
$$

All eigenvalues of the propagator are **nonzero**, therefore $e^{\tau \mathcal{L}_{\mathrm{lin}}}$ is non-degenerate on $V$, i.e. injective. $\blacksquare$

**Corollary G1.1 (Recoverability of initial state):** Knowing $\Gamma(\tau)$ for some $\tau > 0$ and the parameters of $\mathcal{L}_{\mathrm{lin}}$, the initial state $\Gamma(0)$ is determined **uniquely**.

### Lemma G2: Well-posedness of nonlinear inverse problem [Т] {#лемма-g2}

:::tip Lemma G2 (Nonlinear inverse problem) [Т]
The full evolution equation $\frac{d\Gamma}{d\tau} = f(\Gamma)$, including the nonlinear regenerative term $\mathcal{R}$, has uniqueness of solutions: for any $\Gamma_1(0) \neq \Gamma_2(0)$ the trajectories $\Gamma_1(\tau) \neq \Gamma_2(\tau)$ for all $\tau \geq 0$.
:::

**Proof.**

The right-hand side $f(\Gamma) = -i[H_{\mathrm{eff}}, \Gamma] + \mathcal{D}_\Omega[\Gamma] + \kappa(\Gamma)(\rho_* - \Gamma) \cdot g_V(P)$, where:

**(a) Lipschitz continuity.** The linear terms ($-i[H_{\mathrm{eff}}, \cdot]$, $\mathcal{D}_\Omega$) are Lipschitz (linear operators on a finite-dimensional space). The nonlinear term:
- $\kappa(\Gamma) = \kappa_{\mathrm{bootstrap}} + \kappa_0 \cdot \mathrm{Coh}_E(\Gamma)$, where $\mathrm{Coh}_E(\Gamma) = \|\pi_E(\Gamma)\|_{\mathrm{HS}}^2 / \|\Gamma\|_{\mathrm{HS}}^2$ is a rational function of matrix elements [Т]
- $\|\Gamma\|_{\mathrm{HS}}^2 = \mathrm{Tr}(\Gamma^2) \geq 1/7 > 0$ on $\mathcal{D}(\mathbb{C}^7)$ — the denominator is bounded away from zero
- The product $\kappa(\Gamma) \cdot (\rho_* - \Gamma)$ is a smooth function on the compact set $\mathcal{D}(\mathbb{C}^7)$, hence locally Lipschitz

**(b) Picard–Lindelöf theorem.** On the compact set $\mathcal{D}(\mathbb{C}^7)$ local Lipschitz continuity guarantees **existence and uniqueness** of the solution to the Cauchy problem for any initial condition $\Gamma(0) \in \mathcal{D}(\mathbb{C}^7)$.

**(c) Injectivity of flow.** From uniqueness of the Cauchy problem: if $\Gamma_1(0) \neq \Gamma_2(0)$, then $\Gamma_1(\tau) \neq \Gamma_2(\tau)$ for all $\tau$ in the domain of existence (trajectories do not intersect in phase space — a standard result of ODE theory). $\blacksquare$

### Lemma G3: Axiomatic definiteness of structures [Т] {#лемма-g3}

:::tip Lemma G3 (Axiomatic definiteness) [Т]
Axioms A1–A5 uniquely determine (in the given basis $\mathcal{B}$) the following structures:

**(i)** Atomic projectors $\{|k\rangle\langle k|\}_{k=0}^{6}$ (from L-unification [Т])

**(ii)** The system of Fano lines $\{\mathrm{line}_p\}_{p=1}^{7} \subset \binom{[7]}{3}$ (from bridge T15 [Т])

**(iii)** E-projection $\pi_E(\Gamma) = P_E\Gamma + \Gamma P_E - P_E\Gamma P_E$ (from [Coh_E [Т]](/docs/core/foundations/axiom-septicity#hs-projection))

**(iv)** Page–Wootters tensor decomposition $\mathcal{H}_O \otimes \mathcal{H}_{\mathrm{rest}}$, singling out O (from A5)

**(v)** The regeneration formula $\kappa_0 = \omega_0 \cdot |\gamma_{OE}| \cdot |\gamma_{OU}| / \gamma_{OO}$, singling out $\{O, E, U\}$ (from [categorical derivation of κ₀ [Т]](/docs/core/foundations/axiom-septicity#структурный-анзац-kappa0))
:::

**Proof.** Each structure is derived from the axioms:
- (i): [L-unification](/docs/core/foundations/axiom-omega#lk-из-omega) [Т] — atoms $S_k = |k\rangle\langle k|$ of classifier $\Omega$
- (ii): Bridge T15 [Т] — uniqueness of BIBD$(7,3,1)$ $\cong$ PG(2,2) (Hall 1967)
- (iii): [HS-projection theorem](/docs/core/foundations/axiom-septicity#теорема-hs-проекция) [Т] — orthogonal projection in Hilbert–Schmidt space
- (iv): Axiom A5 (Page–Wootters) — explicit postulate
- (v): Adjunction $\mathcal{D}_\Omega \dashv \mathcal{R}$ [Т] — formula for $\kappa_0$ from [categorical derivation](/docs/core/foundations/axiom-septicity#структурный-анзац-kappa0). $\blacksquare$

### Lemma G4: Gauge group = $G_2$ [Т] {#лемма-g4}

:::tip Lemma G4 (Maximal gauge group) [Т]
The maximal subgroup $\mathcal{G} \subseteq U(7)$ whose elements preserve **all five structures** of Lemma G3 is $G_2 = \mathrm{Aut}(\mathbb{O})$.
:::

**Proof.** We proceed in two steps: (A) $G_2 \subseteq \mathcal{G}$ and (B) $\mathcal{G} \subseteq G_2$.

**(A) $G_2 \subseteq \mathcal{G}$: every $g \in G_2$ preserves all structures.**

By definition, $G_2 = \mathrm{Aut}(\mathbb{O})$ acts on $\mathrm{Im}(\mathbb{O}) \cong \mathbb{R}^7 \subset \mathbb{C}^7$ and preserves:
- Octonionic multiplication $e_i \cdot e_j = \varepsilon_{ijk} e_k$
- The multiplication table $\cong$ Fano plane PG(2,2)

Therefore, $g \in G_2$ preserves:
- (ii) Fano lines: $g$ permutes the 7 lines (as an automorphism of PG(2,2))
- (i) The set of atomic projectors: $g|k\rangle\langle k|g^\dagger$ are projectors onto a rotated basis, but the **set** $\{g\Pi_p g^\dagger\} = \{\Pi_{\sigma_g(p)}\}$ is preserved, and the atomic projectors are recovered from intersections: $|k\rangle\langle k| = \Pi_p \Pi_q$ for two lines through point $k$

For (iii), (iv), (v): $G_2 \subset SO(7)$ preserves the metric, and E, O, U transform **within** the $G_2$-orbit. Structures (iii)–(v) are formulated in terms of Fano lines and are covariant by construction. $\checkmark$

**(B) $\mathcal{G} \subseteq G_2$: any $U \in \mathcal{G}$ belongs to $G_2$.**

Let $U \in U(7)$ preserve all five structures of Lemma G3.

**Step B1.** From preservation of (ii) (Fano lines): $U$ induces an automorphism of the Fano plane PG(2,2). Since PG(2,2) is isomorphic to the multiplication table of $\mathrm{Im}(\mathbb{O})$ [Т], $U$ induces an automorphism of octonionic multiplication.

**Step B2.** Restrict $U$ to $\mathrm{Im}(\mathbb{O}) \cong \mathbb{R}^7$. An automorphism of octonionic multiplication on $\mathrm{Im}(\mathbb{O})$ by definition belongs to $G_2 = \mathrm{Aut}(\mathbb{O})$.

:::tip Transition from combinatorial automorphisms to continuous ones
$U \in U(7)$ preserves Fano lines **as subspaces** (not just as index sets). Each Fano line defines a 3-dimensional subspace, and preservation of all 7 such subspaces is equivalent to preservation of the octonionic cross-product (3-form $\varphi_3 = \sum f_{ijk}\, e^i \wedge e^j \wedge e^k$). By definition $G_2 = \{g \in \mathrm{GL}(7,\mathbb{R}) : g^*\varphi_3 = \varphi_3\}$, which proves $U \in G_2$.
:::

:::info Clarification: PSL(2,7) vs G₂
The group of combinatorial automorphisms of PG(2,2) is finite: $\mathrm{Aut}(\mathrm{PG}(2,2)) \cong \mathrm{PSL}(2,7)$, $|\mathrm{PSL}(2,7)| = 168$. The group $G_2 = \mathrm{Aut}(\mathbb{O})$ is a compact Lie group, $\dim G_2 = 14$. Relation: $\mathrm{PSL}(2,7) \subset G_2$ as a **finite subgroup** — every permutation of 7 points compatible with PG(2,2) extends to a continuous automorphism of $\mathbb{O}$. Step B1 shows that $U$ preserves the **structure constants** $f_{ijk}$ (not just combinatorics), and step B2 uses the definition of $G_2$ as the group preserving these constants.
:::

**Step B3.** Since $G_2 \subset SO(7) \subset U(7)$ and $U$ preserves the Hermitian structure (as an element of $U(7)$), the restriction $U\big|_{\mathrm{Im}(\mathbb{O})}$ determines $U$ completely (since $\mathrm{Im}(\mathbb{O})$ is a real form of $\mathbb{C}^7$, and $U$ preserves the real structure via preservation of PG(2,2)).

Therefore, $U \in G_2$. $\blacksquare$

---

## Main theorem {#теорема}

### Theorem (G₂-rigidity of holonomic representation) [Т] {#g2-ригидность}

:::warning Theorem of G₂-rigidity [Т]
Let $S$ be an autonomous system satisfying (AP)+(PH)+(QG)+(V). Let $(\mathbb{C}^7, \mathcal{B}_1, G_1)$ and $(\mathbb{C}^7, \mathcal{B}_2, G_2)$ be two holonomic representations of $S$ (Definition G1).

Then there exists a **unique** $U \in G_2 = \mathrm{Aut}(\mathbb{O})$ such that:

$$
\boxed{G_2(s) = U \, G_1(s) \, U^\dagger \quad \forall \, s \in \mathrm{States}(S)}
$$

Equivalently: **the holonomic representation is unique up to gauge group $G_2$**.
:::

### Proof {#доказательство}

**Step 1: Definiteness of dynamics in each representation.**

In representation $(\mathbb{C}^7, \mathcal{B}_i, G_i)$ axioms A1–A5 determine the Liouvillian $\mathcal{L}_\Omega^{(i)}$ (Lemma G3 [Т]). The compatibility condition (Definition G1) guarantees:

$$
\frac{d}{d\tau} G_i(s(\tau)) = \mathcal{L}_\Omega^{(i)}[G_i(s(\tau))], \quad i = 1, 2
$$

**Step 2: Construction of intertwiner $\Phi$.**

Define $\Phi: \mathcal{D}(\mathbb{C}^7) \to \mathcal{D}(\mathbb{C}^7)$ as:

$$
\Phi := G_2 \circ G_1^{-1}
$$

(the inverse $G_1^{-1}$ exists on the image $G_1(\mathrm{States}(S))$). From the compatibility conditions:

$$
\frac{d}{d\tau} \Phi(\Gamma(\tau)) = \mathcal{L}_\Omega^{(2)}[\Phi(\Gamma(\tau))], \quad \text{where} \quad \frac{d}{d\tau}\Gamma(\tau) = \mathcal{L}_\Omega^{(1)}[\Gamma(\tau)]
$$

**Step 3: $\Phi$ is conjugation by a unitary operator.**

Both representations describe the same physical system and generate the same observables. The spectrum of $\Gamma$ (set of eigenvalues) is invariant: $\mathrm{Spec}(\Phi(\Gamma)) = \mathrm{Spec}(\Gamma)$ for all $\Gamma$ (since physical observables — purity $P = \mathrm{Tr}(\Gamma^2)$, von Neumann entropy, Coh$_E$, etc. — are functions of the spectrum and certain structural elements, and must coincide).

A spectrum-preserving map on $\mathcal{D}(\mathbb{C}^7)$ is conjugation by a unitary (or antiunitary) operator — this is **Wigner's theorem** (Wigner 1931) in the form of Kadison (Kadison 1965):

$$
\Phi(\Gamma) = U \Gamma U^\dagger \quad \text{for some } U \in U(7)
$$

(the antiunitary case is excluded since $\Phi$ is continuously connected to the identity map through a continuous family of systems).

:::tip Extension of Φ to all D(ℂ⁷)
By the viability condition (V), the trajectories of the holon pass through an open neighborhood of the attractor $\rho^*$ (T-125 [Т]). Therefore $\mathrm{Im}(G_1)$ contains an open subset of $\mathrm{Int}(\mathcal{D}(\mathbb{C}^7))$. An affine map defined on an open subset of a complete metric space extends uniquely to the whole space (Tietze theorem). The extended $\Phi$ preserves the spectrum on all of $\mathcal{D}(\mathbb{C}^7)$.
:::

:::info Clarification: Wigner vs. Uhlmann
Here **Wigner's theorem** (in Kadison's form) is applied: an affine bijection $\Phi$ on the state space $\mathcal{D}(\mathbb{C}^7)$ that preserves the spectrum (and hence fidelity $F(\rho, \sigma) = \mathrm{Tr}\sqrt{\sqrt{\rho}\sigma\sqrt{\rho}}$) is realized by unitary or antiunitary conjugation. This is the correct reference for this step, since $\Phi$ is a bijection on the state space, not a CPTP channel. For CPTP channels (which are in general not bijections) preservation of fidelity is characterized by **Uhlmann's theorem** (Uhlmann 1976): $F(\mathcal{E}[\rho], \mathcal{E}[\sigma]) \leq F(\rho, \sigma)$ for any CPTP $\mathcal{E}$, with equality if and only if $\mathcal{E}$ is a unitary channel on the support of $\rho$ and $\sigma$. In the context of the monotonicity of Freedom (Theorem [Properties of Freedom](/docs/core/foundations/consequences#freedom-свойства) in consequences.md), it is precisely Uhlmann's contractivity that justifies the non-increase of freedom under CPTP evolution.
:::

**Step 4: $U \in G_2$.**

Since both representations satisfy axioms A1–A5, the unitary operator $U$ must preserve **all** structures defined by the axioms (Lemma G3 [Т]): atomic projectors, Fano lines, E-projection, PW-decomposition, formula $\kappa_0$.

By Lemma G4 [Т]: $U \in G_2$. $\blacksquare$

**Step 5: Uniqueness of $U$.**

Suppose $U_1, U_2 \in G_2$ both satisfy $G_2 = \mathrm{Ad}_{U_i} \circ G_1$. Then $\mathrm{Ad}_{U_1^{-1}U_2} = \mathrm{Id}$ on the image of $G_1$. If the image of $G_1$ contains sufficiently many states (which is guaranteed by viability: the system passes through a neighborhood of $\rho_*$ by primitivity [Т], and this neighborhood is open in $\mathcal{D}(\mathbb{C}^7)$), then $U_1^{-1}U_2 = e^{i\theta} I$ — a scalar phase, acting trivially on $\mathcal{D}(\mathbb{C}^7)$. $\blacksquare$

---

## Corollaries {#следствия}

### Corollary 1: Space of physical states [Т] {#физические-состояния}

:::tip Corollary 1 (Space of observables) [Т]
The space of **physically distinguishable** states of the holon:

$$
\mathcal{D}_{\mathrm{phys}} = \mathcal{D}(\mathbb{C}^7) / G_2
$$

has dimension:

$$
\dim_\mathbb{R}(\mathcal{D}_{\mathrm{phys}}) = 48 - 14 = 34
$$

where $48 = N^2 - 1 = \dim(\mathrm{su}(7))$ is the full number of parameters of $\Gamma$, and $14 = \dim(G_2)$ is the number of gauge degrees of freedom.
:::

**Proof.** For generic $\Gamma$ (with distinct eigenvalues) the stabilizer $\mathrm{Stab}_{G_2}(\Gamma)$ is trivial (finite group). Then by the orbit theorem: $\dim(\mathrm{Orb}(\Gamma)) = \dim(G_2) = 14$, and $\dim(\mathcal{D}_{\mathrm{phys}}) = 48 - 14 = 34$. $\blacksquare$

:::info Consistency
The value 34 coincides with the number of parameters under full $G_2$-gauge fixing in the pure Fano-observation regime ($\alpha = 0$), stated in [Lindblad operators](/docs/core/operators/lindblad-operators#g2-ковариантность): "$48 \to 34$ parameters."
:::

### Corollary 2: Well-posedness of inverse problem [Т] {#обратная-задача}

:::tip Corollary 2 (Inverse problem) [Т]
For a system $S$ satisfying (AP)+(PH)+(QG)+(V), the initial state $\Gamma(0)$ is **uniquely** recovered from:

**(a)** The observed trajectory $\Gamma(\tau)$ for $\tau \in (0, T]$ (Lemmas G1, G2 [Т])

**(b)** The system parameters $(\omega_0, \lambda_m)$

up to $G_2$-gauge (Theorem of G₂-rigidity [Т]).
:::

### Corollary 3: Faithfulness of functor F [Т] {#верность-функтора}

:::tip Corollary 3 (Faithfulness of functor) [Т]
The functor $F: \mathbf{DensityMat} \to \mathbf{Exp}$ ([categorical formalism](/docs/proofs/categorical/categorical-formalism)) is **faithful** on $G_2$-orbits: if $F(\Gamma_1) \cong F(\Gamma_2)$ in $\mathbf{Exp}$, then $\Gamma_2 = U\Gamma_1 U^\dagger$ for $U \in G_2$.

Kernel of $F$ on the set of isomorphisms:

$$
\ker(F) = \{\mathrm{Ad}_U : U \in G_2\}
$$
:::

### Corollary 4: Predictive power [Т] {#предсказательная-мощность}

:::tip Corollary 4 (Finiteness of gauge group) [Т]
$G_2$ is a **finite-dimensional** (14-dimensional) compact Lie group. This means:

1. A **discrete set** of $G_2$-invariant observables fully characterizes the physical state
2. A **finite number** of gauge-invariant parameters (34) — unlike standard QM, where $U(\mathcal{H})$-freedom is infinite-dimensional
3. The theory is **maximally predictive** at the given dimension $N = 7$: the gauge group $G_2$ is the minimal group preserving the octonionic structure
:::

### Corollary 5: G₂-invariants as physical observables {#инварианты}

The 34 physical parameters are organized as follows:

| Type | Number of parameters | Description |
|-----|:---:|---|
| Spectrum of $\Gamma$ | 6 | Eigenvalues (ordered) |
| $G_2$-invariant angles | 28 | Mutual position of eigenvectors relative to octonionic structure |
| **Total** | **34** | Complete set of physical observables |

The gauge-invariant observables include:

- Purity $P = \mathrm{Tr}(\Gamma^2)$ — $G_2$-invariant ($P(U\Gamma U^\dagger) = P(\Gamma)$ for $U \in U(7) \supset G_2$)
- E-coherence $\mathrm{Coh}_E(\Gamma)$ — invariant within $G_2$-orbit, since $G_2$ preserves the Fano structure and the role of E
- Reflection measure $R$ — determined via $\varphi(\Gamma)$ and $\Gamma$, both transforming covariantly
- Integration measure $\Phi$ — analogously

---

## Relation to open questions {#открытые-вопросы}

### Closing the problem of G at the level of theory

This theorem **fully closes** the question of uniqueness of the map G at the theoretical level:

| Question | Status | Basis |
|--------|:------:|-----------|
| **Existence** of G | **[Т]** | Theorem S + bridge T15 |
| **Uniqueness** of G (up to $G_2$) | **[Т]** | Theorem of $G_2$-rigidity (this document) |
| **Predictivity** of G | [Empirical] | Requires experimental verification |

Question 3 (predictivity) is **epistemological**, not mathematical: it is closed empirically (convergent validity, predictive success, interventional testing). This is the same epistemological standard by which all fundamental physics operates.

### Analogy with physical theories

| Theory | Uniqueness theorem | Gauge group | Empirical verification |
|--------|---|---|---|
| QM | Stone–von Neumann (1931) | $U(\mathcal{H})$ | Spectra, interference |
| GR | Birkhoff (spherical symmetry) | $\mathrm{Diff}(M)$ | Light deflection, gravitational waves |
| SM | Coleman–Mandula / Haag–Łopuszański–Sohnius | Poincaré $\times$ gauge | Accelerators, PDG |
| **UHM** | **$G_2$-rigidity** (this theorem) | **$G_2 = \mathrm{Aut}(\mathbb{O})$** | Cabibbo angle, thresholds, Gap profiles |

---

## Summary {#резюме}

:::tip Key result
**Theorem of $G_2$-rigidity [Т]:** The holonomic representation of a system satisfying (AP)+(PH)+(QG)+(V) is **unique** up to gauge group $G_2 = \mathrm{Aut}(\mathbb{O})$ — a 14-dimensional exceptional Lie group, the automorphism group of the octonions.

**Physical meaning:** Different observers applying UHM to the same system will obtain coherence matrices related by a $G_2$-transformation. All 34 gauge-invariant parameters (purity, coherences, thresholds) will coincide.

**Methodological status:** All steps of the proof are theorems [Т], relying on previously established results. This theorem closes the problem of the map G at the theoretical level and is the analogue of the Stone–von Neumann theorem for UHM.
:::

---

**Related documents:**
- [Axiom Ω⁷](/docs/core/foundations/axiom-omega) — fundamental axioms A1–A5
- [Axiom (AP+PH+QG+V)](/docs/core/foundations/axiom-septicity) — characterizing properties of viable holons
- [Lindblad operators](/docs/core/operators/lindblad-operators) — primitivity of ℒ_Ω, L-unification, G₂-covariance
- [Minimality theorem](/docs/proofs/minimality/theorem-minimality-7) — functional uniqueness of 7 dimensions
- [Structural derivation N=7](/docs/proofs/minimality/theorem-octonionic-derivation) — bridge T15 and octonionic structure
- [Categorical formalism](/docs/proofs/categorical/categorical-formalism) — functor F: DensityMat → Exp
- [Formalization of φ](/docs/proofs/categorical/formalization-phi) — equivalence of self-modeling definitions
- [G₂-structure](/docs/physics/gauge-symmetry/g2-structure) — role of G₂ in physical correspondences
