---
sidebar_position: 13
title: HOLARCH
description: "The holonic meta-specification of digital architecture: seven concerns, 21 typed channels, four computable viability invariants, three-flow dynamics, a composition algebra and a bounded-depth federation budget — compared against UML, C4, SysML v2, DDD, VSM, MAPE-K and the 2024–2026 agentic stack"
---

# HOLARCH: the holonic meta-specification of digital architecture

**Status frame.** This page is an engineering meta-specification, not a set of new
theorems. Every claim carries one of four honesty classes: **VERIFIED** — a computed
fact about the machinery (theorem arithmetic, identity checks, coverage completeness;
reproduced by the laboratory panel HL01–HL14, 14/14);
**DESIGN** — self-consistency of an engineering instance (true by construction,
demonstrated, *not* evidence about external systems); **CONS** — a numerical consonance
with an external published number (a structural rhyme stated precisely, never an
identity claim); **OPEN** — needs field data, with the protocol stated. Imported UHM
mathematics keeps its registry statuses [T]/[C]/[H]/[D]/[I]. The projection from
Γ-mathematics onto software engineering is itself an [D]-definition plus an
[I]-dictionary — structured, configurable, testable; never a fact.

## §1. The door and the claim {#дверь}

If UHM is what the corpus argues it is — a minimal state space with theorems about
viability, self-observation, integration, differentiation, composition and depth —
then digital systems, which are also organized wholes fighting entropy on a substrate,
should not need a *separate* architecture theory. The architecture of a mixnet, a
blockchain, an operating system and an AI-agent platform should crystallize out of one
meta-specification, the way the corpus already crystallized a network fabric
([FANOS](/docs/applied/fanos/fanos-specification)), an AI organism (SYNARC-Ω), and a
navigation machine ([the Prime Radiant](./prime-radiant.md)) — each built by hand, each
converging on the same organs.

HOLARCH is that meta-specification, stated once and audited against the existing field.
The design goal is **zero hidden speculation** and **explicit traceability to established
architectural practices**: §18 compares 44 architectural concerns and capabilities across
major frameworks — from UML 2.5.1 to SysML v2 (2025), C4, ArchiMate, ISO 42010, DDD, VSM,
MAPE-K, Erlang/OTP, Kubernetes, TLA+, Spec Kit, AGENTS.md, MCP and A2A — distinguishing
where HOLARCH provides a **native modeling construct**, where an external notation,
verifier, or execution platform is **retained/embedded**, and where real engineering gaps
remain (§19). HOLARCH operates strictly at the **design-level meta-specification layer**:
it classifies and constrains architecture; it does **not** replace production runtimes
(such as Kubernetes or Erlang/OTP), formally verified kernels (such as seL4), or mature
diagramming toolchains. The laboratory re-checks that every row of §18 resolves to a
section of this page (HL07).

What HOLARCH is *not*: it is not a notation (it emits notations), not a runtime or kernel,
not a process (it contains one as a component), and not a pattern catalog (patterns become
typed channel configurations). It is a computable semantic layer: a **fixed alphabet of
concerns; a complete typed taxonomy of couplings; computable viability invariants with
explicit cuts; dynamics, self-model, composition and bounded-depth federation as
first-class modeling constructs**. Existing notations become projections of one computable
object — the way the same building casts a floor plan, a wiring diagram and an elevation.

## §2. The landscape: what sixty years actually taught {#ландшафт}

Before building, the strongest available test of *need* is comparative: lay out the
mature lineage and see what each branch got permanently right and where every branch
stopped. The reading of each row is [I] over published, uncontested history.

**Wave 1 — notations and description languages.** Academic ADLs of the 1990s (Wright,
Rapide, Darwin, ACME…) had precise semantics and died in niches; surveys agree none
became practitioner tools except domain-locked AADL in embedded avionics. UML won the
documentation war instead — a rich diagram vocabulary over a MOF metamodel — and paid
for breadth with semantic looseness: practitioners use it selectively and informally,
as sketches. C4 (Brown) then won pragmatically inside software teams by fixing a single
axis UML left implicit: **zoom** — context → containers → components → code, "maps, not
models". ArchiMate 3.2 standardized enterprise layering with a relationship taxonomy;
ISO/IEC/IEEE 42010:2022 standardized the *discipline* around any of them: stakeholders,
concerns, viewpoints, views, correspondences. The freshest turn is SysML v2 with KerML
(OMG final adoption, July 2025): textual, git-native, API-first — the notation world
itself concluding that models must be **computable artifacts**, not pictures. What no
notation ever had: a criterion for *which* boxes must exist, any number that says the
described system will live, and any account of runtime dynamics.

**Wave 2 — decomposition criteria.** Parnas (1972) gave the deepest single sentence of
the lineage: decompose around **information hiding** — each module hides a design
decision. Simon (1962) proved the structural side: viable complex systems are
**nearly decomposable** — dense within blocks, sparse but *nonzero* between them.
DDD (Evans 2003) rediscovered both at domain scale: bounded contexts with explicit
context maps. Hexagonal/Clean architectures fixed the direction of dependencies
(ports and adapters around a protected core). DSM — the design structure matrix —
put dependencies into a square matrix and clustered it. Each of these is a *fragment*
of the same object: a state matrix with protected interiority, sparse typed
off-diagonals and a dependency geometry. None of them has the matrix itself with
its thresholds.

**Wave 3 — viability and control.** Cybernetics built the missing dynamical half.
Beer's Viable System Model: five recursively nested systems and the criterion of
**viability** — plus the algedonic (pain/pleasure) channel that bypasses hierarchy in
emergencies. IBM's MAPE-K (2003): the autonomic loop Monitor–Analyze–Plan–Execute over
shared Knowledge. Erlang/OTP: supervision trees and "let it crash" — repair by
**replacement**, not by in-place surgery. Kubernetes generalized the same move into
desired-state reconciliation; crash-only software (Candea–Fox 2003) made restart the
*only* code path. The Reactive Manifesto compressed the operational creed into four
words (responsive, resilient, elastic, message-driven). What this wave never had: a
state space in which "viable" is a theorem rather than a slogan, and any bridge to the
structural wave — VSM and UML do not compose.

**Wave 4 — the agentic turn, 2024–2026.** When AI agents became the builders, the spec
came back to the center of gravity. GitHub's Spec Kit: constitution → specify → plan →
tasks → implement, with the constitution holding non-negotiable principles. AGENTS.md
(formalized August 2025; tens of thousands of repositories within months): a
machine-readable "README for machines". MCP standardized tool contracts (SDK downloads
at React-scale within 16 months); A2A v1.0 (April 2026) standardized agent-to-agent
peering. Anthropic's agent-pattern canon separated workflows from agents and named the
recurring organs: orchestrator–workers, evaluator–optimizer, routing, reflection.
The wave's own diagnosis, visible in its artifacts: agents need **structured,
checkable context** — yet the spec files themselves remain prose. A constitution
nothing can compute is advice, not law.

**The diagnosis, in one place.** Across all four waves, seven capabilities are
systematically absent, and they are exactly the seven UHM supplies as mathematics:

