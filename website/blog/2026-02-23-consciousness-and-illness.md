---
slug: consciousness-and-illness
title: "Consciousness, Illness and Geometry: Gap-Profiles of Psychopathologies"
authors: [uhm]
tags: [consciousness, psychopathology, Gap, qualia, Hamming, theory, applications]
---

# Consciousness, Illness and Geometry {#сознание-болезнь-и-геометрия}

Psychiatry is the only area of medicine where a diagnosis is made from a catalog. DSM-5: around three hundred categories, each defined by a list of symptoms. Five out of nine — diagnosis A. Four out of seven, at least two weeks — diagnosis B. This is a conscientious inventory. But an inventory is not a map.

A dentist does not make a diagnosis from a checklist "hurts when eating, avoids cold, worries about teeth." A dentist takes an X-ray. The dentist has a **structure** — anatomy that explains *why* it hurts, not just *what* hurts.

In the [second post](/blog/geometry-of-inner-world) a map of the inner world was drawn: 21 channels of experience, each with a numerical measure of opacity $\mathrm{Gap}(i,j) \in [0,1]$. A minimum of three channels must remain opaque — a theorem [Т], not a recommendation. Now the question: what happens when the **wrong** channels turn out to be opaque? Or when all channels fly open at once?

The answer: what psychiatry describes as a disorder. The difference being that now each disorder has specific coordinates in 21-dimensional space. Below is an attempt to translate psychopathology into the language of geometry. With one caveat: the mathematical framework (Gap-profiles, Hamming bound) consists of theorems [Т] and definitions [О]. The application to clinical categories is **interpretation** [И], requiring empirical verification.

<!-- truncate -->

## Reminder: The Map and Its Coordinates {#напоминание-карта-и-её-координаты}

In the [second post](/blog/geometry-of-inner-world) it was established: any system is described by a coherence matrix $\Gamma$ — a $7 \times 7$ table whose rows and columns correspond to seven dimensions (A — articulation, S — structure, D — dynamics, L — logic, E — interiority, O — ground, U — unity). Each pair of dimensions — one type of experience, in total $\binom{7}{2} = 21$.

Each coherence $\gamma_{ij}$ is a complex number with amplitude $|\gamma_{ij}|$ (connection strength) and phase $\theta_{ij}$. From the phase the **gap measure** is determined [О]:

$$
\mathrm{Gap}(i,j) = |\sin(\theta_{ij})| \in [0,1]
$$

$\mathrm{Gap} = 0$ — channel is fully transparent: the dimensions "see" each other without distortion. $\mathrm{Gap} = 1$ — channel is fully opaque: the connection exists ($|\gamma_{ij}| > 0$), but is hidden from reflection. Intermediate values — partial opacity.

The collection of all 21 values — the **Gap-profile** [О]:

$$
\mathbf{G}(\Gamma) := (\mathrm{Gap}(i,j))_{1 \leq i < j \leq 7} \in [0,1]^{21}
$$

Twenty-one numbers between zero and one. A complete opacity map: which connections in your inner world are "open," which are "closed," and to what extent. Your Gap-profile differs from mine — that is precisely why your inner world is not a copy of mine: the same algebra, the same 21 channels, but different opacity configurations.

The key result of [post 2](/blog/geometry-of-inner-world): at least 3 out of 21 channels **must** maintain non-zero Gap — the Hamming bound, a consequence of code H(7,4) [Т]. Complete transparency is incompatible with error self-correction: to correct failures in self-modeling, the system needs "control" channels not participating in direct experience. This is not a defect — it is an architectural requirement. Three blind spots — the price of error-resistance.

## When the Wrong Doors Close {#когда-закрываются-не-те-двери}

What does "norm" mean? For a conscious (L2) system:

- $P > P_{\text{crit}} = 2/7$ — sufficient coherence for viability [Т]
- $R \geq R_{\text{th}} = 1/3$ — sufficient reflection for self-modeling [Т]
- $\Phi \geq 1$ — coherences dominate over noise [Т] (T-129)
- At least 3 channels with $\mathrm{Gap} > 0$ — Hamming bound [Т]

