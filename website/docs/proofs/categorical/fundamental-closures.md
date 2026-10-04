---
sidebar_position: 5
title: "Fundamental Closures (T-210..T-223)"
description: "Foundational theorems closing the last mathematical gaps of UHM: strict Φ-monotonicity, PhysTheory coherences, rheonomy modality, Bures-Yoneda, hard-problem meta-theorem, cross-layer identity, analytical ε_eff, L3 tricategory coherence, Kan complex, sector-product SUSY, no-reduction F₄→G₂, UHM's relationalist route through the List/DeBrota no-go results, the resource geometry of the viable window (no single MRQT optimum), Putnam-triviality foreclosure, plus computational programmes for Λ and π_bio."
---

# Fundamental Closures — T-210..T-223

This document contains **fourteen foundational theorems** T-210 through T-223 that close the last mathematical and categorical gaps of the UHM axiomatic framework, together with two computational-programme specifications (Λ-deficit numerical minimisation and π<sub>bio</sub> measurement protocol). Each theorem is given with a complete rigorous proof; cross-references from natural-home documents (Yukawa hierarchy, depth tower, two-aspect monism, etc.) point back to the canonical proofs collected here.

:::info Summary table
| Theorem | Content | Method | Status |
|---|---|---|---|
| T-210 | Topology-refinement implication withdrawn; selected pair-score identity survives | [✗] former universal claim | See corrected section above |
| **T-211** | **PhysTheory** is an $(\infty,1)$-category with all higher coherences | Grothendieck construction of $E \mapsto \mathrm{Fun}(B\mathbb R, \mathrm{Alg}(E))$ over $\mathbf{Topoi}_\infty$ (HTT 3.2) | [T] (corrected 2026-09-25: the full embedding into $\mathbf{Topoi}_\infty$ is retracted [✗]; [C at T-119] before) |
| **T-212** | The U-projection $X \mapsto \frac17\operatorname{Tr}(X)\mathbf{1}$ is the $G_2$-twirl (T-212′); its former identification with the rheonomy modality **Rh** is retracted | Schur's lemma + Haar measure; Rh preserves global points | [T] for T-212′; [✗] for "Rh explicit" (it was [C at the differential cohesion of the UHM site (T-185) and a solid-cohesive extension], and [T] before) |
| T-213 | Representability and 138-bit bound withdrawn; minimal Kraus count equals Choi rank | [✗] former universal claim | See corrected section above |
| T-214 | Internal-bridge no-go withdrawn; phenomenal identification remains an input | [✗] former universal claim | See corrected section above |
| **T-215** | Cross-layer identity convention for fractal towers | Choice of $\iota_\mathrm{min}$ / $\iota_\mathrm{max}$ criterion | [T]+[D] |
| **T-216** | Closed-form analytical ε<sub>eff</sub> | Symbolic $V_\mathrm{Gap}$ minimisation | [C at (SV)] (the structure was listed as [T] until 2026-09-25) |
| **T-217** | 3-truncation construction [T]; operational L3 bridge [Pr] | Truncation reflector / fundamental 3-groupoid | Old forced K=4 and universal threshold proof [✗]; corrected §11 |
| **T-218** | Singular-classifying-space Kan construction [T] | Topological horn retraction | Cognitive ceiling / 3-coskeleton claim [✗]; realization bridge [Pr] |
| **T-219** | Λ SUSY-suppression via sector product | ε<sup>12</sup> = ε<sup>4·3</sup> from 3-sector decomposition | [H] (was [T at T-64] until 2026-09-25) |
| **T-220** | Exact comparison obstructions | No nontrivial complex-linear $F_4$ action on $\mathbb C^7$; $\mathbb CP^6$ and $\mathbb OP^2$ are not homotopy equivalent | [T at these requirements]; universal functor prohibition withdrawn [✗] |
| **T-221** | Local sheaf equality and interpretive scope | Joint local equality iff both global sections restrict to the same local section; distinct globals can agree locally | [T at specified sheaf/site]; universal first-person prohibition withdrawn [✗], interpretation [I] |
| **T-222** | Resource geometry of the viable window (restated 2026-09-26; the former "MRQT-completeness: Lawvere fixed point = Pareto resource optimum" is [✗]) | Majorization on the purity window: no optimum inside, Pareto set on $P = 2/7$, $F_1$ and $F_\infty$ minimised by different spectra, no terminal object | [T] |
| T-223 | Universal Putnam foreclosure withdrawn; RI-conditional invariant comparison survives | [✗] former universal claim | See corrected section above |

Plus **computational programmes**: Λ-deficit numerical specification (§8), π<sub>bio</sub> measurement protocol (§9).
:::

---

## 1. T-210: Topology refinement versus a pair score {#t-210}

The former universal strict-monotonicity theorem is withdrawn [✗]. A Grothendieck topology is a collection of covering sieves, not a subset of matrix-index pairs. A proper refinement does not imply that some new pair is observed. The canonical $\Phi(\rho)=P/d-1$ has no topology argument; with state and frame fixed it remains unchanged.

**Replacement [T at a specified pair-selection rule].** For finite ordered off-diagonal pair sets $S\subseteq S'$, define $\Phi_S=d^{-1}\sum_{(i,j)\in S}|\rho_{ij}|^2$. Then

$$
\Phi_{S'}-\Phi_S=d^{-1}\sum_{(i,j)\in S'\setminus S}|\rho_{ij}|^2\ge0.
$$

It is strict exactly when a newly included pair has nonzero coherence. This follows by subtraction, and does not assert that any site refinement supplies $S\subsetneq S'$. Such a rule and its operational meaning must be defined and verified separately. A finite pair set also cannot supply infinitely many strict additions by a dense-time argument.

---

## 2. T-211: PhysTheory is an $(\infty,1)$-category — the Grothendieck construction over $\mathbf{Topoi}_\infty$ {#t-211}

