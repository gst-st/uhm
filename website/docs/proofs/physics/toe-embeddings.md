---
sidebar_position: 3
title: "Embeddings of Alternative ToEs"
slug: /proofs/physics/toe-embeddings
description: "M-theory, loop quantum gravity and causal sets relative to UHM: the G2 coincidence, encodings of spin networks and posets in holonic states, and the universal property of the UHM kinematic object."
---

# Embeddings of Alternative Candidate Theories into UHM

:::info Status
The results distinguish three mathematical questions. Which finite records can a matrix encode? Which symmetry groups agree? Which morphisms exist between specified systems? Identifying two physical theories additionally requires a correspondence between their observables and dynamics.
:::

---

## 1. M-Theory on $G_2$-Manifolds {#m-теория}

### 1.1 Mathematical Context

M-theory compactified on a 7-dimensional manifold $M_7$ with holonomy $\mathrm{Hol}(M_7) = G_2$ gives $N=1$ supersymmetry in 4D (Acharya, 1998; Atiyah–Witten, 2001; Joyce, 2000). Key results:

- **Acharya (1998, hep-th/9812011):** M-theory on a compact $G_2$-manifold → $N=1$ 4D, gauge groups from singularities.
- **Atiyah–Witten (2001, hep-th/0107177):** M-theory on $G_2$-manifolds with conical singularities → chiral fermions.
- **Halverson–Morrison (2015, 1507.05965):** Systematic extraction of gauge groups from $G_2$-compactifications. $SU(3) \times SU(2) \times U(1)$ from $A$-$D$-$E$ singularities on co-compact submanifolds.
- **Acharya–Witten (2001, hep-th/0109152):** $G_2$-compactification as «M-theory on $G_2$» — a systematic review.

### 1.2 UHM ↔ M-Theory Correspondence {#uhm-m-theory}

#### T-170: The M-theory correspondence — the group coincidence and the finite partition function [T], the correspondence of partition functions [H] {#t-170}

The automorphisms of the torus as a compact abelian group form the discrete group $GL(21,\mathbb Z)$. Every continuous action of connected $G_2$ by such automorphisms is trivial. In the density-matrix representation, general octonionic rotations also change the moduli of the entries. Thus neither argument supplies a nontrivial action on the fixed-modulus torus.

:::tip T-170. Parts (i)–(iii) [T], partition-function correspondence [H]
**(i) Group coincidence [T].** Let $\varphi_0(x, y, z) = \langle x, yz \rangle$ be the associative 3-form on $\mathrm{Im}\,\mathbb{O} = \mathbb{R}^7$ of the Fano multiplication. Its stabiliser in $GL(7, \mathbb{R})$ is $G_2 = \mathrm{Aut}(\mathbb{O})$; at the level of Lie algebras, $\{X \in \mathfrak{gl}(7, \mathbb{R}) : X \cdot \varphi_0 = 0\} = \mathrm{Der}(\mathbb{O})$, of dimension 14. This is the group whose holonomy defines a torsion-free $G_2$-structure on a 7-manifold, and $G_2 \subset \mathrm{Spin}(7)$ is the stabiliser of one unit spinor of the 8-dimensional spin representation — the single parallel spinor behind $N = 1$ in 4D.

**(ii) Finite-$M$ partition function [T].** For $M \in \mathbb{N}$ and $S_{\text{Gap}}$ continuous on the torus $(S^1)^{21M}$, the integral $Z^{(M)}_{\text{UHM}} = \int_{(S^1)^{21M}} e^{-S_{\text{Gap}}[\theta]}\, d\theta$ (normalised Haar measure) is finite and strictly positive.

**(iii) Thermodynamic-limit states [T].** Let $\mathfrak{A} = \bigotimes_{v \in \mathbb{N}} M_7(\mathbb{C})$ be the quasi-local (UHF) $C^*$-algebra, and $\omega_M$ the state that is $\mathrm{Tr}(\rho_M\,\cdot)$ on the first $M$ factors and a fixed product state on the rest. The sequence $(\omega_M)$ has a weak-$*$ convergent subsequence, and every limit is a state on $\mathfrak{A}$. Uniqueness of the limit is not claimed.

**(iv) Correspondence [H].** Equality of partition functions requires compatible field domains, actions, measures and parameter matching on both sides. The group identity and compactness in (i)–(iii) do not establish those data.
:::

**Proof of (i).** A linear map preserving $\varphi_0$ preserves the metric, because the metric is determined by $\varphi_0$ through $6\,\langle x, y\rangle\,\mathrm{vol} = (x \lrcorner \varphi_0) \wedge (y \lrcorner \varphi_0) \wedge \varphi_0$ (Bryant 1987, "Metrics with exceptional holonomy", §2), and therefore it preserves the cross product $\langle x \times y, z\rangle = \varphi_0(x, y, z)$ and the octonion product $xy = -\langle x, y\rangle + x \times y$ on $\mathrm{Im}\,\mathbb{O}$; conversely an automorphism of $\mathbb{O}$ preserves $\varphi_0$. So $\mathrm{Stab}_{GL(7)}(\varphi_0) = \mathrm{Aut}(\mathbb{O}) = G_2$. That $G_2$ is the holonomy group of a torsion-free $G_2$-structure and fixes exactly one spinor of $\mathrm{Spin}(7)$ is standard (Bryant 1987; Harvey, *Spinors and Calibrations*, 1990; Joyce 2000). $\square$

### T-170′. Perturbative matching requirements {#т-170-prime}

A comparison order by order requires two defined, regularized expansions with matched coefficients. No such pair of expansions is specified for the full M-theory correspondence here.

### T-170″. Finite partition functions and limit states {#т-170-double-prime}

Parts (ii) and (iii) concern a specified finite torus model and normalized states on a quasi-local algebra.

**Proof of (ii).** The torus $(S^1)^{21M}$ is compact and $S_{\text{Gap}}$ is continuous on it (a trigonometric polynomial in the phases), so $\lvert S_{\text{Gap}} \rvert \leq C$ for some $C < \infty$. The integrand lies in $[e^{-C}, e^{C}]$ and the normalised Haar measure has total mass 1, so $e^{-C} \leq Z^{(M)}_{\text{UHM}} \leq e^{C}$. $\square$

**Proof of (iii).** The state space of the unital $C^*$-algebra $\mathfrak{A}$ is weak-$*$ compact (Banach–Alaoglu) and, $\mathfrak{A}$ being separable, metrisable; hence $(\omega_M)$ has a convergent subsequence. Positivity and $\omega(1) = 1$ pass to weak-$*$ limits, so every limit is a state (Bratteli–Robinson, *Operator Algebras and Quantum Statistical Mechanics*, Vol. 1). $\square$

**Inputs.** The stabilizer of the positive three-form, compactness of the finite field domain, and weak-* compactness of the state space enter the three mathematical conclusions.

