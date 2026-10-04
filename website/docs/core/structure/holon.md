---
sidebar_position: 1
title: Holon
description: Self-sustaining configuration Γ
---

# Holon ($\mathbb{H}$)

A **Holon** is a proposed model of a system that maintains a specified organisation under declared environmental conditions **[D/H]**. This chapter distinguishes the numerical state, its physical readout, dynamics and capability certificates. The categorical primitive is a chosen structured sheaf model, not a unique density matrix containing all of reality. See the [typed mathematical kernel](/docs/reference/mathematical-kernel).

## Historical precursors

The idea of self-sustaining wholes has deep roots in the scientific thought of the twentieth century.

**Arthur Koestler** (1967) introduced the term **"holon"** in his book *The Ghost in the Machine*. Koestler noticed a paradox: every entity in nature is simultaneously a **whole** (a self-contained unit) and a **part** of something larger. A cell is a whole with respect to its molecules, but a part of an organ. An organ is a whole with respect to cells, but a part of an organism. Koestler called this duality a "holon" (from Greek *holos* — whole + the suffix *-on* denoting a constituent, as in "proton", "neutron"). UHM inherits this intuition, giving it precise mathematical meaning.

**Humberto Maturana and Francisco Varela** (1972) formulated the concept of **autopoiesis** — self-production. An autopoietic system is a system that continuously produces the components of which it is itself composed. A living cell is the classic example: it is constantly being broken down and rebuilt, yet preserves its organisation. In UHM this corresponds to condition **(AP)** — autopoietic closure.

**Robert Rosen** (1991), in his theory of **(M,R)-systems**, showed that the living cannot be reduced to a mechanism: it requires a special type of closure in which the "repair" function of the system is itself part of the system. In UHM this is formalised through the regeneration operator $\mathcal{R}$ and condition **(QG)**.

The Holon in UHM **unifies and formalises** all three ideas: the whole/part duality (Koestler), self-production (Maturana/Varela), and functional closure (Rosen) — within a single mathematical object.

| Precursor | Key idea | What is formalised in UHM |
|---|---|---|
| Koestler (1967) | Holon = whole and part | Nesting hierarchy of Holons; $\mathrm{Tr}_E$ — part, $\Gamma_{\text{global}}$ — whole |
| Maturana/Varela (1972) | Autopoiesis = self-production | Condition (AP): closure of the autopoietic cycle |
| Rosen (1991) | (M,R)-closure = repair of the repairer | Condition (QG): operator $\mathcal{R}$ regenerates itself as well |

**Mapping scope [I/H].** These precursors motivate the vocabulary; the correspondences to a numerical feedback model are additional hypotheses, not proofs that a physical system satisfies the Holon predicates.

## Intuitive explanation

The whirlpool analogy describes persistence of a pattern despite exchange of components **[I]**. It motivates a distinction between a state and the mechanisms maintaining it. It does not prove that every pattern has phenomenal experience or that seven numbers completely describe a cell or brain. Physical autonomy, self-maintenance and experience require independently specified tests.

## Ontological status

The categorical layer is the chosen $\mathcal E_N=\operatorname{Sh}_\infty(\operatorname{Open}(D_N,d_B),J_{\mathrm{open}})$; process maps live in the separate channel category. A numerical state $\Gamma\in D_7$ belongs to an effective state model. Connecting it to a sheaf object and a physical system requires declared representation and observation maps **[P/H]**.

The model distinguishes autonomy and maintenance conditions (AP)+(PH)+(QG)+(V) from the operational hierarchy. $R=1/(7P)$ lies in $[1/7,1]$, so “fundamental mode $R=0$” is impossible in this definition. Vanishing regeneration rate or absent tested self-model can be recorded separately. An organisational hierarchy is not a cognitive-depth hierarchy.

## Hierarchical definition

The following levels organise a model specification [D]. Their numbering does not assert a universal self-reference depth or an empirically established L-level.

### Level 0: Global Γ

Choose a Hilbert space $\mathcal H_{\mathrm{global}}$ and, when appropriate, a trace-class state

$$
\Gamma_{\mathrm{global}}=\Gamma_{\mathrm{global}}^\dagger\succeq0,\qquad
\operatorname{Tr}\Gamma_{\mathrm{global}}=1.
$$

