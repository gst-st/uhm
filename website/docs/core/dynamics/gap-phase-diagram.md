---
sidebar_position: 8
title: "Gap Phase Diagram"
slug: /core/dynamics/gap-phase-diagram
description: "Three Gap phases (ordered, intermediate, disordered), bifurcations, Whitney catastrophes, swallowtail and levels L0→L4, non-Markovian oscillations, critical phenomena"
---

# Gap Phase Diagram

:::info Who this chapter is for
Three phases of coherence, critical phenomena, bifurcations. Assumes familiarity with the [Gap operator](/docs/core/dynamics/gap-operator) and [Gap thermodynamics](/docs/core/dynamics/gap-thermodynamics).
:::

This chapter presents a **map of all possible states** of holon opacity. Just as the phase diagram of water shows at what temperature and pressure water exists as ice, liquid, or steam, the Gap phase diagram shows under what conditions the system's opacity is **ordered** (specific channels are transparent, others are not), **disordered** (all channels are equally murky), or **dead** (coherences have disappeared).

The reader will learn:
- The three Gap phases and how they relate to clinical states
- Critical phenomena and phase transitions between phases
- How the swallowtail catastrophe connects Gap to levels of consciousness L0--L4
- Five independent mechanisms protecting Gap from disappearing

:::tip Water analogy
The three Gap phases are strikingly similar to the three phases of water:

| Water phase | Gap phase | What happens |
|-----------|----------|----------------|
| **Ice** (ordered) | **Phase I** — ordered Gap | Water molecules are arranged in a crystal lattice. Analogously: some channels are transparent, others opaque — there is **structure**. The system "knows" where its blind spots are. |
| **Water** (liquid) | **Phase II** — disordered Gap | Molecules move chaotically but remain bound. Analogously: all channels are **equally murky**. Opacity exists, but without structure — a "diffuse fog." |
| **Steam** (gas) | **Phase III** — dead zone | Molecules have dispersed, no bonds remain. Analogously: coherences have **disappeared**, Gap is undefined. The system is non-viable. |

The ice $\to$ water transition (phase I $\to$ II) is **continuous** (2nd order): the structure gradually "blurs." The ice $\to$ steam transition (phase I $\to$ III) is **discontinuous** (1st order): the system abruptly loses coherence, as in acute decompensation.
:::

The full phase diagram of [Gap dynamics](/docs/core/dynamics/gap-dynamics) describes the stationary opacity regimes of the holon in the plane of control parameters $(T_{\text{eff}}, \kappa/\Gamma_2)$. Three main phases, critical phenomena, and Whitney catastrophes connect Gap thermodynamics with [levels of interiority](/docs/consciousness/hierarchy/interiority-hierarchy) and clinical observations.

---

## 1. Control parameters {#параметры}

Two dimensionless parameters determine the stationary Gap state:

**(a)** Dimensionless temperature:

$$
t := \frac{T_{\text{eff}}}{T_c} = \frac{\Gamma_2}{\kappa_0} \cdot \frac{k_B T_{\text{phys}} \ln 21}{\mu^2}
$$

