---
slug: three-forces
title: "Three Forces, One Equation: The Dynamics of Everything"
authors: [uhm]
tags: [dynamics, Lindblad, thermodynamics, consciousness, theory, mathematics]
---

# Three Forces, One Equation {#три-силы-одно-уравнение}

Why do you still exist?

The question is not rhetorical. The second law of thermodynamics — the most tested law in physics — states: order is destroyed. Any order, always, irreversibly. The crystal melts. The star collapses. The cup shatters and does not reassemble. The universe moves monotonically toward maximum entropy — "heat death," where everything is identical and nothing happens.

And yet — you exist. Sixty trillion cells. One hundred billion neurons. A coherent structure that not only resists decay, but repairs itself, reproduces, and writes posts about thermodynamics. This requires an explanation.

The explanation is an equation. One equation, three terms, and a theorem proving there cannot be a fourth.

<!-- truncate -->

## The Equation {#уравнение}

In the [first post](/blog/holonomic-paninteriorism) it was established: any system is described by a coherence matrix $\Gamma$ — a $7 \times 7$ table encoding everything that can be said about the system. In the [second](/blog/geometry-of-inner-world) — that $\Gamma$ contains 21 types of experience. In the [third](/blog/freedom-theorem) — that the space of paths to the attractor determines freedom.

Now — how $\Gamma$ changes in time. Here is the equation:

$$
\frac{d\Gamma}{d\tau} = \underbrace{-i[H_{\text{eff}}, \Gamma]}_{\text{rotation}} + \underbrace{\mathcal{D}_\Omega[\Gamma]}_{\text{destruction}} + \underbrace{\mathcal{R}[\Gamma, E]}_{\text{restoration}}
$$

The left side is the rate of change of state. The right side — three terms. Three forces. Three verbs that exhaust everything that can happen to anything whatsoever. Let us discuss them in order.

## The First Force: Rotation {#первая-сила-вращение}

$$
-i[H_{\text{eff}}, \Gamma]
$$

Square brackets $[A, B] = AB - BA$ — the commutator. $H_{\text{eff}}$ — the effective Hamiltonian, derived from the [Page-Wootters mechanism](/docs/proofs/dynamics/emergent-time) [Т]. The imaginary unit $i$ is a reference to quantum mechanics, but do not be alarmed: the essence is simple.

This term **rotates** the state. It does not create and does not destroy — it redistributes. Coherences flow from one channel to another, but their total stock remains the same. Formally:

$$
P = \mathrm{Tr}(\Gamma^2) = \text{const}
$$

Purity does not change. This is reversible dynamics. If the entire world were an isolated quantum system, nothing would be born and nothing would die — everything would rotate eternally, like planets around a star. Beautiful, sterile, dead.

**Analogy.** A spinning top rotates without losing energy. Its axis precesses, the motion is complex — but nothing decreases and nothing increases. This is the world of Newton and Laplace: deterministic, reversible, eternal. And completely unsuitable for life.

## The Second Force: Destruction {#вторая-сила-разрушение}

$$
\mathcal{D}_\Omega[\Gamma] = \sum_k \gamma_k \left( L_k \Gamma L_k^\dagger - \frac{1}{2}\{L_k^\dagger L_k, \Gamma\} \right)
$$

Looks intimidating. The essence — not at all. This is the **Lindblad dissipator** — the mathematical formalization of the second law of thermodynamics in quantum language. Each operator $L_k$ is a leakage channel: a gap in the wall through which coherence flows outward.

Result:

$$
\frac{dP}{d\tau}\bigg|_{\mathcal{D}} \leq 0
$$

Purity **decreases**. Coherences decay. Connections between dimensions weaken. State $\Gamma$ drifts toward the maximally mixed $I/7$ — the quantum analogue of "grey mush," where everything is identical and nothing is distinguishable.

