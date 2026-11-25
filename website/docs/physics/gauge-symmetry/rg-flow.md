---
sidebar_position: 6
slug: /physics/gauge-symmetry/rg-flow
title: "Scale dependence of a model"
description: "A sign check for a proposed flow and the data needed for physical matching"
---

# Scale dependence of a model

## Defining a flow {#постановка}

A Wilsonian model specifies its fields, kinetic terms, interactions and regulator. Eliminating a momentum shell generates an effective action. Extracting a few running couplings from it requires a declared projection onto operators. The 21 unordered edges and seven lines of a Fano plane count possible indices. A loop coefficient also depends on the propagator, vertex normalization, dimension and contractions of those indices.

## An exact sign check {#rg-подавление}

Consider a scalar truncation whose equation on a scale interval is $d\lambda/d\log\mu=-\Delta\lambda$ with fixed $\Delta>0$. The solution for a nonzero initial coupling is

$$
\frac{\lambda(\mu)}{\lambda(\mu_0)}
=\left(\frac{\mu}{\mu_0}\right)^{-\Delta}.
$$

Taking $\Delta=5/42$ and $\mu/\mu_0=10^{-61}$ gives a factor $10^{305/42}$, about $10^{7.26}$. The magnitude grows towards the infrared under the stated equation. Whether a scalar truncation describes a measured coupling requires matching its running and boundary value to independent observables.

## Comparing two scales {#стандартная-модель}

For a positive constant rescaling $\alpha=c\lambda$, the beta functions obey $\beta_\alpha=c\beta_\lambda$. A positive quadratic beta function in four dimensions cannot reproduce the negative one-loop beta function of asymptotically free QCD by this rescaling. A test must specify gauge and matter dynamics and compare the coupling at a scale withheld from calibration. A different scale comparison is already defined for transport times on networks. Its observables are the measured times of multiple probes. [Network scale tests](../../geometry/network-scales).

## Two-loop non-SUSY $\mathrm{Spin}(10) \to G_{422} \to G_{\mathrm{SM}}/\mathbb{Z}_6$ unification {#spin10-two-loop-rg}

Within the clock-stabilizer symmetry-breaking chain $\mathrm{Spin}(10) \xrightarrow{L_{e_O}} G_{422} = SU(4)_C \times SU(2)_L \times SU(2)_R \xrightarrow{R_{e_O},\,\nu^c} G_{\mathrm{SM}}/\mathbb{Z}_6$ (`T-329`), two-loop Machacek–Vaughn gauge renormalization-group running from PDG 2024 electroweak inputs ($\alpha_{\mathrm{em}}^{-1} = 127.951$, $\sin^2\theta_W = 0.23122$, $\alpha_s = 0.1180$ at $M_Z$) achieves exact perturbative gauge unification **without supersymmetry** (`verify_deep_frontier_v3.py`, `verify_deep_frontier_v4.py`, `verify_deep_frontier_v7.py`) [C]:

| Symmetry-breaking chain | $M_{\mathrm{PS}}$ (GeV) | $M_{\mathrm{GUT}}$ (GeV) | $\alpha_{\mathrm{GUT}}^{-1}$ | $\tau(p \to e^+\pi^0)$ (yr) | Status |
|---|---|---|---|---|---|
| One-step non-SUSY SM | — | misses by $\Delta\alpha^{-1}=5.58$ | — | — | Falsified [✗] |
| `Chain B` (minimal left-right $G_{3221}$) | — | low $M_{\mathrm{GUT}}$ | — | $5.20\times 10^{33}$ ($<$ Super-K) | Falsified [✗] |
| `Chain A1` ($G_{422}$, 1 real bidoublet + $\Delta_R$) | $9.19\times 10^{10}$ | $1.20\times 10^{16}$ | $45.65$ | $1.22\times 10^{36}$ | Viable [C] |
| `Chain A2` ($G_{422}$, complex $(1,2,2)_{\mathbb{C}}$ + $\Delta_R$) | $1.43\times 10^{11}$ | $7.95\times 10^{15}$ | $45.13$ | $9.08\times 10^{34}\text{–}2.27\times 10^{35}$ | Viable, Hyper-K window [C] |

