---
sidebar_position: 7
title: "Symbolic Correspondences"
slug: /applied/research/symbolic-correspondence
description: "Operationalization of symbolic correspondences: back-projection protocol, correspondence tables (zodiac, hexagrams, arcana), research program"
---

# Symbolic Correspondences

:::info Who This Chapter Is For
Operationalization of bridges between symbolic systems and the Gap formalism: the back-projection protocol and correspondence tables.
:::


Operationalization of bridges between [symbolic systems](/docs/core/structure/symbolic-systems) and the Gap formalism: the back-projection protocol, specific correspondence tables, and an empirical verification program.

:::warning Status [P] — with an execution ledger
The correspondence tables are constructive; the verification programme of §6 was written before any instrument ran. Since then a substantial part of it **has been executed** in the holon laboratory — see §0 for what is now measured, what died, and what replaced the original designs. Section 6 retains the historical proposed protocol with an explicit correction; §7 supplies the revised joint-consistency contract.
:::

## 0. Execution state (2026-08) {#состояние}

The programme below was drafted for interview-based instruments. The laboratory that actually materialised (the [HomoHoloGraph programme](/docs/applied/research/homoholograph)) is harder-edged: deterministic engines, pre-registered nulls, replication before status. The ledger, honestly:

| Original design | What actually ran | Verdict |
|---|---|---|
| H-SC1: zodiac sign ↔ trait coherences | Natal→trait on the strongest external corpus: Gauquelin-class, $n=15\,931$ | **Null** (all $\eta^2 < 0.5\%$) — the strongest form of H-SC1 is dead; [details](/docs/applied/research/homoholograph#x-nulls) |
| H-SC2: I Ching back-projection | The wheel dissected instead: HD = ephemeris-clocked sampler over the hexagram alphabet; antipodal law 32/32, Gray-locality, trigram–center MI — all [Т-computed] | The *structure* is real mathematics; the *human layer* remains untested as designed |
| H-SC3: inter-system consistency | Lattice theorems: nakshatra/pada/navamsha grids **do not embed** in the native lines [T]; sidereal-vs-tropical duel on events and 3 000 deaths | **Systems are not projections of one grid**; longitude systems indistinguishable from chance on dates — consistency question dissolved rather than answered |
| Timing claims (implicit in all tables) | The full oracle programme: 5 mask optics + distribution tests + ML-grade information detector on deaths corpora | **Null across the board** for date-level claims; one [I]-trace (maraka) lives in forward envelopes |
| Chakra questionnaire (§6.2) | Replaced by the native instrument stack: voice diary, tomograph, passive observation channel | The native alphabet made the borrowed questionnaire obsolete |

**Where the programme now lives:** the ontological placement of symbolic systems is stated in [Symbolic systems §10](/docs/core/structure/symbolic-systems#онтологическое-место); the native system built from the core outward is the [Γ-Canon](/docs/applied/research/gamma-canon) plus the native seasons layer; the forward-validation machinery (sealed envelopes, two-engine duels) replaces retrospective correlation designs — retrospection on this class of data has been exhausted honestly.

---

## 1. Back-projection as a constrained inverse problem {#обратная-проекция}

### 1.1 Task

First specify the projection, its domain and its [structural-role contract](/docs/applied/research/structural-correspondence). For an observation $c$ in system $S$, the inverse object is a fibre, which may be empty:

$$
\mathcal F_S(c)=\{\Gamma\in\mathcal D(\mathbb C^7):\pi_S(\Gamma)=c\}.
$$

It is a set of compatible states, not an inverse function. A nonlinear projection has equivalence classes of indistinguishable states, not generally a linear kernel. Empty means incompatible constraints; several states mean incomplete identification. A chosen representative must retain this distinction.

### 1.2 Algorithm

1. **Input:** retain the description, its source and time, and the particular symbolic convention.
2. **Translation:** derive constraints only through the declared correspondence. A card name or narrative supplies no measured numerical coherence by itself.
3. **Feasibility:** impose Hermiticity, trace one and positive semidefiniteness, then the translated constraints. Add Fano-dependent restrictions only when an explicit model supplies them; incidence alone does not fill entries.
4. **Completion:** for a nonempty compact convex feasible set with affine observation constraints, a possible completion is

$$
\Gamma^*=\operatorname*{arg\,max}_{\Gamma\in\mathcal F_S(c)}S(\Gamma),\qquad
S(\Gamma)=-\operatorname{Tr}(\Gamma\ln\Gamma).
$$

Continuity gives existence and strict concavity gives a unique maximizer. This selects a maximum-entropy representative; it does not establish that the person's state equals it. Open sign constraints or nonlinear constraints need separate existence/uniqueness analysis. Minimizing entropy would instead favour concentrated states and is not this prescription.

5. **Output:** report the feasible constraints, uncertainty, selection rule, and the resulting [transparency map](/docs/applied/research/gap-diagnostics). Predictions require a calibrated observation/dynamics model.

### 1.3 Worked example: three-card spread [I] {#пример-расклад}

Consider the ordered narrative “The Fool; The Lovers; The Tower”. Under the illustrative convention of this chapter, these point to the reference state $I/7$, the pair $AE$ and the pair $DS$. Their native roles remain the [canonical UHM coherence roles](/docs/core/dynamics/coherence-matrix): the narrative interpretations “choice” or “destruction” are extra hypotheses about their context and evolution.

The ordering supplies three narrative positions. It does not measure a trajectory $\Gamma(t)$, and a reference background $I/7$ must not be imposed as the exact same state as nonzero off-diagonal entries. Suppose a separate, declared observation procedure supplies $\gamma_{AE}=c_1$ and $\gamma_{DS}=c_2$. Then

$$
\mathcal F=\{\Gamma\succeq0:\operatorname{Tr}\Gamma=1,
\ \gamma_{AE}=c_1,\ \gamma_{DS}=c_2\}
$$

is the affine feasibility problem to solve. If nonempty, maximum entropy chooses one completion. The cards do not determine $c_1,c_2$ or a percentage of the 48 real parameters.

In the named Fano convention used by the corpus, $AE$ belongs to $\{A,E,U\}$ and $DS$ to $\{S,D,E\}$. Their triples are different and share $E$. A precise joint restriction comes from the $3\times3$ principal determinant, for any triple $(i,j,k)$:

$$
\gamma_{ii}\gamma_{jj}\gamma_{kk}
+2\operatorname{Re}(\gamma_{ij}\gamma_{jk}\gamma_{ki})
-\gamma_{ii}|\gamma_{jk}|^2-\gamma_{jj}|\gamma_{ik}|^2
-\gamma_{kk}|\gamma_{ij}|^2\ge0.
$$

This constrains the third coherence when enough of the other quantities are specified, but does not guarantee unique recovery in general. Typically two pair values leave a family of matrices; on the PSD boundary special data can force a unique completion. For example, if all three populations and the first two coherences equal $1/3$, this determinant becomes $-|\gamma_{ki}-1/3|^2/3$, forcing $\gamma_{ki}=1/3$. Identifying a state still does not identify its dynamics. The explicit cycle and support conditions are developed in [structural correspondence §5](/docs/applied/research/structural-correspondence#фазовые-циклы).

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

The table is a semantic proposal. Its $3\times4$ cardinality does not establish preservation of the zodiac circle, triplicities or modalities. In particular, the split $\{A,S,D\}$ is not a line of the named Fano convention. The [structural comparison](/docs/applied/research/structural-correspondence#зодиак) gives an exact cyclic/product model and states precisely when an additional Fano requirement is compatible.

### 2.2 Elements

| Element | Triplet dimension | Characteristic |
|---------|------------------|----------------|
| Fire | $D$ (Dynamics) | Activity, transformation |
| Earth | $S$ (Structure) | Stability, form |
| Air | $A$ (Articulation) | Discernment, communication |
| Water | — (alternating) | Connection via $E$ (Interiority) |

---

## 3. I Ching Hexagrams [I] {#гексаграммы}

### 3.1 Explicit candidate map

Six ordered binary line positions give 64 patterns. To map them to Gamma, six observations must actually be chosen. One possible UHM-side convention is

$$
M_6=((O,U),(E,U),(L,U),(D,U),(S,U),(A,U)),\qquad
b_k(\Gamma)=\begin{cases}1,&\operatorname{Re}\gamma_{M_6(k)}>0,\\0,&\operatorname{Re}\gamma_{M_6(k)}<0.\end{cases}
$$

This is a partial map: zero real parts are unresolved unless an explicit boundary convention or measurement interval is supplied. It reads six pair-to-unity relations; it does not discard U or equate six coherences to six dimensions. The assignment of line positions to these pairs is an interpretation [I], not derived from the count 64. Its compatibility with line changes, reversal and the two-trigram decomposition is a separate structural check.

All 64 sign patterns are realizable in a fixed complex frame. For $s_j\in\{-1,1\}$ and $0<\epsilon<1/(7\sqrt6)$, let

$$
\Gamma_s=I/7+\epsilon\sum_{j\ne U}s_j(E_{jU}+E_{Uj}).
$$

Its eigenvalues are $1/7+\sqrt6\epsilon$, $1/7-\sqrt6\epsilon$ and $1/7$ with multiplicity five; it is positive definite and its six signs are the chosen pattern. This proves representability of the bit patterns by the selected readout. Every nonzero coherence here is real and has zero Gap, despite the different signs. Moreover diagonal sign changes relate all these matrices, so the distinction requires the retained frame; it disappears if those rephasings are quotiented out.

### 3.2 Interpretation and transitions

The component of a line is the named role of its pair in the [coherence vocabulary](/docs/core/dynamics/coherence-matrix). “Positive” and “negative” here are signs of a real component, not automatic judgments of healthy/unhealthy or clear/confused. Neither sign determines $|\sin\theta|$: phases $0$ and $\pi$ have opposite real signs and the same zero Gap.

The stronger exact bridge uses the bit-pattern structure $\mathbb F_2^3\times\mathbb F_2^3$, and then checks which operations survive its alignment with Fano incidence. See [trigrams and structural roles](/docs/applied/research/structural-correspondence#триграммы).

### 3.3 Information retained

One completed six-bit output has at most 6 bits of Shannon entropy. It does not encode the populations, coherence magnitudes or full phases. A percentage of information loss needs a distribution, quantization and observation protocol; counting cards, lines or matrix entries does not provide it.

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

The chakra system loses: all 42 real off-diagonal coordinates (21 complex coherences), the Gap structure, and dynamics.

---

## 6. Research Program [P] {#программа}

:::warning Status [P]
This entire section is a **research program**. None of the hypotheses has yet been empirically verified. The proposed design is the minimum required for rigorous testing.
:::

:::info Historical protocol correction (2026-10-13)
Sections 6.1–6.4 preserve the original proposed protocol, including its unvalidated cutoffs. Their interpretation is superseded by §7: zero correlation alone does not refute a shared latent state; nonsignificance is not proof of equivalence; a symbol name is not a numerical reading; Fano incidence alone supplies no closure equation. Use a specified joint model, calibrated error bounds and prospective scoring. The execution ledger in §0 is not changed by this correction.
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

## 7. Joint consistency of observations {#межсистемная-когерентность}

### 7.1 Problem statement

For each system retain an actual observation $y_k$, its protocol, time and a declared readout $f_k:\mathcal D(\mathbb C^7)\to Y_k$. Each target $Y_k$ has its own distance $d_k$ and calibrated tolerance $\varepsilon_k>0$. A completed matrix is a model-selected representative, not additional observed data.

### 7.2 Formal consistency condition {#условие-согласованности}

$$
\mathcal B_k=\{\Gamma\succeq0:\operatorname{Tr}\Gamma=1,
\ d_k(f_k(\Gamma),y_k)\le\varepsilon_k\},\qquad
\bigcap_k\mathcal B_k\ne\varnothing.
$$

This is compatibility with the specified readouts and data. It neither identifies a unique Gamma nor establishes that the readouts empirically measure the intended human phenomenon. Pairwise intersections do not in general imply a joint intersection; retain a common witness or a verified obstruction.

### 7.3 Example: populations and coherence readouts {#пример-три-системы}

Examples of mathematically defined readouts are

$$
f_{\rm diag}(\Gamma)=(\gamma_{ii})_i,\qquad
f_M(\Gamma)=(|\gamma_{ij}|)_{(i,j)\in M}.
$$

These require actual readings in their respective output spaces. Calling one observation a zodiac sign or one Tarot card does not provide the complete vector $f_M(\Gamma)$. Nor does completion of a modulus-only reading supply measured populations. The map $P\Gamma P$ with $P=I$ returns the entire matrix, not its diagonal; selecting matrix coordinates and taking moduli are different operations.

For overlapping measured pairs, agreement is checked in the shared output type. For nonoverlapping observations, the common PSD constraint supplies joint restrictions. All data must refer to a common time, or be related by an explicitly fitted evolution model.

### 7.4 Diagnosing incompatibility {#диагностика-несогласованности}

An empty intersection rejects the joint package of data, error tolerances, correspondences and time model. To locate a cause, retain a smallest known incompatible subset, source records and failed constraints. It does not by itself identify which assumption failed. Repeatedly changing the correspondence on the test set forfeits that set's independent validation role.

Absence of correlation is not an obstruction to a common latent state: independent coordinates of the same state can be uncorrelated. Conversely, correlation can arise from shared calendar inputs or a common scoring procedure. A forecast needs the explicit target and distribution described in the [predictive-sufficiency contract](/docs/applied/research/structural-correspondence#предсказание).

### 7.5 A calibrated feasibility residual {#мера-когерентности}

For continuous readouts and distances define

$$
R^*=\min_{\Gamma\in\mathcal D(\mathbb C^7)}
\max_k\frac{d_k(f_k(\Gamma),y_k)}{\varepsilon_k}.
$$

Compactness gives a minimizer. The stated tolerance constraints are compatible exactly when $R^*\le1$. This threshold follows from their definition; it is not a probability of correctness or a universal psychological score. The tolerances must be independently justified. With affine readouts and convex residuals the problem is convex; modulus or other nonlinear readouts may require global methods. A local optimizer's failure to find a feasible matrix is not a proof of incompatibility. Report certified bounds or an unresolved search explicitly.

---

## Related Documents

- [Symbolic systems](/docs/core/structure/symbolic-systems) — formal reduction
- [Gap diagnostics](/docs/applied/research/gap-diagnostics) — applied methodology
- [Gap semantics](/docs/physics/dual-aspect/gap-semantics) — 49-element map
- [Measurement protocol](/docs/applied/research/measurement-protocol) — experimental verification
