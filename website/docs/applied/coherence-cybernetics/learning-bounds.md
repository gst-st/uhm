---
sidebar_position: 25
title: "Conditional Learning Bounds"
description: "Exact discrimination, selected signal dynamics, safety certificates and the scope of seven-dimensional learning"
---

# Conditional Learning Bounds

:::info Scope and correction, 2026-10-03
The bounds depend on an observation experiment, task, learner and admissible dynamics. T-113's universal seven-dimensional minimum is withdrawn; a seven-role architecture remains a hypothesis [H]. T-263 gives a local metric statement under fixed premises, not a uniquely best learning algorithm. The previous finite-sample Chernoff inequality had its direction reversed, and the maximum of lower bounds was incorrectly identified with an attained optimum.
:::

Specify what is being learned, what one observation contains and what success means. A software coherence matrix does not by itself turn classical examples into independent quantum copies. The [reconstruction protocol](/docs/applied/research/reconstruction-identifiability) distinguishes identifiable data targets from arbitrary encoders; T-42a supplies no universal canonical encoder.

## 1. Formal definition of the learning task {#определение-задачи}

### 1.1 Learning task for the holon

Let a task have hypotheses $\theta\in\Theta$, an observation law $p_\theta$, a prior or a specified worst-case criterion, allowed observation/decision policies and a loss. A learner uses observations to update a declared state or parameters. Its required sample count $n_*(\delta)$ is the smallest count achieving the **registered** risk at most $\delta$. State validity, computational cost and safety are additional constraints. Counts of observations, physical time and optimization iterations have different units.

### 1.2 Criterion for successful learning {#критерий-обучения}

