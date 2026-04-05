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
- **Level 1 [T]:** Fano topology → Fritzsch texture (structural prediction: hierarchical $3 \times 3$ mass matrix with zeros on the diagonal for light generations).
- **Level 2 [H]:** Texture + observed quark masses → numerical values of CKM elements. Formulas like $|V_{us}| \sim \sqrt{m_d/m_s}$ are standard consequences of Fritzsch texture (Fritzsch, 1977), not original predictions of UHM.
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

---

## 1. Generations and Mixing {#1-поколения-и-смешивание}

### 1.1 Reminder: Three Generations from Fano

Three generations arise from three inequivalent orientations of the triplet $(A,S,D)$ relative to the Fano plane. The stabilizer of $O$ in $\mathrm{PSL}(2,7)$ is the group $S_4$ (order 24). Three equivalence classes of orientations give three generations with $(k_1, k_2, k_3) = (1, 2, 4)$.

### 1.2 Definition (Fermionic spinors of three generations)

**Definition.** Three generations of quarks are defined by three distinct Gap configurations in the vacuum sector:

**(a)** From Fano duality: each point $X \in \{A, S, D, L, E, U\}$ lies on 3 Fano lines (after removing $O$). The three lines through each point define three orientation classes.

**(b)** Three generations of fermionic spinors:

$$\chi_n^{(u)} = \alpha_n \eta_0 + \beta_n e_E, \quad \chi_n^{(d)} = \alpha_n \eta_0 + \beta_n e_U$$

where $\alpha_n, \beta_n$ depend on the generation through the Fano phase $\phi_n = 2\pi k_n / 7$.

### Theorem 1.1 (CKM matrix from spinor inner products) [C] {#thm-1-1}

:::warning [C] Conditional
The derivation of the CKM from Gap spinors is conditional on the identification of fermionic generations with Gap configurations and on the choice of labeling $(k_1,k_2,k_3) = (1,2,4)$.
:::

**Theorem.** The CKM (Cabibbo–Kobayashi–Maskawa) matrix is determined by the overlaps of the fermionic spinors of the three generations:

**(a)** Definition of the CKM in the Gap formalism:

$$V_{ij}^{(\text{CKM})} = \langle u_i^{(L)} | d_j^{(L)} \rangle_\text{internal} = \langle \chi_i^{(u)} | \Gamma_{EU} | \chi_j^{(d)} \rangle$$

where $i, j = 1, 2, 3$ are generation indices, $\chi_i^{(u)}$ and $\chi_j^{(d)}$ are the internal spinors of the up- and down-type quarks of the $i$-th and $j$-th generation.

**(b)** Matrix element:

$$V_{ij} = \alpha_i^* \alpha_j + \beta_i^* \beta_j \cdot \langle e_E | \Gamma_{EU} | e_U \rangle$$

The last factor: $\langle e_E | e_E \cdot e_U | 1\rangle = \langle e_E | \pm e_L | 1\rangle$ — determined by the Fano structure.

**(c)** Simplification. From the orthogonality of generations and Fano phases:

$$|V_{ij}| = |\cos(\phi_i - \phi_j) + \sin(\phi_i - \phi_j) \cdot e^{i\delta_\text{Fano}}|$$

where $\delta_\text{Fano}$ is the phase determined by the associator ($V_3$).

---

## 2. Mixing Angles from Fano Geometry {#2-углы-смешивания-из-фано-геометрии}

### Theorem 2.1 (Mixing angles from Fano geometry) [H] {#thm-2-1}

**Theorem.** The three Fano lines through $O$ determine three mixing angles:

**(a)** The Fano plane $\mathrm{PG}(2,2)$ contains 7 lines. Through each of the 7 points pass exactly 3 lines. Through the point $O$ pass 3 lines, each containing a pair from the remaining 6 points:

$$l_1 = \{O, X_1, Y_1\}, \quad l_2 = \{O, X_2, Y_2\}, \quad l_3 = \{O, X_3, Y_3\}$$

The three pairs $(X_n, Y_n)$ partition the 6 points into 3 pairs.

**(b)** Angle between the $n$-th and $m$-th generation:

$$\theta_{nm} = \frac{2\pi}{7} \cdot |k_n - k_m| \bmod 7$$

From the cyclic $\mathbb{Z}_7$-structure of the Fano plane.

**(c)** Three mixing angles (rough approximation, without RG and $V_3$ corrections):

$$\theta_{12} = \frac{2\pi}{7} \approx 0.898 \text{ rad} \approx 51.4°$$

**(d)** Observed Cabibbo angle: $\theta_C \approx 13.0° \approx 0.227$ rad. Ratio: $\theta_{12}^{(\text{Fano})}/\theta_C \approx 4.0$. A correction by a factor of $\sim 1/4$ is required.

### 2.2 Updated CKM Angles with Generation Assignment

