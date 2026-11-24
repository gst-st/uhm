---
sidebar_position: 3
title: "Yukawa matrices and masses"
description: "Mass scales, chiral symmetry and independent inputs"
---

# Yukawa matrices and masses

## Which data give a mass? {#thm-2-1}

With one canonically normalized Higgs doublet and vacuum value $v/\sqrt2$, a Yukawa matrix $Y$ gives $M=vY/\sqrt2$ at tree level. Its singular values are the fermion masses at the stated matching scale and convention. The Fano tensor with two marked indices can specify the support of a particular interaction. Even if a leading matrix has rank one, the coefficient sets the one nonzero mass. Other interactions determine whether the two zero singular values are lifted. [Fano vertex](../gauge-symmetry/fano-selection-rules).

## What running preserves {#3-quasi-ir-fixed-point-и-масса-t-кварка}

<a id="теорема-mb-mt"></a>
<a id="c7-nonperturbative"></a>

A flow of the form $dy/d\log\mu=yF(\mu,y)$ with a locally unique solution preserves the zero coupling. In particular, a perturbative model with an exact independent right-handed down-quark symmetry cannot generate its forbidden Yukawa term by running. A nonzero bottom mass in such a construction needs a symmetry-breaking interaction. Likewise, infrared focusing can reduce sensitivity to a nonzero initial top coupling, while gauge couplings, the scale interval, $v$ and matching corrections still enter the mass.

## Interpreting a hierarchy parameter {#9-аналитическая-формула-ε}

<a id="thm-5-2"></a>

In an ansatz $Y=\sum_r\epsilon^r A_r$, powers of $\epsilon$ alone leave the ranks, singular vectors and possible cancellations in the $A_r$ free. A fit to one mass ratio can calibrate $\epsilon$. A test requires fixed matrices, a common mass convention and a different ratio or mixing observable. An example is the cross-check of a six-zero texture with $|V_{cb}|$. [Mixing test](./ckm-matrix#derivation-vus).

## Veronese conic syzygy, bulk quartic no-go, and magnetized $M = 7$ Yukawa hierarchy {#veronese-conic-2hdm}

Evaluating the Yukawa overlap tensor $Y^a_{ij} = \int_{T^2} \chi_i(z)\chi_j(z) H_a(z)$ on the magnetized Fano orbifold $(T^2/\mathbb{Z}_2, M = 7)$ yields exact algebraic constraints and sharp dynamical obstructions (`verify_deep_frontier_v4.py`, `verify_deep_frontier_v6.py`, `verify_deep_frontier_v8.py`, `ToEFrontierDynamics.lean`, `ToEFrontierV8.lean`):

1. **Veronese conic syzygy (`veronese_conic_syzygy_dimension_pinch`) [T]:** The three odd Landau modes vanish at all three even fixed points $(0,0), (\frac{1}{2},0), (0,\frac{1}{2})$, imposing three constraints on the $8$-dimensional even Higgs space $H_{14}^+$ ($8 - 3 = 5 < 6 = \dim\mathrm{Sym}^2(H_3^-)$). This forces a unique pointwise Veronese conic syzygy $\sum Q_{ij}(\tau)\chi_i(z)\chi_j(z) \equiv 0$ ($\sigma_6(Y_{8\times 6}) = 4.58\times 10^{-17}$, $\max\lvert Q_{ij}\chi_i\chi_j\rvert = 8.80\times 10^{-15}$).
2. **Bulk quartic flatness no-go (`quartic_higgs_flatness_lower_bound_cq`) [✗]:** A pure bulk quartic potential $V_{\mathrm{quart}}[v] = \int_{T^2}\lvert H\rvert^4 \ge 1$ spreads the Higgs VEV across all 8 even modes ($V_{\min} = 1.1649$ at $\mathrm{Im}\,\tau = 1.5$), producing a quasi-degenerate spectrum $m_1:m_2:m_3 = [0.551, 0.894, 1.000]$ and destroying the mass hierarchy.
3. **Radiative rank-1 top dominance and zero-brane 2HDM hierarchies [C] / [P]:** On odd $M = 7$, radiative top-loop feedback focuses $H_u$ onto the unique active fixed point $z_{\mathrm{top}} = (\frac{1}{2},\frac{1}{2})$ ($\lambda_{\max}(K^{\mathrm{Yuk}}) = 7/2$, exact rank-1 top eigenvector $[1.3\times 10^{-16}, 5.5\times 10^{-16}, 1]$). In a strictly zero-brane coupled 2HDM $(H_u, H_d)$ at $\tau = 1.5i$ (`c_u = 12, c_d = 9, lam_ud = 0.05`), up- and down-quark hierarchies match SM targets at $M_{\mathrm{PS}}$ within $13\text{–}19\%$ ($r_u = [1.0\times 10^{-6}, 4.1\times 10^{-3}, 1]$, $r_d = [8.9\times 10^{-4}, 1.8\times 10^{-2}, 1]$), but with exact $J_{\mathrm{CP}} = 0$ and tiny $\lvert V_{cb}\rvert = 0.003$; moving to complex $\tau = 0.25 + 1.5i$ in a genuinely $SU(2)_L$-invariant $T_{3R}$-shifted 2HDM ($M_Q = M_{u^c} = 7^-$, $M_{d^c} = 4^+$) restores $r_u = [2.2\times 10^{-5}, 3.8\times 10^{-3}, 1]$ and realistic $J_{\mathrm{CP}} = 1.92\times 10^{-5}$, at the open cost of $m_s/m_b = 0.086$ ($4\times$ high) and broken unified $M = 7$ on $d_R^c$ ([CKM Matrix](./ckm-matrix#orbifold-ckm-cp-audit)).
