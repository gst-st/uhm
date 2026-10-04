---
sidebar_position: 3
title: "Operationalization of consciousness"
description: "Declared readouts, conditional error bounds, sampling and the scope of T-128–T-138"
---

# Operationalization of consciousness

:::info Result scope
Definitions [D], empirical/functional hypotheses [H] and conditional mathematical results [T] are distinguished. A computable state function is not automatically identified from observations. Universal encoder uniqueness, scalar purity as a full gate and automatic hypothesis upgrades are withdrawn.
:::

## §1. T-128: a selected 7D differentiation proxy [D] {#t-128}

In the fixed frame, let $\pi_E(X)=P_EX+XP_E-P_EXP_E$ retain the E row and column. Then

$$
\mathrm{Coh}_E=\frac{\|\pi_E\Gamma\|_F^2}{P}\in[0,1],\qquad
D_{\mathrm{diff}}^{7D}:=1+6\mathrm{Coh}_E.
$$

The range and endpoints follow from an orthogonal **operator-space** projection; $\pi_E$ is generally neither positive nor an algebra conditional expectation. Its maximum is attained at $|E\rangle\langle E|$ ([T-154](/docs/proofs/consciousness/substrate-closure#t-154)); zero is attained by states supported outside E.

This formula is a proxy choice [D], not $e^{S(\rho_E)}$ derived from partial trace. A prime seven-dimensional Hilbert space has no nontrivial tensor factor selected by naming an E coordinate. The unnormalized scalar $\gamma_{EE}$ is not a density matrix for reduced entropy; a normalized one-dimensional state has entropy zero. A declared extended lift and partial trace can define a different $\rho_E$, which must be written explicitly. A section–retraction alone does not make every quantity of the larger space a function of the smaller state.

The proxy is not even a universal endpoint match to global entropy: at the pure E state, $D_{\mathrm{diff}}^{7D}=7$ while $e^{S(\Gamma)}=1$. At $I/7$, the proxy is $13/7$ while global $e^S=7$. Claims of equality, CPTP monotonicity or reconstruction of reduced entropy from this scalar are withdrawn. The score $\sigma_E^{\mathrm{diff}}=(7-D_{\mathrm{diff}}^{7D})/5$ is another definition, with range $[0,6/5]$. Use it consistently with the declared gate; it is not the diagonal clamp score of [T-158](/docs/proofs/consciousness/substrate-closure#t-158).

## §2. T-129: integration threshold selection and sharp algebra {#t-129}

Write $d=\sum_i\gamma_{ii}^2$, $q=\sum_{i\ne j}|\gamma_{ij}|^2$, $P=d+q$, $\Phi=q/d$. Trace one gives $d\ge1/7$. Consequently

$$
P=d(1+\Phi),\qquad\Phi\le7P-1,\qquad\Phi\ge1\Rightarrow P\ge2/7.
$$

These are theorems [T] for the fixed-frame measure. Selecting $\Phi\ge1$ as an access criterion is [D]; the inequalities do not force a consciousness criterion, Bayes posterior or universal biological normalization. Purity above $2/7$ need not imply $\Phi\ge1$: a pure diagonal state has $P=1$, $\Phi=0$.

#### Nested HS weight criteria {#вложенные-мажоритарные-критерии}

The orthogonal decomposition $\Gamma=I/7+(\operatorname{diag}\Gamma-I/7)+\operatorname{offdiag}\Gamma$ gives weights $c_1=1/7$, $c_2=d-1/7$, $c_3=q$. Hence

$$
P>2/7\iff c_2+c_3>c_1,\qquad\Phi\ge1\iff c_3\ge c_1+c_2.
$$

Coherence majority implies **non-strict** structural majority; equality requires $c_2=0$, $c_3=c_1$. This is an equality locus, not one unique matrix. It does not make HS weights posterior probabilities or derive $R_{\mathrm{th}}=1/3$ from three operator terms. The diagonal/hollow split is pinned to a declared frame; $\Phi$ generally changes under $G_2$ rotations.

#### T-129a: sharp universal implication on the specified state space [T] {#t-129a-универсальность}

The proof is $P=d(1+\Phi)\ge2d\ge2/7$. Equality occurs iff $d=1/7$ and $\Phi=1$; every other state satisfying $\Phi\ge1$ has strict $P>2/7$. There are many equality states, including phase-conjugate families with the same norm.

The least scalar cut $t$ such that $\Phi\ge t$ guarantees $P\ge2/7$ for all states is $t=1$. Sharpness follows from $\Gamma_\lambda=(1-\lambda)I/7+\lambda|u\rangle\langle u|$, $u=(1,\ldots,1)/\sqrt7$: $\Phi=6\lambda^2$ ranges below one with $P=(1+\Phi)/7<2/7$. This proves that selected extremal guarantee; it does not imply strict viability at equality or independence of every gate. The complete conjunction remains [Cap₂](/docs/reference/mathematical-kernel#thresholds), with a separately realized differentiation variable.

## §3. T-130: correctly typed state/readout error bounds {#t-130}

A feature map $\pi:\mathbb R^D\to\mathcal D_7$ has no diamond norm or Choi matrix by this type. It needs a calibrated observation model; the withdrawn T-123/T-42a do not provide a canonical comparator. Compare state estimates or declared identifiable targets on a specified domain.

**Conditional theorem [T].** If two valid states $\rho,\sigma$ satisfy $\|\rho-\sigma\|_F\le\varepsilon$ (or the stronger trace-norm bound), then

$$
|P(\rho)-P(\sigma)|\le2\varepsilon.
$$

If both purities are at least $p_{\min}>0$, the defined HS reflection $R=1/(7P)$ satisfies

$$
|R(\rho)-R(\sigma)|\le\frac{2\varepsilon}{7p_{\min}^2}.
$$

**Proof.** Factor $P(\rho)-P(\sigma)=\operatorname{Tr}[(\rho-\sigma)(\rho+\sigma)]$ and use $\|\rho\|_F,\|\sigma\|_F\le1$. Divide by $7P(\rho)P(\sigma)$. On all $\mathcal D_7$ one may use $p_{\min}=1/7$, giving $14\varepsilon$; on a certified purity region the tighter constant applies. $\blacksquare$

If $\mathcal A,\mathcal B:M_d\to M_7$ are genuinely **linear** channels with $\|\mathcal A-\mathcal B\|_\diamond\le\varepsilon$, their outputs on any state meet the trace-norm premise. [T-152](/docs/proofs/consciousness/substrate-closure#t-152) states the corresponding Choi bounds. A neural universal-approximation statement for continuous feature functions does not prove diamond-norm channel approximation, calibration or a finite training guarantee. A feature-space “reflection” defined by another norm needs its own bridge, not a renamed $R$.

## §4. T-131: discretization is accuracy/model dependent {#t-131}

The former unique step $h=\pi/(2\|\mathcal L_0\|)$ is a heuristic [D], not a lossless sampling or numerical theorem. A dissipative mode $e^{-\gamma t}\mathbf1_{t\ge0}$ has Fourier transform $1/(\gamma+i\omega)$, nonzero at all frequencies. Bounded imaginary eigenvalues therefore do not establish Shannon band limitation. Even scalar samples alias unknown frequencies differing by $2\pi/h$; identifying a generator requires a specified observation and frequency model.

For a **known fixed** GKSL generator, $e^{h\mathcal L_0}$ is a state-valid exact propagator for every $h\ge0$. For numerical ODE integration select $h$ using a specified method and tolerance. If an autonomous field is $L$-Lipschitz and bounded by $M$ on a neighborhood containing the exact and numerical trajectories, explicit Euler has local truncation error at most $LMh^2/2$ and global error at grid time $T$ at most

$$
\frac{Mh}{2}(e^{LT}-1).
$$

The local bound follows by integrating $\|F(\Gamma(t))-F(\Gamma(0))\|\le LMt$; summing the discrete error recurrence proves the global bound. These are conditional accuracy statements [T], not PSD preservation: Euler may violate positivity. A split product of fixed CPTP propagators preserves states; its order and error require regularity/commutator bounds for that splitting. State-dependent freezing introduces its own approximation error. A polynomial $h^2$ error is not “exponentially small” because a spectral gap is large. Clock ticks, sensor sampling and integrator steps need not coincide and do not order themselves without a declared rate model.

## §5. T-132: complex entries for nonzero phase Gap in a fixed frame {#t-132}

For a nonzero entry, define $\mathrm{Gap}_{ij}=|\sin\arg\gamma_{ij}|$. Then

$$
\mathrm{Gap}_{ij}>0\iff\operatorname{Im}\gamma_{ij}\ne0.
$$

Thus a matrix real in the declared frame has zero entrywise phase Gap. This is the valid conditional theorem [T]; the quantity at a zero entry needs an explicit convention. A diagonal phase change alters these entry phases, so the statement is frame-dependent. Complex data are required for reconstructing signed phases in this representation, not a theorem of irreducible complex ontology.

For real $H,\Gamma$, the Hamiltonian derivative is imaginary only when their commutator is nonzero. If $[H,\Gamma]=0$, it remains zero. Primitivity and $H\ne0$ do not force nontrivial stationary phases: a primitive unital generator has stationary $I/7$, a real diagonal state. The former stronger dynamical claim is withdrawn. Magnitudes or Gap alone do not determine signed phases; [explicit positive-state counterexamples](/docs/applied/research/reconstruction-identifiability#phase-counterexamples) remain indistinguishable by those observations.

## §6. T-133: conditional threshold transfer {#t-133}

If the **same declared** scalar readout has a verified error bound $|R_{\rm estimate}-R_{\rm target}|\le\eta_R$, then

$$
R_{\rm estimate}\ge1/3+\eta_R\Rightarrow R_{\rm target}\ge1/3.
$$

This is a direct subtraction theorem [T]; T-130 supplies $\eta_R$ under its state/channel premises. Strict cuts require strict certified margins. Other readouts and all other Cap₂ conjuncts need their own error bounds or ranges over the observation confidence set. A small error without a margin cannot transfer a boundary verdict.

No dimension-free feature-space bridge or unique empirical target has been proved. Similarity scores, another norm's reflection and an arbitrary $\rho_{RC}$ are not automatically this $R$. H3 remains an empirical identification/calibration question [H]; T-130/T-133 close only the stated mathematical error-transfer problem.

## §7. T-134: population dynamics and stationarity {#t-134}

For the specified equation $\dot\Gamma=-i[H,\Gamma]+\mathcal D(\Gamma)+a(\varphi(\Gamma)-\Gamma)+B(\Gamma)$,

$$
\dot\gamma_{kk}=2\sum_j\operatorname{Im}(H_{kj}\gamma_{jk})+\mathcal D(\Gamma)_{kk}+a(\varphi(\Gamma)_{kk}-\gamma_{kk})+B(\Gamma)_{kk}.
$$

This follows by expanding the commutator and is [T]. Hermiticity makes $[H,\Gamma]_{kk}$ imaginary; multiplying it by $-i$ gives a real, possibly nonzero population derivative. For $H=\sigma_x$, $\Gamma=|(1,i)/\sqrt2\rangle\langle(1,i)/\sqrt2|$ on a two-dimensional subspace, $\dot\gamma_{00}|_H=1$.

At any actual stationary point the **sum** is zero. Stationarity does not imply that each term vanishes or that $\varphi(\Gamma_*)=\Gamma_*$; living stationarity can have nonzero turnover. Away from stationarity populations may change or remain frozen, depending on the field. A sufficient freeze condition is diagonal $H$, population-preserving dephasing, matching target populations and no population-changing input. See the corrected [T-122](/docs/core/dynamics/evolution#теорема-диагональный-freeze).

An unital linear part, $g_V(1/7)=0$ and no external input make the initial $I/7$ stationary. Positive bootstrap alone gives no genesis there. Neither a stationary diagonal nor a transient rate proves a universal personality or learning mechanism.

## §8. T-135: finite-dimensional exponential memory realization {#t-135}

For a specified constant linear operator $C$ and $\omega>0$, set

$$
M(t)=\int_0^te^{-\omega(t-s)}C\Gamma(s)\,ds.
$$

Differentiation gives the exact auxiliary equation $\dot M=C\Gamma-\omega M$, $M(0)=0$. With zero-order hold $\Gamma(s)=\Gamma_n$ within a step of size $h$,

$$
M_{n+1}=qM_n+\frac{1-q}{\omega}C\Gamma_n,\qquad q=e^{-\omega h}.
$$

For a chosen rectangle discrete convolution $M_n=h\sum_{j=0}^nCq^{n-j}\Gamma_j$, the different recurrence is $M_{n+1}=qM_n+hC\Gamma_{n+1}$. Both identities are [T] for their respective conventions; neither is an exact discretization of an unspecified coupled nonlinear dynamics.

A fixed number of exponential terms needs a fixed number of auxiliaries, independent of history length. For $m$ stored state coordinates, memory costs $O(m)$ per term and applying a dense $C$ costs $O(m^2)$; “$O(1)$” refers only to the number of past steps at fixed dimension/operator cost. General kernels need approximation with an error bound. A negative exponential kernel and Euler state update do not automatically preserve PSD, trace or a non-Markovian CPTP family; a physical embedding or separate validity proof is required.

## §9. T-136: score arithmetic versus certified depth {#t-136}

The historical score (the universal T-136 identification is withdrawn [✗]) $s_{n-1}=(P/(2/7))3^{-(n-1)}$ is a definition [D]. Since it depends only on purity it is unitarily invariant and cheap to compute from a known matrix. Its stipulated gate $s_{n-1}>1/(n+1)$ yields the arithmetic cuts $(1/7,2/7,9/14,54/35)$ for levels one to four, and a score cap three. This score can exceed one and is not reflection, a survival probability or a universal cognitive-depth observable.

Bare Fano off-diagonal attenuation is $S_n=3^{-n}$, with a detector-dependent cutoff. A certified meta-depth instead uses the declared nonconstant probes and compatibility tests in [depth tower](/docs/consciousness/hierarchy/depth-tower). A probe is observable from a reduced state exactly when it is constant on the relevant encoder fibers; T-150's iteration identity does not prove that condition. The former equivalence of all autoencoder towers, a purity-only canonical SAD and universal SAD–L implications is withdrawn. Architectural certification remains [D/Pr], with empirical tests [H].

## §10. T-137: computability of selected stress functions {#t-137}

Fix the frame, proxy variant, rate parameters and boundary conventions first. The following are **raw proposed scores**, not equivalent universal definitions:

| Score | Declared expression | Required input / limitation |
|---|---|---|
| $\sigma_A$ | $1-\gamma_{AA}/P$ | State; can be negative |
| $\sigma_S$ | $1-\operatorname{rank}(\Gamma_{ASD})/3$ | State; rank may be zero and is discontinuous at rank changes |
| $\sigma_D$ | $1-7\gamma_{DD}$ | State; range $[-6,1]$ |
| $\sigma_L$ | $7(1-\gamma_{LL})/6$ | State; range $[0,7/6]$ |
| $\sigma_E^{\mathrm{diff}}$ | $(7-D_{\mathrm{diff}}^{7D})/5$ | Chosen T-128 proxy; range $[0,6/5]$ |
| $\sigma_O$ | $1-\kappa_0/\kappa_{\mathrm{bootstrap}}$ | Declared rate model/parameters, positive denominator and singular-boundary treatment |
| $\sigma_U$ | $2/(1+\Phi)$ | State in fixed frame; range $[2/7,2]$ |

From a fully known state and those extra declared inputs, these expressions can be evaluated; clamping a raw score defines a different function. This conditional evaluation statement [T] does not select the scores, prove continuity of rank or their empirical/clinical meaning. In particular, T-137's full-state formulas do not supply seven observed neural targets. A function is identified from data iff it is constant on the [observation fiber](/docs/applied/research/reconstruction-identifiability#fiber-theorem), with noise requiring a confidence range. $\kappa_0$ is not fixed by state data without the kinetic calibration. A real matrix may have nonzero E population or coherence magnitude, so complex arithmetic is not required for every one of these scalar evaluations.

## §11. T-138: product representation and correlation error {#t-138}

For declared marginals $\Gamma_1,\ldots,\Gamma_k$, the product $\Gamma_{\mathrm{mf}}=\bigotimes_i\Gamma_i$ is a valid state and

$$
P(\Gamma_{\mathrm{mf}})=\prod_iP(\Gamma_i).
$$

If every factor has $P_i>2/7$, the product has $P>(2/7)^k$. This is an algebraic purity statement [T], not the full seven-dimensional Cap₂ predicate for a compressed composite. The composite lives in dimension $7^k$ before any declared coarse-graining.

Storing the **factorized representation** costs $O(kN^2)$; materializing its dense matrix costs $O(N^{2k})$. Computing arbitrary correlated observables or interaction corrections may also require larger representations. A general pair density matrix already has $N^4-1$ parameters, so pairwise corrections do not universally cost $O(k^2N^2)$.

Let $\rho$ be the actual joint state and $\delta_{\rm corr}=\rho-\bigotimes_i\rho_i$. Then the approximation error is exactly $\|\delta_{\rm corr}\|_F$; it is small only with a verified bound on the **full** correlation tensor. Off-diagonal cross-coherences alone do not bound it: for $\rho=(|00\rangle\langle00|+|11\rangle\langle11|)/2$ (embedded in $\mathbb C^7\otimes\mathbb C^7$), all off-diagonal entries vanish but $\|\rho-\rho_1\otimes\rho_2\|_F=1/2$. Weak bare coupling without a time/state-dependent correlation estimate supplies no uniform error guarantee. Cluster approximation is a chosen algorithm [D/H], whose truncation, observable errors and state validity require separate checks.

## §12. Scope of the former hypothesis upgrades

### SAD–L equivalence {#г-89-повышение}

Hyp-89 remains a probe/bridge hypothesis. A stipulated score, one successful level or a positive late limit does not certify the entire preceding prefix of meta-tests. No universal equivalence follows from T-136.

### Iteration and tower compatibility {#г-90-повышение}

[T-150](/docs/proofs/consciousness/substrate-closure#t-150) proves $M^nM^m=M^{n+m}$ for iterates of the **same specified map**, which can be nonlinear. Equal dimensions do not identify different maps or prove heterogeneous compatibility $\pi_kM_{k+1}=M_k\pi_k$. That diagram remains a separately stated/tested requirement.

### Conditional genesis {#г-91-обоснование}

[T-148](/docs/proofs/consciousness/substrate-closure#t-148) gives crossing exactly in its specified affine model when $w>1/\sqrt{7P_{\rm env}-1}$. A pure environment and positive coupling alone need not suffice. Stationarity of one isolated initial $I/7$ does not prove embodiment necessary for every living or conscious state.

### H3: calibration and threshold transfer {#h3-закрыта}

T-130/T-133 give conditional error transfer after a correctly typed state/channel bound and strict margin are established. They do not close empirical calibration, observation identifiability or an arbitrary feature-space reflection bridge.

## §13. Status summary

| Result | Current scope |
|---|---|
| T-128 | Proxy definition [D]; entropy/lift equality withdrawn |
| T-129 / T-129a | Sharp algebra [T]; access cut selected [D], only one-way purity implication |
| T-130 | State/readout error theorem [T under certified error]; feature-map diamond claim withdrawn |
| T-131 | Step choice [D]; conditional accuracy bounds [T], no general Shannon/Nyquist derivation |
| T-132 | Entrywise complex necessity [T in a fixed frame]; stationary-phase claim withdrawn |
| T-133 | Margin transfer [T]; empirical H3 remains [H] |
| T-134 | Exact population derivative/stationarity [T]; universal diagonal freeze withdrawn |
| T-135 | Exponential auxiliary/declared convolution identities [T]; general validity and cost not automatic |
| T-136 | Historical score [D], attenuation arithmetic [T]; universal SAD equivalence withdrawn |
| T-137 | Selected scores [D]; evaluation [T with full state and extra model inputs], observation identification separate |
| T-138 | Product validity, purity and factorized storage [T]; coherence-only correlation bound withdrawn |

Related: [operational closure](/docs/proofs/consciousness/operational-closure), [conscious window](/docs/proofs/consciousness/conscious-window), [reconstruction and identifiability](/docs/applied/research/reconstruction-identifiability).
