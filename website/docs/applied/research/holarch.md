---
sidebar_position: 18
title: HOLARCH
description: "The holonic meta-specification of digital architecture: seven concerns, 21 typed channels, four computable viability invariants, three-flow dynamics, a composition algebra and a depth ceiling — validated against UML, C4, SysML v2, DDD, VSM, MAPE-K and the 2024–2026 agentic stack"
---

# HOLARCH: the holonic meta-specification of digital architecture

**Status frame.** This page is an engineering meta-specification, not a set of new
theorems. Every claim carries one of four honesty classes: **VERIFIED** — a computed
fact about the machinery (theorem arithmetic, identity checks, coverage completeness;
reproduced by the laboratory `architecture/holarch_lab.py`, panel HL01–HL14, 14/14);
**DESIGN** — self-consistency of an engineering instance (true by construction,
demonstrated, *not* evidence about external systems); **CONS** — a numerical consonance
with an external published number (a structural rhyme stated precisely, never an
identity claim); **OPEN** — needs field data, with the protocol stated. Imported UHM
mathematics keeps its registry statuses [Т]/[С]/[Г]/[О]/[И]. The projection from
Γ-mathematics onto software engineering is itself an [О]-definition plus an
[И]-dictionary — structured, configurable, testable; never a fact.

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

HOLARCH is that meta-specification, stated once and validated. The delivery criterion
is taken from the request that produced it, at full strength: **no speculation**, and
**not inferior to any established solution in any point**. The second half is not
rhetoric; it is a machine-checked table. §18 lays out 41 load-bearing capabilities of
the strongest existing frameworks — from UML 2.5.1 to SysML v2 (2025), C4, ArchiMate,
ISO 42010, DDD, VSM, MAPE-K, Erlang/OTP, Kubernetes, TLA+, Spec Kit, AGENTS.md, MCP and
A2A — and for each one names the HOLARCH mechanism that carries it, **native** in 28
cases, **embedded** (the framework is kept, as a mandated view or procedure step) in 12,
with exactly **one honest gap** (§19). The laboratory re-checks that the table has no
empty cells and that every named mechanism resolves to a section of this page (HL07).

What HOLARCH is *not*: it is not a notation (it emits notations), not a process (it
contains one as a component), not a pattern catalog (patterns become typed channel
configurations). It is the semantic layer the sixty-year lineage kept circling without
landing on: a **fixed, theorem-forced alphabet of concerns; a complete typed taxonomy
of couplings; computable viability invariants with proven thresholds; dynamics,
self-model, composition and depth as first-class citizens**. Existing languages become
projections of one computable object — the way the same building casts a floor plan,
a wiring diagram and an elevation.

## §2. The landscape: what sixty years actually taught {#ландшафт}

Before building, the strongest available test of *need* is comparative: lay out the
mature lineage and see what each branch got permanently right and where every branch
stopped. The reading of each row is [И] over published, uncontested history.

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

