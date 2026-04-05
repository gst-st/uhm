---
sidebar_position: 1
title: "Dark Matter from Gap"
slug: /physics/cosmology-phys/dark-matter
description: "Systematic overview of dark matter candidates in the Gap formalism: exclusion of SUSY, QCD axion, O-sector Wimpzilla, O-parity, and Fano correlation length ξ_F"
---

# Dark Matter from Gap

:::info Who This Chapter Is For
Dark matter candidates within Gap theory. The reader will learn why the $O$-sector relic is the most viable candidate and how the QCD axion is predicted.
:::


## Overview

Gap theory provides a systematic framework for analysing dark matter candidates. Standard SUSY candidates are **excluded** (too heavy or unstable). The most viable candidate is the **$O$-sector relic** (Wimpzilla, $m \sim 10^{13}$ GeV), gravitationally produced during inflation and stabilised by $O$-parity. A subdominant QCD axion ($m_a \sim 3$ neV, $\sim 1\%$ DM) is additionally predicted.

---

## 1. Criteria for a Candidate

From observations (Planck 2018): $\Omega_{\mathrm{DM}} h^2 = 0.120 \pm 0.001$. A candidate must satisfy [O]:

1. Electric neutrality and absence of colour charge
2. Stability ($\tau \gg t_{\mathrm{Universe}} \sim 10^{10}$ yr)
3. Correct relic density $\Omega h^2 \approx 0.12$
4. Consistency with direct detection (XENON, LZ: $\sigma < 10^{-47}$ cm$^2$ for $m \sim 10^2$ GeV)

---

## 2. Exclusion of SUSY Candidates

:::tip Theorem 8.1 [T]
Standard SUSY dark matter candidates are **excluded** in the Gap formalism:
:::

| Candidate | Mass | Problem | Status |
|----------|-------|----------|--------|
| Neutralino | $m \sim 10^{13}$ GeV | $\Omega h^2 \sim 10^{32} \gg 0.12$ (overproduction) | Excluded |
| Gravitino | $m_{3/2} \sim 10^{13}$ GeV | $\tau \sim 7 \times 10^{-26}$ s (unstable) | Excluded |
| Wino/Bino | $m \sim 10^{11}$ GeV | Analogous to neutralino | Excluded |

**Conclusion:** The SUSY sector of Gap theory contains no viable DM candidate.

### 2.1 Complete Candidate Overview

| Candidate | Mass | Stability | $\Omega h^2$ | Status |
|----------|-------|-------------|---------------|--------|
| Neutralino | $\sim 10^{13}$ GeV | Stable (R-parity) | $\sim 10^{32}$ | Excluded |
| Gravitino | $\sim 10^{13}$ GeV | $\tau \sim 10^{-25}$ s | — | Excluded |
| Wino/Bino | $\sim 10^{11}$ GeV | Stable | $\gg 0.12$ | Excluded |
| Gap instantons | $\sim \Lambda_{\mathrm{QCD}}$ | Stable (topology) | — | Excluded (hadronic) |
| $G_2$-extra bosons | $\sim M_P$ | Stable ($G_2$ charge) | $\sim 10^{-6}$ | Excluded (too little) |
| QCD axion | $\sim 3$ neV | Stable ($U(1)_{\mathrm{PQ}}$) | $\sim 10^{-3}$ | **Subdominant** (§3) |
| Dark ALPs | $\sim 10^{15}$ GeV | Stable | Heavy | Excluded (§4) |
| **$O$-sector relic** | **$\sim 10^{13}$ GeV** | **$\tau \gg t_U$ ($O$-parity)** | **$\sim 0.1$–$0.4$ [C at T-50, CKR]** | **Primary candidate (§5)** |

**Gap instantons** are topological configurations $\theta_{ij}(x)$ with non-zero winding number — hadronic objects ($m \sim \Lambda_{\mathrm{QCD}}$). Excluded by observations (BBN, CMB, structure formation).

**$G_2$-extra bosons** — 6 bosons with masses $\sim M_P$. Under gravitational production $\Omega \sim H_I/M_P \sim 10^{-6}$. Too little to be the primary DM.

---

