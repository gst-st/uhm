---
sidebar_position: 2
title: Notation
description: Mathematical notation of UHM theory
---

# Mathematical Notation

The numerical formulas below use the selected $N=7$ model with a declared semantic frame [P]. Processes, the Bures site, logical support and dynamics have different types; the [mathematical kernel](/docs/reference/mathematical-kernel) fixes their interface.

:::warning Potential notation conflicts
In UHM theory, some symbols have multiple meanings depending on context:
- $D$ — [Dynamics dimension](/docs/core/structure/dimension-d) **vs** $D_{\text{diff}}$ — [differentiation measure](/docs/consciousness/foundations/self-observation#мера-сознательности-c)
- $\mathcal{H}$ — Hilbert space **vs** $H$ — Hamiltonian **vs** $\mathcal{H}_\Gamma$ — Hessian of free energy (in [Freedom](/docs/core/foundations/consequences#freedom-конечномерное))
- $\Phi$ — [integration measure](/docs/core/structure/dimension-u#мера-интеграции-φ). For denoting arbitrary CPTP channels, $\Psi$ is used
- $R$ — the **canonical** [reflection measure](/docs/consciousness/foundations/self-observation#мера-рефлексии-r) $1/(7P) \in [1/7, 1]$ (conscious band $[1/3, 1/2)$) **vs** $R_\varphi$ — reflection as **self-model quality** (can be negative; its range depends on $M$) (formerly also written $Q_\varphi$) **vs** $R^{(n)}$ — the fidelity tower ($n \geq 2$) **vs** $R_{ij}$ — sectoral reflection **vs** $\mathcal{R}$ — regenerative term. The measure forms are told apart in [the three working forms of R](/docs/consciousness/foundations/self-observation#формы-r)
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

<!-- DRY: Canonical definition of Γ in /docs/core/dynamics/coherence-matrix -->
<!-- DRY: Canonical definition P = Tr(Γ²) in /docs/core/dynamics/viability#определение-чистоты -->

| Symbol | Meaning | Definition |
|--------|---------|------------|
| $\mathcal{C}$ | [Primitive category](/docs/core/foundations/axiom-omega#примитив) | A declared small indexing category; it does not alone determine $N$, channels or dynamics |
| $\Gamma$ | [Coherence matrix](/docs/core/dynamics/coherence-matrix) | $\Gamma \in \mathcal{L}(\mathcal{H})$, $\Gamma^\dagger = \Gamma$, $\Gamma \geq 0$, $\mathrm{Tr}(\Gamma) = 1$ |
| $\mathbb{H}$ | [Holon](/docs/core/structure/holon) | Minimal self-sufficient unit of reality |
| $\mathcal{H}$ | Hilbert space | $\mathcal{H} = \mathbb{C}^7$ — see [Seven dimensions](/docs/core/structure/dimensions) |
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
| $T$ | [Terminal object](/docs/reference/mathematical-kernel#terminal-time) | $1_{\mathcal E}$ in the topos; the one-dimensional system in the process category. Distinct from $\Gamma_*$ and $I/7$ |
| $S_\alpha$ | [Stratum](/docs/core/foundations/spacetime#стратификация-x) | A specified stratification $X=\bigsqcup_\alpha S_\alpha$; it does not follow from the nerve or terminality |
| $d_{strat}$ | [Stratified metric](/docs/core/foundations/spacetime#метрика-конна) | $d_{strat}(\omega_1, \omega_2) = \inf_\gamma \int_\gamma ds_\alpha$ |
| $\text{Link}(T)$ | Link of a distinguished point | Determined by local geometry; terminality does not specify a sphere |
| $H^*(X)$ | Cohomology | A contractible nerve of an indexing category with a terminal object has zero positive cohomology with constant coefficients; this is not a claim for every sheaf |
| $H^*_{loc}(X,T)$ | Local cohomology | For a conical neighbourhood $C(K)$: $H^k_{loc}(X,T;A)\cong\widetilde H^{k-1}(K;A)$; the link $K$ is specified separately |
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

**[Chosen regenerative term](/docs/core/dynamics/evolution#3-регенеративный-член) [D]:**

$$
\mathcal{R}[\Gamma, E] = \kappa(\Gamma) \cdot (\rho_* - \Gamma) \cdot g_V(P)
$$

where:
- $a(\Gamma)=\kappa(\Gamma)g_V(P)\ge0$ is a chosen rate; the logical support adjunction does not determine it.
- $\rho_*=M(\Gamma)$ is a specified numerical target in $D_7$, not a logical subobject or necessarily a stationary state.
- $a(\Gamma)(M(\Gamma)-\Gamma)$ is a vector field, not a channel. With locally Lipschitz $a,M$ and $M(D_7)\subseteq D_7$, it preserves states together with the GKSL part.
- $g_V(P)=\mathrm{clamp}((P-P_{\mathrm{crit}})/(P_{\mathrm{opt}}-P_{\mathrm{crit}}),0,1)$ is a chosen gate [D], not a universally derived form.

Use the [state-preserving split step](/docs/core/dynamics/evolution#сохранение-положительности) for a finite update.

## Commutators and Anticommutators

| Notation | Definition |
|----------|------------|
| $[A, B]$ | $AB - BA$ (commutator) |
| $\{A, B\}$ | $AB + BA$ (anticommutator) |

## Interiority Operators (Dimension E)

See [Interiority Dimension](/docs/core/structure/dimension-e) and [Exp Category](/docs/proofs/categorical/categorical-formalism#2-категория-exp).

| Notation | Meaning |
|----------|---------|
| $\rho_E$ | State of a specified experiential readout; partial trace requires an explicit tensor factorization, not a single named axis $E$ |
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
| [Reflection $R$](/docs/consciousness/foundations/self-observation#мера-рефлексии-r) | $R(\Gamma) = R_{\text{canonical}} = \dfrac{1}{7P(\Gamma)}$, where $P = \mathrm{Tr}(\Gamma^2)$; equivalent to $1 - \dfrac{\|\Gamma - I/7\|_F^2}{P}$. Not to be confused with the self-model quality $R_\varphi = 1 - \|\Gamma - \varphi(\Gamma)\|_F^2 / P$ (formerly also written $Q_\varphi$) — see [the three working forms of R](/docs/consciousness/foundations/self-observation#формы-r) | $[1/7, 1]$ |
| [Consciousness $C$](/docs/consciousness/foundations/self-observation#мера-сознательности-c) | $C(\Gamma) = \Phi \times R$ **[T]** (T-140); $D_{\text{diff}} \geq 2$ — separate viability condition | $[0, +\infty)$ |
| Hessian score $\mathrm{Freedom}$ [D] | $1+\dim\ker\nabla^2\mathcal F$ for a specified $C^2$ potential and $d$-dimensional domain; the kernel equals the critical-manifold tangent space only under Morse–Bott hypotheses. No universal CPTP monotonicity or agency follows. | $\{1,\ldots,d+1\}$; $d=48$ on the full-rank $D_7$ stratum |
| Logarithmic Hessian score [D] | $S_{\mathrm{freedom}}=\log\mathrm{Freedom}$; no identification with physical entropy | $[0,\log(d+1)]$ |

## Self-Modelling Operator

Four constructions have different types:

| Symbol | Type and scope |
|---|---|
| $L_G$ | $\mathcal E_{/G}\to\mathrm{Sub}_{\mathcal E}(G)$, image/$(-1)$-truncation in the slice; $L_G\dashv i_G$ [T] |
| $M=\varphi$ | A specified numerical self-model $D_7\to D_7$ [D]; it may be nonlinear |
| $\Psi_\lambda$ | A channel with fixed parameter $\lambda$: $\Psi_\lambda(X)=\sum_mK_{m,\lambda}XK_{m,\lambda}^\dagger$, $\sum_mK_{m,\lambda}^\dagger K_{m,\lambda}=I$ [T] |
| $r$ | $r(\Gamma)=\lim_{t\to\infty}\Phi_t(\Gamma)$ on a forward-invariant domain containing all its fixed-point limits; then $r^2=r$ [T]. Otherwise extend the domain before composing. |

The equality $M(\Gamma)=\Psi_{\lambda(\Gamma)}(\Gamma)$ does not make $M$ a single linear CPTP channel. Use $e^{t\mathcal L_0}$ for a frozen linear generator and $\Phi_t$ for nonlinear dynamics.

If the **specified** $M$ is a contraction in a chosen complete metric with constant $k<1$, Banach's theorem gives a unique fixed point and $d(M^n\Gamma_0,\Gamma_*)\le k^n d(\Gamma_0,\Gamma_*)$. An arbitrary CPTP channel need not be a strict contraction. A numerical fixed point expresses consistency of $M$; interpreting it as self-knowledge requires an independent error model.

See the [typed formalization of φ](/docs/proofs/categorical/formalization-phi).

## Interiority Hierarchy

See the [rigorous specification](/docs/proofs/consciousness/interiority-hierarchy). This taxonomy is a model definition [D]; its level numbers do not automatically denote truncation degrees of a topos object.

| Level | Condition |
|---|---|
| L0 | A specified experiential realization with state $\rho_E$; reduction requires a tensor factorization or a declared readout |
| L1 | L0 and a nontrivial specified phenomenal geometry |
| L2 | The chosen $\mathrm{Cap}_2$ gate: $P>2/7$, $R\ge1/3$, $\Phi\ge1$, $D_{\mathrm{diff}}\ge2$ |
| L3 | L2 and a nonvacuous calibrated metamodel certificate $\mathsf{MetaCert}_2$ on independent probes |
| L4 | L3 and a compatible tower of certificates at all orders; physical realizability is a separate question |

The numbers $R_{\mathrm{th}}=1/3$, $\Phi_{\mathrm{th}}=1$, $D_{\min}=2$ specify the chosen gate. Algebraic consequences of these choices are [T]; identifying them with consciousness is [H]/[I]. The former universal $R^{(2)}_{\mathrm{th}}=1/4$, $X^{(n)}_{\mathrm{th}}=1/(n+1)$ and $\mathrm{SAD}_{\max}=3$ are withdrawn [✗]. Fidelity between iterations of one $M$ does not replace a depth certificate.

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

**Relation:** $d_B^{chord} = \sqrt{2(1 - \cos(d_B^{angle}))} = 2\sin(d_B^{angle}/2) \approx d_B^{angle}$ for small distances.
:::

**Bures ball:** $B_B(\Gamma,r)=\{\Sigma\in D_N:d_B(\Gamma,\Sigma)<r\}$.

**Site:** $\mathcal O_N=\operatorname{Open}(D_N,d_B)$ with inclusions as arrows. A family $(U_i\subseteq U)$ covers $U$ iff $\bigcup_iU_i=U$. Pullback along an inclusion $V\subseteq U$ is the family of intersections $V\cap U_i$.

**Topos and classifier:** $\mathcal E_N=\operatorname{Sh}_\infty(\mathcal O_N,J_{\mathrm{open}})$; $\Omega$ is the sheaf of opens, $\Omega(U)=\operatorname{Open}(U)$, not a matrix algebra of seven projections. CPTP channels are Bures-continuous and induce geometric morphisms through inverse images of opens. The former channel-ball image-cover condition is not used. See the [kernel](/docs/reference/mathematical-kernel#bures-site).

## Special Notation

<!-- DRY: Canonical definition of κ(Γ) in /docs/core/foundations/axiom-septicity#категориальный-вывод-kappa0 -->
<!-- DRY: Canonical definition P_crit = 2/7 in /docs/core/dynamics/viability#критическая-чистота -->

| Notation | Meaning |
|----------|---------|
| $\lVert\cdot\rVert_F$ | Frobenius norm: $\lVert A\rVert_F = \sqrt{\mathrm{Tr}(A^\dagger A)} = \sqrt{\sum_{ij} \lvert a_{ij}\rvert^2}$ |
| $\lVert\cdot\rVert_\infty$ | Supremum norm: $\lVert x\rVert_\infty = \max_i \lvert x_i\rvert$ |
| $d_B(\cdot, \cdot)$ | Bures metric |
| $\mathrm{Fid}(\cdot, \cdot)$ / $F(\cdot, \cdot)$ | Fidelity; $\mathrm{Fid}$ preferred to distinguish from functor $F$ |
| $B_B(\Gamma, r)$ | Bures ball of radius $r$ centred at $\Gamma$ |
| $J_{Bures}$ | Open-cover topology on $\mathcal O_N$ |
| $\Theta(\cdot)$ | Heaviside function |
| $\delta_{ij}$ | Kronecker delta |
| $\mathrm{Tr}(\cdot)$ | Matrix trace |
| $A^\dagger$ | Hermitian conjugate |
| $\mathrm{Coh}_E$ | E-coherence (HS-projection $\pi_E$) **[T]**, $\in [0, 1]$; $= \|\pi_E(\Gamma)\|_{\mathrm{HS}}^2 / \|\Gamma\|_{\mathrm{HS}}^2$ — [master definition](/docs/core/foundations/axiom-septicity#e-coherence-definition), [HS-projection](/docs/core/foundations/axiom-septicity#hs-projection), [CC reference](/docs/applied/coherence-cybernetics/definitions#e-когерентность) |
| IDP | Declared distinguishability definition [D] and ontological interpretation [I]. Specify the observation family and Bures open site; their existence does not prove a phenomenal identification. |
| $\varphi_{\text{coh}}$ | Coherence-preserving self-modelling — generalised φ-operator preserving coherences ([Fano channel](/docs/proofs/gap/fano-channel)) |
| $\kappa(\Gamma)$ | Chosen effective rate, e.g. $\kappa_{\mathrm{bootstrap}}+\kappa_0\mathrm{Coh}_E(\Gamma)$ [D] |
| $D_{\text{diff}}$ | Differentiation dimension — number of dimensions in which $\Gamma$ deviates from $I/N$ |
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
| $\Omega$ | [Subobject classifier](/docs/reference/mathematical-kernel#support-reflector), distinct from chosen frame projectors |
| $\chi_S$ | $\chi_S:G\to\Omega$ classifies a subobject of the topos object $G$; no implicit density-matrix realization |
| $L_k$ | Chosen Lindblad operators, e.g. $L_k=\lvert k\rangle\langle k\rvert$ in a declared frame. $\sum_kL_k^\dagger L_k=I$ holds for this instrument, not for abstract characteristic maps |
| $\mathcal{L}_0$ | Fixed linear GKSL generator $-i[H,\cdot]+\sum_kD_{L_k}$; a unique $I/7$ attractor requires the stated unitality and primitivity hypotheses |
| $\mathcal{L}_\Omega$ | Historical name for the full vector field $\mathcal L_0(\Gamma)+a(\Gamma)(M(\Gamma)-\Gamma)$; generally nonlinear, with conditional stationary states |
| $\triangleright$ | [Temporal modality](/docs/proofs/dynamics/emergent-time#время-из-модальности) on Ω; $\tau_n = \triangleright^n(\mathrm{now})$ |
| $\mathcal{D}_\Omega \dashv \mathcal{R}$ | Historical dissipation–regeneration notation; the claimed numerical adjunction/rate derivation is withdrawn [✗]. The valid support adjunction is $L_G\dashv i_G$ in the slice |
| **(МП)** | A chosen minimal frame/channel representation; the universal derivation from (AP)+(PH)+(QG)+(V) and the closed P1/P2 bridge are withdrawn [✗] |
| **(КГ)** | Historical canonical-grouping proposal [H]; the classifier does not select a seven-atom instrument |

## Coherence Cybernetics Notation

See [Coherence Cybernetics](/docs/applied/coherence-cybernetics/definitions) for a full description.

| Notation | Meaning |
|----------|---------|
| $\mathcal{V}$ | [Viability domain](/docs/core/dynamics/viability) |
| $\mathrm{VIT}$ | Viability Integrity Tensor |
| $\kappa_{\text{bootstrap}}$ | Minimum regeneration rate: $\kappa_{\text{bootstrap}} = \omega_0/7$ **[D]** scale; resolves the bootstrap paradox |
| $\kappa_0$ | Chosen numerical rate/scale; the displayed coherence formula is a model law, not a categorical norm theorem |
| $\kappa(\Gamma)$ | Effective regeneration rate: $\kappa(\Gamma) = \kappa_{\text{bootstrap}} + \kappa_0 \cdot \mathrm{Coh}_E(\Gamma)$ **[T]** |
| $\mathrm{Coh}_E$ | $E$-coherence (HS-projection) **[T]**: $\mathrm{Coh}_E(\Gamma) = \dfrac{\|\pi_E(\Gamma)\|_{\mathrm{HS}}^2}{\|\Gamma\|_{\mathrm{HS}}^2} = \dfrac{\gamma_{EE}^2 + 2\sum_{i \neq E}\lvert\gamma_{Ei}\rvert^2}{\mathrm{Tr}(\Gamma^2)}$ — **canonical formula** ([master definition](/docs/core/foundations/axiom-septicity#e-coherence-definition), [HS-projection](/docs/core/foundations/axiom-septicity#hs-projection)) |
| $P_E$ | E-sector purity (42D): $P_E = \mathrm{Tr}(\rho_E^2)$, where $\rho_E = \mathrm{Tr}_{-E}(\Gamma)$ — **theoretical construction**, defined only in the extended 42D formalism ($\mathcal{H} = \mathbb{C}^{42}$). Formal equivalence $\mathrm{Coh}_E \approx P_E$ — **structural hypothesis [H]** ([details](/docs/applied/coherence-cybernetics/definitions#e-когерентность)) |
| $P_{\text{crit}}$ | Critical purity $= 2/7 \approx 0.286$ — [theorem](/docs/proofs/dynamics/theorem-purity-critical) |
| $\theta_i$ | Stress component thresholds |
| $H_{\text{eff}}$ | Effective Hamiltonian: $H_{\text{eff}}(\tau) = H_{6D} + \langle\tau\vert H_{\text{int}}\vert\tau\rangle_O$ — arises from the Page–Wootters constraint |
| $g_V(P)$ | V-preservation gate: $\mathrm{clamp}\!\bigl(\frac{P - P_{\mathrm{crit}}}{P_{\mathrm{opt}} - P_{\mathrm{crit}}}, 0, 1\bigr)$; activates regeneration at $P > P_{\mathrm{crit}}$ ([derivation](/docs/core/dynamics/evolution#теорема-v-preservation-gate)) |
| $\Theta(\Delta F)$ | Heaviside function of the free-energy change $\Delta F$; necessary condition from Landauer's principle (refined by $g_V(P)$) |
| $\rho_*$ ($= \Gamma_{\text{target}}$) | Numerical target $\rho_*=M(\Gamma)$ [D], distinct from an equilibrium $\Gamma_*$ and a basin limit $r(\Gamma)=\lim_{t\to\infty}\Phi_t(\Gamma)$ when that limit exists |
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
| **P1** | Explicit algebraic realization premise; it is not derived from generic (AP)/(PH)/(QG) |
| **P2** | Nonassociativity premise for the selected algebra; with a finite-dimensional real alternative division algebra it selects the octonionic case conditionally |

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
| $\alpha^*$ | Chosen Fano mixing parameter; a specified optimization problem needs its own objective and hypotheses |
| $T_{\mathrm{eff}}$ | [Effective Gap temperature](/docs/core/dynamics/gap-thermodynamics): $T_{\mathrm{eff}} = (\Gamma_2 / \kappa_0) \cdot k_B \cdot T_{\mathrm{phys}}$ |
| $\xi_F$ | Fano correlation length: $\xi_F \sim 160\;\text{pc}$ — spatial correlation scale of Fano modes |
| $\Theta_M$ | Winding theta-function with Fano character |
| $Z_\Phi(s)$ | Epstein zeta-function with Fano character |
| $B^{(b)}$ | Bilinear form on $(S^1)^{21}$ with Fano contraction |
| $N_F$ | Number of uncorrelated Fano modes: $N_F \sim 6{,}8 \times 10^{23}$ |
| $r = \kappa / \Gamma_2$ | Dimensionless viability parameter — ratio of regeneration rate to decoherence rate |
| $t = T_{\mathrm{eff}} / T_c$ | Dimensionless temperature — reduced to the critical value $T_c$ |

## Spectral Geometry and Bimodular Construction

Symbols related to the [bimodular construction](/docs/proofs/physics/bimodule-construction) of SM representations (T-178–T-181). The finite space $H_F$ is Connes' imported one: the derivation from the UHM spectral triple (T-178) is retracted [✗] (2026-09-25), and T-179 is retracted as stated.

| Notation | Meaning |
|----------|---------|
| $H_F$ | Finite Hilbert space of the spectral triple as an $(A_{\text{int}}, A_{\text{int}}^\circ)$-bimodule (KO-dim 6). Decomposition into irreducible bimodules reproduces one generation of SM fermions — for Connes' imported $H_F$; T-178 (a derivation from the UHM triple) is retracted [✗] 2026-09-25 |
| KO-dim | KO-dimension (mod 8) — classification invariant of a real structure $J$; KO-dimension 6 (Connes' finite space): $J^2 = 1$, $JD = DJ$, $J\gamma = -\gamma J$. Not available on the UHM $\mathbb{C}^7$ (odd dimension; retracted 2026-09-25) |
| $D_{\text{int}}$ | Dirac operator of the internal space; its eigenvalues determine the fermion mass ratios [T-180 [C at (SV)]] |

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
- [Formalisation of operator φ](/docs/proofs/categorical/formalization-phi) — typed support, numerical self-models and frozen CPTP realizations
- [Structural derivation via octonions](/docs/proofs/minimality/theorem-octonionic-derivation) — conditional octonionic realization with explicit premises
- [Gap dynamics](/docs/core/dynamics/gap-dynamics) — Gap operator $\hat{G}$, bifurcations, non-Markovian dynamics
- [Gap thermodynamics](/docs/core/dynamics/gap-thermodynamics) — $T_{\mathrm{eff}}$, variational principle, FDT
- [Fano selection rules](/docs/physics/gauge-symmetry/fano-selection-rules) — $P_{\mathrm{Fano}}$, $\Pi_p$, Yukawa hierarchy
- [Bimodular construction](/docs/proofs/physics/bimodule-construction) — SM representations from bimodules of Connes' imported finite space $H_F$ (T-178–T-181; the derivation from the UHM spectral triple, T-178, is retracted [✗] 2026-09-25, T-179 as stated)
