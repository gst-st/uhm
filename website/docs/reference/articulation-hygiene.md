---
title: Articulation Hygiene (operator+fixpoint protocol)
sidebar_label: Articulation Hygiene
sidebar_position: 8
---

# Articulation Hygiene

## Purpose

This document fixes the **operator-factorization protocol** for all "self-X" / "auto-X" / "само-X" constructions in the UHM corpus. The protocol is not a stylistic preference but a **structural invariant**, established by theorem **NO-19 (Articulation Hygiene)** in Noesis ([diakrisis.gst.st/11-noesis/07-theorems](http://diakrisis.gst.st/11-noesis/07-theorems)). The protocol is mandatory for every articulation passing the Noesis core pipeline (SMT → Axi → AFN-T → **Hygiene**).

## Principle

Any "self-X" construction in an articulation is **underdetermined** without an explicit operator-factorization. It does not specify:

- *which* operator $\Phi$ performs the recursive/reflexive action,
- *which* trajectory $\Phi^\kappa$ (ordinal $\kappa$) generates the construction,
- *which* terminal/fixed object $t$ closes it.

**Hygiene requirement**: for each surface-level "self-X" in an articulation, an explicit triple $(\Phi, \Phi^\kappa, t)$ must be defined. Without such a triple, the articulation is rejected at the Hygiene stage of the pipeline.

## Philosophical context

The protocol formalises an observation by E. Churilov (anticomplexity.org) within the metastemological programme: "self-"-constructions are syntactically suspicious because they conflate the describing and described positions in a single sign. The resolution is to separate these positions explicitly via operator + trajectory + terminal.

Within the [Diakrisis](http://diakrisis.gst.st) / [Актика](http://diakrisis.gst.st/actic) framework, this discipline is already built into the canonical primitive (accessible endofunctors $\mathsf{M}$ and $\mathsf{A}$, ordinal $\nu/\varepsilon$-stratification, $\mathrm{Fix}$-sets). NO-19 elevates it from an implicit formal property to an explicit invariant of the [Noesis](http://diakrisis.gst.st/noesis) core pipeline.

## Canonical factorisation table

For each recurring "self-X" construction in UHM:

| Surface form | Operator $\Phi$ | Trajectory $\Phi^\kappa$ | Terminal $t$ | Source theorem |
|---|---|---|---|---|
| self-model / самомодель | $\varphi: \mathrm{D}(\mathbb{C}^7) \to \mathrm{D}(\mathbb{C}^7)$ | $\varphi^\kappa$ on states | $\rho^* = \varphi(\Gamma)$ | T-96 |
| self-modelling / самомоделирование | $\varphi$ — categorical map (functor) | iteration in Lindblad dynamics | $\rho^* \in \mathrm{eq}(\mathrm{id}, \varphi)$ | T-96 + T-39a |
| autopoiesis / автопоэзис | $\mathsf{A}^\mathrm{act}$ (activation) on AC-side | $\mathsf{A}^{\omega^2}$-iteration | $\varepsilon \in \mathrm{Fix}(\mathsf{A}^{\omega^2})$ | 113.T (Diakrisis) |
| self-observation / самонаблюдение | terminal coalgebra $\Gamma \to F(\Gamma)$ for $F = \varphi$ + reflection-measure $R$ | unfolding of the coalgebra | $\nu F$ — terminal coalgebra; $R \geq 1/3$ | T-126 + T-96 |
| self-reference / самореференция | endomorphism $h:Y\to Y$ and a weakly point-surjective map $X\to Y^X$ | diagonal construction | a fixed point of $h$ when the surjectivity premise holds; stratification restricts the construction | [Diakrisis, 87.T](https://diakrisis.gst.st/06-limits/06-absoluteness), [Diakrisis, 105.T](https://diakrisis.gst.st/06-limits/10-maximality-theorems) |
| self-consistency / самосогласованность | equivalence operator $\varphi \simeq \mathrm{id}$ | — (point-level) | equaliser $\rho^* = \varphi(\Gamma)$ | T-96 |
| self-awareness / самосознание | reflexive measure $R = 1/(7P)$ + Φ-integration | (P, R, Φ, D)-threshold | consciousness predicate $P > 2/7 \wedge R \geq 1/3 \wedge \Phi \geq 1 \wedge D \geq 2$ | T-96 + T-126 + T-129 + T-151 |
| self-closure / самозамыкание | $\mathsf{M}^\kappa$-iteration on the articulation side | trajectory $\alpha \mapsto \mathsf{M}(\alpha) \mapsto \mathsf{M}^2(\alpha) \mapsto \ldots$ | $\alpha \in \mathrm{Fix}(\mathsf{M})$ | 04.T1, Axi-7 |
| self-amplification / самоусиление | positive feedback $\Psi$ | $\Psi^k$-iteration | threshold activation value | Diakrisis §kinetic (context) |

### What is **not** subject to replacement (standard technical terms)

- **self-adjoint** — fixed mathematical term denoting a Hermitian operator, not a reflexive turn of phrase.
- **self-attention** (the Transformer mechanism) — an ML term, preserved as is.
- **self-assembly** (in chemistry / nanotechnology) — a physical term, preserved as is.
- **self-similarity** (fractal) — a mathematical term, preserved as is.

Criterion: if "self-" expresses a **property of a map or object** definable independently of the reflexive interpretation, the term is preserved unchanged.

## Application to UHM

### Tier 1: conceptual files (prose rewrite)

Files where "self-X" appears in a descriptive sense are **fully** subject to replacement per the table above. High-priority targets:

- `/consciousness/foundations/self-observation.md` — canonical document, refactored first (see §"Applied factorisation" below).
- `/proofs/categorical/formalization-phi.md` — formalisation of $\varphi$, already operator-oriented, requires only language synchronisation.
- `/core/foundations/consequences.md`, `axiom-septicity.md` — base consequences, surface layer.
- `/consciousness/hierarchy/interiority-hierarchy.md`, `depth-tower.md` — hierarchical structures.
- `/proofs/consciousness/interiority-hierarchy.md`, `conscious-window.md` — proofs.
- `/applied/coherence-cybernetics/theorems.md`, `definitions.md` — applications.

### Tier 2: status registry and summary theorems

`/reference/status-registry.md`, `/reference/specification.md` — theorem descriptions. "Self-" occurrences in theorem titles are rewritten per the protocol; theorem numbers are preserved.

### Tier 3: formal proof files

In proofs (`/proofs/*`) formal definitions are **already** operator-based ($\varphi$, $\mathcal{L}_\Omega$, CPTP, T-96). Replacement is needed only in transitional commentary and motivation paragraphs.

## Applied factorisation: canonical example

Demonstration of the protocol on the key concept.

**Before (rhetorical)**:
> UHM establishes self-modelling through the operator $\varphi$. Self-observation is the system's ability to describe its own state. Autopoiesis is the system's self-reproduction through self-modelling.

**After (operator-based)**:
> UHM establishes a **categorical map** $\varphi: \mathrm{D}(\mathbb{C}^7) \to \mathrm{D}(\mathbb{C}^7)$ with a fixed point $\rho^* = \varphi(\Gamma)$ (T-96). **Reflection** of the system relative to its own state is formalised as a **terminal coalgebra** structure on the $\Gamma$-dynamics, characterised by the measure $R = 1/(7P)$ (T-126). **Closure under the $\varphi$-trajectory** (on the dual AC-side, an $\mathsf{A}$-fixed point at level $\omega^2$ per 113.T Diakrisis) — trajectory reproduction without external maintenance.

The operator-based content is **identical** to the rhetorical version. But:
1. Every element is explicitly typed ($\varphi$ is an operator, $\rho^*$ a state, $R$ a measure, iteration a trajectory).
2. The describing and described positions are separated ($\Gamma$ and $\varphi(\Gamma)$ are distinct points in $\mathrm{D}(\mathbb{C}^7)$, connected by the fixed-point equation but structurally distinct).
3. The protocol is compatible with Noesis hygiene verification (NO-19): the factorisation is explicit.

## Relation to other documents

- [diakrisis.gst.st/11-noesis/07-theorems](http://diakrisis.gst.st/11-noesis/07-theorems) §NO-19 — structural source of the protocol; theorem NO-19.
- [diakrisis.gst.st/12-actic/07-beyond-metastemology](http://diakrisis.gst.st/12-actic/07-beyond-metastemology) — historical context (Churilov's metastemological programme).
- In the external Diakrisis corpus, theorem 105.T uses its depth-stratification axiom `Diakrisis T-2f*` for paradoxes reducible to the Yanofsky diagonal scheme. [Theorem 105.T](https://diakrisis.gst.st/06-limits/10-maximality-theorems)
- UHM [`/proofs/categorical/formalization-phi`](/docs/proofs/categorical/formalization-phi) — source-level formalisation of the $\varphi$-operator.

## Refactoring plan

1. **Phase A** (this document + `self-observation.md` refactor) — protocol established, canonical example given.
2. **Phase B** — sweep over Tier-1 files (from the Tier-1 list above), applying the table.
3. **Phase C** — Tier-2 (status registry and summary) and Tier-3 (proof files).

Each phase is a separate commit with an audit (count of replaced "self-X", verification that theorem statements are not touched, build check).

## Note

The protocol does not revoke existing UHM theorems — all T-1..T-223+ remain formally correct. The refactor is **interface-level**, affecting only the prose layer. The formal core ($\varphi$, $\mathcal{L}_\Omega$, T-96, T-190, T-223) already operates in operator language; hygiene synchronises the surface with the core.
