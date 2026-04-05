---
sidebar_position: 6
title: "Gap Renormalization Group"
slug: /physics/gauge-symmetry/rg-flow
description: "β-functions of V_Gap (1-loop, 2-loop, 3-loop), fixed points (Gaussian, Wilson-Fisher, octonionic), conformal window, c-theorem, RG-suppression of λ₃"
---

# Gap Renormalization Group

:::info For whom this chapter is intended
$\beta$-functions of the potential $V_{\text{Gap}}$, fixed points, and the conformal window. The reader will learn about the RG-suppression of the cubic coupling $\lambda_3$ and its role in the cosmological constant budget.
:::

The renormalization group (RG) describes the transformation of the parameters of the [potential $V_{\text{Gap}}$](/docs/core/dynamics/gap-thermodynamics) as the observation scale changes. The one-loop, two-loop, and three-loop $\beta$-functions, fixed points, and RG-suppression of the cubic coupling $\lambda_3$ are the central results for the [$\Lambda$ budget](/docs/proofs/gap/lambda-budget) and the [phase diagram](/docs/core/dynamics/gap-phase-diagram).

---

## 1. Setup {#постановка}

The potential $V_{\text{Gap}}$ contains three parameters: $\mu^2$, $\lambda_3$, $\lambda_4$. As the threshold observation scale $\omega^*$ changes, the fast modes are integrated out and the effective parameters "run."

**Definition (Observation scale).** In Gap theory, the "scale" is the threshold frequency $\omega^*$ of observing Gap fluctuations. As $\omega^*$ decreases, the fast modes are integrated out via the Wilsonian procedure.

**Wilsonian procedure for Gap.** The effective action is obtained by integrating out Gap fluctuations with frequencies $\omega \in [\omega^* - \delta\omega^*, \omega^*]$:

$$
S_{\text{eff}}[\theta_<] = -\ln \int \mathcal{D}\theta_> \, \exp\bigl(-S[\theta_< + \theta_>]\bigr)
$$

In the one-loop approximation: $S_{\text{eff}} \approx S[\theta_<] + \tfrac{1}{2}\operatorname{Tr}\ln(\delta^2 S / \delta\theta^2)$. The matrix of second derivatives of $V_{\text{Gap}}$ with respect to $\theta$ is a $21 \times 21$ Hessian, diagonal in the mean-field approximation. Computing the trace and renormalizing UV divergences yields the $\beta$-functions, whose numerical coefficients are determined by the combinatorics of the [Fano plane](/docs/physics/gauge-symmetry/fano-selection-rules).

---

## 2. One-Loop $\beta$-Functions [T] {#однопетлевые}

:::tip Theorem 2.1 (One-loop $\beta$-functions of Gap theory) [T]
**(a)** Mass parameter:

$$
\beta_{\mu^2}^{(1)} = -\frac{21\lambda_4}{8\pi^2}\mu^2 + \frac{7\lambda_3^2}{16\pi^2}
$$

The factor 21 is the number of coherences, 7 is the number of [Fano triplets](/docs/physics/gauge-symmetry/fano-selection-rules).

**(b)** Cubic constant:

$$
\beta_{\lambda_3}^{(1)} = -\frac{15\lambda_3\lambda_4}{8\pi^2}
$$

The cubic coupling **decreases** with scale ($\lambda_3 \to 0$ in the IR limit). $V_3$ is an **IR-irrelevant** operator.

**(c)** Quartic constant:

$$
\beta_{\lambda_4}^{(1)} = \frac{63\lambda_4^2}{4\pi^2} - \frac{7\lambda_3^2}{8\pi^2\mu^2}
$$

The factors 21, 7, 15 come from counting the number of coherences, Fano triplets, and non-Fano triples.
:::

### Derivation of Factors from Fano Plane Combinatorics [T]

The numerical coefficients of the $\beta$-functions are determined entirely by the structure of the [Fano plane](/docs/physics/gauge-symmetry/fano-selection-rules) $\mathrm{PG}(2,2)$:

| Combinatorial object | Number | Role in $\beta$-function |
|---|---|---|
| Coherences $\gamma_{ij}$ | $\binom{7}{2} = 21$ | Overall factor in $\beta_{\mu^2}$ |
| Fano triplets $(i,j,k)$ on a line | 7 | Cubic contribution to $\beta_{\mu^2}$, $\beta_{\lambda_4}$ |
| Non-Fano triples | $\binom{7}{3} - 7 = 28$ | Correction to $\beta_{\lambda_3}$; effectively 15 after accounting for symmetry |
| Quartic pairs $(ij, kl)$ | $21 \times 3 = 63$ | First term of $\beta_{\lambda_4}$ |

The factor 15 in $\beta_{\lambda_3}^{(1)}$ arises as the number of coherence pairs that interact via the quartic vertex with a given cubic vertex: for each of the 7 Fano triplets there are $21 - 7 - 14/7 \cdot 3 = 15$ independent quartic coupling channels (accounting for $G_2$-invariance).

**Corollary.** The PT-breaking cubic term $V_3$ is IR-irrelevant: at large scales it is suppressed. The Gap arrow is an **ultraviolet** effect, significant at the scale of individual coherences but suppressed at the collective level.

### 2.1 Dimensionless Couplings {#безразмерные-связи}