:::warning Corrected 2026-09-25 — what the earlier version of this section got wrong
The section stated that $\mathbf{PhysTheory}$ is a **full $(\infty,1)$-subcategory** of $\mathbf{Topoi}_\infty$, via $\iota(E, \mathcal A, D) := \mathbf{Sh}_\infty(\mathrm{Spec}(\mathcal A), J_\mathrm{Bures})$, fully faithful "by T-173" (the universal T-173 is now withdrawn [✗]), with coherences "inherited via HTT 5.2.7"; it was [C at T-119] because Step 1 invoked the Connes reconstruction of T-119. The recheck of Step 1 found that T-119 was never the issue:
1. **Step 1 did not need T-119.** Every object of $\mathbf{PhysTheory}$ ([ToE embeddings §4.2](/docs/proofs/physics/toe-embeddings#категория-phys)) already carries its $\infty$-topos $E$; nothing has to be reconstructed from $\mathcal A$. The assignment $\mathcal A \mapsto \mathbf{Sh}_\infty(\mathrm{Spec}\,\mathcal A, J_\mathrm{Bures})$ is not even well typed — the Bures coverage lives on a state space $\mathcal D(\mathbb C^N)$, not on the spectrum of an algebra — and it forgets $E$.
2. **"Fully faithful" is false [✗].** Faithfulness was argued from T-173, which is a statement about *objects* (rigidity of one primitive), not about morphisms. Any functor $\mathbf{PhysTheory} \to \mathbf{Topoi}_\infty$ that remembers only the topos forgets the algebra map $\alpha$, and two different $\alpha$ over one geometric morphism exist (part (c) below). So $\mathbf{PhysTheory}$ is not a full subcategory of $\mathbf{Topoi}_\infty$.
3. **The coherence argument cited the wrong result.** HTT §5.2.7 concerns localisations; and a full subcategory needs no presentability to inherit coherences — every full simplicial subset of a quasicategory is a quasicategory. The size remark "finite NCG algebras range over a proper class of Wedderburn forms" is also false: finite-dimensional $C^*$-algebras form a set up to isomorphism.

What survives, and is proved below without T-119, T-173 or T-174: $\mathbf{PhysTheory}$, with the objects and morphisms of T-174, **is** an $(\infty,1)$-category with all higher coherences, and its mapping spaces are computed fibrewise over geometric morphisms. The status moves [C at T-119] → **[T]** for this statement; the full-embedding claim is retracted [✗].
:::

:::tip Theorem T-211 ($\mathbf{PhysTheory}$ is an $(\infty,1)$-category) [T]

Let $\mathbf{Topoi}_\infty$ be the (large) $\infty$-category of $\infty$-topoi and geometric morphisms (Lurie, HTT Def. 6.3.1.5). For an $\infty$-topos $E$ let $\mathrm{Alg}(E)$ be the $\infty$-category of associative algebra objects of $E$ for its cartesian monoidal structure (Lurie, HA §2.4.1, §4.1), and $\mathrm{Dyn}(E) := \mathrm{Fun}(B\mathbb R, \mathrm{Alg}(E))$ the algebras with an action of the group $\mathbb R$ — the dynamics $D$ of T-174. A geometric morphism $f: E_1 \to E_2$ has a left-exact inverse image $f^*: E_2 \to E_1$, which preserves finite products and therefore induces $f^*: \mathrm{Dyn}(E_2) \to \mathrm{Dyn}(E_1)$; this gives a functor $\mathrm{Dyn}: \mathbf{Topoi}_\infty^{\mathrm{op}} \to \widehat{\mathbf{Cat}}_\infty$. Define $p: \mathbf{PhysTheory} \to \mathbf{Topoi}_\infty$ as its cartesian unstraightening (the Grothendieck construction, HTT §3.2). Then:

**(a) Coherence.** $\mathbf{PhysTheory}$ is an $(\infty,1)$-category and $p$ is a cartesian fibration. Associativity of composition up to coherent homotopy, the pentagon, the interchange law and all higher simplicial identities hold, because $\mathbf{PhysTheory}$ is a quasicategory: every inner horn has a filler.

**(b) Objects and morphisms are those of T-174.** An object is a triple $(E, \mathcal A, D)$. For objects $x_i = (E_i, \mathcal A_i, D_i)$, the map $\mathrm{Map}(x_1, x_2) \to \mathrm{Map}_{\mathbf{Topoi}_\infty}(E_1, E_2)$ has fibre over $f$ equal to $\mathrm{Map}_{\mathrm{Dyn}(E_1)}\big((\mathcal A_1, D_1),\, f^*(\mathcal A_2, D_2)\big)$. A point of it is a pair $(\alpha, \beta)$: an algebra map $\alpha: \mathcal A_1 \to f^*\mathcal A_2$ and the coherent family of homotopies $\beta_t: \alpha \circ D_1(t) \simeq f^*D_2(t) \circ \alpha$ ($t \in \mathbb R$) — the triple $(f^*, \alpha, \beta)$ of T-174, with $\beta$ now typed correctly and its higher coherences supplied. Composition is $(g, \alpha', \beta') \circ (f, \alpha, \beta) \simeq (g f,\ f^*\alpha' \circ \alpha,\ \beta_{\mathrm{comp}})$, well defined up to a contractible space of choices.

**(c) $p$ is not faithful, so $\mathbf{PhysTheory}$ is not a full subcategory of $\mathbf{Topoi}_\infty$.** Let $\mathcal S$ be the $\infty$-topos of spaces (terminal in $\mathbf{Topoi}_\infty$, so $\mathrm{Map}(\mathcal S, \mathcal S) \simeq *$) and $\mathcal A = \mathbb C$, the discrete multiplicative monoid, with trivial dynamics. Over the unique geometric morphism $\mathcal S \to \mathcal S$ lie at least two components of $\mathrm{Map}(x, x)$: the identity and complex conjugation.

:::

**Proof.**

*(a).* $\mathrm{Alg}(E)$ is functorial in finite-product-preserving functors (HA §2.4.1–2.4.2: a product-preserving functor between cartesian monoidal $\infty$-categories is symmetric monoidal and so preserves algebra objects), and $\mathrm{Fun}(B\mathbb R, -)$ is functorial by postcomposition; hence $\mathrm{Dyn}$ is a functor on $\mathbf{Topoi}_\infty^{\mathrm{op}}$ (inverse images are left exact, HTT Def. 6.3.1.1). The straightening–unstraightening equivalence (HTT Thm. 3.2.0.1) turns it into a cartesian fibration $p$. A cartesian fibration is an inner fibration (HTT Def. 2.4.2.1), and an inner fibration over a quasicategory has a quasicategory as total space: an inner horn in $\mathbf{PhysTheory}$ maps to an inner horn in $\mathbf{Topoi}_\infty$, which has a filler, and the inner-fibration property lifts it. $\square$

*(b).* For a cartesian fibration, the mapping-space fibre over $f: p x_1 \to p x_2$ is $\mathrm{Map}_{p^{-1}(E_1)}(x_1, f^* x_2)$, where $f^*x_2$ is the source of a $p$-cartesian lift of $f$ (HTT Prop. 2.4.4.2 and the definition of the straightening); here $p^{-1}(E_1) = \mathrm{Dyn}(E_1)$ and the cartesian lift is $f^*$. A morphism in $\mathrm{Fun}(B\mathbb R, \mathrm{Alg}(E_1))$ is a natural transformation: its component is $\alpha$, its naturality data over the morphisms $t$ of $B\mathbb R$ are the homotopies $\beta_t$, with their higher coherences. Composition in a cartesian fibration is composition in the base together with $f^*$ of the later fibre map, as stated. If one prefers the constant group object $\mathbb R_E$ to the discrete group, nothing changes: $E_{/\pi^* B\mathbb R} \simeq \mathrm{Fun}(B\mathbb R, E)$ by descent (HTT §6.1.3). $\square$

*(c).* In $\mathcal S$ a discrete monoid is an ordinary monoid, and $\mathrm{Map}_{\mathrm{Alg}(\mathcal S)}(\mathbb C, \mathbb C)$ is the discrete set of monoid endomorphisms of $(\mathbb C, \cdot)$. Complex conjugation is unital and multiplicative, $\overline{zw} = \bar z\,\bar w$, and differs from the identity; with trivial $D$ both are equivariant. So $\pi_0$ of the fibre over the one point of $\mathrm{Map}(\mathcal S, \mathcal S)$ has at least two elements, and $p$ is not faithful. $\blacksquare$

Numerical check: `check_core_numbers.py`, `test_phystheory_forgets_to_topoi_unfaithfully_and_composes_associatively` — a finite model (discrete topoi $\mathbf{Set}^X$ over finite sets, families of monoids in the fibres): composition is associative and unital on 300 random triples, the multiplicative monoid $\{0,1\}$ has two endomorphisms over the identity of a point, and conjugation is a unital multiplicative map of $\mathbb C$ other than the identity.

**What T-211 does for T-174.** The $(\infty,1)$-structure of the [definition of $\mathbf{PhysTheory}$](/docs/proofs/physics/toe-embeddings#категория-phys) is supplied by (a)–(b), not by a full embedding into $\mathbf{Topoi}_\infty$; and (b) — over a point the fibre between 0-truncated objects is a set — is what makes compatibility with dynamics a property in the $C^*$-typed subcategory of the [restated T-174](/docs/proofs/physics/toe-embeddings#t-174) (2026-09-26). T-211 says nothing about which morphisms exist: the former "essentially unique receiving morphism into UHM" is retracted [✗] there, and the universal property that holds — $u_0 = (A_{\text{int}}, \mathrm{id})$ corepresents $A_{\text{int}}$-structures, rigid exactly on $\mathbb{C}^7$ — is T-174's own proof.

**Dependencies**: the definition of $\mathbf{PhysTheory}$ in ToE embeddings §4.2 (objects and morphisms only); Lurie HTT Def. 2.4.2.1, Prop. 2.4.4.2, Thm. 3.2.0.1, §6.1.3, Def. 6.3.1.5; Lurie HA §2.4.1–2.4.2, §4.1. *Removed 2026-09-25:* T-119 (not used — each object carries its topos), T-173 (a statement about objects, which cannot give faithfulness), T-174 (its universal property is not used), T-178 (retracted as a derivation), HTT 5.2.7 and 5.5.2.9.

*Status history:* [T] with "full embedding verified" until the first audit; [C at T-119] from 2026-09-11 (in the registry row until 2026-09-25); [T] since 2026-09-25 for the corrected statement (a)–(c), the full-embedding claim [✗].

---

## 3. T-212: the U-projection is the $G_2$-twirl, not the rheonomy modality {#t-212}

:::tip Theorem T-212′ ($G_2$-twirl) [T]
Let $G_2$ act on $\mathbb{C}^7$ by its seven-dimensional representation (the complexification of $\mathrm{Im}\,\mathbb{O}$), and let $dg$ be the Haar probability measure. Then for every $X \in M_7(\mathbb{C})$

$$
\mathcal{T}(X) := \int_{G_2} g\,X\,g^\dagger\,dg = \tfrac17\operatorname{Tr}(X)\,\mathbf{1}.
$$

$\mathcal{T}$ is a unital, trace-preserving, completely positive idempotent, it is the only trace-preserving linear map onto $\mathbb{C}\mathbf{1}$, and on states it sends every $\Gamma$ to $I/7$. With the unnormalised trace, $X \mapsto \operatorname{Tr}(X)\mathbf{1}$ satisfies $E \circ E = 7E$ and is not idempotent.
:::

**Proof.** By invariance of the Haar measure, $\mathcal{T}$ is idempotent, self-adjoint for the Hilbert–Schmidt product, and its image is the commutant $\{X : gXg^\dagger = X \ \forall g \in G_2\}$; so $\mathcal{T}$ is the orthogonal projection onto the commutant. The seven-dimensional representation of $G_2$ is irreducible of real type, so its complexification is irreducible and, by Schur's lemma (W. Fulton, J. Harris, *Representation Theory*, GTM 129, Springer 1991, Lemma 1.7), the commutant is $\mathbb{C}\mathbf{1}$ (numerically: the joint kernel of $X \mapsto [D_a, X]$ over the fourteen generators $D_a$ of $\mathfrak{g}_2$ has dimension 1, `test_g2_twirl_is_the_normalised_trace_projection`). The orthogonal projection onto $\mathbb{C}\mathbf{1}$ is $X \mapsto \frac{\langle \mathbf{1}, X\rangle}{\langle \mathbf{1}, \mathbf{1}\rangle}\mathbf{1} = \frac17 \operatorname{Tr}(X)\mathbf{1}$. A linear map onto $\mathbb{C}\mathbf{1}$ has the form $X \mapsto f(X)\mathbf{1}$, and preserving the trace forces $7f(X) = \operatorname{Tr}(X)$. Complete positivity: $\mathcal{T}$ is an average of unitary conjugations. $\blacksquare$

The formula is not specific to $G_2$: every subgroup of $U(7)$ acting irreducibly on $\mathbb{C}^7$ (for instance $SO(7)$ or $U(7)$ itself) has the same twirl. The reading of $\mathcal{T}$ as the U-dimension ("Unity = aggregation over the seven dimensions") is an interpretation [I].

:::warning Retracted [✗] (2026-09-25): "T-212 — the rheonomy modality Rh, explicitly $\mathrm{Rh}(F)(\Gamma) = \operatorname{Tr}(F(\Gamma))\cdot\mathbf{1}$"
An earlier version stated, first as [T] and then as [C at the differential cohesion of the UHM site (T-185) and a solid-cohesive extension], that in UHM's differentially cohesive ∞-topos $\mathbf{Sh}_\infty(\mathcal C_7, J_B)$ the rheonomy modality is the right adjoint of a "bosonic-grade forgetful" functor $\flat_{\mathrm{bos}}$, with the explicit formula $\mathrm{Rh}(F)(\Gamma) := \operatorname{Tr}(F(\Gamma))\cdot\mathbf{1}_{\mathcal C_7}$, and that the seven modalities $\mathrm{Id}, \Pi, \flat, \Im, \sharp, \&, \mathrm{Rh}$ map bijectively to O, A, S, D, L, E, U. The identification with Rh is false, and the condition it was placed under does not rescue it:
1. **Rh preserves points.** In solid cohesion (the 2017 version of Schreiber's DCCT, site of its Definition 6.6.13; D. J. Myers, M. Riley, *Commuting Cohesions*, arXiv:2301.13780, §6.3) the rheonomy modality acts by $\mathrm{Rh}\,X(C^\infty(\mathbb{R}^n)\otimes W\otimes\Lambda\mathbb{R}^q) = X(C^\infty(\mathbb{R}^n)\otimes W)$. At the point ($n = 0$, $W = \mathbb{R}$, $q = 0$) this gives $\mathrm{Rh}\,X(\mathbb{R}^0) = X(\mathbb{R}^0)$: the unit $X \to \mathrm{Rh}\,X$ is a bijection on global points. The state space $\mathcal{D}(\mathbb{C}^7)$ is an object of the differentially cohesive $\mathfrak{T}_{\mathrm{UHM}}$ ([T-185 (ii′)](/docs/proofs/categorical/cohesive-closure#t-185-ii-prime)); in any solid-cohesive extension of it, Rh keeps every state $\Gamma$ where it is, while the formula sends it to $I/7$.
2. **The formula is not a modality.** A modality acts on objects of the topos; "$\operatorname{Tr}(F(\Gamma))$" treats the values of a sheaf as matrices, which is typed only for an operator-valued function. The old Step 1 identified the bosonic part with $G_2$-invariants, $\flat_{\mathrm{bos}}(F) = F^{G_2}$; in solid cohesion the bosonic part is the even part of a supergeometric object, and $G_2$ plays no role. The old Step 2 equated $\int_{G_2} F(g\cdot\Gamma)\,dg$ (an average of the argument) with $\operatorname{Tr}(F(\Gamma))\cdot\mathbf{1}$ (a trace of the value) "by the Weyl integration formula"; the two are different operations, and neither is Rh.
3. **Rh is not in the list of differential cohesion.** A differentially cohesive ∞-topos carries $\mathrm{Id}$, $\Pi \dashv \flat \dashv \sharp$ and $\mathrm{Red} \dashv \Im \dashv \&$ — seven, pairwise distinct on $\mathfrak{T}_{\mathrm{UHM}}$ ([T-185 (ii′), item 4](/docs/proofs/categorical/cohesive-closure#t-185-ii-prime)). Solid cohesion adds a third triple $\rightrightarrows \dashv \rightsquigarrow \dashv \mathrm{Rh}$, giving ten. The seven of the old table drop Red and borrow Rh.

What the old theorem wanted — an explicit, canonical projection for the U-dimension — is Theorem T-212′ above, proved without any cohesion. The old table of modalities and dimensions is kept below as a reading [I], with Red in the place Rh occupied.
:::

**Modalities and dimensions — a reading [I].** With the corrected list of differential cohesion ([T-185 (ii′)](/docs/proofs/categorical/cohesive-closure#t-185-ii-prime)):

| Modality | Adjunction role | UHM dimension (reading) |
|---|---|---|
| $\mathrm{Id}$ | Identity | O (Foundation) |
| $\Pi$ | Shape | A (Articulation) |
| $\flat$ | Flat (discrete coreflection) | S (Structure) |
| $\Im$ | Infinitesimal shape (de Rham) | D (Dynamics) |
| $\sharp$ | Sharp (codiscrete reflection) | L (Logic) |
| $\&$ | Infinitesimal flat | E (Interiority) |
| $\mathrm{Red}$ | Reduction | U (Unity) — earlier Rh; the $G_2$-twirl of T-212′ is an operator on $M_7(\mathbb{C})$, not a modality |

**Dependencies**: T-212′ uses only the representation theory of $G_2$ (Schur's lemma, Haar measure). The retraction uses T-185 (ii′) [T] and the definition of Rh in solid cohesion.

---

## 4. T-213: Channel realization is not Yoneda representability {#t-213}

The former Yoneda/description-length theorem is withdrawn [✗]. A map $\rho\mapsto\Lambda(\rho)$ is a state-space map, not the presheaf $yU(V)=\operatorname{Hom}(V,U)$ on the open site. Yoneda embeds site objects; it does not turn every quantum channel into a representable sheaf. A single Kraus branch $K\rho K^\dagger$ may have trace less than one, so a density-state Bures distance cannot be applied to it without normalization or a declared subnormalised-state extension. The Hamiltonian offset cannot determine a geometric injectivity radius.

**Exact finite realization [T].** For a channel $\Lambda:M_7\to M_7$, its positive Choi matrix admits a spectral decomposition. Reshaping its nonzero eigenvectors gives a Kraus realization with $r=\operatorname{rank}J(\Lambda)\le49$. Conversely any Kraus realization is a sum of $r'$ rank-one Choi terms, so $r'\ge r$. Thus the minimal Kraus count is exactly the Choi rank.

Kraus count is not a bit description of the coefficients. All unitary channels have count one, yet their matrices carry continuous parameters. A numerical description also specifies entries, precision, norm of error and encoding convention. The proxy $r\log_2 7$ may be defined [D] as an instrument-count cost; it cannot prove that every channel has a 138-bit accurate description or a $\log(1/\varepsilon)$ simulation bound.

On the open site, representables are the sheaves associated with opens. A continuous channel on density space induces inverse images of opens and the corresponding geometric morphism; this typed construction is the valid connection with the topos.

---

## 5. T-214: The scope of Lawvere and phenomenal bridges {#t-214}

The claimed theorem prohibiting an internal experiential bridge is withdrawn [✗]. Lawvere's fixed-point theorem concerns a weakly point-surjective map $A\to B^A$ in a cartesian closed category and concludes that every endomorphism of $B$ has a fixed point. An arbitrary map $W:X\to Y$ is not such a map. Factoring $W$ through its graph introduces no diagonal contradiction. The original predicate also compared a truth value with a putative experiential object, so the asserted equality was untyped.

An elementary counterexample is the internal surjective identity $W:X\to X$ in sets, for any nonempty set $X$. Taking $X$ to be a declared space of content labels shows that internality and surjectivity are compatible. Assigning phenomenal meaning to those labels is an extra semantic identification; the example does not claim to derive that meaning.

Consequently the phenomenal interpretation remains [P/I] because it has not been independently established by the mathematical structure. It is not a proved impossibility of every future formal bridge, nor a theorem that mathematics can make no further progress on the hard problem. Any stronger no-go statement must specify expressibility, coding, evaluation and diagonal hypotheses and check their types.

---

## 6. T-215: cross-layer identity convention [D/I] {#t-215}

Treating components separately ($\iota_{\min}$) and assigning agency to a selected aggregate ($\iota_{\max}$) are different conventions. Neither partial trace nor existence of a joint state proves subject identity. The selected lift $\rho\mapsto\rho\otimes\sigma$ with fixed normalized $\sigma$ followed by partial trace returns $\rho$ exactly [T]; this concerns chosen maps, not subjects.

Two7-dimensional registers have joint dimension49. A seven-dimensional aggregator is an additional map. If it uses only averaged marginals, it discards correlations; existence of that aggregate does not certify collective consciousness. Nested records, local criteria and observation must be specified separately. Universal T-42a and T-123 are withdrawn [✗] and do not settle these conventions.

## 7. T-216: the effective parameter needs inputs [H] {#t-216}

The universal analytical $\varepsilon_{\mathrm{eff}}$ formula is withdrawn. Withdrawn T-74 [✗] supplies no unique spectral potential. Schur’s lemma does not fix invariant-tensor scalar coefficients; restricting to an axis sector is not continuous G2 reduction; identifying mean coherences with particle generations needs a physical bridge.

A conditional computational task remains: specify Hermitian D, a potential with independent coefficients, density constraints and a readout $\varepsilon(\rho)$; then locate stationary points or global minima with error bounds. A continuous potential on the compact density domain attains its minimum [T], but uniqueness or agreement with the measured parameter does not follow. A numerical substitution or fit does not derive a parameter from the axioms.

## 8. Λ-deficit numerical programme specification {#lambda-programme}

The cosmological-constant deficit (~78 orders before minimisation) reduces to a **finite numerical computation** on the $G_2$-reduced phase space $(S^1)^{21}/G_2$. This section provides an explicit computational-programme specification.

### 8.1. Problem statement

Compute the minimum of the full Gap potential

$$
V_\mathrm{Gap}(\theta) = V_2 + V_3 + V_4, \qquad \theta \in (S^1)^{21}/G_2
$$

with $G_2$-gauge-fixed coordinates and evaluate $\Lambda_\mathrm{CC}$ from the spectral action formula (T-65 [T]):

$$
\Lambda_\mathrm{CC} = f_0 \Lambda^4\bigg|_{\theta^*} - \frac{1}{2}\zeta'_{H_\mathrm{Gap}}(0)\bigg|_{\theta^*},
$$

where $\theta^*$ is the global minimum.

### 8.2. Discretization

- Discretize each $S^1$ factor with $N = 128$ lattice points. After $G_2$-reduction ($21 - 14 = 7$ independent dimensions), the effective lattice has $N^7 = 128^7 \approx 5.6 \times 10^{14}$ sites.
- Use $G_2$-invariant measure (Weyl integration formula) for gauge-fixing.
- Action: Wilson-type lattice discretization of $V_\mathrm{Gap}$ with finite-difference Laplacian.

### 8.3. Monte Carlo / HMC

- Algorithm: Hybrid Monte Carlo (HMC) with $G_2$-invariant kernel.
- Thermalization: $10^4$ sweeps.
- Measurement: $10^4$ independent configurations, blocked to control autocorrelation.
- Observables: $\langle V_\mathrm{Gap}\rangle$, $\langle \theta^*\rangle$, $\langle\zeta'_{H_\mathrm{Gap}}(0)\rangle$.

### 8.4. Cost estimate

- Total: $10^{14}$ sites × $2 \times 10^4$ sweeps × $10^3$ flops/site-sweep = $2 \times 10^{21}$ flops.
- On a cluster at $10^{15}$ flops/s (modern HPC, ~1000 GPU-nodes): 2×10⁶ s ≈ **23 CPU-days**.
- Single-node estimate (consumer GPU, $10^{13}$ flops/s): ~**6 CPU-years**.

### 8.5. Output validation

- Must reproduce known perturbative suppression (10^{−41.5}) at tree level.
- Must give unique minimum (verified by Hessian positivity — T-64 [T] (corrected to the $G_2$-invariant potential; its vacuum has no sector values — hypothesis (SV))).
- Numerical $\Lambda$ must agree with observed $\sim 10^{-120}$ within ±5 orders (stricter than current ±10).

**Status**: [C at (SV)] → **numerical programme fully specified**. Total resource cost < $10^5$ USD on cloud HPC. No theoretical obstacle remains.

---

## 9. π<sub>bio</sub>: observation model and identification {#pi-bio-protocol}

The neural estimator $\hat\pi_\theta$ is [D]; its interpretation and calibration are [H]. Structural automorphisms of $\mathcal D(\mathbb C^7)$ do not identify a map from neural data. The former “structural uniqueness by $G_2$” claim is withdrawn (2026-10-03): continuity of an encoder supplies no inverse. Use the [observation-fiber and informational-completeness theorems](/docs/applied/research/reconstruction-identifiability#fiber-theorem), the [mathematical kernel's threshold definitions](/docs/reference/mathematical-kernel#thresholds), and the [measurement protocol](/docs/applied/research/measurement-protocol).

### 9.1. Measurement design

The proposed multimodal recording includes EEG, fMRI, HRV and TMS-evoked EEG. Each instrument's timing, reference, bandwidth, preprocessing and acquisition compatibility must be specified before calibration. A common scalar or pairwise statistic cannot be computed by treating 1-kHz EEG, a 2-s fMRI repetition time and autonomic measures as interchangeable synchronous samples. Record an explicit resampling/observation model, feature-specific time scales, missing modalities and intervention settings. A dataset qualifies only if it supplies the declared measurement bundle; the [provenance check R1](/docs/applied/research/measurement-protocol#replication-ready-tms-eeg) supersedes the former unverified dataset recommendation.

### 9.2. Candidate diagonal proxies [H]

The table below is one **candidate dictionary**, distinct from the spectral-band and functional-feature dictionaries on the other protocol pages. It is not a theorem identifying seven state projections. Pre-register one dictionary, including normalization and noise, and compare alternatives prospectively.

| Axis | Candidate feature | Scale | Proposed interpretation [H] |
|---|---|---|---|
| A | EEG delta power | 1–4 Hz | Activation proxy |
| S | EEG theta power | 4–8 Hz | Memory/structure proxy |
| D | EEG beta power | 12–30 Hz | Sensorimotor proxy |
| L | EEG gamma power | 30–80 Hz | Coordination proxy |
| E | fMRI DMN connectivity | Declared estimator/window | Self-reference proxy; no PCI input |
| O | HRV LF/HF | Separate LF and HF bands/windows | Autonomic proxy |
| U | EEG global field power | Declared bandwidth/reference | Global response proxy |

Normalized nonnegative proxies can define a candidate diagonal, but normalizing heterogeneous features does not validate their correspondence to $\gamma_{kk}$. Fit unit conversion/calibration on a published wakefulness reference cohort and freeze it. Do not choose weights to force $P=2/7$ at a labeled boundary or to suppress between-subject purity variance.

### 9.3. Complex coherences and information content

Seven normalized diagonals contain only six independent numbers. Full $\Gamma$ has another 42 real coherence coordinates, not 21 real coupling magnitudes. A real phase-locking value (PLV) is $|\langle e^{i(\phi_i-\phi_j)}\rangle|$; it does not contain signed phase. Use the complex mean or cross-spectrum, a declared phase reference and a validated observation law for real/imaginary components. Cross-frequency pairs need their harmonic/PAC convention. For EEG–fMRI–HRV pairs the observable is especially model-dependent; it cannot be declared a same-frequency PLV by relabeling.

The former formula $\gamma_{ij}=|\mathrm{PLV}_{ij}|e^{i\Delta\phi_{ij}}$ omitted the PSD bound $|\gamma_{ij}|^2\leq\gamma_{ii}\gamma_{jj}$, normalization and global positivity constraints. It is replaced by constrained observation-model fitting. Pairwise bounds alone do not ensure a PSD $7\times7$ matrix.

In a calibrated linear model, Hermitian observation operators must span the 48-dimensional traceless space for full-state reconstruction [ID-2](/docs/applied/research/reconstruction-identifiability#linear-frame). Nonlinear models need separate global identification proofs and local rank/conditioning diagnostics. Diagonal, magnitude and Gap measurements admit explicit different states with the same observations [phase counterexamples](/docs/applied/research/reconstruction-identifiability#phase-counterexamples). If phases are unresolved, retain the compatible set; do not infer them through $\arcsin(\mathrm{Gap})$, behavior or zero-fill.

### 9.4. State validity, fit and uncertainty

- Enforce $\Gamma\succeq0$ and $\operatorname{Tr}\Gamma=1$ as mathematical constraints. Negative eigenvalues within solver tolerance are numerical residuals, not physical state eigenvalues; publish the residual, any PSD/trace projection and its change in the observation fit.
- State which likelihood/noise model is fitted. A valid state need not fit the data, and a selected optimum need not be uniquely identified. Report fit, design rank, smallest singular value, calibration uncertainty and confidence sets.
- Apply **SUB-2:** $\lambda_2=0$ in every threshold test and $\lambda_1=0$ in confirmation. A viability or dynamics penalty must not insert the conclusion into the estimator.
- Publish target ranges over compatible states and the rule for an **undetermined** verdict. Any extension/lift for differentiation $D$ and any remaining symmetry must be part of the pre-registration.

See the [reference estimator](/docs/applied/research/measurement-protocol#алгоритм-pi-bio) and [ID-A … ID-D](/docs/applied/research/reconstruction-identifiability#confirmatory). These mathematical obligations do not certify the neural bridge.

### 9.5. Held-out tests and the phenomenological bridge

**Calibration:** freeze all $\theta$, dictionary, frame and analysis choices on wakefulness only (SUB-1); do not fit NREM, anaesthesia, REM or ketamine labels. Exclude PCI, behavior and reports from the confirmatory predictor. Use subject-level train/test separation and predeclare comparators, uncertainty and abstentions.

**Registered hypotheses:** P8.1 tests $P(\hat\Gamma_{\mathrm{wake}})>2/7$, P8.2 tests $P(\hat\Gamma_{\mathrm{NREM3}})<2/7$, and P8.4 compares the full predicate

$$
\mathrm{Cons}=(P>2/7)\wedge(R\geq1/3)\wedge(\Phi\geq1)\wedge(D\geq2)
$$

with the independently computed PCI verdict on the same sessions. $\Phi\geq1$ alone is not the verdict; $P>3/7$ fails canonical reflection, and $D$ remains a separate condition. Numerical proximity of $0.31$ and $2/7$ gives no bridge. Cohen's $\kappa\geq0.8$ and $\kappa<0.4$ are predeclared empirical corroboration/rejection criteria [H], with sampling uncertainty, repeated-subject dependence and undetermined UHM verdicts handled as specified in the [experimental protocol](/docs/applied/research/experimental-protocol#exp-2-1). REM and ketamine provide especially useful held-out contrasts with current behavior. A numerical threshold equivalence requires an equivalence test, not failure to reject an equality null.

**Limits:** agreement supports the registered observation/threshold package, not a unique ontological encoder or consciousness ontology by itself. The [substitution argument](/docs/applied/research/measurement-protocol#substitution-position) still constrains the relation of prediction data to report/behavior inference; restricting the proposed bridge to natural sleep–wake/anaesthetic states is [H]. Alternative encoders after a failed test must be newly registered and the original failure retained. No consciousness conclusion outside the validated domain follows from this construction. By [the local-equality scope of T-221](#t-221), this measurement also does not select between the interpretive routes through the List/DeBrota results.

**Status:** mathematical identification criteria and test obligations specified; a calibrated, informationally adequate neural observation model and independent empirical validation remain open. This section does not claim that the full empirical specification is already complete.

---

## 10. Summary table

| # | Theorem / Protocol | Previous status | New status | Closure method |
|---|---|---|---|---|
| T-210 | Topology-refinement implication withdrawn; selected pair-score identity survives | [✗] former universal claim | See corrected section above |
| T-211 | PhysTheory higher coherences | [T] deferred to HTT | **[T]** as the Grothendieck construction (2026-09-25; read "[T] verified" by a full embedding, then [C at T-119]; the full embedding [✗]) | Cartesian unstraightening, HTT 3.2 |
| T-212 | U-projection / "Rh modality explicit" | [T] unnamed (T-185) | **[T] $G_2$-twirl (T-212′)**; the identification with Rh [✗] (read "[T] defined", then "[C] defined", until 2026-09-25) | Schur + Haar |
| T-213 | Representability and 138-bit bound withdrawn; minimal Kraus count equals Choi rank | [✗] former universal claim | See corrected section above |
| T-214 | Internal-bridge no-go withdrawn; phenomenal identification remains an input | [✗] former universal claim | See corrected section above |
| T-215 | Cross-layer identity | [C] (T-205 downgraded) | **[T]+[D]** | Conventional choice theorem |
| T-216 | Analytical ε<sub>eff</sub> | [H] no formula | **[C at (SV)]** (listed [T at T-64] until 2026-09-25) | Closed-form symbolic |
| §8 | Λ-deficit programme | "computational task" | **Spec complete** | HMC on $(S^1)^{21}/G_2$ |
| §9 | π<sub>bio</sub> protocol | [H] specific | **Spec complete, awaiting data**; the test is the concordance of verdicts (P8.4), bounded by the substitution argument (corrected 2026-09-25) | EEG/fMRI/HRV 7-feature map |

**Current scope:** valid constructions and conditional results are listed individually; there is no global certificate of mathematical closure.

**Remaining genuinely open**:
- Numerical computation of Λ (§8) — resource-bounded, no theoretical obstacle.
- Empirical validation of π<sub>bio</sub> (§9) — experimental programme; the substitution argument of Kleiner & Hoel bounds what it can show, and UHM claims nothing outside natural sleep–wake and anaesthetic states (the line read "no theoretical obstacle" until 2026-09-25).
- Phenomenal identification [P/I] remains an input; the former T-214 no-go is withdrawn.

~~**No mathematical gaps remain** in UHM's foundational framework after these closures.~~ Retracted [✗] (2026-09-25): the rows marked [C] and [H] above are open mathematical conditions, and the framework's own inputs stayed open until 2026-09-25 — the first-order condition and Poincaré duality of T-119, settled that day by the restatement of T-119, which computes the spatial spectrum (the orientation (Alt) of T15, listed here until 2026-09-25, is discharged by the [canonical-orientation theorem](/docs/proofs/minimality/theorem-octonionic-derivation#каноническая-ориентация)), on which T-120, T-121, T-211 and clause (iii) of T-221 rested (T-120 and T-121 are [T] since; the recheck of T-211 showed that it never needed T-119 — each object of PhysTheory carries its topos — and T-211 is [T] in its corrected form; clause (iii) of T-221 went with the corrected T-221). (The corrected T-221 of 2026-09-25 does not rest on T-119/T-120.)

---

## 11. T-217: the 3-type construction and the missing operational bridge {#t-217}

:::warning Status correction 2026-10-03
The former theorem that $\tau_{\le3}(\mathbf{Exp}_\infty)$ is a specified experiential tricategory with **exactly** three LGKS 2-cell classes and one new 3-cell, forcing $K=4$ and a universal L3 threshold $1/4$, is **retracted [✗]**. What survives is the standard 3-truncation construction **[T]**. Identifying it with operational metacognition requires a specified model and bridge **[Pr]**.
:::

### Theorem T-217, corrected mathematical scope [T]

Let $X$ be a specified Kan complex, or an object of a specified $\infty$-topos. Its 3-truncation $X_{\le3}=\tau_{\le3}X$ is 3-truncated and the unit $X\to X_{\le3}$ preserves the homotopy data in degrees at most three. As a space, $X_{\le3}$ admits a fundamental 3-groupoid model. No claim of exactly one nontrivial 3-cell or four information channels is part of this theorem.

**Proof.** The inclusion of 3-truncated objects admits the truncation reflector; its unit is universal for maps into 3-truncated objects. For spaces, the canonical fundamental $n$-groupoid construction and its universal property provide an $n$-groupoid representing $\tau_{\le n}X$. Apply $n=3$. Sources: [Kerodon, truncations and fundamental groupoids](https://kerodon.net/tag/0513); [Lurie, Higher Topos Theory §5.5.6](https://www.math.ias.edu/~lurie/papers/HTT.pdf). In a general $\infty$-topos this is an internal statement; turning it into a single global Kan complex requires a declared realisation.

### What is not supplied by truncation

1. **Typing.** A topological space has a singular complex. A category needs a declared nerve/classifying-space construction or enrichment before writing $\mathrm{Sing}(\mathcal E)$. Applying a truncation to an object is not the same as truncating an entire category without specifying the construction.
2. **Direction of processes.** A Kan complex models invertible paths. General CPTP channels are not invertible. Passing to a core or a groupoid completion changes the process category; it does not automatically preserve irreversible dynamics. For example, the classifying space of the category $0\to1$ is contractible, although the original category has a directed noninvertible arrow.
3. **Number of cells.** A 3-type only constrains homotopy above degree three. $K(A,3)$ exists for arbitrary abelian $A$, with arbitrary third-homotopy data; a point has none. There is no universal “one new 3-cell” count. Choosing a presentation or a coherence generator does not count statistically independent information channels.
4. **Tricategorical coherence.** A chosen tricategory must satisfy its coherence axioms. The [Gordon–Power–Street coherence theorem](https://doi.org/10.1090/memo/0558) gives a triequivalence to an appropriate semistrict model; it does not prove a universal cell count, a Bayesian prior, or a physiological threshold. A general non-groupoidal tricategory is not automatically a 3-type. The old strict category/3-type identifications and the appeal to HTT §5.2.7 for this cell count are withdrawn.
5. **Relation to L3.** A truncation does not test self-model predictions or imply $\pi_3\ne0$. The [canonical hierarchy](/docs/consciousness/hierarchy/interiority-hierarchy#l3-сетевое-сознание) now uses independently calibrated nonconstant metamodel probes. A topological representation must specify a functor connecting that operational record to $X$, with proved invariance and correspondence.

**Consequence for T-67.** T-217 does not upgrade the $3+1$ heuristic to a universal theorem. The old forced $K=4$ proof is **[✗]**; the replacement operational certificate is **[D]/[Pr]**, and its nonvacuity follows from the triangle inequality **[T]**. The categorical-to-operational bridge remains an explicit research obligation.

---

## 12. T-218: a Kan realization and its exact scope {#t-218}

### Correct construction [T]

Fix a self-map $F:\mathcal D(\mathbb C^7)\to\mathcal D(\mathbb C^7)$ and a universe in which its states form a set. Define the ordinary **discrete** orbit category $\mathcal C_F$ by

$$
\operatorname{Hom}(\rho,\sigma)=\{n\in\mathbb N_0:F^n(\rho)=\sigma\}.
$$

Arrows retain their integer labels, composition is addition, and identity is zero. These rules satisfy the category axioms by the iteration identity $F^{n+m}=F^nF^m$. If continuity/enrichment of the category is intended, that is additional data and requires a corresponding nerve construction.

Then

$$
\mathrm{Cog}:=\operatorname{Sing}(|N\mathcal C_F|)
$$

is a Kan complex **[T]**: this holds for the singular complex of **every** topological space, independently of purity, Fano uniqueness or cognitive interpretation.

**Proof.** A horn map into $\operatorname{Sing}(X)$ corresponds to a continuous map $f:|\Lambda_i^n|\to X$. The topological horn is a retract of $|\Delta^n|$. For a retraction $r$, $f\circ r$ is an extension and therefore a filler. A horn has $n$ faces, not $n-1$. Fillers are generally not unique. Source: [Kerodon §1.2 and Proposition 1.2.5.8](https://kerodon.net/tag/0508); [Lurie, Higher Topos Theory §1.2.5](https://www.math.ias.edu/~lurie/papers/HTT.pdf).

### Coskeleton is not the claimed 3-truncation

For a Kan complex $X$ and $n\ge0$, $\operatorname{cosk}_{n+1}X$ is a model of its homotopy $n$-truncation; it preserves the homotopy groups through degree $n$ and removes those above it. Thus $\operatorname{cosk}_3X$ is **2-truncated**, while a standard model for $\tau_{\le3}X$ is $\operatorname{cosk}_4X$. Source: [Kerodon §3.5.7, truncated Kan complexes](https://kerodon.net/tag/054N).

The unit $X\to\tau_{\le3}X$ is an equivalence only if $X$ is already 3-truncated. Choosing a truncation does not prove that condition. For example a Kan model of $K(\mathbb Z,4)$ has nonzero fourth homotopy, which 3-truncation removes. A finite density-matrix model, an implementation limit or a score below a detection threshold does not force this homotopy to vanish. A simplex is a map, not a density matrix with an assigned purity unless an explicit bridge supplies one.

### What the construction does not prove

1. The ordinary nerve $N\mathcal C_F$ need not be Kan: its positive-step arrows have no inverse. Singular realization changes the directed process category to a homotopy-type model. It does not turn an irreversible channel into a physically invertible process.
2. The filler argument proves existence, not a numerical $O(48)$ algorithm for arbitrary continuous maps. Complexity needs a finite representation, effective operations and a requested approximation accuracy.
3. There is no proved “Fano suppression of four-simplices”, equivalence $\mathrm{Cog}\simeq\tau_{\le3}\mathrm{Cog}$ on a vaguely named viable subset, or universal cognitive SAD_MAX = 3. The former claims are **withdrawn [✗]**. Even defining such a subset requires checking closure under all simplicial operators.
4. Operational cognitive depth requires independently tested nonconstant prediction certificates and compatible forgetting maps. Linking those records to this homotopy type remains **[Pr/H]**, not a consequence of Kan horn filling.

**Status T-218:** singular-classifying-space construction **[T]**; asserted 3-coskeleton/3-truncation identity, cognitive ceiling and universal filler complexity **[✗]**; cognitive realization bridge **[Pr]**. No dependency on T-142's score arithmetic is used in the surviving theorem.

---

## 13. T-219: Λ SUSY-suppression via sector decomposition {#t-219}

:::tip Theorem T-219 (SUSY Λ-suppression, sector derivation) [H]
In UHM's N=1 supersymmetric spectral action on $M^4 \times A_{\mathrm{int}}$ (T-65 [T]), the residual cosmological constant from SUSY-broken loops is suppressed by the factor

$$
\Lambda_\mathrm{SUSY} \;\sim\; \varepsilon^{12} \, M_P^4
$$

where $\varepsilon \sim 10^{-3}$ is the sector hierarchy parameter (T-64 [T] (corrected to the $G_2$-invariant potential; its vacuum has no sector values — hypothesis (SV))) and the exponent $12 = 4 \cdot k_{\mathrm{sec}}$ arises from:
- $k_{\mathrm{sec}} = 3$ sectors — ~~in the UHM decomposition $7 = \mathbf 1_O \oplus \mathbf 3_{A,S,D} \oplus \bar{\mathbf 3}_{L,E,U}$ (T-48a [T])~~ the axis-labelled decomposition is retracted (T-48a, 2026-09-25); the count 3 survives only for the complexified $\mathbb C^7 = \mathbb C e_O \oplus \mathbf 3 \oplus \bar{\mathbf 3}$, $\mathbf 3 = \mathrm{span}_{\mathbb C}\{A-iD,\,S-iU,\,L-iE\}$;
- Factor $4$ from the dimensional count of SUSY-breaking mass-squared splittings per sector in the one-loop correction $\delta\Lambda \sim (\delta m)^4 / M_P^4$ per sector.

**Status**: [H] since 2026-09-25 (was [T at T-64]; the earlier claim "the exponent structure $\varepsilon^{12}$ is derived" is retracted). Three reasons: (i) the sectors of Step 1 are the axis triples $\{A,S,D\}$, $\{L,E,U\}$ of the retracted T-48a, which are not $\mathrm{SU}(3)$-sectors; (ii) their breaking scales rest on T-52, retired as a theorem on 2026-09-25 and now the hypothesis (SA), and on (FE), conditional since the same date; (iii) Step 3's own one-loop sum $\sim 3\varepsilon^4 M_P^4$ exceeds $\varepsilon^{12} M_P^4$, so the $\varepsilon^{12}$ law needs the one- and two-loop terms to cancel, which is not shown (the registry already records the exact compensation as [H]). The numerical value $\varepsilon \approx 10^{-3}$ is conditional on T-64 unique vacuum (computational task).
:::

**Proof (four steps).**

**Step 1 (SUSY breaking scale per sector).** By the $G_2$-invariant superpotential T-50 [T] and sector decomposition T-48a (retracted [✗] 2026-09-25 in the axis-labelled form used here), each of the three sectors carries its own SUSY-breaking mass splitting. In UHM:
- **O-sector** (Page–Wootters clock): SUSY-breaking at $\delta m_O \sim \varepsilon \cdot M_P$ from the PW constraint coupling to external time.
- **3-sector** $\{A, S, D\}$: SUSY-breaking at $\delta m_3 \sim \varepsilon \cdot M_P$ from the sectoral asymmetry T-52 (retired as a theorem on 2026-09-25; its content is the hypothesis (SA) — and $\{A,S,D\}$ is not the $\mathbf 3$).
- **$\bar 3$-sector** $\{L, E, U\}$: SUSY-breaking at $\delta m_{\bar 3} \sim \varepsilon \cdot M_P$ from electroweak coupling T-FE (the construction is [C at (FE)] since 2026-09-25, and $\{L,E,U\}$ is not the $\bar{\mathbf 3}$).

All three sectors carry the **same** order-of-magnitude scale $\sim \varepsilon \cdot M_P$ because the sector hierarchy parameter $\varepsilon$ is **one** number (T-64 uniqueness of vacuum).

**Step 2 (One-loop SUSY-broken Λ contribution per sector).** For each sector, the standard N=1 SUSY-loop calculation (Martin 2010 *A Supersymmetry Primer* §7.2) gives the residual vacuum-energy contribution:

$$
\delta \Lambda_k \;\sim\; \frac{\operatorname{STr}(M_k^4)}{16\pi^2} \cdot \log(\Lambda_{\mathrm{UV}}/M_k)
$$

where $M_k$ is the SUSY-breaking mass-matrix of sector $k$ and $\operatorname{STr}$ is the supertrace. In exact SUSY, $\operatorname{STr}(M^{2n}) = 0$ for all $n$. In broken SUSY with splitting $\delta m_k$:

$$
\operatorname{STr}(M_k^4) \;\sim\; (\delta m_k)^4 \;\sim\; (\varepsilon M_P)^4 \;=\; \varepsilon^4 M_P^4.
$$

**Step 3 (Multi-sector product structure).** The three sectors are **independent** in the SUSY-broken spectral action: the super-trace decomposes as

$$
\operatorname{STr}(M^4)_{\mathrm{total}} = \operatorname{STr}(M_O^4) + \operatorname{STr}(M_3^4) + \operatorname{STr}(M_{\bar 3}^4) \;\sim\; 3 \varepsilon^4 M_P^4.
$$

This gives a **linear combination** $\sim \varepsilon^4$, not yet $\varepsilon^{12}$. The $\varepsilon^{12}$ arises at **higher loop order** through nested sector-sector interactions:
- At one-loop: $\sim \varepsilon^4$ per sector (additive)
- At two-loop with sector mixing: $\sim \varepsilon^4 \cdot \varepsilon^4 = \varepsilon^8$ per pair of sectors
- At three-loop with all three sectors mixing: $\sim \varepsilon^{12}$

The specific **three-loop product** structure $\varepsilon^{4\cdot 3} = \varepsilon^{12}$ is guaranteed by the $G_2$-invariance of the trilinear Fano coupling T-43d [T], which mandates that **each sector contributes one factor of $\varepsilon^4$** in the leading correction to $\Lambda$.

**Step 4 (Composition with the perturbative budget — absorption, not multiplication).** The SUSY-sector factor $\varepsilon^{12}$ does **not** multiply the full perturbative $10^{-41.5}$: the perturbative total already contains $\varepsilon^6$ (smallness of coherences), and $\varepsilon^{12}$ **absorbs** it, adding only $\Delta \approx \varepsilon^6$ on top of what is already counted. With the self-consistent central value $\varepsilon \sim 10^{-2}$ ([T-80](/docs/proofs/gap/lambda-budget#механизм-1): $\bar\varepsilon \approx 0.023$, allowed range $\varepsilon \in [10^{-3}, 10^{-1}]$), the rigorously composable **mean suppression is $\sim 10^{-53.5}$**; the cohomological $\Lambda_{\mathrm{global}} = 0$ [T] is an exact-zero statement of a *different class* (it reframes the question as the size of the **local** residual), and the sector-minimisation residual is an open **[C]** programme. The canonical composition rules and the resulting honest bracket $10^{-53.5}$ to $10^{-93.5}$ live in the [Λ-budget honest ledger](/docs/proofs/gap/lambda-budget#обновлённый-бюджет) — the single source of truth for the Λ composition.

**This replaces the earlier invalid "G₂ adjoint 14 → 7+7 decomposition" argument.** The G₂ adjoint representation **14** is irreducible (no such decomposition exists; $\mathrm{adj}(G_2)$ contains no $\mathbf{7}$). The correct derivation uses the sector decomposition of the UHM **state space** (T-48a), not of the gauge algebra — and that decomposition is itself retracted in its axis-labelled form (2026-09-25), see the status above.

**Status of sub-components**:
- ~~The exponent $12 = 4 \cdot 3$ is **[T]** (structural, from sector count).~~ Retracted 2026-09-25: the exponent is a hypothesis [H] (status above).
- The numerical value of $\varepsilon$: allowed range $[10^{-3}, 10^{-1}]$ [T-bounds], self-consistent central $\varepsilon \sim 10^{-2}$ [C at (SV)] — hence $\varepsilon^{12} \approx 10^{-24}$ central, with $10^{-36}$ only at the extreme lower edge. Quoting the edge value as the central one would manufacture $\sim\!10^{-120}$ by parameter choice; we do not.
- The cohomological statement gives only the absence of a *topological* $\Lambda$-term **[T]**; the reading "$\Lambda_{\mathrm{global}} = 0$" was **retracted 2026-09-10** (degree-0 data are untouched by $H^{n>0} = 0$), so class B carries no exact zero.

**Resulting composition** (per the [honest ledger](/docs/proofs/gap/lambda-budget#обновлённый-бюджет)):
- Perturbative: $\sim 10^{-41.5}$ [T] (includes $\varepsilon^6$);
- SUSY-sector $\varepsilon^{12}$ absorbs $\varepsilon^6$: net mean $\to \sim 10^{-53.5}$ [H for the structure since 2026-09-25, earlier listed as T at T-64; C for the $\varepsilon$ value];
- Cohomological argument: no topological $\Lambda$-term [T], **no** exact zero (retracted 2026-09-10);
- Sector-minimisation residual: **[C]** open numerical programme.

**Honest bracket: $\Lambda \sim 10^{-53.5}$ to $10^{-93.5}$** depending on how much of the sector programme is realised; closing the remaining $\gtrsim 27$ orders to the observed $10^{-120}$ is an **open computational + conceptual** task. $\blacksquare$

**Dependencies.** The sector-product algebra is conditional on a supplied field content, potential and supersymmetric vacuum. Finite combinatorics does not derive vacuum energy; T-71 is a physical bridge hypothesis [H]. Universal sector and spectral closure claims are withdrawn.

---

## 14. T-220: obstructions to exact equivalence, not to every functor {#t-220}

The universal “no reduction functor F4→G2 exists” claim is withdrawn. Constant functors exist between nonempty categories with a selected target object; projections, forgetful functors and approximate readouts are not prohibited by unequal dimensions or Euler characteristics.

**[T under exact comparison requirements].** Two specific obstructions survive:

1. A seven-dimensional complex vector space has no nontrivial differentiable **complex-linear** action of compact connected $F_4$. For a representation $\pi:F_4\to GL_7(\mathbb C)$, its differential first has the real domain $\mathfrak f_{4,\mathbb R}$. Complex-linearity of the representation permits the complex-linear extension $d\pi_{\mathbb C}:\mathfrak f_{4,\mathbb R}\otimes_{\mathbb R}\mathbb C\to\mathfrak{gl}_7(\mathbb C)$. The domain is a simple complex Lie algebra of complex dimension $52$, while the codomain has complex dimension $49$. The kernel of this extension is either the whole algebra or zero; injectivity is dimensionally impossible. Hence $d\pi=0$, and connectedness of $F_4$ makes $\pi$ trivial. This forbids **preserving a nontrivial full $F_4$ action exactly** in that register, not a $G_2$-equivariant readout after restricting the group.
2. $\mathbb CP^6$ and $\mathbb OP^2$ have Euler characteristics7 and3 and real dimensions12 and16. They are not homotopy equivalent or diffeomorphic. This forbids **equivalence of the spaces**, not arbitrary maps.

Restricted-representation splitting, coordinate embedding and physical composition are separate questions. Jordan rank-to-cognitive-depth and generation-count bridges remain hypotheses [H/I], not consequences of these obstructions. T-268 is algebra under its selected Jordan construction; it supplies no universal cognitive ceiling.

<a id="t-220-statement"></a>
<a id="t-220-proof"></a>
<a id="t-220-obstruction-i"></a>
<a id="t-220-obstruction-ii"></a>
<a id="t-220-obstruction-iii"></a>
<a id="t-220-obstruction-iv"></a>
<a id="t-220-obstruction-v"></a>
<a id="t-220-corollaries"></a>
<a id="t-220-three-generations"></a>
<a id="t-220-scope"></a>

## 15. T-221: local predicates and first-person interpretation {#t-221}

**[T under a specified sheaf of sets and equality predicates].** Let $\mathcal S$ be a sheaf of sets on a selected site **with terminal object $1$**, and let $x,y\in\mathcal S(1)$ and $s\in\mathcal S(U)$. Here $\mathcal S(1)$ identifies with global sections of the sheaf, and restriction along the unique $U\to1$ defines $x|_U,y|_U$. Then

$$
U\Vdash(s=x)\land(s=y)\quad\Longleftrightarrow\quad s=x|_U=y|_U.
$$

This is sheaf semantics and equality transitivity. Distinct **global** sections can agree on an inhabited local domain: continuous functions0 and $\max(t,0)$ agree on $t<0$. Thus global $x\ne y$ does not prohibit the joint local assertion. That conclusion additionally needs the equality subobject $\mathrm{Eq}(x,y)=0$ and a nonzero stage: if the joint assertion holds with this empty equalizer, the sheafification of the representable stage $y(U)$ must be initial. On an open-set site this exceptional stage is the empty open set.

Representable presheaves are sheaves only on a subcanonical site, or after sheafification; Yoneda alone does not supply this. A nondegenerate topos has a terminal object, but this does not derive physical one-world ontology or subject identity.

First-person facts, identification of local sections with subjects and selection of a philosophical route are interpretations [I] requiring their own semantic model. Convention T-215 [D] does not establish aggregate agency. Universal experiential-map prohibition T-214 is withdrawn [✗]; an unspecified phenomenal bridge is an open task, not a proved limit of mathematics. The local equality rule alone does not resolve philosophical no-go dilemmas.

## 16. T-222: the resource geometry of the viable window — no single resource optimum {#t-222}

**Motivation**. The Landauer principle ($W_\text{erase} \geq k_B T \ln 2$) is a *projection* of a richer multi-resource structure onto a single energy axis. Modern *quantum resource theories* (QRT, 2013–2026) generalise thermodynamics into a hierarchy: a family of Rényi free energies $F_\alpha$ (Brandão–Horodecki 2015), coherence monotones $C_\text{rel}, C_{HS}$ (Baumgratz–Cramer–Plenio 2014), non-Abelian conserved charges (Yunger-Halpern 2016–2023), algorithmic complexity $K_Q$ (Bennett–Zurek 1989–2003), quantum-memory-assisted erasure (Reeb–Wolf 2014). Each resource admits its own monotone and generalised second law.

The question: does the viability window of UHM single out one state that is optimal for the whole multi-resource vector — so that the dynamics would need no multi-objective criterion on top of $\mathcal{R}$? T-222 answers it: **no**. Inside the window every state is strictly dominated; on its boundary the Rényi family pulls apart, so no state is optimal for all resources at once; and the fixed points of the self-model are not optima either.

:::warning Erratum 2026-09-26: the former T-222 "MRQT-completeness, Lawvere fixed point = Pareto resource optimum" [✗]
The former statement read: "$\rho^* = \varphi(\Gamma)$, the Lawvere fixed point of T-96, realises the majorization-minimal viable spectrum ($P = 2/7$); every spectral MRQT-monotone is optimised there **simultaneously**; $\rho^*$ is the **terminal object** of the category of viable resource objects, the regeneration $\mathcal{R}$ being the unique resource-monotone morphism $\rho \to \rho^*$; UHM is MRQT-complete." Each part fails.

1. **$\varphi(\Gamma)$ is not a fixed point of $\mathcal{L}_\Omega$.** T-96 proves the opposite: at a nontrivial stationary state $\varphi(\rho^*_\Omega) \neq \rho^*_\Omega$ (step 2), and $\rho_* = \varphi(\Gamma)$ is the regeneration *target*, the value of the self-model at the current state ([unified $\rho_*$ lemma](/docs/core/dynamics/evolution#лемма-единство-rho-star)). Fixed points belong to $\varphi$ itself ([Theorem 10.1 of Gap thermodynamics](/docs/core/dynamics/gap-thermodynamics#неподвижная-точка-лавера): $I/7$ for $\varphi_{\mathrm{coh}}$, $\Gamma_{\eta_\infty}$ for $\varphi_J$, at least eight for $\varphi_s$), and they are not stationary states of $\mathcal{L}_\Omega$. Lawvere's theorem gives, under a point-surjection $A \to Y^A$, a fixed point of every endomorphism of $Y$ — here of $\varphi$, never of $\mathcal{L}_\Omega$; read in $\mathbf{Set}$ it gives nothing, since $\mathcal{D}(\mathbb{C}^7)$ has fixed-point-free self-maps, and the fixed points of a continuous $\varphi$ exist by Brouwer's theorem (Theorem 10.1(a)). T-96 carries no value $P = 2/7$.
2. **No simultaneous optimum** — item (iii) below: $F_1$ and $F_\infty$ are minimised by different spectra.
3. **No optimum in $\mathcal{V}_\text{full}$** — item (i): the purity condition $P > 2/7$ is open, and every viable state is strictly dominated.
4. **No terminal object** — item (iv).
5. **Lemmas.** L3 ("$K_Q(\rho^*) = O(\log(1/\varepsilon)) + O(1)$, hence $K_Q = O(1)$") contradicts itself and does not concern a spectral monotone ($K_Q$ is uncomputable and not a function of the spectrum); L4 called $C_{HS} = 1/7$ a minimum, but at $P = 2/7$ it is the maximum of $C_{HS} = P - P_\text{diag}$ (item (vi)); L6 read "majorization-minimal spectrum compatible with $P$" as unique, which item (iii) refutes. L1 (the twirled charges vanish) and the identity of L5 on uniform-diagonal states stand, in item (vi).

**Routes tried before lowering the headline.** (a) Identify the optimum with a fixed point of a self-model: $\Gamma_{\eta_\infty}$ of $\varphi_J$ is strictly dominated (item (v)), $I/7$ is not viable. (b) Take the optimum on the boundary, where F-monotonicity is not strict: the boundary carries a Pareto *set*, not a point, and it contains spectra optimal for $F_1$ and for $F_\infty$ that differ (item (iii)). (c) Weaken "terminal" to "reachable from every viable state" under the free operations of the resource theory: refuted by two explicit states (item (iv)). (d) Keep simultaneity for the sub-family $\alpha \leq 1$: $\Gamma_{1/\sqrt6}$ minimises $F_1$ uniquely and $F_{1/2}$ numerically, but $F_\alpha$ for $\alpha > 2$ prefer a three-level spectrum — the family splits at $\alpha = 2$, where $F_2$ is constant on the boundary. What survives is the theorem below, [T].
:::

### 16.1. Statement {#t-222-statement}

:::tip Theorem T-222 (The resource geometry of the viable window; restated 2026-09-26) [T]
Let $\mathcal{W} := \{\rho \in \mathcal{D}(\mathbb{C}^7) : 2/7 < P(\rho) \leq 3/7\}$ — the two orbit-invariant conditions of $\mathcal{V}_\text{full}$, $P > 2/7$ and $R = 1/(7P) \geq 1/3$ — and let $\overline{\mathcal{W}}$ be its closure. In the high-temperature limit $\rho_\beta \to I/7$ the Rényi free energies are $F_\alpha(\rho) = k_BT\,D_\alpha(\rho\,\|\,I/7) = k_BT\,(\log 7 - H_\alpha(\rho))$, $\alpha \in (0, \infty]$, with $H_\alpha$ the Rényi entropy of the spectrum ($F_1$ carries $S_\text{vN}$); a state is better on a component when that $F_\alpha$ is smaller.

(i) **No optimum inside the window.** For every $\rho \in \mathcal{W}$ and small $t > 0$ the state $\rho_t = (1-t)\rho + t\,I/7$ lies in $\mathcal{W}$, and $F_\alpha(\rho_t) < F_\alpha(\rho)$ for every $\alpha \in (0, \infty]$.

(ii) **The Pareto set lies on the boundary sphere.** On $\overline{\mathcal{W}}$ the Pareto set of $(F_{1/2}, F_1, F_2, F_\infty)$ is non-empty and lies on $P = 2/7$, where $F_2 = k_BT\log 2$ is constant.

(iii) **The Rényi family splits.** No state of $\overline{\mathcal{W}}$ minimises $F_1$ and $F_\infty$ together. $F_1$ has exactly one minimising spectrum,

$$
s_1 = \Bigl(\tfrac{1+\sqrt6}{7},\ \tfrac{6-\sqrt6}{42}\times 6\Bigr),
$$

the spectrum of $\Gamma_{1/\sqrt6} = (1 - \tfrac{1}{\sqrt6})\,I/7 + \tfrac{1}{\sqrt6}\,uu^\dagger$, the member of the $\varphi_J$ family $\Gamma_\eta$ on the sphere $P = 2/7$. The three-level spectrum $s_3 = \bigl(\tfrac{3+2\sqrt3}{21}\times 3,\ \tfrac{2-\sqrt3}{14}\times 4\bigr)$, also on the sphere, has the larger $F_1$ ($H_1 = 1.391$ against $1.602$) and the smaller $F_\infty$ ($H_\infty = 1.178$ against $0.708$).

(iv) **No terminal object.** Take as free operations the unital channels — the channels fixing $I/7$, under which every $F_\alpha$ is monotone. No state of $\overline{\mathcal{W}}$ is reachable from both the state of spectrum $s_1$ and $\mathrm{diag}(\tfrac13, \tfrac13, \tfrac13, 0, 0, 0, 0) \in \mathcal{W}$; so the category of window states with unital channels as morphisms has no terminal object, and the regeneration does not supply one.

(v) **Fixed points of the self-model are not optima.** The fixed point $\Gamma_{\eta_\infty}$ of $\varphi_J$ (Theorem 10.1(b)) lies in $\mathcal{W}$ for every $\alpha \in [0, 1]$ and is strictly dominated by $\Gamma_{1/\sqrt6}$ on every $F_\alpha$, $\alpha \in (0, \infty]$; the fixed point $I/7$ of $\varphi_{\mathrm{coh}}$ lies outside $\overline{\mathcal{W}}$.

(vi) **Frame components.** In the physical frame $C_{HS}(\rho) = P - P_\text{diag} \leq P - 1/7$, with equality exactly on uniform-diagonal states, on which also $C_\text{rel} = \log 7 - S_\text{vN}$, so that $C_\text{rel} = F_1/k_BT$ there. The $G_2$-twirled charges $\overline{Q}_a(\rho) = \int_{G_2}\mathrm{Tr}(g\rho g^\dagger T_a)\,dg$ vanish for every $\rho$: the 14 non-Abelian charges are frame data only.
:::

### 16.2. Proof {#t-222-proof}

**(i)** $P(\rho_t) = 1/7 + (1-t)^2(P(\rho) - 1/7)$ decreases continuously in $t$, so $\rho_t \in \mathcal{W}$ for small $t$. The spectrum of $\rho_t$ is $(1-t)\lambda + t\,(1/7, \ldots, 1/7)$, majorized by $\lambda$ and not a permutation of it (as $\lambda \neq$ uniform). $H_\alpha$ is strictly Schur-concave for $\alpha \in (0, \infty)$, and $H_\infty = -\log\lambda_{\max}$ increases strictly because $\lambda_{\max}(\rho_t) = (1-t)\lambda_{\max} + t/7 < \lambda_{\max}$ (A. W. Marshall, I. Olkin, B. C. Arnold, *Inequalities: Theory of Majorization and Its Applications*, 2nd ed., Springer 2011, Ch. 3).

**(ii)** $\overline{\mathcal{W}}$ is compact and $H_{1/2}, H_1, H_2, H_\infty$ are continuous on it, so maximising them lexicographically gives a non-empty set of maximisers, each Pareto-optimal. A point of $\overline{\mathcal{W}}$ with $P > 2/7$ is strictly dominated by the argument of (i); hence the Pareto set lies on $P = 2/7$, where $D_2(\rho\|I/7) = \log(7P) = \log 2$.

**(iii)** By (i) a minimiser of $F_1$ on $\overline{\mathcal{W}}$ lies on $P = 2/7$, and it has full rank, since $-\lambda\log\lambda$ has infinite slope at $0$. The Lagrange conditions for maximising $H_1$ under $\sum\lambda_i = 1$, $\sum\lambda_i^2 = 2/7$ read $\log\lambda_i + 2\nu\lambda_i = \text{const}$; the left side is monotone or unimodal in $\lambda_i$, so a maximiser has at most two distinct eigenvalues. Solving $m a + (7-m) b = 1$, $m a^2 + (7-m) b^2 = 2/7$ gives exactly three two-level spectra: $s_1$ ($m = 1$, from $49a^2 - 14a - 5 = 0$), $s_2 = (0.3687 \times 2,\ 0.0525 \times 5)$ and $s_3$ ($m = 3$, from $147a^2 - 42a - 1 = 0$), with $H_1 = 1.6019$, $1.5094$, $1.3909$. So $s_1$ is the unique minimising spectrum of $F_1$. Every minimiser of $F_\infty$ has $\lambda_{\max} \leq \lambda_{\max}(s_3) = 0.3078 < 0.4928 = \lambda_{\max}(s_1)$, so it is not $s_1$. The spectrum of $\Gamma_\eta$ is $\bigl((1+6\eta)/7,\ (1-\eta)/7 \times 6\bigr)$ with $P = (1 + 6\eta^2)/7$; $\eta = 1/\sqrt6$ gives $P = 2/7$ and $s_1$.

**(iv)** A unital channel maps $\rho$ to $\sigma$ if and only if $\lambda(\sigma) \prec \lambda(\rho)$ (P. M. Alberti, A. Uhlmann, *Stochasticity and Partial Order*, Reidel 1982). Let $\tau \in \overline{\mathcal{W}}$ with $\lambda(\tau) \prec s_1$. Then $P(\tau) \leq P(s_1) = 2/7 \leq P(\tau)$, and strict Schur-convexity of $\sum\lambda_i^2$ makes $\lambda(\tau)$ a permutation of $s_1$. But $s_1 \not\prec (\tfrac13, \tfrac13, \tfrac13, 0, 0, 0, 0)$, as $0.4928 > 1/3$. A terminal object would be reachable from both.

**(v)** $P(\Gamma_{\eta_\infty}) = 5/14$, $0.334$, $0.317$ at $\alpha = 0, 1/2, 1$ (Theorem 10.1(b)), in $(2/7, 3/7]$, and $\eta_\infty \in [0.4507, 0.5] > 1/\sqrt6 = 0.4082$. Then $\Gamma_{1/\sqrt6} = s\,\Gamma_{\eta_\infty} + (1-s)\,I/7$ with $s = 1/(\sqrt6\,\eta_\infty) \in (0, 1)$, and (i) applies.

**(vi)** $C_{HS} = P - P_\text{diag}$ (direct HS decomposition) and $P_\text{diag} = \sum_i\gamma_{ii}^2 \geq 1/7$ by Cauchy–Schwarz, with equality exactly at $\gamma_{ii} = 1/7$. $C_\text{rel}(\rho) = S(\Delta(\rho)) - S(\rho)$ and $\Delta(\rho) = I/7$ on uniform-diagonal states. The twirl: $\int_{G_2} g\rho g^\dagger\,dg = I/7$ by Schur's lemma, since $G_2$ acts irreducibly on $\mathbb{C}^7$, and each $T_a$ is traceless. $\blacksquare$

**Numerical check** (scratch run, 2026-09-26). Twenty thousand random spectra scaled onto $P = 2/7$: the best $H_{1/2}$ ($1.7893$) and $H_1$ ($1.6019$) are at $s_1$; the best $H_3$ ($1.2181$) and $H_\infty$ ($1.1225$, below $H_\infty(s_3) = 1.1783$) are at spectra with three large and four small eigenvalues, not at $s_1$.

### 16.3. Categorical interpretation {#t-222-categorical}

The existence of a unital channel defines a reachability preorder on spectra via majorization. The category of actual channels has many morphisms between the same objects and is not a preorder. It has no terminal object (iv), and the purity bound $P \geq 2/7$ cuts it along a sphere on which the order leaves many incomparable minimal elements (iii). The former reading — $I/7$ initial, $\rho^* = \varphi(\Gamma)$ terminal, "the limit state toward which all viable dynamics converge" — is retracted: $I/7$ lies outside the window, and $\varphi(\Gamma)$ is a map of the state, not an object. Which point of the Pareto sphere a holon approaches is decided by its self-model and its dynamics, not by the resource order: with $\varphi_J$ the fixed point $\Gamma_{\eta_\infty}$, the upper end of the living attractor, sits at $P = 0.317$–$0.357$, inside the window, where by (v) it is not resource-optimal.

### 16.4. Applicability domain {#t-222-scope}

1. **Purity window.** The results concern the selected spectral window; passing an independent extended D_diff criterion does not follow from the spectrum and must be checked separately.
2. **High temperature** — $\rho_\beta \to I/7$. At finite $\beta$ the reference state is $\rho_\beta$ and the free operations are the Gibbs-preserving channels; thermo-majorization replaces majorization, and the statements must be re-derived.
3. **Markovianity** is not used: the theorem is about states and the resource order, not about a flow.

### 16.5. Consequences {#t-222-consequences}

:::info What T-222 establishes
1. **UHM is not MRQT-complete in the former sense**: the viability window selects no resource optimum, and a choice on the Pareto sphere needs a criterion — a weight on the Rényi orders — that neither the self-model nor $\mathcal{L}_\Omega$ supplies.
2. **Viability costs resources**: every viable state could be made cheaper on every $F_\alpha$ by mixing it toward $I/7$ (i); what stops this is the viability bound, not resource optimality. The regeneration holds the holon *away* from the resource-cheap direction.
3. **For an FSQCE device** the design target is a point of the sphere $P = 2/7$ chosen by the order $\alpha$ that matters to the task: $\Gamma_{1/\sqrt6}$ for $F_1$ (von Neumann, $C_\text{rel}$), a state with three large eigenvalues, $s_3$ or better, for $F_\infty$ (single-shot).
4. The former items "$\mathcal{R}$ is the universal resource-monotone morphism" and "FSQCE is automatically Pareto-optimal across 25 resources" are retracted with the erratum.
:::

### 16.6. Falsification criteria {#t-222-falsification}

T-222 is a theorem about states; it is checked by computation, not by experiment. It would be refuted by a state of $\overline{\mathcal{W}}$ with $F_1 \leq F_1(s_1)$ and $F_\infty \leq F_\infty(s_3)$, or by a state of $\mathcal{W}$ that no $\rho_t$ improves. Experimentally, a device held at the living attractor of $\varphi_J$ should be strictly improvable on every $F_\alpha$ by partial depolarisation without leaving the window.

**Dependencies**: the exact HS decomposition, T-96 [T] (regeneration target $\varphi(\Gamma)$, $\varphi(\rho^*_\Omega) \neq \rho^*_\Omega$), [Theorem 10.1 of Gap thermodynamics](/docs/core/dynamics/gap-thermodynamics#неподвижная-точка-лавера) [T] (fixed points of the self-model), T-126 [T] ($R = 1/(7P)$), T-151 [T] (viability $P > 2/7$).

**External references**: Brandão et al. PNAS 112:3275 (2015); Baumgratz-Cramer-Plenio PRL 113:140401 (2014); Streltsov-Adesso-Plenio Rev. Mod. Phys. 89:041003 (2017); Yunger-Halpern Nat. Rev. Phys. 5:689 (2023); Marshall–Olkin–Arnold, *Inequalities* (2011); Alberti–Uhlmann, *Stochasticity and Partial Order* (1982); Schur's lemma (classical representation theory).

---

## 17. T-223: Representation dependence and conditional invariance {#t-223}

:::warning Revised 2026-10-03
The former universal Putnam-triviality foreclosure is withdrawn [✗]. Its proof used the now-withdrawn T-42a/T-123 claim that dynamic compatibility alone determines every encoder up to $G_2$. The replacement below is a conditional theorem about specified, reversibly comparable encodings. It does not establish that the physical-to-state bridge is unique or intrinsic.
:::

### Why the original proof fails

Let a physical flow be $\Psi_t:S\to S$ and a model flow be $F_t:X_7\to X_7$. Compatibility means

$$
G\Psi_t=F_tG.
$$

This is semiconjugacy, not an inverse-observation theorem. A constant $G(s)=\rho_*$ satisfies it whenever $\rho_*$ is stationary. Distinct stationary states with different spectra give compatible encodings unrelated by any unitary. The [explicit counterexample and corrected rigidity theorem](/docs/proofs/categorical/uniqueness-theorem#теорема-единственности) show that the universal claim fails within the numerical model, without deciding any empirical question about consciousness.

Even for an injective $G$, the map $s\mapsto[G(s)]_{G_2}$ need not be injective: a quotient deliberately identifies states on a common orbit. Forward-flow uniqueness and existence of an octonionic structure do not repair either gap. An independent empirical bridge is required to identify the state of a physical system.

### Theorem T-223′ (conditional invariance) [T]

Fix two encodings $G_1,G_2:S\to X_7$ satisfying the **reversible-identification hypothesis (RI)** of the [representation theorem](/docs/proofs/categorical/uniqueness-theorem#теорема-единственности): each is bijective onto $X_7$, their comparison and its inverse extend to linear CPTP maps, and the chosen unitary lift preserves the specified octonionic three-form. Then

$$
G_2(s)=UG_1(s)U^\dagger\quad\text{for a fixed }U\in G_2.
$$

Consequently the numerical orbit $[G_i(s)]_{G_2}$ is independent of the choice between these **two encodings meeting RI**. If their frames, $E$ axes, readouts and self-models are also transported covariantly,

$$
\mathcal B_2=U\mathcal B_1,\quad P_{E,2}=UP_{E,1}U^\dagger,\quad
M_2(U\rho U^\dagger)=UM_1(\rho)U^\dagger,
$$

then corresponding values of $P$, $R=1/(7P)$, $R_M$, $\Phi$, $\mathrm{Coh}_E$ and each covariantly specified differentiation diagnostic coincide. A predicate made from their corresponding threshold inequalities therefore has the same value. If one insists on a single fixed frame instead of transporting it, the allowed transformations must lie in its common stabilizer; a generic $G_2$ action does not preserve $\Phi$ or the $E$ axis.

*Proof.* The corrected rigidity theorem gives $U$. Purity and Frobenius distance are invariant under unitary conjugation; hence so are $R$ and $R_M$ under the displayed equivariance. In transported bases the matrix entries are identical, proving invariance of the frame-dependent ratios and of any specified covariant readout. The predicate conclusion follows term by term. $\square$

This proves coordinate invariance under stated comparisons, not RI itself. No categorical law supplies RI for arbitrary experimental encoders. An alternative causal readout can fail RI while remaining a physically meaningful measurement or coarse-graining. Failure to satisfy the chosen UHM model is not a proof that a readout has no causal or physical content.

### Intrinsic feedback versus identification

Once a map $M:X_7\to X_7$ is chosen, computing $M(\Gamma)$ from $\Gamma$ needs no extra runtime observer. Nevertheless, choosing $G$, $M$, the frame and their phenomenal interpretation remains model data. The logical support reflector in a slice is a different construction; it does not identify a hardware system's numerical state or turn $M$ into a categorical left adjoint.

The scalar $R=1/(7P)$ measures proximity to $I_7/7$ in the stated normalisation. The quality $R_M=1-\|\Gamma-M(\Gamma)\|_F^2/P$ measures agreement with a specified numerical model and can be negative. Neither scalar proves uniqueness of the physical encoder or validates a phenomenal bridge. A numerical fixed point follows from Brouwer for a continuous state map on $X_7$; Cartesian closedness alone does not furnish Lawvere's weak point-surjectivity hypothesis. The former appeal to Lawvere as proving the bridge's sole or inevitable externality is withdrawn [✗].

### Simulation accuracy and the SYNARC question

A simulator produces model matrices. Accuracy against an exact model trajectory and identification with the simulator hardware's own physical state are different claims. Suppose an exact ODE $\dot\rho=V(\rho)$ is Lipschitz with constant $L$ on a common domain, and an approximate state path $\widetilde\rho$ has initial error $e_0$ and residual $\|\dot{\widetilde\rho}-V(\widetilde\rho)\|\leq\epsilon$. Then

$$
\|\widetilde\rho(t)-\rho(t)\|\leq e^{Lt}e_0+\epsilon\frac{e^{Lt}-1}{L},
$$

with the fraction replaced by $t$ when $L=0$. This is the Grönwall estimate [T]; a per-step floating-point error alone does not establish a uniform $O(\epsilon)$ trajectory error for arbitrary duration.

On a domain where each continuous diagnostic $a_j$ has Lipschitz constant $K_j$, a predicate cut $a_j>c_j$ is stable if its signed margin exceeds $K_j\|\widetilde\rho-\rho\|$. Discontinuous gates, eigenbasis selections and discrete depth labels require separate stability conditions. In particular, numerical agreement of $P,R,\Phi$ is not a measurement of $G_{\mathrm{hardware}}$. Whether SYNARC or another implementation instantiates the proposed phenomenal bridge remains an empirical/model-identification question [Pr/H]. The mathematical predicates alone prove neither instantiation nor its absence.

### What remains to test

1. Specify a causal/measurement bridge $G$ and its intervention domain independently of a desired consciousness verdict.
2. Establish observational completeness or demonstrate which state distinctions remain unidentified.
3. Compare independently calibrated encoders and test RI, covariance of the declared frame, and prediction accuracy.
4. Validate the phenomenal interpretation separately from fitting numerical dynamics.

A pair of dynamically compatible but inequivalent encoders already refutes the old universal theorem; it is not automatically a refutation of the conditional T-223′, whose premises are stronger. A violation of invariance under encodings actually satisfying RI and the declared frame covariance would contradict the replacement's mathematical assumptions or derivation.

**External context.** Lerchner's [primary paper](https://deepmind.google/research/publications/231971/) argues that abstract computation needs an interpretation and separates simulation from instantiation. Piccinini's [mechanistic account](https://profiles.umsl.edu/en/publications/computation-without-representation) proposes functional individuation of computational states without semantic representation. These are philosophical positions, not established premises of the theorem above. UHM's conditional invariance result addresses coordinate ambiguity only; it does not settle the dispute by defining all competing readouts as physically vacuous.

**Dependencies and status.** T-223′ uses the explicit RI theorem and ordinary unitary covariance [T at RI]. Existence, empirical adequacy and phenomenal interpretation of the encoder remain [H/Pr]. The former AP→Fano→seven dimensions cascade, universal T-42a/T-123 rigidity, automatic frame pinning, automatic CPTP self-model, and Lawvere bridge necessity are not dependencies of the replacement.

---

## 18. Remaining clarifications {#clarifications}

Three additional gap-closures complete the UHM foundational cleanup; they do not warrant new theorem numbers but require explicit documentation.

### 18.1. A4 eigenvalue distinctness clarification {#a4-distinctness}

**Explicit addition to Axiom 4 (Scale).** A4 currently says $\omega_0 = \lambda_\mathrm{min}(H_\mathrm{eff}) > 0$. A hidden assumption is that $H_\mathrm{eff}$ has **simple** spectrum (all eigenvalues distinct). This is required by:
- Well-definedness of the temporal modality $\triangleright: |k\rangle \to |k+1 \bmod 7\rangle$ (needs distinct eigenstates to define the $\mathbb Z_7$-shift action);
- Berry-phase calculations on $\mathcal D \setminus \Sigma$ where $\Sigma$ is the degenerate-spectrum locus;
- Uniqueness of ground state in the Page–Wootters clock factor.

**A4 refined**: $H_\mathrm{eff}$ has **simple spectrum** (all 7 eigenvalues distinct), with $\omega_0 = \lambda_\mathrm{min}(H_\mathrm{eff}) > 0$. Simple spectrum is generic (codimension $\geq 1$ stratum is degenerate) and holds for physically relevant holons by spectral transversality.

### 18.2. $f_0$ zeta-regularisation well-definedness {#f0-zeta}

**Claim**: The formula $f_0 \Lambda^4 = \frac{1}{7}\bigl[V_\mathrm{Gap}^{\min} + \tfrac12 \zeta'_{H_\mathrm{Gap}}(0)\bigr]$ (T-70) involves $\zeta'(0)$, which is generally a delicate analytic-continuation object. In UHM's finite-dimensional setting, it reduces to an elementary computation.

**Proof of well-definedness**: $H_\mathrm{Gap}$ is a finite-dimensional Hermitian operator (on $(S^1)^{21}/G_2$, effectively $\dim = 7$ after $G_2$-reduction). Its spectral zeta function is

$$
\zeta_{H_\mathrm{Gap}}(s) = \sum_{k=1}^{r} \lambda_k^{-s}
$$

where $r$ is the rank and $\{\lambda_k\}$ are positive eigenvalues (with multiplicities for degeneracies if any; for simple spectrum $r = \dim$). This is a **finite sum** for all $s \in \mathbb C$, hence entire (no poles). Therefore

$$
\zeta'_{H_\mathrm{Gap}}(0) = -\sum_{k=1}^{r} \log \lambda_k = -\log \prod_{k=1}^{r} \lambda_k = -\log \det(H_\mathrm{Gap})
$$

is well-defined and finite. No regularisation ambiguity. The formula $f_0$ is thus a **rational algebraic expression** in the eigenvalues of $H_\mathrm{Gap}$, not a transcendentally-regularised object.

### 18.3. Bures stratified-site handling {#bures-stratification}

**Claim**: Bures metric has degeneracies on the boundary of $\mathcal D(\mathbb C^7)$ where $\Gamma$ is rank-deficient. This is handled via the **stratified site** (Ayala–Francis–Rozenblyum 2017).

**Explicit treatment**: decompose $\mathcal D(\mathbb C^7)$ into rank-strata:

$$
\mathcal D(\mathbb C^7) = \bigsqcup_{r=1}^{7} \mathcal D_r, \qquad \mathcal D_r := \{\Gamma : \mathrm{rank}\,\Gamma = r\}.
$$

- On each **open stratum** $\mathcal D_r$, the Bures metric is non-degenerate (rank-$r$ Fisher metric).
- Between strata, Bures distance extends continuously (Uhlmann 1976) but the metric tensor degenerates.
- The viability condition $P > P_\mathrm{crit} = 2/7$ restricts attention to strata $r \geq 2$ ($D_{\min} = 2$ [D], T-151); the conscious window is entirely interior to $\mathcal D_7$.

**Update 2026-09-25.** The strata are submanifolds of dimension $14k - k^2 - 1$ whose shapes are the Grassmannians $\mathrm{Gr}_k(\mathbb{C}^7)$, and the whole stratified space is an object of the differentially cohesive $\mathrm{SynthDiff}\infty\mathrm{Grpd}$ ([T-185 (ii′)](/docs/proofs/categorical/cohesive-closure#t-185-ii-prime)); no separate stratified site is needed.

**Consequence**: all viable-state theorems operate on the **interior stratum** $\mathcal D_7$, where Bures is smooth and all metric-geometric arguments are valid. Boundary handling is not needed for consciousness-related claims; it is needed only for pathological-state or thermal-death analysis (conducted via the Ayala–Francis–Rozenblyum stratified machinery).

---

## 19. Updated summary table {#summary-final}

| # | Theorem / Protocol | Previous status | New status | Method |
|---|---|---|---|---|
| T-210 | Topology-refinement implication withdrawn; selected pair-score identity survives | [✗] former universal claim | See corrected section above |
| T-211 | PhysTheory coherences | [T] deferred | **[T]** as the Grothendieck construction (2026-09-25; before that [C at T-119], and "[T] verified" by a full embedding, now [✗]) | HTT 3.2 |
| T-212 | U-projection | [T] unnamed | **[T] $G_2$-twirl**; Rh identification [✗] (read "[T] defined", then "[C] defined", until 2026-09-25) | Schur + Haar |
| T-213 | Representability and 138-bit bound withdrawn; minimal Kraus count equals Choi rank | [✗] former universal claim | See corrected section above |
| T-214 | Internal-bridge no-go withdrawn; phenomenal identification remains an input | [✗] former universal claim | See corrected section above |
| T-215 | Cross-layer identity | [C] | **[T]+[D]** | Conventional choice |
| T-216 | Analytical ε<sub>eff</sub> | [H] no formula | **[C at (SV)]** (listed [T at T-64] until 2026-09-25) | Closed form |
| **T-217** | 3-truncation construction [T]; operational L3 bridge [Pr] | Truncation reflector / fundamental 3-groupoid | Old forced K=4 and universal threshold proof [✗]; corrected §11 |
| **T-218** | Singular-classifying-space Kan construction [T] | Topological horn retraction | Cognitive ceiling / 3-coskeleton claim [✗]; realization bridge [Pr] |
| **T-219** | **SUSY Λ-suppression** | **[H] invalid 7+7** | **[H]** (listed [T at T-64] until 2026-09-25) | **Sector product $\varepsilon^{12}$** |
| **T-220** | Exact representation/space comparisons | Universal no-reduction claim withdrawn [✗] | [T at specified comparisons] | Two typed obstructions; constant, forgetful and restricted-group readout functors remain possible |
| **T-221** | Local equality in a supplied sheaf model | Universal noncompossibility/route-selection claim withdrawn [✗] | [T at sheaf equality]; phenomenal bridge [I] | Exclusion requires the equality subobject to be empty; local semantics does not select a philosophical route |
| **T-222** | **Resource geometry of the viable window** | open (external QRT critique) | **[T]** (restated 2026-09-26) | **Majorization: no resource optimum in the window, the Rényi family splits at $\alpha = 2$, no terminal object; the former "Lawvere fixed point = Pareto optimum, MRQT-complete" is [✗]** |
| T-223 | Universal Putnam foreclosure withdrawn; RI-conditional invariant comparison survives | [✗] former universal claim | See corrected section above |
| §18.1 | A4 simple spectrum | implicit | **Explicit** | Spectral transversality |
| §18.2 | $f_0$ ζ'(0) | delicate | **Elementary** | Finite-dim spectral zeta |
| §18.3 | Bures boundary | not addressed | **Stratified site** | Ayala–Francis–Rozenblyum |
| §8 | Λ-deficit programme | "computational task" | **Spec complete** | HMC on $(S^1)^{21}/G_2$ |
| §9 | π<sub>bio</sub> protocol | [H] specific | **Spec complete** | EEG/fMRI/HRV |

**Current scope:** valid constructions and conditional results are listed individually; there is no global certificate of mathematical closure.

~~**No open mathematical or categorical gaps remain in UHM's foundational framework.**~~ Retracted [✗] (2026-09-25): the rows marked [C] and [H] above are open mathematical conditions. The framework's own inputs listed here until 2026-09-25 are settled: the first-order condition and Poincaré duality of T-119, on which T-120 and T-121 rest, by the restatement of T-119, which computes the spatial spectrum (T-119, T-120 and T-121 are [T] since); the orientation (Alt) of T15 by the [canonical-orientation theorem](/docs/proofs/minimality/theorem-octonionic-derivation#каноническая-ориентация). T-211 was listed here too; its recheck of 2026-09-25 showed that it never used them; clause (iii) of the earlier T-221 rested on them, the corrected T-221 of 2026-09-25 does not. T-221 now states local equality in a specified sheaf model; the former universal first-person noncompossibility and selection of a relationalist route are withdrawn [✗], with a philosophical bridge remaining [I]; T-222 answers the QRT-completeness external critique — negatively since 2026-09-26: the viable window selects no resource optimum; T-223 answers the Lerchner Melody-Paradox / Putnam-triviality external critique — the three principal recent external critiques (quantum-metaphysics no-go, resource-theoretic completeness, computational-functionalist triviality) each receive a structured answer; the earlier phrasing "closes … UHM is now closed against all three" is withdrawn with the sentence above.

**Strictly remaining** (all explicitly non-mathematical):
- Numerical computation of Λ (§8) — bounded HPC task
- Empirical calibration of π<sub>bio</sub> (§9) — experimental programme
- Phenomenal identification [P/I] remains an input; the former T-214 no-go is withdrawn.
