---
sidebar_position: 5
title: "Символические соответствия"
slug: /applied/research/symbolic-correspondence
description: "Operationalization of symbolic correspondences: back-projection protocol, correspondence tables (zodiac, hexagrams, arcana), research program"
---

# Symbolic Correspondences

:::info Who This Chapter Is For
Operationalization of bridges between symbolic systems and the Gap formalism: the back-projection protocol and correspondence tables.
:::


Operationalization of bridges between [symbolic systems](/docs/core/structure/symbolic-systems) and the Gap formalism: the back-projection protocol, specific correspondence tables, and an empirical verification program.

:::warning Status [P]
All material is a **research program**. The correspondence tables are constructive, but empirical verification has not been conducted.
:::

---

## 1. Back-Projection Protocol {#обратная-проекция}

### 1.1 Task

For a description in terms of symbolic system $S$, recover the Gap profile:

$$
\pi_S^{-1}: \mathcal{C}_S \to \text{Hol}
$$

:::warning Warning
The back-projection $\pi_S^{-1}$ is **not unique** — projection loses information. Recovery is defined up to the kernel $\ker(\pi_S)$.
:::

### 1.2 Algorithm

1. **Input:** Description in terms of system $S$ (birth chart, hexagram, spread, etc.)
2. **Mapping:** Translation of elements of $S$ into components of $\Gamma$ via the correspondence table (§2–4)
3. **Completion:** Recovery of missing components of $\Gamma$ via:
   - [Fano constraints](/docs/physics/gauge-symmetry/fano-selection-rules) (coherences on the same Fano line are linked)
   - Positive semidefiniteness condition $\Gamma \geq 0$
   - Minimization of [information entropy](/docs/core/dynamics/gap-thermodynamics) under the given constraints
4. **Output:** Full [transparency map](/docs/applied/research/gap-diagnostics) $7 \times 7$

### 1.3 Worked Example: Three-Card Spread [I] {#пример-расклад}

We demonstrate the algorithm on a concrete three-card Tarot spread.

#### Step 1. Input

A three-card spread (past / present / future):

| Position | Card | Number |
|----------|------|--------|
| Past | The Fool | 0 |
| Present | The Lovers | VI |
| Future | The Tower | XVI |

#### Step 2. Mapping via Table (§4)

Each arcanum maps to an element of $\Gamma$ according to the canonical correspondence (§4.1):

- **The Fool (0):** $\Gamma \propto I/7$ — fully decohered state, all coherences equal zero. In the context of the spread this is not a separate coherence, but a **reference state** — the point of maximum entropy.
- **The Lovers (VI):** $\gamma_{AE}$ — coherence between [Articulation](/docs/core/structure/dimension-a) and [Interiority](/docs/core/structure/dimension-e). Semantics: *discernment through experience*, choice based on inner feeling.
- **The Tower (XVI):** $\gamma_{DS}$ — coherence between [Dynamics](/docs/core/structure/dimension-d) and [Structure](/docs/core/structure/dimension-s). Semantics: *destruction of form through action*, catastrophic collapse of a stable structure.

#### Step 3. Forming the Partial Profile

Two coherences and one reference state are directly specified by the spread. We write:

$$
\text{Known: } |\gamma_{AE}| > 0, \quad |\gamma_{DS}| > 0, \quad \text{background} = I/7
$$

The temporal ordering of the spread defines a **dynamic trajectory**:

$$
\Gamma(t_0) \approx I/7 \;\xrightarrow{\text{activation } \gamma_{AE}}\; \Gamma(t_1) \;\xrightarrow{\text{activation } \gamma_{DS}}\; \Gamma(t_2)
$$

Interpretation: the system started from an undifferentiated state (The Fool), passed through a phase of articulatory-interiority coupling (The Lovers), and is moving toward the destruction of structural-dynamic coherence (The Tower).

#### Step 4. Completion via Fano Constraints

The coherences $\gamma_{AE}$ and $\gamma_{DS}$ lie on **different** [Fano lines](/docs/physics/gauge-symmetry/fano-selection-rules). However, the Fano geometry $\mathrm{PG}(2,2)$ links coherence triplets: if two of the three on one line are known, the third is constrained. In this case:

