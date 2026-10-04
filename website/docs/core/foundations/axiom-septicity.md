---
sidebar_position: 2
title: Holon Requirements and Operational Definitions
description: Typed AP, PH, QG and viability assumptions with exact matrix identities
---

# Holon requirements and operational definitions

The revision of 2026-10-03 replaces the former claim that AP+PH+QG+V follow automatically from a topos with a typed model specification. These are chosen requirements and interpretation bridges, not consequences of the existence of a classifier or seven matrix coordinates. The [mathematical kernel](/docs/reference/mathematical-kernel) governs their use throughout the theory.

## Autonomy {#предварительное-условие-автономность}

First declare a system/environment tensor factorization and observation boundary. A reduced state is $\rho_S=\operatorname{Tr}_{E}\rho_{SE}$. For a quantum Markov condition use **disjoint factors** $S,B,E$ and $I(S:E\mid B)=S(SB)+S(BE)-S(B)-S(SBE)=0$. Calling $B$ both a part of $S$ and a separate factor makes the expression ill typed.

Approximate autonomy requires a specified time interval, effective generator and tolerance. A residual bound $\|\dot\rho_S-\mathcal L_S\rho_S\|\le\epsilon\omega_0\|\rho_S\|$ has consistent units. Energetic autonomy additionally needs an energy/free-energy balance with declared units; it does not follow from purity or matrix rank.

## Requirements {#ap-автопоэзис}

- **AP [P/I]:** declare a self-model $M:D_7\to D_7$ and mechanisms maintaining organization. A continuous $M$ has a fixed point by Brouwer, but arbitrary self-models need not be continuous, and a fixed point does not imply biological autopoiesis.
- **PH [P/I]**: declare an experiential realization and the interpretation linking it to observation. Population of the $E$ axis alone is a scalar. In seven dimensions it is not a tensor factor with a rank-greater-than-one reduced density matrix.
- **QG [P]:** use positive trace-one operators and a stated quantum process model. Diagonal states are valid quantum states; their status does not force nonzero frame coherences, entanglement or full rank.
- **V [D/H]:** separate structural majority from trajectory survival and from its proposed biological interpretation.

## Structural majority {#v-жизнеспособность}

For $\rho\in D_N$, $P=\operatorname{Tr}\rho^2$,

$$
P=1/N+\|\rho-I/N\|_F^2,\qquad
\|\rho-I/N\|_F^2>1/N\iff P>2/N.
$$

This exact theorem gives $2/7$ **after choosing** majority [D]. Ordinary state discrimination has advantage for every $\rho\ne I/N$; there is no universal positive purity cut. At fixed $P$, for $N\ge2$,

$$
\lambda_{\max}\le\frac{1+\sqrt{(N-1)(NP-1)}}N,
$$

with equality only when the remaining eigenvalues are equal. Neither a universal $\lambda_{\max}\approx1/2$, nor an entropy cut, nor $U(N)$ symmetry breaking independently establishes $2/N$. See the [complete threshold proof](/docs/proofs/dynamics/theorem-purity-critical).

All seven diagonal populations can be positive in a rank-one state (the uniform pure vector). Hence functional activation does not imply rank seven. Purity and rank do not establish a connected interaction graph or positive free-energy consumption. These require separate assumptions.

## Informational distinguishability {#формулировка-пир}

The matrix statement $\rho\ne I/N\iff d_B(\rho,I/N)>0$ is a metric fact [T]. Identifying distinguishability with ontological existence is PID [I/P], and is not a tautology of Kripke–Joyal semantics. A metric fact cannot imply the additional majority cut or phenomenal existence.

## $E$-share: exact algebra {#e-coherence-definition}

For the declared orthonormal frame, let $P_E=|E\rangle\langle E|$ and

$$
\pi_E(X)=P_EX+XP_E-P_EXP_E,\qquad
\mathrm{Coh}_E(\rho)=\frac{\rho_{EE}^2+2\sum_{i\ne E}|\rho_{Ei}|^2}{P}.
$$

