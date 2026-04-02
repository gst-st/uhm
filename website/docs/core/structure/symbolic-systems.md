---
sidebar_position: 10
title: "Formal reduction of symbolic systems"
slug: /core/structure/symbolic-systems
description: "Categorical formulation: symbolic systems as projection functors from Γ. Fundamental analysis of all major symbolic traditions, projection table, completeness theorem, structural conclusions"
---

# Formal Reduction of Symbolic Systems

This chapter shows how all symbolic systems of humanity — from the Indian chakras to Western astrology, from the Chinese I Ching to the Kabbalistic Tree of Life, from alchemy to the Big Five — are **projections of the same mathematical object**: the coherence matrix $\Gamma \in \mathbb{C}^{7 \times 7}$. Each of these systems "sees" a part of $\Gamma$, but none sees the whole. UHM is the first formalism in which all these fragmentary descriptions are united into a single picture.

The reader will learn: why structurally similar descriptive systems arose in different cultures and eras; what exactly each of them "sees" and what it "loses"; and why the number 7 appears in symbolic systems so frequently — from the seven chakras to the seven musical notes and the seven days of the week.

:::warning Status [И]
All material in this section has the status of **interpretation**. The projection formulae $\pi_S$ are constructive, but empirical validation has not been carried out. The identifications "symbol ↔ element of Γ" are substantive hypotheses, not identities.
:::

---

## 1. Fundamental formulation {#фундаментальная-постановка}

### 1.1 What is a symbolic system

**Definition.** A symbolic system $S$ is a structured set of elements $\{s_k\}$ with relations $R_S$, claiming to describe the integral state of an entity (organism, person, event).

From the UHM perspective, any such system is formalised as a **projection functor**:

$$
\pi_S: \text{Hol} \to \mathcal{C}_S
$$

where $\text{Hol}$ is the category of [holons](/docs/core/structure/dimensions) and $\mathcal{C}_S$ is the target category of system $S$ (a finite set of symbols with relations).

:::tip What "projection functor" means in plain language
Imagine a three-dimensional object — say, a sculpture. The shadow of that sculpture on the wall is a **projection**: a two-dimensional image that conveys part of the information about the sculpture (outline, general shapes) but loses depth. Different shadows of the same sculpture (from a lamp on the left, from above, from the front) look different, but they are all projections of the same object.

The projection functor $\pi_S$ works analogously. $\Gamma$ is the "sculpture" (48 parameters). Symbolic system $S$ is the "shadow" (a few parameters). The chakra system sees a "shadow" of 7 elements. Tarot — of 22. Astrology — of ~50. But all of them are "shadows" of the same $\Gamma$. The word "functor" means that the projection preserves structure: if two states are connected in $\Gamma$, they will be connected in the projection as well (though the converse does not hold — a projection may "glue together" different states).
:::

### 1.2 Why projections are inevitable

The full state of a holon is described by the [coherence matrix](/docs/core/dynamics/coherence-matrix) $\Gamma \in \mathbb{C}^{7 \times 7}$ with **48 independent real parameters** (7 populations subject to $\text{Tr} = 1$ give 6; 21 complex coherences give 42; total 48).

Any system with $|S| < 48$ elements **cannot** contain complete information about $\Gamma$. Loss of information is not a defect of the symbolic system but a **consequence of the dimensionality theorem**: a map from $\mathbb{R}^{48}$ to $\mathbb{R}^n$ with $n < 48$ is non-injective.

Analogy: you cannot convey colour (3 numbers: R, G, B) in a single number without loss. If you have only brightness (1 number) — you cannot distinguish red from green of equal brightness. In exactly the same way, a 7-element system (chakras) cannot convey all 48 parameters of $\Gamma$ — it inevitably "glues together" different states, losing coherences.

### 1.3 The fundamental question

Why did structurally similar descriptive systems arise in different cultures and eras? The UHM answer: they all map the same mathematical object — $\Gamma$ — and differ only in their **choice of projection**. Stable systems are those whose projections capture structurally significant subspaces of $\Gamma$.

This answer explains two puzzling facts at once: (1) the **similarity** between distant traditions (Indian chakras and European alchemy both distinguish 7 elements — because both project the 7-dimensional diagonal of $\Gamma$); and (2) the **differences** between them (chakras see populations, Tarot sees coherences — because they project different aspects of $\Gamma$).

### 1.4 The projection uncertainty principle {#принцип-неопределённости-проекции}

:::warning Central methodological limitation [И]
UHM defines the object ($\Gamma \in \mathbb{C}^{7 \times 7}$); symbolic systems are **empirical approximations** to it. The choice of projection $\pi_S$ is **not a mathematical derivation** but an empirical hypothesis.
:::

**The problem.** The matrix $\Gamma$ contains **several** 7-element substructures onto which a 7-element symbolic system can be projected:

| Candidate substructure | Elements | Structure |
|---|---|---|
| Populations (diagonal) | $\gamma_{11}, \ldots, \gamma_{77}$ | Linear order (by index) |
| Fano lines | 7 triplets $\{i, j, k\}$ | Incidence geometry PG(2,2) |
| Projectors $\Pi_p$ | 7 projectors onto Fano subspaces | $G_2$-orbit |
| Spectrum of $\Gamma$ | 7 eigenvalues $\lambda_1, \ldots, \lambda_7$ | Ordered set (by magnitude) |
| Atomic Kraus operators | 7 operators $K_m^{(\mathrm{atom})}$ | Set of classifier atoms |

A bijection $\phi: \mathrm{Obj}(S) \to$ (substructure of Γ) for a symbolic system $S$ with 7 elements can be constructed for **any** of the candidates. However, each choice generates a **different** projection $\pi_S$ with different properties.

**Corollary.** All identifications $\pi_S$ in this document are **constructive hypotheses [И]**, not mathematical derivations [Т]. For each symbolic system:

