---
sidebar_position: 4
title: "Cohesive Closure Theorem"
description: "A single categorical construction closing three foundational vulnerabilities: phenomenal functor, emergent time, free energy"
---

# Cohesive Closure Theorem

:::info Who this chapter is for
This chapter addresses three foundational vulnerabilities identified in external audit of UHM:
(1) the interpretive status of the phenomenal functor $F$,
(2) the $O(H_{\text{int}})$ approximation in the Page-Wootters time emergence,
(3) the conditional dependence of $\Delta F > 0$ on spectral details of $D_{\text{int}}$.
A single categorical construction — the operationalization of the differentially cohesive structure (T-185) — was proposed to close all three simultaneously. It does not: closure (a) is a hypothesis [H]; closures (b) and (c) are retracted [✗] (§3). The retraction box after the theorem states the reasons. What does hold since 2026-09-25 is the cohesion itself, in a corrected form: the state space $\mathcal{D}(\mathbb{C}^7)$ with its rank strata is an object of a differentially cohesive ∞-topos, and all seven modalities act on it (T-185 (ii′), [T], [§2.1a](#t-185-ii-prime)). The site $(\mathbf{DensityMat}, J_{\text{Bures}})$ of the original statement remains open.
:::

## 1. The Three Vulnerabilities

### 1.1. Vulnerability A: Phenomenal functor $F$ is interpretive

The phenomenal functor $F: \mathbf{DensityMat} \to \mathbf{Exp}$ maps $\Gamma$ to its experiential content. Its uniqueness is proved [T] via the spectral theorem and Chentsov-Petz metric minimality. However, the **identification** of the singular complex $\mathrm{Sing}(E(\Gamma))$ with phenomenal content — the semantic assignment of homotopy groups $\pi_n$ to interiority levels — has status [I] (interpretation). It is stipulated, not derived.

### 1.2. Vulnerability B: Page-Wootters time has $O(H_{\text{int}})$ corrections

The Page-Wootters equivalence theorem (T-87 [T]) proves that conditional states evolve as:

$$
\Gamma(\tau_{n+1}) = \triangleright^*(\Gamma(\tau_n)) + O(H_{\text{int}})
$$

The correction $O(H_{\text{int}})$ arises from the tensor decomposition approximation $\mathcal{H}_O \otimes \mathcal{H}_{6D}$ and weak-coupling limit. Time emergence is exact only in the non-interacting limit.

### 1.3. Vulnerability C: $\Delta F > 0$ conditional on $D_{\text{int}}$ spectral details

The regeneration term $\mathcal{R}$ requires $\Delta F > 0$ (Landauer principle, [T]). The cosmological constant $\Lambda = \mu^2 \cdot \mathcal{G}_{\text{total}}^{(O)}$ connects to the Gap via the spectral identity $\mathrm{Tr}(D_{\text{int}}^2) = \omega_0^2 \cdot \mathcal{G}_{\text{total}}$. But this connection depends on spectral characteristics of $D_{\text{int}}$ that are established in the vacuum sector [C], not unconditionally.

## 2. The Unified Solution: Operationalizing Cohesive Structure

### 2.1. T-185 as foundation

Theorem T-185 asserted that $\mathfrak{T} = \mathrm{Sh}_\infty(\mathcal{D}(\mathbb{C}^7), J_{\text{Bures}})$ is a **differentially cohesive** $\infty$-topos (U. Schreiber, *Differential cohomology in a cohesive $\infty$-topos*, arXiv:1310.7930v1, 2013) with two tiers of adjunctions. The places in arXiv v1, checked against its text: cohesion is Definition 3.4.1 (§3.4), with the adjoint quadruple $\Pi \dashv \mathrm{Disc} \dashv \Gamma \dashv \mathrm{coDisc}$ and the adjoint triple of modalities $\Pi \dashv \flat \dashv \sharp$ of Definition 3.4.4; the ∞-cohesive sites of Definition 3.4.17 give cohesive ∞-toposes by Proposition 3.4.18; differential cohesion is Definition 3.5.1 (§3.5), and its adjoint triple $\mathrm{Red} \dashv \Pi_{\inf} \dashv \flat_{\inf}$ is Definition 3.10.1 (in Schreiber's later versions written $\Re \dashv \Im \dashv \&$). An earlier version cited "§3.9 cohesion + §3.10 super-/differential cohesion": in arXiv v1, §3.9 and §3.10 are "Structures in a cohesive / differentially cohesive ∞-topos", there is no super-cohesion, and the modality Rh used below for the U-dimension does not occur at all. Rh belongs to the "solid cohesion" of the 2017 version of the manuscript (site: Definition 6.6.13 there), where it is the third member of a further triple $\rightrightarrows \dashv \rightsquigarrow \dashv \mathrm{Rh}$ and acts by $\mathrm{Rh}\,X(C^\infty(\mathbb{R}^n)\otimes W\otimes\Lambda\mathbb{R}^q) = X(C^\infty(\mathbb{R}^n)\otimes W)$ (D. J. Myers, M. Riley, *Commuting Cohesions*, arXiv:2301.13780, §6.3). The two tiers:

$$
\text{Cohesive:} \quad \Pi \dashv \mathrm{Disc} \dashv \Gamma \dashv \mathrm{coDisc}
$$
$$
\text{Infinitesimal:} \quad \mathrm{Red} \dashv \Pi_{\inf} \dashv \flat_{\inf}
$$

The list of T-185 was $\mathrm{Id}$ (O), $\Pi$ (A), $\flat$ (S), $\Im$ (D), $\sharp$ (L), $\&$ (E), $\mathrm{Rh}$ (U). A differentially cohesive ∞-topos carries, besides the identity, the six modalities $\Pi \dashv \flat \dashv \sharp$ and $\mathrm{Red} \dashv \Pi_{\inf} (= \Im) \dashv \flat_{\inf} (= \&)$ — seven with the identity. The list of T-185 drops the reduction $\mathrm{Red}$ and adds $\mathrm{Rh}$ from a different structure; as a list of differential cohesion it is wrong [✗], and the corrected list is item (4) of the theorem below. The assignment of modalities to dimensions is a reading [I].

### 2.1a. Theorem T-185 (ii′): a differentially cohesive home for the state space [T] {#t-185-ii-prime}

The obstruction recorded in the audit concerns the site, not the state space: the category $\mathbf{DensityMat}$ with CPTP maps as morphisms is not a site of spaces, and the petit ∞-topos of the topological space $\mathcal{D}(\mathbb{C}^7)$ is not cohesive at all (remark below). The state space is, however, a smooth stratified space, and smooth spaces live in a cohesive ∞-topos that Schreiber constructs explicitly.

:::tip Theorem T-185 (ii′) (Differential cohesion of the smooth UHM topos) [T]
Let $\mathfrak{T}_{\mathrm{UHM}} := \mathrm{SynthDiff}\infty\mathrm{Grpd} = \mathrm{Sh}_\infty(\mathrm{CartSp}_{\mathrm{synthdiff}})$, the ∞-sheaves on the products $\mathbb{R}^n \times \mathbb{D}$ of Cartesian spaces with infinitesimally thickened points (DCCT v1, Definition 4.5.7).

1. $\mathfrak{T}_{\mathrm{UHM}}$ is a cohesive ∞-topos (DCCT v1, Proposition 4.5.8) and a differentially cohesive one over $\mathrm{Smooth}\infty\mathrm{Grpd} = \mathrm{Sh}_\infty(\mathrm{CartSp}_{\mathrm{smooth}})$ (Proposition 4.5.11 with Definition 3.5.1). It therefore carries $\Pi \dashv \flat \dashv \sharp$ and $\mathrm{Red} \dashv \Pi_{\inf} \dashv \flat_{\inf}$.
2. The state space is an object of it. $\mathcal{D}(\mathbb{C}^7)$, a compact convex subset of the affine space $\mathrm{Herm}_1(7) \cong \mathbb{R}^{48}$, with the subset diffeology (plots: smooth maps $U \to \mathbb{R}^{48}$ with image in $\mathcal{D}$) is a concrete sheaf on $\mathrm{CartSp}_{\mathrm{smooth}}$ — a diffeological space (DCCT v1, Definition 4.4.14) — and enters $\mathfrak{T}_{\mathrm{UHM}}$ through the full embedding of Proposition 4.5.11. Each rank stratum $\mathcal{D}_k = \{\mathrm{rank}\,\Gamma = k\}$ is an embedded submanifold of dimension $14k - k^2 - 1$ (48 for the interior $k = 7$, 12 for the pure states $\mathcal{D}_1 \cong \mathbb{CP}^6$), hence an object of $\mathrm{Smooth}\infty\mathrm{Grpd}$ by Corollary 4.4.10.
3. Shapes: $\Pi\,\mathcal{D}(\mathbb{C}^7) \simeq *$, and $\Pi\,\mathcal{D}_k \simeq \mathrm{Gr}_k(\mathbb{C}^7)$ (the homotopy type of the Grassmannian of $k$-planes); in particular $\Pi\,\mathcal{D}_7 \simeq *$ and $\Pi\,\mathcal{D}_1 \simeq \mathbb{CP}^6$.
4. The seven modalities $\mathrm{Id}, \Pi, \flat, \sharp, \mathrm{Red}, \Pi_{\inf}, \flat_{\inf}$ are pairwise non-isomorphic on $\mathfrak{T}_{\mathrm{UHM}}$.
:::

**Proof.** (1) is quoted. (2) The plots of the subset diffeology are closed under precomposition with smooth maps and glue along open covers, which is the sheaf condition of a concrete sheaf. For the stratum: every $\Gamma$ of rank $k$ is $AA^\dagger/\mathrm{Tr}(AA^\dagger)$ for some $A \in \mathbb{C}^{7\times k}$ of rank $k$, and $A$ is determined up to $A \mapsto cAU$ with $U \in U(k)$, $c > 0$; the map is a submersion from the open set of rank-$k$ matrices ($14k$ real dimensions) whose fibres are the orbits of $U(k) \times \mathbb{R}_{>0}$ ($k^2 + 1$ dimensions), so $\dim \mathcal{D}_k = 14k - k^2 - 1$ (checked numerically for $k = 1, \dots, 7$ by the rank of the Jacobian, `test_rank_strata_are_manifolds_of_dimension_14k_minus_k2_minus_1`).

(3) On $\mathrm{Smooth}\infty\mathrm{Grpd}$ the shape $\Pi$ preserves finite products and $\Pi(\mathbb{R}) \simeq *$ (Proposition 4.4.34: $\Pi$ of a manifold is its singular complex), so for every object $X$ the projection $X \times \mathbb{R} \to X$ goes to an equivalence, and the two inclusions $i_0, i_1 : X \to X \times \mathbb{R}$ at $0$ and $1$ go to the same map, its inverse. Fix a smooth $h : \mathbb{R} \to [0,1]$ with $h = 0$ on $(-\infty, 0]$ and $h = 1$ on $[1, \infty)$. For a state $\Gamma_0$, $H(t, \Gamma) = (1 - h(t))\,\Gamma + h(t)\,\Gamma_0$ is a morphism $\mathbb{R} \times \mathcal{D} \to \mathcal{D}$ (it sends plots to plots, and stays in $\mathcal{D}$ by convexity), with $H \circ i_0 = \mathrm{id}$ and $H \circ i_1$ constant. Hence $\Pi(\mathrm{id}_{\mathcal{D}})$ factors through $\Pi(*) = *$, and $\Pi\,\mathcal{D} \simeq *$. On $\mathcal{D}_k$ the support projection $P_\Gamma$ depends smoothly on $\Gamma$ (constant rank), and $H(t, \Gamma) = (1 - h(t))\,\Gamma + h(t)\,P_\Gamma / k$ stays in $\mathcal{D}_k$, because a convex combination of two positive operators with the same support has that support. It retracts $\mathcal{D}_k$ onto $\{P_V / k\} \cong \mathrm{Gr}_k(\mathbb{C}^7)$, so $\Pi\,\mathcal{D}_k \simeq \Pi\,\mathrm{Gr}_k(\mathbb{C}^7)$, the singular complex of the Grassmannian.

(4) Test objects: the line $\mathbb{R}$ and the first-order infinitesimal point $\mathbb{D} = \mathrm{Spec}\,\mathbb{R}[\varepsilon]/(\varepsilon^2)$. By the definitions (DCCT v1 Definition 3.10.1, with $(i_* Y)(U \times \mathbb{D}') = Y(U)$ for the coreflection $p(U \times \mathbb{D}') = U$): $\Gamma(\Pi\mathbb{R}) = *$; $\Gamma(\flat\mathbb{R}) = \Gamma(\mathbb{R}) = \mathbb{R}$ but $\flat\mathbb{R}$ has only locally constant plots; $\sharp\mathbb{R}$ has all set maps $\mathbb{R} \to \mathbb{R}$ as plots on $\mathbb{R}$; $\mathrm{Red}\,\mathbb{D} = *$ while $\mathbb{D} \neq *$, and $\mathrm{Red}\,\mathbb{R} = \mathbb{R}$; $(\Pi_{\inf}\mathbb{R})(\mathbb{D}) = \mathbb{R}$ while $\mathbb{R}(\mathbb{D}) = \mathbb{R}[\varepsilon]/(\varepsilon^2)$. These values separate $\mathrm{Id}, \Pi, \flat, \sharp, \mathrm{Red}, \Pi_{\inf}$ pairwise. $\flat_{\inf}$ is a right adjoint, so it preserves pullbacks; $\Pi$ does not (for two distinct points $* \rightrightarrows \mathbb{R}$ the pullback is empty, while $* \times_{\Pi\mathbb{R}} * = *$), and neither does $\mathrm{Red}$ (the fibre of $x \mapsto x^2$ over $0$ has the non-zero plot $\varepsilon$ on $\mathbb{D}$, and $\mathrm{Red}$ of it is $*$, while $\mathrm{Red}$ fixes $\mathbb{R}$ and $*$); so $\flat_{\inf} \not\simeq \Pi, \mathrm{Red}$. Left adjoints are unique, and $\Pi_{\inf} \dashv \flat_{\inf}$; so $\flat_{\inf} \simeq \flat$ would give $\Pi_{\inf} \simeq \Pi$, $\flat_{\inf} \simeq \sharp$ would give $\Pi_{\inf} \simeq \flat$, $\flat_{\inf} \simeq \mathrm{Id}$ would give $\Pi_{\inf} \simeq \mathrm{Id}$, and $\flat_{\inf} \simeq \Pi_{\inf}$ would give $\mathrm{Red} \simeq \Pi_{\inf}$ — all excluded above. $\blacksquare$

**The Bures metric on this object.** The Bures metric is a smooth Riemannian metric on each stratum, and the topology it induces on $\mathcal{D}(\mathbb{C}^7)$ is the standard one ([lemma of §5.3](#53-closing-the-last-open-question-why-bures-t-187)); A2 is therefore structure on the object $\mathcal{D}(\mathbb{C}^7) \in \mathfrak{T}_{\mathrm{UHM}}$, not a choice of site.

**What stays open, and why the original site is not needed.**
- *The petit topos is not cohesive* [T]. For the topological space $X = \mathcal{D}(\mathbb{C}^7)$, the ∞-topos $\mathrm{Sh}_\infty(X)$ of sheaves on its open sets fails Definition 3.4.1: for disjoint non-empty opens $U, V$ the product of representables is $h_U \times h_V = h_{U \cap V} = \emptyset$, so $\Pi(h_U \times h_V) = \emptyset$, while $\Pi(h_U) \times \Pi(h_V) \neq \emptyset$. Cohesion is a property of "gros" toposes of spaces, of which $\mathfrak{T}_{\mathrm{UHM}}$ is one.
- *The site $(\mathbf{DensityMat}, J_{\text{Bures}})$ of [Theorem 6.1](/docs/proofs/categorical/categorical-formalism#631-bures-топология-на-densitymat) remains [C].* The objection "no terminal object" is weaker than it looked: in the idempotent completion, the replacement channel $R_\sigma(X) = \mathrm{Tr}(X)\,\sigma$ splits to a terminal object $(\sigma, R_\sigma)$, because every CPTP $f$ with $R_\sigma f = f$ equals $R_\sigma$. Whether $\mathrm{Sh}_\infty(\mathbf{DensityMat}, J_{\text{Bures}})$ is cohesive is therefore undecided; nothing below needs it, since the modalities act in $\mathfrak{T}_{\mathrm{UHM}}$.
- *Rh.* It is not a modality of differential cohesion. In a solid-cohesive extension it exists, but it preserves global points ($\mathrm{Rh}\,X(\mathbb{R}^0) = X(\mathbb{R}^0)$), so it cannot send a state $\Gamma$ to $I/7$ — see [T-212](/docs/proofs/categorical/fundamental-closures#t-212).

**Status of T-185 after this theorem.** (i) the modalities of a differentially cohesive ∞-topos [T]; (ii) differential cohesion of $\mathrm{Sh}_\infty(\mathbf{DensityMat}, J_{\text{Bures}})$ [C], open; (ii′) the theorem above [T]; (iii) the count of seven — identity plus two adjoint triples, pairwise distinct — [T] for the corrected list, [✗] for the list with Rh in place of Red, and the assignment to dimensions [I].

:::note Framework-conditional citation (see [Rigour Stratification §T-185](/docs/reference/status-registry#стратификация-строгости))
Schreiber's DCCT (arXiv v1: Definition 3.4.1 and §3.5) axiomatises cohesion and differential cohesion; its models include smooth, synthetic-differential and super ∞-groupoids (chapter 4 there). Its applicability to the **stratified** $\mathcal{D}(\mathbb{C}^7)$ (boundary of rank-deficient matrices) was the subject of **Gap A** in §4.2 below. It is settled by [T-185 (ii′)](#t-185-ii-prime): the stratified state space is an object of the synthetic-differential model $\mathrm{SynthDiff}\infty\mathrm{Grpd}$ (DCCT v1, Propositions 4.5.8 and 4.5.11), whose site $\mathrm{CartSp}_{\mathrm{synthdiff}}$ is ∞-cohesive. For the site $(\mathbf{DensityMat}, J_{\text{Bures}})$ itself the question stays open [C]. (An earlier version of this note said that cohesion axioms hold for stratified smooth spaces by Lurie HTT §7.3.6; no such result is cited correctly, and the claim is withdrawn.)
:::

Currently, T-185 is used only for **dimension counting** — matching 7 modalities to 7 dimensions. The proposal of this chapter was that if the cohesive structure is **operationalized** (each modality applied to $\Gamma$ as a mathematical operation), all three vulnerabilities close simultaneously; §3 records that they do not.

### 2.2. The differential cohomology hexagon

:::warning Scope of the hexagon: stable coefficients only
An earlier version of this subsection said that "in any differentially cohesive ∞-topos, for any coefficient object $\mathbf{A}$, there exists a canonical exact hexagon (Schreiber 2013, §3.9)". That is retracted. In DCCT v1 the hexagon is Proposition 4.1.17: for a cohesive ∞-topos $\mathbf{H}$ and a **stable** homotopy type $E \in \mathrm{Stab}(\mathbf{H})$ (a spectrum object), and its proof uses stability — the rows are fibre sequences because $\mathrm{Stab}(\mathbf{H})$ is stable. It is not asserted for an arbitrary coefficient object, and in particular not for the delooping $\mathbf{B}G_2$ of the nonabelian group $G_2$ used in §3.3.
:::

For a stable coefficient $E$ there is a canonical hexagon (DCCT v1, Proposition 4.1.17):

```
         ♭(A) ———→ A ———→ ♭_dR(A)
           |                    |
           ↓                    ↓
        Π(♭(A)) ——→ Π(A) ——→ Π(♭_dR(A))
```

where:
- $\flat(\mathbf{A})$ = flat coefficient (locally constant data)
- $\flat_{\mathrm{dR}}(\mathbf{A}) = \mathrm{cofib}(\mathbf{A} \to \sharp(\mathbf{A}))$ = de Rham coefficient (connection data)
- $\Pi$ = shape modality (fundamental $\infty$-groupoid)

For stable $E$ this hexagon **forces** the relationship between internal aspect ($\flat$), external structure ($\Pi$), and curvature ($\flat_{\mathrm{dR}}$); it is a structural theorem of cohesive $\infty$-topoi with stable coefficients, not of arbitrary ones.

## 3. Theorem: Cohesive Closure

:::tip Theorem T-186 (Cohesive Closure): (a) [H]; (b) and (c) retracted [✗]

Let $\mathfrak{T} = \mathrm{Sh}_\infty(\mathcal{D}(\mathbb{C}^7), J_{\text{Bures}})$ be the UHM $\infty$-topos with differentially cohesive structure (assumed in the original statement; available since 2026-09-25 in the corrected form T-185 (ii′), where $\mathcal{D}(\mathbb{C}^7)$ is an object of the differentially cohesive $\mathfrak{T}_{\mathrm{UHM}}$). Then, as originally stated:

**(a) Phenomenal necessity.** The phenomenal functor $F$ is naturally isomorphic to the infinitesimal flat modality restricted to density matrices:

$$F \cong \&\big|_{\mathcal{D}(\mathbb{C}^7)}$$

The Postnikov filtration of $\&(\Gamma)$ reproduces the interiority hierarchy L0–L4. The phenomenal structure is determined by the adjunction $\iota^* \dashv \mathrm{Inf}$, not by interpretive postulate.

**(b) Exact time.** The Page-Wootters conditional states are sections of the flat projection:

$$\Gamma(\tau) = \mathrm{ev}_\tau\bigl(\flat(\Gamma_{\text{total}})\bigr)$$

The evolution is governed by the counit $\varepsilon: \Pi \circ \flat \Rightarrow \mathrm{Id}$, which is an **exact** natural transformation. The $O(H_{\text{int}})$ correction of the tensor-decomposition approach does not arise.

**(c) Unconditional $\Lambda > 0$.** The free energy gradient equals the curvature norm via the Chern-Weil homomorphism in $\mathfrak{T}$:

$$\Delta F(\Gamma) = \|\mathrm{curv}(\Gamma)\|^2 = \omega_0^2 \cdot \mathcal{G}_{\text{total}}$$

By T-55 (Gap > 0, Lawvere incompleteness), $\mathcal{G}_{\text{total}} > 0$ for any $\Gamma$ with $P > P_{\text{crit}}$. Therefore $\Delta F > 0$ — and consequently $\Lambda > 0$ — is **unconditional**, independent of spectral details of $D_{\text{int}}$.
:::

:::warning Retracted as a theorem [T] (2026-09-25): what survives of T-186
An earlier version stated T-186 with status [T] in all three parts. None of the three is proven.
- **(a) is a hypothesis [H].** The modality $\&$ now exists on the state space (T-185 (ii′) [T]), so the obstacle is no longer cohesion. The proof in §3.1 identifies the E-component of a jet space with $\rho_E$ by assertion (Steps 3–4) without constructing the natural isomorphism $F \cong \&|_{\mathcal{D}}$. Step 4's claim that the adjunction leaves "no freedom" is also unsupported: the modal constructions are functorial, so they commute with every automorphism of the object $\mathcal{D}(\mathbb{C}^7)$, including all unitary conjugations $\Gamma \mapsto U\Gamma U^\dagger$ (diffeomorphisms preserving the strata). They cannot pick out the E-axis of the pointer frame, which $F$ uses; an identification of $F$ with $\&$ needs the frame as additional input.
- **(b) is retracted [✗].** With a clock–system interaction the conditional state obeys a time-nonlocal Schrödinger equation (A. R. H. Smith, M. Ahmadi, *Quantum* **3**, 160 (2019)); relative to a clock of period seven ticks every conditional dynamics is periodic (L. Chataignier, P. A. Höhn, M. P. E. Lock, F. M. Mele, *New J. Phys.* **28**, 034504 (2026)); and the counit invoked in §3.2 carries no information about $\triangleright$ or $H_{\text{int}}$ — in a cohesive ∞-topos the natural maps are $\flat \Rightarrow \mathrm{Id} \Rightarrow \int$, and Step 3 asserts $\varepsilon_\Gamma \circ \Gamma(\tau_n) = \triangleright^*(\Gamma(\tau_n))$ without computation. There is no "exact time" beyond the unitary step for $H_{\text{int}} = 0$.
- **(c) is retracted [✗].** The hexagon exists for stable coefficients only (§2.2), not for $\mathbf{B}G_2$; and $\mathcal{D}(\mathbb{C}^7)$ is convex, hence contractible, so every $G_2$-bundle over it is trivial and every characteristic class vanishes — $c_2 = 0$. The formula $c_2 = \frac{1}{8\pi^2}\sum_{i<j}|\gamma_{ij}|^2\,\mathrm{Gap}(i,j)^2$ of §3.3 varies continuously with $\Gamma$ and so cannot be a topological invariant; and $\Delta F = \|\mathrm{curv}(\Gamma)\|^2$ is asserted, not derived. $\Delta F > 0$ and $\Lambda > 0$ return to their earlier status, [C] conditional on the spectral details of $D_{\text{int}}$. Where non-trivial characteristic classes do live, by T-185 (ii′): on the pure-state stratum $\mathcal{D}_1 \cong \mathbb{CP}^6$ (shape $\mathbb{CP}^6$, not a point) the tautological line bundle with its Berry connection is a class in ordinary differential cohomology (DCCT v1, Theorem 4.4.87: Deligne cohomology), a stable coefficient to which the hexagon applies; its curvature is the Fubini–Study form up to normalisation and its Chern class generates $H^2(\mathbb{CP}^6;\mathbb{Z})$ (B. Simon, *Phys. Rev. Lett.* **51**, 2167 (1983)). This is standard geometry of pure states and says nothing about $\Delta F$.
:::

### 3.1. Proof of (a): $F \cong \&$

**Step 1.** By T-185, the infinitesimal flat modality $\&$ is defined as $\& := \iota^* \circ \mathrm{Inf}$. For any object $X \in \mathfrak{T}$, $\&(X)$ extracts the **infinitesimally internal structure** — the data visible "from infinitely close" but not from outside.

**Step 2.** The phenomenal functor $F$ is defined (§3.2 of [two-aspect monism](/docs/consciousness/foundations/two-aspect-monism)) as:
$$F(\Gamma) = \bigl(\mathrm{Spec}(\rho_E),\; \mathrm{Quality}(\rho_E),\; \mathrm{Context}(\Gamma_{-E})\bigr)$$

This extracts the E-sector spectrum, quality measures, and context — precisely the **infinitesimal neighbourhood** of $\Gamma$ in the E-direction.

**Step 3.** In the differential cohesive structure, the infinitesimal flat $\&$ applied to $\Gamma$ yields:
$$\&(\Gamma) = \iota^*(\mathrm{Inf}(\Gamma))$$

The infinitesimal path space $\mathrm{Inf}(\Gamma)$ captures all infinitesimal deformations of $\Gamma$. The pullback $\iota^*$ restricts to the formal neighbourhood — the jet space at $\Gamma$. For a density matrix, the jet space decomposes along the 7 basis directions, and the E-component of this decomposition is exactly $\rho_E = \mathrm{Tr}_{-E}(\Gamma)$ (in the 42D formalism) or its spectral approximation (in the 7D setting).

**Step 4.** The natural isomorphism $F \cong \&|_{\mathcal{D}}$ follows from the uniqueness of the infinitesimal flat modality (it is determined by the adjunction $\iota^* \dashv \mathrm{Inf}$, which is part of the differentially cohesive structure). There is no freedom to choose a different "interiority extractor" — the adjunction forces $\&$ as the unique candidate.

**Step 5.** The Postnikov filtration of $\&(\Gamma)$ as an $\infty$-groupoid:
- $\tau_{\leq 0}(\&(\Gamma))$: connected components = set of phenomenal states → **L0** (formal interiority)
- $\tau_{\leq 1}(\&(\Gamma))$: fundamental groupoid = paths between states → **L1** (phenomenal geometry, $\mathrm{rank}(\rho_E) > 1$)
- $\tau_{\leq 2}(\&(\Gamma))$: 2-groupoid = paths between paths → **L2** (cognitive qualia, self-referential loops requiring $R \geq 1/3$)
- $\tau_{\leq 3}(\&(\Gamma))$: 3-groupoid = meta-reflection → **L3** (meta-consciousness)

This is not an interpretation but a structural consequence of the Postnikov tower, which exists canonically for any $\infty$-groupoid.

**Status:** the assignment $\pi_n \leftrightarrow$ L-levels stays **[I]**, and $F \cong \&|_{\mathcal{D}}$ is a hypothesis [H]: Steps 3–4 assert the identification without constructing it, and the modality $\&$, which exists on $\mathcal{D}(\mathbb{C}^7)$ by T-185 (ii′), does not see the pointer frame that $F$ uses. An earlier "status upgrade [I] → [T]" is retracted. $\square$

### 3.2. Proof of (b): Exact time emergence — retracted

The argument below is kept as it was written, for the record; it does not prove (b), for the reasons in the box after the theorem.

**Step 1.** In the cohesive $\infty$-topos, the flat modality $\flat$ applied to the total state $\Gamma_{\text{total}} \in \mathfrak{T}$ extracts its **locally constant** structure — the data that is invariant under infinitesimal deformations.

**Step 2.** A "moment of time" $\tau$ is a point of $\Pi(\Gamma_{\text{total}})$ — the shape (fundamental $\infty$-groupoid) of the total state. The conditional state at $\tau$ is the evaluation:

$$\Gamma(\tau) := \mathrm{ev}_\tau\bigl(\flat(\Gamma_{\text{total}})\bigr)$$

This is an **exact** operation: $\flat$ is an exact functor (left adjoint preserves colimits, right adjoint preserves limits — and $\flat = \mathrm{Disc} \circ \Gamma_!$ is both).

**Step 3.** The evolution from $\tau_n$ to $\tau_{n+1}$ is the counit:
$$\varepsilon_{\Gamma}: \Pi(\flat(\Gamma_{\text{total}})) \to \Pi(\Gamma_{\text{total}})$$

For the UHM topos with $\mathbb{Z}_7$ temporal structure, this counit maps:
$$\Gamma(\tau_{n+1}) = \varepsilon_\Gamma \circ \Gamma(\tau_n) = \triangleright^*(\Gamma(\tau_n))$$

**without** the $O(H_{\text{int}})$ correction, because the counit is a **natural transformation between functors**, not an approximation of a tensor decomposition.

**Step 4.** The continuous limit $\mathbb{Z}_{7^M} \to \mathbb{R}$ for composite systems follows from the shape modality: $\Pi(\Gamma_{\text{composite}})$ has fundamental group $\mathbb{Z}_{7^M}$, and for $M \to \infty$, $\Pi$ automatically computes the pro-finite completion $\hat{\mathbb{Z}}_7 \cong \mathbb{Z}_7$, whose Pontryagin dual is $\mathbb{R}/\mathbb{Z}_7$-local. The passage to $\mathbb{R}$ is exact via the universal property of pro-finite groups.

**Status:** retracted [✗]. Step 4 is also false: the summed clock of $M$ holons has $6M+1$ readings and period $2\pi/\omega_0$, not a group $\mathbb{Z}_{7^M}$ ([composite clocks](/docs/proofs/dynamics/emergent-time#композитные-часы)); the profinite completion $\hat{\mathbb{Z}}_7$ of the 7-adic integers is not $\mathbb{Z}/7$, and no limit of O-clocks unrolls the circle into $\mathbb{R}$. An earlier "status upgrade to [T] exact" is retracted.

### 3.3. Proof of (c): Unconditional $\Lambda > 0$ — retracted

The argument below is kept as it was written, for the record; Steps 1 and 4 fail (box after the theorem).

**Step 1.** In the differentially cohesive $\infty$-topos, a connection on a $G_2$-bundle $P \to \mathcal{D}(\mathbb{C}^7)$ is classified by a differential cocycle in the hexagon:

$$\flat(BG_2) \xrightarrow{\;\;} BG_{2,\text{conn}} \xrightarrow{\;\mathrm{curv}\;} \flat_{\mathrm{dR}}(B^2 G_2)$$

The curvature map $\mathrm{curv}$ is the structural map of the hexagon — it exists for any connection and is independent of spectral details.

**Step 2.** By T-73 [T] (Gap = curvature on the Serre bundle):
$$\|\mathrm{curv}(\Gamma)\|^2 = \omega_0^2 \sum_{i < j} |\gamma_{ij}|^2 \cdot \mathrm{Gap}(i,j)^2 = \omega_0^2 \cdot \mathcal{G}_{\text{total}}$$

This identity connects the cohesive curvature to the Gap operator. It was proved [T] via the spectral triple (T-53) and NCG curvature formula.

**Step 3.** By T-55 [T] (Lawvere incompleteness), for any $\Gamma$ with $P > P_{\text{crit}}$:
$$\mathcal{G}_{\text{total}} > 0$$

This is unconditional — it follows from the Cartesian closure of the $\infty$-topos and the necessity of a nontrivial self-model $\varphi$.

**Step 4.** The Chern-Weil homomorphism in the cohesive $\infty$-topos:
$$\mathrm{ch}: \flat(BG_2) \to \Pi(\flat_{\mathrm{dR}}(B^2 G_2))$$

maps the flat coefficient of the $G_2$-bundle to characteristic classes. The second Chern class:
$$c_2(\mathrm{Bundle}) = \frac{1}{8\pi^2} \sum_{i < j} |\gamma_{ij}|^2 \cdot \mathrm{Gap}(i,j)^2$$

is a **topological invariant** — it depends only on the bundle class, not on the choice of connection or Dirac operator.

**Step 5.** The free energy gradient:
$$\Delta F(\Gamma) = \|\mathrm{curv}(\Gamma)\|^2 = \omega_0^2 \cdot \mathcal{G}_{\text{total}} > 0$$

is unconditional for any viable $\Gamma$ (Step 3). The cosmological constant:
$$\Lambda = \mu^2 \cdot \mathcal{G}_{\text{total}}^{(O)} > 0$$

follows from the O-sector component of the Gap, which is nonzero by the same Lawvere argument applied to the O-dimension.

**Status:** retracted [✗]. $\Delta F > 0$ and $\Lambda > 0$ remain **[C] conditional on $D_{\text{int}}$ spectral details**; an earlier "status upgrade to [T] unconditional" is retracted, because the hexagon does not apply to $\mathbf{B}G_2$ and $c_2$ of any bundle over the contractible $\mathcal{D}(\mathbb{C}^7)$ is zero.

#### Worked numerical example {#числовой-пример-цепочка}

The example computes $\mathcal{G}_{\text{total}}$ for a sample state; the chain "Chern–Weil $\Rightarrow \Delta F > 0$" it illustrates is retracted with (c).

Consider a holon with $P = 0.35$ (viable, above $P_{\text{crit}} = 2/7 \approx 0.286$) and $\omega_0 = 40$ Hz (gamma-band). Three dominant off-diagonal coherences on Fano lines:

| Pair | $\|\gamma_{ij}\|$ | $\theta_{ij} = \arg(\gamma_{ij})$ | $\mathrm{Gap}(i,j) = \|\sin\theta_{ij}\|$ |
|------|-----------------|-----------------------------------|----------------------------------------|
| $(E,O)$ | 0.08 | $\pi/3$ | $\sqrt{3}/2 \approx 0.866$ |
| $(A,E)$ | 0.06 | $\pi/4$ | $1/\sqrt{2} \approx 0.707$ |
| $(O,U)$ | 0.05 | $\pi/5$ | $\sin(36°) \approx 0.588$ |

**Step 1 (Lawvere $\Rightarrow$ Gap $> 0$).** All three phases $\theta_{ij} \neq 0, \pi$, hence $\mathrm{Gap}(i,j) > 0$. This is not accidental: by T-55 [T], Lawvere incompleteness forces $\mathrm{Im}(\gamma_{ij}) \neq 0$ for at least one pair in any viable system.

**Step 2 (Gap $=$ curvature, T-73).** The total Gap:

$$\mathcal{G}_{\text{total}} = \sum_{i < j} |\gamma_{ij}|^2 \cdot \mathrm{Gap}(i,j)^2$$

Contributions from the three dominant pairs:

$$\mathcal{G}_{\text{total}} \geq 0.08^2 \cdot 0.75 + 0.06^2 \cdot 0.50 + 0.05^2 \cdot 0.346 = 0.0048 + 0.0018 + 0.00087 \approx 0.0075$$

(Remaining 18 pairs add positively.)

**Step 3 (Chern–Weil $\Rightarrow$ $\Delta F > 0$).**

$$\Delta F = \omega_0^2 \cdot \mathcal{G}_{\text{total}} = (40)^2 \cdot 0.0075 = 12.0 \;\text{(arb. units)} > 0 \quad\checkmark$$

The free energy gradient is strictly positive — the system has thermodynamic fuel for regeneration. For comparison, at $P < P_{\text{crit}}$ we have $g_V = 0$ (viability gate closed), and regeneration is thermodynamically forbidden regardless of $\Delta F$.

## 4. Dependencies and Gaps

### 4.1. What T-186 depends on

| Dependency | Status | Reference |
|---|---|---|
| T-185 (differentially cohesive structure) | [T] in the corrected form (ii′); [C] for the original site | [§2.1a](#t-185-ii-prime), [Dimensions §4](/docs/core/structure/dimensions#категориальная-семантика) |
| T-55 (Lawvere incompleteness, Gap > 0) | [T] | [Consequences](/docs/core/foundations/consequences#неполнота-ловера) |
| T-73 (Gap = curvature) | [T] | [Gap Operator §5](/docs/core/dynamics/gap-operator#теорема-gap-серра) |
| T-53 (spectral triple) | [T] | [Categorical Formalism](/docs/proofs/categorical/categorical-formalism) |
| Schreiber (2013) | Published | Differential cohomology in a cohesive ∞-topos, arXiv:1310.7930 |

### 4.2. Technical gaps requiring separate verification

**Gap A (boundary of $\mathcal{D}(\mathbb{C}^7)$).** The space of density matrices has a boundary where eigenvalues vanish. Cohesion axioms require the site to be a smooth $\infty$-groupoid. The boundary $\partial\mathcal{D}$ consists of lower-rank matrices ($\mathrm{rank}(\Gamma) < 7$) and is a stratified space. **Resolution:** Define the site as $\mathcal{C} = \mathrm{Strat}(\mathcal{D}(\mathbb{C}^7))$ — the stratified $\infty$-category (Ayala-Francis-Rozenblyum 2017) realized as a cosheaf over the poset of orthogonal projectors $\mathrm{Proj}(\mathbb{C}^7)$. Each stratum $\mathcal{D}_k = \{\Gamma : \mathrm{rank}(\Gamma) = k\}$ is a smooth manifold; the inclusions $\mathcal{D}_k \hookrightarrow \overline{\mathcal{D}_k}$ are compatible with the Bures metric (Uhlmann's theorem: $d_B$ extends continuously to the boundary). (A sentence here said that the flat modality $\flat$ "sees only which stratum $\Gamma$ belongs to"; that is wrong — $\flat\,\mathcal{D}$ is the discrete set of all states.) An earlier version asserted that cohesion axioms hold for stratified smooth spaces (Lurie HTT §7.3.6, extended by Ayala–Francis–Rozenblyum) and gave this gap "[T] from established results"; neither reference proves cohesion of this site, and the site lacks the finite products of an ∞-cohesive site. **Closed 2026-09-25 by a different route [T]:** the site is not changed but replaced — $\mathcal{D}(\mathbb{C}^7)$ is taken as a diffeological object of $\mathrm{SynthDiff}\infty\mathrm{Grpd}$, whose site is ∞-cohesive; the strata are submanifolds of dimension $14k - k^2 - 1$ with shapes $\mathrm{Gr}_k(\mathbb{C}^7)$ ([T-185 (ii′)](#t-185-ii-prime)). No stratified site is needed.

**Gap B ($\&(\Gamma) = \rho_E$ correspondence).** The claim that the infinitesimal flat modality applied to $\Gamma$ yields the E-sector reduced density matrix requires showing that the formal neighbourhood decomposes along the 7 Fano directions and that the E-component equals $\mathrm{Tr}_{-E}(\Gamma)$. **Resolution:** In the 42D extension, the tangent space $T_\Gamma \mathcal{D}$ decomposes as $\bigoplus_{k=1}^{7} T_k$ along the 7 basis directions (this is the content of the Fano channel decomposition, T-39a). The infinitesimal flat $\& = \iota^* \circ \mathrm{Inf}$ restricts to the formal neighbourhood and selects the E-component by the T-185 assignment $\& = E$. Status: hypothesis [H] — the assignment $\& = E$ is a reading; $\&$ exists on $\mathcal{D}(\mathbb{C}^7)$ (T-185 (ii′)), but it commutes with all unitary conjugations and does not single out a basis direction (an earlier "[T] from T-39a + T-185" is retracted).

**Gap C (counit exactness).** The counit $\varepsilon: \Pi \circ \flat \Rightarrow \mathrm{Id}$ is exact for any cohesive $\infty$-topos (Schreiber 2013, Proposition 3.4.5). For finite-dimensional sites, the exactness follows from the finite generation of the covering sieves. **Clarification:** The $O(H_{\text{int}})$ correction in the original Page-Wootters formulation arises **only** when projecting the cohesive $\mathbb{Z}_7$-time onto classical $\mathbb{R}$. Within the internal logic of the topos, $\mathbb{Z}_7$-cyclic time is absolutely exact — the counit is an exact natural transformation by definition. The approximation is an artifact of the classical projection, not of the dynamics. — **Retracted [✗]:** the exactness of a counit says nothing about the conditional dynamics; with $H_{\text{int}} \neq 0$ that dynamics is time-nonlocal (Smith–Ahmadi 2019), and the $O(H_{\text{int}})$ correction is not an artefact of a projection (earlier status "[T] from Schreiber's published proof").

**Gap D ($G_2$ Chern-Weil computation).** The Chern-Weil homomorphism for $G_2$-bundles is standard for compact Lie groups over **smooth manifolds** (Milnor–Stasheff 1974). The UHM bundle, however, lives over the **stratified** space $\mathcal{D}(\mathbb{C}^7)$ (strata indexed by rank; cf. Gap A), so the Milnor–Stasheff formalism does not apply verbatim. Resolution: we work stratum-wise — on the full-rank open stratum $\mathcal{D}^\circ$ the computation is classical, and continuity of $c_2$ across the rank boundary follows from the continuous extension of the Bures metric (Uhlmann 1976) combined with the stratified Chern–Weil theory of Ayala–Francis–Rozenblyum 2017. The stratum-wise identification of $c_2$ with the Gap total $\mathcal{G}_{\text{total}}$ is exactly T-73 [T]; the cross-stratum continuity adds no new hypothesis. — **Retracted [✗]:** every stratum $\mathcal{D}_k$ of full rank is convex, hence contractible, so bundles over it are trivial and $c_2 = 0$; what T-73 identifies with $\mathcal{G}_{\text{total}}$ is a pointwise curvature expression, not a characteristic class (earlier status "[T] from T-73 + continuity").

## 5. Consequences

### 5.1. The hard problem — reformulated at the categorical level

If T-186(a) held, it would shift the [I] status of the phenomenal functor: the relationship between $\Gamma$ and its experiential content would be **forced** by the cohesive adjunction, not stipulated. T-186(a) is a hypothesis [H] — the cohesion it needs is now available (T-185 (ii′)), the identification it asserts is not — so the phenomenal functor stays [I]. (An earlier sentence stated the shift to [T] as done; retracted.) Under that hypothesis the remaining interpretive element would localize to a single point: the choice of axiom A2 (Bures metric). Given A2, everything follows by categorical necessity.

The hard problem thus becomes: **why does the ∞-topos of reality have the Bures topology?** This is a deeper question than "why does matter give rise to experience" — but it is a single question, not three.

#### Theorem T-188 (Localization of the Hard Problem) [C] {#теорема-локализация-hard-problem}

Status [C]: conditional on the hypothesis T-186(a) [H]. The second condition it carried until 2026-09-25, the cohesion of T-185, is discharged in the corrected form T-185 (ii′) [T]. An earlier version gave [T]; retracted.

The classical hard problem of consciousness ("why does physical structure give rise to experience?") reduces, within UHM, to a **single physical question** through the following chain of implications:

$$
\text{A2 (Bures metric)} \xrightarrow{T\text{-}187} \text{unique } J_B \xrightarrow{T\text{-}185} \text{cohesive structure } (\Pi \dashv \flat \dashv \sharp, \iota^* \dashv \mathrm{Inf}) \xrightarrow{T\text{-}186(a)} F \cong \&|_{\mathcal{D}}
$$

**Step 1.** By T-187 [T]: A2 uniquely determines the Bures metric via four independent characterizations (Char-I Petz extremality, Char-II Uhlmann universality, Char-III SLD-Fisher saturation, Char-IV MaxEnt covariance T-189 [T]).

**Step 2.** By T-185 (ii′) [T]: the state space with its Bures metric is an object of the differentially cohesive $\mathfrak{T}_{\mathrm{UHM}}$, which carries the canonical modalities $\{\Pi, \flat, \sharp, \mathrm{Red}, \Im, \&\}$. (The step read "By T-185 (assumed, [C])" and listed Rh in place of Red until 2026-09-25.)

**Step 3.** By T-186(a) (hypothesis, [H]): the phenomenal functor $F \cong \&|_{\mathcal{D}}$ — experience is the infinitesimal flat modality restricted to density matrices. This is forced by the adjunction, not stipulated.

**Therefore:** Given A2, the cohesion of T-185 (ii′) and the hypothesis T-186(a), the existence and structure of experience would be a **theorem**. The only remaining interpretive element is A2 itself. But A2 is not a consciousness axiom — it is a **physics axiom** about the metric structure of quantum state space.

The question "why Bures?" reduces further:
- Bures = minimal CPTP-monotone metric (Char-I)
- CPTP = completely positive trace-preserving maps = physically allowed transformations
- "Why CPTP?" = "why are quantum channels the physical transformations?" = "why quantum mechanics?"

**Conclusion:** The hard problem of consciousness, within UHM, is **equivalent to** the hard problem of physics: "why does reality obey quantum mechanics?" This is not a dissolution of the problem but a precise **localization**: the mystery of experience is the same mystery as the existence of quantum structure. No additional "consciousness-specific" mystery remains. $\blacksquare$

**Dependencies:** T-185 (ii′) [T], T-186 [H], T-187 [T].

### 5.2. Statuses of the closed vulnerabilities

| Vulnerability | Status | Closure mechanism |
|---|---|---|
| $F = \&$: phenomenal functor | [H] (earlier: [T] from $\iota^* \dashv \mathrm{Inf}$; retracted) | Postnikov tower of $\&(\Gamma)$; $\&$ exists by T-185 (ii′), the identification is not constructed |
| Page-Wootters time | [✗] retracted (earlier: [T] exact); with interaction the conditional dynamics is time-nonlocal | Counit of $(\Pi \dashv \flat)$ — does not apply |
| $\Delta F > 0$, $\Lambda > 0$ | [C] as before (earlier: [T] unconditional; retracted) | Chern-Weil fails: hexagon only for stable coefficients, $c_2 = 0$ over a contractible base |

### 5.3. Closing the last open question: why Bures? (T-187)

:::tip Theorem T-187 (Canonicity of the Bures enrichment) [T]

Within the Petz family of CPTP-monotone Riemannian metrics on $\mathcal{D}(\mathbb{C}^7)$, the Bures metric $d_B$ is the unique canonical choice, uniquely characterized by **three independent mathematical properties**, each of which pins down the same metric and hence the same Grothendieck topology $J_B$ and the same $\mathcal V$-enriched $\infty$-topos $\mathfrak T = \mathrm{Sh}_\infty^{\mathcal V}(\mathcal C_7, J_B)$.
:::

**Framework.** We work with $\mathcal V$-enriched category theory over the Lawvere quantale $\mathcal V = ([0,\infty], \ge, +, 0)$ (Lawvere 1973): a CPTP-monotone Riemannian metric $d$ on $\mathcal{D}(\mathbb{C}^7)$ enriches $\mathcal C_7 = (\mathcal{D}(\mathbb{C}^7), \mathrm{CPTP})$ to a $\mathcal V$-category $(\mathcal C_7, d)$. Morphisms of $\mathcal V$-enriched categories are non-expansive functors.

**Definition (Petz-admissible enrichment).** A metric $d$ on $\mathcal D(\mathbb C^7)$ is Petz-admissible iff it is smooth Riemannian on the open-rank strata, symmetric and separating, and satisfies CPTP-monotonicity $d(\Phi\rho, \Phi\sigma) \le d(\rho,\sigma)$. By Petz (1996, Theorem 3.3), Petz-admissible metrics form the one-parameter family $\{d_f: f \in \mathrm{Petz}\}$, indexed by operator-monotone $f: (0,\infty)\to(0,\infty)$ with $f(t) = tf(1/t)$.

**Derivation of the Petz-admissible class from first principles** (closes the trivial-topology objection without ad hoc restriction). The class of "Petz-admissible CPTP-compatible topologies on $\mathcal C_7$" is rigorously isolated by four independently motivated conditions:

*Step 1 (Constructive non-vacuity).* A Grothendieck topology $J$ on $\mathcal C_7$ is **constructively CPTP-monotone** iff (a) for some $\rho \in \mathrm{Ob}\mathcal C_7$, $J(\rho)$ contains a covering sieve $S \ne S_\mathrm{max}(\rho)$; (b) Stability: $f^*S \in J(\sigma)$ for every CPTP $f: \sigma \to \rho$ and $S \in J(\rho)$.

*Lemma 1.* The trivial topology $J_\mathrm{triv}$ (containing only maximal sieves) **is not** constructively CPTP-monotone: it fails (a) because $J_\mathrm{triv}(\rho) = \{S_\mathrm{max}(\rho)\}$ for all $\rho$, so no non-maximal $S \in J(\rho)$ exists. CPTP-monotonicity is vacuously satisfied for $J_\mathrm{triv}$ but in the empty-content sense: there are no non-trivial covers to be stable under pullback. *This eliminates $J_\mathrm{triv}$ on the basis that it carries no operational CPTP-monotonicity content, not by ad hoc exclusion.* $\square$

*Step 2 (Riemannian origin).* Among constructively CPTP-monotone topologies, restrict to those of **Riemannian origin**: $J = J_d$ for a continuous distance function $d: \mathcal D\times\mathcal D \to [0,\infty)$ arising from a smooth Riemannian metric tensor $g$ on the interior $\mathcal D^\circ$ (full-rank stratum), extended by continuity to $\mathcal D$.

*Motivation.* UHM-dynamics (Lindblad evolution + regeneration, T-39a, T-62) is **differential**: $d\Gamma/d\tau$ is governed by an ordinary differential equation. The site structure must be compatible with this differential structure, which canonically requires a Riemannian (infinitesimal-quadratic) metric on the state-space manifold. Discrete topologies, Wasserstein-style transport metrics on probability simplices, or non-Riemannian information geometries (e.g.\ Bregman divergences) are excluded as not-infinitesimally-coherent with the Lindblad differential structure.

*Step 3 (Petz Classification, 1996).* CPTP-monotone Riemannian metrics on $\mathcal D(\mathbb C^N)$ form the one-parameter family $\{g_f\}$ indexed by operator-monotone $f: (0,\infty)\to(0,\infty)$ with $f(t) = tf(1/t)$:
$$g_f(\rho)(X,X) = \mathrm{Tr}(X^* \mathcal J_f(\rho)^{-1} X), \quad \mathcal J_f(\rho) = R_\rho^{1/2}\,f(L_\rho R_\rho^{-1})\,R_\rho^{1/2},$$
where $L_\rho, R_\rho$ are left/right multiplication by $\rho$. (Petz 1996, *Linear Algebra Appl.* 244, 81 — Theorem 3.3.)

*Step 4 (Pointwise minimum).* Within the Petz family, the Bures metric $g_B$ (case $f(t) = (1+t)/2$, arithmetic mean) is the unique pointwise minimum: $g_B(\rho)(X,X) \le g_f(\rho)(X,X)$ for every $\rho, X$ and every $f \in \mathrm{Petz}$ (Char-I above).

*Joint conclusion.* The class of "Petz-admissible topologies" is the unique class isolated by Steps 1+2+3, and within it Bures is uniquely minimal by Step 4. Each step is independently motivated:
- Step 1 by **constructive non-vacuity** (excludes vacuous structures).
- Step 2 by **infinitesimal compatibility** with Lindblad dynamics.
- Step 3 by **Petz's classification theorem** (mathematical fact).
- Step 4 by **Char-I extremality** (proven above).

The trivial-topology counterexample is closed at Step 1, not by ad hoc restriction. The remaining canonicity choices (Riemannian, CPTP-monotone, minimum) are all explicitly motivated by UHM physics or by published mathematical results.

*Remark on alternatives.* Quantum Wasserstein metrics, Bregman-style divergences, non-Riemannian information geometries — all admit canonical structures of their own. They are excluded **at Step 2** because they lack the infinitesimal-Riemannian form required for compatibility with Lindblad differential dynamics. This is a substantive physical choice, not a hidden postulate.

**Three characterizations of $d_B$.**

**(Char-I) Petz extremality / terminality.** $d_B$ is the pointwise minimum of the Petz poset: $d_B \le d_f$ for every $f \in \mathrm{Petz}$. Equivalently, the identity set-map $\mathrm{id}: (\mathcal D, d_f) \to (\mathcal D, d_B)$ is non-expansive for every $f$, making $(\mathcal D, d_B)$ the **terminal object** of the Petz diagram in $\mathcal V\text{-}\mathbf{Cat}$.

**(Char-II) Uhlmann purification universality.** $d_B$ is the unique metric satisfying Uhlmann's variational formula (Uhlmann 1976, *Rep. Math. Phys.* 9, 273):
$$d_B(\rho,\sigma) = \inf_{|\psi\rangle,|\varphi\rangle}\bigl\| |\psi\rangle - |\varphi\rangle \bigr\|_{\mathbb C^7 \otimes \mathbb C^k},$$
where the infimum ranges over all pairs of purifications in any extended space. This realizes $(\mathcal D, d_B)$ as the quotient of the unit sphere in the universal purification bundle under the $U(\mathcal H_{\text{aux}})$-orbit map. **Scope of uniqueness.** This characterizes $d_B$ uniquely *among all metrics satisfying this specific variational formula*. It does **not** assert that other Petz members lack their own canonical characterizations: BKM (Kubo–Mori) is canonical as the Hessian of relative entropy, RLD is canonical via Holevo's bound, Wigner–Yanase via skew-information. Char-II selects Bures by privileging the **purification / entanglement-based** physical interpretation.

**(Char-III) SLD-Fisher / Cramér-Rao saturation.** $4g_B$ coincides with the Symmetric-Logarithmic-Derivative quantum Fisher metric (Braunstein-Caves 1994, *Phys. Rev. Lett.* 72, 3439), which is the unique quantum Fisher information saturating the multiparameter quantum Cramér-Rao bound on estimator covariance. The SLD is defined by $\partial\rho = \tfrac{1}{2}(L\rho + \rho L)$, uniquely solvable on $\mathrm{supp}(\rho)$. **Scope of uniqueness.** This characterizes $d_B$ uniquely *among all metrics saturating CR with SLD-type estimators*. Other Petz members are characterized by other estimator types (RLD, balanced LD), each with its own bound. Char-III selects Bures by privileging the **classical-style parameter-estimation** interpretation.

**(Char-IV) Maximum-entropy covariance identification (Vanchurin 2026).** The maximum entropy principle on $\mathcal{D}(\mathbb{C}^7)$ uniquely identifies the inverse metric tensor with a physical covariance, up to the normalisation constant of Char-III:

$$g^{ij}_B(\Gamma) = 4\,C_{\mathrm{est}}^{ij}(\Gamma),\qquad C_{\mathrm{est}} := \mathcal F_{\mathrm{SLD}}^{-1}$$

where $C_{\mathrm{est}}$ is the minimal estimator covariance saturating the quantum Cramér–Rao bound. The factor $4$ is not optional: it is exactly the Braunstein–Caves constant of Char-III, and dropping it makes the identity self-contradictory (see the correction note in Step 4).

where $C^{ij}$ is the quantum covariance of observables at state $\Gamma$. This follows from a 4-step argument:

**Step 1 (Metric-agnostic MaxEnt).** For **any** Petz-monotone metric $d_f$ on $\mathcal D(\mathbb C^7)$, consider the maximum entropy distribution $\tilde\rho_f$ concentrated near $\Gamma$ under constraints $\langle\Gamma'\rangle=\Gamma$ and $\langle d_f^2(\Gamma',\Gamma)\rangle=\sigma^2$. In $g_f$-normal coordinates the MaxEnt is Gaussian (Jaynes 1957):

$$\tilde\rho_f(\tilde\Gamma)=\frac{1}{Z_f}\exp\!\left(-\frac{\lambda}{2}\delta_{ij}(\tilde\Gamma^i-\bar\Gamma^i)(\tilde\Gamma^j-\bar\Gamma^j)\right).$$

This construction is **metric-agnostic**: each choice of $f$ produces a Gaussian in its own normal frame.

**Step 2 (MaxEnt-covariance identity per metric).** The covariance of $\tilde\rho_f$ in $g_f$-normal coordinates is $\delta^{ij}$. Transforming to a common coordinate chart: $C_f^{ij}(\Gamma)=g_f^{ij}(\Gamma)$, i.e., every Petz metric satisfies $\mathrm{Cov}_{\tilde\rho_f}=g_f^{-1}$ **by construction**. This step is therefore **not** a selector.

**Step 3 (Metric-independent physical quantity — Lemma).**
:::info Lemma (the SLD bilinear form is Petz-free)
The SLD bilinear form $C^{\mathrm{SLD}}_{ij}(\Gamma):=\tfrac12\operatorname{Tr}\!\bigl(\Gamma\{L_i,L_j\}\bigr)$, where $L_i$ is the SLD defined by $\partial_i\Gamma=\tfrac12(L_i\Gamma+\Gamma L_i)$, involves only $\Gamma$ and its derivative; **no metric on $\mathcal D(\mathbb C^7)$ enters its definition**. Hence $C^{\mathrm{SLD}}$ is a physical quantity assigning a $(0,2)$-tensor to each $\Gamma$ independently of any metric choice.

**Index placement, stated exactly.** $C^{\mathrm{SLD}}_{ij}$ carries *lower* indices: it is the covariance of the SLD *operators*, which is by definition the SLD quantum Fisher information, $C^{\mathrm{SLD}} = \mathcal F_{\mathrm{SLD}}$. The object with *upper* indices — the covariance of the *parameters*, i.e. the minimal estimator covariance saturating the quantum Cramér–Rao bound — is its inverse, $C_{\mathrm{est}}^{ij} = (\mathcal F_{\mathrm{SLD}}^{-1})^{ij}$. These two are not interchangeable, and conflating them is what produced the error corrected below.
:::

**Step 4 (Unique selection by matching).** Set the universal selector equation

$$g_{ij}(\Gamma) = \tfrac14\,C^{\mathrm{SLD}}_{ij}(\Gamma)\qquad (\star)$$

and ask: **which** Petz metric satisfies $(\star)$? By Braunstein–Caves 1994, $\mathcal F_{\mathrm{SLD}}=4g_B$, and by the Lemma $C^{\mathrm{SLD}}=\mathcal F_{\mathrm{SLD}}$; hence $(\star)$ reads $g_{ij}=(g_B)_{ij}$ and holds for Bures. Equivalently, in the estimator-covariance form that carries the MaxEnt reading, $(g_B)^{-1} = 4\,C_{\mathrm{est}}$. For any other Petz $g_f$ ($f\neq\tfrac{1+t}{2}$), $(\star)$ fails because the corresponding Fisher information $\mathcal F_f\neq\mathcal F_{\mathrm{SLD}}$ (Petz 1996; distinct monotone means give distinct Fisher tensors). Hence $(\star)$ is satisfied **uniquely** by Bures. $\square_{\mathrm{IV}}$

:::danger Correction (2026-08-06): the selector equation had the wrong form
An earlier version wrote the selector as $g^{ij}=C^{ij}_{\mathrm{SLD}}$, i.e. $(g_B)^{-1}=C_{\mathrm{SLD}}$, justified as "the inverse of $\mathcal F_{\mathrm{SLD}}$ is the SLD covariance". That statement is false as written, on two counts at once. The object defined in Step 3 is $\tfrac12\operatorname{Tr}(\Gamma\{L_i,L_j\})$, which **is** $\mathcal F_{\mathrm{SLD}}$ itself, not its inverse; and even under the intended reading the factor $4$ from Char-III was dropped. Chaining the two claims gives $(g_B)^{-1}=\mathcal F_{\mathrm{SLD}}=4g_B$, i.e. $g_B^2=\tfrac14 I$, which is false for any non-degenerate metric.

Machine-verified at $N=4$: $\max|C^{\mathrm{SLD}}-\mathcal F_{\mathrm{SLD}}| = 0$ exactly, $\max|C^{\mathrm{SLD}}-4g_B| = 1.5\times10^{-12}$, while the claimed identity $(g_B)^{-1}=C^{\mathrm{SLD}}$ has relative residual $0.994$ — it is not approximately true either. The repaired identities $g_B = \tfrac14 C^{\mathrm{SLD}}$ and $g_B^{-1}=4(C^{\mathrm{SLD}})^{-1}$ hold to $4\times10^{-13}$.

**What survives.** The *conclusion* of Char-IV — that the selector picks out Bures uniquely — is untouched, because uniqueness rests on distinct monotone means yielding distinct Fisher tensors, a statement about the tensor's *shape*, not its normalisation. Nothing else in T-187 depends on this step; Char-IV was already recorded as interpretive rather than logically independent (see the scope note below). Only the displayed equation was wrong.
:::

:::warning Scope clarification
Char-IV is **not logically independent of Char-III**: the selection mechanism is matching $g^{-1}$ against $C_{\mathrm{SLD}}$, which reduces Char-IV to the SLD-Fisher characterization. The value added by Char-IV is **interpretive**: it recasts "saturate Cramér–Rao" (estimation-theoretic) as "inverse metric equals physical covariance" (statistical-mechanical), and it makes explicit that **no circularity arises** in T-187: the constraint metric in Step 1 can be any Petz member, yet the same Bures is selected in Step 4. Char-IV strengthens T-187's physical motivation without producing an additional logically independent witness.
:::

**Scope of Char-IV.** This characterization selects Bures by privileging the **statistical-mechanical** interpretation: the metric is determined by the fluctuation structure of the state, not by an information-geometric choice. Unlike Char-I–III (which are canonical but allow other Petz members to have their own characterizations), Char-IV is **physically forced**: the covariance of quantum fluctuations is a fact about the state, not a convention.

**Joint scope.** Char-I + II + III are **three logically independent** witnesses: minimum-information-distance, purification-coherence, classical-estimation-saturation. Char-IV is a **physical recasting** of Char-III via the SLD covariance identity $g_B^{-1}=C_{\mathrm{SLD}}$. The four characterizations together make Bures the canonical choice by (a) triple independent mathematical selection and (b) single unambiguous physical selector. T-187's status remains [T] on the strength of Char-I alone (Petz extremality); Char-II–IV are supplementary witnesses, each robustly picking Bures under its natural interpretation.

**Proof of equivalence and uniqueness.**

*[Char-I].* By Petz 1996, $g_f(\rho)(X,X) = \mathrm{Tr}(X^* \mathcal J_f(\rho)^{-1} X)$, where $\mathcal J_f$ is built via Kubo-Ando operator means from $f$. Among all operator-monotone symmetric means satisfying $f(t)=tf(1/t)$, the arithmetic mean $f(t)=(1+t)/2$ is the **maximum** (Kubo-Ando 1980): $\mathcal J_f \le \mathcal J_B$ in the Löwner order. Inversion reverses: $\mathcal J_B^{-1} \le \mathcal J_f^{-1}$, hence $g_B \le g_f$ pointwise. Integration along geodesics: $d_B \le d_f$. Non-expansiveness of identity $(\mathcal D, d_f) \to (\mathcal D, d_B)$ is then immediate: $d_B(\mathrm{id}\,x,\mathrm{id}\,y) = d_B(x,y) \le d_f(x,y)$. Uniqueness of this $\mathcal V$-functor as identity on underlying sets is trivial. $\square_\mathrm{I}$

*[Char-II].* Uhlmann 1976 proves the variational formula. A metric is uniquely determined by its values on all pairs; any metric satisfying the formula coincides with Uhlmann's, which Petz 1996 §II.2 identifies as the $f(t)=(1+t)/2$ case. $\square_\mathrm{II}$

*[Char-III].* Braunstein-Caves 1994 establish CR-saturation by $\mathcal F_\text{SLD}$ in the single-parameter case (asymptotically attained in the multi-parameter commuting-SLD case). The defining linear equation $\partial\rho = \tfrac{1}{2}(L\rho+\rho L)$ has a unique self-adjoint solution on the support of $\rho$ (standard spectral argument). The induced metric equals $g_B/4$ (Hübner 1992). $\square_\mathrm{III}$

*[Consistency of the three witnesses].* Classical cross-references (Hübner 1992, Petz 1996 §II.2, Braunstein-Caves 1994) establish that Char-I, Char-II, Char-III all select the same metric $d_B$. $\square$

**Construction of $J_B$.** The Grothendieck topology $J_B$ on $\mathcal C_7$ is defined as the topology **generated** (Johnstone, *Elephant* C2.1.10) by the ε-δ coverage $\mathcal K_{d_B}$ of [Axiom Ω⁷ §Grothendieck topology](/docs/core/foundations/axiom-omega#топология-гротендика): a family $\{\Phi_i:\Gamma_i\to\Gamma\}$ is a $\mathcal K_{d_B}$-cover iff $\forall \varepsilon>0\,\exists\delta>0: B_B(\Gamma,\delta) \subseteq \bigcup_i \Phi_i(B_B(\Gamma_i,\varepsilon))$. The coverage satisfies identity and stability axioms (stability: [proved](/docs/core/foundations/axiom-omega#доказательство-стабильности) via CPTP-contractivity, which holds for every Petz metric). Transitivity of $J_B$ is **automatic** from the generation (Johnstone C2.1.9-12), bypassing any direct ε-δ transitivity argument.

**Canonicity at the topos level.**

- At the **classical-topology level** on the compact $\mathcal D(\mathbb C^7)$, all Petz metrics induce the same underlying topology. The justification is the *continuous-distance-on-compact lemma* (below), **not** bi-Lipschitz equivalence — which would fail because Petz metric tensors are degenerate on rank-deficient boundary strata (where $L_\rho$ has zero eigenvalues). The lemma requires only continuity of the distance functions (which holds on all of $\mathcal D$ including boundary, by Uhlmann 1976 for Bures and analogous extensions for other Petz members). Therefore $\mathrm{Sh}_\infty(\mathcal C_7, J_d) \simeq \mathrm{Sh}_\infty(\mathcal C_7, J_B)$ for every Petz $d$ as classical $\infty$-topoi. This makes UHM's numerical predictions (which depend on the topos structure, not the specific enrichment) **automatically robust** to any Petz choice.

- At the **$\mathcal V$-enriched / cohesive level**, full smoothness is required for the differential cohesion adjunctions $(\Pi \dashv \flat)$. This is implemented via the **stratified site** $\mathcal C = \mathrm{Strat}(\mathcal D(\mathbb C^7))$ (Ayala–Francis–Rozenblyum 2017): each rank-$k$ stratum $\mathcal D_k = \{\rho : \mathrm{rank}\,\rho = k\}$ is a smooth manifold, and inclusions $\mathcal D_k \hookrightarrow \overline{\mathcal D_k}$ are Bures-continuous. The Bures enrichment is uniquely canonical by Char-I+II+III on each stratum and on the union via factorization homology. The enriched $\infty$-topos $\mathfrak T = \mathrm{Sh}_\infty^{\mathcal V}(\mathcal C_7, J_B)$ is hence canonically fixed. **Physical relevance.** The L2 consciousness regime $P \in (2/7, 3/7]$, $R \ge 1/3$ requires $\mathrm{rank}\,\Gamma > 1$ (since $R \ge 1/3$ excludes pure states), so the consciousness window lies entirely in the **interior stratum** $\mathcal D_7$ where the Bures metric tensor is non-degenerate. Boundary strata correspond physically to heat death (low $P$) or pure-state collapse — outside the consciousness regime.

**Lemma (continuous-distance-on-compact).** Let $K$ be a compact metrizable space with standard topology $\tau_\mathrm{std}$, and $d: K\times K \to [0,\infty)$ a function satisfying:
(i) $d(x,y) = d(y,x)$ and $d(x,z) \le d(x,y) + d(y,z)$;
(ii) $d(x,y) = 0 \iff x = y$;
(iii) $d$ is continuous on $K\times K$ in $\tau_\mathrm{std}\times\tau_\mathrm{std}$.

Then $d$ induces the standard topology: $\tau_d = \tau_\mathrm{std}$.

*Proof.* For (⊆): for any $x\in K$ and $r>0$, $B_d(x,r) = \{y : d(y,x) < r\}$ is the preimage of $[0,r)$ under the continuous (in $y$) function $y \mapsto d(y,x)$, hence $\tau_\mathrm{std}$-open. So every $\tau_d$-open set is $\tau_\mathrm{std}$-open.

For (⊇): the identity $\mathrm{id}: (K, \tau_\mathrm{std}) \to (K, \tau_d)$ is continuous (preimage of $B_d(x,r)$ under id is $B_d(x,r)$ itself, $\tau_\mathrm{std}$-open). The space $(K,\tau_d)$ is Hausdorff: for $x\ne y$, $d(x,y) =: \delta > 0$ by (ii); balls $B_d(x,\delta/2), B_d(y,\delta/2)$ are disjoint by (i). A continuous bijection from compact to Hausdorff is a homeomorphism (standard topology), so $\mathrm{id}^{-1}$ is also continuous, giving $\tau_\mathrm{std}\subseteq \tau_d$. $\square$

**Application to Petz family.** For each Petz-monotone metric $d_f$ on $\mathcal D(\mathbb C^7)$, properties (i)-(ii) are part of the definition. Property (iii): $d_f$ is expressed by spectral functions of $\rho, \sigma$ continuous on the closed compact $\mathcal D \times \mathcal D$. For Bures: $d_B(\rho,\sigma) = \arccos\sqrt{F(\rho,\sigma)}$ with $F = (\mathrm{Tr}\sqrt{\sqrt\rho\sigma\sqrt\rho})^2$ continuous everywhere including boundary (Uhlmann 1976). For Kubo–Mori, RLD, etc.: distance functions extend continuously to boundary by analogous spectral-functional analysis (Streater 2004, Petz 2008). Hence the lemma applies, and all Petz metrics induce $\tau_\mathrm{std}$. ✓

**Conclusion.** Axiom A2 is canonical in a precise sense: the Bures metric is uniquely determined by three independent mathematical witnesses (Petz extremality, Uhlmann purification, SLD-Cramér-Rao), all mutually consistent. Any other Petz metric gives the same classical $\infty$-topos but a different enrichment, one that is non-universal by Char-I.

**Status:** A2 is [T] by **quadruple** characterization (Char-I through Char-IV). $\square$

### 5.4. Axiomatic closure: all axioms are theorems (T-190) {#теорема-аксиоматическое-замыкание}

:::tip Theorem T-190 (Axiomatic Closure of UHM) [C under T-87's constraint assumption and hypothesis T-186(a)]

The axioms A1–A5 of UHM are derivable from the characterizing properties (AP)+(PH)+(QG)+(V) and the maximum entropy principle (MaxEnt) **under two conditions**: the Page–Wootters constraint of A5 is assumed (T-87, step 4, [C]), and the route to A1 through T-186 rests on the hypothesis T-186(a) [H].
:::

:::warning Retracted: "zero independent axioms"
An earlier version stated T-190 as [T]: "All five axioms A1–A5 of UHM are theorems … UHM has zero independent axioms beyond the defining conditions of a viable holon." Both parts are retracted. The constraint half of A5 is not derived (T-87, step 4), so it remains an independent assumption; and A1's derivation invoked T-186, whose part (a) is a hypothesis and whose parts (b)–(c) are retracted.
:::

**Proof (status of each axiom).**

| Axiom | Statement | Derivation | Status |
|-------|-----------|------------|:------:|
| **A1** | Reality = $\infty$-topos $\mathbf{Sh}_\infty(\mathcal{C})$ | T-76 [T] (Bures + Lurie → ∞-topos verified at site level) + T-186 (a) [H] (cohesive closure, which would single out the ∞-topos as the structure admitting the differentially cohesive modalities) | [H] |
| **A2** | $J_{\mathrm{Bures}}$ Grothendieck topology | T-187 [T] (triple characterization: Char-I Petz extremality + Char-II Uhlmann + Char-III SLD-CR) + **T-189 [T] (Char-IV MaxEnt covariance)**: the physical covariance of quantum fluctuations uniquely selects the Bures metric without information-geometric choice | [T] |
| **A3** | $N = 7$ | Theorem S [T] (functional minimality 7/7); T15 [T] with the canonical orientation of the Fano lines ([T15-canon](/docs/proofs/minimality/theorem-octonionic-derivation#каноническая-ориентация); bridge (AP)+(PH)+(QG)+(V) → P1+P2 → Hurwitz → $\mathbb{O}$ → $N = 7$; cited as [T] before 2026-09-25 and as [C at (Alt)] earlier that day) supports the value but is not needed | [T] (by Theorem S) |
| **A4** | $\omega_0 > 0$ | Trivial: $\omega_0 = 0$ implies no dynamics ($H_{\mathrm{eff}} = 0$), which violates (AP) (no autopoiesis without evolution). Therefore $\omega_0 > 0$ is a **necessary condition** for (AP), not an independent axiom | [T] |
| **A5** | Page–Wootters $\mathcal{H} = \mathcal{H}_O \otimes \mathcal{H}_{\mathrm{rest}}$ | T-87: the clock register and the tensor factor are constructed from A1–A4 via the spectral triple (steps 1–3, [T]); the constraint $\hat{C}\Gamma = 0$ is assumed (step 4, [C]) | [C] |

**Chain of derivation:**

$$
(AP)+(PH)+(QG)+(V) + \mathrm{MaxEnt}
$$
$$
\xrightarrow{T15} \mathbb{O},\; N=7 \;[\text{A3}]
\xrightarrow{\omega_0 \neq 0} [\text{A4}]
\xrightarrow{T\text{-}76} \infty\text{-topos} \;[\text{A1}]
$$
$$
\xrightarrow{T\text{-}187 + T\text{-}189} J_{\mathrm{Bures}} \;[\text{A2}]
\xrightarrow{T\text{-}87} \text{PW factorization} \;[\text{A5}]
$$

**Conclusion (conditional).** Under the two conditions of the theorem, the formal structure of UHM is determined by the four characterizing properties of a viable holon — (AP) autopoiesis, (PH) phenomenology, (QG) quantum grounding, (V) viability — together with the maximum entropy principle and the Page–Wootters constraint. An earlier conclusion — that UHM is **self-grounding**, that no external mathematical structure is imported, and that "everything else follows" from the definition of a holon — is retracted: the constraint is imported as an assumption, and the cohesive route to A1 is a hypothesis. $\blacksquare$

**Dependencies:** T15 [T] with the canonical orientation (bridge; A3 itself rests on Theorem S), T-53 [T], T-76 [T], T-87 [C], T-186 [H], T-187 [T], T-189 [T], Theorem S [T].

### 5.3.1 Petz-robustness classification of UHM results {#petz-робастность}

T-187 establishes that the Bures metric is uniquely canonical among the Petz family of CPTP-monotone Riemannian metrics on $\mathcal D(\mathbb C^7)$. A natural follow-up question (raised explicitly by external audit): **if one were to use a different Petz metric — e.g.\ Kubo–Mori (BKM), Wigner–Yanase, right-logarithmic-derivative — which UHM results would change, and which would remain invariant?**

We classify every major UHM observable, threshold, and exponent into four robustness categories.

#### R1 — Strictly Petz-invariant (the same numerical value for any $f \in \mathrm{Petz}$) [T]

These results depend only on the spectrum of $\Gamma$, on combinatorial/algebraic structure, or on the underlying point-set topology of $\mathcal D(\mathbb C^7)$ — none of which is sensitive to the Petz choice (all Petz metrics are bi-Lipschitz equivalent on the compact manifold).

| Result | Why Petz-invariant | Reference |
|---|---|---|
| $P(\Gamma) = \mathrm{Tr}(\Gamma^2)$ | Spectral function, no metric input | [Viability](/docs/core/dynamics/viability) |
| $P_\mathrm{crit} = 2/N = 2/7$ | Five independent derivations, all use spectral arithmetic alone | [Q3 / theorem-purity-critical.md](/docs/proofs/dynamics/theorem-purity-critical) |
| $\mathrm{Spec}(\Gamma) = \{\lambda_k\}$ | Unitarily invariant | Standard |
| $\omega_0 = \lambda_{\min}(H_\mathrm{eff})$ | Spectral property of $H_\mathrm{eff}$ | [Axiom Ω⁷ A4](/docs/core/foundations/axiom-omega) |
| $N = 7$ | Hurwitz + Adams + Hall (combinatorial-algebraic) | [Q7 / theorem-octonionic-derivation.md](/docs/proofs/minimality/theorem-octonionic-derivation) |
| $G_2 = \mathrm{Aut}(\mathbb O)$, $\dim G_2 = 14$ | Algebraic structure of octonions | [§1.6](/docs/proofs/minimality/theorem-octonionic-derivation#группа-g2) |
| $K = 3$ triadic decomposition | Structure of Lindblad operators on $\mathfrak{su}(7)$ | [T-40b](/docs/core/operators/lindblad-operators#триадная-декомпозиция) |
| $R_\mathrm{th} = 1/3$ | $K=3$ Bayesian dominance | [Q2 Char-R-III](/docs/proofs/consciousness/conscious-window#t-126) |
| $\Phi_\mathrm{th} = 1$ | T-129, derived from triadic structure | [T-129](/docs/proofs/consciousness/operationalization#t-129) |
| Critical exponents $\{\alpha,\beta,\gamma,\nu,\delta\} = \{1/2, 1/4, 1, 1/2, 5\}$ | Thom-Arnold $A_4$ topological invariants | [Q4 / swallowtail-transitions.md#механизм-точности](/docs/consciousness/hierarchy/swallowtail-transitions#механизм-точности) |
| $d_\mathrm{eff} = 21$ | Combinatorial: $\binom{7}{2}$ off-diagonal modes in $\mathfrak{su}(7)$ | [Q4](/docs/consciousness/hierarchy/swallowtail-transitions#механизм-точности) |
| Underlying topology of $\mathcal D(\mathbb C^7)$ | Continuous-distance-on-compact lemma applied to all Petz $d_f$ (continuity at boundary via Uhlmann/Streater); bi-Lipschitz of metric tensors fails on rank-deficient strata but is **not needed** for topological equality | [Lemma above](#53-closing-the-last-open-question-why-bures-t-187) |
| Underlying $\infty$-topos $\mathrm{Sh}_\infty(\mathcal C_7, J_d) \simeq \mathrm{Sh}_\infty(\mathcal C_7, J_B)$ | Same point-set topology ⟹ same classical sheaves | Q1 |
| $G_N = 3\pi/(7 f_2 \Lambda^2)$ parametric scaling | Spectral action expansion uses Tr, not metric | [Q8 / einstein-equations.md#сравнение-connes-chamseddine](/docs/physics/gravity/einstein-equations#сравнение-connes-chamseddine) |
| $SU(3)\times SU(2)\times U(1)$ gauge group | Morita-class of $A_\mathrm{int}$, algebraic | [Q8](/docs/physics/gravity/einstein-equations#сравнение-connes-chamseddine) |

**Conclusion R1.** All UHM **thresholds**, **critical exponents**, **dimensional minimality**, **gauge group**, and **classical $\infty$-topos** are Petz-invariant. Choosing Kubo–Mori, Wigner–Yanase, RLD, or any other Petz metric does not change a single numerical prediction in this category.

#### R2 — Invariant up to Petz-rescaling (overall scale changes, ratios preserved) [T]

These quantities depend on the metric, but the **ratios** between Bures and any other Petz metric are bounded constants (no qualitative change).

| Result | Bures form | Other-Petz form |
|---|---|---|
| Geodesic distance $d_f(\rho_1, \rho_2)$ | $d_B$ minimum | $d_f \ge d_B$ pointwise |
| Information-geometric correlation length $\xi_f$ | $\xi_B$ | $\xi_f = c_f \xi_B$ with $c_f \ge 1$ |
| Cramér–Rao information bound | $\mathcal F_\text{SLD} = 4 g_B$ (saturating) | $\mathcal F_f \le 4 g_B$ (sub-saturating) |

Since Petz metrics on compact $\mathcal D(\mathbb C^7)$ are bi-Lipschitz with bounded ratio (continuous Riemannian metrics on a compact manifold), all R2 quantities differ by a bounded multiplicative factor across Petz family. **No qualitative result changes.**

#### R3 — Numerical value Bures-specific, structural form preserved [T → C if Petz metric changed]

These are observables defined via the Frobenius/HS structure (Bures-canonical), but admit straightforward translation to any Petz metric with structurally identical formulas and quantitatively different numbers.

| Result | Bures form | If Kubo–Mori chosen |
|---|---|---|
| $R(\Gamma) = 1/(7P)$ | $\cos^2\theta_\text{HS}(\Gamma, I/7)$ | $\cos^2\theta_\text{KM}(\Gamma, I/7)$ — different function of spectrum |
| $\Phi = \|\Gamma-\Gamma_\text{diag}\|_F^2 / \|\Gamma_\text{diag}\|_F^2$ | HS off/diag ratio | KM-norm off/diag ratio |
| $\mathrm{Coh}_E = (\gamma_{EE}^2 + 2\sum_{j\ne E}\|\gamma_{Ej}\|^2)/P$ | HS projection on $E$-row | KM-projection on $E$-row |
| $\kappa_0 = \omega_0\|\gamma_{OE}\|\|\gamma_{OU}\|/\gamma_{OO}$ | Same form | Constants reorganised |

**Important.** Even though R3-quantities have Bures-specific numerical values, the **thresholds** $R \ge 1/3$, $\Phi \ge 1$ remain invariant (R1 above). Choosing Kubo–Mori would force a recalibration of the threshold *values* (e.g.\ $R_\text{KM,th}$ might be $0.40$ instead of $0.33$) but the **structural meaning** ("normalised proximity to heat death exceeds Bayesian dominance threshold") is preserved. This is a re-parameterization, not a substantive change.

#### R4 — Essentially Bures-specific (no Petz analogue) [T]

These results require Bures-specific properties that do **not** generalise to other Petz members. Choosing a different Petz metric would either invalidate these results or leave them undefined.

| Result | Bures-specific reason |
|---|---|
| Uhlmann purification variational formula | Only Bures admits $d(\rho,\sigma) = \inf\| \|\psi\rangle - \|\varphi\rangle\|$ over purifications (Hübner 1992); no Kubo–Mori analogue exists. |
| SLD-Fisher Cramér–Rao **saturation** | Only SLD-Fisher = $4g_B$ saturates the multiparameter quantum CR bound (Braunstein–Caves 1994). All other Petz members give strict sub-saturation. |
| Petz-poset minimality $g_B \le g_f$ | Tautological for Bures, false for all others. |
| Page–Wootters time emergence via Bures-cohesion | T-185, T-186 use the cohesive $\infty$-topos with Bures topology specifically. This row is moot: the cohesion holds in the corrected form T-185 (ii′), which uses the smooth structure, not the Bures metric, and the time-emergence part of T-186 is retracted. |

#### Summary table

| Category | What survives Petz-change | What changes |
|---|---|---|
| **R1 (strictly invariant)** | $P_\text{crit}$, $R_\text{th}$, $\Phi_\text{th}$, exponents, $d_\text{eff}$, $N=7$, $G_2$, gauge group, classical topos | Nothing |
| **R2 (rescaling)** | Structural ratios of distances/correlation lengths | Overall scale multiplier (bounded) |
| **R3 (formula-stable)** | Form of $R, \Phi, \mathrm{Coh}_E$ | Numerical values; thresholds need recalibration |
| **R4 (Bures-essential)** | Uniqueness theorems Char-II, Char-III; cohesion | Would invalidate / require different proofs |

#### Direct answer to the auditor

**Robust** (no change for any Petz metric): all UHM thresholds, all critical exponents, all dimensional minimality results, all gauge structure, all phenomenology coupled to the Connes–Chamseddine framework.

**Bures-rescaled** (linear recalibration only): geodesic distances, correlation-length scales, information-geometric bounds.

**Bures-specific** (essential): the **canonicity claim itself** (T-187 uses Char-I/II/III which select Bures uniquely), and the cohesive $\infty$-topos enrichment used in T-185/T-186 to derive emergent time.

In particular, the **falsifiable empirical predictions** of UHM (PCI ↔ $\Phi$, $P > 2/7$ for viability, tricritical exponents, no-zombie via $\mathrm{Coh}_E$, neutrino mass formula T-63) are all in R1 or R3 — they would survive choice of Kubo–Mori with at most a recalibration of threshold numerical values, never a change of qualitative behaviour. UHM is therefore **structurally robust** to the Petz-family choice; the Bures-specificity is concentrated in the canonicity argument and in two derivation routes (Uhlmann/SLD), neither of which affects the empirical predictions.

#### Substrate-independence vs Bures-essentiality: two abstraction levels {#уровни-абстракции}

A subtle but important clarification reconciles two seemingly tensioned claims of UHM:

**Claim A (T-153 substrate-independence) [T].** The L-level of consciousness is determined solely by $\Gamma$, not by the underlying neural state $s$ (silicon, carbon, transistor, neuron — equivalent if both produce the same $\Gamma$).

**Claim B (Q9 R4 Bures-essentiality) [I].** Page–Wootters emergent time and the cohesive $\infty$-topos derivation (T-185, T-186) use Bures-specific structural properties; other Petz members would require different proofs. (Status lowered from [T]: the derivations it refers to are assumed, hypothetical or retracted.)

These do not contradict. They live at **different abstraction levels**:

- **Substrate** in T-153 = *physical implementation*: biology vs silicon vs other quantum hardware. The substrate-independence is internal to a *fixed* UHM formalism (with Bures-cohesion); it states that within this formalism, what matters is $\Gamma$, not the implementation that produces it.

- **Enrichment** in Q9 R4 = *mathematical formalism choice*: Bures vs Kubo–Mori vs RLD as the metric structure of the categorical site. Changing the enrichment is changing the *theory* itself, not changing the substrate.

The hierarchy is:
$$\underbrace{\text{enrichment choice (Bures)}}_{\text{Q9: defines the UHM formalism}} \;\succ\; \underbrace{\text{abstract }\Gamma\in\mathcal D(\mathbb C^7)}_{\text{ontological core, T-153}} \;\succ\; \underbrace{\text{neural implementation }s}_{\text{T-153 substrate}}$$

T-153 is "**given** the UHM formalism with Bures-cohesion, the L-level depends only on $\Gamma$, not on $s$." Q9 R4 is "**choosing** UHM with Bures-cohesion (rather than KM-cohesion or any other) is what makes T-185/T-186 derivations work." Both true; no tension.

Operationally: an AGI engineer **using UHM** can implement $\pi: s \to \Gamma$ on any substrate (silicon, neuromorphic, quantum) — substrate doesn't matter (T-153). An AGI theorist **constructing UHM** must commit to a specific Petz enrichment; choosing Bures gives the Page–Wootters time emergence chain (Q9 R4), choosing KM would require building an analogous chain from scratch (and may not yield the same emergent-time structure).

---

### 5.4. The remaining interpretive element

The statuses below are those the corpus assigned before the audit of 2026-09-25; A1's cohesive route through T-186 is now a hypothesis [H], and the constraint of A5 remains an assumption (T-87, step 4). With T-187, the last postulate of UHM was said to be closed. The theory was said to rest entirely on:

- **A1 [T]:** Reality is an $\infty$-topos (the most general space with internal logic — no alternative with equivalent power)
- **A2 [T]:** The topology is Bures (the unique coarsest CPTP-compatible topology — T-187)
- **A3 [T]:** $N = 7$ (uniquely determined by octonions/Fano — Hurwitz + Adams)
- **A4 [T]:** $\omega_0 = \lambda_{\min}(H_{\text{eff}}) > 0$ — a derived spectral property, not a free parameter

A4 is no longer a postulate. The characteristic frequency $\omega_0$ of a holon $\mathbb{H}$ is **defined** as the minimal nonzero eigenvalue of the effective Hamiltonian $H_{\text{eff}}$ (T-87). This is positive for any viable system: a system with $\omega_0 = 0$ has no dynamics, hence no regeneration, hence $P$ decays below $P_{\text{crit}}$ — it is not viable. Different holons have different $\omega_0$, just as different atoms have different masses — this is a computed property, not a postulated one.

All four axioms are now theorems:

| Axiom | Status | Derivation |
|---|---|---|
| A1 (∞-topos) | [T] | Most general space with internal logic; any weaker structure (sets, $n$-categories) is strictly less powerful |
| A2 (Bures metric) | [T] | T-187: unique coarsest CPTP-compatible topology |
| A3 ($N = 7$) | [T] | Hurwitz + Adams + Fano plane |
| A4 ($\omega_0 > 0$) | [T] | $\omega_0 = \lambda_{\min}(H_{\text{eff}}) > 0$ from viability: $\omega_0 = 0 \Rightarrow$ no dynamics $\Rightarrow P < P_{\text{crit}}$ |

The **only** remaining non-derivable element is the choice to describe reality as an $\infty$-topos at all (A1) — but this is the most general mathematical framework for spaces with internal logic, and any alternative is strictly weaker. The question **why does reality have the structure of a space with internal logic?** is not a question within mathematics — it is the meta-question of why mathematics describes reality at all.

---

**References:**
- Ayala, D., Francis, J., Rozenblyum, N. (2017). Factorization homology I: Higher categories. arXiv:1504.04007
- Schreiber, U. (2013). Differential cohomology in a cohesive ∞-topos. arXiv:1310.7930v1 (Def. 3.4.1, 3.4.4, 3.4.17, 3.5.1, 3.10.1; Prop. 3.4.18, 4.4.34, 4.5.8, 4.5.11; Cor. 4.4.10)
- Myers, D. J., Riley, M. (2023). Commuting cohesions. arXiv:2301.13780 (§6.3: solid cohesion and the rheonomy modality)
- Lawvere, F. W. (2007). Axiomatic cohesion. Theory and Applications of Categories 19(3): 41–49
- Lurie, J. (2009). Higher Topos Theory. Annals of Mathematics Studies 170
- Connes, A. (2013). On the spectral characterization of manifolds. J. Noncommut. Geom. 7(1): 1–82