### Hilbert–Schmidt projection [T] {#теорема-hs-проекция}

$\pi_E$ retains exactly the $E$ row and column. In the orthonormal matrix-unit basis it is a diagonal mask with entries zero or one. Hence $\pi_E^2=\pi_E=\pi_E^\dagger$ as an operator on Hilbert–Schmidt space. Therefore

$$
\mathrm{Coh}_E=\|\pi_E\rho\|_F^2/\|\rho\|_F^2\in[0,1].
$$

The image is an operator subspace, generally **not** a subalgebra, and $\pi_E$ is **not** a positive map. For $\rho=(|E\rangle+|A\rangle)(\langle E|+\langle A|)/2$, its nonzero block is $\tfrac12\begin{pmatrix}1&1\\1&0\end{pmatrix}$, whose smaller eigenvalue is $(1-\sqrt5)/4<0$. Orthogonal projection in operator space does not imply a quantum channel or a subobject of a topos.

### A genuine conditional expectation [T] {#теорема-условное-ожидание}

With $\bar P_E=I-P_E$,

$$
\mathcal E_E(X)=P_EXP_E+\bar P_EX\bar P_E
$$

is CPTP, unital, idempotent and a trace-preserving conditional expectation onto $\mathbb C\oplus M_6(\mathbb C)$. The Kraus completeness relation is $P_E+\bar P_E=I$. Its image is the block-diagonal algebra and it has the bimodule property. Orthogonality gives

$$
P=\|\mathcal E_E\rho\|_F^2+2\sum_{i\ne E}|\rho_{Ei}|^2.
$$

The two maps $\pi_E$ and $\mathcal E_E$ have different images and purposes.

### Population and coupling {#теорема-coh-e-exact}

Positivity of every $2\times2$ principal minor gives $|\rho_{Ei}|^2\le\rho_{EE}\rho_{ii}$. Thus

$$
\mathrm{Coh}_E>0\iff\rho_{EE}>0.
$$

This is a population criterion, even when every off-diagonal $E$ entry vanishes. Write $Q_E=2\sum_{i\ne E}|\rho_{Ei}|^2/P$ for the separate coupling share. At $I/7$, $\mathrm{Coh}_E=1/7$ and $Q_E=0$. A pure $E$ state has share one and zero von Neumann entropy. These scalars do not by themselves prove differentiated experience. There is no universal lower bound $\mathrm{Coh}_E\ge1/7$ on all majority states; any claimed dynamical floor needs its own model-specific proof.

For any axis $X$, the same mask construction works, but its shares overlap:

$$
\sum_X\mathrm{Coh}_X=1+q/P.
$$

### Fano-line masks {#fano-projections}

For an already chosen Fano plane, use $P_\ell=\sum_{i\in\ell}|i\rangle\langle i|$ and $\pi_\ell(X)=P_\ell X+XP_\ell-P_\ell XP_\ell$. Each mask is an orthogonal HS projection; the seven masks are **not pairwise orthogonal**. Their images contain rows and columns outside the line and are not quaternionic subalgebras. A diagonal entry is counted three times, an off-diagonal entry five times. Hence

$$
\sum_\ell\mathrm{Coh}_\ell=(3d+5q)/P=5-2/(1+\Phi),\qquad
\Phi\ge1\iff\sum_\ell\mathrm{Coh}_\ell\ge4.
$$

Since $\Phi\le6$, the sum lies in $[3,33/7]$. These are exact frame-dependent identities, not a categorical derivation of the frame.

## A rate model with declared assumptions {#структурный-анзац-kappa0}

The retained rate convention [D] is

$$
\kappa=\kappa_b+\kappa_0\mathrm{Coh}_E,\qquad
\kappa_b=\omega_0/7,\qquad
\kappa_0=\omega_0\frac{|\rho_{OE}||\rho_{OU}|}{\rho_{OO}}\quad(\rho_{OO}>0).
$$

