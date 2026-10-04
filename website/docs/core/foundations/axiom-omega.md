---
title: Axiom Ω⁷ and Its Typed Realization
sidebar_position: 1
description: Explicit assumptions, genuine sheaf site and categorical/numerical interfaces
---

# Axiom Ω⁷ and its typed realization

UHM postulates one structured ontology [P]/[I]. Its mathematical realization consists of states, processes, a sheaf semantics and specified dynamical/phenomenal bridges. Calling that structure one primitive does not erase its independent assumptions. This page and the [typed kernel](/docs/reference/mathematical-kernel) replace the former untyped derivations (2026-10-03).

## Explicit axiomatics {#аксиоматика}

| Input | Mathematical content | Status |
|---|---|---|
| A1: semantics | A sheaf $\infty$-topos over a specified site; canonical model $\mathcal E_N=\operatorname{Sh}_\infty(\operatorname{Open}(D_N,d_B))$ | Construction [D], existence [T], ontological identification [P]/[I] |
| A2: geometry | Chordal Bures distance on states; tensor on full-rank strata | Choice [P]; monotonicity under CPTP [T] |
| A3: frame | $\mathcal H=\mathbb C^7$ with semantic orthonormal frame A,S,D,L,E,O,U and specified octonionic structure | [P]/[D]; lower bounds conditional on their stated algebra/coding premises |
| A4: scale | A calibrated $\omega_0>0$; Hamiltonian and dissipative rates specified separately | [P]; not inferred from terminality or positivity of the Hamiltonian |
| A5: clock extension | A chosen extended tensor realization, clock readout and support constraint $\operatorname{supp}\rho\subseteq\ker\hat C$ | [P]/[D]; conditional Page–Wootters consequences |

Density matrices and linear CPTP processes are the chosen quantum formalism [D]/[P]. A self-model $M$, its anchor, state-dependent coefficients, preparation/environment, observation law and phenomenal identification are additional typed data. $(\Sigma_6)$, (MaxΦ), (Mod)/(Cl₀) and (P) retain their explicit bridge status. No equivalence of operational slogans with A1–A5 is inferred without these inputs and actual implication proofs.

## Structured primitive {#примитив}

A precise model is a record

$$
\mathfrak T=(\mathcal E_7,D_7,d_B,\text{frame},\mathcal L_0,M,a,\text{clock extension},\text{observation law}).
$$

Some fields may be fixed by definitions or conditional constructions; others remain free. A model record is one object with many fields. The claim that all physical and interior phenomena are interpretations of this record is the monist thesis [I], not a corollary of the terminal object.

## Sheaf semantics {#infty-структура}

<a id="источник-гомотопии"></a>

For each finite $N$, $D_N$ is the compact convex space of PSD trace-one matrices. Its Bures opens form a small poset site (after choosing universes). Sheaves of spaces on this site form an $\infty$-topos. Higher mapping spaces are available; they need not be nontrivial for every object. Ordinary representables on a 1-site are 0-truncated. Nontrivial experiential homotopy requires an explicitly constructed object and proof.

### Genuine Grothendieck topology {#топология-гротендика}

<a id="доказательство-стабильности"></a>

