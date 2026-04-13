---
sidebar_position: 2
title: "Berry Phase and Topological Protection"
slug: /physics/cosmology-phys/berry-phase
description: "Berry phase as the source of topological protection of the Gap, connection to G₂/H-orbits, Fano Gap bound, refutation of the CS derivation, and uniqueness of the bilinear form B^(b)"
---

# Berry Phase and Topological Protection

:::info Who This Chapter Is For
The Berry phase as the source of topological protection of the Gap structure. The reader will learn about the connection between the geometric phase and $G_2$-orbits and the Fano Gap bound.
:::


## Overview

The topological term of the Gap Lagrangian is determined not by the Chern-Simons functional (that derivation has been **refuted**), but by the **Berry phase** (geometric phase) given by the associative 3-form of $G_2$. The Berry phase provides **topological protection** of the Gap: there exist pairs of dimensions for which $\mathrm{Gap}(i,j) > 0$ for structural reasons that cannot be eliminated by any local deformation of the parameters.

---

## 1. Definition of the Berry Phase

Let the context parameter $\lambda \in M$ (a manifold of contexts) define the effective Hamiltonian $H_{\mathrm{eff}}(\lambda)$. Under adiabatic motion along a closed loop $\gamma: [0,T] \to M$, the system acquires a **geometric Berry phase**:

$$
\Phi_B = \oint_\gamma \mathcal{A}(\lambda) \cdot d\lambda
$$

where $\mathcal{A}(\lambda) = i\langle n(\lambda)|\nabla_\lambda|n(\lambda)\rangle$ is the Berry connection for the $n$-th eigenstate.

---

## 2. Topologically Protected Gap

:::warning Theorem 5.1 [H] — **superseded by T-64 [T]**
**Status:** The hypothesis about $\pi_1(M) \neq 0$ has been superseded by a proven result. T-64 [T] establishes topological protection of the Gap through a different, rigorously proven mechanism: a positive-definite Hessian $+$ $\pi_2(G_2/T^2) \cong \mathbb{Z}^2$ provide an energy barrier $\Delta V \geq 6\mu^2 > 0$ (see [vacuum uniqueness](/docs/proofs/categorical/uniqueness-theorem)). The original formulation via the Berry phase and $\pi_1(M)$ is no longer required.

If $M$ contains non-contractible loops ($\pi_1(M) \neq 0$), then there exist pairs of dimensions $(i, j)$ with a **topologically protected** Gap:

$$
\mathrm{Gap}_{\mathrm{topo}}(i,j) = |\sin(\Phi_B^{(i)} - \Phi_B^{(j)})| > 0
$$

which cannot be eliminated by any local deformation of the parameters.
:::

**Argument:**

**(a)** The Berry phase is a topological invariant determined by the homotopy class of the loop in $M$. If the loop is non-contractible, $\Phi_B \neq 0\!\pmod{2\pi}$.

**(b)** Different eigenstates (dimensions $i$ and $j$) may acquire **different** Berry phases: $\Phi_B^{(i)} \neq \Phi_B^{(j)}$.

**(c)** This creates an irreducible phase shift: $\theta_{ij}$ acquires an addition $\Phi_B^{(i)} - \Phi_B^{(j)}$, which cannot be eliminated by any continuous deformation of $H_{\mathrm{eff}}$. $\blacksquare$

**Interpretation [I].** A topologically protected Gap means that the external and the internal **cannot** fully coincide as long as the contextual space preserves its topology.

### 2.1 Holonomy in the Space of Gap Configurations

The Berry phase $\Phi_B$ is the **holonomy** of the Berry connection in the space of Gap configurations. Under adiabatic variation of the context parameters $\lambda(\tau)$ along a closed loop $\gamma$, the system returns to the same eigenstate but acquires a phase factor $e^{i\Phi_B}$.

:::info Note
The key difference from standard quantum systems: here the "parameters" are not external fields but **contextual configurations** (states of the environment that determine $H_{\mathrm{eff}}$). The holonomy in the space of contexts determines which Gap configurations are topologically protected and which are not.
:::

For a system with 7 dimensions, the space of Gap configurations is parametrised by 21 phases $\theta_{ij}$ ($i < j$). The associative 3-form $\varphi$ induces the **Berry curvature** $\mathcal{F} = d\mathcal{A}$ on this space, and the holonomy around a loop $\gamma$:

$$
\Phi_B[\gamma] = \oint_\gamma \mathcal{A} = \iint_\Sigma \mathcal{F}
$$

is a topological invariant (depends only on the homotopy class $[\gamma] \in \pi_1(M)$).

---

## 3. Connection to Octonionic Structure

The group $G_2 = \mathrm{Aut}(\mathbb{O})$ acts on the space $\mathrm{Im}(\mathbb{O}) \cong \mathbb{R}^7$. If the context space $M \subset G_2/H$ (for some subgroup $H$), then:

$$
\pi_1(G_2/H) \neq 0 \quad \Rightarrow \quad \exists\;\text{topologically protected phases}
$$

Since $G_2$ is a connected compact group with $\pi_1(G_2) = 0$, but $G_2/H$ may have a non-trivial fundamental group for a suitable $H$.

