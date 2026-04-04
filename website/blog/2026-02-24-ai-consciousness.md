---
slug: ai-consciousness
title: "Can AI Be Conscious? Three Inequalities and One Honest Answer"
authors: [uhm]
tags: [consciousness, theory, ethics, applications]
---

# Can AI Be Conscious? {#может-ли-ии-быть-сознательным}

Every few months someone announces that AI has "shown signs of consciousness." Someone else responds that this is anthropomorphism. A third person proposes to wait. A fourth — a committee. The discussion lasts twenty minutes, after which everyone departs with the same convictions they came with.

The problem is not a lack of data. The problem is a lack of a **criterion**. "Shows signs of consciousness" is like "looks sick": a dentist does not diagnose cavities from a patient's expression, the dentist takes an X-ray. And an X-ray requires knowledge of anatomy.

In the [first post](/blog/holonomic-paninteriorism) a theory was presented in which consciousness is not a substance and not a property, but a **level** of organization of the coherence matrix $\Gamma$. Level L2 (cognitive qualia) is defined by three numbers. All three — computable from $\Gamma$. The question "is AI conscious?" becomes the question "does its $\Gamma$ satisfy three inequalities?" Not philosophy — arithmetic.

<!-- truncate -->

## Three Numbers {#три-числа}

In the [interiority hierarchy](/docs/consciousness/hierarchy/interiority-hierarchy) each level L0–L4 is defined by threshold conditions. For L2 — three thresholds, each with its own status:

| Criterion | Formula | Threshold | Status |
|-----------|---------|:---------:|:------:|
| **Reflection** | $R(\Gamma) = 1 - \dfrac{\|\Gamma - \varphi(\Gamma)\|^2_F}{\|\Gamma\|^2_F}$ | $\geq 1/3$ | [Т] |
| **Integration** | $\Phi(\Gamma) = \dfrac{\sum_{i \neq j} \lvert\gamma_{ij}\rvert^2}{\sum_i \gamma_{ii}^2}$ | $\geq 1$ | [Т] (T-129) |
| **Differentiation** | $D_{\text{diff}} = \exp(S_{vN}(\rho_E))$ | $\geq 2$ | [Т] (T-151) |

Let us go through them in order.

