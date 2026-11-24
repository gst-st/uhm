---
sidebar_position: 1
title: "Dark Matter Candidates in the Gap Model"
slug: /physics/cosmology-phys/dark-matter
description: "Refutation of partial O-conjugation parity (withdrawn T-163), obstructions to coordinate-triple axions (withdrawn T-48a, T-333), conditional correlation length (T-14 vs. T-12), and requirements for a UHM dark-matter candidate."
---

# Dark Matter Candidates in the Gap Model

This chapter documents why the previously proposed UHM dark-matter candidates fail, preserves the exact refutation of $O$-parity (`T-163 [✗]`), corrects the conditional Fano correlation-length estimate (`T-14` vs. `T-12`), and states what any future UHM dark-matter construction must supply.

## Overview

UHM does **not** currently derive a dark-matter particle candidate (`[H]`/`[Pr]`). Specifically:

- Partial $O$-conjugation fails positivity on $\mathcal{D}(\mathbb{C}^7)$ with principal minor $-4/27 < 0$ (`T-163 [✗]`), removing the claimed stability symmetry of an $O$-sector relic.
- Real coordinate-triple partitions into $\{A,S,D\}$ and $\{L,E,U\}$ do not realize the complex $\mathbf{3}$ and $\bar{\mathbf{3}}$ colour subrepresentations (`T-48a [✗]`), refuting the coordinate-triple axion and dark-ALP tables.
- A QCD axion is absent from the minimal chiral fermion content and requires an independent Peccei–Quinn extension (`T-333`).
- The correlation length $\xi_F(H_0)$ is a conditional scaling estimate (`T-14`), not a theorem derived from UHM dynamics, and its sign contradicts the infrared-growing equation of `T-12`.

---

## 1. Observational Criteria `[D]`

From Planck (2018), $\Omega_{\mathrm{DM}} h^2 = 0.120 \pm 0.001$. Any viable dark-matter candidate must supply:

1. Electric and colour neutrality;
2. Stability on cosmological timescales ($\tau \gg t_{\mathrm{Universe}} \sim 10^{10}\;\mathrm{yr}$) via a conserved symmetry or suppressed decay width;
3. A derived production mechanism matching $\Omega h^2 \approx 0.12$;
4. Consistency with direct-detection (e.g. XENON, LZ), indirect-detection, and CMB isocurvature bounds.

---

## 2. Constraints on Imported Heavy SUSY Spectra {#2-exclusion-of-susy-candidates}

If heavy supersymmetric spectra are imported externally (`[C under assumed masses, decays and production history]`), generic ultra-heavy scales fail the criteria of §1:

| Imported candidate | Assumed scale | Obstruction | Status |
|---|---|---|---|
| Neutralino / Wino / Bino | $10^{11}$–$10^{13}\;\mathrm{GeV}$ | Thermal relic overproduction ($\Omega h^2 \gg 0.12$) | Excluded at assumed scale |
| Gravitino | $m_{3/2} \sim 10^{13}\;\mathrm{GeV}$ | Rapid decay ($\tau \ll t_{\mathrm{Universe}}$) | Excluded at assumed scale |
| Hadronic phase windings | $\sim \Lambda_{\mathrm{QCD}}$ | Strongly interacting / hadronic | Excluded |

Because UHM derives neither a supersymmetric particle spectrum nor a supersymmetry-breaking scale ([Supersymmetry](/docs/physics/particle-physics/susy)), these scenarios are external model tests rather than predictions of UHM.

---

## 3. Obstructions to Axion Constructions {#3-qcd-аксион-из-компактификации-s121}

### 3.1 Refutation of the coordinate-triple phase ansatz (`T-48a [✗]`) {#31-определение}

Earlier drafts attempted to construct a QCD axion as a linear combination of internal phases spanning $\{A,S,D\} \times \{L,E,U\}$, interpreting those two real coordinate triples as $\mathbf{3}$ and $\bar{\mathbf{3}}$ of $\mathrm{SU}(3) = \mathrm{Stab}_{G_2}(e_O)$. This construction is refuted by **`T-48a [✗]`**: on the real 6-plane $\mathbb{R}^6 = e_O^\perp \subset \mathrm{Im}\,\mathbb{O}$, the stabilizer $\mathrm{SU}(3)$ acts **irreducibly**. Only after complexification does $\mathbb{C}^6$ decompose into $\mathbf{3} \oplus \bar{\mathbf{3}}$; no subset of three real coordinate axes spans either complex subrepresentation ([Octonions and the Fano plane](/docs/physics/gauge-symmetry/g2-structure)).

