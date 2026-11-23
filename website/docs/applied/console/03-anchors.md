---
sidebar_position: 3
title: "03 · Anchors and estimation"
description: "How a real GammaEstimate is produced from evidence. The full 28-item self-audit instrument reproduced, the scoring model that maps responses to a coherence matrix (populations, magnitudes, and the honest phase-blindness), the measurement-bridge mathematics for the neural/physiological path with the PCI verdict comparison, and the oracle protocol — each with its estimator, its uncertainty model, and its declared loss."
---

# 03 · Anchors and estimation

> *The kernel is only as honest as the estimate it is fed. This document specifies the three estimators exactly — what each can see, what it is blind to, and how much to trust it — so that the anchor tag the kernel carries is backed by real mathematics, not a label.*

## §1. The estimation problem, restated {#задача}

An estimator turns evidence $e$ into a `GammaEstimate` — a state `gamma`, a covariance `cov`, an `anchor` tag. The three anchor classes differ in the evidence they use and, crucially, in **which sectors of Γ they can resolve**:

| Anchor | Resolves populations | Resolves coherence magnitudes | Resolves phases (Gap) | `cov` available |
|---|---|---|---|---|
| I — measured | yes | yes | partially (needs time-resolved signals) | yes |
| II — autoephemeris | yes | yes | **no** (a questionnaire is phase-blind) | via test-retest |
| III — oracle | — | — | — | none (not an estimate) |

This table is the honest core: the self-audit gives a good diagonal and good coherence *magnitudes*, but it cannot give phases, so the Gap map from Anchor II is not reported as measured. The kernel's chart-type guardrail ([02 §4](/docs/applied/console/kernel#гардрейлы)) enforces exactly this.

## §2. Anchor II — the self-audit instrument, in full {#инструмент}

The instrument is the **28-cell self-audit** `[Pr]` structured directly on the 7 populations and 21 pairwise channels of $\Gamma$ ([coherence matrix](/docs/core/dynamics/coherence-matrix), [empirical programme](/docs/consciousness/empirical/overview)). Each item is rated $0$–$3$ (almost never / sometimes / often / almost always); first responses are better data than considered ones.

**The seven population items (diagonal).**

| Axis | Item |
|---|---|
| A | I notice fine distinctions — in sensations, words, situations. |
| S | My life holds stable forms: roles, routines, orders that persist. |
| D | There is movement: processes in my life start, develop, complete. |
| L | My views assemble into a consistent whole. |
| E | My inner states are vivid and distinctly felt. |
| O | I feel a source of strength not dependent on circumstances. |
| U | My experience gathers into one whole, not fragments. |

**The twenty-one coherence items (off-diagonal), by canonical name.**

| Cell | Name | Item |
|---|---|---|
| AS | Morphogenesis | What I distinguish crystallises into stable forms — habits, works, concepts. |
| AD | Actualization | Noticing something, I set it moving: distinctions become processes. |
| AL | Predication | I can render my distinctions in precise words and judgements. |
| AE | Apperception | What I perceive genuinely touches me; it enters my inner world. |
| AO | Spontaneity | New distinctions arise in me of themselves, unprompted. |
| AU | Differentiation | I see differences without losing the sense of the whole. |
| SD | Persistence | My forms survive change: structure holds through process. |
| SL | Nomos | My structures are not arbitrary; I see why they must be as they are. |
| SE | Representation | I hold a clear inner image of the structures of my life. |
| SO | Archetype | My stable forms feel rooted in something deeper than convenience. |
| SU | Symmetry | The parts of my life mirror one order; structure expresses wholeness. |
| DL | Regulation | My processes are governed: I can correct course by understanding. |
| DE | Affection | What happens moves me: process reaches feeling. |
| DO | Genesis | My activity springs from the source, not from pressure. |
| DU | Teleology | My changes are directed: movement serves the whole. |
| LE | Evidence | What I understand I also inwardly see: thought carries lived certainty. |
| LO | Grounding | My reasoning stands on ground; it is fed by the primary, not by air. |
| LU | Consistency | Taken whole, I do not contradict myself. |
| EO | Immanence | In the depth of inner experience I meet the source itself. |
| EU | Synthesis | My experiences integrate into the whole of who I am. |
| OU | Completeness | Source and whole coincide: nothing essential is left outside. |

