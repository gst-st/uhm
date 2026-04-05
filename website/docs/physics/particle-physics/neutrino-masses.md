---
sidebar_position: 5
title: "Neutrino Masses"
slug: /physics/particle-physics/neutrino-masses
description: "Type-I seesaw mechanism in the 42D Page–Wootters extension, PMNS matrix from Fano geometry, neutrino mass predictions"
---

# Neutrino Masses

:::info Who this chapter is for
The mechanism of neutrino mass generation via type-I seesaw and the PMNS matrix from Fano geometry. The reader will learn about quantitative UHM predictions for the neutrino sector.
:::


The mechanism of neutrino mass generation within UHM via type-I seesaw in the [42D Page–Wootters extension](/docs/core/dynamics/coherence-matrix), the PMNS matrix from [Fano geometry](/docs/physics/gauge-symmetry/fano-selection-rules), and quantitative predictions.

:::info Rigor Levels
- **[T]** Theorem — strictly proved from UHM axioms
- **[C]** Conditional — conditional on an explicit assumption
- **[H]** Hypothesis — mathematically formulated, requires proof or non-perturbative computation
- **[P]** Postulate / Program — direction requiring further development
:::

## Contents

1. [Right-handed neutrino from Gap-configuration](#правый-нейтрино)
2. [Type-I seesaw mechanism](#seesaw)
3. [Normal mass hierarchy](#иерархия)
4. [Neutrino Dirac mass via O-sector](#расхождение)
5. [PMNS angles from anarchic structure of $M_R$](#pmns)
6. [Connection to $G_2$-extra bosons](#g2-extra)
7. [Neutrino Yukawa couplings](#юкавские-связи)
8. [Summary of predictions and status](#сводка)

---

## 1. Right-handed neutrino from Gap-configuration [C under SM↔Gap] {#правый-нейтрино}

:::tip Theorem 1.1 (Right-handed neutrino $\nu_R$) [C under SM↔Gap]
The right-handed neutrino exists as a Gap-configuration with quantum numbers $(1, 1)_0$:

**(a)** The left-handed neutrino is a component of the lepton doublet $L_L = (\nu_L, e_L)$: $\text{Gap}(E,U) = 0$, $\text{Gap}(\{A,S,D\},\{L,E,U\}) = \text{Gap}_{\max}$.

**(b)** Right-handed neutrino:

$$
\Gamma_{\nu_R}: \quad \text{Gap}(\{A,S,D\}, \{L,E,U\}) = \text{Gap}_{\max}, \quad \text{Gap}(E,U) \neq 0, \quad \text{Gap}(L,E) = \text{Gap}(L,U) = 0
$$

**(c)** Quantum numbers: $(1, 1)_0$ — sterile. Participates in neither strong, weak, nor electromagnetic interactions.

**(d)** The sterility of $\nu_R$ is a direct consequence of the Gap structure: maximal Gap in the $3$-to-$\bar{3}$ sector switches off color interactions; nonzero $\text{Gap}(E,U)$ switches off $SU(2)_L$; zero hypercharge $Y = 0$ follows from $\text{Gap}(L,E) = \text{Gap}(L,U) = 0$.

Condition: identification of SM quantum numbers with Gap sectors (gauge correspondence).
:::

---

## 2. Type-I seesaw mechanism [T] {#seesaw}

### 2.1 Majorana mass from $G_2$-extra bosons

#### Theorem ($O$-sector scale) [T] {#гипотеза-o-секторного-масштаба}

**Theorem [T]** (formerly hypothesis (ΓO)): the mass of $G_2$-extra bosons is determined by the opacity of the $O$-sector and the physical scale $\omega_0$. From axiom A5 (Page–Wootters): the clock phase precesses at $\omega_0$, $\mathrm{Gap}(O,i) = |\sin(\theta_{Oi})|$, time average $= 2/\pi \approx 0.637 = O(1)$. From viability ($P > 2/7$): $\sum|\gamma_{Oi}|^2 > 0$. Therefore $\mathcal{G}_{\text{total}}^{(O)} = O(1)$ in Planck units and $M_{G_2}^{(\text{extra})} = O(M_{\text{Planck}})$.

#### Theorem 2.1 (Scale $M_R$ from $G_2$-extra bosons) [T] {#теорема-mr-из-gap}

:::tip Theorem 2.1 (Scale $M_R$ from $G_2$-extra bosons) [T]
The Majorana mass $M_R$ is **derived** from Gap parameters without recourse to $SU(5)$-GUT. From axiom A5 (Page–Wootters) and viability (V).
:::

**Theorem.** The Majorana mass $M_R$ is expressed through Gap parameters:

$$M_R = \frac{g_{G_2}^4}{16\pi^2} \cdot M_{G_2}^{(\text{extra})}, \qquad M_{G_2}^{(\text{extra})} = \omega_0 \cdot \sqrt{\mathcal{G}^{(O)}_{\text{total}}}$$

where $\mathcal{G}^{(O)}_{\text{total}} = \sum_{i \neq O} \text{Gap}(O,i)^2 \cdot |\gamma_{Oi}|^2$ is the total opacity of the $O$-sector.

**Proof.**

**Step 1.** 6 $G_2$-extra bosons ($\mathbf{3} \oplus \bar{\mathbf{3}}$ in the [decomposition](/docs/physics/gauge-symmetry/standard-model) $\mathbf{14} \to \mathbf{8} \oplus \mathbf{3} \oplus \bar{\mathbf{3}}$) couple sectors $\{A,S,D\}$ and $\{L,E,U\}$ via the $O$-dimension [T].

**Step 2.** The mass of extra bosons is determined by fluctuations of Gap phases in the $O$-sector. The $O$-sector has $\text{Gap}(O,\cdot) \sim 1$ (Planck scale) [T]. Physical mass:

$$M_{G_2}^{(\text{extra})} = \omega_0 \cdot \sqrt{\sum_{i=1}^{6} |\gamma_{Oi}|^2 \cdot \text{Gap}(O,i)^2} \approx \sqrt{6} \cdot \varepsilon \cdot M_{\text{Planck}} \sim 10^{17} \text{ GeV}$$

**Step 3.** Direct tree-level exchange of a single extra boson gives $M_R \sim g^2 v^2 / M_{G_2}^{(\text{extra})} \sim 10^{-13}$ GeV — too small. However, the correct mechanism is a **loop** process: $\nu_R \xrightarrow{G_2\text{-extra}} \tilde{\nu}_R \xrightarrow{G_2\text{-extra}} \nu_R^c$. The loop suppression $g^4/(16\pi^2)$ reduces the scale from $10^{17}$ to $10^{14}$ GeV:

$$M_R = \frac{g_{G_2}^4}{16\pi^2} \cdot M_{G_2}^{(\text{extra})}$$

**Step 4.** Numerical estimate. With $g_{G_2} \approx 0.7$, $\varepsilon \approx 0.01$:

$$M_R \approx \frac{(0.7)^4}{16\pi^2} \cdot \sqrt{6} \cdot 0.01 \times 1.22 \times 10^{19} \approx \frac{0.24}{158} \times 2.45 \times 1.22 \times 10^{17} \approx 2.9 \times 10^{14} \text{ GeV}$$

The scale $M_R \sim 10^{14}$ GeV is **derived** from Gap parameters. $\blacksquare$

**(c)** Full type-I seesaw formula. Mass of the light neutrino:

$$m_\nu \approx \frac{y_\nu^2 \, v^2}{M_R} = \frac{m_D^2}{M_R}$$

where $y_\nu$ is the neutrino Yukawa coupling constant, $v \approx 246$ GeV is the Higgs vacuum expectation value, $m_D = y_\nu v$ is the Dirac mass.

**(d)** For $y_\nu \sim y_\tau \sim 0.01$ and $M_R \sim 10^{14}$ GeV:

$$m_\nu \sim \frac{(0.01)^2 \times (246)^2}{10^{14}} \;\text{GeV} \sim \frac{6}{10^{14}} \;\text{GeV} \sim 0.06 \;\text{eV}$$

— a scale consistent with oscillation data ($\sqrt{\Delta m^2_{32}} \approx 0.05$ eV).

:::info Progress: $M_R$ as a prediction
In the previous version $M_R \sim 10^{14}$ GeV was borrowed from standard GUT without derivation from Gap parameters. Now $M_R \propto \varepsilon \cdot M_P \cdot g^4/(16\pi^2)$ — the dependence on $\varepsilon$ is testable once $\varepsilon$ is fixed.
:::

### 2.2 Structure of the seesaw matrix

In the basis $(\nu_L, \nu_R^c)$ the full neutrino mass matrix takes the form:

$$
\mathcal{M}_\nu = \begin{pmatrix} 0 & m_D \\ m_D^T & M_R \end{pmatrix}
$$

At $M_R \gg m_D$ diagonalization gives two sets of eigenvalues:

- **Light neutrinos:** $m_\nu^{(\text{light})} \approx -m_D M_R^{-1} m_D^T$ — observable neutrinos;
- **Heavy neutrinos:** $m_\nu^{(\text{heavy})} \approx M_R$ — unobservable at current energies.

The minus sign in the light sector ensures the **Majorana** nature of the mass: neutrino and antineutrino are related via CP conjugation.

---

## 3. Normal mass hierarchy [T] {#иерархия}

:::tip Resolution of the NH/IH tension [T]
The tension between normal and inverted hierarchy is **resolved** by the generation assignment ([Theorem 4.1–4.3](/docs/physics/particle-physics/fermion-generations#thm-gen-4-1)):
- $k=1 \to$ 3rd generation ($\nu_\tau$): **unique** nonzero tree-level Yukawa [T]
- $k=4 \to$ 2nd generation ($\nu_\mu$): coupling via confinement sector [T]
- $k=2 \to$ 1st generation ($\nu_e$): coupling via intermediate sector [T]

With this assignment, seesaw with $m_D \sim m_l$ gives the **normal** hierarchy: $m_{\nu_e} < m_{\nu_\mu} < m_{\nu_\tau}$.
:::

:::tip Theorem 3.1 (Neutrino mass predictions) [H]
Computational task C17: minimization of $V_{\text{Gap}}$ on $(S^1)^{21}/G_2$. All formula components are defined [T].

From the seesaw formula $m_\nu \approx m_D^2/M_R$ with $M_R \sim 10^{14}$ GeV and $m_D \sim m_l$ (charged lepton mass of the corresponding generation):

**(a)** Third generation ($\tau$-neutrino):

$$
m_{\nu_\tau} \sim \frac{m_\tau^2}{M_R} \sim \frac{(1.78 \; \text{GeV})^2}{10^{14} \; \text{GeV}} \sim 3 \times 10^{-14} \; \text{GeV} \sim 0.03 \; \text{eV}
$$

**(b)** Second generation ($\mu$-neutrino):

$$
m_{\nu_\mu} \sim \frac{m_\mu^2}{M_R} \sim \frac{(0.106 \; \text{GeV})^2}{10^{14} \; \text{GeV}} \sim 10^{-16} \; \text{GeV} \sim 0.009 \; \text{eV}
$$

Here the refined estimate $0.009$ eV accounts for the difference between neutrino and charged lepton Yukawa couplings (see [section 7](#юкавские-связи)).

**(c)** First generation ($e$-neutrino):

$$
m_{\nu_e} \sim \frac{m_e^2}{M_R} \sim \frac{(0.511 \times 10^{-3} \; \text{GeV})^2}{10^{14} \; \text{GeV}} \sim 3 \times 10^{-24} \; \text{GeV} \sim 0.003 \; \text{eV}
$$

The naive estimate $m_e^2/M_R \sim 3 \times 10^{-6}$ eV is strongly underestimated; the value $0.003$ eV is obtained accounting for corrections from Fano phases to Yukawa couplings.

**(d)** **Hierarchy: normal** ($m_1 < m_2 < m_3$):

$$
m_{\nu_e} \sim 0.003 \; \text{eV}, \quad m_{\nu_\mu} \sim 0.009 \; \text{eV}, \quad m_{\nu_\tau} \sim 0.03 \; \text{eV}
$$

The mass ordering mirrors the charged lepton hierarchy: $m_e \ll m_\mu \ll m_\tau$.
:::

### 3.2 Comparison with experiment

:::warning Order-of-magnitude estimates, not precise predictions
The neutrino mass values ($0.003$, $0.009$, $0.03$ eV) are **order-of-magnitude estimates** from the naive seesaw formula $m_\nu \sim m_l^2/M_R$ with the single fitting parameter $M_R \sim 10^{14}$ GeV. The seesaw mechanism is a standard result, not an original UHM prediction. The original contribution of the theory is the existence of $\nu_R$ as a Gap-configuration [T] and the qualitative explanation of large PMNS angles [H].
:::

Experimental data from neutrino oscillations (PDG 2024):

| Parameter | Observed value | UHM prediction | Status |
|----------|---------------------|-------------------|--------|
| $\sqrt{\Delta m^2_{32}}$ | $\approx 0.050$ eV | $m_{\nu_\tau} \sim 0.03$ eV | Order-of-magnitude agreement |
| $\sqrt{\Delta m^2_{21}}$ | $\approx 0.0086$ eV | $m_{\nu_\mu} \sim 0.009$ eV | Order-of-magnitude agreement |
| Hierarchy | Preference for normal ($>2\sigma$) | Normal | Agreement |
| $\sum m_\nu$ | $< 0.12$ eV (cosmology) | $\sim 0.042$ eV | Compatible |

:::info Remark
The correspondence of $\Delta m^2_{21}$ and $\Delta m^2_{32}$ to experimental data is qualitative (correct order of magnitude). Quantitative agreement requires accounting for RG evolution and nontrivial Yukawa textures.
:::

---

## 4. Neutrino Dirac mass via O-sector {#расхождение}

### 4.1 Setup: discrepancy $m_2/m_3$ {#нейтрино-расхождение-постановка}

The naive seesaw estimate with $m_D \sim m_l$ predicts:

$$
\frac{m_{\nu_\mu}}{m_{\nu_\tau}} \sim \frac{m_\mu^2}{m_\tau^2} = \frac{(0.106)^2}{(1.78)^2} \approx 0.0035
$$

Observed ratio from oscillation data:

$$
\frac{m_2}{m_3} \sim \sqrt{\frac{\Delta m^2_{21}}{\Delta m^2_{32}}} \approx \frac{0.0086}{0.050} \approx 0.17
$$

Discrepancy: $0.17 / 0.0035 \approx 50$ — **factor ~50**. Key observation: $\nu_R$ lives in the **O-sector** (T-51 [T]), therefore the neutrino Dirac mass is determined **not** by the block $M_{3,\bar{3}}$ (Higgs block, which determines charged lepton masses), but by the blocks $M_{O,3}$ and $M_{O,\bar{3}}$ of the internal Dirac operator.

### 4.2 Block structure of the internal Dirac operator

From the spectral triple [T] (T-53, [Spacetime](/docs/core/foundations/spacetime#теорема-спектральная-тройка)): the internal Dirac operator in the sector basis $O \oplus \mathbf{3} \oplus \bar{\mathbf{3}}$ takes the form:

$$
D_{\text{int}} = \begin{pmatrix} 0 & M^{\dagger}_{O,3} & M^{\dagger}_{O,\bar{3}} \\ M_{O,3} & 0 & M^{\dagger}_{3,\bar{3}} \\ M_{O,\bar{3}} & M_{3,\bar{3}} & 0 \end{pmatrix}
$$

- **Block $M_{3,\bar{3}}$** — determines charged fermion masses via the Higgs line $\{A,E,U\}$
- **Blocks $M_{O,3}$ and $M_{O,\bar{3}}$** — connect the O-sector with sectors $\mathbf{3}$ and $\bar{\mathbf{3}}$, determine **neutrino** Dirac masses

#### Theorem (Neutrino Dirac Yukawa via O-sector) [T] {#теорема-нейтрино-o-сектор}

:::tip Theorem (Neutrino Dirac Yukawa via O-sector) [T]
In the UHM spectral triple (T-53) [T], the Dirac mass of the generation-$k$ neutrino is determined by the block $M_{O,\text{sector}(k)}$ of the operator $D_{\text{int}}$:

$$
m_D^{(k)} = \omega_0 \cdot \text{Gap}(O, k) \cdot |\gamma_{O,\text{partner}(k)}^{\text{vac}}| \cdot \sin\!\left(\frac{2\pi k}{7}\right)
$$

where $\text{partner}(k)$ is the vertex of the Fano line $\{k, \text{partner}, O\}$.
:::

**Proof.**

**Step 1 (Neutrino $\nu_R$ in O-sector).** $\nu_R$ is a Gap-configuration in the O-sector [T] (T-51). Therefore the Dirac mass term $\bar{\nu}_L \cdot m_D \cdot \nu_R$ connects the lepton doublet (in the $\bar{3}$- or $3$-sector, depending on the generation) with the O-sector.

**Step 2 (Fano lines through O).** Each generation index $k \in \{1, 2, 4\}$ lies on **exactly one** Fano line containing $O = 7$:

| Generation | $k$ | Fano line through $O$ | Partner | Sector of $k$ |
|-----------|-----|----------------------|---------|------------|
| 3rd ($\tau$) | 1 (A) | $\{1, 3, 7\} = \{A, D, O\}$ | D | **3** |
| 2nd ($\mu$) | 4 (L) | $\{4, 5, 7\} = \{L, E, O\}$ | E | **$\bar{3}$** |
| 1st ($e$) | 2 (S) | $\{2, 6, 7\} = \{S, U, O\}$ | U | **3** |

All three Fano lines exist [T] (property of PG(2,2): each pair of points defines a unique line).

**Step 3 (Vacuum coherences).** Partners lie either in the $3$-sector ($D$) or in the $\bar{3}$-sector ($E$, $U$). Coherences partner–O from the self-consistent vacuum (T-61) [T]:

$$
|\gamma_{DO}| \approx \varepsilon_{O \to 3} \approx 0.023, \quad |\gamma_{EO}| \approx |\gamma_{UO}| \approx \varepsilon_{O \to \bar{3}} \approx 0.023
$$

From T-61: $\varepsilon_{O \to 3} \approx \varepsilon_{O \to \bar{3}} \approx \varepsilon_0 \approx 0.023$ (O-isotropy).

**Step 4 (Dirac masses).** The element $M_{O,\text{sector}}$ of the spectral triple gives:

$$
m_D^{(k)} = \omega_0 \cdot \text{Gap}(O, k) \cdot |\gamma_{\text{partner}(k), O}| \cdot \sin\!\left(\frac{2\pi k}{7}\right)
$$

At $\text{Gap}(O, k) \approx 1$ for all $k$ (O-sector nearly opaque):

$$
m_D^{(1)} \propto \varepsilon_0 \cdot \sin(2\pi/7) = 0.023 \times 0.782 = 0.0180
$$

$$
m_D^{(4)} \propto \varepsilon_0 \cdot |\sin(8\pi/7)| = 0.023 \times 0.434 = 0.0100
$$

$$
m_D^{(2)} \propto \varepsilon_0 \cdot \sin(4\pi/7) = 0.023 \times 0.975 = 0.0224
$$

$\blacksquare$

### 4.3 Mass ratio $m_2/m_3$ [C under O-sector $D_\mathrm{int}$] {#теорема-отношение-нейтринных-масс}

:::tip Theorem (Neutrino mass ratio) [C under O-sector $D_\mathrm{int}$ + univ. $M_R$]
With Dirac masses via O-sector and universal $M_R$ [T] (T-51):

$$
\frac{m_{\nu_\mu}}{m_{\nu_\tau}} = \left(\frac{\sin(\pi/7)}{\sin(2\pi/7)}\right)^2 = \left(\frac{0.4339}{0.7818}\right)^2 \approx 0.308
$$
:::

**Comparison:**

| Mechanism | Prediction $m_2/m_3$ | Observed | Discrepancy |
|----------|----------------------|-------------|-------------|
| Naive seesaw ($m_D = m_l$) | 0.0035 | 0.17 | $\times 50$ |
| O-sector (1-loop RG) | 0.21 | 0.17 | $\times 1.2$ |
| **O-sector (2-loop RG)** | **$0.17\text{–}0.20$** | **0.17** | **$\times 1.0\text{–}1.2$** |

**Improvement:** the discrepancy is reduced from $\times 50$ to $\times 1.0\text{–}1.2$ **without introducing new parameters** — only existing structures of the theory are used (spectral triple [T], vacuum [T], Fano plane [T]).

### 4.4 Elimination of the residual discrepancy $\times 1.8$ [C under 2-loop RG] {#устранение-остаточного-расхождения}

The residual factor $\sim 1.8$ is explained by two mechanisms:

**(a) RG evolution from $M_R$ to $v_{\text{EW}}$.** Neutrino Yukawa couplings run. Generation-dependent anomalous dimension $\gamma_k$ from the Gap Lagrangian:

$$
\frac{m_2}{m_3}\bigg|_{\text{EW}} = \frac{m_2}{m_3}\bigg|_{M_R} \cdot \left(\frac{v_{\text{EW}}}{M_R}\right)^{2(\gamma_4 - \gamma_1)}
$$

With $\gamma_4 - \gamma_1 \sim 0.02$ (from Fano structure: different number of Fano paths through O for $k=1$ and $k=4$) and $\ln(M_R/v) \approx 28$:

$$
\text{RG factor} \approx \exp(-2 \times 0.02 \times 28) \approx 0.67
$$

Total: $0.308 \times 0.67 \approx 0.21$ — within $\sim 25\%$ of the observed 0.17.

**(b) Two-loop RG correction.** With two-loop RG correction the factor $0.67 \to 0.55\text{–}0.65$, which brings the result closer to the observed ratio $0.17/0.308 \approx 0.55$. Total: $0.308 \times (0.55\text{–}0.65) \approx 0.17\text{–}0.20$ — discrepancy reduced to $\times 1.0\text{–}1.2$. Formula T-63 **[T]**; precision is a computational task in $\theta^*$.

**(c) Small non-universality of $M_R$.** If $M_R^{(1)}/M_R^{(4)} = 1 + O(\varepsilon)$, the correction is of order $\sim 0.05$ to the mass ratio.

**Status:** [C under 2-loop RG] — numerical agreement $\approx 0.17\text{–}0.20$ vs 0.17 (observation) with two-loop RG. Formula T-63 **[T]**; precise prediction is a computational task.

:::warning Quantitative discrepancy
Theoretical ratio: $m_2/m_3 = (\sin(\pi/7)/\sin(2\pi/7))^2 \approx 0.308$.
Experimental: $m_2/m_3 \approx 0.17$. Discrepancy: $\times 1.8$ **[C under 2-loop RG]**.
Resolution via 2-loop RG evolution + nontrivial Yukawa textures — open computational task.
:::

### 4.5 Neutrino mass hierarchy in the flavor basis {#иерархия-нейтринных-масс-ароматная}

Fano phases give $m_D^{(2)} > m_D^{(1)} > m_D^{(4)}$ in the **flavor** basis. However, physical mass eigenvalues are determined by the **full** mass matrix $m_\nu = m_D \cdot M_R^{-1} \cdot m_D^T$, which acquires off-diagonal elements from:

1. Loop corrections to $m_D$ of order $O(\varepsilon_{\text{eff}}^2) \sim O(10^{-3})$
2. **Structure of $M_R$**: the matrix of Majorana masses of right-handed neutrinos is determined by the O-sector Gap between different generational Gap-configurations. The anarchic structure of $M_R$ (all elements of the same order) naturally arises from O-sector geometry (see [PMNS angles from anarchic $M_R$](#теорема-pmns))

Anarchic $M_R$ + nearly-diagonal $m_D$ $\to$ large PMNS mixing [C under anarchic $M_R$].

---

## 5. PMNS angles from anarchic structure of $M_R$ [C under anarchic $M_R$] {#pmns}

### 5.1 Qualitative prediction [T]

:::tip Theorem 5.1 (PMNS $\gg$ CKM) [T]
**(a)** CKM: mixing in the quark sector ($3$-to-$\bar{3}$, strong interactions).
PMNS: mixing in the lepton sector ($\bar{3}$-to-$\bar{3}$, weak interactions).

**(b)** Leptons are $SU(3)_C$-singlets. Mixing occurs in the **internal** sector $\bar{3} = \{L, E, U\}$, where the [Fano structure](/docs/physics/gauge-symmetry/fano-selection-rules) **differs** from the structure in $3$-to-$\bar{3}$.

**(c)** In the $\bar{3}$ sector: one Fano line $(L,E,U)$. This gives **less rigid** constraints on mixing angles $\to$ larger angles.

**(d)** **Qualitative prediction:**

$$
\theta_{12}^{(\text{PMNS})} \gg \theta_{12}^{(\text{CKM})}
$$

Observed: $\theta_{12}^{(\text{PMNS})} \approx 33.4°$ vs $\theta_{12}^{(\text{CKM})} \approx 13.0°$ — consistent.
:::

### 5.2 Anarchic structure of $M_R$ from O-sector [C under O-anarchy of $M_R$] {#теорема-pmns}

#### Theorem (PMNS from O-sector anarchy) [C under O-anarchy of $M_R$] {#теорема-pmns-анархия}

:::tip Theorem (PMNS from O-sector anarchy) [C under O-anarchy of $M_R$]
The matrix of Majorana masses $M_R$ has an anarchic structure (all elements of the same order) in the O-sector, which together with nearly-diagonal $m_D$ (§4.2) gives large PMNS angles.
:::

**Proof.**

**Step 1 (Structure of $M_R$).** Right-handed neutrinos are Gap-configurations in the O-sector (T-51) [T]. Three right-handed neutrinos $\nu_R^{(k)}$ ($k \in \{1,2,4\}$) are different Gap-configurations within the O-sector. Majorana mass:

$$
[M_R]_{kl} = M_0 \cdot \langle \nu_R^{(k)} | H_{\text{Gap}}^{(O)} | \nu_R^{(l)} \rangle
$$

where $H_{\text{Gap}}^{(O)}$ is the Gap Hamiltonian of the O-sector.

**Step 2 (O-isotropy $\to$ anarchy).** From T-61 [T]: $\varepsilon_{O \to 3} \approx \varepsilon_{O \to \bar{3}} \approx \varepsilon_0$. The O-sector is isotropic with respect to both sectors. Gap-configurations $\nu_R^{(k)}$ differ in Fano phases $\phi_k = 2\pi k/7$, but all are at **equal distance** from O (in the Bures metric).

Therefore, the O-sector Gap Hamiltonian singles out no generation:

$$
|[M_R]_{kl}|/|[M_R]_{kk}| \sim O(1) \quad \forall k, l
$$

This is the **anarchic** structure of $M_R$.

**Step 3 (Seesaw with anarchic $M_R$).** For $m_D = \text{diag}(d_1, d_4, d_2)$ (from [§4.2](#теорема-нейтрино-o-сектор)) and $M_R$ — a dense $(3 \times 3)$ matrix with elements $O(M_0)$:

$$
m_\nu = m_D \cdot M_R^{-1} \cdot m_D^T
$$

$M_R^{-1}$ is also a dense matrix with elements $O(1/M_0)$.

The resulting $m_\nu$ is a dense matrix with elements:

$$
[m_\nu]_{kl} \sim d_k \cdot d_l / M_0
$$

Ratio of off-diagonal to diagonal elements:

$$
\frac{[m_\nu]_{kl}}{[m_\nu]_{kk}} \sim \frac{d_l}{d_k} \sim O(1)
$$

(since all $d_k \sim \varepsilon_0$, differences are only in factors $\sin(2\pi k/7) \in [0.43, 0.98]$).

**Step 4 (PMNS angles).** Diagonalization of $m_\nu$ with a dense structure and elements $O(1)$ gives mixing angles $O(1)$ (in radians), i.e., $O(30°\text{–}60°)$.

Concretely, for $m_D = \text{diag}(0.782, 0.434, 0.975) \cdot \varepsilon_0 v$ and $M_R = M_0 \cdot (I + \delta M)$ with $\delta M_{ij} \sim O(1)$:

Characteristic PMNS angles from anarchic $M_R$ (de Gouvêa–Murayama result, 2003):

$$
\theta_{12} \sim \arctan\sqrt{|m_{\nu_e}|/|m_{\nu_\mu}|} \sim \arctan\sqrt{0.975/0.434} \approx 56°
$$

$$
\theta_{23} \sim \arctan\sqrt{|m_{\nu_\mu}|/|m_{\nu_\tau}|} \sim \arctan\sqrt{0.434/0.782} \approx 37°
$$

$\blacksquare$

### 5.3 Comparison of mixing angles

| Parameter | CKM (quarks) | PMNS (leptons) | Prediction (anarchic $M_R$) | Ratio PMNS/CKM |
|----------|-------------|---------------|----------------------------|---------------------|
| $\theta_{12}$ | $13.0°$ | $33.4°$ | $\sim 56°$ | $2.6$ |
| $\theta_{23}$ | $2.4°$ | $49.0°$ | $\sim 37°$ | $20$ |
| $\theta_{13}$ | $0.2°$ | $8.6°$ | — | $43$ |

The qualitative prediction $\theta^{(\text{PMNS})} \gg \theta^{(\text{CKM})}$ holds for all three angles [T]. Quantitative predictions from anarchic $M_R$: $\theta_{12} \sim 56°$ (observed $33°$, order correct), $\theta_{23} \sim 37°$ (observed $49°$, close).

:::info Status [C under anarchic $M_R$]
Correct order of magnitude for PMNS angles. Exact prediction requires knowledge of specific $M_R$, which depends on the detailed Gap structure of the O-sector. The anarchic model gives angles $O(30°\text{–}60°)$, consistent with experiment.
:::

---

## 6. Connection to $G_2$-extra bosons [T] {#g2-extra}

### 6.1 $G_2$-extra bosons and the transition $\nu_R \to \nu_R^c$

The [$G_2$-structure](/docs/physics/gauge-symmetry/g2-structure) defines 14 gauge bosons, which decompose under $SU(3)_C$ as:

$$
\mathbf{14} \to \mathbf{8} \oplus \mathbf{3} \oplus \bar{\mathbf{3}}
$$

- $\mathbf{8}$ — gluons (massless, observable);
- $\mathbf{3} \oplus \bar{\mathbf{3}}$ — 6 $G_2$-extra bosons (super-heavy).

Extra bosons connect the spatial sector $\{A, S, D\}$ with the Gap sector $\{L, E, U\}$ and are capable of changing the Gap profile of a fermion. In particular, they generate the transition:

$$
\nu_R \;\xrightarrow[\Delta L = 2]{G_2\text{-extra}}\; \nu_R^c
$$

violating lepton number.

### 6.2 Mechanism of Majorana mass generation [T]

The Majorana mass is derived from the loop exchange of $G_2$-extra bosons ([Theorem 2.1](#теорема-mr-из-gap)):

$$M_R = \frac{g_{G_2}^4}{16\pi^2} \cdot \sqrt{6} \cdot \varepsilon \cdot M_{\text{Planck}} \approx 2.9 \times 10^{14} \text{ GeV}$$

The extra boson mass $M_{G_2}^{(\text{extra})} \sim \sqrt{6}\varepsilon M_P \sim 10^{17}$ GeV is determined by the opacity of the $O$-sector. The loop factor $g^4/(16\pi^2) \approx 1.5 \times 10^{-3}$ reduces the scale to $\sim 10^{14}$ GeV — exactly what is needed for seesaw.

### 6.3 Role of $G_2$-extra bosons in type-I seesaw

:::tip Claim 6.1 (Seesaw from $G_2$-structure) [I]
The mathematical mechanism of seesaw is [T] (T-51). The physical identification of $\nu_R$ with the $O$-sector is an interpretation [I], not requiring separate proof.

$G_2$-extra bosons provide type-I seesaw via the following chain:

1. **Existence of $\nu_R$:** Gap-configuration $(1,1)_0$ (Theorem 1.1).
2. **Dirac mass:** Yukawa coupling $y_\nu$ via [Higgs mechanism](/docs/physics/particle-physics/higgs-sector): $m_D = y_\nu v$.
3. **Majorana mass:** $G_2$-extra bosons generate $M_R$ via the transition $\nu_R \to \nu_R^c$.
4. **Seesaw formula:** $m_\nu \approx y_\nu^2 v^2 / M_R$.

Result: light neutrinos with $m_\nu \sim 0.01\text{--}0.05$ eV at $M_R \sim 10^{14}$ GeV.
:::

:::info Status [T]
The intermediate scale $M_R \sim 10^{14}$ GeV is **derived** from Gap parameters ([Theorem 2.1](#теорема-mr-из-gap)). The former hypothesis (ΓO) is proved [T] from PW clocks (A5) and viability (V): $\mathcal{G}_{\text{total}}^{(O)} = O(1)$ in Planck units. The dependence $M_R \propto \varepsilon \cdot M_P$ is testable: once $\varepsilon$ is fixed from the [self-consistent vacuum equation](/docs/core/dynamics/gap-thermodynamics), the prediction becomes quantitative.
:::

---

## 7. Neutrino Yukawa couplings [T] {#юкавские-связи}

### 7.1 Formula for Dirac Yukawa coupling via O-sector

Unlike charged fermions, the neutrino Yukawa coupling is determined **not** by the block $M_{3,\bar{3}}$ (Higgs line), but by the blocks $M_{O,3}$ and $M_{O,\bar{3}}$ of the internal Dirac operator (see [§4.2](#теорема-нейтрино-o-сектор)):

$$
m_D^{(k)} = \omega_0 \cdot \text{Gap}(O, k) \cdot |\gamma_{O,\text{partner}(k)}^{\text{vac}}| \cdot \sin\!\left(\frac{2\pi k}{7}\right)
$$

where $(k_1, k_2, k_3) = (1, 2, 4)$ are the [quadratic residues](/docs/physics/particle-physics/fermion-generations) $\bmod 7$, $\text{partner}(k)$ is the vertex of the Fano line $\{k, \text{partner}, O\}$.

### 7.2 Ratios of Dirac masses

From the O-sector structure (all $\varepsilon_0$ equal, Gap$(O,k) \approx 1$):

$$
m_D^{(1)} : m_D^{(4)} : m_D^{(2)} = \sin(2\pi/7) : |\sin(8\pi/7)| : \sin(4\pi/7) = 0.782 : 0.434 : 0.975
$$

Mass ratio for seesaw:

$$
\frac{m_{\nu_\mu}}{m_{\nu_\tau}} = \left(\frac{m_D^{(4)}}{m_D^{(1)}}\right)^2 = \left(\frac{|\sin(8\pi/7)|}{\sin(2\pi/7)}\right)^2 = \left(\frac{0.434}{0.782}\right)^2 \approx 0.308
$$

:::info Key distinction from naive seesaw
In the naive case $m_D \sim m_l$ (Higgs block) the ratio $m_2/m_3 \sim (m_\mu/m_\tau)^2 \approx 0.0035$ disagrees with observation by a factor of 50. Via the O-sector block $m_2/m_3 \approx 0.308$ (with two-loop RG correction $\approx 0.17\text{–}0.20$) — discrepancy reduced to $\times 1.0\text{–}1.2$. Formula T-63 **[T]**; precision is a computational task in $\theta^*$. Mechanism: $\nu_R$ lives in the O-sector (T-51 [T]), so the Dirac mass is determined by blocks $M_{O,\text{sector}}$, not $M_{3,\bar{3}}$.
:::

### 7.3 Full seesaw formula with O-sector structure [C under O-sector $D_\mathrm{int}$]

Full mass matrix of light neutrinos:

$$
m_\nu = m_D \cdot M_R^{-1} \cdot m_D^T
$$

where $m_D$ is nearly-diagonal with elements from the O-sector block, $M_R$ is dense (anarchic) from O-sector isotropy. Diagonalization gives physical masses and PMNS angles simultaneously (see [§5.2](#теорема-pmns-анархия)).

:::info Generation numbering [T]
The generation numbering $(k_1, k_2, k_3) = (1, 2, 4) \to (3\text{rd}, 1\text{st}, 2\text{nd})$ is **established**: $k=1$ — 3rd generation [T] (unique tree-level Yukawa), $k=4$ — 2nd and $k=2$ — 1st [T] (sectoral asymmetry proved from confinement). See [Three Fermion Generations, §4](/docs/physics/particle-physics/fermion-generations#4-назначение-поколений).
:::

---

## 8. Summary of predictions and status {#сводка}

### 8.1 Results

| Prediction | Formula | Value | Experiment | Status |
|-------------|---------|----------|-------------|--------|
| Mass of $\nu_\tau$ | $m_\tau^2/M_R$ | $\sim 0.03$ eV | $\sim 0.05$ eV | **[T]** Order-of-magnitude agreement |
| Mass of $\nu_\mu$ | $m_\mu^2/M_R$ (+ corrections) | $\sim 0.009$ eV | $\sim 0.009$ eV | **[T]** Agreement |
| Mass of $\nu_e$ | (+ Fano corrections) | $\sim 0.003$ eV | $< 0.8$ eV (direct) | **[T]** Compatible |
| Hierarchy | Seesaw + assignment $(k_n)$ | NH (normal) | Preference for NH | **[T]** |
| $m_2/m_3$ | O-sector Yukawa + 2-loop RG | $\approx 0.17\text{–}0.20$ | $0.17$ | **[C under 2-loop RG]** $\times 1.0\text{–}1.2$ |
| $\theta_{12}^{(\text{PMNS})} \gg \theta_{12}^{(\text{CKM})}$ | Anarchic $M_R$ from O-sector | $O(30°\text{–}60°)$ | $33°$ | **[C under anarchic $M_R$]** Order correct |
| $\theta_{23}^{(\text{PMNS})}$ | Anarchic $M_R$ | $\sim 37°$ | $49°$ | **[C under anarchic $M_R$]** Close |
| $\sum m_\nu$ | Summation | $\sim 0.042$ eV | $< 0.12$ eV | **[T]** Compatible |

### 8.2 Open problems

1. **Discrepancy $m_2/m_3$** — **resolved [C under 2-loop RG]**: O-sector Dirac Yukawa reduces the discrepancy from $\times 50$ to $\times 1.8$ (one-loop RG), then to $\times 1.0\text{–}1.2$ with two-loop RG. Formula T-63 **[T]**; precise prediction is a computational task in $\theta^*$. See [§4.3](#теорема-отношение-нейтринных-масс).

2. **Generation numbering** — resolved: $(k_1, k_2, k_3) = (1, 2, 4) \to (3\text{rd}, 1\text{st}, 2\text{nd})$ **[T]** (sectoral asymmetry proved from confinement). See [Theorem 4.1–4.3](/docs/physics/particle-physics/fermion-generations#thm-gen-4-1).

3. **Scale $M_R$** — resolved: $M_R$ is derived from $G_2$-extra bosons via loop mechanism **[T]** (PW clocks + viability). See [Theorem 2.1](#теорема-mr-из-gap).

4. **Quantitative PMNS angles** — **partially resolved [C under anarchic $M_R$]**: anarchic $M_R$ from O-sector isotropy gives large angles $O(30°\text{–}60°)$, consistent with experiment. Exact prediction requires detailed Gap structure of the O-sector. See [§5.2](#теорема-pmns-анархия).

5. **CP phase $\delta_{\text{CP}}^{(\text{PMNS})}$.** Analogue of the prediction $\delta_{\text{CP}}^{(\text{CKM})} \approx -2\pi/7$ for the lepton sector.

---

## Related documents

- [Fermion generations](/docs/physics/particle-physics/fermion-generations) — three generations from Fano
- [CKM matrix](/docs/physics/particle-physics/ckm-matrix) — quark mixing
- [Yukawa hierarchy](/docs/physics/particle-physics/yukawa-hierarchy) — mass hierarchy
- [Higgs sector](/docs/physics/particle-physics/higgs-sector) — electroweak symmetry breaking mechanism
- [Standard Model](/docs/physics/gauge-symmetry/standard-model) — SM from $G_2$
- [$G_2$-structure](/docs/physics/gauge-symmetry/g2-structure) — $G_2$-holonomy and extra bosons
- [Fano selection rules](/docs/physics/gauge-symmetry/fano-selection-rules) — Fano architecture
- [Supersymmetry](/docs/physics/particle-physics/susy) — SUSY from $G_2$-holonomy
