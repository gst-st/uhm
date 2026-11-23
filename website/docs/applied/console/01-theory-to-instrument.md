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

The seven axes are not a stylistic choice. They are $[A,S,D,L,E,O,U]$ — Articulation, Structure, Dynamics, Logic, Interiority, Ground, Unity — the seven functional roles isolated by the [minimality analysis](/docs/proofs/minimality/theorem-minimality-7) and [Theorem Σ (T-224)](/docs/applied/research/syndrome-calculus#теорема-сигма) as the smallest self-diagnosing grammar supporting single-fault localisation and a nontrivial state repertoire.

*Why this matters for a product:* the object is low-dimensional (a person's entire readable state is 49 real numbers, 48 after the trace constraint), yet it is compact enough to compute and estimate while carrying both diagonal populations and pairwise coherences.

## §2. Link 2 — the theorems that license the instrument {#теоремы}

Four corpus results (three theorems/constructions and one explicit modelling hypothesis) turn "we have an object" into "we may build an instrument on it."

**(T-224 [T]) The grammar is unique.** [Theorem Σ](/docs/applied/research/syndrome-calculus#теорема-сигма) proves that any complete self-reading grammar — one that can localise a single fault in itself and distinguish a nontrivial repertoire of global states — has *exactly* seven axes with the Fano incidence and the 16-codeword Hamming $H(7,4)$ grammar, uniquely up to relabelling. *Consequence for the product:* the frame is not one option among many; it is the unique minimal single-fault-diagnosable grammar.

**(T-153 [D]/[C] / T-153a [T] / T-253 [T]+[C]) The instrument is substrate-free.** [Substrate closure](/docs/proofs/consciousness/substrate-closure) shows the same formal predicate reads a biological brain, a digital agent, or any admissible carrier once an observation bridge is calibrated, and [T-253](/docs/proofs/consciousness/substrate-closure#t-253) gives the explicit retraction $G_V$ modulo the accessibility clause (Acc). *Consequence:* one kernel serves human, team, and AI targets — the platform thesis of [00 §2](/docs/applied/console/overview#почему-коммерция).

**(T-256 [T]+[I]) Axis-subset orbits are finite and classified.** Under the finite Fano collineation group $\mathrm{GL}(3,2)$ ([Mathematical kernel](/docs/reference/mathematical-kernel), [Status registry](/docs/reference/status-registry)), nonempty subsets of the seven axes partition into **nine nonempty orbit types** `[T]`. Mapping legacy symbolic systems (astrology, I Ching, tarot) onto these subsets is an interpretation `[I]`. *Consequence:* the Console can *host* legacy charts as named sub-configurations with honest loss accounting — the interop feature of [04](/docs/applied/console/use-cases).

**(T-257 [H]) The coupling-channel hypothesis.** [Gap diagnostics](/docs/applied/research/gap-diagnostics) and the [Status registry](/docs/reference/status-registry) frame rate modulation and viability gating as one admissible inter-holon control model rather than symbolic state-writing, while noting that any claimed external forcing (circadian/circalunar entrainment or ephemeris signals) requires an identifiable observation law and physical coupling model `[H]`. *Consequence:* the sensor layer accepts only physically modelled inputs (light, sleep timing, physiological signals), rejects planetary natal claims for lack of any identified observation bridge, and keeps the modulation horizon ([08](/docs/applied/console/hardware-horizon)) within an explicit biasing model rather than state-writing.

## §3. Link 3 — from object to observables {#наблюдаемые}

The kernel computes eleven derived quantities from $\Gamma$. Each is a defined function with a corpus home; [02](/docs/applied/console/kernel) gives the algorithms, here we establish *why each is well-defined and computable*.

| Observable | Definition (from $\Gamma$) | Why computable / scope |
|---|---|---|
| Purity $P$ | $\operatorname{Tr}(\Gamma^2)$ | unitary-invariant matrix trace `[T]` |
| Reflection $R$ | $1/(7P)$ | unitary-invariant scalar function of $P$ `[D]` |
| Self-model quality $R_\varphi$ | $1 - \lVert\Gamma-\varphi(\Gamma)\rVert_F^2/\lVert\Gamma\rVert_F^2$ | closed form for linear anchor-mixing $\varphi_{\mathrm{lin}}$ (`T-249 [T]`) |
| Integration $\Phi$ | $(P - P_{\mathrm{diag}})/P_{\mathrm{diag}}$, $P_{\mathrm{diag}}=\sum_i\gamma_{ii}^2$ | fixed-frame ratio (`T-129 [D]/[T]`); no bipartitions in prime $d=7$ |
| Differentiation $D_{\mathrm{diff}}^{7D}$ | $1 + 6\,\mathrm{Coh}_E(\Gamma)$ | 7D native proxy `[D]` (spectral $\exp S_{vN}(\rho_E)$ requires extended $\mathcal H_E$) |
| Gap map | $\mathrm{Gap}(i,j) = \lvert\sin\theta_{ij}\rvert$ | fixed-frame phases of off-diagonal entries `[D]` |
| Mandalagram | $(p_i;\ \gamma_{ij})$ laid on the 7+21 chart | direct reshaping of $\Gamma$ `[D]` |
| Archetype | nearest $H(7,4)$ codeword of $\{p_i > \tau\}$ | syndrome decode to 16 Hamming codewords (`T-224 [T]`) |
| Mode | dominant term in chosen 3-part grouping of $\dot\Gamma$ | requires a trajectory increment and specified generator grouping `[D]` |
| Meaning | $P\cdot D_{\mathrm{diff}}^{7D}\cdot\Phi\cdot R_\varphi$ | chosen composite indicator `[D]` (not a unique canonical scalar) |
| Freedom | $\mathrm{Freedom}_V(\Gamma_*)=1+\dim\ker\operatorname{Hess}_{\Gamma_*}V$ | chosen Hessian score `[D]` for a supplied $C^2$ potential $V$ (`T-89 [T]` under Morse–Bott) |

The point of the table is that *nothing in the readout requires hidden metaphysical inputs beyond $\Gamma$ (plus a trajectory increment for mode and a declared potential $V$ for the Hessian score).* Every quantity carries its exact scope — unitary-invariant vs fixed-frame, theorem vs definition.

## §4. Link 4 — the estimation problem {#оценка}

Γ is not handed to us; it must be **estimated** from what a system exposes. This is the honest core of the whole enterprise and the reason the anchor classes exist. The estimation problem is: given observable evidence $e$ about a system, produce $\widehat\Gamma(e)$ and a confidence region. Three evidence types, three estimators ([03](/docs/applied/console/anchors) gives the mathematics):

- **Measured (Anchor I).** Freeze the reconstruction before comparing latent-model verdicts to observed outcomes. PCI and purity need independent calibration.
- **Self-tracked (Anchor II):** $e$ = responses to the 28-item audit; $\widehat\Gamma$ via a scoring model that maps item responses to populations and coherences, with test-retest reliability standing in for measurement error.
- **Oracular (Anchor III):** $e$ = a structured random draw; $\widehat\Gamma$ is *not* estimated — the draw is a projective prompt, and the Console labels it so.

The estimation link is where over-claim would enter, and it is exactly where the honesty spine ([00 §4](/docs/applied/console/overview#ось-честности)) clamps it: the confidence region and anchor class travel with $\widehat\Gamma$ through every downstream computation, so no readout can present more certainty than its evidence earned.

## §5. Link 5 — the analytic pipeline {#конвейер}

Given $\widehat\Gamma$ (and its confidence region), the pipeline is deterministic:

1. **Invariants** — evaluate the eleven observables (§3), propagating confidence.
2. **Optical construction** — run the three guardrail checks ([Mathematical kernel](/docs/reference/mathematical-kernel), [Reconstruction identifiability](/docs/applied/research/reconstruction-identifiability)): which sector/orbit does this reading actually resolve (`T-256 [T]+[I]`), is any external anchor physically modelled (`T-257 [H]`), and is the subject inside the viability window (`P > 2/7`, viability gate). These decide *what kind of statement the reading is allowed to make.*
3. **Domain module** — self / trajectory / dyad / group / clinical / AI (see [04](/docs/applied/console/use-cases)) applies domain logic over the invariants.
4. **Rendering + honesty layer** — produce the mandalagram, forecast, or recommendation, each stamped with anchor class and loss/confidence.

The pipeline has no hidden stage. Every arrow from evidence to a rendered claim is one of these four steps, and each step is specified in a later document.

## §6. Link 6 — from pipeline to product feature {#фича}

A product feature is a pipeline configured for a job. "Read my current state" is (Anchor II → invariants → self module → mandalagram). "Are we compatible" is (two Anchor-II estimates → composite Γ → dyad module → cross-coherence report). "Is this AI drifting" is (agent telemetry → Anchor I → invariants → AI module → safety readout). Every feature in [04](/docs/applied/console/use-cases) is a named configuration of the one pipeline — which is why the whole product is one codebase.

## §7. The master traceability table {#трассируемость}

The single artifact that makes this suite a specification rather than a brochure: every product feature, traced to the theorem or definition it rests on. If a row's source is ever retracted, the feature falls with it — that is the discipline.

| Product feature | Rests on (source) | Corpus status | Spec doc |
|---|---|---|---|
| Seven-axis frame | Diagnosability rigidity: Theorem Σ (`T-224`) | [T] | 02 |
| State readout (invariants) | definitions of $P,R,\Phi,D_{\mathrm{diff}}^{7D},R_\varphi$ (`T-129`, `T-249`) + thresholds | [T]/[D] | 02 |
| Mandalagram / bodygraph | 28-cell coherence chart (7 populations + 21 channels) | [D] | 02, 05 |
| Archetype & mode | 16 Hamming $H(7,4)$ codewords (`T-224 [T]`); chosen 3-part dynamical grouping `[D]` | [T]/[D] | 02 |
| Meaning & Freedom readout | Selected composite meaning indicator and Hessian score (`T-89`), with explicit potential/domain and empirical validation | [D]/[I]/[H] | 02 |
| Measured estimation | seven-channel embedding (`[Pr]`); verdict concordance with PCI ($\kappa$) | [Pr]/[C] | 03 |
| Self-audit estimation | 28-item calibrated self-audit (`[Pr]`) | [Pr]/[I] | 03 |
| Trajectory & forecast | transparency windows, bifurcations ([Gap diagnostics](/docs/applied/research/gap-diagnostics)) | [H]/[C] | 03, 04 |
| Correction / practice | minimal-intervention protocol | [C]/[H] | 04 |
| Cooperation and relationship reflection | Typed joint-state data and independent outcomes; `T-77` is a pinching identity, not an empathy theorem | [D]/[H]; identity [T] | 04 |
| Alignment / knowing–doing gap | Observed commitments and actions; a phase proxy requires independent validation | [D]/[H] | 04 |
| Ethical protections and non-manipulation | Explicit normative context, consent and protection constraints; conditional preservation certificates | [I]/[D]; certificates [T] | 10 |
| Org diagnostics | 7-D org profile; structural overlap heuristics | [D]/[H] | 04 |
| Clinical (DOC/anaesthesia/meditation) | altered-states profiles; PCI verdict concordance | [C]/[Pr] | 04, 07 |
| AI introspection | substrate closure (`T-153`, `T-153a`, `T-253`); SYNARC | [D]/[C]/[T] | 04 |
| Symbolic interop | back-projection; 9 nonempty Fano collineation orbits (`T-256`) | [T]+[I] | 04 |
| Human "why/tasks" reading | archetype + Freedom (`T-89`) + $\Gamma^*(\tau)$; birth-refusal | [D]/[I] + refusal | 05 |
| Chronobiology anchor | external-coupling model (`T-257`) | [H]/[Pr] | 03, 08 |
| Modulation horizon | $\mathcal R$; correction; rate/gate model (`T-257`) | [speculative]/[H] | 08 |
| Every guardrail | orbit classification (`T-256`), channel hypothesis (`T-257`), and viability gate | [T]/[H]/[I] | 02, 10 |

**Where this leads.** The next document, [02 · The kernel](/docs/applied/console/kernel), turns §3's observables into exact algorithms and the internal API that every domain module calls.