### 3.1 Classification of Stabilisers

:::tip Theorem 3.1 (Stabilisers of Gap Configurations) [T]
The stabiliser $H_{\hat{\mathcal{G}}}$ depends on the rank of the opacity operator $\hat{\mathcal{G}} = \mathrm{Im}(\Gamma) \in \mathfrak{so}(7)$:

| Rank | Spectrum of $\hat{\mathcal{G}}$ | Stabiliser $H$ | $\dim(H)$ | $G_2/H$ | $\pi_1(G_2/H)$ |
|------|-----------|---------------|--------|-------|-----------|
| 0 | $(0,0,0)$ | $G_2$ | 14 | $\{\mathrm{pt}\}$ | 0 |
| 1 | $(\lambda,0,0)$ | $SU(3)$ | 8 | $G_2/SU(3) \cong S^6$ | 0 |
| 2 | $(\lambda_1,\lambda_2,0)$ | $SU(2) \times U(1)$ | 4 | 10-dim. | 0 |
| 3 (generic) | $(\lambda_1,\lambda_2,\lambda_3)$ | $T^2$ (torus) | 2 | 12-dim. | $\mathbb{Z}^2$ |
| 3 (degenerate) | $(\lambda,\lambda,\lambda)$ | $SU(2)$ | 3 | 11-dim. | 0 |
:::

### 3.2 Topological Protection from $\pi_1$

:::tip Theorem 3.2 [T]
Gap configurations of rank 3 with generic spectrum are **topologically protected**:

**(a)** $\pi_1(G_2/T^2) \cong \mathbb{Z}^2 \neq 0$ — there exist non-degenerate Gap configurations that cannot be contracted to trivial ones.

**(b)** The configuration class $[\hat{\mathcal{G}}] \in \pi_1(G_2/T^2)$ is determined by two integers $(n_1, n_2)$ corresponding to the simple roots of $\mathfrak{g}_2$:
- $\alpha_1$ (short root): $n_1 \in \mathbb{Z}$
- $\alpha_2$ (long root): $n_2 \in \mathbb{Z}$

**(c)** The "untying" energy (transition $(n_1,n_2) \to (0,0)$):

$$
\Delta E_{\mathrm{top}} \geq (|n_1| + |n_2|) \cdot \pi\mu^2 / \lambda_4
$$

**(d)** For ranks 0, 1, 2: $\pi_1 = 0$, topological protection is **absent**.
:::

:::info Interpretation of Winding Numbers
The pair $(n_1, n_2) \in \mathbb{Z}^2$ defines the **topological protection class** of a Gap configuration. The winding numbers $(n_1, n_2)$ correspond to two independent cycles in the maximal torus $T^2 \subset G_2$, which are images of the simple roots $\alpha_1, \alpha_2$ of the root system $\mathfrak{g}_2$.

Transition between sectors $(n_1, n_2)$ and $(n_1', n_2')$ requires surmounting the energy barrier $\Delta E_{\mathrm{top}} \geq (|n_1 - n_1'| + |n_2 - n_2'|) \cdot \pi\mu^2/\lambda_4$, which ensures **stability** of a non-degenerate Gap against small perturbations. Only a **global** phase transition (change of the rank of the spectrum of $\hat{\mathcal{G}}$) can remove the topological protection.
:::

---

## 4. Five Types of Gap Protection

**Five independent** mechanisms of Gap irreducibility have been established:

| # | Protection type | Mechanism |
|---|-----------|----------|
| 1 | Code-theoretic | Hamming bound $H(7,4)$: $\geq 3$ non-zero Gaps |
| 2 | Algebraic | Octonionic associator $[e_i,e_j,e_k] \neq 0$ |
| 3 | Energetic | Spontaneous minimum $V_{\mathrm{Gap}} \neq 0$ from $V_3$ |
| 4 | Categorical | Lawvere's theorem: the fixed point cannot be trivial |
| 5 | **Topological** | $\pi_1(G_2/T^2) \cong \mathbb{Z}^2$: non-degenerate Gap is non-contractible |

Five **independent** arguments (code-theoretic, algebraic, variational, categorical, topological) establish the irreducibility of the Gap as a **fundamental** fact of a 7-dimensional octonionic system.

---

## 5. Sectoral Gap Bound {#секторная-gap-граница}

### 5.1 Retraction of the Original Fano Bound [✗]

:::danger Retraction: Theorem 6.1 (Fano Bound $\leq 1/2$) [✗]
The original formulation claimed: $\mathrm{Gap}_{\mathrm{intra}}(i,j) \leq 1/2$ for all pairs $(i,j)$ on the same line of the Fano plane.

**Counterexample:** In $\mathrm{PG}(2,2)$ **every** pair lies on exactly one Fano line (any two points of the projective plane determine a line). The lines containing O: $\{A, O, U\}$, $\{S, L, O\}$, $\{D, E, O\}$. For the pairs $(A,O)$, $(S,O)$, $(D,O)$, $(E,O)$, $(L,O)$, $(U,O)$ on these lines, $\mathrm{Gap}(O,i) \approx 1$ (from the Page–Wootters mechanism: the O-sector serves as an internal clock with maximal phase). This is a **direct counterexample** to the original formulation $\leq 1/2$.

