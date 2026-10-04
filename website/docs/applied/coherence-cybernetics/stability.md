---
sidebar_position: 19
title: "Stability Analysis"
description: "Homeostatic regime, basin of attraction, death spiral, perturbation bounds, parametric sensitivity"
---

# Stability: geometric margins and controlled dynamics

:::warning Mathematical revision — 2026-10-03
Distance to a static boundary, equilibrium stability and controlled recovery are different problems. T-104 provides no universal allowable decoherence-rate change or guaranteed therapy. The selected T-92 panel [D] is not equivalent to the full window; universal three-channel completeness T-102 is withdrawn [✗].
:::

## 1. Objects and units

The state $\rho\in\mathcal D_7$, $P=\mathrm{Tr}\rho^2$, $R=1/(7P)$ and $\Phi=P/d-1$, $d=\sum_i\rho_{ii}^2$, are specified in a fixed frame. Kinetic rates have inverse-time units. State distance is dimensionless; comparing it with a rate perturbation requires a sensitivity model. Extended $D_{\mathrm{diff}}$ needs its own definition and data.

The cut $p_c=2/7$ is the selected HS-majority convention [D]. Its identification with biological survival or consciousness requires a separate bridge. The exact window has four margins: $P-2/7$, $3/7-P$, $\Phi-1$, $D_{\mathrm{diff}}-2$. One margin does not replace the others.

## 2. Exact geometric distance

**[T at the selected purity boundary].** For $P(\rho)>p_c>1/7$, Hilbert–Schmidt distance to $\{\sigma\in\mathcal D_7:P(\sigma)=p_c\}$ is

$$
r_{\mathrm{HS}}(\rho)=\sqrt{P(\rho)-1/7}-\sqrt{p_c-1/7}.
$$

**Proof.** For $X=\rho-I/7$, $\|X\|_2^2=P-1/7$. The reverse triangle inequality gives the lower bound. It is attained by

$$
\sigma=I/7+t(\rho-I/7),\quad t=\sqrt{\frac{p_c-1/7}{P-1/7}}\in(0,1),
$$

a convex mixture of states with the required purity. Thus the bound is exact for every state, including boundary states. This is geometry, not an attractor theorem.

Every admissible state change with $\|\delta\rho\|_2<r_{\mathrm{HS}}$ preserves $P>p_c$. A simpler sufficient estimate is $|P(\rho)-P(\sigma)|\le2\|\rho-\sigma\|_2$.

## 3. T-104: Bures distance and formula scope

Define [D]

$$
r_B(\rho)=\min_{P(\sigma)=p_c}d_B(\rho,\sigma),\qquad d_B^2=2(1-\mathrm{Tr}\sqrt{\sqrt\rho\sigma\sqrt\rho}).
$$

The minimum exists by compactness and continuity. The former $r_B=\sqrt{P-p_c}$ is withdrawn [✗]. A general certified lower bound is

$$
r_B\ge r_{\mathrm{HS}}/\sqrt2.
$$

For traceless Hermitian $X=X_+-X_-$, let $T=\mathrm{Tr}X_+=\mathrm{Tr}X_-$. Then $\|X\|_2^2\le2T^2$. Fuchs–van de Graaf gives $T\le\sqrt{1-F}\le d_B$, proving the estimate without spectral assumptions.

In the family $\rho_a=\mathrm{diag}(a,(1-a)/6,\ldots,(1-a)/6)$, $a\ge1/7$, a radial boundary candidate has $a_c=(1+\sqrt6)/7$. Distance to **this candidate** is

$$
d_B(\rho_a,\rho_{a_c})=\sqrt{2(1-\sqrt{aa_c}-\sqrt{(1-a)(1-a_c)})}.
$$

This is an upper bound on $r_B$ unless global optimality of the candidate is separately proved. Agreement with numerical optimization on a finite grid is not that proof. For $a_c<a<1$, the candidate’s expansion starts with $r^2=(49\sqrt6/80)(P-2/7)^2$; general $r_B$ is not determined by purity alone.

## 4. Trajectory stability under field perturbations

**[T under explicit regularity hypotheses].** Suppose $\dot\rho=F(\rho,t)$ and $\dot\sigma=\widetilde F(\sigma,t)$ preserve the density domain, $F$ is $L$-Lipschitz in norm2, and $\|F(x,t)-\widetilde F(x,t)\|_2\le\eta(t)$ on the relevant region. Then

$$
\|\rho(t)-\sigma(t)\|_2\le e^{Lt}\|\rho(0)-\sigma(0)\|_2+\int_0^t e^{L(t-s)}\eta(s)\,ds.
$$

This is Grönwall’s inequality. For constant $\eta$, the second term is $\eta(e^{Lt}-1)/L$; for $L=0$ it is $\eta t$. If the right side stays below the reference trajectory’s minimum geometric margin on $[0,T]$, the perturbed trajectory stays above the selected boundary throughout that interval. This needs a margin **along the trajectory**, a time horizon and measured constants, not initial purity alone.

