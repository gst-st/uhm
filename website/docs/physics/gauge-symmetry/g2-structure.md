---
sidebar_position: 1
title: "G₂-Structure and the Fano Plane"
---

# G₂-Structure and the Fano Plane

:::info For whom this chapter is intended
The group $G_2 = \mathrm{Aut}(\mathbb{O})$ and the Fano plane $\mathrm{PG}(2,2)$ as the central algebraic structures of UHM theory. The reader will learn how the multiplication table of the octonions determines the physical architecture of the theory.
:::


## Overview

The group $G_2 = \mathrm{Aut}(\mathbb{O})$ — the automorphism group of the octonions — is the central algebraic structure of UHM theory. The Fano plane $\mathrm{PG}(2,2)$ encodes the multiplication table of the imaginary units of $\mathbb{O}$ and determines the entire physical architecture of the theory: from Lindblad operators to gauge symmetries and selection rules.

---

## 1. Fano Plane PG(2,2)

### 1.1 Definition

The **Fano plane** $\mathrm{PG}(2,2)$ is the minimal finite projective plane. It contains:
- **7 points**, identified with the 7 imaginary units of the octonions $e_1, \ldots, e_7$, and in UHM theory — with the 7 dimensions $\{A, S, D, L, E, U, O\} = \{1, 2, 3, 4, 5, 6, 7\}$
- **7 lines**, each containing exactly 3 points

### 1.2 Table of Fano Lines {#12-таблица-фано-линий}

| # | Fano line | Dimensions |
|---|-----------|-----------|
| 1 | $\{1, 2, 4\}$ | $\{A, S, L\}$ |
| 2 | $\{2, 3, 5\}$ | $\{S, D, E\}$ |
| 3 | $\{3, 4, 6\}$ | $\{D, L, U\}$ |
| 4 | $\{4, 5, 7\}$ | $\{L, E, O\}$ |
| 5 | $\{5, 6, 1\}$ | $\{E, U, A\}$ |
| 6 | $\{6, 7, 2\}$ | $\{U, O, S\}$ |
| 7 | $\{7, 1, 3\}$ | $\{O, A, D\}$ |

### 1.3 Fundamental Properties

1. **Through any two points there passes exactly one line.** This means that every pair of dimensions $(i, j)$ uniquely determines a Fano line $(i, j, k)$.

2. **Each point lies on exactly 3 lines.** Consequently:

$$\sum_{p=1}^{7} \Pi_p = 3I$$

where $\Pi_p = \sum_{i \in \mathrm{line}_p} |i\rangle\langle i|$ is the projector onto the subspace corresponding to Fano line $p$.

3. **Octonion structure constants** $f_{ijk}$: $f_{ijk} = \pm 1$ if and only if $\{i, j, k\}$ is a Fano line, and $f_{ijk} = 0$ otherwise. The multiplication table of $\mathbb{O}$:

$$e_i \cdot e_j = f_{ijk}\, e_k - \delta_{ij}$$

### 1.4 Automorphism Group

$$\mathrm{Aut}(\mathrm{PG}(2,2)) = \mathrm{PSL}(2,7)$$

This is the group of order 168, isomorphic to $\mathrm{GL}(3, \mathbb{F}_2)$. It acts transitively on both points and lines.

---

## 2. Octonionic Multiplication and $G_2$ {#октонионное-умножение-и-g2}

### 2.1 The Octonion Algebra $\mathbb{O}$

The octonions are an 8-dimensional real division algebra. Each octonion is written as:

$$x = x_0 \cdot 1 + \sum_{i=1}^{7} x_i \, e_i, \quad x_0, x_i \in \mathbb{R}$$

where $1$ is the real unit, and $e_1, \ldots, e_7$ are imaginary units satisfying:

$$e_i^2 = -1, \quad e_i \cdot e_j = -e_j \cdot e_i \;\; (i \neq j)$$

In UHM theory the imaginary units are identified with the 7 dimensions: $e_1 = A$, $e_2 = S$, $e_3 = D$, $e_4 = L$, $e_5 = E$, $e_6 = U$, $e_7 = O$.

### 2.2 Octonion Multiplication Table

The multiplication of imaginary units is **completely** determined by the Fano plane. For each Fano line $(i, j, k)$ with canonical ordering:

$$e_i \cdot e_j = e_k, \quad e_j \cdot e_k = e_i, \quad e_k \cdot e_i = e_j$$

| $\times$ | $e_1$ (A) | $e_2$ (S) | $e_3$ (D) | $e_4$ (L) | $e_5$ (E) | $e_6$ (U) | $e_7$ (O) |
|----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
| $e_1$ (A) | $-1$ | $e_4$ | $-e_7$ | $-e_2$ | $e_6$ | $-e_5$ | $e_3$ |
| $e_2$ (S) | $-e_4$ | $-1$ | $e_5$ | $e_1$ | $-e_3$ | $e_7$ | $-e_6$ |
| $e_3$ (D) | $e_7$ | $-e_5$ | $-1$ | $e_6$ | $e_2$ | $-e_4$ | $-e_1$ |
| $e_4$ (L) | $e_2$ | $-e_1$ | $-e_6$ | $-1$ | $e_7$ | $e_3$ | $-e_5$ |
| $e_5$ (E) | $-e_6$ | $e_3$ | $-e_2$ | $-e_7$ | $-1$ | $e_1$ | $e_4$ |
| $e_6$ (U) | $e_5$ | $-e_7$ | $e_4$ | $-e_3$ | $-e_1$ | $-1$ | $e_2$ |
| $e_7$ (O) | $-e_3$ | $e_6$ | $e_1$ | $e_5$ | $-e_4$ | $-e_2$ | $-1$ |

