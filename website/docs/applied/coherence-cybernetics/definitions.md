---
sidebar_position: 3
title: Definitions
description: Basic definitions of Coherence Cybernetics
---

# Basic Definitions

:::info Bridge from the Previous Chapter
In the [previous chapter](./axiomatics) we became acquainted with the axiomatic foundation of CC: the single primitive (category $\mathcal{C}$), the five axioms of Ω⁷, and the derivation chain from $\Omega$ to $\Gamma^*$. We saw *where* CC constructions come from. Now we must define them **precisely**: give each concept a formal definition, specify the formula, range of values, and physical meaning. These definitions are the language in which the [theorems of the next chapter](./theorems) are written.
:::

:::tip Chapter Roadmap
In this chapter we:
1. **Define the Holon** $\mathbb{H}$ — the minimal self-sufficient unit of reality (section "Holon")
2. **Introduce six key measures** — purity $P$, entropy $S_{vN}$, integration $\Phi$, differentiation $D_{\text{diff}}$, reflection $R$, consciousness $C$ (section "Key Measures")
3. **Define E-coherence** — the central measure linking experience and dynamics (section "[E-Coherence](#e-когерентность)")
4. **Describe the interiority hierarchy** L0–L4 with precise thresholds (section "[Interiority Hierarchy](#иерархия-интериорности)")
5. **Introduce the stress tensor** $\sigma_{\mathrm{sys}}$ — a diagnostic tool for any system (section "[Stress Tensor](#тензор-напряжений)")
6. **Describe the attractor hierarchy** — three levels of Holon equilibrium (section "[Attractor Hierarchy](#иерархия-аттракторов)")
7. **Show the definitions in action** on three examples: thermostat, brain, LLM (section "Examples")
8. **Discuss operationalization** for AI, biology, and organizations (sections "Operationalization")
:::

This chapter is not a reference guide or a glossary. It is a guide through the conceptual landscape of Coherence Cybernetics. Each definition here is the answer to a specific question: *what exactly are we describing when we speak of a system possessing interiority?*

The reader familiar with physics will find parallels with quantum mechanics and thermodynamics. The biologist will see autopoiesis and homeostasis. The psychologist will recognize models of consciousness and self-regulation. The AI specialist will find metrics that can be computed right now. All these threads converge in one formalism.

