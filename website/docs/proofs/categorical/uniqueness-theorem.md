---
slug: /proofs/categorical/uniqueness-theorem
sidebar_position: 3
title: "Uniqueness theorem of representation"
description: "G₂-rigidity of holonomic representation: uniqueness of the map G up to gauge group G₂ = Aut(O). Analogue of the Stone–von Neumann theorem for UHM."
---

# Uniqueness Theorem of Holonomic Representation

:::tip Status: [T] — the octonionic structure follows from the axioms with the canonical orientation (T15-canon)
The uniqueness theorem of holonomic representation is a **theorem [T]** about $\mathbb{C}^7$ carrying the octonionic multiplication of the oriented Fano plane. From the axioms that structure follows through the bridge T15 (registry row 41n) with the canonical orientation of the Fano lines — the unique orientation class invariant under the collineations of the design ([T15-canon](/docs/proofs/minimality/theorem-octonionic-derivation#каноническая-ориентация)) — so the theorem is **[T]** as a consequence of the axioms. Earlier on 2026-09-25 this box read "[T] given the octonionic structure; that structure is [C at (Alt)]"; that orientation input is discharged. Before that it read "[T] — all steps proven, relying exclusively on previously proven results". It relies on:
- Primitivity of $\mathcal{L}_\Omega$ [T] ([proof](/docs/core/operators/lindblad-operators#примитивность-ℒω))
- Full minimality 7/7 [T] ([proof](/docs/proofs/minimality/theorem-minimality-7))
- Bridge T15 [T]: (AP)+(PH)+(QG)+(V) $\Rightarrow$ BIBD(7,3,1) = PG(2,2) [T] $\Rightarrow$ $\mathbb{O}$ (canonical orientation, T15-canon [T]) $\Rightarrow$ $G_2$ ([proof](/docs/proofs/minimality/theorem-octonionic-derivation#мост))
- L-unification [T] ([proof](/docs/core/operators/lindblad-operators))
- Uniqueness of E, O, U [T] ([proof](/docs/proofs/minimality/theorem-minimality-7))
:::

:::warning Frame decision D-0910 — two groups, one representation (single source of truth)
The corpus uses $G_2$ in two roles that must not be conflated; this box fixes the split, and every other page defers to it.

1. **Kinematic rigidity.** The maximal subgroup of $U(7)$ preserving the octonionic 3-form $\varphi_3$ is $G_2 = \mathrm{Aut}(\mathbb{O})$ (Lemma G4). Two holonomic representations of one system can differ by an element of $G_2$ — never by more. This is the content of the theorem below, and it fixes the count $34 = 48 - 14$ of $G_2$-orbit invariants of the *kinematic* state (spectrum + $\varphi_3$-relative angles).
2. **Dynamical identification.** The axiomatic dynamics $\mathcal{L}_\Omega$ — pinching dissipator $\mathcal{D}_{\mathrm{Fano}} = \tfrac23\mathcal{D}_{\mathrm{atom}}$, the regeneration coefficient $\kappa_0$, the PW clock — is **not** $G_2$-covariant: it breaks $G_2$ to the finite octonionic frame group $\Gamma_{\!\text{oct}} \subset G_2$ ([Theorem 5.1b](/docs/proofs/gap/fano-channel#g2-ковариантность) [T]; $\Gamma_{\!\text{oct}} = 2^3 \!\cdot\! \mathrm{PSL}(3,2)$, order $1344$ — the 168 Fano-line-preserving basis permutations together with the 8 sign patterns constant on Fano lines; see [frame rigidity](#жёсткость-репера)). Hence the transformations relating *physically indistinguishable* descriptions of one holon form $\Gamma_{\!\text{oct}}$, not the 14-dimensional $G_2$: **all 48 real parameters of $\Gamma$ are physical** (modulo a finite relabelling of axes), and the frame-pinned observables $\Phi$, $\mathrm{Coh}_E$, $\kappa_0$ are physical observables with well-defined thresholds ($\Phi \geq 1$, $\mathrm{Coh}_E > 1/7$).

Consequently, wherever the corpus says "34 physical parameters", "states related by $G_2$ are physically identical" or "$\Phi$, $\mathrm{Coh}_E$ are $G_2$-invariant", the statement is to be read through this decision: 34 counts kinematic $G_2$-invariants; physical identity is $\Gamma_{\!\text{oct}}$-identity; $\Phi$ and $\mathrm{Coh}_E$ are frame-pinned, not $G_2$-invariant (an explicit $g \in G_2$ with $g e_1 = (e_1 + e_2)/\sqrt2$ sends $\Phi(|e_1\rangle\langle e_1|) = 0$ to $1$ and $\mathrm{Coh}_E$ from $1$ to $3/4$; a full rotation $e_1 \mapsto e_2$ sends $\mathrm{Coh}_E$ to $0$). $G_2$ keeps its *physical* role as the structure group of the octonionic sector: $SU(3)_C = \mathrm{Stab}_{G_2}(e_O)$, the Fano selection rules, and the decomposition $48 = 27 \oplus 14 \oplus 7$ (T-301).

**This is not a choice among options: it is forced.** The theorem below shows that $\Phi$ is preserved by *no* continuous group at all, so any reading on which the L2 condition $\Phi \geq 1$ is a physical condition must take a discrete identification group. See [frame rigidity](#жёсткость-репера).
:::

### Theorem (Frame rigidity: $\Phi$ admits no continuous symmetry) [T] {#жёсткость-репера}

:::warning Theorem (frame rigidity) [T]
Let $\Phi(\Gamma) = \sum_{i \neq j}|\gamma_{ij}|^2 / \sum_i \gamma_{ii}^2$ be the integration measure. Then the largest subgroup of $O(7)$ preserving $\Phi$ on all states is the **hyperoctahedral group** of signed permutations; its intersection with $G_2$ is the finite octonionic frame group $\Gamma_{\!\text{oct}}$, of order

$$
|\Gamma_{\!\text{oct}}| = 1344 = 2^3 \cdot |\mathrm{PSL}(3,2)| = 8 \cdot 168,
$$

the maximal subgroup $2^3 \!\cdot\! \mathrm{PSL}(3,2) \subset G_2$. In particular **no continuous subgroup of $G_2$ (or even of $SO(7)$) preserves $\Phi$**: $\dim\{X \in \mathfrak{g}_2 : \delta_X\Phi = 0\} = 0$.
:::

**Proof.** On real pure states $\Gamma = vv^{\mathsf T}$, $\|v\|_2 = 1$, one has $\sum_i\gamma_{ii}^2 = \sum_i v_i^4 = \|v\|_4^4$ and $\sum_{ij}|\gamma_{ij}|^2 = 1$, hence

$$
\Phi(vv^{\mathsf T}) = \frac{1 - \|v\|_4^4}{\|v\|_4^4},
$$

a strictly decreasing function of $\|v\|_4$. So a linear map preserving $\Phi$ on this family preserves the $\ell^4$-norm on the unit $\ell^2$-sphere and, by homogeneity, on all of $\mathbb{R}^7$. By the **Banach–Lamperti theorem** (the linear isometries of $\ell^p$, $p \neq 2$, are exactly the signed permutations of coordinates) such a map is a signed permutation. Signed permutations preserving the associative 3-form $\varphi_3$ form $\Gamma_{\!\text{oct}}$: the permutation part must be a collineation of $PG(2,2)$ ($|{\rm PSL}(3,2)| = 168$) and the sign part must satisfy $\varepsilon_i\varepsilon_j\varepsilon_k = 1$ on each Fano line — the simplex code $[7,3]$, of size $2^3 = 8$. Conversely every such map preserves both $\varphi_3$ and the coordinate diagonal, hence $\Phi$. $\blacksquare$

**Machine verification** (2026-09-10). Exhaustive enumeration over signed permutations: $|\Gamma_{\!\text{oct}}| = 1344$, with exactly $168$ distinct permutation parts and a sign-only subgroup of order $8$; permutation parts of order 7: $48$, i.e. $8$ Singer subgroups of $\mathrm{PSL}(3,2)$ (in $\Gamma_{\!\text{oct}}$ itself each lifts eight times: $384$ elements of order 7; clarified 2026-09-25). First-order rigidity by least squares over random pure states: $\dim\{X \in \mathfrak{so}(7): \delta_X\Phi = 0\} = 0$ and $\dim\{X \in \mathfrak{g}_2: \delta_X\Phi = 0\} = 0$. The identity $\Phi = (1 - \|v\|_4^4)/\|v\|_4^4$ was checked to $10^{-15}$.

:::info The lattice of candidate identification groups
Every candidate for "which transformations relate physically indistinguishable descriptions" is a subgroup of $G_2$; there are four natural ones. The parameter count is $48 - \dim$ (generic orbit); invariance is stated for the frame-referenced observables. All rows are machine-verified.

| Identification group | $\dim$ | Parameters | $\mathrm{Coh}_E$ (No-Zombie) | $\Phi$ (L2) |
|---|:---:|:---:|---|---|
| $G_2$ | 14 | 34 | not invariant (witness: $1 \to 0.75$) | not invariant (witness: $0 \to 1$) |
| $SU(3) = \mathrm{Stab}_{G_2}(e_O)$ | 8 | 40 | not invariant (witness: $1 \to 0.45$) | not invariant (witness: $0 \to 2.19$) |
| $SU(2) = \mathrm{Stab}_{G_2}(e_E, e_O)$ | 3 | 45 | **invariant** | not invariant (witness: $0.690 \to 0.637$) |
| $\Gamma_{\!\text{oct}}$ (frame group) | 0 | 48 | invariant only under the $192$ of $1344$ elements that keep the $E$-axis (witness for the others: $1 \to 0$) | **invariant** (all $1344$) |

*Corrected 2026-09-25.* The frame-group row read "$\mathrm{Coh}_E$: **invariant**"; that is retracted: an element of $\Gamma_{\!\text{oct}}$ that moves the $E$-axis to another axis takes $\mathrm{Coh}_E(\lvert e_E\rangle\langle e_E\rvert)$ from $1$ to $0$, and exhaustive enumeration finds $\mathrm{Coh}_E$ preserved on exactly $192 = 1344/7$ elements — those that keep the $E$-axis ($96$ fix $e_E$, $96$ send it to $-e_E$) — while $\Phi$ is preserved on all $1344$ (regression test `test_coh_e_is_invariant_only_on_the_e_axis_stabiliser`).

Reading the lattice: $\mathrm{Coh}_E$ needs only a distinguished $E$-axis, so the No-Zombie threshold survives on the stabiliser of that axis — already at $SU(2)_{E,O}$, in fact on the whole eight-dimensional $\mathrm{Stab}_{G_2}(e_E) \cong SU(3)$ (a rotation fixing $e_E$ fixes $\gamma_{EE}$ and the norm of the $E$-row), and in the frame group only on its $E$-axis stabiliser. $\Phi$ survives **nowhere above the discrete row** — by the rigidity theorem this is not an artefact of the present definition of the window but of $\Phi$ itself. Hence the corpus takes the last row: the identification group is $\Gamma_{\!\text{oct}}$ and all 48 parameters are physical. (With the corrected row, the only group of the lattice that preserves both observables with the axes held fixed is the $E$-axis stabiliser inside $\Gamma_{\!\text{oct}}$, of order $192$; the frame decision takes $\Gamma_{\!\text{oct}}$ with the functional labels carried along with the axes, as in Step 4 of the proof below, so that $\mathrm{Coh}_E$ is read on the image of the $E$-axis.) The alternative — keeping a continuous group — is available only at the price of rewriting the L2 condition in invariants of that group (for $SU(2)_{E,O}$: 45 parameters, $\Phi$ replaced by an $SU(2)$-invariant), and the octonionic reading would then have to rebuild the phenomenology of the 21 pairs on $1 \oplus 27 \oplus 7 \oplus 14$.
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
| **Physical parameters** | Infinitely many (quantum numbers) | **48** (all, modulo the finite frame group $\Gamma_{\!\text{oct}}$); **34** = 48 $-$ 14 of them are kinematic $G_2$-orbit invariants (D-0910) |

The key distinction: in QM the gauge group is infinite-dimensional ($U(\mathcal{H})$), leaving enormous freedom. In UHM the kinematic gauge group is **finite-dimensional** $G_2$, which radically restricts this freedom and increases the predictive power of the theory — and the axiomatic dynamics narrows it further to the *finite* frame group $\Gamma_{\!\text{oct}}$ (frame decision D-0910 above).

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

All results below have status **[T]** and are proven in the respective documents.

### P1. Primitivity of $\mathcal{L}_0$ (linear part) [T] {#p1-примитивность}

The linear part of the Liouvillian $\mathcal{L}_0$ is [primitive](/docs/core/operators/lindblad-operators#примитивность-ℒω) (T-39a): there exists a **unique** stationary state $I/7 \in \mathcal{D}(\mathbb{C}^7)$ for $\mathcal{L}_0$, and for any initial $\rho_0$:

$$
\lim_{\tau \to \infty} e^{\tau\mathcal{L}_0}[\rho_0] = I/7
$$

The full nonlinear operator $\mathcal{L}_\Omega = \mathcal{L}_0 + \mathcal{R}$ has a **unique non-trivial attractor** $\rho_* \neq I/7$ with $P > 1/7$ (T-96 [T]).

Spectrum of $\mathcal{L}_\Omega$ on the space $\mathrm{Herm}_0(\mathbb{C}^7)$ (traceless Hermitian matrices, $\dim_\mathbb{R} = 48$):

$$
\mathrm{Spec}(\mathcal{L}_\Omega) = \{0\} \cup \{\lambda_k : \mathrm{Re}(\lambda_k) < 0, \; k = 1, \ldots, 47\}
$$

### P2. Functional uniqueness of dimensions [T] {#p2-единственность}

All 7 dimensions are [functionally unique](/docs/proofs/minimality/theorem-minimality-7):

- Each dimension performs an irreducible function (F1–F7)
- [E is unique](/docs/proofs/minimality/theorem-minimality-7) [T]: (PH) + $\kappa_0$ (requires $\mathrm{Hom}(O,E)$) + rank greater than 1
- [O is unique](/docs/proofs/minimality/theorem-minimality-7) [T]: $\mathcal{R}$ [T] + $\kappa_0$ ($\mathrm{End}(O)$, $\mathrm{Hom}(O,E)$, $\mathrm{Hom}(O,U)$) + PW (A5) + functional independence
- [E $\perp$ O](/docs/proofs/minimality/theorem-minimality-7) [T]: causal + categorical (O = E degenerates $\kappa_0$)

### P3. Bridge T15 [T] {#p3-мост}

Full chain [(AP)+(PH)+(QG)+(V) $\Rightarrow$ P1+P2](/docs/proofs/minimality/theorem-octonionic-derivation#мост) of 12 steps; the steps up to PG(2,2) are [T], and the step to $\mathbb{O}$ takes the canonical orientation of the seven lines: only 16 of the 128 orientations are normed, and they form the only orientation class the design itself determines ([T15-canon](/docs/proofs/minimality/theorem-octonionic-derivation#каноническая-ориентация); registry row 41n). The chain was stated as "all [T]" until 2026-09-25 without the orientation step, then as [C at (Alt)] the same day until T15-canon:

$$
\mathrm{(AP)+(PH)+(QG)+(V)} \xrightarrow{[\text{T}]} \mathrm{BIBD}(7,3,1) \xrightarrow{[\text{T}]} \mathrm{PG}(2,2) \xrightarrow{[\text{T}]\ \text{canonical orientation}} \mathbb{O} \xrightarrow{[\text{T}]} G_2
$$

### P4. L-unification [T] {#p4-л-унификация}

[Lindblad operators are derived](/docs/core/operators/lindblad-operators) from the classifier $\Omega$:

$$
L_k = |k\rangle\langle k|, \quad k \in \{A, S, D, L, E, O, U\}
$$

Fano operators are defined by the 7 lines of PG(2,2):

$$
L_p^{\mathrm{Fano}} = \frac{1}{\sqrt{3}} \Pi_p, \quad \Pi_p = \sum_{i \in \mathrm{line}_p} |i\rangle\langle i|, \quad p = 1, \ldots, 7
$$

### P5. Covariance groups of the dissipators [T] {#p5-ковариантность}

The Fano dissipator is **proportional** to the atomic one, $\mathcal{D}_{\mathrm{Fano}} = \tfrac23\,\mathcal{D}_{\mathrm{atom}}$ ([Theorem 5.1a](/docs/proofs/gap/fano-channel#g2-ковариантность) [T]), and therefore shares its symmetry group: both are covariant under the finite octonionic frame group $\Gamma_{\!\text{oct}} \subset G_2$ (and $S_7$-equivariant),

$$
\forall \, g \in \Gamma_{\!\text{oct}}: \quad \mathcal{D}_{\mathrm{Fano}}[g\Gamma g^\dagger] = g \, \mathcal{D}_{\mathrm{Fano}}[\Gamma] \, g^\dagger,
$$

and **neither** is covariant under the full continuous $G_2$ ([Theorem 5.1b](/docs/proofs/gap/fano-channel#g2-ковариантность) [T]; machine check: $\|\mathcal{D}_{\mathrm{Fano}}[g\Gamma g^\top] - g\,\mathcal{D}_{\mathrm{Fano}}[\Gamma]\,g^\top\| = 0.08$ against $\|\mathcal{D}_{\mathrm{Fano}}[\Gamma]\| = 0.25$ for a generic $g \in G_2$). The genuinely $G_2$-covariant dissipator $\mathcal{D}_{G_2}$ built from $\varphi_{abc}$ exists (Theorem 5.1c) but is not the axiomatic UHM dissipator. Hence $G_2$ is a symmetry of the *kinematics* (the 3-form), not of the dynamics — the frame decision D-0910 above. (Earlier drafts of this section stated "the Fano dissipator is $G_2$-covariant"; that statement is retracted.)

---

## New lemmas {#леммы}

### Lemma G1: Spectral injectivity of propagator [T] {#лемма-g1}

:::tip Lemma G1 (Spectral injectivity) [T]
For any $\tau > 0$ the map $e^{\tau \mathcal{L}_{\mathrm{lin}}}$ is injective on $\mathrm{Herm}_0(\mathbb{C}^7)$, where $\mathcal{L}_{\mathrm{lin}} = -i[H_{\mathrm{eff}}, \cdot] + \mathcal{D}_\Omega$ is the linear part of the Liouvillian.
:::

**Proof.**

Let $\mathcal{L}_{\mathrm{lin}}$ act on $V = \mathrm{Herm}_0(\mathbb{C}^7)$ ($\dim_\mathbb{R} V = 48$). By primitivity [T] (§[P1](#p1-примитивность)):

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

### Lemma G2: Well-posedness of nonlinear inverse problem [T] {#лемма-g2}

:::tip Lemma G2 (Nonlinear inverse problem) [T]
The full evolution equation $\frac{d\Gamma}{d\tau} = f(\Gamma)$, including the nonlinear regenerative term $\mathcal{R}$, has uniqueness of solutions: for any $\Gamma_1(0) \neq \Gamma_2(0)$ the trajectories $\Gamma_1(\tau) \neq \Gamma_2(\tau)$ for all $\tau \geq 0$.
:::

**Proof.**

The right-hand side $f(\Gamma) = -i[H_{\mathrm{eff}}, \Gamma] + \mathcal{D}_\Omega[\Gamma] + \kappa(\Gamma)(\rho_* - \Gamma) \cdot g_V(P)$, where:

**(a) Lipschitz continuity.** The linear terms ($-i[H_{\mathrm{eff}}, \cdot]$, $\mathcal{D}_\Omega$) are Lipschitz (linear operators on a finite-dimensional space). The nonlinear term:
- $\kappa(\Gamma) = \kappa_{\mathrm{bootstrap}} + \kappa_0 \cdot \mathrm{Coh}_E(\Gamma)$, where $\mathrm{Coh}_E(\Gamma) = \|\pi_E(\Gamma)\|_{\mathrm{HS}}^2 / \|\Gamma\|_{\mathrm{HS}}^2$ is a rational function of matrix elements [T]
- $\|\Gamma\|_{\mathrm{HS}}^2 = \mathrm{Tr}(\Gamma^2) \geq 1/7 > 0$ on $\mathcal{D}(\mathbb{C}^7)$ — the denominator is bounded away from zero
- The product $\kappa(\Gamma) \cdot (\rho_* - \Gamma)$ is a smooth function on the compact set $\mathcal{D}(\mathbb{C}^7)$, hence locally Lipschitz

**(b) Picard–Lindelöf theorem.** On the compact set $\mathcal{D}(\mathbb{C}^7)$ local Lipschitz continuity guarantees **existence and uniqueness** of the solution to the Cauchy problem for any initial condition $\Gamma(0) \in \mathcal{D}(\mathbb{C}^7)$.

**(c) Injectivity of flow.** From uniqueness of the Cauchy problem: if $\Gamma_1(0) \neq \Gamma_2(0)$, then $\Gamma_1(\tau) \neq \Gamma_2(\tau)$ for all $\tau$ in the domain of existence (trajectories do not intersect in phase space — a standard result of ODE theory). $\blacksquare$

### Lemma G3: Axiomatic definiteness of structures [T] {#лемма-g3}

:::tip Lemma G3 (Axiomatic definiteness) [T]
Axioms A1–A5 uniquely determine (in the given basis $\mathcal{B}$) the following structures:

**(i)** Atomic projectors $\{|k\rangle\langle k|\}_{k=0}^{6}$ (from L-unification [T])

**(ii)** The system of Fano lines $\{\mathrm{line}_p\}_{p=1}^{7} \subset \binom{[7]}{3}$ with its orientation, i.e. the structure constants $f_{ijk}$ (from bridge T15: the lines [T], their canonical orientation [T] by T15-canon)

**(iii)** E-projection $\pi_E(\Gamma) = P_E\Gamma + \Gamma P_E - P_E\Gamma P_E$ (from [Coh_E [T]](/docs/core/foundations/axiom-septicity#hs-projection))

**(iv)** Page–Wootters tensor decomposition $\mathcal{H}_O \otimes \mathcal{H}_{\mathrm{rest}}$, singling out O (from A5)

**(v)** The regeneration formula $\kappa_0 = \omega_0 \cdot |\gamma_{OE}| \cdot |\gamma_{OU}| / \gamma_{OO}$, singling out $\{O, E, U\}$ (from [categorical derivation of κ₀ [T]](/docs/core/foundations/axiom-septicity#структурный-анзац-kappa0))
:::

**Proof.** Each structure is derived from the axioms:
- (i): [L-unification](/docs/core/foundations/axiom-omega#lk-из-omega) [T] — atoms $S_k = |k\rangle\langle k|$ of classifier $\Omega$
- (ii): Bridge T15 — uniqueness of BIBD$(7,3,1)$ $\cong$ PG(2,2) (Hall 1967) [T]; the orientation that turns the lines into the structure constants $f_{ijk}$ is the canonical one, the unique collineation-invariant class (T15-canon [T]; registry row 41n). This line read "Bridge T15 [T]" without the orientation step until 2026-09-25, then named the orientation as the input (Alt) until T15-canon
- (iii): [HS-projection theorem](/docs/core/foundations/axiom-septicity#теорема-hs-проекция) [T] — orthogonal projection in Hilbert–Schmidt space
- (iv): Axiom A5 (Page–Wootters) — explicit postulate
- (v): Adjunction $\mathcal{D}_\Omega \dashv \mathcal{R}$ [T] — formula for $\kappa_0$ from [categorical derivation](/docs/core/foundations/axiom-septicity#структурный-анзац-kappa0). $\blacksquare$

### Lemma G4: The octonionic-structure gauge group is $G_2$ [T] {#лемма-g4}

:::tip Lemma G4 (Gauge group of the octonionic 3-form) [T]
The maximal subgroup $\mathcal{G} \subseteq U(7)$ preserving the octonionic associative 3-form $\varphi_3 = \sum_{i<j<k} f_{ijk}\, e^i\wedge e^j\wedge e^k$ — equivalently, the structure constants $f_{ijk}$ of Lemma G3(ii) — is $G_2 \times \mu_3$, where $\mu_3 = \{\mathbb{1}, \omega\mathbb{1}, \omega^2\mathbb{1}\}$, $\omega = e^{2\pi i/3}$. The scalars $\omega\mathbb{1}$ preserve every 3-form and act trivially on density matrices, so on states the gauge group is $G_2 = \mathrm{Aut}(\mathbb{O})$. (It read "is exactly $G_2$" until 2026-09-25.)

The remaining structures of Lemma G3 — the atomic projectors (i), the E-projection (iii), the PW clock $O$ (iv), the $\kappa_0$ formula (v) — are **not** $G_2$-invariant; they fix a **functional frame** (a choice of gauge) inside each $G_2$-orbit. Two representations related by $U\in G_2$ carry their frames into one another.
:::

**Proof.** We show $\mathcal{G} = G_2 \times \mu_3$ in two inclusions.

**(A) $G_2 \subseteq \mathcal{G}$.** By definition $G_2 = \{g\in GL(7,\mathbb{R}) : g^\ast\varphi_3 = \varphi_3\}$ preserves the 3-form, and $G_2\subset SO(7)\subset U(7)$ preserves the Hermitian structure. Hence every $g\in G_2$ preserves $\varphi_3$, i.e. $g\in\mathcal{G}$. The scalars $\omega\mathbb{1}$, $\omega^3 = 1$, preserve every 3-form, so $\mu_3 \subseteq \mathcal{G}$ as well. $\checkmark$

:::warning The functional labels are frame data, not $G_2$-invariants
Since $\mathbb{C}^7$ is an **irreducible** $G_2$-module (Cartan 1894), by Schur's lemma it has **no** nonzero proper $G_2$-invariant subspace. Consequently:
- no coordinate axis $|k\rangle$ — in particular the E, O, U axes — is $G_2$-invariant; a generic $g\in G_2$ rotates it;
- the *set* of atomic projectors $\{|k\rangle\langle k|\}$ is preserved only by the **finite** frame subgroup $\Gamma_{\!\text{oct}} = 2^3 \!\cdot\! \mathrm{PSL}(3,2) \subset G_2$ of order $1344$ (permutation part $\mathrm{Aut}(PG(2,2)) \cong PSL(2,7)$, order 168; sign part of order 8 — [frame rigidity](#жёсткость-репера)), not by all of $G_2$;
- hence $\mathrm{Coh}_E$, $\Phi$ and $\kappa_0$, which reference the E/O/U axes, are **frame-dependent**: invariant under $\mathrm{Stab}_{G_2}$ of the chosen frame, not under all of $G_2$ — $\Phi$ under the whole frame group $\Gamma_{\!\text{oct}}$, $\mathrm{Coh}_E$ only under its $192$ elements that keep the $E$-axis, $\kappa_0$ only under the elements that keep the axes it references. They are physical because the frame is pinned by the dynamics (Definition G1's $\mathcal{L}_\Omega$-covariance), **not** because they descend to $\mathcal{D}(\mathbb{C}^7)/G_2$.

The genuinely $G_2$-invariant content is the spectrum (6 numbers) plus the $\varphi_3$-relative angles (28) — the $48-14=34$ parameters of Corollary 1.
:::

**(B) $\mathcal{G} \subseteq G_2 \times \mu_3$.** Let $U \in \mathcal{G}$.

**Step B1 (Lie algebra).** Write $X \in \mathfrak{u}(7)$ as $X = A + iS$ with $A$ real antisymmetric and $S$ real symmetric. Since $\varphi_3$ is real, $X\cdot\varphi_3 = A\cdot\varphi_3 + i\,S\cdot\varphi_3$ vanishes only if $A\cdot\varphi_3 = 0$ and $S\cdot\varphi_3 = 0$, i.e. only if $A$ and $S$ lie in the Lie algebra $\mathfrak{g}_2 \subset \mathfrak{so}(7)$ of $G_2 = \{g \in GL(7,\mathbb{R}) : g^*\varphi_3 = \varphi_3\}$; a symmetric $S$ in $\mathfrak{so}(7)$ is zero. So the Lie algebra of $\mathcal{G}$ is $\mathfrak{g}_2$ and its identity component is $G_2$ (machine check: the stabiliser of $\varphi_3$ in $\mathfrak{u}(7)$ has real dimension $14$).

**Step B2 (normaliser).** $U$ normalises the identity component, so $g \mapsto UgU^{-1}$ is an automorphism of $G_2$. $G_2$ has no outer automorphisms, so there is $h \in G_2$ with $UgU^{-1} = hgh^{-1}$ for all $g \in G_2$, and $h^{-1}U$ commutes with $G_2$. Since $\mathbb{C}^7$ is an irreducible $G_2$-module (Cartan 1894), Schur's lemma gives $h^{-1}U = \lambda\mathbb{1}$ with $\lvert\lambda\rvert = 1$.

**Step B3 (the scalar).** $\lambda\mathbb{1} = h^{-1}U$ preserves $\varphi_3$, and $(\lambda\mathbb{1})^*\varphi_3 = \lambda^3\varphi_3$, so $\lambda^3 = 1$ and $U = h\,\lambda\mathbb{1} \in G_2 \times \mu_3$. The product is direct: $\mu_3$ is central, and $\omega\mathbb{1}$ is not real, so $\mu_3 \cap G_2 = \{\mathbb{1}\}$. $\blacksquare$

*Corrected 2026-09-25:* part (B) started from a $U$ preserving "all five structures of Lemma G3" (not the hypothesis of the lemma) and relied on a box asserting that "preservation of all 7 such subspaces is equivalent to preservation of the octonionic cross-product". That equivalence is false: every diagonal unitary preserves the seven coordinate line subspaces, and a generic one does not preserve $\varphi_3$ (machine check). The former Step B3 assumed that $U$ preserves the real structure, which $\omega\mathbb{1}$ does not. Steps B1–B3 and the box are replaced by the argument above; the lemma changes only by the scalars $\mu_3$, which act trivially on states.

:::info Clarification: PSL(2,7) vs G₂
The group of combinatorial automorphisms of PG(2,2) is finite: $\mathrm{Aut}(\mathrm{PG}(2,2)) \cong \mathrm{PSL}(2,7)$, $|\mathrm{PSL}(2,7)| = 168$. The group $G_2 = \mathrm{Aut}(\mathbb{O})$ is a compact Lie group, $\dim G_2 = 14$. Relation: every collineation of PG(2,2) has exactly $8$ lifts — signed permutations of the basis that are automorphisms of $\mathbb{O}$; the lifts form the frame group $\Gamma_{\!\text{oct}} \subset G_2$ of order $1344$, a non-split extension $2^3 \cdot \mathrm{PSL}(3,2)$, so the collineation group is a quotient of $\Gamma_{\!\text{oct}}$, not a subgroup of it. (Until 2026-09-25 this read "$\mathrm{PSL}(2,7) \subset G_2$ as a finite subgroup — every permutation of 7 points compatible with PG(2,2) extends to a continuous automorphism of $\mathbb{O}$"; as bare permutations only $21$ of the $168$ collineations are automorphisms.) Part (B) uses only the 3-form $\varphi_3$, not the combinatorics of the lines.
:::

---

## Main theorem {#теорема}

### Theorem (G₂-rigidity of holonomic representation) [T] {#g2-ригидность}

:::warning Theorem of G₂-rigidity [T]
Let $S$ be an autonomous system satisfying (AP)+(PH)+(QG)+(V), with $\mathbb{C}^7$ carrying the octonionic multiplication of Lemma G3(ii) (from the axioms through the bridge T15 with the canonical orientation, T15-canon). Let $(\mathbb{C}^7, \mathcal{B}_1, G_1)$ and $(\mathbb{C}^7, \mathcal{B}_2, G_2)$ be two holonomic representations of $S$ (Definition G1).

Then there exists a **unique** $U \in G_2 = \mathrm{Aut}(\mathbb{O})$ such that:

$$
\boxed{G_2(s) = U \, G_1(s) \, U^\dagger \quad \forall \, s \in \mathrm{States}(S)}
$$

Equivalently: **the holonomic representation is unique up to gauge group $G_2$**.

**Sharpening (frame decision D-0910).** Because $\mathcal{L}_\Omega$ itself is covariant only under the finite frame group, the intertwiner $U$ of two representations that share the *same* axiomatic dynamics lies in $\Gamma_{\!\text{oct}} \subset G_2$. The $G_2$ statement is the kinematic envelope — the largest group any two representations can differ by; the $\Gamma_{\!\text{oct}}$ statement is the dynamical identification.
:::

### Proof {#доказательство}

**Step 1: Definiteness of dynamics in each representation.**

In representation $(\mathbb{C}^7, \mathcal{B}_i, G_i)$ axioms A1–A5 determine the Liouvillian $\mathcal{L}_\Omega^{(i)}$ (Lemma G3 [T]). The compatibility condition (Definition G1) guarantees:

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

Both representations describe the same physical system and generate the same observables. The spectrum of $\Gamma$ (set of eigenvalues) is invariant: $\mathrm{Spec}(\Phi(\Gamma)) = \mathrm{Spec}(\Gamma)$ for all $\Gamma$ (since the spectral observables — purity $P = \mathrm{Tr}(\Gamma^2)$, von Neumann entropy, the eigenvalues — must coincide; the frame-pinned observables such as $\mathrm{Coh}_E$ are carried covariantly and enter in Step 4).

A spectrum-preserving map on $\mathcal{D}(\mathbb{C}^7)$ is conjugation by a unitary (or antiunitary) operator — this is **Wigner's theorem** (Wigner 1931) in the form of Kadison (Kadison 1965):

$$
\Phi(\Gamma) = U \Gamma U^\dagger \quad \text{for some } U \in U(7)
$$

(the antiunitary case is excluded since $\Phi$ is continuously connected to the identity map through a continuous family of systems).

:::tip Extension of Φ to all D(ℂ⁷)
By the viability condition (V), the trajectories of the holon pass through an open neighborhood of the attractor $\rho^*$ (T-125 [T]). Therefore $\mathrm{Im}(G_1)$ contains an open subset of $\mathrm{Int}(\mathcal{D}(\mathbb{C}^7))$. An affine map defined on an open subset of a complete metric space extends uniquely to the whole space (Tietze theorem). The extended $\Phi$ preserves the spectrum on all of $\mathcal{D}(\mathbb{C}^7)$.
:::

:::info Clarification: Wigner vs. Uhlmann
Here **Wigner's theorem** (in Kadison's form) is applied: an affine bijection $\Phi$ on the state space $\mathcal{D}(\mathbb{C}^7)$ that preserves the spectrum (and hence fidelity $F(\rho, \sigma) = \mathrm{Tr}\sqrt{\sqrt{\rho}\sigma\sqrt{\rho}}$) is realized by unitary or antiunitary conjugation. This is the correct reference for this step, since $\Phi$ is a bijection on the state space, not a CPTP channel. For CPTP channels (which are in general not bijections) preservation of fidelity is characterized by **Uhlmann's theorem** (Uhlmann 1976): $F(\mathcal{E}[\rho], \mathcal{E}[\sigma]) \leq F(\rho, \sigma)$ for any CPTP $\mathcal{E}$, with equality if and only if $\mathcal{E}$ is a unitary channel on the support of $\rho$ and $\sigma$. In the context of the monotonicity of Freedom (Theorem [Properties of Freedom](/docs/core/foundations/consequences#freedom-свойства) in consequences.md), it is precisely Uhlmann's contractivity that justifies the non-increase of freedom under CPTP evolution.
:::

**Step 4: $U \in G_2$.**

Since both representations satisfy axioms A1–A5, the unitary $U$ must preserve the **octonionic 3-form** $\varphi_3$ carried by the axiomatic Fano structure (Lemma G3(ii) [T]). The functional labels (atomic projectors, E-projection, PW clock, $\kappa_0$) are carried covariantly: $U$ maps the frame of representation 1 to the frame of representation 2.

By Lemma G4 [T], preservation of $\varphi_3$ gives $U \in G_2$. $\blacksquare$

**Step 5: Uniqueness of $U$.**

Suppose $U_1, U_2 \in G_2$ both satisfy $G_2 = \mathrm{Ad}_{U_i} \circ G_1$. Then $\mathrm{Ad}_{U_1^{-1}U_2} = \mathrm{Id}$ on the image of $G_1$. If the image of $G_1$ contains sufficiently many states (which is guaranteed by viability: the system passes through a neighborhood of $\rho_*$ by primitivity [T], and this neighborhood is open in $\mathcal{D}(\mathbb{C}^7)$), then $U_1^{-1}U_2 = e^{i\theta} I$ — a scalar phase, acting trivially on $\mathcal{D}(\mathbb{C}^7)$. $\blacksquare$

---

## Corollaries {#следствия}

### Corollary 1: Kinematic invariants and physical states [T] {#физические-состояния}

:::tip Corollary 1 (Kinematic invariants and physical states) [T]
The space of $G_2$-orbits of **kinematic** states of the holon (spectrum + $\varphi_3$-relative angles):

$$
\mathcal{D}_{\mathrm{kin}} = \mathcal{D}(\mathbb{C}^7) / G_2
$$

has dimension:

$$
\dim_\mathbb{R}(\mathcal{D}_{\mathrm{kin}}) = 48 - 14 = 34
$$

where $48 = N^2 - 1 = \dim(\mathrm{su}(7))$ is the full number of parameters of $\Gamma$, and $14 = \dim(G_2)$ is the dimension of a generic kinematic $G_2$-orbit. The space of **physically distinguishable** states is $\mathcal{D}_{\mathrm{phys}} = \mathcal{D}(\mathbb{C}^7)/\Gamma_{\!\text{oct}}$, of full dimension **48** (frame decision D-0910): the 14 orbit directions are physical because the axiomatic dynamics pins the frame.
:::

**Proof.** For generic $\Gamma$ (with distinct eigenvalues) the stabilizer $\mathrm{Stab}_{G_2}(\Gamma)$ is trivial (finite group). Then by the orbit theorem: $\dim(\mathrm{Orb}(\Gamma)) = \dim(G_2) = 14$, and $\dim(\mathcal{D}_{\mathrm{kin}}) = 48 - 14 = 34$. $\blacksquare$

:::info Consistency
The value 34 is the kinematic count only. The pinching dynamics is $\Gamma_{\!\text{oct}}$-covariant, not $G_2$-covariant, at **every** $\alpha$ — including the pure Fano regime $\alpha = 0$ ([Theorem 5.1b](/docs/proofs/gap/fano-channel#g2-ковариантность), [Lindblad operators](/docs/core/operators/lindblad-operators#g2-ковариантность)) — so no dynamical regime realises a $48 \to 34$ reduction of the physical parameter space (D-0910).
:::

### Corollary 2: Well-posedness of inverse problem [T] {#обратная-задача}

:::tip Corollary 2 (Inverse problem) [T]
For a system $S$ satisfying (AP)+(PH)+(QG)+(V), the initial state $\Gamma(0)$ is **uniquely** recovered from:

**(a)** The observed trajectory $\Gamma(\tau)$ for $\tau \in (0, T]$ (Lemmas G1, G2 [T])

**(b)** The system parameters $(\omega_0, \lambda_m)$

up to the finite frame group $\Gamma_{\!\text{oct}}$ (frame decision D-0910); in particular up to $G_2$ (Theorem of G₂-rigidity [T]).
:::

### Corollary 3: Faithfulness of functor F [T] {#верность-функтора}

:::tip Corollary 3 (Faithfulness of functor) [T]
The functor $F: \mathbf{DensityMat} \to \mathbf{Exp}$ ([categorical formalism](/docs/proofs/categorical/categorical-formalism)) is **faithful** on frame orbits: if $F(\Gamma_1) \cong F(\Gamma_2)$ in $\mathbf{Exp}$, then $\Gamma_2 = U\Gamma_1 U^\dagger$ for $U \in \Gamma_{\!\text{oct}}$ (in particular $U \in G_2$).

Kernel of $F$ on the set of isomorphisms (experience reads the frame-pinned $E$-sector, so a generic $G_2$-rotation changes it — D-0910, and so does every element of $\Gamma_{\!\text{oct}}$ that moves the $E$-axis):

$$
\ker(F) \subseteq \{\mathrm{Ad}_U : U \in \Gamma_{\!\text{oct}},\ U e_E = \pm e_E\} \subsetneq \{\mathrm{Ad}_U : U \in \Gamma_{\!\text{oct}}\} \subset \{\mathrm{Ad}_U : U \in G_2\}
$$

The $E$-axis stabiliser in $\Gamma_{\!\text{oct}}$ has $192 = 1344/7$ elements.
:::

*Corrected 2026-09-25.* The corollary stated $\ker(F) = \{\mathrm{Ad}_U : U \in \Gamma_{\!\text{oct}}\}$; that is retracted: $F$ reads the $E$-sector, and an element of $\Gamma_{\!\text{oct}}$ that moves the $E$-axis takes $\mathrm{Coh}_E(\lvert e_E\rangle\langle e_E\rvert)$ from $1$ to $0$, so $\mathrm{Ad}_U$ changes $F$ for $1152$ of the $1344$ elements; only the $192$ that keep the $E$-axis can lie in the kernel ([lattice of identification groups](#жёсткость-репера); regression test `test_coh_e_is_invariant_only_on_the_e_axis_stabiliser`). The faithfulness statement above is unaffected.

### Corollary 4: Predictive power [T] {#предсказательная-мощность}

:::tip Corollary 4 (Finiteness of gauge group) [T]
$G_2$ is a **finite-dimensional** (14-dimensional) compact Lie group. This means:

1. A **discrete set** of $G_2$-invariant observables fully characterizes the kinematic state; the physical state additionally carries the 14 frame-orientation parameters, pinned by the dynamics (D-0910)
2. A **finite number** of parameters — 34 kinematic $G_2$-invariants, 48 physical parameters in the pinned frame — unlike standard QM, where $U(\mathcal{H})$-freedom is infinite-dimensional
3. The theory is **maximally predictive** at the given dimension $N = 7$: the gauge group $G_2$ is the minimal group preserving the octonionic structure
:::

### Corollary 5: G₂-invariants as physical observables {#инварианты}

The 34 kinematic $G_2$-invariants are organized as follows (with the 14 frame-orientation parameters they make up the 48 physical parameters, D-0910):

| Type | Number of parameters | Description |
|-----|:---:|---|
| Spectrum of $\Gamma$ | 6 | Eigenvalues (ordered) |
| $G_2$-invariant angles | 28 | Mutual position of eigenvectors relative to octonionic structure |
| **Total** | **34** | Complete set of kinematic $G_2$-invariants |

Two classes of observable must be distinguished (irreducibility of $\mathbf 7$, Lemma G4):

**Genuinely $G_2$-invariant** (descend to $\mathcal{D}(\mathbb{C}^7)/G_2$):
- Purity $P = \mathrm{Tr}(\Gamma^2)$ — in fact $U(7)$-invariant, hence $G_2$-invariant
- Reflection measure $R = 1/(7P)$ — a function of $P$, hence $G_2$-invariant
- the spectrum (6) and the $\varphi_3$-relative angles (28) — the 34 parameters above

**Frame-dependent** (defined only after the functional frame is fixed by the dynamics; invariant under $\mathrm{Stab}_{G_2}$ of the frame, *not* under all of $G_2$, since no axis is $G_2$-invariant):
- E-coherence $\mathrm{Coh}_E(\Gamma)$ — references the E-axis; invariant only under the elements that keep it ($192$ of the $1344$ in $\Gamma_{\!\text{oct}}$)
- Integration measure $\Phi = \sum_{i\neq j}|\gamma_{ij}|^2/\sum_i\gamma_{ii}^2$ — references the coordinate basis; invariant under all of $\Gamma_{\!\text{oct}}$
- the regeneration coefficient $\kappa_0$ — references the O, E, U axes

These frame-dependent quantities are physical because the dynamics ($\mathcal{L}_\Omega$-covariance, Definition G1) pins the frame; they are not among the 34 orbit-invariants.

---

## Relation to open questions {#открытые-вопросы}

### Closing the problem of G at the level of theory

This theorem **fully closes** the question of uniqueness of the map G at the theoretical level:

| Question | Status | Basis |
|--------|:------:|-----------|
| **Existence** of G | **[T]** (Theorem S); the octonionic structure via the bridge T15, [T] with the canonical orientation (T15-canon) | Theorem S + bridge T15 |
| **Uniqueness** of G (up to $G_2$) | **[T]** | Theorem of $G_2$-rigidity (this document) |
| **Predictivity** of G | [Empirical] | Requires experimental verification |

Question 3 (predictivity) is **epistemological**, not mathematical: it is closed empirically (convergent validity, predictive success, interventional testing). This is the same epistemological standard by which all fundamental physics operates.

### Analogy with physical theories

| Theory | Uniqueness theorem | Gauge group | Empirical verification |
|--------|---|---|---|
| QM | Stone–von Neumann (1931) | $U(\mathcal{H})$ | Spectra, interference |
| GR | Birkhoff (spherical symmetry) | $\mathrm{Diff}(M)$ | Light deflection, gravitational waves |
| SM | Coleman–Mandula / Haag–Łopuszański–Sohnius | Poincaré $\times$ gauge | Accelerators, PDG |
| **UHM** | **$G_2$-rigidity** (this theorem) | **$G_2 = \mathrm{Aut}(\mathbb{O})$** | thresholds, Gap profiles (the Cabibbo angle was listed here; withdrawn 2026-09-26, T-345(e): its agreement came from a fitted $C_{\mathrm{norm}}\approx26$) |

---

## Summary {#резюме}

:::tip Key result
**Theorem of $G_2$-rigidity [T]:** The holonomic representation of a system satisfying (AP)+(PH)+(QG)+(V) is **unique** up to gauge group $G_2 = \mathrm{Aut}(\mathbb{O})$ — a 14-dimensional exceptional Lie group, the automorphism group of the octonions.

**Physical meaning:** Different observers applying UHM to the same system, with the frame pinned by the axiomatic dynamics, obtain coherence matrices related by an element of the finite frame group $\Gamma_{\!\text{oct}} \subset G_2$ (D-0910): all 48 parameters coincide up to a relabelling of axes. The 34 kinematic $G_2$-invariants (spectrum, $\varphi_3$-relative angles) coincide even before the frame is pinned.

**Methodological status:** All steps of the proof are theorems [T], relying on previously established results. This theorem closes the problem of the map G at the theoretical level and is the analogue of the Stone–von Neumann theorem for UHM.
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
