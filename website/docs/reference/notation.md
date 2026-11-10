---
sidebar_position: 2
title: "Mathematical notation"
description: "Symbols for preparations, records, density-model readouts and Fano coordinates"
---

# Mathematical notation

## Processes and measurement records

| Symbol | Meaning |
|---|---|
| $p:a\to b$ | A process with declared input and output types. A preparation has the trivial input type. |
| $T[p]$ | A closed experiment containing the process in an allowed test context. |
| $p\sim q$ | All allowed closed tests have equal records for the two processes. A new intervention can refine this relation. |
| $C(y)$ | States and calibration parameters compatible with the observation $y$. |
| $U_{ji}$ | Transport from site $i$ to site $j$. Under local frame changes, $U_{ji}\mapsto g_j U_{ji}g_i^{-1}$. |
| $d(i,j)$ | Minimum cost of an admissible transfer when a complete search or a proof establishes that minimum. Directional costs can be asymmetric. |

[Network observables](./network-results) · [Measurement and uncertainty](./falsifiability).

## A finite-dimensional quantum model

| Symbol | Definition |
|---|---|
| $\mathcal H$, $D_N$ | Hilbert space of dimension $N$ and its positive trace-one matrices. The selected semantic register uses $N=7$. |
| $\Gamma$, $\gamma_{ij}$ | State and its entries in the declared basis. $\gamma_{ji}=\overline{\gamma_{ij}}$. |
| $K$, $K^*$ | A linear channel and its trace adjoint on observables. A trace-preserving channel has a unital adjoint. |
| $E_y$ | An outcome effect. A measurement obeys $E_y\succeq0$, $\sum_y E_y=I$ and $p(y)=\operatorname{Tr}(E_y\Gamma)$. |
| $H$, $L_j$ | Hermitian Hamiltonian and specified jump operators of a quantum Markov model. |
| $\sigma$, $\kappa$ | A target state and rate for a specified replacement law. Time units and rate calibration must agree. |
| $P$, $S$ | Purity $P=\operatorname{Tr}\Gamma^2$ and entropy $S=-\operatorname{Tr}(\Gamma\log\Gamma)$ with the declared log base. |

For a supplied tensor product $\mathcal H_A\otimes\mathcal H_B$, $\rho_A=\operatorname{Tr}_B\Gamma_{AB}$. A coordinate compression $\Pi\Gamma\Pi$ on one register is a different operation and may have trace less than one. [Model specification](./specification).

## Seven-axis readouts {#индексы-измерений-протокол-измерения}

$A,S,D,L,E,O,U$ name articulation, structure, dynamics, logic, interiority, ground and unity. In the cyclic octonion table used on the physics pages the numbering is $(A,S,D,L,E,U,O)=(1,2,3,4,5,6,7)$. A matrix displayed in another order requires the same permutation on rows, columns and observables.

Write $d=\sum_i\gamma_{ii}^2$ and $q=\sum_{i\ne j}|\gamma_{ij}|^2$. Then $P=d+q$, $\Phi=q/d$ and $R=1/(7P)$ for the specified readouts. $D_{\rm diff}=\exp S(\rho_E)$ needs its own defined state $\rho_E$. $I_A,\ldots,I_U$ denote candidate experimental indices, such as mutual information or a thresholded Jacobian rank. Their correspondence with populations or coherences requires calibration. [Measurement protocol](../applied/research/measurement-protocol).

## Geometry, incidence and fields {#топология-гротендика}

$F(\rho,\sigma)=(\operatorname{Tr}\sqrt{\sqrt\rho\sigma\sqrt\rho})^2$ denotes squared fidelity. The Bures angle is $\arccos\sqrt F$ and the chordal Bures distance is $\sqrt{2-2\sqrt F}$. The open-site topology uses inclusion and union covers. An explicit formula fixes which distance enters a numerical bound.

$f_{ijk}=\langle e_i e_j,e_k\rangle$ are octonion structure constants; $G_2=\mathrm{Aut}(\mathbb O)$. $H_F$ denotes the supplied finite fermion space of a spectral model, $D_F$ its internal Dirac operator. Mass matrices can already be entries of that operator. The gauge action, local fields and physical energy scale require separate specification. [Fano table](../physics/gauge-symmetry/g2-structure) · [Mass inputs](../physics/particle-physics/yukawa-hierarchy).
