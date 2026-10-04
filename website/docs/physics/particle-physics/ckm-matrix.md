---
sidebar_position: 2
title: "CKM Matrix from Fritzsch Texture"
description: "Derivation of the CKM matrix, Cabibbo angle, CP phase, and Jarlskog invariant from Fano geometry"
---

# CKM Matrix from Fritzsch Texture

:::info Rigor levels
- **[T]** Theorem — rigorously proved from the UHM axioms
- **[C]** Conditional — conditional on an explicit assumption
- **[H]** Hypothesis — mathematically formulated, requires proof or non-perturbative computation
- **[✗]** Retracted — contains an error, corrected or replaced

**Important note on levels:**
- **Level 1, retracted [✗] (2026-09-26, T-345(e)):** Fano topology → Fritzsch texture. The six-zero Fritzsch texture is refuted by the data whatever its origin: with the running masses at $M_Z$ it gives $|V_{cb}|\ge0.073$ for every choice of phases, against $0.04183^{+0.00079}_{-0.00069}$ (PDG 2024). The line read "Level 1 [T]: Fano topology → Fritzsch texture (structural prediction)". See [§11](#11-вкус-с-часов).
- **Level 2 [H]:** Texture + observed quark masses → numerical values of CKM elements. Formulas like $|V_{us}| \sim \sqrt{m_d/m_s}$ are standard consequences of Fritzsch texture (Fritzsch, 1977), not original predictions of UHM.
- **Harmonic reading (T-328, 2026-09-25):** this page uses the axis reading of the generations. In the harmonic reading (hypothesis (GC)) an exact family $\mathbb{Z}_3$ would make $|V_{\mathrm{CKM}}|$ a permutation matrix, which $|V_{us}|\approx0.224$ refutes. Mixing then measures the breaking of the family $\mathbb{Z}_3$, and no value of it is derived ([Fermion generations, §5.3(d)](/docs/physics/particle-physics/fermion-generations#поколения-t328)).
- **What the clock can supply (T-345, 2026-09-26):** [§11](#11-вкус-с-часов) lists every parameter-free structure of the clock register and shows which of them can break the family $\mathbb{Z}_3$ and which data exclude them. The numerical claims of §§2–7 below ($\theta_{12}=2\pi/7$ with a tuned $C_{\mathrm{norm}}$, $\delta_{\mathrm{CP}}=64.5°$ from a "two-loop correction", the Fritzsch-texture values) are corrected there and in place.
:::

## Contents

1. [Generations and Mixing](#1-поколения-и-смешивание)
2. [Mixing Angles from Fano Geometry](#2-углы-смешивания-из-фано-геометрии)
3. [Cabibbo Angle: θ_C ≈ 13° from RG correction 2π/7](#3-угол-кабиббо)
4. [CP-Violation Phase](#4-фаза-cp-нарушения) — including [generation mechanism from $V_3$](#delta-cp-mechanism)
5. [Jarlskog Invariant](#5-инвариант-ярлского)
6. [CKM from Mismatch of Yukawa Textures](#6-ckm-из-несовпадения-юкавских-текстур) — including [derivation of $|V_{us}| \sim \sqrt{m_d/m_s}$](#derivation-vus)
7. [Wolfenstein Parameters](#7-вольфенштейновские-параметры)
8. [Honest Assessment of Status](#8-честная-оценка-статуса)
9. [Non-circularity of the CKM derivation](#ckm-non-circularity)
10. [UHM and the Cabibbo Angle Anomaly](#10-cabibbo-angle-anomaly)
11. [Flavour from the clock: what can break the family ℤ₃ (T-345)](#11-вкус-с-часов)

---

## 1. Generations and Mixing {#1-поколения-и-смешивание}

### 1.1 Reminder: Three Generations from Fano

Three generations arise from three inequivalent orientations of the triplet $(A,S,D)$ relative to the Fano plane. The stabilizer of $O$ in $\mathrm{PSL}(2,7)$ is the group $S_4$ (order 24). Three equivalence classes of orientations give three generations with $(k_1, k_2, k_3) = (1, 2, 4)$.

### 1.2 Definition (Fermionic spinors of three generations)

**Definition.** Three generations of quarks are defined by three distinct Gap configurations in the vacuum sector:

**(a)** From Fano duality: each point $X \in \{A, S, D, L, E, U\}$ lies on 3 Fano lines (after removing $O$). The three lines through each point define three orientation classes.

**(b)** Three generations of fermionic spinors:

$$
\chi_n^{(u)} = \alpha_n \eta_0 + \beta_n e_E, \quad \chi_n^{(d)} = \alpha_n \eta_0 + \beta_n e_U
$$

where $\alpha_n, \beta_n$ depend on the generation through the Fano phase $\phi_n = 2\pi k_n / 7$.

### Theorem 1.1 (CKM matrix from spinor inner products) [C] {#thm-1-1}

:::warning [C] Conditional
The derivation of the CKM from Gap spinors is conditional on the identification of fermionic generations with Gap configurations and on the choice of labeling $(k_1,k_2,k_3) = (1,2,4)$.
:::

**Theorem.** The CKM (Cabibbo–Kobayashi–Maskawa) matrix is determined by the overlaps of the fermionic spinors of the three generations:

**(a)** Definition of the CKM in the Gap formalism:

$$
V_{ij}^{(\text{CKM})} = \langle u_i^{(L)} | d_j^{(L)} \rangle_\text{internal} = \langle \chi_i^{(u)} | \Gamma_{EU} | \chi_j^{(d)} \rangle
$$

where $i, j = 1, 2, 3$ are generation indices, $\chi_i^{(u)}$ and $\chi_j^{(d)}$ are the internal spinors of the up- and down-type quarks of the $i$-th and $j$-th generation.

**(b)** Matrix element:

$$
V_{ij} = \alpha_i^* \alpha_j + \beta_i^* \beta_j \cdot \langle e_E | \Gamma_{EU} | e_U \rangle
$$

The last factor: $\langle e_E | e_E \cdot e_U | 1\rangle = \langle e_E | \pm e_L | 1\rangle$ — determined by the Fano structure.

**(c)** Simplification. From the orthogonality of generations and Fano phases:

$$
|V_{ij}| = |\cos(\phi_i - \phi_j) + \sin(\phi_i - \phi_j) \cdot e^{i\delta_\text{Fano}}|
$$

where $\delta_\text{Fano}$ is the phase determined by the associator ($V_3$).

---

## 2. Mixing Angles from Fano Geometry {#2-углы-смешивания-из-фано-геометрии}

### Theorem 2.1 (Mixing angles from Fano geometry) [✗] {#thm-2-1}

*Status corrected 2026-09-26 from [H] to [✗] (T-345(e)).* The angles $2\pi\lvert k_n-k_m\rvert/7$ are refuted by the data, and the running that was to repair them does not exist: see the note after §2.2.

**Theorem.** The three Fano lines through $O$ determine three mixing angles:

**(a)** The Fano plane $\mathrm{PG}(2,2)$ contains 7 lines. Through each of the 7 points pass exactly 3 lines. Through the point $O$ pass 3 lines, each containing a pair from the remaining 6 points:

$$
l_1 = \{O, X_1, Y_1\}, \quad l_2 = \{O, X_2, Y_2\}, \quad l_3 = \{O, X_3, Y_3\}
$$

The three pairs $(X_n, Y_n)$ partition the 6 points into 3 pairs.

**(b)** Angle between the $n$-th and $m$-th generation:

$$
\theta_{nm} = \frac{2\pi}{7} \cdot |k_n - k_m| \bmod 7
$$

From the cyclic $\mathbb{Z}_7$-structure of the Fano plane.

**(c)** Three mixing angles (rough approximation, without RG and $V_3$ corrections):

$$
\theta_{12} = \frac{2\pi}{7} \approx 0.898 \text{ rad} \approx 51.4°
$$

**(d)** Observed Cabibbo angle: $\theta_C \approx 13.0° \approx 0.227$ rad. Ratio: $\theta_{12}^{(\text{Fano})}/\theta_C \approx 4.0$. A correction by a factor of $\sim 1/4$ is required.

### 2.2 Updated CKM Angles with Generation Assignment

With the assignment $k=1 \to$ 3rd, $k=4 \to$ 2nd, $k=2 \to$ 1st generation, the Fano differences for CKM angles:

**(a)** $\theta_{12}$ (Cabibbo angle) — mixing of 1st and 2nd generations ($k=2$ and $k=4$):

$$
\theta_{12}^{(\text{Fano})} \propto |k_{1\text{st}} - k_{2\text{nd}}| = |2 - 4| = 2
$$

**(b)** $\theta_{23}$ — mixing of 2nd and 3rd ($k=4$ and $k=1$):

$$
\theta_{23}^{(\text{Fano})} \propto |k_{2\text{nd}} - k_{3\text{rd}}| = |4 - 1| = 3
$$

**(c)** $\theta_{13}$ — mixing of 1st and 3rd ($k=2$ and $k=1$):

$$
\theta_{13}^{(\text{Fano})} \propto |k_{1\text{st}} - k_{3\text{rd}}| = |2 - 1| = 1
$$

**(d)** Ratios of Fano phases:

$$
\Delta k_{12} : \Delta k_{23} : \Delta k_{13} = 2 : 3 : 1
$$

Observed angle ratios: $\theta_{12} : \theta_{23} : \theta_{13} \approx 13° : 2.4° : 0.2° \approx 65 : 12 : 1$.

**(e)** Fano ratios ($2:3:1$) do not match the observed ones ($65:12:1$). The discrepancy is due to RG suppression depending on the generation mass ratio (Fritzsch texture):

$$
\theta_{12} \sim \sqrt{m_u/m_c}, \quad \theta_{23} \sim \sqrt{m_c/m_t}, \quad \theta_{13} \sim \sqrt{m_u/m_t}
$$

:::warning[Correction 2026-09-26 (T-345(e)): the ratios 2 : 3 : 1 are refuted, and running does not repair them]
With PDG 2024 ($\sin\theta_{12}=0.22501$, $\sin\theta_{23}=0.04183$, $\sin\theta_{13}=0.003732$) the angles are $13.00°$, $2.397°$, $0.2138°$, in the ratio $60.8:11.2:1$ (the "$65:12:1$" above is an older rounding). The Fano differences give $2:3:1$, so $\theta_{23}$ would exceed $\theta_{12}$; the data have $\theta_{12}/\theta_{23}=5.4$. Renormalisation cannot turn one pattern into the other. In one-loop Standard Model running from $M_Z$ to $2\times10^{16}$ GeV $\lvert V_{us}\rvert$ changes by $2\times10^{-5}$, $\sin\delta$ by $2\times10^{-5}$, and $\lvert V_{cb}\rvert$, $\lvert V_{ub}\rvert$ grow by 13 % (`test_ckm_phase_does_not_run_in_the_sm`). The formulas of (e) are the Fritzsch texture, which the data refute separately ([§6.3](#derivation-vus)). Theorem 2.1 is therefore [✗].
:::

---

## 3. Cabibbo Angle {#3-угол-кабиббо}

### Theorem 3.1 (V₃ correction to mixing angles) {#thm-3-1}

:::warning [✗] Retracted 2026-09-26 (T-345(e))
Earlier status [H]: "Qualitative agreement is established. The normalization factor $C_\text{norm} \approx 26$ is tuned from the unitarity condition, not derived from first principles." Retracted on three grounds. (i) The cubic $V_3$ whose running is used here is retracted: every $G_2$-invariant cubic is PT-even ([T-331](/docs/core/dynamics/gap-thermodynamics#g2-инвариантный-кубик)). (ii) With $C_{\mathrm{norm}}$ fitted to $\theta_C$, the agreement with $\theta_C$ is the fit; the suppression factor $0.0097\times26=0.25$ is $\theta_C/(2\pi/7)$ by construction. (iii) Mixing angles do not run appreciably in the Standard Model (note after §2.2), so no RG factor of order $10^{-2}$ can act on an angle.
:::

**Theorem.** The cubic potential $V_3$ contributes a **multiplicative** correction to the bare Fano angles:

**(a)** $V_3$ is an IR-irrelevant operator. Under the RG flow from the Planck to the electroweak scale:

$$
\frac{\lambda_3(\mu_\text{EW})}{\lambda_3(\mu_\text{Planck})} \sim \left(\frac{\mu_\text{EW}}{\mu_\text{Planck}}\right)^{15\lambda_4/(8\pi^2)}
$$

**(b)** Correction to the mixing angle:

$$
\theta_{12}^{(\text{phys})} = \theta_{12}^{(\text{Fano})} \cdot \frac{\lambda_3(\mu_\text{EW})}{\lambda_3(\mu_\text{Planck})}
$$

From the RG beta function: $\beta_{\lambda_3} = -15\lambda_3\lambda_4/(8\pi^2)$:

$$
\frac{\lambda_3(\mu_\text{EW})}{\lambda_3(\mu_\text{Planck})} = \exp\left(-\frac{15\lambda_4^*}{8\pi^2} \ln\frac{\mu_\text{Planck}}{\mu_\text{EW}}\right)
$$

**(c)** Numerically. $\lambda_4^* = 4\pi^2/63 \approx 0.625$. $\ln(\mu_\text{Planck}/\mu_\text{EW}) \approx \ln(10^{17}) \approx 39$:

$$
\frac{\lambda_3(\text{EW})}{\lambda_3(\text{Planck})} = \exp\left(-\frac{15 \times 0.625}{8\pi^2} \times 39\right) = \exp\left(-\frac{9.375}{78.96} \times 39\right) = \exp(-4.63) \approx 0.0097
$$

**(d)** Corrected Cabibbo angle:

$$
\theta_{12}^{(\text{phys})} \approx \frac{2\pi}{7} \times 0.0097 \times C_\text{norm} \approx 0.898 \times 0.0097 \times C_\text{norm}
$$

The normalization factor $C_\text{norm}$ is determined from the unitarity condition of the CKM matrix. At $C_\text{norm} \approx 26$:

$$
\theta_{12}^{(\text{phys})} \approx 0.227 \text{ rad} \approx 13.0°
$$

— **agrees** with the experimental Cabibbo angle.

**(e)** Falsifiable prediction. Ratio of mixing angles:

$$
\frac{\theta_{23}}{\theta_{12}} = \frac{|k_2 - k_3|}{|k_1 - k_2|} \cdot \frac{f(\phi_2, \phi_3)}{f(\phi_1, \phi_2)}
$$

Observed: $\theta_{23}/\theta_{12} \approx 0.040/0.227 \approx 0.18$. This is consistent with $\lambda_3^{1/2} \sim 0.1$.

### Theorem 3.2 (Refined Cabibbo angle with selection principle) {#thm-3-2}

*Retracted [✗] 2026-09-26 (T-345(e)) together with Theorem 3.1:* it uses the same suppression $\exp(-4.63)$ of the retracted cubic, and angles do not run appreciably in the Standard Model. The text is the former derivation.

**Theorem.** Taking into account the selection principle $(k_1,k_2,k_3) = (1,2,4)$ and RG evolution:

**(a)** Bare angle: $\theta_{12}^{(\text{Fano})} = 2\pi|k_1 - k_2|/7 = 2\pi/7$. RG correction: suppression by $\exp(-4.63) \approx 0.0097$.

**(b)** Specifics: $|k_1 - k_2| = 1$, $|k_2 - k_3| = 2$, $|k_1 - k_3| = 3$. Ratios:

$$
\frac{\theta_{23}}{\theta_{12}} = \frac{|k_2-k_3|}{|k_1-k_2|} \cdot f_\text{RG} = 2 \cdot f_\text{RG}
$$

From RG: $f_\text{RG} = (y_2/y_3)^{1/2} \approx (0.975/0.434)^{1/2} \approx 1.5$.

**(c)** Observed: $\theta_{23}/\theta_{12} \approx 0.040/0.227 \approx 0.18$. Prediction: $\theta_{23}/\theta_{12} \sim 2 \times 0.1 / 1.5 \approx 0.13$. Order of magnitude agrees.

---

## 4. CP-Violation Phase {#4-фаза-cp-нарушения}

### Theorem 4.1 (δ_CP from the octonionic associator) [✗] {#thm-4-1}

*Status corrected 2026-09-26 from [H] to [✗] (T-345(e)).* Its source, the PT-odd cubic $V_3$, is retracted: every $G_2$-invariant cubic is PT-even ([T-331](/docs/core/dynamics/gap-thermodynamics#g2-инвариантный-кубик)), and with the corrected potential the Gap sector has no CP violation ([T-333](/docs/physics/gauge-symmetry/confinement#pt-на-фермионах-t341)). The values it gives are refuted in [Theorem 4.2](#thm-4-2). The text of 4.1–4.3 is the former derivation.

**Theorem.** The CP-violation phase in the CKM matrix is determined by the structure of $V_3$:

**(a)** In the standard parametrization: the CKM contains one physical phase $\delta_\text{CP}$. Jarlskog invariant:

$$
J = \text{Im}(V_{us} V_{cb} V_{ub}^* V_{cs}^*) = c_{12} c_{23} c_{13}^2 s_{12} s_{23} s_{13} \sin\delta
$$

**(b)** In the Gap formalism: the phase $\delta_\text{CP}$ arises from the **complexity** of the matrix elements $\langle\chi_i|\Gamma_{EU}|\chi_j\rangle$. This complexity is a direct consequence of $V_3$ (PT-odd):

$$
\delta_\text{CP} = \arg\left(\sum_{(i,j,k) \in 3\text{-to-}\bar{3}} \varepsilon_{ijk}^\text{Fano} \cdot \phi_1 \cdot \phi_2 \cdot \phi_3\right)
$$

**(c)** From Fano structure: $\varepsilon^\text{Fano}_{ijk} = \pm 1$ for 7 triplets. Sum over triplets involving all three generations:

$$
\delta_\text{CP} = \arg\left(\sum_\text{Fano} \pm e^{i(\phi_1 + \phi_2 - \phi_3)}\right)
$$

### 4.1 Mechanism of $\delta_\text{CP}$ Generation from the $V_3$ Phase {#delta-cp-mechanism}

:::warning [H] Hypothesis
Qualitative mechanism: $V_3$ (octonionic associator, PT-odd) is the unique source of CP violation in the Gap formalism. The specific numerical value of the phase is determined by the $\mathbb{Z}_7$-structure, but two-loop corrections require further computation.

Computational task C16: 3-loop RG + threshold corrections. All formulas are defined [T]; computation is feasible in SYNARC.

*Retracted [✗] 2026-09-26 (T-345(e)):* $V_3$ is not PT-odd — every $G_2$-invariant cubic is PT-even (T-331) — so it is no source of CP violation, and the phase does not run appreciably (Theorem 4.2). This box keeps its former text.
:::

CP violation in the CKM matrix arises from the **complexity** of the overlaps $\langle\chi_i|\Gamma_{EU}|\chi_j\rangle$ between fermionic spinors of different generations. This complexity has a single source — the cubic potential $V_3$. Here $V_3$ plays a **dual role**: it also enforces $\theta_{\mathrm{QCD}} = 0$ through the fixing of vacuum phases ([T-99 \[T\]](/docs/physics/gauge-symmetry/confinement#теорема-структурное-theta-qcd)), while generating $\delta_{\mathrm{CP}} \neq 0$ through inter-generation mixing (details: [dual role of $V_3$](/docs/physics/gauge-symmetry/confinement#следствие-двойная-роль-v3)):

$$
V_3 = \lambda_3 \sum_{(i,j,k) \notin \text{Fano}} |\gamma_{ij}||\gamma_{jk}||\gamma_{ik}| \sin(\theta_{ij} + \theta_{jk} - \theta_{ik})
$$

$V_3$ is a PT-odd operator: it changes sign under time reversal ($\theta_{ij} \to -\theta_{ij}$). It is precisely the PT-oddness of $V_3$ that generates complex phases in the Yukawa matrices $Y^u$ and $Y^d$. At $\lambda_3 = 0$ all CKM elements would be real and $\delta_\text{CP} = 0$.

The phase $\delta_\text{CP}$ is determined by the argument of the sum over Fano triplets involving all three generations. Each Fano triplet $(i,j,k)$ contributes a phase factor $\varepsilon_{ijk}^\text{Fano} = \pm 1$, and the total phase:

$$
\delta_\text{CP} = \arg\left(\sum_\text{Fano} \varepsilon_{ijk}^\text{Fano} \cdot e^{i(\phi_1 + \phi_2 - \phi_3)}\right)
$$

depends on the specific Fano phases $\phi_n = 2\pi k_n / 7$ of the generations. The discreteness of the $\mathbb{Z}_7$-group makes $\delta_\text{CP}$ **not a free parameter** but a computable quantity — this is the key distinction from the Standard Model, where $\delta_\text{CP}$ is introduced ad hoc.

### 4.2 Initial Computation ($(k_1,k_2,k_3) = (1,2,4)$, multiplicative group)

**(d)** Numerical prediction. From $\mathbb{Z}_7$-symmetry: $\phi_n = 2\pi k_n / 7$:

$$
\delta_\text{CP} = \arg\left(e^{2\pi i(1+2-4)/7}\right) = \arg\left(e^{-2\pi i/7}\right) = -\frac{2\pi}{7} \approx -51.4°
$$

Magnitude: $|\delta_\text{CP}| \approx 51.4°$.

**(e)** Observed value: $\delta_\text{CP} \approx 65.7° \pm 1.5°$ (PDG 2024). Discrepancy of the raw Fano value ~17%. Sources:
- RG corrections to $\delta$ ($V_3$ runs)
- Two-loop contributions to the phase
- Corrections from the generation mass hierarchy

### 4.3 Updated Computation with Generation Assignment

### Theorem 4.2 (Updated phase δ_CP) {#thm-4-2}

:::warning[Retracted 2026-09-26 (T-345(e)): the 12.6° correction does not exist]
The value $64.5°$ below is $77.1°-12.6°$, and the $12.6°$ is not a property of the Standard Model. In one-loop running of the full Yukawa matrices from $M_Z$ to $2\times10^{16}$ GeV the phase moves by $0.003°$ and $\sin\delta$ by $2\times10^{-5}$ (`test_ckm_phase_does_not_run_in_the_sm`); the rephasing invariants $J$ and $\sin\delta$ run only through products of small Yukawa couplings. The estimate $y_t^2/(16\pi^2)\cdot\ln(\mu_{\mathrm{GUT}}/\mu_{\mathrm{EW}})\cdot2\pi/7$ multiplies a phase by the running of a coupling, which is not how a phase runs, and its sign was chosen to fit. Without it the prediction is $\lvert\delta\rvert=77.1°$ (or $51.4°$ for the first assignment), against $65.7°\pm1.5°$ (PDG 2024, $\delta=1.147\pm0.026$ rad): $7.6\sigma$ (resp. $9.5\sigma$). The phase source $V_3$ is retracted (T-331), and in the Clifford frame the CKM phase is a Yukawa input ([T-333](/docs/physics/gauge-symmetry/confinement#pt-на-фермионах-t341)). The text below is kept as the former derivation; its status is [✗]. A parameter-free phase from the clock's own Gauss sum, $\pi-\arg b_7=\arctan\sqrt7=69.30°$ with $b_7=(-1+i\sqrt7)/2$, was also tried: $2.4\sigma$ from the global fit, and it has no mechanism behind it ([§11](#11-вкус-с-часов)).
:::

**Theorem.** With the new assignment ($k=2 \to$ 1st, $k=4 \to$ 2nd, $k=1 \to$ 3rd):

**(a)** Phase:

$$
\delta_\text{CP} = \arg(e^{2\pi i(k_{1\text{st}} + k_{2\text{nd}} - k_{3\text{rd}})/7}) = \arg(e^{2\pi i(2+4-1)/7}) = \arg(e^{10\pi i/7})
$$

$$
= \frac{10\pi}{7} - 2\pi = -\frac{4\pi}{7} \approx -102.9°
$$

**(b)** Magnitude: $|\delta_\text{CP}| = 180° - 102.9° = 77.1°$ (reduction to the upper half-plane).

Observed (**canonical value, SSOT**): $|\delta_\text{CP}| = 65.7° \pm 1.5°$ (PDG 2024 global fit). The cleanest tree-level determination — the LHCb combination reported at ICHEP 2024 — gives $\gamma \equiv \delta_\text{CP} = 64.6° \pm 2.8°$, sitting essentially on top of the prediction below. The older "$69°\pm4°$" figure is superseded. Raw-value discrepancy $\sim 11°$ (removed by the two-loop correction below).

**(c)** With two-loop correction: $|\delta^{(2)}| \sim 12.6°$. RG correction to $\delta$:

$$
\delta_\text{CP}^{(\text{phys})} = -\frac{2\pi}{7} + \delta^{(2)}, \quad |\delta^{(2)}| \sim \frac{y_t^2}{16\pi^2} \cdot \ln\frac{\mu_\text{GUT}}{\mu_\text{EW}} \cdot \frac{2\pi}{7}
$$

$$
|\delta^{(2)}| \sim \frac{1.0}{16\pi^2} \times 39 \times 0.898 \approx 0.22 \text{ rad} \approx 12.6°
$$

With a negative sign for the two-loop correction:

$$
|\delta_\text{CP}^{(\text{phys})}| \approx 77.1° - 12.6° = 64.5°
$$

Discrepancy from the global-fit $65.7°$: $\sim 1.2°$ ($< 1\sigma$); against the direct LHCb tree combination $64.6° \pm 2.8°$ the predicted $64.5°$ lands within $\sim 0.1°$ ($\approx 0.04\sigma$) — a near-exact coincidence. **Improved agreement** — and far better against the current values than against the older $69°$ figure.

**(d)** With a positive sign: $77.1° + 12.6° = 89.7°$ — discrepancy $\sim 20°$ ($> 4\sigma$). Thus, the new assignment **predicts a negative sign** for the two-loop correction.

#### Sign of the two-loop correction [C under SM 2-loop RG] {#sign-two-loop}

:::info [C under SM 2-loop RG] Sign of the two-loop correction
The sign of the two-loop correction to $\delta_\text{CP}$ is determined from the SM limit of Gap RG. In the Standard Model the two-loop RG equation for the Jarlskog invariant $J$ is known (Antusch, Ratz, 2003):

$$
\frac{dJ}{d\ln\mu} \propto -y_t^2 \cdot J \cdot (\text{positive factor})
$$

The negative sign means that $J$ **decreases** when moving from IR to UV (i.e. increases from top to bottom in energy). Since $J \propto \sin\delta_\text{CP}$, the phase $\delta_\text{CP}$ decreases from UV to IR. Therefore:
- **Sign** of the two-loop correction — **negative** (IR value is larger in magnitude than UV) **[C under SM 2-loop RG]**
- Tree-level value $\delta_\text{CP}^{(\text{tree})} = |2\pi/7| \approx 51.4°$ — UV value
- IR value: $\delta_\text{CP}^{(\text{phys})} \approx 51.4° + |\delta^{(2)}| \approx 64°$ (correction is added due to sign convention)
- **Magnitude** $|\delta^{(2)}| \sim 12.6°$ depends on threshold corrections at the GUT scale — **[H]**

*Retracted [✗] 2026-09-26 (T-345(e)):* the running of $J$ in the SM follows that of the angles ($\lvert V_{cb}\rvert$, $\lvert V_{ub}\rvert$ grow by 13 % from $M_Z$ to $2\times10^{16}$ GeV), while the phase itself moves by $0.003°$ and $\sin\delta$ by $2\times10^{-5}$ (`test_ckm_phase_does_not_run_in_the_sm`); there is no correction of $12.6°$ whose sign could be fixed. This box keeps its former text.
:::

### Former final prediction, retracted [✗]:

$$
|\delta_\text{CP}| \approx 64.5° \quad \text{(former: sign of correction [C under SM 2-loop RG], magnitude [H])}
$$

*Retracted 2026-09-26 (T-345(e)):* the correction it rests on is absent in the Standard Model (box under Theorem 4.2); the uncorrected value $77.1°$ is $7.6\sigma$ from the data.

:::warning Discrepancy with experiment
Observed value $\delta_\text{CP} = 65.7° \pm 1.5°$ (PDG 2024). Predicted value $\approx 64.5°$ deviates from the central experimental value by $\sim 1.2°$ ($< 1\sigma$). Sign of the two-loop correction is fixed by SM RG [C]; precise value depends on GUT threshold corrections [H].

*Retracted 2026-09-26 (T-345(e)):* the predicted value is retracted [✗] (box under Theorem 4.2); the discrepancy of the uncorrected $77.1°$ is $11.4°$, $7.6\sigma$.
:::

---

## 5. Jarlskog Invariant {#5-инвариант-ярлского}

### Theorem 5.1 (Jarlskog invariant from Fano parameters) {#thm-5-1}

:::warning [H] Hypothesis
The numerical agreement $J \approx 3 \times 10^{-5}$ follows from Fritzsch texture with observed masses, and is not an independent prediction.

*Corrected 2026-09-26 (T-345(e)):* (c) and (d) are [✗]. The phase $64.5°$ of (c) is retracted (Theorem 4.2), and in (d) the observed $\delta = 65.7°$ is substituted: $J$ computed from the observed angles and the observed phase reproduces the observed $J$ by construction, so it is not a prediction. With the uncorrected Fano phase, $\sin 77.1° = 0.975$ against $\sin 65.7° = 0.911$.
:::

**Theorem.** The Jarlskog invariant is computed from the CKM parameters:

**(a)** Formula:

$$
J = c_{12} c_{23} c_{13}^2 s_{12} s_{23} s_{13} \sin\delta_\text{CP}
$$

**(b)** Initial estimate ($\delta = 51.4°$):

$$
J \approx 0.97 \times 0.999 \times 0.9999 \times 0.227 \times 0.040 \times 0.004 \times \sin(51.4°)
$$

$$
J \approx 3.5 \times 10^{-5} \times 0.78 \approx 2.7 \times 10^{-5}
$$

Observed: $J \approx 3.0 \times 10^{-5}$. Agreement within 10%.

**(c)** Updated estimate ($\delta = 64.5°$):

With $s_{12} = 0.225$, $s_{23} = 0.042$, $s_{13} = 0.0037$, $\sin(64.5°) = 0.903$:

$$
J = 0.974 \times 0.999 \times 0.9999 \times 0.225 \times 0.042 \times 0.0037 \times 0.903
$$

$$
\approx 3.1 \times 10^{-5}
$$

Observed: $J = (3.08 \pm 0.15) \times 10^{-5}$. **Agreement within 1%.**

**(d)** Clarification: prediction $\delta = 64.5°$ vs observed $\delta = 65.7° \pm 1.5°$. Discrepancy $< 1\sigma$. At $\delta = 65.7°$: $J_\text{pred} \approx 3.1 \times 10^{-5}$ — in agreement with the observed $J \approx 3.08\times10^{-5}$.

:::info Honest assessment of the accuracy of J
Of the 4 parameters in the formula ($s_{12}$, $s_{23}$, $s_{13}$, $\delta$) only **one** ($\delta$) is predicted by the theory. The remaining three are observables. The residual phase discrepancy is small: $\sin(64.5°)/\sin(65.7°) = 0.903/0.911 = 0.991$ ($\sim 1\%$).

Correct formulation: with Fano-predicted phase $\delta = 64.5°$ and **observed** CKM angles: $J_\text{pred} = 0.967 \times J_\text{obs} \approx 3.0 \times 10^{-5}$. The only genuine prediction is $\sin\delta = 0.903$ vs observed $0.934$ ($\sim 3\%$ discrepancy).

*Corrected 2026-09-26 (T-345(e)):* that one parameter is retracted [✗] (Theorem 4.2), so none of the four is predicted.
:::

---

## 6. CKM from Mismatch of Yukawa Textures {#6-ckm-из-несовпадения-юкавских-текстур}

### Theorem 6.1 (CKM matrix in the Fano formalism) {#thm-6-1}

:::warning [✗] Retracted 2026-09-26 (T-345(e))
Earlier: "[T] Level 1 — structural prediction. Fano topology predicts Fritzsch texture. This is an original prediction of UHM." The Fritzsch texture is refuted by $\lvert V_{cb}\rvert$ ([§6.3](#derivation-vus)); the formulas (a)–(b) below are the generic small-angle expansion of $V=U_u^\dagger U_d$ and hold for any hierarchical texture.
:::

**Theorem.** CKM matrix $V = U_u^\dagger U_d$, where $U_{u,d}$ diagonalize $Y^{u,d} Y^{u,d\dagger}$:

**(a)** From hierarchical texture:

$$
U_u \approx \begin{pmatrix} 1 & -\epsilon_{12}/y_c & \epsilon_{13}/y_t \\ \epsilon_{12}^*/y_c & 1 & -\epsilon_{23}/y_t \\ -\epsilon_{13}^*/y_t & \epsilon_{23}^*/y_t & 1 \end{pmatrix}
$$

and similarly for $U_d$ (with $\epsilon^u \to \epsilon^d$).

**(b)** CKM elements (leading order):

$$
V_{us} \approx \frac{\epsilon_{12}^{d*}}{y_s} - \frac{\epsilon_{12}^{u*}}{y_c}
$$

$$
V_{cb} \approx \frac{\epsilon_{23}^{d*}}{y_b} - \frac{\epsilon_{23}^{u*}}{y_t}
$$

$$
V_{ub} \approx \frac{\epsilon_{13}^{d*}}{y_b} - \frac{\epsilon_{13}^{u*}}{y_t}
$$

### Theorem 6.2 (Quantitative CKM from Fano) {#thm-6-2}

:::warning [H] Level 2 — numerical values
Formulas $|V_{us}| \sim \sqrt{m_d/m_s}$ are standard consequences of Fritzsch texture (Fritzsch, 1977), not original predictions of UHM. The theory's prediction is the **texture structure** [T], not the numbers [H].

*Corrected 2026-09-26 (T-345(e)):* the texture structure is retracted [✗] (§6.3). In (a) the value $0.044$ is not what the Fritzsch texture gives: its exact diagonalisation gives $\lvert V_{cb}\rvert\ge0.073$ for every phase, and the factor $0.5$ from a "Fano phase" $\pi/7$ is not derived.
:::

**Theorem.** From Fano texture with $\epsilon_\text{eff} \approx 0.06$:

**(a)** $V_{cb}$. From Fritzsch texture ([Theorem 5.2](/docs/physics/particle-physics/yukawa-hierarchy#thm-5-2)): element $(2,3)$ of the mass matrix $M^u_{23} = B_u$, where $|B_u|^2 = m_c \cdot m_t$ (from the characteristic equation). Then:

$$
V_{cb} \approx \left|\frac{B_u}{m_t} - \frac{B_d}{m_b}\right| = \left|\sqrt{\frac{m_c}{m_t}} \cdot e^{i\phi_u} - \sqrt{\frac{m_s}{m_b}} \cdot e^{i\phi_d}\right|
$$

At $|\phi_u - \phi_d| \sim \pi/7$ (Fano phase):

$$
V_{cb} \approx \sqrt{m_c/m_t} \times |\sin\phi_u - \sin\phi_d| \approx 0.087 \times 0.5 \approx 0.044
$$

Observed: $|V_{cb}| \approx 0.040$. **Agreement** within 10%.

:::info Note on normalization
The naive estimate $\epsilon_{23} \sim \epsilon_\text{eff} y_t \approx 0.06$ substituted into the formula $V_{cb} \approx \epsilon_{23}^d/y_b - \epsilon_{23}^u/y_t$ gives the absurd result $V_{cb} \approx 2.5 > 1$. The error lies in the incorrect normalization: the mixing parameters $\epsilon_{23}$ scale as a fraction of the **corresponding** Yukawa (Fritzsch texture), not of $y_t$. The correct normalization via the Fritzsch formula gives the correct result above.
:::

**(b)** $V_{us}$ (Cabibbo angle):

$$
V_{us} \approx \sqrt{m_d/m_s} - \sqrt{m_u/m_c} \cdot e^{i\phi}
$$

$$
\approx \sqrt{0.0047/0.095} - \sqrt{0.0022/1.3} \cdot e^{i\phi} = 0.222 - 0.041 \cdot e^{i\phi}
$$

$$
|V_{us}| \approx 0.222 \pm 0.041 \approx 0.18\text{--}0.26
$$

Observed: $|V_{us}| = 0.2243 \pm 0.0005$. **Agreement** at the center of the range.

### 6.3 Derivation of the Formula $|V_{us}| \sim \sqrt{m_d/m_s}$ from Fritzsch Texture {#derivation-vus}

:::warning [H] Standard consequence of Fritzsch texture
The formula $|V_{us}| \sim \sqrt{m_d/m_s}$ is **not** an original prediction of UHM. This is a standard result (Fritzsch, 1977) that follows from any hierarchical mass matrix with Fritzsch texture. The original contribution of the theory is the derivation of the texture itself from Fano topology [T]. *Corrected 2026-09-26 (T-345(e)):* that derivation is retracted [✗] (box below).
:::

The derivation chain consists of two fundamentally distinct steps:

:::danger[The Fritzsch texture is refuted (T-345(e), 2026-09-26)]
Whatever its derivation, the texture below cannot describe the quarks. Its $(2,3)$ sector fixes $\lvert V_{cb}\rvert=\lvert\sqrt{m_s/m_b}-e^{i\phi}\sqrt{m_c/m_t}\rvert$ up to small corrections, and with the running masses at $M_Z$ (Huang and Zhou, *Phys. Rev. D* **103**, 016010 (2021): $m_s/m_b=0.01872$, $m_c/m_t=0.00368$) the exact diagonalisation gives $\lvert V_{cb}\rvert\ge0.073$ over all phases, against $0.04183^{+0.00079}_{-0.00069}$ (PDG 2024) — about $40\sigma$ (`test_fritzsch_six_zero_texture_overshoots_vcb`). That the original Fritzsch texture predicts too large a $\lvert V_{cb}\rvert$ and too small a $\lvert V_{ub}/V_{cb}\rvert$ is standard (B. Belfatto, Z. Berezhiani, *JHEP* **08** (2023) 162, arXiv:2305.00069). Step 1 was also derived in the axis reading of the generations (only $k=1$ on the Higgs line $\{A,E,U\}$), which cannot carry a family symmetry ([T-328(a)](/docs/physics/particle-physics/fermion-generations#поколения-t328)), and with $H\sim\gamma_{EU}$, which is [H]. The agreement $\lvert V_{us}\rvert\approx\sqrt{m_d/m_s}$ (Gatto–Sartori–Tonin) survives as an empirical relation of any texture with a zero in the $(1,1)$ entries; it is not a prediction of UHM.
:::

**Former Step 1 [✗] (was [T]): Fano topology $\to$ Fritzsch texture.** From the Fano selection rule ([Theorem 5.2](/docs/physics/particle-physics/yukawa-hierarchy#thm-5-2)) the down-quark mass matrix has the structure:

$$
M^d_\text{Fritzsch} = \begin{pmatrix} 0 & A_d & 0 \\ A_d^* & 0 & B_d \\ 0 & B_d^* & C_d \end{pmatrix}
$$

The zeros on the diagonal for the light generations are a consequence of the fact that only the third generation ($k=1$, dimension $A$) lies on the Higgs Fano line $\{E,U,A\}$. The elements $A_d$ and $B_d$ are generated by loop corrections through $V_3$ vertices.

**Step 2 [H]: Fritzsch texture + experimental masses $\to$ $|V_{us}|$.** From the characteristic equation of the matrix $M^d M^{d\dagger}$ with Fritzsch texture:

$$
|A_d|^2 = m_d \cdot m_s, \qquad |B_d|^2 = m_s \cdot m_b
$$

Diagonalization matrix $U_d$ at leading order:

$$
\sin\theta_{12}^{(d)} = \sqrt{\frac{m_d}{m_s}}, \qquad \sin\theta_{23}^{(d)} = \sqrt{\frac{m_s}{m_b}}
$$

Similarly for up-type quarks: $\sin\theta_{12}^{(u)} = \sqrt{m_u/m_c}$. CKM matrix element:

$$
V_{us} = \sin\theta_{12}^{(d)} \cdot e^{i\alpha_d} - \sin\theta_{12}^{(u)} \cdot e^{i\alpha_u}
$$

Since $\sqrt{m_d/m_s} \approx 0.222 \gg \sqrt{m_u/m_c} \approx 0.041$, the leading contribution:

$$
|V_{us}| \approx \sqrt{\frac{m_d}{m_s}} \approx 0.222
$$

Substituting experimental masses (PDG): $m_d = 4.7$ MeV, $m_s = 93.5$ MeV, $m_u = 2.2$ MeV, $m_c = 1.3$ GeV. Result $|V_{us}| \approx 0.222$ — in agreement with the observed $0.2243 \pm 0.0005$.

:::info Distinction of rigor levels
**What the theory was said to predict (retracted [✗], was [T]):** hierarchical texture $M^d$ with $M^d_{11} = M^d_{22} = 0$ (zeros on the diagonal), from which $|V_{us}| \sim \sqrt{m_d/m_s}$ follows **structurally**.

**What depends on experiment [H]:** the specific numerical value $0.222$ is determined by substituting the experimental masses $m_d$ and $m_s$, which are themselves not predicted by the theory with sufficient accuracy. From the Gap formalism: $m_d \sim \epsilon_\text{eff}^4 \cdot v$ and $m_s \sim \epsilon_\text{eff}^2 \cdot v$, whence $|V_{us}| \sim \epsilon_\text{eff}$ — only the order of magnitude $O(0.01\text{--}0.1)$.
:::

**(c)** $V_{ub}$:

$$
V_{ub} \approx \sqrt{m_u/m_t} \cdot e^{i\delta} \approx 0.0036 \cdot e^{i\delta}
$$

Observed: $|V_{ub}| \approx 0.0037$. **Agreement** within 3%.

---

## 7. Wolfenstein Parameters {#7-вольфенштейновские-параметры}

### Corollary 7.1 (Wolfenstein parameters)

**Corollary.** Predictions in the Wolfenstein parametrization:

| Parameter | Fano prediction | Observation | Status |
|---|---|---|---|
| $\lambda = \lvert V_{us}\rvert$ | $0.222$ | $0.22501 \pm 0.00068$ | [✗] (Fritzsch input, §6.3) |
| $A = \lvert V_{cb}\rvert/\lambda^2$ | $0.044/0.049 = 0.89$ | $0.826^{+0.016}_{-0.015}$ | [✗] ($0.044$ is not the Fritzsch value; that one is $\ge0.073$) |
| $\bar{\rho}$ | depends on $\delta$ | $0.1591 \pm 0.0094$ | [H] |
| $\bar{\eta}$ | depends on $\delta$ | $0.3523^{+0.0073}_{-0.0071}$ | [H] |

*Observations updated 2026-09-26 to the PDG 2024 fit (Eq. 12.26 of the CKM review); the column read $0.2243$, $0.836$, $0.122$, $0.356$.*

Precise values of $\bar{\rho}$, $\bar{\eta}$ depend on the phases of the Yukawa matrices, which require non-perturbative computation.

---

## 8. Honest Assessment of Status {#8-честная-оценка-статуса}

### 8.1 What the Theory Actually Predicts

:::tip Structural statements (items 1–3 retracted 2026-09-26, T-345(e); item 4 retracted 2026-09-26, T-99; items 5–6 [T])
1. ~~**Fritzsch texture** from Fano topology — hierarchical $3 \times 3$ mass matrix.~~ [✗]: refuted by $\lvert V_{cb}\rvert$ (§6.3).
2. ~~**Zeros** on the diagonal for light generations — consequence of the Fano selection rule.~~ [✗]: same texture.
3. ~~**CP phase** determined by $\mathbb{Z}_7$-structure — discrete set of possible values.~~ [✗]: the multiples of $2\pi/7$ nearest the data, $51.4°$ and $77.1°$, are $9.5\sigma$ and $7.6\sigma$ away (Theorem 4.2).
4. **Strong CP: $\theta_\text{QCD} = 0$** — [T-99, \[C at (SV)\]](/docs/physics/gauge-symmetry/confinement#теорема-структурное-theta-qcd) (corrected 2026-09-25 from [T]): only through the chain of the retracted cubic $V_3$. The corrected potential is PT-even, and no lift of its vacuum's antiunitary symmetry gives $\bar\theta = 0$ with $m_t \neq m_b$ and $J \neq 0$ ([T-333](/docs/physics/gauge-symmetry/confinement#pt-на-фермионах-t341)). With the fields the Clifford frame forces there is no Peccei–Quinn symmetry and no spontaneous CP violation, so $\bar\theta$ is a free parameter there ([T-333(e)–(h)](/docs/physics/gauge-symmetry/confinement#пк-и-нб)). *Retracted [✗] 2026-09-26 (T-99 corrected):* the $V_3$ chain fails at its own step 4, so $\theta_\text{QCD} = 0$ is not derived at all; strong CP is open [Pr] ([Confinement §3.1c](/docs/physics/gauge-symmetry/confinement#тета-не-из-потенциала)).
5. **One channel gives no mixing [T]** ([T-332(g)](/docs/physics/particle-physics/higgs-sector#юкавы-t340)): if every generation couples through one flavour matrix times the same internal Clifford operator, $M_u \propto M_d$ and $V_{\mathrm{CKM}} = 1$. Mixing needs at least two channels (in $\mathrm{SO}(10)$ language, $\mathbf{10}$ with $\overline{\mathbf{126}}$ or $\mathbf{120}$). Under the hypothesis (UP) the down-type matrix is subleading, so the whole CKM matrix comes from subleading down-type terms. These must be tree-level, of relative size $\varepsilon\approx0.03$: the exact (UP), with a vanishing down-type matrix, is refuted, and loops cannot generate it ([T-332(h)–(k)](/docs/physics/particle-physics/higgs-sector#голоморфность-вп)). Its hierarchy is not derived [Pr].
6. **What the clock can and cannot supply [T]** ([§11](#11-вкус-с-часов), T-345): every structure of the clock register that commutes with its tick — the Fano incidence, the quadratic residues and Gauss sums, the clock Hamiltonian, the anchor on the trivial harmonic — is diagonal on the generations and gives $\lvert V\rvert$ a permutation matrix in any number of channels; the only automorphism-fixed instant gives the democratic rank-one matrix; and two channels one of which is rank one cannot fit the quark and lepton masses together.
:::

### 8.2 What Follows from Standard Formulas [H]

:::warning [H] Numerical values
Numerical values of CKM elements ($|V_{us}| \approx 0.222$, $|V_{cb}| \approx 0.044$, $|V_{ub}| \approx 0.0036$, $J \approx 3 \times 10^{-5}$) follow from Fritzsch texture upon substituting the observed quark masses. Formulas:
- $|V_{us}| \sim \sqrt{m_d/m_s}$
- $|V_{cb}| \sim \sqrt{m_c/m_t}$
- $|V_{ub}| \sim \sqrt{m_u/m_t}$

These are standard formulas (Fritzsch, 1977), not original predictions of UHM.

*Corrected 2026-09-26 (T-345(e)):* the texture behind them is refuted ($\lvert V_{cb}\rvert\ge0.073$ against $0.0418$, §6.3); $\lvert V_{us}\rvert\approx\sqrt{m_d/m_s}$ survives as the empirical Gatto–Sartori–Tonin relation, and $0.044$ is not a Fritzsch value.
:::

### 8.3 Anatomy of the Derivation Chain: Structure vs Numbers

For each CKM result it is necessary to clearly distinguish two levels:

| Statement | Level | What it uses | Status |
|---|---|---|---|
| Yukawa matrix is Fritzsch texture | Structural, retracted [✗] 2026-09-26 (was [T]) | Fano topology, $\mathbb{Z}_7$-symmetry | Refuted: $\lvert V_{cb}\rvert\ge0.073$ against $0.0418$ (was "genuine prediction") |
| $\lVert V_{us}\rVert \approx \sqrt{m_d/m_s} \approx 0.222$ | Consequence [H] | Texture + $m_d = 4.7$ MeV, $m_s = 93.5$ MeV (PDG) | Standard Fritzsch |
| $\lVert V_{cb}\rVert \approx \sqrt{m_c/m_t} \times f(\phi) \approx 0.044$ | Consequence [H] | Texture + $m_c$, $m_t$ (PDG) + Fano phase | Depends on $\lVert\phi_u - \phi_d\rVert$ |
| $\lVert V_{ub}\rVert \approx \sqrt{m_u/m_t} \approx 0.0036$ | Consequence [H] | Texture + $m_u$, $m_t$ (PDG) | Standard Fritzsch |
| $\sin\delta_\text{CP} \approx 0.903$ | Retracted [✗] 2026-09-26 (was prediction [H]) | $V_3$-phase from $\mathbb{Z}_7$ + two-loop correction | The $12.6°$ correction is absent in the SM; $V_3$ retracted (T-331) (was "only genuine numerical prediction") |

The formula $|V_{us}| \sim \sqrt{m_d/m_s}$ is a standard consequence of Fritzsch texture (Fritzsch, 1977). It arises from diagonalizing the mass matrix $M^d M^{d\dagger}$ with zero diagonal elements for the light generations (detailed derivation: [section 6.3](#derivation-vus)). The analogous formulas $|V_{cb}| \sim \sqrt{m_c/m_t}$ and $|V_{ub}| \sim \sqrt{m_u/m_t}$ follow from elements $(2,3)$ and $(1,3)$ of the diagonalization matrices.

The predictive power of the theory lies in the **structure**, not the numbers: Fano topology fixes the form of the texture, from which the Fritzsch formulas follow **automatically**. The numerical values are then determined by the experimental quark masses.

*Corrected 2026-09-26 (T-345(e)):* the structure named here is retracted [✗] — the Fritzsch texture gives $\lvert V_{cb}\rvert\ge0.073$ against $0.0418$ — and no parameter-free structure of the clock supplies another one (§11).

### 8.4 Honest Assessment of the Jarlskog Invariant

*Corrected 2026-09-26 (T-345(e)):* the phase $64.5°$ used below is retracted [✗] (Theorem 4.2), so $J$ here has no predicted parameter left; the text is the former assessment.

Of the 4 parameters of the formula $J = c_{12} c_{23} c_{13}^2 s_{12} s_{23} s_{13} \sin\delta$ only **one** ($\delta$) is predicted by the theory. The remaining three angles ($s_{12}$, $s_{23}$, $s_{13}$) are observed quantities. The claim of "agreement within 1%" for $J$ is due to:

$$
\frac{\sin(64.5°)}{\sin(69°)} = \frac{0.903}{0.934} = 0.967
$$

The discrepancy of $J_\text{pred}$ and $J_\text{obs}$ is determined **only** by the discrepancy in the phase ($\sim 3\%$). Correct formulation: with Fano-predicted phase $\delta = 64.5°$ and **observed** CKM angles: $J_\text{pred} = 0.967 \times J_\text{obs} \approx 3.0 \times 10^{-5}$. The only genuine prediction is $\sin\delta = 0.903$ vs observed $0.934$ ($\sim 3\%$ discrepancy, $\sim 1\sigma$).

### 8.5 Updated Status Table

| Result | Original status | Current status |
|---|---|---|
| **Fritzsch texture from Fano topology** | [T] | **[✗]** (2026-09-26: $\lvert V_{cb}\rvert\ge0.073$ against $0.0418$) |
| **$\lVert V_{us}\rVert$, $\lVert V_{ub}\rVert$ numerical** | [T] (1%) | **[H]** (consequence of Fritzsch + observed masses) |
| **$\lVert V_{cb}\rVert$ numerical** | [T] (4%) | **[H]** (depends on phase; standard Fritzsch) |
| **$J \approx 3.1 \times 10^{-5}$** | [T] (1%) | **[H]** (3 out of 4 parameters are observables; real accuracy $\sim 3\%$ in $\sin\delta$) |
| **$\sin\delta \approx 0.90$** | [H] | **[✗]** (2026-09-26: the $12.6°$ correction is absent in the SM; $\delta$ runs by $0.003°$) |
| **$\delta_\text{CP}$ from $V_3$-phase** | [H] | **[✗]** (2026-09-26: $V_3$ retracted, T-331; values $7.6\sigma$ and $9.5\sigma$ off) |
| **Mixing angles $2\pi\lvert\Delta k\rvert/7$ with RG suppression** | [H] | **[✗]** (2026-09-26: $2:3:1$ against $60.8:11.2:1$; angles do not run) |
| **Normalization of $\epsilon_{23}$ via Fritzsch formula** | [T] | **[H]** (direct computation from Gap formalism gives $V_{cb} \approx 2.5$; transition to Fritzsch formula — post-hoc correction) |

### 8.6 What is a Genuine Prediction and What is Not

:::tip [P] Full list of genuine CKM-sector predictions (corrected 2026-09-26)
1. ~~**Fritzsch texture** from Fano topology — $M^{u,d}_{11} = M^{u,d}_{22} = 0$ for light generations [T].~~ Retracted [✗] (§6.3).
2. ~~**Form** of the mixing formulas ($|V_{us}| \sim \sqrt{m_d/m_s}$ etc.) as a **structural** consequence of the texture [T].~~ Retracted [✗] with the texture.
3. ~~**CP-violation phase** $\delta_\text{CP}$ determined by $V_3$ and $\mathbb{Z}_7$-structure, not a free parameter [H].~~ Retracted [✗] (Theorem 4.2).
4. ~~**$\theta_\text{QCD} = 0$** — consequence of the isotropy of the Gap vacuum of the retracted $V_3$, [C at (SV)] (corrected 2026-09-25 from [T]; T-333 closes the route through the corrected vacuum).~~ Retracted [✗] 2026-09-26 (T-99 corrected): the vacuum of $V_3$ is not isotropic in the phases; $\bar\theta$ is free ([Confinement §3.1c](/docs/physics/gauge-symmetry/confinement#тета-не-из-потенциала)).
:::

:::warning Correct status of numerical predictions
- Numerical values of CKM elements ($|V_{us}| = 0.222$, $|V_{cb}| = 0.044$, etc.) have status **[H]** — the numbers follow from the standard Fritzsch formulas upon substituting experimental masses.
- Agreement for CP violation: $\sin\delta_\text{pred} / \sin\delta_\text{obs} = 0.967$, i.e. $\sim 3\%$ — order of magnitude, not an exact prediction.
- *Corrected 2026-09-26 (T-345(e)):* the Fritzsch texture and $\delta_\text{pred} = 64.5°$ are retracted [✗]; the numbers above are the Gatto–Sartori–Tonin relation and substituted observations, not predictions.
:::

### 8.7 Open Questions

*Corrected 2026-09-26 (T-345(e)):* the first two items are void — Theorems 3.1 and 4.2 are retracted — and the last one is answered in the negative for the clock structures ([§11](#11-вкус-с-часов)).

- The normalization factor $C_\text{norm} \approx 26$ is tuned, not derived.
- The sign of the two-loop correction to $\delta_\text{CP}$ is fixed by SM 2-loop RG (negative) **[C under SM 2-loop RG]**; the precise magnitude $|\delta^{(2)}|$ depends on GUT threshold corrections **[H]**.
- Precise values of Wolfenstein $\bar{\rho}$, $\bar{\eta}$ require non-perturbative computation.
- The assignment $k=2 \leftrightarrow k=4$ is a hypothesis.
- Computation of $V_{cb}$ from first principles (without substituting the Fritzsch formula) requires the correct normalization of $\epsilon_{23}$ from the Yukawa texture.
- Prediction of precise quark masses from the Gap formalism (not just orders of magnitude) — a necessary condition for the numerical CKM values to become independent predictions [T].

---

## 9. Non-circularity is an input-identification requirement {#ckm-non-circularity}

### 9.1 What a supplied Dirac operator computes

In a chosen Standard-Model finite spectral geometry, $D_F$ contains Yukawa and neutrino matrices as spectral data. Given them and a supplied Higgs scale, their singular values give fermion masses. Left singular bases give

$$
V_{\rm CKM}=U_{uL}^\dagger U_{dL}.
$$

This is a correct computation [T at the supplied matrices]. Treating $D_F$ as fixed during diagonalization does not prove that it was obtained independently of the observed masses or mixing. The [Chamseddine–Connes–Marcolli model](https://arxiv.org/abs/hep-th/0610241) supplies a geometric framework and relations at its stated scale; it is not a theorem deriving every Yukawa entry from UHM.

### 9.2 What rigidity does not determine

The former universal primitive rigidity T-173 is withdrawn [✗]. Choosing a positive three-form/frame gives a $G_2$ representation [D/T]; it does not determine a fermionic Dirac operator or its coefficients. Conditional RI gives comparison of reversible encoders preserving specified structure; it does not select that structure or physical Yukawa couplings.

Representation branching, anomaly constraints and a prescribed sparsity pattern can restrict admissible data, but restrictions alone need not fix the coefficients. “Every pair lies on a Fano line for some third axis” is true for every distinct pair and supplies no sparsity. An independently justified scalar/fermion carrier and selection rule must be stated. The selected finite arithmetic/group bounds of later sections remain valid at their assumptions, without fixing an unrestricted $D_F$.

### 9.3 A conditional prediction protocol [C/Pr]

A CKM value is predicted only when the model's matrices, scales, frame and coefficients are fixed **without using that target datum**, with their provenance recorded. If measured masses are used to identify parameters, CKM may still be an out-of-sample conditional prediction; those masses are inputs and must be listed. Fitting a normalization to $V_{us}$ makes that element an input, not a prediction.

To establish non-circularity, publish the parameter/input list, identification rule, uncertainty propagation, and held-out predictions before comparison. Diagonalization proves how observables follow from fixed data; it does not prove where the data came from. The old “theorem at T-173” and blanket claim of no Yukawa parameters are withdrawn [✗].

### 9.4 Fritzsch texture and residual parameters

The Hermitian texture

$$
Y=\begin{pmatrix}0&A&0\\A^*&0&B\\0&B^*&C\end{pmatrix}
$$

still has supplied coefficients. Hermiticity alone neither forces its zeros nor fixes $A,B,C$. The old universal emergence from $G_2$/Fano labels and its quantitative CKM claim are withdrawn [✗]; [T-345(e)](#11-вкус-с-часов) records the $|V_{cb}|$ obstruction. An alternative texture or coupling model must be independently specified and validated.

### 9.5 Remaining work

A quantitative flavor model needs an independently identified $D_F$, its dynamics/RG matching, numerical validation and uncertainties [Pr/H]. The missing structure is not automatically supplied by a finite-group arithmetic bound, a chosen frame, a spectral cutoff or an assertion that only computational work remains. The subsequent conditional clock-family results are separate from a complete derivation of all fermion data.

## 10. UHM and the Cabibbo Angle Anomaly (T-265) {#10-cabibbo-angle-anomaly}

The **Cabibbo Angle Anomaly** (CAA) is a $\sim 3.2\sigma$ deficit in the first-row CKM unitarity test:

$$
|V_{ud}|^2 + |V_{us}|^2 + |V_{ub}|^2 = 0.9985(5) < 1,
$$

with $V_{ud} = 0.97373(31)$ from superallowed nuclear $\beta$ decay and $V_{us}$ from $K_{\ell 3}$ (a second internal tension has since appeared between $V_{us}$ from kaon and pion semileptonic decays). The standard resolution taxonomy splits into two families:

- **Standard-Model extraction** — nuclear/hadronic radiative corrections (notably the $\gamma W$ box, $\Box_{\gamma W}^A = 3.90(9)\times 10^{-3}$, and its nuclear-structure dependence), the lattice form factor $f_+^K(0) = 0.9698(17)$, and the $K$–$\pi$ $V_{us}$ tension.
- **Beyond the Standard Model** — a fourth generation, **vector-like quarks** (the phenomenologically "most promising" global-fit candidate), **MeV-scale sterile neutrinos** (which raise the extracted $|V_{ud}|$), leptoquarks, vector boson triplets, vector-like leptons, or otherwise modified $W$–quark couplings.

The UHM spectrum is fixed, and it collides head-on with the BSM family.

### Theorem 10.1 (Resolution channel of the CAA) [H] {#thm-10-1-t-265}

*Status corrected 2026-09-25 from [T-structural]+[C] to [H].* The table below keeps the former grounds and gives each exclusion its status now: the fourth generation is excluded only [C at 43c identification] — the count 3 is exact, its identification with the physical generations is [I] (registry row 43c); the vector-like-quark exclusion is [H], because its chirality ground is retracted ($i\Gamma_O\Gamma_A\Gamma_S\Gamma_D$ has eigenvalues $\pm i$, and all $G_2$ representations are real — [Standard Model, §4](/docs/physics/gauge-symmetry/standard-model#кираль)); the leptoquark/extra-boson exclusion is [H], because the 'exactly SM gauge content' rests on (FE), now [C at (FE)], and on [T-297](/docs/physics/gauge-symmetry/standard-model#запрет-z-прайм), now [H]. The channel prediction is therefore a hypothesis.

**Statement (T-265).** Within UHM the physical quark-mixing matrix is **exactly the $3\times3$ CKM matrix and is exactly unitary**; consequently, if the CAA persists, it must resolve **entirely within the Standard-Model extraction sector** and **not** through any new quark, lepton, or boson state. Every leading BSM resolution channel is excluded by the fixed UHM spectrum:

| BSM channel | UHM verdict | Ground |
|---|---|---|
| **Fourth generation** | **excluded [C at 43c identification]** (listed as a theorem until 2026-09-25) | $N_{\text{gen}} = 3$ exactly — the generations are the quadratic residues $\{1,2,4\} = \mathrm{QR}(7)$, the **unique** order-3 subgroup of $\mathbb{Z}_7^\ast$ closed under the associative Fano product ([§1](/docs/physics/particle-physics/fermion-generations#1-число-поколений-из-топологии-gap-вакуума)); not 2, not 4, not 6 |
| **Vector-like quarks** | **[H]** (listed as excluded [T-structural] until 2026-09-25) | *Retracted ground:* UHM fermions are chiral by construction: $\gamma_5 = i\Gamma_O\Gamma_A\Gamma_S\Gamma_D$ acts with definite eigenvalue on the internal spinor ([SM sector, chirality](/docs/physics/gauge-symmetry/standard-model#кираль)) — the frame admits no non-chiral (vector-like) quark configuration. *Why retracted:* $i\Gamma_O\Gamma_A\Gamma_S\Gamma_D$ has eigenvalues $\pm i$, and $G_2$ has only real representations; chirality enters with Connes' imported $H_F$ |
| **MeV sterile neutrino** | **excluded [C]** | the neutrino sector is type-I seesaw with three right-handed $\nu_R = (1,1)_0$ at $M_R \sim 3\times10^{14}$ GeV and normal hierarchy ([neutrino masses §2](/docs/physics/particle-physics/neutrino-masses#seesaw)) — no eV–MeV sterile state in the spectrum |
| **Leptoquarks / extra gauge bosons** | **[H]** (listed as excluded [T-structural] until 2026-09-25) | *Former ground:* the gauge sector is $G_2 \to \mathrm{SU}(3)_C\times\mathrm{SU}(2)_L\times\mathrm{U}(1)_Y$ with exactly SM content [T], and the **only** scalar is the unique $\{A,E,U\}$ Higgs line [T] — no leptoquark scalar, no vector boson triplet. *Now:* $G_2$ does not contain $SU(2)_L\times U(1)_Y$ (rank 2 < 4), the electroweak construction is [C at (FE)], and the no-$Z'$ corollary T-297 is [H] |

**Consequence.** UHM makes a sharp, falsifiable prediction about the *channel* of the anomaly: the deficit lives in the **$\gamma W$-box / nuclear-structure radiative corrections, the lattice $K$/$\pi$ form factors, or the $K$–$\pi$ $V_{us}$ tension** — the SM hadronic/nuclear inputs — not in the mixing matrix itself.

**Self-consistency.** This is precisely what licenses the corpus's own Cabibbo derivation ([§3](#3-угол-кабиббо)) to fix the normalisation $C_{\text{norm}}$ from the CKM unitarity condition: UHM's fundamental CKM is exactly unitary [C at 43c identification] (the count $N_{\text{gen}}=3$ is exact, its physical identification is [I]; until 2026-09-25 this read "T from $N_{\text{gen}}=3$"), so the measured $\sim 0.15\%$ deficit is, within UHM, an **extraction artifact**, not a property of the mixing. *Note 2026-09-26 (T-345(e)):* the Cabibbo derivation of §3 is retracted [✗], so this licence no longer serves a derivation; the unitarity statement itself is unaffected.

**What UHM does *not* predict [D].** The **magnitude** and **sign** of the deficit are Standard-Model hadronic/nuclear physics (the size of $\Box_{\gamma W}$, nuclear-structure corrections, form-factor values); UHM offers no derivation of the $\sim 0.15\%$ number. That residual is the genuinely open part.

:::warning Falsification of T-265
If the CAA is established to **require** a fourth generation, a vector-like quark, an MeV sterile neutrino, or a leptoquark — e.g. a collider discovery of such a state, or a precision global fit that excludes the SM-radiative resolution at high significance — then the identification of the three $\mathrm{QR}(7)$ classes with the physical generations (registry row 43c) is falsified; the count itself is arithmetic. Conversely, resolution through improved $\gamma W$-box / lattice / $K$–$\pi$ treatment **confirms the UHM-predicted channel**. Status (corrected 2026-09-25; it read [T-structural] for the first three exclusions): [C at 43c identification] for the fourth-generation exclusion, [H] for the vector-like-quark and leptoquark exclusions, [C] for the sterile-neutrino exclusion, [D] for the magnitude.
:::

**Proof sketch.** (1) $N_{\text{gen}}=3$ is [T] ([§1](/docs/physics/particle-physics/fermion-generations#1-число-поколений-из-топологии-gap-вакуума), [fermion generations Thm 6.1](/docs/physics/particle-physics/fermion-generations#thm-6-1)): the associator-free Fano triplet is unique, $\{1,2,4\}$, and equals the unique order-3 subgroup of $\mathbb{Z}_7^\ast$. Hence exactly three generations and a $3\times3$ mixing matrix — given that these three classes are the physical generations, which registry row 43c records as [I]. (2) The Yukawa matrices are $3\times3$; their bi-unitary diagonalisation yields a $3\times3$ **unitary** CKM ([Thm 1.1](#thm-1-1)); with no further quark states, first-row unitarity is exact. (3) ~~Chirality (γ₅ definite on $\chi_{\text{int}}$) forbids vector-like partners;~~ (retracted 2026-09-25: the γ₅ written there has eigenvalues $\pm i$, so no exclusion of vector-like partners follows); the unique Higgs line forbids leptoquark scalars; the seesaw spectrum has no light sterile. (4) Therefore any observed unitarity deficit is not a property of the fundamental $V_{\text{CKM}}$ and must originate in the extraction — the SM radiative/lattice inputs. $\blacksquare$

---

## 11. Flavour from the clock: what can break the family ℤ₃ (T-345) {#11-вкус-с-часов}

:::tip[Status: (a)–(d) \[T\] as mathematics; with the data they refute \[✗\] every parameter-free structure of the clock register in any number of channels and every two-channel frame with a rank-one channel; (e) the former numerical claims of this page \[✗\]; (f) the three-channel frame \[H\]]
Registry row T-345 (2026-09-26). The question: under the hypothesis (GC) of [T-328](/docs/physics/particle-physics/fermion-generations#поколения-t328) the family $\mathbb{Z}_3$ must be broken ([T-328(d)](/docs/physics/particle-physics/fermion-generations#поколения-t328)) and mixing needs at least two Clifford channels ([T-332(g)](/docs/physics/particle-physics/higgs-sector#юкавы-t340)). Can a structure the clock already carries, with no free parameter, supply the breaking and predict masses and mixing?
:::

**Setting.** Under (GC) a generation is a non-trivial real harmonic of $\mathbb{Z}_7$ on the clock register $\mathcal{H}_{\text{clock}}\cong\mathbb{C}^7$. The energy states $\lvert k\rangle$ of $H_O=\omega_0\sum_k k\lvert k\rangle\langle k\rvert$ are the harmonics, grouped into the planes $\{k,7-k\}$; the time states are $\lvert\tau_n\rangle=7^{-1/2}\sum_k e^{-2\pi i kn/7}\lvert k\rangle$, and the tick $V_O$ maps $\lvert\tau_n\rangle$ to $\lvert\tau_{n+1}\rangle$ ([emergent time](/docs/proofs/dynamics/emergent-time)). The family $\mathbb{Z}_3$ is multiplication of the labels by $2$ and $4$. In the $\mathrm{Spin}(10)$ Clifford frame ([T-329](/docs/physics/gauge-symmetry/standard-model), [T-332](/docs/physics/particle-physics/higgs-sector#юкавы-t340)) a whole generation is one $\mathbf{16}$, and each channel $c$ ($\mathbf{10}$, $\overline{\mathbf{126}}$, $\mathbf{120}$) couples $\psi_i\psi_j$ through one flavour matrix $Y_c$ on the generations: $M_f=\sum_c v_f^{(c)}Y_c$, with the same $Y_c$ in the up, down, charged-lepton and neutrino-Dirac masses and only the coefficients depending on the sector (for example $v_e^{(126)}=-3v_d^{(126)}$).

The candidates without free parameters are: (i) the circulants of the clock — the Fano incidence (lines $\{t,t+1,t+3\}$), its collinearity $2I+J$, the quadratic-residue sum $\sum_{q\in\mathrm{QR}}V_O^{\,q}$ whose eigenvalues are the Gauss sum $b_7=(-1+i\sqrt7)/2$ and its conjugate, and the cyclic Hamming code, which is the quadratic-residue code of length 7; (ii) the clock Hamiltonian $H_O$ and its functions; (iii) the self-model anchor $uu^\dagger$ with $u$ uniform, which on the clock register is either the projector onto the trivial harmonic ($u$ uniform over time states) or $\lvert\tau_0\rangle\langle\tau_0\rvert$ ($u$ uniform over energy states); (iv) time-localised structures — the instants $\lvert\tau_n\rangle\langle\tau_n\rvert$ and the time operator $T=\sum_n n\lvert\tau_n\rangle\langle\tau_n\rvert$, which is what the depth register ([emergent time §11.4](/docs/proofs/dynamics/emergent-time#114-регистр-глубины)) adds to one clock: its digits are ordered readings of the same $\mathbb{Z}_7$.

**Theorem 11.1 (T-345).**

**(a) Everything that commutes with the tick is diagonal on the generations [T].** An operator that commutes with $V_O$ is diagonal in the energy basis and so maps each harmonic plane to itself. All of (i), (ii) and the first placement of (iii) are of this kind. Yukawa matrices built from them, in any number of channels, are diagonal in one basis in every sector, so $\lvert V_{\mathrm{CKM}}\rvert$ is a permutation matrix and a PMNS column has modulus 1. This is refuted by $\lvert V_{us}\rvert=0.22501\pm0.00068$ (PDG 2024). Besides, the Fano circulants have eigenvalues of modulus $\sqrt2$ on all six non-trivial harmonics (a difference set with $\lambda=1$), the residue sum has $b_7$ or $\bar b_7$ with $\lvert b_7\rvert=\sqrt2$, and the collinearity is $2$ on all of them: equal moduli on the three generations and degenerate masses, refuted by $m_c/m_t=0.00368$. $H_O$ separates them only as $1:2:4$ (or $1:2:3$), refuted by the hierarchy.

**(b) The instant fixed by the family is democratic [T].** Of the seven time states only $\lvert\tau_0\rangle$ is fixed by $n\mapsto2n$. On the generations $\lvert\tau_0\rangle\langle\tau_0\rvert$ is the democratic matrix $J/7$ (all entries equal), of rank one; the anchor in the second placement is exactly this matrix. It is invariant under all permutations of the generations, so it keeps the family $\mathbb{Z}_3$. Alone it gives one massive generation and two massless ones in every sector — the leading form of the observed hierarchy — and no mixing. The other instants $\lvert\tau_n\rangle\langle\tau_n\rvert$ are the same matrix up to a rephasing of the generations.

**(c) Structures in a common plane leave a unit entry [T].** If the ranges of all flavour matrices of both quark sectors lie in one two-dimensional subspace (for example two instants), each sector has a massless state and $\lvert V\rvert$ has an entry of modulus 1. Refuted by $m_u=1.23$ MeV at $M_Z$ and by $\min_{ij}\lvert V_{ij}\rvert=\lvert V_{ub}\rvert=0.003732$.

**(d) Two channels, one of rank one, cannot carry quarks and leptons [T].** Let $M_f=\alpha_f A+\beta_f B$ with $A$ of rank one and $A$, $B$ common to $u$, $d$, $e$, and let the rank-one channel carry the heavy generation, $x_f=\beta_f/\alpha_f$ small (normalise $\lVert A\rVert=1$). Write $\tilde B$ for the compression of $B$ to the complements of the range and co-range of $A$, and $s_1$ for its larger singular value. Then

$$
\frac{m_2}{m_3}=\lvert x_f\rvert s_1\,\bigl(1+O(x_f)\bigr),\qquad \frac{m_1}{m_2}=\frac{\lvert\det\tilde B-x_f\,c\rvert}{s_1^{2}}\,\bigl(1+O(x_f)\bigr),
$$

with a constant $c$ fixed by $A$ and $B$: $m_1/m_2=\lvert\rho-\kappa\xi_f\rvert$, where $\lvert\xi_f\rvert=m_2/m_3$ and $\rho$, $\kappa$ are the same in every sector. With the running masses at $M_Z$ (Huang, Zhou, *Phys. Rev. D* **103**, 016010 (2021)) $m_2/m_3=0.00368,\ 0.01872,\ 0.05887$ and $m_1/m_2=0.00198,\ 0.0502,\ 0.00475$ for $u$, $d$, $e$. The triangle inequality gives $\lvert\kappa\rvert\ge(0.0502-0.00198)/(0.00368+0.01872)=2.15$ from $u$ and $d$, and $\lvert\kappa\rvert\le(0.00475+0.00198)/(0.05887-0.00368)=0.122$ from $u$ and $e$. The two bounds differ by a factor of 17.7, while the neglected terms are of relative size $\lesssim0.06$. So every two-channel frame with a rank-one channel is refuted — in particular the democratic instant of (b) with any second channel, clock-built or not. A direct scan says the same for full-rank pairs of clock structures: over all 112 ordered pairs from $\{1, H_O, H_O^2, \lvert\tau_0\rangle\langle\tau_0\rvert, T, T^2, \{H_O,T\}/2, i[H_O,T]\}$ on the harmonics $\{1,2,4\}$ or $\{1,2,3\}$, the pencil $A+xB$ over the whole complex plane never comes closer to $(m_u/m_t, m_c/m_t)$ than a factor $e^{2.46}=11.7$, nor to the down-type ratios than a factor $e^{0.69}=2.0$.

**(e) The former claims of this page [T for the computations; the claims are ✗].** The six-zero Fritzsch texture gives $\lvert V_{cb}\rvert\ge0.073$ (§6.3). The Fano angle ratios $2:3:1$ stand against $60.8:11.2:1$ (§2.2). In one-loop Standard Model running from $M_Z$ to $2\times10^{16}$ GeV the CKM phase moves by $0.003°$, so the "two-loop correction" $12.6°$ of Theorem 4.2 does not exist, and the uncorrected $\lvert\delta\rvert=77.1°$ ($51.4°$) is $7.6\sigma$ ($9.5\sigma$) from $65.7°\pm1.5°$. The parameter-free phase of the Gauss sum, $\pi-\arg b_7=\arctan\sqrt7=69.30°$, is $2.4\sigma$ away and has no mechanism behind it.

**(f) Three channels with the canonical clock structures [numbers; the frame [H]].** By (d), and by the two-Higgs no-go of Babu, Bajc and Saad — a real $\mathbf{10}_H$ with a $\overline{\mathbf{126}}_H$ forces $\lvert v_u\rvert=\lvert v_d\rvert$ in the $\mathbf{10}$ and cannot split $m_t$ from $m_b$ (the equal-moduli statement of T-332(b)), and $\overline{\mathbf{126}}_H$ with $\mathbf{120}_H$ gives $m_\tau/m_b\simeq3$ at the GUT scale against $1.4$–$1.7$ — the Clifford frame needs all three channels. With the canonical clock structures in them — $\mathbf{10}\propto\lvert\tau_0\rangle\langle\tau_0\rvert$ of (b), $\overline{\mathbf{126}}$ tick-commuting (any diagonal matrix), $\mathbf{120}\propto$ the $\mathbb{Z}_3$-covariant antisymmetric matrix ($A_{12}=A_{23}=A_{31}=1$) — and free complex coefficients, a numerical search over the ten quark observables at $10^{12}$ GeV (one-loop running from $M_Z$) found no fit. The best maximal deviation is a factor $e^{0.34}=1.40$ with the diagonal free (14 real parameters, 360 seeded starts and 300 local restarts from the best), where $m_s$ comes out 43 % high, $m_b$ 31 % low and $\lvert V_{cb}\rvert$ 25 % low together, and $e^{1.34}=3.8$ with the diagonal fixed to $H_O$. This is a search, not a proof. The most constrained frame known to be viable is the minimal renormalizable non-supersymmetric $\mathrm{SO}(10)$ with a real $\mathbf{10}_H$, a real $\mathbf{120}_H$, a complex $\overline{\mathbf{126}}_H$ and free flavour matrices: K. S. Babu, B. Bajc, S. Saad, *JHEP* **02** (2017) 136 (arXiv:1612.04329) fit all fermion masses and mixings with it and, with a type-I seesaw, predict normal ordering, a nearly massless lightest neutrino ($m_1=1.5\times10^{-4}$ eV at the GUT scale), $m_{\beta\beta}=2.1$ meV, $m_\beta=5.1$ meV and $\delta_{\mathrm{PMNS}}=2.8°$ (their Table 4; with type I+II, $\delta_{\mathrm{PMNS}}=-151°$ and $m_{\beta\beta}=4.1$ meV). Against NuFIT 6.0 (normal ordering without SK atmospheric data, $\delta=177^{+19}_{-20}\,°$, $3\sigma$ range $96°$–$422°$) both phases lie inside $3\sigma$ and outside $1\sigma$; inverted ordering is disfavoured there by $\Delta\chi^2=6.1$. The real $\mathbf{10}_H$ of that model is what the colour-free Clifford plane of T-332 is. Taking this frame for UHM is a hypothesis [H]. It is refuted by inverted ordering, by $m_{\beta\beta}$ well above $5$ meV, or by $\delta_{\mathrm{PMNS}}$ established near $180°$ at more than $3\sigma$. Its numbers belong to the $\mathrm{SO}(10)$ fit, not to UHM: nothing in UHM fixes its flavour matrices.

**Proof.** (a) $V_O$ has seven distinct eigenvalues, so its commutant is the diagonal algebra; circulants in time are functions of $V_O$. The eigenvalue of the circulant with offset set $S$ on the harmonic $k$ is $\sum_{s\in S}e^{-2\pi iks/7}$, and $\lvert\sum_{s\in S}\zeta^{ks}\rvert^2=\lvert S\rvert-\lambda+\lambda\cdot7\,\delta_{k0}$ for a $(7,3,1)$ difference set, i.e. $2$ for $k\neq0$; for $S=\mathrm{QR}$ it is the Gauss sum. Simultaneously diagonal $M_u$, $M_d$ give $V$ a permutation. (b) $2n\equiv n\pmod7$ only for $n=0$; $\langle k\vert\tau_0\rangle=7^{-1/2}$ for all $k$. (c) A vector orthogonal to the common plane is annihilated by $M_u^\dagger$ and $M_d^\dagger$, so it is a left null vector of both, and the corresponding row and column of $V$ are a unit vector. (d) In the bases $\{a,Q_a\}$, $\{b,Q_b\}$ adapted to $A=ab^\dagger$ the light $2\times2$ block after removing the heavy state is $x\tilde B-x^2 C+O(x^3)$ with $C$ of rank one; $\det(\tilde B-xC)=\det\tilde B-x\,\mathrm{tr}(\mathrm{adj}\tilde B\,C)$ is exactly linear in $x$, and $m_1m_2m_3=\lvert\det M\rvert$. The inequalities are the triangle inequality for $\lvert\rho-\kappa\xi_f\rvert$. (e) Diagonalisation and integration of the one-loop equations for the full Yukawa matrices. $\blacksquare$

Witnesses in `check_core_numbers.py`: `test_tick_commuting_clock_structures_are_generation_diagonal`, `test_the_automorphism_fixed_instant_is_the_democratic_rank_one_matrix`, `test_flavour_matrices_in_a_common_plane_give_a_unit_ckm_entry`, `test_two_channels_with_a_rank_one_channel_cannot_fit_quarks_and_leptons` (the formula of (d) is checked on random $A$, $B$), `test_parameter_free_clock_pairs_miss_the_up_quark_ratios`, `test_fritzsch_six_zero_texture_overshoots_vcb`, `test_ckm_phase_does_not_run_in_the_sm`.

**What this changes.** No structure the clock carries predicts a mass ratio or a mixing angle. The tick-invariant ones — which include everything built from the Fano plane, the quadratic residues and the anchor — cannot break the family $\mathbb{Z}_3$ in a way that mixes, and most of them cannot split the masses. The one that breaks translations and keeps the family, the fixed instant $\tau_0$, gives the right leading pattern (one heavy generation per sector) but, used as one of two channels, is excluded by the lepton masses. A flavour prediction would need a principle that fixes the coefficients of at least three channels, and the corpus has none [Pr]. (GC) keeps its two consequences — three generations, no fourth sequential one — and gains no third.

---

## Connection with Other Sections

- **Three generations:** Uniqueness of the triplet $(1,2,4)$ → [Three fermion generations](./fermion-generations.md)
- **Mass hierarchy:** Yukawa couplings generating the texture → [Yukawa mass hierarchy](./yukawa-hierarchy.md)
- **Higgs sector:** Electroweak breaking mechanism → [Higgs sector](./higgs-sector.md)

---

**Related documents:**
- [Fano selection rules](/docs/physics/gauge-symmetry/fano-selection-rules)
- [Yukawa hierarchy](/docs/physics/particle-physics/yukawa-hierarchy)
- [Neutrino masses](/docs/physics/particle-physics/neutrino-masses)
- [Fermion generations](/docs/physics/particle-physics/fermion-generations)
