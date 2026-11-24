---
sidebar_position: 2
title: "Quark mixing and tests of flavour models"
description: "Independent mass inputs, basis misalignment and a texture test"
---

# Quark mixing and tests of flavour models

## Relative flavour bases {#6-ckm-из-несовпадения-юкавских-текстур}

<a id="ckm-non-circularity"></a>
<a id="thm-10-1-t-265"></a>

Let $U_{uL},U_{dL}$ diagonalize $Y_uY_u^\dagger,Y_dY_d^\dagger$ in the same weak basis. With three left-handed quark doublets and the usual charged current, $V=U_{uL}^\dagger U_{dL}$ is unitary. Specifying the six singular values does not determine this product. At fixed masses one may vary a left unitary rotation of $Y_d$ relative to $Y_u$. A spectral model that takes the Yukawa matrices as input can compute $V$, but testing flavour dynamics requires an independent origin for those matrices. [Example of a finite spectral model](https://arxiv.org/abs/hep-th/0610241).

## A texture tested on another observable {#derivation-vus}

A zero in a mass matrix is a basis-dependent statement. A texture hypothesis must fix the form of both matrices in a common basis. In the Hermitian six-zero Fritzsch ansatz, $V_{cb}$ is a sum of three complex terms with two adjustable relative phases. For the running masses in the repository test at $M_Z$, $(m_u,m_c,m_t)=(0.00123,0.620,168.26)$ GeV and $(m_d,m_s,m_b)=(0.00267,0.05316,2.839)$ GeV, diagonalization gives their magnitudes $a_i$ as $0.00002491$, $0.13181608$ and $0.05993983$. Opposing the smaller terms to the largest attains the triangle bound $2\max_i a_i-\sum_i a_i=0.07185$. The reference value in this test is $0.04183$. Agreement of $\sqrt{m_d/m_s}$ with a Cabibbo estimate does not repair that failure. [Reproducible mass and mixing checks](https://github.com/gst-st/uhm/blob/main/website/scripts/check_core_numbers.py).

## The seven-tick clock {#11-вкус-с-часов}

<a id="thm-4-2"></a>

The shift has seven distinct complex eigenvalues. Every operator commuting with it is diagonal in its Fourier basis. If both mass operators preserve the individual family modes and have nondegenerate spectra, their relative basis gives a permutation up to phases. Obtaining a physical mixing angle and CP phase requires an interaction that distinguishes the two bases. Fitting a correction to the measured phase uses that measurement as input. [Clock harmonics](./fermion-generations#поколения-t328).

## Orbifold Wilson-line no-go, modular CP violation, and CKM audit on $M = 7$ {#orbifold-ckm-cp-audit}

Testing CKM mixing and Jarlskog CP violation $J_{\mathrm{CP}}$ directly inside the magnetized $(T^2/\mathbb{Z}_2, M = 7)$ two-Higgs-doublet model (`verify_deep_frontier_v6.py`–`verify_deep_frontier_v8.py`, `ToEFrontierV7.lean`) establishes three sharp obstructions alongside the surviving $SU(2)_L$-invariant pathway:

1. **Discrete $\mathbb{Z}_2$ Wilson-line fixed-point no-go (`discrete_wilson_line_m7_disjoint_or_wrong_ng`) [T] / [✗]:** Every nontrivial discrete twist $(\alpha, \beta) \neq (0, 0)$ either shifts $d_R$'s active fixed point off $Q_L$'s $z_{\mathrm{top}} = (\frac{1}{2}, \frac{1}{2})$ or activates 3 fixed points ($N_{\mathrm{odd}} = 4 \neq 3$).
2. **Exact real vacuum at $\tau = 1.5i$, same-flux hierarchy-vs-CP no-go, and $SU(2)_L$ no-go against $(Y^a)^*$ [✗]:** At purely imaginary $\tau = 1.5i$, the Yukawa tensor is purely real ($\max\lvert\mathrm{Im}\,Y\rvert = 1.4\times 10^{-17}$) and the real CP-conserving vacuum attains the strict global minimum with exact $J_{\mathrm{CP}} = 0$. At complex $\tau = 0.25 + 1.5i$ with identical flux $M_u = M_d = 7^-$, weak repulsion (`lam_ud = 0.05`) preserves both hierarchies ($r_u = [1.9\times 10^{-5}, 4.1\times 10^{-3}, 1]$, $r_d = [1.2\times 10^{-3}, 1.8\times 10^{-2}, 1]$) yet gives tiny $\lvert V_{cb}\rvert = 0.0035$ and $J_{\mathrm{CP}} = 1.34\times 10^{-8}$, whereas strong repulsion (`lam_ud = 0.45`) restores $J_{\mathrm{CP}} = 7.29\times 10^{-6}$ at the cost of flattening $r_d = [0.11, 0.43, 1]$ and forcing $\lvert V_{us}\rvert = 0.994$. Conjugating the entire down-quark tensor $M_d \to \sum v_{d,a}(Y^a)^*$ explicitly breaks $SU(2)_L$ on $Q_L = (u_L, d_L)$ ($M(d_L) = -7 \neq M(u_L) = +7$), while conjugating only $d_R^c$ forces $M_{H_d} = 0$ and $Y_d = I_3$ (error $2.2\times 10^{-16}$).
3. **Genuine $SU(2)_L$-invariant $T_{3R}$-shifted zero-brane 2HDM [C] / [P]:** Choosing $M_Q = M_{u^c} = 7^-$, $M_{d^c} = 4^+$ ($M_{H_u} = 14^+$, $M_{H_d} = 11^-$) at complex $\tau = 0.25 + 1.5i$ (`c_d = 30`) breaks modular CP explicitly while preserving $SU(2)_L$ exactly, yielding $r_u = [2.2\times 10^{-5}, 3.8\times 10^{-3}, 1]$, $\lvert V_{cb}\rvert = 0.092$, $\lvert V_{ub}\rvert = 0.0081$, and $J_{\mathrm{CP}} = 1.92\times 10^{-5}$ (vs. SM $3.1\times 10^{-5}$). Reproducing $\lvert V_{us}\rvert = 0.225$ (currently $0.057$) and $m_s/m_b = 0.021$ (currently $0.086$) without breaking unified $M = 7$ $\mathrm{PSL}(2,7)$ symmetry on $d_R^c$ remains open [P].
