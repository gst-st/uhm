---
sidebar_position: 3
title: "Emergent Time"
description: "Derivation of time from the structure of category 𝒞 — definitions and key results"
---

# Emergent Time

This chapter is one of the most revolutionary in the Unitary Holonomic Monism. We are accustomed to thinking of time as something that "simply exists" — an invisible river carrying everything forward. Newton regarded time as absolute — a cosmic clock ticking uniformly for everyone. Einstein showed that time is relative: it flows differently for observers moving at different speeds. But even in relativity, time **exists** as a background structure — flexible, yet imposed from outside.

UHM takes the next, radical step: **time does not exist as a background**. Time is not stage scenery but part of the performance. It *emerges* from the internal structure of reality, like a pattern appearing on fabric in a certain light.

:::info DRY: Master definition of temporal structure
Time is **derived** from the structure of the [subobject classifier Ω](/docs/core/foundations/axiom-omega), not postulated. The full proof and all four constructions are in the [Theorem on Emergent Time](/docs/proofs/dynamics/emergent-time).
:::

---

## Historical Precursors

The idea of emergent time did not arise from nothing. It grew from centuries of reflection on the nature of temporality.

**Newton (1687)** postulated *absolute time* — invisible clocks ticking uniformly throughout the Universe. This worked beautifully for mechanics, but was philosophically unsatisfying: where do these clocks come from? Who wound them up?

**Einstein (1905, 1915)** replaced absolute time with *relative* time. Time became part of spacetime, whose fabric is curved by mass. But spacetime was still a *background* — the stage on which physics is performed.

**Wheeler and DeWitt (1967)** discovered a fundamental problem. When they attempted to quantize gravity, the Schrödinger equation became $\hat{H}|\Psi\rangle = 0$ — the total energy of the Universe equals zero. Time *disappeared* from the equations. This became known as the "frozen formalism problem": quantum gravity describes a Universe in which nothing happens!

**Page and Wootters (1983)** proposed an elegant solution. Time had not disappeared — it was hidden *inside* quantum correlations. If one part of the system is designated as "a clock" and one asks "what is the rest of the system doing when the clock reads τ?" — dynamics is recovered. Time is not a background, but a **correlation between subsystems**.

**Connes (1994)** showed how to extract time from algebraic structure. In noncommutative geometry, the automorphism group of the algebra of observables contains a one-parameter flow — "time" — as a purely algebraic object.

UHM synthesises all these ideas into a single construction, where time emerges in four equivalent ways from the same mathematical source — the [classifier Ω](/docs/core/foundations/axiom-omega).

---

## Intuitive Explanation: A Room Without Clocks

Imagine a room with no windows and no clocks. Inside is a pendulum. You do not "know" the time in any absolute sense — no cosmic clock ticks behind the walls. But you can *define* time by watching the pendulum: "When the pendulum was on the left, the ball was rolling right. By the time the pendulum reached the right, the ball had already fallen."

The pendulum is not time. But without the pendulum there is no way to "know" the time. Time is what you *extract* from the correlations between the pendulum and the other objects in the room.

In UHM the role of the pendulum is played by the [O-dimension (Foundation)](/docs/core/structure/dimension-o). The Holon is a system of 7 dimensions. One of them (O) functions as an internal clock. The remaining 6 "dance" in correlation with that clock. Time is not the background on which the dance takes place, but the **rhythm extracted from the dance**.

:::note Key idea
Time in UHM is not a container in which events are immersed, but a **pattern of correlations** between the O-dimension (the clock) and the other six dimensions. The Universe is "stationary" as a whole, yet contains internal dynamics — like a frozen hologram in which each cross-section shows its own "moment".
:::

---

## Temporal Modality ▷ {#темпоральная-модальность}

On the classifier $\Omega \in \mathbf{Sh}_\infty(\mathcal{C})$ a temporal modality is defined — **algebraically**, independently of dynamics:

$$
\triangleright: \Omega \to \Omega, \quad \triangleright(S_i) := S_{(i+1) \bmod N}
$$

