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

1. **Two-loop SM Higgs criticality cured at $M_{\mathrm{PS}}$ [C]:** Running the PDG 2024 Standard Model couplings ($m_t = 172.57\,\mathrm{GeV}$, $m_h = 125.25\,\mathrm{GeV}$) at two loops drives the Higgs quartic coupling $\lambda_H(\mu)$ through zero at $\mu_{\mathrm{inst}} = 5.28\times 10^{10}\,\mathrm{GeV}$ ($\lambda_H(M_{\mathrm{PS}}) = -0.00089$, $\lambda_H(M_{\mathrm{Pl}}) = -0.01021$). Because UHM's Pati–Salam symmetry-breaking scale $M_{\mathrm{PS}} \approx 9.19\times 10^{10}\text{–}1.43\times 10^{11}\,\mathrm{GeV}$ lies directly at $\mu_{\mathrm{inst}}$, the scalar threshold coupling to $\Delta_R = (10,1,3)$ shifts $\lambda_H$ upward and stabilizes the electroweak vacuum up to $M_{\mathrm{Pl}}$.
2. **Finite $\overline{\mathrm{MS}}$ Vissani hierarchy obstruction (`vissani_hierarchy_tuning_lower_bound_cq`) [T] / [✗] / [P]:** Even setting aside quadratic UV divergences, integrating out heavy right-handed neutrinos $N_i$ induces a **finite** one-loop $\overline{\mathrm{MS}}$ Higgs mass-squared shift $\delta m_H^2 \sim y_\nu^2 M_N^2 / (4\pi^2)$. Naturalness ($\lvert\delta m_H^2\rvert \le m_h^2$) caps $M_N \le 5.73\times 10^6\,\mathrm{GeV}$ (conservatively $7.21\times 10^6\,\mathrm{GeV}$). At `Chain A2`'s actual $M_{N_3} = 3.005\times 10^{11}\,\mathrm{GeV}$ and $y_{\nu 3} = 0.542$, classical scale invariance cannot protect the electroweak scale, forcing irreducible fine-tuning $\Delta_{\mathrm{EW}} = 8.58\times 10^{16}$ ($\ge 1.45\times 10^{17}$ for $y = 1$). Resolving the $v_{\mathrm{EW}}/M_{\mathrm{Pl}} \sim 10^{-17}$ hierarchy without supersymmetry remains open [P].
