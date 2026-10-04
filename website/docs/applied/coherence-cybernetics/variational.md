---
sidebar_position: 11
title: "Variational Principles"
description: "Principle of stationary action, Euler–Lagrange equations for Gap, Onsager relations, connection to FEP, minimum entropy production, FDT"
---

# Variational derivation under an explicit action

:::warning Scope — 2026-10-03
The results below follow from a selected action and supplied force. Universal equivalence with Keldysh derivation T-75 is withdrawn [✗]; phase action and GKSL dynamics need a separate comparison bridge.
:::

## 1. Equation of motion

Let $L=\tfrac12\dot\theta^TM\dot\theta-V(\theta)$, with constant $M=M^T\succ0$, $V\in C^2$, and $Q=-B\dot\theta+u(t)$, $B=B^T\succeq0$. For endpoint-vanishing variations,

$$
0=\delta\int Ldt+\int Q^T\delta\theta\,dt=\int(-M\ddot\theta-\nabla V+Q)^T\delta\theta\,dt.
$$

The fundamental lemma gives $M\ddot\theta+\nabla V+B\dot\theta=u$. Local existence and uniqueness follow from local Lipschitz regularity in the extended coordinates $(\theta,\dot\theta)$ and continuous $u$. Global existence and matrix positivity need additional estimates.

For $M=M(\theta)$ add

$$
\Gamma_{abc}\dot\theta_b\dot\theta_c,\quad\Gamma_{abc}=\tfrac12(\partial_bM_{ac}+\partial_cM_{ab}-\partial_aM_{bc}).
$$

Omitting mass derivatives is not exact when amplitudes vary.

## 2. Energy balance and stability

For time-independent $M,V$, energy $E=\tfrac12\dot\theta^TM\dot\theta+V$ obeys

$$
\dot E=-\dot\theta^TB\dot\theta+\dot\theta^Tu.
$$

With $u=0$ it is nonincreasing. If $B\succ0$, the potential has a strict isolated minimum and an appropriate level domain is compact and invariant, LaSalle gives local asymptotic stability of that equilibrium. If $B\succeq0$, analyze the largest invariant set in $\dot E=0$; universal convergence does not follow.

Linearizing at a minimum with $K=\nabla^2V\succ0$ gives

$$
M\ddot x+B\dot x+Kx=0.
$$

The Hamiltonian, potential and boundary conditions determine frequencies and damping. Component count does not select universal neural rhythms.

## 3. A restricted minimum principle

**[T under a specified quadratic model].** For $B\succ0$ and fixed linear boundary constraints $Av=b$, $\tfrac12v^TBv$ has a unique minimum on a nonempty feasible affine set. The Lagrange conditions are

$$
Bv+A^T\lambda=0,\quad Av=b.
$$

This is a quadratic Dirichlet problem, not a universal entropy-minimization theorem for nonlinear living systems. Identifying the objective as physical entropy production requires a linear-response and reservoir model. Onsager symmetry needs appropriate microscopic reversibility; it does not follow from seven axis names.

## 4. Variational free energy

For a specified probability model $p(y,z)$ and normalized $q(z)$ with existing integrals,

$$
\mathcal F[q]=\mathbb E_q[\log q(z)-\log p(y,z)]=D_{KL}(q\|p(z\mid y))-\log p(y).
$$

Thus $\mathcal F\ge-\log p(y)$, with equality at $q=p(z\mid y)$. This exact probabilistic identity does not identify every numerical self-model as a Bayesian posterior or derive unique regeneration, a consciousness limit or UHM’s full action.

## 5. Comparison with the matrix field

Comparing with $\dot\rho=F(\rho)$ requires a coordinate-to-positive-density map, amplitude and phase dynamics, identical vector fields or a reduction-error bound, and a nonzero-amplitude domain. There $\dot\theta_{ij}=\mathrm{Im}(F_{ij}/\gamma_{ij})$ exactly. This is first-order; an independent second-order inertial model is not automatically the same system.

See the [selected Lagrangian](./lagrangian), [evolution](/docs/core/dynamics/evolution) and [numerical implementation](./implementation).

<a id="от-ферма-до-фейнмана"></a>
<a id="принцип-действия"></a>
<a id="уравнения-эйлера-лагранжа"></a>
<a id="четыре-силы"></a>
<a id="необратимая-термодинамика"></a>
<a id="соотношения-онзагера"></a>
<a id="метриплектическая-геометрия"></a>
<a id="связь-с-fep"></a>
<a id="фристон-из-кк"></a>
<a id="минимум-производства-энтропии"></a>
<a id="пригожин-и-экономия"></a>
<a id="фдт"></a>
<a id="идея-фдт"></a>
<a id="вариационный-вывод-регенерации"></a>
<a id="сводная-таблица"></a>
<a id="заключение"></a>
<a id="что-мы-узнали"></a>
