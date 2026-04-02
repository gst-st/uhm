---
sidebar_position: 2
title: "Lindblad Operators"
description: "Master definition of the Lindblad operators L_k in UHM: atomic and Fano-structured operators, CPTP verification, G₂-covariance"
---

# Lindblad Operators L_k

This chapter is about how reality dissipates coherence — and why that is not a catastrophe but a necessary condition of life. Any system interacting with an environment gradually loses quantum correlations (coherences). This is the fundamental process known as *decoherence*. In the classical analogy it is a wind that blurs a drawing in the sand. Each Lindblad operator $L_k$ is a specific "direction of the wind", a specific channel through which information leaks out of the system.

But UHM adds an unexpected twist to this classical picture: the structure of decoherence is **not arbitrary**. It is uniquely determined by the axioms of the theory and organised according to the [Fano plane](/docs/physics/gauge-symmetry/fano-selection-rules) — the same algebraic structure that governs the octonions and the exceptional group $G_2$. Decoherence is not chaos, but *structured forgetting*.

:::info DRY: Master definition of the Lindblad operators
This is the **canonical definition** of the Lindblad operators $L_k$ in UHM. All documents should reference this page rather than repeat the definition.
:::

---

## Historical Precursors

The theory of open quantum systems is one of the most important achievements of mathematical physics in the twentieth century.

**Göran Lindblad** (Sweden, 1976) and **independently** Vittorio Gorini, Andrzej Kossakowski, and George Sudarshan (Italy–India, 1976) proved a fundamental theorem: *any* Markovian evolution of a quantum system (without memory of the past) can be written in the form of a master equation with specific operators $L_k$. This equation now bears the name LGKS (Lindblad–Gorini–Kossakowski–Sudarshan), although it is more commonly referred to simply as "the Lindblad equation".

**Karl Kraus** (1983) demonstrated an equivalent approach via the *operator-sum representation*: any quantum channel can be written as $\Phi(\rho) = \sum_k K_k \rho K_k^\dagger$ subject to $\sum_k K_k^\dagger K_k = I$. The Kraus operators $K_k$ are the "building blocks" from which any admissible quantum transformation is constructed.

**Wojciech Stinespring** (1955) proved an even deeper result: any quantum channel is the projection of a unitary (reversible) evolution in a larger space. Decoherence is not a "loss" of information but its "leakage" into the environment.

In UHM the Lindblad operators are **not postulated** — they are *derived* from the structure of the subobject classifier $\Omega$. Each atom of $\Omega$ generates its own operator $L_k$, and the structure of the [Fano plane](/docs/physics/gauge-symmetry/fano-selection-rules) determines their unique physically admissible combination.

---

## Intuitive Explanation: Wind and a Drawing in the Sand {#интуиция-ветер}

Imagine a drawing in the sand. The wind gradually blurs it. Each gust of wind is a single Lindblad operator $L_k$: a specific direction, a specific force.

If the wind blows **from all directions equally** (atomic operators $L_k^{\text{atom}}$), the drawing is erased *completely*. What remains is a flat surface — the maximally mixed state $I/7$.

But if the wind blows **in a structured way** (Fano operators $L_p^{\text{Fano}}$), it erases fine details while *preserving* the broad features. The drawing fades (coherences are reduced by a factor of 3), but does not disappear. This is critically important for living systems: they need to interact with the environment (to let the wind blow), while at the same time preserving their identity (preventing the drawing from vanishing entirely).

---

## L-Unification

In UHM the letter **L** unifies three levels of structure. This is not a coincidental overlap of notation — behind it lies a deep structural connection.