### 3.2 Peccei–Quinn requirements and isocurvature constraints (`T-333`)

In a chiral fermion model with massive quarks, the physical strong CP parameter depends on both the gauge $\theta$-angle and the phase of the quark mass determinant; a real internal potential alone leaves that phase unrestricted (`T-333 [T]`, [Confinement and the static potential](/docs/physics/gauge-symmetry/confinement#тета-не-из-потенциала)). With three generations of $\mathbf{16}$ and a single Higgs doublet, no colour-anomalous $\mathrm{U}(1)$ symmetry compatible with quark masses remains. Realizing a QCD axion therefore requires adding an independent Peccei–Quinn sector `(PQ)` and a QCD-dominated potential.

Even if `(PQ)` is introduced externally with a GUT-scale decay constant $f_a \sim 2 \times 10^{15}\;\mathrm{GeV}$ (giving the standard QCD instanton mass $m_a \approx \frac{\sqrt{m_u m_d}}{m_u + m_d}\frac{m_\pi f_\pi}{f_a} \sim 3\;\mathrm{neV}$), high-scale inflationary isocurvature bounds from Planck exclude percent-level misalignment abundances under fluctuation-only initial angles, capping the axion dark-matter fraction at $\lesssim 3 \times 10^{-5}$. Earlier claims of $\Omega_a h^2 \approx 10^{-3}$ at $f_a \sim 2\times 10^{15}\;\mathrm{GeV}$ are incompatible with Planck isocurvature constraints and have been removed.

---

## 4. Why Phase-Torus Coordinates Do Not Yield Dark ALPs {#4-dark-alps-from-the-3-to-3-sector}

The 21 off-diagonal phases $\theta_{ij}$ of a single $7\times 7$ coherence matrix are dimensionless internal parameters, not quantized four-dimensional scalar fields with a derived Lagrangian or mass matrix. Grouping these 21 pairs into "$\mathbf{3}$-to-$\bar{\mathbf{3}}$" (9), "$\mathbf{3}$-to-$\mathbf{3}$" (3), "$\bar{\mathbf{3}}$-to-$\bar{\mathbf{3}}$" (3), and "$O$-sector" (6) relies on the refuted coordinate-triple split **`T-48a [✗]`**. Neither GUT-scale ALP masses nor a multi-axion cosmological spectrum follow from $(S^1)^{21}$.

---

## 5. Refutation of $O$-Parity (`T-163 [✗]`) and Gravitational Production

### 5.1 $O$-Parity {#53-o-parity}

#### Theorem T-163 (Partial $O$-conjugation fails positivity) `[✗]` {#теорема-11-2}

The stabilizer of the marked octonionic axis $e_O$ is $\mathrm{SU}(3)$ `[T]`. To protect a hypothetical heavy $O$-sector relic from decaying, earlier versions postulated an additional $\mathbb{Z}_2$ parity $\sigma$ acting on $\mathcal{D}(\mathbb{C}^7)$ by complex conjugation **only** on matrix entries touching the $O$-axis ($\gamma_{Oi} \mapsto \gamma_{Oi}^*$, $\gamma_{iO} \mapsto \gamma_{iO}^*$, with all non-$O$ entries unchanged).

**Refutation `[T]` (withdrawal of `T-163 [✗]`).** Consider the pure state $\psi = (1, 1, i)/\sqrt{3}$ supported on three axes $(O, a, b)$ (and zero on the remaining four axes). On its $3\times 3$ support, the density matrix $\rho = \psi\psi^\dagger$ and its image $\sigma(\rho)$ under partial $O$-conjugation are

$$
\rho = \frac{1}{3}\begin{pmatrix} 1 & 1 & -i \\ 1 & 1 & -i \\ i & i & 1 \end{pmatrix},
\qquad
\sigma(\rho) = \frac{1}{3}\begin{pmatrix} 1 & 1 & i \\ 1 & 1 & -i \\ -i & i & 1 \end{pmatrix}.
$$

Expanding the determinant of the $3\times 3$ principal block of $\sigma(\rho)$ gives

$$
\det \sigma(\rho) = \frac{1}{27}\Bigl[1(1 - 1) - 1(1 + 1) + i(i + i)\Bigr] = -\frac{4}{27} < 0.
$$

Because a principal minor is strictly negative, $\sigma(\rho)$ has a negative eigenvalue and leaves $\mathcal{D}(\mathbb{C}^7)$. Partial $O$-conjugation is **not** a positive map on the state space and cannot generate a physical stability parity. (Global complex conjugation $\rho \mapsto \rho^*$ preserves positivity, but acts on all pairs rather than singling out the $O$-sector.) $\blacksquare$

### 5.2 Gravitational production requires external field and cosmological inputs {#54-details-of-ckr-production-of-the-o-relic}

For any *externally supplied* stable massive scalar or spinor field of mass $m_X$ produced non-thermally at scale factor $a_*$ with number density $n_X(a_*)$ and conserved comoving number thereafter (`[C for a specified stable species and cosmological history]`), dilution $n_X \propto a^{-3}$ gives

$$
\Omega_X h^2 = \frac{h^2 m_X n_X(a_*)}{\rho_{c,0}}\left(\frac{a_*}{a_0}\right)^3.
$$

In standard Chung–Kolb–Riotto (1998) gravitational production during inflation, the resulting abundance depends sensitively on the supplied particle mass $m_X$, the inflationary Hubble rate $H_I$, the inflaton coupling, and the reheating history. Because UHM derives **none** of $m_X$, $H_I$, a stabilizing symmetry (`T-163 [✗]`), or a scattering/annihilation interaction (note also that in natural units $G_N^2 m_X^2 m_N^2$ is dimensionless and yields no cross section in $\mathrm{cm}^2$), tuning $m_X \sim 10^{13}\;\mathrm{GeV}$ and $H_I \sim 4\times 10^{13}\;\mathrm{GeV}$ to match $\Omega_{\mathrm{DM}} h^2 \approx 0.12$ is free-parameter fitting and has been removed.

---

## 6. Gauge-Lorentz Parity $\mathbb{Z}_2^{\mathrm{DM}}$ and Unified `Chain A2` Dark-Matter Audit {#z2-dm-audit}

While partial $O$-conjugation fails positivity (`T-163`) [✗], breaking $\mathrm{Spin}(10) \to G_{\mathrm{SM}}/\mathbb{Z}_6$ via $\overline{\mathbf{126}}_H$ ($\lvert\Delta(B-L)\rvert = 2$) automatically preserves the exact, anomaly-free **gauge-Lorentz dark-matter parity** $\mathbb{Z}_2^{\mathrm{DM}} = (-1)^{3(B-L)+2s}$ (`minimal_spin10_all_fields_dm_parity_even`, `spin10_210F_singlet_dm_parity_odd`, `verify_deep_frontier_v7.py`, `verify_deep_frontier_v8.py`) [T].

All states of minimal `Chain A2` ($\mathbf{16}_F, \mathbf{10}_H, \mathbf{45}_V, \overline{\mathbf{126}}_H, \mathbf{210}_H$) are strictly $P_{\mathrm{DM}}$-even ($+1$), so dark matter requires an explicit $P_{\mathrm{DM}}$-odd representation ($\mathbf{10}_F, \mathbf{45}_F, \mathbf{54}_F, \mathbf{210}_F, \mathbf{1}_F$, or scalar $\mathbf{16}_H$) [T]. Joint two-loop RGE, Super-K proton-decay, BBN, Planck $\Omega_{\mathrm{DM}} h^2 = 0.120$, LZ 2024, and $SO(10)$ $D$-parity constraints yield an exhaustive classification:

| Candidate ($P_{\mathrm{DM}} = -1$) | Two-loop `Chain A2` impact ($M_{\mathrm{PS}}, M_{\mathrm{GUT}}, \tau_p$) | Relic / direct-detection / symmetry test | Verdict |
|---|---|---|---|
| Minimal `Chain A2` (no extra odd rep) | $1.43\times 10^{11}$, $7.95\times 10^{15}$, $9.08\times 10^{34}\,\mathrm{yr}$ | Zero $P_{\mathrm{DM}}$-odd states (`minimal_spin10_all_fields_dm_parity_even`) | No DM [✗] |
| $\mathbf{10}_F$ doublet / isolated $\mathbf{45}_F$ triplet / $(1,5,0)_F$ / inert $\mathbf{16}_H$ | $\tau_p = 3.59\times 10^{28}$ / $1.28\times 10^{29}$ / $1.50\times 10^{22}$ / $5.27\times 10^{33}\,\mathrm{yr}$ | Violate Super-K ($> 2.4\times 10^{34}\,\mathrm{yr}$); $\mathbf{10}_F$ also fails LZ by $10^8\times$ | Falsified [✗] |
| $\mathbf{16}_H$ complex singlet $(1,1,0)_S$ | Preserves `Chain A2` | High-mass plateau $\sigma_{\mathrm{SI}} = 1.63\times 10^{-45}\,\mathrm{cm}^2$ excluded by LZ; FIMP over-thermalized by $M_{Z'} = 2.94\times 10^{11}\,\mathrm{GeV}$ ($\Gamma_{Z'}/H = 4.40 > 1 \implies m_S \le 84\,\mathrm{eV}$, excluded $60\times$ by Lyman-$\alpha$); only Higgs funnel $62.5\,\mathrm{GeV}$ survives | Funnel only [C] |
| Minimal $\mathbf{210}_F + \mathbf{210}_H$ | Preserves `Chain A2` only if split | **Refuted by $SO(10)$ $D$-parity** (`spin10_210F_singlet_dm_parity_odd`): $(1,1,1)_H \subset \mathbf{210}_H$ is $D$-odd ($-1$), forcing $(1,1,1)_F^2\langle\mathbf{210}_H\rangle \equiv 0$ (zero portal) and leaving $120/210$ states ($119$ colored/EW fermions) unsplit | Falsified [✗] |
| Split $\mathbf{45}_F$: $(1,3,0)$ at $2.8\,\mathrm{TeV}$ + $(8,1,0)$ at $10^9\,\mathrm{GeV}$ | $M_{\mathrm{PS}} \to 6.47\times 10^{14}$, $\tau_p = 4.81\times 10^{34}\,\mathrm{yr}$, $\tau_8 = 0.11\,\mathrm{s}$ | Narrow window $M_8 \in [6\times 10^8, 1.2\times 10^9]\,\mathrm{GeV}$, $\Omega h^2 = 0.120$, $\sigma_{\mathrm{SI}} \approx 2.3\times 10^{-47}\,\mathrm{cm}^2$; shifts $M_{\mathrm{PS}}$ above Higgs $\mu_{\mathrm{inst}}$, shifts $\alpha_{\mathrm{GUT}}^{-1} \to 39.05$, needs cored Galactic Center vs. H.E.S.S. | Narrow / strained [C] |
| **$D$-even $\mathbf{54}_H@M_{\mathrm{GUT}} + \mathbf{54}_F$ (or $\mathbf{210}_F$)** FIMP | **Preserves `Chain A2` 100%** ($\tau_p = 9.08\times 10^{34}\,\mathrm{yr}$, $\alpha_{\mathrm{GUT}}^{-1}=45.13$) | Splits all $4/5$ PS blocks distinctly; tree-level $\mathbf{10}_H^\dagger \mathbf{54}_H \mathbf{10}_H$ dim-5 portal gives cold $\Omega h^2 = 0.120$ at $m_\chi = 4.44\text{–}8.89\,\mathrm{GeV}$, $\sigma_{\mathrm{SI}} = 3.80\text{–}4.56\times 10^{-72}\,\mathrm{cm}^2$ | Viable FIMP [C] |
| **Pure $\mathrm{Spin}(10)$ singlet $\chi_1 = \mathbf{1}_F$** FIMP | **Preserves `Chain A2` 100%** (zero GUT partners) | Planck dim-5 portal gives cold $\Omega h^2 = 0.120$ at $m_{\chi_1} = 4.17\text{–}8.35\,\mathrm{TeV}$, $\sigma_{\mathrm{SI}} = 5.94\times 10^{-75}\,\mathrm{cm}^2$ | Viable FIMP [C] |

Both `Chain A2`-preserving FIMP survivors evade all proton-decay, BBN, Higgs-stability, and H.E.S.S. constraints, at the honest empirical cost that $\sigma_{\mathrm{SI}} \le 4.6\times 10^{-72}\,\mathrm{cm}^2$ lies far below direct-detection reach; dynamically deriving the chosen odd representation from the 7D holon remains open [P].

---

## 6b. General Requirements for Any Future UHM Dark-Matter Candidate [H] {#6-summary-candidate}

Constructing a genuine UHM dark-matter candidate remains an open research program (`[Pr]`) requiring three explicit elements not yet present in the 7D register formalism:

| Requirement | Current status | What must be supplied |
|---|---|---|
| **Network matter sector** | Open `[Pr]` | A derived particle/excitation spectrum with mass scale (extending [Verified Network Results](/docs/reference/network-results)) |
| **Stability mechanism** | Open after `T-163 [✗]` | A state-preserving unitary/CPTP conserved charge or an independently computed decay width $\tau \gg t_{\mathrm{Universe}}$ |
| **Cosmological background & couplings** | Open `[Pr]` | A dynamical spacetime metric, thermal/inflationary production law, and explicit interaction cross sections |

---

## 7. Conditional Model Correlation Length $\xi_F$ (`T-14` and `T-12`)

**Theorem T-14 (`[C under assumed running exponent, UV normalization and IR scale]`).**
Suppose a model correlation length $\xi_F(\mu)$ satisfies the scale equation

$$
\frac{d\ln \xi_F}{d\ln \mu} = -1 + \eta_F
$$

with **constant** assumed exponent $\eta_F$, UV boundary condition $\xi_F(M_P) = \ell_P$, and evaluation at the IR scale $\mu = H_0$. Integrating yields

$$
\xi_F(\mu) = \ell_P \left(\frac{M_P}{\mu}\right)^{1 - \eta_F}.
$$

Two critical checks replace earlier overstated claims:

1. **Sign tension with `T-12`:** In [Scale Dependence of a Model](/docs/physics/gauge-symmetry/rg-flow#rg-подавление) (`T-12`), the stated scalar beta equation $d\lambda/d\ln\mu = -\Delta\lambda$ carries the **negative** signed exponent $-\Delta = -5/42$, so lowering $\mu$ from $M_P$ to $H_0$ by $\sim 61$ decades **increases** the magnitude by $10^{+305/42} \approx 10^{+7.26}$. Substituting $\eta_F = -5/42$ gives $1 - \eta_F = 47/42$ and $\xi_F(H_0) \approx 2.5 \times 10^{33}\;\mathrm{m} \gg R_H$, exceeding the Hubble radius by nearly seven orders of magnitude.
2. **Arithmetic under the assumed positive sign:** Obtaining a sub-Hubble scale requires **assuming** the positive exponent $\eta_F = +5/42$ ($1 - \eta_F = 37/42$), together with $\xi_F(M_P) = \ell_P$ and $\mu = H_0$. With CODATA values ($\ell_P = 1.616 \times 10^{-35}\;\mathrm{m}$, $M_P \approx 1.22 \times 10^{28}\;\mathrm{eV}$, $H_0 \approx 1.44 \times 10^{-33}\;\mathrm{eV}$), this gives $\xi_F(H_0) \approx 7.7 \times 10^{18}\;\mathrm{m} \approx 248\;\mathrm{pc}$ (or $\sim 160$–$180\;\mathrm{pc}$ using rounded inputs $\ell_P = 10^{-35}\;\mathrm{m}$ and $M_P/H_0 = 10^{61}$).

Accordingly, $\xi_F \sim \mathcal{O}(10^2)\;\mathrm{pc}$ is strictly a **conditional model correlation length** (`T-14 [C]`), not a theorem derived from UHM and not a prediction for astrophysical structure or molecular clouds.

---

## 8. Observational Status {#8-falsifiable-predictions}

| Proposed observable | Status | Obstruction / missing input |
|---|---|---|
| QCD axion ($m_a$, $f_a$, $\Omega_a$) | Not derived (`T-48a [✗]`, `T-333`) | Requires independent `(PQ)` sector; GUT-scale misalignment excluded by Planck isocurvature |
| Heavy $O$-sector relic | Refuted parity (`T-163 [✗]`) | Partial $O$-conjugation breaks positivity ($\det = -4/27 < 0$); mass, production, and cross section unproved |
| Dark ALPs from $(S^1)^{21}$ | Not derived (`T-48a [✗]`) | Internal phases lack a derived 4D field action and invariant coordinate split |
| Correlation length $\xi_F$ | Conditional model scale (`T-14 [C]`) | Requires assuming $\eta_F = +5/42$ (opposite to `T-12`), UV normalization $\ell_P$, and IR scale $H_0$ |

---

## 9. Related Documents

- [Confinement and the static potential](/docs/physics/gauge-symmetry/confinement) — Wilson-loop static potential, chiral matter, and strong CP (`T-333`)
- [Scale dependence of a model](/docs/physics/gauge-symmetry/rg-flow) — exact sign check for `T-12`
- [Octonions and the Fano plane](/docs/physics/gauge-symmetry/g2-structure) — irreducibility of $\mathbb{R}^6$ under $\mathrm{SU}(3)$ (`T-48a [✗]`)
- [Cosmological constant](/docs/physics/gravity/cosmological-constant) — volume-response identifiability and open vacuum energy
- [Supersymmetry](/docs/physics/particle-physics/susy) — independence of supersymmetric field content
- [Verified network results](/docs/reference/network-results) — operational transport and foundational bounds
