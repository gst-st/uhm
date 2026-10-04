---
sidebar_position: 0
title: Origin of the Universe
description: The primordial state and spontaneous symmetry breaking
---

# Origin and entropy: explicit models and open bridges

:::warning Scope — 2026-10-03
A density matrix and categorical definitions do not prove cosmogenesis, the necessity of the Universe or phenomenal experience. Identifying state, physical time and energy with cosmology requires separate hypotheses [H/I]. The exact dynamics below are distinct from that programme.
:::

## 1. Source and stationary state

$I/7$ maximizes entropy of the selected register. It is not terminal in the category of7-dimensional CPTP processes; the terminal register has dimension1. A fixed register’s states do not specify the Universe’s initial state.

For a unital linear generator, $\mathcal L(I/7)=0$. Normalized Fano dephasing plus a Hamiltonian with connected coupling graph has this unique stationary density. In the HS inner product,

$$
\mathrm{Re}\langle X,\mathcal LX\rangle=-\frac{2\gamma}{3}\|X_{\mathrm{off}}\|_2^2\le0.
$$

Under that connectivity there are no stationary or purely imaginary traceless modes, and the finite-dimensional flow approaches $I/7$. The former universal proof of source **instability** and inevitable cosmogenesis is therefore withdrawn [✗].

Nonlinear injection can change this only through specified targets and rates. A gate closed at $I/7$ makes the addition vanish there. Nonzero external injection with a different target can make the source nonstationary: that is a property of the chosen open model, not of the category.

## 2. T-271: exact entropy derivative

**[T under full rank and a differentiable trajectory].** For $S(\rho)=-\mathrm{Tr}(\rho\log\rho)$ and $\mathrm{Tr}\dot\rho=0$,

$$
\dot S=-\mathrm{Tr}(\dot\rho\log\rho).
$$

Units are nats; bits use $\log_2$. On the cone boundary the derivative may be infinite, so substituting $\log0$ needs a limiting argument.

For the specified field $\dot\rho=-i[H,\rho]+\mathcal D\rho+a(\sigma-\rho)$:

- $\dot S_H=0$, because $[\rho,\log\rho]=0$.
- A unital semigroup does not decrease $S$. Fano dephasing fixes every diagonal state, including states with $P>2/7$, so its contribution is not universally strictly positive.
- $\dot S_{\mathrm{inj}}=-a\mathrm{Tr}((\sigma-\rho)\log\rho)$ has no universal sign. A target $I/7$ can increase entropy; a purer target can decrease it in an appropriate region.
- At stationarity the sum of **all** fluxes vanishes. Exactly two nonzero nonunitary contributions must balance, but their signs need separate hypotheses.

Universal claims “more Coh_E implies less entropy,” “regeneration is always negentropic,” and “consciousness keeps entropy below heat death” are withdrawn. Purity alone determines neither entropy nor its flux. The consciousness reading is an interpretation that a matrix derivative does not prove.

## 3. T-273/T-276: physical erasure cost

**[C under a physical erasure protocol].** For initially independent system and thermal reservoir and global unitary evolution, the Reeb–Wolf equality reads

$$
\beta Q=\Delta S+I(S':R')+D(\rho'_R\|\rho_R),
$$

where $\Delta S=S(\rho_S)-S(\rho'_S)$ is system entropy decrease and $\beta=1/(k_BT)$. The last terms are nonnegative, giving $Q\ge k_BT\Delta S$. See [Reeb–Wolf](https://arxiv.org/abs/1306.4352).

If an additional physical model identifies maintenance with positive erasure rate $\dot S_{\mathrm{erase}}$ in nats/s, then $\dot Q\ge k_BT\dot S_{\mathrm{erase}}$. For bits/s include $\ln2$. Model dephasing is not automatically that erasure. Universal positive hardware power from purity alone and monotonic cost in $\kappa/\gamma$ are unproved.

Changing the numerical timestep leaves a fixed physical process unchanged. It changes approximation error and computational load. Physical hardware frequency and entropy rate need independent measurement; femto/picowatt estimates do not follow from a software matrix.

## 4. Cosmological programme

A cosmological comparison needs:

1. observable energy density, pressure, geometry and conservation laws;
2. a specific mapping from model states into those quantities, including units and scales;
3. field degrees of freedom, an action and boundary conditions;
4. initial data and solution stability;
5. independent observations distinguishing the model from alternatives.

Finite internal coordinates do not derive spatial dimension. Local ODE uniqueness does not select an initial condition or prove time’s origin. Metrics, topologies and a chosen octonionic frame may be useful model inputs; their cosmological role remains a testable hypothesis.

See the [cosmological constant](/docs/physics/gravity/cosmological-constant), [Λ budget](/docs/proofs/gap/lambda-budget), [evolution](/docs/core/dynamics/evolution) and [mathematical kernel](/docs/reference/mathematical-kernel).

<a id="источник"></a>
<a id="доказательство-нестабильности"></a>
<a id="космогенезис-неизбежность"></a>
<a id="самоусиление"></a>
<a id="эволюция-от-источника"></a>
<a id="направление-эволюции"></a>
<a id="t-271"></a>
<a id="количественные-оценки"></a>
<a id="почему-вообще-что-то-есть"></a>
