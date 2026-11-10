---
sidebar_position: 1
title: "Dark Matter Candidates in the Gap Model"
slug: /physics/cosmology-phys/dark-matter
description: "Relic densities in specified axion, heavy-particle and supersymmetric scenarios."
---

# Dark Matter Candidates in the Gap Model

This chapter examines which particle, symmetry and cosmological inputs each relic estimate uses.


## Overview

The heavy $O$ relic is a proposed field [H]. Its putative protecting symmetry fails on the density-matrix state space (T-163, withdrawn [✗], below). Production during inflation presupposes the field, its mass and a cosmological history. The QCD axion requires an additional Peccei–Quinn sector (§3). None of the estimates identifies the dark matter constituent.

---

## 1. Criteria for a Candidate

From observations (Planck 2018): $\Omega_{\mathrm{DM}} h^2 = 0.120 \pm 0.001$. A candidate must satisfy [D]:

1. Electric neutrality and absence of colour charge
2. Stability ($\tau \gg t_{\mathrm{Universe}} \sim 10^{10}$ yr)
3. Correct relic density $\Omega h^2 \approx 0.12$
4. Consistency with direct detection (XENON, LZ: $\sigma < 10^{-47}$ cm$^2$ for $m \sim 10^2$ GeV)

---

## 2. Constraints on the assumed SUSY spectra {#2-exclusion-of-susy-candidates}

:::note Theorem 8.1 [C under the listed masses, decays and production history]
The table tests the supplied SUSY scenarios. Other mass scales, symmetries and production histories give different relics.
:::

| Candidate | Mass | Problem | Status |
|----------|-------|----------|--------|
| Neutralino | $m \sim 10^{13}$ GeV | $\Omega h^2 \sim 10^{32} \gg 0.12$ (overproduction) | Excluded |
| Gravitino | $m_{3/2} \sim 10^{13}$ GeV | $\tau \sim 7 \times 10^{-26}$ s (unstable) | Excluded |
| Wino/Bino | $m \sim 10^{11}$ GeV | Analogous to neutralino | Excluded |

The listed choices fail the criteria in §1.

### 2.1 Complete Candidate Overview

| Candidate | Mass | Stability | $\Omega h^2$ | Status |
|----------|-------|-------------|---------------|--------|
| Neutralino | $\sim 10^{13}$ GeV | Stable (R-parity) | $\sim 10^{32}$ | Excluded |
| Gravitino | $\sim 10^{13}$ GeV | $\tau \sim 10^{-25}$ s | — | Excluded |
| Wino/Bino | $\sim 10^{11}$ GeV | Stable | $\gg 0.12$ | Excluded |
| Gap instantons | $\sim \Lambda_{\mathrm{QCD}}$ | Stable (topology) | — | Excluded (hadronic) |
| $G_2$-extra bosons | $\sim M_P$ | Stable ($G_2$ charge) | $\sim 10^{-6}$ | Excluded (too little) |
| QCD axion | $\sim 3$ neV | Stable ($U(1)_{\mathrm{PQ}}$) | $\sim 10^{-3}$ | **Not realised** in the Clifford content; needs (PQ) (§3, T-333(e)–(h)) |
| Dark ALPs | $\sim 10^{15}$ GeV | Stable | Heavy | Excluded (§4) |
| **$O$-sector relic** | Assumed $\sim10^{13}$ GeV | Protection open (§5.3) | Scenario only (§5.4) | [H] |

**Gap instantons** are topological configurations $\theta_{ij}(x)$ with non-zero winding number — hadronic objects ($m \sim \Lambda_{\mathrm{QCD}}$). Excluded by observations (BBN, CMB, structure formation).

**$G_2$-extra bosons** — 6 bosons with masses $\sim M_P$. Under gravitational production $\Omega \sim H_I/M_P \sim 10^{-6}$. Too little to be the primary DM.

---

## 3. Axion estimates under the Peccei–Quinn hypothesis {#3-qcd-аксион-из-компактификации-s121}

:::info Role of the Axion in the Gap Formalism
T-99's structural derivation of $\bar\theta=0$ was withdrawn. A QCD axion with a colour anomaly and a QCD-dominated potential could relax $\bar\theta$ in an extended model. [Strong CP](/docs/physics/gauge-symmetry/confinement#тета-не-из-потенциала)
:::

