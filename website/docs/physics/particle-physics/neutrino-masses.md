---
sidebar_position: 5
slug: /physics/particle-physics/neutrino-masses
title: "Neutrino masses and mixing"
description: "What follows from a specified seesaw model and what oscillations determine"
---

# Neutrino masses and mixing

## Eliminating a heavy sector {#seesaw}

<a id="гипотеза-o-секторного-масштаба"></a>
<a id="теорема-нейтрино-o-сектор"></a>
<a id="теорема-mr-из-gap"></a>

A type-I seesaw supplies electroweak singlet fermions, a Dirac coupling $m_D$ and an invertible symmetric Majorana mass $M_R$. When the singlets are heavy compared with the mixing, the leading light mass matrix is the Schur complement

$$
M_\mathrm{light}=-m_D M_R^{-1}m_D^T .
$$

A one-family model illustrates the freedom. Rescaling $m_D\mapsto c m_D$, $M_R\mapsto c^2 M_R$ for real $c>0$ preserves the leading light mass while changing the heavy scale. A clock frequency or the dimension of an octonion representation alone fixes neither mass matrix. A proposed loop origin for $M_R$ would require explicit lepton-number-violating interactions.

## Observable spectral differences {#теорема-отношение-нейтринных-масс}

The light masses are the nonnegative singular values in the Takagi factorization. Oscillation phases involve differences $\Delta m^2_{ij}$ and propagation distance divided by energy. A common shift of all $m_i^2$ leaves these differences fixed. Absolute masses, mass ordering and the heavy scale consequently require distinct inputs or measurements.

## Mixing {#теорема-pmns-анархия}

The leptonic mixing matrix compares the charged-lepton and light-neutrino diagonalizing bases. A qualitative assumption of anarchy in $M_R$ gives no numerical angle until a distribution over matrices and the other inputs have been specified. A candidate model can be tested on an oscillation spectrum withheld when fixing its parameters. [Measurement options](../../reference/frontier-ledger).

## Non-PQ `Chain A2` seesaw, $3\times 3$ density-matrix leptogenesis, and Weyl no-go {#nonpq-chain-a2-seesaw}

Inside UHM's clock-stabilizer Pati–Salam chain ($\mathrm{Spin}(10) \to G_{422} \to G_{\mathrm{SM}}/\mathbb{Z}_6$), proton-decay bounds cap $M_{\mathrm{PS}} \le 3.06\times 10^{11}\,\mathrm{GeV}$ ([Proton Decay](./proton-decay#chain-a2-proton-decay)), separating viable from falsified neutrino and baryogenesis mechanisms (`verify_deep_frontier_v4.py`–`verify_deep_frontier_v9.py`, `ToEFrontierDynamics.lean`, `ToEFrontierV6.lean`–`ToEFrontierV9.lean`):

