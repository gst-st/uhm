---
sidebar_position: 1
title: Glossary
description: Definitions of the main terms of UHM theory
---

# Glossary

:::tip Navigation
For mathematical notation see [Notation](./notation). For verification criteria see [Falsifiability](./falsifiability).
:::

## Core Terms

| Term | Definition |
|------|------------|
| **$\mathcal{C}$ (Category)** | [Primitive category](/docs/core/foundations/axiom-omega#примитив) — **sole primitive**; small category with a finite number of objects |
| **$\Gamma$ (Gamma)** | [Coherence matrix](/docs/core/dynamics/coherence-matrix) — Hermitian positive semi-definite matrix with $\mathrm{Tr}(\Gamma) = 1$ |
| **$\mathbb{H}$ (Holon)** | [Minimal self-sufficient unit](/docs/core/structure/holon) of reality, containing an image of the whole |
| **$\Gamma_\odot$ (Source)** | [Primordial pure state](/docs/physics/cosmology-phys/origin) — superposition of all dimensions |
| **$P$ (Purity)** | $P = \mathrm{Tr}(\Gamma^2) \in [1/7, 1]$ — [coherence measure](/docs/core/dynamics/viability#определение-чистоты) |
| **$S_{vN}$** | Von Neumann entropy $S_{vN} = -\mathrm{Tr}(\Gamma \log \Gamma) \in [0, \log 7]$ |
| **Coherence** | Quantum correlations between dimensions — off-diagonal elements $\gamma_{ij}$ of matrix $\Gamma$ |
| **Decoherence** | Process of losing coherence through interaction with the environment — see [dissipative term](/docs/core/dynamics/evolution#логический-лиувиллиан) |
| **Unitary evolution** | Deterministic evolution of a closed system that preserves $P$ |
| **Internal time τ** | Emergent parameter arising from correlations between O and the remaining dimensions — [theorem](/docs/proofs/dynamics/emergent-time) |
| **Page–Wootters mechanism** | Construction for deriving time from the structure of $\Gamma_{total}$ with the constraint $\hat{C} \cdot \Gamma_{total} = 0$ |
| **Bures metric** | $d_B(\Gamma_1, \Gamma_2) = \arccos(\sqrt{F})$, where $F = \left(\text{Tr}\sqrt{\sqrt{\Gamma_1}\Gamma_2\sqrt{\Gamma_1}}\right)^2$ — [Uhlmann fidelity](/docs/proofs/dynamics/emergent-time#41-метрика-бурес); angular distance in state space |
| **∞-groupoid Exp_∞** | Extension of the Exp category with 1-morphisms (time) and n-morphisms (homotopies) |
| **∞-topos Sh_∞(Exp)** | Category of ∞-sheaves on Exp_∞ with internal temporal modal logic |

## Base Space and Stratification Terms

| Term | Definition |
|------|------------|
| **Base space X** | $X = \|N(\mathcal{C})\|$ — [geometric realisation of the nerve](/docs/core/foundations/spacetime#базовое-пространство) of category $\mathcal{C}$; derived endogenously, not postulated |
| **Nerve N(𝒞)** | [Simplicial set](/docs/core/foundations/spacetime#нерв-категории): 0-simplices = objects, n-simplices = chains of morphisms |
| **Terminal object T** | $T = \Gamma^*$ — [global attractor](/docs/core/foundations/axiom-omega#свойство-3); $\forall\Gamma, \exists! f: \Gamma \to T$; ensures contractibility of X |
| **Stratification** | Decomposition $X = \bigsqcup_\alpha S_\alpha$ into [strata](/docs/core/foundations/spacetime#стратификация-x); $S_0 = \{T\}$ |
| **Local–global dichotomy** | [Principle](/docs/core/foundations/spacetime#локально-глобальная-дихотомия): $H^*(X) = 0$ globally (monism), $H^*_{loc}(X,T) \neq 0$ locally (physics) |
| **Cohomological monism** | [Theorem](/docs/core/foundations/consequences#когомологический-монизм): $H^n(X, \mathcal{F}) = 0$ for $n > 0$ — monism as a mathematical fact |
| **Stratified metric d_strat** | $d_{strat}(\omega_1, \omega_2) = \inf_\gamma \int_\gamma ds_\alpha$ — [Connes metric](/docs/core/foundations/spacetime#метрика-конна) on strata |
| **Link Link(T)** | Topological structure near T; $\text{Link}(T) \cong S^6$ — 6-sphere |
| **Arrow of time (geometric)** | [Stratum collapse](/docs/core/dynamics/evolution#стрела-времени-эволюция): $\dim(X_\tau) \geq \dim(X_{\tau+1})$ towards terminal T |
| **IC cohomology** | [Intersection cohomology](/docs/proofs/categorical/categorical-formalism#производные-категории) — cohomology of strata capturing the "hidden topology" |
| **Derived category D^b(X)** | [Bounded derived category](/docs/proofs/categorical/categorical-formalism#производные-категории) of sheaves on stratified X |

## Holon Dimensions

See [Seven dimensions](/docs/core/structure/dimensions) for a full description.

| Term | Definition |
|------|------------|
| **Dimension** | One of the 7 fundamental aspects of the [Holon](/docs/core/structure/holon) |
| **[$A$ — Articulation](/docs/core/structure/dimension-a)** | Dimension I — capacity to differentiate |
| **[$S$ — Structure](/docs/core/structure/dimension-s)** | Dimension II — capacity to hold form |
| **[$D$ — Dynamics](/docs/core/structure/dimension-d)** | Dimension III — capacity to change |
| **[$L$ — Logic](/docs/core/structure/dimension-l)** | Dimension IV — capacity to be consistent |
| **[$E$ — Interiority](/docs/core/structure/dimension-e)** | Dimension V — capacity to experience |
| **[$O$ — Ground](/docs/core/structure/dimension-o)** | Dimension VI — connection to the Source and **internal clock** (Page–Wootters) |
| **[$U$ — Unity](/docs/core/structure/dimension-u)** | Dimension VII — integration of all dimensions |

## Interiority Hierarchy (L0→L1→L2→L3→L4)

See [Interiority hierarchy](/docs/proofs/consciousness/interiority-hierarchy) for formal definitions and proofs.

:::warning Terminological discipline
The term **"qualia"** is used ONLY for level L2 (cognitive qualia). For L0 and L1, the terms "interiority" and "phenomenal geometry" are used respectively. L3 and L4 are post-reflexive levels. This is a categorically correct distinction.
:::

| Term | Level | Definition |
|------|-------|------------|
| **Interiority** | L0 | Fundamental property of "having an inside"; $\mathrm{Int}(S) := \exists \rho_E = \mathrm{Tr}_{-E}(\Gamma_S)$; corresponds to $\tau_{\leq 0}(\mathrm{Exp}_\infty)$ |
| **Phenomenal geometry** | L1 | Structure with a metric; $\mathrm{PG}(S) := (\mathbb{P}(\mathcal{H}_E), d_{\mathrm{FS}}, \rho_E)$, where $\mathrm{rank}(\rho_E) > 1$; corresponds to $\tau_{\leq 1}$ |
| **Cognitive qualia** | L2 | Reflexively accessible experience; $R \geq 1/3$, $\Phi \geq 1$; corresponds to $\tau_{\leq 2}$ |
| **Network consciousness** | L3 | Distributed cognitive network; $\pi_3 \neq 0$, $R^{(2)} \geq 1/4$; **metastable** with $\tau_3 = 1/(\kappa_{\mathrm{bootstrap}} \cdot (1 - R^{(2)}))$ |
| **Unitary consciousness** | L4 | Full ∞-groupoid; $\forall k: \pi_k \neq 0$, $\lim_n R^{(n)} > 0$, $P > 6/7$; maximal level (Postnikov stabilisation) |
| **Experiential content** | L0–L4 | $\mathcal{Q} := (\mathrm{Intensity}, \mathrm{Quality}, \mathrm{Context}, \mathrm{History})$ |
| **n-truncation $\tau_{\leq n}$** | — | Operation on an ∞-groupoid that zeroes out $\pi_k$ for $k > n$; connects Ln levels to homotopy structure |
| **Universal reflection threshold** | — | Formula $X^{(n)}_{\mathrm{th}} = 1/(n+1)$: L2 ($n=2$): $R_{\mathrm{th}} = 1/3$, L3 ($n=3$): $R^{(2)}_{\mathrm{th}} = 1/4$, L4 ($n=4$): $R^{(3)}_{\mathrm{th}} = 1/5$. Integration threshold: $\Phi_{\mathrm{th}} = 1$ |

## Components of Experiential Content

See [Exp category](/docs/proofs/categorical/categorical-formalism#2-категория-exp) for a formal description.

| Term | Definition |
|------|------------|
| **Intensity** | $\{\lambda_i\}$ — spectrum of $\Gamma$; defines the *strength* of the state |
| **Quality** | $\{[\lvert q_i\rangle]\} \subset \mathbb{P}(\mathcal{H}_E)$ — defines the *character* of the state |
| **Context** | $\Gamma_{-E}$ — states of all dimensions except $E$ |
| **History** | Derived as the loop space in the ∞-groupoid: $\mathrm{Hist}(\mathcal{Q}) := \Omega_\mathcal{Q}(\mathbf{Exp}_\infty)$ — [theorem](/docs/proofs/dynamics/emergent-time#5-категорное-время-через-infty-группоид) |
| **$\mathbb{P}(\mathcal{H}_E)$** | [Projective space](/docs/reference/specification#проективное-пространство-качеств) of qualities |
| **$d_{\mathrm{FS}}$** | [Fubini-Study metric](/docs/reference/specification#метрика-фубини-штуди): $d_{\mathrm{FS}}([\lvert\psi\rangle],[\lvert\phi\rangle]) = \arccos(\lvert\langle\psi\vert\phi\rangle\rvert)$ |
| **Relational identity of qualia** | [Theorem](/docs/consciousness/foundations/two-aspect-monism#реляционная-идентичность): by Yoneda's lemma, the identity of qualia $[\lvert q\rangle]$ is fully determined by its relational position in the Exp category. Inverted qualia are impossible. |
| **Phenomenal vector FV** | $\text{FV}(\rho_E) := \{(\lambda_i, [\lvert q_i\rangle])\}$ — [unique functor](/docs/consciousness/foundations/two-aspect-monism#теорема-единственность-фв), extracting experiential content from $\rho_E$. Not an arbitrary postulate, but a forced structure. |

## Calibration Terms

| Term | Definition |
|------|------------|
| **Isospectrality** | $\mathrm{Spec}(\rho_1) = \mathrm{Spec}(\rho_2)$, but $\mathrm{Eigvec}(\rho_1) \neq \mathrm{Eigvec}(\rho_2)$ |
| **Calibration** | Procedure for establishing correspondence between mathematics and phenomenology |
| **Contrast spectrum** | $\log(\lambda_i / \lambda_i^{\text{ref}})$ — relative intensities |
| **Categorical gap** | Boundary of explanation: impossibility of deducing "why there is experience" — see [Axiom Ω⁷](/docs/core/foundations/axiom-omega) |
| **Axiom Ω⁷** | [Fundamental axiomatics](/docs/core/foundations/axiom-omega): ∞-topos $\mathbf{Sh}_\infty(\mathcal{C})$ as the sole primitive |

## Categorical Terms {#категорные-термины}

See [Categorical formalism](/docs/proofs/categorical/categorical-formalism) for a full description.

| Term | Definition |
|------|------------|
| **$\mathbf{DensityMat}$** | [Category of density matrices](/docs/proofs/categorical/categorical-formalism#1-категория-densitymat) with CPTP morphisms |
| **$\mathbf{Exp}$** | [Category of experiential states](/docs/proofs/categorical/categorical-formalism#2-категория-exp) |
| **$\mathbf{Exp}_\infty$** | [∞-groupoid of paths](/docs/proofs/categorical/categorical-formalism#10-infty-группоид-и-infty-топос-для-эмерджентного-времени) — time as a 1-morphism |
| **$\mathbf{Sh}_\infty(\mathbf{Exp})$** | [∞-topos of sheaves](/docs/proofs/categorical/categorical-formalism#104-infty-топос-пучков) — internal temporal logic |
| **Functor $F$** | [Experience functor](/docs/proofs/categorical/categorical-formalism#3-функтор-f-на-объектах): $F: \mathbf{DensityMat} \to \mathbf{Exp}$ |
| **CPTP** | Completely Positive Trace-Preserving — quantum channels, see [Formalisation of φ](/docs/proofs/categorical/formalization-phi) |
| **∞-topos (∞-topos)** | ∞-category satisfying Giraud's axioms. In UHM: $\mathrm{Sh}_\infty(\mathcal{C})$ — sole primitive of the theory in the Ω⁷ formulation |
| **Grothendieck topology** | [Site](/docs/core/foundations/axiom-omega#топология-гротендика) $(\mathcal{C}, J_{Bures})$ — coverage function turning $\mathcal{C}$ into a basis for constructing the topos |
| **Bures covering** | Family $\{\Phi_i: \Gamma_i \to \Gamma\}$ covers $\Gamma$ if $B_B(\Gamma, \delta) \subseteq \bigcup_i \Phi_i(B_B(\Gamma_i, \epsilon))$ |
| **Bures metric $d_B$** | $d_B(\Gamma_1, \Gamma_2) = \arccos(\sqrt{F})$; [monotone](/docs/proofs/categorical/categorical-formalism#631-bures-топология-на-densitymat) under CPTP |
| **Fidelity (Fid)** | $\mathrm{Fid}(\rho, \sigma) = (\mathrm{Tr}\sqrt{\sqrt{\rho}\sigma\sqrt{\rho}})^2$ — measure of proximity of quantum states. The notation $\mathrm{Fid}$ is used to distinguish from functor $F$ |
| **Site (site)** | Category with a coverage function $J$ satisfying the axioms: identity, stability, transitivity |
| **∞-terminal object** | Object $T$ in an ∞-category such that $\mathrm{Map}(\Gamma, T) \simeq *$ for all $\Gamma$. Admits a multitude of equivalent paths |
| **Map(Γ, T)** | Morphism space (mapping space) in an ∞-category. Unlike $\mathrm{Hom}(\Gamma, T)$ in a 1-category, it is an ∞-groupoid |
| **Homotopy** | 2-morphism between 1-morphisms. Connects different paths between objects |
| **HoTT (Homotopy Type Theory)** | Internal logic of the ∞-topos. Formalises identity through paths |
| **Free will (Freedom)** | $\mathrm{Freedom}(\Gamma) := \dim\ker(\mathcal{H}_\Gamma) + 1$ **[T]** — number of zero modes of the free-energy functional's Hessian + 1. ∞-categorical motivation: $\pi_0(\mathrm{Map}(\Gamma, T)^{\text{non-trivial}})$. Monotone under CPTP, $G_2$-invariant. See [Consequences](/docs/core/foundations/consequences#freedom-конечномерное), [Free will](/docs/consciousness/ethics-meaning/freedom#количественная-мера) |
| **Freedom entropy** | $S_{\text{freedom}} := \log(\text{Freedom}(\Gamma)) = \log(\dim\ker(\mathcal{H}_\Gamma) + 1) \in [0, \log 7]$ — quantitative measure of the space of choice |

## L-Unification Terms

See [L-unification](/docs/core/structure/dimension-l#категориальное-определение) and [Categorical formalism](/docs/proofs/categorical/categorical-formalism) for a full description.

| Term | Definition |
|------|------------|
| **L-unification** | Central theorem of UHM: $L \cong \Omega \cap \Gamma$ — the Logic dimension is identical to the projection of the subobject classifier onto the state |
| **$\Omega$ (classifier)** | [Subobject classifier](/docs/core/foundations/axiom-omega#внутренняя-логика) of the ∞-topos $\mathrm{Sh}_\infty(\mathcal{C})$ — defines the internal logic of the theory |
| **$\chi_S$ (characteristic)** | Characteristic morphism $\chi_S: \Gamma \to \Omega$ of the subobject $S$ — "membership predicate" |
| **$L_k$ (Lindblad)** | Dissipation operators: $L_k^{\text{atom}} = \lvert k\rangle\langle k\rvert$ — projectors derived from the atoms of the classifier Ω. Historical notation $L_k = \sqrt{\chi_{S_k}}$ — convention ($\sqrt{P} = P$ for projectors). See [Lindblad operators](/docs/core/operators/lindblad-operators) |
| **$\mathcal{L}_\Omega$ (Liouvillian)** | [Logical Liouvillian](/docs/core/dynamics/evolution#логический-лиувиллиан) — evolution superoperator derived from Ω |
| **$\triangleright$ (temporal modality)** | [Modal operator](/docs/proofs/dynamics/emergent-time#время-из-модальности) "will be true tomorrow" on Ω; generates discrete time $\tau_n = \triangleright^n(\mathrm{now})$ |
| **$\mathcal{D}_\Omega \dashv \mathcal{R}$ (adjunction)** | [Dissipation–regeneration adjunction](/docs/core/foundations/axiom-septicity#категориальный-вывод-kappa0): $\mathcal{D}_\Omega$ — dissipative functor, $\mathcal{R}$ — regenerative functor; $\kappa_0$ is derived from it |
| **CPTP automatically** | Consequence of L-unification: $\sum_k L_k^\dagger L_k = \sum_k \chi_{S_k} = \mathbb{1}$ — the CPTP condition is derived from the classifier's structure |

## Formalisation Terms

| Term | Definition |
|------|------------|
| **$R$ (reflection)** | $R = R_{\text{canonical}} := 1/(7P)$ — canonical definition used in all thresholds. Not to be confused with $Q_\varphi := 1 - \|\Gamma - \varphi(\Gamma)\|_F^2 / P$ (quality measure of self-modelling). Details: [formalisation of φ](/docs/proofs/categorical/formalization-phi#28-рефлексия-n-го-порядка-для-l3l4) |
| **$R_{\text{th}}$** | Reflection threshold $= 1/3$ **[T]** ($K = 3$ from [triadic decomposition](/docs/core/operators/lindblad-operators#триадная-декомпозиция) + [Bayesian dominance](/docs/core/foundations/axiom-septicity#теорема-порог-рефлексии)) |
| **$\Phi_{\text{th}}$** | Integration threshold $= 1$ **[T]** ([T-129](/docs/proofs/consciousness/operationalization#t-129)) — unique self-consistent value at $P_{\text{crit}} = 2/7$; [coherent dominance](/docs/core/structure/dimension-u#мера-интеграции-φ) |
| **$D_{\min}$** | Minimum differentiation $= 2$ **[T]** ([T-151](/docs/proofs/consciousness/substrate-closure#t-151)) — unconditional consequence of $\Phi_{\text{th}} = 1$ [T]; [definition](/docs/core/structure/dimension-e#differentiation-threshold-dmin-2) |
| **$C_{\text{th}}$** | Consciousness threshold $= \Phi_{\text{th}} \times R_{\text{th}} = 1 \times 1/3 = 1/3$ **[T]** (T-140); $D_{\text{diff}} \geq D_{\min} = 2$ — separate viability condition [T] (T-151) |
| **$\varphi$ (operator)** | [Self-modelling operator](/docs/proofs/categorical/formalization-phi); $\varphi(\Gamma) = \sum_m K_m \Gamma K_m^\dagger$ |
| **$K_m$** | Kraus operators; $\sum_m K_m^\dagger K_m = I$ |
| **Fixed point** | $\Gamma^* = \varphi(\Gamma^*)$ — state of ideal self-knowledge |
| **Convergence** | $\|\varphi^n(\Gamma_0) - \Gamma^*\|_F \leq k^n \cdot \|\Gamma_0 - \Gamma^*\|_F$, $k \in [0,1)$ |
| **(M,R)-system** | Rosen's system: Metabolism, Repair, $\beta$-closure |
| **[Minimality theorem](/docs/proofs/minimality/theorem-minimality-7)** | From (AP)+(PH)+(QG) it follows that $\dim(\mathcal{H}) = 7$ minimally |
| **[Uniqueness theorem](/docs/proofs/minimality/theorem-minimality-7#часть-vii-теорема-о-единственности-базиса)** | Basis $\{A,S,D,L,E,O,U\}$ is unique **[T]**: A,S,D,L,U — algebraically; E,O — via κ₀ and functional independence |
| **(AP)** | Autopoiesis: $\exists\varphi$ with a fixed point |
| **(PH)** | Phenomenology: $\exists\rho_E$ with non-trivial interiority |
| **(QG)** | Quantum ground: Lindblad equation with regeneration |
| **(V) Viability** | Fourth condition in the definition of the Holon: $P(\Gamma) > P_{\text{crit}} = 2/7$. Together with (AP), (PH), (QG) forms the complete definition — see [Viability](/docs/core/dynamics/viability) |
| **IDP (Information Distinguishability Principle)** | Definition **[D]** (T16): distinguishability via $J_{\text{Bures}}$-coverings is identical to ontological distinguishability — built into A1+A2. Every Holon contains a substructure modelling its own whole. Formally: $\exists\varphi: \Gamma \to \Gamma$, $\varphi$ — CPTP channel with $F(\Gamma, \varphi(\Gamma)) > 0$ |
| **$P_{\text{crit}}$ (critical purity)** | Viability threshold $P_{\text{crit}} = 2/N = 2/7$. Derived from five independent paths — see [Theorem P_crit](/docs/proofs/dynamics/theorem-purity-critical) |
| **$\mathrm{Coh}_E$ (E-coherence)** | HS-projection **[T]**: $\mathrm{Coh}_E(\Gamma) = \|\pi_E(\Gamma)\|_{\mathrm{HS}}^2 / \|\Gamma\|_{\mathrm{HS}}^2 = (\gamma_{EE}^2 + 2\sum_{i \neq E}\lvert\gamma_{Ei}\rvert^2) / \mathrm{Tr}(\Gamma^2)$, $\in [1/7, 1]$ — [master definition](/docs/core/foundations/axiom-septicity#e-coherence-definition), [HS-projection](/docs/core/foundations/axiom-septicity#hs-projection). Formal equivalence $\mathrm{Coh}_E \approx P_E = \mathrm{Tr}(\rho_E^2)$ — **structural hypothesis [H]** |
| **$\kappa_0$ (base regeneration coefficient)** | Coupling scale of the Holon to the environment in the regenerative term $\mathcal{R}[\Gamma, E]$ — see [categorical derivation of κ₀](/docs/core/foundations/axiom-septicity#категориальный-вывод-kappa0) |
| **$D_{\text{diff}}$ (differentiation dimension)** | Number of dimensions in which $\Gamma$ deviates from the maximally mixed state. L2 threshold: $D_{\text{diff}} \geq 2$ — see [definition](/docs/core/structure/dimension-e#differentiation-threshold-dmin-2) |
| **$\mathcal{R}_\alpha$ (regenerative operator)** | CPTP operator: $\mathcal{R}_\alpha(\rho) = (1-\alpha)\rho + \alpha\rho_*$ [T] — unique CPTP interpolation with a replacement channel; see [derivation of the ℛ form](/docs/core/dynamics/evolution#вывод-формы-регенерации) |
| **Correctness condition** | $\alpha = \kappa \cdot \Delta\tau < 1$ — positivity guarantee in numerical integration |
| **Interpolation formulation** | Consequence [T] of CPTP-uniqueness of the replacement channel: regeneration as a convex combination of $\mathrm{Id}$ and $\mathcal{C}_{\rho_*}$; proves preservation of $\Gamma \geq 0$ |
| **$R^{(n)}$ (n-th order reflection)** | $R^{(n)}(\Gamma) := F(\varphi^{(n-1)}(\Gamma), \varphi^{(n)}(\Gamma))$ — consistency measure between successive levels of self-modelling |
| **Spectral formula $\varphi$** | $\varphi(\Gamma) = \sum_{k: \mathrm{Re}(\lambda_k)=0} \langle L_k \vert \Gamma \rangle R_k$ — projection onto the kernel of $\mathcal{L}_\Omega$; see [formalisation of φ](/docs/proofs/categorical/formalization-phi#27-спектральная-формула-для-φ-явное-вычисление) |
| **Variational characterisation of φ** | **Theorem 3.1:** $\varphi = \arg\min_{\psi \in \mathcal{CPTP}} [S_{vN}(\psi(\Gamma)) + D_{KL}(\psi(\Gamma) \| \Gamma)]$; see [proof](/docs/proofs/dynamics/fep-derivation#3-теорема-о-вариационной-характеризации) |
| **$S_{spec}$ (spectral entropy)** | For density matrices $S_{spec} = S_{vN}$ ([Theorem 5.1](/docs/proofs/dynamics/fep-derivation#5-s_spec-vs-s_vn-обоснование-выбора)). General: $S_{spec}(A) = -\sum_i \lvert\lambda_i\rvert \log\lvert\lambda_i\rvert$ |
| **Canonical $\Delta F$** | $\Delta F(\Gamma) := d_B^2(\Gamma, \Gamma_{\mathrm{eq}}) - d_B^2(\Gamma, \varphi(\Gamma))$ — unified definition via the Bures metric |
| **L3 metastability** | Lifetime of network consciousness: $\tau_3 = 1/(\kappa_{\mathrm{bootstrap}} \cdot (1 - R^{(2)}))$; finite without active maintenance |
| **$H_{\mathrm{eff}}$ (effective Hamiltonian)** | Hamiltonian of the system after integrating over time: $H_{\mathrm{eff}}(\tau) = H_{6D} + \langle\tau\lvert H_{\mathrm{int}}\rvert\tau\rangle_O$; see [Page–Wootters](/docs/core/dynamics/evolution#вывод-h_eff) |
| **Lindblad equation** | $\frac{d\Gamma}{d\tau} = -i[H_{\mathrm{eff}}, \Gamma] + \mathcal{D}[\Gamma] + \mathcal{R}[\Gamma, E]$; three terms: unitary, dissipative, regenerative |
| **Bootstrap paradox** | Problem: regeneration requires coherence ($\kappa \propto \mathrm{Coh}_E$), but a low-coherence system cannot regenerate. Solution: $\kappa_{\mathrm{bootstrap}} > 0$ provides minimal regeneration; see [Genesis Protocol](/docs/core/foundations/axiom-omega#genesis-protocol) |
| **$\kappa_{\mathrm{bootstrap}}$** | Minimum regeneration rate: $\kappa_{\mathrm{bootstrap}} := \|\eta\| > 0$, where $\eta$ — unit of the adjunction $\mathcal{D}_\Omega \dashv \mathcal{R}$; resolves the bootstrap paradox |

## Taxonomy of Γ Configurations {#таксономия-конфигураций-γ}

| Term | Definition |
|------|------------|
| **Fundamental mode Γ** | Γ subsystem with $R = 0$; dynamics degenerate into Schrödinger/Dirac. Passive stability (symmetries). Examples: quarks, leptons, bosons. **Not a Holon** — does not satisfy (AP)+(QG) |
| **Composite configuration Γ** | Quasi-autonomous configuration with $0 < R \ll 1$; near-unitary dynamics. Passive stability (bonds). Examples: atoms, simple molecules. **Not a Holon** — does not satisfy (AP)+(QG) |
| **Holon** | Self-sufficient unit, (AP)+(PH)+(QG)+(V), where (V): $P > P_{\text{crit}} = 2/7$. Examples: cells, organisms |
| **L2-Holon** | Holon with cognitive qualia: $R \geq R_{\text{th}}$, $\Phi \geq \Phi_{\text{th}}$. Which systems reach L2 is an empirical question |
| **Passive stability** | Stability through symmetries (conservation laws). Characteristic of fundamental modes and composite Γ configurations |
| **Active stability** | Stability through autopoiesis (metabolism + repair). Characteristic of Holons |

## Related Theories {#связанные-теории}

| Term | Definition |
|------|------------|
| **Integrated Information Theory (IIT)** | Tononi's theory. UHM generalises: $C = \Phi_{\text{UHM}} \times R$ **[T T-140]**; $D_{\text{diff}} \geq D_{\min}$ — separate viability condition. **Important:** $\Phi_{\text{UHM}} \neq \Phi_{\text{IIT}}$ — see [notation](/docs/reference/notation) |
| **Free Energy Principle (FEP)** | Friston's theory. In UHM: **special case** (classical limit) of the variational characterisation of φ — [Theorem 4.2](/docs/proofs/dynamics/fep-derivation#4-классический-предел-вывод-fep). Full formulation: $\varphi = \arg\min[S_{vN} + D_{KL}]$ |
| **Global Workspace Theory (GWT)** | Baars's theory — global access to information |
| **Conscious realism** | Hoffman's theory; connection to UHM: agent $\approx$ L2-Holon (hypothesis) |
| **Panpsychism** | "Everything has consciousness." UHM: **paninteriorism** — everything has L0, not L2 |

## Status of Claims

### Rigour-level markers

| Marker | Alternative | Meaning | Description |
|--------|-------------|---------|-------------|
| **[T] STRICT** | Theorem | Mathematically proved | Follows from axioms without additional assumptions |
| **[C] CONDITIONAL** | Conditional | Proved under assumptions | Requires explicitly stated interpretational or physical assumptions |
| **[H] PROGRAMME** | Hypothesis | Mathematically formulated | Requires proof |

:::note Full marker system
The full system includes 7 markers: [T] Theorem, [C] Conditional, [H] Hypothesis, [P] Postulate, [D] Definition, [I] Interpretation, [✗] Retracted. See [Status registry](/docs/reference/status-registry).
:::

### Classical statuses

| Term | Definition |
|------|------------|
| **Formalised** | Strictly defined and/or proved mathematically (equivalent to [T]) |
| **Empirical** | Value requires experimental calibration |
| **Heuristic** | Conceptual direction, not a strict derivation (equivalent to [C]) |
| **Programme** | Research direction requiring development (equivalent to [H]/[P]) |
| **Hypothesis** | Statement requiring proof (equivalent to [H]) |

## Terms Related to Gödel's Theorems

| Term | Definition |
|------|------------|
| **Gödelian completeness** | Property of a system in which every truth is provable; unattainable for sufficiently expressive systems |
| **Minimal completeness** | Property of UHM: 7 dimensions are sufficient for (AP)+(PH)+(QG); distinct from Gödelian completeness |
| **$\mathrm{Prov}(L)$** | Set of logically provable statements in dimension $L$ |
| **$\mathrm{Coh}(\Gamma)$** | Coherence-truth — consistency with the structure of $\Gamma$; $\mathrm{Prov}(L) \subsetneq \mathrm{Coh}(\Gamma)$ |
| **Enacted consistency** | Consistency demonstrated through existence (autopoiesis) |
| **Topological surgery** | Overcoming Gödelian limitations through extension from dimension $O$ |

## Coherence Cybernetics Terms

See [Coherence Cybernetics](/docs/applied/coherence-cybernetics/definitions) for a full description.

| Term | Definition |
|------|------------|
| **CC** | Coherence Cybernetics — meta-theory of systems described by $\Gamma \in D(\mathbb{C}^7)$ |
| **$\mathcal{V}$** | [Viability domain](/docs/core/dynamics/viability): $\mathcal{V} = \{\Gamma : P(\Gamma) > P_{\text{crit}}\}$ |
| **$\mathrm{VIT}$** | Viability Integrity Tensor — viability integrity tensor |
| **$\sigma_{\mathrm{sys}}$** | System stress tensor $\in \mathbb{R}^7$ |
| **$\kappa$** | Regeneration rate; $\kappa(\Gamma) = \kappa_{\text{bootstrap}} + \kappa_0 \cdot \mathrm{Coh}_E(\Gamma)$ — [master definition](/docs/core/foundations/axiom-septicity#структурный-анзац-kappa0) |
| **$\kappa_0$** | Base regeneration rate: $\kappa_0 = \|\mathrm{Nat}(\mathcal{D}_\Omega, \mathcal{R})\|$ — [categorical derivation](/docs/core/foundations/axiom-septicity#категориальный-вывод-kappa0) from the adjunction $\mathcal{D}_\Omega \dashv \mathcal{R}$ |
| **$\mathrm{Coh}_E$** | $E$-coherence (HS-projection) **[T]**: $\mathrm{Coh}_E(\Gamma) = \|\pi_E(\Gamma)\|_{\mathrm{HS}}^2 / \|\Gamma\|_{\mathrm{HS}}^2$ — [master definition](/docs/core/foundations/axiom-septicity#e-coherence-definition), [HS-projection](/docs/core/foundations/axiom-septicity#hs-projection), [CC reference](/docs/applied/coherence-cybernetics/definitions#e-когерентность) |
| **$\rho_*$ ($\Gamma_{\text{target}}$)** | Unique stationary state of $\mathcal{L}_\Omega$ [T]: $\rho_* = \varphi(\Gamma)$ — regeneration target, uniquely determined by [primitivity](/docs/core/operators/lindblad-operators#примитивность-ℒω) |
| **$\omega_0$** | Fundamental clock frequency — parameter of the computational approximation of κ₀; see [categorical derivation of κ₀](/docs/core/foundations/axiom-septicity#категориальный-вывод-kappa0) |
| **No-Zombie** | [Theorem [T]](/docs/applied/coherence-cybernetics/theorems#теорема-81-условная-необходимость-интериорности-no-zombie): $\mathrm{Viable} \land \mathcal{D}_\Omega \neq 0 \Rightarrow \mathrm{Coh}_E > 1/7$ — impossibility of viable zombies |
| **$\mathbf{Hol}$** | Category of Holons with CPTP morphisms |
| **$P_{\text{crit}}$** | Critical purity $= 2/7 \approx 0.286$ — [theorem](/docs/proofs/dynamics/theorem-purity-critical) (derived by 5 methods from UHM axioms) |

## Octonionic Terms

See [Structural derivation via octonions](/docs/proofs/minimality/theorem-octonionic-derivation) for a full description.

| Term | Definition |
|------|------------|
| **Octonions ($\mathbb{O}$)** | 8-dimensional normed division algebra over $\mathbb{R}$; non-associative, alternative |
| **$\mathrm{Im}(\mathbb{O})$** | Imaginary part of the octonions; $\dim = 7$; space of internal degrees of freedom of the Holon [I] |
| **Hurwitz's theorem [T]** | Normed division algebras over $\mathbb{R}$ exist only in dimensions 1, 2, 4, 8 ($\mathbb{R}, \mathbb{C}, \mathbb{H}, \mathbb{O}$) |
| **Adams's theorem [T]** | Parallelisable spheres: only $S^0, S^1, S^3, S^7$; equivalent to $\dim(\mathrm{Im}) \in \{0, 1, 3, 7\}$ |
| **Cayley–Dickson construction [T]** | Recursive doubling: $\mathbb{R} \to \mathbb{C} \to \mathbb{H} \to \mathbb{O} \to \mathbb{S}$; each step loses a property |
| **Cayley–Dickson boundary [C]** | $\mathbb{O}$ — last division algebra; the next step (sedenions $\mathbb{S}$) loses divisibility |
| **Fano plane PG(2,2) [T]** | Minimal projective plane: 7 points, 7 lines, 3 points on each line; defines the multiplication table of the octonions |
| **$G_2$ [T]** | $\mathrm{Aut}(\mathbb{O}) = G_2$ — 14-parameter exceptional Lie group; $G_2 \subset SO(7)$ |
| **Hamming code $H(7,4)$ [T]** | Perfect code: 4 information + 3 check bits; isomorphic to the lines of the Fano plane |
| **Associator [T]** | $[x, y, z] = (xy)z - x(yz)$; measure of deviation from associativity; $= 0$ in $\mathbb{R}, \mathbb{C}, \mathbb{H}$; $\neq 0$ in $\mathbb{O}$ |
| **Alternativity [T]** | Property of $\mathbb{O}$: $[x, x, y] = [x, y, y] = 0$; any two elements generate an associative subalgebra (Artin's theorem) |
| **Artin's theorem [T]** | In an alternative algebra, any two elements generate an associative subalgebra |
| **Moufang identities [T]** | $(xyx)z = x(y(xz))$ and analogues; generalised associativity for octonions |
| **Theorem P1 [T]** | Space of internal degrees of freedom is isomorphic to $\mathrm{Im}(\mathbb{A})$ for a division algebra $\mathbb{A}$ (derived from axioms along the T15 chain) |
| **Theorem P2 [T]** | Non-associativity: $\exists x, y, z : [x, y, z] \neq 0$; excludes $\mathbb{R}, \mathbb{C}, \mathbb{H}$ (derived from axioms along the T15 chain) |
| **Track A** | Justification of N=7 via (AP)+(PH)+(QG) → minimality ([Theorem S](/docs/proofs/minimality/theorem-minimality-7)) |
| **Track B** | Justification of N=7 via P1+P2 → $\mathbb{O}$ → $\dim(\mathrm{Im}(\mathbb{O})) = 7$ ([Structural derivation](/docs/proofs/minimality/theorem-octonionic-derivation)) |

:::tip Bridge [T] — fully closed (T15)
Connection (AP)+(PH)+(QG)+(V) → P1+P2 — full chain of 12 steps (T1–T16), **all [T]** (T16/IDP reclassified [D] — definition built into A1+A2; computational results unaffected). Former condition (МП) proved by T11–T13. See [bridge](/docs/proofs/minimality/theorem-octonionic-derivation#мост).
:::

## Gap-Dynamics and Fano-Structure Terms

See [Gap operator](/docs/core/dynamics/gap-operator) and [φ-operator](/docs/core/operators/phi-operator) for a full description.

| Term | Definition |
|------|------------|
| **Gap landscape** | Mapping $G: D(\mathbb{C}^7) \to [0,1]^{21}$, map of all 21 Gap values — [phase diagram](/docs/core/dynamics/gap-phase-diagram) |
| **Gap operator ($\hat{G}$)** | Anti-Hermitian operator $\hat{G} = \mathrm{Im}(\Gamma) \in so(7)$, describing the mismatch between the outer and inner aspects. Spectrum: $\{\pm i\lambda_1, \pm i\lambda_2, \pm i\lambda_3, 0\}$. Opacity rank = number of non-zero pairs (0–3) — [definition](/docs/core/dynamics/gap-operator) |
| **O-parity** | Approximately conserved charge $(-1)^{\Delta N_O}$, stabilising dark-matter candidates — [dark matter](/docs/physics/cosmology-phys/dark-matter) |
| **Swallowtail** | Whitney catastrophe with 4 sheets, connecting Gap bifurcations to interiority levels L0–L4 — [phase diagram](/docs/core/dynamics/gap-phase-diagram) |
| **$\varphi_{\mathrm{coh}}$** | Coherence-preserving self-modelling operator, canonical construction via Fano structure: $\varphi_{\mathrm{coh}} = k[\alpha^* P_{\mathrm{base}} + (1-\alpha^*) P_{\mathrm{Fano}}] + (1-k)\Gamma_{\mathrm{anchor}}$ — [φ-operator](/docs/core/operators/phi-operator) |
| **Transparency map** | $7 \times 7$ heat map visualising $\mathrm{Gap}(i,j)$ for a specific Holon — [Gap diagnostics](/docs/applied/research/gap-diagnostics) |
| **Opacity rank** | Number of non-zero pairs $(\pm i\lambda_k)$ in the spectrum of Gap operator $\hat{G}$. Takes values 0, 1, 2, 3 — [Gap operator](/docs/core/dynamics/gap-operator) |

## Spectral Geometry and SM Terms

| Term | Definition |
|------|------------|
| **Bimodule $H_F$** | Finite Hilbert space of the UHM spectral triple as an $(A_{\text{int}}, A_{\text{int}}^\circ)$-bimodule via the real structure $J$ (KO-dim 6). Decomposition into irreducible bimodules exactly matches one generation of SM fermions. T-178 [T] (bimodular realisation), T-179 [T] (hypercharge fixation), T-180 [T] (mass relations), T-181 [T] (derivation of (AP),(PH),(QG),(V) from A1–A4) — [bimodular construction](/docs/proofs/physics/bimodule-construction) |
| **KO-dimension** | Classification invariant of the real structure $J$ on a spectral triple. In UHM: KO-dim $= 6$ (mod 8) — condition ensuring chirality and the SM generation structure. From Connes's conditions: $J^2 = 1$, $JD = DJ$, $J\gamma = -\gamma J$ — [bimodular construction](/docs/proofs/physics/bimodule-construction) |
| **T-181 (characterising properties)** | (AP), (PH), (QG), (V) — theorems from A1–A4. (QG) from A1 (∞-topos), (AP) from A1 (terminal object + adjunction), (PH) from A1+A3, (V) from A2+A3. Consequence: number of independent UHM axioms = 4 — [bimodular construction](/docs/proofs/physics/bimodule-construction#вывод-apphqgv) |
| **$\mathrm{SAD}_{\max}$** | Maximum recursive self-modelling depth: $\mathrm{SAD}_{\max} = 3$ **[C]** (from Fano contraction $\alpha = 2/3$, $P_{\text{crit}}^{(n)} = P_{\text{crit}} \cdot 3^{n-1}/(n+1)$). Pred 12 — [depth tower](/docs/consciousness/hierarchy/depth-tower#критическая-чистота-sad) |
| **Fano channel ($P_{\mathrm{Fano}}$)** | CPTP map $P_{\mathrm{Fano}}(\Gamma) = \frac{1}{3}\sum_p \Pi_p \Gamma \Pi_p$, preserving coherences. $G_2$-covariant — [Fano channel](/docs/proofs/gap/fano-channel) |
| **ISF (Infra-Slow Fluctuations)** | Infra-Slow Fluctuations — quasi-Goldstone modes of $G_2$-symmetry breaking, manifesting in EEG/MEG at frequencies $0.005$–$0.02$ Hz. Number of independent ISF components $N_{\text{ISF}} \in [6, 12]$ determined by the opacity rank of the [Gap operator](/docs/core/dynamics/gap-operator) — [Goldstone modes](/docs/applied/coherence-cybernetics/goldstone-modes#isf-prediction), [F-ISF](/docs/reference/falsifiability#f-isf-isf-компоненты-в-фмрт) |

## Physical Correspondence Terms

See [Physics overview](/docs/physics/overview) for a full description of the physical consequences of the theory.

| Term | Definition |
|------|------------|
| **RG flow (renormalisation group flow)** | Dependence of coupling constants and Gap parameters on the energy scale $\mu$. $\beta$-functions $\beta_i = \mu \partial g_i / \partial\mu$ define fixed points (Gaussian, Wilson-Fisher, octonionic) and phase transitions of the potential $V_{\mathrm{Gap}}$ — [RG flow](/docs/physics/gauge-symmetry/rg-flow), [F-Cabibbo](/docs/reference/falsifiability#f-cabibbo-угол-кабиббо-из-rg-подавления-фано-угла) |
| **Pendleton–Ross fixed point** | Infrared quasi-fixed point of the RG evolution of the top-quark Yukawa coupling: $y_t^* = \sqrt{8\pi^2 c_2 / (9 \cdot 7)}$, where $c_2$ is the quadratic Casimir operator. The unique $O(1)$ Yukawa coupling (Fano-Higgs line $\{A, E, U\}$) is attracted to this point, fixing $m_t \approx 173$ GeV — [Yukawa hierarchy](/docs/physics/particle-physics/yukawa-hierarchy#3-quasi-ir-fixed-point-и-масса-t-кварка), [F-m_t](/docs/reference/falsifiability#f-m_t-масса-top-кварка-из-неподвижной-точки-пендлтона-росса) |
| **Fritzsch texture** | Specific zero pattern in quark mass matrices arising from Fano geometry: $M_{\mathrm{Fritzsch}} = \begin{pmatrix} 0 & A & 0 \\ A^* & 0 & B \\ 0 & B^* & C \end{pmatrix}$. Zeros on the diagonal for light generations are derived from the [Fano selection rule](/docs/physics/gauge-symmetry/fano-selection-rules); defines CKM angles through mass ratios ($\|V_{us}\| \sim \sqrt{m_d/m_s}$) — [Theorem 5.2](/docs/physics/particle-physics/yukawa-hierarchy#thm-5-2), [CKM matrix](/docs/physics/particle-physics/ckm-matrix#6-ckm-из-несовпадения-юкавских-текстур), [F-δ_CP](/docs/reference/falsifiability#f-δ_cp-cp-фаза-ckm-из-фано-фазы) |

## Abbreviations

| Abbreviation | Expansion | Translation / Note |
|--------------|-----------|-------------------|
| **SAD** | Self-Awareness Depth | Self-awareness depth — number of levels of recursive reflection |
| **HS** | Hilbert-Schmidt | Hilbert-Schmidt norm/projection: $\|A\|_{\mathrm{HS}} = \sqrt{\mathrm{Tr}(A^\dagger A)}$ |
| **BIBD** | Balanced Incomplete Block Design | Balanced incomplete block design; BIBD$(7,3,1)$ = Fano plane |
| **SUSY** | Supersymmetry | Supersymmetry; $\mathcal{N}=1$ SUSY used in UV-finiteness (T-66) |
| **SM** | Standard Model | Standard Model of particle physics |
| **GUT** | Grand Unified Theory | Grand Unified Theory |
| **EW** | Electroweak | Electroweak interaction; EW sector in UHM: [T]/[C] split |

## Applied Terms

| Term | Definition |
|------|------------|
| **Quasi-functor** | Approximate functor $G: \mathbf{AIState} \to \mathbf{DensityMat}$ with bounded error $\|G(f \circ g) - G(f) \circ G(g)\|_F \leq \varepsilon_{\text{functor}}$; used in the [measurement protocol](/docs/applied/research/measurement-protocol) |
| **$\Phi_{\text{eff}}$** | Effective integration measure for AI systems: $\Phi_{\text{eff}} = \lambda_2(L_{\text{attn}}) / \lambda_{\max}(L_{\text{attn}})$, where $L_{\text{attn}}$ is the Laplacian of the attention graph; polynomial approximation to the theoretical $\Phi$ |
| **Coherence flow ($J_P$)** | $J_P = dP/d\tau$ — rate of change of purity; diagnostic quantity in the [measurement protocol](/docs/applied/research/measurement-protocol) |
| **$P_{\text{norm}}$** | Normalised purity: $P_{\text{norm}} = (P - P_{\text{crit}}) / (1 - P_{\text{crit}})$; maps $[P_{\text{crit}}, 1] \to [0, 1]$ |

## Bibliography

### Philosophy of consciousness

| Author | Work | Relevance for UHM |
|--------|------|-------------------|
| **Chalmers D.** | *The Conscious Mind* (1996); *Panpsychism and Panprotopsychism* (2015) | Hard problem of consciousness; L0 as paninteriorism |
| **Nagel T.** | *What Is It Like to Be a Bat?* (1974) | Qualia and subjective experience; motivation for $\mathcal{H}_E$ |
| **Hoffman D.** | *The Case Against Reality* (2019); *Conscious Realism* | L2-Holon ≈ conscious agent (hypothesis) |

### Theories of consciousness

| Author | Work | Relevance for UHM |
|--------|------|-------------------|
| **Tononi G.** | *Integrated Information Theory* (IIT 3.0, 2014) | Integration measure Φ; UHM generalises via $C = \Phi \times R$ **[T T-140]**; $D_{\text{diff}}$ — separate condition |
| **Friston K.** | *Free Energy Principle* (2010); *Active Inference* (2016) | Free energy minimisation; connection to regeneration $\mathcal{R}$ |
| **Baars B.** | *Global Workspace Theory* (1988) | Global access to information |

### Autopoiesis and cybernetics

| Author | Work | Relevance for UHM |
|--------|------|-------------------|
| **Maturana H., Varela F.** | *Autopoiesis and Cognition* (1980) | Autopoiesis (AP); self-generation of boundaries |
| **Rosen R.** | *Life Itself* (1991) | (M,R)-systems; $\beta$-closure |

### Quantum mechanics and time

| Author | Work | Relevance for UHM |
|--------|------|-------------------|
| **Page D., Wootters W.** | *Evolution without evolution* (1983) | Page–Wootters mechanism; emergent time τ |
| **Lindblad G.** | *On generators of quantum dynamical semigroups* (1976) | Lindblad operators $L_k$; dissipation $\mathcal{D}[\Gamma]$ |

### Mathematics

| Author | Work | Relevance for UHM |
|--------|------|-------------------|
| **Hurwitz A.** | *Über die Composition der quadratischen Formen* (1898) | Hurwitz's theorem: division algebras only in dim 1, 2, 4, 8 |
| **Adams J.F.** | *On the Non-Existence of Elements of Hopf Invariant One* (1960) | Adams's theorem: parallelisable spheres only $S^0, S^1, S^3, S^7$ |
| **Baez J.** | *The Octonions* (2002) | Survey of octonions; $G_2$, Fano plane |
| **Bures D.** | *An extension of Kakutani's theorem* (1969) | Bures metric $d_B$; topology $J_{Bures}$ |
| **Fubini G., Study E.** | *Geometria proiettiva differenziale* (1906) | Fubini-Study metric $d_{\text{FS}}$; phenomenal space L1 |
| **Grothendieck A.** | *SGA 4* (1963-1969) | Grothendieck topology; sites and toposes |
| **Connes A.** | *Noncommutative Geometry* (1994) | Spectral triples; stratified metric |
| **Lurie J.** | *Higher Topos Theory* (2009) | ∞-toposes; $\mathbf{Sh}_\infty(\mathcal{C})$ |
| **Mac Lane S.** | *Categories for the Working Mathematician* (1971) | Functor coherence; lax 2-functor |

### Topology and geometry

| Author | Work | Relevance for UHM |
|--------|------|-------------------|
| **Perelman G.** | *Ricci flow with surgery* (2002-2003) | Proof of the Poincaré conjecture; analogy with regeneration |
| **Goresky M., MacPherson R.** | *Intersection Homology* (1980) | IC cohomology; stratification of X |

---

**Related documents:**
- [Notation](./notation) — mathematical notation
- [Falsifiability](./falsifiability) — theory verification criteria
- [Axiom Ω⁷](/docs/core/foundations/axiom-omega) — fundamental axiomatics with the ∞-topos as the sole primitive
- [Consequences](/docs/core/foundations/consequences) — cohomological monism, local–global dichotomy
- [Theorem on emergent time](/docs/proofs/dynamics/emergent-time) — derivation of time, including stratificational
- [Holon](/docs/core/structure/holon) — definition of $\mathbb{H}$
- [Seven dimensions](/docs/core/structure/dimensions) — basis $\mathcal{H}$
- [Dimension O](/docs/core/structure/dimension-o) — internal clock
- [Coherence matrix](/docs/core/dynamics/coherence-matrix) — definition of $\Gamma$
- [Evolution](/docs/core/dynamics/evolution) — terminal object T and the arrow of time
- [Spacetime](/docs/core/foundations/spacetime) — base space X, metric d_strat
- [Interiority hierarchy](/docs/proofs/consciousness/interiority-hierarchy) — levels L0→L1→L2→L3→L4 and n-truncations of the ∞-groupoid
- [Categorical formalism](/docs/proofs/categorical/categorical-formalism) — functor $F$, ∞-groupoid, ∞-topos, derived categories
- [Formalisation of operator φ](/docs/proofs/categorical/formalization-phi) — CPTP channels
- [Viability](/docs/core/dynamics/viability) — measure $P$ and $P_{\text{crit}}$
- [Structural derivation via octonions](/docs/proofs/minimality/theorem-octonionic-derivation) — P1+P2 → 𝕆 → N=7