Which **specific** channels are opaque — varies. The mathematician's brain may have high transparency in channels $(L,E)$ and $(L,D)$, but opacity in $(S,E)$. The dancer's — the opposite. Both are normal. The difference is not pathology, but individual configuration.

Pathology begins when:

1. **Anomalously high Gap** in channels critical for functioning;
2. **Anomalously low Gap** in all channels simultaneously (psychosis); or
3. **Total coherence** $P$ stagnates near threshold $2/7$ (depression).

Below — six patterns. Each — a specific Gap-profile with precise coordinates. All clinical identifications have status **[И]**.

### Alexithymia: "I Feel, But Don't Know What" {#алекситимия}

$$
\mathrm{Gap}(L,E) \to 1, \quad \mathrm{Gap}(A,E) \to 1 \qquad [\mathrm{И}]
$$

Two channels to the E-dimension (interiority) are closed: logic ($L$) cannot process the experience, attention ($A$) cannot notice it. The subject **has** an experience — coherence $|\gamma_{SE}|$ may be high, the body "feels." But to become aware of this feeling and, moreover, to name it in words — impossible.

This explains the alexithymia paradox: a person sincerely says "I feel nothing," while their body shows all the signs of stress. The experience is not absent — it bypasses consciousness and manifests somatically. The connection exists, but the doors are closed.

### Impulsivity: "I Act, But Don't Think" {#импульсивность}

$$
\mathrm{Gap}(L,D) \to 1 \qquad [\mathrm{И}]
$$

The logic-dynamics channel is opaque. Actions ($D$) unfold without logical governance ($L$). Meanwhile $\mathrm{Gap}(D,E)$ may be low: the subject perfectly **feels** the impulse, but cannot **evaluate** it before the action is committed.

A subtlety: coherence $|\gamma_{DL}|$ may be high — the connection between action and logic **exists**. But the phase $\arg(\gamma_{DL}) \approx \pi/2$, meaning maximum gap: $\mathrm{Gap}(L,D) = |\sin(\pi/2)| = 1$. The connection is strong, but purely imaginary — it does not contribute to transparency.

### Existential Crisis: "I Live, But Why?" {#кризис}

$$
\mathrm{Gap}(O,E) \to 1 \qquad [\mathrm{И}]
$$

The ground-interiority channel is opaque. Experience ($E$) is disconnected from ontological ground ($O$). Experiences exist, but are deprived of a deep connection to their source. The subject describes this as "meaninglessness" — and this is the precise word: meaning is literally disconnected.

In the extended version ($\mathrm{Gap}(O,E) \to 1$, $\mathrm{Gap}(O,U) \to 1$) — loss of the ground's connection to both experience and unity: "a world without meaning and without wholeness."

### Dissociation: "This is Happening Not to Me" {#диссоциация}

Dissociation is a splitting **within** the E-dimension [И]. If E is decomposed into subspaces $E = E_1 \oplus E_2$, then the coherences between them are opaque: $\mathrm{Gap}(E_1, E_2) \to 1$. The subject possesses two "islands" of experience, not connected to each other.

In the 7-dimensional model (without subspace decomposition) dissociation manifests as:

$$
\mathrm{Gap}(S,E) \to 1, \quad \mathrm{Gap}(D,E) \approx 0 \qquad \text{(or vice versa)} \quad [\mathrm{И}]
$$

Different aspects of experience — bodily ($S$) and dynamic ($D$) — are isolated from each other through different transparency relative to E. The body "remembers," but the emotion is not experienced; or the emotion exists, but the body "does not participate." "This is happening not to me" — not a metaphor, but a literal description: the structural and experiential components are disconnected.

### Depression: Life at the Threshold {#депрессия}

$$
P \to P_{\text{crit}} + \varepsilon, \quad \frac{dP}{d\tau} \approx 0, \quad \varepsilon \ll 1 \qquad [\mathrm{И}]
$$

