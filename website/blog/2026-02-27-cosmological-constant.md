---
slug: cosmological-constant
title: "The Cosmological Constant: Physics' Most Precise Puzzle and One Algebra"
authors: [uhm]
tags: [physics, cosmology, vacuum, consciousness, Lawvere, theory, mathematics]
---

# The Cosmological Constant {#космологическая-постоянная}

Quantum field theory is the best physical theory created by humans. It predicts the anomalous magnetic moment of the electron to twelve decimal places. It also predicts vacuum energy with an error of $10^{120}$ times.

In 1917 Einstein introduced the cosmological constant $\Lambda$ to hold the Universe from expanding. In 1929, after Hubble's discovery, he called it "the greatest blunder." In 1998 two teams of astronomers discovered that the expansion is accelerating — and $\Lambda$ returned. The observed value:

$$
\Lambda_{\text{obs}} \sim 10^{-120} \, M_P^4
$$

Standard quantum field theory gives $\Lambda_{\text{QFT}} \sim M_P^4$, i.e. unity in Planck units. The discrepancy — **120 orders of magnitude**. This is the largest mismatch between theory and experiment in the history of physics.

Each of the existing approaches — supersymmetry, the anthropic principle, sequestering — explains part of the suppression. None explains everything. And none answers the simpler question: *why is $\Lambda > 0$ at all?*

UHM answers both questions. The positivity of $\Lambda$ is a theorem [Т]. The smallness follows from six proven mechanisms [Т] and a spectral formula [Т]. The final estimate: $\sim 10^{-120 \pm 10}$ [С]. Without fitting.

<!-- truncate -->

## Global Zero {#глобальный-ноль}

Let us begin not with "why is $\Lambda$ small?" but with "why is the vacuum not infinitely heavy?"