1. **Falsified minimal mechanisms [✗]:** Naive Pati–Salam Type-I seesaw ($Y_\nu = Y_u$ at $M_{\mathrm{PS}} \approx 9.19\times 10^{10}\,\mathrm{GeV}$) predicts $m_{\nu 3} = 102.1\,\mathrm{eV}$ — a $2042\times$ overshoot (`patiSalam_naive_seesaw_exceeds_obs_cq`). Restricting to a Peccei–Quinn-symmetric $\mathbf{10}_H \oplus \overline{\mathbf{126}}_H$ sector also fails below the Super-K cap (requiring $M_{N_3} \sim 5.4\times 10^{12}\text{–}1.1\times 10^{13}\,\mathrm{GeV}$).
2. **Non-PQ `Chain A2` exact seesaw rescue (`nonPQ_chainA2_decoupling_cq`) [T] / [C]:** Dropping external PQ symmetry (which is absent from UHM's Clifford content, `T-333`) equips `Chain A2` ($\mathbf{10}_H \oplus \mathbf{10}_H^* \oplus \overline{\mathbf{126}}_H$, complex bidoublet $(1,2,2)_{\mathbb{C}}$) with the exact algebraic decoupling $M_{\nu_D} = M_u - r_u(M_d - M_e)$ and $M_R \propto B = \frac{1}{4}(M_d - M_e)$. With all 9 charged fermion masses and CKM satisfied identically, this achieves $\chi^2_\nu = 0.000000$ across all 4 oscillation/PMNS observables ($\sin^2\theta_{12}=0.3070$, $\sin^2\theta_{23}=0.5460$, $\sin^2\theta_{13}=0.02200$, $r_{\Delta m}=0.02956$, $J_{\mathrm{PMNS}} = 0.0329$), satisfies the DESI cosmology bound $\sum m_\nu = 0.0650 < 0.072\,\mathrm{eV}$ (normal ordering: $[4.83, 9.87, 50.30]\,\mathrm{meV}$), and stays strictly below the Super-K ceiling ($M_N \le 3.06\times 10^{11}\,\mathrm{GeV}$) at perturbative coupling $r_u$.
3. **Full 13-ODE $3\times 3$ density-matrix leptogenesis with dynamic $y_c(z)$ and 3-channel thermal-threshold EW gauge $\Delta L = 1$ (`spectator_3x3_u2_covariant_collapse_cq`, `dynamic_yc_onsager_schur_complement_cq`, F-34) [T] / [C]:** At $T = M_{N_1} = 1.801\times 10^{10}\,\mathrm{GeV}$, the 12-equation SM chemical network with dynamical charm equilibration $\Delta_c(z) = \mu_{cR} - \mu_{uR}$ satisfies the exact Onsager-symmetric rank-1 Schur-complement identity ($v_c = -6w_c$, Lyapunov relaxation eigenvalue $\lambda_c = 237/230 > 0$, $C_{230} - v_c w_c^T/\lambda_c \equiv C_{316}$). Integrating the coupled 13-ODE system at the unmodified strictly perturbative benchmark `X_RES` ($M_N = [1.801\times 10^{10}, 1.827\times 10^{10}, 3.005\times 10^{11}]\,\mathrm{GeV}$, $1.41\%$ splitting, $(M_2 - M_1)/\Gamma_2 = 9.69 \gg 1$, $r_u = +9.59 + 6.36i$) proves dynamical charm equilibration (`Dc_fin/Dc_eq = 1.0000`), collapsing the earlier static-$y_c$ bracket from $-19.1\%$ to **$-0.34\%$** (`+5.925e-10 → +5.905e-10`). Replacing the gauge proxy by exact 4D Dirac-trace thermal-threshold EW gauge $\Delta L = 1$ scatterings verified across **all three crossing-related channels** ($N\ell\leftrightarrow\phi A$, $N\bar{\phi}\leftrightarrow\bar{\ell} A$, $NA\leftrightarrow\bar{\ell}\phi$; Ward identity $< 10^{-15}$, closed forms $< 10^{-13}$, asymptotic thermal masses $m_{W,B,H,\ell}/T$ and kinematic thresholds $u_{\min} = (1+m_{\mathrm{in}}/M_1)^2$) yields an honest zero-retuning **$\eta_B = +5.591\times 10^{-10}$** (**$-8.65\%$** vs. Planck 2018 $+6.12\times 10^{-10}$). Quantifying the NLO thermal uncertainty band at unmodified `X_RES` (`verify_deep_frontier_v9.py` V9.3.B) gives: soft/hard $t$/$u$-channel IR cutoff $\kappa_{\mathrm{IR}}\in[0.5,2.0] \Rightarrow [5.483, 5.711]\times 10^{-10}$ (`-10.41% .. -6.69%`), NLO top-Yukawa/EW-gauge interference $\pm 15\% \Rightarrow [5.530, 5.654]\times 10^{-10}$ (`-9.64% .. -7.61%`), collinear $1\leftrightarrow 2$ LPM splitting ($c_{\mathrm{LPM}} = +0.25$) $\Rightarrow 5.515\times 10^{-10}$ (`-9.88%`), and the physical GNRS $1\leftrightarrow 2$ thermal phase-space threshold $f_{12}$ $\Rightarrow$ **`6.027e-10` (`-1.52%`)** alone or **`5.821e-10` (`-4.89%`)** with LPM — yielding a full physical NLO envelope **`[5.354, 6.424] × 10⁻¹⁰` (`-12.52% .. +4.97%`)** that cleanly brackets Planck $+6.12\times 10^{-10}$ without retuning `X_RES`. First-principles finite-$T$ NLO/LPM resummation remains open [P].
4. **Weyl $U(1)_{L_e - L_\mu}$ no-go and $\mathrm{PSL}(2,7)$ branching (`weyl_2d_le_lmu_nogo_ratio_cq`) [T] / [✗] / [P]:** In any 2D $(e,\mu)$ block of $B = \frac{1}{4}(M_d - M_e)$, Weyl's singular-value inequality forces $M_2/M_1 \ge (m_\mu - m_s)/(m_s + m_e) = 2.8318 \gg 1.01414$, proving that the $1.41\%$ $N_1/N_2$ quasi-degeneracy requires 3rd-generation $m_\tau$ leakage. Inside $\mathrm{PSL}(2,7)$, modular stabilizers $D_4, S_3, \mathbb{Z}_4, \mathbb{Z}_3$ admit 2-dimensional Majorana invariants with exact $M_1 = M_2 \neq M_3$, while dynamically tying them to $B = \frac{1}{4}(M_d - M_e)$ remains open [P].
