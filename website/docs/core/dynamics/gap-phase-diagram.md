---
sidebar_position: 8
title: "Gap Regimes and Conditional Phase Models"
slug: /core/dynamics/gap-phase-diagram
description: "Measured phase profiles, weighted observables, conditional bifurcations, memory kernels and symmetry tests"
---

# Gap Regimes and Conditional Phase Models

A distribution of matrix phases is an observable in a fixed semantic frame. It is not, by itself, a thermodynamic phase, cognitive level or clinical state. This page uses the [typed kernel](/docs/reference/mathematical-kernel) and corrects the old universal three-phase/swallowtail claims **[✗]**. A proposed phase model must specify dynamics, ensemble, controls and a measurement bridge.

## 1. Controls and dimensions {#параметры}

A rate ratio $r=\kappa/\Gamma_2$ is dimensionless if both are rates in the same units and $\Gamma_2>0$. A reduced temperature $t=T_{\mathrm{eff}}/T_c$ needs independently specified positive quantities with the same units. The former formulas for $T_c$, $r_c$, and a unique boundary are not consequences of $P,R,\Phi$ or the number 21. Nonlinear targets, bootstrap terms and environmental sources change the stationary equation. Their full parameter dependence must be retained.

## 2. Descriptive regimes, not three universal phases {#три-фазы}

For detected coherences $S_\eta=\{(i,j):i<j,|\gamma_{ij}|\ge\eta\}$, define

$$
g_{ij}=|\operatorname{Im}\gamma_{ij}|/|\gamma_{ij}|,\quad
W=\sum_{i\ne j}|\gamma_{ij}|^2,\quad A_\eta=\operatorname{Var}_{S_\eta}(g_{ij}).
$$

The amplitude threshold and empty-support convention must be stated. A detection mask is not inferred as zero phase. Choose $w_0,a_0$ and optionally describe:

| Descriptive regime [D] | Declared test |
|---|---|
| Nonuniform supported profile | $W>w_0$, $A_\eta>a_0$ |
| Nearly uniform supported profile | $W>w_0$, $A_\eta\le a_0$ |
| Low coherent weight | $W\le w_0$ |

If support data are inadequate, return unknown. These tests neither prove symmetry breaking nor distinguish spontaneous thermodynamic phases. They do not imply awareness of blind spots, dissociation or death. A pure diagonal state has $W=0$ and $P=1$: loss of off-diagonal weight alone does not imply loss of the purity gate, although the integration gate fails.

A continuous weighted observable is

$$
J^2:=\|\operatorname{Im}\Gamma\|_F^2=2\sum_{i<j}|\gamma_{ij}|^2g_{ij}^2.
$$

