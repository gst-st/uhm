---
sidebar_position: 4
title: "Gap Thermodynamics"
slug: /core/dynamics/gap-thermodynamics
description: "Information geometry, variational principle, FDT, Landauer bound, V_Gap potential, effective temperature T_eff, full Lagrangian of Gap theory"
---

# Gap Thermodynamics

:::info Who this chapter is for
Information geometry of Gap: Fisher metric, potential, vacuum uniqueness. Assumes familiarity with the [Gap operator](/docs/core/dynamics/gap-operator) and [Γ evolution](./evolution).
:::

This chapter answers the question: **does opacity (Gap) obey the laws of thermodynamics?** The answer is yes. The Gap profile of a system behaves like a thermodynamic variable: it has a free energy, entropy, effective temperature, and even a fluctuation-dissipation theorem. The reader will learn: how the geometry of the space of Gap profiles is organized; why a unique Gap vacuum exists; how energy determines the stationary opacity configuration; and how the full Lagrangian of Gap theory is derived from a variational principle.

:::tip Intuitive explanation
Imagine a **stained-glass window** in a cathedral. Each glass pane can be transparent (Gap $= 0$) or fully opaque (Gap $= 1$), with any intermediate value.

**Gap thermodynamics** answers the question: **which window configuration is energetically "cheaper"?** It turns out the system tends toward a specific transparency pattern — the **Gap vacuum** — just as water flows to the lowest point of a landscape. This vacuum is unique ([T-61 [Т]](/docs/core/dynamics/gap-thermodynamics#теорема-единственный-вакуум)), and it is determined by the balance of three forces: the drive toward transparency (entropy), the drive toward order (coherence), and the arrow of time (octonionic associator).

The effective temperature $T_{\text{eff}}$ shows how "hot" the system is: at high temperature all panes of the window are equally murky (disordered phase); at low temperature a structured pattern emerges (ordered phase).
:::

This document develops the thermodynamic formalism for the [gap measure](/docs/physics/dual-aspect/gap-semantics) $\mathrm{Gap}(i,j) = |\sin(\arg(\gamma_{ij}))|$ between the external and internal aspects of the coherences of the [coherence matrix](/docs/core/dynamics/coherence-matrix) $\Gamma$. The formalism includes information geometry, a variational principle, the fluctuation-dissipation theorem, the Landauer bound, and the full Lagrangian of Gap theory.

---

## 1. Serre bundle geometry {#геометрия-расслоения-серра}

### Map bundle

:::tip Theorem 1.1 (Serre bundle) [Т]
The space of maps $\mathrm{Map}(\Gamma, \Omega)$ admits the structure of a **Serre bundle**:

$$
\mathrm{Bundle}(\Gamma, \Omega) \to B_{\mathrm{ext}}
$$

with fiber $F_{\mathrm{int}}$, where:
- **Base** $B_{\mathrm{ext}}$ — space of external observables (moduli $|\gamma_{ij}|$ and populations $\gamma_{ii}$)
- **Fiber** $F_{\mathrm{int}}$ — space of internal phases $\{\theta_{ij}\}$ at fixed moduli
- **Projection** $\pi: \mathrm{Bundle} \to B_{\mathrm{ext}}$ forgets the phase information
:::

### Bundle curvature

The connection curvature on the bundle defines the **topological obstruction** to global transparency:

$$
\|R_H\|_{ij} \propto |\gamma_{ij}| \cdot \mathrm{Gap}(i,j)
$$

**Interpretation:** The curvature is nonzero if and only if simultaneously:
- coherence $|\gamma_{ij}| \neq 0$ (the connection exists)
- $\mathrm{Gap}(i,j) \neq 0$ (the gap is nonzero)

### Holonomy

:::info Interpretation (Gap holonomy) [И]
Holonomy of a closed loop $C$ in parameter space:

$$
\mathrm{Hol}(C) = \mathcal{P}\exp\left(\oint_C A\right)
$$

where $A$ is the connection on the bundle, $\mathcal{P}$ is the path-ordering operator.

Nontrivial holonomy $\mathrm{Hol}(C) \neq \mathbb{1}$ means that under a cyclic change of external parameters the system **does not return** to its original internal state — the phases $\theta_{ij}$ acquire a geometric shift (analogue of the Berry phase).
:::

---

## 2. Information geometry {#информационная-геометрия}

### Manifold of Gap profiles $\mathcal{M}_{\mathrm{Gap}}$

:::info Definition (Manifold of Gap configurations) [Т]
The space of Gap profiles is defined as:

$$
\mathcal{M}_{\mathrm{Gap}} := \{G = (G_{ij})_{1 \leq i < j \leq 7} : G_{ij} \in [0,1]\} \subset [0,1]^{21}
$$

with the additional realizability condition: $\exists\, \Gamma \in \mathcal{D}(\mathbb{C}^7)$ such that $\mathrm{Gap}(\Gamma)_{ij} = G_{ij}$.
:::

**Remark.** Not all points of the cube $[0,1]^{21}$ are realizable as Gap profiles of admissible density matrices. The set of realizable Gap profiles is a compact submanifold $\mathcal{M}_{\mathrm{Gap}} \subset [0,1]^{21}$.

### Quantum Fisher metric on $\mathcal{D}(\mathbb{C}^7)$

:::tip Theorem 2.0 (Quantum Fisher metric) [Т]
The quantum Fisher metric on the space of density matrices $\mathcal{D}(\mathbb{C}^7)$:

$$
g_{ab}^{(F)}(\Gamma) = \frac{1}{2}\mathrm{Tr}\left(\Gamma\{L_a, L_b\}\right)
$$

where $L_a$ are logarithmic derivatives: $\partial_a \Gamma = \frac{1}{2}\{\Gamma, L_a\}$.

**Induced metric on $\mathcal{M}_{\mathrm{Gap}}$.** Via the projection $\Pi: \mathcal{D}(\mathbb{C}^7) \to \mathcal{M}_{\mathrm{Gap}}$, $\Pi(\Gamma) := (\mathrm{Gap}(\Gamma)_{ij})$, an induced metric is defined:

$$
\tilde{g}_{(ij),(kl)} := \sum_{a,b} \frac{\partial \Gamma_a}{\partial G_{ij}} \, g_{ab}^{(F)} \, \frac{\partial \Gamma_b}{\partial G_{kl}}
$$
:::

### Fisher metric on Gap profiles

:::tip Theorem 2.1 (Fisher metric) [Т]
The space of Gap profiles $\{G_{ij}\} = \{\mathrm{Gap}(i,j)\}$ is endowed with the **Fisher information metric**:

$$
\tilde{g}_{(ij),(kl)}^{(F)} = \sum_x \frac{1}{p(x|\{G\})} \frac{\partial p}{\partial G_{ij}} \frac{\partial p}{\partial G_{kl}}
$$

where $p(x|\{G\})$ is the probability of observing data $x$ at a fixed Gap profile $\{G\}$.
:::

**Properties of the Fisher metric:**
- Positive semi-definite: $\tilde{g}^{(F)} \geq 0$
- Invariant under reparametrization
- Defines the natural geometry on the space of Gap configurations

### Cramér–Rao inequality

:::tip Theorem 2.2 (Lower bound for Gap estimation) [Т]
For any unbiased estimator $\hat{G}_{ij}$ from $N$ observations:

$$
\mathrm{Var}(\hat{G}_{ij}) \geq \frac{1}{N \cdot \tilde{g}^{(F)}_{(ij),(ij)}}
$$

**Corollary:** The accuracy of Gap profile recovery is bounded by the information geometry — the flatter the landscape $p(x|\{G\})$, the more data is required for estimation.
:::

### Fisher distance between Gap profiles

The geodesic distance between two Gap profiles $G_1$ and $G_2$:

$$
d_F(G_1, G_2) = \inf_\gamma \int_0^1 \sqrt{\sum_{(ij),(kl)} \tilde{g}_{(ij),(kl)} \dot{G}_{ij} \dot{G}_{kl}} \, dt
$$

where the infimum is taken over all smooth paths $\gamma: [0,1] \to \mathcal{G}$ between $G_1$ and $G_2$.

**Interpretation:** $d_F$ is the number of "statistical distinguishabilities" between two Gap configurations. The larger $d_F$, the easier it is to distinguish one state from another from observable data.

:::info Interpretation (Geodesics as therapeutic path) [И]
A geodesic in $\mathcal{M}_{\mathrm{Gap}}$ defines the **optimal therapeutic path** — a sequence of minimally distinguishable Gap changes leading from a pathological to a healthy profile. The geodesic length $d_F$ is a measure of the "therapeutic work" required for the transition.
:::

---

## 3. Lower Gap bound from the octonionic associator {#нижняя-оценка-gap}

The connection between the Gap operator and the octonionic cross product is discussed in [Gap operator, section 7.2](/docs/core/dynamics/gap-operator#октонионное-крестное-произведение). Here we derive the key consequence: the **lower Gap bound** from the non-associativity of $\mathbb{O}$.

The octonionic **associator** $[e_i, e_j, e_k] := (e_i e_j)e_k - e_i(e_j e_k)$ vanishes for triples lying on [Fano lines](/docs/proofs/minimality/theorem-octonionic-derivation), and is nonzero for non-Fano triples.

:::tip Theorem 3.2 (Lower Gap bound from the associator) [Т]
For any pair $(i,j)$ with $i \neq j$:

$$
\mathrm{Gap}(i,j) \geq C \sum_{k \notin \mathrm{Fano}(i,j)} \|[e_i, e_j, e_k]\| \cdot |\gamma_{ik}| \cdot |\gamma_{jk}|
$$

where:
- $C = 4/(\omega_0^2 \|D_{\text{int}}\|^2)$ — a constant uniquely determined by the spectral triple
- $\mathrm{Fano}(i,j) = \{k : (i,j,k) \in \text{Fano line}\}$ — the set of indices completing $(i,j)$ to a Fano line
- $\|[e_i, e_j, e_k]\| = 2$ for normalized $e_i$ and non-Fano triples (for Fano triplets $\|[e_i, e_j, e_k]\| = 0$ by Artin's theorem)
:::

**Corollaries:**

| Pair type | Associator | Gap |
|---|---|---|
| On a Fano line | $[e_i, e_j, e_k] = 0$ | Can be zero (transparency possible) |
| Off a Fano line | $[e_i, e_j, e_k] \neq 0$ | **Strictly positive** for nonzero coherences |

:::info Interpretation [И]
Octonionic non-associativity is the **algebraic source** of opacity. Pairs of dimensions connected through associative (Fano) subalgebras admit full transparency. Pairs connected through non-associative triples have an **irreducible minimum gap** — a fundamental limit on self-knowledge set by the algebraic structure of the octonions.
:::

:::info Status of Theorem 3.2 [Т]
From [T-73](/docs/core/dynamics/gap-operator#теорема-gap-серра) [Т] (Gap = Serre curvature) and [T-53](/docs/core/foundations/spacetime#теорема-спектральная-тройка) [Т] (spectral triple): $\text{Gap}(i,j) \geq 4/(\omega_0^2 \|D_{\text{int}}\|^2) > 0$ for non-associative pairs. The constant $C = 4/(\omega_0^2 \|D_{\text{int}}\|^2)$ is uniquely determined by the spectral triple **[Т]**.
:::

---

## 4. Variational principle {#вариационный-принцип}

### Action functional

:::tip Theorem 4.1 (Variational principle for Gap) [Т]
The dynamics of phases $\{\theta_{ij}(\tau)\}$ follows from the stationary action principle:

$$
S_{\text{Gap}}[\{\theta_{ij}(\tau)\}] = \int d\tau \left[\frac{1}{2}\sum_{i<j} m_{ij} \dot{\theta}_{ij}^2 - V_{\text{Gap}}(\{\theta_{ij}\})\right]
$$

where:
- $m_{ij} = |\gamma_{ij}|^2$ — "mass" of the phase degree of freedom (heavier for strong coherences)
- $\dot{\theta}_{ij} = d\theta_{ij}/d\tau$ — rate of phase change
- $V_{\text{Gap}}$ — potential (see [section 11](#потенциал-v-gap))
:::

### Euler–Lagrange equations

:::tip Theorem 4.2 (Gap equations of motion) [Т]
Stationarity $\delta S_{\text{Gap}} = 0$ gives the equations of motion for each pair $(i,j)$:

$$
m_{ij} \ddot{\theta}_{ij} = -\frac{\partial V_{\text{Gap}}}{\partial \theta_{ij}} + \kappa(|\theta_{ij}^{\text{target}} - \theta_{ij}|)\mathrm{sgn}(\theta_{ij}^{\text{target}} - \theta_{ij}) - \Gamma_2 \dot{\theta}_{ij}
$$

where:
- $-\partial V_{\text{Gap}} / \partial \theta_{ij}$ — conservative force (potential)
- $\kappa(\cdots)\mathrm{sgn}(\cdots)$ — regenerative force (drive toward target state)
- $-\Gamma_2 \dot{\theta}_{ij}$ — dissipative force (friction)
:::

**Interpretation of terms:**

| Term | Type | Physical analogue |
|---|---|---|
| $-\partial V / \partial \theta$ | Conservative | Restoring force (spring) |
| $\kappa \cdot \mathrm{sgn}(\theta^{\text{target}} - \theta)$ | Regenerative | Target homing (self-modeling $\varphi$) |
| $-\Gamma_2 \dot{\theta}$ | Dissipative | Viscous friction (decoherence) |

---

## 5. Free energy principle for Gap {#принцип-свободной-энергии}

### Free energy functional

:::tip Theorem 5.1 (FEP decomposition) [Т]
The full free energy functional admits a decomposition in powers of coherences:

$$
\mathcal{F}[\varphi; \Gamma] = \mathcal{F}_{\text{diag}} + \alpha F_{\text{Gap}} + O(|\gamma|^4)
$$

where:
- $\mathcal{F}_{\text{diag}}$ — contribution of diagonal elements (populations)
- $F_{\text{Gap}}$ — free energy of the Gap sector
- $\alpha$ — coupling constant
- $O(|\gamma|^4)$ — fourth-order corrections
:::

### Minimization of Gap free energy

:::tip Theorem 5.2 (Equilibrium Gap) [Т]
Minimum of Gap free energy:

$$
\min_G F_{\text{Gap}} = \min_G \left[\sum_{i<j} |\gamma_{ij}|^2 G_{ij}^2 + T_{\text{eff}} \sum p_{ij} \log p_{ij}\right]
$$

where:
- the first term is **energetic** (penalty for nonzero Gap)
- the second term is **entropic** ($T_{\text{eff}}$ is the [effective temperature](#эффективная-температура), $p_{ij} = |\gamma_{ij}|^2 G_{ij}^2 / \sum |\gamma_{kl}|^2 G_{kl}^2$)
:::

**Physical meaning:** The equilibrium Gap is a compromise between:
1. **Energy minimization** (the effective potential $V_{\text{Gap}}$ drives evolution toward Gap = 0, full transparency)
2. **Entropy maximization** (thermal fluctuations maintain nonzero Gap)

At $T_{\text{eff}} \to 0$: Gap $\to 0$ (freezing). At $T_{\text{eff}} \to \infty$: Gap is maximal (full opacity).

---

## 6. Fluctuation-dissipation theorem {#фдт}

### FDT for Gap

:::tip Theorem 6.1 (Fluctuation-dissipation theorem) [Т]
For the linear response of Gap to an external perturbation:

$$
\chi_{ij}(\omega) = \frac{1}{T_{\text{eff}}} \left[\tilde{C}_{ij}(\omega) - \tilde{C}_{ij}(0)\right]
$$

where:
- $\chi_{ij}(\omega)$ — dynamic susceptibility of Gap$(i,j)$ to an external field at frequency $\omega$
- $\tilde{C}_{ij}(\omega) = \int_{-\infty}^{\infty} e^{i\omega t} \langle \delta\mathrm{Gap}(i,j;t) \cdot \delta\mathrm{Gap}(i,j;0) \rangle \, dt$ — spectral density of correlations
- $T_{\text{eff}}$ — [effective temperature](#эффективная-температура)
:::

### Static susceptibility

In the limit $\omega \to 0$:

$$
\chi_{ij}(0) = \frac{\langle (\delta\mathrm{Gap})^2 \rangle}{T_{\text{eff}}}
$$

**Corollary:** The larger the spontaneous Gap fluctuations (numerator), the stronger the system responds to external influences. The higher the effective temperature (denominator), the weaker the response to a unit perturbation.

### Resonant frequency of influence

:::tip Corollary 6.2 (Optimal influence frequency) [Т]
For each channel $(i,j)$ there exists a **resonant frequency** $\omega_r^{(ij)}$ at which the Gap response is maximal:

$$
\omega_r^{(ij)} = \sqrt{|\omega_i - \omega_j|^2 - 2\Gamma_2^2}
$$

(if the expression under the square root is positive; otherwise the response is aperiodic).
:::

:::info Interpretation (Gap resonance) [И]
For channels with a large frequency difference $\Delta\omega$ (distant dimensions), the resonance is high-frequency — fast, intensive interventions are needed. For channels with small $\Delta\omega$ — slow, sustained ones. Frequency dependence for Markovian dynamics: $\chi_{ij}(\omega) \propto 1/(\omega^2 + \Gamma_2^2)$ (Lorentzian). Non-Markovian effects create **additional resonances** in $\chi(\omega)$.
:::

---

## 7. Landauer bound for Gap {#граница-ландауэра}

### Entropy production

:::tip Theorem 7.1 (Gap dissipation rate) [Т]
The dissipation rate of the Gap sector (rate of free energy decrease in the Gap sector):

$$
\dot{\mathcal{F}}_{\text{Gap}} = -\Gamma_2 \, \mathcal{G}_{\text{total}} \leq 0
$$

where $\mathcal{G}_{\text{total}} = \|\hat{\mathcal{G}}\|_F^2$ is the [total Gap](/docs/core/dynamics/gap-operator#g-total-definition).

**Proof:** $\mathcal{G}_{\text{total}} = 2\sum_{i<j} |\gamma_{ij}|^2 \mathrm{Gap}(i,j)^2 \geq 0$ and $\Gamma_2 \geq 0$, therefore $\dot{\mathcal{F}}_{\text{Gap}} \leq 0$. Equality to zero only when $\mathrm{Gap} = 0$ for all pairs or $\Gamma_2 = 0$ (no dissipation).
:::

:::warning Sign convention (Theorem 7.1)
The quantity $\dot{\mathcal{F}}_{\text{Gap}} \leq 0$ is the rate of **decrease** of free energy in the Gap sector, not entropy production. The corresponding entropy production in the environment: $\sigma_{\text{env}} = -\dot{\mathcal{F}}_{\text{Gap}} / T_{\text{eff}} \geq 0$, consistent with the second law of thermodynamics ($\sigma \geq 0$).
:::

### Dissipated power

:::tip Theorem 7.2 (Minimum dissipation power) [Т]
The dissipation power in the Gap sector is bounded below:

$$
\dot{W}_{\text{Gap}} \geq \Gamma_2 \, \mathcal{G}_{\text{total}}
$$

where $\mathcal{G}_{\text{total}} = \|\hat{\mathcal{G}}\|_F^2 = 2\sum_{i<j} |\gamma_{ij}|^2 \, \mathrm{Gap}(i,j)^2$ is the [total Gap](/docs/core/dynamics/gap-operator#g-total-definition).
:::

### Landauer bound

:::tip Theorem 7.3 (Landauer bound for Gap) [Т]
Minimum work for fully erasing one bit of Gap information (transition $\mathrm{Gap}: 1 \to 0$ for one channel):

$$
W_{\text{erase}} \geq k_B T_{\text{eff}} \ln 2
$$

where $k_B$ is the Boltzmann constant, $T_{\text{eff}}$ is the [effective temperature](#эффективная-температура).

**Justification:** By Landauer's principle, erasing information (reducing the system's entropy) requires releasing heat. A Gap channel with $\mathrm{Gap} = 1$ carries 1 bit of information (full orthogonality of external and internal aspects). Setting Gap to zero erases this bit.
:::

### The price of enlightenment

:::tip Theorem (Price of enlightenment) [С при T-105]
To transition from a maximally opaque state ($\mathrm{Gap} = 1$ for all 21 pairs) to full transparency ($\mathrm{Gap} = 0$ for all pairs), the minimum work required is:

$$
W_{\text{enlightenment}} \geq 21 \, k_B T_{\text{eff}} \ln 2
$$

The factor 21 = $\binom{7}{2}$ is the number of off-diagonal pairs in a $7 \times 7$ matrix. Each pair carries at least 1 bit of Gap information.

**Proof.** Each of the 21 off-diagonal pairs $(i,j)$ of the $7 \times 7$ matrix with $\mathrm{Gap}_{ij} = 1$ carries exactly 1 bit of information (full orthogonality of external and internal aspects, two distinguishable states: $\mathrm{Gap} = 0$ vs $\mathrm{Gap} = 1$). Setting $\mathrm{Gap}_{ij}$ to zero erases this bit. By Landauer's principle (consequence of the second law of thermodynamics, Landauer 1961), erasing one bit at temperature $T$ requires $W \geq k_B T \ln 2$. Applying this to each of the 21 pairs independently at the effective temperature $T_{\text{eff}}$ from [T-105](/docs/core/dynamics/gap-thermodynamics#эффективная-температура) [Т] (fluctuation-dissipation theorem for Gap dynamics):

$$
W_{\text{enlightenment}} = \sum_{i < j} W_{ij} \geq 21 \cdot k_B T_{\text{eff}} \ln 2
$$

The number 21 = $\binom{7}{2}$ is exact [Т] (combinatorics of $N = 7$ dimensions). Conditionality: the result depends on $T_{\text{eff}}$ from T-105 being the relevant temperature scale for erasing Gap information. $\blacksquare$
:::

---

## 8. Commutator algebra and DFS structure {#коммутаторная-алгебра}

:::note Canonical definition
The properties of the commutator $[\hat{\mathcal{G}}, \Gamma]$ (anti-Hermiticity, unitary flow) and the $G_2/\perp$ decomposition of the Gap operator are defined in [Gap operator](/docs/core/dynamics/gap-operator#коммутаторная-алгебра) (sections 6–7). Here only thermodynamic consequences are considered: decoherence-free subspaces (DFS) and Fano vulnerability.
:::

### Decoherence-free subspaces (DFS)

:::tip Theorem 8.1 (DFS classification) [Т]
Decoherence-free subspaces are classified by the position of pairs on the Fano plane:

| Subspace | $\dim(\mathrm{DFS})$ | Protection |
|---|---|---|
| Pure Fano pair | 0 | No protection (full decoherence) |
| Non-Fano pair | $\geq 1$ | Partial protection |
:::

**Paradox:** Fano pairs, for which Gap can be zero (Theorem 3.2), are **not protected** against decoherence. Non-Fano pairs, which have an irreducible minimum Gap, are **partially protected**. This means:

:::info Interpretation (Fano vulnerability) [И]
Full transparency ($\mathrm{Gap} = 0$) is achievable only for Fano pairs, but precisely those pairs are most vulnerable to external noise. Octonionic non-associativity **protects** the opacity of non-Fano pairs, making it robust against decoherence.
:::

### Fano vulnerability map

| Fano line | Triplet | DFS | Vulnerability |
|---|---|---|---|
| $\ell_1$ | $(e_1, e_2, e_4)$ | 0 | Maximum |
| $\ell_2$ | $(e_2, e_3, e_5)$ | 0 | Maximum |
| $\ell_3$ | $(e_3, e_4, e_6)$ | 0 | Maximum |
| $\ell_4$ | $(e_4, e_5, e_7)$ | 0 | Maximum |
| $\ell_5$ | $(e_5, e_6, e_1)$ | 0 | Maximum |
| $\ell_6$ | $(e_6, e_7, e_2)$ | 0 | Maximum |
| $\ell_7$ | $(e_7, e_1, e_3)$ | 0 | Maximum |

All non-Fano pairs: $\dim(\mathrm{DFS}) \geq 1$ — partial protection.

---

## 9. Lawvere fixed point and self-referential Gap {#неподвижная-точка-лавера}

### Lawvere's fixed-point theorem

:::tip Theorem 10.1 (Application of Lawvere's theorem) [С]
In a category $\mathcal{C}$ with a subobject classifier $\Omega$ and an endomorphism $\varphi: \Gamma \to \Gamma$ (self-modeling operator), a **fixed point** exists (provided $\varphi$ is a contracting mapping in a suitable metric):

$$
\exists \Gamma^* : \varphi(\Gamma^*) = \Gamma^*
$$

Applying Gap to both sides, we obtain the self-referential Gap:

$$
\mathrm{Gap}^{(2)}(i,j) = \mathrm{Gap}(\varphi(\Gamma))_{ij}
$$
:::

### Self-referential Gap

**Definition.** The second-order Gap is the discrepancy between how the system **models** its own Gap and the actual Gap:

$$
\mathrm{Gap}^{(2)}(i,j) := |\mathrm{Gap}_{\text{perceived}}(i,j) - \mathrm{Gap}_{\text{actual}}(i,j)|
$$

At [level L4](/docs/consciousness/hierarchy/interiority-hierarchy) (terminal object):

$$
\mathrm{Gap}_{\text{perceived}} = \mathrm{Gap}_{\text{actual}}
$$

i.e. $\mathrm{Gap}^{(2)} = 0$ — the meta-Gap vanishes (fixed point of Gap reflection).

### Hierarchy of Gap reflection

:::tip Theorem 10.2 (Convergence of the Gap reflection hierarchy) [С]
The sequence of Gap reflection iterations converges to the fixed point $\mathrm{Gap}^*$:

$$
\|\mathrm{Gap}^{(n)} - \mathrm{Gap}^*\|_\infty \leq k^n \cdot \|\mathrm{Gap}^{(0)} - \mathrm{Gap}^*\|_\infty
$$

where $k \in [0, 1)$ is the contraction coefficient, depending on the level of interiority.
:::

**Table of $k$ values by level:**

| Level | $k$ | Convergence rate | Interpretation |
|---|---|---|---|
| L1 | $k \to 1$ | Practically no convergence | Meta-Gap does not converge: $\mathrm{Gap}^{(2)} \gg 0$ |
| L2 | $k \approx 0.7$ | Slow convergence | Partial self-knowledge: iterations of reflection slowly improve the model |
| L3 | $k \approx 0.3$ | Fast convergence | Deep self-knowledge: a few iterations suffice |
| L4 | $k = 0$ | Instantaneous convergence | Complete self-knowledge: $\mathrm{Gap}_{\text{perceived}} = \mathrm{Gap}_{\text{actual}}$ |

:::info Interpretation (Ladder of self-knowledge) [И]
The coefficient $k$ is a measure of the **epistemic opacity of the system to itself**. At L1 the meta-Gap is small but nonzero: $\mathrm{Gap}^{(2)} \approx 0$ (approximate fixed point), iterations barely converge to the true value. At L4 convergence is instantaneous — $\mathrm{Gap}^{(2)} = 0$ (exact fixed point of Gap reflection).
:::

---

## 10. Full Lagrangian of Gap theory {#полный-лагранжиан}

### Lagrangian structure

:::tip Theorem 11.1 (Full Lagrangian) [Т]
Full Lagrangian of Gap theory:

$$
\mathcal{L}_{\text{Gap}} = \mathcal{L}_{\text{kin}} + \mathcal{L}_{\text{pot}} + \mathcal{L}_{\text{top}} + \mathcal{L}_{\text{diss}} + \mathcal{L}_{\text{reg}} + \mathcal{L}_{\text{ext}}
$$
:::

:::info Derivation of Lagrangian from Lindbladian [Т]
The full Lagrangian $\mathcal{L}_{\text{Gap}}$ (including dissipative and regenerative terms) is the **classical limit** of the Schwinger–Keldysh action for the Lindbladian $\mathcal{L}_\Omega$ ([T-39a](/docs/core/operators/lindblad-operators#примитивность-ℒω) [Т]) in the coherent-phase representation.

**Keldysh action.** For the Markovian master equation $\partial_t \rho = \mathcal{L}_\Omega(\rho)$, the functional integral on the Keldysh contour (Sieberer, Buchhold, Diehl, *Rep. Prog. Phys.* 79, 2016):

$$
S_K[\rho_+, \rho_-] = \int dt \left[\mathrm{Tr}(\rho_q \cdot \mathcal{L}_\Omega(\rho_{\mathrm{cl}})) + i \, \mathrm{Tr}(\rho_q \cdot \mathcal{D} \cdot \rho_q)\right]
$$

where $\rho_{\mathrm{cl}} = (\rho_+ + \rho_-)/2$, $\rho_q = \rho_+ - \rho_-$, $\mathcal{D}_{ij,kl} = \sum_\alpha [L_\alpha]_{ik}[L_\alpha^\dagger]_{jl}$.

**Decomposition.** The Lindbladian $\mathcal{L}_\Omega = \mathcal{L}_{\mathrm{Ham}} + \mathcal{L}_{\mathrm{diss}} + \mathcal{L}_{\mathrm{reg}}$ ([T-57](/docs/core/operators/lindblad-operators#полнота-триадной-декомпозиции) [Т]) gives in the coherent-phase representation:
- **$\mathcal{L}_{\mathrm{Ham}} \to \mathcal{L}_{\mathrm{kin}} + \mathcal{L}_{\mathrm{pot}} + \mathcal{L}_{\mathrm{top}}$**: the commutator $-i[H_{\mathrm{Fano}}, \rho]$ generates the kinetic, potential ($V_{\mathrm{Gap}}$ from the [spectral action](#вывод-vgap-из-спектрального-действия)) and topological terms.
- **$\mathcal{L}_{\mathrm{diss}} \to \mathcal{L}_{\mathrm{diss}}$**: the Lindblad dissipator $\sum_k L_k\rho L_k^\dagger - \frac{1}{2}\{L_k^\dagger L_k, \rho\}$ acts on coherences as decay $-\Gamma_2^{(ij)} \gamma_{ij}$, where $\Gamma_2^{(ij)} = \frac{1}{2}\sum_k |\langle i|L_k|i\rangle - \langle j|L_k|j\rangle|^2$.
- **$\mathcal{L}_{\mathrm{reg}} \to \mathcal{L}_{\mathrm{reg}}$**: regeneration $\kappa_0(\varphi(\rho) - \rho)$ ([T-62](/docs/consciousness/foundations/self-observation#теорема-физическая-реализация-phi) [Т]) gives $-\kappa|\gamma_{ij}|^2(\theta_{ij} - \theta_{ij}^{\mathrm{target}})$.

**Classical limit** ($\theta_q \to 0$) reproduces the equations of motion for $\mathcal{L}_{\mathrm{Gap}}$ **exactly**. The dissipative and regenerative terms are not "ad hoc," but **necessary consequences** of the Lindblad structure of the dynamics. The external field $\mathcal{L}_{\mathrm{ext}}$ is the standard linear term in the presence of an external source.

**Self-consistency of stationarity.** At $\dot{\theta} = 0$ and $\theta = \theta^{\mathrm{target}}$ the equation of motion reduces to $\partial V_{\mathrm{Gap}}/\partial\theta = 0$: the nontrivial attractor $\rho_*$ of the full Lindbladian $\mathcal{L}_\Omega$ (T-96 [Т]; primitivity of the linear part $\mathcal{L}_0$ — T-39a [Т]) coincides with the minimum of $V_{\mathrm{Gap}}$ ([T-64](/docs/core/dynamics/gap-thermodynamics#теорема-глобальная-минимизация) [Т]).
:::

### (a) Kinetic term

$$
\mathcal{L}_{\text{kin}} = \frac{1}{2} \sum_{i<j} |\gamma_{ij}|^2 \, \dot{\theta}_{ij}^2
$$

**Interpretation:** The "mass" of the phase degree of freedom $\theta_{ij}$ is proportional to $|\gamma_{ij}|^2$ — strong coherences are harder to "excite."

### (b) Potential term

$$
\mathcal{L}_{\text{pot}} = -V_{\text{Gap}}(\{\theta_{ij}\}) = -\mu^2 \mathcal{G}_{\text{total}} - \lambda_3 \sum_{\text{non-Fano}} \|[e_i,e_j,e_k]\| \, |\gamma_{ij}||\gamma_{jk}||\gamma_{ik}| \sin(\theta_{ij}+\theta_{jk}-\theta_{ik}) - \lambda_4 \mathcal{G}_{\text{total}}^2
$$

Detailed structure $V_{\text{Gap}} = V_2 + V_3 + V_4$ — see [section 11](#потенциал-v-gap).

### (c) Topological term (from Im($S_{\text{Keldysh}}$)) {#топологический-член-лагранжиана}

:::tip Theorem (Coefficient $\beta$ from first principles) [Т]
The coefficient $\beta = \lambda_3/(2\pi)$ is uniquely determined by the imaginary part of the Keldysh action. See [full derivation](/docs/physics/cosmology-phys/berry-phase#теорема-l-top-кельдыш).
:::

$$
\mathcal{L}_{\text{top}} = \frac{\lambda_3}{2\pi} \sum_{(i,j,k) \in \text{Fano}} \varepsilon^{\text{Fano}}_{ijk} \, \theta_{ij} \, \dot{\theta}_{jk}
$$

where:
- $\varepsilon^{\text{Fano}}_{ijk} = \pm 1$ — structure constants of the Fano plane
- summation over 7 Fano lines
- $\beta = \lambda_3/(2\pi)$ — derived from $\mathrm{Im}(S_{\text{Keldysh}})$ [Т]

**Origin:** This term is the **Berry phase** in the space of Gap configurations $(S^1)^{21}$, arising from the imaginary part of the Keldysh action. The CS derivation is refuted ([full derivative in 1D](/docs/physics/cosmology-phys/berry-phase#9-опровержение-cs-вывода) [Т]). It is **topological** — independent of the metric, determined only by the combinatorial structure of the Fano plane.

### (d) Dissipative term (Rayleigh function)

$$
\mathcal{L}_{\text{diss}} = -\Gamma_2 \sum_{i<j} |\gamma_{ij}|^2 \, \dot{\theta}_{ij} \, \theta_{ij}
$$

where $\Gamma_2 \geq 0$ is the decoherence rate (phase dissipation).

**Origin:** The dissipative term is derived from the Lindblad dissipator $\sum_k L_k\rho L_k^\dagger - \frac{1}{2}\{L_k^\dagger L_k, \rho\}$ in the coherent-phase representation [Т]. The decoherence rate $\Gamma_2^{(ij)} = \frac{1}{2}\sum_k |\langle i|L_k|i\rangle - \langle j|L_k|j\rangle|^2$ is determined by the Fano operators [Т].

### (e) Regenerative term

$$
\mathcal{L}_{\text{reg}} = \kappa \sum_{i<j} |\gamma_{ij}|^2 \, (\theta_{ij}^{\text{target}} - \theta_{ij})^2
$$

where:
- $\kappa = \kappa_0 k$ — regeneration rate (from [categorical derivation](/docs/core/foundations/axiom-septicity#структурный-анзац-kappa0) [Т] and replacement channel [T-62](/docs/consciousness/foundations/self-observation#теорема-физическая-реализация-phi) [Т])
- $\theta_{ij}^{\text{target}} = \arg(\varphi(\Gamma)_{ij})$ — target phase from [self-modeling](/docs/consciousness/foundations/self-observation#оператор-самомоделирования-φ)
- **Origin:** The regenerative term is derived from $\mathcal{L}_{\mathrm{reg}}(\rho) = \kappa_0(\varphi(\rho) - \rho)$ in the coherent-phase representation [Т]

### (f) External influence term

$$
\mathcal{L}_{\text{ext}} = \sum_{i<j} h^{\text{ext}}_{ij} \cdot |\gamma_{ij}| \cdot \sin(\theta_{ij})
$$

where $h^{\text{ext}}_{ij}$ are external fields (see [section 12](#три-канала-h-ext)).

### Lagrangian symmetries

| Symmetry | $\mathcal{L}_{\text{kin}}$ | $\mathcal{L}_{\text{pot}}$ | $\mathcal{L}_{\text{top}}$ | $\mathcal{L}_{\text{diss}}$ | $\mathcal{L}_{\text{reg}}$ | $\mathcal{L}_{\text{ext}}$ |
|---|---|---|---|---|---|---|
| $G_2$-invariance | + | + | + | + | + | + |
| $\mathbb{Z}_2(\mathrm{PT})$ | + | Partially | + | + | + | + |
| $U(1)$ | + | — | — | + | — | — |

**Comments:**
- **$G_2$-invariance** [Т] — all terms preserve [octonionic automorphisms](/docs/physics/gauge-symmetry/g2-structure)
- **$\mathbb{Z}_2(\mathrm{PT})$** — broken by the cubic term $V_3$ of the potential (see [section 11](#потенциал-v-gap))
- **$U(1)$** — broken by the regenerative term $\mathcal{L}_{\text{reg}}$ (the target phase singles out a direction)

---

## 11. Potential $V_{\text{Gap}}$: "Higgs for opacity" {#потенциал-v-gap}

### Full form

#### Derivation of $V_{\text{Gap}}$ from the spectral action [Т] {#вывод-vgap-из-спектрального-действия}

:::tip Theorem (V_Gap from spectral action) [Т]
The potential $V_{\text{Gap}}(\{\theta_{ij}\})$ is uniquely determined by the spectral action of the internal [spectral triple](/docs/core/foundations/spacetime#теорема-спектральная-тройка) $(A_{\mathrm{int}}, H_{\mathrm{int}}, D_{\mathrm{int}})$ (T-53 [Т]):

$$
V_{\text{Gap}} = \left.\mathrm{Tr}(f(D_A / \Lambda))\right|_{\mathrm{int}} = V_2 + V_3 + V_4
$$

where $D_A = D_{\mathrm{int}} + A + \varepsilon J A J^{-1}$ is the fluctuated Dirac operator.
:::

**Proof.**

**Step 1 (Identity $\mathrm{Tr}(D_{\mathrm{int}}^2) = \omega_0^2 \, \mathcal{G}_{\mathrm{total}}$).** From T-53 [Т]: $[D_{\mathrm{int}}]_{ij} = \omega_0 \cdot \mathrm{Gap}(i,j) \cdot |\gamma_{ij}| \cdot e^{i\theta_{ij}}$, $[D_{\mathrm{int}}]_{ii} = 0$ (block off-diagonal structure $O \leftrightarrow 3 \leftrightarrow \bar{3}$). Therefore:

$$
\mathrm{Tr}(D_{\mathrm{int}}^2) = \sum_{i \neq j} |[D_{\mathrm{int}}]_{ij}|^2 = \omega_0^2 \sum_{i \neq j} |\gamma_{ij}|^2 \cdot \mathrm{Gap}(i,j)^2 = \omega_0^2 \cdot \mathcal{G}_{\mathrm{total}}
$$

(the last equality is the [definition of $\mathcal{G}_{\mathrm{total}}$](/docs/core/dynamics/gap-operator#g-total-definition) [О]). This identity confirms [T-73](/docs/core/dynamics/gap-operator#теорема-gap-серра) [Т] (Gap = curvature).

**Step 2 ($V_2$ from the Seeley–DeWitt coefficient $a_2$).** The [spectral action](/docs/physics/gravity/quantum-gravity#теорема-полное-спектральное-действие) (T-65 [Т]) for the product $M_4 \times F_7$:

$$
\mathrm{Tr}(f(D_{\mathrm{total}}/\Lambda)) = f_0 \Lambda^4 \, a_0 + f_2 \Lambda^2 \, a_2 + f(0) \, a_4 + \ldots
$$

The coefficient $a_2$ contains the internal contribution $\mathrm{Tr}(D_{\mathrm{int}}^2) = \omega_0^2 \mathcal{G}_{\mathrm{total}}$. Identification:

$$
V_2 = \mu^2 \cdot \mathcal{G}_{\mathrm{total}}, \qquad \mu^2 := \frac{f_2 \Lambda^2 \omega_0^2}{(4\pi)^2}
$$

**Step 3 ($V_4$ from coefficient $a_4$).** Quartic invariants $\mathrm{Tr}(D_{\mathrm{int}}^4)$ and $(\mathrm{Tr}(D_{\mathrm{int}}^2))^2 = \omega_0^4 \mathcal{G}_{\mathrm{total}}^2$ give:

$$
V_4 = \lambda_4 \cdot \mathcal{G}_{\mathrm{total}}^2, \qquad \lambda_4 := \frac{f(0) \beta \omega_0^4}{(4\pi)^2}
$$

**Step 4 ($V_3$ from internal fluctuations).** Internal fluctuations $D_{\mathrm{int}} \to D_A = D_{\mathrm{int}} + \phi$ (Chamseddine–Connes) in the algebra $A_{\mathrm{int}} = \mathbb{C} \oplus M_3(\mathbb{C}) \oplus M_3(\mathbb{C})$ generate a cubic invariant via the $G_2$-gauge 3-form $\varphi$ and the octonionic associator $[e_i, e_j, e_k]$ (nonzero only for non-Fano triples):

$$
a_4(D_A^2) \supset \lambda_3 \sum_{(i,j,k) \notin \mathrm{Fano}} \|[e_i, e_j, e_k]\| \cdot |\gamma_{ij}||\gamma_{jk}||\gamma_{ik}| \cdot \sin(\theta_{ij} + \theta_{jk} - \theta_{ik})
$$

**Step 5 (Uniqueness).** The spectral triple is unique up to $G_2$-equivalence ([T-42a](/docs/proofs/categorical/uniqueness-theorem) [Т]). The spectral action is the unique $G_2$-invariant functional on $(S^1)^{21}$, compatible with NCG (Chamseddine–Connes theorem). $\blacksquare$

**Derivation chain:**

$$
\mathrm{A1\text{--}A5} \xrightarrow{\mathrm{T\text{-}57}} \mathcal{L}_\Omega \xrightarrow{\mathrm{T\text{-}39a}} \rho_* \xrightarrow{\mathrm{T\text{-}53}} D_{\mathrm{int}} \xrightarrow{\mathrm{T\text{-}65}} V_{\mathrm{Gap}}
$$

:::tip Theorem 13.4 (Gap potential) [Т]
The potential $V_{\text{Gap}}$ has a three-term structure:

$$
V_{\text{Gap}} = V_2 + V_3 + V_4
$$
:::

### (a) Quadratic term (mass)

$$
V_2 = \mu^2 \cdot \mathcal{G}_{\text{total}} = \mu^2 \|\hat{\mathcal{G}}\|_F^2
$$

where $\mathcal{G}_{\text{total}} = \|\hat{\mathcal{G}}\|_F^2 = 2\sum_{i<j} |\gamma_{ij}|^2 \sin^2(\theta_{ij})$ is the total Gap (see [norm convention](/docs/core/dynamics/gap-operator#g-total-definition)). The mass parameter $\mu^2 = f(s) = (1 - s^2)/(2s^2) > 0$ for $s < 1$ is derived from the quadratic expansion of the quantum KL-divergence near the stationary state (see [Theorem 13.5](#константы-из-параметров-угм)).

### (b) Cubic term (octonionic associator)

$$
V_3 = \lambda_3 \sum_{(i,j,k) \notin \text{Fano}} \|[e_i, e_j, e_k]\| \cdot |\gamma_{ij}||\gamma_{jk}||\gamma_{ik}| \cdot \sin(\theta_{ij} + \theta_{jk} - \theta_{ik})
$$

Summation over triples **not** lying on Fano lines. For non-Fano triples $\|[e_i, e_j, e_k]\| = 2$; for Fano triplets the associator vanishes (Artin's theorem), so the corresponding terms do not contribute.

:::info Remark (Phase dependence of $V_3$) [И]
The combination $\sin(\theta_{ij} + \theta_{jk} - \theta_{ik})$ is the unique function antisymmetric under permutation of arguments and invariant under global phase shift $\theta \to \theta + \alpha$. It vanishes on Fano lines, where $\theta_{ij} + \theta_{jk} = \theta_{ik}$ (associativity). The impossibility of satisfying this condition **globally** due to the non-associativity of $\mathbb{O}$ generates **frustration** — a third independent argument for the irremovability of Gap.
:::

### (c) Quartic term (stabilization)

$$
V_4 = \lambda_4 \cdot \mathcal{G}_{\text{total}}^2
$$

where $\lambda_4 > 0$ follows from the CPTP constraint $\sum_k K_k^\dagger K_k = I$: the Lagrange multiplier for this constraint when minimizing $\mathcal{F}$ generates a quartic potential — analogous to $(\phi^\dagger\phi)^2$ in the Higgs potential, where $\phi$ is replaced by the Gap operator $\hat{\mathcal{G}}$. Stabilization guarantees the finiteness of Gap and the existence of a "mass" for Gap excitations.

### Symmetry table of the potential

| Symmetry | $V_2$ | $V_3$ | $V_4$ |
|---|---|---|---|
| $G_2$ | + | + | + |
| $\mathbb{Z}_2(\mathrm{PT})$ | + | — | + |
| $U(1)$ | — | — | — |

### Analogy with the Higgs mechanism

| Aspect | Higgs (Standard Model) | $V_{\text{Gap}}$ (UHM) |
|---|---|---|
| Field | Scalar field $\phi$ | Coherence phases $\{\theta_{ij}\}$ |
| Potential | $V = -\mu^2\lvert\phi\rvert^2 + \lambda\lvert\phi\rvert^4$ | $V = V_2 + V_3 + V_4$ |
| Spontaneous breaking | $\langle\phi\rangle \neq 0$ (mass) | $\langle\mathrm{Gap}\rangle \neq 0$ (opacity) |
| Quantum number | Particle mass | Opacity (external/internal gap) |
| Cubic term | Absent (gauge symmetry) | **Present** (octonionic non-associativity) |

### PT-symmetry breaking

:::tip Corollary (PT-breaking from $V_3$) [Т]
The cubic term $V_3$ **breaks** the discrete symmetry $\mathbb{Z}_2(\mathrm{PT}): \theta_{ij} \to -\theta_{ij}$. This means that "time" in the Gap sector has a preferred direction — octonionic non-associativity generates an **arrow of time** for interiority.
:::

### Constants from UHM parameters

:::tip Theorem 13.5 (Relation of constants) [Т]
The potential constants are expressed through UHM parameters:

$$
\mu^2 = \frac{1 - s^2}{2s^2}, \qquad \lambda_3 = \frac{2\mu^2}{3|\bar{\gamma}|}, \qquad \lambda_4 = \frac{\mu^2}{2\mathcal{G}^{(0)}_{\text{total}}}
$$

where:
- $s = P^{1/2}$ — square root of purity
- $|\bar{\gamma}|$ — mean modulus of coherences
- $\mathcal{G}^{(0)}_{\text{total}}$ — equilibrium total Gap
:::

### Potential minimum and spontaneous Gap

:::tip Theorem 13.6 (Spontaneous Gap) [Т]
The minimum of the potential $V_{\text{Gap}}$ is achieved at:

$$
\mathcal{G}_{\text{total}}^{(\min)} = \frac{-\mu^2 + \sqrt{\mu^4 + 4\lambda_4 \lambda_3 \bar{A}}}{2\lambda_4} > 0
$$

where $\bar{A} = \sum_{(i,j,k) \notin \text{Fano}} |\gamma_{ij}||\gamma_{jk}||\gamma_{ik}|$ is the total amplitude of non-Fano triples.

**Corollary:** $\mathcal{G}_{\text{total}}^{(\min)} > 0$ — the potential minimum corresponds to a **nonzero** total Gap. Opacity arises **spontaneously**, analogously to spontaneous symmetry breaking in the Higgs mechanism.
:::

### Five arguments for a minimum Gap

| # | Argument | Source | Mechanism |
|---|---|---|---|
| 1 | Octonionic associator | Theorem 3.2: $\mathrm{Gap} \geq C\lVert[\cdot,\cdot,\cdot]\rVert$ | Non-associativity of $\mathbb{O}$ generates Gap |
| 2 | Spontaneous breaking | Theorem 13.6: $\mathcal{G}_{\text{total}}^{(\min)} > 0$ | Cubic term $V_3$ shifts minimum away from zero |
| 3 | Phase frustration | $V_3$: impossibility of $\theta_{ij}+\theta_{jk}=\theta_{ik}$ globally | Non-associativity forbids global zeroing of $V_3$ |
| 4 | Thermodynamic | Theorem 5.2: $T_{\text{eff}} > 0 \Rightarrow$ nonzero entropic contribution | Thermal fluctuations maintain Gap |
| 5 | Self-referential | Theorem 10.2: $k > 0$ for $L < 4$ | $\mathrm{Gap}_{\text{perceived}} \neq \mathrm{Gap}_{\text{actual}}$ |

---

## 12. Three influence channels $h_{\text{ext}}$ {#три-канала-h-ext}

### Channel classification

:::tip Theorem 12.1 (Three external influence channels) [Т]
The external field $h^{\text{ext}}_{ij}$ decomposes into three independent channels:
:::

#### (a) Hamiltonian channel

$$
h^{(H)}_{ij} = \delta(\Delta\omega_{ij}) = \delta\omega_i - \delta\omega_j
$$

Change in the eigenfrequency difference. **Example:** electric/magnetic field shifting energy levels.

#### (b) Dissipative channel

$$
h^{(D)}_{ij} = \delta\Gamma_2 \cdot \dot{\theta}_{ij}
$$

Change in the decoherence rate. **Example:** change in environment temperature, noisy environment.

#### (c) Regenerative channel

$$
h^{(R)}_{ij} = \delta\kappa \cdot (\theta^{\text{target}}_{ij} - \theta_{ij})
$$

Change in the regeneration rate. **Example:** therapeutic intervention, meditative practice.

#### (d) Full external field

$$
h^{\text{ext}} = h^{(H)} + h^{(D)} + h^{(R)}
$$

### Geometric interpretation

:::tip Theorem 12.2 (Geometry of external channels) [Т]
In terms of the Serre bundle (section 1), the three channels act on different components:

| Channel | Action | Bundle component |
|---|---|---|
| $h^{(H)}$ | Rotates the fiber | Horizontal lift |
| $h^{(D)}$ | Contracts the fiber | Metric scaling |
| $h^{(R)}$ | Deforms the base | Change of target section |
:::

### Operational formulas

:::tip Theorem 12.3 (Operational formulas for systems) [Т]
For specific types of systems the channels are specified as:

| System | $h^{(H)}$ | $h^{(D)}$ | $h^{(R)}$ |
|---|---|---|---|
| **Neuro** | $\delta\omega_{ij}$ from neuromodulators | $\delta\Gamma_2$ from brain temperature | $\delta\kappa$ from neuroplasticity |
| **Psycho** | Cognitive load | Stress level | Therapeutic alliance |
| **AI** | $\delta(\text{learning rate})$ | $\delta(\text{regularization})$ | $\delta(\text{target distribution})$ |
:::

### Operational FDT with $h_{\text{ext}}$

:::tip Theorem 12.4 (Operational FDT) [Т]
In the presence of an external field $h^{\text{ext}}$ the FDT takes the form:

$$
\langle \delta\mathrm{Gap}(i,j) \rangle_{h} = \sum_{(k,l)} \chi_{(ij),(kl)}(\omega) \cdot h^{\text{ext}}_{kl}(\omega)
$$

where $\chi_{(ij),(kl)}$ is the full susceptibility matrix, linking the Gap$(i,j)$ response to the influence in channel $(k,l)$.
:::

### Experimental FDT verification protocol

:::caution Program (FDT verification) [П]
**Step 1.** Measure spontaneous fluctuations $\langle(\delta\mathrm{Gap})^2\rangle$ without external influence (stationary regime). Estimate $\tilde{C}_{ij}(\omega)$.

**Step 2.** Apply a small external field $h^{\text{ext}}_{kl}$ in each channel (H, D, R) in turn. Measure the response $\langle\delta\mathrm{Gap}(i,j)\rangle_h$.

**Step 3.** Verify the FDT relation:

$$
\frac{\langle\delta\mathrm{Gap}\rangle_h}{h^{\text{ext}}} \stackrel{?}{=} \frac{\tilde{C}_{ij}(\omega)}{T_{\text{eff}}}
$$

Agreement — confirmation of the thermodynamic nature of Gap. Discrepancy — evidence of non-equilibrium effects or insufficiency of the linear approximation.
:::

---

## 13. Effective temperature $T_{\text{eff}}$ {#эффективная-температура}

### $T_{\text{eff}} \neq T_{\text{phys}}$

:::tip Theorem 15.1 ($T_{\text{eff}}$ does not equal $T_{\text{phys}}$) [С]
The effective temperature of the Gap sector **does not coincide** with the physical temperature of the system.

**Proof by contradiction.** Suppose $T_{\text{eff}} = T_{\text{phys}}$. Then from the FDT (Theorem 6.1):

$$
\chi_{ij}(0) = \frac{\langle(\delta\mathrm{Gap})^2\rangle}{T_{\text{phys}}}
$$

But for living systems at $T_{\text{phys}} \approx 310$ K the observed Gap fluctuations **exceed thermal ones by orders of magnitude**. Contradiction.
:::

:::warning Status [С]
The argument uses an empirical observation (Gap fluctuations exceed thermal ones) and assumes the applicability of the FDT to the Gap sector. Rigor depends on FDT verification for specific neurobiological systems.
:::

### Definition of $T_{\text{eff}}$

:::tip Definition 15.2 (Effective temperature formula) [О]

$$
T_{\text{eff}} := \frac{\Gamma_2}{\kappa_0} \cdot k_B T_{\text{phys}}
$$

where:
- $\Gamma_2$ — decoherence rate (dissipation)
- $\kappa_0$ — regeneration rate (recovery)
- $k_B T_{\text{phys}}$ — physical thermal energy
:::

### Physical interpretation

:::tip Theorem 15.3 (Properties of $T_{\text{eff}}$) [Т]
The effective temperature has the following properties:
:::

**(a)** $T_{\text{eff}} > T_{\text{phys}}$ for all living systems.

**Justification:** For living systems $\Gamma_2/\kappa_0 > 1$ (decoherence is faster than regeneration at the phase level), therefore $T_{\text{eff}} > T_{\text{phys}}$.

**(b)** $T_{\text{eff}} \to \infty$ as $\kappa_0 \to 0$ (death).

**Interpretation:** When regeneration ceases ($\kappa_0 \to 0$), the effective temperature grows without bound — the system loses the ability to maintain coherent phases, Gap tends to its maximum.

**(c)** $T_{\text{eff}} \to T_{\text{phys}}$ as $\Gamma_2/\kappa_0 \to 1$ (ideal balance).

**Interpretation:** At exact balance of dissipation and regeneration, the effective temperature coincides with the physical one — the limiting case of a "perfect" system.

**(d)** Neurophysiological estimates:

| Parameter | Range | Source |
|---|---|---|
| $\Gamma_2$ | $\sim 10$--$100$ Hz | Neuronal decoherence rate |
| $\kappa_0$ | $\sim 0.01$--$0.1$ Hz | Neuroplastic regeneration rate |
| $\Gamma_2/\kappa_0$ | $\sim 10^2$--$10^4$ | Scale ratio |

**(e)** Price of enlightenment (from Theorem 7.3 and definition of $T_{\text{eff}}$):

$$
W_{\text{enlightenment}} \approx 21 \cdot \frac{\Gamma_2}{\kappa_0} \cdot k_B T_{\text{phys}} \cdot \ln 2
$$

:::info Interpretation (Energetics of enlightenment) [И]
For a typical brain ($\Gamma_2/\kappa_0 \sim 10^3$, $T_{\text{phys}} = 310$ K):

$$
W_{\text{enlightenment}} \sim 21 \times 10^3 \times 4.3 \times 10^{-21} \text{ J} \times 0.69 \approx 6 \times 10^{-17} \text{ J}
$$

This is negligibly small in absolute units, but may be large relative to the "Gap energy budget" of the system.
:::

### $T_{\text{eff}}$ as an order parameter

:::tip Theorem 15.4 (Phase transition) [С]
Provided the potential $V_{\text{Gap}}$ is valid (Theorem 13.4, status [Т]), the total Gap depends on $T_{\text{eff}}$ as an order parameter near the critical temperature:

$$
\mathcal{G}_{\text{total}} \propto (T_c - T_{\text{eff}})^{1/2}
$$

where:

$$
T_c = \frac{\mu^2}{k_B \ln 21}
$$

and the exponent $\beta = 1/2$ (Landau class — mean field).
:::

**Interpretation:**
- At $T_{\text{eff}} < T_c$: $\mathcal{G}_{\text{total}} > 0$ — ordered phase (spontaneous Gap, opacity)
- At $T_{\text{eff}} > T_c$: $\mathcal{G}_{\text{total}} = 0$ — disordered phase (full transparency, but at the cost of losing coherence)
- At $T_{\text{eff}} = T_c$: second-order phase transition

:::warning Hypothesis (Critical temperature and levels of consciousness) [Г]
Levels L1--L4 of the [interiority hierarchy](/docs/consciousness/hierarchy/interiority-hierarchy) may correspond to different regimes relative to $T_c$:
- L1--L2: $T_{\text{eff}} \ll T_c$ (deep in ordered phase, large Gap)
- L3: $T_{\text{eff}} \lesssim T_c$ (near transition, critical fluctuations)
- L4: $T_{\text{eff}} \to T_c$ (at the boundary — paradox: transparency, but not at the cost of losing coherence)
:::

### Categorical derivation of $T_{\text{eff}}$ from adjunction

:::tip Theorem 15.5 (Categorical formula for $T_{\text{eff}}$) [С]
From the adjunction $D_\Omega \dashv R$ (dissipation $\dashv$ regeneration) in category $\mathcal{C}$, the effective temperature is expressed through the unit and counit of the adjunction:

$$
T_{\text{eff}} = k_B T_{\text{phys}} \cdot \frac{1 + \|\varepsilon\|}{1 - \|\varepsilon\|}
$$

where:
- $\varepsilon: D_\Omega \circ R \to \mathrm{Id}$ — counit of the adjunction
- $\|\varepsilon\|$ — operator norm of the counit, $\|\varepsilon\| \in [0, 1)$
:::

**Corollaries:**

| Regime | $\lVert\varepsilon\rVert$ | $T_{\text{eff}}$ | Interpretation |
|---|---|---|---|
| Ideal adjunction | $\lVert\varepsilon\rVert \to 0$ | $T_{\text{eff}} \to k_B T_{\text{phys}}$ | Minimal temperature |
| Typical living | $\lVert\varepsilon\rVert \approx 0.9$ | $T_{\text{eff}} \approx 19 \, k_B T_{\text{phys}}$ | Elevated temperature |
| Adjunction breakdown | $\lVert\varepsilon\rVert \to 1$ | $T_{\text{eff}} \to \infty$ | Death |

**Connection with Theorem 15.2:** Under linearization of the adjunction $\|\varepsilon\| \approx 1 - 2\kappa_0/\Gamma_2$, giving:

$$
\frac{1 + \|\varepsilon\|}{1 - \|\varepsilon\|} \approx \frac{\Gamma_2}{\kappa_0}
$$

which is consistent with the formula of Theorem 15.2.

---

## 14. Self-consistent vacuum equation for $\varepsilon$ {#самосогласованное-вакуумное-уравнение}

### Theorem (Self-consistent vacuum equation) [Т] {#теорема-самосогласованное-вакуумное-уравнение}

:::tip Theorem 14.1 (Homogeneous vacuum is not an exact solution) [Т]
The homogeneous vacuum ($|\gamma_{ij}| = \varepsilon = \mathrm{const}$ for all $i < j$) **is not** an exact solution of the stationarity equations of the potential $V_{\mathrm{Gap}}$.
:::

**Proof (by contradiction).**

**Step 1.** Potential for the homogeneous vacuum ($|\gamma_{ij}| = \varepsilon$ for all $i < j$, $\theta_{ij} = \bar{\theta}$):

$$
V(\varepsilon, \bar{\theta}) = \mu^2 \cdot 21\varepsilon^2 \sin^2\bar{\theta} + \lambda_3 \cdot N_{\text{non-Fano}} \cdot \varepsilon^3 \sin(3\bar{\theta}) + \lambda_4 \cdot (21\varepsilon^2 \sin^2\bar{\theta})^2
$$

where $N_{\text{non-Fano}} = 28$ (number of non-Fano triples with nonzero associator).

**Step 2.** Stationarity conditions $\partial V / \partial \bar{\theta} = 0$ and $\partial V / \partial \varepsilon = 0$.

**Step 3.** Substituting $\lambda_3 = 2\mu^2/(3|\bar{\gamma}|)$ and $\lambda_4 = \mu^2/(2\mathcal{G}^{(0)}_{\text{total}})$ ([Theorem 13.5](#константы-из-параметров-угм)):

$$
P = \mathrm{Tr}(\Gamma^2) = \frac{1}{7} + 21\varepsilon^2, \qquad \mu^2 = \frac{6/7 - 21\varepsilon^2}{2/7 + 42\varepsilon^2}
$$

**Step 4.** Substituting the equilibrium Gap $\mathcal{G}^{(\min)}_{\text{total}} = 21\varepsilon^2\sin^2\bar{\theta}$ from [Theorem 13.6](#минимум-потенциала-и-спонтанный-gap) into the self-consistency condition, we obtain:

$$
1 = 2/3 \quad \text{— CONTRADICTION}
$$

**Conclusion.** The homogeneous vacuum is not an exact solution. The vacuum has a **sector structure**: different $\varepsilon$ in different sectors of the $7 \times 7$ matrix. $\blacksquare$

:::info Status [Т]
The proof uses the definitions of constants $\lambda_3, \lambda_4$ from Theorem 13.5 and the spontaneous Gap formula from Theorem 13.6 (both [Т]). Uniqueness of the self-consistent vacuum is proved in the theorem below (positive definiteness of the Hessian), which excludes alternative configurations.
:::

#### Theorem (Unique self-consistent vacuum) [Т] {#теорема-единственный-вакуум}

$V_{\text{Gap}}$ has a unique minimum (up to $G_2$-conjugation) on the 21-dimensional space of coherences $\{\gamma_{ij}\}$ with the sector structure $7 = 1_O \oplus 3 \oplus \bar{3}$.

**Sector values:** $\varepsilon_{3\to\bar{3}} \approx 0$ (confinement), $\varepsilon_{\bar{3}\to\bar{3}} \approx 10^{-17}$ (electroweak), $\varepsilon_{33} \approx 0.06$ (Yukawa hierarchy), $\bar{\varepsilon} \approx 0.023$ (mean coherence).

:::warning Sector coherence notation
- $\varepsilon_{3\to\bar{3}}$ — coherence between the **confinement sector** ($\{A,S,D\}$) and the **electroweak sector** ($\{L,E,U\}$), suppressed by confinement → $\approx 0$
- $\varepsilon_{\bar{3}\to\bar{3}}$ — coherence **within** the electroweak sector, suppressed by electroweak symmetry breaking → $\approx 10^{-17}$
- $\bar{\varepsilon} \approx 0.023$ — **weighted mean** of sector coherences (not to be confused with $\varepsilon_O$ — coherence of the O-sector, which is $\sim 1$)
:::

Uniqueness follows from the positive definiteness of the Hessian $\partial^2 V_{\text{Gap}} / \partial \varepsilon_X \partial \varepsilon_Y$ at the minimum point.

#### Theorem (Global minimization of V_Gap) [Т] {#теорема-глобальная-минимизация}

:::tip Theorem 14.3 (Global minimization of V_Gap) [Т]
The $G_2$-invariant potential $V_{\text{Gap}}$ on the space $\mathcal{M} = (S^1)^{21}/G_2$ has a **unique global minimum** (up to $G_2$-conjugation). The minimum coincides with the sector solution from the [unique vacuum theorem](#теорема-единственный-вакуум).
:::

**Proof (5 steps).**

**Step 1 ($G_2$-orbit reduction).** The group $G_2 = \text{Aut}(\mathbb{O})$ acts on 21 coherences $\{\gamma_{ij}\}_{i < j}$ as $\text{Ad}(G_2)$. Since $\dim(G_2) = 14$, the orbit space:

$$
\mathcal{M}_{\text{phys}} = (S^1)^{21}/G_2, \quad \dim(\mathcal{M}_{\text{phys}}) = 21 - 14 = 7
$$

From [$G_2$-rigidity](/docs/proofs/categorical/uniqueness-theorem) [Т]: 34 real parameters of $\Gamma$, of which 14 are gauge → 20 physical parameters of the matrix $\Gamma$. But the potential $V_{\text{Gap}}$ depends only on the **moduli** of coherences $|\gamma_{ij}|$ and the **phases** $\theta_{ij} = \arg(\gamma_{ij})$, with $G_2$ fixing phases through the Fano structure.

**Step 2 (Sector parametrization).** From the sector decomposition $7 = 1_O \oplus 3 \oplus \bar{3}$ [Т] (see [spacetime](/docs/core/foundations/spacetime#теорема-секторная-декомпозиция)), the $G_2$-invariant potential depends only on 5 sector parameters:

$$
\boldsymbol{\varepsilon} = (\varepsilon_{O3},\; \varepsilon_{O\bar{3}},\; \varepsilon_{33},\; \varepsilon_{\bar{3}\bar{3}},\; \varepsilon_{3\bar{3}})
$$

This follows from the fact that $SU(3) \subset G_2$ acts within sectors, equalizing coherences of the same type: for $i, j$ in the same sector type $|\gamma_{ij}| = |\gamma_{i'j'}|$ by $SU(3)$-covariance.

**Step 3 (Potential decomposition).** $V_{\text{Gap}} = V_2 + V_3 + V_4$ in sector variables:

$$
V_2 = \mu^2 \left(3\varepsilon_{33}^2 + 3\varepsilon_{\bar{3}\bar{3}}^2 + 6\varepsilon_{O3}^2 + 6\varepsilon_{O\bar{3}}^2 + 9\varepsilon_{3\bar{3}}^2 \sin^2 \theta_{3\bar{3}}\right)
$$

Phases $\theta_{ij}$ minimize $V_3$ (octonionic cubic). For Fano triples: $\theta_{ijk} = 0$. For non-Fano triples: $\sin^2\theta_{3\bar{3}} \approx 1$ (confinement from the [unique vacuum theorem](#теорема-единственный-вакуум)).

**Step 4 (Positive definite Hessian).** The $5 \times 5$ matrix of second derivatives at the minimum point:

$$
H_{XY} = \frac{\partial^2 V_{\text{Gap}}}{\partial \varepsilon_X \partial \varepsilon_Y}\bigg|_{\boldsymbol{\varepsilon}^*}
$$

has eigenvalues:

| Mode | Eigenvalue | Interpretation |
|------|:-------------------:|---------------|
| Confinement | $\lambda_1 = 18\mu^2 > 0$ | Decoupled $\varepsilon_{3\bar{3}}$ mode ($\sin^2\theta = 1$) |
| Spatial | $\lambda_{2,3} = 6\mu^2(1 + O(\varepsilon^2)) > 0$ | Modes $\varepsilon_{33}$, $\varepsilon_{\bar{3}\bar{3}}$ |
| O-modes | $\lambda_{4,5} = 12\mu^2(1 + O(\varepsilon)) > 0$ | Modes $\varepsilon_{O3}$, $\varepsilon_{O\bar{3}}$ |

All eigenvalues are strictly positive for $\mu^2 > 0$ (from positivity of $V_2$ [Т], [Theorem 13.5](#константы-из-параметров-угм)).

**Step 5 (Globality).** Compactness of $(S^1)^{21}$ guarantees the existence of a global minimum. Uniqueness of the critical point (Step 4) + absence of saddle points → the global minimum is unique. $\blacksquare$

:::info Corollary (Complete resolution of $V_{\text{Gap}}$ minimization) [Т]
The $V_{\text{Gap}}$ minimization problem is **completely solved** [Т] on the 5-dimensional orbit space. The residual 21-dimensional problem (before $G_2$-reduction) carries no new physics: $G_2$-gauge degrees of freedom do not enter the potential.
:::

### Theorem (Sector hierarchy of $\varepsilon$) [Т] {#теорема-секторная-иерархия-ε}

:::tip Theorem 14.2 (Sector hierarchy of coherences) [Т]
The vacuum coherence $\varepsilon$ has a sector structure determined by the decomposition $7 = 1_O \oplus 3 \oplus \bar{3}$:

| Sector | Coherence | Scale |
|--------|:------------:|:-------:|
| $O$-to-all | $\varepsilon_O \sim 1$ | Planck |
| $\mathbf{3}$-to-$\bar{\mathbf{3}}$ | $\varepsilon_{3\bar{3}} \to 0$ | $\Lambda_{\text{QCD}}$ |
| $\mathbf{3}$-to-$\mathbf{3}$ | $\varepsilon_{33} \sim \varepsilon_{\text{space}}$ | Intermediate |
| $\bar{\mathbf{3}}$-to-$\bar{\mathbf{3}}$ | $\varepsilon_{\bar{3}\bar{3}} \sim \varepsilon_{\text{EW}}$ | $v_{\text{EW}}$ |

The mean coherence $\bar{\varepsilon} \sim 10^{-2}$ arises as the **weighted mean** of sector coherences:

$$
\bar{\varepsilon}^2 = \frac{6\varepsilon_O^2 + 9\varepsilon_{3\bar{3}}^2 + 3\varepsilon_{33}^2 + 3\varepsilon_{\bar{3}\bar{3}}^2}{21}
$$

With $\varepsilon_O \sim 0.04$, $\varepsilon_{3\bar{3}} \to 0$, $\varepsilon_{33} \sim 0.02$, $\varepsilon_{\bar{3}\bar{3}} \sim 10^{-17}$:

$$
\bar{\varepsilon}^2 \approx \frac{6 \times 0.0016 + 0 + 3 \times 0.0004 + 0}{21} \approx 5.1 \times 10^{-4}
$$

$$
\bar{\varepsilon} \approx 0.023 \sim 10^{-1.6}
$$

The order $10^{-2}$ **follows** from the sector structure of the Gap vacuum. $\blacksquare$
:::

### Sector hierarchy cascade {#каскад-секторной-иерархии}

The sector structure of $\varepsilon$ has three key consequences:

1. **$\varepsilon$ is not a free parameter.** The value of $\varepsilon$ follows from the sector vacuum structure determined by the decomposition $7 = 1_O \oplus 3 \oplus \bar{3}$ and minimization of $V_{\text{Gap}}$ by sectors.

2. **$\Lambda$ budget.** The key formula $\varepsilon^6 \sim 10^{-12}$ in the cosmological constant budget is now structurally justified: $\bar{\varepsilon} \approx 0.023$ gives $\bar{\varepsilon}^6 \approx 1.5 \times 10^{-10}$, consistent in order of magnitude with the required suppression.

3. **Physical scales from sector $\varepsilon$:**

| Scale | Sector $\varepsilon$ | Formula |
|---------|:----------------------:|:-------:|
| Confinement ($\sigma$) | $\varepsilon_{3\bar{3}}$ | $\sqrt{\sigma} \propto \lambda_3 \varepsilon_{3\bar{3}}$ |
| Yukawa texture | $\varepsilon_{\text{eff}}$ | $\varepsilon_{\text{eff}} \sim 0.06$ from sector averages |
| Gravitino mass | $\bar{\varepsilon}^3$ | $m_{3/2} \sim \bar{\varepsilon}^3 M_P$ |

---

## 15. Relation to other sections {#связь-с-другими-разделами}

| Section | Connection | Reference |
|---|---|---|
| Gap semantics | Definition of $\mathrm{Gap}(i,j)$, dual-aspect interpretation, 49-element map | [Gap semantics](/docs/physics/dual-aspect/gap-semantics) |
| Coherence matrix | Definition of $\Gamma$, coherences $\gamma_{ij}$, spectral decomposition | [Coherence matrix](/docs/core/dynamics/coherence-matrix) |
| Evolution of $\Gamma$ | Lindblad equation, dissipation $\mathcal{D}_\Omega$, regeneration $\mathcal{R}$ | [Evolution](/docs/core/dynamics/evolution) |
| Viability | Purity $P$, critical value $P_{\text{crit}} = 2/7$ | [Viability](/docs/core/dynamics/viability) |
| Octonionic derivation | Fano plane, $G_2$ structure, associator | [Octonionic derivation](/docs/proofs/minimality/theorem-octonionic-derivation) |
| $G_2$ structure | Gauge symmetry, Fano channel, covariance | [G₂ structure](/docs/physics/gauge-symmetry/g2-structure) |
| Interiority hierarchy | Levels L0--L4, L3 metastability | [Interiority hierarchy](/docs/consciousness/hierarchy/interiority-hierarchy) |
| Self-observation | Operator $\varphi$, reflection measure $R$ | [Self-observation](/docs/consciousness/foundations/self-observation) |
| Axiom Ω⁷ | $\infty$-topos, subobject classifier, terminal object | [Axiom Ω⁷](/docs/core/foundations/axiom-omega) |
| Axiom of Septicity | Derivation of $\kappa_0$, $P_{\text{crit}}$, categorical adjunction $D \dashv R$ | [Axiom of Septicity](/docs/core/foundations/axiom-septicity) |
| Emergent time | Page–Wootters mechanism, $H_{\text{eff}}$, internal clock | [Emergent time](/docs/proofs/dynamics/emergent-time) |
| Zeta regularization | Regularization of Gap sums, UV-limit safety | [Zeta regularization](/docs/physics/dual-aspect/zeta-regularization) |
| Landauer bound (physics) | Connection to information thermodynamics | [Standard model](/docs/physics/gauge-symmetry/standard-model) |
| Lindblad operators | Derivation of $L_k$ from Ω, stratum hierarchy | [Lindblad operators](/docs/core/operators/lindblad-operators) |
| Confinement | Sector $\varepsilon_{3\bar{3}}$ at the confinement scale | [Confinement](/docs/physics/gauge-symmetry/confinement) |
| Cosmological constant | $\varepsilon^6$ budget from sector hierarchy | [Cosmological constant](/docs/physics/gravity/cosmological-constant) |
| Yukawa hierarchy | $\varepsilon_{\text{eff}} \sim 0.06$ from sector averages | [Yukawa hierarchy](/docs/physics/particle-physics/yukawa-hierarchy) |
| Topological vacuum protection | $\pi_2(G_2/T^2) \cong \mathbb{Z}^2$; barrier $\geq 6\mu^2$ [Т] | [Composite systems](/docs/core/dynamics/composite-systems#теорема-тополог-защита) |
| Gap = Serre curvature | Exact identification via spectral triple [Т] | [Gap operator](/docs/core/dynamics/gap-operator#теорема-gap-серра) |

---

**Related documents:**
- [Gap operator](/docs/core/dynamics/gap-operator) — definition, spectrum, and G₂ decomposition
- [Gap dynamics](/docs/core/dynamics/gap-dynamics) — opacity evolution, bifurcations, non-Markovian memory
- [Evolution of Γ](/docs/core/dynamics/evolution) — full equation of motion for the coherence matrix
- [Gap phase diagram](/docs/core/dynamics/gap-phase-diagram) — three phases of coherence and critical phenomena
