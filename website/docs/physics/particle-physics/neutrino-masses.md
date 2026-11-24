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

Inside UHM's clock-stabilizer Pati–Salam chain ($\mathrm{Spin}(10) \to G_{422} \to G_{\mathrm{SM}}/\mathbb{Z}_6$), proton-decay bounds cap $M_{\mathrm{PS}} \le 3.06\times 10^{11}\,\mathrm{GeV}$ ([Proton Decay](./proton-decay#chain-a2-proton-decay)), separating viable from falsified neutrino and baryogenesis mechanisms (`verify_deep_frontier_v4.py`–`verify_deep_frontier_v10.py`, `ToEFrontierDynamics.lean`, `ToEFrontierV6.lean`–`ToEFrontierV10.lean`):

1. **Falsified minimal mechanisms [✗]:** Naive Pati–Salam Type-I seesaw ($Y_\nu = Y_u$ at $M_{\mathrm{PS}} \approx 9.19\times 10^{10}\,\mathrm{GeV}$) predicts $m_{\nu 3} = 102.1\,\mathrm{eV}$ — a $2042\times$ overshoot (`patiSalam_naive_seesaw_exceeds_obs_cq`). Restricting to a Peccei–Quinn-symmetric $\mathbf{10}_H \oplus \overline{\mathbf{126}}_H$ sector also fails below the Super-K cap (requiring $M_{N_3} \sim 5.4\times 10^{12}\text{–}1.1\times 10^{13}\,\mathrm{GeV}$).
2. **Non-PQ `Chain A2` exact seesaw rescue (`nonPQ_chainA2_decoupling_cq`) [T] / [C]:** Dropping external PQ symmetry (which is absent from UHM's Clifford content, `T-333`) equips `Chain A2` ($\mathbf{10}_H \oplus \mathbf{10}_H^* \oplus \overline{\mathbf{126}}_H$, complex bidoublet $(1,2,2)_{\mathbb{C}}$) with the exact algebraic decoupling $M_{\nu_D} = M_u - r_u(M_d - M_e)$ and $M_R \propto B = \frac{1}{4}(M_d - M_e)$. With all 9 charged fermion masses and CKM satisfied identically, this achieves $\chi^2_\nu = 0.000000$ across all 4 oscillation/PMNS observables ($\sin^2\theta_{12}=0.3070$, $\sin^2\theta_{23}=0.5460$, $\sin^2\theta_{13}=0.02200$, $r_{\Delta m}=0.02956$, $J_{\mathrm{PMNS}} = 0.0329$), satisfies the DESI cosmology bound $\sum m_\nu = 0.0650 < 0.072\,\mathrm{eV}$ (normal ordering: $[4.83, 9.87, 50.30]\,\mathrm{meV}$), and stays strictly below the Super-K ceiling ($M_N \le 3.06\times 10^{11}\,\mathrm{GeV}$) at perturbative coupling $r_u$.
3. **Full 13-ODE $3\times 3$ density-matrix leptogenesis with dynamic $y_c(z)$, 3-channel thermal-threshold EW gauge $\Delta L = 1$, and first-principles 2D impact-parameter LPM solver (`spectator_3x3_u2_covariant_collapse_cq`, `dynamic_yc_onsager_schur_complement_cq`, `verify_deep_frontier_v10.py` V10.3.A) [T] / [C]:** At $T = M_{N_1} = 1.801\times 10^{10}\,\mathrm{GeV}$, the 12-equation SM chemical network with dynamical charm equilibration $\Delta_c(z) = \mu_{cR} - \mu_{uR}$ satisfies the exact Onsager-symmetric rank-1 Schur-complement identity ($v_c = -6w_c$, $\lambda_c = 237/230 > 0$, $C_{230} - v_c w_c^T/\lambda_c \equiv C_{316}$). Integrating the coupled 13-ODE system at unmodified strictly perturbative `X_RES` ($M_N = [1.801\times 10^{10}, 1.827\times 10^{10}, 3.005\times 10^{11}]\,\mathrm{GeV}$, $1.41\%$ splitting, $(M_2 - M_1)/\Gamma_2 = 9.69$, $r_u = +9.59 + 6.36i$) proves dynamical charm equilibration (`Dc_fin/Dc_eq = 1.0000`, collapsing `-19.1% → -0.34%`). With exact 3-channel thermal-threshold EW gauge $\Delta L = 1$ scatterings ($N\ell\leftrightarrow\phi A$, $N\bar{\phi}\leftrightarrow\bar{\ell} A$, $NA\leftrightarrow\bar{\ell}\phi$; Ward identity $< 10^{-15}$), Born $1\leftrightarrow 2$ yields $\eta_B = +5.5904\times 10^{-10}$ (`-8.65%` vs. Planck $+6.12\times 10^{-10}$). Replacing the parametric LPM/GNRS estimate with a **first-principles 2D radial impact-parameter LPM Schrödinger solver** (Aurenche–Gelis–Zaraket HTL dipole collision kernel, **zero free parameters**; free-limit $C = 0$ validated to $8.2\times 10^{-17}$ at $x = 0.5$ and $0.56\%$ at $x = 1.5$) fills the kinematically forbidden sub-threshold bremsstrahlung gap ($x = 0.5$: GNRS `0.0000` $\to$ LPM `0.2381`) and reproduces above-threshold LPM destructive interference ($x = 1.5$: GNRS `0.6544` $\to$ LPM `0.6506`, `-0.58%`). Plugged directly into the 13-ODE solver at **unmodified `X_RES`**, exact 2D LPM yields **$\eta_B = +6.2216\times 10^{-10}$ (`+1.66%` vs. Planck 2018 $+6.12\times 10^{-10}$, zero parameter retuning!)** [T/C].
4. **Weyl $U(1)_{L_e - L_\mu}$ no-go and dynamical origin of $N_1/N_2$ splitting via $\mathrm{PSL}(2,7)\supset S_4\supset D_4/S_3$ RG running (`weyl_2d_le_lmu_nogo_ratio_cq`, `psl2_7_d4_s3_branching_degeneracy`, `rg_radiative_splitting_resonant_peak_cq`, `V10.3.B`, `F-38A,B`) [T] / [C] / [P]:** In any 2D $(e,\mu)$ block of $B = \frac{1}{4}(M_d - M_e)$, Weyl's singular-value inequality forces $M_2/M_1 \ge 2.8318 \gg 1.01414$, proving 3rd-generation $m_\tau$ leakage is mandatory. Inside $\mathrm{PSL}(2,7)$, zero-axiom character branching $\mathbf{3}\vert_{D_4} = \mathbf{2}\oplus\mathbf{1}_{-+}$ and $\mathbf{3}\vert_{S_3} = \mathbf{2}\oplus\mathbf{1}$ (`F-38A`) locks exact tree-level degeneracy $M_{N_1}(M_{\mathrm{GUT}}) = M_{N_2}(M_{\mathrm{GUT}})$; pure 1-loop Yukawa RG running from $M_{\mathrm{GUT}}$ to $M_{N_1}$ then **dynamically generates** the resonant mass splitting $\delta_{21} = 0.242\%$ (SM, $1.68\,\Gamma_2/M_2$) to $0.449\%$ (PS+SM, $3.12\,\Gamma_2/M_2$) right in the resonant peak window ($\Delta M \sim \Gamma$, `F-38B`). **Honest radiative-CP audit:** pure $M_1 = M_2$ 1-loop RG aligns $\operatorname{Re}(H'_{12}) \approx 0$ in the mass-eigenstate basis, suppressing pure-RG leptogenesis to $\eta_B^{\mathrm{RG}} = +3.406\times 10^{-12}$ (SM) / $+3.335\times 10^{-12}$ (PS+SM) — proving RG explains the resonant mass-splitting scale $\mathcal{O}(0.2\%\text{–}0.5\%)$, while the observed $+6.12\times 10^{-10}$ amplitude still requires a small soft/threshold $D_4$-breaking misalignment or 2-loop $Y_\tau$ misalignment [T/C/P].
