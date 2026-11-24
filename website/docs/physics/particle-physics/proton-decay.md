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

In UHM's two-loop clock-stabilizer Pati–Salam chains (`verify_deep_frontier_v3.py`, `verify_deep_frontier_v4.py`, `verify_deep_frontier_v7.py`–`verify_deep_frontier_v9.py`, `ToEFrontierV9.lean`), $M_X = M_{\mathrm{GUT}}$ and $\alpha_{\mathrm{GUT}}$ are fixed by PDG 2024 electroweak couplings without free gauge parameters ([RG Flow](../gauge-symmetry/rg-flow#spin10-two-loop-rg)):

- **Minimal `Chain A1` and `Chain A2` [C]:** `Chain A1` predicts $\tau(p \to e^+\pi^0) \approx 1.22\times 10^{36}\,\mathrm{yr}$ ($M_{\mathrm{GUT}} = 1.20\times 10^{16}\,\mathrm{GeV}$), while non-PQ `Chain A2` predicts $\tau(p \to e^+\pi^0) \approx 9.08\times 10^{34}\text{–}2.27\times 10^{35}\,\mathrm{yr}$ ($M_{\mathrm{GUT}} = 7.95\times 10^{15}\,\mathrm{GeV}$, $\alpha_{\mathrm{GUT}}^{-1} = 45.13$) — strictly above Super-Kamiokande ($> 2.4\times 10^{34}\,\mathrm{yr}$) and directly inside the **Hyper-Kamiokande** / **DUNE** discovery window. By contrast, `Chain B` ($5.20\times 10^{33}\,\mathrm{yr}$) is falsified [✗].
- **Hard anti-correlation ceiling ($r = -0.928$) [C]:** Across Hall–Weinberg GUT threshold variations ($\lvert\Delta\alpha_i^{-1}\rvert \le 1.0$), raising $M_{\mathrm{PS}}$ lowers $M_{\mathrm{GUT}}$ and $\tau_p$ with correlation $r(\log_{10} M_{\mathrm{PS}}, \log_{10}\tau_p) = -0.928$, enforcing $M_{\mathrm{PS}} \le 3.06\times 10^{11}\,\mathrm{GeV}$ (which rules out naive Pati–Salam Type-I seesaw $Y_\nu = Y_u$ by a factor of $2042\times$; see [Neutrino Masses](./neutrino-masses#nonpq-chain-a2-seesaw)).
- **Dark-matter exclusion via proton decay — including $\mathbf{54}_F$ & $\mathbf{210}_F$ GUT thresholds (`F-33A,B`) [T] / [✗]:** Super-Kamiokande directly falsifies TeV-scale $\mathbf{10}_F$ doublets ($\tau_p = 3.59\times 10^{28}\,\mathrm{yr}$), isolated $\mathbf{45}_F$ triplets ($\tau_p = 1.28\times 10^{29}\,\mathrm{yr}$), $(1,5,0)_F$ quintuplets ($\tau_p = 1.50\times 10^{22}\,\mathrm{yr}$), and inert $\mathbf{16}_H$ doublets ($\tau_p = 5.27\times 10^{33}\,\mathrm{yr}$). Moreover, zero-axiom group theory (`spin10_54F_210F_fimp_threshold_ratios`) proves that tuning the $(1,1,1)_F$ FIMP singlet to $m_\chi \ll M_{\mathrm{GUT}}$ under $\langle\mathbf{54}_H\rangle = v\,\mathrm{diag}(2^6,-3^4)$ locks sign-invariant partner mass ratios `6:4:1` for $\mathbf{54}_F$ ($\Delta_{4C}-\Delta_{2L} = \frac{1}{3\pi}\ln(6561/16) = +0.6384 \implies M_{\mathrm{GUT}} \to 3.50\times 10^{15}\,\mathrm{GeV}$, $\tau_p = 3.16\text{–}3.50\times 10^{33}\,\mathrm{yr}$, **$7.6\times$ Super-K excluded**; even $5\times$ inverted $\mathbf{54}_H$ scalar splitting $R_H = 0.2$ gives $1.84\times 10^{34}\,\mathrm{yr}$, requiring extreme inversion $R_H < 0.157$) and `4:3:2:1` for $\mathbf{210}_F$ ($\Delta_{4C}-\Delta_{2L} = \frac{1}{3\pi}\ln 324 = +0.6134 \implies \tau_p = 3.23\text{–}4.65\times 10^{33}\,\mathrm{yr}$, **$7.4\times$ Super-K excluded**). Only the pure $\mathrm{Spin}(10)$-singlet $\chi_1 = \mathbf{1}_F$ has zero GUT partners ($\Delta_a \equiv 0$) and uniquely preserves $\tau_p = 9.08\times 10^{34}\,\mathrm{yr}$ ([Dark Matter](../cosmology-phys/dark-matter#z2-dm-audit)).
