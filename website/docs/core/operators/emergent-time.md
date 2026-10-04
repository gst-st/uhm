---
sidebar_position: 3
title: "Emergent Time"
description: "Specified clocks, conditional histories, and the exact scope of temporal claims"
---

# Emergent Time

Temporal structure requires a specified clock, readout, and dynamics. The categorical [kernel](/docs/reference/mathematical-kernel#terminal-time) supplies none of these automatically. On the chosen site $\operatorname{Open}_B(D_N)$ the classifier $\Omega$ describes logical subobjects; it is not a set of $N$ rank-one projectors. $N=7$ is the selected model dimension, not a theorem forcing seven moments of physical time.

The relational idea of [Page and Wootters (1983)](https://doi.org/10.1103/PhysRevD.27.2885) is to describe a system conditional on an internal clock reading. Implementing it requires the clock subsystem and the joint state. The constructions below distinguish cyclic labels, a directed history, metric length, and physical calibration.

<a id="темпоральная-модальность"></a>

## A supplied cyclic clock

Choose an integer $N\ge2$, a free transitive $C_N$-set $T$, a generator $s$, and a basepoint $t_0$. Then $t_n=s^nt_0$ labels its $N$ readings. On the external Boolean algebra $2^T$, define $\triangleright p=p\circ s^{-1}$; it preserves the Boolean operations and satisfies $\triangleright^N=\mathrm{id}$. This is a definition on the supplied clock labels, not a modality forced on the topos classifier or a guarded “later” modality.

<a id="temporal-modality-pw"></a>
<a id="clock-basis"></a>
<a id="fourier-clock-basis"></a>

Set $\mathcal H_C=\ell^2(T)\cong\mathbb C^N$. With an independently chosen energy basis and scale $\omega_0>0$, take $\hbar=1$ and define

$$
H_C=\omega_0\sum_{k=0}^{N-1}k\lvert E_k\rangle\langle E_k\rvert,
\qquad
\lvert\tau_n\rangle=\frac1{\sqrt N}\sum_{k=0}^{N-1}e^{-2\pi i kn/N}\lvert E_k\rangle.
$$

The finite Fourier sum proves orthonormality and the exact shift identity

$$
e^{-iH_C\delta t}\lvert\tau_n\rangle=\lvert\tau_{n+1\bmod N}\rangle,
\qquad \delta t=\frac{2\pi}{N\omega_0}.
$$

The choice of spectrum fixes this realization. A matrix logarithm of the shift has branch ambiguity; it does not uniquely recover a Hamiltonian or its physical scale from logic.

<a id="page-wootters"></a>

## A supplied tensor factor and conditional states

Choose $\mathcal H_{CS}=\mathcal H_C\otimes\mathcal H_S$ and a density matrix $\Gamma_{CS}$. A labelled one-dimensional O-axis in $\mathbb C^7$ is a subspace, not a seven-dimensional clock factor. In particular $\mathbb C^7=\mathbb C\oplus\mathbb C^6$ does not give $\mathbb C^7\cong\mathbb C^7\otimes\mathbb C^6$; the latter is a separately constructed 42-dimensional joint system.

<a id="constraint"></a>

For a supplied self-adjoint constraint

$$
\widehat C=H_C\otimes I_S+I_C\otimes H_S+H_{\mathrm{int}},
\qquad \operatorname{supp}\Gamma_{CS}\subseteq\ker\widehat C,
$$

one has $\widehat C\Gamma_{CS}=0$ and $[\widehat C,\Gamma_{CS}]=0$. Stationarity alone does not imply the support constraint: a mixture over two distinct constraint eigenvalues commutes with $\widehat C$ but cannot be supported in one kernel after an energy shift. T-87 remains conditional on the specified tensor factor and support constraint.

<a id="emergent-tau"></a>

For $\Pi_n=\lvert\tau_n\rangle\langle\tau_n\rvert\otimes I_S$ and $p_n=\operatorname{Tr}(\Pi_n\Gamma_{CS})>0$, the conditional state is

$$
\rho_S(n)=\frac{\operatorname{Tr}_C(\Pi_n\Gamma_{CS}\Pi_n)}{p_n}.
$$

This gives valid density matrices. A unitary conditional evolution further requires compatible clock and system spectra and the chosen constraint; the tensor product or stationarity alone is insufficient. An interacting or dissipative conditional law requires its own construction.

<a id="chronon"></a>

## Cyclic resolution and directed histories

The step $\delta t$ is the resolution of the specified spectrum, not a universal quantum of physical or subjective time. The clock repeats after $2\pi/\omega_0$ and records only $n\bmod N$. For $M$ identical additive $N=7$ clocks the sum has $6M+1$ distinct energies, although the tensor space has dimension $7^M$; its period is unchanged. Positional history registers are a different construction.

T-53b supplies an exact finite realization of a **specified** channel history using a chosen register, Stinespring dilation, and a history constraint; see [§11.4](/docs/proofs/dynamics/emergent-time#114-регистр-глубины). A state-dependent nonlinear trajectory can be reproduced by a constraint fitted to that trajectory; this does not produce one linear CPTP law for all inputs. The verified finite and limiting register constructions are in [§11](/docs/proofs/dynamics/emergent-time#11-прецеденты-и-родственные-программы).

<a id="four-constructions-equivalence"></a>

## T-53a: the exact label-set theorem

Given two based free transitive $C_N$-sets $(T_1,s_1,t_1)$ and $(T_2,s_2,t_2)$, the map

$$
b(s_1^nt_1)=s_2^nt_2
$$

is the unique equivariant bijection carrying $t_1$ to $t_2$ [T]. Freeness makes the formula well-defined modulo $N$, and transitivity proves bijectivity. Without the selected basepoint correspondence there are $N$ such bijections, so no canonical one is supplied.

Assigning PW, geometric, or categorical descriptions to these labels is additional model data. The theorem does not identify their processes or prove equal clock rates. Bures arc length is a curve-dependent functional; it can vanish on a stationary curve and reparameterizes a regular curve only where its speed is positive. An invertible path groupoid does not by itself encode irreversible channel histories. A directed depth $n$ and cyclic label $n\bmod N$ are not bijective. The former universal equivalence of four temporal constructions is withdrawn [✗]; see [§6](/docs/proofs/dynamics/emergent-time#6-теорема-об-эквивалентности).

<a id="t-53c"></a>

## The Arrow of Time
The arrow below belongs to a **specified history** of quantum processes; it is not derived from a terminal object or the existence of a topos. Choose $\rho_0\in D_N$ and linear CPTP channels $K_0,\ldots,K_{m-1}$, and set $\rho_{n+1}=K_n(\rho_n)$. Assigning states $(N,\rho_n)$ to the objects of the ordered category $[m]=(0<\cdots<m)$ and channel composites to its arrows gives a directed history [D]. Its direction is supplied by the order of records; identifying it with physical time requires a separate bridge.

:::warning T-53c: exact scope [T under unital channels]
If all $K_n$ are unital, $K_n(I/N)=I/N$, data processing gives

$$
D(\rho_{n+1}\Vert I/N)\le D(\rho_n\Vert I/N),\qquad
D(\rho\Vert I/N)=\log N-S_{vN}(\rho).
$$

Entropy is therefore non-decreasing along the specified history [T]. For a fixed unital GKSL semigroup the same statement holds in its parameter $t\ge0$. CPTP and unitality are explicit hypotheses, not consequences of orientation toward a terminal object.

Strict loss needs a separate condition: nonunitarity or absence of a CPTP inverse **alone** does not make the inequality strict at every input. Identity and unitary steps preserve $D$; a coarse-graining may preserve an already coarse-grained state. If a channel merges two distinct admissible states, there is no common recovering left inverse on that class. An arbitrary functor has no specified linear kernel; “$\ker\pi\ne0$” is not a general criterion for nonequivalence.

A strict decrease of $D(\rho\Vert I/N)$ excludes a CPTP recovery that restores **both states in the pair** $(\rho,I/N)$ after the step. It does not exclude preparing one previously known $\rho$ with a replacement channel; that preparation does not recover information about an unknown input.

**Verified strict example.** For $0<p<1$, choose $K_p(X)=(1-p)X+p\operatorname{Tr}(X)I/N$. When $\rho\ne I/N$, strict concavity of entropy gives $S(K_p\rho)>S(\rho)$, hence $D(K_p\rho\Vert I/N)<D(\rho\Vert I/N)$. This channel has zero linear kernel but no CPTP inverse: data processing for a proposed inverse would contradict strictness. This is a non-reversible action under explicit hypotheses, not a universal law of all channels.
:::

### Intuitive Explanation of the Arrow

Forgetting is irreversible on a class of records if distinct inputs yield the same output record: the output alone cannot recover the selected input. This property of a specified readout does not prove that every physical step forgets information or that every trajectory tends to one attractor. The directed count $n$ and cyclic tick $\tau=n\bmod7$ have different types; the tick label alone carries no strict monotonicity.

### Relation to CPTP

Fixed GKSL generators give linear CPTP semigroups; specified numerical self-models and rates may instead give a nonlinear state-preserving flow $\Phi_t$. It cannot be called one CPTP semigroup, and the entropy theorem above does not automatically apply to it. Monotonicity and convergence for the full dynamics require separate proofs.

The former derivations “terminality → collapse of strata → CPTP → universal cosmic arrow” and a general Lyapunov functional for the full nonlinear flow are withdrawn [✗]. The terminal process system is one-dimensional; $I/N$ is a state, not the terminal object or an automatically selected attractor. See the [kernel](/docs/reference/mathematical-kernel#terminal-time) and [direct proof](/docs/proofs/dynamics/emergent-time#7-теорема-о-стреле-времени).

---

<a id="time-freezing-derivation"></a>

## T-53d: conditional slowing at a fold

Purity alone does not determine a clock rate. With $P(\rho)=\operatorname{Tr}\rho^2$ and a fixed Hamiltonian,

$$
\lVert[H,\rho]\rVert_F\le2\lVert H\rVert_{\mathrm{op}}\sqrt{P(\rho)-1/N}.
$$

This is an upper bound, obtained by writing $\rho=I/N+\delta\rho$. A state diagonal in the energy basis has zero unitary speed at any allowed purity; neither $P>2/7$ nor $P=2/7$ implies a temporal threshold.

**(Fold).** Assume a smooth finite-dimensional vector field at an interior equilibrium has a simple zero eigenvalue, all other eigenvalues with negative real parts, and a nondegenerate one-parameter fold. In a smooth center coordinate and the specified evolution parameter, its reduced equation is

$$
\dot x=a\mu+b x^2+O(\lvert x\rvert^3+\lvert\mu x\rvert+\mu^2),
\qquad ab<0.
$$

For $\mu>0$ the stable branch has $x_*(\mu)=s\sqrt{-a/b}\sqrt\mu+O(\mu)$, where $s\in\{\pm1\}$ is chosen so $b x_*<0$. Its slow eigenvalue and local relaxation rate satisfy

$$
\lambda_{\mathrm{slow}}=-2\sqrt{-ab}\sqrt\mu+O(\mu),
\qquad r=-\lambda_{\mathrm{slow}}.
$$

**(ClockReadout).** Independently specify a smooth nonnegative rate along this branch, $q(x,\mu)=d x+O(x^2+\lvert\mu\rvert)$, with $d s\sqrt{-a/b}>0$. Define the internal clock by $d\tau_{\mathrm{int}}/dt=q(x_*(\mu),\mu)$. Then

$$
\frac{d\tau_{\mathrm{int}}}{dt}=C\sqrt\mu+O(\mu),
\qquad C=d s\sqrt{-a/b}>0.
$$

This is T-53d **[C under (Fold)+(ClockReadout)]**. A fold gives the square-root relaxation scale; identifying that scale with clock speed is the separate readout condition. The normal-form background is given in [Kuznetsov’s lecture notes](https://webspace.science.uu.nl/~kouzn101/INLDS/L2.pdf); [Kuehn (2009)](https://arxiv.org/abs/0807.1546) analyzes how degeneracy changes saddle-node scaling.

Replacing $\mu$ by $P-P_0$ requires an additional positive linear calibration $\mu=c_P(P(\rho_*(\mu))-P_0)+O((P-P_0)^2)$, $c_P>0$. If instead $P-P_0\propto\sqrt\mu$, the rate is linear in that purity difference. No argument sets $P_0=2/7$ universally. The former universal freezing, viability equivalence, and infinite subjective-time conclusions are withdrawn [✗]. See the [direct proof](/docs/proofs/dynamics/emergent-time#8-связь-с-критической-чистотой).

## Connections and preserved addresses

The [evolution model](/docs/core/dynamics/evolution) and its [density-preserving compiled step](/docs/core/dynamics/evolution#сохранение-положительности) must supply the dynamics. A target, an attractor, and logical support have different types; none selects the clock. The [full proof](/docs/proofs/dynamics/emergent-time) contains the independent finite history-register constructions. Historical addresses below now lead to the corrected scopes on this page.

<a id="clock-basis-for-n7"></a>
<a id="connections"></a>
<a id="construction-1-pagewootters-the-pendulum-in-the-room"></a>
<a id="construction-2-information-geometric-path-length"></a>
<a id="construction-3-categorical-chains-of-arrows"></a>
<a id="construction-4-stratificational-descent-down-the-staircase"></a>
<a id="derivation-of-the-time-slowing-formula-t-53d-t"></a>
<a id="discreteness-and-the-chronon"></a>
<a id="formal-justification-of-the-equivalence-of-the-four-constructions"></a>
<a id="four-equivalent-constructions"></a>
<a id="from-discrete-to-continuous"></a>
<a id="historical-precursors"></a>
<a id="intuitive-explanation-a-room-without-clocks"></a>
<a id="intuitive-explanation-freezing-of-time"></a>
<a id="relation-to-critical-purity"></a>
<a id="relation-to-the-pagewootters-hamiltonian"></a>
<a id="seven-frames-of-animation"></a>
<a id="summary-five-key-ideas"></a>
<a id="temporal-modality-"></a>
<a id="the-chronon-quantum-of-subjective-time"></a>
<a id="the-emergent-parameter-τ"></a>
<a id="the-pagewootters-constraint"></a>
<a id="the-pagewootters-mechanism-for-uhm"></a>
<a id="why-the-fourier-basis"></a>
