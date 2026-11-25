---
sidebar_position: 4
title: "Higgs representation and mass inputs"
description: "Colour neutrality, a weak doublet and the normalization of a scalar potential"
---

# Higgs representation and mass inputs

## Identifying a Higgs doublet {#теорема-отождествление-хиггса}

<a id="запрет-второго-дублета"></a>
<a id="юкавы-t340"></a>
<a id="голоморфность-вп"></a>

A candidate order parameter must transform with the required colour, weak and hypercharge assignments. For colour stabilizing $e_O$, the six perpendicular real axes mix. An isolated nonzero coherence on the axes $E,U$ therefore fails to be a colour-singlet vacuum under that action. The unique Fano line through two marked points determines incidence; establishing a Higgs doublet requires a representation and its gauge transformations. Counting such lines does not constrain additional scalar multiplets. [Colour representations](../gauge-symmetry/standard-model).

## Mass and self-coupling {#теорема-f0-канонический}

<a id="итоговая-оценка-mh"></a>

For a canonically normalized doublet with $V(H)=-\mu^2H^\dagger H+\lambda(H^\dagger H)^2$, $\mu^2,\lambda>0$, take $H=(0,(v+h)/\sqrt2)^T$. Stationarity gives $v^2=\mu^2/\lambda$. The curvature is $m_h^2=2\lambda v^2$ and the third derivative at the vacuum is $6\lambda v$. These relations apply to this specified tree-level potential. Choosing $v$ and the measured Higgs mass fixes $\lambda$ at this order. Comparing the resulting trilinear coupling against independent data tests the shape of the potential.

## Conditions for a vacuum transition {#4-4}

<a id="скорость-хирального-туннелирования"></a>

A tunnelling rate requires at least two specified configurations, a kinetic term, a potential barrier and boundary conditions for the transition. A static incidence tensor gives none of the barrier, spacetime scale or action evaluated along the path. [Conditional experimental comparisons](../../reference/frontier-ledger).

## Two-loop SM Higgs criticality at $M_{\mathrm{PS}}$ and the Vissani hierarchy obstruction {#higgs-criticality-vissani}

Evaluating the scalar sector inside UHM's non-SUSY $\mathrm{Spin}(10) \to G_{422} \to G_{\mathrm{SM}}/\mathbb{Z}_6$ `Chain A2` (`verify_deep_frontier_v7.py`, `ToEFrontierV7.lean`) separates vacuum stability (which succeeds) from electroweak naturalness (which faces an irreducible finite threshold obstruction):

1. **Two-loop SM Higgs criticality & CCvS $\Delta_R$ threshold stabilization (`F-42`, `verify_deep_frontier_v11.py` V11.3.C, `verify_deep_frontier_v12.py` V12.2.C) [C]:** Running the PDG 2024 Standard Model couplings ($m_t = 172.57\text{–}172.69\,\mathrm{GeV}$, $m_h = 125.25\,\mathrm{GeV}$) at two loops drives the Higgs quartic coupling $\lambda_H(\mu)$ through zero at $\mu_{\mathrm{inst}} = 1.35\text{–}5.28\times 10^{10}\,\mathrm{GeV}$ (`v11.py` Buttazzo $m_t=172.69\,\mathrm{GeV}$ vs. `v7.py` $m_t=172.57\,\mathrm{GeV}$; 2-loop Buttazzo running gives $\lambda_H(M_{\mathrm{PS}}^-) = -0.00412$ at `Chain A2` $M_{\mathrm{PS}} = 1.45\times 10^{11}\,\mathrm{GeV}$, $\lambda_H(M_{\mathrm{Pl}}) = -0.01021\text{ to }-0.01283$, and $\lambda_H^- = -0.00344\text{ to }-0.00366$ for `Split-C/R` at $M_{\mathrm{heavy}}=10^{15}\,\mathrm{GeV}$). Because UHM's Pati–Salam symmetry-breaking scale $M_{\mathrm{PS}} \approx 0.93\text{–}1.45\times 10^{11}\,\mathrm{GeV}$ (in both `Chain A2` and the Heavy-Threshold Split CCvS lift, `F-42`) sits directly above $\mu_{\mathrm{inst}}$, integrating out the heavy scalar $\Delta_R = (\overline{10},1,3)$ induces the positive tree-level portal shift $\lambda_H(M_{\mathrm{PS}}^+) = \lambda_H(M_{\mathrm{PS}}^-) + \lambda_{H\Delta}^2 / \lambda_\Delta$: stabilizing the electroweak vacuum for $\lambda_{H\Delta}/\sqrt{\lambda_\Delta} \ge 0.059\text{–}0.064$ and simultaneously matching the positive Connes–Chamseddine–van Suijlekom NCG boundary ($\lambda_H^+ \approx 0.10$) at $\lambda_{H\Delta}/\sqrt{\lambda_\Delta} \approx 0.322\text{–}0.323$ for $m_h = 125.25\,\mathrm{GeV}$ (curing the classic $170\,\mathrm{GeV}$ NCG Higgs-mass tension without supersymmetry). Note that because **`Super-F-40`** closes all 4D Dirac spectral actions for gravity, this CCvS Pati–Salam scalar mechanism operates strictly as the **Stratum-B** internal matter/Higgs sector ([RG Flow](../gauge-symmetry/rg-flow#ccvs-pati-salam-rge)).
2. **Finite $\overline{\mathrm{MS}}$ Vissani hierarchy obstruction & heavy-scalar naturalness (`vissani_hierarchy_tuning_lower_bound_cq`, `V12.2.C`) [T] / [✗] / [P]:** Even setting aside quadratic UV divergences, integrating out heavy right-handed neutrinos $N_i$ induces a **finite** one-loop $\overline{\mathrm{MS}}$ Higgs mass-squared shift $\delta m_H^2 \sim y_\nu^2 M_N^2 / (4\pi^2)$. Naturalness ($\lvert\delta m_H^2\rvert \le m_h^2$) caps $M_N \le 5.73\times 10^6\,\mathrm{GeV}$ (conservatively $7.21\times 10^6\,\mathrm{GeV}$). At `Chain A2`'s actual $M_{N_3} = 3.005\times 10^{11}\,\mathrm{GeV}$ and $y_{\nu 3} = 0.542$, classical scale invariance cannot protect the electroweak scale, forcing irreducible fine-tuning $\Delta_{\mathrm{EW}}(N_3) = 8.58\times 10^{16}$ ($\ge 1.45\times 10^{17}$ for $y = 1$). Extending this finite Vissani audit to the CCvS scalar thresholds ($\lambda_{\mathrm{portal}} = 0.10$) yields $\Delta_{\mathrm{EW}}(\Delta_R) \approx (0.71\text{–}1.69)\times 10^{15}$ per dof (`Split-C` to `Chain A2`) and $\Delta_{\mathrm{EW}}(M_{\mathrm{heavy}}=10^{15}\,\mathrm{GeV}) \approx 8.07\times 10^{22}$ per dof, compounded by $10^{-8}$ tree / $(2.4\text{–}4.4)\times 10^{-7}$ 1-loop tuning on $M_{\Delta_R}$ from $R = 0.5000$ portals [T] / [✗]. Resolving both the $10^4\times$ UV split and the $v_{\mathrm{EW}}/M_{\mathrm{Pl}} \sim 10^{-17}$ hierarchy without supersymmetry remains open [P].
