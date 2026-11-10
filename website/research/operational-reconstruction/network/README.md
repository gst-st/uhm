# Network reconstruction from transport and response

The primitive data are distinguishable inputs and readouts, local changes of frame, and possible compositions with their measured costs. An exact signed-interference model adds coherent linear combination as a separate experimental premise. Reference: operational-canon blueprint, SHA-256 `6d9a758e1b344d08aba44b40c13c44126200990bd21650a3befa72ab96526934`. The general cost result can be used on a register with no amplitudes or preassigned spatial dimension.

| Question | Construction and scope | Discriminating control |
|---|---|---|
| Can the same shared-mode generators commute on a faithful larger space? | Intertwining through an injection pulls commutativity back to the source. | The two hopping generators act differently in opposite orders on the source endpoint. |
| Can local gauge actions coexist with moving matter? | Orient links, act on both ends, and transport matter on each move. Each reversible move commutes with the full site action on complete configurations. For the finite group Q8 each station has an invariant orbit sum on the link-and-colour basis. | Changing only one incident link changes the signal. The distinct motion generators still fail to commute. Two commuting independent edge actions require different registers in this construction. |
| Can distance be inferred without choosing a graph? | Scan a decidable table of achievable costs through a witnessed bound. Idle, separation and relay composition yield a directed metric. Reversibility at no greater cost is equivalent to symmetry. Two probes have identical costs iff they can match one another's transfers at no greater cost. A uniform overhead per complete transfer gives a corresponding bound on the distance discrepancy. | Forward transfer can take one tick while the reverse handshake takes two. Unknown entries in an experimental table are unmeasured. A scan certifies minimality only for a complete physical or mathematical protocol class. |
| Does such a metric appear in an actual signal? | On a synchronous one-dimensional local update, induction determines the entire leading front. Reflection gives the reverse experiment. Three-station readout agrees with the path metric for every pair when the front is visible in both directions. Independent local frames leave the complete response covariant. Positive two-bond delays have one shape up to one factor per probe iff the reference minors vanish. | On a fixed chain two different internal operators give all six off-diagonal delays 2,3,5 (in each direction). A slower second segment for only one species gives the nonzero minor 2. |
| Can a holonomy change apparent timing on the same network? | Two equally early arms can cancel. Reversing the relative phase of one arm and keeping both observations restores the front. The bound on the stronger registration is sharp. Four intensity differences yield the two quadratures of the relative transport. | In the fundamental and conjugation representations the same central minus sign gives different one-setting readouts. A physical arm control must act after choosing the representation. |
| Can a reporting time identify an inner onset? | A crossed table of integer times separates into a condition and a mode offset iff its reference rectangle contrasts vanish. The two offsets retain a free additive constant. | Synthetic tables differing in one cell discriminate an interaction; distinct event/report splittings with identical observations demonstrate non-identifiability. |

The physical continuum, a unique microscopic gauge group, a Standard Model matter spectrum and empirical equivalence of contemplative experiences each require new evidence. The additive reporting model is a protocol for future data. The three-station simulation uses unnormalized linear response amplitudes; unitarity of an individual link does not imply unitarity of the full discrete update. Cost-composition geometry, lattice gauge covariance, two-arm interference and additive effects have established precedents. The package contribution is their scoped operational synthesis, the exact probes and the counterexamples used to decide between the models.

## Cycles and changes of scale

| Measured property | Exact reduction or obstruction |
|---|---|
| State after a closed walk | For supplied root access walks, one simultaneous conjugator for the rooted edge loops reconstructs the frames at every node. With internal access and separate crossing ports, contracting a cell preserves the probe's transport iff the internal edge loops are trivial. [CyclicTransport](CyclicTransport.lean) |
| First delivery | The Boolean update on finite incoming lists gives a physical walk of exactly the detected length, and its first tick realizes the protocol minimum. The time of a coherent response is controlled by the net amplitude in each parity class of simultaneously arriving routes. A shared switch can leave a receiver dark forever. [SignalNetwork](SignalNetwork.lean) · [RouteReadout](RouteReadout.lean) |
| Terminal reduction | Cutting a fine walk at successive terminals gives macro passages with the same total cost. Keeping full impulse kernels instead carries the delayed response and initial hidden excitation of an additive network onto its boundary. [TerminalNetwork](TerminalNetwork.lean) · [BoundaryMemory](BoundaryMemory.lean) |
| Block contraction | Every proposed coarse step must lift from every actual starting port to its destination block within budget to preserve reachable balls. The criterion composes through nested scales. With switch diameter D and free endpoints, the excess fine cost is at most (m−1)D for m≥1 steps. The cyclic two-port strip attains the bound for arbitrarily large m. [PortQuotient](PortQuotient.lean) · [ScaleObstruction](ScaleObstruction.lean) |
| Macroscopic comparison | Mutual calibrated simulations characterize a common distance table. At increasing scales, uniform vanishing of normalized discrepancies transfers convergence to the same reference table. A fixed positive tick can collapse in that limit. Uniform physical delay lines multiply all first arrival times by the same factor, including on cyclic networks. [NetworkScale](NetworkScale.lean) · [ClockRefinement](ClockRefinement.lean) |

