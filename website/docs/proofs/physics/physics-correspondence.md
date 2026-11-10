---
slug: /proofs/physics/physics-correspondence
sidebar_position: 1
title: "Comparing the network with physical theories"
description: "What follows from operational equivalence, and which extra premises select a physical realization."
---

## Processes and representations {#1-категорная-структура-связей}

Two preparations represent the same state when they can be substituted in every admissible single-hole experiment without changing its complete record. Their equivalence is preserved by serial and parallel wiring. A representation in matrices must preserve these experiments, including joint readouts; agreement on isolated systems is insufficient. [Operational proof](/docs/core/foundations/operational-processes#composition) · [A comparison with independent references](/docs/networks/reference-comparison)

## Truth values and physical instruments {#2-l-унификация}

A subobject classifier supplies characteristic arrows. To obtain an instrument one needs a representation of the alternatives by effects, their probabilities, and state updates conditional on the outcome. A dissipative generator additionally needs rates and a time scale. None of these is fixed by the classifier of open subsets. [Assumptions and countermodels](/docs/reference/mathematical-kernel#bures-site)

## Unitary evolution {#3-редукция-к-квантовой-механике}

Given a complex Hilbert space, a density operator, time and a self-adjoint Hamiltonian, turning off dissipation and regeneration leaves the commutator evolution. This is a limit of the specified equation. In the chosen seven-dimensional model $R=1/(7P)\ge1/7$; setting rates to zero is not a state with zero reflection. [Exact unitary regime](/docs/physics/quantum-mechanics/qm-reduction)

## Distance from response {#4-эмерджентная-геометрия}

Reachability bounds the earliest possible effect; it does not ensure that a specific probe sees the front. An arrival distance needs detection, reciprocity and a calibrated clock. A positive common limiting distance further needs control of interscale errors and separation of ports. Model rings and their products satisfy explicit conditions. [Common limit](/docs/geometry/common-limit)

## Gravitational dynamics {#5-связь-с-общей-теорией-относительности}

A distance on detector positions does not select dimension, a Lorentzian signature, or equations of motion. The curvature term in a heat-kernel expansion starts with a specified Riemannian spectral geometry. Relating it to a measured gravitational field requires a physical action, a continuum limit with causal structure and a matter response in the same units. [Gravity](/docs/physics/gravity/einstein-equations)

## Gauge actions and fields {#6-калибровочные-симметрии-и-стандартная-модель}

Changing frames at the endpoints of an edge gives the transport law $U_{ji}\mapsto g_jU_{ji}g_i^{-1}$. Intermediate frames cancel on a path. This holds for many groups. The stabilizer of a chosen unit imaginary octonion in $G_2$ is isomorphic to $SU(3)$; the representation and charges of measured matter remain extra physical inputs. [Gauge transport](/docs/networks/three-node-transport) · [Particle models and observables](/docs/reference/frontier-ledger)

## What seven counts {#7-соответствие-7-измерений-физическим-структурам}

Correction of one error, signed interference and a shared decoder select seven positions under their stated operational hypotheses. A code position is not a particle species, a spatial coordinate or a separately measured degree of freedom. [Address bound and its assumptions](/docs/core/foundations/operational-processes#address)

## Unconditional remote records {#запрет-сигнализации}

A local choice cannot change the remaining record if it acts on an independent wire, interchange holds and discarding its result gives the same operation for both choices. This holds for correlated preparations. In a tensor representation it includes $\mathrm{Tr}_A[(\Lambda_A\otimes I)\rho]=\mathrm{Tr}_A\rho$ for trace-preserving local channels, by the Kraus completeness identity. It does not identify a selected branch with the unconditional record. [General process theorem](/docs/core/foundations/operational-processes#composition)

## Conditioning with nonlinear evolution {#85-ансамблевая-независимость}

For an ensemble with probabilities $p_k$ and states $\rho_k$, evolving the selected branches gives $\sum_k p_k F(\rho_k)$. Evolving the marginal gives $F(\sum_k p_k\rho_k)$. Equality for every finite ensemble is precisely affinity. If the partner can steer a purification into every decomposition and local measurements separate states, selective evolution that is nonaffine can distinguish the remote preparation. Marginal invariance of a local channel by itself does not settle this question.

## Amplification, time and precision {#86-вычислительное-ограничение}

For the ideal self-registering feedback model on the diagonal line $p=(1/2+x,1/2-x,0,\ldots)$ with constant positive rate, diagonal Hamiltonian and the specified dephasing, $\dot x=(2\kappa/7)x(1-4x^2)/(1+4x^2)^2$. The derivative at zero is $2\kappa/7$. Integrating to a fixed threshold strictly below $1/2$ takes time logarithmic in the inverse initial positive bias. This says nothing about the cost of preparing that bias, keeping the saddle fixed to that accuracy, bounded measurement error or implementing the nonlinear feedback on an unknown preparation. [Feedback resource bound](https://github.com/uhm-theory/holon/blob/main/website/research/operational-reconstruction/feedback.md)

## What must be measured {#87-прочтение-измерения}

Record remote choice and outcome separately. Compare the unconditional response and the response grouped by the transmitted outcome; transmit the outcome only after the local readout. With no coupling between the laboratories, a unique autonomous evolution of the unconditional marginal gives the same local trajectory regardless of the remote channel. Conditioning can still change the grouped statistics.

## When the marginal is forced {#88-прочтение-вынуждено}

Let a local description agree with the local state on every product preparation and be invariant under all remote channels, including discarding the remote system and replacing it with a fixed state. Applying that replacement to a joint preparation gives the local marginal times the fixed state. The two requirements therefore force the local description to equal the marginal. This proof explicitly assumes remote replacement and invariance; it does not select a physical dynamics or a relativistic time slicing.

## Shared symmetries {#g2-многообразия}

A group may act on two different spaces. To transfer physics one needs a map of preparations and observables preserving their evolution and measured predictions. The name of the symmetry does not supply that map. [Comparison of realizations](/docs/proofs/physics/toe-embeddings)
