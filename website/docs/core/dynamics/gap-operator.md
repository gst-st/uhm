---
sidebar_position: 7
title: "Gap Operator"
slug: /core/dynamics/gap-operator
description: "Definition of Ĝ = Im(Γ), antisymmetry, spectrum, opacity rank, relation to purity, Serre bundle curvature, G₂/⊥ decomposition"
---

# Gap Operator

:::info Who this chapter is for
The antisymmetric part of Γ: definition, spectrum, relation to curvature. Assumes familiarity with the [coherence matrix](./coherence-matrix) and basic linear algebra.
:::

This chapter introduces the **Gap operator** $\hat{\mathcal{G}}$ — a mathematical object that precisely measures the **total opacity** of the holon. If the [Gap measure](/docs/core/dynamics/coherence-matrix#мера-зазора) $\mathrm{Gap}(i,j) \in [0,1]$ describes the opacity of a single pair of dimensions, then the Gap operator collects all information about 21 pairs into a single algebraic object with a spectrum, symmetries, and geometric meaning.

The reader will learn:
- What $\hat{\mathcal{G}} = \mathrm{Im}(\Gamma)$ is and why it is antisymmetric
- How the spectrum of $\hat{\mathcal{G}}$ determines the **opacity rank** (from 0 to 3)
- Why Gap is **literally the curvature** of a finite noncommutative geometry
- How the $G_2$ decomposition separates "healthy" and "pathological" Gap

:::tip Intuitive explanation
Recall the [coherence matrix](./coherence-matrix) $\Gamma$ — it is Hermitian, meaning $\gamma_{ji} = \gamma_{ij}^*$. This means each coherence has a **real** and an **imaginary** part:

- **Real part** $\mathrm{Re}(\gamma_{ij})$ — the aspect in which the external and internal views of the connection **agree**. This is "common ground" — what is accessible both to the observer and to the system itself.
- **Imaginary part** $\mathrm{Im}(\gamma_{ij})$ — the aspect in which they **diverge**. This is the "gap" — the mismatch between how the connection looks "from outside" and how it is felt "from inside."

The Gap operator $\hat{\mathcal{G}} = \mathrm{Im}(\Gamma)$ is a **map of all mismatches at once**. If $\hat{\mathcal{G}} = 0$, the system is fully transparent: external and internal coincide for all pairs. If $\hat{\mathcal{G}} \neq 0$, there are "blind spots" — pairs of dimensions where the system does not "see" itself as the world sees it.

A remarkable fact: $\hat{\mathcal{G}}$ belongs to the Lie algebra $\mathfrak{so}(7)$ — the same algebra that describes rotations in 7-dimensional space. Gap generates a **rotation** of the coherence matrix: strong opacity in pair $(i,j)$ "mixes" dimensions $i$ and $j$.
:::

The Gap operator $\hat{\mathcal{G}}$ is the central object of [Gap dynamics](/docs/core/dynamics/gap-dynamics), formalizing the **antisymmetric part** of the [coherence matrix](/docs/core/dynamics/coherence-matrix) $\Gamma$. It measures the total opacity of the system and belongs to the Lie algebra $\mathfrak{so}(7)$, linking [dual-aspect semantics](/docs/physics/dual-aspect/gap-semantics) with the [G₂ structure](/docs/physics/gauge-symmetry/g2-structure).

:::warning Gap notation conventions {#конвенции-gap}

| Notation | Meaning | Formula |
|-------------|----------|---------|
| $\hat{\mathcal{G}}$ | Gap **operator** | $\hat{\mathcal{G}} = \mathrm{Im}(\Gamma) \in \mathfrak{so}(7)$ |
| $\mathrm{Gap}(i,j)$ | Gap **between dimensions** $i,j$ | $\lvert\sin(\arg(\gamma_{ij}))\rvert$ |
| $\mathcal{G}_{\text{total}}$ | **Total** Gap | $2(\lambda_1^2 + \lambda_2^2 + \lambda_3^2)$ |
| $\mathrm{Gap}_{AB}(i,j)$ | **Inter-holon** Gap | $\lvert\sin(\arg(\gamma_{i^A j^B}))\rvert$ |

In this document $\hat{\mathcal{G}}$ denotes the Gap operator (antisymmetric matrix); $\mathcal{G}_{\text{total}}$ denotes its total magnitude.
:::

---

## 1. Definition {#определение}

### 1.1 Basic definition

:::tip Definition (Gap operator) [Т]
For a Hermitian coherence matrix $\Gamma \in \mathcal{D}(\mathbb{C}^7)$, $\Gamma^\dagger = \Gamma$, the **Gap operator** is defined as:

$$
\hat{\mathcal{G}} := \frac{1}{2i}(\Gamma - \Gamma^T) = \mathrm{Im}(\Gamma)
$$

— the purely imaginary part of the coherence matrix.
:::

Since $\Gamma^\dagger = \Gamma$ (Hermiticity), the transposed matrix $\Gamma^T = \Gamma^*$ (complex conjugate), hence:

$$
\hat{\mathcal{G}} = \frac{\Gamma - \Gamma^*}{2i} = \mathrm{Im}(\Gamma)
$$

Matrix elements:

$$
\hat{\mathcal{G}}_{ij} = \mathrm{Im}(\gamma_{ij}) = |\gamma_{ij}| \cdot \sin(\theta_{ij})
$$

where $\theta_{ij} = \arg(\gamma_{ij})$ is the phase of the coherence.

### 1.2 Relation to the Gap measure

For a pair of dimensions $(i, j)$ the gap measure is $\mathrm{Gap}(i,j) = |\sin(\theta_{ij})|$, therefore:

$$
|\hat{\mathcal{G}}_{ij}| = |\gamma_{ij}| \cdot \mathrm{Gap}(i,j)
$$

The Gap operator combines **connection strength** $|\gamma_{ij}|$ and **opacity** $\mathrm{Gap}(i,j)$ into a single object.

:::info Necessity of complex Γ [Т-132]
A nontrivial Gap structure ($\mathrm{Gap}(i,j) > 0$) **requires** complex coherences: for $\gamma_{ij} \in \mathbb{R}$ the measure $\mathrm{Gap} = |\sin(\arg(\gamma_{ij}))| = 0$ identically. Details: [T-132 [Т]](/docs/proofs/consciousness/operationalization#t-132).
:::

### 1.3 Full table of 21 coherence pairs {#таблица-21-пара}

$\binom{7}{2} = 21$ pairs of dimensions define 21 coherences $\gamma_{ij}$, each lying on exactly one [Fano line](/docs/physics/gauge-symmetry/fano-selection-rules):

| Pair $(i,j)$ | Fano line | Sector | Physical meaning |
|:---:|:---:|:---:|:---|
| $(A,S)$ | $\{A,S,D\}$ | $\mathbf{3}$-$\mathbf{3}$ | Articulation structure |
| $(A,D)$ | $\{A,S,D\}$ | $\mathbf{3}$-$\mathbf{3}$ | Dynamic articulation |
| $(S,D)$ | $\{A,S,D\}$ | $\mathbf{3}$-$\mathbf{3}$ | Structural dynamics |
| $(L,E)$ | $\{L,E,U\}$ | $\bar{\mathbf{3}}$-$\bar{\mathbf{3}}$ | Logic of interiority |
| $(L,U)$ | $\{L,E,U\}$ | $\bar{\mathbf{3}}$-$\bar{\mathbf{3}}$ | Logical unity |
| $(E,U)$ | $\{L,E,U\}$ | $\bar{\mathbf{3}}$-$\bar{\mathbf{3}}$ | **Higgs channel** |
| $(A,L)$ | $\{A,L,O\}$ | $\mathbf{3}$-$\bar{\mathbf{3}}$ | Articulation of logic |
| $(A,O)$ | $\{A,L,O\}$ | $O$-link | Observation of articulation |
| $(L,O)$ | $\{A,L,O\}$ | $O$-link | Logical foundation |
| $(S,E)$ | $\{S,E,O\}$ | $\mathbf{3}$-$\bar{\mathbf{3}}$ | Structure of interiority |
| $(S,O)$ | $\{S,E,O\}$ | $O$-link | Structural foundation |
| $(E,O)$ | $\{S,E,O\}$ | $O$-link | **Regenerative channel** ($\kappa_0$) |
| $(D,U)$ | $\{D,U,O\}$ | $\mathbf{3}$-$\bar{\mathbf{3}}$ | Dynamics of unity |
| $(D,O)$ | $\{D,U,O\}$ | $O$-link | Dynamic foundation |
| $(U,O)$ | $\{D,U,O\}$ | $O$-link | **Clock channel** ($\kappa_0$) |
| $(A,E)$ | — | $\mathbf{3}$-$\bar{\mathbf{3}}$ | Articulation of experience |
| $(A,U)$ | — | $\mathbf{3}$-$\bar{\mathbf{3}}$ | Articulation of unity |
| $(S,L)$ | — | $\mathbf{3}$-$\bar{\mathbf{3}}$ | Structural logic |
| $(S,U)$ | — | $\mathbf{3}$-$\bar{\mathbf{3}}$ | Structural unity |
| $(D,E)$ | — | $\mathbf{3}$-$\bar{\mathbf{3}}$ | Dynamics of interiority |
| $(D,L)$ | — | $\mathbf{3}$-$\bar{\mathbf{3}}$ | Dynamic logic |

:::info Sector membership
The 21 pairs split into sectors according to the decomposition $7 = 1_O \oplus \mathbf{3}_{A,S,D} \oplus \bar{\mathbf{3}}_{L,E,U}$:
- **$\mathbf{3}$-$\mathbf{3}$**: 3 pairs (within the confinement sector), $\varepsilon_{33} \sim 0.06$
- **$\bar{\mathbf{3}}$-$\bar{\mathbf{3}}$**: 3 pairs (within the electroweak sector), $\varepsilon_{\bar{3}\bar{3}} \sim 10^{-17}$
- **$\mathbf{3}$-$\bar{\mathbf{3}}$**: 9 pairs (confinement↔electroweak), $\varepsilon_{3\bar{3}} \approx 0$
- **$O$-links**: 6 pairs ($O$ with the rest), $\varepsilon_O \sim 1$

The assignment of pairs marked "—" to Fano lines depends on the choice of $G_2$ gauge ([T-42a](/docs/proofs/categorical/uniqueness-theorem#g2-ригидность) [Т]). The first 15 pairs are uniquely determined by the base lines; the last 6 form the remaining Fano lines out of 7.
:::

---

## 2. Algebraic properties {#свойства}

:::tip Theorem 2.1 (Properties of the Gap operator) [Т]
**(a)** $\hat{\mathcal{G}}$ is a real **antisymmetric** matrix: $\hat{\mathcal{G}}^T = -\hat{\mathcal{G}}$.

**(b)** The eigenvalues of $\hat{\mathcal{G}}$ are purely imaginary: $\mathrm{spec}(\hat{\mathcal{G}}) \subset i\mathbb{R}$. They come in pairs $(\pm i\lambda_1, \pm i\lambda_2, \pm i\lambda_3, 0)$ with $\lambda_k \in \mathbb{R}$, plus one zero (since $N = 7$ is odd).

**(c)** $\hat{\mathcal{G}} \in \mathfrak{so}(7)$ — an element of the Lie algebra of the rotation group $\mathrm{SO}(7)$. It generates the rotation group via the exponential map $e^{\epsilon\hat{\mathcal{G}}} \in \mathrm{SO}(7)$.

**(d)** Total Gap:

$$
\mathcal{G}_{\text{total}} := \|\hat{\mathcal{G}}\|_F^2 = 2\sum_{i<j} \mathrm{Im}(\gamma_{ij})^2 = 2\sum_{i<j} |\gamma_{ij}|^2 \cdot \mathrm{Gap}(i,j)^2
$$

:::

### Convention for the norm $\mathcal{G}_{\text{total}}$ {#g-total-definition}

:::warning Norm convention [О]
$\mathcal{G}_{\text{total}}$ is defined as the **full** Frobenius norm (counting both pairs $(i,j)$ and $(j,i)$): $\mathcal{G}_{\text{total}} = \|\hat{\mathcal{G}}\|_F^2 = \sum_{i,j} |\hat{\mathcal{G}}_{ij}|^2 = 2\sum_{i<j} \mathrm{Im}(\gamma_{ij})^2$. The factor of 2 is due to the antisymmetry $\hat{\mathcal{G}}_{ji} = -\hat{\mathcal{G}}_{ij}$. This ensures consistency with the purity decomposition $P = P_{\text{sym}} + \mathcal{G}_{\text{total}}$ (Theorem 4.1) and the spectral formula $\mathcal{G}_{\text{total}} = 2(\lambda_1^2 + \lambda_2^2 + \lambda_3^2)$ (Theorem 3.1).
:::

#### Identity with the Dirac operator [Т] {#тождество-tr-d2}

:::tip Corollary (Spectral identity)
$$
\mathrm{Tr}(D_{\mathrm{int}}^2) = \omega_0^2 \cdot \mathcal{G}_{\mathrm{total}}
$$

where $D_{\mathrm{int}}$ is the [internal Dirac operator](/docs/core/foundations/spacetime#теорема-спектральная-тройка) (T-53 [Т]) with elements $[D_{\mathrm{int}}]_{ij} = \omega_0 \cdot \mathrm{Gap}(i,j) \cdot |\gamma_{ij}| \cdot e^{i\theta_{ij}}$. This identity connects the total Gap to the coefficient $a_2$ of the [spectral action](/docs/physics/gravity/quantum-gravity#теорема-полное-спектральное-действие) (T-65 [Т]) and justifies the derivation of the potential [$V_{\mathrm{Gap}}$](/docs/core/dynamics/gap-thermodynamics#вывод-vgap-из-спектрального-действия) from the axioms.
:::

**Proof.** (a) $\hat{\mathcal{G}}^T = \mathrm{Im}(\Gamma)^T$. Since $\mathrm{Im}(\gamma_{ij}) = -\mathrm{Im}(\gamma_{ji})$ (consequence of Hermiticity), we get $\hat{\mathcal{G}}^T = -\hat{\mathcal{G}}$. (b) Standard property of antisymmetric matrices of odd dimension. (c) $\mathfrak{so}(7)$ is the space of antisymmetric $7 \times 7$ matrices. (d) $\|\hat{\mathcal{G}}\|_F^2 = \sum_{ij} |\hat{\mathcal{G}}_{ij}|^2 = 2\sum_{i<j} \mathrm{Im}(\gamma_{ij})^2$ (the factor of 2 from counting both pairs $(i,j)$ and $(j,i)$). $\square$

---

## 3. Spectral interpretation {#спектр}

:::tip Theorem 3.1 (Spectral structure of Gap) [Т]
Let $\mathrm{spec}(\hat{\mathcal{G}}) = \{0, \pm i\lambda_1, \pm i\lambda_2, \pm i\lambda_3\}$. Then:

**(a)** $\mathcal{G}_{\text{total}} = \|\hat{\mathcal{G}}\|_F^2 = 2(\lambda_1^2 + \lambda_2^2 + \lambda_3^2)$

**(b)** $\lambda_{\max} = \max(\lambda_1, \lambda_2, \lambda_3)$ determines the **maximum opacity channel**.

**(c)** The number of nonzero $\lambda_k$ determines the **opacity rank** $r \in \{0, 1, 2, 3\}$.
:::

### Opacity rank table

| Rank | $\lambda$-spectrum | Interpretation |
|------|------------------|---------------|
| 0 | $(0, 0, 0)$ | Full transparency (all $\mathrm{Gap} = 0$) |
| 1 | $(\lambda, 0, 0)$ | One-dimensional opacity — one "break channel" |
| 2 | $(\lambda_1, \lambda_2, 0)$ | Two-dimensional opacity |
| 3 | $(\lambda_1, \lambda_2, \lambda_3)$ | Full opacity (maximum rank) |

:::info Remark [И]
The maximum opacity rank = 3 coincides with the number of "check" dimensions (E, O, U) in the [Hamming code H(7,4) analogy](/docs/core/dynamics/gap-dynamics#код-хэмминга). This coincidence connects the algebra of the Gap operator to the coding-theoretic structure.
:::

:::info Connection between Gap rank and the Hamming code
The maximum rank of $\hat{\mathcal{G}}$ equals **6** (three pairs of nonzero eigenvalues $\pm i\lambda_k$), corresponding to 3 independent "rotation planes" in $\mathbb{R}^7$. The number **3** coincides with the number of check bits in the Hamming code $H(7,4)$: 7 data bits, 3 check bits. The connection is not coincidental — both structures are determined by the Fano plane PG(2,2). Details: [Theorem T9](/docs/core/operators/lindblad-operators#теорема-хемминг-фано).
:::

---

## 4. Relation to purity {#связь-чистота}

:::tip Theorem 4.1 (Gap and purity) [Т]
The purity of the holon decomposes into symmetric and antisymmetric parts:

$$
P = \mathrm{Tr}(\Gamma^2) = P_{\text{sym}} + \mathcal{G}_{\text{total}}
$$

where $P_{\text{sym}} = \mathrm{Tr}(\mathrm{Re}(\Gamma)^2)$ is the "symmetric purity."
:::

**Corollary.** The total Gap **increases** purity $P$ at fixed $P_{\text{sym}}$: nonzero imaginary parts of coherences make a positive contribution to $\mathrm{Tr}(\Gamma^2)$.

**Proof.** $\mathrm{Tr}(\Gamma^2) = \mathrm{Tr}((\mathrm{Re}(\Gamma) + i\,\mathrm{Im}(\Gamma))^2)$. Expanding: $\mathrm{Tr}(\mathrm{Re}^2) - \mathrm{Tr}(\mathrm{Im}^2) + 2i\,\mathrm{Tr}(\mathrm{Re} \cdot \mathrm{Im})$. Since $P \in \mathbb{R}$ (spectral theorem), the imaginary part vanishes, and $P = \mathrm{Tr}(\mathrm{Re}^2) - \mathrm{Tr}(\mathrm{Im}^2)$. Since $\mathrm{Im}(\Gamma)$ is a real antisymmetric matrix, $\mathrm{Tr}(\mathrm{Im}^2) = -\|\mathrm{Im}(\Gamma)\|_F^2 = -\mathcal{G}_{\text{total}}$. Therefore $P = P_{\text{sym}} + \mathcal{G}_{\text{total}}$. $\square$

---

## 5. Serre bundle curvature {#кривизна-серра}

#### Theorem 5.1 / T-73 (Gap = curvature from the spectral triple) [Т] {#теорема-gap-серра}

:::tip Theorem 5.1
Within the [spectral triple](/docs/core/foundations/spacetime#теорема-спектральная-тройка) of UHM (T-53 [Т]), the measure $\mathrm{Gap}(i,j)$ **exactly coincides** with the norm of the connection curvature on the [Serre bundle](/docs/core/dynamics/gap-thermodynamics#геометрия-расслоения-серра) $\mathrm{Bundle}(\Gamma, \Omega) \to B_{\mathrm{ext}}$:

$$
\|\mathrm{Curv}\|_{ij}^2 = |[D_{\mathrm{int}}]_{ij}|^2 = \omega_0^2 |\gamma_{ij}|^2 \cdot \mathrm{Gap}(i,j)^2
$$
:::

**Proof (5 steps).**

**Step 1 (Connection from $D_{\mathrm{int}}$).** The internal Dirac operator $D_{\mathrm{int}}$ ([T-53](/docs/core/foundations/spacetime#теорема-спектральная-тройка) [Т]) defines a connection on the bundle of internal phases. Elements of $D_{\mathrm{int}}$:

$$
[D_{\mathrm{int}}]_{ij} = \omega_0 \cdot \mathrm{Gap}(i,j) \cdot |\gamma_{ij}| \cdot e^{i\theta_{ij}}
$$

This is the **covariant derivative** along internal directions. When $\gamma_{ij} = 0$, the connection breaks (no transport). When $\gamma_{ij} \neq 0$, transport is determined by $D_{\mathrm{int}}$.

**Step 2 (Connection curvature).** The bundle curvature is the commutator of covariant derivatives. In terms of $D_{\mathrm{int}}$:

$$
\|F\|_{ij}^2 = \sum_{k} |[D_{\mathrm{int}}]_{ik} \cdot [D_{\mathrm{int}}]_{kj} - [D_{\mathrm{int}}]_{jk} \cdot [D_{\mathrm{int}}]_{ki}|^2
$$

**Step 3 (Dominant contribution).** For pairs $(i,j)$ with a direct Gap, the dominant contribution to the curvature is the direct element:

$$
\|F\|_{ij}^{\mathrm{direct}} = \omega_0^2 \cdot |\gamma_{ij}|^2 \cdot \mathrm{Gap}(i,j)^2
$$

This coincides with $\|R_H\|_{ij}^2 \propto |\gamma_{ij}|^2 \cdot \mathrm{Gap}(i,j)^2$ from Theorem 1.1 of [gap-thermodynamics](/docs/core/dynamics/gap-thermodynamics#геометрия-расслоения-серра).

**Step 4 (Second Chern class).** Chern–Weil theory on the bundle:

$$
c_2(\mathrm{Bundle}) = \frac{1}{8\pi^2}\int \mathrm{Tr}(F \wedge F) = \frac{1}{8\pi^2}\sum_{i < j}|\gamma_{ij}|^2 \cdot \mathrm{Gap}(i,j)^2 = \frac{1}{8\pi^2}\mathrm{Tr}(D_{\mathrm{int}}^2) / \omega_0^2
$$

This is a **topological invariant**, defined via the spectral triple [Т] (T-53), not via analogy.

**Step 5 (Rigor from NCG).** In Connes' noncommutative geometry, curvature is defined through "junk" $a[D,b]$. For the finite triple $(A_{\mathrm{int}}, H_{\mathrm{int}}, D_{\mathrm{int}})$:

$$
\mathrm{Curv} = \sum_{i \neq j} [D_{\mathrm{int}}, e_{ij}]
$$

where $e_{ij}$ are matrix units. Curvature norm:

$$
\|\mathrm{Curv}\|_{ij}^2 = |[D_{\mathrm{int}}]_{ij}|^2 = \omega_0^2 |\gamma_{ij}|^2 \cdot \mathrm{Gap}(i,j)^2
$$

This is an **exact** identification, not an approximation, justified by the spectral triple [Т]. $\blacksquare$

:::info Clarification: norm vs. full curvature 2-form
The identification $\|\mathrm{Curv}\|_{ij}^2 = \omega_0^2|\gamma_{ij}|^2 \cdot \mathrm{Gap}(i,j)^2$ relates the connection norm to the square of the norm of the curvature 2-form. This is an **exact** identity at the level of norms. However, the full curvature 2-form $F$ carries additional geometric information not captured by the norm alone: holonomy of closed loops, Chern classes (topological invariants such as $c_2$ in Step 4), and the structure of the connection on the bundle (parallel transport). The norm $\|F\|^2$ determines the **energetics** (Yang–Mills action), but not the **topology** of the bundle in full.
:::

**Interpretation:**
- **Zero Gap** = flat connection = parallel transport is path-independent (the external description uniquely determines the internal one).
- **Nonzero Gap** = curvature $\neq 0$ = under a cyclic change of external parameters, the internal state acquires a geometric shift (analogue of the [Berry phase](/docs/physics/cosmology-phys/berry-phase)).

:::info Corollary (Geometric nature of Gap)
Gap is not an "analogy" with curvature — it is **literally the curvature** of a finite noncommutative geometry. All properties of Gap (antisymmetry, $G_2$-covariance, phase diagram) are direct consequences of the bundle geometry, not special postulates. The canonical metric of information geometry [gap-thermodynamics](/docs/core/dynamics/gap-thermodynamics#информационная-геометрия) is defined via $\mathrm{Tr}(D_{\mathrm{int}}^2)$.
:::

### Holonomy

Nontrivial holonomy of a closed loop $C$:

$$
\mathrm{Hol}(C) = \mathcal{P}\exp\left(\oint_C \mathcal{A}\right) \neq \mathbb{1}
$$

means that a system that has traversed a closed cycle of external influences has an **altered internal state** — a geometric formalization of "post-traumatic growth."

---

## 6. G₂/⊥ decomposition {#g2-разложение}

The Gap operator $\hat{\mathcal{G}} \in \mathfrak{so}(7)$ decomposes into components associated with the [G₂ structure](/docs/physics/gauge-symmetry/g2-structure).

:::tip Theorem 6.1 (G₂/⊥ decomposition of the Gap operator) [Т]
**(a)** $\hat{\mathcal{G}}$ decomposes into the G₂ part and the orthogonal complement:

$$
\hat{\mathcal{G}} = \hat{\mathcal{G}}_{G_2} + \hat{\mathcal{G}}_{\perp}
$$

where $\hat{\mathcal{G}}_{G_2} \in \mathfrak{g}_2 \subset \mathfrak{so}(7)$ is the projection onto the 14-dimensional subalgebra $G_2$, and $\hat{\mathcal{G}}_{\perp} \in \mathfrak{so}(7) / \mathfrak{g}_2$ is the complement (7-dimensional, since $\dim\,\mathfrak{so}(7) = 21$, $\dim\,\mathfrak{g}_2 = 14$).

**(b)** $\hat{\mathcal{G}}_{G_2}$ **preserves** the [Fano structure](/docs/physics/gauge-symmetry/fano-selection-rules): the flow generated by $\hat{\mathcal{G}}_{G_2}$ transforms $\Gamma$ while preserving the octonionic multiplication.

**(c)** $\hat{\mathcal{G}}_{\perp}$ **breaks** the Fano structure: the flow generated by $\hat{\mathcal{G}}_{\perp}$ mixes the Fano triplets.

**(d)** The complement is 7-dimensional: exactly one "breaking" direction per [dimension](/docs/core/structure/dimensions).
:::

### Two types of Gap

| Component | Dimension | Character | Interpretation |
|------------|-------------|----------|---------------|
| $\hat{\mathcal{G}}_{G_2}$ | 14 | Structure-preserving | "Coherent" Gap, compatible with the algebraic structure of $\mathbb{O}$ |
| $\hat{\mathcal{G}}_{\perp}$ | 7 | Structure-breaking | "Decoherent" Gap, associated with the loss of algebraic structure |

:::info Interpretation (Therapeutic) [И]
A healthy system has Gap predominantly in the $G_2$ sector. Pathological Gap is in the $\perp$ sector. The therapeutic goal: bring $\hat{\mathcal{G}}_{\perp} \to 0$ while leaving $\hat{\mathcal{G}}_{G_2}$ (which may be nonzero and beneficial).
:::

---

## 7. Commutator algebra {#коммутаторная-алгебра}

### 7.1 Properties of the commutator [Ĝ, Γ]

:::tip Theorem 7.1 (Commutator of the Gap operator with Γ) [Т]
**(a)** $[\hat{\mathcal{G}}, \Gamma]$ is **anti-Hermitian**: $[\hat{\mathcal{G}}, \Gamma]^\dagger = -[\hat{\mathcal{G}}, \Gamma]$.

**(b)** $\mathrm{Tr}([\hat{\mathcal{G}}, \Gamma]) = 0$.

**(c)** The commutator generates a **unitary flow**:

$$
\Gamma(\epsilon) = e^{i\epsilon\hat{\mathcal{G}}}\,\Gamma\,e^{-i\epsilon\hat{\mathcal{G}}} = \Gamma + i\epsilon[\hat{\mathcal{G}}, \Gamma] + O(\epsilon^2)
$$
:::

The Gap operator generates a rotation of the coherence matrix: strong Gap in pair $(i,j)$ rotates $\Gamma$ in the $(i,j)$ plane.

### 7.2 Octonionic cross product {#октонионное-крестное-произведение}

The Gap operator is related to the **cross product** on $\mathrm{Im}(\mathbb{O}) \cong \mathbb{R}^7$:

$$
x \times y := \frac{1}{2}(xy - yx) = \mathrm{Im}(xy)
$$

:::tip Theorem 7.2 (Gap via cross product) [Т]
**(a)** $\mathrm{Im}(\gamma_{ij})$ corresponds to the component of the cross product $(\hat{e}_i \times \hat{e}_j)_k \propto \epsilon_{ijk}$, arising from the non-commutativity of octonionic multiplication $e_i \cdot e_j \neq e_j \cdot e_i$.

**(b)** For pairs within a [Fano triplet](/docs/physics/gauge-symmetry/fano-selection-rules) $(i,j,k) \in PG(2,2)$: $e_i \times e_j = \pm e_k$ — the cross product is associative along the line (subalgebra $\cong \mathbb{H}$).

**(c)** For pairs **outside** a Fano triplet: the associator $[e_i, e_j, e_k] \neq 0$ generates an additional phase shift that increases Gap.
:::

:::info Proof: Gap = octonionic product [Т]

**Step 1 (Two $G_2$-invariant 2-forms).** (a) The imaginary parts $\mathrm{Im}(\gamma_{ij})$ of the coherence matrix entries define an antisymmetric bilinear form $\omega_\Gamma \in \Lambda^2(\mathbb{C}^7)$ via $\omega_\Gamma(e_i, e_j) = \mathrm{Im}(\gamma_{ij})$. (b) The imaginary part of the octonionic product $\omega_\mathbb{O}(e_i, e_j) = \mathrm{Im}(e_i \cdot e_j)$ defines an antisymmetric form on $\mathrm{Im}(\mathbb{O}) \cong \mathbb{R}^7$.

**Step 2 ($G_2$-invariance of both forms).** (a) Under $g \in G_2$: $\omega_\Gamma(ge_i, ge_j) = \mathrm{Im}((g\Gamma g^\dagger)_{ij}) = \mathrm{Im}(\gamma_{ij})$ by the $G_2$-covariance of the Fano dissipator (T-42a [Т]). (b) $\omega_\mathbb{O}$ is $G_2$-invariant by definition: $G_2 = \mathrm{Aut}(\mathbb{O})$ preserves the product.

**Step 3 (Schur's lemma).** The 7-dimensional representation $\mathbf{7}$ of $G_2$ is irreducible (standard, see Slansky 1981). By Schur's lemma, $\dim \mathrm{Hom}_{G_2}(\Lambda^2(\mathbf{7}), \mathbb{R}) = 1$ (the space of $G_2$-invariant 2-forms on $\mathbb{R}^7$ is one-dimensional). This is because $\Lambda^2(\mathbf{7}) = \mathbf{7} \oplus \mathbf{14}$ as $G_2$-representations, and $\mathrm{Hom}_{G_2}(\mathbf{7}, \mathbb{R}) = \{0\}$, $\mathrm{Hom}_{G_2}(\mathbf{14}, \mathbb{R}) = \{0\}$, but the invariant form arises from the $G_2$-invariant associative 3-form $\varphi \in \Lambda^3(\mathbf{7})$ via contraction with a fixed vector $v$: $\iota_v \varphi \in \Lambda^2(\mathbf{7})$. This gives exactly one independent 2-form.

**Step 4 (Proportionality and normalization).** Since both $\omega_\Gamma$ and $\omega_\mathbb{O}$ are $G_2$-invariant elements of the same 1-dimensional space, they are proportional: $\omega_\Gamma = c \cdot \omega_\mathbb{O}$ for some $c \in \mathbb{R}$. The coefficient $c$ is fixed by comparing on any Fano line: for $(i,j,k) \in PG(2,2)$, $\mathrm{Im}(e_i \cdot e_j) = \pm 1$ and $\mathrm{Im}(\gamma_{ij}) = |\gamma_{ij}| \sin\theta_{ij}$, giving $c = |\gamma_{ij}| \sin\theta_{ij} = |\gamma_{ij}| \cdot \mathrm{Gap}(i,j)$.

**Conclusion:** $\mathrm{Gap}(i,j) = |\sin(\arg(\gamma_{ij}))| = |\omega_\Gamma(e_i, e_j)| / |\gamma_{ij}|$ is the normalized projection of the coherence onto the octonionic product structure. $\blacksquare$
:::

---

## 8. Stabilizers and topological protection {#стабилизаторы}

The stabilizer of a Gap configuration determines topological protection against continuous deformations.

:::tip Theorem 8.1 (Stabilizer classification) [Т]
For the Gap operator $\hat{\mathcal{G}}$ with fixed spectrum $\{0, \pm i\lambda_1, \pm i\lambda_2, \pm i\lambda_3\}$, the stabilizer $H_{\hat{\mathcal{G}}} = \{g \in G_2 : g\hat{\mathcal{G}}g^{-1} = \hat{\mathcal{G}}\}$:

| Rank | Spectrum of $\hat{\mathcal{G}}$ | $H$ | $\dim(H)$ | $G_2/H$ | $\pi_1(G_2/H)$ |
|------|---------------------------|-----|-----------|---------|-----------------|
| 0 | $(0,0,0)$ | $G_2$ | 14 | $\{pt\}$ | 0 |
| 1 | $(\lambda,0,0)$ | $\mathrm{SU}(3)$ | 8 | $S^6$ | 0 |
| 2 | $(\lambda_1,\lambda_2,0)$ | $\mathrm{SU}(2) \times \mathrm{U}(1)$ | 4 | 10-dim. | 0 |
| 3 (generic) | $(\lambda_1,\lambda_2,\lambda_3)$ | $T^2$ | 2 | 12-dim. | $\mathbb{Z}^2$ |
| 3 (degen.) | $(\lambda,\lambda,\lambda)$ | $\mathrm{SU}(2)$ | 3 | 11-dim. | 0 |
:::

**Corollary.** Only at rank 3 with generic spectrum is the second homotopy group $\pi_2(G_2/T^2) \cong \mathbb{Z}^2 \neq 0$, which provides **topological protection**: nondegenerate Gap configurations cannot be continuously contracted to trivial ones ($G_2$ is simply connected, so $\pi_1(G_2/T^2) = 1$; the nontrivial invariant lives in $\pi_2$, equal to $\pi_1(T^2) = \mathbb{Z}^2$). This is one of the [five types of Gap protection](/docs/core/dynamics/gap-phase-diagram#защита-gap).

---

## 9. Gap dynamics from octonionic non-associativity [Т] {#gap-от-неассоциативности}

The octonionic associator is the fundamental source of Gap dynamics. This section derives the explicit contribution of non-associativity to the evolution of Gap.

:::tip Theorem 9.1 (Associator contribution to Gap dynamics) [Т]

For three dimensions $(i,j,k)$ **not** on a common Fano line, the octonionic associator

$$[e_i, e_j, e_k] := (e_i \cdot e_j) \cdot e_k - e_i \cdot (e_j \cdot e_k)$$

is non-zero and contributes to the phase dynamics of coherences:

$$\frac{d\theta_{ij}}{d\tau}\bigg|_{\text{assoc}} = \omega_0 \sum_{k \notin \text{line}(i,j)} \mathrm{Im}\left(\frac{[e_i, e_j, e_k]}{\|[e_i, e_j, e_k]\|}\right) \cdot |\gamma_{ik}| \cdot |\gamma_{jk}|$$

where $\theta_{ij} = \arg(\gamma_{ij})$ and the sum runs over the 4 dimensions $k$ that do **not** share a Fano line with $(i,j)$.
:::

**Proof.**

**Step 1 (Associator structure).** In the octonions, the associator vanishes for triples on a Fano line (Artin's theorem: $\mathbb{O}$ is alternative, so any two elements generate an associative subalgebra $\cong \mathbb{H}$). For triples $(i,j,k)$ NOT on a Fano line:

$$[e_i, e_j, e_k] = \pm 2 e_l$$

where $l$ is determined by the Fano plane structure (standard octonion algebra, Baez 2002). The factor 2 arises from the alternating property.

**Step 2 (Fano line count).** Each pair $(i,j)$ lies on **exactly one** Fano line containing a third element $k_0$. The remaining 4 elements $k \in \{1,\ldots,7\} \setminus \{i,j,k_0\}$ are NOT on the $(i,j)$-line. For each such $k$, the associator $[e_i, e_j, e_k] \neq 0$.

**Step 3 (Phase contribution).** The unitary part of the evolution $-i[H_{\text{eff}}, \Gamma]$ generates phase rotation of coherences: $d\theta_{ij}/d\tau = \Delta\omega_{ij}$ (frequency detuning). The Hamiltonian $H_{\text{eff}}$ contains terms from the octonionic multiplication table. For triples outside Fano lines, the non-associativity introduces **additional** phase terms proportional to the associator magnitude and the coherence amplitudes of the third-party connections $|\gamma_{ik}|$, $|\gamma_{jk}|$.

**Step 4 (Gap dynamics).** Since $\mathrm{Gap}(i,j) = |\sin\theta_{ij}|$, the rate of change:

$$\frac{d\,\mathrm{Gap}(i,j)}{d\tau} = |\cos\theta_{ij}| \cdot \frac{d\theta_{ij}}{d\tau}$$

The associator contribution (Step 3) adds a **positive** term to $|d\theta_{ij}/d\tau|$ for triples outside Fano lines, driving $\theta_{ij}$ away from 0 and $\pi$ (where Gap = 0). This means:

- **On Fano lines:** associator = 0, no additional phase drift → Gap can be zero (associative subalgebra)
- **Off Fano lines:** associator ≠ 0, phase drift → Gap > 0 is dynamically maintained

This provides a **microscopic mechanism** for Lawvere incompleteness (T-55 [Т]): the non-associativity of octonions **structurally prevents** full phase alignment, ensuring Gap > 0 for any viable system. $\blacksquare$

:::warning Physical consequence
Non-associativity is not a mathematical curiosity — it is the **engine of the explanatory gap**. The fact that $(e_i \cdot e_j) \cdot e_k \neq e_i \cdot (e_j \cdot e_k)$ for off-line triples means that triple interactions **cannot be decomposed** into sequences of pairwise ones. This irreducible triplicity is the mathematical source of the [Map splitting](/docs/consciousness/foundations/two-aspect-monism) (T-186 [Т]): the internal and external descriptions cannot be simultaneously exact because the algebraic structure itself forbids full associativity.
:::

**Numerical example.** For the triple (A,E,U) = (e₁,e₅,e₆), which is a Fano line: $[e_1, e_5, e_6] = 0$ (associative subalgebra). For the triple (A,E,D) = (e₁,e₅,e₃), which is NOT a Fano line: $[e_1, e_5, e_3] = \pm 2e_l \neq 0$, contributing a phase shift of order $2\omega_0 |\gamma_{13}| \cdot |\gamma_{53}|$ to $d\theta_{15}/d\tau$.

---

## Related documents

- [Gap dynamics](/docs/core/dynamics/gap-dynamics) — bifurcations, non-Markovian effects, Choi–Jamiołkowski
- [Gap thermodynamics](/docs/core/dynamics/gap-thermodynamics) — Fisher metric, Lagrangian, T_eff
- [Gap phase diagram](/docs/core/dynamics/gap-phase-diagram) — three phases, Whitney catastrophes
- [Dual-aspect Gap semantics](/docs/physics/dual-aspect/gap-semantics) — 49-element map
- [G₂ structure](/docs/physics/gauge-symmetry/g2-structure) — G₂ = $\mathrm{Aut}(\mathbb{O})$
- [Proofs: Fano channel](/docs/proofs/gap/fano-channel) — rigorous theorems on G₂-covariance
