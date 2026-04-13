---
sidebar_position: 1
title: "Gap Semantics: 49 Elements"
description: "Dual-aspect semantics of the coherence matrix: 49 elements, exterior and interior, gap measure"
---

# Gap Semantics: 49 Elements

:::info Who This Chapter Is For
Complete semantics of the 49 elements of the coherence matrix. The reader will learn how the super-diagonal and sub-diagonal elements carry distinct semantics of the exterior and interior aspects.
:::


## Problem Statement

The coherence matrix $\Gamma \in \mathbb{C}^{7 \times 7}$ is Hermitian. The standard interpretation: 7 populations (diagonal) + 21 "pairs" of coherences (upper triangle), related to the lower via $\gamma_{ij} = \gamma_{ji}^*$. The conventional approach treats $\gamma_{ij}$ and $\gamma_{ji}$ as "the same" coherence written from two sides.

:::warning Thesis
This approach loses fundamental information. In the context of UHM, where every entity has both an exterior ($\mathrm{Map}_{\mathrm{ext}}$) and an interior ($\mathrm{Map}_{\mathrm{int}}$) aspect, the super-diagonal and sub-diagonal elements carry **distinct semantics**:

- **Super-diagonal $\gamma_{ij}$ ($i < j$):** exterior aspect of coherence — how the connection of dimensions $i \leftrightarrow j$ appears to an external observer
- **Sub-diagonal $\gamma_{ji}$ ($j > i$):** interior aspect of the same coherence — how the connection is represented from the system's own side (conjugate projection)

Hermitian conjugation $*: \gamma_{ij} \mapsto \gamma_{ji}$ is the **duality functor**, translating the exterior description into the interior. The matrix of 49 cells is the complete map of the entity's being: 7 populations + 21 exterior projections + 21 interior projections.
:::

---

## Mathematical Foundation

### Coherence Decomposition

Any off-diagonal element $\gamma_{ij}$ ($i \neq j$) is a complex number:

$$
\gamma_{ij} = |\gamma_{ij}| \cdot e^{i\theta_{ij}} = \underbrace{\mathrm{Re}(\gamma_{ij})}_{\text{symmetric part}} + i \underbrace{\mathrm{Im}(\gamma_{ij})}_{\text{directed part}}
$$

Hermiticity $\Gamma^\dagger = \Gamma$ means $\gamma_{ji} = \gamma_{ij}^*$, giving:

| Component | Property | Semantics |
|---|---|---|
| $\lvert\gamma_{ij}\rvert = \lvert\gamma_{ji}\rvert$ | Moduli are equal | The coupling strength is the same for exterior and interior |
| $\mathrm{Re}(\gamma_{ij}) = \mathrm{Re}(\gamma_{ji})$ | Real parts are equal | **Common**: what coincides between exterior and interior |
| $\mathrm{Im}(\gamma_{ij}) = -\mathrm{Im}(\gamma_{ji})$ | Imaginary parts are opposite | **Gap**: what distinguishes exterior from interior |
| $\arg(\gamma_{ij}) = -\arg(\gamma_{ji})$ | Phases are opposite | The direction of the "duality arrow" is reversed for exterior and interior projections |

### Theorem 2.1: Hermitian Conjugation as Dual-Aspect Functor

:::info Interpretation / postulate [I]
The identification "upper triangle = $\mathrm{Map}_{\mathrm{ext}}$, lower = $\mathrm{Map}_{\mathrm{int}}$" is a semantic interpretation of the mathematical structure (Hermiticity), not a derivable theorem. Hermiticity is a property of any density matrix; the dual interpretation is an additional UHM postulate.
:::

Let $\Gamma \in \mathrm{Ob}(\mathcal{C})$ be the coherence matrix in the $\infty$-topos $\mathrm{Sh}_\infty(\mathcal{C})$. Then Hermitian conjugation $*$ realizes the duality functor:

$$
*: \mathrm{Map}_{\mathrm{ext}}(i, j) \longrightarrow \mathrm{Map}_{\mathrm{int}}(j, i)
$$

satisfying:

1. **Involutivity:** $** = \mathrm{id}$ (exterior of interior = reverse exterior)
2. **Modulus preservation:** $|*(\gamma_{ij})| = |\gamma_{ij}|$ (coupling strength is invariant under perspective)
3. **Phase reversal:** $\arg(*(\gamma_{ij})) = -\arg(\gamma_{ij})$ (the "inside" perspective inverts the phase orientation)

**Argument.** In UHM every map $\mathrm{Map}(\Gamma, \Omega)$ splits into exterior and interior components:

$$
\mathrm{Map}(\Gamma, \Omega) \simeq \mathrm{Map}_{\mathrm{ext}}(\Gamma, \Omega) \oplus \mathrm{Map}_{\mathrm{int}}(\Gamma, \Omega)
$$

For the matrix element $\gamma_{ij} = \langle i|\Gamma|j\rangle$:
- $\langle i|\Gamma|j\rangle$ — "how state $|j\rangle$ projects onto $|i\rangle$" (exterior: observer in basis $|i\rangle$ measures $|j\rangle$)
- $\langle j|\Gamma|i\rangle = \gamma_{ij}^*$ — "how state $|i\rangle$ projects onto $|j\rangle$" (interior: same interaction, but from the perspective of $|j\rangle$)

Hermiticity guarantees that both aspects describe **the same reality**, but from **two perspectives**. $\blacksquare$

### Gap Measure for Each Pair