For $\delta=\|\rho-\sigma\|_2$, bounds $|\delta P|\le2\delta$, $|\delta R|\le14\delta$, $|\delta\Phi|\le112\delta$ supply sufficient conditions for retaining the first three gates. The fourth requires stability of its extended readout. These conservative estimates do not classify clinical states.

## 5. Local and exponential stability

For $F(\rho_*)=0$, analyze $DF(\rho_*)$ on the traceless Hermitian tangent space of the full differentiable field. On the cone boundary also check invariance and admissible directions. Primitivity of a frozen linear generator does not establish stability of arbitrary nonlinear feedback.

If $\langle x-y,F(x)-F(y)\rangle\le-\alpha\|x-y\|_2^2$, $\alpha>0$, is proved, trajectory distance decays as $e^{-\alpha t}$. Under a field perturbation bounded by $\eta$,

$$
\|\rho(t)-\sigma(t)\|_2\le e^{-\alpha t}\delta_0+\eta(1-e^{-\alpha t})/\alpha.
$$

This is a sufficient return-to-neighborhood condition, not a consequence of the word “regeneration.” A stable linear matrix generally needs an estimate $K e^{-\alpha t}$ with $K\ge1$: non-normality permits transient growth.

## 6. Purity flux and recovery

For the selected field $\dot\rho=-i[H,\rho]+\mathcal D(\rho)+a(\rho,t)(\sigma(\rho,t)-\rho)$, $a\ge0$, $\sigma\in\mathcal D_7$, exactly

$$
\dot P=2\mathrm{Tr}(\rho\mathcal D\rho)+2a\bigl(\mathrm{Tr}(\rho\sigma)-P\bigr).
$$

The Hamiltonian contribution vanishes. Injection may increase, decrease or preserve purity. Normalized Fano dephasing $\mathcal D\rho=-(2\gamma/3)\rho_{\mathrm{off}}$ contributes $-(4\gamma/3)\|\rho_{\mathrm{off}}\|_2^2$. An arbitrary non-unital GKSL term has a different sign.

In the selected $a=\kappa g_V(P)$ model with $g_V=0$ below the cut, the closed baseline generator keeps $I/7$ fixed. A positive constant $\kappa_b=\omega_0/7$ [D] does not automatically produce viability: a closed gate or coinciding target makes injection vanish. Crossing needs a specified external drive or different gate model. Medical necessity does not follow from this scheme.

## 7. Entropy, power and topology

A unital quantum semigroup does not decrease entropy, but Fano dephasing fixes every diagonal state; strict positive entropy flux for every $\rho\ne I/7$ is false. Injection is not universally negentropic. Landauer’s principle needs physical erasure, a reservoir and specified entropy units; a software matrix does not determine device power.

$\pi_2(G_2/T^2)=\mathbb Z^2$ concerns maps from a space with two-dimensional topology into the corresponding order-parameter space. A single finite matrix has no such topological charge. An energy barrier needs a field configuration, boundary conditions and an energy functional. Continuous ODEs give continuous purity, but do not guarantee sufficient intervention time.

## 8. Practical protocol

1. Specify state, frame, readout and uncertainty set.
2. Compute geometric margins and analyze dynamic stability separately.
3. Specify admissible controls, constraints and loss.
4. Check density preservation, reconstruction error and numerical error.
5. Test recovery on independent perturbations, including transient growth and a closed gate.

Compact feasible sets and continuous losses guarantee existence of a minimizer; uniqueness and global safety require additional hypotheses. Applications remain a test programme [H/Pr].

See [viability](/docs/core/dynamics/viability), [evolution](/docs/core/dynamics/evolution), [identifiability](/docs/applied/research/reconstruction-identifiability) and the [density-preserving implementation](./implementation).

<a id="гомеостаз-как-системы-сохраняют-себя"></a>
<a id="гомеостатический-режим"></a>
<a id="бассейн-притяжения"></a>
<a id="радиус-стабильности-сколько-система-может-выдержать"></a>
<a id="радиус-устойчивости"></a>
<a id="числовой-пример-r-stab"></a>
<a id="спираль-смерти-каскад-разрушения"></a>
<a id="спираль-смерти"></a>
<a id="время-жизни"></a>
<a id="границы-пертурбации"></a>
<a id="параметрическая-чувствительность"></a>
<a id="энергетический-метаболизм"></a>
<a id="энергетический-баланс"></a>
<a id="метаболические-режимы"></a>
<a id="три-метаболических-режима"></a>
<a id="диагностика-нестабильности-реализации"></a>
<a id="критерии-восстановления"></a>
<a id="антихрупкость-и-посттравматический-рост"></a>
<a id="устойчивость-ии-систем"></a>
<a id="резюме"></a>
<a id="что-мы-узнали-стабильность"></a>

[Fuchs–van de Graaf, primary paper](https://arxiv.org/abs/quant-ph/9712042).