## 3. QCD Axion from $(S^1)^{21}$ Compactification {#3-qcd-аксион-из-компактификации-s121}

:::info Role of the Axion in the Gap Formalism
In standard physics the Peccei–Quinn axion solves the strong CP problem via dynamical relaxation $\theta_{\mathrm{QCD}} \to 0$. In the Gap formalism $\theta_{\mathrm{QCD}} = 0$ follows **structurally** from the reality of the octonionic $f_{ijk}$ and vacuum uniqueness ([T-99 \[T\]](/docs/physics/gauge-symmetry/confinement#теорема-структурное-theta-qcd)). The Gap axion is therefore a **purely DM candidate**, not a solution to the CP problem.
:::

### 3.1 Definition {#31-определение}

The Gap axion is a pseudoscalar field $a(x)$, the zero mode of the phases $\theta_{ij}$ in the $3$-to-$\bar{3}$ sector, possessing an axial anomaly with QCD:

$$
a(x) := f_a \cdot \frac{1}{3} \sum_{i \in \{A,S,D\}} \sum_{j \in \{L,E,U\}} c_{ij}\, \theta_{ij}(x)
$$

where $c_{ij}$ are coefficients determined from the anomaly condition $\partial_\mu j^\mu_A = \frac{g^2}{32\pi^2} G\tilde{G}$. In the Gap vacuum $\theta_{\mathrm{QCD}} = 0$ **exactly** ([T-99 \[T\]](/docs/physics/gauge-symmetry/confinement#теорема-структурное-theta-qcd)); the axion $a$ describes fluctuations $a \propto \delta\theta$.

### 3.2 Decay Constant

:::tip Theorem 9.1 [T]
The decay constant of the Gap axion:

$$
f_a = \frac{\epsilon \cdot M_P}{N_{\mathrm{DW}}} \approx 2 \times 10^{15}\;\text{GeV}
$$

for $\epsilon \sim 10^{-3}$, $M_P = 2.4 \times 10^{18}$ GeV, $N_{\mathrm{DW}} = 1$ (number of domain walls for the simplest realisation).
:::

Canonical normalisation: from the kinetic term $\mathcal{L}_{\mathrm{kin}} = \frac{1}{2}m_{ij}(\partial_\mu\theta_{ij})^2$, where $m_{ij} \sim \epsilon^2 M_P^2$ in the $3$-to-$\bar{3}$ sector, one finds $f_a = \sqrt{m_{ij}} = \epsilon \cdot M_P$. Including RG evolution: $\epsilon(\mu_{\mathrm{GUT}}) \sim 10^{-3}$, $\epsilon(\mu_{\mathrm{EW}}) \sim 10^{-2}$; axion physics is determined at the GUT scale.

### 3.3 Axion Mass

:::tip Theorem 9.2 [T]
The mass is determined by QCD instantons:

$$
m_a = \frac{\sqrt{m_u m_d}}{m_u + m_d} \cdot \frac{m_\pi f_\pi}{f_a} \approx 3 \times 10^{-9}\;\text{eV} = 3\;\text{neV}
$$
:::

An ultralight axion within the sensitivity range of the CASPEr and ABRACADABRA experiments.

### 3.4 Relic Density

:::tip Theorem 9.3 [T]
From the vacuum misalignment mechanism:

$$
\Omega_a h^2 \approx 0.12 \times \left(\frac{f_a}{10^{12}\;\text{GeV}}\right)^{7/6} \times \left(\frac{\theta_i}{\pi}\right)^2 \approx 10^{-3}
$$
:::

For $\theta_i \sim H_I/(2\pi f_a) < 3.7 \times 10^{-3}$ (from the Planck bound $r < 0.036$):

$$
\Omega_a h^2 \approx 0.12 \times 7100 \times 1.39 \times 10^{-6} \approx 1.2 \times 10^{-3}
$$

**Conclusion [C]:** The QCD axion constitutes $\sim 1\%$ of the observed dark matter — a **subdominant** component (subject to $\epsilon \sim 10^{-3}$ and $N_{\mathrm{DW}} = 1$).

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

## 4. Dark ALPs from the $3$-to-$3$ Sector

Compactification on $(S^1)^{21}$ generates additional axion-like particles (ALPs). Of the 21 phases $\theta_{ij}$:

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

$O$-sector configurations (Gap $\sim 1$ for pairs involving $O$) are heavy particles with masses $\sim 10^{13}$ GeV ($\sim m_{3/2}$). They interact weakly with the SM — through gravity and suppressed $G_2$-extra exchanges.

### 5.2 Gravitational Production during Inflation

The Chung–Kolb–Riotto (CKR, 1998) mechanism predicts a particle number density of mass $m$ in de Sitter space with Hubble parameter $H_I$:

$$
n \sim H_I^3 \cdot e^{-2\pi m / H_I} \quad \text{for } m > H_I
$$

:::info Note: Exponential Mass Selection [I]
For Planck-mass particles ($m \sim M_P \sim 10^{19}$ GeV, $H_I \sim 10^{13}$ GeV) production is **exponentially suppressed**: $e^{-2\pi \times 10^{19}/10^{13}} = e^{-6.3 \times 10^6} \approx 0$. Therefore $G_2$-extra bosons ($m \sim M_P$) are **not produced** during standard inflation. By contrast, for lighter $O$-sector configurations ($m \sim m_{3/2} \sim 10^{13}$ GeV $\approx H_I$) the exponent $\sim e^{-2\pi} \sim 10^{-3}$, giving $n \sim 10^{37}$ cm$^{-3}$ — a physically significant number density.
:::

:::tip Theorem 11.1 [T]
Standard formula for non-thermal relics (Chung, Kolb, Riotto, Phys.Rev.D 59, 023501):

$$
\Omega_X h^2 \approx 0.1 \times \left(\frac{m_X}{10^{13}\;\text{GeV}}\right)^{3/2} \times \left(\frac{H_I}{10^{13}\;\text{GeV}}\right) \sim 0.1\text{--}0.4
$$

for $m_X = m_{3/2} \sim 10^{13}$ GeV, $H_I \sim 4 \times 10^{13}$ GeV.
:::

:::info Promotion of Order-of-Magnitude Estimate [C at T-50, CKR]
The order of magnitude $\Omega_X h^2 \sim 0.1$–$0.4$ is promoted to **[C at T-50, CKR standard cosmology]**:
- $m_X \sim m_{3/2} \sim \varepsilon^3 M_P \sim 10^{13}$ GeV — from T-50 [T] (uniqueness of the superpotential, Schur's lemma)
- CKR formula (Chung–Kolb–Riotto, 1998) — standard result of non-thermal production
- Structural coincidence $m_{3/2} \sim H_I$ (both $\sim \varepsilon^3 M_P$) — not fine-tuning, but a consequence of a unified SUSY-breaking scale

The exact numerical coefficient has an uncertainty of $\times 2$–$3$ (from CKR). Stability requires $O$-parity (see [§5.3](#53-o-parity)).
:::

The order of magnitude **coincides** with the observed $\Omega_{\mathrm{DM}} h^2 = 0.12$.

### 5.3 $O$-Parity {#53-o-parity}

In standard SUSY, $R$-parity $R = (-1)^{3(B-L)+2S}$ stabilises the LSP. In the Gap formalism the analogue of $R$-parity is **$O$-parity**.

#### Theorem 11.2 [T] {#теорема-11-2}

:::tip Theorem 11.2 [T]
$O$-parity is a discrete $\mathbb{Z}_2$ symmetry that stabilises the heavy relic:

$$
P_O := (-1)^{\Delta N_O}
$$

where $\Delta N_O := N_O^{\mathrm{state}} - N_O^{\mathrm{vac}}$ is the number of excited $O$-pairs relative to the vacuum.
:::

*Proof:*

**Step 1 (Stabiliser).** $\mathrm{Stab}_{G_2}(e_O) = SU(3)$ [T] ([T-42e](/docs/proofs/categorical/uniqueness-theorem)). Consequently the $O$-sector possesses a distinguished $SU(3)$-invariant structure.

**Step 2 ($\mathbb{Z}_2$ symmetry from reality).** Complex conjugation $\sigma: \gamma_{Oi} \mapsto \bar{\gamma}_{Oi}$ is a $\mathbb{Z}_2$ symmetry of the potential $V_{\mathrm{Gap}}$, since the structure constants $f_{ijk} \in \mathbb{R}$ ([T-99 \[T\]](/docs/physics/gauge-symmetry/confinement#теорема-структурное-theta-qcd), step 1).

**Step 3 (Commutation with dynamics).** The full Lindblad operator $\mathcal{L}_\Omega$ has real structure constants, hence $\sigma(\mathcal{L}_\Omega[\Gamma]) = \mathcal{L}_\Omega[\sigma(\Gamma)]$, i.e. $[\sigma, \mathcal{L}_\Omega] = 0$.

**Step 4 (Conservation).** $P_O = \pm 1$ is the eigenvalue of $\sigma$ on $O$-sector excitations. From $[\sigma, \mathcal{L}_\Omega] = 0$ it follows that $P_O$ is conserved under evolution. The lightest $O$-odd particle ($P_O = -1$) cannot decay into SM particles ($P_O = +1$) → stable.

**Step 5 (Topological barrier).** [T-69 \[T\]](/docs/core/dynamics/composite-systems#теорема-тополог-защита): $\Delta V \geq 6\mu^2 > 0$ prevents $O$-parity-violating tunnelling. $\blacksquare$

:::info Note: Redefinition via Excitations [I]
The naive definition $P_O = (-1)^{N_O}$, where $N_O$ is the absolute number of $O$-components with Gap $\sim 1$, is **trivial in the vacuum**: all 6 pairs $\{O,A\}, \{O,S\}, \{O,D\}, \{O,L\}, \{O,E\}, \{O,U\}$ have Gap $\sim 1$, so $N_O = 6$ and $P_O = +1$ **for all** states in the vicinity of the vacuum — the symmetry does not distinguish the vacuum from excitations. The correct definition via $\Delta N_O = N_O^{\mathrm{state}} - N_O^{\mathrm{vac}}$ resolves this problem and is the precise analogue of $R$-parity in SUSY.
:::

| Configuration | $\Delta N_O$ | $P_O$ | Consequence |
|-------------|-------------|-------|-----------|
| Vacuum | 0 | $+1$ | |
| Single $O$-quantum | 1 | $-1$ | Stable (cannot decay to SM with $P_O = +1$) |
| Pair of $O$-quanta | 2 | $+1$ | Can annihilate |
| SM particles | 0 | $+1$ | |

**Lifetime:** From the structure of $V_3$: vertices with $O \in \{i,j,k\}$ are suppressed, so transitions changing $\Delta N_O$ are exponentially suppressed:

$$
\tau_X \sim \frac{M_P}{m_X^2} \cdot e^{+M_P/m_X}
$$

For $m_X \sim 10^{13}$ GeV: $e^{M_P/m_X} = e^{10^6} \gg 10^{10^5}$ — **fantastically stable**.

**Status:** $O$-parity is an **exact** $\mathbb{Z}_2$ symmetry of the dynamics $\mathcal{L}_\Omega$ [T], exponentially protected by the topological barrier T-69 [T].

### 5.4 Details of CKR Production of the $O$-Relic {#54-details-of-ckr-production-of-the-o-relic}

The Chung–Kolb–Riotto (CKR) mechanism describes non-thermal production of heavy particles through rapid expansion of de Sitter space during inflation. For $O$-sector configurations the process proceeds in three stages:

:::tip Theorem 11.1a [T]
**(a)** Number density of particles of mass $m$ immediately after inflation:

$$
n_X \sim H_I^3 \cdot e^{-2\pi m_X / H_I}
$$

For $m_X \sim m_{3/2} \sim 10^{13}$ GeV with $m_X \approx H_I$:

$$
n_X \sim (10^{13}\;\text{GeV})^3 \cdot e^{-2\pi} \sim 10^{39} \times 2 \times 10^{-3} \sim 10^{37}\;\text{cm}^{-3}
$$
:::

**(b)** Relic density after dilution by reheating to temperature $T_{\mathrm{RH}}$: [T]

$$
\Omega_X h^2 \sim \frac{m_X \cdot n_X}{T_{\mathrm{RH}}^3} \cdot \frac{T_0^3}{\rho_c} \cdot T_{\mathrm{RH}}^3
$$

Standard CKR formula (Phys.Rev.D 59, 023501):

$$
\Omega_X h^2 \approx 0.1 \times \left(\frac{m_X}{10^{13}\;\text{GeV}}\right)^{3/2} \times \left(\frac{H_I}{10^{13}\;\text{GeV}}\right)
$$

**(c)** Substituting Gap theory parameters ($m_X = m_{3/2} \sim 10^{13}$ GeV, $H_I \sim 4 \times 10^{13}$ GeV): [C at T-50, CKR]

$$
\Omega_X h^2 \sim 0.1 \times 1 \times 4 = 0.4
$$

Accounting for the CKR coefficient uncertainty ($\times 2$--$3$): $\Omega_X h^2 \sim 0.1$--$0.4$, consistent with the observed $\Omega_{\mathrm{DM}} h^2 = 0.120 \pm 0.001$.

:::info Note: Key Role of the Scale $m_X \approx H_I$ [I]
The coincidence $m_{3/2} \sim H_I$ is not parameter fine-tuning. In Gap theory the gravitino mass $m_{3/2}$ is determined by SUSY breaking (Gap $\sim 1$ in the $O$-sector), while the inflation scale $H_I$ is determined by the dynamics of the Gap vacuum. Both are fixed at $\sim 10^{13}$ GeV by independent structural arguments.
:::

:::warning Fitting vs. Prediction
The scale $m_{3/2} \sim \varepsilon^3 M_P \sim 10^{13}$ GeV follows from T-50 [T] (uniqueness of the superpotential) at $\varepsilon \sim 10^{-3}$. The parameter $\varepsilon$ (vacuum coherence) is **not derived** from first principles but is chosen to match the SUSY-breaking scale. The CKR formula gives $\Omega h^2 \sim 0.1$-$0.4$ against the observed $0.120 \pm 0.001$; the agreement is at order of magnitude [C at T-50, CKR], but the uncertainty range ($\times 2$-$3$) covers the observed value. An exact prediction $\Omega h^2 = 0.12$ remains an open problem.
:::

### 5.5 Interaction Cross Section of the $O$-Relic

The $O$-sector relic interacts with Standard Model particles exclusively through gravitational and suppressed $G_2$-extra exchanges.

:::tip Theorem 11.3 [T]
Elastic scattering cross section of the $O$-relic on a nucleon:

$$
\sigma_{X\text{-}N} \sim G_N^2 \, m_X^2 \, m_N^2 \sim \left(\frac{1}{M_P^2}\right)^2 m_X^2 \, m_N^2
$$

Numerically for $m_X \sim 10^{13}$ GeV, $m_N \sim 1$ GeV, $M_P = 2.4 \times 10^{18}$ GeV:

$$
\sigma_{X\text{-}N} \sim \frac{m_X^2 \, m_N^2}{M_P^4} \sim \frac{10^{26} \times 1}{(2.4)^4 \times 10^{72}} \sim 10^{-46}\;\text{GeV}^{-2} \sim 10^{-60}\;\text{cm}^2
$$
:::

This is **13 orders of magnitude** below current experimental limits (XENON1T, LZ: $\sigma < 10^{-47}$ cm$^2$ for $m \sim 100$ GeV) and is practically **unobservable** by direct detectors. [T]

:::warning Annihilation Cross Section for $O$-Relic Pairs [H]
For pairs of $O$-quanta ($\Delta N_O = 2$, $P_O = +1$) annihilation is possible:

$$
\sigma_{\mathrm{ann}} v \sim \frac{m_X^2}{M_P^4} \sim 10^{-46}\;\text{GeV}^{-2}
$$

Annihilation $O\bar{O} \to$ SM particles with energy $E \sim m_X \sim 10^{13}$ GeV may produce ultra-high-energy cosmic rays (UHECR, $E > 10^{20}$ eV) — a potentially observable signal.
:::

### 5.6 Relic Density Budget

:::tip Full Decomposition of $\Omega_{\mathrm{DM}}$ [C at T-50, CKR]
Gap theory predicts two-component dark matter:

| Component | Mass | $\Omega h^2$ | Fraction of DM | Mechanism |
|-----------|-------|-------------|-----------|----------|
| $O$-relic (Wimpzilla) | $\sim 10^{13}$ GeV | $\sim 0.1$–$0.4$ | $\sim 83$–$100\%$ | CKR (gravitational) |
| QCD axion | $\sim 3$ neV | $\sim 1.2 \times 10^{-3}$ | $\sim 1\%$ | Vacuum misalignment |
| Dark ALPs | $\sim 10^{9}$–$10^{15}$ GeV | negligible | $\ll 1\%$ | Gravitational (suppressed) |
| $G_2$-extra bosons | $\sim M_P$ | $\sim 10^{-6}$ | $\ll 1\%$ | Gravitational (exponentially suppressed) |
| **Total** | | **$\sim 0.1$–$0.4$** | **$\sim 100\%$** | |

The observed value $\Omega_{\mathrm{DM}} h^2 = 0.120 \pm 0.001$ is reproduced to order of magnitude.
:::

---

## 6. Summary Candidate

| Parameter | Value | Source |
|----------|----------|----------|
| Mass | $m_X \sim 10^{13}$ GeV | [Standard Model from $G_2$](/docs/physics/gauge-symmetry/standard-model) §5.2 |
| Production mechanism | Gravitational (inflation, CKR) | [§5.4 above](#54-details-of-ckr-production-of-the-o-relic) |
| $\Omega_X h^2$ | $\sim 0.1$--$0.4$ [C at T-50, CKR] | [§5.4 above](#54-details-of-ckr-production-of-the-o-relic) |
| Stability | $\tau \gg t_U$ ($O$-parity) | [§5.3 above](#53-o-parity) |
| Direct detection | $\sigma \sim G_N^2 m_X^2 \sim 10^{-60}$ cm$^2$ | Unobservable |
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

## 8. Falsifiable Predictions

| # | Prediction | Value | Experiment |
|---|-------------|----------|-------------|
| P1 | $m_a \sim 3$ neV | $2.85 \times 10^{-9}$ eV | CASPEr, ABRACADABRA |
| P2 | $f_a \sim 2 \times 10^{15}$ GeV | From $\epsilon \cdot M_P$ | Axion-photon conversion |
| P3 | $\Omega_a / \Omega_{\mathrm{DM}} \sim 10^{-2}$ | $\sim 1\%$ DM | Cosmological constraints |
| P4 | $m_{\mathrm{DM}} \sim 10^{13}$ GeV | Wimpzilla | UHECR anomalies |
| P5 | No WIMP-DM in direct detectors | $\sigma < 10^{-60}$ cm$^2$ | XENON, LZ (confirmed) |
| P6 | $\xi_F \sim 160$ pc | Fano correlation length | Large-scale structure |

---

## 9. Connection to Other Sections

| Topic | Page | Connection |
|------|----------|-------|
| Cosmological Constant | [Cosmological Constant](/docs/physics/gravity/cosmological-constant) | Vacuum structure, $O$-sector and $\xi_F$ in the $\Lambda$ budget |
| Einstein Equations | [Einstein Equations from Gap](/docs/physics/gravity/einstein-equations) | Dark energy as Gap dynamics in the Im-sector |
| $G_2$-Structure | [$G_2$-Structure](/docs/physics/gauge-symmetry/g2-structure) | Fano plane and sectoral decomposition |
| Berry Phase | [Berry Phase](/docs/physics/cosmology-phys/berry-phase) | Topological protection of Gap in the $O$-sector |
| Fano Selection Rule | [Fano Selection Rules](/docs/physics/gauge-symmetry/fano-selection-rules) | Fano correlations and $\xi_F$ |
| Confinement | [Confinement from Gap](/docs/physics/gauge-symmetry/confinement) | Gap $\to 0$ in the $3$-to-$\bar{3}$ sector; QCD axion |


---

**Related documents:**
- [Supersymmetry from G₂](/docs/physics/particle-physics/susy)
- [Cosmological Constant](/docs/physics/gravity/cosmological-constant)
- [Cosmological Genesis](/docs/physics/cosmology-phys/origin)
- [Phase Diagram](/docs/applied/coherence-cybernetics/phase-diagram-cc)
