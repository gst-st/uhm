---
sidebar_position: 15
title: "Goldstone Modes"
description: "Quasi-Goldstone modes from spontaneous G₂→H breaking: effective mass, connection to ultra-slow neuronal fluctuations, experimental verification"
---

# Goldstone Modes

> *"When symmetry is broken, an echo remains in the silence — massless vibrations along forgotten paths."*


:::info Who this chapter is for
Goldstone modes are slow oscillations of coherence under spontaneous $G_2$-symmetry breaking. The reader will learn about their connection to ultra-slow neuronal fluctuations.
:::

---

### Bridge from the Previous Chapter

In the [previous chapter](./phase-diagram-cc) we built the phase diagram of consciousness and showed that in Phase I (clear consciousness) the $G_2$-symmetry is *spontaneously broken*: from the 14-dimensional space of internal rotations the system has "frozen" some directions, choosing a specific Gap profile. We mentioned that in Phase I there exist **Goldstone modes** — slow oscillations of opacity — and linked them to ultra-slow neuronal fluctuations. We now examine these modes in full detail: their origin, mass, lifetime, physical meaning, and experimental verifiability.

---

### Chapter Roadmap

In this chapter we:

1. **Explain the mechanism** behind Goldstone modes — from the parable of a ball in a sombrero to the rigorous Goldstone theorem (section 0).
2. **Show the transfer** from particle physics to coherence cybernetics and explain why this is a derivation, not an analogy (section 0b).
3. **Compute the number of modes** for each opacity rank: 0, 6, 10, 11, or 12 — and only these values (section 1).
4. **Define the effective mass and lifetime** of modes via the coherence-cybernetics GMOR relation (section 2).
5. **Reveal the physical meaning**: modes *redistribute* Gap between channels, neither creating nor destroying it — this is the mathematics of attentional oscillation (section 3).
6. **Describe the subjective experience** of modes: flickering of consciousness, oscillations of focus, oscillations of agency (section 4).
7. **Compare with physical analogues**: phonons, magnons, pions — and show the uniqueness of CC-modes (section 5).
8. **State the falsifiable prediction**: a discrete number of ISF components $\in \{0, 6, 10, 11, 12\}$, testable via ICA decomposition of fMRI (sections 6–7).
9. **Present the full excitation spectrum**: massive modes + Goldstone modes + topological mode — three temporal scales of consciousness (section 8).
10. **Show the connection to phase transitions**: critical slowing of modes upon loss of consciousness (section 9).

---