Scanning 30 Hall–Weinberg threshold realizations ($\lvert\Delta\alpha_i^{-1}\rvert \le 1.0$) reveals a rigid anti-correlation $r(\log_{10} M_{\mathrm{PS}}, \log_{10}\tau_p) = -0.928$, capping the intermediate Pati–Salam scale strictly at $M_{\mathrm{PS}} \le 3.06\times 10^{11}\,\mathrm{GeV}$ under the Super-Kamiokande bound $\tau_p > 2.4\times 10^{34}\,\mathrm{yr}$ [C]. Meanwhile, the same two-loop SM running drives the Higgs quartic coupling $\lambda_H(\mu)$ through zero at $\mu_{\mathrm{inst}} = 5.28\times 10^{10}\,\mathrm{GeV}$ — directly adjacent to $M_{\mathrm{PS}}$, where the Pati–Salam scalar threshold $\Delta_R = (10,1,3)$ stabilizes the vacuum ([Higgs Sector](../particle-physics/higgs-sector#higgs-criticality-vissani)).

### Kähler–Dirac Clifford Lift to CCvS Pati–Salam NCG (`F-42`, `V11.3`) {#ccvs-pati-salam-rge}

Theorem **`F-42`** (`f42_spin6_stab_su4_dim`, `f42_ccvs_ko6_and_zeroth_order`, `f42_ccvs_orbit_vs_full_fluctuations`, `ToEFrontierV11.lean`, `verify_deep_frontier_v11.py` V11.3) formalizes the **Stratum-B** `(Cl₀)+KO-6+(P)` lift from the octonionic $\mathrm{Cl}_{0,7}$ spinor $S_\varphi \cong \mathbf{4}_{\mathbb{C}}$ (clock stabilizer $\mathfrak{spin}(6) \cong \mathfrak{su}(4)_C$, $\dim = 15$, $J_O = \Gamma_7$ with $J_O^2 = -I_8$) to the Connes–Chamseddine–van Suijlekom (CCvS) Pati–Salam finite spectral triple $A_F = \mathbb{H}_L \oplus \mathbb{H}_R \oplus M_4(\mathbb{C})$ on $H_F = \mathbb{C}^{32}$ (exact KO-dimension $6$, universal 0th-order condition, genuine 1st-order violation `max = 7.0`) [T]:

- **Unitary orbit vs. genuine coupled unital CCvS inner fluctuations [T]:** On the $32\times 32$ unitary gauge orbit $U D_F U^\dagger$, the antisymmetric $(6,1,1)_{\mathbb{C}}$ diquark/leptoquark vanishes identically (`real dim = 8 + 120 + 60 = 188`), whereas genuine coupled unital self-adjoint CCvS semigroup perturbations $\Phi(\omega)(D_F)$ automatically preserve KO-dim 6 and strictly generate $(6,1,1)_{\mathbb{C}}$ (`real dim = 200`, single coupled witness `M_6(0,1) = -7`, and 4-perturbation pure-$(6,1,1)_{\mathbb{C}}$ linear combination with zero Yukawa block `M_6(0,1) = -28`).
- **Two-loop CCvS Pati–Salam unification (exact 4-color $C_{\mathrm{top}}^{\mathrm{PS}} = [2,2,2]$, PDG $\pm 1\sigma$ $\alpha_s$ sensitivity), leptogenesis & heavy-threshold split (`V11.3.B,C`) [C] / [✗]:**

| CCvS / Pati–Salam scalar benchmark | $M_{\mathrm{PS}}$ (GeV) | $\Lambda_{\mathrm{NCG}}$ (GeV) | $\alpha^{-1}(\Lambda_{\mathrm{NCG}})$ | $M_{\mathrm{PS}}$ vs. $M_{N_1}=1.80\times 10^{10}$ & $(6,1,1)_{\mathbb{C}}$ p-decay |
|---|---|---|---|---|
| `Chain A2` (`(1,2,2)_C + (10,1,3)_C`) | $1.45\times 10^{11}$ | $7.89\times 10^{15}$ | $45.15$ | OK ($> M_{N_1}$, PDG $\pm 1\sigma$ $\alpha^{-1}\in[45.11,45.18]$; v10 baseline $45.13$) [C] |
| `CCvS-trunc` (`+ (6,1,1)_C`) | $5.05\times 10^{10}$ | $2.05\times 10^{16}$ | $45.56$ | Excluded by $(6,1,1)_{\mathbb{C}}$ Super-K bound ($M_6 \ge 8.35\times 10^{10}$) [✗] |
| `CCvS-FULL-R` (`+ (15,2,2)_R + (6,1,1)_C`) | $1.53\times 10^{10}$ | $5.03\times 10^{16}$ | $39.05$ | Drops $1.17\times$ below $M_{N_1}$ & fails Super-K $M_6$ [✗] |
| `CCvS-FULL-C` (`+ (15,2,2)_C + (6,1,1)_C`) | $1.25\times 10^9$ | $2.71\times 10^{17}$ | $28.49$ | Breaks resonant leptogenesis ($14.4\times$ below $M_{N_1}$ across full $\pm 1\sigma$ band) & fails $M_6$ [✗] |
| `Split-R` (`(6,1,1)_C + (15,2,2)_R` at $10^{15}$) | $1.07\times 10^{11}$ | $1.03\times 10^{16}$ | $44.22$ | Restores $M_{\mathrm{PS}} > M_{N_1}$ & cures $(6,1,1)_{\mathbb{C}}$ p-decay [C] |
| `Split-C` (`(6,1,1)_C + (15,2,2)_C` at $10^{15}$) | $9.35\times 10^{10}$ | $1.17\times 10^{16}$ | $43.11$ | Restores $M_{\mathrm{PS}} > M_{N_1}$ & cures $(6,1,1)_{\mathbb{C}}$ p-decay [C] |

Because **`Super-F-40`** closes ALL 4D Dirac spectral actions as UV completions of gravity, the CCvS Pati–Salam spectral triple supplies the **Stratum-B** internal gauge/Yukawa/Higgs architecture while 4D quantum gravity strictly requires a separate **Stratum-C** background-free dynamical geometry ([Quantum Gravity](../gravity/quantum-gravity#microscopic-area-law)).
