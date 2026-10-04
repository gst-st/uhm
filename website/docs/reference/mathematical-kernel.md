---
title: Typed Mathematical Kernel
sidebar_position: 2
description: Canonical domains, assumptions and valid bridges of UHM
---

# Typed mathematical kernel

This page fixes the mathematical interface of UHM after the foundational revision of 2026-10-03. A theorem concerns its stated objects and assumptions; an interpretation does not change their types. The numerical state model is retained, while the formerly asserted identification of categorical logic, channels, attractors and experience is replaced by explicit bridges.

## States and processes {#states-processes}

Fix finite-dimensional complex Hilbert spaces with chosen semantic frames. Write

$$
D_N=\{\rho\in M_N(\mathbb C):\rho=\rho^\dagger,\ \rho\succeq0,\ \operatorname{Tr}\rho=1\}.
$$

Its trace-one affine hull has real dimension $N^2-1$. Full-rank states form its relative interior; rank-deficient states are not an open smooth manifold of that dimension.

The process category has objects $M_N(\mathbb C)$, $N\ge1$, and linear CPTP maps as arrows. Its pointed version has objects $(N,\rho)$ and arrows $K:(N,\rho)\to(M,\sigma)$ with $K(\rho)=\sigma$. Composition and the tensor product are inherited from channels. The tensor unit $M_1(\mathbb C)$ is terminal: the only trace-preserving map to it is discarding, $X\mapsto\operatorname{Tr}X$.

**Terminality theorem [T].** No state $(N,\rho)$ with $N>1$ is terminal in the pointed process category. Both the identity and the replacement channel $X\mapsto\operatorname{Tr}(X)\rho$ are distinct endomorphisms fixing $\rho$. In particular $I/N$ is a state, not the terminal object.

The sector $N=7$ is a selected state model [P], not a tensor-closed category: two seven-dimensional systems have joint state in $D_{49}$. A literal partial trace requires a specified tensor factorization. A named basis vector does not define a nontrivial tensor factor.

## A genuine Bures site {#bures-site}

Equip $D_N$ with the chordal Bures distance

$$
d_B(\rho,\sigma)=\sqrt{2(1-\sqrt{F(\rho,\sigma)})}.
\qquad F(\rho,\sigma)=\left\|\sqrt\rho\sqrt\sigma\right\|_1^2.
$$

Use the site $\mathcal O_N=\operatorname{Open}(D_N,d_B)$: arrows are inclusions of open sets and a family $(U_i\subseteq U)$ covers iff $\bigcup_iU_i=U$. This gives the canonical realization

$$
\mathcal E_N=\operatorname{Sh}_\infty(\mathcal O_N,J_{\mathrm{open}}).
$$

**Site theorem [T].** Identities cover, pullback is intersection, and unions of covering families cover. Indeed $V\cap U=\bigcup_i(V\cap U_i)$ and $U=\bigcup_{i,j}U_{ij}$ whenever $U_i=\bigcup_jU_{ij}$. Thus the open-cover topology satisfies the Grothendieck axioms. Universe conventions make this a small site.

A CPTP map $K:D_N\to D_M$ is Bures-continuous (in fact contractive), so inverse images of opens define a geometric morphism $\mathcal E_N\to\mathcal E_M$. This is the correct bridge between the process category and sheaf semantics. It does not identify channels with inclusions of opens or with every morphism of a sheaf topos.

**Former channel-cover argument withdrawn [✗].** The condition that images of small balls cover a target ball is not proved to be stable as a sieve by CPTP contractivity. Contractivity bounds images, not inverse lifts. The old proof additionally used pullbacks in the process category without establishing their existence. One can generate a Grothendieck topology from arbitrary specified sieves, but generation alone does not prove its subcanonicity, metric interpretation or equivalence to the open site. None of those equivalences is assumed here.

The Bures and Euclidean topologies coincide on finite-dimensional $D_N$; a metric tensor is extra structure beyond its topology. Bures is distinguished within the family of monotone quantum metrics, not the only possible distinguishability metric. Its Riemannian tensor is used on full-rank strata; metric continuity extends to the boundary.

## Logic and a support mirror {#support-reflector}

In any $\infty$-topos $\mathcal E$, fix an object $G$. The correct universal construction is

$$
\operatorname{im}_G:\mathcal E_{/G}\rightleftarrows\operatorname{Sub}_{\mathcal E}(G):i_G,\qquad\operatorname{im}_G\dashv i_G.
$$