**Definition.** The Gap between the exterior and interior aspects of coherence $\gamma_{ij}$:

$$
\mathrm{Gap}(i,j) := \frac{|\mathrm{Im}(\gamma_{ij})|}{|\gamma_{ij}|} = |\sin(\arg(\gamma_{ij}))| \in [0, 1]
$$

**Interpretation:**

- **Gap = 0** ($\gamma_{ij} \in \mathbb{R}$): complete transparency. Exterior and interior projections coincide. No hidden content.
- **Gap = 1** ($\gamma_{ij} \in i\mathbb{R}$): maximal opacity. Exterior and interior aspects are fully orthogonal.
- **Gap $\in (0, 1)$**: partial gap — the norm for systems with non-zero imaginary part of coherences.

:::note Level-dependent semantics
The structural interpretation of Gap is universal (applicable to any holon from atom to social system). The phenomenological interpretation depends on the [level of interiority](/docs/consciousness/hierarchy/interiority-hierarchy):
- **L0–L1** (atom, molecule, cell): Gap describes phase asymmetry without subjective content
- **L2+** (organisms with CNS): Gap correlates with mismatch between observable behaviour and subjective experience (alexithymia, dissociation, etc.)
:::

### Quantum Probability Current Between Dimensions

**Theorem 2.2 (Inter-Dimensional Probability Current) [T].**

For a pair of dimensions $(i, j)$ the probability current is defined by:

$$
J_{i \leftarrow j} = \frac{2}{\hbar} \, \mathrm{Im}(H_{ij} \cdot \gamma_{ji}) = \frac{2}{\hbar} \, \mathrm{Im}(H_{ij} \cdot \gamma_{ij}^*)
$$

$$
J_{\mathrm{net}}(i,j) = 2|H_{ij}| \cdot |\gamma_{ij}| \cdot \sin(\alpha_{ij} - \theta_{ij})
$$

where $\alpha_{ij} = \arg(H_{ij})$, $\theta_{ij} = \arg(\gamma_{ij})$.

**Corollaries:**

1. **Current direction** is determined by the phase difference $(\alpha - \theta)$:
   - $\sin(\alpha - \theta) > 0$: current flows from $j$ to $i$ (dimension $i$ "receives" from $j$)
   - $\sin(\alpha - \theta) < 0$: current flows from $i$ to $j$
   - $\sin(\alpha - \theta) = 0$: equilibrium, no current

2. **Under unitary evolution** the phase rotates:

$$
\theta_{ij}(\tau) = \theta_{ij}(0) + (\omega_i - \omega_j) \cdot \tau
$$

where $\omega_i, \omega_j$ are the Hamiltonian eigenfrequencies. The current **oscillates** with frequency $|\omega_i - \omega_j|$.

3. **Normalisation is preserved:**

$$
\frac{d}{d\tau} \mathrm{Tr}(\Gamma) = 0 \quad \Rightarrow \quad \sum_{j \neq i} J_{\mathrm{net}}(i,j) = -\frac{d\gamma_{ii}}{d\tau}\bigg|_{\text{unitary}}
$$

This is the continuity equation: what leaves population $\gamma_{ii}$ is distributed across currents to other dimensions.

---

## Octonionic Non-Commutativity as the Source of Phase Asymmetry

### Anticommutator and Phase

Octonionic multiplication:

$$
e_i \cdot e_j = -\delta_{ij} + \varepsilon_{ijk} \, e_k
$$

Non-commutativity:

$$
e_i \cdot e_j - e_j \cdot e_i = 2\varepsilon_{ijk} \, e_k \neq 0 \quad \text{(for } i \neq j\text{)}
$$

This means that **the order of factors matters**: the product $e_i \cdot e_j$ and $e_j \cdot e_i$ differ in the sign of the antisymmetric part. This is precisely why $\arg(\gamma_{ij}) \neq \arg(\gamma_{ji})$ — the phases of coherences in the "forward" and "reverse" directions are **opposite**. Non-commutative multiplication in $\mathbb{O}$ is the algebraic source of the fact that "the view from outside" and "the view from inside" yield different phase orientations.

In the [coherence matrix](/docs/core/dynamics/coherence-matrix):

$$
\gamma_{ij} - \gamma_{ji} = \gamma_{ij} - \gamma_{ij}^* = 2i \cdot \mathrm{Im}(\gamma_{ij})
$$

:::tip Isomorphism [T]
The antisymmetric part of octonionic multiplication (structure constants $\varepsilon_{ijk}$) maps onto the antisymmetric part of the matrix (imaginary parts of coherences). Octonionic non-commutativity is the **algebraic source** of the gap between exterior and interior.

Moreover, beyond non-commutativity, octonions possess **non-associativity**: $(e_i \cdot e_j) \cdot e_k \neq e_i \cdot (e_j \cdot e_k)$ for non-Fano triplets. This produces a **second, independent source** of Gap — even if all two-point coherences are real, three-point correlations may contain an irreducible phase shift via the associator $[e_i, e_j, e_k]$.
:::

### Fano Triplets: Two Types of Coherences {#разделение-когерентностей}

The Fano plane $\mathrm{PG}(2,2)$ defines 7 triplets. Within each triplet $(e_i, e_j, e_k)$ multiplication is **associative** (subalgebra $\cong \mathrm{Im}(\mathbb{H})$). Between triplets — **non-associative**.

The partition of coherences is determined by the Fano structure at two levels:

**At the pair level (21 = 21).** In the Fano plane $\mathrm{PG}(2,2)$ any two points lie on **exactly one** line. Each of the 7 lines contains $\binom{3}{2} = 3$ pairs, giving $7 \times 3 = 21$ — all 21 dimension pairs belong to some Fano line.

**At the triplet level ($\binom{7}{3} = 35 = 7 + 28$).** Of the 35 possible triples of dimensions, exactly **7 triplets** lie on Fano lines (associative subalgebras $\cong \mathrm{Im}(\mathbb{H})$), and **28 triplets** are non-Fano (non-associative, with non-zero associator $[e_i, e_j, e_k] \neq 0$).

This partition of triplets determines the properties of coherences — for a pair $(i,j)$ the criterion is the associativity of the triplet containing $(i,j)$:

| Property | Coherences within Fano triplets | Coherences with non-associative context |
|---|---|---|
| Algebra | Associative subalgebra $\cong \mathrm{Im}(\mathbb{H})$ | Full non-associativity of octonions |
| Phase characteristic | **Re-dominated** ("transparent") | **Im-dominated** ("opaque") |
| Gap bound | $\mathrm{Gap}_{\mathrm{intra}}(i,j) \leq \frac{1}{2}$ **[✗ — retracted, see below]** | $\mathrm{Gap}_{\mathrm{inter}}(i,j) > 0$ (non-zero from below) |
| Stability | More resistant to decoherence | Less resistant |
| Role | Scaffold of coherent structure | Zones of potential growth and vulnerability |

:::info Terminology note [I]
The terms "transparent" (Re-dominated) and "opaque" (Im-dominated) reflect Gap semantics: the real part $\mathrm{Re}(\gamma_{ij})$ is what is common between exterior and interior, the imaginary part $\mathrm{Im}(\gamma_{ij})$ is the gap. Coherences in associative triplets tend to have small imaginary parts (low Gap), hence they are "more transparent".
:::

#### Map of the 7 Fano Triplets

The specific identification $e_i \leftrightarrow$ dimensions and the standard octonionic structure constants determine:

| # | Triplet | Dimensions | Fano pairs (coherences) | Interpretation |
|---|---|---|---|---|
| 1 | $(e_1, e_2, e_3)$ | A, S, D | $\gamma_{AS}$, $\gamma_{AD}$, $\gamma_{SD}$ | Material block |
| 2 | $(e_1, e_4, e_5)$ | A, L, E | $\gamma_{AL}$, $\gamma_{AE}$, $\gamma_{LE}$ | Cognitive block |
| 3 | $(e_1, e_6, e_7)$ | A, O, U | $\gamma_{AO}$, $\gamma_{AU}$, $\gamma_{OU}$ | Transcendent block |
| 4 | $(e_2, e_4, e_6)$ | S, L, O | $\gamma_{SL}$, $\gamma_{SO}$, $\gamma_{LO}$ | Structural-logical block |
| 5 | $(e_2, e_5, e_7)$ | S, E, U | $\gamma_{SE}$, $\gamma_{SU}$, $\gamma_{EU}$ | Somatic-integrative block |
| 6 | $(e_3, e_4, e_7)$ | D, L, U | $\gamma_{DL}$, $\gamma_{DU}$, $\gamma_{LU}$ | Active-holistic block |
| 7 | $(e_3, e_5, e_6)$ | D, E, O | $\gamma_{DE}$, $\gamma_{DO}$, $\gamma_{EO}$ | Vital-dynamic block |

Each dimension lies on exactly 3 Fano lines, hence $\sum_{p=1}^{7} \Pi_p = 3I$.

#### Theorem on the Fano Gap Bound

:::danger Retracted: Fano Gap Bound [✗]
The original formulation ($\mathrm{Gap} \leq 1/2$ for **all** pairs) has been **refuted**: O-sector Fano pairs (6 of 21) have $\mathrm{Gap}(O,i) \approx 1 > 1/2$ — a direct counterexample.

