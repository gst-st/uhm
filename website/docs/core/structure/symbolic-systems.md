---
sidebar_position: 10
title: "Formal reduction of symbolic systems"
slug: /core/structure/symbolic-systems
description: "Typed symbolic readouts, preservation of relations and actions, conditional dimension bounds and information loss"
---

# Formal Reduction of Symbolic Systems

This chapter develops a common language for comparing symbolic systems with the coherence matrix $\Gamma\in\mathcal D(\mathbb C^7)$. Its substantive proposal is that selected symbolic distinctions may be represented by populations, coherences, incidence relations and transformations of this model. The correspondence must specify **which roles, relations and operations it preserves**; a shared number of symbols alone does not establish it.

The semantic tables below are candidate interpretations. Exact structural correspondences — including binary trigrams, Fano incidence and Hamming codes — are treated separately in [Structural correspondences](/docs/applied/research/structural-correspondence). This distinction lets a proposed interpretation be strengthened by a verifiable map and, where relevant, a measurement protocol.

:::warning Status of the correspondence
The finite combinatorics and the conditional statements below can be proved. Identifications such as “chakra ↔ population” remain hypotheses [I]. A defined readout is a mathematical model of an interpretation; whether a tradition actually measures that readout is an additional empirical question.
:::

:::tip The generative counterpart
This chapter is the *analytic* half of the pair: it reduces existing traditions to projections of $\Gamma$. The *generative* half — the canonical UHM-native symbolic system built directly from the derived structures (seven layers, sixteen error-correcting archetypes, an honest anchoring theory, practice protocols) — is constructed in the [Γ-Canon](/docs/applied/research/gamma-canon).
:::

---

## 1. Fundamental formulation {#фундаментальная-постановка}

### 1.1 What is a symbolic system

**Definition.** A symbolic system $S$ has a typed vocabulary, specified relations $R_S$ and, when applicable, named partial transformations. Types distinguish, for example, an axis, a relation between axes, an outcome label and an action. To represent its observations in UHM, fix a readout

$$
\pi_S:X\longrightarrow Y_S,\qquad X=\mathcal D(\mathbb C^7),
$$

where $Y_S$ is the space of complete records produced by the chosen protocol. One card from 22 possibilities, a 21-coordinate rating and a sequence of draws have different record spaces even if they use the same vocabulary.

**Structural contract.** A correspondence $h:S\to T$ assigns a map to each declared sort. It preserves a named relation when $R_S(a_1,\ldots,a_k)$ implies $R_T(h(a_1),\ldots,h(a_k))$; equivalence requires the converse as well. For a source action $c:D_c\to S$ and its target action $d:D_d\to T$, an exact executable correspondence requires, on the relevant sort,

$$
a\in D_c\iff h(a)\in D_d,\qquad h(c(a))=d(h(a))\quad(a\in D_c).
$$

The second equation preserves execution; the first prevents undefined actions from silently becoming defined. Observations must commute with the map through explicitly specified decoders. These obligations are stronger than a bijection between names.

A **functor** is available after specifying actual categories: objects, arrows, identity arrows and composition. For example, a map of action paths induces a functor only when it preserves the declared path equations. A set with arbitrary relations is not automatically such a category. The notation $\pi_S:\mathrm{Hol}\to\mathcal C_S$ is appropriate only after these additional data and checks have been supplied.

