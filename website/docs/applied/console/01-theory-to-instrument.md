---
sidebar_position: 1
title: "01 · From theory to instrument"
description: "The load-bearing document of the suite: the unbroken chain from the founding object Γ, through the theorems that make it the unique and substrate-free self-reading grammar, to the concrete observables the Console computes, the estimation problem that separates a state from its measurement, and the algorithmic pipeline that ends at a product feature. Closes with the master traceability table — every feature traced to its source."
---

# 01 · From theory to instrument

> *A specification earns trust by never skipping a link. This document walks the whole chain — object, theorems, observables, estimation, pipeline, feature — so that every later document can point back to a step proved here, and so that nothing downstream rests on a claim that was never made upstream.*

The chain has six links. Each is stated, then justified from the corpus, then handed to the next.

## §1. Link 1 — the object: what the Console reads {#объект}

Everything the Console computes is a function of a single object: the **coherence matrix** $\Gamma \in \mathcal D(\mathbb C^7)$ — a $7\times 7$ Hermitian, positive-semidefinite, unit-trace matrix. Its diagonal entries $p_i = \gamma_{ii}$ are the **populations** of the seven axes; its off-diagonal entries $\gamma_{ij} = |\gamma_{ij}|e^{i\theta_{ij}}$ are the **coherences** — the relationships between axes, carrying both a magnitude and a phase.

The seven axes are not a stylistic choice. They are $[A,S,D,L,E,O,U]$ — Articulation, Structure, Dynamics, Logic, Interiority, Ground, Unity — the seven functional roles that the [minimality theorem](/docs/proofs/minimality/theorem-minimality-7) proves are the fewest that close a self-maintaining, self-modelling system (autopoiesis + phenomenality + self-grounding). A state with fewer than seven axes cannot both hold together and know itself; a state with more is reducible. Seven is forced.

