---
slug: freedom-theorem
title: "Freedom of Will: A Theorem, not a Discussion"
authors: [uhm]
tags: [philosophy, freedom, infinity-categories, homotopy, consciousness, ethics]
---

# Freedom of Will: A Theorem, not a Discussion {#свобода-воли-теорема-а-не-дискуссия}

Twenty-five centuries of philosophers have debated free will. The result: two camps, both wrong.

Determinists say: everything is predetermined, freedom is an illusion. Libertarians (not those ones) say: freedom is real, but it cannot be explained. Compatibilists try to sit on two chairs and say: freedom is compatible with determinism, if one defines the terms correctly. Laplace is satisfied. Sartre is offended. Hume shrugs.

The problem is not in the answers — the problem is in the question. "Is the will free?" is a question that cannot be answered "yes" or "no" without saying something foolish. Because the answer is a **number**. Freedom is not a yes/no property. It is a measurable quantity taking values from 1 to 7, and here is the formula:

$$
\text{Freedom}(\Gamma) = \dim\ker(\mathcal{H}_\Gamma) + 1
$$

Below — what this means, where it comes from, and why Spinoza was closest.

<!-- truncate -->

## The Trap: A Single Goal {#ловушка-единственная-цель}

In the [previous posts](/blog/holonomic-paninteriorism) it was established: reality is described by an ∞-topos — a single mathematical structure from which everything else is derived. One of the consequences is the existence of a **terminal object** $T$: a global attractor toward which all trajectories converge.

Axiom Ω⁷ states:

$$
\forall \Gamma \in \mathcal{C},\; \exists!\, f : \Gamma \to T
$$

In plain language: for every state $\Gamma$ there exists a **unique** morphism to $T$.

At first glance — a verdict. A single goal, a single path, a single fate. Stone, human, galaxy — everything moves toward $T$, and there is no choice. Determinism, and of the harshest kind: not just "causes determine effects," but "the endpoint is fixed axiomatically."

If this is so, UHM theory sentences free will on the very first page. An agent incapable of choosing is not an agent. Consciousness deprived of choice is a meaningless epiphenomenon. Ethics without alternatives is nonsense.

Fortunately, the verdict is based on a misreading. Quite literally.

## The Rescue: What Does "Unique" Mean {#спасение-что-значит-единственный}

The error lies in the word "unique." More precisely, in *which mathematical context* it is uttered.

### Two Worlds {#два-мира}

In an ordinary (1-)category, morphisms are arrows. They are either equal or distinct. No third option. "A unique morphism $f: \Gamma \to T$" means literally: one arrow, one path, zero choice. This is Laplace's world.

In an **∞-category**, between morphisms there exist **2-morphisms** (homotopies — continuous deformations), between 2-morphisms — 3-morphisms, and so on, to infinity. This is not an abstract complication — it is a fundamentally different way of speaking about "uniqueness."

In an ∞-category, "a unique morphism" means not "one arrow," but:

$$
\mathrm{Map}_{\mathcal{C}_\infty}(\Gamma, T) \simeq *
$$

The space of morphisms from $\Gamma$ to $T$ is **contractible** — homotopically equivalent to a point. And here the magic begins.

### Contractible ≠ One-Point {#стягиваемо-одноточечно}

A contractible space can contain **arbitrarily many points**. Classic example: the disk $D^2$ is contractible to a point (simply squeeze it), but contains a continuum of points. Each point is a concrete element; the fact that the space is contractible means only that **all points are connected by continuous paths**.

Translating into the language of free will:

| Property | 1-category | ∞-category |
|----------|-----------|-----------|
| **Goal** | Single ($T$) | Single ($T$) |
| **Paths** | One | Many |
| **Connection between paths** | — | All connected by homotopies |
| **Choice** | Absent | Choice of a specific path |
| **Outcome** | Fatalism | Freedom within unity |

Imagine a mountain with a single summit. From any point at the foot, the summit is the same. But there are many trails. One can ascend by the north slope (steep, fast). One can circle the mountain spirally (gentle, long). One can storm the ridge, wait out the storm in a cave, lose the path and return. All routes lead to the summit, all are "homotopically equivalent" — and all are *distinct*.

Fate determines **where** you will arrive. Freedom determines **how** you get there.