| Notation | Meaning | Source |
|-------------|----------|----------|
| $L$ (logic) | [Logic dimension](/docs/core/structure/dimension-l) | Structure of Ω |
| $L_k$ (operators) | Lindblad operators | Dissipative dynamics |
| $\mathcal{L}_\Omega$ | [Logical Liouvillian](/docs/core/dynamics/evolution#логический-лиувиллиан) | Generator of evolution |

It is like the word "key" in English — door-key, musical key, key to an answer — three different concepts. But in UHM it turns out that "L-key" is genuinely *the same* construction at different levels of description. The L-dimension (the logical structure of the Holon) generates $L_k$ (the specific operators), which assemble into $\mathcal{L}_\Omega$ (the full generator of evolution). One letter — one root — three manifestations.

:::tip Theorem: L-unification
The three constructions are derived from a single source — [Axiom Ω⁷](/docs/core/foundations/axiom-omega):

$$
\Omega \xrightarrow{\text{logic}} L \xrightarrow{\text{stratification}} L_k \xrightarrow{\text{generator}} \mathcal{L}_\Omega
$$

[Proof →](/docs/proofs/physics/physics-correspondence#2-l-унификация) | Status: **[Т]**
:::

## Definition of the Lindblad Operators

### Standard Lindblad Form for Open Systems

For an arbitrary open quantum system the Lindblad (LGKS) master equation takes the form:

$$
\frac{d\Gamma}{d\tau} = -i[H_{\text{eff}}, \Gamma] + \mathcal{D}[\Gamma]
$$

where the dissipator $\mathcal{D}$ is specified by a set of operators $\{L_k\}$:

$$
\mathcal{D}[\Gamma] = \sum_{k} \left( L_k \Gamma L_k^\dagger - \frac{1}{2}\{L_k^\dagger L_k, \Gamma\} \right)
$$

In standard physics the operators $L_k$ are **postulated** from phenomenological considerations. In UHM they are **derived** from the structure of the subobject classifier $\Omega$.

### Derivation from the Classifier $\Omega$ {#деривация-из-классификатора}

[Axiom Ω⁷](/docs/core/foundations/axiom-omega) defines the subobject classifier $\Omega$ of the $\infty$-topos in which the Holon lives. The atoms of $\Omega$ — the minimal non-trivial subobjects — uniquely generate the Lindblad operators through the following chain:

**Step 1. Atoms of $\Omega$ → projectors.** Each atomic subobject $S_k \subset \Omega$ ($k \in \{A, S, D, L, E, O, U\}$) corresponds to one dimension of the Holon. Projection onto the subobject yields the **atomic Lindblad operator**:

$$
L_k^{\text{atom}} = |k\rangle\langle k|
$$

This is a projector, not a transition operator — $L_k^{\text{atom}}$ "observes" the $k$-th dimension without generating transitions between dimensions.

**Step 2. Composite atoms → Fano operators.** The classifier $\Omega$ in the $\infty$-topos contains not only point-like atoms but also **composite subobjects**. The [Fano plane](/docs/physics/gauge-symmetry/g2-structure) PG(2,2) defines 7 linear subobjects — triples of dimensions. Each Fano line $p = (i, j, k)$ yields a **Fano Lindblad operator**:

$$
L_p^{\text{Fano}} = \frac{1}{\sqrt{3}}\,\Pi_p = \frac{1}{\sqrt{3}}(|i\rangle\langle i| + |j\rangle\langle j| + |k\rangle\langle k|)
$$

**Step 3. Canonical form.** The uniqueness of the Fano form as the physically correct one is proved below (theorem on [uniqueness of the Fano form](#теорема-единственность-фано) [Т]): only the Fano operators simultaneously satisfy CPTP, $G_2$-covariance, and primitivity.

:::info Remark: the role of the Hamiltonian in generating transitions
The atomic and Fano operators are **projectors**, not transition operators. Inter-level transitions (off-diagonal dynamics) are generated by the **Hamiltonian** part $-i[H_{\text{eff}}, \Gamma]$: it is the commutator with $H_{\text{eff}}$ that creates coherences between dimensions. The dissipator $\mathcal{D}[\Gamma]$ with projective $L_k$ is responsible for **decoherence** — the suppression of coherences. The full dynamics arises from the balance between these two processes.
:::

### Properties

1. **Trace preservation:** The dissipator $\mathcal{D}[\Gamma]$ automatically preserves the trace: $\mathrm{Tr}(\mathcal{D}[\Gamma]) = 0$ for arbitrary $L_k$ (follows from the structure of the Lindblad equation). **Note:** The condition $\sum_k L_k^\dagger L_k = \mathbb{I}$ applies to the **Kraus operators** of the CPTP channel (see [Fano operators](#фано-операторы)), not to the Lindblad operators in the master equation.
2. **Projective nature:** each $L_k$ is a projector onto a subobject of the classifier $\Omega$, performing "observation" of the corresponding sector
3. **Relation to χ_S:** the operators define the [subjectness characteristic](/docs/consciousness/foundations/self-observation)
4. **Relation to ▷:** via L-unification, $L_k$ generate the [temporal modality](/docs/core/operators/emergent-time)

## Two Types of Atoms of the Classifier Ω {#атомы-классификатора}

### Intuitive Explanation: Pixels and Groups {#интуиция-атомы}

The subobject classifier $\Omega$ is a "dictionary" of all possible parts of the Holon. In this dictionary there are two types of "words":

- **Atomic subobjects** $S_k$ — individual "pixels". Each $S_k$ corresponds to one dimension: $S_A$ — the Affect dimension, $S_S$ — the Structure dimension, and so on. There are 7 of them — one per dimension.

- **Composite subobjects** $S_p$ — "groups of pixels". Each $S_p$ is a triple of dimensions forming a line on the [Fano plane](/docs/physics/gauge-symmetry/fano-selection-rules). There are also 7 of them, and each dimension belongs to exactly 3 triples. For example, if line $p$ connects dimensions $\{A, D, U\}$, then $S_p = \mathrm{span}\{|A\rangle, |D\rangle, |U\rangle\}$.

The two types of atoms generate two types of Lindblad operators — *atomic* and *Fano*. The atomic operators observe each dimension individually (pixel vision). The Fano operators observe triples (defocused vision). The Fano operators are the physically canonical ones — they are the ones that determine the actual dynamics.

---

From [L-unification](/docs/proofs/categorical/categorical-formalism) it follows that the Lindblad operators are derived from the **atoms** of the classifier $\Omega$. [Axiom Ω⁷](/docs/core/foundations/axiom-omega) defines the **basic (atomic) atoms**:

:::warning Historical remark: early formulations of $L_k$
Early formulations of UHM used the notations $L_k = \sqrt{\chi_{S_k}}$ (characteristic morphism) and $L_k = \sqrt{\gamma_k}|k\rangle\langle k+1| \otimes P_{\text{strat}}^{(k)}$ (transition operators). Both notations are **obsolete**: the first is mathematically incorrect ($\sqrt{\chi} = \chi$ for $\chi \in \{0,1\}$), the second conflates the roles of the Hamiltonian (transitions) and the dissipator (projections). The canonical definition — projectors $L_k^{\text{atom}} = |k\rangle\langle k|$ and $L_p^{\text{Fano}} = \frac{1}{\sqrt{3}}\Pi_p$ — see [§Derivation from the classifier](#деривация-из-классификатора). Uniqueness of the Fano form: [Т] ([theorem](#теорема-единственность-фано)).
:::

$$
S_k = |k\rangle\langle k|, \quad k \in \{A, S, D, L, E, O, U\}
$$

However, the classifier $\Omega$ in the $\infty$-topos contains not only atomic subobjects but also **composite** ones. The [Fano plane](/docs/physics/gauge-symmetry/g2-structure) $\mathrm{PG}(2,2)$ defines 7 **linear subobjects** — projections onto 3-dimensional subspaces:

$$
\Pi_p = \sum_{i \in \mathrm{line}_p} |i\rangle\langle i|, \quad p = 1, \ldots, 7
$$

Each Fano line $p = (i, j, k)$ generates a **composite atom** $S_p = \mathrm{span}\{|i\rangle, |j\rangle, |k\rangle\}$.

:::tip Theorem: Completeness of Fano atoms [Т]
Each dimension lies on exactly 3 Fano lines. Therefore:

$$
\sum_{p=1}^{7} \Pi_p = 3I
$$

[Proof →](/docs/proofs/gap/fano-channel#фано-канал) | Status: **[Т]**
:::

:::info Remark: Categorical interpretation
The atomic subobjects $S_k$ and the composite Fano subobjects $S_p$ together form the lattice of subobjects of the classifier $\Omega$. The transition from atomic to composite atoms corresponds to an enrichment of the classifier's logic — from Boolean (point-like) to projective (linear). This reflects the structure of the $\infty$-topos, where $\Omega$ contains a hierarchy of truth-value types.
:::

:::info Distinction between the two forms of $L_k$ {#разграничение-форм-lk}
UHM employs **two distinct forms** of the operators $L_k$ that should not be conflated:

| Form | Notation | Definition | Role |
|-------|-------------|-------------|------|
| **Formal (atomic)** | $L_k^{\text{atom}} = \lvert k\rangle\langle k\rvert$ | Projectors from the subobject classifier $\Omega$ | Categorical foundation; proof of primitivity |
| **Fano form (composite)** | $L_p^{\text{Fano}} = \frac{1}{\sqrt{3}}\Pi_p$ | Projectors onto Fano lines of PG(2,2) | Physical theorems; CPTP channels; dynamics |

**All physical results** (coherence contraction, $P_{\text{crit}} = 2/7$, $G_2$-covariance, formula for $\kappa_0$) use the **Fano form**. The atomic form serves as the foundation for proving primitivity of the linear part $\mathcal{L}_0$ [Т] and $S_7$-equivariance [Т], but is replaced by the Fano operators in physical computations.

**The equivalence of the two forms** follows from the L-unification chain T11–T13 [Т]: Choi rank of the channel = 7 (T11) + projective decomposition from L-unification (T12) + forced BIBD$(7,3,1)$ (T13) prove that the atomic projectors $L_k^{\text{atom}}$ **uniquely generate** the Fano operators $L_p^{\text{Fano}}$ as the unique minimal composite decomposition. Details: [T11](#теорема-ранг-хои), [T12](#теорема-проективная-декомпозиция), [T13](#теорема-bibd-из-хои).
:::

#### Theorem (Uniqueness of the Fano form from axioms) [Т] {#теорема-единственность-фано}

:::tip Theorem (Uniqueness of the Fano form from axioms) [Т]
The Fano operators are the **unique** minimal composite Lindblad operators compatible with axioms A1–A5.

**Proof (7 steps).**

**Step 1 (Autopoiesis → $c > 0$).** From A1 (autopoiesis) one needs $c > 0$ ([T7](#теорема-необходимость-c) [Т]): without an active Fano channel, regeneration is suppressed.

**Step 2 ($c > 0$ → full pair coverage).** From [T2](#теорема-полнота-покрытия) [Т]: $c > 0$ requires that the interaction graph $G_H$ covers **all** pairs $(i,j)$ through at least one operator $L_p$.

**Step 3 (Choi rank = 7).** From [T11](#теорема-ранг-хои) [Т]: the Choi matrix rank of the channel $\Phi_{k=3}$ equals 7.

**Step 4 (Optimal block $k = 3$).** From [T12](#теорема-проективная-декомпозиция) [Т]: the projective decomposition from L-unification requires rank-3 projectors (the minimal rank covering all pairs at $N = 7$).

**Step 5 (BIBD uniqueness).** From [T13](#теорема-bibd-из-хои) [Т]: a system of $b = 7$ rank-$k = 3$ projectors on $\mathbb{C}^7$ with full pair coverage is a $\mathrm{BIBD}(7, 3, 1)$. By Fisher's inequality and the uniqueness of the projective plane of order 2 (Veblen–Wedderburn): $\mathrm{BIBD}(7,3,1) \cong PG(2,2)$ — **unique** up to isomorphism.

**Step 6 (Relation to atomic).** The Fano projectors are expressed through the atomic ones: $\Pi_p = \sum_{k \in \text{line}_p} L_k^{\text{atom}}$. Conversely, the atomic operators are recovered from the Fano ones via: $L_k^{\text{atom}} = \frac{1}{3}\sum_{p : k \in \text{line}_p} \Pi_p - \frac{1}{3}I_7$ (from the involutory incidence matrix of the Fano plane). This is a bijective correspondence.

**Step 7 (Dynamical non-equivalence, but structural generability).** The Lindbladians $\mathcal{L}_{\text{atom}}$ and $\mathcal{L}_{\text{Fano}}$ are **different** channels (dephasing vs. partial preservation of coherences). But $\mathcal{L}_{\text{Fano}}$ is the **unique** Lindbladian simultaneously satisfying:
- CPTP [Т] (T-78)
- $G_2$-covariance [Т] (T-42a)
- Full pair coverage [Т] (T-41b)
- Primitivity [Т] (T-39a)

The atomic operators are the "alphabet"; the Fano operators are the unique "grammar" compatible with physics. $\blacksquare$
:::

## Fano-Structured Lindblad Operators $L_p^{\text{Fano}}$ {#фано-операторы}

### Definition

For each [Fano line](/docs/physics/gauge-symmetry/g2-structure) $p = (i, j, k)$ the Lindblad operator is defined as:

$$
L_p^{\text{Fano}} := \frac{1}{\sqrt{3}}\,\Pi_p = \frac{1}{\sqrt{3}}(|i\rangle\langle i| + |j\rangle\langle j| + |k\rangle\langle k|)
$$

:::tip Theorem: CPTP verification of the Fano operators [Т]
The operators $L_p^{\text{Fano}}$ satisfy the completeness condition (Complete Positivity and Trace Preservation):

$$
\sum_{p=1}^{7} (L_p^{\text{Fano}})^\dagger L_p^{\text{Fano}} = \frac{1}{3}\sum_{p=1}^{7} \Pi_p = \frac{1}{3} \cdot 3I = I \quad \checkmark
$$

Consequently, the Fano operators define a well-formed CPTP channel. Status: **[Т]**
:::

:::info Remark on the canonicity of the Fano form [Т]
The atomic operators $L_k^{\mathrm{atom}} = |k\rangle\langle k|$ and the Fano operators $L_p^{\mathrm{Fano}} = \frac{1}{\sqrt{3}}\Pi_p$ define **different** CPTP channels: $\Phi_{\mathrm{atom}}(\rho) = \mathrm{diag}(\rho)$ (complete dephasing) vs. $\Phi_{\mathrm{Fano}}(\rho) = \frac{1}{3}\sum_p \Pi_p \rho \Pi_p$ (partial). Both are well-formed CPTP channels [Т] (Kraus form → complete positivity). For all physical theorems of UHM the **canonical form is Fano** [Т], dictated by $G_2$-symmetry (T-42a [Т]).

**Stinespring dilation.** Environment $\mathcal{E} = \mathbb{C}^7$, unitary embedding $U|v\rangle|0\rangle = \sum_{p=1}^{7}(L_p|v\rangle) \otimes |p\rangle$. Check: $\langle 0|U^\dagger U|0\rangle = \sum_p L_p^\dagger L_p = \mathbb{I}_7$ ✓
:::

### Fano Predictive Channel {#фано-канал}

The Fano operators generate a **predictive channel** acting on the [coherence matrix](/docs/core/dynamics/coherence-matrix):

$$
\mathcal{P}_{\text{Fano}}(\Gamma) := \sum_{p=1}^{7} L_p^{\text{Fano}} \, \Gamma \, (L_p^{\text{Fano}})^\dagger = \frac{1}{3}\sum_{p=1}^{7} \Pi_p \, \Gamma \, \Pi_p
$$

:::tip Theorem: The Fano channel preserves coherences [Т]
For an arbitrary coherence matrix $\Gamma$:

**(a)** Diagonal elements are preserved exactly:

$$
[\mathcal{P}_{\text{Fano}}(\Gamma)]_{ii} = \gamma_{ii}
$$

**(b)** Off-diagonal elements (coherences) are preserved with a factor of $1/3$:

$$
[\mathcal{P}_{\text{Fano}}(\Gamma)]_{ij} = \frac{1}{3}\gamma_{ij} \quad \text{for all } i \neq j
$$

**(c)** The phases of coherences are preserved exactly:

$$
\arg([\mathcal{P}_{\text{Fano}}(\Gamma)]_{ij}) = \arg(\gamma_{ij}) = \theta_{ij}
$$

[Proof →](/docs/proofs/gap/fano-channel#фано-канал) | Status: **[Т]**
:::

:::info Remark: Key difference from the atomic channel
The atomic channel $\mathcal{P}_{\text{base}}(\Gamma) = \sum_m P_m \Gamma P_m = \mathrm{diag}(\Gamma)$ **destroys** all coherences ($\gamma_{ij} \to 0$ for $i \neq j$). The Fano channel **preserves** coherences with a scaling factor of $1/3$ without distorting their phases. This is critically important for [viable systems](/docs/core/dynamics/viability), where $P > P_{\mathrm{crit}}$ requires non-zero coherences.
:::

## Primitivity of $\mathcal{L}_\Omega$ {#примитивность-ℒω}

:::info DRY: Canonical formulation of the primitivity theorem
This is the **canonical definition** of primitivity of the logical Liouvillian $\mathcal{L}_\Omega$ in UHM. All documents should reference this page.

**Clarification:** primitivity is proved for the **linear part** $\mathcal{L}_0 = -i[H,\cdot] + \mathcal{D}$ (without the nonlinear regeneration term $\mathcal{R}$). The full dynamics $\mathcal{L}_\Omega = \mathcal{L}_0 + \mathcal{R}$ is nonlinear (since $\rho_* = \varphi(\Gamma)$ depends on the state) and may have **multiple** fixed points (the trivial $I/7$ plus nontrivial attractors, see [T-96](/docs/core/dynamics/evolution#теорема-нетривиальность-аттрактора)).
:::

### Definition of Primitivity

A generator $\mathcal{L}$ is called **primitive** (relaxing) if:

1. There exists a **unique** stationary state $\rho_* \in \mathcal{D}(\mathcal{H})$: $\mathcal{L}[\rho_*] = 0$
2. For **any** initial state $\rho_0 \in \mathcal{D}(\mathcal{H})$:

$$
\lim_{\tau \to \infty} e^{\tau\mathcal{L}}[\rho_0] = \rho_*
$$

Equivalent spectral formulation: all eigenvalues $\lambda_k$ of the superoperator $\mathcal{L}$ satisfy $\text{Re}(\lambda_k) \leq 0$, with $\text{Re}(\lambda_k) = 0$ only for the unique stationary mode ($\lambda_0 = 0$, multiplicity 1).

### Interaction Graph

**Definition.** The interaction graph $G_H = (V, E)$ of the Hamiltonian $H$:
- $V = \{A, S, D, L, E, O, U\}$ (7 vertices)
- $(i,j) \in E \Leftrightarrow H_{ij} \neq 0$ (an edge if there is a non-zero coupling)

### Primitivity Theorem

:::tip Theorem T-39a: Primitivity of the linear part $\mathcal{L}_0$ [Т]
Let $\mathcal{H} = \mathbb{C}^7$ be the state space of a holon satisfying (AP)+(PH)+(QG)+(V). Let $\mathcal{L}_0 = -i[H_{\text{eff}}, \cdot] + \mathcal{D}[\cdot]$ be the **linear** part of the Liouvillian (without the nonlinear regenerative term $\mathcal{R}$), with atomic operators $L_k = |k\rangle\langle k|$ and a connected interaction graph.

Then $\mathcal{L}_0$ is primitive: the unique stationary state is $I/7$, and for any $\rho_0$:

$$
\lim_{\tau \to \infty} e^{\tau\mathcal{L}_0}[\rho_0] = I/7
$$

Status: **[Т]**

:::warning Clarification: $\mathcal{L}_0$ vs $\mathcal{L}_\Omega$
Primitivity is proved for the **linear part** $\mathcal{L}_0$. The full Liouvillian $\mathcal{L}_\Omega = \mathcal{L}_0 + \mathcal{R}$ includes nonlinear regeneration and may have a **nontrivial** stationary state $\rho^* \neq I/7$ (T-96 [Т]). Primitivity of $\mathcal{L}_0$ guarantees uniqueness of $I/7$ for the dissipative part and a spectral gap $\Delta > 0$.
:::
:::

**Proof.** We apply the Evans–Spohn criterion (Evans 1977, Spohn 1976):

> A Lindblad generator $\mathcal{L}$ is primitive if and only if the fixed-point algebra $\mathcal{F}(\mathcal{L}) := \{X \in M_N(\mathbb{C}) : [X, L_k] = [X, L_k^\dagger] = [X, H] = 0 \;\forall k\}$ is trivial: $\mathcal{F}(\mathcal{L}) = \mathbb{C} \cdot I$.

**Lemma 1.** $[X, |k\rangle\langle k|] = 0$ for all $k \in \{0,\ldots,6\}$ $\Leftrightarrow$ $X$ is diagonal.

*Proof.* Matrix element of the commutator: $[X, |k\rangle\langle k|]_{mn} = x_{mk}\delta_{nk} - x_{kn}\delta_{mk}$. For $m \neq k$, $n = k$: $x_{mk} = 0$. Ranging over all $k$: $x_{ij} = 0$ for $i \neq j$. $\blacksquare$

**Lemma 2.** If $X = \text{diag}(x_0,\ldots,x_6)$, $[X, H] = 0$, and the graph $G_H$ is connected, then $X = c \cdot I$.

*Proof.* $[X, H]_{ij} = (x_i - x_j)H_{ij}$. If $H_{ij} \neq 0$ (an edge in $G_H$), then $x_i = x_j$. By connectedness of $G_H$: for any $i,j$ there exists a path along which all $x_{v_\ell}$ are equal. Hence $x_0 = \cdots = x_6 = c$. $\blacksquare$

Combining Lemmas 1 and 2: $\mathcal{F}(\mathcal{L}_\Omega) = \mathbb{C} \cdot I$. By the Evans–Spohn criterion: $\mathcal{L}_\Omega$ is primitive. $\blacksquare$

**References:**
- Evans, D. E. (1977). *Irreducible quantum dynamical semigroups.* Commun. Math. Phys. **54**, 293–297.
- Spohn, H. (1976). *An algebraic condition for the approach to equilibrium.* Lett. Math. Phys. **2**, 33–38.
- Frigerio, A. (1978). *Stationary states of quantum dynamical semigroups.* Commun. Math. Phys. **63**, 269–276.

### Connectivity Theorem

:::tip Theorem: Connectivity of $G_H$ from viability [Т]
If a 7D system satisfies (AP)+(PH)+(QG)+(V), then the interaction graph $G_H$ of its effective Hamiltonian is connected.

Status: **[Т]**
:::

*Proof.* By contradiction.

Suppose $G_H$ is disconnected. Then $V = V_1 \sqcup V_2$, $|V_1| \geq 1$, $|V_2| \geq 1$, and $H_{ij} = 0$ for all $i \in V_1$, $j \in V_2$.

Consider the action of $\mathcal{L}_\Omega$ on the inter-component coherences $\gamma_{ij}$ ($i \in V_1$, $j \in V_2$):

**Hamiltonian part:**

$$
(-i[H,\Gamma])_{ij} = -i\sum_m (H_{im}\gamma_{mj} - \gamma_{im}H_{mj})
$$

For $i \in V_1$: $H_{im} \neq 0$ only for $m \in V_1$. For $j \in V_2$: $H_{mj} \neq 0$ only for $m \in V_2$. This expression couples $\gamma_{ij}$ only to other inter-component coherences. The Hamiltonian **does not generate** inter-component coherences from intra-component ones.

**Dissipative part** (atomic dissipator):

$$
\mathcal{D}[\Gamma]_{ij} = -\gamma_{ij}(1-\delta_{ij})
$$

For $i \neq j$: $\mathcal{D}[\Gamma]_{ij} = -\gamma_{ij}$. The dissipator **exponentially suppresses** all coherences.

**Combination:** The inter-component coherences are subject to exponential decay (from the dissipator) and receive no "feed" from intra-component ones:

$$
\gamma_{ij}(\tau) \xrightarrow{\tau \to \infty} 0 \quad \text{for all } i \in V_1,\, j \in V_2
$$

Asymptotically $\Gamma$ becomes **block-diagonal**, i.e. the system dynamically splits into two subsystems of dimensions $|V_1|$ and $|V_2|$, both strictly less than 7. For each of the three key dimensions:

- If $E \in V_2$: loss $\gamma_{iE} \to 0$ for $i \in V_1$ → violation of **(PH)** (interiority loses its connection to the structural dimensions)
- If $O \in V_2$: loss $\gamma_{iO} \to 0$ for $i \in V_1$ → violation of **(QG)** (regeneration becomes impossible for subsystem $V_1$)
- If $U \in V_2$: loss $\gamma_{iU} \to 0$ for $i \in V_1$ → violation of **(AP)** (subsystem $V_1$ loses integration)

But [Theorem S](/docs/proofs/minimality/theorem-minimality-7) **[Т]** proves that (AP)+(PH)+(QG) require **at least 7** dynamically coupled dimensions. Condition **(V)** ($P > P_{\text{crit}} = 2/7$) requires a stable state. If $G_H$ is disconnected, degradation is inevitable.

Contradiction: a viable holon cannot have a disconnected $G_H$. $\blacksquare$

Connectivity of $G_H$ follows from (V) viability: the nontrivial attractor ([T-96](/docs/core/dynamics/evolution#теорема-нетривиальность-аттрактора) [Т]) has $P_{\mathrm{coh}} > 0$, and the Fano channel with $c > 0$ generates coherences for **all** pairs $(i,j)$ (full coverage), which defines a complete graph $G_H$. Details: [Theorem T2](/docs/proofs/minimality/theorem-octonionic-derivation#мост).

### Extension to the Fano Construction

:::tip Corollary: Primitivity with Fano operators [Т]
The primitivity theorem also holds for the Fano operators $L_p^{\text{Fano}} = \frac{1}{\sqrt{3}}\Pi_p$.

*Proof.* The algebra generated by $\{\Pi_p\}_{p=1}^7$ contains all atomic projections $\{|k\rangle\langle k|\}$, since $\Pi_p \Pi_q = |k\rangle\langle k|$ for two lines intersecting at point $k$. The rest follows by Lemmas 1 and 2. $\blacksquare$

Status: **[Т]**
:::

### Cascading Corollaries of Primitivity

The proof of primitivity closes **5 conditional results**, upgrading their status from [С] to [Т]:

| Result | Old status | New status | Reason |
|-----------|:---:|:---:|---|
| Equivalence (1)⇔(2) for φ | [С] | **[Т]** | Perron–Frobenius theorem applicable |
| Variational characterisation of φ (Th.3.1 FEP) | [С] | **[Т]** | Uniqueness of the stationary state |
| Spectral formula for φ (Th.2.3) | [Т] | **[Т]** (multiplicity 1) | Unique zero mode |
| Convergence $R \to 1$ (Th.4.2) | [Т] | **[Т]** (unconditionally) | Guaranteed for any initial state |
| Uniqueness of the regeneration target | implicit | **[Т]** | $\Gamma_{\text{target}} = \rho_*$ uniquely |

**Details:** [Formalisation of φ](/docs/proofs/categorical/formalization-phi), [FEP derivation](/docs/proofs/dynamics/fep-derivation)

### Uniqueness of the Fano Structure from Design Theory {#единственность-фано}

:::tip Theorem: Uniqueness of the Fano from (7,3,1)-BIBD [Т]
Among all CPTP channels on $\mathcal{D}(\mathbb{C}^7)$ constructed from projective Kraus operators $K_p = \frac{1}{\sqrt{r}}\Pi_p$ (rank-$k$ projections) satisfying:

**(a)** $\sum_p K_p^\dagger K_p = I$ (CPTP);
**(b)** $[\mathcal{P}(\Gamma)]_{ii} = \gamma_{ii}$ (population preservation);
**(c)** Democracy: each pair $(i,j)$ is contained in **exactly** $\lambda$ projections

with $\lambda = 1$ (maximal uniformity), the **unique** solution is the Fano channel $\mathcal{P}_{\text{Fano}}$ with projections onto the 7 lines of PG(2,2).

Status: **[Т]** (standard combinatorics — Hall 1967)
:::

*Proof.* Conditions (a)–(c) define a $(v,k,\lambda)$-balanced incomplete block design (BIBD): $v = 7$ points, $b$ blocks of size $k$, each point in $r$ blocks, each pair in $\lambda = 1$ blocks.

Necessary BIBD relations: $bk = vr$, $r(k-1) = \lambda(v-1) = 6$.

From $r(k-1) = 6$ with integers $r, k \geq 2$:

| $k$ | $r$ | $b = 7r/k$ | Admissibility |
|-----|-----|-----------|---|
| 2 | 6 | 21 | Formally admissible, but 21 operators is an unnatural construction |
| 3 | 3 | 7 | **(7,3,1)-BIBD** |
| 4 | 2 | 3.5 | Not an integer — forbidden |
| 7 | 1 | 1 | Trivial |

For $k = 3$: **Theorem (Hall 1967).** The $(7,3,1)$-BIBD is **unique** up to isomorphism and is isomorphic to the Fano projective plane $\text{PG}(2,2)$. Uniqueness follows from the fact that $\text{PG}(2,q)$ is unique for prime $q$, and $q = 2$ is the unique prime with $v = q^2 + q + 1 = 7$.

Properties of the unique solution:
- The Fano plane is **isomorphic** to the multiplication table of the octonions
- $\text{Aut}(\text{PG}(2,2)) \cong GL(3,\mathbb{F}_2) \cong PSL(2,7)$, order 168
- $PSL(2,7) \subset G_2 = \text{Aut}(\mathbb{O})$

$\blacksquare$

### $S_7$-Equivariance of the Atomic Dissipator {#s7-эквивариантность}

:::tip Theorem T5: $S_7$-equivariance of the atomic dissipator [Т]
Let $\mathcal{D}_\text{atom}$ be the atomic dissipator with operators $L_k = |k\rangle\langle k|$, $k = 0, \ldots, 6$. For any permutation $\sigma \in S_7$ and the corresponding unitary operator $U_\sigma: |k\rangle \mapsto |\sigma(k)\rangle$:

$$
\mathcal{D}_\text{atom}[U_\sigma \Gamma U_\sigma^\dagger] = U_\sigma \, \mathcal{D}_\text{atom}[\Gamma] \, U_\sigma^\dagger
$$

Status: **[Т]**
:::

**Proof.**

**(a)** Operator transformation: $U_\sigma L_k U_\sigma^\dagger = |\sigma(k)\rangle\langle\sigma(k)| = L_{\sigma(k)}$.

**(b)** Compute $\mathcal{D}_\text{atom}[U_\sigma \Gamma U_\sigma^\dagger] = \sum_{k}(L_k (U_\sigma \Gamma U_\sigma^\dagger) L_k^\dagger - \frac{1}{2}\{L_k^\dagger L_k, U_\sigma \Gamma U_\sigma^\dagger\})$.

**(c)** Compute $U_\sigma \mathcal{D}_\text{atom}[\Gamma] U_\sigma^\dagger = \sum_{k}(L_{\sigma(k)} (U_\sigma \Gamma U_\sigma^\dagger) L_{\sigma(k)}^\dagger - \frac{1}{2}\{L_{\sigma(k)}^\dagger L_{\sigma(k)}, U_\sigma \Gamma U_\sigma^\dagger\})$.

**(d)** Since $\sigma$ is a bijection, $\sum_{k} f(L_{\sigma(k)}) = \sum_{k} f(L_k)$. The expressions coincide. $\blacksquare$

#### Theorem T6: Uniform contraction of coherences [Т] {#теорема-равномерная-контракция}

> The atomic dissipator $\mathcal{D}_\text{atom}$ contracts **all** coherences at the same rate:
>
> $$
> \mathcal{D}_\text{atom}[\Gamma]_{ij} = -\gamma_{ij} \quad (i \neq j), \qquad \mathcal{D}_\text{atom}[\Gamma]_{ii} = 0
> $$

**Proof.** $\mathcal{D}_\text{atom}[\Gamma]_{ij} = \sum_k \langle i|k\rangle\langle k|\Gamma|k\rangle\langle k|j\rangle - \gamma_{ij} = \delta_{ij}\gamma_{ii} - \gamma_{ij}$. $\blacksquare$

**Significance.** Uniform contraction is a **structural consequence** of $S_7$-equivariance: the dissipator does not distinguish between pairs $(i,j)$. All coherences decohere with $\alpha = 1$. This proves the democracy of contraction **unconditionally** (without (КГ)).

#### Theorem T7: Autopoietic necessity of $c > 0$ [Т] {#теорема-необходимость-c}

> The atomic dissipator ($c = 0$) is incompatible with stable viability (AP)+(V): the formula for $\kappa_0$ [Т] is suppressed faster than the dissipative contribution.

**Proof.** (a) With $\alpha = 1$: $|\gamma_{ij}(\tau)| \sim e^{-\tau}$. The rate $\kappa_0 = \omega_0 |\gamma_{OE}| |\gamma_{OU}| / \gamma_{OO}$ decays exponentially. (b) Stationary purity $P^* \approx 1/N + \kappa^*/(2\alpha)$. With $\alpha = 2/3$ (Fano): $P^* \approx 1/7 + 3\kappa^*/4$ — the viability region is broader. (c) Dissipation acts on all 21 pairs, regeneration is modulated through $\gamma_{OE}$, $\gamma_{OU}$ — the coefficients are asymmetric. For stability, $c > 0$ is necessary. $\blacksquare$

#### Theorem T8: Hamming bound [Т] {#теорема-граница-хемминга}

> For a length-$n = 7$ code correcting 1 error: $2^r \geq 8$, minimum $r = 3$. The bound is achieved — the code is **perfect**. The unique one is $H(7,4)$. (Hamming 1950)

#### Theorem T9: Structure of $H(7,4)$ = PG(2,2) [Т] {#теорема-хемминг-фано}

> The codewords of weight 3 in the dual code $H(7,4)^\perp = S(3,7)$ form 7 triples — the lines of the Fano plane. (standard coding theory)

**Connection to autopoiesis.** Distinguishing 8 situations (no perturbation + 7 single-dimensional ones) requires $\lceil\log_2 8\rceil = 3$ observations — exactly 3 parity-check bits of $H(7,4)$. The number 3 coincides with $K = 3$ (triadic decomposition [Т]), $k = 3$ (Fano block size), $d = 3$ (code distance).

#### Theorem T10: Autopoietic optimality of the Fano channel [Т] {#теорема-оптимальность-фано}

> Among $S_7$-invariant BIBD$(7,k,1)$ channels ($k \in \{2,3\}$) satisfying $c > 0$ (T7), full pair coverage (T2), and democracy (T6), the **unique optimal** one is the Fano channel ($k=3$, $c=1/3$): it strictly dominates in contraction rate, stationary purity, number of operators, and $G_2$-covariance.

---

### Closing the Bridge (AP)+(PH)+(QG)+(V) ⇒ P1+P2 [Т] {#редукция-моста}

Sixteen theorems (T1–T16) generate a **complete chain of implications**, all steps being theorems [Т] (T16/ПИР is reclassified [О] — a definition embedded in A1+A2; computational results are unaffected):

$$
\boxed{(AP)+(PH)+(QG)+(V)} \xrightarrow{[\text{Т}]} N = 7 \xrightarrow{[\text{Т}]} \text{связность } G_H \xrightarrow{[\text{Т}]} \forall(i,j):\,\lambda_{ij} \geq 1
$$

$$
\xrightarrow{[\text{Т}]} S_7\text{-равномерность} \xrightarrow{[\text{Т}]} k = 3 \xrightarrow{[\text{Т}]} \text{ранга-3 проекторы} \xrightarrow{[\text{Т}]} b = 7
$$

$$
\xrightarrow{[\text{Т}]} \text{BIBD}(7,3,1) = \text{PG}(2,2) \xrightarrow{[\text{Т}]} \mathbb{O} \xrightarrow{[\text{Т}]} G_2 \xrightarrow{[\text{Т}]} P1+P2
$$

#### Theorem T1: Equivalence of BIBD channels [Т] {#теорема-bibd-эквивалентность}

> All $(v,k,\lambda)$-BIBD channels with the same $v$ and $k$ (but arbitrary $\lambda$) generate **the same** CPTP channel. The coherence contraction $c = (k-1)/(v-1)$ depends only on $(v,k)$.

**Proof.** For the BIBD channel $\Phi_{\mathcal{B}}(\Gamma) = \frac{1}{r}\sum_p \Pi_p\Gamma\Pi_p$: diagonal elements $[\Phi]_{ii} = \gamma_{ii}$ (each point in $r$ blocks), off-diagonal $[\Phi]_{ij} = \frac{\lambda}{r}\gamma_{ij} = \frac{k-1}{v-1}\gamma_{ij}$ (from the BIBD relation $r(k-1) = \lambda(v-1)$). The expression does not depend on $\lambda$. $\blacksquare$

**Corollary T1.1.** For $v=7$, $k=3$: the contraction $c = 1/3$ is the same for the Fano channel ($\lambda=1$, $b=7$) and any $(7,3,\lambda)$-BIBD channel. The choice $\lambda=1$ is **forced** by Theorems T11–T13 [Т]: Choi rank of the channel = 7 (minimal decomposition), L-unification yields projective operators, and 7 rank-3 projectors with contraction 1/3 form a BIBD$(7,3,1)$.

#### Theorem T2: Full pair coverage [Т] {#теорема-полнота-покрытия}

> Let $\Phi$ be a projective CPTP observation channel on $\mathcal{D}(\mathbb{C}^7)$. If the interaction graph $G_H$ is connected [Т] and the Liouvillian is primitive [Т], then every pair $(i,j)$ must be covered by at least one block: $\lambda_{ij} \geq 1$.

**Proof.** (a) Connectivity of $G_H$ is proved from (AP)+(PH)+(QG)+(V) + Theorem S [Т]. (b) Primitivity of $\mathcal{L}_\Omega$ [Т] and connectivity of $G_H$ guarantee $\gamma^*_{ij} \neq 0$ for all $i \neq j$ in the stationary $\rho_*$. (c) If $\lambda_{ij} = 0$, then $[\Phi(\Gamma)]_{ij} = 0$ — the channel is "blind" to the coupling $(i,j)$, the self-model contains no information about the non-zero coupling $\gamma^*_{ij}$, which contradicts (AP). $\blacksquare$

#### Theorem T3: Democracy of coverage [Т] {#теорема-демократичность}

:::warning Superseded by T6 [Т]
T3 proved the democracy of coverage $\lambda_{ij} = \lambda$. **The theorem is fully superseded** by the unconditional T6 ($S_7$-equivariance → uniform contraction [Т]) and the chain T11–T13 ($\lambda = 1$ from Choi rank + L-unification).
:::

#### Theorem T4: Optimal block size k=3 [Т] {#теорема-оптимальный-k}

> Among admissible non-trivial BIBD$(7,k,1)$ channels ($k \in \{2,3\}$; $k \in \{4,5,6\}$ do not admit integer BIBD parameters; $k=7$ is trivial), the channel with $k=3$ **strictly dominates**:

| Criterion | $k=2$ | $k=3$ | Best |
|----------|:---:|:---:|:---:|
| Contraction $c(k)$ | 1/6 | **1/3** | $k=3$ |
| Number of Kraus operators $b$ | 21 | **7** | $k=3$ |
| Purity loss $1-c^2$ | 35/36 | **8/9** | $k=3$ |
| $G_2$-covariance | **No** [Т] | **Yes** [Т] | $k=3$ |

$k=3$ is the **unique** admissible size with $G_2$-covariance and optimal coherence preservation. $\blacksquare$

**Additional arguments:** (1) The triadic decomposition [Т] (§[below](#триадная-декомпозиция)) establishes exactly $K=3$ types of dynamics — the block size $k=3$ coincides with the number of types. (2) Theorem T7 [Т] (§[above](#теорема-необходимость-c)) proves the necessity of $c > 0$, excluding the atomic channel. (3) Theorem T10 [Т] (§[above](#теорема-оптимальность-фано)) gives the full optimality of $k=3$. (4) The Hamming code $H(7,4)$ [Т] (Theorems T8, T9) provides an information-theoretic justification of the Fano structure. (5) Theorems T11–T13 [Т] (§[below](#теорема-ранг-хои)) prove that $\lambda = 1$ is **forced** by the Choi rank + L-unification, closing the bridge.

#### Theorem T11: Choi rank of the channel $\Phi_{k=3}$ [Т] {#теорема-ранг-хои}

> The CPTP channel $\Phi_{k=3}$ on $\mathcal{D}(\mathbb{C}^7)$ with contraction $[\Phi]_{ij} = \gamma_{ii}\delta_{ij} + \frac{1}{3}\gamma_{ij}(1-\delta_{ij})$ has **Choi rank** equal to 7.

**Proof.** The Choi matrix $C_\Phi = \sum_{i,j} c_{ij}|ii\rangle\langle jj|$ has support on $V = \mathrm{span}\{|ii\rangle\}$. The restriction $C_V = \frac{2}{3}I_7 + \frac{1}{3}J_7$ (where $J_7$ is the all-ones matrix). Spectrum: $\{3, \frac{2}{3}, \ldots, \frac{2}{3}\}$ — all eigenvalues strictly positive, $\mathrm{rank}(C_\Phi) = 7$. By the Choi rank theorem: the minimum number of Kraus operators = 7. $\blacksquare$

**Corollary T11.1.** The Fano decomposition (7 operators $L_p^{\text{Fano}} = \frac{1}{\sqrt{3}}\Pi_p$) is the **rank-minimal** Kraus decomposition.

#### Theorem T12: Projective decomposition from L-unification [Т] {#теорема-проективная-декомпозиция}

> Given L-unification [Т] ($L_k = |k\rangle\langle k|$) and optimal block size $k = 3$ [Т], the composite observation operators take the form of **rank-3 orthogonal projectors**: $K_p = \frac{1}{\sqrt{r}}\Pi_p$, $\Pi_p = \sum_{m \in B_p} |m\rangle\langle m|$, $|B_p| = 3$.

**Proof.** L-unification defines the atomic $L_k = |k\rangle\langle k|$ as rank-1 projectors. A composite observation with block $B_p$ is a coarsening (Lüders, 1951): $\Pi_p = \sum_{m \in B_p} L_m$ — a rank-3 projector ($\Pi_p^2 = \Pi_p$). Non-projective decompositions are excluded: observation via $\Omega$ is **by definition** projective. $\blacksquare$

#### Theorem T13: BIBD$(7,3,1)$ from the minimal projective decomposition [Т] {#теорема-bibd-из-хои}

> Suppose the channel $\Phi_{k=3}$ is decomposed into $b = 7$ rank-3 diagonal projectors. Then the block system is a **BIBD**$(7,3,1) = \text{PG}(2,2)$.

**Proof.** (a) Regularity: CPTP preservation $[\Phi]_{ii} = \gamma_{ii}$ requires $r_i = r$ for all $i$; from $7r = 21$: $r = 3$. (b) Uniform coverage: contraction $c = 1/3$ for **all** pairs (T1 [Т]) gives $\lambda_{ij}/r = 1/3$, hence $\lambda_{ij} = 1$. (c) Parameters $v=7, b=7, k=3, r=3, \lambda=1$ define a BIBD$(7,3,1)$. By uniqueness (Kirkman 1847): $S(2,3,7) = \text{PG}(2,2)$. $\blacksquare$

#### Theorem T14: Max-min optimality of BIBD [Т] {#теорема-maxmin}

> Among regular block designs $(v=7, k=3, \lambda_{ij} \geq 1)$, BIBD$(7,3,1)$ **maximises** $\min_{i \neq j}\lambda_{ij}/r$.

**Proof.** The average contraction $\bar{c} = 1/3$ does not depend on the design. By the max-min inequality: $\min c_{ij} \leq \bar{c} = 1/3$, with equality only when $\lambda_{ij} = 1$ for all pairs = BIBD. $\blacksquare$

**Significance for autopoiesis:** $\kappa_0 \propto |\gamma_{OE}| \cdot |\gamma_{OU}|$ — the minimal contraction defines the "bottleneck". BIBD is optimal for stable viability.

#### Theorem T15: Closing the bridge [Т] {#замыкание-моста}

> **Theorem T15.** $(AP)+(PH)+(QG)+(V) \Longrightarrow P1 + P2$ — complete chain, **all steps are theorems [Т]**.

:::info Final bridge status: [Т] — fully closed

| Step | Implication | Status |
|-----|-----------|--------|
| 1 | (AP)+(PH)+(QG) ⟹ $N \geq 7$ | **[Т]** Theorem S |
| 2 | $N=7$ + (V) ⟹ connectivity of $G_H$ | **[Т]** Evans–Spohn |
| 3 | Connectivity + primitivity ⟹ $\lambda_{ij} \geq 1$ | **[Т]** Theorem T2 |
| 4 | $S_7$-equivariance ⟹ uniform contraction | **[Т]** Theorems T5, T6 |
| 5 | Admissibility + (AP)+(V) ⟹ $k=3$ | **[Т]** Theorems T4, T7, T10 |
| 6 | L-unification + $k=3$ ⟹ rank-3 projective operators | **[Т]** Theorem T12 |
| 7 | Choi rank = 7 ⟹ $b \geq 7$ | **[Т]** Theorem T11 |
| 8 | $b=7, k=3, v=7$, contraction $1/3$ ⟹ BIBD$(7,3,1)$ | **[Т]** Theorem T13 |
| 9 | $(7,3,1)$-BIBD ≅ PG(2,2) | **[Т]** Hall 1967 |
| 10 | PG(2,2) ≅ multiplication table of Im($\mathbb{O}$) | **[Т]** standard algebra |
| 11 | $\mathrm{Aut}(\mathbb{O}) = G_2$ | **[Т]** standard Lie theory |
| 12 | $\mathbb{O}$ — normed non-associative division algebra ⟹ P1+P2 | **[Т]** definition |

The bridge is closed **[Т]** (T-15) — a complete chain of 12 steps, all theorems. Condition (МП) follows as a direct consequence of T11 + T12 + T13. Cascading corollaries: P1, P2 **[Т]**; Track B ($\mathbb{O} \Rightarrow N=7$) **[Т]**; $G_2$-structure, Fano plane, Hamming code, double extremality — all **[Т]**.

See [Status registry](/docs/reference/status-registry), [Octonionic derivation](/docs/proofs/minimality/theorem-octonionic-derivation#мост).
:::

---

## Triadic Decomposition of Holonomic Dynamics {#триадная-декомпозиция}

:::info DRY: Canonical formulation of the triadic decomposition
This is the **canonical definition** of the triadic decomposition of holonomic dynamics in UHM. All documents should reference this page.
:::

:::tip Theorem: Triadic decomposition [Т]
The axiomatic system {A1, A2, A3, A4, A5} generates **exactly three** structurally distinct types of dynamical contributions to the evolution of the coherence matrix Γ:

$$
\frac{d\Gamma}{d\tau} = \underbrace{-i[H_{\text{eff}}, \Gamma]}_{\text{Aut: automorphisms (A5)}} + \underbrace{\mathcal{D}_\Omega[\Gamma]}_{\text{Left adjoint (A1)}} + \underbrace{\mathcal{R}[\Gamma, E]}_{\text{Right adjoint (A1+A4)}}
$$

These three types:
1. **Structure-preserving** (automorphism): $-i[H_{\text{eff}}, \Gamma]$ — preserves the spectrum of Γ
2. **Structure-forgetting** (left adjoint): $\mathcal{D}_\Omega[\Gamma]$ — dissipation towards $I/N$
3. **Structure-restoring** (right adjoint): $\mathcal{R}[\Gamma, E]$ — regeneration towards $\rho_*$

are **exhaustive** within the axiomatic system.

Status: **[Т]**
:::

### Proof

**Step 1. Generation of each type by the axioms.**

**(a) Type 1: Hamiltonian from A5.** Axiom A5 (Page–Wootters) establishes the tensor decomposition $\mathcal{H} = \mathcal{H}_O \otimes \mathcal{H}_{\text{rest}}$ and the constraint $H_{\text{total}}|\Psi\rangle = 0$, from which $H_{\text{eff}} = \mathrm{Tr}_O(H_{\text{total}} \cdot |\tau\rangle\langle\tau|_O)$. The unitary group $\{e^{-iH_{\text{eff}}\tau}\}$ is an automorphism of $\mathcal{D}(\mathbb{C}^7)$ (Stone's theorem) [Т].

**(b) Type 2: Dissipation from A1.** Axiom A1 (∞-topos) defines the classifier Ω with atoms $S_k$. [L-unification](#примитивность-ℒω) (Th. 15.1, [Т]): $L \cong \Omega \cong \text{source}(L_k)$ generates the Lindblad operators $L_k$ forming the dissipator. Stationary state: maximally mixed $I/N$ [Т].

**(c) Type 3: Regeneration from A1+A4.** The adjunction $\mathcal{D}_\Omega \dashv \mathcal{R}$ (Th. 15.3.1, [Т]) generates $\mathcal{R}[\Gamma, E] = \kappa(\Gamma) \cdot (\rho_* - \Gamma) \cdot g_V(P)$ with $\kappa_0 = \omega_0 \cdot |\gamma_{OE}| \cdot |\gamma_{OU}| / \gamma_{OO}$, where $\omega_0$ is from A4. Stationary state: $\rho_*$ (unique, [primitivity](#примитивность-ℒω) [Т]).

**Step 2. Structural distinguishability.**

| Property | Aut (Hamiltonian) | 𝒟 (Dissipation) | ℛ (Regeneration) |
|----------|:---:|:---:|:---:|
| Generator spectrum | Purely imaginary | Re < 0 | Re < 0 |
| Action on P | Preserves | Decreases | Increases |
| Fixed point | Kernel of $[H,\cdot]$ | $I/N$ | $\rho_*$ |
| Categorical type | Automorphism | Left adjoint | Right adjoint |
| Reversibility | Reversible ($U^\dagger$) | Irreversible | Irreversible |

**Step 3. Exhaustiveness.** A2 (Bures) is a metric constraint that **does not generate** dynamics. A3 ($N = 7$) is a dimension constraint that **does not generate** dynamics. All dynamical contributions are generated only by A1, A4, A5.

**Step 4. Impossibility of a 4th type.** Any additional functor $\mathcal{X}$ would require a new classifier $\Omega' \neq \Omega$ (but A1 defines a unique Ω), a new adjunction (but [L-unification](#примитивность-ℒω) [Т] establishes uniqueness), or a new axiom (but A1–A5 exhaust all dynamical contributions). $\blacksquare$

#### Completeness of the triadic decomposition (T-57) [Т] {#полнота-триадной-декомпозиции}

:::tip Theorem (Impossibility of a 4th type of dynamics) [Т]
An arbitrary generator of a Markovian semigroup on $M_7(\mathbb{C})$ compatible with A1–A5 decomposes into $\mathcal{L} = \mathcal{L}_{\text{Ham}} + \mathcal{L}_{\text{diss}} + \mathcal{L}_{\text{reg}}$ — no other components exist.

**Proof:** The LGKS theorem (1976) gives a unique decomposition into Hamiltonian and dissipative parts. The dissipative part is uniquely split into $\mathcal{D}$ (Fano contraction, $dP/d\tau \leq 0$) and $\mathcal{R}$ (replacement channel, $dP/d\tau \geq 0$) under the constraints of A5 (PW-anchoring of $\mathcal{R}$ to the O-sector), Fano-structuredness of $\mathcal{D}$, and $G_2$-covariance.
:::

### Corollary: K = 3 for the reflexion threshold {#следствие-k3}

The triadic decomposition defines **exactly three** behavioural modes of the system: autonomous (ℛ dominates, attractor $\rho_*$), chaotic (𝒟 dominates, attractor $I/N$), external (Aut dominates, attractor $\sigma_{\text{env}}$). The number of competing hypotheses $K = 3$ is a structural consequence of the axioms, not a postulate.

Hence: $R_{\text{th}} = 1/K = 1/3$ **[Т]** — see [Theorem on the reflexion threshold](/docs/core/foundations/axiom-septicity#теорема-порог-рефлексии).

---

## Compositional Fano Morphisms {#композиционные-фано-морфизмы}

Fano-structured dissipation is not merely "noise": successive applications of the Fano projectors $\Pi_p$ generate *compositional symbols* — a discrete language of state transitions. Each chain of projections $\Pi_{p_1} \circ \Pi_{p_2} \circ \cdots \circ \Pi_{p_n}$ specifies a unique (for generic $\Gamma$) image in $\mathcal{D}(\mathbb{C}^7)$, turning the 7 Fano operators into an **alphabet** with an exponentially growing vocabulary. This is the mathematical foundation of the theory of language in UHM: the structure of decoherence itself defines the grammar of possible transitions between states of consciousness.

#### Theorem T-114: Fano grammar [Т] {#теорема-фано-грамматика}

The Markov chain on the lines of PG(2,2) with transition matrix $M_{ij} = (1 + \lambda \cdot \mathrm{Inc}(i,j)) / Z_i$, where $\mathrm{Inc}(i,j) = |\mathrm{line}(i) \cap \mathrm{line}(j)|$ is the incidence matrix of PG(2,2), is **ergodic** and generates a regular language over the alphabet $\{1,\ldots,7\}$.

**Proof:**
1. **Connectivity of PG(2,2):** Each line contains 3 points, each point lies on 3 lines. The incidence graph has diameter 2 → **connected**
2. **Aperiodicity:** $M_{ii} = 1/Z_i > 0$ (self-loops, $\mathrm{Inc}(i,i) = 3$)
3. **Ergodicity:** Connectivity + aperiodicity → ergodic (Perron–Frobenius). PG(2,2) is self-dual → the graph is regular → stationary distribution $\pi_i = 1/7$ ∎

Specification: language-limits-preveal.md §2.4–2.5 | Status: **[Т]**

#### Theorem T-115: Algebraic distinguishability of compositions [Т] {#теорема-различимость-композиций}

For generic $\Gamma \in V$ (with 7 distinct eigenvalues and non-zero off-diagonal coherences):

$$|\mathrm{Comp}(n)| = 7^n$$

The set of $\Gamma$ with collisions is an algebraic submanifold of codimension $\geq 1$ (measure zero in $\mathcal{D}(\mathbb{C}^7)$).

**Proof:**
1. The Fano projectors $\Pi_p$ are pairwise distinct (T-82 [Т]) with images in general position
2. For generic $\Gamma$: distinct projections $m_{p_i}(\Gamma) \neq m_{p_j}(\Gamma)$ when $p_i \neq p_j$ (rank-3 projection onto distinct 3-dimensional subspaces)
3. Induction on $n$: a collision $m_{p_1:n}(\Gamma) = m_{q_1:n}(\Gamma)$ for $(p_1,\ldots,p_n) \neq (q_1,\ldots,q_n)$ defines an algebraic equation → submanifold of codimension $\geq 1$ ∎

:::warning Caveat: diagonal $\Gamma$ — compositionality deficit
For a **diagonal** $\Gamma$ (all $\gamma_{ij} = 0$ for $i \neq j$) the Fano projectors act as $\Pi_p \cdot \mathrm{diag}(\gamma) \cdot \Pi_p = \mathrm{diag}(\Pi_p \gamma)$, which generates only **linear** growth of distinguishable symbols:

$$|\mathrm{Comp}(n)|_{\mathrm{diag}} = O(7n)$$

In particular: $|\mathrm{Comp}(2)|_{\mathrm{diag}} \approx 14$ (instead of 49), $|\mathrm{Comp}(3)|_{\mathrm{diag}} \approx 21$ (instead of 343).

**Reason:** On the diagonal $\mathbb{R}^7$, rank-3 Fano projectors generate only $\binom{7}{3} = 35$ distinct 3-element sums, but collisions $\sum_{k \in l_p} \gamma_k = \sum_{k \in l_q} \gamma_k$ are abundant when $\gamma_k = 1/7$. Full exponential compositionality $7^n$ requires working with the full (off-diagonal) matrix $\Gamma$.
:::

Specification: language-limits-preveal.md §2.4–2.5 | Status: **[Т]**

---

## $G_2$-Covariance of the Fano Dissipator {#g2-ковариантность}

The group $G_2 = \mathrm{Aut}(\mathbb{O})$ preserves octonionic multiplication and therefore the [Fano structure](/docs/physics/gauge-symmetry/g2-structure). This gives rise to a fundamental distinction between the atomic and Fano dissipators.

:::warning Theorem: The atomic dissipator is NOT $G_2$-covariant [Т]
The dissipative channel with atomic operators $L_k = |k\rangle\langle k|$ **is not** $G_2$-covariant:

$$
\exists\, g \in G_2: \quad \mathcal{D}_{\text{atom}}[g\Gamma g^\dagger] \neq g \, \mathcal{D}_{\text{atom}}[\Gamma] \, g^\dagger
$$

The violation arises because the operation $\mathrm{diag}(\cdot)$ does not commute with $G_2$-transformations: $\mathrm{diag}(g\Gamma g^\dagger) \neq g \cdot \mathrm{diag}(\Gamma) \cdot g^\dagger$ for general $g \in G_2$.

[Proof →](/docs/proofs/gap/fano-channel) | Status: **[Т]**
:::

:::tip Theorem: The Fano dissipator is $G_2$-covariant [Т]
The dissipative channel with Fano-structured operators $L_p^{\text{Fano}}$ **is** $G_2$-covariant:

$$
\forall\, g \in G_2: \quad \mathcal{D}_{\text{Fano}}[g\Gamma g^\dagger] = g \, \mathcal{D}_{\text{Fano}}[\Gamma] \, g^\dagger
$$

The proof relies on the fact that $G_2$ **permutes** the Fano lines: $g \Pi_p g^\dagger = \Pi_{\sigma_g(p)}$, where $\sigma_g$ is a permutation of lines. When summing over all 7 lines, reindexing does not change the result.

[Proof →](/docs/proofs/gap/fano-channel) | Status: **[Т]**
:::

### Degree of $G_2$-Violation under Mixed Observation

For the canonical [coherence-preserving self-modelling](/docs/proofs/categorical/formalization-phi) with parameter $\alpha$ (balance between atomic and Fano observation):

$$
\mathcal{P}_\alpha = \alpha \, \mathcal{P}_{\text{base}} + (1 - \alpha) \, \mathcal{P}_{\text{Fano}}
$$

the measure of $G_2$-symmetry violation is defined as:

$$
\Delta_{G_2}(\alpha) := \sup_{g \in G_2} \|\mathcal{P}_\alpha \circ \mathrm{Ad}_g - \mathrm{Ad}_g \circ \mathcal{P}_\alpha\|_{\text{op}}
$$

| $\alpha$ | Mode | $G_2$-covariance | Gauge reduction |
|----------|-------|---------------------|----------------------|
| $0$ | Purely Fano | Full ($\Delta_{G_2} = 0$) | $48 \to 34$ parameters |
| $\alpha^* \in (0,1)$ | Mixed (optimal) | Partial ($\Delta_{G_2} = \alpha^* \cdot \Delta_{\max}$) | Intermediate |
| $1$ | Purely atomic | Broken ($\Delta_{G_2} = \Delta_{\max}$) | No reduction (48 parameters) |

:::info Remark: The price of self-knowledge [И]
Self-observation (non-zero $\alpha$) **partially breaks** the algebraic symmetry of the octonions. The deeper the self-knowledge (the larger $\alpha$), the more the $G_2$-symmetry is broken and the more parameters are needed to describe the system. This is the fundamental "price of self-knowledge": knowledge about oneself increases the complexity of self-description.

The reduction $48 \to 34$ at $\alpha = 0$ is a consequence of the [$G_2$-rigidity theorem](/docs/proofs/categorical/uniqueness-theorem#g2-ригидность) [Т]: the gauge group = $G_2$ (14 parameters), the physical space = $\mathcal{D}(\mathbb{C}^7)/G_2$.
:::

## Connections

- **Derived from:** [Axiom Ω⁷](/docs/core/foundations/axiom-omega) → stratification → $L_k$ (atomic); Fano plane → $L_p^{\text{Fano}}$ (composite)
- **Used in:** [Evolution](/docs/core/dynamics/evolution), [Viability](/docs/core/dynamics/viability), [Emergent time](/docs/core/operators/emergent-time)
- **L-unification:** [Correspondence with physics](/docs/proofs/physics/physics-correspondence#2-l-унификация)
- **Fano channel:** [G₂-structure](/docs/physics/gauge-symmetry/g2-structure) — Lindblad via structure constants $f_{ijk}$
- **Proofs:** [Fano channel and Gap theorems](/docs/proofs/gap/fano-channel) — rigorous proofs of CPTP, coherence preservation, $G_2$-covariance
- **Categorical foundation:** [Categorical formalism](/docs/proofs/categorical/categorical-formalism) — derivation of $L_k$ from atoms of the classifier $\Omega$
- **Representation uniqueness:** [$G_2$-rigidity theorem](/docs/proofs/categorical/uniqueness-theorem) — the holonomic representation is unique up to $G_2$; 34 = 48 − 14 physical parameters
- **Gap dynamics:** [Gap dynamics](/docs/core/dynamics/gap-dynamics) — application of Fano operators in the dynamics of Gap profiles
