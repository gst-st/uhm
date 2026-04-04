---
sidebar_position: 2
title: Notation
description: Mathematical notation of UHM theory
---

# Mathematical Notation

:::warning Potential notation conflicts
In UHM theory, some symbols have multiple meanings depending on context:
- $D$ — [Dynamics dimension](/docs/core/structure/dimension-d) **vs** $D_{\text{diff}}$ — [differentiation measure](/docs/consciousness/foundations/self-observation#мера-сознательности-c)
- $\mathcal{H}$ — Hilbert space **vs** $H$ — Hamiltonian **vs** $\mathcal{H}_\Gamma$ — Hessian of free energy (in [Freedom](/docs/core/foundations/consequences#freedom-конечномерное))
- $\Phi$ — [integration measure](/docs/core/structure/dimension-u#мера-интеграции-φ). For denoting arbitrary CPTP channels, $\Psi$ is used
- $R$ — [reflection measure](/docs/consciousness/foundations/self-observation#мера-рефлексии-r) **vs** $\mathcal{R}$ — regenerative term
- $\mathcal{C}$ — primitive category (Axiom Ω⁷) **vs** $C$ — [consciousness measure](/docs/consciousness/foundations/self-observation#мера-сознательности-c). The context space in the Exp category is denoted $\Gamma_{-E}$
- $\gamma_{ij}$ — elements of the coherence matrix **vs** $\gamma_k$ — decoherence rates in the Lindblad dissipator (in different documents). **Recommendation:** use $\Gamma_2$ for decoherence rates (as in [Theorem 8.1](/docs/applied/coherence-cybernetics/theorems#теорема-81-условная-необходимость-интериорности-no-zombie))

Context usually makes the meaning unambiguous.
:::

:::info Connection to IIT (Integrated Information Theory)
The integration measure $\Phi$ in UHM **differs** from $\Phi$ in Tononi's theory (IIT):

| Parameter | UHM | IIT |
|-----------|-----|-----|
| **Definition** | $\Phi_{\text{UHM}} = \sum_{i \neq j} \lvert\gamma_{ij}\rvert^2 / \sum_i \gamma_{ii}^2$ | $\Phi_{\text{IIT}}$ = minimum mutual information over partitions |
| **Interpretation** | Coherence between dimensions | Integrated information |
| **Computational complexity** | $O(n^2)$ | NP-hard |

UHM generalises IIT: the consciousness measure $C = \Phi \times R$ **[T T-140]** includes integration $\Phi$ and reflection $R$. Differentiation $D_{\text{diff}} \geq D_{\min}$ — a separate viability condition.
:::

## Core Symbols

| Symbol | Meaning | Definition |
|--------|---------|------------|
| $\mathcal{C}$ | [Primitive category](/docs/core/foundations/axiom-omega#примитив) | Small category with a finite number of objects — **sole primitive** |
<!-- DRY: Canonical definition of Γ in /docs/core/dynamics/coherence-matrix -->
| $\Gamma$ | [Coherence matrix](/docs/core/dynamics/coherence-matrix) | $\Gamma \in \mathcal{L}(\mathcal{H})$, $\Gamma^\dagger = \Gamma$, $\Gamma \geq 0$, $\mathrm{Tr}(\Gamma) = 1$ |
| $\mathbb{H}$ | [Holon](/docs/core/structure/holon) | Minimal self-sufficient unit of reality |
| $\mathcal{H}$ | Hilbert space | $\mathcal{H} = \mathbb{C}^7$ — see [Seven dimensions](/docs/core/structure/dimensions) |
<!-- DRY: Canonical definition P = Tr(Γ²) in /docs/core/dynamics/viability#определение-чистоты -->
| $P$ | [Purity](/docs/core/dynamics/viability#определение-чистоты) | $P = \mathrm{Tr}(\Gamma^2) \in [1/7, 1]$ |
| $S_{vN}$ | Von Neumann entropy | $S_{vN} = -\mathrm{Tr}(\Gamma \log \Gamma) \in [0, \log 7]$ |
| $\tau$ | [Internal time](/docs/proofs/dynamics/emergent-time) | Evolution parameter derived from the structure of $\mathcal{C}$; $\tau \in \mathbb{Z}_7$ for 7D |
| $t, t'$ | Time parameter in formulae | Used in integrals and histories; related to $\tau$ via $t = n \cdot \delta\tau$ |
| $H_{\text{eff}}$ | [Effective Hamiltonian](/docs/core/dynamics/evolution#вывод-h_eff) | $H_{\text{eff}}(\tau) = H_{6D} + \langle\tau\vert H_{\text{int}}\vert\tau\rangle_O$ |
| $d_B$ | [Bures metric](/docs/proofs/dynamics/emergent-time#41-метрика-бурес) | Angular: $d_B^{\mathrm{angle}} = \arccos(\sqrt{F})$; chord: $d_B^{\mathrm{chord}} = \sqrt{2(1-\sqrt{F})}$. See [convention below](#топология-гротендика) |

## Base Space and Stratification

| Symbol | Meaning | Definition |
|--------|---------|------------|
| $X$ | [Base space](/docs/core/foundations/spacetime#базовое-пространство) | $X = \|N(\mathcal{C})\|$ — geometric realisation of the nerve of the category |
| $N(\mathcal{C})$ | [Nerve of the category](/docs/core/foundations/spacetime#нерв-категории) | Simplicial set: n-simplices = composable chains of morphisms |
| $T$ | [Terminal object](/docs/core/foundations/axiom-omega#свойство-3) | $T = \Gamma^*$ — global attractor; $\forall\Gamma, \exists! f: \Gamma \to T$ |
| $S_\alpha$ | [Stratum](/docs/core/foundations/spacetime#стратификация-x) | Component of the stratification $X = \bigsqcup_\alpha S_\alpha$; $S_0 = \{T\}$ |
| $d_{strat}$ | [Stratified metric](/docs/core/foundations/spacetime#метрика-конна) | $d_{strat}(\omega_1, \omega_2) = \inf_\gamma \int_\gamma ds_\alpha$ |
| $\text{Link}(T)$ | Link of the terminal object | $\text{Link}(T) \cong S^6$ — 6-sphere |
| $H^*(X)$ | [Cohomology](/docs/core/foundations/consequences#когомологический-монизм) | $H^n(X, \mathcal{F}) = 0$ for $n > 0$ (monism) |
| $H^*_{loc}(X,T)$ | [Local cohomology](/docs/core/foundations/spacetime#локально-глобальная-дихотомия) | $H^*_{loc}(X,T) \cong \tilde{H}^{*-1}(S^6) \neq 0$ (physics) |
| $D^b(X)$ | [Derived category](/docs/proofs/categorical/categorical-formalism#производные-категории) | Bounded derived category of sheaves on X |
| $IC(S_\alpha)$ | IC sheaf | Intersection cohomology sheaf of stratum $S_\alpha$ |

## Dimensions

Seven basis states of [space $\mathcal{H}$](/docs/core/structure/dimensions):

| Symbol | Dimension | Associated structure | More |
|--------|-----------|---------------------|------|
| $A$ | Articulation | Projectors, measurements | [→](/docs/core/structure/dimension-a) |
| $S$ | Structure | Hamiltonian $H$ | [→](/docs/core/structure/dimension-s) |
| $D$ | Dynamics | Unitary evolution $U(\tau)$ | [→](/docs/core/structure/dimension-d) |
| $L$ | Logic | Operator algebra | [→](/docs/core/structure/dimension-l) |
| $E$ | Interiority | Density matrix $\rho_E$ | [→](/docs/core/structure/dimension-e) |
| $O$ | Ground | Vacuum state $\vert 0\rangle$, internal clock ([Page–Wootters](/docs/proofs/dynamics/emergent-time)) | [→](/docs/core/structure/dimension-o) |
| $U$ | Unity | Trace operation $\mathrm{Tr}$ | [→](/docs/core/structure/dimension-u) |

## State Space Basis

$$
\mathcal{H} = \mathrm{span}\{|A\rangle, |S\rangle, |D\rangle, |L\rangle, |E\rangle, |O\rangle, |U\rangle\} = \mathbb{C}^7
$$

Orthonormality: $\langle i|j\rangle = \delta_{ij}$ for $i, j \in \{A, S, D, L, E, O, U\}$.

## Clock Algebra (Page–Wootters)

| Symbol | Meaning | Definition |
|--------|---------|------------|
| $H_O$ | [Clock Hamiltonian](/docs/core/structure/dimension-o#гамильтониан-часов-h_o) | $H_O = \omega_0 \sum_{k=0}^{N-1} k \vert k\rangle\langle k\vert_O$ |
| $V_O$ | [Time shift operator](/docs/core/structure/dimension-o#оператор-сдвига-v_o) | $V_O^N = \mathbb{1}$, $V_O H_O V_O^\dagger = H_O + \omega_0 \mathbb{1}$ |
| $\mathcal{A}_O$ | [Clock C*-algebra](/docs/core/structure/dimension-o#c-алгебра-часов-a_o) | $\mathcal{A}_O = C^*(H_O, V_O) \cong M_N(\mathbb{C})$ |
| $H_{\text{int}}$ | [Interaction Hamiltonian](/docs/core/foundations/axiom-omega#гамильтониан-взаимодействия) | Coupling of O with E and U |
| $\hat{C}$ | [Page–Wootters constraint](/docs/core/foundations/axiom-omega#свойство-2) | $\hat{C} = H_O \otimes \mathbb{1}_{6D} + \mathbb{1}_O \otimes H_{6D} + H_{\text{int}}$ |
| $\mathcal{H}_{total}$ | Global space | $\mathcal{H}_{total} = \mathcal{H}_O \otimes \mathcal{H}_{6D}$, $\dim = 42$ |
| $\omega_0$ | Fundamental frequency | Base frequency of clock O |
| $\vert\tau_n\rangle$ | Clock basis | Eigenstates of $V_O$ |

## Evolution Equation

<!-- DRY: Canonical definition of the evolution equation in /docs/core/dynamics/evolution -->
Full [evolution equation](/docs/core/dynamics/evolution) with [emergent internal time](/docs/proofs/dynamics/emergent-time) τ:

$$
\frac{d\Gamma(\tau)}{d\tau} = -i[H_{\text{eff}}, \Gamma] + \mathcal{D}[\Gamma] + \mathcal{R}[\Gamma, E]
$$

where:

**[Unitary term](/docs/core/dynamics/evolution#1-unitary-term):**
$$
-i[H_{\text{eff}}, \Gamma] = -i(H_{\text{eff}}\Gamma - \Gamma H_{\text{eff}})
$$

Here $H_{\text{eff}}$ is the effective Hamiltonian arising from the Page–Wootters constraint.

**[Dissipative term](/docs/core/dynamics/evolution#логический-лиувиллиан):**
$$
\mathcal{D}[\Gamma] = \sum_k \gamma_k \left( L_k \Gamma L_k^\dagger - \frac{1}{2}\{L_k^\dagger L_k, \Gamma\} \right)
$$

**[Regenerative term](/docs/core/dynamics/evolution#3-регенеративный-член) [T]:**
$$
\mathcal{R}[\Gamma, E] = \kappa(\Gamma) \cdot (\rho_* - \Gamma) \cdot g_V(P)
$$

where:
- $\kappa(\Gamma) \geq 0$ — regeneration rate [T] (adjunction $\mathcal{D}_\Omega \dashv \mathcal{R}$)
- $\rho_* = \varphi(\Gamma)$ — categorical self-model of the current state [T] ([φ-operator](/docs/core/operators/phi-operator))
- $(\rho_* - \Gamma)$ — unique CPTP relaxation [T]
- $g_V(P) = \mathrm{clamp}\!\bigl(\frac{P - P_{\mathrm{crit}}}{P_{\mathrm{opt}} - P_{\mathrm{crit}}}\bigr)$ — V-preservation gate [T] (Landauer + V-invariance, [derivation](/docs/core/dynamics/evolution#теорема-v-preservation-gate))

## Commutators and Anticommutators

| Notation | Definition |
|----------|------------|
| $[A, B]$ | $AB - BA$ (commutator) |
| $\{A, B\}$ | $AB + BA$ (anticommutator) |

## Interiority Operators (Dimension E)

See [Interiority Dimension](/docs/core/structure/dimension-e) and [Exp Category](/docs/proofs/categorical/categorical-formalism#2-категория-exp).

| Notation | Meaning |
|----------|---------|
| $\rho_E$ | Reduced density matrix of the Interiority dimension |
| $\lambda_i$ | Eigenvalue of $\Gamma$ (intensity) |
| $\vert q_i\rangle$ | Eigenvector of $\Gamma$ (quality) |
| $[\vert q\rangle]$ | Equivalence class in $\mathbb{P}(\mathcal{H}_E)$ |
| $\mathbb{P}(\mathcal{H}_E)$ | [Projective space](/docs/reference/specification#проективное-пространство-качеств) of qualities |
| $d_{\mathrm{FS}}$ | [Fubini-Study metric](/docs/reference/specification#метрика-фубини-штуди) |

**Fubini-Study metric:**
$$
d_{\mathrm{FS}}([|\psi\rangle], [|\phi\rangle]) = \arccos(|\langle\psi|\phi\rangle|) \in [0, \pi/2]
$$

## Consciousness Measures

See [Self-observation](/docs/consciousness/foundations/self-observation) for full definitions.

| Measure | Formula | Range |
|---------|---------|-------|
| [Integration $\Phi$](/docs/core/structure/dimension-u#мера-интеграции-φ) | $\Phi(\Gamma) = \dfrac{\sum_{i \neq j} \lvert\gamma_{ij}\rvert^2}{\sum_i \gamma_{ii}^2}$ | $[0, +\infty)$ |
| [Differentiation $D_{\text{diff}}$](/docs/consciousness/foundations/self-observation#мера-сознательности-c) | $D_{\text{diff}}(\Gamma) = \exp(S_{vN}(\rho_E))$ | $[1, 7]$ |
| [Reflection $R$](/docs/consciousness/foundations/self-observation#мера-рефлексии-r) | $R(\Gamma) = R_{\text{canonical}} = \dfrac{1}{7P(\Gamma)}$, where $P = \mathrm{Tr}(\Gamma^2)$; equivalent to $1 - \dfrac{\|\Gamma - I/7\|_F^2}{P}$. Not to be confused with $Q_\varphi = 1 - \|\Gamma - \varphi(\Gamma)\|_F^2 / P$ (quality measure of self-modelling) | $[0, 1]$ |
| [Consciousness $C$](/docs/consciousness/foundations/self-observation#мера-сознательности-c) | $C(\Gamma) = \Phi \times R$ **[T]** (T-140); $D_{\text{diff}} \geq 2$ — separate viability condition | $[0, +\infty)$ |
| Free will $\mathrm{Freedom}(\Gamma)$ **[T]** | $\mathrm{Freedom}(\Gamma) = \dim\ker(\mathcal{H}_\Gamma) + 1$, where $\mathcal{H}_\Gamma = \partial^2 \mathcal{F}/\partial\Gamma^2$ — [finite-dimensional definition](/docs/core/foundations/consequences#freedom-конечномерное). ∞-categorical motivation: $\pi_0(\mathrm{Map}(\Gamma, T)^{\text{non-trivial}})$ | $\{1, \ldots, 7\}$ |
| Freedom entropy $S_{\text{freedom}}$ | $S_{\text{freedom}} = \log(\text{Freedom}(\Gamma))$ | $[0, \log 7]$ |

## Self-Modelling Operator

See [Formalisation of operator φ](/docs/proofs/categorical/formalization-phi) for a full description.

**CPTP channel** (Completely Positive Trace-Preserving):
$$
\varphi(\Gamma) = \sum_m K_m \Gamma K_m^\dagger
$$

**Completeness condition** (trace preservation):
$$
\sum_m K_m^\dagger K_m = I
$$

**Convergence to fixed point** $\Gamma^* = \varphi(\Gamma^*)$:
$$
\|\varphi^n(\Gamma_0) - \Gamma^*\|_F \leq k^n \cdot \|\Gamma_0 - \Gamma^*\|_F, \quad k \in [0, 1)
$$

## Interiority Hierarchy

See [Interiority hierarchy](/docs/proofs/consciousness/interiority-hierarchy) for formal conditions and proofs.

| Level | Notation | Condition | n-truncation |
|-------|----------|-----------|--------------|
| L0 | $\mathrm{Int}(S)$ — Interiority | $\exists \rho_E$ | $\tau_{\leq 0}$ |
| L1 | $\mathrm{PG}(S)$ — Phenomenal geometry | $\mathrm{rank}(\rho_E) > 1$ | $\tau_{\leq 1}$ |
| L2 | Cognitive qualia | $R \geq R_{\text{th}}$, $\Phi \geq \Phi_{\text{th}}$, $D_{\text{diff}} \geq 2$ | $\tau_{\leq 2}$ |
| L3 | Network consciousness | $R^{(2)} \geq R^{(2)}_{\text{th}}$ (metastable) | $\tau_{\leq 3}$ |
| L4 | Unitary consciousness | $\lim_{n \to \infty} R^{(n)} > 0$, $P > 6/7$ | $\tau_{\leq \infty}$ |

**Threshold values** ([all proved mathematically [T]](/docs/core/foundations/axiom-septicity#пороги-l2-строгий-вывод), [threshold justifications](/docs/proofs/consciousness/interiority-hierarchy#обоснование-порогов)):

| Threshold | Value | Status |
|-----------|-------|--------|
| $R_{\text{th}}$ | $1/3$ | [T] Theorem ($K=3$ from triadic decomposition + Bayesian dominance) |
| $\Phi_{\text{th}}$ | $1$ | [T] Theorem (T-129: unique self-consistent value) |
| $R^{(2)}_{\text{th}}$ | $1/4$ | [T] Theorem (L3 threshold) |
| $X^{(n)}_{\text{th}}$ | $1/(n+1)$ | [T] Universal formula |

## Stress Tensor

<!-- DRY: Canonical definition of σ_k in /docs/applied/coherence-cybernetics/theorems (T-92) -->
See [Viability](/docs/core/dynamics/viability) for a full description.

$$
\sigma_{\mathrm{sys}}(\Gamma) = [\sigma_A, \sigma_S, \sigma_D, \sigma_L, \sigma_E, \sigma_O, \sigma_U]^T \in \mathbb{R}^7
$$

**Viability condition:**
$$
\|\sigma_{\mathrm{sys}}(\Gamma)\|_\infty < 1
$$

**Viability margin:**
$$
\mathrm{margin}(\Gamma) = 1 - \|\sigma_{\mathrm{sys}}(\Gamma)\|_\infty > 0
$$

## Grothendieck Topology {#топология-гротендика}

See [Grothendieck topology](/docs/core/foundations/axiom-omega#топология-гротендика) and [Categorical formalism](/docs/proofs/categorical/categorical-formalism#63-топология-гротендика-на-densitymat-и-exp).

**Bures metric (canonical form):**
$$
d_B(\Gamma_1, \Gamma_2) = \arccos\left(\mathrm{Tr}\sqrt{\sqrt{\Gamma_1}\Gamma_2\sqrt{\Gamma_1}}\right) = \arccos(\sqrt{F})
$$

**Fidelity:**
$$
\mathrm{Fid}(\Gamma_1, \Gamma_2) = \left(\mathrm{Tr}\sqrt{\sqrt{\Gamma_1}\Gamma_2\sqrt{\Gamma_1}}\right)^2
$$

:::note Notation Fid vs F
$\mathrm{Fid}$ is used for fidelity in contexts where $F$ could be confused with the [experience functor](/docs/proofs/categorical/categorical-formalism#3-функтор-f-на-объектах) $F: \mathbf{DensityMat} \to \mathbf{Exp}$. In formulae where the context is unambiguous, the notation $F$ is permitted.
:::

:::note Two forms of the Bures metric
UHM uses **both forms** depending on context:

| Form | Formula | Application |
|------|---------|-------------|
| **Angular** | $d_B^{angle} = \arccos(\sqrt{F})$ | Geometric theorems ([emergent time](/docs/proofs/dynamics/emergent-time#41-метрика-бурес)) |
| **Chord** | $d_B^{chord} = \sqrt{2(1-\sqrt{F})}$ | Computations, [ΔF](/docs/core/dynamics/evolution#каноническое-delta-f), [specification](/docs/reference/specification#топология-гротендика) |

**Relation:** $d_B^{chord} = \sqrt{2(1 - \cos(d_B^{angle}))} \approx \sqrt{2} \cdot d_B^{angle}$ for small distances.
:::

**Bures ball:**
$$
B_B(\Gamma, r) = \{\Sigma \in \mathcal{C} : d_B(\Gamma, \Sigma) < r\}
$$

**Bures covering:** Family $\{\Phi_i: \Gamma_i \to \Gamma\}_{i \in I}$ covers $\Gamma$ if:
$$
\forall \epsilon > 0, \exists \delta > 0: \quad B_B(\Gamma, \delta) \subseteq \bigcup_{i \in I} \Phi_i(B_B(\Gamma_i, \epsilon))
$$

**Site:** Pair $(\mathcal{C}, J_{Bures})$ where $J_{Bures}$ is the coverage function.

**Classifier from topology:**
$$
\Omega = \mathcal{O}(\mathcal{C}, d_B)
$$

## Special Notation

| Notation | Meaning |
|----------|---------|
| $\lVert\cdot\rVert_F$ | Frobenius norm: $\lVert A\rVert_F = \sqrt{\mathrm{Tr}(A^\dagger A)} = \sqrt{\sum_{ij} \lvert a_{ij}\rvert^2}$ |
| $\lVert\cdot\rVert_\infty$ | Supremum norm: $\lVert x\rVert_\infty = \max_i \lvert x_i\rvert$ |
| $d_B(\cdot, \cdot)$ | Bures metric |
| $\mathrm{Fid}(\cdot, \cdot)$ / $F(\cdot, \cdot)$ | Fidelity; $\mathrm{Fid}$ preferred to distinguish from functor $F$ |
| $B_B(\Gamma, r)$ | Bures ball of radius $r$ centred at $\Gamma$ |
| $J_{Bures}$ | Bures coverage function (Grothendieck topology) |
| $\Theta(\cdot)$ | Heaviside function |
| $\delta_{ij}$ | Kronecker delta |
| $\mathrm{Tr}(\cdot)$ | Matrix trace |
| $A^\dagger$ | Hermitian conjugate |
| $\mathrm{Coh}_E$ | E-coherence (HS-projection $\pi_E$) **[T]**, $\in [1/7, 1]$; $= \|\pi_E(\Gamma)\|_{\mathrm{HS}}^2 / \|\Gamma\|_{\mathrm{HS}}^2$ — [master definition](/docs/core/foundations/axiom-septicity#e-coherence-definition), [HS-projection](/docs/core/foundations/axiom-septicity#hs-projection), [CC reference](/docs/applied/coherence-cybernetics/definitions#e-когерентность) |
| IDP | Information Distinguishability Principle **[D]** (T16) — [definition](/docs/core/foundations/axiom-septicity#формулировка-пир), built into A1+A2: distinguishability via $J_{\text{Bures}}$-coverings is identical to ontological distinguishability |
| $\varphi_{\text{coh}}$ | Coherence-preserving self-modelling — generalised φ-operator preserving coherences ([Fano channel](/docs/proofs/gap/fano-channel)) |
<!-- DRY: Canonical definition of κ(Γ) in /docs/core/foundations/axiom-septicity#категориальный-вывод-kappa0 -->
| $\kappa(\Gamma)$ | Regeneration coefficient: $\kappa(\Gamma) = \kappa_{\text{bootstrap}} + \kappa_0 \cdot \mathrm{Coh}_E$ |
| $D_{\text{diff}}$ | Differentiation dimension — number of dimensions in which $\Gamma$ deviates from $I/N$ |
<!-- DRY: Canonical definition P_crit = 2/7 in /docs/core/dynamics/viability#критическая-чистота -->
| $P_{\text{crit}}$ | Critical purity $= 2/N = 2/7$ — [theorem](/docs/proofs/dynamics/theorem-purity-critical) |
| $d_B^{chord}$ | Chord form of the Bures metric: $d_B^{chord} = \sqrt{2(1 - \sqrt{F(\rho, \sigma)})}$ |
| (AP), (PH), (QG), (V) | Four conditions of the Holon definition: autopoiesis, phenomenality, quantum geometry, viability |

## Categorical Notation

See [Categorical formalism](/docs/proofs/categorical/categorical-formalism) for a full description.

| Notation | Meaning |
|----------|---------|
| $\mathcal{C}$ | [Primitive category of UHM](/docs/core/foundations/axiom-omega#примитив) — sole primitive |
| $\mathbf{DensityMat}$ | [Category of density matrices](/docs/proofs/categorical/categorical-formalism#1-категория-densitymat) |
| $\mathbf{Exp}$ | [Category of experiential states](/docs/proofs/categorical/categorical-formalism#2-категория-exp) |
| $\mathbf{Hol}$ | Category of Holons |
| $T$ | [Terminal object](/docs/core/foundations/axiom-omega#свойство-3) — $\forall\Gamma, \exists! f: \Gamma \to T$ |
| $F: \mathbf{DensityMat} \to \mathbf{Exp}$ | [Experience functor](/docs/proofs/categorical/categorical-formalism#3-функтор-f-на-объектах) |
| $\mathrm{CPTP}$ | Completely Positive Trace-Preserving channels |
| $\mathrm{Mor}(\rho_1, \rho_2)$ | Morphisms between objects |
| $\otimes$ | Tensor product (composition of Holons) |
| $\mathbf{Exp}_\infty$ | [∞-groupoid of experience](/docs/proofs/categorical/categorical-formalism#10-infty-группоид-и-infty-топос-для-эмерджентного-времени) |
| $\mathbf{Exp}^{disc}_\infty$ | [Discrete ∞-groupoid](/docs/proofs/categorical/categorical-formalism#exp-disc-infty) for $N < \infty$ |
| $\mathbf{Sh}_\infty(\mathbf{Exp})$ | [∞-topos of ∞-sheaves](/docs/proofs/categorical/categorical-formalism#10-infty-группоид-и-infty-топос-для-эмерджентного-времени) over Exp |
| $\Omega\mathbf{Exp}_\infty$ | Loop space — emergent history |
| $D^b(X)$ | [Derived category](/docs/proofs/categorical/categorical-formalism#производные-категории) of sheaves on X |
| $\mathbf{Perv}(X)$ | [Category of perverse sheaves](/docs/proofs/categorical/categorical-formalism#производные-категории) |
| $\mathcal{T}_H$ | [∞-topos of Holons](/docs/proofs/categorical/categorical-formalism#infty-топос-голономов) with HoTT as internal logic |
| $\mathrm{Sh}_\infty(\mathcal{C})$ | ∞-topos of sheaves on category $\mathcal{C}$, sole primitive in $\Omega^7$ |
| $\mathrm{Map}(\Gamma, T)$ | Morphism space in an ∞-category (mapping space) |
| $\pi_n(X)$ | n-th homotopy group of space $X$ |
| $\simeq$ | Weak homotopy equivalence |
| $\Omega$ | [Subobject classifier](/docs/core/foundations/axiom-omega#внутренняя-логика) — unified source of L, L_k, τ |
| $\chi_S$ | [Characteristic morphism](/docs/core/structure/dimension-l#категориальное-определение) of subobject S: $\chi_S: \Gamma \to \Omega$ |
| $L_k$ | [Lindblad operators](/docs/core/dynamics/evolution#логический-лиувиллиан): $L_k = P_k = \lvert k\rangle\langle k\rvert$ — operator representatives of characteristic morphisms of atoms of Ω ([derivation](/docs/core/foundations/axiom-omega#lk-из-omega)). Notation $L_k = \sqrt{\chi_{S_k}}$ — convention ($\sqrt{P} = P$ for projectors) |
| $\mathcal{L}_0$ | Linear Liouvillian (without regeneration): $\mathcal{L}_0 = -i[H_{\text{eff}},\cdot] + \sum_k D_{L_k}$. Primitivity [T-39a [T]](/docs/core/operators/lindblad-operators#примитивность-ℒω); unique attractor $I/7$ |
| $\mathcal{L}_\Omega$ | [Full logical Liouvillian](/docs/core/dynamics/evolution#логический-лиувиллиан): $\mathcal{L}_\Omega = \mathcal{L}_0 + \mathcal{R}$ (with regeneration). Non-trivial attractor $\rho^*_\Omega \neq I/7$ [T] (T-96) |
| $\triangleright$ | [Temporal modality](/docs/proofs/dynamics/emergent-time#время-из-модальности) on Ω; $\tau_n = \triangleright^n(\mathrm{now})$ |
| $\mathcal{D}_\Omega \dashv \mathcal{R}$ | [Dissipation–regeneration adjunction](/docs/core/foundations/axiom-septicity#категориальный-вывод-kappa0); $\kappa_0 = \|\mathrm{Nat}(\mathcal{D}_\Omega, \mathcal{R})\|$ |
| **(МП)** | **Minimal representation principle** (historical condition, now **[T]** T11–T13): among equivalent BIBD$(7,3,\lambda)$ channels, $\lambda = 1$ is chosen — minimum number of operators ($b=7$). Proved as a theorem from (AP)+(PH)+(QG)+(V); bridge to P1+P2 fully closed **[T]**. [Bridge to P1+P2](/docs/core/foundations/axiom-septicity#мост-p1p2) |
| **(КГ)** | **Canonical grouping** (historical): categorically natural mechanism for grouping atoms of Ω into composite blocks. Replaced by the weaker (МП), which in turn has been proved as theorem T11–T13 |

## Coherence Cybernetics Notation

See [Coherence Cybernetics](/docs/applied/coherence-cybernetics/definitions) for a full description.

| Notation | Meaning |
|----------|---------|
| $\mathcal{V}$ | [Viability domain](/docs/core/dynamics/viability) |
| $\mathrm{VIT}$ | Viability Integrity Tensor |
| $\kappa_{\text{bootstrap}}$ | Minimum regeneration rate: $\kappa_{\text{bootstrap}} = \omega_0/7$ **[D]** scale; resolves the bootstrap paradox |
| $\kappa_0$ | Categorical norm: $\kappa_0 = \omega_0 \cdot |\gamma_{OE}| \cdot |\gamma_{OU}| / \gamma_{OO}$ **[T]** — [categorical derivation](/docs/core/foundations/axiom-septicity#категориальный-вывод-kappa0) |
| $\kappa(\Gamma)$ | Effective regeneration rate: $\kappa(\Gamma) = \kappa_{\text{bootstrap}} + \kappa_0 \cdot \mathrm{Coh}_E(\Gamma)$ **[T]** |
| $\mathrm{Coh}_E$ | $E$-coherence (HS-projection) **[T]**: $\mathrm{Coh}_E(\Gamma) = \dfrac{\|\pi_E(\Gamma)\|_{\mathrm{HS}}^2}{\|\Gamma\|_{\mathrm{HS}}^2} = \dfrac{\gamma_{EE}^2 + 2\sum_{i \neq E}\lvert\gamma_{Ei}\rvert^2}{\mathrm{Tr}(\Gamma^2)}$ — **canonical formula** ([master definition](/docs/core/foundations/axiom-septicity#e-coherence-definition), [HS-projection](/docs/core/foundations/axiom-septicity#hs-projection)) |
| $P_E$ | E-sector purity (42D): $P_E = \mathrm{Tr}(\rho_E^2)$, where $\rho_E = \mathrm{Tr}_{-E}(\Gamma)$ — **theoretical construction**, defined only in the extended 42D formalism ($\mathcal{H} = \mathbb{C}^{42}$). Formal equivalence $\mathrm{Coh}_E \approx P_E$ — **structural hypothesis [H]** ([details](/docs/applied/coherence-cybernetics/definitions#e-когерентность)) |
| $P_{\text{crit}}$ | Critical purity $= 2/7 \approx 0.286$ — [theorem](/docs/proofs/dynamics/theorem-purity-critical) |
| $\theta_i$ | Stress component thresholds |
| $H_{\text{eff}}$ | Effective Hamiltonian: $H_{\text{eff}}(\tau) = H_{6D} + \langle\tau\vert H_{\text{int}}\vert\tau\rangle_O$ — arises from the Page–Wootters constraint |
| $g_V(P)$ | V-preservation gate: $\mathrm{clamp}\!\bigl(\frac{P - P_{\mathrm{crit}}}{P_{\mathrm{opt}} - P_{\mathrm{crit}}}, 0, 1\bigr)$; activates regeneration at $P > P_{\mathrm{crit}}$ ([derivation](/docs/core/dynamics/evolution#теорема-v-preservation-gate)) |
| $\Theta(\Delta F)$ | Heaviside function of the free-energy change $\Delta F$; necessary condition from Landauer's principle (refined by $g_V(P)$) |
| $\rho_*$ ($= \Gamma_{\text{target}}$) | Unique stationary state of $\mathcal{L}_\Omega$ [T]: $\rho_* = \varphi(\Gamma) = \lim_{\tau\to\infty} e^{\tau\mathcal{L}_\Omega}[\Gamma]$ — regeneration target |
| $\omega_0$ | Fundamental clock frequency — parameter of the computational approximation; see [κ₀](/docs/core/foundations/axiom-septicity#категориальный-вывод-kappa0) |
| $D_{\mathrm{KL}}$ | Kullback–Leibler divergence: $D_{\mathrm{KL}}(p \| q) = \sum_i p_i \log(p_i / q_i)$ |

## Dimension Indices (Measurement Protocol) {#индексы-измерений-протокол-измерения}

Empirical indices for measuring Γ projections in AI systems. See [Measurement protocol](/docs/applied/research/measurement-protocol) for a full description.

| Index | Dimension | AI metric | Formula |
|-------|-----------|-----------|---------|
| $I_A$ | Articulation | Mutual information input↔latent | $I_A = I(\text{input}; \text{latent}) / H(\text{input})$ |
| $I_S$ | Structure | Jacobian rank | $I_S = \mathrm{rank}_\varepsilon(J_f) / \min(d_{\text{out}}, d_{\text{in}})$ |
| $I_D$ | Dynamics | Lyapunov exponent | $I_D = \max_i \lambda_i^{\text{Lyap}}$ (normalised) |
| $I_L$ | Logic | Layer commutators | $I_L = 1 - \|[f_i, f_j]\|_F / (\|f_i\| \cdot \|f_j\|)$ |
| $I_E$ | Interiority | Differentiation (entropy) | $I_E = D_{\text{diff}}^{\text{approx}} = \exp(S_{vN}(\rho_{\text{attn}}))$ — [see dimension E](/docs/core/structure/dimension-e#differentiation-threshold-dmin-2) |
| $I_O$ | Ground | Noise robustness | $I_O = 1 - \|\nabla_\epsilon \mathbf{h}\|_F$ |
| $I_U$ | Unity | Effective Φ (integration) | $I_U = \Phi_{\text{eff}} = \lambda_2(L_{\text{attn}}) / \lambda_{\max}(L_{\text{attn}})$ — [see dimension U](/docs/core/structure/dimension-u#мера-интеграции-φ) |

**Relation to Γ:** Diagonal elements $\gamma_{ii} \approx I_i^2$ (empirical calibration).

### Additional Applied Symbols

| Notation | Meaning |
|----------|---------|
| $G$ | Quasi-functor $\mathbf{AIState} \to \mathbf{DensityMat}$ — mapping of AI state to density matrix |
| $J_P$ | Coherence flow: $J_P = dP/d\tau$ |
| $\varepsilon_{\text{functor}}$ | Upper bound on the error of quasi-functor $G$ |
| $P_{\text{norm}}$ | Normalised purity: $(P - P_{\text{crit}}) / (1 - P_{\text{crit}})$ |
| $\mathbf{r}$ | Generalised Bloch vector: $\Gamma = I/N + \sum_k r_k \lambda_k / 2$ |

## Octonionic Notation

See [Structural derivation via octonions](/docs/proofs/minimality/theorem-octonionic-derivation) for a full description.

| Notation | Meaning |
|----------|---------|
| $\mathbb{O}$ | Octonion algebra — 8-dimensional normed division algebra over $\mathbb{R}$ |
| $\mathrm{Im}(\mathbb{O})$ | Imaginary part of the octonions; $\dim(\mathrm{Im}(\mathbb{O})) = 7$ |
| $e_1, \ldots, e_7$ | Imaginary units of the octonions; $e_i^2 = -1$, $e_i e_j = -e_j e_i$ ($i \neq j$) |
| $G_2$ | $\mathrm{Aut}(\mathbb{O})$ — 14-parameter automorphism group of the octonions; $G_2 \subset SO(7)$ |
| $\mathrm{PG}(2,2)$ | Fano plane — projective plane over $\mathbb{F}_2$; 7 points, 7 lines, 3 points per line |
| $[x, y, z]$ | Associator: $[x, y, z] = (xy)z - x(yz)$; measure of non-associativity |
| $H(7,4)$ | Hamming code: 4 information + 3 check bits; connection to PG(2,2) |
| **P1** | Theorem [T]: space of internal degrees of freedom $\cong \mathrm{Im}(\mathbb{A})$ for a division algebra $\mathbb{A}$ (derived along the T15 chain) |
| **P2** | Theorem [T]: non-associativity ($[x, y, z] \neq 0$ for some $x, y, z$) (derived along the T15 chain) |

:::warning Status of octonionic notation [I]
The correspondence $e_i \leftrightarrow$ dimension — **interpretation** [I]. Mathematical operations on $\mathbb{O}$ (multiplication, associator) are strict [T]; their physical realisation in the space $\{A,S,D,L,E,O,U\}$ — [open problem](/docs/proofs/minimality/theorem-octonionic-derivation#открытые-проблемы).
:::

## Gap Dynamics and Fano Structure

<!-- DRY: Canonical definition of Gap operator in /docs/core/dynamics/gap-operator -->
Symbols related to the [Gap operator](/docs/core/dynamics/gap-dynamics), [Gap thermodynamics](/docs/core/dynamics/gap-thermodynamics) and [Fano selection rules](/docs/physics/gauge-symmetry/fano-selection-rules).

| Notation | Meaning |
|----------|---------|
| $\hat{G}$ | [Gap operator](/docs/core/dynamics/gap-dynamics): $\hat{G} = \mathrm{Im}(\Gamma) \in \mathfrak{so}(7)$ — imaginary part of the coherence matrix |
| $P_{\mathrm{Fano}}$ | [Fano predictive channel](/docs/physics/gauge-symmetry/fano-selection-rules): $P_{\mathrm{Fano}}(\Gamma) = \tfrac{1}{3}\sum_p \Pi_p \Gamma \Pi_p$ — averaging over Fano lines |
| $\Pi_p$ | Projector onto the 3-dimensional subspace of Fano line $p$ ($p = 1, \ldots, 7$) |
| $\alpha^*$ | Optimal self-modelling parameter: $\alpha^* = \operatorname{argmin} F[P_\alpha;\, \Gamma]$ |
| $T_{\mathrm{eff}}$ | [Effective Gap temperature](/docs/core/dynamics/gap-thermodynamics): $T_{\mathrm{eff}} = (\Gamma_2 / \kappa_0) \cdot k_B \cdot T_{\mathrm{phys}}$ |
| $\xi_F$ | Fano correlation length: $\xi_F \sim 160\;\text{pc}$ — spatial correlation scale of Fano modes |
| $\Theta_M$ | Winding theta-function with Fano character |
| $Z_\Phi(s)$ | Epstein zeta-function with Fano character |
| $B^{(b)}$ | Bilinear form on $(S^1)^{21}$ with Fano contraction |
| $N_F$ | Number of uncorrelated Fano modes: $N_F \sim 6{,}8 \times 10^{23}$ |
| $r = \kappa / \Gamma_2$ | Dimensionless viability parameter — ratio of regeneration rate to decoherence rate |
| $t = T_{\mathrm{eff}} / T_c$ | Dimensionless temperature — reduced to the critical value $T_c$ |

## Spectral Geometry and Bimodular Construction

Symbols related to the [bimodular construction](/docs/proofs/physics/bimodule-construction) of SM representations (T-178–T-181).

| Notation | Meaning |
|----------|---------|
| $H_F$ | Finite Hilbert space of the spectral triple as an $(A_{\text{int}}, A_{\text{int}}^\circ)$-bimodule (KO-dim 6). Decomposition into irreducible bimodules reproduces one generation of SM fermions [T-178 [T]] |
| KO-dim | KO-dimension $= 6$ (mod 8) — classification invariant of the real structure $J$; Connes's conditions: $J^2 = 1$, $JD = DJ$, $J\gamma = -\gamma J$ |
| $D_{\text{int}}$ | Dirac operator of the internal space; its eigenvalues determine the fermion mass ratios [T-180 [T]] |

---

**Related documents:**
- [Glossary](./glossary) — definitions of terms
- [Mathematical apparatus](/docs/reference/specification) — formal definitions
- [Computational implementation](/docs/reference/computational) — Python code
- [Coherence matrix](/docs/core/dynamics/coherence-matrix) — definition of $\Gamma$
- [Evolution](/docs/core/dynamics/evolution) — equation $d\Gamma(\tau)/d\tau$
- [Emergent time](/docs/proofs/dynamics/emergent-time) — derivation of τ from the structure of Γ
- [Viability](/docs/core/dynamics/viability) — measure $P$ and $P_{\text{crit}}$
- [Self-observation](/docs/consciousness/foundations/self-observation) — measures $R$, $\Phi$, $D_{\text{diff}}$, $C$
- [Interiority hierarchy](/docs/proofs/consciousness/interiority-hierarchy) — levels L0→L1→L2→L3→L4
- [Categorical formalism](/docs/proofs/categorical/categorical-formalism) — functor $F$, ∞-groupoid $\mathbf{Exp}_\infty$
- [Formalisation of operator φ](/docs/proofs/categorical/formalization-phi) — CPTP channels
- [Structural derivation via octonions](/docs/proofs/minimality/theorem-octonionic-derivation) — P1+P2 → 𝕆 → N=7
- [Gap dynamics](/docs/core/dynamics/gap-dynamics) — Gap operator $\hat{G}$, bifurcations, non-Markovian dynamics
- [Gap thermodynamics](/docs/core/dynamics/gap-thermodynamics) — $T_{\mathrm{eff}}$, variational principle, FDT
- [Fano selection rules](/docs/physics/gauge-symmetry/fano-selection-rules) — $P_{\mathrm{Fano}}$, $\Pi_p$, Yukawa hierarchy
- [Bimodular construction](/docs/proofs/physics/bimodule-construction) — SM representations from bimodules of the spectral triple (T-178–T-181)
