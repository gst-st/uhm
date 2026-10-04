---
sidebar_position: 4
title: "Pathology of Consciousness"
description: "Conditional matrix models and identifiability of clinical research features; hypotheses and validation requirements"
slug: /consciousness/states/pathological
---

# Pathology of Consciousness

This chapter proposes a research vocabulary for relating independently assessed clinical phenomena to a declared matrix model. A clinical category is not a Gap-profile by definition. Candidate correspondences have status **[H/I]** and require validation; mathematical constraints on matrices have status **[T]**.

:::note Typed statistics and observations
In a fixed native frame, $P=\mathrm{Tr}\Gamma^2$, $Q=\sum_i\gamma_{ii}^2$, $\Phi=P/Q-1$ and $R=1/(7P)$. For nonzero entries, $G_{ij}=|\sin\arg\gamma_{ij}|$ records an unoriented phase statistic. A zero entry has undefined phase. For a specified numerical self-model $M$, $R_M=1-\|\Gamma-M\Gamma\|_F^2/P$ can be negative and differs from $R$. The chosen capability gate $\mathrm{Cap}_2$ includes $P,R,\Phi$ and a separately typed differentiation certificate. Its relation to consciousness is a bridge hypothesis; the value $2/7$ is not a clinical survival cutoff. See the [mathematical kernel](/docs/reference/mathematical-kernel).
:::

:::warning Research scope
Neither Gap, purity, self-model score nor capability labels diagnose a disorder, determine its severity, or prescribe an intervention. The programme below requires independent clinical labels, a validated observation model, uncertainty estimates and held-out outcomes. It withdraws the previous diagnostic equivalences, universal three-opaque-channel rule and score-derived therapeutic times or targets.
:::

### Chapter roadmap

Historical frameworks; candidate feature mappings; statistical identifiability; joint phenomena; intervention study design; conditional dynamics and coding theory.

## 1. Historical perspective {#история}

### 1.1 Emil Kraepelin (1883): classification by course

Kraepelin — the father of nosological psychiatry. His key idea: mental diseases should be classified by *course* (outcome), rather than by *symptoms* (current picture). He distinguished two main forms:
- **Dementia praecox** (schizophrenia) — progressive deterioration
- **Manic-depressive psychosis** (bipolar disorder) — cyclical course

The proposed relation between longitudinal clinical course and matrix dynamics is a hypothesis [H]; neither monotone channel loss nor a Hopf model follows from the classification.

### 1.2 DSM: categorical approach (1952–2013)

The Diagnostic and Statistical Manual (DSM) — a categorical classification: each disorder is defined by a list of symptoms and inclusion/exclusion criteria. DSM has gone through 5 editions (I–5), gradually moving from psychodynamic concepts toward a descriptive approach.

**Problem with DSM:** categoricality. A patient 'has' or 'does not have' a disorder; the boundaries between categories are arbitrary; comorbidity (overlapping diagnoses) is the rule, not the exception. More than 50% of patients with depression have a comorbid anxiety disorder.

### 1.3 RDoC: dimensional approach (2010–present)

Research Domain Criteria (RDoC) — an initiative of the NIMH (National Institute of Mental Health, USA), proposing a *dimensional* approach: mental disorders are described not by categories but by *dimensions* (domains):
- Negative valence (fear, anxiety)
- Positive valence (reward, motivation)
- Cognitive systems (attention, memory)
- Social processes
- Arousal/regulatory systems

### 1.4 From RDoC to UHM

A dimensional observation model can compare clinical descriptions with estimated features of $\Gamma$ **[H]**. RDoC domains do not canonically equal matrix axes or pairwise phases; DSM labels do not supply a matrix reconstruction. Course is modeled by longitudinal data, not by an assumed universal bifurcation. The useful research question is whether a fixed encoder and its uncertainty-aware features add predictive value beyond independently measured baselines on held-out data.

## 2. Pathological Gap-patterns {#паттерны}

The following are proposed feature associations **[H]**, not definitions of the named conditions. They can overlap, fail to replicate or depend on the encoder. Each needs an independent target and a comparison model. The entries of a density matrix must jointly satisfy positivity; an arbitrary list of Gap values is not a certified state.

### 2.1 Alexithymia {#алекситимия}