**Fate exists. Fatalism does not.**

## The Formula of Freedom {#формула-свободы}

The metaphor is good, but insufficient. A number is needed. How many paths exactly are available to system $\Gamma$?

### The Hessian and Zero Modes {#гессиан-и-нулевые-моды}

Each system $\Gamma$ exists in some "landscape" of free energy $\mathcal{F}[\Gamma]$. This is a function defining the "energetic relief" of the state space. It has a single global minimum — the stationary point $\rho^*$ (the attractor) — and the system naturally "flows" toward it, like a ball on a surface.

At each point $\Gamma$, this landscape is characterized by the **Hessian** — the matrix of second derivatives:

$$
\mathcal{H}_\Gamma := \frac{\partial^2 \mathcal{F}}{\partial \Gamma^2}\bigg|_{\Gamma}
$$

The Hessian is the "curvature of the landscape." A positive eigenvalue — a direction in which the surface curves upward (a slope along which the ball rolls toward the minimum). This direction is **constrained**: moving along it, you pay with energy.

A zero eigenvalue — a direction along which the surface is **flat**. The ball can roll along such a direction without any energy penalty. This is a **zero mode** of the Hessian. Each zero mode is an independent choice that requires no expenditure.

Formula:

$$
\boxed{\text{Freedom}(\Gamma) = \dim\ker(\mathcal{H}_\Gamma) + 1}
$$

Freedom = the number of zero modes of the Hessian + 1.

The term $+1$ accounts for the trivial path — the possibility of "staying in place." Even if all directions are constrained (the Hessian is positive definite, no zero modes), the system is "free" in the minimal sense: it *exists*.

### Why This Works {#почему-это-работает}

The connection with ∞-categories is not an analogy but a **theorem** [Т] (Sol.78, T-89). The formalism of Morse-Bott theory proves: the number of connected components of the space of gradient trajectories from $\Gamma$ to $\rho^*$ (up to continuous deformation) **equals** $\dim\ker(\mathcal{H}_\Gamma) + 1$. This is precisely $\pi_0(\mathrm{Map}(\Gamma, T))$ — the number of path classes in ∞-categorical language.

