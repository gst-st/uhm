---
sidebar_position: 4
title: "Gap Diagnostics"
slug: /applied/research/gap-diagnostics
description: "Transparency map, diagnostic patterns, dual interview protocol, phase forecasting, correction protocols, transparency windows"
---

# Gap Diagnostics

:::info Who This Chapter Is For
Applied methodology of Gap diagnostics: transparency map, diagnostic patterns, and correction protocols for misalignments between the exterior and interior projections.
:::


Gap diagnostics is an applied methodology based on the [gap measure](/docs/physics/dual-aspect/gap-semantics) $\mathrm{Gap}(i,j) = |\sin(\arg(\gamma_{ij}))|$, which allows one to assess the misalignment between the exterior and interior projections for each of the 21 pairs of [seven dimensions](/docs/core/structure/dimensions). This document describes the transparency map, diagnostic patterns, and correction protocols.

:::warning Status [I]
All material in this section has the status of **interpretation/application**. Gap diagnostics is an operationalization of the mathematical formalism of the [coherence matrix](/docs/core/dynamics/coherence-matrix); empirical validation requires a separate [research program](/docs/applied/research/measurement-protocol).
:::

:::note Scope of Applicability
Gap as a mathematical measure ($|\sin\theta|$) is defined for **any holon**. However, the diagnostic and correction protocols of this document assume a system of [level L2+](/docs/consciousness/hierarchy/interiority-hierarchy) (organisms with a CNS), for which the interior projection ($\mathrm{Map}_{\mathrm{int}}$) is accessible through introspective reports.
:::

---

## 1. Transparency Map {#карта-прозрачности}

### 1.1 Definition

For a specific holon with coherence matrix $\Gamma$, $\mathrm{Gap}(i,j) = |\sin(\arg(\gamma_{ij}))|$ is computed for all 21 pairs. The result is visualized as a **heatmap** $7 \times 7$:

| Zone | Gap | Color | Interpretation |
|------|-----|-------|----------------|
| Transparent | $\approx 0$ | Green | Exterior and interior aspects are aligned |
| Transitional | $0.3$–$0.7$ | Yellow | Partial misalignment — zone of growth |
| Opaque | $\approx 1$ | Red | Complete dissociation |

### 1.2 Diagonal: 7 Populations

The diagonal elements $\gamma_{ii} \in \mathbb{R}$ have $\mathrm{Gap} = 0$ identically — population is the **only quantity** that is completely coincident between the exterior and interior projections.

| Element | [Dimension](/docs/core/structure/dimensions) | Exterior manifestation | Interior aspect (L2+) |
|---------|-----------|----------------------|-----------------------|
| $\gamma_{AA}$ | [Articulation](/docs/core/structure/dimension-a) | Communicative activity | Clarity of discrimination |
| $\gamma_{SS}$ | [Structure](/docs/core/structure/dimension-s) | Physical stability | Sense of stability |
| $\gamma_{DD}$ | [Dynamics](/docs/core/structure/dimension-d) | Observable activity | Sense of energy |
| $\gamma_{LL}$ | [Logic](/docs/core/structure/dimension-l) | Cognitive performance | Sense of mental clarity |
| $\gamma_{EE}$ | [Interiority](/docs/core/structure/dimension-e) | Emotional reactivity | Depth of experience |
| $\gamma_{OO}$ | [Ground](/docs/core/structure/dimension-o) | Vitality | Sense of groundedness |
| $\gamma_{UU}$ | [Unity](/docs/core/structure/dimension-u) | Behavioral integration | Sense of wholeness |

---

## 2. Diagnostic Patterns {#паттерны}

### 2.1 Main Patterns

