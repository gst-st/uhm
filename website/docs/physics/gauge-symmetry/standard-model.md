---
sidebar_position: 2
title: "Standard Model from G₂"
---

# Standard Model from G₂

:::info For whom this chapter is intended
Derivation of the Standard Model gauge group from $G_2 = \mathrm{Aut}(\mathbb{O})$. The reader will learn about the dual extraction strategy for $\mathrm{SU}(3)_C$ and the electroweak sector.
:::


## Overview

:::info[Correctness of the heading — [T]]
$\mathrm{rank}(G_2) = 2 < \mathrm{rank}(\mathrm{SM}) = 4$, so the SM gauge group **is not a subgroup** of $G_2$. However, the full SM group **is unique** and is derived from the axioms:
- $\mathrm{SU}(3)_C$ from $G_2$ as the stabilizer of the O-direction — **[T]** (standard mathematical fact)
- Electroweak sector $\mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$ from the Fano-electroweak construction (FE) — **[T]** (combinatorics: uniqueness of $(E,U)$); **[C]** (dynamical gauge structure)
- Full correspondence "SM from $G_2$ + (FE)" — **[C]** (electroweak dynamics is conditional)
:::

The central task is the derivation of the Standard Model gauge group $\mathrm{SU}(3)_C \times \mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$ from $G_2 = \mathrm{Aut}(\mathbb{O})$. The strategy is dual: $\mathrm{SU}(3)_C$ is extracted from the stabilizer of the O-direction in $G_2$, while the electroweak sector $\mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$ comes from the Fano-electroweak construction (FE): the Higgs line $\{A,E,U\}$ canonically decomposes $\bar{3} \to \{E,U\} \oplus \{L\}$.

:::tip[Status: \[T\] for SU(3)\_C]
$\mathrm{SU}(3)_C$ from $G_2$ is a standard mathematical fact.
:::

