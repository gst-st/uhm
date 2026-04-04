---
sidebar_position: 3
title: Falsifiability
description: Verification criteria and predictions of UHM theory
---

# Falsifiability and Predictions

:::note On notation
In this document:
- $\rho$, $\rho_E$ — [density matrix](/docs/core/dynamics/coherence-matrix), reduced density matrix of the Interiority dimension
- $\Gamma_{-E}$ — [context](/docs/reference/specification#полное-экспериенциальное-пространство) (states of all dimensions except $E$)
- $\lambda_i$ — eigenvalues of $\Gamma$ (intensities)
- L0, L1, L2 — [interiority hierarchy levels](/docs/proofs/consciousness/interiority-hierarchy)
- $d_{\mathrm{FS}}$ — [Fubini-Study metric](/docs/reference/specification#метрика-фубини-штуди)
- $R_{\text{th}}$, $\Phi_{\text{th}}$ — [threshold values](/docs/proofs/consciousness/interiority-hierarchy#обоснование-порогов)
:::

## Falsification Criteria

### Experimental Predictions

The extended theory makes testable predictions:

#### 1. Isospectral discrimination

Two states $\rho_1$, $\rho_2$ with $\mathrm{Spec}(\rho_1) = \mathrm{Spec}(\rho_2)$ but $\mathrm{Eigvec}(\rho_1) \neq \mathrm{Eigvec}(\rho_2)$ should yield:
- Identical experience intensity (spectrum determines intensity)
- Distinguishable experience quality (eigenvectors determine [quality](/docs/proofs/categorical/categorical-formalism#2-категория-exp))

**Numerical criteria:**
- Spectra 'identical': $\|\mathrm{Spec}(\rho_1) - \mathrm{Spec}(\rho_2)\|_2 < \varepsilon_{\text{spec}} = 0.01$
- Vectors 'distinguishable': $\min_i |\langle v_i^{(1)} | v_i^{(2)} \rangle| < 1 - \varepsilon_{\text{vec}}$, where $\varepsilon_{\text{vec}} = 0.1$
- Quality 'distinguishable': $d_{\text{FS}}([|q_1\rangle], [|q_2\rangle]) > \varepsilon_{\text{qual}} = 0.05$ rad

**Test:** Create isospectral neural states, measure phenomenal reports.

#### 2. Contextual modulation

Changing [context](/docs/reference/specification#полное-экспериенциальное-пространство) $\Gamma_{-E}$ with fixed $\rho_E$ should alter the *quality* of experience without changing *intensity*.

**Numerical criteria:**
- $\rho_E$ 'fixed': $\|\rho_E^{(1)} - \rho_E^{(2)}\|_F < \varepsilon_{\rho} = 0.02$
- Context 'changed': $\|\Gamma_{-E}^{(1)} - \Gamma_{-E}^{(2)}\|_F > \delta_{\Gamma} = 0.1$
- Intensity 'constant': $|\mathrm{Tr}((\rho_E^{(1)})^2) - \mathrm{Tr}((\rho_E^{(2)})^2)| < \varepsilon_P = 0.05$
- Quality 'changed': phenomenal report distinguishable with $p < 0.01$ (statistical test)

**Test:** Modulate context (attention, mood) at constant stimulus, measure changes in perceptual quality.

#### 3. Adaptation dynamics

[Experiential content](/docs/proofs/categorical/categorical-formalism#2-категория-exp) (levels [L1–L2](/docs/proofs/consciousness/interiority-hierarchy)) should follow the adaptation law:

$$
\mathcal{Q}(t) \sim \log\left(\frac{\lambda_{\max}(t)}{\langle\lambda_{\max}\rangle_\tau}\right)
$$

where:
- $\mathcal{Q}(t)$ — subjective experience intensity at time $t$
- $\lambda_{\max}(t)$ — maximum eigenvalue of $\Gamma(t)$
- $\langle\lambda_{\max}\rangle_\tau$ — average over adaptation period $\tau$

:::info Interpretation
This prediction follows from the fact that perception encodes *changes* relative to baseline (Weber-Fechner law), not absolute values.
:::

**Numerical criteria:**
- Correlation $r(\mathcal{Q}_{\text{measured}}, \mathcal{Q}_{\text{predicted}}) > r_{\min} = 0.7$
- Regression slope $\beta \in [0.8, 1.2]$ (close to 1)
- RMSE $< \sigma_{\mathcal{Q}} / 2$ (error less than half the standard deviation)
- Adaptation period $\tau \in [100, 1000]$ ms (typical range)

**Test:** Measure the temporal dynamics of adaptation, compare with prediction.

#### 4. Metric relations

Distances in phenomenal space ([L1](/docs/proofs/consciousness/interiority-hierarchy#уровень-1-феноменальная-геометрия-phenomenal-geometry)) should correspond to the [Fubini-Study metric](/docs/reference/specification#метрика-фубини-штуди):

$$
d_{\mathrm{perceived}}(q_1, q_2) \sim d_{\mathrm{FS}}([|q_1\rangle], [|q_2\rangle])
$$

where $[|q\rangle] \in \mathbb{P}(\mathcal{H}_E)$ — equivalence class in [projective space](/docs/reference/specification#проективное-пространство-качеств).

**Numerical criteria:**
- Spearman correlation $\rho_S(d_{\text{perceived}}, d_{\text{FS}}) > 0.6$
- Monotonicity: violations $< 10\%$ of the total number of pairs
- Metric consistency: $|d(a,b) + d(b,c) - d(a,c)| < \varepsilon_{\triangle} = 0.15$ (triangle inequality)
- MDS reconstruction: stress $< 0.1$ when mapping to $\mathbb{R}^k$

**Test:** Build a phenomenal quality map (L1), compare with predicted geometry.

## Refutation Criterion

The theory is falsified if:

$$
\exists \rho_1, \rho_2 : \mathcal{I}(\rho_1) = \mathcal{I}(\rho_2), \text{ but } F(\rho_1) \neq F(\rho_2)
$$

where:
- $\mathcal{I}(\rho) := (\mathrm{Spec}(\rho), \mathrm{Eigvec}(\rho), \Gamma_{-E}, \mathrm{Hist})$ — full invariant
- $F: \mathbf{DensityMat} \to \mathbf{Exp}$ — [experience functor](/docs/proofs/categorical/categorical-formalism#3-функтор-f-на-объектах)

That is, if two states with *identical* full invariants (spectrum + eigenvectors + context + history) yield *distinguishable* experience.

:::info Gauge precision [T]
The [$G_2$-rigidity theorem](/docs/proofs/categorical/uniqueness-theorem) [T] refines the notion of 'identity': two states $\rho_1, \rho_2$ are considered **physically identical** if $\rho_2 = U\rho_1 U^\dagger$ for some $U \in G_2$. The full invariant $\mathcal{I}(\rho)$ is defined on the space $\mathcal{D}(\mathbb{C}^7)/G_2$ (34 parameters). The eigenvectors in the table below implicitly assume a fixed $G_2$-gauge; under gauge change $v_i \to Uv_i$, but the inner products $|\langle v_i^{(1)} | v_i^{(2)} \rangle|$ are $G_2$-invariant.
:::

**Operational tolerances:**

| Invariant component | 'Identity' criterion |
|---------------------|------------------------|
| Spectrum | $\|\mathrm{Spec}(\rho_1) - \mathrm{Spec}(\rho_2)\|_2 < 0.01$ |
| Eigenvectors | $\forall i: \lvert\langle v_i^{(1)} \vert v_i^{(2)} \rangle\rvert > 0.99$ |
| Context | $\|\Gamma_{-E}^{(1)} - \Gamma_{-E}^{(2)}\|_F < 0.02$ |
| History | $d_{\text{edit}}(\mathrm{Hist}_1, \mathrm{Hist}_2) < 0.05 \cdot \lvert\mathrm{Hist}\rvert$ |

| Interiority | 'Distinguishability' criterion |
|------|------------------------|
| Phenomenal report | Statistically distinguishable ($p < 0.01$, Wilcoxon test) |
| Behavioural marker | AUC > 0.7 in discrimination task |

:::note Practical criterion
For experimental verification it is sufficient to compare the spectrum and eigenvectors (without history): if $\mathrm{spec}(\rho_1) = \mathrm{spec}(\rho_2)$ and $|q_i^{(1)}\rangle = |q_i^{(2)}\rangle$, but $\mathcal{F}(\rho_1) \neq \mathcal{F}(\rho_2)$, the theory is falsified.
:::

:::info Note on operationalisation
The full invariant $\mathcal{I}(\rho) = (\mathrm{Spec}, \mathrm{Eigvec}, \Gamma_{-E}, \mathrm{Hist})$ is a **theoretical ideal**. Operational realisation:
- **Spec(ρ):** measurable via quantum state tomography
- **Eigvec(ρ):** measurable via full tomography (neural correlates)
- **Γ_{-E}:** approximately measurable via partial trace — discarding the E-component
- **Hist:** approximated via time correlators $\langle O(\tau)O(0) \rangle$ (two-point functions, accessible via fMRI/EEG)

The falsification criterion is **strict in the theoretical sense** and **approximate in the experimental sense**. This is the standard situation for theories with directly unobservable objects (cf. the wave function in QM).
:::

**See also:** [КК falsification criteria](/docs/applied/coherence-cybernetics/predictions#критерий-фальсификации-кк) — additional operational criteria for the applied theory.

## Current Empirical Status

| Prediction | Status | Comment |
|--------------|--------|-------------|
| Isospectral discrimination | Open | Requires neurophenomenological experiments |
| Contextual modulation | Partially confirmed | Consistent with attention influence data |
| Adaptation dynamics | Consistent | Consistent with Weber-Fechner law |
| Metric relations | Open | Requires phenomenal space mapping ([L1](/docs/proofs/consciousness/interiority-hierarchy#уровень-1-феноменальная-геометрия-phenomenal-geometry)) |
| Functional purity | Programme | $P > P_{\text{crit}}$ for $\geq 90\%$ of functioning systems |
| P-quality correlation | Programme | Correlation of $P$ with functional quality: $r > 0.5$ |
| [F-m_t](#f-m_t-масса-top-кварка-из-неподвижной-точки-пендлтона-росса): $m_t \approx 173$ GeV | Consistent | Observation: $172.57 \pm 0.29$ GeV |
| [F-Cabibbo](#f-cabibbo-угол-кабиббо-из-rg-подавления-фано-угла): $\theta_{12} \approx 13°$ | Consistent | Observation: $12.96°$ ($\|V_{us}\| = 0.2243$) |
| [F-δ_CP](#f-δ_cp-cp-фаза-ckm-из-фано-фазы): $\delta_{\text{CP}} \approx 64°$ | Consistent (${\sim}0.8\sigma$) | Observation: $69° \pm 4°$, $\sigma_{\mathrm{comb}} \approx 6.4°$ |
| [F-Gap-1](#f-gap-1-внутри-триплетный-gap-ниже-межтриплетного): Gap_intra < Gap_inter | Open | Requires ISF analysis of fMRI |
| [F-ISF](#f-isf-isf-компоненты-в-фмрт): 6–12 ISF components | Open | Requires systematic fMRI analysis |
| [F-ξ](#f-ξ-корреляционная-длина-фано): $\xi_F \sim 160$ pc | Open | Testable through LSS surveys |
| [F-nEDM](#f-nedm-нейтронный-эдм): $d_n = 0$ (T-99) | Consistent | $\|d_n\| < 1.8 \times 10^{-26}$ e·cm (PSI 2020) |
| [F-τ_p](#f-τ_p-время-жизни-протона): $\tau_p \sim 6.7 \times 10^{37}$ years | Open | Hyper-K: sensitivity $\sim 10^{35}$ years |
| [F-Higgs](#f-higgs-отклонение-самосвязи-хиггса): $\delta\lambda/\lambda \sim 10^{-2}$–$10^{-3}$ | Open | Awaiting FCC-hh |

## Falsifiable predictions from Fano integration

:::info Source
Predictions are derived from the integration of [Fano geometry](/docs/physics/gauge-symmetry/fano-selection-rules) with [Gap dynamics](/docs/core/dynamics/gap-dynamics), [Gap thermodynamics](/docs/core/dynamics/gap-thermodynamics), and [RG flow](/docs/physics/gauge-symmetry/rg-flow). Each prediction is assigned a rigour status in accordance with the [registry](/docs/reference/status-registry).
:::

### F-Gap-1: Intra-triplet Gap below inter-triplet {#f-gap-1-внутри-триплетный-gap-ниже-межтриплетного}

$$
\langle \mathrm{Gap}_{\mathrm{intra}} \rangle < \langle \mathrm{Gap}_{\mathrm{inter}} \rangle
$$

The mean [Gap](/docs/physics/dual-aspect/gap-semantics) within [Fano triplets](/docs/physics/gauge-symmetry/fano-selection-rules) is lower than between them. Coherences belonging to the same Fano line are more transparent (closer to $\mathrm{Gap}=0$) than coherences connecting different lines.

**Testability:** ISF components (independent slow features) in fMRI. Intra-triplet correlations should systematically exceed inter-triplet correlations.

**Status:** [H] Hypothesis — consequence of [Gap semantics](/docs/physics/dual-aspect/gap-semantics) and [G₂-covariance](/docs/physics/gauge-symmetry/g2-structure).

---

### F-Gap-2: Block transparency by Fano triplets {#f-gap-2-блоковая-прозрачность-по-фано-триплетам}

Coherences within the same [Fano line](/docs/physics/gauge-symmetry/fano-selection-rules) are more strongly correlated, forming a block structure in the coherence matrix $\Gamma$. The Fano dissipator preserves triplet coherences ([T], [G₂-structure](/docs/physics/gauge-symmetry/g2-structure)), generating distinguished block transparency.

**Testability:** Correlation analysis of the coherence matrix — 7 blocks of $3 \times 3$ (by Fano lines) should be statistically separated from off-block elements.

**Status:** [T] Theorem — consequence of theorems 10.1–10.3 (Fano channel preserves coherences, [status registry](/docs/reference/status-registry)).

---

### F-ξ: Fano correlation length {#f-ξ-корреляционная-длина-фано}

$$
\xi_F \sim 160 \; \text{pc}
$$

The correlation length of [Fano structure](/docs/physics/gauge-symmetry/fano-selection-rules) in [large-scale structure](/docs/physics/cosmology-phys/dark-matter). The scale is determined by [RG suppression](/docs/physics/gauge-symmetry/rg-flow) of the cubic coupling $\lambda_3$ and the [phase diagram](/docs/core/dynamics/gap-phase-diagram) of the Gap potential.

**Testability:** Large-scale structure of the Universe — correlation function on scales $\sim 100$–$200$ pc. Absence of a preferred scale $\sim 160$ pc falsifies the prediction.

**Status:** [T] Theorem — theorems 9.1–9.2 ([status registry](/docs/reference/status-registry)).

---

### F-τ_p: Proton lifetime {#f-τ_p-время-жизни-протона}

$$
\tau_p \sim 6.7 \times 10^{37} \; \text{years}
$$

The proton lifetime, computed from the masses of [$X,Y$-leptoquarks](/docs/physics/particle-physics/proton-decay) via the [Gap hierarchy](/docs/physics/gauge-symmetry/standard-model).

**Testability:** Hyper-Kamiokande experiment (sensitivity up to $\sim 10^{35}$ years). Current Super-K limit: $\tau_p > 2.4 \times 10^{34}$ years. The prediction lies 2–3 orders of magnitude above Hyper-K sensitivity — direct detection of decay at this $\tau_p$ is unlikely, but **detection of decay at $\tau_p < 10^{36}$ years** falsifies the prediction.

:::warning Note on testability
The prediction $\tau_p \sim 10^{37}$–$10^{38}$ years **exceeds the sensitivity** of Hyper-K ($\sim 10^{35}$ years for $p \to e^+\pi^0$) by 2–3 orders of magnitude. Direct verification is **impossible** in the foreseeable future. Indirect constraints are possible via neutron-antineutron oscillations.
:::

**Status:** [H] Hypothesis — depends on the precision of the $M_X$ computation ([proton decay](/docs/physics/particle-physics/proton-decay)).

---

### F-m_t: Top quark mass from the Pendleton-Ross fixed point {#f-m_t-масса-top-кварка-из-неподвижной-точки-пендлтона-росса}

$$
m_t \approx 173 \; \text{GeV}
$$

The top quark mass is derived from the quasi-IR [Pendleton-Ross fixed point](/docs/physics/particle-physics/yukawa-hierarchy#3-quasi-ir-fixed-point-и-масса-t-кварка). The unique Fano-Higgs line $\{A, E, U\}$ admits a tree-level Yukawa coupling [only for the third generation](/docs/physics/particle-physics/higgs-sector#1-единственность-хиггсовой-линии-aeu); the RG evolution of this coupling is attracted to the fixed point that fixes $m_t$.

**Testability:** Already consistent with observations ($m_t^{\text{exp}} = 172.57 \pm 0.29$ GeV). The prediction is falsified by a significant shift in the experimental value.

**Status:** [T] Theorem — theorem 5.1 ([status registry](/docs/reference/status-registry), [Yukawa hierarchy](/docs/physics/particle-physics/yukawa-hierarchy)).

---

### F-ISF: ISF components in fMRI {#f-isf-isf-компоненты-в-фмрт}

$$
N_{\text{ISF}} \in [6, 12]
$$

The number of ISF components (independent slow features) in fMRI data is determined by the opacity rank of the [Gap operator](/docs/core/dynamics/gap-dynamics). At full transparency (all $\mathrm{Gap}(i,j) = 0$) the rank is 0 and all 21 coherences are active; at full opacity the rank is maximal (21). For biologically realistic regimes the rank is $\sim 9$–$15$, giving $21 - 15 = 6$ to $21 - 9 = 12$ active independent components.

**Testability:** ISF component analysis of fMRI data. Systematic detection of $N_{\text{ISF}} < 6$ or $N_{\text{ISF}} > 12$ falsifies the prediction. The dependence of $N_{\text{ISF}}$ on the state of consciousness (wakefulness / sleep / anaesthesia) should correlate with the rank of the Gap operator.

**Status:** [H] Hypothesis — consequence of [Gap dynamics](/docs/core/dynamics/gap-dynamics) and the [interiority hierarchy](/docs/consciousness/hierarchy/interiority-hierarchy).

---

### F-Neural: Neural correlates of L-levels [C with bridge assumption] {#f-neural-нейронные-корреляты}

The form of scaling relations (threshold at $P = 2/7$, monotonic dependence of $\Phi$ on connectivity) is derived [C with bridge assumption]. Numerical coefficients are empirical. Experimental protocol: fMRI/EEG during anaesthesia$\leftrightarrow$wakefulness transitions to verify the threshold.

**Testability:** Measurement of the $\Phi$ jump under pharmacological control of anaesthesia depth (sevoflurane, propofol). Prediction: existence of a sharp transition $P \approx 2/7$, not gradual sliding. The $\Phi(\text{connectivity})$ dependence is monotonic.

**Status:** [C with bridge assumption] — the scaling form is derived from theory; numerical coefficients require empirical calibration.

---

### F-Higgs: Higgs self-coupling deviation {#f-higgs-отклонение-самосвязи-хиггса}

$$
\frac{\delta\lambda}{\lambda_{\text{SM}}} \sim O(10^{-2} \text{–} 10^{-3})
$$

The octonionic correction to the [Higgs sector](/docs/physics/particle-physics/higgs-sector#4-масса-хиггса-с-октонионной-коррекцией) modifies the Higgs self-coupling at the level of $\sim 1\%$–$0.1\%$ relative to the Standard Model prediction.

**Testability:** FCC-hh collider (sensitivity to $\delta\lambda/\lambda_{\text{SM}} \sim$ several percent). If FCC-hh measures $\lambda_{hhh}$ with $\sim 5\%$ precision and detects a deviation of order $1\%$ — that is confirmation. Absence of deviations at precision $\ll 0.1\%$ — falsification.

**Status:** [H] Hypothesis — depends on non-perturbative computations in the [Higgs sector](/docs/physics/particle-physics/higgs-sector).

---

### F-δ_CP: CKM CP-phase from the Fano phase {#f-δ_cp-cp-фаза-ckm-из-фано-фазы}

$$
\delta_{\text{CP}} \approx 64° \pm 5°
$$

The [CKM matrix](/docs/physics/particle-physics/ckm-matrix#4-фаза-cp-нарушения) CP-phase is derived from the geometric phase of the [Fano plane](/docs/physics/gauge-symmetry/fano-selection-rules). Observed value: $\delta_{\text{CP}}^{\text{exp}} = 69° \pm 4°$. At combined uncertainty $\sigma_{\mathrm{comb}} = \sqrt{5^2 + 4^2} \approx 6.4°$ the discrepancy is $5°/6.4° \approx 0.8\sigma$.

**Testability:** Refinement of the experimental value at LHCb and Belle II. The prediction is falsified if $\delta_{\text{CP}}^{\text{exp}}$ shifts beyond $\sim 2\sigma$ from $64°$ (i.e. beyond $[54°, 74°]$).

**Status:** [H] Hypothesis — depends on the [Fritzsch texture](/docs/physics/particle-physics/ckm-matrix#6-ckm-из-несовпадения-юкавских-текстур) and loop corrections.

---

### F-Cabibbo: Cabibbo angle from RG suppression of the Fano angle {#f-cabibbo-угол-кабиббо-из-rg-подавления-фано-угла}

$$
\theta_{12} \approx 13°
$$

The [Cabibbo angle](/docs/physics/particle-physics/ckm-matrix#3-угол-кабиббо) is derived from [RG suppression](/docs/physics/gauge-symmetry/rg-flow) of the fundamental Fano angle $2\pi/7 \approx 51.4°$. Observed value: $\theta_{12}^{\text{exp}} \approx 13.0°$.

**Testability:** Consistent with current data ($|V_{us}| = 0.2243 \pm 0.0005$, corresponding to $\theta_{12} \approx 12.96°$). The prediction is falsified by a significant revision of $|V_{us}|$.

**Status:** [H] Hypothesis — depends on loop corrections and [RG flow](/docs/physics/gauge-symmetry/rg-flow).

---

### F-nEDM: Neutron EDM ($\theta_{\mathrm{QCD}} = 0$ exactly) {#f-nedm-нейтронный-эдм}

$$
d_n = 0 \quad \text{(exactly)}
$$

Prediction [T] (T-99): $\theta_{\mathrm{QCD}} = 0$ **exactly** ([structural proof](/docs/physics/gauge-symmetry/confinement#теорема-структурное-theta-qcd)), not $\theta < 10^{-10}$. Neutron electric dipole moment:

$$
d_n = \frac{e \cdot m_q}{m_n^2} \cdot \theta_{\mathrm{QCD}} = 0
$$

Current experimental limit: $|d_n| < 1.8 \times 10^{-26}$ e·cm (PSI 2020). Future experiments (n2EDM, nEDM@SNS) will reach sensitivity $\sim 10^{-28}$ e·cm.

**Falsification:** Detection of $d_n \neq 0$ at **any** level → direct refutation of T-99.

**Difference from axion solution:** The axion allows $\theta \sim m_a / f_a \cdot T \sim 10^{-18}$ — non-zero, albeit ultra-small. Gap theory predicts a **strict zero**.

**Status:** [T] Theorem — T-99 ([status registry](/docs/reference/status-registry), [confinement](/docs/physics/gauge-symmetry/confinement#теорема-структурное-theta-qcd)).

---

### Summary table of predictions

| Code | Prediction | Falsification criterion | Experiment | Status |
|-----|-------------|------------------------|-------------|--------|
| **F-Gap-1** | $\langle\mathrm{Gap}_{\mathrm{intra}}\rangle < \langle\mathrm{Gap}_{\mathrm{inter}}\rangle$ | Systematically $\mathrm{Gap}_{\mathrm{intra}} \geq \mathrm{Gap}_{\mathrm{inter}}$ | fMRI (ISF) | [H] |
| **F-Gap-2** | Block transparency by Fano triplets | Absence of block structure in coherences | fMRI | [T] |
| **F-ξ** | $\xi_F \sim 160$ pc | Absence of preferred scale $\sim 160$ pc | LSS surveys | [T] |
| **F-τ_p** | $\tau_p \sim 6.7 \times 10^{37}$ years | $\tau_p < 10^{36}$ years | Hyper-K | [H] |
| **F-m_t** | $m_t \approx 173$ GeV | Significant shift in $m_t^{\text{exp}}$ | Colliders | [T] |
| **F-ISF** | 6–12 ISF components | $N_{\text{ISF}} \notin [6, 12]$ | fMRI | [H] |
| **F-Neural** | Threshold $P = 2/7$, monotonic $\Phi$(connectivity) | Gradual transition without threshold | fMRI/EEG (anaesthesia) | [C with bridge] |
| **F-Higgs** | $\delta\lambda/\lambda_{\text{SM}} \sim 10^{-2}$–$10^{-3}$ | No deviations at precision $\ll 0.1\%$ | FCC-hh | [H] |
| **F-δ_CP** | $\delta_{\text{CP}} \approx 64° \pm 5°$ | $\delta_{\text{CP}}^{\text{exp}} \notin [54°, 74°]$ | LHCb, Belle II | [H] |
| **F-Cabibbo** | $\theta_{12} \approx 13°$ | Significant revision of $\|V_{us}\|$ | Kaon experiments | [H] |
| **F-nEDM** | $d_n = 0$ (T-99: $\theta_{\mathrm{QCD}} = 0$ exactly) | $d_n \neq 0$ at any level | n2EDM, nEDM@SNS | [T] |

:::warning Status of predictions
Predictions marked [T] are based on rigorously proved theorems (see [status registry](/docs/reference/status-registry)). The [octonionic bridge](/docs/proofs/minimality/theorem-octonionic-derivation) is fully closed [T] (T15). Predictions marked [H] require additional computations or contain gaps in the physical arguments.
:::

## Completeness of Theory

The theory is complete in the following sense:

1. **Self-sufficiency:** Requires no external postulates or references
2. **Universality:** Applicable to structural aspects of self-referential systems — from quantum to cognitive
3. **Internal consistency:** Contains no contradictions
4. **Operationality:** Can be computationally implemented
5. **Explanatory power:** Resolves traditional philosophical problems
6. **Falsifiability:** Makes testable predictions about the structure of experience
7. **Formal rigour:** Key theorems proved ([7D minimality](/docs/proofs/minimality/theorem-minimality-7), [operator φ](/docs/proofs/categorical/formalization-phi), [functor F](/docs/proofs/categorical/categorical-formalism))
8. **Compatibility with QM:** The nonlinear regenerative term $\mathcal{R}$ [does not violate the no-signalling constraint](/docs/proofs/physics/physics-correspondence#запрет-сигнализации) — proved via the CPTP property of $\varphi$ (conditions [NS1-NS3](/docs/core/dynamics/evolution#запрет-сигнализации))
9. **Ensemble independence:** Evolution is defined on $\Gamma$ (density matrix), not on wave functions — [does not depend on decomposition](/docs/proofs/physics/physics-correspondence#85-ансамблевая-независимость)
10. **Computational consistency:** The nonlinearity $\mathcal{R}$ [does not provide acceleration](/docs/proofs/physics/physics-correspondence#86-вычислительное-ограничение) beyond BQP

## Vulnerability analysis {#анализ-уязвимостей}

Systematic analysis of five main vulnerabilities of the theory (2026):

| # | Vulnerability | Initial status | Result | New status |
|---|-----------|----------------|-----------|-------------|
| 1 | $\dim = 7$ as postulate | Not empirically verified | 15+ independent derivations [T]: Theorem S (minimality) + octonionic derivation + T15 (bridge) | **Closed** (theoretically) |
| 2 | $D_{\mathrm{diff}} \geq 2$ [C] | Conditional theorem | T-129 [T]: $\Phi_{\mathrm{th}} = 1$ from first principles → T-151 [T]: $D_{\min} = 2$ unconditionally | **Closed** (fully) |
| 3 | $R = 1/(7P)$ counterintuitive | Requires empirical verification | Algebraic identity [T], [physical interpretation](/docs/proofs/consciousness/conscious-window#физическая-интерпретация-r), T-124 [T] (non-emptiness of Goldilocks zone) | **Closed** (theoretically) |
| 4 | No experiments | 157+ theorems without lab verification | ~30 testable [predictions](/docs/applied/coherence-cybernetics/predictions), 5 post-hoc coincidences (F-m\_t, F-Cabibbo, F-δ\_CP, F-nEDM, Weber-Fechner) | **Confirmed** (requires experiment) |
| 5 | Quantum nature of $\Gamma$ | Tegmark decoherence | T-132 [T] (necessity of complex $\gamma_{ij}$) + T-153 [T] (substrate closure), but [Tegmark argument](/docs/consciousness/foundations/two-aspect-monism#квантовая-природа-gamma) not fully addressed | **Partially open** |

**Summary:** 3 of 5 vulnerabilities closed theoretically; 1 is fundamentally experimental; 1 is deeply open (quantum nature of $\Gamma$).

## Theory Boundaries {#границы-теории}

:::info Philosophy of boundaries
Acknowledging boundaries is not a weakness, but a strength of a scientific theory. A theory that claims to explain everything without exception is most likely unscientific.
:::

### Structural Boundaries (what is not proved)

| Question | Status | Comment |
|--------|--------|-------------|
| Why 7 dimensions? | [Minimality proved](/docs/proofs/minimality/theorem-minimality-7) | But not uniqueness |
| Values of constants $\omega_i$, $J_{ij}$, $\gamma_k$ | Empirical | Not derived from axioms |
| Uniqueness of $\Gamma$ | Not proved | Other 'universes' possible |
| Uniqueness of partition $\{A,S,D,L,E,O,U\}$ | **Proved [T]** | All 7 dimensions are [functionally unique](/docs/proofs/minimality/theorem-minimality-7#единственность-e) (A,S,D,L,U — algebraically; E,O — via κ₀) |

### Physical Boundaries

| Question | Status | Comment |
|--------|--------|-------------|
| Einstein equations | **[T] Derived** | Spectral action (T-65); $M^4$ derived (T-120) |
| Standard Model | Structure **[T]**, parameters partially | $G_2 \to SU(3)_C \times SU(2)_L \times U(1)_Y$ [T]; specific masses — partially |
| Spacetime dimensionality $3+1$ | **[T] Derived** | Sectoral decomposition + Connes reconstruction (T-119, T-120) |
| Constants $c$, $G$, $\hbar$ | $G$ **[T]** derived, $c$, $\hbar$ not explained | $G_N = 3\pi/(7f_2\Lambda^2)$ (T-65); $c$, $\hbar$ — fundamental |

### Phenomenal Boundaries (what is taken as axiom)

1. **Categorical gap:** The theory does not explain *why* mathematical structures are 'felt.' The identity of being and experience — [Axiom Ω⁷](/docs/core/foundations/axiom-omega), not a theorem.

2. **Qualia calibration:** The correspondence between specific eigenvalues/eigenvectors and specific qualities of experience is established empirically.

:::info Qualia calibration — an empirical question
Which specific $[|q\rangle] \in \mathbb{P}(\mathcal{H}_E)$ corresponds to 'red' is an empirical question, not a theoretical defect. This is analogous to how the electron mass is not derived from the Standard Model. The structure of experience (spectral decomposition) is the [unique functor](/docs/consciousness/foundations/two-aspect-monism#теорема-единственность-фв) compatible with the axiomatics, but the specific calibration is determined experimentally.
:::

3. **Absolute qualia:** The question of the existence of context-independent qualia remains open.

4. **Thresholds [L2](/docs/proofs/consciousness/interiority-hierarchy#уровень-2-когнитивные-квалиа-cognitive-qualia):** $R_{\text{th}} = 1/3$ **[T]** — derived from [triadic decomposition](/docs/core/operators/lindblad-operators#триадная-декомпозиция) ($K = 3$ types of dynamics from axioms) + [Bayesian dominance](/docs/core/foundations/axiom-septicity#теорема-порог-рефлексии). $\Phi_{\text{th}} = 1$ **[T]** — unique self-consistent value at $P_{\text{crit}} = 2/7$ ([T-129](/docs/proofs/consciousness/operationalization#t-129)).

### Categorical Boundaries

1. **$\mathbf{Exp}$ is not a topos:** [It is proved](/docs/proofs/categorical/categorical-formalism#6-топосная-структура) that the category $\mathbf{Exp}$ is not a topos — there is no internal logic of experiential content.

2. **Functor $F$ is non-invertible:** One cannot uniquely recover $\rho$ from experiential content — different states may yield 'identical' experience.

3. **Problem of time:** The category $\mathbf{DensityMat}$ is static; time requires an external parameter.

### Status of Boundaries

These boundaries are **not a deficiency**, but an acknowledgement:
- The theory describes *structure*, not the question of 'why this particular structure'
- Some questions may be *beyond* any possible explanation
- Honest acknowledgement of boundaries is a mark of a mature theory

**Comparison with physics:**
Physics does not explain *why* the laws of nature exist — it describes their structure. Analogously, UHM describes the structure of experience, acknowledging the boundaries of explanation.

### Octonionic Falsification Criteria

[The structural derivation](/docs/proofs/minimality/theorem-octonionic-derivation) through octonions generates additional testable predictions:

| Prediction | Falsification criterion | Status |
|--------------|------------------------|--------|
| **Fano symmetries of coherences** | 7 triplets $(e_i, e_j, e_k)$ of the Fano plane should be distinguishable in the structure of coherences $\gamma_{ij}$ | [T] |
| **$G_2$-covariance** | The dynamics of $\Gamma$ must be covariant with respect to $G_2 \subset SO(7)$, not the full $SO(7)$ | [T] |
| **Associator anomalies** | Triple interactions of dimensions should exhibit non-associativity: $[x, y, z] \neq 0$ | [T] |
| **Hamming threshold** | Structure $H(7,4)$: system is viable with loss of up to 3 of 7 coherences (error correction) | [T] |

:::tip Bridge [T] — fully closed (T15)
The connection (AP)+(PH)+(QG)+(V) → P1+P2 is established via the complete formal chain T15 (12 steps, all [T]). T11–T13 prove the former condition (МП). All octonionic predictions are consequences of the structural derivation [T].
:::

### Research programme

Boundaries do not mean a halt to development. Open directions:

| Direction | Goal | Priority |
|-------------|------|-----------|
| Quantum gravity | Derive $g_{\mu\nu}$ from $\Gamma$ | High |
| Experimental validation of thresholds | Verify $R_{\text{th}} = 1/3$, $\Phi_{\text{th}} = 1$ empirically | High |
| Isospectral experiments | Test prediction 1 with numerical tolerances | High |
| ISF analysis of fMRI | Verify [F-Gap-1](#f-gap-1-внутри-триплетный-gap-ниже-межтриплетного), [F-Gap-2](#f-gap-2-блоковая-прозрачность-по-фано-триплетам), [F-ISF](#f-isf-isf-компоненты-в-фмрт) | High |
| Non-perturbative computations | Refine [F-Higgs](#f-higgs-отклонение-самосвязи-хиггса), [F-τ_p](#f-τ_p-время-жизни-протона) | High |
| Correlation length $\xi_F$ | Verify [F-ξ](#f-ξ-корреляционная-длина-фано) through LSS surveys | Medium |
| Connection with Hoffman | Prove equivalence with the theory of conscious agents | Medium |
| $\infty$-topos | Construct $\infty$-topos on $\mathbf{Exp}$ | Low |
| Standard Model | Close the derivation of $\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$ from the [Gap hierarchy](/docs/physics/gauge-symmetry/standard-model) | Long-term |

---

**Related documents:**
- [Glossary](./glossary) — definitions of terms
- [Status registry](/docs/reference/status-registry) — complete registry of results with classification [T]/[H]/[P]/[I]/[D]
- [Axiom Ω⁷](/docs/core/foundations/axiom-omega) — ∞-topos Sh_∞(𝒞) as primitive
- [Mathematical apparatus](/docs/reference/specification) — formal definitions of $\Gamma$, $d_{\mathrm{FS}}$
- [Interiority hierarchy](/docs/proofs/consciousness/interiority-hierarchy) — levels L0→L1→L2→L3→L4, thresholds $R_{\text{th}}$, $\Phi_{\text{th}}$, $R^{(n)}_{\text{th}}$
- [Categorical formalism](/docs/proofs/categorical/categorical-formalism) — functor $F$, categories $\mathbf{DensityMat}$ and $\mathbf{Exp}$
- [7D minimality theorem](/docs/proofs/minimality/theorem-minimality-7) — proof of $N = 7$
- [Structural derivation via octonions](/docs/proofs/minimality/theorem-octonionic-derivation) — P1+P2 → 𝕆 → N=7
- [Formalisation of operator φ](/docs/proofs/categorical/formalization-phi) — CPTP channels
- [Theorems](/docs/applied/coherence-cybernetics/theorems) — formal results
- [CC predictions](/docs/applied/coherence-cybernetics/predictions) — CC-specific falsification criteria
- [Fano selection rules](/docs/physics/gauge-symmetry/fano-selection-rules) — Fano selection rule for Yukawa couplings
- [Gap semantics](/docs/physics/dual-aspect/gap-semantics) — dual-aspect semantics of 49 elements
- [Gap dynamics](/docs/core/dynamics/gap-dynamics) — Gap operator, bifurcations, non-Markovian dynamics
- [Gap thermodynamics](/docs/core/dynamics/gap-thermodynamics) — information geometry, potential $V_{\text{Gap}}$
- [RG flow of Gap](/docs/physics/gauge-symmetry/rg-flow) — $\beta$-functions, fixed points, RG suppression of $\lambda_3$
- [Higgs sector](/docs/physics/particle-physics/higgs-sector) — uniqueness of the line $\{A,E,U\}$, Higgs mass
- [CKM matrix](/docs/physics/particle-physics/ckm-matrix) — Fritzsch texture, Cabibbo angle, CP phase
- [Yukawa hierarchy](/docs/physics/particle-physics/yukawa-hierarchy) — Pendleton–Ross fixed point, $m_t$
- [Proton decay](/docs/physics/particle-physics/proton-decay) — $X,Y$-leptoquarks, $\tau_p$
- [Dark matter](/docs/physics/cosmology-phys/dark-matter) — $O$-sector relic, $\xi_F$
- [G₂ structure](/docs/physics/gauge-symmetry/g2-structure) — covariance of the Fano dissipator
