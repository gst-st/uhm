---
sidebar_position: 3
title: "Cosmological Constant"
slug: /physics/gravity/cosmological-constant
description: "Vacuum energy as a volume-response coefficient, its units, its observability and conditional spectral estimates."
---

# The cosmological constant

The geometric cosmological constant $\Lambda$ is the coefficient of $g_{\mu\nu}$ in the Einstein equation. It has units $\mathrm{m}^{-2}$. A constant vacuum energy density $\epsilon_{\rm vac}$ has units $\mathrm{J\,m^{-3}}$. In general relativity its contribution to that coefficient is

$$
\Lambda_{\rm vac}=\frac{8\pi G_N}{c^4}\,\epsilon_{\rm vac}.
$$

This conversion assumes a metric, the Einstein–Hilbert coupling and a vacuum stress tensor proportional to the metric. An internal register by itself supplies none of those measurements. [Gravitational action](/docs/physics/gravity/einstein-equations)

## Why differences of energy cannot fix this coefficient {#стратегия-замыкания}

Consider two models whose energies at fixed volume differ by a constant. For every pair of states the energy difference is the same in both models. The minimizing states are the same, and the common factor cancels from every normalized Gibbs probability. No sequence of these measurements distinguishes the models, even though they assign different absolute energies to the vacuum. Vanishing cohomology in positive degrees leaves degree-zero constants available. [Identifiability proof](/docs/proofs/gap/lambda-budget#постановка)

## A measurement that can separate two coefficients {#требования-полного-решения}

Suppose a model assigns the action $S_b[h]=S_0[h]+bV[h]$ to an accessible history $h$, where $V$ is a measured additive volume. To test $b$, specify how the instrument reads an action contrast. Independently calibrate the volume, the instrument response and the other action terms. For two histories define $\Delta S_b=S_b[h_2]-S_b[h_1]$ and use the same ordering for $\Delta S_0$ and $\Delta V$. Then

$$
\Delta S_b-\Delta S_0=b\,\Delta V .
$$

If $\Delta V\ne0$ and the instrument resolves this contrast, the ratio determines $b$ in units of action per volume. At equal volume every candidate $b$ yields the same contrast. With a phase-only measurement the phase ambiguity must also be resolved. A third volume contrast provides a held-out test of the fitted coefficient. Identifying $b$ with a gravitational vacuum contribution additionally requires specifying which physical volume is integrated and fixing the action normalization. No such differential volume measurement is supplied by the network results. [Volume-response criterion](/docs/proofs/gap/lambda-budget#структурное-замыкание-лямбда)

## Positive matrix readouts {#теорема-лямбда-положительна}

For a trace-one Hermitian register $\rho$ of dimension seven, $P=\operatorname{Tr}\rho^2$ satisfies

$$
P-\frac17=\|\rho-I/7\|_F^2 .
$$

**T-71.** Choose a readout $\epsilon_{\rm model}=C(P-1/7)$ with a positive $C$ in density units. This readout vanishes at $I/7$ and is positive elsewhere. The positivity statement follows exactly from the identity. The choice of zero, scale, state and coupling of the readout to gravity are physical hypotheses.

### Clock-sector weights {#теорема-лямбда-o-доминирование}

The weighted phase statistic $\mathcal G_O=\sum_{i\ne O}|\gamma_{Oi}|^2\mathrm{Gap}(O,i)^2$ is nonnegative. Other sectors can carry weight independently of these six entries. A physical assertion of $O$-sector dominance therefore needs both a sector profile and an energy functional whose weights are fixed independently of the cosmological observation.

## What spectral calculations determine {#теорема-спектральная-лямбда}

On a supplied four-dimensional Riemannian product geometry, the heat-kernel expansion has a volume term. In natural units its density can involve $\Lambda_{\rm cut}^4\operatorname{Tr}1$, $\Lambda_{\rm cut}^2\operatorname{Tr}D_{\rm int}^2$ and $\operatorname{Tr}D_{\rm int}^4$. Each has energy dimension four. The cutoff moments, the operator and the finite subtraction prescription enter the result. For instance, imposing $\|D_{\rm int}\|\le c_0\varepsilon^3M_P$ on a Hermitian seven-dimensional matrix gives the bound $\operatorname{Tr}D_{\rm int}^4\le7c_0^4\varepsilon^{12}M_P^4$. Bounding this one trace does not set the renormalized volume coefficient. [Spectral action](/docs/physics/gravity/quantum-gravity#canonical-f)

### A finite winding example {#7-сумма-гаусса-для-фано-фаз}

For seven independent, identically oriented blocks and a positive Gaussian cost, the specified theta sum factorizes as $\Theta_M=\Theta_+^7$. At $S_0=20$ the relative reduction in magnitude from the unweighted sum is about $1.34\times10^{-16}$ including zero winding and $1.55\times10^{-9}$ when zero is excluded from both sums. Thus both ratios remain close to one. These are dimensionless properties of the chosen weights. A zero of an analytically continued sum likewise determines a value of that function. Coupling it to physical volume still requires a field model and normalization. [Lattice sum and zeta zeros](/docs/physics/dual-aspect/zeta-regularization)

## Time dependence of a chosen fluid {#теорема-лямбда-дрейф}

**T-254.** If an effective density is specified as $\epsilon_{\rm DE}(a)=C\mathcal G_O(a)^2>0$ with constant $C$, and the fluid is separately conserved, then $d\ln\epsilon_{\rm DE}/d\ln a=-3(1+w)$. Differentiation gives

$$
1+w=-\frac23\,\frac{d\ln\mathcal G_O}{d\ln a}.
$$

A strictly constant density has $w=-1$ under these hypotheses. Interpreting a changing density as an effective fluid requires a map from the register's time coordinate to $a$. It is distinct from a constant geometric $\Lambda$.

### Observable histories {#теорема-трихотомия-ветвей}

**T-255.** A chosen response model can generate particular shapes for $w(a)$. In general a linear response can contain several real or oscillatory modes. A small list of shapes needs its own dynamical restriction and comparison on independent observations.

### Inferring a cosmological state {#теорема-стадия-вселенной}

**T-266.** A history of expansion does not specify a seven-register state or a relaxation rate without an observation map. To infer either, give distinguishable predictions for competing state histories, calibrate on independent records and test the remaining predictions. The sign and magnitude of the physical vacuum contribution remain open.

---

## Unimodular decoupling, sequestering, and falsified internal scales {#unimodular-sequestering-falsifications}

Restricting gravitational variation to fixed four-volume ($\delta V = 0 \iff g^{\mu\nu}\delta g_{\mu\nu} = 0$) yields the traceless Einstein equation $R_{\mu\nu} - \frac{1}{4} R g_{\mu\nu} = 8\pi G_N(T_{\mu\nu} - \frac{1}{4} T g_{\mu\nu})$ [T], from which any radiative vacuum shift $T_{\mu\nu} \to T_{\mu\nu} - \rho_{\mathrm{vac}} g_{\mu\nu}$ drops out identically, turning $\Lambda_{\mathrm{int}}$ into a radiatively stable integration constant; combined with Kaloper–Padilla global sequestering, electroweak and QCD phase-transition jumps are suppressed to $10^{-20}\,\rho_{\Lambda 0}$ and $10^{-16}\,\rho_{\Lambda 0}$ respectively [C].

By contrast, exhaustive analytic, Lean 4, and numerical stress-tests (`verify_deep_frontier_v4.py`–`verify_deep_frontier_v9.py`, `ToEFrontierV6.lean`–`ToEFrontierV9.lean`) **refute every candidate internal UHM mechanism** for generating the numerical scale $\rho_{\Lambda 0} \approx 2.5\times 10^{-47}\,\mathrm{GeV}^4 \sim 10^{-123} M_{\mathrm{Pl}}^4$:

| Candidate internal mechanism | Exact quantitative test / Lean theorem | Verdict |
|---|---|---|
| Sorkin fluctuating everpresent $\Lambda \sim N_4^{-1/2}$ | Ratio $34.2\times$ CMB/BBN conflict at $z \sim 1100$ without fine-tuned temporal correlation | Falsified [✗] |
| Internal `Chain A2` gauge instantons ($\mathrm{Spin}(10)$, $SU(4)_C$, $SU(2)_{L,R}$) | With Bernard 1-loop det $\exp(-1.68 h^\vee + 0.292\sum T_W)$ + strongest $\overline{\mathbf{126}}_H$ $F_{ij}$/$Y_{\nu D}$ closures: best upper bound is $\mathrm{Spin}(10)$ at $M_{\mathrm{GUT}}$ giving $-49.61$ (deficit $-3.01\,\mathrm{dex}$ vs $-46.60$, $-6.96\,\mathrm{dex}$ with scalar det), zero internal axion, and $\pi_3(U(1)_{B-L})=0$ | Falsified [✗] |
| Non-Abelian dark factor inside $\mathrm{Spin}(10)$ | `spin10_sm_centralizer_zero_nonabelian_roots`: $0/40$ roots of $D_5$ commute with $G_{\mathrm{SM}}$ Cartan; $\mathrm{Cent}_{\mathfrak{so}(10)}(\mathfrak{g}_{\mathrm{SM}}) = \mathfrak{u}(1)_Y \oplus \mathfrak{u}(1)_{B-L}$ | Falsified [✗] |
| Single 7D holon 21 phases or Fano $\mathrm{PG}(2,2)$ multi-axion alignment | **Multi-axion WGC convex-hull closure** (`multiaxion_wgc_holon_21_nogo_cq`, F-35D): forces $N_{\mathrm{ax}} \ge 46$ ($m_e$), $\ge 79$ ($\Lambda_{\mathrm{QCD}}$), $\ge 127$ ($v_{\mathrm{EW}}$), $\ge 341$ ($M_{\mathrm{PS}}$), $\ge 591$ ($M_{\mathrm{Pl}}$), $\ge 620$ (`Chain A2` $\mathrm{Spin}(10)$, $S = 283.5$), strictly excluding all $\binom{7}{2}=21 < 46$ holon phases; `fano_incidence_positive_definite_int` ($\det(2I_7+J_7)=24$) | Falsified [✗] |
| 7-gear $q=2$ clockwork alignment | $f_{\mathrm{eff}}/f = \sqrt{5461} = 73.90$, yet violates IR-EFT sublattice WGC by $73.90\times$ ($L_1/L_2 = 0.5819 < 1$) | Falsified [✗] |
| Unbroken confining pure Yang–Mills $SU(N_d)$ at $\Lambda_d = 2.236\,\mathrm{meV}$ | Exact 2-loop PDG running requires $\alpha_d^{-1}(M_{\mathrm{GUT}}) = 76.58$ ($SU(2)$), $114.87$ ($SU(3)$), $153.16$ ($SU(4)$) — incompatible with $\alpha_{\mathrm{GUT}}^{-1} \approx 44\text{–}45$ | Falsified [✗] |

## Unconditional WGC–quintessence boundary theorem and DESI likelihood {#wgc-quintessence-boundary}

For any single-field periodic cosine axion potential $V(\phi) = \Lambda^4(1 - \cos(\phi/f_a)) \le 2\Lambda^4$ matching $\rho_{\Lambda 0} = 3\Omega_\Lambda H_0^2 M_{\mathrm{Pl}}^2$ ($\Omega_\Lambda = 0.685$), the curvature-decay product obeys the unconditional lower bound $m_\phi f_a = \Lambda^2 \ge \sqrt{3\Omega_\Lambda/2}\,H_0 M_{\mathrm{Pl}} = 1.0137\,H_0 M_{\mathrm{Pl}} > H_0 M_{\mathrm{Pl}}$. Combining this with the Weak Gravity Conjecture ($S f_a \le c_{\mathrm{AW}} M_{\mathrm{Pl}}$, $c_{\mathrm{AW}} = \pi\sqrt{6}/2 = 3.8476 < 3.85$) proves the **WGC–Quintessence Product Boundary Theorem** (`wgc_quintessence_product_lower_bound_cq`, `wgc_thawing_quintessence_action_ceiling_cq`) [T]:

$$
S \cdot H_0 \le c_{\mathrm{WGC}}\,m_\phi,
\qquad
m_\phi \le 3 H_0 \;\Longrightarrow\; S < 12
\;\Longrightarrow\; \Lambda_{\mathrm{UV}} \le 38.54\,\mathrm{meV} < m_{\nu 3} = 50.3\,\mathrm{meV}.
$$

At generic initial displacement $\phi_0 = \pi f_a / 2$, the ceiling tightens to $\Lambda_{\mathrm{UV}} \le 16.74\,\mathrm{meV}$; every internal UV scale from $m_e$ ($m_\phi/H_0 \ge 20.28$) up to $M_{\mathrm{Pl}}$ ($m_\phi/H_0 \ge 72.88$) oscillates early as dark matter rather than thawing dark energy [✗]. Furthermore, under the multi-axion convex-hull WGC (`multiaxion_wgc_holon_21_nogo_cq`, F-35D), even $N_{\mathrm{ax}}$ aligned fields can boost $f_{\mathrm{eff}}$ at most by $\sqrt{N_{\mathrm{ax}}}$, tightening the multiplicity floor to $N_{\mathrm{ax}} \ge 46$ ($m_e$), $\ge 591$ ($M_{\mathrm{Pl}}$), and $\ge 620$ (`Chain A2` $\mathrm{Spin}(10)$), decisively closing all 21 holon phases. Consequently, only two structural escapes remain [P]:
1. **External decoupled dark sector (`verify_deep_frontier_v10.py` V10.4.A, `su2d_delta_neff_entropy_dilution_cq` + `toe_v10_f39_nonvacuity_cq`, `F-39A`) [T] / [C] / [✗]:** Exact Machacek–Vaughn 2-loop RG running of an external $SU(2)_d$ dark sector confining at $\Lambda_d = 2.3\,\mathrm{meV}$ gives $\alpha_d^{-1}(M_{\mathrm{GUT}}) = 76.95$ (Pure YM, $b_1 = 136/3$), $75.21$ (Higgsed, $b_1 = 259/6$), and $47.10$ ($N_f = 4\text{ Dirac} + 1H$, closest to `Chain A2` $\alpha_{\mathrm{GUT}}^{-1} = 44.23$). Crucially, an $SU(2)_d$ glueball/condensate vacuum avoids the single-axion WGC bound ($S < 12$), whereas a dark axion at $S = 2\pi\alpha_d^{-1} \approx 280$ **still fails WGC** [✗]. Moreover, computing the exact entropy-diluted dark-radiation signature $\Delta N_{\mathrm{eff}} = \frac{4}{7} g_d (43/(4 g_{*S}))^{4/3}$ for decoupling at SM ($g_{*S} = 106.75$) / PS ($180$) / $\mathrm{Spin}(10)$ ($250$) yields a sharp CMB-S4 test ($\sigma(\Delta N_{\mathrm{eff}}) \approx 0.027$):
   - Pure YM $SU(2)_d$ ($g_d = 6$): $\Delta N_{\mathrm{eff}} = 0.1606$ (SM) / $0.0800$ (PS) / $0.0517$ ($\mathrm{Spin}(10)$) — **detectable by CMB-S4** [C];
   - Higgsed $SU(2)_d$ ($g_d = 10$): $\Delta N_{\mathrm{eff}} = 0.2677$ (SM) / $0.1334$ (PS) / $0.0861$ ($\mathrm{Spin}(10)$) — **detectable by CMB-S4** [C];
   - $SU(2)_d + 4\text{ Dirac} + 1H$ ($g_d = 38$, matching $\alpha_{\mathrm{GUT}}^{-1}$): $\Delta N_{\mathrm{eff}} = 1.0173$ (SM) / $0.5069$ (PS) / $0.3271$ ($\mathrm{Spin}(10)$) — **strictly EXCLUDED by Planck+ACT+DESI ($\Delta N_{\mathrm{eff}} < 0.28$) if thermally populated at $M_{\mathrm{GUT}}$** [T/✗], forcing non-thermal decoupling ($T_d / T_{\mathrm{SM}} < 0.90$). Alternatively, multi-axion alignment requires $N_{\mathrm{ax}} \ge 46$ ($m_e$) / $\ge 591$ ($M_{\mathrm{Pl}}$), lying strictly outside $\mathrm{Spin}(10)$ and the 7D holon.
2. **Sequestered meV-scale dynamics:** active neutrino masses $m_{\nu 1,2} = 4.83,\, 9.87\,\mathrm{meV}$ sit below the $16.74\,\mathrm{meV}$ ceiling ($m_{\nu 2}^4/(16\pi^2) = 2.40\,\rho_{\Lambda 0}$), but standard mass-varying neutrino (MaVaN) realizations suffer adiabatic instability ($c_s^2 < 0$) and require sequestering all scales $\ge m_e$.

Independently of the UV origin of $\Lambda$, a sequestered thawing pseudo-Nambu–Goldstone potential $V(\phi) = \frac{A}{2}(1 + \cos(\phi/f))$ at $f = 0.7\,M_{\mathrm{Pl,red}}$ ($w_0 = -0.81$, strictly $w(z) \ge -1$ with zero phantom crossing) tested against the joint likelihood of DESI DR1 BAO (7 bins / 12 measurements), Planck $100\theta_*$, and exact integral SNe Ia anchors (`verify_deep_frontier_v6.py`) yields [C]:

| Joint cosmological dataset | $\Lambda$CDM $\chi^2$ ($\Omega_m, h$) | Thawing $f = 0.7\,M_{\mathrm{Pl,red}}$ $\chi^2$ ($\Omega_m, h$) | $\Delta\chi^2$ |
|---|---|---|---|
| DESI DR1 BAO + Planck $100\theta_*$ | $12.81$ ($0.293, 0.688$) | $12.92$ ($0.316, 0.659$) | $+0.11$ (tie) |
| DESI + Planck + Pantheon+ SNe | $17.32$ ($0.299, 0.684$) | $18.18$ ($0.313, 0.660$) | $+0.86$ (tie) |
| DESI + Planck + DESY5 SNe | $23.31$ ($0.303, 0.681$) | $14.96$ ($0.314, 0.660$) | $-8.35$ (favored without $w < -1$) |