Each row and column contains all 7 imaginary units exactly once (up to sign) — a division algebra.

### 2.3 The Group $G_2 = \mathrm{Aut}(\mathbb{O})$

**Definition.** The group $G_2$ is the group of all $\mathbb{R}$-linear bijections $g: \mathbb{O} \to \mathbb{O}$ preserving multiplication:

$$G_2 = \{g \in \mathrm{GL}(\mathbb{O}) : g(xy) = g(x)g(y) \; \forall x, y \in \mathbb{O}\}$$

Since $g(1) = 1$ for any automorphism, $g$ acts on the 7-dimensional subspace of imaginary octonions $\mathrm{Im}(\mathbb{O}) \cong \mathbb{R}^7$.

:::tip[Status: Theorem \[T\]]
$G_2$ is an exceptional compact simple Lie group with the following characteristics:
- $\dim(G_2) = 14$
- $\mathrm{rank}(G_2) = 2$
- $G_2 \subset \mathrm{SO}(7)$ — a proper subgroup of the rotation group of $\mathbb{R}^7$
:::

**Why $\dim(G_2) = 14$?** The group $\mathrm{SO}(7)$ has dimension $7 \cdot 6 / 2 = 21$. The condition of preserving octonionic multiplication imposes 7 independent constraints (one per Fano line): $g(e_i \cdot e_j) = g(e_i) \cdot g(e_j)$ for all $(i,j,k) \in \mathrm{PG}(2,2)$. Total:

$$\dim(G_2) = 21 - 7 = 14$$

**Why $\mathrm{rank}(G_2) = 2$?** The maximal torus of $G_2$ is two-dimensional: it is generated by two commuting rotations in $\mathbb{R}^7$ compatible with all 7 Fano lines. Two independent angles $(\theta_1, \theta_2)$ parametrise the maximal torus, yielding 2 quantum numbers — Noether charges (see [G₂-Noether Charges](/docs/physics/gauge-symmetry/noether-charges)).

### 2.4 Fourteen Generators of $G_2$ {#генераторы-g2}

The Lie algebra $\mathfrak{g}_2$ has 14 generators, which can be decomposed with respect to the representations of the subgroup $\mathrm{SU}(3) \subset G_2$:

$$\mathfrak{g}_2 = \mathfrak{su}(3) \oplus \mathbb{C}^3$$

| Type | Count | $\mathrm{SU}(3)$ representation | Physical interpretation in UHM |
|-----|-------|-------------------------------|-------------------------------|
| $\mathrm{SU}(3)$ generators | 8 | $\mathbf{8}$ (adjoint) | Gauge transformations between triples of dimensions on a single Fano line; analogue of gluon fields |
| Additional generators | 6 | $\mathbf{3} \oplus \bar{\mathbf{3}}$ | Transformations mixing dimensions from **different** Fano lines; 'inter-line' rotations |

All 14 generators are anti-Hermitian $7 \times 7$ matrices $T_a \in \mathfrak{so}(7)$ satisfying:

$$[T_a, T_b] = f_{ab}^{\;\;c}\, T_c, \quad a, b, c = 1, \ldots, 14$$

where $f_{ab}^{\;\;c}$ are the structure constants of $\mathfrak{g}_2$.

### 2.5 Example: Octonionic Multiplication and Non-associativity {#пример-октонионное-умножение}

The octonions are the **unique** normed division algebra that is **non-associative**. Let us demonstrate this with a concrete example.

**Problem.** Compute $(e_1 \cdot e_2) \cdot e_3$ and $e_1 \cdot (e_2 \cdot e_3)$ and verify that the results differ.

**Step 1.** From the multiplication table (Fano line $\{1,2,4\}$):

$$e_1 \cdot e_2 = e_4 \quad (\text{A} \cdot \text{S} = \text{L})$$

**Step 2.** Now multiply the result by $e_3$ (Fano line $\{3,4,6\}$):

$$(e_1 \cdot e_2) \cdot e_3 = e_4 \cdot e_3 = -e_6 \quad (\text{L} \cdot \text{D} = -\text{U})$$

(the minus sign — because the canonical orientation of line $\{3,4,6\}$ gives $e_3 \cdot e_4 = e_6$, and we are multiplying in the reverse order).

**Step 3.** Separately compute the right bracket (Fano line $\{2,3,5\}$):

$$e_2 \cdot e_3 = e_5 \quad (\text{S} \cdot \text{D} = \text{E})$$

**Step 4.** Multiply $e_1$ by the result (Fano line $\{5,6,1\}$):

$$e_1 \cdot (e_2 \cdot e_3) = e_1 \cdot e_5 = e_6 \quad (\text{A} \cdot \text{E} = \text{U})$$

**Result:**

$$(e_1 \cdot e_2) \cdot e_3 = -e_6, \quad e_1 \cdot (e_2 \cdot e_3) = +e_6$$

The difference: $(e_1 \cdot e_2) \cdot e_3 - e_1 \cdot (e_2 \cdot e_3) = -2e_6$. The non-associativity is manifest.

:::tip[Physical Interpretation]
In terms of UHM dimensions: the sequence of interactions $A \to S \to D$ yields **different** results depending on the grouping order. This means that the octonionic structure encodes the **contextual dependence** of coherent transitions: the result depends not only on the participating dimensions, but also on the order of their involvement.
:::

