---
sidebar_position: 3
title: "03 · Anchors and estimation"
description: "How a real GammaEstimate is produced from evidence. The full 28-item self-audit instrument reproduced, the scoring model that maps responses to a coherence matrix (populations, magnitudes, and the honest phase-blindness), the measurement-bridge mathematics for the neural/physiological path with the PCI calibration, and the oracle protocol — each with its estimator, its uncertainty model, and its declared loss."
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

The instrument is the [П1 28-cell audit](/docs/applied/research/gamma-canon#п1-картирование). Each item is rated $0$–$3$ (almost never / sometimes / often / almost always); first responses are better data than considered ones.

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

From the 28 raw responses $r$ (each in $\{0,1,2,3\}$) to a valid `gamma`:

1. **Populations.** Set raw diagonal $\tilde p_i = (r_i + \alpha)$ with a small Laplace smoothing $\alpha$, then normalise to unit trace: $p_i = \tilde p_i / \sum_j \tilde p_j$. The trace constraint (a state has $\sum p_i = 1$) is what turns seven independent ratings into a point on the simplex.
2. **Coherence magnitudes.** Map each coherence item to a raw magnitude $\tilde m_{ij} = r_{ij}/3 \in [0,1]$, then scale so the off-diagonal block is consistent with the populations: the coherence between $i$ and $j$ cannot exceed $\sqrt{p_i p_j}$ (Cauchy–Schwarz on a PSD matrix), so $|\gamma_{ij}| = \tilde m_{ij}\cdot\sqrt{p_i p_j}$. This bound is not a fudge — it is the PSD constraint, and it makes strong-coherence claims on weak populations automatically impossible, matching intuition (you cannot have intense S–E coherence if neither Structure nor Interiority is present).
3. **Phases.** Set $\theta_{ij} = 0$ (all coherences real and non-negative) — the honest default, because the questionnaire carries no phase information. The estimate is therefore a *real, non-negative* coherence matrix; its Gap map is flagged non-resolved.
4. **PSD projection.** Assemble $\Gamma$, then project to the PSD cone (clip negative eigenvalues, renormalise) exactly as the kernel does on ingestion.
5. **Uncertainty.** `cov` is estimated from the instrument's test-retest statistics (population-level, refined per user as their own repeat sessions accumulate): each item's response variance propagates through steps 1–2 by the delta method. This is a *self-report* uncertainty, not a measurement one, and is labelled as such.

The output is a fully valid `GammaEstimate` with `anchor = AUTOEPHEMERIS`, honest about its phase-blindness and its self-report covariance.

## §4. Anchor I — the measurement bridge {#измерение}

The hard-science path uses the corpus's [seven-channel embedding](/docs/applied/coherence-cybernetics/measurement#измерение-напряжений). Evidence $e$ is time-resolved signal: EEG (consumer or research grade), heart-rate variability, actigraphy, and light-exposure logging.

**Purity axis — the keystone.** The [PCI calibration](/docs/applied/coherence-cybernetics/measurement#калибровка) fixes the scale: perturbational complexity index $\mathrm{PCI} = 0.31$ maps to $P_{\mathrm{crit}} = 2/7$, with wakefulness at $\mathrm{PCI}\approx0.44$ and REM at $\approx0.32$. Where TMS-EEG PCI is available (clinical), it directly anchors $P$; where only resting EEG is available (consumer), a validated proxy (spectral/entropy complexity calibrated against the PCI ladder) estimates $P$ with wider bounds.

**Coherences from cross-channel structure.** The seven axes map to seven signal channels (the σ-audit assignment); the coherence magnitudes and — here, unlike Anchor II — the **phases** are estimated from the cross-spectral density between channels at the integration timescale. Time-resolved signals *can* carry phase, which is why the measured anchor resolves the Gap map that the questionnaire cannot.

**Chronobiology.** The [T-257 licensed ledger](/docs/applied/research/one-grammar#t-257) admits exactly two external drivers — solar (circadian/circannual) and lunar (circatidal/circalunar). Light-exposure and sleep-timing logs feed the entrainment model; no planetary input is accepted (it is rejected at ingestion by the anchor-licence guardrail). This is the *only* place the Console reads the sky, and it reads the two channels physics licenses, nothing more.

**Uncertainty.** `cov` comes from the estimator's own error model (signal SNR, session length, sensor grade) — a genuine measurement covariance, so Anchor-I readouts carry real confidence intervals and the honesty layer renders them as measured.

## §5. Anchor III — the oracle protocol {#оракул}

The [П4 casting protocol](/docs/applied/research/gamma-canon#п4-оракул) is retained in full, with its epistemics stated: a draw is a **structured projective prompt**, not information about the world. Procedure: state the question in one sentence; draw one of the sixteen archetypes (or walk a three-step triadic chain from a random line, e.g. *Meaning → Foundation → Action*); contemplate strictly inside the drawn frame for a fixed interval. The Console renders the frame and the contemplation scaffold, and stamps the output `anchor = ORACLE, std = null` — never a measurement, never a forecast. The value is the lens, and the lens is honest because its grammar matches the derived state space.

## §6. Fusion and the autoephemeris {#слияние}

When multiple evidence types are present (e.g. a self-audit plus a wearable), the Console fuses them by inverse-variance weighting on the shared sectors and keeps them separate on the disjoint ones: the wearable's phase-resolved Gap map is used where the questionnaire is blind; the questionnaire's fine population items refine the diagonal where the wearable is coarse. The fused estimate carries the *weakest* anchor tag present on each sector, so no sector is ever labelled more rigorous than its actual source.

The **autoephemeris** is the time series of estimates (§[07](/docs/applied/console/roadmap-validation) details the cadence): four or more repeats activate the [trajectory layer](/docs/applied/research/gap-diagnostics#прогностика) — trends per cell, mode identification, bifurcation warnings (accelerating loss of a stable profile = the saddle-node "dark night" signature), and archetype drift. Predictions, where the Console makes them, are statements about *this trajectory's* attractors — falsifiable per person, which is what no natal chart can be.

**Where this leads.** [04 · The use-case catalogue](/docs/applied/console/use-cases) configures these estimators and the kernel into named product features across every domain the instrument serves.