For a state quotient, an executable readout must also respect its fibers. If $\pi_S(x)=\pi_S(x')$, every retained observable must agree on $x,x'$; each retained action must be defined on both or neither, and their successors must have equal readouts. Otherwise no deterministic action on $Y_S$ can reproduce the source action. See the [general structural contract](/docs/applied/research/structural-correspondence).

### 1.2 When information loss is inevitable

The [coherence matrix](/docs/core/dynamics/coherence-matrix) has 48 independent real parameters on its positive-definite interior: 6 independent populations and 42 real coordinates of 21 complex coherences. Positivity couples their allowed values; boundary strata may have smaller dimension.

**Continuous dimension bound [T].** A continuous readout into $\mathbb R^n$ with $n<48$ cannot be injective on this interior. Indeed, identify a neighbourhood with an open subset of $\mathbb R^{48}$ and append $48-n$ zero coordinates to the alleged injection. Invariance of domain would make its image open in $\mathbb R^{48}$, whereas it lies in a lower-dimensional coordinate subspace. This is a contradiction.

Continuity is essential: arbitrary set-theoretic encodings can inject finitely many real coordinates into one real number. Separately, a readout with only finitely many possible records is noninjective on the continuum of states, regardless of how its alphabet size compares with 48. **Alphabet size, number of continuous output coordinates and information in bits are different quantities.** A finite vocabulary used in unbounded expressions need not have a finite record space.

For example, brightness alone does not distinguish all RGB colours. This concerns the chosen one-dimensional continuous readout, not the number of colour words available.

### 1.3 The fundamental question

The research hypothesis is that some recurring symbolic distinctions capture the same structural features through different readouts. It becomes substantive when independently specified relations or interventions agree under the maps in §1.1. Historical recurrence and empirical reliability require their own evidence.

Under the population interpretation, seven labelled entries of the diagonal have 6 independent degrees of freedom because their sum is 1. Interpreting a second sevenfold vocabulary by these entries is a possible model, not a consequence of the equality of cardinalities. Likewise, a proposed coherence-based interpretation must say how its symbols encode or measure those coherences.

### 1.4 The projection uncertainty principle {#принцип-неопределённости-проекции}

:::warning Central methodological limitation [I]
UHM specifies the model state; representing a symbolic system by a readout of that state is a proposed empirical interpretation. The choice of projection $\pi_S$ is **not a mathematical derivation** but an empirical hypothesis.
:::

**The problem.** The matrix $\Gamma$ contains **several** 7-element substructures onto which a 7-element symbolic system can be projected:

| Candidate substructure | Elements | Structure |
|---|---|---|
| Populations (diagonal) | $\gamma_{11}, \ldots, \gamma_{77}$ | Linear order (by index) |
| Fano lines | 7 triplets $\{i, j, k\}$ | Incidence geometry PG(2,2) |
| Projectors $\Pi_p$ | 7 projectors onto Fano subspaces | Finite coordinate family in a fixed octonion frame |
| Spectrum of $\Gamma$ | 7 eigenvalues $\lambda_1, \ldots, \lambda_7$ | Ordered set (by magnitude) |
| Atomic Kraus operators | 7 operators $K_m^{(\mathrm{atom})}$ | Set of classifier atoms |

Seven distinct symbolic labels admit a bijection with the seven labelled slots of any candidate. Equal eigenvalues do not become distinct values through that labelling. A slot assignment still needs a readout rule, and different rules may retain different distinctions.

**Corollary.** All identifications $\pi_S$ in this document are **constructive hypotheses [I]**, not mathematical derivations [T]. For each symbolic system:

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

The modulus–phase coordinates are valid where the respective coherences are nonzero; at zero the phase is undefined. Positivity constrains their joint values. All coordinates refer to the fixed semantic frame, not to basis-independent observables.

### 2.1 Classification of projections

**Definition.** A coordinate-selection profile for a readout is the quadruple:

$$
\operatorname{profile}(\pi_S) = (D_S, \, M_S, \, \Phi_S, \, \text{Res}_S)
$$

where:
- $D_S \subseteq \{1,\ldots,7\}$ — which dimensions the system "sees" (populations)
- $M_S \subseteq \{(i,j): i<j\}$ — which coherence pairs support the profile
- $\Phi_S \subseteq M_S$ — for which pairs it distinguishes phase
- $\text{Res}_S \in \{\text{binary}, \text{discrete}, \text{continuous}\}$ — resolving power


This profile does not yet define $\pi_S$: the output space, quantisation thresholds, phase convention and boundary rules must also be specified. A phase-only readout need not report a modulus; in that case $M_S$ records the supporting pair indices, not a claim that all their moduli are observed.

---

## 3. Taxonomy of symbolic systems {#таксономия}

### 3.1 Systems based on populations (diagonal of $\Gamma$)

These systems describe the **distribution of energy** among dimensions, ignoring connections (coherences).

#### Chakra system (7 chakras) {#чакры}

:::info The [Projection uncertainty principle](#принцип-неопределённости-проекции) applied
The analysis below demonstrates that the identification of chakras with elements of $\Gamma$ is a **constructive hypothesis** [I], not a mathematical derivation. Several projection candidates and their properties are presented.
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

The order is a thin category. The [Fano plane](/docs/physics/gauge-symmetry/g2-structure) instead specifies points, lines and incidence; its incidence poset has 14 objects, not just the 7 points. These structures must not be equated by their object counts.

A bijection of the seven chakra labels with the seven points can **transport** the full ternary Fano relation. If only the linear order is retained, that extra relation has been forgotten. Consecutiveness in an order is a different relation from collinearity, so neither its presence nor absence proves categorical compatibility. A rigorous comparison declares the target relation and checks preservation using §1.1.

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
| $\{1,2,4\}$ | $\{A, S, L\}$ | $\{5, 6, 4\}$ — consecutive after sorting: $4,5,6$ |
| $\{2,3,5\}$ | $\{S, D, E\}$ | $\{6, 3, 2\}$ — **not** adjacent |
| $\{3,4,6\}$ | $\{D, L, U\}$ | $\{3, 4, 7\}$ — **not** adjacent |
| $\{4,5,7\}$ | $\{L, E, O\}$ | $\{4, 2, 1\}$ — **not** adjacent |
| $\{5,6,1\}$ | $\{E, U, A\}$ | $\{2, 7, 5\}$ — **not** adjacent |
| $\{6,7,2\}$ | $\{U, O, S\}$ | $\{7, 1, 6\}$ — **not** adjacent |
| $\{7,1,3\}$ | $\{O, A, D\}$ | $\{1, 5, 3\}$ — **not** adjacent |

The first line occupies three consecutive positions; the other six do not. This calculation describes the chosen ordering. It neither prohibits adding Fano incidence to the chakra vocabulary nor establishes that its traditional relations are Fano relations.

##### F. Verification criteria

What could confirm or refute a specific mapping $\phi$?

1. **Correlation test:** If $\phi$ is correct, activation of chakra $k$ should correlate with an increase in population $\gamma_{\phi(k)\phi(k)}$ (measurable via the [Gap-diagnostics protocol](/docs/applied/research/gap-diagnostics))
2. **Tattva monotonicity:** The subtlety order of the tattvas should monotonically correspond to some computable characteristic of the dimensions (e.g., mean coherence or entropy)
3. **Incidence test:** If a Fano relation is claimed, specify the independently observed ternary relation and verify that $\phi$ preserves it. A match of names or positions is insufficient.

**Current status:** The mapping $\phi_0$ above is the **most widely discussed candidate**, but empirical verification has not been carried out. Alternative $\phi$ mappings (the remaining 119 bijections) have not been studied systematically.

**Under this population-readout hypothesis:** a protocol returning all seven populations determines the diagonal, with 6 independent values. It loses the 21 complex offdiagonal entries, hence 42 real coordinates. The Fano incidence of the fixed frame is background structure, not an additional state variable that a diagonal readout measures.

**Structural observation.** Sevenfold vocabularies, including chakras and alchemical metals, can be compared with the seven chosen dimensions. The equality $\dim\operatorname{Im}\mathbb O=7$ provides an algebraic candidate; it does not select a cultural bijection or establish its accuracy. The precise conditional bounds for the UHM dimension are stated in §5.2.

#### Sufi Lataif (subtle centres)

*The specific identifications below are [projection hypotheses](#принцип-неопределённости-проекции) [I].*

**Structure.** 5–7 subtle centres (names: Nafs, Qalb, Ruh, Sirr, Khafi, Akhfa, sometimes additional ones).

**Projection:** A subset of the diagonal, typically 5 main ones: $\pi_{\text{lataif}}: \Gamma \mapsto (\gamma_{OO}, \gamma_{EE}, \gamma_{DD}, \gamma_{LL}, \gamma_{UU})$.

**Note.** Seven-centre variants admit bijections with the chakra labels. Structural isomorphism would additionally require matching their specified relations and operations.

#### The five skandhas (Buddhism)

*The specific identifications below are [projection hypotheses](#принцип-неопределённости-проекции) [I].*

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

*All element↔coherence identifications in §3.2 are [projection hypotheses](#принцип-неопределённости-проекции) [I].*

These systems describe **connections** between dimensions.

#### Tarot (Major Arcana)

**Structure.** 22 cards of the Major Arcana (0–XXI).

**Projection:**

$$
q_{\text{Tarot}}(\Gamma)=(\lvert\gamma_{ij}\rvert)_{i<j}\in\mathbb R_{\geq0}^{21}
$$

| Card group | Elements of $\Gamma$ | Number |
|---|---|---|
| Cards I–XXI | 21 coherences $\lvert\gamma_{ij}\rvert$ ($i < j$) | 21 |
| Card 0 (The Fool) | State $\Gamma \propto I/7$ (uniform, without coherences) | 1 |

**Model readout:** the proposed vector records 21 moduli. The table assigns symbolic labels to its coordinates and a distinguished state. A single card draw does not return this vector; obtaining it requires an independently specified rating or measurement protocol. An actual card-output map $\pi_{\text{Tarot}}$ additionally needs a rule taking states to outcomes.
**What it loses:** Populations (diagonal), phases (directedness of connections), dynamics.

**Structural observation.** The number 22 = 21 + 1 coincides exactly with the number of off-diagonal elements in the upper triangle plus the trivial state. The "Fool" card (0) semantically describes pure potentiality — the state before discriminations — which corresponds to $\Gamma = I/7$.

#### Kabbalah (Tree of Life)

**Structure.** 10 sefirot + 22 paths.

**Projection:**

$$
q_{\text{Kabbalah}}: \Gamma \mapsto (f_1(\Gamma),\ldots,f_{10}(\Gamma))\in\mathbb R^{10}
$$

The following ten candidate readouts mix populations and coherences. They are scalar functions, not vector superpositions; one formula must be selected wherever alternatives are listed:

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

The 22 paths are separate graph data: their endpoints, direction and correspondence to letters must be fixed for a chosen convention. They cannot inject into the 21 unordered offdiagonal pairs. Repeated readouts or additional typed relations are possible, but must be declared and checked by the contract in §1.1.

**What this candidate records:** ten scalar functions with at most ten locally independent outputs where differentiable; their actual rank can be lower. **What remains undetermined:** the fiber $q_{\text{Kabbalah}}^{-1}(y)\cap\mathcal D(\mathbb C^7)$, rather than “39 of 49 entries”. Recovery is a constrained completion problem, not an inverse function. Mixing populations and coherences is a legitimate modelling choice; its symbolic interpretation and graph compatibility remain to be tested.

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

*All identifications below are [projection hypotheses](#принцип-неопределённости-проекции) [I].*

These systems discretise the continuous phase $\theta_{ij} \in [0, 2\pi)$ into a binary value.

#### I Ching (易經)

**Structure.** 64 hexagrams, each of 6 lines (yin/yang).

**Candidate binary readout.** Fix six distinct pairs $M_6\subset\{(i,j):i<j\}$, a calibrated semantic basis, and the explicit convention $b(x)=+1$ for $x\geq0$, $b(x)=-1$ for $x<0$. Then

$$
\pi_{\mathrm{IC}}(\Gamma)=\bigl(b(\operatorname{Re}\gamma_{ij})\bigr)_{(i,j)\in M_6}\in\{-1,+1\}^6.
$$

A protocol may instead refuse at zero, but must not treat an undefined phase as measured. The present convention makes the function total and discontinuous at the sign boundary. The six pair indices must be supplied before the model is operational.

| Property | Exact content of this candidate |
|---|---|
| Output alphabet | $2^6=64$ binary configurations |
| Retained feature | Six real-part signs in the fixed basis |
| Geometric support | Six pairs, which need not involve only six dimensions |
| Omitted values | Populations, moduli and all distinctions within each sign cell |

For a nonzero coherence, the sign is the sign of $\cos\theta_{ij}$. It is **not** a threshold of $\mathrm{Gap}_{ij}=\lvert\sin\theta_{ij}\rvert$: phases 0 and$\pi$ both have Gap 0 and opposite signs. A basis rephasing can alter the signs, so calibration is part of the contract. The exact Boolean structure of hexagrams does not select these six UHM readouts by itself.

#### Numerology

**Structure.** Nine outcome labels, often obtained by a digit-sum convention.

**Typing requirement.** A date-based rule has external input $d$ and the form $n(d)\in\{1,\ldots,9\}$. A state readout would instead require a declared function $g:\mathcal D(\mathbb C^7)\to\{1,\ldots,9\}$ and a tested bridge between the two. The former formula $f(\sum_i\gamma_{ii})$ is constant because $\operatorname{Tr}\Gamma=1$; it cannot distinguish states.

A single nine-valued outcome has capacity at most $\log_2 9$ bits. Whether it captures a useful invariant depends on the function and data, not on the number 9 alone.

---

### 3.4 Systems describing external coherences (upper triangle)

*All identifications below are [projection hypotheses](#принцип-неопределённости-проекции) [I].*

These systems describe **how connections between dimensions appear from outside** ($\text{Map}_{\text{ext}}$), but not how they are experienced from within ($\text{Map}_{\text{int}}$).

#### Western astrology

**Structure.** A vocabulary of planets, signs, houses and aspects. Their counts describe several sorts of objects, not a single output dimension or an information capacity.

**Projection:**

$$
q_{\mathrm{astro}}(\Gamma)=\bigl(\lvert\gamma_{ij}\rvert,Q_{ij}(\arg\gamma_{ij})\bigr)_{i<j}
$$

In this candidate interpretation, planets label dimensions or combinations, while $Q_{ij}$ is a specified phase quantiser, with refusal or a separate zero symbol when $\gamma_{ij}=0$. Identifying an astronomical angle with a coherence phase is an additional calibration hypothesis. Conditional on that identification, the following Gap values are trigonometric calculations:

| Astrological aspect | Approximate Gap range |
|---|---|
| Conjunction (0°) | $\theta_{ij}\approx0$, Gap ≈ 0; modulus is not fixed |
| Opposition (180°) | $\theta_{ij} \approx \pi$, Gap ≈ 0 (but Re < 0) |
| Square (90°) | $\theta_{ij} \approx \pi/2$, Gap ≈ 1 |
| Trine (120°) | $\theta_{ij} \approx 2\pi/3$, Gap ≈ √3/2 |
| Sextile (60°) | $\theta_{ij} \approx \pi/3$, Gap ≈ √3/2 |

**What this model records:** selected moduli and quantised phases. **What it loses:** populations if omitted, distinctions within phase bins, and trajectories if only one state is observed. The complex upper triangle determines the lower triangle by Hermiticity; these are not independent sets of state coordinates. Whether the astronomical record supplies the proposed readout is not established by that algebraic identity.

#### Human Design

**Structure.** 64 gates (from I Ching) + 36 channels + 9 centres + 4 types + 6 profiles.

**Projection:** A hybrid of several projections:

$$
\pi_{\text{HD}} = \pi_{\text{centres}} \oplus \pi_{\text{channels}} \oplus \pi_{\text{gates}}
$$

| HD component | Elements of $\Gamma$ | Projection type |
|---|---|---|
| 9 centres | Subsets of populations $\gamma_{ii}$ | Diagonal (coarse) |
| 36 channels | Candidate functions of coherences; not an injection into 21 pairs | Requires a typed graph/readout map |
| 64 gates | Binary I Ching projection via astrological positions | Binary |
| Type (4 types) | Coarse classification of overall profile | Scalar |

**What it sees:** Part of the diagonal + part of the coherences through a synthesis of I Ching and astrology.
**What it loses:** Unreported phase distinctions and dynamics; an independent internal state is not inferred from the missing entries.

**Composition.** Two maps from the same state space always form the product map $\Gamma\mapsto(\pi_A(\Gamma),\pi_B(\Gamma))$. Different outputs are not a contradiction. Inconsistency arises when independently supplied data have no common preimage under the stipulated maps; joint feasibility must be tested against those maps and the original observations.

---

### 3.5 Systems with elemental structure

*All identifications below are [projection hypotheses](#принцип-неопределённости-проекции) [I].*

Systems that describe not individual elements of $\Gamma$ but **equivalence classes** of states.

#### Alchemy (European)

**Structure.** 4 elements (Fire, Water, Air, Earth) + 3 principles (Sulfur, Mercury, Salt) + 7 metals.

**Projection:**

| Alchemical concept | Projection in $\Gamma$ |
|---|---|
| 4 elements | 4 combinations of 2 axes: Hot/Cold × Dry/Moist ≈ $b(\gamma_{DD}-t_D),\ b(\gamma_{EE}-t_E)$ |
| 3 principles | Triplet: Sulfur (D, active), Mercury (A, mediating), Salt (S, stable) |
| 7 metals | 7 populations $\gamma_{ii}$, traditionally associated with planets |

**What it sees:** 7 populations (via metals), a 4-cluster binary classification (via elements).
**What it loses:** Coherences, phases, continuity.

**Structural observation.** Seven metals, seven traditional planets and seven UHM axes admit candidate bijections. Their meanings and relations require independent checks. The four-quadrant readout additionally needs fixed thresholds $t_D,t_E$ and a boundary convention $b$; the unshifted populations have no negative signs.

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

*All identifications below are [projection hypotheses](#принцип-неопределённости-проекции) [I].*

#### Platonic solids

**Structure.** 5 regular polyhedra: tetrahedron (4), cube (6), octahedron (8), dodecahedron (12), icosahedron (20).

**Connection with $\Gamma$:** The Platonic solids are not a projection of $\Gamma$ but a description of the **symmetries** of subspaces of $\mathcal{H}$. The symmetry groups of the Platonic solids ($A_4, S_4, A_5$) are finite subgroups of $SO(3) \subset G_2$, and their representations on $\mathbb{C}^7$ determine invariant subspaces of the coherence matrix.

#### Runes (Elder Futhark)

**Structure.** 24 runes organised into 3 "aettir" of 8.

**Projection:** 24 = 21 coherences + 3 populations. The organisation into 3 groups of 8 recalls the decomposition $7 \to 1 + 3 + \bar{3}$ under SU(3) (8 generators of SU(3) = adjoint representation).

---

## 4. Quantitative comparison {#количественное-сравнение}

### 4.1 Information capacity requires a protocol

For one record $Y$ taking at most $M$ values, $H(Y)\leq\log_2 M$. For $J$ jointly reported coordinates with at most $r$ levels each, $H(Y)\leq J\log_2 r$; constraints or correlations may reduce this bound. No percentage of “48 parameters lost” follows from either formula without a distribution and a common encoding precision.

| System | Candidate record | Bound or missing specification |
|---|---|---|
| Chakras | Seven rated populations | At most $7\log_2 r$ bits for $r$ levels each; 6 independent continuous coordinates |
| Five skandhas | Five rated populations | At most $5\log_2 r$ bits under that protocol |
| Wu Xing | Five ratings and measured cyclic relations | Rate and relation protocols needed separately |
| Numerology | One of 9 outcomes | At most $\log_2 9$ bits |
| Enneagram | One of 9 types | At most $\log_2 9$ bits; additional ratings change the protocol |
| I Ching | One of 64 hexagrams | At most 6 bits |
| Tarot (Major) | One of 22 cards, or a separate 21-coordinate protocol | One card: at most $\log_2 22$ bits; not 21 measured moduli |
| Kabbalah | Ten scalar readouts and a specified path graph | Precision and independence of readouts must be supplied |
| Astrology | Positions and aspects with stated precision | A count of names does not bound the information in positions |
| Human Design | A compound chart | Joint alphabet and dependencies must be supplied |
| Runes | One of 24 labels, or a sequence | One label: at most $\log_2 24$ bits |
| Alchemy | Seven ratings and a four-class label | Joint protocol and dependencies must be supplied |
| UHM ($\Gamma$) | A density matrix in a fixed frame | 48 continuous interior coordinates; no finite Shannon value without quantisation and a distribution |

### 4.2 Structural comparison of the proposed readouts

The following describes model variables, not an established measurement capability of each tradition.

| Candidate | Populations | Coherences | Further obligation |
|---|---|---|---|
| Chakra readout | All 7 entries, 6 independent | None | Calibrate population ratings |
| I Ching readout | None | Six real-part signs | Fix six pairs, basis and zero convention |
| Tarot coordinate readout | None | 21 moduli | Supply a protocol returning the vector |
| Kabbalah readout | Mixed with coherences | Ten scalar functions | Select formulas and verify the path map |
| Astrological readout | Not in the displayed formula | Moduli and phase bins | Calibrate angles to phases |
| HD composite readout | Depends on component maps | Depends on component maps | Verify joint feasibility and typed relations |
| Full $\Gamma$ model | All 7 entries | All 21 complex entries | Positivity, calibration and specified dynamics |

A static record does not determine dynamics or self-correction. Falsifiability concerns a specified hypothesis and protocol, not a privilege conferred by its vocabulary.

---

## 5. Completeness and minimality {#теорема-полноты}

After analysing more than ten symbolic systems from different eras and cultures, two questions arise: (1) is the formalism $\Gamma$ sufficient to describe everything that these systems describe? and (2) is $\Gamma$ the minimal such formalism?

### 5.1 Predicate pullback [D] {#описательная-полнота}

If $\pi_S:X\to Y_S$ is a specified readout and $P:Y_S\to\{0,1\}$ a predicate on its records, then

$$
\widetilde P=P\circ\pi_S:X\to\{0,1\}.
$$

This is a well-typed pullback, not a theorem that every historical meaning has already been captured. Conversely, a state predicate $Q:X\to\{0,1\}$ factors through $\pi_S$ exactly when it is constant on every fiber of $\pi_S$. Necessity follows by applying the same output predicate to equal records; sufficiency follows by defining that predicate on each attained record using any representative of its fiber. Thus completeness is always relative to an explicitly chosen family of distinctions.

### 5.2 Conditional minimality {#минимальность-гаммы}

The existence of symbolic readouts alone does not imply $N\geq7$. The [current minimality theorem](/docs/proofs/minimality/theorem-minimality-7) supplies two precise routes:

1. A binary status code of minimum distance at least 3, whose radius-one balls partition the full cube, with more than 2 codewords, has length $N\geq7$. At $N=7$ the Hamming code attains this coding bound.
2. A unital faithful $*$-representation of the **specified** algebra $\mathbb C\oplus M_3(\mathbb C)\oplus M_3(\mathbb C)$ in $M_N(\mathbb C)$ exists exactly when $N\geq7$: its three summands require dimensions at least 1,3,3.

Transferring either bound to another architecture requires establishing its premises for that architecture. Calling an object “a living being” or “a soul”, or giving seven roles different names, does not establish those premises. The seven-dimensional UHM realization is a structured candidate; these conditional bounds do not prove that it is the unique encoding of all symbolic vocabularies.

### 5.3 Information loss with an explicit distribution [T] {#информационная-утрата}

Let $X$ be a finite-valued random state description and $Y=\pi_S(X)$ a deterministic readout taking at most $M$ values. Then

$$
H(X\mid Y)=H(X)-H(Y)\geq\max\{0,H(X)-\log_2M\}.
$$

**Proof.** Determinism gives $H(Y\mid X)=0$; the chain rule gives the equality, while $H(Y)\leq\log_2M$ and nonnegativity give the bound. For $J$ coordinates of at most $r$ levels each, use $M\leq r^J$. A hexagram carries at most 6 bits per record, but the actual loss still depends on $H(X)$ and on the map.

There is no distribution-free positive lower bound: for a constant state both entropies are zero. A continuous density matrix requires a probability law and either a stated quantisation or a separately justified differential-entropy/information formulation. Its 48 real coordinates are not a fixed number of bits.

---

## 6. Structural analysis: what determines the stability of a projection {#структурный-анализ}

### 6.1 Fano structure and natural projections

The [Fano plane](/docs/proofs/gap/fano-channel) provides seven associative coordinate triplets in the chosen octonion frame. Every unordered pair belongs to exactly one line. Consequently, “within-triplet” and “between-triplet” coherences do not partition the 21 pairs. A stability statement needs an evolution generator and a comparison of specified perturbations or decay rates; it does not follow from incidence alone.

The cultural labels in the following table are interpretations [I]. A finite classification of configurations under an incidence group can organise these candidates once their domain is specified, but does not prove that every historical symbolic system belongs to that domain or explain its prevalence.

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

**Exact incidence fact.** The three lines through A are $\{A,S,L\}$, $\{E,U,A\}$ and $\{O,A,D\}$. The degree 3 of every point is a theorem of PG(2,2). The cultural interpretation “body–mind–spirit” is a proposed assignment to this structure, not a consequence of that degree.

### 6.2 The seven-dimensional algebraic candidate

For the octonions, $\dim\operatorname{Im}\mathbb O=7$. Hurwitz's theorem classifies finite-dimensional real **normed division algebras** up to isomorphism as $\mathbb R,\mathbb C,\mathbb H,\mathbb O$, with imaginary dimensions 0,1,3,7. It does not give a unique octonion basis or a theorem about the origins of sevenfold traditions. [Baez's exposition](https://math.ucr.edu/home/baez/octonions/node2.html) states the precise algebraic hypotheses. The conditional UHM dimension bounds in §5.2 require their own premises.

### 6.3 Which phase information a readout loses

Hermiticity gives $\gamma_{ji}=\overline{\gamma_{ij}}$. Thus the complete complex upper triangle and diagonal determine the entire state. A readout retaining only moduli loses phase distinctions, while a phase quantiser loses distinctions within its bins. These losses can be demonstrated by distinct positive states with the same readout; they do not establish an intrinsic impossibility of phase measurement.

For nonzero coherences in the fixed semantic frame, [Gap](/docs/core/dynamics/gap-operator) is $\lvert\sin\theta_{ij}\rvert$. The conjugate entries express the two orientations of the same coherence; their interpretation as external and internal aspects is a semantic commitment of UHM. The dagger operation on Hilbert-space morphisms is a contravariant involution; that categorical statement does not turn a single matrix-entry assignment into a functor or an empirical theory of every tradition.

---

## 7. Formalisation of mystical concepts [I] {#мистические-концепты}

A number of cross-cultural phenomenological concepts admit formalisation through the Gap structure. The formulations below are constructive interpretations, not empirically confirmed identities.

| Concept | Formalisation in UHM | Mechanism |
|---|---|---|
| **"Enlightenment"** | L4: $\varphi(\Gamma^*) = \Gamma^*$ — [fixed point](/docs/consciousness/hierarchy/interiority-hierarchy) of self-modelling | Not Gap = 0, but **reflexive transparency**: the system accurately knows its own Gap |
| **"Dark night of the soul"** | Saddle-node [Gap bifurcation](/docs/core/dynamics/gap-phase-diagram#бифуркации): loss of stable Gap profile | The stationary attractor disappears as parameters change |
| **"Kundalini"** | Cascading activation of coherences bottom-up: $\gamma_{OE} \to \gamma_{OD} \to \gamma_{OS} \to \gamma_{OA}$ | The O-dimension sequentially connects with the others |
| **"Synchronicity"** (Jung) | Inter-system $\text{Gap}_{AB}(i,j) \to 0$ for a specific channel | Two [holons](/docs/core/dynamics/composite-systems) temporarily resonate along one dimension |
| **"Non-duality"** (Advaita) | Limit $\text{Gap} \to 0$ for all pairs | Real-valued states attain this algebraically; a dynamical obstruction requires the additional conditions in §9 |
| **"Mandala"** | Visualisation of the Gap profile (heat map $7 \times 7$) | Structured representation of 49 elements |
| **"Karma"** | Non-Markovian memory kernel $K(\tau-s)$ in the [integro-differential equation](/docs/core/dynamics/gap-phase-diagram#немарковские-осцилляции) of Gap dynamics | Past configurations influence current evolution through the memory kernel |
| **"Dharma"** (Buddha) | Attractor $\Gamma^*$ of the evolution equation: the stationary state toward which the system tends as $\tau \to \infty$ | The structure of the equation itself, not a specific configuration |

---

## 8. Fundamental conclusions {#фундаментальные-выводы}

Having analysed more than ten symbolic systems — from the most ancient (chakras, I Ching, alchemy) to modern ones (Human Design, Enneagram) — we can formulate general patterns: why symbolic systems are structured as they are, and what they inevitably cannot describe.

### 8.1 Three precise principles

**1. Readout loss.** A finite-valued record cannot distinguish the continuum of all states. A continuous readout of fewer than 48 real coordinates cannot distinguish the full interior. Neither statement says that a specified finite family of decisions cannot be preserved exactly.

**2. Structural preservation.** A proposed Fano correspondence must preserve the declared incidence relation; an executable correspondence must also preserve definedness and action composition. These are checkable obligations, not consequences of the number 7.

**3. Relative completeness.** A family of observations factors through a readout exactly when each observation is constant on its fibers. A new distinction may require a richer record. This identifies the specific information an interface must retain rather than assigning an unsupported universal loss percentage.

### 8.2 What can remain hidden

The fiber $\pi_S^{-1}(y)$ is the set of model states compatible with a record. When it contains states with different values of a requested observable, that observable is not identifiable by this protocol. For example, modulus data alone may leave phase ambiguous. Supplying a complete formal state space describes this ambiguity but does not by itself recover the actual state.

The external/internal interpretation of UHM coherences is distinct from this statistical identifiability question. An imaginary part is not mathematically unobservable merely because it changes sign under conjugation. Its operational accessibility depends on the measurement model.

### 8.3 Descriptive coherence and testing [I]

A proposed correspondence is useful when it preserves substantive, independently specified distinctions and operations. The tables supply candidates for that task. Predicate pullback (§5.1) does not prove that every phenomenological claim of every tradition is captured.

Tests must fix the maps, output protocols, noise assumptions and target predictions before evaluating held-out data. An observed violation of a claimed relation or commuting action diagram refutes that particular structural map. Failure of its registered empirical predictions challenges the calibrated model. Counting more than 7 real parameters is not a refutation of a state space with 48 real coordinates; arbitrary post-hoc remappings cannot substitute for such tests.

---

## 9. What would establish a Gap obstruction? {#защита-gap}

**Counterexample to unconditional ineliminability [T].** Let $J$ be the all-ones $7\times7$ matrix and

$$
\Gamma_\varepsilon=I/7+\varepsilon(J-I),\qquad0<\varepsilon<1/7.
$$

Its eigenvalues are $1/7+6\varepsilon$ once and $1/7-\varepsilon$ six times, so it is positive definite with trace 1. All 21 offdiagonal entries equal the nonzero real number $\varepsilon$. Every phase and every pairwise Gap is zero. Thus seven-dimensional octonionic background structure alone does not forbid zero-Gap density matrices.

A theorem excluding such states from a specified **viable dynamical regime** needs additional assumptions. The following are distinct research obligations:

| Proposed source | Required bridge to a Gap obstruction |
|---|---|
| Hamming code | Define the map from a seven-bit code to 21 pair phases and prove the claimed phase constraint; minimum Hamming distance alone supplies none |
| Octonion associator | Specify how the nonassociative product enters the evolution of $\Gamma$ and forces a nonzero phase |
| Energetic potential | Establish its admissible domain, minima and stability; a stipulated potential is not a universal constraint on density matrices |
| Self-modelling/fixed points | Prove a phase constraint for the chosen self-model; a fixed-point theorem alone does not require a nonzero Gap |
| Topological sector | Define the configuration map, boundary conditions, nontrivial sector and allowed homotopies; an ambient nonzero homotopy group does not place every configuration in a nontrivial sector |

The corresponding [dynamical and topological models](/docs/core/dynamics/gap-phase-diagram) must be read with those premises. None of these mathematical questions establishes a universal historical claim about what all symbolic traditions regarded as attainable.

---

## 10. Where symbolic systems live: emergent interfaces of nestedness {#онтологическое-место}

:::info Owner's question, crystallised (2026-08)
If UHM is everything and everything derives from it — where exactly does a symbolic system sit in the ontology? The answer that survives the analysis of this chapter and the empirical programme: **on the emergent levels, as an interface of a concrete nestedness** — never in the core.
:::

### 10.1 The claim [О/И]

A symbolic system can be modelled as an **interface that an emergent level builds to the core**: a finite vocabulary in which one holon at one rung of the cosmic nesting — Earth → planetary system → galactic arm → Galaxy → … — reads its own state against the *shared clock of its neighbourhood*. For the clock-based subclass, three modelling considerations motivate this placement:

1. **The vocabulary is tied to the rung, not to the core.** The astronomical traditions considered here sample the *local sky*: the bodies visible from Earth, their periods, their returns. The core ($\Gamma$, the 21 coherences, the thresholds) contains no ephemerides — the [lattice theorems](/docs/applied/research/homoholograph#x-lattices) prove the traditional grids (nakshatras, padas, navamshas) do **not** embed in the native lines, and the [era analysis of Human Design](/docs/applied/research/human-design#эпохи) shows its "constants" are functions of the outer planets' epoch — properties of the neighbourhood, not of the person.
2. **Geocentrism is a reference frame, not an error.** "Earth as the ship, I at the centre" is the *correct covariant choice* for a holon whose body rides this planet: an ephemeris is the shared atlas-clock of the local nesting (the [blueprint](/docs/applied/research/prime-radiant#чертёж) row "astrology = deterministic shared clock"), and the [geo-layer](/docs/applied/research/homoholograph#часть-xxii-углы-места) reads *place* as a re-calibration of the same frame. A holon riding a different body — or none — would build a different atlas with the same functor.
3. **The interface can be parameterised by its environment.** A proposed clock-based interface can take environmental periods and observations as inputs in addition to $\Gamma$. Applying it to another holon requires an operational encoding and the structural contract of §1.1. The formal possibility of these inputs does not prove that every environment supplies a suitable clock or that the same calibrated readout transfers.

### 10.2 Research commitments [I]

- **Clock-based interfaces:** test the decomposition *Encoder + environmental atlas-clock + alphabet* on systems for which time/place observations are part of the declared input. Extending it to non-astronomical traditions requires a separate argument.
- **Expressive limits:** a finite record cannot recover every continuous state distinction. It can still preserve specified observables exactly, including selected phase distinctions, when its protocol measures them.
- **Native construction:** the [Γ-Canon](/docs/applied/research/gamma-canon) builds an interface from declared UHM structures. Its advantage is that incidence, coding and action obligations can be checked directly. Uniqueness, superiority of every readout, and empirical calibration do not follow from that construction alone.

### 10.3 Status honesty

The *placement* (emergent interface, not core) is [D]-convention resting on [T]-anchors (lattice non-embedding, era-functions, Kepler bias, the Enc functor). The *generalisation to arbitrary holons* is a research direction [P]: it becomes testable exactly when a second nestedness is instrumented (a long-duration crew, a non-terrestrial holon, an artificial holon with its own periodic neighbourhood — the [environment mandate](/docs/applied/research/homoholograph#часть-xxiv-мир-как-холон) is the first step). Until then it earns its keep as the *organising frame* that already explains why traditions look the way they do — and why none of them could have been the core.

---

## Related documents

- [Coherence matrix](/docs/core/dynamics/coherence-matrix) — definition of $\Gamma$
- [Seven dimensions](/docs/core/structure/dimensions) — A, S, D, L, E, O, U
- [Gap operator](/docs/core/dynamics/gap-operator) — measure of divergence between external and internal
- [Gap semantics](/docs/physics/dual-aspect/gap-semantics) — 49-element map
- [Gap diagnostics](/docs/applied/research/gap-diagnostics) — applied methodology
- [Interiority hierarchy](/docs/consciousness/hierarchy/interiority-hierarchy) — levels L0–L4
- [Γ-Canon](/docs/applied/research/gamma-canon) — the generative counterpart: the canonical UHM-native symbolic system
- [Symbolic correspondences](/docs/applied/research/symbolic-correspondence) — operationalisation
- [Fano channel](/docs/proofs/gap/fano-channel) — associative triplets and codes
- [Theorem on minimality N = 7](/docs/proofs/minimality/theorem-minimality-7) — why 7

- [Structural correspondences](/docs/applied/research/structural-correspondence) — typed relation/action maps and exact finite examples