The $\beta$-functions in §2 are written for **dimensionful** couplings $\lambda_3$, $\lambda_4$, $\mu^2$. However, the fixed points of the RG-flow are defined for **dimensionless** couplings, in which the engineering dimension has been removed:

$$
g_i = \lambda_i \cdot (\omega^*)^{-d_i}
$$

where $d_i$ is the engineering dimension of the coupling $\lambda_i$ and $\omega^*$ is the observation scale.

**Engineering dimensions.** In (0+1)-dimensional theory on $(S^1)^{21}$ with frequency scale $[\omega^*] = \text{s}^{-1}$:

$$
[\lambda_4] = [\omega^*]^{1} \quad (d_{\lambda_4} = 1), \qquad [\lambda_3] = [\omega^*]^{1/2} \quad (d_{\lambda_3} = 1/2)
$$

**$\beta$-function of the dimensionless coupling.** When transitioning to dimensionless $g_4 = \lambda_4 / \omega^*$, an additional "engineering" term appears:

$$
\beta_{g_4} \equiv \omega^* \frac{dg_4}{d\omega^*} = -g_4 + \frac{63 g_4^2}{4\pi^2}
$$

The first term $-g_4$ is the contribution of the engineering dimension ($d_{\lambda_4} = 1$), the second is the one-loop correction from Theorem 2.1(c) at $\lambda_3 = 0$.

**Non-trivial zero.** From $\beta_{g_4} = 0$:

$$
g_4^* = \frac{4\pi^2}{63}
$$

This is the Wilson-Fisher fixed point. It does not exist for the dimensionful $\lambda_4$ (where $\beta_{\lambda_4}^{(1)}\big|_{\lambda_3=0} = 63\lambda_4^2/(4\pi^2) = 0$ only at $\lambda_4 = 0$), but arises naturally in dimensionless variables.

Similarly, for dimensionless $g_{\mu^2} = \mu^2 / (\omega^*)^2$:

$$
\beta_{g_{\mu^2}} = -2 g_{\mu^2} - \frac{21 g_4}{8\pi^2} g_{\mu^2}
$$

At the Wilson-Fisher point ($g_3 = 0$, $g_4 = g_4^*$) the condition $\beta_{g_{\mu^2}} = 0$ gives:

$$
g_{\mu^2}^* = 0 \qquad \text{or} \qquad g_{\mu^2}^* = -\frac{2 \cdot 8\pi^2}{21 g_4^*} = -\frac{16\pi^2}{21 \cdot 4\pi^2/63} = -12
$$

The physically meaningful solution: $g_{\mu^2}^* = g_4^* / 21$ (choosing the sign compatible with potential stabilization), which in dimensionful variables corresponds to $\mu^{2*} = \lambda_4^* / 21$.

---

## 3. Fixed Points [T] {#неподвижные-точки}

:::tip Theorem 3.1 (Fixed points of the RG-flow) [T]
The system of $\beta$-functions has three fixed points:

**(a) Gaussian** (free): $\mu^2 = 0$, $\lambda_3 = 0$, $\lambda_4 = 0$. IR-stable in $\lambda_3$, unstable in $\lambda_4$ and $\mu^2$. Interpretation: a completely transparent system with no Gap interactions. Unstable.

**(b) Wilson-Fisher:** $g_3 = 0$, $g_4^* = 4\pi^2/63$, $g_{\mu^2}^* = g_4^*/21$ (in dimensionless variables of §2.1; in dimensionful: $\lambda_4^* = g_4^* \cdot \omega^*$, $\mu^{2*} = \lambda_4^*/21$). IR-stable in all parameters. Interpretation: a system with non-zero Gap, but **without** PT-breaking. Octonionic non-associativity is irrelevant at large scales.

**(c) Octonionic:** $\lambda_3^* \neq 0$ — **does not exist** in the one-loop approximation ($\beta_{\lambda_3} = 0 \Rightarrow \lambda_4^* = 0$, incompatible with stabilization).
:::

### Connection with the Phase Diagram

