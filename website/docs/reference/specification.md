---
slug: /reference/specification
sidebar_position: 4
title: "Mathematical specification"
description: "State space, process composition, dynamics, readouts and model conditions"
---

# Mathematical specification

## State and process types {#матрица-когерентности}

The operational construction takes preparations modulo indistinguishability under the allowed closed experiments. A finite-dimensional quantum realization supplies a complex Hilbert space $\mathcal H$, a state $\Gamma=\Gamma^\dagger\succeq0$ with $\operatorname{Tr}\Gamma=1$, and linear completely positive trace-preserving maps for deterministic processes. An instrument has completely positive, trace-nonincreasing outcome branches whose sum is trace preserving. Outcome probabilities are traces. Condition on an outcome by dividing by its probability only when it is positive.

Sequential wiring is composition. Independent parallel wiring uses a tensor product. A pair of seven-dimensional quantum registers has joint dimension 49. The matrix of a single seven-dimensional register has 48 real trace-one Hermitian parameters; positivity further restricts their values. Which parameters a given lab identifies depends on its accessible effects. [Observation closure](./mathematical-kernel#observable-closure).

## Specified dynamics {#уравнение-эволюции}

<a id="гамильтониан"></a>

For a time-homogeneous quantum Markov semigroup in finite dimension a generator can be written, in units with $\hbar=1$, as

$$
\dot\Gamma=-i[H,\Gamma]+\sum_j\left(L_j\Gamma L_j^\dagger-\tfrac12\{L_j^\dagger L_j,\Gamma\}\right).
$$

The Hermitian $H$ and jump operators $L_j$ are model inputs. A fixed replacement target $\sigma$ permits the trace-preserving generator $\kappa(\sigma\operatorname{Tr}X-X)$ for $\kappa\ge0$. A state-dependent target or gate generally gives nonlinear state evolution. Its positivity, tensor extension, resource requirements and implementation require their own conditions. [Dynamics](../core/dynamics/evolution) · [Premises and rates](./premises#свободные-параметры).

## Geometry of specified observations {#проективное-пространство-качеств}

<a id="метрика-фубини-штуди"></a>
<a id="полное-экспериенциальное-пространство"></a>
<a id="теорема-невозможность-спектрального-функтора"></a>

For normalized rays in a supplied Hilbert space, $d_{\rm FS}([u],[v])=\arccos|\langle u,v\rangle|$. For density matrices one may use the Bures angle $\arccos\operatorname{Tr}\sqrt{\sqrt\rho\,\sigma\sqrt\rho}$. Both are defined after choosing the quantum state representation. A spectrum-only readout identifies isospectral states even when a calibrated projector distinguishes them. For example $|0\rangle\langle0|$ and $|1\rangle\langle1|$ have the same spectrum but give probabilities one and zero on the effect $|0\rangle\langle0|$. Interpreting either geometry as perceived similarity requires independent report data.

<a id="топология-гротендика"></a>

The metric opens form a site with inclusions and ordinary union covers. A sheaf specifies how local data agree and glue. A chosen record of contextual inputs or past observations is additional structure. A time history, a loop and a tensor marginal have different domains.

## The selected seven-axis scores

In a specified basis put $d=\sum_i\Gamma_{ii}^2$, $q=\sum_{i\ne j}|\Gamma_{ij}|^2$, $P=d+q$, $\Phi=q/d$ and $R=1/(7P)$. Since $d\ge1/7$, the condition $\Phi\ge1$ implies $P\ge2/7$. The converse can fail on diagonal states. The conjunction $P>2/7$, $R\ge1/3$, $\Phi\ge1$ and $D_{\rm diff}\ge2$ defines the chosen gate. Its numerical cuts are conventions. The entropy-based $D_{\rm diff}=\exp S(\rho_E)$ requires a specified density-valued readout or tensor factor. A basis axis by itself has no such nontrivial marginal. [Thresholds](./mathematical-kernel#thresholds) · [Empirical tests](./falsifiability).

## Octonion and field data {#октонионная-алгебра}

A positive three-form on a real seven-dimensional vector space determines a metric, orientation and stabilizer $G_2$. An oriented Fano basis displays its multiplication components. Assigning matter to a bimodule $H_F$, choosing a physical Dirac operator and specifying the field action are independent steps. A fixed algebra and frame do not determine a particle spectrum. [Gauge representations](../physics/gauge-symmetry/standard-model).