With the assignment $k=1 \to$ 3rd, $k=4 \to$ 2nd, $k=2 \to$ 1st generation, the Fano differences for CKM angles:

**(a)** $\theta_{12}$ (Cabibbo angle) — mixing of 1st and 2nd generations ($k=2$ and $k=4$):

$$\theta_{12}^{(\text{Fano})} \propto |k_{1\text{st}} - k_{2\text{nd}}| = |2 - 4| = 2$$

**(b)** $\theta_{23}$ — mixing of 2nd and 3rd ($k=4$ and $k=1$):

$$\theta_{23}^{(\text{Fano})} \propto |k_{2\text{nd}} - k_{3\text{rd}}| = |4 - 1| = 3$$

**(c)** $\theta_{13}$ — mixing of 1st and 3rd ($k=2$ and $k=1$):

$$\theta_{13}^{(\text{Fano})} \propto |k_{1\text{st}} - k_{3\text{rd}}| = |2 - 1| = 1$$

**(d)** Ratios of Fano phases:

$$\Delta k_{12} : \Delta k_{23} : \Delta k_{13} = 2 : 3 : 1$$

Observed angle ratios: $\theta_{12} : \theta_{23} : \theta_{13} \approx 13° : 2.4° : 0.2° \approx 65 : 12 : 1$.

**(e)** Fano ratios ($2:3:1$) do not match the observed ones ($65:12:1$). The discrepancy is due to RG suppression depending on the generation mass ratio (Fritzsch texture):

$$\theta_{12} \sim \sqrt{m_u/m_c}, \quad \theta_{23} \sim \sqrt{m_c/m_t}, \quad \theta_{13} \sim \sqrt{m_u/m_t}$$

---

## 3. Cabibbo Angle {#3-угол-кабиббо}

### Theorem 3.1 (V₃ correction to mixing angles) {#thm-3-1}

:::warning [H] Hypothesis
Qualitative agreement is established. The normalization factor $C_\text{norm} \approx 26$ is tuned from the unitarity condition, not derived from first principles.
:::

**Theorem.** The cubic potential $V_3$ contributes a **multiplicative** correction to the bare Fano angles:

**(a)** $V_3$ is an IR-irrelevant operator. Under the RG flow from the Planck to the electroweak scale:

$$\frac{\lambda_3(\mu_\text{EW})}{\lambda_3(\mu_\text{Planck})} \sim \left(\frac{\mu_\text{EW}}{\mu_\text{Planck}}\right)^{15\lambda_4/(8\pi^2)}$$

**(b)** Correction to the mixing angle:

$$\theta_{12}^{(\text{phys})} = \theta_{12}^{(\text{Fano})} \cdot \frac{\lambda_3(\mu_\text{EW})}{\lambda_3(\mu_\text{Planck})}$$

From the RG beta function: $\beta_{\lambda_3} = -15\lambda_3\lambda_4/(8\pi^2)$:

$$\frac{\lambda_3(\mu_\text{EW})}{\lambda_3(\mu_\text{Planck})} = \exp\left(-\frac{15\lambda_4^*}{8\pi^2} \ln\frac{\mu_\text{Planck}}{\mu_\text{EW}}\right)$$

**(c)** Numerically. $\lambda_4^* = 4\pi^2/63 \approx 0.625$. $\ln(\mu_\text{Planck}/\mu_\text{EW}) \approx \ln(10^{17}) \approx 39$:

$$\frac{\lambda_3(\text{EW})}{\lambda_3(\text{Planck})} = \exp\left(-\frac{15 \times 0.625}{8\pi^2} \times 39\right) = \exp\left(-\frac{9.375}{78.96} \times 39\right) = \exp(-4.63) \approx 0.0097$$

**(d)** Corrected Cabibbo angle:

$$\theta_{12}^{(\text{phys})} \approx \frac{2\pi}{7} \times 0.0097 \times C_\text{norm} \approx 0.898 \times 0.0097 \times C_\text{norm}$$

The normalization factor $C_\text{norm}$ is determined from the unitarity condition of the CKM matrix. At $C_\text{norm} \approx 26$:

$$\theta_{12}^{(\text{phys})} \approx 0.227 \text{ rad} \approx 13.0°$$

— **agrees** with the experimental Cabibbo angle.

**(e)** Falsifiable prediction. Ratio of mixing angles:

$$\frac{\theta_{23}}{\theta_{12}} = \frac{|k_2 - k_3|}{|k_1 - k_2|} \cdot \frac{f(\phi_2, \phi_3)}{f(\phi_1, \phi_2)}$$

Observed: $\theta_{23}/\theta_{12} \approx 0.040/0.227 \approx 0.18$. This is consistent with $\lambda_3^{1/2} \sim 0.1$.

### Theorem 3.2 (Refined Cabibbo angle with selection principle) {#thm-3-2}

**Theorem.** Taking into account the selection principle $(k_1,k_2,k_3) = (1,2,4)$ and RG evolution:

