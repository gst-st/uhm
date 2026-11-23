---
sidebar_position: 2
title: "Calibration: Coherences to Qualities"
description: "Prospective protocol sketch [Pr] for calibrating proposed relations between physical measurements and independently recorded qualities, pending definition and validation of π_bio."
slug: /consciousness/empirical/calibration
---

# Calibration: Coherences to Qualities

:::info Prospective protocol sketch [Pr]
This page is a **prospective protocol sketch [Pr]** pending an explicit definition and empirical validation of the biological encoder $\pi_{\mathrm{bio}}$ and its observation model. No participant data have been collected and no biological calibration has been validated.
:::

A candidate encoder maps recorded signals to an estimated state. A separate observation model relates that estimate to a participant’s report. Both the form and the parameters of those maps require evidence. The protocols below give examples of tests. Participant data are pending. [What a phenomenal difference requires](/docs/consciousness/foundations/phenomenal-distinction)

## Two calibrations, not one {#two-calibrations}

**1. Measurement calibration.** Fix the sensor configuration, encoding $\pi$ and noise model. Different encoders can agree on all calibration observations. For example, a diagonal measurement leaves every off-diagonal phase unconstrained. A separately calibrated interference probe can test a phase assignment. [Identifiability of the observation model](/docs/applied/research/reconstruction-identifiability)

**2. The phenomenal calibration** takes $\hat\Gamma$ to named qualities. It has two parts:

