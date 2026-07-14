---
sidebar_position: 7
title: "07 · Roadmap and validation"
description: "The build sequence, from something empirically validatable today to the far horizon, with the per-stage validation protocol that turns each layer from design into confirmed. Milestones, deliverables, the empirical study tied to each corpus prediction, success metrics and KPIs, and the data strategy that makes the product and the science the same activity."
---

# 07 · Roadmap and validation

> *Start with what can be validated now, and let every next layer be earned by evidence rather than ambition. Each stage ships a product and runs a study; the study is what licenses the next stage's claims.*

## §1. Principle: crawl by validatability {#принцип}

The sequence is ordered by *(validatable now × market pull × build cost)*, not by ambition. A layer is not promoted from `[design]`/`[research]` to confirmed until its validation protocol passes. This discipline is the difference between an instrument and a horoscope with a nicer UI, and it is also the fundraising story: each stage de-risks the next with data.

## §2. V0 — Crawl: the self-audit instrument {#v0}

**Deliverable.** Pure-software product: the [28-item audit](/docs/applied/console/anchors#инструмент) → `GammaEstimate` (Anchor II) → full kernel readout, mandalagram, archetype, mode, and the autoephemeris once repeats accumulate. Consumer surfaces: self-read ([04 §1.1](/docs/applied/console/use-cases#индивид)), honest oracle ([04 §5.2](/docs/applied/console/use-cases#созерцание)), back-projection onboarding ([04 §9.1](/docs/applied/console/use-cases#интероп)). No hardware.

**Validation protocol (V0-VAL).**
- *Convergent validity:* correlate the seven populations and the block scores against Big Five, well-being (e.g. WEMWBS), and integration/differentiation instruments on a recruited sample; pre-register expected correspondences.
- *Reliability:* two-week test-retest on the 28 items; target ICC in the accepted range for trait instruments, lower for state-sensitive cells (expected and interpreted).
- *Structural prediction — the theory's own:* the corpus predicts coherences *within* a [Fano triad](/docs/core/structure/symbolic-systems#структурный-анализ) cluster more tightly than across triads (a self-report analog of F-Gap-2). Test by confirmatory factor analysis: does the 7-triad block structure fit better than random tripartitions? A pass is direct evidence *for the frame itself*, not just the instrument.

**Success metrics.** Instrument validity thresholds met; the triad-clustering prediction confirmed at pre-registered significance; retention of the self-read loop above a set weekly-active bar. **Gate to V1:** V0-VAL passed and a user base large enough to power the neural study.

## §3. V1 — Walk: the measurement bridge {#v1}

**Deliverable.** The [measurement anchor](/docs/applied/console/anchors#измерение): consumer EEG + HRV + actigraphy → a genuinely measured `GammaEstimate` with real covariance and a resolved Gap map; the chronobiology channel (solar/lunar entrainment) from light/sleep logs.

**Validation protocol (V1-VAL) — the corpus's sharpest test.**
- *The keystone:* confirm the [F-Neural prediction](/docs/reference/falsifiability) — that the $P_{\mathrm{crit}} = 2/7 \leftrightarrow \mathrm{PCI} = 0.31$ calibration holds on independent data across arousal states (wake / drowsy / sleep). This is the single result that moves the clinical case ([04 §4](/docs/applied/console/use-cases#клиника)) from `[research]` toward `[medical]`.
- *Cross-anchor agreement:* where a user has both a self-audit and a wearable, the shared sectors (populations, coherence magnitudes) should agree within their stated confidence — a direct check that the two anchors estimate the same object.
- *Chronobiology:* circadian/circalunar modulation of $P$ should be detectable and phase-locked to the licensed drivers, and *absent* for any planetary index (a negative control that, if it ever came back positive, would falsify [T-257](/docs/applied/research/one-grammar#t-257)).

**Success metrics.** PCI calibration reproduced within CI; cross-anchor agreement within bounds; the planetary negative control stays null. **Gate to V2:** V1-VAL passed with clinical-grade signal on at least one partnered device.

## §4. V2 — Run: dyad, group, clinical, interop {#v2}

**Deliverable.** Composite-Γ synastry ([04 §2](/docs/applied/console/use-cases#диада)), org mandalagram and pathology detection ([04 §3](/docs/applied/console/use-cases#коллектив)), the regulated clinical modules ([04 §4](/docs/applied/console/use-cases#клиника)) built with clinical partners, and full symbolic interop.

**Validation protocol (V2-VAL).**
- *Dyad:* the jam pattern (two circuits sharing two themes) predicts reported recurring conflict above chance; composite synastry predicts relationship-satisfaction measures.
- *Org:* the org profile tracks team-performance/engagement metrics; a detected jam precedes an escalation.
- *Clinical:* against gold-standard DOC/anaesthesia-depth references, under a registered clinical study and the appropriate regulatory pathway ([10](/docs/applied/console/ethics-governance)).

**Success metrics.** Each domain's predictive claim confirmed under pre-registration; clinical module meeting the regulatory bar for its class.

## §5. First B2B in parallel — AI introspection {#b2b}

Not a roadmap stage but a parallel track from early on, because it reuses the kernel with a telemetry estimator and sells to a well-capitalised buyer with no consumer-scale UX needed. **Deliverable:** the [agent-introspection API](/docs/applied/console/use-cases#ии) ($P,R,\Phi$ on an agent over training/inference). **Validation:** the invariants flag known failure episodes (the hallucinating-LLM case) earlier or more reliably than existing metrics. This track can fund the consumer roadmap.

## §6. Horizon — hardware {#горизонт}

Sequenced in [08](/docs/applied/console/hardware-horizon): measurement gadgets (tighter sensors → tighter $\widehat\Gamma$) are a continuation of V1; directed modulation is a research frontier gated by the ethics of [10](/docs/applied/console/ethics-governance) and bounded by the theory itself (gate, not message — [T-257(a)](/docs/applied/research/one-grammar#t-257)). No modulation claim ships without its own validation protocol, defined when the science supports writing one.

## §7. Data strategy — product and science as one activity {#данные}

Every consented session is a data point for the validation studies. This is the structural advantage from [00 §2](/docs/applied/console/overview#почему-коммерция): a growing user base *is* the population sample that confirms or refutes the corpus predictions. Consent is explicit and revocable; research data is aggregated with differential privacy; and the pre-registration discipline applies to product-derived studies exactly as to lab ones — otherwise the science self-corrupts into marketing.

## §8. KPI summary {#kpi}

| Stage | Product KPI | Scientific KPI | Gate |
|---|---|---|---|
| V0 | weekly-active, back-projection funnel conversion | instrument validity + triad-clustering (F-Gap-2 analog) | studies pass, base sufficient |
| V1 | measured-anchor adoption | PCI calibration reproduced; planetary control null | clinical-grade signal on a device |
| V2 | B2B seats; clinical pilots | domain predictions confirmed; regulatory bar met | per-domain pre-registration passed |
| B2B-AI | enterprise contracts | early-warning lift over baselines | — (parallel) |
| Horizon | — | modulation protocol defined only when writable | ethics + theory bound |

**Where this leads.** [08 · The hardware horizon](/docs/applied/console/hardware-horizon) specifies the sensor and modulation staging and the hard boundary the theory places on what hardware may do.