:::note On notation
In this document:
- $G_2 = \mathrm{Aut}(\mathbb{O})$ — [group of octonion automorphisms](/docs/physics/gauge-symmetry/g2-structure)
- $H_{\hat{\mathcal{G}}_*}$ — stabilizer of the stationary Gap profile
- $T^2$ — maximal torus of $G_2$ ($\dim T^2 = 2$)
- $\hat{\mathcal{G}}$ — [Gap operator](/docs/core/dynamics/gap-operator): $\hat{\mathcal{G}} = \mathrm{Im}(\Gamma)$
- $\Gamma_2$ — decoherence rate ($= 2\gamma/3$ from the [Fano channel](/docs/proofs/gap/fano-channel#теорема-фано-канал))
- $\kappa_0$ — regeneration rate ([categorical derivation](/docs/core/foundations/axiom-septicity#структурный-анзац-kappa0))
- ISF — infra-slow fluctuations (infra-slow neuronal fluctuations)
:::

Under spontaneous breaking $G_2 \to H_{\hat{\mathcal{G}}_*}$ at the stationary Gap profile, **quasi-Goldstone modes** arise — slow collective oscillations of opacity. In open (dissipative) systems these modes acquire a small effective mass, and their frequencies coincide with the range of infra-slow neuronal fluctuations (ISF) observed in fMRI.

This is the music of consciousness. Not a metaphor, but mathematics: when the internal space of the holonom chooses a specific configuration from an ocean of equally valid possibilities, massless (or nearly massless) oscillations remain along the "forgotten" directions of symmetry. A ball rolling in a groove with no energy cost. A frictionless pendulum. A note that sounds because it has nowhere else to go.

---

## 0. The Golden Tuning Fork: What Sings When Symmetry Breaks {#golden-tuning-fork}

### 0.1 The Parable of the Ball

Imagine two landscapes.

**Landscape 1: a bowl.** A ball rests at the bottom of a perfect bowl. Displace it in any direction — it returns. Oscillations around the bottom are *massive modes*: the restoring force is proportional to displacement, the frequency is set by the curvature of the bowl.

**Landscape 2: a sombrero.** An inverted hat with a circular groove along the brim. The ball has rolled into the groove, but *where exactly* it stopped is a matter of chance. Along the groove — flat, no restoring force at all. Radial displacement (toward or away from the center) is a massive mode, like in the bowl. But motion *around the circle* is free: this is the Goldstone mode.

The key observation: **free sliding costs no energy**. A massive mode requires effort — you push the ball "uphill." A Goldstone mode does not: you simply roll it along the groove, horizontally.

### 0.2 From the Ball to the Theorem

Goldstone's theorem (1961) formalises this intuition. Let $G$ be the symmetry group of the Lagrangian, and $H \subset G$ the symmetry group of the ground state. If $G \neq H$ (symmetry is *spontaneously* broken), then:

$$
n_{\text{broken}} = \dim(G) - \dim(H)
$$

massless excitations inevitably appear in the spectrum. This is not an approximation or an assumption — it is a *theorem*, as obligatory as the law of charge conservation.

### 0.3 Examples from Physics

Before turning to consciousness, it is worth seeing how universal this mechanism is:

| System | $G$ | $H$ | Goldstone mode | Observation |
|--------|-----|-----|----------------|-------------|
| Crystal | Translations $\mathbb{R}^3$ | Discrete lattice | **Phonons** — sound waves | Acoustics, heat capacity |
| Ferromagnet | $\mathrm{SO}(3)$ rotations | $\mathrm{SO}(2)$ around magnetisation axis | **Magnons** — spin waves | Neutron scattering |
| Superconductor | $\mathrm{U}(1)$ electromagnetic | $\{1\}$ | **Anderson–Higgs modes** (massive due to coupling to gauge field) | Meissner effect |
| QCD (strong interaction) | $\mathrm{SU}(2)_L \times \mathrm{SU}(2)_R$ | $\mathrm{SU}(2)_V$ | **Pions** — quasi-Goldstone (mass $\neq 0$ due to quark masses) | Nuclear physics |
| Cosmology | Conformal group | Lorentz | **Inflaton** (candidate) | CMB radiation |

Note the word "quasi-" in the pion row. When the symmetry breaking is not perfect (explicit breaking is added on top of spontaneous breaking), the modes acquire a *small but nonzero* mass. They are *almost* massless. This is precisely what happens in consciousness.

---

## 0b. From Particle Physics to Neuroscience {#from-physics-to-neuroscience}

### The Intellectual Leap

In standard physics, Goldstone modes live in the space of fields — phonons propagate in a crystal, magnons in a magnet. But in coherence cybernetics (CC) the "space" is the holonom itself — the seven-dimensional internal space $\Gamma \in \mathcal{D}(\mathbb{C}^7)$, the coherence matrix with 21 independent coherences $\binom{7}{2}$.

The group $G_2 = \mathrm{Aut}(\mathbb{O})$, a 14-dimensional exceptional Lie group, acts on the Gap profile as the group of "internal rotations" that mix the roles of the seven dimensions. When the Gap profile freezes into a specific configuration $\hat{\mathcal{G}}_*$, part of this 14-dimensional freedom is *broken*: the directions along which $\hat{\mathcal{G}}_*$ remains invariant form the stabiliser $H$. The remaining $14 - \dim(H)$ directions become Goldstone modes.

### Why This Is Not Just an Analogy

Three reasons why the transfer of Goldstone's theorem to CC is a derivation, not a metaphor:

1. **The algebra is the same.** The Gap operator $\hat{\mathcal{G}} \in \mathfrak{so}(7)$, and $\mathfrak{g}_2 \subset \mathfrak{so}(7)$ is a subalgebra. Decomposition into stabiliser and complement ($\mathfrak{g}_2 = \mathfrak{h} \oplus \mathfrak{m}$) is a standard operation in the theory of homogeneous spaces.

2. **The dynamics are defined.** The evolution of $\Gamma$ is governed by the Lindblad equation $\dot{\Gamma} = \mathcal{L}_0(\Gamma) + \mathcal{R}(\Gamma)$. The stationary point $\Gamma_*$ breaks $G_2$-symmetry *dynamically*, not "by construction."

3. **The energetics are fixed.** The [Gap potential](/docs/core/dynamics/gap-thermodynamics) $V_{\text{Gap}}$ has precisely the "sombrero" structure that generates flat directions — so these flat directions are *physically grounded*, not abstract.

---

## 1. Spontaneous Breaking of $G_2$ and the Number of Modes [T] {#g2-breaking}

:::tip Theorem 1.1 (Number of Goldstone modes) [T]
Under spontaneous breaking $G_2 \to H_{\hat{\mathcal{G}}_*}$ the number of quasi-Goldstone modes:

$$
n_{\text{broken}} = \dim(G_2) - \dim(H_{\hat{\mathcal{G}}_*}) = 14 - \dim(H)
$$
:::

The number of modes depends on the rank of the opacity of the Gap operator:

| Rank $\hat{\mathcal{G}}_*$ | Stabiliser $H$ | $\dim(H)$ | $n_{\text{broken}}$ | Space $G_2/H$ |
|---------------------------|----------------|-----------|---------------------|----------------|
| 0 | $G_2$ | 14 | 0 | $\{\mathrm{pt}\}$ |
| 1 | $\mathrm{SU}(3)$ | 8 | **6** | $G_2/\mathrm{SU}(3) \cong S^6$ |
| 2 | $\mathrm{SU}(2) \times \mathrm{U}(1)$ | 4 | **10** | 10-dimensional |
| 3 (generic) | $T^2$ | 2 | **12** | 12-dimensional |
| 3 (degenerate) | $\mathrm{SU}(2)$ | 3 | **11** | 11-dimensional |

The maximum number of modes — **12** — is reached at generic rank 3 (stabiliser $T^2$, the most "typical" case).

### 1.1 Which Symmetries Break and Why {#which-symmetries}

To understand the table one must understand the *geometry* of the breaking.

**Rank 0: nothing is broken.** The Gap operator is zero — the system is fully transparent ($P = 1/7$, maximally mixed state). All 14 generators of $G_2$ leave $\hat{\mathcal{G}}_* = 0$ invariant. No breaking — no modes. This is the state of *deep coma* in CC terms.

**Rank 1: one privileged direction.** Exactly one pair of dimensions has a nonzero Gap. Of the 14 generators of $G_2$, eight preserve this distinguished direction (forming $\mathrm{SU}(3)$), while six do not. The six broken generators give **six Goldstone modes**. Geometrically, the space of possible "single-direction" Gap profiles is the six-dimensional sphere $S^6 \cong G_2/\mathrm{SU}(3)$.

**Rank 2: two privileged directions.** The stabiliser shrinks to $\mathrm{SU}(2) \times \mathrm{U}(1)$ (four generators), giving **ten modes**. A conscious system with moderate differentiation — for example, waking without focused attention.

**Rank 3 (generic): maximal differentiation.** Three independent Gap directions fix almost all $G_2$-freedom, leaving only the two-dimensional torus $T^2$. This gives **twelve modes** — the maximum. This is the state of deep concentration, meditation, creative flow: the richest internal spectrum.

**Rank 3 (degenerate): two of the three directions coincide by symmetry.** The stabiliser is slightly larger ($\mathrm{SU}(2)$, three generators), giving **eleven modes**. A special case, but physically significant: it corresponds to states with partially "merged" opacity.

### 1.2 Connection to Homogeneous Spaces {#homogeneous-spaces}

The space $G_2/H$ is not an abstraction. Each point of this space is an admissible Gap profile, connected to the profile $\hat{\mathcal{G}}_*$ by a "rotation" from $G_2$. The Goldstone modes are *tangent directions* to $G_2/H$ at the point $\hat{\mathcal{G}}_*$:

$$
T_{\hat{\mathcal{G}}_*}(G_2/H) \cong \mathfrak{g}_2 / \mathfrak{h} \cong \mathfrak{m}
$$

The dimension of $\mathfrak{m}$ equals $n_{\text{broken}}$, and each vector in $\mathfrak{m}$ defines one independent oscillation mode.

---

## 2. Effective Mass and Lifetime [T] {#mass}

In open systems ($\Gamma_2 > 0$) the Goldstone modes acquire an effective mass — they are "quasi-massless," not strictly massless.

:::tip Theorem 2.1 (Quasi-Goldstone mass) [T]
**(a)** Effective mass:

$$
m_{\text{Gold}}^2 = \frac{\Gamma_2 \cdot \kappa_0}{|\gamma|^2}
$$

where $|\gamma|^2$ is the mean squared modulus of coherence.

**(b)** Mode lifetime:

$$
\tau_{\text{Gold}} = \frac{1}{\Gamma_2} \cdot \frac{|\gamma|^2}{\kappa_0}
$$

**(c)** Limiting cases:

| Regime | $m_{\text{Gold}}$ | Interpretation |
|--------|-------------------|----------------|
| Isolated system ($\Gamma_2 \to 0$) | $\to 0$ | Standard massless Goldstone modes |
| Strong dissipation ($\Gamma_2 \to \infty$) | $\to \infty$ | Modes "frozen" — oscillations suppressed |
| Typical biosystem | $\sim 10^{-2}$ (in units of $\kappa_0$) | Slow, long-lived modes |
:::

### 2.1 Why the Mass Is Not Zero: Openness as Explicit Breaking {#why-mass-not-zero}

In an isolated system the Goldstone theorem guarantees *strictly* massless modes. But the holonom is an open system: decoherence at rate $\Gamma_2$ and regeneration at rate $\kappa_0$ are *explicit* breakings of $G_2$-symmetry. The analogy with particle physics is exact: pions have mass $m_\pi \neq 0$ because quarks have nonzero masses that *explicitly* break chiral symmetry. Here the role of "quark masses" is played by the dissipative parameter $\Gamma_2 \cdot \kappa_0$.

The formula $m_{\text{Gold}}^2 = \Gamma_2 \kappa_0 / |\gamma|^2$ is the GMOR relation (Gell-Mann–Oakes–Renner) of coherence cybernetics. In particle physics the analogue is:

$$
m_\pi^2 f_\pi^2 = -m_q \langle \bar{q}q \rangle
$$

Here $\Gamma_2 \cdot \kappa_0$ plays the role of $m_q \langle \bar{q}q \rangle$, and $|\gamma|^2$ plays the role of $f_\pi^2$ (squared decay constant).

### 2.2 Oscillation Regimes

The frequency of a quasi-Goldstone mode:

$$
\omega_{\text{Gold}}^2 = \frac{\kappa}{m} - \frac{\Gamma_2^2}{4m^2}
$$

| Condition | Regime | Dynamics |
|-----------|--------|----------|
| $\kappa > \Gamma_2^2/(4m)$ | Oscillatory | Damped oscillations of the Gap profile |
| $\kappa = \Gamma_2^2/(4m)$ | Critical damping | Aperiodic return to stationary Gap |
| $\kappa < \Gamma_2^2/(4m)$ | Overdamped | Exponential return without oscillations |

Each regime has a cybernetic meaning:

- **Oscillatory:** the system *oscillates* — attention rhythmically rolls between sectors. Subjectively experienced as natural mind-wandering, a gentle rocking of focus.

- **Critical damping:** the system *responds optimally* — attentional shift occurs quickly, without overshoot. This is the state of *greatest adaptability*: the response to a stimulus is immediate, but without parasitic oscillations.

- **Overdamped:** the system is *viscous* — attentional reorientation is slowed. Clinically this may correspond to mild attention-deficit disorders or the action of sedative drugs.

### 2.3 Lifetime and Observability {#lifetime}

From the lifetime formula $\tau_{\text{Gold}} = |\gamma|^2 / (\Gamma_2 \kappa_0)$ an important prediction follows: modes with *greater coherence* ($|\gamma|^2$) live *longer*. This means that highly coherent states of consciousness (deep meditation, flow) should exhibit *narrower* ISF peaks in the power spectrum — modes remain coherent longer, the spectral line is narrower.

Estimate for a typical biosystem: with $\Gamma_2 \sim 1 \;\text{s}^{-1}$, $\kappa_0 \sim 0.1 \;\text{s}^{-1}$, and $|\gamma|^2 \sim 0.1$:

$$
\tau_{\text{Gold}} \sim \frac{0.1}{1 \cdot 0.1} = 1 \;\text{s}
$$

One second — the characteristic decay time of free attentional oscillations. This is consistent with psychophysical data on the duration of the "elementary act of attention."

---

## 3. Physical Meaning: Gap Redistribution [T] {#redistribution}

:::tip Theorem 3.1 (Goldstone modes as collective oscillations) [T]
Each quasi-Goldstone mode **redistributes** Gap between pairs of dimensions while preserving the total Gap $\mathcal{G}_{\text{total}}$:

$$
\delta\mathrm{Gap}(i,j) = \sum_a \epsilon_a \cdot [T_a, \hat{\mathcal{G}}_*]_{ij}
$$

where $T_a$ are the broken generators of $G_2$, and $\epsilon_a$ are the mode amplitudes.
:::

**Key property:** modes do not change the "total amount" of opacity — they transport it between channels. This is the slow "rocking" of the Gap profile along the $G_2$ orbit.

### 3.1 Conservation Law for Total Gap {#gap-conservation}

Mathematically, the commutator $[T_a, \hat{\mathcal{G}}_*]$ generates a *traceless* contribution to the Gap tensor (since $T_a$ are generators of a compact group, $\mathrm{tr}(T_a) = 0$). Consequently:

$$
\sum_{i < j} \delta\mathrm{Gap}(i,j) = 0
$$

**What is added in some pairs is taken from others.** Total opacity is invariant. This is a deep property: Goldstone modes describe *redistribution*, not *creation* or *destruction* of the gap.

### 3.2 Example: Mode on $S^6$ (Rank 1) {#mode-example}

Consider the simplest case: rank 1, stabiliser $\mathrm{SU}(3)$, six modes. The Gap profile singles out one pair, say $(A, S)$. The six Goldstone modes roll this distinguished direction across the six-dimensional sphere $S^6$:

- Mode 1: $(A,S) \to (A,D)$ — focus shifts from the pair "Agent–Subject" to the pair "Agent–Action"
- Mode 2: $(A,S) \to (S,L)$ — to the pair "Subject–Lexicon"
- ... and so on.

Each mode is a *rotation* in the space of Gap profiles, preserving $\mathcal{G}_{\text{total}}$ but changing the *distribution* of opacity between channels.

### 3.3 Cybernetic Interpretation [I] {#cybernetic-interpretation}

**Cybernetic interpretation [I]:** Goldstone modes describe **natural oscillations of attention** — the background redistribution of the "opacity focus" between sectors. The system neither loses nor gains overall opacity level, but slowly retunes itself.

This explains a fundamental property of conscious experience: **attention cannot be simultaneously focused on everything.** Strengthening Gap in one channel (focusing on sound) inevitably weakens Gap in another (peripheral vision "blurs"). Goldstone modes are the mathematical description of this inevitable trade-off.

---

## 4. Free Oscillations of Consciousness {#free-oscillations}

### 4.1 What Is Felt When a Mode Oscillates {#subjective-experience}

Each Goldstone mode is an oscillation of opacity between a pair of channels. But since the [seven dimensions](/docs/core/structure/dimension-u) of the holonom carry *semantic* content (A — Agent, S — Subject, D — Action, L — Lexicon, E — Experience, O — Observer, U — Universe), the oscillations are not abstract: they carry *subjective* meaning.

**Mode $(E, O)$:** opacity oscillates between Experience and Observer. Subjectively: rhythmic alternation between "immersion in the experience" and "detached observation." This is the classical "flickering of consciousness" described by meditative traditions as the alternation of samadhi and vipassana.

**Mode $(L, D)$:** oscillates between Lexicon and Action. Subjectively: alternation between "inner monologue" and "readiness for action." A familiar feeling: you formulate a thought, then switch to action, then back to thought.

**Mode $(A, U)$:** oscillates between Agent and Universe. Subjectively: alternation between "I am the doer" and "I am part of the whole." This is the oscillation between a sense of agency and a sense of dissolution, well known in the phenomenology of altered states.

### 4.2 Why We Do Not Notice the Modes {#invisibility}

Goldstone modes are *infra-slow*: their frequencies $\sim 0.01$ Hz, periods $\sim 100$ s. Ordinary introspective "scanning" occurs on timescales $\sim 1$ s (frequency $\sim 1$ Hz), which is two orders of magnitude faster. We do not notice the modes for the same reason we do not notice the tide: the process is too slow for our attentional "temporal resolution."

But they can be detected *objectively* — through analysis of fMRI and EEG in the ultra-slow range. And — even more interestingly — *subjectively* in extended meditation, when the temporal resolution of introspection increases.

---

## 5. Comparison with Physical Analogues {#comparison}

It is instructive to compare CC Goldstone modes with their physical analogues, to see what is shared and what is unique:

| Property | Phonons (crystal) | Magnons (magnet) | Pions (QCD) | CC Goldstone modes |
|----------|--------------------|------------------|-------------|---------------------|
| Broken symmetry | Translational | Rotational $\mathrm{SO}(3)$ | Chiral $\mathrm{SU}(2)_L \times \mathrm{SU}(2)_R$ | $G_2 = \mathrm{Aut}(\mathbb{O})$ |
| Stabiliser | Lattice translations | $\mathrm{SO}(2)$ | $\mathrm{SU}(2)_V$ | $H \in \{G_2, \mathrm{SU}(3), \mathrm{SU}(2) \times \mathrm{U}(1), T^2\}$ |
| Number of modes | 3 (acoustic) | 1 (for $S = 1/2$) | 3 ($\pi^+, \pi^-, \pi^0$) | $\in \{0, 6, 10, 11, 12\}$ |
| Mass | 0 (exact) | 0 (at $T = 0$) | 135–140 MeV (quasi) | $m_{\text{Gold}}^2 = \Gamma_2 \kappa_0 / |\gamma|^2$ (quasi) |
| Source of mass | — | Thermal fluctuations, anisotropy | Nonzero quark masses | Decoherence $\Gamma_2$, regeneration $\kappa_0$ |
| Propagation medium | Crystal lattice | Spin lattice | QCD vacuum | Internal space $\mathcal{D}(\mathbb{C}^7)$ |
| Characteristic frequency | $10^{12}$ Hz (THz) | $10^{9}$–$10^{12}$ Hz (GHz–THz) | $10^{23}$ Hz | $0.005$–$0.02$ Hz |
| Observability | Raman spectroscopy | Neutron scattering | Particle detectors | fMRI, EEG |

Two features make CC modes *unique*:

1. **Extremely low frequency.** 25 orders of magnitude lower than phonons. This reflects the *macroscopic* character of consciousness: the timescales of cognitive processes are seconds and minutes, not picoseconds.

2. **Variable number of modes.** In physics the number of Goldstone modes is fixed for a given system. In CC it *depends on the state of consciousness* (through the rank of the Gap operator): from 0 in coma to 12 in deep concentration. This is a dynamic symmetry breaking that changes on the fly.

---

<a id="предсказание-isf"></a>

## 6. Falsifiable Prediction: Connection to ISF [H] {#isf-prediction}

### 6.1 Prediction of Infra-Slow Fluctuations {#frequency-prediction}

:::warning Prediction (Goldstone modes $\leftrightarrow$ infra-slow fluctuations) [H]
Frequency of quasi-Goldstone modes:

$$
f_{\text{Gold}} = \frac{\omega_{\text{Gold}}}{2\pi} \approx \frac{1}{2\pi}\sqrt{\frac{\kappa}{m}} \sim 0.005\text{–}0.02 \;\text{Hz}
$$

This coincides with the range of **infra-slow neuronal fluctuations** (ISF) observed in resting-state fMRI ($0.01$–$0.1$ Hz).

**Status:** algebra [T], frequency coincidence [H], experimental verification [P].
:::

:::warning Free parameters in the numerical prediction [C]
The specific range $0.005$--$0.02$ Hz depends on the values of $\kappa$ and $m_{\text{Gold}}$, which are **not determined** from first principles but estimated by order of magnitude. With two free parameters ($\kappa$, $m$) the ISF range can be fitted post hoc. The falsifiable content is the **structural** prediction (number of components $\in \{6, 10, 12\}$, dependence on state of consciousness), not the exact frequency range. Status of the numerical prediction: **[C]**, not [T].
:::

### 6.2 What Is Known about ISF from Experiment {#isf-data}

Infra-slow fluctuations (ISF) are a well-documented neurophysiological phenomenon:

- **Discovery:** First noticed in resting-state fMRI as spontaneous oscillations of the BOLD signal (Biswal et al., 1995).
- **Frequency range:** $0.01$–$0.1$ Hz, with the core at $0.01$–$0.03$ Hz.
- **Properties:** Spatially organised into "resting-state networks" (default mode network, DMN), exhibiting anti-correlations between DMN and the task-positive network.
- **Dependence on consciousness:** Weakened under anaesthesia (Boveroux et al., 2010), disappear in deep coma (Noirhomme et al., 2010), enhanced during meditation (Brewer et al., 2011).

This profile is precisely what the theory predicts: modes that depend on the level of consciousness, with a characteristic frequency in the ultra-slow range.

### 6.3 Quantitative Predictions

| Opacity rank | $n_{\text{Gold}}$ | Prediction for ISF |
|--------------|-------------------|--------------------|
| 1 | 6 | 6 independent ISF components |
| 2 | 10 | 10 ISF components |
| 3 | 12 | 12 ISF components |

Comparison with ICA decomposition data from resting-state fMRI: the typical number of independent ISF components is $\sim 10$–$20$, consistent with rank 2–3.

### 6.4 Specific Predictions for EEG

| Parameter | Prediction | Verification method |
|-----------|------------|---------------------|
| Frequency range | $0.005$–$0.02$ Hz | Spectral analysis of EEG in the $0.001$–$0.1$ Hz band |
| Number of components | $6$, $10$, or $12$ | ICA decomposition of ultra-slow EEG |
| Absence in coma | $n_{\text{Gold}} \to 0$ | Comparison of spectra: consciousness vs. coma |
| Dependence on meditation | Shift in $f_{\text{Gold}}$ with change in $\kappa$ | Longitudinal study of meditators |

### 6.5 The Key Structural Test: Discrete Number of Modes {#structural-test}

The strongest (and most falsifiable) prediction is *not* the numerical value of the frequency, but the *discreteness* of the number of modes. The theory asserts that the number of independent ISF components can only take values from the set $\{0, 6, 10, 11, 12\}$ — and no others. This is a direct consequence of the classification of subgroups of $G_2$:

$$
n_{\text{broken}} \in \{0, 6, 10, 11, 12\} \quad \text{and no other values}
$$

If ICA decomposition finds, say, a stable 8 or 15 components, this *falsifies* the $G_2$ mechanism. If it finds 10 or 12 — this *confirms* it with high specificity, since the posterior probability of a random coincidence with one of the five discrete values is small.

---

## 7. Experimental Verification Protocol [P] {#protocol}

:::caution Verification programme [P]
**Stage 1: Spectral analysis (EEG)**

1. Record 64-channel EEG at rest (eyes-closed, 30 min)
2. Bandpass filtering: $0.001$–$0.1$ Hz
3. Compute power spectrum in the ultra-slow range
4. Determine the number of significant peaks in the $0.005$–$0.02$ Hz band
5. Compare with prediction: $n_{\text{peaks}} \in \{6, 10, 12\}$

**Stage 2: Dependence on state of consciousness**

1. Repeat for states: wakefulness, sleep (N1–N3, REM), anaesthesia
2. Prediction: number of ISF components decreases with decreasing level of consciousness
3. In deep anaesthesia / coma: $n_{\text{peaks}} \to 0$

**Stage 3: Correlation with G₂ structure**

1. Construct the $21 \times 21$ correlation matrix (see [G₂ Noether charges](./g2-noether-cc))
2. Verify [Ward identities](/docs/physics/gauge-symmetry/noether-charges#6-тождества-уорда-для-gap-корреляторов)
3. Estimate opacity rank from the number of ISF components
:::

### 7.1 Detailed EEG Study Protocol {#eeg-protocol}

**Participants:** $N \geq 30$, healthy adults, no neurological pathology, no psychotropic medications.

**Equipment:**
- 64-channel EEG (10-20 system + additional electrodes)
- Sampling rate $\geq 500$ Hz (for artefacts), but key data in the 0.001–0.1 Hz band
- Reference: average of ear electrodes
- Simultaneous ECG, EOG recording (for artefact correction)

**Recording protocol:**
1. **Baseline (30 min):** eyes closed, relaxed wakefulness
2. **Task (15 min):** N-back (working memory) — to change opacity rank
3. **Meditation (30 min):** experienced meditators, open monitoring
4. **Sleep (where possible):** overnight polysomnography with full EEG

**Data analysis:**
1. Preprocessing: artefact removal (ICA), re-referencing
2. Bandpass filtering: $0.001$–$0.1$ Hz (causal filter, to avoid phase distortion)
3. Spectral analysis: multitaper method (Thomson, 1982) to increase spectral resolution
4. ICA decomposition in the ultra-slow range: determination of the number of statistically significant components
5. Comparison with prediction: $n_{\text{ICA}} \in \{6, 10, 11, 12\}$

**Statistical criteria:**
- $H_0$: the number of ISF components is continuously distributed (does not cluster around $\{6, 10, 12\}$)
- $H_1$: the number of ISF components is discrete, consistent with the $G_2/H$ prediction
- Test: comparison of the distribution of $n_{\text{ICA}}$ with uniform ($\chi^2$ criterion or bootstrap)

### 7.2 fMRI Study Protocol {#fmri-protocol}

**Advantages of fMRI:** higher spatial resolution, direct access to ISF via the BOLD signal.

**Protocol:**
1. Resting-state fMRI, 20 min, TR $\leq 1$ s (to access $f \leq 0.5$ Hz)
2. ICA decomposition (FSL MELODIC or equivalent)
3. Extraction of components with a power peak in $0.005$–$0.02$ Hz
4. Count of such components
5. Repeat in different states: wakefulness, propofol sedation (light, deep)

**Prediction:** the number of ISF components decreases discretely ($12 \to 10 \to 6 \to 0$) with deepening sedation, reflecting the sequential restoration of $G_2$-symmetry.

---

## 8. Excitation Spectrum: The Full Picture [T] {#spectrum}

The full space of small oscillations around the stationary Gap profile divides into three sectors:

| Sector | Number of modes | Frequency | Physical meaning |
|--------|-----------------|-----------|-----------------|
| Massive | $21 - n_{\text{broken}} - n_{\text{top}}$ | $\omega_{\text{mass}}^2 = \mu_{\text{eff}}^2 + \kappa/m$ | Oscillations perpendicular to the $G_2$ orbit |
| Quasi-Goldstone | $n_{\text{broken}}$ | $\omega_{\text{Gold}}^2 = \kappa/m - \Gamma_2^2/(4m^2)$ | Slow oscillations along the $G_2$ orbit |
| Topologically protected | $0$ or $1$ | Determined by $Q_{\text{top}}$ | Does not decay without a phase transition |

Total number of modes: $n_{\text{mass}} + n_{\text{Gold}} + n_{\text{top}} = 21$ — equal to the number of independent coherences $\binom{7}{2}$.

### 8.1 Hierarchy of Timescales {#timescale-hierarchy}

The three spectral sectors define three *cardinally different* timescales in consciousness:

| Sector | Characteristic frequency | Timescale | Cognitive analogue |
|--------|--------------------------|-----------|--------------------|
| Massive modes | $\sim 1$–$40$ Hz | $25$–$1000$ ms | Perceptual processes, working memory, alpha/beta/gamma rhythms |
| Goldstone modes | $\sim 0.005$–$0.02$ Hz | $50$–$200$ s | Infra-slow fluctuations, mind-wandering, mode switching |
| Topological mode | $\sim 0$ (does not decay) | $\to \infty$ | Stable "core" of self-consciousness, continuity of the "I" |

This hierarchy explains why consciousness simultaneously *reacts quickly* to stimuli (massive modes), *drifts slowly* in the background (Goldstone modes), and *stably preserves* self-identity (topological mode).

### 8.2 Full Spectrum in the Oscillatory Regime {#full-spectrum}

In the oscillatory regime ($\kappa > \Gamma_2^2/(4m)$ for all sectors) the full spectrum is:

$$
\omega_k = \begin{cases}
\sqrt{\mu_k^2 + \kappa/m} - i\Gamma_2/(2m) & \text{massive, } k = 1, \ldots, 21 - n_{\text{broken}} - n_{\text{top}} \\
\sqrt{\kappa/m - \Gamma_2^2/(4m^2)} - i\Gamma_2/(2m) & \text{Goldstone, } k = 1, \ldots, n_{\text{broken}} \\
\omega_{\text{top}} & \text{topological, } k = 0 \text{ or } 1
\end{cases}
$$

The Goldstone modes form a *quasi-degenerate* cluster near the lower edge of the spectrum: their frequencies are nearly equal (the small spread is determined by the nuances of the $G_2$ structure), but *much lower* than the massive modes. This is the spectral gap separating "fast" processes from "slow" ones.

---

## 9. Goldstone Modes and Consciousness Phase Transitions {#phase-transitions}

### 9.1 Connection to the Phase Diagram {#connection-to-phases}

The [Gap phase diagram](/docs/core/dynamics/gap-phase-diagram) distinguishes three phases: symmetric (coherent), intermediate, and "frozen" (decohered). Goldstone modes play a key role at *transitions* between phases:

- **Symmetric phase** ($P < P_{\text{crit}}$): $G_2$ is unbroken, $n_{\text{broken}} = 0$, no modes. The system is "faceless" — all Gap directions are equivalent.
- **Intermediate phase** ($P \in (P_{\text{crit}}, 3/7]$): $G_2$ is broken, modes appear. The number of modes grows as $P$ increases (the rank of the Gap operator grows). This is the region of *conscious experience*.
- **At the phase transition** $P \to P_{\text{crit}}$ from below: modes "condense" — their mass tends to zero, lifetime to infinity, amplitude to zero. This is *critical* slowing, analogous to the divergence of the correlation length at a second-order phase transition.

### 9.2 Critical Slowing at Loss of Consciousness {#critical-slowing}

During falling asleep, anaesthesia, or loss of consciousness, the *reverse* phase transition occurs: $P$ decreases toward $P_{\text{crit}}$. The Goldstone modes:

1. **Slow down:** $\omega_{\text{Gold}} \to 0$, frequency tends to zero.
2. **"Spread out":** mode coherence drops, spectral lines broaden.
3. **Disappear:** $n_{\text{broken}} \to 0$ upon full restoration of $G_2$-symmetry.

This prediction is directly testable: upon administration of an anaesthetic, the ISF spectrum should show a *red shift* (shift to lower frequencies) followed by *disappearance* of ISF peaks.

---

## 10. Status Summary {#statuses}

| Result | Status |
|--------|--------|
| Spontaneous breaking $G_2 \to H$: $n_{\text{broken}} = 14 - \dim(H)$ | [T] |
| Quasi-Goldstone mass: $m_{\text{Gold}}^2 = \Gamma_2 \kappa_0 / \lvert\gamma\rvert^2$ | [T] |
| Three spectral sectors (massive, Goldstone, topological) | [T] |
| Modes redistribute Gap preserving $\mathcal{G}_{\text{total}}$ | [T] |
| Frequency $f_{\text{Gold}} \sim 0.005$–$0.02$ Hz | [C] (numerical range depends on $\kappa$, $m$) |
| Coincidence with ISF range | [H] |
| Number of ISF components $\in \{6, 10, 12\}$ determined by rank | [H] |
| Discreteness of number of modes (only $\{0, 6, 10, 11, 12\}$) | [H] |
| Red shift of ISF upon loss of consciousness | [H] |
| Experimental verification protocol | [P] |
| Cybernetic interpretation (attentional oscillations) | [I] |
| Subjective experience of modes (flickering of consciousness) | [I] |

---

## What We Learned {#what-we-learned}

Summary of key results:

- **Goldstone modes** are an inevitable consequence of spontaneous $G_2$-symmetry breaking in Phase I. Their number $n_{\text{broken}} = 14 - \dim(H)$ takes only discrete values: $\{0, 6, 10, 11, 12\}$ (Theorem 1.1 [T]).
- **Modes are quasi-massless**: mass $m_{\text{Gold}}^2 = \Gamma_2 \kappa_0 / |\gamma|^2$ is nonzero due to the openness of the system (decoherence + regeneration), by analogy with pion masses from quark masses (Theorem 2.1 [T]).
- **Modes redistribute Gap**, neither creating nor destroying it: $\sum \delta\mathrm{Gap}(i,j) = 0$. This is the mathematics of *attentional oscillations* (Theorem 3.1 [T]).
- **Three spectral sectors** define three timescales: massive modes (ms, perception), Goldstone modes ($\sim 100$ s, mind-wandering), topological mode ($\to \infty$, continuity of the "I").
- **Falsifiable prediction**: the number of ISF components in ICA decomposition of fMRI should take values from $\{0, 6, 10, 11, 12\}$ and decrease discretely upon loss of consciousness [H]. Frequency range $\sim 0.005$--$0.02$ Hz coincides with ISF [C].
- **Critical slowing** at $P \to P_{\text{crit}}$: modes slow down, spread out, and disappear — red shift of the ISF spectrum under anaesthesia [H].
- **Subjective experience** of modes: flickering of consciousness ($E \leftrightarrow O$), speech/action oscillations ($L \leftrightarrow D$), oscillations of agency ($A \leftrightarrow U$) [I].

---

### Bridge to the Next Chapter

We have described Goldstone modes — the "echo" of broken $G_2$-symmetry. But behind every broken continuous symmetry stands a *conservation law* (Noether's theorem). What quantities exactly are conserved when $G_2$ acts on the Gap profile? What do these conserved charges mean cybernetically? And how can they be measured experimentally?

In the [next chapter](./g2-noether-cc) we translate the $G_2$ Noether charge formalism into the language of coherence cybernetics: 7 Fano charges + 7 inter-sector charges, Ward identities for Gap correlators, and a concrete experimental verification protocol for the $G_2$ structure.

---

## Related Documents

- [Gap Phase Diagram](/docs/core/dynamics/gap-phase-diagram) — three phases, Goldstone modes (mathematical foundation)
- [Gap Operator](/docs/core/dynamics/gap-operator) — stabilisers, opacity rank
- [G₂ Noether Charges](/docs/physics/gauge-symmetry/noether-charges) — broken symmetries, Goldstone modes
- [G₂ Structure](/docs/physics/gauge-symmetry/g2-structure) — $G_2 = \mathrm{Aut}(\mathbb{O})$
- [CC Phase Diagram](./phase-diagram-cc) — cybernetic interpretation of phases
- [Falsifiability](/docs/reference/falsifiability) — prediction verification criteria
- [CC Predictions](./predictions) — unique predictions of the theory
- [Topological Protection of Coherence](./topological-protection) — protection of Gap configurations
- [Gap Thermodynamics](/docs/core/dynamics/gap-thermodynamics) — potential $V_{\text{Gap}}$, $T_{\text{eff}}$
- [Coherence Matrix](/docs/core/dynamics/coherence-matrix) — definition of $\Gamma$ and its properties
- [Seven Dimensions](/docs/core/structure/dimension-u) — semantics of A, S, D, L, E, O, U
- [Measurement Methodology](./measurement) — how to detect Goldstone modes experimentally
- [Comparison with Alternatives](./comparison) — uniqueness of the mode prediction for CC
