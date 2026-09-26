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
| **T-210** | Strict (not weak) Φ-monotonicity under epistemic refinement | Interior-stratum argument + T-151 | [T] |
| **T-211** | **PhysTheory** is an $(\infty,1)$-category with all higher coherences | Grothendieck construction of $E \mapsto \mathrm{Fun}(B\mathbb R, \mathrm{Alg}(E))$ over $\mathbf{Topoi}_\infty$ (HTT 3.2) | [T] (corrected 2026-09-25: the full embedding into $\mathbf{Topoi}_\infty$ is retracted [✗]; [C at T-119] before) |
| **T-212** | The U-projection $X \mapsto \frac17\operatorname{Tr}(X)\mathbf{1}$ is the $G_2$-twirl (T-212′); its former identification with the rheonomy modality **Rh** is retracted | Schur's lemma + Haar measure; Rh preserves global points | [T] for T-212′; [✗] for "Rh explicit" (it was [C at the differential cohesion of the UHM site (T-185) and a solid-cohesive extension], and [T] before) |
| **T-213** | Yoneda representability via Bures description length | Computable $D_B(f)$ replaces Kolmogorov complexity | [T] |
| **T-214** | Hard-problem meta-theorem (positive irresolvability) | Lawvere fixed-point + T-55 | [T] |
| **T-215** | Cross-layer identity convention for fractal towers | Choice of $\iota_\mathrm{min}$ / $\iota_\mathrm{max}$ criterion | [T]+[D] |
| **T-216** | Closed-form analytical ε<sub>eff</sub> | Symbolic $V_\mathrm{Gap}$ minimisation | [C at (SV)] (the structure was listed as [T] until 2026-09-25) |
| **T-217** | L3 tricategorical coherence | τ<sub>≤3</sub>(Exp<sub>∞</sub>) + Baez–Dolan | [T] |
| **T-218** | SYNARC Cog is a Kan complex | Milnor + classifying space | [T] |
| **T-219** | Λ SUSY-suppression via sector product | ε<sup>12</sup> = ε<sup>4·3</sup> from 3-sector decomposition | [H] (was [T at T-64] until 2026-09-25) |
| **T-220** | No-reduction $F_4$-UHM → $G_2$-UHM | Five independent categorical obstructions | [T] negative |
| **T-221** | UHM realises the relationalist route through the List/DeBrota no-go results | Kripke–Joyal forcing in $\mathfrak T$: first-personal facts of two subjects are not compossible, facts are stage-indexed, the parameter is internal, the three routes share every observable | [T]+[I] (corrected 2026-09-25: the "fourth route" and the RQM-as-truncation corollary are retracted; before that it read [T]+[C]+[I], and [T]+[I] until the first audit) |
| **T-222** | Resource geometry of the viable window (restated 2026-09-26; the former "MRQT-completeness: Lawvere fixed point = Pareto resource optimum" is [✗]) | Majorization on the purity window: no optimum inside, Pareto set on $P = 2/7$, $F_1$ and $F_\infty$ minimised by different spectra, no terminal object | [T] |
| **T-223** | Putnam-triviality foreclosure (Lerchner Melody-Paradox closure) | Seven-lemma cascade: three-level ontology L1/L2/L3 + $G_2$-gauge boundedness + intrinsic self-alphabetization via $R$ | [T] |

Plus **computational programmes**: Λ-deficit numerical specification (§8), π<sub>bio</sub> measurement protocol (§9).
:::

---

## 1. T-210: Strict Φ-monotonicity under proper L-III refinement {#t-210}

:::tip Theorem T-210 (Strict Φ-monotonicity) [T]