| Pattern | Gap profile | Clinical description |
|---------|-------------|---------------------|
| **Alexithymia** | $\mathrm{Gap}(S,E) \approx 1$ | Body and experience are severed: the patient does not feel their body |
| **Splitting neurosis** | $\mathrm{Gap}(L,E) \approx 1$ | Logic and experience are severed: "understands everything, but does not feel" |
| **Impulsivity** | $\mathrm{Gap}(D,L) \approx 1$ | Action and logic are severed: acts without thinking |
| **Existential crisis** | $\mathrm{Gap}(O,U) \approx 1$ | Source and whole are severed: loss of meaning |
| **Authenticity** | $\mathrm{Gap}(A,O) \approx 0$ | Discrimination and ground are aligned: "words = essence" |
| **Wisdom** | $\mathrm{Gap}(L,O) \approx 0$ | Logic and ground are aligned: grounded understanding |

### 2.2 Systematics by Fano Lines {#фано-паттерны}

Each pair $(i,j)$ uniquely determines a Fano line $(i,j,k)$ in $\mathrm{PG}(2,2)$. Therefore diagnostic patterns naturally group by **7 Fano lines** (mapping $\phi_0$: A=1, S=2, D=3, L=4, E=5, U=6, O=7):

#### Line 1: {A, S, L} — cognitive-communicative {#линия-asl}

| Pair | High Gap ($\approx 1$) | Low Gap ($\approx 0$) |
|------|------------------------|----------------------|
| $A \leftrightarrow S$ | **Somatic muteness**: the body does not support speech; rupture of expression and sensation | Bodily expressiveness: the body "speaks" |
| $A \leftrightarrow L$ | **Demagoguery**: speaks without thinking; or thinks without formulating | Clear argumentation: word = thought |
| $S \leftrightarrow L$ | **Cognitive splitting**: bodily sensations and logic are misaligned | Embodied logic: thought is rooted in the body |

:::tip Triplet Pattern {A,S,L}
If all three Gaps on line $\{A,S,L\}$ are high — **cognitive fragmentation** [I]: the system articulates, structures, and analyzes, but the three processes are not connected. Characteristic of hyperintellectualization in somatic disorders.
:::

#### Line 2: {S, D, E} — psychosomatic {#линия-sde}

| Pair | High Gap ($\approx 1$) | Low Gap ($\approx 0$) |
|------|------------------------|----------------------|
| $S \leftrightarrow D$ | **Dyskinesia**: body and movement are misaligned, structure does not support dynamics | Plasticity: form follows movement |
| $S \leftrightarrow E$ | **Alexithymia**: body and experience are severed (main pattern, see §2.1) | Bodily sensitivity |
| $D \leftrightarrow E$ | **Blind activity**: action without experience, "robot" | Meaningful activity |

:::tip Triplet Pattern {S,D,E}
All three Gaps high — **psychosomatic dissociation** [I]: body, movement, and feeling are disconnected. Occurs in severe traumatic states (freezing).
:::

#### Line 3: {D, L, U} — volitional synthesis {#линия-dlu}

| Pair | High Gap ($\approx 1$) | Low Gap ($\approx 0$) |
|------|------------------------|----------------------|
| $D \leftrightarrow L$ | **Impulsivity**: action without reflection (main pattern, see §2.1) | Deliberate action |
| $D \leftrightarrow U$ | **Chaotic activity**: movement is not integrated into the whole | Goal-directed activity |
| $L \leftrightarrow U$ | **Fragmentary thinking**: logic does not see the whole, "trees without forest" | Holistic understanding |

:::tip Triplet Pattern {D,L,U}
All three Gaps high — **volitional paralysis** [I]: neither action, nor thought, nor wholeness are aligned. Characteristic of existential-type procrastination.
:::

#### Line 4: {L, E, O} — semantic axis {#линия-leo}

| Pair | High Gap ($\approx 1$) | Low Gap ($\approx 0$) |
|------|------------------------|----------------------|
| $L \leftrightarrow E$ | **Splitting neurosis**: logic and experience are severed (main pattern, see §2.1) | Emotional intelligence |
| $L \leftrightarrow O$ | **Alienated knowledge**: understands, but is not grounded; "knowledge without wisdom" | **Wisdom**: grounded understanding |
| $E \leftrightarrow O$ | **Groundless experience**: feels, but does not know where from or why | Grounded feeling: experience with a "foundation" |