Numerical check: `check_core_numbers.py`, `test_t170_gap_phases_carry_no_g2_action_and_the_torus_quotient_is_not_an_orbifold` — the stabiliser of $\varphi_0$ in $\mathfrak{gl}(7)$ has dimension 14 and is annihilated exactly by the 14 derivations of $\mathbb{O}$; on $\mathbf{14} \oplus \mathbf{7}$ the $G_2$-orbits of a generic point, of $(0, v)$ and of $0$ have dimensions 14, 6 and 0; two states with equal phases and different moduli get phases differing by more than 0.5 rad under one $g \in G_2$.

### 1.3 Formal Functor {#функтор-m-theory}

A Gelfand spectrum construction requires a chosen commutative algebra. The full tensor product of internal matrix algebras is noncommutative. A functor to $G_2$-manifolds would additionally have to assign a seven-manifold, a torsion-free structure and compatible maps to each object and arrow. [T-170](#t-170) establishes a group identity.

### 1.4 Embedding Assessment

| Aspect | Status | Comment |
|--------|--------|---------|
| $G_2$-symmetry coincides | **[T]** | T-170 (i): $\mathrm{Stab}_{GL(7)}(\varphi_0) = \mathrm{Aut}(\mathbb{O})$, Lie algebra of dimension 14 |
| $N=1$ SUSY | **[T]** at the group level | $G_2 \subset \mathrm{Spin}(7)$ fixes exactly one spinor; the physical identification $\eta_0 = 1_{\mathbb{O}}$ is part of (iv) [H] |
| $SU(3) = \mathrm{Stab}_{G_2}(e_O)$ | **[T]** | T-42e; "the same mechanism as the singularity gauge groups of Acharya and Halverson–Morrison" is not proved [H] |
| Phase quotient | Obstruction | There is no nontrivial continuous action of $G_2$ by group automorphisms on the torus. |
| Perturbative correspondence $Z_{\text{UHM}} = Z_M$ | **[✗]** as a theorem | $Z_M^{\text{pert}}$ is not defined; the equality is part of (iv) [H] |
| Finiteness of $Z_{\text{UHM}}^{(M)}$ | **[T]** | T-170'' (ii), on the torus $(S^1)^{21M}$ |
| Thermodynamic-limit states | **[T]** existence | T-170'' (iii); uniqueness open |
| Non-perturbative definition of $Z_M$ (M-theory) | open | External open problem of M-theory |

---

## 2. Loop Quantum Gravity {#пкг}

### 2.1 Mathematical Context

Loop quantum gravity (LQG) is based on:
- **Spin networks** (Penrose, 1971; Rovelli–Smolin, 1995): graphs with edges labeled by $SU(2)$ representations and vertices labeled by intertwiners.
- **Spin foams** (Baez, 1998; Perez, 2013): 2-complexes as the «evolution» of spin networks, defining transition amplitudes.
- **Key algebra:** $SU(2)$ — gauge group in the Ashtekar formalism.

Connection $SU(2) \subset G_2$: the chain of embeddings

$$
SU(2) \subset SU(3) \subset G_2
$$

where $SU(3) = \mathrm{Stab}_{G_2}(e_O)$ (T-42e [T]) and $SU(2) \subset SU(3)$ is the standard embedding.

### 2.2 Embedding Construction {#lqg-embedding}

#### T-171: Spin networks are encoded in holonic states [T] {#t-171}

:::tip T-171. Encoding a finite labelled spin network [T]
Let $\mathcal{S} = (G, j, k)$ be a finite spin network: a finite directed graph $G = (V, E)$ without loops and with at most one edge between two vertices, spins $j_e \in \tfrac12\mathbb{Z}_{\geq 0}$ (unbounded), and at each vertex $v$ a label $k_v \in \mathbb{Z}_{\geq 0}$ — the index of an intertwiner in a fixed orthonormal basis of $\mathrm{Inv}\big(\bigotimes_{e \ni v} V_{j_e}\big)$. Put $M = \lvert V\rvert$, choose weights $\eta, \kappa > 0$ with $\eta\lvert E\rvert + \kappa M \leq 1$, and

$$
\Gamma_{\mathcal{S}} := (1 - \eta\lvert E\rvert - \kappa M)\,\frac{\mathbb{1}}{7^M} + \eta \sum_{e = (v,w) \in E} \psi_{j_e}^{(v,w)} \otimes \frac{\mathbb{1}}{7^{M-2}} + \kappa \sum_{v \in V} \chi_{k_v}^{(v)} \otimes \frac{\mathbb{1}}{7^{M-1}},
$$

where $\psi_j = \lvert\psi_j\rangle\langle\psi_j\rvert$ acts on the ordered pair (source, target), $\lvert\psi_j\rangle \propto \lvert 01\rangle + \lvert 12\rangle + (2j+1)\lvert 23\rangle$, and $\chi_k = \lvert\chi_k\rangle\langle\chi_k\rvert$, $\lvert\chi_k\rangle \propto \lvert 3\rangle + \lvert 4\rangle + (k+1)\lvert 5\rangle$ (unit vectors). Then:

**(a) State.** $\Gamma_{\mathcal{S}} \in \mathcal{D}\big((\mathbb{C}^7)^{\otimes M}\big)$; it has full rank when $\eta\lvert E\rvert + \kappa M < 1$.

**(b) Local decoding.** For an ordered pair $v \neq w$ with two-body marginal $\rho_{vw}$, and a vertex $v$ with one-body marginal $\rho_v$:
$(v, w) \in E \iff \langle 01\rvert\rho_{vw}\lvert 12\rangle \neq 0$; then $2j_{(v,w)} + 1 = \langle 01\rvert\rho_{vw}\lvert 23\rangle / \langle 01\rvert\rho_{vw}\lvert 12\rangle$; and $k_v + 1 = \langle 3\rvert\rho_v\lvert 5\rangle / \langle 3\rvert\rho_v\lvert 4\rangle$.
Hence $\mathcal{S} \mapsto \Gamma_{\mathcal{S}}$ is injective, and the decoding does not use $\eta$, $\kappa$.

**(c) Restriction.** For $W \subset V$, the decoding of $\mathrm{Tr}_{V \setminus W}\,\Gamma_{\mathcal{S}}$ is the induced subnetwork $\mathcal{S}\vert_W$ (the edges with both ends in $W$, their spins, the labels on $W$). Encoding followed by decoding thus turns partial trace into restriction to induced subnetworks.

**(d) No state-preserving covariant functor.** For $M_1 < M_2$ and full-rank $\Gamma_{\mathcal{S}_2}$, no isometry $V: (\mathbb{C}^7)^{\otimes M_1} \to (\mathbb{C}^7)^{\otimes M_2}$ satisfies $V\,\Gamma_{\mathcal{S}_1} V^\dagger = \Gamma_{\mathcal{S}_2}$.

**(e) Group chain.** $SU(3) = \mathrm{Stab}_{G_2}(e_O)$ (T-42e) and the standard $SU(2) \subset SU(3)$ give, as complex representations, $\mathbf{7} \to \mathbf{1} \oplus \mathbf{3} \oplus \bar{\mathbf{3}} \to \mathbf{1} \oplus (\mathbf{2} \oplus \mathbf{1}) \oplus (\mathbf{2} \oplus \mathbf{1})$. (The split is of representations over $\mathbb{C}$, not a split of the seven coordinate axes; `check_core_numbers.py`, `test_no_axis_triple_is_su3_invariant`.)
:::

A graph with loops or multiple edges is encoded after subdividing each edge once (both halves carry $j_e$) and marking the subdivision vertices by $\lvert\chi\rangle \propto \lvert 3\rangle + \lvert 4\rangle$, whose ratio in (b) is $0$; then $M = \lvert V\rvert + \lvert E\rvert$.

### Lemma C29′. Local decoding [T] {#lemma-c29}

For the encoding of T-171(a)–(c), the two-site reduced matrix recovers edge presence and the spin label.

**Proof.** *(a)* $\psi_j$, $\chi_k$ and $\mathbb{1}/7^{m}$ are density matrices, and so are their tensor products; the coefficients $1 - \eta\lvert E\rvert - \kappa M$, $\eta$, $\kappa$ are non-negative and sum to 1 over the $1 + \lvert E\rvert + M$ summands, so $\Gamma_{\mathcal{S}}$ is a convex combination of states. If the first coefficient $c$ is positive, $\Gamma_{\mathcal{S}} \geq c\,\mathbb{1}/7^M > 0$.

*(b)* Every matrix element used is of the form $\langle ab\rvert X \otimes Y\lvert cd\rangle = \langle a\rvert X\lvert c\rangle\langle b\rvert Y\lvert d\rangle$ with $a \neq c$ and $b \neq d$ (two-body) or $\langle a\rvert X \lvert c\rangle$ with $a \neq c$ (one-body). Compute the contributions of each summand of $\Gamma_{\mathcal{S}}$ to $\rho_{vw}$:
- the identity term gives $\mathbb{1}/49$ — diagonal, contributes 0;
- $\psi_{j_e}$ for $e = (v, w)$ gives $\eta\,\psi_{j_e}$ itself: $\langle 01\rvert\psi_j\lvert 12\rangle = 1/n_j^2$ and $\langle 01\rvert\psi_j\lvert 23\rangle = (2j+1)/n_j^2$, $n_j^2 = 2 + (2j+1)^2$;
- $\psi$ on the reversed pair $(w, v)$ cannot occur (at most one edge between two vertices); in any case $\langle 10\rvert\psi\lvert 21\rangle = 0$, since $\lvert\psi\rangle$ has components only on $\lvert 01\rangle, \lvert 12\rangle, \lvert 23\rangle$;
- $\psi$ on an edge sharing one vertex with $\{v, w\}$ gives (one-body marginal of $\psi$) $\otimes\, \mathbb{1}/7$; both one-body marginals of $\lvert\psi_j\rangle$ are diagonal, because the three components have pairwise different first and pairwise different second factors — contributes 0;
- edges disjoint from $\{v, w\}$ give $\mathbb{1}/49$; vertex terms give $\chi \otimes \mathbb{1}/7$ or $\mathbb{1}/7 \otimes \chi$, whose second or first factor is diagonal — contribute 0.
So $\langle 01\rvert\rho_{vw}\lvert 12\rangle = \eta/n_j^2$ if $(v, w) \in E$ and $0$ otherwise, and the ratio is $2j + 1$. For $\rho_v$: edge terms give diagonal one-body marginals, the identity is diagonal, other vertices give $\mathbb{1}/7$; only $\kappa\chi_{k_v}$ contributes to $\langle 3\rvert\rho_v\lvert 4\rangle = \kappa/m_k^2$ and $\langle 3\rvert\rho_v\lvert 5\rangle = \kappa(k_v+1)/m_k^2$.

*(c)* The two- and one-body marginals of $\mathrm{Tr}_{V\setminus W}\Gamma_{\mathcal{S}}$ on $W$ are those of $\Gamma_{\mathcal{S}}$; by (b) they decode to the edges, spins and labels inside $W$. $\blacksquare$

### Proof of T-171

(a)–(c) are Lemma C29'. *(d)* $\mathrm{rank}\,(V\Gamma_{\mathcal{S}_1}V^\dagger) \leq 7^{M_1} < 7^{M_2} = \mathrm{rank}\,\Gamma_{\mathcal{S}_2}$. *(e)* $SU(3) = \mathrm{Stab}_{G_2}(e_O)$ is T-42e; the restriction of the 7-dimensional representation of $G_2$ to $SU(3)$ is $\mathbf{1} \oplus \mathbf{3} \oplus \bar{\mathbf{3}}$ after complexification (the real $\mathbf{6} = e_O^\perp$ becomes $\mathbb{C}^3$ with the complex structure $x \mapsto e_O x$), and $\mathbf{3}\vert_{SU(2)} = \mathbf{2} \oplus \mathbf{1}$ for the standard embedding. $\blacksquare$

Numerical check: `check_core_numbers.py`, `test_t171_spin_networks_with_unbounded_spin_are_decoded_from_ratios_of_coherences` — random directed graphs on 2 and 3 vertices with spins up to 20 and labels up to 5: $\Gamma_{\mathcal{S}}$ is a full-rank state, edges, directions, spins and labels are decoded exactly, and the partial trace over one vertex decodes to the induced subnetwork

### 2.3a Extension to unbounded spin {#t-171-prime-unbounded}

#### T-171′. Arbitrarily large spin labels [T]

:::tip Theorem T-171'
Every finite spin network with unbounded spins $j_e \in \tfrac12\mathbb{Z}_{\geq 0}$ is encoded injectively in a state of $M = \lvert V\rvert$ holons, with local decoding and restriction as in T-171 (a)–(c).
:::

**Proof.** T-171 (a)–(c) put no bound on $j_e$. $\blacksquare$

### 2.3 Fano amplitudes: finite ansatz and invariant tensors {#fano-spin-foam}

The finite incidence diagram can label an amplitude ansatz after spins, contractions and weights are specified. This is not an embedding theorem for spin-foam dynamics.

#### Theorem 2.3. Finite sums and invariant contractions {#теорема-2-3-fano-axioms}

A finite sum of finite amplitudes is finite. Gauge invariance and gluing require additional contraction data.

1. A Wigner $3j$ symbol is an invariant **tensor**, but summing its entries against a fixed vector of ones is not automatically an invariant contraction. Each internal index must have a declared representation and an invariant pairing/intertwiner. A finite scalar expression alone supplies no action on boundary states.
2. Gluing contracts matched boundary indices. Generally $\sum_m a_mb_m\ne(\sum_m a_m)(\sum_m b_m)$.
3. A rigid Fano frame supports a finite incidence symmetry. Gauge invariance requires the full tensor contraction to be invariant under the specified local action.
4. A Casimir on the irreducible fundamental $\mathbf7$ is $cI$. Thus $\prod_p\langle\psi_p|\mathcal C_{G_2}|\psi_p\rangle=c^7$ for normalized $\psi_p$ in that representation. This invariant is a constant and does not define a nontrivial spin-dependent weight or a map from $SU(2)$ spin labels to these vectors.

A valid replacement programme [Pr] chooses boundary representation spaces and intertwiners, contracts matching indices by invariant pairings, and defines gluing as that contraction. Under these choices invariance follows from invariance of the constituent tensors [T]; physical correspondence, convergence and any specific nontrivial weight remain additional claims. This retains ordinary representation mathematics without identifying arbitrary products of line labels with a quantum-gravity amplitude.

The tetrahedral Ponzano–Regge asymptotic applies to a $6j$ symbol with its nondegenerate large-spin hypotheses. A $3j$ tensor by itself specifies no Regge action.

### 2.4 Embedding Assessment

| Aspect | Status | Comment |
|--------|--------|---------|
| $SU(2) \subset SU(3) \subset G_2$ | **[T]** | T-171 (e): branching of representations over $\mathbb{C}$ |
| Graph, directions, spins, intertwiner labels in one state | **[T]** | T-171 (a)–(b): read from ratios of coherences, $M = \lvert V\rvert$ holons |
| Restriction to induced subnetworks = partial trace | **[T]** | T-171 (c) |
| Unbounded spin | [T] | The encoding allows every nonnegative half-integer. |
| State validity | [T] for the displayed encoding | Positivity and trace normalization are checked in T-171. |
| Physical area spectrum | Additional input | Recovering spin labels does not fix the LQG area observable. |
| Fano amplitudes (A1)–(A4) | **[✗] / [Pr]** | Finite sums retained; invariant contractions and gluing must be supplied (§2.3) |
| Fano amplitudes (semi-classical limit) | **[C]** | Fano-Regge compatibility — open problem |

---

## 3. Causal Sets {#каузальные-множества}

### 3.1 Mathematical Context

The theory of causal sets (Bombelli–Lee–Meyer–Sorkin, 1987) postulates:
- A discrete set of events $(C, \preceq)$ with a partial order;
- Causal structure is fundamental; metric and topology are derived;
- The number of elements of a causal set ↔ volume ($V \sim N$ — the Hauptvermutung);
- The d'Alembertian on a causal set → curvature in the continuum limit.

### 3.2 Embedding Construction {#causal-embedding}

#### T-172: Causal sets — encoding in holonic states and embedding as internal categories [T] {#t-172}

A finite partial order generally contains incomparable elements. A single time reading gives a total preorder, so it cannot encode the causal relation by chronological comparison alone. The construction below encodes each ordered pair directly.

:::tip T-172. Encoding a finite partial order [T]
Let $(C, \preceq)$ be a finite partially ordered set — any, no embedding into $M^4$ assumed; $M = \lvert C\rvert$, $N_\prec = \#\{(c, c') : c \prec c'\}$.

**(a) Encoding.** For $\eta \in (0, 1/N_\prec]$ put

$$
\Gamma_C := (1 - \eta N_\prec)\,\frac{\mathbb{1}}{7^M} + \eta \sum_{c \prec c'} \psi^{(c,c')} \otimes \frac{\mathbb{1}}{7^{M-2}}, \qquad \lvert\psi\rangle = \tfrac{1}{\sqrt2}\big(\lvert 01\rangle + \lvert 12\rangle\big) \text{ on the ordered pair } (c, c').
$$

Then $\Gamma_C \in \mathcal{D}\big((\mathbb{C}^7)^{\otimes M}\big)$, and for $c \neq c'$ with two-body marginal $\rho_{cc'}$: $c \prec c' \iff \langle 01\rvert\rho_{cc'}\lvert 12\rangle \neq 0$ (the value is then $\eta/2$). For $D \subset C$, the decoding of $\mathrm{Tr}_{C \setminus D}\,\Gamma_C$ is the induced order on $D$.

