---
sidebar_position: 3
title: "Freedom of Will"
description: "Formalisation of freedom of will through the ∞-categorical structure of UHM"
slug: /consciousness/ethics-meaning/freedom
---

# Freedom of Will in UHM

> *"If a Being... knew all the forces that animate nature, and the respective positions of the beings that compose it... nothing would be uncertain for it, and the future, like the past, would be present to its eyes."*
> — Pierre-Simon Laplace, *A Philosophical Essay on Probabilities* (1814)

:::info Bridge from the previous chapter
In [Meaning of Existence](/docs/consciousness/ethics-meaning/meaning) we defined meaning as the direction $\vec{s}(\Gamma)$ in state space. But a key question arises: **can we choose** this direction? If $\Gamma$ obeys the [evolution equation](/docs/core/dynamics/evolution), is the trajectory not predetermined? This document shows: no. The goal is one, but paths are infinitely many.
:::

---

## Part 0. Historical context: from Laplace to compatibilism

The problem of freedom of will is one of the most persistent in philosophy. Before showing how UHM resolves it, let us trace the history of the question.

### Laplace: the demon of determinism

In 1814 Laplace formulated a thought experiment: if an intellect existed that knew the position and velocity of every particle in the Universe, it could compute all future and all past. In such a world **there is no room for freedom**: every 'choice' you make is merely the inevitable consequence of the Universe's initial conditions.

**Problem:** If Laplace is right, moral responsibility is an illusion. One cannot blame a criminal who 'could not have done otherwise'.

### Kant: two worlds

Kant proposed an elegant, if radical, solution: a human being belongs to **two worlds** simultaneously. In the world of **appearances** (phenomena) causality operates — everything is determined. In the world of **things-in-themselves** (noumena) freedom operates — we **choose**. Problem: how do the two worlds interact? Kant acknowledged this is incomprehensible.

### Compatibilism: freedom is compatible with determinism

**Daniel Dennett** (and before him — Hume, Hobbes) proposed: freedom is not the 'absence of causes' but a **certain type of causality**. Free is not the one whose actions are 'uncaused' (that is chance, not freedom), but the one whose actions flow from **their own** desires, beliefs, and character. Compatibilism is the most popular position in contemporary academic philosophy.

**Problem:** If my desires are the result of causes I did not choose (genetics, upbringing, culture), in what sense are they 'mine'?

### Libertarian free will