Free energy $\mathcal{F}[\Gamma]$ is a smooth function on the compact manifold $\mathcal{D}(\mathbb{C}^7)$ with a single non-degenerate minimum $\rho^*$ ([T-64](/docs/core/dynamics/gap-thermodynamics#теорема-глобальная-минимизация) [Т]). Critical submanifolds are orbits of the $G_2$ action. Each zero mode parametrizes a "flat" direction along which distinct descent trajectories to the minimum exist. The classes of these trajectories are precisely the distinct "routes to the summit."

## Four Properties of Freedom {#четыре-свойства-свободы}

The formula is not just a definition. Four properties follow from it, each with status [Т].

### 1. Freedom Cannot Be Imposed from Outside {#свободу-нельзя-навязать-извне}

$$
\text{Freedom}(\mathcal{E}[\Gamma]) \leq \text{Freedom}(\Gamma)
$$

for any CPTP channel $\mathcal{E}$ (a completely positive, trace-preserving map — this is the formalism of any physical process acting on the system from outside).

A CPTP channel contracts the Bures metric (Uhlmann's theorem). At the level of the Hessian: external influence **does not weaken the curvature** of free energy, and therefore does not increase the number of zero modes.

What does this mean for a person? One cannot **make** someone free. One can remove obstacles, can create conditions — but freedom arises only from within, as a property of one's own configuration $\Gamma$. Education does not "give" freedom — it helps the system discover its own zero modes. Prison does not "take away" freedom — it adds non-zero modes to the Hessian (additional constraints that make the landscape steeper).

### 2. Freedom Does Not Depend on the Description {#свобода-не-зависит-от-описания}

$$
\text{Freedom}(U\Gamma U^\dagger) = \text{Freedom}(\Gamma) \quad \forall U \in G_2
$$

A $G_2$ transformation is a change of "coordinate system" in the space of seven dimensions. The spectrum of the Hessian does not change under unitary conjugation. Freedom is an **invariant** independent of the language of description. The system can be described in English, in the language of neural networks, in the language of quantum states — the number of zero modes is the same. Freedom is objective.

### 3. Extreme Values {#крайние-значения}

| State | $\dim\ker(\mathcal{H}_\Gamma)$ | Freedom | Meaning |
|-------|-------------------------------|---------|---------|
| $I/7$ (maximum uncertainty) | 6 | **7** | All directions are free |
| $\Gamma_\odot$ (Source) | 6 | **7** | Maximum symmetry |
| Arbitrary $\Gamma$ | $0 \leq k \leq 6$ | $1$–$7$ | Depends on configuration |
| $\rho^*$ (attractor) | 0 | **1** | Hessian is positive definite |

Why Freedom(I/7) = 7? The maximally mixed state $I/7$ has full $S_7$-symmetry. The Hessian at this point is identically zero ($\mathcal{H}_{I/7} = 0$): all directions are equal, none is preferred. Six independent directions (on the manifold $\mathrm{Tr} = 1$) plus the trivial path = 7.

Why Freedom($\rho^*$) = 1? The stationary point $\rho^*$ is the global minimum of free energy. The Hessian is positive definite: **all** directions lead upward. No zero modes. The only "choice" — remain in place.

### 4. Freedom Decreases with the Growth of Consciousness {#свобода-убывает-с-ростом-сознания}

$$
\text{Freedom}(L0) > \text{Freedom}(L1) > \text{Freedom}(L2)
$$

This is the most counterintuitive property. Let us dwell on it.

## The Paradox of Conscious Unfreedom {#парадокс-осознанной-несвободы}

A hydrogen atom is maximally "free." Its coherence matrix is close to $I/7$, the Hessian is almost zero, there are many zero modes. Freedom ≈ 7.

A human is significantly less "free." Reflection $R \geq 1/3$ fixes the direction of self-modeling $\varphi$. Integration $\Phi \geq 1$ binds the dimensions. Differentiation $D_{\text{diff}} \geq 2$ constrains the spectrum. Each of these conditions is an **additional constraint** that removes zero modes from the Hessian. Freedom(L2) < Freedom(L0).

**An atom is freer than a human.** Mathematically.

But the atom does not *know* it is free. Formally its $R \approx 1$ — trivially maximal, because $\Gamma \approx I/7$ coincides with the dissipative attractor. But this is not consciousness: $\Phi \approx 0$ (no integration), $D_{\text{diff}} \approx 0$ (no differentiation). The atom "knows itself" in the same sense that a blank sheet "contains all texts" — trivially. Its "freedom" is pure potentiality, like the freedom of wind that does not choose a direction but simply blows. Freedom without a subject of freedom.

A human is more constrained — but *is aware of* those constraints and the residual freedom. Their Freedom is smaller, but each zero mode is **experienced from within** — as a choice, as a fork in the road, as existential anxiety or creative impulse.

Formally:

| Level | Freedom | Consciousness | Character of choice |
|-------|---------|--------------|---------------------|
| L0 (stone) | ~7 | No ($R \approx 1$ trivially, $\Phi \approx 0$) | Automatic — no subject |
| L1 (bacterium) | 4–6 | Proto ($\Phi < 1$) | Reactive — stimulus-response |
| L2 (human) | 2–4 | Yes ($R \geq 1/3$, $\Phi \geq 1$, $D_{\text{diff}} \geq 2$) | **Reflective** — conscious choice |
| L3 (meditation) | 2–3 | Meta ($R^{(2)} \geq 1/4$) | **Meta-reflective** — choice of criteria for choice |
| $\rho^*$ (attractor) | 1 | Stationary | No choice — stationary point |

Read the last row again. **Stationary point = no choice.** The attractor $\rho^*$ is the global minimum of free energy. The Hessian is positive definite: all directions lead upward, no zero modes. Every direction is determined, every step is predetermined. At the same time $\varphi(\rho^*) \neq \rho^*$ — complete self-knowledge is unattainable ([Т], T-55, Lawvere incompleteness). A system can be completely determined without being completely self-transparent.

Spinoza, 1677: "That thing is called free, which exists solely by the necessity of its own nature, and of which the action is determined by itself alone" (*Ethics*, Part I, Def. 7). Hegel (via Engels): "Freedom is recognized necessity." UHM, 2026: "Freedom is the dimensionality of the space in which necessity does not act. Structure is what narrows that space."

Spinoza was closest — but off by one quantifier. Freedom is not *self-determination* and not *recognition of necessity*, but the *geometry* of what remains after subtracting necessity. The more complex the system (greater $P$, $\Phi$, $D_{\text{diff}}$), the fewer zero modes remain ($\dim\ker \to 0$). Structure = constraint = loss of freedom = acquisition of determinacy. The exchange rate is fixed, and there is no one to bargain with.

## Compatibilism as Theorem {#компатибилизм-как-теорема}

Philosophical compatibilism — an attempt to reconcile determinism and freedom by redefining terms. Hume (1748): freedom is the absence of external coercion, and it is compatible with causal necessity. Frankfurt (1971): freedom is acting in accordance with second-order desires. Dennett (1984): freedom is a certain type of causal structure.

UHM offers not a redefinition, but a **structure**:

**∞-categorical argument [Т].** The space of morphisms $\mathrm{Map}(\Gamma, T) \simeq *$ is contractible — but a contractible space can contain many points (paths) connected by homotopies. Determinism (uniqueness of $T$) and the multiplicity of paths to it coexist — not by definition, but by the construction of the ∞-topos.

**Local argument.** For configurations $\Gamma$ far from the attractor $\rho^*$, the Hessian $\mathcal{H}_\Gamma$ typically has zero modes — the free energy landscape contains "flat" directions along which different descent trajectories are possible. But this is **not a theorem with a universal lower bound**: near the attractor $\rho^*$ the Hessian is positive definite and Freedom($\rho^*$) = 1. One cannot guarantee Freedom $\geq$ 2 for **all** viable states — only for those far from $\rho^*$.

In practice this is not a limitation: living systems are by definition far from $\rho^*$ (they actively maintain themselves through $\mathcal{R}$, while $\rho^*$ is the stationary point where dynamics cease). But formally: compatibilism here is a consequence of the ∞-categorical structure [Т], not a universal quantitative estimate.

## Responsibility {#ответственность}

If Freedom $> 1$ (the system is far from the attractor), it **could have** chosen a different path. From the multiplicity of paths follows responsibility: the consequences are determined not only by the endpoint ($T$ is the same for all), but by the **content of the route** — experiences, influence on other holons, local change of coherence.

Two paths to $T$: one through increasing $P$ in those around (helping), the other through decreasing it (harm). Both lead to the same point. But on the first path the total coherence grows, on the second — it falls. Ethical significance is not in the destination, but in the journey. The Golden Rule of ethics receives a geometric interpretation: from all available zero modes, choose the one that increases the coherence of the composite system $\Gamma_{\text{composite}}$.

## Freedom and Meaning {#свобода-и-смысл}

[Meaning](/docs/consciousness/ethics-meaning/meaning) in the UHM formalism has status [И] (interpretation), but its structure is suggested by mathematics. Peak potential of meaningfulness:

$$
\text{Meaning}_{\text{peak}} = \max_\tau \left[ P \cdot D_{\text{diff}} \cdot \Phi \cdot R \right]
$$

Four factors: wholeness ($P$), richness ($D_{\text{diff}}$), connectedness ($\Phi$), awareness ($R$). The product vanishes if at least one equals zero.

Connection with freedom: at Freedom = 1 ($\rho^*$) — stationary point, $D_{\text{diff}}$ is minimal (maximally predetermined configuration). At Freedom = 7 ($I/7$) — $\Phi = 0$, $D_{\text{diff}} = 0$, and meaning vanishes: neither richness nor awareness. **Meaningfulness is maximal somewhere in between** — in a system with enough freedom to choose and enough structure to understand what it is choosing.

This is L2. Consciousness. Not coincidentally it seems to us the most valuable of all there is.

## What Philosophers Say {#что-говорят-философы}

| Philosopher | Position | What the formula says |
|-------------|---------|----------------------|
| **Laplace** | Freedom is an illusion | ❌ ∞-categorical structure admits multiple paths |
| **Sartre** | We are "condemned to be free" | ≈ Contractibility of Map(Γ,T) is a structural property, not a choice |
| **Spinoza** | Freedom is recognized necessity | ≈ More precisely: the geometry of the remainder after subtracting necessity |
| **Kant** | Noumenal freedom, phenomenal determinism | ≈ ∞-categories provide the mechanism: "unique" → "contractible" |
| **Hume** | Compatibility of freedom and causality | ✅ Theorem, not definition |
| **Frankfurt** | Hierarchy of desires | ≈ L2 (reflective) vs L3 (meta-reflective) |
| **Libet** | Decision is made before awareness | ? φ-operator precedes awareness, but consciousness chooses from zero modes |

Libet deserves a separate comment. His famous experiment (1983) showed that the "readiness potential" in the brain arises ~350 ms before the conscious decision. Libet's conclusion: the decision is made unconsciously, freedom is an illusion.

Within the UHM framework: the self-modeling operator $\varphi$ does indeed precede awareness — this is not a bug but the [theorem on the physical realization of φ](/docs/consciousness/foundations/self-observation#теорема-физическая-реализация-phi) [Т]. But $\varphi$ **narrows** the space of alternatives, it does not **eliminate** it. Consciousness (L2, $R \geq 1/3$) does not *generate* alternatives — it *selects* from the zero modes left by unconscious filtering. Libet discovered not the absence of freedom, but its two-stage architecture: $\varphi$ proposes → consciousness chooses.

## What the Theory Is Silent About {#о-чём-молчит-теория}

The theory **formalizes** freedom. It does not **explain** the subjective experience of choice. The formula $\text{Freedom}(\Gamma) = \dim\ker(\mathcal{H}_\Gamma) + 1$ has status [Т] — it is a proven theorem. The interpretation "zero mode = conscious choice" has status [И] — a philosophical extrapolation.

Analogy: quantum mechanics formalizes probabilities and predicts the results of measurements with incredible precision. But it does not explain *why* the collapse of the wave function looks like "nature's choice." UHM is in an analogous position: the formula works, the statuses are honest, and the metaphysics of freedom remains — slightly less mysterious, slightly more geometric.

## Summary {#итого}

| Result | Status | Content |
|--------|--------|---------|
| Freedom(Γ) = dim ker(H_Γ) + 1 | [Т] | Formula of freedom |
| Equivalence to ∞-categorical definition | [Т] | Morse-Bott theory (T-89) |
| Monotonicity under CPTP | [Т] | Freedom cannot be imposed from outside |
| $G_2$-invariance | [Т] | Freedom is objective |
| Freedom(I/7) = 7, Freedom(ρ*) = 1 | [Т] | Extreme values |
| Freedom(L0) > Freedom(L2) | [Т] | Consciousness restricts freedom |
| Multiplicity of paths in the ∞-topos | [Т] | Contractibility ≠ being one-point |
| Freedom > 1 for configurations far from $\rho^*$ | [И] | Typical, but not universal property |
| "Zero mode = choice" | [И] | Interpretation, not theorem |
| Connection with meaning | [И] | Meaning = P · D_diff · Φ · R |

Freedom is not an illusion and not a mystery. It is the dimensionality of the kernel of the Hessian of the free-energy functional. A stone has this dimensionality greater than a human — but the stone does not know this (its $R \approx 1$ is trivially maximal, $\Phi \approx 0$). A human has it smaller — but each remaining zero mode is aware. At the attractor $\rho^*$ — zero: complete determinacy, stationary point.

Between "complete indeterminacy" (Freedom = 7, $\Phi = 0$) and "complete determinacy" (Freedom = 1, stationary point) lies human life: a few zero modes, not fully aware, not always chosen wisely, but — chosen. This is enough for meaning, responsibility, and anxiety.

Mathematics, as usual, does not ask for permission. But sometimes — it consoles.

---

**Related materials:**
- [Holonomic Paninteriorism](/blog/holonomic-paninteriorism) — UHM philosophical position
- [Geometry of the Inner World](/blog/geometry-of-inner-world) — 21 types of experience
- [Freedom of will](/docs/consciousness/ethics-meaning/freedom) — full formalism
- [Consequences from axioms](/docs/core/foundations/consequences#freedom-конечномерное) — proof and properties
- [Meaning of existence](/docs/consciousness/ethics-meaning/meaning) — teleology and meaning
- [UHM ethics](/docs/consciousness/ethics-meaning/value-consciousness) — from axioms to moral law