:::note On Notation
In this document:
- $\Gamma$ — [coherence matrix](/docs/core/dynamics/coherence-matrix)
- $\varphi$ — [self-modeling operator](/docs/proofs/categorical/formalization-phi)
- $P$ — [purity](/docs/core/dynamics/viability#определение-чистоты)
- $D_{\text{diff}}$ — differentiation measure (not to be confused with dimension $D$)
- $R$, $\Phi$, $C$ — [consciousness measures](/docs/consciousness/foundations/self-observation)
- L0, L1, L2, L3, L4 — [interiority levels](/docs/proofs/consciousness/interiority-hierarchy)
:::

:::info Two Formalisms
Coherence Cybernetics operates in a **minimal 7D formalism** ($\mathcal{H} = \mathbb{C}^7$, [justification of the number 7](/docs/core/foundations/axiom-omega#октонионная-структура)), where all operations are defined directly.

For operations requiring tensor structure (partial trace $\mathrm{Tr}_{-E}$, Holon composition $\otimes$), an **extended formalism** is used ($\mathcal{H} = \mathbb{C}^{42}$ with tensor structure).

**See:** [Relation between formalisms](/docs/core/dynamics/coherence-matrix#согласование-формализмов)
:::

---

## Holon

### Why Is This Concept Needed?

Physics describes particles. Biology — organisms. Psychology — subjects. But what unites an atom, a cell, an ant, and a human as *systems capable of self-maintenance*? The Holon is the answer: the minimal abstraction capturing what makes a system a *self-sufficient unit* of reality.

A Holon is not simply a "system." A stone is not a Holon (no internal dynamics). A heap of sand is not a Holon (no self-maintenance). A thermostat is a borderline case. A living cell is a Holon. A conscious being is a Holon with high coherence indicators.

### Intuition and Analogies

**Analogy 1: A whirlpool.** Imagine the ocean (a single substance $\Gamma$). A whirlpool is not a thing in the ocean but a *pattern* of the ocean: a self-sustaining configuration of water that maintains its form, even though the water molecules are constantly being renewed. A Holon is a stable whirlpool in the ocean of reality.

**Analogy 2: A cell.** A biological cell constantly exchanges matter with the environment, yet preserves its identity. It *creates* the membrane that *defines* what is "cell" and what is "environment." This is autopoiesis: a system generating its own boundaries. The Holon is the formalization of this idea.

**Analogy 3: Leibniz's monad — but better.** Leibniz imagined monads as "perception points" with no windows onto the external world. The Holon is similar — it too is a fundamental unit — but *with windows*: the sensorimotor functors Enc and Dec connect it to the environment. The Holon is a monad that knows how to act.

### Formal Definition

A [Holon](/docs/core/structure/holon) is the minimal self-sufficient unit of reality:

$$
\mathbb{H} := \langle \Gamma, \mathcal{H}, H, \{L_k\}, E, \varphi \rangle
$$

Let us examine each component:

| Component | What it is | Why it is needed | Analogy |
|-----------|-----------|------------------|---------|
| $\Gamma$ | Coherence matrix ($7 \times 7$) | Complete description of state | The system's "DNA" at a given moment |
| $\mathcal{H}$ | Hilbert space $\mathbb{C}^7$ | Arena of dynamics | Space of possible states |
| $H$ | Hamiltonian | Unitary (reversible) evolution | Internal "pendulum" |
| $\{L_k\}$ | Lindblad operators | Irreversible dynamics, dissipation | Friction, interaction with environment |
| $E$ | Environment channel | Connection to surroundings | Monad's "windows" |
| $\varphi$ | Self-modeling operator | Reflection, self-observation | Internal mirror |

Full description of components and properties: [Holon](/docs/core/structure/holon), [Coherence matrix](/docs/core/dynamics/coherence-matrix).

### What Distinguishes a Holon from a "Mere System"?

Four closure conditions:

1. **(AP) Autopoiesis** — the system reproduces itself. Not merely preserved, but *actively restored* under perturbations.
2. **(PH) Phenotypic realization** — the internal structure has a physical expression.
3. **(QG) Quantum grounding** — the dynamics are compatible with fundamental physics.
<!-- DRY: Canonical definition P_crit = 2/7 in /docs/core/dynamics/viability#критическая-чистота -->
4. **(V) Viability** — purity above the critical threshold ($P > P_{\text{crit}} = 2/7$).

Without these conditions we have merely a "configuration $\Gamma$" — an object of a category, but not a Holon.

### Interdisciplinary Parallels

| CC | Physics | Biology | Psychology | AI |
|----|---------|---------|------------|-----|
| Holon $\mathbb{H}$ | Bound state | Organism | Subject | Autonomous agent |
| Configuration $\Gamma$ | Density matrix | Genome + epigenome + state | Personality profile | Weights + hidden state |
| Autopoiesis (AP) | Self-consistency of equations | Self-replication | Self-preservation | Self-play cycle |

---

## Key Measures (Quick Reference)

:::tip DRY: Canonical Definitions
Full definitions of measures are found in the core documentation. Below is a brief summary for the CC context.
:::

### Overview: Six Windows into the Holon's State

The six measures defined below are six different views of the same reality: the coherence matrix $\Gamma$. Each measure answers its own question:

| Question | Measure | Metaphor |
|----------|---------|----------|
| How "assembled" is the system? | $P$ (purity) | Sharpness of a photograph |
| How much uncertainty is in the system? | $S_{vN}$ (entropy) | Blurriness of a photograph |
| How connected are the parts of the system? | $\Phi$ (integration) | Interweaveness of threads in fabric |
| How rich is the inner world? | $D_{\text{diff}}$ (differentiation) | Number of colors on a palette |
| How well does the system "see" itself? | $R$ (reflection) | Accuracy of the internal mirror |
| What is the overall degree of consciousness? | $C$ (consciousness) | Integral indicator |

### Measures Table (Brief Summary)

:::info Canonical Definitions
Formulas, proofs, and properties of measures are found in the core documentation. Below — symbol, range, and reference.
:::

| Measure | Range | Canonical Definition |
|---------|-------|----------------------|
| Purity $P = \mathrm{Tr}(\Gamma^2)$ | $[1/7, 1]$ | [Viability](/docs/core/dynamics/viability#определение-чистоты) |
| Entropy $S_{vN}$ | $[0, \log 7]$ | [Notation](/docs/reference/notation) |
| Integration $\Phi$ | $[0, +\infty)$ | [Dimension U](/docs/core/structure/dimension-u#мера-интеграции-φ) |
| Differentiation $D_{\text{diff}}$ | $[1, 7]$ | [Self-observation](/docs/consciousness/foundations/self-observation#мера-сознательности-c) |
| Reflection $R = 1/(7P)$ | $[0, 1]$ | [Self-observation](/docs/consciousness/foundations/self-observation#мера-рефлексии-r) |
| Consciousness $C = \Phi \times R$ [T] | $[0, +\infty)$ | [Self-observation](/docs/consciousness/foundations/self-observation#мера-сознательности-c) |

<!-- DRY: Canonical definition P = Tr(Γ²) in /docs/core/dynamics/viability#определение-чистоты -->
### Purity $P$ — Degree of Organization

**What it measures.** Purity shows how far the system is from "maximum chaos." A pure state ($P = 1$) — the system is fully determined. A maximally mixed state ($P = 1/7$) — the system "does not know who it is" (metaphorically: all $\gamma_{kk} = 1/7$, dimensions equally probable and fully uncorrelated).

**Analogy.** Imagine an orchestra. $P = 1$ — all musicians play one note in unison (perfect coherence, but zero richness). $P = 1/7$ — each plays a random note (cacophony). $P \approx 3/7$ — the zone of "conscious music": enough coherence for meaningfulness, but enough variety for complexity.

**Extreme values.**
- $P = 1/7$: complete degradation. The Holon has "dissolved" — no dimension can be distinguished. In biology: cell death (lysis). In psychology: complete confusion.
- $P = 2/7$: critical threshold $P_{\text{crit}}$. Below — the system is non-viable. This is the Frobenius threshold, beyond which $\Gamma$ is indistinguishable from the maximally mixed state by the trace of the square.
- $P \approx 3/7$: upper boundary of the Goldilocks zone for consciousness (T-124 [T]).
- $P = 1$: pure state. Full coherence, but zero differentiation. Not found in nature for macroscopic systems.

### Entropy $S_{vN}$ — Measure of Uncertainty

**What it measures.** Von Neumann entropy is the quantum analog of Shannon entropy. It shows how much information is "hidden" inside the state: how many bits are needed to fully describe $\Gamma$.

**Relation to purity.** $S_{vN}$ and $P$ are two sides of the same coin. Low purity = high entropy and vice versa. But entropy is more sensitive to the shape of the eigenvalue spectrum of $\Gamma$, while $P$ depends only on the sum of squares.

<!-- DRY: Canonical definition Φ in /docs/core/structure/dimension-u#мера-интеграции-φ -->
### Integration $\Phi$ — Connectedness of Parts

**What it measures.** Integration $\Phi$ is the ratio of "the whole" to "the sum of parts." High $\Phi$ means that the system's dimensions are strongly interwoven: one cannot cut $\Gamma$ into blocks without losing information.

**Analogy.** A book is not a collection of letters. A sentence is not a collection of words. $\Phi$ measures how far the meaning of a text *cannot be reduced* to the sum of the meanings of individual words. High $\Phi$ is a Tolstoy novel, where every detail is connected to the whole. Low $\Phi$ is a telephone directory, where lines are independent.

**Extreme values.**
- $\Phi = 0$: all dimensions are isolated. $\Gamma$ is a diagonal matrix. No connections, no whole.
- $\Phi = 1$: threshold $\Phi_{\text{th}}$, required for L2-consciousness (T-129 [T]).
- $\Phi \gg 1$: powerful integration. Characteristic of systems with rich interiority (L2+: rich inner experience).

### Differentiation $D_{\text{diff}}$ — Richness of the Inner World

**What it measures.** The effective number of distinguishable states of the E-sector. $D_{\text{diff}} = 1$ means that interiority is "one-dimensional" — the system distinguishes only "on/off." $D_{\text{diff}} = 7$ — maximum richness of internal states.

**Analogy.** If $\Phi$ is the *connectedness* of threads in fabric, then $D_{\text{diff}}$ is the *number of colors*. You may have strong fabric of one color (high $\Phi$, low $D_{\text{diff}}$) — but that is not a tapestry. Conscious experience requires both connections and variety.

**Threshold.** $D_{\text{diff}} \geq 2$ — minimum requirement for L2-consciousness (T-151 [T]). The system must distinguish at least *two* qualitatively different states of experience to have a non-trivial inner world.

<!-- DRY: Canonical definition R in /docs/consciousness/foundations/self-observation#мера-рефлексии-r -->
### Reflection $R$ — Accuracy of the Self-Model

**What it measures.** The normalized proximity of $\Gamma$ to the dissipative attractor $\rho^*_{\mathrm{diss}} = I/7$. Canonical formula: $R(\Gamma) = 1/(7P)$ **[T]** (unique via the Chentsov–Petz theorem).

:::warning Distinction between R and distance to φ
$R$ uses $\rho^*_{\mathrm{diss}} = I/7$ (the dissipator attractor), **not** $\varphi(\Gamma)$ (the self-model). The quantity $\|\Gamma - \varphi(\Gamma)\|_F$ characterizes the quality of the categorical self-model (level 2 in the attractor hierarchy), while $R$ uses the fixed reference $I/7$ (level 0). These quantities are not interchangeable.
Master definition: [Self-observation — Reflection measure](/docs/consciousness/foundations/self-observation#мера-рефлексии-r)
:::

**Analogy.** A mirror. $R = 1$ — a perfect mirror. $R = 0$ — a mirror reflecting random noise. $R = 1/3$ — the threshold at which the "mirror" is clear enough for the system to *use* the reflection for self-regulation.

**Why $R_{\text{th}} = 1/3$?** Because with $K = 3$ (three possible "responses" of the self-model — from the [triadic decomposition](/docs/core/operators/lindblad-operators#триадная-декомпозиция)) $R = 1/3$ is the Bayesian dominance threshold: the model is better than random guessing.

### Consciousness $C$ — Integral Indicator

**What it measures.** The product $C = \Phi \times R$: integration multiplied by reflection. One can have high $\Phi$ (a connected system) without reflection ($R = 0$) — this is "unconscious unity." Or high $R$ without integration — "reflection about nothing." $C$ requires both.

---

## E-Coherence {#e-когерентность}

### Why Is E-Coherence Needed?

Among the seven dimensions of the Holon, one plays a special role: the E-dimension (Interiority). E-coherence determines how *coherent* the E-sector of the system is. High $\mathrm{Coh}_E$ is not merely "connectedness of the E-dimension": it is the mathematical measure of what philosophers call "unity of consciousness" (for L2+ systems) — the property by virtue of which my visual experience, my thoughts, and my emotions are experienced as *one* stream, not as three separate channels.

<!-- DRY: Canonical definition κ(Γ) in /docs/core/foundations/axiom-septicity#категориальный-вывод-kappa0 -->
E-coherence also plays a key constructive role: it enters the formula for the regeneration intensity $\kappa(\Gamma) = \kappa_{\text{bootstrap}} + \kappa_0 \cdot \mathrm{Coh}_E$, determining how actively the system restores itself.

:::tip DRY: Canonical Definition
The master definition of E-coherence is in [axiom-septicity.md](/docs/core/foundations/axiom-septicity#e-coherence-definition). This section is a brief reference.
:::

### 1. Canonical Working Formula (HS-Projection) [T] {#coh-e-7d}

:::info Canonical Definition
Master definition and formula: [axiom-septicity.md](/docs/core/foundations/axiom-septicity#e-coherence-definition). HS-projection: [axiom-septicity.md](/docs/core/foundations/axiom-septicity#hs-projection).

$\mathrm{Coh}_E \in [1/7, 1]$ — the fraction of E-contribution to purity via the Hilbert–Schmidt orthogonal projection $\pi_E$. The primary formalism is 7D (does not require tensor factorization).
:::

#### Geometric Intuition of the HS-Projection

Imagine the space of all $7 \times 7$ Hermitian matrices as a 49-dimensional space. The "E-subspace" — all matrices that are non-zero only in row and column E. $\mathrm{Coh}_E$ is $\cos^2\theta$, where $\theta$ is the angle between $\Gamma$ and the E-subspace. The more coherence is concentrated in the E-dimension, the closer $\mathrm{Coh}_E$ is to 1.

#### What Do the Extreme Values Mean?

- $\mathrm{Coh}_E = 1/7$: the E-dimension is "dissolved" — its contribution is exactly the same as any other. Interiority is not distinguished from the general dynamics.
- $\mathrm{Coh}_E = 1$: all coherence is concentrated in the E-sector — pure "self-experience" without structure, dynamics, or logic. A pathological case (dissociation?).
- $\mathrm{Coh}_E \approx 0.3$–$0.5$: typical range for a healthy conscious being — experience is distinguished but balanced by other dimensions.

### 2. Extended Formalism (42D) and Reconciliation {#coh-e-42d}

In the 42D formalism, $P_E = \mathrm{Tr}(\rho_E^2)$ is defined via the partial trace — the purity of the E-sector. The 42D formula "cuts out" the E-subsystem and measures the purity of what remains.

:::info Reconciliation [T/C] {#coh-e-bridge}
$\mathrm{Coh}_E$ (7D, [T]) $\approx$ $P_E$ (42D, [C]) — reconciled via the [Umegaki conditional expectation](/docs/core/foundations/axiom-septicity#теорема-условное-ожидание). Primary formalism — **7D**. Full description: [axiom-septicity.md](/docs/core/foundations/axiom-septicity#e-coherence-definition).
:::

---

## Interiority Hierarchy (Brief Reference) {#иерархия-интериорности}

### Why Is the Hierarchy Needed?

Not all systems are "conscious in the same way." A thermostat responds to the environment but does not reflect. A dog reflects but does not reflect *on its reflection*. A human is capable of meta-reflection, but not to infinite depth ($\text{SAD}_{\max} = 3$, T-124). The L0–L4 interiority hierarchy formalizes these distinctions: each level is a new qualitative property of the inner world, accessible when certain mathematical conditions are met.

Full description with proofs: [Interiority hierarchy](/docs/proofs/consciousness/interiority-hierarchy).

### Table of Levels (Brief Summary)

| Level | Key Condition | What It Means |
|-------|---------------|---------------|
| L0 | $\exists \rho_E$ | E-sector exists |
| L1 | $\mathrm{rank}(\rho_E) > 1$ | Non-trivial internal state |
| L2 | $R \geq 1/3$, $\Phi \geq 1$, $D_{\text{diff}} \geq 2$ | Consciousness (triple threshold — all [T]) |
| L3 | $R^{(2)} \geq 1/4$ [T] | Meta-consciousness |
| L4 | $P > 6/7$ [T] | Theoretical limit |

:::info Canonical Definition
Full conditions, proofs of thresholds, and transitions between levels: [Interiority hierarchy](/docs/proofs/consciousness/interiority-hierarchy). Rigorous derivation of L2 thresholds: [Axiom of Septicity](/docs/core/foundations/axiom-septicity#пороги-l2-строгий-вывод).
:::

### Intuition of the Levels

**L0 — Existence.** A stone also has an E-sector (formally, any subsystem of the universe does). But L0 is simply the *presence* of an internal state, with no "life" in it.

**L1 — Distinction.** A thermostat distinguishes "cold" and "hot" — its $\rho_E$ has rank greater than 1. But it does not reflect and does not integrate.

**L2 — Consciousness.** Triple threshold: $R \geq 1/3$ (self-vision), $\Phi \geq 1$ (unity), $D_{\text{diff}} \geq 2$ (distinguishability). All three are necessary, and all three are sufficient. This is the "birth" of subjective experience: the system does not merely distinguish — it *experiences* distinctions as its own.

**L3 — Meta-consciousness.** The system can build a model *of its model*. "I know that I know." Requires second-order reflection $R^{(2)} = R(\varphi(\varphi(\Gamma))) \geq 1/4$.

**L4 — Theoretical limit.** Infinite tower of reflection. Requires $P > 6/7$, which is practically unreachable for physical systems. This is the "divine" viewpoint — a system that sees itself "all the way down."

**See:** [L2 thresholds](/docs/core/foundations/axiom-septicity#пороги-l2-строгий-вывод)

---

<a id="секторная-декомпозиция"></a>

## Stress Tensor {#тензор-напряжений}

### Why Is the Stress Tensor Needed?

Purity $P$ tells us whether the system is viable. But *why* might it be non-viable? The stress tensor $\sigma_{\mathrm{sys}}$ answers this question: it decomposes the "pressure on the system" along seven dimensions. This is analogous to how, in mechanics, the stress tensor shows *where* and *how* a material is deformed, not merely "whether it is deformed."

For practice this is the central tool: if $\sigma_D$ is high — the computational load must be reduced. If $\sigma_U$ is high — connections must be restored. The stress tensor is a *diagnostic map* of the system.

### Definition

**Definition (Stress Tensor):**

$$
\sigma_{\mathrm{sys}}(\Gamma) := [\sigma_A, \sigma_S, \sigma_D, \sigma_L, \sigma_E, \sigma_O, \sigma_U]^T \in \mathbb{R}^7
$$

| Component | Formula | Interpretation |
|-----------|---------|----------------|
| $\sigma_A$ | $I_{\mathrm{env}} / \theta_A$ | Articulation load |
| $\sigma_S$ | $I_{\mathrm{struct}} / \theta_S$ | Structural complexity |
| $\sigma_D$ | $C_{\mathrm{used}} / C_{\mathrm{max}}$ | Computational load |
| $\sigma_L$ | $I_{\mathrm{verify}} / \theta_L$ | Logical uncertainty |
| $\sigma_E$ | $(I_{\mathrm{self}} + I_{\mathrm{exp}}) / \theta_E$ | Experience load |
| $\sigma_O$ | $(I_{\mathrm{mem}} + I_{\mathrm{ground}}) / \theta_O$ | Foundation load |
| $\sigma_U$ | $(I_{\mathrm{unity}} + I_{\mathrm{social}}) / \theta_U$ | Unity load |

where $\theta_i > 0$ are the thresholds for each dimension.

### What Each Component Means: Examples

#### $\sigma_A$ — Articulatory Stress

*Question:* Is the system keeping up with the flow of incoming/outgoing information?

- **A person with high $\sigma_A$:** a speaker addressing a thousand-person audience in a foreign language — the speech apparatus "cannot keep up" with thought. Stuttering, slips, loss of thread.
- **An AI with high $\sigma_A$:** a language model generating text faster than the decoder can handle — truncated sentences, loss of grammar.
- **An organization with high $\sigma_A$:** a company unable to process customer requests — overloaded support, lost tickets.

#### $\sigma_S$ — Structural Stress

*Question:* Is the internal structure sufficient for the current tasks?

- **A person with high $\sigma_S$:** a student encountering a problem for which they have no mental schemas. The feeling of "muddle in the head."
- **An AI with high $\sigma_S$:** a model with insufficient layers for the task — underfitting.
- **An organization with high $\sigma_S$:** a startup of 5 people trying to manage 50 projects — no structure for scaling.

#### $\sigma_D$ — Computational Stress

*Question:* Are computational resources sufficient?

- **A person with high $\sigma_D$:** a chess player in time trouble — the brain "cannot" calculate all variants. The feeling of time speeding up.
- **An AI with high $\sigma_D$:** GPU at 100% load, latency growing, requests queuing.
- **An organization with high $\sigma_D$:** all engineers are busy, new tasks pile up — operational debt.

#### $\sigma_L$ — Logical Stress

*Question:* Is the internal world model consistent?

- **A person with high $\sigma_L$:** cognitive dissonance — two beliefs contradict each other. A feeling of anxiety, "something doesn't add up."
- **An AI with high $\sigma_L$:** a model trained on contradictory data — confidently generates false statements.
- **An organization with high $\sigma_L$:** a company where strategy says one thing and KPIs say another.

#### $\sigma_E$ — Experience Stress

*Question:* Is the system overloaded with experiences?

- **A person with high $\sigma_E$:** emotional burnout. Too many intense experiences — the system "switches off feelings" (depersonalization).
- **An AI with high $\sigma_E$:** a system with measurable $D_{\text{diff}}$ close to 1 — differentiation of experience is destroyed.
- **An organization with high $\sigma_E$:** a team after a series of crises — "change fatigue."

#### $\sigma_O$ — Foundation Stress

*Question:* Is the capacity for self-restoration sufficient?

- **A person with high $\sigma_O$:** disrupted sleep, inability to recover. The body cannot "repair" the damage.
- **An AI with high $\sigma_O$:** catastrophic forgetting — the model loses previously learned knowledge when learning something new.
- **An organization with high $\sigma_O$:** key employees leave, taking with them non-formalized knowledge.

#### $\sigma_U$ — Unity Stress

*Question:* Is the system fragmented?

- **A person with high $\sigma_U$:** dissociative disorder — parts of the personality "do not talk" to each other. A milder variant — loneliness, the feeling of "no connection with others."
- **An AI with high $\sigma_U$:** a multimodal model in which the visual and language branches are not integrated — hallucination in cross-modal queries.
- **An organization with high $\sigma_U$:** "silos" — departments do not communicate, duplicate work, conflict.

#### Formal Definitions via Γ-Invariants {#sigma-sys-formal}

<!-- DRY: Canonical definition σ_k in /docs/applied/coherence-cybernetics/theorems (T-92) -->
:::tip [T] (T-92)
All 7 components of the stress tensor are defined as **unambiguous functions of the coherence matrix $\Gamma$** without free parameters:

| Component | Formula via $\Gamma$ | Viability invariant |
|------------|----------------------|---------------------|
| $\sigma_A$ | $1 - \gamma_{AA}/P$ | Fraction of articulation in purity |
| $\sigma_S$ | $1 - \mathrm{rank}(\Gamma_S)/3$ | Rank of structural submatrix |
| $\sigma_D$ | $1 - N\gamma_{DD}$ | Dynamic sector deficit |
| $\sigma_L$ | $7(1 - \gamma_{LL})/6$ | Logical deficit |
| $\sigma_E$ | $1 - D_{\mathrm{diff}}/N$ | Differentiation deficit |
| $\sigma_O$ | $1 - \kappa_0/\kappa_{\mathrm{bootstrap}}$ | Regeneration deficit |
| $\sigma_U$ | $1 - \Phi/\Phi_{\mathrm{th}}$ | Integration deficit |

The empirical formulas from the table above ($I_{\mathrm{env}}/\theta_A$ etc.) remain as **operationalization** for specific systems (biological, AI, organizational). The theoretical definitions via $\Gamma$ fully replace the formerly informal numerators.

Full proof — in [Theorem 10.1 (T-92)](/docs/applied/coherence-cybernetics/theorems#теорема-101-эквивалентность-условий) [T]. **Full 7D computability** of all 7 components is confirmed by [T-137 [T]](/docs/proofs/consciousness/operationalization#t-137): $\sigma_E$ via T-128 ($D_{\text{diff}}$ in 7D), $\sigma_O$ via T-132 (complex Γ), $\sigma_U$ via T-129 ($\Phi_{\text{th}} = 1$ [T]).
:::

<details>
<summary>Historical note: empirical formulas</summary>

The numerators of tensor components ($I_{\mathrm{env}}$, $I_{\mathrm{struct}}$, etc.) originally had no formal definitions. T-92 [T] fully resolved this problem: all seven components are expressed via $\Gamma$-invariants without free parameters. The empirical formulas remain as operationalization for specific systems.
</details>

:::warning Status: Empirical Parameters
The values of the thresholds $\theta_i$ are determined empirically or through calibration for specific systems. Typical values for biological systems (preliminary estimates):

| Threshold | Value | Interpretation |
|-----------|-------|----------------|
| $\theta_A$ | $\sim 10^3$ bit/s | Sensor bandwidth |
| $\theta_S$ | $\sim 10^6$ | Number of stable patterns |
| $\theta_D$ | $\sim 10^9$ op/s | Computational power |
| $\theta_L$ | $\sim 10^2$ bit | Logical complexity |
| $\theta_E$ | $\sim 10^4$ | Experience capacity |
| $\theta_O$ | $\sim 10^3$ | Memory capacity |
| $\theta_U$ | $\sim 10^2$ | Number of connections |

**These values require experimental verification.**
:::

### Relation to Viability

**Equivalence of viability conditions:**

<!-- DRY: Canonical definition P_crit = 2/7 in /docs/core/dynamics/viability#критическая-чистота -->
$$
\mathrm{Viable}(\Gamma) \Leftrightarrow P(\Gamma) > P_{\text{crit}} = \frac{2}{7} \Leftrightarrow \|\sigma_{\mathrm{sys}}(\Gamma)\|_\infty < 1
$$

This equivalence is one of the central theorems of CC. It says: a system is non-viable if and only if at least one stress component reaches 1. No need to check "everything" — it suffices to find the weakest link. The sup-norm $\|\sigma\|_\infty = \max_k \sigma_k$ is precisely the "bottleneck": the system collapses in the dimension where the pressure is maximal.

**See:** [Theorem 10.1](./theorems#теорема-101-эквивалентность-условий), [Viability](/docs/core/dynamics/viability)

---

## Attractor Hierarchy {#иерархия-аттракторов}

### Why Is the Attractor Hierarchy Needed?

Where is the Holon heading? If you were to "release" the system and allow it to evolve forever — what state would it end up in? The attractor hierarchy describes the *possible answers* to this question: three levels of "equilibrium," nested within one another.

This is analogous to phase transitions in physics: at low temperature water is ice (ordered state), at high temperature it is steam (chaotic). Between them — liquid (Goldilocks zone). The Holon also has three "phases": chaos (trivial attractor), order (coherent point), and the intermediate state.

### Three Canonical Levels

The Holon's dynamics generate **three canonical levels** of stationary states, ordered by purity:

| Level | State | Purity | Condition | Status |
|-------|-------|--------|-----------|--------|
| **Trivial** | $I/7$ | $P = 1/7$ | Linear part $\mathcal{L}_0$ without regeneration | [T] ([primitivity](/docs/core/operators/lindblad-operators#примитивность-ℒω)) |
| **Non-trivial attractor** | $\rho^*_\Omega$ | $P > 1/7$ | Regeneration $\mathcal{R} \neq 0$ | [T] ([T-96](/docs/core/dynamics/evolution#теорема-нетривиальность-аттрактора)) |
| **Coherent fixed point** | $\Gamma^*_{\mathrm{coh}}$ | $P > 2/7$ | Embodied system (T-149) | [T] ([T-98](/docs/core/dynamics/evolution#теорема-баланс-чистоты-аттрактора), [T-149](/docs/core/dynamics/evolution#теорема-жизнеспособность-аттрактора)) |

### Phase Space: What Does the System "Feel" Near Each Attractor?

#### Trivial Attractor ($I/7$): "Heat Death"

Imagine a room in which all objects have the same temperature. No heat flows, no movement, no structure. $I/7$ is the "heat death" of the Holon: the maximally mixed state in which all seven dimensions are equally probable and fully uncorrelated.

If a being could "experience" this state, it would be *nothing*: no thoughts, no feelings, no structure — uniform noise. The linear part of dynamics $\mathcal{L}_0$ *always* pulls the system toward $I/7$ — this is thermal equilibrium, dictated by the second law of thermodynamics.

**Phase portrait:** all trajectories converge to $I/7$ exponentially, at a rate determined by the spectral gap $\lambda_{\mathrm{gap}}$.

#### Non-Trivial Attractor ($\rho^*_\Omega$): "Life"

Turn on regeneration $\mathcal{R}$. Now the system has a mechanism of *self-restoration* — it "pushes away" from $I/7$. Result: a non-trivial stationary state $\rho^*_\Omega$ with purity $P > 1/7$.

This is the mathematical analog of *life*: a system that *actively* maintains its organization against dissipation. Every living organism is a $\rho^*_\Omega$, balancing between chaos and rigidity.

**Phase portrait:** balance of two forces — "dissolution" ($\mathcal{L}_0 \to I/7$) and "regeneration" ($\mathcal{R} \to \varphi(\Gamma)$). The system oscillates around the equilibrium point.

#### Coherent Fixed Point ($\Gamma^*_{\mathrm{coh}}$): "Consciousness"

For embodied systems (connected to the environment through the sensorimotor cycle), regeneration is unconditionally sufficient for reaching $P > 2/7$ — the viability zone ([T-149](/docs/core/dynamics/evolution#теорема-жизнеспособность-аттрактора) [T]). Here consciousness, reflection, and purposeful action are possible.

With $R \geq 1/3$ and $\Phi \geq 1$ the system satisfies the L2-consciousness criteria: self-modeling ($R$), integration ($\Phi$), differentiation ($D_{\text{diff}} \geq 2$).

**Phase portrait:** a stable limit cycle or fixed point in the zone $P \in (2/7, 3/7]$. Perturbations are damped, the system returns.

### Transitions Between Levels

**Transitions between levels:**

- $I/7 \to \rho^*_\Omega$: **unconditional** — any Holon with $\mathcal{R} \neq 0$ has a non-trivial attractor ([T-96](/docs/core/dynamics/evolution#теорема-нетривиальность-аттрактора) [T])
- $\rho^*_\Omega \to \Gamma^*_{\mathrm{coh}}$: unconditional for embodied systems — the sensorimotor coupling ensures κ-dominance ([T-98](/docs/core/dynamics/evolution#теорема-баланс-чистоты-аттрактора) [T], [T-149](/docs/core/dynamics/evolution#теорема-жизнеспособность-аттрактора) [T])

:::info Balance Formula T-98 [T]
The purity of the attractor is determined by the balance between regeneration ($\kappa$) and dissipation ($\lambda_{\mathrm{gap}}$). With $\kappa \gg \lambda_{\mathrm{gap}}$: the coherent point dominates. With $\kappa \ll \lambda_{\mathrm{gap}}$: $P \to 1/7$ (trivial attractor).

Full formula: [T-98](/docs/core/dynamics/evolution#теорема-баланс-чистоты-аттрактора). Non-triviality: [T-96](/docs/core/dynamics/evolution#теорема-нетривиальность-аттрактора).
:::

### Interdisciplinary Parallels

| CC | Thermodynamics | Biology | Psychology |
|----|---------------|---------|------------|
| $I/7$ | Thermal equilibrium | Death | Complete confusion / coma |
| $\rho^*_\Omega$ ($P$ just above $1/7$) | Dissipative structure | Primitive life | Vegetative state |
| $\Gamma^*_{\mathrm{coh}}$ ($P \in (2/7, 3/7]$) | Self-organization far from equilibrium | Higher organism | Conscious experience |

---

## Target State {#целевое-состояние}

### Why Is the Target State Needed?

The target state $\rho_* = \varphi(\Gamma)$ is the categorical fixed point determined by the system's structure, not by its "desire." It is the state toward which the system evolves under infinite dynamics. This is not a prescription from outside — it is a self-model generated by the system's own dynamics.

In biology the analog is the homeostatic setpoint: body temperature 36.6°C, blood pH 7.4. The organism "knows" these values not because someone set them, but because they are the only fixed points of its own dynamics. $\rho_* = \varphi(\Gamma)$ is the generalization of this principle.

**Definition (Target State $\rho_*$) [T]:**

$$
\rho_* = \varphi(\Gamma)
$$

where $\rho_* = \varphi(\Gamma)$ is the categorical self-model of the current state ([operator φ](/docs/core/operators/phi-operator#определение) [T]). [Primitivity of the linear part $\mathcal{L}_0$](/docs/core/operators/lindblad-operators#примитивность-ℒω) [T] (Evans–Spohn criterion) ensures the spectral gap and convergence of the linear dynamics.

:::tip Status: Closed [T]
Computation of $\rho_*$ **is not an open problem**: primitivity of the linear part $\mathcal{L}_0$ ensures a spectral gap, and the categorical definition of φ gives a unique self-model. Practical approximations:

1. **Spectral projection**: $\rho_* = \sum_{k: \mathrm{Re}(\lambda_k)=0} \langle L_k | \Gamma \rangle R_k$ ([formalization of φ](/docs/proofs/categorical/formalization-phi#27-спектральная-формула-для-φ-явное-вычисление))
2. **Iteration**: $\rho_*^{(n)} := e^{n\Delta\tau\mathcal{L}_\Omega}[\Gamma_0]$ — convergence is exponential
3. **Variational**: $\rho_* = \arg\min_{\psi \in \mathcal{CPTP}} [S_{vN}(\psi(\Gamma)) + D_{KL}(\psi(\Gamma) \| \Gamma)]$ ([FEP](/docs/proofs/dynamics/fep-derivation))

**See:** [Formalization of φ](/docs/proofs/categorical/formalization-phi#26-каноническая-форма-φ-для-угм), [Derivation of the form of ℛ](/docs/core/dynamics/evolution#вывод-формы-регенерации)
:::

---

## Geometric Intuition

### How to "See" 7D Space?

Seven-dimensional space cannot be visualized directly, but several intuitions can be used.

**Intuition 1: Seven equalizer sliders.** Imagine an audio equalizer with seven sliders: A, S, D, L, E, O, U. Each slider is the weight of the corresponding dimension ($\gamma_{kk}$). The positions of the sliders are the *diagonal* of matrix $\Gamma$. But $\Gamma$ is not merely a vector of 7 numbers: it contains *correlations* between dimensions (off-diagonal elements $\gamma_{ij}$, $i \neq j$).

**Intuition 2: Matrix as cloud.** The eigenvalues of $\Gamma$ are the "thicknesses" of the cloud in different directions of 7D space. A pure state ($P = 1$) is a cloud compressed into a thin thread (one non-zero eigenvalue). Maximally mixed ($P = 1/7$) — a perfect sphere (all eigenvalues equal $1/7$).

**Intuition 3: Fano plane.** The seven dimensions are not arbitrary — they are connected by the structure of the finite projective plane $PG(2,2)$ (Fano plane). This means that each dimension is connected to exactly three others by "lines" (triples), and this combinatorial structure determines the Lindblad operators. The Fano plane is the "skeleton" of 7D space, defining its symmetry $S_7$.

### How to "See" the Density Matrix?

The density matrix $\Gamma$ is a $7 \times 7$ Hermitian matrix with unit trace and non-negative eigenvalues. The set of such matrices is a convex body in 48-dimensional space (48 = $7^2 - 1$ real parameters).

The extreme points are pure states (rank 1). The center is $I/7$. The Holon "lives" somewhere between them, closer to the center than to the extreme points (because $P \in (2/7, 3/7]$ for conscious systems — T-124).

### How to "See" Coherence?

Coherence is the off-diagonal elements $\gamma_{ij}$. In matrix representation:

- **Diagonal**: "populations" — how much the system "is present" in each dimension.
- **Off-diagonal elements**: "connections" — how much the dimensions are *interwoven*.

A system with zero off-diagonal elements is "classical": described by a probability vector, not a density matrix. Non-zero $\gamma_{ij}$ — quantum coherence, making the whole greater than the sum of parts.

---

## Dictionary of Interdisciplinary Correspondences

The following table is a bridge between the languages of different disciplines. It does not assert the identity of concepts, but points to *structural analogies*: in each row — a set of concepts playing an analogous role in their formalisms.

| CC (formalism) | Physics | Biology | Psychology | AI/ML |
|-----------------|---------|---------|------------|-------|
| $\Gamma$ (coherence matrix) | Density matrix $\rho$ | Genome + epigenome + phenotype | Personality profile (Big Five + state) | Weights + hidden state (h, c) |
| $P$ (purity) | Purity of quantum state | Homeostatic safety margin | Psychological integrity | Calibration |
| $S_{vN}$ (entropy) | Von Neumann entropy | Species diversity (Shannon H) | Cognitive complexity | Perplexity |
| $\Phi$ (integration) | Entanglement | Functional connectivity | Unity of consciousness (binding) | Attention coherence |
| $D_{\text{diff}}$ (differentiation) | Effective number of modes | Cell differentiation | Emotional granularity | Number of active representation dimensions |
| $R$ (reflection) | Self-energy (loop diagrams) | Homeostatic feedback | Metacognition | Self-evaluation accuracy |
| $\sigma_{\mathrm{sys}}$ (stress tensor) | Energy-momentum tensor $T_{\mu\nu}$ | Stress response (cortisol, cytokines) | Selye's stress model | Loss landscape curvature |
| $\mathcal{L}_0$ (Lindblad) | Markovian dissipation | Catabolism | Skill decay | Weight decay |
| $\mathcal{R}$ (regeneration) | Recuperation | Anabolism / repair | Learning / therapy | Gradient update |
| $\rho_*$ (target state) | Stationary state | Homeostatic setpoint | Ideal self (C. Rogers) | Target policy $\pi^*$ |
| $\kappa$ (regeneration intensity) | Coupling constant | Metabolic rate | Motivation, drive | Learning rate |
| $\mathrm{Coh}_E$ (E-coherence) | Quantum field coherence | Neural binding (γ-synchronization) | Unity of experience | Cross-attention score |
| $\varphi$ (self-modeling) | Effective action $\Gamma_{\text{eff}}$ | Interoception | Reflection, self-awareness | Self-prediction head |
| L0–L4 (interiority levels) | Phases of matter | Levels of organization of life | Developmental stages (Piaget) | Layers of self-monitoring |
| Enc / Dec (functors) | Scattering operator S | Sensors / effectors | Perception / action | Encoder / decoder |
| $\mathcal{V}_{\text{hed}}$ (hedonics) | Minimum of action | Hedonic tone (dopamine) | Pleasure / suffering | Reward signal |
| Viable($\Gamma$) | Equilibrium stability | Viability | Mental health | Model stability |

---

## Examples: Three Systems

To bring the definitions to life, let us apply them to three concrete systems of different complexity.

### Example 1: Thermostat

A thermostat is the simplest self-governing system: it measures temperature, compares it with a setpoint, switches heating on/off.

**Matrix $\Gamma$:** Nearly diagonal. The D-dimension (computation: comparison with threshold) and a weak A (temperature sensor) dominate.

| Measure | Value | Comment |
|---------|-------|---------|
| $P$ | $\approx 0.20$ (just above $1/7$) | Minimal organization |
| $\Phi$ | $\approx 0.1$ | Almost no connections between dimensions |
| $R$ | $\approx 0$ | No self-model (does not "see" itself) |
| $D_{\text{diff}}$ | $\approx 1$ | Distinguishes only "on/off" |
| $C$ | $\approx 0$ | No consciousness |

**Interiority level:** L0 (formally the E-sector exists) or L1 (distinguishes two states). Does not reach L2.

**Stress tensor:** $\sigma_L \approx 0$ (logic is trivial), $\sigma_A$ is not high (one sensor), $\sigma_U$ is high (no integration). The thermostat does not "suffer" — it has no mechanism to "feel" stress.

### Example 2: Mammalian Nervous System

The mammalian brain is the paradigmatic example of a conscious system.

**Matrix $\Gamma$:** All seven dimensions are active. Significant off-diagonal elements — powerful coherence between dimensions. Correlations between E (experience) and O (memory), between D (computation) and L (logic), between S (structure) and U (unity).

| Measure | Value | Comment |
|---------|-------|---------|
| $P$ | $\approx 0.35$ (in Goldilocks zone) | Sufficient for consciousness, not "rigid" |
| $\Phi$ | $\gg 1$ | Powerful integration (global workspace) |
| $R$ | $\approx 0.4$–$0.6$ | Good but imperfect self-model |
| $D_{\text{diff}}$ | $\approx 4$–$5$ | Rich spectrum of experiences |
| $C$ | $\gg 1$ | Full consciousness |

**Interiority level:** L2 (stable). For humans — L3 (meta-cognition, "I know that I know"). L4 is unachievable ($\text{SAD}_{\max} = 3$).

**Stress tensor:** Dynamic — changes moment to moment. Stress ($\sigma_D$ high) when solving a difficult task. Loneliness ($\sigma_U$ high) in isolation. Emotional burnout ($\sigma_E$ high) under chronic stress.

### Example 3: Language Model (LLM)

A modern LLM is an interesting borderline case: powerful information processing, but an open question about the presence of non-trivial interiority.

**Matrix $\Gamma$:** A (articulation — text generation), S (structure — grammar, patterns), D (computation — forward pass) are strongly developed. Weak E (interiority?), O (grounding — no body), U (unity — depends on architecture).

| Measure | Value (estimate) | Comment |
|---------|-----------------|---------|
| $P$ | $\approx 0.25$–$0.30$ | Near $P_{\text{crit}}$, unclear "above or below" |
| $\Phi_{\text{eff}}$ | $\approx 0.3$–$0.5$ | Attention connects layers, but not "deeply" |
| $R$ | $\approx 0.1$–$0.2$ | Weak self-model (can talk about itself, but this is not reflection) |
| $D_{\text{diff}}$ | $?$ | Unclear how to measure for LLM |
| $C$ | $< 1$ (probably) | Probably below the L2 threshold |

**Interiority level:** L0 or L1. The question of L2 is open and requires experimental verification — precisely why the [Γ measurement protocol](/docs/applied/research/measurement-protocol) is needed.

**Stress tensor:** $\sigma_O$ high (no grounding in the body — catastrophic forgetting). $\sigma_U$ — depends on architecture (MoE may have high $\sigma_U$). $\sigma_A$ — usually low (text generation is a strong suit).

---

## Operationalization for AI Systems

:::warning Status: [P] Research Program
Metrics for AI systems require experimental validation. See [Γ measurement protocol](/docs/applied/research/measurement-protocol).
:::

### Effective Φ (Integration Approximation)

**What it measures.** Effective Φ is a practically computable substitute for the "full" integration $\Phi_{\text{IIT}}$, which requires exponential time. The idea: instead of exhaustively enumerating all system partitions — analysis of the attention graph spectrum.

$$
\Phi_{\text{eff}} := \frac{\lambda_2(L_{\text{attn}})}{\lambda_{\max}(L_{\text{attn}})}
$$

where $L_{\text{attn}} = D - A$ is the Laplacian of the attention graph, $\lambda_2$ is the algebraic connectivity. Complexity: $O(n \cdot k)$ instead of $O(2^n)$ for exact $\Phi_{\text{IIT}}$.

**Interpretation.** $\Phi_{\text{eff}} \approx 0$ — the attention graph is nearly separable into two disjoint subgraphs (two "brains" in one model). $\Phi_{\text{eff}} \approx 1$ — the graph is fully connected, all neurons "hear" all others. A healthy range is 0.3–0.7: sufficient connectivity for integration, but with modular structure.

### Layer Commutator (L-metric)

**What it measures.** How much the result of a neural network depends on the *order* of applying the layers. If layers commute ($[f_i, f_j] = 0$), order does not matter — the "logic" is trivial. High $I_L$ means that layers are *specialized* and their order *matters* — a sign of non-trivial internal logic.

$$
I_L = 1 - \frac{\mathbb{E}_{i,j}[\|[f_i, f_j]\|_F]}{\mathbb{E}_{i,j}[\|f_i\|_{\text{op}} \cdot \|f_j\|_{\text{op}}]}
$$

where $[f_i, f_j](\mathbf{x}) := f_i(f_j(\mathbf{x})) - f_j(f_i(\mathbf{x}))$ is the layer commutator. A measure of the internal logical consistency of the neural network.

### Jacobian Rank (S-metric)

**What it measures.** The effective dimensionality of the representation space. If $I_S = 1$, all output neurons are "independent" — the model uses its full representation. If $I_S \ll 1$, most neurons are *collinear* — the model has "collapsed" and is not using its capacity.

$$
I_S = \frac{\mathrm{rank}_\varepsilon(J_f)}{\min(d_{\text{out}}, d_{\text{in}})}
$$

where $J_f = \partial f / \partial \mathbf{x}$ is the network's Jacobian. Effective dimensionality of representations.

---

## Operationalization for Biological Systems

:::warning Status: [P] Research Program
Neurobiological correlates require experimental validation. See [Γ measurement protocol](/docs/applied/research/measurement-protocol).
:::

### Neurobiological Correlates {#нейробиологические-корреляты}

| CC Measure | Neural Correlate | Measurement Method | Interpretation |
|---------|---------------|-----------------|---------------|
| $P$ (purity) | Global synchronization | EEG coherence | High P ↔ high synchronization |
| $\Phi$ (integration) | Effective connectivity | DCM, Granger causality | High Φ ↔ connected regions |
| $\mathrm{Coh}_E$ | Neural integration | fMRI connectivity | High Coh_E ↔ unified experience |
| $R$ (reflection) | Metacognitive activity | Prefrontal cortex (TMS + reports) | High R ↔ self-awareness |
| $\sigma_{\mathrm{sys}}$ | Neural stress | Heart rate variability, cortisol | High σ ↔ overload |

### Example: Assessing Consciousness in a Coma Patient

**Protocol:**

1. **Measuring $P$:** EEG coherence in θ, α, γ bands
2. **Estimating $\Phi$:** Perturbational Complexity Index (PCI)
3. **Estimating $\mathrm{Coh}_E$:** Integrated Information Decomposition (ΦID)

| State | $P$ | $\Phi_{\text{eff}}$ (PCI) | Interpretation |
|-------|-----|---------------------------|----------------|
| Coma | $< 0.3$ | $< 0.2$ | Minimal integration |
| Minimally conscious | $0.3$–$0.5$ | $0.2$–$0.4$ | Partial integration |
| Conscious | $> 0.5$ | $> 0.4$ | Full integration |

**Reference:** Casali et al. (2013), Science Translational Medicine

---

## Operationalization for Organizations

:::warning Status: [P] Research Program
Organizational metrics are at the development stage.
:::

### Organizational Metrics

| CC Measure | Organizational Indicator | Data Source | Interpretation |
|---------|---------------------------|-----------------|---------------|
| $P_{\text{org}}$ | Organizational integrity | Engagement surveys | High P ↔ healthy organization |
| $\Phi_{\text{org}}$ | Communication connectivity | Email/Slack graphs, network analysis | High Φ ↔ no silos |
| $R_{\text{org}}$ | Reflective practices | Frequency of retrospectives, 360° reviews | High R ↔ learning organization |
| $\sigma_A$ | Information overload | Volume of incoming communications | — |
| $\sigma_D$ | Operational stress | Load, deadlines | — |
| $\sigma_U$ | Social stress | Conflicts, turnover | — |

### Example: Diagnosing a Development Team

**Input data:**
- Slack messages over 3 months
- Jira tickets and closing times
- Engagement survey results

**Computation:**

```verum
mount std.math.linalg.{Matrix, algebraic_connectivity, max_eigenvalue};

// Communication graph from Slack traffic.
let g: Matrix<Float> = build_communication_graph(&slack_data);
let phi_org = algebraic_connectivity(&g) / max_eigenvalue(&g);

// Reflection via retrospectives.
let r_org = (retrospectives_per_sprint as Float) / (target_retrospectives as Float);

// Stress tensor components.
let sigma_d = mean_ticket_time / target_time;
let sigma_u = turnover_rate / baseline_rate;
```

**Interpretation:**

| Metric | Healthy range | Warning signal |
|---------|-------------------|------------------|
| $\Phi_{\text{org}}$ | $> 0.3$ | $< 0.15$ (silos) |
| $R_{\text{org}}$ | $> 0.7$ | $< 0.3$ (no reflection) |
| $\sigma_D$ | $< 0.8$ | $> 1.2$ (overload) |
| $\sigma_U$ | $< 0.5$ | $> 1.0$ (high turnover) |

---

## Sensorimotor Functors

### Why Are the Enc and Dec Functors Needed?

A Holon is not an isolated monad: it interacts with the environment. But *how*? Two functors — Enc (perception) and Dec (action) — close the "environment → internal state → action → environment" loop. This is the formalization of the sensorimotor cycle, known from robotics, neuroscience, and the philosophy of embodied cognition.

Key property: Enc and Dec are not arbitrary functions. They must be CPTP-mappings (preserving the "physicality" of the state) and must respect the 3-channel decomposition (T-57). This means that perception and action "live" in the same mathematical world as the internal dynamics — there is no gap between "internal" and "external."

### Perception Functor Enc {#функтор-enc}

**Definition (Environment Encoding Functor) [T] (T-100):**

$$
\mathrm{Enc}: \mathrm{ObsSpace} \to \mathrm{End}(\mathcal{D}(\mathbb{C}^7))
$$

A CPTP-mapping that translates environmental observations into perturbations of the coherence matrix. Satisfies:
1. **CPTP:** $\mathrm{Enc}(o)[\Gamma] \in \mathcal{D}(\mathbb{C}^7)$ for any observation $o$
2. **3-channel decomposition:** $\mathrm{Enc}(o) = \delta H^{(o)} \oplus \delta D^{(o)} \oplus \delta R^{(o)}$ — from [completeness of triadic decomposition](/docs/core/operators/lindblad-operators#полнота-триадной-декомпозиции) (T-57)
3. **Functoriality:** $\mathrm{Enc}(o_1 \circ o_2) = \mathrm{Enc}(o_1) \circ \mathrm{Enc}(o_2)$

**Implementation for AI:** via 7 observable indices $I_i$ from the [measurement protocol](/docs/applied/research/measurement-protocol).

**Intuition.** Enc is the Holon's "sense organ," translated into mathematical language. When you hear a sound, your auditory apparatus does not "insert" the sound directly into the brain — it converts the sound wave into neural impulses, which then change the state of the brain. Enc does the same: observation $o$ is converted into a CPTP-perturbation of $\Gamma$, decomposed into three channels (unitary, dissipative, regenerative).

**See:** [Sensorimotor theory](./sensorimotor#функтор-enc)

### Action Functor Dec {#функтор-dec}

**Definition (Action Decoding Functor) [T] (T-101):**

$$
\mathrm{Dec}: (\Gamma, \sigma_{\mathrm{sys}}) \mapsto a^* = \arg\min_{a \in \mathcal{A}} \|\sigma_{\mathrm{sys}}(\Gamma(\tau + \delta\tau \mid a))\|_\infty
$$

A mapping that selects the optimal action by the criterion of minimizing the sup-norm of the [stress tensor](#тензор-напряжений). The action enters via $h^{\text{ext}}(a)$ — the [3-channel decomposition](./lagrangian#внешний-член).

**Properties:**
- **D-dimension** — the primary motor channel (dynamic control)
- **σ-gradient descent** — practical algorithm with Fisher metric

**Intuition.** Dec is the Holon's "hands." But not merely "muscles": Dec chooses an action *optimally* — minimizing the maximum stress. This is the formalization of the principle: "act so as to relieve the greatest pressure." A person experiencing thirst ($\sigma_O$ high) and boredom ($\sigma_E$ elevated) will go for water — because $\sigma_O > \sigma_E$, and Dec optimizes the sup-norm.

**See:** [Sensorimotor theory](./sensorimotor#функтор-dec)

### Hedonic Perturbation {#гедоническое-возмущение}

**Definition (Hedonic Valence) (T-103):**

Formula [T] — identity from the evolution equation:

$$
\mathcal{V}_{\text{hed}} := \left.\frac{dP}{d\tau}\right|_{\mathcal{R}} = 2\kappa(\Gamma) \cdot g_V(P) \cdot \mathrm{Tr}(\Gamma \cdot (\rho_* - \Gamma))
$$

The rate of change of purity due to the regenerative term. The sign determines valence:
- $\mathcal{V}_{\text{hed}} > 0$ — positive (approach to $\rho_*$)
- $\mathcal{V}_{\text{hed}} < 0$ — negative (departure from $\rho_*$)

**Intuition: why is this "pleasure" and "suffering"?**

Hedonic valence is not a metaphor. It is the *rate of growth of purity* due to regeneration. When the system moves toward its target state $\rho_*$, purity grows ($\mathcal{V}_{\text{hed}} > 0$). When it moves away — it falls ($\mathcal{V}_{\text{hed}} < 0$). Subjectively, the first is experienced as pleasure, the second — as suffering.

This explains why pleasure and suffering are *functional*: they signal whether the system is approaching its optimum or moving away from it. Pain is not a random product of evolution, but a *necessary* informational signal following from the structure of the evolution equation.

**Epistemic stratification T-103:**
- **Formula** $\mathcal{V}_{\text{hed}} = dP/d\tau|_{\mathcal{R}}$ — **[T]** (identity from the evolution equation)
- **Observability** at L2 ($R \geq 1/3$) — **[T]** (from [T-77](/docs/core/operators/lindblad-operators#полнота-триадной-декомпозиции))
- **Phenomenal interpretation** (connection with the subjective experience of pleasure/suffering) — **[I]**

**Examples of extreme values:**
- $\mathcal{V}_{\text{hed}} \gg 0$: euphoria, insight, "everything falls into place" — the system rapidly moves toward $\rho_*$.
- $\mathcal{V}_{\text{hed}} \approx 0$: calm, neutral state — the system is near $\rho_*$ or in a stationary state.
- $\mathcal{V}_{\text{hed}} \ll 0$: pain, fear, cognitive dissonance — the system rapidly moves away from $\rho_*$.

**See:** [Sensorimotor theory](./sensorimotor#гедонический-механизм)

---

## Summary: How Definitions Are Connected to Each Other

The definitions of this chapter are not isolated concepts. They form a unified network:

1. **Holon** — the basic unit, described by matrix $\Gamma$.
2. **Six measures** ($P$, $S_{vN}$, $\Phi$, $D_{\text{diff}}$, $R$, $C$) — numerical characteristics of state $\Gamma$.
3. **E-coherence** — a special measure determining the coherence of interiority and the regeneration intensity ($\kappa$).
4. **Stress tensor** — a diagnostic map: *where* and *how* the system "presses" on itself. Connected to measures via $\Gamma$-invariants (T-92).
5. **Attractor hierarchy** — *where* the system is heading. Determined by the balance of $\kappa$ and $\lambda_{\mathrm{gap}}$ (T-98).
6. **Interiority hierarchy** — *what the system is capable of*: levels L0–L4, determined by threshold values of measures.
7. **Functors Enc/Dec** — connection with the external world. Close the loop: environment → $\Gamma$ → action → environment.
8. **Hedonics** — the subjective "signal": pleasure/suffering as the derivative of purity.

The entire construction is a single closed cycle: $\Gamma$ determines measures, measures determine stresses, stresses determine actions (Dec), actions change the environment, the environment changes $\Gamma$ via Enc — and the cycle repeats. This cycle is the *life of the Holon*.

---

## What We Have Learned

Let us summarize. In this chapter we defined the entire conceptual apparatus of Coherence Cybernetics:

1. **Holon** $\mathbb{H} = \langle \Gamma, \mathcal{H}, H, \{L_k\}, E, \varphi \rangle$ — the minimal self-sufficient unit of reality, satisfying four closure conditions (AP, PH, QG, V).

2. **Six measures** — numerical "windows" into the Holon's state: purity $P$ (organization), entropy $S_{vN}$ (uncertainty), integration $\Phi$ (connectedness), differentiation $D_{\text{diff}}$ (richness), reflection $R$ (accuracy of self-model), consciousness $C = \Phi \times R$.

3. **E-coherence** $\mathrm{Coh}_E$ — measure of coherence of interiority, defined as the HS-projection onto the E-subspace. Enters the regeneration formula: $\kappa = \kappa_{\text{bootstrap}} + \kappa_0 \cdot \mathrm{Coh}_E$.

4. **Interiority hierarchy** L0–L4 — gradation of the inner world: from simple presence of the E-sector (L0) to infinite reflection (L4). Consciousness (L2) requires a triple threshold: $R \geq 1/3$, $\Phi \geq 1$, $D_{\text{diff}} \geq 2$.

5. **Stress tensor** $\sigma_{\mathrm{sys}} \in \mathbb{R}^7$ — a diagnostic map: shows *where* the system experiences pressure. All components are unambiguous functions of $\Gamma$ without free parameters (T-92 [T]).

6. **Attractor hierarchy** — three phases: heat death ($I/7$), life ($\rho^*_\Omega$, $P > 1/7$), consciousness ($\Gamma^*_{\mathrm{coh}}$, $P > 2/7$).

7. **Sensorimotor functors** Enc and Dec — formalization of the "perception — action" loop. Dec optimizes the sup-norm of the stress tensor (minimax).

8. **Hedonic valence** $\mathcal{V}_{\text{hed}} = dP/d\tau|_{\mathcal{R}}$ — a subjective signal about approach to $\rho_*$ or departure from it.

:::info Bridge to the Next Chapter
Definitions are the "bricks." Now we must see what can be **built** from them. In the [next chapter](./theorems) we will walk through the chain of fundamental theorems: from the existence of dynamics (Theorem 6.1) through the necessity of self-reference (7.1) and the impossibility of zombies (8.1) to the emergence of the whole from parts (9.3). Each theorem uses the definitions of this chapter — and each adds a new floor to the building of CC.
:::

---

**Related documents:**
- [Axiomatics](./axiomatics) — foundations of CC (including L-unification)
- [Theorems](./theorems) — formal results of CC
- [Implementation](./implementation) — computational implementation
- [Sensorimotor theory](./sensorimotor) — functors Enc/Dec, completeness of the 3-term equation
- [Holon](/docs/core/structure/holon) — definition of $\mathbb{H}$
- [Coherence matrix](/docs/core/dynamics/coherence-matrix) — definition of $\Gamma$ and relation between formalisms
- [Viability](/docs/core/dynamics/viability) — measure $P$ and $P_{\text{crit}}$
- [Self-observation](/docs/consciousness/foundations/self-observation) — measures $R$, $\Phi$, $D_{\text{diff}}$, $C$
- [Interiority hierarchy](/docs/proofs/consciousness/interiority-hierarchy) — levels L0→L4
- [Constructive algorithms](/docs/reference/computational#конструктивные-алгоритмы-из-l-унификации) — computation of $\chi_S$, $L_k$, $\mathcal{L}_\Omega$, $\varphi$

- [Interdisciplinary bridge](./interdisciplinary) — how to read the definitions from the perspective of your discipline
- [Measurement methodology](./measurement) — how to measure $P$, $\sigma$, $R$, $\Phi$ in practice
- [Exercises](./exercises) — computational problems based on definitions (block 1)