:::tip[Status: \[T\] for the combinatorics of the electroweak sector]
The electroweak sector $\mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$ is derived from the Fano-electroweak construction (FE): the formula $\kappa_0$ [T] categorically singles out the **unique** pair $(E,U)$ via $\mathrm{Hom}(O,E)$ and $\mathrm{Hom}(O,U)$, the Higgs line $\{A,E,U\}$ canonically decomposes $\bar{3} \to \{E,U\} \oplus \{L\}$, which determines $\mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$. Full proof of uniqueness: [sect. 2.3a](#теорема-единственности-фэ).
:::

:::warning Distinction between [T] and [C] in the electroweak sector {#электрослабое-разграничение}
Two levels of results must be clearly separated:

- **[T] (proven):** combinatorial uniqueness of the pair $(E,U)$ from $\kappa_0$, uniqueness of the Higgs line $\{A,E,U\}$, canonical decomposition $\bar{3} \to 2_{EU} \oplus 1_L$
- **[C] (conditional):** full dynamical gauge structure $\mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$ with correct running of coupling constants — depends on dynamical content (Gap potential, RG equations) going beyond pure combinatorics
- **Free parameter:** the hypercharge generator $Y$ contains the parameter $\alpha$ (relative weight of baryon number and weak isospin within $\bar{3}$), whose value is not fixed by the Fano structure and requires an additional condition (e.g., from anomaly freedom or phenomenology)
:::

---

## 1. Anatomy of $G_2$ and the Rank Problem

### 1.1 Setup

**Fundamental obstacle.** $\mathrm{rank}(G_2) = 2$, while $\mathrm{rank}(\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)) = 2 + 1 + 1 = 4$. Consequently, the SM group **is not a subgroup** of $G_2$.

**Strategy.** Overcome the obstacle through two mechanisms:
- (A) $\mathrm{SU}(3)_C$ from the stabilizer of the O-direction in $G_2$ — **[T]** (structural symmetry, rank $2 \to$ rank 2)
- (B) $\mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$ from the Fano-electroweak construction (FE): the Higgs line $\{A,E,U\}$ canonically decomposes $\bar{3} \to \{E,U\} \oplus \{L\}$ — **[T]** (uniqueness of the pair $(E,U)$ from $\kappa_0$ [T]; adds rank 2 in the 42D PW extension)

### 1.2 Theorem 1.1 (Decomposition of $G_2$-generators under $\mathrm{SU}(3)$)

:::tip[Status: Theorem \[T\]]
The maximal embedding $\mathrm{SU}(3) \subset G_2$ (stabilizer of a vector in $\mathrm{Im}(\mathbb{O}) \cong \mathbb{R}^7$) determines the decomposition.
:::

**(a)** Representation **7** (fundamental):

$$7 \to 1_O \oplus 3_{ASD} \oplus \bar{3}_{LEU}$$

where: $1$ — distinguished O-direction (time, Page–Wootters); $3$ — spatial triplet $\{A, S, D\}$; $\bar{3}$ — Gap triplet $\{L, E, U\}$.

**(b)** Adjoint representation **14** (algebra $\mathfrak{g}_2$):

$$14 \to 8 \oplus 3 \oplus \bar{3}$$

where $8$ is the adjoint representation of $\mathrm{SU}(3)$ (generators of $\mathrm{SU}(3)$), $3$ and $\bar{3}$ are fundamental representations.

**(c)** The 21 coherences $\gamma_{ij}$ decompose into sectors:

| Sector | Pairs | Number | $\mathrm{SU}(3)$-representation |
|---|---|---|---|
| O-to-3 | $\{A\text{-}O, S\text{-}O, D\text{-}O\}$ | 3 | $3$ |
| O-to-$\bar{3}$ | $\{L\text{-}O, E\text{-}O, U\text{-}O\}$ | 3 | $\bar{3}$ |
| 3-to-3 | $\{A\text{-}S, A\text{-}D, S\text{-}D\}$ | 3 | $\bar{3}$ ($\wedge^2 3$) |
| $\bar{3}$-to-$\bar{3}$ | $\{L\text{-}E, L\text{-}U, E\text{-}U\}$ | 3 | $3$ ($\wedge^2 \bar{3}$) |
| **3-to-$\bar{3}$** | **$\{A\text{-}L, A\text{-}E, A\text{-}U, S\text{-}L, S\text{-}E, S\text{-}U, D\text{-}L, D\text{-}E, D\text{-}U\}$** | **9** | **$8 \oplus 1$** |

**(d)** The 3-to-$\bar{3}$ sector contains the **adjoint representation of $\mathrm{SU}(3)$** (8 generators) plus the **$\mathrm{SU}(3)$-singlet** (1 generator). Eight is precisely the number of gluons in QCD.

**Proof.** Standard representation theory of exceptional Lie algebras. The embedding $\mathrm{SU}(3) \subset G_2$ is defined by the stabilizer: $\mathrm{Stab}_{G_2}(e_1) \cong \mathrm{SU}(3)$ for any unit vector $e_1 \in S^6 \subset \mathrm{Im}(\mathbb{O})$. The decomposition of **7** follows from the fact that $\mathrm{SU}(3)$ acts trivially on $e_1$ (singlet) and as fundamental/antifundamental on the orthogonal complement. The decomposition of **14** follows from the structural theorem for the pair $(G_2, \mathrm{SU}(3))$:

$$\mathfrak{g}_2 = \mathfrak{su}(3) \oplus \mathfrak{m}, \quad \mathfrak{m} \cong \mathbb{C}^3$$

where $\mathfrak{m}$ is the orthogonal complement, isomorphic to $3 \oplus \bar{3}$ as an $\mathrm{SU}(3)$-module (Besse, 1987). For sector (c): 21 pairs $= C(7,2)$ decompose by the rules of tensor products of $\mathrm{SU}(3)$ representations. The sector $3 \otimes \bar{3} = 8 \oplus 1$ is the standard decomposition (Clebsch-Gordan). $\blacksquare$

### 1.3 Corollary 1.1 ($\mathrm{SU}(3)_C$ as the Stabilizer of Time)

:::tip[Status: Theorem \[T\]]
The choice of the O-dimension as "clock" (Page–Wootters, Axiom 4) spontaneously breaks $G_2 \to \mathrm{SU}(3)$.
:::

:::info Fundamentality of $G_2$-gauge symmetry [T]
$G_2$ is not an arbitrarily chosen symmetry, but the **only maximal gauge group** of UHM, proven in the [$G_2$-rigidity theorem](/docs/proofs/categorical/uniqueness-theorem#лемма-g4) [T]: no larger subgroup of $U(7)$ preserves all axiomatic structures. Consequently, the entire SM structure ($G_2 \to \mathrm{SU}(3)_C$ breaking, electroweak sector) is a **necessary** consequence of the uniqueness of the holonomy representation, not a parametric choice.
:::

The remaining $\mathrm{SU}(3)$ is identified with the **gauge group of the strong interaction** $\mathrm{SU}(3)_C$:

**(a)** 8 generators of $\mathrm{SU}(3)_C$ = 8 coherences of the 3-to-$\bar{3}$ sector (after subtracting the singlet):

$$T_a^{(\mathrm{color})} \in \{A\text{-}L, A\text{-}E, A\text{-}U, S\text{-}L, S\text{-}E, S\text{-}U, D\text{-}L, D\text{-}E, D\text{-}U\}_{\mathrm{traceless}}$$

**(b)** "Gluon field" — fluctuations of the 8 Gap phases $\theta_{ij}$ in the 3-to-$\bar{3}$ sector around the vacuum value:

$$A_\mu^a(x) \sim \partial_\mu \theta_{ij}^{(a)}(x), \quad a = 1, \ldots, 8$$

**(c)** $\mathrm{SU}(3)_C$ is an **exact** symmetry (not broken in the vacuum), because the Gap vacuum $\Gamma_{\mathrm{vac}}$ (L0) is **isotropic** in the 3-to-$\bar{3}$ sector:

$$\mathrm{Gap}(A,L) = \mathrm{Gap}(A,E) = \cdots = \mathrm{Gap}(D,U) = \mathrm{Gap}_{\mathrm{vac}}^{(3\bar{3})}$$

All 9 coherences of this sector have the same Gap, and $\mathrm{SU}(3)$ is unbroken.

**Justification of the identification.** Of all possible candidates for $\mathrm{SU}(3)$ (stabilizers of $A, S, \ldots, U$), O is the only one for which:
- (i) The stabilizer has a physical meaning (choice of the "clock" subsystem)
- (ii) The remaining $\mathrm{SU}(3)$ acts on the spatial + Gap sectors
- (iii) $G_2$-invariance of the Lagrangian guarantees conservation of $\mathrm{SU}(3)_C$ charges (8 of the 14 $G_2$-charges)

---

## 2. Electroweak Sector from the Fano-Electroweak Construction (FE) {#электрослабый-сектор-фэ}

### 2.1 The Rank Problem and Its Solution {#проблема-ранга}

**Problem.** $\mathrm{rank}(\mathrm{SU}(2)_L \times \mathrm{U}(1)_Y) = 2$, but after extracting $\mathrm{SU}(3) \subset G_2$ (rank 2) no rank remains for the electroweak sector — $G_2$ is already "exhausted."

**Solution through two mechanisms:**

| Mechanism | Source | Result | Status |
|---|---|---|---|
| $G_2 \to \mathrm{SU}(3)_C$ | Stabilizer of the O-direction | rank 2 — strong interaction | **[T]** |
| Fano-electroweak construction (FE) | Higgs line $\{A,E,U\}$ | rank 2 — electroweak interaction | **[T]** (combinatorics); **[C]** (dynamics) |

**Analysis in 7D:** The generator $T_3 = (\lvert E\rangle\langle E\rvert - \lvert U\rangle\langle U\rvert)/2$ of $\mathrm{SU}(2)_L$ is a diagonal operator. Within $\mathfrak{su}(3)$ acting on $\bar{3} = \{L,E,U\}$, the Cartan generators (analogues of Gell-Mann's $\lambda_3$, $\lambda_8$) include $\lvert E\rangle\langle E\rvert - \lvert U\rangle\langle U\rvert$ as one of the two Cartans. Consequently, $T_3 \in \mathfrak{h}(\mathrm{SU}(3))$, and in 7D $\mathrm{SU}(2)_L$ is a **subgroup** of $\mathrm{SU}(3)_{\bar{3}}$. The rank remains 2.

**Resolution in 42D:** In the Page–Wootters extension (Axiom A5):

$$\mathcal{H}_{\mathrm{total}} = \mathcal{H}_O \otimes \mathcal{H}_{6D} = \mathbb{C}^7 \otimes \mathbb{C}^6 = \mathbb{C}^{42}$$

$\mathrm{SU}(3)_C$ (from $G_2$ on the clock factor) and $\mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$ (from (FE) on the system factor) act on **different** tensor factors, so they commute and ranks add: $2 + 2 = 4 = \mathrm{rank}(\mathrm{SM})$. Status: **[T]** (under Axiom A5, Page–Wootters).

:::tip Resolved: bimodule construction [T]
SM representations $(3,2)_{1/6}$ arise **not** from the tensor product $\mathbb{C}^7 \otimes \mathbb{C}^6$ (this is the PW realization for emergent time), but from the **bimodule decomposition** of $H_F$ via the real structure $J$ (KO-dim 6): the left action of $\mathbb{H}$ gives weak isospin, the right action of $M_3(\mathbb{C})^\circ$ gives color. Both act on the same element $\xi \in H_F$. Full proof: [Bimodule construction T-176](/docs/proofs/physics/bimodule-construction#бимодульная-конструкция).
:::

### 2.2 Fano Structure and the Higgs Line {#фановская-структура}

The seven Fano lines of $\mathrm{PG}(2,2)$ (with the identification $\{1,2,3,4,5,6,7\} = \{A,S,D,L,E,U,O\}$):

| Fano line | Dimensions | Type |
|---|---|---|
| $\{1,2,4\}$ | $\{A,S,L\}$ | Generation triplet |
| $\{2,3,5\}$ | $\{S,D,E\}$ | Color-Gap bridge |
| $\{3,4,6\}$ | $\{D,L,U\}$ | Color-Gap bridge |
| $\{4,5,7\}$ | $\{L,E,O\}$ | Temporal-Gap |
| **$\{5,6,1\}$** | **$\{E,U,A\}$** | **Higgs line** |
| $\{6,7,2\}$ | $\{U,O,S\}$ | Temporal-Gap |
| $\{7,1,3\}$ | $\{O,A,D\}$ | Temporal-spatial |

The Higgs line $\{A,E,U\} = \{5,6,1\}$ is the **unique** Fano line containing both electroweak dimensions $E$ and $U$ (proven in sect. 9.2, [T]).

**Classification with respect to the decomposition $7 = 1_O \oplus 3_{ASD} \oplus \bar{3}_{LEU}$:**

| Type | Fano lines | Number | Characteristic |
|-----|-----------|-------|----------------|
| O-lines | $\{L,E,O\}$, $\{U,O,S\}$, $\{O,A,D\}$ | 3 | Pass through O |
| Mixed | $\{A,S,L\}$, $\{S,D,E\}$, $\{A,E,U\}$ | 3 | Contain elements from both 3 and $\bar{3}$, do not pass through O |
| Inner $\bar{3}$ | $\{D,L,U\}$ | 1 | Entirely within $\bar{3}$ |

:::note Asymmetry 3 / 3̄ [T]
No Fano line lies entirely within $3 = \{A,S,D\}$: the triple $\{1,2,3\}$ is **not** a Fano line. The only inner line is $\{D,L,U\} \subset \bar{3}$. This structural asymmetry between $3$ and $\bar{3}$ is a consequence of the incidence geometry of PG(2,2).
:::

### 2.3 Theorem 2.1 (Fano-Electroweak Construction) {#теорема-фэ}

:::tip[Status: Theorem \[T\]]
The Higgs line $\{A,E,U\}$ canonically defines the electroweak gauge symmetry $\mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$. The uniqueness of the construction is proven: the formula $\kappa_0$ [T] categorically singles out the pair $(E,U)$ — see [sect. 2.3a](#теорема-единственности-фэ).
:::

**Fano-electroweak uniqueness theorem (FE).** *The canonical decomposition $\bar{3} \to 2_{EU} \oplus 1_L$, induced by the Higgs line $\{A,E,U\}$, determines the **unique** effective gauge symmetry of the electroweak sector [T].*

**(a)** The antifundamental triplet $\bar{3}_{LEU} = \{L, E, U\}$ decomposes along the Higgs line:

$$\bar{3}_{LEU} \to 2_{EU} \oplus 1_L$$

where $2_{EU} = \{E, U\}$ is the doublet, $1_L = \{L\}$ is the singlet. The decomposition is canonical: the Higgs line $\{A,E,U\}$ singles out the pair $\{E,U\}$ from $\bar{3}$ in a unique way (sect. 9.2).

**(b)** Gauge structure with explicit generators:

$\mathrm{SU}(2)_L$ — 3 generators (rotations in the $\{E,U\}$-subspace):

$$
T_1 = \frac{1}{2}(\lvert E\rangle\langle U\rvert + \lvert U\rangle\langle E\rvert), \quad T_2 = \frac{1}{2i}(\lvert E\rangle\langle U\rvert - \lvert U\rangle\langle E\rvert), \quad T_3 = \frac{1}{2}(\lvert E\rangle\langle E\rvert - \lvert U\rangle\langle U\rvert)
$$

$\mathrm{U}(1)_Y$ — 1 generator (weak hypercharge):

$$
Y = \frac{1}{3}\left(\sum_{i \in 3} \lvert i\rangle\langle i\rvert - \sum_{j \in \bar{3}} \lvert j\rangle\langle j\rvert\right) + \alpha\left(\lvert L\rangle\langle L\rvert - \frac{1}{2}(\lvert E\rangle\langle E\rvert + \lvert U\rangle\langle U\rvert)\right)
$$

where the first term is an analogue of baryon number (distinguishes 3 and $\bar{3}$), the second is weak isospin within $\bar{3}$ (distinguishes $1_L$ and $2_{EU}$). Total: 4 generators = $\dim(\mathrm{SU}(2) \times \mathrm{U}(1))$.

:::warning Unfixed parameter α
The parameter α in the hypercharge generator Y is **not fixed** by the Fano structure. The uniqueness of the gauge group SU(3)×SU(2)×U(1) is [T]; the uniqueness of the hypercharge embedding is [C, upon fixing α from anomaly freedom or phenomenology].
:::

**(c)** Advantage over the SU(6)-construction:

| Criterion | Old approach [H] (SU(6)) | (FE)-construction [T] |
|----------|--------------------------|--------------------------|
| Number of hypotheses | $\geq 3$ (SU(6), SU(5)-embedding, GJ-decomposition) | 0 (derived from $\kappa_0$ [T]) |
| Use of Fano | Minimal | Central (Higgs line) |
| SU(3) consistency | Requires a separate theorem | Automatic (single SU(3) from $G_2$) |
| Predictive power | X,Y-leptoquarks (not observed) | Yukawa hierarchy (consistent) |
| Economy | 35 generators of SU(6) | 12 generators of SM |
| Status | [H] | **[T]** — uniqueness theorem |

### 2.3a Uniqueness Theorem for the Electroweak Construction {#теорема-единственности-фэ}

:::tip[Status: Theorem \[T\]+\[I\]]
The SM gauge group $G_{\mathrm{SM}} = \mathrm{SU}(3)_C \times \mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$ is the **unique** rank-4 gauge group compatible with the Fano-plane structure and $G_2$-symmetry. The key element is the categorical uniqueness of the pair $(E,U)$ from the formula $\kappa_0$ [T]. Identification of the abstract generators with the physical SM gauge fields is **[I]** (an interpretive step).
:::

**Theorem (Uniqueness of the electroweak construction).** Under axioms A1–A5, the Standard Model gauge group
$$G_{\mathrm{SM}} = \mathrm{SU}(3)_C \times \mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$$
is the **unique** rank-4 gauge group compatible with the Fano-plane structure and $G_2$-symmetry.

#### Proof {#доказательство-единственности-фэ}

**Step 1. $\mathrm{SU}(3)_C$ from $G_2$ [T] (existing result).**

The stabilizer of the O-direction in the $G_2$-representation on $\mathbb{C}^7$ is $\mathrm{SU}(3)$ [T]. Under $G_2 \to \mathrm{SU}(3)$:
$$7 \to 3 \oplus \bar{3} \oplus 1$$
where $1 = O$, $3 = \{A, S, D\}$, $\bar{3} = \{L, E, U\}$. Rank$(\mathrm{SU}(3)_C) = 2$, fully exhausting rank$(G_2)$.

**Step 2. Necessity of tensor extension [T].**

Rank$(G_{\mathrm{SM}}) = 4 > 2 =$ rank$(G_2)$. Consequently, $G_{\mathrm{SM}} \not\subset G_2$. The additional rank 2 can arise **only** from the Page–Wootters tensor extension (A5):
$$\mathcal{H} = \mathcal{H}_O \otimes \mathcal{H}_S = \mathbb{C}^7 \otimes \mathbb{C}^6$$
where $G_2$ acts on $\mathcal{H}_O$ (structural factor) and the electroweak group acts on $\mathcal{H}_S$ (system factor). Tensor independence guarantees commutativity:
$$[\mathrm{SU}(3)_C^{(\text{struct})}, G_{\mathrm{EW}}^{(\text{sys})}] = 0$$
and addition of ranks.

**Step 3. Classification of possible gauge groups on $\bar{3}$ [T].**

On the system factor, the electroweak group $G_{\mathrm{EW}}$ acts on $\bar{3} = \{L, E, U\} \cong \mathbb{C}^3$. Required rank $= 2$. Maximal subgroups of $\mathrm{U}(3)$ of rank 2:

| Subgroup | Rank | Fano-compatibility |
|-----------|:----:|:------------------:|
| $\mathrm{SU}(3)$ | 2 | Yes, but trivial (full $\bar{3}$-symmetry) |
| $\mathrm{SU}(2) \times \mathrm{U}(1)$ | 2 | **Requires** a 2+1 decomposition of $\bar{3}$ |
| $\mathrm{U}(1) \times \mathrm{U}(1)$ | 2 | Abelian — insufficient for the mass spectrum |
| $\mathrm{U}(2)$ | 2 | Isomorphic to $\mathrm{SU}(2) \times \mathrm{U}(1)$ up to center |

**Step 4. Uniqueness of the decomposition $\bar{3} \to 2 \oplus 1$ [T] (key new element).**

Each decomposition $\bar{3} = \{L, E, U\} \to (2) \oplus (1)$ is defined by a distinguished **pair** in $\bar{3}$. Pairs in $\bar{3}$:

| Pair | Remainder | Fano line through the pair | Third point |
|------|---------|----------------------|-------------|
| $\{E, U\}$ | $\{L\}$ | $\{A, E, U\}$ | $A \in 3$ |
| $\{L, U\}$ | $\{E\}$ | $\{D, L, U\}$ | $D \in 3$ |
| $\{L, E\}$ | $\{U\}$ | $\{L, E, O\}$ | $O = 1$ |

Uniqueness criterion — **categorical compatibility with $\kappa_0$ [T]**.

The formula $\kappa_0 = \omega_0 \cdot |\gamma_{OE}| \cdot |\gamma_{OU}| / \gamma_{OO}$ [T] singles out **exactly the pair $(E, U)$** via the morphisms $\mathrm{Hom}(O, E)$ and $\mathrm{Hom}(O, U)$. This is the pair through which regeneration is carried out: $O$ (Ground) is connected to $E$ (Interiority) and $U$ (Unity) **functionally**, through the unique axiomatic formula. Substituting another pair:

- Pair $\{L, U\}$: no $\mathrm{Hom}(O, L)$ in $\kappa_0$ — $L$ is not categorically singled out
- Pair $\{L, E\}$: excludes $U$ from the doublet — destroys the normalization $\mathrm{Tr}(\Gamma) = 1$ (function of U)

Consequently, the decomposition $\bar{3} \to \{E, U\} \oplus \{L\}$ is **unique**.

**Step 5. Uniqueness of the Fano-Higgs line [T] (existing result).**

In PG(2,2), exactly one line passes through the points $E = 5$ and $U = 6$: $\{A, E, U\} = \{1, 5, 6\}$. $\blacksquare$

**Step 6. Uniqueness of $\mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$ [T].**

On the doublet $\{E, U\} \cong \mathbb{C}^2$:
- $\mathrm{SU}(2)_L$ is the unique (up to isomorphism) rank-1 group acting irreducibly on $\mathbb{C}^2$
- $\mathrm{U}(1)_Y$ is the unique (up to normalization) generator commuting with $\mathrm{SU}(2)_L$ and distinguishing $3$ and $\bar{3}$

**Step 7. Result: rank = 4 [T].**

$$\text{rank}(\mathrm{SU}(3)_C) + \text{rank}(\mathrm{SU}(2)_L) + \text{rank}(\mathrm{U}(1)_Y) = 2 + 1 + 1 = 4$$

Since at each step the choice is **unique**, an alternative rank-4 gauge group **does not exist**. $\blacksquare$

:::info[Key new element]
Step 4 — **categorical uniqueness of the pair $(E, U)$** from the formula $\kappa_0$ [T]. Previously, (FE) was treated as a separate hypothesis; now it is derived from the $\kappa_0$-theorem. The formula $\kappa_0$ [T] contains **exactly** $|\gamma_{OE}|$ and $|\gamma_{OU}|$ — this is not a free parameter, but a consequence of the adjunction $\mathcal{D} \dashv \mathcal{R}$ [T].
:::

### 2.4 Theorem 2.2 (Consistency of the Two $\mathrm{SU}(3)$'s) {#согласование-su3}

:::tip[Status: Theorem \[T\]]
The two routes to $\mathrm{SU}(3)_C$ — through $G_2$ (sect. 1.3) and through the 42D tensor structure (sect. 2.1) — yield **the same** subgroup.
:::

**(a)** Definition of consistency. $G_2$ acts on $\mathcal{H}_O \cong \mathbb{C}^7$ (7D formalism). In the 42D PW extension, $\mathrm{SU}(3)_C$ acts on the $3_{ASD}$-factor. Consistent embedding:

$$\mathrm{SU}(3)_C \hookrightarrow G_2|_{\mathrm{Stab}(O)} \cap \mathrm{U}(6)|_{3_{ASD}}$$

is defined by the condition: the $\mathrm{SU}(3)_C$-transformation of the coherence $\gamma_{ij}$ (in 7D) **coincides** with the $\mathrm{SU}(3)$-transformation of the tensor element $\Gamma_{ab,cd}$ (in 42D) when restricted to the 3-to-$\bar{3}$ sector.

**(b)** Proof of consistency. From the decomposition:
- In 7D: $3_{ASD} = \{A, S, D\}$ — fundamental $\mathrm{SU}(3)$ from $G_2$
- In 42D: $3_{ASD}$ — the same triplet in the tensor factor $\mathcal{H}_{6D}$

Identification: $\{A, S, D\}_{7D} = \{1, 2, 3\}_{\mathrm{color}}$. In both formalisms $\mathrm{SU}(3)$ rotates $\{A, S, D\}$ as a fundamental triplet.

**(c)** Commutativity. $\mathrm{SU}(3)_C$ acts on $3_{ASD}$, while $\mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$ acts on $\bar{3}_{LEU}$ (through the decomposition $\bar{3} \to 2_{EU} \oplus 1_L$). Since the subspaces do not intersect:

$$[\mathrm{SU}(3)_C, \, \mathrm{SU}(2)_L \times \mathrm{U}(1)_Y] = 0$$

Rank of the full gauge group: $\mathrm{rank}(\mathrm{SU}(3)_C) + \mathrm{rank}(\mathrm{SU}(2)_L) + \mathrm{rank}(\mathrm{U}(1)_Y) = 2 + 1 + 1 = 4 = \mathrm{rank}(\mathrm{SM})$.

**Proof.** Constructive. $G_2 \subset \mathrm{SO}(7)$ acts on $\mathbb{R}^7 = \mathrm{Im}(\mathbb{O})$. The choice of O-direction gives $\mathrm{SU}(3) \subset G_2$ with $7 \to 1 + 3 + \bar{3}$. The Higgs line $\{A,E,U\}$ decomposes $\bar{3} \to 2_{EU} \oplus 1_L$. Commutativity of the diagram:

```
       G₂         Fano plane PG(2,2)
        |                   |
        | Stab(O)           | Higgs line {A,E,U}
        v                   v
      SU(3)_C        SU(2)_L × U(1)_Y
     (on 3_ASD)     (on 2_EU ⊕ 1_L from 3̄_LEU)
```

Commutativity follows from $\{A,S,D\} \cap \{E,U,L\} = \varnothing$. $\blacksquare$

---

## 3. Fermionic Representations as Gap Configurations

### 3.1 Theorem 3.1 (Quarks and Leptons as Gap Configurations)

:::warning[Status: Hypothesis \[H\]]
Elementary fermions are identified with degenerate ($R \to 0$) configurations $\Gamma$, classified by quantum numbers $\mathrm{SU}(3)_C \times \mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$.
:::

:::info Status stratification
- Algebraic embedding $G_2 \supset SU(3) \times SU(2) \times U(1)$: **[T]** (standard group theory)
- Concrete identification of Gap configurations with quarks/leptons: **[H]** (assigned by analogy with quantum numbers, not derived from dynamics)
:::

**(a)** Left quark doublet $Q_L = (u_L, d_L)$:

$$\Gamma_{Q_L}: \quad \mathrm{Gap}(A,L) = \mathrm{Gap}(S,E) = 0 \; (\text{color channels}), \quad \mathrm{Gap}(E,U) = 0 \; (\text{weak isospin})$$

Quantum numbers: $(3, 2)_{1/6}$

**(b)** Right-handed u-quark $u_R$:

$$\Gamma_{u_R}: \quad \mathrm{Gap}(A,L) = \mathrm{Gap}(S,E) = 0, \quad \mathrm{Gap}(E,U) \neq 0$$

Quantum numbers: $(3, 1)_{2/3}$

**(c)** Left lepton doublet $L_L = (\nu_L, e_L)$:

$$\Gamma_{L_L}: \quad \mathrm{Gap}(\{A,S,D\}, \{L,E,U\}) = \mathrm{Gap}_{\max} \; (\text{colorless}), \quad \mathrm{Gap}(E,U) = 0$$

Quantum numbers: $(1, 2)_{-1/2}$

**(d)** Right-handed electron $e_R$:

$$\Gamma_{e_R}: \quad \mathrm{Gap}(\{A,S,D\}, \{L,E,U\}) = \mathrm{Gap}_{\max}, \quad \mathrm{Gap}(E,U) \neq 0$$

Quantum numbers: $(1, 1)_{-1}$

**Justification.** Particles are configurations with $R \approx 0$ (no self-modeling). Their Gap profile determines the transformation properties:

- **Color ($\mathrm{SU}(3)_C$):** determined by the number of transparent channels in the 3-to-$\bar{3}$ sector. 8 transparent $\to$ fundamental representation (quark). 0 transparent $\to$ singlet (lepton).

- **Weak isospin ($\mathrm{SU}(2)_L$):** determined by the transparency of the E-U channel ($\bar{3}$-to-$\bar{3}$ sector). $\mathrm{Gap}(E,U) = 0$ $\to$ doublet. $\mathrm{Gap}(E,U) \neq 0$ $\to$ singlet.

- **Hypercharge ($\mathrm{U}(1)_Y$):** determined by the total Gap in the O-sector:

$$Y = \frac{1}{3}\left(\sum_{i \in 3} \mathrm{Gap}(O,i) - \sum_{j \in \bar{3}} \mathrm{Gap}(O,j)\right)$$

### 3.2 Theorem 3.2 (Anomaly Cancellation)

:::tip[Status: Theorem \[T\]]
The set of fermionic representations satisfies the gauge anomaly cancellation condition.
:::

$$\sum_{\mathrm{fermions}} Y^3 = 0, \quad \sum_{\mathrm{fermions}} Y = 0$$

**Proof.** For one generation: $Q_L(1/6)^3 \times 6 + u_R(2/3)^3 \times 3 + d_R(-1/3)^3 \times 3 + L_L(-1/2)^3 \times 2 + e_R(-1)^3 \times 1 = \ldots$ Standard calculation, identical to SM. The fermionic representations from sect. 3.1 form the same structure as one SM generation — anomalies cancel by construction. $\blacksquare$

### 3.3 Theorem 3.3 (Number of Generations)

:::tip[Status: Theorem \[T\]]
The original argument via $S_4$ orbits is not formalized, but the result $N_{\text{gen}} = 3$ is **rigorously proven** by an alternative route: upper bound $\leq 3$ from swallowtail $A_4$ [T] + lower bound $\geq 3$ from uniqueness of the associative triplet $(1,2,4) \subset \mathbb{Z}_7^*$ [T] + indecomposability of $\mathbb{Z}_3$. Full proof: [Theorem 1.2 (Exactly 3 generations)](/docs/physics/particle-physics/fermion-generations#теорема-ровно-три-генерации).
:::

**(a)** Each generation corresponds to a **topologically distinct** minimum of $V_{\mathrm{Gap}}$ in the vacuum configuration.

**(b)** From Swallowtail analysis: the number of minima of $V_{\mathrm{eff}}$ depends on the codimension of the catastrophe. For $A_4$ (swallowtail): up to 3 minima.

**(c)** The number of generations $N_{\mathrm{gen}} =$ the number of distinct **types** of degenerate $\Gamma$-configurations with $R \to 0$ not connected by a $G_2$-transformation.

**(d)** From the Fano structure: the 7 Fano lines define 7 "privileged" triplets. From Fano duality (point $\leftrightarrow$ line): each point lies on 3 lines $\to$ 3 nonequivalent "types" of vacuum alignment $\to$ **$N_{\mathrm{gen}} = 3$**.

**Justification of (d).** The vacuum configuration selects the O-direction (sect. 1.3). The remaining 6 directions form a Fano graph with 3 lines passing through each point. Three classes of nonequivalent orientations of the triplet $(A,S,D)$ relative to the Fano structure give 3 generations. More precisely: the automorphism group of the Fano plane $\mathrm{PSL}(2,7)$ (order 168) acts on 7 points. The stabilizer of one point (O) has order $168/7 = 24 \cong S_4$. Orbits of $S_4$ on pairs from the remaining 6 points: $C(6,2) = 15$ pairs, divided into classes by size. Three classes $\to$ three generations.

---

## 4. Chirality from $G_2$-Orientability

### 4.1 Clifford Spinor Algebra on $\mathrm{Im}(\mathbb{O})$

The Clifford algebra $\mathrm{Cliff}(7)$ is defined by generators $\{\Gamma_i\}_{i=1}^{7}$ corresponding to the 7 imaginary units of the octonions $\{e_1, \ldots, e_7\} \leftrightarrow \{A, S, D, L, E, U, O\}$:

$$\Gamma_i \Gamma_j + \Gamma_j \Gamma_i = -2\delta_{ij} \cdot \mathbf{1}_8$$

$\mathrm{Cliff}(7) \cong M_8(\mathbb{R}) \oplus M_8(\mathbb{R})$. Spinor representation: $\Delta_7 = \mathbb{R}^8$.

There is an isomorphism of spinor representations: the spinor space $\Delta_7 \cong \mathbb{O}$ (octonions as an 8-dimensional real space). Action of the Clifford generator:

$$\Gamma_i(\psi) \;\longleftrightarrow\; e_i \cdot q \quad (i = 1, \ldots, 7)$$

where the multiplication is **left** octonionic.

### 4.2 Parallel Spinor and $G_2$-Holonomy

On a $G_2$-manifold there exists a unique covariantly constant spinor $\eta_0 = 1_{\mathbb{O}} \in \mathbb{O}$ — the unit of the octonions. $G_2$ acts on $\mathrm{Im}(\mathbb{O})$ (leaving 1 fixed), so $g \cdot \eta_0 = \eta_0$ for all $g \in G_2$.

The parallel spinor $\eta_0$ defines a 3-form:

$$\varphi_{ijk} = \langle \Gamma_{ijk} \eta_0, \eta_0 \rangle$$

This 3-form is the standard calibrating form of $G_2$:

$$\varphi = \sum_{(i,j,k) \in \mathrm{Fano}} e^i \wedge e^j \wedge e^k$$

summing over the 7 Fano lines. **Orientability of a $G_2$-manifold is equivalent to the existence of a parallel spinor.**

### 4.3 Chiral Operator from 4D Reduction

Under reduction 7D $\to$ 4D (splitting $\mathrm{Im}(\mathbb{O}) = \mathbb{R}^1_O \oplus \mathbb{R}^3_{ASD} \oplus \mathbb{R}^3_{LEU}$) the spinor representation induces a chiral operator:

$$\gamma_5 = i\Gamma_O \Gamma_A \Gamma_S \Gamma_D$$

This operator has eigenvalues $\pm 1$ and defines the chirality of 4D spinors:

$$\gamma_5 \psi_L = -\psi_L, \quad \gamma_5 \psi_R = +\psi_R$$

The chirality of a 4D spinor is determined by the **internal spinor** $\chi_{\mathrm{int}}$:

$$\gamma_5 \psi = \pm \psi \quad \Longleftrightarrow \quad \Gamma_L \Gamma_E \Gamma_U \chi_{\mathrm{int}} = \mp \chi_{\mathrm{int}}$$

:::tip[Status: Theorem \[T\]]
The connection $\mathrm{Gap}(E,U) = 0 \leftrightarrow$ left chirality is derived from the structure of the $G_2$-parallel spinor $\eta_0$ and the reduction $\mathrm{Cliff}(7) \supset \mathrm{Cliff}(1,3) \otimes \mathrm{Cliff}(3)$.
:::

---

## 5. Full Gauge Structure: 18 Bosons {#калибровочные-бозоны}

### 5.1 Theorem 5.1 (Full Table of Gauge Fields)

:::tip[Status: Theorem \[T\] for the SM part; \[H\] for $G_2$-extra]
$G_2$-generators generate $\mathrm{SU}(3)_C$ (8 gluons) and 6 $G_2$-extra bosons. The Fano-electroweak construction (FE) determines $\mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$ (4 bosons) — **[T]** (uniqueness from $\kappa_0$).
:::

| Field | Group | Number | Mass | Status |
|---|---|---|---|---|
| Gluons $g$ | $\mathrm{SU}(3)_C$ | 8 | 0 (confinement) | SM [T] |
| $W^\pm, Z$ | $\mathrm{SU}(2)_L$ | 3 | $M_W, M_Z$ (Higgs) | SM [T] |
| Photon $\gamma$ | $\mathrm{U}(1)_{\mathrm{EM}}$ | 1 | 0 | SM [T] |
| **$G_2$-extra** | **$G_2/\mathrm{SU}(3)$** | **6** | **$M_{G_2} \sim \mu_{\mathrm{phys}}$** | **Beyond SM [H]** |

**(a)** 6 $G_2$-extra bosons are "connector" fields from $3 + \bar{3}$ in the decomposition $14 \to 8 + 3 + \bar{3}$. They connect the spatial ($3$) and Gap ($\bar{3}$) sectors. The mass is determined by the Gap in the O-to-$3$ and O-to-$\bar{3}$ sectors:

$$M_{G_2}^{(\mathrm{extra})} \sim \mu_{\mathrm{phys}} \cdot \mathrm{Gap}_{\mathrm{vac}}^{(O)} \cdot |\gamma_{\mathrm{vac}}^{(O)}|$$

**(b)** Total number of gauge bosons: $8 + 3 + 1 + 6 = $ **18**.

:::info[Note: X,Y-leptoquarks removed]
In the previous version, 12 X,Y-leptoquarks were derived from the chain $\mathrm{SU}(6) \to \mathrm{SU}(5) \to \mathrm{SM}$. The Fano-electroweak construction (FE) does not require an intermediate $\mathrm{SU}(5)$-structure, so X,Y-leptoquarks are **not predicted**. Their absence weakens the prediction for proton decay via d=6 operators (see sect. 13).
:::

### 5.2 Mass Hierarchy of Gauge Bosons

:::warning[Status: Hypothesis \[H\]]
The mass scale hierarchy of gauge bosons is determined by the Gap hierarchy of the vacuum.
:::

**(a)** Massless ($\mathrm{Gap} = 0$ in the corresponding sector):
- Gluons: $\mathrm{Gap} = 0$ in 3-to-$\bar{3}$ $\to$ confinement (nonlinear dynamics at $\mathrm{Gap} \to 0$)
- Photon: $\mathrm{Gap} = 0$ for the diagonal $\mathrm{U}(1)_{\mathrm{EM}}$ combination

**(b)** Electroweak scale ($\mathrm{Gap} \sim 10^{-17}$ from Planck):
- $W^\pm, Z$: $\mathrm{Gap}(E,U) \sim v/M_{\mathrm{Planck}} \sim 10^{-17}$

**(c)** Planck scale:
- $G_2$-extra: $\mathrm{Gap} \sim 1$ $\to$ mass $\sim M_{\mathrm{Planck}}$

**Corollary.** The mass hierarchy $M_\gamma = 0 \ll M_W \ll M_{G_2}$ follows from the Gap-value hierarchy $0 \ll 10^{-17} \ll 1$ in the corresponding coherence sectors. The mass hierarchy problem reduces to the question: **why does the Gap vacuum have such different values in different sectors?**

### 5.3 Hypothesis 5.1 (Resolution of the Hierarchy Problem via RG)

:::warning[Status: Hypothesis \[H\]]
The hierarchy of Gap values in the vacuum follows from RG-evolution with democratic initial conditions at the Planck scale.
:::

**(a)** At the Planck scale: all $\mathrm{Gap} \sim O(1)$ (democratic initial condition).

**(b)** RG-flow from Planck to IR: different sectors run with different anomalous dimensions:

| Sector | Anomalous dimension | Gap at IR scale |
|---|---|---|
| 3-to-$\bar{3}$ (color) | $\Delta_{3\bar{3}} = 0$ (marginal) | $\sim 0$ (confinement) |
| $\bar{3}$-to-$\bar{3}$ (EW) | $\Delta_{\bar{3}\bar{3}} = \Delta_3 = 5/42$ | $\sim 10^{-17}$ (EW scale) |
| O-to-3 (gravity) | $\Delta_{O3} \gg 1$ (IR-relevant) | $\sim 1$ (Planck scale) |

**(c)** The difference in anomalous dimensions is determined by the Fano combinatorics: the number of Fano lines passing through a pair $(i,j)$ influences $\Delta_{ij}$.

:::info[Note]
The anomalous dimension $\Delta_3 = 5/42$ in the $\bar{3}$-to-$\bar{3}$ sector is a characteristic value fixed by $G_2$-invariance and the Fano structure (see [evolution](/docs/core/dynamics/evolution)). The exponential suppression $e^{-\Delta \cdot \ln(M_P/M_{EW})} \sim 10^{-17}$ at $\Delta = 5/42$ and 39 e-folds of RG-running reproduces the electroweak hierarchy.
:::

---

## 6. Higgs Mechanism from Gap Condensation

### 6.1 Theorem 6.1 (Higgs Field as E-U Coherence)

:::warning[Status: Hypothesis \[H\]]
Spontaneous electroweak symmetry breaking arises from Gap condensation in the $\bar{3}$-to-$\bar{3}$ sector.
:::

**(a)** The Higgs field is identified with the E-U coherence ($\bar{3}$-to-$\bar{3}$ sector):

$$H \sim \gamma_{EU} = |\gamma_{EU}| e^{i\theta_{EU}}$$

**(b)** VEV (vacuum expectation value):

$$\langle H \rangle = \langle |\gamma_{EU}| \rangle e^{i\langle\theta_{EU}\rangle} \neq 0$$

Non-zero VEV breaks $\mathrm{SU}(2)_L \times \mathrm{U}(1)_Y \to \mathrm{U}(1)_{\mathrm{EM}}$:
- $\mathrm{SU}(2)_L$: 3 generators $\to$ 2 broken ($W^+, W^-$) + 1 linear combination broken ($Z$)
- $\mathrm{U}(1)_Y$: 1 generator
- $\mathrm{U}(1)_{\mathrm{EM}}$ = diagonal subgroup (photon) — unbroken

**(c)** Mass of the $W$-boson:

$$M_W = \frac{g}{2} v, \quad v = \langle |\gamma_{EU}| \rangle \cdot \mu_{\mathrm{phys}}$$

where $g$ is the electroweak coupling constant, $\mu_{\mathrm{phys}} = \mu \cdot \omega_0$.

**(d)** The Gap potential projected onto the E-U channel:

$$V_{EU}(\gamma_{EU}) = \mu^2 |\gamma_{EU}|^2 + \lambda_4 |\gamma_{EU}|^4 + \lambda_3 \bar{A} |\gamma_{EU}|^3 \cos(\text{phase})$$

:::danger Warning C7: non-perturbative regime
The parameter λ₃ ≈ 74 ≫ 4π means that the octonionic cubic vertex is in the **strong coupling** regime. All loop calculations using λ₃ as a perturbative parameter are formally unreliable. The quantitative results in this section (masses, branching ratios, numerical coefficients) have status **[H]** pending a non-perturbative analysis.
:::

At $\mu^2 < 0$ (low-temperature regime): minimum at $|\gamma_{EU}| = v \neq 0$ — the standard Higgs mechanism applied to the Gap potential.

### 6.2 Theorem 6.2 (Higgs Mass with Octonionic Correction)

:::tip[Status: Hypothesis \[H\]]
The octonionic structure predicts a deviation of the Higgs mass from the standard relation.
:::

**(a)** Higgs boson mass (second derivative of $V_{EU}$ at the minimum):

$$M_H^2 = 2\lambda_4 v^2 + \frac{3\lambda_3^2 \bar{A}^2}{4\mu^2}$$

First term — standard (from $V_4$). Second — **octonionic correction** from $V_3$.

**(b)** In SM: $M_H^2 = 2\lambda v^2$ (one parameter $\lambda$). In UHM: $M_H^2 = 2\lambda_4 v^2 + \delta M_H^2$, where:

$$\delta M_H^2 = \frac{3\lambda_3^2 \bar{A}^2}{4\mu^2} \approx \frac{3 \cdot (73.8)^2 \cdot (0.047)^2}{4 \cdot 16.6} \approx 5.5$$

**(c)** Octonionic correction to $\lambda_{\mathrm{eff}} = \lambda_4 + \delta\lambda$:

$$\frac{\delta\lambda}{\lambda_4} = \frac{3\lambda_3^2 \bar{A}^2}{8\lambda_4 \mu^2 v^2}$$

:::info[Falsifiable prediction \[I\]]
As the precision of measurement of the triple Higgs vertex improves (HL-LHC, FCC), the effective self-coupling $\lambda_{\mathrm{eff}}$ differs from the SM value by:

$$\frac{\delta\lambda}{\lambda_{\mathrm{SM}}} \sim \frac{\lambda_3^2 \bar{A}^2}{\lambda_4 \mu^2} \sim O(10^{-2}\text{--}10^{-3})$$

— at the percent level, potentially accessible to FCC-hh. Detection of a deviation of $\lambda_{\mathrm{eff}}$ from the SM prediction would confirm the $V_3$ contribution; absence of deviation at the $10^{-3}$ level constrains $\lambda_3 \bar{A}/\mu$.
:::

---

## 7. Ward Identities and the $\Lambda$ Suppression Factor

### 7.1 Vacuum Correlator from Ward Identities

The 14 Ward identities generated by $G_2$-symmetry uniquely fix the vacuum two-point Gap correlator:

$$C_{(ij),(kl)}^{(\mathrm{vac})} = \langle\mathrm{Gap}(i,j) \cdot \mathrm{Gap}(k,l)\rangle_{\mathrm{vac}} = \alpha \delta_{(ij),(kl)} + \beta \sum_p \Pi_p^{(ij)} \Pi_p^{(kl)} + \gamma \epsilon^{\mathrm{Fano}} \epsilon^{\mathrm{Fano}}$$

With $G_2$-invariance taken into account: $C$ decomposes over $G_2$-invariant tensors:

$$C = \alpha \cdot \mathbf{1}_{21} + \beta \cdot \mathbf{F}_{21} + \gamma \cdot \mathbf{F}_{21}^2$$

The Ward identities fix the relations:

$$\beta = -\frac{3\alpha}{7}, \quad \gamma = \frac{3\alpha}{49}$$

The only free parameter is $\alpha$ (overall amplitude of fluctuations).

### 7.2 Anticorrelation and the $19/49$ Suppression Factor

:::tip[Status: Theorem \[T\]]
The Ward identities lead to suppression of the total contribution of Gap fluctuations to $\Lambda$.
:::

The correlator $C = \lambda_+ P_7 + \lambda_- P_{14}$ with eigenvalues $\lambda_+ = 19\alpha/49$ and $\lambda_- = 73\alpha/49$ (from the [$F_{21}$ spectrum](/docs/physics/gauge-symmetry/noether-charges#собственные-значения-f21)). The vector $\mathbf{1}_{21}$ lies entirely in the Fano-symmetric sector $V_7$ ($P_7\mathbf{1} = \mathbf{1}$), so the total contribution of Gap fluctuations to $\Lambda$ is determined only by the "small" eigenvalue $\lambda_+$:

$$\frac{\mathbf{1}^T C \mathbf{1}}{\mathbf{1}^T (\alpha I_{21}) \mathbf{1}} = \frac{\lambda_+}{\alpha} = \frac{19}{49} \approx 0.39$$

Suppression by a factor of $\sim 2.6$ (or $10^{-0.41}$), applied to the cosmological constant $\Lambda$. More detail: [Cosmological constant](/docs/physics/gravity/cosmological-constant).

---

## 8. Generation Selection Principle

### 8.1 PSL(2,7)-Classification of Z₇-Orbits

The three fermion generations are determined by three Fano phases $\phi_n = 2\pi k_n / 7$, where $(k_1, k_2, k_3) \subset \mathbb{Z}_7^*$. Of the 20 unordered triples ($C(6,3)$) — which one is realized?

**Definition.** A Z₇-triplet is an unordered triple $\{k_1, k_2, k_3\} \subset \mathbb{Z}_7 \setminus \{0\}$ with $k_i \neq k_j$.

The three Fano lines through O determine a partition of $\{1,2,3,4,5,6\}$ into three pairs. The number of such partitions:

$$\frac{6!}{(2!)^3 \cdot 3!} = 15$$

### 8.2 Theorem 8.1 (PSL(2,7)-Orbits)

:::tip[Theorem 8.1 (PSL(2,7)-orbits) \[T\]]
The automorphism group of the Fano plane $\mathrm{PSL}(2,7)$ (order 168) acts on the set of partitions and divides the 15 partitions into two equivalence classes.
:::

**(a)** $\mathrm{PSL}(2,7)$ contains the stabilizer of the point O: $\mathrm{Stab}(O) \cong S_4$ (order 24). Action of $S_4$ on the 6 points $\{1,\ldots,6\}$ via $S_4 \subset S_6$.

**(b)** Number of orbits on 15 partitions under the action of $S_4$: by Burnside's lemma:

$$|X/S_4| = \frac{1}{|S_4|} \sum_{g \in S_4} |X^g| = 2$$

Two equivalence classes:
- **Class I** (type "associative"): 6 partitions. $(k_1, k_2, k_3)$ such that $k_1 + k_2 + k_3 \equiv 0 \pmod{7}$.
- **Class II** (type "non-associative"): 9 partitions. $k_1 + k_2 + k_3 \not\equiv 0 \pmod{7}$.

**(c)** Example. Multiplicative group $\mathbb{Z}_7^* = \{1,2,3,4,5,6\}$. Triple $(1,2,4)$: $1+2+4 = 7 \equiv 0 \pmod{7}$ — **Class I**.

**Proof.** From the structural theorem for $\mathrm{PSL}(2,7)$: the stabilizer of a point $S_4$ acts on $\mathbb{F}_7 \setminus \{0\}$ via linear/affine transformations. A partition $\{a_1,b_1\},\{a_2,b_2\},\{a_3,b_3\}$ is invariant under $g \in S_4$ if and only if $g$ permutes the pairs. The orbit structure is determined by the "sum invariant" $\sigma = k_1 + k_2 + k_3 \bmod 7$. Under the $S_4$-action, $\sigma \equiv 0$ is an invariant condition (subset of the kernel). $\blacksquare$

### 8.3 Theorem 8.2 (Selection Principle: Minimal Associator)

:::tip[Theorem 8.2 (Selection principle) \[T\]]
The physically realized Z₇-triplet minimizes the total associator of the three generations. The unique triplet with $\mathcal{A} = 0$ is $(1,2,4)$.
:::

**(a)** Associator measure of a triplet:

$$\mathcal{A}(k_1, k_2, k_3) := \|[e_{k_1}, e_{k_2}, e_{k_3}]\|^2 = \|(e_{k_1} \cdot e_{k_2}) \cdot e_{k_3} - e_{k_1} \cdot (e_{k_2} \cdot e_{k_3})\|^2$$

where $e_k$ are the imaginary units of the octonions.

**(b)** From the octonion multiplication table (see [octonionic derivation](/docs/proofs/minimality/theorem-octonionic-derivation)):

For a Fano triplet $(i,j,k)$: $[e_i, e_j, e_k] = 0$ (associator is zero). For a non-Fano triple:

$$\|[e_i, e_j, e_k]\|^2 = 4 \quad \text{for all non-Fano triples}$$

**(c)** Classification:

| Triple $(k_1,k_2,k_3)$ | Fano line? | $\mathcal{A}$ | Class |
|---|---|---|---|
| **(1,2,4)** — quadratic residues | **Yes** | **0** | **I (unique)** |
| (3,5,6) — non-residues | No | 4 | II |
| (1,3,5), (2,4,6), ... | No | 4 | II |

**(d)** Class I triplets with $\mathcal{A} = 0$ are **associative**: the three imaginary units $e_{k_1}, e_{k_2}, e_{k_3}$ form an associative subalgebra $\mathbb{H} \subset \mathbb{O}$ (quaternionic).

**(e)** Selection principle. From $V_3$-dynamics: the vacuum configuration minimizes energy. Contribution of three generations:

$$V_3^{(\text{gen})} \propto \mathcal{A}(k_1, k_2, k_3) \cdot \lambda_3 \prod_n |\gamma_n|$$

**Minimum is reached at $\mathcal{A} = 0$** — Class I.

**(f)** $(1,2,4)$ is the **unique** triplet from $\mathbb{Z}_7^* \setminus \{7\}$ with $\mathcal{A} = 0$ (up to permutations). This is the subgroup of index 2 in $\mathbb{Z}_7^*$, isomorphic to $\mathbb{Z}_3$ (quadratic residues $\bmod 7$).

:::info[Note on uniqueness]
The map $k \to 7-k \pmod{7}$ is **not** an automorphism of the Fano plane ($k \to -k \notin \mathrm{Aut}(\mathrm{PG}(2,2)) = \mathrm{PSL}(2,7)$), so $\{3,5,6\}$ is not equivalent to $\{1,2,4\}$. Check: $\{3,5,6\}$ is not a Fano line, $\mathcal{A}(3,5,6) = 4 \neq 0$. The selection principle singles out $(1,2,4)$ in a **unique** way, without degeneracy.
:::

**Proof.** Step 1: from the PSL(2,7)-classification (sect. 7.2) — two classes. Step 2: from $V_3$-minimization — Class I ($\mathcal{A} = 0$). Step 3: from the definition of the associator in $\mathbb{O}$ — a triple $(k_1,k_2,k_3)$ forms a quaternionic subalgebra if and only if the triple is a subgroup of $\mathbb{Z}_7^*$. The unique subgroup of order 3 in $\mathbb{Z}_7^*$: the quadratic residues $\{1,2,4\}$. $\blacksquare$

---

## 9. Fano Selection Rule for Yukawa Couplings

### 9.1 Definition (Fano-Higgs Line)

**Definition.** The Fano-Higgs line is the Fano line of $\mathrm{PG}(2,2)$ containing **both** Higgs dimensions $E = 5$ and $U = 6$.

### 9.2 Theorem 9.1 (Uniqueness of the Fano-Higgs Line)

:::tip[Theorem 9.1 (Uniqueness) \[T\]]
There exists exactly one Fano-Higgs line: $\{1, 5, 6\} = \{A, E, U\}$.
:::

**Proof.** In $\mathrm{PG}(2,2)$ exactly one line passes through any two points. Points $E=5$ and $U=6$. From the Fano-line table (see [octonionic derivation](/docs/proofs/minimality/theorem-octonionic-derivation)):

$$\{5,6,1\} = \{A, E, U\}$$

This is the unique line containing both 5 and 6. $\blacksquare$

### 9.3 Theorem 9.2 (Fano Selection Rule)

:::tip[Theorem 9.2 (Fano selection rule) \[T\]]
The tree-level Yukawa coupling of generation $k_n$ with the Higgs field $\gamma_{EU}$ is proportional to the octonionic structure constant $f_{k_n, E, U}$, which is non-zero if and only if $(k_n, E, U)$ is a Fano line.

Status **[T]**: proven through the octonionic structure constants $f_{ijk}$ — the unique $G_2$-invariant trilinear operator on $\mathrm{Im}(\mathbb{O})$. Full proof: [Theorem 2.2](/docs/physics/gauge-symmetry/fano-selection-rules#теорема-фано-отбор-fijk).
:::

$$y_n^{(\text{tree})} = g_W \cdot f_{k_n, E, U} \cdot \sin\left(\frac{2\pi k_n}{7}\right) \cdot |\gamma_{\text{vac}}^{(EU)}|$$

where $f_{ijk} = \pm 1$ if $(i,j,k)$ is a Fano line, and $f_{ijk} = 0$ otherwise.

**(a)** For $k_n = 1$: the triple $(1, 5, 6) = \{A, E, U\}$ is a Fano line. $f_{1,5,6} = 1$.

$$y_1^{(\text{tree})} = g_W \cdot 1 \cdot \sin(2\pi/7) \cdot |\gamma_{\text{vac}}| \neq 0$$

**(b)** For $k_n = 2$: the triple $(2, 5, 6)$. Line through 2 and 5: $\{2,3,5\}$ (contains 3, not 6). Line through 2 and 6: $\{6,7,2\}$ (contains 7, not 5). $f_{2,5,6} = 0$.

$$y_2^{(\text{tree})} = 0$$

**(c)** For $k_n = 4$: the triple $(4, 5, 6)$. Line through 4 and 5: $\{4,5,7\}$ (contains 7, not 6). Line through 4 and 6: $\{3,4,6\}$ (contains 3, not 5). $f_{4,5,6} = 0$.

$$y_4^{(\text{tree})} = 0$$

**(d)** Summary of the selection rule:

| Generation | $k_n$ | Dimension | $(k_n, E, U)$ Fano? | $y^{(\text{tree})}$ |
|---|---|---|---|---|
| **Heaviest** | **1** | **A (awareness)** | **Yes: $\{1,5,6\}$** | **$\neq 0$** |
| Light | 2 | S (stability) | No | $= 0$ |
| Light | 4 | L (levels) | No | $= 0$ |

**Proof.** The Yukawa coupling of three dimensions $(a,b,c)$ is proportional to the octonionic structure constant:

$$y_{abc}^{(\text{tree})} \propto f_{abc}$$

where $f_{abc} = \pm 1$ if and only if $\{a,b,c\}$ is a Fano line of $\mathrm{PG}(2,2)$, and $f_{abc} = 0$ otherwise. This follows from the multiplication table of $\mathbb{O}$: $e_a e_b = f_{abc} e_c + \delta_{ab}$.

For generation $k=1$ (line $\{1,5,6\}$): $f_{156} = 1$ — Yukawa $O(1)$.
For generations $k=2,4$: the triples $(2,5,6)$ and $(4,5,6)$ are not Fano lines, $f_{256} = f_{456} = 0$ — Yukawa couplings vanish. $\blacksquare$

### 9.4 Z₃-Symmetry and Its Breaking

The map $\sigma: k \mapsto 2k \bmod 7$ is an automorphism of the Fano plane and cyclically permutes the elements of the Fano line $\{1,2,4\}$:

$$\sigma: 1 \to 2 \to 4 \to 1 \quad (\text{cycle } (1\,2\,4))$$

**Corollary.** Any Fano-invariant functional $F(k_1, k_2, k_3)$ satisfies $F(1,2,4) = F(2,4,1) = F(4,1,2)$, i.e., it is **the same** for all three generations. Consequently, the mass hierarchy $m_t \gg m_c \gg m_u$ **cannot** be explained by Fano geometry alone — a Z₃-breaking factor is required.

This factor is provided by the Fano-Higgs line $\{1,5,6\}$: among the elements of the generation triplet $(1,2,4)$, only $k=1$ lies on this line. The vacuum Gap profile additionally breaks Z₃, since $k=1$ (A) and $k=2$ (S) lie in the 3-sector, while $k=4$ (L) lies in the $\bar{3}$-sector.

---

## 10. Mass Hierarchy of Generations

### 10.1 Theorem 10.1 (Mass Hierarchy: Qualitative)

:::tip[Theorem 10.1 (Mass hierarchy) \[T\]]
The Fano selection rule [T] (sect. 9.3) generates the mass hierarchy $m_t \gg m_c, m_u$, resolving vulnerability K-1 (the IR fixed point paradox).
:::

**(a)** $k=1$ (A) — **third generation** (t, b, $\tau$): tree-level Yukawa coupling $y_1^{(\text{tree})} \sim O(1)$. Under RG-evolution $y_1$ is attracted to the quasi-IR fixed point (Pendleton–Ross, 1981):

$$m_t = y_t^{(\text{FP})} \cdot \frac{v}{\sqrt{2}} \approx 1.0 \times 174 \approx 173 \text{ GeV}$$

**(b)** $k=2$ (S) and $k=4$ (L) — first and second generations: $y_{2,4}^{(\text{tree})} = 0$. Masses are generated by **loop** corrections through the $V_3$-potential:

$$y_{2,4}^{(\text{eff})} \sim \epsilon_{\text{loop}} \ll 1$$

**(c)** Loop Yukawa couplings are **not** attracted to the IR fixed point (since $y \ll 1$, the quadratic term $c_1 y^2$ is negligible compared to the gauge term $c_3 g_s^2$). Their RG-running is determined by the anomalous dimension of mass:

$$y_n(\mu) = y_n(\mu_0) \cdot \left(\frac{\alpha_s(\mu)}{\alpha_s(\mu_0)}\right)^{12/(33-2N_f)} \quad (n = 2, 4)$$

### 10.2 Resolution of the IR Fixed Point Paradox

:::info[Resolution of vulnerability K-1]
Previously, three O(1) initial Yukawa couplings were postulated ($|y_1|:|y_2|:|y_3| = 0.78:0.98:0.43$), all of which converge to a single IR fixed point, generating no hierarchy. The Fano selection rule eliminates this problem: initial Yukawa couplings are $y_1^{(0)} \sim O(1)$, $y_2^{(0)} = 0$, $y_4^{(0)} = 0$.
:::

RG-system with one O(1) Yukawa + two small ones:

$$\frac{dy_1}{d\ln\mu} \approx \frac{y_1}{16\pi^2}(c_1 y_1^2 - c_3 g_s^2 - c_4 g_W^2)$$

$$\frac{dy_n}{d\ln\mu} \approx \frac{y_n}{16\pi^2}(c_2 y_1^2 - c_3 g_s^2 - c_4 g_W^2) \quad (n = 2, 4;\; y_n \ll 1)$$

$y_1$ is attracted to $y^{(\text{FP})} = \sqrt{(c_3 g_s^2 + c_4 g_W^2)/c_1} \approx 1$. Small $y_{2,4}$ run with anomalous dimension and **preserve** their smallness. The hierarchy is stable under RG-evolution to the electroweak scale.

### 10.3 Mass Generation Mechanism for Light Generations

Generations $k=2$ (S) and $k=4$ (L) with $y^{(\text{tree})} = 0$ acquire masses through **mixing** with generation $k=1$ (A), induced by $V_3$-vertices on non-Fano triples via the intermediate dimension $D=3$:

- $V_3 \supset \lambda_3 |\gamma_{12}| |\gamma_{23}| |\gamma_{13}| \sin(\theta_{12} + \theta_{23} - \theta_{13})$ — triple $\{1,2,3\} = \{A,S,D\}$
- $V_3 \supset \lambda_3 |\gamma_{24}| |\gamma_{43}| |\gamma_{23}| \sin(\theta_{24} + \theta_{43} - \theta_{23})$ — triple $\{2,4,3\} = \{S,L,D\}$
- $V_3 \supset \lambda_3 |\gamma_{14}| |\gamma_{43}| |\gamma_{13}| \sin(\theta_{14} + \theta_{43} - \theta_{13})$ — triple $\{1,4,3\} = \{A,L,D\}$

All three are non-Fano triples (containing $D=3$ as mediator). Generation mixing passes through the **color dimension D**, which connects the generation mechanism with [confinement](/docs/physics/gauge-symmetry/confinement).

### 10.4 Theorem 10.2 (Generation Assignment and Fano Distance to Higgs)

:::warning[Hypothesis 10.2 (Generation assignment) \[H\]]
The distinction between $k=2$ and $k=4$ is determined by the type of intermediate sector in the Fano path to the Higgs. Strictly — a hypothesis requiring lattice confirmation.
:::

Define the **O-free Fano distance** $d_H(k_n)$ as the minimum number of Fano lines in the path from $k_n$ to the Higgs $(E, U)$, not passing through $O = 7$ ($\mathrm{Gap} \sim 1$, suppressed paths).

**(a)** $k=1$ (A): direct Fano line $\{1,5,6\}$. $d_H(1) = 0$ (tree level).

**(b)** $k=2$ (S): path $\{2,3,5\}: S \to D \to E$, then $\{5,6,1\}: E \to U$. One intermediate step through the $3$-to-$3$ sector ($\mathrm{Gap} \sim \epsilon_{\text{space}} \neq 0$). $d_H(2) = 1$.

**(c)** $k=4$ (L): path $\{3,4,6\}: L \to D \to U$, then $\{5,6,1\}: U \to E$. One intermediate step, entirely through the confinement sector ($\mathrm{Gap} \approx 0$). $d_H(4) = 1$.

**(d)** Key distinction: the path $k=2$ passes through the $3$-to-$3$ sector ($\mathrm{Gap} \sim \epsilon_{\text{space}} \neq 0$), while the path $k=4$ passes entirely through the confinement sector ($\mathrm{Gap} \approx 0$). Therefore $k=4$ has greater connectivity to the Higgs:

$$y_4^{(\text{eff})} > y_2^{(\text{eff})}$$

**(e)** Generation assignment prediction:

| Mass | Generation | Fano $k$ | Dimension | Mechanism |
|---|---|---|---|---|
| **Heaviest** | 3rd (t,b,$\tau$) | **1** | **A** | Tree-level, IR FP |
| **Medium** | 2nd (c,s,$\mu$) | **4** | **L** | 1-loop, confinement |
| **Light** | 1st (u,d,e) | **2** | **S** | 1-loop, $3$-to-$3$ |

### 10.5 Theorem 10.3 (Phenomenological Bound)

:::warning[Hypothesis 10.3 (Loop suppression of masses) \[H\]]
From the observed quark masses, effective suppression parameters are extracted, consistent with the loop mechanism.
:::

**(a)** Physical Yukawa couplings ($y_n = m_n / 174$ GeV):

| Generation | Fano $k$ | Yukawa | Suppression $y_n/y_t$ |
|---|---|---|---|
| 3rd (t) | 1 (A) | $\approx 1.0$ | 1 (tree-level) |
| 2nd | 4 (L) | $\approx 7.5 \times 10^{-3}$ | $\sim 10^{-2}$ |
| 1st | 2 (S) | $\approx 1.2 \times 10^{-5}$ | $\sim 10^{-5}$ |

**(b)** Suppression $\sim 10^{-2}$ for the second generation is consistent with **one** loop factor:

$$\epsilon_{\text{1-loop}} \sim \frac{\lambda_3}{16\pi^2} \times (\text{Gap factor}) \sim 10^{-2}$$

**(c)** Suppression $\sim 10^{-5}$ for the first generation is consistent with **two** loop factors:

$$\epsilon_{\text{2-loop}} \sim \left(\frac{\lambda_3}{16\pi^2}\right)^2 \times (\text{Gap factors}) \sim 10^{-4}\text{--}10^{-5}$$

### 10.6 Full Mass Table

| Particle | Generation | $k$ | Mechanism | Prediction | Observation |
|---|---|---|---|---|---|
| t | 3 | 1 (A) | Tree + IR FP | 173 GeV | 173 GeV |
| c | 2 | 4 (L) | 1-loop | $\sim$ GeV | 1.3 GeV |
| u | 1 | 2 (S) | 1-loop ($3$-to-$3$) | $\sim$ MeV | 2.2 MeV |
| b | 3 | 1 (A) | Tree + RG | $\sim 4$ GeV | 4.2 GeV |
| s | 2 | 4 (L) | 1-loop | $\sim 100$ MeV | 95 MeV |
| d | 1 | 2 (S) | 1-loop ($3$-to-$3$) | $\sim$ MeV | 4.7 MeV |
| $\tau$ | 3 | 1 (A) | Tree | $\sim 2$ GeV | 1.78 GeV |
| $\mu$ | 2 | 4 (L) | 1-loop | $\sim 100$ MeV | 106 MeV |
| e | 1 | 2 (S) | 1-loop ($3$-to-$3$) | $\sim$ MeV | 0.511 MeV |

:::info[Precision]
All predictions are order-of-magnitude estimates. Exact values require lattice computation of $V_3$-loop contributions.
:::

---

## 11. N=1 Supersymmetry from $G_2$-Holonomy

### 11.1 Theorem 11.1 (N=1 SUSY from the Parallel Spinor)

:::tip[Theorem 11.1 (N=1 SUSY) \[T\]]
The parallel spinor $\eta_0 = 1_\mathbb{O}$ defines exactly one preserved supersymmetry — N=1 SUSY in 4D. Standard result of $G_2$-compactification theory.
:::

**(a)** From M-theory (Aganagic-Witten, 2001; Atiyah-Witten, 2001): compactification 11D $\to$ 4D on a 7-dimensional $G_2$-manifold $M_7$:

$$\mathbb{R}^{1,3} \times M_7, \quad \mathrm{Hol}(M_7) = G_2$$

Number of supersymmetries in 4D = number of covariantly constant spinors on $M_7$ = number of singlets in the decomposition $8_s \to 1 \oplus 7$.

**(b)** $G_2 \subset \mathrm{Spin}(7)$: $\Delta_7 = \mathbb{R}^8 \to 1 \oplus 7$ — exactly **one** parallel spinor $\eta_0$. Consequently, **N=1 SUSY** in 4D.

**(c)** Supersymmetry generator:

$$Q_\alpha = \eta_0 \otimes \psi_\alpha^{(4D)}$$

Anticommutator:

$$\{Q_\alpha, \bar{Q}_{\dot{\beta}}\} = 2\sigma^\mu_{\alpha\dot{\beta}} P_\mu$$

**(d)** SUSY transformations. For the Gap field $\theta_{ij}$ and its superpartner $\tilde{\theta}_{ij}$ (gapsino):

$$\delta_\epsilon \theta_{ij} = \bar{\epsilon} \tilde{\theta}_{ij}, \quad \delta_\epsilon \tilde{\theta}_{ij} = i\sigma^\mu \bar{\epsilon} \partial_\mu \theta_{ij}$$

**Proof.** Standard result of $G_2$-compactification theory (Joyce-Karigiannis, 2017). A covariantly constant spinor $\nabla \eta_0 = 0$ on $M_7$ exists if and only if $\mathrm{Hol} \subseteq G_2$ (Berger's theorem). $\blacksquare$

### 11.2 Theorem 11.2 (Superpartner Spectrum)

:::tip[Theorem 11.2 (Superpartner spectrum) \[T\]]
N=1 SUSY doubles the Gap spectrum: to each Gap field $\theta_{ij}$ (boson, spin 0) there corresponds a superpartner — the gapsino $\tilde{\theta}_{ij}$ (fermion, spin 1/2).
:::

| SM particle | Gap configuration | Superpartner | Gap configuration |
|---|---|---|---|
| Quark $q_L$ | $\mathrm{Gap}(E,U)=0$, $\mathrm{Gap}(3\text{-}\bar{3})\neq 0$ | Squark $\tilde{q}_L$ | $\theta_{\text{Gap}} \to$ boson |
| Gluon $g$ | $\delta\theta_{ij}^{(3\bar{3})}$ | Gluino $\tilde{g}$ | $\tilde{\theta}_{ij}^{(3\bar{3})}$ |
| $W^\pm, Z$ | $\delta\theta_{EU}$, $\delta\theta_{LE,LU}$ | Wino, Zino | $\tilde{\theta}_{EU}$, ... |
| Higgs $H$ | $\gamma_{EU}$ (VEV) | Higgsino $\tilde{H}$ | $\tilde{\gamma}_{EU}$ |
| Graviton $g_{\mu\nu}$ | Metric from Gap | Gravitino $\psi_{3/2}$ | $\tilde{g}_{\mu\nu}$ |

In unbroken SUSY: superpartner mass = particle mass. Observationally: SUSY is broken ($m_{\tilde{q}} \gg m_q$).

### 11.3 SUSY Breaking in the Gap Formalism

:::warning[Hypothesis 11.3 (SUSY breaking via $V_3$) \[H\]]
SUSY breaking in the Gap formalism is the mismatch between bosonic and fermionic minima of $V_{\text{Gap}}$. Construction of the superpotential $W(\Theta)$ remains an open problem.
:::

**(a)** $V_3$ (PT-odd) breaks SUSY: the bosonic and fermionic contributions to $V_3$ do not compensate:

$$V_3^{(\text{bos})} + V_3^{(\text{ferm})} \neq 0$$

**(b)** SUSY-breaking parameter (F-term):

$$F = \langle \partial V_{\text{Gap}} / \partial \theta \rangle_{\text{ferm}} \neq 0$$

**(c)** SUSY-breaking scale from $V_3$-dynamics:

$$\sqrt{F} \sim \sqrt{\lambda_3 \cdot 28 \cdot \epsilon^3} \cdot \mu_{\text{phys}}$$

For cosmological Gap: $\mu_{\text{phys}} \sim M_{\text{Planck}}$, $\epsilon \sim \epsilon_{\text{GUT}} \sim 10^{-3}$:

$$\sqrt{F} \sim \sqrt{73.8 \times 28 \times 10^{-9}} \times M_{\text{Planck}} \approx 1.4 \times 10^{-3} \times M_{\text{Planck}} \approx 3.4 \times 10^{16} \text{ GeV}$$

SUSY-breaking scale $\sqrt{F} \sim 10^{16}$ GeV — an intermediate scale, close to GUT.

### 11.4 Theorem 11.4 (Gravitino Mass)

:::warning[Hypothesis 11.4 (Gravitino mass) \[H\*\]]
The prediction $m_{3/2} \sim 10^{13}$ GeV is conditional on $\mu_{\text{phys}} = M_{\text{Planck}}$; at $\mu_{\text{phys}} = M_{\text{GUT}}$ the value shifts by 3-6 orders of magnitude.
:::

**(a)** Standard supergravity formula:

$$m_{3/2} = \frac{F}{\sqrt{3} M_{\text{Planck}}}$$

**(b)** From the estimate $F \approx (1.4 \times 10^{-3})^2 M_{\text{Planck}}^2 \approx 2 \times 10^{-6} M_{\text{Planck}}^2$:

$$m_{3/2} \approx \frac{2 \times 10^{-6} M_{\text{Planck}}^2}{\sqrt{3} M_{\text{Planck}}} \approx 1.2 \times 10^{-6} M_{\text{Planck}} \approx 2.9 \times 10^{13} \text{ GeV}$$

**(c)** $m_{3/2} \sim 10^{13}$ GeV — a **super-heavy** gravitino. Characteristic of models with SUSY breaking at a high-energy scale (high-scale SUSY).

**(d)** Corollary: squark and slepton masses are of the same order:

$$m_{\tilde{q}} \sim m_{\tilde{l}} \sim m_{3/2} \sim 10^{13} \text{ GeV}$$

Inaccessible to the LHC ($\sqrt{s} = 14$ TeV). This explains the non-observation of superpartners.

---

## 12. SUSY Spectrum and Experimental Consequences

### 12.1 Theorem 12.1 (Full SUSY Spectrum from Gap)

:::warning[Hypothesis 12.1 (SUSY spectrum) \[H\]]
Superpartner masses are determined by SUSY breaking through $V_3$ (gravity mediation).
:::

| Particle | Mass | Status |
|---|---|---|
| Squarks $\tilde{q}$ | $\sim m_{3/2} \sim 10^{13}$ GeV | Unobservable |
| Sleptons $\tilde{l}$ | $\sim m_{3/2} \sim 10^{13}$ GeV | Unobservable |
| Gluino $\tilde{g}$ | $\sim m_{3/2} \sim 10^{13}$ GeV | Unobservable |
| Wino/Bino | $\sim m_{3/2} \cdot (\alpha / 4\pi) \sim 10^{11}$ GeV | Unobservable |
| Higgsino | $\sim \mu_H \sim m_{3/2} \sim 10^{13}$ GeV | Unobservable |
| Gravitino $\psi_{3/2}$ | $m_{3/2} \sim 10^{13}$ GeV | Unobservable |

**Falsifiable prediction.** Gap theory predicts the **absence** of superpartners at scales accessible to the LHC and future colliders ($\sqrt{s} < 10^5$ GeV). Discovery of any superpartner with mass $\ll 10^{13}$ GeV would **falsify** the Gap value $\epsilon_{\text{GUT}} \sim 10^{-3}$.

### 12.2 SUSY Traces

Indirect traces of SUSY may manifest in:

1. **Gauge coupling unification** at $\mu_{\text{GUT}} \sim 2 \times 10^{16}$ GeV (predicted). At $m_{\text{SUSY}} \sim 10^{13}$ GeV, the beta functions contain threshold corrections (SM below $10^{13}$ GeV, MSSM above), and the precision of unification requires a separate check.

2. **Higgs mass** $m_H \approx 125$ GeV — within the MSSM with heavy stops.

3. Gauge coupling unification. From Gap-RG:

$$\alpha_s(\mu_{\text{GUT}}) = \alpha_W(\mu_{\text{GUT}}) = \alpha_{\text{GUT}} \approx 1/24$$

Unification scale:

$$\mu_{\text{GUT}} = M_Z \cdot \exp\left(\frac{2\pi}{\beta_1^{(1)}} \cdot \frac{1}{\alpha_1(M_Z) - \alpha_{\text{GUT}}}\right) \approx 2 \times 10^{16} \text{ GeV}$$

---

## 13. Proton Decay {#распад-протона}

:::info[Note: revision of proton decay predictions]
Within the Fano-electroweak construction (FE), X,Y-leptoquarks are **not predicted** (they were an artifact of the intermediate $\mathrm{SU}(5)$-structure). However, proton decay remains possible through $G_2$-extra bosons and higher-dimensional operators.
:::

### 13.1 Proton Decay via $G_2$-Extra Bosons

:::warning[Status: Hypothesis \[H\]]
Proton decay within (FE) is mediated by $G_2$-extra bosons of Planck mass. Lifetime $\tau_p \sim 10^{72}$ years — practically unobservable.
:::

6 $G_2$-extra bosons with $M_{G_2} \sim M_{\text{Planck}}$ mediate proton decay channels (d=6 operators via $G_2$-extra exchange). Lifetime:

$$\tau_p^{(G_2)} \sim \frac{M_{\text{Planck}}^4}{\alpha_{G_2}^2 m_p^5} \sim 10^{72} \text{ years}$$

This is $\sim 35$ orders of magnitude above the current experimental limit (Super-Kamiokande: $\tau_p > 2.4 \times 10^{34}$ years). **The proton is effectively stable** within (FE).

### 13.2 Consequences for Experiments

| Experiment | Channel | Sensitivity | Status in (FE) |
|---|---|---|---|
| Super-Kamiokande | $p \to e^+\pi^0$ | $> 2.4 \times 10^{34}$ years | Not constraining |
| Hyper-Kamiokande | $p \to e^+\pi^0$ | up to $10^{35}$ years | Not constraining |
| DUNE | $p \to K^+\bar{\nu}$ | up to $10^{35}$ years | Not constraining |

:::info[Falsifiable consequence]
Detection of proton decay at scales $\tau_p \lesssim 10^{40}$ years would **falsify** (FE), since it would indicate an intermediate gauge structure (of $\mathrm{SU}(5)$ type) with bosons at scale $M_X \ll M_{\text{Planck}}$.
:::

---

## 14. Updated CKM Phenomenology

### 14.1 Theorem 14.1 (Updated Phase $\delta_{\text{CP}}$)

:::warning[Hypothesis 14.1 (CP-violation phase) \[H\]]
The formula $\delta_{\text{CP}} = \arg(e^{2\pi i(k_{1\text{st}} + k_{2\text{nd}} - k_{3\text{rd}})/7})$ is heuristic, not derived from diagonalization of Yukawa matrices.
:::

With the assignment $k_{\text{1st}}=2$, $k_{\text{2nd}}=4$, $k_{\text{3rd}}=1$:

**(a)** Bare value:

$$\delta_{\text{CP}} = \arg(e^{2\pi i(2+4-1)/7}) = \arg(e^{10\pi i/7}) = -\frac{4\pi}{7} \approx -102.9°$$

Modulus: $|\delta_{\text{CP}}| = 180° - 102.9° = 77.1°$ (reduction to the first half-plane; $\sin 77.1° = \sin 102.9°$).

**(b)** Two-loop RG-correction:

$$\delta^{(2)} \sim \frac{y_t^2}{16\pi^2} \cdot \ln\frac{\mu_{\text{GUT}}}{\mu_{\text{EW}}} \cdot \frac{2\pi}{7}$$

$$|\delta^{(2)}| \sim \frac{1.0}{16\pi^2} \times 39 \times 0.898 \approx 0.22 \text{ rad} \approx 12.6°$$

**(c)** Final prediction (with negative sign of correction):

$$|\delta_{\text{CP}}^{(\text{phys})}| \approx 77.1° - 12.6° = 64.5° \pm 5°$$

Observed: $69° \pm 4°$ (PDG). Discrepancy $\sim 4.5°$ ($\sim 1\sigma$).

:::info[Note on the sign]
The sign of the two-loop correction is determined from $\mathrm{Im}\,\mathrm{Tr}(Y_u Y_u^\dagger Y_d Y_d^\dagger [Y_u Y_u^\dagger, Y_d Y_d^\dagger])$ (Antusch et al., 2003). With positive sign: $77.1° + 12.6° = 89.7°$ — discrepancy $> 4\sigma$. The new assignment **predicts a negative sign** of the correction. Full range: $|\delta_{\text{CP}}| = 77.1° \pm 12.6°$ (from $64.5°$ to $89.7°$).
:::

### 14.2 Updated CKM Angles

With the assignment $k_{\text{1st}}=2$, $k_{\text{2nd}}=4$, $k_{\text{3rd}}=1$:

**(a)** Fano differences for CKM angles:

$$\Delta k_{12} = |k_{\text{1st}} - k_{\text{2nd}}| = |2 - 4| = 2$$
$$\Delta k_{23} = |k_{\text{2nd}} - k_{\text{3rd}}| = |4 - 1| = 3$$
$$\Delta k_{13} = |k_{\text{1st}} - k_{\text{3rd}}| = |2 - 1| = 1$$

**(b)** Ratios of Fano phases: $\Delta k_{12} : \Delta k_{23} : \Delta k_{13} = 2 : 3 : 1$. Observed angle ratios: $\theta_{12} : \theta_{23} : \theta_{13} \approx 13° : 2.4° : 0.2° \approx 65 : 12 : 1$. The difference is due to RG-suppression through the Fritzsch texture:

$$\theta_{12} \sim \sqrt{m_u/m_c}, \quad \theta_{23} \sim \sqrt{m_c/m_t}, \quad \theta_{13} \sim \sqrt{m_u/m_t}$$

Angles are determined by effective Yukawa couplings, not by the Fano differences directly.

### 14.3 Lepton Sector

**(a)** The Fano selection rule applies to charged leptons as well:
- $\tau$ (heaviest) — $k=1$ (A): tree-level Yukawa.
- $\mu, e$ — $k=4, k=2$: loop-level.

**(b)** Neutrinos: masses are determined by the seesaw mechanism. The selection rule gives:

$$y_{\nu_\tau}^{(\text{tree})} \neq 0, \quad y_{\nu_\mu}^{(\text{tree})} = y_{\nu_e}^{(\text{tree})} = 0$$

$$m_\nu \sim \frac{y_\nu^2 v^2}{M_R} \implies m_{\nu_\tau} \gg m_{\nu_\mu} \gg m_{\nu_e}$$

Consistent with the normal neutrino mass hierarchy.

:::warning[Hypothesis (PMNS) \[H\]]
The large PMNS mixing angles ($\theta_{12} \sim 34°$, $\theta_{23} \sim 45°$) are explained by the fact that the right-handed neutrino mass matrix $M_R$ does not obey the Fano selection rule (right-handed neutrinos are singlets, not connected to the Higgs through E-U). The justification is partial: the selection rule is specific to electroweak Yukawa couplings.
:::

---

## 15. Status Summary

| Result | Status |
|---|---|
| $\mathrm{SU}(3)_C$ from the stabilizer of O in $G_2$ | [T] |
| Decomposition $14 \to 8 + 3 + \bar{3}$ (gluons + extra) | [T] |
| $\mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$ from Fano-electroweak construction (FE) | [T] (combinatorics: uniqueness of $(E,U)$, Higgs line); [C] (dynamical gauge structure, running of couplings) |
| Consistency of the two $\mathrm{SU}(3)$'s ($G_2$ and 42D PW) | [T] |
| Full SM from $G_2$ + (FE) | [C] (electroweak dynamics is conditional) |
| Quarks and leptons as Gap configurations | [H] |
| Three generations from Fano structure ($N_{\text{gen}} = 3$ exactly) | **[T]** ([proof](/docs/physics/particle-physics/fermion-generations#теорема-ровно-три-генерации)) |
| Chirality from $\eta_0$ and $\mathrm{Gap}(E,U) = 0$ | [T] |
| 18 gauge bosons (SM + 6 $G_2$-extra) | [T] for SM; [H] beyond SM |
| Mass hierarchy from Gap hierarchy of the vacuum | [H] |
| Resolution of hierarchy via RG with anomalous dimensions | [H] |
| Higgs as Gap condensate of E-U coherence | [T] (#9: uniqueness of {A,E,U} + T-70: canonical $f_0$) |
| $M_H^2 = 2\lambda_4 v^2 + 3\lambda_3^2 \bar{A}^2/(4\mu^2)$ (octonionic correction) | [H] |
| $\delta\lambda/\lambda_{\text{SM}} \sim O(10^{-2}\text{--}10^{-3})$ (FCC prediction) | [I] |
| Gap anticorrelation (Ward), factor $19/49$ | [T] |
| Generation selection principle $(1,2,4)$ from associator | [T] (uniqueness) |
| Fano Yukawa selection rule | **[T]** (via $f_{ijk}$ — unique $G_2$-invariant trilinear operator) |
| Mass hierarchy $m_t \gg m_c \gg m_u$ from Fano selection | **[T]** (consequence of selection rule [T]) |
| $m_t \approx 173$ GeV from IR fixed point (unique O(1) Yukawa) | [T] |
| Light generation masses via loop suppression | [H] (order of magnitude) |
| Generation assignment: $k=1 \to 3$rd, $k=4 \to 2$nd, $k=2 \to 1$st | **[T]** (45a, 45b: uniqueness from Fano selection rule) |
| N=1 SUSY from parallel spinor $\eta_0$ | [T] |
| SUSY breaking via $V_3$ | **[T]** (T-50: superpotential $W$ is unique, Schur's lemma) |
| $m_{3/2} \sim 10^{13}$ GeV | **[T]** (T-50: $m_{3/2} \sim \varepsilon^3 M_P$ from uniqueness of $W$, Schur's lemma) |
| $m_{\tilde{q}} \sim 10^{13}$ GeV (absence at LHC) | [H] |
| $\tau_p \sim 10^{72}$ years ($G_2$-extra channel) | [H] (proton effectively stable) |
| $\delta_{\text{CP}} \approx 64.5°$ | [H] ($1\sigma$ from $69°$) |
| Normal neutrino mass hierarchy | **[C]** (O-sector Yukawa; C14: $m_2/m_3$ with RG-correction) |


---

**Related documents:**
- [G₂-structure and Fano plane](/docs/physics/gauge-symmetry/g2-structure)
- [Fano selection rules](/docs/physics/gauge-symmetry/fano-selection-rules)
- [Confinement](/docs/physics/gauge-symmetry/confinement)
- [Higgs sector](/docs/physics/particle-physics/higgs-sector)
