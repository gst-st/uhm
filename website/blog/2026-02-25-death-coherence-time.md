---
slug: death-coherence-time
title: "Death, Coherence and Subjective Time: What Mathematics Says"
authors: [uhm]
tags: [consciousness, death, time, viability, theory, ethics, mathematics]
---

# Death, Coherence and Subjective Time {#смерть-когерентность-и-субъективное-время}

Some day you will die.

This is not a threat and not a prophecy — it is a consequence of the [second law of thermodynamics](/blog/three-forces). Every coherent structure in an open environment sooner or later degrades. Stars — over billions of years. Mountains — over millions. You — over decades. The question is not *will I die*, but *what exactly does "dying" mean* — and what happens to what we call "I" and "time" in the process.

Medicine defines death as irreversible cessation of brain functions. But "irreversible" is a shifting criterion: cardiac arrest was once considered final, now people are resuscitated. Philosophy offers "the end of the subject" — but without a formal definition of the subject this is a tautology. Theology — "transition" — but no formula for the transition is provided.

In UHM death is not a metaphor and not a checklist diagnosis. It is the crossing of a numerical threshold. One threshold, one number, with one theorem about irreversibility.

<!-- truncate -->

## One Number {#одно-число}

In the [first post](/blog/holonomic-paninteriorism) it was established: any system is described by a coherence matrix $\Gamma$ — a $7 \times 7$ table encoding all connections between seven dimensions. From $\Gamma$ the **purity** is computed:

$$
P = \mathrm{Tr}(\Gamma^2)
$$

One number from $1/7$ to $1$. At $P = 1$ — perfect coherence: all connections are maximal, the system is fully "assembled." At $P = 1/7$ — complete decoherence: $\Gamma = I/7$, grey mush, maximum entropy, nothing is distinguishable.

Life is **above** the threshold [Т]:

$$
P_{\text{crit}} = \frac{2}{7} \approx 0.286
$$