**Candidate [H].** Test whether independently assessed difficulty identifying or verbalising emotions covaries with selected features such as $G_{AE}$ or $G_{LE}$. High phase Gap does not mathematically imply inability to notice, name or experience an emotion, and does not establish a two-channel clinical definition. Include amplitudes, task responses and uncertainty rather than assigning an illustrative patient a fabricated full profile. See [Gap-diagnostics](/docs/applied/research/gap-diagnostics).

### 2.2 Split neurosis (dissociation) {#невроз}

**Candidate [H].** A proposed dissociation model compares independently assessed discontinuities of access or report with features of a declared experiential extension. In minimal $\mathbb C^7$, the basis axis $E$ is one-dimensional: writing $E=E_1\oplus E_2$ does not create two nonzero subspaces. A richer $\mathcal H_E$, its normalized state and its readout must be supplied first. Contrasting $G_{SE}$ and $G_{DE}$ can be a proxy hypothesis; it is not equivalent to internal decomposition or a diagnosis.

### 2.3 Impulsivity {#импульсивность}

**Candidate [H].** Compare independently measured response inhibition with amplitude and oriented-phase features of a proposed $(L,D)$ mapping. The identity $G_{LD}=|\sin\theta_{LD}|$ makes $G_{LD}=1$ at $\theta_{LD}=\pi/2$ **[T]**. It does not make the phase a loss of logical control. A large matrix modulus is not evidence of stored knowledge, and a self-model score above $1/3$ does not certify awareness.

### 2.4 Existential crisis {#кризис}

**Interpretation [I/H].** The names “ground” and “unity” motivate testing whether features assigned to $(O,E)$ and $(O,U)$ relate to independently collected reports of meaning or coherence. These names do not prove that a high phase Gap disconnects a person from an ontological source. No numerical target for restoring meaning or clinical categorisation follows from them.

### 2.5 Depression {#депрессия}

**Candidate [H].** Longitudinal task measures could be compared with $P$, $\dot P$ and proposed affect-related features. Depression is not defined by $P\approx2/7$ or $\dot P\approx0$. For example, a stationary pure state has $P=1$ and $\dot P=0$, while stationary $I_7/7$ has $P=1/7$; stationarity occurs across the purity range **[T]**. No clinical label follows from either state. Repeated self-referential reports also do not mathematically imply high predictive accuracy of $M$; that accuracy needs a separate held-out prediction task.

### 2.6 Psychosis {#психоз}