These conditions define valid density matrices; they do not select a unique state. A topos has a terminal object, but it is not $I_7/7$ or a cosmological attractor. In the channel category the tensor unit is the one-dimensional system with its discarding map. A global physical state and its relation to the categorical layer are additional model inputs **[P/H]**.

### Level 1: Subsystem

Given an actual factorization $\mathcal H_{\mathrm{global}}=\mathcal H_S\otimes\mathcal H_{\mathrm{env}}$, define

$$
\Gamma_S=\operatorname{Tr}_{\mathrm{env}}\Gamma_{\mathrm{global}}.
$$

The partial trace preserves positivity and trace **[T]**. Its existence uses the supplied tensor factorization; a semantic axis or arbitrary vector-space summand does not supply that factor. Purity may increase or decrease: $|u\rangle\langle u|\otimes I_7/7$ has joint purity $1/7$ and a pure system marginal. A marginal alone does not reconstruct its correlations with the environment.

### Level 2: Autonomy

Autonomy is a declared criterion involving the subsystem, environment, allowed perturbations and dynamics **[D/H]**. The linked conditions [A1–A3](../foundations/axiom-septicity#предварительное-условие-автономность) must be operationalised. A physical boundary is not the quantum separability condition: separable mixed states can have classical correlations, and a chosen tensor factor need not be dynamically autonomous. Stability requires an actual stability or recovery estimate; it is not implied by naming a boundary.

### Level 3: 7D structure

A seven-dimensional effective state is a selected representation **[P]**, conditional on a readout. If an actual factorization $\mathcal H_S\cong\mathbb C^7\otimes\mathcal H_{\mathrm{internal}}$ is supplied, then $\Gamma_S^{(7)}=\operatorname{Tr}_{\mathrm{internal}}\Gamma_S\in D_7$. More generally one can declare a CPTP readout $\Lambda$ into $D_7$ and test its sufficiency for a specified family of tasks.

The names $A,S,D,L,E,O,U$ are semantic assignments, not a proof that every autonomous system has seven independent physical degrees of freedom. The [minimality result](../../proofs/minimality/theorem-minimality-7) retains its distinguishability premises. In particular the basis axis $O$ is not a nontrivial tensor-factor clock.

### Relation to quantum mechanics

A chosen contraction/compression $\Pi_7:\mathcal H_{\mathrm{full}}\to\mathbb C^7$ with $\Pi_7^\dagger\Pi_7\le I$ gives a subnormalised state $\widetilde\Gamma=\Pi_7\rho\Pi_7^\dagger$. For $p=\operatorname{Tr}\widetilde\Gamma>0$, the conditional state is $\Gamma_{\mathrm{eff}}=\widetilde\Gamma/p$. Report $p$: this conditioning is not a deterministic linear CPTP readout. Alternatively specify a genuine CPTP reduction including the excluded outcomes.

Mapping operators, populations or a spin marginal to semantic roles requires a representation bridge **[H/I]**. It is not a consequence of standard quantum mechanics and does not claim that $D_7$ suffices for every spectrum, physical system or conscious phenomenon.

### Level 4: Holon (definition)

**Definition [D].** A Holon model is an augmented record

$$
\mathbb H=(\Gamma,\mathsf{Readout},\mathsf{Dynamics},\mathsf{Environment},M,\mathsf{Tests}),\qquad\Gamma\in D_7,
$$

with the declared autonomy and maintenance predicates (AP)+(PH)+(QG)+(V). The readout specifies the physical-to-state map and uncertainty; the dynamics specifies $H$, dissipative channels and any feedback; tests specify operational targets. PH as an experiential interpretation retains **[I/H]**. The numerical cut V is a definition, not a theorem about biological survival.

A numerical self-model $M:D_7\to D_7$ is distinct from the logical support reflector $\varphi$. A state-preserving $M$ need not be affine or CPTP. Frozen channel parameters may define CPTP maps; state-dependent selection generally gives a nonlinear map. Neither $H$, $M$, environmental coupling nor observation law can be reconstructed uniquely from a single $\Gamma$.

## Fundamental properties

### 1. Structural self-similarity

Within the selected effective model, different systems have states in the same type of space $D_7$ **[D]**. This is a common representation, not an isomorphism of all physical Hilbert spaces or a lossless description of every system. Readout, dynamics, stored records and task capabilities can differ even when $\Gamma$ is identical.

### 2. Partiality (boundary)

A supplied tensor factorization permits $\Gamma_{\mathbb H}=\operatorname{Tr}_{\mathrm{env}}\Gamma_{\mathrm{total}}$ **[T]**. The physical boundary and its relation to that factorization are separate modeling inputs. A basis partition or compressed block is not automatically a partial trace or a subsystem with independent dynamics.

### 3. Dynamicity

The canonical candidate flow is

$$
\dot\Gamma=-i[H,\Gamma]+\mathcal D(\Gamma)+a(\Gamma)(M(\Gamma)-\Gamma),\qquad a\ge0.
$$

For locally Lipschitz $a,M$, $M(D_7)\subseteq D_7$, and a fixed GKSL linear part, the density-state domain is forward invariant and solutions continue globally **[T]**; see the [kernel](../../reference/mathematical-kernel#dynamics). This nonlinear flow is not automatically a linear CPTP semigroup.

A stationary solution is compatible with maintenance; $\dot\Gamma=0$ does not mean the system ceases to exist. Unitary motion preserves spectrum. General dissipation can purify as well as mix; convergence to $I_7/7$ requires the relevant unital mixing assumptions. The feedback term need not raise purity in every state. A physical energy/resource balance requires specified Hamiltonians, reservoirs and currents; the scalar feedback rate and semantic O-axis do not supply it. Internal time needs a separately supplied clock and constraint, not the basis axis alone.

### 4. Interiority

Interiority is the ontological interpretation **[I]** of the model. Formal capabilities use an augmented record and the [canonical hierarchy](/docs/consciousness/hierarchy/interiority-hierarchy).

$$
\mathrm{Cap}_2=(P>2/7)\land(R\ge1/3)\land(\Phi\ge1)\land(D_{\mathrm{diff}}\ge2),
\quad R=1/(7P),\quad\Phi=P/\sum_i\gamma_{ii}^2-1.
$$

L1 requires the declared experiential realization or proxy; a 7D basis axis is not a multidimensional $\rho_E$. L3 adds nontrivial held-out metamodel prediction tests; L4 is an ideal compatible tower. The former $P>6/7$ clause contradicts inherited $P\le3/7$ and is withdrawn. A fixed point or successive fidelity equal to one does not certify these tests. Neither Gap nor a chosen SAD score fixes the physical level, and no universal depth ceiling of three follows.

## Examples of Holons

The examples are motivating interpretations [I/H], not reconstructed state certificates or proofs of physical L-levels.

### Cell

A cell motivates the autonomy and self-maintenance vocabulary [I]. Assigning receptors, structure, metabolism, regulation, internal records, resources and integration to the seven roles is a candidate encoding [H]. It does not measure purity or establish a phenomenal state. The readout and closure tests must be supplied independently.

### Brain

A brain motivates tests of self-model predictions and task-dependent access [H]. Its physical L-label cannot be inferred from the word “brain”, an unmeasured R, or an assumed cell-to-brain distinction. The canonical gate and higher-order certificates require a validated observation model and actual task data.

### Ecosystem

An ecosystem can motivate a composite model [H]. Whether it has autonomous maintenance or a collective capability is an open empirical question requiring joint dynamics and a declared collective readout; mutual information alone does not decide it.

### What is NOT a Holon

A feedback device, passive material structure or software description is not automatically a Holon. Evaluate the stipulated autonomy and closure predicates rather than inferring their failure from a name or setting R=0. Dependence on environmental resources alone does not exclude self-maintenance: the allowed environment is part of the criterion.

## Nesting hierarchy

A declared subsystem can be contained in a composite system. Nesting of physical boundaries, tensor factors and effective models must be specified separately. Neither a partial trace nor a hierarchy of organisational names guarantees that every part or aggregate satisfies the Holon predicates.

### Taxonomy by levels of organisation {#таксономия-по-уровням-организации}

| Model class [D/H] | Required evidence |
|---|---|
| State configuration | Valid state and readout |
| Holon | Declared autonomy and (AP)+(PH)+(QG)+(V) tests |
| L2-capable Holon | Full $\mathrm{Cap}_2$ and experiential test |
| L3-capable Holon | L2 plus nontrivial metamodel prediction certificate |
| Ideal L4 model | Compatible certificates at every order |

These are model predicates, not universal labels for particles, cells, meditators or societies. The numerical cuts are chosen operational criteria; their algebraic consequences are theorems, and their physical interpretation retains its bridge hypotheses.

## Life cycle of a Holon

Emergence, persistence and loss of an organisation require a model of the relevant processes and an independent identification criterion [H]. They are not determined by a single purity trajectory. A new attractor or bifurcation requires a parameterized flow and its stability conditions; loss of a certificate does not by itself establish biological death or irreversible loss of personal records.

## Composition of Holons

### Tensor product

For two supplied seven-dimensional factors,

$$
\mathcal H_{12}=\mathbb C^7\otimes\mathbb C^7\cong\mathbb C^{49},\qquad
\Gamma_{12}\in D_{49},\qquad\Gamma_i=\operatorname{Tr}_{\bar i}\Gamma_{12}.
$$

A declared interaction Hamiltonian may be $H_{12}=H_1\otimes I+I\otimes H_2+V_{12}$. Its channels, feedback and environment must also be specified. The joint density-state affine space has dimension $49^2-1=2400$; at fixed marginals, its correlation degrees have dimension $2400-2(7^2-1)=2304$. The difference $49-14$ is not a correlation count.

Total mutual information is

$$
I(1:2)=S(\Gamma_1)+S(\Gamma_2)-S(\Gamma_{12})
=D(\Gamma_{12}\|\Gamma_1\otimes\Gamma_2)\ge0.
$$

It vanishes exactly for a product state **[T]**. Separable mixtures can have positive classical correlations: $\sum_i p_i|ii\rangle\langle ii|$ has $I=H(p)$ without entanglement. Thus mutual information is not an entanglement criterion or a numerical proof of collective agency.

An effective joint state in $D_7$ needs a declared readout $\Lambda_{12}:D_{49}\to D_7$ and task-sufficiency tests. No generic projection preserves all marginals or proves one collective subject. See [Composite systems](../dynamics/composite-systems).

### Closure of composition

Tensor composition preserves the density-state types, but does not automatically preserve autopoiesis, viability or capability. These predicates must be tested on the joint model with its environment and readout [D/H]. An interaction can disrupt the maintenance of either component; no universal mutual-information threshold proves closure.

## Viability condition

The chosen structural-majority criterion V is $P>2/7$ **[D/I]**. The exact identity

$$
P=1/7+\|\Gamma-I_7/7\|_F^2
$$

implies that $I_7/7$ is the only state at $P=1/7$ **[T]**. Every different state is mathematically distinguishable from it by some measurement; no universal $2/7$ detection threshold follows without a sample/noise model.

**Counterexample to irreversible dissolution at the cut.** The valid driven flow $\dot\Gamma=\lambda(\rho_a-\Gamma)$, $\lambda>0$, with pure $\rho_a$ and initial $I_7/7$ has

$$
\Gamma(\tau)=e^{-\lambda\tau}I_7/7+(1-e^{-\lambda\tau})\rho_a,
\qquad P(\tau)=\frac{1+6(1-e^{-\lambda\tau})^2}{7}.
$$

It crosses $2/7$ from below. Consequently neither positivity nor a GKSL realization forbids recovery of the chosen numerical score below that cut. Imposing a vanishing input/feedback rate there would be an extra dynamical assumption. Conversely a replacement channel preserves trace one while erasing every input record, so normalization is not conservation of identity. Physical survival and record continuity require independent criteria.

## Open questions

Open questions concern an identifiable physical-to-state readout, independent autonomy/maintenance tests, task sufficiency of D7, collective readouts from D49, operational higher-order certificates and record continuity. The scalar window (2/7,3/7] is an algebraic consequence of the chosen gate; its phenomenal or biological interpretation needs evidence. The [research programme](/docs/applied/research/symbolic-correspondence#программа) must retain those bridges explicitly.