It distinguishes phase power from amplitude-free means and remains continuous when a coherence vanishes. All-zero phases can occur both inside and outside $\mathsf{Cap}_2$; see [the exact counterexample](/docs/consciousness/hierarchy/gap-characterization#gap-инъекция).

**Random-phase calculation [T under a declared distribution].** If a selected phase is uniform on $[0,2\pi)$, its Gap has density

$$
p(g)=\frac{2}{\pi\sqrt{1-g^2}},\quad0<g<1,
$$

mean $2/\pi$ and variance $1/2-4/\pi^2$. Uniform phase does not give uniform Gap. Equal time averages across channels need a common stationary law and ergodicity; thermalisation or invariance under general $G_2$ rotations does not follow from that equality.

## 3. Clinical correspondence is an empirical bridge {#клиническое-соответствие}

The former assignments of regimes to coma, dementia, psychosis, dissociation and clinical death are hypotheses **[H]**, not diagnoses from a static scalar. A test requires independent clinical labels, longitudinal measurements, an identifiable reconstruction model, relevant confounders and held-out validation. The physical-to-phenomenal bridge remains separate **[I]**. No patient measurements or treatment outcomes are established by this page.

## 4. Verified dynamical bifurcations {#бифуркации}

Find equilibria of the specified flow on the trace-one tangent space and compute its Jacobian. A saddle-node needs a simple zero eigenvalue, nonzero quadratic centre coefficient and transverse parameter variation. A Hopf bifurcation needs a simple imaginary eigenvalue pair, transverse crossing and a Lyapunov-coefficient calculation. A pitchfork requires the appropriate exact symmetry and nondegeneracy. None follows from a crossing of $P=2/7$ or a phase-variance threshold.

## 5. Catastrophes and level labels {#катастрофы-уитни}

A scalar smooth gradient reduction and the explicit degeneracy/unfolding hypotheses are needed. The $A_4$ potential $x^5/5+a x^3/3+b x^2/2+c x$ has a quartic derivative and at most **two** nondegenerate interior minima, not three. A confining even sextic can have three minima in some parameter regimes; its tricritical germ is $A_5$. Three controls alone do not select either model.

Sheets and stationary roots receive no L-label from the normal form. L2 uses the full $\mathsf{Cap}_2$ and typed differentiation; L3 additionally uses independent metamodel tests. A fixed point is not L4. Full corrected prerequisites, discriminants and conditional exponents: [transition models](/docs/consciousness/hierarchy/swallowtail-transitions).

## 6. Memory: a solvable conditional linear model {#немарковские-осцилляции}

For a **signed fluctuation** $x$ around a declared stationary point, consider

$$
\dot x(t)=-\int_0^tK(t-s)x(s)\,ds+f(t)+\xi(t).
$$

This linear equation is a model **[D]**, not an equation for a bounded absolute phase globally. With Fourier convention $e^{i\omega t}$, a stationary causal response has

$$
\chi(\omega)=\frac1{-i\omega+\widetilde K(\omega)},\qquad S_x(\omega)=|\chi(\omega)|^2S_\xi(\omega).
$$

The second identity assumes a stationary linear response and a specified noise spectrum. A fluctuation–dissipation relation further requires the equilibrium/noise assumptions and its precise convention; an arbitrary memory kernel does not supply them.

For $K(t)=(a/\tau)e^{-t/\tau}$, $a,\tau>0$, introduce $y(t)=\int_0^tK(t-s)x(s)ds$. In the homogeneous equation,

$$
\dot x=-y,\quad\dot y=(a x-y)/\tau,\quad
\ddot x+\dot x/\tau+a x/\tau=0.
$$

Its eigenvalues are $[-1\pm\sqrt{1-4a\tau}]/(2\tau)$ **[T]**. Oscillation requires $4a\tau>1$; the other cases are critical/overdamped. This makes no therapeutic frequency recommendation or universal neuronal prediction.

**Frequency correction.** For diagonal unitary dynamics $\gamma_{ij}(t)=e^{-i(\omega_i-\omega_j)t}\gamma_{ij}(0)$, the supported Gap follows the corresponding absolute sine **[T]**. The tuple $(0,1,2,3,5,8,13)$ has integer differences: all nonzero frequency ratios are rational and all profiles share a period. The limit of Fibonacci-number ratios does not make this finite tuple irrational. Arbitrary phases need not simultaneously become zero, but fully real stationary states show that total phase transparency is possible. Quasiperiodic laws require genuinely incommensurate frequencies and retain the nonlinear Gap distribution above.

## 7. Conditional critical phenomena {#критические-явления}

An explicitly tuned even sextic mean-field potential gives $\beta=1/4,\gamma=1,\delta=5,\alpha=1/2$; an ordinary positive-quartic Landau model gives its own mean-field values. The parameter-to-temperature and state-to-order-parameter maps must be nonsingular and specified. A spatial correlation length additionally needs a spatial field and gradient term. Exactness for a physical model requires fluctuation and finite-size control. Internal mode count 21 is not spatial dimension, and deterministic flow does not prove universal exactness. See corrected [T-161](/docs/consciousness/hierarchy/swallowtail-transitions#критические-экспоненты).

## 8. Symmetry and linearised modes {#голдстоуновские-моды}

For the **actual matrix** $A=\operatorname{Im}\Gamma\in\mathfrak{so}(7)$, rank is $0,2,4,6$. The frame-indexed absolute phase array does not transform by this adjoint representation.

### Stabiliser of a specified tensor {#стабилизатор-gap}

If an actual tensor $A_*$ carries the adjoint action, define

$$
H_{A_*}=\{g\in G_2:gA_*g^{-1}=A_*\},\qquad\dim(G_2/H_{A_*})=14-\dim H_{A_*}.
$$

This orbit-dimension identity is **[T]**. Rank alone does not determine $H$ or the number of dynamical modes. A global symmetry must be proved for the action/generator and distinguished from a gauge redundancy or an explicit semantic frame.

**Conditional zero-mode statement [T].** For a differentiable equivariant vector field $F$ with $F(A_*)=0$, differentiating $F(gA_*g^{-1})=0$ along the orbit gives

$$
DF(A_*)[T,A_*]=0.
$$

Thus independent orbit tangents are Jacobian zero directions. A symmetry-breaking term may lift them, but its rates/frequencies come from the full Jacobian. No universal mass, 6/10/12-mode table or fMRI frequency follows from phase rank. A finite system's symmetry orbit is not automatically a thermodynamic spontaneously broken phase.

## 9. Claims of unavoidable Gap {#защита-gap}

Hamming bounds count code redundancy, associators describe a specified nonassociative algebra, an energy barrier needs a potential and separated sets, and homotopy classes classify spatial maps with boundary data. Lawvere's theorem has its own representability/diagonal assumptions. None separately or together proves a nonzero phase floor for every seven-dimensional state. The positive real $\Gamma(t)$ family supplies a direct all-zero-phase counterexample. See [Gap identifiability](/docs/consciousness/hierarchy/gap-characterization) and [actual energy-separation theorem](./composite-systems#теорема-тополог-защита).

## 10. Correct symmetry tests {#тождества-уорда}

For a specified real linear representation $D(g)$ on an observable vector $X$ and an invariant probability law with finite second moments, its covariance obeys

$$
C=D(g)CD(g)^T,\qquad A_aC+CA_a^T=0,
$$

where $A_a=dD(T_a)$ **[T]**, by differentiating invariance. These are equations whose independent rank must be computed; 14 generators do not subtract exactly 14 scalar degrees of freedom. For example, in the irreducible real seven-vector representation, invariant symmetric covariance is a multiple of the identity, leaving one parameter rather than $28-14$.

Absolute pairwise Gap is not automatically the linear representation used in these identities. Its induced law may be tested by nonlinear pushforwards, with an identified observation model. Passing finitely many covariance equations does not establish invariance of every distribution or prove that the biological encoder is unique. The former count 217 and universal phase-Ward equations are **withdrawn [✗]**.

## Related documents

- [Typed kernel](/docs/reference/mathematical-kernel)
- [Gap definition and identification](/docs/consciousness/hierarchy/gap-characterization)
- [Conditional transition models](/docs/consciousness/hierarchy/swallowtail-transitions)
- [Composite systems](./composite-systems)