:::tip Triplet Pattern {L,E,O}
All three Gaps high — **meaning vacuum** [I]: thought, feeling, and ground are not connected. Characteristic of existential depression.
:::

#### Line 5: {E, U, A} — integrative-expressive {#линия-eua}

| Pair | High Gap ($\approx 1$) | Low Gap ($\approx 0$) |
|------|------------------------|----------------------|
| $E \leftrightarrow U$ | **Emotional fragmentation**: experience is not embedded in the whole | Emotional maturity |
| $E \leftrightarrow A$ | **Mask**: expresses other than what is felt | Expressive authenticity |
| $U \leftrightarrow A$ | **Diffuse identity**: wholeness is not expressed in discrimination | Integral self-expression |

:::tip Triplet Pattern {E,U,A}
All three Gaps high — **authenticity crisis** [I]: feelings, wholeness, and expression are disconnected. Characteristic of the "false self" (Winnicott).
:::

#### Line 6: {U, O, S} — ontological stability {#линия-uos}

| Pair | High Gap ($\approx 1$) | Low Gap ($\approx 0$) |
|------|------------------------|----------------------|
| $U \leftrightarrow O$ | **Existential crisis**: whole and source are severed (main pattern, see §2.1) | Grounded wholeness |
| $U \leftrightarrow S$ | **Disintegration**: wholeness is not supported by bodily structure | Embodied wholeness |
| $O \leftrightarrow S$ | **Groundlessness**: body is separated from the source, "I don't feel the ground" | Groundedness: body = support |

:::tip Triplet Pattern {U,O,S}
All three Gaps high — **ontological instability** [I]: neither whole, nor source, nor body are aligned. Characteristic of schizoid states (Laing).
:::

#### Line 7: {O, A, D} — activity-based groundedness {#линия-oad}

| Pair | High Gap ($\approx 1$) | Low Gap ($\approx 0$) |
|------|------------------------|----------------------|
| $O \leftrightarrow A$ | **Inauthenticity**: discrimination and ground are misaligned | **Authenticity**: "words = essence" (main pattern, see §2.1) |
| $O \leftrightarrow D$ | **Fussiness**: activity without ground, actions "in vain" | Meaningful activity |
| $A \leftrightarrow D$ | **Activity dysphasia**: says one thing — does another | Active speech: word = deed |

:::tip Triplet Pattern {O,A,D}
All three Gaps high — **activity disorientation** [I]: no connection between what is said, done, and what is grounded in. Characteristic of burnout syndrome.
:::

#### Summary Table of Triplet Patterns

| Fano line | Triplet | Pattern | Clinical analogue |
|------------|---------|---------|-------------------|
| $\ell_1$ | $\{A,S,L\}$ | Cognitive fragmentation | Hyperintellectualization |
| $\ell_2$ | $\{S,D,E\}$ | Psychosomatic dissociation | Traumatic freezing |
| $\ell_3$ | $\{D,L,U\}$ | Volitional paralysis | Existential procrastination |
| $\ell_4$ | $\{L,E,O\}$ | Meaning vacuum | Existential depression |
| $\ell_5$ | $\{E,U,A\}$ | Authenticity crisis | "False self" |
| $\ell_6$ | $\{U,O,S\}$ | Ontological instability | Schizoid position |
| $\ell_7$ | $\{O,A,D\}$ | Activity disorientation | Burnout syndrome |

### 2.3 Extended Diagnostics (Example)

> **Subject:** high $|\gamma_{LE}|$ (strong logic–experience connection), but $\arg(\gamma_{LE}) \approx \pi/2$ ($\mathrm{Gap} \approx 1$).
>
> **External** ($\gamma_{LE}$): the observer sees moments of insight — the person "understands."
>
> **Internal** ($\gamma_{EL}$): the subject senses that experiences do not become understanding.
>
> **Diagnosis:** Intellectualization of affect. Maximum gap at maximum connection strength.
>
> **Correction:** Practices uniting logic and experience (body-oriented therapy, koan practice in Zen). Goal: $\arg(\gamma_{LE}) \to 0$, keeping $|\gamma_{LE}|$ high.