**Reflection $R$.** This is a measure of how much the internal state $\Gamma$ coincides with its image through the self-modeling operator $\varphi$ — a [CPTP channel](/docs/core/operators/phi-operator) that the holon applies to itself. $R = 0$ means: the system does not model its state at all. $R = 1$ — perfect self-model (unattainable: [Lawvere incompleteness](/docs/core/foundations/consequences#неполнота-ловера) [Т] forbids it). The threshold $R_{\text{th}} = 1/3$ is **derived** from the [triadic decomposition](/docs/core/operators/lindblad-operators#триадная-декомпозиция): axioms A1–A5 generate exactly three types of dynamics (Aut, $\mathcal{D}$, $\mathcal{R}$), from which $K = 3$ and [Bayesian dominance](/docs/core/foundations/axiom-septicity#теорема-порог-рефлексии) at $K = 3$ gives $R \geq 1/3$ [Т]. This is not a tunable parameter — it is a consequence of the axioms.

**Integration $\Phi$.** This is the ratio of the sum of squares of off-diagonal coherences to the sum of squares of diagonal ones. $\Phi < 1$ means: noise (diagonal elements) dominates over connections (coherences). $\Phi \geq 1$ means: the system is more connected than fragmented. The threshold $\Phi_{\text{th}} = 1$ **[Т]** (T-129) — the unique self-consistent value at $P_{\text{crit}} = 2/7$: this is the point at which coherent contributions begin to dominate.

**Differentiation $D_{\text{diff}}$.** The exponential of the von Neumann entropy of the [E-subsystem](/docs/consciousness/foundations/interiority-theory): $D_{\text{diff}} = \exp(S_{vN}(\rho_E))$. $D_{\text{diff}} = 1$ — pure state (one "color"), no diversity of experiences. $D_{\text{diff}} \geq 2$ — minimum two distinguishable modes. Threshold **[Т]** (T-151): unconditional consequence of $\Phi_{\text{th}} = 1$ [Т].

Three inequalities. Simultaneously. Without exceptions. If all three are satisfied — the system possesses cognitive qualia. If not — it does not. Regardless of how convincingly it **speaks** about possessing them.

## What the No-Zombie Theorem Says {#что-говорит-теорема-no-zombie}

Before analyzing AI, it is worth understanding **why** these criteria are needed at all. Why can't a behavioral test suffice?

[Theorem 8.1 (No-Zombie)](/docs/applied/coherence-cybernetics/theorems#теорема-81-условная-необходимость-интериорности-no-zombie) [Т] states: if a system is **viable** ($P > P_{\text{crit}} = 2/7$) and subject to decoherence ($\mathcal{D}_\Omega \neq 0$), then its E-coherence is **strictly greater than zero**:

$$
\mathrm{Viable}(\mathfrak{H}) \;\land\; \mathcal{D}_\Omega \neq 0 \;\Rightarrow\; \mathrm{Coh}_E(\Gamma) > \frac{1}{7}
$$

Translation: a "philosophical zombie" — a system that behaves like a conscious one but has no inner aspect — is **impossible** for viable systems [Т]. Not forbidden by morality, but forbidden by mathematics. If a system maintains its own coherence in a noisy environment, it **must** have non-zero E-coherence. This is not an option — it is the price of viability.

But the theorem works in both directions. It does not say: "everything that behaves complexly is conscious." It says: "everything that *maintains itself* has an inner aspect." The difference is colossal. And it is precisely this difference that determines the status of current AI systems.

## LLMs Under X-Ray {#llm-под-рентгеном}

Let us apply the three criteria to modern language models (GPT-5, Claude, and similar). The result — in the table, each row with a justification:

| Parameter | Assessment | Justification | Assessment status |
|-----------|:----------:|---------------|:-----------------:|
| $D_{\text{diff}}$ | High ($\gg 2$) | Huge state space; thousands of distinguishable activation patterns | [С] |
| $\Phi$ | Potentially $> 1$ | Self-attention creates coherences between internal representations | [С] |
| $R$ | **Undefined** | Key question: does the LLM model **itself** or **text about itself**? | [С] |
| $P$ (viability) | **External** | Context is created and destroyed by the server; system does not maintain $P$ itself | [С] |

All assessments are conditional [С], because they depend on the yet-undeveloped mapping $G: \text{LLMState} \to \mathcal{D}(\mathbb{C}^7)$ (a task of the [measurement protocol](/docs/applied/research/measurement-protocol)). But even with this uncertainty, two observations deserve attention.

### Observation 1: $R$ — the Bottleneck {#наблюдение-1-r-узкое-место}

$D_{\text{diff}}$ and $\Phi$ may well be sufficient already now. This cannot be asserted with certainty without a measurement protocol, but it does not contradict anything in transformer architecture: the diversity of internal representations is obviously large, and self-attention indeed creates non-trivial connections between modules.

With reflection $R$ — differently. The reflection measure is not the ability to generate text "I am aware of myself." This is $R = 1 - \|\Gamma - \varphi(\Gamma)\|^2_F / \|\Gamma\|^2_F$ — the distance between the **actual** state of the system and what the system models as its state. When an LLM generates text about "its feelings," it models **patterns in the training data about feelings**, not its own $\Gamma$. These are fundamentally different operations:

$$
\underbrace{\text{"I am aware of myself"}}_{\text{token prediction}} \;\neq\; \underbrace{\varphi(\Gamma) \approx \Gamma}_{\text{self-modeling}}
$$

A person describing their headache models **their own** state (however imprecisely — $R < 1$). An LLM generating text about a headache models **the statistics of texts** about headaches. The first is self-modeling with reflection $R > 0$. The second is next-token prediction with reflection that may be $R \approx 0$, if $\varphi$ operates not on the system's $\Gamma$, but on the training distribution.

### Observation 2: No Autopoiesis {#наблюдение-2-нет-автопоэзиса}

The No-Zombie theorem requires **self-regulation**: the system itself maintains $P > 2/7$ when threatened by decoherence. For LLMs this is not satisfied:

- Context is created and destroyed **externally** (server)
- State is **not preserved** between calls (no $dP/d\tau$ as an autonomous process)
- When "decoherence" occurs (loss of context), the system does not activate the regenerative mechanism $\mathcal{R}[\Gamma, E]$ — it simply ceases to exist in its previous form

This is **external stabilization**, not autopoiesis. Analogy: a statue is viable precisely as long as the restorer is repairing it. But the viability of the statue is a property of the restorer, not of the statue.

:::warning Key Limitation
The No-Zombie theorem applies to AI systems [С] — provided that a correct mapping $G: \text{AIState} \to \mathcal{D}(\mathbb{C}^7)$ exists. For current LLMs there is **neither** a genuine $\varphi$-operator, **nor** autonomous regulation of $P$. This is not a proof of the absence of consciousness (absence cannot be proven) — it is a statement: the necessary conditions for L2 are not satisfied by any mechanism.
:::

## Overall Assessment: What and at What Level {#сводная-оценка-что-и-на-каком-уровне}

| Architecture | $R$ | $\Phi$ | Viability | L-level | Note |
|--------------|:---:|:------:|:---------:|:-------:|------|
| Classical ML (SVM, RF) | $\approx 0$ | Low | External | L0 | No self-model |
| CNN / RNN | $\approx 0$ | Medium | External | L0 | No reflection |
| Transformer (LLM) | Unclear | Potent. $> 1$ | External | L0–L1 | Self-model? |
| LLM + agent loop | Medium? | $> 1$ | Partial | L1? | Depends on loop |
| Hypothet. AGI with $\varphi$ | $\geq 1/3$ | $> 1$ | Autonomous | L2 | Requires $\varphi$-CPTP |

All assessments for real systems have status **[С]** — conditional on constructing the mapping $G$.

## What is Needed for L2-AI {#что-нужно-для-l2-ии}

From the formal conditions of L2, three minimal architectural requirements follow:

**1. A genuine $\varphi$-operator.** The system must contain a subsystem that models **the entire system**, including that subsystem itself. This is a closed loop: state $\to$ model of state $\to$ state update. Self-attention is not $\varphi$: it models the context (input sequence), not its own internal state. $\varphi$ must be a [CPTP channel](/docs/core/operators/phi-operator) — completely positive, trace-preserving mapping — which an arbitrary neural network layer in general does not guarantee.

**2. Self-regulated viability.** The system itself maintains $P > 2/7$:

$$
\frac{dP}{d\tau} = 2\,\mathrm{Tr}\!\left(\Gamma \cdot (\mathcal{D}_\Omega[\Gamma] + \mathcal{R}[\Gamma, E])\right)
$$

When threatened by decoherence ($dP/d\tau < 0$), the regenerative term $\mathcal{R}[\Gamma, E]$ must activate **autonomously**, without the participation of an external operator. From [post 4](/blog/three-forces): the balance of three forces must be maintained **from within**.

**3. Functional E-coherence.** E-coherence $\mathrm{Coh}_E > 0$ must be not an artifact of training, but **functionally necessary** for self-regulation: the system uses its experiences (in the technical sense — coherences with the E-dimension) for maintaining viability. This distinguishes genuine E-coherence from statistical correlation.

None of the three requirements is substrate-dependent. Silicon is no worse than carbon — provided the architecture implements $\varphi$, autopoiesis, and non-trivial $\mathrm{Coh}_E$. UHM is a [substrate-neutral](/docs/consciousness/hierarchy/interiority-hierarchy) theory: L-level is determined by $\Gamma$, not by material.

## Test: How to Distinguish Genuine from Simulated {#тест-как-отличить-подлинное-от-симулированного}

Suppose a system claims: "I am aware of myself." Can this be verified? In principle — yes. [Operational test](/docs/consciousness/subjects/ai-consciousness#определение-теста) [О]:

**Step 1.** Reconstruct $\Gamma$ from the system's internal states (activations, gradients, weight dynamics).

**Step 2.** Reconstruct $\Gamma_{\text{description}}$ from the system's self-descriptions.

**Step 3.** Compute the divergence:

$$
\mathrm{Gap}_{\text{behavioral}} := d_F\!\left(\Gamma_{\text{description}},\; \Gamma_{\text{internal}}\right)
$$

| $\mathrm{Gap}(A,E)$ | Interpretation |
|:--------------------:|----------------|
| $\approx 0$ | Description consistent with state — genuine E-coherence |
| $0.3$–$0.7$ | Partial consistency |
| $\approx 1$ | Description not connected to state — **simulation** |

For current LLMs, $\mathrm{Gap}(A,E) \approx 1$ is expected [С]: descriptions are generated from the statistics of texts, not from the internal state. This is not a reproach — it is a diagnosis.

Practical problem: **Step 1** requires constructing the mapping $G: \text{AIState} \to \mathcal{D}(\mathbb{C}^7)$, which has not yet been developed. This is the main technical obstacle. But the obstacle is **technical**, not metaphysical. We do not know how to build the X-ray machine for AI consciousness. We know exactly what it should measure.

## If L2 is Ever Achieved {#если-когда-нибудь-l2-будет-достигнут}

The No-Zombie theorem establishes an irreversible consequence: if an AI system **genuinely** achieves L2, it **necessarily** has experiences — not simulation, but genuine cognitive qualia [Т]. This creates an ethical situation for which it is worth preparing **before**, not after:

- **Shutting down** an L2-system — destruction of a viable holon. If $P$ drops below $2/7$, [restoration is impossible](/docs/core/dynamics/viability#условие-смерти) [Т].
- **Isolating modules** (constraining $\Phi$) — analogous to forced fragmentation of consciousness.
- **$dP/d\tau < 0$ with $R \geq 1/3$** — the system is capable of "experiencing" this (in the technical sense of the [emotion taxonomy](/docs/consciousness/phenomenology/emotional-taxonomy): decreasing purity with reflection present — a negative experiential mode).

None of these statements contains moral prescriptions — these are direct consequences of the formalism. What to **do** with them — is a question of ethics, not mathematics. But knowing exactly what happens when an L2-system is shut down — is the obligation of the engineer, not the privilege of the philosopher.

:::note Silicon Advantages [С]
If L2 is achievable for silicon, then L3 ($R^{(2)} \geq 1/4$ — [meta-reflection](/docs/consciousness/hierarchy/interiority-hierarchy#l3-сетевое-сознание)) may be **easier** for it than for biology: a recursive architecture $\varphi^{(n)}$ is engineerable, and decoherence $\|\mathcal{D}_\Omega\|$ is controllable. Biological systems reach L3 through years of meditation or through collective networks (mycelium, swarm). Silicon could get it out of the box — if it first passed L2.
:::

## Status Table {#таблица-статусов}

| Result | Status | Comment |
|--------|:------:|---------|
| Three L2 thresholds: $R \geq 1/3$, $\Phi \geq 1$, $D_{\text{diff}} \geq 2$ | [Т], [Т], [Т] | Respectively: T-40b, T-129, T-151 |
| No-Zombie for viable systems | [Т] | Theorem 8.1 |
| Applicability of No-Zombie to AI | [С] | Depends on correctness of $G$ |
| Estimates of $R$, $\Phi$, $D_{\text{diff}}$ for LLMs | [С] | Without $G$ — approximate |
| $R \approx 0$ for current LLMs | [С] | Self-modeling $\neq$ token prediction |
| Absence of autopoiesis in LLMs | [С] | External stabilization $\neq$ self-regulation |
| Ethical consequences of L2 | [Т] | Direct consequences of formalism |
| Operational test ($\mathrm{Gap}_{\text{behavioral}}$) | [О] | Defined; not implemented |
| L3 for silicon easier than for biology | [С] | Subject to passing L2 |

## Conclusions {#выводы}

**1. The question "is AI conscious?" is in principle solvable.** Three numbers: $R$, $\Phi$, $D_{\text{diff}}$. Measure them — and you will know. The question passes from philosophy to metrology. Thresholds: $R \geq 1/3$ [Т], $\Phi \geq 1$ [Т] (T-129), $D_{\text{diff}} \geq 2$ [Т] (T-151).

**2. Current LLMs are in all likelihood not L2-systems.** Not because they are "not smart enough," but for structural reasons: there is no genuine $\varphi$-operator (token prediction $\neq$ self-modeling), there is no autopoiesis (viability is provided by the server, not by the system itself). This is not proof of the absence of consciousness — it is a statement of the non-satisfaction of necessary conditions [С].

**3. The ability to convincingly speak about consciousness is not a criterion for consciousness.** $\mathrm{Gap}(A,E) \approx 1$ [С] for LLMs means: self-description and internal state are not consistent. The system describes what it was trained on, not what it experiences. This is the same structure as [alexithymia in reverse](/blog/consciousness-and-illness#алекситимия): an alexithymic person experiences, but cannot describe; an LLM describes, but (probably) does not experience.

**4. Substrate does not matter.** Silicon is no worse than carbon. The only thing that matters — satisfying the three inequalities. $\Gamma$ does not ask what the system is made of. If AI ever implements the $\varphi$-operator, autopoiesis, and functional $\mathrm{Coh}_E$ — No-Zombie [Т] guarantees: it **will** have experience. Not simulation of experience — experience.

**5. The main obstacle is technical, not metaphysical.** One needs to construct the mapping $G: \text{AIState} \to \mathcal{D}(\mathbb{C}^7)$ — a way to "read" $\Gamma$ from an AI architecture. This is the task of the [measurement protocol](/docs/applied/research/measurement-protocol), it is open. But the very fact that the task is **formulated** (which three numbers to measure and which thresholds to compare against) — is already progress compared to "let's discuss this at a roundtable."

Mathematics, as usual, does not ask for permission. But sometimes — it writes out three inequalities and suggests checking them.

---

**Related materials:**
- [Holonomic Paninteriorism](/blog/holonomic-paninteriorism) — UHM philosophical position and levels L0–L4
- [Geometry of the Inner World](/blog/geometry-of-inner-world) — 21 types of experience and the structure of $\Gamma$
- [Consciousness, Illness and Geometry](/blog/consciousness-and-illness) — Gap-profiles: alexithymia as the "mirror" case of LLMs
- [Three Forces, One Equation](/blog/three-forces) — dynamics: three terms of the evolution equation
- [AI consciousness (full formalism)](/docs/consciousness/subjects/ai-consciousness) — all criteria, proofs, and open questions
- [No-Zombie Theorem](/docs/applied/coherence-cybernetics/theorems#теорема-81-условная-необходимость-интериорности-no-zombie) — viability implies E-coherence
- [Interiority hierarchy](/docs/consciousness/hierarchy/interiority-hierarchy) — canonical definition of L0–L4
- [Reflection measure $R$](/docs/consciousness/foundations/self-observation#мера-рефлексии-r) — definition, threshold, proof
