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

**Gap thermodynamics** answers the question: **which window configuration is energetically "cheaper"?** It turns out the system tends toward a specific transparency pattern — the **Gap vacuum** — just as water flows to the lowest point of a landscape. It is unique only up to the symmetries of the potential, and that only numerically ([T-61](/docs/core/dynamics/gap-thermodynamics#теорема-единственный-вакуум), restated as a hypothesis on 2026-09-25, §14); the sector structure once claimed for it is withdrawn [✗]. The vacuum is determined by the balance of three forces: the drive toward transparency (entropy), the drive toward order (coherence), and the arrow of time (octonionic associator).

The effective temperature $T_{\text{eff}}$ shows how "hot" the system is: at high temperature all panes of the window are equally murky (disordered phase); at low temperature a structured pattern emerges (ordered phase).
:::

This document develops the thermodynamic formalism for the [gap measure](/docs/physics/dual-aspect/gap-semantics) $\mathrm{Gap}(i,j) = |\sin(\arg(\gamma_{ij}))|$ between the external and internal aspects of the coherences of the [coherence matrix](/docs/core/dynamics/coherence-matrix) $\Gamma$. The formalism includes information geometry, a variational principle, the fluctuation-dissipation theorem, the Landauer bound, and the full Lagrangian of Gap theory.

---

## 1. Serre bundle geometry {#геометрия-расслоения-серра}

### Map bundle

:::tip Theorem 1.1 (Serre bundle) [T]
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

:::info Interpretation (Gap holonomy) [I]
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

:::info Definition (Manifold of Gap configurations) [T]
The space of Gap profiles is defined as:

$$
\mathcal{M}_{\mathrm{Gap}} := \{G = (G_{ij})_{1 \leq i < j \leq 7} : G_{ij} \in [0,1]\} \subset [0,1]^{21}
$$

with the additional realizability condition: $\exists\, \Gamma \in \mathcal{D}(\mathbb{C}^7)$ such that $\mathrm{Gap}(\Gamma)_{ij} = G_{ij}$.
:::

**Remark.** Not all points of the cube $[0,1]^{21}$ are realizable as Gap profiles of admissible density matrices. The set of realizable Gap profiles is a compact submanifold $\mathcal{M}_{\mathrm{Gap}} \subset [0,1]^{21}$.

### Quantum Fisher metric on $\mathcal{D}(\mathbb{C}^7)$

:::tip Theorem 2.0 (Quantum Fisher metric) [T]
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

:::tip Theorem 2.1 (Fisher metric) [T]
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

:::tip Theorem 2.2 (Lower bound for Gap estimation) [T]
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

:::info Interpretation (Geodesics as therapeutic path) [I]
A geodesic in $\mathcal{M}_{\mathrm{Gap}}$ defines the **optimal therapeutic path** — a sequence of minimally distinguishable Gap changes leading from a pathological to a healthy profile. The geodesic length $d_F$ is a measure of the "therapeutic work" required for the transition.
:::

---

## 3. Lower Gap bound from the octonionic associator {#нижняя-оценка-gap}

The connection between the Gap operator and the octonionic cross product is discussed in [Gap operator, section 7.2](/docs/core/dynamics/gap-operator#октонионное-крестное-произведение). Here we derive the key consequence: the **lower Gap bound** from the non-associativity of $\mathbb{O}$.

The octonionic **associator** $[e_i, e_j, e_k] := (e_i e_j)e_k - e_i(e_j e_k)$ vanishes for triples lying on [Fano lines](/docs/proofs/minimality/theorem-octonionic-derivation), and is nonzero for non-Fano triples.

:::tip Theorem 3.2 (Lower Gap bound from the associator) [T]
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

:::info Interpretation [I]
Octonionic non-associativity is the **algebraic source** of opacity. Pairs of dimensions connected through associative (Fano) subalgebras admit full transparency. Pairs connected through non-associative triples have an **irreducible minimum gap** — a fundamental limit on self-knowledge set by the algebraic structure of the octonions.
:::

:::info Status of Theorem 3.2 [T]
From [T-73](/docs/core/dynamics/gap-operator#теорема-gap-серра) [T] (Gap = Serre curvature) and [T-53](/docs/core/foundations/spacetime#теорема-спектральная-тройка) [T] (spectral triple): $\text{Gap}(i,j) \geq 4/(\omega_0^2 \|D_{\text{int}}\|^2) > 0$ for non-associative pairs. The constant $C = 4/(\omega_0^2 \|D_{\text{int}}\|^2)$ is uniquely determined by the spectral triple **[T]**.
:::

---

## 4. Variational principle {#вариационный-принцип}

### Action functional

:::tip Theorem 4.1 (Variational principle for Gap) [T]
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

:::tip Theorem 4.2 (Gap equations of motion) [T]
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

:::tip Theorem 5.1 (FEP decomposition) [T]
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

:::tip Theorem 5.2 (Equilibrium Gap) [T]
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

:::tip Theorem 6.1 (Fluctuation-dissipation theorem) [T]
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

:::tip Corollary 6.2 (Optimal influence frequency) [T]
For each channel $(i,j)$ there exists a **resonant frequency** $\omega_r^{(ij)}$ at which the Gap response is maximal:

$$
\omega_r^{(ij)} = \sqrt{|\omega_i - \omega_j|^2 - 2\Gamma_2^2}
$$

(if the expression under the square root is positive; otherwise the response is aperiodic).
:::

:::info Interpretation (Gap resonance) [I]
For channels with a large frequency difference $\Delta\omega$ (distant dimensions), the resonance is high-frequency — fast, intensive interventions are needed. For channels with small $\Delta\omega$ — slow, sustained ones. Frequency dependence for Markovian dynamics: $\chi_{ij}(\omega) \propto 1/(\omega^2 + \Gamma_2^2)$ (Lorentzian). Non-Markovian effects create **additional resonances** in $\chi(\omega)$.
:::

---

## 7. Landauer bound for Gap {#граница-ландауэра}

### Entropy production

:::tip Theorem 7.1 (Gap dissipation rate) [T]
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

:::tip Theorem 7.2 (Minimum dissipation power) [T]
The dissipation power in the Gap sector is bounded below:

$$
\dot{W}_{\text{Gap}} \geq \Gamma_2 \, \mathcal{G}_{\text{total}}
$$

where $\mathcal{G}_{\text{total}} = \|\hat{\mathcal{G}}\|_F^2 = 2\sum_{i<j} |\gamma_{ij}|^2 \, \mathrm{Gap}(i,j)^2$ is the [total Gap](/docs/core/dynamics/gap-operator#g-total-definition).
:::

### Landauer bound

:::tip Theorem 7.3 (Landauer bound for Gap) [T]
Minimum work for fully erasing one bit of Gap information (transition $\mathrm{Gap}: 1 \to 0$ for one channel):

$$
W_{\text{erase}} \geq k_B T_{\text{eff}} \ln 2
$$

where $k_B$ is the Boltzmann constant, $T_{\text{eff}}$ is the [effective temperature](#эффективная-температура).

**Justification:** By Landauer's principle, erasing information (reducing the system's entropy) requires releasing heat. A Gap channel with $\mathrm{Gap} = 1$ carries 1 bit of information (full orthogonality of external and internal aspects). Setting Gap to zero erases this bit.
:::

### The price of enlightenment

:::tip Theorem (Price of enlightenment) [C at T-105]
To transition from a maximally opaque state ($\mathrm{Gap} = 1$ for all 21 pairs) to full transparency ($\mathrm{Gap} = 0$ for all pairs), the minimum work required is:

$$
W_{\text{enlightenment}} \geq 21 \, k_B T_{\text{eff}} \ln 2
$$

The factor 21 = $\binom{7}{2}$ is the number of off-diagonal pairs in a $7 \times 7$ matrix. Each pair carries at least 1 bit of Gap information.

**Proof.** Each of the 21 off-diagonal pairs $(i,j)$ of the $7 \times 7$ matrix with $\mathrm{Gap}_{ij} = 1$ carries exactly 1 bit of information (full orthogonality of external and internal aspects, two distinguishable states: $\mathrm{Gap} = 0$ vs $\mathrm{Gap} = 1$). Setting $\mathrm{Gap}_{ij}$ to zero erases this bit. By Landauer's principle (consequence of the second law of thermodynamics, Landauer 1961), erasing one bit at temperature $T$ requires $W \geq k_B T \ln 2$. Applying this to each of the 21 pairs independently at the effective temperature $T_{\text{eff}}$ from [T-105](/docs/core/dynamics/gap-thermodynamics#эффективная-температура) [T] (fluctuation-dissipation theorem for Gap dynamics):

$$
W_{\text{enlightenment}} = \sum_{i < j} W_{ij} \geq 21 \cdot k_B T_{\text{eff}} \ln 2
$$

The number 21 = $\binom{7}{2}$ is exact [T] (combinatorics of $N = 7$ dimensions). Conditionality: the result depends on $T_{\text{eff}}$ from T-105 being the relevant temperature scale for erasing Gap information. $\blacksquare$
:::

---

## 8. Commutator algebra and DFS structure {#коммутаторная-алгебра}

:::note Canonical definition
The properties of the commutator $[\hat{\mathcal{G}}, \Gamma]$ (anti-Hermiticity, unitary flow) and the $G_2/\perp$ decomposition of the Gap operator are defined in [Gap operator](/docs/core/dynamics/gap-operator#коммутаторная-алгебра) (sections 6–7). Here only thermodynamic consequences are considered: decoherence-free subspaces (DFS) and Fano vulnerability.
:::

### Decoherence-free subspaces (DFS)

:::tip Theorem 8.1 (DFS classification) [T]
Decoherence-free subspaces are classified by the position of pairs on the Fano plane:

| Subspace | $\dim(\mathrm{DFS})$ | Protection |
|---|---|---|
| Pure Fano pair | 0 | No protection (full decoherence) |
| Non-Fano pair | $\geq 1$ | Partial protection |
:::

**Paradox:** Fano pairs, for which Gap can be zero (Theorem 3.2), are **not protected** against decoherence. Non-Fano pairs, which have an irreducible minimum Gap, are **partially protected**. This means:

:::info Interpretation (Fano vulnerability) [I]
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

### Fixed points of the self-model

:::tip Theorem 10.1 (Fixed points of the self-model; corrected 2026-09-26) [T]
**(a) Existence.** Every continuous self-model $\varphi: \mathcal{D}(\mathbb{C}^7) \to \mathcal{D}(\mathbb{C}^7)$ has a fixed point:

$$
\exists \Gamma^* : \varphi(\Gamma^*) = \Gamma^*
$$

— in particular $\varphi_{\mathrm{coh}}$, the self-registering $\varphi_s$ and the collineation-anchored $\varphi_J$, whose weights $R = 1/(7P)$, $k = 1 - R$ are continuous because $P \geq 1/7$.

**(b) Uniqueness depends on the self-model.** $\varphi_{\mathrm{coh}}$ has exactly one fixed point, $I/7$. $\varphi_J$ has exactly one, $\Gamma_{\eta_\infty} = (1 - \eta_\infty)\,I/7 + \eta_\infty\,uu^\dagger$, where $\eta_\infty$ is the unique positive root of $6(1 - c)\eta^3 + \eta - 1 = 0$, $c = (1 - \alpha)/3$; its purity $(1 + 6\eta_\infty^2)/7$ is $5/14$, $0.334$, $0.317$ at $\alpha = 0, 1/2, 1$ — the upper end $P_\infty$ of the [living attractor](/docs/core/dynamics/evolution#теорема-живой-аттрактор-в-окне). $\varphi_s$ has at least eight: $I/7$ and the seven basis states.

**(c) No contraction.** Banach's theorem applies to none of them: near pure states $\varphi_{\mathrm{coh}}$ stretches Frobenius distances by up to $54/49$ and $\varphi_J$ by $1.129$.

Applying Gap to both sides, we obtain the self-referential Gap:

$$
\mathrm{Gap}^{(2)}(i,j) = \mathrm{Gap}(\varphi(\Gamma))_{ij}
$$
:::

*Erratum 2026-09-26.* The box read: "a **unique fixed point** exists: $\varphi$ is contractive with $k = 1 - R < 1$ (T-62 [T]), $\mathcal{D}(\mathbb{C}^7)$ is compact ⇒ complete metric space, Banach FPT gives unique $\Gamma^*$". The factor $k$ multiplies the deviation from the anchor, not distances, so it is not a Lipschitz constant (item (c)), and $\varphi_s$ has several fixed points. What survives is existence, which is Brouwer's theorem, not Banach's; uniqueness holds for $\varphi_{\mathrm{coh}}$ and $\varphi_J$ by the computation below. Lawvere's theorem gives, in a topos, a fixed point of every endomorphism of an object $Y$ that receives a point-surjection $A \to Y^A$; it is the categorical reading of (a) and says nothing about uniqueness.

**Proof.** (a) $\mathcal{D}(\mathbb{C}^7)$ is a compact convex subset of the 48-dimensional real space of trace-one Hermitian matrices, and Brouwer's theorem applies to every continuous self-map of it. (b) $\varphi_{\mathrm{coh}}$: [φ operator](/docs/core/operators/phi-operator#неподвижная-точка-phi-coh). $\varphi_J$: $\mathcal{P}_\alpha$ keeps the diagonal and multiplies coherences by $c$, so the diagonal of $\varphi_J(\Gamma) = \Gamma$ reads $k\gamma_{ii} + R/7 = \gamma_{ii}$, i.e. $R(1/7 - \gamma_{ii}) = 0$, and every $\gamma_{ii} = 1/7$; each coherence obeys $kc\,\gamma_{ij} + R/7 = \gamma_{ij}$, so all equal $\eta/7$ with the real $\eta = R/(1 - kc)$. Then $P = (1 + 6\eta^2)/7$, $R = 1/(1 + 6\eta^2)$, $k = 6\eta^2/(1 + 6\eta^2)$, and $\eta(1 - kc) = R$ becomes $\eta + 6(1 - c)\eta^3 = 1$, whose left side increases strictly: one root, in $(0, 1)$. $\varphi_s$: $\mathcal{P}_\alpha(e_m) = e_m$ and $e_m^2/\mathrm{Tr}\,e_m^2 = e_m$, so $\varphi_s(e_m) = e_m$; and $\varphi_s(I/7) = I/7$. (c) [Evolution, iterative scheme](/docs/core/dynamics/evolution#итеративная-схема) (`test_phi_coh_contracts_toward_i7_but_is_not_a_contraction`, `test_self_model_contraction_holds_only_for_constant_weight_and_unital_part`). $\blacksquare$

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

*(Scope, 2026-09-26: read with the Gap operator $\hat{\mathcal G} = \mathrm{Im}\,\Gamma$, a self-model of replacement form with a real anchor — $\varphi_{\mathrm{coh}}$, $\varphi_J$ — registers exactly the fraction $kc \leq 2/7$ of the Gap operator (Theorem 10.2), so $\mathrm{Gap}^{(2)} = (1 - kc)\,|\hat{\mathcal G}_{ij}|$ and vanishes only where the Gap does. The equality above holds at the fixed points of Theorem 10.1, where $\hat{\mathcal G} = 0$; it is not a property of a level of interiority.)*

### Hierarchy of Gap reflection

:::tip Theorem 10.2 (The Gap reflection hierarchy; restated 2026-09-26) [T]
Let $\varphi(\Gamma) = k\,\mathcal{P}_\alpha(\Gamma) + R\,\rho_a(\Gamma)$ be a self-model of replacement form whose anchor $\rho_a(\Gamma)$ is real — $\varphi_{\mathrm{coh}}$ ($\rho_a = I/7$), $\varphi_J$ ($\rho_a = uu^\dagger$), every real constant anchor — and let $\Gamma^{(n)} = \varphi^n(\Gamma)$, $\hat{\mathcal G}^{(n)} = \mathrm{Im}\,\Gamma^{(n)}$ the Gap operator ([norm convention](/docs/core/dynamics/gap-operator#g-total-definition)).

1. **The Gap operator.** $\hat{\mathcal G}(\varphi(\Gamma)) = k(\Gamma)\,c\,\hat{\mathcal G}(\Gamma)$ exactly. Hence

$$
\|\hat{\mathcal G}^{(n)}\|_F \leq \Bigl(\frac{6c}{7}\Bigr)^n \|\hat{\mathcal G}^{(0)}\|_F \leq \Bigl(\frac27\Bigr)^n \|\hat{\mathcal G}^{(0)}\|_F :
$$

the hierarchy converges to $\hat{\mathcal G}^* = 0$ at a rate of at most $2/7$ per reflection, whatever the level of interiority.

2. **The phase Gap** $\mathrm{Gap}(i,j) = |\sin\arg\gamma_{ij}|$. $\varphi_{\mathrm{coh}}$ keeps every phase, so $\mathrm{Gap}^{(n)} = \mathrm{Gap}^{(0)}$ as long as the coherence stays above $\varepsilon_{\min}$, and $\mathrm{Gap} := 1$ once it falls below ([convention](/docs/core/dynamics/gap-operator)). For $\varphi_J$, $\mathrm{Re}\,\gamma^{(n)}_{ij} \geq 1/49$ for $n \geq 4$ and $\mathrm{Gap}^{(n)}(i,j) \leq \tfrac{49}{2}\,(2/7)^n$.
3. **The states.** $\|\varphi_{\mathrm{coh}}^n(\Gamma) - I/7\|_F \leq (6/7)^n\|\Gamma - I/7\|_F$. At $\Gamma_{\eta_\infty}$ the Jacobian of $\varphi_J$ has the eigenvalues $k$ ($\times 6$), $kc$ ($\times 41$) and $-6\eta_\infty^2(2 - 3c)/(1 + 6\eta_\infty^2)$ (along $uu^\dagger - I/7$), so the fixed point attracts for $\alpha < \alpha^*$ and repels along the family for $\alpha > \alpha^*$, where $\alpha^* = 0.7900$ is the real root of $27\alpha^3 - 8\alpha^2 - 8\alpha - 2 = 0$.
:::

**Proof.** (1) $\mathcal{P}_\alpha$ keeps the real diagonal and multiplies the off-diagonal part by $c$, so $\mathrm{Im}\,\mathcal{P}_\alpha(\Gamma) = c\,\mathrm{Im}\,\Gamma$; $\mathrm{Im}\,\rho_a = 0$. With $k = 1 - 1/(7P) \leq 6/7$ and $c \leq 1/3$ the bound follows. (2) The coherences of $\varphi_{\mathrm{coh}}(\Gamma)$ are $kc\,\gamma_{ij}$ with $kc > 0$. For $\varphi_J$, $\mathrm{Re}\,\gamma^{(n+1)}_{ij} = k_n c\,\mathrm{Re}\,\gamma^{(n)}_{ij} + R_n/7$ with $k_nc \leq 2/7$, $R_n \geq 1/7$ and $|\mathrm{Re}\,\gamma^{(0)}_{ij}| \leq 1/2$; the lower bounds $-1/2$, $-6/49$, $-5/343$, $39/2401$ make $\mathrm{Re}\,\gamma^{(3)}_{ij} > 0$, whence $\mathrm{Re}\,\gamma^{(n)}_{ij} \geq 1/49$ for $n \geq 4$; with $|\mathrm{Im}\,\gamma^{(n)}_{ij}| \leq (2/7)^n/2$ from (1), $|\sin\arg\gamma| \leq |\mathrm{Im}\,\gamma|/\mathrm{Re}\,\gamma$ gives the bound. (3) $\varphi_{\mathrm{coh}}(\Gamma) - I/7 = k\,\mathcal{P}_\alpha(\Gamma - I/7)$ with $\|\mathcal{P}_\alpha\| \leq 1$. The family $\Gamma_\eta$ is invariant, $\varphi_J(\Gamma_\eta) = \Gamma_{f(\eta)}$ with $f(\eta) = (1 + 6c\eta^3)/(1 + 6\eta^2)$, and $f'(\eta_\infty)$ is the stated eigenvalue. The derivatives of $k$ and $R$ multiply $\mathcal{P}_\alpha(\Gamma) - uu^\dagger$, a multiple of $uu^\dagger - I/7$, and are paired with $dP(X) = 2\,\mathrm{Tr}(\Gamma_{\eta_\infty}X)$, which vanishes on traceless diagonal $X$ and on coherence directions orthogonal to $uu^\dagger$; so the Jacobian is block-triangular, $k$ on the diagonal, $kc$ on the other coherences. $|f'(\eta_\infty)| = 1$ together with $\eta_\infty + 6(1 - c)\eta_\infty^3 = 1$ gives $\eta_\infty = \alpha/(2 - 4c)$ and $27\alpha^3 = 2(1 + 2\alpha)^2$. $\blacksquare$

**Numerical check** (`test_fixed_points_of_self_models_and_the_gap_reflection_hierarchy`). $\eta_\infty = 0.5000$, $0.4725$, $0.4507$ at $\alpha = 0, 1/2, 1$, residual $\|\varphi_J(\Gamma_{\eta_\infty}) - \Gamma_{\eta_\infty}\|_F < 10^{-15}$; $\|\mathrm{Im}\,\varphi_J(\Gamma)\|_F = kc\,\|\mathrm{Im}\,\Gamma\|_F$ to $10^{-13}$ at every step; from 20 random starts per $\alpha$, 3000 iterations of $\varphi_J$ reach $\Gamma_{\eta_\infty}$ to $10^{-14}$ at $\alpha = 0$, $0.25$, $0.5$, $0.75$ and end on a 2-cycle at $\alpha = 0.8$, $0.9$, $1$ (distance $0.056$, $0.21$, $0.31$ from the fixed point).

*Retracted 2026-09-26 [✗]: the table of $k$ by level ($k \to 1$ at L1, $k \approx 0.7$ at L2, $k \approx 0.3$ at L3, $k = 0$ at L4) and the interpretation "Ladder of self-knowledge" [I] built on it. The values were not derived, and the per-reflection factor of the Gap operator is $kc \leq 2/7$ at every level (item 1); the phase Gap of $\varphi_{\mathrm{coh}}$ does not move at all (item 2).*

---

## 10. Full Lagrangian of Gap theory {#полный-лагранжиан}

### Lagrangian structure

:::tip Theorem 11.1 (Full Lagrangian) [T]
Full Lagrangian of Gap theory:

$$
\mathcal{L}_{\text{Gap}} = \mathcal{L}_{\text{kin}} + \mathcal{L}_{\text{pot}} + \mathcal{L}_{\text{top}} + \mathcal{L}_{\text{diss}} + \mathcal{L}_{\text{reg}} + \mathcal{L}_{\text{ext}}
$$
:::

:::info Derivation of Lagrangian from Lindbladian [T]
The full Lagrangian $\mathcal{L}_{\text{Gap}}$ (including dissipative and regenerative terms) is the **classical limit** of the Schwinger–Keldysh action for the Lindbladian $\mathcal{L}_\Omega$ ([T-39a](/docs/core/operators/lindblad-operators#примитивность-ℒω) [T]) in the coherent-phase representation.

**Keldysh action.** For the Markovian master equation $\partial_t \rho = \mathcal{L}_\Omega(\rho)$, the functional integral on the Keldysh contour (Sieberer, Buchhold, Diehl, *Rep. Prog. Phys.* 79, 2016):

$$
S_K[\rho_+, \rho_-] = \int dt \left[\mathrm{Tr}(\rho_q \cdot \mathcal{L}_\Omega(\rho_{\mathrm{cl}})) + i \, \mathrm{Tr}(\rho_q \cdot \mathcal{D} \cdot \rho_q)\right]
$$

where $\rho_{\mathrm{cl}} = (\rho_+ + \rho_-)/2$, $\rho_q = \rho_+ - \rho_-$, $\mathcal{D}_{ij,kl} = \sum_\alpha [L_\alpha]_{ik}[L_\alpha^\dagger]_{jl}$.

**Decomposition.** The Lindbladian $\mathcal{L}_\Omega = \mathcal{L}_{\mathrm{Ham}} + \mathcal{L}_{\mathrm{diss}} + \mathcal{L}_{\mathrm{reg}}$ ([T-57](/docs/core/operators/lindblad-operators#полнота-триадной-декомпозиции) [T]) gives in the coherent-phase representation:
- **$\mathcal{L}_{\mathrm{Ham}} \to \mathcal{L}_{\mathrm{kin}} + \mathcal{L}_{\mathrm{pot}} + \mathcal{L}_{\mathrm{top}}$**: the commutator $-i[H_{\mathrm{Fano}}, \rho]$ generates the kinetic, potential ($V_{\mathrm{Gap}}$ from the [spectral action](#вывод-vgap-из-спектрального-действия)) and topological terms.
- **$\mathcal{L}_{\mathrm{diss}} \to \mathcal{L}_{\mathrm{diss}}$**: the Lindblad dissipator $\sum_k L_k\rho L_k^\dagger - \frac{1}{2}\{L_k^\dagger L_k, \rho\}$ acts on coherences as decay $-\Gamma_2^{(ij)} \gamma_{ij}$, where $\Gamma_2^{(ij)} = \frac{1}{2}\sum_k |\langle i|L_k|i\rangle - \langle j|L_k|j\rangle|^2$.
- **$\mathcal{L}_{\mathrm{reg}} \to \mathcal{L}_{\mathrm{reg}}$**: regeneration $\kappa_0(\varphi(\rho) - \rho)$ ([T-62](/docs/consciousness/foundations/self-observation#теорема-физическая-реализация-phi) [T]) gives $-\kappa|\gamma_{ij}|^2(\theta_{ij} - \theta_{ij}^{\mathrm{target}})$.

**Classical limit** ($\theta_q \to 0$) reproduces the equations of motion for $\mathcal{L}_{\mathrm{Gap}}$ **exactly**. The dissipative and regenerative terms are not "ad hoc," but **necessary consequences** of the Lindblad structure of the dynamics. The external field $\mathcal{L}_{\mathrm{ext}}$ is the standard linear term in the presence of an external source.

**Self-consistency of stationarity.** At $\dot{\theta} = 0$ and $\theta = \theta^{\mathrm{target}}$ the equation of motion reduces to $\partial V_{\mathrm{Gap}}/\partial\theta = 0$: the nontrivial attractor $\rho_*$ of the full Lindbladian $\mathcal{L}_\Omega$, where one exists (T-96 [T]; it needs a non-unital self-model or an environment — an isolated holon with the canonical $\varphi_{\mathrm{coh}}$ has none, [T-124c](/docs/core/dynamics/evolution#теорема-единственность-нетривиального-аттрактора)) coincides with a minimum of $V_{\mathrm{Gap}}$ (for the $G_2$-invariant potential this minimum is unique up to $G_2$ — [T-64](/docs/core/dynamics/gap-thermodynamics#теорема-глобальная-минимизация), corrected 2026-09-25: [T] for every $\kappa > 0$ off the transition curves, §14).
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

:::tip Theorem (Coefficient $\beta$ from first principles) [T]
The coefficient $\beta = \lambda_3/(2\pi)$ is uniquely determined by the imaginary part of the Keldysh action. See [full derivation](/docs/physics/cosmology-phys/berry-phase#теорема-l-top-кельдыш).
:::

$$
\mathcal{L}_{\text{top}} = \frac{\lambda_3}{2\pi} \sum_{(i,j,k) \in \text{Fano}} \varepsilon^{\text{Fano}}_{ijk} \, \theta_{ij} \, \dot{\theta}_{jk}
$$

where:
- $\varepsilon^{\text{Fano}}_{ijk} = \pm 1$ — structure constants of the Fano plane
- summation over 7 Fano lines
- $\beta = \lambda_3/(2\pi)$ — derived from $\mathrm{Im}(S_{\text{Keldysh}})$ [T]

**Origin:** This term is the **Berry phase** in the space of Gap configurations $(S^1)^{21}$, arising from the imaginary part of the Keldysh action. The CS derivation is refuted ([full derivative in 1D](/docs/physics/cosmology-phys/berry-phase#9-опровержение-cs-вывода) [T]). It is **topological** — independent of the metric, determined only by the combinatorial structure of the Fano plane.

### (d) Dissipative term (Rayleigh function)

$$
\mathcal{L}_{\text{diss}} = -\Gamma_2 \sum_{i<j} |\gamma_{ij}|^2 \, \dot{\theta}_{ij} \, \theta_{ij}
$$

where $\Gamma_2 \geq 0$ is the decoherence rate (phase dissipation).

**Origin:** The dissipative term is derived from the Lindblad dissipator $\sum_k L_k\rho L_k^\dagger - \frac{1}{2}\{L_k^\dagger L_k, \rho\}$ in the coherent-phase representation [T]. The decoherence rate $\Gamma_2^{(ij)} = \frac{1}{2}\sum_k |\langle i|L_k|i\rangle - \langle j|L_k|j\rangle|^2$ is determined by the Fano operators [T].

### (e) Regenerative term

$$
\mathcal{L}_{\text{reg}} = \kappa \sum_{i<j} |\gamma_{ij}|^2 \, (\theta_{ij}^{\text{target}} - \theta_{ij})^2
$$

where:
- $\kappa = \kappa_0 k$ — regeneration rate (from [categorical derivation](/docs/core/foundations/axiom-septicity#структурный-анзац-kappa0) [T] and replacement channel [T-62](/docs/consciousness/foundations/self-observation#теорема-физическая-реализация-phi) [T])
- $\theta_{ij}^{\text{target}} = \arg(\varphi(\Gamma)_{ij})$ — target phase from [self-modeling](/docs/consciousness/foundations/self-observation#оператор-самомоделирования-φ)
- **Origin:** The regenerative term is derived from $\mathcal{L}_{\mathrm{reg}}(\rho) = \kappa_0(\varphi(\rho) - \rho)$ in the coherent-phase representation [T]

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
- **$G_2$-invariance** [T] — all terms preserve [octonionic automorphisms](/docs/physics/gauge-symmetry/g2-structure)
- **$\mathbb{Z}_2(\mathrm{PT})$** — broken by the cubic term $V_3$ of the potential (see [section 11](#потенциал-v-gap))
- **$U(1)$** — broken by the regenerative term $\mathcal{L}_{\text{reg}}$ (the target phase singles out a direction)

---

## 11. Potential $V_{\text{Gap}}$: "Higgs for opacity" {#потенциал-v-gap}

### Full form

#### Derivation of $V_{\text{Gap}}$ from the spectral action [T] {#вывод-vgap-из-спектрального-действия}

:::tip Theorem (V_Gap from spectral action) [T]
The potential $V_{\text{Gap}}(\{\theta_{ij}\})$ is uniquely determined by the spectral action of the internal [spectral triple](/docs/core/foundations/spacetime#теорема-спектральная-тройка) $(A_{\mathrm{int}}, H_{\mathrm{int}}, D_{\mathrm{int}})$ (T-53 [T]):

$$
V_{\text{Gap}} = \left.\mathrm{Tr}(f(D_A / \Lambda))\right|_{\mathrm{int}} = V_2 + V_3 + V_4
$$

where $D_A = D_{\mathrm{int}} + A + \varepsilon J A J^{-1}$ is the fluctuated Dirac operator.
:::

**Proof.**

**Step 1 (Identity $\mathrm{Tr}(D_{\mathrm{int}}^2) = \omega_0^2 \, \mathcal{G}_{\mathrm{total}}$).** From T-53 [T]: $[D_{\mathrm{int}}]_{ij} = \omega_0 \cdot \mathrm{Gap}(i,j) \cdot |\gamma_{ij}| \cdot e^{i\theta_{ij}}$, $[D_{\mathrm{int}}]_{ii} = 0$ (block off-diagonal structure $O \leftrightarrow 3 \leftrightarrow \bar{3}$). Therefore:

$$
\mathrm{Tr}(D_{\mathrm{int}}^2) = \sum_{i \neq j} |[D_{\mathrm{int}}]_{ij}|^2 = \omega_0^2 \sum_{i \neq j} |\gamma_{ij}|^2 \cdot \mathrm{Gap}(i,j)^2 = \omega_0^2 \cdot \mathcal{G}_{\mathrm{total}}
$$

(the last equality is the [definition of $\mathcal{G}_{\mathrm{total}}$](/docs/core/dynamics/gap-operator#g-total-definition) [D]). This identity confirms [T-73](/docs/core/dynamics/gap-operator#теорема-gap-серра) [T] (Gap = curvature).

:::info Worked numerical example
For a holon at $P = 0.35$ with three representative off-diagonal coherences $\gamma_{EO} = 0.08\,e^{i\pi/3}$, $\gamma_{AE} = 0.06\,e^{i\pi/4}$, $\gamma_{OU} = 0.05\,e^{i\pi/5}$:

$$\mathcal{G}_{\text{total}} \geq 0.08^2 \cdot \sin^2(\pi/3) + 0.06^2 \cdot \sin^2(\pi/4) + 0.05^2 \cdot \sin^2(\pi/5) = 0.0048 + 0.0018 + 0.0009 \approx 0.0075$$

At $\omega_0 = 40$ Hz: $\mathrm{Tr}(D_{\text{int}}^2) = 1600 \cdot 0.0075 = 12.0 > 0$. The spectral action contribution is strictly positive — reflecting the thermodynamic fuel for regeneration. By T-55 [T], $\mathcal{G}_{\text{total}} = 0$ requires all $\sin\theta_{ij} = 0$ (purely real coherences), which Lawvere incompleteness forbids for viable systems.
:::

**Step 2 ($V_2$ from the Seeley–DeWitt coefficient $a_2$).** The [spectral action](/docs/physics/gravity/quantum-gravity#теорема-полное-спектральное-действие) (T-65 [T]) for the product $M_4 \times F_7$:

$$
\mathrm{Tr}(f(D_{\mathrm{total}}/\Lambda)) = f_0 \Lambda^4 \, a_0 + f_2 \Lambda^2 \, a_2 + f_4 \, a_4 + \ldots
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

**Step 5 (Uniqueness).** The spectral triple is unique up to $G_2$-equivalence ([T-42a](/docs/proofs/categorical/uniqueness-theorem) [T]). The spectral action is the unique $G_2$-invariant functional on $(S^1)^{21}$, compatible with NCG (Chamseddine–Connes theorem). $\blacksquare$

**Derivation chain:**

$$
\mathrm{A1\text{--}A5} \xrightarrow{\mathrm{T\text{-}57}} \mathcal{L}_\Omega \xrightarrow{\mathrm{T\text{-}39a}} \rho_* \xrightarrow{\mathrm{T\text{-}53}} D_{\mathrm{int}} \xrightarrow{\mathrm{T\text{-}65}} V_{\mathrm{Gap}}
$$

:::tip Theorem 13.4 (Gap potential) [T]
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

:::info Remark (Phase dependence of $V_3$) [I]
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
| $G_2$ | + | — | + |
| $\mathbb{Z}_2(\mathrm{PT})$ | + | — | + |
| $U(1)$ | — | — | — |

*(Erratum 2026-09-25, audit A-90: the $G_2$ entry for $V_3$ read "+". It is false. $V_2$ and $V_4$ depend on $\Gamma$ only through $\mathcal{G}_{\text{total}} = \lVert \mathrm{Im}\,\Gamma \rVert_F^2$ and are even $O(7)$-invariant, but the sum over the 28 non-Fano triples in $V_3$ changes under generic elements of $G_2$ and even of $SU(3) = \mathrm{Stab}_{G_2}(e_O)$ — 10 of 10 random elements moved it (`test_v_gap_cubic_term_is_not_g2_invariant`); of the 896 signed permutations of the axes that preserve $V_3$, only 56 lie in $G_2$.)*

### The $G_2$-invariant cubic (T-331) {#g2-инвариантный-кубик}

The erratum above leaves the question of which cubic term a $G_2$-invariant potential can have. Invariant theory answers it. Write $\Gamma = I/7 + S + iX$, with $S$ real symmetric and traceless (the $\mathbf{27}$ of $G_2$) and $X$ real antisymmetric, $X = X_7 + X_{14}$ ($\Lambda^2\mathbb R^7 = \mathbf 7 \oplus \mathbf{14}$). $\mathrm{PT}$ acts as $\Gamma \mapsto \bar\Gamma$, that is $X \mapsto -X$, and $\mathcal{G}_{\text{total}} = \lVert X \rVert_F^2$.

:::tip Theorem 13.7 (T-331): $G_2$-invariant Gap potentials up to quartic order [T]
**(a)** The $G_2$-invariant polynomials in $(S, X)$ are: three quadratic ($\lVert S\rVert^2$, $\lVert X_7\rVert^2$, $\lVert X_{14}\rVert^2$), five cubic and twenty-one quartic. No invariant of degree $\le 3$ is odd in $X$; the $\mathrm{PT}$-odd invariants begin in degree 4, where there are three (of the types $S^3X_7$, $SX_7^2X_{14}$, $SX_7X_{14}^2$). No cubic invariant depends on $X$ alone. Hence every $G_2$-invariant potential of degree $\le 3$ is $\mathrm{PT}$-even, and a cubic term in the Gap field $\mathrm{Im}\,\Gamma$ alone does not exist.

**(b)** Under the finite frame group $\Gamma_{\!\text{oct}}$ alone ([D-0910](/docs/proofs/categorical/uniqueness-theorem#g2-ригидность)) there are 25 cubic invariants of $\Gamma$, three of them $\mathrm{PT}$-odd. None of them has the triangle form $\sum_{ijk} c_{ijk}\,\mathrm{Im}(\gamma_{ij}\gamma_{jk}\gamma_{ki})$ of $V_3$, and the average of $V_3$ over $\Gamma_{\!\text{oct}}$ is zero.

**(c)** The **associator cubic**

$$
\mathcal A(\Gamma) = \sum_{i,j,k,a,b,c} \big\langle [e_i,e_j,e_k],\,[e_a,e_b,e_c] \big\rangle\, \Gamma_{ia}\Gamma_{jb}\Gamma_{kc}
$$

(the mean of $\lVert[x,y,z]\rVert^2$ over three independent vectors with covariance $\Gamma$) is $G_2$-invariant, $\mathrm{PT}$-even and non-negative on $\mathcal D(\mathbb C^7)$. It equals $96\,\mathrm{Tr}(\Pi_7\,\Lambda^3\Gamma)$, where $\Pi_7$ is the projector of $\Lambda^3\mathbb C^7$ onto $\Lambda^3_7 = \{\iota_v\psi\}$. On the coordinate state $\tfrac13(|e_i\rangle\langle e_i| + |e_j\rangle\langle e_j| + |e_k\rangle\langle e_k|)$ it equals $\tfrac{6}{27}\lVert[e_i,e_j,e_k]\rVert^2$ — zero on a Fano line and $24/27$ off it, the weights of $V_3$ squared. It vanishes on every state of rank $\le 2$ and on every state supported on an associative 3-plane (Artin's theorem).

**(d)** Up to a factor, $\mathcal A$ is the only $G_2$-invariant cubic that depends on $\Gamma$ through the associator, that is, has the form $\mathrm{Tr}(K\,a\,(\Lambda^3\Gamma)\,a^\dagger)$ with $a: \Lambda^3\mathbb C^7 \to \mathbb C^7$ the associator map and $K$ an invariant operator on $\mathbb C^7$.
:::

**Proof.** (a) The dimensions of the invariants in $\mathrm{Sym}^d(\mathbf{27}\oplus\mathbf 7\oplus\mathbf{14})$, graded by the degrees in $S$, $X_7$, $X_{14}$, are computed by the Weyl integration formula over the maximal torus of $G_2$; a finite grid integrates the trigonometric polynomials of these degrees exactly. The structure behind the zeros: $\mathbf 7^{\otimes 3}$ has one invariant, the alternating $\varphi$, so $\mathrm{Sym}^3\mathbf 7$ has none; $\mathrm{Sym}^2\mathbf 7 = \mathbf 1\oplus\mathbf{27}$ and $\mathrm{Sym}^2\mathbf{14} = \mathbf 1\oplus\mathbf{27}\oplus\mathbf{77}$ contain neither $\mathbf 7$ nor $\mathbf{14}$; $G_2$ has no cubic Casimir (its degrees are 2 and 6); and the count shows that $\mathrm{Sym}^2\mathbf{27}$ contains neither $\mathbf 7$ nor $\mathbf{14}$, so no $S S X$ invariant exists. (b) Burnside's count over the 1344 elements of $\Gamma_{\!\text{oct}}$, with and without $\mathrm{PT}$. A product $\mathrm{Im}(\gamma_{ij}\gamma_{jk}\gamma_{ki})$ is unchanged by sign changes of the axes (each index occurs twice) and alternates under permutations of $(i,j,k)$; the collineations lift to $\Gamma_{\!\text{oct}}$ and permute the vertices of any triangle in all six ways ([T-177](/docs/core/structure/dimensions#комбинаторная-единственность)), so an invariant alternating weight is zero. (c) The associator tensor is totally antisymmetric ($a = 2\psi$), so $\mathcal A = \sum_l \langle a_l|\Gamma^{\otimes 3}|a_l\rangle \ge 0$ and $\mathcal A$ factors through $\Lambda^3\Gamma$; $a\,a^\dagger$ is an invariant operator on the irreducible $\mathbb C^7$, hence scalar, so $a^\dagger a$ is a multiple of $\Pi_7$, fixed by $\mathcal A(I/7) = 672/343$ and $\mathrm{Tr}\,\Pi_7 = 7$. Real conjugation fixes $a$, so $\mathcal A(\bar\Gamma) = \overline{\mathcal A(\Gamma)} = \mathcal A(\Gamma)$. (d) By Schur's lemma $K = c\,I$. $\blacksquare$

Checks: `test_g2_invariant_cubics_are_pt_even`, `test_frame_group_cubics_and_the_page_v3_average`, `test_associator_cubic_is_invariant_positive_and_factors_through_lambda3_7`.

**The corrected potential.** $V_2$ and $V_4$ stand. The cubic term is replaced by the associator cubic:

$$
V_{\text{Gap}} = \mu^2\,\mathcal{G}_{\text{total}} + \lambda_4\,\mathcal{G}_{\text{total}}^2 - \kappa\,\mathcal A(\Gamma).
$$

The sign is chosen so that $\kappa > 0$ lets non-associativity lower the potential, as $V_3$ did at its optimal phases (there the sine is $-1$ and $V_3 = -\lambda_3\sum_{\notin\text{Fano}}\lVert[e_i,e_j,e_k]\rVert\,|\gamma_{ij}||\gamma_{jk}||\gamma_{ik}|$); [T-64](#теорема-глобальная-минимизация) treats every sign. The value of $\kappa$ is not derived: Theorem 13.5 gave $\lambda_3$ for the retracted $V_3$ only. The sources of the potential that the corpus does derive all give $\kappa = 0$.

:::tip T-331(e): no derived source of $V_{\text{Gap}}$ carries the associator cubic [T]
Let $F$ be a functional on $\mathcal D(\mathbb C^7)$ of one of three kinds: (i) a function of the off-diagonal entries of $\Gamma$ in the axis frame alone — in particular every spectral action $\mathrm{Tr}\,f(D_A^2/\Lambda^2)$ of the internal Dirac operator of T-53, whose entries are $\omega_0\,\mathrm{Gap}(i,j)\,|\gamma_{ij}|\,e^{i\theta_{ij}}$, with fluctuations $D_A = D + A + \varepsilon JAJ^{-1}$, $A = \sum a[D,b]$; (ii) a function of the spectrum of $\Gamma$ — entropy, purity, relative entropy to $I/7$, the source of $\mu^2 = (1-s^2)/(2s^2)$; (iii) the $G_2$-average $\int_{G_2} V_3(g\Gamma g^{\mathsf T})\,dg$ of the retracted cubic. If $F = c_2\mathcal{G}_{\text{total}} + c_4\mathcal{G}_{\text{total}}^2 - \kappa\mathcal A + F'$ with $F'$ of kind (i) or (ii), then $\kappa = 0$; and the average (iii) is identically $0$. None of these sources fixes $\kappa \ne 0$; taken as the whole potential, each gives $\kappa = 0$, where T-64 (a) applies — no spontaneous Gap and no unique vacuum.
:::

**Proof.** The coordinate states $\tfrac13(|e_i\rangle\langle e_i| + |e_j\rangle\langle e_j| + |e_k\rangle\langle e_k|)$ of a Fano line and of a triple off the lines are both diagonal, have the same spectrum and $\mathcal{G}_{\text{total}} = 0$, so every functional of kinds (i) and (ii) takes one value on both, while $\mathcal A$ takes $0$ and $24/27$ (T-331(c)); subtracting gives $\kappa\cdot 24/27 = 0$. (iii) $\mathrm{PT}$ is complex conjugation and commutes with the real group $G_2$, so the $G_2$-average of the $\mathrm{PT}$-odd $V_3$ is a $\mathrm{PT}$-odd $G_2$-invariant cubic; by T-331(a) there is none. $\blacksquare$

The $G_2$-covariant dissipator of [Theorem 5.1c](/docs/proofs/gap/fano-channel#g2-ковариантность) does not single out $\mathcal A$ either: its cubic functionals $\mathrm{Tr}(\Gamma^2\mathcal D_{G_2}[\Gamma])$, $\mathrm{Tr}(\Gamma\,\mathcal D_{G_2}[\Gamma]^2)$ and $\mathrm{Tr}(\mathcal D_{G_2}[\Gamma]^3)$ are not of the form $\alpha\mathcal A$ plus spectral terms (least-squares residual $0.008$–$0.011$ on 60 random states against the span of $1$, $\mathrm{Tr}\,\Gamma^2$, $\mathrm{Tr}\,\Gamma^3$, $\mathcal A$).

The sources that remain are the holon's own dynamics — the living self-model $\varphi_J$ and its attractor, the Fano dissipator, the depth register — and the three-copy structure of composites. The next theorem closes all of them at once. Its reason is that $\mathcal A$ tells a Fano line from a triple off the lines, while the dynamics of an isolated holon treats every triple of axes alike: every pair of axes lies on exactly one line, so $\mathcal D_\Omega$ and $\mathcal P_\alpha$ are covariant under all $5040$ permutations of the axes ([Fano channel, Theorem 11.1](/docs/proofs/gap/fano-channel#s7-эквивариантность)), and the anchor $uu^\dagger$ of $\varphi_J$ is fixed by all of them ([T-334](/docs/core/operators/phi-operator#t-334), item 5).

<span id="t-331f"></span>

:::tip T-331(f): the associator is invisible to every source that does not resolve triples of axes [T]
**(a)** For every diagonal unitary $D$ the average of $\mathcal A(D\sigma\Gamma\sigma^{\mathsf T}D^\dagger)$ over the $5040$ axis permutations $\sigma$ — and already over the $720$ that fix one axis — is $\tfrac{96}{5}\,e_3(\Gamma)$, where $e_3$ is the third elementary symmetric function of the eigenvalues of $\Gamma$. Over the $168$ collineations, or over the $24$ permutations that fix three axes, the average is not spectral.

**(b)** Put $\mathcal A^\circ = \mathcal A - \tfrac{96}{5}e_3$ and, for any inner product on functionals of $\Gamma$ that is invariant under $U(7)$, $\kappa[F] := -\langle F, \mathcal A^\circ\rangle/\langle\mathcal A^\circ, \mathcal A^\circ\rangle$ — the associator weight of $F$. Then $\kappa[V_{\text{Gap}}] = \kappa$ for every such inner product, $\kappa[F] = 0$ for every function of the spectrum, and the $G_2$-average of $F$ has the weight of $F$. On real states the weight has a canonical version $\kappa_{\mathbb R}[F]$: the $G_2$-invariant cubics of a real traceless $\Delta$ are exactly two, $\mathrm{tr}\,\Delta^3$ and $\mathcal A(\Delta)$, and $\kappa_{\mathbb R}[F]$ is the coefficient of $-\mathcal A$ in the $G_2$-average of the cubic term of $F$ at $I/7$; $\kappa_{\mathbb R}[V_{\text{Gap}}] = \kappa$.

**(c)** $\kappa[F] = 0$ for every functional $F$ invariant under the permutations that fix one axis, in any phase gauge, and $\kappa_{\mathbb R}[F] = 0$ when the gauge is real. This covers every functional determined by the dynamics of an isolated holon — with $\varphi_{\mathrm{coh}}$, $\varphi_s$ or $\varphi_J$ (anchor $D\,uu^\dagger D^\dagger$, any $D$), the Fano dissipator, the gate $g_V$, a rate $\kappa(\Gamma) = \kappa_{\text{bootstrap}} + \kappa_0\,\mathrm{Coh}_E(\Gamma)$ and $H \in \mathrm{span}\{I, J\}$: Lyapunov functions averaged over the symmetry group, relative entropies to the attractors, quasi-potentials, histories on the depth register, and the cubic moments of $\mathcal D_\Omega$ as a superoperator. For a general Hamiltonian the weight of a functional $F_H$ built from the dynamics depends on $H$, and its average over the permuted Hamiltonians $\sigma H\sigma^{\mathsf T}$ is $0$.

**(d)** Weight is carried only by functionals that tell triples of axes apart, and its value is a property of the functional. The weights $\kappa_{\mathbb R}$: $\sum_p \det(\Gamma|_p)$ over the Fano lines $p$ — the cubic moment of the line resolution $\mathcal D_\Omega = \tfrac13\sum_p\mathcal D[\Pi_p]$ — has weight $1/144$; $\sum_p(\mathrm{Tr}\,\Pi_p\Delta)^3$ of the Fano readout $p_p = \mathrm{Tr}(\Pi_p\Gamma)/3$ has $1/72$, and the readout entropy $-\sum_p p_p\log p_p$ has $49/11664$; the calibration cubic $\langle\varphi|\Lambda^3\Gamma|\varphi\rangle/7$ has $1/168$. The axis resolution $\mathcal D_\Omega = \tfrac23\sum_i\mathcal D[\,|i\rangle\langle i|\,]$ of the same generator has weight $0$.

**(e)** A three-copy coupling $\mathrm{Tr}(K\,\Gamma^{\otimes 3})$ with $K = x_1\Pi_1 + x_7\Pi_7 + x_{27}\Pi_{27}$ $G_2$-invariant on $\Lambda^3\mathbb C^7 = \Lambda^3_1 \oplus \Lambda^3_7 \oplus \Lambda^3_{27}$ has $\kappa_{\mathbb R} = (x_1 - x_{27})/168 - (x_7 - x_{27})/96$: every value.
:::

**Proof.** (a) $\mathcal A = 96\,\mathrm{Tr}(\Pi_7\Lambda^3\Gamma)$, and conjugation by $M = D\sigma$ acts on $\Lambda^3\mathbb C^7$ by $\Lambda^3 M$; so the average is $96\,\mathrm{Tr}(\bar\Pi\,\Lambda^3\Gamma)$, where $\bar\Pi$, the group average of $(\Lambda^3M)^\dagger\Pi_7\Lambda^3M$, lies in the commutant of the group on $\Lambda^3\mathbb C^7$. Two facts about $\Pi_7$ decide it. First, $M \mapsto \mathrm{Tr}(\Pi_7\,d\Gamma(M))$, with $d\Gamma(M) = \frac{d}{dt}\Lambda^3(I + tM)|_{t=0}$, is a linear $G_2$-invariant functional on $\mathrm{End}\,\mathbb C^7 = (\mathbf 1 \oplus \mathbf 7 \oplus \mathbf{14} \oplus \mathbf{27})\otimes\mathbb C$, hence $3\,\mathrm{Tr}\,M$ ($d\Gamma(I) = 3$, $\mathrm{Tr}\,\Pi_7 = 7$); for a unit $w$, $E_w = d\Gamma(ww^\dagger)$ is the projector onto $w \wedge \Lambda^2 w^\perp$ and $\mathrm{Tr}(\Pi_7E_w) = 3$. Second, $\mathrm{Tr}(\Pi_7E_xE_w) = 1$ for orthonormal $x$ real and $w \perp x$: the pairing is $G_2$-invariant and bilinear in $xx^{\mathsf T}$ and $ww^\dagger$, sees only $\mathrm{Re}\,ww^\dagger$, and $G_2$ is transitive on orthonormal real pairs. For the axis permutations in the gauge $D$, $\Lambda^3\mathbb C^7 = w\wedge\Lambda^2w^\perp \oplus \Lambda^3w^\perp$ with $w = Du$ is the sum of the inequivalent irreducibles $\Lambda^2V_6$ ($15$) and $\Lambda^3V_6$ ($20$) of the standard representation $V_6$, so $\bar\Pi = \tfrac{3}{15}E_w + \tfrac{4}{20}(1 - E_w) = I/5$ and the average is $\tfrac{96}{5}\mathrm{Tr}\,\Lambda^3\Gamma = \tfrac{96}{5}e_3$. For the stabiliser of an axis $e$ the commutant is spanned by the projectors onto $e\wedge w'\wedge V_5$, $e\wedge\Lambda^2V_5$, $w'\wedge\Lambda^2V_5$, $\Lambda^3V_5$ ($w'$ the gauged unit sum of the other six axes) and two intertwiners, the nonzero blocks of $d\Gamma(w'e^\dagger)$ and $d\Gamma(ew'^\dagger)$; their traces with $\Pi_7$ are $1, 2, 2, 2$ and $3\langle e, w'\rangle = 0$ — one fifth of their traces — so again $\bar\Pi = I/5$. The last sentence is a finite computation (`test_axis_permutations_average_the_associator_to_a_spectral_cubic`). (b) An inner product invariant under $U(7)$ is invariant under the axis permutations, so for $F$ invariant under them $\langle F, \mathcal A^\circ\rangle = \langle F, \bar{\mathcal A}^\circ\rangle = 0$ by (a), $\bar{\mathcal A}^\circ$ the average; $\mathcal G_{\text{total}}$, $\mathcal G_{\text{total}}^2$ and functions of the spectrum are such, and $\langle\mathcal A, \mathcal A^\circ\rangle = \langle\mathcal A^\circ, \mathcal A^\circ\rangle$, which gives $\kappa[V_{\text{Gap}}] = \kappa$. $G_2$-averaging is self-adjoint and fixes $\mathcal A^\circ$. On real states the same holds for an $O(7)$-invariant inner product on cubics of $\Delta$, and with two invariant cubics the orthogonal projection onto $\mathcal A^\circ$ is the coefficient of $-\mathcal A$. The count of real cubics is the Weyl integration of [T-331(a)](#g2-инвариантный-кубик) (grading $(3, 0, 0)$: two). (c) If $F$ is invariant under the permutations fixing an axis in the gauge $D$, $\langle F, \mathcal A^\circ\rangle = \langle F\circ\mathrm{Ad}_D, \mathcal A^\circ\circ\mathrm{Ad}_D\rangle$ and the average of $\mathcal A^\circ\circ\mathrm{Ad}_D$ over those permutations vanishes by (a); in a real gauge the permutations keep the real states, and the same argument runs there. The listed dynamics are covariant under the permutations ($\mathrm{Coh}_E$ under those fixing $E$), so what they determine without a further choice is invariant, and a Lyapunov function stays one when averaged over the group, since the group maps trajectories to trajectories. For a Hamiltonian, covariance gives $F_{\sigma H\sigma^{\mathsf T}} = F_H\circ\mathrm{Ad}_{\sigma^{\mathsf T}}$, and the average of the weights is the weight of $F_H$ against $\bar{\mathcal A}^\circ = 0$. (d) For real $R$, $\langle\varphi|\Lambda^3R|\varphi\rangle + \mathcal A(R)/24 = e_3(R)$ — the identity $\varphi(x,y,z)^2 + |\chi(x,y,z)|^2 = |x\wedge y\wedge z|^2$ of associative calibration (R. Harvey, H. B. Lawson, "Calibrated geometries", *Acta Math.* **148** (1982) 47–157), with $[x,y,z] = 2\chi$, summed over the eigen-triples of $R$. $\sum_p\det(\Gamma|_p) = \mathrm{Tr}(E_L\Lambda^3\Gamma)$ with $E_L$ the projector onto the seven line vectors $e_p$; $\mathrm{Tr}(E_L\Pi_1) = 1$, $\mathrm{Tr}(E_L\Pi_7) = 0$ ($\mathcal A$ vanishes on line states), so its $G_2$-average is $\Pi_1 + \tfrac{6}{27}\Pi_{27}$ and on real states the weight is $\tfrac{1}{168} - \tfrac{6}{27}\bigl(\tfrac{1}{168} - \tfrac{1}{96}\bigr) = \tfrac{1}{144}$. The readout entropy has cubic term $\tfrac{49}{6}\sum_p\delta_p^3$, $\delta_p = \mathrm{Tr}(\Pi_p\Delta)/3$, hence weight $\tfrac{49}{162}\cdot\tfrac{1}{72}$. $\sum_p\Pi_p\Gamma\Pi_p = 2\,\mathrm{diag}\,\Gamma + \Gamma$ gives the line resolution of $\mathcal D_\Omega$; the other weights are computed by (b). (e) $\mathrm{Tr}(\Pi_1\Lambda^3\Gamma) = \langle\varphi|\Lambda^3\Gamma|\varphi\rangle/7$ and $\mathrm{Tr}(\Pi_{27}\Lambda^3\Gamma) = e_3 - \mathrm{Tr}(\Pi_1\Lambda^3\Gamma) - \mathcal A/96$, with (d). $\blacksquare$

Checks: `test_axis_permutations_average_the_associator_to_a_spectral_cubic`, `test_symmetric_sources_carry_no_associator_weight_and_fano_readouts_carry_any` (four permutation-invariant cubics have $\kappa_{\mathbb R}$ below $10^{-12}$ — three of them in a random complex gauge, where (c) proves only $\kappa = 0$; the four Fano weights to $10^{-12}$).

**What T-331(e)–(f) leave.** The dynamics of a holon does not know which triples of axes are Fano lines, so nothing it determines carries the associator; the Lyapunov route in particular fixes nothing — an unsymmetrised Lyapunov function is not unique, and near a hyperbolic sink $W + \varepsilon\mathcal A$ is again one for small $\varepsilon$. The associator enters only through a readout that resolves the lines, and then its weight belongs to the chosen functional of the readout ($1/144$, $1/72$, $49/11664$, $1/168$, and every value for three-copy couplings), for which the corpus has no principle. The three-copy structure of composites gives no value either: the canonical aggregation of holons is the mean of marginals and is linear ([Theorem 9.5 (a)](/docs/applied/coherence-cybernetics/theorems#теорема-95-каноническая-агрегация)), and the octonion product — the one aggregation that would compose associators — kills every uncoupled pair ([Theorem 9.6 (b)](/docs/applied/coherence-cybernetics/theorems#теорема-96-сильная-связь)). $\kappa$ stays a free coupling [T for the no-go], and with it the choice between the symmetric phase and the Gap phase (T-64 (b)–(d)).

### Analogy with the Higgs mechanism

| Aspect | Higgs (Standard Model) | $V_{\text{Gap}}$ (UHM) |
|---|---|---|
| Field | Scalar field $\phi$ | Coherence phases $\{\theta_{ij}\}$ |
| Potential | $V = -\mu^2\lvert\phi\rvert^2 + \lambda\lvert\phi\rvert^4$ | $V = V_2 + V_3 + V_4$ |
| Spontaneous breaking | $\langle\phi\rangle \neq 0$ (mass) | $\langle\mathrm{Gap}\rangle \neq 0$ (opacity) |
| Quantum number | Particle mass | Opacity (external/internal gap) |
| Cubic term | Absent (gauge symmetry) | **Present** (octonionic non-associativity) |

### PT-symmetry breaking

:::tip Corollary (PT-breaking from $V_3$) — [T] for the formula $V_3$; retracted [✗] for the vacuum potential
The cubic term $V_3$ **breaks** the discrete symmetry $\mathbb{Z}_2(\mathrm{PT}): \theta_{ij} \to -\theta_{ij}$. This means that "time" in the Gap sector has a preferred direction — octonionic non-associativity generates an **arrow of time** for interiority.
:::

*(Scope, 2026-09-25, [T-331](#g2-инвариантный-кубик): the first sentence is a property of the formula $V_3$, which is neither $G_2$- nor $\Gamma_{\!\text{oct}}$-invariant and averages to zero over $\Gamma_{\!\text{oct}}$. Every $G_2$-invariant cubic is PT-even, so the corrected potential is PT-even and its cubic term gives no arrow of time; the second sentence is retracted [✗]. The arrow of time of the corpus is the dissipative one of the depth register ([T-53b](/docs/proofs/dynamics/emergent-time#114-регистр-глубины)).)*

### Constants from UHM parameters {#константы-из-параметров-угм}

:::tip Theorem 13.5 (Relation of constants) [T]
The potential constants are expressed through UHM parameters:

$$
\mu^2 = \frac{1 - s^2}{2s^2}, \qquad \lambda_3 = \frac{2\mu^2}{3|\bar{\gamma}|}, \qquad \lambda_4 = \frac{\mu^2}{2\mathcal{G}^{(0)}_{\text{total}}}
$$

where:
- $s = P^{1/2}$ — square root of purity
- $|\bar{\gamma}|$ — mean modulus of coherences
- $\mathcal{G}^{(0)}_{\text{total}}$ — equilibrium total Gap
:::

### Potential minimum and spontaneous Gap {#минимум-потенциала-и-спонтанный-gap}

:::tip Theorem 13.6 (Spontaneous Gap) [T]
The minimum of the potential $V_{\text{Gap}}$ is achieved at:

$$
\mathcal{G}_{\text{total}}^{(\min)} = \frac{-\mu^2 + \sqrt{\mu^4 + 4\lambda_4 \lambda_3 \bar{A}}}{2\lambda_4} > 0
$$

where $\bar{A} = \sum_{(i,j,k) \notin \text{Fano}} |\gamma_{ij}||\gamma_{jk}||\gamma_{ik}|$ is the total amplitude of non-Fano triples.

**Corollary:** $\mathcal{G}_{\text{total}}^{(\min)} > 0$ — the potential minimum corresponds to a **nonzero** total Gap. Opacity arises **spontaneously**, analogously to spontaneous symmetry breaking in the Higgs mechanism.
:::

*(Scope, 2026-09-25: the formula concerns the retracted cubic $V_3$. For the $G_2$-invariant potential of §11 the Gap is spontaneous only above a threshold of the cubic coupling: never for $\kappa \le \mu^2/48$, always for $\kappa > \min(7\mu^2/48, \kappa_1)$ ([T-64](#теорема-глобальная-минимизация)).)*

### Five arguments for a minimum Gap

| # | Argument | Source | Mechanism |
|---|---|---|---|
| 1 | Octonionic associator | Theorem 3.2: $\mathrm{Gap} \geq C\lVert[\cdot,\cdot,\cdot]\rVert$ | Non-associativity of $\mathbb{O}$ generates Gap |
| 2 | Spontaneous breaking | Theorem 13.6: $\mathcal{G}_{\text{total}}^{(\min)} > 0$ | Cubic term $V_3$ shifts minimum away from zero |
| 3 | Phase frustration | $V_3$: impossibility of $\theta_{ij}+\theta_{jk}=\theta_{ik}$ globally | Non-associativity forbids global zeroing of $V_3$ |
| 4 | Thermodynamic | Theorem 5.2: $T_{\text{eff}} > 0 \Rightarrow$ nonzero entropic contribution | Thermal fluctuations maintain Gap |
| 5 | Self-referential | Theorem 10.2: a self-model with a real anchor registers the fraction $kc \leq 2/7$ of the Gap operator | $\mathrm{Gap}_{\text{perceived}} \neq \mathrm{Gap}_{\text{actual}}$ wherever $\hat{\mathcal G} \neq 0$ |

*(Rows 2 and 3 rest on the retracted cubic $V_3$ (2026-09-25). With the $G_2$-invariant potential, row 2 holds above the threshold of [T-64](#теорема-глобальная-минимизация) (d), and row 3 has no counterpart: the associator cubic depends on no phase combination and is PT-even.)*

---

## 12. Three influence channels $h_{\text{ext}}$ {#три-канала-h-ext}

### Channel classification

:::tip Theorem 12.1 (Three external influence channels) [T]
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

:::tip Theorem 12.2 (Geometry of external channels) [T]
In terms of the Serre bundle (section 1), the three channels act on different components:

| Channel | Action | Bundle component |
|---|---|---|
| $h^{(H)}$ | Rotates the fiber | Horizontal lift |
| $h^{(D)}$ | Contracts the fiber | Metric scaling |
| $h^{(R)}$ | Deforms the base | Change of target section |
:::

### Operational formulas

:::tip Theorem 12.3 (Operational formulas for systems) [T]
For specific types of systems the channels are specified as:

| System | $h^{(H)}$ | $h^{(D)}$ | $h^{(R)}$ |
|---|---|---|---|
| **Neuro** | $\delta\omega_{ij}$ from neuromodulators | $\delta\Gamma_2$ from brain temperature | $\delta\kappa$ from neuroplasticity |
| **Psycho** | Cognitive load | Stress level | Therapeutic alliance |
| **AI** | $\delta(\text{learning rate})$ | $\delta(\text{regularization})$ | $\delta(\text{target distribution})$ |
:::

### Operational FDT with $h_{\text{ext}}$

:::tip Theorem 12.4 (Operational FDT) [T]
In the presence of an external field $h^{\text{ext}}$ the FDT takes the form:

$$
\langle \delta\mathrm{Gap}(i,j) \rangle_{h} = \sum_{(k,l)} \chi_{(ij),(kl)}(\omega) \cdot h^{\text{ext}}_{kl}(\omega)
$$

where $\chi_{(ij),(kl)}$ is the full susceptibility matrix, linking the Gap$(i,j)$ response to the influence in channel $(k,l)$.
:::

### Experimental FDT verification protocol

:::caution Program (FDT verification) [P]
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

:::tip Theorem 15.1 ($T_{\text{eff}}$ does not equal $T_{\text{phys}}$) [C]
The effective temperature of the Gap sector **does not coincide** with the physical temperature of the system.

**Proof by contradiction.** Suppose $T_{\text{eff}} = T_{\text{phys}}$. Then from the FDT (Theorem 6.1):

$$
\chi_{ij}(0) = \frac{\langle(\delta\mathrm{Gap})^2\rangle}{T_{\text{phys}}}
$$

But for living systems at $T_{\text{phys}} \approx 310$ K the observed Gap fluctuations **exceed thermal ones by orders of magnitude**. Contradiction.
:::

:::warning Status [C]
The argument uses an empirical observation (Gap fluctuations exceed thermal ones) and assumes the applicability of the FDT to the Gap sector. Rigor depends on FDT verification for specific neurobiological systems.
:::

### Definition of $T_{\text{eff}}$

:::tip Definition 15.2 (Effective temperature formula) [D]

$$
T_{\text{eff}} := \frac{\Gamma_2}{\kappa_0} \cdot k_B T_{\text{phys}}
$$

where:
- $\Gamma_2$ — decoherence rate (dissipation)
- $\kappa_0$ — regeneration rate (recovery)
- $k_B T_{\text{phys}}$ — physical thermal energy
:::

### Physical interpretation

:::tip Theorem 15.3 (Properties of $T_{\text{eff}}$) [T]
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

:::info Interpretation (Energetics of enlightenment) [I]
For a typical brain ($\Gamma_2/\kappa_0 \sim 10^3$, $T_{\text{phys}} = 310$ K):

$$
W_{\text{enlightenment}} \sim 21 \times 10^3 \times 4.3 \times 10^{-21} \text{ J} \times 0.69 \approx 6 \times 10^{-17} \text{ J}
$$

This is negligibly small in absolute units, but may be large relative to the "Gap energy budget" of the system.
:::

### $T_{\text{eff}}$ as an order parameter

:::tip Theorem 15.4 (Phase transition) [C]
Provided the potential $V_{\text{Gap}}$ is valid (Theorem 13.4, status [T]), the total Gap depends on $T_{\text{eff}}$ as an order parameter near the critical temperature:

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

:::warning Hypothesis (Critical temperature and levels of consciousness) [H]
Levels L1--L4 of the [interiority hierarchy](/docs/consciousness/hierarchy/interiority-hierarchy) may correspond to different regimes relative to $T_c$:
- L1--L2: $T_{\text{eff}} \ll T_c$ (deep in ordered phase, large Gap)
- L3: $T_{\text{eff}} \lesssim T_c$ (near transition, critical fluctuations)
- L4: $T_{\text{eff}} \to T_c$ (at the boundary — paradox: transparency, but not at the cost of losing coherence)
:::

### Categorical derivation of $T_{\text{eff}}$ from adjunction

:::tip Theorem 15.5 (Categorical formula for $T_{\text{eff}}$) [C]
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

### Theorem (Self-consistent vacuum equation) [T] {#теорема-самосогласованное-вакуумное-уравнение}

:::tip Theorem 14.1 (Homogeneous vacuum is not an exact solution) [T]
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
P = \mathrm{Tr}(\Gamma^2) = \frac{1}{7} + 42\varepsilon^2, \qquad \mu^2 = \frac{1-P}{2P} = \frac{6/7 - 42\varepsilon^2}{2/7 + 84\varepsilon^2}
$$

*(Erratum 2026-08-10, instrument E26: for a Hermitian $\Gamma$ with $|\gamma_{ij}| = \varepsilon$ on all $21$ pairs each pair contributes $|\gamma_{ij}|^2 + |\gamma_{ji}|^2 = 2\varepsilon^2$ to $\mathrm{Tr}(\Gamma^2)$, so the off-diagonal mass is $42\varepsilon^2$, not $21\varepsilon^2$; the earlier line mixed the two conventions between its numerator and denominator. The contradiction $1 = 2/3$ of this theorem survives the fix — the homogeneous vacuum remains excluded.)*

**Step 4.** Substituting the equilibrium Gap $\mathcal{G}^{(\min)}_{\text{total}} = 21\varepsilon^2\sin^2\bar{\theta}$ from [Theorem 13.6](#минимум-потенциала-и-спонтанный-gap) into the self-consistency condition, we obtain:

$$
1 = 2/3 \quad \text{— CONTRADICTION}
$$

**Conclusion.** The homogeneous vacuum is not an exact solution. The vacuum has a **sector structure**: different $\varepsilon$ in different sectors of the $7 \times 7$ matrix. $\blacksquare$

:::info Status [T]
The proof uses the definitions of constants $\lambda_3, \lambda_4$ from Theorem 13.5 and the spontaneous Gap formula from Theorem 13.6 (both [T]). The uniqueness of the self-consistent vacuum, which the next theorem claimed from the positive definiteness of a Hessian, holds for the retracted cubic $V_3$ only up to its symmetries and only numerically; for the $G_2$-invariant potential it holds up to $G_2$ (T-64 corrected, see below); the exclusion of the homogeneous vacuum does not depend on it. The "sector structure" in the conclusion means only that the vacuum is not homogeneous: no split into sectors follows from this proof.
:::

#### Theorem (Unique self-consistent vacuum) — corrected: for the $G_2$-invariant potential unique up to $G_2$ [T], without sector structure [✗] {#теорема-единственный-вакуум}

:::danger Corrected 2026-09-25 (audit A-90)
The statement below claimed a unique vacuum with the sector values of hypothesis (SV). Three repairs were tried; what survives is weaker.

1. **Axis sectors.** The sectors $\{A,S,D\}$ and $\{L,E,U\}$ are the axis triples of T-48a, retracted: no triple of axes is $SU(3)$-invariant (0 of 20), and the triplet is $\mathbf 3 = \mathrm{span}_{\mathbb C}\{A-iD,\,S-iU,\,L-iE\}$.
2. **Correct complex triplets.** The $SU(3)_C$-invariant states are $\Gamma = a\,|O\rangle\langle O| + b\,P_{\mathbf 3} + c\,P_{\bar{\mathbf 3}}$. Their only coherences sit on the pairs $(A,D)$, $(S,U)$, $(L,E)$, all of modulus $\delta = \lvert b-c\rvert/2$; on them $V_3 \equiv 0$ and $V_{\text{Gap}} = 6\mu^2\delta^2 + 36\lambda_4\delta^4$, minimal at $\delta = 0$, that is at $\mathcal{G}_{\text{total}} = 0$ (`test_su3_invariant_vacuum_has_no_spontaneous_gap`). A vacuum that keeps colour has no spontaneous Gap and none of the sector values below.
3. **No sector ansatz; Fano lines instead.** Minimised over all of $\mathcal D(\mathbb C^7)$ with the self-consistent constants of Theorem 13.5, the vacuum is unique up to the 896 symmetries of $V_{\text{Gap}}$ (numerically) and sits on two Fano lines through one point, not on $SU(3)$ sectors — see T-64 below.

What stands: Theorem 14.1 [T] (the homogeneous vacuum is not a stationary point); uniqueness of the self-consistent vacuum up to the symmetries of $V_{\text{Gap}}$ — the numerically supported hypothesis T-64 [H]. Retracted [✗]: the sector structure of the vacuum and the uniqueness modulo $G_2$. The sector values are the named hypothesis [(SV)](#гипотеза-секторного-вакуума) [H].
:::

*(Update 2026-09-25, T-64 corrected: the three repairs above used the retracted cubic $V_3$. With the $G_2$-invariant potential of §11 the vacuum is unique up to $G_2$ for every $\kappa > 0$ off the transition curves [T]: the point $I/7$ in the symmetric phase (always for $\kappa \le \mu^2/48$), one orbit $S^6$ of colour-invariant states in the Gap phase; on a transition curve two orbits coexist (T-64 (g); [(RT)](#теорема-ву) proven 2026-09-25). Repair 2 then works: the colour-invariant family does carry a spontaneous Gap, because the associator cubic, unlike $V_3$, does not vanish on it. The sector values remain the hypothesis (SV), which this vacuum does not produce. The self-consistency relations of Theorem 13.5 were derived for $V_3$ and are not claimed for $\kappa$.)*


*Earlier statement (retracted):* $V_{\text{Gap}}$ has a unique minimum (up to $G_2$-conjugation) on the 21-dimensional space of coherences $\{\gamma_{ij}\}$ with the sector structure $7 = 1_O \oplus 3 \oplus \bar{3}$.

**Sector values:** $\varepsilon_{3\to\bar{3}} \approx 0$ (confinement), $\varepsilon_{\bar{3}\to\bar{3}} \approx 10^{-17}$ (electroweak), $\varepsilon_{33} \approx 0.06$ (Yukawa hierarchy), $\bar{\varepsilon} \approx 0.023$ (mean coherence).

:::warning Sector coherence notation (earlier, axis-labelled sectors — see the retraction above)
- $\varepsilon_{3\to\bar{3}}$ — coherence between the **confinement sector** ($\{A,S,D\}$) and the **electroweak sector** ($\{L,E,U\}$), suppressed by confinement → $\approx 0$
- $\varepsilon_{\bar{3}\to\bar{3}}$ — coherence **within** the electroweak sector, suppressed by electroweak symmetry breaking → $\approx 10^{-17}$
- $\bar{\varepsilon} \approx 0.023$ — **weighted mean** of sector coherences (not to be confused with $\varepsilon_O$ — coherence of the O-sector, which is $\sim 1$)
:::

*(Earlier argument, retracted: "uniqueness follows from the positive definiteness of the Hessian $\partial^2 V_{\text{Gap}} / \partial \varepsilon_X \partial \varepsilon_Y$ at the minimum point". The Hessian was taken in five axis-sector variables, which do not parametrise the states; a positive-definite Hessian at one point would in any case give a local, not a global, statement.)*

#### Theorem T-64 (Global minimisation of $V_{\text{Gap}}$) — corrected to the $G_2$-invariant potential [T]; the axis-frame statement [H]; the $G_2$-reduction retracted [✗] {#теорема-глобальная-минимизация}

The potential is the $G_2$-invariant one of [§11](#g2-инвариантный-кубик): $V = \mu^2\mathcal{G}_{\text{total}} + \lambda_4\mathcal{G}_{\text{total}}^2 - \kappa\mathcal A$ on $\mathcal D(\mathbb C^7)$, with $\mu^2 > 0$, $\lambda_4 \ge 0$ and $\kappa$ real. For a unit $v \in \mathbb R^7$ let $P_{\mathbf 3}(v)$, $P_{\bar{\mathbf 3}}(v)$ be the projectors onto the $\mp i$-eigenspaces of $L_v$ on $v^\perp$ (the colour triplet and antitriplet of $\mathrm{SU}(3)_v = \mathrm{Stab}_{G_2}(v)$), and call the states $a|v\rangle\langle v| + b P_{\mathbf 3}(v) + c P_{\bar{\mathbf 3}}(v)$, $a + 3b + 3c = 1$, the **colour-invariant sector** of $v$.

:::tip T-64 (corrected 2026-09-25; (RT) proven the same day): the vacuum of the $G_2$-invariant $V_{\text{Gap}}$ [T]
**(a) [T]** If $\kappa \le 0$, then $\min V = 0$, attained exactly on the real states with $\kappa\mathcal A = 0$; the real pure states — a whole $G_2$-orbit $\mathbb{RP}^6$ — are among them. No Gap is spontaneous and the vacuum is not unique up to $G_2$.

**(b) [T]** If $0 < \kappa \le \mu^2/48$, the state $I/7$ is the unique global minimum. The vacuum has $\mathcal{G}_{\text{total}} = 0$ and keeps all of $G_2$, colour included.

**(c) [T]** $I/7$ is a critical point for every $\kappa$. Its Hessian has the eigenvalues $96\kappa/7$ on $\mathbf{27}$, $2\mu^2 - 96\kappa/7$ on $\mathbf 7$ and $2\mu^2 + 192\kappa/7$ on $\mathbf{14}$. For $\kappa > 0$ it is a strict local minimum exactly when $\kappa < 7\mu^2/48$; above that value $V$ descends from $I/7$ along $X \propto L_v$, a direction whose stabiliser is $\mathrm{SU}(3)_v$.

**(d) [T]** If $\kappa > \min(7\mu^2/48,\ \kappa_1)$, every global minimiser has $\mathcal{G}_{\text{total}} > 0$: the Gap is spontaneous. Here $\kappa_1(\lambda_4/\mu^2)$ is the smallest $\kappa$ at which some colour-invariant state has $V < -672\kappa/343$: $\kappa_1 = 0.0787\mu^2$, $0.0842\mu^2$, $0.1054\mu^2$ at $\lambda_4/\mu^2 = 0, 1, 5$, and $\kappa_1 = 7\mu^2/48$ for $\lambda_4 \ge \lambda_* = 12.93\mu^2$.

**(e) [T]** On the colour-invariant sector $\mathcal A = 48(b+c)^3 + 144a(b^2+c^2)$ and $\mathcal{G}_{\text{total}} = \tfrac32(b-c)^2$. The minimum of $V$ over the sector is $I/7$ for $\kappa \le \kappa_1$; for $\kappa > \kappa_1$ it has $b \neq c$: rank 4 with $c = 0$ (the branch $b = s$, $V = \tfrac32\mu^2 s^2 + \tfrac94\lambda_4 s^4 - \kappa(144s^2 - 384s^3)$) when $\lambda_4 < \lambda_*$ or $\kappa > \kappa_2(\lambda_4)$, and rank 7 ($bc > 0$) when $\lambda_4 > \lambda_*$ and $7\mu^2/48 < \kappa < \kappa_2(\lambda_4)$. At $\kappa_2$ the minimiser jumps from the rank-7 to the rank-4 branch: $\kappa_2 = 0.1514$, $0.1854$, $0.2458$, $0.3696$, $0.6818$, $1.934$, $6.319$ (in units of $\mu^2$) at $\lambda_4/\mu^2 = 14, 20, 30, 50, 100, 300, 1000$. Such a state $\Gamma_v$ has stabiliser exactly $\mathrm{SU}(3)_v$ in $G_2$ (when $a \notin \{b, c\}$), its orbit is $G_2/\mathrm{SU}(3) \cong S^6$, and $\mathrm{PT}$ maps $\Gamma_v$ to $\Gamma_{-v}$ in the same orbit.

**(f) [T]** Reduction. Let $\Gamma = R + iX$ with $X_7 = L_w$, $w = \rho\hat w$ (any unit $\hat w$ if $w = 0$), and $\kappa > 0$. Then $V(\Gamma) \ge V(\mathcal T_{\hat w}\Gamma)$, where $\mathcal T_{\hat w}$ averages over $\mathrm{SU}(3)_{\hat w}$ and lands in the colour-invariant sector of $\hat w$, with equality only if $\Gamma = \mathcal T_{\hat w}\Gamma$. The key step is the real twirl inequality (RT), Lemma 3 below.

**(g) [T]** Hence, for every $\kappa > 0$, the set of vacua is the union of the $G_2$-orbits of the minimisers of the sector problem (e): the point $I/7$ in the symmetric phase, one orbit $S^6 = G_2/\mathrm{SU}(3)$ in the Gap phase. Two orbits coexist on the transition curves: $\kappa = \kappa_1(\lambda_4)$ for $\lambda_4 < \lambda_*$ ($I/7$ and an $S^6$) and $\kappa = \kappa_2(\lambda_4)$ for $\lambda_4 > \lambda_*$ (the rank-7 and the rank-4 orbit); off these curves the sector minimiser is unique on the scanned range ($\lambda_4/\mu^2$ from $0$ to $1000$, $\kappa/\mu^2$ from $0.05$ to $5$), so the vacuum is unique up to $G_2$. The Gap is spontaneous exactly above $\kappa_c = \kappa_1$ (first order, a jump from $I/7$, for $\lambda_4 < \lambda_*$) or $\kappa_c = 7\mu^2/48$ (continuous, for $\lambda_4 \ge \lambda_*$). Colour — the stabiliser $\mathrm{SU}(3)_v$ of the vacuum direction, $v = e_O$ in the corpus frame — is unbroken, and $G_2$ breaks to it.
:::

<a id="теорема-ву"></a>

:::tip Lemma 3 (RT): the real twirl inequality [T]
For every real state $R \in \mathcal D(\mathbb R^7)$ and unit $\hat w$: $\mathcal A(R) \le 8rt^2 + \tfrac{16}{9}t^3$, where $r = \langle\hat w, R\hat w\rangle$ and $t = 1 - r$. The right-hand side is $\mathcal A(\mathcal T_{\hat w}R)$: twirling a real state over $\mathrm{SU}(3)_{\hat w}$ never lowers $\mathcal A$. Equality holds only for $R = \mathcal T_{\hat w}R = r\,\hat w\hat w^{\mathsf T} + \tfrac t6(I - \hat w\hat w^{\mathsf T})$. At $r = 1/7$ this is Lemma 1 below.
:::

*(Status history: stated 2026-09-25 as hypothesis (RT) [H], proven then only for $\beta = 0$ and for $M^- = 0$ in the notation of the proof of (f), and supported by 288 minimisations of its defect; proven in general the same day, below. A relaxation through the eigenvalues of $R$ alone fails by $0.015$, because it forgets how the eigenvectors of $R$ sit relative to $\hat w$; the proof keeps them by linearising in one slot of $\mathcal A$.)*

**Proof.** *Lemma 1 (real states).* For real $R = \sum_m p_m u_m u_m^{\mathsf T}$ the associator of orthonormal real vectors satisfies $\lVert[x,y,z]\rVert^2 = 4(1 - \varphi(x,y,z)^2)$ (Harvey–Lawson), and for each $m$ the cross product $J_m = L_{u_m}$ is a complex structure on $u_m^\perp$. Summing over the eigenbasis gives the identity $\mathcal A(R) = 4\sum_m p_m\big[(1-p_m)^2 - 2\lVert R^+_m\rVert^2\big]$, where $R^+_m$ is the part of $R|_{u_m^\perp}$ commuting with $J_m$. Cauchy–Schwarz gives $\lVert R^+_m\rVert^2 \ge (1-p_m)^2/6$, so $\mathcal A(R) \le \tfrac83\sum_m p_m(1-p_m)^2$. The function $p(1-p)^2$ is concave on $[0, 2/3]$, so the sum is at most $7\cdot\tfrac17\cdot\tfrac{36}{49}$ when all $p_m \le 2/3$, with equality only at $p_m = 1/7$; if some $p_m > 2/3$ the sum is below $\tfrac{2}{27} + \tfrac13$. Hence $\mathcal A(R) \le 672/343$ on real states, with equality only at $I/7$.

*Lemma 3 (RT).* Write $\mathcal A(X,Y,Z)$ for the symmetric trilinear form with $\mathcal A(R,R,R) = \mathcal A(R)$, and $\mathcal T = \mathcal T_{\hat w}$. On real symmetric matrices $\mathcal T R = r\,\hat w\hat w^{\mathsf T} + \tfrac t6 P$, $P = I - \hat w\hat w^{\mathsf T}$, is the orthogonal projection onto the $\mathrm{SU}(3)_{\hat w}$-invariants $\mathrm{span}\{\hat w\hat w^{\mathsf T}, P\}$. Put $\Delta = R - \mathcal TR$. The linear functional $\mathcal A(\mathcal TR, \mathcal TR, \cdot)$ is invariant, so it vanishes on $\Delta$, and expanding $\mathcal A(\mathcal TR + \Delta)$ gives the identity

$$
8rt^2 + \tfrac{16}{9}t^3 - \mathcal A(R) = -2\mathcal A(\mathcal TR,\Delta,\Delta) - \mathcal A(R,\Delta,\Delta) = \sum_m p_m\,Q_{u_m}(\Delta),
$$

where $R = \sum_m p_m u_mu_m^{\mathsf T}$ and, for a unit vector $u$, $Q_u(Y) = -2\mathcal A(\mathcal T(uu^{\mathsf T}),Y,Y) - \mathcal A(uu^{\mathsf T},Y,Y)$ — the middle expression is linear in $R$ at fixed $\Delta$. It therefore suffices that $Q_u \ge 0$ on the 26-dimensional space $W$ of real symmetric matrices orthogonal to $\hat w\hat w^{\mathsf T}$ and $P$. The form $Q_u$ is covariant under $\mathrm{SU}(3)_{\hat w}$, which is transitive on the unit sphere of $\hat w^\perp$, so one may take $u = c\,\hat w + s\,d$ with a fixed unit $d \perp \hat w$, $c^2 = \langle u, \hat w\rangle^2$, $s^2 = 1 - c^2$. In the Frobenius metric the spectrum of $Q_u$ on $W$ is $16s^2/3$ (ten times) together with the roots of

$$
9\lambda^2 - (216c^2 + 96s^2)\lambda + 768c^2s^2 + 160s^4 \ \ (\text{once}), \qquad 9\lambda^2 - (216c^2 + 144s^2)\lambda + 2016c^2s^2 + 368s^4 \ \ (\text{four times}),
$$

$$
9\lambda^2 - (216c^2 + 144s^2)\lambda + 2304c^2s^2 + 320s^4 \ \ (\text{three times}).
$$

This is an exact computation: in the basis of $W$ made of coordinate matrices adapted to the axes $\hat w$, $d$, $L_{\hat w}d$ and the four remaining axes, the Gram matrix of $Q_u$ is block-diagonal with blocks of sizes 5, 12 and 9 whose entries are integer combinations of $c^2$, $cs$, $s^2$ (the associator has entries $0$, $\pm 2$), and $\det(Q_u - \lambda G)$ factors as displayed ($G$ the Gram matrix of the basis). Each quadratic has real roots with positive sum and non-negative product, so $Q_u \ge 0$, and $Q_u > 0$ for $s \ne 0$; at $s = 0$ the eigenvalues are $0$ (18 times) and $24$ (8 times). Equality: if the defect vanishes, $Q_{u_m}(\Delta) = 0$ for every $m$ with $p_m > 0$; if $\Delta \ne 0$ this forces all those $u_m = \pm\hat w$, so $R = r\,\hat w\hat w^{\mathsf T} = \mathcal TR$ and $\Delta = 0$ — a contradiction. $\square$

*Lemma 2 (coupling).* Every $G_2$-invariant cubic is $\mathrm{PT}$-even (T-331), so $\mathcal A(R + iX) = \mathcal A(R) + Q_R(X)$ with $Q_R$ quadratic in $X$ and linear in $R$. For $R = uu^{\mathsf T}$ the form $Q_R$ has the eigenvalues $48$ (once, on $L_u$), $0$ (twelve times) and $-24$ (eight times, on $\mathfrak{su}(3)_u$) — computed at $u = e_O$ and carried to every $u$ by the transitivity of $G_2$ on $S^6$. Hence $Q_R(X) \le 48\lVert X\rVert^2$ for every state $R$, and $Q_R(X) \le 288\,w^{\mathsf T}Rw$ when $X_7 = L_w$ (use $\langle L_w, L_u\rangle_F = 6\langle w, u\rangle$).

(a) $\mathcal A \ge 0$, so $V \ge \mu^2\mathcal{G}_{\text{total}} + \lambda_4\mathcal{G}_{\text{total}}^2 \ge 0$ for $\kappa \le 0$, with equality iff $X = 0$ and $\kappa\mathcal A = 0$; $\Lambda^3$ of a rank-one state vanishes. (b) By Lemmas 1 and 2, $V \ge -\tfrac{672}{343}\kappa + (\mu^2 - 48\kappa)\mathcal{G}_{\text{total}} + \lambda_4\mathcal{G}_{\text{total}}^2 \ge V(I/7)$ for $0 < \kappa \le \mu^2/48$; equality forces $R = I/7$ and then $X = 0$, since $Q_{I/7}(X) < 48\lVert X\rVert^2$ for $X \ne 0$. (c) The gradient at $I/7$ is a $G_2$-invariant traceless Hermitian matrix; $\mathbf{27}$, $\mathbf 7$ and $\mathbf{14}$ contain no invariant, so it vanishes. By Schur's lemma the second variation of $\mathcal A$ is a scalar on each of the three: $-48/7$, $+48/7$, $-96/7$ (the last two also follow from Lemma 2, since $Q_{I/7} = \tfrac17\sum_m Q_{e_me_m^{\mathsf T}}$ has trace $48$ on $\mathbf 7$ and $-192$ on $\mathbf{14}$). (d) If $\kappa > 7\mu^2/48$, $I/7$ is not a local minimum, so $\inf V < V(I/7) = -\tfrac{672}{343}\kappa$, while $V(R) = -\kappa\mathcal A(R) \ge -\tfrac{672}{343}\kappa$ for every real $R$ by Lemma 1; a minimiser exists because $V$ is continuous on the compact $\mathcal D(\mathbb C^7)$, and it is not real. If $\kappa > \kappa_1$, a colour-invariant state already lies below $-\tfrac{672}{343}\kappa$. (e) Direct evaluation in the eigenbasis $v$, $\mathbf 3$, $\bar{\mathbf 3}$; with $s = b + c$, $d = b - c$ the sector potential is $\tfrac32\mu^2d^2 + \tfrac94\lambda_4d^4 - \kappa[48s^3 + 72(1-3s)(s^2+d^2)]$ on $0 \le |d| \le s \le 1/3$, quadratic in $d^2$ at fixed $s$. If $g \in G_2$ fixes $\Gamma_v$, it preserves the eigenline of $a$, so $gv = \pm v$; $gv = -v$ would exchange $P_{\mathbf 3}$ and $P_{\bar{\mathbf 3}}$ (because $L_{-v} = -L_v$), which changes $\Gamma_v$ when $b \ne c$. (f) The twirl keeps $r$, replaces $R|_{\hat w^\perp}$ by $\tfrac t6 I$, kills $X_{14}$ and the part of $X_7$ orthogonal to $L_{\hat w}$ (there is no $\mathrm{SU}(3)$-singlet in $\mathbf{14}$ or in $\mathbf 3\oplus\bar{\mathbf 3}$), and keeps $L_w$; so $\mathcal{G}_{\text{total}}(\mathcal T_{\hat w}\Gamma) = 6\rho^2 \le \mathcal{G}_{\text{total}}(\Gamma)$. The operators $(P \pm iL_{\hat w})/2$, $P = I - \hat w\hat w^{\mathsf T}$, are orthogonal projectors, so $\mathrm{Tr}\,\Gamma(P \pm iL_{\hat w}) \ge 0$, i.e. $6\rho \le t$. By Lemma 2 and Lemma 3, $\mathcal A(\Gamma) \le 8rt^2 + \tfrac{16}{9}t^3 + 288\rho^2 r$, and by (e) the right-hand side is $\mathcal A(\mathcal T_{\hat w}\Gamma)$; so $V(\Gamma) \ge V(\mathcal T_{\hat w}\Gamma)$ for $\kappa > 0$, and equality forces $\mathcal{G}_{\text{total}}(\Gamma) = 6\rho^2$ (so $X = L_w$) and equality in Lemma 3 (so $R = \mathcal T_{\hat w}R$), that is $\Gamma = \mathcal T_{\hat w}\Gamma$; if $w = 0$ it forces $X = 0$ and $R = \mathcal T_{\hat w}R$ for every $\hat w$, that is $\Gamma = I/7$. The two special cases proven first, superseded by Lemma 3 and still checked: write $R = \begin{pmatrix} M & \beta \\ \beta^{\mathsf T} & r\end{pmatrix}$ in $\hat w^\perp \oplus \mathbb R\hat w$ and split $M = M^+ + M^-$ into the parts commuting and anticommuting with $L_{\hat w}$. If $\beta = 0$, then $\mathcal A(R) = 12r(t^2 - 2\lVert M^+\rVert^2) + \mathcal A(M)$ (the terms with $\hat w$ once, by the Harvey–Lawson identity), $\lVert M^+\rVert^2 \ge t^2/6$, and $\mathcal A(M) \le \tfrac{16}{9}t^3$: the identity of Lemma 1 on $\hat w^\perp$, with $q_m = \langle L_{\hat w}u_m, M L_{\hat w}u_m\rangle$, $\sum_m q_m = t$, and Cauchy–Schwarz on the 4-planes $\{u_m, L_{\hat w}u_m\}^\perp$, reduces it, after maximising over the $q_m$, to $\sum_m p_m(1-p_m)^2 - 1/\sum_m p_m^{-1} \le 2/3$ on the open 6-simplex (smaller supports give less); with $\delta_m = p_m - \tfrac16$ this reads $\sum_m \delta_m^2/p_m \le \sum_k p_k^{-1}\cdot\sum_m\delta_m^2(\tfrac32 - \delta_m)$, which holds term by term. If $M^- = 0$, the defect equals $24r(\lVert M^+\rVert^2 - t^2/6) + 24\beta^{\mathsf T}(tI - 2M^+)\beta + 8\,\mathrm{Tr}(M^+)^3 - \tfrac29t^3$ (a cubic identity, checked at random points), and each term is non-negative: the eigenvalues of $M^+$ come in pairs, so none exceeds $t/2$, and $\mathrm{Tr}(M^+)^3 \ge t^3/36$ by the power mean. (g) By (f) every global minimiser equals its own twirl, so it lies in a colour-invariant sector, and by $G_2$-transitivity on $S^6$ all sectors are conjugate; the rest is (e). $\blacksquare$

Checks in `website/scripts/check_core_numbers.py`: `test_real_states_obey_the_associator_identity_and_peak_at_i_over_7`, `test_symmetric_vacuum_hessian_and_the_associator_coupling`, `test_colour_invariant_sector_is_solved_in_closed_form`, `test_g2_invariant_vacuum_is_symmetric_or_colour_invariant_with_gap`, `test_real_twirl_inequality_holds_in_its_proven_cases_and_on_samples`, `test_real_twirl_inequality_is_a_sum_of_positive_forms`, `test_colour_sector_transitions_and_the_bound_on_mean_coherence`. Beyond them: the global minimisation over all of $\mathcal D(\mathbb C^7)$ at 36 parameter points ($\lambda_4/\mu^2 \in \{0, 1, 30\}$, twelve values of $\kappa/\mu^2$ from $0.01$ to $2$, 16 starts each, analytic gradient) reaches the sector minimum at every point, to $10^{-15}$, with stabiliser 14 ($I/7$) or 8 ($\mathrm{SU}(3)_v$) and never below it. At four points in the Gap phase the Hessian in the 98 real coordinates of $A$, $\Gamma = AA^\dagger/\mathrm{Tr}$, has no negative eigenvalue; its zero modes are exactly the gauge directions of $A$ plus the six directions of the orbit $S^6$ (47 zero and 51 positive at rank 4, 56 and 42 at rank 7).

**Consequences.** (i) The vacuum of the $G_2$-invariant potential has none of the (SV) values. At $I/7$ all coherences vanish; in the Gap phase $\Gamma_v$ written in the axis basis with $v = e_O$ is $a|O\rangle\langle O| + \tfrac{b+c}{2}(I - |O\rangle\langle O|) + i\tfrac{b-c}{2}L_{e_O}$: its only coherences sit on $(A,D)$, $(S,U)$, $(L,E)$, of modulus $|b-c|/2$, and the $O$-coherences are zero, not $\sim 1$. (ii) Its non-$O$ root-mean-square coherence is $\bar\varepsilon = |b-c|/(2\sqrt5)$: zero in the symmetric phase and, for every $\kappa > 0$ and $\lambda_4 \ge 0$, $\bar\varepsilon \le \tfrac{1}{2\sqrt5}\big(\tfrac14 - \tfrac{\mu^2}{384\kappa}\big) < \tfrac{\sqrt5}{40} \approx 0.0559$, the supremum being approached as $\kappa/\mu^2 \to \infty$. Proof: the feasible set $0 \le d^2 \le s^2 \le 1/9$ of (e) does not depend on $\lambda_4$ and the sector potential grows with $\lambda_4$ by $\tfrac94\lambda_4d^4$, so comparing $V$ at minimisers for $\lambda_4' > \lambda_4$ gives $\tfrac94(\lambda_4' - \lambda_4)(d'^4 - d^4) \le 0$: $d^2$ at a minimiser does not increase with $\lambda_4$. At $\lambda_4 = 0$ the minimiser is $I/7$ or the rank-4 branch with $b = s = \tfrac14 - \tfrac{\mu^2}{384\kappa}$. (iii) $V$ is $\mathrm{PT}$-even and its vacuum set is $\mathrm{PT}$-invariant; $I/7$ is $\mathrm{PT}$-invariant, and $\Gamma_v$ is invariant under the antiunitary $\Theta_v = g_v\circ\mathrm{PT}$ for any $g_v \in G_2$ with $g_vv = -v$. (iv) The vacuum manifold is $S^6$, with $\pi_1 = \pi_2 = 0$ — not the $G_2/T^2$ of T-69.

##### Axis-frame record: the retracted cubic $V_3$ {#t64-осевая-запись}

:::danger Corrected 2026-09-25 (audit A-90): with the cubic $V_3$ of §11 the minimum is not unique modulo $G_2$ and has no sector structure
Checked with the page's own potential, $V_{\text{Gap}} = \mu^2\mathcal{G}_{\text{total}} + 2\lambda_3\sum_{(i,j,k)\notin\text{Fano}} \mathrm{Im}(\gamma_{ij}\gamma_{jk}\gamma_{ki}) + \lambda_4\mathcal{G}_{\text{total}}^2$ with $\mathcal{G}_{\text{total}} = \lVert\mathrm{Im}\,\Gamma\rVert_F^2$ (§11: the sine of the phase sum times the three moduli is $\mathrm{Im}(\gamma_{ij}\gamma_{jk}\gamma_{ki})$; the associator norm is 2), minimised over all states of $\mathcal D(\mathbb C^7)$ with no sector split assumed:

1. **Step 1 fails.** $V_3$ is not $G_2$-invariant (erratum to the symmetry table, §11), so "$V_{\text{Gap}}$ on $(S^1)^{21}/G_2$" is not defined; besides, $G_2$ acts on $\Gamma$ by $\Gamma \mapsto g\Gamma g^{\mathsf T}$, not on a torus of phases.
2. **Step 2 fails for either choice of sectors.** With axis triples it rests on T-48a (retracted). With the correct triplets the $SU(3)$-invariant states carry one coherence parameter, not five, and among them the minimum is at $\mathcal{G}_{\text{total}} = 0$ (T-61 above). $SU(3)$-covariance does not equalise the coherences of a state that is not $SU(3)$-invariant.
3. **Not unique modulo $G_2$.** The minimiser is carried by the symmetries of $V_{\text{Gap}}$ to minimisers on which the $G_2$-invariant $\lVert w\rVert^2$, $w_k = \varphi_{ijk}\,\mathrm{Im}\,\Gamma_{ij}$, takes two values: two $G_2$-orbits at one value of $V$ (`test_v_gap_vacuum_is_unique_up_to_its_symmetries_not_up_to_g2`).
4. **No sector structure.** The stabiliser in $\mathfrak g_2$ of the minimiser is zero: the vacuum keeps no $SU(3)$ — neither $SU(3)_C = \mathrm{Stab}(e_O)$ nor the stabiliser of any other unit vector. The five "sector values" and the Hessian eigenvalues $18\mu^2$, $6\mu^2$, $12\mu^2$ of Step 4 describe no critical point of $V_{\text{Gap}}$.
:::

:::note Axis-frame restatement of T-64 [H] (the retracted cubic $V_3$): the self-consistent vacuum is unique up to the symmetries of $V_{\text{Gap}}$
**Exact part.** (a) $V_{\text{Gap}}$ is continuous on the compact $\mathcal D(\mathbb C^7)$, so its minimum value exists. (b) The signed permutations of the axes that preserve $V_{\text{Gap}}$ are the seven cyclic shifts $e_k \mapsto e_{k+1}$ (indices mod 7) combined with the $2^7$ sign changes — 896 in all, of which 56 lie in $G_2$ (`test_v_gap_cubic_term_is_not_g2_invariant`). (c) On the $SU(3)_C$-invariant states the minimum is at $\mathcal{G}_{\text{total}} = 0$.

**Numerical part — the hypothesis.** With the constants of Theorem 13.5 taken self-consistently (iterate: minimise, then recompute $\lambda_3/\mu^2 = 2/(3|\bar\gamma|)$ and $\lambda_4/\mu^2 = 1/(2\mathcal{G}^{(0)}_{\text{total}})$ at the minimiser; the iteration settles at $\lambda_3/\mu^2 = 9.25$, $\lambda_4/\mu^2 = 32.2$), 28 of 30 random starts reach $V_{\min} = -0.1973\,\mu^2$, and all 28 minimisers lie in one orbit of the 896 symmetries. The vacuum has rank 2, $P = 0.709$, $\mathcal{G}_{\text{total}} = 0.0155$, mean $|\gamma_{ij}| = 0.072$; it is supported on five axes forming the union of two Fano lines through one point (for one representative $\{D,L,U\} \cup \{O,A,D\}$; the cyclic shifts move the common point through all seven axes). The same picture holds at fixed constants $(\lambda_3/\mu^2, \lambda_4/\mu^2) = (1,1), (7,25), (30,10)$: 19, 26 and 30 of 30 starts reach the minimum, each set in one orbit, each support the union of two lines through a point. No proof of global optimality is given, hence [H].

**Consequence.** The vacuum of $V_{\text{Gap}}$ has no $SU(3)$ sector structure and none of the (SV) values: its $O$-coherences are $0.08$–$0.20$, not $\sim 1$, and its mean coherence is of order $10^{-1}$, not $10^{-2}$. Results that were "[C at T-64]" used the (SV) values, so they are [C at (SV)].
:::


:::note Earlier statement (Theorem 14.3, retracted [✗])
The $G_2$-invariant potential $V_{\text{Gap}}$ on the space $\mathcal{M} = (S^1)^{21}/G_2$ has a **unique global minimum** (up to $G_2$-conjugation). The minimum coincides with the sector solution from the [unique vacuum theorem](#теорема-единственный-вакуум).
:::

**Earlier proof (5 steps; retracted — see the box above).**

**Step 1 ($G_2$-orbit reduction).** The group $G_2 = \text{Aut}(\mathbb{O})$ acts on 21 coherences $\{\gamma_{ij}\}_{i < j}$ as $\text{Ad}(G_2)$. Since $\dim(G_2) = 14$, the orbit space:

$$
\mathcal{M}_{\text{phys}} = (S^1)^{21}/G_2, \quad \dim(\mathcal{M}_{\text{phys}}) = 21 - 14 = 7
$$

From [$G_2$-rigidity](/docs/proofs/categorical/uniqueness-theorem) [T]: 34 real parameters of $\Gamma$, of which 14 are gauge → 20 physical parameters of the matrix $\Gamma$. But the potential $V_{\text{Gap}}$ depends only on the **moduli** of coherences $|\gamma_{ij}|$ and the **phases** $\theta_{ij} = \arg(\gamma_{ij})$, with $G_2$ fixing phases through the Fano structure.

**Step 2 (Sector parametrization).** From the sector decomposition $7 = 1_O \oplus 3 \oplus \bar{3}$ [T] (see [spacetime](/docs/core/foundations/spacetime#теорема-секторная-декомпозиция)), the $G_2$-invariant potential depends only on 5 sector parameters:

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

All eigenvalues are strictly positive for $\mu^2 > 0$ (from positivity of $V_2$ [T], [Theorem 13.5](#константы-из-параметров-угм)).

**Step 5 (Globality).** Compactness of $(S^1)^{21}$ guarantees the existence of a global minimum. Uniqueness of the critical point (Step 4) + absence of saddle points → the global minimum is unique. $\blacksquare$

:::info Corollary (Complete resolution of $V_{\text{Gap}}$ minimization) — retracted [✗]
*Earlier text:* "The $V_{\text{Gap}}$ minimization problem is completely solved on the 5-dimensional orbit space. The residual 21-dimensional problem (before $G_2$-reduction) carries no new physics: $G_2$-gauge degrees of freedom do not enter the potential." Retracted with Theorem 14.3: $V_3$ is not $G_2$-invariant, so the $G_2$ directions do enter the potential, and the minimisation is open.
:::

#### Hypothesis (SV): the sector vacuum [H] {#гипотеза-секторного-вакуума}

:::note Hypothesis (SV) [H]
The vacuum coherences have the hierarchy of the table in the next subsection: $O$-pairs $\varepsilon_O \sim 1$; within the triplet $\varepsilon_{33} \sim 10^{-2}$; within the antitriplet $\varepsilon_{\bar 3\bar 3} \sim 10^{-17}$; between them $\varepsilon_{3\bar 3} \to 0$ — with a unique vacuum and a positive-definite fluctuation spectrum (eigenvalues $18\mu^2$, $6\mu^2$, $12\mu^2$).

It is not derived. Neither potential of this page gives it: the retracted cubic $V_3$ gives a vacuum on two Fano lines (the axis-frame record of T-64), and the $G_2$-invariant potential gives $I/7$ or a colour-invariant state with zero $O$-coherences (T-64, corrected, [T] for every $\kappa > 0$; for $\kappa \le 0$ its vacuum is not unique); and (SV) is in tension with unbroken colour: a state with a nonzero coherence anywhere except on the pairs $(A,D)$, $(S,U)$, $(L,E)$ is not $SU(3)_C$-invariant (`test_su3_invariant_states_are_coherent_only_on_o_line_pairs`), so the $O$-coherences $\varepsilon_O \sim 1$ of (SV) already break $SU(3)_C$. Results that took these values from T-64 are conditional on (SV).

**Decision (2026-09-25, with T-64 [T]).** No value of $\kappa$ makes (SV) the vacuum of the $G_2$-invariant $V_{\text{Gap}}$: for $\kappa \le 0$ the minimum is not unique (T-64 (a)); for $\kappa > 0$ every vacuum has $O$-coherences $0$ and $\bar\varepsilon < \sqrt5/40$ (T-64, consequences (i)–(ii)); and $\kappa$ itself is fixed by no derived source (T-331(e)–(f)). As a consequence of $V_{\text{Gap}}$, (SV) is refuted [✗]; it remains only an independent hypothesis [H].
:::


### Sector hierarchy of $\varepsilon$ [C at (SV)] {#теорема-секторная-иерархия-ε}

:::note Theorem 14.2 (Sector hierarchy of coherences) — corrected from [T] to [C at (SV)]: the table is hypothesis (SV), and the mean is taken over the non-O pairs (erratum below)
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

*Earlier conclusion (retracted): "The order $10^{-2}$ follows from the sector structure of the Gap vacuum."*
:::

*(Erratum 2026-09-25, audit A-83: the computation substitutes $\varepsilon_O \sim 0.04$, while the table above — and T-80, $\mathrm{Gap}(O,i) \approx 1$ — give $\varepsilon_O \sim 1$; the table of T-61 also had $\varepsilon_{33} \approx 0.06$, not $0.02$. With the table's own values the 21-pair formula gives $\bar\varepsilon^2 = (6 \cdot 1 + 3 \cdot 0.02^2)/21$, so $\bar\varepsilon = \sqrt{6/21} \approx 0.53$; the value $0.023$ is reached only at $\varepsilon_O \approx 0.04$, which contradicts the table (`test_mean_coherence_with_the_tables_own_eps_o`). The six $O$-pairs dominate any mean over all 21 pairs. **Repair.** The quantity used downstream — the bound on non-O Gap in T-80 and the mean of [Berry phase](/docs/physics/cosmology-phys/berry-phase) — is the mean over the 15 non-O pairs, so $\bar\varepsilon$ is redefined as their root mean square: $\bar\varepsilon^2 = (9\varepsilon_{3\bar 3}^2 + 3\varepsilon_{33}^2 + 3\varepsilon_{\bar 3\bar 3}^2)/15$, which under (SV) is $\varepsilon_{33}/\sqrt 5$: $0.027$ at $\varepsilon_{33} = 0.06$ and $0.009$ at $\varepsilon_{33} = 0.02$. The order $10^{-2}$ therefore holds, conditional on (SV) — [C at (SV)]; the earlier $0.023$ lies inside this range but was obtained from a wrong substitution. Note that the self-consistent vacuum of the retracted cubic $V_3$ (axis-frame record of T-64) gives a non-O root mean square of $0.097$, and the $G_2$-invariant potential (T-64, corrected) gives $|b-c|/(2\sqrt5)$: zero in the symmetric phase and below $\sqrt5/40 \approx 0.056$ in the Gap phase for every $\kappa$ [T] — so $10^{-2}$ is a property of (SV), not of $V_{\text{Gap}}$. Retracted [✗]: "the order $10^{-2}$ follows from the sector structure of the Gap vacuum".)*

### Sector hierarchy cascade {#каскад-секторной-иерархии}

Under hypothesis (SV) [H] the sector structure has the consequences below, each conditional on (SV). Items 1 and 2 were stated as derived; that is retracted [✗] (2026-09-25): the minimisation does not produce the sector values (T-64 restated), and with the non-O mean of the erratum to Theorem 14.2, $\bar\varepsilon \approx 0.027$ and $\bar\varepsilon^6 \approx 4 \times 10^{-10}$ (not $1.5 \times 10^{-10}$) — the same order.

1. **Retracted:** **$\varepsilon$ is not a free parameter.** The value of $\varepsilon$ follows from the sector vacuum structure determined by the decomposition $7 = 1_O \oplus 3 \oplus \bar{3}$ and minimization of $V_{\text{Gap}}$ by sectors.

2. **Retracted:** **$\Lambda$ budget.** The key formula $\varepsilon^6 \sim 10^{-12}$ in the cosmological constant budget is now structurally justified: $\bar{\varepsilon} \approx 0.023$ gives $\bar{\varepsilon}^6 \approx 1.5 \times 10^{-10}$, consistent in order of magnitude with the required suppression.

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
| Topological vacuum protection | $\pi_2(G_2/T^2) \cong \mathbb{Z}^2$; barrier $\geq 6\mu^2$ [C at (SV)] | [Composite systems](/docs/core/dynamics/composite-systems#теорема-тополог-защита) |
| Gap = Serre curvature | Exact identification via spectral triple [T] | [Gap operator](/docs/core/dynamics/gap-operator#теорема-gap-серра) |

---

**Related documents:**
- [Gap operator](/docs/core/dynamics/gap-operator) — definition, spectrum, and G₂ decomposition
- [Gap dynamics](/docs/core/dynamics/gap-dynamics) — opacity evolution, bifurcations, non-Markovian memory
- [Evolution of Γ](/docs/core/dynamics/evolution) — full equation of motion for the coherence matrix
- [Gap phase diagram](/docs/core/dynamics/gap-phase-diagram) — three phases of coherence and critical phenomena