$\omega_0>0$ is a calibrated inverse-time scale. A categorical adjunction does not define a norm on a set of natural transformations, and Yoneda does not identify a hom-space with a matrix entry. The old derivation $\|\operatorname{Nat}(\mathcal D,\mathcal R)\|=\kappa$ is withdrawn [✗]. Nor does GKSL first-order evolution imply that rates are first order in these state entries.

### A controlled kinetic approximation {#вывод-kappa0-cycle-flux}

Choose a two-state kinetic system with transition $O\to B$ at rate $a$, and two labelled transitions $B\to O$, return at $b$ and productive firing at $c$. If $p_O+p_B=1$, then

$$
\dot p_B=ap_O-(b+c)p_B,\qquad p_B^*=a/(a+b+c),\qquad J=c p_B^*=ac/(a+b+c).
$$

Thus $J=(ac/b)[1+(a+c)/b]^{-1}$ and

$$
\frac{ac/b-J}{ac/b}=\frac{a+c}{a+b+c}\le\frac{a+c}{b}.
$$

Only under rapid return $a+c\ll b$ and the additional identification $a=\omega_0|\rho_{OE}|$, $b=\omega_0\rho_{OO}$, $c=\omega_0|\rho_{OU}|$ does the leading approximation equal $\kappa_0$. The exact flux is not the product-over-occupancy formula. Other reaction networks give other laws. This replacement strengthens the kinetic claim by specifying the model and an error bound [T], while retaining the rate/coherence bridge as an assumption.

### Boundary and regularity {#обработка-сингулярности-gamma-oo}

PSD gives

$$
\frac{|\rho_{OE}||\rho_{OU}|}{\rho_{OO}}\le\sqrt{\rho_{EE}\rho_{UU}}\le1/2.
$$

The quotient is bounded but has no unique continuous extension at $\rho_{OO}=0$. Along pure states with $O$ amplitude tending to zero and nonzero $E,U$ amplitudes it tends to their product; along diagonal states it is zero. Positivity forces numerator zero at the boundary, giving $0/0$, not a proof of death. Also $P>2/7$ does not bound $\rho_{OO}$ away from zero.

For global well-posedness choose and disclose a regularization, e.g.

$$
\kappa_0^{\varepsilon}=\omega_0\frac{|\rho_{OE}||\rho_{OU}|}{\rho_{OO}+\varepsilon},\qquad\varepsilon>0,
$$

or use the exact kinetic flux with its boundary convention. Regularization changes the model; the number $0.01P_{\mathrm{crit}}$ is a numerical choice, not a theorem. A bootstrap coefficient is likewise a chosen parameter, and cannot cause genesis when multiplied by a gate that vanishes at the initial state.

## State preservation {#сохранение-положительности-s7}

