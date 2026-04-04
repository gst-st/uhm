---
sidebar_position: 3
title: "Embeddings of Alternative ToEs"
slug: /proofs/physics/toe-embeddings
description: "Formal embeddings of M-theory, loop quantum gravity, and causal sets into UHM. Universal property of the ∞-topos."
---

# Embeddings of Alternative Candidate Theories into UHM

:::info Status
To substantiate the Meta-ToE status, it is necessary to show that competing approaches to quantum gravity are recovered as limits or special cases of UHM. This document contains four constructions with varying levels of rigor: from [Т] (standard mathematics) to [Г] (requires additional justification).
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

#### T-170: Recovery of the M-Theoretic Limit [С при C27, C28] {#t-170}

:::tip Theorem T-170
Under the following conditions:

**(C27)** (Continuous Gap limit): the limit $a \to 0$ of the lattice of Gap fields $\theta_{ij}(x)$ exists, in which the $\sigma$-model on $(S^1)^{21}/G_2$ defines a smooth 7-dimensional target space $\mathcal{M}_7$;

**(C28)** (Supersymmetric extension): the SUSY extension of the Gap integral ([SUSY from $G_2$](/docs/physics/particle-physics/susy)) is a well-defined quantum supersymmetric functional integral;

the UHM Gap functional integral:

$$
Z_{\text{UHM}} = \int_{(S^1)^{21}} \mathcal{D}[\theta]\, \mathcal{D}[\tilde{\theta}]\, e^{-S_{\text{Gap}}[\theta, \tilde{\theta}]}
$$

recovers the M-theoretic partition function on a $G_2$-manifold:

$$
Z_{\text{M}} = \int_{\mathcal{M}_7} \mathcal{D}[C_3]\, \mathcal{D}[g]\, e^{-S_{11D}[g, C_3]}
$$

via the identification:

**(a)** Target space: $(S^1)^{21}/G_2$ (7-dimensional orbifold) is identified with the moduli of the $G_2$-metric on $\mathcal{M}_7$;

**(b)** Gap phases: 21 phases $\theta_{ij}$ ↔ deformations of the associative 3-form $\varphi \in \Omega^3(\mathcal{M}_7)$ parametrizing the $G_2$-structure. The dimension of the deformation space = $b_3(\mathcal{M}_7)$, and for $b_3 = 21$ the correspondence is bijective;

**(c)** Gauge symmetry: $G_2 = \mathrm{Aut}(\mathbb{O})$ in UHM ↔ holonomy group $\mathrm{Hol}(\mathcal{M}_7) = G_2$. Both define the same exceptional structure;

**(d)** Superpartners: Gap superpartners $\tilde{\theta}_{ij}$ ↔ fermionic moduli of the $G_2$-manifold (covariantly constant spinor $\eta_0 = 1_{\mathbb{O}}$).
:::

**Proof sketch.**

**Step 1 (Dimensional correspondence).** M-theory: 11D = 4D ($M^4$) + 7D ($\mathcal{M}_7$). UHM: $M^4$ is derived (T-120 [Т]), and the 7D internal space is parametrized by $\mathcal{D}(\mathbb{C}^7)$. The spectral triple $(A_{\text{int}}, H_{\text{int}}, D_{\text{int}})$ with KO-dim = 6 (T-53 [Т]) upon supersymmetric extension gives KO-dim = 6 + 1 = 7 (standard $\mathbb{Z}_8$-shift).

**Step 2 (Gap moduli = $G_2$ moduli).** The physical configuration space of UHM:

$$
\mathcal{M}_{\text{phys}} = (S^1)^{21}/G_2, \quad \dim = 21 - 14 = 7
$$