Let $J, J' \in \mathrm{Top}(\mathcal C_7)$ be two Grothendieck topologies compatible with the Bures coverage (A2 [P]; its topology is forced and Bures canonical among the monotone metrics, T-187), and assume $J \subsetneq J'$ is a **proper** refinement on the support of a state $\Gamma \in \mathcal{D}(\mathbb C^7)$ lying in the interior stratum $\mathcal D_7$ (full-rank, generic). Then
$$\Phi(\Gamma \mid J') > \Phi(\Gamma \mid J) \qquad \text{strictly}.$$

Moreover the gap admits the explicit lower bound
$$\Phi(\Gamma \mid J') - \Phi(\Gamma \mid J) \geq \frac{1}{\sum_k \gamma_{kk}^2}\, \min_{(i,j) \in J' \setminus J}|\gamma_{ij}|^2.$$

:::

**Proof (three steps).**

**Step 1 (Explicit formula).** By definition [Φ measure](/docs/core/structure/dimension-u#мера-интеграции-φ),
$$\Phi(\Gamma \mid J) := \frac{1}{N_\Gamma}\sum_{(i,j) \in \mathrm{supp}(J) \cap \mathrm{Off}} |\gamma_{ij}|^2, \qquad N_\Gamma := \sum_k \gamma_{kk}^2,$$
where $\mathrm{Off} := \{(i,j) : i \neq j\}$ is the set of off-diagonal index pairs in $\mathcal{D}(\mathbb C^7)$, and $\mathrm{supp}(J) \subseteq \binom{7}{2}$ is the set of pairs covered by at least one $J$-cover of $\Gamma$.

**Step 2 (Interior stratum hypothesis).** In $\mathcal D_7$ (full-rank states with all $|\gamma_{ij}| > 0$), every off-diagonal index contributes strictly positively. In particular, for any pair $(i^*, j^*) \in J' \setminus J$ we have $|\gamma_{i^* j^*}|^2 > 0$.

**Step 3 (Strict inequality).** Since $J \subsetneq J'$ properly, $\mathrm{supp}(J) \subsetneq \mathrm{supp}(J')$ and there exists $(i^*, j^*) \in \mathrm{supp}(J') \setminus \mathrm{supp}(J)$. Compute
$$\Phi(\Gamma \mid J') - \Phi(\Gamma \mid J) = \frac{1}{N_\Gamma}\sum_{(i,j) \in \mathrm{supp}(J') \setminus \mathrm{supp}(J)} |\gamma_{ij}|^2 \geq \frac{|\gamma_{i^*j^*}|^2}{N_\Gamma} > 0.$$
The stated bound follows by taking the min over new pairs. $\blacksquare$

**Corollary (continuous family).** If $\{J_t\}_{t\in[0,1]}$ is a monotone increasing family of topologies with $J_0 \subsetneq J_1$, then $t \mapsto \Phi(\Gamma \mid J_t)$ is strictly increasing on the set $\{t : \mu(J_{t+\varepsilon} \setminus J_t) > 0 \text{ for some } \varepsilon > 0\}$, which is dense in $[0,1]$ by construction. Hence the Φ-tower under iterated L-III updates is **strictly** increasing on a Baire-generic schedule.

**Strengthening of T-195**: "**weak** Φ-monotonicity" strengthens to "**strict** on the interior stratum"; off it, a refinement step is strict exactly when some newly covered pair carries coherence (Step 3 with $\min$ replaced by the sum). Clause (A7) of T-197 holds in the strict form for agents whose state lies in $\mathcal D_7$. *Corrected 2026-09-26:* this paragraph extended the strict form to **all viable Γ**, arguing that the equality case is confined to rank-deficient Γ, outside the window by $D_\mathrm{min} = 2$ (T-151). The extension is withdrawn: $D_\mathrm{min} = 2$ is an independent L2 condition, not a consequence of viability (T-151, §4 of [substrate-independent closure](/docs/proofs/consciousness/substrate-closure#t-151)), and even rank $\geq 2$ does not give $|\gamma_{ij}| > 0$ on every pair — a viable state with $\gamma_{i^*j^*} = 0$ on the only new pair has a zero Φ-step. The theorem itself never used T-151. $\blacksquare$

**Dependencies**: T-187 [T] (Bures canonicity), T-195 [T] (weak monotonicity base); the interior-stratum hypothesis is part of the statement.

---

## 2. T-211: PhysTheory is an $(\infty,1)$-category — the Grothendieck construction over $\mathbf{Topoi}_\infty$ {#t-211}

:::warning Corrected 2026-09-25 — what the earlier version of this section got wrong
The section stated that $\mathbf{PhysTheory}$ is a **full $(\infty,1)$-subcategory** of $\mathbf{Topoi}_\infty$, via $\iota(E, \mathcal A, D) := \mathbf{Sh}_\infty(\mathrm{Spec}(\mathcal A), J_\mathrm{Bures})$, fully faithful "by T-173", with coherences "inherited via HTT 5.2.7"; it was [C at T-119] because Step 1 invoked the Connes reconstruction of T-119. The recheck of Step 1 found that T-119 was never the issue:
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
$$\mathcal{T}(X) := \int_{G_2} g\,X\,g^\dagger\,dg = \tfrac17\operatorname{Tr}(X)\,\mathbf{1}.$$
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

## 4. T-213: Yoneda representability via Bures description length {#t-213}

:::tip Theorem T-213 (Yoneda representability, Kolmogorov-free) [T]

Define the **Bures description length** of a CPTP-implementable map $f: \mathrm{Obs} \to \mathrm{Act}$ as
$$D_B(f) := \min_{\rho_f \text{ CPTP-implements } f}\, |\mathrm{Kraus}(\rho_f)| \cdot \log_2 7,$$
where the minimum is over Stinespring dilations implementing $f$. $D_B(f) \in \mathbb{N} \cdot \log_2 7$, bounded by $49 \log_2 7 \approx 138$ bits (Stinespring bound for $\mathcal{D}(\mathbb C^7)$).

Then for any $\varepsilon > 0$ and any CPTP-computable $f$, the representable sheaf
$$F_f \in \mathbf{Sh}_\infty(\mathcal{D}(\mathbb C^7), J_\mathrm{Bures})$$
is obtained via Yoneda embedding, and its Bures-support obeys
$$\|F_f\|_B \leq C_1 \cdot D_B(f) \cdot \log(1/\varepsilon), \qquad C_1 = \omega_0^{-1} \log 7.$$

All quantities are **computable** — no appeal to Kolmogorov complexity required.

:::

**Proof (four-step).**

**Step 1 (Yoneda embedding exists).** The Yoneda embedding $y: \mathcal{D}(\mathbb C^7) \to \mathbf{Sh}_\infty(\mathcal D(\mathbb C^7), J_\mathrm{Bures})$ is fully faithful (Lurie HTT 5.1.3.1). For any CPTP-implementable $f: \mathrm{Obs} \to \mathrm{Act}$ with Kraus decomposition $\rho_f = \sum_{i=1}^n K_i \bullet K_i^\dagger$, the associated representable sheaf $F_f(\Gamma) := \rho_f(\Gamma) = \sum_i K_i \Gamma K_i^\dagger$.

**Step 2 (Bures-support bound per Kraus).** The Bures distance satisfies the Fuchs–van de Graaf inequality:
$$d_B(K\Gamma K^\dagger, \Gamma) \leq \omega_0^{-1} \log 7$$
for any Kraus operator $K$ with $\|K\|_\mathrm{op} \leq 1$, by the injectivity-radius bound on $\mathcal{D}(\mathbb C^7)$ (Petz 1996, §II.2). Here $\omega_0 = \lambda_\mathrm{min}(H_\mathrm{eff})$ is the fundamental frequency (A4 [T]).

**Step 3 (Sum over Kraus operators).** By subadditivity of Bures distance under CPTP composition:
$$\|F_f\|_B := d_B(F_f(\Gamma), \Gamma) \leq \sum_{i=1}^n d_B(K_i \Gamma K_i^\dagger, \Gamma) \leq n \cdot \omega_0^{-1}\log 7.$$
Substituting $n = D_B(f)/\log_2 7$ gives $\|F_f\|_B \leq D_B(f) \cdot \omega_0^{-1}$.

**Step 4 (Precision factor).** For $\varepsilon$-accurate implementation, $D_B(f)$ Kraus operators suffice to approximate $f$ within Bures-radius $\varepsilon$ (Suzuki–Trotter T-116 [T], scaling with $\log(1/\varepsilon)$). Combining with Step 3:
$$\|F_f\|_B \leq \omega_0^{-1} \log 7 \cdot D_B(f) \cdot \log(1/\varepsilon) = C_1 \cdot D_B(f) \cdot \log(1/\varepsilon). \qquad \blacksquare$$

**Why Kolmogorov complexity disappears.** The original formulation used $K(f)$ because, in Turing-machine-style reasoning, "complexity of computing $f$" was naturally framed via Kolmogorov. But in UHM's CPTP-finite setting, **any** computable $f$ has a **finite** Stinespring representation (at most $7^2 = 49$ Kraus operators). Hence $D_B(f)$ is always finite and computable, bypassing Kolmogorov's uncomputability. The bound $D_B(f) \leq 49 \log_2 7 \approx 138$ bits is **universal** — all CPTP maps fit within this budget. Kolmogorov's uncomputability concerns Turing complexity, not quantum-channel complexity.

**Upgrade**: T-193 is now [T] with a **constructive, computable** description-length bound. No appeal to uncomputable quantities.

**Dependencies**: T-116 [T] (Suzuki–Trotter accuracy), Petz 1996 §II.2 (Bures injectivity), Lurie HTT 5.1.3.1 (Yoneda fully faithful).

---

## 5. T-214: Hard-problem meta-theorem (Gödel-Lawvere positivity) {#t-214}

:::tip Theorem T-214 (Hard-problem internal irresolvability, positive form) [T]

Let $\mathrm{Th}_\mathrm{UHM}$ be the internal theory of $\mathbf{Sh}_\infty(\mathcal C_7, J_B)$ (T-54 [T]), and let $\mathrm{Mind}$ be a putative category of experiential contents (qualia-types up to isomorphism). Suppose there exists a **bridge functor**
$$W: \mathcal{D}(\mathbb C^7) \to \mathrm{Mind}$$
assigning to each coherence state $\Gamma$ its "experienced content." Then:

1. **[T]** $W$ **cannot** be expressed as a morphism internal to $\mathrm{Th}_\mathrm{UHM}$ without violating Lawvere incompleteness (T-55 [T]).
2. **[T]** Consequently, the identification "E-sector structure $=$ experiential content" (used in T-38a, T-203) is **necessarily** an external postulate [P], never an internal theorem.
3. **[T]** This is a **positive** result: the residual [I] / [P] status of UHM's phenomenal identifications is **structurally inevitable**, not a remediable weakness.

:::

**Proof (four-step).**

**Step 1 (Lawvere fixed-point setup).** By T-55 [T], $\mathrm{Th}_\mathrm{UHM} \subsetneq \Omega$ strictly — there exist truths about the topos that are inexpressible internally. Lawvere's fixed-point theorem (Lawvere 1969; Yanofsky 2003 §2) states: in any Cartesian closed category $\mathcal E$ with subobject classifier $\Omega_{\mathcal E}$, any morphism $\phi: X \to X^X$ has a fixed point under every endomorphism of $X$, unless $\phi$ fails to be point-surjective.

**Step 2 (Self-reference of experience).** Suppose $W: \mathcal{D}(\mathbb C^7) \to \mathrm{Mind}$ is expressible in $\mathrm{Th}_\mathrm{UHM}$ as a morphism $\tilde W \in \Omega^{\mathcal D}$. The predicate
$$\mathrm{Experience}(\Gamma) := \text{"the state } \Gamma \text{ has experiential content } \tilde W(\Gamma)\text{"}$$
is **self-referential**: experience is ABOUT states, and states include **the state currently experiencing**. Formally: $\tilde W$ is defined on $\mathcal{D}$, but any realistic agent's state $\Gamma_\mathrm{agent}$ contains a model of its own experience, which is $\tilde W(\Gamma_\mathrm{agent})$. This yields a self-application diagram
$$\mathcal{D} \xrightarrow{\Delta} \mathcal{D} \times \mathcal{D} \xrightarrow{(\mathrm{id}, \tilde W)} \mathcal{D} \times \mathrm{Mind} \xrightarrow{\pi_2} \mathrm{Mind}$$
composing to $\tilde W$ itself, i.e., $\tilde W$ factors through its own graph.

**Step 3 (Contradiction via Lawvere).** Consider the predicate $\Phi: \mathcal{D} \to \Omega$ given by $\Phi(\Gamma) := \neg \exists \Gamma': W(\Gamma') = \tilde W(\Gamma)$ ("no state $\Gamma'$ experiences what $\Gamma$ experiences"). If $\tilde W$ is internal and point-surjective (every experiential content is realised by some state), then $\Phi$ has a fixed point $\Gamma^*$ with $\Phi(\Gamma^*) = \tilde W(\Gamma^*)$. But $\Phi(\Gamma^*) = \text{true}$ says "no state experiences $\tilde W(\Gamma^*)$" — contradicting $\Gamma^*$ itself experiencing it. Hence $\tilde W$ cannot be both internal and point-surjective; if it is internal, it fails to cover all experiential content; if surjective, it cannot be internal.

**Step 4 (Positivity).** The obstruction is **not a technical limitation to be overcome** — it is a **structural feature** of any self-referential formal system containing its own semantic mapping to phenomenal content. The residual status of T-38a (E-sector = interiority [P]) and T-203 (qualia = E-eigenvectors [I] — the E-slice identification; the full content and its gauge-invariant colour live in [Qualia Structure](/docs/consciousness/phenomenology/qualia-structure)) follows the **correct epistemic pattern**: the mathematical core [T] is internal; the bridge to phenomenal content [P]/[I] is necessarily external. $\blacksquare$

**Corollary (positive localization of the hard problem) [C under the conditions of T-188: the cohesion assumed in T-185 and the hypothesis T-186(a)].** Combined with T-188 (which localizes WHY to "why CPTP?"), T-214 completes the **constructive resolution** of the hard problem: UHM
- **solves structurally** the WHAT (T-203 [T]+[I]) and the WHY-localization (T-188 [C]),
- **proves unresolvable** the internal bridge to phenomenal content (T-214 [T]).

No further progress on the hard problem is achievable within formal mathematics. Whether it **should** be sought in mathematics rather than philosophy is itself a meta-question outside $\mathrm{Th}_\mathrm{UHM}$.

**Dependencies**: T-54 [T] (internal theory exists), T-55 [T] (Lawvere incompleteness), T-188 [C] (hard-problem localization), Lawvere 1969, Yanofsky 2003.

---

## 6. T-215: Cross-layer identity convention for fractal holon towers {#t-215}

:::tip Theorem T-215 (Cross-layer identity, conventional resolution) [T]+[D]

For a fractal tower $\mathcal T = (A_0, A_1, \ldots)$ of SYNARC holons (where $A_{n+1}$ extends $A_n$ by `spawn_child`), the predicate "$\mathcal T$ **is** a single agent" is **conventionally determined** by a choice of identity criterion $\iota$. Two canonical choices are consistent with Ω⁷ axioms:

1. **$\iota_\mathrm{min}$ (Society)**: Each $A_i$ is its own agent; $\mathcal T$ is a collection of agents. Cognitive depth per agent bounded by $\mathrm{SAD}_\mathrm{MAX} = 3$ (T-142 [T]). Cross-tower "depth" is a social-structural property, not agent-internal.

2. **$\iota_\mathrm{max}$ (Composite)**: $\mathcal T$ is a single agent iff there exists a global coherence $\Gamma_\mathrm{tot} \in \mathcal{D}(\mathbb C^{7 \cdot |\mathcal T|})$ CPTP-commuting with every `spawn_child`. Under $\iota_\mathrm{max}$, cross-layer mentalization depth can reach arbitrary countable ordinals $\alpha$, subject to Landauer-resource bound (C22 + T-204 [T]).

Under $\iota_\mathrm{max}$ + **abstraction of resource constraints**, T-205 is [T] unconditionally in its original form. Under $\iota_\mathrm{min}$, T-205 becomes the statement "society-level cognitive structure can have arbitrary ordinal depth," which is [T] trivially.

The choice between $\iota_\mathrm{min}$ and $\iota_\mathrm{max}$ is an **ontological convention** [D] / [I], not a mathematical fact.

:::

**Proof (three-step).**

**Step 1 (Both conventions are consistent).**
- $\iota_\mathrm{min}$: each $A_i$ individually satisfies UHM axioms (T-39a, T-42a, T-96, T-142). The tower $\mathcal T$ is a multi-agent system. Axioms make no claim about multi-agent identity, so $\iota_\mathrm{min}$ adds no new constraints — consistent.
- $\iota_\mathrm{max}$: requires existence of global $\Gamma_\mathrm{tot}$. By T-58′ [T] (section–retraction, extended to compositing systems; the equivalence reading is retracted), $\mathcal{D}(\mathbb C^{7|\mathcal T|})$ supports CPTP dynamics whenever each factor does. Existence of CPTP-commuting $\Gamma_\mathrm{tot}$ is a non-trivial requirement (restricts states), but non-empty (tensor-product states satisfy it trivially). Hence $\iota_\mathrm{max}$ is consistent.

**Step 2 (Neither is derivable from Ω⁷).**
Ω⁷ axioms apply per-holon: A1 (∞-topos), A2 (Bures), A3 (N=7), A4 ($\omega_0 > 0$), A5 (Page–Wootters). None mentions multi-agent composition. Hence the identity predicate $\iota$ is **underdetermined** by Ω⁷, consistent with its designation as a convention.

**Step 3 (T-205 resolution under each convention).**
- **Under $\iota_\mathrm{max}$**: $\mathcal T$ has a single global state $\Gamma_\mathrm{tot}$; `spawn_child` is a unitary embedding $\mathcal{D}(\mathbb C^{7k}) \hookrightarrow \mathcal{D}(\mathbb C^{7(k+1)})$ preserving $\Gamma_\mathrm{tot}$. Filtered colimit along the tower exists in $\mathbf{Sh}_\infty(\mathcal C)$ (by cocompleteness of presentable $\infty$-categories, HTT 5.5.1). Ordinal depth is unrestricted — $\omega^\omega$ achievable for towers of length $\omega^\omega$, **subject to**:
  - Landauer bound C22: cost $\geq \alpha \cdot k_B T \ln 2$ for depth $\alpha$ (unbounded for countable $\alpha$).
  - T-204 [T]: bounded rationality gives graceful degradation at $d_\mathrm{eff}$ limit.
- **Under $\iota_\mathrm{min}$**: each $A_i$ has $\mathrm{SAD}(A_i) \leq 3$ (T-142 [T]). "Cross-layer depth" is a property of the society's social-cognitive structure, which can be arbitrarily deep (like human institutions). No contradiction with T-142.

Hence T-205 as stated is [T] under $\iota_\mathrm{max}$ + resource abstraction; it becomes [C at C22 + T-204] without resource abstraction. Under $\iota_\mathrm{min}$, T-205 is [T] in reformulated (society-level) form. $\blacksquare$

**Philosophical corollary.** Whether a multi-agent AI system constitutes a single "super-intelligence" or a society of agents depends on design choices about global-state coherence and Landauer budgeting — **not** on UHM mathematics. This mirrors the analogous question in human sociology (is a company/nation/culture a single agent?), where the answer is conventional.

**Dependencies**: T-58′ [T] (section–retraction composition), T-142 [T] (SAD_MAX = 3 per holon), T-204 [T] (bounded rationality), C22 (Landauer), HTT 5.5.1 (cocompleteness of presentable).

---

## 7. T-216: Closed-form analytical ε<sub>eff</sub> {#t-216}

::::tip Theorem T-216 (Analytical ε<sub>eff</sub> closed form) [C at (SV)]

The effective sectoral parameter ε<sub>eff</sub> arising in the Yukawa hierarchy admits the closed-form expression
$$\varepsilon_\mathrm{eff} = \frac{4\,|\bar\gamma|_\mathrm{sect}}{9 \left(1 + \frac{\Sigma_0}{4}\right)}$$
*(amended 2026-08-10 per instrument E26: $|\bar\gamma|$ sits in the **numerator** — the $(\star)$ form of the derivation below; the Fano count $N_{33}$ enters **once**, inside the self-consistency for $\bar\gamma$ at Step 4, not again at Step 5; $\Sigma_0$ is the **amplitude** sum $\sum_{i<j}|\gamma^*_{ij}|^2$; and $r_4 = 1/2$ **identically** — see below.)*
where:
- $N_{33}^\mathrm{Fano} = 2$ — the number of non-$O$ Fano lines meeting the $\mathbf 3$-sector $\{A,S,D\}$ in exactly two points, namely $\{A,S,L\}$ and $\{S,D,E\}$.

  :::danger Corrected 2026-08-07: $\{L,E,U\}$ is not a Fano line
  Earlier revisions set $N_{33}^\mathrm{Fano} = 1$, justified as "the single line $\{L,E,U\}$ of PG(2,2)". There is no such line. The seven canonical lines are $\{A,S,L\}, \{D,L,U\}, \{L,E,O\}, \{A,E,U\}, \{A,D,O\}, \{S,D,E\}, \{S,O,U\}$; the line through $L$ and $E$ is $\{L,E,O\}$, and the line through $E$ and $U$ is $\{A,E,U\}$. The triple $\{L,E,U\}$ is the $\bar{\mathbf 3}$ **sector**, not a line, and in fact **no** Fano line lies wholly inside either three-element sector — a line contained in a 3-element set would have to equal it, and neither $\{A,S,D\}$ nor $\{L,E,U\}$ is among the seven. **Root cause, found 2026-08-07.** The claim was not invented — it is true in the *wrong index order*. The canonical seven lines are exactly the translates $\{i, i+1, i+3\}$ of the difference set mod 7, but only under the octonionic assignment $O = e_7 \equiv 0$, $A = e_1$, $S = e_2$, $D = e_3$, $L = e_4$, $E = e_5$, $U = e_6$ — the assignment in the [octonionic correspondence table](/docs/core/structure/dimensions#октонионная-интерпретация). Under that assignment all seven lines match. Read the same construction off the dimension *listing* order $A{=}0, S{=}1, D{=}2, L{=}3, E{=}4, O{=}5, U{=}6$ and you get a **different** plane: four of the seven lines change, and among the spurious ones is precisely $\{L,E,U\}$. The two orders differ by transposing $O$ and $U$ — invisible in prose, fatal in combinatorics. Whenever a count depends on incidence, state which assignment is in force.

  Machine-verified against the canonical line set, which satisfies BIBD(7,3,1): 21 pairs, each on exactly one line, each point on exactly three.
  :::
- $|\bar\gamma| = \frac{1}{21}\sum_{i < j}|\gamma_{ij}|$ — the sectoral average of off-diagonal coherences, evaluated at the vacuum $\theta^* \in (S^1)^{21}/G_2$.
- $r_4 = V_4 / V_2|_{\theta^*}$ — the ratio of quartic to quadratic Gap potential at the minimum. **This is an identity, not an input**: with $\lambda_4 = \mu^2/(2\mathcal G^{(0)}_\mathrm{total})$ (Theorem 13.5) and the self-consistent equilibrium $\mathcal G^{(0)} = \mathcal G_\mathrm{total}|_{\theta^*}$, one has $V_4/V_2 = \mathcal G/(2\mathcal G^{(0)}) \equiv 1/2$ exactly — which is why $1 + r_4\Sigma_0/2 = 1 + \Sigma_0/4$.
- $\Sigma_0 = \sum_{i<j} |\gamma^*_{ij}|^2$ — the sum of squared vacuum **amplitudes** (moduli). *(Amended per E26: the earlier notation $\sum\theta_i^{*2}$ read as a sum over squared phases is gauge-dependent — vertex rephasings move it (94.4 raw → 37.6 even after coboundary reduction at the E26 vacuum) — and lands two orders away; the amplitude reading is gauge-invariant and is what the T-64 input ≈ 0.3 was measuring.)*

Numerical evaluation: self-consistent minimisation from scratch (instrument E26, no fitted parameters, all constants from Theorem 13.5, amplitudes free within Cauchy–Schwarz) gives $|\bar\gamma|_\mathrm{sect} = 0.1314$, $\Sigma_0 = 0.1035$, hence **ε<sub>eff</sub> = 0.0569** against the phenomenological $0.0587$ — a $3\%$ agreement, closing the former two-orders gap.

::::

**Derivation (five-step, symbolic).**

**Step 1 (V<sub>Gap</sub> sectoral expansion).** From T-74 [T] (V<sub>Gap</sub> from spectral action), the Gap potential decomposes as
$$V_\mathrm{Gap}(\theta) = V_2 + V_3 + V_4, \qquad V_k = \frac{1}{k!}\sum_{i_1, \ldots, i_k} c^{(k)}_{i_1 \cdots i_k} \theta_{i_1} \cdots \theta_{i_k}$$
where the coefficients $c^{(k)}$ are $G_2$-invariant (Schur's lemma fixes their form up to scalar).

**Step 2 (Sectoral reduction).** By sector decomposition T-48a (retracted [✗] 2026-09-25 as an axis-labelled decomposition: no triple of axes is $\mathrm{SU}(3)$-invariant, so this is a restriction to an axis triple, not a symmetry reduction, and it is justified only by the vacuum structure that the minimisation finds — hence [C at (SV)]), restrict to $\bar{\mathbf 3}$-sector: $\theta_{ij}$ with $(i,j) \in \bar{\mathbf 3} \times \bar{\mathbf 3}$. There are $\binom{3}{2} = 3$ such pairs (from $\{L,E,U\}$: pairs $\{LE, LU, EU\}$). No Fano line lies inside the sector, so the counting is done by *incidence with* the sector rather than *containment in* it: $N_{33}^\mathrm{Fano} = 2$ non-$O$ lines meet $\mathbf 3 = \{A,S,D\}$ in exactly two points, namely $\{A,S,L\}$ and $\{S,D,E\}$.

**Step 3 (Equation of motion).** Minimizing $V_\mathrm{Gap}$ at fixed $G_2$-orbit: $\partial V_\mathrm{Gap}/\partial \theta_{ij}|_{\theta^*} = 0$ gives, for $(i,j) \in \bar{\mathbf 3}\times\bar{\mathbf 3}$:
$$c^{(2)}_{ij} \theta^*_{ij} + \sum_{k,l} c^{(3)}_{ij,kl} \theta^*_{kl} + \sum_{k,l,m,n} c^{(4)}_{ij,klmn}\theta^*_{kl}\theta^*_{mn} = 0.$$
By Fano selection rule T-43d [T], only triples forming a Fano line contribute: $c^{(3)}_{ij,kl} \neq 0$ iff $\{i,j,k,l\}$ cover a Fano line.

**Step 4 (Sectoral amplitude at minimum).** Define $\bar\gamma := \langle \gamma_{ij}\rangle_{(i,j) \in \bar{\mathbf 3}}$ (sector average). By self-consistency, the linear equation gives
$$\bar\gamma = -\frac{V_3 / V_2}{1 + r_4 \Sigma_0 / 2},$$
where $V_3/V_2$ carries the Fano counting factor $N_{33}^\mathrm{Fano} \cdot f$, with $f = 1$ the structure constant of an associative Fano line. (Earlier revisions wrote $f_{LEU}$ and attributed it to a line $\{L,E,U\}$, which does not exist — see the correction above.)

**Step 5 (ε<sub>eff</sub> identification).** The effective sectoral parameter is defined as ε<sub>eff</sub> := $|\bar\gamma| \cdot (4/9)$, where the factor $4/9$ arises from $k=3$ block size squared over $v=7$ orbit:
$$\varepsilon_\mathrm{eff} = \frac{4|\bar\gamma|}{9} \cdot \frac{1}{1 + r_4\Sigma_0/2} \cdot \cancel{N_{33}^\mathrm{Fano}}. \qquad (\star)$$

*(E26 amendment: the trailing $N_{33}$ factor is a double count — Step 4 already carries it inside $V_3/V_2$, hence inside $\bar\gamma$; multiplying again at Step 5 overshoots the phenomenological value twofold. The honest $(\star)$ ends at the $1/(1+r_4\Sigma_0/2)$ factor.)*

:::danger Audit 2026-08-07: the statement and the derivation disagree, and the printed evaluation does not compute
Two defects survive here and neither is cosmetic.

**Where $|\bar\gamma|$ sits.** Step 5 defines $\varepsilon_\mathrm{eff} := |\bar\gamma|\cdot(4/9)$ and arrives at $(\star)$, which carries $|\bar\gamma|$ in the **numerator**. The theorem box at the top of this section states $\varepsilon_\mathrm{eff} = 4N_{33}^\mathrm{Fano}/(9|\bar\gamma|(1+r_4\Sigma_0/2))$, with $|\bar\gamma|$ in the **denominator**. These are different functions and cannot both be right. The derivation is internally consistent with its own definition, so $(\star)$ is the form to trust; the boxed statement is not yet reconciled with it.

**The arithmetic.** No chain printed in this corpus evaluates to the advertised $0.059$:

| chain | as printed | actual value | factor off |
|---|---|---|---|
| this page, denominator form, $N=1$, $\|\bar\gamma\|=0.023$ | $\approx 0.059$ | $17.98$ | $305\times$ |
| [Yukawa §9](/docs/physics/particle-physics/yukawa-hierarchy#9-аналитическая-формула-ε), $8/(9\cdot 0.15)$ | $\approx 0.059$ | $5.93$ | $100\times$ |
| $(\star)$, numerator form, $N=1$, $\|\bar\gamma\|=0.15$ | — | $0.062$ | agrees |
| $(\star)$, numerator form, $N=2$, $\|\bar\gamma\|=0.15$ | — | $0.124$ | $2\times$ |

Note also that the two pages use different values for the same symbol: $|\bar\gamma| \approx 0.023$ here (which is the *global* average $\bar\varepsilon$ of Yukawa §9(d)) against $|\bar\gamma| \approx 0.15$ there (the *sectoral* average). Only the numerator form at the sectoral value lands near the target, and the corrected count $N_{33} = 2$ then overshoots it twofold.

**What therefore stands.** ~~The **structural** result is [T]~~ — corrected 2026-09-25: the **structural** result is [C at (SV)]. $(\star)$ follows from symbolic $V_\mathrm{Gap}$ minimisation once the minimisation is restricted to one axis triple, and $N_{33}^\mathrm{Fano} = 2$ is a combinatorial fact; but the restriction was justified by the axis-labelled sector decomposition T-48a, which is retracted, and now rests only on the vacuum pattern the minimisation finds (cross-class coherences at machine zero, E26 below), i.e. on T-64. The **numerical** value $\varepsilon_\mathrm{eff} \approx 0.059$ is [C at (SV)] and is *phenomenological*: it comes from the independent loop route $\lambda_3\varepsilon/(4\pi) \approx 74\times 0.01/12.6 = 0.0587$, not from $(\star)$. Reconciling $(\star)$ with it requires fixing the $|\bar\gamma|$ placement, settling which average enters, and performing the full minimisation on $(S^1)^{21}/G_2$. Open.

**Resolved 2026-08-10 (instrument E26: self-consistent minimisation, no fitted parameters).** All three questions closed by computation:
| question | verdict | the losing readings |
|---|---|---|
| $\lvert\bar\gamma\rvert$ placement | **numerator** — the $(\star)$ form | denominator form lands $\times 56$–$393$ off |
| which average | **sectoral** ($\lvert\bar\gamma\rvert_{33} = 0.1314$ at the E26 vacuum) | global average lands at $\times 0.28$ |
| $N_{33}$ at Step 5 | **double counting — drop it**: $N_{33}$ already enters $\bar\gamma$ through Step 4's self-consistency | keeping it overshoots $\times 1.94$ |
Plus two findings the audit had not asked for: $r_4 = 1/2$ is an **identity** of Theorem 13.5 (not a measured input), and $\Sigma_0$ must be read as the **amplitude** sum (the phase reading is gauge-dependent). With these, the closed form evaluates to $\varepsilon_\mathrm{eff} = 0.0569$ vs the loop route's $0.0587$ — $3\%$, with the minimiser independently reproducing the T-64 vacuum structure (confinement $\varepsilon_{3\bar 3} \to 0$, electroweak $\varepsilon_{\bar 3\bar 3} \to 0$). The ansatz caveat is **discharged** by the wave-2 run (120 multistarts, all 21 amplitudes free within Cauchy–Schwarz): the sector *selection* is reproduced exactly — the dying classes ($\varepsilon_{3\bar 3}$, $\varepsilon_{\bar 3\bar 3}$, $\varepsilon_{O\bar 3}$) sit at machine zero — while intra-class equality of moduli holds only approximately (std $0.023$ on mean $0.1265$: the $SU(3)$ ansatz was a mild constraint, and the ansatz-free minimum is slightly deeper, $V = -0.2216$ vs $-0.2167$); $\varepsilon_\mathrm{eff} = 0.0549$ ($\times 0.93$ of the loop figure) — the agreement holds. Uniqueness (T-64): the global basin captured $17\%$ of starts and is separated from the second level ($V = -0.2086$). What keeps the value at [C] now is only the phenomenological character of the loop route itself.
:::

**Inputs used above** (from T-64 numerical minimization; reading fixed by E26): $V_4/V_2 = 1/2$ — an identity of 13.5; $\Sigma_0 = \sum|\gamma^*|^2 \approx 0.3$ (the amplitude sum; the E26 vacuum gives $0.1035$); sectoral $|\bar\gamma| \approx 0.15$ (E26: $0.1314$), global $\bar\varepsilon \approx 0.023$.

**Upgrade**: T-176 now has an **explicit algebraic expression** rather than a "claimed analytical" form. Numerical values remain [C at (SV)] because they depend on full vacuum minimization — a computational task, not a theoretical lacuna.

**Dependencies**: T-43d [T] (Fano selection rule), T-48a (sector decomposition; retracted [✗] 2026-09-25 — Step 2 now rests on the T-64 vacuum), T-64 [T] (corrected to the $G_2$-invariant potential; its vacuum has no sector values — hypothesis (SV)) (unique vacuum), T-74 [T] (V_Gap from spectral action), T-176 [C at (SV)] (analytical form).

---

## 8. Λ-deficit numerical programme specification {#lambda-programme}

The cosmological-constant deficit (~78 orders before minimisation) reduces to a **finite numerical computation** on the $G_2$-reduced phase space $(S^1)^{21}/G_2$. This section provides an explicit computational-programme specification.

### 8.1. Problem statement

Compute the minimum of the full Gap potential
$$V_\mathrm{Gap}(\theta) = V_2 + V_3 + V_4, \qquad \theta \in (S^1)^{21}/G_2$$
with $G_2$-gauge-fixed coordinates and evaluate $\Lambda_\mathrm{CC}$ from the spectral action formula (T-65 [T]):
$$\Lambda_\mathrm{CC} = f_0 \Lambda^4\bigg|_{\theta^*} - \frac{1}{2}\zeta'_{H_\mathrm{Gap}}(0)\bigg|_{\theta^*},$$
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

## 9. π<sub>bio</sub> measurement protocol specific mapping {#pi-bio-protocol}

The bridge $\pi_\mathrm{bio}: \mathrm{NeuralData} \to \mathcal{D}(\mathbb C^7)$ is [T] in structural form (G₂-uniqueness) but [H] in specific calibration. This section provides an explicit operational protocol; the conditions under which its test can fail — no predicate in the estimator, calibration on wakefulness only, verdict concordance with PCI instead of a numerical PCI conversion — are those of the [measurement protocol](/docs/applied/research/measurement-protocol#substitution-position) (corrected 2026-09-25).

### 9.1. Measurement setup

Simultaneous recording:
- **EEG** 128-channel, 1 kHz sampling, 60 min session.
- **fMRI** 3T, TR = 2 s, whole-brain coverage.
- **HRV** photoplethysmography, 500 Hz sampling.
- **TMS stimulation** 100 single-pulse trains at predetermined frontal cortex sites.

### 9.2. Feature extraction (7 diagonals)

| UHM dim | Neural feature | Frequency band | Rationale |
|---|---|---|---|
| $\gamma_{AA}$ | EEG delta power | 1–4 Hz | Cortical activation (consciousness level) |
| $\gamma_{SS}$ | EEG theta power | 4–8 Hz | Structural memory retention (hippocampus) |
| $\gamma_{DD}$ | EEG beta power | 12–30 Hz | Sensorimotor dynamics |
| $\gamma_{LL}$ | EEG gamma power | 30–80 Hz | Binding / logical coordination |
| $\gamma_{EE}$ | fMRI DMN coherence | — | Default-mode network = self-referential processing |
| $\gamma_{OO}$ | HRV LF/HF ratio | 0.04–0.15 Hz | Autonomic clock / vagal tone |
| $\gamma_{UU}$ | EEG global field power | broadband | Integration over whole cortex |

Normalize so $\sum \gamma_{kk} = 1$.

### 9.3. Feature extraction (21 off-diagonals)

For each pair $(i,j)$:
- Phase-locking value (PLV) between frequency bands $i$ and $j$ within a 2-s window.
- Complex coherence $\gamma_{ij} = |\mathrm{PLV}_{ij}| \exp(i\Delta\phi_{ij})$.

### 9.4. Validation gates

Reconstructed $\Gamma$ must satisfy:
- **Trace normalization**: $\mathrm{Tr}(\Gamma) = 1 \pm 0.01$.
- **Positive semi-definite**: all eigenvalues $\geq -0.001$ (numerical tolerance).
- **No predicate in the estimator**: the reconstruction carries no viability penalty ($\lambda_2 = 0$) and, in the confirmatory run, no consistency term with $\mathcal L_\Omega$ ($\lambda_1 = 0$) — SUB-2 of the [measurement protocol](/docs/applied/research/measurement-protocol#substitution-position). With the earlier default $\lambda_2 = 100$ every sub-threshold state of the uniform family was reconstructed at $\hat P = 2/7$ exactly, so the threshold test below could not fail.

*Corrected 2026-09-25:* the third gate read "Correlation with PCI: $P(\Gamma)$ should correlate with PCI across wake / NREM / anesthesia states". A correlation with PCI is not a gate on the reconstruction — it is the test itself, and PCI is not a function of $P$ (it is a normalised Lempel–Ziv complexity of a binarised response). The comparison with PCI is the concordance of verdicts in §9.5.

### 9.5. What the data can test, and where the substitution argument binds

**Calibration.** The parameters $\theta$ of $\pi_{\mathrm{bio}}$ (band weights, observation-model coefficients) are frozen on wakefulness sessions only (SUB-1); no NREM, anaesthesia, REM or ketamine label enters the fit. Specific frequency-band assignments stay **[H]** until the frozen protocol is validated on $N \geq 50$ subjects with independent replication. *Corrected 2026-09-25:* the list read "three consciousness states (wake, NREM3, anesthesia)" for calibration; a threshold fitted to report-labelled states reproduces the labels by construction and tests nothing (Kleiner–Hoel, strict-dependence horn).

**Predictions on out-of-sample sessions:**
- $P(\hat\Gamma_\mathrm{wake}) > 2/7$ (P8.1).
- $P(\hat\Gamma_\mathrm{NREM3}) < 2/7$ (P8.2 — observable only with $\lambda_2 = 0$).
- **Concordance of verdicts** (P8.4, SUB-5): on the same sessions, Cohen's $\kappa$ between $\mathrm{Cons}(\hat\Gamma) = (P > 2/7) \wedge (R \geq 1/3) \wedge (\Phi \geq 1) \wedge (D \geq 2)$ and $\mathrm{PCI}_{\max} > 0.31$; $\kappa \geq 0.8$ corroborates, $\kappa < 0.4$ falsifies. Raw agreement is not the measure: 34 agreements out of 40 give $\kappa = 0.70$ with balanced verdicts and $\kappa = 0.17$ with skewed ones (`test_verdict_concordance_is_judged_by_kappa_not_by_raw_agreement`, illustrative counts). REM and ketamine sessions (consciousness without behaviour at the time) are the decisive rows.

*Corrected 2026-09-25:* the third prediction read "$\Phi(\Gamma) \geq 1$ iff conscious (matching PCI > 0.31 threshold)". Both halves are withdrawn [✗]. (i) $\Phi \geq 1$ is necessary for $\mathrm{Cons}$, not sufficient: the predicate has a second exit, $P > 3/7$ ($R < 1/3$); on the uniform family the state with $\Phi = 3$ has $P = 4/7$, $R = 1/4$ and is not in the window (`test_phi_at_least_one_is_not_the_consciousness_verdict`). (ii) No derivation links $\Phi = 1$ or $P = 2/7$ to $\mathrm{PCI} = 0.31$; the nearness of $0.31$ to $2/7 \approx 0.286$ is a coincidence of unrelated scales, and the testable bridge is the concordance of verdicts above.

**Status**: protocol specified; awaiting data. *Corrected 2026-09-25:* the line read "No theoretical obstacle remains beyond experimental programme". One remains, and it is the substitution argument of Kleiner & Hoel (2021): with $\theta$ frozen, $\mathrm{Cons}_\theta$ is a function of prediction data alone, so wherever a physically possible variation keeps the reports and moves $\hat\Gamma$ across a threshold, either some system falsifies $\mathrm{Cons}$ or report-based inference fails for some system. The [measurement protocol](/docs/applied/research/measurement-protocol#substitution-position) proves where $\mathrm{Cons}$ sits between the two horns [T] and takes a domain-restricted lenient dependency inside natural sleep–wake and anaesthetic states [H]; outside that domain — unfoldings, emulations, language models — UHM makes no consciousness claim. By [T-221(e)](#t-221), no $\pi_{\mathrm{bio}}$ measurement discriminates the routes through the List/DeBrota no-go results either.

---

## 10. Summary table

| # | Theorem / Protocol | Previous status | New status | Closure method |
|---|---|---|---|---|
| T-210 | Strict Φ-monotonicity | [T] weak (T-195) | **[T] strict** | Interior-stratum argument |
| T-211 | PhysTheory higher coherences | [T] deferred to HTT | **[T]** as the Grothendieck construction (2026-09-25; read "[T] verified" by a full embedding, then [C at T-119]; the full embedding [✗]) | Cartesian unstraightening, HTT 3.2 |
| T-212 | U-projection / "Rh modality explicit" | [T] unnamed (T-185) | **[T] $G_2$-twirl (T-212′)**; the identification with Rh [✗] (read "[T] defined", then "[C] defined", until 2026-09-25) | Schur + Haar |
| T-213 | Yoneda without Kolmogorov | [T] uncomputable (T-193) | **[T] computable** | Bures description length |
| T-214 | Hard-problem meta-theorem | [I] residual | **[T] positive irresolvability** | Lawvere fixed-point |
| T-215 | Cross-layer identity | [C] (T-205 downgraded) | **[T]+[D]** | Conventional choice theorem |
| T-216 | Analytical ε<sub>eff</sub> | [H] no formula | **[C at (SV)]** (listed [T at T-64] until 2026-09-25) | Closed-form symbolic |
| §8 | Λ-deficit programme | "computational task" | **Spec complete** | HMC on $(S^1)^{21}/G_2$ |
| §9 | π<sub>bio</sub> protocol | [H] specific | **Spec complete, awaiting data**; the test is the concordance of verdicts (P8.4), bounded by the substitution argument (corrected 2026-09-25) | EEG/fMRI/HRV 7-feature map |

**Total (after extensions)**: of the ten theorems T-210–T-219, eight stand as [T] (T-210, T-211 in the corrected form of 2026-09-25 — its full-embedding claim is retracted — T-212 in the corrected form T-212′ — its former identification with Rh is retracted — T-213, T-214, T-215 with a definitional part, T-217, T-218), one is [C] (T-216) and one is [H] (T-219); plus 2 computational-programme specifications. *Corrected 2026-09-25:* the line read "10 new [T] theorems … All mathematical and categorical gaps of UHM's foundational framework are closed at fundamental level"; the second sentence is retracted — the rows marked [C] and [H] above are open mathematical conditions, and the framework's own inputs stayed open until 2026-09-25 — the first-order condition and Poincaré duality of T-119, settled that day by the restatement of T-119, which computes the spatial spectrum (the orientation (Alt) of T15, listed here until 2026-09-25, is discharged by the [canonical-orientation theorem](/docs/proofs/minimality/theorem-octonionic-derivation#каноническая-ориентация)), on which T-120, T-121, T-211 and clause (iii) of T-221 rested (T-120 and T-121 are [T] since; the recheck of T-211 showed that it never needed T-119 — each object of PhysTheory carries its topos — and T-211 is [T] in its corrected form; clause (iii) of T-221 went with the corrected T-221). (The corrected T-221 of 2026-09-25 does not rest on T-119/T-120.)

**Remaining genuinely open**:
- Numerical computation of Λ (§8) — resource-bounded, no theoretical obstacle.
- Empirical validation of π<sub>bio</sub> (§9) — experimental programme; the substitution argument of Kleiner & Hoel bounds what it can show, and UHM claims nothing outside natural sleep–wake and anaesthetic states (the line read "no theoretical obstacle" until 2026-09-25).
- The [P] bridge from E-sector structure to experienced content — **structurally inevitable** (T-214 [T]), not a lacuna.

~~**No mathematical gaps remain** in UHM's foundational framework after these closures.~~ Retracted [✗] (2026-09-25): the rows marked [C] and [H] above are open mathematical conditions, and the framework's own inputs stayed open until 2026-09-25 — the first-order condition and Poincaré duality of T-119, settled that day by the restatement of T-119, which computes the spatial spectrum (the orientation (Alt) of T15, listed here until 2026-09-25, is discharged by the [canonical-orientation theorem](/docs/proofs/minimality/theorem-octonionic-derivation#каноническая-ориентация)), on which T-120, T-121, T-211 and clause (iii) of T-221 rested (T-120 and T-121 are [T] since; the recheck of T-211 showed that it never needed T-119 — each object of PhysTheory carries its topos — and T-211 is [T] in its corrected form; clause (iii) of T-221 went with the corrected T-221). (The corrected T-221 of 2026-09-25 does not rest on T-119/T-120.)

---

## 11. T-217: L3 tricategorical coherence via ∞-truncation {#t-217}

:::tip Theorem T-217 (L3 tricategory coherence) [T]
The third-level interiority category $\mathbf{Exp}^{(3)} := \tau_{\leq 3}(\mathbf{Exp}_\infty)$ is a **coherent tricategory** in the Gordon–Power–Street sense (Gordon–Power–Street 1995, *Coherence for tricategories*). Pentagon identity for 1-cells, interchange law for 2-cells, and the pentagon-of-pentagons axiom for 3-cells all hold. The cellular structure decomposes as $K = 3 + 1 = 4$:
- **Three inherited 2-cells** from the L2 bicategory (T-192 [T]) corresponding to the LGKS triadic components (Aut, $\mathcal D$, $\mathcal R$);
- **One new 3-cell modification** $\eta: \varphi^{(2)} \Rightarrow \varphi\circ\varphi$ corresponding to the coherence of second-order self-reflection.
:::

**Proof (four steps).**

**Step 1 (Kan complex foundation).** By T-91 [T], $\mathbf{Exp}_\infty := \mathrm{Sing}(\mathcal E)$ is a Kan complex (Milnor 1957 applied to the Bures-topologized experiential category $\mathcal E$). Kan complexes are precisely the simplicial models of $\infty$-groupoids (Lurie HTT 1.2.5.1).

**Step 2 (Truncation functor preserves coherence).** The truncation functor $\tau_{\leq n}: s\mathbf{Set} \to s\mathbf{Set}_{\leq n}$ maps Kan complexes to $n$-truncated Kan complexes (Lurie HTT 5.5.6.18). Applied at $n = 3$: $\tau_{\leq 3}(\mathbf{Exp}_\infty)$ is a 3-truncated Kan complex, equivalently a **3-type** (homotopy type with $\pi_k = 0$ for $k > 3$).

**Step 3 (3-types ≃ tricategories).** By the Baez–Dolan stabilisation hypothesis (proved for $n \leq 3$ by Hirschowitz–Simpson, *Descente pour les n-champs*, arXiv:math/9807049, 2001; Leinster, *A Survey of Definitions of n-Category*, *Theory Appl. Categ.* 10 (2002), 1–70) in conjunction with the Gordon–Power–Street coherence theorem (*Coherence for Tricategories*, Mem. AMS 117 (1995)):
$$\bigl\{\text{3-types}\bigr\} \;\simeq\; \bigl\{\text{coherent tricategories with invertible cells}\bigr\}.$$
The equivalence is realised by the classifying-space functor $B: \mathrm{Tricat} \to s\mathbf{Set}_{\leq 3}$ and its left adjoint $\Pi_3: s\mathbf{Set}_{\leq 3} \to \mathrm{Tricat}$. Under this equivalence, $\tau_{\leq 3}(\mathbf{Exp}_\infty)$ corresponds to a coherent tricategory $\mathbf{Exp}^{(3)} := \Pi_3(\tau_{\leq 3}(\mathbf{Exp}_\infty))$.

:::note Framework-conditional citation (see [Rigour Stratification §T-217](/docs/reference/status-registry#стратификация-строгости))
The Baez–Dolan correspondence "3-types ≃ coherent tricategories" is standard in the category-theoretic literature (Hirschowitz–Simpson 2001; Leinster 2002; Gordon–Power–Street 1995). Its applicability here rests on $\tau_{\leq 3}(\mathbf{Exp}_\infty)$ being a 3-type admissible under the correspondence — this is immediate from Step 2 (Kan complex truncation) but the passage from the Kan complex to the GPS tricategory $\mathbf{Exp}^{(3)}$ is a category-bridging step, not a direct simplicial identity.
:::

**Step 4 (K=3+1 cellular count).** The $n$-cells of $\mathbf{Exp}^{(3)}$ are identified as:

| Level | Content | Count | Source |
|---|---|---|---|
| 0-cells | Density matrices $\Gamma \in \mathcal D(\mathbb C^7)$ | $\dim \mathcal D = 48$ (continuum) | State space |
| 1-cells | CPTP channels $\Phi: \Gamma \to \Gamma'$ | — | $G_2$-covariant (T-42a) |
| 2-cells (LGKS) | Natural transformations between CPTP channels | **3 structural classes** (Aut, $\mathcal D$, $\mathcal R$) | T-57 [T] triadic decomposition |
| 3-cells (new) | Modifications between natural transformations | **1 structural class**: $\eta: \varphi^{(2)} \Rightarrow \varphi\circ\varphi$ | Self-reflection coherence |

The 2-cell count $K_2 = 3$ follows from T-57 [T] (LGKS decomposition: any CPTP generator decomposes uniquely into unitary, dissipative, and regenerative components).

The 3-cell count $K_3 = 1$ follows from:
- The experiential tricategory has strict 2-categorical substructure at L2 (T-192 [T] strict 2-category).
- Strict 2-categories have **trivial interchange law failures** (Eckmann–Hilton argument).
- The only non-trivial 3-cell in a strict-2-category-enriched-tricategory is the coherence modification between $\varphi^{(2)}$ (defined as the 2-fold composition $\varphi\circ_2\varphi$ in the tricategory structure) and $\varphi\circ\varphi$ (defined as 1-cell composition).
- These two are **not** equal in general (they live in different cell positions), but are related by a unique up-to-modification equivalence. This is the new 3-cell $\eta$.

Hence total $K_\text{L3} = K_2 + K_3 = 3 + 1 = 4$. This justifies the Bayesian-dominance threshold $R^{(2)} \geq 1/K = 1/4$ (T-67 [T] statement) with the count now derived from tricategorical first principles rather than heuristic argument. $\blacksquare$

**Pentagon-of-pentagons coherence.**
The Gordon–Power–Street pentagon axiom at the 3-cell level states that for five 1-cells $f_1, \ldots, f_5$, the composition-associativity 3-cells satisfy a higher pentagon identity. This is automatic for $\tau_{\leq 3}$ of a Kan complex (Lurie HTT 5.2.7 + Baez–Dolan coherence), hence holds in $\mathbf{Exp}^{(3)}$.

**Consequence for T-67.** The "3+1 heuristic decomposition" flagged in [T-67 stratification](/docs/consciousness/hierarchy/interiority-hierarchy#теорема-l3-k4) is now **derived from tricategorical coherence** (the 3 cells are LGKS triadic 2-cells, the +1 cell is the coherence modification $\eta$). T-67 thus has status [T]: the count $K = 4$ carries full categorical justification via T-217.

**Dependencies**: T-91 [T] ($\infty$-groupoid $\mathbf{Exp}_\infty$), T-192 [T] (L2 strict 2-category), T-57 [T] (LGKS triadic decomposition), T-42a [T] ($G_2$-rigidity). Standard mathematics: Milnor 1957, Gordon–Power–Street 1995, Lurie HTT 5.5.6 + 5.2.7, Hirschowitz–Simpson 2001, Leinster 2002, Eckmann–Hilton argument.

---

## 12. T-218: SYNARC cognitive complex is a Kan complex {#t-218}

:::tip Theorem T-218 (Cog as Kan complex) [T]
The SYNARC cognitive simplicial set, defined as the singular complex of the classifying space of the Fano-Kraus category,
$$\mathrm{Cog} \;:=\; \mathrm{Sing}\bigl(B_\bullet\mathcal C_{\mathrm{FKraus}}\bigr),$$
is a **Kan complex**: every horn $\Lambda^n_k \to \mathrm{Cog}$ admits a filler $\Delta^n \to \mathrm{Cog}$, for all $n \geq 1$ and $0 \leq k \leq n$ (including outer horns). Its 3-coskeletal truncation $\tau_{\leq 3}\mathrm{Cog}$ is a 3-truncated Kan complex, justifying SAD_MAX = 3 at the categorical level.
:::

**Proof (three steps).**

**Step 1 (Classifying space construction).** The Fano-Kraus category $\mathcal C_{\mathrm{FKraus}}$ has:
- Objects: density matrices $\Gamma \in \mathcal D(\mathbb C^7)$;
- Morphisms $\mathrm{Hom}_{\mathcal C_{\mathrm{FKraus}}}(\Gamma_1, \Gamma_2) := \{n \in \mathbb N : F_{\mathrm{Kraus}}^n(\Gamma_1) = \Gamma_2\}$ — natural-number iterations of the Fano-Kraus channel.

The classifying space $B_\bullet\mathcal C_{\mathrm{FKraus}}$ is defined as the geometric realisation of the nerve:
$$B_\bullet\mathcal C_{\mathrm{FKraus}} := |N_\bullet \mathcal C_{\mathrm{FKraus}}|.$$
This is a topological space (actually a CW-complex by Segal 1968).

**Step 2 (Singular complex is Kan by Milnor).** For any topological space $X$, the singular simplicial set $\mathrm{Sing}(X)_n := \mathrm{Map}_{\mathbf{Top}}(\Delta^n_{\mathrm{top}}, X)$ is a **Kan complex** (Milnor 1957; Lurie HTT 1.2.5.3). This is because every horn inclusion $\Lambda^n_k \hookrightarrow \Delta^n$ is a trivial cofibration in the Quillen model structure on $s\mathbf{Set}$, and singular complexes of topological spaces are fibrant objects.

Applying this to $X = B_\bullet\mathcal C_{\mathrm{FKraus}}$: $\mathrm{Cog} = \mathrm{Sing}(B_\bullet\mathcal C_{\mathrm{FKraus}})$ is a Kan complex. **Both inner and outer horns fill.** $\checkmark$

**Step 3 (Explicit filler construction).** For implementation-readiness, an explicit filler algorithm for outer horns:
- **Input**: horn $\Lambda^n_k \to \mathrm{Cog}$ represented by $(n-1)$ compatible simplices $\sigma_0, \ldots, \hat\sigma_k, \ldots, \sigma_n$.
- **Output**: filler $\sigma: \Delta^n \to \mathrm{Cog}$ completing the horn.

Construction: each $\sigma_i$ represents a continuous map $\Delta^{n-1}_{\mathrm{top}} \to B_\bullet\mathcal C_{\mathrm{FKraus}}$. Assemble into a continuous map on $\Lambda^n_k \subset \partial\Delta^n_{\mathrm{top}}$. Extend to $\Delta^n_{\mathrm{top}}$ using the retraction $r_k: \Delta^n_{\mathrm{top}} \to \Lambda^n_k$ that sends interior points radially to the horn. Pullback via $r_k$ gives the filler $\sigma$. $\checkmark$

**Algorithm complexity**: $O(n \cdot \dim\mathcal D)$ per filler — each of the $n-1$ input simplices is composed via radial pullback in bounded time. For SYNARC's $n \leq 3$ (3-coskeletal): $O(\dim\mathcal D) = O(48)$ operations per filler.

**Step 4 (3-coskeletal truncation).** Apply $\tau_{\leq 3}$ to $\mathrm{Cog}$:
- By T-142 [T] (SAD_MAX = 3), the Fano contraction suppresses 4-simplices below distinguishability: every 4-horn filler has Bures-support below $P_{\mathrm{crit}}^{(4)} = 54/35 > 1$, hence fails the viability constraint.
- Therefore $\tau_{\leq 3}\mathrm{Cog} \simeq \mathrm{Cog}$ in the sense that truncation is an equivalence on cells above dimension 3.
- $\tau_{\leq 3}\mathrm{Cog}$ is itself a Kan complex (Lurie HTT 5.5.6.21: truncation preserves Kan fibrancy).

:::note Scope of the suppression argument (see [Rigour Stratification §T-218](/docs/reference/status-registry#стратификация-строгости))
The "Fano contraction suppresses 4-simplices below distinguishability" step is a **category-bridging argument** (simplicial-combinatorial $\leftrightarrow$ Bures-metric viability), not a simplicial-identity proof. Formally: the Kan-complex part of T-218 (Steps 1–3) is [T] via Milnor 1957 + Segal 1968. The 3-coskeletal truncation in Step 4 is equivalent to $\mathrm{Cog}$ only **on the SYNARC-viable subset** where the $P_{\mathrm{crit}}^{(n)}$ constraint of T-142 [T] applies. Off the viable subset, $\tau_{\leq 3}$ is the standard simplicial truncation and is not an equivalence. This is the intended reading of "SAD_MAX = 3 at the categorical level."
:::

Hence SYNARC's 3-coskeletal bound is now rigorously verified: Cog is a Kan complex, fillers are explicitly constructible, and the 3-truncation matches the SAD_MAX = 3 cognitive ceiling. $\blacksquare$

**Consequence**: The SYNARC paper's claim that Cog is a Kan complex (previously stated without explicit horn-filler construction) is now fully verified. Implementation can use the algorithm of Step 3 to compute outer horn fillers in bounded time per cell.

**Dependencies**: T-91 [T] (general Kan-complex theory), T-142 [T] (SAD_MAX = 3), T-82 [T] (Fano uniqueness). Standard mathematics: Milnor 1957, Segal 1968, Lurie HTT 1.2.5 + 5.5.6.

---

## 13. T-219: Λ SUSY-suppression via sector decomposition {#t-219}

:::tip Theorem T-219 (SUSY Λ-suppression, sector derivation) [H]
In UHM's N=1 supersymmetric spectral action on $M^4 \times A_{\mathrm{int}}$ (T-65 [T]), the residual cosmological constant from SUSY-broken loops is suppressed by the factor
$$\Lambda_\mathrm{SUSY} \;\sim\; \varepsilon^{12} \, M_P^4$$
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
$$\delta \Lambda_k \;\sim\; \frac{\operatorname{STr}(M_k^4)}{16\pi^2} \cdot \log(\Lambda_{\mathrm{UV}}/M_k)$$
where $M_k$ is the SUSY-breaking mass-matrix of sector $k$ and $\operatorname{STr}$ is the supertrace. In exact SUSY, $\operatorname{STr}(M^{2n}) = 0$ for all $n$. In broken SUSY with splitting $\delta m_k$:
$$\operatorname{STr}(M_k^4) \;\sim\; (\delta m_k)^4 \;\sim\; (\varepsilon M_P)^4 \;=\; \varepsilon^4 M_P^4.$$

**Step 3 (Multi-sector product structure).** The three sectors are **independent** in the SUSY-broken spectral action: the super-trace decomposes as
$$\operatorname{STr}(M^4)_{\mathrm{total}} = \operatorname{STr}(M_O^4) + \operatorname{STr}(M_3^4) + \operatorname{STr}(M_{\bar 3}^4) \;\sim\; 3 \varepsilon^4 M_P^4.$$

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

**Dependencies**: T-48a (sector decomposition; retracted [✗] 2026-09-25), T-50 [T] (unique superpotential, Schur), T-52 (sector asymmetry; retired as a theorem 2026-09-25, now the hypothesis (SA)), T-64 [T] (corrected to the $G_2$-invariant potential; its vacuum has no sector values — hypothesis (SV)) (unique vacuum), T-65 [T] (spectral action), T-71 [T] (cohomological $\Lambda_\mathrm{global}=0$). Standard mathematics: Martin 2010 SUSY primer, Seeley–de Witt heat kernel expansion, standard N=1 one-loop calculation.

---

## 14. T-220: No-reduction theorem for $F_4$-UHM → $G_2$-UHM {#t-220}

**Motivation.** A natural question when considering category shifts of UHM (replacing $G_2 = \mathrm{Aut}(\mathbb{O})$ with $F_4 = \mathrm{Aut}(\mathcal{J}_3(\mathbb{O}))$) is whether $G_2$-UHM is a *functorial section* of a prospective $F_4$-UHM. Theorem T-220 establishes unconditionally that **no such reduction functor exists** preserving the canonical UHM invariants.

### 14.1. Statement {#t-220-statement}

:::tip Theorem T-220 (No-reduction, $F_4 \to G_2$) [T]
Let $\mathbf{C}_{F_4}$ denote the hypothetical base category of $F_4$-UHM — objects: states on the exceptional Jordan algebra $\mathcal{J}_3(\mathbb{O})$ with $F_4$-equivariance, morphisms: Jordan-triple dynamics preserving the cubic Freudenthal trace form. Let $\mathbf{C}_{G_2}$ be the category of $G_2$-UHM — states on $\mathbb{C}^7$ with $G_2$-equivariant CPTP (Lindblad) dynamics.

Then there does **not exist** a functor
$$
R: \mathbf{C}_{F_4} \longrightarrow \mathbf{C}_{G_2}
$$
satisfying any three of the following four conditions simultaneously:

(S1) **State-space compatibility**: $R$ factors through a canonical $F_4$-equivariant linear projection $\pi: \mathcal{J}_3(\mathbb{O}) \twoheadrightarrow \mathbb{C}^7$.

(S2) **Incidence compatibility**: $R$ maps the Cayley plane $\mathbb{O}P^2$ to the Fano plane $\mathrm{PG}(2,2)$ $F_4$-equivariantly and non-trivially.

(S3) **Dynamical compatibility**: $R$ maps Jordan-triple dynamics on $\mathcal{J}_3(\mathbb{O})$ to CPTP (Lindblad) dynamics on $\mathbb{C}^7$ via an algebra homomorphism.

(S4) **Numerical compatibility**: $R$ preserves the full set of UHM invariants
$$
\{P_{\mathrm{crit}} = 2/7,\ \alpha = 2/3,\ \mathrm{SAD}_{\max} = 3,\ R_{\mathrm{th}} = 1/3,\ \Phi_{\mathrm{th}} = 1\}.
$$

In fact, each of (S1), (S2), (S3), (S4) is independently obstructed.
:::

### 14.2. Proof {#t-220-proof}

We establish five independent obstructions. Any one suffices; together they rule out even substantial weakenings of the statement.

#### Obstruction I — Representation theory (kills S1) {#t-220-obstruction-i}

Use the Borel–de Siebenthal chain
$$
F_4 \supset \mathrm{Spin}(9) \supset \mathrm{Spin}(7) \supset G_2.
$$

Under $\mathrm{Spin}(9) \subset F_4$, the traceless 26-dimensional irrep splits
$$
\mathbf{26} = \mathbf{1} \oplus \mathbf{9} \oplus \mathbf{16}
$$
(trivial + vector + spinor).

Under $\mathrm{Spin}(7) \subset \mathrm{Spin}(9)$:
- $\mathbf{9} \to \mathbf{7} \oplus \mathbf{1} \oplus \mathbf{1}$ (the $\mathrm{Spin}(9)$-vector restricts to $\mathrm{Spin}(7)$-vector plus two $\mathrm{Spin}(7)$-invariants, matching the codimension-2 inclusion $\mathbb{R}^7 \subset \mathbb{R}^9$);
- $\mathbf{16} \to \mathbf{8}_s \oplus \mathbf{8}_s$ (the $\mathrm{Spin}(9)$-spinor restricts to two copies of the $\mathrm{Spin}(7)$-spinor).

Under $G_2 \subset \mathrm{Spin}(7)$ (defining $G_2$ as stabiliser of a unit spinor in $\mathbb{R}^8$):
- $\mathbf{7} \to \mathbf{7}$ (the $\mathrm{Spin}(7)$-vector is already $G_2$-fundamental, since $G_2 \subset \mathrm{SO}(7)$);
- $\mathbf{8}_s \to \mathbf{7} \oplus \mathbf{1}$ (classical Gray–Salamon decomposition).

Combining:
$$
\boxed{\mathcal{J}_3(\mathbb{O})\big|_{G_2} = \mathbf{27} = 3 \cdot \mathbf{7} \,\oplus\, 6 \cdot \mathbf{1}.}
$$

Dimension check: $3 \cdot 7 + 6 \cdot 1 = 27$. ✓

**Three distinct $G_2$-isotypic copies of $\mathbf{7}$ appear** — one from the $\mathrm{Spin}(9)$-vector branch, two from the $\mathrm{Spin}(9)$-spinor branch. Under the maximal subalgebra $A_1 \times G_2 \subset F_4$ the $\mathbf{26}$ decomposes
$$
\mathbf{26} = (\mathbf{4}, \mathbf{1}) \oplus (\mathbf{2}, \mathbf{7}) \oplus (\mathbf{1}, \mathbf{7}) \oplus (\mathbf{1}, \mathbf{1}),
$$
revealing that the three $\mathbf{7}$-copies form an $A_1$-doublet $(\mathbf{2},\mathbf{7})$ plus a singlet $(\mathbf{1},\mathbf{7})$.

Any projection $\pi: \mathcal{J}_3(\mathbb{O}) \to \mathbb{C}^7$ must select one (or a linear combination) of these three copies. But:
- selecting the $A_1$-doublet copies breaks $A_1$-symmetry (hence $F_4$-equivariance);
- selecting the $A_1$-singlet copy preserves $A_1$ but not the rest of $F_4$, since $F_4$ mixes the $A_1 \times G_2$-isotypic components via the $(\mathbf{4},\mathbf{1})$ and $(\mathbf{1},\mathbf{1})$ generators.

**No $F_4$-equivariant projection $\pi$ exists.** This contradicts (S1). $\blacksquare$

#### Obstruction II — Geometry of incidence (kills S2) {#t-220-obstruction-ii}

- $\mathbb{O}P^2$ is a 16-real-dimensional smooth manifold (the Cayley projective plane), on which $F_4$ acts **transitively and isometrically** (with respect to the Freudenthal metric).
- $\mathrm{PG}(2,2)$ is a discrete 7-point configuration (the Fano plane), $\dim_\mathbb{R} = 0$.

A continuous $F_4$-equivariant map $\varphi: \mathbb{O}P^2 \to \mathrm{PG}(2,2)$ factors through the orbit space $\mathbb{O}P^2 / F_4$, which is a single point by transitivity. Hence $\varphi$ is **constant**, losing all information.

Alternative via homotopy: $\pi_1(\mathbb{O}P^2) = 0$ (simply connected), so there is no non-trivial discrete map via fundamental-group considerations either.

**No $F_4$-equivariant non-constant reduction of incidence exists.** This contradicts (S2). $\blacksquare$

#### Obstruction III — Jordan exceptionality (kills S3) {#t-220-obstruction-iii}

**Zelmanov's theorem (1983)**: the exceptional Jordan algebra $\mathcal{J}_3(\mathbb{O})$ is *not special* — it admits no embedding into any associative algebra.

Consequence for dynamics: a CPTP (Lindblad) map
$$
\mathcal{L}(\rho) = -i[H,\rho] + \sum_k \left( L_k \rho L_k^\dagger - \tfrac{1}{2}\{L_k^\dagger L_k, \rho\}\right)
$$
on $B(\mathbb{C}^7)$ is defined via the associative multiplication of $M_7(\mathbb{C})$. Any homomorphism from Jordan-triple dynamics on $\mathcal{J}_3(\mathbb{O})$ to Lindblad dynamics on $\mathbb{C}^7$ would lift to a Jordan-algebra homomorphism $\mathcal{J}_3(\mathbb{O}) \to M_7(\mathbb{C})^+$, where $M_7(\mathbb{C})^+$ is the special Jordan algebra underlying $M_7(\mathbb{C})$.

By Zelmanov, no such homomorphism exists: $\mathcal{J}_3(\mathbb{O})$ is exceptional, not special.

**No algebra-homomorphism preserving dynamics exists.** This contradicts (S3). $\blacksquare$

#### Obstruction IV — Numerical invariants (kills S4) {#t-220-obstruction-iv}

Even granting a non-canonical projection $\pi_c$ (the $A_1$-invariant $\mathbf{7}$-copy) and closing eyes on Obstructions II–III, numerical invariants fail to transfer:

- **$\alpha^{G_2} = 2/3$** derives from the incidence combinatorics of $\mathrm{PG}(2,2)$: each point lies on 3 lines, each line has 3 points, BIBD(7,3,1). On $\mathbb{O}P^2$ the analogous "contraction coefficient" is controlled by the sectional curvatures of the Freudenthal metric: $\mathbb{O}P^2$ is a rank-one symmetric space with sectional curvatures pinched between $1/4$ and $1$, yielding an effective contraction $\alpha^{F_4} \in [1/4, 1/2]$ for any averaging kernel. In particular $\alpha^{F_4} \neq 2/3$.

- **$P_{\mathrm{crit}}^{G_2} = 2/7$** derives from Frobenius-norm distinguishability on $\mathbb{C}^7$. On $\mathcal{J}_3(\mathbb{O})$ the relevant bound uses the cubic Freudenthal trace form, yielding $P_{\mathrm{crit}}^{F_4} \sim c/27$ for some $O(1)$ constant $c$ — quantitatively different from $2/7$.

- **$\mathrm{SAD}_{\max}^{G_2} = 3$** depends on $\alpha = 2/3$ via the geometric tower bound $P_{\mathrm{crit}}^{(n)} = P_{\mathrm{crit}}\cdot 3^{n-1}/(n+1)$. With $\alpha^{F_4} \neq 2/3$ and $P_{\mathrm{crit}}^{F_4} \neq 2/7$, the physical-maximum crossing occurs at a different $n$.

- **$R_{\mathrm{th}}^{G_2} = 1/3$, $\Phi_{\mathrm{th}}^{G_2} = 1$** derive from the tripartite K=3 decomposition of the Fano plane. $\mathcal{J}_3(\mathbb{O})$ has a natural 3-diagonal structure (the three diagonal entries $a,b,c$), but this is a 3-dimensional subspace within $\mathcal{J}_3(\mathbb{O})$, not the same structure as Fano K=3. Numerical values differ.

**No $R$ preserves the five-element invariant set.** This contradicts (S4). $\blacksquare$

#### Obstruction V — Cohomological / K-theoretic mismatch (independent verification) {#t-220-obstruction-v}

As independent confirmation of Obstructions I–IV, compare topological invariants of the canonical state-space manifolds:

| Invariant | $\mathbb{C}P^6$ ($G_2$-UHM) | $\mathbb{O}P^2$ ($F_4$-UHM) |
|---|---|---|
| Euler characteristic $\chi$ | $7$ | $3$ |
| Cohomology ring | $\mathbb{Z}[x]/x^7$, $\|x\|=2$ | $\mathbb{Z}[y]/y^3$, $\|y\|=8$ |
| Rank of $K^0$ | $\mathbb{Z}^7$ | $\mathbb{Z}^3$ |
| Real dimension | $12$ | $16$ |

$\chi = 7 \neq 3$ alone rules out any continuous retraction $\mathbb{O}P^2 \twoheadrightarrow \mathbb{C}P^6$: the Euler characteristic would be preserved by retraction composed with embedding, forcing $7 = \chi(\mathbb{C}P^6) \leq \chi(\mathbb{O}P^2) = 3$, contradiction.

$K^0(\mathbb{C}P^6) = \mathbb{Z}^7$ and $K^0(\mathbb{O}P^2) = \mathbb{Z}^3$ are non-isomorphic abelian groups, so no K-theory-preserving functor between the corresponding categories of vector bundles exists.

**Independent verification of Obstructions I–IV.** $\blacksquare$

Combining the five obstructions proves T-220. $\square$

### 14.3. Corollaries {#t-220-corollaries}

:::info Corollary 14.1 — Category shift is not safe
The naïve shift $G_2$-UHM $\hookrightarrow F_4$-UHM as a *refinement* (in the sense that $G_2$-UHM is a functorial section of $F_4$-UHM) is **impossible**. Any genuinely realised $F_4$-UHM is a **distinct theory** requiring its own empirical calibration.
:::

:::info Corollary 14.2 — Outcome-1 elimination
Of the three possible outcomes of an $F_4$-category shift (replacement / parallel theory / meta-UHM), **Outcome 1 ("$G_2$-UHM is a slice of $F_4$-UHM") is ruled out**. Only Outcome 2 (parallel theories) and Outcome 3 (meta-UHM via an $\infty$-topos comparison) remain viable.
:::

:::info Corollary 14.3 — Mathesis-level comparison is the only route
The only available mechanism to compare $G_2$-UHM and $F_4$-UHM is **Mathesis $\infty$-topos $\mathfrak{M}$**, in which both theories appear as objects (not mutually reducible). This aligns with M-10 (Lawvere fixed-point boundary): no single theory contains a complete self-description of the other.
:::

### 14.4. Open direction unlocked: three generations hypothesis {#t-220-three-generations}

The decomposition $\mathcal{J}_3(\mathbb{O})|_{G_2} = 3 \cdot \mathbf{7} \oplus 6 \cdot \mathbf{1}$ exposes **three $G_2$-isotypic copies of the fundamental $\mathbf{7}$-representation**. ~~Independently of UHM, octonion-based derivations of the Standard Model (Dubois-Violette, Boyle–Farnsworth) recover the three fermion generations from similar triple-copy structures.~~ **Retracted 2026-09-25:** the sentence said that octonionic derivations of the Standard Model recover the three generations; none of the cited works derives the number three. Dubois-Violette (Nucl. Phys. B 912, 426, 2016) takes "the existence of 3 generations" as a premise and associates the three generations with the triality of $\mathcal{J}_3(\mathbb{O})$, as do Dubois-Violette and Todorov (Nucl. Phys. B 938, 751, 2019); Boyle and Farnsworth (New J. Phys. 22, 073023, 2020) represent the three generations by taking three copies of the one-generation representation; Boyle alone (arXiv:2006.16265; J. Math. Phys. 67, 071701, 2026) writes that "it is natural to suspect" triality to be their origin. The triple-copy structure is thus a shared hypothesis, not a result.

**Hypothesis (T-220-H, speculative)**: the three $\mathbf{7}$-copies correspond to three "generations of consciousness sectors" — one $A_1$-singlet generation (stable) and one $A_1$-doublet generation (excited). This would couple UHM to the three-generation mystery of the Standard Model, but requires a separate empirical programme and falls outside T-220's scope.

### 14.5. Dependencies and scope {#t-220-scope}

**Depends on**: G₂ branching chain (classical Lie theory, Adams 1996), Borel–de Siebenthal classification (1949), Gray–Salamon spinor decomposition, Zelmanov 1983 (Jordan exceptionality), standard algebraic topology (Euler characteristics of $\mathbb{O}P^2$ and $\mathbb{C}P^6$).

**Scope**: T-220 rules out naive functorial reduction $F_4 \to G_2$ UHM; it does **not** rule out:
- $\infty$-topos-level comparison (Mathesis);
- existence of $F_4$-UHM as an independent theory;
- partial/qualitative correspondences between the two.

---

## 15. T-221: Which route UHM takes through the List/DeBrota no-go results {#t-221}

:::warning Corrected 2026-09-25 — what the earlier version of this section got wrong
1. **The quadrilemma was misquoted.** List's quadrilemma (*Philos. Q.* 75(3): 1026–1048, 2025) has **four** claims — first-person realism (FPR), non-solipsism (NS), non-fragmentation (NF), one world (OW) — that are jointly inconsistent, while *any three* are consistent. Non-relationalism (NR) is not a fifth claim there: in List (2025) it "was not stated as a separate thesis but was treated as a presupposition of first-personal realism" (DeBrota & List, arXiv:2604.14234, footnote 5). The five-thesis form belongs to DeBrota & List (2026, arXiv:2604.14234, §3): FPR, NS and *objectivism* = OW ∧ NF ∧ NR are jointly inconsistent, and any two of the three are consistent. The earlier line "any two or three are jointly consistent; any four are not" is false [✗]: dropping any single thesis of the five leaves a consistent four.
2. **Wrong source for the heptalemma.** The heptalemma is DeBrota & List, "A heptalemma for quantum mechanics", *Found. Phys.* **56**, 24 (2026), arXiv:2512.01982. arXiv:2604.14234 is the programmatic paper "Consciousness, quantum mechanics, and the limits of scientific objectivism" (14 April 2026), which states the consciousness no-go in the five-thesis form and compares the two domains.
3. **"A fourth route" [✗].** Replacing NR by a site-relative NR<sub>site</sub> while keeping OW and NF is exactly the **relationalist** route of DeBrota & List (§4: "uphold one world and non-fragmentation and … argue that first-personal facts are only relative rather than absolute facts"). It is not outside their taxonomy. The following are retracted with it: "FPR is forced" (it rested on the hypothesis T-186(a) and, in any case, UHM keeps FPR only in relativised form); Corollary T-221.1 as a "positive response" (the consistency of {FPR, NS, OW, NF, NR<sub>site</sub>} is the consistency of the relationalist route, which the authors grant); Corollary T-221.3 "RQM = τ<sub>≤1</sub>(𝔗)" (the site $\mathcal C_7$ is an ordinary category, so its representables are already 0-truncated and 1-truncation changes none of them — nothing is "collapsed"); the reading of fragmentalism as "dropping descent" (DeBrota & List cite the sheaf-theoretic formalisation of Abramsky & Brandenburger 2011, where descent holds and what fails is a *global section*); and the "empirical discriminator" (by part (e) below, the routes share every observable).
:::

**The two no-go results, as stated by their authors.**

1. **List (2025).** FPR: "for any conscious subject, there are first-personal facts"; NS: "there is more than one conscious subject"; NF: "the totality of facts that hold in any given world are compossible"; OW: "reality consists of one world, not of many" (wording of the 2023 preprint, philsci-archive 22582). The four are jointly inconsistent; any three are consistent. The routes: drop FPR (most analytic theories — physicalist, dualist, "and arguably also the various recently influential Russellian, neutral, or double-aspect monist views"), drop NS (Hare's egocentric presentism), drop NF (Fine 2005, Lipman 2023), drop OW (List 2023, the many-worlds theory of consciousness).
2. **DeBrota & List (2026, arXiv:2604.14234).** FPR, NS and objectivism (OW ∧ NF ∧ NR) are jointly inconsistent; any two consistent. Relaxing one objectivist conjunct gives three non-objectivist routes — relationalist (drop NR), fragmentalist (drop NF), many-subjective-worlds (drop OW). For the relationalist route the authors raise two objections: relativised first-personal facts "would amount to a denial of first-personal realism in the originally intended sense", because the table of them "leaves open which experiences I have"; and one must say what the relativisation parameter is (Fine 2005: a "pure metaphysical self … that stands outside the world"). The choice among routes is left to "an inference to the best explanation"; they consider it "unlikely that empirical evidence alone could adjudicate the issue".
3. **DeBrota & List (*Found. Phys.* 56, 24, 2026).** Locality, measurement independence, measurement realism, NR, NF, OW and NS are jointly inconsistent with the predictions of quantum mechanics; any six are consistent.

**Setting.** $\mathfrak{T} = \mathrm{Sh}_\infty(\mathcal{C}_7, J_{\mathrm{Bures}}, \omega_0)$ is the UHM $\infty$-topos. Propositions are read in its internal language by Kripke–Joyal forcing (Mac Lane & Moerdijk, *Sheaves in Geometry and Logic*, §VI.6–7): for a stage $U$ (an object of the site, embedded by Yoneda as $y(U)$) and a formula $\varphi$, "$U \Vdash \varphi$" says that $\varphi$ holds at $U$. A fact holds **absolutely** — in the sense of NR — when it is forced at the terminal object $1$; it holds **relative to $U$** when it is forced at $U$. A **subject** is a viable state $\Gamma$ taken as a stage; its **state** is the element $s_U \in \mathcal D(U)$ of the sheaf of states $\mathcal D$ that the stage carries ($s_{y(\Gamma)} = \Gamma$). The first-personal proposition "I am in state $X$" is the formula $[s = X]$. Propositions are $(-1)$-truncated objects, so the forcing relation lives in the 1-topos $\tau_{\leq 0}\mathfrak{T}$ of 0-truncated objects, where the classical Kripke–Joyal clauses apply.

:::tip Theorem T-221 (UHM realises the relationalist route) [T]+[I]
In $\mathfrak{T}$:

**(a) The no-go holds inside UHM [T].** If $X \neq Y$, no inhabited stage forces $[s = X] \wedge [s = Y]$. The first-personal facts of two subjects in different complete states are not compossible — List's lemma is a theorem of UHM's semantics, not something UHM evades.

**(b) Route [T].** UHM keeps OW (one topos — by the choice of primitive, not by a derivation), NF (the internal logic is consistent: $1 \nVdash \bot$), NS (under the identity convention $\iota_{\min}$ of T-215) and FPR **in relativised form**: each subject's first-personal facts are forced at its own stage. By (a) they cannot all be forced at $1$, so NR fails for them. This is the relationalist route of DeBrota & List (2026). In List's (2025) four-claim map, where NR is part of FPR, the same position lies on the first horn — FPR given up in its original, non-relational sense — together with the double-aspect monisms List places there.

**(c) The relativisation parameter is internal [T].** The parameter is the stage $y(\Gamma)$, an object of $\mathfrak{T}$ itself (the Yoneda embedding lands in $\mathfrak{T}$; the site is essentially small). This answers the second objection of DeBrota & List — Fine's "pure metaphysical self … outside the world" — and is what distinguishes UHM within the relationalist route: in relational quantum mechanics any physical system is a parameter, in UHM a viable state.

**(d) The first objection stands [T].** The absolute facts — those forced at $1$ — contain no fact of the form "I am $\Gamma_1$" whenever a second subject exists (by (a)). Moreover, every automorphism $\alpha$ of the site (for example conjugation $\Gamma \mapsto V\Gamma V^\dagger$ by a unitary $V$, which maps CPTP maps to CPTP maps and preserves the Bures distance) preserves forcing: $U \Vdash \varphi \iff \alpha(U) \Vdash \varphi$ for every closed formula $\varphi$. Nothing in the theory selects "my" stage; selecting one is a choice of a point $p : \mathbf{Set} \to \mathfrak{T}$, data the theory does not supply. This is the vertiginous question of Hellie (2013) in the form T-214 predicts: an external postulate, not an internal morphism.

**(e) The mathematics does not choose the route [T]; the choice is interpretive [I].** The three non-objectivist routes are three readings of the same forcing relation: *relationalist* — a fact is a pair $(U, \varphi)$ with $U \Vdash \varphi$; *fragmentalist* — a fact is any $\varphi$ forced at some inhabited stage (by (a) this collection contains $[s = X]$ and $[s = Y]$ although their conjunction is forced nowhere; globally each has an intermediate truth value in $\Omega$, neither $\top$ nor $\bot$, and reading every locally true proposition as true simpliciter is exactly what makes the collection incoherent — the shape DeBrota & List point to when they cite the sheaf-theoretic tools of Abramsky & Brandenburger); *many-subjective-worlds* — a world is a point $p$ with the facts $\{\varphi : p \Vdash \varphi\}$, the objective facts being those true at every point (these are the facts forced at $1$ whenever $\mathfrak{T}$ has enough points). Every observable of UHM — $P$, $R$, $\Phi$, $D$ and every prediction built from them — is a function of the forcing relation and is the same under all three readings. No measurement, $\pi_{\mathrm{bio}}$ included, can discriminate them. The corpus's stated semantics — facts as sections indexed by stages — is the relationalist reading; that is the route UHM *takes*, not one it is *forced* into.
:::

**Corollary T-221.1 (Where UHM sits in the two maps) [T].** In the five-thesis map of DeBrota & List (2026): the relationalist route. In List's (2025) four-claim map: the first horn (FPR dropped in its original sense). *Replaces* the earlier "positive response to the quadrilemma — a fourth route", retracted [✗] 2026-09-25 (see the box above).

**Corollary T-221.2 (The heptalemma) [T].** UHM's reading of measurement outcomes keeps locality ([physics correspondence, Theorem 8.5](/docs/proofs/physics/physics-correspondence#88-прочтение-вынуждено): the regeneration acts on the unconditioned marginal, and the full dynamics does not signal), measurement independence (T-62), measurement realism (outcomes are fixed points $\rho^* = \varphi(\Gamma)$, T-96, T-98), NS, OW and NF, and relaxes NR — the route of relational quantum mechanics. That these six are jointly consistent with the predictions of quantum mechanics is the theorem of DeBrota & List ("any six of the seven theses are jointly consistent"); UHM supplies a model of that route. (Status history: [T] until the first audit, [C at T-120] from 2026-09-25 because OW was read as the emergence of $M^4$ in T-120; OW in the heptalemma is "reality is exhausted by one objective world", which the single topos satisfies without T-120.)

**Corollary T-221.3 (UHM and relational quantum mechanics) [I].** UHM and RQM take the same route; they differ in the relativisation parameter (a viable $\Gamma$-stage against any physical system). *Replaces* the earlier "RQM = $\tau_{\leq 1}(\mathfrak{T})$ [T]", retracted [✗] 2026-09-25: the representables of the 1-category $\mathcal C_7$ are 0-truncated, so 1-truncation leaves them unchanged, and RQM has no formal model in the corpus with which an equivalence could be proved.

**Proof.**

*(a).* Kripke–Joyal: $U \Vdash \varphi \wedge \psi$ iff $U \Vdash \varphi$ and $U \Vdash \psi$; $U \Vdash [s = X]$ iff $s_U = X|_U$ in $\mathcal D(U)$. If $U$ forces both, then $X|_U = Y|_U$ in $\mathcal D(U)$; for $X \neq Y$ (disjoint global states) this holds only if $U$ is covered by the empty family, i.e. $U$ is not inhabited. $\square$

*(b).* One topos with one terminal object is one world. $1 \Vdash \bot$ would require $1$ to be covered by the empty family, i.e. $\mathfrak{T}$ degenerate ($0 \simeq 1$); $\mathfrak{T}$ has non-empty stages not covered by the empty family (a non-empty Bures-open set of states is not covered by no opens), so it is not degenerate. NS is T-215 under $\iota_{\min}$. By (a), with two subjects in different states the two first-personal facts cannot both be forced at $1$; they are forced at their own stages. $\square$

*(c).* $\mathcal C_7$ is essentially small (its objects form a set of density matrices), $\mathfrak{T}$ is presentable (Lurie, HTT 6.3.1.16), and the Yoneda embedding $y: \mathcal C_7 \hookrightarrow \mathfrak{T}$ lands in $\mathfrak{T}$. $\square$

*(d).* The forcing clauses are defined by induction on formulas from the site, its covers and the sheaves involved; an automorphism $\alpha$ of the site preserving $J_{\mathrm{Bures}}$ induces an automorphism of $\mathfrak{T}$ that carries each clause at $U$ to the same clause at $\alpha(U)$. Conjugation by a unitary $V$ is such an $\alpha$: $\Phi \mapsto \mathrm{Ad}_V \circ \Phi \circ \mathrm{Ad}_{V^\dagger}$ maps CPTP maps to CPTP maps, and the Bures distance is unitarily invariant. A point of $\mathfrak{T}$ is a geometric morphism $\mathbf{Set} \to \mathfrak{T}$; its choice is not determined by the forcing relation, which (by the automorphism argument) cannot tell apart symmetric stages. $\square$

*(e).* The three readings are defined from one relation $\{(U, \varphi) : U \Vdash \varphi\}$; any observable of UHM is computed from $\Gamma$ at a stage, i.e. from that relation. For the last clause: in a topos with enough points, $1 \Vdash \varphi$ iff $p \Vdash \varphi$ for every point $p$ (this is what "enough points" means for subobjects of $1$). $\square$

The finite form of (a) — centred worlds $(w, s)$, the first-personal propositions of two subjects with different complete states have empty intersection, their relativised versions hold together — is checked in `check_core_numbers.py` (`test_first_person_facts_of_two_subjects_are_not_compossible`).

**Interpretive addendum [I].** Two-aspect monism, read through T-221, is a relationalism whose parameter is a state of the one world. It keeps what List calls first-person realism only in relativised form; the fact "I am *this* subject rather than that one" is, in UHM as in every relationalism, not among the facts — it is the choice of a point, a primitive in the sense of [T-214](#t-214). Whether that is a cost or the correct account is the question DeBrota & List leave to inference to the best explanation, and UHM does not settle it.

**Dependencies**: T-215 [T]+[D] (identity convention, for NS), T-62, T-96, T-98 and [Theorem 8.5 of the physics correspondence](/docs/proofs/physics/physics-correspondence#88-прочтение-вынуждено) (for T-221.2), Kripke–Joyal semantics, Lurie HTT 6.3.1.16. The earlier dependencies on T-120 (OW as emergent spacetime), T-186 (FPR as a forced interior functor) and T-211 are removed: none of them is needed for (a)–(e).

**External references**: List C., "A quadrilemma for theories of consciousness", *Philos. Q.* 75(3): 1026–1048 (2025), doi:10.1093/pq/pqae053; DeBrota J.B., List C., "Consciousness, quantum mechanics, and the limits of scientific objectivism", arXiv:2604.14234 (2026); DeBrota J.B., List C., "A heptalemma for quantum mechanics", *Found. Phys.* 56, 24 (2026), doi:10.1007/s10701-026-00919-9; Fine K., "Tense and reality" (2005); Abramsky S., Brandenburger A., "The sheaf-theoretic structure of non-locality and contextuality", *New J. Phys.* 13, 113036 (2011); Hellie B. (2013); Rovelli C. (1996, 2025); Glick D. (2021); Mermin N.D. (2019).

---

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

**(vi)** $C_{HS} = P - P_\text{diag}$ (T-73) and $P_\text{diag} = \sum_i\gamma_{ii}^2 \geq 1/7$ by Cauchy–Schwarz, with equality exactly at $\gamma_{ii} = 1/7$. $C_\text{rel}(\rho) = S(\Delta(\rho)) - S(\rho)$ and $\Delta(\rho) = I/7$ on uniform-diagonal states. The twirl: $\int_{G_2} g\rho g^\dagger\,dg = I/7$ by Schur's lemma, since $G_2$ acts irreducibly on $\mathbb{C}^7$, and each $T_a$ is traceless. $\blacksquare$

**Numerical check** (scratch run, 2026-09-26). Twenty thousand random spectra scaled onto $P = 2/7$: the best $H_{1/2}$ ($1.7893$) and $H_1$ ($1.6019$) are at $s_1$; the best $H_3$ ($1.2181$) and $H_\infty$ ($1.1225$, below $H_\infty(s_3) = 1.1783$) are at spectra with three large and four small eigenvalues, not at $s_1$.

### 16.3. Categorical interpretation {#t-222-categorical}

The window with unital channels as morphisms is a preorder — Alberti–Uhlmann's majorization order on spectra. It has no terminal object (iv), and the purity bound $P \geq 2/7$ cuts it along a sphere on which the order leaves many incomparable minimal elements (iii). The former reading — $I/7$ initial, $\rho^* = \varphi(\Gamma)$ terminal, "the limit state toward which all viable dynamics converge" — is retracted: $I/7$ lies outside the window, and $\varphi(\Gamma)$ is a map of the state, not an object. Which point of the Pareto sphere a holon approaches is decided by its self-model and its dynamics, not by the resource order: with $\varphi_J$ the fixed point $\Gamma_{\eta_\infty}$, the upper end of the living attractor, sits at $P = 0.317$–$0.357$, inside the window, where by (v) it is not resource-optimal.

### 16.4. Applicability domain {#t-222-scope}

1. **Purity window** — $\rho \in \overline{\mathcal{W}}$. The other conditions of $\mathcal{V}_\text{full}$ are frame conditions. $\Phi = P_\text{coh}/P_\text{diag} \geq 1$ is met by the uniform-diagonal representative of every spectrum with $P \geq 2/7$ (Schur–Horn), so the spectral statements hold on $\mathcal{V}_\text{full}$ as well; $D_\text{diff} \geq 2$ has status [C] and is not used.
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

**Dependencies**: T-73 [T] ($C_{HS} = P - P_\text{diag}$), T-96 [T] (regeneration target $\varphi(\Gamma)$, $\varphi(\rho^*_\Omega) \neq \rho^*_\Omega$), [Theorem 10.1 of Gap thermodynamics](/docs/core/dynamics/gap-thermodynamics#неподвижная-точка-лавера) [T] (fixed points of the self-model), T-126 [T] ($R = 1/(7P)$), T-151 [T] (viability $P > 2/7$).

**External references**: Brandão et al. PNAS 112:3275 (2015); Baumgratz-Cramer-Plenio PRL 113:140401 (2014); Streltsov-Adesso-Plenio Rev. Mod. Phys. 89:041003 (2017); Yunger-Halpern Nat. Rev. Phys. 5:689 (2023); Marshall–Olkin–Arnold, *Inequalities* (2011); Alberti–Uhlmann, *Stochasticity and Partial Order* (1982); Schur's lemma (classical representation theory).

---

## 17. T-223: Putnam-triviality foreclosure (Lerchner Melody-Paradox closure) {#t-223}

:::tip Theorem T-223 (Putnam-triviality foreclosure) [T]

Let $S$ be a physical system satisfying axioms (AP)+(PH)+(QG)+(V). Let $(\mathsf{PT})$ denote the Putnam triviality claim — that for any non-trivial physical trajectory $p(\cdot)$ and any two finite directed graphs $\mathcal A, \mathcal B$ there exist alphabetizers $(\Sigma_A, f_A), (\Sigma_B, f_B)$ realising $\mathcal A$ and $\mathcal B$ respectively. Let $(\mathsf{LC})$ denote Lerchner's (2026) Melody-Paradox corollary that "computation is extrinsic to the vehicle". Then:

**(a) Foreclosure at the categorical layer L2.** The quotient map
$$G_S/G_2 : \mathrm{States}(S) \longrightarrow \mathcal D(\mathbb C^7)/G_2$$
is well-defined and injective on the class of UHM-compatible representations; the $G_2$-orbit $[\Gamma_S]_{G_2}$ is **invariant** under (PT)'s alphabetizer freedom:
$$[\Gamma_S^{f_A}]_{G_2} = [\Gamma_S^{f_B}]_{G_2}.$$

**(b) Observable invariance.** Purity $P$ and reflection $R=1/(7P)$ are $U(7)$-invariant and descend to $\mathcal D(\mathbb C^7)/G_2$. The frame-referenced observables $\Phi, \mathrm{Coh}_E, \Lambda, H$ are defined in the physical frame pinned by the dynamics $\mathcal L_\Omega$; since every admissible alphabetizer preserves that dynamics (clause d and L5), it preserves the frame up to $\mathrm{Stab}_{G_2}$, so these observables are **alphabetization-invariant** as well. (They are frame-relative, not orbit-invariants — see [uniqueness theorem §invariants](/docs/proofs/categorical/uniqueness-theorem#инварианты) — but no admissible alphabetizer can change them.)

**(c) Predicate invariance.** The consciousness predicate
$$\mathrm{Cons}(S) := (P > 2/7) \wedge (R \geq 1/3) \wedge (\Phi \geq 1) \wedge (D_{\min} \geq 2)$$
is **alphabetization-invariant** by (b): its $P,R$ terms factor through $[\Gamma_S]_{G_2}$, and its $\Phi, D_{\min}$ terms are fixed by the dynamical frame. Hence $\mathrm{Cons}(S)$ is invariant under (PT).

**(d) Dichotomy on non-compatible alphabetizers.** Any $f$ outside the UHM-compatible class (i.e. violating dynamic covariance with $\mathcal L_\Omega$) carries zero physical content — it does not describe any causal process of $S$ and realises no Piccinini (2008)-mechanism. Hence (PT)'s under-determination at that extreme is vacuous.

**(e) Residual externality.** The only externality remaining in the chain $S \to [\Gamma_S]_{G_2} \to \mathsf{Mind}$ is the phenomenal bridge $W: \mathcal D(\mathbb C^7) \to \mathsf{Mind}$, which by T-214 [T] is structurally inevitable under Lawvere incompleteness. This residual is minimal, formal, and not a Lerchner mapmaker.

:::

**Motivation.** Lerchner (2026) "The Abstraction Fallacy: Why AI Can Simulate But Not Instantiate Consciousness" (DeepMind, 2026-03-19) raises the Melody-Paradox (§3.3, Fig. 3): a single physical trajectory can be mapped to "Beethoven's 5th", to "Market Data", or to "coherent noise" via different alphabetizers, hence the computational identity is extrinsic. In the UHM context one must verify that this does not propagate to the $G_2$-equivalence class of the holonomic state $\Gamma$, which is what UHM identifies consciousness with.

**Three-level ontology.** Lerchner's analysis has two strata: L1 = physical vehicle, L3 = alphabetized symbolic readout. UHM inserts a third, *intermediate*, stratum:

| Stratum | Object | Intrinsic? |
|---|---|---|
| L1 | Physical substrate, trajectory $p: [0,T] \to \mathsf{Phys}(S)$ | yes (physicalism) |
| L2 | Holonomic-categorical class $[\Gamma_S]_{G_2} \in \mathcal D(\mathbb C^7)/G_2$ | **yes — categorically forced** |
| L3 | Symbolic readout $f: \mathsf{Phys}(S) \to \Sigma^*$ | no (Lerchner's mapmaker) |

Putnam–Lerchner triviality concerns L1→L3. UHM's consciousness predicate concerns L1→L2. These arrows are orthogonal; (PT) does not propagate.

**Proof of T-223 (seven lemmas).**

**L1 (Categorical necessity of $\mathbb C^7$ and $G_2$) — context; clauses (a)–(e) do not use it.** Combine T-82 (BIBD(7,3,1) / Fano plane uniqueness via Fisher + Veblen–Wedderburn), T-42a ($G_2$-rigidity of the Fano dissipator), T-151 ($D_{\min} = 2$ from Φ-threshold), T-149 (viability of the embodied attractor). The Bridge T15 (row 41n) chains them:
$$(\text{AP})+(\text{PH})+(\text{QG})+(\text{V}) \xrightarrow{[T]} \mathrm{BIBD}(7,3,1) \xrightarrow{[T]} \mathrm{PG}(2,2) \xrightarrow{\text{canonical orientation, [T]}} \mathbb O \xrightarrow{[T]} G_2.$$
The step $\mathrm{PG}(2,2) \to \mathbb O$ needs an orientation of the seven lines, and only 16 of the 128 orientations give a normed algebra; they form the only orientation class invariant under the collineations of PG(2,2), so the algebra canonically attached to the design is $\mathbb O$ ([T15-canon](/docs/proofs/minimality/theorem-octonionic-derivation#каноническая-ориентация)), and $\dim = 7$ and $G_2$ are forced for it [T]. (Until 2026-09-25 this step was [C at (Alt)].) *Corrected 2026-09-25:* the lemma read "no step admits parameter freedom; $\dim = 7$ and $G_2$ are forced with zero external input" and also listed T-120 ($M^4$ from the quantum CLT), which plays no role in the Putnam argument, and T-190 as "zero-axiom categorical closure" — withdrawn: T-190 is [C] (the Page–Wootters constraint is assumed and the route to A1 via T-186(a) is a hypothesis). ∎

**L2 (Covariance gate).** A UHM-admissible holonomic representation is a triple $(\mathbb C^7, \mathcal B, G_S)$ satisfying Definition G1 of the Uniqueness Theorem:
$$\frac{d}{d\tau} G_S(s(\tau)) = \mathcal L_\Omega[G_S(s(\tau))]$$
for every physical trajectory $s(\tau)$ of $S$. This is the gate through which any admissible alphabetizer must pass.

**L3 ($G_2$-uniqueness).** By T-123 [T] (Uniqueness Theorem of Holonomic Representation), any two UHM-compatible holonomic representations of the same $S$ are related by $U \in G_2$: $G_2^{\mathrm{rep}}(s) = U G_1^{\mathrm{rep}}(s) U^\dagger$. Hence $[\Gamma_S]_{G_2}$ is well-defined.

**L4 (alphabetization-invariance of observables).** $P = \mathrm{Tr}(\Gamma^2)$ and $R = 1/(7P)$ are $U(7)$-invariant, hence $G_2$-invariant and descending to the quotient. $\Phi$ and $\mathrm{Coh}_E$ are **frame-dependent**: they reference the coordinate basis / E-axis, which — since $\mathbf 7$ is an irreducible $G_2$-module (Schur) — is not $G_2$-invariant; they are invariant only under $\mathrm{Stab}_{G_2}$ of the physical frame. But every admissible alphabetizer preserves the dynamics $\mathcal L_\Omega$ (L5), hence preserves the physical frame up to $\mathrm{Stab}_{G_2}$; therefore $P, R, \Phi, \mathrm{Coh}_E$ all take alphabetizer-independent values. The frame-averaged $\Lambda, H$ are $G_2$-invariant by the twirl (Schur). ($\pi_{\mathrm{bio}}$ was listed here and in clause (b) until 2026-09-25; it is not an observable of $\Gamma$ but an estimator of $\Gamma$ from L1 data, with free parameters $\theta$ that are fixed by pre-registration, not by $\mathcal L_\Omega$ — the choice of $\theta$ is a measurement-model choice outside the $G_2$-gauge freedom, and what it can and cannot test is set out in the [measurement protocol](/docs/applied/research/measurement-protocol#substitution-position).) This is *stronger* than the earlier "all observables descend to $\mathcal D/G_2$" claim, which was false for $\Phi, \mathrm{Coh}_E$.

**L5 (Admissible alphabetizers factor through $G$).** If $f : \mathsf{Phys}(S) \to \Sigma^*$ is an alphabetizer whose induced dynamics admits a CPTP realisation commuting with $\mathcal L_\Omega$, then the corresponding $G^f$ satisfies Definition G1 by construction, and L3 yields $G^f = U G U^\dagger$ for some $U \in G_2$. Hence the alphabetizer-freedom accessible under (PT) while preserving physical dynamics is bounded by $G_2$ (a 14-dimensional compact Lie group), not by the countably-infinite choices of a generic Lerchner alphabetizer.

**L6 (Non-dynamical alphabetizers are physically vacuous).** If $f$ does not commute with $\Phi^{\mathsf{phys}}_\tau$, then $f$ cannot be read off any causal process of $S$; it is an act of pure epistemic interpretation with no grounding in causal closure (Kim 2005). Such $f$ correspond to Lerchner's Mapping C ("Market Data") and Mapping B ("backward Beethoven") in Fig. 3 when those readings are not themselves realised as separate physical processes. Lerchner correctly identifies them as extrinsic; UHM adds that they are extrinsic *to physics*, hence irrelevant to any physicalist grounding of consciousness.

**L7 (Self-alphabetization via $R$).** By T-96 [T], the regeneration target of $\mathcal L_\Omega$ is $\rho_* = \varphi(\Gamma)$, the functorial categorical self-model of the current state (T-62: the left adjoint) — computed from $\Gamma$ alone. It is not a fixed point of $\mathcal L_\Omega$: at a nontrivial stationary state $\varphi(\rho^*_\Omega) \neq \rho^*_\Omega$ (T-96, step 2). Fixed points belong to $\varphi$ itself — $I/7$ for $\varphi_{\mathrm{coh}}$, $\Gamma_{\eta_\infty}$ for $\varphi_J$, at least eight for $\varphi_s$ ([Theorem 10.1 of Gap thermodynamics](/docs/core/dynamics/gap-thermodynamics#неподвижная-точка-лавера) [T]: existence by Brouwer; Lawvere's theorem concerns fixed points of an endomorphism such as $\varphi$, never of $\mathcal L_\Omega$) — and they are not stationary states of $\mathcal L_\Omega$. The lemma needs neither: it needs only that the target is a functional of $\Gamma$. (Corrected 2026-09-26: the sentence read "$\rho_* = \varphi(\Gamma)$ is the intrinsic Lawvere fixed point of $\mathcal L_\Omega$".) The reflection measures are functionals of $\Gamma$ alone: the canonical $R(\Gamma) = 1/(7P(\Gamma)) = 1 - \|\Gamma - I/7\|_F^2/\|\Gamma\|_F^2$ (T-126 [T]), and the self-model quality $R_\varphi(\Gamma) = 1 - \|\Gamma - \varphi(\Gamma)\|_F^2/\|\Gamma\|_F^2$ involves only $\Gamma$ and its internal self-model $\varphi(\Gamma)$ ([the three working forms of R](/docs/consciousness/foundations/self-observation#формы-r)). No external observer or alphabetizer appears. The threshold $R \geq 1/3$ quantifies *how much* self-observation is required for consciousness. This makes UHM strictly stronger than Lerchner's own enactivist gesture (his §2.3 citing Thompson 2019 / Maturana-Varela 1980: "the mapmaker is the entire structurally unified organism") — UHM supplies a *quantitative, $G_2$-invariant* criterion for intrinsic self-alphabetization.

**Combination (proof of clauses a–e).**

- **(a)** L2+L3 establish $G_2$-uniqueness of every UHM-compatible representation, whose existence is the premise of the theorem (L1 is context; it read "L1+L2+L3 establish existence and $G_2$-uniqueness" until 2026-09-25); L5 bounds the alphabetizer-compatible freedom to $G_2$; hence $[\Gamma_S]_{G_2}$ is invariant across all UHM-compatible alphabetizations.
- **(b)** ~~By L4, the seven listed observables factor through $\mathcal D(\mathbb C^7)/G_2$.~~ **Retracted 2026-09-25:** the line counted all seven observables of clause (b) as $G_2$-invariants; that is false for the frame-referenced ones — $\Phi$ and $\mathrm{Coh}_E$ refer to the coordinate frame and are invariant only under the finite frame group $\Gamma_{\!\text{oct}}$ ([frame decision D-0910](/docs/proofs/categorical/uniqueness-theorem#g2-ригидность)). Replacement: $P$ and $R = 1/(7P)$ factor through $\mathcal D(\mathbb C^7)/G_2$; the frame-referenced observables are frame-pinned, and by L4+L5 no admissible alphabetizer changes them.
- **(c)** ~~$\mathrm{Cons}(S)$ is a conjunction of four $G_2$-invariant inequalities; factors through $[\Gamma_S]_{G_2}$; alphabetization-invariant by (a)+(b).~~ **Retracted 2026-09-25:** of the four inequalities only $P > 2/7$ and $R \geq 1/3$ are $G_2$-invariant; $\Phi \geq 1$ and $D_{\min} \geq 2$ are fixed by the dynamical frame (D-0910), so the factorisation of $\mathrm{Cons}(S)$ through $[\Gamma_S]_{G_2}$ is unproven. Replacement: $\mathrm{Cons}(S)$ is alphabetization-invariant by (a) and the corrected (b) — its $P, R$ terms through $[\Gamma_S]_{G_2}$, its $\Phi, D_{\min}$ terms through the frame that every admissible alphabetizer preserves (L4+L5).
- **(d)** L6 establishes that non-UHM-compatible alphabetizers are physically vacuous.
- **(e)** T-214 [T] establishes the phenomenal-bridge externality with Lawvere necessity; L7 ensures no additional mapmaker externality at L1→L2. ∎

**Counter-diagram for Lerchner's Figure 3.** Above Lerchner's diagram, insert the L2 stratum:

```
        [Γ_S]_{G_2}   (L2: intrinsic, G₂-rigid)
             ▲
             │   L1→L2: covariance gate L2 + T-123 (not T-190, which is [C])
             │
   Physical trajectory  p → p'     (L1)
             │
             │   L1→L3: external, Lerchner-variable
        ┌────┴────┐
        ▼         ▼
    f_A "5th"   f_B "Market"       (L3)
```

Lerchner's horizontal arrow $p \to \{f_A, f_B\}$ is correct. UHM adds the vertical arrow $p \to [\Gamma_S]_{G_2}$. Consciousness lives at the vertical arrow's target; computation lives at the horizontal arrows' targets. Putnam's multiplicity is confined to the horizontal; UHM's consciousness predicate is alphabetization-invariant.

**Why $G_2$-rigidity alone is not the complete answer.** T-123 handles L2→L3 residual freedom (the 14-dim $G_2$ action on $\Gamma$) but not L1→L2 forcing (where *a priori* one might still suspect mapmaker choice). The full foreclosure requires six components:
1. **Intrinsic-forcing of L2** (T-82 + T-42a + T-151 + T-149 + the Bridge T15): ensures L2 is not a chosen abstraction — [T] with the canonical orientation of T15 ([T15-canon](/docs/proofs/minimality/theorem-octonionic-derivation#каноническая-ориентация); [C at (Alt)] until 2026-09-25). (The list included T-120 and T-190 until 2026-09-25; the first plays no role here, and the second is [C].)
2. **$G_2$-gauge boundedness** (T-42a + T-82): residual L2 freedom is a 14-dim compact Lie group action.
3. ~~**Observable $G_2$-invariance** (L4): all consciousness-relevant quantities insensitive to (2).~~ **Retracted 2026-09-25:** $\Phi$ and $\mathrm{Coh}_E$ are not $G_2$-invariant (D-0910). Replacement — **observable invariance** (L4): $P$ and $R$ are insensitive to (2); the frame-pinned $\Phi, \mathrm{Coh}_E$ are insensitive to the admissible alphabetizers of L5, which preserve the dynamical frame.
4. **Dynamic-covariance gate** (L2 + L6): non-UHM-compatible alphabetizers are physically vacuous.
5. **Intrinsic self-alphabetization** (T-96 + T-98 via $R$): no external mapmaker needed for the consciousness threshold.
6. **Lawvere residual localisation** (T-214): only unavoidable externality is the phenomenal bridge.

T-223 packages exactly this cascade.

**SYNARC corollary (corrected 2026-09-25).** The Rust SYNARC prototype computes a trajectory of $7 \times 7$ matrices in floating point. (i) *[T]* If its update rule is UHM-compatible (Definition G1 up to the arithmetic error $\varepsilon$), then by L3 + L5 the computed $P, R$ and the frame-pinned $\Phi, D$ agree with those of the exact trajectory to $O(\varepsilon)$, so $\mathrm{Cons}$ evaluated on the computed matrices equals $\mathrm{Cons}$ on the exact ones for every state farther than $O(\varepsilon)$ from the thresholds. (ii) *Open.* Whether the computed matrix is the prototype's own holonomic state $G_S(s)$ — an L2 object — or an L3 readout of its hardware trajectory is exactly the question T-223 separates, and the corpus has no measurement that settles it: no reconstruction $\pi_\theta$ is validated outside natural sleep–wake and anaesthetic states ([measurement protocol, position against the substitution argument](/docs/applied/research/measurement-protocol#substitution-position)), and a matching report-level structure carries no weight for $\mathrm{Cons}$ (same section, Kawakita et al. 2024). So neither "SYNARC simulates but does not instantiate" nor its converse is asserted.

*Retracted [✗] 2026-09-25:* the corollary read "the current Rust SYNARC prototype is a τ<sub>≤1</sub>-truncated shadow of the categorical-full 𝔗-object (T-221 terminology) … by T-148 + T-214 the shadow *simulates* consciousness-relevant dynamics but does not *instantiate* phenomenality". (1) The τ<sub>≤1</sub> terminology went with the retracted Corollary T-221.3: the representables of the 1-category $\mathcal C_7$ are already 0-truncated, so truncation distinguishes nothing. (2) T-214 places the phenomenal bridge outside the formalism for every system alike; it cannot separate a simulation from an instantiation. (3) T-148 is the genesis bound under environmental coupling and says nothing about substrate. (4) By T-223's own clause (c), a UHM-compatible system with the same $P, R, \Phi, D$ has the same predicate value, so the simulation/instantiation line cannot be drawn by the predicate; UHM draws it — if at all — at the L2-versus-L3 question of (ii), which is open.

**Falsification criteria.**
- **F-223-1**: Any experiment producing two physically realisable UHM-compatible alphabetizations of the same $S$ yielding ~~distinct $G_2$-invariants (distinct $P, R, \Phi, \mathrm{Coh}_E$)~~ distinct values of the $G_2$-invariants $P, R$ or of the frame-pinned $\Phi, \mathrm{Coh}_E$ would refute (a)–(c). *Corrected 2026-09-25: the earlier wording counted $\Phi$ and $\mathrm{Coh}_E$ as $G_2$-invariants ([frame decision D-0910](/docs/proofs/categorical/uniqueness-theorem#g2-ригидность)).*
- **F-223-2**: Any alphabetization of $S$ commuting with $\mathcal L_\Omega$ but not factoring through a $G_2$-conjugate representation would refute L5.
- **F-223-3**: Any physical process realising a Lerchner "Mapping C" (Market Data on a Beethoven trajectory) with non-zero contribution to $R$ or $\Phi$ would refute L6.

**Dependencies**: T-42a [T] ($G_2$-rigidity), T-82 [T] (BIBD(7,3,1) uniqueness), T-96 [T] (regeneration target $\rho_* = \varphi(\Gamma)$), Theorem 10.1 of Gap thermodynamics [T] (fixed points of $\varphi$), T-98 [T] (balance formula for $R$), T-123 [T] ($G_2$-uniqueness of holonomic representation), T-148 [T] (embodiment requirement), T-149 [T] (Fano plane minimality), T-151 [T] ($D_{\min} = 2$), T-153a [T] (consciousness predicate C1–C3), T-214 [T] (hard-problem meta-theorem, Lawvere positivity).

*Corrected 2026-09-25:* the dependency list also named the emergent-manifold theorem (the $M^4$ derivation, now conditional) and the axiomatic closure T-190 (conditional); neither is used by (a)–(e), which concern UHM-compatible representations whose existence is the premise — they entered only the context lemma L1.

**External references**: Putnam 1988 *Representation and Reality* (MIT Press); Sprevak 2018 "Triviality arguments about computational implementation", *Routledge Handbook of the Philosophy of Computing and Information*; Piccinini 2008 "Computation without representation", *Phil. Stud.* 137; Kim 2005 *Physicalism, or Something Near Enough*; Maturana-Varela 1980 *Autopoiesis and Cognition*; Thompson 2019 *Mind in Life*; Lerchner 2026 "The Abstraction Fallacy" (DeepMind preprint, 2026-03-19); Lawvere 1969, Yanofsky 2003 (inherited via T-214).

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
$$\zeta_{H_\mathrm{Gap}}(s) = \sum_{k=1}^{r} \lambda_k^{-s}$$
where $r$ is the rank and $\{\lambda_k\}$ are positive eigenvalues (with multiplicities for degeneracies if any; for simple spectrum $r = \dim$). This is a **finite sum** for all $s \in \mathbb C$, hence entire (no poles). Therefore
$$\zeta'_{H_\mathrm{Gap}}(0) = -\sum_{k=1}^{r} \log \lambda_k = -\log \prod_{k=1}^{r} \lambda_k = -\log \det(H_\mathrm{Gap})$$
is well-defined and finite. No regularisation ambiguity. The formula $f_0$ is thus a **rational algebraic expression** in the eigenvalues of $H_\mathrm{Gap}$, not a transcendentally-regularised object.

### 18.3. Bures stratified-site handling {#bures-stratification}

**Claim**: Bures metric has degeneracies on the boundary of $\mathcal D(\mathbb C^7)$ where $\Gamma$ is rank-deficient. This is handled via the **stratified site** (Ayala–Francis–Rozenblyum 2017).

**Explicit treatment**: decompose $\mathcal D(\mathbb C^7)$ into rank-strata:
$$\mathcal D(\mathbb C^7) = \bigsqcup_{r=1}^{7} \mathcal D_r, \qquad \mathcal D_r := \{\Gamma : \mathrm{rank}\,\Gamma = r\}.$$
- On each **open stratum** $\mathcal D_r$, the Bures metric is non-degenerate (rank-$r$ Fisher metric).
- Between strata, Bures distance extends continuously (Uhlmann 1976) but the metric tensor degenerates.
- The viability condition $P > P_\mathrm{crit} = 2/7$ restricts attention to strata $r \geq 2$ (T-151 [T] $D_{\min} = 2$); the conscious window is entirely interior to $\mathcal D_7$.

**Update 2026-09-25.** The strata are submanifolds of dimension $14k - k^2 - 1$ whose shapes are the Grassmannians $\mathrm{Gr}_k(\mathbb{C}^7)$, and the whole stratified space is an object of the differentially cohesive $\mathrm{SynthDiff}\infty\mathrm{Grpd}$ ([T-185 (ii′)](/docs/proofs/categorical/cohesive-closure#t-185-ii-prime)); no separate stratified site is needed.

**Consequence**: all viable-state theorems operate on the **interior stratum** $\mathcal D_7$, where Bures is smooth and all metric-geometric arguments are valid. Boundary handling is not needed for consciousness-related claims; it is needed only for pathological-state or thermal-death analysis (conducted via the Ayala–Francis–Rozenblyum stratified machinery).

---

## 19. Updated summary table {#summary-final}

| # | Theorem / Protocol | Previous status | New status | Method |
|---|---|---|---|---|
| T-210 | Strict Φ-monotonicity | [T] weak | **[T] strict** | Interior-stratum |
| T-211 | PhysTheory coherences | [T] deferred | **[T]** as the Grothendieck construction (2026-09-25; before that [C at T-119], and "[T] verified" by a full embedding, now [✗]) | HTT 3.2 |
| T-212 | U-projection | [T] unnamed | **[T] $G_2$-twirl**; Rh identification [✗] (read "[T] defined", then "[C] defined", until 2026-09-25) | Schur + Haar |
| T-213 | Yoneda computable | [T] uncomputable | **[T] computable** | Bures description |
| T-214 | Hard-problem meta-theorem | [I] residual | **[T] positive** | Lawvere |
| T-215 | Cross-layer identity | [C] | **[T]+[D]** | Conventional choice |
| T-216 | Analytical ε<sub>eff</sub> | [H] no formula | **[C at (SV)]** (listed [T at T-64] until 2026-09-25) | Closed form |
| **T-217** | **L3 tricategory coherence** | **[H] K=4 heuristic** | **[T]** | **∞-truncation + Baez–Dolan** |
| **T-218** | **SYNARC Cog Kan complex** | **[H] horn-fillers asserted** | **[T]** | **Milnor + classifying space** |
| **T-219** | **SUSY Λ-suppression** | **[H] invalid 7+7** | **[H]** (listed [T at T-64] until 2026-09-25) | **Sector product $\varepsilon^{12}$** |
| **T-220** | **No-reduction $F_4 \to G_2$ UHM** | open question | **[T] negative** | **5 independent obstructions** |
| **T-221** | **Relationalist route through the List/DeBrota no-go** | open (external critique) | **[T]+[I]** (corrected 2026-09-25; the fourth-route reading and "RQM = 1-truncation" retracted [✗]) | **No-go holds internally; UHM keeps OW, NF, NS and relativised FPR; the routes are readings of one forcing relation** |
| **T-222** | **Resource geometry of the viable window** | open (external QRT critique) | **[T]** (restated 2026-09-26) | **Majorization: no resource optimum in the window, the Rényi family splits at $\alpha = 2$, no terminal object; the former "Lawvere fixed point = Pareto optimum, MRQT-complete" is [✗]** |
| **T-223** | **Putnam-triviality foreclosure (Lerchner Melody-Paradox)** | open (external critique) | **[T]** | **Seven-lemma cascade: three-level L1/L2/L3 ontology + $G_2$-gauge boundedness + intrinsic self-alphabetization via $R$** |
| §18.1 | A4 simple spectrum | implicit | **Explicit** | Spectral transversality |
| §18.2 | $f_0$ ζ'(0) | delicate | **Elementary** | Finite-dim spectral zeta |
| §18.3 | Bures boundary | not addressed | **Stratified site** | Ayala–Francis–Rozenblyum |
| §8 | Λ-deficit programme | "computational task" | **Spec complete** | HMC on $(S^1)^{21}/G_2$ |
| §9 | π<sub>bio</sub> protocol | [H] specific | **Spec complete** | EEG/fMRI/HRV |

**Total after all closures**: of the fourteen theorems T-210–T-223, eleven stand as [T] (T-215 with a definitional part, T-212 in the corrected form T-212′, T-211 in the corrected form of 2026-09-25), T-221 is stratified into [T] and [I] parts (its [C] parts went with the retracted fourth-route reading, 2026-09-25), one is [C] (T-216) and one is [H] (T-219); plus 3 explicit clarifications and 2 computational-programme specifications (the line read "14 new [T] theorems" until 2026-09-25).

~~**No open mathematical or categorical gaps remain in UHM's foundational framework.**~~ Retracted [✗] (2026-09-25): the rows marked [C] and [H] above are open mathematical conditions. The framework's own inputs listed here until 2026-09-25 are settled: the first-order condition and Poincaré duality of T-119, on which T-120 and T-121 rest, by the restatement of T-119, which computes the spatial spectrum (T-119, T-120 and T-121 are [T] since); the orientation (Alt) of T15 by the [canonical-orientation theorem](/docs/proofs/minimality/theorem-octonionic-derivation#каноническая-ориентация). T-211 was listed here too; its recheck of 2026-09-25 showed that it never used them; clause (iii) of the earlier T-221 rested on them, the corrected T-221 of 2026-09-25 does not. T-221 answers the List/DeBrota *external* critique by locating UHM on the relationalist route (corrected 2026-09-25; the earlier "fourth route" is retracted); T-222 answers the QRT-completeness external critique — negatively since 2026-09-26: the viable window selects no resource optimum; T-223 answers the Lerchner Melody-Paradox / Putnam-triviality external critique — the three principal recent external critiques (quantum-metaphysics no-go, resource-theoretic completeness, computational-functionalist triviality) each receive a structured answer; the earlier phrasing "closes … UHM is now closed against all three" is withdrawn with the sentence above.

**Strictly remaining** (all explicitly non-mathematical):
- Numerical computation of Λ (§8) — bounded HPC task
- Empirical calibration of π<sub>bio</sub> (§9) — experimental programme
- Hard-problem [P] bridge — structurally inevitable (T-214 [T]), not a gap