Intuitively: the operator ▷ is a "shift by one step". It cyclically permutes the subobjects of the classifier, creating an algebraic structure from which time can be read. This is like the hand of a clock: it does not *create* time, but its motion *defines* the sequence of moments.

**Properties:**
1. **Monotonicity:** $p \leq q \Rightarrow \triangleright p \leq \triangleright q$ — the shift preserves order
2. **Cyclicity:** $\triangleright^N = \text{Id}$ — after $N$ steps we return to the beginning
3. **Compatibility with logic:** $\triangleright(p \land q) = \triangleright p \land \triangleright q$ — the shift respects logical structure

#### Relation to the Page–Wootters Hamiltonian {#temporal-modality-pw}

The temporal modality $\triangleright$ is the **discrete analogue** of the time-shift operator $e^{-iH_O \delta\tau}$:

$$
\triangleright = e^{-iH_O \cdot 2\pi/(7\omega_0)}
$$

In the limit $N \to \infty$ (composite systems) the discrete shift passes to a continuous generator:

$$
\triangleright \xrightarrow{N \to \infty} e^{-iH_O dt}, \quad H_O = -i\frac{N\omega_0}{2\pi}\ln(\triangleright)
$$

The Hamiltonian $H_O$ is **recovered** from $\triangleright$ via the matrix logarithm — time–energy duality in the discrete setting.

---

## Four Equivalent Constructions

UHM derives time in four different ways — and proves that all of them yield the same result. This is like four different routes leading to the same mountain summit. Each route illuminates its own aspect of the nature of time.

| # | Construction | Source | Time |
|---|-------------|----------|-------|
| 1 | **Page–Wootters** | Correlation with the [O-dimension](/docs/core/structure/dimension-o) | $\tau_n = \langle\tau_n\lvert\rho\rvert\tau_n\rangle_O$ |
| 2 | **Information-geometric** | Bures metric on $\mathcal{D}(\mathcal{H})$ | $ds^2_{\text{Bures}}$ |
| 3 | **Categorical** | ∞-groupoid of paths $\text{Exp}_\infty$ | Chains of morphisms |
| 4 | **Stratificational** | Collapse of strata to $T$ | $d_{\text{strat}}$ |