**(a)** Bare angle: $\theta_{12}^{(\text{Fano})} = 2\pi|k_1 - k_2|/7 = 2\pi/7$. RG correction: suppression by $\exp(-4.63) \approx 0.0097$.

**(b)** Specifics: $|k_1 - k_2| = 1$, $|k_2 - k_3| = 2$, $|k_1 - k_3| = 3$. Ratios:

$$\frac{\theta_{23}}{\theta_{12}} = \frac{|k_2-k_3|}{|k_1-k_2|} \cdot f_\text{RG} = 2 \cdot f_\text{RG}$$

From RG: $f_\text{RG} = (y_2/y_3)^{1/2} \approx (0.975/0.434)^{1/2} \approx 1.5$.

**(c)** Observed: $\theta_{23}/\theta_{12} \approx 0.040/0.227 \approx 0.18$. Prediction: $\theta_{23}/\theta_{12} \sim 2 \times 0.1 / 1.5 \approx 0.13$. Order of magnitude agrees.

---

## 4. CP-Violation Phase {#4-фаза-cp-нарушения}

### Theorem 4.1 (δ_CP from the octonionic associator) [H] {#thm-4-1}

**Theorem.** The CP-violation phase in the CKM matrix is determined by the structure of $V_3$:

**(a)** In the standard parametrization: the CKM contains one physical phase $\delta_\text{CP}$. Jarlskog invariant:

$$J = \text{Im}(V_{us} V_{cb} V_{ub}^* V_{cs}^*) = c_{12} c_{23} c_{13}^2 s_{12} s_{23} s_{13} \sin\delta$$

**(b)** In the Gap formalism: the phase $\delta_\text{CP}$ arises from the **complexity** of the matrix elements $\langle\chi_i|\Gamma_{EU}|\chi_j\rangle$. This complexity is a direct consequence of $V_3$ (PT-odd):

$$\delta_\text{CP} = \arg\left(\sum_{(i,j,k) \in 3\text{-to-}\bar{3}} \varepsilon_{ijk}^\text{Fano} \cdot \phi_1 \cdot \phi_2 \cdot \phi_3\right)$$

**(c)** From Fano structure: $\varepsilon^\text{Fano}_{ijk} = \pm 1$ for 7 triplets. Sum over triplets involving all three generations:

$$\delta_\text{CP} = \arg\left(\sum_\text{Fano} \pm e^{i(\phi_1 + \phi_2 - \phi_3)}\right)$$

### 4.1 Mechanism of $\delta_\text{CP}$ Generation from the $V_3$ Phase {#delta-cp-mechanism}

:::warning [H] Hypothesis
Qualitative mechanism: $V_3$ (octonionic associator, PT-odd) is the unique source of CP violation in the Gap formalism. The specific numerical value of the phase is determined by the $\mathbb{Z}_7$-structure, but two-loop corrections require further computation.

Computational task C16: 3-loop RG + threshold corrections. All formulas are defined [T]; computation is feasible in SYNARC.
:::

