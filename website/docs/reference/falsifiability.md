---
sidebar_position: 3
title: "Falsifiability and predictions"
---

# Falsifiability and predictions

## What an observation can reject {#refutation-criterion}

An experimental claim needs a preparation, allowed interventions, recorded outcomes and a predicted distribution or interval. For a latent state $x$ and calibrated observation law $O$, let $C(y)$ contain every state compatible with the record $y$ and the calibration uncertainty. A predicted quantity $F$ is identified at $y$ exactly when $F$ is constant on $C(y)$. If a measured contrast lies outside the entire compatible prediction range after allowing for noise, it challenges the joint model. An interval overlapping competing predictions leaves the comparison unresolved. [Identifiability](../applied/research/reconstruction-identifiability#fiber-theorem).

## An intervention with competing outcomes {#summary-table-of-predictions}

On a network with two coherent arrival paths, two contributions at the same time can cancel in one detector setting. A calibrated sign reversal on one arm changes their sum into a difference. When at least one arm carries a nonzero amplitude, the two settings cannot both vanish. This statement assumes a linear response, control of the relative phase in the measured representation and a detector sensitive to the specified mode. A dark receiver alone does not identify a long path. A distinct experiment compares first-arrival delays for two calibrated probes on the same chain. [Network results and witnesses](./network-results).

## A seven-rate model {#f-rank7-ранг-7-анизотропия-декогеренции}

<a id="f-gap-1-внутри-триплетный-gap-ниже-межтриплетного"></a>
<a id="f-gap-2-блоковая-прозрачность-по-фано-триплетам"></a>
<a id="f-ξ-корреляционная-длина-фано"></a>

For the chosen family of Fano dephasing jumps, the pairwise decay rates obey $r=A\gamma$ with seven nonnegative rates $\gamma_p$. The row for $i,j$ has entry $1/6$ for a line containing exactly one of the indices and zero otherwise. The $21\times7$ matrix has rank seven. A measured rate vector must lie in its seven-dimensional column space and in the smaller cone $A\mathbb R^7_{\ge0}$. Fit rates from time-resolved data with Hamiltonian motion and feedback controlled, and test residuals allowing for correlated errors. One snapshot of the coherence magnitudes does not identify the rates. Every pair of Fano points lies on a line, so a comparison of line and off-line behaviour must define *triples* or an explicitly marked family of pairs. [Fano instrument](../proofs/gap/fano-channel).

## An exact constraint and its experimental bridge {#f-band-две-суммы-живого-состояния}

For a density matrix write $d=\sum_i\rho_{ii}^2$ and $q=\sum_{i\ne j}|\rho_{ij}|^2$. A specified gate requiring $q\ge d$, $2/7<d+q\le3/7$ implies $1/7\le d\le3/14$ and $1/7<q\le2/7$. Here $d\ge1/7$ follows from normalization. A matrix violating the bounds while passing the gate would disprove the algebra or reveal an implementation error. Applying the gate to a biological preparation additionally requires an independently calibrated encoder and outcome criterion. [Thresholds](./mathematical-kernel#thresholds).

## Reports of experience {#phenomenal-boundaries}

<a id="isospectral-discrimination"></a>
<a id="contextual-modulation"></a>
<a id="adaptation-dynamics"></a>
<a id="metric-relations"></a>
<a id="f-isf-isf-компоненты-в-фмрт"></a>
<a id="f-neural-нейронные-корреляты"></a>

| Comparison | Input to fix before collecting the test data | Held-out outcome |
|---|---|---|
| Isospectral preparations | Operational frame, indistinguishability margin for spectra, resolvable spectral projectors | A predicted report contrast for preparations satisfying the margin. |
| Context intervention | Which intensity readout is preserved and how the intervention changes context | Change in a specified report at comparable measured intensity. |
| Adaptation | Baseline window, response equation, coefficients, competing predictors | Time-resolved report error on new subjects or sessions. |
| Perceived distance | State-to-ray map and calibration of a proposed distance | Similarity judgements for new pairs or triples, with uncertainty on the triangle inequality. |

A behavioural report and the physical state reconstructed from instruments have different observation laws. Freeze both calibrations, comparison models, effect size, stopping rule and uncertainty analysis before the independent test. [Measurement protocol](../applied/research/measurement-protocol#substitution-position).

## Particle and cosmological models {#границы-теории}

<a id="f-τ_p-время-жизни-протона"></a>
<a id="f-m_t-масса-top-кварка-из-неподвижной-точки-пендлтона-росса"></a>
<a id="f-higgs-отклонение-самосвязи-хиггса"></a>
<a id="f-δ_cp-cp-фаза-ckm-из-фано-фазы"></a>
<a id="f-cabibbo-угол-кабиббо-из-rg-подавления-фано-угла"></a>
<a id="f-nedm-нейтронный-эдм"></a>
<a id="f-w-форма-дрейфа-тёмной-энергии"></a>
<a id="анализ-уязвимостей"></a>

A lifetime test needs an interaction and mediator scale. A mixing test needs two independently specified Yukawa matrices. A cosmological test needs an expansion or source model and calibrated distances or times. A fitted particle mass, vacuum-energy scale or mixing phase remains an input to subsequent predictions. The field models, comparison observables and necessary inputs for twelve particle searches are set out in the [frontier ledger](./frontier-ledger).

### Quantitative experimental targets of the `Chain A2` and QCA architecture {#quantitative-targets}

After eliminating falsified sub-models (`Chain B`, naive $Y_\nu = Y_u$ seesaw, PQ $\mathbf{10}_H \oplus \overline{\mathbf{126}}_H$, single-field WGC gravitational instantons, minimal $\mathbf{210}_F + \mathbf{210}_H$ DM), six sharp quantitative targets stand out for 2026–2040 observations [C]:

| Target | Quantitative signature | Primary experiment / falsification criterion |
|---|---|---|
| Proton decay $p \to e^+\pi^0$ | $\tau_p \approx 9.08\times 10^{34}\text{–}2.27\times 10^{35}\,\mathrm{yr}$ (`Chain A2`; `Chain A1`: $1.22\times 10^{36}\,\mathrm{yr}$) | Hyper-Kamiokande / DUNE ([Proton Decay](../physics/particle-physics/proton-decay#chain-a2-proton-decay)) |
| Neutrino mass sum & $0\nu\beta\beta$ | Normal ordering, $\sum m_\nu \approx 0.065\,\mathrm{eV} < 0.072\,\mathrm{eV}$, Majorana $\nu^c \in \mathbf{16}_+$ | DESI / Euclid, LEGEND-1000, nEXO ([Neutrino Masses](../physics/particle-physics/neutrino-masses#nonpq-chain-a2-seesaw)) |
| Absence of Clifford PQ axion | No PQ symmetry inside $\mathrm{Cl}_{0,7}$ (`T-333`); tree-level $\bar{\theta}_{\mathrm{tree}} = 0$ via $L \leftrightarrow R$ | ADMX / MADMAX (classic QCD axion detection refutes minimal axion-free branch), nEDM |
| Non-phantom thawing dark energy | $w(z) \ge -1$ ($w_0 \approx -0.81$ at $f = 0.7\,M_{\mathrm{Pl,red}}$; $\Delta\chi^2 = -8.35$ on DESY5) | DESI DR2+ / Euclid / Roman (confirmed phantom crossing $w < -1$ refutes single-field thawing; [Cosmological Constant](../physics/gravity/cosmological-constant#wgc-quintessence-boundary)) |
| Quartic QCA UV dispersion | Zero linear $O(E/M_{\mathrm{Pl}})$ shift; subluminal quartic $O(a^2 E^2)$ octahedral term only | Fermi-LAT, CTA, LHAASO |
| Laboratory quantum-information bounds | Bilocal complex contrast $6\sqrt{2} \approx 8.4853 > 7.6605$; $K_3$ Aharonov–Bohm spectrum; Choi $m_W(7)=245$ | Photonic / superconducting / Rydberg quantum simulators ([Network Results](./network-results)) |