- The line containing $\gamma_{AE}$ also contains coherences with $O$ and $U$ (depending on the specific line). Fano condition: $\gamma_{AE} \cdot \gamma_{EO} \cdot \gamma_{AO}$ satisfies closure.
- The line containing $\gamma_{DS}$ links $D$, $S$, and a third dimension. An analogous constraint.

The remaining 19 coherences are recovered via:

$$
\Gamma^* = \arg\min_{\Gamma \geq 0} S(\Gamma) \quad \text{subject to } \gamma_{AE} = c_1, \; \gamma_{DS} = c_2, \; \text{Tr}(\Gamma) = 1
$$

where $S(\Gamma) = -\text{Tr}(\Gamma \ln \Gamma)$ — von Neumann entropy. The maximum entropy principle under fixed constraints gives the **least biased** completion.

#### Step 5. Output

The result is a partial [transparency map](/docs/applied/research/gap-diagnostics) of size $7 \times 7$ with two "highlighted" coherences ($\gamma_{AE}$, $\gamma_{DS}$) and an entropy background for the rest.

:::warning Example Limitations
Three cards out of 22 specify only $\sim 10\%$ of the information about the coherence profile. A full spread (e.g., Celtic Cross, 10 cards) provides substantially more constraints, but it too does not recover $\Gamma$ uniquely due to the loss of phases and the diagonal (see §4.2).
:::

---

## 2. Zodiac Correspondences [I] {#зодиак}

### 2.1 Principle

12 zodiac signs map to 12 pairs from $\{A, S, D\} \times \{L, E, O, U\}$ — the intersection of the spatial triplet with the inner quartet:

| Sign | Pair $(i,j)$ | Element | Gap interpretation |
|------|-------------|---------|-------------------|
| Aries | $(D, E)$ | Fire | Dynamics-Interiority: action through experience |
| Taurus | $(S, O)$ | Earth | Structure-Ground: stability in being |
| Gemini | $(A, L)$ | Air | Articulation-Logic: expression through thought |
| Cancer | $(S, E)$ | Water | Structure-Interiority: body and feeling |
| Leo | $(D, O)$ | Fire | Dynamics-Ground: creative force |
| Virgo | $(A, O)$ | Earth | Articulation-Ground: discernment of essence |
| Libra | $(A, E)$ | Air | Articulation-Interiority: aesthetic harmony |
| Scorpio | $(D, L)$ | Water | Dynamics-Logic: transformation of understanding |
| Sagittarius | $(D, U)$ | Fire | Dynamics-Unity: aspiration toward wholeness |
| Capricorn | $(S, L)$ | Earth | Structure-Logic: systematic construction |
| Aquarius | $(A, U)$ | Air | Articulation-Unity: holistic vision |
| Pisces | $(S, U)$ | Water | Structure-Unity: dissolution into wholeness |

### 2.2 Elements

| Element | Triplet dimension | Characteristic |
|---------|------------------|----------------|
| Fire | $D$ (Dynamics) | Activity, transformation |
| Earth | $S$ (Structure) | Stability, form |
| Air | $A$ (Articulation) | Discernment, communication |
| Water | — (alternating) | Connection via $E$ (Interiority) |

---

## 3. I Ching Hexagrams [I] {#гексаграммы}

### 3.1 Principle

64 hexagrams = $2^6$ binary signatures of 6 of the 7 [dimensions](/docs/core/structure/dimensions) (excluding $U$):

$$
\pi_{\text{yijing}}(\Gamma) = \left(\text{sgn}(\text{Re}(\gamma_{ij}))\right)_{(i,j) \in \mathcal{S}_6}
$$

Each line (yin/yang) = the sign of the real part of the coherence.

### 3.2 Example

| Line | Pair | Yang ($\text{Re} > 0$) | Yin ($\text{Re} < 0$) |
|------|------|----------------------|----------------------|
| 1 (bottom) | $O$ | Active ground | Hidden ground |
| 2 | $E$ | Open experience | Suppressed experience |
| 3 | $L$ | Clear logic | Confused logic |
| 4 | $D$ | Active dynamics | Stagnation |
| 5 | $S$ | Stable structure | Instability |
| 6 (top) | $A$ | Clear articulation | Inexpressiveness |