---

## 3. $G_2 = \mathrm{Aut}(\mathbb{O})$ and its Action on Coherences {#g2-действие}

### 3.1 Action of $G_2$ on the Space of Coherences

Upon identifying $e_i \leftrightarrow$ dimensions (from the `dimensions.md` table), the group $G_2$ acts on the $7D$ space:

$$g \in G_2: \quad |i\rangle \mapsto \sum_j D_{ji}(g) |j\rangle$$

where $D(g)$ is the 7-dimensional (fundamental) representation of $G_2$.

**Action on the coherence matrix:**

$$g: \Gamma \mapsto D(g)\, \Gamma\, D(g)^\dagger$$

**Action on coherences:**

$$g: \gamma_{ij} \mapsto \sum_{k,l} D_{ki}(g)\, D_{lj}^*(g)\, \gamma_{kl}$$

### 3.2 $G_2$ Preserves the Fano Structure

Since $G_2 = \mathrm{Aut}(\mathbb{O})$ preserves octonionic multiplication, it preserves the structure constants $f_{ijk}$ and hence the Fano plane:

$$g \in G_2 \quad \Rightarrow \quad g \text{ permutes the Fano lines}$$

More precisely: for each $g \in G_2$ there exists a permutation $\sigma_g$ on the set $\{1, \ldots, 7\}$ of lines:

$$g\, \Pi_p\, g^\dagger = \Pi_{\sigma_g(p)}$$

---

## 3b. Physical Interpretation of $G_2$-Symmetry {#физическая-интерпретация-g2}

### What $G_2$-Invariance Preserves

$G_2$-symmetry is the **gauge freedom** of UHM theory: $G_2$ transformations do not change the physics, but merely rename the basis of dimensions $\{A, S, D, L, E, U, O\}$, preserving the octonionic algebraic structure.

:::tip[Status: Theorem \[T\]]
The $G_2$-transformation $g: \Gamma \mapsto D(g)\,\Gamma\,D(g)^\dagger$ preserves the following physical quantities:

| Invariant | Formula | Physical meaning |
|-----------|---------|-----------------|
| Total purity | $P = \mathrm{Tr}(\Gamma^2)$ | Degree of consciousness integration |
| Reflection measure | $R = R(\Gamma)$ | Depth of self-observation |
| Integration | $\Phi = \Phi(\Gamma)$ | System irreducibility |
| Spectrum of $\Gamma$ | $\lambda_1 \geq \cdots \geq \lambda_7$ | Eigenvalue populations |
| Total coherence | $\sum_{i < j} |\gamma_{ij}|^2$ | Overall connectivity of dimensions |
| Fano structure | $f_{ijk}$ | Octonion multiplication table |
:::

### What $G_2$ Does NOT Preserve

The $G_2$-transformation **mixes** specific dimensions. In general:

- **Populations of individual dimensions** $\gamma_{ii}$ are not invariant: $G_2$ can transfer population from $A$ to $S$.
- **Specific coherences** $\gamma_{ij}$ are not invariant: the $A \leftrightarrow S$ coupling can transform into $D \leftrightarrow L$.
- **Gap profile** $\{\mathrm{Gap}(i,j)\}_{i<j}$ is not invariant elementwise (although the total Gap is invariant).
- **Stress vector** $\sigma_k = 1 - 7\gamma_{kk}$ is not invariant componentwise.

### Geometric Meaning: Rotations in $\{A, S, D, L, E, U, O\}$

A $G_2$-transformation can be viewed as a **rotation** of the 7-dimensional space that:

1. **Is compatible with the Fano plane:** if $\{i, j, k\}$ is a Fano line, then the image $\{g(i), g(j), g(k)\}$ is also a Fano line.
2. **Is not arbitrary:** of the 21 possible rotations in $\mathrm{SO}(7)$, only the 14-dimensional submanifold $G_2$ preserves octonionic multiplication.
3. **Physically:** a $G_2$-transformation is a change of 'coordinate system' in the space of dimensions, under which all algebraic relations (Fano lines, signs of structure constants, triples of related dimensions) remain unchanged.

:::warning[$G_2$-Covariance Principle]
The physical laws of UHM theory (evolution, consciousness thresholds, Lindblad operators) must be formulated in terms of $G_2$-invariants. The specific 'label' of a dimension ($A$, $S$, $D$, ...) is a matter of basis choice, not of physics.
:::

### Analogy with Gauge Theories

| Theory | Gauge group | What is preserved | What is mixed |
|--------|---------------------|-----------------|-------------------|
| Electrodynamics | $U(1)$ | Charge | Phase of the wave function |
| Chromodynamics | $SU(3)$ | Color singlet | Quark color (r, g, b) |
| **UHM** | $G_2$ | $P$, $R$, $\Phi$, spectrum, Fano structure | Dimension labels $\{A,S,D,L,E,U,O\}$ |

In this sense $G_2$ for UHM theory is the analogue of $SU(3)_c$ for QCD: specific 'colors' (dimensions) are not directly observable; only invariant combinations are observable.

---

## 4. $G_2$-Invariants of the Gap Profile

### Theorem 2.1 ($G_2$-Invariants of the Gap Profile)

:::tip[Status: Theorem \[T\]]
The following quantities are $G_2$-invariants (unchanged under $G_2$ transformations).
:::