For a state-preserving map $M$ and frozen $0\le\alpha\le1$, $(1-\alpha)\rho+\alpha M(\rho)$ is a state. It is a CPTP map on operators only if the complete map is affine with a CP linear extension. State-dependent coefficients do not supply this property. The invariant-cone proof for the nonlinear ODE, including local Lipschitz assumptions and global continuation, is in the [typed kernel](/docs/reference/mathematical-kernel#dynamics).

## Capability gates {#пороги-l2-строгий-вывод}

The canonical definitions are

$$
R=1/(7P),\quad\Phi=q/d,\quad
\mathrm{Cap}_2=(P>2/7)\land(R\ge1/3)\land(\Phi\ge1)\land(D_{\mathrm{diff}}\ge2).
$$

$D_{\mathrm{diff}}$ is defined for a declared experiential realization, or as an explicitly labelled proxy. The use of these cuts as consciousness criteria is a bridge [I]/[H]; algebraic identities do not validate it experimentally.

### Integration {#теорема-порог-интеграции}

The chosen coherent-majority criterion $q\ge d$ is exactly $\Phi\ge1$. Also $d\ge1/7$ implies $\Phi\le7P-1$. Therefore $\Phi\ge1$ implies $P\ge2/7$, but the converse is false, even for a pure diagonal state. Uniform diagonals give $\Phi=7P-1$; the old extension of this equality to every state is withdrawn [✗]. Coherence in a selected frame is not tensor entanglement.

### Reflection and posterior probabilities {#теорема-порог-рефлексии}

A three-hypothesis posterior $(w_1,w_2,w_3)$ has $w_1\ge\max(w_2,w_3)$ iff $w_1\ge1/3$ **under the additional equality** $w_2=w_3=(1-w_1)/2$. Equal priors alone do not imply equal posteriors. Without that equality $(0.4,0.5,0.1)$ disproves the implication. A likelihood and priors must independently justify identifying $R$ with $w_1$; none is supplied by the three displayed terms of the evolution equation.

Consequently $R_{\mathrm{th}}=1/3$ is a model definition, with a conditional Bayesian realization. Within the isotropic family $\rho_t=(1-t)I/7+tuu^\dagger$, $R$ and Bures proximity to $I/7$ are monotonically related. That does not identify either scalar with a posterior or a discrimination success probability. The family is not isospectral.

### Differentiation and the product {#теорема-порог-дифференциации}

The cut $D_{\mathrm{diff}}\ge2$ is an independent convention. A literal experiential entropy cannot be obtained by partially tracing a single basis vector out of $\mathbb C^7$: specify a tensor extension and its readout. The proxy $1+6\mathrm{Coh}_E$ may be used only under that name.

$C=\Phi R\ge1/3$ is necessary for $R\ge1/3$ and $\Phi\ge1$, but is not sufficient. For a uniform pure state $R=1/7$, $\Phi=6$, so $C=6/7$ passes while access fails. Use the conjunction, not a product gate. The first two conjuncts give $P\in(2/7,3/7]$; that interval does not guarantee the other two.

## Dimension and interpretation {#теорема-s-семимерность--следствие-из-аксиомы}

The chosen frame $(A,S,D,L,E,O,U)$ has seven orthogonal axes by definition. Functional names do not prove independence. The former unconditional Theorem S and semantic uniqueness claims are withdrawn [✗]. The [replacement minimality theorems](/docs/proofs/minimality/theorem-minimality-7) establish:

1. $N\ge7$ under perfect binary single-fault diagnosability $(\Sigma_6)$ with more than two codewords;
2. $N\ge7$ for a faithful representation of $\mathbb C\oplus M_3(\mathbb C)\oplus M_3(\mathbb C)$, with a unique minimal representation up to unitary equivalence.

Applying either premise to all autonomous or phenomenal systems is an additional physical assumption. Rosen's $(M,R)$ roles suggest a correspondence [I], not an isomorphism without specified categories, functors and inverse transformations. The octonionic channel and canonical-orientation theorems are retained with their actual inputs in the [structural derivation](/docs/proofs/minimality/theorem-octonionic-derivation).

## Historical link targets

The old proof claims at these addresses are withdrawn; their corrected scope is specified above.

<a id="coh-e-canonical"></a>
<a id="hs-projection"></a>
<a id="ph-феноменология"></a>
<a id="pi-x-generalization"></a>
<a id="qg-квантовое-основание"></a>
<a id="категориальный-вывод-kappa0"></a>
<a id="комбинированный-порог-сознательности"></a>
<a id="критическая-чистота-теорема"></a>
<a id="мост-p1p2"></a>
<a id="определение-автономная-подсистема"></a>
<a id="полнота-порогов"></a>
<a id="принцип-информационной-различимости"></a>
<a id="теорема-kappa-bootstrap"></a>
<a id="теорема-kappa0-функториальность"></a>
<a id="теорема-непротиворечивость-иерархии-определений"></a>
<a id="формализация-моста-r"></a>
