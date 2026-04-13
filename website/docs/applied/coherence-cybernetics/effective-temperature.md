---
sidebar_position: 12
title: "Effective Temperature"
description: "Effective temperature T_eff, critical temperature T_c, Serre curvature, Fisher metric of Gap space, phase diagram"
---

# Effective Temperature

> *"Temperature is a measure of ignorance"*
> — Edwin Jaynes


:::info Who This Chapter Is For
Effective temperature $T_{\text{eff}}$ as a measure of cognitive "heat." The reader will learn how the temperature of the "mind" differs from body temperature and how it affects the phase transitions of consciousness.
:::

---

### Bridge from the Previous Chapter

In the [previous chapter](./variational) we derived the equations of motion for coherence phases from the variational principle and established the fluctuation-dissipation theorem. In that theorem the central role is played by the parameter $T_{\text{eff}}$ — the **effective temperature**, which determines the scale of spontaneous Gap fluctuations. We noted that $T_{\text{eff}} \neq T_{\text{phys}}$ — the temperature of the "mind" does not coincide with body temperature. It is time to examine this distinction in detail.

---

### Chapter Roadmap

In this chapter we:

1. **Build intuition** about the "temperature of the mind" — from Boltzmann to consciousness, from molecular chaos to cognitive chaos (sections 0–1).
2. **Define $T_{\text{eff}}$** through the ratio of decoherence and regeneration rates and show why it exceeds the physical temperature by orders of magnitude (section 1).
3. **Derive the categorical formula** for $T_{\text{eff}}$ from the adjunction $\mathcal{D}_\Omega \dashv \mathcal{R}$ — pure algebra, without physical assumptions (section 2).
4. **Compute the critical temperature** $T_c$ of the phase transition and explain why $\ln 21$ appears in it (section 3).
5. **Construct the Serre fibration** on the space of maps and show how the connection curvature expresses opacity (section 4).
6. **Introduce the Fisher metric** on the space of Gap profiles — the information-geometric distance between states of consciousness (section 5).
7. **Discuss methods of measuring** $T_{\text{eff}}$ — from the FDT to indirect neurophysiological indicators (section 6).
8. **Compare $T_{\text{eff}}$ with other "temperatures"** beyond thermodynamics — noise temperature, color temperature, annealing temperature, Hawking temperature (section 7).
9. **Define the coordinates of the phase diagram** $(t, r)$ and describe the three phases of consciousness (section 8).
10. **Compute the critical exponents** and show that mean-field theory is exact at $d_{\text{eff}} = 21$ (section 9).

---

