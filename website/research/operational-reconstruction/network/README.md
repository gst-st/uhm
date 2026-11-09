# Experiments on three stations

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

## Replay

From this directory use Lean 4.35.0 (Std only), a Python 3 interpreter and the native `verum-source-replay` checker from the `verum_source_proof` crate.

~~~sh
lake build
python3 -B audit_lean.py
python3 -B experiment.py
python3 -B replay_verum.py /absolute/path/to/verum-source-replay
~~~

The Lean audit examines all theorem dependencies in the six local Lean modules. It refuses unreviewed axioms, including `Classical.choice` and `sorryAx`. It does not infer experimental validity from theorem names.

Verum checks two parametrically typed propositions using the native logical profile and six finite source contracts covering 73 input cases. The two logical statements are compared with independently specified de Bruijn types; for the finite profile the native checker binds the function body, contract and number of input cases. Every declaration has a separately rejected semantic mutation. The [native receipt](verum-receipt.json) identifies the binary, the source bytes and the returned kernel. A successful Lean compilation or the Python simulator cannot substitute for native Verum replay. The general induction for the propagation front and the cost/reciprocity biconditionals are Lean results; the finite Verum contracts have the scopes recorded in the receipt.

## Canon pages

- [Gauge transport](../../../docs/networks/three-node-transport.md)
- [Distance from response](../../../docs/geometry/response-metric.md)
- [Practice and report](../../../docs/consciousness/empirical/practice-and-report.md)
- [Result registry](../../../docs/reference/network-results.md)