**Replacement**: sectoral Gap bound **[T]** (T-80): $\mathrm{Gap}(i,j) \leq \bar{\varepsilon} \approx 0.023$ for non-O pairs; $\mathrm{Gap}(O,i) \approx 1$ for O-pairs — [Berry phase](/docs/physics/cosmology-phys/berry-phase#теорема-секторная-gap-граница).

<details>
<summary>Original formulation (historical)</summary>

Let $\gamma_{ij}$ be the coherence between dimensions $i$ and $j$ (identified with imaginary units $e_i, e_j \in \mathrm{Im}(\mathbb{O})$). Then:

**(a)** If $(i, j, k)$ is a Fano triplet (associative case):

$$
\mathrm{Gap}_{\mathrm{intra}}(i,j) \leq \frac{|\varepsilon_{ijk}|}{1 + |\varepsilon_{ijk}|} = \frac{1}{2}
$$

**(b)** If $(i, j)$ belongs to a triplet with non-zero associator (non-associative case):

$$
\mathrm{Gap}_{\mathrm{inter}}(i,j) \geq \frac{|[e_i, e_j, e_k]|}{2 + |[e_i, e_j, e_k]|} > 0
$$

where $[e_i, e_j, e_k] = (e_i \cdot e_j) \cdot e_k - e_i \cdot (e_j \cdot e_k)$ is the associator.
</details>
:::

:::info Correct predictions from the sectoral Gap bound [T] (T-80)
**F1.** The average Gap for non-O coherences (15 pairs) is **strictly below** $\bar{\varepsilon} \approx 0.023$, while O-sector coherences (6 pairs) have $\mathrm{Gap}(O,i) \approx 1$.

**F2.** Connections **within** each block (e.g., $A \leftrightarrow S \leftrightarrow D$) are more conscious (lower Gap) than O-sector connections. The sectoral structure replaces the former division into "intra-Fano" vs "between triplets".

Both predictions are falsifiable given a reliable Gap profile of the subject.
:::

#### $G_2$-Decomposition of the Gap Operator: 14 + 7

The Gap operator $\hat{\mathcal{G}} = \mathrm{Im}(\Gamma)$ is a real antisymmetric matrix, belonging to the Lie algebra $\mathfrak{so}(7)$ (dimension 21). The group $G_2 = \mathrm{Aut}(\mathbb{O}) \subset SO(7)$ has dimension 14, determining the decomposition $21 = 14 + 7$:

| Component | Dimension | Property | Interpretation |
|---|---|---|---|
| $\hat{\mathcal{G}}_{G_2}$ | 14 | Structure-preserving | "Coherent" Gap, compatible with the algebraic structure of $\mathbb{O}$. Does not break [Fano symmetry](/docs/physics/gauge-symmetry/fano-selection-rules) |
| $\hat{\mathcal{G}}_{\perp}$ | 7 | Structure-breaking | "Decoherent" Gap, breaking Fano symmetry. Exactly one "breaking" direction per dimension |

**Corollary.** The Gap profile is fully determined by two components:

1. **$G_2$-Gap** ($\hat{\mathcal{G}}_{G_2}$, 14 parameters): structure-preserving opacity, compatible with the algebraic structure of $\mathbb{O}$.
2. **Breaking Gap** ($\hat{\mathcal{G}}_{\perp}$, 7 parameters): structure-breaking opacity, associated with loss of algebraic structure.

:::info Interpretation [I]
A healthy system has Gap predominantly in the $G_2$-sector (structure-preserving). Pathological Gap is in the $\perp$-sector (structure-breaking). Therapeutic goal: $\hat{\mathcal{G}}_{\perp} \to 0$, leaving $\hat{\mathcal{G}}_{G_2}$ (which can be non-zero and beneficial).

Opacity ($\mathrm{Gap} > 0$) is "entropic ballast": a system with high Gap **loses coherence faster**. Maintaining Gap costs energy — this is a thermodynamic formalisation of "dark coherence".
:::

### Hamming Code H(7,4) and Correlation Stability

7 [dimensions](/docs/core/structure/dimensions) = 4 "information" (A, S, D, L) + 3 "check" (E, O, U).

Parity-check matrix:

$$
H = \begin{pmatrix} 1 & 0 & 1 & 0 & 1 & 0 & 1 \\ 0 & 1 & 1 & 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 1 & 1 & 1 & 1 \end{pmatrix}
$$

:::info Status note [I]
The analogy with Hamming code H(7,4) is motivational, but no formal identification of coherence dynamics with a block code has been established. In particular: (a) the Hamming code operates over $\mathrm{GF}(2)$, while coherences are continuous complex quantities; (b) the "syndrome" via $(\Delta\gamma_{iE}, \Delta\gamma_{iO}, \Delta\gamma_{iU})$ is not formally defined; (c) the Hamming bound is applied by analogy, not rigorously. Status of all results: **[I]** (interpretation/analogy).
:::

#### Fano Structure and Hamming

The Fano structure defines the **coherence scaffold** of the system. 4 information bits (A, S, D, L) carry content, 3 check bits (E, O, U) ensure integrity. Fano triplets set the rules by which check dimensions are connected to information ones:
- Each check dimension participates in certain triplets with information dimensions
- A coherence violation in an information channel "manifests" as an anomaly in the check coherences $\gamma_{iE}, \gamma_{iO}, \gamma_{iU}$

Correlation stability is determined by the minimum code distance $d = 3$:
- The system can **detect** a violation in 2 coherences
- The system can **correct** a violation in 1 coherence

**Practical corollary:** In diagnostics it is sufficient to restore **one** violated coherence — the system will automatically correct the rest through the self-modelling mechanism $\varphi$.

:::warning Warning [I]
When $\geq 2$ coherences are violated the system **cannot** recover automatically — external correction is required across multiple channels simultaneously.
:::

#### Quantum Hamming Bound for Gap

:::tip Theorem (quantum Hamming bound for Gap) [I]
The number of simultaneously "transparent" channels ($\mathrm{Gap} \approx 0$) is bounded:

$$
|\{(i,j): \mathrm{Gap}(i,j) < \varepsilon\}| \leq 21 - 3 = 18
$$

At least **3 coherences** out of 21 **must** have non-zero Gap. This corresponds to the 3 check bits of H(7,4).
:::

**Interpretation.** At least 3 Gaps out of 21 are fundamentally non-zero — the system **must** maintain a non-zero gap between exterior and interior in at least 3 channels. This is the "price" of error resistance: **complete transparency is incompatible with error correction**.

---

## The Complete 49-Cell Map {#полная-49-клеточная-карта}

### Diagonal: 7 Populations

Common to exterior and interior ($\gamma_{ii} \in \mathbb{R}$, Gap = 0):

| Element | Dimension | Exterior manifestation | Interior aspect | L2+ phenomenology |
|---|---|---|---|---|
| $\gamma_{AA}$ | [Articulation](/docs/core/structure/dimension-a) | Communicative activity | Degree of differentiation of inner space | Clarity of distinction |
| $\gamma_{SS}$ | [Structure](/docs/core/structure/dimension-s) | Physical stability | Structural connectedness of components | Sense of stability |
| $\gamma_{DD}$ | [Dynamics](/docs/core/structure/dimension-d) | Observable activity | Intensity of internal processes | Sense of energy |
| $\gamma_{LL}$ | [Logic](/docs/core/structure/dimension-l) | Cognitive productivity | Degree of consistency of internal rules | Sense of mental clarity |
| $\gamma_{EE}$ | [Interiority](/docs/core/structure/dimension-e) | Emotional reactivity | Integration of interior states | Depth of experience |
| $\gamma_{OO}$ | [Foundation](/docs/core/structure/dimension-o) | Vital force | Connection to the resource source | Sense of groundedness |
| $\gamma_{UU}$ | [Unity](/docs/core/structure/dimension-u) | Behavioural integration | Degree of global connectedness | Sense of wholeness |

:::note
For the diagonal Gap = 0 identically, since $\gamma_{ii} \in \mathbb{R}$. Population is the one thing that fully coincides between the exterior and interior projections. This is why "energy level" is the most objective (perspective-invariant) measure. The "L2+ phenomenology" column applies only to systems of level L2 and above (organisms with CNS).
:::

### Upper Triangle: 21 Exterior Projections ($\mathrm{Map}_{\mathrm{ext}}$)

How the connection between dimensions **appears** to an observer. Observable behaviour, measurable correlations, objective indicators.

:::note Level-dependent interpretation
Descriptions in the "Exterior manifestation" column are formulated in terms universal for all holons (from atom to social system). The names of coherences (Affection, Evidence, etc.) reflect the categorical semantics of the morphism Hom(i,j) and are used as cross-domain labels.
:::

| $\gamma_{ij}$ | Pair | Name | Exterior manifestation |
|---|---|---|---|
| $\gamma_{AS}$ | A$\leftrightarrow$S | Morphogenesis | Form-giving: distinctions crystallise into observable structures |
| $\gamma_{AD}$ | A$\leftrightarrow$D | Actualisation | Initiation: a distinction actualises into an observable process |
| $\gamma_{AL}$ | A$\leftrightarrow$L | Predication | Classification: a distinction becomes a logical predicate |
| $\gamma_{AE}$ | A$\leftrightarrow$E | Apperception | Awareness: a distinction enters interiority |
| $\gamma_{AO}$ | A$\leftrightarrow$O | Spontaneity | Emergence of new distinctions from the foundation without external cause |
| $\gamma_{AU}$ | A$\leftrightarrow$U | Differentiation | Analysis: decomposition of the whole into observable parts |
| $\gamma_{SD}$ | S$\leftrightarrow$D | Persistence | Homeostasis: observable preservation of form through process |
| $\gamma_{SL}$ | S$\leftrightarrow$L | Nomos | Lawfulness: observable logical necessity of structure |
| $\gamma_{SE}$ | S$\leftrightarrow$E | Representation | Psychophysics: measurable representation of structure in interiority |
| $\gamma_{SO}$ | S$\leftrightarrow$O | Archetype | Invariant: stable patterns preserved over time |
| $\gamma_{SU}$ | S$\leftrightarrow$U | Symmetry | Harmony: observable proportionality of parts within the whole |
| $\gamma_{DL}$ | D$\leftrightarrow$L | Regulation | Control: observable adherence of process to logical rules |
| $\gamma_{DE}$ | D$\leftrightarrow$E | Affection | Expression: observable action of process on interiority |
| $\gamma_{DO}$ | D$\leftrightarrow$O | Genesis | Creativity: observable generation of novelty from depth |
| $\gamma_{DU}$ | D$\leftrightarrow$U | Teleology | Observable directedness of action toward a goal |
| $\gamma_{LE}$ | L$\leftrightarrow$E | Evidence | Insight: observable logical coherence within interiority |
| $\gamma_{LO}$ | L$\leftrightarrow$O | Grounding | Axiom: observable rootedness of logic in the foundation |
| $\gamma_{LU}$ | L$\leftrightarrow$U | Consistency | Non-contradiction: observable logical coherence of the whole |
| $\gamma_{EO}$ | E$\leftrightarrow$O | Immanence | Observable presence of the foundation within interiority |
| $\gamma_{EU}$ | E$\leftrightarrow$U | Synthesis | Observable integration of interior content into the whole |
| $\gamma_{OU}$ | O$\leftrightarrow$U | Wholeness | Completeness: observable self-sufficiency of the system |

### Lower Triangle: 21 Interior Projections ($\mathrm{Map}_{\mathrm{int}}$)

The conjugate projection of the same coherence — how the connection is represented from the system's own side. Mathematically: $\gamma_{ji} = \gamma_{ij}^*$ (Hermitian conjugation inverts the phase, preserving the modulus).

:::note Level-dependent interpretation
The "Interior aspect" column describes the structural meaning of the conjugate projection, universal for all holons (from atom to social system). The "L2+ phenomenology" column is a subjective interpretation, applicable only to systems of [level L2+](/docs/consciousness/hierarchy/interiority-hierarchy) (organisms with CNS).
:::

| $\gamma_{ji}$ | Pair | Name | Interior aspect | L2+ phenomenology |
|---|---|---|---|---|
| $\gamma_{SA}$ | S$\to$A | Filter | Structural constraints on the space of distinctions | "My habits constrain my distinctions" |
| $\gamma_{DA}$ | D$\to$A | Flow | Dynamic processes reveal new distinctions | "The process itself discloses the new" |
| $\gamma_{LA}$ | L$\to$A | Frame | Logical rules determine available distinctions | "Logic determines what I am able to distinguish" |
| $\gamma_{EA}$ | E$\to$A | Expression | Interior states seek expression | "Experience demands expression" |
| $\gamma_{OA}$ | O$\to$A | Calling | Basic patterns modulate articulation | "Something deep drives toward distinction" |
| $\gamma_{UA}$ | U$\to$A | Intuition of the whole | Global connectedness directs articulation | "The whole hints where to direct attention" |
| $\gamma_{DS}$ | D$\to$S | Formation | Dynamic process generates new structure | "The process creates new structure" |
| $\gamma_{LS}$ | L$\to$S | Construction | Logical rules determine the form of organisation | "Rules determine the form of being" |
| $\gamma_{ES}$ | E$\to$S | Psychosomatics | Interior states influence structure | "Experiences affect the body" |
| $\gamma_{OS}$ | O$\to$S | Manifestation | Basic patterns determine morphology | "Something deep determines form" |
| $\gamma_{US}$ | U$\to$S | Embodiment | Global connectedness expresses through concrete form | "Wholeness is embodied in form" |
| $\gamma_{LD}$ | L$\to$D | Governance | Logical rules direct dynamics | "Logic governs actions" |
| $\gamma_{ED}$ | E$\to$D | Motivation | Interior states activate dynamics | "Experience drives to action" |
| $\gamma_{OD}$ | O$\to$D | Impulse | Basic patterns initiate dynamic processes | "Something deep generates movement" |
| $\gamma_{UD}$ | U$\to$D | Mission | Global connectedness directs action | "The whole directs actions" |
| $\gamma_{EL}$ | E$\to$L | Insight | Interior states crystallise into rules | "Experience crystallises into understanding" |
| $\gamma_{OL}$ | O$\to$L | Self-evidence | Basic patterns precede logical inference | "Some truths are given before reasoning" |
| $\gamma_{UL}$ | U$\to$L | Harmony | Global connectedness sets internal logic | "The whole sets the logic" |
| $\gamma_{OE}$ | O$\to$E | Revelation | Basic patterns generate interior states | "From depth comes an unplanned experience" |
| $\gamma_{UE}$ | U$\to$E | Integration of experience | Global connectedness modulates interior states | "Wholeness is experienced as a special quality" |
| $\gamma_{UO}$ | U$\to$O | Return | Global connectedness and source close the loop | "Whole and source are one" |

### Theorem 4.1: Principle of the Conjugate Pair

:::info Interpretation [I]
The principle of the conjugate pair is a semantic statement (interpretation of the modulus as "common", the phase as "perspective"), not a mathematical theorem. The mathematical content is a trivial consequence of the polar decomposition of a complex number.
:::

For each coherence $\gamma_{ij}$:

$$
\underbrace{\gamma_{ij}}_{\text{exterior}} = \underbrace{|\gamma_{ij}|}_{\text{common}} \cdot \underbrace{e^{i\theta}}_{\text{perspective}}, \qquad \underbrace{\gamma_{ji}}_{\text{interior}} = \underbrace{|\gamma_{ij}|}_{\text{common}} \cdot \underbrace{e^{-i\theta}}_{\text{reverse perspective}}
$$

1. **Modulus** $|\gamma_{ij}|$ — **invariant** of duality: coupling strength does not depend on perspective
2. **Phase** $\theta$ — **perspective index**: the "viewing angle" on the same connection
3. **$\mathrm{Gap}(i,j) = |\sin\theta|$** — measure of mismatch between exterior and interior

**Corollary:** A fully "transparent" system (all $\gamma_{ij} \in \mathbb{R}$) is a theoretical limit in which exterior and interior aspects coincide. This state is equivalent to **Level L4** (unitary consciousness), where $\varphi(\Gamma) = \Gamma$ and all phases vanish.

---

## Phase Diagnostics

### Transparency Map

For a specific system $\Gamma$ we compute $\mathrm{Gap}(i,j) = |\sin(\arg(\gamma_{ij}))|$ for all 21 pairs. The result is a **transparency map**:

- **Green zones** (Gap $\approx 0$): Exterior and interior aspects are aligned.
- **Yellow zones** (Gap $\in (0.3, 0.7)$): Partial misalignment. Zones of potential growth.
- **Red zones** (Gap $\approx 1$): Complete dissociation of exterior and interior.

### Diagnostic Patterns

| Pattern | Gap profile | Interpretation |
|---|---|---|
| **Alexithymia** | $\mathrm{Gap}(S,E) \approx 1$ | Body and experience are severed: patient does not feel the body |
| **Splitting neurosis** | $\mathrm{Gap}(L,E) \approx 1$ | Logic and experience are severed: understands everything but feels nothing |
| **Impulsivity** | $\mathrm{Gap}(D,L) \approx 1$ | Action and logic are severed: acts without reflection |
| **Existential crisis** | $\mathrm{Gap}(O,U) \approx 1$ | Source and whole are severed: loss of meaning |
| **Authenticity** | $\mathrm{Gap}(A,O) \approx 0$ | Distinction and foundation are aligned: words = essence |
| **Wisdom** | $\mathrm{Gap}(L,O) \approx 0$ | Logic and foundation are aligned: understanding is grounded |

### Extended Diagnostic Example

> **Subject**: high $|\gamma_{LE}|$ (strong logic–experience connection), but $\arg(\gamma_{LE}) \approx \pi/2$ (Gap $\approx 1$).
>
> **Exterior** ($\gamma_{LE}$): Observer sees moments of insight — the person "understands".
> **Interior** ($\gamma_{EL}$): Subject feels that experiences do not become understanding. Knowledge is there, feelings are there, but there is a wall between them.
>
> **Diagnosis:** Intellectualisation of affect. Maximum gap at maximum coupling strength — energy is spent maintaining the rupture.
>
> **Correction:** Practices that unite logic and experience (body-oriented therapy, koan practice in Zen). Goal: $\arg(\gamma_{LE}) \to 0$, keeping $|\gamma_{LE}|$ high.

---

## Phase Prognostics

### Phase Evolution and Gap Oscillation

Under unitary evolution the phase of a coherence rotates:

$$
\theta_{ij}(\tau) = \theta_{ij}(0) + (\omega_i - \omega_j) \cdot \tau
$$

This means that **Gap oscillates** with frequency $|\omega_i - \omega_j|$:

$$
\mathrm{Gap}(i,j;\tau) = |\sin(\theta_{ij}(0) + \Delta\omega_{ij} \cdot \tau)|
$$

**Practical corollaries:**

1. **Transparency windows:** Periods when $\mathrm{Gap}(i,j) \approx 0$. At these moments exterior and interior are aligned — optimal time for awareness, therapy, decision-making.

2. **Turbulence zones:** Periods when $\mathrm{Gap}(i,j) \approx 1$. Maximal misalignment — risk of disorientation, but also potential for deep transformation (crisis = opportunity).

3. **Phase resonances:** When several pairs simultaneously pass through Gap $\approx 0$ — a moment of "total clarity" (all channels transparent).

### Dissipation and Regeneration

Beyond unitary rotation:

- **Dissipation** $\mathcal{D}[\Gamma]$: decreases $|\gamma_{ij}|$ (weakens connections), shifts $\theta \to 0$ (erases the distinction of perspectives, but at the cost of losing coherence)
- **Regeneration** $\mathcal{R}[\Gamma, E]$: restores $|\gamma_{ij}|$ to the target value $\varphi(\Gamma)$, sets $\theta \to \theta_{\mathrm{target}}$

:::tip Key distinction [T]
Evolution is **NOT** cyclic. Regeneration through $\varphi(\Gamma)$ creates **spiral** dynamics: each cycle of phase rotation changes the system through self-modelling. The system can "learn" more transparent states.
:::

### Predicting Phase Transitions

**Bifurcation** occurs when:

$$
\lambda_{\max}\left(\frac{\partial^2 P}{\partial \Gamma^2}\right) = 0
$$

At this moment a small perturbation of one coherence can change the entire phase map. This is the analogue of the "critical transit" in astrology, but with exact computation of the moment and bifurcation vector.

---

## Therapeutic Protocol for Gap Correction

### Diagnostic Protocol

**Input:**
1. External measurements (observer): questionnaires, biometrics, behavioural markers — estimation of $\gamma_{ij}$ (upper triangle)
2. Internal reports (subject): introspection, experience scales — estimation of $\gamma_{ji}$ (lower triangle)
3. Computation of $\mathrm{Gap}(i,j)$ for all 21 pairs

**Output:**
- Transparency map (heat map $7 \times 7$)
- Population vector (histogram of 7)
- Current profile (directions of flows between dimensions)

### Prognostic Protocol

1. Estimate current $\Gamma(\tau_0)$
2. Compute effective Hamiltonian $H_{\mathrm{eff}}$ (from context/environment)
3. Integrate $d\Gamma/d\tau$ over the forecast horizon
4. Determine transparency windows, turbulence zones, and bifurcation points

### Correction Protocol

For each red zone (Gap $\approx 1$) define the correction operator:

| Problematic channel | Gap | Corrective practice | Goal |
|---|---|---|---|
| S$\leftrightarrow$E | $\approx 1$ | Body practices (yoga, dance) | $\arg(\gamma_{SE}) \to 0$ |
| L$\leftrightarrow$E | $\approx 1$ | Koan meditation, logotherapy | $\arg(\gamma_{LE}) \to 0$ |
| D$\leftrightarrow$L | $\approx 1$ | GTD, step-by-step planning | $\arg(\gamma_{DL}) \to 0$ |
| A$\leftrightarrow$O | $\approx 1$ | Practice of sincerity, silence | $\arg(\gamma_{AO}) \to 0$ |
| O$\leftrightarrow$U | $\approx 1$ | Contemplation, via negativa | $\arg(\gamma_{OU}) \to 0$ |
| D$\leftrightarrow$E | $\approx 1$ | Sport + mindfulness | $\arg(\gamma_{DE}) \to 0$ |
| A$\leftrightarrow$U | $\approx 1$ | Holistic practices | $\arg(\gamma_{AU}) \to 0$ |

---

## Comparison with Occult Systems [I]

| Parameter | I Ching | Astrology | Human Design | Kabbalah | **UHM Matrix** |
|---|---|---|---|---|---|
| Elements | 64 hexagrams | ~50 (planets $\times$ signs $\times$ houses) | 64 gates, 36 channels | 10 sefirot, 22 paths | **49 cells** (7 + 21 + 21) |
| Duality | Yin/Yang (binary) | Sign/House (discrete) | Type/Profile (discrete) | Sefirah/Path (discrete) | **Phase $\theta \in [0, 2\pi)$** (continuous) |
| Directionality | Implicit | Implicit (aspects) | Partial (channels) | Partial (paths) | **Explicit** ($\mathrm{Im}(\gamma_{ij})$, current $J$) |
| Dynamics | Static | Cyclic | Static | Static | **Evolutionary** ($d\Gamma/d\tau$) |
| Self-correction | No | No | No | No | **Yes** ($\varphi$-operator) |
| Forecast | Symbolic | Symbolic | Descriptive | Symbolic | **Quantitative** (phase trajectories) |
| Falsifiability | No | No | No | No | **Yes** |
| Int/Ext | No | No | No | No | **Yes** ($\mathrm{Map}_{\mathrm{ext}}/\mathrm{Map}_{\mathrm{int}}$) |

### Why UHM Is Strictly Stronger

1. **Formalisation:** Every concept has a mathematical definition, not a symbolic association.
2. **Continuity:** Instead of discrete "types" (12 signs, 64 hexagrams) — a continuous state space with 48 degrees of freedom.
3. **Exterior/interior duality:** No occult system formalises the distinction between the exterior ($\gamma_{ij}$) and interior ($\gamma_{ji}$) projections of a connection. UHM does this through Hermitian conjugation.
4. **Dynamics:** The evolution equation $d\Gamma/d\tau = -i[H,\Gamma] + \mathcal{D}[\Gamma] + \mathcal{R}[\Gamma,E]$ gives exact trajectories, not "transits" by analogy.
5. **Self-correction:** The operator $\varphi$ provides feedback. The system does not merely describe, but points the way to the optimal state.
6. **Falsifiability:** Predictions $\mathrm{Gap}(i,j;\tau)$ are measurable and testable. If the matrix is constructed correctly, forecasts must be confirmed.

### How Traditional Systems "Project" onto $\Gamma$

Each occult system is a **partial projection** of the full 49-cell matrix:

| Occult system | What it sees | What it loses |
|---|---|---|
| **Astrology** | Exterior coherences (upper triangle) via planetary symbolism | Interior aspect (lower triangle), phase dynamics |
| **I Ching** | 6 of 7 dimensions (without U?), binary projection of phase (yin/yang) | Continuity of phase, 7th dimension |
| **Kabbalah** | 10 of 49 elements (sefirot $\approx$ superpositions of dimensions) | Most coherences, dynamics |
| **Human Design** | Hybrid: part of diagonal + part of coherences | Full phase structure, interior aspect |

---

## Conclusions

### Main Result

Hermitian conjugation $\gamma_{ij} = \gamma_{ji}^*$ is not merely a mathematical property, but the **formal expression of the dual-aspect monism of UHM**. The upper triangle = exterior ($\mathrm{Map}_{\mathrm{ext}}$), the lower = interior ($\mathrm{Map}_{\mathrm{int}}$), and the functor $*$ is the bridge between them.

This yields:
- **49 meaningful elements** (not 28): 7 populations + 21 exterior projections + 21 interior projections
- **Gap measure** $\mathrm{Gap}(i,j) = |\sin(\arg(\gamma_{ij}))|$ for each pair
- **Quantum current** $J_{\mathrm{net}}(i,j)$ — directed flow between dimensions
- **Phase prognostics** — prediction of transparency windows and turbulence zones
- **Sectoral Gap bound** [T] (T-80) — sectoral Gap constraints
- **Hamming bound** [I] — at least 3 of 21 coherences must be opaque (the price of error resistance)
- **$G_2$-decomposition** — 14 structure-preserving + 7 structure-breaking Gap directions

### Open Questions

1. **Phase measurement:** How to practically measure $\arg(\gamma_{ij})$? A protocol mapping external observations and internal reports is needed.
2. **Sectoral Gap bound** T-80 [T] — replaces the original Fano bound (X3 [✗]).
3. **Calibration of $H_{\mathrm{eff}}$:** How to determine the effective Hamiltonian for a specific person in a specific context?
4. **Scaling:** Is the 49-element map applicable to collectives (family, organisation, society)?
5. **$G_2$-covariance:** Prove or disprove $G_2$-covariance of the evolution equations. If confirmed — implement $G_2$-reduction of diagnostics (48 parameters $\to$ 34).
6. **Hamming syndrome:** Construct a concrete protocol for computing the "syndrome of violated coherence" from observable data.

---

## Cross-References

- [Coherence matrix](/docs/core/dynamics/coherence-matrix) — formal definition of $\Gamma$ and its properties
- [7 dimensions](/docs/core/structure/dimensions) — semantics of basis states $|A\rangle, |S\rangle, |D\rangle, |L\rangle, |E\rangle, |O\rangle, |U\rangle$
- [Dimension D (Dynamics)](/docs/core/structure/dimension-d) — example of a dimension with exterior/interior aspect
- [G₂-structure](/docs/physics/gauge-symmetry/g2-structure) — octonionic automorphisms and gauge theory of Gap
- [Fano selection rules](/docs/physics/gauge-symmetry/fano-selection-rules) — Fano plane and allowed/forbidden connections
- [Zeta regularisation](/docs/physics/dual-aspect/zeta-regularization) — factorisation over Fano lines and Gap regularisation


---

**Related documents:**
- [Coherence matrix](/docs/core/dynamics/coherence-matrix)
- [Zeta regularisation](/docs/physics/dual-aspect/zeta-regularization)
- [Gap diagnostics](/docs/applied/research/gap-diagnostics)
- [G₂-structure and Fano plane](/docs/physics/gauge-symmetry/g2-structure)