Some philosophers (Kane, O'Connor) insist: genuine freedom requires **indeterminism** — at the moment of choice the future is not uniquely determined. Quantum mechanics would seem to offer this possibility (randomness in measurements). But randomness $\neq$ freedom: if my choice is the result of quantum randomness, it is no more 'mine' than if it had been determined.

### UHM: a third way

UHM proposes a solution that fits none of the traditional positions:

- **Not classical determinism:** the goal (T) is unique, but paths are infinitely many
- **Not indeterminism:** each path is **determined** by laws (the evolution equation)
- **Not Dennett's compatibilism:** freedom is not a redefinition of the word 'freedom' but a **mathematical structure** (multiplicity of morphisms in the ∞-category)

**Key metaphor:** All rivers flow into the ocean (T is unique). But between source and mouth there exist **many** possible channels. The determinism of the goal (ocean) does not exclude freedom of path.

## Chapter roadmap

1. **The problem** — how to reconcile the determinism of equations with the experience of freedom
2. **Resolution via ∞-categories** — multiplicity of paths with uniqueness of goal
3. **Finite-dimensional Freedom measure** — Hessian of free energy [T]
4. **Connection to consciousness** — L2 agents are aware of the multiplicity of trajectories
5. **Ethical consequences** — responsibility and connection to meaning
6. **Mathematical details** — path sheaves and HoTT

:::note About notation
In this document:
- $\Gamma$ — [coherence matrix](/docs/core/dynamics/coherence-matrix) — description of the system state
- $P = \mathrm{Tr}(\Gamma^2)$ — [purity](/docs/core/dynamics/viability) — measure of integrity
- $T$ — [terminal object](/docs/core/foundations/axiom-omega#свойство-3) — 'endpoint' of all trajectories
- $\varphi$ — [self-modelling operator](/docs/core/operators/phi-operator) — how the system sees itself
- L0→L4 — [interiority hierarchy](/docs/consciousness/hierarchy/interiority-hierarchy) — levels of depth of consciousness
:::

:::info Status: Formalised [T]
Freedom of will is formalised in two equivalent ways: (1) through the ∞-categorical structure of the theory (multiplicity of paths to terminal object T); (2) through the finite-dimensional definition $\text{Freedom}(\Gamma) = \dim\ker(\mathcal{H}_\Gamma) + 1$, where $\mathcal{H}_\Gamma$ is the Hessian of the free-energy functional. Monotonicity, extreme values, and $G_2$-invariance are proven — see [Consequences from the axioms](/docs/core/foundations/consequences#freedom-конечномерное).
:::

---

## 1. The problem of teleological determinism

### 1.1 Statement of the problem

[Axiom Ω⁷](/docs/core/foundations/axiom-omega) asserts the existence of terminal object T:

$$
\forall \Gamma \in \mathcal{C}, \exists! f : \Gamma \to T
$$

**Literal reading:** For each state there exists a **unique** morphism to T.

**Apparent consequence:** There is no choice. Fate is predetermined. Freedom is an illusion.

This is the formal analogue of **Laplacian determinism**, but stronger: Laplace spoke of the determination of the **trajectory**, here the **goal** itself (T) is determined.

### 1.2 Why this would be a problem

If UHM theory claims to describe consciousness and agency:
- **Agency** presupposes choice among alternatives
- **A unique morphism** excludes alternatives
- A contradiction arises between ontology and phenomenology

If there is no choice, then:
- Moral responsibility is meaningless (one cannot blame someone who could not have done otherwise)
- [Meaning](/docs/consciousness/ethics-meaning/meaning) is fiction (if the path is unique, 'choosing the path' is an illusion)
- [Consciousness](/docs/consciousness/overview#сознательное-окно) is an epiphenomenon (if $\Gamma$ follows a unique trajectory, why be aware of 'alternatives'?)

---

## 2. Resolution via ∞-categories

### 2.1 Key distinction: 1-categories vs ∞-categories

The resolution of the paradox lies in the distinction between **ordinary** (1-)categories and **∞-categories**. This distinction is subtle but fundamental.

In an ordinary (1-)category:
- Morphisms are either equal or distinct — there is no third option
- 'A unique morphism' = literally one morphism, one path, no alternatives

In an ∞-category:
- Between morphisms there exist **2-morphisms** (homotopies — 'paths between paths')
- Between 2-morphisms — **3-morphisms** (homotopies between homotopies)
- And so on, to infinity
- 'Uniqueness' means not 'one path' but **contractibility** of the space of paths

**Analogy for the non-specialist.** Imagine the surface of the Earth. Between Moscow and Tokyo there exist **many** routes: across Siberia, across Europe and the Atlantic, across the North Pole. All of them are 'equivalent' in the sense that they lead from Moscow to Tokyo. But each passes through different landscapes, and **the choice of a specific route matters** — for the traveller.

In a 1-category you would be told: 'there is one route' (a straight line). In an ∞-category: 'there are infinitely many routes, and all of them are equivalent — but not identical'.

### 2.2 ∞-terminal object

**Definition:**

In the ∞-category $\mathcal{C}_\infty$ an object T is called **∞-terminal** if for any object $\Gamma$ the morphism space is **contractible**:

$$
\text{Map}_{\mathcal{C}_\infty}(\Gamma, T) \simeq *
$$

**What does 'contractible' mean?** A space is contractible if it can be continuously 'compressed' to a point. The disk $D^2$ is contractible (can be compressed to its centre), the circle $S^1$ is not (cannot be compressed without tearing).

**Key point:** A contractible space may contain **arbitrarily many points**, connected by paths. The disk contains a **continuum** of points, but is contractible. So too $\text{Map}(\Gamma, T)$: it contains many morphisms (paths), but is contractible (all paths are equivalent).

### 2.3 Multiplicity within unity

**Observation (Multiplicity of paths):**

Let T be an ∞-terminal object. Then:

1. **Set of 1-morphisms:** $|\text{Mor}_1(\Gamma, T)|$ can be arbitrarily large — there are many concrete trajectories
2. **Unification:** All 1-morphisms are connected by 2-morphisms (homotopies) — every two paths are 'connected'
3. **Contractibility:** $\text{Map}(\Gamma, T) \simeq *$ (homotopically equivalent to a point) — globally the space is 'one'

**Proof:**

A contractible space may contain an arbitrary number of points connected by paths. Example: disk D² is contractible to a point, but contains a continuum of points.

Analogously: Map(Γ, T) ≃ * means that all 1-morphisms Γ → T can be 'connected' by 2-morphisms. ∎

---

## 3. Formalisation of freedom of will

### 3.1 Definition (∞-categorical)

:::warning Definition (Structural freedom in UHM: ∞-categorical motivation) [I]
For an agent $\Gamma \in \mathcal{C}$, ∞-categorical freedom is defined through the multiplicity of 1-morphisms:

$$
\mathrm{Freedom}(\Gamma) := |\text{Mor}_1(\Gamma, T)|
$$

— the number of distinguishable 1-morphisms (trajectories) to terminal object T.

**Note:** The space Map(Γ, T) is contractible ($\pi_0 = 1$), so all trajectories are connected by 2-morphisms (homotopies). Freedom consists **not in the choice of class**, but in the **choice of a specific trajectory** within the unique class.

**Finite-dimensional formalisation [T]:** $\text{Freedom}(\Gamma) = \dim\ker(\mathcal{H}_\Gamma) + 1$ — see [§3.3](#количественная-мера).
:::

**Interpretation:**
- $\pi_0$ — the set of 'coarse' trajectory classes. Contractibility gives $\pi_0 = 1$: one class.
- But within this class — **many** concrete trajectories
- Choice of a specific trajectory = freedom of will

**Returning to the river analogy:** The class is one — 'the river flows into the ocean'. But specific channels are many. The river is 'free' in choosing its channel, though 'not free' in choosing its endpoint.

### 3.2 Theorem on multiplicity

**Claim:**

For $\Gamma \neq T$ the space Map(Γ, T) contains many distinct 1-morphisms connected by non-trivial 2-morphisms.

**Proof:**

1. Map(Γ, T) ≃ * (contractible) — all homotopy groups are trivial: $\pi_n(\text{Map}(\Gamma, T)) = 0$.
2. However, contractibility **does not imply uniqueness of points**: disk D² is contractible, but contains a continuum of points.
3. Between any two 1-morphisms $f, g: \Gamma \to T$ there exists a 2-morphism (homotopy) $\eta: f \Rightarrow g$.
4. The set of 2-morphisms between fixed $f$ and $g$ may be non-trivial — there exist **different ways** of passing from $f$ to $g$.

**Key point:** Freedom lies not in the non-triviality of $\pi_n$, but in the **multiplicity of concrete paths** under their global equivalence. ∎

:::warning Clarification
$\pi_n(\text{Map}(\Gamma, T)) = 0$ for a contractible space. Freedom is measured by the **number of distinct 1-morphisms** (paths) and the **richness of 2-morphisms** (homotopies between them), not by the homotopy groups of the space as a whole.
:::

### 3.3 Finite-dimensional Freedom measure [T] {#количественная-мера}

The ∞-categorical definition is conceptually elegant, but how does one **measure** freedom for a specific system $\Gamma \in \mathcal{D}(\mathbb{C}^7)$? A finite-dimensional formalisation is needed.

:::warning Definition (Freedom in finite dimensions) [T]
For a configuration $\Gamma \in \mathcal{D}(\mathbb{C}^7)$:

$$
\text{Freedom}(\Gamma) := \dim\ker(\mathcal{H}_\Gamma) + 1
$$

where $\mathcal{H}_\Gamma$ is the Hessian of the free-energy functional:

$$
\mathcal{H}_\Gamma := \frac{\partial^2 \mathcal{F}[\varphi; \Gamma]}{\partial \Gamma^2}\bigg|_{\Gamma}
$$
:::

**Explanation of each symbol:**

- $\mathcal{F}[\varphi; \Gamma]$ — the free-energy functional, defining the 'landscape' of possible states. Its minima are stationary states $\rho^*$
- $\mathcal{H}_\Gamma$ — the **Hessian** (matrix of second derivatives) of $\mathcal{F}$ at point $\Gamma$. It describes the 'curvature of the landscape' around the current state
- $\ker(\mathcal{H}_\Gamma)$ — the **kernel** of the Hessian: the set of directions along which $\mathcal{F}$ does not change (zero modes, 'flat valleys')
- $\dim\ker(\mathcal{H}_\Gamma)$ — the number of independent 'flat' directions
- $+1$ — accounts for the trivial path (staying in place)

**Motivation.** In the $\infty$-categorical definition $\pi_0(\text{Map}(\Gamma, T)^{\text{non-trivial}})$ is the number of 'distinct' trajectories to $T$ that cannot be continuously deformed into one another. The finite-dimensional equivalent: the number of **distinct** directions in state space along which the free energy does not change (zero modes of the Hessian). Each zero mode is an **independent choice**: the system can move in that direction without an energy penalty.

**Everyday analogy:** Standing on top of a hill (a saddle point), you can go in **any** downward direction — all zero modes, high Freedom. Standing in a deep valley (a minimum of $\mathcal{F}$), you have one 'path' — upward out of the valley (Freedom = 1). On a mountain pass — you can walk along the ridge or descend into one of two valleys (Freedom = 2–3).

### Numerical example

Consider three states $\Gamma$ and compute their Freedom:

**State 1: Maximally mixed** ($\Gamma = I/7$)

The Hessian $\mathcal{H}_{I/7} = 0$ by $S_7$-symmetry: at the point of maximal entropy all directions are equivalent. $\dim\ker = 6$ (the space of $7 \times 7$ Hermitian matrices with unit trace has 48 real parameters, but for the diagonal — 6 independent). $\text{Freedom}(I/7) = 7$.

**State 2: Stationary** ($\Gamma = \rho^*$)

At the minimum of $\mathcal{F}$ the Hessian is **positive definite**: all eigenvalues $> 0$, kernel is empty. $\dim\ker = 0$. $\text{Freedom}(\rho^*) = 1$. The system has 'found its path' — further choice is impossible.

**State 3: Intermediate** ($P = 0.5$, conscious system)

The Hessian has 2 zero eigenvalues (two 'flat' directions). $\text{Freedom} = 3$. The system can choose one of three directions: stay in place, move along the first zero mode, move along the second.

#### Theorem (Properties of Freedom) [T]

**(a) Monotonicity under CPTP:**

$$
\text{Freedom}(\mathcal{E}[\Gamma]) \leq \text{Freedom}(\Gamma)
$$

*Proof.* The CPTP channel $\mathcal{E}$ is an affine map on $\mathcal{D}(\mathbb{C}^7)$. By the rank theorem: $\dim\ker(\mathcal{H}_{\mathcal{E}[\Gamma]}) \leq \dim\ker(\mathcal{H}_\Gamma)$, since $\mathcal{E}$ does not increase the dimension of the kernel (the image contracts). $\blacksquare$

**What does this mean?** Decoherence (CPTP channel) **reduces** freedom. Noise, chaos, destruction — all of these narrow the space of available trajectories. Intuitively obvious: a sick person is 'less free' than a healthy one — they have fewer available paths.

**(b) Extreme values:**
- $\text{Freedom}(I/7) = 7$: maximally mixed — all directions are 'indifferent' ($\mathcal{H}_{I/7} = 0$ by $S_7$-symmetry)
- $\text{Freedom}(\rho^*) = 1$: stationary — minimum of $\mathcal{F}$, Hessian positive definite ($\dim\ker = 0$)
- $\text{Freedom}(\Gamma_\odot) = 7$: Source — maximally symmetric pure state

**(c) $G_2$-invariance:**

$$
\text{Freedom}(U\Gamma U^\dagger) = \text{Freedom}(\Gamma) \quad \forall U \in G_2
$$

*Proof.* $G_2$-transformation is unitary conjugation, preserving the spectrum of $\mathcal{H}_\Gamma$. $\blacksquare$

**What does this mean?** Freedom is an **invariant**: it does not depend on the 'coordinate system' (basis), but only on the internal structure of $\Gamma$.

**(d) Connection to L-levels:**

$$
\text{Freedom}(L0) > \text{Freedom}(L1) > \text{Freedom}(L2)
$$

L0 systems have more zero modes (few constraints); L2 systems — fewer (reflection $R \geq 1/3$ fixes the direction of $\varphi$).

**This seems paradoxical:** is a conscious system not 'freer' than an unconscious one?

Answer: **formal** freedom (number of available directions) decreases as L grows, but the **quality** of freedom increases. An L0 system is 'free' like a leaf in the wind — it has many directions, but does not choose. An L2 system is constrained, but **is aware of** choice — and therein lies its genuine freedom.

Analogy: a child is 'freer' than an adult — can do anything. But the child does not **choose** — their 'freedom' is randomness. An adult is 'less free' (obligations, responsibility), but their freedom is **conscious choice**.

Full proof: [Consequences from the axioms](/docs/core/foundations/consequences#freedom-конечномерное).

#### Entropy of freedom

$$
S_{\text{freedom}}(\Gamma) := \log(\text{Freedom}(\Gamma)) = \log(\dim\ker(\mathcal{H}_\Gamma) + 1)
$$

**Properties:**
- At $\Gamma = \rho^*$ (stationary): $S_{\text{freedom}} = 0$ (no freedom, minimum reached)
- At $\Gamma = I/7$: $S_{\text{freedom}} = \log 7$ (maximal freedom)

---

## 4. Interpretation

### 4.1 Determinism + Freedom: comparative table

| Aspect | 1-category (determinism) | ∞-category (UHM) | Everyday analogy |
|--------|--------------------------|-------------------|------------------|
| Goal | Unique (T) | Unique (T) | All rivers → to the ocean |
| Path | Unique (f) | Many equivalent ones | Many channels |
| Choice | Absent | Choice of homotopic path | River 'chooses' its channel |
| Freedom | Illusion | Freedom = choice of trajectory | Terrain determines, but not uniquely |

### 4.2 Philosophical interpretation

> **Freedom of will** is not the choice of goal (T is unique), but the **choice of trajectory** for achieving that goal.

We do not choose the endpoint (T is the [∞-terminal object](/docs/core/foundations/axiom-omega#свойство-3)), but we choose **how** to live our life.

**Comparison with philosophical positions:**

| Position | Claim | UHM position |
|----------|-------|--------------|
| **Hard determinism** (Laplace) | Freedom is an illusion | No: there are many paths |
| **Libertarianism** (Kane) | Freedom requires indeterminism | No: paths are determined, but there are many |
| **Compatibilism** (Dennett) | Freedom = a certain type of causality | Close, but UHM provides a **quantitative** measure |
| **Kant** | Freedom is in the noumenal world | Close: ∞-categorical structure is the 'noumenal' level |

UHM is closest to **compatibilism**, but goes further: not just the 'compatibility' of freedom and determinism, but a **quantitative measure** of freedom ($\text{Freedom}(\Gamma)$) that decreases with decoherence and depends on the level of consciousness.

**From everyday life:** we all 'move' towards death (T is unique). But **how** we live our life — with care or indifference, with knowledge or ignorance, with love or hatred — this is our choice. And this choice **matters**, because it determines [meaning](/docs/consciousness/ethics-meaning/meaning) — $\text{Meaning}_{\text{total}} = \int P \cdot D_{\text{diff}} \cdot \Phi \cdot R\, d\tau$.

### 4.3 Connection to viability

Freedom is connected to [viability](/docs/core/dynamics/viability):

$$
P(\Gamma) > P_{\text{crit}} = \frac{2}{7} \Rightarrow S_{\text{freedom}}(\Gamma) > 0
$$

A viable system possesses non-zero freedom of path choice. A system below the threshold ($P \leq P_{\text{crit}}$) moves towards $I/7$ by a unique path — freedom is lost.

---

## 5. Choice of path

### 5.1 Structure of path space

The space Map(Γ, T) decomposes:

$$
\text{Map}(\Gamma, T) = \bigsqcup_{[\gamma] \in \pi_0} \text{Path}_{[\gamma]}
$$

Each component $\text{Path}_{[\gamma]}$ is a class of homotopically equivalent paths. For ∞-terminal T: $\pi_0 = 1$ (one class), but within this class — **infinite variety** of concrete trajectories.

### 5.2 Extended analogy: rivers and channels

Imagine a mountain landscape through which water flows down to the ocean.

**Ocean** = T (terminal object). All rivers flow into it — this is 'uniqueness of goal'.

**Terrain** = $\mathcal{F}[\Gamma]$ (free-energy functional). It determines where water 'flows' — which trajectories are possible.

**Channels** = concrete morphisms $f: \Gamma \to T$. There are many: through a mountain valley, across a plain, through caves.

**Zero modes of the Hessian** = 'passes' and 'plateaux': places where water can flow into any of several valleys. At these points — maximal Freedom.

**Minima of $\mathcal{F}$** = 'deep lakes': water 'gets stuck' (stationary $\rho^*$, Freedom = 1). Exit is possible only with external influence.

**Waterfalls** = bifurcations: points where a small perturbation leads to the choice of a fundamentally different channel.

### 5.3 Criteria for choice

An agent chooses a path according to criteria:

| Criterion | Formula | Interpretation | Example |
|-----------|---------|----------------|---------|
| Energy | $\int_\gamma \lVert d\Gamma/d\tau\rVert_B$ | Minimal effort | Laziness, habit |
| Time | $\text{length}(\gamma)$ | Shortest path | Efficiency |
| Risk | $\min_\tau P(\Gamma(\tau))$ | Maximum viability | Caution |
| Interiority | $\int_\gamma S_{vN}(\rho_E)$ | Richness of interior states | Fullness of life |

### 5.4 Choice algorithm

```
ALGORITHM choose_path(Γ, T, preferences):
    # Input: current state, terminal object, agent preferences
    # Output: specific path γ: Γ → T

    # 1. Compute path space
    PathSpace := Map(Γ, T)

    # 2. Decompose into connected components
    Components := π₀(PathSpace)

    # 3. Apply viability constraints
    Viable := filter(c for c in Components if min_purity(c) > P_crit)

    # 4. Optimise by preferences
    Optimal := argmin(Viable, cost(preferences))

    # 5. Select representative
    γ := representative(Optimal)

    RETURN γ
```

:::note Status: Conceptual pseudocode
This algorithm is a **conceptual scheme**, not directly implementable. Computing Map(Γ, T) in an ∞-category is an infinite-dimensional task. For practical implementation, finite-dimensional approximations are required.
:::

---

## 6. Connection to consciousness

### 6.1 Reflexive choice

The [self-modelling operator](/docs/proofs/categorical/formalization-phi) $\varphi$ is connected to freedom of will: $\varphi$ selects a **specific** self-model from the set of possible ones:

$$
\varphi: \mathcal{D}(\mathcal{H}) \to \mathcal{D}(\mathcal{H}), \quad \varphi(\Gamma) \in \text{Sub}(\Gamma)
$$

Each choice of $\varphi$ induces an evolution trajectory $\Gamma \to \varphi(\Gamma) \to \varphi^2(\Gamma) \to \cdots$, which can be viewed as an element of Map(Γ, T) upon identifying the limit point with T.

**Connection to Freedom:** The richer the space $\text{Sub}(\Gamma)$ (subalgebras of $\Gamma$), the more options for $\varphi$ — and the higher the Freedom. High $R$ **constrains** $\varphi$ (self-model is more precise → less 'freedom of choice' of self-model), but **improves** the quality of choice.

### 6.2 Conscious vs automatic choice

| Interiority level | Character of choice | Analogy | Freedom |
|-------------------|---------------------|---------|---------|
| [L0](/docs/consciousness/hierarchy/interiority-hierarchy) (interiority) | Automatic: fixed trajectory | Stone rolls down a hill | High (many modes, no choice) |
| [L1](/docs/consciousness/hierarchy/interiority-hierarchy) (phenomenal geometry) | Reactive: choice from a finite set | Animal: run or hide | Medium |
| [L2](/docs/consciousness/hierarchy/interiority-hierarchy) (cognitive qualia) | Reflexive: conscious choice of trajectory | A person plans a career | Low (conscious) |
| [L3](/docs/consciousness/hierarchy/interiority-hierarchy) (network consciousness) | Meta-reflexive: choice of choice criteria | Philosopher: 'but are my criteria correct?' | Even lower |
| [L4](/docs/consciousness/hierarchy/interiority-hierarchy) (unitary consciousness) | Integral: choice with complete self-modelling | Sage: self-model coincides with reality | Minimal (Freedom = 1 or 2) |

A conscious agent (L2+) is aware of the **multiplicity** of trajectories and makes a **reflexive** choice. L3–L4 agents are additionally capable of choosing the very criteria of choice.

**The paradox of wisdom:** An L4 system (sage) has minimal Freedom — but maximal **qualitative** freedom. The sage 'cannot act otherwise' (their $\varphi(\Gamma) \approx \Gamma$, the path is unique), but this unique path is **the best one**. They are free because they **do not need** alternatives.

---

## 7. Ethical consequences

### 7.1 Responsibility

The multiplicity of paths grounds **moral responsibility**:

- An agent **could have** chosen a different path (Freedom > 1)
- The choice of this path is the result of the agent's **decision** ($\varphi$ selects a specific trajectory)
- Consequently, the agent is **responsible** for the consequences

:::note Limitation
All trajectories are homotopically equivalent (they lead to the same T). The moral significance of a choice is determined not by the endpoint (T) but by the **content of the path**: experiences, impact on other Holons, local change in $P$.
:::

**Connection to criminal law:** Responsibility is proportional to Freedom. An L0 system (stone) — zero responsibility. An L1 system (animal) — limited (reactive choice). An L2 system (human) — full responsibility: conscious choice from many alternatives. Diminished responsibility (temporary reduction of $R < 1/3$) — **diminished** responsibility, because the awareness of choice is reduced.

### 7.2 Connection to meaning

Freedom of path choice is connected to [meaning of existence](/docs/consciousness/ethics-meaning/meaning):

$$
\text{Meaning}(\Gamma) \propto S_{\text{freedom}}(\Gamma) \cdot \text{Significance}(\gamma)
$$

Meaning = freedom × significance of chosen path. A system with zero freedom (Freedom = 1, stationary) cannot 'choose' a meaningful path. A system with maximal freedom (Freedom = 7, chaos) cannot assess significance. The highest meaning is in the **intermediate zone**: enough freedom to choose, enough structure to assess.

This explains why a 'too easy' life (everything decided for you, Freedom → 1) and a 'too chaotic' one (no structure, Freedom → max) are equally **meaningless**. Maximum meaning is in the **zone of conscious choice**: L2–L3, where Freedom is moderate and awareness is high.

---

## 8. Mathematical details

### 8.1 Path space as a sheaf

**Definition (Path sheaf):**

$$
\mathcal{P}\text{ath}_{\Gamma \to T} : U \mapsto \text{Map}_{\mathcal{C}_\infty}(\Gamma|_U, T|_U)
$$

where $U$ is an open subset of the base space $X = |N(\mathcal{C})|$.

### 8.2 Local sections = local choices

**Statement (Local freedom):**

Let $\{U_\alpha\}$ be a cover of X. Then:

1. Over each $U_\alpha$ there exists a set of local sections $s_\alpha \in \Gamma(U_\alpha, \mathcal{P}\text{ath})$
2. Sections agree on intersections: $s_\alpha|_{U_\alpha \cap U_\beta} \simeq_2 s_\beta|_{U_\alpha \cap U_\beta}$
3. Global section $s \in \Gamma(X, \mathcal{P}\text{ath})$ — a specific trajectory

**Interpretation:**
- Local choice — an agent chooses a path in their 'neighbourhood of experience'
- Global consistency — local choices are 'stitched together' into a single trajectory
- Freedom = choice of local section

### 8.3 Connection to HoTT

In homotopy type theory (internal logic of ∞-topos):

| HoTT | Freedom of will |
|------|-----------------|
| Type Path(a, b) | Path space Γ → T |
| Term p : Path(a, b) | Specific trajectory |
| Path q : p = p' | Equivalence of trajectories |
| Univalence | (Γ = T) ≃ (Γ ≃ T) |

---

### What we learned {#что-мы-узнали}

1. **Determinism and freedom are compatible.** The goal (T) is unique, but paths are many. The ∞-categorical structure resolves the paradox.
2. **Freedom is formalised [T]:** $\text{Freedom}(\Gamma) = \dim\ker(\mathcal{H}_\Gamma) + 1$ — the number of zero modes of the Hessian + 1.
3. **Monotonicity [T]:** CPTP channels do not increase freedom. Decoherence **reduces** the number of available trajectories.
4. **Freedom(L0) > Freedom(L2):** formal freedom decreases as L grows, but the **quality** of freedom (awareness of choice) increases.
5. **Responsibility is grounded:** an agent **could have** chosen differently — and is responsible for the consequences of the specific choice.
6. **Connection to meaning:** $\text{Meaning} \propto S_{\text{freedom}} \times \text{Significance}$. Highest meaning is in the intermediate freedom zone.
7. **UHM's historical position:** closest to compatibilism, but with a quantitative measure and ∞-categorical justification.

## Summary

:::tip Key results
1. **Teleological determinism resolved:** The goal (T) is unique, but trajectories are many
2. **Freedom formalised [T]:** $\text{Freedom}(\Gamma) = \dim\ker(\mathcal{H}_\Gamma) + 1$ — the number of zero modes of the Hessian + 1 (see [§3.3](#количественная-мера))
3. **Monotonicity [T]:** $\text{Freedom}(\mathcal{E}[\Gamma]) \leq \text{Freedom}(\Gamma)$ for CPTP channels
4. **$G_2$-invariance [T]:** $\text{Freedom}(U\Gamma U^\dagger) = \text{Freedom}(\Gamma)$ for $U \in G_2$
5. **Connection to consciousness:** L2+ agents are aware of the multiplicity of trajectories; $\text{Freedom}(L0) > \text{Freedom}(L1) > \text{Freedom}(L2)$
6. **Ethical consequence:** Multiplicity of trajectories grounds responsibility
:::

:::tip Bridge to the next chapter
We have shown that an agent is free in choosing a trajectory. But what happens when the trajectory **ends**? What does $P \to 0$ mean — and is there something 'after'? In the next — and concluding — chapter: [Death and Continuity](/docs/consciousness/ethics-meaning/death-continuity).
:::

---

**Related documents:**
- [Axiom Ω⁷](/docs/core/foundations/axiom-omega) — ∞-terminal object
- [Meaning of existence](/docs/consciousness/ethics-meaning/meaning) — connection between freedom and meaning
- [Viability](/docs/core/dynamics/viability) — $P > P_{\text{crit}} \Rightarrow S_{\text{freedom}} > 0$
- [Categorical formalism](/docs/proofs/categorical/categorical-formalism) — ∞-topos and lax 2-functor
- [Formalisation of φ](/docs/proofs/categorical/formalization-phi) — φ as path choice
- [Interiority hierarchy](/docs/consciousness/hierarchy/interiority-hierarchy) — levels of awareness of choice
- [UHM ethics](/docs/consciousness/ethics-meaning/value-consciousness) — responsibility as consequence of freedom
