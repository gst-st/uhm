---
sidebar_position: 12
title: "Effective Temperature"
description: "Effective temperature: units, stochastic models, fluctuation-response measurements and conditional physical meaning"
---

# Effective Temperature

An effective temperature is meaningful only after specifying an observable, its conjugate perturbation, a stochastic dynamics and an energy scale. The two rates $\Gamma_2$ and $\kappa_0$ alone do not determine fluctuation amplitudes or a temperature. This chapter uses one explicit linear stochastic model, distinguishes a rate-ratio convention from an FDT measurement, and keeps physical and phenomenal interpretations conditional.

## Temperature: from Boltzmann to Consciousness {#от-больцмана-к-сознанию}

Physical temperature is in kelvin; $k_BT$ is an energy. For equilibrium thermodynamic entropy in joules/kelvin, $1/T=(\partial S/\partial E)$ at fixed other extensive variables. For dimensionless entropy in nats, the derivative is $1/(k_BT)$. The identity $\langle E_{\mathrm{kin}}\rangle=3k_BT/2$ additionally assumes a classical three-dimensional translational degree of freedom with quadratic kinetic energy. It is not a general definition for cognitive observables, nor does zero temperature always select a unique ground state.

In a statistical model, $p(x)\propto e^{-V(x)/\Theta}$ uses an energy scale $\Theta$ if $V$ is an energy. A dimensionless score requires a dimensionless scale instead; it cannot acquire kelvin units without physical calibration.

## Psychological temperature: interpretation {#психологическая-температура}

Associating fluctuation amplitude with attention, creativity, anxiety or other reports is a hypothesis [H/I]. Those reports are not thermometers for a latent matrix. No clinical state or consciousness level follows from “high” or “low” temperature alone. A fluctuation model must be tested against its independently defined observations and interventions.

## 1. Definitions and units {#определение}

### 1.1 A rate-ratio convention [D]

For calibrated rates $\Gamma_2\ge0$, $\kappa_0>0$ in the **same reciprocal-time units**, one may choose

$$
r_0=\frac{\Gamma_2}{\kappa_0},\qquad
\Theta_{\mathrm{ratio}}=r_0 k_BT_{\mathrm{phys}},\qquad
T_{\mathrm{ratio}}=\Theta_{\mathrm{ratio}}/k_B=r_0T_{\mathrm{phys}}.
$$

The former $T_{\mathrm{eff}}=(\Gamma_2/\kappa_0)k_BT_{\mathrm{phys}}$ had energy units while being compared to a temperature. The corrected convention distinguishes the two units. Identifying $T_{\mathrm{ratio}}$ with a measured fluctuation temperature is a further model hypothesis [H/C], not a theorem about regeneration.

A neural oscillation frequency is not automatically an exponential decorrelation rate, and a recovery rate is not automatically the same model's regenerative coefficient. The current [kinetic construction of $\kappa_0$](/docs/core/foundations/axiom-septicity#структурный-анзац-kappa0) requires its specified rates and calibration; a categorical counit norm does not supply them.

### 1.2 Comparison with physical temperature {#t-eff-neq-t-phys}

