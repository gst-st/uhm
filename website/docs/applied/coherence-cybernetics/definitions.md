---
sidebar_position: 2
title: Coherence Cybernetics Definitions
description: Typed model records, exact statistic ranges, and a selected diagnostic panel
---

# Coherence Cybernetics Definitions

## Model record

A holon in the seven-axis model specifies $(\rho,H,\mathcal L,M,a,\mathcal E,q_E,p_\rho,\mathcal U)$: state, Hamiltonian, linear dissipator, numerical self-model, feedback rate, experiential extension and readout, observation law, and admissible controls. Frame and physical calibration are explicit. Self-sufficiency requires a concrete dynamic viability condition; static purity alone does not imply it.

$\rho\in\mathcal D_7$ is a selected subsystem space. Two joint factors have dimension 49. A lift into a selected 42-dimensional space and its readout are separate data; they are not a universal Morita equivalence or a tensor E-factorisation of $\mathbb C^7$.

## Statistics

| Quantity | Definition | Exact range |
|---|---|---|
| $P$ | $\operatorname{Tr}\rho^2$ | $[1/7,1]$ |
| $S$ | $-\operatorname{Tr}\rho\log\rho$ | $[0,\log7]$ |
| $\Phi$ | $P/d-1$, $d=\sum_i\rho_{ii}^2$ | $[0,6]$ |
| Canonical $R$ | $1/(7P)$, a selected scalar | $[1/7,1]$ |
| $R_M$ | $1-\|\rho-M(\rho)\|_F^2/P$ | Not necessarily nonnegative; distinct from $R$ |
| $C$ | $\Phi R$, a selected product | $[0,6/7]$ |
| $D_{\rm diff}$ | $\exp S(q_E\mathcal E(\rho))$ for a specified lift | Depends on output-state dimension |

From $d\ge1/7$, $\Phi\le7P-1$ and $C=1/(7d)-1/(7P)\le6/7$. Purity is not a universal detection criterion against $I/7$: states below $2/7$ can have Helstrom advantage. Entropy is not determined by purity; it depends on the full spectrum. A pure state can have a large E-proxy, so $P=1$ does not imply zero experiential differentiation without a particular readout.

## E-Coherence {#e-когерентность}

### HS share {#coh-e-7d}

$$
\mathrm{Coh}_E(\rho)=\frac{\rho_{EE}^2+2\sum_{j\ne E}|\rho_{Ej}|^2}{P}\in[0,1].
$$

This is the squared-norm share of the HS E-row/column mask. The mask is orthogonal in operator space but is not a positive quantum channel or partial trace. $I/7$ has value $1/7$ with no E-couplings. The universal viable-state E-floor T-38a is withdrawn; a conditional flux balance requires explicit source and rate bounds.

### Extension and proxy {#coh-e-42d}

With a specified experience factor, compute its reduced state and effective entropy rank. The formula $D^{7D}=1+6\mathrm{Coh}_E$ is a separate proxy [D], not an entropy identity. Its cut $D^{7D}\ge2$ is equivalent to $\mathrm{Coh}_E\ge1/6$ by definition; this is not a theorem of dynamical necessity. An experience model specifies the lift, readout, and observation law.

## Capability hierarchy {#иерархия-интериорности}

L-levels use nested Cap certificates on the augmented record, as in [the rigorous hierarchy](/docs/consciousness/hierarchy/interiority-hierarchy). L2 requires four gates; L3 adds an independent predictive certificate; L4 a compatible tower of all orders. A scalar $C$, phase Gap, and iteration count do not determine these certificates. The phenomenal reading of each level is a separate bridge.

## Diagnostic panels and gate margins {#тензор-напряжений}

A seven-component resource/sector panel is a chosen diagnostic [D], not a proof of survival or consciousness. Specify its calibration, target and units. A diagonal deficit $1-7\rho_{kk}$ can take negative values, so its signed maximum is not its sup-norm. Neither convention alone determines purity: $I/7$ and the uniform pure state have the same diagonal but purities $1/7$ and one.

### Formal scope {#sigma-sys-formal}

The older formulas can be retained as **separate** raw scores:

$$
\tilde\sigma_A=1-\rho_{AA}/P,\quad\tilde\sigma_S=1-\operatorname{rank}(\rho_{ASD})/3,\quad
\tilde\sigma_D=1-7\rho_{DD},\quad\tilde\sigma_L=7(1-\rho_{LL})/6,
$$

$$
\tilde\sigma_E=(7-D_{\mathrm{diff}})/5,\quad\tilde\sigma_O=1-\kappa_0/\kappa_b,\quad
\tilde\sigma_U=2/(1+\Phi).
$$

Here $\rho_{ASD}$ is a principal block, not a tensor subsystem; a numerical-rank tolerance is an extra convention. $D_{\mathrm{diff}}$ requires an experiential realization or declared proxy, and $\kappa_0$ depends on the rate/regularization model. The scores are frame dependent, can be negative or discontinuous, and are not universally parameter free.

Let $\sigma_k=\max(0,\tilde\sigma_k)$ if a nonnegative panel is desired, and define $V_\sigma=\{\max_k\sigma_k<1\}$ **by convention**. Then $V_\sigma\subseteq\{P>2/7\}$ because its U-condition gives $\Phi>1$ and $\Phi\le7P-1$. This is an implication; $V_\sigma$ is not the whole capability gate. At every uniform-diagonal state $\tilde\sigma_L=1$, including states strictly inside the capability window. Also strict panel inequalities exclude equality at the inclusive integration/differentiation cuts.

For the canonical gate use the actual margin vector

$$
m=(P-2/7,\ R-1/3,\ \Phi-1,\ D_{\mathrm{diff}}-2).
$$

$\mathrm{Cap}_2$ holds exactly when $m_1>0$ and $m_2,m_3,m_4\ge0$ [T at the definitions]. Robust verdicts require margins larger than reconstruction error bounds. This panel tests a declared mathematical predicate; clinical, organizational and phenomenal readings remain calibration hypotheses.

The former universal T-92 equivalence and claims of parameter-free biological diagnostics are withdrawn. Use [identifiability](/docs/applied/research/reconstruction-identifiability) before assigning a verdict from data. Empirical demand/capacity panels and these state margins answer different questions and require a measured observation bridge.

<a id="панель-нагрузки"></a>

## Attractor and target {#иерархия-аттракторов}

A target $B(\rho)$, a self-model fixed point, and a stationary point of the full vector field are different objects. Frozen-target replacement converges to its target. With Hamiltonian and dissipation, stationarity requires full balance and does not imply $\rho=B(\rho)$. Nonlinear gates permit multiple basins. Psychological identification of a basin or critical point requires an empirical bridge.

## Observation and interfaces {#функтор-enc}

Physical reconstruction specifies $p_\rho(y\mid u)$ and proves identifiability. A neural feature, subjective report, and matrix entry are not identified without calibration. A simulated matrix does not establish a patient's clinical state or a language model's consciousness. [The reconstruction protocol](/docs/applied/research/reconstruction-identifiability) supplies uncertainty sets and an unresolved verdict.

### Control {#функтор-dec}

An admissible channel family and loss are specified. Compactness and continuity give minimum existence; safety, uniqueness, and efficient optimisation require extra hypotheses. A categorical name requires explicit composition laws, as in [the sensorimotor model](./sensorimotor).

<a id="геометрическая-интуиция"></a>
<a id="нейробиологические-корреляты"></a>

<a id="секторная-декомпозиция"></a>
<a id="целевое-состояние"></a>