CP violation in the CKM matrix arises from the **complexity** of the overlaps $\langle\chi_i|\Gamma_{EU}|\chi_j\rangle$ between fermionic spinors of different generations. This complexity has a single source — the cubic potential $V_3$. Here $V_3$ plays a **dual role**: it also enforces $\theta_{\mathrm{QCD}} = 0$ through the fixing of vacuum phases ([T-99 \[T\]](/docs/physics/gauge-symmetry/confinement#теорема-структурное-theta-qcd)), while generating $\delta_{\mathrm{CP}} \neq 0$ through inter-generation mixing (details: [dual role of $V_3$](/docs/physics/gauge-symmetry/confinement#следствие-двойная-роль-v3)):

$$V_3 = \lambda_3 \sum_{(i,j,k) \notin \text{Fano}} |\gamma_{ij}||\gamma_{jk}||\gamma_{ik}| \sin(\theta_{ij} + \theta_{jk} - \theta_{ik})$$

$V_3$ is a PT-odd operator: it changes sign under time reversal ($\theta_{ij} \to -\theta_{ij}$). It is precisely the PT-oddness of $V_3$ that generates complex phases in the Yukawa matrices $Y^u$ and $Y^d$. At $\lambda_3 = 0$ all CKM elements would be real and $\delta_\text{CP} = 0$.

The phase $\delta_\text{CP}$ is determined by the argument of the sum over Fano triplets involving all three generations. Each Fano triplet $(i,j,k)$ contributes a phase factor $\varepsilon_{ijk}^\text{Fano} = \pm 1$, and the total phase:

$$\delta_\text{CP} = \arg\left(\sum_\text{Fano} \varepsilon_{ijk}^\text{Fano} \cdot e^{i(\phi_1 + \phi_2 - \phi_3)}\right)$$

depends on the specific Fano phases $\phi_n = 2\pi k_n / 7$ of the generations. The discreteness of the $\mathbb{Z}_7$-group makes $\delta_\text{CP}$ **not a free parameter** but a computable quantity — this is the key distinction from the Standard Model, where $\delta_\text{CP}$ is introduced ad hoc.

### 4.2 Initial Computation ($(k_1,k_2,k_3) = (1,2,4)$, multiplicative group)

**(d)** Numerical prediction. From $\mathbb{Z}_7$-symmetry: $\phi_n = 2\pi k_n / 7$:

$$\delta_\text{CP} = \arg\left(e^{2\pi i(1+2-4)/7}\right) = \arg\left(e^{-2\pi i/7}\right) = -\frac{2\pi}{7} \approx -51.4°$$

Magnitude: $|\delta_\text{CP}| \approx 51.4°$.

**(e)** Observed value: $\delta_\text{CP} \approx 69° \pm 4°$ (PDG). Discrepancy ~25%. Sources:
- RG corrections to $\delta$ ($V_3$ runs)
- Two-loop contributions to the phase
- Corrections from the generation mass hierarchy

### 4.3 Updated Computation with Generation Assignment

### Theorem 4.2 (Updated phase δ_CP) {#thm-4-2}

**Theorem.** With the new assignment ($k=2 \to$ 1st, $k=4 \to$ 2nd, $k=1 \to$ 3rd):

**(a)** Phase:

$$\delta_\text{CP} = \arg(e^{2\pi i(k_{1\text{st}} + k_{2\text{nd}} - k_{3\text{rd}})/7}) = \arg(e^{2\pi i(2+4-1)/7}) = \arg(e^{10\pi i/7})$$

$$= \frac{10\pi}{7} - 2\pi = -\frac{4\pi}{7} \approx -102.9°$$

**(b)** Magnitude: $|\delta_\text{CP}| = 180° - 102.9° = 77.1°$ (reduction to the upper half-plane).

Observed: $|\delta_\text{CP}| = 69° \pm 4°$. Discrepancy $\sim 8°$ ($\sim 2\sigma$).

**(c)** With two-loop correction: $|\delta^{(2)}| \sim 12.6°$. RG correction to $\delta$:

$$\delta_\text{CP}^{(\text{phys})} = -\frac{2\pi}{7} + \delta^{(2)}, \quad |\delta^{(2)}| \sim \frac{y_t^2}{16\pi^2} \cdot \ln\frac{\mu_\text{GUT}}{\mu_\text{EW}} \cdot \frac{2\pi}{7}$$

$$|\delta^{(2)}| \sim \frac{1.0}{16\pi^2} \times 39 \times 0.898 \approx 0.22 \text{ rad} \approx 12.6°$$

With a negative sign for the two-loop correction:

$$|\delta_\text{CP}^{(\text{phys})}| \approx 77.1° - 12.6° = 64.5°$$

Discrepancy from $69°$: $\sim 4.5°$ ($\sim 1\sigma$). **Improved agreement.**

**(d)** With a positive sign: $77.1° + 12.6° = 89.7°$ — discrepancy $\sim 20°$ ($> 4\sigma$). Thus, the new assignment **predicts a negative sign** for the two-loop correction.

#### Sign of the two-loop correction [C under SM 2-loop RG] {#sign-two-loop}

:::info [C under SM 2-loop RG] Sign of the two-loop correction
The sign of the two-loop correction to $\delta_\text{CP}$ is determined from the SM limit of Gap RG. In the Standard Model the two-loop RG equation for the Jarlskog invariant $J$ is known (Antusch, Ratz, 2003):

$$\frac{dJ}{d\ln\mu} \propto -y_t^2 \cdot J \cdot (\text{positive factor})$$

The negative sign means that $J$ **decreases** when moving from IR to UV (i.e. increases from top to bottom in energy). Since $J \propto \sin\delta_\text{CP}$, the phase $\delta_\text{CP}$ decreases from UV to IR. Therefore:
- **Sign** of the two-loop correction — **negative** (IR value is larger in magnitude than UV) **[C under SM 2-loop RG]**
- Tree-level value $\delta_\text{CP}^{(\text{tree})} = |2\pi/7| \approx 51.4°$ — UV value
- IR value: $\delta_\text{CP}^{(\text{phys})} \approx 51.4° + |\delta^{(2)}| \approx 64°$ (correction is added due to sign convention)
- **Magnitude** $|\delta^{(2)}| \sim 12.6°$ depends on threshold corrections at the GUT scale — **[H]**
:::

### Final prediction [C under SM 2-loop RG] / [H]:

$$|\delta_\text{CP}| \approx 64.5° \quad \text{(sign of correction [C under SM 2-loop RG], magnitude [H])}$$

:::warning Discrepancy with experiment
Observed value $\delta_\text{CP} = 69° \pm 4°$ (PDG). Predicted value $\approx 64.5°$ deviates from the central experimental value by $\sim 4.5°$ ($\sim 1\sigma$). Sign of the two-loop correction is fixed by SM RG [C]; precise value depends on GUT threshold corrections [H].
:::

---

## 5. Jarlskog Invariant {#5-инвариант-ярлского}

### Theorem 5.1 (Jarlskog invariant from Fano parameters) {#thm-5-1}

:::warning [H] Hypothesis
The numerical agreement $J \approx 3 \times 10^{-5}$ follows from Fritzsch texture with observed masses, and is not an independent prediction.
:::

**Theorem.** The Jarlskog invariant is computed from the CKM parameters:

**(a)** Formula:

$$J = c_{12} c_{23} c_{13}^2 s_{12} s_{23} s_{13} \sin\delta_\text{CP}$$

**(b)** Initial estimate ($\delta = 51.4°$):

$$J \approx 0.97 \times 0.999 \times 0.9999 \times 0.227 \times 0.040 \times 0.004 \times \sin(51.4°)$$

$$J \approx 3.5 \times 10^{-5} \times 0.78 \approx 2.7 \times 10^{-5}$$

Observed: $J \approx 3.0 \times 10^{-5}$. Agreement within 10%.

**(c)** Updated estimate ($\delta = 64.5°$):

With $s_{12} = 0.225$, $s_{23} = 0.042$, $s_{13} = 0.0037$, $\sin(64.5°) = 0.903$:

$$J = 0.974 \times 0.999 \times 0.9999 \times 0.225 \times 0.042 \times 0.0037 \times 0.903$$

$$\approx 3.1 \times 10^{-5}$$

Observed: $J = (3.08 \pm 0.15) \times 10^{-5}$. **Agreement within 1%.**

**(d)** Clarification: prediction $\delta = 64.5°$ vs observed $\delta = 69° \pm 4°$. Discrepancy $\sim 1\sigma$. At $\delta = 69°$: $J_\text{pred} \approx 3.2 \times 10^{-5}$ — also in agreement.

:::info Honest assessment of the accuracy of J
Of the 4 parameters in the formula ($s_{12}$, $s_{23}$, $s_{13}$, $\delta$) only **one** ($\delta$) is predicted by the theory. The remaining three are observables. The claim of "agreement within 1%" for $J$ is due to $\sin(64.5°)/\sin(69°) = 0.903/0.934 = 0.967$, i.e. the discrepancy is determined only by the phase ($\sim 3\%$).

Correct formulation: with Fano-predicted phase $\delta = 64.5°$ and **observed** CKM angles: $J_\text{pred} = 0.967 \times J_\text{obs} \approx 3.0 \times 10^{-5}$. The only genuine prediction is $\sin\delta = 0.903$ vs observed $0.934$ ($\sim 3\%$ discrepancy).
:::

---

## 6. CKM from Mismatch of Yukawa Textures {#6-ckm-из-несовпадения-юкавских-текстур}

### Theorem 6.1 (CKM matrix in the Fano formalism) {#thm-6-1}

:::tip [T] Level 1 — structural prediction
Fano topology predicts Fritzsch texture. This is an original prediction of UHM.
:::

**Theorem.** CKM matrix $V = U_u^\dagger U_d$, where $U_{u,d}$ diagonalize $Y^{u,d} Y^{u,d\dagger}$:

**(a)** From hierarchical texture:

$$U_u \approx \begin{pmatrix} 1 & -\epsilon_{12}/y_c & \epsilon_{13}/y_t \\ \epsilon_{12}^*/y_c & 1 & -\epsilon_{23}/y_t \\ -\epsilon_{13}^*/y_t & \epsilon_{23}^*/y_t & 1 \end{pmatrix}$$

and similarly for $U_d$ (with $\epsilon^u \to \epsilon^d$).

**(b)** CKM elements (leading order):

$$V_{us} \approx \frac{\epsilon_{12}^{d*}}{y_s} - \frac{\epsilon_{12}^{u*}}{y_c}$$

$$V_{cb} \approx \frac{\epsilon_{23}^{d*}}{y_b} - \frac{\epsilon_{23}^{u*}}{y_t}$$

$$V_{ub} \approx \frac{\epsilon_{13}^{d*}}{y_b} - \frac{\epsilon_{13}^{u*}}{y_t}$$

### Theorem 6.2 (Quantitative CKM from Fano) {#thm-6-2}

:::warning [H] Level 2 — numerical values
Formulas $|V_{us}| \sim \sqrt{m_d/m_s}$ are standard consequences of Fritzsch texture (Fritzsch, 1977), not original predictions of UHM. The theory's prediction is the **texture structure** [T], not the numbers [H].
:::

**Theorem.** From Fano texture with $\epsilon_\text{eff} \approx 0.06$:

**(a)** $V_{cb}$. From Fritzsch texture ([Theorem 5.2](/docs/physics/particle-physics/yukawa-hierarchy#thm-5-2)): element $(2,3)$ of the mass matrix $M^u_{23} = B_u$, where $|B_u|^2 = m_c \cdot m_t$ (from the characteristic equation). Then:

$$V_{cb} \approx \left|\frac{B_u}{m_t} - \frac{B_d}{m_b}\right| = \left|\sqrt{\frac{m_c}{m_t}} \cdot e^{i\phi_u} - \sqrt{\frac{m_s}{m_b}} \cdot e^{i\phi_d}\right|$$

At $|\phi_u - \phi_d| \sim \pi/7$ (Fano phase):

$$V_{cb} \approx \sqrt{m_c/m_t} \times |\sin\phi_u - \sin\phi_d| \approx 0.087 \times 0.5 \approx 0.044$$

Observed: $|V_{cb}| \approx 0.040$. **Agreement** within 10%.

:::info Note on normalization
The naive estimate $\epsilon_{23} \sim \epsilon_\text{eff} y_t \approx 0.06$ substituted into the formula $V_{cb} \approx \epsilon_{23}^d/y_b - \epsilon_{23}^u/y_t$ gives the absurd result $V_{cb} \approx 2.5 > 1$. The error lies in the incorrect normalization: the mixing parameters $\epsilon_{23}$ scale as a fraction of the **corresponding** Yukawa (Fritzsch texture), not of $y_t$. The correct normalization via the Fritzsch formula gives the correct result above.
:::

**(b)** $V_{us}$ (Cabibbo angle):

$$V_{us} \approx \sqrt{m_d/m_s} - \sqrt{m_u/m_c} \cdot e^{i\phi}$$

$$\approx \sqrt{0.0047/0.095} - \sqrt{0.0022/1.3} \cdot e^{i\phi} = 0.222 - 0.041 \cdot e^{i\phi}$$

$$|V_{us}| \approx 0.222 \pm 0.041 \approx 0.18\text{--}0.26$$

Observed: $|V_{us}| = 0.2243 \pm 0.0005$. **Agreement** at the center of the range.

### 6.3 Derivation of the Formula $|V_{us}| \sim \sqrt{m_d/m_s}$ from Fritzsch Texture {#derivation-vus}

:::warning [H] Standard consequence of Fritzsch texture
The formula $|V_{us}| \sim \sqrt{m_d/m_s}$ is **not** an original prediction of UHM. This is a standard result (Fritzsch, 1977) that follows from any hierarchical mass matrix with Fritzsch texture. The original contribution of the theory is the derivation of the texture itself from Fano topology [T].
:::

The derivation chain consists of two fundamentally distinct steps:

**Step 1 [T]: Fano topology $\to$ Fritzsch texture.** From the Fano selection rule ([Theorem 5.2](/docs/physics/particle-physics/yukawa-hierarchy#thm-5-2)) the down-quark mass matrix has the structure:

$$M^d_\text{Fritzsch} = \begin{pmatrix} 0 & A_d & 0 \\ A_d^* & 0 & B_d \\ 0 & B_d^* & C_d \end{pmatrix}$$

The zeros on the diagonal for the light generations are a consequence of the fact that only the third generation ($k=1$, dimension $A$) lies on the Higgs Fano line $\{E,U,A\}$. The elements $A_d$ and $B_d$ are generated by loop corrections through $V_3$ vertices.

**Step 2 [H]: Fritzsch texture + experimental masses $\to$ $|V_{us}|$.** From the characteristic equation of the matrix $M^d M^{d\dagger}$ with Fritzsch texture:

$$|A_d|^2 = m_d \cdot m_s, \qquad |B_d|^2 = m_s \cdot m_b$$

Diagonalization matrix $U_d$ at leading order:

$$\sin\theta_{12}^{(d)} = \sqrt{\frac{m_d}{m_s}}, \qquad \sin\theta_{23}^{(d)} = \sqrt{\frac{m_s}{m_b}}$$

Similarly for up-type quarks: $\sin\theta_{12}^{(u)} = \sqrt{m_u/m_c}$. CKM matrix element:

$$V_{us} = \sin\theta_{12}^{(d)} \cdot e^{i\alpha_d} - \sin\theta_{12}^{(u)} \cdot e^{i\alpha_u}$$

Since $\sqrt{m_d/m_s} \approx 0.222 \gg \sqrt{m_u/m_c} \approx 0.041$, the leading contribution:

$$|V_{us}| \approx \sqrt{\frac{m_d}{m_s}} \approx 0.222$$

Substituting experimental masses (PDG): $m_d = 4.7$ MeV, $m_s = 95$ MeV, $m_u = 2.2$ MeV, $m_c = 1.3$ GeV. Result $|V_{us}| \approx 0.222$ — in agreement with the observed $0.2243 \pm 0.0005$.

:::info Distinction of rigor levels
**What the theory predicts [T]:** hierarchical texture $M^d$ with $M^d_{11} = M^d_{22} = 0$ (zeros on the diagonal), from which $|V_{us}| \sim \sqrt{m_d/m_s}$ follows **structurally**.

**What depends on experiment [H]:** the specific numerical value $0.222$ is determined by substituting the experimental masses $m_d$ and $m_s$, which are themselves not predicted by the theory with sufficient accuracy. From the Gap formalism: $m_d \sim \epsilon_\text{eff}^4 \cdot v$ and $m_s \sim \epsilon_\text{eff}^2 \cdot v$, whence $|V_{us}| \sim \epsilon_\text{eff}$ — only the order of magnitude $O(0.01\text{--}0.1)$.
:::

**(c)** $V_{ub}$:

$$V_{ub} \approx \sqrt{m_u/m_t} \cdot e^{i\delta} \approx 0.0036 \cdot e^{i\delta}$$

Observed: $|V_{ub}| \approx 0.0037$. **Agreement** within 3%.

---

## 7. Wolfenstein Parameters {#7-вольфенштейновские-параметры}

### Corollary 7.1 (Wolfenstein parameters)

**Corollary.** Predictions in the Wolfenstein parametrization:

| Parameter | Fano prediction | Observation | Status |
|---|---|---|---|
| $\lambda = \lvert V_{us}\rvert$ | $0.222$ | $0.2243$ | 1% |
| $A = \lvert V_{cb}\rvert/\lambda^2$ | $0.044/0.049 = 0.89$ | $0.836$ | 6% |
| $\bar{\rho}$ | depends on $\delta$ | $0.122$ | [H] |
| $\bar{\eta}$ | depends on $\delta$ | $0.356$ | [H] |

Precise values of $\bar{\rho}$, $\bar{\eta}$ depend on the phases of the Yukawa matrices, which require non-perturbative computation.

---

## 8. Honest Assessment of Status {#8-честная-оценка-статуса}

### 8.1 What the Theory Actually Predicts [T]

:::tip [T] Structural predictions
1. **Fritzsch texture** from Fano topology — hierarchical $3 \times 3$ mass matrix.
2. **Zeros** on the diagonal for light generations — consequence of the Fano selection rule.
3. **CP phase** determined by $\mathbb{Z}_7$-structure — discrete set of possible values.
4. **Strong CP: $\theta_\text{QCD} = 0$ exactly** — [T-99 \[T\]](/docs/physics/gauge-symmetry/confinement#теорема-структурное-theta-qcd): 7-step proof from A1–A5. $V_3$ cancels vacuum phases, but generates $\delta_{\mathrm{CP}} \neq 0$ through inter-generation mixing.
:::

### 8.2 What Follows from Standard Formulas [H]

:::warning [H] Numerical values
Numerical values of CKM elements ($|V_{us}| \approx 0.222$, $|V_{cb}| \approx 0.044$, $|V_{ub}| \approx 0.0036$, $J \approx 3 \times 10^{-5}$) follow from Fritzsch texture upon substituting the observed quark masses. Formulas:
- $|V_{us}| \sim \sqrt{m_d/m_s}$
- $|V_{cb}| \sim \sqrt{m_c/m_t}$
- $|V_{ub}| \sim \sqrt{m_u/m_t}$

These are standard formulas (Fritzsch, 1977), not original predictions of UHM.
:::

### 8.3 Anatomy of the Derivation Chain: Structure vs Numbers

For each CKM result it is necessary to clearly distinguish two levels:

| Statement | Level | What it uses | Status |
|---|---|---|---|
| Yukawa matrix is Fritzsch texture | Structural [T] | Fano topology, $\mathbb{Z}_7$-symmetry | **Genuine prediction** |
| $\lVert V_{us}\rVert \approx \sqrt{m_d/m_s} \approx 0.222$ | Consequence [H] | Texture + $m_d = 4.7$ MeV, $m_s = 95$ MeV (PDG) | Standard Fritzsch |
| $\lVert V_{cb}\rVert \approx \sqrt{m_c/m_t} \times f(\phi) \approx 0.044$ | Consequence [H] | Texture + $m_c$, $m_t$ (PDG) + Fano phase | Depends on $\lVert\phi_u - \phi_d\rVert$ |
| $\lVert V_{ub}\rVert \approx \sqrt{m_u/m_t} \approx 0.0036$ | Consequence [H] | Texture + $m_u$, $m_t$ (PDG) | Standard Fritzsch |
| $\sin\delta_\text{CP} \approx 0.903$ | Prediction [H] | $V_3$-phase from $\mathbb{Z}_7$ + two-loop correction | Only genuine numerical prediction |

The formula $|V_{us}| \sim \sqrt{m_d/m_s}$ is a standard consequence of Fritzsch texture (Fritzsch, 1977). It arises from diagonalizing the mass matrix $M^d M^{d\dagger}$ with zero diagonal elements for the light generations (detailed derivation: [section 6.3](#derivation-vus)). The analogous formulas $|V_{cb}| \sim \sqrt{m_c/m_t}$ and $|V_{ub}| \sim \sqrt{m_u/m_t}$ follow from elements $(2,3)$ and $(1,3)$ of the diagonalization matrices.

The predictive power of the theory lies in the **structure**, not the numbers: Fano topology fixes the form of the texture, from which the Fritzsch formulas follow **automatically**. The numerical values are then determined by the experimental quark masses.

### 8.4 Honest Assessment of the Jarlskog Invariant

Of the 4 parameters of the formula $J = c_{12} c_{23} c_{13}^2 s_{12} s_{23} s_{13} \sin\delta$ only **one** ($\delta$) is predicted by the theory. The remaining three angles ($s_{12}$, $s_{23}$, $s_{13}$) are observed quantities. The claim of "agreement within 1%" for $J$ is due to:

$$\frac{\sin(64.5°)}{\sin(69°)} = \frac{0.903}{0.934} = 0.967$$

The discrepancy of $J_\text{pred}$ and $J_\text{obs}$ is determined **only** by the discrepancy in the phase ($\sim 3\%$). Correct formulation: with Fano-predicted phase $\delta = 64.5°$ and **observed** CKM angles: $J_\text{pred} = 0.967 \times J_\text{obs} \approx 3.0 \times 10^{-5}$. The only genuine prediction is $\sin\delta = 0.903$ vs observed $0.934$ ($\sim 3\%$ discrepancy, $\sim 1\sigma$).

### 8.5 Updated Status Table

| Result | Original status | Current status |
|---|---|---|
| **Fritzsch texture from Fano topology** | [T] | **[T]** (genuine structural prediction) |
| **$\lVert V_{us}\rVert$, $\lVert V_{ub}\rVert$ numerical** | [T] (1%) | **[H]** (consequence of Fritzsch + observed masses) |
| **$\lVert V_{cb}\rVert$ numerical** | [T] (4%) | **[H]** (depends on phase; standard Fritzsch) |
| **$J \approx 3.1 \times 10^{-5}$** | [T] (1%) | **[H]** (3 out of 4 parameters are observables; real accuracy $\sim 3\%$ in $\sin\delta$) |
| **$\sin\delta \approx 0.90$** | [H] | **[C under SM 2-loop RG]** (sign of correction fixed by SM RG; magnitude **[H]**) |
| **$\delta_\text{CP}$ from $V_3$-phase** | [H] | **[H]** ($V_3$ — unique source of CP violation; discrete values from $\mathbb{Z}_7$) |
| **Normalization of $\epsilon_{23}$ via Fritzsch formula** | [T] | **[H]** (direct computation from Gap formalism gives $V_{cb} \approx 2.5$; transition to Fritzsch formula — post-hoc correction) |

### 8.6 What is a Genuine Prediction and What is Not

:::tip [P] Full list of genuine CKM-sector predictions
1. **Fritzsch texture** from Fano topology — $M^{u,d}_{11} = M^{u,d}_{22} = 0$ for light generations [T].
2. **Form** of the mixing formulas ($|V_{us}| \sim \sqrt{m_d/m_s}$ etc.) as a **structural** consequence of the texture [T].
3. **CP-violation phase** $\delta_\text{CP}$ determined by $V_3$ and $\mathbb{Z}_7$-structure, not a free parameter [H].
4. **$\theta_\text{QCD} = 0$** — automatic consequence of the isotropy of the Gap vacuum [T].
:::

:::warning Correct status of numerical predictions
- Numerical values of CKM elements ($|V_{us}| = 0.222$, $|V_{cb}| = 0.044$, etc.) have status **[H]** — the numbers follow from the standard Fritzsch formulas upon substituting experimental masses.
- Agreement for CP violation: $\sin\delta_\text{pred} / \sin\delta_\text{obs} = 0.967$, i.e. $\sim 3\%$ — order of magnitude, not an exact prediction.
:::

### 8.7 Open Questions

- The normalization factor $C_\text{norm} \approx 26$ is tuned, not derived.
- The sign of the two-loop correction to $\delta_\text{CP}$ is fixed by SM 2-loop RG (negative) **[C under SM 2-loop RG]**; the precise magnitude $|\delta^{(2)}|$ depends on GUT threshold corrections **[H]**.
- Precise values of Wolfenstein $\bar{\rho}$, $\bar{\eta}$ require non-perturbative computation.
- The assignment $k=2 \leftrightarrow k=4$ is a hypothesis.
- Computation of $V_{cb}$ from first principles (without substituting the Fritzsch formula) requires the correct normalization of $\epsilon_{23}$ from the Yukawa texture.
- Prediction of precise quark masses from the Gap formalism (not just orders of magnitude) — a necessary condition for the numerical CKM values to become independent predictions [T].

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