---

## 3. The "Dual Interview" Protocol {#протокол}

:::info Full Protocol Version
The full description of the dual interview protocol — including 4 stages with biometrics (EEG, fMRI, HRV), spectral reconstruction of $H_{\text{eff}}$, physiological frequencies, and Gap-profile reconstruction code — see [Γ Measurement Protocol: Dual Interview](/docs/applied/research/measurement-protocol#протокол-двойного-интервью-для-биологических-систем). Below is the concise diagnostic version.
:::

### 3.1 Data Input

**Step 1. External measurements** (observer):
- Questionnaires, biometrics, behavioral markers
- Estimation of $\gamma_{ij}$ (upper triangle — Map_ext)

**Step 2. Internal reports** (subject):
- Introspective reports, experience scales
- Estimation of $\gamma_{ji}$ (lower triangle — Map_int)

**Step 3. Computation:**
- $\mathrm{Gap}(i,j)$ for all 21 pairs
- Population vector $\{\gamma_{ii}\}$
- Profile of [quantum currents](/docs/core/dynamics/coherence-matrix) $J_{\text{net}}(i,j)$

### 3.2 Output

- **Transparency map** (heatmap $7 \times 7$)
- **Population vector** (histogram of 7 values)
- **Current profile** (flow directions between dimensions)
- **Opacity rank** (0–3, from the [Gap operator spectrum](/docs/core/dynamics/gap-operator#спектр))

---

## 4. Phase Forecasting {#прогностика}

### 4.1 Phase Evolution

Under unitary evolution, the phase rotates:

$$
\theta_{ij}(\tau) = \theta_{ij}(0) + (\omega_i - \omega_j) \cdot \tau
$$

Gap oscillates with frequency $|\omega_i - \omega_j|$:

$$
\mathrm{Gap}(i,j;\tau) = |\sin(\theta_{ij}(0) + \Delta\omega_{ij} \cdot \tau)|
$$

### 4.2 Transparency Windows

**Definition.** A period when $\mathrm{Gap}(i,j) \approx 0$ — exterior and interior aspects are aligned. Optimal time for:
- Awareness
- Therapeutic intervention
- Decision-making

### 4.3 Turbulence Zones

Periods $\mathrm{Gap}(i,j) \approx 1$: maximum misalignment. Risk of disorientation, but potential for deep transformation (crisis = opportunity).

### 4.4 Phase Resonances

When several pairs simultaneously pass through $\mathrm{Gap} \approx 0$ — a moment of "total transparency" (all channels are transparent). The probability of resonance is determined by the rationality of the ratios of differential frequencies $\Delta\omega_{ij}/\Delta\omega_{kl}$.

#### Numerical Example: Resonance Window Calculation {#численный-резонанс}

Consider a system with eigenfrequencies (in dimensionless units $\tau^{-1}$):

$$
\omega = (\omega_A, \omega_S, \omega_D, \omega_L, \omega_E, \omega_O, \omega_U) = (1.0,\; 3.0,\; 4.0,\; 6.0,\; 7.0,\; 9.0,\; 12.0)
$$

and initial phases $\theta_{ij}(0) = 0$ for all pairs.

**Step 1.** Compute the differential frequencies for the pairs of Fano line $\{A,S,L\} = \{1,2,4\}$:

$$
\Delta\omega_{AS} = |1-3| = 2, \quad \Delta\omega_{AL} = |1-6| = 5, \quad \Delta\omega_{SL} = |3-6| = 3
$$

**Step 2.** Transparency condition: $\mathrm{Gap}(i,j;\tau) = |\sin(\Delta\omega_{ij} \cdot \tau)| < \varepsilon$ is satisfied near $\tau = n\pi/\Delta\omega_{ij}$, $n \in \mathbb{Z}$.

Transparency windows for each pair ($\varepsilon = 0.1$, window $\delta\tau \approx \varepsilon / \Delta\omega_{ij}$):

| Pair | $\Delta\omega$ | Period | Windows (first) | Window width |
|------|----------------|--------|-----------------|-------------|
| $A \leftrightarrow S$ | 2 | $\pi/2 \approx 1.57$ | $\tau = 0, 1.57, 3.14, \ldots$ | $\delta\tau \approx 0.05$ |
| $A \leftrightarrow L$ | 5 | $\pi/5 \approx 0.63$ | $\tau = 0, 0.63, 1.26, \ldots$ | $\delta\tau \approx 0.02$ |
| $S \leftrightarrow L$ | 3 | $\pi/3 \approx 1.05$ | $\tau = 0, 1.05, 2.09, \ldots$ | $\delta\tau \approx 0.03$ |

**Step 3.** Triple resonance condition on line $\{A,S,L\}$: all three Gaps simultaneously $< \varepsilon$. This requires:

$$
2\tau \approx n_1 \pi, \quad 5\tau \approx n_2 \pi, \quad 3\tau \approx n_3 \pi
$$

Frequency ratios: $\Delta\omega_{AS} / \Delta\omega_{SL} = 2/3$ (rational!), $\Delta\omega_{AL} / \Delta\omega_{SL} = 5/3$ (rational!). Therefore, the triple resonance is **periodic** with period:

$$
T_{\text{res}} = \frac{\pi}{\gcd(2, 3, 5)} = \pi
$$

First non-trivial triple resonance: $\tau^* = \pi \approx 3.14$.

**Step 4.** Verification: at $\tau = \pi$:
- $\mathrm{Gap}(A,S) = |\sin(2\pi)| = 0$
- $\mathrm{Gap}(A,L) = |\sin(5\pi)| = 0$
- $\mathrm{Gap}(S,L) = |\sin(3\pi)| = 0$

All three channels are transparent simultaneously.

:::warning Counterexample: Irrational Frequencies
If $\omega_L = 1 + \sqrt{5} \approx 3.236$, then $\Delta\omega_{AL}/\Delta\omega_{AS}$ would become irrational, and the triple resonance would **never** occur exactly — only approximate windows by Weyl's equidistribution theorem. This is the "Fibonacci system" case from §6.5.
:::

### 4.5 Predicting Phase Transitions

[Bifurcation](/docs/core/dynamics/gap-phase-diagram#бифуркации) occurs when:

$$
\lambda_{\max}\left(\frac{\partial^2 P}{\partial \Gamma^2}\right) = 0
$$

A small perturbation of one coherence can change the entire phase map.

---

## 5. Correction Protocols {#коррекция}

### 5.1 Principle of Minimal Intervention

From the [Hamming code H(7,4) analogy](/docs/core/dynamics/gap-dynamics#код-хэмминга): when **one** coherence is disrupted, it is sufficient to restore **one** connection — the system will automatically correct the rest through the [φ-operator](/docs/core/operators/phi-operator).

:::warning Warning
When $\geq 2$ coherences are disrupted, automatic correction is **not guaranteed** — intervention across multiple channels is required.
:::

### 5.2 Correction Table

| Problem channel | Gap | Correction practice | Goal |
|-----------------|-----|---------------------|------|
| $S \leftrightarrow E$ | $\approx 1$ | Bodily practices (yoga, dance) | $\arg(\gamma_{SE}) \to 0$ |
| $L \leftrightarrow E$ | $\approx 1$ | Koan meditation, logotherapy | $\arg(\gamma_{LE}) \to 0$ |
| $D \leftrightarrow L$ | $\approx 1$ | GTD, step-by-step planning | $\arg(\gamma_{DL}) \to 0$ |
| $A \leftrightarrow O$ | $\approx 1$ | Sincerity practice, silence | $\arg(\gamma_{AO}) \to 0$ |
| $O \leftrightarrow U$ | $\approx 1$ | Contemplation, via negativa | $\arg(\gamma_{OU}) \to 0$ |
| $D \leftrightarrow E$ | $\approx 1$ | Sport + mindfulness | $\arg(\gamma_{DE}) \to 0$ |
| $A \leftrightarrow U$ | $\approx 1$ | Holistic practices | $\arg(\gamma_{AU}) \to 0$ |

### 5.3 Optimal Intervention Frequency

From [FDT for Gap](/docs/core/dynamics/gap-thermodynamics): for each channel $(i,j)$ there is a resonant frequency:

$$
\omega_r^{(ij)} = \sqrt{|\omega_i - \omega_j|^2 - 2\Gamma_2^2}
$$

Therapeutic intervention is most effective when its time scale coincides with $\omega_r$.

### 5.4 Correction Algorithm {#коррекционный-алгоритм}

A step-by-step correction protocol based on [Hamming code H(7,4)](/docs/core/dynamics/gap-dynamics#код-хэмминга) and the [stress measure](/docs/consciousness/foundations/self-observation) $\sigma_k = \mathrm{clamp}(1 - 7\gamma_{kk}, 0, 1)$ [T-92].

#### Step 1. Identification of Critical Channels {#шаг-1}

Compute $\mathrm{Gap}(i,j)$ for all 21 pairs. Identify the set of **critical channels**:

$$
\mathcal{C} = \{(i,j) : \mathrm{Gap}(i,j) > 0.7\}
$$

If $|\mathcal{C}| = 0$ — the system is in the green zone, no correction needed.

#### Step 2. Verification of Fano Linearity {#шаг-2}

For each critical channel $(i,j) \in \mathcal{C}$, identify the Fano line $\ell(i,j) = \{i, j, k\}$. Check:

- **Isolated error**: only one channel $(i,j)$ on line $\ell$ has $\mathrm{Gap} > 0.7$, the other two channels on the same line have $\mathrm{Gap} < 0.3$.
- **Line error**: two or three channels of one Fano line have $\mathrm{Gap} > 0.7$ (triplet pattern from §2.2).
- **Distributed error**: critical channels lie on different Fano lines.

#### Step 3. Single Correction (H(7,4)) {#шаг-3}

If the error is **isolated** (one channel):

1. Apply the correction practice from table §5.2 for the specific channel $(i,j)$.
2. By [analogy with H(7,4)](/docs/core/dynamics/gap-dynamics#код-хэмминга): the code corrects **one** error. The [φ-operator](/docs/core/operators/phi-operator) will automatically restore coherences on adjacent channels.
3. **Expected dynamics**: $\mathrm{Gap}(i,j) \to 0$ over time $\sim 1/\omega_r^{(ij)}$ (resonant frequency from §5.3).

#### Step 4. Multiple Correction with Prioritization by $\sigma_k$ {#шаг-4}

If there are $\geq 2$ errors (line or distributed):

1. **Priority by stress.** For each dimension $k$ involved in critical channels, compute $\sigma_k = \mathrm{clamp}(1 - 7\gamma_{kk}, 0, 1)$. The dimension with maximum $\sigma_k$ is the most stressed — it receives priority.

2. **Intervention order.** Sort critical channels by descending $\max(\sigma_i, \sigma_j)$:

$$
(i_1, j_1), (i_2, j_2), \ldots \quad \text{where } \max(\sigma_{i_1}, \sigma_{j_1}) \geq \max(\sigma_{i_2}, \sigma_{j_2}) \geq \ldots
$$

3. **Sequential intervention.** For each channel in priority order:
   - Apply the correction practice from §5.2.
   - After each intervention, **wait** an interval $\Delta\tau \geq 2\pi/\omega_r^{(ij)}$ (one full cycle) and re-evaluate $\mathrm{Gap}$ for all 21 pairs.
   - If autocorrection via the φ-operator has already reduced the Gap of adjacent channels — skip them.

4. **Triplet correction.** If all three channels of one Fano line are critical (triplet pattern), intervene on **all three** simultaneously (the φ-operator cannot handle two errors on the same line).

:::warning H(7,4) Limitation
Hamming code H(7,4) guarantees correction of **exactly one** error. With $|\mathcal{C}| \geq 2$ channels on one Fano line, automatic φ-correction is **not guaranteed** — multiple intervention per step 4 is required.
:::

#### Step 5. Monitoring Gap Dynamics {#шаг-5}

After each intervention, track:

| Metric | Formula | Target value |
|--------|---------|-------------|
| Channel Gap | $\mathrm{Gap}(i,j;\tau)$ | $< 0.3$ (green zone) |
| Average Gap | $\bar{G} = \frac{1}{21}\sum_{i<j}\mathrm{Gap}(i,j)$ | $< 0.2$ |
| Maximum $\sigma$ | $\sigma_{\max} = \max_k \sigma_k$ | $< 0.5$ |
| Purity | $P = \mathrm{tr}(\Gamma^2)$ | $> 2/7$ (consciousness threshold) |

**Correction completion criterion:**

$$
\max_{(i,j)} \mathrm{Gap}(i,j) < 0.3 \;\;\wedge\;\; \sigma_{\max} < 0.5 \;\;\wedge\;\; P > P_{\text{crit}} = 2/7
$$

**Escalation criterion** (transition to intensive protocol):

$$
|\mathcal{C}| > 7 \;\;\vee\;\; \bar{G} > 0.7 \;\;\vee\;\; P < 1/7 + 0.02
$$

:::tip Algorithm Summary
1. $\mathcal{C} \leftarrow \{(i,j) : \mathrm{Gap}(i,j) > 0.7\}$
2. If $|\mathcal{C}| = 0$ → stop (system is healthy)
3. If $|\mathcal{C}| = 1$ and error is isolated → single H(7,4) correction (step 3)
4. Otherwise → prioritization by $\sigma_k$ (step 4): sorting, sequential intervention, re-evaluation
5. Monitor $\mathrm{Gap}$, $\sigma$, $P$ until the completion criterion is met (step 5)
:::

---

## 6. Model Systems {#модельные-системы}

### 6.1 Uniform System ($\Gamma = I/7$)

All coherences $= 0$. Gap is undefined. $P = 1/7$ — minimum purity. **Completely decoherent system.**

### 6.2 Pure State (Uniform Superposition)

$|\psi\rangle = (1/\sqrt{7})\sum_i |i\rangle$: all $\gamma_{ij} = 1/7 \in \mathbb{R}$, $\mathrm{Gap} = 0$ for all pairs. **Ideal transparency.**

### 6.3 State with Phases (Fano Structure)

$\phi_k = (k-1)\pi/7$: $\mathrm{Gap}(i,j) = |\sin((i-j)\pi/7)|$. Gap grows monotonically with the "distance" between dimensions. Nearest dimensions are more transparent, distant ones — more opaque.

### 6.4 Alexithymia Model

$\gamma_{SE} = |\gamma_{SE}| \cdot e^{i\pi/2}$, remaining coherences $\in \mathbb{R}$. $\mathrm{Gap}(S,E) = 1$ (maximum). One coherence is disrupted → correction via H(7,4).

### 6.5 Dynamic System (Fibonacci)

$\omega = (0, 1, 2, 3, 5, 8, 13)$. Irrational ratios $\Delta\omega$ → Gap takes all values ergodically → complete transparency is unachievable.

---

## Related Documents

- [Dual-aspect Gap semantics](/docs/physics/dual-aspect/gap-semantics) — 49-element map
- [Gap dynamics](/docs/core/dynamics/gap-dynamics) — bifurcations, Hamming
- [Gap phase diagram](/docs/core/dynamics/gap-phase-diagram) — three phases, critical phenomena
- [Measurement protocol](/docs/applied/research/measurement-protocol) — experimental verification
- [Interiority hierarchy](/docs/consciousness/hierarchy/interiority-hierarchy) — levels L0–L4