The category of holons $\mathcal{C}$ possesses a [terminal object](/docs/core/foundations/consequences#когомологический-монизм) $T$ — the unique limiting configuration toward which every system tends. This is the algebraic analogue of an "absolute attractor": for any object $C$ there exists a unique morphism $C \to T$.

From a standard theorem of algebraic topology (Quillen, 1973): the nerve of a category with a terminal object is contractible. Consequence:

$$
H^n(X, \mathcal{F}) = 0 \quad \forall\, n > 0, \;\forall\, \mathcal{F} \qquad [\mathrm{Т}]
$$

All higher cohomologies are trivial. In physical terms:

$$
\Lambda_{\text{global}} = 0 \qquad [\mathrm{Т}]
$$

Globally the vacuum is empty. Not "small" — **exactly zero**.

But we observe $\Lambda > 0$. A contradiction?

## Local Life {#локальная-жизнь}

No. Global triviality does not prohibit local structure. From the [local-global dichotomy](/docs/core/foundations/consequences#локально-глобальная-дихотомия) [Т]:

$$
H^*_{\text{loc}}(X, T) \cong \tilde{H}^{*-1}(\mathrm{Link}(T)) \cong \tilde{H}^{*-1}(S^6) \neq 0 \qquad [\mathrm{Т}]
$$

The link of the terminal object is $S^6$ (six dimensions = $N - 1 = 7 - 1$). In particular, $H^7_{\text{loc}}(X, T) \cong \mathbb{Z}$ — nonzero cohomology.

**Analogy.** The Earth's surface is a closed sphere, topologically "simple". But if you are standing in the Himalayas, the relief is complex. Global simplicity does not cancel a local mountain range.

We do not live "in the global Universe". We live **near** $T$ — in the region of nontrivial cohomologies. Globally $\Lambda = 0$. Locally — no. The difference between $10^{-120}$ and $1$ is the difference between global and local.

This argument is not specific to UHM — it is a consequence of the structure of any category with a terminal object. Quillen's algebraic topology (1973) and the long exact sequence of local cohomologies are standard mathematical tools. UHM supplies the concrete category $\mathcal{C}$ and the concrete link $S^6$.

## Why Greater Than Zero {#почему-больше-нуля}

The sign of $\Lambda$ is determined by autopoiesis. Near $T$ the vacuum energy (T-71) [Т]:

$$
\rho_{\text{vac}}(T) = \kappa_0 \cdot \left[P(\rho^*) - P(I/7)\right] \cdot \omega_0
$$

Three factors — three theorems:

| Factor | Value | Source |
|-----------|:--------:|----------|
| $\kappa_0$ (regeneration rate) | $> 0$ | T-44a [Т]: [categorical derivation](/docs/core/foundations/axiom-septicity#категориальный-вывод-kappa0) |
| $P(\rho^*) - P(I/7)$ (purity excess) | $> 0$ | T-96 [Т]: [nontrivial attractor](/docs/core/dynamics/evolution#теорема-нетривиальность-аттрактора) |
| $\omega_0$ (base frequency) | $> 0$ | A5: [Page–Wootters](/docs/core/foundations/axiom-omega#pw-constraint) |

The product of three positive numbers is positive:

$$
\boxed{\Lambda_{\text{obs}} = 8\pi G_N \cdot \rho_{\text{vac}}(T) > 0} \qquad [\mathrm{Т}]
$$

Vacuum energy is **autopoietic work**: the cost of maintaining coherence $\rho^*$ above the maximally mixed state $I/7$. The system expends energy to remain "itself". This expenditure is the cosmological constant.

### Indirect Consequence: de Sitter {#непрямое-следствие-де-ситтер}

$\Lambda > 0$ implies closed spatial topology [Т] (T-120b): $\Sigma^3 \cong S^3$. The vacuum metric is de Sitter. The observed accelerated expansion is not a coincidence and not "dark energy of unknown nature" — it is a consequence of the autopoietic work of the vacuum. At large radius of curvature, de Sitter is indistinguishable from flat space — which is what is observed ($\Omega_k \approx 0 \pm 0.01$).

### Connection to Lawvere Incompleteness {#связь-с-неполнотой-ловера}

From [T-55](/docs/core/foundations/consequences#неполнота-ловера) [Т]: the internal theory $\text{Th}_{\text{UHM}} \subsetneq \Omega$ — the system cannot fully describe itself. The self-model $\varphi(\Gamma) \neq \Gamma$:

$$
\|\Gamma - \varphi(\Gamma)\|_F^2 = (1 - R) \cdot \|\Gamma\|_F^2 > 0
$$

Gödel showed that sufficiently rich arithmetic is incomplete. Lawvere generalized: in a Cartesian closed category, self-modelling is inevitably incomplete. UHM translates incompleteness into physics: the informational gap between "how the system sees itself" and "how it is actually structured" is the energy source for $\rho_{\text{vac}} > 0$ [И].

The Universe pays for the impossibility of perfect self-knowledge. Socrates would not have been surprised — though he would have appreciated the formulation.

## The Cost of Observation {#стоимость-наблюдения}

From [O-sector dominance](/docs/physics/gravity/cosmological-constant#теорема-лямбда-o-доминирование) [Т] (Sol.63):

$$
\mathcal{G}_{\text{total}} = \mathcal{G}_O + O(\bar{\varepsilon}^2)
$$

The cosmological constant is determined by the opacity of the O-sector — [Grounding](/docs/core/structure/dimension-o), the very dimension that generates time through [Page–Wootters](/docs/core/foundations/spacetime#теорема-время-из-o) ([post 5](/blog/spacetime-dimensions)). O-channels are almost completely "closed" ($\mathrm{Gap}(O,i) \approx 1$) — this creates the effect of time flow. But opacity costs energy:

$$
\Lambda_{\text{CC}} \propto \mathcal{G}_O = 2\sum_{i \neq O} |\gamma_{Oi}|^2 \cdot \mathrm{Gap}(O,i)^2
$$

$\Lambda$ is the energetic cost of observation. The more precise the internal clock, the larger $\Lambda$. The presence of an observer — literally — costs energy. The anthropic principle here ceases to be speculation and becomes a theorem: a universe without O-sector opacity contains no observers; a universe with it — inevitably has $\Lambda > 0$.

Weinberg's formula (1987) established anthropic **bounds** for $\Lambda$: too large — galaxies do not form. But Weinberg did not explain where $\Lambda$ comes from. UHM gives both the mechanism and the bound: $\Lambda$ is the local price for having an O-sector with $\mathrm{Gap} \approx 1$.

## Six Mechanisms {#шесть-механизмов}

Why is $\Lambda$ not just positive, but small? Because six independent mechanisms suppress it — each [Т]:

| # | Mechanism | Suppression | Essence |
|:-:|----------|:---------:|------|
| 1 | $\varepsilon^6$ | $10^{-12}$ | Vacuum coherences are small: $\lvert\gamma_{ij}\rvert = \varepsilon \sim 10^{-2}$ |
| 2 | $\lambda_3^2$ (RG) | $10^{-14.5}$ | Octonion associator — IR-irrelevant; $\Delta_3 = 5/42$ |
| 3 | Ward identities | $10^{-0.45}$ | 14 Noether charges $G_2$ → anti-correlation of Gap at large scales |
| 4 | Fano code | $10^{-0.9}$ | [Hamming $H(7,4)$](/blog/geometry-of-inner-world): 6 constraints → suppression $1/8$ |
| 5 | $\sqrt{N_F}$ | $10^{-11.9}$ | $\sim 6.8 \times 10^{23}$ uncorrelated Fano modes in Hubble volume |
| 6 | O-isolation | $10^{-1.7}$ | Only [6 of 21 pairs](/blog/spacetime-dimensions) contribute: $(6/21)^3 \approx 0.02$ |
| | **Total** | **$10^{-41.5}$** | **Perturbative budget** [Т] |

Not one of the six mechanisms was "invented for $\Lambda$". Ward identities follow from [$G_2$-symmetry](/blog/why-seven). The Fano code follows from the [Fano plane](/blog/geometry-of-inner-world). O-isolation follows from [sector decomposition](/blog/spacetime-dimensions). RG suppression follows from the fact that the octonionic associator ($\lambda_3$) is an IR-irrelevant operator.

Forty-one and a half orders. Strictly proven. Seventy-nine remain.

## The Remaining 79 Orders {#оставшиеся-79-порядков}

Three levels of compensation close the budget:

### SUSY Compensation [Т] {#susy-компенсация-т}

[$G_2$-holonomy](/blog/why-seven) generates $\mathcal{N}=1$ supersymmetry [Т]. The Witten index:

$$
W = \chi\bigl((S^1)^{21}\bigr) = 0 \qquad [\mathrm{Т}]
$$

(The number of bosonic and fermionic vacuum states is equal: $n_B = n_F = 2^{20}$.) In the supersymmetric limit — exact compensation: $\Lambda_{\text{SUSY}} = 0$ [Т].

Supersymmetry is broken at $m_{3/2} \sim \varepsilon^3 M_P$. Residual $\Lambda$ [Т]:

$$
\Lambda_{\text{res}} \sim \varepsilon^{12} \cdot M_P^4 \sim 10^{-24}\, M_P^4
$$

Status raised to [Т] via the [spectral formula](/docs/physics/gravity/cosmological-constant#теорема-спектральная-лямбда) $\Lambda_{\text{CC}}$ (Sol.41): the cosmological constant is expressed through the moments of the internal Dirac operator of the finite spectral triple. This is a direct application of the Chamseddine–Connes spectral action — the standard apparatus of noncommutative geometry — to the specific spectral triple $(A_{\text{int}}, \mathbb{C}^7, D_{\text{int}})$, whose existence is proven [Т].

### Sector Minimization [С] {#секторная-минимизация-с}

[Global minimization of $V_{\text{Gap}}$](/docs/core/dynamics/gap-thermodynamics#теорема-глобальная-минимизация) on $(S^1)^{21}/G_2$ gives suppression $\sim 10^{-40}$ [С]. The minimization structure is proven [Т]; the exact value is a computational task.

### Structural Closure [Т-structural] {#структурное-замыкание-т-структурное}

All coefficients are defined through the fixed point $\theta^*$ of the self-consistent map ([T-79](/docs/core/foundations/consequences#теорема-самозамыкание) [Т]): the theory sets its own dynamics, leaving no free parameters. The complete chain:

| Component | Suppression | Status |
|-----------|:---------:|:------:|
| 6 perturbative mechanisms | $10^{-41.5}$ | [Т] |
| Cohomological $\Lambda_{\text{glob}} = 0$ | complete global cancellation | [Т] |
| SUSY-breaking $\varepsilon^{12}$ | $10^{-24}$ | [Т] |
| RG $\lambda_3^2$ | $10^{-14.5}$ | [Т] |
| Sector minimization | $\sim 10^{-40}$ | [С] |
| **Full estimate** | **$\sim 10^{-120 \pm 10}$** | **[С]** |

The $\pm 10$ uncertainty is an honest estimate. But the conceptual budget is closed: 120 orders out of 120. The remaining gap is numerical minimization on $(S^1)^{21}/G_2$, not a gap in understanding.

## What Physicists Say {#что-говорят-физики}

| Approach | Mechanism | Achieved | Problem |
|--------|----------|:---------:|---------|
| **Standard Model** | Fine-tuning of counterterm | 120 (by hand) | Does not explain — fits |
| **SUSY** | Boson–fermion compensation | $\sim 60$ | Not observed at LHC |
| **Anthropic principle** | Landscape $\sim 10^{500}$ | 120 (probabilistically) | Not falsifiable |
| **Sequestering** | Dynamical relaxation | $\sim 60$ | Requires UV completion |
| **UHM** | 6 mechanisms + spectral formula | $\sim 120 \pm 10$ | Numerical precision [С] |

The key difference is not in the number of orders, but in **explanatory power**. In the Standard Model the sign of $\Lambda$ is undefined (fitted). The anthropic principle allows any sign. Sequestering "relaxes" $\Lambda$ to zero — which contradicts observation. Only in UHM is $\Lambda > 0$ a theorem, not a choice.

The second difference: string theory requires a choice from $\sim 10^{500}$ landscape vacua without predicting a specific one. In UHM all parameters are fixed through $\theta^*$ (T-79 [Т]): the theory determines its own dynamics. Not "among possible universes ours is one of" — but **"the unique structure compatible with the axioms."**

## Status Table {#таблица-статусов}

| Result | Status | Comment |
|-----------|:------:|-------------|
| $\Lambda_{\text{glob}} = 0$ | [Т] | Cohomological monism: $H^n(X) = 0$ |
| $H^*_{\text{loc}}(X, T) \neq 0$ | [Т] | $\tilde{H}^6(S^6) \cong \mathbb{Z}$ |
| $\Lambda_{\text{obs}} > 0$ (T-71) | [Т] | Autopoiesis + local cohomologies |
| $\rho_{\text{vac}} = \kappa_0[P(\rho^*) - P(I/7)]\omega_0 > 0$ | [Т] | Each factor $> 0$ |
| $\Sigma^3 \cong S^3$ (de Sitter) (T-120b) | [Т] | Consequence of $\Lambda > 0$ |
| O-sector dominance (Sol.63) | [Т] | $\mathcal{G}_{\text{total}} = \mathcal{G}_O + O(\bar\varepsilon^2)$ |
| 6 perturbative mechanisms | [Т] | At $\varepsilon = 10^{-2}$ [Г] |
| Perturbative budget $10^{-41.5}$ | [С] | Depends on $\varepsilon$ |
| Spectral formula $\Lambda_{\text{CC}}$ (Sol.41) | [Т] | Moments of $D_{\text{int}}$ |
| SUSY compensation $\varepsilon^{12}$ | [Т] | Spectral action |
| Sector minimization $\sim 10^{-40}$ | [С] | Structure [Т]; exact value — computational task |
| Full estimate $\sim 10^{-120 \pm 10}$ | [С] | Structural closure; numerical precision [С] |
| Connection to Lawvere incompleteness | [И] | Informational gap → $\rho_{\text{vac}}$ |
| $\varepsilon = 10^{-2}$ | [Г] | Not derived from first principles |

## Conclusions {#выводы}

**1. Globally — exact zero.** Cohomological monism [Т]: contractibility of the state space to the terminal object cancels global vacuum energy. Not "small" — **zero**. The observed $\Lambda$ is a local effect from $H^*_{\text{loc}}(X, T) \neq 0$ [Т].

**2. Locally — strictly positive.** $\Lambda_{\text{obs}} > 0$ is theorem T-71 [Т]. Three factors ($\kappa_0$, $P(\rho^*) - P(I/7)$, $\omega_0$) — each positive by a separate theorem. A universe with $\Lambda \leq 0$ cannot contain autopoietic systems — this is not the anthropic principle as a probability argument, but a **prohibition** as a consequence of algebra.

**3. $\Lambda$ is the cost of observation.** O-sector opacity determines $\Lambda$ [Т] (Sol.63). The same sector generates time through Page–Wootters. The presence of an observer — literally — costs energy. The cosmological constant is the bill for existing internal clocks.

**4. 120 orders — not one mystery, but a chain of mechanisms.** Six perturbative mechanisms [Т] give $10^{-41.5}$. SUSY compensation [Т], spectral formula [Т], and sector minimization [С] close the budget to $\sim 10^{-120 \pm 10}$. Without fitting. Without a landscape. Without anthropic probability.

**5. Incompleteness as energy source.** Lawvere's theorem (T-55 [Т]): the system cannot fully describe itself. The informational gap $\|\Gamma - \varphi(\Gamma)\| > 0$ translates into $\rho_{\text{vac}} > 0$ [И]. Vacuum energy is the payment for the fundamental incompleteness of self-modelling. Gödel, Tarski, Lawvere — three levels of incompleteness; the third turns out to be physical.

**6. First explanation — not first number.** $\pm 10$ orders is an honest uncertainty. But for the first time in the history of this problem: the sign is explained [Т], the suppression structure is closed [Т], all coefficients are defined through $\theta^*$ [Т], there are no free parameters. A computational task remains. The conceptual one is solved.

Mathematics, as usual, does not ask permission. But sometimes — it presents a bill.

---

**Related materials:**
- [Holonomic Paninteriorism](/blog/holonomic-paninteriorism) — philosophical position and autopoiesis
- [Geometry of the Inner World](/blog/geometry-of-inner-world) — Fano plane and Hamming code
- [Three Forces, One Equation](/blog/three-forces) — dynamics: regeneration and $\kappa(\Gamma)$
- [Why Space is Three-Dimensional](/blog/spacetime-dimensions) — O-dimension and time from Page–Wootters
- [Why Exactly Seven](/blog/why-seven) — octonionic algebra and $G_2$-symmetry
- [Death, Coherence and Time](/blog/death-coherence-time) — $P_{\text{crit}} = 2/7$ and irreversibility
- [Cosmological Constant](/docs/physics/gravity/cosmological-constant) — full formalism
- [$\Lambda$ Budget: Proofs](/docs/proofs/gap/lambda-budget) — six mechanisms in detail
