---
sidebar_position: 10
title: "Lagrangian of Gap Theory"
description: "Complete 6-term Lagrangian of Gap theory, the potential V_Gap, spontaneous minimum, and connection with the octonionic structure"
---

# Gap Lagrangian models: a selected action and its scope

:::warning Corrected T-75 scope — 2026-10-03
The exact universal six-term Keldysh derivation is withdrawn [✗]. Neither a subobject classifier nor a GKSL representation selects a unique Lagrangian, phase inertia or potential coefficients. The conditional model below [D/H] has checkable mathematical consequences.
:::

## 1. Coordinates and constraints

In a fixed frame, $\gamma_{ij}=r_{ij}e^{i\theta_{ij}}$ for $i<j$. A local phase chart needs $r_{ij}>0$; estimation stability needs an amplitude floor. Seven populations have six independent coordinates;21complex coherences have42real coordinates. Phases alone do not determine a state. Varying phases at fixed amplitudes can violate positivity, so the admissible domain must be checked.

Diagonal rephasing sends $\theta_{ij}$ to $\theta_{ij}+\alpha_i-\alpha_j$. Triangle holonomy is invariant under this operation, but selected real-G2-frame observables need not share that gauge symmetry. G2 does not generally act on a fixed-amplitude phase torus as a closed state domain.

## 2. Explicit model ansatz

Select a local phase domain, a constant symmetric positive definite matrix $M$, smooth potential $V(\theta)$ and action

$$
S[\theta]=\int_{t_0}^{t_1}\left(\tfrac12\dot\theta^TM\dot\theta-V(\theta)\right)dt.
$$

$M$ has units consistent with action and the selected time; coefficients do not follow from seven axes. The potential and its symmetries are separate inputs. Select a force $Q=-B\dot\theta+u$ with symmetric $B\succeq0$. Lagrange–d’Alembert gives

$$
M\ddot\theta+\nabla V+B\dot\theta=u.
$$

This follows exactly **from the stated action and forces**, not from arbitrary density evolution.

“Kinetic, potential, topological, dissipative, regenerative, external” is a selected grouping. Other admissible GKSL operators are not forbidden; universal completeness T-102 is withdrawn [✗]. Positivity of $M$ and $B$ are hypotheses, not consequences of the internal category.

## 3. What a matrix ODE supplies

For specified $\dot\rho=F(\rho,t)$ where $\gamma_{ij}\ne0$,

$$
\dot r_{ij}=\mathrm{Re}(e^{-i\theta_{ij}}F_{ij}),\qquad\dot\theta_{ij}=\mathrm{Im}(F_{ij}/\gamma_{ij}).
$$

Differentiate $r e^{i\theta}$ to obtain these identities. They give first-order dynamics. A second-order inertial equation needs velocity state or an independent closure; relabeling a dephasing rate as friction does not create it. At zero amplitude the phase and division are undefined.

## 4. Keldysh and the physical bridge

Closed-time-path methods are tools for a specified microscopic model. Deriving an effective action needs degrees of freedom, initial state, reservoir interaction, eliminated variables and controlled approximations. The method itself does not select $M$, a potential or UHM’s six terms. See the primary review [Sieberer–Buchhold–Diehl](https://arxiv.org/abs/1512.00637).

The former $\rho_+\log\rho_-$ formula did not prove equivalence of GKSL and the complete phase action; its stated classical limit was not derived. Universal T-75 is withdrawn. Such a comparison remains a separate task for each chosen physical realization.

## 5. Symmetries and interpretation

If specified $M,V,B,u$ respect a group, apply Noether’s theorem to the conservative part and compute charge changes from $Q$. Equal projector dimensions do not supply intertwiners with irreducible G2 representations. An odd term of a selected potential does not prove universal PT breaking: transformation of the state and all parameters must be specified.

Habit, qualia and the direction of experienced time are interpretations [I]. Phase coordinates, physical energy units and experimental readout need independent calibration.

See [variational derivation](./variational), [Gap](/docs/core/dynamics/gap-operator), [Gap thermodynamics](/docs/core/dynamics/gap-thermodynamics) and [Noether charges](/docs/physics/gauge-symmetry/noether-charges).

<a id="от-ньютона-к-лагранжу"></a>
<a id="шесть-аспектов"></a>
<a id="полная-структура"></a>
<a id="кинетический-член"></a>
<a id="потенциальный-член"></a>
<a id="потенциал-v-gap"></a>
<a id="механизм-хиггса"></a>
<a id="спонтанный-минимум"></a>
<a id="топологический-член"></a>
<a id="стрела-времени"></a>
<a id="диссипативный-член"></a>
<a id="регенеративный-член"></a>
<a id="внешний-член"></a>
<a id="швингер-келдыш"></a>
<a id="симметрии"></a>
<a id="спектр-возбуждений"></a>
<a id="пять-аргументов"></a>
<a id="единство"></a>
<a id="что-мы-узнали"></a>