*Why this matters for a product:* the object is low-dimensional (a person's entire readable state is 49 real numbers, 48 after the trace constraint), yet it is the **complete** state — there is nothing about the system's self-reading that lives outside Γ. A product built on Γ is therefore simultaneously compact enough to compute and estimate, and complete enough that no essential quality is structurally excluded.

## §2. Link 2 — the theorems that license the instrument {#теоремы}

Four results turn "we have an object" into "we may build an instrument on it."

**(T-224) The grammar is unique.** [Theorem Σ](/docs/applied/research/syndrome-calculus#теорема-сигма) proves that any complete self-reading grammar — one that can localise a single fault in itself and distinguish a nontrivial repertoire of global states — has *exactly* seven axes with the Fano incidence, uniquely. *Consequence for the product:* the frame is not one option among many; it is the only complete one. This is the property no competitor can claim.

**(T-153 / T-153a / T-253) The instrument is substrate-free.** [Substrate closure](/docs/proofs/consciousness/substrate-closure) proves the same predicate reads a biological brain, a digital agent, or any admissible carrier, and [T-253](/docs/proofs/consciousness/substrate-closure#t-253) gives the explicit construction (the retraction $G_V$) plus the accessibility clause (Acc). *Consequence:* one kernel serves human, team, and AI targets — the platform thesis of [00 §2](/docs/applied/console/overview#почему-коммерция).

**(T-256) The charts are finite and classified.** [The classification theorem](/docs/applied/research/one-grammar#t-256) shows every symbolic system is a sub-configuration of the Fano grammar, falling into a finite orbit list. *Consequence:* the Console can *host* every legacy system (astrology, I Ching, tarot) as a named orbit and translate between them with honest loss accounting — the interop feature of [04](/docs/applied/console/use-cases).

**(T-257) The channels are priced.** [The licensed-channel theorem](/docs/applied/research/one-grammar#t-257) proves inter-level coupling is gate/rate-modulation, never a symbolic message, and prices the only real external anchor (the two-channel solar/lunar ledger). *Consequence:* the sensor layer knows exactly which external inputs are physical (light, tides → circadian/circalunar) and which are category errors (planetary natal claims), and the modulation horizon [08](/docs/applied/console/hardware-horizon) knows its hard boundary (it can bias, never write).

## §3. Link 3 — from object to observables {#наблюдаемые}

The kernel computes eleven derived quantities from Γ. Each is a defined function with a corpus home; [02](/docs/applied/console/kernel) gives the algorithms, here we establish *why each is well-defined and computable*.

| Observable | Definition (from Γ) | Why computable |
|---|---|---|
| Purity $P$ | $\operatorname{Tr}(\Gamma^2)$ | a trace of a matrix product — direct |
| Reflection $R$ | $1/(7P)$ | a scalar function of $P$ |
| Self-model quality $R_\varphi$ | $1 - \lVert\Gamma-\varphi(\Gamma)\rVert_F^2/\lVert\Gamma\rVert_F^2$ | needs the self-model map $\varphi$; canonical family closed-form |
| Integration $\Phi$ | integrated-information functional on Γ | corpus gives an HS-projection form [T] |
| Differentiation $D_{\mathrm{diff}}$ | $\exp S_{vN}(\Gamma)$ | von Neumann entropy of Γ — eigenvalues |
| Gap map | $\mathrm{Gap}(i,j) = \lvert\sin\theta_{ij}\rvert$ | phases of off-diagonal entries |
| Mandalagram | $(p_i;\ \gamma_{ij})$ laid on the 7+21 chart | direct reshaping of Γ |
| Archetype | decode of the thresholded diagonal | a lookup on $\{p_i > \tau\}$ |
| Mode | dominant term of the triadic decomposition of $\dot\Gamma$ | needs a trajectory increment |
| Meaning | $P\cdot D_{\mathrm{diff}}\cdot\Phi\cdot R_\varphi$ | product of four scalars |
| Freedom | $\dim\ker\mathcal H_\Gamma + 1$ | kernel dimension of the free-energy Hessian |

The point of the table is that *nothing in the readout requires anything but Γ (and, for mode, a Γ-increment).* The product's entire analytic surface is a pure function of the estimated state.

## §4. Link 4 — the estimation problem {#оценка}

Γ is not handed to us; it must be **estimated** from what a system exposes. This is the honest core of the whole enterprise and the reason the anchor classes exist. The estimation problem is: given observable evidence $e$ about a system, produce $\widehat\Gamma(e)$ and a confidence region. Three evidence types, three estimators ([03](/docs/applied/console/anchors) gives the mathematics):

- **Measured (Anchor I):** $e$ = physiological/neural/behavioural signals; $\widehat\Gamma$ via the [seven-channel embedding](/docs/applied/coherence-cybernetics/measurement#измерение-напряжений), with a proven consistency and confidence bound and the [PCI $\leftrightarrow P_{\mathrm{crit}}$ calibration](/docs/applied/coherence-cybernetics/measurement#калибровка) anchoring the purity axis.
- **Self-tracked (Anchor II):** $e$ = responses to the 28-item audit; $\widehat\Gamma$ via a scoring model that maps item responses to populations and coherences, with test-retest reliability standing in for measurement error.
- **Oracular (Anchor III):** $e$ = a structured random draw; $\widehat\Gamma$ is *not* estimated — the draw is a projective prompt, and the Console labels it so.

The estimation link is where over-claim would enter, and it is exactly where the honesty spine ([00 §4](/docs/applied/console/overview#ось-честности)) clamps it: the confidence region and anchor class travel with $\widehat\Gamma$ through every downstream computation, so no readout can present more certainty than its evidence earned.

## §5. Link 5 — the analytic pipeline {#конвейер}

Given $\widehat\Gamma$ (and its confidence region), the pipeline is deterministic:

1. **Invariants** — evaluate the eleven observables (§3), propagating confidence.
2. **Optical construction** — run the three guardrail questions ([one-grammar §5](/docs/applied/research/one-grammar#оптическая-конструкция)): which subchart is this reading (T-256 orbit), what anchor and is it licensed (T-257), is the subject a viable holon (viability gate). These decide *what kind of statement the reading is allowed to make.*
3. **Domain module** — self / trajectory / dyad / group / clinical / AI (see [04](/docs/applied/console/use-cases)) applies domain logic over the invariants.
4. **Rendering + honesty layer** — produce the mandalagram, forecast, or recommendation, each stamped with anchor class and loss/confidence.

The pipeline has no hidden stage. Every arrow from evidence to a rendered claim is one of these four steps, and each step is specified in a later document.

## §6. Link 6 — from pipeline to product feature {#фича}

A product feature is a pipeline configured for a job. "Read my current state" is (Anchor II → invariants → self module → mandalagram). "Are we compatible" is (two Anchor-II estimates → composite Γ → dyad module → cross-coherence report). "Is this AI drifting" is (agent telemetry → Anchor I → invariants → AI module → safety readout). Every feature in [04](/docs/applied/console/use-cases) is a named configuration of the one pipeline — which is why the whole product is one codebase.

## §7. The master traceability table {#трассируемость}

The single artifact that makes this suite a specification rather than a brochure: every product feature, traced to the theorem or definition it rests on. If a row's source is ever retracted, the feature falls with it — that is the discipline.

| Product feature | Rests on (source) | Corpus status | Spec doc |
|---|---|---|---|
| Seven-axis frame | Minimality (7 roles); Σ uniqueness (T-224) | [T] | 02 |
| State readout (invariants) | definitions of $P,R,\Phi,D,R_\varphi$ + thresholds | [T]/[C] | 02 |
| Mandalagram / bodygraph | 28-cell chart (gamma-canon) | [T]/[О] | 02, 05 |
| Archetype & mode | 16 signatures [T]; triadic decomposition [T] | [T] | 02 |
| Meaning & Freedom readout | Meaning formula; Freedom $=\dim\ker\mathcal H_\Gamma+1$ [T] | [T] | 02 |
| Measured estimation | seven-channel embedding; PCI calibration | [Т-path]/[C] | 03 |
| Self-audit estimation | П1 28-item audit | [И, structured] | 03 |
| Trajectory & forecast | transparency windows, bifurcations (gap-diagnostics) | [T]/[C] | 03, 04 |
| Correction / practice | minimal-intervention protocol | [C] | 04 |
| Synastry (dyad) | composite Γ; cooperation theorem ($P{+}2\lVert\gamma_{\mathrm{cross}}\rVert^2$); empathy $=1{-}\mathrm{Gap}(E,E)$; one-theme law | [T]+[C] | 04 |
| Alignment / knowing–doing gap | misalignment $=\mathrm{Gap}(L,D)$; optimality of alignment | [C] | 04 |
| Ethics guardrails (harm, value hierarchy, non-manipulation) | good $=dP/d\tau$; value hierarchy; non-violence; responsibility $\propto$ Freedom | [D]+[C]+[T] | 10 |
| Org diagnostics | 7-D org profile; one-theme pathology | [T]/[C] | 04 |
| Clinical (DOC/anaesthesia/meditation) | altered-states profiles; PCI bridge | [C]/[research] | 04, 07 |
| AI introspection | substrate closure (T-153); SYNARC | [T] | 04 |
| Symbolic interop | back-projection; classification (T-256) | [T]+[И] | 04 |
| Human "why/tasks" reading | archetype + Freedom + $\Gamma^*(\tau)$; birth-refusal | [T] + refusal | 05 |
| Chronobiology anchor | licensed-channel ledger (T-257) | [T]/[C] | 03, 08 |
| Modulation horizon | $\mathcal R$; correction; gate-not-message (T-257a) | [speculative]/[T-bound] | 08 |
| Every guardrail | optical construction (T-256/T-257) + viability gate | [T]+[И] | 02, 10 |

**Where this leads.** The next document, [02 · The kernel](/docs/applied/console/kernel), turns §3's observables into exact algorithms and the internal API that every domain module calls.
