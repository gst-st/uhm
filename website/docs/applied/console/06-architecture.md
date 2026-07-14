---
sidebar_position: 6
title: "06 · Technical architecture"
description: "How the kernel, the estimators, the domain modules, the honesty layer, and the data-custody layer compose into a deployable, multi-target system. Component boundaries, the data model, the service API surfaces, the local-first privacy engineering, the substrate-agnostic reuse across human/team/AI targets, observability, and the stack choices — each justified by a requirement traced to the theory or the ethics."
---

# 06 · Technical architecture

> *The architecture has one job beyond working: to make the dishonest output unbuildable and the private data un-leakable, because those two properties are the product's moat and its licence to exist. Everything else is ordinary engineering.*

## §1. Component map {#компоненты}

Five rings, inside-out, each depending only on those inside it:

1. **Kernel** ([02](/docs/applied/console/kernel)) — the substrate-agnostic invariant engine + optical-construction guardrails. Pure, deterministic, no I/O. One library, versioned, oracle-tested on every build.
2. **Estimators** ([03](/docs/applied/console/anchors)) — the three anchor pipelines (self-audit, measurement bridge, oracle) that produce `GammaEstimate`. Each declares its anchor class and covariance model. Pluggable: new sensors are new estimators, not kernel changes.
3. **Domain modules** ([04](/docs/applied/console/use-cases)) — self, trajectory, dyad, group, clinical, AI, interop. Thin logic over `kernel.evaluate`; each is a named pipeline configuration.
4. **Honesty layer** — a mandatory middleware between any module and any surface: it verifies that every emitted claim carries an anchor tag and a confidence/loss statement, and it downgrades or blocks claims that exceed their evidence (a phase-dependent Gap value off a phase-blind estimate is blocked, not shown faint). It is a *compiler-enforced* boundary, not a UI convention (§4).
5. **Surfaces** — apps (web/mobile), the practitioner/clinician console, the B2B/AI API, the research export. Surfaces render `Readout` + honesty metadata; they never compute invariants themselves.

Around all five: **data custody** (§5), cross-cutting.

## §2. The data model {#модель-данных}

Four core entities:

- **Subject** — a stable id for the read system (person, team, agent). Holds no raw evidence, only references. For teams/agents, a `composition` pointing to member Subjects (composite Γ is computed, not stored redundantly).
- **Evidence** — a raw input record (audit responses, a signal window, a legacy reading for back-projection), with source, timestamp, and the estimator that consumes it. Encrypted at rest; never leaves custody without explicit export.
- **GammaEstimate** — the output of an estimator (`gamma`, `cov`, `anchor`, `t`, `quality`). The immutable atom the kernel consumes.
- **Readout** — the kernel output plus honesty metadata and the domain module that produced it. Cacheable, reproducible from `(GammaEstimate, kernelVersion)`.

The **autoephemeris** is simply the ordered sequence of a Subject's `GammaEstimate`s; the trajectory module ([04 §1.2](/docs/applied/console/use-cases#индивид)) reads it. Reproducibility is a hard requirement: any Readout must be re-derivable from its inputs and the pinned kernel version, so a scientific claim ([04 §7](/docs/applied/console/use-cases#наука)) is auditable.

## §3. Service API surfaces {#api}

Two API tiers over the internal kernel API of [02 §5](/docs/applied/console/kernel#api):

- **Ingestion API** — `submitEvidence(subject, evidence)` → runs the matching estimator → stores `GammaEstimate`. Rejects unlicensed external inputs (planetary/natal) at the boundary per the [T-257 guardrail](/docs/applied/research/one-grammar#t-257).
- **Readout API** — `read(subject, module, options)` → assembles the estimate(s), calls `kernel.evaluate`, runs the domain module, passes through the honesty layer, returns `Readout` + metadata. Every response is self-describing: anchor class, confidence, loss, kernel version.

The **B2B/AI variant** is the same Readout API with a telemetry-adapter estimator — the platform property realised as an API, not a fork. One service, three markets.

## §4. The honesty layer, enforced in types {#честность}

The single most important architectural decision: honesty is a **type-level** property, not a runtime check that can be forgotten. `Readout` fields are parameterised by their anchor and confidence, and a surface cannot render a field without also consuming its provenance — the type of a "measured" readout and an "oracular" readout differ, so a UI that tried to show an oracle draw in the measurement view would not type-check. This turns the ethical requirement ([00 §4](/docs/applied/console/overview#ось-честности)) into a compile-time invariant. The moat is partly this: a competitor bolting honesty on as a disclaimer can be undercut; one where dishonesty is unrepresentable cannot casually regress.

## §5. Data custody and privacy engineering {#приватность}

Self-model data is the most intimate data class, and the [no-cloning results](/docs/consciousness/ethics-meaning/death-continuity#почему-нет-сосуществования) are the fitting reminder that a coherent self-state is uniquely non-fungible. Engineering commitments:

- **Local-first.** Evidence and estimates live on the user's device by default; the kernel runs client-side (it is small and pure). Cloud sync is opt-in, end-to-end encrypted, and carries only what the user exports.
- **Zero-knowledge server option.** For sync and B2B, the server stores ciphertext and computes on it only where the user grants; aggregate research data ([04 §7](/docs/applied/console/use-cases#наука)) is collected under explicit, revocable consent and differential-privacy noise.
- **No dark patterns.** The [value-consciousness](/docs/consciousness/ethics-meaning/value-consciousness#определение-благо) harm definition is a product rule with a formula behind it: the Console must not engineer engagement by driving a user's $dP/d\tau < 0$ — degrading viability, or the higher-tier values $\Phi$/$R_\varphi$, through manufactured anxiety. Retention comes from usefulness, not manufactured need — the anti-astrology stance extends to the business model.

## §6. Substrate-agnostic reuse {#переиспользование}

The kernel never inspects substrate beyond the anchor tag ([02 §5](/docs/applied/console/kernel#api)); the estimators are the only substrate-aware components. Adding a target (a new wearable, a new AI framework) is adding an estimator that outputs `GammaEstimate` — the kernel, honesty layer, and domain modules are untouched. This is why one team maintains human, team, and AI products: the surface area that differs per target is a thin estimator, and the expensive, correctness-critical core is shared and shared-tested.

## §7. Stack and deployment {#стек}

Justified by requirements, not fashion:

- **Kernel:** a small, portable numerics library (the eleven routines are fixed-size linear algebra). A single reference implementation compiled to native + WebAssembly so the *identical* kernel runs on device, in browser, and server-side — reproducibility demands one implementation, not three.
- **Estimators:** language per source (signal DSP where the sensors live; lightweight scoring on device for the audit).
- **Surfaces:** web + mobile client rendering `Readout`; a practitioner console; a documented API for B2B.
- **Deployment:** client-first; optional encrypted sync; research pipeline isolated and consent-gated.
- **Observability:** every Readout logs its kernel version, anchor classes, and guardrail verdicts (never the private evidence) — enough to audit correctness and honesty, nothing that compromises custody.

## §8. What the architecture guarantees {#гарантии}

Three invariants the design makes structural rather than aspirational: **honesty** (dishonest output is untyped, §4), **privacy** (raw evidence is local-first and non-fungible, §5), and **reproducibility** (every claim re-derives from inputs + pinned kernel, §2). These three are the technical form of the project's promise; the rest of the stack serves them.

**Where this leads.** [07 · Roadmap and validation](/docs/applied/console/roadmap-validation) sequences the build and specifies, per stage, the empirical protocol that turns each layer from `[design]` into confirmed.
