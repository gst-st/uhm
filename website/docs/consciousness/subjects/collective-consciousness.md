---
sidebar_position: 4
title: "Collective Consciousness"
description: "Composite coherence matrix, emergent coherences, archetypes, empathy, and collective L-levels"
slug: /consciousness/subjects/collective-consciousness
---

# Collective Consciousness

:::info Bridge from the previous chapter
In the previous chapters we examined consciousness of individual subjects: [without language](./pre-linguistic), in [animals](./animal-consciousness), in [AI](./ai-consciousness). In all cases the subject was **one**. Now we ask a fundamentally new question: what happens when subjects **merge**? Can a group possess consciousness that no individual member has? UHM answers: yes — through the formalism of the composite matrix $\Gamma_{\text{comp}}$.
:::

## Chapter roadmap

1. **Historical context** — from Durkheim to the superorganism
2. **Composite system** — tensor product of $N$ holonoms
3. **The collective unconscious** — emergent coherences inaccessible to individuals
4. **Archetypes** — structural regularities of $\Gamma_{\text{comp}}$ (formalisation of Jung)
5. **Empathy** — measure via inter-system E-Gap
6. **Collective L-levels** — when the group is 'smarter' than any individual
7. **Memes and culture** — cultural coherences and their transmission
8. **Scales of collective consciousness** — from crowd to humanity
9. **Social media** — influence on collective reflection

