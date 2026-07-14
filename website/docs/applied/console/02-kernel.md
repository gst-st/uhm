---
sidebar_position: 2
title: "02 · The kernel specification"
description: "The engineering heart of UHM Console: the substrate-agnostic library that turns an estimated coherence matrix into the full derived readout. Exact algorithms for all eleven invariants, the internal representation of Γ, confidence propagation, edge-case handling, the optical-construction guardrails, and the internal API surface that every domain module calls. Nothing here is heuristic — each routine computes a corpus-defined quantity."
---

# 02 · The kernel specification

> *One library, reused for a person, a team, and an agent. It takes an estimated state and its uncertainty, and returns the readout with the uncertainty carried through. Everything a domain module needs, it gets by calling the kernel; the kernel calls nothing but linear algebra.*

## §1. Representation of Γ {#представление}

The kernel's single input type is an **estimate object** `GammaEstimate`:

- `gamma`: a $7\times7$ complex Hermitian matrix, PSD, unit trace — axis order fixed as $[A,S,D,L,E,O,U]$.
- `cov`: a covariance over the 48 real degrees of freedom (7 populations − 1 trace + 21 magnitudes + 21 phases; the trace constraint removes one population dof), used for confidence propagation. May be `null` for anchor III.
- `anchor`: one of `MEASURED | AUTOEPHEMERIS | ORACLE` (the honesty tag).
- `t`: timestamp, for trajectory assembly.

**Validation and projection.** Any incoming `gamma` is projected to the nearest valid state before use: Hermitize ($\Gamma \leftarrow \tfrac12(\Gamma+\Gamma^\dagger)$), clip negative eigenvalues to zero, renormalise the trace. The projection distance is recorded as an input-quality flag — a large projection means the estimator produced something far from a physical state, which the honesty layer surfaces.

## §2. The eleven invariants — exact routines {#инварианты}

Each routine is a pure function of `gamma` (plus, where noted, a second state for increments). All are $O(1)$ in problem size (fixed $7\times7$); the only nontrivial numerics are a Hermitian eigendecomposition and one small Hessian.

**Purity $P$.** `P = trace(gamma @ gamma).real`. Range $[1/7, 1]$; $1/7$ is the maximally mixed "heat-death" state $I/7$, $1$ is a pure state. Threshold of viability $P > 2/7$ ([T](/docs/core/dynamics/viability)).