- **the metric map** $f$ from perceived dissimilarity to the Fubini–Study distance $d_{\mathrm{FS}}$. The [enriched Yoneda theorem](/docs/proofs/categorical/categorical-formalism#enriched-yoneda) [T] makes the quality space testable only after $f$ is fixed; with $f$ only assumed monotone, the test is ordinal and weaker;
- **the anchoring**: which ray or state label corresponds to a named quality (for example, red). Universal faithfulness of state encoders up to a finite frame group is withdrawn ([T-42a [✗]](/docs/proofs/categorical/uniqueness-theorem); [identifiability scope](/docs/consciousness/foundations/two-aspect-monism#faithful-g2-box)); observed marginals, spectra, and moduli generally have non-trivial fibres, so the correspondence between state coordinates and quality names must be measured and anchored empirically rather than derived. Whether two subjects' quality spaces are related by an inversion stays open ([relational identity](/docs/consciousness/foundations/two-aspect-monism#теорема-реляционная-определённость)).

Neither part can be settled by proof. Both are settled by fitting on data where the answer is independently known and testing on data that did not enter the fit.

## Observables and where they enter $\Gamma$ {#observables}

| Observable | Typical measure | Component of $\Gamma$ it bears on | Source | Status of the mapping |
|---|---|---|---|---|
| Presence / absence report | immediate or delayed report | ground truth for the verdict $\mathrm{Cons}(\hat\Gamma)$ — inference data only | [substitution theorem](/docs/applied/research/measurement-protocol#substitution-position) | [T] as a statement about test design |
| Intensity rating | magnitude estimation | spectrum $\lambda_i$ | [falsifiability, predictions 1, 3](/docs/reference/falsifiability#isospectral-discrimination) | open prediction [H] |
| Discrimination | $d'$, just-noticeable difference | $d_{\mathrm{FS}}$ between rays at fixed spectrum | [isospectral discrimination](/docs/reference/falsifiability#isospectral-discrimination) | open prediction [H] |
| Similarity judgement | pairwise dissimilarity matrix | $d_{\mathrm{FS}}$ through $f$ | [metric relations](/docs/reference/falsifiability#metric-relations); [enriched Yoneda](/docs/proofs/categorical/categorical-formalism#enriched-yoneda) | geometry [T]; identification of experiences with rays [I] |
| Metacognition | meta-$d'$, confidence calibration | reflection $R$, self-model quality $R_\varphi$ | [phenomenology map](/docs/applied/research/phenomenology-map#карта); [gate theorem T-252 [T]](/docs/proofs/categorical/formalization-phi#гейт-теорема) | bound [T]; correspondence [H] |
| Valence, arousal | rating scales, circumplex | hypothesized correspondence to $\mathrm{sign}(dP/d\tau)$, $\lvert dP/d\tau\rvert$; for a differentiable declared 30-feature readout, two trace identities bound the Jacobian rank by $\le 28$ (T-147 [T]) | [affective reports and purity change](/docs/consciousness/phenomenology/emotional-taxonomy#базовые-координаты); [T-147](/docs/proofs/consciousness/operational-closure#t-147) | rank bound [T]; affect bridge [H]/[I] |
| EEG spectral power | band power | populations $\gamma_{kk}$ | [Step 1](/docs/applied/research/measurement-protocol#шаг-1-диагональ) | [H] (C31) |
| Cross-frequency coupling | phase–amplitude coupling | moduli $\lvert\gamma_{ij}\rvert$ | [Step 2](/docs/applied/research/measurement-protocol#шаг-2-когерентности) | [H] (C31) |
| Phase locking | complex phase-locking values | phases, hence Fano holonomies $H_p$ | [Step 3](/docs/applied/research/measurement-protocol#шаг-3-фазы); SUB-3 | [H] |
| TMS-evoked complexity | $\mathrm{PCI}_{\max}$ | an **independent verdict** ($\mathrm{PCI}_{\max} > 0.31$), not a number to match | [Step 5](/docs/applied/research/measurement-protocol#pci-связь) | concordance test [Pr] |
| fMRI slow components | number of independent slow features | opacity rank of the Gap operator | [F-ISF](/docs/reference/falsifiability#f-isf-isf-компоненты-в-фмрт) | [H] |

Two cautions carry over from the sources. Observables are defined in incommensurable units, so each enters as a percentile against a **declared reference ensemble** that is published with the result ([Lesson 1](/docs/applied/research/measurement-protocol#граница-валидации)). And $\Gamma$ is built from functional indices, never from raw signal statistics, because signals with an atypical carrier (the hypersynchronous delta EEG of awake children with Angelman syndrome) mislead any carrier-level measure (Lesson 3).

## The design rule: prediction data and inference data {#design-rule}

Kleiner and Hoel separate the data a theory predicts from (*prediction data*: here, the signals that enter $\hat\Gamma$) from the data an experimenter infers experience from (*inference data*: reports and behaviour). The corpus has a theorem on where UHM stands between their two horns ([position against the substitution argument](/docs/applied/research/measurement-protocol#substitution-position), [T] with part (v) [H]):

- a reconstruction whose $\theta$ is fitted on report-labelled sessions tests nothing on those sessions — its agreement with the labels holds by construction;
- after $\theta$ is frozen, the verdict depends on prediction data alone, and reports count as evidence only inside a declared domain $D_{\mathrm{nat}}$ (intact adult brains, natural sleep–wake states, standard anaesthetics).

Every protocol below therefore follows the pre-registration SUB-1…SUB-6 of that section: $\theta$ frozen on wakefulness only; no viability penalty in confirmatory runs ($\lambda_2 = 0$ — with the default $\lambda_2 = 100$ the estimator returned $\hat P = 2/7$ for every sub-threshold state of the uniform family, so P8.2 could not be observed); phases from EEG, never from reaction times; verdicts registered before unblinding.

## Protocols {#protocols}

### K1. Threshold concordance — existing protocol {#k1-threshold}

**Claim.** In $D_{\mathrm{nat}}$, $P(\hat\Gamma_{\mathrm{wake}}) > 2/7$ (P8.1) and $P(\hat\Gamma_{\mathrm{NREM3}}) < 2/7$ (P8.2), and the verdict $\mathrm{Cons}(\hat\Gamma)$ agrees with $\mathrm{PCI}_{\max} > 0.31$ on the same sessions (P8.4 in concordance form, SUB-5) — [table of P8 predictions](/docs/applied/research/measurement-protocol#тестируемые-предсказания-p8).

**Data.** The sessions of Casarotto et al. (2016): 150 subjects, 540 TMS-evoked potential sets. The decisive rows are REM sleep (8 subjects) and ketamine anaesthesia (6 subjects) — consciousness without behaviour at the time, out of sample once $\theta$ is frozen on wakefulness.

**Measure of what the decisive rows can show.** If all 14 of them come out concordant, the one-sided 95 % lower bound on the concordance rate in that class is $0.05^{1/14} = 0.807$; with the 8 REM subjects alone it is $0.688$. The 14 subjects can corroborate; they cannot establish a rate above about 0.8.

**Decision.** Cohen's $\kappa \geq 0.8$ corroborates, $\kappa < 0.4$ falsifies (SUB-5 [Pr]). Current status: untested — no $\pi_{\mathrm{bio}}$ session exists ([decision protocols](/docs/applied/coherence-cybernetics/predictions#decision-protocols)).

### K2. The two exits — existing protocol {#k2-two-exits}

Among sessions with $\mathrm{PCI}_{\max} \leq 0.31$, responses that stay local are predicted to have $\hat\Phi < 1$, and responses that spread as a stereotyped global wave $\hat P > 3/7$ ($\hat R < 1/3$) — SUB-6 [H]. The window has two edges, so a low complexity has two UHM signatures. This compares prediction data with prediction data, so the substitution argument does not touch it.

### K3. Metric calibration of quality space — proposed here [Pr] {#k3-metric}

**Claim under test.** Perceived dissimilarities are a monotone function of $d_{\mathrm{FS}}$ between the rays assigned by a declared quality-ray readout ([prediction 4](/docs/reference/falsifiability#metric-relations)).

**Protocol.** (1) A stimulus set of $m$ items in one modality; full pairwise dissimilarity ratings from each subject, twice (test–retest). (2) In the same sessions, reconstruct per-stimulus $\hat\Gamma$ (and, where an extended experiential register $\mathcal{H}_E$ is declared, the reduced state $\hat\rho_E$) from $\pi_{\mathrm{bio}}$ with frozen $\theta$, together with a predeclared normalized stimulus-to-ray map $s \mapsto [\lvert q(s)\rangle] \in \mathbb{CP}^{n-1}$ (distinct from the mutually orthogonal eigenrays of any single matrix, whose pairwise Fubini–Study distances are trivially $\pi/2$ and which are non-unique at spectral degeneracy; if the readout yields mixed states, predeclare a mixed-state metric such as the Bures distance instead of substituting eigenrays). (3) Fit a monotone $f$ on a random half of the stimuli; predict the ordering of dissimilarities among the held-out half from the declared state distance alone.

**Pass criteria** (from the falsifiability page): Spearman $\rho_S(d_{\mathrm{perceived}}, d_{\mathrm{FS}}) > 0.6$; monotonicity violations below 10 % of pairs; MDS stress below 0.1.

**What it calibrates.** The fitted $f$ is the constant the enriched Yoneda test needs; once $f$ is fixed, the realisability test of the [structure page](./structure#realisability) becomes metric rather than ordinal.

**Limit.** Step (2) requires a validated biological encoder $\pi_{\mathrm{bio}}$ and an explicit stimulus-to-ray (or mixed-state) readout; until both are defined and calibrated, only the behavioural half — whether similarity data admit a complex-projective geometry at all — can be run, and it belongs to the [structure page](./structure).

### K4. Intensity and quality dissociate — existing criteria {#k4-dissociation}

Two distinct hypotheses on the [falsifiability page](/docs/reference/falsifiability#isospectral-discrimination) test whether spectral and frame/context degrees of freedom dissociate [H], and they operate at different architectural levels that must not be conflated: (i) on the native $7\times 7$ matrix $\Gamma$, a nondegenerate spectrum carries 6 real eigenvalues (fixing purity $P$ and canonical reflection $R$) while the unitary orbit carries 42 real parameters ([T-300 [T]](/docs/consciousness/phenomenology/qualia-structure#теорема-пространство-качества)), so isospectral states with distinct declared readouts are hypothesized to differ in quality rather than spectral intensity (spectra within $0.01$, declared ray/state separation $> 0.05$ rad); (ii) context modulation at fixed $\rho_E$ applies only after declaring an extended tensor-product experiential register $\mathcal{H}_E \otimes \mathcal{H}_{-E}$ ([realization contract](/docs/core/structure/dimension-e#rho-e-7d-42d)), since the native $E$-axis is one-dimensional and does not define a non-trivial reduced density matrix $\rho_E$. In that extended setting, canonical differentiation is $D_{\mathrm{diff}} = \exp S_{vN}(\rho_E)$ on $\mathcal{H}_E$ (whereas the native 7D proxy is $D^{7D} = 1 + 6\,\mathrm{Coh}_E(\Gamma)$, never $\exp S_{vN}(\Gamma)$ on the full $7\times 7$ matrix $\Gamma$); varying the complementary context $\Gamma_{-E}$ at fixed $\rho_E$ and bounded global purity shift ($\lvert\Delta P\rvert < 0.05$) is hypothesized to shift reported quality ($p < 0.01$) without changing the $\rho_E$-spectrum.

### K5. Affect calibration — proposed here [Pr] {#k5-affect}

**Claim under test.** A proposed empirical bridge [H]/[I] maps rated valence to $\mathrm{sign}(dP/d\tau)$ and arousal to $\lvert dP/d\tau\rvert$ ([affective reports and purity change](/docs/consciousness/phenomenology/emotional-taxonomy#базовые-координаты); purity flux $\dot P = 2\operatorname{Tr}(\Gamma\dot\Gamma)$ is purely dynamical and requires an independent outcome to test any hedonic reading, cf. [T-147 [T]](/docs/proofs/consciousness/operational-closure#t-147), where two trace identities bound the Jacobian rank of a differentiable declared 30-feature readout by $\le 28$ without establishing an emotion taxonomy).

**Protocol.** Within-subject time series: continuous valence and arousal ratings during an affect-inducing sequence, and $d\hat P/d\tau$ from $\pi_{\mathrm{bio}}$ with frozen $\theta$. **Pass:** sign agreement between rated valence and $d\hat P/d\tau$ above the rate obtained after circularly shifting the rating series (the null keeps both autocorrelations and breaks the alignment), pre-registered at $p < 0.01$. **Fail:** no agreement above the shifted null.

### K6. Metacognition and the self-model — existing correspondence, sharpened [H] {#k6-metacognition}

The phenomenology map predicts that metacognitive sensitivity (meta-$d'$) tracks reflection $R$. The [gate theorem](/docs/proofs/categorical/formalization-phi#гейт-теорема) (T-252 [T]) gives the correspondence a form: any decision read through the self-model $\varphi$ loses at most $2\sqrt{3/7}\,\sqrt{P(1 - R_\varphi)}$ of accuracy. The testable consequence [H]: across sessions, the gap between first-order accuracy and metacognitive accuracy grows with $\sqrt{\hat P(1 - \hat R_\varphi)}$. A flat relation falsifies the correspondence, not the theorem.

### K7. Adaptation dynamics — existing criteria {#k7-adaptation}

Intensity follows $\mathcal{Q}(t) \sim \log(\lambda_{\max}(t)/\langle\lambda_{\max}\rangle_\tau)$ ([prediction 3](/docs/reference/falsifiability#adaptation-dynamics)): correlation above 0.7, slope in $[0.8, 1.2]$, adaptation period between 100 and 1000 ms. The falsifiability page lists it as "consistent" with the Weber–Fechner law; a law that many theories share does not discriminate between them, so a pass here corroborates little.

### K8. Regeneration and $E$-coherence — existing protocol, underpowered as written {#k8-regeneration}

Treat a correlation between an estimated $E$-coherence and a recovery rate as an empirical hypothesis. Freeze the estimator and the response window, estimate sample size for the smallest effect of interest and compare against a model using baseline physiology. Choosing $\kappa$ proportional to a coherence in a simulation imposes the model relation and cannot validate it in observations.

## Controls {#controls}

| Control | What it guards against | Source |
|---|---|---|
| $\theta$ frozen on wakefulness; no NREM, anaesthesia, REM or ketamine label in the fit | a verdict that reproduces its own training labels | SUB-1 |
| $\lambda_2 = 0$ in confirmatory runs | an estimator that contains the predicate | SUB-2 |
| Phases from EEG, not reaction times | inference data leaking into prediction data | SUB-3 |
| Basis and encoder sensitivity: repeat the analysis under admissible axis permutations and alternative phase/encoder conventions | a result that is an artefact of an unidentifiable basis or encoder choice (universal finite-group faithfulness is withdrawn, T-42a [✗]) | [identifiability](/docs/applied/research/reconstruction-identifiability); [uniqueness scope](/docs/proofs/categorical/uniqueness-theorem) |
| Label-shuffle and circular-shift nulls | alignment produced by autocorrelation | standard |
| Test–retest of every behavioural matrix | an unstable ground truth | [Console V0-VAL](/docs/applied/console/roadmap-validation#v0) |
| Cross-anchor agreement (self-report against wearable on shared sectors) | two instruments estimating different objects | [Console V1-VAL](/docs/applied/console/roadmap-validation#v1) |
| Negative control: an unrelated exogenous time series or sham stimulus must not modulate $\hat P$ | a pipeline that finds spurious structure anywhere | standard |
| Blind raters for any behavioural scoring | expectation effects | [test E10](/docs/consciousness/subjects/ai-consciousness#тест-e10-ethical-threshold) |

## Statistics {#statistics}

- **Pre-registration.** Hypotheses, pass and fail thresholds, sample sizes, exclusion rules and the reference ensemble are registered before data are unblinded (SUB-4). A test that was not pre-registered counts as exploration, not as corroboration or refutation (the rule of the [in-silico suite](/docs/consciousness/subjects/ai-consciousness#agi-инженерные-тесты)).
- **Power for correlations** (two-sided $\alpha = 0.05$, power 0.8, Fisher $z$): $r = 0.3$ needs $n = 85$; $r = 0.5$ needs $n = 29$; $r = 0.6$ needs $n = 20$.
- **Power for concordance.** With chance agreement 0.5 and a true $\kappa = 0.8$, the half-width of the 95 % interval for $\kappa$ is about 0.20 at 35 sessions, 0.17 at 50 and 0.12 at 100. Separating the corroboration threshold 0.8 from the falsification threshold 0.4 needs about 35 sessions or more.
- **Dependent pairs.** A dissimilarity matrix over $m$ stimuli has $m(m-1)/2$ entries (4278 for 93 colours), but they are not independent: significance comes from permutation of stimulus labels (Mantel-type tests), not from the pair count.
- **Many channels.** Tests run over 21 channels or 7 lines form a pre-declared family, corrected by Holm or false-discovery-rate control.
- **Effect sizes.** Every result is reported with its effect size and confidence interval; paired designs use the Wilcoxon test, as the falsifiability page specifies.

## Falsification criteria {#falsification}

| Result | What it refutes | Level ([three-level system](/docs/applied/research/experimental-protocol#falsification)) |
|---|---|---|
| $\hat P < 2/7$ in healthy waking subjects, or $\hat P > 2/7$ in N3, with $\theta$ frozen (P8.1, P8.2) | the window as the criterion of consciousness in $D_{\mathrm{nat}}$ | structural |
| $\kappa < 0.4$ between $\mathrm{Cons}(\hat\Gamma)$ and $\mathrm{PCI}_{\max} > 0.31$ (SUB-5) | the concordance claim | structural |
| Local low-complexity responses with $\hat\Phi \geq 1$, or global stereotyped ones with $\hat P \leq 3/7$ (SUB-6) | the two-exit reading [H] | local |
| Two states with identical full invariants and distinguishable experience | supervenience of experience on $(\Gamma, \mathrm{Hist})$ — only jointly with a frozen $\pi_{\mathrm{bio}}$ ([refutation criterion](/docs/reference/falsifiability#refutation-criterion)) | catastrophic |
| No monotone relation between perceived dissimilarity and $d_{\mathrm{FS}}$ (K3) | the metric prediction; the identification of quality space with $\mathbb{CP}^{n-1}$ [I] loses its only direct support | structural |
| $\hat\Gamma$ non-positive or irreproducible across sessions ([Prediction 21](/docs/applied/coherence-cybernetics/predictions#предсказание-21)) | the calibration $\pi_{\mathrm{bio}}$, not the formalism | local |

Agreement at one fitted point does not test transfer. A confirmatory failure counts against the preregistered prediction for its stated population, outcome and readout.

**Next:** [Structure →](./structure) · **Back:** [Overview](./overview)