Objects are Bures-open $U\subseteq D_N$, arrows inclusions, and covers are unions $U=\bigcup_iU_i$. Base change is intersection, $V\cap U=\bigcup_i(V\cap U_i)$; composition of covers is union of unions. This proves the site axioms. CPTP continuity sends opens to opens by inverse image and induces a geometric morphism. The [kernel](/docs/reference/mathematical-kernel#bures-site) gives the complete interface.

The earlier small-ball image criterion on pointed CPTP arrows is withdrawn as a proved site construction [✗]. Image contractivity does not establish lifting or sieve stability. No equivalence between that channel site and the open site is assumed. A set of spectra is not a skeleton of *framed* states with their instruments: unitary equivalence of states need not preserve the semantic frame, and a skeleton retains transported morphisms rather than replacing them by spectral data alone.

### Interiority and truncation {#связь-с-интериорностью}

Postnikov truncation is a logical/homotopical operation. It is not the numerical purity or consciousness hierarchy. A Postnikov tower has an inverse limit; convergence is an extra completeness property. Finite dimension, finite time resolution and an $\infty$-topos do not force nonzero homotopy groups in arbitrarily high degrees. The [operational hierarchy](/docs/consciousness/hierarchy/interiority-hierarchy) states its distinct readout conditions.

## Internal logic {#внутренняя-логика}

The classifier $\Omega$ classifies subobjects. In the open-site model $\Omega(U)=\operatorname{Open}(U)$; global truth values are opens of $D_N$. The classifier object is not a Hilbert space, density matrix, Boolean algebra of seven projections or a clock register.

### Semantic frame and projective instrument {#атомы-классификатора}

<a id="решающий-фрагмент"></a>
<a id="необходимость-трёхуровневой-структуры"></a>
<a id="lk-из-omega"></a>

A chosen frame defines $P_i=|i\rangle\langle i|$, $\sum_iP_i=I$ and the pinching channel $\rho\mapsto\sum_iP_i\rho P_i$ [T]. The projectors and instrument are specified operator data [D]. The labels A–U give their semantic interpretation [I]. They are not forced by $\Omega$: sets $\{\rho:\rho_{ii}>0\}$ overlap on every full-rank state, so they are not disjoint atoms; connected $D_N$ has only two clopen sets. The former classifier-to-Lindblad derivation and the forced three-tier logic are withdrawn [✗]. A quantization/instrument-selection bridge would be required to derive operator data from a logical predicate.

### Temporal modality {#темпоральная-модальность}

A specified order-seven frame permutation gives an action of $\mathbb Z_7$, and therefore an autoequivalence on sheaf semantics when it preserves the chosen geometry. Iterating it is periodic. A continuous or aperiodic clock, an arrow of time and an irreversible semigroup require additional dynamical data. Neither $P_i\mapsto P_{i+1}$ nor an internal modality alone derives them.

### Gap and holonomy {#gap-голономия}

Pairwise $|\sin\arg\rho_{ij}|$ is a statistic in a native semantic frame [D]/[I]. It changes under general rephasing. Triangle products $\rho_{ij}\rho_{jk}\rho_{ki}$ have rephasing-invariant phases when their entries are nonzero [T]. Identifying those phases with holonomy of a geometric connection requires a specified bundle, connection and loops; a connection is not supplied merely by the existence of a topos. Zero coherences have no defined phase.

## Informational distinguishability {#пир-как-теорема}

Distinct density matrices have positive Bures distance [T]. PID is the chosen ontological reading of operational distinctions [D]/[I]. It does not force a survival cut: all states other than $I/N$ are distinguishable from it, even below $2/N$.

### Thresholds {#пороги-различимости}

Structural majority defines $P>2/7$; $R=1/(7P)$ with a selected access cut $R\ge1/3$ defines the upper boundary $P\le3/7$. Coherent majority defines $\Phi\ge1$. Their exact implications are in [critical purity](/docs/proofs/dynamics/theorem-purity-critical) and [the kernel](/docs/reference/mathematical-kernel#thresholds). Biological viability and phenomenal identification are separate hypotheses. A Bayesian posterior requires a likelihood and priors; it is not defined by assigning that name to $R$.

## Five interface properties

### Property 1: finite realization {#свойство-1}

The operational single-holon state is in $D_7$. Composite states lie in $D_{7^k}$; a selected clock realization may lie in $D_{42}$. These are different spaces with explicitly specified maps, not categorically equivalent solely because a section–retraction exists.

### Property 2: clock constraint {#свойство-2}

<a id="pw-constraint"></a>

$\hat C\rho=0$ means $\operatorname{supp}\rho\subseteq\ker\hat C$ for the declared Hermitian constraint. It is an extra restriction, not a consequence of an unconstrained tensor product. Conditional states require normalization and exist only at readouts with nonzero probability. A literal E-reduction requires an actual tensor factor or declared contraction, not a one-dimensional basis axis.

### Property 3: terminal object {#свойство-3}

The terminal object $1_{\mathcal E}$ of sheaf semantics has contractible $\operatorname{Map}(X,1_{\mathcal E})$ for each $X$ [T]. Its global sections form a point. This does not produce a density matrix, attractor, thermodynamic state or convergence trajectory. In the process category the terminal object is the one-dimensional discarding target; $I/7$ is not terminal (identity and reset are distinct endomorphisms).

### Property 4: support self-mirror {#свойство-4}

The logical mirror is the image reflector in a slice:

$$
\operatorname{im}_G\dashv i_G:\operatorname{Sub}_{\mathcal E}(G)\hookrightarrow\mathcal E_{/G}.
$$

The old inclusion into the ambient topos for every $G$ would force every $G$ terminal and is withdrawn [✗]. A numerical $M:D_7\to D_7$ is independent data. See [φ formalization](/docs/proofs/categorical/formalization-phi#категориальное-определение-φ).

### Property 5: stratification {#свойство-5}

Rank or spectral-multiplicity strata can be specified on $D_N$; operational capability regions can also be defined by inequalities. Their dimensions, topology, invariance and transition dynamics require separate proofs. A decomposition into strata does not force trajectories toward the terminal object or dimensional collapse.

## Hamiltonian and scale {#гамильтониан-взаимодействия}

<a id="калибровка"></a>

A Hermitian $H$ defines the commutator dynamics. Its absolute energy zero is arbitrary: $H$ and $H+cI$ give the same commutator. Hence $\min\operatorname{spec}H$ is not a physical frequency. Calibrate $\omega_0$ or choose a specified nonzero Bohr gap $(E_i-E_j)/\hbar$. Regeneration and dissipative rates are calibrated independently; their positivity or magnitude does not follow from adjunction.

## Base space and cohomology {#базовое-пространство}

<a id="когомологический-монизм"></a>

The open-site realization has base space $D_N$, which is convex and contractible by $\rho\mapsto(1-t)\rho+tI/N$ [T]. Its constant-coefficient positive-degree cohomology vanishes. This calculation is independent of the terminal object of its sheaf topos. It does not imply vanishing for arbitrary coefficient sheaves or gluing of every self-model.

A category with a terminal object has contractible nerve [T], but a topological space is not recovered from the nerve of its poset of *all* opens: that poset always has a terminal open, even for a circle. The relevant sheaf shape/Čech descent carries the space's topology. The former inference from topos terminality to a contractible indexing nerve or universal local-to-global gluing is withdrawn [✗]. Cohomology of a chosen contractible model does not establish ontological monism.

## Time and geometry {#эмерджентное-время}

<a id="эмерджентная-метрика"></a>

For a specified clock extension, constraint and readout, Page–Wootters conditional evolution is a conditional construction. A spectral triple, its Dirac operator, metric extraction and any physical spacetime interpretation require their own assumptions. Neither a seven-tick register nor an arbitrary finite spectral triple proves physical 3+1 Lorentz geometry; the matter/spacetime bridges remain in the [premise register](/docs/reference/premises).

## Genesis and viable dynamics {#genesis-protocol}

<a id="теорема-kappa-bootstrap-bound"></a>

If the autonomous regeneration gate vanishes at $I/7$ and the linear part is unital, $I/7$ is stationary. Genesis then requires external preparation or a non-unital environment [T]. No positive bootstrap rate is supplied by the logical reflector. A source of free energy and an explicit dynamical mechanism are additional data. Non-unital self-model anchors have viable sinks only in their proved parameter regimes; a static purity cut is not a stability proof.

## Choice and ontology {#свобода-воли}

A Hessian kernel counts infinitesimal flat directions at a specified stationary point. A nonzero kernel does not by itself give a family of distinct minima or agency (higher-order terms may lift it). Its reading as freedom or will is [I]. The availability of category-theoretic arrows is not evidence of physical choice.

## Consistency

The individual mathematical components above exist. This provides models of stated constructions, not a proof that every earlier assertion of the corpus follows from five axioms or that the physical interpretation is true. Joint consistency of additional constraints must be exhibited by a model; no metatheoretic completeness theorem for reality is asserted.

Primary categorical and quantum sources, exact interface statements and regression checks are collected in the [typed kernel](/docs/reference/mathematical-kernel#sources). This is the canonical reading of Ω⁷ for subsequent chapters.

## Historical anchors

<a id="иерархия-lk"></a>
<a id="теорема-алгебра-динамика-ошибка"></a>
<a id="a5-из-спектральной-тройки"></a>
<a id="теорема-pw-suzuki-trotter"></a>
<a id="октонионная-структура"></a>
<a id="структура"></a>
<a id="иерархия-зависимостей"></a>

These anchors refer to the typed definitions above. Earlier deductions conflating topoi, channels, state matrices and trajectories are withdrawn.