**(a)** Total purity: $P = \mathrm{Tr}(\Gamma^2)$ — invariant under $\mathrm{SO}(7) \supset G_2$.

**(b)** Total Gap:

$$\mathcal{G}_{\mathrm{total}} := \sum_{i<j} |\gamma_{ij}|^2 \cdot \mathrm{Gap}(i,j)^2 = \sum_{i<j} |\mathrm{Im}(\gamma_{ij})|^2$$

The total 'imaginary energy' of coherences is invariant under $\mathrm{SO}(7)$.

**(c)** However, the **distribution** of Gap over pairs $(i,j)$ is **not** a $G_2$-invariant. $G_2$ 'mixes' Gap between pairs, preserving only the total.

**Proof.** (a) and (b) follow from the unitary invariance of the Frobenius norm. (c) follows from the fact that $G_2$ is not diagonal in the basis $\{|i\rangle\}$. $\blacksquare$

### Theorem 2.2 ($G_2$-Orbits of Gap Profiles)

:::tip[Status: Theorem \[T\]]
The set of all possible Gap profiles $\{\mathrm{Gap}(i,j)\}_{i<j}$ for a fixed $\Gamma$ decomposes into $G_2$-orbits.
:::

**(a)** The total number of $G_2$-invariants for a Hermitian $7 \times 7$ matrix: $48 - 14 = 34$, where $14 = \dim(G_2)$. Consequently, $G_2$ gauge freedom reduces the 48-dimensional parameter space to a **34-dimensional** space of physically distinguishable configurations. The [$G_2$-rigidity theorem](/docs/proofs/categorical/uniqueness-theorem#физические-состояния) [T] proves that $G_2$ is the **maximal** gauge group (Lemma G4): no larger subgroup of $U(7)$ preserves all axiomatic structures A1–A5. The reduction $48 \to 34$ is not an arbitrary gauge choice, but a **necessary** consequence of the uniqueness of the holonomy representation.

**(b)** Of the 21 Gap values, only $34 - 7 = $ **up to 27** are 'physically distinguishable' (7 populations are subtracted from the invariants).

**(c)** This means that $21 - (27 - 21) = $ **all 21 Gaps** can be distinguishable, but with 14 relations between them. In practice, knowing 7 Gaps, one can (under $G_2$-covariance) recover the remaining 14.

### Corollary: $G_2$-Reduction of Diagnostics

If the UHM evolution equations are $G_2$-covariant, a full diagnostic requires measuring only:

- 7 populations $\gamma_{ii}$
- 7 moduli $|\gamma_{ij}|$ for one 'base set' of pairs
- 7 phases $\theta_{ij}$ for the same set

The remaining 27 parameters are computed from $G_2$ relations.

:::warning[Status: Open Problem \[H\]]
$G_2$-covariance of the evolution equations has not been proved in full generality. The degree of $G_2$ breaking is determined by the parameter $\alpha$ (see Theorem 11.3 below).
:::

---

## 5. Fano-Structured Lindblad Operators

### 5.1 Two Types of Classifier Atoms

From L-unification: Lindblad operators $L_k = \sqrt{\chi_{S_k}}$ are derived from **atoms** of the classifier $\Omega$. There are two types:

**Basis atoms** (7 in total):

$$S_k = |k\rangle\langle k|, \quad k \in \{A, S, D, L, E, U, O\}$$

**Composite atoms** (7 in total): the Fano lines define 7 **linear subobjects** — projections onto 3-dimensional subspaces:

$$\Pi_p = \sum_{i \in \mathrm{line}_p} |i\rangle\langle i|, \quad p = 1, \ldots, 7$$

Each Fano line $p = (i, j, k)$ generates a **composite atom** $S_p = \mathrm{span}\{|i\rangle, |j\rangle, |k\rangle\}$.

### Theorem 10.0 (Completeness of Fano Atoms)

:::tip[Status: Theorem \[T\]]
Each dimension lies on exactly 3 Fano lines.
:::

$$\sum_{p=1}^{7} \Pi_p = 3I$$

**Proof.** A property of the Fano plane: each of the 7 points is incident to exactly 3 lines. $\blacksquare$

### 5.2 Definition (Fano-Structured Lindblad Operators)

For each Fano line $p = (i, j, k)$, a Lindblad operator is defined:

$$L_p^{\mathrm{Fano}} := \frac{1}{\sqrt{3}} \Pi_p = \frac{1}{\sqrt{3}}(|i\rangle\langle i| + |j\rangle\langle j| + |k\rangle\langle k|)$$

**CPTP verification:**

$$\sum_{p=1}^{7} (L_p^{\mathrm{Fano}})^\dagger L_p^{\mathrm{Fano}} = \frac{1}{3}\sum_{p=1}^{7} \Pi_p = \frac{1}{3} \cdot 3I = I \quad \checkmark$$

### 5.3 Definition (Fano Predictive Channel)

$$\mathcal{P}_{\mathrm{Fano}}(\Gamma) := \sum_{p=1}^{7} L_p^{\mathrm{Fano}} \, \Gamma \, (L_p^{\mathrm{Fano}})^\dagger = \frac{1}{3}\sum_{p=1}^{7} \Pi_p \, \Gamma \, \Pi_p$$

---

## 6. Properties of the Fano Channel

### Theorem 10.1 (Fano Channel Preserves Coherences)

:::tip[Status: Theorem \[T\]]
For an arbitrary coherence matrix $\Gamma$:
:::

**(a)** Diagonal elements are preserved exactly:

$$[\mathcal{P}_{\mathrm{Fano}}(\Gamma)]_{ii} = \gamma_{ii}$$

**(b)** Off-diagonal elements (coherences) are preserved with a factor of $1/3$:

$$[\mathcal{P}_{\mathrm{Fano}}(\Gamma)]_{ij} = \frac{1}{3}\gamma_{ij} \quad \text{for all } i \neq j$$

**(c)** Phases of coherences are preserved exactly:

$$\arg([\mathcal{P}_{\mathrm{Fano}}(\Gamma)]_{ij}) = \arg(\gamma_{ij}) = \theta_{ij}$$

**Proof.**

**(a)** $[\sum_p \Pi_p \Gamma \Pi_p]_{ii} = \sum_{p:\, i \in \mathrm{line}_p} \gamma_{ii} = 3\gamma_{ii}$. With factor $1/3$: $\gamma_{ii}$. $\checkmark$

**(b)** In $\mathrm{PG}(2,2)$ any two points lie on exactly one line. For the pair $(i,j)$, $i \neq j$: exactly one line $p^*$ contains both points.

$$\left[\sum_p \Pi_p \Gamma \Pi_p\right]_{ij} = \sum_{p:\, i,j \in \mathrm{line}_p} \gamma_{ij} = 1 \cdot \gamma_{ij}$$

With factor $1/3$: $\gamma_{ij}/3$. $\checkmark$

**(c)** $\arg(\gamma_{ij}/3) = \arg(\gamma_{ij})$, since $1/3 > 0$. $\checkmark$ $\blacksquare$

### Theorem 10.2 (Canonical Form of $\varphi_{\mathrm{coh}}$)

:::tip[Status: Theorem \[T\]]
Canonical coherence-preserving self-modelling is determined by a two-component structure.
:::

$$\varphi_{\mathrm{coh}}(\Gamma) = k \cdot \left[\alpha \cdot \mathcal{P}_{\mathrm{base}}(\Gamma) + (1 - \alpha) \cdot \mathcal{P}_{\mathrm{Fano}}(\Gamma)\right] + (1 - k) \cdot \Gamma_{\mathrm{anchor}}$$

where:
- $\mathcal{P}_{\mathrm{base}}(\Gamma) = \sum_m P_m \Gamma P_m = \mathrm{diag}(\Gamma)$ — atomic channel (decohering observation)
- $\mathcal{P}_{\mathrm{Fano}}(\Gamma) = \frac{1}{3}\sum_p \Pi_p \Gamma \Pi_p$ — Fano channel
- $\alpha \in [0, 1]$ — **decoherence depth parameter** (balance between atomic and Fano observation)
- $k < 1$ — contraction parameter
- $\Gamma_{\mathrm{anchor}}$ — E-accented anchor

**CPTP verification:** For arbitrary $\alpha \in [0,1]$:

$$\varphi_{\mathrm{coh}} = k \cdot \mathcal{P}_\alpha + (1-k) \cdot \mathrm{const}$$

where $\mathcal{P}_\alpha = \alpha \mathcal{P}_{\mathrm{base}} + (1-\alpha) \mathcal{P}_{\mathrm{Fano}}$ is a convex combination of CPTP channels, hence CPTP. $\checkmark$

### Theorem 10.3 (Target Coherences of $\varphi_{\mathrm{coh}}$)

:::tip[Status: Theorem \[T\]]
For canonical $\varphi_{\mathrm{coh}}$ the target coherences are determined as follows.
:::

**(a)** Modulus of the target coherence:

$$|\gamma_{ij}^{\mathrm{target}}| = \left[\frac{k(1-\alpha)}{3}\right] \cdot |\gamma_{ij}| + (1-k) \cdot [\Gamma_{\mathrm{anchor}}]_{ij}$$

For a diagonal anchor ($[\Gamma_{\mathrm{anchor}}]_{ij} = 0$ for $i \neq j$):

$$|\gamma_{ij}^{\mathrm{target}}| = \frac{k(1-\alpha)}{3} \cdot |\gamma_{ij}|$$

**(b)** Target phase:

$$\theta_{ij}^{\mathrm{target}} = \theta_{ij} \quad \text{(phase is preserved!)}$$

**(c)** Target Gap:

$$\mathrm{Gap}^{\mathrm{target}}(i,j) = |\sin(\theta_{ij})| = \mathrm{Gap}(i,j) \quad \text{(Gap is preserved!)}$$

**Fundamental corollary.** Canonical $\varphi_{\mathrm{coh}}$ **does not tend to change the Gap** — it tends to reproduce the Gap with reduced amplitude. The target state does **not destroy** coherences, but scales them.

### Theorem 10.4 (Variational Determination of $\alpha^*$)

:::tip[Status: Theorem \[T\]]
The optimal parameter $\alpha^*$ is determined by a variational principle.
:::

$$\alpha^* = \arg\min_{\alpha \in [0,1]} \mathcal{F}[\mathcal{P}_\alpha; \Gamma] = \arg\min_{\alpha} \left[S_{\mathrm{spec}}(\mathcal{P}_\alpha(\Gamma)) + D_{KL}(\mathcal{P}_\alpha(\Gamma) \| \Gamma)\right]$$

**(a)** At $\alpha = 1$ (purely atomic): $\mathcal{P}_1 = \mathcal{P}_{\mathrm{base}}$, destroys all coherences. $D_{KL}$ is large (information about coherences is lost). $S_{\mathrm{spec}}$ is maximal (complete decoherence).

**(b)** At $\alpha = 0$ (purely Fano): $\mathcal{P}_0 = \mathcal{P}_{\mathrm{Fano}}$, preserves coherences with factor $1/3$. $D_{KL}$ is small (little information is lost). But $S_{\mathrm{spec}}$ is not minimal (the predictive model is less precise).

**(c)** The optimum $\alpha^* \in (0, 1)$ is a balance between predictive accuracy (atomic observation) and structure preservation (Fano observation).

**(d)** For a system with purity $P > P_{\mathrm{crit}}$:

$$\alpha^* \approx 1 - \frac{P_{\mathrm{crit}}}{P} = 1 - \frac{2}{7P}$$

At $P = 1$ (pure state): $\alpha^* \approx 5/7 \approx 0.71$ — significant Fano contribution.

At $P \to P_{\mathrm{crit}}$: $\alpha^* \to 0$ — almost entirely Fano (minimal destruction of coherences for survival).

**Proof.** Minimisation of $\mathcal{F}$ over $\alpha$ at fixed $P$ determines the balance: increasing $\alpha$ improves predictive accuracy ($S_{\mathrm{spec}}$ decreases), but increases coherence loss ($D_{KL}$ grows). The condition $P > P_{\mathrm{crit}}$ requires preserving a sufficient number of coherences, which bounds $\alpha$ from above. The optimum is found from $\partial \mathcal{F}/\partial \alpha = 0$. $\blacksquare$

### Theorem 10.5 (Explicit Coefficients of $\varphi_{\mathrm{coh}}$)

:::tip[Status: Theorem \[T\]]
The Kraus operators of canonical $\varphi_{\mathrm{coh}}$ take a specific form.
:::

**Atomic operators (7 in total):**

$$K_m^{(\mathrm{atom})} = \sqrt{\alpha^* k / 7} \cdot |m\rangle\langle m|, \quad m = 1, \ldots, 7$$

**Fano operators (7 in total):**

$$K_p^{(\mathrm{Fano})} = \sqrt{(1-\alpha^*) k / 3} \cdot \Pi_p, \quad p = 1, \ldots, 7$$

**Anchor operator:**

$$K_0^{(\mathrm{anch})} = \sqrt{1-k} \cdot \Gamma_{\mathrm{anchor}}^{1/2}$$

**CPTP verification:**

$$\sum_{m=1}^{7} (K_m^{(\mathrm{atom})})^\dagger K_m^{(\mathrm{atom})} + \sum_{p=1}^{7} (K_p^{(\mathrm{Fano})})^\dagger K_p^{(\mathrm{Fano})} + (K_0^{(\mathrm{anch})})^\dagger K_0^{(\mathrm{anch})}$$

First term: $\alpha^* k / 7 \cdot 7I = \alpha^* k \cdot I$.

Second term: $(1-\alpha^*) k / 3 \cdot 3I = (1-\alpha^*) k \cdot I$.

Third term: $(1-k) \cdot I$.

**Total = $I$. $\checkmark$**

**Corollary.** The coefficients $c_{mn}$ are determined by:

$$c_{mn} = \begin{cases} \alpha^* k & \text{for } m = n \text{ (atomic part)} \\ (1-\alpha^*) k / 3 & \text{for } m \neq n, (m,n) \text{ on a common Fano line} \\ 0 & \text{for } m \neq n, (m,n) \text{ not on a common Fano line} \end{cases}$$

The coefficients are fully determined by:
- The Fano structure $\mathrm{PG}(2,2)$ (algebraic geometry)
- The variational principle ($\alpha^*$ via $P$ and $P_{\mathrm{crit}}$)
- The contraction parameter $k$

---

## 7. $G_2$-Covariance

### Theorem 11.1 (Atomic Dissipator is NOT $G_2$-Covariant)

:::danger[Status: Theorem — negative result \[T\]]
The dissipative channel with atomic Lindblad operators $L_k = |k\rangle\langle k|$ is **not** $G_2$-covariant.
:::

$$\exists g \in G_2: \quad \mathcal{D}_{\mathrm{atom}}[g\Gamma g^\dagger] \neq g \, \mathcal{D}_{\mathrm{atom}}[\Gamma] \, g^\dagger$$

**Proof.**

**(a)** Atomic dissipator:

$$\mathcal{D}_{\mathrm{atom}}[\Gamma] = \sum_{k=1}^{7} L_k \Gamma L_k^\dagger - \Gamma = \sum_k |k\rangle\langle k| \Gamma |k\rangle\langle k| - \Gamma = \mathrm{diag}(\Gamma) - \Gamma$$

**(b)** Action of $G_2$: for $g \in G_2$, $g\Gamma g^\dagger \mapsto D(g)\Gamma D(g)^\dagger$, where $D(g)$ is the 7-dimensional representation of $G_2$.

**(c)** We check covariance:

$$\mathcal{D}_{\mathrm{atom}}[g\Gamma g^\dagger] = \mathrm{diag}(g\Gamma g^\dagger) - g\Gamma g^\dagger$$

$$g \, \mathcal{D}_{\mathrm{atom}}[\Gamma] \, g^\dagger = g[\mathrm{diag}(\Gamma) - \Gamma]g^\dagger = g \cdot \mathrm{diag}(\Gamma) \cdot g^\dagger - g\Gamma g^\dagger$$

**(d)** Equality requires:

$$\mathrm{diag}(g\Gamma g^\dagger) = g \cdot \mathrm{diag}(\Gamma) \cdot g^\dagger \quad \forall \Gamma$$

This means: 'diagonal of the transformed matrix = transform of the diagonal'. This holds **only** for diagonal $g$ (permutations + phases), but NOT for general $g \in G_2$.

**(e)** Counterexample: take $g$ = rotation by angle $\pi/4$ in the plane $(e_1, e_2)$. For a matrix $\Gamma$ with $\gamma_{12} \neq 0$:

$$\mathrm{diag}(g\Gamma g^\dagger) \neq g \cdot \mathrm{diag}(\Gamma) \cdot g^\dagger$$

since the left-hand side annihilates the coherence $\gamma_{12}$ in the rotated basis, while the right-hand side does not. $\blacksquare$

### Theorem 11.2 (Fano Dissipator is $G_2$-Covariant)

:::tip[Status: Theorem \[T\]]
The dissipative channel with Fano-structured Lindblad operators $L_p^{\mathrm{Fano}} = \frac{1}{\sqrt{3}}\Pi_p$ **is** $G_2$-covariant.
:::

$$\forall g \in G_2: \quad \mathcal{D}_{\mathrm{Fano}}[g\Gamma g^\dagger] = g \, \mathcal{D}_{\mathrm{Fano}}[\Gamma] \, g^\dagger$$

**Proof.**

**(a)** The group $G_2 = \mathrm{Aut}(\mathbb{O})$ **preserves** octonionic multiplication. The Fano plane $\mathrm{PG}(2,2)$ is defined by the structure constants of $\mathbb{O}$. Therefore $G_2$ **preserves** the Fano structure:

$$g \in G_2 \quad \Rightarrow \quad g \text{ permutes the Fano lines}$$

More precisely: for each $g \in G_2$ there exists a permutation $\sigma_g$ on the set $\{1, \ldots, 7\}$ of lines:

$$g\, \Pi_p\, g^\dagger = \Pi_{\sigma_g(p)}$$

**(b)** Fano dissipator:

$$\mathcal{D}_{\mathrm{Fano}}[\Gamma] = \frac{1}{3}\sum_{p=1}^{7} \Pi_p \Gamma \Pi_p - \Gamma$$

**(c)** Substituting $g\Gamma g^\dagger$:

$$\mathcal{D}_{\mathrm{Fano}}[g\Gamma g^\dagger] = \frac{1}{3}\sum_p \Pi_p (g\Gamma g^\dagger) \Pi_p - g\Gamma g^\dagger$$

**(d)** Using $g^\dagger \Pi_p g = \Pi_{\sigma_g^{-1}(p)}$ (from (a)):

$$= \frac{1}{3}\sum_p \Pi_p g \Gamma g^\dagger \Pi_p = \frac{1}{3}\sum_p g (g^\dagger \Pi_p g) \Gamma (g^\dagger \Pi_p g) g^\dagger$$

$$= \frac{1}{3}g\left[\sum_p \Pi_{\sigma_g^{-1}(p)} \Gamma \Pi_{\sigma_g^{-1}(p)}\right]g^\dagger$$

Since $\sigma_g$ is a permutation: $\sum_p \Pi_{\sigma_g^{-1}(p)} = \sum_q \Pi_q$ (reindexing). Therefore:

$$= g \left[\frac{1}{3}\sum_q \Pi_q \Gamma \Pi_q\right] g^\dagger = g \, \mathcal{P}_{\mathrm{Fano}}(\Gamma) \, g^\dagger$$

And:

$$\mathcal{D}_{\mathrm{Fano}}[g\Gamma g^\dagger] = g \, \mathcal{P}_{\mathrm{Fano}}(\Gamma) \, g^\dagger - g\Gamma g^\dagger = g[\mathcal{P}_{\mathrm{Fano}}(\Gamma) - \Gamma]g^\dagger = g \, \mathcal{D}_{\mathrm{Fano}}[\Gamma] \, g^\dagger$$

$\blacksquare$

### Theorem 11.3 (Degree of $G_2$ Breaking is Determined by $\alpha$)

:::tip[Status: Theorem \[T\]]
For canonical $\varphi_{\mathrm{coh}}$ with parameter $\alpha$, the degree of $G_2$-covariance is determined as follows.
:::

**(a)** At $\alpha = 0$ (purely Fano): **full** $G_2$-covariance. The gauge reduction $48 \to 34$ is valid.

**(b)** At $\alpha = 1$ (purely atomic): $G_2$ is **fully broken**. No gauge reduction.

**(c)** For intermediate $\alpha \in (0, 1)$: **partial** $G_2$-covariance. Mixed channel:

$$\mathcal{P}_\alpha = \alpha \, \mathcal{P}_{\mathrm{base}} + (1 - \alpha) \, \mathcal{P}_{\mathrm{Fano}}$$

Measure of $G_2$-symmetry breaking:

$$\Delta_{G_2}(\alpha) := \sup_{g \in G_2} \|\mathcal{P}_\alpha \circ \mathrm{Ad}_g - \mathrm{Ad}_g \circ \mathcal{P}_\alpha\|_{\mathrm{op}}$$

where $\mathrm{Ad}_g(\Gamma) = g\Gamma g^\dagger$.

**(d)** $\Delta_{G_2}(\alpha)$ increases monotonically with $\alpha$:

$$\Delta_{G_2}(0) = 0, \quad \Delta_{G_2}(1) = \Delta_{\max} > 0$$

**(e)** At optimal $\alpha^* \approx 1 - 2/(7P)$:

$$\Delta_{G_2}(\alpha^*) = \alpha^* \cdot \Delta_{\max}$$

**Proof.** (a)–(b): direct consequence of Theorems 11.1 and 11.2. (c)–(e): $\mathcal{P}_\alpha$ is a convex combination of the $G_2$-covariant ($\mathcal{P}_{\mathrm{Fano}}$) and $G_2$-breaking ($\mathcal{P}_{\mathrm{base}}$) channels. The measure of breaking is linear in $\alpha$ (from the linearity of both channels). $\blacksquare$

:::warning Limits of $G_2$-Covariance
- Fano dissipator $\mathcal{D}_{\text{Fano}}$: $G_2$-covariant **[T]** (T-11.2)
- Atomic dissipator $\mathcal{D}_{\text{atom}}$: **NOT** $G_2$-covariant **[T]** (T-11.1)
- Full dynamics $\mathcal{L}_\Omega = \mathcal{D}_{\text{atom}} + \mathcal{D}_{\text{Fano}} + \mathcal{R}$: $G_2$-covariance of the full evolution — **[C]** (depends on the fraction of atomic vs Fano component)
:::

### Theorem 11.4 (Modified Gauge Reduction)

:::tip[Status: Theorem \[T\]]
Under partial $G_2$-covariance ($\alpha \in (0,1)$), the parameter space of Gap profiles is reduced.
:::

**(a)** Full $G_2$ ($\alpha = 0$): $48 - 14 = $ **34** independent parameters.

**(b)** Partial $G_2$ (optimal $\alpha^*$): **$34 + 14\alpha^*$** parameters. The number of 'additional' parameters $= 14\alpha^* \approx 14(1 - 2/(7P))$.

**(c)** No $G_2$ ($\alpha = 1$): **48** parameters (full space).

**For a typical living system** with $P \approx 0.5$: $\alpha^* \approx 0.43$, number of parameters $\approx 34 + 6 = $ **40**. Reduction from 48 to 40 — moderate but significant.

**For a highly coherent system** with $P \approx 0.8$: $\alpha^* \approx 0.64$, number of parameters $\approx 34 + 9 = $ **43**. The reduction is even more moderate.

**Interpretation.** Self-observation (nonzero $\alpha$) **partially breaks** the algebraic symmetry of the octonions. The deeper the self-knowledge (larger $\alpha$), the more broken the $G_2$-symmetry, and the more parameters are needed to describe the system. This is the fundamental 'price of self-knowledge': knowledge about oneself increases the complexity of self-description.

### Updated Diagnostic Protocol

Taking into account partial $G_2$-covariance:

| Mode | Number of parameters | Protocol |
|-------|-----------------|----------|
| $\alpha = 0$ (no self-knowledge, L0) | 34 (full $G_2$) | Minimal tomography: 7 populations + 7 moduli + 7 phases + $G_2$ relations |
| $\alpha^* \approx 0.4$ (typical L2 system) | $\sim$40 | Extended tomography: 7 + 12 moduli + 12 phases + partial $G_2$ relations |
| $\alpha = 1$ (full L4) | 48 (no $G_2$) | Full tomography: all 48 parameters |

---

## 8. Unified Theorem of Self-Observation and Gap

### Theorem 12.1 (Fano-Coherent Self-Modelling)

:::tip[Status: Theorem \[T\]]
Canonical coherence-preserving self-modelling for UHM theory is determined uniquely (up to the contraction parameter $k$).
:::

**(a)** **Algebraic structure:** The Fano plane $\mathrm{PG}(2,2)$ determines the composite atoms of the classifier $\Omega$, generating the Fano–Lindblad operators $L_p^{\mathrm{Fano}}$.

**(b)** **Variational principle:** The balance of atomic and Fano observation $\alpha^*$ minimises the functional $\mathcal{F} = S_{\mathrm{spec}} + D_{KL}$.

**(c)** **Phase properties:** Canonical $\varphi_{\mathrm{coh}}$ **preserves** the phases of coherences. The target Gap coincides with the current Gap (amplitude scaling without phase distortion).

**(d)** **Symmetry:** $G_2$-covariance is partially broken by the atomic component. The degree of breaking $\Delta_{G_2} = \alpha^* \cdot \Delta_{\max}$ depends on the purity $P$.

**(e)** **Stationary Gap:** Substituting into the stationary equation with $\theta_{ij}^{\mathrm{target}} = \theta_{ij}$ gives:

$$\mathrm{Gap}^{(\infty)}(i,j) = \left|\sin\left(\theta_{ij} - \arctan\left(\frac{\Delta\omega_{ij}}{\Gamma_2 + \kappa}\right)\right)\right|$$

The stationary Gap is **shifted** relative to the current one by the angle $\arctan(\Delta\omega/(\Gamma_2 + \kappa))$ — even with phase-preserving $\varphi_{\mathrm{coh}}$, unitary rotation creates a difference between the target and the stationary.


---

**Related documents:**
- [Standard Model from G₂](/docs/physics/gauge-symmetry/standard-model)
- [Fano Selection Rules](/docs/physics/gauge-symmetry/fano-selection-rules)
- [G₂-Noether Charges](/docs/physics/gauge-symmetry/noether-charges)
- [Confinement](/docs/physics/gauge-symmetry/confinement)
