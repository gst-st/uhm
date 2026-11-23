---
sidebar_position: 15
title: Domain Transfer
description: "The generative layer — the third-order engine (mediators, closure law, self-checking dictionary) unfolded across ten domain templates, each with a derivation, verified numbers, honest status markers, and a falsifiable test."
---

# Domain Transfer: the generative layer

:::info What this document is
The seven-dimensional relation structure $\Gamma$ is not an unstructured collection of 49 numbers; it is a layered object whose specific Fano combinatorics lives at **third order** (on triples, not pairs). Once formulated — [§0](#движок) — it serves as a *structural transfer template*: any domain onto which the seven axes can be faithfully encoded inherits the same rigid third-order combinatorics. This document unfolds that template across ten domains. Each entry has the same structure: **dictionary** (how domain variables map to the seven axes) → **derivation** (the transferred computation) → **number** (verified algebraically or numerically) → **status** (honest `[T]`/`[C]`/`[H]`/`[I]`/`[Pr]`) → **test** (a falsifiable check via the self-checking mediator table in [§0](#движок)).
:::

## §0. The engine {#движок}

Four structural facts, each proved elsewhere in the corpus, compose into the transfer engine.

**(1) The first-order blind spot `[T]`.** The sum of the adjacency matrices of the seven Fano lines equals $J - I$ exactly — the adjacency of the complete graph $K_7$, spectrum $\{6, -1^6\}$. Any equal-weight pairwise statistic (covariance, two-point function, correlation) built symmetrically from the lines is a function of $J-I$ alone, hence *indistinguishable from unstructured full connectivity*. Distinguishable Fano structure begins at third order (triples). Canonical home: [Fano fingerprint §0](/docs/applied/research/fano-fingerprint#слепое-пятно).

**(2) The mediator map `[T]`.** By the Steiner property $S(2,3,7)$, every unordered pair $(i,j)$ lies on exactly one line, so it has a unique **mediator** $k^*(i,j)$ — the third point of that line (the [polar point $\pi(i,j)$ of T-226](/docs/applied/research/fano-fingerprint#полярное-разбиение)). Under the canonical Singer cyclic Fano plane (all 21 pairs):

| Line | Mediations inside the line |
|---|---|
| $\{A,S,L\}$ | $A\!\leftrightarrow\!S$ via $L$; $A\!\leftrightarrow\!L$ via $S$; $S\!\leftrightarrow\!L$ via $A$ |
| $\{S,D,E\}$ | $S\!\leftrightarrow\!D$ via $E$; $S\!\leftrightarrow\!E$ via $D$; $D\!\leftrightarrow\!E$ via $S$ |
| $\{D,L,U\}$ | $D\!\leftrightarrow\!L$ via $U$; $D\!\leftrightarrow\!U$ via $L$; $L\!\leftrightarrow\!U$ via $D$ |
| $\{L,E,O\}$ | $L\!\leftrightarrow\!E$ via $O$; $L\!\leftrightarrow\!O$ via $E$; $E\!\leftrightarrow\!O$ via $L$ |
| $\{E,U,A\}$ | $E\!\leftrightarrow\!U$ via $A$; $E\!\leftrightarrow\!A$ via $U$; $U\!\leftrightarrow\!A$ via $E$ |
| $\{U,O,S\}$ | $U\!\leftrightarrow\!O$ via $S$; $U\!\leftrightarrow\!S$ via $O$; $O\!\leftrightarrow\!S$ via $U$ |
| $\{O,A,D\}$ | $O\!\leftrightarrow\!A$ via $D$; $O\!\leftrightarrow\!D$ via $A$; $A\!\leftrightarrow\!D$ via $O$ |

Read as a table of structural levers: within the Fano incidence geometry, creating or reinforcing the link $(i,j)$ through third-order closure involves the two arms $(i,k^*)$ and $(k^*,j)$, and no others.

**(3) The closure law `[T]`.** Two coherences generate a third under cubic line coupling **iff** the triple is a Fano line. The cubic line functional $W(\Gamma) = \sum_{\text{lines}} \mathrm{Re}(\gamma_{ij}\gamma_{jk}\gamma_{ki})$ has a gradient flow that, seeded on a collinear path $A\!-\!S\!-\!L$ (both edges in $\{A,S,L\}$), feeds **exactly one** new edge — the closing edge $L\!-\!A$ — and, seeded on a non-collinear path $A\!-\!S\!-\!E$ ($\{A,S,E\}$ is not a Fano line), feeds **nothing**. This is the selection rule: cubic mediation is line-local.

**(4) The channel contraction $\Phi \to \Phi/9$ `[T]`.** The Fano pinching channel (Kraus projectors onto the three-dimensional line subspaces, complete because each point lies on three lines) preserves a population across all three of its lines ($3\times\tfrac13 = 1$) but preserves an off-diagonal coherence only in its single containing line out of three ($\times\tfrac13$); squared, off-diagonal Frobenius mass contracts by $\tfrac19$, giving $\Phi_{\text{in}}/\Phi_{\text{out}} = 9$ identically on every state with $\Phi_{\text{in}} > 0$. The factor of nine is a Steiner incidence count, not a fitted parameter.

**The self-checking dictionary `[T]` / `[Pr]`.** These four facts turn any proposed seven-axis domain dictionary into a *falsifiable empirical claim* rather than a free analogy: a valid encoding must reproduce the 21-pair mediator table above. There are $7!/|\mathrm{PGL}(3,2)| = 5040/168 = 30$ distinct labelled Fano planes on seven axes (chance agreement $1/30$ under a uniform random axis permutation, and $(1/5)^7 = 1/78{,}125 \approx 1.3\times 10^{-5}$ if seven independent mediator triples are guessed from the remaining five axes). Every domain reading below is an explicit structural template `[I]`/`[Pr]` licensed only to the extent that an operational encoder passes this mediator check.

---

## §1. Level I — the individual mind {#уровень-i}

### §1.1 Discovery 1 — the clinic: an ordered shutdown, and the right instrument {#d1}

**Dictionary.** The seven axes are mapped to seven functional channels of a single cognitive system ($A$ Articulation, $S$ Structure, $D$ Dynamics, $L$ Logic, $E$ Interiority, $O$ Ground, $U$ Unity). Anaesthetic induction is modelled as uniform dephasing $\dot\Gamma \supset \gamma_d(\mathrm{diag}\,\Gamma - \Gamma)$ over a coupling Hamiltonian $H \propto J-I$.

**Derivation.** Dephasing damps the *off-diagonal* entries (coherences) exponentially while leaving the *diagonal* (populations) invariant. Since $\Phi$ is the ratio of off-diagonal coherence mass to diagonal population mass and $P = \mathrm{Tr}(\Gamma^2)$ retains the diagonal contribution, the integration threshold $\Phi = 1$ is crossed **before** the purity threshold $P = 2/7$. This yields an *ordered shutdown*: integration fails before purity drops below $P_{\text{crit}}$.

**Number.** Over a numerical sweep of $39$ viable conscious initial states (initial purity and integration above threshold; three dephasing rates, three mixing weights, six random seeds), $\Phi$ crossed $1$ before $P$ crossed $2/7$ in **39/39** cases. The *ordering* is structural for pure-dephasing dominance; the *time ratio* (in one parametrization, $t_P/t_\Phi \approx 1.09$) is model-dependent and not derived.

**Status.** `[C]` (within the dephasing-dominated model, the shutdown ordering is structural; actual clinical timescales depend on the physiological noise model and encoder `[H]`).

**Test.** Two predictions `[H]`/`[Pr]`. (i) Under graded anaesthesia (propofol, sevoflurane, xenon), large-scale *integration* markers should collapse **before** behavioural loss of responsiveness. (ii) **The discriminating instrument is third-order.** By the first-order blind spot, purely pairwise two-point metrics cannot distinguish Fano incidence from uniform all-to-all coupling; the appropriate probe is **bicoherence** (the third-order EEG cross-bispectrum). Once seven physiological channels are mapped to the axes, triples corresponding to Fano lines are predicted to carry systematically higher bicoherence than the 28 non-line triples — testable on existing EEG datasets.

### §1.2 Discovery 2 — therapy as mediator engineering {#d2}

**Dictionary `[I]`.** A weakened coupling between two functional domains $(i,j)$ — for example Interiority $E$ and Logic $L$ ("difficulty reasoning about felt experience").

**Derivation.** By the cubic closure law `[T]`, a severed coherence $(i,j)$ is not directly closed by pairwise excitation alone; under the cubic functional $W(\Gamma)$ it regenerates through the two arms $(i,k^*)$ and $(k^*,j)$ meeting at the unique mediator $k^*(i,j)$. Reading directly from the canonical [mediator table](#движок): for $(E,L)$ the mediator is $O$ (Ground) via $\{L,E,O\}$; for $(A,E)$ it is $U$ (Unity) via $\{E,U,A\}$; for $(A,O)$ it is $D$ (Dynamics) via $\{O,A,D\}$.

**Structure.** The canonical Fano plane fixes all 21 mediator triples uniquely once the axis dictionary is fixed; there is no post-hoc freedom to pick mediators, which makes the protocol falsifiable.

**Status.** `[T]` (algebraic closure law) / `[I]`–`[H]` (clinical translation protocol).

**Test.** Given a calibrated 7-axis assessment protocol: estimate the 21 couplings, identify a weak link $(i,j)$, evaluate both arms through $k^*(i,j)$, and target the weaker arm. Falsifiable prediction `[H]`: interventions strengthening the mediator arms restore the target coupling more effectively than control interventions targeting non-mediator axes (the other four axes provide a built-in negative control).

### §1.3 Discovery 3 — learning: state-space reflection and triple-lock bounds {#d3}

**Dictionary `[I]`.** A learner acquiring a structured skill spanning two axes $(i,j)$, coupled to a reflective self-model channel $\varphi$ (self-testing, metacognitive monitoring, retrieval practice).

**Derivation.** Two formal UHM ingredients transfer as structural templates. First, the [triple-lock learning bounds](/docs/applied/coherence-cybernetics/learning-bounds) combine three necessary sample/step lower bounds, $n_{\text{opt}} = \max(n_{\text{info}}, n_{\text{dyn}}, n_{\text{stab}})$ (`T-109`, `T-110`, `T-112` `[T]` under their respective task and accumulator hypotheses): insufficient statistical signal, update rate exceeding integration speed, or step amplitude exceeding the stability radius (`T-104` `[T]`) are three separable failure modes. Second, the formal reflection criterion $R(\Gamma) \ge R_{\mathrm{th}} = 1/3$ (`[T]` in the L2 window definition) is a **state-space fidelity requirement** on the self-model $\varphi$, *not* a prescription of wall-clock study-time fractions: translating a Hilbert–Schmidt fidelity ratio into a schedule percentage requires an explicit empirical encoder from practice regimes to $\Gamma$ (`[H]`). Third, under the closure law, consolidation of a link $(i,j)$ is reinforced within its Fano triple $\{i, j, k^*(i,j)\}$.

**Status.** `[T]` (necessary learning bounds `T-109`, `T-110`, `T-112`, stability radius `T-104`, and state-space threshold $R_{\mathrm{th}} = 1/3$) / `[H]`–`[Pr]` (empirical encoder mapping training protocols and skills to $\Gamma$).

**Test.** Empirical protocols (spaced retrieval, interleaving, self-explanation) can be tested against non-reflective baselines by constructing an operational proxy for self-model prediction accuracy (`[Pr]`) and testing whether triadic practice aligned with a validated mediator triple outperforms matched non-mediator triples.

---

## §2. Level II — groups and organizations {#уровень-ii}

### §2.1 Discovery 4 — the Steiner protocol for team communication {#d4}

**Dictionary.** A team of seven functional roles has $\binom{7}{2} = 21$ pairwise working interfaces to maintain.

**Derivation and optimality.** Cover the 21 pairs by three-person meetings. Each meeting of three covers $\binom{3}{2} = 3$ pairs, so at least $\lceil 21/3\rceil = 7$ meetings are required, with equality **iff** an exact zero-overlap cover exists — precisely a Steiner triple system $S(2,3,7)$, i.e., the Fano plane. The seven canonical Singer cyclic meetings

$$\{A,S,L\},\ \{S,D,E\},\ \{D,L,U\},\ \{L,E,O\},\ \{E,U,A\},\ \{U,O,S\},\ \{O,A,D\}$$

cover all 21 pairs exactly once, with uniform attendance load **exactly 3** per member and zero redundancy. **Single-fault tolerance:** because every two lines of $\mathrm{PG}(2,2)$ intersect in a unique point, removing *any* single member leaves all $\binom{6}{2}=15$ surviving pairs still sharing a meeting (every surviving pair retains either a 3-person meeting or a 2-person meeting from the deleted member's three lines). Each pairwise conflict $(i,j)$ belongs to a unique meeting with a unique third-party mediator $k^*(i,j)$.

**Number.** 7 meetings, load 3 per member, 0 pairwise overlap, single-member fault tolerance — exact combinatorial facts.

**Status.** `[T]` (covering optimality and single-fault tolerance of $S(2,3,7)$) / `[I]`–`[Pr]` (organizational mapping of roles to axes).

**Test.** Compared against ad-hoc schedules of equal total meeting load, the Steiner schedule maintains full pairwise coverage at minimal attendance load and degrades gracefully under single-node absence; omitting any single line leaves exactly three specific pairwise interfaces uncovered — a concrete, checkable failure signature.

### §2.2 Discovery 5 — attenuation limits on vertical composition {#d5}

**Dictionary `[I]`.** Nested organizational hierarchies: individual $\to$ team $\to$ division $\to$ multi-level enterprise.

**Derivation and honest boundary.** Earlier drafts invoked a universal depth ceiling of 3 for nested subjecthood; that universal depth ceiling is **withdrawn** (`T-217 [✗]`, `T-136 [✗]`). The algebraic inequality `T-142 [T]` holds only for a stipulated attenuation-score convention and does *not* establish a universal prohibition against deeper metamodels or multi-tier organizations. What *is* formally established in UHM is twofold: (i) multi-holon composition preserves viability margins under **weak coupling** and explicit mean-marginal aggregation (`CC-5` / `T-72` `[T]` under weak coupling and stated positive margins), and (ii) each coarse-grained Fano line-projection hop contracts off-diagonal integration by $\Phi \to \Phi/9$ (`[T]`). Consequently, multi-level hierarchies face an exponential coherence-attenuation cost unless active cross-tier coupling compensates for coarse-graining losses, making deep institutional composition an engineering trade-off (`[Pr]`) rather than a hard universal wall at depth 3.

**Status.** `[T]` (weak-coupling composition `CC-5`/`T-72` and single-hop $\Phi/9$ contraction) / `[I]`–`[Pr]` (organizational design reading); universal depth-3 ceiling withdrawn (`T-217 [✗]`, `T-136 [✗]`).

**Design consequence.** Architect large institutions with explicit cross-tier coherence maintenance or loosely coupled federations rather than assuming free hierarchical integration; monitor inter-tier coupling losses quantitatively rather than invoking a fixed tier ceiling.

---

## §3. Level III — machines {#уровень-iii}

### §3.1 Discovery 6 — the seven as a native error-correcting code {#d6}

**Dictionary.** Any seven-channel architecture: a seven-sector control agent, a seven-mode photonic chip, or a seven-service distributed cluster.

**Derivation.** The Fano incidence structure *is* the parity-check geometry of the Hamming code $H(7,4)$: the sixteen codewords of $H(7,4)$ include exactly seven codewords of weight 3, whose supports form an $S(2,3,7)$ — so **Hamming$(7,4)$ and the Fano plane are one combinatorial object** (up to relabelling). The Steane quantum code is $\mathrm{CSS}(H(7,4), H(7,4))$ — the quantum lift of the same structure ([Σ-calculus T-224/T-225](/docs/applied/research/syndrome-calculus)). Consequently, a seven-channel architecture carries a **native distance-3 single-error-correcting code**: under a persistent single-fault observation model (`T-225 [C]`), one corrupted channel is localized by three binary syndrome checks — the diagnostic pyramid $21 \to 7 \to 3 \to 1$ (21 pairwise relations $\to$ 7 axes $\to$ 3 syndrome bits $\to$ 1 fault address). The three-bit syndrome decodes the fault position uniquely for all seven single-error patterns.

**Number.** $[n,k,d] = [7,4,3]$: corrects every single-channel fault, detects double faults; three parity checks localize one of seven channels.

**Status.** `[T]` (coding geometry `T-224`) / `[C]` (operational pyramid under declared single-fault observation law `T-225`).

**Test.** Any seven-channel system equipped with binary line/parity health checks can localize a single degraded channel from three parity observables without probing all 21 pairwise couplings — a directly buildable diagnostic benchmark.

### §3.2 Discovery 7 — distributed systems: buses, not point-to-point {#d7}

Replace 21 point-to-point channels by **7 triple-buses** (the Fano lines): each node sits on exactly 3 buses (uniform degree, reflecting the 2-transitivity of $\mathrm{PSL}(2,7)$), any two buses intersect in a unique node (guaranteed rendezvous), and routing fallback follows the mediator table — a failed direct link $(i\to j)$ reroutes deterministically through $k^*(i,j)$ without dynamic routing tables. This architecture is developed as a reference protocol in [FANOS](/docs/applied/fanos/fanos-specification); here it appears as an engineering instantiation of the same $S(2,3,7)$ combinatorics. `[T]` (graph/design combinatorics) / `[Pr]` (protocol implementation).

### §3.3 Discovery 8 — agent architecture from structural invariants {#d8}

A UHM-inspired seven-sector agent architecture uses theorem-derived structural invariants as design priors rather than arbitrary hyperparameters: state-space reflection threshold $R \ge R_{\mathrm{th}} = 1/3$; purity operating window $(2/7, 3/7]$ with stability radius $r_{\mathrm{stab}}$ (`T-104` `[T]` at selected purity shell); inter-module coherence attenuation $\times 1/9$ per Fano line-projected hop (`[T]`); **line-aware routing** (a mixture-of-experts architecture ignoring Fano line structure incurs the ninefold integration contraction per coarse projection); and the empirical hypothesis `[H]` that delayed generalization jumps (grokking) correspond to block-integration $\Phi$ crossing unity. Developed further in the [SYNARC-Ω specification](/docs/applied/coherence-cybernetics/implementation). `[T]` (algebraic invariants) / `[H]`–`[Pr]` (neural-architecture mapping).

---

## §4. Level IV — markets and society {#уровень-iv}

### §4.1 Discovery 9 — the critical correlation of systemic risk {#d9}

**Dictionary `[H]`.** A portfolio of seven asset classes whose normalized covariance/correlation matrix is modelled by the equicorrelation density matrix $\Gamma = \big((1-r)I + rJ\big)/7$ with uniform pairwise correlation $r \in (-1/6, 1]$.

**Derivation.** For the equicorrelation matrix, the integration functional is exactly quadratic in $r$:

$$
\Phi(r) \;=\; \frac{\sum_{\text{off}} |\gamma_{ij}|^2}{\sum_{\text{diag}} |\gamma_{ii}|^2} \;=\; \frac{42\,(r/7)^2}{7\,(1/7)^2} \;=\; 6r^2,
$$

so the threshold $\Phi = 1$ is reached at

$$
\boxed{\,r^* = \tfrac{1}{\sqrt{6}} \approx 0.408\,}
$$

— and on this uniform-diagonal stratum the identity $\Phi = 7P - 1$ holds exactly, so $\Phi = 1$ coincides with $P = 2/7$: the integration threshold and the purity threshold fall on the exact same critical correlation.

**Number.** $r^* = 1/\sqrt{6} \approx 0.408$.

**Status.** `[T]` (the algebraic identities $\Phi(r) = 6r^2$, $\Phi = 7P - 1$, and $r^* = 1/\sqrt{6}$) / `[H]` (identifying equity-class correlation matrices with $\Gamma$).

**Test.** Empirically, mean cross-asset equity correlations often sit near $0.2$–$0.3$ in calm regimes and rise to $0.5$–$0.7$ during systemic crises. Under the `[H]` dictionary, $r^* \approx 0.408$ marks a candidate regime crossover from diversified (low-$\Phi$) to strongly coupled (high-$\Phi$) dynamics. By the third-order principle, **co-skewness** (the third standardized joint moment) provides a testable higher-order leading indicator prior to pairwise correlation spikes.

### §4.2 Discovery 10 — structural orbits and triadic forms {#d10}

**Dictionary `[I]`.** Formal classification of subsets of seven functional elements into symmetry classes.

**Derivation.** By `T-256` (`[T]` for the specified finite Fano collineation action + `[I]` for symbolic interpretation), under the collineation group $\mathrm{Aut}(\mathrm{PG}(2,2)) = \mathrm{PGL}(3,2) \cong \mathrm{PSL}(2,7)$ of order 168, the $2^7 - 1 = 127$ nonempty subsets of the seven axes partition into exactly **nine** orbit types. In particular, all $\binom{7}{2} = 21$ unordered pairs form a **single** orbit (2-transitivity, no pair is structurally distinguished), whereas the $\binom{7}{3} = 35$ triples split into **two** distinct orbits: the 7 collinear Fano lines and the 28 non-collinear triangles. Thus, within Fano combinatorics, **triads are the minimal subset size carrying nontrivial symmetry distinction**. Note strictly the scope of `T-256`: mapping real cultural or symbolic systems onto Fano subsets is an interpretation `[I]`; neither a universal classification of cultures nor empirical cross-cultural recurrence follows from finite-group orbit counting alone.

**Status.** `[T]` (nine nonempty collineation orbits and pair-vs-triple orbit splitting in `T-256`) / `[I]`–`[H]` (any mapping onto empirical cultural or institutional corpora).

**Test.** As an empirical corpus-linguistics hypothesis `[H]`, one may test whether stable institutional or conceptual classifications exhibit statistically elevated triadic incidence structures compared against matched dyadic baselines, controlling for base rates and coding bias.

---

## §5. Level V — physics: the senior sibling {#уровень-v}

Physics requires no separate catalogue entry here because it is the layer of the corpus where this third-order algebra was studied first: the cubic line functional mirrors the [Fano Yukawa selection rule](/docs/physics/gauge-symmetry/fano-selection-rules); the channel layer ($\Phi \to \Phi/9$) is the Fano pinching contraction; the code layer is Steane $= \mathrm{CSS}(H(7,4), H(7,4))$; and third-order bicoherence is the signal-processing analogue of a **three-point correlation function**.

---

## §6. Summary table of transfer constants {#сводная-таблица}

| Constant | Value | Structural role across domain templates |
|---|---|---|
| $P_{\text{crit}} = 2/7$ | $0.2857$ | purity threshold (structuredness cut) |
| Window $(2/7, 3/7]$ | width $1/7$ | viable conscious purity band (`T-124` `[T]`) |
| $R_{\text{th}} = 1/3$ | $0.3333$ | reflection threshold in state space (not a wall-clock time fraction) |
| $\Phi_{\text{th}} = 1 \iff r^* = 1/\sqrt6$ | $0.4082$ | integration threshold $\iff$ critical equicorrelation |
| Channel contraction | $1/9$ | off-diagonal $\Phi$ factor per Fano line-projected hop |
| Spectral gap of $\mathcal{P}_{\text{Fano}} - \mathrm{Id}$ | $2/3$ | off-diagonal relaxation rate under Fano pinching |
| $\kappa_{\text{bootstrap}} = 1/7$ | $0.1429$ | baseline regeneration scale |
| Pyramid | $21 \to 7 \to 3 \to 1$ | single-fault diagnostic compression (`T-224` `[T]`, `T-225` `[C]`) |
| $r_{\text{stab}}$ | $\sqrt{P - 1/7} - \sqrt{P_{\text{crit}} - 1/7}$ | Hilbert–Schmidt purity-shell stability radius (`T-104` `[T]`) |

---

## §7. Honest boundaries {#границы}

The first-order blind spot cuts both ways: it explains why Fano incidence is invisible to equal-weight pairwise statistics, but it also implies that **decisive empirical tests must be third-order**, and third-order sample statistics (bicoherence, co-skewness) carry much higher estimation variance and data requirements than pairwise correlations. Discovery 1's shutdown *ordering* holds in the dephasing-dominated model, whereas any specific time ratio is parametrization-dependent. Discoveries 2, 3, 9, and 10 are `[T]` on their algebraic identities and `[H]`/`[I]` on their domain dictionaries. The most direct empirical test is Discovery 1's line-resolved EEG bicoherence once a seven-channel encoder is fixed prior to testing. Above all, a domain transfer template earns empirical weight only by passing the self-checking mediator test in [§0](#движок): the finite combinatorics is `[T]`, while every real-world dictionary remains `[H]`/`[I]` until calibrated and tested.

---

**Related documents:**
- [Fano fingerprint (T-226)](/docs/applied/research/fano-fingerprint) — the first-order blind spot, polar/mediator partition, and fourteen rate sum rules.
- [Mathematical kernel (T-256)](/docs/reference/mathematical-kernel) — the nine nonempty Fano collineation orbits (`T-256 [T]+[I]`).
- [Gap diagnostics (T-257)](/docs/applied/research/gap-diagnostics) — canonical Singer cyclic Fano lines and rate-modulation hypotheses (`T-257 [H]`).
- [Σ-calculus (T-224/T-225)](/docs/applied/research/syndrome-calculus) — diagnosability rigidity (`T-224 [T]`), diagnostic pyramid (`T-225 [C]`), and Hamming/Steane code layer.
- [FANOS](/docs/applied/fanos/fanos-specification) — Discovery 7 developed as a reference distributed protocol.
- [SYNARC-Ω implementation](/docs/applied/coherence-cybernetics/implementation) — Discovery 8, agent architecture built around structural invariants.
- [Fano selection rules](/docs/physics/gauge-symmetry/fano-selection-rules) — the physical counterpart of the cubic selection layer.
