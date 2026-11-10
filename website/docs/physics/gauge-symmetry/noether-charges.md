---
sidebar_position: 5
slug: /physics/gauge-symmetry/noether-charges
title: "Charges of an invariant action"
description: "Conditions for a conserved charge and freedom in a symmetric covariance"
---

# Charges of an invariant action

## Conservation along a trajectory {#шаг-6-доказательство}

For a differentiable Lagrangian $L(q,\dot q)$, suppose each infinitesimal transformation $\delta_a q$ changes $L$ by a total derivative $dB_a/dt$. On Euler–Lagrange solutions, $Q_a=\sum_i (\partial L/\partial\dot q_i)\delta_a q_i-B_a$ is conserved. Applying this result to $G_2$ requires a dynamical action with that symmetry. A choice of instrument or external forcing can break it. A local gauge symmetry additionally has constraints and boundary conditions relevant to the definition of physical charges. [Noether](https://arxiv.org/abs/physics/0503066).

## Invariant covariances {#тождества-уорда-разложение}

<a id="6-тождества-уорда-для-gap-корреляторов"></a>

On $\Lambda^2\mathbb R^7=\mathbf7\oplus\mathbf{14}$ a symmetric $G_2$-invariant covariance has the form $a\mathsf P_7+b\mathsf P_{14}$ for the actual representation projectors. Each irreducible summand occurs once. Positivity requires $a,b\ge0$ and a trace measurement fixes $7a+14b$. A second independent measurement is needed to fix both coefficients.

## A coordinate covariance {#оператор-f21-определение}

<a id="собственные-значения-f21"></a>

On the 21 unordered Fano edges, join distinct edges on the same line. Every edge belongs to one line, so the adjacency matrix $F$ has seven $J_3-I_3$ blocks. Its eigenvalues are 2 and $-1$, with multiplicities 7 and 14. For the particular polynomial $C=\alpha(I-3F/7+3F^2/49)$ the uniform-vector eigenvalue is $19\alpha/49$ and the other eigenvalue is $73\alpha/49$. This ratio depends on the polynomial. A physical covariance needs a specified state and measurement of fluctuations. Matching multiplicities alone supplies no intertwiner between the unsigned edge coordinates and the wedge representation.
