---
sidebar_position: 7
title: "Gap Operator"
slug: /core/dynamics/gap-operator
description: "Definition of Ĝ = Im(Γ), antisymmetry, spectrum, opacity rank, relation to purity, chosen Dirac norm and the withdrawn curvature bridge, G₂/⊥ decomposition"
---

# Gap Operator

:::info Who this chapter is for
The antisymmetric part of Γ: definition, spectrum, relation to curvature. Assumes familiarity with the [coherence matrix](./coherence-matrix) and basic linear algebra.
:::

This chapter introduces the **Gap operator** $\hat{\mathcal{G}}$ — a mathematical object that precisely measures the **total opacity** of the holon. If the [Gap measure](/docs/core/dynamics/coherence-matrix#мера-зазора) $\mathrm{Gap}(i,j) \in [0,1]$ describes the opacity of a single pair of dimensions, then the Gap operator collects all information about 21 pairs into a single algebraic object with a spectrum, symmetries, and geometric meaning.

The reader will learn:
- What $\hat{\mathcal{G}} = \mathrm{Im}(\Gamma)$ is and why it is antisymmetric
- How the spectrum of $\hat{\mathcal{G}}$ determines the **opacity rank** (from 0 to 3)
- What a chosen Dirac-entry norm establishes and why curvature needs additional data
- How the $G_2$ decomposition separates "healthy" and "pathological" Gap

:::tip Intuitive explanation
Recall the [coherence matrix](./coherence-matrix) $\Gamma$ — it is Hermitian, meaning $\gamma_{ji} = \gamma_{ij}^*$. This means each coherence has a **real** and an **imaginary** part:

- **Real part** $\mathrm{Re}(\gamma_{ij})$ — the aspect in which the external and internal views of the connection **agree**. This is "common ground" — what is accessible both to the observer and to the system itself.
- **Imaginary part** $\mathrm{Im}(\gamma_{ij})$ — the aspect in which they **diverge**. This is the "gap" — the mismatch between how the connection looks "from outside" and how it is felt "from inside."

The Gap operator $\hat{\mathcal{G}} = \mathrm{Im}(\Gamma)$ is a **map of all mismatches at once**. If $\hat{\mathcal{G}} = 0$, the system is fully transparent: external and internal coincide for all pairs. If $\hat{\mathcal{G}} \neq 0$, there are "blind spots" — pairs of dimensions where the system does not "see" itself as the world sees it.

A remarkable fact: $\hat{\mathcal{G}}$ belongs to the Lie algebra $\mathfrak{so}(7)$ — the same algebra that describes rotations in 7-dimensional space. Gap generates a **rotation** of the coherence matrix: strong opacity in pair $(i,j)$ "mixes" dimensions $i$ and $j$.
:::

The Gap operator $\hat{\mathcal{G}}$ is the central object of [Gap dynamics](/docs/core/dynamics/gap-dynamics), formalizing the **antisymmetric part** of the [coherence matrix](/docs/core/dynamics/coherence-matrix) $\Gamma$. It measures the total opacity of the system and belongs to the Lie algebra $\mathfrak{so}(7)$, linking [dual-aspect semantics](/docs/physics/dual-aspect/gap-semantics) with the [G₂ structure](/docs/physics/gauge-symmetry/g2-structure).

<a id="конвенции-gap"></a>

:::warning Gap notation conventions

| Notation | Meaning | Formula |
|-------------|----------|---------|
| $\hat{\mathcal{G}}$ | Gap **operator** | $\hat{\mathcal{G}} = \mathrm{Im}(\Gamma) \in \mathfrak{so}(7)$ |
| $\mathrm{Gap}(i,j)$ | Gap **between dimensions** $i,j$ | $\lvert\sin(\arg(\gamma_{ij}))\rvert$ |
| $\mathcal{G}_{\text{total}}$ | **Total** Gap | $2(\lambda_1^2 + \lambda_2^2 + \lambda_3^2)$ |
| $\mathrm{Gap}_{AB}(i,j)$ | **Inter-holon** Gap | $\lvert\sin(\arg(\gamma_{i^A j^B}))\rvert$ |

In this document $\hat{\mathcal{G}}$ denotes the Gap operator (antisymmetric matrix); $\mathcal{G}_{\text{total}}$ denotes its total magnitude.
:::

#### Convention: vanishing coherence {#конвенция-нулевой-когерентности}

**[D]** At exactly $\gamma_{ij}=0$, the phase is mathematically undefined. At a nonzero entry its argument remains defined even if small. A chosen experimental cutoff $\varepsilon_{\min}$ may exclude weak entries from reporting and assign $\mathrm{Gap}_{\rm op}(i,j):=1$ below the cutoff. That diagnostic convention is discontinuous and does not assert a mathematical limit $|\sin\arg\gamma|\to1$ as $\gamma\to0$: approaching along a real ray gives zero. The exact weighted identity uses the unthresholded phase at nonzero entries, $|G_{ij}|=|\gamma_{ij}|\,|\sin\arg\gamma_{ij}|$, with zero at the zero entry. It generally fails with $\mathrm{Gap}_{\rm op}$ below a nonzero cutoff. Per-pair phase diagnostics depend on the chosen frame; triple products can be rephasing invariant without thereby becoming holonomy of a supplied connection. Phenomenological interpretations of cutoff crossings are [I/H].

---

## 1. Definition {#определение}

### 1.1 Basic definition

:::tip Definition (Gap operator) [T]
For a Hermitian coherence matrix $\Gamma \in \mathcal{D}(\mathbb{C}^7)$, $\Gamma^\dagger = \Gamma$, the **Gap operator** is defined as:

$$
\hat{\mathcal{G}} := \frac{1}{2i}(\Gamma - \Gamma^T) = \mathrm{Im}(\Gamma)
$$

— the entrywise imaginary part, a real skew-symmetric matrix.
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

:::info Necessity of complex Γ [T-132]
At a nonzero coherence, a nonzero phase Gap **requires** a nonzero imaginary part: for $\gamma_{ij} \in \mathbb{R}$ the measure $\mathrm{Gap} = |\sin(\arg(\gamma_{ij}))| = 0$ identically. Details: [T-132 [T]](/docs/proofs/consciousness/operationalization#t-132).
:::

### 1.3 Full table of 21 coherence pairs {#таблица-21-пара}

$\binom{7}{2} = 21$ pairs of dimensions define 21 coherences $\gamma_{ij}$, each lying on exactly one [Fano line](/docs/physics/gauge-symmetry/fano-selection-rules):

| Pair $(i,j)$ | Fano line | Sector | Physical meaning |
|:---:|:---:|:---:|:---|
| $(A,S)$ | $\{A,S,L\}$ | $\mathbf{3}$-$\mathbf{3}$ | Articulation structure |
| $(A,D)$ | $\{O,A,D\}$ | $\mathbf{3}$-$\mathbf{3}$ | Dynamic articulation |
| $(S,D)$ | $\{S,D,E\}$ | $\mathbf{3}$-$\mathbf{3}$ | Structural dynamics |
| $(L,E)$ | $\{L,E,O\}$ | $\bar{\mathbf{3}}$-$\bar{\mathbf{3}}$ | Logic of interiority |
| $(L,U)$ | $\{D,L,U\}$ | $\bar{\mathbf{3}}$-$\bar{\mathbf{3}}$ | Logical unity |
| $(E,U)$ | $\{E,U,A\}$ | $\bar{\mathbf{3}}$-$\bar{\mathbf{3}}$ | **Higgs channel** |
| $(A,L)$ | $\{A,S,L\}$ | $\mathbf{3}$-$\bar{\mathbf{3}}$ | Articulation of logic |
| $(A,O)$ | $\{O,A,D\}$ | $O$-link | Observation of articulation |
| $(L,O)$ | $\{L,E,O\}$ | $O$-link | Logical foundation |
| $(S,E)$ | $\{S,D,E\}$ | $\mathbf{3}$-$\bar{\mathbf{3}}$ | Structure of interiority |
| $(S,O)$ | $\{U,O,S\}$ | $O$-link | Structural foundation |
| $(E,O)$ | $\{L,E,O\}$ | $O$-link | **Regenerative channel** ($\kappa_0$) |
| $(D,U)$ | $\{D,L,U\}$ | $\mathbf{3}$-$\bar{\mathbf{3}}$ | Dynamics of unity |
| $(D,O)$ | $\{O,A,D\}$ | $O$-link | Dynamic foundation |
| $(U,O)$ | $\{U,O,S\}$ | $O$-link | **Clock channel** ($\kappa_0$) |
| $(A,E)$ | $\{E,U,A\}$ | $\mathbf{3}$-$\bar{\mathbf{3}}$ | Articulation of experience |
| $(A,U)$ | $\{E,U,A\}$ | $\mathbf{3}$-$\bar{\mathbf{3}}$ | Articulation of unity |
| $(S,L)$ | $\{A,S,L\}$ | $\mathbf{3}$-$\bar{\mathbf{3}}$ | Structural logic |
| $(S,U)$ | $\{U,O,S\}$ | $\mathbf{3}$-$\bar{\mathbf{3}}$ | Structural unity |
| $(D,E)$ | $\{S,D,E\}$ | $\mathbf{3}$-$\bar{\mathbf{3}}$ | Dynamics of interiority |
| $(D,L)$ | $\{D,L,U\}$ | $\mathbf{3}$-$\bar{\mathbf{3}}$ | Dynamic logic |

:::info Sector membership — axis-triple labels; the $SU(3)$ reading is retracted [✗]
*Corrected 2026-09-25.* The "Sector" column and the list below label pairs by the axis triples $\{A,S,D\}$ and $\{L,E,U\}$ of the decomposition $7 = 1_O \oplus \mathbf{3}_{A,S,D} \oplus \bar{\mathbf{3}}_{L,E,U}$, which is retracted (registry row 48a): no three of the six non-$O$ axes span an $\mathrm{SU}(3)$-invariant subspace, so "$\mathbf{3}$" and "$\bar{\mathbf{3}}$" here are bookkeeping names of axis triples, not colour sectors, and "confinement" and "electroweak" are not their properties. The $\varepsilon$ values are the vacuum pattern of the sector hierarchy, [C at (SV)] (T-216). The "Fano line" column now lists the canonical lines of [$G_2$-structure, §1.2](/docs/physics/gauge-symmetry/g2-structure#12-таблица-фано-линий); it used to list $\{A,S,D\}$ and $\{L,E,U\}$, which are not lines, and to leave six pairs unassigned.

Former split:
- **$\mathbf{3}$-$\mathbf{3}$**: 3 pairs (within the confinement sector), $\varepsilon_{33} \sim 0.06$
- **$\bar{\mathbf{3}}$-$\bar{\mathbf{3}}$**: 3 pairs (within the electroweak sector), $\varepsilon_{\bar{3}\bar{3}} \sim 10^{-17}$
- **$\mathbf{3}$-$\bar{\mathbf{3}}$**: 9 pairs (confinement↔electroweak), $\varepsilon_{3\bar{3}} \approx 0$
- **$O$-links**: 6 pairs ($O$ with the rest), $\varepsilon_O \sim 1$

Every pair lies on exactly one of the seven lines of PG(2,2): three pairs per line, $7 \times 3 = 21$. (An earlier sentence said that the assignment of six pairs to lines "depends on the choice of $G_2$ gauge"; retracted — the lines are fixed by the multiplication table, and $G_2$ does not permute them.)
:::

---

## 2. Algebraic properties {#свойства}

:::tip Theorem 2.1 (Properties of the Gap operator) [T]
**(a)** $\hat{\mathcal{G}}$ is a real **antisymmetric** matrix: $\hat{\mathcal{G}}^T = -\hat{\mathcal{G}}$.

**(b)** The eigenvalues of $\hat{\mathcal{G}}$ are purely imaginary: $\mathrm{spec}(\hat{\mathcal{G}}) \subset i\mathbb{R}$. They come in pairs $(\pm i\lambda_1, \pm i\lambda_2, \pm i\lambda_3, 0)$ with $\lambda_k \in \mathbb{R}$, plus one zero (since $N = 7$ is odd).

**(c)** $\hat{\mathcal{G}} \in \mathfrak{so}(7)$ — an element of the Lie algebra of the rotation group $\mathrm{SO}(7)$. It generates the rotation group via the exponential map $e^{\epsilon\hat{\mathcal{G}}} \in \mathrm{SO}(7)$.

**(d)** Total Gap:

$$
\mathcal{G}_{\text{total}} := \|\hat{\mathcal{G}}\|_F^2 = 2\sum_{i<j} \mathrm{Im}(\gamma_{ij})^2 = 2\sum_{i<j} |\gamma_{ij}|^2 \cdot \mathrm{Gap}(i,j)^2
$$

:::

### Convention for the norm $\mathcal{G}_{\text{total}}$ {#g-total-definition}

:::warning Norm convention [D]
$\mathcal{G}_{\text{total}}$ is defined as the **full** Frobenius norm (counting both pairs $(i,j)$ and $(j,i)$): $\mathcal{G}_{\text{total}} = \|\hat{\mathcal{G}}\|_F^2 = \sum_{i,j} |\hat{\mathcal{G}}_{ij}|^2 = 2\sum_{i<j} \mathrm{Im}(\gamma_{ij})^2$. The factor of 2 is due to the antisymmetry $\hat{\mathcal{G}}_{ji} = -\hat{\mathcal{G}}_{ij}$. This ensures consistency with the purity decomposition $P = P_{\text{sym}} + \mathcal{G}_{\text{total}}$ (Theorem 4.1) and the spectral formula $\mathcal{G}_{\text{total}} = 2(\lambda_1^2 + \lambda_2^2 + \lambda_3^2)$ (Theorem 3.1).
:::

#### Identity with the Dirac operator [T] {#тождество-tr-d2}

:::tip Corollary (Spectral identity)

$$
\mathrm{Tr}(D_{\mathrm{int}}^2) = \omega_0^2 \cdot \mathcal{G}_{\mathrm{total}}
$$

where $D_{\mathrm{int}}$ is the [internal Dirac operator](/docs/core/foundations/spacetime#теорема-спектральная-тройка) (T-53 [T]) with elements $[D_{\mathrm{int}}]_{ij} = \omega_0 \cdot \mathrm{Gap}(i,j) \cdot |\gamma_{ij}| \cdot e^{i\theta_{ij}}$. This identity connects the total Gap to the coefficient $a_2$ of the [spectral action](/docs/physics/gravity/quantum-gravity#теорема-полное-спектральное-действие) (T-65 [T]) and justifies the derivation of the potential [$V_{\mathrm{Gap}}$](/docs/core/dynamics/gap-thermodynamics#вывод-vgap-из-спектрального-действия) from the axioms.
:::

**Proof.** (a) $\hat{\mathcal{G}}^T = \mathrm{Im}(\Gamma)^T$. Since $\mathrm{Im}(\gamma_{ij}) = -\mathrm{Im}(\gamma_{ji})$ (consequence of Hermiticity), we get $\hat{\mathcal{G}}^T = -\hat{\mathcal{G}}$. (b) Standard property of antisymmetric matrices of odd dimension. (c) $\mathfrak{so}(7)$ is the space of antisymmetric $7 \times 7$ matrices. (d) $\|\hat{\mathcal{G}}\|_F^2 = \sum_{ij} |\hat{\mathcal{G}}_{ij}|^2 = 2\sum_{i<j} \mathrm{Im}(\gamma_{ij})^2$ (the factor of 2 from counting both pairs $(i,j)$ and $(j,i)$). $\square$

---

## 3. Spectral interpretation {#спектр}

:::tip Theorem 3.1 (Spectral structure of Gap) [T]
Let $\mathrm{spec}(\hat{\mathcal{G}}) = \{0, \pm i\lambda_1, \pm i\lambda_2, \pm i\lambda_3\}$. Then:

**(a)** $\mathcal{G}_{\text{total}} = \|\hat{\mathcal{G}}\|_F^2 = 2(\lambda_1^2 + \lambda_2^2 + \lambda_3^2)$

**(b)** $\lambda_{\max} = \max(\lambda_1, \lambda_2, \lambda_3)$ determines the **maximum opacity channel**.

**(c)** The number of nonzero $\lambda_k$ determines the **opacity rank** $r \in \{0, 1, 2, 3\}$.
:::

### Opacity rank table

| Rank | $\lambda$-spectrum | Interpretation |
|------|------------------|---------------|
| 0 | $(0, 0, 0)$ | Zero weighted imaginary part; a zero-coherence reporting convention may still give phase Gap 1 |
| 1 | $(\lambda, 0, 0)$ | One-dimensional opacity — one "break channel" |
| 2 | $(\lambda_1, \lambda_2, 0)$ | Two-dimensional opacity |
| 3 | $(\lambda_1, \lambda_2, \lambda_3)$ | Full opacity (maximum rank) |

:::info Remark [I]
The maximum opacity rank = 3 coincides with the number of "check" dimensions (E, O, U) in the [Hamming code H(7,4) analogy](/docs/core/dynamics/gap-dynamics#код-хэмминга). This coincidence connects the algebra of the Gap operator to the coding-theoretic structure.
:::

:::info Connection between Gap rank and the Hamming code
Any real antisymmetric $7\times7$ matrix has rank at most six, with three rotation planes. This follows from skew-symmetry and odd dimension, independently of a Fano structure. The Hamming code H(7,4) separately has three check bits; their numerical equality establishes no dynamical or coding equivalence.
:::

---

## 4. Relation to purity {#связь-чистота}

:::tip Theorem 4.1 (Gap and purity) [T]
The purity of the holon decomposes into symmetric and antisymmetric parts:

$$
P = \mathrm{Tr}(\Gamma^2) = P_{\text{sym}} + \mathcal{G}_{\text{total}}
$$

where $P_{\text{sym}} = \mathrm{Tr}(\mathrm{Re}(\Gamma)^2)$ is the "symmetric purity."
:::

**Corollary.** The total Gap **increases** purity $P$ at fixed $P_{\text{sym}}$: nonzero imaginary parts of coherences make a positive contribution to $\mathrm{Tr}(\Gamma^2)$.

**Proof.** $\mathrm{Tr}(\Gamma^2) = \mathrm{Tr}((\mathrm{Re}(\Gamma) + i\,\mathrm{Im}(\Gamma))^2)$. Expanding: $\mathrm{Tr}(\mathrm{Re}^2) - \mathrm{Tr}(\mathrm{Im}^2) + 2i\,\mathrm{Tr}(\mathrm{Re} \cdot \mathrm{Im})$. Since $P \in \mathbb{R}$ (spectral theorem), the imaginary part vanishes, and $P = \mathrm{Tr}(\mathrm{Re}^2) - \mathrm{Tr}(\mathrm{Im}^2)$. Since $\mathrm{Im}(\Gamma)$ is a real antisymmetric matrix, $\mathrm{Tr}(\mathrm{Im}^2) = -\|\mathrm{Im}(\Gamma)\|_F^2 = -\mathcal{G}_{\text{total}}$. Therefore $P = P_{\text{sym}} + \mathcal{G}_{\text{total}}$. $\square$

---

## 5. Dirac-entry norm and the withdrawn curvature identification {#кривизна-серра}

### T-73: what the identity establishes {#теорема-gap-серра}

Choose a Hermitian matrix $D$ with zero diagonal and

$$
D_{ij}=\omega_0|\operatorname{Im}\gamma_{ij}|e^{i\arg\gamma_{ij}},\quad i\ne j,
$$

setting zero-coherence entries to zero. Then [T at this definition]

$$
|D_{ij}|^2=\omega_0^2|\operatorname{Im}\gamma_{ij}|^2,\qquad \operatorname{Tr}D^2=\omega_0^2\|\operatorname{Im}\Gamma\|_F^2.
$$

For nonzero coherences this is also $\omega_0^2|\gamma_{ij}|^2\mathrm{Gap}(i,j)^2$. The experimental small-coherence cutoff is a reporting convention and does not change this exact matrix identity.

The former **Gap = curvature** and **second Chern number = $\operatorname{Tr}D^2/(8\pi^2\omega_0^2)$** are withdrawn [✗]. A spectral triple does not equate an entry of $D$ with a curvature two-form. One needs a module/bundle, differential calculus, connection $\nabla$ and its curvature $\nabla^2$ (in a chosen calculus, $dA+A^2$); Chern–Weil pairing also needs a cycle and normalization. In finite spectral geometry the differential calculus includes its junk quotient. [Connes, *C* algebras and differential geometry](https://arxiv.org/abs/hep-th/0101093).

There is also a direct obstruction to the proposed Chern identity: the RHS changes continuously under $\Gamma_t=I/7+t(\Gamma-I/7)$, as $t^2\|\operatorname{Im}\Gamma\|^2/(8\pi^2)$. It is not an integral characteristic number. The native density-state space is convex and contractible; every vector bundle over it is topologically trivial and has zero positive-degree Chern classes. Nonzero local curvature can still exist on a trivial bundle, but its choice is additional geometry [D/H].

### Holonomy

Holonomy belongs to a supplied connection and paths. Coordinate phases of $\Gamma$ and invariant triangle products can be specified as numerical observables, but are not automatically the holonomy of a Serre bundle. The proposed bridge remains a research construction [Pr], rather than an exact curvature theorem.

## 6. G₂/⊥ decomposition {#g2-разложение}

The Gap operator $\hat{\mathcal{G}} \in \mathfrak{so}(7)$ decomposes into components associated with the [G₂ structure](/docs/physics/gauge-symmetry/g2-structure).

:::tip Theorem 6.1 (G₂/⊥ decomposition of the Gap operator) [T]
**(a)** $\hat{\mathcal{G}}$ decomposes into the G₂ part and the orthogonal complement:

$$
\hat{\mathcal{G}} = \hat{\mathcal{G}}_{G_2} + \hat{\mathcal{G}}_{\perp}
$$

where $\hat{\mathcal{G}}_{G_2} \in \mathfrak{g}_2 \subset \mathfrak{so}(7)$ is the projection onto the 14-dimensional subalgebra $G_2$, and $\hat{\mathcal{G}}_{\perp} \in \mathfrak g_2^\perp$ is the orthogonal complement (7-dimensional, since $\dim\,\mathfrak{so}(7) = 21$, $\dim\,\mathfrak{g}_2 = 14$).

**(b)** Exponentiating $\hat{\mathcal G}_{G_2}$ preserves the chosen positive three-form and octonion multiplication [T]. It need not preserve the seven coordinate Fano-line projectors individually or as a set; that is a stronger finite-frame condition.

**(c)** A nonzero complementary generator does not infinitesimally preserve the chosen three-form [T]. This describes the chosen algebraic structure, not a derived pathology, flux tube or phenomenological failure.

**(d)** The complement is 7-dimensional: exactly one "breaking" direction per [dimension](/docs/core/structure/dimensions).
:::

The positive three-form and conjugation determine this equivariant decomposition. Preserving the three-form does not preserve a fixed coordinate Fano list; only its frame stabilizer does. The complement is an orthogonal vector subspace, not a quotient matrix Lie algebra. Its therapeutic interpretation is [I/H].

### Two types of Gap

| Component | Dimension | Character | Interpretation |
|------------|-------------|----------|---------------|
| $\hat{\mathcal{G}}_{G_2}$ | 14 | Structure-preserving | "Coherent" Gap, compatible with the algebraic structure of $\mathbb{O}$ |
| $\hat{\mathcal{G}}_{\perp}$ | 7 | Structure-breaking | "Decoherent" Gap, associated with the loss of algebraic structure |

:::info Interpretation (Therapeutic) [I]
A healthy system has Gap predominantly in the $G_2$ sector. Pathological Gap is in the $\perp$ sector. The therapeutic goal: bring $\hat{\mathcal{G}}_{\perp} \to 0$ while leaving $\hat{\mathcal{G}}_{G_2}$ (which may be nonzero and beneficial).
:::

---

## 7. Commutator algebra and cross-product typing {#коммутаторная-алгебра}

### 7.1 Correct adjoints and rotation flow [T]

Write $G=\operatorname{Im}\Gamma$. Then $G$ is real skew-symmetric, hence $G^\dagger=-G$. Consequently $[G,\Gamma]^\dagger=[G,\Gamma]$ and $\operatorname{Tr}[G,\Gamma]=0$. For frozen $G$,

$$
\Gamma(\epsilon)=e^{\epsilon G}\Gamma e^{-\epsilon G}=\Gamma+\epsilon[G,\Gamma]+O(\epsilon^2)
$$

is unitary (indeed real orthogonal) conjugation. The previous anti-Hermitian-commutator statement and $e^{i\epsilon G}$ unitary formula were incorrect [✗]. Equivalently use the Hermitian generator $H=iG$ with $e^{-i\epsilon H}=e^{\epsilon G}$. A state-dependent generator defines a separate nonlinear isospectral ODE.

### 7.2 Scalar two-forms and the octonionic cross product {#октонионное-крестное-произведение}

Choose a positive three-form $\varphi$ and its oriented orthonormal frame [D]. It defines the vector-valued cross product by $\langle x\times y,z\rangle=\varphi(x,y,z)$. The corresponding $G_2$ action is equivariant: $(gx)\times(gy)=g(x\times y)$. In contrast, $G$ is a state-dependent **scalar** two-form/matrix, not the vector-valued product. Covariance of a state under conjugation does not make its entries invariant. The fixed coordinate Fano dissipator has only its declared frame covariance, not automatic continuous $G_2$ covariance.

The representation identity $\Lambda^2\mathbb R^7\simeq\mathbf7\oplus\mathbf{14}$ has no trivial summand, so

$$
\operatorname{Hom}_{G_2}(\Lambda^2\mathbb R^7,\mathbb R)=0.
$$

The former one-dimensional invariant-two-form proof and proportionality $G=c\,\operatorname{Im}(e_i e_j)$ are withdrawn [✗]. Contracting $\varphi$ with a **chosen nonzero vector** gives a two-form preserved by its $SU(3)$ stabilizer, not by all $G_2$. This supplies the seven-dimensional component of $G$ after the form is chosen; it does not eliminate the fourteen-dimensional component. [Baez, *The Octonions*](https://arxiv.org/abs/math/0105155).

## 8. Stabilizers need the representation component {#стабилизаторы}

The spectrum classifies skew matrices up to $SO(7)$ conjugacy, not up to the smaller $G_2$. For $G=G_7+G_{14}$ in the chosen decomposition,

$$
\operatorname{Stab}_{G_2}(G)=\operatorname{Stab}_{G_2}(G_7)\cap\operatorname{Stab}_{G_2}(G_{14}).
$$

The old rank-only table is withdrawn [✗]. For $G=0$ the stabilizer is $G_2$. For a nonzero pure seven-component $G=\iota_v\varphi$, it is $SU(3)_v$; the operator has real rank six, not rank two. For a regular element of $\mathfrak g_2$ with zero seven-component, the stabilizer is a maximal torus $T^2$. Arbitrary sums need the displayed intersection, and can have a discrete stabilizer.

For the specified orbit $G_2/T^2$, the fibration gives $\pi_2(G_2/T^2)\cong\mathbb Z^2$ [T]. This describes maps into that orbit under fixed-spectrum constraints; it does not prevent a state from continuously reducing its Gap. The valid path $I/7+t(\Gamma-I/7)$ sends $G$ to $tG$ and reaches zero. Topological protection requires a field domain, boundary conditions and an admissible homotopy class [H/C].

## 9. Phase dynamics requires a specified vector field {#gap-от-неассоциативности}

For the chosen normed octonion multiplication, a distinct basis triple on a Fano line has zero associator, while an off-line triple has associator $\pm2e_l$ [T]. Each pair lies on one line and has four off-line third axes. These algebraic identities do not determine the density-state evolution.

For a specified Hermitian, trace-preserving vector field $\dot\Gamma=F(\Gamma)$ and a nonzero coherence,

$$
\dot\theta_{ij}=\operatorname{Im}\frac{F_{ij}(\Gamma)}{\gamma_{ij}}.
$$

Away from zeros of $\sin\theta$, the exact derivative is

$$
\frac{d}{d\tau}|\sin\theta|=\operatorname{sgn}(\sin\theta)\cos\theta\,\dot\theta,
$$

which may be negative. At a zero use one-sided derivatives; at zero coherence the phase is undefined. For a diagonal Hamiltonian alone, $\dot\theta_{ij}=-(h_i-h_j)$.

The former T.9.1 phase equation is withdrawn [✗]: its RHS used a vector-valued octonionic imaginary part as a scalar phase rate, supplied no Hamiltonian/coupling derivation, and incorrectly inferred positive Gap drift. Associator couplings must be declared and shown to preserve valid states [D/H]. Octonion nonassociativity does not change associativity of ordinary matrix/channel composition. Real states, zero Hamiltonian, real targets and diagonal dissipators give counterexamples to any universal forced complex phase or opacity; Lawvere's fixed-point theorem supplies no such dynamical implication.

## Related documents

- [Gap dynamics](/docs/core/dynamics/gap-dynamics) — bifurcations, non-Markovian effects, Choi–Jamiołkowski
- [Gap thermodynamics](/docs/core/dynamics/gap-thermodynamics) — Fisher metric, Lagrangian, T_eff
- [Gap phase diagram](/docs/core/dynamics/gap-phase-diagram) — three phases, Whitney catastrophes
- [Dual-aspect Gap semantics](/docs/physics/dual-aspect/gap-semantics) — 49-element map
- [G₂ structure](/docs/physics/gauge-symmetry/g2-structure) — G₂ = $\mathrm{Aut}(\mathbb{O})$
- [Proofs: Fano channel](/docs/proofs/gap/fano-channel) — rigorous theorems on G₂-covariance