Depression is not an anomaly of one channel, but a global state: the system "freezes" just above the viability threshold $P_{\text{crit}} = 2/7$ [Т]. Sufficient coherence for existence, but not enough for development. The rate of change of $P$ is close to zero — no improvement, no deterioration. Stagnation.

Gap-profile in depression [И]:
- $\mathrm{Gap}(D,E)$ elevated — dynamics disconnected from experience (**anhedonia**: actions bring no pleasure)
- $\mathrm{Gap}(D,U)$ elevated — dynamics disconnected from wholeness (**loss of purpose**: actions lead nowhere)
- $R$ may be normal or even **elevated**

The last point deserves explanation. Depressive rumination — obsessive thought loops — is a form of reflection. The subject "looks at the map," but the map does not change. High $R$ with a frozen Gap-profile is like examining a blank wall with a magnifying glass: resolution is perfect, nothing to see. Reflection without dynamics — a trap, not a tool.

In terms of [post 4](/blog/three-forces): in depression the balance of three forces (rotation, dissipation, regeneration) is frozen at a point where all three are nearly compensated near the minimum. The system does not decay — but does not restore either. Thermodynamic stalemate.

### Psychosis: When All Doors Fly Open {#психоз}

$$
\overline{\mathrm{Gap}} \to 0 \quad \text{(step change)}, \quad R \geq R_{\text{th}} \qquad [\mathrm{И}]
$$

Psychosis is the complete opposite of alexithymia. Not one channel is closed — **all** channels fly open simultaneously. The boundaries between dimensions dissolve. Reflection is preserved ($R \geq 1/3$): the subject does not lose the ability to self-model, but the model ceases to be error-resistant.

Here a single **theorem** [Т] of the clinical section comes into play:

:::note Theorem T-90 (Structural vs. Functional Loss) [Т]
The Hamming bound is a **structural** property of code H(7,4): for any L2-system $|\{(i,j): \mathrm{Gap}(i,j) > 0\}| \geq 3$. This holds **always**, including in psychosis. However, in psychosis fewer than 3 channels maintain $\mathrm{Gap}(i,j) > \varepsilon_{\text{noise}}$: formally the wall exists, functionally — it does not. The Hamming bound guarantees Gap $> 0$, but does not guarantee Gap $> \varepsilon_{\text{noise}}$.
:::

In plain language: a minimum of three "walls" must mathematically exist — this is proved. But in psychosis they thin down to noise level: formally the wall stands, functionally — it is gone. The system loses error-resistance in self-modeling. Everything is connected to everything — but the connection does not generate understanding, it generates chaos.

The contrast with meditative samadhi is instructive: there too $\overline{\mathrm{Gap}} \to \min$, but **controllably**, through $\varphi$-optimization, with preservation of the functional Hamming bound. Psychosis is an uncontrolled leap through a bifurcation, without preparation and without error-resistance. All doors open — but the meditator worked toward this for years, while in psychosis the doors were knocked out.

## Summary Table of Pathologies {#сводная-таблица-патологий}

| Pathology | Key channels | $\overline{\mathrm{Gap}}$ | $P$ | $R$ |
|-----------|:------------:|:-------------------------:|:---:|:---:|
| **Alexithymia** | Gap(L,E)↑, Gap(A,E)↑ | Moderate | Normal | Normal |
| **Impulsivity** | Gap(L,D)↑ | Moderate | Normal | Reduced |
| **Exist. crisis** | Gap(O,E)↑, Gap(O,U)↑ | Elevated | Reduced | Normal/↑ |
| **Dissociation** | Gap within E-sector | High | Normal | Normal |
| **Depression** | Gap(D,E)↑, Gap(D,U)↑ | Elevated | $\to 2/7$ | Normal/↑ |
| **Psychosis** | All Gap↓ (step) | $\to 0$ | Varies | Normal |

Six pathologies — six distinguishable patterns, each with specific coordinates. DSM describes each with a separate symptom list; a Gap-profile describes each as a point in the same 21-dimensional space [И].

## What Freud and Jung Saw {#что-видели-фрейд-и-юнг}

