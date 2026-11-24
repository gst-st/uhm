---
sidebar_position: 7
slug: /physics/particle-physics/proton-decay
title: "Proton decay in a specified field model"
description: "Baryon-number violation, mediator-scale dependence and independent searches"
---

# Proton decay in a specified field model

## A dimension-six operator {#время-жизни}

Proton decay requires an interaction that violates baryon number. Suppose a heavy mediator with mass $M_X$ and coupling $g$ generates a dimension-six operator with coefficient proportional to $g^2/M_X^2$. For a fixed final state $f$, its amplitude also contains the running of the operator and its hadronic matrix element. At fixed couplings, running, phase space and matrix element this gives

$$
\Gamma(p\to f)\propto \frac{g^4}{M_X^4},\qquad \tau_f=1/\Gamma(p\to f)\propto M_X^4.
$$

Increasing $M_X$ by one decade then raises the partial lifetime by four decades. An abstract group embedding or a dimensionless hierarchy leaves the mediator mass and baryon-number-violating couplings undetermined.

## A test with a second channel {#каналы}

A bound on one partial lifetime constrains the corresponding operator coefficient. Using that bound to set the mediator scale spends it as input. If the same field model independently fixes the relative flavour couplings and matrix elements, a ratio of two partial rates can cancel a common $M_X^{-4}$ factor. Another channel can then distinguish competing operator assignments. Several contributing operators also require relative phases. [Conditional experimental comparisons](../../reference/frontier-ledger).

## Two-loop $\mathrm{Spin}(10) \to G_{422}$ lifetime predictions and the Super-K $M_{\mathrm{PS}}$ ceiling {#chain-a2-proton-decay}

In UHM's two-loop clock-stabilizer Pati–Salam chains (`verify_deep_frontier_v3.py`, `verify_deep_frontier_v4.py`, `verify_deep_frontier_v7.py`, `verify_deep_frontier_v8.py`), $M_X = M_{\mathrm{GUT}}$ and $\alpha_{\mathrm{GUT}}$ are fixed by PDG 2024 electroweak couplings without free gauge parameters ([RG Flow](../gauge-symmetry/rg-flow#spin10-two-loop-rg)):

- **Minimal `Chain A1` and `Chain A2` [C]:** `Chain A1` predicts $\tau(p \to e^+\pi^0) \approx 1.22\times 10^{36}\,\mathrm{yr}$ ($M_{\mathrm{GUT}} = 1.20\times 10^{16}\,\mathrm{GeV}$), while non-PQ `Chain A2` predicts $\tau(p \to e^+\pi^0) \approx 9.08\times 10^{34}\text{–}2.27\times 10^{35}\,\mathrm{yr}$ ($M_{\mathrm{GUT}} = 7.95\times 10^{15}\,\mathrm{GeV}$, $\alpha_{\mathrm{GUT}}^{-1} = 45.13$) — strictly above Super-Kamiokande ($> 2.4\times 10^{34}\,\mathrm{yr}$) and directly inside the **Hyper-Kamiokande** / **DUNE** discovery window. By contrast, `Chain B` ($5.20\times 10^{33}\,\mathrm{yr}$) is falsified [✗].
- **Hard anti-correlation ceiling ($r = -0.928$) [C]:** Across Hall–Weinberg GUT threshold variations ($\lvert\Delta\alpha_i^{-1}\rvert \le 1.0$), raising $M_{\mathrm{PS}}$ lowers $M_{\mathrm{GUT}}$ and $\tau_p$ with correlation $r(\log_{10} M_{\mathrm{PS}}, \log_{10}\tau_p) = -0.928$, enforcing $M_{\mathrm{PS}} \le 3.06\times 10^{11}\,\mathrm{GeV}$ (which rules out naive Pati–Salam Type-I seesaw $Y_\nu = Y_u$ by a factor of $2042\times$; see [Neutrino Masses](./neutrino-masses#nonpq-chain-a2-seesaw)).
- **Dark-matter exclusion via proton decay [✗]:** Super-Kamiokande directly falsifies TeV-scale $\mathbf{10}_F$ doublets ($\tau_p = 3.59\times 10^{28}\,\mathrm{yr}$), isolated $\mathbf{45}_F$ triplets ($\tau_p = 1.28\times 10^{29}\,\mathrm{yr}$), $(1,5,0)_F$ quintuplets ($\tau_p = 1.50\times 10^{22}\,\mathrm{yr}$), and inert $\mathbf{16}_H$ doublets ($\tau_p = 5.27\times 10^{33}\,\mathrm{yr}$), whereas pure Pati–Salam-singlet FIMP completions (`54_H + 54_F/210_F` and `1_F`) leave $\tau_p = 9.08\times 10^{34}\,\mathrm{yr}$ unchanged ([Dark Matter](../cosmology-phys/dark-matter#z2-dm-audit)).
