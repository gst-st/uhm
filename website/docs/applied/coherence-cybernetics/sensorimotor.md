---
sidebar_position: 18
title: Sensorimotor Theory
description: Typed observation, admissible control, and conditional information bounds
---

# Sensorimotor Theory

A sensorimotor model specifies observations, state reconstruction, controls, and a loss. Its existence is a design choice [D], and its identification with a physical system is an independently testable bridge. The revised model follows [the mathematical kernel](/docs/reference/mathematical-kernel) and [identifiability protocol](/docs/applied/research/reconstruction-identifiability).

## Admissible environmental influence {#теорема-полнота-трёх-членов}

The former T-102/T-57 prohibition of a fourth generator is withdrawn. A sum of GKSL generators with nonnegative rates is another admissible GKSL generator. A Hamiltonian term, a dissipative term, and a replacement-feedback term form a **selected grouping**, not three exhaustive categorical types. A replacement generator with fixed target $\tau$ has Kraus jumps $K_{mn}=\sqrt{a\lambda_m}|m\rangle\langle n|$, where $\tau=\sum_m\lambda_m|m\rangle\langle m|$; substitution gives $a(\tau\operatorname{Tr}\rho-\rho)$. It already belongs to the GKSL class.

A signed difference of two generators need not itself be admissible. Validate the full controlled generator, including rate signs, target positivity and boundary regularity. State-dependent feedback is a density-preserving nonlinear law under the stated hypotheses; it is not one linear quantum channel.

## Observation and encoding {#теорема-кодирование-среды}

Specify a sample space $\mathcal Y$ and probability law $p_\rho(y\mid u)$ for each preparation or intervention $u$. An estimator $G:\mathcal Y^m\to\mathcal D_7$ outputs a candidate state and an uncertainty set. The map $G$ is a classical estimator, not a CPTP map between quantum matrix algebras. Positive parametrisation is useful but does not establish identifiability.

For a quantum instrument, specify CP maps $\mathcal I_y$ with trace-preserving sum; then $p_\rho(y)=\operatorname{Tr}\mathcal I_y(\rho)$. Its quantum output and classical readout are distinct. A feature model needs its own likelihood. Codomain $G_2$ symmetry does not make either construction unique. The old T-42a claim is withdrawn; strong encoder comparison requires (RI).

Calling Enc a functor requires explicit source and target categories, identity preservation, and compatibility with composition. A collection of state-indexed perturbations does not supply these laws automatically. An ordinary statistical model is sufficient when no categorical composition is used.

## Action and optimisation {#теорема-оптимальное-действие}

An action $u\in\mathcal U$ selects an admissible channel $\Lambda_u$, or a specified evolution segment. For a declared loss $\ell$,

$$
u^*\in\operatorname*{argmin}_{u\in\mathcal U}\ell(\Lambda_u(\rho)).
$$

For finite $\mathcal U$, an optimum exists by enumeration. For compact $\mathcal U$ and continuous objective, it exists by the extreme-value theorem. Neither hypothesis establishes uniqueness, convexity, global polynomial-time optimisation, or viability of the selected action. A safety guarantee requires a feasible safe action and a verified invariant condition on the full trajectory under the specified disturbances.

For the four-condition gate use $P>2/7$, $R\ge1/3$, $\Phi\ge1$, and the declared $D_{\rm diff}\ge2$. The selected seven-component stress panel is not equivalent to this gate. A minimax stress objective is a design loss [D].

## Motor scores with a fixed target {#теорема-моторный-стресс}

Given a fixed target $\tau$ with $\tau_{kk}>0$, define the raw score

$$
s_k=1-\rho_{kk}/\tau_{kk}.
$$

Then $\partial s_k/\partial\rho_{kk}=-1/\tau_{kk}$. This is a coordinate derivative of a chosen score. If the target is $\tau(\rho)$, its derivative also contributes:

$$
ds_k=-\frac{d\rho_{kk}}{\tau_{kk}}+\frac{\rho_{kk}}{\tau_{kk}^2}d\tau_{kk}.
$$

The positive parts $\max(0,s_k)$ are bounded by one for valid positive populations, while raw scores may be negative. They measure population deficit, not the complete stress panel or all four gates. Equality with $1-7\rho_{kk}$ holds when the fixed target is $I/7$; no universal convergence to this target at $P=2/7$ follows. Simultaneous axis permutation preserves the indexed comparison. General $G_2$ conjugation changes the coordinate ratios.

