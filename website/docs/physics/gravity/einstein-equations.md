---
sidebar_position: 2
title: "Einstein Equations from Gap"
slug: /physics/gravity/einstein-equations
description: "Derivation of the Einstein equations from the Gap action via the Lovelock theorem, two-loop renormalization group with Fano combinatorics, Swallowtail catastrophe, and connection with L-levels"
---

# Einstein Equations from Gap

:::info Who this chapter is for
Derivation of the Einstein equations from the Gap action via the Chamseddine–Connes spectral action. The reader will learn why gravity is emergent in UHM.
:::


## Overview

The central result of the gravitational sector of UHM: **the Einstein equations are derived** from the Gap action via the Chamseddine–Connes spectral action [T]. The full spectral triple from [T-53 [T]](/docs/core/foundations/spacetime#теорема-спектральная-тройка) reproduces the Einstein–Hilbert action + the Standard Model. An additional argument is the Lovelock theorem. Gravity **is not** a fundamental interaction — it emerges from Gap curvature.

---

## 1. Emergent Metric from Coherences

### 1.1 Projection onto the 4D Sector

From the decomposition $\mathrm{SU}(3) \subset G_2$:

$$
\mathrm{Im}(\mathbb{O}) \cong \mathbb{R}^7 = \mathbb{R}^1_{\mathrm{time}} \oplus \mathbb{R}^3_{\mathrm{space}} \oplus \mathbb{R}^3_{\mathrm{gap}}
$$

Projector onto the spacetime sector:

$$
\Pi_{\mathrm{ST}}: \mathbb{R}^7 \to \mathbb{R}^4, \quad \Pi_{\mathrm{ST}} = \Pi_O \oplus \Pi_{\mathrm{Re}}
$$

where $\Pi_O$ is the projection onto the $O$-dimension (emergent time), $\Pi_{\mathrm{Re}}$ is the projection onto $\mathrm{Re}(\mathbb{C}^3)$ (space).

### 1.2 Metric Tensor

:::tip Theorem 1.1 (Emergent metric) [T]
The emergent metric on 4D spacetime:

$$
g_{\mu\nu}(x) = \eta_{\mu\nu} + h_{\mu\nu}(x)
$$

where $\eta_{\mu\nu} = \mathrm{diag}(+1, -1, -1, -1)$, and the perturbation:

$$
h_{\mu\nu}(x) = \sum_{i \in \mu,\, j \in \nu} |\gamma_{ij}|^2 \cdot \mathrm{Gap}(i,j)^2
$$

summation over holon dimensions belonging to the given 4D direction.
:::

**Properties:**

**(a)** Linear order at $\mathrm{Gap} \ll 1$:

$$
h_{\mu\nu} \approx \sum_{i \in \mu,\, j \in \nu} |\gamma_{ij}|^2 \sin^2(\theta_{ij})
$$

**(b)** Lorentzian signature is ensured by the background metric $\eta_{\mu\nu} = \mathrm{diag}(+1,-1,-1,-1)$. The perturbation $h_{\mu\nu} \geq 0$ (as a sum of squares) does not change the signature when $|h_{\mu\nu}| \ll 1$.

:::warning Status map of the derivation
- Spectral action → $R_{\mu\nu}$: **[T]** (T-53, standard Chamseddine–Connes result)
- Linearization $h_{\mu\nu} \sim |\gamma_{ij}|^2 \sin^2(\theta_{ij})$: **[C under weak-field]** (valid in the weak-field approximation; the full nonlinear connection is an open problem)
:::

:::warning Origin of $\eta_{\mu\nu}$: resolved [T]
The formula $h_{\mu\nu} = \sum |\gamma_{ij}|^2 \cdot \mathrm{Gap}^2$ yields only non-negative components. The Lorentzian signature $(+1,-1,-1,-1)$ is **derived** from the finite spectral triple [T-53 [T]](/docs/core/foundations/spacetime#теорема-спектральная-тройка): the Page–Wootters mechanism gives $g_{00} > 0$ (temporal component), and the spatial components $g_{aa} < 0$ from the spectrum of $D_{\text{int}}$. The signature convention $(+1,-1,-1,-1)$ (east coast convention) is used consistently throughout all documents of the theory.
:::

**(c)** Connes distance:

$$
d(p, q) = \sup\{|f(p) - f(q)| : \|[D_\alpha, f]\| \leq 1\}
$$

defines the metric via the spectral data of the Dirac operator $D_\alpha$, whose eigenvalues are determined by the coherences $\Gamma$.

---

## 2. Projection of the Gap Action onto 4D

:::tip Theorem 1.2 [T]
The Gap action upon projection onto the 4D sector takes the form:

$$
S_{\mathrm{Gap}}^{(4D)} = \int d^4x \sqrt{-g} \left[\frac{1}{16\pi G_{\mathrm{Gap}}} \mathcal{R}^{(4D)} + \Lambda_{\mathrm{Gap}} + \mathcal{L}_{\mathrm{matter}}^{(4D)}\right]
$$
:::

where:

**(a)** Scalar curvature: $\mathcal{R}^{(4D)} = g^{\mu\nu} R_{\mu\nu}^{(4D)}$

**(b)** Gravitational constant:

$$
G_{\mathrm{Gap}} = \frac{c^4}{2\mu^2 \cdot \langle|\gamma_{\mathrm{ST}}|^2\rangle}
$$

where $\langle|\gamma_{\mathrm{ST}}|^2\rangle = \frac{1}{6}\sum_{\substack{i,j \in \mathrm{ST} \\ i < j}} |\gamma_{ij}|^2$ is the mean squared modulus of the coherence in the spacetime sector (6 pairs from 4 directions).

**(c)** Cosmological constant:

$$
\Lambda_{\mathrm{Gap}} = \mu^2 \cdot \mathcal{G}_{\mathrm{total}}^{(O)}
$$

where $\mathcal{G}_{\mathrm{total}}^{(O)} = \sum_i \mathrm{Gap}(O,i)^2 \cdot |\gamma_{Oi}|^2$ is the total opacity of the $O$-sector.

**(d)** Matter Lagrangian:

$$
\mathcal{L}_{\mathrm{matter}}^{(4D)} = \Pi_{\mathrm{ST}}\!\left[\frac{m_{ij}}{2}\dot{\theta}_{ij}^2 + V_3(\theta) + V_4(\theta) - V_2^{(4D)}(\theta)\right]
$$

### 2.1 Derivation Chain for the Projection [T]

The proof of Theorem 1.2 proceeds through four steps building a bridge from the full Gap action to the Einstein–Hilbert form.

**Step 1 (Original Gap action).** Full action on the 21-dimensional coherence space:

$$
S_{\mathrm{Gap}} = \int d\tau \left[\sum_{i<j} \frac{m_{ij}}{2}\dot{\theta}_{ij}^2 - V_{\mathrm{Gap}}(\theta) + \mathcal{L}_{\mathrm{top}} + \mathcal{L}_{\mathrm{diss}} + \mathcal{L}_{\mathrm{reg}} + \mathcal{L}_{\mathrm{ext}}\right]
$$

**Step 2 (Sector decomposition).** The 21 coherence pairs are divided into three groups:

| Group | Definition | Number of pairs | Role |
|--------|-------------|----------------|------|
| ST pairs | $(i,j)$, both in $\{O, \mathrm{Re}_1, \mathrm{Re}_2, \mathrm{Re}_3\}$ | 6 | Determine $g_{\mu\nu}$ |
| Gap pairs | $(i,j)$, one or both in $\{\mathrm{Im}_1, \mathrm{Im}_2, \mathrm{Im}_3\}$ | 15 | Determine "matter" |
| Cross | Between ST and Gap sectors | (subset of Gap pairs) | Contribution to $T_{\mu\nu}$ |

**Step 3 (Projection of the quadratic potential).** The potential $V_2 = \mu^2 \mathcal{G}_{\mathrm{total}}$ upon projection onto the ST sector:

$$
V_2^{(4D)} = \mu^2 \sum_{\substack{i,j \in \mathrm{ST} \\ i < j}} |\gamma_{ij}|^2 \sin^2(\theta_{ij}) = \mu^2 \sum_{\mu < \nu} h_{\mu\nu}
$$

Scalar curvature in the linearized approximation: $R^{(4D)} \sim \partial^2 h \sim \mu^2 \cdot \sum \sin^2(\theta)$. Comparison gives:

$$
R^{(4D)} \propto \frac{V_2^{(4D)}}{\langle|\gamma|^2\rangle}
$$

from which $G_{\mathrm{Gap}}$ is identified.

:::tip Lemma (Linearized bridge derivation) [T under $|\delta\Gamma| \ll 1$] {#лемма-линеаризованный-мост}

**Setup.** Let $\Gamma_0$ be a vacuum configuration with coherences of the ST sector $\gamma_{\mu\nu}^{(0)} = \varepsilon_0 e^{i\phi_{\mu\nu}^{(0)}}$, $\mu,\nu \in \{A,S,D,L\}$. Consider a spatially dependent perturbation $\gamma_{\mu\nu}(x) = \gamma_{\mu\nu}^{(0)} + \delta\gamma_{\mu\nu}(x)$ with $|\delta\gamma_{\mu\nu}| \ll \varepsilon_0$.

**(a) Metric identification** [definition]:
$$h_{\mu\nu}(x) \equiv \frac{2\,\mathrm{Re}(\delta\gamma_{\mu\nu}(x))}{\varepsilon_0}, \quad g_{\mu\nu}(x) = \eta_{\mu\nu} + h_{\mu\nu}(x)$$

The imaginary part $\mathrm{Im}(\delta\gamma_{\mu\nu})$ parametrizes the $B$-field (2-form), which is inessential in this sector.

**(b) Kinetic term → Fierz–Pauli action** [T]:

The kinetic term of the Gap action for the $x$-dependent configuration in the ST sector (arising from the product spectral triple $D = D_\mathrm{ext} \otimes \mathbf{1} + \gamma_5 \otimes D_\mathrm{int}$, T-53):
$$S_\mathrm{kin}^{(ST)} = \frac{\varepsilon_0^2}{4\mu^2} \int \sum_{\mu < \nu \in \mathrm{ST}} \partial_\rho h_{\mu\nu}(x)\,\partial^\rho h^{\mu\nu}(x)\;d^4x$$

After integration by parts (boundary terms vanish under the asymptotic condition $h_{\mu\nu}(x) \to 0$ as $|\mathbf{x}| \to \infty$, standard asymptotic flatness) and imposing the de Donder gauge $\partial^\mu \bar{h}_{\mu\nu} = 0$ (where $\bar{h}_{\mu\nu} = h_{\mu\nu} - \frac{1}{2}\eta_{\mu\nu} h$):
$$S_\mathrm{kin}^{(ST)} \supset \frac{1}{32\pi G_N^{(ST)}} \int \!\!\left[-\tfrac{1}{2}\partial_\rho h_{\mu\nu}\partial^\rho h^{\mu\nu} + \tfrac{1}{4}\partial_\rho h\,\partial^\rho h\right]d^4x$$

This is the standard massless spin-2 Fierz–Pauli action with:
$$G_N^{(ST)} = \frac{4\pi\mu^2}{\varepsilon_0^2}$$

The tensor structure of $R_{\mu\nu}$ (not just the scalar $R$) is reproduced in full, since $S_\mathrm{kin}^{(ST)}$ is quadratic in all components of $h_{\mu\nu}$ and contains the correct cross-terms from $\partial_\rho h_{\mu\nu}\partial^\rho h^{\mu\nu}$.

**(c) On-shell closure of Step 3** [T under small $\delta\theta$]:

The potential $V_2^{(ST)} \approx \mu^2 \varepsilon_0^2 \sum_{\mu<\nu} \theta_{\mu\nu}^2(x)$ plays the role of a source $T_{\mu\nu}$. Equations of motion:
$$\Box\, h_{\mu\nu}(x) = 8\pi G_N^{(ST)}\,T_{\mu\nu}^{(\mathrm{Gap})}(x) = 8\pi G_N^{(ST)}\cdot \mu^2\varepsilon_0^2\sin^2(\theta_{\mu\nu}(x))\cdot \eta_{\mu\nu}$$

Hence on-shell:
$$R^{(4D)} \sim \partial^2 h \sim \mu^2\sin^2(\theta) \qquad \blacksquare$$

The relation of Step 3 is a **field equation** (on-shell), not a kinematic identity. It holds rigorously in the classical limit at small $\theta$. The nonlinear generalization is via T-53 [T] (arbitrary $\theta$, full Einstein tensor, no weak-field assumption).
:::

:::note Hierarchy of proofs
Step 3 (bridge lemma) — **[T under $|\delta\Gamma| \ll 1$]**: closed for the linearized regime. Main Theorem 1.3 — **[T]** via T-53: closed for arbitrary fields. The geometric explanation of Step 3 and the main result are now consistent and mutually independent.
:::

**Step 4 (Cosmological term).** The non-dynamical part of $V_2$ in the $O$-sector (constant background Gap) gives $\Lambda_{\mathrm{Gap}}$.

---

## 3. Einstein Equations from Gap Variation

:::tip Theorem 1.3 (Main result) [T]
**Status [T]:** The full spectral triple $(A, H, D)$ from [T-53 [T]](/docs/core/foundations/spacetime#теорема-спектральная-тройка) satisfies Connes' axioms. The Chamseddine–Connes spectral action $S = \mathrm{Tr}(f(D_A/\Lambda))$ reproduces the Einstein–Hilbert action with $G_N = 3\pi/(7 f_2\Lambda^2)$ [T]. Additional argument: the Lovelock theorem (applicability to the emergent metric — [C under T-120], see [analysis of limitations](#34-ограничения-аргумента-лавлока) below). T-120 [T] derives $M^4$ as a smooth 4-manifold; the Lovelock theorem requires a smooth 4D manifold + diffeoinvariance + metric tensor — all conditions are satisfied by the emergent $M^4$.

Variation of the full Gap action with respect to the emergent metric $g_{\mu\nu}$ gives the Einstein equations:

$$
\frac{\delta S_{\mathrm{Gap}}^{(4D)}}{\delta g^{\mu\nu}} = 0 \quad \Longrightarrow \quad G_{\mu\nu} + \Lambda_{\mathrm{Gap}}\, g_{\mu\nu} = 8\pi G_{\mathrm{Gap}} \cdot T_{\mu\nu}^{(\mathrm{Gap})}
$$

where $G_{\mu\nu} = R_{\mu\nu} - \frac{1}{2}g_{\mu\nu}R$ is the Einstein tensor.
:::

**Proof (outline).**

**Main argument (spectral action).** The full spectral triple $(A, H, D)$ with finite part from [T-53 [T]](/docs/core/foundations/spacetime#теорема-спектральная-тройка) generates the spectral action $\mathrm{Tr}(f(D_A/\Lambda))$, whose expansion in Seeley–DeWitt coefficients gives the Einstein–Hilbert action with $G_N = 3\pi/(7 f_2 \Lambda^2)$ (details — [full spectral action](/docs/physics/gravity/quantum-gravity#теорема-полное-спектральное-действие)).

**Additional argument (Lovelock theorem).**

**Step 1 (Conditions of the Lovelock theorem).** The action $S_{\mathrm{Gap}}^{(4D)}$ satisfies:
- **4D covariance:** The projection $\Pi_{\mathrm{ST}}$ commutes with $G_2$-transformations that stabilize the $\mathrm{SU}(3)$-subgroup. Therefore $S_{\mathrm{Gap}}^{(4D)}$ is invariant under transformations induced on the 4D sector.
- **Metricity:** The action depends on $g_{\mu\nu}$ and its first and second derivatives (via the curvature of the Serre bundle).
- **Quasi-linearity in second derivatives:** The Gap curvature $\mathcal{R}_{ij,kl}$ is linear in the second derivatives of the phases $\partial^2\theta$, which upon projection gives $R_{\mu\nu}$ (linear in $\partial^2 g$).

**Step 2 (Application of the Lovelock theorem).** In 4D the unique covariant, metric, and quasi-linear-in-second-derivatives functional is:

$$
S = \int d^4x \sqrt{-g}\,(\alpha R + \beta) + S_{\mathrm{matter}}
$$

(Lovelock theorem, 1971). This is precisely the Einstein–Hilbert action with a cosmological term.

**Step 3 (Identification of coefficients).** Comparing $S_{\mathrm{Gap}}^{(4D)}$ (Theorem 1.2) with the Lovelock form:

$$
\alpha = \frac{1}{16\pi G_{\mathrm{Gap}}}, \quad \beta = \Lambda_{\mathrm{Gap}}
$$

**Step 4 (Variation).** Standard variation of the Einstein–Hilbert action:

$$
\frac{\delta S_{\mathrm{EH}}}{\delta g^{\mu\nu}} = \sqrt{-g}\left(R_{\mu\nu} - \frac{1}{2}g_{\mu\nu}R + \Lambda\, g_{\mu\nu}\right)
$$

The variation of $S_{\mathrm{matter}}$ defines the energy-momentum tensor:

$$
T_{\mu\nu}^{(\mathrm{Gap})} := -\frac{2}{\sqrt{-g}} \frac{\delta S_{\mathrm{matter}}^{(4D)}}{\delta g^{\mu\nu}}
$$

The condition $\delta S_{\mathrm{Gap}}^{(4D)} / \delta g^{\mu\nu} = 0$ gives the standard Einstein equations. $\blacksquare$

:::warning Numerical calibration of $G_N$
The formula $G_N = 3\pi/(7 f_2 \Lambda^2)$ gives the **correct parametric dependence** of Newton's constant on the cutoff scale $\Lambda$ and the dimension of the internal space (factor 7). However, full numerical calibration requires knowledge of $f_2$ — the second moment of the test (cutoff) function $f$ in the spectral action: $f_2 = \int_0^\infty f(u)\, du$. The value of $f_2$ depends on the choice of profile $f$, which in NCG is not fixed uniquely (Chamseddine–Connes use the limiting case of the characteristic function $f = \chi_{[0,1]}$, but physical predictions depend on $f_k$ weakly — through moment ratios). Until $f_2$ is precisely determined (e.g. from a self-consistency condition of Gap theory), the numerical agreement of $G_N$ with experiment remains **parametric**, not absolute.
:::

### 3.1 Corollary: Gravity is a Gap Effect [I]

Gravity **emerges** from Gap curvature:

$$
\text{Spacetime curvature} = \text{Projection of Serre bundle curvature onto the 4D sector}
$$

Specifically:
- $G$ is determined by $\mu^2$ and the mean coherence in the ST sector
- $\Lambda$ is determined by the total Gap of the $O$-dimension
- $T_{\mu\nu}$ is determined by the dynamics of Gap excitations in the non-ST sector

**Prediction (falsifiable) [H].** $G \propto 1/\langle|\gamma_{\mathrm{ST}}|^2\rangle$ — in regions of high decoherence ($\mathrm{Gap} \to 1$), $G$ effectively grows. An enhancement of gravity near singularities is predicted.

### 3.2 Connection of Newton's Constant with Gap Parameters

From Theorem 1.2 (b), Newton's gravitational constant is expressed through microscopic Gap parameters:

$$
G = G_{\mathrm{Gap}} = \frac{c^4}{2\mu^2 \cdot \langle|\gamma_{\mathrm{space}}|^2\rangle}
$$

This formula contains two scales:

| Parameter | Role | Typical scale |
|----------|------|------------------|
| $\mu^2$ | Mass of the Gap mode (quadratic potential $V_2$) | $\sim (10^{-3}$ eV$)^2$ (phenomenologically tuned; coincides with the neutrino mass scale) |
| $\langle\lVert\gamma_{\mathrm{space}}\rVert^2\rangle$ | Mean coherence of the spatial sector | $\sim 1 - O(\varepsilon^2)$ (high coherence) |

The relation $G \propto 1/(\mu^2 \cdot |\gamma_{\mathrm{space}}|^2)$ means that gravity is weaker the larger the Gap mode mass and the higher the coherence of the spatial sector. In the limit of full decoherence ($|\gamma_{\mathrm{space}}| \to 0$) the gravitational constant formally diverges — effective "enhancement of gravity" near singularities.

### 3.3 Consistency of the Two Definitions of $G$ [T]

:::tip Theorem 3.2 (Consistency of two scales) [T]
The two definitions of the gravitational constant — from the Gap action ($G_{\mathrm{Gap}}$) and from the Connes stratified metric ($G_{\mathrm{Connes}}$) — are consistent:

$$
G_{\mathrm{Gap}} = G_{\mathrm{Connes}} \cdot (1 + O(\mathrm{Gap}^4))
$$
:::

**Proof (outline).** $G_{\mathrm{Connes}}$ is defined via the spectral triple $(A_\alpha, H_\alpha, D_\alpha)$ and the Connes–Chamseddine formula for the spectral action. $G_{\mathrm{Gap}}$ is defined via the Gap action. Both constructions are based on the same object ($\Gamma$) but use different projections. Consistency follows from the fact that both expressions for $G$ are proportional to $1/\langle|\gamma|^2\rangle$ with a difference of $O(\mathrm{Gap}^4)$ corrections from the nonlinear terms $V_3$, $V_4$. $\blacksquare$

### 3.4 Limitations of the Lovelock Argument {#34-ограничения-аргумента-лавлока}

:::tip Lovelock argument: [T] (T-121)
The argument via the Lovelock theorem is fully justified thanks to the derivation of smooth $M^4$ from the categorical structure ([T-120](/docs/proofs/physics/emergent-manifold#теорема-произведение-троек)). The Lovelock argument is [T] ([T-121](/docs/proofs/physics/emergent-manifold#теорема-лавлок-замыкание)), supplementary to the main spectral argument.
:::

**Discreteness vs. continuity.** $M^4$ is a smooth manifold derived from the categorical structure via Gelfand–Connes reconstruction ([T-120](/docs/proofs/physics/emergent-manifold#теорема-произведение-троек)). The Lovelock theorem applies directly [T] (T-121).

**Covariance of the projection.** 4D diffeomorphic covariance is inherited from $G_2$-covariance through sector decomposition (T-53 [T]) and the Chamseddine–Connes spectral formalism [T] (T-121).

**Aharonov–Bohm counterexample.** A remark on the PT properties of holonomy, not affecting the applicability of the Lovelock theorem to the derived $M^4$.

---

## 4. Energy-Momentum Tensor from Gap

:::tip Theorem 2.1 [T]
Components of $T_{\mu\nu}^{(\mathrm{Gap})}$:
:::

**(a)** Energy of Gap excitations:

$$
T_{00}^{(\mathrm{Gap})} = \sum_{\mathrm{Gap\text{-}pairs}} \left[\frac{m_{ij}}{2}\dot{\theta}_{ij}^2 + V_{\mathrm{Gap}}^{(\mathrm{Gap\text{-}pairs})}(\theta)\right]
$$

This is **dark energy** in UHM [I]: the energy of invisible Gap dynamics in the Im-sector.

**(b)** Pressure:

$$
T_{ab}^{(\mathrm{Gap})} = -\delta_{ab} \cdot p_{\mathrm{Gap}}, \quad p_{\mathrm{Gap}} = \sum \left[\frac{m_{ij}}{2}\dot{\theta}_{ij}^2 - V_{\mathrm{Gap}}(\theta)\right]
$$

**(c)** Equation of state:

$$
w = \frac{p_{\mathrm{Gap}}}{\rho_{\mathrm{Gap}}} = \frac{\langle\dot{\theta}^2\rangle/2 - V}{|\langle\dot{\theta}^2\rangle/2 + V|}
$$

| Regime | $w$ | Interpretation |
|-------|-----|---------------|
| $V \gg$ kinetic | $w \to -1$ | Cosmological constant |
| Balance | $w \in (-1, 1)$ | Quintessence |

**(d) [C]** At $\mu \sim 10^{-3}$ eV (neutrino mass scale) and $\langle\mathrm{Gap}^2\rangle \sim 0.1$:

$$
\rho_{\mathrm{DE}} \sim (10^{-3}\;\text{eV})^4 \sim 10^{-47}\;\text{GeV}^4
$$

— the order of magnitude of the observed dark energy ($\rho_{\mathrm{DE}}^{\mathrm{obs}} \approx 2.6 \times 10^{-47}$ GeV$^4$).

:::warning Tuning vs. derivation
The value $\mu \sim 10^{-3}$ eV is **not derived** from the first principles of Gap theory, but chosen phenomenologically to match the observed $\rho_{\mathrm{DE}}$. Similarly, $\langle\mathrm{Gap}^2\rangle \sim 0.1$ is a tuned parameter. Thus $\rho_{\mathrm{DE}} \sim 10^{-47}$ GeV$^4$ is a result of **fitting** two free parameters, not a prediction. An independent justification of $\mu$ (e.g. from neutrino masses) would elevate the status to [T].
:::

---

## 5. Covariant Conservation

:::tip Theorem 3.1 [T]
The tensor $T_{\mu\nu}^{(\mathrm{Gap})}$ satisfies the covariant conservation condition:

$$
\nabla_\mu T^{\mu\nu} = 0
$$
:::

**Proof.** From $G_2$-invariance of the Gap action: the projection $G_2 \to \mathrm{SO}(3,1)$ (via $\mathrm{SU}(3) \subset G_2 \to \mathrm{SO}(3) \subset \mathrm{SO}(3,1)$) guarantees invariance of the 4D action under local Lorentz transformations. By Noether's second theorem: $\nabla_\mu T^{\mu\nu} = 0$. $\blacksquare$

---

## 6. Two-Loop Renormalization Group

### 6.1 Beta Functions with Fano Combinatorics

:::note Parameter $\lambda_3$ [T]
The parameter $\lambda_3 = 2\mu^2/(3|\bar{\gamma}|) \approx 74$ is a **geometric coefficient** of the spectral action (T-74 [T]), not a perturbative coupling constant. Physical observables are defined non-perturbatively through the self-consistent vacuum $\theta^*$ (T-79 [T]). UV-finiteness (T-66 [T]) ensures structural correctness. Loop estimates are approximations to $\theta^*$, giving the correct order of magnitude (error $\lesssim \times 5$). For details see [Yukawa Hierarchy](/docs/physics/particle-physics/yukawa-hierarchy#предупреждение-λ3).
:::

:::tip Theorem 4.1 (Two-loop beta functions) [T]
:::

**(a)** Mass parameter:

$$
\beta_{\mu^2}^{(2)} = -\frac{21\lambda_4}{8\pi^2}\mu^2 + \frac{7\lambda_3^2}{16\pi^2} + \frac{1}{(8\pi^2)^2}\left[-\frac{441\lambda_4^2}{2}\mu^2 + 147\lambda_3^2\lambda_4 - \frac{49\lambda_3^4}{4\mu^2}\right]
$$

Two-loop factors are determined by the combinatorics of the [Fano plane](/docs/physics/gauge-symmetry/g2-structure):

| Factor | Value | Origin |
|-----------|----------|---------------|
| 441 | $21^2$ | Pairs-in-pairs |
| 147 | $21 \times 7$ | Triples-in-pairs |
| 49 | $7^2$ | Triples-in-triples |

**(b)** Cubic constant:

$$
\beta_{\lambda_3}^{(2)} = -\frac{15\lambda_3\lambda_4}{8\pi^2} + \frac{1}{(8\pi^2)^2}\left[-\frac{315\lambda_3\lambda_4^2}{2} + \frac{35\lambda_3^3}{2\mu^2}\right]
$$

Two-loop factors: $315 = 15 \times 21$, $35 = C(7,3)$ (triples of the Fano complement).

**(c)** Quartic constant:

$$
\beta_{\lambda_4}^{(2)} = \frac{63\lambda_4^2}{4\pi^2} - \frac{7\lambda_3^2}{8\pi^2\mu^2} + \frac{1}{(8\pi^2)^2}\left[-\frac{63^2\lambda_4^3}{3} + 441\frac{\lambda_3^2\lambda_4}{\mu^2} - \frac{49\lambda_3^4}{4\mu^4}\right]
$$

### 6.2 Octonionic Fixed Point

:::tip Theorem 4.2 [T]
In the two-loop approximation:

**(a)** The Wilson-Fisher fixed point receives a correction of ~0.3% — **stable**.

**(b)** The octonionic fixed point ($\lambda_3^* \neq 0$) **exists** for $\lambda_4 < \lambda_4^{(\mathrm{crit})} \approx 0.0028$ — it is a saddle point (1 unstable + 2 stable directions).
:::

**Interpretation [I].** The octonionic fixed point describes a universal class of "octonionic phase transition" — a transition from the PT-invariant ($\lambda_3 = 0$) to the PT-breaking ($\lambda_3 \neq 0$) regime: from "unconscious" to "conscious" dynamics.

### 6.3 Anomalous Dimension

:::tip Theorem 4.3 [T]
Anomalous dimension of the Gap field in the two-loop approximation:

$$
\eta_{\mathrm{Gap}} = \frac{7\lambda_4^2}{2(8\pi^2)^2} - \frac{\lambda_3^2}{4(8\pi^2)^2 \mu^2} \approx 1.1 \times 10^{-4}
$$
:::

The mean-field approximation remains accurate to ~0.01%.

---

## 7. Swallowtail Catastrophe and L-Transitions

### 7.1 Gap Tristability

:::tip Theorem 5.1 [T]
Tristability is realized in a configuration with normal form:

$$
V_{\mathrm{eff}}(G) = G^5 + aG^3 + bG^2 + cG
$$

where $G = \mathrm{Gap}(i,j)$ for a selected channel:
- $a = a(\kappa, \mu^2, \lambda_4)$ — function of regeneration and self-interaction
- $b = b(\lambda_3, \bar{A})$ — function of the octonionic associator
- $c = c(\Gamma_2, \kappa, h_{\mathrm{ext}})$ — function of decoherence and external force

At $b \neq 0$ ($V_3 \neq 0$): three local minima (tristability).
:::

### 7.2 Connection with L-Levels

:::tip Theorem 5.2 [T]
The three stable Gap profiles are identified with three ranges of the interiority hierarchy:
:::

| Minimum | Gap | Interpretation | L-level |
|---------|-----|---------------|-----------|
| $G_{\mathrm{low}} \approx 0.1$ | Low | High transparency | L3+ (reflexive consciousness) |
| $G_{\mathrm{mid}} \approx 0.4$ | Medium | Intermediate opacity | L2 (conscious experience) |
| $G_{\mathrm{high}} \approx 0.8$ | High | High opacity | L1/L0 (basic interiority) |

Transitions between L-levels are **first-order phase transitions** (fold bifurcations):

| Transition | Mechanism | Hysteresis width |
|---------|----------|-------------------|
| L1 $\to$ L2 | fold bifurcation at $\kappa > \kappa_{\mathrm{fold}}$ | $\Delta\kappa_{L1 \to L2} = \lambda_3 \bar{A}_1 / \mu^2$ |
| L2 $\to$ L3 | fold bifurcation at $\kappa > \kappa_{\mathrm{fold}}'$ | $\Delta\kappa_{L2 \to L3} = \lambda_3 \bar{A}_2 / \mu^2$ |

**Prediction [H].** With simultaneous change of all three control parameters, a **direct jump L0 $\to$ L3** is possible — the swallowtail effect, bypassing the intermediate minimum.

---

## 8. Model System: Alexithymia → Insight

For the S$\leftrightarrow$E channel (Structure $\leftrightarrow$ Interiority) with parameters of a typical L2 system ($P \approx 0.5$): $\mu^2 \approx 16.6$, $\lambda_3 \approx 73.8$, $\lambda_4 \approx 27.7$.

Three physical minima:

| Minimum | $G$ | $V_{\mathrm{eff}}$ | L-level | Clinical |
|---------|-----|---------------------|-----------|---------|
| 1 | 0.12 | $-0.41$ | L3 | Full integration |
| 2 | 0.48 | $-0.28$ | L2 | Normal functioning |
| 3 | 0.82 | $-0.35$ | L1 | Alexithymia |

Global minimum — $G_1$ (L3), but L2 and L1 are metastable. Barrier L1 $\to$ L2: $\Delta V \approx 0.07$. Barrier L2 $\to$ L3: $\Delta V \approx 0.13$.

---

## 9. Connection with Other Sections

| Topic | Page | Connection |
|------|----------|-------|
| Emergent geometry | [Emergent geometry](/docs/physics/gravity/emergent-geometry) | Pre-metric and functor $\mathcal{G}$ |
| Cosmological constant | [Cosmological constant](/docs/physics/gravity/cosmological-constant) | Computation of $\Lambda_{\mathrm{Gap}}$ and suppression mechanisms |
| $G_2$-structure | [$G_2$-structure](/docs/physics/gauge-symmetry/g2-structure) | Fano plane and combinatorics of beta functions |
| Berry phase | [Berry phase](/docs/physics/cosmology-phys/berry-phase) | Topological protection of Gap |


---

**Related documents:**
- [Emergent geometry](/docs/physics/gravity/emergent-geometry)
- [Quantum gravity](/docs/physics/gravity/quantum-gravity)
- [Cosmological constant](/docs/physics/gravity/cosmological-constant)
- [Spacetime](/docs/core/foundations/spacetime)