**(b) Internal categories.** Let $X = \mathcal{D}(\mathbb{C}^7)$ with the topology of the Bures metric, $\mathcal{E} = \mathbf{Sh}_\infty(X)$ and $\pi^*: \mathcal{S} \to \mathcal{E}$ the constant-sheaf functor. The functor

$$
\mathbf{Poset}_{\text{fin}} \to \mathrm{Fun}(\Delta^{\mathrm{op}}, \mathcal{E}), \qquad C \mapsto \pi^* N_\bullet(C)
$$

(levelwise constant sheaf on the finite sets of $n$-chains $c_0 \preceq \dots \preceq c_n$) is fully faithful: each mapping space $\mathrm{Map}(\pi^*N_\bullet C, \pi^*N_\bullet C')$ is discrete and equals the set of order-preserving maps $C \to C'$. Its values are Segal objects (internal categories) of $\mathcal{E}$.

**(c) The realisation forgets the order.** $C \mapsto \pi^*\lvert N_\bullet(C)\rvert \in \mathcal{E}$ is neither faithful nor injective on isomorphism classes.

**(d) Clock labels.** The rank $\tau_c$ of $c$ in a linear extension of $\preceq$ is strictly monotone ($c \prec c' \Rightarrow \tau_c < \tau_{c'}$) and takes $M$ values, which the $6M + 1$ readings of the summed clock of $M$ holons accommodate ([composite clocks](/docs/proofs/dynamics/emergent-time#композитные-часы)). (a) does not need them.
:::

If two space-like separated events have different time coordinates, chronological order alone does not make them causally related. A faithful spacetime embedding would require additional spacetime data.

### Lemma C30. Decoding the order [T] {#lemma-c30}

**Statement.** The two-site readout in T-172(a) decodes the incidence relation of any supplied finite partial order.

**Proof.** $\psi$ and $\mathbb{1}/7^m$ are states and the coefficients are non-negative with sum 1, so $\Gamma_C$ is a state. For the marginal $\rho_{cc'}$, the matrix element $\langle 01\rvert X \otimes Y \lvert 12\rangle = \langle 0\rvert X\lvert 1\rangle\langle 1\rvert Y\lvert 2\rangle$ vanishes whenever $X$ or $Y$ is diagonal. The summand for the pair $(c, c')$ itself gives $\eta\,\langle 01\rvert\psi\rangle\langle\psi\lvert 12\rangle = \eta/2$. The summand for the reversed pair $(c', c)$, read in the order $(c, c')$, gives $\eta\,\langle 10\rvert\psi\rangle\langle\psi\lvert 21\rangle = 0$ (and it is absent anyway, by antisymmetry of $\prec$). A summand for a pair sharing one element with $\{c, c'\}$ gives a one-body marginal of $\psi$ tensored with $\mathbb{1}/7$; the one-body marginals $\tfrac12(\lvert 0\rangle\langle 0\rvert + \lvert 1\rangle\langle 1\rvert)$ and $\tfrac12(\lvert 1\rangle\langle 1\rvert + \lvert 2\rangle\langle 2\rvert)$ are diagonal. All other summands give $\mathbb{1}/49$. Hence $\langle 01\rvert\rho_{cc'}\lvert 12\rangle = \eta/2$ if $c \prec c'$ and $0$ otherwise. Marginals of $\mathrm{Tr}_{C\setminus D}\Gamma_C$ on $D$ are those of $\Gamma_C$. $\blacksquare$

### Proof of T-172

*(a)* is Lemma C30.

*(b)* The nerve $N: \mathbf{Cat} \to \mathbf{sSet}$ is fully faithful, so order-preserving maps $C \to C'$ are exactly the simplicial maps $N_\bullet C \to N_\bullet C'$. $X$ is connected (a convex subset of the Hermitian matrices, hence path-connected). For finite sets $A, B$: $\mathrm{Map}_{\mathcal{E}}(\pi^*A, \pi^*B) \simeq \mathrm{Map}_{\mathcal{S}}(A, \pi_*\pi^*B)$, and $\pi_*\pi^*B$ is the set of locally constant functions $X \to B$ — which, $X$ being connected, is $B$. So $\pi^*$ is fully faithful on finite sets, with discrete mapping spaces. A map of simplicial objects between levelwise images $\pi^*A_\bullet \to \pi^*B_\bullet$ is computed by the end $\int_{[n]}\mathrm{Map}_{\mathcal{E}}(\pi^*A_n, \pi^*B_n) = \int_{[n]}\mathrm{Hom}(A_n, B_n) = \mathrm{Hom}_{\mathbf{sSet}}(A_\bullet, B_\bullet)$. The Segal maps $N_n C \to N_1 C \times_{N_0 C} \dots \times_{N_0 C} N_1 C$ are bijections, and $\pi^*$ preserves finite limits, so $\pi^*N_\bullet C$ satisfies the Segal condition.

*(c)* A poset with a least element $\bot$ has a contractible realisation (the nerve is a cone with apex $\bot$). So the one-element poset $\{\ast\}$ and the chain $\{0 \prec 1\}$ both go to the terminal object $1 \in \mathcal{E}$, and the two order-preserving maps $\{\ast\} \to \{0 \prec 1\}$ go to the one map $1 \to 1$: not faithful. The chains of $C$ and of $C^{\mathrm{op}}$ are the same subsets, so $\lvert N_\bullet C\rvert \cong \lvert N_\bullet C^{\mathrm{op}}\rvert$; the poset $\{\bot \prec a, \bot \prec b\}$ and its opposite are not isomorphic and have the same image, and so do the chains of one and of two elements (both go to $1$): not injective on isomorphism classes.

*(d)* Every finite poset has a linear extension (Szpilrajn); its rank function is strictly monotone. $\blacksquare$

Numerical check: `check_core_numbers.py`, `test_t172_every_finite_poset_is_encoded_and_realisation_forgets_order` — random posets on 2–4 elements: $\Gamma_C$ is a state, the order is decoded exactly, and the partial trace over one element decodes to the induced order; the old $W_{cc'}$ with random antisymmetric phases has a negative eigenvalue; the order complex of a chain of 1–4 elements has Euler characteristic 1, and a random poset and its opposite have the same chains.

**Status:** [T]. Uses: nerves of categories (Mac Lane 1998); the global-sections geometric morphism $\pi: \mathcal{E} \to \mathcal{S}$ (HTT Prop. 6.3.4.1) and constant sheaves on a connected space; Szpilrajn's extension theorem; [composite clocks](/docs/proofs/dynamics/emergent-time#композитные-часы) (only for (d)). Removed: HTT 6.1.3.8 (misquoted), T-38b as a clock construction (only the reading count is used), T-117–T-120 (the continuum remark is not part of the theorem).

### 3.3 Embedding Assessment

| Aspect | Status | Comment |
|--------|--------|---------|
| Order of any finite poset in one state | **[T]** | T-172 (a): read from $\langle 01\rvert\rho_{cc'}\lvert 12\rangle$; no $M^4$-embedding needed |
| Posets as internal categories of $\mathbf{Sh}_\infty(\mathcal{C})$ | **[T]** | T-172 (b): fully faithful, because $\mathcal{D}(\mathbb{C}^7)$ is connected |
| Nerve realised as an object of the ∞-topos | **[✗]** as an embedding | T-172 (c): contractible for any poset with a least element |
| Discrete time structure | **[T]** | $6M+1$ readings of the summed clock (T-38b [T] per holon); linear-extension ranks fit (T-172 (d)) |
| Continuum limit → $M^4$ | not part of T-172 | T-118, T-119, T-120 are separate theorems |

---

## 4. Universal Property of the UHM ∞-Topos {#универсальное-свойство}

### 4.1 Mathematical Context

The category and the directions of its morphisms determine the universal property one can test.

Key references:
- **Schreiber (2013, 1310.7930):** Differential cohomology in a cohesive ∞-topos. Gauge fields, QFT, BV-BRST formalism — all within cohesive ∞-toposes.
- **Baez (1995, q-alg/9503002):** Higher algebra and topological QFT. Extended TQFTs as functors from nCob.
- **Lurie (2009):** Classification of extended TQFTs: fully dualizable objects.

### 4.2 Category of Physical Theories {#категория-phys}

**Definition (Category $\mathbf{PhysTheory}$).** $\mathbf{PhysTheory}$ is the ∞-category of [T-211](/docs/proofs/categorical/fundamental-closures#t-211): the cartesian unstraightening over $\mathbf{Topoi}_\infty$ of $E \mapsto \mathrm{Dyn}(E) = \mathrm{Fun}(B\mathbb{R}, \mathrm{Alg}(E))$. Objects are triples $(E, \mathcal{A}, D)$:
- $E$ — an ∞-topos;
- $\mathcal{A}$ — an associative algebra (monoid) object of $E$ for its cartesian structure;
- $D$ — an action of the group $\mathbb{R}$ on $\mathcal{A}$ by algebra automorphisms.

A morphism $(E_1, \mathcal{A}_1, D_1) \to (E_2, \mathcal{A}_2, D_2)$ is a triple $(f, \alpha, \beta)$:
- $f: E_1 \to E_2$ — a geometric morphism, with inverse image $f^*: E_2 \to E_1$;
- $\alpha: \mathcal{A}_1 \to f^*\mathcal{A}_2$ — a map of algebra objects in $E_1$;
- $\beta$ — the coherent family of homotopies $\beta_t: \alpha \circ D_1(t) \simeq f^*D_2(t) \circ \alpha$, $t \in \mathbb{R}$ (T-211 (b)).

A morphism includes a geometric inverse-image functor and a map of algebras over the same base, together with compatibility with the specified dynamics.

### 4.3 Scope of primitive uniqueness {#теорема-единственности-мета}

#### T-173. Data specifying a primitive {#t-173}

A structured physical theory requires a site, observation algebra and dynamics. Distinct monotone quantum metrics and generators can be specified on the same finite state space.

Dimension seven requires the explicit premises of the [minimality theorem](/docs/proofs/minimality/theorem-minimality-7). A positive octonionic form has stabilizer $G_2$, but this codomain symmetry does not identify physical encoders.

For the given dimension $N$ and open-cover site, the associated sheaf topos is determined up to equivalence. Physical dynamics and its observable interpretation remain separate inputs.

### 4.4 Universal Property: Receiving Map {#приёмное-отображение}

#### T-174: Universal property of the UHM kinematic object [T] {#t-174}

**Setting.** Consider the fibre of $\mathbf{PhysTheory}$ over the terminal ∞-topos $\mathcal{S}$ (theories over a point). Its subcategory $\mathbf{PhysTheory}^{C^*}_{\mathrm{pt}}$ has as objects $x = (\mathcal{S}, A, \sigma)$ with $A$ a unital $C^*$-algebra (entering T-211 through its multiplicative monoid) and $\sigma: \mathbb{R} \to \mathrm{Aut}(A)$ a group of $*$-automorphisms, and as morphisms $(\mathrm{id}, \alpha, \beta)$ with $\alpha$ a unital $*$-homomorphism; identities and composites of such are such, so this is a (non-full) subcategory. Because the objects are 0-truncated, the fibre of T-211 (b) is a set: $\beta$ exists iff $\alpha \circ \sigma_1(t) = \sigma_2(t) \circ \alpha$ for all $t$, and is then unique — compatibility with dynamics is a property, not data. Put

$$
u_0 := (\mathcal{S}, A_{\text{int}}, \mathrm{id}), \qquad x_n := (\mathcal{S}, M_n(\mathbb{C}), \mathrm{id}), \qquad A^\sigma := \{a \in A : \sigma_t(a) = a \ \forall t\}.
$$

:::tip T-174. Corepresentation and conditional expectation [T]
**(a) Corepresentation.** For every object $x = (\mathcal{S}, A, \sigma)$, morphisms $u_0 \to x$ are in bijection with the $A_{\text{int}}$-structures in $A^\sigma$: families $\big(p;\ (e_{ij})_{i,j=1}^3;\ (f_{ij})_{i,j=1}^3\big)$ in $A^\sigma$ with $p = p^* = p^2$, $e_{ij}^* = e_{ji}$, $e_{ij}e_{kl} = \delta_{jk}e_{il}$, the same for $f$, all products between $p$, $e$, $f$ equal to zero, and $p + \sum_i e_{ii} + \sum_i f_{ii} = 1$. The morphism is faithful (injective $\alpha$) iff $p$, $e_{11}$, $f_{11}$ are all non-zero.

**(b) Classification and rigidity at 7.** Up to conjugation by $U(n)$, morphisms $u_0 \to x_n$ correspond to triples $(a, b, c) \in \mathbb{Z}_{\geq 0}^3$ with $a + 3b + 3c = n$ (the multiplicities of the three summands). Faithful morphisms exist iff $n \geq 7$; they form exactly one conjugacy class iff $n \in \{7, 8, 9\}$ (for $n = 10$: three). The **multiplicity-free** faithful morphism ($a = b = c = 1$; commutant $\cong \mathbb{C}^3$, abelian) exists iff $n = 7$. For $n = 7$ the faithful morphisms $u_0 \to x_7$ form one $U(7)$-orbit, $U(7)/U(1)^3$, of real dimension 46.

**(c) Dynamics.** For $x = (\mathcal{S}, M_n(\mathbb{C}), \mathrm{Ad}\,e^{itH})$, $A^\sigma = \{H\}'$, and a faithful morphism $u_0 \to x$ exists iff the eigenspace dimensions $m_1, \dots, m_r$ of $H$ admit decompositions $m_i = a_i + 3b_i + 3c_i$ with $\sum_i a_i, \sum_i b_i, \sum_i c_i \geq 1$. For $n = 7$ the multiplicity-free morphism $\alpha_0$ (sector projections $P_0, P_1, P_2$ of ranks 1, 3, 3) is a morphism into $x$ iff $H \in \mathrm{span}(P_0, P_1, P_2)$; if $H$ has simple spectrum there is no faithful morphism at all. In the extension of the fibre to semigroups of unital completely positive maps (the group $B\mathbb{R}$ replaced by the monoid $\mathbb{R}_{\geq 0}$ — outside T-211 as stated), for a primitive semigroup $T$ on $M_n(\mathbb{C})$ the only morphism $u_0 \to (M_n(\mathbb{C}), T)$ is $\lambda \oplus A \oplus B \mapsto \lambda\,1$, which is not faithful. In particular a primitive linear part of the UHM Liouvillian (T-39a) fixes no faithful $A_{\text{int}}$-structure.

**(d) The receiving map on states.** Let $\alpha: u_0 \to x$ be faithful, $A$ finite-dimensional and $\tau$ a faithful tracial state on $A$. There is exactly one unital completely positive map $E: A \to A_{\text{int}}$ with $E \circ \alpha = \mathrm{id}$ and $\tau \circ \alpha \circ E = \tau$ — the $\tau$-preserving conditional expectation onto $\alpha(A_{\text{int}})$. If $\sigma_t$ preserves $\tau$ and $\alpha(A_{\text{int}})$ as a set, then $E \circ \sigma_t = (\alpha^{-1}\sigma_t\alpha) \circ E$. For $A = M_n(\mathbb{C})$, $E$ is never a homomorphism. For $n = 7$, $\alpha_0$ and $\tau = \mathrm{tr}/7$: $E(a) = (a_{00},\ P_1 a P_1,\ P_2 a P_2)$, and the induced map on states, $\rho \mapsto \rho \circ \alpha_0$, is the sector pinching $\rho \mapsto (\rho_{00}, P_1\rho P_1, P_2\rho P_2)$.

**(e) Receiving morphisms.** Receiving morphisms $x \to \text{UHM}$ in $\mathbf{PhysTheory}$ do not have the universal property: none exists for $x = x_7$ with $\alpha$ a $*$-homomorphism, and infinitely many pairwise inequivalent ones exist with $\alpha$ a monoid map. The universal property is carried by $u_0$ and goes in the opposite direction, (a)–(c).
:::

**Proof.**

*(a)* $A_{\text{int}}$ is the universal $C^*$-algebra on the generators $p, e_{ij}, f_{ij}$ with the stated relations: the relations say that $p$, $\sum e_{ii}$, $\sum f_{ii}$ are orthogonal projections with sum 1 and that $(e_{ij})$, $(f_{ij})$ are systems of $3 \times 3$ matrix units in the corners they cut out; the $*$-algebra they span has dimension at most $1 + 9 + 9 = 19$, and it maps onto $A_{\text{int}}$ (where the standard matrix units satisfy the relations), so it is $A_{\text{int}}$. Given such a family in $A^\sigma$, $\alpha(\lambda, (a_{ij}), (b_{ij})) := \lambda p + \sum a_{ij}e_{ij} + \sum b_{ij}f_{ij}$ is a unital $*$-homomorphism; since $u_0$ has trivial dynamics, the compatibility $\alpha = \sigma_t \circ \alpha$ says exactly that the image lies in $A^\sigma$. Conversely the images of the standard generators under a morphism form such a family. The ideals of $A_{\text{int}}$ are sums of its three summands, and $\alpha$ kills a summand iff it kills its unit $p$, $\sum e_{ii}$ or $\sum f_{ii}$ — equivalently $p$, $e_{11}$ or $f_{11}$ (as $e_{ii} = e_{i1}e_{11}e_{1i}$).

*(b)* A unital $*$-representation of $A_{\text{int}}$ on $\mathbb{C}^n$ is a direct sum of irreducibles — $\mathbb{C}$ (through the first summand), $\mathbb{C}^3$ (through the first $M_3$), $\mathbb{C}^3$ (through the second) — with multiplicities $(a, b, c)$, $a + 3b + 3c = n$; two are unitarily equivalent iff their multiplicities agree (semisimplicity). Faithful means $a, b, c \geq 1$, so $n \geq 7$. Faithful classes: $n = 7$: $(1,1,1)$; $n = 8$: $(2,1,1)$; $n = 9$: $(3,1,1)$; for $n \geq 10$ at least $(n-6,1,1)$, $(n-9,2,1)$, $(n-9,1,2)$. The commutant of the class $(a, b, c)$ is $M_a \oplus M_b \oplus M_c$, abelian iff $a, b, c \leq 1$; with faithfulness this forces $a = b = c = 1$, $n = 7$. The stabiliser of $\alpha_0$ under conjugation is the unitary group of the commutant, $U(1)^3$, so the orbit is $U(7)/U(1)^3$, of dimension $49 - 3 = 46$.

*(c)* The fixed-point algebra of $\{\mathrm{Ad}\,e^{itH}\}_{t \in \mathbb{R}}$ is the commutant $\{H\}' = \bigoplus_i M_{m_i}(\mathbb{C})$ over the eigenspaces. A unital $*$-homomorphism into it is a family of unital representations of $A_{\text{int}}$ on the eigenspaces, one per block, with multiplicities $(a_i, b_i, c_i)$; it is faithful iff each summand of $A_{\text{int}}$ appears in some block. For $\alpha_0$: $\alpha_0(A_{\text{int}}) \subset \{H\}'$ iff $H \in \alpha_0(A_{\text{int}})' = \mathrm{span}(P_0, P_1, P_2)$. Simple spectrum: $\{H\}'$ is abelian, and $M_3(\mathbb{C})$ has no non-zero $*$-homomorphism into an abelian algebra (its irreducible representations are 3-dimensional). For a primitive semigroup $T_t = e^{t\mathcal{L}^\dagger}$ on $M_n(\mathbb{C})$: primitivity means $\dim\ker\mathcal{L} = 1$ with a faithful stationary state; in finite dimensions $\dim\ker\mathcal{L}^\dagger = \dim\ker\mathcal{L} = 1$, and $\mathcal{L}^\dagger(1) = 0$ (unitality), so the fixed points are $\mathbb{C}1$. A morphism has image in the fixed points, so it is a character of $A_{\text{int}}$ times $1$; the only character is $\lambda \oplus A \oplus B \mapsto \lambda$ (the $M_3$ summands have no characters).

*(d)* On the finite-dimensional Hilbert space $L^2(A, \tau)$ let $E$ be the orthogonal projection onto $\alpha(A_{\text{int}})$, composed with $\alpha^{-1}$. It is the $\tau$-preserving conditional expectation (Umegaki 1954; Takesaki 1972 — the modular group of a trace is trivial, so the invariance condition holds), in particular unital completely positive with $E \circ \alpha = \mathrm{id}$. Uniqueness: if $E'$ is unital completely positive with $E' \circ \alpha = \mathrm{id}$, then $\alpha \circ E'$ is a projection of norm one onto $\alpha(A_{\text{int}})$, hence a conditional expectation (Tomiyama 1957), in particular $\alpha(A_{\text{int}})$-bimodular; if also $\tau \circ \alpha \circ E' = \tau$, then $\tau\big(\alpha(E'(a))\,\alpha(b)\big) = \tau\big(\alpha(E'(a\,\alpha(b)))\big) = \tau(a\,\alpha(b))$ for all $b \in A_{\text{int}}$, which is the defining property of $E$, so $E' = E$. Equivariance: for $b \in A_{\text{int}}$, $\tau(\alpha E(\sigma_t a)\,\alpha(b)) = \tau(\sigma_t(a)\,\alpha(b)) = \tau(a\,\sigma_{-t}\alpha(b)) = \tau(\alpha E(a)\,\sigma_{-t}\alpha(b)) = \tau(\sigma_t\alpha E(a)\,\alpha(b))$, using $\tau \circ \sigma_t = \tau$ and $\sigma_{-t}\alpha(b) \in \alpha(A_{\text{int}})$. Not a homomorphism for $A = M_n(\mathbb{C})$: a multiplicative $E$ has a two-sided ideal as kernel; $M_n(\mathbb{C})$ is simple and $E \neq 0$, so $E$ would be injective, $n^2 \leq 19$, contradicting $n \geq 7$. The formula for $n = 7$ satisfies $E \circ \alpha_0 = \mathrm{id}$ and $\mathrm{tr}(E(a)\,b) = \mathrm{tr}(a\,b)$ for block-diagonal $b$; by uniqueness it is $E$. The dual map on states is restriction along $\alpha_0$, which reads off the three diagonal blocks.

*(e)* A $*$-homomorphism $M_7(\mathbb{C}) \to A_{\text{int}}$ followed by the projection onto a summand $M_m$ ($m \in \{1, 3\}$) is a $*$-homomorphism $M_7(\mathbb{C}) \to M_m(\mathbb{C})$, which is zero because a non-zero one is a multiple of the 7-dimensional irreducible representation and $7 > m$; so the only $*$-homomorphism is $0$, which is not unital. Monoid maps: $a \mapsto \det(a)^k\,1$ is unital and multiplicative. If a monoid automorphism $\psi$ of $(A_{\text{int}}, \cdot)$ carried $\det^k 1$ to $\det^m 1$ with $k \neq m$, then $\psi(z^k 1) = z^m 1$ for all $z \in \mathbb{C}$ (take $a = \mathrm{diag}(z, 1, \dots, 1)$); for $k = 0$ this is false at $z = 0$; for $k, m \geq 1$, a primitive root of unity of order $k$ gives $z^m = 1$, so $k \mid m$, symmetrically ($\psi^{-1}$) $m \mid k$, so $k = m$. $\blacksquare$

Numerical check: `check_core_numbers.py`, `test_t174_a_int_corepresents_structures_and_the_old_receiving_map_fails` — the commutant of $\alpha_0(A_{\text{int}})$ in $M_7(\mathbb{C})$ has dimension 3; the numbers of faithful classes for $n = 1, \dots, 12$ are $0,0,0,0,0,0,1,1,1,3,3,3$, and $(1,1,1)$ occurs only at $n = 7$; $E$ is completely positive (Choi matrix $\geq 0$), keeps the trace against $A_{\text{int}}$, satisfies $E \circ \alpha_0 = \mathrm{id}$ and has a multiplicativity defect $> 1$ on random matrices; a random primitive Lindbladian on $\mathbb{C}^7$ has one stationary state and Heisenberg fixed points $\mathbb{C}1$; $H$ with simple spectrum commutes with none of the 12 off-diagonal matrix units, $H \in \mathrm{span}(P_0, P_1, P_2)$ commutes with all 19 generators; the $G_2$-orbit of a random state has dimension 14 in the 48-dimensional $\mathcal{D}(\mathbb{C}^7)$.

**Inputs for T-174.** The mapping spaces in T-211 specify the morphisms. The representation calculation uses finite-dimensional $C^*$-algebras. The state map uses the trace-preserving conditional expectation.

### 4.5 Embedding Diagram {#схема-вложений}

```
     u0 = (A_int, trivial dynamics)  -- corepresents A_int-structures (T-174 a) --
        |                    |                       |
        | *-hom into A^sigma | unique up to U(7)     | E: tau-preserving expectation
        v                    v   iff n = 7, 8, 9     v   (UCP, not a *-hom; T-174 d)
   any theory x       M_n(C), n >= 7          states of x --> states of A_int

   spin networks (all j)  --Gamma_S-->  states of |V| heptads   [T-171]
   finite posets          --Gamma_C-->  states of |C| heptads   [T-172 a]
   finite posets          --pi* N-->    Segal objects of Sh(D(C^7)), fully faithful [T-172 b]
   M-theory on G2         :  Stab(phi_0) = Aut(O) = G2 [T-170 i];  Z_UHM = Z_M  [H]
```

---

## 5. Summary Table {#сводная-таблица}

| Theory | Map | Key mechanism | Status | Conditions |
|--------|-----|---------------|--------|------------|
| **M-theory** | Group comparison | $\mathrm{Stab}_{GL(7)}(\varphi_0)=G_2$ | [T] for the specified form | Matching partition functions is [H]. |
| **LQG** (all finite spin networks) | $\mathcal{S} \mapsto \Gamma_{\mathcal{S}}$, $M = \lvert V\rvert$ | spins and labels as ratios of coherences | **[T]** | — (T-171, T-171') |
| **Causal sets** (all finite posets) | $C \mapsto \Gamma_C$; $C \mapsto \pi^*N_\bullet C$ | ordered pair state; connectedness of $\mathcal{D}(\mathbb{C}^7)$ | **[T]** | — (T-172) |
| **Universal property** | $u_0 = (A_{\text{int}}, \mathrm{id})$ corepresents $A_{\text{int}}$-structures | universal $C^*$-algebra; multiplicity-free only at $n = 7$ | **[T]** | Conditions in T-174 |

### 5.1 Honest Assessment


What is **proven [T]**:
1. $\mathrm{Stab}_{GL(7)}(\varphi_0) = \mathrm{Aut}(\mathbb{O}) = G_2$, the holonomy group of torsion-free $G_2$-structures (T-170 (i));
2. The chain $SU(2) \subset SU(3) \subset G_2$ with $\mathbf{7} \to \mathbf{1} \oplus \mathbf{3} \oplus \bar{\mathbf{3}}$ over $\mathbb{C}$ (T-171 (e));
3. Injective, locally decodable encodings of finite spin networks and finite posets in holonic states (T-171, T-172);
4. $u_0$ corepresents $A_{\text{int}}$-structures; the multiplicity-free faithful one exists only on $\mathbb{C}^7$ and is unique there up to $U(7)$ (T-174).

What is **not proven**:
1. $Z_{\text{UHM}} = Z_M$ at any level (T-170 (iv) [H]);
2. The specific form of Fano spin foam amplitudes and their semi-classical limit;
3. A universal property *into* UHM from every theory of a class — false as stated (T-174 (e)).

---

## 6. Results Registration {#регистрация}

| Theorem | Statement | Status | Conditions |
|---------|-----------|--------|------------|
| **T-170** | Group identity, finite partition integral, limit states | [T] for specified models | Physical partition-function correspondence [H] |
| **T-171** | Encoding finite spin networks | [T] | Supplied graph, labels and readout |
| **T-171′** | Unbounded spin labels | [T] | Local decoding of the specified encoding |
| **T-172** | Finite poset encoding and internal category | [T] | Supplied order and readout |
| **T-173** | Topos for the specified site | [T] under the site data | Physical dynamics require further assumptions |
| **T-174** | Corepresentation, multiplicity, dynamics criterion and expectation | [T] | As in the theorem |
| **C27-M** | Continuous Gap limit | [P] | Part of the hypothesis T-170 (iv) |
| **C28-M** | Supersymmetric extension | [P] | Part of the hypothesis T-170 (iv) |
| **C29'** | Spatial encoding (all finite spin networks) | [T] | Lemma C29' = T-171 (a)–(c) |
| **C29** | Spatial limit for unbounded spin networks | [T] | Closed by T-171 (no bound on $j_e$) |
| **C30** | Causal encoding (all finite posets, no $M^4$-embedding) | [T] | Lemma C30 = T-172 (a) |

---

## Links

- **Relies on:** [Spectral triple (T-53)](/docs/proofs/physics/physics-correspondence), [Emergent $M^4$ (T-117–T-121)](/docs/proofs/physics/emergent-manifold), [specified octonionic symmetry and conditional RI](/docs/proofs/categorical/uniqueness-theorem), [SUSY from $G_2$](/docs/physics/particle-physics/susy), [Gap functional integral](/docs/physics/gravity/quantum-gravity), [Sector decomposition](/docs/physics/gauge-symmetry/standard-model)
- **Justifies:** Meta-ToE status of UHM
- **Status registry:** T-170 — T-174, C27-M — C30 ([Registry](/docs/reference/status-registry))