## Common limiting geometry

- [Clock normalization](ClockNormalization.lean) and [the limit construction](LimitMetric.lean) use natural cross-products throughout. Positive tick calibrations may differ between probes. A common positive limit for a pair exists iff the reference readings are Cauchy, the calibrated discrepancy vanishes and the reference has a positive tail. The limit is constructed in the quotient of nonnegative dyadic Cauchy names and is unique for the specified convergence.
- [Dynamic refinement](DynamicRefinement.lean) and [common geometry](CommonGeometry.lean) derive tail estimates from simulations of actual passages. A reserve pays for the next refinement and tends to zero in common units. Conditional on these certificates a pair is positively separated iff **one finite** local causal register rises by more than that level's reserve. The first-arrival clock realizes the extremum. Local root-loop measurements in [CycleDelays](CycleDelays.lean) also test equality of constrained round trips. Asymptotic reciprocity of each probe then gives agreement of one-way readings.
- [PeriodicLimit](PeriodicLimit.lean), [CircleLimit](CircleLimit.lean) and [ProductLimit](ProductLimit.lean) connect the ordinary local pulse detector to the circle of binary angular addresses modulo zero angular separation and to the sum metric on its square. The examples include positive separation of antipodes, explicit dense stations, nonuniform interior delays and a diagonal actuator which changes the geometry. [MeshControl](MeshControl.lean) bounds the distortion for unlabelled stations when port coverage is certified. [DriftControl](DriftControl.lean) constructs reciprocal first arrivals with adjacent normalized changes tending to zero and no limiting time.
- Native Verum independently replays the refinement-surplus induction, local finite-speed lower bounds on real walks, convergence transfer, positivity, and the reciprocity step for round trips. It also checks finite clock, shortcut and diagonal-actuator controls and rejects their semantic mutations. The general construction of real-valued distances and the infinite-address circle and torus theorems are Lean proofs. The [receipt](verum-receipt.json) records what the native profiles check.

## Replay

From this directory use Lean 4.35.0 (Std only), a Python 3 interpreter and the native `verum-source-replay` checker from the `verum_source_proof` crate.

~~~sh
lake build
python3 -B audit_lean.py --replay-kernels
python3 -B experiment.py
python3 -B network_scale_experiment.py
python3 -B boundary_experiment.py
python3 -B limit_experiment.py
python3 -B replay_verum.py /absolute/path/to/verum-source-replay
~~~

The Lean audit inventories theorem declarations in the compiled environment of every local module, including private and generated proofs. It rejects local axioms and dependencies outside `propext` and `Quot.sound`. The optional kernel replay exports public theorem closures from these same modules to a temporary NDJSON file and sends it to leanchecker-paranoid, lean4lean and nanoda. Nanoda receives an explicit axiom whitelist. The temporary export is released after verification.

Native Verum verifies source contracts for the declared logical and finite profiles. The Church-fold path constructors and dependent port lifting, transfer of attained minima, and compositional calibration checks are parametric. Finite controls include the six-edge ring, incompatible loop gauges, signal loss with four paths and hidden boundary memory. The replay checks independently specified logical types, native verdicts, source digests, finite coverage and a rejected mutation per declaration. The [receipt](verum-receipt.json) gives the exact coverage and binary digest. General graph induction, the quantitative sharp bound, cyclic coherent response and calibrated asymptotics are proved in Lean.

## Canon pages

- [Gauge transport](../../../docs/networks/three-node-transport.md)
- [Distance from response](../../../docs/geometry/response-metric.md)
- [Practice and report](../../../docs/consciousness/empirical/practice-and-report.md)
- [Cycle observations](../../../docs/networks/cycle-observations.md)
- [Networks across scales](../../../docs/geometry/network-scales.md)
- [Common limiting distance](../../../docs/geometry/common-limit.md)
- [Result registry](../../../docs/reference/network-results.md)
