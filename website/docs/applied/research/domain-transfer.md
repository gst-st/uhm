---
sidebar_position: 9
title: Domain Transfer
description: "The generative layer — the third-order engine (mediators, closure law, self-checking dictionary) unfolded to full depth across ten domains, each with a derivation, a verified number, an honest status, and a falsifiable test."
---

# Domain Transfer: the generative layer

:::info What this document is
The seven-dimensional relation structure $\Gamma$ is not a bag of 49 numbers; it is a layered object whose specific information lives at **third order** (on triples, not pairs). Once that is seen — [§0](#движок) — it becomes a *transfer engine*: any domain onto which the seven axes map inherits the same rigid combinatorics. This document unfolds that engine across ten domains at full depth. Each entry has the same skeleton: **dictionary** (what maps to the seven axes) → **derivation** (the transferred computation) → **number** (machine-verified) → **status** (honest [Т]/[С]/[Г]) → **test** (a falsifiable prediction via the [self-checking dictionary](/docs/applied/research/one-grammar#самопроверяемость-словаря)). Every quantitative claim below is reproduced by the verifier `domain_transfer_verify.py`.
:::

## §0. The engine {#движок}

Four facts, each proved elsewhere in the corpus, compose into the transfer engine.

**(1) The first-order blind spot [Т].** The sum of the adjacency matrices of the seven Fano lines equals $J - I$ exactly — the adjacency of the complete graph $K_7$, spectrum $\{6, -1^6\}$. Any equal-weight pairwise statistic (covariance, two-point function, correlation) built from the lines is a function of $J-I$ alone, hence *indistinguishable from unstructured full connectivity*. Structure begins at three. Canonical home: [Fano fingerprint §0](/docs/applied/research/fano-fingerprint#слепое-пятно).

**(2) The mediator map [Т].** By the Steiner property $S(2,3,7)$, every pair $(i,j)$ lies on exactly one line, so it has a unique **mediator** $k^*(i,j)$ — the third point of that line (the [polar point $\pi(i,j)$ of T-226](/docs/applied/research/fano-fingerprint#полярное-разбиение)). The full table (verified, all 21 pairs):

| Line | Mediations inside the line |
|---|---|
| $\{A,S,L\}$ | $A\!\leftrightarrow\!S$ via $L$; $A\!\leftrightarrow\!L$ via $S$; $S\!\leftrightarrow\!L$ via $A$ |
| $\{A,D,E\}$ | $A\!\leftrightarrow\!D$ via $E$; $A\!\leftrightarrow\!E$ via $D$; $D\!\leftrightarrow\!E$ via $A$ |
| $\{A,O,U\}$ | $A\!\leftrightarrow\!O$ via $U$; $A\!\leftrightarrow\!U$ via $O$; $O\!\leftrightarrow\!U$ via $A$ |
| $\{S,D,O\}$ | $S\!\leftrightarrow\!D$ via $O$; $S\!\leftrightarrow\!O$ via $D$; $D\!\leftrightarrow\!O$ via $S$ |
| $\{S,E,U\}$ | $S\!\leftrightarrow\!E$ via $U$; $S\!\leftrightarrow\!U$ via $E$; $E\!\leftrightarrow\!U$ via $S$ |
| $\{D,L,U\}$ | $D\!\leftrightarrow\!L$ via $U$; $D\!\leftrightarrow\!U$ via $L$; $L\!\leftrightarrow\!U$ via $D$ |
| $\{L,E,O\}$ | $L\!\leftrightarrow\!E$ via $O$; $L\!\leftrightarrow\!O$ via $E$; $E\!\leftrightarrow\!O$ via $L$ |

Read it as a table of levers: to create or repair the link $(i,j)$ you need the two live links $(i,k^*)$ and $(k^*,j)$, and only those.

**(3) The closure law [Т].** Two coherences birth a third **iff** the triple is a line. The cubic line functional $W(\Gamma) = \sum_{\text{lines}} \mathrm{Re}(\gamma_{ij}\gamma_{jk}\gamma_{ki})$ has a gradient flow that, seeded on a path $A\!-\!S\!-\!L$ (both edges in the line $\{A,S,L\}$), feeds **exactly one** new edge — the closing $L\!-\!A$ — and, seeded on a cross-line path $A\!-\!S\!-\!E$, feeds **nothing** (verified). This is the selection rule: mediation is line-local.

**(4) The channel contraction $\Phi \to \Phi/9$ [Т].** The Fano channel (Kraus projectors onto the three-dimensional line-subspaces, complete because each point lies on three lines) preserves a population across all three of its lines ($3\times\tfrac13 = 1$) but preserves a coherence only in its single line out of three ($\times\tfrac13$); squared, that is $\tfrac19$. Verified: $\Phi_{\text{in}}/\Phi_{\text{out}} = 9.000000$ on random states. The nine is a Steiner incidence count, not a fit.

**The self-checking dictionary [Т-method].** These four make every domain mapping *falsifiable*, not interpretive: a correct mapping must reproduce the mediator table, and a chance mapping does so with probability $\sim(1/5)^7 \approx 3\times10^{-5}$ — see [one grammar §6](/docs/applied/research/one-grammar#самопроверяемость-словаря). This is the licence under which the domain readings below carry weight.

---

## §1. Level I — the individual mind {#уровень-i}

### §1.1 Discovery 1 — the clinic: an ordered shutdown, and the right instrument {#d1}

**Dictionary.** The seven axes are the interoceptive/cognitive channels of a single mind ($A$ articulation, $S$ structure, $D$ dynamics, $L$ logic, $E$ interiority, $O$ ground/clock, $U$ unity). Anaesthetic induction is modelled as dephasing $\dot\Gamma \supset \gamma_d(\mathrm{diag}\,\Gamma - \Gamma)$ over the coupling $H \propto J-I$.

**Derivation.** Dephasing attacks the *off-diagonal* (coherences) exponentially while the *diagonal* (populations) is inertial. Since $\Phi$ is a ratio of coherence-mass to population-mass and $P = \mathrm{Tr}(\Gamma^2)$ is dominated by the diagonal, the integration threshold $\Phi = 1$ is crossed **before** the viability threshold $P = 2/7$. This is an *ordered shutdown*: binding (unified experience) fails first, structuredness later.

**Number.** Over a sweep of $39$ viable conscious starts (initial purity and integration above threshold; three dephasing rates, three mixing weights, six seeds), $\Phi$ crossed $1$ before $P$ crossed $2/7$ in **39/39** cases. The *order* is robust; the *time-ratio* (in one parametrization, $t_P/t_\Phi \approx 1.09$) is not derived.

**Status.** **[С-model]** — the shutdown order is structural (integration is carried by coherences, which decohere first); the specific timescales depend on the dephasing model.

**Test.** Two predictions. (i) Under graded anaesthesia (propofol, sevoflurane, xenon), fronto-parietal *integration* markers should collapse **before** behavioural loss of responsiveness, in that order — consistent with the clinical picture of connectivity breakdown preceding unreactivity. (ii) **The right instrument is third-order.** By the first-order blind spot, PCI and spectral-power measures are two-point and *constitutionally cannot see the Fano geometry*; the discriminating instrument is **bicoherence** (the EEG triple spectrum). Prediction: channel-triples that map to Fano lines carry systematically higher bicoherence than the 28 non-line triples. This is runnable on existing EEG datasets and is the single cheapest decisive test of the whole transfer programme.

### §1.2 Discovery 2 — therapy as mediator engineering {#d2}

**Dictionary.** A broken or weak link between two faculties $(i,j)$ — say Interiority $E$ and Logic $L$ ("I cannot reason about what I feel").

**Derivation.** By the closure law, a severed coherence $(i,j)$ is **not** repaired head-on. It regenerates only through the two arms $(i,k^*)$ and $(k^*,j)$ that pass through the mediator $k^*(i,j)$. For $(E,L)$ the mediator is $O$ (Ground): $E\!\leftrightarrow\!L$ is reachable only via $O$. For $(A,E)$ it is $D$ (Dynamics): perception and feeling connect only through movement/time. These are read straight off the [mediator table](#движок), with no freedom to choose.

**Number / structure.** The table fixes all 21 repair routes uniquely; there is no tunable path, which is exactly what makes the protocol falsifiable.

**Status.** **[Т]** mechanism (closure law) / **[С]** clinical protocol.

**Test.** A protocol: diagnose the 21 links, find the break $(i,j)$, verify both arms through $k^*(i,j)$, and intervene on the *weaker arm* — never on $(i,j)$ directly. Prediction: interventions that strengthen the mediator arms regenerate the target link, while equal-effort direct work on $(i,j)$ does not. Because the mediator is fixed by the table, mis-specified "mediators" are a control condition and the protocol is falsifiable on outcome.

### §1.3 Discovery 3 — learning: the reflection budget and the schedule {#d3}

**Dictionary.** A learner acquiring a skill $(i,j)$; the self-model channel is the reflective loop (self-testing, metacognition, recall).

**Derivation.** The reflection threshold $R_{\mathrm{th}} = 1/3$ [Т] is not an aspiration but a floor: below one third of effort spent on the self-model, $R$ drops under the L2 gate and the material never consolidates into cognitive qualia. The [triple-lock learning bounds](/docs/applied/coherence-cybernetics/learning-bounds) $n_{\text{opt}} = \max(n_{\text{info}}, n_{\text{dyn}}, n_{\text{stab}})$ (T-109…T-112 [Т]) transfer directly: too little signal, too fast for integration, or destructively strong are the three separable failure causes. New skills consolidate **by line**: to fix $(i,j)$, train it in the triple with its mediator $k^*$.

**Number.** $R_{\mathrm{th}} = 1/3$ — one third of study time on reflection (self-testing/recall/teaching-back), as a theorem threshold, not a study tip.

**Status.** **[Т]** ($R_{\mathrm{th}}$, triple-lock) / **[Г]** (the specific skill$\leftrightarrow$axis dictionary).

**Test.** Spaced retrieval and interleaving already outperform massed study empirically; the sharp prediction here is the *fraction*: reflective time below $\sim 1/3$ should show a qualitative (not gradual) drop in retention, marking the $R = 1/3$ gate.

---

## §2. Level II — groups and organizations {#уровень-ii}

### §2.1 Discovery 4 — the Steiner protocol for team communication {#d4}

**Dictionary.** A team of seven roles has $\binom{7}{2} = 21$ pairwise working relationships to maintain.

**Derivation and optimality.** Cover the 21 pairs by three-person meetings. Each meeting of three covers $\binom{3}{2} = 3$ pairs, so at least $\lceil 21/3\rceil = 7$ meetings are needed, with equality **iff** an exact cover with no overlap exists — which is precisely a Steiner triple system $S(2,3,7)$, i.e. the Fano plane. The seven meetings

$$\{A,S,L\},\ \{A,D,E\},\ \{A,O,U\},\ \{S,D,O\},\ \{S,E,U\},\ \{D,L,U\},\ \{L,E,O\}$$

cover all 21 pairs exactly once, with attendance load **exactly 3** per member and zero redundancy — a verified optimum. **Fault tolerance:** because any two lines of a projective plane meet in exactly one point, after the loss of *any* single member all $\binom{6}{2}=15$ surviving pairs still share a meeting (verified for every removed node). Each conflict $(i,j)$ has a single designated meeting and a single designated **mediator** $k^*(i,j)$.

**Number.** 7 meetings, load 3 each, 0 overlap, single-fault-tolerant — all machine-verified.

**Status.** **[Т-structure]** (the covering optimality and fault tolerance are theorems) / **[С]** (the "roles map to the seven axes" dictionary).

**Test.** Against an ad-hoc meeting schedule, the Steiner schedule is predicted to maintain all pairwise relationships at lower total meeting-load and to degrade gracefully under absence; a schedule that omits any line leaves exactly three pair-relations uncovered — a concrete, checkable failure mode.

### §2.2 Discovery 5 — the ceiling of vertical composition {#d5}

**Dictionary.** Nested subjecthood: individual → team → organization.

**Derivation.** $\mathrm{SAD}_{\max} = 3$ [Т] (T-142): subjecthood does not compose beyond three levels. Structures deeper than three subject-floors do not form a fourth subject — they form **administration**, an ecology of organizations rather than a larger mind (the same ceiling that makes a UHM-compliant super-intelligence necessarily an *ecology*, [App. K](/docs/applied/coherence-cybernetics/theorems), S-14).

**Status.** **[Т]** (the ceiling) / **[И]** (the organizational reading).

**Design consequence.** Build mega-structures as ecologies of $\leq 3$-deep subjects, not as a single agent scaled without limit; expect the fourth tier to behave as coordination, not cognition.

---

## §3. Level III — machines {#уровень-iii}

### §3.1 Discovery 6 — the seven as a native error-correcting code {#d6}

**Dictionary.** Any seven-channel architecture: an agent with seven sectors, a seven-mode photonic chip, a seven-service cluster.

**Derivation.** The Fano incidence *is* the parity-check matrix of the Hamming code $H(7,4)$: the sixteen codewords include exactly seven of weight 3, and their supports form an $S(2,3,7)$ — so **Hamming$(7,4)$ and the Fano plane are one object** (any $S(2,3,7)$ is isomorphic to Fano). The Steane quantum code is $\mathrm{CSS}(\text{Hamming},\text{Hamming})$ — the quantum lift of the same structure ([Σ-calculus T-224/T-225](/docs/applied/research/syndrome-calculus)). Consequently a seven-holon carries a **native distance-3 code**: one corrupted component is localized by three syndrome checks — the pyramid $21 \to 7 \to 3 \to 1$ (21 pair-checks $\to$ 7 axes $\to$ 3 syndrome bits $\to$ 1 verdict). Verified: the three-bit syndrome decodes the fault position exactly for all seven single-error patterns.

**Number.** $[n,k,d] = [7,4,3]$: corrects single errors, detects double; three checks localize one of seven.

**Status.** **[Т]**.

**Test.** Any seven-channel system instrumented for per-channel health should be able to localize a single degraded channel from three parity checks alone, without probing all 21 pairwise relations — a directly buildable diagnostic.

### §3.2 Discovery 7 — distributed systems: buses, not point-to-point {#d7}

Replace 21 pairwise channels by **7 triple-buses** (the lines): each node sits on exactly 3 buses (uniform load, a consequence of the 2-transitivity of $\mathrm{PSL}(2,7)$), any two buses intersect (guaranteed rendezvous), and routing repair follows the closure law — a path $(i\to j)$ regenerates only through $k^*(i,j)$, a deterministic fallback with no routing tables. This discovery is developed to full depth as a reference protocol in [FANOS](/docs/applied/fanos/fanos-specification); here it is one instance of the same engine. **[Т]**.

### §3.3 Discovery 8 — the agent's constitution from constants {#d8}

A UHM-compliant agent is governed by theorem-fixed dials, not hyperparameters: reflection budget $\geq 1/3$ ($R_{\mathrm{th}}$); purity window $(2/7, 3/7]$ with update-strength ceiling $r_{\mathrm{stab}} = \sqrt{P - 2/7}$ (T-104); composition $\leq 3$ (SAD); inter-module coherence attenuating $\times 1/9$ per line-projected hop; **line-aware routing** (a mixture-of-experts blind to the lines pays that ninefold integration loss); and **grokking as a $\Phi$-crossing** (the delayed generalization jump predicted to be block-integration $\Phi$ crossing 1). Developed to full depth in the [SYNARC-Ω specification](/docs/applied/coherence-cybernetics/implementation); a *constitution from constants*. **[Т]**-arithmetic / **[С]**-dictionary.

---

## §4. Level IV — markets and society {#уровень-iv}

### §4.1 Discovery 9 — the critical correlation of systemic risk {#d9}

**Dictionary.** A market or portfolio of seven asset classes; $\Gamma$ is the (equicorrelation) correlation structure $\Gamma = \big((1-r)I + rJ\big)/7$ with mean pairwise correlation $r$.

**Derivation.** For the equicorrelation matrix, integration is exactly quadratic in $r$:

$$
\Phi(r) \;=\; \frac{\sum_{\text{off}} |\gamma|^2}{\sum_{\text{diag}} |\gamma|^2} \;=\; \frac{42\,(r/7)^2}{7\,(1/7)^2} \;=\; 6r^2,
$$

so the integration threshold $\Phi = 1$ is reached at

$$
\boxed{\,r^* = \tfrac{1}{\sqrt{6}} \approx 0.408\,}
$$

— and on this stratum the identity $\Phi = 7P - 1$ holds, so $\Phi = 1$ coincides *exactly* with $P = 2/7$: the integration threshold and the viability threshold fall on the same correlation. Verified: $\Phi(r) = 6r^2$ to machine precision, $\Phi = 7P-1$ on the stratum, $r^* = 1/\sqrt6$ with $P = 2/7$ simultaneously.

**Number.** $r^* = 1/\sqrt{6} \approx 0.408$.

**Status.** **[Т-arithmetic]** (the $\Phi = 6r^2$ law and $r^*$) / **[Г-dictionary]** (assets $\leftrightarrow$ axes).

**Test.** A stylized market fact: mean equity correlations run $\sim 0.2$–$0.3$ in calm years and jump to $0.5$–$0.7$ in crises. The threshold $r^* \approx 0.408$ separates the regimes: below it the market is *pre-integrated* and diversification works; above it the market moves as **one subject** and diversification is illusory. And, once more, the third-order principle: the leading indicator of the transition is not the correlation (a lagging, second-order quantity) but the **co-skewness** — the third moment, an existing econometric instrument — which should rise before the correlation does.

### §4.2 Discovery 10 — cultural engineering: why triads {#d10}

**Dictionary.** Stable symbolic/cultural forms as configurations of the seven axes.

**Derivation.** [T-256 [Т+И]](/docs/applied/research/one-grammar#t-256) already establishes that symbolic systems are orbits of Fano subconfigurations under $\mathrm{Aut} = \mathrm{PSL}(2,7)$ of order 168 — cross-cultural recurrence as a theorem. The third-order principle adds a sharp corollary: **stable cultural forms are triadic, not dyadic** — triads of deities, three branches of power, triples of archetypes — because the triple is the *minimal carrier of distinguishable structure* while a pair is structureless under $\mathrm{Aut}$ (one orbit, §0).

**Status.** **[Т]** (third-order $\Rightarrow$ triads are the minimal structured unit) / **[Г]** (the specific cultural mapping).

**Test.** On mythology and institutional corpora, the frequency of stable **triads** should exceed that of stable **dyads**, controlling for base rates — a corpus-linguistics measurement.

---

## §5. Level V — physics: the senior sibling {#уровень-v}

Physics needs no separate catalogue entry: it is the corpus layer where the engine was **first** applied, and every discovery above is a younger sibling of a physical one. The cubic vision is the [Fano Yukawa selection rule [Т]](/docs/physics/gauge-symmetry/fano-selection-rules); the channel layer ($\times 1/9$) is the [FSQCE $\Phi$-contraction [Т]](/docs/applied/coherence-cybernetics/theorems); the code layer is Steane $= \mathrm{CSS}$; and "bicoherence" is what physics calls the **three-point function**. The programme did not borrow from physics; physics was the first domain to be read by the same seven.

---

## §6. Summary table of transfer constants {#сводная-таблица}

| Constant | Value | Role across domains |
|---|---|---|
| $P_{\text{crit}} = 2/7$ | $0.2857$ | structuredness threshold (system / dataset / market) |
| Window $(2/7, 3/7]$ | width $1/7$ | operating band of subjecthood |
| $R_{\text{th}} = 1/3$ | $0.3333$ | minimum reflection budget |
| $\Phi_{\text{th}} = 1 \iff r^* = 1/\sqrt6$ | $0.4082$ | integration threshold $\iff$ critical mean correlation |
| Channel contraction | $1/9$ | cost per coarse (line-projected) hop |
| Spectral gap $\mathcal{L}_0$ | $2/3$ | forgetting / relaxation rate |
| $\kappa_{\text{bootstrap}} = 1/7$ | $0.1429$ | minimal regeneration |
| Cascade ceiling | $4/3$ (at $N=2,3$) | multiplication limit (photovoltaics, org cascades) |
| $\mathrm{SAD}_{\max}$ | $3$ | ceiling of subject-composition depth |
| Pyramid | $21 \to 7 \to 3 \to 1$ | universal diagnostic protocol |
| $r_{\text{stab}} = \sqrt{P - 2/7}$ | — | admissible intervention / update strength |

---

## §7. Honest boundaries {#границы}

The second-order blind spot cuts both ways: it explains why the seven were never seen in ordinary statistics, but it also means **the decisive experiments are third-order**, and triple statistics need orders of magnitude more data than pairwise ones (third moments have large variance). Discovery 1's time-*ratio* is one parametrization — the *order* is structural, the ratio is not. Discoveries 9–10 are **[Г]** on the dictionary while **[Т]** on the arithmetic. The cheapest decisive test of the entire programme is Discovery 1's line-resolved bicoherence, precisely because the data already exist. And every mapping is licensed only insofar as it passes the [self-checking dictionary](/docs/applied/research/one-grammar#самопроверяемость-словаря): the interpretation is optional, the third-order combinatorics is not.

---

**Related documents:**
- [Fano fingerprint (T-226)](/docs/applied/research/fano-fingerprint) — the first-order blind spot, the polar/mediator partition, the fourteen rate-identities.
- [The One Grammar (T-256/T-257)](/docs/applied/research/one-grammar) — the classification of charts and the self-checking dictionary that licenses every mapping here.
- [Σ-calculus (T-224/T-225)](/docs/applied/research/syndrome-calculus) — the diagnosability pyramid and the Hamming/Steane code layer of Discovery 6.
- [FANOS](/docs/applied/fanos/fanos-specification) — Discovery 7 developed as a reference distributed protocol.
- [SYNARC-Ω implementation](/docs/applied/coherence-cybernetics/implementation) — Discovery 8, the agent's constitution from constants.
- [Fano selection rules](/docs/physics/gauge-symmetry/fano-selection-rules) — the physical senior sibling of the cubic layer.