## Valence and qualia {#гедоническая-валентность}

A score such as a directional change in purity or loss can be defined mathematically [D]. Its identification with pleasure, pain, perception or qualia is [I/H], requiring a readout and empirical bridge. The $\binom72=21$ complex off-diagonal entries form 42 real parameters in a fixed frame; this coordinate count is not a proof of twenty-one mutually independent sensory modalities or communication channels. A higher experiential extension cannot be reconstructed from these entries without a specified lift and observation law.

## Conditional information bound {#теорема-информационная-ёмкость}

For a classical label $X$ encoded in an ensemble $\{p_x,\rho_x\}$ on a seven-dimensional quantum register and measured with a POVM,

$$
I(X:Y)\le\chi:=S(\bar\rho)-\sum_xp_xS(\rho_x)\le\log_2 7.
$$

This is the Holevo bound for that encoding/measurement task [T]. Orthogonal pure signal states attain $\log_2 7$ with the matching measurement. For $n$ seven-dimensional registers carrying one message, even a collective measurement obeys $I(X:Y)\le n\log_2 7$ because their joint dimension is $7^n$.

The bound does not limit unrestricted classical sensor data, arbitrary external memory, or physical information per clock tick without an additional encoding/resource model. It also does not exclude tomography from repeated preparations: the sample count grows as accuracy increases. To infer a lower bound on required uses, specify the message entropy or discrimination task, error tolerance, and allowed side information. Identifying this bound with universal biological bounded rationality is unsupported.

[Watrous, Theory of Quantum Information, chapter 5](https://cs.uwaterloo.ca/~watrous/TQI/TQI.double.5.pdf) supplies the information-theoretic theorem. The physical identification of the register and one channel use belongs to the model.

## Joint systems and aggregation {#теорема-композиционность}

Two factors use $\mathcal D(\mathbb C^7\otimes\mathbb C^7)$. A chosen linear aggregation to one factor cannot be composed with itself when its output and input dimensions differ. The mean of marginals is a specified channel and discards connected correlations. A correlation-sensitive subject criterion needs additional data and an exclusion rule. Weak-coupling transfer of a margin requires a bound on marginal error, as in [Theorem 9.1](./theorems#теорема-91-фрактальное-замыкание); it does not establish universal scale invariance.

The full interface is reproducible only with its observations, preparation, controls, target, gate, physical time, loss, and uncertainty rules recorded. [The implementation](./implementation) gives a state-preserving numerical step for a specified family.

<a id="21-квалиа-тип"></a>
<a id="t-103-стратификация"></a>
<a id="гедонический-механизм"></a>
<a id="гранд-канонический-словарь"></a>
<a id="заключение"></a>
<a id="информационная-ёмкость"></a>
<a id="каноническое-включение"></a>
<a id="композициональность-enc-dec"></a>
<a id="моторный-стресс"></a>
<a id="мультимодальная-декомпозиция"></a>
<a id="предиктивная-структура"></a>
<a id="пример-робот"></a>
<a id="пример-хемотаксис"></a>
<a id="пример-человек"></a>
<a id="разобранные-примеры"></a>
<a id="реализация-enc"></a>
<a id="резюме"></a>
<a id="связь-с-результатами"></a>
<a id="следствие-кумулятивная-информация"></a>
<a id="следствие-минимальные-наблюдения"></a>
<a id="следствие-мультимодальная-декомпозиция"></a>
<a id="следствие-предиктивный-enc"></a>
<a id="следствие-факторизация-enc"></a>
<a id="сравнение-с-fep"></a>
<a id="сравнение-с-rl"></a>
<a id="сравнение-с-классическими-подходами"></a>
<a id="сравнение-с-управлением"></a>
<a id="среда-через-3-канала"></a>
<a id="темпоральная-интеграция"></a>
<a id="теорема-гедоническая-валентность"></a>
<a id="теорема-термодинамическая-трихотомия"></a>
<a id="термодинамическая-трихотомия"></a>
<a id="универсальная-архитектура"></a>
<a id="факторизация-enc"></a>
<a id="функтор-dec"></a>
<a id="функтор-enc"></a>
<a id="что-мы-узнали-сенсомоторика"></a>