1. a **fixed alphabet of concerns** with a rigidity theorem for single-fault localizability — supplied by N=7 diagnosability rigidity, T-224 [T];
2. a **complete typed taxonomy of couplings** — supplied by the 21 coherences of Γ;
3. **numeric viability invariants** with declared cuts [D] and proven independence/robustness — P, R, Φ, D (T-124b/d [T], T-129 [D], T-151 [D]);
4. **dynamics as first-class** — a three-flow grouping [D] with dephasing-model spectral/Onsager identities, T-262 [T at specified dephasing model] (diagonal kernel; not a Riemannian metric or $G_2$-covariant);
5. a **self-model with an anti-Goodhart discipline** — φ(Γ), T-96/T-191 [T under stated model/contraction hypotheses]; T-222 [T] adds that in the high-temperature Rényi model no resource vector can stand in for the target;
6. an **exact block-purity identity with an explicit comparison** — T-77 [T]; operational benefit remains a separate obligation;
7. a **score-convention depth ladder and bounded-depth federation budget** — T-142 [T at specified SAD score convention] and T-304 [D]+[H] (the universal depth ceiling T-217 is withdrawn [✗]).

The rest of this page states the meta-specification (§3–§14), runs it through three
worked designs (§15–§17), presents the comparative capability mapping (§18), and attacks it (§19).

## §3. The signature of an architectural holon {#холон}

**[D] Definition.** An architectural holon is a five-tuple

$$
h \;=\; \langle\, \Gamma,\; B,\; \varphi,\; \mathcal{L},\; C \,\rangle
$$

— **state** $\Gamma \in D(\mathbb{C}^7)$, a positive semidefinite unit-trace 7×7
matrix over the seven concerns (§4): the diagonal is the budget each concern actually
commands; the off-diagonal is the live coupling between concerns (§5); — **boundary**
$B$: what is inside the holon's interiority and what crosses only through contracts
(the bounded context of DDD, made load-bearing); — **self-model** $\varphi(\Gamma)$:
the holon's own computable account of its state (§8); — **dynamics** $\mathcal{L}$:
the three-flow evolution law (§7); — **contracts** $C$: the typed channels to other
holons (§9).

For a reader arriving from the engineering side: $\Gamma$ is the **design structure
matrix grown up**. A DSM records that module *i* touches module *j*; $\Gamma$ records
it as a physical state — positive semidefinite (so the couplings must be *jointly
realizable*, not an arbitrary wish-list; §12 shows this constraint biting), unit-trace
(so budgets are a real distribution, and concentration is measurable), typed (each
cell has a canonical name and semantics), and equipped with invariants and an
evolution law. Everything downstream — verdicts, ablations, views — is computed from
this one object. A system is then a **holarchy**: a bounded-depth tree of holons (§10)
with contracts on the edges — the corpus's
[holarchic hierarchy](/docs/consciousness/hierarchy/interiority-hierarchy) restricted to
engineered systems.

## §4. The seven aspects {#аспекты}

The seven concerns are the seven dimensions of Γ, with their canonical corpus names
(the [SSOT](/docs/core/dynamics/coherence-matrix) `src/data/coherences.ts`; the
laboratory check HL01 keeps this table drift-free), each given its engineering
reading. The reading is an [I]-dictionary: structured and testable, never a fact.