Total time about seven minutes. For teams and organisations the same geometry is used with institutional items (the [σ-audit](/docs/applied/coherence-cybernetics/measurement#измерение-напряжений)).

## §3. Anchor II — the scoring model {#скоринг}

The Likert-to-$\Gamma$ scoring map is a **prospective empirical protocol `[Pr]`** whose calibration parameter $\beta$ is to be validated against independent psychometric criteria in V0-VAL ([07 §2](/docs/applied/console/roadmap-validation#v0)), not a canon-derived physical law. From the 28 raw responses $r$ (each in $\{0,1,2,3\}$) to a valid `gamma`:

1. **Populations.** Set raw diagonal $\tilde p_i = (r_i + \alpha)$ with Laplace smoothing $\alpha = 0.5$, then normalise to unit trace: $p_i = \tilde p_i / \sum_j \tilde p_j$. The trace constraint ($\sum_i p_i = 1$) maps seven independent ratings onto the simplex.
2. **Calibrated coherence magnitudes (preventing the all-3s pathology).** A naive mapping $\tilde m_{ij} = r_{ij}/3 \in [0,1]$ with $|\gamma_{ij}| = \tilde m_{ij}\sqrt{p_i p_j}$ has a fatal boundary pathology: when a maximally flourishing user answers all-3s ($r_i = 3, r_{ij} = 3$), uniform populations $p_i = 1/7$ combine with $\tilde m_{ij} = 1$ to produce the rank-1 pure state $\Gamma = \frac{1}{7}\mathbf 1\mathbf 1^\top$, giving $P = 1$ and $R = 1/(7P) = 1/7 < 1/3$ — absurdly classifying a maximally flourishing respondent as over-coherent/unconscious. To align flourishing self-report profiles with the viable conscious window $P \in (2/7, 3/7]$, $R \geq 1/3$, $\Phi \geq 1$, $D_{\mathrm{diff}}^{7D} \geq 2$, map item scores linearly in **coherence energy** with a calibrated ceiling $\beta$:

   $$\tilde m_{ij} = \beta\,\sqrt{\frac{r_{ij}}{3}}, \qquad |\gamma_{ij}| = \tilde m_{ij}\,\sqrt{p_i p_j}, \qquad \beta \in \bigl(1/\sqrt{6},\ 1/\sqrt{3}\bigr) \approx (0.408,\ 0.577).$$

   For uniform populations $p_i = 1/7$ and uniform $\tilde m_{ij} = c$, $P = (1 + 6c^2)/7$, so $P \in (2/7, 3/7] \iff c \in (1/\sqrt{6}, 1/\sqrt{3}]$. With the provisional default $\beta = 0.55$ (to be empirically calibrated in V0-VAL `[Pr]`):
   - **all-3s** ("almost always"): $P \approx 0.402 \in (2/7, 3/7]$, $R \approx 0.355 \geq 1/3$, $\Phi \approx 1.82 \geq 1$, $D_{\mathrm{diff}}^{7D} \approx 2.41 \geq 2$ (viable, high integration);
   - **all-2s** ("often"): $P \approx 0.316 \in (2/7, 3/7]$, $R \approx 0.452 \geq 1/3$, $\Phi \approx 1.21 \geq 1$, $D_{\mathrm{diff}}^{7D} \approx 2.33 \geq 2$ (viable, moderate integration);
   - **all-1s** ("sometimes"): $P \approx 0.229 < 2/7$, $\Phi \approx 0.61 < 1$ (below viability);
   - **all-0s** ("almost never"): $\Gamma = I/7$, $P = 1/7$, $\Phi = 0$, $R = 1$ (maximally mixed).
   The factor $\sqrt{p_i p_j}$ enforces the pairwise Cauchy–Schwarz bound so strong coherences cannot be claimed on weak populations.
3. **Phases.** Set $\theta_{ij} = 0$ (all coherences real and non-negative) — the honest default, because the questionnaire carries no phase information. The estimate is therefore a *real, non-negative* coherence matrix; its Gap map is flagged non-resolved.
4. **PSD projection.** Assemble $\Gamma$, then project to the PSD cone (clip negative eigenvalues, renormalise) exactly as the kernel does on ingestion. (Uniform profiles are already PSD with zero projection distance; heterogeneous off-diagonal patterns may require minor projection, recorded in `quality`.)
5. **Uncertainty.** `cov` is estimated from the instrument's test-retest statistics (population-level, refined per user as their own repeat sessions accumulate): each item's response variance propagates through steps 1–2 by the delta method. This is a *self-report* uncertainty, not a physical measurement covariance, and is labelled as such.

The output is a fully valid `GammaEstimate` with `anchor = AUTOEPHEMERIS`, marked `[Pr]` pending V0-VAL calibration, and honest about its phase-blindness and self-report covariance.

## §4. Anchor I — the measurement bridge {#измерение}

The empirical measurement bridge `[Pr]` builds on the corpus's [seven-channel embedding](/docs/applied/coherence-cybernetics/measurement#измерение-напряжений) and [empirical programme](/docs/consciousness/empirical/overview). Evidence $e$ is time-resolved signal: EEG (consumer dry-EEG or research/clinical high-density EEG), wrist heart-rate variability (HRV), actigraphy, and light-exposure logging.

:::note Prospective proxy status [Pr]
Consumer **wrist-HRV**, actigraphy, and **dry-EEG** mappings onto $\widehat\Gamma$ are a **prospective empirical proxy `[Pr]`**, *not* a validated physical readout of $\Gamma$. Sensor noise covariances are physically measured, but the biological observation bridge $\pi_{\mathrm{bio}}$ linking peripheral/consumer signals to $\Gamma$ requires independent calibration and held-out validation (V1-VAL, [07 §3](/docs/applied/console/roadmap-validation#v1)) before any readout may be interpreted as an established physical measurement of the state.
:::

**Purity axis — the keystone.** $P$ is estimated from the reconstruction $\widehat\Gamma$ (EEG/HRV through $\pi_{\mathrm{bio}}$, parameters frozen on wakefulness, no viability penalty in the estimator), not converted from PCI. Where TMS-EEG PCI is available (clinical), it supplies an independent verdict to compare with — the concordance of $\mathrm{Cons}(\widehat\Gamma)$ with $\mathrm{PCI}_{\max} > 0.31$, Cohen's $\kappa$ ([P8.4](/docs/applied/research/measurement-protocol#тестируемые-предсказания-p8)) — never a scale anchor for $P$; where only consumer dry-EEG or wrist-HRV is available, $\widehat P$ is a prospective proxy `[Pr]` with wider bounds and no PCI comparison.

**Coherences from cross-channel structure.** The seven axes map to seven signal channels (the σ-audit assignment); the coherence magnitudes and — here, unlike Anchor II — candidate **phases** are estimated from the cross-spectral density between channels at the integration timescale. Time-resolved signals *can* carry phase, which is why the measured anchor is the prospective path toward resolving the Gap map that the questionnaire cannot.

**Chronobiology (`T-257 [H]`).** Under the [coupling-channel hypothesis T-257](/docs/applied/research/gap-diagnostics) ([Status registry](/docs/reference/status-registry)), any claimed external entrainment requires an identifiable observation law and physical coupling model `[H]`. Light-exposure and sleep-timing logs feed the circadian/circalunar entrainment model as a testable physical bridge `[Pr]`; planetary/natal inputs lack any identified coupling model and are rejected at ingestion by the anchor-licence guardrail.

**Uncertainty.** `cov` comes from the estimator's signal error model (SNR, session length, sensor grade) — genuine signal-level covariance, paired with an explicit `[Pr]` bridge-validation flag until $\pi_{\mathrm{bio}}$ passes V1-VAL.

## §5. Anchor III — the oracle protocol {#оракул}

The **projective casting protocol `[I]`** is retained in full, with its epistemics stated: a draw is a **structured projective prompt**, not information about the world. Procedure: state the question in one sentence; draw one of the sixteen Hamming $H(7,4)$ signatures (or walk a three-step triadic chain from a random Fano line, e.g. *Meaning → Foundation → Action*); contemplate strictly inside the drawn frame for a fixed interval. The Console renders the frame and the contemplation scaffold, and stamps the output `anchor = ORACLE, std = null` — never a measurement, never a forecast. The value is the lens, and the lens is honest because its grammar matches the derived state space.

## §6. Fusion and the autoephemeris {#слияние}

When multiple evidence types are present (e.g. a self-audit plus a wearable), the Console fuses them by inverse-variance weighting on the shared sectors and keeps them separate on the disjoint ones: the wearable's phase-resolved Gap map is used where the questionnaire is blind; the questionnaire's fine population items refine the diagonal where the wearable is coarse. The fused estimate carries the *weakest* anchor tag present on each sector, so no sector is ever labelled more rigorous than its actual source.

The **autoephemeris** is the time series of estimates (§[07](/docs/applied/console/roadmap-validation) details the cadence): four or more repeats activate the [trajectory layer](/docs/applied/research/gap-diagnostics#прогностика) — trends per cell, mode identification, bifurcation warnings (accelerating loss of a stable profile = the saddle-node "dark night" signature), and archetype drift. Predictions, where the Console makes them, are statements about *this trajectory's* attractors — falsifiable per person, which is what no natal chart can be.

**Where this leads.** [04 · The use-case catalogue](/docs/applied/console/use-cases) configures these estimators and the kernel into named product features across every domain the instrument serves.