1. The type of substructure (diagonal, Fano lines, spectrum, …) — **first-order hypothesis**
2. The specific bijection within the chosen type — **second-order hypothesis**
3. Verification requires empirical data (see the [research programme](/docs/applied/research/symbolic-correspondence#программа))

---

## 2. Structure of the coherence matrix as the source of projections {#структура-гаммы}

The matrix $\Gamma$ contains three types of information targeted by different symbolic systems:

| Data type | Elements of $\Gamma$ | Number of parameters | What it describes |
|---|---|---|---|
| **Populations** | $\gamma_{ii}$ (diagonal) | 6 (accounting for $\text{Tr}=1$) | Distribution of "energy" across [dimensions](/docs/core/structure/dimensions) |
| **Coherence moduli** | $\lvert\gamma_{ij}\rvert$ (off-diagonal) | 21 | Strength of connection between dimensions |
| **Coherence phases** | $\theta_{ij} = \arg(\gamma_{ij})$ | 21 | Directedness of connection, [Gap](/docs/core/dynamics/gap-operator) between outer and inner |

Symbolic systems differ in **which of these three types** they are capable of expressing, and with what completeness.

### 2.1 Classification of projections

**Definition.** Projection $\pi_S$ is characterised by a quadruple:

$$
\pi_S = (D_S, \, M_S, \, \Phi_S, \, \text{Res}_S)
$$

where:
- $D_S \subseteq \{1,\ldots,7\}$ — which dimensions the system "sees" (populations)
- $M_S \subseteq \{(i,j): i<j\}$ — which coherence moduli it captures
- $\Phi_S \subseteq M_S$ — for which pairs it distinguishes phase
- $\text{Res}_S \in \{\text{binary}, \text{discrete}, \text{continuous}\}$ — resolving power

---

## 3. Taxonomy of symbolic systems {#таксономия}

### 3.1 Systems based on populations (diagonal of $\Gamma$)

These systems describe the **distribution of energy** among dimensions, ignoring connections (coherences).

#### Chakra system (7 chakras) {#чакры}

:::info The [Projection uncertainty principle](#принцип-неопределённости-проекции) applied
The analysis below demonstrates that the identification of chakras with elements of $\Gamma$ is a **constructive hypothesis** [И], not a mathematical derivation. Several projection candidates and their properties are presented.
:::

##### A. UHM formulation

The chakra system is an ordered set of 7 elements. Question: which 7-element substructures of $\Gamma$ can a system with a **linear order** describe?

| Candidate | Substructure of $\Gamma$ | Natural order? |
|---|---|---|
| Diagonal (populations) | $\gamma_{11}, \ldots, \gamma_{77}$ | By index (conventional) or by magnitude |
| Fano lines | 7 triplets | **No** — incidence geometry, not an order |
| Spectrum of $\Gamma$ | $\lambda_1 \geq \cdots \geq \lambda_7$ | By magnitude (natural) |

##### B. Categorical analysis

The chakra system defines a **thin category** (a category-order):

$$\mathrm{Chak} = (\mathrm{Mu} \leq \mathrm{Sv} \leq \mathrm{Ma} \leq \mathrm{An} \leq \mathrm{Vi} \leq \mathrm{Aj} \leq \mathrm{Sa})$$

This is a linearly ordered set (total order). The dimension space with [Fano structure](/docs/physics/gauge-symmetry/g2-structure) is **not an order**: it is incidence geometry $\mathrm{PG}(2,2)$ with non-linear relations (each point on 3 lines, each line through 3 points).

**Categorical incompatibility.** Any bijection $\phi: \mathrm{Obj}(\mathrm{Chak}) \to \mathrm{Obj}(\mathrm{Dim})$ **destroys** the non-linear Fano structure. A linear order cannot represent projective geometry: of the 7 Fano lines, none, in general, "respects" the order (i.e., none consists of three consecutive elements). This is an **information loss** that is inevitable when projecting from $\mathrm{PG}(2,2)$ to a linear chain.

##### C. Tattva hierarchy

The traditional chakra system carries additional structure: each chakra is assigned an **element** (tattva) forming a hierarchy of subtlety:

$$\text{Earth} \to \text{Water} \to \text{Fire} \to \text{Air} \to \text{Ether} \to \text{Mind} \to \text{Beyond}$$

This is a functor $F: \mathrm{Chak} \to \mathrm{Subtlety}$ into the subtlety category (also a linear order). Question: is there a **natural** subtlety order on $\{A, S, D, L, E, U, O\}$? If so, the mapping of chakras to dimensions must be **monotone** with respect to both orders (the chakra hierarchy and the subtlety hierarchy).

##### D. Boundary constraints

Two identifications have the **strongest functional justification**:

| Chakra | Dimension | Justification |
|---|---|---|
| Muladhara (root, base, support) | $O$ (Ground) | Functional match: nourishment, regeneration, source |
| Sahasrara (crown, thousand-petalled) | $U$ (Unity) | Functional match: integration, wholeness, normalisation |

With $O \leftrightarrow \mathrm{Mu}$ and $U \leftrightarrow \mathrm{Sa}$ fixed, the remaining task is to map the five middle chakras $\{\mathrm{Sv}, \mathrm{Ma}, \mathrm{An}, \mathrm{Vi}, \mathrm{Aj}\}$ onto the five dimensions $\{A, S, D, L, E\}$. Number of possible bijections: $5! = 120$.

##### E. Compatibility analysis

One of the 120 candidates (used in the previous version of this document):

| Chakra | Dimension | Tattva ↔ Function |
|---|---|---|
| 1. Muladhara | $O$ | Earth ↔ Nourishment |
| 2. Svadhisthana | $E$ | Water ↔ Experience |
| 3. Manipura | $D$ | Fire ↔ Dynamics |
| 4. Anahata | $L$ | Air ↔ Connection/Coordination |
| 5. Vishuddha | $A$ | Ether ↔ Articulation |
| 6. Ajna | $S$ | Mind ↔ Structure/Pattern |
| 7. Sahasrara | $U$ | Beyond ↔ Unity |

This candidate (denote it $\phi_0$) induces an order on dimensions: $O < E < D < L < A < S < U$.

**Fano compatibility.** From the 7 [Fano lines](/docs/physics/gauge-symmetry/g2-structure#12-таблица-фано-линий) $\{1,2,4\}, \{2,3,5\}, \{3,4,6\}, \{4,5,7\}, \{5,6,1\}, \{6,7,2\}, \{7,1,3\}$ under mapping $\phi_0$ (A=1, S=2, D=3, L=4, E=5, U=6, O=7) we obtain:

| Fano line | Dimensions ($\phi_0$) | Positions in chakra order |
|---|---|---|
| $\{1,2,4\}$ | $\{A, S, L\}$ | $\{5, 6, 4\}$ — **not** adjacent |
| $\{2,3,5\}$ | $\{S, D, E\}$ | $\{6, 3, 2\}$ — **not** adjacent |
| $\{3,4,6\}$ | $\{D, L, U\}$ | $\{3, 4, 7\}$ — **not** adjacent |
| $\{4,5,7\}$ | $\{L, E, O\}$ | $\{4, 2, 1\}$ — **not** adjacent |
| $\{5,6,1\}$ | $\{E, U, A\}$ | $\{2, 7, 5\}$ — **not** adjacent |
| $\{6,7,2\}$ | $\{U, O, S\}$ | $\{7, 1, 6\}$ — **not** adjacent |
| $\{7,1,3\}$ | $\{O, A, D\}$ | $\{1, 5, 3\}$ — **not** adjacent |

**Not a single** Fano line consists of three consecutive chakras. This confirms the categorical incompatibility (§B): the linear order of chakras is **orthogonal** to the Fano geometry.

##### F. Verification criteria

What could confirm or refute a specific mapping $\phi$?

1. **Correlation test:** If $\phi$ is correct, activation of chakra $k$ should correlate with an increase in population $\gamma_{\phi(k)\phi(k)}$ (measurable via the [Gap-diagnostics protocol](/docs/applied/research/gap-diagnostics))
2. **Tattva monotonicity:** The subtlety order of the tattvas should monotonically correspond to some computable characteristic of the dimensions (e.g., mean coherence or entropy)
3. **Fano neutrality:** Since $\mathrm{Chak}$ is an order and $\mathrm{PG}(2,2)$ is not, a correct $\phi$ **must not** assert correspondences with Fano lines

**Current status:** The mapping $\phi_0$ above is the **most widely discussed candidate**, but empirical verification has not been carried out. Alternative $\phi$ mappings (the remaining 119 bijections) have not been studied systematically.

**What it sees (for any $\phi$):** The complete diagonal — all 7 populations.
**What it loses:** All 42 coherences (21 moduli + 21 phases), the Fano structure, dynamics. It does not describe the *connections* between centres, only their individual "charge."

**Structural observation.** Of all traditional systems, the chakra system is unique in containing **exactly 7 elements** — a number coinciding with the dimensionality of $\Gamma$. This is no coincidence: 7 is the dimensionality of the imaginary octonions $\text{Im}(\mathbb{O})$, which determines the minimal basis for (AP)+(PH)+(QG) ([Theorem S](/docs/proofs/minimality/theorem-minimality-7)).

#### Sufi Lataif (subtle centres)

*The specific identifications below are [projection hypotheses](#принцип-неопределённости-проекции) [И].*

**Structure.** 5–7 subtle centres (names: Nafs, Qalb, Ruh, Sirr, Khafi, Akhfa, sometimes additional ones).

**Projection:** A subset of the diagonal, typically 5 main ones: $\pi_{\text{lataif}}: \Gamma \mapsto (\gamma_{OO}, \gamma_{EE}, \gamma_{DD}, \gamma_{LL}, \gamma_{UU})$.

**Note.** Variants with 7 Lataif are structurally isomorphic to the chakra system.

#### The five skandhas (Buddhism)

*The specific identifications below are [projection hypotheses](#принцип-неопределённости-проекции) [И].*

**Structure.** 5 aggregates: Rupa (form), Vedana (sensation), Sanna (perception), Sankhara (formations), Vinnana (consciousness).

**Projection:** $\pi_{\text{skandhas}}: \Gamma \mapsto (\gamma_{SS}, \gamma_{EE}, \gamma_{AA}, \gamma_{DD}, \gamma_{UU})$.

| Skandha | Dimension | Justification |
|---|---|---|
| Rupa (form) | S | Bodily structure |
| Vedana (sensation) | E | Subjective experience |
| Sanna (perception) | A | Discrimination, recognition |
| Sankhara (formations) | D | Volitional impulses, processes |
| Vinnana (consciousness) | U | Integrative awareness |

**What it sees:** 5 of the 7 populations.
**What it loses:** Populations L and O; all coherences.

**Structural observation.** Buddhist analysis systematically *does not single out* logic (L) as a separate aspect and *does not thematise* ground (O). This is consistent with the anatta doctrine: denial of a fixed substrate (O) and dissolution of formal logic into processuality (D).

---

### 3.2 Systems based on coherences (off-diagonal elements)

*All element↔coherence identifications in §3.2 are [projection hypotheses](#принцип-неопределённости-проекции) [И].*

These systems describe **connections** between dimensions.

#### Tarot (Major Arcana)

**Structure.** 22 cards of the Major Arcana (0–XXI).

**Projection:**

$$
\pi_{\text{Tarot}}: \Gamma \mapsto \{21 \text{ coherences} + 1 \text{ zero element}\}
$$

| Card group | Elements of $\Gamma$ | Number |
|---|---|---|
| Cards I–XXI | 21 coherences $\lvert\gamma_{ij}\rvert$ ($i < j$) | 21 |
| Card 0 (The Fool) | State $\Gamma \propto I/7$ (uniform, without coherences) | 1 |

**What it sees:** Moduli of all 21 coherences (upper triangle).
**What it loses:** Populations (diagonal), phases (directedness of connections), dynamics.

**Structural observation.** The number 22 = 21 + 1 coincides exactly with the number of off-diagonal elements in the upper triangle plus the trivial state. The "Fool" card (0) semantically describes pure potentiality — the state before discriminations — which corresponds to $\Gamma = I/7$.

#### Kabbalah (Tree of Life)

**Structure.** 10 sefirot + 22 paths.

**Projection:**

$$
\pi_{\text{Kabbalah}}: \Gamma \mapsto \{10 \text{ superpositions}; \, 22 \text{ connections}\}
$$

The 10 sefirot are **not separate dimensions** but non-linear combinations (superpositions) of elements of $\Gamma$:

| Sefira | Approximate combination | Type |
|---|---|---|
| Kether | $\gamma_{UU}$ (or $\gamma_{UU} + \text{Re}(\gamma_{OU})$) | Population + coherence |
| Chokmah | $\gamma_{AA} + \lvert\gamma_{AL}\rvert$ | Mixed |
| Binah | $\gamma_{LL} + \lvert\gamma_{LS}\rvert$ | Mixed |
| Chesed | $\lvert\gamma_{SU}\rvert$ | Coherence |
| Gevurah | $\lvert\gamma_{DL}\rvert$ | Coherence |
| Tiferet | $\gamma_{EE} + \text{Re}(\gamma_{EU})$ | Population + coherence |
| Netzach | $\lvert\gamma_{DE}\rvert$ | Coherence |
| Hod | $\lvert\gamma_{AL}\rvert$ | Coherence |
| Yesod | $\gamma_{OO} + \lvert\gamma_{OE}\rvert$ | Mixed |
| Malkuth | $\gamma_{SS}$ | Population |

The 22 paths correspond to the 22 letters of the Hebrew alphabet and map onto a subset of coherences.

**What it sees:** 10 of the 49 elements — mixed combinations of populations and coherences.
**What it loses:** The majority of coherences (39 of 49 elements), phase structure, dynamics.

**Structural observation.** Kabbalah is the only traditional system that *mixes* populations and coherences within single elements (sefirot). This makes the inverse projection $\pi_{\text{Kabbalah}}^{-1}$ the most complex of all.

#### Enneagram

**Structure.** 9 types + 18 directed connections (arrows of integration/disintegration).

**Projection:** $\pi_{\text{Ennea}}: \Gamma \mapsto \{9 \text{ subsets}\}$.

The 9 types are combinations of 3 centres (head/heart/body ↔ L/E/D) × 3 strategies (active/passive/harmonising):

| Type | Centre | Strategy | Approximate projection |
|---|---|---|---|
| 1 | D (body) | harmonising | $\lvert\gamma_{DL}\rvert > \lvert\gamma_{DE}\rvert$, $\gamma_{DD}$ low |
| 2 | E (heart) | active | $\lvert\gamma_{EA}\rvert$ high |
| 3 | E (heart) | harmonising | $\lvert\gamma_{ED}\rvert$ high |
| 4 | E (heart) | passive | $\lvert\gamma_{EO}\rvert$ high |
| 5 | L (head) | passive | $\gamma_{LL}$ high, $\lvert\gamma_{LE}\rvert$ low |
| 6 | L (head) | harmonising | $\lvert\gamma_{LS}\rvert$ high |
| 7 | L (head) | active | $\lvert\gamma_{LD}\rvert$ high |
| 8 | D (body) | active | $\gamma_{DD}$ high |
| 9 | D (body) | passive | $\gamma_{DD}$ low, $\lvert\gamma_{DU}\rvert$ high |

**What it sees:** A subset of populations and moduli, coarsely discretised into 9 clusters.
**What it loses:** Continuity of the state space, phases, exact values.

**Structural observation.** The number 9 = $C(3,1) \times 3$ — a direct product of three "centres" by three "positions" — is a coarse factorisation of the 3-dimensional subspace $\{D, L, E\}$.

---

### 3.3 Systems with binary phase projection

*All identifications below are [projection hypotheses](#принцип-неопределённости-проекции) [И].*

These systems discretise the continuous phase $\theta_{ij} \in [0, 2\pi)$ into a binary value.

#### I Ching (易經)

**Structure.** 64 hexagrams, each of 6 lines (yin/yang).

**Projection:**

$$
\pi_{\text{IC}}: \Gamma \mapsto (\text{sgn}(\text{Re}(\gamma_{ij})))_{(i,j) \in M_6} \in \{-1, +1\}^6
$$

where $M_6$ is 6 pairs of dimensions (presumably without the U-dimension or with a fixed combination).

| Property | Value |
|---|---|
| Number of elements | $2^6 = 64$ hexagrams |
| Binary projection | $\text{sgn}(\text{Re}(\gamma_{ij}))$: yin (−) / yang (+) |
| Number of dimensions | 6 of 7 (without U or with U encoded globally) |

**What it sees:** The sign of the real part for 6 coherences — the coarsest binary phase information.
**What it loses:** Phase continuity ($\theta \in [0, 2\pi)$ → 1 bit), the 7th dimension, moduli of all coherences, populations.

**Structural observation.** The binary projection $\text{sgn}(\text{Re}(\gamma_{ij}))$ is equivalent to asking: "is the phase in the first or second semicircle?" — i.e., $\theta_{ij} \in (-\pi/2, \pi/2)$ (yang) or $\theta_{ij} \in (\pi/2, 3\pi/2)$ (yin). This is the maximally coarse discretisation of Gap: Gap < 1/√2 → "yang" (relative transparency), Gap > 1/√2 → "yin" (relative opacity).

#### Numerology

**Structure.** 9 base numbers (1–9), obtained by summing digits.

**Projection:** $\pi_{\text{numer}}: \Gamma \mapsto f(\sum_i \gamma_{ii}) \bmod 9 + 1$, where $f$ is a function depending on input data (date of birth, etc.).

**What it sees:** One number — the maximally coarse scalar projection.
**What it loses:** Almost everything (48 → 1 parameter).

**Structural observation.** Numerology is an example of a **critically degenerate** projection. Information capacity: $\log_2 9 \approx 3.2$ bits out of $48 \times \log_2(\text{Res})$, where Res is the resolving power. This does not mean uselessness: even 3 bits can capture a meaningful invariant if the projection is well chosen.

---

### 3.4 Systems describing external coherences (upper triangle)

*All identifications below are [projection hypotheses](#принцип-неопределённости-проекции) [И].*

These systems describe **how connections between dimensions appear from outside** ($\text{Map}_{\text{ext}}$), but not how they are experienced from within ($\text{Map}_{\text{int}}$).

#### Western astrology

**Structure.** ~50 elements: 10 planets × 12 signs × 12 houses + aspects between planets.

**Projection:**

$$
\pi_{\text{astro}}: \Gamma \mapsto \{\lvert\gamma_{ij}\rvert, \, \text{discrete\_aspects}(\lvert\gamma_{ij}\rvert)\}_{i < j}
$$

Planets map onto dimensions or their combinations; signs and houses — onto discretisation of moduli; aspects — onto discretisation of coherences:

| Astrological aspect | Approximate Gap range |
|---|---|
| Conjunction (0°) | $\lvert\gamma_{ij}\rvert$ maximal, Gap ≈ 0 |
| Opposition (180°) | $\theta_{ij} \approx \pi$, Gap ≈ 0 (but Re < 0) |
| Square (90°) | $\theta_{ij} \approx \pi/2$, Gap ≈ 1 |
| Trine (120°) | $\theta_{ij} \approx 2\pi/3$, Gap ≈ √3/2 |
| Sextile (60°) | $\theta_{ij} \approx \pi/3$, Gap ≈ √3/2 |

**What it sees:** The upper triangle — external coherences through the symbolism of planets and aspects. Coarse phase discretisation (5–7 aspects from a continuous $[0, 2\pi)$).
**What it loses:** The inner aspect ($\text{Map}_{\text{int}}$, lower triangle), phase dynamics, self-correction.

**Structural observation.** Astrology is the **richest** of the traditional systems in number of elements (~50), but it captures only $\text{Map}_{\text{ext}}$. This explains its stability: external observations are more accessible than introspection.

#### Human Design

**Structure.** 64 gates (from I Ching) + 36 channels + 9 centres + 4 types + 6 profiles.

**Projection:** A hybrid of several projections:

$$
\pi_{\text{HD}} = \pi_{\text{centres}} \oplus \pi_{\text{channels}} \oplus \pi_{\text{gates}}
$$

| HD component | Elements of $\Gamma$ | Projection type |
|---|---|---|
| 9 centres | Subsets of populations $\gamma_{ii}$ | Diagonal (coarse) |
| 36 channels | Subset of coherences $\lvert\gamma_{ij}\rvert$ | Moduli (partial) |
| 64 gates | Binary I Ching projection via astrological positions | Binary |
| Type (4 types) | Coarse classification of overall profile | Scalar |

**What it sees:** Part of the diagonal + part of the coherences through a synthesis of I Ching and astrology.
**What it loses:** Full phase structure, $\text{Map}_{\text{int}}$, dynamics.

**Structural observation.** Human Design is an eclectic system — an attempt to increase the information capacity of the projection by combining several traditional systems. However, the combination of projections $\pi_A \oplus \pi_B$ is not equivalent to an extension — it can introduce contradictions if $\pi_A$ and $\pi_B$ project the same element of $\Gamma$ differently.

---

### 3.5 Systems with elemental structure

*All identifications below are [projection hypotheses](#принцип-неопределённости-проекции) [И].*

Systems that describe not individual elements of $\Gamma$ but **equivalence classes** of states.

#### Alchemy (European)

**Structure.** 4 elements (Fire, Water, Air, Earth) + 3 principles (Sulfur, Mercury, Salt) + 7 metals.

**Projection:**

| Alchemical concept | Projection in $\Gamma$ |
|---|---|
| 4 elements | 4 combinations of 2 axes: Hot/Cold × Dry/Moist ≈ $\text{sgn}(\gamma_{DD}), \text{sgn}(\gamma_{EE})$ |
| 3 principles | Triplet: Sulfur (D, active), Mercury (A, mediating), Salt (S, stable) |
| 7 metals | 7 populations $\gamma_{ii}$, traditionally associated with planets |

**What it sees:** 7 populations (via metals), a 4-cluster binary classification (via elements).
**What it loses:** Coherences, phases, continuity.

**Structural observation.** The alchemical seven metals (Au, Ag, Cu, Fe, Sn, Pb, Hg) → 7 planets → 7 dimensions is one of the oldest sevenfold classifications. The number 7 here is no coincidence: it reflects the fundamentality of $\dim(\text{Im}(\mathbb{O})) = 7$.

#### Wu Xing (五行, Five Elements)

**Structure.** 5 phases: Wood, Fire, Earth, Metal, Water. Cycles of generation and conquest.

**Projection:** $\pi_{\text{WuXing}}: \Gamma \mapsto 5$ classes, with cyclic relations.

| Element | Possible identification | Justification |
|---|---|---|
| Wood (木) | D (Dynamics) | Growth, expansion |
| Fire (火) | E (Interiority) | Experience, intensity |
| Earth (土) | S (Structure) | Stability, support |
| Metal (金) | L (Logic) | Clarity, discrimination |
| Water (水) | O (Ground) | Depth, source |

**What it sees:** 5 of the 7 populations. Generation/conquest cycles — coarse discretisation of net currents $J_{\text{net}}(i,j)$ between dimensions.
**What it loses:** 2 dimensions (A and U), coherences, continuity.

**Structural observation.** The generation cycle Wood→Fire→Earth→Metal→Water→Wood corresponds to a cyclic permutation of 5 dimensions. The conquest cycle is a "skip-one" permutation. Both cycles are special cases of the net-current structure $J_{\text{net}}(i,j)$ for specific configurations of $\Gamma$.

---

### 3.6 Geometric and numerical systems

*All identifications below are [projection hypotheses](#принцип-неопределённости-проекции) [И].*

#### Platonic solids

**Structure.** 5 regular polyhedra: tetrahedron (4), cube (6), octahedron (8), dodecahedron (12), icosahedron (20).

**Connection with $\Gamma$:** The Platonic solids are not a projection of $\Gamma$ but a description of the **symmetries** of subspaces of $\mathcal{H}$. The symmetry groups of the Platonic solids ($A_4, S_4, A_5$) are finite subgroups of $SO(3) \subset G_2$, and their representations on $\mathbb{C}^7$ determine invariant subspaces of the coherence matrix.

#### Runes (Elder Futhark)

**Structure.** 24 runes organised into 3 "aettir" of 8.

**Projection:** 24 = 21 coherences + 3 populations. The organisation into 3 groups of 8 recalls the decomposition $7 \to 1 + 3 + \bar{3}$ under SU(3) (8 generators of SU(3) = adjoint representation).

---

## 4. Quantitative comparison {#количественное-сравнение}

### 4.1 Information capacity

| System | Elements | Information (bits) | Of 48 parameters | Loss (%) |
|---|---|---|---|---|
| **Chakras** | 7 | ~21 (3 bits × 7) | 7 populations | 85% |
| **Five skandhas** | 5 | ~15 | 5 populations | 90% |
| **Wu Xing** | 5 + cycles | ~17 | 5 populations + 5 directed connections | 87% |
| **Numerology** | 9 numbers | ~3.2 | 1 scalar invariant | 97% |
| **Enneagram** | 9 + 18 | ~25 | ~9 clusters in 3D subspace | 82% |
| **I Ching** | 64 | 6 | 6 binary signs from 21 phases | 88% |
| **Tarot (Major)** | 22 | ~45 | 21 moduli + 1 trivial state | 53% |
| **Kabbalah** | 32 (10+22) | ~50 | 10 mixed + 22 paths | 48% |
| **Astrology** | ~50 | ~60 | Upper triangle + coarse phase | 42% |
| **Human Design** | ~170 | ~70 | Hybrid of several projections | 38% |
| **Runes** | 24 | ~33 | 21 coherences + 3 populations | 65% |
| **Alchemy** | 7+4+3 | ~27 | 7 populations + 4 binary classes | 77% |
| **UHM ($\Gamma$)** | **49** | **~144** | **All 48 parameters** | **0%** |

### 4.2 Structural comparison

| Parameter | I Ching | Astrology | Kabbalah | HD | Tarot | Chakras | **UHM** |
|---|---|---|---|---|---|---|---|
| Populations | 0/7 | Partial | 4/7 | Partial | 0/7 | **7/7** | **7/7** |
| Coherence moduli | 0/21 | ~15/21 | ~8/21 | ~10/21 | **21/21** | 0/21 | **21/21** |
| Phases | 6 bits | 5–7 discrete | 0 | 0 | 0 | 0 | **21 continuous** |
| Ext/int duality | No | No | Partial | No | No | No | **Yes** |
| Dynamics | Static | Cycles | Static | Static | Static | Static | **$d\Gamma/d\tau$** |
| Self-correction | No | No | No | No | No | No | **Yes** ($\varphi$) |
| Falsifiability | No | No | No | No | No | No | **Yes** |

---

## 5. Completeness and minimality {#теорема-полноты}

After analysing more than ten symbolic systems from different eras and cultures, two questions arise: (1) is the formalism $\Gamma$ sufficient to describe everything that these systems describe? and (2) is $\Gamma$ the minimal such formalism?

### 5.1 Descriptive completeness [О] {#описательная-полнота}

:::info Observation (Descriptive completeness) [О]
For every predicate $P$ expressible in any of the listed symbolic systems, there exists a formula in terms of $\Gamma$:

$$
P = \pi_S(F_P(\Gamma))
$$
:::

:::warning Epistemic status
This observation is a **trivial consequence of definitions** (status [О]), not a substantive theorem. Each $\pi_S$ is defined as a map *from* $\Gamma$, so the expressibility of $P$ through $\Gamma$ is a tautology. The other two statements are non-trivial.
:::

### 5.2 Minimality of Γ [Т] {#минимальность-гаммы}

:::warning Claim (Minimality) [Т]
The matrix $\Gamma \in \mathcal{D}(\mathbb{C}^7)$ is the **minimal** object unifying all the listed projections. More precisely: for any alternative formalism $\Gamma' \in \mathcal{D}(\mathbb{C}^{N'})$ admitting the same projections:

$$
N' \geq 7
$$
:::

**Proof.** By [Theorem S](/docs/proofs/minimality/theorem-minimality-7) [Т]: $N = 7$ is the minimum dimensionality for (AP)+(PH)+(QG). Symbolic systems that describe autopoietic entities (chakras as "energy centres of a living being", Kabbalah as "the structure of the soul") implicitly assume all three conditions. Therefore $N' \geq 7$. $\blacksquare$

### 5.3 Information-theoretic characterisation of loss [Т] {#информационная-утрата}

:::warning Theorem (Information loss bound) [Т]
For a projection $\pi_S: \mathcal{D}(\mathbb{C}^7) \to \mathcal{C}_S$ with $|\mathrm{Obj}(\mathcal{C}_S)| = M$ elements, the information loss is bounded below by:

$$
H(\Gamma | \pi_S(\Gamma)) \geq \log_2 \binom{48}{M} - M \cdot \log_2(\text{Res}_S)
$$

where $H(\cdot|\cdot)$ is the conditional entropy and $\text{Res}_S$ is the resolving power of the elements of system $S$.
:::

**Corollary.** For binary systems ($\text{Res}_S = 2$, like I Ching): $H \geq \log_2 \binom{48}{6} - 6 \approx 16.7$ bits are lost out of $\sim 144$ bits at 3 decimal digits of resolution. This formalises the intuition of the table in §4.1.

---

## 6. Structural analysis: what determines the stability of a projection {#структурный-анализ}

### 6.1 Fano structure and natural projections

The [Fano plane](/docs/proofs/gap/fano-channel) PG(2,2) defines 7 associative triplets. Coherences **within** Fano triplets are more stable than those between them. This explains why certain groupings of dimensions recur across cultures:

| # | Fano line | Dimensions | Cultural analogue |
|---|---|---|---|
| 1 | $\{1, 2, 4\}$ | $\{A, S, L\}$ | "Mind" (cognitive block: discrimination + form + coordination) |
| 2 | $\{2, 3, 5\}$ | $\{S, D, E\}$ | "Body" (somatic block: form + motion + sensation) |
| 3 | $\{3, 4, 6\}$ | $\{D, L, U\}$ | "Will" (active-integral: action + logic + integration) |
| 4 | $\{4, 5, 7\}$ | $\{L, E, O\}$ | "Wisdom" (depth block: understanding + experience + source) |
| 5 | $\{5, 6, 1\}$ | $\{E, U, A\}$ | "Spirit" (integrative consciousness: experience + unity + articulation) |
| 6 | $\{6, 7, 2\}$ | $\{U, O, S\}$ | "Being" (ground: integration + nourishment + stability) |
| 7 | $\{7, 1, 3\}$ | $\{O, A, D\}$ | "Vital force" (vital block: source + discrimination + dynamics) |

*Index convention: $\{A, S, D, L, E, U, O\} = \{1, 2, 3, 4, 5, 6, 7\}$ — consistent with the [G₂-structure](/docs/physics/gauge-symmetry/g2-structure#12-таблица-фано-линий). Each line is a triplet $\{i, i{+}1, i{+}3 \bmod 7\}$.*

**Observation.** The three Fano lines containing A (=1): $\{A, S, L\}$, $\{E, U, A\}$, $\{O, A, D\}$. The tripartite division "body–mind–spirit" is one of the most stable cross-cultural classifications. In UHM it follows from the fact that each dimension (in particular A) participates in exactly 3 Fano triplets — a fundamental property of PG(2,2).

### 6.2 Why the sevenfold is stable

The number 7 appears in symbolic systems with inexplicable frequency: 7 chakras, 7 alchemical metals, 7 days of the week, 7 notes, 7 planets of antiquity, 7 deadly sins, 7 sacraments, 7 Lataif. Within UHM this has a precise explanation:

$$
\dim(\text{Im}(\mathbb{O})) = 7
$$

The seven imaginary units of the octonions $\{e_1, \ldots, e_7\}$ are the **unique** admissible basis for a division algebra over $\mathbb{R}$ (besides $\mathbb{R}, \mathbb{C}, \mathbb{H}$, which give 0, 1, 3 imaginary units). Hurwitz's theorem (1898) fixes the possible dimensions: 1, 2, 4, 8. The imaginary part dimensions: 0, 1, 3, 7. For a system with (AP)+(PH)+(QG), the minimum sufficient dimension is 7.

### 6.3 Why the duality is hidden

No traditional symbolic system formalises the distinction between the **external** ($\gamma_{ij}$, upper triangle) and **internal** ($\gamma_{ji} = \gamma_{ij}^*$, lower triangle) aspect of coherence. The reason:

The distinction between $\gamma_{ij}$ and $\gamma_{ji}$ is encoded in the **phase** $\theta_{ij} = \arg(\gamma_{ij})$. Phase is the most "fragile" parameter: it is the first to be destroyed when the observation is coarsened (dephasing). Traditional systems arose from introspective and phenomenological experience, which does not have sufficient resolution to register phase information.

In the UHM formalism, the duality is realised through **Hermitian conjugation** $*: \gamma_{ij} \mapsto \gamma_{ji}$, which is a contravariant involutive functor in the $\dagger$-category of Hilbert spaces. [Gap](/docs/core/dynamics/gap-operator) $= |\sin(\theta_{ij})|$ is the precise measure of the divergence between external and internal.

---

## 7. Formalisation of mystical concepts [И] {#мистические-концепты}

A number of cross-cultural phenomenological concepts admit formalisation through the Gap structure. The formulations below are constructive interpretations, not empirically confirmed identities.

| Concept | Formalisation in UHM | Mechanism |
|---|---|---|
| **"Enlightenment"** | L4: $\varphi(\Gamma^*) = \Gamma^*$ — [fixed point](/docs/consciousness/hierarchy/interiority-hierarchy) of self-modelling | Not Gap = 0, but **reflexive transparency**: the system accurately knows its own Gap |
| **"Dark night of the soul"** | Saddle-node [Gap bifurcation](/docs/core/dynamics/gap-phase-diagram#бифуркации): loss of stable Gap profile | The stationary attractor disappears as parameters change |
| **"Kundalini"** | Cascading activation of coherences bottom-up: $\gamma_{OE} \to \gamma_{OD} \to \gamma_{OS} \to \gamma_{OA}$ | The O-dimension sequentially connects with the others |
| **"Synchronicity"** (Jung) | Inter-system $\text{Gap}_{AB}(i,j) \to 0$ for a specific channel | Two [holons](/docs/core/dynamics/composite-systems) temporarily resonate along one dimension |
| **"Non-duality"** (Advaita) | Limit $\text{Gap} \to 0$ for all pairs | Theoretical limit; unreachable for non-trivial systems due to [topological Gap protection](/docs/core/dynamics/gap-phase-diagram#защита-gap) |
| **"Mandala"** | Visualisation of the Gap profile (heat map $7 \times 7$) | Structured representation of 49 elements |
| **"Karma"** | Non-Markovian memory kernel $K(\tau-s)$ in the [integro-differential equation](/docs/core/dynamics/gap-phase-diagram#немарковские-осцилляции) of Gap dynamics | Past configurations influence current evolution through the memory kernel |
| **"Dharma"** (Buddha) | Attractor $\Gamma^*$ of the evolution equation: the stationary state toward which the system tends as $\tau \to \infty$ | The structure of the equation itself, not a specific configuration |

---

## 8. Fundamental conclusions {#фундаментальные-выводы}

Having analysed more than ten symbolic systems — from the most ancient (chakras, I Ching, alchemy) to modern ones (Human Design, Enneagram) — we can formulate general patterns: why symbolic systems are structured as they are, and what they inevitably cannot describe.

### 8.1 Three laws of symbolic systems

Based on the analysis carried out, three structural laws are formulated:

**Law 1 (Inevitability of projection).** Any finite descriptive system with fewer than 48 elements is a non-injective projection of $\Gamma$. Information loss is not a defect of the system but a consequence of the dimensionality theorem.

**Law 2 (Fano structure of projections).** Stable symbolic systems project onto subspaces that respect the Fano structure PG(2,2). Tripartite divisions (body/psyche/spirit; Sulfur/Mercury/Salt; etc.) reflect the 3-element Fano triplets in which coherences are most stable.

**Law 3 (Inaccessibility of duality).** The distinction between $\text{Map}_{\text{ext}}$ and $\text{Map}_{\text{int}}$ (encoded by phase $\theta_{ij}$) systematically eludes traditional symbolic systems, since phase information requires the greatest resolving power of the observer.

### 8.2 What lies behind "occultism"

The word "occult" derives from the Latin *occultus* — "hidden." Symbolic systems are perceived as "occult" (hidden) for two reasons, which UHM allows to formalise precisely:

1. **Epistemological:** The projection $\pi_S$ loses information, but the practitioner of system $S$ does not know what exactly has been lost. The recovery $\pi_S^{-1}$ is ambiguous, creating the illusion of "mystery."

2. **Ontological:** The [Gap](/docs/core/dynamics/gap-operator) between external and internal ($|\sin(\theta_{ij})| > 0$) means that full reality *in principle* cannot be reduced to external observation. There is a part of reality (Im($\gamma_{ij}$)) inaccessible through $\text{Map}_{\text{ext}}$. This is the formalisation of the intuition underlying all esoteric traditions.

UHM **removes** the first reason (by providing a complete formalism) and **explains** the second (Gap is a precisely defined measure of the "hidden").

### 8.3 Descriptive coherence and its limitations [И]

:::info Observation (Descriptive coherence) [И]
UHM is capable of deriving every phenomenological predicate of every analysed symbolic system through the unified formalism $\Gamma \in \mathbb{C}^{7 \times 7}$. This is a **necessary** condition for the adequacy of the theory (if $\Gamma$ could not express the known systems, the theory would be incomplete), but **not a sufficient** condition for its truth (descriptive coherence is not the same as predictive power).
:::

**Limitations of this analysis:**

1. **Arbitrariness of projections.** The specific identifications (chakra ↔ dimension) are hypotheses [И], not theorems. For each symbolic system there exist $k!$ possible bijections, of which one "most justified" is chosen. Without empirical verification the choice remains speculative.

2. **Retrospectiveness.** The analysis was carried out *after* the theory was formulated. Predictive power requires the theory to predict the structure of *unknown* symbolic systems or new properties of *known* ones.

3. **Risk of overfitting.** 48 free parameters of $\Gamma$ against 12 systems analysed is a high parameter-to-data ratio. Strict verification criteria are needed (see the [research programme](/docs/applied/research/symbolic-correspondence#программа)).

**Popper criterion.** The analysis would be *falsified* if a stable symbolic system were found that requires $> 7$ independent parameters to describe, or that is incompatible with any projection $\pi_S$ from $\Gamma$.

---

## 9. Five types of Gap irreducibility [Т/Г] {#защита-gap}

Analysis of symbolic systems reveals a fundamental fact: no tradition has described the state of "complete transparency" (Gap = 0 for all pairs) as realisable. In UHM this follows from **five independent** mechanisms of Gap ineliminability:

| Type | Mechanism | Source | Status |
|---|---|---|---|
| 1. Code-theoretic | Hamming bound H(7,4): ≥ 3 of 21 Gaps are non-zero | [Coding theory](/docs/proofs/gap/fano-channel) | [И] |
| 2. Algebraic | Octonionic associator $[e_i, e_j, e_k] \neq 0$ generates a phase shift | [Octonionic structure](/docs/proofs/minimality/theorem-octonionic-derivation) | [Г] |
| 3. Energetic | Spontaneous minimum $V_{\text{Gap}} \neq 0$ from cubic potential $V_3$ | [Gap thermodynamics](/docs/core/dynamics/gap-thermodynamics) | [Г] |
| 4. Categorical | Lawvere's theorem: the fixed point of self-modelling is non-trivial | [φ-operator](/docs/core/operators/phi-operator) | [Г] |
| 5. Topological | $\pi_1(G_2/T^2) \cong \mathbb{Z}^2$: some Gap configurations cannot be continuously contracted | [Gap phase diagram](/docs/core/dynamics/gap-phase-diagram) | [Г] |

**Conclusion.** Complete transparency (absence of the "hidden") is mathematically impossible for a non-trivial 7D octonionic system. This explains why all symbolic traditions point to the "incomprehensible" — not as a metaphor but as a structural property of reality.

---

## Related documents

- [Coherence matrix](/docs/core/dynamics/coherence-matrix) — definition of $\Gamma$
- [Seven dimensions](/docs/core/structure/dimensions) — A, S, D, L, E, O, U
- [Gap operator](/docs/core/dynamics/gap-operator) — measure of divergence between external and internal
- [Gap semantics](/docs/physics/dual-aspect/gap-semantics) — 49-element map
- [Gap diagnostics](/docs/applied/research/gap-diagnostics) — applied methodology
- [Interiority hierarchy](/docs/consciousness/hierarchy/interiority-hierarchy) — levels L0–L4
- [Symbolic correspondences](/docs/applied/research/symbolic-correspondence) — operationalisation
- [Fano channel](/docs/proofs/gap/fano-channel) — associative triplets and codes
- [Theorem on minimality N = 7](/docs/proofs/minimality/theorem-minimality-7) — why 7