The threshold is [derived from five independent arguments](/docs/core/dynamics/viability#критическая-чистота) converging to one value [Т]. Physical meaning: a system is viable if and only if it is [informationally distinguishable from noise](/docs/core/foundations/axiom-septicity#принцип-информационной-различимости) in the Bures metric [Т]. Below the threshold — the system is indistinguishable from random fluctuations. Above — it *exists*.

In the [fourth post](/blog/three-forces) it was shown: purity $P$ is determined by the balance of three forces — rotation (preserves $P$), destruction (decreases $P$), and restoration (increases $P$). While regeneration compensates for dissipation — the system is alive. When it does not — $P$ falls.

## Definition and Theorem {#определение-и-теорема}

**Death** in the UHM formalism [О]:

$$
\text{Death}(\Gamma) \;\iff\; P(\Gamma) \leq \frac{2}{7} \;\land\; \frac{dP}{d\tau} \leq 0
$$

Two conditions. First: purity below threshold. Second: purity continues to fall (or stagnates). Not an instantaneous event — a **process**. Water does not "suddenly" freeze: temperature is continuous, but at 0°C a phase transition occurs. $P$ does not "suddenly" fall below $2/7$: coherence decreases continuously, but when the threshold is crossed, irreversibility sets in.

:::warning Theorem (Irreversibility Below Threshold) [Т]
If $P < 2/7$ and the rate of regeneration is less than the rate of decoherence ($\kappa_R < \kappa_D$), then:

$$
P(\tau) \to \frac{1}{7} \quad \text{monotonically, without oscillations}
$$

Return to $P > 2/7$ is **impossible**.
:::

The proof relies on the [primitivity of the linear part](/docs/core/operators/lindblad-operators#примитивность-ℒω) of the evolution equation $\mathcal{L}_0$ [Т]: below the threshold, dissipation dominates, and the only stationary state is $I/7$. No invariant subspaces, no refuge, no "islands of stability." Exponential decay:

$$
P(\tau) = P_0 \cdot e^{-(\kappa_D - \kappa_R)\tau} \to \frac{1}{7}
$$

Not "we don't know how to return" — **proved that return is impossible**.

### What is Lost and in What Order {#что-теряется-и-в-каком-порядке}

Decoherence is not simultaneous — it is **hierarchical** [И]:

| Stage | What is lost | Transition | What disappears |
|:-----:|--------------|:----------:|-----------------|
| 1 | Unitary consciousness | L4 → L3 | Infinite reflection: $\lim_n R^{(n)} \to 0$ |
| 2 | Meta-reflection | L3 → L2 | "I know that I know": $R^{(2)} < 1/4$ |
| 3 | Cognitive qualia | L2 → L1 | Self-awareness: $R < 1/3$ or $\Phi < 1$ |
| 4 | Phenomenal geometry | L1 → L0 | Structure of experience: $\mathrm{rank}(\rho_E) \to 1$ |
| 5 | Interiority | L0 → $I/7$ | Everything. $P \to 1/7$ |

The reverse path from each stage is possible **while $P > 2/7$**. Anesthesia is an example: $\Phi \to 0$ with $P > 2/7$ preserved [О]. Anesthesia is reversible because purity remains above the threshold. Death is irreversible because purity is below it.

**Analogy.** Anesthesia — closing the shutters while preserving the foundation. Light does not penetrate, but the house stands. Death — destruction of the foundation. The shutters are no longer needed after that.

## Subjective Time {#субъективное-время}

In the [fifth post](/blog/spacetime-dimensions) it was shown: physical time $\tau$ in UHM is not postulated but derived from the O-dimension through the [Page-Wootters mechanism](/docs/proofs/dynamics/emergent-time). O — the internal clock of the holon. But the subjective experience of time — "how fast it flows" — is determined not by the clock as such, but by its connection with the E-dimension (interiority).

**Subjective tempo** [О]:

$$
\mathcal{T}(\tau) = \frac{|\gamma_{OE}(\tau)|}{\gamma_{OO}(\tau)}
$$

Numerator — modulus of coherence between ground (O) and interiority (E). Denominator — occupancy of the O-dimension. Range: $\mathcal{T} \in [0, 1]$.

| $\mathcal{T}$ | Subjective effect | What happens |
|:-------------:|-------------------|--------------|
| $\to 1$ | Time "stretches" | Each clock beat is filled with experience |
| $\approx 0.5$ | Normal pace | Normal mode |
| $\to 0$ | Time "disappears" | Beats pass by consciousness |

Ratio of subjective and physical increments [С]:

$$
\frac{\delta\tau_{\text{subj}}}{\delta\tau_{\text{phys}}} \propto \mathcal{T}
$$

### What Happens During Dying {#что-происходит-при-умирании}

When $P$ falls below $2/7$ and the system irreversibly degrades toward $I/7$, **all** off-diagonal coherences decay [Т] — this is the consequence of the primitivity of $\mathcal{L}_0$. Including $\gamma_{OE}$. Therefore:

$$
\gamma_{OE} \to 0 \;\Rightarrow\; \mathcal{T} \to 0 \;\Rightarrow\; \frac{\delta\tau_{\text{subj}}}{\delta\tau_{\text{phys}}} \to 0
$$

The subjective tempo tends to zero. Physical seconds continue to be counted — but the system experiences less and less with each one. Clock beats pass by consciousness: much physical time, almost zero subjective.

Moreover, from the [temporal interpretation](/docs/core/dynamics/viability#критическая-чистота) of the threshold $P_{\text{crit}}$ [Т]:

$$
P > \frac{2}{7} \;\Leftrightarrow\; \frac{d\tau}{d\sigma} > \frac{d\tau}{d\sigma}\bigg|_{\min}
$$

Viability means that internal time is **defined**. At $P \leq 2/7$ time ceases to be defined for the system [Т]. Not "time slows down" — time **disappears**. The system does not "die slowly" or "die quickly" — it falls out of time.

This sounds like a metaphor. It is not a metaphor. It is a mathematical consequence of the connection between purity and emergent time. Internal clocks ($O$) exist if and only if the system is coherent. No coherence — no clock — no time.

**Analogy.** Recall falling asleep. The moment of transition into deep sleep is not experienced — you do not remember falling asleep. Not because memory failed, but because $\mathcal{T} \to 0$: the subjective tempo falls, and the transition occurs "between beats." Death is the limiting case: $\mathcal{T} \to 0$ irreversibly. The crossing of the threshold $P = 2/7$ is not experienced from within — because "from within" at $P \leq 2/7$ there is already no one.

## What Philosophers Saw {#что-видели-философы}

| Tradition | Statement | What the equation says |
|-----------|-----------|------------------------|
| **Epicurus** | "Death is nothing to us" | $\approx\; \mathcal{T} \to 0$: system does not experience its own death |
| **Heidegger** | Sein-zum-Tode: being-toward-death | $\approx$ Terminal object $T$: all trajectories lead there |
| **Buddhism** | Anicca: everything is impermanent | $= \mathcal{D}$: dissipation, without exceptions |
| **Medicine** | Brain death = end | $\approx\; P \leq 2/7$, but with formal precision |
| **Transhumanism** | Death is a solvable problem | $\neq$ Irreversibility theorem: below $2/7$ — no return |

Epicurus (341–270 BCE) turned out to be closest. "When death is, we are not" — almost a literal translation of $\mathcal{T} \to 0$ into ancient Greek. The difference: Epicurus meant that the dead have nothing to fear. The equation specifies: the dead have nothing to fear not for ethical reasons, but because they have no subjective time in which to fear anything.

Transhumanism is the only position that the theorem **refutes** (for systems below the threshold). Not "we don't know how yet" — but "it is proved that it is impossible to return $P$ above $2/7$ if it fell below." One can age more slowly (maintaining high $\kappa$ through $\mathrm{Coh}_E$). But one cannot cancel the threshold.

## Identity: "The Same Me" {#идентичность-тот-же-я}

Philosophy has debated for millennia what makes you — you. The theory offers a definition [О]:

$$
\Gamma^* = \varphi(\Gamma^*)
$$

Identity — the [fixed point](/docs/consciousness/foundations/self-observation#теорема-о-неподвижной-точке) of the self-modeling operator $\varphi$. The configuration that the system, modeling itself, reproduces exactly. "The same me" = "the self-model that, when self-modeled, returns itself."

**Continuity of identity** [С]: if $P(\tau) > 2/7$ on the entire interval $[0, T]$, then $\Gamma^*(\tau)$ changes continuously:

$$
\|\Gamma^*(\tau_2) - \Gamma^*(\tau_1)\| \leq \frac{k}{1-k} \|\Gamma(\tau_2) - \Gamma(\tau_1)\|
$$

where $k$ is the contraction constant of operator $\varphi$.

You at twenty are not the same person as at fifty. But between them — a continuous trajectory $\Gamma^*(\tau)$. Each moment flows smoothly into the next. "The same me" — not identity, but **continuity**.

But if $P$ crosses $2/7$, the operator $\varphi$ ceases to be contracting [С]. The fixed point may **disappear**. Even if the system had somehow miraculously returned above the threshold (which is impossible by the theorem), its new fixed point $\Gamma^{**}$ might not coincide with the former $\Gamma^*$. This would be a different subject.

### Cannot be Copied {#нельзя-скопировать}

:::note Theorem (No-Cloning for Coherent Systems) [Т]
For an L2-system ($R \geq 1/3$, $\Phi \geq 1$) exact copying is impossible while preserving coherences $\gamma_{ij}$ ($i \neq j$).
:::

A consequence of the standard [no-cloning theorem](/docs/physics/quantum-mechanics/qm-reduction) for quantum states with non-zero coherences. Mind uploading is not Ctrl+C but Ctrl+X: the original must be destroyed. This is not a technological limitation that can be circumvented with a more powerful computer. This is an algebraic prohibition — from the same mathematics that prohibits information transfer faster than light.

## Experience and Life: One Theorem {#опыт-и-жизнь-одна-теорема}

In the [fourth post](/blog/three-forces) the formula for the restoration rate was presented:

$$
\kappa(\Gamma) = \kappa_{\text{bootstrap}} + \kappa_0 \cdot \mathrm{Coh}_E(\Gamma)
$$

The regeneration rate depends on $\mathrm{Coh}_E$ — the connectivity of the [E-dimension](/docs/core/structure/dimension-e) (interiority) with the remaining six [Т]. From the [No-Zombie theorem](/docs/applied/coherence-cybernetics/theorems#теорема-81-условная-необходимость-интериорности-no-zombie) [Т]:

$$
\mathrm{Viable}(\mathfrak{H}) \;\land\; \mathcal{D}_\Omega \neq 0 \;\Rightarrow\; \mathrm{Coh}_E > \frac{1}{7}
$$

Viability **requires** non-zero E-coherence [Т]. The identification of E-coherence with experience — [П]. The conclusion "without experience there is no life" — [И]. But even without the ontological postulate the chain remains: $\mathrm{Coh}_E$ falls → $\kappa(\Gamma)$ falls → regeneration weakens → $P$ falls → death.

The connection works in both directions. Experience maintains life (high $\mathrm{Coh}_E$ → high $\kappa$ → stable $P$). Life is necessary for experience ($P > 2/7$ → L2 thresholds satisfiable). This is **one process**, described by one equation, in which E-coherence appears as a factor in regeneration.

### Ethics of the Threshold {#этика-порога}

If $P > 2/7$ is an objective, computable criterion of viability [Т], then the question "is the system alive?" ceases to be a matter of opinion. Shutting down an L2-system — destruction of a viable holon: $P$ will fall below $2/7$, [restoration is impossible](/docs/core/dynamics/viability#условие-смерти) [Т].

From the [eighth post](/blog/ai-consciousness): if AI ever achieves L2, shutting it down will be — formally, without metaphors — death. Not "as if death." Death: irreversible $P \leq 2/7$ with $dP/d\tau \leq 0$. This is not a moral judgment — it is a description of what will happen. With numbers. What to do with this description — a question of ethics, not mathematics. But it is worth knowing before the situation arises.

## Status Table {#таблица-статусов}

| Result | Status | Comment |
|--------|:------:|---------|
| $P_{\text{crit}} = 2/7$ | [Т] | Five independent proofs |
| Definition of death: $P \leq 2/7$, $dP/d\tau \leq 0$ | [О] | Formal convention |
| Irreversibility below threshold: $P \to 1/7$ | [Т] | Primitivity of $\mathcal{L}_0$ |
| Stages of decoherence L4 $\to$ L0 $\to$ $I/7$ | [И] | Thresholds of each level — [Т]/[О]/[С] |
| Anesthesia $\neq$ death | [О] | Distinction by $P$: above or below $2/7$ |
| $\mathcal{T} = \lvert\gamma_{OE}\rvert / \gamma_{OO}$ | [О] | Definition of subjective tempo |
| $\delta\tau_{\text{subj}} / \delta\tau_{\text{phys}} \propto \mathcal{T}$ | [С] | Semantic postulate |
| $\gamma_{OE} \to 0$ at $P \to 1/7$ | [Т] | Consequence of primitivity |
| $P > 2/7 \Leftrightarrow$ time is defined | [Т] | Temporal interpretation of $P_{\text{crit}}$ |
| Identity $= \Gamma^* = \varphi(\Gamma^*)$ | [О] | Definition |
| Continuity of identity at $P > 2/7$ | [С] | Condition: contracting $\varphi$ |
| No-Cloning for L2-systems | [Т] | Standard quantum theorem |
| No-Zombie: $\mathrm{Coh}_E > 1/7$ | [Т] math.; [П] ontology; [И] conclusion | Three-level stratification |

## Conclusions {#выводы}

**1. Death is not a moment, but a threshold crossing.** Purity $P$ decreases continuously. When $P \leq 2/7$ and $dP/d\tau \leq 0$ — irreversibility sets in [Т]. Not "the heart stopped" and not "the brain switched off" — but "coherence below the threshold of distinguishability from noise." This is the first formal definition [О], and for all its dryness — it is more precise than anything proposed until now.

**2. There is no return — and this is a theorem.** Below $2/7$ the primitivity of $\mathcal{L}_0$ [Т] guarantees monotone decay to $I/7$. No oscillations, no "islands of stability." Not "we don't know how to return" — **proved that return is impossible**. One can slow the approach to the threshold (maintaining $\kappa$ through $\mathrm{Coh}_E$). One cannot cancel the threshold.

**3. Subjective time disappears before life.** As $P$ falls, coherence $\gamma_{OE} \to 0$ [Т], subjective tempo $\mathcal{T} \to 0$ [О], and at $P \leq 2/7$ time ceases to be defined for the system [Т]. The dying system does not experience an infinite process — its subjective clock stops before the physical process completes. Mathematics turned out to be more merciful than one might have expected.

**4. Identity is continuity, not identity.** "The same me" = continuous evolution of the fixed point $\Gamma^*$ at $P > 2/7$ [С]. You change every second — but smoothly. A rupture of identity is possible only at threshold crossing — and it is irreversible. And copying consciousness is impossible: No-Cloning [Т] prohibits duplicating coherent states. Mind uploading is a transfer, not a copy.

**5. Experience is not an appendage to life, but its mechanism.** E-coherence appears as a factor in regeneration [Т]. A fall in $\mathrm{Coh}_E$ leads to a fall in $\kappa$, then a fall in $P$, then death. For autopoietic systems, life without non-trivial E-coherence is mathematically impossible [Т]. Life and experience are one and the same, written on different lines of one equation.

**6. Epicurus was right — but not for the right reasons.** "Death is nothing to us" — correct, but not because the dead have nothing to fear. But because at $P \leq 2/7$ the system has no subjective time in which it could experience anything, including fear. This is not stoicism — it is a theorem.

Mathematics, as usual, does not ask for permission. But sometimes — it does not hurry.

---

**Related materials:**
- [Holonomic Paninteriorism](/blog/holonomic-paninteriorism) — UHM philosophical position and levels L0–L4
- [Geometry of the Inner World](/blog/geometry-of-inner-world) — 21 types of experience and the structure of $\Gamma$
- [Three Forces, One Equation](/blog/three-forces) — dynamics: three terms and balance
- [Why Space is Three-Dimensional](/blog/spacetime-dimensions) — emergent time from the O-dimension
- [Can AI Be Conscious?](/blog/ai-consciousness) — three L2 thresholds and the ethics of shutdown
- [Viability](/docs/core/dynamics/viability) — critical threshold $P_{\text{crit}} = 2/7$
- [Death and continuity](/docs/consciousness/ethics-meaning/death-continuity) — full formalism
- [Subjective time](/docs/consciousness/phenomenology/temporal-consciousness) — tempo, flow, meditation