It sends $X\to G$ to its effective-epimorphism/monomorphism image, equivalently its $(-1)$-truncation in the slice. A map $X\to S$ over $G$ for a subobject $S\hookrightarrow G$ exists exactly when the image lies in $S$, and its space is contractible when it exists. This proves the adjunction; its restriction to subobjects is the identity. See the [full typed self-model construction](/docs/proofs/categorical/formalization-phi#категориальное-определение-φ).

This support mirror is logical. A numerical self-model $M:D_N\to D_N$ is a different object requiring a definition and, for empirical use, an observation model. No CPTP property, anchor, regeneration rate, Bures optimization, spectral projector or phenomenal content follows merely from the support adjunction.

The classifier $\Omega$ classifies subobjects. For sheaves on a space, its sections over $U$ are opens of $U$. It is not a seven-element algebra of projections. On connected $D_N$, clopen sets are only $\varnothing,D_N$; predicates $\rho_{ii}>0$ overlap, so they cannot be seven disjoint Boolean atoms. A chosen orthogonal frame gives a seven-outcome projective instrument [D], independently of $\Omega$. Reading it as articulation or internal logic is a bridge [I].

## Numerical self-models and dynamics {#dynamics}

A quantum channel is linear on the operator algebra and hence affine on states. The assertion “$M(\rho)\in D_N$ for every $\rho$” is only state preservation. If parameters depend on $\rho$, even a family of CPTP maps $K_\rho$ need not give an affine map $M(\rho)=K_\rho(\rho)$.

For example a fixed-anchor model

$$
M(\rho)=(1-R(\rho))\mathcal P_\alpha(\rho)+R(\rho)\rho_a,\qquad R(\rho)=1/(NP(\rho))
$$

has a CPTP realization for each frozen input-dependent coefficient, but the complete state map is generally nonlinear. Intrinsic anchors such as $\rho^2/P(\rho)$ are also nonlinear. Joint-system extensions must be specified; applying a nonlinear map to an unspecified ensemble is not a definition.

The evolution model is

$$
\dot\rho=-i[H,\rho]+\mathcal D(\rho)+a(\rho)(M(\rho)-\rho),\qquad a(\rho)\ge0.
$$

Given locally Lipschitz $a,M$, with $M(D_N)\subseteq D_N$, and a fixed GKSL generator for the linear part, it has unique solutions remaining in $D_N$ [T]. At a boundary vector $v\in\ker\rho$, the commutator and anticommutator contribute zero, and the remaining quadratic forms are $\sum_k v^\dagger L_k\rho L_k^\dagger v+a\,v^\dagger M(\rho)v\ge0$. Trace is preserved. The finite-dimensional tangent-cone criterion gives invariance; compactness gives global continuation. This theorem proves well-posedness, not physical selection of $M,a,H$.

Neither a unique stationary state nor a gap of the *linear* generator proves uniqueness or contraction of the nonlinear flow. On the trace-one tangent space the Jacobian of a hyperbolic sink has no zero eigenvalue. The zero trace mode of a linear operator on all matrices cannot be substituted for a state-dependent self-model.

If every trajectory in a forward-invariant domain converges to a fixed point **in that domain**, its limit map is idempotent there [T]. An open basin may exclude its boundary limits: either require that all limits lie in the domain, or extend the map by the identity on those fixed points before composing it with itself. Existence, continuity, linearity and complete positivity of this limit are separate questions. An idempotent set map alone does not define a categorical reflector.

## Thresholds and operational meaning {#thresholds}

Write $P=\operatorname{Tr}\rho^2$, $d=\sum_i\rho_{ii}^2$, $q=P-d$, and $\Phi=q/d$. Then

$$
P=1/N+\|\rho-I/N\|_F^2,\quad d\ge1/N,\quad \Phi\le NP-1.
$$

These are exact [T]. The following are model choices [D]/[I]: call structural majority $\|\rho-I/N\|_F^2>1/N$ “viability”; call $R\ge1/3$ “reflexive access”; call coherent majority $\Phi\ge1$ “integration”. They imply the numerical cuts $2/N,1/3,1$ [T]. Their interpretation as biological survival or experience remains [H]/[I]. A posterior probability requires a likelihood and priors; $R=1/(NP)$ does not become one by being named reflection.

For $N=7$, the capability gate is

$$
\mathrm{Cap}_2=(P>2/7)\land(R\ge1/3)\land(\Phi\ge1)\land(D_{\mathrm{diff}}\ge2).
$$

Here $D_{\mathrm{diff}}$ requires its stated experiential realization or a separately declared proxy. The first two conjuncts give $(2/7,3/7]$. The interval alone is not the whole gate. The product $C=\Phi R\ge1/3$ is necessary for the two scalar access conditions but is not sufficient for their conjunction. Identifying $\mathrm{Cap}_2$ with consciousness is an empirical/ontological bridge, not a theorem about matrices.

Phases alone do not determine this gate. See [Gap identifiability](/docs/consciousness/hierarchy/interiority-hierarchy#теорема-gap-инъекция). Reconstruction from data likewise requires informational completeness or a demonstrated identifiable statistical model, not only symmetry of the codomain.

**Representation bridge (RI) [H].** A conditional comparison of encoders can assume that both are bijective and that their comparison is a CPTP isomorphism preserving a specified octonionic three-form. The resulting symmetry classification is then a theorem with those inputs. Observed data, dynamics and codomain symmetry do not imply (RI); it is much stronger than covariance. General reconstruction uses observation-law fibres instead. See the [corrected uniqueness theorem](/docs/proofs/categorical/uniqueness-theorem).

## Dimension and physics bridges {#dimension-physics}

Seven functional names do not prove seven linearly independent coordinates. The strongest established lower bound here is conditional on the perfect-diagnosability premise $(\Sigma_6)$; a separate exact representation theorem bounds faithful representations of $\mathbb C\oplus M_3(\mathbb C)\oplus M_3(\mathbb C)$ by dimension seven. Each conclusion retains its premise. See [minimality](/docs/proofs/minimality/theorem-minimality-7).

Tensor extensions $D_7\to D_{42}$ require a named lift and readout. A section–retraction is not Morita equivalence and does not make lift-dependent reduced entropies functions of $\rho\in D_7$ automatically.

The matter-action bridge (Mod)/(Cl₀), spacetime bridge (P), anchor principle (MaxΦ), chosen rates and phenomenal identification remain explicit inputs. Mathematical group coincidences and encodings do not derive physical dynamics without them; the [premise register](/docs/reference/premises) records these dependencies.

## Topology, terminality and time {#terminal-time}

The terminal object $1_{\mathcal E}$ exists in every topos. Its global sections are the terminal space, not $I/7$. It does not supply a relaxation channel or an arrow of time. A category with a terminal object has contractible nerve, but terminality of its *sheaf category* does not imply terminality of the indexing category.

$D_N$ is convex and contractible. Removing degeneracy sets may produce nontrivial topology; its homotopy and that of an explicitly specified experiential object must be calculated. The availability of higher mapping spaces does not force them to be nontrivial or identify a Postnikov stage with consciousness. A Postnikov tower has inverse limit, with convergence requiring Postnikov completeness of the object/topos.

A physical frequency must be invariant under $H\mapsto H+cI$. Thus $\min\operatorname{spec}H$ cannot supply it. Use a specified nonzero Bohr-frequency scale or a calibrated $\omega_0>0$ [P]. A clock factor and Page–Wootters constraint are additional data; periodic ticks do not by themselves give an aperiodic time line or thermodynamic arrow.

<a id="verification"></a>

## Sources and verification {#sources}

- Jacob Lurie, [Higher Topos Theory](https://arxiv.org/abs/math/0608040), §§5.5.6, 6.2: truncations, sheaf topoi and geometric morphisms.
- Dénes Petz and Csaba Sudár, [Geometries of Quantum States](https://www.esi.ac.at/preprints/esi204.pdf): monotone metrics and the distinguished minimal metric.
- John Watrous, [The Theory of Quantum Information](https://jhwatrous.github.io/books-and-courses.html): channels, discrimination, measurements and reconstruction.
- R. W. Hamming, [Error Detecting and Error Correcting Codes](https://doi.org/10.1002/j.1538-7305.1950.tb00463.x): coding assumptions underlying the dimension bound.
- Yui Kuramochi, [GKSL derivation from Kraus representations](https://arxiv.org/abs/2406.03775): finite-dimensional linear semigroups; no extension to arbitrary nonlinear maps is presumed.

`website/scripts/check_mathematical_kernel.py` checks counterexamples to the withdrawn implications and the explicit replacement identities. Numerical checks supplement the proofs; they do not certify every theorem or any phenomenal interpretation.