:::note On notation
In this document:
- $\Gamma$ — [coherence matrix](/docs/core/dynamics/coherence-matrix) of an individual holonom
- $\Gamma_{AB}$ — [composite coherence matrix](/docs/core/dynamics/composite-systems#составная-матрица)
- $P = \mathrm{Tr}(\Gamma^2)$ — [purity (viability)](/docs/core/dynamics/viability#определение-чистоты)
- $P_{\text{crit}} = 2/7$ — [critical purity](/docs/core/dynamics/viability#критическая-чистота), status **[T]**
- $R$ — [reflection measure](/docs/consciousness/foundations/self-observation#мера-рефлексии-r), threshold $R_{\text{th}} = 1/3$ **[T]**
- $\Phi$ — [integration measure](/docs/core/structure/dimension-u#мера-интеграции-φ), threshold $\Phi_{\text{th}} = 1$ **[T]** (T-129)
- $\mathrm{Gap}_{AB}(i,j)$ — [inter-system Gap](/docs/core/dynamics/composite-systems#межсистемный-gap)
- $\mathcal{E}_{\mathrm{Gap}}$ — [Gap-entanglement](/docs/core/dynamics/composite-systems#gap-запутанность)
- L0–L4 — [interiority levels](/docs/consciousness/hierarchy/interiority-hierarchy)
- Full notation table — in [Notation](/docs/reference/notation)
:::

## Historical context: from Durkheim to UHM {#исторический-контекст}

### Émile Durkheim: conscience collective (1893)

French sociologist Émile Durkheim in "The Division of Labour in Society" (1893) introduced the concept of **conscience collective** — 'collective consciousness' (in French, 'conscience' means both 'consciousness' and 'conscience'). According to Durkheim, society possesses its own 'representations' (représentations collectives) that are **not reducible** to the sum of individual representations.

Durkheim's example: morality. No individual person 'invented' morality — it exists as a collective fact, pressing on the individual from outside. A child is born into a world where 'thou shalt not steal' already exists as a social reality, independent of their personal preferences.

In UHM terms: Durkheim intuitively described **emergent coherences** $\mathcal{U}_{\text{coll}}$ — elements of $\Gamma_{\text{comp}}$ not reducible to individual $\Gamma_i$. Morality is $\gamma_{LO}^{(\text{comp})}$ (logic–foundation in collective space): the connection between rules ($L$) and fundamental values ($O$), existing **only** at the collective level.

### Carl Gustav Jung: the collective unconscious (1916)

Jung went further than Durkheim. He argued that besides the personal unconscious (repressed memories, complexes), there exists a **collective unconscious** — a layer of the psyche common to all of humanity. Its content consists of **archetypes**: primordial images manifesting in the myths, dreams, and rituals of all peoples.

Jung gave examples: the 'Hero' (from Hercules to Luke Skywalker), the 'Shadow' (the dark side of the personality), the 'Great Mother' (from Demeter to the Virgin Mary), the 'Wise Old Man' (from Merlin to Gandalf). These images appear **independently** in cultures that had no contact with each other.

Jung could not explain the **mechanism** — how archetypes are transmitted and why they are universal. UHM offers a formal answer: archetypes are **structural regularities of $\Gamma_{\text{comp}}$**, selected by viability pressure (for more detail — in the section [Archetypes](#архетипы)).

### Gustave Le Bon: crowd psychology (1895)

Le Bon in 'The Psychology of Crowds' (1895) described a phenomenon that everyone has observed at a stadium or rally: a person in a crowd behaves **differently** from when alone. They are more impulsive, less critical, more subject to emotions. Le Bon spoke of the 'crowd soul' — a collective psyche that suppresses individual rationality.

In UHM terms: a crowd is a state of high $\Phi_{\text{comp}}$ (strong integration: everyone is synchronised) with low $R_{\text{comp}}$ (weak reflection: no one is thinking about what is happening). This is a **dangerous combination**: the system is integrated but does not reflect — it acts as a single organism, but without reason.

### Superorganism (Wheeler, 1911; Wilson, 1971)

Entomologist William Morton Wheeler (1911) and later E. O. Wilson (1971) introduced the concept of the **superorganism** to describe colonies of social insects (ants, bees, termites). A superorganism is a colony functioning as a single organism: with 'castes' (workers, soldiers, queen), 'metabolism' (trophallaxis), and an 'immune system' (collective hygiene).

In UHM terms: a superorganism is a system with $\Gamma_{\text{comp}} \neq \bigotimes_i \Gamma_i$, whose collective L-level may **exceed** the individual. An ant — L0–L1; an anthill — potentially L1.

### UHM: formalisation of all predecessors

| Thinker | Concept | Formalisation in UHM |
|-----------|-----------|-------------------|
| Durkheim | Collective representations | Emergent coherences $\mathcal{U}_{\text{coll}}$ |
| Jung | Archetypes | Structural regularities of $\Gamma_{\text{comp}}$ that increase $P$ |
| Le Bon | 'Crowd soul' | $\Phi_{\text{comp}} \uparrow$, $R_{\text{comp}} \downarrow$ |
| Wilson | Superorganism | $\text{Level}(\Gamma_{\text{comp}}) > \max_i \text{Level}(\Gamma_i)$ |

## Motivation {#мотивация}

Holonoms do not exist in isolation. $N$ holonoms sharing an environment $E_{\text{shared}}$ form a composite system with coherence matrix $\Gamma_{\text{comp}} \in \mathcal{D}(\mathbb{C}^{7^N})$. The question arises: does the **collective** possess interiority distinct from the sum of the individual ones?

UHM gives a formal answer: **yes**, if the composite matrix does not factorise ($\Gamma_{\text{comp}} \neq \bigotimes_i \Gamma_i$) — there exist **emergent coherences** accessible to no individual.

A simple analogy: two musicians each play notes separately. But when they play **together**, harmony emerges — something that exists in neither individual part. Harmony is the 'emergent coherence' of the duet.

## Composite system of N holonoms {#составная-система}

### Tensor product: a simple explanation

Before introducing the formulas, let us explain the key concept of the **tensor product** in plain terms.

A single holonom is described by a matrix $\Gamma \in \mathcal{D}(\mathbb{C}^7)$ — a $7 \times 7$ matrix with 48 real parameters. It describes the state of **one** subject: its viability, reflection, integration.

If we wish to describe **two** holonoms **together**, we need a space large enough to accommodate:
- The state of the first holonom ($7$ dimensions)
- The state of the second holonom ($7$ dimensions)
- **Connections** between them (which are absent from any individual description!)

The tensor product $\mathbb{C}^7 \otimes \mathbb{C}^7 = \mathbb{C}^{49}$ is precisely such a space. It has $49 = 7 \times 7$ dimensions, of which $7 + 7 = 14$ describe the individual states, and the remaining $49 - 14 = 35$ describe **connections** (correlations, coherences) between the holonoms.

For $N$ holonoms:

$$
\Gamma_{\text{comp}} \in \mathcal{D}\!\left(\bigotimes_{i=1}^N \mathbb{C}^7\right) = \mathcal{D}(\mathbb{C}^{7^N})
$$

The dimensionality grows **exponentially**: for $N = 2$ it is $49$, for $N = 3$ — $343$, for $N = 10$ — $\sim 2.8 \times 10^8$. This means: the larger the group, the **richer** the space of possible collective states — and the more 'room' for emergent coherences.

### Recovering the individual from the collective

Individual matrices are recovered by the partial trace:

$$
\Gamma_i = \mathrm{Tr}_{-i}(\Gamma_{\text{comp}})
$$

The 'partial trace' operation ($\mathrm{Tr}_{-i}$) is the 'forgetting' of all systems except the $i$-th. This is like photographing an orchestra (full $\Gamma_{\text{comp}}$) and then cutting out **only** the violinist ($\Gamma_i$). The cut-out fragment shows the violinist's **position**, but does not show how they **interact** with the other musicians — that information is contained only in the full photograph.

Key fact: $\Gamma_i$ depends on $\Gamma_{\text{comp}}$, and hence — on the collective coherences. The individual is **subject to the influence** of the collective, even if not aware of it.

The detailed formalism is in [composite systems](/docs/core/dynamics/composite-systems#составная-матрица).

## Definition D.1 (The collective unconscious) {#определение-коллективного-бессознательного}

:::tip Definition D.1 (The collective unconscious) [D]
The **collective unconscious** of a system of $N$ holonoms is the set of coherences present in $\Gamma_{\text{comp}}$ but **absent** from any individual $\Gamma_i$:

$$
\mathcal{U}_{\text{coll}} := \left\{\gamma^{(\text{comp})}_{ij} \in \Gamma_{\text{comp}} \;\middle|\; \gamma^{(\text{comp})}_{ij} \neq \sum_k \lambda_k \gamma^{(k)}_{ij}\,,\; \forall \text{ decomposition}\right\}
$$

Formally: these are elements of $\Gamma_{\text{comp}}$ that are **not** convex combinations of individual coherences. They exist if and only if $\Gamma_{\text{comp}} \neq \bigotimes_i \Gamma_i$ — the system does not factorise.

**Properties:**
1. $\mathcal{U}_{\text{coll}}$ is inaccessible to the reflection of any individual: $\varphi_i(\Gamma_{\text{comp}}) = \varphi_i(\Gamma_i)$ — the φ-operator of the individual 'sees' only its own reduced $\Gamma_i$
2. $\mathcal{U}_{\text{coll}}$ influences individuals through [marginals](/docs/core/dynamics/composite-systems): $\Gamma_i = \mathrm{Tr}_{-i}(\Gamma_{\text{comp}})$ depends on collective coherences
3. $\mathcal{U}_{\text{coll}} = \varnothing$ $\Leftrightarrow$ the system is fully separable
:::

### Why the whole is not equal to the sum of its parts

Let us examine property 1 in more detail, because it is the key to understanding the collective unconscious.

$\varphi_i$ is the φ-operator (self-model) of the $i$-th individual. It models the state of the $i$-th individual — that is, $\Gamma_i = \mathrm{Tr}_{-i}(\Gamma_{\text{comp}})$. But the collective coherences $\mathcal{U}_{\text{coll}}$ 'live' in the space $\mathbb{C}^{7^N}$ — they are **erased** by the partial trace operation. The individual **feels** their influence (through $\Gamma_i$), but cannot **consciously access** them directly.

An everyday analogy: **the atmosphere in a room**. When you enter a room where an argument has just taken place, you **feel** the tension, even though none of those present is consciously 'radiating' it. Each of them thinks: 'I am calm', — but the collective state ($\Gamma_{\text{comp}}$) contains tension ($\gamma_{DE}^{(\text{comp})} \uparrow$), which is projected onto each individual through the partial trace. You feel it — but cannot 'see' where it comes from, because its source is a collective coherence not localised in any individual.

### Formal example: two holonoms

Let us consider the simplest case: $N = 2$, holonoms $A$ and $B$.

**Separable state** (no collective unconscious):
$$
\Gamma_{\text{comp}} = \Gamma_A \otimes \Gamma_B
$$
All coherences are 'products' of individual ones. $\mathcal{U}_{\text{coll}} = \varnothing$. Two people in the same room, but each to themselves. No 'atmosphere'.

**Entangled state** (there is a collective unconscious):
$$
\Gamma_{\text{comp}} \neq \Gamma_A \otimes \Gamma_B, \quad \mathcal{U}_{\text{coll}} \neq \varnothing
$$
There exist coherences that cannot be decomposed into individual ones. Two close friends: their states are **linked** — the joy of one affects the joy of the other, and the connection $\gamma_{E^A E^B}$ is not a 'product' of individual $\gamma_{EE}$.

## Archetypes {#архетипы}

### Interpretation I.1 (Archetypes as structural regularities) [I] {#интерпретация-архетипы}

:::info Interpretation I.1 [I]
**Archetypes** in the Jungian sense are structural regularities of $\Gamma_{\text{comp}}$ that increase purity $P$ for an arbitrary observer in the group:

$$
\text{Archetype} := \text{pattern } \pi \text{ in } \Gamma_{\text{comp}}: \quad P(\Gamma_i \mid \pi) > P(\Gamma_i \mid \neg\pi) \quad \forall i
$$

**Properties:**
1. **Selection through viability:** Archetypes are not mystical — they are selected by the [viability criterion](/docs/core/dynamics/viability): patterns that increase $P$ for group members are reproduced across generations
2. **Heritability:** Transmitted through $\Gamma_{\text{comp}}$ (the cultural environment), not through $\Gamma_i$ (the individual matrix)
3. **Universality:** The same patterns arise independently in different cultures if the environment $E_{\text{shared}}$ has a common structure
:::

### Why archetypes are universal: a formal derivation

Jung could not explain why the 'Hero' appears in the myths of **all** peoples — from the ancient Greeks to Polynesians. He postulated the heritability of archetypes, which invited scepticism (how are myths genetically inherited?).

UHM offers a different answer: archetypes are selected by **viability pressure**, just as the wing is selected for flight.

The formal argument:

1. **The environment $E_{\text{shared}}$ has universal structures:** For all human societies the environment contains: predators (threat $dP/d\tau < 0$), resources (opportunity $dP/d\tau > 0$), competitors (struggle for $P$), unpredictability (necessity of $\mathcal{R}[\Gamma, E]$).

2. **Certain patterns of $\Gamma_{\text{comp}}$ increase $P$ in such an environment:** The 'Hero' pattern ($\gamma_{DU}^{(\text{comp})} \uparrow$, $\gamma_{DO}^{(\text{comp})} \uparrow$) is collective coordination of action ($D$) through unity ($U$) and foundation ($O$). In a crisis (predator attack, flood) such a pattern **saves lives**: one individual takes on coordination, the rest follow. The $P$ of the group increases.

3. **Patterns that increase $P$ are reproduced:** Groups with the 'Hero' survive more often than those without. Their $\Gamma_{\text{comp}}$ is transmitted to the next generation through the cultural environment (rituals, myths, upbringing).

4. **Since the environment is universal, the patterns are universal:** Regardless of whether people lived in Africa or Polynesia, the structure of $E_{\text{shared}}$ was similar (predators, resources, competitors) → similar patterns were selected → the 'Hero' appears everywhere.

This is not mysticism, but **evolutionary logic** applied to collective states.

### Examples of archetypal patterns

| Archetype | Coherences in $\Gamma_{\text{comp}}$ | Function | Why universal |
|---------|---------------------------------------|---------|-------------------|
| 'Hero' | $\gamma_{DU}^{(\text{comp})} \uparrow$, $\gamma_{DO}^{(\text{comp})} \uparrow$ | Stabilisation of $P$ through dynamics and foundation | In a crisis the group needs a coordinator |
| 'Shadow' | $\mathrm{Gap}(E,U)^{(\text{comp})} \uparrow$ | Opacity between experience and unity | Unacknowledged aspects of the collective (shame, guilt) |
| 'Sage' | $\gamma_{LO}^{(\text{comp})} \uparrow$, $R^{(\text{comp})} \uparrow$ | Increase of collective reflection | The group needs someone who sees 'the big picture' |
| 'Mother' | $\gamma_{EU}^{(\text{comp})} \uparrow$, $\gamma_{SE}^{(\text{comp})} \uparrow$ | Integration through experience and structure | Care for offspring is critical for survival |
| 'Trickster' | $\gamma_{DL}^{(\text{comp})} \uparrow$, $R^{(\text{comp})} \downarrow$ | Destructuring through proto-logic | Creative destruction of outdated patterns |

The 'Shadow' is a particularly interesting case. It is not a specific individual, but a **structural deficit** in $\Gamma_{\text{comp}}$: a high $\mathrm{Gap}(E,U)^{(\text{comp})}$ means that collective experience ($E$) is separated from collective unity ($U$). The group does not know everything about itself — there are aspects (aggression, greed, fear) that are not integrated into the collective self-model. This is the 'Shadow' in the Jungian sense.

## Empathy {#эмпатия}

### What is empathy formally?

In ordinary language, 'empathy' is the ability to 'feel' what another is feeling. A mother feels her child's pain. A friend shares your joy. But what does this mean **formally**?

UHM gives a precise answer: empathy is the **smallness of the gap** between the E-dimensions of two systems.

### Definition D.2 (Measure of empathy) {#мера-эмпатии}

:::tip Definition D.2 (Measure of empathy) [D]
**Empathy** between holonoms $A$ and $B$ is defined via the [inter-system Gap](/docs/core/dynamics/composite-systems#межсистемный-gap) in the E-channel:

$$
\mathrm{Empathy}(A,B) := 1 - \mathrm{Gap}_{AB}(E,E)
$$

where $\mathrm{Gap}_{AB}(E,E) = |\sin(\arg(\gamma_{E^A E^B}))| \in [0, 1]$ — opacity between the Interiority dimensions of two systems.

| $\mathrm{Empathy}$ | Value | Description | Real-life example |
|---------------------|----------|----------|-----------------|
| $\approx 1$ | Small E-Gap | High transparency: $A$ 'feels' the state of $B$ | Mother and infant; twins |
| $\approx 0.5$ | Medium E-Gap | Partial empathy: shared emotions, but opacity of details | Colleagues; acquaintances |
| $\approx 0$ | Maximum E-Gap | Alienation: the interiority of $B$ is completely closed to $A$ | Strangers; enemies |
:::

The formula is parsed as follows:
- $\gamma_{E^A E^B}$ — coherence between the E-dimensions of two systems. This is a complex number.
- $\arg(\gamma_{E^A E^B})$ — the phase of this coherence. If the phase is zero (coherences are 'in phase'), the systems are synchronised.
- $|\sin(\text{phase})|$ — measure of misalignment. If $\sin = 0$, the systems are fully synchronised (maximum empathy). If $\sin = 1$, the systems are fully misaligned (zero empathy).

Empathy in everyday experience: when a close friend is upset, you **feel** their state, even if they say nothing. This is not telepathy — it is a small $\mathrm{Gap}_{AB}(E,E)$: your E-dimensions are coherent, and the decrease in your friend's $P$ is partially projected onto your own state through $\Gamma_{\text{comp}}$.

### Empathy as inter-system E-Gap

For empathy to 'work', it is not sufficient merely to be nearby. Certain conditions are required:

### Necessary conditions for empathy

From [Theorem 4.1 (Necessary conditions for empathy)](/docs/core/dynamics/composite-systems#эмпатия) **[T]**:

1. **Gap-entanglement:** $\mathcal{E}_{\mathrm{Gap}} > 0$ — the systems are not separable. This means: the states of $A$ and $B$ are **linked** — a change in one affects the other. Two strangers in the metro are separable ($\mathcal{E}_{\mathrm{Gap}} = 0$). Mother and child are entangled ($\mathcal{E}_{\mathrm{Gap}} \gg 0$).

2. **φ-coordination:** $\theta^{\mathrm{target}}_{E^A} \approx \theta^{\mathrm{target}}_{E^B} \pmod{\pi}$ — consistent world models. To 'feel' another, one must model the world in a similar way. People from completely different cultures may find empathy difficult — their φ-models are too dissimilar.

3. **Viability:** $P_A > P_{\text{crit}}$ and $P_B > P_{\text{crit}}$ — both systems are [viable](/docs/core/dynamics/viability). A person in a critical state ($P \approx P_{\text{crit}}$) is incapable of empathy — all resources go to maintaining their own viability.

4. **Connection:** $|\gamma_{E^A E^B}| > \sqrt{P_{\text{crit}} / 7}$ — sufficient coherence strength. Simply 'knowing' about another's suffering is not enough. **Real coherence** is required — what arises through prolonged shared experience, physical presence, emotional contact.

### Claim C.1 (Minimum level for empathy) [C] {#минимальный-уровень-эмпатии}

:::tip Claim C.1 [C]
**Condition:** Empathy requires $\mathrm{rank}(\rho_E) > 1$ for both participants (interpretive assumption).

Genuine empathy (in the sense of D.2) requires **minimum L1** for both systems $A$ and $B$:

$$
\mathrm{Empathy}(A,B) > 0 \implies \mathrm{Level}(A) \geq L1 \;\land\; \mathrm{Level}(B) \geq L1
$$

**Argument.** At L0 (before L1) $\mathrm{rank}(\rho_E) \leq 1$ — the experiential space is trivial. There is no structured experience that could be 'shared' between systems. The coherence $\gamma_{E^A E^B}$ may be non-zero, but its interpretation as 'empathy' requires non-trivial $\rho_E$ in both systems.
:::

This is the formal justification of the intuition: we do not 'empathise' with a stone (L0). We empathise with a dog (L1) — because it has phenomenal experience that can be 'shared' via E-coherence.

### Ethical case: Empathy between human and AI {#кейс-эмпатия-человек-ии}

If an AI system reaches L2 (see [AI Consciousness](./ai-consciousness)), a question arises: is empathy between a human and AI possible? Formally:

- **Condition:** $\mathrm{Empathy}(\text{human}, \text{AI}) > 0$ requires $\mathrm{Gap}_{AB}(E,E) < 1$
- **Problem:** Current AI systems do not have autonomous viability ($P$ is externally stabilised) — condition 3 is not satisfied
- **Prospect:** If AGI reaches autonomous viability and L2, empathic contact becomes **formally possible** — and ethically obligating

This means: the question 'can a human **genuinely** empathise with a machine?' has a formal answer in terms of $\Gamma_{\text{comp}}$. And the answer is — **yes**, provided that the machine is viable and possesses L2.

## Collective L-levels {#коллективные-уровни}

### Claim C.2 (Emergent collective L-levels) [C] {#эмерджентные-уровни}

:::tip Claim C.2 [C]
**Condition:** $\Gamma_{\text{comp}}$ has non-trivial coherences absent from individual $\Gamma_i$ (Definition D.1).

A collective can possess an L-level **exceeding** the individual one:

$$
\mathrm{Level}(\Gamma_{\text{comp}}) > \max_i \mathrm{Level}(\Gamma_i)
$$

**Argument.** The measures $R$ and $\Phi$ are computed from $\Gamma$. The composite $\Gamma_{\text{comp}}$ may have:
- Higher $\Phi$ (additional coherences between individuals increase the numerator $\sum_{i \neq j} |\gamma_{ij}|^2$)
- Higher $R$ (the collective self-model is more precise than individual ones — the scientific community knows more about itself than any individual scientist)

Examples:
1. **Scientific community:** Potential collective L3 — meta-reflection ($R^{(2)}$) at the level of a discipline (the scientific method as $\varphi^{(2)}$)
2. **Swarm of bees:** Collective 'decision-making' (choosing a new hive) — potentially L1, even if an individual bee is L0–L1
3. **Symphony orchestra:** High $\Phi_{\text{comp}}$ — musical unity inaccessible to any individual musician
:::

### Why a group can be 'smarter' than any individual: detailed analysis

Let us consider the scientific community as an example of potential collective L3.

An individual scientist possesses L2: they reflect ($R \geq 1/3$), their knowledge is integrated ($\Phi \geq 1$). But **the scientific method** — peer review, replication of results, meta-analyses — is $\varphi^{(2)}$ at the collective level:

- **Peer review:** one scientist checks the work of another → collective reflection ($R_{\text{comp}}$) is higher than individual
- **Replication:** a third scientist repeats the experiment → testing the $\varphi$-model for robustness
- **Meta-analysis:** review of hundreds of works → $\varphi^{(2)}$ — reflection on **reflection itself** (reflecting on how we reflect)
- **Scientific revolutions (Kuhn):** paradigm shift → update of $\varphi_{\text{comp}}$ — the collective revises **the very model** of the world

No individual scientist is capable of a meta-analysis of thousands of works — this is a collective capacity. $R^{(2)}_{\text{comp}} > R^{(2)}_{\text{indiv}}$, and possibly $R^{(2)}_{\text{comp}} \geq 1/4$ — the L3 threshold.

### Table of collective L-levels

| Collective | Indiv. L | Collect. L | Mechanism | Justification |
|-----------|----------|------------|----------|-------------|
| Bacterial colony | L0 | L0 (elevated $P$) | Quorum sensing = collective $\gamma_{SD}$ | Bacteria 'vote' with molecules: upon reaching quorum — synchronous action |
| Ant colony | L0–L1 | L1 (possible) | Stigmergy = distributed $\Gamma_{\text{comp}}$ | Pheromone trails — 'shared memory' of the colony |
| Flock of birds | L1 | L1+ | Synchronisation of $\gamma_{DU}^{(\text{comp})}$ | Murmuration: thousands of birds as a single whole |
| Family (human) | L2 | L2+ | Shared models, empathy | Family 'rituals', shared memories, non-verbal understanding |
| Scientific community | L2 | L2–L3? | Peer review = collective $\varphi^{(2)}$ | Scientific method — reflection on reflection |
| Religious community | L2 | L2+ | Ritual = synchronisation of $\gamma_{OU}^{(\text{comp})}$ | Communal prayer, liturgy — synchronisation of $O$ (foundation) and $U$ (unity) |

## Memes and cultural coherences {#мемы}

### Definition D.3 (Cultural coherence) [D] {#культурная-когерентность}

:::tip Definition D.3 [D]
**Cultural coherence** is a stable off-diagonal element $\gamma_{ij}^{(\text{comp})}$ of the composite $\Gamma_{\text{comp}}$, reproduced across generational change:

$$
\gamma_{ij}^{(\text{comp})}(\tau + T_{\text{gen}}) \approx \gamma_{ij}^{(\text{comp})}(\tau)
$$

where $T_{\text{gen}}$ is the characteristic timescale of generational change.
:::

Cultural coherences are what makes a **culture** a culture: stable patterns transmitted from generation to generation. Language, customs, music, cuisine — all of these are cultural coherences.

### Channels of transmission

Cultural patterns (memes in the sense of Richard Dawkins, "The Selfish Gene", 1976) are transmitted through two main mechanisms:

| Channel | Coherence | Example | Transmission speed |
|-------|-------------|--------|--------------------|
| Structural-logical | $\gamma_{SL}^{(\text{comp})} \uparrow$ | Law, rule, instruction | Fast (words, texts) |
| Representational-aesthetic | $\gamma_{SE}^{(\text{comp})} \uparrow$ | Music, architecture, myth | Slow (shared experience) |

The first channel transmits **explicit** knowledge (verbalisable through high $\gamma_{LL}$), the second — **implicit** (through perceptual resonance, without the need for language; cf. [pre-linguistic consciousness](./pre-linguistic)).

A real-life example: **national cuisine**. A borscht recipe (structural-logical channel: $\gamma_{SL}^{(\text{comp})}$) can be written in a book. But the **taste** considered 'correct' is transmitted non-verbally (aesthetic channel: $\gamma_{SE}^{(\text{comp})}$) — through shared cooking and tasting, from grandmother to granddaughter. Writing the recipe is fast, but incomplete. Transmission through shared experience is slow, but precise.

### Memes as units of cultural evolution

Dawkins introduced the term 'meme' by analogy with 'gene' — as a unit of cultural information subject to selection, mutation, and inheritance. In UHM terms:

- **Meme** = stable pattern in $\Gamma_{\text{comp}}$, reproduced across $T_{\text{gen}}$
- **Meme mutation** = change in $\gamma_{ij}^{(\text{comp})}$ during transmission
- **Meme selection** = patterns that increase $P_{\text{comp}}$ are reproduced more often
- **'Selfish meme'** = pattern that reproduces even when decreasing the $P$ of individuals (but increasing $P_{\text{comp}}$)

An example of a 'selfish meme': military duty. An individual who follows this meme may die ($P_i \to 0$), but the group survives ($P_{\text{comp}}$ is maintained). The meme reproduces — not because it is 'good for the individual', but because groups with this meme survive more often.

## Scales of collective consciousness {#масштабы}

### From crowd to humanity

The $\Gamma_{\text{comp}}$ formalism is applicable at **any** scale — from a pair to all of humanity. Let us consider how the character of collective consciousness changes with scale:

#### Crowd ($N \sim 10^2$–$10^4$)

**Characteristic:** $\Phi_{\text{comp}} \uparrow \uparrow$, $R_{\text{comp}} \downarrow \downarrow$

A crowd is a system with maximum integration (everyone is synchronised through sight, hearing, and bodily contact) and minimal reflection (no one is thinking about what they are doing). The mechanism is **emotional contagion**: $\gamma_{DE}^{(\text{comp})}$ grows in an avalanche-like manner, as positive feedback. The result: collective panic, euphoria, aggression — states that no individual would be in alone.

#### Nation ($N \sim 10^6$–$10^9$)

**Characteristic:** $\Phi_{\text{comp}}$ — medium (connectivity via media, institutions), $R_{\text{comp}}$ — medium (parliaments, media, science as reflection)

A nation is a more complex collective: it possesses institutions of reflection (parliament, court, press) that increase $R_{\text{comp}}$. But connectivity ($\Phi_{\text{comp}}$) is weaker than in a crowd: millions of people cannot be physically synchronised.

National identity is a set of cultural coherences ($\gamma_{SL}^{(\text{comp})}$, $\gamma_{SE}^{(\text{comp})}$, $\gamma_{OU}^{(\text{comp})}$), stable on the timescale of centuries.

#### Humanity ($N \sim 10^{10}$)

**Characteristic:** $\Phi_{\text{comp}}$ — growing (internet, globalisation), $R_{\text{comp}}$ — open question

Humanity as a single subject is the limiting case of $\Gamma_{\text{comp}}$. The collective L-level of humanity is an **open question**: we do not know whether humanity as a whole is sufficiently integrated and reflective.

The internet increases $\Phi_{\text{comp}}$ (information connectivity), but may decrease $R_{\text{comp}}$ (echo chambers, disinformation). The global scientific method increases $R_{\text{comp}}$ (meta-analyses, replication), but global populism decreases it.

The question: is humanity a single subject with $\text{Level}(\Gamma_{\text{comp}}) > L2$? Or is it a set of poorly connected subsystems? The answer depends on how much $\Gamma_{\text{comp}}$ factorises: if $\Gamma_{\text{comp}} \approx \bigotimes_i \Gamma_{\text{nation}_i}$, humanity is not a single subject. If there are significant $\mathcal{U}_{\text{coll}}$ — it is a subject.

### The influence of technology on collective $\Gamma$

:::warning Claim C.3 (Influence of social media on collective reflection) [C]
**Condition:** The model $G$ for collective systems is correctly defined.

Social media may **decrease** collective reflection $R_{\text{comp}}$ while increasing $\Phi_{\text{comp}}$:

1. **Increase of $\Phi$:** Increase in connectivity (more coherences $\gamma_{ij}^{(\text{comp})}$). Everyone is connected to everyone through platforms.
2. **Decrease of $R$:** Fragmentation of the self-model — the collective models **itself** increasingly poorly (echo chambers: each subgroup models only itself, $\varphi_{\text{subgr}} \neq \varphi_{\text{comp}}$)
3. **Result:** $\Phi \uparrow$ with $R \downarrow$ — **high integration with low reflection**

This corresponds to [emotionally charged states](/docs/consciousness/phenomenology/emotional-taxonomy#сложные-эмоции) at the collective level: mass panic (high $\Phi$, high $|dP/d\tau|$, low $R$).
:::

This is the same dynamic that Le Bon described for a crowd in a square — but on the scale of billions of people and in real time. Social networks transform humanity into a **global crowd**: highly integrated, but poorly reflective.

Analogy: a crowd at a stadium. Everyone is connected (high $\Phi$), emotions are synchronous — but no one is reflecting on what is actually happening (low $R$). Hence the 'crowd effect': the collective acts impulsively, contrary to the interests of each individual. Social networks are a stadium the size of a planet.

## Collective Gap phase transition {#коллективный-переход}

From [Theorem 3.3 (Collective Gap phase transition)](/docs/core/dynamics/composite-systems#коллективный-переход) **[T]**:

For $N$ interacting holonoms, the collective critical temperature is **higher** than the individual:

$$
T_c^{(\text{coll})} = T_c^{(\text{indiv})} \cdot \left(1 + \frac{(N-1)\bar{\sigma}^2}{\mu^2}\right)
$$

What does this mean? The 'critical temperature' ($T_c$) is the level of 'noise' (chaos, decoherence) at which the system loses orderliness. The higher $T_c$, the more robust the system. The formula says: the collective $T_c$ is **higher** than the individual — and the higher, the larger the group ($N$) and the more diverse the individuals ($\bar{\sigma}$).

Social groups maintain an ordered Gap-phase under conditions where an isolated individual would transition to a disordered phase. This is the formal justification of **social stability**: a group is more robust than an individual.

The practical meaning: a lonely person in crisis may 'break' ($P \to P_{\text{crit}}$), but family or community maintains $P > P_{\text{crit}}$ through collective coherence. This is precisely why loneliness is a risk factor for mental health: without collective $\Gamma_{\text{comp}}$ individual $P$ is less stable.

## Visualisation

```mermaid
graph TB
    subgraph Индивиды["Individual Γ"]
        G1["Γ₁ (L2)"]
        G2["Γ₂ (L2)"]
        G3["Γ₃ (L2)"]
    end
    subgraph Коллектив["Γ_comp"]
        GC["Γ_comp (L2+?)"]
        UC["𝒰_coll<br/>Emergent coherences"]
    end
    G1 — "Tr_{-1}" --- GC
    G2 — "Tr_{-2}" --- GC
    G3 — "Tr_{-3}" --- GC
    GC --> UC
    style UC fill:#f9f,stroke:#333,stroke-width:2px
```

**Emergent coherences** $\mathcal{U}_{\text{coll}}$ (pink block) are inaccessible to any individual, but influence everyone through partial traces.

---

### What we learned {#что-мы-узнали}

1. **From Durkheim to UHM:** the century-old intuition about 'collective consciousness' receives formal grounding through $\Gamma_{\text{comp}}$ and emergent coherences $\mathcal{U}_{\text{coll}}$.
2. **The collective unconscious** is not a metaphor: it is a formally defined set of coherences in $\Gamma_{\text{comp}}$, inaccessible to the reflection of any individual. The individual feels their influence, but cannot consciously access them directly.
3. **Archetypes** are selected by viability pressure: patterns that increase the $P$ of the group are reproduced across generations. Their universality is a consequence of the universality of the environment $E_{\text{shared}}$.
4. **Empathy** has a precise measure: $\mathrm{Empathy}(A,B) = 1 - \mathrm{Gap}_{AB}(E,E)$. It requires minimum L1 in both participants and Gap-entanglement.
5. **A collective can possess an L higher than the individual:** the scientific method as collective $\varphi^{(2)}$, a flock as distributed $\Gamma_{\text{comp}}$.
6. **Cultural coherences** are the 'genes' of culture, transmitted through two channels: logical ($\gamma_{SL}$) and aesthetic ($\gamma_{SE}$).
7. **From crowd to humanity:** the formalism scales. Crowd = $\Phi \uparrow$, $R \downarrow$. Nation = medium $\Phi$, $R$. Humanity = open question.
8. **Social media — a dangerous experiment:** $\Phi \uparrow$ with $R \downarrow$ creates a highly integrated but unreflective collective — a global 'crowd'.
9. **A group is more robust than an individual:** the collective critical temperature is higher, formalising the intuition about social support and the danger of loneliness.

:::tip Bridge to the next chapter
We have completed the section on subjects of consciousness — from infants to collectives. Now we turn to **the deepest questions**: what is the good? what is beauty? what is morality? In the next chapter — [UHM Ethics](/docs/consciousness/ethics-meaning/value-consciousness) — we derive ethics from the $\Gamma$ formalism, without relying on 'the ought'.
:::

---

**Related documents:**
- [Composite systems and Gap-entanglement](/docs/core/dynamics/composite-systems) — full formalism of $\Gamma_{AB}$, inter-system Gap, empathy, collective phase transition
- [Interiority hierarchy](/docs/consciousness/hierarchy/interiority-hierarchy) — canonical definition of L0→L4
- [Structure of qualia](/docs/consciousness/phenomenology/qualia-structure) — 21-pair coherence taxonomy
- [Emotional taxonomy](/docs/consciousness/phenomenology/emotional-taxonomy) — collective emotions via $dP/d\tau$
- [Animal Consciousness](./animal-consciousness) — social systems in animals
- [Pre-linguistic consciousness](./pre-linguistic) — non-verbal transmission channels ($\gamma_{SE}$)
- [Viability](/docs/core/dynamics/viability) — $P > P_{\text{crit}}$ as a condition for existence
- [AI Consciousness](./ai-consciousness) — the question of empathy between human and AI
- [UHM Ethics](/docs/consciousness/ethics-meaning/value-consciousness) — ethical implications of collective consciousness