**Reflection $R$.** `R = 1.0 / (7*P)`. Range $[1/7, 1]$; the normalised distance from $I/7$. Consciousness band $R \geq 1/3$ ([T](/docs/consciousness/foundations/self-observation#формы-r)). This is the *canonical* R; do not confuse it with $R_\varphi$ (below) — the two are distinct working forms and the kernel exposes both under their own names.

**Self-model quality $R_\varphi$.** Requires the self-model map $\varphi$. For the canonical (dissipative) family, `phi(gamma) = (1-k)*gamma + k*eye(7)/7` with `k = 1 - 1/(7*P)`; then `R_phi = 1 - fro(gamma - phi(gamma))**2 / fro(gamma)**2`. Range $[0,1]$. Where a trained target $\rho_\theta$ is available (the [two-timescale model](/docs/proofs/categorical/formalization-phi#механизмы-rφ)), `phi_theta(gamma) = (1-k)*gamma + k*rho_theta` is used instead — this is what lets practice raise the baseline.

**Integration $\Phi$.** Computed from the HS-projection functional of [dimension-U](/docs/core/structure/dimension-u#мера-интеграции-φ): the loss of information under the best factorised approximation of Γ across the minimum-information bipartition. Algorithm: for each bipartition of the seven axes, form the product-of-marginals approximation, take the HS distance to Γ; $\Phi$ is the minimum over bipartitions (the "weakest link"), normalised so the consciousness threshold sits at $\Phi = 1$. Sixty-three bipartitions — trivially enumerable.

**Differentiation $D_{\mathrm{diff}}$.** `evals = eigvalsh(gamma); S = -sum(evals * log(evals + eps)); D_diff = exp(S)`. Range $[1, 7]$; the effective number of occupied dimensions. Threshold $D_{\mathrm{diff}} \geq 2$ ([T](/docs/proofs/consciousness/operationalization)).

**Gap map.** For each pair $(i,j)$: `Gap[i,j] = abs(sin(angle(gamma[i,j])))`, with the [vanishing-coherence convention](/docs/core/dynamics/gap-operator#конвенция-нулевой-когерентности): if `abs(gamma[i,j]) < eps_min`, set `Gap[i,j] = 1` (a channel with no coherence is not "transparent", it is absent — phase is undefined). Returns the 21 upper-triangle values as the transparency chart.

**Mandalagram.** A pure reshape: the 7 populations `diag(gamma).real` and the 21 coherences `(magnitude, phase)` laid on the 7-node / 21-edge chart, with the [canonical cell names](/docs/applied/research/gamma-canon#слой-1). No computation, only layout — this is the render model the UI consumes.

**Archetype.** Threshold the diagonal at $\tau$ (default the mean population) to a 7-bit pattern; decode to one of the [sixteen signatures](/docs/applied/research/gamma-canon#слой-4) via the fixed lookup (the 16 signatures are the $G_2$-orbit classes of thresholded diagonals). Returns the signature id plus the margin to the nearest neighbouring signature (how robust the classification is).

**Mode.** Requires two states $\Gamma(t)$, $\Gamma(t')$. Form the increment $\dot\Gamma \approx (\Gamma(t')-\Gamma(t))/(t'-t)$ and decompose it into the [triadic components](/docs/core/operators/lindblad-operators#триадная-декомпозиция) — Hamiltonian (preserving), dissipative (dissolving toward $I/7$), regenerative (restoring toward $\varphi(\Gamma)$). Returns the three fractions summing to one; the "mode" is the dominant fraction.

**Meaning.** `Meaning = P * D_diff * Phi * R_phi` — the [product form](/docs/consciousness/ethics-meaning/meaning). Returned both as the scalar and as its four factors, so the UI can show *which* factor limits meaning (the smallest factor is the bottleneck).

**Freedom.** Build the free-energy Hessian $\mathcal H_\Gamma$ (second derivative of the free-energy functional at Γ over the 48 real dof), take its eigenvalues, count those below a flatness tolerance: `Freedom = count(abs(hessian_evals) < tol) + 1` ([T](/docs/consciousness/ethics-meaning/freedom)). Returns the count plus the flat directions themselves (the eigenvectors) — the actual axes along which the system may move without energy penalty, which the decision-support module reads.

## §3. Confidence propagation {#доверие}

Every scalar invariant carries an uncertainty derived from `cov` by the delta method: for invariant $f(\Gamma)$, `var(f) = grad_f.T @ cov @ grad_f`, with `grad_f` computed analytically where closed-form (P, R, R_phi, D_diff, Meaning) and by autodiff/finite-difference otherwise (Phi, Freedom). The kernel returns each invariant as a `(value, std, anchor)` triple. **Anchor III inputs have no `cov`**, so their invariants return `std = null` and are rendered as "orientational, not measured" — the honesty spine enforced at the numeric layer.

## §4. The optical-construction guardrails {#гардрейлы}

Before any readout is released, the kernel runs the three [optical-construction](/docs/applied/research/one-grammar#оптическая-конструкция) checks and attaches the verdicts:

1. **Chart type (T-256).** Which sub-configuration does this reading actually resolve? A questionnaire estimate resolves populations well and phases poorly; the kernel tags which sectors are trustworthy for *this* estimate, so downstream code never reads a phase-dependent Gap value off a phase-blind anchor.
2. **Anchor licence (T-257).** If any external signal fed the estimate, is it on the licensed ledger (solar/lunar/physiological) or a category error (planetary/natal)? Unlicensed external inputs are rejected at ingestion, not silently used.
3. **Viability gate.** Is the subject actually in a viable regime ($P>2/7$, etc.)? Below the gate, the "consciousness-predicate" readouts are marked not-applicable rather than reported as small numbers — a rock does not have a low $\Phi$, it has none.

These verdicts are not advisory; a domain module that ignores them cannot compile against the API (§5), because the readout type is parameterised by the guardrail outcome.

## §5. The internal API {#api}

The kernel exposes one entry point and a typed readout:

```
readout = kernel.evaluate(estimate: GammaEstimate,
                          prev: GammaEstimate | null) -> Readout
```

`Readout` fields: `invariants` (the eleven `(value, std, anchor)` triples; `mode` present only if `prev` given), `mandalagram` (render model), `archetype` (id + margin), `guardrails` (the three §4 verdicts), `quality` (the input-projection flag from §1). Every field that can be uncertain carries its uncertainty; every field carries its anchor. There is **no** call that returns a bare number without its provenance — the API makes the dishonest output unrepresentable.

**Substrate-agnosticism.** `evaluate` never inspects *where* `gamma` came from beyond the `anchor` tag. The same call serves a human self-audit, an EEG pipeline, and an AI-telemetry adapter — the platform property of [00 §2](/docs/applied/console/overview#почему-коммерция), enforced by keeping the kernel blind to substrate.

## §6. Testing and numerical discipline {#тесты}

The kernel ships with an oracle suite (the same discipline the corpus uses): analytic invariants checked against random states to $\sim10^{-12}$; the $R_\varphi = 1-(1-R)^3$ identity for the canonical family as a cross-check; boundary states ($I/7$, pure states) hitting the exact threshold values; and property tests (monotonicity of Meaning in each factor, $G_2$-invariance of every scalar under a random $G_2$ rotation of the axes). A build that fails any oracle does not ship — the readout's authority rests on the kernel being provably the corpus's functions, not approximations of them.

**Where this leads.** [03 · Anchors and estimation](/docs/applied/console/anchors) specifies how a real `GammaEstimate` is produced from each of the three evidence types, with the full self-audit instrument and the measurement-bridge mathematics.