:::warning Theorem T-53a (Equivalence of the four constructions of time) [Т]
All four constructions — Page–Wootters, information-geometric, categorical, and stratificational — generate **isomorphic** temporal structures: canonical bijections exist between the sets of "moments" that preserve order and metric (up to normalisation).
[Proof →](/docs/proofs/dynamics/emergent-time#6-теорема-об-эквивалентности) | Status: **[Т]**
:::

### Formal Justification of the Equivalence of the Four Constructions {#four-constructions-equivalence}

Proof sketch for the equivalence (full proof: [Theorem →](/docs/proofs/dynamics/emergent-time#6-теорема-об-эквивалентности)):

**PW ↔ Information-geometric.** The Bures arc length between successive conditional states is constant: $d_B(\Gamma(\tau_n), \Gamma(\tau_{n+1})) = \delta\tau \cdot \|d\Gamma/d\tau\|_B = \text{const}$, since the PW mechanism generates a uniform discrete flow. Summing over $n$ ticks gives total time as the path-length integral.

**PW ↔ Categorical.** Each conditional state $\Gamma(\tau_n)$ is a 0-morphism in $\mathbf{Exp}_\infty$. The transition $\Gamma(\tau_n) \to \Gamma(\tau_{n+1})$ is a 1-morphism induced by the CPTP channel $e^{\delta\tau \mathcal{L}_\Omega}$. The chain of 1-morphisms forms a path in the ∞-groupoid whose length = number of ticks = discrete time.

**PW ↔ Stratificational.** Each tick of the PW clock is a coarsening of the stratification: $\pi_n: \mathcal{C}_n \to \mathcal{C}_{n-1}$ is a functor that loses homotopic information. The descent depth (number of applications of $\pi$) to the terminal object $T$ coincides with the number of PW ticks for a compatible choice of clock.

### Construction 1: Page–Wootters (the pendulum in the room)

This is the most intuitive construction. We designate one dimension (O) as "the clock" and ask: "What is the rest of the system doing when the clock reads τ?"

Analogy: you are in a windowless room. The pendulum (O) swings. You cannot look at an external clock. But you can say: "When the pendulum is *here*, the temperature is *this*. When the pendulum is *there*, the temperature is *different*." History thus emerges from correlations.

### Construction 2: Information-geometric (path length)

Time is the "distance" travelled by the system through state space. The Bures metric measures how much two quantum states differ from each other.

Analogy: imagine walking through an unfamiliar city without a map or a watch. You can estimate "how much time has passed" by how much the landscape around you has changed. The faster the landscape changes, the faster "time flows". In a desert time slows down (the landscape is monotonous); in a city centre it speeds up.

### Construction 3: Categorical (chains of arrows)

In the ∞-groupoid, time is a "chain of morphisms" (arrows) connecting states. The length of the chain is time itself.

Analogy: imagine a family tree. The "time" between you and your great-grandfather is the number of generations (arrows "parent → child"). Time here is not physical seconds but *structural depth* — the number of steps in the chain of transformations.

### Construction 4: Stratificational (descent down the staircase)

The ∞-topos has a hierarchy of levels (strata). Each coarsening is a transition from a more detailed description to a less detailed one. Time is the "descent depth" to the terminal object $T$.

Analogy: imagine a staircase. At the top is complete information about everything (the state of every particle). At the bottom is the maximally coarse description (simply "something exists"). Each step down erases detail. The descent is irreversible — what is forgotten cannot be recalled. This irreversibility *is* the arrow of time.

---

## The Page–Wootters Mechanism for UHM {#page-wootters}

The [O-dimension (Foundation)](/docs/core/structure/dimension-o) plays the role of **internal clock**. The total system decomposes as:

$$
\mathcal{H}_{total} = \mathcal{H}_O \otimes \mathcal{H}_{6D}
$$

where $\mathcal{H}_{6D} = \mathrm{span}\{|A\rangle, |S\rangle, |D\rangle, |L\rangle, |E\rangle, |U\rangle\}$.

This decomposition can be understood as follows: of the Holon's seven dimensions, one (O) is singled out as the "metronome". The remaining six are the "orchestra" playing in time with that metronome. The music (dynamics) exists only as a correlation between the metronome and the orchestra.

### The Page–Wootters Constraint {#constraint}

The global state $\Gamma_{total}$ satisfies the **constraint** (the analogue of the Wheeler–DeWitt equation):

$$
\hat{C} \cdot \Gamma_{total} = 0
$$

where the constraint operator is:

$$
\hat{C} = H_O \otimes \mathbb{1}_{6D} + \mathbb{1}_O \otimes H_{6D} + H_{int}
$$

This constraint is equivalent to the requirement:

$$
[\hat{C}, \Gamma_{total}] = 0
$$

i.e. the total system is **stationary** — time emerges only as an internal parameter of correlations.

:::info What does "stationary" mean?
"Stationary" does not mean "dead". A standing wave on a guitar string appears motionless, yet every point on the string is oscillating. So too the Universe in UHM: *as a whole* it does not change, but inside it there is motion — like the patterns inside a frozen hologram.
:::

### Clock Basis for N=7 {#clock-basis}

How exactly does the O-dimension function as a clock? Through a special basis — the **clock basis**. For $N = 7$ it is defined via the discrete Fourier transform over the energy levels $|E_k\rangle_O$:

$$
|\tau_n\rangle_O = \frac{1}{\sqrt{7}} \sum_{k=0}^{6} e^{-2\pi i k n / 7} |E_k\rangle_O, \quad n = 0, 1, \ldots, 6
$$

Here $n$ labels the "moments of time". The Holon has exactly **seven** of them — like seven frames in an animation. Each $|\tau_n\rangle$ is a superposition of all energy levels of the O-dimension with phases chosen so as to give the most "localised" moment.

:::note Numerical example: clock basis
For $N = 7$, let the energies of the O-dimension be $E_k = k\omega_0$ ($k = 0, \ldots, 6$). Then:

$$
|\tau_0\rangle = \frac{1}{\sqrt{7}}(|E_0\rangle + |E_1\rangle + |E_2\rangle + |E_3\rangle + |E_4\rangle + |E_5\rangle + |E_6\rangle)
$$

$$
|\tau_1\rangle = \frac{1}{\sqrt{7}}\sum_{k=0}^{6} e^{-2\pi i k/7}|E_k\rangle
$$

and so on. The states $|\tau_n\rangle$ are orthonormal: $\langle \tau_m | \tau_n\rangle = \delta_{mn}$, and are cyclically shifted by the operator $e^{-iH_O \delta\tau}$:

$$
e^{-iH_O \cdot 2\pi/(7\omega_0)} |\tau_n\rangle = |\tau_{(n+1) \bmod 7}\rangle
$$

This is how the clock "ticks": each tick shifts the state to the next moment.
:::

#### Why the Fourier Basis? {#fourier-clock-basis}

The choice of the discrete Fourier transform for the clock basis is **not arbitrary**:

- **Energy eigenstates** $|E_k\rangle$ are **maximally delocalised in time**: stationary states do not evolve and cannot distinguish moments.
- The Fourier transform exchanges uncertainties: **localisation in energy ↔ delocalisation in time** and vice versa. This is the discrete analogue of the time–energy uncertainty principle.
- Each $|\tau_n\rangle$ is the **unique** state that is maximally peaked at "moment $n$" while remaining normalisable. This is the discrete analogue of the coherent states of the harmonic oscillator.

### The Emergent Parameter τ {#emergent-tau}

**Internal time** $\tau$ is defined through conditional states. We "ask" the total state: "What is the six-dimensional system doing when the clock reads $\tau_n$?"

$$
\Gamma(\tau) := \frac{\mathrm{Tr}_O\left[ (|\tau\rangle\langle \tau|_O \otimes \mathbb{1}_{6D}) \cdot \Gamma_{total} \right]}{p(\tau)}
$$

where $p(\tau) = \mathrm{Tr}[(|\tau\rangle\langle\tau|_O \otimes \mathbb{1}_{6D}) \cdot \Gamma_{total}]$ is the probability of "moment" $\tau$.

Intuitively: we project the total state onto a "slice" at a specific clock reading $\tau$. Each slice is the coherence matrix $\Gamma(\tau)$ of the six-dimensional subsystem. The collection of slices is a "film" assembled from "frames".

:::warning Theorem T-53b (Emergent dynamics) [Т]
The conditional states $\Gamma(\tau)$ evolve according to the full UHM equation:

$$
\frac{d\Gamma(\tau)}{d\tau} = -i[H_{\text{eff}}, \Gamma(\tau)] + \mathcal{D}[\Gamma(\tau)] + \mathcal{R}[\Gamma(\tau), E]
$$

where $H_{\text{eff}}(\tau) = H_{6D} + \langle\tau| H_{\text{int}} |\tau\rangle_O$ is the effective Hamiltonian, $\mathcal{D}$ is the [Fano dissipator](/docs/core/operators/lindblad-operators), and $\mathcal{R}$ is the [regenerator](/docs/core/dynamics/evolution#вывод-формы-регенерации).

All three components of the [triadic decomposition](/docs/core/operators/lindblad-operators#триадная-декомпозиция) emerge **automatically** from the PW constraint — time is born together with the full dynamics.
[Proof →](/docs/proofs/dynamics/emergent-time#3-механизм-page-wootters-для-угм) | Status: **[Т]**
:::

Remarkably, the emergent dynamics *automatically* contains all three components of the [triadic decomposition](/docs/core/operators/lindblad-operators#триадная-декомпозиция): the Hamiltonian $-i[H_{eff}, \cdot]$, the dissipator $\mathcal{D}$, and the regenerator $\mathcal{R}$. Time does not merely "emerge" — it emerges *together with the full dynamics*.

:::warning Status of the tensor structure
The decomposition $\mathcal{H} = \mathcal{H}_O \otimes \mathcal{H}_{6D}$ is formally **Axiom 5**, but is **derivable** from A1–A4 via the spectral triple T-53 **[Т]**: the algebra $A_{\text{int}} = \mathbb{C} \oplus M_3(\mathbb{C}) \oplus M_3(\mathbb{C})$ with KO-dimension 6 uniquely determines the tensor decomposition. Details: [derivation of A5](/docs/core/foundations/axiom-omega#a5-из-спектральной-тройки). Status: **[Т]**
:::

---

## Discreteness and the Chronon {#chronon}

### Seven Frames of Animation

For $N = 7$ time is **fundamentally discrete**: $\tau \in \mathbb{Z}_7$. The Holon has exactly 7 "moments" — like 7 frames in an animation. The transition between frames is the minimal quantum of subjective time, called the **chronon**:

$$
\delta\tau = \frac{2\pi}{7\omega_0}
$$

where $\omega_0$ is the fundamental frequency of the O-dimension.

The analogy with cinema is deeper than it appears. When you watch a film, you see continuous motion — but it is actually 24 frames per second. The brain "stitches" the discrete frames into the illusion of continuity. Continuous physical time is likewise an illusion arising from the discrete "ticks" of the O-dimension.

### From Discrete to Continuous

Continuous physical time is the **macroscopic approximation** when $N_{\text{eff}} \gg 7$ for composite systems. The algebraic limit:

$$
\mathbb{C}[\mathbb{Z}_N] \to C(S^1) \quad \text{as } N \to \infty
$$

Here $\mathbb{C}[\mathbb{Z}_N]$ is the group algebra of the cyclic group of $N$ elements (discrete clock with $N$ divisions), and $C(S^1)$ is the algebra of continuous functions on the circle (continuous clock). As $N \to \infty$ a discrete dial with $N$ divisions becomes continuous.

:::info How continuous time arises
An individual Holon has 7 "ticks". But a composite system of $M$ Holons has $N_{\text{eff}} = 7^M$ ticks (in the simplest case). Already for $M = 10$ (a modest system of 10 Holons) $N_{\text{eff}} \approx 3 \times 10^8$ — resolution so fine that discreteness is indistinguishable. For macroscopic systems ($M \sim 10^{23}$) time is effectively continuous.

**Discretisation error estimate.** For a system of $M$ independent Holons the approximation error for continuous time is $O(7^{-M})$ — exponentially small. Formally: by the Stone–Weierstrass theorem, $\mathbb{C}[\mathbb{Z}_N]$ is dense in $C(S^1)$ in the sup-norm as $N \to \infty$.

**Remark:** $N_{\text{eff}} = 7^M$ holds for **independent** Holons (tensor product of clocks). For interacting systems $N_{\text{eff}}$ may differ from $7^M$ depending on the coupling spectrum.
:::

[More on the limit $N \to \infty$ →](/docs/proofs/dynamics/emergent-time#предел-n-infty)

---

## The Arrow of Time

Why does time flow "forward" and not "backward"? Why do we remember the past but not the future? In classical physics the arrow of time is a puzzle: the laws are symmetric under time reversal. In UHM the arrow of time is a **structural necessity**.

:::warning Theorem T-53c (Arrow of time) [Т]
The arrow of time arises as the **collapse of strata** of the ∞-topos to the terminal object $T$. For the coarsening functor $\pi_n: \mathcal{C}_n \to \mathcal{C}_{n-1}$:

1. **Irreversibility:** $\pi_n$ is not an equivalence ($\ker(\pi_n) \neq 0$ — information is lost)
2. **Monotonicity:** $\dim(\mathcal{C}_n) \geq \dim(\mathcal{C}_{n-1})$ — complexity does not increase
3. **CPTP structure:** Orientation toward $T$ entails the CPTP property of evolution (a consequence, not a postulate)

[Proof →](/docs/proofs/dynamics/emergent-time#7-теорема-о-стреле-времени) | Status: **[Т]**
:::

### Intuitive Explanation of the Arrow

Imagine a tower of LEGO bricks. Each floor is a level of description (a stratum). On the top floor is complete information (the position of every atom). On the bottom floor is the maximally coarse description (simply "something exists").

Moving from the top floor to the bottom is easy: one only needs to "forget" details. Moving back is impossible: one cannot recover the position of every atom knowing only "something exists". This **irreversibility of forgetting** is the arrow of time.

Formally: each stratum $\mathcal{C}_n$ projects onto the next $\mathcal{C}_{n-1}$ via the coarsening functor $\pi_n: \mathcal{C}_n \to \mathcal{C}_{n-1}$. This functor **is not an isomorphism** — it loses information. The loss of information defines a unique direction — from $\mathcal{C}_n$ to $T$ (the terminal object) — which is the arrow of time.

### Relation to CPTP

CPTP channels (completely positive, trace-preserving maps) are the canonical form of quantum evolution. In standard quantum theory their CPTP property is postulated. In UHM it is **derived**: the orientation of strata toward $T$ means that each step of evolution is a coarsening, and coarsenings are automatically CPTP.

---

## Relation to Critical Purity

As $P \to P_{\text{crit}} = 2/7$ the rate of flow of internal time tends to zero:

$$
\frac{d\tau_{int}}{dt_{ext}} \propto (P - P_{\text{crit}})^{1/2}
$$

Viability ($P > 2/7$) is equivalent to the Holon **continuing to exist in time**.

#### Derivation of the Time-Slowing Formula (T-53d) [Т] {#time-freezing-derivation}

:::warning Theorem T-53d (Critical slowing of internal time) [Т]

$$
\frac{d\tau_{\text{int}}}{dt_{\text{ext}}} = c_0 \cdot (P - P_{\text{crit}})^{1/2} + O(P - P_{\text{crit}})
$$

where $c_0 > 0$ is a constant depending on $\omega_0$ and the spectrum of $\mathcal{L}_0$.
:::

**Proof.**

**Step 1 (Speed from the PW mechanism).** The rate of internal time is given by the Bures norm of the conditional states:

$$
v_{\text{int}}^2 := \left\|\frac{d\Gamma(\tau)}{d\tau}\right\|_B^2 = 4\sum_{i \neq O} |\gamma_{Oi}|^2 \cdot \omega_0^2
$$

This follows from the fact that the PW mechanism generates evolution via O-coherences: $d\Gamma/d\tau = -i[H_O \otimes \mathbb{1}, \Gamma_{\text{total}}]|_{\tau}$, and $\|[H_O, \cdot]\|_B^2 = 4\omega_0^2 \sum_{i \neq O} |\gamma_{Oi}|^2$.

**Step 2 (O-coherences near $P_{\text{crit}}$).** Expand $\Gamma = I/7 + \delta\Gamma$, where $\delta\Gamma$ is the deviation from the maximally mixed state. Purity: $P = 1/7 + \|\delta\Gamma\|_F^2$. Spectral gap of the Liouvillian $\mathcal{L}_0$ (T-39a [Т]): $\Delta(\mathcal{L}_0) = \min_{\lambda \neq 0} |\mathrm{Re}(\lambda)| > 0$. The coherences $\gamma_{Oi}$ as components of $\delta\Gamma$ satisfy $\dot{\gamma}_{Oi} = -\Delta \cdot \gamma_{Oi} + \kappa \cdot f_i(\Gamma)$. In the stationary regime: $|\gamma_{Oi}|^2 \propto \kappa^2 / \Delta^2$. Near $P_{\text{crit}}$: the balance of regeneration and dissipation gives $\kappa / \Delta \propto (P - P_{\text{crit}})^{1/2}$ (from the pitchfork bifurcation of the stationary state — analogue of $m \propto (T_c - T)^{1/2}$ in Landau theory).

**Step 3 (Combining).** Substituting Step 2 into Step 1:

$$
v_{\text{int}} = 2\omega_0 \sqrt{\sum_{i \neq O} |\gamma_{Oi}|^2} \propto (P - P_{\text{crit}})^{1/2}
$$

The rate of internal time vanishes as $(P - P_{\text{crit}})^{1/2}$ — **critical slowing down**, analogous to slowing in the theory of second-order phase transitions (the critical exponent $\beta = 1/2$ coincides with the prediction of Landau mean-field theory). $\blacksquare$

### Intuitive Explanation: Freezing of Time

Purity $P$ is a measure of the "definiteness" of the Holon's state. At $P = 2/7$ (the critical threshold) the system is on the boundary between life and death. The rate of internal time vanishes here — time *freezes*.

Analogy: imagine a clock driven by a spring. The spring unwinds (purity drops). The weaker the spring, the slower the clock ticks. At $P = 2/7$ the spring is fully relaxed — the clock stops. The Holon ceases to "experience" time.

This is not merely a metaphor. The formula $d\tau_{int}/dt_{ext} \propto (P - P_{\text{crit}})^{1/2}$ means that near the threshold time slows *critically* — according to the square-root law. This recalls critical phenomena in the physics of phase transitions: near the critical temperature dynamics "freezes" (critical slowing down).

:::warning Subjective time and death
For an observer *inside* the Holon (i.e. for consciousness itself) the moment $P \to 2/7$ is unreachable in finite subjective time — time slows faster than the system approaches the threshold. This is analogous to the event horizon of a black hole: an external observer sees the object "freeze" at the horizon, while the object itself crosses it in finite proper time. In UHM the situation is reversed: subjective time stretches *infinitely*, protecting the system from "experiencing" its own death.
:::

[Proof →](/docs/proofs/dynamics/emergent-time#8-связь-с-критической-чистотой) | Status: **[Т]**

---

## The Chronon: Quantum of Subjective Time

The chronon $\delta\tau$ is the minimal interval of subjective time distinguishable by the Holon. This is not merely a mathematical abstraction — it is a fundamental limit on the "temporal resolution" of consciousness.

$$
\delta\tau = \frac{2\pi}{7\omega_0}
$$

The chronon is determined by two quantities:
- **7** — the number of dimensions of the Holon (determines the number of "frames")
- **$\omega_0$** — the fundamental frequency of the O-dimension (determines the rate at which "frames" are played)

:::info Physical scale of the chronon
For neural systems $\omega_0$ is related to the characteristic frequency of neural oscillations (~40 Hz for the gamma rhythm). Then $\delta\tau \sim 2\pi/(7 \times 40) \approx 22$ ms — on the order of the duration of one "perceptual frame". This is consistent with psychophysical data on the minimum interval of conscious discrimination (~20–30 ms).
:::

---

## Summary: Five Key Ideas

1. **Time does not exist as a background.** It emerges from correlations between the O-dimension (the clock) and the other six dimensions of the Holon.

2. **Four constructions — one result.** The Page–Wootters, information-geometric, categorical, and stratificational constructions yield an equivalent notion of time [Т].

3. **Time is fundamentally discrete.** The Holon has 7 "moments". Continuous time is the macroscopic approximation for composite systems.

4. **The arrow of time is a structural necessity.** It arises from the irreversibility of coarsening (the collapse of strata to the terminal object).

5. **Time freezes as P → 2/7.** The rate of subjective time vanishes at the viability threshold — consciousness cannot "experience" its own disappearance.

---

## Connections

- **Derived from:** [Axiom Ω⁷](/docs/core/foundations/axiom-omega), [L-unification](/docs/proofs/physics/physics-correspondence#2-l-унификация)
- **Used in:** [Evolution](/docs/core/dynamics/evolution), [O-dimension](/docs/core/structure/dimension-o), [Viability](/docs/core/dynamics/viability)
- **Full proof:** [Theorem on Emergent Time](/docs/proofs/dynamics/emergent-time)
- **Lindblad operators:** [L_k — generators of dissipation](/docs/core/operators/lindblad-operators)
- **Critical purity:** [Theorem on purity](/docs/proofs/dynamics/theorem-purity-critical)
- **Emergent spacetime:** [Emergent manifold M⁴](/docs/proofs/physics/emergent-manifold)