### 3.3 Information Loss

I Ching loses: (a) phase continuity $\theta \in [0, 2\pi)$ → binary projection; (b) the 7th dimension $U$ (Unity); (c) all imaginary parts $\text{Im}(\gamma_{ij})$ — the entire Gap profile.

---

## 4. Tarot Major Arcana [I] {#таро}

### 4.1 Principle

22 Major Arcana $\approx$ 21 coherences + 1 null element (The Fool = $\Gamma \propto I/7$, [fully decohered system](/docs/applied/research/gap-diagnostics#модельные-системы)):

$$
\pi_{\text{tarot}}: \{\gamma_{ij}\}_{i<j} \cup \{I/7\} \to \{0, I, II, \ldots, XXI\}
$$

### 4.2 Information Loss

Tarot loses: (a) populations $\gamma_{ii}$ (diagonal); (b) phases $\theta_{ij}$ (continuous information); (c) dynamics ($d\Gamma/d\tau$); (d) the distinction between Map_ext / Map_int.

---

## 5. Chakra System [I] {#чакры}

:::warning Hypothesis Status
The table below is **one of 120 possible** bijections of the middle chakras onto dimensions (with fixed boundary identifications O↔Muladhara and U↔Sahasrara). For detailed categorical analysis, including the incompatibility of the linear order of chakras with the Fano geometry PG(2,2), see [Symbolic Systems: §3.1 Chakras](/docs/core/structure/symbolic-systems#чакры).
:::

7 chakras $\approx$ 7 populations $\gamma_{ii}$ ([diagonal of $\Gamma$](/docs/core/dynamics/coherence-matrix)):

| Chakra | Dimension | $\gamma_{ii}$ |
|--------|-----------|--------------|
| Muladhara | $O$ ([Ground](/docs/core/structure/dimension-o)) | $\gamma_{OO}$ |
| Svadhisthana | $E$ ([Interiority](/docs/core/structure/dimension-e)) | $\gamma_{EE}$ |
| Manipura | $D$ ([Dynamics](/docs/core/structure/dimension-d)) | $\gamma_{DD}$ |
| Anahata | $L$ ([Logic](/docs/core/structure/dimension-l)) | $\gamma_{LL}$ |
| Vishuddha | $A$ ([Articulation](/docs/core/structure/dimension-a)) | $\gamma_{AA}$ |
| Ajna | $S$ ([Structure](/docs/core/structure/dimension-s)) | $\gamma_{SS}$ |
| Sahasrara | $U$ ([Unity](/docs/core/structure/dimension-u)) | $\gamma_{UU}$ |

The chakra system loses: all 42 coherences (21 external + 21 internal), the Gap structure, and dynamics.

---

## 6. Research Program [P] {#программа}

:::warning Status [P]
This entire section is a **research program**. None of the hypotheses has yet been empirically verified. The proposed design is the minimum required for rigorous testing.
:::

### 6.1 Hypotheses {#гипотезы}

#### H-SC1: Zodiac-Gap Correlation [P]

**Formulation.** For a subject with a birth chart in which sign $Z_k$ dominates, the corresponding coherence $\gamma_{ij}(Z_k)$ (per the table in §2.1) is statistically significantly above the mean.

**Specific prediction.** Subjects with dominant Aries ($Z_1 = \text{Aries} \mapsto (D, E)$) have $|\gamma_{DE}| > \langle|\gamma_{DE}|\rangle_{\text{pop}}$ with effect size $d \geq 0.3$ (small, per Cohen).

**Justification.** If the zodiac correspondences (§2) reflect a real structure, the population of certain coherences should correlate with astrological configurations.

#### H-SC2: Predictive Power of I Ching Back-Projection [P]

**Formulation.** The hexagram obtained from a subject's measured Gap profile via direct projection $\pi_{\text{yijing}}(\Gamma)$ matches the hexagram chosen by the subject in a ritual context more often than random selection (chance level = 1/64).

**Specific prediction.** Match frequency $\geq 3/64$ (3+ times above chance level), $p < 0.01$ by Fisher's exact test.

**Justification.** If I Ching is a projection of $\Gamma$ (§3), then a subject intuitively choosing a hexagram implicitly reads the sign structure of their own $\Gamma$.

#### H-SC3: Inter-System Consistency [P]

**Formulation.** For a single subject, partial $\Gamma$-profiles recovered from different symbolic systems ($S_1, S_2, S_3$) agree in common components to within $\|\Delta\Gamma\|_F < \varepsilon_{\text{crit}}$.

**Specific prediction.** The correlation between $\gamma_{ii}$ from chakra diagnostics and $\gamma_{ii}$ from the zodiac chart is $r \geq 0.4$ (see also §7).

**Justification.** If all symbolic systems are projections of one $\Gamma$ (the central thesis of [Symbolic Systems](/docs/core/structure/symbolic-systems)), their recovered profiles must be compatible.

### 6.2 Methodology {#методология}

#### Sample

| Parameter | Value | Justification |
|-----------|-------|---------------|
| $N$ (total size) | $\geq 200$ | Power 0.80 at $d = 0.3$, $\alpha = 0.01$ |
| Groups for H-SC1 | 12 zodiac groups $\times$ $\geq 17$ subjects | Uniform coverage of signs |
| Group for H-SC2 | $\geq 100$ subjects with dual measurement | Sufficient for Fisher's exact test |
| Control group | $\geq 50$ subjects without knowledge of symbolic systems | Control for expectation effect |

#### Measurement Instruments

1. **Gap profile:** [Dual Interview Protocol](/docs/applied/research/gap-diagnostics#протокол) — standardized procedure with external and internal modules.
2. **Birth chart:** Standard astrological software (fixed ephemerides, Placidus house system for uniformity).
3. **I Ching:** Ritual coin toss (6 throws × 3 coins) under standardized conditions.
4. **Chakra diagnostics:** Bioenergetic self-assessment questionnaire (7 scales, validated on a Russian-speaking sample; if none exists — development and pre-validation as a separate stage).
5. **Tarot:** Standardized spread (Celtic Cross, 10 cards) with double-blind coding.

#### Statistical Tests

| Hypothesis | Test | Correction |
|------------|------|------------|
| H-SC1 | One-sample $t$-test for each of the 12 groups, Cohen's effect size $d$ | Bonferroni ($\alpha_{\text{adj}} = 0.01/12$) |
| H-SC2 | Fisher's exact test (match/mismatch vs. chance 1/64) | No correction (single hypothesis) |
| H-SC3 | Intraclass correlation ICC(3,1) between projections | Bootstrap 95% CI |

#### Artifact Control

- **Double blinding:** The Gap diagnostics operator does not know the subject's astrological data.
- **Order randomization:** Symbolic systems are presented in random order.
- **Pre-registration:** Protocol and analysis plan are published before data collection begins (OSF or equivalent).

### 6.3 Expected Outcomes {#ожидаемые-исходы}

#### If Confirmed

| Hypothesis | Result | Consequence |
|------------|--------|-------------|
| H-SC1 confirmed | $d \geq 0.3$ for $\geq 6$ of 12 signs | Zodiac correspondences (§2) transition from [I] to [C] — conditionally confirmed |
| H-SC2 confirmed | Match $\geq 3/64$ | I Ching as a projection of $\Gamma$ (§3) transitions from [I] to [C]; the question of the readout mechanism opens up |
| H-SC3 confirmed | ICC $\geq 0.4$ | The central thesis on [the unity of projections](/docs/core/structure/symbolic-systems) receives empirical support |

#### If Refuted

| Hypothesis | Result | Consequence |
|------------|--------|-------------|
| H-SC1 refuted | $d < 0.1$ for $\geq 10$ signs | The zodiac table (§2) is erroneous or astrology does not reflect $\Gamma$ |
| H-SC2 refuted | Match $\leq 1/64$ | The I Ching projection (§3) does not work; revision of the binary encoding |
| H-SC3 refuted | ICC $< 0.2$ | The systems project **different** objects, not one $\Gamma$ — fatal for the unity thesis |

### 6.4 Falsification Criteria {#фальсификация}

The symbolic correspondences approach is **definitively refuted** if at least one of the following conditions holds:

1. **Zero inter-system correlation.** ICC between partial $\Gamma$-profiles from three or more independent symbolic systems for one subject does not differ from zero ($\text{ICC} < 0.05$, $N \geq 200$). This means the symbolic systems do not project a common object.

2. **Randomness of direct projection.** The direct projection $\pi_S(\Gamma_{\text{measured}})$ for measured $\Gamma$ does not predict the subject's symbolic description better than random selection for any of the four systems $S$ (zodiac, I Ching, Tarot, chakras), $N \geq 200$, $p > 0.10$ for all.

3. **Fano closure violation.** Recovered coherences systematically violate [Fano constraints](/docs/physics/gauge-symmetry/fano-selection-rules) — coherence triplets on one Fano line are incompatible with $\Gamma \geq 0$ in $> 50\%$ of cases.

4. **Control invariance.** The result of back-projection $\pi_S^{-1}$ is statistically indistinguishable for radically different subjects (e.g., healthy adult vs. patient with severe disorder), indicating zero diagnostic sensitivity.

:::info Principle
No single negative result for an **individual** symbolic system refutes the approach as a whole — it only shows that the given correspondence table is wrong. Falsification requires a negative result **for all systems simultaneously** (criterion 2) or a negative result **for inter-system consistency** (criterion 1).
:::

---

## 7. Inter-System Coherence {#межсистемная-когерентность}

:::warning Status [I]
The formal consistency condition is an **interpretation**. Empirical verification is part of the [research program](#программа) (H-SC3).
:::

### 7.1 Problem Statement

Let back-projections from $K$ symbolic systems be performed for one and the same subject (holon) with true coherence matrix $\Gamma^*$:

$$
\hat{\Gamma}_1 = \pi_{S_1}^{-1}(s_1), \quad \hat{\Gamma}_2 = \pi_{S_2}^{-1}(s_2), \quad \ldots, \quad \hat{\Gamma}_K = \pi_{S_K}^{-1}(s_K)
$$

Each $\hat{\Gamma}_k$ is the best recovery of $\Gamma^*$ from the data of system $S_k$ (algorithm §1.2). Question: **do these recoveries agree?**

### 7.2 Formal Consistency Condition {#условие-согласованности}

**Definition.** The set of recoveries $\{\hat{\Gamma}_k\}_{k=1}^K$ is **consistent** if there exists a single $\Gamma^* \geq 0$, $\text{Tr}(\Gamma^*) = 1$, such that:

$$
\boxed{\forall k: \quad \left\| P_k \, \hat{\Gamma}_k \, P_k - P_k \, \Gamma^* \, P_k \right\|_F < \varepsilon_k}
$$

where $P_k$ is the orthogonal projector onto the subspace "visible" to system $S_k$, and $\varepsilon_k$ is the admissible error determined by the information loss of $\pi_{S_k}$.

Equivalent formulation via intersections:

$$
\bigcap_{k=1}^K \mathcal{B}_k(\hat{\Gamma}_k, \varepsilon_k) \neq \varnothing
$$

where $\mathcal{B}_k(\hat{\Gamma}_k, \varepsilon_k) = \{\Gamma \geq 0 : \|P_k \Gamma P_k - P_k \hat{\Gamma}_k P_k\|_F < \varepsilon_k, \; \text{Tr}(\Gamma)=1\}$ — the set of admissible $\Gamma$ given the data of system $S_k$.

### 7.3 Example: Chakras + Zodiac + Tarot {#пример-три-системы}

Consider a specific situation with three systems for one subject:

| System | What it sees | $P_k$ |
|--------|-------------|-------|
| Chakras (§5) | 7 populations $\gamma_{ii}$ | $P_{\text{chakras}} = \text{diag}(1,1,1,1,1,1,1)$ |
| Zodiac (§2) | 12 coherences $|\gamma_{ij}|$ for pairs $(i,j) \in \{A,S,D\} \times \{L,E,O,U\}$ | $P_{\text{zod}}$ — projector onto 12 off-diagonal elements |
| Tarot (§4) | 21 coherences $|\gamma_{ij}|$ ($i < j$) | $P_{\text{tarot}}$ — projector onto the full upper triangle |

**Consistency means:**

1. The populations $\gamma_{ii}$ from chakra diagnostics and the populations recovered from the zodiac profile via completion (§1.2, step 3) must agree within $\varepsilon$.
2. The twelve coherences specified by the zodiac must be a subset of the 21 coherences specified by the Tarot, to within $\varepsilon$.
3. All constraints simultaneously must admit a single $\Gamma^* \geq 0$.

Formally:

$$
\left\| \text{diag}(\hat{\Gamma}_{\text{chakras}}) - \text{diag}(\hat{\Gamma}_{\text{zod}}) \right\|_2 < \varepsilon_1
$$

$$
\left\| \hat{\gamma}_{ij}^{(\text{zod})} - \hat{\gamma}_{ij}^{(\text{tarot})} \right\| < \varepsilon_2 \quad \forall (i,j) \in \{A,S,D\} \times \{L,E,O,U\}
$$

### 7.4 Diagnosing Inconsistency {#диагностика-несогласованности}

If $\bigcap_k \mathcal{B}_k = \varnothing$ (the intersection is empty), three interpretations are possible:

#### 7.4.1 Error in the Correspondence Table

One or more tables (§2–5) contain an incorrect identification "symbol $\leftrightarrow$ element of $\Gamma$". This is the most likely cause and the least fatal: correcting the table may restore consistency.

**Diagnostic sign:** The inconsistency *systematically* affects the same system $S_k$ for different subjects.

#### 7.4.2 Different Temporal Cross-Sections

Symbolic systems describe $\Gamma$ at different moments in time: a birth chart captures $\Gamma(t_{\text{birth}})$, chakra diagnostics — $\Gamma(t_{\text{now}})$, a Tarot spread — $\Gamma(t_{\text{question}})$. The divergence reflects the real [dynamics $d\Gamma/d\tau$](/docs/core/dynamics/evolution), not a correspondence error.

**Diagnostic sign:** The inconsistency grows with the temporal gap between the "snapshot" moments.

#### 7.4.3 Fundamental Incompatibility

The symbolic systems **are not** projections of a single object. This is the fatal outcome for the unity thesis, equivalent to falsification criterion §6.4, item 1.

**Diagnostic sign:** The inconsistency *does not decrease* with (a) table corrections, (b) temporal cross-section synchronization, (c) sample size increase.

### 7.5 Inter-System Coherence Measure {#мера-когерентности}

For quantitative assessment, we introduce the **inter-system coherence index**:

$$
\mathcal{I}_K = 1 - \frac{\min_{\Gamma^* \geq 0} \sum_{k=1}^K w_k \|P_k \Gamma^* P_k - P_k \hat{\Gamma}_k P_k\|_F^2}{\sum_{k=1}^K w_k \|P_k \hat{\Gamma}_k P_k\|_F^2}
$$

where $w_k = \dim(\text{Im}(P_k)) / \sum_j \dim(\text{Im}(P_j))$ — the weight of the system, proportional to the number of "visible" parameters.

| $\mathcal{I}_K$ | Interpretation |
|------------------|---------------|
| $\geq 0.8$ | High consistency — the systems project one object |
| $0.4$–$0.8$ | Moderate — table errors or temporal mismatches are possible |
| $< 0.4$ | Low — the unity thesis is questionable |
| $\leq 0$ | Complete incompatibility — falsification (§6.4, item 1) |

---

## Related Documents

- [Symbolic systems](/docs/core/structure/symbolic-systems) — formal reduction
- [Gap diagnostics](/docs/applied/research/gap-diagnostics) — applied methodology
- [Gap semantics](/docs/physics/dual-aspect/gap-semantics) — 49-element map
- [Measurement protocol](/docs/applied/research/measurement-protocol) — experimental verification