Under the ratio convention, $T_{\mathrm{ratio}}>T_{\mathrm{phys}}$ **iff** $r_0>1$ for positive $T_{\mathrm{phys}}$. Equality and a lower value are also allowed. The full [Cap₂ gate](/docs/reference/mathematical-kernel#thresholds) contains no such rate inequality, so “hotter than the body for every living system” is not established.

A measured FDT temperature differs from $T_{\mathrm{phys}}$ only if calibrated fluctuation and response measurements demonstrate the difference under the chosen model. Large raw variance alone is insufficient: susceptibility, units, filtering and energy scale also matter.

### 1.3 Limits and time scales

For fixed positive $\Gamma_2$ and $T_{\mathrm{phys}}$, the **chosen ratio** diverges as $\kappa_0\downarrow0$. At $\kappa_0=0$ it is undefined; if both rates tend to zero their ratio can have any limit. This algebra neither establishes a divergent FDT temperature nor proves death or coma. In a stationary finite-state model bounded observables have bounded variance, and a limit can also destroy stationarity or the inference of temperature.

The earlier identification of $0.01$–$0.1\,\mathrm{s}^{-1}$ with hours–days was incorrect: reciprocal time scales are 10–100 seconds. No numerical neural-rate or “$10^3$ times body temperature” estimate is asserted here without an identified observation model and primary data.

### 1.4 Fluctuation scale and stability {#два-режима}

At a fixed stable potential curvature, increasing noise broadens the stationary distribution in the model below. Changing curvature or mobility can change variance at the same temperature. Consequently a noise level alone does not establish an optimal learning regime, a phase transition or biological viability.

## 2. Stochastic model and FDT conditions {#категориальный-вывод}

Choose dimensionless coordinates $x\in\mathbb R^m$, an energy $V(x)=x^TCx/2$ with $C=C^T>0$, symmetric mobility $M=M^T>0$, and a conjugate field $h$ entering the energy as $-h^Tx$ [D]. In physical time,

$$
dx=(-MCx+Mh)\,dt+B\,dW_t,\qquad Q=BB^T.
$$

$C$ and $h$ have energy units, $M$ has units $(\mathrm{energy}\cdot\mathrm{time})^{-1}$, and $Q$ has units $\mathrm{time}^{-1}$. At $h=0$, the stable linear process has covariance determined by

$$
MC\Sigma+\Sigma CM=Q.
$$

A single equilibrium-like temperature is consistent with this chosen gradient/mobility model when

$$
Q=2k_BT_{\mathrm{eff}}M.
$$

Then $\Sigma=k_BT_{\mathrm{eff}}C^{-1}$ and the stationary density is proportional to $e^{-V/(k_BT_{\mathrm{eff}})}$. This is the additional noise–mobility relation; it is not implied by a pair of deterministic decay rates. If $Q$ is not a scalar multiple of $M$, different directions generally give different ratios and this equilibrium scalar-temperature model fails.

For example, choose units $E_0,t_0>0$, normalized time $\tau=t/t_0$, and field $\widetilde h=h/E_0$. The process $dx=(-2x+\widetilde h)d\tau+\sqrt{2d}\,dW_\tau$ has $\Sigma=d/2$ and physical static susceptibility $\chi(0)=1/(2E_0)$, so $k_BT_{\mathrm{eff}}=E_0d$. Splitting its restoring rate $2/t_0$ into two named rates $1/t_0$ leaves their ratio one while arbitrary $d>0$ changes the fluctuation temperature.

This OU process is an exact chosen model on $\mathbb R^m$. Its use for bounded Gap observables or local coordinates of a PSD coherence matrix is a **local approximation/bridge** [C/H]. Unbounded Gaussian coordinates do not themselves ensure global PSD, trace one, or $0\le\mathrm{Gap}\le1$; an actual state-valued realization or boundary dynamics must be specified separately.

### Categorical formula: withdrawn universal implication

An abstract natural transformation has no canonical operator norm without a specified enriched realization and norms. An adjunction alone supplies neither $Q$, $M$, an energy unit nor a thermal bath. The former counit formula $(1+\|\varepsilon\|)/(1-\|\varepsilon\|)$ is therefore not a categorical derivation of temperature.

One can instead **define** $\eta=(r_0-1)/(r_0+1)\in(-1,1)$, giving $r_0=(1+\eta)/(1-\eta)$ by algebra. Replacing $\eta$ by a nonnegative norm further restricts $r_0\ge1$ by choice. The asymptotic expression $\eta=1-2/r_0+O(r_0^{-2})$ holds only for large $r_0$; none of these parametrizations proves a physical identification.

## 3. Critical temperature requires a selected model {#критическая-температура}

A dimensionless mass parameter $\mu^2$ does not have energy units. A temperature such as $E_0\mu^2/(k_B\ln21)$ requires a declared energy scale $E_0$ and a statistical model producing that formula.

For a concrete finite model with one ground state and 21 excited states of energy $\Delta>0$,

$$
Z=1+21e^{-\Delta/(k_BT)},\qquad T_*=\frac{\Delta}{k_B\ln21}
$$

is the temperature of equal total ground/excited probabilities. Its finite partition function is analytic for $T>0$; $T_*$ is a crossover, not a thermodynamic singularity. Twenty-one coherence pairs do not by themselves imply 21 equal-energy microstates or this partition function.

### Criticality and consciousness {#фазовый-переход-сознания}

A bifurcation or statistical transition needs a potential, dynamics, noise model and, where relevant, a thermodynamic/spatial limit. Connecting it to reports or Cap₂ requires an independent readout [H/I]. Neither a mode count nor the ratio convention fixes a universal $T_c$ or an L1–L4 correspondence. Use the [specified Gap phase models](/docs/core/dynamics/gap-phase-diagram) rather than a universal three-phase claim.

## 4. Fibers, connections and holonomy {#кривизна-серра}

A projection from internal states to observable behavior defines observational fibers. A Serre fibration additionally needs the homotopy-lifting property; a general observation map does not possess it automatically. A smooth connection and its curvature require specified smooth bundle data and a chosen horizontal distribution. Serre fibrations alone have no canonical differential curvature.

No universal identity $\|R_H\|_{ij}\propto|\gamma_{ij}|\mathrm{Gap}(i,j)$ follows from these definitions. Phase-triangle holonomy, connection holonomy and Berry holonomy are different constructions and need a demonstrated bridge. Neither a temperature nor a nontrivial fiber proves phenomenal content. See [reconstruction fibers and phase information](/docs/applied/research/reconstruction-identifiability).

## 5. Fisher geometry requires an observation model {#метрика-фишера}

For a differentiable likelihood $p(y\mid\theta)$ satisfying its regularity conditions, classical Fisher information is

$$
g_{ab}(\theta)=\mathbb E_\theta[\partial_a\log p\,\partial_b\log p].
$$

It is positive semidefinite; unresolved parameter directions can be null. Positive definiteness requires identifiable regular directions. For a fixed measure and a Gibbs model $p\propto e^{-V_\theta/\Theta}$ with **constant** $\Theta$, it reduces to $\operatorname{Cov}(\partial_aV,\partial_bV)/\Theta^2$. Variable temperature, parameter-dependent measures or an unspecified likelihood require additional terms/data.

Quantum Fisher metrics require a specified state family and metric normalization; they are not interchangeable with classical feature Fisher information. A pullback can be degenerate for a many-to-one Gap map. No universal “softening at $T_c$”, subjective distinguishability or optimal therapeutic path follows from the metric alone. Geodesic optimality refers only to the selected metric-length objective, not physical control cost or treatment outcomes.

## 6. Measuring a fluctuation temperature {#измерение}

For the scalar equilibrium-like model, with the **same observable and its calibrated conjugate field**, static FDT gives

$$
T_{\mathrm{eff}}=\frac{\operatorname{Var}(x)}{k_B\chi(0)}.
$$

For a stationary classical process, define the two-sided angular-frequency spectrum by $S_{xx}(\omega)=\int_{\mathbb R}e^{i\omega t}\langle\delta x(t)\delta x(0)\rangle dt$, and susceptibility by the response to $h(t)\propto e^{-i\omega t}$. Under equilibrium FDT, for $\omega>0$ with positive dissipative response,

$$
S_{xx}(\omega)=\frac{2k_BT_{\mathrm{eff}}}{\omega}\operatorname{Im}\chi(\omega),\qquad
T_{\mathrm{eff}}(\omega)=\frac{\omega S_{xx}(\omega)}{2k_B\operatorname{Im}\chi(\omega)}.
$$

For scalar mobility $m$ and curvature $c$, $\chi(\omega)=m/(mc-i\omega)$ and $S_{xx}=2mk_BT_{\mathrm{eff}}/((mc)^2+\omega^2)$. The zero-frequency expression is obtained by a limit, not division by zero. Specify angular versus ordinary frequency and one-sided versus two-sided spectra before comparing normalizations. Wiener–Khinchin defines the covariance/spectrum relation; it does not independently impose FDT.

Preregister the observable, energy calibration, weak perturbation, time window, stationarity checks, detector noise, covariance estimation and uncertainty. Verify response linearity and test whether a common temperature fits the selected modes/frequencies. A frequency-dependent FDT ratio may be reported as an operational effective temperature [D/C], but thermodynamic meaning requires further equilibration conditions. See [Kubo](https://doi.org/10.1143/JPSJ.12.570) and the explicit nonequilibrium constructions of [Cugliandolo, Kurchan & Peliti](https://arxiv.org/abs/cond-mat/9611044).

No EEG power, HRV, reported recovery time or learning rate alone measures this conjugate response/noise ratio. Unknown calibration and incomplete complex phases remain [identification problems](/docs/applied/research/reconstruction-identifiability#observation-model).

## 7. Other uses of “temperature” {#связь-с-другими-температурами}

Noise temperature, spectral/color temperature, annealing parameters and Hawking temperature have different definitions and assumptions. An annealing score becomes a physical temperature only with an energy calibration and appropriate stochastic realization. Analogies do not identify a cognitive fiber with an event horizon or derive its temperature from information loss alone.

## 8. Phase-diagram coordinates {#фазовая-диаграмма}

If $T_{\mathrm{eff}}$, $T_c$, $\kappa$ and $\Gamma_2$ are defined and positive, $t=T_{\mathrm{eff}}/T_c$ and $r=\kappa/\Gamma_2$ are dimensionless choices [D]. They need not be independent: under $\kappa=\kappa_0$ and the ratio convention, $tr=T_{\mathrm{phys}}/T_c$. At fixed $T_{\mathrm{phys}}$ and $T_c$, this restricts the diagram to a curve. If $\kappa$ is a different total/gated rate, specify that relation; do not silently exchange it with $\kappa_0$.

The lines, coexistence regions and critical point depend on the selected potential and kinetics. Coordinates alone do not derive three universal phases, a critical $r_c$ or diagnoses such as coma, dissociation or borderline personality disorder [H/I].

### Line-resolved rates and temperatures {#линейные-температуры}

For the chosen diagonal Fano-jump family,

$$
r_{ij}=\frac16\sum_{|\ell_p\cap\{i,j\}|=1}\gamma_p,\qquad\gamma_p\ge0.
$$

The $21\times7$ incidence matrix has rank seven; noiseless identifiable pairwise rates determine seven line rates and obey 14 linear relations. Uniform $\gamma_p=\gamma$ yields $r_{ij}=2\gamma/3$. This is a statement about the chosen **rates**, not seven measured temperatures. Determining line temperatures also needs line noise amplitudes, mobility/response and energy calibration. A violation rejects the calibrated Fano-jump model, not every possible physical dissipator. See [the rate-tomography test](/docs/reference/falsifiability#f-rank7-ранг-7-анизотропия-декогеренции).

## 9. Control parameter and critical exponents {#параметр-порядка}

Temperature is a control parameter; an order parameter is a separately defined response. For the chosen deterministic quartic potential $F(A)=aA^2/2+uA^4/4$, $u>0$, its minima obey $A^2=-a/u$ for $a<0$. If $a\propto T-T_c$, the amplitude exponent is $1/2$, while a quadratic quantity such as $\mathcal G_{\mathrm{total}}\propto A^2$ scales with power one. At a tuned even sixth-order potential with vanishing quartic coefficient, the amplitude exponent is $1/4$. These are conditional algebraic normal-form results, not universal measured exponents of the full state dynamics.

Twenty-one complex coherence pairs are an internal mode count, not spatial dimension $d=21$ or a thermodynamic large-$N$ limit. Determinism alone neither selects a normal form nor excludes noise/finite-size corrections in a physical realization. A finite stable Gaussian/Gibbs model has no automatic singular critical temperature. See [corrected criticality scope](/docs/consciousness/hierarchy/swallowtail-transitions#механизм-точности).

### Erasure work

Landauer concerns physical entropy reduction with a thermal reservoir. Under its conditions, erasing $b$ independent unbiased bits has a bound $Q\ge b k_BT_{\mathrm{bath}}\ln2$, with finite-bath/correlation corrections; see [Reeb & Wolf](https://arxiv.org/abs/1306.4352). Twenty-one continuous Gap parameters do not equal 21 bits, and a rate-ratio/FDT temperature is not automatically the bath temperature. No universal energy cost of “enlightenment” or transparency follows from the former $21k_BT_{\mathrm{eff}}\ln2$ expression. Physical cost requires a specified encoding, entropy change, bath and process.

## 10. Status of the statements {#сводная-таблица}

| Statement | Scope |
|---|---|
| Ratio convention | [D]; temperature $r_0T_{\mathrm{phys}}$ and energy $k_Br_0T_{\mathrm{phys}}$ distinguished |
| Scalar FDT temperature | [C] under calibrated stationary linear-response/noise–mobility assumptions |
| Comparison with body temperature | [H/C] measured per system; no universal strict inequality |
| Counit formula | Universal implication withdrawn; optional algebraic parametrization [D] |
| $\Delta/(k_B\ln21)$ | Crossover of a selected finite degeneracy model; no automatic critical point |
| Fisher/connection geometry | Requires a likelihood or bundle and its stated regularity |
| Fano rate relations | Conditional algebra for the selected jump family; temperature identification separate |
| Critical/phenomenal/clinical interpretation | Model-dependent [H/I]; all Cap₂ conjuncts still required |

## Operational consequences {#что-мы-узнали}

Publish the stochastic model, measured fluctuation and conjugate response, units and uncertainty. Compare the inferred FDT temperature with the separately chosen ratio model rather than identify them by definition. Keep covariance, phase observability, physical rate calibration and biological/phenomenal interpretation distinct. No additional universal theorem is introduced here.

## Related documents

- [State dynamics and rate models](/docs/core/dynamics/evolution)
- [Observation and reconstruction](/docs/applied/research/reconstruction-identifiability)
- [Gap thermodynamics](/docs/core/dynamics/gap-thermodynamics)
- [Defined capability thresholds](/docs/reference/mathematical-kernel#thresholds)