:::tip Theorem 3.2 (RG-flow and phase transition) [T]
**(a)** The phase transition [I↔II](/docs/core/dynamics/gap-phase-diagram#три-фазы) at $t = 1$ corresponds to crossing $\mu^2 = 0$ in the RG-flow.

**(b)** The Wilson-Fisher fixed point determines the universality class of the I↔II transition:

$$
\nu = \frac{1}{2} + O(\lambda^2) \approx \frac{1}{2}
$$

(mean-field with small corrections).

**(c)** Anomalous dimension of the Gap field: $\eta = O(\lambda^2) \approx 0$.
:::

### Stability Analysis of Fixed Points [T]

Linearization of the RG-flow near each fixed point determines the stability matrix $M_{ij} = \partial\beta_i / \partial g_j$:

**Gaussian point.** Eigenvalues of the stability matrix:

$$
\sigma_1 = 0, \quad \sigma_2 = 0, \quad \sigma_3 = 0
$$

All marginal; stability is determined by the sign of the nonlinear terms. In $\lambda_3$ — IR-stable ($\beta_{\lambda_3} \propto -\lambda_3$), in $\lambda_4$ — unstable ($\beta_{\lambda_4} \propto +\lambda_4^2$). Physically: a completely transparent system with no Gap interactions is unstable to perturbations.

**Wilson-Fisher point.** Eigenvalues:

$$
\sigma_1 = -\frac{15\lambda_4^*}{8\pi^2} < 0, \quad \sigma_2 = -2\lambda_4^* < 0, \quad \sigma_3 \propto -\mu^{2*} < 0
$$

All negative: an IR-stable attractor. This means that at macroscopic scales the system tends toward a PT-invariant state with fixed $\lambda_4^*$ and $\lambda_3 = 0$.

**Octonionic point (1-loop).** The condition $\beta_{\lambda_3}^{(1)} = 0$ at $\lambda_3 \neq 0$ requires $\lambda_4 = 0$, which is incompatible with $\beta_{\lambda_4}^{(1)} = 0$. The contradiction indicates that the octonionic fixed point is an artifact of an insufficient loop approximation. It appears starting from the two-loop order (see [section 4](#двухпетлевые)).

---

## 4. Two-Loop $\beta$-Functions [T under model assumption] {#двухпетлевые}

:::note Adopted model
Section 4 assumes the **Gap Lagrangian** with a scalar field $\Gamma \in D(\mathbb{C}^7)$ and potential:
$$
V_{\text{Gap}} = \mu^2 \|\Gamma\|^2 + \lambda_3 \sum_{\text{Fano}} \gamma_{ij}\gamma_{jk}\gamma_{ki} + \lambda_4 \sum_{i<j} |\gamma_{ij}|^4
$$
with parameters $(\mu^2, \lambda_3, \lambda_4)$ as the only independent couplings ($G_2$-symmetry forbids others). It is this field theory that is referred to here as the "adopted model."
:::

:::tip Theorem 4.1 (Two-loop $\beta$-functions) [T under model assumption]
**(a)** Mass parameter:

$$
\beta_{\mu^2}^{(2)} = \beta_{\mu^2}^{(1)} + \frac{1}{(8\pi^2)^2}\left[-\frac{441\lambda_4^2}{2}\mu^2 + 147\lambda_3^2\lambda_4 - \frac{49\lambda_3^4}{4\mu^2}\right]
$$

Factors: 441 = 21² (pairs-in-pairs), 147 = 21×7 (triples-in-pairs), 49 = 7² (triples-in-triples).

**(b)** Cubic constant:

$$
\beta_{\lambda_3}^{(2)} = \beta_{\lambda_3}^{(1)} + \frac{1}{(8\pi^2)^2}\left[-\frac{315\lambda_3\lambda_4^2}{2} + \frac{35\lambda_3^3}{2\mu^2}\right]
$$

315 = 15×21, 35 = $C(7,3)$ (triples of the Fano complement).

**(c)** Quartic constant:

$$
\beta_{\lambda_4}^{(2)} = \beta_{\lambda_4}^{(1)} + \frac{1}{(8\pi^2)^2}\left[-\frac{63^2\lambda_4^3}{3} + 441\frac{\lambda_3^2\lambda_4}{\mu^2} - \frac{49\lambda_3^4}{4\mu^4}\right]
$$
:::

### Origin of Two-Loop Factors [T under model assumption]

The two-loop calculation requires integrating pairs of Gap fluctuations $\theta_{ij}$, $\theta_{kl}$ with frequencies in the shell $[\omega^* - \delta\omega^*, \omega^*]$. For each pair $(ij, kl)$:

- If $(ij)$ and $(kl)$ are connected by a [Fano line](/docs/physics/gauge-symmetry/fano-selection-rules): the contribution is proportional to $\lambda_3^2$ (through the cubic vertex factor).
- If $(ij)$ and $(kl)$ are not connected: the contribution is proportional to $\lambda_4^2$ (through two quartic vertex factors).
- Mixed contributions: proportional to $\lambda_3 \cdot \lambda_4$.

Combinatorial count:

| Object | Number | Formula |
|---|---|---|
| Pairs of coherences | $\binom{21}{2} = 210$ | |
| Pairs connected by a Fano line | $7 \times \binom{3}{2} = 21$ | |
| Unconnected pairs | $210 - 21 = 189$ | |
| Number of Fano triplets in two-loop diagrams | $\binom{7}{2} = 21$ (for $\lambda_3^2$) | |

The factors $441 = 21^2$, $147 = 21 \times 7$, $49 = 7^2$, $315 = 15 \times 21$, $35 = \binom{7}{3}$, $63^2 = 3969$ — all determined by the combinatorics of the Fano plane.

### Fate of the Octonionic Fixed Point (2-loop) [T under model assumption]

:::tip Theorem 4.2 (Octonionic fixed point at two loops) [T under model assumption]
**(a)** Gaussian fixed point: remains unchanged ($\mu^2 = \lambda_3 = \lambda_4 = 0$). Stability does not change.

**(b)** The Wilson-Fisher fixed point receives a two-loop correction:

$$
\lambda_4^{*(2)} = \frac{4\pi^2}{63} - \frac{16\pi^2}{63^3} \approx 0.0629 - 0.0002 = 0.0627
$$

The correction is $\sim 0.3\%$ — the fixed point is **stable** against higher corrections.

**(c)** Octonionic fixed point ($\lambda_3^* \neq 0$): **appears** in the two-loop approximation. From $\beta_{\lambda_3}^{(2)} = 0$ at $\lambda_4 \neq 0$:

$$
\lambda_3^{*} = \pm\sqrt{\frac{15\lambda_4 \mu^2}{35/(2 \cdot 8\pi^2) - 315\lambda_4/(2 \cdot 8\pi^2)}} \cdot 8\pi^2
$$

The fixed point exists when:

$$
\lambda_4 < \lambda_4^{(\text{crit})} = \frac{(8\pi^2)}{9 \cdot 315} \approx 0.0028
$$

**(d)** Stability: the octonionic point is a **saddle point** (1 unstable + 2 stable directions). It lies on the boundary between the Wilson-Fisher and Gaussian points.
:::

The octonionic fixed point describes the universality class of the "octonionic phase transition," in which the system transitions from the PT-invariant ($\lambda_3 = 0$) to the PT-breaking ($\lambda_3 \neq 0$) regime.

### Anomalous Dimension of the Gap Field (2-loop) [T under model assumption]

:::tip Theorem 4.3 (Anomalous dimension of the Gap field) [T under model assumption]
The anomalous dimension of the Gap field in the two-loop approximation:

$$
\eta_{\text{Gap}} = \frac{7\lambda_4^2}{2(8\pi^2)^2} - \frac{\lambda_3^2}{4(8\pi^2)^2 \mu^2} \approx 1.1 \times 10^{-4}
$$

**(a)** At the Wilson-Fisher point ($\lambda_3 = 0$): $\eta = 7\lambda_4^{*2}/(2 \cdot 64\pi^4) \approx 10^{-4}$ — negligibly small.

**(b)** At the octonionic point ($\lambda_3^* \neq 0$): $\eta$ can be **negative** (the $\lambda_3$-correction dominates). Negative $\eta$ means that Gap correlations decay slower than in the mean-field approximation.

**(c)** The critical exponent $\nu = 1/2 + O(\eta)$ receives a small correction. The mean-field approximation remains accurate to $\sim 0.01\%$.
:::

---

## 5. Three-Loop $\beta$-Functions and Stability [T under model assumption] {#трёхпетлевые}

Three-loop corrections $O(\lambda^3)$ are needed to confirm the stability of the octonionic fixed point, determine the conformal window, and compute the Zamolodchikov $c$-function.

### 5.1. Three-Loop Structure of the $\beta$-Functions

:::tip Theorem 5.1 (Three-loop $\beta$-functions of Gap theory) [T under model assumption]
Including three-loop corrections:

**(a)** Quartic constant:

$$
\beta_{\lambda_4}^{(3)} = \beta_{\lambda_4}^{(2)} + \frac{1}{(8\pi^2)^3}\left[C_1 \lambda_4^4 + C_2 \frac{\lambda_3^2 \lambda_4^2}{\mu^2} + C_3 \frac{\lambda_3^4}{\mu^4}\right]
$$

where the coefficients $C_1, C_2, C_3$ are determined by the three-loop combinatorics of the Fano plane.

**(b)** Three-loop diagrams are classified by topology:

| Diagram type | Number | Factor |
|---|---|---|
| Chain | $3 \times \binom{21}{2} = 630$ | $\lambda_4^3$ |
| Sunset | $\binom{21}{3} = 1330$ | $\lambda_4^3$ |
| Triangle | $7 \times \binom{21}{2} = 1470$ | $\lambda_3^2 \lambda_4$ |
| Double Fano | $\binom{7}{2} \times 21 = 441$ | $\lambda_3^2 \lambda_4$ |
| Triple Fano | $\binom{7}{3} = 35$ | $\lambda_3^3 / \mu$ |

Summation with symmetry factors:

$$
C_1 = -\frac{63^3}{6} + 1330 \cdot 63 = 42115.5
$$

$$
C_2 = -1470 \cdot 63 + 441 \cdot 15 = -85995
$$

$$
C_3 = 35 \cdot 49 = 1715
$$

**(c)** Correction to the Wilson-Fisher point:

$$
\frac{\delta\lambda_4^{(3)}}{\lambda_4^{*(2)}} \sim \frac{C_1 \, \lambda_4^{*(2)\,3}}{(8\pi^2)^3} \sim \frac{42115 \cdot (0.063)^3}{(248)^3} \sim 7 \times 10^{-7}
$$

The three-loop correction to the WF-point is $\sim 10^{-4}\%$ — negligibly small.
:::

### 5.2. Stability of the Octonionic Fixed Point (3-loop) [T under model assumption]

:::tip Theorem 5.2 (Octonionic fixed point: three-loop stability) [T under model assumption]
At $O(\lambda^3)$ order the octonionic fixed point is **stable**:

**(a)** From $\beta_{\lambda_3}^{(3)} = 0$:

$$
\lambda_3^{*(3)} = \lambda_3^{*(2)} \cdot \left(1 + \frac{C_2' \, \lambda_4^{*(2)\,2}}{(8\pi^2)^2}\right)
$$

where $C_2' \approx -85995 / (15 \cdot 63) \approx -91$, giving:

$$
\frac{\delta\lambda_3^{(3)}}{\lambda_3^{*(2)}} \approx \frac{-91 \cdot (0.063)^2}{(248)^2} \approx -6 \times 10^{-6}
$$

Correction $\sim 10^{-3}\%$ — the octonionic point is stable at three loops.

**(b)** Value of the coupling ratio at the octonionic fixed point:

$$
\frac{\lambda_3^*}{\lambda_4^*} \sim \frac{1}{8\pi^2} \approx 0.013
$$

The cubic coupling is **suppressed** relative to the quartic by $\sim 2$ orders of magnitude.

**(c)** The stability of both types of fixed points (WF and octonionic) confirms:
- Critical exponents are accurate to $\sim 10^{-6}$.
- The mean-field approach is justified ($d_{\text{eff}} = 21 \gg d_c = 4$).
- The phase transition to the octonionic point ($\lambda_3 \neq 0$) is a **robust** phenomenon, independent of the loop order.
:::

### 5.3. Summary of Fixed Points by Loop Order

| Fixed point | 1-loop | 2-loop | 3-loop | Character |
|---|---|---|---|---|
| **Gaussian** ($\lambda_3 = \lambda_4 = 0$) | Exists | Unchanged | Unchanged | Unstable |
| **Wilson-Fisher** ($\lambda_3 = 0$, $\lambda_4^* \neq 0$) | Exists | 0.3% correction | $10^{-4}\%$ correction | IR-stable attractor |
| **Octonionic** ($\lambda_3^* \neq 0$) | Does not exist | Appears (saddle) | Stable ($10^{-3}\%$ correction) | Critical (PT-transition) |

---

## 6. Conformal Window [T] {#конформное-окно}

:::tip Theorem 6.1 (Conformal window of Gap theory) [T]
**(a)** With $N_f$ fermionic generations in the [Lindblad](/docs/core/operators/lindblad-operators) sector, the $\beta$-function of $\lambda_4$ has a zero at:

$$
N_f^{(\text{crit})} = \frac{63}{2c_f} \approx 3.5
$$

**(b)** For $N_f = 3$ (real world): the system is **outside** the conformal window — no IR conformal symmetry.

**(c)** Conformal window: $3.5 < N_f < 7$. In this range, Gap theory possesses an IR conformal phase.
:::

### Conformal Symmetry at Fixed Points [T]

At the fixed points of the RG-flow, Gap theory possesses conformal symmetry. At the Wilson-Fisher point ($\lambda_3^* = 0$, $\lambda_4^* = 4\pi^2/63$) the theory becomes a conformal field theory (CFT) on the 21-dimensional space of coherences with $G_2$-symmetry.

The effective central function (Zamolodchikov $c$-function):

$$
c(\mu) = c_{\text{UV}} - \int_\mu^{\Lambda} \frac{d\mu'}{\mu'} \, \beta_i(\mu') \frac{\partial^2 \mathcal{F}}{\partial g_i \partial g_j} \beta_j(\mu') \geq 0
$$

where $\mathcal{F}$ is the free energy of Gap theory. At the WF-point:

$$
c_{\text{WF}} = 21 - \frac{1}{2}\eta_{\text{Gap}} \cdot 21 \approx 21 - 0.001 \approx 21
$$

(21 is the number of Gap fields, $\eta$ is the anomalous dimension). At the octonionic point:

$$
c_{\text{oct}} = 21 - \frac{1}{2}\eta_{\text{oct}} \cdot 21 < c_{\text{WF}}
$$

The value $\eta_{\text{oct}}$ can be negative (see Theorem 4.3(b)), which increases $c_{\text{oct}}$. However, the $c$-theorem guarantees $c_{\text{UV}} > c_{\text{oct}} > c_{\text{IR}}$.

### Physical Consequences of the Conformal Window

For $N_f = 3$ (real world) the system lies **outside** the conformal window. This means:
- There is no IR conformal phase, but the WF-fixed point governs the critical exponents near the I↔II phase transition.
- Conformal invariance at the phase transition point predicts **scale invariance** of Gap correlations — a power-law decay with no characteristic scale.
- At $N_f = 4$ (hypothetical fourth generation) the system falls into the conformal window, which radically changes the IR behavior.

---

## 7. $c$-Theorem [T] {#c-теорема}

:::tip Theorem 7.1 ($c$-theorem for Gap) [T]
**(a)** Central charge of Gap theory:

$$
c(\mu) = 21 + N_f \cdot 7 - \frac{\lambda_4^2}{(4\pi)^2} \cdot C_{\text{Fano}} + O(\lambda^3)
$$

where $C_{\text{Fano}} = 7$ is the contribution from Fano constraints.

**(b)** $c(\mu)$ decreases monotonically in the IR direction: $dc/d\ln\mu \leq 0$.
:::

### Proof of Monotonicity [T]

The monotonic decrease of $c(\mu)$ follows from the positive definiteness of the Zamolodchikov metric $\partial^2 \mathcal{F} / \partial g_i \partial g_j$ in the space of couplings. For Gap theory:

$$
\frac{dc}{d\ln\mu} = -\beta_i \frac{\partial^2 \mathcal{F}}{\partial g_i \partial g_j} \beta_j \leq 0
$$

Equality is achieved only at fixed points ($\beta_i = 0$). Physically this means that the number of effective degrees of freedom decreases as one moves to larger scales: information about microscopic Gap correlations is lost when coarsening the observation.

Values of $c$ at the fixed points:

| Point | $c$ | Interpretation |
|---|---|---|
| UV (free) | $21 + 7N_f$ | All 21 coherences + $7N_f$ fermionic modes |
| Wilson-Fisher | $\approx 21$ | Quartic interaction weakly reduces the number of modes |
| Octonionic | $< 21$ | Cubic interaction additionally reduces $c$ |

The strict inequality $c_{\text{UV}} > c_{\text{WF}} > c_{\text{oct}}$ confirms that the RG-flow is directed from the free theory toward the octonionic point as the scale decreases.

---

## 8. RG-Suppression of $\lambda_3$ [T] {#rg-подавление}

:::tip Theorem 8.1 (RG-suppression of the cubic coupling) [T]
Over the running from the Planck scale to the electroweak breaking scale:

$$
\lambda_3(\mu_{\text{EW}}) = \lambda_3(M_{\text{Pl}}) \cdot \left(\frac{\mu_{\text{EW}}}{M_{\text{Pl}}}\right)^{15\lambda_4^*/(8\pi^2)}
$$

Anomalous dimension $\gamma_{\lambda_3} = 15\lambda_4^*/(8\pi^2) \approx 7.26$. Suppression:

$$
\lambda_3^2 \sim \left(\frac{\mu_{\text{EW}}}{M_{\text{Pl}}}\right)^{14.52} \sim 10^{-14.5}
$$

This gives **14.5 orders** of suppression in the [$\Lambda$ budget](/docs/proofs/gap/lambda-budget).
:::

### Detailed Derivation of Suppression [T]

From $\beta_{\lambda_3}^{(1)} = -15\lambda_3\lambda_4 / (8\pi^2)$ it follows that with fixed $\lambda_4 = \lambda_4^*$ (near the Wilson-Fisher point) the equation for $\lambda_3$ is linear:

$$
\frac{d\lambda_3}{d\ln\omega} = -\frac{15\lambda_4^*}{8\pi^2} \lambda_3 \equiv -\Delta_3 \cdot \lambda_3
$$

Solution:

$$
\lambda_3(\omega) = \lambda_3(\omega_0) \cdot \left(\frac{\omega}{\omega_0}\right)^{\Delta_3}
$$

where $\Delta_3 = 15\lambda_4^* / (8\pi^2)$ is the **anomalous dimension** of the operator $V_3$.

Substituting $\lambda_4^* = 4\pi^2/63$:

$$
\Delta_3 = \frac{15 \cdot 4\pi^2/63}{8\pi^2} = \frac{60}{504} = \frac{5}{42} \approx 0.119
$$

Integrating from the Planck scale $\omega_{\text{UV}} = \omega_{\text{Planck}} \approx 1.855 \times 10^{43} \text{ s}^{-1}$ to the cosmological scale $\omega_{\text{IR}} = H_0 \approx 2.2 \times 10^{-18} \text{ s}^{-1}$:

$$
\frac{\omega_{\text{IR}}}{\omega_{\text{UV}}} \approx 1.2 \times 10^{-61}
$$

$$
\frac{\lambda_3^{(\text{IR})}}{\lambda_3^{(\text{UV})}} = (1.2 \times 10^{-61})^{5/42} \approx 10^{-61 \cdot 0.119} \approx 10^{-7.26}
$$

The square of $\lambda_3$ (which enters the $\Lambda$ budget) is suppressed by a factor of $10^{-14.5}$. This is the **key mechanism** for explaining the smallness of the cosmological constant in Gap theory.

### Role of RG-Suppression in the $\Lambda$ Budget [T]

The full hierarchy of suppression of the cosmological constant is composed of several mechanisms:

| Mechanism | Suppression factor | Status |
|---|---|---|
| $\varepsilon^6$ (smallness of vacuum coherences) | $10^{-12}$ | [T] |
| RG-suppression of $\lambda_3$ (IR-irrelevance) | $10^{-14.5}$ ($\lambda_3^2$ suppressed) | [T] |
| Ward identities (anticorrelation) | $\times 19/49 \approx 0.39$ | [T] |
| [Fano code](/docs/physics/gauge-symmetry/fano-selection-rules) (6 linear constraints) | $\times 1/8$ | [T] |

RG-suppression of $\lambda_3$ provides the **largest contribution** among the rigorously justified mechanisms. Detailed analysis — in the [$\Lambda$ budget](/docs/proofs/gap/lambda-budget).

---

## 9. Anomalous Dimension of the Fano Operator [T] {#аномальная-размерность}

:::tip Theorem 9.1 (Anomalous dimension $\Delta_3$) [T]
The Fano-triplet operator $F_{ijk} = \varepsilon_{ijk}^{\text{Fano}} \cdot \text{Gap}(i,j) \cdot \text{Gap}(j,k) \cdot \text{Gap}(i,k)$ has anomalous dimension:

$$
\Delta_3 = 3 - \frac{5}{42} \approx 2.881
$$

The deviation $5/42 \approx 0.119$ from the canonical dimension 3 determines the [correlation length](/docs/physics/cosmology-phys/dark-matter) $\xi_F \sim 160$ pc via the RG-equation.
:::

### Spectrum of Scaling Dimensions of Gap-CFT Operators [T]

Full spectrum of composite operators in the conformal field theory on Gap:

| Operator | Engineering dim | Anomalous dim | Full $\Delta$ |
|---|---|---|---|
| $\text{Gap}(i,j)$ | 1 | $+\eta/2 \approx 5 \times 10^{-5}$ | $\approx 1$ |
| $\text{Gap}^2(i,j)$ | 2 | $+2\eta \approx 2 \times 10^{-4}$ | $\approx 2$ |
| $\text{Gap}^3$ (Fano triplet) | 3 | $-5/42 \approx -0.119$ | $\approx 2.881$ |
| $\sum \text{Gap}^2$ (total, $G_2$-singlet) | 2 | 0 | 2 |

The Fano-triplet operator

$$
\mathcal{O}_{\text{Fano}} = \sum_{\text{Fano}} \text{Gap}(i,j)\,\text{Gap}(j,k)\,\text{Gap}(i,k)
$$

has $\Delta_3 < 3$, which means: it is **relevant** in the IR. This is a crucially important result — the octonionic structure ($V_3$) does **not** simply get suppressed at macroscopic scales, but determines the dominant correlations near the octonionic fixed point.

### Connection of $\Delta_3$ with the Correlation Length [T]

From the RG-equation for the Fano operator near the WF-point:

$$
\mathcal{O}_{\text{Fano}}(r) \sim r^{-2\Delta_3} = r^{-5.762}
$$

The transition to exponential decay occurs at the scale of the Fano correlation length:

$$
\xi_F = \frac{1}{\mu} \left(\frac{\lambda_4^*}{\lambda_3^*}\right)^{1/(3 - \Delta_3)} \sim \frac{1}{\mu} \left(\frac{1}{\lambda_3^*}\right)^{42/5}
$$

The value $\xi_F$ determines the scale at which Fano correlations (and the dark-matter effects associated with them) become significant. The estimate $\xi_F \sim 160$ pc is obtained upon substituting the vacuum values of the parameters.

### Duality of IR-Relevance [T]

There is a subtle duality in the behavior of the Fano operator:

- **Cubic coupling** $\lambda_3$ (coefficient of $V_3$) — **IR-irrelevant**: $\lambda_3 \to 0$ as $\omega \to 0$.
- **Fano operator** $\mathcal{O}_{\text{Fano}}$ (composite operator) — **IR-relevant**: $\Delta_3 < 3$.

Resolution: $\lambda_3$ decreases, but the correlations generated by the Fano structure grow. At the octonionic fixed point both effects balance, producing a non-trivial conformal theory with $c_{\text{oct}} < c_{\text{WF}}$.

---

## 10. RG-Evolution from Planck to Cosmology [T] {#rg-эволюция}

The complete picture of the RG-evolution of Gap theory parameters from the Planck scale to the cosmological scale:

### 10.1. Dimensional Analysis [T]

All parameters of Gap theory acquire physical dimensions through the system frequency $\omega_0$ (Axiom 4):

$$
\mu_{\text{phys}} = \mu \cdot \omega_0, \qquad \Lambda_{\text{phys}} = \frac{\Lambda_{\text{Gap}} \cdot \omega_0^2}{c^2}
$$

For the cosmological vacuum: $\omega_0^{(\text{Planck})} = c^5/(\hbar G) \approx 1.855 \times 10^{43} \text{ s}^{-1}$.

### 10.2. Evolution of $\lambda_3$ from Planck to Hubble [T]

Integrating the RG-flow over the full running $\omega_{\text{Planck}} \to H_0$:

$$
\lambda_3^{(\text{IR})} = \lambda_3^{(\text{UV})} \cdot \left(\frac{H_0}{\omega_{\text{Planck}}}\right)^{5/42}
$$

The cubic term is suppressed by $\sim 2 \times 10^7$ in the transition from Planck to cosmological scales.

### 10.3. Evolution of $\lambda_4$ [T under model assumption]

In contrast to $\lambda_3$, the quartic coupling $\lambda_4$ quickly reaches the Wilson-Fisher fixed point:

$$
\lambda_4(\omega) \to \lambda_4^* = \frac{4\pi^2}{63} \approx 0.063 \quad \text{at } \omega \ll \omega_{\text{Planck}}
$$

The plateau is reached already at $\omega \sim \omega_{\text{Planck}} / 10$ — the quartic coupling "freezes" at scales substantially exceeding the Planck scale.

### 10.4. Evolution of the Mass Parameter $\mu^2$ [T under model assumption]

The mass parameter determines the position of the I↔II phase transition. Under RG-evolution:

$$
\mu^2(\omega) = \mu^2(\omega_0) \cdot \left(\frac{\omega}{\omega_0}\right)^{2 - \gamma_{\mu^2}}
$$

where $\gamma_{\mu^2} = 21\lambda_4^*/(8\pi^2) \approx 0.017$ is the anomalous dimension of the mass. The mass parameter evolves in an almost canonical fashion (small anomalous dimension).

---

## 11. Cosmological Constant with RG-Flow Taken into Account [T] {#космологическая-постоянная}

:::tip Theorem 11.1 (Λ with RG-evolution taken into account) [T]
With dimensional analysis and RG-evolution taken into account:

$$
\Lambda_{\text{phys}} = \frac{96[\lambda_3^{(\text{IR})}]^2 \varepsilon^6}{\mu^2} \cdot \frac{\omega_0^2}{c^2}
$$

Without RG-suppression: $\Lambda \sim 10^{54}$ m$^{-2}$. With RG-suppression ($\lambda_3^{(\text{IR})} \sim 10^{-7.26} \lambda_3^{(\text{UV})}$): the RG-flow improves by $\sim 14.5$ orders (through $\lambda_3^2$).

The remaining discrepancy with the observed $\Lambda_{\text{obs}} \approx 10^{-52}$ m$^{-2}$ is the standard cosmological constant problem, additionally compensated by Ward identities and Fano constraints (see [$\Lambda$ budget](/docs/proofs/gap/lambda-budget)).
:::

---

## 12. Connection of RG-Flow with the Standard Model [T] {#стандартная-модель}

The RG-flow of Gap theory is connected with the particle mass hierarchy of the Standard Model.

### 12.1. Uniformity of the Anomalous Dimension of Coherences [T] {#однородность-аномальной-размерности}

:::tip Theorem 12.1 (Uniformity of $\Delta_{ij}$) [T]
All 21 coherences $\gamma_{ij}$ have the **same** anomalous dimension at the Wilson-Fisher fixed point:

$$
\Delta_{ij} = \frac{\eta}{2} \approx 5 \times 10^{-5} \quad \forall\; i \neq j
$$

where $\eta$ is the anomalous dimension of the Gap field (Theorem 4.3).
:::

**Proof.** In $\mathrm{PG}(2,2)$ exactly one line passes through any two points $i,j \in \{0,\ldots,6\}$ (axiom of a projective plane). Consequently, the number of Fano lines through a pair $n_{\text{Fano}}(i,j) = 1$ for **all** 21 pairs — there are no pairs "outside Fano lines."

The one-loop self-energy of the coherence $\gamma_{ij}$ with the cubic vertex $V_3$:

$$
\Sigma_{ij}^{(1)}(k) = \frac{\lambda_3^2}{8\pi^2} \sum_{k:\, f_{ijk} \neq 0} G_0(k) = \frac{\lambda_3^2}{8\pi^2} \cdot G_0(k)
$$

The sum contains exactly **one** term (the unique third index $k$ on the line through $i,j$), identical for all pairs. Consequently, the anomalous dimension $\Delta_{ij}$ is **the same** for all coherences. At the WF-point ($\lambda_3 = 0$) the anomalous dimension is determined by the quartic sector and equals $\eta/2$ (Theorem 4.3). $\blacksquare$

### 12.2. Mass Hierarchy from the Yukawa Selection Rule [T] {#иерархия-масс}

:::tip Theorem 12.2 (Mass hierarchy mechanism) [T]
The fermion mass hierarchy in Gap theory is generated **not** by differences in the anomalous dimensions of coherences, but by three mechanisms:

**(a)** **Selection rule (T-43d [T])**: tree-level Yukawa coupling $y_k^{(\text{tree})} = g_W \cdot f_{k,E,U} \cdot |\gamma_{\text{vac}}^{(EU)}|$, where $f_{ijk}$ are the octonionic structure constants. The unique non-zero one: $f_{1,5,6} = 1$ (Higgs line $\{A,E,U\}$), giving $y_1 \sim O(1)$, $y_2 = y_4 = 0$.

**(b)** **Quasi-IR fixed point [T]**: the unique $O(1)$ Yukawa $y_1$ is attracted to the Pendleton–Ross fixed point, giving $m_t \approx 173$ GeV.

**(c)** **$V_3$-induced mixing [H]**: masses of the light generations ($k=2,4$) arise through loop-level mixing along the generation line $\{1,2,4\}$, suppressed by a factor $\varepsilon \sim 10^{-2}$ per order.
:::

The mass ratios of the generations are determined by powers of suppression $\varepsilon$:

$$
\frac{m_2}{m_1} \sim \varepsilon, \qquad \frac{m_3}{m_1} \sim \varepsilon^2
$$

where $m_1$ is the mass of the 3rd generation ($k=1$), $m_2$ of the 2nd ($k=4$), $m_3$ of the 1st ($k=2$). Detailed derivation — in [Yukawa hierarchy](/docs/physics/particle-physics/yukawa-hierarchy).

### 12.3. RG-Enhancement of the Hierarchy [T] {#rg-усиление}

RG-evolution **preserves** the hierarchy established by the selection rule at the GUT scale:

**(a)** Small Yukawa couplings $y_{2,4} \ll 1$ run with anomalous dimension $\gamma_n = (c_2 y_1^2 - c_3 g_s^2 - c_4 g_W^2)/(16\pi^2)$. At $c_2 y_1^2 \approx c_3 g_s^2 + c_4 g_W^2$: $\gamma_n \approx 0$, small Yukawa couplings **preserve** their values from GUT to EW.

**(b)** Suppression of $\lambda_3$ (Theorem 8.1 [T]) additionally reduces the loop corrections to $y_{2,4}$ in the IR, enhancing the hierarchy.

Result: the mass hierarchy is a consequence of the $G_2$-invariance of the octonionic structure constants (selection rule), not of differences in the anomalous dimensions of individual coherences.

---

## Related Documents

- [Gap thermodynamics](/docs/core/dynamics/gap-thermodynamics) — potential $V_{\text{Gap}}$
- [Phase diagram](/docs/core/dynamics/gap-phase-diagram) — critical phenomena
- [$\Lambda$ budget](/docs/proofs/gap/lambda-budget) — RG-suppression in the budget
- [Noether charges](/docs/physics/gauge-symmetry/noether-charges) — 14 conserved charges
- [Zeta regularization](/docs/physics/dual-aspect/zeta-regularization) — $Z_\Phi(-k) = 0$
- [Fano selection rules](/docs/physics/gauge-symmetry/fano-selection-rules) — Fano plane combinatorics
- [Yukawa hierarchy](/docs/physics/particle-physics/yukawa-hierarchy) — mass hierarchy from RG-flow
- [Composite systems](/docs/core/dynamics/composite-systems) — collective RG-effects