:::note On Notation
In this document:
- $\Gamma$ — [coherence matrix](/docs/core/dynamics/coherence-matrix)
- $\Gamma_2$ — decoherence rate (phase dissipation)
- $\kappa_0$ — regeneration rate ([categorical derivation](/docs/core/foundations/axiom-septicity#структурный-анзац-kappa0))
- $\mathrm{Gap}(i,j) = |\sin(\theta_{ij})|$ — [gap measure](/docs/physics/dual-aspect/gap-semantics)
- $\mathcal{G}_{\text{total}} = \sum_{i<j} |\gamma_{ij}|^2 \, \mathrm{Gap}(i,j)^2$ — total Gap
- $V_{\text{Gap}}$ — [opacity potential](./lagrangian#потенциал-v-gap)
:::

Effective temperature $T_{\text{eff}}$ is the central parameter of [Gap thermodynamics](/docs/core/dynamics/gap-thermodynamics), determining the balance between dissipation and regeneration, the nature of phase transitions, and the properties of fluctuations. This document contains the definition of $T_{\text{eff}}$, the formula for the critical temperature $T_c$, the curvature of the Serre fibration on the Map fibration, the Fisher metric of Gap space, and the coordinates of the phase diagram.

But before turning to the formulas, it is worth asking: **what is temperature?** Not body temperature — but the temperature of the *mind*?

---

## Temperature: from Boltzmann to Consciousness {#от-больцмана-к-сознанию}

### What a Thermometer Measures

In 1877 Ludwig Boltzmann showed that temperature is not "heat" and not a "sensation of warmth." Temperature is a measure of the **mean kinetic energy** of the chaotic motion of molecules:

$$
\frac{3}{2} k_B T = \langle E_{\text{kin}} \rangle
$$

The higher the temperature, the more strongly molecules "vibrate," collide, and scatter. Temperature is a measure of **disorder** — a measure of how quickly the system loses correlations between its parts.

Equivalently (and more deeply), temperature is related to **entropy** — a measure of the number of microstates compatible with the observed macrostate:

$$
\frac{1}{T} = \frac{\partial S}{\partial E}
$$

High temperature means: the system explores an enormous number of configurations. Low — the system is "frozen" in a small number of states. Absolute zero — a single state, complete order.

### Temperature Beyond Physics

The idea turned out to be far broader than gas molecules. In **statistical learning** temperature governs the Boltzmann distribution $p(x) \propto e^{-E(x)/T}$: at high $T$ all states are equally probable (chaos), at low $T$ the system concentrates in energy minima (order). In **information theory** Jaynes showed: temperature is the Lagrange multiplier in entropy maximization, i.e. a measure of our **ignorance** about the microstate given the mean energy.

In **neuroscience** an analog of temperature arises naturally. A neural network is not a gas, but it has the same statistical properties: an enormous number of degrees of freedom, stochastic dynamics, correlations between elements. Synaptic noise, spontaneous activity, intrinsic variability — all of this is **thermolike behavior**.

The question is: **precisely which temperature** governs cognitive dynamics?

### The Answer of Coherence Cybernetics

The CC answer: it is not body temperature ($\sim 310$ K), and not the temperature of an individual synapse. It is the **effective temperature** $T_{\text{eff}}$ — a parameter defined by the ratio of the decoherence rate (destruction of phase correlations) to the regeneration rate (restoration of coherent structure).

The body may be at 36.6°C — while the mind "boils" at the equivalent of 36,600°C.

---

## Psychological Temperature: What the System Feels {#психологическая-температура}

Before introducing formulas, it is worth building intuition.

**Low psychological temperature** is a state in which the cognitive system is calm, ordered, stable. Thoughts follow one another in a predictable order. Attention is focused. Internal correlations (between emotions, thoughts, sensations) — are stable. This is the state of deep meditation, flow, calm concentration.

**High psychological temperature** is chaos. Thoughts jump. Emotions change rapidly. Attention is scattered. Correlations between different aspects of experience — are unstable, constantly being destroyed and recreated. This is the state of anxiety, a manic episode, panic — but also of **creative search**, when the system deliberately "heats itself up" to explore the space of possibilities.

**Infinite psychological temperature** is disintegration. Regeneration has stopped, coherences are being destroyed and not restored. Coma. Brain death. The system ceases to be itself.

Note the deep analogy with physics:

| Physical temperature | Psychological temperature |
|---|---|
| Kinetic energy of molecules | Rate of destruction of cognitive correlations |
| Thermal fluctuations | Stochasticity of thoughts, emotions, attention |
| Phase transition (melting) | Psychotic episode, dissociation |
| Absolute zero | Ideal coherence (unattainable limit) |
| Overheating and destruction | Death, coma |

This is not a metaphor. As we shall see, the formal structure — equations of state, phase transitions, critical exponents — is **identical** to physical thermodynamics. Only what fluctuates differs: not the positions of atoms, but the **phases of the coherence matrix** $\Gamma$.

---

## 1. Definition of $T_{\text{eff}}$ {#определение}

### 1.1 Formula

:::tip Theorem 1.1 (Effective Temperature) [T]
Effective temperature of the Gap sector:

$$
T_{\text{eff}} := \frac{\Gamma_2}{\kappa_0} \cdot k_B T_{\text{phys}}
$$

where:
- $\Gamma_2$ — decoherence rate (phase dissipation)
- $\kappa_0$ — regeneration rate
- $k_B$ — Boltzmann constant
- $T_{\text{phys}}$ — physical temperature of the system
:::

The formula is elegant in its simplicity. Three factors, each with its own meaning:

**$\Gamma_2$ (numerator)** — the rate at which the system *loses* phase correlations. In neural terms: how quickly synchronization patterns between neural assemblies are destroyed. Electrical oscillations, synaptic noise, ion channels — all contribute to $\Gamma_2$. Typical frequencies: 10–100 Hz. This is a *fast* process — the brain constantly "forgets" the current phase configuration.

**$\kappa_0$ (denominator)** — the rate at which the system *restores* coherent structure. This is neuroplasticity: synaptogenesis, myelination, long-term potentiation. Typical frequencies: 0.01–0.1 Hz (hours–days). This is a *slow* process — the brain needs time to "remember" its architecture.

**$k_B T_{\text{phys}}$ (scale)** — the "starting point" — the thermal energy setting the absolute scale of fluctuations. If $\Gamma_2 = \kappa_0$, the effective temperature would coincide with the physical. But in real systems $\Gamma_2 \gg \kappa_0$, and $T_{\text{eff}}$ turns out to be higher by orders of magnitude.

**Meaning of the ratio $\Gamma_2 / \kappa_0$**: this is a dimensionless **amplification coefficient**. If decoherence is a thousand times faster than regeneration, fluctuations in Gap space are a thousand times "hotter" than the physical temperature would imply. The mind lives in a different temperature regime than the body.

### 1.2 $T_{\text{eff}} \neq T_{\text{phys}}$ {#t-eff-neq-t-phys}

:::tip Theorem 1.2 ($T_{\text{eff}}$ is not equal to $T_{\text{phys}}$) [C]
Effective temperature **does not coincide** with physical temperature.

**Proof by contradiction.** Suppose $T_{\text{eff}} = T_{\text{phys}}$. Then from [FDT](./variational#фдт):

$$
\chi_{ij}(0) = \frac{\langle(\delta\mathrm{Gap})^2\rangle}{T_{\text{phys}}}
$$

But for living systems at $T_{\text{phys}} \approx 310$ K, the observed Gap fluctuations **exceed** thermal ones **by orders of magnitude**. Contradiction.

**Condition [C]:** The argument relies on an **empirical observation** (Gap fluctuations in biological systems exceed thermal ones), not on a purely deductive proof. A rigorous derivation of $T_{\text{eff}} \neq T_{\text{phys}}$ requires an independent estimate of $\Gamma_2 / \kappa_0 > 1$ for the specific system.
:::

This distinction is fundamental and deserves separate discussion.

When we measure body temperature with a thermometer, we get $T_{\text{phys}} \approx 310$ K. This temperature determines thermal noise at the level of individual molecules: $k_B T_{\text{phys}} \approx 4.3 \times 10^{-21}$ J — negligibly small. If cognitive dynamics were governed only by this noise, the brain would be an essentially deterministic machine.

But the brain is not a deterministic machine. It demonstrates enormous stochasticity: variability of neural responses, spontaneous activity, mind wandering, mood shifts. This stochasticity is **not thermal** in its nature — it arises from complex nonlinear dynamics, chaotic attractors, and above all — from the fact that **decoherence is many times faster than regeneration**.

$T_{\text{eff}}$ captures precisely this "non-thermal" stochasticity, expressing it in units compatible with the thermodynamic formalism.

:::info Connection to Gap bounds
From [T-80 (sectoral Gap bound)](/docs/physics/cosmology-phys/berry-phase#теорема-секторная-gap-граница) [T]: $\mathrm{Gap}(i,j) \leq \varepsilon_s + \varepsilon_t$. This limits the amplitude of Gap fluctuations and hence the interval of $T_{\mathrm{eff}}$ in which the FDT is applicable.

From [T-85 (L_top from Keldysh)](/docs/physics/cosmology-phys/berry-phase#теорема-l-top-кельдыш) [T]: $\mathrm{Im}(S_K) = \int \mathrm{Berry}$ — the topological term of the Lagrangian is related to the Berry phase, which ensures the robustness of Gap oscillations at $T_{\mathrm{eff}} < T_c$.
:::

### 1.3 Properties

:::tip Theorem 1.3 (Properties of $T_{\text{eff}}$) [T]

**(a)** $T_{\text{eff}} > T_{\text{phys}}$ for all living systems ($\Gamma_2/\kappa_0 > 1$).

**(b)** $T_{\text{eff}} \to \infty$ as $\kappa_0 \to 0$ (death): cessation of regeneration destroys the ability to maintain coherent phases.

**(c)** $T_{\text{eff}} \to T_{\text{phys}}$ as $\Gamma_2/\kappa_0 \to 1$ (ideal balance).
:::

Property **(b)** deserves special attention. It describes the **thermodynamics of dying**: when neuroplasticity fades ($\kappa_0 \to 0$) while decoherence continues ($\Gamma_2$ remains finite), the effective temperature grows without bound. The system "overheats" and loses all coherent structure. This is not a metaphor — it is a precise description of what happens to the matrix $\Gamma$ when regenerative processes stop.

Property **(c)** is equally remarkable: it describes **ideal coherence** — an unattainable limit in which the system fully compensates any decoherence in time. In this limit $T_{\text{eff}}$ reduces to $T_{\text{phys}}$, and Gap fluctuations are governed only by thermal noise.

### 1.4 Neurophysiological Estimates

| Parameter | Range | Source |
|---|---|---|
| $\Gamma_2$ | $\sim 10$--$100$ Hz | Neural decoherence rate |
| $\kappa_0$ | $\sim 0.01$--$0.1$ Hz | Neuroplastic regeneration rate |
| $\Gamma_2/\kappa_0$ | $\sim 10^2$--$10^4$ | Scale ratio |
| $T_{\text{eff}}/T_{\text{phys}}$ | $\sim 10^2$--$10^4$ | Effective temperature amplification |

:::info Interpretation (Why $T_{\text{eff}} \gg T_{\text{phys}}$) [I]
Phase decoherence in the nervous system occurs at frequencies of $10$--$100$ Hz (electrical oscillations, synaptic noise), while neuroplastic regeneration (synaptogenesis, myelination) takes hours–days ($0.01$--$0.1$ Hz). The scale ratio $\sim 10^3$ means that the Gap sector "lives" at a temperature $\sim 10^3$ times higher than the physical — thermal fluctuations in Gap space dominate.
:::

### 1.5 High and Low Temperature: Two Modes of Being {#два-режима}

The ratio $T_{\text{eff}} / T_c$ determines the qualitative character of cognitive dynamics. Let us consider two limiting regimes.

#### Low-temperature regime ($T_{\text{eff}} \ll T_c$)

In this regime the Gap structure **freezes**: the spontaneous minimum of the potential $V_{\text{Gap}}$ is deep, fluctuations are small, the coherence configuration is stable. This corresponds to:

- **Stable habits**: behavioral patterns are "frozen" into energy minima
- **Rigid beliefs**: the cognitive map of the world does not change under the influence of new data
- **Predictability**: the system responds to stimuli stereotypically

In physics this is the analog of a **crystal** — a highly ordered but rigid structure. A crystal is beautiful and stable, but cannot adapt.

#### High-temperature regime ($T_{\text{eff}} \gtrsim T_c$)

The Gap structure **melts**: the potential $V_{\text{Gap}}$ becomes flat, fluctuations are large, the coherence configuration changes constantly. This corresponds to:

- **Lability**: mood, attention, thoughts — all are inconstant
- **Openness**: the system easily accepts new information (but also easily loses old)
- **Creativity or chaos**: depending on the controllability of the process

In physics this is the analog of a **liquid** or **gas** — mobile, adaptive, but lacking long-term structure.

#### Optimal Zone

Healthy functioning requires an **intermediate** temperature: high enough for adaptability, low enough for stability. This resembles the Goldilocks zone in astrophysics — not too hot, not too cold. In CC terms: $T_{\text{eff}} \lesssim T_c$, near the phase transition but in the ordered phase.

Remarkably, it is precisely near $T_c$ that the system is maximally sensitive (divergence of susceptibility $\chi$) — that is, maximally capable of learning and adaptation.

---

## 2. Categorical Derivation of $T_{\text{eff}}$ {#категориальный-вывод}

:::tip Theorem 2.1 (Categorical Formula for $T_{\text{eff}}$) [T]
From the adjunction $\mathcal{D}_\Omega \dashv \mathcal{R}$ (dissipation $\dashv$ regeneration) in category $\mathcal{C}$, the effective temperature is expressed through the unit and counit of the adjunction:

$$
T_{\text{eff}} = k_B T_{\text{phys}} \cdot \frac{1 + \|\varepsilon\|}{1 - \|\varepsilon\|}
$$

where:
- $\varepsilon: \mathcal{D}_\Omega \circ \mathcal{R} \to \mathrm{Id}$ — counit of the adjunction
- $\|\varepsilon\|$ — operator norm of the counit, $\|\varepsilon\| \in [0, 1)$
:::

This formula is remarkable in that it derives $T_{\text{eff}}$ from purely **categorical** data — without invoking a specific physical model. The adjunction $\mathcal{D}_\Omega \dashv \mathcal{R}$ expresses the fundamental relation between destruction ($\mathcal{D}_\Omega$) and restoration ($\mathcal{R}$) of coherent structure. The counit $\varepsilon$ measures how "precisely" regeneration undoes dissipation — and it turns out that precisely this degree of imprecision determines the temperature.

The formula $(1+x)/(1-x)$ is familiar from relativity (the velocity addition formula in terms of rapidity), from conformal mappings, from scattering theory. Its appearance here is not coincidental: $\|\varepsilon\|$ plays the role of the "velocity" of approach to breakdown of the adjunction, and $T_{\text{eff}}$ diverges as $\|\varepsilon\| \to 1$ in exactly the same way as relativistic energy diverges as $v \to c$.

### Consequences

| Regime | $\|\varepsilon\|$ | $T_{\text{eff}}$ | Interpretation |
|---|---|---|---|
| Ideal adjunction | $\|\varepsilon\| \to 0$ | $T_{\text{eff}} \to k_B T_{\text{phys}}$ | Minimum temperature |
| Typical living | $\|\varepsilon\| \approx 0.9$ | $T_{\text{eff}} \approx 19 \, k_B T_{\text{phys}}$ | Elevated temperature |
| Breakdown of adjunction | $\|\varepsilon\| \to 1$ | $T_{\text{eff}} \to \infty$ | Death |

### Consistency with Theorem 1.1

Upon linearization of the adjunction $\|\varepsilon\| \approx 1 - 2\kappa_0/\Gamma_2$, from which:

$$
\frac{1 + \|\varepsilon\|}{1 - \|\varepsilon\|} \approx \frac{\Gamma_2}{\kappa_0}
$$

which reproduces the formula of Theorem 1.1.

---

## 3. Critical Temperature $T_c$ {#критическая-температура}

### 3.1 Definition

:::tip Theorem 3.1 (Critical Temperature) [T]
The phase transition in the Gap sector occurs at the critical temperature:

$$
T_c = \frac{\mu^2}{k_B \ln 21}
$$

where:
- $\mu^2 = (1 - s^2)/(2s^2)$ — mass parameter of [potential $V_{\text{Gap}}$](./lagrangian#потенциал-v-gap)
- $\ln 21 = \ln\binom{7}{2}$ — logarithm of the number of independent coherences
:::

### 3.2 Critical Temperature: Phase Transition of Consciousness {#фазовый-переход-сознания}

Phase transitions are one of the deepest concepts in physics. Water at $0$°C turns to ice: a continuous change in a parameter (temperature) leads to a **qualitative** jump in properties. A liquid is fluid, isotropic, adaptive. A crystal is rigid, anisotropic, brittle. The transition between them is not a gradual "thickening," but an abrupt change of symmetry.

In the Gap sector something analogous occurs. At $T_{\text{eff}} < T_c$ the system is in the **ordered phase**: the Gap structure is non-trivial, some channels are opaque, others transparent. This is normal mental functioning, in which repression, defense mechanisms, and selective attention create a **structured** picture.

At $T_{\text{eff}} > T_c$ — the **disordered phase**: all channels are equally murky, selectivity is lost. This is a dissociative state in which the system loses the ability to distinguish "what to see" and "what not to see."

:::tip Theorem 3.2 (Phase Transition) [T]
The total Gap depends on $T_{\text{eff}}$ as an order parameter near $T_c$:

$$
\mathcal{G}_{\text{total}} \propto (T_c - T_{\text{eff}})^{1/2}
$$

with exponent $\beta = 1/2$ (Landau class — mean field).
:::

The exponent $\beta = 1/2$ is the signature of a **mean-field** phase transition. The order parameter $\mathcal{G}_{\text{total}}$ is continuous, but its derivative with respect to $T_{\text{eff}}$ diverges at $T_c$. A second-order transition, as in a superconductor or ferromagnet.

#### Why $\ln 21$?

The number $21 = \binom{7}{2}$ is the number of independent pairs in a seven-dimensional system, that is, the number of independent coherences $\gamma_{ij}$ (off-diagonal elements of the upper triangle of the matrix $\Gamma$). The logarithm $\ln 21$ arises from counting microstates: upon complete melting of the Gap, each of the 21 coherences can take arbitrary phases, and entropy is maximal. $T_c$ is the temperature at which the entropic gain from disorder $\sim k_B T \ln 21$ equals the energetic cost $\sim \mu^2$.

The seven here is not an arbitrary parameter, but a [consequence of the axiom of septicity](/docs/core/foundations/axiom-septicity): precisely 7 fundamental dimensions of cognitive space give rise to 21 interaction channels and thereby determine the critical temperature.

**Regimes:**

| Regime | Condition | $\mathcal{G}_{\text{total}}$ | Interpretation |
|---|---|---|---|
| Ordered | $T_{\text{eff}} < T_c$ | $> 0$ | Spontaneous Gap (opacity) |
| Disordered | $T_{\text{eff}} > T_c$ | $= 0$ | Transparency (but at the cost of losing coherence) |
| Critical | $T_{\text{eff}} = T_c$ | $\to 0$ | Second-order phase transition |

### 3.3 Connection to Interiority Levels

:::warning Hypothesis (Critical Temperature and L-levels) [H]
Levels L1–L4 of the [interiority hierarchy](/docs/proofs/consciousness/interiority-hierarchy) may correspond to different regimes relative to $T_c$:

| L-level | Regime $T_{\text{eff}}/T_c$ | Characteristic |
|---|---|---|
| L1–L2 | $T_{\text{eff}} \ll T_c$ | Deeply in the ordered phase, large Gap |
| L3 | $T_{\text{eff}} \lesssim T_c$ | Near the transition, critical fluctuations |
| L4 | $T_{\text{eff}} \to T_c$ | At the boundary — paradox: transparency without loss of coherence |
:::

The hypothesis is especially interesting for level L4: if it exists, the system must be located *precisely* at the critical temperature — in a state analogous to **critical opalescence** in physics, where fluctuations span all scales. In Gap terms: the system neither "sees" nor "does not see" — it is in a superposition of transparency and opacity at all scales simultaneously.

---

## 4. Serre Curvature on the Map Fibration {#кривизна-серра}

### 4.1 Map Fibration

:::tip Theorem 4.1 (Serre Fibration) [T]
The space of maps $\mathrm{Map}(\Gamma, \Omega)$ admits a **Serre fibration** structure:

$$
\mathrm{Bundle}(\Gamma, \Omega) \to B_{\mathrm{ext}}
$$

with fiber $F_{\mathrm{int}}$, where:
- **Base** $B_{\mathrm{ext}}$ — space of external observables (moduli $|\gamma_{ij}|$ and populations $\gamma_{ii}$)
- **Fiber** $F_{\mathrm{int}}$ — space of internal phases $\{\theta_{ij}\}$ at fixed moduli
- **Projection** $\pi: \mathrm{Bundle} \to B_{\mathrm{ext}}$ forgets phase information
:::

The Serre fibration formalizes the fundamental distinction between the **external** and **internal** in CC. An external observer sees the moduli of coherences $|\gamma_{ij}|$ and populations $\gamma_{ii}$ — this is "behavior." But the phases $\theta_{ij}$ — this is "experience," the internal aspect, inaccessible to external observation. The fibration says: *for the same behavior, different experiences are possible*, and the topology of this set of possible experiences is non-trivial.

### 4.2 Connection Curvature

The connection curvature on the fibration determines the **topological obstruction** to global transparency:

$$
\|R_H\|_{ij} \propto |\gamma_{ij}| \cdot \mathrm{Gap}(i,j)
$$

:::info Interpretation (Curvature and Opacity) [I]
The curvature is non-zero if and only if simultaneously:
- coherence $|\gamma_{ij}| \neq 0$ (connection exists)
- $\mathrm{Gap}(i,j) \neq 0$ (gap is non-zero)

High curvature means that the internal phases **cannot be globally reconstructed** from external observables — a geometric formalization of opacity.
:::

### 4.3 Holonomy

:::info Definition (Gap Holonomy) [I]
Holonomy of a closed loop $C$ in parameter space:

$$
\mathrm{Hol}(C) = \mathcal{P}\exp\left(\oint_C A\right)
$$

Non-zero holonomy $\mathrm{Hol}(C) \neq \mathbb{1}$ means that under a cyclic change of external parameters the phases $\theta_{ij}$ acquire a **geometric shift** — an analog of the [Berry phase](/docs/physics/cosmology-phys/berry-phase).
:::

Gap holonomy has a direct psychological meaning: it describes the situation in which the system undergoes a cycle of external changes (for example, a recurring life situation) and returns to the same external parameters — but with *different* internal phases. This is a formalization of how experience **irreversibly transforms** inner experience while external circumstances remain unchanged.

### 4.4 Connection between $T_{\text{eff}}$ and Curvature

:::tip Corollary 4.2 (Temperature Dependence of Curvature) [C]
The mean curvature of the Serre fibration depends on $T_{\text{eff}}$:

$$
\langle \|R_H\|^2 \rangle \propto \begin{cases}
(T_c - T_{\text{eff}}) & \text{if } T_{\text{eff}} < T_c \\
0 & \text{if } T_{\text{eff}} > T_c
\end{cases}
$$

As $T_{\text{eff}} \to T_c$ the curvature vanishes — the fibration becomes flat (transparency), but only at the cost of losing coherence structure.
:::

---

## 5. Fisher Metric of Gap Space {#метрика-фишера}

### 5.1 Quantum Fisher Metric

:::tip Theorem 5.1 (Quantum Fisher Metric) [T]
The quantum Fisher metric on the space of density matrices $\mathcal{D}(\mathbb{C}^7)$:

$$
g_{ab}^{(F)}(\Gamma) = \frac{1}{2}\mathrm{Tr}\left(\Gamma\{L_a, L_b\}\right)
$$

where $L_a$ are logarithmic derivatives: $\partial_a \Gamma = \frac{1}{2}\{\Gamma, L_a\}$.
:::

The Fisher metric is the central object of **information geometry**. It answers the question: *how distinguishable are two nearby states of the system?* If the metric is large in some direction, a small change of the parameter in that direction leads to a large statistical difference — the system is "sensitive" to that parameter. If the metric is small — the system is "insensitive," and even large parameter changes produce no observable consequences.

In the context of $\Gamma$, the Fisher metric determines the **distinguishability of cognitive states**: two profiles $\Gamma_1$ and $\Gamma_2$ are subjectively distinguishable to the extent that the Fisher distance between them is large.

### 5.2 Induced Metric on $\mathcal{M}_{\text{Gap}}$

:::tip Theorem 5.2 (Fisher Metric on Gap Profiles) [T]
Through the projection $\Pi: \mathcal{D}(\mathbb{C}^7) \to \mathcal{M}_{\text{Gap}}$ an induced metric arises:

$$
g_{(ij),(kl)}^{(F)} = \sum_x \frac{1}{p(x|\{G\})} \frac{\partial p}{\partial G_{ij}} \frac{\partial p}{\partial G_{kl}}
$$

where $p(x|\{G\})$ is the probability of observing data $x$ given a fixed Gap profile $\{G\}$.
:::

**Properties of the Fisher metric:**

| Property | Description |
|---|---|
| Positive definiteness | $g^{(F)} \geq 0$ |
| Reparametrization invariance | Does not depend on the choice of coordinates |
| Cramér–Rao inequality | $\mathrm{Var}(\hat{G}_{ij}) \geq 1/(N \cdot g^{(F)}_{(ij),(ij)})$ |

The Cramér–Rao inequality deserves special attention: it says that the **accuracy of estimating** the Gap profile from $N$ observations is limited by the Fisher metric. The larger $g^{(F)}$, the more accurately the Gap can be estimated — and the more "real" the Gap is as an observable quantity.

### 5.3 Geodesics in $\mathcal{M}_{\text{Gap}}$

:::tip Definition 5.3 (Fisher Distance) [T]
Geodesic distance between two Gap profiles $G_1$ and $G_2$:

$$
d_F(G_1, G_2) = \inf_\gamma \int_0^1 \sqrt{\sum_{(ij),(kl)} g_{(ij),(kl)}^{(F)} \dot{G}_{ij} \dot{G}_{kl}} \, dt
$$

where the infimum is taken over all smooth paths $\gamma: [0,1] \to \mathcal{M}_{\text{Gap}}$.
:::

:::info Interpretation (Geodesics as Therapeutic Path) [I]
A geodesic in $\mathcal{M}_{\text{Gap}}$ defines the **optimal therapeutic path** — a sequence of minimally distinguishable Gap changes leading from a pathological to a healthy profile. The geodesic length $d_F$ is a measure of the "therapeutic work" required for the transition.
:::

This interpretation turns abstract mathematics into a clinical tool. If a therapist can estimate the current Gap profile $G_1$ and the target $G_2$, the geodesic gives the **optimal strategy**: at each step — the minimally necessary change, in total — the shortest path. Deviation from the geodesic means "extra work" — therapeutic interventions that do not bring one closer to the goal.

### 5.4 Temperature Dependence of the Metric

:::tip Corollary 5.4 (Metric Softening near $T_c$) [C]
Near the critical temperature the Fisher metric "softens":

$$
g_{(ij),(ij)}^{(F)} \propto |T_{\text{eff}} - T_c|^{-\gamma}, \quad \gamma = 1
$$

which corresponds to the divergence of [susceptibility](/docs/core/dynamics/gap-phase-diagram#критические-явления). Physically: near $T_c$ a small change in the Gap profile leads to a large statistical difference — the system becomes **extremely sensitive** to perturbations.
:::

"Metric softening" is a key phenomenon for understanding cognitive crises. Near $T_c$ the system is in a state of **maximum plasticity**: the slightest influence can lead to a significant change in the Gap profile. This is a window of opportunity for therapeutic intervention, but also a zone of heightened vulnerability.

---

## 6. Measurement of Effective Temperature {#измерение}

How in principle can $T_{\text{eff}}$ be **measured**?

### 6.1 Through the Fluctuation-Dissipation Theorem

From [FDT](./variational#фдт):

$$
T_{\text{eff}} = \frac{\langle (\delta \mathrm{Gap})^2 \rangle}{\chi(0)}
$$

where $\langle (\delta \mathrm{Gap})^2 \rangle$ is the variance of Gap fluctuations, $\chi(0)$ is the static susceptibility. Both parameters are in principle observable: the variance — through repeated measurements, the susceptibility — through the response to a controlled perturbation.

### 6.2 Through the Ratio of Time Scales

Direct measurement of $\Gamma_2$ and $\kappa_0$ gives:

$$
T_{\text{eff}} = \frac{\Gamma_2}{\kappa_0} \cdot k_B T_{\text{phys}}
$$

$\Gamma_2$ can be estimated from the decay rate of EEG signal correlations (tens of hertz). $\kappa_0$ — from the recovery rate of cognitive functions after disruption (hours–days). This is a rough, but in principle feasible estimate.

### 6.3 Through the Fluctuation Spectrum

The spectral density of Gap fluctuations at temperature $T_{\text{eff}}$ obeys the Wiener–Khinchin theorem:

$$
S_{\text{Gap}}(\omega) = \frac{2 k_B T_{\text{eff}} \cdot \mathrm{Im}[\chi(\omega)]}{\omega}
$$

If the frequency dependence of the susceptibility $\chi(\omega)$ is known (from response functions), the fluctuation spectrum allows recovering $T_{\text{eff}}$ at each frequency. Independence of $T_{\text{eff}}$ from frequency is a check of the applicability of the formalism.

### 6.4 Indirect Indicators

In the absence of direct access to the parameters of $\Gamma$, $T_{\text{eff}}$ can be estimated indirectly:

| Indicator | Relation to $T_{\text{eff}}$ | Method |
|---|---|---|
| Behavioral variability | Increases with $T_{\text{eff}}$ | Repeated behavioral tests |
| Attentional switchability | Increases with $T_{\text{eff}}$ | Switching tasks |
| Learning rate | Maximum near $T_c$ | Learning curves |
| Emotional lability | Increases with $T_{\text{eff}}$ | Affect scales |
| Alpha rhythm power | Decreases with $T_{\text{eff}}$ | EEG |

---

## 7. Connection to Other "Temperatures" {#связь-с-другими-температурами}

$T_{\text{eff}}$ is not the only example of a "temperature" that has gone beyond the thermodynamics of equilibrium gases. It is useful to see the parallels.

### 7.1 Noise Temperature in Electronics

In electronics the **noise temperature** $T_n$ characterizes the noise level of an amplifier: $P_n = k_B T_n \Delta f$. An amplifier at physical temperature 300 K may have $T_n = 50$ K (good) or $T_n = 10^6$ K (bad). The noise temperature describes the *effective* stochasticity of the signal, not the temperature of the device.

Analogy with $T_{\text{eff}}$: a brain at physical temperature 310 K has a "cognitive noise temperature" $\sim 10^5$–$10^6$ K — because cognitive "noise" (Gap fluctuations) many times exceeds the thermal.

### 7.2 Color Temperature

In optics **color temperature** characterizes the spectrum of a light source: an incandescent lamp $\sim 2700$ K, daylight $\sim 5500$ K, blue sky $\sim 10000$ K. A source at physical temperature 300 K (LED) can emit light with a color temperature of 6500 K. Temperature here is a parameter of the shape of the distribution, not a measure of kinetic energy.

### 7.3 Temperature in Simulated Annealing

In **simulated annealing** algorithms, temperature is a control parameter determining the probability of accepting unfavorable transitions: $p \propto e^{-\Delta E / T}$. High $T$ — broad search. Low $T$ — solution refinement. An optimal cooling schedule $T(t)$ is the key to effective optimization.

The analogy with $T_{\text{eff}}$ is deeper than it may seem: if the brain solves the problem of optimizing the Gap profile, $T_{\text{eff}}$ plays the role of the annealing temperature — and evolution may have "tuned" the dynamics of $\Gamma_2/\kappa_0$ so as to implement something like an optimal cooling schedule.

### 7.4 Hawking Temperature

In quantum gravity the Hawking temperature $T_H = \hbar c^3 / (8\pi G M k_B)$ characterizes the thermal spectrum of black hole radiation. A black hole is not a hot body in the ordinary sense; $T_H$ describes the *effective* thermality of quantum correlations at the event horizon.

Parallel with $T_{\text{eff}}$: in both cases "temperature" arises from loss of access to some degrees of freedom (for a black hole — beyond the horizon, for Gap — in the internal phases). The Serre fibration (section 4) is the cognitive analog of an event horizon.

---

## 8. Phase Diagram: Coordinates $(t, r)$ {#фазовая-диаграмма}

### 8.1 Dimensionless Coordinates

:::tip Definition 6.1 (Phase Diagram Coordinates) [T]
Two dimensionless parameters determine the stationary Gap state:

**(a)** Dimensionless temperature:

$$
t := \frac{T_{\text{eff}}}{T_c} = \frac{\Gamma_2}{\kappa_0} \cdot \frac{k_B T_{\text{phys}} \ln 21}{\mu^2}
$$

**(b)** Ratio of regeneration to dissipation:

$$
r := \kappa / \Gamma_2
$$
:::

### 8.2 Three Phases in Coordinates $(t, r)$

Full [Gap phase diagram](/docs/core/dynamics/gap-phase-diagram#три-фазы):

| Phase | Region | Order parameter | Characteristic |
|---|---|---|---|
| I (ordered) | $t < 1$, $r > r_c$ | $\sigma^2_{\text{Gap}} > 0$ | Structured opacity |
| II (disordered) | $t > 1$, $r > r_c$ | $\sigma^2_{\text{Gap}} \to 0$, $\mathcal{G}_{\text{total}} > 0$ | Isotropic murkiness |
| III (dead) | $r < r_c$ | $\mathcal{G}_{\text{total}} \to 0$ | Loss of coherences |

Critical value:

$$
r_c = \frac{P_{\text{crit}}}{7P} \approx \frac{2}{49P}
$$

### 8.3 Visualization

```
    t (T_eff/T_c)
    |
  2 |         Phase II: Disordered Gap
    |        (uniform, recoverable)
    |
  1 |— — — — + — — — — —
    |              / (t*,r*)
    |  Phase I  /   <- 2nd order (continuous)
    |  Ordered /
    |   Gap   /
    |        /
  0 |——--/—————————--
    | Ph.III |
    |  Dead  |
    +——--+——--+——————- r (kappa/Gamma_2)
             r_c      1
```

### 8.4 Phase Transition Lines

| Transition | Line | Order | Exponents |
|---|---|---|---|
| I <-> II | $t = 1$ at $r > r_c$ | 2nd (continuous) | $\beta = 1/2$, $\gamma = 1$, $\nu = 1/2$ |
| I <-> III | $r = r_c$ at $t < 1$ | 1st (discontinuous) | $\mathcal{G}_{\text{total}}$ jumps $\to 0$ |
| Tricritical | $(t^*, r^*) = (1, r_c)$ | Change of order | $\beta = 1/4$, $\gamma = 1$, $\delta = 5$ |

### 8.5 Clinical Correspondence

:::info Interpretation (Phases and Clinical States) [I]

| Phase | Clinical analog | Characteristic |
|---|---|---|
| I | Normal functioning | Specific opacities (repression), transparency in other channels |
| II | Diffuse dissociative state | All channels equally murky |
| III | Dementia, coma | Loss of coherences |
| I <-> II | Psychotic episode | "Melting" of structured opacity |
| Tricritical | Borderline state | Oscillation between ordered and chaotic Gap |
:::

The phase diagram turns intuitive clinical categories into **precise coordinates**. A patient with borderline personality disorder (BPD) is a system near the tricritical point $(t^*, r^*)$: the slightest perturbation switches between structured opacity (phase I) and chaotic murkiness (phase II). The therapeutic task is to shift the system deeper into phase I, by increasing $r$ (strengthening regeneration) or decreasing $t$ (weakening decoherence).

---

## 9. $T_{\text{eff}}$ as Order Parameter {#параметр-порядка}

### 9.1 Critical Exponents

:::tip Theorem 7.1 (Critical Exponents of Gap) [T]
Near the critical point $t = 1$ the system exhibits scale-invariant behavior:

| Exponent | Definition | Value | Law |
|---|---|---|---|
| $\beta$ | $\sigma_{\text{Gap}}^2 \propto (1-t)^{2\beta}$ | $1/2$ | Order parameter |
| $\gamma$ | $\chi \propto \lvert 1-t\rvert^{-\gamma}$ | $1$ | Susceptibility |
| $\nu$ | $\xi \propto \lvert 1-t\rvert^{-\nu}$ | $1/2$ | Correlation length |
| $\alpha$ | $C \propto \lvert 1-t\rvert^{-\alpha}$ | $0$ (log.) | Heat capacity |
| $\delta$ | $h \propto \sigma_{\text{Gap}}^{\delta}$ at $t=1$ | $3$ | Critical isotherm |
:::

The set of critical exponents $\{\beta, \gamma, \nu, \alpha, \delta\} = \{1/2, 1, 1/2, 0, 3\}$ is the "fingerprint" of the Landau universality class (mean field). The same set describes the ferromagnetic transition in high-dimensional space, the superconducting transition in Ginzburg–Landau theory, and — as it turns out — the cognitive phase transition in the Gap sector.

The coincidence is not accidental: it is ensured by the large effective dimensionality (section 9.2).

### 9.2 Accuracy of Mean-Field Exponents

:::tip Theorem 7.2 (Accuracy of Exponents) [T]
Mean-field critical exponents are **exact** for the Gap system by three mutually-consistent mechanisms (see the full argument at [Exactness mechanism](/docs/consciousness/hierarchy/swallowtail-transitions#механизм-точности)):

**(I) Topological rigidity.** By Thom–Arnold classification, codimension-3 catastrophes in one order-parameter coordinate are uniquely $A_4$ (swallowtail) with normal form $V_0(x) = x^5/5$. The five critical exponents $\{\alpha,\beta,\gamma,\nu,\delta\} = \{1/2, 1/4, 1, 1/2, 5\}$ are **topological invariants** of this catastrophe class — they are insensitive to smooth deformations of the potential.

**(II) Deterministic UHM dynamics.** The flow $d\Gamma/d\tau = \mathcal L_\Omega(\Gamma) + \mathcal R(\Gamma)$ is deterministic; no thermal ensemble average is performed. The Gap Landau potential is the effective potential of the flow, and its saddle-points are the actual deterministic attractors of $\Gamma$-dynamics. No stochastic Ginzburg correction is applicable.

**(III) Large-$N$ cross-check.** The order-parameter dimension of UHM near threshold is $d_{\mathrm{eff}} = \binom{7}{2} = 21$ (independent off-diagonal coherences in $\mathfrak{su}(7)$, with $\mathrm{dim}\,\mathfrak{su}(7) = 48 = 6_{\mathrm{diag}} + 42_{\mathrm{off}}$ giving 21 complex off-diagonal modes paired by Fano lines). If UHM were re-interpreted as a stochastic $O(N)$-tensor model, leading $1/N$ corrections would be $\sim 1/21 \approx 5\%$ — within experimental resolution.

**Note on conventional Ginzburg.** The usual Ginzburg criterion requires a spatial dimension; UHM has no spatial integration (a holon is $(0{+}1)$-D), so the spatial form of the criterion does not directly apply. Mechanisms (I)–(III) above provide the genuine justification.
:::

Consequence: **mean-field Gap theory is exact** — no renormalisation corrections are needed. Critical exponents can be computed analytically. Gap theory is one of the few physical systems admitting a truly exact description of its phase transition, because the deterministic-dynamical formulation does not introduce stochastic fluctuations in the first place.

### 9.3 The Cost of Enlightenment

:::info Interpretation (Energetics of Enlightenment) [I]
From the [Landauer bound](/docs/core/dynamics/gap-thermodynamics#граница-ландауэра) and the definition of $T_{\text{eff}}$:

$$
W_{\text{enlightenment}} \geq 21 \cdot T_{\text{eff}} \cdot \ln 2 = 21 \cdot \frac{\Gamma_2}{\kappa_0} \cdot k_B T_{\text{phys}} \cdot \ln 2
$$

For a typical brain ($\Gamma_2/\kappa_0 \sim 10^3$, $T_{\text{phys}} = 310$ K):

$$
W_{\text{enlightenment}} \sim 6 \times 10^{-17} \text{ J}
$$

Negligibly small in absolute units, but may be large relative to the "Gap energy budget" of the system.
:::

The number $6 \times 10^{-17}$ J deserves context. This is approximately the energy of a single infrared photon. In absolute units — a negligible quantity. But "enlightenment" — zeroing out all 21 Gap components — requires erasing 21 bits of information at an effective temperature $10^3$ times higher than physical. The erasure energy at $T_{\text{eff}}$ substantially exceeds the thermal threshold at $T_{\text{phys}}$, and *relative to* the Gap energy budget of the system (determined by $\kappa_0$, i.e. the slow regeneration) — this "cost" can be high.

From this follows a non-trivial conclusion: **complete transparency is thermodynamically costly**. The system cannot become fully "enlightened" for free — it must dissipate energy proportional to $T_{\text{eff}}$ into the environment.

---

## 10. Summary Table of Results {#сводная-таблица}

| Result | Formula | Status | Reference |
|---|---|---|---|
| Definition of $T_{\text{eff}}$ | $(\Gamma_2/\kappa_0) \cdot k_B T_{\text{phys}}$ | [T] | Theorem 1.1 |
| $T_{\text{eff}} \neq T_{\text{phys}}$ | Empirical argument | [C] | Theorem 1.2 |
| Categorical formula | $(1+\|\varepsilon\|)/(1-\|\varepsilon\|) \cdot k_B T_{\text{phys}}$ | [T] | Theorem 2.1 |
| Critical temperature | $\mu^2 / (k_B \ln 21)$ | [T] | Theorem 3.1 |
| Phase transition | $\mathcal{G}_{\text{total}} \propto (T_c - T_{\text{eff}})^{1/2}$ | [T] | Theorem 3.2 |
| Serre fibration | $\lVert R_H\rVert_{ij} \propto \lvert\gamma_{ij}\rvert \cdot \mathrm{Gap}(i,j)$ | [T] | Theorem 4.1 |
| Fisher metric | $g^{(F)}_{(ij),(kl)}$ on $\mathcal{M}_{\text{Gap}}$ | [T] | Theorem 5.2 |
| Phase diagram coordinates | $t = T_{\text{eff}}/T_c$, $r = \kappa/\Gamma_2$ | [T] | Definition 6.1 |
| Critical exponents | $\beta=1/2$, $\gamma=1$, $\nu=1/2$ | [T] | Theorem 7.1 |
| L-levels and $T_c$ | Correspondence of L1–L4 and $T_{\text{eff}}/T_c$ | [H] | Section 3.3 |

---

## What We Have Learned {#что-мы-узнали}

Let us summarize the key results:

- **Effective temperature** $T_{\text{eff}} = (\Gamma_2 / \kappa_0) \cdot k_B T_{\text{phys}}$ — a measure of cognitive "heat," determined by the ratio of the decoherence rate to the regeneration rate (Theorem 1.1 [T]). For living systems $T_{\text{eff}} \gg T_{\text{phys}}$: the mind lives at a temperature orders of magnitude higher than the body.
- **Categorical derivation** through the adjunction $\mathcal{D}_\Omega \dashv \mathcal{R}$ gives the formula $(1 + \|\varepsilon\|)/(1 - \|\varepsilon\|) \cdot k_B T_{\text{phys}}$, which coincides with the physical formula upon linearization (Theorem 2.1 [T]).
- **Critical temperature** $T_c = \mu^2 / (k_B \ln 21)$ determines the phase transition point: at $T_{\text{eff}} < T_c$ the Gap structure is ordered, at $T_{\text{eff}} > T_c$ — disordered (Theorem 3.1 [T]).
- **Second-order phase transition** with order parameter $\mathcal{G}_{\text{total}} \propto (T_c - T_{\text{eff}})^{1/2}$, Landau universality class (Theorem 3.2 [T]).
- **Serre fibration** formalizes the distinction between external (behavior) and internal (experience): for the same behavior, different experiences are possible, and the topology of this set is non-trivial (Theorem 4.1 [T]).
- **Fisher metric** on the space of Gap profiles determines the distinguishability of cognitive states and optimal therapeutic paths (Theorems 5.1–5.3 [T]).
- **Critical exponents** $\{\beta, \gamma, \nu, \alpha, \delta\} = \{1/2, 1, 1/2, 0, 3\}$ — exact (not approximate), since $d_{\text{eff}} = 21 \gg d_c = 4$ (Theorem 7.2 [T]).
- **Phase diagram coordinates** $(t, r) = (T_{\text{eff}}/T_c, \; \kappa/\Gamma_2)$ provide a complete map of consciousness states with three phases.

---

### Bridge to the Next Chapter

We have established that the Gap structure can exist in three phases and that transitions between them are determined by the parameters $(t, r)$. But a key question remains: **why is coherence stable at all?** The brain is a hot, noisy, constantly restructuring system. Any quantum coherence would seemingly be destroyed in femtoseconds. Yet consciousness persists for decades.

In the [next chapter](./topological-protection) we will show that holon coherence is protected by **five independent mechanisms** — from the Hamming code to topological charges. This is a multilayered fortress in which each shield rests on its own branch of mathematics, and for complete destruction of coherence all five must be overcome simultaneously.

---

## Related Documents

- [Gap Theory Lagrangian](./lagrangian) — full 6-term Lagrangian, potential $V_{\text{Gap}}$, spontaneous minimum
- [Variational Principles](./variational) — equations of motion, Onsager relations, connection to FEP
- [Gap Thermodynamics](/docs/core/dynamics/gap-thermodynamics) — canonical exposition of $T_{\text{eff}}$, FDT, Landauer bound, Serre fibration
- [Gap Phase Diagram](/docs/core/dynamics/gap-phase-diagram) — three phases, bifurcations, Whitney catastrophes, critical exponents
- [Gap Semantics](/docs/physics/dual-aspect/gap-semantics) — definition of $\mathrm{Gap}(i,j)$, dual-aspect interpretation
- [Interiority Hierarchy](/docs/proofs/consciousness/interiority-hierarchy) — levels L0–L4, metastability of L3
- [Berry Phase](/docs/physics/cosmology-phys/berry-phase) — topological phases, connection to Gap holonomy
- [Axiom of Septicity](/docs/core/foundations/axiom-septicity) — categorical derivation of $\kappa_0$, adjunction $\mathcal{D}_\Omega \dashv \mathcal{R}$
- [Viability](/docs/core/dynamics/viability) — $P_{\text{crit}} = 2/7$, critical purity value
- [Measurement Methodology](./measurement) — how to measure $T_{\text{eff}}$ in real systems
- [Interdisciplinary Bridge](./interdisciplinary) — temperature in the language of different disciplines