1. a **fixed alphabet of concerns** with a uniqueness theorem (not "however many
   layers we drew this year") — supplied by N=7 diagnosability rigidity, T-224 [Т];
2. a **complete typed taxonomy of couplings** — supplied by the 21 coherences of Γ;
3. **numeric viability invariants** with proven thresholds — P, R, Φ, D [Т];
4. **dynamics as first-class** — the three-flow decomposition of ℒ_Ω, T-262 [Т];
5. a **self-model with an anti-Goodhart theorem** — φ(Γ), T-96/T-191 [Т] + MRQT;
6. a **composition algebra with a measurable gain** — T-77 [Т];
7. a **depth ceiling with a federation rule** — T-142 [Т/С].

The rest of this page states the meta-specification (§3–§14), runs it through three
worked designs (§15–§17), proves the subsumption table (§18), and attacks it (§19).

## §3. The signature of an architectural holon {#холон}

**[О] Definition.** An architectural holon is a five-tuple

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
[holarchic ladder](/docs/applied/research/gamma-canon#холархия) restricted to
engineered systems.

## §4. The seven aspects {#аспекты}

The seven concerns are the seven dimensions of Γ, with their canonical corpus names
(the [SSOT](/docs/core/dynamics/coherence-matrix) `src/data/coherences.ts`; the
laboratory check HL01 keeps this table drift-free), each given its engineering
reading. The reading is an [И]-dictionary: structured and testable, never a fact.

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
([T-224](/docs/applied/research/syndrome-calculus#t-224) [Т]) proves that perfect
single-fault localizability with a nontrivial state grammar forces $n \ge 7$ axes, and
at $n = 7$ the grammar is *unique up to relabeling* (Hamming (7,4) = the Fano plane);
at every larger admissible size uniqueness fails. Seven concerns with Fano wiring is
the one alphabet where a single failing aspect is *localizable by design*. OSI's seven
layers, Zachman's six interrogatives, C4's four zooms are conventions; this is the
only such number carrying a rigidity theorem — which is also why HOLARCH does not
treat OSI as a cousin: OSI is a linear encapsulation ladder (a depth structure, §10),
not an aspect decomposition, and pretending otherwise would be numerology.

**Every aspect carries a stress gauge.** The σ-panel
([T-92](/docs/reference/status-registry) [Т], with the v1 errata rows) gives each
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
strongest [И]-evidence on the page.

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

**Completeness [О].** The classic coupling taxonomies embed: structured design's
content/common/control/stamp/data coupling, ArchiMate's relationship set, UML
dependency kinds — each instance lands in a typed cell (matrix rows in §18; checked
non-empty by HL07). The claim "here is a dependency no pair of aspects can type" is
one of the explicit falsifiers in §19.

**Pairs are probes' floor, not their ceiling.** The seven Fano lines
({A,S,L}, {A,D,E}, {A,O,U}, {S,D,O}, {S,E,U}, {D,L,U}, {L,E,O}) are the minimal honest
*diagnostic* units: the corpus proves first-order blindness
([T-226](/docs/applied/research/fano-fingerprint#t-226) [Т]) — the equal-weight sum of
line-adjacency matrices is exactly $J - I$, so **any equal-weight pairwise statistic
sees no structure at all**. The laboratory re-derives the identity (HL13). The
engineering consequence is immediate and non-obvious: a monitoring mesh of pairwise
heartbeats is provably structure-blind; observability must probe **triads** (this is
the FANOS "diagnosis on triples" imported upward). HOLARCH therefore ships a
**Fano-coverage meter**: the count (0–7) of lines all three of whose edges carry
above-median coupling. The three worked designs of this page score 3, 2, 2 —
nontrivial, *not* saturated, and reported as a deficit gauge, not a rubber stamp
(HL10).

## §6. The four viability invariants {#инварианты}

Everything in this section is imported theorem arithmetic; the engineering layer only
chooses what to feed it. For a design, Γ is assembled from declared budgets and flows
(§12, §14); at runtime, from measurement. Four numbers then decide, with thresholds
that are proved, not tuned ([viability](/docs/core/dynamics/viability),
[T-124b](/docs/proofs/consciousness/conscious-window#t-124b)):

| Invariant | Formula | Threshold | Guards against — the named pathology |
|-----------|---------|-----------|--------------------------------------|
| V1 Distinguishability | $P = \mathrm{Tr}(\Gamma^2)$ | $P > 2/7$ [Т] | **mud**: the big ball — activity smeared until the system is statistically indistinguishable from noise |
| V2 Reflection | $R \ge 1/3$ [Т]; lower-bound form $R = 1/(7P)$ ⇔ $P \le 3/7$ | $R \ge 1/3$ | **crystal/monolith**: one global pattern eats the system; nothing is left to observe it |
| V3 Integration | $\Phi = \sum_{i \ne j}\lvert\gamma_{ij}\rvert^2 / \sum_i \gamma_{ii}^2$ | $\Phi \ge 1$ [Т] (T-129) | **fragmentation**: parts without binding — the microservice archipelago with no real contracts |
| V4 Differentiation | $D_{\mathrm{diff}} = 1 + 6\,\mathrm{Coh}_E$ | $D \ge 2$ [Т] (T-151) | **rigidity**: a single-mode system — no degraded mode, no second regime to fall back to |

Four properties make this table an instrument rather than a metaphor.

**Independence.** T-124b [Т] exhibits four constructive counterexamples: drop any one
threshold and a specific pathological state slips through. The four sicknesses above
are those counterexamples wearing engineering names. The laboratory demonstrates the
same pattern *constructively* on every worked design: four targeted ablations — smear
into background, collapse into one mode, cut the shared flows, unplug interiority —
each break **exactly their own invariant** (HL04–HL06, DESIGN).

**Robustness.** T-124d [Т]: all four measures respond $O(\varepsilon)$ to
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
**CONS/[И]** — same fraction, different bases (validator weight vs purity); a
structural consonance, not an identity (HL09, HL14).

## §7. Dynamics: the three flows {#динамика}

An architecture that only describes standing structure describes a corpse. The corpus
proves the evolution law decomposes *exactly* into three geometric flows
([T-262](/docs/core/dynamics/evolution#теорема-динамическая-трихотомия) [Т]+[С]):

1. **Work — the unitary flow**: transformations that preserve every spectral
   functional. Engineering: the reversible moves — refactorings that provably keep
   behavior, blue-green switchovers, live migrations. What characterizes them: they
   cost energy, never structure.
2. **Heat — the dissipative flow**: gradient descent of negentropy at rate γ; the
   system relaxing toward grey. Engineering: bitrot, dependency drift, config
   entropy, knowledge evaporation. This flow is *never zero*; pretending otherwise
   is how systems die politely.
3. **Matter — the regenerative flow** ℛ: replacement toward the target $\rho^*$
   through the self-model. Engineering: supervision restarts, immutable-infra
   redeploys, crash-only recovery — repair by **replacement**, not surgery
   (Erlang/OTP and Kubernetes each industrialized one half of this flow).

Three imported results give the flows teeth:

- **No supply, no being.** An isolated holon provably dies: with regeneration
  anchored to the grey state, purity is non-increasing and $P \to 1/7$
  ([T-288](/docs/reference/status-registry) [Т]). Viability is a *driven* phenomenon
  with an ignition threshold in drive-to-dissipation ratio, numerically
  $(r/\gamma)_c \approx 7$ for reference dissipation (T-289 [Т]/[С]). An
  architecture document that does not state its supply loop has not stated the
  system.
- **The silver floor.** In the stationary feeding model (T-259 [Т в модели]), the
  maintenance-to-decay ratio $x = \kappa_{\mathrm{eff}}/\Gamma_2$ must exceed
  $1 + \sqrt{2} \approx 2.414$ for the state to hold above the $2/7$ floor — the
  laboratory reproduces the fold: $x = 0.9\,x_{\min}$ starves ($P_\infty = 0.277 <
  2/7$), $x_{\min}$ lands exactly on the floor, $1.3\,x_{\min}$ lives
  ($P_\infty = 0.307$) (HL12). Engineering translation, deliberately blunt: **a
  system whose regeneration tempo is not ≈2.4× its entropy tempo is dissolving,
  whatever the roadmap says.**
- **Halt and reignition.** The off-switch is a physics-level statement: cut the
  drive and the system settles to grey in $t_{\mathrm{off}} \approx 0.49/\gamma$,
  with **hysteresis-free reignition** (T-288) — which is the crash-only design rule
  (recovery = the one and only start path) derived rather than preached.
- **The algedonic wire.** $\mathcal{V}_{\mathrm{hed}} = dP/d\tau$ (T-103 [Т]+[И]) —
  the signed tempo of organization — is VSM's algedonic channel with a formula: one
  scalar that bypasses dashboards and says *getting better / getting worse*.

## §8. The self-model and the anti-Goodhart clause {#самомодель}

Every wave-3 loop (MAPE-K's Knowledge, Kubernetes' desired state, the digital twin)
carries an unexamined assumption: that the system's account of itself can be trusted.
HOLARCH imports the corpus results that examine it:

- $\varphi(\Gamma)$ — the self-model — is a **functor** (T-96 [Т]): it must be
  computed *from the state* by a lawful map, not asserted alongside it.
- The self-model tower $\varphi, \varphi^{(2)}, \ldots$ **converges** (T-191 [Т])
  and terminates at depth 3 (T-142) — reflection on reflection has a floor and a
  ceiling; §10 prices it.
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

## §9. Composition: the gain lives in the contract {#композиция}

The composition law is the corpus's cooperation theorem
([T-77](/docs/consciousness/ethics-meaning/value-consciousness#теорема-кооперация)
[Т]):

$$
P(\rho^{(12)}_*) \;=\; P(\rho_{\mathrm{diag}}) \;+\; 2\,\lVert\gamma_{\mathrm{cross}}\rVert_F^2
$$

The purity of a composed pair exceeds the uncoupled sum by exactly twice the squared
Frobenius norm of the **cross-coherence block** — the integration gain lives *in the
contract*, not inside either participant. The laboratory verifies the identity to
machine precision on 240/240 random pairs (HL11). Consequences, each of which the
lineage held as folklore and now holds as arithmetic:

- **Integration is worth exactly what the contract carries.** A partnership with a
  thin interface gains ~nothing regardless of the partners' quality; deepening the
  cross-block is the *only* lever. DDD's context-mapping patterns (partnership,
  shared kernel, customer–supplier, anticorruption layer, …) become settings of
  $\gamma_{\mathrm{cross}}$ — including the honest zero of *separate ways*.
- **Conway's law is a synastry statement.** The org chart and the system are two
  holons; the mirroring of communication structure into architecture is their
  cross-block. Team Topologies' three interaction modes are cross-block regimes.
  You do not fight Conway's law; you *type* it and budget it.
- **Meta-holon or federation.** Composition with mutual information above the
  integration threshold founds a new whole (a platform); below it, stay federated
  peers ([holon composition](/docs/core/structure/holon#таксономия-по-уровням-организации)).
  A2A peering contracts and MCP tool contracts are the two industrial shapes of the
  cross-block, arriving fifteen years after the theorem's first form.
- **Coordination is declared, not hoped.** Every LU-consistency contract must
  declare its CALM class — monotone (coordination-free) or non-monotone (pays a
  consensus round). This imports the CALM theorem as a mandatory contract field.

## §10. Depth: the ladder and the ceiling {#глубина}

The Depth Tower ([T-142](/docs/consciousness/hierarchy/depth-tower) [Т at
α = 2/3] + [С at the ladder formula]) prices reflection levels: sustaining
self-model depth $n$ requires purity above

$$
P_{\mathrm{crit}}^{(n)} = \frac{2}{7}\cdot\frac{3^{\,n-1}}{n+1}
\;:\qquad
\tfrac{1}{7},\;\; \tfrac{2}{7},\;\; \tfrac{9}{14},\;\; \tfrac{54}{35} > 1
$$

(HL02). The fourth rung demands purity beyond the physical maximum — **depth 3 is a
ceiling**, resting on three independent arguments (dynamical, categorical, algebraic)
in the corpus. Engineering translation:

- **Mandate concentration climbs the ladder.** A depth-2 governor must run at
  $P > 2/7$; a depth-3 governor at $P > 9/14 \approx 0.64$ — more than twice as
  concentrated. Deep control layers must be *small and pure*: the microkernel
  instinct (a minimal, verified core under a broad userland) is this rung
  arithmetic felt by hand.
- **Above three: federate.** There is no depth-4 governor; there is an **ecology**
  of depth-≤3 systems with contracts (§9). C4's practical stop at four zooms and
  VSM's recursion (same shape at every level, never a taller tower per subject) both
  encode the ceiling as craft.
- **External consonance [CONS].** The blockchain lineage ran the experiment at
  ecosystem scale: L2 rollups scale L1; stacked L3s do *not* compound scaling —
  Buterin's argument is that data "can be compressed once, but not again", so L3's
  legitimate role is customization, not another turn of the same crank. An
  independent discipline discovering "the same trick does not stack a third time"
  is exactly what a real ceiling looks like from outside (§16).

## §11. Diagnosability: the seven-axis instrument panel {#диагностика}

Three corpus results make a HOLARCH system *diagnosable by construction* — the
capability no framework in §18 offers at all:

1. **The alphabet is the code.** T-224 [Т]: seven axes with the Fano grammar are the
   unique perfectly single-fault-localizable alphabet of their size — a failing
   aspect names itself.
2. **The wiring is testable.** T-226 [Т]: fourteen parameter-free sum rules over the
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
| Ω0 | Constitution | the four invariants + status discipline ([Т]/[С]/[Г]/[О]/[И] on every claim) | fixed; not negotiable per-project |
| Ω1 | Specify | Γ-target: intended budget profile + tier (viable / agentic window) | target satisfies V1–V4 *on paper* |
| Ω2 | Decompose | holon tree with per-holon budgets | depth ≤ 3; every holon has all 7 aspects addressed (a zero is a decision, not an omission) |
| Ω3 | Wire | flows and typed channels (§5, §14) | Γ assembles PSD; Φ ≥ 1 reachable; Fano-coverage reported |
| Ω4 | Verify | verdict P/R/Φ/D + σ-panel + **ablation calculus** | all four invariants green; each planned failure mode breaks *only* its invariant |
| Ω5 | Views | C4/UML/SysML/ArchiMate/TLA+ projections (§13) | every view generated from the instance, none hand-drawn |
| Ω6 | Implement | tasks per holon per aspect (Spec Kit / AGENTS.md compatible) | tasks trace to channels, not to vibes |
| Ω7 | Operate | runtime Γ estimation; σ-monitoring; $\mathcal{V}_{\mathrm{hed}}$ wire | alert tree = Σ-pyramid; triad probes deployed |
| Ω8 | Regenerate | ℛ-policy: supervision, redeploy cadence, off-switch semantics | feeding ratio $x > 1+\sqrt 2$ with margin; reignition tested |
| Ω9 | Compose | T-77 contracts with neighbor systems (MCP/A2A shapes) | cross-block declared; CALM class on every LU contract |

One lesson of this page's own laboratory belongs in Ω3 as a standing principle,
because it contradicts common practice. The first draft of the worked designs
declared couplings the intuitive way — a list of pairwise contract strengths. The
constructor **failed**: a dense wish-list of strong pairwise couplings is not jointly
realizable as a physical state (Γ must stay positive semidefinite), and the shrink
needed to repair it destroyed integration ($\Phi \approx 0.5$). Integration that
clears $\Phi \ge 1$ has to ride **shared flows** — system-wide coherent modes
(control / data / supply, an [И]-echo of §7's three flows) that concerns co-load.
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
| C4 | the holon tree at depths 0–3 = context/containers/components/code; the ceiling theorem explains why the fourth zoom is where maps hand off to code |
| UML class / sequence / state | S-aspect structure; D-channel interactions; SD persistence machines |
| SysML v2 / KerML | the full instance, textual and API-first — closest cousin in spirit; HOLARCH adds the invariants v2 does not have |
| ArchiMate | strata of the holarchy; its relationship taxonomy lands in the 21 channels |
| TLA+ / Alloy / Verum | L-aspect contracts: every LU/DL/LE contract of weight above threshold *must* carry a formal view — verification is a mandated projection, not a luxury |
| DSM | $\lvert\Gamma\rvert$ itself, clustered |
| Org chart / Team Topologies | the org-holon and its T-77 cross-block onto the system (§9) |
| arc42 / ADR | the documentation skeleton; ADRs inherit status discipline — every decision carries [Т]/[С]/[Г]/[О]/[И] |

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
contracts:                          # T-77 cross-blocks to neighbor holons
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
+50 ms — and the anonymity trilemma (Das–Meiser–Mohammadi–Kate 2018 [external Т])
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
(HL09 states both sides precisely; [И], not an identity). And the depth ceiling ran
its own experiment here: L2 scales L1; stacked L3s do not compound (compression does
not stack) — the ecosystem discovered §10's ceiling from outside (CONS).

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
§10 prices the depth: orchestrator→worker→tool is depth 3, and a fourth reflective
tier has no budget — federate instead (A2A), which is what the industry's
multi-agent turn did empirically. The corpus's SYNARC-Ω is the full-strength
realization of this breed (the AGI-grade instance with all theorems switched on);
the [Prime Radiant's case №1](./prime-radiant.md#кейсы) runs its σ-panel as
interoception.

## §18. The subsumption matrix {#матрица}

The delivery criterion, mechanically. 41 load-bearing capabilities across the
strongest frameworks; each row names the HOLARCH mechanism and its section. **Native**
(N): the capability is carried by HOLARCH's own machinery. **Embedded** (E): the
framework itself is retained — as a mandated view, procedure stage or contract field —
so its capability (and its tooling) is inherited rather than reinvented. The
laboratory verifies no row is empty and every mechanism anchor resolves (HL07:
28 N / 12 E / 1 honest gap, listed in §19).

| Framework → capability | Mode | HOLARCH mechanism |
|---|---|---|
| **UML 2.5.1** — diagram vocabulary; MOF interchange; tooling ecosystem | E·E·**G** | view emission from S/D/L projections (§13); `holarch.v1` as interchange (§14); *gap: native tooling* (§19) |
| **SysML v2/KerML** — textual git-native models, API; traceability | N·N | text-first instance + lab-as-API (§14); Γ-target→budget→channel trace (§12) |
| **C4** — zoom levels; maps-not-models pragmatism | N·E | depth tower with a ceiling theorem (§10); views stay maps, the model computes behind them (§13) |
| **ArchiMate 3.2** — EA layers; relationship taxonomy | E·E | holarchy strata; relations land in 21 channels (§5, §13) |
| **ISO 42010** — stakeholder/concern/viewpoint discipline | N | fixed concern alphabet + generated views + trivialized correspondences (§13) |
| **arc42 / ADR** — documentation skeleton; decision log | E·N | emitted from instance (§12 Ω5); ADR + status discipline [Т]/[С]/[Г]/[О]/[И] (§13) |
| **TOGAF ADM / Zachman** — process cycle; interrogative coverage | E·E | Ω0–Ω9 with computable gates (§12); interrogatives = aspect×view queries (§13) |
| **AADL** — analyzable embedded semantics | E | O/L channel contracts carry analysis annexes; AADL as mandated view (§5) |
| **TLA+/Alloy** — formal behavior verification | E | mandatory formal view on heavy L-contracts (§13) |
| **DDD** — bounded contexts; context-mapping patterns | N·N | holon boundary = E-interiority (§3); T-77 typed cross-blocks incl. separate-ways zero (§9) |
| **Hexagonal/Clean** — dependency rule, ports/adapters | N | A-ports, O-adapters, protected L/S/E core; the rule is channel direction (§4) |
| **Parnas 1972** — information hiding as criterion | N | E is an *axis with a measure* (Coh_E), not advice (§4) |
| **Simon 1962** — near-decomposability | N | sparse-but-nonzero cross-blocks, quantified by the Φ window (§6) |
| **Alexander** — pattern language; semilattice not tree | N | Fano incidence: overlapping lines over 7 aspects — a semilattice by theorem (§11) |
| **DSM** — dependency matrix + clustering | N | Γ *is* the matrix — typed, PSD, dynamic, thresholded (§3) |
| **VSM** — viability criterion; recursion; algedonic channel | N·N·N | four invariants [Т] (§6); depth tower (§10); $\mathcal V_{\mathrm{hed}} = dP/d\tau$ (§7) |
| **MAPE-K** — autonomic loop over knowledge | N | φ(Γ) + reconciliation flows, with convergence theorems (§8, §7) |
| **Erlang/OTP / Kubernetes** — supervision; desired-state reconciliation | N·N | ℛ replacement flow (§7); ρ* attractor + DU channel (§5, §7) |
| **Reactive Manifesto** — responsive/resilient/elastic/message-driven | N | thresholds + ℛ + O-budget elasticity + A/D channel style (§6, §7) |
| **12-Factor** — operational hygiene | E | each factor lands in an aspect checklist at Ω2 (§12) |
| **CALM** — coordination boundary | E | mandatory monotone/coordinated field on LU contracts (§9) |
| **Conway / Team Topologies** — org↔system mirror; interaction modes | N·N | org-holon ⊗ system-holon cross-block (§9) |
| **ATAM** — scenario-based tradeoff analysis | N | ablation calculus: scenario = ablation, sensitivity = ∂verdict (§12 Ω4) |
| **Spec Kit SDD** — constitution→specify→plan→tasks | N | Ω0–Ω9 with mathematics inside the gates (§12) |
| **AGENTS.md** — machine context for repos | N | the `holarch.v1` instance *is* the design-level machine context (§14) |
| **MCP / A2A** — tool contracts; agent peering | N·N | SL/AS contract channels (§5); T-77 synastry with measurable gain (§9) |
| **Anthropic agent patterns** — workflows-vs-agents; evaluator-optimizer | N | DL regulation loop + LE evidence critic + R_φ fidelity (§17, §8) |
| **LangGraph/AutoGen/CrewAI** — orchestration graphs | E | U-organ emitted as graph views (§13) |
| **Nym/Loopix · Ethereum-modular · seL4** — reference architectures | N·N·N | re-derived in §15; re-derived in §16; LO-grounding channel at [Т]-grade (§5) |

Reading the table honestly in both directions: HOLARCH **adds** to every row at least
one of {computable invariants, typed channels, dynamics, anti-Goodhart, composition
arithmetic, depth ceiling, diagnosability} — the seven absences of §2; and HOLARCH
**loses** to the field in exactly one column (tooling maturity), stated in §19 rather
than hidden in an appendix.

## §19. Critical analysis: boundaries, falsifiers, the one gap {#границы}

A meta-specification claiming perfection would refute itself; this section is the
spec attacking its own weakest planks, in descending order of load.

**The honest gap: tooling.** UML has forty years of editors, generators and trained
readers. HOLARCH's answer — inherit tooling through mandated view emission, keep the
model computable in a 700-line reference validator — is architecturally sound and
*young*. Until independent implementations of `holarch.v1` exist, "not inferior"
holds at the level of capability-by-mechanism (§18), not at the level of ecosystem
mass. This is the single **G** cell, and it closes only with adoption, not with
argument.

**Aspect assignment is judgment.** Whether a given artifact is S-work or L-work is a
modeling decision. The dictionary (§4–§5) is structured enough to make assignments
*arguable* — but inter-rater reliability is unmeasured. **OPEN protocol:** two
architects independently profile the same three systems; agreement below
Cohen's κ ≈ 0.6 on aspect budgets would demote the dictionary from "operational"
to "suggestive", and that result would be published in this page's status table.

**Threshold transfer is calibration, not derivation.** Inside Γ-mathematics the
thresholds are theorems. That a *software system's* concern budgets, assembled by the
§14 constructor, deserve those exact thresholds is an [О]-choice validated so far by
coherence of consequences (the ablation pathologies land on recognizable industry
failure modes) — not by field data. The DESIGN class exists precisely to keep this
distinction loud.

**Consonances are rhymes.** BFT's 1/3, client-diversity's 1/3–2/3, Buterin's
non-stacking L3s are *external* laws that share shape with internal theorems. The
laboratory states each pair precisely and tags them CONS/[И]. None is presented as a
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
| Seven-aspect alphabet is uniquely diagnosable at its size | [Т] import | T-224; HL01 |
| 21 channels; SSOT names carry engineering readings unmodified | [О]+[И] | HL01; §5 |
| Four invariants, thresholds, independence, robustness | [Т] import | T-124b/d, T-129, T-151; HL03 |
| Three-flow dynamics; silver feeding floor; halt/reignition | [Т]/[С] import | T-262, T-259, T-288/289; HL12 |
| Self-model functor, tower convergence, anti-Goodhart | [Т] import + [О] rule | T-96, T-191; §8 |
| Composition gain = 2‖γ_cross‖² | [Т] import | T-77; HL11 (240/240) |
| Depth ladder and ceiling 3 | [Т/С] import | T-142; HL02 |
| Pairwise monitoring is structure-blind; probe triads | [Т] import | T-226; HL13 |
| Three worked designs land in the window; ablations break their own invariant | DESIGN | HL04–HL06 |
| Mixnet arithmetic: f^ℓ, trilemma, knee at 3 | VERIFIED + external [Т] | HL08 |
| BFT-1/3 and client-diversity rhymes | CONS [И] | HL09, HL14 |
| Subsumption: 41 capabilities, 28 N / 12 E / 1 G | VERIFIED | HL07 |
| Integration rides shared flows, not pairwise links | VERIFIED (constructor) | §12; lab history |
| Inter-rater reliability of aspect assignment | **OPEN** | §19 protocol |
| Blind design-trial utility | **OPEN** | §19 protocol |

## §21. The laboratory {#лаборатория}

`architecture/holarch_lab.py` — panel HL01–HL14, all PASS at the time of writing:
SSOT synchronization (HL01), the depth ladder (HL02), Γ-calculator reference points
(HL03), the three worked designs with four-way ablations (HL04–HL06), subsumption
completeness with anchor resolution against this very page (HL07), mixnet arithmetic
(HL08), the two consonance blocks (HL09, HL14), the Fano-coverage meter (HL10), the
T-77 identity (HL11), the feeding fold (HL12), first-order blindness (HL13). One
command, no arguments, exit code is the verdict:

```bash
python3 architecture/holarch_lab.py
```

The panel is the release gate of this specification: any future edit that breaks a
row must either fix itself or change the page honestly.