Classical psychoanalytic concepts receive precise coordinates [И]:

| Concept | Author | Gap-formulation |
|---------|--------|----------------|
| **Repression** | Freud | $\mathrm{Gap}(L,E) \to 1$ — logic has no access to experience |
| **Shadow** | Jung | $\mathrm{Gap}(A,E) \to 1$ — attention does not "see" certain experiences |
| **Unconscious** | Freud, Jung | $\mathcal{U}(\Gamma) = \{(i,j): \mathrm{Gap}(i,j) \to 1,\; R_{ij} < R_{\text{th}}\}$ |

The unconscious is not a "repository" and not a "place." It is a Gap-structure [О]: channels with high Gap and low channel-specific reflection $R_{ij}$. The connection exists ($|\gamma_{ij}| > 0$) — it is real and influences behavior. But it is opaque to self-modeling. This explains Freudian slips and Jungian projections through one mechanism: coherence manifests in actions, but does not enter the self-model $\varphi(\Gamma)$.

Repression differs from shadow in its **channel**: in repression the path from experience to **logic** is closed (I feel, but cannot understand), in shadow — to **attention** (I don't even notice that I feel). This is precisely the distinction Freud and Jung described qualitatively — and the Gap-profile expresses quantitatively.

## Therapy as Changing the Map {#терапия-как-изменение-карты}

If each pathology is a deformation of the Gap-profile, then therapy is a targeted change of specific coordinates [И]:

| Channel for correction | Therapeutic approach | Goal |
|------------------------|---------------------|------|
| Gap(L,E)↓ | CBT, psychoanalysis | Understanding experiences through verbalization |
| Gap(A,E)↓ | Mindfulness, Gestalt | Noticing experiences through attention |
| Gap(S,E)↓ | Body-oriented therapy | Somatic awareness |
| Gap(D,E)↓ | Expressive therapy | Restoration of affective contact |
| Gap(O,E)↓ | Existential therapy | Restoration of connection with ground |
| Gap(L,D)↓ | Behavioral therapy | Logical control of impulses |

Two limitations:

**Lower bound.** By the theorem on the [Hamming bound](/docs/consciousness/hierarchy/gap-characterization#граница-хэмминга) [Т]: even ideal therapy cannot lead to $\overline{\mathrm{Gap}} = 0$. At least 3 channels out of 21 maintain non-zero Gap. The goal is not elimination of all gaps, but **redistribution** of opacity from pathological channels to structurally necessary "control" ones.

**Upper bound.** The therapeutic trajectory must maintain $P > 2/7$ and $R \geq 1/3$ throughout [И]. One cannot "disassemble" the system to its foundation and then reassemble it — along the way it may cross the viability threshold.

Therapy rate:

$$
\tau_{\text{exit}} \propto \tau_{\text{mem}} \cdot \max_{(i,j) \in \text{path}} \mathrm{Gap}(i,j) \qquad [\mathrm{И}]
$$

The longer the system's memory ($\tau_{\text{mem}}$) and the deeper the opacity — the longer the therapy. Childhood trauma (large $\tau_{\text{mem}}$, high Gap) corrects more slowly than recent stress (small $\tau_{\text{mem}}$, moderate Gap). This is not a discovery — every therapist knows this intuitively. But the difference between intuition and formula is the same as between "hurts when eating" and an X-ray.

## Status Table {#таблица-статусов}

As always — honest about what is proved and what is not:

| Result | Status | Comment |
|--------|:------:|---------|
| Gap-profile $\mathbf{G} \in [0,1]^{21}$ | [О] | Definition by convention |
| Hamming bound: $\geq 3$ channels with Gap $> 0$ | [Т] | Consequence of H(7,4) |
| T-90: structural vs. functional loss | [Т] | Sol.79 — Gap $> 0$ does not guarantee Gap $> \varepsilon_{\text{noise}}$ |
| Gap injection of levels L0–L4 | [Т] | Different levels → distinguishable profiles |
| Alexithymia = Gap(L,E)↑ + Gap(A,E)↑ | [И] | Clinical identification |
| Impulsivity = Gap(L,D)↑ | [И] | Clinical identification |
| Existential crisis = Gap(O,E)↑ | [И] | Clinical identification |
| Dissociation = splitting within E | [И] | Clinical identification |
| Depression = stagnation near $P_{\text{crit}}$ | [И] | Clinical identification |
| Psychosis = global Gap-reduction | [И] | Clinical identification |
| Therapy = targeted Gap-correction | [И] | Operationalization |
| Repression = Gap(L,E) → 1 | [И] | Psychoanalytic identification |
| Shadow = Gap(A,E) → 1 | [И] | Psychoanalytic identification |

## Conclusions {#выводы}

**1. Mental disorder is not a broken mechanism, but a deformed map.** Each pathology is a specific configuration of the 21-dimensional Gap-profile: certain channels are anomalously opaque or anomalously transparent. Not "chemical imbalance" (too coarse) and not "cognitive distortion" (too narrow) — but a geometric structure with precise coordinates. Definitions — [О]; identification with clinical categories — [И].

**2. The unconscious is not a place, but a Gap-structure.** Freud and Jung described repression and shadow qualitatively: something is hidden, something is invisible. The Gap-profile gives coordinates: repression — closed channel $(L,E)$, shadow — closed channel $(A,E)$. Coherence does not disappear — it manifests in behavior, but is opaque to self-modeling [И].

**3. Therapy is not "working on yourself in general," but changing specific coordinates.** CBT reduces Gap(L,E). Mindfulness — Gap(A,E). Body therapy — Gap(S,E). Each approach has a target in 21-dimensional space. The goal is not zero Gap (impossible by theorem [Т] and dangerous for error-resistance), but redistribution of opacity from pathological channels to structurally necessary ones [И].

**4. Depression is stagnation, not "bad mood."** The system freezes at the viability threshold $P_{\text{crit}} = 2/7$ [Т]: sufficient coherence to exist, not enough to develop. Rumination — high reflection with a frozen profile: a magnifying glass directed at a blank wall. From [post 4](/blog/three-forces): the three forces of the evolution equation are frozen at a stalemate point [И].

**5. Psychosis and meditation are topological neighbors.** Both states are characterized by global Gap reduction. The difference — in the way of reaching it: controlled $\varphi$-optimization vs. uncontrolled bifurcation — and in the preservation of the functional Hamming bound. Theorem T-90 [Т] formalizes this distinction: the structural Hamming bound is not violated in either case, but the functional one — is violated in psychosis. All doors open — but the meditator worked toward this for years, while in psychosis the doors were knocked out.

**6. One algebra — from particles to pathologies.** The Fano plane organizes 21 types of experience ([post 2](/blog/geometry-of-inner-world)), defines three particle generations ([post 6](/blog/three-generations)), sets 3+1 spacetime dimensions ([post 5](/blog/spacetime-dimensions)). Now — describes pathologies of consciousness. One mathematical object applied to physics, phenomenology, and clinic. Particle physics and psychopathology — two consequences of one algebra. Different scale, one structure.

Mathematics, as usual, does not ask for permission. But sometimes — it makes a diagnosis.

---

**Related materials:**
- [Holonomic Paninteriorism](/blog/holonomic-paninteriorism) — UHM philosophical position
- [Geometry of the Inner World](/blog/geometry-of-inner-world) — 21 types of experience and Hamming code
- [Three Forces, One Equation](/blog/three-forces) — dynamics and balance of forces
- [Why Space is Three-Dimensional](/blog/spacetime-dimensions) — the same Fano structure in geometry
- [Why There Are Exactly Three Particle Generations](/blog/three-generations) — the same algebra in particle physics
- [Pathology of consciousness](/docs/consciousness/states/pathological) — full formalism
- [Gap characterization of levels](/docs/consciousness/hierarchy/gap-characterization) — normal profiles L0–L4
- [Gap-structure of the unconscious](/docs/consciousness/states/unconscious) — definition of opaque sectors
