---
sidebar_position: 3
title: Viability
description: Structural-majority criterion, dynamical viability and the full consciousness predicate
---

# Purity and Viability

Purity is a spectral statistic of a density matrix. UHM chooses $P>2/7$ as its **structural-majority criterion**; remaining in that set is a separate dynamical problem. Neither the chosen criterion nor positive state reconstruction by itself establishes biological life or experience. The precise separation of definitions, mathematical consequences and empirical bridges is fixed in the [mathematical kernel](/docs/reference/mathematical-kernel#thresholds).

## Definition of purity {#определение-чистоты}

For $\Gamma=\Gamma^\dagger\succeq0$, $\operatorname{Tr}\Gamma=1$ on $\mathbb C^7$,

$$
P(\Gamma)=\operatorname{Tr}(\Gamma^2)=\sum_i\gamma_{ii}^2+\sum_{i\ne j}|\gamma_{ij}|^2=\sum_kp_k^2.
$$

A pure basis state has $P=1$ but zero off-diagonal coherence. Purity must not be confused with frame-dependent integration $\Phi$ or with system functionality.

## Range of values

$$
\frac17\leq P\leq1.
$$

The lower equality holds exactly at $I/7$ and the upper exactly at rank-one states. These are algebraic statements [T], not labels of physiological or psychological conditions. Numerical assignments such as “flow means $P>0.7$” or “psychosis means $P<2/7$” require an independently validated measurement bridge and are not asserted here.

## Relation to entropy {#связь-с-энтропией}

$$
S(\Gamma)=-\sum_kp_k\log p_k,\qquad -\log P\leq S(\Gamma)\leq\log7.
$$

The lower bound follows from Jensen's inequality applied to $-\log p_k$ with weights $p_k$; zero eigenvalues contribute zero by continuity. Purity and von Neumann entropy do **not** have a universal inverse-monotone relation in dimension seven. For example, spectra $(1/2,1/2,0,\ldots,0)$ and $(0.7,0.05,\ldots,0.05)$ have respectively $(P,S)=(0.5,\log2)$ and $(0.505,\approx1.1484)$: both purity and entropy increase. Along specified majorization chains purity decreases while entropy increases; arbitrary state pairs need not be comparable.

## Critical purity: structural-majority definition {#критическая-чистота}

Let $\Delta=\Gamma-I/N$. Orthogonality of the identity and traceless parts gives

$$
\|\Gamma\|_{\mathrm{HS}}^2=\|I/N\|_{\mathrm{HS}}^2+\|\Delta\|_{\mathrm{HS}}^2=\frac1N+\|\Delta\|_{\mathrm{HS}}^2.
$$

### Derivation relative to the declared criterion {#вывод-pcrit}

**Definition [D, Vdef].** Structural majority means $\|\Delta\|_{\mathrm{HS}}^2>\|I/N\|_{\mathrm{HS}}^2$. Given this definition,

$$
\|\Delta\|_{\mathrm{HS}}^2>\frac1N\quad\Longleftrightarrow\quad P>\frac2N.
$$

Thus $P_{\mathrm{crit}}=2/7$ is an exact consequence **of that criterion** [T]. The identity contribution is a reference weight; calling it measured thermal-noise power requires a separate statistical noise model. No comparison of a squared distance with an unsquared distance is permitted. The identification of structural majority with biological viability is [H]/[I], not a further consequence of the norm decomposition. See the corrected [purity theorem](/docs/proofs/dynamics/theorem-purity-critical).

### Bures geometry does not give an exact purity conversion

Choose the usual convention $d_B^2(\rho,\sigma)=2-2\operatorname{Tr}\sqrt{\sqrt\rho\sigma\sqrt\rho}$. Then

$$
d_B^2(\Gamma,I/N)=2-\frac2{\sqrt N}\sum_k\sqrt{p_k}.
$$

This depends on more than $P$. The seven-component spectra $(1/2,1/2,0,\ldots,0)$ and $(2/3,1/6,1/6,0,\ldots,0)$ have the same $P=1/2$ but different Bures distances to $I/7$. Consequently a universal equivalence $P>2/7\iff d_B>d_B^{\mathrm{noise}}$ is not proved by the purity identity. A Bures noise threshold requires its own noise law and calibration, or a restriction to a specified spectral family. On the actual surface $P=2/7$, spectra $(a_\pm,b_\pm,b_\pm,b_\pm,0,0,0)$ with $a_\pm=(1\pm\sqrt{3/7})/4$, $b_\pm=(1-a_\pm)/3$ also give different Bures distances. Thus one constant Bures radial boundary cannot be identified with the entire critical purity surface.

Bures is a particular monotone quantum metric; monotonicity does not uniquely select it. [Petz and Sudár, *Extending the Fisher metric to density matrices*](https://arxiv.org/abs/quant-ph/0102132) describe the operator-monotone family. This geometric choice does not identify a neural encoder; that requires the [observation-model analysis](/docs/applied/research/reconstruction-identifiability).

### Temporal interpretation

If an internal-clock model sets its rate proportional to $(P-P_{\mathrm{crit}})_+^{1/2}$, clock freezing below threshold follows from that specified clock law. It is not independently implied by purity, distinguishability or existence of a density matrix. External evolution can remain defined below the threshold. Link to the [emergent-time model](/docs/proofs/dynamics/emergent-time) only with its clock/dynamical premises stated.

## Static membership and dynamical viability {#viability-kernel}

The static predicate is

$$
\mathrm{Viable}_{\mathrm{static}}(\Gamma):=P(\Gamma)>2/7.
$$

Specify dynamics $\dot\Gamma=f(\Gamma,u,w)$, admissible controls $u$, disturbances $w$, initial state, time horizon and existence of state-preserving solutions. For a declared margin $0<\varepsilon<5/7$ define the closed constraint set $K_\varepsilon=\{\Gamma:P\geq2/7+\varepsilon\}$. Robust dynamical viability is

$$
\mathrm{Viab}_{f,\mathsf U,\mathsf W}(K_\varepsilon)=\{\Gamma_0\in K_\varepsilon:\exists\text{ admissible causal policy }u\ \forall w,\ \Gamma(t)\in K_\varepsilon\ \forall t\geq0\}.
$$

Without controls this reduces to states whose actual trajectories remain in the constraint set. Quantifier order matters: a policy cannot depend on future disturbances. This is a stronger formalization than a one-time purity check; it follows the controlled-invariance approach of [Aubin, *Viability Kernels and Capture Basins of Sets Under Differential Inclusions*](https://doi.org/10.1137/S036301290036968X).

**Counterexample to static sufficiency.** Depolarizing dynamics $\dot\Gamma=\gamma(I/7-\Gamma)$, $\gamma>0$, gives

$$
P(t)=\frac17+\left(P(0)-\frac17\right)e^{-2\gamma t}.
$$

Any $P(0)>2/7$ crosses the static boundary at finite time $t_*=(2\gamma)^{-1}\log(7P(0)-1)$. A state can therefore pass the static criterion and fail dynamical viability. Regeneration rates, resource supply, choice of $\varphi$, disturbances and control limits are material premises, not determined by the inequality alone.

## Viability domain {#область-жизнеспособности}

### Minimal static domain {#минимальная-жизнеспособность}

$$
\mathcal V_P=\{\Gamma\in\mathcal D(\mathbb C^7):P>2/7\}.
$$

This is relatively open in the state space; its relative boundary is $P=2/7$. Unindexed $\mathcal V$ elsewhere denotes this **static** set unless a dynamical kernel is explicitly stated.

### Full constraint domain {#полная-жизнеспособность}

For explicitly defined dimensionless stress functions, retain

$$
\mathcal V_{\mathrm{full}}=\{\Gamma:\|\sigma_{\mathrm{sys}}(\Gamma)\|_\infty<1\}.
$$

This is another static constraint set. Its nonemptiness, relation to the consciousness predicate and invariance require the actual stress functions and any extensions used to define them. They do not follow from the symbol $\sigma$ alone.

#### Conditional embedding theorem [T] {#теорема-вложение-областей}

If the stress definition includes $\sigma_U=2/(1+\Phi)$, then $\mathcal V_{\mathrm{full}}\subsetneq\mathcal V_P$: membership implies $\Phi>1$ and hence

$$
P=(1+\Phi)\sum_i\gamma_{ii}^2>2/7
$$

by Cauchy–Schwarz. The pure basis state has $P=1$, $\Phi=0$, $\sigma_U=2$ and witnesses proper inclusion. This proof uses the stated stress convention; it does not prove that every point of either set is dynamically viable.

### Invariance and positivity preservation

:::info Sufficient barrier criterion [T with stated dynamics]
Assume global state-preserving solutions and an admissible policy for which, along all permitted disturbances and while the trajectory is in the constraint neighborhood,

$$
\dot P\geq-a(t)(P-2/7-\varepsilon),\qquad a\geq0,\quad a\in L^1_{\mathrm{loc}}.
$$

For $m=P-2/7-\varepsilon$, Grönwall's inequality gives $m(t)\geq m(0)e^{-\int_0^ta(s)ds}$. Thus $m(0)\geq0$ cannot cross below zero at finite time; the declared policy certifies dynamical viability. A purity derivative at **one** state is insufficient. Control and disturbance assumptions must make the inequality hold on the relevant trajectories.
:::

An alternative boundary tangent-cone proof requires the regularity and tangency hypotheses of the applicable invariance theorem; “regeneration $\geq$ dissipation” is not an order between matrix-valued vector fields until converted into a precise scalar or tangent condition.

The finite step

$$
\Gamma'=(1-\alpha)\mathcal E(\Gamma)+\alpha\varphi(\Gamma),\qquad0\leq\alpha\leq1
$$

preserves PSD and trace-one if $\mathcal E(\Gamma)$ and $\varphi(\Gamma)$ are states. $\mathcal E$ may be CPTP; a nonlinear $\varphi$ need only be a specified state-valued map for this argument. Positivity of the step neither makes the full nonlinear evolution a linear CPTP channel nor guarantees $P>2/7$.

The current canonical $\varphi_{\mathrm{coh}}$ with anchor $I/7$ has its unique fixed point at $I/7$, with $P=1/7$; the former claim of a fixed point at $2/7$ is false. Alternative nonunital/state-dependent anchors can support different regimes only under their stated assumptions. See [operator φ](/docs/core/operators/phi-operator).

**Noise:** a second-moment bound alone cannot establish an exponential survival probability. For a single perturbation $Z$, Markov's inequality gives $\Pr(\|Z\|\geq r)\leq\mathbb E\|Z\|^2/r^2$. Exponential bounds require specified tail assumptions; survival over a time interval additionally requires pathwise/maximal estimates. Infinite-time survival cannot be inferred from a single-time concentration bound.

## Purity dynamics {#динамика-чистоты}

$$
\dot P=2\operatorname{Tr}(\Gamma\dot\Gamma).
$$

The Hamiltonian commutator contributes zero. For regeneration $\kappa(\varphi(\Gamma)-\Gamma)$ with $\kappa\geq0$,

$$
\dot P_{\mathcal R}=2\kappa\big(\operatorname{Tr}(\Gamma\varphi(\Gamma))-P\big).
$$

Its sign depends on the target; it is not automatically positive. Unital CPTP dynamics cannot increase purity, but general nonunital dissipative dynamics can: amplitude damping towards a pure state is a counterexample. Thermodynamic resource availability alone does not determine either sign.

## Conditional irreversible decay {#условие-смерти}

Assume the regeneration gate is zero below $2/7$, the remaining generator is fixed, **unital and primitive**, and there is no external purification or change of rates. Then purity is nonincreasing, the subthreshold set is forward invariant, and the state converges to $I/7$. These assumptions define a decay regime; $P<2/7$ together with $\dot P<0$ at one instant is not sufficient for irreversible decay under arbitrary dynamics. Landauer's principle alone does not force the gate to switch off at a universal purity.

For a finite-dimensional nonnormal generator with spectral gap $g>0$, a generally valid estimate is $\|\Gamma(t)-I/7\|\leq C_\eta e^{-\eta t}\|\Gamma(0)-I/7\|$ for every $0<\eta<g$, with a generator-dependent constant. The prefactor-one bound with the eigenvalue gap requires stronger contractivity/coercivity; it does not follow from the spectral theorem for a general superoperator. A sufficient Hilbert–Schmidt condition is $\operatorname{Re}\langle\Delta,\mathcal L_0\Delta\rangle\leq-\eta\|\Delta\|^2$ for all traceless $\Delta$.

“Death” is an ontological interpretation of this declared decay regime, not a clinically established readout. It supplies no conclusion about what the system experiences.

## Numerical examples {#числовой-пример-жизнеспособность}

A diagonal state with spectrum $(0.48,0.20,0.12,0.08,0.06,0.04,0.02)$ has $P=0.2968>2/7$, but $\Phi=0$: it passes structural majority and fails integration. The maximally mixed state has $P=1/7$. Neither numerical fact determines the system's future without dynamics.

The uniform family $\Gamma(t)=(1-t)I/7+tuu^\dagger$, $u=(1,\ldots,1)/\sqrt7$, $0\leq t\leq1$, has

$$
P=(1+6t^2)/7,\qquad\Phi=6t^2,\qquad R=1/(1+6t^2).
$$

At $t=0.45$, $(P,\Phi,R)\approx(0.31643,1.215,0.45147)$. This satisfies the first three formal consciousness conditions; differentiation still requires its specified definition/extension and measurement.

## Four formal conditions of consciousness {#четыре-условия-сознания}

The selected predicate is

$$
\mathrm{Cons}(\Gamma)=(P>2/7)\wedge(R\geq1/3)\wedge(\Phi\geq1)\wedge(D\geq2).
$$

Thresholds are model criteria [D]; their algebraic consequences are [T]; their identification with phenomenal consciousness is [I]/[H]. With the canonical $R=1/(7P)$ the first two imply the purity window $(2/7,3/7]$. The window alone is insufficient: integration and differentiation remain separate conjuncts. $D$ must specify the extension/lift or subsystem used; it is not recovered from seven-dimensional purity alone.

The exact implication $\Phi\geq1\Rightarrow P\geq2/7$ follows from $P=(1+\Phi)\sum_i\gamma_{ii}^2$ and $\sum_i\gamma_{ii}^2\geq1/7$. It is **one-way** and weak at the boundary. A diagonal state can have $P>2/7$ and $\Phi=0$. A product summary $C=\Phi R$ cannot replace the conjunction: the uniform state with $\Phi=3$ has $P=4/7$, $R=1/4$, $C=3/4$, but fails reflection. Large $C$ therefore does not certify $\mathrm{Cons}$.

When reconstructing from data, use the [confidence-set and identification rules](/docs/applied/research/reconstruction-identifiability#uncertainty). A verdict is determined only if the predicate is constant over the compatible states and all declared extensions. A missing phase or differentiation observation must not be replaced by a preferred value to make the verdict pass.

## Octonionic norm {#октонионная-норма}

The multiplicative norm of $\mathbb O$ is a statement about octonion vectors/products. Purity is the Hilbert–Schmidt norm squared of a matrix. Relating them requires an explicit representation map and proof of which norms/observables it preserves. An octonionic interpretation does not independently derive the structural-majority threshold or its biological meaning.

**Related documents:** [mathematical kernel](/docs/reference/mathematical-kernel#thresholds), [purity theorem](/docs/proofs/dynamics/theorem-purity-critical), [coherence matrix](/docs/core/dynamics/coherence-matrix), [evolution](/docs/core/dynamics/evolution), [operator φ](/docs/core/operators/phi-operator), [reconstruction and identifiability](/docs/applied/research/reconstruction-identifiability).