The M-theoretic moduli of a $G_2$-manifold are parametrized by harmonic 3-forms: $\dim(\mathcal{M}_{G_2}) = b_3(\mathcal{M}_7)$. For a compact $G_2$-manifold with $b_3 = 21$ (e.g., Joyce's $G_2$-resolution $T^7/\Gamma$) the dimensions coincide.

**Step 3 (Action).** The Connes–Chamseddine spectral action:

$$
S_{\text{spec}} = \mathrm{Tr}(f(D/\Lambda))
$$

for the spectral triple $(C^\infty(M^4) \otimes A_{\text{int}},\, H,\, D)$ reproduces (T-65 [Т]):

$$
S_{\text{spec}} = \int_{M^4} \left[ a_0 \Lambda^4 + a_2 \Lambda^2 R + a_4 (\alpha R^2 + \beta |F|^2 + \gamma |\nabla\phi|^2 + \ldots) \right]
$$

The coefficients $a_k$ are determined by the internal triple. The Gap variables $\theta_{ij}$ upon minimization of $V_{\text{Gap}}$ (T-64 [Т]) fix the vacuum, analogous to the moduli fixing of the $G_2$-manifold in M-theory.

**Step 4 (SUSY breaking).** The SUSY breaking mechanism via $V_3 \neq 0$ ([SUSY](/docs/physics/particle-physics/susy#нарушение-susy)) ↔ non-Fano associator (28 out of 35 triples). In M-theory, analogous SUSY breaking via 4-form flux $G_4 \neq 0$ (Acharya–Kane, 2006): $\langle G_4 \rangle \neq 0$ on non-associative 4-cycles ↔ $V_3 \neq 0$ from non-Fano triples.

### 1.3 Formal Functor {#функтор-m-theory}

**Definition (M-theory recovery functor).**

$$
\mathcal{F}_M: \mathbf{Hol}_{\text{comp}} \to \mathbf{G_2\text{-}Mfld}
$$

On objects: a composite system of $M$ holons $\mapsto$ $G_2$-manifold $\mathcal{M}_7(M)$, the Gelfand spectrum of the algebra $A_{\text{int}}^{\otimes M}/G_2$.

On morphisms: a CPTP channel $\Phi: \Gamma_1 \to \Gamma_2$ $\mapsto$ a diffeomorphism $f: \mathcal{M}_7 \to \mathcal{M}_7$ preserving the $G_2$-structure (when $\Phi \in G_2$-sector).

**Functor status:** [Г]. For a full proof of functoriality one needs:
- A proof of smoothness of the limit $(S^1)^{21N}/G_2^N \to \mathcal{M}_7$ as $N \to \infty$ (C27);
- Control of the SUSY extension at the quantum level (C28).

### 1.4 Embedding Assessment

| Aspect | Status | Comment |
|--------|--------|---------|
| $G_2$-symmetry coincides | **[Т]** | Identical group: $\mathrm{Aut}(\mathbb{O}) = \mathrm{Hol}(\mathcal{M}_7)$ |
| $N=1$ SUSY | **[Т]** | One covariantly constant spinor $\eta_0 = 1_{\mathbb{O}}$ |
| SM from singularities $\leftrightarrow$ SM from $G_2$ | **[Т]** | $SU(3) = \mathrm{Stab}_{G_2}(e_O)$ — identical mechanism |
| 21D modular space | **[С при C27]** | Requires continuous limit $a \to 0$ |
| Full correspondence $Z_{\text{UHM}} = Z_M$ | **[С при C27, C28]** | Requires both conditions |

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

where $SU(3) = \mathrm{Stab}_{G_2}(e_O)$ (T-42e [Т]) and $SU(2) \subset SU(3)$ is the standard embedding.

### 2.2 Embedding Construction {#lqg-embedding}

#### T-171: LQG Embedding Functor [С при C29] {#t-171}

:::tip Theorem T-171
Under the condition:

**(C29)** (Spatial limit): the limit $M \to \infty$ of a composite system of holons with finite-range Gap coupling generates a spin network on the graph $\mathcal{G}_M$ (the adjacency graph of holons);

there exists a functor

$$
\mathcal{F}_{\text{LQG}}: \mathbf{SpinNet}_{SU(2)} \to \mathbf{Hol}_{\text{comp}}
$$

with the following properties:

**(a)** On objects: the spin network $(\mathcal{G}, j_e, i_v)$ (graph $\mathcal{G}$, spins $j_e$ on edges, intertwiners $i_v$ on vertices) maps to a composite system of holons:

$$
(\mathcal{G}, j_e, i_v) \mapsto \bigotimes_{v \in V(\mathcal{G})} \Gamma_v
$$

where each holon $\Gamma_v \in \mathcal{D}(\mathbb{C}^7)$ is associated with vertex $v$, and the Gap-coherences $\gamma_{ij}^{(v,w)}$ between adjacent holons $(v,w)$ encode the edge spin:

$$
j_e = \frac{1}{2} \left\lfloor 7 \cdot |\gamma_{\{A,S,D\}}^{(v,w)}|^2 \right\rfloor
$$

**(b)** Restriction $G_2 \to SU(3) \to SU(2)$: the choice of O-direction (Page–Wootters, A5) breaks $G_2 \to SU(3)$ (T-42e [Т]). Further restriction to the $\{A,S,D\}$-sector (spatial degrees of freedom) gives $SU(2) \subset SU(3)$:

$$
\mathbf{3}_{SU(3)} \to \mathbf{2}_{SU(2)} \oplus \mathbf{1}
$$

Intertwiners $i_v$ are recovered from the $G_2$-invariants of the internal algebra.

**(c)** Area spectrum: the area operator in LQG has a discrete spectrum $A = 8\pi l_P^2 \gamma \sum_e \sqrt{j_e(j_e+1)}$. In UHM, discreteness follows from the finite-dimensionality of $\mathcal{D}(\mathbb{C}^7)$ (the spectrum of $D_{\text{int}}$ is discrete, T-53 [Т]).
:::

**Proof sketch.**

**Step 1 (Graph from coherences).** For $M$ holons, the inter-holon coherence defines the graph $\mathcal{G}_M$: vertices are holons, edge $(v,w)$ exists $\Leftrightarrow$ $\|\Gamma_{vw}^{\text{cross}}\|_F > \epsilon$ (Gap coupling). This is a direct analogue of the spin network graph.

**Step 2 (Spin from the $\{A,S,D\}$-sector).** The sector $\{A,S,D\} \cong \mathbf{3}_{SU(3)}$ (T-53 [Т]). Restriction to $SU(2) \subset SU(3)$: $\mathbf{3} \to \mathbf{2} \oplus \mathbf{1}$. The inter-holon coherence in the $\{A,S,D\}$-sector determines an element of the $SU(2)$-representation, i.e., the spin $j$ of the edge.

**Step 3 (Intertwiners).** At each vertex $v$, the contraction of incoming/outgoing $SU(2)$-representations is the standard intertwiner construction. In UHM this is a section of the coherence matrix $\Gamma_v$ in the $\{A,S,D\}$-sector.

**Step 4 (Dynamics).** Spin foam = history of spin networks = 2-complex. In UHM the evolution $\mathcal{L}_\Omega$ of the composite system = a sequence of states $\{\Gamma_v(\tau)\}_{v,\tau}$ generating a 2-complex (graph $\times$ time).

### 2.3 Fano Spin Foam Amplitudes {#fano-spin-foam}

The vertex amplitude in the EPRL/FK model is defined by the 15$j$-symbol. In UHM the analogous construction uses the Fano plane:

**Definition (Fano amplitude).** For a vertex $v$ with 7 adjacent edges (Fano configuration):

$$
A_{\text{Fano}}(v) = \prod_{p=1}^{7} \left( \sum_{m} \begin{pmatrix} j_{i_p} & j_{j_p} & j_{k_p} \\ m_{i_p} & m_{j_p} & m_{k_p} \end{pmatrix} \right) \cdot W_7[\{j_e\}]
$$

where $(i_p, j_p, k_p)$ is Fano line $p$, the 3$j$-symbols are standard, and $W_7$ is a weight factor from $G_2$ representation theory.

**Status:** [Г]. Required: (a) prove that $A_{\text{Fano}}$ satisfies the axioms of a spin foam amplitude; (b) show convergence to classical geometry.

### 2.4 Embedding Assessment

| Aspect | Status | Comment |
|--------|--------|---------|
| $SU(2) \subset SU(3) \subset G_2$ | **[Т]** | Standard representation theory |
| Graph from coherences | **[Т]** | Direct construction |
| Spin from $\{A,S,D\}$-sector | **[Т]** | Sector decomposition (T-53 [Т]) |
| Full functor $\mathcal{F}_{\text{LQG}}$ | **[С при C29]** | Requires control of the limit $M \to \infty$ |
| Fano amplitudes | **[Г]** | Construction proposed, rigorous proof absent |

---

## 3. Causal Sets {#каузальные-множества}

### 3.1 Mathematical Context

The theory of causal sets (Bombelli–Lee–Meyer–Sorkin, 1987) postulates:
- A discrete set of events $(C, \preceq)$ with a partial order;
- Causal structure is fundamental; metric and topology are derived;
- The number of elements of a causal set ↔ volume ($V \sim N$ — the Hauptvermutung);
- The d'Alembertian on a causal set → curvature in the continuum limit.

### 3.2 Embedding Construction {#causal-embedding}

#### T-172: Causal Sets Embedding [С при C30] {#t-172}

:::tip Theorem T-172
Under the condition:

**(C30)** (Causal completeness): for any finite causal set $(C, \preceq)$ that faithfully embeds into $M^4$ (T-120 [Т]), there exists a configuration of $M = |C|$ holons with Gap coupling reproducing the causal order;

every finite causal set $(C, \preceq)$ embeds into the ∞-topos $\mathbf{Sh}_\infty(\mathcal{C})$ via the nerve:

$$
\mathcal{F}_{\text{CS}}: \mathbf{CausalSet}_{\text{fin}} \to \mathbf{Sh}_\infty(\mathcal{C})
$$

**(a)** On objects: $(C, \preceq) \mapsto N_\bullet(C)$ — the nerve of the category $(C, \preceq)$ (viewed as a category), which is a simplicial set and defines an object in $\mathbf{Sh}_\infty(\mathcal{C})$.

**(b)** Causal order from $\mathbb{Z}_7$-clocks: emergent time $\tau \in \mathbb{Z}_7$ (A5, Page–Wootters) [Т] defines a «clock position» $\tau_v$ for each holon. Causal order:

$$
v \preceq w \quad \Leftrightarrow \quad \tau_v \leq \tau_w \;\land\; d_{\mathcal{G}}(v,w) \leq c \cdot |\tau_w - \tau_v|
$$

where $d_{\mathcal{G}}$ is the Connes distance (T-119 [Т]) and $c$ is the maximum speed of coupling (finite-range Gap coupling).

**(c)** Discreteness: the temporal clocks $\mathbb{Z}_{7^M}$ and the finite number of holons $M$ ensure the discreteness of the causal set. In the continuum limit (T-118, T-119, T-120 [Т]) the Lorentzian manifold $M^4$ is recovered.
:::

**Proof sketch.**

**Step 1 (Partial order from Page–Wootters).** Each holon has emergent clocks $\tau_v \in \mathbb{Z}_{7^M}$ (T-38b [Т]). This defines a canonical temporal ordering.

**Step 2 (Spatial structure).** The finite-range Gap coupling defines a «light cone»: $v$ can influence $w$ $\Leftrightarrow$ $d(v,w) \leq c \cdot \Delta\tau$. This is the standard causal structure.

**Step 3 (Nerve as an object of the ∞-topos).** The nerve $N_\bullet(C, \preceq)$ is the canonical embedding of a partially ordered set into an ∞-category. Since $\mathbf{Sh}_\infty(\mathcal{C})$ is an ∞-topos (A1), $N_\bullet(C)$ defines an object in it (as an ∞-sheaf on $\mathcal{C}$ with Bures topology).

**Step 4 (Metric recovery).** The volume-element correspondence of causal sets ($V \sim N$) ↔ the thermodynamic limit of UHM ($M \to \infty$, T-117 [Т]).

### 3.3 Embedding Assessment

| Aspect | Status | Comment |
|--------|--------|---------|
| Discrete time structure | **[Т]** | $\mathbb{Z}_{7^M}$ — discrete clocks (T-38b [Т]) |
| Causal order | **[Т]** | Finite-range Gap coupling + emergent time |
| Continuum limit → $M^4$ | **[Т]** | T-118 + T-119 + T-120 [Т] |
| Full functor | **[С при C30]** | Requires proof of causal completeness |
| Embedding into ∞-topos | **[Т]** | Nerve — standard construction |

---

## 4. Universal Property of the UHM ∞-Topos {#универсальное-свойство}

### 4.1 Mathematical Context

To assert the Meta-ToE status, a category-theoretic justification is required: the ∞-topos $\mathbf{Sh}_\infty(\mathcal{D}(\mathbb{C}^7), J_{\text{Bures}})$ must possess a **universal property** in an appropriate category of physical theories.

Key references:
- **Schreiber (2013, 1310.7930):** Differential cohomology in a cohesive ∞-topos. Gauge fields, QFT, BV-BRST formalism — all within cohesive ∞-toposes.
- **Baez (1995, q-alg/9503002):** Higher algebra and topological QFT. Extended TQFTs as functors from nCob.
- **Lurie (2009):** Classification of extended TQFTs: fully dualizable objects.

### 4.2 Category of Physical Theories {#категория-phys}

**Definition (Category $\mathbf{PhysTheory}$).** Objects are triples $(E, \mathcal{A}, D)$:
- $E$ — ∞-topos (state space);
- $\mathcal{A}$ — observable algebra (C*-algebra or its ∞-categorical version);
- $D$ — dynamics (automorphism or flow on $\mathcal{A}$).

Morphisms are triples $(f^*, \alpha, \beta)$:
- $f^*: E_1 \to E_2$ — geometric morphism of ∞-toposes;
- $\alpha: \mathcal{A}_1 \to f^*\mathcal{A}_2$ — algebra homomorphism;
- $\beta: D_1 \to f^* D_2 \circ \alpha$ — compatibility with dynamics.

### 4.3 Uniqueness Theorem {#теорема-единственности-мета}

#### T-173: Rigidity of the UHM Primitive [Т] {#t-173}

:::tip Theorem T-173
The structured primitive $\mathfrak{T} = (\mathbf{Sh}_\infty(\mathcal{C}), J_{\text{Bures}}, \omega_0)$ is unique (up to equivalence of ∞-toposes) among those ∞-toposes of the form $\mathbf{Sh}_\infty(\mathcal{D}(\mathbb{C}^N), J)$ that satisfy:

**(i)** $J$ is induced by a monotone metric (Chentsov–Petz theorem: $J = J_{\text{Bures}}$ — the unique minimal one [Т]);

**(ii)** The classifier $\Omega$ generates L-operators $L_k = |k\rangle\langle k|$, yielding a primitive Liouvillian (T-39a [Т]);

**(iii)** Minimality: $N = 7$ (Theorem S [Т], octonionic derivation [Т]);

**(iv)** $G_2$-rigidity: the holonomic representation is unique up to $G_2$ (T-42a [Т]).

Therefore: $\mathfrak{T}$ is unique (up to $G_2$, $\omega_0$).
:::

**Proof.**

Each of the conditions (i)–(iv) fixes the corresponding structure:

**(i)** Petz's theorem (1996): the class of monotone Riemannian metrics on $\mathcal{D}(\mathcal{H})$ is parametrized by operator-monotone functions $f$. The Bures metric is minimal ($g_{\text{Bures}} \leq g_f$ for all $f$). The choice of minimal metric is canonical and unique [Т] ([Emergent Geometry](/docs/physics/gravity/emergent-geometry)).

**(ii)** L-unification determines $L_k$ from $\Omega$ (T-16 [Т]). Primitivity of $\mathcal{L}_0$ for given $L_k$ is a theorem (T-39a [Т]). These conditions fix the Liouvillian.

**(iii)** $N = 7$ is the minimal dimension satisfying (AP)+(PH)+(QG)+(V) (Theorem S [Т]) and simultaneously realizing the octonionic structure P1+P2 → $\mathbb{O}$ (Track B [Т]). The uniqueness of $N$ fixes the category $\mathcal{C}$.

**(iv)** $G_2$-rigidity (T-42a [Т]) shows that the representation is unique up to the 14-dimensional $G_2$. Consequently, two ∞-toposes satisfying (i)–(iii) are related by a $G_2$-transformation.

In total: $\mathfrak{T}$ is determined uniquely up to $G_2 \times \mathbb{R}_{>0}$ (gauge + scale $\omega_0$). $\blacksquare$

### 4.4 Universal Property: Receiving Map {#приёмное-отображение}

#### T-174: Receiving Map [Г] {#t-174}

:::tip Theorem T-174
For any object $(E, \mathcal{A}, D)$ in $\mathbf{PhysTheory}$ satisfying:

**(a)** $\mathcal{A}$ contains a C*-subalgebra isomorphic to $A_{\text{int}} = \mathbb{C} \oplus M_3(\mathbb{C}) \oplus M_3(\mathbb{C})$;

**(b)** The dynamics $D$ is CPTP (completely positive and trace-preserving);

**(c)** There exists a distinguished observable subalgebra of dimension $\leq 7$;

there exists an essentially unique morphism:

$$
(f^*, \alpha, \beta): (E, \mathcal{A}, D) \to (\mathbf{Sh}_\infty(\mathcal{C}), A_{\text{int}}, \mathcal{L}_\Omega)
$$

in $\mathbf{PhysTheory}$.
:::

**Proof sketch.**

**Step 1.** Condition (a) fixes the sector decomposition $1 \oplus 3 \oplus \bar{3}$ (T-53 [Т]).

**Step 2.** Condition (b) + (c): CPTP dynamics on a $\leq 7$-dimensional space. By Theorem S [Т], the minimal complete realization is $N = 7$. The map $\alpha: \mathcal{A} \to A_{\text{int}}$ is a factorization through projection onto the 7D subalgebra.

**Step 3.** Dynamical compatibility: $\mathcal{L}_\Omega$ is the unique primitive CPTP Liouvillian for given $L_k$ (T-39a [Т]) with a $G_2$-covariant Fano dissipator. The map $\beta$ is determined uniquely up to $G_2$.

**Step 4.** The induced geometric morphism $f^*: E \to \mathbf{Sh}_\infty(\mathcal{C})$ follows from the universality of the ∞-topos of sheaves: by Giraud's theorem, for any local map $\alpha$ there exists a unique geometric morphism.

**Status:** [Г]. A full proof requires: (i) formalization of $\mathbf{PhysTheory}$ as an (∞,1)-category; (ii) verification of all conditions of Giraud's theorem in this context; (iii) explicit construction of $\beta$ for specific physical theories (QM, QFT, GR).

### 4.5 Embedding Diagram {#схема-вложений}

```
                    Sh_∞(D(C⁷), J_Bures)
                         │    [Т-173]
                    ┌────┼────────────┐
                    │    │            │
              F_M   │    │ F_CS       │ F_LQG
            [С]     │    │ [С]        │ [С]
                    ▼    ▼            ▼
              M-theory  CausalSet   SpinNet
              on G₂     ∞-topos     SU(2)⊂G₂
                    │                 │
                    │    G₂-holonomy  │ SU(2)⊂SU(3)⊂G₂
                    │                 │
                    ▼                 ▼
              11D = 4D + 7D      spin = {A,S,D}
              [Т: T-120+T-53]    [Т: T-53]
```

---

## 5. Summary Table {#сводная-таблица}

| Theory | Functor | Key mechanism | Status | Conditions |
|--------|---------|---------------|--------|------------|
| **M-theory** | $\mathcal{F}_M: \mathbf{Hol}_{\text{comp}} \to \mathbf{G_2\text{-}Mfld}$ | $G_2 = \mathrm{Aut}(\mathbb{O}) = \mathrm{Hol}(\mathcal{M}_7)$ | **[С при C27, C28]** | Continuous limit, SUSY extension |
| **LQG** | $\mathcal{F}_{\text{LQG}}: \mathbf{SpinNet} \to \mathbf{Hol}_{\text{comp}}$ | $SU(2) \subset SU(3) \subset G_2$, spin from $\{A,S,D\}$ | **[С при C29]** | Spatial limit |
| **Causal sets** | $\mathcal{F}_{\text{CS}}: \mathbf{CausalSet} \to \mathbf{Sh}_\infty(\mathcal{C})$ | $\mathbb{Z}_{7^M}$-clocks, finite-range Gap coupling | **[С при C30]** | Causal completeness |
| **Universal property** | Receiving map in $\mathbf{PhysTheory}$ | $G_2$-rigidity + minimality 7 | **[Г]** | Formalization of $\mathbf{PhysTheory}$ |

### 5.1 Honest Assessment

All three embeddings (Tasks 1–3) have status **[С]** — conditional theorems. Conditions C27–C30 are substantive mathematical statements, not trivialities. The universal property (Task 4) is **[Г]**: the formulation is proposed, but a full proof requires substantial additional work.

What is **proven unconditionally [Т]**:
1. The $G_2$-symmetry is identical between UHM and M-theory on $G_2$-manifolds;
2. The chain of embeddings $SU(2) \subset SU(3) \subset G_2$ connects LQG with UHM algebraically;
3. The discrete time structure ($\mathbb{Z}_{7^M}$) + continuum limit ($M^4$) encompasses causal sets as an intermediate stage;
4. Primitive rigidity (T-173) shows the uniqueness of the UHM construction.

What is **not proven**:
1. Full equivalence $Z_{\text{UHM}} = Z_M$ at the quantum level;
2. The specific form of Fano spin foam amplitudes;
3. The universal property in the strict categorical sense.

---

## 6. Results Registration {#регистрация}

| Theorem | Statement | Status | Conditions |
|---------|-----------|--------|------------|
| **T-170** | Recovery of the M-theoretic limit | [С при C27, C28] | Continuous Gap limit, SUSY extension |
| **T-171** | LQG embedding functor | [С при C29] | Spatial limit |
| **T-172** | Causal sets embedding | [С при C30] | Causal completeness |
| **T-173** | Rigidity of the UHM primitive | [Т] | — |
| **T-174** | Receiving map in $\mathbf{PhysTheory}$ | [Г] | Formalization of the category |
| **C27** | Continuous Gap limit | [П] | — |
| **C28** | Supersymmetric extension | [П] | — |
| **C29** | Spatial limit | [П] | — |
| **C30** | Causal completeness | [П] | — |

---

## Links

- **Relies on:** [Spectral triple (T-53)](/docs/proofs/physics/physics-correspondence), [Emergent $M^4$ (T-117–T-121)](/docs/proofs/physics/emergent-manifold), [$G_2$-rigidity (T-42a)](/docs/proofs/categorical/uniqueness-theorem), [SUSY from $G_2$](/docs/physics/particle-physics/susy), [Gap functional integral](/docs/physics/gravity/quantum-gravity), [Sector decomposition](/docs/physics/gauge-symmetry/standard-model)
- **Justifies:** Meta-ToE status of UHM
- **Status registry:** T-170 — T-174, C27 — C30 ([Registry](/docs/reference/status-registry))