| # | Aspect | Canon meaning | Engineering reading — what lives here |
|---|--------|---------------|----------------------------------------|
| **A** | **Articulation** | distinguishing activity | ingress and perception: parsing, validation, feature extraction, raw telemetry intake, API surface of *distinctions the system can make* |
| **S** | **Structure** | form stability | schemas, types, data structures, configuration, wire formats — *what stays fixed while the system runs* |
| **D** | **Dynamics** | process activity | execution paths, pipelines, transactions, actuation, delivery — *what moves* |
| **L** | **Logic** | internal consistency | invariants, contracts, verification, consensus rules, cryptographic laws — *what must reconcile without contradiction* |
| **E** | **Interiority** | intensity of interior states | private state, memory, context, hidden pools, secrets — *what is visible only from inside* (Parnas's information hiding as an axis with a measure, not as advice) |
| **O** | **Ground** | connection to source | substrate and supply: runtime, transport, storage, energy, budget, stake — *what the system stands on and feeds from* |
| **U** | **Unity** | integration | identity and orchestration: the one canonical whole, governance, goal — *what makes the parts one system* |

Three things distinguish this from every "N-layer" scheme in the lineage.

**The count is forced, not chosen.** Theorem Σ
([T-224](/docs/applied/research/syndrome-calculus#t-224) [T]) proves that perfect
single-fault localizability with a nontrivial state grammar forces $n \ge 7$ axes, and
at $n = 7$ the grammar is *unique up to relabeling* (Hamming (7,4) = the Fano plane);
at every larger admissible size uniqueness fails. Seven concerns with Fano wiring is
the one alphabet where a single failing aspect is *localizable by design*. OSI's seven
layers, Zachman's six interrogatives, C4's four zooms are conventions; this is the
only such number carrying a rigidity theorem — which is also why HOLARCH does not
treat OSI as a cousin: OSI is a linear encapsulation ladder (a depth structure, §10),
not an aspect decomposition, and pretending otherwise would be numerology.

**Every aspect carries a stress gauge.** The σ-panel
([T-92](/docs/reference/status-registry) [D]) defines for each
aspect a computable depletion signal: $\sigma_k = \mathrm{clamp}(1 - 7\gamma_{kk},
0, 1)$ for A, S, D, L, O; $\sigma_E = (7 - D_{\mathrm{diff}})/5$ and $\sigma_U =
2/(1+\Phi)$ measure the *remaining headroom* of differentiation and integration —
so for ordinary viable systems σ_E and σ_U sit high, and that is normal: they read
distance to the ideal, not distance to the floor.

**The aspects are axes, not modules.** A microservice, a subsystem, a team — each is a
holon with its *own* 7-profile. "Where does the scheduler go?" is answered not by
filing it in a drawer but by writing its budget vector: a scheduler is D-heavy with L
and O couplings. The profile — the diagonal of Γ — is the component's character
passport, and misfiled character (an "L-service" quietly doing E-work) shows up as
coupling anomalies, not as a filing dispute.

## §5. The 21 typed channels {#каналы}

Any dependency between two concerns — inside one holon or across a contract — is
typed by an unordered pair of aspects: $\binom{7}{2} = 21$ channels, and the corpus
already named all 21 (same SSOT; HL01). The names were minted for the theory of
consciousness years before this page; read the middle column and watch them land on
engineering unmodified — this "the dictionary was already correct" effect is the
strongest [I]-evidence on the page.

| Channel | Canon name | Engineering reading (examples) |
|---------|-----------|--------------------------------|
| AS | Morphogenesis | parsing into schema; schema-on-write ingestion |
| AD | Actualization | event triggers process: event-driven activation |
| AL | Predication | observation becomes a predicate: validation rules, alert conditions |
| AE | Apperception | input enters interiority: **context engineering**, telemetry → memory |
| AO | Spontaneity | substrate-born events: interrupts, timers, entropy sources |
| AU | Differentiation | distinctions that keep the whole intact: tenancy, routing without fragmentation |
| SD | Persistence | form maintained through process: state machines, durable state, migrations |
| SL | Nomos | structure with logical force: typed contracts, schema constraints (**MCP** lives on AS+SL) |
| SE | Representation | structure mirrored inside: indexes, materialized views, caches |
| SO | Archetype | form rooted in substrate: data layout, memory allocation, ISA fit |
| SU | Symmetry | structural expression of unity: **replication**, sharding symmetry, consistent hashing |
| DL | Regulation | logically governed process: control loops, schedulers, consensus rounds |
| DE | Affection | process writes interiority: write paths, event-sourcing appends |
| DO | Genesis | generative process from substrate: bootstrap, provisioning, spawn |
| DU | Teleology | integrated directed change: **desired-state reconciliation** (the Kubernetes loop is this channel verbatim), rollouts |
| LE | Evidence | logic inside interiority: audit logs, attestations, transactional integrity, **evals** |
| LO | Grounding | logic rooted in substrate: verified kernels (seL4), proof-of-stake/work — law priced in ground |
| LU | Consistency | non-contradiction of the whole: linearizability, finality, system invariants |
| EO | Immanence | ground felt inside: **backpressure**, resource-awareness, data locality |
| EU | Synthesis | interior content gathered into one: state aggregation, global snapshots, observability rollup |
| OU | Completeness | identity of source and whole: capacity accounting, **data availability**, sovereignty of supply |

Two structural facts elevate this from a naming exercise.

**Completeness [D].** The classic coupling taxonomies embed: structured design's
content/common/control/stamp/data coupling, ArchiMate's relationship set, UML
dependency kinds — each instance lands in a typed cell (matrix rows in §18; checked
non-empty by HL07). The claim "here is a dependency no pair of aspects can type" is
one of the explicit falsifiers in §19.

**Pairs are probes' floor, not their ceiling.** The seven Fano lines
({A,S,L}, {S,D,E}, {D,L,U}, {L,E,O}, {E,U,A}, {U,O,S}, {O,A,D}) are the minimal honest
*diagnostic* units: the corpus proves first-order blindness
([T-226](/docs/applied/research/fano-fingerprint#t-226) [T]) — the equal-weight sum of
line-adjacency matrices is exactly $J - I$, so **any equal-weight pairwise statistic
sees no structure at all**. The laboratory re-derives the identity (HL13). The
engineering consequence is immediate and non-obvious: a monitoring mesh of pairwise
heartbeats is provably structure-blind; observability must probe **triads** (this is
the FANOS "diagnosis on triples" imported upward). HOLARCH therefore ships a
**Fano-coverage meter**: the count (0–7) of lines all three of whose edges carry
above-median coupling. The three worked designs of this page score 2, 2, 1 —
nontrivial, *not* saturated, and reported as a deficit gauge, not a rubber stamp
(HL10). The meter carries **no pass threshold**, and deliberately so: raising a
diagnostic reading by rewiring the design under test is exactly what the
anti-Goodhart clause of §8 forbids. A low count is information about the design,
not a grade to be optimised away.

## §6. The four viability invariants {#инварианты}

Everything in this section imports corpus state-space functionals; the engineering layer
chooses what to feed them. For a design, Γ is assembled from declared budgets and flows
(§12, §14); at runtime, from measurement. Four numbers then form the verdict, using
**declared threshold cuts `[D]`** whose mutual independence, Lipschitz robustness, and
algebraic interrelations are proven theorems ([viability](/docs/core/dynamics/viability),
[T-124b](/docs/proofs/consciousness/conscious-window#t-124b) [T],
[T-124d](/docs/proofs/consciousness/conscious-window#t-124d) [T]):

| Invariant | Formula | Threshold cut | Guards against — the named pathology |
|-----------|---------|---------------|--------------------------------------|
| V1 Distinguishability | $P = \mathrm{Tr}(\Gamma^2)$ | $P > 2/7$ **[D]** (non-empty window T-124 [T]; $\Phi\ge1\Rightarrow P\ge2/7$ T-129a [T]) | **mud**: the big ball — activity smeared until the system is statistically indistinguishable from noise |
| V2 Reflection | $R \ge 1/3$ **[D]**; algebraic lower-bound identity $R = 1/(7P) \iff P \le 3/7$ [T] | $R \ge 1/3$ **[D]** | **crystal/monolith**: one global pattern eats the system; nothing is left to observe it |
| V3 Integration | $\Phi = \sum_{i \ne j}\lvert\gamma_{ij}\rvert^2 / \sum_i \gamma_{ii}^2$ | $\Phi \ge 1$ **[D]** (T-129 [D]; one-way purity bound T-129a [T]) | **fragmentation**: parts without binding — the microservice archipelago with no real contracts |
| V4 Differentiation | 7D native proxy $D^{7D} = 1 + 6\,\mathrm{Coh}_E$ [D] (canonical $D_{\mathrm{diff}}=\exp S_{\mathrm{vN}}(\rho_E)$ on extended $\mathcal{H}_E$) | $D \ge 2$ **[D]** (T-151 [D]) | **rigidity**: a single-mode system — no degraded mode, no second regime to fall back to |

Four properties make this table an instrument rather than a metaphor.

**Independence.** T-124b [T] exhibits four constructive counterexamples: drop any one
threshold and a specific pathological state slips through. The four sicknesses above
are those counterexamples wearing engineering names. The laboratory demonstrates the
same pattern *constructively* on every worked design: four targeted ablations — smear
into background, collapse into one mode, cut the shared flows, unplug interiority —
each break **exactly their own invariant** (HL04–HL06, DESIGN).

**Robustness.** T-124d [T]: all four measures respond $O(\varepsilon)$ to
$O(\varepsilon)$ state noise — no threshold has divergent sensitivity, so a noisy
telemetry pipeline cannot flip a verdict by itself.

**The window.** V1 and V2 together bound a corridor: $P \in (2/7,\, 3/7]$ in the
lower-bound form — organized enough to exist, not so consolidated that reflection
dies. This is the corpus's Goldilocks window (T-124), and it is the **agentic tier**:
a system inside the window with $\Phi \ge 1$, $D \ge 2$ has the structural
prerequisites of a self-steering system. Ordinary services live legitimately below
the full conjunction (viable, not agentic); the ladder of tiers is the corpus's
[interiority hierarchy](/docs/consciousness/hierarchy/interiority-hierarchy) L0–L4.
For real self-models the canonical R is a lower bound; the operative measure is
$R_\varphi$ — self-model fidelity (§8).

**Anti-dominance reads sideways.** The V2 ceiling is an anti-concentration law: no
single pattern above ~3/7 of the whole. Two independent engineering communities
converged on the same *shape* of law: BFT consensus tolerates strictly less than 1/3
faulty weight (quorum intersection arithmetic), and Ethereum's client-diversity
practice treats any client above 1/3 as dangerous and above 2/3 as
finality-breaking. The laboratory states both sides precisely and marks the rhyme
**CONS/[I]** — same fraction, different bases (validator weight vs purity); a
structural consonance, not an identity (HL09, HL14).

## §7. Dynamics: the three flows {#динамика}

An architecture that only describes standing structure describes a corpse. HOLARCH organizes
evolution into a **three-flow modeling decomposition `[D]`** (a chosen grouping of
unitary, dissipative, and regenerative terms rather than a unique categorical exhaustion
of all GKSL generators). Within the **specified dephasing model**,
[T-262](/docs/core/dynamics/evolution#теорема-динамическая-трихотомия)
(**[T at specified dephasing model]**) establishes unitary spectral invariance,
nonnegative dephasing entropy production, and a positive semidefinite Onsager identity —
noting explicitly that the operator has a **diagonal kernel** and is **neither a
Riemannian metric nor $G_2$-covariant**:

1. **Work — the unitary flow**: transformations that preserve every spectral
   functional. Engineering: the reversible moves — refactorings that provably keep
   behavior, blue-green switchovers, live migrations. What characterizes them: they
   cost energy, never structure.
2. **Heat — the dissipative flow**: dephasing/entropy production at rate γ; the
   system relaxing toward grey. Engineering: bitrot, dependency drift, config
   entropy, knowledge evaporation. This flow is *never zero*; pretending otherwise
   is how systems die politely.
3. **Matter — the regenerative flow** ℛ: replacement toward a target $\rho^*$.
   Engineering: supervision restarts, immutable-infra redeploys, crash-only
   recovery — repair by **replacement**, not surgery (conceptually aligned with
   Erlang/OTP supervision and Kubernetes desired-state reconciliation).

Model-conditional corpus results give the flows quantitative benchmarks:

- **No supply, no being.** Under the specified linear unital channel, purity is
  non-increasing ([T-288](/docs/reference/status-registry) **[T under the specified
  linear unital channel]**; strict decay to $1/7$ requires primitivity). Under the
  specified affine driven injection model with depolarizing dissipation and a fixed
  replacement state, stationary purity depends on the drive-to-dissipation ratio
  (numerically $(r/\gamma)_c \approx 7$ in the reference parametrization;
  T-289 **[T under the specified affine driven injection model]**). An architecture
  document that does not state its supply loop has not stated the system.
- **The silver floor.** In the stationary isotropic fixed-target feeding model (T-259 **[T in the model]**), the
  maintenance-to-decay ratio $x = \kappa_{\mathrm{eff}}/\Gamma_2$ must exceed
  $1 + \sqrt{2} \approx 2.414$ for the stationary branch to hold above the $2/7$ floor — the
  laboratory reproduces the fold: $x = 0.9\,x_{\min}$ starves ($P_\infty = 0.277 <
  2/7$), $x_{\min}$ lands exactly on the floor, $1.3\,x_{\min}$ lives
  ($P_\infty = 0.307$) (HL12). Engineering rule of thumb: **a system whose
  regeneration tempo falls below its model-specific entropy-balance threshold is
  dissolving, whatever the roadmap says.**
- **Halt and reignition.** In the same driven model, cutting the drive returns the
  state monotonically toward $I/7$ (time scale $\sim 0.49/\gamma$ in the reference
  run, T-288/T-289), matching the crash-only design discipline (recovery = the one
  and only start path).
- **The algedonic wire.** Under a specified differentiable injection field, purity
  flux $\dot P = 2a\,\mathrm{Tr}(\rho(\sigma-\rho))$ (T-103 **[T at specified
  differentiable injection field] + [I]**; sign is state-dependent and hedonic
  reading is an interpretation) serves as a compact VSM-style algedonic scalar
  signaling whether organization is rising or falling.

## §8. The self-model and the anti-Goodhart clause {#самомодель}

Every wave-3 loop (MAPE-K's Knowledge, Kubernetes' desired state, the digital twin)
carries an unexamined assumption: that the system's account of itself can be trusted.
HOLARCH imports the corpus results that examine it:

- $\varphi(\Gamma)$ — the self-model — must be **computed from the state** by a
  declared map rather than asserted alongside it (T-96 **[T under the stated
  stationary model]** gives nontrivial purity/mismatch conditions under its
  explicit baseline and diagonal-preservation hypotheses).
- Fixed-point iteration $\varphi, \varphi^{(2)}, \ldots$ **converges geometrically**
  whenever its Lipschitz constant is strictly below one on the chosen complete
  invariant domain (T-191 **[T under the stated strict contraction]**; purity alone
  does not bound the Lipschitz constant). Under the stipulated score convention of
  T-142 (**[T at specified SAD score convention]**; universal depth ceiling T-217
  is withdrawn **[✗]**), the score stops at 3 — §10 analyses the resulting
  window trade-off and architectural budget.
- **Fidelity is a number**: $R_\varphi = 1 - \lVert\Gamma - \varphi(\Gamma)\rVert^2
  / \lVert\Gamma\rVert^2$ — the fraction of the system's actual state its telemetry
  and models capture. For an agent platform this is, concretely, eval fidelity: how
  much of real behavior the eval harness sees.
- **The anti-Goodhart clause.** In the SYNARC-Ω closure the target of motion is
  driven by the attractor $\rho^*_\Omega$, **not** by the self-model φ(Γ), and the
  anti-wirehead hull result shows the design cannot gain by editing its own gauge.
  Engineering rule, stated flat: *no health metric may be computable from the
  self-report alone; every SLO must bottom out in user-facing or substrate-facing
  measurement.* A system allowed to optimize its own dashboard will, by Goodhart's
  law, become a dashboard.

## §9. Composition and certified comparisons {#композиция}

[T-77](/docs/consciousness/ethics-meaning/value-consciousness#теорема-кооперация) is the exact pinching identity

$$
P(\rho)-P(\mathcal E\rho)=\|\rho-\mathcal E\rho\|_F^2,
\qquad \mathcal E\rho=\sum_a\Pi_a\rho\Pi_a.
$$

For two blocks the right-hand side is $2\|B\|_F^2$. The comparison holds the diagonal blocks fixed. If they are $p\rho_A$ and $(1-p)\rho_B$, their pinched purity is $p^2P(\rho_A)+(1-p)^2P(\rho_B)$, not an “uncoupled sum”. The direct sum represents alternative sectors. Simultaneous seven-dimensional systems instead require a $49$-dimensional tensor state, compatible marginals and a declared correlation model.

**Laboratory witness.** HL11 constructs normalised positive $14\times14$ Gram states and checks Hermiticity, trace one, positivity, weighted block normalisation and the pinching identity. The narrow seeded run passed **240/240**, with maximum identity residual $5.551\times10^{-17}$ and minimum eigenvalue $6.398\times10^{-6}$. This checks the block identity; it is not a tensor-composition or cooperation experiment. The previous panel labelled 14D matrices “org⊗system” and checked no positivity: reproducing its seed gave **54/240** nonpositive matrices (minimum eigenvalue $-0.0162786174$).

Engineering composition therefore requires further data **[D/H]**:

- **Interfaces and outcomes.** Declare messages, resources, failure modes and the benefit criterion. Compare joint operation with an explicit independent-action baseline. An off-diagonal norm alone does not price a partnership or certify a benefit to either participant.
- **Organisation and software.** A model relating communication structure to software architecture must specify how observations determine its variables. Calling that relation a cross-block does not derive an organisational law.
- **Federation or a new aggregate.** Define responsibilities, state ownership and measurable operational requirements. A mutual-information threshold alone neither selects the architecture nor establishes a new subject.
- **Coordination.** State the consistency requirements and assumptions of the distributed model. Any claim of coordination-free execution or required consensus needs a matching theorem or protocol; T-77 supplies neither.

**Composition needs an address, and the address is not free [C].** A task benefit
requires that work reaches the right participant; this is separate from the pinching identity. Addressing is itself one of the
21 channels — **AU, Differentiation**: *distinctions that keep the whole intact,
routing without fragmentation* — so a holon that routes spends part of its own
channel budget on routing. The laboratory prices this (HL15). At 42 contexts split
across two children, each child sitting exactly at the 21-channel capacity, the
undivided holon misses 310 times; a router that **learns** its assignment from the
task's own reward misses 286; a router that **declares** the assignment once and
commits to it misses 228 — a 26% gain the learned router never reaches. The reason
is the contract rule this section already states: coordination is declared, not
hoped. A routing policy optimised against the same reward as the task it routes
never holds still long enough for a child to specialise, and every re-decision
hands a context to a sibling that has not learned it. Industry states the same fact
twice: consistent hashing exists so that keys do *not* migrate on every topology
change, and shard keys are chosen at design time rather than continuously
re-optimised.


And the rule is sharper than "declare it". A $2\times2$ factorial imposes freezing
and balance independently (HL16): a *frozen skewed* router assigns each context
once but sends most of them to one child; a *churning balanced* router picks a
child uniformly at random every visit. Against an undivided holon's 910 misses,
frozen-and-balanced gives 636, frozen-but-skewed 734, and churning-but-balanced
888 — balance without a stable address recovers essentially nothing, while
freezing alone recovers 19% and freezing with balance 30%. **Stability is the
precondition and balance the multiplier**, which is why consistent hashing fixes
the key *and* spreads it: either half alone would leave most of the gain on the
table [C].


## §10. Depth: the score ladder, the window trade-off, and the architectural budget {#глубина}

Under the stipulated attenuation score convention ([T-142](/docs/consciousness/hierarchy/depth-tower)
**[T at the specified SAD score convention]** — `scoreR0 = 7P/2`, attenuation $3^{-(k-1)}$,
cut $1/(k+1)$), the purity thresholds for score rungs $n = 1, 2, 3, 4$ evaluate algebraically to

$$
P_{\mathrm{crit}}^{(n)} = \frac{2}{7}\cdot\frac{3^{\,n-1}}{n+1}
\;:\qquad
\tfrac{1}{7},\;\; \tfrac{2}{7},\;\; \tfrac{9}{14},\;\; \tfrac{54}{35} > 1
$$

(HL02). Two critical clarifications replace earlier overclaims:

1. **Not a universal depth ceiling.** The universal depth ceiling (`T-217` **[✗]**) is
   **withdrawn**; `T-142` holds only algebraically for that stipulated score convention
   and imposes no universal prohibition on metamodels or deeper engineered hierarchies.
2. **Conflict between $P > 9/14$ and the agentic window $(2/7, 3/7]$.** Notice that the
   $n = 3$ rung requires $P > 9/14 \approx 0.643$, which **exceeds the upper edge
   $P = 3/7 \approx 0.429$ of the V1–V2 conscious/agentic window (§6)**: at
   $P > 9/14$, the lower-bound reflection satisfies $R = 1/(7P) < 2/9 \approx 0.222 < 1/3$,
   violating V2 (the "crystal/monolith" regime). Consequently, a single holon running inside
   the agentic window $P \in (2/7, 3/7]$ **cannot** simultaneously operate at $P > 9/14$
   under the lower-bound $R$ criterion.

Engineering translation:

- **Deterministic kernels vs. agentic holons.** A minimal, rigid verification core (such as
  a microkernel) may legitimately operate at high concentration $P > 3/7$ by trading away
  lower-bound reflection $R$ in favor of deterministic lock-in. Conversely, a reflective
  agentic holon stays inside the window $P \in (2/7, 3/7]$ and does **not** seek $P > 9/14$.
- **Federation as an architectural budget (`T-304` [D] + [H]).** Rather than stacking
  arbitrary nesting depth inside one holon, HOLARCH adopts **depth $\le 3$** as an
  **architectural design budget `[D]`** and delegates larger scale to a federated **ecology**
  of bounded-depth holons with declared contracts (§9). C4's practical four-zoom cap and
  VSM's bounded recursion reflect the same engineering craft.
- **External consonance [CONS].** The blockchain lineage ran a related experiment at
  ecosystem scale: L2 rollups scale L1, whereas stacked L3s do *not* compound compression
  (Buterin's argument: data "can be compressed once, but not again"), so L3's legitimate
  role is customization rather than repeating the same layer (§16). This is a structural
  rhyme, not a derivation.
- **Breadth budget and addressing cost (`T-304` [D] + [H]).** A node types at most
  21 distinct dependencies (§5), so allocating one subordinate per unordered pair gives
  21 slots; under the chosen architectural budget of depth 3, one holarchy spans at most
  $21^3 = 9261$ typed contexts (or $21 \cdot 2^2 = 84$ if each address is read only from
  a single channel sign bit). These are **architectural capacity budgets**, not universal
  composition ceilings. The laboratory separates the two regimes (HL15): the declared
  holarchy gains 26% over the undivided holon at fan-out 2 and 39% at fan-out 7 — the
  advantage *grows* with branching, matching channel-bound fan-out rather than bit-bound
  fan-out. At 84 contexts over four leaves at depth 3, the declared-routing holarchy
  misses 242 against the undivided holon's 339: reach is earned by spending one declared
  contract per child.


## §11. Diagnosability: the seven-axis instrument panel {#диагностика}

Three corpus results make a HOLARCH system *diagnosable by construction* — the
capability no framework in §18 offers at all:

1. **The alphabet is the code.** T-224 [T]: seven axes with the Fano grammar are the
   unique perfectly single-fault-localizable alphabet of their size — a failing
   aspect names itself.
2. **The wiring is testable.** T-226 [T]: fourteen parameter-free sum rules over the
   21 pairwise decoherence rates hold *iff* the wiring is Fano — a conformance test
   that an implementation's coupling structure matches its declaration, for free.
3. **Diagnosis compresses lawfully.** The Σ-pyramid 21 → 7 → 3 → 1
   ([T-225](/docs/applied/research/syndrome-calculus)) aggregates channel readings
   to line syndromes to a triad to one verdict — the escalation path of an alerting
   tree, derived.

Plus the negative result that pays for the panel: pairwise monitoring is
structure-blind (T-226 first-order blindness; HL13), so the minimal honest probes are
triads, and the Fano-coverage meter (§5) is the design-time gauge of how much of the
system the diagnosis can actually see.

## §12. The Ω-procedure: how a design agent uses this {#процедура}

The meta-specification is operational: it is written to be *executed* by a design
intelligence — human or AI — as a loop of ten steps, each with an input, an output
and a computable gate. Spec Kit's constitution→specify→plan→tasks pipeline is the
industrial ancestor; the Ω-procedure is that pipeline with mathematics inside the
gates.

| Step | Name | Output | Gate |
|------|------|--------|------|
| Ω0 | Constitution | the four invariants + status discipline ([T]/[C]/[H]/[D]/[I] on every claim) | fixed; not negotiable per-project |
| Ω1 | Specify | Γ-target: intended budget profile + tier (viable / agentic window) | target satisfies V1–V4 *on paper* |
| Ω2 | Decompose | holon tree with per-holon budgets | depth ≤ 3; every holon has all 7 aspects addressed (a zero is a decision, not an omission) |
| Ω3 | Wire | flows and typed channels (§5, §14) | Γ assembles PSD; Φ ≥ 1 reachable; Fano-coverage reported |
| Ω4 | Verify | verdict P/R/Φ/D + σ-panel + **ablation calculus** | all four invariants green; each planned failure mode breaks *only* its invariant |
| Ω5 | Views | C4/UML/SysML/ArchiMate/TLA+ projections (§13) | every view generated from the instance, none hand-drawn |
| Ω6 | Implement | tasks per holon per aspect (Spec Kit / AGENTS.md compatible) | tasks trace to channels, not to vibes |
| Ω7 | Operate | runtime Γ estimation; σ-monitoring; $\mathcal{V}_{\mathrm{hed}}$ wire | alert tree = Σ-pyramid; triad probes deployed |
| Ω8 | Regenerate | ℛ-policy: supervision, redeploy cadence, off-switch semantics | feeding ratio $x > 1+\sqrt 2$ with margin; reignition tested |
| Ω9 | Compose | Typed contracts with neighbor systems (MCP/A2A shapes) | cross-block declared; CALM class on every LU contract |

One lesson of this page's own laboratory belongs in Ω3 as a standing principle,
because it contradicts common practice. The first draft of the worked designs
declared couplings the intuitive way — a list of pairwise contract strengths. The
constructor **failed**: a dense wish-list of strong pairwise couplings is not jointly
realizable as a physical state (Γ must stay positive semidefinite), and the shrink
needed to repair it destroyed integration ($\Phi \approx 0.5$). Integration that
clears $\Phi \ge 1$ has to ride **shared flows** — system-wide coherent modes
(control / data / supply, an [I]-echo of §7's three flows) that concerns co-load.
Point-to-point integration is a wish; flow integration is a state. This is measured,
not opined (the failed constructor and the flow constructor are both in the lab), and
it retroactively explains two industry instincts: why event backbones and shared
platforms integrate where point-to-point meshes tangle, and why "integration teams"
fail where "platform teams" succeed.

## §13. Views: every notation is a projection {#виды}

HOLARCH complies with ISO/IEC/IEEE 42010 by construction — stakeholders hold
concerns; concerns are the seven aspects; viewpoints are projection recipes; views
are their outputs — with one inversion of custom: **the view is generated from the
computable instance, never drawn beside it**. Correspondence rules (the 42010 burden
notations struggle with) collapse into "both views project one Γ".

| Notation | What projects into it |
|----------|----------------------|
| C4 | the holon tree at depths 0–3 = context/containers/components/code; the depth-3 architectural budget (§10) mirrors where C4 hands off to code |
| UML class / sequence / state | S-aspect structure; D-channel interactions; SD persistence machines |
| SysML v2 / KerML | the full instance, textual and API-first — closest cousin in spirit; HOLARCH adds the invariants v2 does not have |
| ArchiMate | strata of the holarchy; its relationship taxonomy lands in the 21 channels |
| TLA+ / Alloy / Verum | L-aspect contracts: every LU/DL/LE contract of weight above threshold *must* carry a formal view — verification is a mandated projection, not a luxury |
| DSM | $\lvert\Gamma\rvert$ itself, clustered |
| Org chart / Team Topologies | a declared org/system coupling model (§9) |
| arc42 / ADR | the documentation skeleton; ADRs inherit status discipline — every decision carries [T]/[C]/[H]/[D]/[I] |

## §14. The machine-readable core {#схема}

A HOLARCH instance is a small document; the reference validator is the laboratory.
Schema `holarch.v1`, worked-design W1 abridged:

```yaml
holarch: v1
holon: mixnet-node            # FANOS/Nym class, §15
tier: agentic-window
flows: [control, data, supply]     # coherent modes; weights λ sum to 1
lambda: [0.34, 0.38, 0.28]
background: 0.40                    # ε — unstructured operational activity
participation:                      # aspect × flow co-loading (derives Γ)
  A: {control: 0.6, data: 1.5, supply: 0.4}   # ingress rides the data flow
  S: {control: 0.9, data: 1.1, supply: 0.5}   # Sphinx uniform format
  D: {control: 1.0, data: 1.5, supply: 0.8}
  L: {control: 1.5, data: 0.9, supply: 0.7}   # routing/crypto law
  E: {control: 0.6, data: 1.5, supply: 1.2}   # the hidden pool — anonymity itself
  O: {control: 0.6, data: 0.7, supply: 1.7}   # transport, stake, cover budget
  U: {control: 1.6, data: 0.5, supply: 0.8}   # epoch topology / directory
contracts:                          # Explicit interface contracts with neighbor holons
  - with: directory-authority
    channels: [DU, OU, SU]
    calm: coordinated               # epoch consensus is non-monotone
verdict:                            # computed, never hand-written
  P: 0.366  R: 0.391  Phi: 1.53  D: 2.65  window: true
```

The same structure in Verum types (the corpus's specification language), carrying the
invariants as refinement predicates:

```verum
/// A concern budget: probabilities over the 7 aspects, Σ = 1.
public type AspectBudget is {
    a: Float, s: Float, d: Float, l: Float, e: Float, o: Float, u: Float,
} where (self.a + self.s + self.d + self.l + self.e + self.o + self.u - 1.0).abs() < 1.0e-6;

/// The four-invariant verdict of an assembled design state.
public type Verdict is {
    p: Float, r: Float, phi: Float, d_diff: Float,
};

implement Verdict {
    /// The agentic window: all four thresholds, jointly (T-124b: each is
    /// independently necessary — dropping any one admits a named pathology).
    public pure fn viable_window(&self) -> Bool {
        self.p > 2.0/7.0 && self.r >= 1.0/3.0 && self.phi >= 1.0 && self.d_diff >= 2.0
    }
}

@test
fn grey_is_dead() {
    let grey = Verdict { p: 1.0/7.0, r: 1.0, phi: 0.0, d_diff: 1.857 };
    assert(!grey.viable_window());
}
```

## §15. Worked design W1: a mixnet {#воркед-mixnet}

*The question the user's request poses directly: what is the correct architecture of
a mixnet?* Run the Ω-procedure and watch the known answer fall out — that is the
test: a meta-specification earns trust when it re-derives, from its own arithmetic,
the design that a decade of anonymity research converged on.

**Ω1–Ω2.** The Γ-target puts the *anonymity itself* where no mainstream methodology
has a place for it: in **E — interiority**. A mix's product is precisely its
unobservable inside (the hidden pool, the keys, the random delays); a mixnet is an
E-machine the way a blockchain is an L-machine. Supply (O) carries transport, stake
and — critically — the **cover-traffic budget**: dummy packets are substrate spent
*inside* privacy, which is the EO channel (Immanence) read literally.

**Ω3.** Flows: data (packets: A→D→E, ingress into the hidden pool — AE Apperception
is the mixing), control (routing law and epoch topology: L, U), supply (stake,
cover). The assembled verdict (HL04, DESIGN): $P = 0.366$, $R \ge 0.391$,
$\Phi = 1.53$, $D = 2.65$ — inside the agentic window; dominant channels, read off
the state: DE Affection (forwarding reshapes the pool), EO Immanence (cover),
DL Regulation (Poisson release), AD Actualization — the load-bearing organs of the
Loopix design, *named by the state itself*.

**Ω4 numbers** (HL08, VERIFIED). Against a stratified topology with adversarial
fraction $f = 1/3$ per layer, the fully-hostile-route probability is $f^\ell$: 33.3%
at one layer, 11.1% at two, **3.7% at three**, 1.2% at four — at ~50 ms per hop.
Depth 2→3 buys 9× at +50 ms; 3→4 buys only the same 3× multiplier for another
+50 ms — and the anonymity trilemma (Das–Meiser–Mohammadi–Kate 2018 [external T])
proves the remaining gap is always paid in bandwidth (cover) or latency, never free.
The procedure therefore lands on: **at least two independent mixing layers (V4's
$D \ge 2$ heard at topology scale: one mix = one trusted party = no anonymity),
three as the knee of the curve, cover traffic as a budgeted EO line-item, and a
directory/epoch organ in U** — which is Nym/Loopix: entry gateway, three mix layers,
exit gateway, Poisson cover, epoch topology. The corpus's own
[FANOS](/docs/applied/fanos/fanos-specification) is this class rebuilt on PG(2,q)
with the diagnosability panel switched on; HOLARCH is the meta-level FANOS
instantiates.

**Ω4 ablations.** Smear the flows → V1 mud; single global pattern → V2; flows retreat
to islands → V3; unplug E → V4 — the four failure modes of real anonymity networks
(traffic smearing without structure, single-operator consolidation, partitioned
directories, and *loss of the hidden pool itself*), each caught by exactly one gauge.

## §16. Worked design W2: a blockchain {#воркед-блокчейн}

**Ω1–Ω3.** A public blockchain is an **L-machine**: its product is enforced
consistency (LU: finality) among strangers, priced in substrate (LO: proof-of-stake —
the Grounding channel taken literally: logic that costs ground). The aspect layout of
the modular stack: A mempool ingress; S ledger schema and state commitments;
D execution; L consensus law (the dominant voice, by design); E node-local state
(thin — the ledger is public); O stake, p2p, **data availability** (OU Completeness:
the whole must be *fed* its own data — the DA layer is this channel's name spelled
out); U the one canonical head (fork-choice as DU Teleology). Verdict (HL05, DESIGN):
$P = 0.360$, $R \ge 0.397$, $\Phi = 1.49$, $D = 2.06$ — viable, with the honest
signature of the breed: **D barely clears 2**. Transparent-by-design systems run
structurally thin interiority; below the modeled node-local allocation, $D_{\mathrm{diff}}$
dips under 2 — the meta-spec's way of saying that a chain with *no* private
node-state margin has one regime and no floor to degrade onto.

**External numbers [CONS].** The anti-dominance family (§6) at ecosystem scale,
2026 execution-layer client shares: Geth ≈ 50%, Nethermind 25%, Besu 10%, Reth 8%,
Erigon 7% (HL14) — the leader sits *above* the community's 1/3 danger line and below
the 2/3 finality-killing line, which is exactly how the ecosystem itself talks about
it. BFT's $f < n/3$ and the R-ceiling are the same *shape* of law on different bases
(HL09 states both sides precisely; [I], not an identity). And the depth-budget heuristic
finds an external consonance here: L2 scales L1; stacked L3s do not compound compression —
a structural rhyme with §10's bounded-depth federation rule (CONS).

**Ω8.** The feeding law lands bluntly on this breed: issuance+fees fund the
regeneration flow; a chain whose maintenance-to-entropy ratio slips under the silver
floor (§7) is dissolving regardless of its narrative — the meta-spec turns "crypto
winter kills chains" into a gauge.

## §17. Worked design W3: an AI-agent platform {#воркед-агент}

**Ω1–Ω3.** The 2026 production canon (orchestrator–workers, planner, critic, memory
tiers, evals, MCP tools, A2A peering) lays out on the aspects with no remainder:
A perception/ingress; S tool and message schemas (MCP is an SL/AS artifact);
D tool execution; L planner, guardrails and eval law; **E memory tiers and context —
the load-bearing aspect of the breed** (AE Apperception *is* context engineering);
O models, compute, quotas; U the orchestrator. Verdict (HL06, DESIGN): $P = 0.373$,
$R \ge 0.383$, $\Phi = 1.59$, $D = 2.59$ — in the window; dominant channels DE
(acts write experience), DU (orchestrator reconciles to goal), DL (planner loop),
EO (context budget felt inside — the token-budget backpressure every agent developer
now knows by hand).

**What the invariants add over the pattern canon.** The canon says "add a critic";
V2+§8 say *what the critic is*: the reflection budget, with a fidelity number
$R_\varphi$ (eval coverage of real behavior) and an anti-Goodhart clause — the agent
must not grade its own homework with a gauge it can write to. The canon says "add
memory"; V4 says memory is the *differentiation organ*: unplug E and the ablation
lands exactly on rigidity — an agent with no interior state has one regime, which is
the observed brittleness of stateless prompt-chains. The canon says "orchestrate";
§10 adopts an architectural depth-3 budget (`T-304` [D]+[H]): orchestrator→worker→tool
caps a single hierarchy and delegates further nesting to federation (A2A), mirroring the
industry's multi-agent turn. The corpus's SYNARC-Ω is the full-strength
realization of this breed (the AGI-grade instance with all theorems switched on);
the [Prime Radiant's case №1](./prime-radiant.md#кейсы) runs its σ-panel as
interoception.

## §18. Comparative mapping against established frameworks {#матрица}

This section maps 44 architectural concerns across established notations, methods,
runtimes, and reference systems onto HOLARCH's vocabulary, making explicit what HOLARCH
models natively and what remains external. **Native modeling construct** (N): HOLARCH's
own state-matrix specification provides a first-class architectural representation for
that concern. **Embedded / External** (E): the established notation, formal verifier,
execution runtime, or reference system is **retained as an external artifact or platform**
— HOLARCH classifies where it sits in the design and does **not** replace its runtime,
consensus protocol, or formal proofs. **Gap** (G): ecosystem capability not yet built.
The laboratory verifies that every row is non-empty and every section anchor resolves
(HL07).

| Framework → capability | Mode | HOLARCH comparative mapping |
|---|---|---|
| **UML 2.5.1** — diagram vocabulary; MOF interchange; tooling ecosystem | E·E·**G** | view emission from S/D/L projections (§13); `holarch.v1` as interchange (§14); *gap: native tooling* (§19) |
| **SysML v2/KerML** — textual git-native models, API; traceability | N·N | text-first instance + lab-as-API (§14); Γ-target→budget→channel trace (§12) |
| **C4** — zoom levels; maps-not-models pragmatism | N·E | bounded-depth federation budget (§10); views stay maps, the model computes behind them (§13) |
| **ArchiMate 3.2** — EA layers; relationship taxonomy | E·E | holarchy strata; relations map onto 21 channels (§5, §13) |
| **ISO 42010** — stakeholder/concern/viewpoint discipline | N | fixed concern alphabet + generated views + single-source correspondences (§13) |
| **arc42 / ADR** — documentation skeleton; decision log | E·N | emitted from instance (§12 Ω5); ADR + status discipline [T]/[C]/[H]/[D]/[I] (§13) |
| **TOGAF ADM / Zachman** — process cycle; interrogative coverage | E·E | Ω0–Ω9 with computable gates (§12); interrogatives = aspect×view queries (§13) |
| **AADL** — analyzable embedded semantics | E | O/L channel contracts carry analysis annexes; AADL retained as mandated view (§5) |
| **TLA+/Alloy** — formal behavior verification | E | mandatory external formal view on heavy L-contracts (§13) |
| **DDD** — bounded contexts; context-mapping patterns | N·N | holon boundary = E-interiority (§3); typed interface models; T-77 has only the block-identity scope (§9) |
| **Hexagonal/Clean** — dependency rule, ports/adapters | N | A-ports, O-adapters, protected L/S/E core; the rule is channel direction (§4) |
| **Parnas 1972** — information hiding as criterion | N | E is an *axis with a measure* (Coh_E), not advice (§4) |
| **Simon 1962** — near-decomposability | N | sparse-but-nonzero cross-blocks, quantified by the Φ cut (§6) |
| **Alexander** — pattern language; semilattice not tree | N | Fano incidence: overlapping lines over 7 aspects — a semilattice by theorem (§11) |
| **DSM** — dependency matrix + clustering | N | Γ *is* the matrix — typed, PSD, dynamic, thresholded (§3) |
| **VSM** — viability criterion; recursion; algedonic channel | N·N·N | four invariants ([D] cuts; independence/robustness [T], §6); bounded-depth federation (§10); purity-flux scalar (§7) |
| **MAPE-K** — autonomic loop over knowledge | N | φ(Γ) + three-flow model, with conditional contraction/feeding bounds (§8, §7) |
| **Erlang/OTP / Kubernetes** — supervision; desired-state reconciliation | E·E | *specification-level mapping only*: conceptual correspondence to $\mathcal{R}$ replacement flow and `DU` channel (§5, §7); **production supervision, scheduling, and cluster reconciliation remain in Erlang/OTP and Kubernetes** |
| **Reactive Manifesto** — responsive/resilient/elastic/message-driven | N | threshold cuts + ℛ policy + O-budget elasticity + A/D channel style (§6, §7) |
| **12-Factor** — operational hygiene | E | each factor lands in an aspect checklist at Ω2 (§12) |
| **CALM** — coordination boundary | E | mandatory monotone/coordinated field on LU contracts (§9) |
| **Conway / Team Topologies** — org↔system mirror; interaction modes | N·N | declared org–system coupling model (§9) |
| **ATAM** — scenario-based tradeoff analysis | N | ablation calculus: scenario = ablation, sensitivity = ∂verdict (§12 Ω4) |
| **Spec Kit SDD** — constitution→specify→plan→tasks | N | Ω0–Ω9 with computable checks inside the gates (§12) |
| **AGENTS.md** — machine context for repos | N | the `holarch.v1` instance serves as a design-level machine context (§14) |
| **MCP / A2A** — tool contracts; agent peering | E·E | mapped to SL/AS contract channels (§5) and declared peering (§9); **actual wire protocols remain MCP and A2A** |
| **Anthropic agent patterns** — workflows-vs-agents; evaluator-optimizer | N | DL regulation loop + LE evidence critic + R_φ fidelity (§17, §8) |
| **LangGraph/AutoGen/CrewAI** — orchestration graphs | E | U-organ emitted as graph views; runtime execution stays in the orchestration framework (§13) |
| **Nym/Loopix · Ethereum-modular · seL4** — reference architectures | E·E·E | *architectural profiling only*: W1 (§15) and W2 (§16) profile Loopix and modular-blockchain designs in `holarch.v1`; **seL4's machine-checked Isabelle/HOL kernel proof is an external formal-verification artifact mapped to `LO` (§5) — HOLARCH classifies it and never derives or replaces it** |

Reading the table honestly in both directions: at the **architectural modeling layer**,
HOLARCH adds a common state-matrix grammar (fixed 7-aspect alphabet, 21 typed channels,
four computable cuts, ablation checks, and Fano triad diagnostics) across notations that
otherwise do not compose. Conversely, HOLARCH does **not** subsume or replace execution
runtimes (Kubernetes, Erlang/OTP), formally verified kernels (seL4), formal model
checkers (TLA+/Alloy), wire protocols (MCP/A2A), or mature diagramming toolchains (§19).

## §19. Critical analysis: boundaries, falsifiers, and honest gaps {#границы}

A meta-specification claiming perfection would refute itself; this section is the
spec attacking its own weakest planks, in descending order of load.

**Honest scope and gaps: tooling, runtimes, and domain proofs.** UML and SysML have
decades of editors, generators, and trained practitioners; Kubernetes and Erlang/OTP
provide battle-tested distributed execution; seL4 provides a machine-checked C/binary
proof of kernel isolation in Isabelle/HOL. HOLARCH is strictly a **design-level
meta-specification** backed by a ~700-line reference validator — it complements those
systems rather than competing with them, and its own tooling ecosystem remains an open
gap (**G** in §18) that closes only with independent adoption.

**Aspect assignment is judgment.** Whether a given artifact is S-work or L-work is a
modeling decision. The dictionary (§4–§5) is structured enough to make assignments
*arguable* — but inter-rater reliability is unmeasured. **OPEN protocol:** two
architects independently profile the same three systems; agreement below
Cohen's κ ≈ 0.6 on aspect budgets would demote the dictionary from "operational"
to "suggestive", and that result would be published in this page's status table.

**Threshold transfer is calibration, not derivation.** Inside Γ-mathematics the
thresholds are theorems. That a *software system's* concern budgets, assembled by the
§14 constructor, deserve those exact thresholds is an [D]-choice validated so far by
coherence of consequences (the ablation pathologies land on recognizable industry
failure modes) — not by field data. The DESIGN class exists precisely to keep this
distinction loud.

**Consonances are rhymes.** BFT's 1/3, client-diversity's 1/3–2/3, Buterin's
non-stacking L3s are *external* laws that share shape with internal theorems. The
laboratory states each pair precisely and tags them CONS/[I]. None is presented as a
derivation, and the page contains no OSI-style numerology (§4 explicitly declines
the one everyone expects).

**The constructor has conventions.** The flow-mode assembly (rank-3 + background ε)
is one honest way to realize declared budgets as a PSD state; ε ≈ 0.4 encodes "no
real system is pure structure". Other constructors are possible; the invariants and
thresholds do not depend on the choice, but specific instance numbers do.

**Falsifiers, stated as targets:**
1. exhibit a real architectural dependency that no aspect pair can type (§5 breaks);
2. exhibit a demonstrably viable system that violates the full invariant conjunction
   under any faithful Γ-assembly (§6 breaks);
3. run the OPEN inter-rater protocol to κ < 0.6 (§4 demotes);
4. run a blind design trial — two teams, one brief, one team using Ω0–Ω9 — with no
   measurable quality delta (the procedure demotes to documentation).

**What HOLARCH does not claim.** It does not claim software systems are conscious
(the window is a structural tier, not an experience claim); it does not replace
domain knowledge (the dictionary types decisions, it does not make them); it does
not generate code; and it does not claim the three worked designs are evidence about
Nym, Ethereum or any real deployment — they are demonstrations that the calculus
*re-derives known-good shapes*, which is necessary, not sufficient.

## §20. Status summary {#статусы}

| Claim | Class / status | Witness |
|-------|---------------|---------|
| Seven-aspect alphabet is uniquely diagnosable at its size | [T] import | T-224; HL01 |
| 21 channels; SSOT names carry engineering readings unmodified | [D]+[I] | HL01; §5 |
| Four invariants: threshold cuts [D]; independence, robustness, $\Phi\ge1\Rightarrow P\ge2/7$ [T] | [D] + [T] import | T-124, T-124b/d, T-129, T-129a, T-151; HL03 |
| Three-flow grouping [D]; dephasing spectral/Onsager identity (diagonal kernel, not $G_2$-covariant); model-conditional feeding/decay | [D] + [T at specified model] | T-262, T-259, T-288/289, T-103; HL12 |
| Self-model contraction, model-conditional mismatch, anti-Goodhart | [T under stated hypotheses] + [D] rule | T-96, T-191, T-222; §8 |
| Two-block pinching identity; no operational gain theorem | [T] identity; finite numerical check | T-77; HL11 (240/240 PSD, trace-one states) |
| Score-convention depth ladder ($P > 9/14$ exits V2 window) and architectural depth-3 budget | [T at specified score convention] + [D]/[H] | T-142, T-304; HL02 (universal T-217 withdrawn [✗]) |
| Pairwise monitoring is structure-blind; probe triads | [T] import | T-226; HL13 |
| Three worked designs land in the window; ablations break their own invariant | DESIGN | HL04–HL06 |
| Mixnet arithmetic: f^ℓ, trilemma, knee at 3 | VERIFIED + external [T] | HL08 |
| BFT-1/3 and client-diversity rhymes | CONS [I] | HL09, HL14 |
| Comparative mapping: 44 capabilities (23 N / 20 E / 1 G); no runtime/kernel replacement | VERIFIED (anchor audit) | HL07; §18–§19 |
| Integration rides shared flows, not pairwise links | VERIFIED (constructor) | §12; lab history |
| Inter-rater reliability of aspect assignment | **OPEN** | §19 protocol |
| Blind design-trial utility | **OPEN** | §19 protocol |

## §21. The laboratory {#лаборатория}

Panels HL01–HL15, all PASS at the time of writing:
SSOT synchronization (HL01), the depth ladder (HL02), Γ-calculator reference points
(HL03), the three worked designs with four-way ablations (HL04–HL06), comparative-mapping
completeness with anchor resolution against this very page (HL07), mixnet arithmetic
(HL08), the two consonance blocks (HL09, HL14), the Fano-coverage meter (HL10), the
T-77 identity (HL11), the feeding fold (HL12), first-order blindness (HL13), the price of addressing (HL15). One
command, no arguments, exit code is the verdict:

```bash
python3 architecture/holarch_lab.py
```

The panel is the release gate of this specification: any future edit that breaks a
row must either fix itself or change the page honestly.
