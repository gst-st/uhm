---
sidebar_position: 2
title: "The Unconscious"
description: "Gap-structure of the unconscious: definition, theorem on incomplete transparency, Freudian repression, Jungian shadow and dynamics of Gap-reduction"
slug: /consciousness/states/unconscious
---

# The Unconscious

:::info Bridge from the previous chapter
In [Altered States of Consciousness](/docs/consciousness/states/altered-states) we saw how the $\Gamma$-profile deviates from wakefulness during sleep, meditation, and psychedelics. In all these states, part of the coherences remained **opaque** — $\mathrm{Gap}(i,j) \to 1$. Now we ask: what are these opaque channels? Can they become transparent? And why is full transparency **impossible**? The answer: the unconscious is not a 'repository', but the **Gap-structure** of the coherence matrix.
:::

:::note On notation
In this document:
- $\Gamma$ — [coherence matrix](/docs/core/dynamics/coherence-matrix), $\gamma_{ij}$ — its elements
- $\mathrm{Gap}(i,j) = |\sin(\arg(\gamma_{ij}))|$ — [gap measure](/docs/core/dynamics/gap-operator#определение)
- $\hat{\mathcal{G}} \in \mathfrak{so}(7)$ — [Gap-operator](/docs/core/dynamics/gap-operator)
- $R$ — [reflection measure](/docs/consciousness/foundations/self-observation#мера-рефлексии-r)
- $R_{\text{th}} = 1/3$ — [reflection threshold](/docs/consciousness/hierarchy/interiority-hierarchy)
- $\varphi$ — [φ-operator](/docs/core/operators/phi-operator)
- L0–L4 — [levels of interiority](/docs/consciousness/hierarchy/interiority-hierarchy)
- Full notation table — see [Notation](/docs/reference/notation)
:::

:::warning Document status
The definition of the unconscious through Gap-structure — **[D]** (definition by convention). The theorem on incomplete transparency — **[C]** (conditional on the H(7,4) analogy). Identification of psychoanalytic concepts with specific Gap-channels — **[I]** (interpretation).
:::

### Chapter roadmap

1. **Historical perspective** — from Freud through Jung to the cognitive unconscious and UHM
2. **Definition** — the unconscious as the set of channels with high Gap
3. **Theorem on incomplete transparency** — at minimum 3 channels must be opaque
4. **Psychoanalysis as Gap-patterns** — repression, shadow, archetypes
5. **Dynamics** — Gap-reduction and conditions of awareness
6. **How the unconscious manifests** — specific examples of influence on behaviour
7. **Gap-reduction: therapy protocols** — Γ-interpretation of therapeutic approaches
8. **E-sector analysis** — which channels are most significant for phenomenology
9. **Summary table** — the unconscious by levels L0–L4

---

## 1. Historical perspective {#история}

### 1.1 Sigmund Freud: the unconscious as the repressed

The concept of the unconscious was not invented by Freud — philosophers (Leibniz, Schopenhauer, Hartmann) discussed 'unconscious processes' long before psychoanalysis. But it was Freud (1900, *The Interpretation of Dreams*; 1923, *The Ego and the Id*) who made the unconscious the central concept of the science of the psyche.

Freud's **topographic model** (1900):
- **Consciousness** (Bewusstsein) — that which is consciously experienced at any given moment
- **Preconscious** (Vorbewusstes) — that which can become conscious with effort
- **Unconscious** (Unbewusstes) — that which cannot become conscious directly; accessible only through analysis of symptoms, dreams, and slips

Freud's **structural model** (1923):
- **Id** (Es/Id) — drives without direct access to consciousness
- **Ego** (Ich/Ego) — mediator between the Id and reality
- **Superego** (Über-Ich/Superego) — internalised norms

**Key mechanism:** *repression* (Verdrängung) — the active exclusion of content from consciousness. The repressed does not disappear, but continues to influence behaviour through symptoms, slips and dreams.

### 1.2 Carl Jung: the collective unconscious

Jung extended Freud's model by adding the **collective unconscious** — a layer common to all people, containing **archetypes** (Anima/Animus, Shadow, Self, Wise Old Man, etc.). Jung described the **shadow** (Schatten) — the totality of repressed qualities that the subject does not recognise in themselves, but projects onto others.

### 1.3 The cognitive unconscious

In the 1970s–2000s, psychology moved away from Freud's model of 'repression' toward the **cognitive unconscious**: implicit memory (Schacter, 1987), implicit associations (Greenwald and Banaji, 1995), priming, automatic processing (Bargh and Chartrand, 1999). The unconscious became not a 'repository of the repressed', but 'the totality of processes that do not require awareness'.

### 1.4 From classical models to UHM

| Classical model | UHM formalism |
|---------------------|---------------|
| Freud: repression | $\mathrm{Gap}(L,E) \to 1$ — logic-experience channel opaque |
| Jung: shadow | $\mathrm{Gap}(A,E) \to 1$ — attention-experience channel opaque |
| Jung: archetypes | Recurrent patterns in $\Gamma_{\text{comp}}$ |
| Cognitive unconscious | $\gamma_{ij} \neq 0$ with $\mathrm{Gap}(i,j) > 0$ — process active, but opaque |
| Topographic model | Gap gradient: consciousness ($\mathrm{Gap} \approx 0$), preconscious ($0.3 < \mathrm{Gap} < 0.7$), unconscious ($\mathrm{Gap} > 0.7$) |

Key advantage of UHM: a *unified formalism* for all types of unconscious. Freud, Jung, and cognitivists described different phenomena; the Gap-structure formalism unifies them as **different channels** of a single matrix $\Gamma$.

---

The unconscious is not a separate 'region' of the psyche, but the **Gap-structure** of the coherence matrix: the set of coherences $\gamma_{ij}$ that the system **has**, but cannot reflexively access due to high $\mathrm{Gap}(i,j)$.

**Everyday analogy.** Imagine a house with 21 windows (matching the number of coherences $\gamma_{ij}$ in the $7 \times 7$ matrix for $i < j$). Some windows are transparent — through them you see the world (conscious contents). Others are painted over ($\mathrm{Gap} \to 1$) — something is happening behind them, sounds come through, but you cannot see what. The unconscious is not the basement, but the **painted-over windows**. The coherence $\gamma_{ij}$ exists and influences your life (the noise through the glass), but you have no reflexive access to it.

---

## 2. Definition of the unconscious {#определение}

:::info Definition (Unconscious sector) [D]
**Unconscious sector** of a holomn with coherence matrix $\Gamma$ — a subset of coherences:

$$
\mathcal{U}(\Gamma) := \{(i,j) : \mathrm{Gap}(i,j) \to 1 \;\;\text{and}\;\; R_{ij} < R_{\text{th}}\}
$$

where $R_{ij}$ is the partial reflection for channel $(i,j)$:

$$
R_{ij} = 1 - \frac{|\gamma_{ij} - [\varphi(\Gamma)]_{ij}|^2}{|\gamma_{ij}|^2}
$$

The system 'possesses' coherence $\gamma_{ij} \neq 0$ (it is real and influences behaviour), but has **no reflexive access** to it ($R_{ij} < R_{\text{th}}$).
:::

**Motivation for the definition.** Why is the unconscious defined through *two* conditions ($\mathrm{Gap} \to 1$ *and* $R_{ij} < R_{\text{th}}$), and not through one?

- $\mathrm{Gap}(i,j) \to 1$ means that the channel is *opaque*: the phase shift $\arg(\gamma_{ij})$ is close to $\pi/2$, and the 'inner' content of the coherence is inaccessible from 'outside'.
- $R_{ij} < R_{\text{th}}$ means that the self-model $\varphi(\Gamma)$ does not reproduce this coherence: the system 'does not know' about it.
- Both conditions usually correlate (high Gap leads to low partial reflection), but are formally independent: one can have high Gap with high $R_{ij}$ (if the self-model 'knows' about the opacity, but cannot eliminate it).

### 2.1 Key distinction: absence vs. opacity

| Situation | $\gamma_{ij}$ | $\mathrm{Gap}(i,j)$ | Interpretation |
|----------|:-----------:|:------------------:|---------------|
| Coherence absent | $= 0$ | Undefined | Connection does not exist |
| Conscious connection | $\neq 0$ | $\approx 0$ | Connection is conscious |
| **Unconscious connection** | $\neq 0$ | $\approx 1$ | Connection exists, but opaque |
| Preconscious connection | $\neq 0$ | $0.3$–$0.7$ | Connection partially transparent |

The unconscious = **non-zero coherence with maximum Gap**. This fundamentally distinguishes the UHM approach from approaches where the unconscious is a 'storage place'. In UHM there is no 'repository' — there is only the current state $\Gamma$ and its Gap-structure.

**Numerical example.** In a person with alexithymia (inability to recognise one's own emotions): $|\gamma_{DE}| = 0.20$ (strong emotional dynamics — the body responds, the pulse quickens), but $\mathrm{Gap}(D,E) = 0.95$ — near-complete opacity. The emotion *exists* ($\gamma_{DE} \neq 0$), it *influences* behaviour, but is not *consciously experienced*. Compare: in a healthy person $|\gamma_{DE}| = 0.20$, $\mathrm{Gap}(D,E) = 0.15$ — the same intensity, but the channel is transparent, the emotion is experienced consciously.

### 2.2 Gradation of opacity

The unconscious is not a binary property, but a *gradation*. It is useful to introduce three zones:

| Zone | Gap | Name | Accessibility |
|------|:---:|----------|-------------|
| Transparent | $0 \leq \mathrm{Gap} < 0.3$ | Conscious | Full reflexive access |
| Semi-transparent | $0.3 \leq \mathrm{Gap} < 0.7$ | Preconscious | Accessible with directed attention |
| Opaque | $0.7 \leq \mathrm{Gap} \leq 1$ | Unconscious | Inaccessible; influences indirectly |

This gradation corresponds to Freud's topographic model: consciousness ↔ transparent zone, preconscious ↔ semi-transparent, unconscious ↔ opaque. But unlike Freud, the boundaries between zones are *quantitative* (Gap values), not qualitative.

**Numerical example.** For a typical adult (L2), the full Gap-profile of 21 channels may look as follows:

| Zone | Channels | Example |
|------|:------:|--------|
| Transparent ($\mathrm{Gap} < 0.3$) | $\sim 9$ of 21 | $(A,E)$, $(S,E)$, $(L,E)$, $(A,S)$, $(S,D)$, ... |
| Semi-transparent ($0.3$–$0.7$) | $\sim 6$ of 21 | $(D,E)$, $(O,E)$, $(A,U)$, ... |
| Opaque ($\mathrm{Gap} > 0.7$) | $\sim 6$ of 21 | $(O,U)$, $(L,U)$, $(D,U)$, ... |

---

## 3. Theorem on incomplete transparency {#теорема-неполная-прозрачность}

:::tip Theorem 1.1 (Incomplete transparency) [C]
Condition: analogy with [Hamming code H(7,4)](/docs/core/dynamics/gap-dynamics#код-хэмминга), [Hamming bound](/docs/consciousness/hierarchy/gap-characterization#граница-хэмминга).

For any system of level L2 or above:

$$
|\mathcal{U}(\Gamma)| \geq 3
$$

i.e. **at minimum three** out of 21 coherence channels must have $\mathrm{Gap} > 0$.

**Corollary:** Every conscious being **inevitably** has an unconscious. Full transparency ($\mathrm{Gap} = 0$ for all 21 channels) is incompatible with the noise immunity of self-modelling.

**Argument.** By the [Hamming bound for Gap](/docs/consciousness/hierarchy/gap-characterization#граница-хэмминга-подробно), the code H(7,4) with parameters $[n=7, k=4, d=3]$ requires at minimum $d = 3$ 'check' channels with non-zero Gap for detecting and correcting errors of self-modelling. If all channels had $\mathrm{Gap} = 0$, the operator $\varphi$ would become the identity, and correction of misalignments would become impossible.

**Step-by-step derivation:**
1. Self-modelling $\varphi: \Gamma \to \varphi(\Gamma)$ — a mapping that brings the system closer to self-knowledge.
2. For error correction it is necessary to *detect* the misalignment between $\Gamma$ and $\varphi(\Gamma)$.
3. Detection requires 'check channels' — the analogue of check bits in the Hamming code.
4. The code H(7,4) encodes 4 information bits using 3 check bits, providing correction of 1 error (distance $d = 3$).
5. Analogously: out of 7 dimensions, 4 are 'information' and 3 are 'check', requiring $\geq 3$ channels with non-zero Gap.
6. Consequently, $|\mathcal{U}(\Gamma)| \geq 3$. $\square$
:::

:::info Interpretation [I]
The unconscious is not a defect, but a **structural necessity**. Just as check bits in the Hamming code ensure the integrity of information, so non-zero Gap in the 'check' channels ensures the integrity of self-modelling. Consciousness is possible precisely because part of the coherences remains opaque.

**Analogy.** The body's immune system cannot be fully 'transparent' to the organism — otherwise it would lose the ability to distinguish 'self' from 'other'. Likewise, consciousness cannot be fully transparent to itself — certain 'check' channels *must* remain opaque, so that the system $\varphi$ can detect and correct errors. This is a deep and perhaps counterintuitive result: the unconscious does not impede consciousness, but **makes it possible**.

Another analogy: a mirror cannot reflect itself. For self-reflection, a *second* mirror is needed. Analogously, consciousness cannot fully 'see' itself: opaque channels are needed, playing the role of the 'second mirror' — providing feedback for correction.
:::

**Numerical example: the Hamming bound in practice.** The most 'transparent' person at level L4 (transient samādhi): out of 21 channels, 18 have $\mathrm{Gap} < 0.1$ (nearly transparent), but 3 channels retain $\mathrm{Gap} \geq 0.15$. These 3 channels — the minimally necessary unconscious. Which channels specifically turn out to be 'check' ones depends on the individual configuration of $\Gamma$, but their count $\geq 3$ is an invariant.

---

## 4. Psychoanalytic concepts as Gap-patterns {#психоанализ}

### 4.1 Freudian repression {#вытеснение}

:::info Definition (Repression) [I]
**Repression** — a state in which the logic–experience channel is opaque:

$$
\text{Repression:} \quad \mathrm{Gap}(L,E) \to 1
$$

Logic ($L$) cannot 'reach' experience ($E$): rational analysis has no access to the experience. At the same time $|\gamma_{LE}| > 0$ — the connection **exists** and manifests in behaviour (slips, symptoms), but is opaque to reflection.
:::

Additional feature: $\mathrm{Gap}(A,E)$ may be low — the subject **notices** experiences (the attention–experience channel is transparent), but cannot **understand** them (the logic–experience channel is opaque).

**Numerical example (detailed).** Patient with repressed childhood trauma:

| Channel | $|\gamma_{ij}|$ | $\mathrm{Gap}(i,j)$ | $R_{ij}$ | Interpretation |
|-------|:---:|:---:|:---:|:---|
| $(L,E)$ | $0.15$ | $0.92$ | $0.08$ | Logic–experience connection: strong, fully opaque |
| $(A,E)$ | $0.12$ | $0.25$ | $0.60$ | Attention–experience connection: notices anxiety |
| $(D,E)$ | $0.18$ | $0.30$ | $0.45$ | Dynamics–experience connection: body reacts, partially aware |
| $(S,E)$ | $0.10$ | $0.20$ | $0.55$ | Structure–experience connection: bodily sensations accessible |

The subject *notices* anxiety ($\gamma_{AE}$ works — $\mathrm{Gap} = 0.25$), *feels* it in the body ($\gamma_{DE}$ — $\mathrm{Gap} = 0.30$), but does not *understand* its cause ($\gamma_{LE}$ blocked — $\mathrm{Gap} = 0.92$). To the question 'what do you feel?' the subject answers: 'anxious' (channel $A \to E$), 'heart is pounding' (channel $D \to E$), but to the question 'why?' — 'I don't know' (channel $L \to E$ is opaque).

In psychotherapy (CBT, psychoanalysis) the goal is to reduce $\mathrm{Gap}(L,E)$ to values $\sim 0.2$–$0.3$. For more detail — see [Pathology of consciousness](/docs/consciousness/states/pathological#коррекция).

### 4.2 Jungian shadow {#тень}

:::info Definition (Shadow) [I]
**Shadow** — a state in which the attention–experience channel is opaque:

$$
\text{Shadow:} \quad \mathrm{Gap}(A,E) \to 1
$$

Attention ($A$) cannot 'see' certain experiences ($E$). Unlike repression, here the experience itself remains **unnoticed** — the subject not only does not understand, but does not see.
:::

**Mechanism of projection.** When $\mathrm{Gap}(A,E) \to 1$, one's own experience $\gamma_{AE}$ is inaccessible to attention. But coherence $\gamma_{AE} \neq 0$ — it *exists* and seeks an 'outlet'. This outlet is projection: the subject 'sees' in others what they cannot see in themselves. Formally: coherence is redirected from channel $(A,E)_{\text{self}}$ to channel $(A,E)_{\text{other}}$ via the [composite system](/docs/core/dynamics/composite-systems).

### 4.3 Distinction between repression and shadow

| Characteristic | Repression (Freud) | Shadow (Jung) |
|----------------|:-------------------:|:----------:|
| Key channel | $\mathrm{Gap}(L,E) \to 1$ | $\mathrm{Gap}(A,E) \to 1$ |
| Does subject notice the experience? | Yes ($\mathrm{Gap}(A,E)$ is low) | No ($\mathrm{Gap}(A,E)$ is high) |
| Does subject understand the experience? | No ($\mathrm{Gap}(L,E)$ is high) | Not applicable |
| Manifestation | Slips, symptoms | Projection onto others |
| Example | 'I feel anxious, but I don't know why' | 'He is aggressive' (not noticing one's own aggression) |
| Therapeutic approach | CBT, psychoanalysis (verbalisation) | Jungian analysis, gestalt (awareness) |

**Analogy.** Repression — you see a stain on the wall, but cannot understand what it is (the 'I see' channel works, the 'I understand' channel is blocked). Shadow — you do not see the stain at all, although it influences you (both channels are blocked, but projection onto others — 'it is *he* who is dirty!' — betrays the existence of the connection $\gamma_{AE} \neq 0$).

### 4.4 Jungian archetypes {#архетипы}

:::info Definition (Archetype) [I]
**Archetype** — a recurrent pattern in [the composite coherence matrix](/docs/core/dynamics/composite-systems) $\Gamma_{\text{comp}}$ that increases [viability](/docs/core/dynamics/viability) $P$ for an arbitrary observer:

$$
\text{Archetype } \alpha: \quad \Delta P(\Gamma_{\text{obs}} | \alpha) > 0 \quad \forall\, \Gamma_{\text{obs}} \in \mathcal{D}_{\text{L2}}
$$

Archetypes are structural regularities selected by [evolutionary dynamics](/docs/core/dynamics/evolution) through the viability criterion. They exist not 'in' the individual unconscious, but in the space of $\Gamma_{\text{comp}}$ — composite systems.
:::

**Motivation.** Why are archetypes *universal* (Jung insisted on this)? In the UHM formalism the answer is simple: an archetype is a pattern $\alpha$ in $\Gamma_{\text{comp}}$ that raises $P$ for *any* observer of level L2. If an archetype raised $P$ only for some observers, it would not be universal. The condition $\forall\, \Gamma_{\text{obs}} \in \mathcal{D}_{\text{L2}}$ is the mathematical expression of Jung's 'collectivity'.

**Numerical example.** The archetype of the 'Mother': pattern $\alpha_M$ in $\Gamma_{\text{comp}}$, characterised by strengthening of coherences $(S,E)$ and $(D,E)$ (care = structure–experience connection + dynamics–experience connection). For any L2 observer, contact with this pattern raises $P$ by $\Delta P \approx 0.01$–$0.03$ (subjectively: a sense of security and acceptance). This is precisely why the image of the 'Mother' is present in all cultures — it *objectively* increases viability.

---

## 5. Dynamics of the unconscious {#динамика}

### 5.1 Reduction of Gap

The boundary between conscious and unconscious is **movable**. Gap can decrease under certain conditions:

$$
\frac{d\,\mathrm{Gap}(i,j)}{d\tau} = -\kappa_{\text{red}} \cdot f(R, \Phi, |\gamma_{ij}|) + \eta(\tau)
$$

where:
- $\kappa_{\text{red}}$ — rate of Gap-reduction (depends on the intensity of therapy / practice)
- $f(R, \Phi, |\gamma_{ij}|)$ — a function of the system state: the higher $R$ and $\Phi$, the easier it is to reduce Gap
- $\eta(\tau)$ — stochastic noise (random fluctuations)

The full Gap dynamics is described in [Gap-dynamics](/docs/core/dynamics/gap-dynamics).

### 5.2 Conditions for Gap-reduction

:::tip Theorem 2.1 (Conditions for Gap-reduction) [C]
Condition: [non-Markovian Gap dynamics](/docs/core/dynamics/gap-dynamics#немарковские-эффекты). The channel $(i,j) \in \mathcal{U}(\Gamma)$ transitions from unconscious to conscious ($\mathrm{Gap}(i,j) \to 0$) when:

**(a)** $R > R_{\text{th}}/2$ — minimal reflexive capacity preserved (the system is not fully decohered)

**(b)** $|\gamma_{ij}| > \varepsilon_{\min}$ — coherence is sufficiently strong to be 'captured' by the $\varphi$-operator

**(c)** $\exists\, k: \mathrm{Gap}(i,k) < 1$ and $\mathrm{Gap}(k,j) < 1$ — there exists a 'bridge' channel $k$ through which transparency can 'propagate'
:::

**Let us examine each condition:**

**(a) Minimal reflection ($R > R_{\text{th}}/2 = 1/6 \approx 0.167$).** If $R$ is below this threshold, the self-model $\varphi(\Gamma)$ is so inaccurate that it cannot detect misalignment in channel $(i,j)$. Gap-reduction is impossible — the system 'does not know what it does not know'. This explains why under deep anaesthesia ($R \approx 0.02$) or severe psychosis ($R$ unstable) Gap-reduction does not occur.

**(b) Sufficient coherence ($|\gamma_{ij}| > \varepsilon_{\min}$).** If coherence $\gamma_{ij}$ is too weak, the operator $\varphi$ cannot 'distinguish' it against the background noise. Formally: the signal-to-noise ratio $|\gamma_{ij}|^2 / \sigma^2_{\text{noise}}$ must exceed the detection threshold. At $|\gamma_{ij}| < \varepsilon_{\min}$, content has been lost through [kernel decoherence](/docs/consciousness/states/attention-memory#забывание) — this is no longer unconscious, but *forgotten*.

**(c) 'Bridge' channel.** This is the most non-trivial condition. Direct reduction of $\mathrm{Gap}(i,j)$ at very high Gap is difficult. But if there exists an intermediate dimension $k$ through which transparency can 'propagate', the task is simplified.

**Numerical example: 'bridge' channel in action.**

Situation: $\mathrm{Gap}(D,E) = 0.95$ (emotions are unconscious). Direct reduction is difficult — Gap is too high.

Step 1: we check for the presence of a 'bridge'. $\mathrm{Gap}(D,S) = 0.20$ (dynamics–structure connection is transparent) and $\mathrm{Gap}(S,E) = 0.30$ (structure–experience connection is also transparent). Bridge $S$ exists.

Step 2: through 'bridge' $S$, transparency propagates:
- $\tau = 0$: Gap(D,E) = 0.95, Gap(D,S) = 0.20, Gap(S,E) = 0.30
- $\tau = 10$ sessions: Gap(D,E) = 0.70, Gap(D,S) = 0.18, Gap(S,E) = 0.25
- $\tau = 30$ sessions: Gap(D,E) = 0.40, Gap(D,S) = 0.15, Gap(S,E) = 0.20

Mechanism: first the subject becomes aware of bodily sensations ($S$) associated with emotions ($D$) — 'when I feel anxious, my neck tenses'. Then, through the body channel, the emotions themselves ($E$) become conscious — 'this tension = anxiety'. This very mechanism underlies body-oriented therapy. For more detail — see [Pathology of consciousness](/docs/consciousness/states/pathological#коррекция).

### 5.3 Contexts of Gap-reduction

| Context | Mechanism | Target channels | Speed |
|----------|----------|----------------|:--------:|
| Psychotherapy | Verbalisation — $\mathrm{Gap}(L,E) \downarrow$ | $(L,E)$, $(A,E)$ | Months |
| Crisis | Forced reorganisation ([bifurcation](/docs/core/dynamics/gap-dynamics#бифуркации)) | Globally | Days |
| Development | Gradual $\varphi$-optimisation | All channels | Years |
| Meditation | Voluntary Gap observation — [transparency jump](/docs/consciousness/states/altered-states#медитация) | E-sector | Weeks |
| Psychedelics | Global $\overline{\mathrm{Gap}} \downarrow$ at $R \downarrow$ | All (transient) | Hours |

### 5.4 Non-Markovian memory effects

In Gap-reduction, [non-Markovian effects](/docs/applied/coherence-cybernetics/non-markovian) are essential: the memory kernel $K(\tau - s)$ determines how much past states influence current dynamics. Unconscious contents with a long history ($\tau_{\text{mem}} \gg 1$) require more time for integration:

$$
\tau_{\text{integ}} \propto \tau_{\text{mem}} \cdot \mathrm{Gap}_{\text{init}}
$$

**Numerical example: therapy duration.**

| Type of content | $\tau_{\text{mem}}$ | $\mathrm{Gap}_{\text{init}}$ | $\tau_{\text{integ}}$ | Real analogue |
|----------------|:---:|:---:|:---:|:---|
| Recent conflict | 2 weeks | $0.60$ | $\propto 1.2$ | 5–10 CBT sessions |
| Adolescent trauma | 10 years | $0.80$ | $\propto 8.0$ | 1–2 years of psychotherapy |
| Early childhood trauma | 25 years | $0.95$ | $\propto 23.75$ | 3–5 years of psychoanalysis |

**Analogy.** The longer the window was painted over ($\tau_{\text{mem}}$) and the thicker the layer ($\mathrm{Gap}$), the longer it takes to clean. Trauma from early childhood ($\tau_{\text{mem}} \sim$ decades) with deep repression ($\mathrm{Gap} \approx 0.95$) will require significantly more therapeutic effort than a recent conflict ($\tau_{\text{mem}} \sim$ weeks) with moderate repression ($\mathrm{Gap} \approx 0.60$). For more on types of memory — see [Attention and Memory](/docs/consciousness/states/attention-memory#память); on [CC theorems](/docs/applied/coherence-cybernetics/theorems) — in the section on non-Markovian dynamics.

---

## 6. How the unconscious manifests in behaviour {#проявления}

Unconscious coherences ($\gamma_{ij} \neq 0$ at $\mathrm{Gap}(i,j) \to 1$) are *not* inert — they actively influence the dynamics of $\Gamma$ and, consequently, behaviour. Let us examine specific mechanisms.

### 6.1 Slips of the tongue (Freudian slips)

**Mechanism.** The repressed coherence $\gamma_{LE}$ ($\mathrm{Gap}(L,E) \to 1$) momentarily 'breaks through' the Gap barrier through a stochastic fluctuation $\eta(\tau)$:

$$
\mathrm{Gap}(L,E; \tau_{\text{slip}}) = \mathrm{Gap}_0 - |\eta(\tau_{\text{slip}})| < \mathrm{Gap}_0
$$

For a moment logic 'sees' experience — and this manifests as an uncontrolled utterance.

**Numerical example.** Baseline level: $\mathrm{Gap}(L,E) = 0.90$. Fluctuation: $|\eta| = 0.25$. At the moment of the slip: $\mathrm{Gap} = 0.65$ — a brief transition into the semi-transparent zone. Duration: $\Delta\tau \sim 0.1$ s — sufficient for one word, but not for reflection.

### 6.2 Somatisation

**Mechanism.** With $\mathrm{Gap}(L,E) \to 1$ and $\mathrm{Gap}(A,E) \to 1$ (alexithymia), the emotional coherence $\gamma_{DE}$ has no 'outlet' through consciousness. But the channel $(D,S)$ can be transparent — dynamics influences structure (the body). Result: 'the body carries what consciousness cannot carry'.

**Numerical example.** Patient with chronic back pain without organic cause:
- $|\gamma_{DE}| = 0.22$ (strong hidden emotion)
- $\mathrm{Gap}(D,E) = 0.93$ (emotion is unconscious)
- $\mathrm{Gap}(D,S) = 0.15$ (dynamics→structure channel is transparent)
- Result: emotion is 'translated' into a somatic symptom through the transparent channel $(D,S)$

### 6.3 Projection

**Mechanism.** With $\mathrm{Gap}(A,E) \to 1$ (shadow), one's own coherence $\gamma_{AE}$ is inaccessible to attention. But in a [composite system](/docs/core/dynamics/composite-systems), coherence can be 'transferred' to another: $\gamma_{AE}^{\text{self}} \to \gamma_{AE}^{\text{other}}$. The subject 'sees' in the other what they cannot see in themselves.

**Example.** A person with unconscious aggression ($|\gamma_{DE}^{\text{self}}| = 0.20$, $\mathrm{Gap}(A,E)^{\text{self}} = 0.92$): does not notice their own anger, but is convinced that a colleague is 'hostile' ($\mathrm{Gap}(A,E)^{\text{other}} = 0.15$ — sees the other's aggression perfectly well).

### 6.4 Dreams

**Mechanism.** During [REM sleep](/docs/consciousness/states/altered-states#rem), $\mathrm{Gap}(A,E) \to 1$ (attention is switched off), but $\mathrm{Gap}(S,E) \downarrow$ (structure–experience is transparent). Unconscious contents 'emerge' through channel $(S,E)$ in the form of images, bypassing the critical control of $(L,E)$ and $(A,E)$.

Freud was right that dreams are the 'royal road to the unconscious'. In UHM terms: REM is a state in which E-sector Gaps are redistributed, giving unconscious coherences a temporary 'outlet' through the imagery channel.

---

## 7. Gap-reduction: therapy protocols and their Γ-interpretation {#терапия}

### 7.1 Cognitive-behavioural therapy (CBT)

**Target channel:** Gap(L,E) — logic–experience.

**Mechanism.** CBT systematically trains the connection between thought ($L$) and experience ($E$): the patient learns to *name* and *evaluate* their experiences.

**Γ-trajectory:**
- Start: $\mathrm{Gap}(L,E) = 0.85$
- Thought diary (2 weeks): $\mathrm{Gap}(L,E) = 0.70$ — the patient begins to identify the connection 'event → thought → emotion'
- Cognitive restructuring (2 months): $\mathrm{Gap}(L,E) = 0.45$ — alternative interpretations
- Consolidation (6 months): $\mathrm{Gap}(L,E) = 0.25$ — new Gap-profile stabilises

### 7.2 Psychoanalysis

**Target channels:** Gap(L,E) and Gap(A,E) — through free associations and transference.

**Mechanism.** Psychoanalysis uses the 'bridge' mechanism: the analyst 'mirrors' the patient's unconscious coherences, creating a temporary transparent channel via the [composite system](/docs/core/dynamics/composite-systems) 'patient–analyst'.

**Γ-trajectory:** slow (years), but deep — not only the Gap-profile is restructured, but also $H_{\text{eff}}$ ([procedural memory](/docs/consciousness/states/attention-memory#память)).

### 7.3 Body-oriented therapy

**Target channel:** Gap(S,E) — structure–experience, with 'bridge' through channel $(D,S)$.

**Mechanism.** The patient learns to become aware of bodily sensations ($S$) associated with emotions ($D$), and through the body — to become aware of the emotions themselves ($E$). The classic 'bridge' mechanism (section 5.2).

### 7.4 Mindfulness practices

**Target channel:** Gap(A,E) — attention–experience.

**Mechanism.** Systematic direction of attention ($A$) to current experience ($E$) reduces Gap(A,E). This is the formalisation of [shamatha](/docs/consciousness/states/altered-states#шаматха) and [vipassanā](/docs/consciousness/states/altered-states#випассана) in a therapeutic context.

---

## 8. Structure of the unconscious: E-sector analysis {#e-сектор}

Most significant for the phenomenology of the unconscious are the channels associated with the E-dimension ([E-sector Gap-vector](/docs/consciousness/hierarchy/gap-characterization#e-секторные)):

| Channel | $\mathrm{Gap}(X,E) \to 1$ | What is unconscious | Example of manifestation | Therapeutic approach |
|-------|:-------------------------:|---------------------|:---|:---|
| $(S,E)$ | Structure opaque to experience | Bodily sensations | Does not feel pain until injury | Body therapy |
| $(D,E)$ | Dynamics opaque to experience | Emotions | Somatisation | Expressive therapy |
| $(A,E)$ | Attention does not reach experience | Experiences in general | Projection, 'blind spots' | Mindfulness |
| $(L,E)$ | Logic does not reach experience | Meaning of experiences | Slips, symptoms | CBT, psychoanalysis |
| $(O,E)$ | Ground opaque to experience | Deep presence | Existential emptiness | Existential therapy |
| $(U,E)$ | Unity opaque to experience | Wholeness | Sense of fragmentation | Integrative therapy |

---

## 9. Summary table: the unconscious by levels {#сводная-таблица}

| Level | $\lvert\mathcal{U}\rvert$ (number of unconscious channels) | Character of the unconscious | Example |
|---------|:---------------------------------------:|--------------------------|--------|
| **L0** | $\approx 21$ (all) | Everything opaque; no reflection | Stone, thermostat |
| **L1** | $18$–$20$ | One or two E-channels partially transparent | Amoeba, insect |
| **L2** | $10$–$15$ | E-sector channels partially transparent; others opaque | Typical human |
| **L3** | $5$–$10$ | Most channels transparent; residual unconscious | Experienced meditator |
| **L4** | $\geq 3$ (Hamming bound) | Minimal unconscious, structurally necessary | Samādhi (transient) |

**Numerical example (detailed).** A typical adult (L2): $|\mathcal{U}| \approx 12$. Out of 21 channels:
- ~9 transparent ($\mathrm{Gap} < 0.3$): main E-sector channels and connections between 'adjacent' dimensions
- ~6 semi-transparent ($0.3 < \mathrm{Gap} < 0.7$): peripheral connections, accessible with effort
- ~6 opaque ($\mathrm{Gap} > 0.7$): deep connections (O- and U-sector), early patterns

Even in the most 'enlightened' being (L4, samādhi) — at minimum 3 channels with $\mathrm{Gap} > 0$. The difference between L2 and L4 is not in the *presence* of the unconscious (both have it), but in its *volume*: 12 channels in a typical L2 vs. 3 channels in L4.

---

### What we learned {#итоги}

1. **Historical line**: Freud (repression) → Jung (shadow, archetypes) → cognitive unconscious → UHM (Gap-structure) — a unified formalism for all types of unconscious
2. **The unconscious** = the set of channels $(i,j)$ with $\mathrm{Gap}(i,j) \to 1$ and $R_{ij} < R_{\text{th}}$ — not a repository, but the *opacity* of existing coherences
3. **Theorem on incomplete transparency** [C]: at minimum 3 out of 21 channels must have $\mathrm{Gap} > 0$ — the unconscious is **ineliminable** and **structurally necessary**
4. **Repression** (Freud) = $\mathrm{Gap}(L,E) \to 1$; **shadow** (Jung) = $\mathrm{Gap}(A,E) \to 1$ — precise Gap-differentiation
5. Gap-reduction requires: (a) $R > R_{\text{th}}/2$, (b) $|\gamma_{ij}| > \varepsilon_{\min}$, (c) existence of a 'bridge' channel
6. **Manifestations**: slips of the tongue (Gap fluctuation), somatisation (redirection through transparent channel), projection (transfer to other in composite system), dreams (REM redistribution of Gap)
7. Non-Markovian effects determine integration time: $\tau_{\text{integ}} \propto \tau_{\text{mem}} \cdot \mathrm{Gap}_{\text{init}}$
8. **Therapy** = targeted Gap-reduction in specific channels: CBT → Gap(L,E), mindfulness → Gap(A,E), body therapy → Gap(S,E)

:::tip Bridge to the next chapter
The unconscious is a static picture of opaque channels. But how does the system govern *which* channels are transparent? The answer — through **attention** (redistribution of coherence) and **memory** (the non-Markovian kernel). In the next chapter — [Attention and Memory](/docs/consciousness/states/attention-memory) — we will show that attention = a 'spotlight' in the A-sector, and memory = the form of the kernel $K(\tau)$.
:::

## Connections

- **Gap-operator:** [Definition and properties](/docs/core/dynamics/gap-operator) — canonical definition of $\hat{\mathcal{G}}$
- **Gap-characterisation:** [Gap-characterisation of levels](/docs/consciousness/hierarchy/gap-characterization) — E-sector signatures
- **Gap-dynamics:** [Bifurcations and non-Markovian effects](/docs/core/dynamics/gap-dynamics) — equations of Gap-evolution
- **Gap-diagnostics:** [Applied Gap-diagnostics](/docs/applied/research/gap-diagnostics) — diagnostic patterns
- **Pathology:** [Pathology of consciousness](/docs/consciousness/states/pathological) — pathological Gap-profiles
- **Altered states:** [ASC](/docs/consciousness/states/altered-states) — Gap dynamics in ASC
- **Composite systems:** [Composite systems](/docs/core/dynamics/composite-systems) — archetypes in $\Gamma_{\text{comp}}$
- **CC Theorems:** [Coherence Cybernetics](/docs/applied/coherence-cybernetics/theorems) — non-Markovian dynamics and Gap-patterns
