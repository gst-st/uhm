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

Each routine is a pure function of `gamma` (plus, where noted, a second state for increments or a declared potential $V$ for the Hessian score). All are $O(1)$ in problem size (fixed $7\times7$); the only nontrivial numerics are the PSD projection eigendecomposition and, when requested, a supplied potential's Hessian.

**Purity $P$ `[T]`.** `P = trace(gamma @ gamma).real`. Unitary invariant. Range $[1/7, 1]$; $1/7$ is the maximally mixed "heat-death" state $I/7$, $1$ is a pure state. Threshold of viability $P > 2/7$ ([T](/docs/core/dynamics/viability)).

**Reflection $R$ `[D]`.** `R = 1.0 / (7*P)`. Unitary invariant. Range $[1/7, 1]$; the normalised proximity to $I/7$. Consciousness band $R \geq 1/3$ (equivalently $P \leq 3/7$; [self-observation](/docs/consciousness/foundations/self-observation#формы-r)). This is the *canonical* $R$; do not confuse it with $R_\varphi$ (below) — the two are distinct working forms and the kernel exposes both under their own names.

**Self-model quality $R_\varphi$ `[T]`.** Requires an explicitly specified self-model map $\varphi$. For the **linear anchor-mixing** family ([T-249](/docs/proofs/categorical/formalization-phi#дф-производная)),

$$\varphi_{\mathrm{lin}}(\Gamma) := R(\Gamma)\,\Gamma + (1 - R(\Gamma))\,I/7 = (1-k)\,\Gamma + k\,I/7, \qquad k = 1 - R(\Gamma) = 1 - \frac{1}{7P(\Gamma)},$$

then `R_phi = 1 - fro(gamma - phi_lin(gamma))**2 / fro(gamma)**2`, which reduces identically to $R_\varphi = 1 - (1 - R)^3 \in [0, 1]$ and is unitary-invariant. Do **not** conflate $\varphi_{\mathrm{lin}}$ (weight $R$ on $\Gamma$, $1-R$ on $I/7$) with the **coherent dephasing-anchor** map $\varphi_{\mathrm{coh}}(\Gamma) := (1-R)\,\mathcal{P}_\alpha(\Gamma) + R\,I/7$ or the **anchored** map $\varphi_J(\Gamma) := (1-R)\,\mathcal{P}_\alpha(\Gamma) + R\,|\psi\rangle\langle\psi|$ ([T-334](/docs/reference/status-registry)). Where a trained anchor $\rho_\theta$ is supplied ([formalization of $\varphi$](/docs/proofs/categorical/formalization-phi#механизмы-rφ)), $\varphi_\theta(\Gamma) = R\,\Gamma + (1-R)\,\rho_\theta$ is evaluated instead.

**Integration $\Phi$ `[D]/[T]`.** Computed directly from the canonical fixed-frame coherence ratio of [dimension-U](/docs/core/structure/dimension-u#мера-интеграции-φ) and [T-129](/docs/proofs/consciousness/operationalization#t-129):

$$\Phi(\Gamma) = \frac{P - P_{\mathrm{diag}}}{P_{\mathrm{diag}}} = \frac{\sum_{i \neq j} |\gamma_{ij}|^2}{\sum_{i=1}^7 \gamma_{ii}^2}, \qquad P_{\mathrm{diag}} = \sum_{i=1}^7 \gamma_{ii}^2.$$

Algorithm: `P_diag = sum(diag(gamma).real**2); Phi = (P - P_diag) / P_diag`. Because $\mathbb C^7$ has prime dimension $7$, it admits **no** nontrivial tensor factorisations or bipartitions; $\Phi$ is an $O(1)$ fixed-frame algebraic ratio, **not** an enumeration over bipartitions and **not** invariant under arbitrary unitary rotations. Range $[0, 6]$, obeying $\Phi \leq 7P - 1$ (hence $\Phi \leq 2$ inside the conscious window $P \leq 3/7$); access criterion $\Phi \geq 1$ `[D]`, which algebraically implies $P \geq 2/7$ (`T-129 [T]`).

**Differentiation $D_{\mathrm{diff}}^{7D}$ `[D]`.** In the native 7D state space, the kernel computes the canonical **7D native proxy** of [operationalization](/docs/proofs/consciousness/operationalization#t-128):

$$\mathrm{Coh}_E(\Gamma) = \frac{\gamma_{EE}^2 + 2\sum_{j \neq E} |\gamma_{Ej}|^2}{P} = \frac{\|\pi_E(\Gamma)\|_F^2}{P} \in [0, 1], \qquad D_{\mathrm{diff}}^{7D}(\Gamma) = 1 + 6\,\mathrm{Coh}_E(\Gamma).$$

Algorithm (with axis $E$ at index `4` in $[A,S,D,L,E,O,U]$): `coh_E = (gamma[4,4].real**2 + 2*sum(abs(gamma[4, j])**2 for j != 4)) / P; D_diff_7D = 1.0 + 6.0 * coh_E`. Range $[1, 7]$; working threshold $D_{\mathrm{diff}}^{7D} \geq 2$ `[D]`. Fixed-frame (depends on axis $E$). The spectral von Neumann measure $\exp S_{vN}(\rho_E)$ is defined **only** when an extended experiential register $\mathcal H_E$ with an explicit tensor factorisation and partial trace $\rho_E$ is supplied; it is **never** equated with $\exp S_{vN}(\Gamma)$ on the full $7\times 7$ matrix $\Gamma$ (at $|E\rangle\langle E|$, $D_{\mathrm{diff}}^{7D} = 7$ while $\exp S_{vN}(\Gamma) = 1$; at $I/7$, $D_{\mathrm{diff}}^{7D} = 13/7$ while $\exp S_{vN}(\Gamma) = 7$).

**Gap map `[D]`.** For each pair $(i,j)$: `Gap[i,j] = abs(sin(angle(gamma[i,j])))`, with the [vanishing-coherence convention](/docs/core/dynamics/gap-operator#конвенция-нулевой-когерентности): if `abs(gamma[i,j]) < eps_min`, set `Gap[i,j] = 1` (a channel with no coherence is not "transparent", it is absent — phase is undefined). Returns the 21 upper-triangle values as the fixed-frame transparency chart.

**Mandalagram `[D]`.** A pure reshape: the 7 populations `diag(gamma).real` and the 21 coherences `(magnitude, phase)` laid on the 7-node / 21-edge chart ([coherence matrix](/docs/core/dynamics/coherence-matrix), [Gap diagnostics](/docs/applied/research/gap-diagnostics#фано-паттерны)). No computation, only layout — this is the render model the UI consumes.

**Archetype `[T]/[D]`.** Threshold the diagonal at $\tau$ (default mean population $1/7$) to a 7-bit word $\{p_i > \tau\} \in \{0,1\}^7$, then syndrome-decode to the unique nearest codeword among the **16 codewords of the Hamming code $H(7,4)$** ([T-224](/docs/applied/research/syndrome-calculus#теорема-сигма)). Returns the codeword id (0–15) plus the margin to the nearest neighbouring codeword. Keep this strictly distinct from the **9 nonempty orbit types** of axis subsets under the finite Fano collineation group $\mathrm{GL}(3,2)$ ([T-256](/docs/reference/status-registry), [Mathematical kernel](/docs/reference/mathematical-kernel)) — neither classification is a $G_2$ orbit partition of thresholded diagonals.

**Mode `[D]`.** Requires two states $\Gamma(t)$, $\Gamma(t')$ and a declared generator grouping. Form the increment $\dot\Gamma \approx (\Gamma(t')-\Gamma(t))/(t'-t)$ and project it onto the chosen [three-part dynamical grouping](/docs/core/operators/lindblad-operators#триадная-декомпозиция) — Hamiltonian (preserving), dissipative (relaxing toward $I/7$), and regenerative (restoring toward $\varphi(\Gamma)$). This three-part grouping is a chosen modelling convention `[D]`, not an exhaustive GKSL classification theorem. Returns the three fractions summing to one; the "mode" is the dominant fraction.

**Meaning `[D]`.** `Meaning = P * D_diff_7D * Phi * R_phi` — a chosen composite scalar indicator (per [Meaning](/docs/consciousness/ethics-meaning/meaning#пиковый-потенциал), infinitely many monotone products exist and there is no unique canonical scalar of meaning). Returned both as the scalar and as its four factors, so the UI can show *which* factor is smallest.

**Freedom `[D]` (conditional `T-89 [T]`).** Given an **explicitly supplied $C^2$ potential $V$** on a smooth domain in the 48-real-dimensional state space and a critical point $\Gamma_*$, define the [Hessian score](/docs/consciousness/ethics-meaning/freedom#количественная-мера):

$$\mathrm{Freedom}_V(\Gamma_*) := 1 + \dim\ker\operatorname{Hess}_{\Gamma_*} V \in [1, 49].$$

Numerically, the kernel forms $\operatorname{Hess}_{\Gamma_*} V$, computes its eigenvalues, and evaluates `Freedom = count(abs(hessian_evals) < tol) + 1`, returning the count together with the flat eigenvectors. By [T-89](/docs/consciousness/ethics-meaning/freedom#количественная-мера) (`[T]` under the Morse–Bott hypothesis), the nullity equals the tangent dimension of a smooth critical manifold; without Morse–Bott regularity, higher-order terms can eliminate flat paths despite zero quadratic modes. If no potential $V$ is supplied, `Freedom` is returned as `null`. The score is neither CPTP-monotone nor a standalone measure of personal agency without an independent policy-repertoire model.

## §3. Confidence propagation {#доверие}

Every scalar invariant carries an uncertainty derived from `cov` by the delta method: for invariant $f(\Gamma)$, `var(f) = grad_f.T @ cov @ grad_f`, with `grad_f` computed analytically for the closed-form functions ($P, R, R_\varphi, \Phi, D_{\mathrm{diff}}^{7D}, \mathrm{Meaning}$) and by autodiff/finite-difference for `Freedom` (when a potential $V$ is supplied). The kernel returns each invariant as a `(value, std, anchor)` triple. **Anchor III inputs have no `cov`**, so their invariants return `std = null` and are rendered as "orientational, not measured" — the honesty spine enforced at the numeric layer.

## §4. The optical-construction guardrails {#гардрейлы}

Before any readout is released, the kernel runs three guardrail checks ([Mathematical kernel](/docs/reference/mathematical-kernel), [Reconstruction identifiability](/docs/applied/research/reconstruction-identifiability)) and attaches the verdicts:

1. **Chart type (`T-256 [T]+[I]`).** Which of the 9 nonempty Fano collineation orbit types and which state sectors does this reading actually resolve? A questionnaire estimate resolves populations and magnitudes but is phase-blind; the kernel tags which sectors are trustworthy for *this* estimate, so downstream code never reads a phase-dependent Gap value off a phase-blind anchor.
2. **Anchor licence (`T-257 [H]`).** If any external signal fed the estimate, does it carry an identified physical coupling model (light/sleep timing, physiological telemetry) or is it an unmodelled ephemeris/natal claim? Under the coupling-channel hypothesis ([T-257](/docs/applied/research/gap-diagnostics), [Status registry](/docs/reference/status-registry)), unmodelled planetary/natal inputs are rejected at ingestion as an architectural policy, not silently used.
3. **Viability gate `[D]`.** Is the subject actually in a viable regime ($P>2/7$, etc.)? Below the gate, consciousness-window indicators are marked not-applicable rather than reported as small numbers — an unviable state is flagged outside the window.

These verdicts are not advisory; a domain module that ignores them cannot compile against the API (§5), because the readout type is parameterised by the guardrail outcome.

## §5. The internal API {#api}

The kernel exposes one entry point and a typed readout:

```
readout = kernel.evaluate(estimate: GammaEstimate,
                          prev: GammaEstimate | null,
                          potential: PotentialSpec | null = null) -> Readout
```

`Readout` fields: `invariants` (the eleven `(value, std, anchor)` triples; `mode` present only if `prev` given, `freedom` present only if `potential` given), `mandalagram` (render model), `archetype` (Hamming $H(7,4)$ codeword id + margin), `guardrails` (the three §4 verdicts), `quality` (the input-projection flag from §1). Every field that can be uncertain carries its uncertainty; every field carries its anchor. There is **no** call that returns a bare number without its provenance — the API makes the dishonest output unrepresentable.

**Substrate-agnosticism.** `evaluate` never inspects *where* `gamma` came from beyond the `anchor` tag. The same call serves a human self-audit, an EEG pipeline, and an AI-telemetry adapter — the platform property of [00 §2](/docs/applied/console/overview#почему-коммерция), enforced by keeping the kernel blind to substrate.

## §6. Testing and numerical discipline {#тесты}

The kernel ships with an oracle suite (the same discipline the corpus uses):
- **Analytic identities** checked against random density matrices to $\sim 10^{-12}$, including $R_\varphi = 1-(1-R)^3$ for the linear anchor-mixing family $\varphi_{\mathrm{lin}}$ (`T-249 [T]`) and $\Phi \leq 7P - 1$ (`T-129 [T]`).
- **Boundary states** hitting exact canonical values: at $I/7$, $P = 1/7$, $R = 1$, $\Phi = 0$, $D_{\mathrm{diff}}^{7D} = 13/7$; at $|E\rangle\langle E|$, $P = 1$, $R = 1/7$, $\Phi = 0$, $D_{\mathrm{diff}}^{7D} = 7$; at the uniform pure state $|u\rangle\langle u|$, $P = 1$, $R = 1/7$, $\Phi = 6$.
- **Unitary-invariance tests (strictly scoped):** under random $U \in U(7)$ (and in particular $G_2 \subset SO(7) \subset U(7)$), the oracle verifies invariance **only of true unitary/spectral invariants** — $P(\Gamma)$, $R(\Gamma) = 1/(7P)$, the spectrum (eigenvalues) of $\Gamma$, and $R_\varphi(\Gamma)$ for $\varphi_{\mathrm{lin}}$.
- **Frame-dependence and covariance tests:** explicit negative tests verify that fixed-frame quantities ($\Phi$, $\mathrm{Coh}_E$, $D_{\mathrm{diff}}^{7D}$, Gap map, Hamming $H(7,4)$ codeword) are **not** basis-invariant under generic unitary or $G_2$ rotations, while transforming covariantly under axis permutations (and preserving the $H(7,4)$ code under $\mathrm{GL}(3,2)$ Fano collineations).
- **Monotonicity tests:** monotonicity of the composite Meaning indicator in each of its four factors.

A build that fails any oracle does not ship — the readout's authority rests on the kernel computing the corpus's exact definitions without smuggling in false invariances.

**Where this leads.** [03 · Anchors and estimation](/docs/applied/console/anchors) specifies how a real `GammaEstimate` is produced from each of the three evidence types, with the full self-audit instrument and the measurement-bridge mathematics.
