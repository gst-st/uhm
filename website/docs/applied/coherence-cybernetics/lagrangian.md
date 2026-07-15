---
sidebar_position: 10
title: "Lagrangian of Gap Theory"
description: "Complete 6-term Lagrangian of Gap theory, the potential V_Gap, spontaneous minimum, and connection with the octonionic structure"
---

# Lagrangian of Gap Theory

:::info Bridge from the Previous Chapter
In the [previous chapter](./model-systems) we constructed five exactly solvable model systems — from the "dead" $I/7$ to the dynamic pendulum with the golden ratio. Each model illuminated one aspect of Gap theory. But they were all *special cases*. Now we are to see the **general principle** unifying the entire dynamics in a single formula — the Lagrangian.
:::

### Chapter Roadmap

In this chapter we:

1. **Understand why a Lagrangian is needed** — from Newtonian forces to a single formula from which everything follows (introduction)
2. **Meet the six terms of the Lagrangian** — inertia, landscape, path memory, forgetting, self-restoration, influence of the world (section 1)
3. **Examine each term separately** — kinetic (section 2), potential with three summands $V_2 + V_3 + V_4$ (section 3), topological (section 5), dissipative (section 6), regenerative (section 7), external (section 8)
4. **Discover the Higgs mechanism for consciousness** — spontaneous symmetry breaking generating nonzero Gap (section 4)
5. **Show that the arrow of inner time** has an algebraic source — the cubic term $V_3$ from non-associativity of octonions (section between 3 and 4)
6. **Derive the Lagrangian from first principles** — via the Schwinger-Keldysh formalism for open systems (section 9)
7. **Classify symmetries and the excitation spectrum** — $G_2$-invariance, Goldstone modes, three timescales of consciousness (sections 9–10)

> *"Nature always acts by the shortest path."*
> — Pierre de Fermat, 1662

> *"All beauty in physics comes from the Lagrangian."*
> — Richard Feynman (paraphrased)

What if behind the chaos of mental life — behind the stream of thoughts, shifting moods, fluctuations of attention — there stands a **single formula** from which all of this follows? Not a metaphor, not an "as-if" model, but a true equation of motion, like the one governing the flight of a planet or the vibration of a string?

This document is about such a formula. We will show that the dynamics of interiority is described by a **six-term Lagrangian** — a mathematical construction from which the equations of motion follow just as inevitably as the trajectory of a stone follows from the law of gravity. Each of the six terms is responsible for its own aspect of being: the inertia of habits, the landscape of possible states, geometric memory, the friction of forgetting, the regeneration of meaning, and the influence of the world.