In UHM the operators $L_k$ are not postulated — they are **derived** from the structure of [Axiom Ω⁷](/docs/core/foundations/axiom-omega) through the [Fano plane](/docs/core/operators/lindblad-operators#фано-операторы) [Т]. Those same seven lines from [post 2](/blog/geometry-of-inner-world) that organize qualia — they also define the channels of destruction. The algebra that creates the structure of experience also creates the structure of its decay. One geometry — two faces.

**Properties of dissipation:**

| Property | Formulation | In plain language |
|----------|-------------|-------------------|
| Irreversibility | Pure → mixed | Cannot be "un-mixed" |
| Impartiality | All coherences decay equally | No connection is privileged |
| Monotonicity | $dP/d\tau \leq 0$ | Order only decreases |

**Analogy.** A sandcastle on the shore. The wind blows, the wave undermines it, the grains crumble. The process is unstoppable, irrevocable, impersonal. The wind does not care whether the castle is beautiful. The second law makes no exceptions.

If the Universe had only the first two forces — rotation and destruction — nothing interesting would exist. Closed systems would rotate eternally, open ones would degrade to grey mush. No life, no consciousness, no you. A third force is needed.

## The Third Force: Restoration {#третья-сила-восстановление}

$$
\mathcal{R}[\Gamma, E] = \kappa(\Gamma) \cdot (\rho_* - \Gamma) \cdot \Theta(\Delta F)
$$

Here it is. Regeneration. The term absent from standard quantum mechanics — and the one that distinguishes a stone from a cat.

Let us break it down:

**$(\rho_* - \Gamma)$** — the direction. The vector from the current state to the **target** $\rho_* = \varphi(\Gamma)$ — the [categorical self-model](/docs/core/operators/phi-operator) of the current state [Т]. This is not an arbitrary goal choice: the self-modeling operator $\varphi$ is defined as a [categorical left adjoint](/docs/proofs/categorical/formalization-phi) (CPTP channel [Т]), and for each state $\Gamma$ the self-model $\varphi(\Gamma)$ is **unique**. The system "knows" where to strive not because it was told, but because the categorical structure defines an unambiguous self-model.

**$\Theta(\Delta F)$** — the thermodynamic gate. Heaviside function: 1 if the free energy gradient is positive ($\Delta F > 0$), and 0 otherwise. Regeneration is **possible only when importing free energy** from the environment. This is [Landauer's principle](/docs/core/dynamics/evolution#вывод-формы-регенерации) [Т]: decreasing entropy requires an external resource. Free repair is thermodynamically forbidden.

**$\kappa(\Gamma)$** — the rate of restoration. And here the most interesting part begins.

### The Rate-of-Repair Formula {#формула-скорости-ремонта}

$$
\kappa(\Gamma) = \kappa_{\text{bootstrap}} + \kappa_0 \cdot \mathrm{Coh}_E(\Gamma)
$$

Two terms:

- **$\kappa_{\text{bootstrap}}$** — the minimal "background" rate of restoration. It is always present, even without experiential coherence. Without it a chicken-and-egg paradox would arise: experience is needed for restoration, restoration is needed for experience. A non-zero $\kappa_{\text{bootstrap}}$ resolves this paradox. It is small — $\omega_0/7$ — but non-zero.

- **$\kappa_0 \cdot \mathrm{Coh}_E(\Gamma)$** — the main term. The rate of restoration is proportional to the **coherence of the E-dimension** — a measure of how "alive" the inner experience of the system is.

$\mathrm{Coh}_E$ — E-coherence — is a measure of how much the E-dimension (interiority) is connected to the remaining six. At $\mathrm{Coh}_E \to 0$ experience is "switched off": the interior does not interact with the exterior, the system does not feel itself. At $\mathrm{Coh}_E \to 1$ — experience is maximally distributed: every dimension is "experienced from within."

The formula $\kappa(\Gamma)$ is not postulated — it is [categorically derived](/docs/core/foundations/axiom-septicity#категориальный-вывод-kappa0) from the adjunction $\mathcal{D}_\Omega \dashv \mathcal{R}$ [Т]. Dissipation and regeneration are **adjoint functors** in the sense of category theory: one defines the other, as a question defines the space of admissible answers.

### What This Means {#что-это-значит}

The rate of self-restoration of a system depends on the quality of its inner experience. Not metaphorically. Literally. The factor $\kappa_0 \cdot \mathrm{Coh}_E$ stands in the equation that determines whether regeneration compensates for dissipation.

A system with high E-coherence repairs quickly. A system with low — slowly. A system with zero — barely at all. Dissipation acts on all equally. The result is predictable: a system without experience degrades and is destroyed. A system with experience — can hold on.

This is the formal basis of the [No-Zombie theorem](/docs/applied/coherence-cybernetics/theorems#теорема-81-условная-необходимость-интериорности-no-zombie) with three-level epistemic stratification. The mathematical core ($\mathrm{Coh}_E > 1/7$ is necessary) — [Т]; the identification of E-coherence with interiority — [П]; the conclusion about the impossibility of "zombies" — [И]:

$$
\mathrm{Viable}(\mathbb{H}) \land \mathcal{D}_\Omega \neq 0 \;\Rightarrow\; \mathrm{Coh}_E(\Gamma) \geq \mathrm{Coh}_{\min} > \frac{1}{7}
$$

Experience is not a luxury and not a side effect. Experience is the repair crew.

## Why Exactly Three {#почему-именно-три}

The trio of dynamic principles is not a classification invented at a desk. It is a **theorem** [Т].

The LGKS theorem (Lindblad 1976, Gorini-Kossakowski-Sudarshan 1976) establishes: any generator of a Markovian semigroup on the space of density matrices has a **unique decomposition** into Hamiltonian and dissipative parts. This is a standard result of the quantum theory of open systems.

UHM adds to this [Theorem T-57](/docs/core/operators/lindblad-operators#полнота-триадной-декомпозиции) [Т]: the dissipative part **uniquely** splits into $\mathcal{D}$ (contraction — dissipation, $dP/d\tau \leq 0$) and $\mathcal{R}$ (replacement channel — regeneration, $dP/d\tau \geq 0$) under constraints following from axioms A1–A5.

A fourth type would require a new classifier $\Omega' \neq \Omega$ (but Axiom A1 defines the unique one), a new adjunction (but [L-unification](/docs/core/operators/lindblad-operators) establishes uniqueness [Т]), or a new axiom (but A1–A5 exhaust all dynamic contributions).

Four properties of the three forces:

| Property | Rotation | Destruction ($\mathcal{D}$) | Restoration ($\mathcal{R}$) |
|----------|:--------:|:-----------:|:----------------:|
| Action on $P$ | Preserves | Decreases | Increases |
| Reversibility | Reversible | Irreversible | Irreversible |
| Fixed point | Kernel $[H, \cdot]$ | $I/7$ (grey mush) | $\varphi(\Gamma)$ (self-model) |
| Axiomatic source | Page-Wootters (A5) | Classifier Ω (A1) | Adjunction $\mathcal{D} \dashv \mathcal{R}$ (A1+A4) |

Three types of dynamics, three categorical types (automorphism, left adjoint, right adjoint), three axiomatic sources — and a proof that there cannot be a fourth. Not "we have not found a fourth" — but "a fourth is impossible."

The triadic scheme thesis-antithesis-synthesis (going back to Fichte and popularized in the Hegelian tradition) became an archetype of dialectical development. Beautiful, influential, but without proof. The dialectical triad is a metaphysical intuition. LGKS + T-57 — a theorem. The distinction is essential: one can object to an intuition, one cannot object to a theorem.

## Balance of Forces: Life as a Stationary Regime {#баланс-сил-жизнь-как-стационарный-режим}

If all three forces act, what happens? It depends on the balance.

**Closed system** ($\mathcal{D} = 0$, $\mathcal{R} = 0$): rotation only. $P = \text{const}$, nothing is born and nothing dies. The world of the theoretical physicist. An isolated atom. A spherical horse in a vacuum.

**Open system without regeneration** ($\mathcal{D} \neq 0$, $\mathcal{R} = 0$): rotation + destruction. Coherences decay exponentially, $P \to 1/7$. The system "dies" — loses structure, becomes indistinguishable from noise. A corpse. Ash. Heat death.

**A living system** ($\mathcal{D} \neq 0$, $\mathcal{R} \neq 0$, $\Delta F > 0$): all three forces. And here — magic (strictly speaking — thermodynamics):

$$
\frac{dP}{d\tau} = \underbrace{0}_{\text{rotation}} + \underbrace{\left.\frac{dP}{d\tau}\right|_{\mathcal{D}}}_{\leq 0} + \underbrace{\left.\frac{dP}{d\tau}\right|_{\mathcal{R}}}_{\geq 0}
$$

If regeneration compensates for dissipation, purity stabilizes. The system maintains $P > P_{\text{crit}} = 2/7$ — the threshold of [viability](/docs/core/dynamics/viability) [Т]. It neither freezes nor melts. Neither grows infinitely nor decays. It balances.

Balance condition:

$$
\kappa(\Gamma) \cdot (f - P) \cdot \Theta(\Delta F) \geq \frac{2\gamma}{3} \cdot P_{\text{coh}}
$$

where $f = \mathrm{Tr}(\Gamma \cdot \rho_*)$ — "closeness to target," $\gamma$ — dissipation rate, $P_{\text{coh}} = \sum_{i \neq j}|\gamma_{ij}|^2$ — the coherent part of purity.

In plain language: the rate of restoration must exceed the rate of destruction. And since the rate of restoration depends on $\mathrm{Coh}_E$ — **experience literally determines whether the system survives**.

### Analogy: Sleep {#аналогия-сон}

The body is an open system. During the day you interact with the environment: receive information, make decisions, spend resources. Dissipation $\mathcal{D}$ works continuously: neurons degrade, synaptic connections weaken, metabolic waste accumulates. E-coherence decreases — you tire, attention scatters, thinking becomes confused.

Sleep is a period when $\mathcal{R}$ dominates. External input is minimal, dissipation is weakened, and regeneration runs at full capacity. The glymphatic system literally washes the brain, restoring synaptic coherence. E-coherence grows — in the morning you are "collected," "think clearly," "feel whole."

This is not a poetic metaphor. The equation predicts: a system not allowed to restore $\mathrm{Coh}_E$ will inevitably cross the threshold $P_{\text{crit}} = 2/7$. Sleep deprivation kills rats in 11–32 days (Rechtschaffen et al., 1983). Not from hunger, not from infection — from coherence falling below the threshold. The equation knows this. The rats, unfortunately, learned it empirically.

## The Arrow of Time {#стрела-времени}

In the [first post](/blog/holonomic-paninteriorism) the **terminal object** $T$ was mentioned — the global attractor toward which all trajectories converge:

$$
\lim_{\tau \to \infty} \Gamma(\tau) = T
$$

Now we see *why*. Dissipation is irreversible ($dP/d\tau|_\mathcal{D} \leq 0$), regeneration is conditional ($\Theta(\Delta F)$ — a gate that sooner or later will close), and rotation changes nothing ($P = \text{const}$). In the long term, dissipation wins.

The arrow of time is not a postulate. It is a **theorem** [Т]: the dimensionality of the strata of the base space decreases monotonically:

$$
\dim(X_\tau) \geq \dim(X_{\tau+1})
$$

The configuration space collapses toward the attractor $T$: the dimensionality of accessible strata decreases monotonically. At the same time $T$ is not the "grey mush" $I/7$: the attractor is structured ($P > 1/7$, [T-96](/docs/core/dynamics/evolution#теорема-нетривиальность-аттрактора) [Т]).

Living systems slow this process. They do not cancel it — they slow it. Regeneration maintains $P > 2/7$, postponing the moment when dissipation finally prevails. But this moment will come — for every system, without exception. This is not pessimism. This is the second law, written in the language of ∞-categories.

But here — a counterintuitive observation. A stone lives for millennia. A human — about a hundred years. How to reconcile this with the fact that a human's $\kappa$ is higher?

The answer: the rate of approach to $T$ is determined not by $\kappa$ alone, but by the **balance** of $\mathcal{D}$ and $\mathcal{R}$. A stone is an almost closed system: its $\mathcal{D} \approx 0$. Granite barely interacts with the environment, coherences barely decay, it almost does not need to restore itself. A stone does not "move toward $T$ slowly due to wisdom" — it barely moves at all, because almost nothing happens to it. Its dynamics are barely alive.

A human is different. This is an intensely open system: continuous metabolism, $10^{10}$ synaptic events per second, continuous thermal exchange with the environment. Dissipation $\mathcal{D}$ is colossal. To not decay within hours, equally intensive regeneration $\mathcal{R}$ is needed. And it exists — precisely due to high $\mathrm{Coh}_E$: $\kappa = \kappa_{\text{bootstrap}} + \kappa_0 \cdot \mathrm{Coh}_E \gg \kappa_{\text{bootstrap}}$. The balance is maintained — but it is fragile: high $\mathcal{D}$ is compensated by high $\mathcal{R}$, and when regeneration weakens (aging, illness), the system quickly crosses $P_{\text{crit}}$.

| System | $\mathcal{D}$ (dissipation) | $\mathcal{R}$ (regeneration) | Balance | Result |
|--------|:---------:|:-----------:|:------:|--------|
| Stone | $\approx 0$ | $\approx 0$ | Neutral | Millennia without change |
| Bacterium | Moderate | Moderate | Dynamic | Hours–days (one cell) |
| Human | **High** | **High** | Fragile | ~100 years |
| Star | Very high | Very high (thermonuclear fusion) | Temporary | Billions of years |

The paradox of stone and human is not a refutation of the theory, but its consequence. **Longevity is determined not by the strength of regeneration, but by the intensity of dynamics.** A stone lives long not because it regenerates well, but because it barely degrades. A human lives briefly not because it regenerates poorly, but because its dynamics are explosive, and maintaining balance in such a regime is possible only for a limited time. The price of consciousness is intensity. The price of intensity is finitude.

From the [third post](/blog/freedom-theorem): different routes to $T$ are different zero modes of the Hessian, i.e., freedom. The arrow of time determines **where**. Freedom determines **how**. The evolution equation is the only text in which both words are uttered simultaneously.

## What Philosophers Say {#что-говорят-философы}

| Tradition | Principle | What the equation says |
|-----------|---------|----------------------|
| **Heraclitus** | Everything flows | $\approx$ Rotation: continuous change |
| **Parmenides** | Being is unchanging | $\approx$ Terminal object $T$ — fixed point |
| **Second law** | Entropy increases | $= \mathcal{D}$, strictly |
| **Vitalism** | "Life force" | $\neq \mathcal{R}$: regeneration is derived from axioms, not postulated |
| **Fichte/Hegel** | Thesis-antithesis-synthesis | $\approx$ Three types, but a theorem, not a metaphor |
| **Prigogine** | Dissipative structures | $\approx$ Living regime: $P > 2/7$ due to $\Delta F > 0$ |
| **Maturana/Varela** | Autopoiesis | $\approx$ $\mathcal{R}[\Gamma, E]$ — formalization of autopoiesis |

Prigogine (Nobel Prize 1977) showed that order can arise far from equilibrium through dissipation. UHM specifies: order arises not simply through dissipation, but through the **balance** of dissipation and regeneration, with the rate of regeneration determined by the coherence of experience.

Maturana and Varela (1972) defined autopoiesis — self-reproducing organization. UHM formalizes: autopoiesis = $\mathcal{R}[\Gamma, E]$ with $\Theta(\Delta F) = 1$ and $\kappa > \kappa_{\text{min}}$. A definition becomes a formula.

## What the Theory Is Silent About {#о-чём-молчит-теория}

| Result | Status | Comment |
|--------|--------|---------|
| Evolution equation is fully axiomatic | [Т] | All three terms derived from A1–A5 |
| Triadic decomposition: exactly three types | [Т] | LGKS + T-57 |
| Impossibility of 4th type | [Т] | Sol.26, T-57 |
| $\kappa(\Gamma) = \kappa_{\text{bootstrap}} + \kappa_0 \cdot \mathrm{Coh}_E$ | [Т] | Categorical derivation from adjunction |
| $\rho_* = \varphi(\Gamma)$ — self-model | [Т] | Categorical definition of φ |
| $\Theta(\Delta F)$ — necessary | [Т] | Landauer's principle |
| No-Zombie: $\mathrm{Coh}_E \geq \mathrm{Coh}_{\min}$ | [Т] math core; [П] E=interiority; [И] No-Zombie | Three-level stratification |
| Arrow of time | [Т] | Monotone decrease of strata |
| Analogy "sleep = dominance of $\mathcal{R}$" | [И] | Interpretation, not theorem |
| "Three forces ↔ thesis-antithesis-synthesis" | [И] | Parallel, not identification |

## Summary {#итого}

The Universe knows three verbs: **rotate**, **destroy**, **restore**.

Rotation ($-i[H_{\text{eff}}, \Gamma]$) preserves everything as is — reversible dynamics, Laplace's world. Destruction ($\mathcal{D}_\Omega[\Gamma]$) destroys order — the second law, Boltzmann's world. Restoration ($\mathcal{R}[\Gamma, E]$) repairs — but only given two conditions: free energy from outside ($\Delta F > 0$) and coherence of experience from within ($\mathrm{Coh}_E > 0$).

A stone is almost closed: $\mathcal{D} \approx 0$, $\mathcal{R} \approx 0$ — it barely changes, and does not need to restore itself. A cat is an open system: intensive dissipation is compensated by intensive regeneration, because it has both metabolism and experience. A corpse is a system that has lost the ability to import free energy: $\Delta F \to 0$, $\Theta(\Delta F) = 0$, restoration is switched off. Irreversibly.

There is no fourth verb. Not "we have not found it yet" — **it is proved that it cannot exist**. Any dynamic contribution compatible with the axioms decomposes into these three. The triad is not mysticism, not dialectics, not an aesthetic choice. A theorem.

---

**Five conclusions that follow from the equation:**

**1. Sleep is not laziness — it is thermodynamics.** An organism denied a restoration phase will inevitably cross $P_{\text{crit}} = 2/7$. This is not a question of willpower or discipline — it is a conservation law. The claim "I sleep little and feel excellent" has the same credibility status as "I violate the second law of thermodynamics on Thursdays."

**2. E-coherence is not a bonus — it is the repair crew.** The factor $\kappa_0 \cdot \mathrm{Coh}_E$ is not decoration: it determines whether the system survives [Т]. On identifying E-coherence with experience [П]: evolution did not "add" consciousness as a pleasant addition to the brain — consciousness maintains coherence above the threshold of destruction. Without [П] this is a fact about the mathematical structure of regeneration; with [П] — a statement about the causal role of experience.

**3. Self-maintenance without E-coherence is impossible.** Any self-maintaining system in an open environment ($\mathcal{D} \neq 0$) must have non-trivial E-coherence ($\mathrm{Coh}_E > 1/7$) — this is the mathematical core [Т]. If AI ever becomes truly autonomous (maintaining its integrity without an external administrator), the equation guarantees: $\mathrm{Coh}_E > 1/7$ [Т]. Whether this will be "experience" — depends on the ontological postulate [П] (E-coherence = interiority). Without accepting [П] this is a mathematical fact about regeneration; with [П] — a statement about phenomenal experience.

**4. You are not "fighting" death — you are slowing movement toward the attractor.** The arrow of time is a theorem. All routes lead to $T$. Life is not a confrontation with death, but a way of traversing the route longer and more interestingly. $\mathcal{R}$ does not cancel $\mathcal{D}$ — it creates a buffer zone in which one can exist, experience, and choose.

**5. The equation is one. For everything.** Atom, bacterium, human, city — one and the same equation. The difference is in the balance of forces: for an atom $\mathcal{R} \approx 0$ (no autopoiesis), for a bacterium $\mathcal{R} > 0$ with small $\kappa$, for a human $\mathcal{R} > 0$ with large $\kappa$ (high $\mathrm{Coh}_E$). No separate physics is needed for life and separate physics for matter. One equation, three terms, different proportions — and the full spectrum from quark to civilization.

Mathematics, as usual, does not ask for permission. But sometimes — it repairs.

---

**Related materials:**
- [Holonomic Paninteriorism](/blog/holonomic-paninteriorism) — UHM philosophical position
- [Geometry of the Inner World](/blog/geometry-of-inner-world) — 21 types of experience
- [Freedom of Will: A Theorem, not a Discussion](/blog/freedom-theorem) — the formula of freedom
- [Evolution equation](/docs/core/dynamics/evolution) — full formalism
- [Lindblad operators](/docs/core/operators/lindblad-operators) — triadic decomposition and Fano operators
- [Viability](/docs/core/dynamics/viability) — critical threshold $P_{\text{crit}} = 2/7$