Replacing theorem: [Sectoral Gap Bound](#теорема-секторная-gap-граница) [T].
:::

### 5.2 Theorem (Sectoral Gap Bound) [T] {#теорема-секторная-gap-граница}

:::tip Theorem (Sectoral Gap Bound) [T]
In the unique vacuum ([T-64](/docs/core/dynamics/gap-thermodynamics#теорема-глобальная-минимизация) [T]) the Gap configuration $\theta^*$ satisfies:

**(a)** For all non-O pairs ($i,j \in \{A,S,D,L,E,U\}$):
$$\mathrm{Gap}(i,j) \leq \bar{\varepsilon} \approx 0.023 \ll 1/2$$

**(b)** For O-sectoral pairs ($i \in \{A,S,D,L,E,U\}$):
$$\mathrm{Gap}(O,i) = 1 - O(\bar{\varepsilon}^2) \approx 1$$

**(c)** The total Gap is dominated by the O-sector:
$$\mathcal{G}_{\text{total}} = \mathcal{G}_O + O(\bar{\varepsilon}^2), \quad \mathcal{G}_O := 2\sum_{i \neq O} |\gamma_{Oi}|^2 \cdot \mathrm{Gap}(O,i)^2$$
:::

**Proof.**

**Step 1 (Vacuum sectoral hierarchy).** The unique global minimum of $V_{\text{Gap}}$ ([T-64](/docs/core/dynamics/gap-thermodynamics#теорема-глобальная-минимизация) [T]) defines the sectoral parametrisation $\boldsymbol{\varepsilon} = (\varepsilon_{O3}, \varepsilon_{O\bar{3}}, \varepsilon_{33}, \varepsilon_{\bar{3}\bar{3}}, \varepsilon_{3\bar{3}})$. From the positive definiteness of the Hessian (T-64):

| Sector | Pairs | $\varepsilon$ | Gap |
|--------|------|--------------|-----|
| O-to-all | 6 pairs | $\varepsilon_O \approx 1$ | $\approx 1$ |
| $\mathbf{3}$-$\mathbf{3}$ | 3 pairs | $\varepsilon_{33} \approx 0.06$ | $\approx 0.06$ |
| $\bar{\mathbf{3}}$-$\bar{\mathbf{3}}$ | 3 pairs | $\varepsilon_{\bar{3}\bar{3}} \approx 10^{-17}$ | $\approx 10^{-17}$ |
| $\mathbf{3}$-$\bar{\mathbf{3}}$ | 9 pairs | $\varepsilon_{3\bar{3}} \approx 0$ | $\approx 0$ |

**Step 2 (Upper bound for non-O pairs).** The potential $V_2 = \mu^2 \mathcal{G}_{\text{total}}$ quadratically suppresses large phases. The competing $V_3$ (cubic) and $V_4$ (quartic) terms generate a non-zero minimum, but:

$$\mathrm{Gap}(i,j) \leq \varepsilon_{\max} = \varepsilon_{33} \approx 0.06 \ll \frac{1}{2}$$

The mean coherence $\bar{\varepsilon} = \frac{1}{15}\sum_{i<j, \, i,j \neq O} \varepsilon_{ij} \approx 0.023$, and the maximum $\varepsilon_{\max} = \varepsilon_{33} \approx 0.06 \ll 1/2$.

**Step 3 (O-sector — necessity of Gap $\approx$ 1).** The Page–Wootters mechanism (A5) requires the O-subsystem to serve as a clock. The rate of time flow (from the [spectral triple](/docs/core/foundations/spacetime#теорема-спектральная-тройка) T-53 [T]):

$$\frac{d\tau}{d\sigma} = \omega_0 \cdot \sqrt{\sum_{i \neq O} |\gamma_{Oi}|^2 \cdot \mathrm{Gap}(O,i)^2}$$

For $d\tau/d\sigma > 0$ it is necessary that $\mathrm{Gap}(O,i) > 0$ for at least one $i$. Minimising $V_{\text{Gap}}$ subject to PW-viability gives $\mathrm{Gap}(O,i) \approx 1$ — the maximum value, providing the most accurate "clock". $\blacksquare$

### 5.3 Map of Fano Triplets

| # | Triplet | Dimensions | Interpretation |
|---|---------|-----------|---------------|
| 1 | $(e_1, e_2, e_3)$ | $A, S, D$ | Material block |
| 2 | $(e_1, e_4, e_5)$ | $A, L, E$ | Cognitive block |
| 3 | $(e_1, e_6, e_7)$ | $A, O, U$ | Transcendent block |
| 4 | $(e_2, e_4, e_6)$ | $S, L, O$ | Structural-logical block |
| 5 | $(e_2, e_5, e_7)$ | $S, E, U$ | Somatic-integrative block |
| 6 | $(e_3, e_4, e_7)$ | $D, L, U$ | Active-holistic block |
| 7 | $(e_3, e_5, e_6)$ | $D, E, O$ | Dynamic-foundational block |

### 5.4 Updated Falsifiable Prediction

The mean Gap for non-O coherences is strictly lower than for O-sectoral coherences:

$$\langle\mathrm{Gap}_{\text{non-O}}\rangle \ll \langle\mathrm{Gap}_O\rangle \approx 1$$

Specifically: $\langle\mathrm{Gap}_{\text{non-O}}\rangle \leq \bar{\varepsilon} \approx 0.023$, i.e. non-O pairs are nearly transparent while O-pairs are maximally opaque.

---

## 6. Spontaneous Breaking and Goldstone Modes

### 6.1 Broken Symmetries under Spontaneous Gap

:::tip Theorem 4.1 [T]
The stationary state $\Gamma^*$ with a non-zero Gap profile breaks $G_2$-symmetry:

$$
G_2 \to H_{\hat{\mathcal{G}}_*}, \quad n_{\mathrm{broken}} = 14 - \dim(H)
$$

| Rank of $\hat{\mathcal{G}}_*$ | $H$ | $\dim(H)$ | $n_{\mathrm{broken}}$ | Goldstone modes |
|----------|---|--------|----------|---------------------|
| 1 | $SU(3)$ | 8 | 6 | 6 |
| 2 | $SU(2) \times U(1)$ | 4 | 10 | 10 |
| 3 (generic) | $T^2$ | 2 | 12 | 12 |
| 3 (degenerate) | $SU(2)$ | 3 | 11 | 11 |
:::

### 6.2 Modification for Dissipative Systems

:::tip Theorem 4.2 [T]
In an open (dissipative) system the Goldstone modes are **quasi-massive**:

$$
m_{\mathrm{Gold}}^2 = \Gamma_2 \cdot \kappa_0 / |\gamma|^2
$$

$$
\tau_{\mathrm{Gold}} = \frac{1}{\Gamma_2} \cdot \frac{|\gamma|^2}{\kappa_0}
$$

- When $\Gamma_2 \to 0$ (isolated system): $m_{\mathrm{Gold}} \to 0$ — standard Goldstone regime.
- When $\Gamma_2 \to \infty$ (strong dissipation): $m_{\mathrm{Gold}} \to \infty$ — modes are frozen.
:::

### 6.3 Excitation Spectrum

:::tip Theorem 5.1 [T]
The spectrum of small oscillations near the minimum of $V_{\mathrm{Gap}}$ splits into three sectors:

**(a)** **Massive modes** ($n_{\mathrm{massive}}$ in total): directions perpendicular to the $G_2$-orbit, $\omega_{\mathrm{massive}}^2 = \mu_{\mathrm{eff}}^2 + \kappa/m$.

**(b)** **Quasi-Goldstone modes** ($n_{\mathrm{broken}}$ in total): broken generators of $G_2$, $\omega_{\mathrm{Gold}}^2 = \kappa/m - \Gamma_2^2/(4m^2)$.

**(c)** **Topologically protected mode** (0 or 1): when $Q_{\mathrm{top}} \neq 0$ — cannot decay without a phase transition.

**(d)** Total count: $n_{\mathrm{massive}} + n_{\mathrm{broken}} + n_{\mathrm{top}} = 21$.
:::

### 6.4 Physical Interpretation: ISF

The quasi-Goldstone modes are **slow collective oscillations** of the Gap profile along the $G_2$-orbit, redistributing the Gap among pairs while conserving $\mathcal{G}_{\mathrm{total}}$:

$$
\delta\mathrm{Gap}(i,j) = \sum_a \epsilon_a \cdot [T_a, \hat{\mathcal{G}}_*]_{ij}
$$

Frequency of Goldstone modes for a neural system [C]:

$$
f_{\mathrm{Gold}} \approx \frac{1}{2\pi}\sqrt{\frac{\kappa}{m}} \sim 0.005\text{--}0.02\;\text{Hz}
$$

This matches in order of magnitude the **infra-slow neuronal fluctuations** (ISF) observed in fMRI (0.01–0.1 Hz).

:::warning Parameter Fitting
The values of $\kappa$ and $m$ are not derived from microscopic theory but are chosen so that $f_{\mathrm{Gold}}$ falls within the ISF range. The coincidence with observed frequencies of 0.01–0.1 Hz is a consequence of fitting, not a prediction.
:::

:::info Falsifiable Prediction (ISF)
The number of independent ISF components depends on the opacity rank:

| Rank | $n_{\mathrm{Gold}}$ | ISF prediction |
|------|--------|---------------------|
| 1 | 6 | 6 independent ISF components |
| 2 | 10 | 10 ISF components |
| 3 | 12 | 12 ISF components |

Typical number of ICA components in resting-state fMRI: $\sim 10$–$20$, consistent with rank 2–3.
:::

---

## 7. Gap Phase Diagram

### 7.1 Control Parameters

Two dimensionless parameters:
- **Dimensionless temperature:** $t := T_{\mathrm{eff}}/T_c = (\Gamma_2/\kappa_0) \cdot (k_B T_{\mathrm{phys}} \ln 21) / \mu^2$
- **Viability:** $r := \kappa / \Gamma_2$

### 7.2 Three Phases

:::tip Theorem 6.1 (Phase Diagram) [T]
**(a) Phase I: Ordered Gap** ($t < 1$, $r > r_c$). Several channels with high Gap, the rest transparent. $G_2 \to H$ spontaneously broken. Goldstone modes exist.

**(b) Phase II: Disordered Gap** ($t > 1$, $r > r_c$). Gap is uniform: $\mathrm{Gap}(i,j) \approx \mathrm{const}$. $G_2$ approximately conserved.

**(c) Phase III: Dead Zone** ($r < r_c$). Coherences decay: $|\gamma_{ij}| \to 0$.

**(d)** I↔II: **second-order** (continuous), $\beta = 1/2$.
**(e)** I↔III: **first-order** (discontinuous).
**(f)** Tricritical point: $(t^*, r^*) = (1, r_c)$, exponents $\beta = 1/4$, $\gamma = 1$, $\delta = 5$.
:::

```
    t (T_eff/T_c)
    │
  2 ┤         Phase II: Disordered Gap
    │        (uniform, recoverable)
    │
  1 ┤─ ─ ─ ─ ─ ─ ─ ─ ╋ ─ ─ ─ ─ ─ ─ ─ ─ ─
    │               ╱ (t*,r*)
    │   Phase I   ╱   ← 2nd-order (continuous)
    │  Ordered   ╱
    │   Gap     ╱
    │          ╱
  0 ┤─────────╱─────────────────────────────
    │ Ph. III│
    │  Dead  │
    └────────┼────────┼─────────────────── r (κ/Γ₂)
             r_c      1
```

### 7.3 Clinical Correspondence

| Phase | Clinical correspondence | Characteristic |
|------|--------------------------|----------------|
| I (ordered) | Normal functioning | Specific opacities, transparency in other channels |
| II (disordered) | Diffuse dissociative state | All channels equally opaque |
| III (dead) | Dementia, coma | Loss of coherences, breakdown of bonds |
| I↔II transition | Psychotic episode | Sudden "melting" of structured opacity |
| I↔III transition | Acute decompensation | Abrupt breakdown upon resource exhaustion |
| Tricritical | Borderline state | Oscillation between ordered and chaotic Gap |

---

## 8. Critical Phenomena

:::tip Theorem 7.1 (Critical Exponents) [T]
Near $t = 1$ (I↔II transition):

| Exponent | Value | Physical meaning |
|-----------|---------|------------------|
| $\beta = 1/2$ | $\sigma_{\mathrm{Gap}}^2 \propto (1-t)^{2\beta}$ | Gap anisotropy |
| $\gamma = 1$ | $\chi \propto \lvert 1-t\rvert^{-\gamma}$ | Susceptibility |
| $\nu = 1/2$ | $\xi \propto \lvert 1-t\rvert^{-\nu}$ | Correlation length |
| $\alpha = 0$ | Logarithmic divergence | Heat capacity |

Scaling relations are satisfied:
- Rushbrooke's law: $\alpha + 2\beta + \gamma = 0 + 1 + 1 = 2$ ✓
- Josephson's law: $d\nu = 2 - \alpha = 2 \Rightarrow d_{\mathrm{eff}} = 4$
:::

:::tip Theorem 7.2 [T]
Mean-field exponents are **exact** in UHM by three independent mechanisms (see [Exactness mechanism](/docs/consciousness/hierarchy/swallowtail-transitions#механизм-точности) for the full argument): (i) Thom-Arnold topological rigidity of the $A_2$ cusp catastrophe ensures critical exponents are topological invariants of the catastrophe class; (ii) UHM dynamics is deterministic (Lindblad + regeneration), not thermodynamically stochastic, so the Landau potential is the *effective potential of the deterministic flow* and its saddle-points are the actual attractors — no Ginzburg fluctuation correction is applicable; (iii) order-parameter dimension $d_{\mathrm{eff}} = \binom{7}{2} = 21$ gives a quantitative $1/N$ cross-check with fluctuation corrections of $\approx 5\%$, within the experimental PCI resolution.
:::

---

## 9. Refutation of the CS Derivation {#9-опровержение-cs-вывода}

### 9.1 Refutation of the CS Derivation of the Topological Term

:::danger Theorem 2.1 (CS on 1D — Total Derivative) [T]
The Chern-Simons functional for a $\mathfrak{g}_2$-connection on a 1D base is a **total derivative** and does not generate a topological phase:

$$
CS_1[\mathcal{A}] = \frac{\kappa}{2}\sum_a A_a \dot{A}_a = \frac{d}{d\tau}\!\left(\frac{\kappa}{4}\sum_a A_a^2\right)
$$
:::

**Proof.**

**(a)** In the 1D case, the triple wedge $\mathcal{A} \wedge \mathcal{A} \wedge \mathcal{A}$ **vanishes identically** (all 1-forms are proportional to $d\tau$, and $d\tau \wedge d\tau = 0$). Only the quadratic part remains:

$$
CS_1[\mathcal{A}] = \frac{1}{2}\mathrm{Tr}(\mathcal{A}\,\dot{\mathcal{A}})
$$

**(b)** The $\mathfrak{g}_2$-connection is expanded in orthonormal generators $T_a$ ($a = 1,\ldots,14$):

$$
\mathcal{A} = \sum_a A_a\,T_a, \quad \mathrm{Tr}(T_a\,T_b) = \kappa\,\delta_{ab}
$$

**(c)** Substituting:

$$
CS_1 = \frac{\kappa}{2}\sum_a A_a\,\dot{A}_a = \frac{d}{d\tau}\!\left(\frac{\kappa}{4}\sum_a A_a^2\right)
$$

This is a **total derivative** with respect to $\tau$. Upon integration over a closed loop (compactification of $\tau$ on $S^1$) the contribution is a boundary term — **zero** for periodic fields $A_a(\tau + T) = A_a(\tau)$. $\blacksquare$

:::warning Corollary [T]
$CS_1$ on a 1D base **does not generate** a topological phase for winding sectors. The identification "$CS_1 = \sum_{\mathrm{Fano}} \theta_{ij}\dot{\theta}_{jk}$" does not follow from $\mathrm{Tr}(\mathcal{A}\dot{\mathcal{A}})$, since the latter is a total derivative.
:::

### 9.2 Topological Term from Im($S_{\text{Keldysh}}$) [T] {#теорема-l-top-кельдыш}

:::tip Theorem (Topological Lagrangian from Im($S_{\text{Keldysh}}$)) [T]
The topological contribution to the action of Gap theory is uniquely determined by the imaginary part of the Keldysh action ([T-75](/docs/core/dynamics/gap-thermodynamics#полный-лагранжиан) [T]):

$$\mathcal{L}_{\text{top}} = \mathrm{Im}\left(\frac{\partial S_{\text{Keldysh}}}{\partial \tau}\right)\bigg|_{\text{cyclic}} = \frac{\lambda_3}{2\pi} \cdot \varphi_{ijk} \, \theta^{ij} \dot{\theta}^{jk}$$

where $\varphi_{ijk}$ is the gauge 3-form of $G_2$.
:::

**Proof.**

**Step 1 (Keldysh action — complex structure).** From the [derivation of the Lagrangian from the Lindbladian](/docs/core/dynamics/gap-thermodynamics#полный-лагранжиан) [T]:

$$S_K[\rho_+, \rho_-] = \mathrm{Re}\,\mathrm{Tr}[\rho_+ \ln\rho_- - \mathcal{L}_\Omega[\rho_+]\ln\rho_-]$$

The full Keldysh action $S_K = S_{\text{Re}} + i S_{\text{Im}}$ also contains an imaginary part:

$$S_{\text{Im}} = \mathrm{Im}\,\mathrm{Tr}[\rho_+ \ln\rho_- - \mathcal{L}_\Omega[\rho_+]\ln\rho_-]$$

**Step 2 (Imaginary part = geometric phase).** Under cyclic evolution ($\rho(\tau + T) = \rho(\tau)$):

$$S_{\text{Im}}[C] = \oint_C \mathrm{Im}(\mathcal{A}) = \oint_C \sum_{ij} A_{ij}^{\text{Berry}} \, d\theta_{ij}$$

This is the **Berry phase** in the space of Gap configurations $(S^1)^{21}$.

**Step 3 (Berry connection from $V_3$).** The imaginary part of the logarithm $\ln\rho$ for a density matrix with coherences $\gamma_{ij} = |\gamma_{ij}|e^{i\theta_{ij}}$:

$$\mathrm{Im}(\mathrm{Tr}[\rho_+ \ln\rho_-]) = \sum_{ij} |\gamma_{ij}|^2 \cdot \theta_{ij} + O(\theta^3)$$

Contribution of the $\mathcal{L}_\Omega$-term via $V_3$:

$$\mathrm{Im}(\mathrm{Tr}[\mathcal{L}_\Omega[\rho_+]\ln\rho_-]) \supset \lambda_3 \sum_{(i,j,k) \notin \text{Fano}} |\gamma_{ij}||\gamma_{jk}||\gamma_{ik}| \cdot \cos(\theta_{ij}+\theta_{jk}-\theta_{ik}) \cdot (\dot{\theta}_{ij}+\dot{\theta}_{jk}-\dot{\theta}_{ik})$$

**Step 4 ($G_2$-covariant contraction).** The gauge 3-form of $G_2$:

$$\varphi = \sum_{(i,j,k) \in \text{Fano}} e^i \wedge e^j \wedge e^k$$

Using Fano/non-Fano duality ($\varphi_{ijk} = \varepsilon^{\text{Fano}}_{ijk}$), the imaginary part of $S_K$ in the linear approximation reduces to:

$$S_{\text{Im}} = \int d\tau \, \frac{\lambda_3}{2\pi} \cdot \varphi_{ijk} \, \theta^{ij} \dot{\theta}^{jk}$$

**Step 5 (Uniqueness of the form).** From [Theorem 4.1](#единственность-билинейной-формы-bb) [T]: the cyclic $S_3$-invariant bilinear form $B^{(b)}(\mathbf{n})$ on winding numbers is **unique** (up to a scalar) and $G_2$-covariant. Variant (b) is the only non-degenerate one. Consequently, $\mathcal{L}_{\text{top}} = \beta \cdot \varphi_{ijk} \theta^{ij} \dot{\theta}^{jk}$ with $\beta = \lambda_3/(2\pi)$ is the **unique** $G_2$-covariant topological Lagrangian. $\blacksquare$

:::info Key Point: CS Replaced by Keldysh
Chern-Simons gave a total derivative (trivial contribution, [Theorem 2.1](#9-опровержение-cs-вывода) [T]). The Keldysh formalism gives a **non-trivial** geometric phase via the imaginary part of $S_K$. $G_2$-covariance $+$ uniqueness of the bilinear form $=$ a unique $\mathcal{L}_{\text{top}}$. The coefficient $\beta = \lambda_3/(2\pi)$ is determined from first principles.
:::

Physically: $\varphi$ defines a "magnetic field" in the phase space of the Gap, and $\mathcal{L}_{\mathrm{top}}$ is the analogue of $A \cdot \dot{x}$ for a charged particle.

---

## 10. $G_2$-Orientational Symmetry

### 10.1 Three Summation Variants

When computing the winding phase $\Phi(\mathbf{n})$ from the topological term, the question arises as to the range of summation:

| Variant | Terms | Rank | $G_2$-covariance |
|---------|-----------|------|---------------------|
| (a) Full antisymmetrisation | 42 | **0** (identically zero) | Yes |
| (b) Cyclic sum | 21 | **21** (non-degenerate) | **Yes** |
| (c) Monomial ($i<j<k$) | 7 | 14 (degenerate) | No |

### 10.2 Full Antisymmetrisation Yields Zero

:::tip Theorem 3.1 [T]
Full antisymmetrisation (variant (a), all 6 permutations per line) gives an identically zero quadratic winding phase:

$$
B^{(a)}(\mathbf{n}) = \frac{1}{6}\sum_{i,j,k=1}^{7} \varepsilon_{ijk}\,n_{ij}\,n_{jk} \equiv 0
$$

for all $\mathbf{n}$ with symmetric $n_{ij} = n_{ji}$.
:::

**Proof.** For each Fano line $\{a,b,c\}$ with $\varepsilon_l = \varepsilon_{abc}$, expanding the 6 permutations (using $n_{ij} = n_{ji}$):

| Permutation | $\varepsilon$ | Product $n \cdot n$ |
|-------------|---|----------|
| $(a,b,c)$ | $+\varepsilon_l$ | $n_{ab}n_{bc}$ |
| $(b,c,a)$ | $+\varepsilon_l$ | $n_{bc}n_{ac}$ |
| $(c,a,b)$ | $+\varepsilon_l$ | $n_{ac}n_{ab}$ |
| $(a,c,b)$ | $-\varepsilon_l$ | $n_{ac}n_{bc}$ |
| $(c,b,a)$ | $-\varepsilon_l$ | $n_{bc}n_{ab}$ |
| $(b,a,c)$ | $-\varepsilon_l$ | $n_{ab}n_{ac}$ |

Sum: $+\varepsilon_l(n_{ab}n_{bc} + n_{bc}n_{ac} + n_{ac}n_{ab}) - \varepsilon_l(n_{ac}n_{bc} + n_{bc}n_{ab} + n_{ab}n_{ac}) = 0$. $\blacksquare$

### 10.3 Cyclic Formula

:::tip Theorem 3.2 [T]
The oriented cyclic sum gives a **non-zero non-degenerate** quadratic form:

$$
B^{(b)}(\mathbf{n}) = \sum_{l=1}^{7} \varepsilon_l \left(n_{ab}n_{bc} + n_{bc}n_{ca} + n_{ca}n_{ab}\right)
$$

with matrix $\tilde{M} = \bigoplus_{l=1}^{7} \varepsilon_l(J_3 - I_3)$, rank $= 21$.
:::

Each block $(J_3 - I_3)$ has eigenvalues $2$ (multiplicity 1), $-1$ (multiplicity 2) — non-degenerate.

### 10.4 Monomial Formula — Degenerate

:::tip Theorem 3.3 [T]
The canonical monomial formula (variant (c), only $i<j<k$) gives a **degenerate** quadratic form:

$$
B^{(c)}(\mathbf{n}) = \sum_{l:\,a<b<c} \varepsilon_{abc}\,n_{ab}\,n_{bc}
$$

with rank 14 and $\dim\ker = 7$.
:::

**Proof.** For each line $\{a,b,c\}$ ($a<b<c$): the single term $n_{ab}n_{bc}$ connects edges $(a,b)$ and $(b,c)$ through the middle vertex $b$. The edge $(a,c)$ **does not participate** — it is "orphaned".

The symmetrised matrix for block $l$ in the basis $(n_{ab}, n_{ac}, n_{bc})$:

$$
\tilde{M}_l^{(c)} = \frac{\varepsilon_l}{2}\begin{pmatrix} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 0 \end{pmatrix}
$$

Eigenvalues: $\pm\varepsilon_l/2$ (multiplicity 1 each), $0$ (multiplicity 1). Block rank = 2. Full rank: $2 \times 7 = 14$. Kernel: 7 orphaned edges. $\blacksquare$

### 10.5 Violation of $G_2$-Covariance by the Monomial Formula

The canonical ordering $i<j<k$ singles out the middle vertex $b$, breaking the **cyclic** $\mathbb{Z}_3$-symmetry of the Fano line. The stabiliser of the line in $\mathrm{PSL}(2,7) \cong \mathrm{Aut}(\mathrm{Fano})$ contains $\mathbb{Z}_3$:

$$
(a,b,c) \to (b,c,a) \to (c,a,b)
$$

The monomial formula is **not invariant** under $\mathbb{Z}_3$ — this is a coordinate artefact, not a physical structure.

---

## 11. Uniqueness of the Bilinear Form $B^{(b)}$

#### Theorem 4.1 (Uniqueness of the Bilinear Form) {#единственность-билинейной-формы-bb}

:::tip Theorem 4.1 (Uniqueness of the Bilinear Form $B^{(b)}$) [T]
The oriented cyclic sum is the **unique** non-zero $G_2$-covariant quadratic form on winding numbers defined by the Fano structure.

**Status:** **[T]**. The topological Lagrangian is derived from the imaginary part of the Keldysh action ([Theorem L_top from Keldysh](#теорема-l-top-кельдыш) [T]), and the uniqueness of the form follows from the $S_3$-argument below $+$ the uniqueness of $\mathrm{Im}(S_K)$.
:::

**Proof (alternative, via $S_3$-argument).**

**(a)** The stabiliser of a Fano line in $\mathrm{PSL}(2,7)$ contains the full $S_3$, acting on the 3 points of the line. $S_3$-invariance requires:
- All 3 cyclic permutations — common coefficient $\alpha$
- All 3 anti-cyclic permutations — common coefficient $\beta$

**(b)** Using $n_{ij} = n_{ji}$: anti-cyclic terms $=$ minus cyclic ones.

**(c)** Full form on the line:

$$
Q_l = (\alpha - \beta)\varepsilon_l(n_{ab}n_{bc} + n_{bc}n_{ca} + n_{ca}n_{ab}) = c \cdot B^{(b)}_l
$$

The non-zero form is unique up to scale. $\blacksquare$

The proof **does not use** representation theory of $G_2$, but is based on:
1. $G_2$-transitivity on Fano lines
2. $S_3$-invariance of the line stabiliser
3. The identity $n_{ij} = n_{ji}$

### 11.1 Recovery of 9 Orders

With the three-term formula ($B^{(b)}$, rank 21) the Gaussian sum gives:

$$
|G_7| = 7^{21/2}, \quad \frac{|G_7|}{7^{21}} = 7^{-21/2} \approx 10^{-8.87}
$$

| Aspect | Monomial (c) | Cyclic (b) |
|--------|-----------------|-----------------|
| Rank | 14 | **21** |
| Suppression | $10^{-5.9}$ | **$10^{-8.9}$** |
| $G_2$-covariance | No | **Yes** |

:::info Caveat
Although the mathematical result of the Gaussian sum is rigorous, at physical $S_0 = 20$ destructive interference **does not work** (dominant sectors have zero phase). See the [Cosmological Constant](/docs/physics/gravity/cosmological-constant#7-сумма-гаусса-для-фано-фаз) page for details.
:::

---

## 12. Connection to Other Sections

| Topic | Page | Connection |
|------|----------|-------|
| $G_2$-Structure | [$G_2$-Structure and the Fano Plane](/docs/physics/gauge-symmetry/g2-structure) | Associative 3-form $\varphi$ and Fano triplets |
| Cosmological Constant | [Cosmological Constant](/docs/physics/gravity/cosmological-constant) | Uniqueness of $B^{(b)}$ and Gauss sum |
| Dark Matter | [Dark Matter from Gap](/docs/physics/cosmology-phys/dark-matter) | Topological protection of Gap in the $O$-sector |
| Einstein Equations | [Einstein Equations from Gap](/docs/physics/gravity/einstein-equations) | Gap curvature and emergent geometry |
| Emergent Geometry | [Emergent Geometry](/docs/physics/gravity/emergent-geometry) | Metric from coherences |
| Gap Dynamics | [Gap Dynamics](/docs/core/dynamics/gap-dynamics) | Topological term $\mathcal{L}_{\mathrm{top}}$ in the Gap Lagrangian |
| Fano Selection Rules | [Fano Selection Rules](/docs/physics/gauge-symmetry/fano-selection-rules) | Fano triplets and cyclic orientation |


---

**Related documents:**
- [Gap Semantics: 49 Elements](/docs/physics/dual-aspect/gap-semantics)
- [G₂-Structure and the Fano Plane](/docs/physics/gauge-symmetry/g2-structure)
- [Topological Protection of Coherence](/docs/applied/coherence-cybernetics/topological-protection)
- [Vacuum Uniqueness](/docs/proofs/categorical/uniqueness-theorem)