Use independent held-out data for performance and frozen readouts for the [full Cap₂ predicate](/docs/reference/mathematical-kernel#thresholds). Classification accuracy, a matrix predicate and phenomenal interpretation are separate claims. Calibrating an encoder with the evaluation labels changes the experiment and invalidates the originally registered risk.

### 1.3 Learning as attractor update {#обучение-как-аттрактор}

An update of $\varphi$, the observation model or a policy is a model choice [D/H]. It need not be an attractor update, and an attractor needs an actual stability proof. Frozen-target replacement is linear CPTP; state-dependent feedback generally produces a nonlinear state map. Purity of the target alone does not guarantee that regeneration raises current purity.

## 2. Information bounds (T-109) [T under the stated experiment] {#информационная-граница}

#### T-109: exact binary discrimination and Chernoff scope {#теорема-информационная-граница}

For equal priors and $n$ i.i.d. copies of **known physical quantum states** $\rho_0,\rho_1$, allowing all collective POVMs, the Helstrom optimum is

$$
p_e^*(n)=\frac12-\frac14\|\rho_0^{\otimes n}-\rho_1^{\otimes n}\|_1.
$$

Therefore every test with error at most $\delta$ must satisfy $p_e^*(n)\le\delta$. This is an exact finite-sample criterion. Restricted measurements can require more copies.

Define $Q=\inf_{0\le s\le1}\operatorname{Tr}\rho_0^s\rho_1^{1-s}$, $\xi=-\log Q$. For $0<Q<1$, quantum Chernoff gives

$$
p_e^*(n)\le\tfrac12 Q^n,\qquad\lim_{n\to\infty}-\frac1n\log p_e^*(n)=\xi.
$$

Thus $n\ge\lceil\log(1/(2\delta))/\xi\rceil$ is **sufficient** for the unrestricted optimal test, not the former necessary lower bound. The exponent is asymptotically optimal; it does not supply an exact finite-sample equality. See [Audenaert et al.](https://arxiv.org/abs/quant-ph/0610027) and [Nussbaum–Szkoła](https://arxiv.org/abs/quant-ph/0607216).

A useful genuine necessary bound follows from root fidelity $f=\|\sqrt{\rho_0}\sqrt{\rho_1}\|_1$ and the trace-distance/fidelity inequality:

$$
p_e^*(n)\ge\tfrac12\bigl(1-\sqrt{1-f^{2n}}\bigr).
$$

For $0<f<1$ and $0<\delta<1/2$, attaining error at most $\delta$ requires

$$
n\ge L_F:=\frac{\log(1/[4\delta(1-\delta)])}{-2\log f}.
$$

Indeed the lower-error expression must be at most $\delta$, implying $f^{2n}\le4\delta(1-\delta)$. Multiplicativity of fidelity gives the product exponent. The underlying inequalities and Helstrom formula are in [Watrous, Chapter 3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf). Identical states ($f=1$) are indistinguishable under this task; orthogonal supports can be distinguished in one copy. Zero observations with equal priors still have error $1/2$.

### 2.1 Local alternatives {#близкие-гипотезы}

Quadratic exponents occur for regular nearby alternatives, with coefficients depending on the states, direction and experiment. They are not universally $\varepsilon^2/8$. For the commuting binary pair

$$
\rho_\pm=\operatorname{diag}(1/2\pm u,1/2\mp u,0,\ldots,0),\quad0<u<1/2,
$$

symmetry gives $Q=f=\sqrt{1-4u^2}$ and $\xi=-\tfrac12\log(1-4u^2)=2u^2+O(u^4)$. This pair is already realized in dimension two. Singular, orthogonal or nonregular alternatives need not have quadratic scaling.

### 2.2 Numerical Chernoff certificates {#числовые-оценки-info}

For that pair and $\delta=0.05$:

| $u$ | $\xi$ | Sufficient copy count $\lceil\log10/\xi\rceil$ |
|---|---|---|
| 0.25 | 0.143841 | 17 |
| 0.10 | 0.020411 | 113 |
| 0.05 | 0.005025 | 459 |

These are certificates for an allowed optimal test, not guaranteed training durations or necessary lower counts. There is no dimensional ceiling $\xi\le\log7$: for pure states with overlap $c$, $Q=c^2$, so $\xi=-2\log c$ becomes arbitrarily large as $c\to0$. The Holevo bound $\chi\le\log_2N$ concerns average accessible information for an ensemble in one $N$-level system, a different quantity.

## 3. Selected dynamical bound (T-110) {#динамическая-граница}

#### T-110: a scalar accumulator [T] {#теорема-динамическая-граница}

Choose one mode with attenuation $q=e^{-\alpha\Delta t}\in(0,1)$ and a constant aligned impulse $b>0$. For $x_{j+1}=qx_j+b$, $x_0=0$,

$$
x_n=\frac{b(1-q^n)}{1-q},\qquad x_\infty=\frac b{1-q}.
$$

For a target $d>0$, the non-strict cut $x_n\ge d$ is reached in finite time iff $d<x_\infty$. Its first step is

$$
n_D=\left\lceil\frac{\log(1-d(1-q)/b)}{\log q}\right\rceil.
$$

At equality $d=x_\infty$ only the limit reaches it. For $q=0$, the first step reaches the cut iff $b\ge d$; for $q=1$, $x_n=nb$ and $n_D=\lceil d/b\rceil$. A strict cut uses a floor plus one. The proof is the geometric-series identity followed by solving $q^n\le1-d(1-q)/b$; dividing by $\log q<0$ reverses the inequality.

For vector impulses with $\|b_j\|\le b$, the triangle inequality gives only $\|x_n\|\le b(1-q^n)/(1-q)$. Thus the scalar envelope yields a necessary time to attain norm $d$, but cancellation can prevent attainment. A claimed impulse update of a density matrix still needs a PSD/trace-preserving realization.

### 3.1 Physical meaning {#физический-смысл-dyn}

The value $\alpha=2/3$ belongs to a normalized Fano coherence mode in the specified generator. It is not a universal physical clock or the decay rate of every variable. Translating steps into seconds needs an independently measured rate. Non-normal coupled dynamics may need a transient prefactor rather than a single scalar exponential.

### 3.2 Role of regeneration {#роль-регенерации}

Feedback can alter the mode, attenuation and impulse. A changing $\varphi$ or rate invalidates the fixed-coefficient recurrence unless its reduction is proved. [Evolution](/docs/core/dynamics/evolution) supplies chosen state-preserving models and conditional attractor constructions; positive regeneration alone does not ensure safety or optimal learning.

## 4. Safety and noise (T-111) {#стабилизационная-граница}

#### T-111: a sufficient safe-neighborhood condition [T] {#теорема-стабилизационная-граница}

Fix a region $K$ of valid states satisfying **all** desired cuts, a norm and a state $\Gamma$ in its relative interior. Let $r=\operatorname{dist}(\Gamma,\mathcal D_7\setminus K)>0$. A state-valid update with $\|\Delta\Gamma\|<r$ remains in $K$. This is a sufficient condition, not a necessary bound on every successful learning update; a larger update in a safe direction may remain in $K$. A basin or trajectory certificate additionally requires the specified vector field, as in [viability](/docs/core/dynamics/viability#viability-kernel).

For the **purity cut alone** $P>P_c$ in HS norm, the exact distance is

$$
r_P=\sqrt{P-1/7}-\sqrt{P_c-1/7}=\sqrt{P-1/7}-1/\sqrt7\quad(P_c=2/7).
$$

The reverse triangle inequality around $I/7$ is a lower bound; radial mixing toward $I/7$ attains it within $\mathcal D_7$. This is not a Bures distance, a basin radius or the radius to all capability cuts. The former $\sqrt{P-2/7}$ formula was incorrect.

If $\|\Delta\Gamma_{\rm signal}\|\le b$ and bounded state-update noise has norm at most $\eta$, then $b+\eta<r$ is sufficient. Unbounded Gaussian noise does not give such a pathwise guarantee and requires a state-preserving noise model plus a finite-horizon exit estimate; see [T-145](/docs/proofs/consciousness/operational-closure#t-145).

### 4.1 A declared noise experiment {#компромисс-обучение-стабильность}

For independent **classical** observations $Y_j\sim\mathcal N(\pm m,\sigma^2)$ with equal priors, the optimal test uses the sample mean and has

$$
p_e^*(n)=\mathsf\Phi(-m\sqrt n/\sigma),\qquad
n_* = \left\lceil\frac{\sigma^2}{m^2}[\mathsf\Phi^{-1}(1-\delta)]^2\right\rceil,
$$

where $\mathsf\Phi$ is the standard normal CDF, distinct from matrix integration $\Phi$. The signal sum grows as $nm$, while its noise standard deviation grows as $\sqrt n\sigma$. This explains $1/\mathrm{SNR}^2$ scaling under this specific independent Gaussian law, not a separate universal stability law. Noise correlation, bias or a different loss changes the count. Attenuation is an engineering policy; its optimum requires an explicit cost and constraints.

### 4.2 Stability zones as a policy {#три-зоны-стабильности}

A policy may reduce its step as the certified margin shrinks, reject uncertified updates or fall back to a feasible state. Stress bands and action thresholds are choices [D/H], not universally derived clinical categories. Matrix noise and a purity deficit alone do not establish depression, trauma or treatment mechanisms.

## 5. Combining valid bounds (T-112) {#комбинированная-граница}

#### T-112: maximum of necessary bounds [T] {#теорема-оптимальная-граница}

If, for the **same task and admissible protocol class**, all successful protocols require $n\ge L_1$, $n\ge L_2$ and $n\ge L_3$, then

$$
n_*\ge n_{\rm LB}:=\max(L_1,L_2,L_3).
$$

This follows by conjunction. It proves neither equality, existence of a protocol attaining the maximum nor a unique best algorithm. The old label $n_{\mathrm{opt}}$ named this lower-bound score; use $n_{\rm LB}$ to avoid identifying it with an optimum. Chernoff's sufficient count cannot be inserted as a necessary $L_1$.

### 5.1 Comparing regimes {#диаграмма-режимов}

A verified fidelity lower bound $L_F$, a specified dynamical envelope and a separately necessary constraint can be compared after aligning units and premises. The largest identifies the strongest currently established obstruction. Distinct bounds may share assumptions or information and need not be independent. Simultaneous attainability requires a common constructive protocol, not separate equality examples.

### 5.2 Including genesis time {#генезис-плюс-обучение}

Adding initialization and learning times requires sequential stages with declared clocks. [T-148](/docs/proofs/consciousness/substrate-closure#t-148) gives an exact first-passage count for one constant-input recurrence, including a regime in which crossing never occurs. There is no universal genesis guarantee or $N\log N$ law from dimension alone. Adding a lower bound to an upper bound does not give an upper bound for total time.

## 6. Seven dimensions and learning (T-113) [H] {#оптимальность-n7}

<a id="теорема-t-113"></a>

#### Scope of T-113 {#теорема-минимальность-n7}

The former theorem “learning is impossible for $N<7$, uniquely Pareto-optimal at $N=7$” is withdrawn. A functional count of seven named roles does not prove that all learning requires seven orthogonal Hilbert-space axes. Neither self-observation, replacement nor statistical learning generally requires a Fano plane. Hurwitz classifies certain normed division algebras; it does not classify learning algorithms or all state-space dimensions.

A concrete counterexample is a two-level learner. Encode $q_j\in[0,1]$ as $\Gamma_j=\operatorname{diag}(q_j,1-q_j)$ and observe independent $Y_j\in\{0,1\}$ with mean $p$. Set

$$
\Gamma_{j+1}=(1-\eta_j)\Gamma_j+\eta_j\operatorname{diag}(Y_{j+1},1-Y_{j+1}),\qquad\eta_j=1/(j+1).
$$

For $j\ge1$, $q_j$ is the sample mean, $\mathbb E q_j=p$ and $\mathbb E(q_j-p)^2=p(1-p)/j\to0$. Each fixed observed update is a convex combination of identity and a replacement CPTP channel. This is finite-dimensional learning through replacement with $N=2$, without Fano structure. It refutes the universal claim, while leaving a specifically chosen seven-role architecture testable.

### 6.1 Structural requirements versus universal necessities {#цепочка-необходимостей}

If a selected implementation represents the seven Fano points by seven mutually orthogonal nonzero directions, then $N\ge7$ by dimension counting. This is a requirement of that representation [D], not of every learner. A fixed larger space can contain an invariant seven-dimensional sector and train only its parameters; extra dimensions do not necessarily slow learning. Embeddings and retractions do not establish a unique empirical encoder or functional frame.

### 6.2 Parameters and the selected efficiency score {#параметры-n7}

A general $N$-level density matrix has $N^2-1$ real parameters; at $N=7$ it has $48$. The selected ratio

$$
\eta(N):=\frac{\log_2N}{N^2-1}
$$

strictly decreases for real $N>1$: the derivative has the sign of $1-N^{-2}-2\log N<0$, because $2\log N-1+N^{-2}$ starts at zero and has positive derivative. Thus **if one separately restricts the class to $N\ge7$ and selects this score**, its maximum is at $7$. The ratio is not a universal resource/learning capacity, and a one-objective maximum does not establish a Pareto frontier. Rates, bootstrap strength, accessible information and genesis time still need their respective physical/model premises.

## 7. A reproducible binary example {#бинарная-дискриминация}

### 7.1 The two-button task {#задача-двух-кнопок}

Choose the commuting pair in §2.1 with equal priors, register the allowed observations and compare independent test error. Matrices encode an actual probability experiment here; no unique universal encoder is assumed.

### 7.2 Signal and mechanism {#сигнал-и-механизм}

For binary samples, reward-driven state updates can use the two-level recurrence above or a declared embedding into $\mathcal D_7$. Interpretations such as pleasure and punishment are separate hypotheses. The exact purity derivative of replacement is $2a(\operatorname{Tr}\Gamma\rho_*-P)$; it can be negative even if the target is purer.

### 7.3 Exact error and sufficient count {#оценки-числа-нажатий}

For $p_0=1/2-u$, $p_1=1/2+u$, the classical optimum is

$$
p_e^*(n)=\frac12\sum_{k=0}^n{n\choose k}\min\{p_0^k(1-p_0)^{n-k},p_1^k(1-p_1)^{n-k}\}.
$$

This finite sum is exact, including ties, and equals the quantum Helstrom value for these commuting states. The following code evaluates it with logarithmic binomial coefficients and also reports the Chernoff sufficient count.

```python
from math import ceil, exp, fsum, lgamma, log, log1p

def exact_binary_error(n, u):
    if not (n >= 0 and int(n) == n and 0 < u < 0.5):
        raise ValueError("n must be a nonnegative integer and 0<u<1/2")
    n = int(n)
    p0, p1 = 0.5-u, 0.5+u
    terms = []
    for k in range(n+1):
        log_binom = lgamma(n+1)-lgamma(k+1)-lgamma(n-k+1)
        a = k*log(p0)+(n-k)*log1p(-p0)
        b = k*log(p1)+(n-k)*log1p(-p1)
        terms.append(exp(log_binom+min(a,b)))
    return 0.5*fsum(terms)

def chernoff_sufficient_count(u, delta):
    if not (0 < u < 0.5 and 0 < delta < 0.5):
        raise ValueError("require 0<u<1/2 and 0<delta<1/2")
    xi = -0.5*log1p(-4*u*u)
    return max(1, ceil(log(1/(2*delta))/xi))
```

Finite-precision output is a numerical check, not an interval certificate; critical comparisons should use a verified error tolerance.

### 7.3a Separate signal and safety checks {#числовой-пример-nopt}

With $u=0.1$, $\delta=0.05$, the Chernoff sufficient count is $113$, while the exact sum can determine the smaller actual discrimination count. For a separately chosen accumulator $q=e^{-2/3}$, $b=0.1$, $d=0.15$, the exact dynamical count is $2$. These numbers are not interchangeable training lower bounds.

At $P=0.39$, the purity-only HS margin is $\sqrt{0.39-1/7}-1/\sqrt7\approx0.11917$, not $0.323$. No safety verdict follows without the direction, state validity and other gate margins. A chosen attenuation policy changes the observation law if it discards distinguishability; recompute that law rather than assuming every exponent changes as an arbitrary squared matrix amplitude.

### 7.4 Registered test criterion {#прогноз-кк-тест}

An empirical violation is assessed against the registered observation/task model with uncertainty and held-out data. Beating a sufficient Chernoff count is allowed. Lower error than a valid exact Helstrom optimum would instead challenge the stated encoding, independence/measurement assumptions or implementation. Speed in a simulator alone does not validate the physiological or phenomenal bridge.

## 8. Comparison with other learning results {#сравнение-с-классикой}

### 8.1 PAC learning and VC dimension

PAC guarantees require a hypothesis class, sampling law and loss; VC dimension measures a different object than the number of density-matrix coordinates. Forty-eight state parameters do not determine a hypothesis class's generalization complexity. A binary testing task is not every learning task.

### 8.2 Rademacher complexity and generalization

Capacity, regularity, sample dependence and the evaluation protocol affect generalization. An encoder selected using labels can add statistical degrees of freedom even if its output has only 48 coordinates. Parameter dimension alone is neither a sample bound nor an identifiability proof.

### 8.3 Shannon and Chernoff

Shannon transmission rate, Holevo accessible information and Chernoff error exponent address different experiments. Their units and operational definitions must be stated before comparison. Commuting quantum hypotheses recover the corresponding classical test; no $\xi\le\log7$ ceiling follows.

### 8.4 Thermodynamic assumptions

Landauer inequalities apply to a specified physical erasure process, bath and entropy balance, not to every decline of matrix purity. The [evolution page](/docs/core/dynamics/evolution#теорема-v-preservation-gate) states the conditional Reeb–Wolf equality. Neither a unique learning gate nor $k_BT\Delta S$ as a universal cost per training example follows from a software state update.

### 8.5 Local optimal direction and its limits {#за-границами-оптимальный-поток}

For a fixed potential $F$, positive definite metric and prescribed instantaneous speed $s$, Cauchy–Schwarz gives $dF(v)\ge-s\|\operatorname{grad}F\|$. If the gradient is nonzero the unique minimizing tangent velocity is $v=-s\operatorname{grad}F/\|\operatorname{grad}F\|$. This is [T-263's](/docs/core/dynamics/evolution#теорема-наилучший-обучающий-поток) local scope. Fixed-target reverse relative entropy has BKM gradient $\Gamma-\rho_*$; an input-dependent target introduces additional derivatives.

The result does not compare different potentials, metrics, observations, discretizations, global convergence or statistical sample rates. It proves neither a unique algorithm, an $O(1/k)$ rate for all learners nor attainment of the preceding bounds. Physics claims such as T-264 require their own declared realization and do not complete such an optimization proof.

## 9. Practical implications {#практические-следствия}

Use matched architecture tests, identifiable observation laws, separate sample/time/compute costs and state-valid updates. Certify local feasible margins and use an explicit objective for any learning-rate or attenuation optimization. Application to education or therapy requires independently validated biological readouts and clinical evidence; the matrix theorems do not derive a diagnosis or intervention.

## 10. Links and assumptions {#связь-с-результатами}

| Result | Valid use here |
|---|---|
| T-109 | Exact quantum i.i.d. binary discrimination; conditional Chernoff certificates |
| T-110 | Exact selected accumulator or its norm envelope |
| T-111 | Sufficient feasible-state neighborhood; separately specified noise law |
| T-112 | Conjunction of valid necessary bounds, without attainment |
| T-113 [H] | Selected seven-role architecture hypothesis; universal minimum withdrawn |
| T-42a [✗] | Supplies no universal encoder or equivalent empirical frame |
| T-148 | Conditional constant-input genesis, including no-crossing regimes |
| T-263 | Local steepest direction for specified metric/potential/speed |

## 11. Conclusion {#заключение}

The established results require explicit experiments and model assumptions. Seven state dimensions, covariance and a local gradient identity do not uniquely determine a learner or its empirical encoding. A stronger theory records these choices and tests their consequences.

## Summary {#резюме}

1. Exact Helstrom error is a genuine finite-sample obstruction; Chernoff's finite bound is sufficient.
2. The scalar accumulator has an exact crossing law under fixed coefficients.
3. Safe-neighborhood control is sufficient; full trajectory safety needs a dynamics certificate.
4. A maximum of necessary bounds remains a lower bound, not an attained optimum.
5. Two-level replacement learning disproves universal $N=7$ necessity; selected seven-role hypotheses remain testable.

### What was established {#что-мы-узнали-обучение}

Independent data, an identifiable readout and verified model premises connect these mathematical results to an empirical learning claim. See [measurement protocol](/docs/applied/research/measurement-protocol), [viability](/docs/core/dynamics/viability) and [evolution](/docs/core/dynamics/evolution).
