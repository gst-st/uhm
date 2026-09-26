---
sidebar_position: 2
title: "Standard Model from G₂"
---

# Standard Model from G₂

:::info For whom this chapter is intended
Derivation of the Standard Model gauge group from $G_2 = \mathrm{Aut}(\mathbb{O})$. The reader will learn about the dual extraction strategy for $\mathrm{SU}(3)_C$ and the electroweak sector.
:::


## Overview

:::info[What the heading means]
$\mathrm{rank}(G_2) = 2 < \mathrm{rank}(\mathrm{SM}) = 4$, so the SM gauge group **is not a subgroup** of $G_2$. The page obtains it from $G_2$ **plus** constructions outside $G_2$; after the retraction of 2026-09-25 (the axis sets $\{A,S,D\}$, $\{L,E,U\}$ are not the $\mathbf 3$, $\bar{\mathbf 3}$ of $\mathrm{SU}(3)$, Theorem 1.1(a) below) the statuses are:
- $\mathrm{SU}(3)_C$ from $G_2$ as the stabilizer of the O-direction — **[T]** as mathematics ($\mathrm{Stab}_{G_2}(e_O)\cong\mathrm{SU}(3)$; prior art, Günaydın–Gürsey 1973); its reading as colour is **[I]**
- Electroweak sector $\mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$ from the Fano-electroweak construction (FE): the pair $(E,U)$ from $\kappa_0$ and the line $\{A,E,U\}$ through it are **[T]** combinatorics; the group and its uniqueness are **[C at (FE)]**, where (FE) is the assumption that the electroweak group acts on $\mathrm{span}\{L,E,U\}$ of the Page–Wootters system factor — an input that the retracted split "$\bar{\mathbf 3}=\{L,E,U\}$" used to supply
- Full correspondence "SM from $G_2$ + (FE)" — **[C]** (electroweak dynamics is conditional)
- **Corrected route (2026-09-25, [§2.5](#sm-из-клиффорда)):** on $\mathbb{C}\otimes\mathbb{O}$ — UHM's Hilbert space plus the parallel spinor — the octonionic Clifford system is forced and generates $\mathfrak{spin}(9)$. The centraliser of colour in it is $\mathfrak{u}(2)$, and the whole group is $(\mathrm{SU}(3)\times\mathrm{SU}(2)\times\mathrm{U}(1))/\mathbb{Z}_6$ with hypercharges $\tfrac16$ and $-\tfrac12$ on the left-handed doublets. This is **[T]** as mathematics (T-326; prior art Todorov–Dubois-Violette 2018, Krasnov 2021) and **[C at (Cl)]** as a result of UHM. Chirality of the doublets: T-327. Families must be horizontal: T-328. The complexified spinor carries a forced tenth generator and one complete, anomaly-free generation with $\nu_R$; in it the $\mathrm{SU}(2)$ of T-326 is the diagonal of $\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$, and $B-L$ returns: T-329 ([§2.6](#поколение-t329))
:::

The central task is the derivation of the Standard Model gauge group $\mathrm{SU}(3)_C \times \mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$ from $G_2 = \mathrm{Aut}(\mathbb{O})$. The strategy is dual: $\mathrm{SU}(3)_C$ is extracted from the stabilizer of the O-direction in $G_2$, while the electroweak sector $\mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$ comes from the Fano-electroweak construction (FE) on the pair $(E,U)$ and the Higgs line $\{A,E,U\}$. (The former phrase "the Higgs line canonically decomposes $\bar{3} \to \{E,U\} \oplus \{L\}$" is retracted [✗]: $\{L,E,U\}$ is not the $\bar{\mathbf 3}$.)

:::tip[Status: \[T\] for SU(3)\_C]
$\mathrm{SU}(3)_C$ from $G_2$ is a standard mathematical fact.
:::

:::tip[Status: \[T\] for the combinatorics of the electroweak sector; the group is \[C at (FE)\]]
The formula $\kappa_0$ [T] categorically singles out the **unique** pair $(E,U)$ via $\mathrm{Hom}(O,E)$ and $\mathrm{Hom}(O,U)$, and the only Fano line through $E$ and $U$ is $\{A,E,U\}$ — both [T]. That these data determine $\mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$ is [C at (FE)]; the step "the Higgs line canonically decomposes $\bar{3} \to \{E,U\} \oplus \{L\}$" that used to carry it is retracted [✗]. Proof and its status: [sect. 2.3a](#теорема-единственности-фэ).
:::

<a id="электрослабое-разграничение"></a>

:::warning Distinction between [T] and [C] in the electroweak sector
Two levels of results must be clearly separated:

- **[T] (proven):** combinatorial uniqueness of the pair $(E,U)$ from $\kappa_0$, uniqueness of the Higgs line $\{A,E,U\}$. The "canonical decomposition $\bar{3} \to 2_{EU} \oplus 1_L$" listed here before is retracted [✗]
- **[C] (conditional):** full dynamical gauge structure $\mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$ with correct running of coupling constants — depends on dynamical content (Gap potential, RG equations) going beyond pure combinatorics
- **Free parameter:** the hypercharge generator $Y$ contains the parameter $\alpha$ (relative weight of baryon number and weak isospin within $\bar{3}$), whose value is not fixed by the Fano structure and requires an additional condition (e.g., from anomaly freedom or phenomenology)
:::

---

## 1. Anatomy of $G_2$ and the Rank Problem

### 1.1 Setup

**Fundamental obstacle.** $\mathrm{rank}(G_2) = 2$, while $\mathrm{rank}(\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)) = 2 + 1 + 1 = 4$. Consequently, the SM group **is not a subgroup** of $G_2$.

**Strategy.** Overcome the obstacle through two mechanisms:
- (A) $\mathrm{SU}(3)_C$ from the stabilizer of the O-direction in $G_2$ — **[T]** (structural symmetry, rank $2 \to$ rank 2)
- (B) $\mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$ from the Fano-electroweak construction (FE) on the Page–Wootters system factor — **[C at (FE)]** (the pair $(E,U)$ from $\kappa_0$ is [T]; adds rank 2 in the 42D PW extension). The former "the Higgs line canonically decomposes $\bar{3} \to \{E,U\} \oplus \{L\}$ — [T]" is retracted [✗]. In the Clifford frame of [§2.5–§2.6](#sm-из-клиффорда) (FE) is replaced by (Cl₀) — fermions are vectors of the spinor module — and the electroweak group follows as [C at (Cl)] (T-326, T-329); (FE) is carried only by the axis-frame construction kept on this page ([Premises of UHM](/docs/reference/premises#гипотезы-отождествления)).

### 1.2 Theorem 1.1 (Decomposition of $G_2$-generators under $\mathrm{SU}(3)$)

:::tip[Status: Theorem \[T\]]
The maximal embedding $\mathrm{SU}(3) \subset G_2$ (stabilizer of a vector in $\mathrm{Im}(\mathbb{O}) \cong \mathbb{R}^7$) determines the decomposition.
:::

**(a)** Representation **7** (fundamental). Over $\mathbb{R}$: $\mathbf 7\to\mathbf 1\oplus\mathbf 6$, with $\mathbf 6$ irreducible of complex type (the complex structure is left multiplication by $e_O$, which pairs $A\leftrightarrow D$, $S\leftrightarrow U$, $L\leftrightarrow E$). Over $\mathbb{C}$ **[T]**:

$$7 \to 1_O \oplus \mathbf 3 \oplus \bar{\mathbf 3},\qquad \mathbf 3=\mathrm{span}_{\mathbb C}\{A-iD,\ S-iU,\ L-iE\},\quad \bar{\mathbf 3}=\overline{\mathbf 3}.$$

The earlier labels $3_{ASD}=\{A,S,D\}$ ("spatial triplet") and $\bar{3}_{LEU}=\{L,E,U\}$ ("Gap triplet") are **retracted [✗]** (2026-09-25): none of the 20 triples of non-$O$ axes spans an $\mathrm{SU}(3)$-invariant subspace (`test_no_axis_triple_is_su3_invariant` in `website/scripts/check_core_numbers.py`). Prior art for the split and its colour reading: Günaydın and Gürsey 1973 ([G₂-structure, §2.6](/docs/physics/gauge-symmetry/g2-structure#прецеденты-g2)). No axis is spatial. Spatial directions whose rotations commute with this $\mathrm{SU}(3)$ exist only outside $\mathrm{Im}\,\mathbb O$: they form the colour-singlet part $\mathfrak h_2(\mathbb C_O)$ of $\mathfrak h_2(\mathbb O)$ ([Spacetime, Theorem 48c](/docs/core/foundations/spacetime#теорема-48c), [T] as mathematics, [C at (Q)] as spacetime).

**(b)** Adjoint representation **14** (algebra $\mathfrak{g}_2$):

$$14 \to 8 \oplus 3 \oplus \bar{3}$$

where $8$ is the adjoint representation of $\mathrm{SU}(3)$ (generators of $\mathrm{SU}(3)$), $3$ and $\bar{3}$ are fundamental representations.

**(c)** — **retracted [✗] as an assignment of axis pairs.** The multiplicities are right: over $\mathbb{C}$, $\Lambda^2(\mathbf 1\oplus\mathbf 3\oplus\bar{\mathbf 3})=\mathbf 8\oplus\mathbf 1\oplus2\cdot\mathbf 3\oplus2\cdot\bar{\mathbf 3}$ (21 dimensions). But the pair sets in the table below are not the invariant subspaces — an $\mathrm{SU}(3)$-invariant $7\times7$ matrix has off-diagonal entries only on $(A,D)$, $(S,U)$, $(L,E)$ (`test_su3_invariant_states_are_coherent_only_on_o_line_pairs`). Record of the retracted table:

| Sector | Pairs | Number | $\mathrm{SU}(3)$-representation |
|---|---|---|---|
| O-to-3 | $\{A\text{-}O, S\text{-}O, D\text{-}O\}$ | 3 | $3$ |
| O-to-$\bar{3}$ | $\{L\text{-}O, E\text{-}O, U\text{-}O\}$ | 3 | $\bar{3}$ |
| 3-to-3 | $\{A\text{-}S, A\text{-}D, S\text{-}D\}$ | 3 | $\bar{3}$ ($\wedge^2 3$) |
| $\bar{3}$-to-$\bar{3}$ | $\{L\text{-}E, L\text{-}U, E\text{-}U\}$ | 3 | $3$ ($\wedge^2 \bar{3}$) |
| **3-to-$\bar{3}$** | **$\{A\text{-}L, A\text{-}E, A\text{-}U, S\text{-}L, S\text{-}E, S\text{-}U, D\text{-}L, D\text{-}E, D\text{-}U\}$** | **9** | **$8 \oplus 1$** |

**(d)** ~~The 3-to-$\bar{3}$ sector contains the **adjoint representation of $\mathrm{SU}(3)$** (8 generators) plus the **$\mathrm{SU}(3)$-singlet** (1 generator).~~ Retracted [✗] with (c): the nine pairs $\{A,S,D\}\times\{L,E,U\}$ do not span $\mathbf 8\oplus\mathbf 1$. What holds is (b): the eight generators of $\mathfrak{su}(3)$ — the number of gluons in QCD.

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

:::danger Items (a)–(c) retracted [✗] (2026-09-25)
They identified the eight generators of $\mathrm{SU}(3)_C$ with coherences of the nine pairs $\{A,S,D\}\times\{L,E,U\}$ and read unbroken colour off an equal Gap on those pairs. Both rest on the retracted labels of Theorem 1.1(a). The generators of $\mathfrak{su}(3)\subset\mathfrak{g}_2\subset\mathfrak{so}(7)$ are real antisymmetric $7\times7$ matrices acting on all six non-$O$ axes (its Cartan subalgebra rotates the planes $(A,D)$, $(S,U)$, $(L,E)$ with angles summing to zero). An $\mathrm{SU}(3)_C$-invariant $\Gamma$ has off-diagonal entries only on $(A,D)$, $(S,U)$, $(L,E)$ (`test_su3_invariant_states_are_coherent_only_on_o_line_pairs`); a vacuum with non-zero coherence on the nine pairs, equal Gap or not, therefore breaks $\mathrm{SU}(3)_C$ instead of exhibiting it. Unbroken colour is thus not derived on this page; what vacuum is compatible with it is an open problem [Pr].
:::

**(a)** ~~8 generators of $\mathrm{SU}(3)_C$ = 8 coherences of the 3-to-$\bar{3}$ sector (after subtracting the singlet): $T_a^{(\mathrm{color})} \in \{A\text{-}L, A\text{-}E, A\text{-}U, S\text{-}L, S\text{-}E, S\text{-}U, D\text{-}L, D\text{-}E, D\text{-}U\}_{\mathrm{traceless}}$~~ — retracted [✗].

**(b)** ~~"Gluon field" — fluctuations of the 8 Gap phases $\theta_{ij}$ in the 3-to-$\bar{3}$ sector around the vacuum value, $A_\mu^a(x) \sim \partial_\mu \theta_{ij}^{(a)}(x)$~~ — retracted [✗] with (a).

**(c)** ~~$\mathrm{SU}(3)_C$ is an exact symmetry, because the Gap vacuum is isotropic in the 3-to-$\bar{3}$ sector, $\mathrm{Gap}(A,L) = \cdots = \mathrm{Gap}(D,U)$~~ — retracted [✗]: equal Gap on axis pairs is not $\mathrm{SU}(3)$-invariance (box above).

**Justification of the identification.** Of all possible candidates for $\mathrm{SU}(3)$ (stabilizers of $A, S, \ldots, U$), O is the only one for which:
- (i) The stabilizer has a physical meaning (choice of the "clock" subsystem)
- (ii) The remaining $\mathrm{SU}(3)$ acts on the six axes other than $O$, as on one copy of $\mathbb{C}^3$ (not separately on "spatial" and "Gap" sectors — Theorem 1.1(a))
- (iii) $G_2$-invariance of the Lagrangian guarantees conservation of $\mathrm{SU}(3)_C$ charges (8 of the 14 $G_2$-charges)

---

## 2. Electroweak Sector from the Fano-Electroweak Construction (FE) {#электрослабый-сектор-фэ}

### 2.1 The Rank Problem and Its Solution {#проблема-ранга}

**Problem.** $\mathrm{rank}(\mathrm{SU}(2)_L \times \mathrm{U}(1)_Y) = 2$, but after extracting $\mathrm{SU}(3) \subset G_2$ (rank 2) no rank remains for the electroweak sector — $G_2$ is already "exhausted."

**Solution through two mechanisms:**

| Mechanism | Source | Result | Status |
|---|---|---|---|
| $G_2 \to \mathrm{SU}(3)_C$ | Stabilizer of the O-direction | rank 2 — strong interaction | **[T]** |
| Fano-electroweak construction (FE) | Higgs line $\{A,E,U\}$ | rank 2 — electroweak interaction | **[C at (FE)]** (the combinatorics of $(E,U)$ is [T]; dynamics [C]) |

**Analysis in 7D — retracted [✗] and replaced.** The former analysis read $\bar{3} = \{L,E,U\}$ as the anti-triplet, took $\lvert E\rangle\langle E\rvert - \lvert U\rangle\langle U\rvert$ for one of its Cartan generators and concluded that in 7D $\mathrm{SU}(2)_L$ is a subgroup of "$\mathrm{SU}(3)_{\bar{3}}$". Both premises are false: the anti-triplet is spanned by $A+iD$, $S+iU$, $L+iE$, and the generators of $\mathrm{SU}(3)\subset G_2\subset\mathrm{SO}(7)$ are real antisymmetric matrices, which a real diagonal matrix is not. What is true in 7D: the $\mathrm{SU}(2)$ generated by $T_{1,2,3}$ on $\mathrm{span}\{E,U\}$ does **not** commute with $\mathrm{SU}(3)_C$ (numerically $\max_a\|[T_a,X]\|=3.6$ over a basis $X$ of $\mathfrak{su}(3)$), and Schur's lemma gives the centraliser of $\mathrm{SU}(3)_C$ in $\mathrm{U}(7)$ as $\mathrm{U}(1)^3$ (dimension 3, checked) — it contains no $\mathrm{SU}(2)$ at all. In 7D the electroweak group of (FE) and the colour group therefore cannot coexist as commuting factors.

**Resolution in 42D:** In the Page–Wootters extension (Axiom A5):

$$\mathcal{H}_{\mathrm{total}} = \mathcal{H}_O \otimes \mathcal{H}_{6D} = \mathbb{C}^7 \otimes \mathbb{C}^6 = \mathbb{C}^{42}$$

$\mathrm{SU}(3)_C$ (from $G_2$ on the clock factor) and $\mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$ (from (FE) on the system factor) act on **different** tensor factors, so they commute and ranks add: $2 + 2 = 4 = \mathrm{rank}(\mathrm{SM})$. Status: **[C at (FE)]** under Axiom A5 (Page–Wootters). The commutation itself is trivial here — any two groups on different tensor factors commute — and it is the only sense in which the two groups commute; in 7D they do not (above).

:::warning Bimodule construction — retracted as a derivation [✗] (2026-09-25)
This box said "Resolved [T]": SM representations $(3,2)_{1/6}$ arise **not** from the tensor product $\mathbb{C}^7 \otimes \mathbb{C}^6$ but from the **bimodule decomposition** of $H_F$ via the real structure $J$ (KO-dim 6) — left action of $\mathbb{H}$ for weak isospin, right action of $M_3(\mathbb{C})^\circ$ for colour ([Bimodule construction, T-178](/docs/proofs/physics/bimodule-construction#бимодульная-конструкция); the box cited it as "T-176"). The mechanism is Connes's, and it works for his $A_F$ acting on his $H_F$ (96 states for three generations). It is not derived from the UHM triple: $H_{\text{int}}=\mathbb{C}^7$ cannot carry the 16 states of one generation, the passage $A_{\text{int}}\to A_F$ leaned on the Morita claim T-175a (retracted), and $J$ = complex conjugation does not have KO-dimension 6 ([spacetime, Step 6](/docs/core/foundations/spacetime#теорема-спектральная-тройка)). Status of the representation content in UHM: imported, not derived.
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

**Classification with respect to the axis sets $\{O\}$, $\{A,S,D\}$, $\{L,E,U\}$** (incidence combinatorics only: these sets are not the $\mathrm{SU}(3)$ sectors, Theorem 1.1(a); below, "3" and "$\bar 3$" name the two axis sets):

| Type | Fano lines | Number | Characteristic |
|-----|-----------|-------|----------------|
| O-lines | $\{L,E,O\}$, $\{U,O,S\}$, $\{O,A,D\}$ | 3 | Pass through O |
| Mixed | $\{A,S,L\}$, $\{S,D,E\}$, $\{A,E,U\}$ | 3 | Contain elements from both 3 and $\bar{3}$, do not pass through O |
| $\bar{3}$-anchored | $\{D,L,U\}$ | 1 | Two points in $\bar{3}$ ($L,U$), one in $3$ ($D$) |

:::note Symmetry of 3 and 3̄ [T]
**No** Fano line lies entirely within $3 = \{A,S,D\}=\{1,2,3\}$ **nor** within $\bar{3} = \{L,E,U\}=\{4,5,6\}$: neither $\{1,2,3\}$ nor $\{4,5,6\}$ is a Fano line. The four non-O lines each meet **both** sectors — e.g. $\{D,L,U\}=\{3,4,6\}$ has $D\in 3$ and $L,U\in\bar 3$. In particular $\{D,L,U\}$ is **not** entirely within $\bar 3$ (since $D\in 3$). The $3$/$\bar 3$ split is therefore symmetric at the incidence level; sector asymmetry enters only dynamically (via the O-sector coupling), not combinatorially.
:::

### 2.3 Theorem 2.1 (Fano-Electroweak Construction) {#теорема-фэ}

:::tip[Status: \[C at (FE)\]; the pair $(E,U)$ and the Higgs line are \[T\]]
The Higgs line $\{A,E,U\}$ and the pair $(E,U)$ singled out by the formula $\kappa_0$ [T] define the electroweak gauge symmetry $\mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$ **given (FE)**: the electroweak group acts on $\mathrm{span}\{L,E,U\}$ of the Page–Wootters system factor. Until 2026-09-25 this box said "Theorem [T]", with (FE) supplied by reading $\{L,E,U\}$ as the $\bar{\mathbf 3}$ of $\mathrm{SU}(3)$; that reading is retracted (Theorem 1.1(a)). See [sect. 2.3a](#теорема-единственности-фэ).
:::

**Fano-electroweak construction (FE).** *Given (FE), the split of $\mathrm{span}\{L,E,U\}$ into $\mathrm{span}\{E,U\}\oplus\mathrm{span}\{L\}$, singled out by the Higgs line $\{A,E,U\}$, carries the effective gauge symmetry of the electroweak sector [C at (FE)].* The former wording, "the canonical decomposition $\bar{3} \to 2_{EU} \oplus 1_L$ … determines the **unique** effective gauge symmetry [T]", is retracted [✗].

**(a)** ~~The antifundamental triplet $\bar{3}_{LEU} = \{L, E, U\}$ decomposes along the Higgs line, $\bar{3}_{LEU} \to 2_{EU} \oplus 1_L$~~ — retracted [✗]: $\{L,E,U\}$ is not the antifundamental triplet. What remains [T]: the pair $\{E,U\}$ is singled out by $\kappa_0$ and lies on exactly one Fano line, $\{A,E,U\}$ (sect. 9.2). The split $\mathrm{span}\{L,E,U\}=\mathrm{span}\{E,U\}\oplus\mathrm{span}\{L\}$ into a doublet $2_{EU}$ and a singlet $1_L$ is then a definition [D] on the system factor.

**(b)** Gauge structure with explicit generators:

$\mathrm{SU}(2)_L$ — 3 generators (rotations in the $\{E,U\}$-subspace):

$$
T_1 = \frac{1}{2}(\lvert E\rangle\langle U\rvert + \lvert U\rangle\langle E\rvert), \quad T_2 = \frac{1}{2i}(\lvert E\rangle\langle U\rvert - \lvert U\rangle\langle E\rvert), \quad T_3 = \frac{1}{2}(\lvert E\rangle\langle E\rvert - \lvert U\rangle\langle U\rvert)
$$

$\mathrm{U}(1)_Y$ — 1 generator (weak hypercharge):

$$
Y = \frac{1}{3}\left(\sum_{i \in 3} \lvert i\rangle\langle i\rvert - \sum_{j \in \bar{3}} \lvert j\rangle\langle j\rvert\right) + \alpha\left(\lvert L\rangle\langle L\rvert - \frac{1}{2}(\lvert E\rangle\langle E\rvert + \lvert U\rangle\langle U\rvert)\right)
$$

where the first term is an analogue of baryon number (it distinguishes the axis sets $\{A,S,D\}$ and $\{L,E,U\}$ named "3" and "$\bar{3}$"), the second is weak isospin within $\{L,E,U\}$ (distinguishes $1_L$ and $2_{EU}$). Total: 4 generators = $\dim(\mathrm{SU}(2) \times \mathrm{U}(1))$. Note that in 7D the first term does not commute with $\mathrm{SU}(3)_C$: the only $\mathfrak{u}(1)$ in $\mathfrak{so}(7)$ commuting with $\mathfrak{su}(3)$ is generated by the cross product $x\mapsto e_O\times x$ (left multiplication by $e_O$ on the six axes orthogonal to it), which is not diagonal in the axes and does not lie in $\mathfrak{g}_2$ (the centraliser of $\mathfrak{su}(3)$ in $\mathfrak{g}_2$ is zero). A hypercharge that separates $\mathbf 3$ from $\bar{\mathbf 3}$ is therefore outside $G_2$.

:::warning Unfixed parameter α
The parameter α in the hypercharge generator Y is **not fixed** by the Fano structure. The uniqueness of the gauge group SU(3)×SU(2)×U(1) is [C at (FE)] (it was stated as [T] until 2026-09-25); the uniqueness of the hypercharge embedding is [C, upon fixing α from anomaly freedom or phenomenology].
:::

**(c)** Advantage over the SU(6)-construction:

| Criterion | Old approach [H] (SU(6)) | (FE)-construction [C at (FE)] |
|----------|--------------------------|--------------------------|
| Number of hypotheses | $\geq 3$ (SU(6), SU(5)-embedding, GJ-decomposition) | 1: (FE) (the pair $(E,U)$ itself is derived from $\kappa_0$ [T]) |
| Use of Fano | Minimal | Central (Higgs line) |
| SU(3) consistency | Requires a separate theorem | Not automatic: in 7D the SU(2) on $\mathrm{span}\{E,U\}$ does not commute with $\mathrm{SU}(3)_C$; they commute only on different PW tensor factors (Theorem 2.2 retracted) |
| Predictive power | X,Y-leptoquarks (not observed) | Yukawa hierarchy (consistent) |
| Economy | 35 generators of SU(6) | 12 generators of SM |
| Status | [H] | **[C at (FE)]** (was "[T] — uniqueness theorem" until 2026-09-25) |

### 2.3a Uniqueness Theorem for the Electroweak Construction {#теорема-единственности-фэ}

:::tip[Status: construction \[C at (FE)\]; uniqueness \[H\] in the axis picture, \[C at (Cl)\] through T-326; identification \[I\]]
The SM gauge group $G_{\mathrm{SM}} = \mathrm{SU}(3)_C \times \mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$ is claimed to be the **unique** rank-4 gauge group compatible with the Fano-plane structure and $G_2$-symmetry. Status since 2026-09-25: the axis construction below is [C at (FE)]; its uniqueness is [H] — Step 3 is not a classification (see there), and no uniqueness theorem for $\mathrm{SU}(2)\times\mathrm{U}(1)$ exists in the literature; the former status "[T]+[I]" is retracted [✗]. Through the Clifford system of $\mathbb{C}\otimes\mathbb{O}$ ([§2.5](#sm-из-клиффорда), T-326) the uniqueness holds as a theorem of the construction, [C at (Cl)]: the electroweak algebra is the centraliser of colour in $\mathfrak{spin}(9)$, which admits no alternative.

#### Corollary: rank-4 prohibition — no Z′, no fifth force [H] (T-297) {#запрет-z-прайм}

The former text: uniqueness of $G_{\mathrm{SM}}$ as the **rank-4** group compatible with Fano + $G_2$ forbids every gauge extension of higher rank: any extra gauge $\mathrm{U}(1)$ — a $Z'$, gauged $B{-}L$, a gauged "dark photon" — would raise the rank to 5, and no rank-5 subgroup fits the incidence structure, so collider and dark-sector searches for a *gauge* $Z'$ remain empty "at any energy". Downgraded to **[H]** (2026-09-25): the uniqueness it rests on is [H] (above), and the octonionic routes that do derive Standard Model structure end with an extra $\mathrm{U}(1)$ — Furey and Hughes obtain "Standard model + $B-L$" from their division-algebraic symmetry breaking (*Phys. Lett. B* **831**, 137186 (2022), [arXiv:2210.10126](https://arxiv.org/abs/2210.10126)), and Boyle a left–right symmetric extension (*J. Math. Phys.* **67**, 071701 (2026), [arXiv:2006.16265](https://arxiv.org/abs/2006.16265)). A gauged $B-L$ broken near the corpus's own seesaw scale $M_R\sim3\times10^{14}$ GeV would give a $Z'$ far beyond any collider, which the corpus does not exclude; "empty searches" would then not test the claim. Defensible form [H]: the (FE) construction contains no extra gauge $\mathrm{U}(1)$; a gauge $Z'$ found within collider reach would contradict (FE). (Notation guard: the quantity $Z'_\Phi(-2)$ of the [$\Lambda$-budget](/docs/proofs/gap/lambda-budget) is the *derivative of an Epstein zeta regulator*, not a boson.)

**What the Clifford framework settles, and at which scale $B-L$ survives (T-329).** Under (Cl) of [§2.5](#sm-из-клиффорда) the question can be answered by computation. (i) In the doublet sector no $Z'$ exists [C at (Cl)]: the centraliser of $G_{\mathrm{SM}}$ in $\mathrm{Spin}(9)$ is $\mathrm{U}(1)_Y$ itself (dimension 1, checked), and no larger Clifford system exists on $\mathbb{C}\otimes\mathbb{O}$ (nine generators is the maximum on $\mathbb{R}^{16}$). (ii) The right-handed fields are not in $\mathbb{C}\otimes\mathbb{O}$. They live in its complexification $\mathbb{R}^{32}=(\mathbb{C}\otimes\mathbb{O})\otimes_{\mathbb{R}}\mathbb{C}'$, where a tenth generator is forced ([§2.6](#поколение-t329), Theorem 2.6(a)), and there the centraliser of colour in $\mathfrak{spin}(10)$ has dimension 7 with one-dimensional centre and six-dimensional derived algebra. It is $\mathfrak{su}(2)_L\oplus\mathfrak{su}(2)_R\oplus\mathfrak{u}(1)_{B-L}$, rank 5 with colour (`test_left_right_extension_brings_b_minus_l`). This is the left–right symmetric outcome of Boyle and the "Standard model + $B-L$" of Furey and Hughes, reached from the other side. So $B-L$ survives exactly when the singlets enter through the Clifford extension, and UHM does not fix its breaking scale. If the Majorana mass of $\nu_R$ comes from $B-L$ breaking with a coupling of order one, then $v_{B-L}\gtrsim M_R\approx3\times10^{14}$ GeV, the seesaw scale of the [neutrino page](/docs/physics/particle-physics/neutrino-masses#seesaw), and the $Z'_{B-L}$ weighs of order $10^{14}$ GeV — far beyond colliders. T-297 therefore stratifies: no $Z'$ in the doublet sector, [C at (Cl)]; no $Z'$ within collider reach, [C at (Cl)] plus $B-L$ breaking at the seesaw scale; no $Z'$ at any energy, [H] — a gauged $B-L$ at $\sim10^{14}$ GeV is the expected, not the excluded, outcome of the extension.

 The key element is the categorical uniqueness of the pair $(E,U)$ from the formula $\kappa_0$ [T]. Identification of the abstract generators with the physical SM gauge fields is **[I]** (an interpretive step).
:::

**Claim (Uniqueness of the electroweak construction) — [C at (FE)] for the construction, [H] for uniqueness.** Under axioms A1–A5 and (FE), the Standard Model gauge group
$$G_{\mathrm{SM}} = \mathrm{SU}(3)_C \times \mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$$
is the **unique** rank-4 gauge group compatible with the Fano-plane structure and $G_2$-symmetry.

#### Argument {#доказательство-единственности-фэ}

**Step 1. $\mathrm{SU}(3)_C$ from $G_2$ [T] (existing result).**

The stabilizer of the O-direction in the $G_2$-representation on $\mathbb{C}^7$ is $\mathrm{SU}(3)$ [T]. Under $G_2 \to \mathrm{SU}(3)$:
$$7 \to 3 \oplus \bar{3} \oplus 1$$
where $1 = O$ and $3=\mathrm{span}_{\mathbb C}\{A-iD,S-iU,L-iE\}$, $\bar 3$ its conjugate. (The former "$3 = \{A, S, D\}$, $\bar{3} = \{L, E, U\}$" is retracted [✗], Theorem 1.1(a).) Rank$(\mathrm{SU}(3)_C) = 2$, fully exhausting rank$(G_2)$.

**Step 2. Necessity of tensor extension [T].**

Rank$(G_{\mathrm{SM}}) = 4 > 2 =$ rank$(G_2)$. Consequently, $G_{\mathrm{SM}} \not\subset G_2$. The additional rank 2 can arise **only** from the Page–Wootters tensor extension (A5):
$$\mathcal{H} = \mathcal{H}_O \otimes \mathcal{H}_S = \mathbb{C}^7 \otimes \mathbb{C}^6$$
where $G_2$ acts on $\mathcal{H}_O$ (structural factor) and the electroweak group acts on $\mathcal{H}_S$ (system factor). Tensor independence guarantees commutativity:
$$[\mathrm{SU}(3)_C^{(\text{struct})}, G_{\mathrm{EW}}^{(\text{sys})}] = 0$$
and addition of ranks.

**Step 3. Possible gauge groups on $\mathrm{span}\{L,E,U\}$ — [C at (FE)], not a classification.**

On the system factor, the electroweak group $G_{\mathrm{EW}}$ acts on $\mathrm{span}\{L, E, U\} \cong \mathbb{C}^3$ — this is the assumption (FE); the former justification "$\bar{3} = \{L, E, U\}$" is retracted. Required rank $= 2$. The table lists some subgroups of $\mathrm{U}(3)$ of rank 2; it is not a classification — for instance $\mathrm{SO}(3)\times\mathrm{U}(1)$ also has rank 2 and acts on $\mathbb{C}^3$ irreducibly without any $2+1$ split:

| Subgroup | Rank | Fano-compatibility |
|-----------|:----:|:------------------:|
| $\mathrm{SU}(3)$ | 2 | Yes, but trivial (full $\bar{3}$-symmetry) |
| $\mathrm{SU}(2) \times \mathrm{U}(1)$ | 2 | **Requires** a 2+1 decomposition of $\bar{3}$ |
| $\mathrm{U}(1) \times \mathrm{U}(1)$ | 2 | Abelian — insufficient for the mass spectrum |
| $\mathrm{U}(2)$ | 2 | Isomorphic to $\mathrm{SU}(2) \times \mathrm{U}(1)$ up to center |

**Step 4. Uniqueness of the split $\{L,E,U\} \to 2 \oplus 1$ [T] given (FE) (key new element).**

Each split $\{L, E, U\} \to (2) \oplus (1)$ is defined by a distinguished **pair** in $\{L,E,U\}$. Pairs:

| Pair | Remainder | Fano line through the pair | Third point |
|------|---------|----------------------|-------------|
| $\{E, U\}$ | $\{L\}$ | $\{A, E, U\}$ | $A \in 3$ |
| $\{L, U\}$ | $\{E\}$ | $\{D, L, U\}$ | $D \in 3$ |
| $\{L, E\}$ | $\{U\}$ | $\{L, E, O\}$ | $O = 1$ |

Uniqueness criterion — **categorical compatibility with $\kappa_0$ [T]**.

The formula $\kappa_0 = \omega_0 \cdot |\gamma_{OE}| \cdot |\gamma_{OU}| / \gamma_{OO}$ [T] singles out **exactly the pair $(E, U)$** via the morphisms $\mathrm{Hom}(O, E)$ and $\mathrm{Hom}(O, U)$. This is the pair through which regeneration is carried out: $O$ (Ground) is connected to $E$ (Interiority) and $U$ (Unity) **functionally**, through the unique axiomatic formula. Substituting another pair:

- Pair $\{L, U\}$: no $\mathrm{Hom}(O, L)$ in $\kappa_0$ — $L$ is not categorically singled out
- Pair $\{L, E\}$: excludes $U$ from the doublet — destroys the normalization $\mathrm{Tr}(\Gamma) = 1$ (function of U)

Consequently, the split $\{L,E,U\} \to \{E, U\} \oplus \{L\}$ is **unique** among the three pairs.

**Step 5. Uniqueness of the Fano-Higgs line [T] (existing result).**

In PG(2,2), exactly one line passes through the points $E = 5$ and $U = 6$: $\{A, E, U\} = \{1, 5, 6\}$. $\blacksquare$

**Step 6. Uniqueness of $\mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$ [T].**

On the doublet $\{E, U\} \cong \mathbb{C}^2$:
- $\mathrm{SU}(2)_L$ is the unique (up to isomorphism) rank-1 group acting irreducibly on $\mathbb{C}^2$
- $\mathrm{U}(1)_Y$ is the unique (up to normalization) generator commuting with $\mathrm{SU}(2)_L$ and distinguishing the axis sets $\{A,S,D\}$ and $\{L,E,U\}$ (on the system factor; in 7D such a generator does not commute with $\mathrm{SU}(3)_C$, Theorem 2.1(b))

**Step 7. Result: rank = 4 [C at (FE)].**

$$\text{rank}(\mathrm{SU}(3)_C) + \text{rank}(\mathrm{SU}(2)_L) + \text{rank}(\mathrm{U}(1)_Y) = 2 + 1 + 1 = 4$$

~~Since at each step the choice is unique, an alternative rank-4 gauge group does not exist.~~ Retracted [✗]: Step 3 is not exhaustive and Step 1's labels are retracted; what follows is that, given (FE), this construction yields $G_{\mathrm{SM}}$ with rank 4 [C at (FE)]. Uniqueness among all rank-4 groups compatible with the axioms is [H]. $\blacksquare$

:::info[Key new element]
Step 4 — **categorical uniqueness of the pair $(E, U)$** from the formula $\kappa_0$ [T]. The formula $\kappa_0$ [T] contains **exactly** $|\gamma_{OE}|$ and $|\gamma_{OU}|$ — this is not a free parameter, but a consequence of the adjunction $\mathcal{D} \dashv \mathcal{R}$ [T]. The pair is derived; the three-dimensional space on which the electroweak group acts is not. That input, (FE), was treated as a separate hypothesis before, was then taken as derived through "$\bar{\mathbf 3}=\{L,E,U\}$", and is a named assumption again since the retraction of 2026-09-25.
:::

### 2.4 Theorem 2.2 (Consistency of the Two $\mathrm{SU}(3)$'s) — retracted [✗] {#согласование-su3}

:::danger[Status: Retracted \[✗\] (2026-09-25)]
The theorem claimed that the two routes to $\mathrm{SU}(3)_C$ — through $G_2$ (sect. 1.3) and through the 42D tensor structure (sect. 2.1) — yield **the same** subgroup, and that it commutes with $\mathrm{SU}(2)_L\times\mathrm{U}(1)_Y$. Its proof (b) identified the triplet with the axes $\{A,S,D\}$, and (c) derived the commutation from $\{A,S,D\} \cap \{E,U,L\} = \varnothing$. Both fail. $\mathrm{SU}(3)_C$ acts on all six non-$O$ axes at once — $7\to1\oplus\mathbf 3\oplus\bar{\mathbf 3}$ is a complex split with no axis in either summand — and Schur's lemma makes its centraliser in $\mathrm U(7)$ equal to $\mathrm U(1)^3$ (dimension 3, checked), which contains no $\mathrm{SU}(2)$: in 7D the two groups do not commute ($\max_a\|[T_a,X]\|=3.6$, sect. 2.1). In the 42D Page–Wootters extension, $\mathrm{SU}(3)_C$ on the clock factor commutes with any group on the system factor for the trivial reason of tensor independence; nothing more is claimed.
:::

*Record of the retracted theorem (reason in the box above).*

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

### 2.5 The Standard Model group from the Clifford system of $\mathbb{C}\otimes\mathbb{O}$ (T-326) {#sm-из-клиффорда}

:::tip[Status: Theorem 2.5 is \[T\] as mathematics; as a result of UHM it is \[C at (Cl)\]]
Sections 2.1–2.4 obtain the electroweak group by placing it on axes it cannot share with colour. This section obtains the whole group $(\mathrm{SU}(3)\times\mathrm{SU}(2)\times\mathrm{U}(1))/\mathbb{Z}_6$ with its hypercharges from one structure that UHM already contains: octonion multiplication on the seven axes and the complex numbers of quantum mechanics. The price is one named assumption, (Cl), stated below. Given (Cl), the electroweak group is not chosen: it is the centraliser of colour. It acts on the left-handed doublets. In the complete generation of [§2.6](#поколение-t329) its $\mathrm{SU}(2)$ is the diagonal of $\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$ and its $\mathrm{U}(1)$ is $(B-L)/2$; on the left half they act as $\mathrm{SU}(2)_L$ and $Y$. Registry row T-326; numbers in `website/scripts/check_core_numbers.py`.
:::

**The space.** The octonions sit on the seven axes (T15 [T] with the canonical orientation of the Fano lines — [T15-canon](/docs/proofs/minimality/theorem-octonionic-derivation#каноническая-ориентация); the input (Alt), named here at first, is discharged by it) with the clock unit $e_O$. The spinor module of the Clifford algebra of $\mathrm{Im}\,\mathbb{O}$ is $\mathbb{O}$ itself, with generators $\Gamma_i = L_{e_i}$ (§4.1) and the $G_2$-invariant spinor $\eta_0 = 1$ (§4.2). Quantum mechanics complexifies it:
$$\mathcal{S} := \mathbb{C}\otimes\mathbb{O} = \mathbb{C}\,\eta_0 \oplus \mathcal{H},\qquad \mathcal{H} = \mathbb{C}\otimes\mathrm{Im}\,\mathbb{O} = \mathbb{C}^7 .$$
So $\mathcal{S}$ is UHM's Hilbert space plus the line of the parallel spinor. It is read below as a real space $\mathbb{R}^{16}$, with complex conjugation $J$ as its real structure.

**Assumption (Cl).** *The internal gauge transformations of fermions are the elements of the spin group of the Clifford system generated on $\mathcal{S}$ by the octonionic structure maps. The clock breaks this group to its largest connected subgroup in which colour, $\mathrm{SU}(3)_C=\mathrm{Stab}_{G_2}(e_O)$, is a normal factor.* (Cl) replaces (FE). It says where fermions live and which group acts on them; it names no axis triple. UHM's axioms do not state it — that fermions are spinors of $\mathrm{Im}\,\mathbb{O}$ is an input. *Update (T-329):* the second sentence is a theorem — the clock's stabiliser, the rule that gives colour in $G_2$ ([§2.6](#поколение-t329)). The first sentence, (Cl₀), is what remains, and it is shown there to be independent of the axioms about $\Gamma$.

**Theorem 2.5 (T-326).**

**(a) The Clifford system is forced and maximal [T].** The nine operators
$$\gamma_k = i L_{e_k}\ (k=1,\dots,7),\qquad \gamma_8 = J,\qquad \gamma_9 = iJ$$
satisfy $\gamma_a\gamma_b+\gamma_b\gamma_a = 2\delta_{ab}$ on $\mathcal{S}\cong\mathbb{R}^{16}$. The last two are not a choice: the operators that anticommute with all seven $iL_{e_k}$ form exactly the two-dimensional space $\mathrm{span}\{J, iJ\}$. No tenth such operator exists on $\mathbb{R}^{16}$. The products $\gamma_a\gamma_b/2$ span $\mathfrak{spin}(9)$ (dimension 36), and $\mathfrak{g}_2\subset\mathfrak{spin}(7)\subset\mathfrak{spin}(9)$.

**(b) The electroweak algebra is the centraliser of colour [T].** In $\mathfrak{spin}(9)$ the centraliser of $\mathfrak{su}(3)_C$ is $\mathfrak{u}(2)=\mathfrak{su}(2)\oplus\mathfrak{u}(1)$: dimension 4, centre of dimension 1, derived algebra of dimension 3. The normaliser of $\mathfrak{su}(3)_C$ is $\mathfrak{su}(3)\oplus\mathfrak{su}(2)\oplus\mathfrak{u}(1)$, of dimension 12. It coincides with the centraliser of right multiplication $R_{e_O}$ — Krasnov's characterisation, reached here from colour. The centraliser of the whole 12-dimensional algebra in $\mathfrak{spin}(9)$ is one $\mathfrak{u}(1)$, the hypercharge.

**(c) The global group is $(\mathrm{SU}(3)\times\mathrm{SU}(2)\times\mathrm{U}(1))/\mathbb{Z}_6$ [T].** Parametrise $\mathrm{U}(1)$ by the charge $6Y$ with period $2\pi$. Among the 72 central triples $(\omega^a, \pm1, e^{i\pi n/6})$, $a\in\{0,1,2\}$, $n\in\{0,\dots,11\}$, exactly six act trivially on $\mathcal{S}$. They form the $\mathbb{Z}_6$ generated by $(e^{2\pi i/3}, -1, e^{i\pi/3})$.

**(d) The representation [T].** Take the complex structure $\mathcal{J}=L_{e_O}$ (T-327, §4.4). Then
$$(\mathcal{S},\mathcal{J}) \cong (\mathbf 3,\mathbf 2)_{1/6}\oplus(\mathbf 1,\mathbf 2)_{-1/2},$$
the left-handed quark doublet and lepton doublet of one generation. The electric charges $Q=T_3+Y$ are $\tfrac23$ (three states), $-\tfrac13$ (three), $0$ and $-1$. The lepton doublet lies on the complex line $\mathbb{C}_{e_O}=\mathrm{span}\{\eta_0, e_O\}$. The quark doublet lies on the six axes orthogonal to it — the colour $\mathbb{C}^3$ of Theorem 1.1(a). The ratio $Y_Q:Y_L = 1:(-3)$ comes out; it is not put in. The sixteen real dimensions carry the isospin index, not the Lorentz spinor index: a Weyl field valued in $\mathcal{S}$ is $\mathbb{C}_O^2\otimes_{\mathbb{C}}\mathcal{S}_{\mathbb{C}}$, with the Weyl index a separate factor ([Spacetime, Theorem 48e](/docs/core/foundations/spacetime#теорема-48e)(d)–(e); 48d(e)).

**Proof.** (a) The relations are direct computation. For the extension: $\mathrm{Cl}_{7,0}$ acts on $\mathcal{S}=\mathbb{C}^8$ as $M_8(\mathbb{C})$, and its volume element is $\gamma_1\cdots\gamma_7 = i$ (checked). If $T$ anticommutes with all $\gamma_k$, then $J^{-1}T$ commutes with them. It therefore lies in their commutant $\mathrm{span}\{1, i\}$, so $T\in\mathrm{span}\{J, Ji\}$. The real Clifford algebra of nine generators squaring to $+1$ is $M_{16}(\mathbb{R})\oplus M_{16}(\mathbb{R})$, and that of ten is $M_{32}(\mathbb{R})$ (the periodicity table: Lawson and Michelsohn, *Spin Geometry*, Princeton 1989, ch. I §4). Its irreducible modules therefore have real dimensions 16 and 32, and nine is the maximum on $\mathbb{R}^{16}$.

(b) $\mathrm{SU}(3)_C$ acts on the complexified octonions by automorphisms that fix $\eta_0$ and $e_O$ and commute with $J$ and $i$. So $\mathbb{R}^9=\mathrm{span}\{\gamma_a\}$ splits as $\mathbb{R}^6\oplus\mathbb{R}^3$, with $\mathbb{R}^6=\mathrm{span}\{\gamma_k : e_k\perp e_O\}\cong\mathbf 3\oplus\bar{\mathbf 3}$ and $\mathbb{R}^3=\mathrm{span}\{\gamma_O, J, iJ\}$ trivial. Then $\mathfrak{so}(9)=\mathfrak{so}(6)\oplus\mathfrak{so}(3)\oplus(\mathbb{R}^6\otimes\mathbb{R}^3)$. Under $\mathfrak{su}(3)$ the singlets are one $\mathfrak{u}(1)\subset\mathfrak{so}(6)$ (the complex structure of $\mathbb{R}^6$, i.e. $L_{e_O}$ on $e_O^\perp$) and all of $\mathfrak{so}(3)$, while $\mathbb{R}^6\otimes\mathbb{R}^3$ is three copies of $\mathbf 3\oplus\bar{\mathbf 3}$. This gives dimension 4. Since $\mathfrak{su}(3)$ is semisimple, its normaliser is $\mathfrak{su}(3)\oplus\mathfrak{c}(\mathfrak{su}(3))$, dimension 12. The coincidence with $\mathfrak{c}(R_{e_O})$ and the one-dimensional centraliser of the whole algebra are computed.

(c), (d) The central elements and the charge spectrum are computed on $\mathcal{S}$. The kernel follows from the charges alone: $(\omega^a, s, z)$ acts as $\omega^a s z$ on quarks and as $s z^{-3}$ on leptons, and both equal 1 exactly when $z=\omega^{-a}s$. That leaves $3\times2=6$ elements. $\blacksquare$

Witnesses: `test_complex_octonion_clifford_system_is_maximal_spin9`, `test_standard_model_algebra_is_the_centraliser_of_colour_in_spin9`, `test_spin9_standard_model_group_has_exactly_z6_kernel`, `test_complex_octonion_doublets_are_chiral`.

**Prior art, and what is new here.** The group-theoretic core is published. Todorov and Dubois-Violette obtain $G_{\mathrm{SM}}$ as the intersection $\mathrm{Spin}(9)\cap(\mathrm{SU}(3)\times\mathrm{SU}(3))/\mathbb{Z}_3$ inside $F_4=\mathrm{Aut}\,J_3(\mathbb{O})$ (*Int. J. Mod. Phys. A* **33**, 1850118 (2018), [arXiv:1806.09450](https://arxiv.org/abs/1806.09450)). Krasnov proves that "the group $G_{SM}$ is the subgroup of $\mathrm{Spin}(9)$ that commutes with … a certain complex structure $J_R$ in the space $\mathbb{O}^2$ of $\mathrm{Spin}(9)$ spinors", with $J_R$ right multiplication by a unit imaginary octonion. He finds the spinor to be $L=(1,2)_{-1}$ and $Q=(3,2)_{1/3}$ (his normalisation is $2Y$), with the $\mathbb{Z}_6$ above. He also notes that "the right-handed fermions that are SU(2) singlets are not part of $\mathbb{O}^2$" (*J. Math. Phys.* **62**, 021703 (2021), [arXiv:1912.11282](https://arxiv.org/abs/1912.11282), Theorem 1 and §3.6). Four things are UHM's own. (i) The spinor space is UHM's Hilbert space plus the parallel spinor, and the Clifford system on it is forced: no generator is chosen. (ii) The electroweak algebra is characterised as the centraliser of the colour group that UHM already derives from $G_2$. (iii) The imaginary unit of $\mathcal{H}$ acts on $\mathcal{S}$ as a weak-isospin generator: $i/2\in\mathfrak{su}(2)_L$ (checked). (iv) The chirality statement T-327 and the $B-L$ statement T-329 below.

**What (Cl) does not give.**
- *The Lorentz spinor index — a separate factor (2026-09-25, [Spacetime, Theorem 48e](/docs/core/foundations/spacetime#теорема-48e)).* No $\mathrm{SU}(2)$ acting on $\mathcal{S}_{\mathbb{C}}$ commutes with $G_{\mathrm{SM}}$: the commutant of $\mathfrak{g}_{\mathrm{SM}}$ in $\mathfrak{so}(32)$ is abelian, of dimension 6. The Weyl index is therefore the colour-fixed part $\mathbb{C}_O^2$ of the octonionic spinor of Theorem 48c, and one generation is $F=\mathbb{C}_O^2\otimes_{\mathbb{C}}\mathcal{S}_{\mathbb{C}}=(\mathbf 2,\mathbf{16})$ of $\mathrm{SL}(2,\mathbb{C}_O)\times\mathrm{Spin}(10)$: $2\times16=32$ complex components, $4$ for the lepton doublet. The spatial rotations of 48c act on the first factor and commute with the whole $\mathrm{Spin}(10)$, so the $\mathrm{SU}(2)$ of (b) is not a spacetime rotation (the mismatch of Theorem 48d(d) is resolved).
- *Right-handed fields — supplied by the complexification.* $\mathcal{S}$ holds the left-handed doublets only. The $\mathrm{SU}(2)_L$-singlets $u_R, d_R, e_R$ (and $\nu_R$) do not fit into sixteen real dimensions. They appear in $\mathcal{S}_{\mathbb{C}}=\mathcal{S}\otimes_{\mathbb{R}}\mathbb{C}'$, where the tenth generator is forced, with the Standard Model hypercharges, and with them comes $\mathrm{U}(1)_{B-L}$ (T-329, [§2.6](#поколение-t329), sect. 2.3a).
- *The Higgs doublet.* The vector representation of $\mathrm{Spin}(9)$ decomposes as $(\mathbf 1,\mathbf 3)_0\oplus(\mathbf 3,\mathbf 1)_{-1/3}\oplus(\bar{\mathbf 3},\mathbf 1)_{1/3}$ (checked: hypercharges $0$ and $\pm\tfrac13$) and contains no doublet. In the vector of the $\mathrm{Spin}(10)$ of [§2.6](#поколение-t329) the colour-free four-plane $\{iL_{e_O},J,iJ,\gamma_{10}\}$ is one doublet with $Y=\pm\tfrac12$ (Theorem 2.6(f); the identification is [H], and the Yukawa structure is open). The identification $H\sim\gamma_{EU}$ of the Higgs sector belongs to the axis picture and is not supported here.
- *The complex structure of $\mathcal{H}$.* Under (Cl) the fermionic complex structure is $L_{e_O}$, not the $i$ of $\mathcal{H}$. The gauge group does not commute with $i$ (commutator norm $0.97$), because $i$ is itself a generator of $\mathrm{SU}(2)_L$. That the global phase of the holon's state space and a weak-isospin rotation coincide on $\mathcal{S}$ is a structural consequence of (Cl). Its reading is [I]. In the complete generation $i/2=T_{3L}+T_{3R}$, and the electric charge is $Q=i/2+(B-L)/2$ (Theorem 2.6(d)).

**Effect on sections 2.1–2.4.** The electroweak group no longer needs (FE). The axis construction of §2.3 is kept as a record [C at (FE)]. Under (Cl) the claim of §2.3a — uniqueness of $\mathrm{SU}(2)\times\mathrm{U}(1)$ given colour — holds as a theorem of the construction: the electroweak algebra is a centraliser, and a centraliser involves no choice. The objection of §2.1 — "the centraliser of $\mathrm{SU}(3)_C$ in $\mathrm{U}(7)$ is $\mathrm{U}(1)^3$" — concerns complex-linear maps of $\mathcal{H}$. $\mathrm{Spin}(9)$ acts on $\mathcal{S}$ real-linearly, and there the centraliser is $\mathrm{U}(2)$.

### 2.6 The complete generation: the complexified spinor and $\mathrm{Spin}(10)$ (T-329) {#поколение-t329}

:::tip[Status: Theorem 2.6 (a)–(f) is \[T\] as mathematics; as a result of UHM it is \[C at (Cl)\]; the Higgs identification in (f) is \[H\]]
Section 2.5 leaves the right-handed fields out. They come back without a new assumption. A Weyl field is complex, so a field with values in the real spinor $\mathcal{S}$ takes values in its complexification $\mathcal{S}_{\mathbb{C}}$. On $\mathcal{S}_{\mathbb{C}}$ the Clifford system gains exactly one generator, the group becomes $\mathrm{Spin}(10)$, and $\mathcal{S}_{\mathbb{C}}$ is one complete generation with $\nu_R$. The same computation settles which $\mathrm{SU}(2)$ is left-handed: the $\mathrm{SU}(2)$ of Theorem 2.5 is the diagonal of $\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$, and it acts as $\mathrm{SU}(2)_L$ only on the left half. Registry row T-329; numbers in `website/scripts/check_core_numbers.py`.
:::

**The space.** A Weyl spinor field takes values in a complex space $S_+\otimes_{\mathbb{C}}V$. If the internal space is the real module $\mathcal{S}$ of §2.5, then
$$S_+\otimes_{\mathbb{R}}\mathcal{S} = S_+\otimes_{\mathbb{C}}\mathcal{S}_{\mathbb{C}},\qquad \mathcal{S}_{\mathbb{C}} := \mathcal{S}\otimes_{\mathbb{R}}\mathbb{C}' \cong \mathbb{R}^{32}.$$
Here $\mathbb{C}'=\mathbb{R}^2$ has its own imaginary unit $i'$ and conjugation $K'$. The unit $i'$ is the one the field needs. It is not the $i$ of $\mathcal{H}$, which already acts inside $\mathcal{S}$ as a weak-isospin generator. This is the doubling $V\oplus\bar V$ that Distler and Garibaldi identify as the failure of $E_8$ models. Here it gives the whole chiral generation, because the group that acts on $\mathcal{S}_{\mathbb{C}}$ is larger than $\mathrm{Spin}(9)$.

**Theorem 2.6 (T-329).**

**(a) The tenth generator is forced [T].** The nine generators of §2.5, made $\mathbb{C}'$-antilinear, $\gamma_a K'$ ($a=1,\dots,9$), satisfy the Clifford relations on $\mathcal{S}_{\mathbb{C}}$. The operators that anticommute with all nine span exactly $\{i'K',\,i'\}$. Of these, only $\pm i'K'=:\pm\gamma_{10}$ are symmetric with square $+1$; the sign is the orientation of $\mathbb{R}^{10}$. The volume element $\omega=\gamma_1\cdots\gamma_{10}$ equals $\pm i'$: the $\mathrm{Spin}(10)$-invariant complex structure is the imaginary unit of the field. No eleventh generator exists on $\mathbb{R}^{32}$. The ten generate $\mathfrak{spin}(10)$ (dimension 45), in which $\mathfrak{spin}(9)$ of §2.5 acts as its $\mathbb{C}'$-linear extension, and $(\mathcal{S}_{\mathbb{C}},\omega)$ is the $\mathbf{16}$ of $\mathrm{Spin}(10)$.

**(b) The left and right halves are canonical [T].** Colour fixes four of the ten directions pointwise: $iL_{e_O}$, $J$, $iJ$, $\gamma_{10}$. The volume element $\omega_4$ of this four-plane satisfies $\omega_4^2=1$ and splits $\mathcal{S}_{\mathbb{C}}=V_L\oplus V_R$, $16+16$. On $V_L$ the field's complex structure is $\omega=+L_{e_O}$, on $V_R$ it is $\omega=-L_{e_O}$, with one sign for quarks and leptons alike. So $(V_L,\omega)=(\mathcal{S},L_{e_O})$ is the doublet space of Theorems 2.5(d) and 4.4, and $(V_R,\omega)$ is its conjugate copy. The centraliser of colour in $\mathfrak{spin}(10)$ (dimension 7) is $\mathfrak{su}(2)_L\oplus\mathfrak{su}(2)_R\oplus\mathfrak{u}(1)$. Here $\mathfrak{su}(2)_L$ acts only on $V_L$ and $\mathfrak{su}(2)_R$ only on $V_R$. The centre is the hypercharge of Theorem 2.5, which in the completion is $(B-L)/2$.

**(c) The $\mathrm{SU}(2)$ of Theorem 2.5 is diagonal [T].** The $\mathrm{Spin}(9)$ of §2.5 is the stabiliser of $\gamma_{10}$. Each element of its $\mathfrak{su}(2)$ has components of equal norm in $\mathfrak{su}(2)_L$ and in $\mathfrak{su}(2)_R$: it is the diagonal. No $\mathrm{Spin}(9)\subset\mathrm{Spin}(10)$ that contains colour contains $\mathrm{SU}(2)_L$. Such a $\mathrm{Spin}(9)$ fixes a unit vector $v$ of the colour-free four-plane. The stabiliser of $v$ in $\mathfrak{so}(4)=\mathfrak{su}(2)_L\oplus\mathfrak{su}(2)_R$ is the graph of an isomorphism and meets $\mathfrak{su}(2)_L$ in zero, because $\mathrm{SU}(2)_L$ acts on $\mathbb{R}^4=\mathbb{H}$ by left multiplication and fixes no vector. On $V_L\cong\mathcal{S}$ the diagonal acts as $\mathrm{SU}(2)_L$ and $(B-L)/2$ acts as $Y$, so Theorems 2.5 and 4.4 describe the left half correctly. The gauge group of a full generation, however, does not lie in that $\mathrm{Spin}(9)$.

**(d) Hypercharges: one generation with $\nu_R$ [T].** The imaginary unit of $\mathcal{H}$ lifts to $\mathcal{S}_{\mathbb{C}}$ as $i/2=T_{3L}+T_{3R}$, the rotation of the plane $\{J,iJ\}$. Put $T_{3R}:=(i/2)|_{V_R}$ and $Y:=(B-L)/2+T_{3R}$. Then
$$(V_L,\omega)=(\mathbf 3,\mathbf 2)_{1/6}\oplus(\mathbf 1,\mathbf 2)_{-1/2},\qquad (V_R,\omega)=(\bar{\mathbf 3},\mathbf 1)_{-2/3}\oplus(\bar{\mathbf 3},\mathbf 1)_{1/3}\oplus(\mathbf 1,\mathbf 1)_{1}\oplus(\mathbf 1,\mathbf 1)_{0},$$
that is $Q_L, L_L$ and $u^c, d^c, e^c, \nu^c$: one generation with a right-handed neutrino, every field a left-handed Weyl field. The electric charge is
$$Q=T_{3L}+Y=\tfrac{i}{2}+\tfrac{B-L}{2},$$
with $\pm\tfrac23$ and $\pm\tfrac13$ three times each, $\pm1$ once each and $0$ twice. The stabiliser of $\nu^c$ in $\mathfrak{su}(3)\oplus\mathfrak{su}(2)_L\oplus\mathfrak{su}(2)_R\oplus\mathfrak{u}(1)_{B-L}$ is exactly $\mathfrak{g}_{\mathrm{SM}}$ (dimension 12); in $\mathfrak{spin}(10)$ it is $\mathfrak{su}(5)$ (dimension 24). The kernel of $\mathrm{SU}(3)\times\mathrm{SU}(2)_L\times\mathrm{U}(1)_Y$ on $\mathcal{S}_{\mathbb{C}}$ is again exactly $\mathbb{Z}_6$. The sign of $T_{3R}$ does not matter: the two signs are exchanged by the Weyl reflection of $\mathrm{SU}(2)_R$.

**(e) The anomalies cancel [T].** For every $X\in\mathfrak{spin}(10)$, $\mathrm{Tr}_{\mathbf{16}}X^3=0$ and $\mathrm{Tr}_{\mathbf{16}}X=0$, because $\mathfrak{so}(10)$ has no cubic invariant (Georgi and Glashow, *Phys. Rev. D* **6**, 429 (1972)). Since $Y\in\mathfrak{spin}(10)$, all perturbative anomalies of the generation vanish: $\mathrm{SU}(3)^2Y$, $\mathrm{SU}(2)^2Y$, $Y^3$, gravitational $Y$, and $\mathrm{SU}(3)^3$, with two triplets $Q$ against the two antitriplets $u^c, d^c$. Witten's global $\mathrm{SU}(2)$ anomaly (*Phys. Lett. B* **117**, 324 (1982)) is absent too: there are four doublets, an even number. With $\nu^c$ the anomalies $(B-L)^3$ and gravitational $B-L$ also vanish; without it $(B-L)^3=-1$ per generation. The hypercharges are not fitted. The objection to T-179, that with $\nu_R$ every $Y+c(B-L)$ passes, does not apply: here $Y$ is fixed by $\nu^c$ and $i$.

**(f) The colour-free Clifford plane is one Higgs doublet [T as a representation; the identification is \[H\]].** The four directions $\{iL_{e_O},J,iJ,\gamma_{10}\}$ of the vector $\mathbb{R}^{10}$ carry $(\mathbf 1,\mathbf 2,\mathbf 2)_0$ of $\mathfrak{su}(2)_L\oplus\mathfrak{su}(2)_R\oplus\mathfrak{u}(1)_{B-L}$. Under $G_{\mathrm{SM}}$ they are one complex doublet with $Y=\pm\tfrac12$: $\mathfrak{su}(2)_L$ fixes no vector of the plane, and $Y$ rotates it with charge $\tfrac12$. Clifford multiplication by these vectors exchanges $V_L$ and $V_R$, which is the form of a Dirac mass. The stabiliser in $\mathfrak{g}_{\mathrm{SM}}$ of $\gamma_{10}$, or of any vector of the plane $\{iL_{e_O},\gamma_{10}\}$, is $\mathfrak{su}(3)\oplus\mathfrak{u}(1)_Q$ with exactly the $Q$ of (d). A vacuum in the plane of the clock and the tenth generator therefore leaves the photon. The six colour directions are $(\mathbf 3\oplus\bar{\mathbf 3},\mathbf 1)_{\pm1/3}$ and preserve the halves. This answers where the doublet sits that §2.5 could not find in the vector of $\mathrm{Spin}(9)$. A caveat: one real vector coupled by Clifford multiplication gives the four members of a generation one Dirac mass. That is the relation $m_t=m_b=m_\tau$ of minimal $\mathrm{SO}(10)$ with a real $\mathbf{10}$, which fails. The Yukawa structure is open [Pr].

**Proof.** (a) The relations are direct computation. The volume element of the nine, $\gamma_1K'\cdots\gamma_9K' = K'$ (the volume of §2.5 is $1$), is central in their Clifford algebra and splits $\mathbb{R}^{32}$ into its $\pm1$ eigenspaces $\mathcal{S}\otimes e_\pm$, the two inequivalent irreducible modules. An operator $T$ that anticommutes with the nine anticommutes with $K'$, so it exchanges the two. It commutes with the even algebra $\mathrm{Cl}_8\cong M_{16}(\mathbb{R})$, whose commutant is $\mathbb{R}$. By Schur's lemma $T=1\otimes(a\sigma_1+bJ_2)$ with $J_2=i'$, and $\sigma_1=i'K'$ up to sign: a two-dimensional space. Its square is $(a^2-b^2)\,1$, and it is symmetric only for $b=0$. $\mathrm{Cl}_{11,0}\cong M_{32}(\mathbb{C})$ has irreducible modules of real dimension 64 (Lawson and Michelsohn, ch. I §4), so ten is the maximum on $\mathbb{R}^{32}$. (b) $\omega_4$ is a product of four anticommuting symmetric involutions, so $\omega_4^2=1$. The restrictions of $\omega$ and the splitting of the centraliser are computed. (c) The graph argument is given above; the equal norms are computed. (d)–(f) The spectra, stabilisers and the kernel are computed; the anomaly traces are computed for random $X\in\mathfrak{spin}(10)$ and from the charge table. $\blacksquare$

Witnesses: `test_the_tenth_generator_is_forced_by_complexifying_the_spinor`, `test_left_right_split_is_canonical_and_the_t326_su2_is_diagonal`, `test_one_generation_with_a_right_handed_neutrino`, `test_the_full_generation_is_anomaly_free`, `test_the_colour_singlet_clifford_plane_is_one_higgs_doublet`.

**Premises of §2.6 (2026-09-26).** As a result of UHM, T-329 uses (Cl₀) — fermions are vectors of the spinor module $\mathcal{S}$ — and (W₀), that the spinor factor of the field is a complex space; the second sentence of (Cl) is the theorem below. (W₀) is not a free input. It follows from (P) of [Theorem 48e](/docs/core/foundations/spacetime#теорема-48e), and **under (Cl₀) it is equivalent to one generation being chiral and anomaly-free** [T, 48e(f),(h)]: with a real Lorentz factor every fermion space built on $\mathcal{S}$ is anomalous or vector-like, with a complex one it is chiral and anomaly-free in every dimension. (Cl₀) itself is independent of (P\*), the spacetime premise stated for an arbitrary fermion module: $F = \mathbb{C}^2\otimes_{\mathbb{C}}\mathbb{C}^7$ satisfies (P\*) and not (Cl₀) ($\mathbb{C}^7$ is not a $\mathrm{Cl}_7$-module), and $F_3 = \mathbb{C}^3\otimes_{\mathbb{C}}\mathcal{S}_{\mathbb{C}}$ satisfies (Cl₀) and not (P\*) ([Premises of UHM](/docs/reference/premises#посылка-кл0), §7).

**The clock breaks the symmetry in three steps [T].** The second sentence of (Cl) in §2.5 — the clock breaks $\mathrm{Spin}(9)$ to the normaliser of colour — is a theorem. It follows from the rule by which UHM obtains colour, $\mathrm{SU}(3)_C=\mathrm{Stab}_{G_2}(e_O)$, applied to the two structure maps of the clock unit, $L_{e_O}$ and $R_{e_O}$:

| algebra | centraliser of $L_{e_O}$ | centraliser of $R_{e_O}$ = of both |
|---|---|---|
| $\mathfrak{g}_2$ | $\mathfrak{su}(3)_C$ (8) | $\mathfrak{su}(3)_C$ (8) |
| $\mathfrak{spin}(9)$ on $\mathcal{S}$ | $\mathfrak{su}(4)\oplus\mathfrak{su}(2)$ (18) | normaliser of colour, $\mathfrak{su}(3)\oplus\mathfrak{su}(2)\oplus\mathfrak{u}(1)$ (12) |
| $\mathfrak{spin}(10)$ on $\mathcal{S}_{\mathbb{C}}$ | $\mathfrak{su}(4)\oplus\mathfrak{su}(2)_L\oplus\mathfrak{su}(2)_R$ (21) | $\mathfrak{su}(3)\oplus\mathfrak{su}(2)_L\oplus\mathfrak{su}(2)_R\oplus\mathfrak{u}(1)_{B-L}$ (15) |

In $\mathfrak{g}_2$ the two maps have the same stabiliser; beyond $\mathfrak{g}_2$ they differ. The left map alone leaves Pati–Salam; both leave the left–right model. The vector $\nu^c$ of (d) then leaves $G_{\mathrm{SM}}$, and a vacuum in the plane $\{iL_{e_O},\gamma_{10}\}$ of (f) leaves $\mathrm{SU}(3)\times\mathrm{U}(1)_Q$. The breaking scale of $B-L$ is not fixed (§2.3a). Witness: `test_the_clock_stabiliser_gives_pati_salam_then_left_right_then_colour`.

**What remains of (Cl).** Its first sentence, (Cl₀): *fermion fields take values in the spinor module $\mathcal{S}$ of the octonionic Clifford system.* Three facts narrow it, and a fourth restates it. (i) The closure of $\mathrm{Im}\,\mathbb{O}$ under the seven left multiplications is all of $\mathbb{O}$, since $e_ke_k=-1$. So the parallel spinor $\eta_0$ is forced as soon as $\mathcal{H}$ must carry the structure maps. Neither $\mathcal{H}=\mathbb{C}^7$ ($\mathbb{R}^{14}$) nor the Page–Wootters space $\mathbb{C}^7\otimes\mathbb{C}^7$ ($\mathbb{R}^{98}$) is a $\mathrm{Cl}_7$-module: module dimensions are multiples of 16. (ii) (Cl₀) cannot follow from axioms about $\Gamma$ [T for the obstruction]. The central element $-1$ of $\mathrm{SU}(2)_L$ acts as $-1$ on $\mathcal{S}$ and as $+1$ on $\mathrm{End}(\mathcal{S})$. So everything built from coherence matrices, including their tensor products, has integer weak isospin. The doublets are vectors of $\mathcal{S}$, not operators on it. (iii) The reading "$\Gamma$ is a bilinear of the matter field", with the bilinears of spinors as operators, is [I]. Witness: `test_fermions_are_vectors_of_s_not_operators_and_eta0_is_forced`. (iv) (Cl₀) has an equivalent form that names no module ([T-347](/docs/reference/premises#t-347)(b), [T]): the product of the holon's octonions acts on the fermion field, $\rho(x)\rho(x)=\rho(x^2)$ with $\rho$ commuting with $i$. Its irreducible modules are $\mathbb O$ with left and with right multiplication, and both give $\mathcal S$ with the $\mathrm{Spin}(9)$ of §2.5. Maximality of that $\mathrm{Spin}(9)$, faithfulness of a representation of the holon's observables and every property of the holon do not force (Cl₀) (T-347(a), (c)). Witness: `test_fermion_module_premise_is_the_holons_product_acting_on_matter`.

**What T-329 uses of the spinor factor (2026-09-26).** Step (a) uses only that the spinor factor $S_+$ of the field is a complex space. Its dimension enters nowhere; call this (W₀). By [Spacetime, Theorem 48e](/docs/core/foundations/spacetime#теорема-48e)(f), (a)–(f) hold unchanged on $\mathbb{C}^n\otimes_{\mathbb{C}}\mathcal{S}_{\mathbb{C}}$ for every $n$, with every anomaly trace multiplied by $n$. By 48e(h), (W₀) is what a chiral, anomaly-free generation requires: with a real spinor factor every fermion space built on $\mathcal{S}$ is anomalous or vectorlike. So T-329 does not use the two-component premise (W) of the 3+1 reading. Its status, [T] as mathematics and [C at (Cl)] in UHM, is unchanged, and it no longer shares a premise with the physical reading of Theorem 48c. Witnesses: `test_uhm_internal_structure_is_blind_to_the_multiplicity_of_the_fermion_field`, `test_a_real_lorentz_factor_gives_an_anomalous_or_vectorlike_generation`.

**Prior art, and what is new here.** The algebra of the completion is textbook. Pati and Salam gave the left–right group with lepton number as a fourth colour (*Phys. Rev. D* **10**, 275 (1974)). Georgi (*AIP Conf. Proc.* **23**, 575 (1975)) and Fritzsch and Minkowski (*Ann. Phys.* **93**, 193 (1975)) put one generation with $\nu_R$ into the $\mathbf{16}$ of $\mathrm{SO}(10)$, with the Higgs bidoublet in the $\mathbf{10}$. Krasnov obtains Pati–Salam times Lorentz as the commutant of two complex structures on $\mathbb{O}\otimes\mathbb{O}'$ in $\mathrm{Spin}(11,3)$. He reads the eigenspaces of one complex structure as particles and antiparticles, and he breaks the symmetry with a Higgs that transforms as the bidoublet of the left–right model ("Spin(11,3), particles and octonions", [arXiv:2104.01786](https://arxiv.org/abs/2104.01786)). UHM's own here: (i) the tenth generator is forced by the complex unit of the field, not chosen; (ii) the halves are cut by the colour-free four-plane and told apart by $\omega=\pm L_{e_O}$; (iii) the diagonal statement (c), which corrects the reading of T-326 as the gauge group of a full generation; (iv) $i/2=T_{3L}+T_{3R}$ and $Q=i/2+(B-L)/2$; (v) the breaking chain as stabilisers of the clock's two structure maps.

---

## 3. Fermionic Representations as Gap Configurations

### 3.1 Theorem 3.1 (Quarks and Leptons as Gap Configurations)

:::warning[Status: Hypothesis \[H\]]
Elementary fermions are identified with degenerate ($R \to 0$) configurations $\Gamma$, classified by quantum numbers $\mathrm{SU}(3)_C \times \mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$.
:::

:::info Status stratification
- ~~Algebraic embedding $G_2 \supset SU(3) \times SU(2) \times U(1)$: [T] (standard group theory)~~ — **retracted [✗]** (2026-09-25): impossible, $\mathrm{rank}\,G_2 = 2 < 4 = \mathrm{rank}\,(SU(3) \times SU(2) \times U(1))$ (sect. 1.1 of this page says so itself); the maximal subgroups of full rank in $G_2$ are $\mathrm{SU}(3)$ and $\mathrm{SO}(4)$, and the centraliser of $\mathrm{SU}(3)$ in $G_2$ is finite. What holds: $\mathrm{SU}(3)\subset G_2$ [T]; $\mathrm{SU}(2)\times\mathrm{U}(1)$ is added outside $G_2$ by (FE) [C at (FE)]
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
The result $N_{\text{gen}} = 3$ has **composite status: count [T], identification [I]**. The **count** is the exact cardinality $N_{\text{gen}} = |\mathrm{QR}(7)| = |\mathbb{Z}_7^*/\{\pm1\}| = (7-1)/2 = 3$ **[T]** — the three generations are the quadratic-residue classes (equivalently charge-conjugation orbits, since $-1$ is a non-residue mod $7$) of the unique order-3 subgroup $\{1,2,4\}\subset\mathbb{Z}_7^*$; this is group-theoretic and **independent of the Gap-potential topology** (the older $A_4$-swallowtail bound is now only a consistency check). The physical identification of these classes with the observed generations remains **[I]**. Full discussion: [Theorem 1.2](/docs/physics/particle-physics/fermion-generations#теорема-ровно-три-генерации).
:::

:::note[Family symmetry under (Cl) — T-328]
Any family symmetry must commute with $G_{\mathrm{SM}}$. Under (Cl) ([§2.5](#sm-из-клиффорда)) this can be computed. One copy of $\mathbb{C}\otimes\mathbb{O}$ admits only the phases $\mathrm{U}(1)_B\times\mathrm{U}(1)_L$, so no permutation of three objects inside it — axes, Fano lines through $O$, quaternionic subalgebras — is horizontal; the reasoning of items (c)–(d) below finds colour, not families. Triality fixes colour but rotates the plane spanned by $L_{e_O}$ and $R_{e_O}$ through $2\pi/3$, so it permutes embeddings of the Standard Model group rather than copies of fermions. A horizontal three exists on the Page–Wootters clock register: its three non-trivial real harmonics are permuted simply transitively by $\mathrm{Aut}(\mathbb{Z}_7)/\{\pm1\}\cong\mathbb{Z}_3$, which commutes with all of $G_{\mathrm{SM}}$. The identification of generations with these harmonics is the hypothesis (GC) [H]. With that $\mathbb{Z}_3$ exact, every mixing matrix would be trivial — refuted by $|V_{us}|\approx0.224$ — so under (GC) the family $\mathbb{Z}_3$ must be broken. Details: [Fermion generations, §5.3](/docs/physics/particle-physics/fermion-generations#поколения-t328).
:::

**(a)** Each generation corresponds to a **topologically distinct** minimum of $V_{\mathrm{Gap}}$ in the vacuum configuration.

**(b)** From Swallowtail analysis: the number of minima of $V_{\mathrm{eff}}$ depends on the codimension of the catastrophe. For $A_4$ (swallowtail): up to 3 minima.

**(c)** The number of generations $N_{\mathrm{gen}} =$ the number of distinct **types** of degenerate $\Gamma$-configurations with $R \to 0$ not connected by a $G_2$-transformation.

**(d)** From the Fano structure: the 7 Fano lines define 7 "privileged" triplets. From Fano duality (point $\leftrightarrow$ line): each point lies on 3 lines $\to$ 3 nonequivalent "types" of vacuum alignment $\to$ **$N_{\mathrm{gen}} = 3$**.

**Justification of (d).** The vacuum configuration selects the O-direction (sect. 1.3). The remaining 6 directions form a Fano graph with 3 lines passing through each point. Three classes of nonequivalent orientations of the triplet $(A,S,D)$ relative to the Fano structure give 3 generations. More precisely: the automorphism group of the Fano plane $\mathrm{PSL}(2,7)$ (order 168) acts on 7 points. The stabilizer of one point (O) has order $168/7 = 24 \cong S_4$. Orbits of $S_4$ on pairs from the remaining 6 points: $C(6,2) = 15$ pairs, divided into classes by size. Three classes $\to$ three generations.

---

## 4. Chirality from $G_2$-Orientability {#кираль}

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

summing over the 7 Fano lines. ~~Orientability of a $G_2$-manifold is equivalent to the existence of a parallel spinor.~~ Corrected (2026-09-25): a parallel spinor exists exactly when the holonomy lies in $G_2$; orientability (with a spin structure) only guarantees a $G_2$-structure, not a parallel one. And a smooth manifold of $G_2$ holonomy gives no chiral fermions in four dimensions — they require singularities (Acharya and Witten, "Chiral fermions from manifolds of $G_2$ holonomy", [arXiv:hep-th/0109152](https://arxiv.org/abs/hep-th/0109152)).

### 4.3 Chiral Operator from 4D Reduction — retracted [✗]

:::danger Retracted [✗] (2026-09-25): chirality is not derived from $G_2$
This subsection claimed that the reduction 7D → 4D along $\mathrm{Im}(\mathbb{O}) = \mathbb{R}^1_O \oplus \mathbb{R}^3_{ASD} \oplus \mathbb{R}^3_{LEU}$ induces the chirality operator $\gamma_5 = i\Gamma_O\Gamma_A\Gamma_S\Gamma_D$ with eigenvalues $\pm1$, and that left chirality of $\mathrm{Gap}(E,U)=0$ follows from the parallel spinor [T]. Three facts refute it.
1. *The operator.* In this page's own convention, $\Gamma_i\Gamma_j+\Gamma_j\Gamma_i=-2\delta_{ij}$ realised by left octonionic multiplication, $(\Gamma_O\Gamma_A\Gamma_S\Gamma_D)^2=+1$ — for all 35 quadruples of generators — so $i\Gamma_O\Gamma_A\Gamma_S\Gamma_D$ has eigenvalues $\pm i$, not $\pm1$ (`test_gamma5_with_i_has_imaginary_spectrum`).
2. *The split.* $\mathbb{R}^3_{ASD}\oplus\mathbb{R}^3_{LEU}$ is the retracted axis split (Theorem 1.1(a)); reading $\{O,A,S,D\}$ as the four spacetime directions is retracted with it ([spacetime](/docs/core/foundations/spacetime#секторная-декомпозиция)).
3. *No chirality from $G_2$.* Every irreducible representation of $G_2$ is real — the longest element of its Weyl group is $-1$ — so every $G_2$-module is self-conjugate, i.e. non-chiral in the sense of Distler and Garibaldi (*Commun. Math. Phys.* **298**, 419–436 (2010), [arXiv:0905.2658](https://arxiv.org/abs/0905.2658), Def. 2.5), and a self-conjugate structure stays self-conjugate on restriction to any subgroup. On the geometric side, compactification on a smooth manifold of $G_2$ holonomy gives no four-dimensional chiral fermions (Acharya and Witten, [arXiv:hep-th/0109152](https://arxiv.org/abs/hep-th/0109152)).

Where the corpus actually takes chirality from: the $\mathbb{Z}_2$-grading of a KO-dimension-6 finite spectral triple — Connes's $(A_F,H_F)$, imported through the bimodule construction (T-178, retracted as a derivation) — and a hypercharge that separates $\mathbf 3$ from $\bar{\mathbf 3}$, which lies outside $G_2$ (the centraliser of $\mathrm{SU}(3)$ in $G_2$ is finite). Chirality is an input of the UHM construction, not an output; deriving it is a research programme [Pr]. For the left-handed doublets this is superseded under (Cl): [§4.4](#киральность-t327), T-327, [C at (Cl)].
:::

*Record of the retracted derivation.* Under reduction 7D $\to$ 4D (splitting $\mathrm{Im}(\mathbb{O}) = \mathbb{R}^1_O \oplus \mathbb{R}^3_{ASD} \oplus \mathbb{R}^3_{LEU}$) the spinor representation was said to induce a chiral operator:

$$\gamma_5 = i\Gamma_O \Gamma_A \Gamma_S \Gamma_D$$

This operator was said to have eigenvalues $\pm 1$ (it has $\pm i$, item 1 above) and to define the chirality of 4D spinors:

$$\gamma_5 \psi_L = -\psi_L, \quad \gamma_5 \psi_R = +\psi_R$$

The chirality of a 4D spinor is determined by the **internal spinor** $\chi_{\mathrm{int}}$:

$$\gamma_5 \psi = \pm \psi \quad \Longleftrightarrow \quad \Gamma_L \Gamma_E \Gamma_U \chi_{\mathrm{int}} = \mp \chi_{\mathrm{int}}$$

:::note[Status: Retracted \[✗\]]
~~The connection $\mathrm{Gap}(E,U) = 0 \leftrightarrow$ left chirality is derived from the structure of the $G_2$-parallel spinor $\eta_0$ and the reduction $\mathrm{Cliff}(7) \supset \mathrm{Cliff}(1,3) \otimes \mathrm{Cliff}(3)$.~~ Retracted with this subsection (box above); the former status was "Theorem [T]".
:::

### 4.4 Chirality of the doublets under (Cl) (T-327) {#киральность-t327}

:::tip[Status: Theorem 4.4 is \[T\] as mathematics; as a result of UHM it is \[C at (Cl)\]]
In §4.3 the claim that chirality follows from $G_2$ was retracted: $G_2$ has only real representations. Under (Cl) of [§2.5](#sm-из-клиффорда) the fermion representation of the left-handed doublets is complex and not self-conjugate, whatever admissible complex structure is taken. So it passes the requirement Distler and Garibaldi set for unified models, without a choice made afterwards. The right-handed singlets lie outside $\mathbb{C}\otimes\mathbb{O}$. In its complexification ([§2.6](#поколение-t329)) the uniform choice of (c) is forced, and the whole generation, $\nu_R$ included, is chiral. Registry row T-327.
:::

**Theorem 4.4 (T-327).** Let $G_{\mathrm{SM}}$ act on $\mathcal{S}=\mathbb{C}\otimes\mathbb{O}\cong\mathbb{R}^{16}$ as in Theorem 2.5.

**(a)** The commutant of $\mathfrak{g}_{\mathrm{SM}}$ in $\mathrm{End}_{\mathbb{R}}(\mathcal{S})$ has dimension 4. It is $\mathbb{C}\oplus\mathbb{C}$, one factor on the quark block (real dimension 12) and one on the lepton block (real dimension 4). The $G_{\mathrm{SM}}$-invariant complex structures on $\mathcal{S}$ are therefore exactly four: $\pm L_{e_O}$ on each block independently.

**(b)** Each of the four makes $\mathcal{S}$ a complex representation that is not isomorphic to its conjugate. The hypercharge spectrum is $\tfrac16$ (six states) and $\pm\tfrac12$ (two states), and it is not symmetric under $Y\mapsto -Y$. No admissible complex structure yields a self-conjugate — non-chiral — fermion representation.

**(c)** The uniform choice
$$\mathcal{J} = L_{e_O} = \gamma_O\,\gamma_8\,\gamma_9$$
is the volume element of the three Clifford directions orthogonal to the colour plane. It is also the complex structure that makes colour a unitary group (T-279: multiplication by an axis is a complex structure on its sky). This choice gives quark and lepton doublets the same handedness, $(\mathbf 3,\mathbf 2)_{1/6}\oplus(\mathbf 1,\mathbf 2)_{-1/2}$, as in the Standard Model. Reversing the sign on the lepton block gives $(\mathbf 3,\mathbf 2)_{1/6}\oplus(\mathbf 1,\mathbf 2)_{+1/2}$. Reversing the overall sign gives the mirror world, which is a choice of orientation. In the completion of [§2.6](#поколение-t329) the field's complex structure is $\omega=+L_{e_O}$ on the whole left half (Theorem 2.6(b)): the block-reversed structure does not occur, and the overall sign is the orientation of $\gamma_{10}$.

**Proof.** (a) Under $\mathfrak{g}_{\mathrm{SM}}$, $\mathcal{S}$ is the sum of two real-irreducible modules of complex type, and they are not isomorphic because their hypercharges differ. By Schur's lemma the commutant is $\mathbb{C}\oplus\mathbb{C}$, and its complex structures are $(\pm i,\pm i)$. The dimension 4 and the identity $\gamma_O\gamma_8\gamma_9=L_{e_O}$ are computed. (b), (c) The spectra are computed for $L_{e_O}$ and for the block-reversed structure. $\blacksquare$

Witness: `test_complex_octonion_doublets_are_chiral` (both choices, the charges, and $i/2\in\mathfrak{su}(2)_L$).

**How this meets the test of Distler and Garibaldi.** They prove that no real or complex form of $E_8$ contains the Lorentz group and the Standard Model group so that the fermions come out chiral. The mechanism of failure is general: a real representation complexifies to $V\oplus\bar V$, and a Weyl fermion valued in it is vectorlike (*Commun. Math. Phys.* **298**, 419–436 (2010), [arXiv:0905.2658](https://arxiv.org/abs/0905.2658)). Here the fermion field is a Weyl spinor tensored over $\mathbb{C}$ with $(\mathcal{S},\mathcal{J})$, $\psi\in S_+\otimes_{\mathbb{C}}(\mathcal{S},\mathcal{J})$. Theorem 4.4(b) says that no admissible $\mathcal{J}$ can return a self-conjugate $V$. *Update (T-329):* the identification of the field's complex structure with $\mathcal{J}$ is no longer needed. Tensoring over $\mathbb{R}$ is what a field with values in the real $\mathcal{S}$ does, and it gives $\mathcal{S}_{\mathbb{C}}=V\oplus\bar V$. This doubling is vectorlike only for the diagonal group of Theorem 2.5. On it the tenth Clifford generator is forced, and for the $G_{\mathrm{SM}}\subset\mathrm{Spin}(10)$ of Theorem 2.6(d) the space $(\mathcal{S}_{\mathbb{C}},\omega)$ is the chiral $\mathbf{16}$: its hypercharges $\tfrac16$ (six), $-\tfrac12$ (two), $-\tfrac23$, $\tfrac13$ (three each), $1$ and $0$ are not symmetric under $Y\mapsto-Y$. The field's complex unit is $i'=\pm\omega$. It is neither the $i$ of $\mathcal{H}$ nor $L_{e_O}$, and it coincides with $L_{e_O}$ on the left half. *Update ([Spacetime, Theorem 48e](/docs/core/foundations/spacetime#теорема-48e)(e)):* the Weyl spinor is $S_+=\mathbb{C}_O^2$, the colour-fixed part of the spinor $\mathbb{O}^2$ of Theorem 48c, and $i'$ is its complex unit. On $F=S_+\otimes_{\mathbb{C}}\mathcal{S}_{\mathbb{C}}$ (real dimension 64) the Lorentz algebra $\mathfrak{sl}(2,\mathbb{C}_O)$ and $\mathfrak{spin}(10)$ commute, their joint commutant is $\mathbb{C}$, and the Weyl unit acts as $+L_{e_O}$ on $F_L$ and as $-L_{e_O}$ on $F_R$. So $F=(\mathbf 2,\mathbf{16})$ is chiral for $\mathrm{SL}(2,\mathbb{C}_O)\times G_{\mathrm{SM}}$: sixteen left-handed Weyl fields; the conjugate representation is right-handed, and the hypercharges of the $\mathbf{16}$ are not symmetric under $Y\mapsto-Y$. *Update (2026-09-26, [Spacetime, Theorem 48e](/docs/core/foundations/spacetime#теорема-48e)(f), (h)):* the mechanism of Distler and Garibaldi holds inside UHM as a theorem. With a real Lorentz factor, $F=\mathbb{R}^m\otimes_{\mathbb{R}}\mathcal{S}$ with any complex structure that commutes with $\mathfrak{g}_{\mathrm{SM}}$ is $p\,Q_L\oplus(m-p)\,\bar Q_L\oplus r\,L_L\oplus(m-r)\,\bar L_L$, and it is anomaly-free only if it is vectorlike. Chirality needs the complex unit of the Lorentz factor, not its two components: $\mathbb{C}^n\otimes_{\mathbb{C}}\mathcal{S}_{\mathbb{C}}$ is chiral and anomaly-free for every $n$.

---

## 5. Full Gauge Structure: 18 Bosons {#калибровочные-бозоны}

### 5.1 Theorem 5.1 (Full Table of Gauge Fields)

:::tip[Status: Theorem \[T\] for the SM part; \[H\] for $G_2$-extra]
$G_2$-generators generate $\mathrm{SU}(3)_C$ (8 gluons) and 6 $G_2$-extra bosons. The Fano-electroweak construction (FE) determines $\mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$ (4 bosons) — **[C at (FE)]** (the pair $(E,U)$ from $\kappa_0$ is [T]).
:::

| Field | Group | Number | Mass | Status |
|---|---|---|---|---|
| Gluons $g$ | $\mathrm{SU}(3)_C$ | 8 | 0 (confinement) | SM [T] |
| $W^\pm, Z$ | $\mathrm{SU}(2)_L$ | 3 | $M_W, M_Z$ (Higgs) | SM [T] |
| Photon $\gamma$ | $\mathrm{U}(1)_{\mathrm{EM}}$ | 1 | 0 | SM [T] |
| **$G_2$-extra** | **$G_2/\mathrm{SU}(3)$** | **6** | **$M_{G_2} \sim \mu_{\mathrm{phys}}$** | **Beyond SM [H]** |

**(a)** 6 $G_2$-extra bosons are "connector" fields from $3 + \bar{3}$ in the decomposition $14 \to 8 + 3 + \bar{3}$: the generators that move the $O$-direction. (The former gloss "they connect the spatial ($3$) and Gap ($\bar{3}$) sectors" used the retracted axis labels, Theorem 1.1(a).) The mass is determined by the Gap in the O-to-$3$ and O-to-$\bar{3}$ sectors:

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
Spontaneous electroweak symmetry breaking arises from Gap condensation in the $\bar{3}$-to-$\bar{3}$ sector (the axis pairs of $\{L,E,U\}$; not an $\mathrm{SU}(3)$ sector, Theorem 1.1(a)). A condensate $\gamma_{EU}\neq0$ is not $\mathrm{SU}(3)_C$-invariant (sect. 9.4), so as stated this hypothesis breaks colour together with the electroweak group.
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

$$\delta M_H^2 = \frac{3\lambda_3^2 \bar{A}^2}{4\mu^2} \approx \frac{3 \cdot (73.8)^2 \cdot (0.047)^2}{4 \cdot 16.6} \approx 0.54$$

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

This factor is provided by the Fano-Higgs line $\{1,5,6\}$: among the elements of the generation triplet $(1,2,4)$, only $k=1$ lies on this line. ~~The vacuum Gap profile additionally breaks Z₃, since $k=1$ (A) and $k=2$ (S) lie in the 3-sector, while $k=4$ (L) lies in the $\bar{3}$-sector.~~ Retracted [✗] (2026-09-25): the sector labels are not an $\mathrm{SU}(3)$ decomposition (Theorem 1.1(a)).

:::warning The generation $\mathbb{Z}_3$ is a colour rotation
$\sigma$ extends to the automorphism $e_k\mapsto e_{2k}$ of $\mathbb{O}$ (all signs $+$); it fixes $e_O=e_7$ and therefore lies in $\mathrm{SU}(3)_C=\mathrm{Stab}_{G_2}(e_O)$ of sect. 1.3. In the basis $A-iD$, $S-iU$, $L-iE$ of the triplet it is the cyclic permutation matrix, of determinant 1 (`test_generation_z3_lies_in_colour_su3`). Whatever breaks $\langle\sigma\rangle$ breaks $\mathrm{SU}(3)_C$. The Higgs line does: $\sigma$ maps the pair $(E,U)$ to $(D,E)$, so a condensate $\gamma_{EU}\neq0$ (sect. 6.1) is not $\mathrm{SU}(3)_C$-invariant — as no $\Gamma$ with a coherence outside the pairs $(A,D)$, $(S,U)$, $(L,E)$ is not. In UHM's own identifications, the $\mathbb{Z}_3$ breaking that the mass hierarchy needs is therefore colour breaking. No mechanism on this page reconciles it with unbroken colour; the contradiction is open [Pr] ([fermion generations, Theorem 5.2](/docs/physics/particle-physics/fermion-generations#thm-5-2)).
:::

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

All three are non-Fano triples (containing $D=3$ as mediator). Generation mixing passes through **dimension D**, which the page used to call the "color dimension" and connect with [confinement](/docs/physics/gauge-symmetry/confinement); no axis is a colour direction (the triplet is spanned by $A-iD$, $S-iU$, $L-iE$, Theorem 1.1(a)), so that link is retracted [✗].

### 10.4 Theorem 10.2 (Generation Assignment and Fano Distance to Higgs)

:::warning[Hypothesis 10.2 (Generation assignment) \[H\]]
The distinction between $k=2$ and $k=4$ is determined by the type of intermediate sector in the Fano path to the Higgs. Strictly — a hypothesis requiring lattice confirmation. The "sectors" below are sets of axis pairs, not $\mathrm{SU}(3)$ sectors (Theorem 1.1(a)); the premise that $(L,D)$ carries Gap $\approx0$ and $(S,D)$ Gap $\sim\epsilon$ is the vacuum assumption (SA) [H] of [fermion generations, §4.4](/docs/physics/particle-physics/fermion-generations#гипотеза-секторной-асимметрии).
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
Proton decay within (FE) is mediated by $G_2$-extra bosons of Planck mass. Lifetime $\tau_p \sim 4\times10^{47}$ years — practically unobservable.
:::

6 $G_2$-extra bosons with $M_{G_2} \sim M_{\text{Planck}}$ mediate proton decay channels (d=6 operators via $G_2$-extra exchange). Lifetime:

$$\tau_p^{(G_2)} \sim \frac{M_{\text{Planck}}^4}{\alpha_{G_2}^2 m_p^5} \sim 4\times10^{47} \text{ years}$$

This is $\sim 13$ orders of magnitude above the current experimental limit (Super-Kamiokande: $\tau_p > 2.4 \times 10^{34}$ years). **The proton is effectively stable** within (FE): evaluating $M_{\text{Planck}}^4/(\alpha_{G_2}^2 m_p^5)$ with $M_{\text{Planck}}=1.22\times10^{19}$ GeV, $\alpha_{G_2}\sim1/24$ gives $\sim4\times10^{47}$ yr — far beyond any detector.

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

:::warning[Retracted 2026-09-26 (T-345(e)); the status was Hypothesis 14.1 (CP-violation phase) \[H\]]
**Status [✗].** The value $64.5°$ in (c) is $77.1°-12.6°$, and the $12.6°$ of (b) is not a property of the Standard Model: in one-loop running of the full Yukawa matrices from $M_Z$ to $2\times10^{16}$ GeV the phase moves by $0.003°$ and $\sin\delta$ by $2\times10^{-5}$. The estimate multiplies a phase by the running of a coupling, and its sign was chosen to fit. Without it the Fano value $\lvert\delta\rvert=77.1°$ is $7.6\sigma$ from $65.7°\pm1.5°$ (PDG 2024). The phase source, the PT-odd cubic $V_3$, is retracted: every $G_2$-invariant cubic is PT-even (T-331), and in the Clifford frame the CKM phase is a Yukawa input (T-333). See [CKM, Theorem 4.2](/docs/physics/particle-physics/ckm-matrix#thm-4-2) and [§11](/docs/physics/particle-physics/ckm-matrix#11-вкус-с-часов). The text below is the former derivation. Former box: "The formula $\delta_{\text{CP}} = \arg(e^{2\pi i(k_{1\text{st}} + k_{2\text{nd}} - k_{3\text{rd}})/7})$ is heuristic, not derived from diagonalization of Yukawa matrices."
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

Observed: $65.7° \pm 1.5°$ (PDG 2024 global fit); the LHCb tree-level combination gives $64.6° \pm 2.8°$ (ICHEP 2024). The predicted $64.5°$ agrees within $\sim 0.1°$ ($\approx 0.04\sigma$) with the direct value and within $\sim 1\sigma$ of the fit. The older $69° \pm 4°$ is superseded. See [CKM §4.2](/docs/physics/particle-physics/ckm-matrix#thm-4-2) for the canonical value.

:::info[Note on the sign]
The sign of the two-loop correction is determined from $\mathrm{Im}\,\mathrm{Tr}(Y_u Y_u^\dagger Y_d Y_d^\dagger [Y_u Y_u^\dagger, Y_d Y_d^\dagger])$ (Antusch et al., 2003). With positive sign: $77.1° + 12.6° = 89.7°$ — discrepancy $> 8\sigma$ from the direct $64.6° \pm 2.8°$. The new assignment **predicts a negative sign** of the correction. Full range: $|\delta_{\text{CP}}| = 77.1° \pm 12.6°$ (from $64.5°$ to $89.7°$). *Retracted 2026-09-26 (T-345(e)):* there is no correction of either sign to choose; the phase runs by $0.003°$ (box above).
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

:::warning[Retracted 2026-09-26 (T-345(e)): the ratios 2 : 3 : 1 are refuted, and running does not repair them]
**Status [✗].** With PDG 2024 the angles are $13.00°$, $2.397°$, $0.2138°$, in the ratio $60.8:11.2:1$ (the "$65:12:1$" above is an older rounding); the Fano differences give $2:3:1$, so $\theta_{23}$ would exceed $\theta_{12}$, while the data have $\theta_{12}/\theta_{23}=5.4$. In one-loop Standard Model running from $M_Z$ to $2\times10^{16}$ GeV $\lvert V_{us}\rvert$ changes by $2\times10^{-5}$, so no RG suppression acts on an angle. The formulas of (b) are the Fritzsch texture, refuted separately by $\lvert V_{cb}\rvert\ge0.073$ against $0.0418$ ([CKM, note after §2.2](/docs/physics/particle-physics/ckm-matrix#thm-2-1), [§6.3](/docs/physics/particle-physics/ckm-matrix#derivation-vus)).
:::

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
| $\mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$ from Fano-electroweak construction (FE) | [T] for the combinatorics (uniqueness of $(E,U)$, Higgs line); [C at (FE)] for the group; uniqueness among rank-4 groups [H]; the "$\bar 3\to\{E,U\}\oplus\{L\}$" decomposition retracted [✗] |
| Consistency of the two $\mathrm{SU}(3)$'s ($G_2$ and 42D PW) | retracted [✗] (Theorem 2.2) |
| Decomposition $7\to1_O\oplus3_{ASD}\oplus\bar3_{LEU}$ (axis labels) | retracted [✗]; replaced by $\mathbb{C}^7=\mathbb{C}e_O\oplus\mathbf 3\oplus\bar{\mathbf 3}$, $\mathbf 3=\mathrm{span}_{\mathbb C}\{A-iD,S-iU,L-iE\}$ [T] (Theorem 1.1(a)) |
| $G_2\supset SU(3)\times SU(2)\times U(1)$ | retracted [✗] (rank $2<4$; sect. 3.1) |
| Full SM from $G_2$ + (FE) | [C] (electroweak dynamics is conditional) |
| $G_{\mathrm{SM}}=(\mathrm{SU}(3)\times\mathrm{SU}(2)\times\mathrm{U}(1))/\mathbb{Z}_6$ as the normaliser of colour in the $\mathrm{Spin}(9)$ of $\mathbb{C}\otimes\mathbb{O}$ (T-326, §2.5) | [T] as mathematics; [C at (Cl)] in UHM; electroweak uniqueness through it [C at (Cl)] |
| Chirality of the left-handed doublets, $(\mathbf 3,\mathbf 2)_{1/6}\oplus(\mathbf 1,\mathbf 2)_{-1/2}$ not self-conjugate (T-327, §4.4) | [C at (Cl)]; with the completion of §2.6 the whole generation is chiral |
| No family symmetry inside one copy; triality not horizontal; clock ℤ₃ horizontal (T-328) | [T]; generations as clock harmonics [C at (GC)], (GC) [H]; (GC) with an exact ℤ₃ is refuted by mixing data [✗] |
| Complexified spinor: forced tenth generator, $V_L\oplus V_R$ with $\omega=\pm L_{e_O}$, the $\mathrm{SU}(2)$ of T-326 diagonal, one generation with $\nu_R$ and SM hypercharges, anomalies cancel, the Higgs doublet in the colour-free Clifford plane; no $Z'$ in the doublet sector, $B-L$ with the right-handed fields (T-329, §2.6) | [T] as mathematics, [C at (Cl)] in UHM; Higgs identification [H]; "no $Z'$ at any energy" (T-297) stays [H] |
| Quarks and leptons as Gap configurations | [H] |
| Three generations from Fano structure ($N_{\text{gen}} = 3$) | **count [T], identification [I]** — exact count $\|\mathrm{QR}(7)\|=3$ [T], physical identification [I] ([proof](/docs/physics/particle-physics/fermion-generations#теорема-ровно-три-генерации)) |
| Chirality from $\eta_0$ and $\mathrm{Gap}(E,U) = 0$ | retracted [✗] (sect. 4.3: spectrum $\pm i$, not $\pm1$; $G_2$ has only real representations) |
| 18 gauge bosons (SM + 6 $G_2$-extra) | [T] for SM; [H] beyond SM |
| Mass hierarchy from Gap hierarchy of the vacuum | [H] |
| Resolution of hierarchy via RG with anomalous dimensions | [H] |
| Higgs as Gap condensate of E-U coherence | [H] (as in sect. 6.1; the table said [T] until 2026-09-25; a condensate $\gamma_{EU}\neq0$ is not $\mathrm{SU}(3)_C$-invariant, sect. 9.4) |
| $M_H^2 = 2\lambda_4 v^2 + 3\lambda_3^2 \bar{A}^2/(4\mu^2)$ (octonionic correction) | [H] |
| $\delta\lambda/\lambda_{\text{SM}} \sim O(10^{-2}\text{--}10^{-3})$ (FCC prediction) | [I] |
| Gap anticorrelation (Ward), factor $19/49$ | [T] |
| Generation selection principle $(1,2,4)$ from associator | [T] (uniqueness) |
| Fano Yukawa selection rule | **[T]** (via $f_{ijk}$ — unique $G_2$-invariant trilinear operator) |
| Mass hierarchy $m_t \gg m_c, m_u$ from Fano selection | **[T]** (consequence of selection rule [T]); the further $m_c \gg m_u$ needs (SA) — [C at (SA)] |
| $m_t \approx 173$ GeV from IR fixed point (unique O(1) Yukawa) | [T] |
| Light generation masses via loop suppression | [H] (order of magnitude) |
| Generation assignment: $k=1 \to 3$rd, $k=4 \to 2$nd, $k=2 \to 1$st | $k=1\to3$rd **[T]** (45a); $k=4\to2$nd, $k=2\to1$st **[C at (SA)]**, (SA) [H] (45b retracted) |
| N=1 SUSY from parallel spinor $\eta_0$ | [T] |
| SUSY breaking via $V_3$ | **[T]** (T-50: superpotential $W$ is unique, Schur's lemma) |
| $m_{3/2} \sim 10^{13}$ GeV | **[T]** (T-50: $m_{3/2} \sim \varepsilon^3 M_P$ from uniqueness of $W$, Schur's lemma) |
| $m_{\tilde{q}} \sim 10^{13}$ GeV (absence at LHC) | [H] |
| $\tau_p \sim 4\times10^{47}$ years ($G_2$-extra channel) | [H] (proton effectively stable) |
| $\delta_{\text{CP}} \approx 64.5°$ | **[✗]** (2026-09-26, T-345(e): the $12.6°$ correction is absent in the SM, uncorrected $77.1°$ is $7.6\sigma$ from $65.7°\pm1.5°$; was [H], $\approx 0.04\sigma$ from direct $64.6° \pm 2.8°$) |
| Normal neutrino mass hierarchy | **[C]** (O-sector Yukawa; C14: $m_2/m_3$ with RG-correction) |


---

**Related documents:**
- [G₂-structure and Fano plane](/docs/physics/gauge-symmetry/g2-structure)
- [Fano selection rules](/docs/physics/gauge-symmetry/fano-selection-rules)
- [Confinement](/docs/physics/gauge-symmetry/confinement)
- [Higgs sector](/docs/physics/particle-physics/higgs-sector)
