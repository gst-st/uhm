---
slug: /reference/specification
sidebar_position: 4
title: Mathematical Apparatus
description: Formal mathematical specification of UHM
---

# Mathematical Apparatus

:::note On notation
In this document:
- $\mathcal{H}$ — Hilbert space. Not to be confused with $H$ — the Hamiltonian.
- $\mathcal{C}$ — context space. Not to be confused with $C$ — [consciousness measure](/docs/consciousness/foundations/self-observation#мера-сознательности-c).
- $\mathcal{R}[\Gamma, E]$ — regenerative term of the evolution equation. Not to be confused with $R$ — [reflection measure](/docs/consciousness/foundations/self-observation#мера-рефлексии-r).
- $N = 7$ — dimensionality of the state space of the [Holon](/docs/core/structure/holon).
:::

## State Space

The state space of the [Holon](/docs/core/structure/holon) is a 7-dimensional complex Hilbert space (see [Seven dimensions](/docs/core/structure/dimensions)):

$$
\mathcal{H} = \mathbb{C}^7 = \mathrm{span}\{|A\rangle, |S\rangle, |D\rangle, |L\rangle, |E\rangle, |O\rangle, |U\rangle\}
$$

## Coherence Matrix {#матрица-когерентности}

<!-- DRY: Canonical definition of Γ in /docs/core/dynamics/coherence-matrix -->
See [Coherence matrix](/docs/core/dynamics/coherence-matrix) for the full definition.

$$
\Gamma \in \mathcal{L}(\mathcal{H}) \quad \text{— linear operator on } \mathcal{H}
$$

where $\mathcal{L}(\mathcal{H})$ is the space of linear operators on $\mathcal{H}$.

$$
\Gamma = \Gamma^\dagger \quad \text{— Hermitian}
$$

$$
\Gamma \geq 0 \quad \text{— positive semi-definite}
$$

$$
\mathrm{Tr}(\Gamma) = 1 \quad \text{— normalised}
$$

### Matrix form

$$
\Gamma = \begin{pmatrix}
\gamma_{AA} & \gamma_{AS} & \gamma_{AD} & \gamma_{AL} & \gamma_{AE} & \gamma_{AO} & \gamma_{AU} \\
\gamma_{SA} & \gamma_{SS} & \gamma_{SD} & \gamma_{SL} & \gamma_{SE} & \gamma_{SO} & \gamma_{SU} \\
\gamma_{DA} & \gamma_{DS} & \gamma_{DD} & \gamma_{DL} & \gamma_{DE} & \gamma_{DO} & \gamma_{DU} \\
\gamma_{LA} & \gamma_{LS} & \gamma_{LD} & \gamma_{LL} & \gamma_{LE} & \gamma_{LO} & \gamma_{LU} \\
\gamma_{EA} & \gamma_{ES} & \gamma_{ED} & \gamma_{EL} & \gamma_{EE} & \gamma_{EO} & \gamma_{EU} \\
\gamma_{OA} & \gamma_{OS} & \gamma_{OD} & \gamma_{OL} & \gamma_{OE} & \gamma_{OO} & \gamma_{OU} \\
\gamma_{UA} & \gamma_{US} & \gamma_{UD} & \gamma_{UL} & \gamma_{UE} & \gamma_{UO} & \gamma_{UU}
\end{pmatrix}
$$

## Hamiltonian {#гамильтониан}

See [Evolution: Unitary term](/docs/core/dynamics/evolution#1-unitary-term).

$$
H = \sum_{i=1}^{N} \omega_i |i\rangle\langle i| + \sum_{i \neq j} J_{ij} |i\rangle\langle j|
$$

where:
- $\omega_i$ — eigenfrequencies of dimensions
- $J_{ij}$ — coupling coefficients between dimensions
- $N = 7$ — number of dimensions

## Evolution Equation {#уравнение-эволюции}

<!-- DRY: Canonical definition of the evolution equation in /docs/core/dynamics/evolution -->
See [Evolution](/docs/core/dynamics/evolution) for a full description. Time τ is the [emergent internal time](/docs/proofs/dynamics/emergent-time).

$$
\frac{d\Gamma(\tau)}{d\tau} = -i[H_{eff}, \Gamma] + \underbrace{\sum_k \gamma_k \left( L_k \Gamma L_k^\dagger - \frac{1}{2}\{L_k^\dagger L_k, \Gamma\} \right)}_{\mathcal{D}[\Gamma]} + \mathcal{R}[\Gamma, E]
$$

where:
- $\tau$ — [internal time](/docs/proofs/dynamics/emergent-time), arising from correlations with dimension O
- $H_{eff}$ — effective Hamiltonian from the Page–Wootters constraint
- $-i[H_{eff}, \Gamma]$ — unitary (Hamiltonian) evolution
- $\mathcal{D}[\Gamma]$ — dissipative term ([decoherence](/docs/core/dynamics/evolution#логический-лиувиллиан))
- $\mathcal{R}[\Gamma, E]$ — [regenerative term](/docs/core/dynamics/evolution#3-регенеративный-член)
- $L_k = L_k^{\text{atom}} = \lvert k\rangle\langle k\rvert$ — [Lindblad operators](/docs/core/operators/lindblad-operators), derived from the atoms of the classifier $\Omega$ (projectors; historical notation $L_k = \sqrt{\chi_{S_k}}$ — convention)
- $\gamma_k \geq 0$ — decoherence rates

## Viability Measure (Purity)

<!-- DRY: Canonical definition P = Tr(Γ²) in /docs/core/dynamics/viability#определение-чистоты -->
See [Viability](/docs/core/dynamics/viability) for a full description.

$$
P = \mathrm{Tr}(\Gamma^2) \in \left[\frac{1}{N}, 1\right] = \left[\frac{1}{7}, 1\right]
$$

- $P = 1$: pure state ($\Gamma = |\psi\rangle\langle\psi|$)
- $P = 1/N = 1/7$: [maximally mixed state](/docs/core/dynamics/coherence-matrix#maximally-mixed-state) ($\Gamma = I_N/N$)

### Viability Condition

<!-- DRY: Canonical definition P_crit = 2/7 in /docs/core/dynamics/viability#критическая-чистота -->
The [Holon](/docs/core/structure/holon) is viable if:

$$
P > P_{\text{crit}} = \frac{2}{7} \approx 0.286
$$

At $P < P_{\text{crit}}$ the system enters irreversible decay (see [death condition](/docs/core/dynamics/viability#условие-смерти) and [theorem on critical purity](/docs/proofs/dynamics/theorem-purity-critical)).

## Experiential Space

See [Categorical formalism](/docs/proofs/categorical/categorical-formalism#2-категория-exp) for a full description.

### Projective Space of Qualities {#проективное-пространство-качеств}

$$
\mathbb{P}(\mathcal{H}_E) := (\mathcal{H}_E \setminus \{0\}) / {\sim}
$$

where $|\psi\rangle \sim |\varphi\rangle \Leftrightarrow \exists c \in \mathbb{C}^*: |\psi\rangle = c|\varphi\rangle$.

For $\mathcal{H}_E = \mathbb{C}^N$: $\dim_\mathbb{C}(\mathbb{P}(\mathbb{C}^N)) = N - 1$.

**Topology:**
- $\mathbb{P}(\mathbb{C}^N)$ is compact and connected
- $\mathbb{P}(\mathbb{C}^N) \cong S^{2N-1} / S^1$

### Fubini-Study Metric {#метрика-фубини-штуди}

**Definition:**
$$
d_{\mathrm{FS}}([|\psi\rangle], [|\varphi\rangle]) := \arccos(|\langle\psi|\varphi\rangle|) \in [0, \pi/2]
$$

**Properties:**
- $d_{\mathrm{FS}} = 0 \Leftrightarrow |\psi\rangle = e^{i\theta}|\varphi\rangle$
- $d_{\mathrm{FS}} = \pi/2 \Leftrightarrow \langle\psi|\varphi\rangle = 0$
- $d_{\mathrm{FS}}$ — Riemannian metric on $\mathbb{P}(\mathcal{H}_E)$

**Infinitesimal form:**
$$
ds^2 = \langle d\psi|d\psi\rangle - |\langle\psi|d\psi\rangle|^2
$$

### Full Experiential Space {#полное-экспериенциальное-пространство}

$$
\mathcal{E} := \Delta^{N-1} \times_{\mathrm{Spec}} \mathbb{P}(\mathcal{H}_E)^N \times \mathcal{C} \times \mathrm{Hist}
$$

where:
- $\Delta^{N-1} = \{(\lambda_1, \ldots, \lambda_N) : \lambda_i \geq 0, \sum \lambda_i = 1\}$ — $(N-1)$-simplex of intensities
- $\mathbb{P}(\mathcal{H}_E)^N$ — $N$ copies of the projective space (qualities)
- $\mathcal{C}$ — context space (see below)
- $\mathrm{Hist}$ — history space (see below)
- $\times_{\mathrm{Spec}}$ — fibred product over the spectrum

### Context Space 𝒞

**Definition:** The context space contains the states of all dimensions except [E](/docs/core/structure/dimension-e):

$$
\mathcal{C} := \mathcal{D}(\mathcal{H}_{-E}) \cong \mathcal{D}(\mathbb{C}^6)
$$

where $\mathcal{H}_{-E} = \mathrm{span}\{|A\rangle, |S\rangle, |D\rangle, |L\rangle, |O\rangle, |U\rangle\}$.

**Elements:** A context $c \in \mathcal{C}$ is the reduced density matrix:

$$
c = \rho_{-E} = \mathrm{Tr}_E(\Gamma)
$$

**Topology:** $\mathcal{C}$ inherits its topology from $\mathcal{D}(\mathbb{C}^6)$:
- Compact (closed subset of the unit ball in $\mathbb{C}^{6 \times 6}$)
- Connected
- Metrisable by the Frobenius norm: $d_{\mathcal{C}}(c_1, c_2) = \|c_1 - c_2\|_F$

**Interpretation:** The context determines how the remaining dimensions (Articulation, Structure, Dynamics, Logic, Ground, Unity) modulate the interiority state.

### History Space Hist

**Definition:** The history space is the functional space of trajectories:

$$
\mathrm{Hist} := C([0, \tau], \mathcal{D}(\mathcal{H}_E))
$$

where $\tau > 0$ is the memory horizon, $C([0, \tau], X)$ — space of continuous functions $[0, \tau] \to X$.

**Elements:** A history $h \in \mathrm{Hist}$ is the trajectory of the reduced density matrix of experience:

$$
h = \{\rho_E(t') : t' \in [t - \tau, t]\}
$$

**Topology:** $\mathrm{Hist}$ is equipped with the topology of uniform convergence:
- Metric: $d_{\mathrm{Hist}}(h_1, h_2) = \sup_{t' \in [0, \tau]} \|\rho_E^{(1)}(t') - \rho_E^{(2)}(t')\|_F$
- Banach space with the sup norm
- Separable

**Interpretation:** History encodes the temporal structure of experience — memory, anticipation, adaptation to patterns.

:::note Practical simplification
For computations, discretisation is often used: $\mathrm{Hist}_{\text{disc}} = \{\rho_E(t_0), \rho_E(t_1), \ldots, \rho_E(t_K)\}$ with step $\Delta t = \tau / K$.
:::

### Full Metric on $\mathcal{E}$

$$
d_{\mathcal{E}}(\mathcal{Q}_1, \mathcal{Q}_2) := \sqrt{d_\Delta(\lambda_1, \lambda_2)^2 + \alpha \sum_i d_{\mathrm{FS}}([q_1^{(i)}], [q_2^{(i)}])^2 + \beta \cdot d_{\mathcal{C}}(c_1, c_2)^2 + \gamma \cdot d_{\mathrm{Hist}}(h_1, h_2)^2}
$$

where $\alpha, \beta, \gamma > 0$ are weight coefficients.

## Categorical Formalism

See [Categorical formalism](/docs/proofs/categorical/categorical-formalism) for a full description and proofs.

### Category of Density Matrices

**Definition (DensityMat):**

$$
\mathbf{DensityMat} := (\mathrm{Ob}, \mathrm{Mor})
$$

$$
\mathrm{Ob}(\mathbf{DensityMat}) = \{\rho \in \mathcal{L}(\mathcal{H}) : \rho^\dagger = \rho, \rho \geq 0, \mathrm{Tr}(\rho) = 1\}
$$

$$
\mathrm{Mor}_{\mathbf{DM}}(\rho_1, \rho_2) = \{\Psi : \mathcal{L}(\mathcal{H}) \to \mathcal{L}(\mathcal{H}) \mid \Psi \text{ — CPTP}, \Psi(\rho_1) = \rho_2\}
$$

**Kraus representation:** $\Psi$ — CPTP $\Leftrightarrow \exists\{K_i\}: \Psi(\rho) = \sum_i K_i \rho K_i^\dagger$, $\sum_i K_i^\dagger K_i = I$

:::info CPTP structure of regeneration
The UHM regenerative operator is a CPTP channel:

$$
\mathcal{R}_\alpha(\rho) = (1-\alpha)\rho + \alpha\varphi(\rho)
$$

with $\alpha = \kappa(\Gamma) \cdot g_V(P) \cdot \Delta\tau \in [0,1]$. Kraus representation: $\tilde{K}_0 = \sqrt{1-\alpha}I$, $\tilde{K}_k = \sqrt{\alpha}K_k$.

**Correctness condition:** $\alpha < 1 \Leftrightarrow \Delta\tau < 1/\kappa_{\max}$.

See [preservation of positivity](/docs/core/dynamics/evolution#сохранение-положительности).
:::

See [Formalisation of operator φ](/docs/proofs/categorical/formalization-phi) for details of CPTP channels.

### Experience Functor

**Definition of F on objects:**
$$
F: \mathrm{Ob}(\mathbf{DensityMat}) \to \mathrm{Ob}(\mathbf{Exp})
$$

$$
F(\rho) := (\mathrm{Spectrum}(\rho_E), \mathrm{Quality}(\rho_E), \mathrm{Context}(\Gamma_{-E}), \mathrm{History}(t))
$$

**[Theorem (Functoriality)](/docs/proofs/categorical/categorical-formalism#5-доказательство-функториальности):** $F$ is a functor.

*Proof:*
1. $F(\mathrm{id}_\rho) = \mathrm{id}_{F(\rho)}$ ✓
2. $F(\Psi \circ \Phi) = F(\Psi) \circ F(\Phi)$ ✓

## Grothendieck Topology {#топология-гротендика}

To construct the ∞-topos $\mathbf{Sh}_\infty(\mathcal{C})$, the Grothendieck topology on the base category must be explicitly specified.

### Bures Metric

**Definition (chord form):**

$$
d_B^{\mathrm{chord}}(\Gamma_1, \Gamma_2) := \sqrt{2\left(1 - \sqrt{F(\Gamma_1, \Gamma_2)}\right)}
$$

where $F(\Gamma_1, \Gamma_2) = \left(\mathrm{Tr}\sqrt{\sqrt{\Gamma_1}\Gamma_2\sqrt{\Gamma_1}}\right)^2$ — fidelity.

:::note Convention: two forms of $d_B$
UHM uses two forms of the Bures metric. Here the **chord** form is applied ($d_B^{\mathrm{chord}} \in [0, \sqrt{2}]$). Angular form: $d_B^{\mathrm{angle}} = \arccos(\sqrt{F})$. See [full convention](/docs/reference/notation#топология-гротендика).
:::

**Properties:**
- $d_B^{\mathrm{chord}} \in [0, \sqrt{2}]$
- $d_B^{\mathrm{chord}}(\Gamma, \Gamma) = 0$
- Monotonicity: $d_B^{\mathrm{chord}}(\Psi(\rho), \Psi(\sigma)) \leq d_B^{\mathrm{chord}}(\rho, \sigma)$ for CPTP $\Psi$
- Riemannian metric on the manifold of density matrices

### Bures Coverings

**Definition (DensityMat Site):**

A family of morphisms $\{\Psi_i: \Gamma_i \to \Gamma\}_{i \in I}$ forms a **covering** of object $\Gamma$ if:

$$
\forall \epsilon > 0, \exists \delta > 0: \quad B_B(\Gamma, \delta) \subseteq \bigcup_{i \in I} \Psi_i(B_B(\Gamma_i, \epsilon))
$$

**Site axioms:**

1. **Identity:** $\{\mathrm{id}_\Gamma\}$ covers $\Gamma$
2. **Stability:** Pullback of a covering is a covering
3. **Transitivity:** Composition of coverings is a covering

### Connection to the ∞-topos

The superscript "loc" in the definition of $\mathbf{Sh}_\infty(\mathcal{C})^{loc}$ denotes localisation relative to Bures coverings:

$$
F \text{ — sheaf} \Leftrightarrow F(X) \xrightarrow{\sim} \lim_{\{U \to X\} \in \text{Cov}(X)} F(U)
$$

**Subobject classifier:**

$$
\Omega := \mathcal{O}(\mathcal{C}, d_B)
$$

— lattice of open sets in the Bures topology.

See [Categorical formalism: Grothendieck topology](/docs/proofs/categorical/categorical-formalism#63-топология-гротендика-на-densitymat-и-exp) for the full specification.

---

### Theorem on the Impossibility of a Spectral Functor {#теорема-невозможность-спектрального-функтора}

:::warning Theorem
There is no functor $F: \mathbf{DensityMat} \to \mathbf{Exp}$ that factors *only* through the spectrum.
:::

**Proof:**
1. Suppose $F = G \circ \mathrm{Spec}$, where $\mathrm{Spec}: \rho \mapsto \mathrm{Spectrum}(\rho)$
2. Consider isospectral $\rho_1 \neq \rho_2$
3. Then $F(\rho_1) = F(\rho_2)$
4. But $\rho_1$ and $\rho_2$ can describe distinguishable experiences
5. Contradiction ∎

**Corollary:** The full functor $F$ must account for eigenvectors, context, and history.

## Consciousness Measures

### Reflection Measure

<!-- DRY: Canonical definition of R in /docs/consciousness/foundations/self-observation#мера-рефлексии-r -->
See [Self-observation: Reflection measure R](/docs/consciousness/foundations/self-observation#мера-рефлексии-r).

$$
R(\Gamma) := \frac{1}{7P(\Gamma)}, \quad P = \mathrm{Tr}(\Gamma^2)
$$

Equivalent form via Frobenius norm: $R = 1 - \|\Gamma - \rho^*_{\mathrm{diss}}\|_F^2 / \|\Gamma\|_F^2$, where $\rho^*_{\mathrm{diss}} = I/7$ — dissipative attractor (not $\varphi(\Gamma)$). Derivation: [Self-observation](/docs/consciousness/foundations/self-observation#мера-рефлексии-r).

:::note Distinguishing $R_{\text{canonical}}$ and $Q_\varphi$
$R = R_{\text{canonical}} := 1/(7P)$ — **canonical definition**, used in all thresholds ($R_{\text{th}} = 1/3$). This is a measure of proximity to the maximally mixed state $I/7$. The self-modelling quality measure is defined separately: $Q_\varphi(\Gamma) := 1 - \|\Gamma - \varphi(\Gamma)\|_F^2 / \|\Gamma\|_F^2$. Details: [Formalisation of φ](/docs/proofs/categorical/formalization-phi#28-рефлексия-n-го-порядка-для-l3l4).
:::

### Higher-Order Reflection $R^{(n)}$

See [Higher-order reflection](/docs/proofs/categorical/formalization-phi#28-рефлексия-n-го-порядка-для-l3l4) and [Interiority hierarchy](/docs/proofs/consciousness/interiority-hierarchy).

$$
R^{(n)}(\Gamma) := F(\varphi^{(n-1)}(\Gamma), \varphi^{(n)}(\Gamma)) \in [0, 1]
$$

where:
- $\varphi^{(k)}$ — $k$-fold application of the self-modelling operator
- $F(\rho, \sigma)$ — fidelity (quantum fidelity)

**Interpretation:** $R^{(n)}$ measures the consistency between successive levels of self-modelling.

**Connection to interiority levels:**
- L2 requires $R = R^{(1)} \geq 1/3$
- L3 requires $R^{(2)} \geq 1/4$
- L4 requires $\lim_n R^{(n)} > 0$ (infinite recursiveness)

### Universal Formula for Reflection Thresholds

**Reflection** thresholds follow a unified pattern (Bayesian dominance over $n+1$ alternatives):

$$
R^{(n)}_{\mathrm{th}} = \frac{1}{n+1}
$$

| Transition | Measure | Threshold | Status | Derivation |
|------------|---------|-----------|--------|------------|
| L0→L1 | $\Phi$ | $> 0$ | | Structural condition (any integration) |
| L1→L2 | $R, \Phi, D_{\text{diff}}$ | $1/3, 1, 2$ | **[T],[T],[T]** | $R$: triadic decomposition + Bayesian; $\Phi$: T-129; $D_{\min}$: T-151 |
| L2→L3 | $R^{(2)}$ | $1/4$ | **[T]** | $1/(3+1)$ |
| L3→L4 | $\lim R^{(n)}$ | $> 0$ | **[T]** | Postnikov stabilisation |

:::note Origin and status of thresholds
- **$P_{\text{crit}} = 2/7$** **[T]** — [strictly proved](/docs/proofs/dynamics/theorem-purity-critical) (five independent paths)
- **$R_{\text{th}} = 1/3$** **[T]** — $K=3$ from [triadic decomposition](/docs/core/operators/lindblad-operators#триадная-декомпозиция) + [Bayesian dominance](/docs/core/foundations/axiom-septicity#теорема-порог-рефлексии)
- **$\Phi_{\text{th}} = 1$** **[T]** — unique self-consistent value at $P_{\text{crit}} = 2/7$ ([T-129](/docs/proofs/consciousness/operationalization#t-129))
- **$D_{\text{diff}} \geq 2$** **[T]** — unconditional consequence of $\Phi_{\text{th}} = 1$ [T] ([T-151](/docs/proofs/consciousness/substrate-closure#t-151))
:::

### Integration Measure

<!-- DRY: Canonical definition of Φ in /docs/core/structure/dimension-u#мера-интеграции-φ -->
See [Unity dimension: Integration measure Φ](/docs/core/structure/dimension-u#мера-интеграции-φ).

$$
\Phi(\Gamma) := \frac{\sum_{i \neq j} |\gamma_{ij}|^2}{\sum_i \gamma_{ii}^2}
$$

### Differentiation Measure

$$
D_{\text{diff}}(\Gamma) := \exp(S_{vN}(\rho_E))
$$

where $S_{vN}(\rho_E) = -\mathrm{Tr}(\rho_E \log \rho_E)$ — [von Neumann entropy](/docs/core/dynamics/coherence-matrix#энтропия-фон-неймана).

:::warning Requirement: extended formalism for D_diff
Computing $D_{\text{diff}}$ requires the full reduced matrix $\rho_E = \mathrm{Tr}_{-E}(\Gamma)$, which is defined only in the [extended tensor formalism](/docs/core/dynamics/coherence-matrix#two-levels-of-formalization) (42D). In 7D, the partial trace is undefined (7 is prime).

**Note:** The scalar measure $\mathrm{Coh}_E$ (E-coherence) **does not require** a partial trace — it is defined in 7D via the [HS-projection](/docs/core/foundations/axiom-septicity#hs-projection) **[T]**. The extended formalism is needed only for the spectral decomposition of $\rho_E$ and consequently for $D_{\text{diff}}$.
:::

**Range:** $D_{\text{diff}} \in [1, N]$, where $N = \dim(\mathcal{H}_E)$.

**Interpretation:**
- $D_{\text{diff}} = 1$ (pure state): one component of experience
- $D_{\text{diff}} = N$ (maximally mixed): $N$ equally probable components

:::note Alternative definition
In some contexts $D_{\text{diff}} = \mathrm{rank}(\rho_E)$ is used. This is an integer version, less sensitive to the distribution of eigenvalues. The primary definition via $\exp(S_{vN})$ is a more informative, continuous measure.
:::

### Consciousness Measure

See [Self-observation: Consciousness measure C](/docs/consciousness/foundations/self-observation#мера-сознательности-c).

$$
C = \Phi \times R
$$

---

## Octonionic Algebra {#октонионная-алгебра}

:::info Definition of 𝕆 ([structural derivation](../proofs/minimality/theorem-octonionic-derivation))
**Octonions** $\mathbb{O}$ — 8-dimensional normed division algebra over $\mathbb{R}$:

$$
\mathbb{O} = \{a_0 + \sum_{k=1}^{7} a_k e_k \mid a_i \in \mathbb{R}\}
$$

**Multiplication table** is defined by 7 triplets of the [Fano plane](../proofs/minimality/theorem-octonionic-derivation#плоскость-фано):

$$
e_i \cdot e_j = -\delta_{ij} + \varepsilon_{ijk} e_k
$$

**Automorphism group:** $\text{Aut}(\mathbb{O}) = G_2$, $\dim(G_2) = 14$, $\text{rank}(G_2) = 2$.

**Connection to UHM:** $N = \dim(\text{Im}(\mathbb{O})) = 7$ — [two-track justification](../core/foundations/axiom-omega#октонионная-структура) of Axiom 3.
:::

---

**Related documents:**
- [Holon](/docs/core/structure/holon) — definition of $\mathbb{H}$
- [Seven dimensions](/docs/core/structure/dimensions) — basis $\mathcal{H}$
- [Coherence matrix](/docs/core/dynamics/coherence-matrix) — definition of $\Gamma$
- [Evolution](/docs/core/dynamics/evolution) — dynamics $d\Gamma(\tau)/d\tau$
- [Emergent time](/docs/proofs/dynamics/emergent-time) — derivation of τ from the structure of Γ
- [Viability](/docs/core/dynamics/viability) — measure $P$ and $P_{\text{crit}}$
- [Self-observation](/docs/consciousness/foundations/self-observation) — measures $R$, $C$, $D_{\text{diff}}$
- [Unity dimension](/docs/core/structure/dimension-u) — measure $\Phi$
- [Formalisation of operator φ](/docs/proofs/categorical/formalization-phi) — CPTP channels
- [Categorical formalism](/docs/proofs/categorical/categorical-formalism) — functor $F$, ∞-groupoid $\mathbf{Exp}_\infty$
- [Interiority hierarchy](/docs/proofs/consciousness/interiority-hierarchy) — levels L0→L1→L2→L3→L4 and n-truncations of the ∞-groupoid
- [Bimodular construction](/docs/proofs/physics/bimodule-construction) — SM representations from bimodules of the spectral triple (T-178–T-181)
- [Computational implementation](./computational) — Python code