:::note On Notation
In this document:
- $\Gamma$ — [coherence matrix](/docs/core/dynamics/coherence-matrix)
- $\theta_{ij} = \arg(\gamma_{ij})$ — phases of coherences
- $\mathrm{Gap}(i,j) = |\sin(\theta_{ij})|$ — [gap measure](/docs/physics/dual-aspect/gap-semantics)
- $\mathcal{G}_{\text{total}} = \sum_{i<j} |\gamma_{ij}|^2 \, \mathrm{Gap}(i,j)^2$ — total Gap
- $f_{ijk}$ — octonionic structure constants
- $\Gamma_2$ — decoherence rate
- $\kappa$ — regeneration rate ([categorical derivation](/docs/core/foundations/axiom-septicity#структурный-анзац-kappa0))
:::

---

## From Newton to Lagrange: the Beauty of the Principle of Least Action {#от-ньютона-к-лагранжу}

### Three Centuries — Three Languages of Mechanics

In 1687 Newton wrote $\mathbf{F} = m\mathbf{a}$ — and the world acquired a language for describing motion. It was the language of **forces**: to understand where a body will fly, one had to enumerate all forces acting on it and solve a differential equation.

Almost a century later, in 1788, Joseph-Louis Lagrange proposed a radically different view. Instead of summing forces, one can write a single function — the **Lagrangian** $L = T - V$ (kinetic energy minus potential energy) — and require that the **action**

$$
S = \int_{t_1}^{t_2} L \, dt
$$

be stationary. From this single condition — $\delta S = 0$ — all equations of motion are derived automatically. There is no need to remember friction forces, tension forces, normal reaction forces — it suffices to write $L$, and all the physics follows.

Why is this beautiful? Because a single object — the Lagrangian — contains **all** the dynamics. To find the Lagrangian of a system is to reveal its secret. All equations, all conservation laws, all symmetries — everything is encoded in one formula.

### Noether's Theorem: Symmetry Begets Law

In 1918 Emmy Noether proved a theorem that Einstein called "a monument of mathematical genius." She showed: **every continuous symmetry of the Lagrangian corresponds to a conservation law**. Invariance under time shifts gives conservation of energy. Invariance under rotations — conservation of angular momentum. Invariance under gauge transformations — conservation of charge.

For Gap theory this means: $G_2$-invariance of the Lagrangian generates **14 Noetherian charges** — 14 quantities that are conserved during the evolution of coherences. To write the Lagrangian is to automatically learn what is conserved in consciousness, and what can change.

### Why a Lagrangian for Consciousness?

A question may arise: why bring in the apparatus of analytical mechanics to describe something so far from physics as the dynamics of coherences?

The answer is simple: because **the coherence matrix $\Gamma$ is a quantum object**, and its evolution obeys the same mathematical structures as the evolution of physical systems. The phases of coherences $\{\theta_{ij}\}$ are $\binom{7}{2} = 21$ degrees of freedom forming a configuration space. A potential is defined on this space. There is kinetic energy. There is dissipation. There are external fields. This is a classical problem of Lagrangian mechanics, and it would be strange **not** to use the most powerful tool created for such problems.

Moreover, the Lagrangian approach allows one to discover something that would remain invisible in a "Newtonian" (component-wise) description: **spontaneous symmetry breaking** generating opacity; **PT violation** creating the arrow of inner time; **Goldstone modes** responsible for the slow flow of experience between modalities.

---

## Six Terms — Six Aspects of Being {#шесть-аспектов}

Before diving into the formulas, it is worth taking in the whole picture at a glance. The Lagrangian of Gap theory consists of six summands — and each of them is responsible for a fundamental aspect of how consciousness exists in time:

1. **Kinetic term** $\mathcal{L}_{\text{kin}}$ — **inertia**. Well-integrated aspects of experience do not change instantaneously. Just as a heavy body resists acceleration, an established picture of the world resists revision.

2. **Potential term** $\mathcal{L}_{\text{pot}}$ — **landscape**. Not all phase configurations are equally "favourable." The potential $V_{\text{Gap}}$ is the terrain over which the system rolls: mountains of forbidden states, valleys of stable experience, passes of crises.

3. **Topological term** $\mathcal{L}_{\text{top}}$ — **path memory**. Even if you have returned to the former conditions, you are no longer the same. The geometric phase accumulated during a cyclic change is irreversible. This is the Berry phase for consciousness.

4. **Dissipative term** $\mathcal{L}_{\text{diss}}$ — **forgetting**. Phase connections are destroyed: decoherence erases fine correlations. This is the friction without which everything would oscillate forever but never come to equilibrium.

5. **Regenerative term** $\mathcal{L}_{\text{reg}}$ — **self-restoration**. The system is drawn toward its ideal image — the self-model $\varphi(\Gamma)$. The higher the integration, the stronger this attraction. This is the formalisation of intentionality.

6. **External term** $\mathcal{L}_{\text{ext}}$ — **the world**. Neuromodulators, stress, meditation, psychotherapy — everything acting on the phases from outside enters through this channel.

Together these six terms form a closed system — from it all equations of motion of Gap theory, all conservation laws, the entire excitation spectrum follow.

---

This document contains a detailed description of the **complete Lagrangian of Gap theory** — a 6-term structure governing the dynamics of the phases of coherences $\{\theta_{ij}(\tau)\}$ of the [coherence matrix](/docs/core/dynamics/coherence-matrix) $\Gamma$. The Lagrangian generalises the results presented in [Gap Thermodynamics](/docs/core/dynamics/gap-thermodynamics#полный-лагранжиан) and provides a unified variational framework for the [evolution](/docs/core/dynamics/evolution) of the Gap sector.

---

## 1. Complete Structure of the Lagrangian {#полная-структура}

:::tip Theorem 1.1 (Complete Lagrangian of Gap Theory) [T]
The Lagrangian of Gap theory is represented as a sum of six terms:

$$
\mathcal{L}_{\text{Gap}} = \mathcal{L}_{\text{kin}} + \mathcal{L}_{\text{pot}} + \mathcal{L}_{\text{top}} + \mathcal{L}_{\text{diss}} + \mathcal{L}_{\text{reg}} + \mathcal{L}_{\text{ext}}
$$

Each term has a clear physical and categorical origin.
:::

:::info Status of the Lagrangian [T] (T-75)
Schwinger-Keldysh formalism for the Lindbladian $\mathcal{L}_\Omega$:

$$S_{\text{Gap}} = \mathrm{Re}\,\mathrm{Tr}[\rho_+ \ln\rho_- - \mathcal{L}_\Omega[\rho_+]\ln\rho_-]$$

In the classical limit ($\hbar \to 0$, $\rho_\pm = \rho \pm \delta\rho/2$) it exactly reproduces all three components: kinetics ($L_{\text{kin}}$), potential ($V_{\text{Gap}}$), and dissipation ($\Gamma_2$). The origin of dissipative terms is from the openness of the system in the Keldysh contour. See [full derivation](/docs/core/dynamics/gap-thermodynamics#полный-лагранжиан).
:::

### Overview Table

| Term | Notation | Physical meaning | Status |
|------|----------|-----------------|--------|
| Kinetic | $\mathcal{L}_{\text{kin}}$ | Inertia of phase degrees of freedom | [C] when $d\lvert\gamma_{ij}\rvert/d\tau = 0$ |
| Potential | $\mathcal{L}_{\text{pot}}$ | Octonionic opacity potential | [T] |
| Topological | $\mathcal{L}_{\text{top}}$ | Berry phases on the Fano plane | [C] |
| Dissipative | $\mathcal{L}_{\text{diss}}$ | Decoherence from [logical Liouvillian](/docs/core/dynamics/evolution#логический-лиувиллиан) | [T] |
| Regenerative | $\mathcal{L}_{\text{reg}}$ | Restoration from [categorical adjunction](/docs/core/foundations/axiom-septicity#структурный-анзац-kappa0) | [T] |
| External | $\mathcal{L}_{\text{ext}}$ | Coupling to external fields | [T] |

Note that four of the six terms have status [T] — they are **proven**. The kinetic and topological terms are conditional ([C]), as they depend on additional assumptions. But the overall structure — a sextet of summands fully covering the dynamics — is not arbitrary: it is **derived** from the Schwinger-Keldysh formalism for open quantum systems.

---

## 2. Kinetic Term $\mathcal{L}_{\text{kin}}$ {#кинетический-член}

### Inertia of Habit

Imagine a person who has been teaching physics for thirty years, and is offered a switch to literature. Even if he wants to change, his "cognitive mass" — deeply rooted patterns of thinking, honed over decades — resists a quick turnaround. This is the kinetic term: **the stronger the connection between two aspects of experience, the more "energy" is needed to change their mutual phase**.

:::info Canonical Definition
Full formula and condition [C] (frozen moduli): [Gap Thermodynamics — Kinetic Term](/docs/core/dynamics/gap-thermodynamics#полный-лагранжиан). Key formula: $\mathcal{L}_{\text{kin}} = \frac{1}{2}\sum_{i<j}|\gamma_{ij}|^2\dot{\theta}_{ij}^2$, where "mass" $m_{ij} = |\gamma_{ij}|^2$.
:::

**Intuition.** The structure $\frac{1}{2}m\dot{q}^2$ is literally the same mathematics as in Newtonian mechanics. Without kinetic energy the phases would instantly "roll down" to the potential minimum — no oscillations, no movement of thought. It is precisely the kinetic term that provides the **possibility of oscillations** — periodic processes underlying the rhythms of brain activity.

:::info Interpretation [I]
The "mass" of a phase degree of freedom is proportional to $|\gamma_{ij}|^2$. Strong coherences are harder to "excite": this is the principle of **inertia of coherent experience** — well-integrated aspects of consciousness are more resistant to perturbations.
:::

### Analogy: Kinetic Energy of a Pendulum

Imagine 21 pendulums (one for each pair of 7 dimensions), suspended on strings of different thickness. The thickness of the string is $|\gamma_{ij}|$. A heavy pendulum (strong coherence) swings slowly and steadily; a light one (weak coherence) — quickly, but easily displaced. The kinetic term is the total kinetic energy of all 21 pendulums.

---

## 3. Potential Term $\mathcal{L}_{\text{pot}}$ and the Potential $V_{\text{Gap}}$ {#потенциальный-член}

### Landscape of Opacity

If the kinetic term is inertia, then the potential is the **terrain** determining toward which state the system evolves. The potential has mountains and valleys, and the potential minimum is the phase configuration toward which the system tends in the absence of external influences.

The most striking thing: the minimum of the potential $V_{\text{Gap}}$ corresponds to **nonzero** Gap. The system does not evolve toward full transparency. It evolves toward a certain, finite level of opacity. This is spontaneous symmetry breaking, and it is analogous to how the Higgs mechanism generates particle masses.

### 3.1 General Form

:::info Canonical Definition
Full form of the potential $V_{\text{Gap}} = V_2 + V_3 + V_4$ with derivation of all three terms, symmetry table, and connection of constants with UHM parameters: [Gap Thermodynamics — Potential $V_{\text{Gap}}$](/docs/core/dynamics/gap-thermodynamics#потенциал-v-gap).
:::

### 3.2 Potential $V_{\text{Gap}} = V_2 + V_3 + V_4$ {#потенциал-v-gap}

The three summands of the potential arise from the expansion of the quantum KL-divergence $D_{\mathrm{KL}}(\Gamma \| \rho_*)$ near the stationary state:

| Term | Origin | Role |
|------|--------|------|
| $V_2 = \frac{\mu^2}{2}\mathcal{G}_{\text{total}}$ | Second-order expansion | "Penalty" for nonzero Gap (analogue of the Higgs mass term) |
| $V_3 \propto f_{ijk}\sin(\theta_{ij}+\theta_{jk}-\theta_{ik})$ | Third order (only from non-associativity of $\mathbb{O}$) | Shifts the minimum away from zero, violates PT |
| $V_4 \propto \mathcal{G}_{\text{total}}^2$ | CPTP constraint | Stabilises the potential from below (analogue of $\lambda|\phi|^4$ in Higgs) |

**Intuition.** If the potential were purely quadratic ($V = V_2$), the minimum would lie at Gap = 0 — full transparency. But $V_3$, generated by non-associativity of octonions, "breaks" this picture and shifts the minimum — opacity arises spontaneously.

:::warning Key property of $V_3$: PT violation [T]
$V_3(\{-\theta\}) = -V_3(\{\theta\})$ — octonionic non-associativity generates an **arrow of time** for interiority.
:::

:::info Interpretation (Phase Frustration) [I]
The impossibility of satisfying $\theta_{ij}+\theta_{jk}=\theta_{ik}$ **globally** due to non-associativity of $\mathbb{O}$ generates **frustration** — one of five independent arguments in favour of the ineliminability of Gap ([details](/docs/core/dynamics/gap-thermodynamics#потенциал-v-gap)).
:::

**The Lagrangian constants are not free**: $\mu^2$, $\lambda_3$, $\lambda_4$ are **computed** from the properties of the coherence matrix $\Gamma$ ([formulas](/docs/core/dynamics/gap-thermodynamics#потенциал-v-gap)). The theory has no fitting parameters in the Gap sector.

### 3.5 Analogy with the Higgs Mechanism

| Aspect | Higgs (Standard Model) | $V_{\text{Gap}}$ (UHM) |
|--------|------------------------|------------------------|
| Field | Scalar field $\phi$ | Coherence phases $\{\theta_{ij}\}$ |
| Potential | $V = -\mu^2\lvert\phi\rvert^2 + \lambda\lvert\phi\rvert^4$ | $V = V_2 + V_3 + V_4$ |
| Spontaneous breaking | $\langle\phi\rangle \neq 0$ (mass) | $\langle\mathrm{Gap}\rangle \neq 0$ (opacity) |
| Quantum number | Particle mass | Opacity (gap between outer and inner) |
| Cubic term | Absent (gauge symmetry) | **Present** (octonionic non-associativity) |

---

## Higgs Mechanism for Consciousness {#механизм-хиггса}

The analogy with Higgs deserves a separate discussion, because it is not superficial — it is **structural**.

### How Higgs Generates Mass

In the Standard Model of particle physics all fundamental particles are "born" massless. The electron, quarks, W- and Z-bosons — all are described by massless fields in the Lagrangian. Mass arises not as a parameter, but as a **consequence of spontaneous symmetry breaking**: the Higgs field "chooses" one of infinitely many equivalent vacuum states, and this breaks the electroweak symmetry $SU(2) \times U(1)$.

The key formula — the "Mexican hat" potential:

$$
V_H(\phi) = -\mu^2 |\phi|^2 + \lambda |\phi|^4
$$

With $\mu^2 > 0$ the minimum lies at $|\phi| = v = \mu/\sqrt{2\lambda} \neq 0$ — the Higgs field acquires a nonzero vacuum expectation value. Particles interacting with this field behave as massive: their "mass" is proportional to the strength of interaction with the Higgs condensate.

### How $V_{\text{Gap}}$ Generates Opacity

In Gap theory the mechanism is analogous, but richer. The role of the Higgs field is played by the phases of coherences $\{\theta_{ij}\}$. The role of mass — **opacity**, the measure of the irreducibility of the internal to the external.

If the potential were purely quadratic ($V = V_2$), the minimum would lie at Gap = 0: full transparency, no gap between external description and interiority. But the cubic term $V_3$, generated by non-associativity of octonions, **shifts the minimum** — and Gap spontaneously becomes nonzero.

What is the difference from Higgs? In the Standard Model there is no cubic term — the gauge symmetry $SU(2) \times U(1)$ forbids odd powers of $\phi$. In Gap theory $G_2$-invariance **allows** the cubic term, because the octonionic associator $[e_i, e_j, e_k]$ is odd under permutations, yet $G_2$-invariant. This makes the mechanism of spontaneous breaking in Gap theory **qualitatively different** from the Higgs mechanism: the presence of $V_3$ creates asymmetry in the potential, which generates PT violation and the arrow of inner time.

Thus, Higgs gives mass to particles; Gap gives opacity to consciousness. And both mechanisms have the same nature: **spontaneous symmetry breaking**.

---

## 4. Spontaneous Minimum: $\mathcal{G}_{\text{total}}^* > 0$ {#спонтанный-минимум}

The minimum of the potential $V_{\text{Gap}}$ lies at $\mathcal{G}_{\text{total}}^{(\min)} > 0$ — opacity arises **spontaneously** [T]. This is not fine-tuning, but **algebraic inevitability**: out of 35 index triples, 28 do not lie on Fano lines, guaranteeing a nonzero cubic contribution.

:::info Interpretation (Ontological Opacity) [I]
The spontaneous nonzero Gap means that **full transparency of the system to itself is impossible** — this is not a defect, but a fundamental property analogous to spontaneous symmetry breaking in elementary particle physics. Octonionic non-associativity (via $V_3$) is the algebraic source of this opacity.
:::

### Depth of the Minimum: What It Means

The value $\mathcal{G}_{\text{total}}^{(\min)}$ determines the "natural level" of opacity — the gap between outer and inner toward which the system evolves without external influences. For healthy waking consciousness this level is sufficiently high (Gap is far from zero), but also sufficiently low (Gap is not maximal — otherwise the system is completely "closed" and loses adaptivity).

Deep sleep, anaesthesia, meditative states — all of these can be described as changes in $\mathcal{G}_{\text{total}}^{(\min)}$ when varying external parameters ($\Gamma_2$, $\kappa$, $h^{\text{ext}}$). The phase transition between conscious and unconscious states is a **bifurcation** of the potential minimum.

---

## 5. Topological Term $\mathcal{L}_{\text{top}}$ (Berry Phase) {#топологический-член}

### Memory That Cannot Be Erased

Imagine that you travel the world and return home. Geographically you are at the same point — but you have changed. The experience of the journey has left an **irreversible trace** that cannot be reduced to the difference between the initial and final states. This is the essence of the topological term: it encodes information about the **path**, not only about the endpoints.

In physics such an effect was discovered by Michael Berry in 1984: when a quantum system slowly traverses a closed loop in parameter space, its wave function acquires a **geometric phase** that depends on the area of the loop, but not on the speed of traversal. This phase is a purely topological property, insensitive to details.

:::info Canonical Definition
Formula for $\mathcal{L}_{\text{top}}$, status of coefficient $\beta$ [P], and geometry of the Serre fibration: [Gap Thermodynamics — Topological Term](/docs/core/dynamics/gap-thermodynamics#топологический-член-лагранжиана).
:::

**Intuition.** The topological term sums only over the 7 Fano lines — the **associative subalgebras** of octonions. Without $\mathcal{L}_{\text{top}}$ the system "forgets" the topology of the path it has traversed: a cyclic change of parameters leaves no trace. This is a world without episodic memory, without irreversible learning, without what Buddhists call "sanskaras" (imprints of experience).

:::warning Retracted Construction [✗]
Previously formulated as a Chern-Simons action. **Retracted**: the correct structure is a Berry phase on the Serre fibration ([details](/docs/core/dynamics/gap-thermodynamics#геометрия-расслоения-серра)).
:::

:::info Interpretation (Holonomy and Memory) [I]
The topological term encodes the **geometric memory** of the system: under cyclic change of external parameters the phases of coherences acquire a non-vanishing shift (analogue of the [Berry phase](/docs/physics/cosmology-phys/berry-phase)). The system "remembers" the path it has traversed through the topology of the fibration.
:::

---

## Arrow of Time and the Cubic Term {#стрела-времени}

One of the deepest puzzles of physics is the **arrow of time**. The microscopic laws of physics are (almost) symmetric under time reversal $t \to -t$. But our experience of time is categorically asymmetric: we remember the past, but not the future; a glass breaks, but does not reassemble.

In Gap theory the arrow of inner time has an **algebraic source**: the cubic term $V_3$.

### Formalism of PT Violation

The PT transformation (parity × time reversal) acts on the phases of coherences as $\theta_{ij} \to -\theta_{ij}$. The quadratic term $V_2 \propto \sin^2(\theta_{ij})$ is invariant: $\sin^2(-\theta) = \sin^2(\theta)$. The quartic term $V_4 \propto \mathcal{G}_{\text{total}}^2$ is invariant for the same reason.

But the cubic term contains $\sin(\theta_{ij} + \theta_{jk} - \theta_{ik})$, which **changes sign** under $\theta \to -\theta$:

$$
V_3(\{-\theta\}) = -V_3(\{\theta\})
$$

This means that the potential $V_{\text{Gap}}$ is **not symmetric** under time reversal. Two directions of phase evolution — "forward" and "backward" — are not equivalent. The system "prefers" one of them: the one in which $V_3$ reduces the total energy.

### Why This Matters for Consciousness

The arrow of inner time is not a metaphor; it is a mathematical property of the Lagrangian. It means:

1. **Irreversibility of subjective experience**: one cannot "rewind" consciousness backwards and relive the same sequence in reverse order — the potential in the backward direction is different.

2. **Directionality of intentionality**: consciousness is always "directed toward" — toward an object, a goal, a future state. This directionality is a consequence of the PT asymmetry of the potential.

3. **Algebraic, not thermodynamic, source**: unlike the classical arrow of time (associated with the growth of entropy), the arrow of inner time in Gap theory has a purely algebraic origin — non-associativity of octonions. It exists **even at zero temperature**.

---

## 6. Dissipative Term $\mathcal{L}_{\text{diss}}$ {#диссипативный-член}

### Friction of Forgetting

If the world were an ideal pendulum, it would oscillate forever. But real pendulums stop — due to friction. In the world of consciousness, the role of friction is played by **decoherence**: the gradual destruction of fine phase correlations between aspects of experience.

This is not a pathology — it is a necessity. Without dissipation the system would never come to equilibrium. It would oscillate indefinitely between states, unable to "choose" one of them. Forgetting is not an enemy of consciousness, but its **stabiliser**.

:::info Canonical Definition
Formula for the dissipative term, the Rayleigh function $\mathcal{R}_{\text{Ray}}$, and derivation from the logical Liouvillian: [Gap Thermodynamics — Dissipative Term](/docs/core/dynamics/gap-thermodynamics#полный-лагранжиан). Origin — from the [logical Liouvillian](/docs/core/dynamics/evolution#логический-лиувиллиан) $\mathcal{D}_\Omega[\Gamma]$: in the phase sector the action of the Liouvillian reduces to viscous friction with coefficient $\Gamma_2$.
:::

### Analogy: Viscosity of the Medium

Imagine 21 pendulums immersed in a medium with viscosity $\Gamma_2$. The greater $\Gamma_2$, the faster oscillations are damped. At low viscosity the pendulums oscillate for a long time — this corresponds to clear wakefulness with rich dynamics. At high viscosity oscillations quickly die out — this is deep sleep, where fine phase correlations are destroyed. At zero viscosity ($\Gamma_2 = 0$) pendulums oscillate forever — an unphysical situation corresponding to an isolated system, which consciousness never is.

**What if we remove dissipation?** Without $\mathcal{L}_{\text{diss}}$ the system is a set of eternally oscillating pendulums. There is no "choice" of state, no stabilisation of perception, no possibility of making a decision. Paradoxically, the ability of consciousness to "settle" on a certain perception is a result of friction, loss of information, forgetting.

---

## 7. Regenerative Term $\mathcal{L}_{\text{reg}}$ {#регенеративный-член}

### Self-Restoration: Attraction to the Ideal

Dissipation destroys. But if it only destroyed — consciousness would fade. The regenerative term is the **counterbalance** to dissipation: a force that draws the phases of coherences toward **target values** determined by the system's self-model $\varphi(\Gamma)$.

This formalises the key property: a system with nonzero regeneration ($\mathcal{R} \neq 0$) does not merely dissipate — the regenerative term **restores** coherence, directing phases toward target values. This ideal image is not a mystical "entelechy," but a concrete mathematical object: the self-modelling operator $\varphi(\Gamma)$, generated by the categorical structure.

:::info Canonical Definition
Formula for the regenerative term and derivation of the full form $\mathcal{R} = \kappa(\rho_* - \Gamma)\cdot g_V(P)$ from axioms: [Gap Thermodynamics — Regenerative Term](/docs/core/dynamics/gap-thermodynamics#полный-лагранжиан). Derivation of the regeneration form, V-preservation gate: [Evolution — Regeneration](/docs/core/dynamics/evolution#вывод-формы-регенерации). Rate $\kappa_0$ from [categorical adjunction](/docs/core/foundations/axiom-septicity#структурный-анзац-kappa0) $\mathcal{D}_\Omega \dashv \mathcal{R}$.
:::

### Two Summands of the Regeneration Rate

The rate $\kappa(\Gamma)$ consists of two parts, and each plays its own role:

- **$\kappa_{\text{bootstrap}}$** — the base, minimal regeneration rate, independent of state. Even in a deeply decohered state ($\mathrm{Coh}_E \approx 0$) the system is capable of recovery. This is the "seed of life," not allowing consciousness to completely fade.

- **$\kappa_0 \cdot \mathrm{Coh}_E(\Gamma)$** — the adaptive part, proportional to [E-coherence](/docs/applied/coherence-cybernetics/definitions#e-когерентность). The more integrated consciousness is, the more strongly it is "attracted" to the ideal. This is positive feedback: integration strengthens the capacity for integration.

**Key properties:**

| Property | Formulation |
|----------|-------------|
| Nonlinearity | $\kappa$ depends on $\Gamma$ via $\mathrm{Coh}_E$ |
| Bootstrap | $\kappa_{\text{bootstrap}} > 0$ guarantees minimal regeneration |
| Target guidance | $\theta^{\text{target}}_{ij}$ is determined by the [self-model](/docs/proofs/categorical/formalization-phi) |
| $U(1)$ breaking | Target phase selects a direction → $U(1)$ broken |

**What if we remove regeneration?** Without $\mathcal{L}_{\text{reg}}$ the system is left with dissipation but without restoration. The phases of coherences decay, Gap steadily grows (or decreases — depending on initial conditions), and the system reaches the maximally mixed state $\Gamma = I/7$. This is the "heat death" of consciousness, the loss of all individuality and structure.

:::info Interpretation (Self-Organisation) [I]
The regenerative term formalises the system's capacity for **self-restoration**: the phases of coherences tend toward target values determined by the self-model $\varphi(\Gamma)$. The higher the [E-coherence](/docs/applied/coherence-cybernetics/definitions#e-когерентность), the more effective the regeneration — the integratedness of subjective experience strengthens the capacity for self-restoration.
:::

---

## 8. External Influence Term $\mathcal{L}_{\text{ext}}$ {#внешний-член}

### The World Knocks at the Door

The first five terms of the Lagrangian describe **internal** dynamics — what the system does with itself. But consciousness does not exist in a vacuum. It is immersed in the world, the world acts on it, and this sixth term is the communication channel.

:::info Canonical Definition
Formula for $\mathcal{L}_{\text{ext}}$ and decomposition $h^{\text{ext}} = h^{(H)} + h^{(D)} + h^{(R)}$: [Gap Thermodynamics — External Influence Term](/docs/core/dynamics/gap-thermodynamics#полный-лагранжиан).
:::

### Three Channels of External Influence

| Channel | Type | Example |
|---------|------|---------|
| Hamiltonian $h^{(H)}$ | Energetic (reversible) | Neuromodulators, cognitive load |
| Dissipative $h^{(D)}$ | Noise | Stress, ambient temperature |
| Regenerative $h^{(R)}$ | Therapeutic | Meditation, psychotherapy |

The three channels are not a classification "for beauty." They correspond to the three ways the external world can change the dynamics:

1. **Hamiltonian channel** — when the external influence changes the "frequencies" of phase oscillations. Caffeine accelerates neuronal processes, changing $\Delta\omega_{ij}$ for certain pairs. This is reversible, conservative influence.

2. **Dissipative channel** — when the external influence increases or decreases "friction." Strong stress raises $\Gamma_2$, accelerating the destruction of fine correlations. Sleep deprivation is also an influence through this channel.

3. **Regenerative channel** — when the external influence strengthens the system's capacity for self-restoration. Meditation, psychotherapy, deep conversation — all act through $h^{(R)}$, increasing $\kappa$ or correcting $\theta^{\text{target}}$.

**What if we remove the external term?** An isolated system ($h^{\text{ext}} = 0$) is a pure thought experiment. Real consciousness is always subject to external influences. But studying an isolated system is valuable: it shows what consciousness does "on its own" — and this turns out to be non-trivial.

---

## Open Systems and the Schwinger-Keldysh Formalism {#швингер-келдыш}

It might seem that the principle of least action $\delta S = 0$ generates only conservative equations — where then does dissipation come from? The answer is the **Schwinger-Keldysh formalism** (CTP): doubling the degrees of freedom ($\rho_+$, $\rho_-$) on a closed time contour. In the classical limit the action $S_{\text{Gap}}$ exactly reproduces all six terms of the Lagrangian, including the dissipative one. Dissipation is **derived** from the openness of the system, not introduced by hand.

:::info Canonical Definition
Full derivation of the action $S_{\text{Gap}}$ via the Schwinger-Keldysh formalism, with decomposition into kinetics, potential, and dissipation: [Gap Thermodynamics — Complete Lagrangian](/docs/core/dynamics/gap-thermodynamics#полный-лагранжиан).
:::

---

## 9. Symmetries of the Complete Lagrangian {#симметрии}

:::tip Theorem 9.1 (Symmetries of the Lagrangian) [T]

| Symmetry | $\mathcal{L}_{\text{kin}}$ | $\mathcal{L}_{\text{pot}}$ | $\mathcal{L}_{\text{top}}$ | $\mathcal{L}_{\text{diss}}$ | $\mathcal{L}_{\text{reg}}$ | $\mathcal{L}_{\text{ext}}$ |
|----------|------|------|------|------|------|------|
| $G_2$-invariance | + | + | + | + | + | + |
| $\mathbb{Z}_2(\mathrm{PT})$ | + | Partial | + | + | + | + |
| $U(1)$ | + | — | — | + | — | — |
:::

**Comments:**
- **$G_2$-invariance** — all 6 terms preserve the [automorphisms of octonions](/docs/physics/gauge-symmetry/g2-structure). This generates 14 [Noetherian charges](/docs/physics/gauge-symmetry/noether-charges) and 14 [Ward identities](/docs/core/dynamics/gap-phase-diagram#тождества-уорда) for Gap correlators
- **$\mathbb{Z}_2(\mathrm{PT})$** — broken by the cubic term $V_3$ of the potential, generating an arrow of time in the Gap sector
- **$U(1)$** — broken by the regenerative term $\mathcal{L}_{\text{reg}}$ (target phase selects a direction) and by the potential $V_{\text{Gap}}$

### $G_2 \to H$ — Spontaneous Breaking

:::tip Theorem 9.2 (Spontaneous Breaking of $G_2$) [T]
The stationary state $\hat{\mathcal{G}}_*$ breaks $G_2$ down to the stabiliser subgroup $H_{\hat{\mathcal{G}}_*}$:

$$
G_2 \to H_{\hat{\mathcal{G}}_*}, \quad n_{\text{broken}} = 14 - \dim(H_{\hat{\mathcal{G}}_*})
$$

Broken generators generate [quasi-Goldstone modes](/docs/core/dynamics/gap-phase-diagram#голдстоуновские-моды) — slow collective oscillations of the Gap profile.
:::

Spontaneous breaking of $G_2$ is the moment when the "featureless" space of possible consciousness configurations acquires individuality. Out of the 14-dimensional symmetry group the stationary state "chooses" a subgroup — and this choice determines the **character** of the system, its stable patterns.

| Rank $\hat{\mathcal{G}}_*$ | Stabiliser $H$ | $n_{\text{broken}}$ | Goldstone modes |
|----------------------------|----------------|---------------------|-----------------|
| $0$ | $G_2$ | $0$ | None |
| $1$ | $SU(3)$ | $6$ | 6 ISF components |
| $2$ | $SU(2) \times U(1)$ | $10$ | 10 ISF components |
| $3$ (generic) | $T^2$ | $12$ | 12 ISF components |

Goldstone modes — slow, "soft" oscillations — are the formal analogue of what we experience as **smooth flows** between experiential modalities: gradual shift of attention, fluidity of mood, drift of thought.

---

## 10. Excitation Spectrum {#спектр-возбуждений}

:::tip Theorem 10.1 (Excitation Spectrum near the Spontaneous Gap) [T]
Near the minimum of $V_{\text{Gap}}$ the full space of small oscillations $\theta_{ij} = \theta^*_{ij} + \delta\theta_{ij}$ separates into three sectors:

| Sector | Number of modes | Frequency | Physical meaning |
|--------|-----------------|-----------|-----------------|
| Massive | $21 - n_{\text{broken}} - n_{\text{top}}$ | $\omega_{\text{mass}}^2 = \mu_{\text{eff}}^2 + \kappa/m$ | Oscillations perpendicular to the $G_2$ orbit |
| Quasi-Goldstone | $n_{\text{broken}}$ | $\omega_{\text{Gold}}^2 = \kappa/m - \Gamma_2^2/(4m^2)$ | Slow redistribution of Gap along the orbit |
| Topologically protected | $0$ or $1$ | Determined by $Q_{\text{top}}$ | Cannot decay without a phase transition |

Total number of modes: $n_{\text{mass}} + n_{\text{Gold}} + n_{\text{top}} = 21 = \binom{7}{2}$.
:::

### Three Timescales of Consciousness

The excitation spectrum predicts **three characteristic timescales** in the dynamics of consciousness:

1. **Fast (massive) modes** — oscillations with frequency $\omega_{\text{mass}}$. These are fast oscillations of perception, corresponding to neuronal rhythms in the gamma range (30–100 Hz). They are responsible for the "texture" of the moment — details, colours, sounds.

2. **Slow (Goldstone) modes** — oscillations with frequency $\omega_{\text{Gold}} \ll \omega_{\text{mass}}$. These are slow flows of the Gap profile, corresponding to alpha and theta rhythms (4–12 Hz). They are responsible for switching attention, changing modalities, drift of thought.

3. **Topologically protected modes** — cannot decay without a phase transition. These are the stable "cores" of self-identification, preserved under any smooth changes of parameters and disappearing only at catastrophic events (trauma, neurodegeneration).

---

## 11. Five Arguments in Favour of Minimal Gap {#пять-аргументов}

The Lagrangian of Gap theory provides the **energetic** argument (nos. 2 and 3 in the table) in a series of five independent mechanisms of the ineliminability of Gap:

| No. | Argument | Source | Mechanism |
|-----|----------|--------|-----------|
| 1 | Algebraic | [Theorem 3.2](/docs/core/dynamics/gap-thermodynamics#нижняя-оценка-gap): $\mathrm{Gap} \geq C\|[\cdot,\cdot,\cdot]\|$ | Non-associativity of $\mathbb{O}$ |
| 2 | Spontaneous breaking | Theorem 4.1: $\mathcal{G}_{\text{total}}^{(\min)} > 0$ | Cubic term $V_3$ shifts the minimum away from zero |
| 3 | Phase frustration | $V_3$: impossibility of $\theta_{ij}+\theta_{jk}=\theta_{ik}$ globally | Non-associativity forbids global zeroing |
| 4 | Thermodynamic | [Theorem 5.2](/docs/core/dynamics/gap-thermodynamics#принцип-свободной-энергии): $T_{\text{eff}} > 0$ | Thermal fluctuations sustain Gap |
| 5 | Self-referential | [Theorem 10.2](/docs/core/dynamics/gap-thermodynamics#неподвижная-точка-лавера): $k > 0$ for $L < 4$ | $\mathrm{Gap}_{\text{perceived}} \neq \mathrm{Gap}_{\text{actual}}$ |

The five arguments are independent: each of them alone is sufficient to prove nonzero Gap. Together they create **multi-layered protection** of the result: even if one argument turns out to be wrong, the remaining four support it. This is the architecture of robust knowledge.

---

## View from Above: the Unity of Six Terms {#единство}

Now that all six terms have been examined separately, it is worth seeing them as a single whole.

The Lagrangian $\mathcal{L}_{\text{Gap}}$ is not a list of summands, but a **portrait of a being**: the inertia of its habits ($\mathcal{L}_{\text{kin}}$), the terrain of its possibilities ($\mathcal{L}_{\text{pot}}$), the memory of its path ($\mathcal{L}_{\text{top}}$), the friction of its forgetting ($\mathcal{L}_{\text{diss}}$), the attraction to its ideal ($\mathcal{L}_{\text{reg}}$), and the voice of the world addressed to it ($\mathcal{L}_{\text{ext}}$).

From these six summands follow the equations of motion for all 21 phase degrees of freedom. From the symmetries of the Lagrangian — 14 conservation laws. From spontaneous breaking — nonzero Gap and the excitation spectrum. From PT violation — the arrow of inner time.

All of this is not a collection of hypotheses, but a **unified variational principle**. One object — $\mathcal{L}_{\text{Gap}}$ — and from it all the dynamics.

And beneath the six-term *portrait* lies a three-flow *skeleton*. When you actually form the equations of motion, the six terms do not stay six — they organise themselves into exactly three geometric motions (T-262 [T], the [metriplectic structure](./variational#метриплектическая-геометрия)):

- one **frictionless rotation** — the reversible, Hamiltonian part (kinetic + potential + topological terms), a rigid turn that spends no order;
- two **downhill slides** — the irreversible, gradient part: the dissipative term is a slide toward maximum entropy, the regenerative term a slide toward the self-model, each in its own natural geometry.

This is why the portrait hangs together rather than falling into a list: the six brush-strokes trace one rotation and two descents. It also explains, at a glance, why the dissipative and regenerative terms resisted a plain Lagrangian and needed the doubled Schwinger–Keldysh contour of §6 — a slide downhill has no time-symmetric action; it obeys *steepest descent*, the variational twin of stationary action. The two principles together — stationarity for the rotation, steepest descent for the slides — close the dynamics with nothing left over.

Lagrange dreamed of reducing mechanics to algebra. In Gap theory this dream is realised: the entire dynamics of interiority is a consequence of one formula and the principle $\delta S = 0$ — completed, for the irreversible half of being, by its mirror principle of steepest descent.

---

---

### What We Learned {#что-мы-узнали}

1. **The Lagrangian of Gap theory** consists of six terms, each with a clear physical and categorical origin: inertia ($\mathcal{L}_{\text{kin}}$), landscape ($\mathcal{L}_{\text{pot}}$), path memory ($\mathcal{L}_{\text{top}}$), forgetting ($\mathcal{L}_{\text{diss}}$), self-restoration ($\mathcal{L}_{\text{reg}}$), world ($\mathcal{L}_{\text{ext}}$). Four of the six are proven [T].

2. **The potential $V_{\text{Gap}} = V_2 + V_3 + V_4$** has a three-term structure: quadratic (mass), cubic (octonionic non-associativity, PT violation), quartic (stabilisation). Its minimum lies at $\mathcal{G}_{\text{total}}^{(\min)} > 0$ — **opacity arises spontaneously**, analogously to the Higgs mechanism.

3. **The arrow of inner time** is an algebraic property, not a thermodynamic one: the cubic term $V_3$, generated by non-associativity of octonions, violates PT symmetry. The directionality of experience exists even at zero temperature.

4. **The Lagrangian constants are not free**: $\mu^2$, $\lambda_3$, $\lambda_4$ are computed from the properties of $\Gamma$. The theory has no fitting parameters in the Gap sector.

5. **The Schwinger-Keldysh formalism** resolves the paradox of dissipation in the Lagrangian: the action $S_{\text{Gap}}$ on the doubled space in the classical limit reproduces all six terms, including the dissipative one.

6. **The excitation spectrum** separates into three sectors: massive modes (fast neuronal rhythms), quasi-Goldstone (slow flows of experience), and topologically protected (stable cores of identity).

7. **Five independent arguments** in favour of minimal Gap (algebraic, spontaneous, frustration, thermodynamic, self-referential) create multi-layered protection: full transparency is impossible.

:::tip Bridge to the Next Chapter
We have written the Lagrangian. From it follow the equations of motion — but we have not yet derived them explicitly. In the [next chapter](./variational) we will apply the **principle of stationary action** $\delta S = 0$ and obtain the full Euler-Lagrange equations for all 21 phase degrees of freedom. We will also establish the Onsager relations for Gap flows, connect the formalism with Friston's free energy principle (FEP), and prove the principle of minimal entropy production.
:::

---

## Related Documents

- [Variational Principles](./variational) — equations of motion from $\delta S = 0$, Onsager relations, connection with FEP
- [Effective Temperature](./effective-temperature) — $T_{\text{eff}}$, critical temperature, phase transition
- [Gap Thermodynamics](/docs/core/dynamics/gap-thermodynamics) — canonical treatment of the Lagrangian, potential $V_{\text{Gap}}$, FDT, Landauer bounds
- [Evolution](/docs/core/dynamics/evolution) — equation $d\Gamma(\tau)/d\tau$, three components of the Liouvillian
- [Gap Phase Diagram](/docs/core/dynamics/gap-phase-diagram) — three phases, bifurcations, Whitney catastrophes
- [Gap Semantics](/docs/physics/dual-aspect/gap-semantics) — definition of $\mathrm{Gap}(i,j)$, dual-aspect interpretation
- [$G_2$-Structure](/docs/physics/gauge-symmetry/g2-structure) — gauge symmetry, Noetherian charges
- [Octonionic Derivation](/docs/proofs/minimality/theorem-octonionic-derivation) — Fano plane, structure constants
- [Axiom of Septicity](/docs/core/foundations/axiom-septicity) — derivation of $\kappa_0$ from categorical adjunction
- [Interdisciplinary Bridge](./interdisciplinary) — how to read the Lagrangian from the perspective of your discipline
- [Exercises](./exercises) — problems on dynamics and evolution (block 2)