:::warning[Correction 2026-09-26 (T-333(e)–(h)): in the Clifford content this axion is not a QCD axion]
[Confinement §3.1b](/docs/physics/gauge-symmetry/confinement#пк-и-нб) (T-333(e)–(h)) shows that with the fields the Clifford frame forces — three generations of the $\mathbf{16}$ and one doublet — no $\mathrm{U}(1)$ with a colour anomaly survives the quark masses. So a Gap phase has no $G\tilde G$ coupling, and the "axial anomaly with QCD" of §3.1 needs a Peccei–Quinn sector that the frame lacks: a second doublet with a singlet, or new coloured fermions. Call this addition the hypothesis (PQ). Three more points. (1) The mass formula of §3.3 needs the potential of $a$ to come from QCD alone, while §3.5 gives every phase a mass from $V_{\mathrm{Gap}}$; the two cannot both hold. (2) "$\theta_{\mathrm{QCD}}=0$ structurally" rests only on the retracted cubic $V_3$ (T-99 was [C at (SV)]; since 2026-09-26 its conclusion is retracted [✗], [Confinement §3.1c](/docs/physics/gauge-symmetry/confinement#тета-не-из-потенциала)). An axion with a $G\tilde G$ coupling and a QCD-dominated potential relaxes $\theta$ whatever else holds, so it cannot be "purely a DM candidate". (3) The relic estimate of §3.4 takes $\theta_i=H_I/(2\pi f_a)$, a pure fluctuation around $\theta=0$. The axion density is then isocurvature with relative amplitude of order one, and the Planck bound allows $\Omega_a/\Omega_c\lesssim3\times10^{-5}$, not $10^{-2}$. Theorem 9.1 is corrected from [T] to [H] ($\epsilon\sim10^{-3}$ and $N_{\mathrm{DW}}=1$ are assumed), and Theorems 9.2 and 9.3 from [T] to [C at (PQ)]. The arithmetic stands: $f_a=2\times10^{15}$ GeV gives $m_a=2.9$ neV.
:::

### 3.1 Definition {#31-определение}

A candidate phase combination can be written in a chosen coordinate frame as

$$
a(x) := f_a \cdot \frac{1}{3} \sum_{i \in \{A,S,D\}} \sum_{j \in \{L,E,U\}} c_{ij}\, \theta_{ij}(x)
$$

An extension must supply the coefficients $c_{ij}$ and a colour-anomalous axial current. The two triples of real coordinate axes in this ansatz are not invariant colour representations (registry 48a).

### 3.2 Decay Constant

:::tip Theorem 9.1 [H] (corrected 2026-09-26 from [T])
The decay constant of the Gap axion:

$$
f_a = \frac{\epsilon \cdot M_P}{N_{\mathrm{DW}}} \approx 2 \times 10^{15}\;\text{GeV}
$$

for $\epsilon \sim 10^{-3}$, $M_P = 2.4 \times 10^{18}$ GeV, $N_{\mathrm{DW}} = 1$ (number of domain walls for the simplest realisation).
:::

Canonical normalisation: from the kinetic term $\mathcal{L}_{\mathrm{kin}} = \frac{1}{2}m_{ij}(\partial_\mu\theta_{ij})^2$, where $m_{ij} \sim \epsilon^2 M_P^2$ in the $3$-to-$\bar{3}$ sector, one finds $f_a = \sqrt{m_{ij}} = \epsilon \cdot M_P$. Including RG evolution: $\epsilon(\mu_{\mathrm{GUT}}) \sim 10^{-3}$, $\epsilon(\mu_{\mathrm{EW}}) \sim 10^{-2}$; axion physics is determined at the GUT scale.

### 3.3 Axion Mass

:::tip Theorem 9.2 [C at (PQ)] (corrected 2026-09-26 from [T])
The mass is determined by QCD instantons:

$$
m_a = \frac{\sqrt{m_u m_d}}{m_u + m_d} \cdot \frac{m_\pi f_\pi}{f_a} \approx 3 \times 10^{-9}\;\text{eV} = 3\;\text{neV}
$$
:::

An ultralight axion within the sensitivity range of the CASPEr and ABRACADABRA experiments.

### 3.4 Relic Density

:::tip Theorem 9.3 [C at (PQ)] (corrected 2026-09-26 from [T])
From the vacuum misalignment mechanism:

$$
\Omega_a h^2 \approx 0.12 \times \left(\frac{f_a}{10^{12}\;\text{GeV}}\right)^{7/6} \times \left(\frac{\theta_i}{\pi}\right)^2 \approx 10^{-3}
$$
:::

For $\theta_i \sim H_I/(2\pi f_a) < 3.7 \times 10^{-3}$ (from the Planck bound $r < 0.036$):

$$
\Omega_a h^2 \approx 0.12 \times 7100 \times 1.39 \times 10^{-6} \approx 1.2 \times 10^{-3}
$$

The quoted $1\%$ abundance cannot be assigned to the stated fluctuation-only initial condition. With a QCD axion added, the isocurvature analysis in T-333(e)–(h) instead caps its fraction near $3\times10^{-5}$ in that scenario.

### 3.5 Full Axion Spectrum from $(S^1)^{21}$

Compactification on the torus $(S^1)^{21}$ generates the full spectrum of axion-like particles (ALPs). Of the 21 compact phases $\theta_{ij}$, the mass spectrum is determined by the sectoral structure of the Gap vacuum:

:::warning Hypothesis [H]
Mass spectrum of the multi-axion system from $(S^1)^{21}$:

| Sector | Number of modes | Mass scale | Mass-generation mechanism |
|--------|-----------|-------------|--------------------------|
| $3$-to-$\bar{3}$: QCD axion | 1 | $m_a \sim 3$ neV | QCD instantons |
| $3$-to-$\bar{3}$: gluonic | 8 | $m \sim \Lambda_{\mathrm{QCD}} \sim 1$ GeV | Confinement |
| $3$-to-$3$: dark ALPs | 3 | $m \sim 10^{9}$–$10^{15}$ GeV | Hessian of $V_{\mathrm{Gap}}$ |
| $\bar{3}$-to-$\bar{3}$: electroweak ALPs | 3 | $m \sim v_{\mathrm{EW}}$–$10^{15}$ GeV | EWSB $+$ $V_{\mathrm{Gap}}$ |
| $O$-sector | 6 | $m \sim M_P$ | Gap $\sim 1$ (hard modes) |
:::

All 21 phases acquire mass from the potentials $V_3$ or $V_2$ — **there are no flat directions**. This is a fundamental distinction from models with tuned potentials: Gap theory does **not** naturally predict ultralight axions (fuzzy DM, $m \sim 10^{-22}$ eV). [H]

---

## 4. Hypothetical axion-like fields {#4-dark-alps-from-the-3-to-3-sector}

The table groups coordinates in a chosen frame. Assigning particles, charges and masses to these coordinates is an additional hypothesis.

| Sector | Phases | Gap | Modes |
|--------|-----|-----|------|
| $3$-to-$\bar{3}$ ($\{A,S,D\} \times \{L,E,U\}$) | 9 | $\to 0$ | 1 QCD axion + 8 gluonic ($m \sim \Lambda_{\mathrm{QCD}}$) |
| $3$-to-$3$ ($\{A,S,D\} \times \{A,S,D\}$, $i<j$) | 3 | $\sim \epsilon_{\mathrm{space}}$ | 3 dark ALPs |
| $\bar{3}$-to-$\bar{3}$ ($\{L,E,U\} \times \{L,E,U\}$) | 3 | $\sim \epsilon_{\mathrm{EW}}$ | 3 electroweak ALPs (massive after EWSB) |
| $O$-sector | 6 | $\sim 1$ | 6 heavy modes ($m \sim M_P$) |

Potential DM candidates are the **3 dark ALPs** from the $3$-to-$3$ sector: pairs $(A,S)$, $(A,D)$, $(S,D)$.

:::warning Hypothesis [H]
The masses of the dark ALPs are determined by the Hessian of $V_{\mathrm{Gap}}$ in the vacuum:

$$
m_{\mathrm{ALP}} \sim \sqrt{\lambda_3}\,\epsilon\,\mu_{\mathrm{phys}} \sim 10^{15}\;\text{GeV}
$$
:::

This is **of GUT order** — too heavy for standard DM mechanisms. With additional suppression of $\lambda_3$ from partial SUSY preservation in the $3$-to-$3$ sector (Gap $\sim \epsilon_{\mathrm{space}} \sim 10^{-3}$): $m_{\mathrm{ALP}} \sim 10^{9}$ GeV — still heavy, but accessible to **gravitational production** (§5).

There are **no flat directions**: all 21 phases acquire mass from $V_3$ or $V_2$. Gap theory does **not** naturally predict ultralight axions (fuzzy DM).

:::info Open Direction: Collective Enhancement [H]
Multi-axion cosmology from $(S^1)^{21}$ is an open question of medium priority. Is **collective enhancement** of the relic density possible when several ALP fields are simultaneously present? This may modify the estimate of $\Omega_a h^2$ for the subdominant axion sector.
:::

---

## 5. $O$-Sector Relic (Wimpzilla)

### 5.1 $O$-Sector Dark Matter

The proposed scenario adds a weakly coupled particle of mass $m_X\sim10^{13}$ GeV. A large matrix opacity carries no units of mass. The verified transport model starts from a specified moving register and link variables. Frame covariance of its motion holds for its chosen group and representation. Identifying a physical dark particle requires an independent spectrum. [Network results](/docs/reference/network-results)

### 5.2 Gravitational Production during Inflation

The Chung–Kolb–Riotto (CKR, 1998) mechanism predicts a particle number density of mass $m$ in de Sitter space with Hubble parameter $H_I$:

$$
n \sim H_I^3 \cdot e^{-2\pi m / H_I} \quad \text{for } m > H_I
$$

For $m_X/H_I\gg1$ the exponential suppresses production in this approximation. Near $m_X=H_I$ a quantitative abundance needs the field equation and the inflation-to-reheating transition.

:::note Theorem 11.1 [H, illustrative abundance model]
The parameterization used below is

$$
\Omega_X h^2 \approx 0.1 \times \left(\frac{m_X}{10^{13}\;\text{GeV}}\right)^{3/2} \times \left(\frac{H_I}{10^{13}\;\text{GeV}}\right) \sim 0.1\text{--}0.4
$$

for $m_X = m_{3/2} \sim 10^{13}$ GeV, $H_I \sim 4 \times 10^{13}$ GeV.
:::

The range uses chosen masses and Hubble rates. Gravitational production also depends on the inflationary transition, subsequent dilution and survival to the present. The group stabilizer and a choice of superpotential do not fix those inputs.

### 5.3 $O$-Parity {#53-o-parity}

Write $P_O=(-1)^{\Delta N_O}$ for a model with an integer excitation count. The definition assigns a sign. Conservation would require a symmetry of all allowed transitions.

#### Theorem 11.2 (T-163) — partial conjugation fails [✗] {#теорема-11-2}

The stabilizer of the chosen octonionic axis is $\mathrm{SU}(3)$ [T]. The proposed extra involution conjugates only the entries touching $O$, leaving the other entries unchanged. Take the pure state $\psi=(1,1,i)/\sqrt3$ on axes $(O,a,b)$, padded by zeros on the remaining axes. On its support, $\rho=\psi\psi^\dagger$ and its proposed image are

$$
\rho=\frac13\begin{pmatrix}1&1&-i\\1&1&-i\\i&i&1\end{pmatrix},
\qquad
\sigma(\rho)=\frac13\begin{pmatrix}1&1&i\\1&1&-i\\-i&i&1\end{pmatrix}.
$$

The displayed principal minor of the image is $-4/27$. Hence the image fails positivity and the map cannot act as a symmetry on density matrices. Global conjugation is a different map. A finite barrier also permits tunnelling in principle. A stable relic would need a state-preserving symmetry and dynamics conserving its charge, or an independently computed lifetime [H].

### 5.4 Details of CKR Production of the $O$-Relic {#54-details-of-ckr-production-of-the-o-relic}

The Chung–Kolb–Riotto (CKR) mechanism describes non-thermal production of heavy particles through rapid expansion of de Sitter space during inflation. For $O$-sector configurations the process proceeds in three stages:

**Theorem 11.1a [C for the specified production history].** If the species survives, its number density scales as $a^{-3}$ after production with conserved comoving number. For production at $a_*$ this gives

$$
\Omega_X h^2 = \frac{h^2m_X n_X(a_*)}{\rho_{c,0}}\left(\frac{a_*}{a_0}\right)^3.
$$

The mass, production rate and dilution enter separately. In natural units $H_I^3$ has units of energy cubed. The former value in $\mathrm{cm}^{-3}$ omitted this conversion. Substitution of $m_X=10^{13}$ GeV and $H_I=4\times10^{13}$ GeV in the illustrative §5.2 formula gives $0.4$. Comparing that output to $0.120\pm0.001$ cannot establish a relic species or select its mass.

### 5.5 Interaction Cross Section of the $O$-Relic

**Theorem 11.3 (previous cross-section estimate withdrawn) [✗].** In natural units $G_N^2m_X^2m_N^2$ is dimensionless. It cannot supply the stated area in $\mathrm{cm}^2$. A scattering calculation needs a field interaction, incident kinematics, momentum-transfer range and a detector response for the proposed mass. The cross section is open.

:::warning Annihilation Cross Section for $O$-Relic Pairs [H]
For pairs of $O$-quanta ($\Delta N_O = 2$, $P_O = +1$) annihilation is possible:

$$
\sigma_{\mathrm{ann}} v \sim \frac{m_X^2}{M_P^4} \sim 10^{-46}\;\text{GeV}^{-2}
$$

Annihilation $O\bar{O} \to$ SM particles with energy $E \sim m_X \sim 10^{13}$ GeV may produce ultra-high-energy cosmic rays (UHECR, $E > 10^{20}$ eV) — a potentially observable signal.
:::

### 5.6 Relic Density Budget

:::note Conditional scenarios
The entries assume particle content and production histories.

| Component | Mass | $\Omega h^2$ | Fraction of DM | Mechanism |
|-----------|-------|-------------|-----------|----------|
| $O$ relic | Assumed $\sim10^{13}$ GeV | §5.2 estimate | Undetermined | Gravitational production |
| QCD axion (only under (PQ), T-333(e)–(h)) | $\sim 3$ neV | $\lesssim 4 \times 10^{-6}$ (isocurvature) | $\lesssim 3\times10^{-5}$ | Vacuum misalignment |
| Dark ALPs | $\sim 10^{9}$–$10^{15}$ GeV | negligible | $\ll 1\%$ | Gravitational (suppressed) |
| $G_2$-extra bosons | $\sim M_P$ | $\sim 10^{-6}$ | $\ll 1\%$ | Gravitational (exponentially suppressed) |

The relative abundances are undetermined.
:::

---

## 6. Conditions for a heavy relic {#6-summary-candidate}

| Parameter | Value | Source |
|----------|----------|----------|
| Mass | Assumed $\sim10^{13}$ GeV | §5.1 |
| Production mechanism | Gravitational (inflation, CKR) | [§5.4 above](#54-details-of-ckr-production-of-the-o-relic) |
| $\Omega_X h^2$ | Scenario estimate at chosen $m_X,H_I$ | §5.4 |
| Stability | Open after the T-163 counterexample | §5.3 |
| Direct detection | Cross section undetermined | §5.5 |
| Indirect signatures | UHECR ($E > 10^{20}$ eV) from annihilation | Testable |

---

## 7. Fano Correlation Length $\xi_F$

The Fano correlation length $\xi_F$ is the scale over which Fano correlations in the Gap vacuum decay. It is connected to the spatial distribution of dark matter through the structure of the Gap vacuum.

### 7.1 Definition

$$
C_{\mathrm{Fano}}(r) := \langle F_{ijk}(0) \cdot F_{ijk}(r) \rangle_{\mathrm{vac}} \sim e^{-r/\xi_F}
$$

where $F_{ijk}(x) = \varepsilon_{ijk}^{\mathrm{Fano}} \cdot \mathrm{Gap}(i,j,x) \cdot \mathrm{Gap}(j,k,x) \cdot \mathrm{Gap}(i,k,x)$ is the local Fano function.

### 7.2 RG Evolution

:::tip Theorem 9.4 [T]
The Fano correlation length satisfies the RG equation:

$$
\frac{d \ln \xi_F}{d \ln \mu} = -1 + \eta_F, \quad \eta_F = \frac{5}{42} \approx 0.119
$$

where $\eta_F$ is the anomalous dimension of the Fano operator. Solution:

$$
\xi_F(\mu) = \ell_{\mathrm{Planck}} \cdot \left(\frac{M_{\mathrm{Planck}}}{\mu}\right)^{37/42}
$$
:::

### 7.3 Quantitative Prediction

At the Hubble scale ($\mu \sim H_0 \sim 10^{-33}$ eV):

$$
\xi_F(H_0) = \ell_{\mathrm{Planck}} \cdot \left(\frac{10^{28}\;\text{eV}}{10^{-33}\;\text{eV}}\right)^{37/42} = 10^{-35}\;\text{m} \cdot 10^{53.7} \approx 5 \times 10^{18}\;\text{m} \sim 160\;\text{pc}
$$

:::info Note: Physical Meaning [I]
$\xi_F \sim 160$ pc is a scale comparable to the size of small molecular clouds. This defines the region within which Gap configurations are correlated through the Fano structure. Number of uncorrelated Fano modes in the observable Universe:

$$
N_F = \left(\frac{R_H}{\xi_F}\right)^3 = \left(\frac{4.4 \times 10^{26}\;\text{m}}{5 \times 10^{18}\;\text{m}}\right)^3 \approx 6.8 \times 10^{23}
$$
:::

:::warning Caveat: Two Scales [I]
$\ell_{\mathrm{Planck}}$ is the UV cutoff (lattice spacing), $\xi_F$ is the IR correlation. These are **different** physical scales. The number of degrees of freedom $N_{\mathrm{DOF}} = V/\ell_P^3$ should not be confused with the number of Fano modes $N_F = (R_H/\xi_F)^3 \sim 10^{24}$.
:::

---

## 8. Conditional estimates and observables {#8-falsifiable-predictions}

The entries use the candidate fields, masses, cosmological history and coupling scales specified in §§2–7. For example, the value of the axion mass requires (PQ), and a heavy relic requires an independent stability mechanism.

| # | Prediction | Value | Experiment |
|---|-------------|----------|-------------|
| P1 | $m_a \sim 3$ neV (only under (PQ), T-333(e)–(h)) | $2.85 \times 10^{-9}$ eV | CASPEr, ABRACADABRA |
| P2 | $f_a \sim 2 \times 10^{15}$ GeV | From $\epsilon \cdot M_P$ | Axion-photon conversion |
| P3 | $\Omega_a / \Omega_{\mathrm{DM}} \sim 10^{-2}$ — excluded by isocurvature (T-333(e)–(h)) | $\lesssim 3\times10^{-5}$ under (PQ) | Cosmological constraints |
| P4 | $m_{\mathrm{DM}} \sim 10^{13}$ GeV | Wimpzilla | UHECR anomalies |
| P5 | Direct search for a heavy relic | No derived cross section at $m_X\sim10^{13}$ GeV | XENON, LZ |
| P6 | $\xi_F \sim 160$ pc | Fano correlation length | Large-scale structure |

---

## 9. Connection to Other Sections

| Topic | Page | Connection |
|------|----------|-------|
| Cosmological Constant | [Cosmological Constant](/docs/physics/gravity/cosmological-constant) | Vacuum structure, $O$-sector and $\xi_F$ in the $\Lambda$ budget |
| Einstein equations | [Einstein equations](/docs/physics/gravity/einstein-equations) | Conditional matter coupling in a metric theory |
| $G_2$-Structure | [$G_2$-Structure](/docs/physics/gauge-symmetry/g2-structure) | Fano plane and sectoral decomposition |
| Berry phase | [Berry phase](/docs/physics/cosmology-phys/berry-phase) | Homotopy of specified field maps |
| Fano Selection Rule | [Fano Selection Rules](/docs/physics/gauge-symmetry/fano-selection-rules) | Fano correlations and $\xi_F$ |
| Confinement | [Confinement from Gap](/docs/physics/gauge-symmetry/confinement) | Gap $\to 0$ in the $3$-to-$\bar{3}$ sector; QCD axion |


---

**Related documents:**
- [Supersymmetry from G₂](/docs/physics/particle-physics/susy)
- [Cosmological Constant](/docs/physics/gravity/cosmological-constant)
- [Cosmological Genesis](/docs/physics/cosmology-phys/origin)
- [Phase Diagram](/docs/applied/coherence-cybernetics/phase-diagram-cc)