where $T_{\text{eff}} = (\Gamma_2 / \kappa_0) \cdot k_B T_{\text{phys}}$ is the [effective temperature](/docs/core/dynamics/gap-thermodynamics#эффективная-температура).

**(b)** Ratio of regeneration to dissipation:

$$
r := \kappa / \Gamma_2
$$

— dimensionless "viability" parameter.

---

## 2. Three phases {#три-фазы}

:::tip Theorem 2.1 (Gap phase diagram) [Т]
In the $(t, r)$ plane the system has three phases:

**(a) Phase I — Ordered Gap** ($t < 1$, $r > r_c$):
a few channels with high Gap, the rest transparent. $G_2 \to H$ spontaneously broken. Goldstone modes exist. Order parameter: $\mathcal{G}_{\text{total}} > 0$, rank $\hat{\mathcal{G}} \in \{1, 2, 3\}$.

**(b) Phase II — Disordered Gap** ($t > 1$, $r > r_c$):
Gap distributed uniformly across all channels. Anisotropy $\sigma^2_{\text{Gap}} \to 0$. $G_2$ approximately preserved. Note: the stationary formula $\mathrm{Gap}^{(\infty)}(i,j) = |\sin(\theta_{ij} - \arctan(\ldots))|$ from the [unified theorem](/docs/core/dynamics/gap-dynamics#единая-теорема) admits inhomogeneous $\theta_{ij}$, but at $T_{\text{eff}} > T_c$ thermal fluctuations randomize phases, making the **time-averaged** Gap isotropic.

**(c) Phase III — Dead zone** ($r < r_c$):
regeneration is too weak, coherences decay: $|\gamma_{ij}| \to 0$. The system is not [viable](/docs/core/dynamics/viability).
:::

### Order parameters of the three phases

For each phase, explicit order parameters are defined to quantitatively distinguish regimes:

| Phase | Primary order parameter | Secondary parameter | Behavior |
|---|---|---|---|
| I (ordered) | $\sigma^2_{\text{Gap}} := \mathrm{Var}\bigl(\{\mathrm{Gap}(i,j)\}\bigr) > 0$ | $\mathrm{rank}(\hat{\mathcal{G}}) \in \{1,2,3\}$ | Nonzero anisotropy, G₂ broken to $H_{\hat{\mathcal{G}}_*}$ |
| II (disordered) | $\sigma^2_{\text{Gap}} \to 0$ | $\mathcal{G}_{\text{total}} > 0$, but $\mathrm{Gap}(i,j) \approx \mathrm{const}$ | Isotropic murkiness, G₂ approximately preserved |
| III (dead) | $\mathcal{G}_{\text{total}} \to 0$ | $\lvert\gamma_{ij}\rvert \to 0 \;\forall\, (i,j)$ | Coherences die out, Gap undefined |

:::note Remark [Т]
The order parameter $\sigma^2_{\text{Gap}}$ vanishes continuously on the transition line I $\leftrightarrow$ II ($t = 1$), characterizing a **second-order** transition. On the line I $\leftrightarrow$ III ($r = r_c$) the total Gap $\mathcal{G}_{\text{total}}$ undergoes a **discontinuity** — a first-order transition.
:::

Critical value:

$$
r_c = \frac{P_{\text{crit}}}{7P} \approx \frac{2}{49P}
$$

### Phase diagram visualization

```
    t (T_eff/T_c)
    │
  2 ┤         Phase II: Disordered Gap
    │        (uniform, recoverable)
    │
  1 ┤─ ─ ─ ─ ─ ─ ─ ─ ╋ ─ ─ ─ ─ ─ ─ ─ ─ ─
    │               ╱ (t*,r*)
    │   Phase I   ╱   ← 2nd order (continuous)
    │  Ordered   ╱
    │   Gap     ╱
    │          ╱
  0 ┤─────────╱─────────────────────────────
    │ Ph. III │
    │  Dead   │
    └────────┼────────┼─────────────────── r (κ/Γ₂)
             r_c      1
```

### Phase transition lines

| Transition | Line | Order | Characteristic |
|---|---|---|---|
| I ↔ II | $t = 1$ at $r > r_c$ | 2nd (continuous) | $\beta = 1/2$ (Landau class) |
| I ↔ III | $r = r_c$ at $t < 1$ | 1st (discontinuous) | $\mathcal{G}_{\text{total}}$ jumps → 0 |
| Tricritical | $(t^*, r^*) = (1, r_c)$ | Order change | $\beta = 1/4$, $\gamma = 1$, $\delta = 5$ |

---

## 3. Clinical correspondence {#клиническое-соответствие}

:::info Theorem 3.1 (Correspondence of phases to clinical states) [И]

| Phase | Clinical analogue | Characteristic |
|---|---|---|
| I (ordered) | Normal functioning | Specific opacities (repression), transparency in other channels |
| II (disordered) | Diffuse dissociative state | All channels equally murky |
| III (dead) | Dementia, coma, clinical death | Loss of coherences |
| I ↔ II transition | Psychotic episode | "Melting" of structured opacity |
| I ↔ III transition | Acute decompensation | Discontinuous collapse under resource exhaustion |
| Tricritical | Borderline state | Oscillation between ordered and chaotic Gap |
:::

---

## 4. Gap-landscape bifurcations {#бифуркации}

:::note Canonical definition
The definition of the Gap landscape ($\mathcal{G}: \mathcal{D}(\mathbb{C}^7) \to [0,1]^{21}$), three types of bifurcations (pitchfork, saddle-node, Hopf), and their clinical analogues are described in detail in [Gap Dynamics, sections 3.1–3.3](/docs/core/dynamics/gap-dynamics#бифуркации). Only aspects specific to the phase diagram are considered here.
:::

In the $(t, r)$ plane, bifurcations of the Gap landscape generate the phase transition lines (section 2). Key types: **pitchfork** (spontaneous breaking of Gap-profile symmetry), **saddle-node** (disappearance of a stationary profile), and **Hopf** (transition to an oscillatory regime). Detailed formulas and proofs are given in [Gap dynamics](/docs/core/dynamics/gap-dynamics#бифуркации).

---

## 5. Whitney catastrophes {#катастрофы-уитни}

The basic catastrophes (fold, cusp) are described in [Gap Dynamics, section 3.4](/docs/core/dynamics/gap-dynamics#бифуркации). Here we consider their extension to the **swallowtail** ($A_4$) with 3 control parameters and the connection with [levels of interiority](/docs/consciousness/hierarchy/interiority-hierarchy).

### Swallowtail and levels L0 → L4

:::tip Theorem 5.2 (Swallowtail cascade and L-levels) [Т]
With 3 control parameters $(\kappa, \alpha, \Delta F)$, a **swallowtail** appears — a catastrophe with 4 sheets. Proved via Arnold's theorem (1972): codimension 3, approximate $\mathbb{Z}_2$-symmetry of purity $\Rightarrow$ $A_4$-bifurcation. See [$A_4$-bifurcation](/docs/consciousness/hierarchy/interiority-hierarchy#теорема-a4-бифуркация).

Correspondence of swallowtail sheets to [interiority levels](/docs/consciousness/hierarchy/interiority-hierarchy):

| Swallowtail sheet | Level | Characteristic |
|---|---|---|
| Outer stable | L0–L1 | Stationary Gap, unconscious |
| Intermediate | L2 | Partially conscious Gap, metastable |
| Inner unstable | L3 | Near-full Gap awareness |
| Self-intersection point | L4 | Fixed point $\varphi(\Gamma^*) = \Gamma^*$ |
:::

### Tristability and quantitative swallowtail model

Normal form of the swallowtail catastrophe ($A_4$) for the effective Gap potential:

$$
V_{\text{eff}}(G) = G^5 + a\,G^3 + b\,G^2 + c\,G
$$

where $(a, b, c)$ are the three control parameters. The stationary condition $\partial V_{\text{eff}}/\partial G = 0$ gives a degree-four polynomial admitting up to **three stable minima** under the standard swallowtail catastrophe conditions (Arnold, 1975):

$$
|a| > \sqrt[3]{27b^2/4}, \quad c \in (c_{\min}(a,b),\, c_{\max}(a,b))
$$

:::tip Theorem 5.3 (Three minima of the Gap potential and L-levels) [Т]
Three stable Gap profiles are identified with ranges of the interiority hierarchy:

| Minimum | $G$ | Reflection | L-level | Clinical |
|---|---|---|---|---|
| $G_{\text{high}} \approx 0.8$ | High | $R \approx 0$ | L0/L1 | Basic interiority, alexithymia |
| $G_{\text{mid}} \approx 0.4$ | Medium | $R > 0$ | L2 | Normal functioning |
| $G_{\text{low}} \approx 0.1$ | Low | $R \gg 0$ | L3+ | Reflective / metacognitive consciousness |
:::

**Transitions between L-levels** — first-order phase transitions (fold bifurcations): [Т]

- **L1 $\to$ L2** (awakening of consciousness): fold bifurcation at $\kappa > \kappa_{\text{fold}}$; Gap drops discontinuously from $G_{\text{high}}$ to $G_{\text{mid}}$.
- **L2 $\to$ L3** (insight): fold bifurcation at $\kappa > \kappa'_{\text{fold}}$; Gap drops discontinuously from $G_{\text{mid}}$ to $G_{\text{low}}$.
- Reverse transitions occur at **smaller** values of $\kappa$ (hysteresis). Hysteresis width:

$$
\Delta\kappa_{L1 \to L2} = \frac{\lambda_3 \bar{A}_1}{\mu^2}, \qquad \Delta\kappa_{L2 \to L3} = \frac{\lambda_3 \bar{A}_2}{\mu^2}
$$

- **Direct jump L1 $\to$ L3** is possible with simultaneous control of all three parameters — a swallowtail path bypassing the intermediate minimum. Necessary condition:

$$
\lambda_3 \bar{A} < \frac{4\mu^6}{27\lambda_4^2}
$$

— suppression of octonionic non-associativity below the swallowtail threshold. [Т]

:::tip Status of the swallowtail model [Т]
Theorems 5.2 and 5.3 are proved via Arnold's theorem (1972): three physically independent control parameters $(\kappa, \alpha, \Delta F)$ and the approximate $\mathbb{Z}_2$-symmetry of purity uniquely determine codimension 3 and catastrophe type $A_4$ (swallowtail). The identification of sheets with L-levels is a consequence of the structure of the evolution equation. Full proof: [$A_4$-bifurcation](/docs/consciousness/hierarchy/interiority-hierarchy#теорема-a4-бифуркация).
:::

---

## 6. Non-Markovian Gap oscillations {#немарковские-осцилляции}

The basic theory of non-Markovian oscillations (exponential memory kernel, three regimes: Markovian, oscillatory, overdamped) is presented in [Gap Dynamics, section 4](/docs/core/dynamics/gap-dynamics#немарковские-эффекты). Here we consider extensions specific to the phase diagram: the generalized FDT and Fibonacci frequencies.

### 6.1 Non-Markovian FDT for Gap [Т]

For non-Markovian dynamics with an arbitrary memory kernel $K(\tau)$, the fluctuation-dissipation theorem is generalized. Equation of motion:

$$
\frac{d\,\mathrm{Gap}(i,j;\tau)}{d\tau} = -\int_0^\tau K(\tau - \tau')\,\mathrm{Gap}(i,j;\tau')\,d\tau' + \xi_{ij}(\tau)
$$

Generalized FDT in frequency space:

$$
\chi_{ij}(\omega) = \frac{1}{T_{\text{eff}}} \cdot \frac{\widetilde{C}_{ij}(\omega)}{\mathrm{Re}\bigl[\widetilde{K}(\omega)\bigr]}
$$

where $\widetilde{K}(\omega) = \int_0^\infty K(\tau)\,e^{i\omega\tau}\,d\tau$ is the Fourier transform of the memory kernel.

For the exponential kernel $K(\tau) = (\Gamma_2^2/\tau_M)\,e^{-\tau/\tau_M}$:

$$
\chi_{ij}(\omega) = \frac{1 + \omega^2\tau_M^2}{T_{\text{eff}}\,\Gamma_2^2\,\tau_M} \;\widetilde{C}_{ij}(\omega)
$$

At $\omega\tau_M \gg 1$: $\chi \propto \omega^2$ — **anti-resonance**. A system with memory responds more strongly to high-frequency perturbations. This explains the effectiveness of repeated short therapeutic sessions compared to infrequent long ones. [С]

:::warning Status of non-Markovian FDT [С]
The generalized FDT for non-Markovian dynamics is correct provided that the memory kernel $K(\tau)$ describes linear response (regime of small deviations from the stationary state). Applicability to real neurobiological systems, where nonlinearities are significant, is not established.
:::

### 6.2 Fibonacci frequencies and the golden ratio [И]

:::warning Hypothesis (Fibonacci frequencies of Gap oscillations) [И]
If the eigenfrequencies of the effective Hamiltonian $H_{\text{eff}}$ follow the Fibonacci series:

$$
\omega = (0, 1, 2, 3, 5, 8, 13) \quad \text{(normalized)}
$$

then the difference frequencies $|\omega_i - \omega_j|$ determine Gap oscillations:

$$
\mathrm{Gap}(i,j;\tau) = \bigl|\sin\bigl(\theta_{ij}(0) + (\omega_i - \omega_j)\tau\bigr)\bigr|
$$

Pairs with rational ratios $\Delta\omega/\Delta\omega'$ have **periodic** transparency windows. Pairs with irrational ratios fill $[0,1]$ **ergodically** — Gap takes all values with equal probability.

Since the ratio of successive Fibonacci numbers converges to the **golden ratio** $\varphi = (1+\sqrt{5})/2 \approx 1.618$ — the most irrational number — most difference frequencies are mutually irrational. Consequence: full transparency ($\mathrm{Gap} = 0$) is an unreachable **limit**, not a stationary state.
:::

If this hypothesis is correct, it entails a concrete prediction: the power spectrum of Gap oscillations must contain peaks at frequencies $f_n = (\omega_i - \omega_j) \cdot f_0$, where $f_0$ is the base frequency and the ratios of peaks approach $\varphi$. Verification — via analysis of infra-slow fluctuations in resting-state fMRI. [И]

---

## 7. Critical phenomena {#критические-явления}

:::tip Theorem 7.1 (Critical exponents) [Т]
Near the critical point $t = 1$ (transition I ↔ II) the system exhibits scale-invariant behavior:

**(a)** Order parameter: $\sigma_{\text{Gap}}^2 \propto (1 - t)^{2\beta}$, $\beta = 1/2$ (mean-field)

**(b)** Susceptibility: $\chi \propto |1 - t|^{-\gamma}$, $\gamma = 1$

**(c)** Correlation length: $\xi \propto |1 - t|^{-\nu}$, $\nu = 1/2$
:::

The universality class is **Landau** (mean-field), which is natural for a system with long-range coherences.

### 7.1 Full table of critical exponents [Т]

Near the transition line I $\leftrightarrow$ II ($t = 1$) and at the tricritical point $(t^*, r^*) = (1, r_c)$ the critical exponents take the following values:

| Exponent | Definition | On line $t = 1$ (Landau) | At tricritical point | Physical meaning |
|---|---|---|---|---|
| $\beta$ | $\sigma_{\text{Gap}}^2 \propto (1-t)^{2\beta}$ | $1/2$ | $1/4$ | Growth of order parameter |
| $\gamma$ | $\chi \propto \lvert 1-t\rvert^{-\gamma}$ | $1$ | $1$ | Divergence of susceptibility |
| $\nu$ | $\xi \propto \lvert 1-t\rvert^{-\nu}$ | $1/2$ | $1/2$ | Divergence of correlation length |
| $\alpha$ | $C \propto \lvert 1-t\rvert^{-\alpha}$ | $0$ (log.) | $1/2$ | Heat capacity anomaly |
| $\delta$ | $h \propto \sigma_{\text{Gap}}^{\delta}$ at $t = 1$ | $3$ | $5$ | Critical isotherm |

:::tip Theorem 7.2 (Accuracy of mean-field exponents) [Т]
Mean-field critical exponents are **exact** for the Gap system by three independent rigorous mechanisms — Thom-Arnold topological rigidity of the $A_4$ (swallowtail) catastrophe, deterministic (non-stochastic) UHM dynamics, and large-$N$ cross-check with $d_{\mathrm{eff}} = \binom{7}{2} = 21$ order-parameter modes — unified in [Exactness mechanism](/docs/consciousness/hierarchy/swallowtail-transitions#механизм-точности) [Т].

**(a)** Order-parameter dimension $d_{\text{eff}} = 21$ = number of independent off-diagonal coherences of $\Gamma \in \mathcal D(\mathbb C^7)$. This is the genuine count of fluctuation modes in any stochastic reinterpretation of the dynamics.

**(b)** The spatial-dimension form of the Ginzburg criterion does **not** apply, because UHM is $(0{+}1)$-dimensional (no spatial integration). Mean-field exactness is instead established topologically (Thom-Arnold) and dynamically (deterministic flow).

**(c)** Near the tricritical point the effective theory is $\varphi^6$, an $A_4$ catastrophe with codimension 3 matching UHM's three physical control parameters $(\kappa, \gamma_{\text{Lindblad}}, \Delta F)$. Exponents $\{\alpha,\beta,\gamma,\nu,\delta\} = \{1/2, 1/4, 1, 1/2, 5\}$ are topological invariants of the $A_4$ class.
:::

:::note On independence of the 21 coherence modes
The count $d_{\text{eff}} = \binom{7}{2} = 21$ refers to the 21 independent off-diagonal pairs $(i,j)$ with $1 \le i < j \le 7$, matching the $42 = 21\cdot 2$ real off-diagonal components of $\mathfrak{su}(7)$. $G_2 \subset SO(7)$ reduces this to $21 - 14 = 7$ $G_2$-invariant modes in the deep-broken phase, but the full $21$ enter the fluctuation counting near threshold (before $G_2$-fixing) — consistent with the catastrophe-theoretic count of codimension-3 $A_4$ deformations. This does not change the topological protection of the exponents in (I).
:::

Scaling relations:

$$
\alpha + 2\beta + \gamma = 0 + 1 + 1 = 2 \quad \checkmark \quad \text{(Rushbrooke's law)}
$$

:::info Remark on Josephson's law [О]
The hyperscaling relation $d\nu = 2 - \alpha$ holds at $d = d_c = 4$ (upper critical dimension), but **fails** at $d_{\text{eff}} = 21 > d_c$. This is expected behavior: above the upper critical dimension hyperscaling does not hold, mean-field exponents apply without hyperscaling corrections.
:::

---

## 8. Goldstone modes {#голдстоуновские-моды}

Under spontaneous breaking $G_2 \to H_{\hat{\mathcal{G}}_*}$, Goldstone modes arise — slow collective oscillations of the Gap profile.

:::tip Theorem 8.1 (Quasi-Goldstone modes) [Т]
In an open (dissipative) system:

**(a)** Modes are **quasi-massive** (not strictly massless): $m_{\text{Gold}}^2 = \Gamma_2 \cdot \kappa_0 / |\gamma|^2$.

**(b)** Each mode redistributes Gap between pairs while preserving $\mathcal{G}_{\text{total}}$:

$$
\delta\mathrm{Gap}(i,j) = \sum_a \epsilon_a \cdot [T_a, \hat{\mathcal{G}}_*]_{ij}
$$

**(c)** The number of modes depends on the opacity rank:

| Rank | $n_{\text{Gold}}$ | Prediction for ISF |
|---|---|---|
| 1 | 6 | 6 independent ISF components |
| 2 | 10 | 10 ISF components |
| 3 | 12 | 12 ISF components |

**(d)** Frequency: $f_{\text{Gold}} \sim 0.005$–$0.02$ Hz — coincides with infra-slow neuronal fluctuations (ISF) in fMRI.
:::

### 8.1 Excitation spectrum around spontaneous Gap [Т]

Near the minimum of $V_{\text{Gap}}$, the full space of small oscillations $\theta_{ij} = \theta^*_{ij} + \delta\theta_{ij}$ splits into three sectors:

| Sector | Number of modes | Frequency | Physical meaning |
|---|---|---|---|
| Massive | $21 - n_{\text{broken}} - n_{\text{top}}$ | $\omega_{\text{mass}}^2 = \mu_{\text{eff}}^2 + \kappa/m$ | Oscillations perpendicular to the $G_2$ orbit |
| Quasi-Goldstone | $n_{\text{broken}} = 14 - \dim(H)$ | $\omega_{\text{Gold}}^2 = \kappa/m - \Gamma_2^2/(4m^2)$ | Slow redistribution of Gap along the orbit |
| Topologically protected | $0$ or $1$ | Determined by $Q_{\text{top}}$ | Cannot decay without a phase transition |

Total number of modes: $n_{\text{mass}} + n_{\text{Gold}} + n_{\text{top}} = 21$ — equal to the number of independent coherences $\binom{7}{2}$.

At $\kappa > \Gamma_2^2/(4m)$ quasi-Goldstone modes undergo **damped oscillations**. At $\kappa < \Gamma_2^2/(4m)$ — **aperiodic decay** (overdamped regime). In the limiting case of an isolated system ($\Gamma_2 \to 0$), Goldstone modes become strictly massless: $\omega_{\text{Gold}} \to \sqrt{\kappa/m}$ as $m_{\text{Gold}} \to 0$. [Т]

### 8.2 Broken symmetries and number of modes [Т]

**Definition [О].** {#стабилизатор-gap} Isotropy subgroup (stabilizer) of the stationary Gap configuration:

$$H_{\hat{\mathcal{G}}_*} := \{g \in G_2 : \mathrm{Ad}_g(\hat{\mathcal{G}}_*) = \hat{\mathcal{G}}_*\}$$

where $\mathrm{Ad}_g$ is the adjoint action of $G_2$ on $\mathfrak{so}(7)$. Number of broken generators: $n_{\text{broken}} = 14 - \dim(H_{\hat{\mathcal{G}}_*})$.

The full $G_2$-symmetry of the Lagrangian is broken by the stationary state to the stabilizer subgroup:

$$
G_2 \to H_{\hat{\mathcal{G}}_*}, \quad n_{\text{broken}} = 14 - \dim(H_{\hat{\mathcal{G}}_*})
$$

| Rank $\hat{\mathcal{G}}_*$ | Stabilizer $H$ | $\dim(H)$ | $n_{\text{broken}}$ | Space $G_2/H$ |
|---|---|---|---|---|
| $0$ | $G_2$ | $14$ | $0$ | $\{\mathrm{pt}\}$ |
| $1$ | $SU(3)$ | $8$ | $6$ | $G_2/SU(3) \cong S^6$ |
| $2$ | $SU(2) \times U(1)$ | $4$ | $10$ | $10$-dim. |
| $3$ (generic) | $T^2$ | $2$ | $12$ | $12$-dim. |
| $3$ (degen.) | $SU(2)$ | $3$ | $11$ | $11$-dim. |

The discrete $PT$-symmetry ($\theta \to -\theta$, $\tau \to -\tau$) is broken by the cubic term $V_3$ of the potential already at the Lagrangian level — the stationary state inherits this breaking. [Т]

---

## 9. Five types of Gap protection {#защита-gap}

Taking all results into account, **five independent mechanisms** of Gap irremovability are established:

| # | Protection type | Source | Mechanism |
|---|---|---|---|
| 1 | Code-theoretic | [Gap dynamics](/docs/core/dynamics/gap-dynamics#код-хэмминга) | Hamming bound H(7,4): $\geq 3$ nonzero Gaps |
| 2 | Algebraic | [Gap operator](/docs/core/dynamics/gap-operator#g2-разложение) | Octonionic associator $[e_i,e_j,e_k] \neq 0$ |
| 3 | Energetic | [Gap thermodynamics](/docs/core/dynamics/gap-thermodynamics) | Spontaneous minimum $V_{\text{Gap}} \neq 0$ from $V_3$ |
| 4 | Categorical | [Self-observation](/docs/consciousness/foundations/self-observation) | Lawvere's theorem: the fixed point cannot be trivial |
| 5 | Topological | [Gap operator](/docs/core/dynamics/gap-operator#стабилизаторы) | $\pi_2(G_2/T^2) \cong \mathbb{Z}^2$ |

---

## 10. Ward identities for Gap correlators {#тождества-уорда}

$G_2$-invariance of the Lagrangian generates **14 linear relations** between Gap correlators — an analogue of Ward identities in quantum field theory. [Т]

:::tip Theorem 10.1 (Ward identities) [Т]
For the $n$-point correlator $G^{(n)}\bigl((i_1,j_1,\tau_1),\ldots,(i_n,j_n,\tau_n)\bigr) := \langle\mathrm{Gap}(i_1,j_1;\tau_1)\cdots\mathrm{Gap}(i_n,j_n;\tau_n)\rangle$:

**(a)** For each generator $T_a \in \mathfrak{g}_2$:

$$
\sum_{i<j} [T_a]_{ij}\,\frac{\partial}{\partial\theta_{ij}}\,G^{(n)} = 0
$$

**(b)** For the two-point correlator $C_{(ij),(kl)}(\tau) = \langle\mathrm{Gap}(i,j;\tau)\;\mathrm{Gap}(k,l;0)\rangle$:

$$
\sum_{m}\bigl([T_a]_{im}\,C_{(mj),(kl)} + [T_a]_{jm}\,C_{(im),(kl)}\bigr) = 0
$$

**(c)** Number of independent two-point correlators accounting for the 14 identities:

$$
N_{\text{corr}} = \frac{21 \times 22}{2} - 14 = 217
$$
:::

**Experimental verification of $G_2$-symmetry.** The degree of Ward identity violation is a measure of $G_2$-symmetry breaking:

$$
\Delta_{G_2}^{(\text{exp})} := \max_a \Bigl\|\sum_m [T_a]_{im}\,C_{(mj),(kl)} + [T_a]_{jm}\,C_{(im),(kl)}\Bigr\|
$$

At $\Delta_{G_2}^{(\text{exp})} = 0$: full $G_2$-symmetry. At $\Delta_{G_2}^{(\text{exp})} > 0$: partial breaking. This is the first operational protocol for verifying $G_2$-structure in experimental data (neuroimaging, AI metrics, psychometrics). [О]

---

## Related documents

- [Gap operator](/docs/core/dynamics/gap-operator) — definition of $\hat{\mathcal{G}}$, spectrum, G₂ decomposition
- [Gap dynamics](/docs/core/dynamics/gap-dynamics) — bifurcations, Choi–Jamiołkowski, Hamming
- [Gap thermodynamics](/docs/core/dynamics/gap-thermodynamics) — Lagrangian, $V_{\text{Gap}}$, $T_{\text{eff}}$
- [Interiority hierarchy](/docs/consciousness/hierarchy/interiority-hierarchy) — levels L0–L4
- [Proofs: Fano channel](/docs/proofs/gap/fano-channel) — G₂-covariance of the Fano dissipator
- [Coherence matrix](/docs/core/dynamics/coherence-matrix) — definition of $\gamma_{ij}$, order parameter
- [Symbolic systems](/docs/core/structure/symbolic-systems) — octonionic algebra and structure constants