A low or rapidly changing mean Gap is not a definition or diagnostic criterion of psychosis **[H]**. Phase coherence, reality assessment, report and noise immunity are distinct quantities. The earlier comparison “samādhi obeys a three-channel Hamming constraint, psychosis violates it” is withdrawn: no map from matrix phases to that code was provided, and the bound itself does not forbid all pairwise Gap values being zero. The explicit gate counterexample is in [§8.3](#психоз-хэмминг).

A prospective comparison would measure independently assigned clinical status, reports, task errors and a fixed matrix reconstruction, allowing the same Gap profile in different groups **[Pr]**. Distinguishing these groups requires validated observation distributions; a static feature vector does not establish delusions, hallucinations, reversibility or a required intervention.

## 3. Summary table of pathologies {#сводная-таблица}

| Proposed association [H] | Independent target | Candidate features |
|---|---|---|
| Alexithymia | Emotion identification/report task | $(A,E),(L,E)$ features |
| Dissociation | Access/report discontinuity | Specified experiential extension |
| Impulsivity | Response-inhibition task | $(L,D)$ features |
| Existential crisis | Independently collected meaning reports | $(O,E),(O,U)$ features |
| Depression | Independently assessed clinical state and task outcomes | Longitudinal features, without a purity cutoff |
| Psychosis | Independently assessed clinical state and task errors | Full observation model, without a Gap-zero rule |

The table supplies research questions, not a classifier. Capability levels are recorded separately using all prerequisites and higher-order certificates; no row assigns a physical L-level.

## 4. Correspondence of Gap-patterns to DSM-5 diagnoses {#dsm-таблица}

Clinical categories must be assigned independently of the candidate Gap features. A correspondence to DSM terminology is a proposed crosswalk **[H]**, not an equivalence, causal account or diagnostic conversion table. One label may include diverse feature profiles, and one profile may occur under several labels. The former numerical mappings and “bipolar disorder = Hopf oscillations of $P$” are not validated consequences of UHM. Evaluation should compare a preregistered feature model with clinical and task baselines on an independent cohort.

## 5. Diagnostic protocol {#протокол}

This is a research protocol **[Pr]**, not a diagnostic procedure validated for patients. The linked [measurement programme](/docs/applied/research/measurement-protocol) must supply an identifiable observation model.

### 5.1 Steps of pathological diagnosis

1. Specify independently assessed labels and task outcomes before fitting the encoder.
2. Declare the frame, observation law, identifiable features and reconstruction uncertainty; test full matrix positivity.
3. Fit candidate associations using training data; keep amplitudes, oriented phases and missing phases distinct.
4. Evaluate calibration and error rates on held-out participants or tasks, including controls and competing models.
5. Assess longitudinal dynamics from repeated observations. Report unmeasured capability or clinical variables as unknown.

### 5.2 Differential diagnosis

**Corrected identifiability statement [T].** For an observation map $s:Z\to S$, a target label $\ell:Z\to C$ can be recovered exactly from $s$ if and only if $\ell$ is constant on each fibre of $s$. Proof: if $\ell=h\circ s$, equal observations give equal labels; conversely define $h(s(z))=\ell(z)$, which is well-defined precisely under fibre constancy.

The former criterion “diagnoses differ iff some Gap differs by $\delta$” assumed this identifiability without proving it. **Counterexample.** The family $\Gamma(t)=(1-t)I_7/7+tuu^\dagger$, $u=(1,\ldots,1)/\sqrt7$, has all 21 phase Gaps zero for every $t>0$, while $P=(1+6t^2)/7$ and $\Phi=6t^2$ vary. A target depending on these features is not identifiable from Gap alone. This is a statement about statistics, not a clinical classification of these matrices.

With noisy observations, distinguishability concerns distributions $\mathbb P_A$ and $\mathbb P_B$, not a coordinate cutoff. For equal prior probabilities, the optimal single-observation binary error is $(1-\mathrm{TV}(\mathbb P_A,\mathbb P_B))/2$ **[T]**, where total variation uses the actual observation laws. Identical laws yield error $1/2$ regardless of assumed latent Gap differences. No universal $\delta=0.3$ ensures reliable differential diagnosis. See [Watrous, *The Theory of Quantum Information*, state discrimination](https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf) and [reconstruction identifiability](/docs/applied/research/reconstruction-identifiability).

## 6. Comorbidity as superposition of Gap-patterns {#коморбидность}

Co-occurrence of independently assessed phenomena requires a joint observation model **[H]**. Clinical coexistence is not a quantum superposition or a canonically defined operation on Gap vectors.

### 6.1 Superposition principle

A convex mixture $\Gamma_p=p\Gamma_A+(1-p)\Gamma_B$, $0\le p\le1$, is a valid density matrix **[T]**. It represents a declared mixture, not automatically comorbidity. The nonlinear phase statistic satisfies neither an additive nor a coordinatewise-max law in general.

**Counterexample.** On a $2\times2$ block let $\Gamma_\pm=\begin{pmatrix}1/2&\pm ia\\\mp ia&1/2\end{pmatrix}$, $0<a<1/2$. Both are positive and have Gap $1$ on the pair, but their half-mixture has zero coherence and hence undefined phase. Therefore $G(\Gamma_{1/2})=\max(G(\Gamma_+),G(\Gamma_-))$ is not a defined identity. Embed the block in $\mathbb C^7$ if desired. Coordinatewise maximum can be a separate descriptive rule **[D]**, but need not correspond to a realizable matrix or clinical mechanism.

### 6.2 Examples of comorbidity

Test a joint-outcome model against separate-outcome models, including interaction terms only when supported by data **[Pr]**. No multiplicative deterioration of purity or unique combined diagnosis follows from taking a union or maximum of candidate feature sets.

### 6.3 Visualisation of pathology space

A feature-space plot should show estimated joint distributions and uncertainty, with clinical labels supplied independently. Connecting two labels by an edge is a descriptive convention, not a proof of a trajectory or causal transition.

## 7. Corrective strategies {#коррекция}

The matrix model may motivate intervention hypotheses **[H]**. Its surrogate statistics do not establish clinical benefit, safety, dose, duration or modality selection.

### 7.1 Principles of correction

Choose the independently assessed outcome before selecting a feature objective **[Pr]**. A controller may target a realizable matrix profile **[D]**, but the meaningful empirical question is whether the intervention changes the outcome relative to a comparison condition. Neither $\mathbf G_{\mathrm{target}}\ne0$ nor retention of three nonzero Gaps is a universal therapeutic constraint. Preservation of the formal capability gate also does not replace clinical safety assessment.

### 7.2 Three correction modalities

Different intervention classes can be compared through independently specified protocols and outcomes **[Pr]**. Assigning one class to a decrease in Gap, another to an increase in regeneration and a third to a self-model score is a modeling hypothesis requiring separate evidence. The previous numerical treatment response tables and time estimates were illustrative assignments without that evidence and are withdrawn.

### 7.3 Correspondence of therapeutic approaches and channels

An approach-to-channel correspondence is a candidate mediation model **[H]**. It must test both the proposed feature change and the independently measured outcome; a target such as Gap $0.90	o0.25$ has no universal clinical meaning. Report intervention and outcome measurements separately from the reconstructed matrix.

### 7.4 Limitations of correction

Full phase transparency is mathematically possible; it is not proved dangerous by Hamming coding. Limits of a proposed intervention must come from its actual dynamics, observation uncertainty, resource constraints and outcome evidence. A metaphor of three load-bearing walls cannot supply those prerequisites.

## 8. Dynamics of pathological transitions {#динамика}

A temporal change of a feature or a clinical label need not be a bifurcation. Bifurcation claims require a specified flow, control parameter, equilibria and verified nondegeneracy conditions.

### 8.1 Entry into pathology

**Conditional models [C/H].** A saddle-node requires a zero eigenvalue and appropriate quadratic and parameter transversality conditions. A Hopf model requires a conjugate eigenvalue pair crossing the imaginary axis, with the remaining spectrum and nonlinear coefficient satisfying the relevant hypotheses. A pitchfork additionally requires the stated symmetry and degeneracy structure. Their clinical identification is an extra hypothesis; normal-form names do not determine a diagnosis or timescale. See [Ghrist, bifurcation theory](https://www2.math.upenn.edu/~ghrist/preprints/ADS-DRAFT.pdf).

**Counterexample to “oscillatory purity proves Hopf”.** A fixed qubit Hamiltonian and a pure initial state can give oscillating populations while purity stays $1$. Alternatively prescribing $P(\tau)=P_0+A\sin\omega\tau$ supplies a readout curve without any parameterized flow, stability loss or Hopf crossing. For this curve $\dot P=A\omega\cos\omega\tau$ is zero at its maxima and minima; the former table had these derivatives reversed. A fitted periodic signal therefore needs a separately validated dynamical explanation.

### 8.2 Exit from pathology

Recovery of an independently measured outcome can be studied longitudinally **[Pr]**. Non-Markovianity alone does not imply $	au_{\mathrm{exit}}\propto	au_{\mathrm{mem}}\max G$. Such a constitutive fit would require an explicitly defined exit event, units, parameters and validation. No treatment duration follows from kernel depth or Gap amplitude.

#### Operational noise threshold [D/H] {#определение-epsilon-noise}

The former “first principles” derivation is withdrawn. In a declared estimator model $\widehat\gamma_{ij}=\gamma_{ij}+\eta_{ij}$ with $\mathbb E\eta_{ij}=0$ and $\mathbb E|\eta_{ij}|^2=\sigma_{ij}^2$, one may define $\mathrm{SNR}_{ij}=|\gamma_{ij}|^2/\sigma_{ij}^2$ **[D]**. A detection threshold must then be calibrated to the noise law, sample size, chosen error criterion and readout.

**Counterexample.** Entries $r e^{i\theta}$ and $r'e^{i\theta}$ have the same phase Gap but different SNR at fixed noise variance. Thus $G<\varepsilon_{\mathrm{noise}}$ does not imply SNR $<1$, and SNR $=1$ does not universally mean $50\%$ error. Neither a sector-vacuum scale nor a binary-code bound supplies a universal clinical detectability threshold.

### 8.3 Psychosis and the Hamming bound {#психоз-хэмминг}

**Correct coding statement [T].** For a binary code of length $n$ correcting $t$ errors, disjoint Hamming balls give $M\sum_{j=0}^{t}\binom nj\le2^n$. The binary Hamming $(7,4,3)$ code has $M=16$, $t=1$ and saturates $16(1+7)=128$. Its three parity coordinates are not three nonzero pairwise phase Gaps. Applying it requires an encoder into binary words, a noise channel and a decoder; none is supplied by the density matrix definition. See [Hamming (1950)](https://doi.org/10.1002/j.1538-7305.1950.tb00463.x).

**Explicit counterexample to the previous T-90/41g application.** For the family in §5.2 at $t=0.45$,

$$
P=0.3164285714,\quad R=0.4514672686,\quad\Phi=1.215,
\quad G_{ij}=0\ (i<j).
$$

Using the *declared 7D proxy* from the hierarchy,

$$
\mathrm{Coh}_E=\frac{1+12t^2}{7(1+6t^2)},\qquad
D^{7D}=1+6\mathrm{Coh}_E\approx2.327314.
$$

The complete proxy gate $\mathrm{Cap}_2$ is satisfied although no pair is opaque. Hence neither the canonical gate nor Hamming's coding theorem forces three nonzero phase Gaps. This certifies a mathematical counterexample, not a physical or clinical conscious state. The universal pathology/coding identification is **withdrawn [✗]**; a specified code implementation could be studied conditionally **[H/Pr]**.

## 9. Pathology space: visualisation {#пространство-патологий}

A plot of estimated features is a projection of the chosen observation model. Distinct clinical groups may overlap in it, and projection may erase distinguishing variables. A point or cluster is not automatically an attractor; an attractor requires a specified dynamical system.

## 10. Map of pathologies on the phase diagram {#фазовая-диаграмма}

The [Gap phase diagram](/docs/core/dynamics/gap-phase-diagram) is a conditional model of an explicitly chosen potential and control parameters. Clinical labels cannot be located uniquely on it from a mean Gap or purity. Relating a fitted transition to a clinical trajectory requires independently measured controls and the bifurcation conditions in §8.1; no universal category-to-phase assignment is asserted.

### What we learned {#итоги}

1. Clinical labels and task outcomes must be measured independently; proposed Gap associations remain hypotheses.
2. A target is identifiable from a statistic only when constant on its fibres; noisy classification depends on observation distributions and calibrated errors.
3. Matrix mixtures do not obey a universal maximum or additive Gap law, and do not by definition model comorbidity.
4. Bifurcations require an actual flow and nondegeneracy hypotheses; an oscillating or threshold-crossing score is insufficient.
5. Hamming's code bound concerns binary codewords. The explicit zero-Gap $\mathrm{Cap}_2$ example rules out the claimed three-opaque-channel necessity.
6. Intervention effects, safety and duration cannot be deduced from static matrix scores; the remaining programme uses independent outcomes and held-out validation.

## Connections

- **Gap-diagnostics:** [Applied Gap-diagnostics](/docs/applied/research/gap-diagnostics) — protocol and diagnostic patterns
- **Gap-dynamics:** [Bifurcations of the Gap-landscape](/docs/core/dynamics/gap-dynamics#бифуркации) — transition theory
- **Unconscious:** [Gap-structure of the unconscious](/docs/consciousness/states/unconscious) — definition of opaque sectors
- **Gap-characterisation of levels:** [Gap-signatures](/docs/consciousness/hierarchy/gap-characterization) — normal profiles for L0–L4
- **Altered states:** [ASC](/docs/consciousness/states/altered-states) — psychedelics and meditation as therapeutic trajectories
- **Viability:** [Viability measure](/docs/core/dynamics/viability) — threshold $P_{\text{crit}} = 2/7$
- **Measurement protocol:** [Measurement of Γ](/docs/applied/research/measurement-protocol) — empirical validation
- **CC Theorems:** [Coherence Cybernetics](/docs/applied/coherence-cybernetics/theorems) — withdrawn T-90 clinical bridge; conditional coding and research designs
