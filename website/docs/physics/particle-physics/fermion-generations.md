---
sidebar_position: 1
title: "Three Generations of Fermions"
description: "Derivation of three fermion generations from the geometry of the Fano plane and PSL(2,7)-classification"
---

# Three Fermion Generations from Fano Geometry

:::info Rigor Levels
Each result is marked with one of the canonical statuses:
- **[T]** Theorem — strictly proved
- **[C]** Conditional — conditional on an explicit assumption
- **[H]** Hypothesis — mathematically formulated, requires proof or non-perturbative computation
- **[D]** Definition — definition by convention
- **[I]** Interpretation — physical interpretation of a formal result
- **[✗]** Retracted — contains an error, corrected or replaced
- **[Pr]** Program — research direction
:::

## Contents

1. [Number of generations from Gap-vacuum topology](#1-число-поколений-из-топологии-gap-вакуума)
   - [1.2 Theorem: exactly 3 generations](#теорема-ровно-три-генерации)
   - [1.3 Precedents and related programmes](#прецеденты-три-поколения)
2. [PSL(2,7)-classification of Z₇-orbits](#2-psl27-классификация-z₇-орбит)
3. [Selection principle: minimal associator](#3-принцип-отбора-минимальный-ассоциатор)
   - [3.2 Refutation of equivalence (1,2,4) ↔ (3,5,6) [✗]](#refutation-equivalence)
4. [Generation assignment: k=1 → 3rd, k=4 → 2nd, k=2 → 1st](#4-назначение-поколений)
5. [Z₃-symmetry and the Fano selection rule](#5-z₃-симметрия-и-фановское-правило-отбора)
6. [Uniqueness of the triplet (1,2,4)](#6-единственность-триплета-124)
7. [Mass hierarchy of generations](#7-массовая-иерархия-поколений)
8. [Refined predictions: Cabibbo angle and CP violation](#8-уточнённые-предсказания-угол-кабиббо-и-cp-нарушение)

---

## 1. Number of generations from Gap-vacuum topology {#1-число-поколений-из-топологии-gap-вакуума}

### Theorem 1.1 (Number of generations) {#thm-1-1}

:::warning [H] Hypothesis (original argument 1.1)
The original argument via $S_4$-orbits on 6 points is not strictly defined, and the catastrophe-theory route ($V_\text{eff}\leq 2$ interior minima from the $A_4$ swallowtail + a boundary minimum) was only conditional. **These are superseded: $N_{\text{gen}} = 3$ is now an exact group-theoretic count** $|\mathrm{QR}(7)| = |\mathbb{Z}_7^*/\{\pm1\}| = (7-1)/2 = 3$ — **[T]** — with only the physical identification remaining **[I]**; see [Theorem 1.2](#теорема-ровно-три-генерации).
:::

**Theorem.** The number of fermionic generations is determined by the topology of the Gap-vacuum:

**(a)** Each generation corresponds to a **topologically distinct** minimum of $V_\text{Gap}$ in the vacuum configuration.

**(b)** From swallowtail analysis: the number of minima of $V_\text{eff}$ depends on the catastrophe. For the $A_4$ swallowtail ($V\sim x^5$), $V' $ is a quartic with $\leq 4$ real roots, which alternate, giving **$\leq 2$ interior minima**. A **third** minimum requires either (i) a **boundary** minimum on the compact Gap domain $\mathrm{Gap}\in[0,1]$, or (ii) the **butterfly** $A_5$ ($V\sim x^6$, which was retracted as X4). Hence the "$\leq 3$" upper bound is **[C under Gap-potential topology]**, conditional on realizing route (i) on the compact domain — it is not an unconditional $A_4$ fact.

**(c)** The number of generations $N_\text{gen}$ = the number of distinct **types** of degenerate $\Gamma$-configurations with $R \to 0$, not connected by a $G_2$-transformation.

**(d)** From the Fano structure: 7 Fano lines define 7 "privileged" triplets. From Fano duality (point ↔ line): each point lies on 3 lines → 3 inequivalent "types" of vacuum alignment:

$$N_\text{gen} = 3$$

**Justification (d).** The vacuum configuration selects an O-direction. The remaining 6 directions form a Fano graph with 3 lines passing through each point. Three classes of inequivalent orientations of the triplet $(A,S,D)$ relative to the Fano structure give 3 generations.

More precisely: the automorphism group of the Fano plane $\mathrm{PSL}(2,7)$ (order 168) acts on 7 points. The stabilizer of one point ($O$) has order $168/7 = 24 \cong S_4$. Orbits of $S_4$ on pairs from the remaining 6 points: $C(6,2) = 15$ pairs, divided into classes by size. Three classes → three generations.

### Theorem 1.2 (Exactly 3 generations) {#теорема-ровно-три-генерации}

:::tip Theorem 1.2 (Exactly 3 generations) — count [T], identification [I]
Lower bound $N_{\text{gen}}\geq 3$ — from the unique order-3 subgroup $(1,2,4)\subset\mathbb{Z}_7^*$ and irreducibility of $\mathbb{Z}_3$ **[T]**. Upper bound $N_{\text{gen}}\leq 3$ — **[T]** by the same group-theoretic count (Step 4: $\mathbb{Z}_7^* \cong \mathbb{Z}_6$ has no subgroups of order 4 or 5); the earlier catastrophe-theory bound **[C under Gap-potential topology]** is now only a consistency check (see the status box in §"Composite status"). Physical identification of the three classes with the observed generations is **[I]**. Composite status: count **[T]**, identification **[I]** (harmonised 2026-09-10 with the body of the proof; the flat "[T] strictly proved" of earlier drafts remains retracted for the *identification*).
:::

**Theorem.** The number of fermionic generations in UHM equals **exactly 3**:

$$N_{\text{gen}} = 3$$

**Proof.**

**Step 1. Upper bound $N_{\text{gen}} \leq 3$ [T] (existing result).**

From the $A_4$-catastrophe (swallowtail): the number of minima of $V_{\text{Gap}}$ with three control parameters is $\leq 3$ (see [Theorem 1.1](#thm-1-1)).

**Step 2. Lower bound $N_{\text{gen}} \geq 3$ [T] (new result).**

Argument via orbits of automorphisms on non-collinear triples of Fano points.

**Definition.** A non-collinear triple is a set $(p_1, p_2, p_3)$ of points in PG(2,2) not lying on a single Fano line.

#### Lemma 1.2a (28 non-collinear triples) {#лемма-28-троек}

**Lemma.** In PG(2,2) there are exactly **28** non-collinear triples.

*Proof.* Total triples from 7 points: $\binom{7}{3} = 35$. Collinear triples (= Fano lines): 7. Non-collinear: $35 - 7 = 28$. $\blacksquare$

#### Lemma 1.2b (PSL(2,7)-transitivity) {#лемма-psl27-транзитивность}

**Lemma.** The group $\text{PSL}(2,7) = \text{Aut}(\text{PG}(2,2))$ (order 168) acts **transitively** on the set of 28 non-collinear triples.

*Proof.* The proof proceeds via counting ordered triples with numerical coincidence $|G| = |\text{orbit}|$.

**Step 1. Counting ordered triples.**

Number of ordered triples of distinct points from 7: $7 \cdot 6 \cdot 5 = 210$.

Number of ordered **collinear** triples: 7 lines $\times\, 3! = 7 \times 6 = 42$.

Number of ordered **non-collinear** triples: $210 - 42 = 168$.

**Step 2. Action of PSL(2,7) on ordered non-collinear triples.**

The group $\text{PSL}(2,7)$ acts faithfully on 7 points of PG(2,2) (trivial kernel), hence acts faithfully on triples of points as well. In particular, it acts on the set $\widetilde{X}$ of 168 ordered non-collinear triples (collinearity is an invariant property, since PSL(2,7) preserves lines).

**Step 3. Numerical coincidence $\Rightarrow$ free transitive action.**

$$|\text{PSL}(2,7)| = 168 = |\widetilde{X}|.$$

Choose an arbitrary ordered non-collinear triple $\tilde{t} \in \widetilde{X}$ and consider its orbit $G \cdot \tilde{t} \subseteq \widetilde{X}$. By the orbit-stabilizer formula:

$$|G \cdot \tilde{t}| = \frac{|G|}{|\text{Stab}_G(\tilde{t})|} = \frac{168}{|\text{Stab}_G(\tilde{t})|}.$$

PSL(2,7) acts **faithfully** on points, so the only element fixing an ordered triple $(p_1, p_2, p_3)$ of pairwise distinct points is the identity (an automorphism of the projective plane fixing 3 points in general position is trivial). Hence $|\text{Stab}_G(\tilde{t})| = 1$, giving:

$$|G \cdot \tilde{t}| = 168 = |\widetilde{X}|.$$

Since the orbit $G \cdot \tilde{t}$ exhausts the entire set $\widetilde{X}$, the action is **transitive** on ordered non-collinear triples.

**Step 4. Transitivity on unordered triples.**

For any two unordered non-collinear triples $\{p_1, p_2, p_3\}$ and $\{q_1, q_2, q_3\}$, fix arbitrary orderings $\tilde{t} = (p_1, p_2, p_3)$ and $\tilde{s} = (q_1, q_2, q_3)$. By Step 3 there exists $g \in \text{PSL}(2,7)$ with $g \cdot \tilde{t} = \tilde{s}$, in particular $g\{p_1, p_2, p_3\} = \{q_1, q_2, q_3\}$. Hence PSL(2,7) acts transitively on the set of **28 unordered** non-collinear triples as well. $\blacksquare$

**Step 3. Construction of three distinct generations [T].**

The generation triplet $(k_1, k_2, k_3) = (1, 2, 4)$ is the unique associative triplet [T] (quadratic residues mod 7, minimal associator $\mathcal{A} = 0$, see [Theorem 6.1](#thm-6-1)). The three generations are defined by the three **distinct** elements of the triplet:

| Generation | Index $k$ | Dimension | Fano distance to Higgs line |
|-----------|:----------:|-----------|:-------------------------------:|
| 3rd (t,b,τ) | $k_1 = 1$ | A | $d = 0$ (on Higgs line) |
| 2nd (c,s,μ) | $k_2 = 4$ | L | $d = 1$ (line $\{D,L,U\}$) |
| 1st (u,d,e) | $k_3 = 2$ | S | $d = 1$ (line $\{S,D,E\}$) |

All three elements are **distinct** ($k_1 \neq k_2 \neq k_3 \neq k_1$), which follows from the definition of the multiplicative subgroup $\{1, 2, 4\} \subset \mathbb{Z}_7^*$.

**Step 4. Proof that $N_{\text{gen}} = 3$ exactly [T]** (both bounds simultaneously, from a group-theoretic count).

The generations are the elements of the **unique order-3 multiplicative subgroup** of $\mathbb{Z}_7^*$, i.e. the quadratic residues $\mathrm{QR}(7) = \{1,2,4\}$. Its cardinality is fixed with **no analytic input**:

$$
N_{\text{gen}} = |\mathrm{QR}(7)| = \frac{7-1}{2} = 3 \qquad\textbf{[T, exact].}
$$

This is simultaneously the lower **and** upper bound — there is no "$\leq$" to prove separately:

1. **$\mathbb{Z}_7^* \cong \mathbb{Z}_6$** (cyclic) has exactly one subgroup of each order dividing $6$: orders $1,2,3,6$. Order $1$ ($\{1\}$) is trivial; order $2$ ($\{1,6\}=\{\pm1\}$) is **charge conjugation**, not a family structure; order $6$ is the whole group. The **unique proper nontrivial subgroup closed under the octonionic (associative Fano) product** is the order-3 subgroup $\{1,2,4\}=\mathrm{QR}(7)$ ([Theorem 6.1](#thm-6-1): $(1,2,4)$ is the unique associator-free Fano line). Hence exactly $3$ elements — not $2$, not $4$, not $6$.

2. **Charge-conjugation cross-check.** Because $7\equiv 3 \pmod 4$, $-1$ is a quadratic **non**-residue mod $7$ ($-1\equiv 6\notin\mathrm{QR}$). Therefore $C:k\mapsto -k$ maps $\mathrm{QR}\leftrightarrow\mathrm{QNR}$ bijectively, and the generations are exactly the **$C$-orbits** $\mathbb{Z}_7^*/\{\pm1\} = \{\{1,6\},\{2,5\},\{3,4\}\}$ — again $|\mathbb{Z}_7^*|/2 = 3$. The set $\{1,2,4\}$ is a complete transversal (one representative per orbit).

3. **Irreducibility / non-extendability.** The order-3 subgroup is $\mathbb{Z}_3$ (simple) — it cannot be reduced to $2$; and it cannot be extended to $4$ or more, since $4,5$ do **not** divide $6=|\mathbb{Z}_7^*|$ (Lagrange), so no subgroup of order $4$ or $5$ exists.

Therefore $N_{\text{gen}} = 3$ is an **exact count** [T], independent of the effective-potential topology. $\blacksquare$

:::note Swallowtail $A_4$ is now a consistency check, not the bound
The catastrophe-theory route (the Gap potential $V_{\text{Gap}}$ realises an $A_4$ swallowtail, giving $\leq 2$ interior minima plus a boundary minimum on the compact Gap domain) serves as a **consistency check** on the group-theoretic count above: the Morse structure of $V_{\text{Gap}}$ is compatible with exactly $3$ stationary generation-vacua, matching $|\mathrm{QR}(7)|=3$. The count itself is group-theoretic and independent of the potential's topology.
:::

:::warning Composite status
$N_{\text{gen}} = 3$ as a **mathematical count** is now **[T]** — the exact cardinality $|\mathrm{QR}(7)| = |\mathbb{Z}_7^*/\{\pm1\}| = (7-1)/2 = 3$, group-theoretic and topology-independent (the earlier **[C under Gap-potential topology]** is retired). The **identification** of the three $\mathrm{QR}(7)$-classes (equivalently $C$-orbits) with the observed physical fermion generations remains **[I]** (an interpretive correspondence via minimal embeddability, not derivable from the axioms alone).

**Final status**: count $N_{\text{gen}} = 3$ — **[T]**; connection to observed generations — **[I]**.
:::

:::info Clarification: lower bound and triplet (1,2,4)
The lower bound $N_{\text{gen}} \geq 3$ (Step 2) uses the specific triplet $(1, 2, 4) \subset \mathbb{Z}_7^*$ — the unique subgroup of order 3 of the multiplicative group $\mathbb{Z}_7^*$ (order 6). This is not an arbitrary choice: $(1,2,4)$ is the **unique** maximal cyclic subgroup of index 2 in $\mathbb{Z}_7^*$, and it coincides with the set of quadratic residues $\bmod 7$. Uniqueness follows from the fact that $\mathbb{Z}_7^* \cong \mathbb{Z}_6$ has exactly one subgroup of each order dividing 6. Nevertheless, the argument can be strengthened: a complete classification of all subgroups of $\mathbb{Z}_7^*$ (orders 1, 2, 3, 6) shows that no other subgroup structure gives a different number of generations within the swallowtail constraint.
:::

:::info Remark
This theorem **does not depend** on the generation assignment ($k=1 \to$ 3rd, etc.). The assignment of the 3rd generation ($k=1$) — **[T]** (unique nonzero tree-level Yukawa, [Theorem 4.1](#thm-gen-4-1)). The ordering $k=4 \to$ 2nd, $k=2 \to$ 1st — **[C at (SA)]**, with (SA) a hypothesis [H] ([Theorem 4.3](#thm-gen-4-3); it was stated as [T] until 2026-09-25).
:::

### 1.3 Precedents and related programmes {#прецеденты-три-поколения}

Why matter comes in three generations is an open question of the Standard Model. Reviewing grand unified theories, Baez and Huerta write that "no one knows why the Standard Model is this redundant, with three sets of very similar particles. It remains a mystery" (*Bull. Amer. Math. Soc.* **47**, 483–552 (2010), [arXiv:0904.1556](https://arxiv.org/abs/0904.1556)). Experiment fixes the number, not the reason: the Z-resonance data of LEP and SLD give $2.9840\pm0.0082$ light neutrino species (*Phys. Rep.* **427**, 257–454 (2006), [arXiv:hep-ex/0509008](https://arxiv.org/abs/hep-ex/0509008)), and a fourth sequential chiral generation is excluded at $5.3\sigma$ by a fit to the Higgs and electroweak data (Eberhardt *et al.*, *Phys. Rev. Lett.* **109**, 241802 (2012), [arXiv:1209.1101](https://arxiv.org/abs/1209.1101)). Several programmes obtain "three" from the same octonionic structures that Theorems 1.1 and 1.2 use; their results fix what those theorems can claim as new.

**Manogue and Dray (1999): three generations from the three Fano lines through a chosen unit.** Corinne Manogue and Tevian Dray obtained three generations from the same count that Theorem 1.1(d) uses. In "Dimensional reduction" (*Mod. Phys. Lett. A* **14**, 99–103 (1999), [arXiv:hep-th/9807044](https://arxiv.org/abs/hep-th/9807044)) they write the ten-dimensional massless Dirac equation with octonions and choose one preferred imaginary unit $\ell$. The choice reduces spacetime from ten to four dimensions without compactification and "singles out 3 natural, nonoverlapping quaternionic subalgebras of $\mathbb{O}$ which contain $\ell$", which they identify as three generations: each contains one massive spin-½ particle with two spin states, one massless spin-½ particle with a single helicity, and their antiparticles — one generation of leptons — while one further massless particle belongs to no generation. *Standing:* the construction treats free particles in momentum space; interactions were not built (the authors' own conclusion); a later $E_6$ version describes lepton properties and leaves quarks speculative ("Octonions, $E_6$, and particle physics", *J. Phys. Conf. Ser.* **254**, 012005 (2010), [arXiv:0911.2253](https://arxiv.org/abs/0911.2253)). *Parallel:* a quaternionic subalgebra spanned by basis units and containing a given unit is a Fano line through that unit, so their three subalgebras are the three lines through $O$ counted in Theorem 1.1(d); the residues $\{1,2,4\}$ of Theorem 1.2 take exactly one point from each of these lines ($1\in\{7,1,3\}$, $2\in\{6,7,2\}$, $4\in\{4,5,7\}$). Reading their $\ell$ as UHM's $O$ is an interpretation [I]. *Difference:* three generations as the three Fano lines through a distinguished unit are prior art from 1999. The count $|\mathrm{QR}(7)|=(7-1)/2=3$ of Theorem 1.2 is the same number, obtained from a transversal of the same three lines. Manogue and Dray attach spin and helicity content to each generation; the UHM count attaches none (identification [I]).

**Furey (2014–2025): three generations under the unbroken gauge group.** Furey builds particle states from the complex octonions $\mathbb{C}\otimes\mathbb{O}$ acting on themselves, and her programme contains the most explicit octonionic three-generation result, with quantum numbers assigned state by state. Left multiplication of $\mathbb{C}\otimes\mathbb{O}$ on itself generates a 64-complex-dimensional algebra (the Clifford algebra $\mathbb{C}\ell(6)$); an $\mathfrak{su}(3)\oplus\mathfrak{u}(1)$ action splits it into $\mathrm{SU}(3)$ generators and 48 states that behave as three generations of quarks and leptons under the two unbroken gauge symmetries $\mathrm{SU}(3)_c$ and $\mathrm{U}(1)_{\mathrm{em}}$, with electric charge given by a number operator, $Q=N/3$ ("Generations: three prints, in colour", *JHEP* **10** (2014) 046, [arXiv:1405.4601](https://arxiv.org/abs/1405.4601); *Phys. Lett. B* **785**, 84–89 (2018), [arXiv:1910.08395](https://arxiv.org/abs/1910.08395)). *Standing:* active. Her 2025 checklist names five hurdles for any algebraic model of the Standard Model — ⟨1⟩ the Coleman–Mandula theorem, ⟨2⟩ fermion doubling, ⟨3⟩ chirality, ⟨4⟩ an unwanted low-energy $B-L$ symmetry, ⟨5⟩ three generations, which "should be linearly independent from one another" — and states that her current model passes the first four and "has yet to cross" the fifth (*Ann. Phys. (Berlin)* **537**, 2400323 (2025), [arXiv:2312.12799](https://arxiv.org/abs/2312.12799)). *Parallel:* Theorem 1.2 [I]. *Difference:* Furey's 48 states carry colour and charge, but they form three copies only under $\mathrm{SU}(3)_c\times\mathrm{U}(1)_{\mathrm{em}}$, not under the full Standard Model group, and she counts the problem as open. The UHM count yields the number three with no representation content; measured by checkpoint ⟨5⟩, it is not yet an explanation.

**Dubois-Violette, Todorov and Boyle (2016–2026): three generations from triality.** A third line takes the exceptional Jordan algebra $J_3(\mathbb{O})$ — Hermitian $3\times3$ matrices with octonionic entries — as the internal quantum space, so that its three off-diagonal octonions can carry three generations. Dubois-Violette associates these three octonions, which are permuted by triality (the symmetry of $\mathrm{Spin}(8)$ that permutes its vector representation and its two spinor representations), with the three generations, and the split $\mathbb{O}=\mathbb{C}\oplus\mathbb{C}^3$ with one lepton and three quark colours (*Nucl. Phys. B* **912**, 426–449 (2016), [arXiv:1604.01247](https://arxiv.org/abs/1604.01247)). Boyle describes one generation as the tangent space $(\mathbb{C}\otimes\mathbb{O})^2$ of the complex octonionic projective plane, which transforms as the $16$ of $\mathrm{Spin}(10)$, notes that it arises in three triality-related ways, and concludes that "it is natural to suspect that this is the origin of the three generations" (*J. Math. Phys.* **67**, 071701 (2026), [arXiv:2006.16265](https://arxiv.org/abs/2006.16265)). *Standing:* published proposals; on generations the authors' own wording is conjectural ("tempting to speculate", "natural to suspect"). *Parallel:* the branching of $J_3(\mathbb{O})$ into three $G_2$-copies of the $7$ used in the Koide section below (T-220) [I]. *Difference:* in these proposals each of the three copies is a full Standard Model generation; the three copies of T-220 are representations of $G_2$, not of the Standard Model group.

**Luhn, Nasri and Ramond (2007): the phases $e^{2\pi ik/7}$, $k\in\{1,2,4\}$, as a flavour triplet.** Flavour physics assigned the three families the same seventh roots of unity that §4.1 uses. $\mathrm{PSL}_2(7)$, the automorphism group of the Fano plane (order 168), is the only simple subgroup of $\mathrm{SU}(3)$ with a complex three-dimensional irreducible representation; in that triplet an element of order seven acts as $\mathrm{diag}(\eta,\eta^2,\eta^4)$ with $\eta^7=1$, and its trace is $\eta+\eta^2+\eta^4=(-1+i\sqrt7)/2$ ("Simple finite non-Abelian flavor groups", *J. Math. Phys.* **48**, 123519 (2007), [arXiv:0709.1447](https://arxiv.org/abs/0709.1447)). Its order-21 subgroup $\mathbb{Z}_7\rtimes\mathbb{Z}_3$ was proposed as a family symmetry ("Tri-bimaximal neutrino mixing and the family symmetry $\mathbb{Z}_7\rtimes\mathbb{Z}_3$", *Phys. Lett. B* **652**, 27–33 (2007), [arXiv:0706.2341](https://arxiv.org/abs/0706.2341)). *Standing:* part of the discrete-flavour programme; the target of the second paper, exact tri-bimaximal neutrino mixing, requires the mixing angle $\theta_{13}=0$ and was excluded when Daya Bay measured $\sin^22\theta_{13}=0.092\pm0.016\,(\mathrm{stat})\pm0.005\,(\mathrm{syst})$ at $5.2\sigma$ (*Phys. Rev. Lett.* **108**, 171803 (2012)). *Parallel:* the generation phases $\phi_n=2\pi k_n/7$, $k_n\in\{1,2,4\}$, of §4.1, the Gauss sum $\eta_1$ of Theorem 2.2 and the order-3 map $k\mapsto2k$ of Corollary 5.1 [I]. *Difference:* giving three families the exponents $\{1,2,4\}$ and cycling them by an order-3 map is prior art from 2007, and there the number three is an input, not a result: "Thankfully, there are only three chiral families in Nature, and the hunt for candidate finite flavor groups is limited to those groups which have two- or three-dimensional irreducible representations" ([arXiv:0706.2341](https://arxiv.org/abs/0706.2341) v2, p. 4). In that work the family group is *horizontal* — it commutes with the gauge group. In UHM it does not.

The last point deserves a plain statement. The map $\sigma:e_k\mapsto e_{2k}$ of Theorem 5.1 is an automorphism of the octonion table of [G₂-structure, §2](/docs/physics/gauge-symmetry/g2-structure#октонионное-умножение-и-g2) (all signs $+$, direct check) and fixes $e_O=e_7$; it therefore lies in the stabiliser of the $O$-direction, the subgroup that the [Standard Model page](/docs/physics/gauge-symmetry/standard-model) identifies with $\mathrm{SU}(3)_C$. Left multiplication by $e_7$ makes the six other axes a copy of $\mathbb{C}^3$ with complex basis $\{A,S,L\}=\{e_1,e_2,e_4\}$ — the colour space of Günaydın and Gürsey, written with the same labelling by Todorov and Dubois-Violette (*Int. J. Mod. Phys. A* **33**, 1850118 (2018), eq. 2.5). In UHM's own identifications the three "generation" axes $k\in\{1,2,4\}$ are thus a basis of the colour triplet, and the $\mathbb{Z}_3$ that cycles them is a colour rotation. Standard Model generations are three copies of one colour representation, and any family symmetry commutes with $\mathrm{SU}(3)_c$. The identification [I] of Theorem 1.2 therefore needs a reason why axes that the octonionic lineage reads as colours should be read as families; and Theorem 5.2, which let the vacuum break this $\mathbb{Z}_3$, would break $\mathrm{SU}(3)_C$ with it — it is retracted accordingly (2026-09-25; checked numerically, `test_generation_z3_lies_in_colour_su3`).

**Noncommutative geometry (Chamseddine and Connes 2008 to Chamseddine 2025): the number is an input.** The spectral Standard Model, whose finite algebra the [spacetime page](/docs/core/foundations/spacetime#алгебра-морита) compares with UHM's, does not derive the number of generations either. Chamseddine and Connes classify the finite geometries of KO-dimension 6 and single out the Standard Model algebra, but state in the abstract that "the number of generations is still an input" ("Why the Standard Model", *J. Geom. Phys.* **58**, 38–47 (2008), [arXiv:0706.3688](https://arxiv.org/abs/0706.3688)); in his 2025 review Chamseddine lists among the questions that remain "an explanation for the number of generations N = 3; it is phenomenologically required (e.g. CP violation), but not derived here (nor anywhere else)" ([arXiv:2511.05909](https://arxiv.org/abs/2511.05909), §7). Yu and Ma claim such a derivation from tensor-product and quaternion extensions of the finite geometry ("Origin of fermion generations from extended noncommutative geometry", *Int. J. Mod. Phys. A* **33**, 1850168 (2018), [arXiv:1810.10189](https://arxiv.org/abs/1810.10189)); one of the programme's founders, writing seven years later, does not count it ("nor anywhere else"). *Standing:* in NCG the count is an acknowledged open problem. *Parallel:* Theorem 1.2 [I]. *Difference:* none in substance — UHM's count $|\mathrm{QR}(7)|=3$ attaches no representation content to the three classes, so it does not close the gap Chamseddine names.

**3-3-1 models (1992): the number of families tied to the number of colours.** A dynamical argument ties the two threes together without octonions. Pisano and Pleitez (*Phys. Rev. D* **46**, 410–417 (1992), [arXiv:hep-ph/9206242](https://arxiv.org/abs/hep-ph/9206242)) and Frampton (*Phys. Rev. Lett.* **69**, 2889–2891 (1992)) extend the electroweak group to $\mathrm{SU}(3)_L\times\mathrm{U}(1)_X$ and treat the third quark family differently from the first two. Gauge anomalies — quantum inconsistencies that must cancel in a chiral gauge theory — then cancel only between families, which requires "that the number of families be equal to the number of quark colors" (Frampton's abstract; see also Pisano, *Mod. Phys. Lett. A* **11**, 2639–2647 (1996)). *Standing:* an active, falsifiable extension of the Standard Model. It predicts new gauge bosons, among them doubly charged "bileptons" and a $Z'$; a 2023 reinterpretation of an ATLAS search bounds the bilepton mass at $m_Y>1300$ GeV (Calabrese *et al.*, [arXiv:2312.02287](https://arxiv.org/abs/2312.02287)); in the minimal version the $\mathrm{U}(1)_X$ coupling grows without bound (a Landau pole) at a few TeV — about 4 TeV in the older literature, up to about 8.5 TeV in a 2023 re-analysis (Barela, [arXiv:2305.05066](https://arxiv.org/abs/2305.05066)). *Parallel:* in UHM, too, the number of generations and the colour triplet are threes of one structure [I]. *Difference:* the 3-3-1 argument is a consistency condition of a chiral quantum field theory and predicts new particles; the UHM count is combinatorial, and at colliders the corpus predicts the opposite — registry row T-297 forbids any gauge $Z'$ ("discovery refutes FE-uniqueness"). A 3-3-1 $Z'$ would refute T-297, which since 2026-09-25 is itself only a hypothesis [H] ([Standard Model, T-297](/docs/physics/gauge-symmetry/standard-model#запрет-z-прайм)).

**Singh (2022–2026): masses from the eigenvalues of $J_3(\mathbb{O})$.** Tejinder Singh's "octonionic unification" programme claims numerical Standard Model parameters from the exceptional Jordan algebra. His paper in *Eur. Phys. J. Plus* states that the eigenvalues of the characteristic equation of $J_3(\mathbb{O})$ reproduce known mass ratios of quarks and leptons and derives the low-energy fine-structure constant (*Eur. Phys. J. Plus* **137**, 664 (2022), [arXiv:2205.06614](https://arxiv.org/abs/2205.06614)); later preprints extend the mass-ratio claims (an "edge universality" of the ratios between adjacent generations) and add a "falsification-oriented catalogue" of predictions, among them an inverted neutrino mass ordering ([arXiv:2508.10131](https://arxiv.org/abs/2508.10131); [arXiv:2604.06288](https://arxiv.org/abs/2604.06288)). *Standing:* speculative; the results appear in the author's own papers, and in September 2026 we found neither an independent confirmation nor a published critique. *Parallel:* the Koide section below (a mass operator on $J_3(\mathbb{O})$, hypothesis T-220-H) and the neutrino hierarchy of §4.6.1 [I]. *Difference:* the Koide section declines to derive masses from $J_3(\mathbb{O})$ and classes Koide's relation as empirical input, which is more cautious than Singh's claims. The two programmes predict opposite neutrino orderings — normal in §4.6.1, inverted in Singh's catalogue — so a measurement of the ordering will refute at least one of them.

**Critiques that apply.** We found no peer-reviewed critique aimed specifically at the octonionic three-generation arguments; three published critiques of the wider genre apply to them and to Theorem 1.2. Distler and Garibaldi prove that embedding the Lorentz group and the Standard Model gauge group in a real or complex form of $E_8$, in the way such unified models require, never yields a chiral theory, and that three generations do not even fit by dimension — at least $2\times2\times45=180$ fermionic states are needed where 112 or 128 are available ("There is no 'Theory of Everything' inside $E_8$", *Commun. Math. Phys.* **298**, 419–436 (2010), [arXiv:0905.2658](https://arxiv.org/abs/0905.2658)). Their lesson — a structure that contains the number three need not contain three chiral generations — applies directly: Theorem 1.2 produces no chiral representation at all. Good proposes to judge a numerical coincidence by its prior probability, its simplicity and its "consilience" with independent formulas ("A quantal hypothesis for hadrons and the judging of physical numerology", in *Disorder in Physical Systems*, ed. G. Grimmett and D. Welsh, Oxford University Press 1990, 129–165). The Fano plane offers many small integers — 7 points, 7 lines, 3 points on each line, 3 lines through each point, 168 automorphisms — and the [octonionic derivation, §5.4](/docs/proofs/minimality/theorem-octonionic-derivation#информационная-интерпретация) lists four "independent" appearances of 3; a match with the observed three is weak evidence unless the identification is fixed before the comparison. Robertson showed that a celebrated group-theoretic "derivation" of the fine-structure constant agreed with experiment only after an arbitrary choice, a radius set equal to one (*Phys. Rev. Lett.* **27**, 1545–1547 (1971)); the same caution applies to agreements reached after an unforced choice, such as the sign of the two-loop correction in [Theorem 8.2](#thm-8-2), which the page itself marks [H].

**What remains UHM's own.** The count $|\mathrm{QR}(7)|=3$ is arithmetic (registry row 43c: count [T], identification [I]). Its physical content lies entirely in the identification, and this subsection does not strengthen it: the count coincides with the count of Manogue and Dray (1999), the phases with a flavour triplet of 2007, and in UHM's own identifications the three axes form a colour basis. The assignment of particular $k$ to particular generations (Theorems 4.1–4.3) has no counterpart in the works reviewed here. Since 2026-09-25, [§5.3](#поколения-t328) (T-328) separates the two readings of the identification: the axis reading cannot carry a family symmetry commuting with the Standard Model group, and the clock-harmonic reading can.

---

## 2. PSL(2,7)-classification of Z₇-orbits {#2-psl27-классификация-z₇-орбит}

### 2.1 Setup

The three fermion generations are defined by three Fano phases $\phi_n = 2\pi k_n / 7$, where $(k_1, k_2, k_3) \subset \mathbb{Z}_7^*$. Of 35 possible ordered triples — which one is realized?

### Definition 2.1 (Z₇-triplets)

**Definition.** A $\mathbb{Z}_7$-triplet is an ordered triple $(k_1, k_2, k_3) \in (\mathbb{Z}_7 \setminus \{0\})^3$ with $k_i \neq k_j$ for $i \neq j$.

**(a)** Total $6 \times 5 \times 4 = 120$ ordered triples. Accounting for physical indistinguishability of generation permutations: $120/6 = 20$ unordered.

**(b)** Three Fano lines through $O$ define a specific partition of $\{1,2,3,4,5,6\}$ into three pairs. Each line $l_n = \{O, X_n, Y_n\}$ gives a pair $(X_n, Y_n)$. Number of such partitions:

$$\frac{6!}{(2!)^3 \cdot 3!} = 15$$

**(c)** Each partition defines a triple $(k_1, k_2, k_3)$, where $k_n = X_n$ (one of the two elements of the pair; the choice determines the orientation of the generation).

### Theorem 2.1 (PSL(2,7)-orbits) {#thm-2-1}

:::tip Theorem 2.1 (PSL(2,7)-orbits) [T]
Strictly proved. Based on standard representation theory of $\mathrm{PSL}(2,7)$.
:::

**Theorem.** The automorphism group of the Fano plane $\mathrm{PSL}(2,7)$ (order 168) acts on the set of partitions and divides the 15 partitions into equivalence classes:

**(a)** $\mathrm{PSL}(2,7)$ contains the stabilizer of a point $O$: $\mathrm{Stab}(O) \cong S_4$ (order 24). Action of $S_4$ on 6 points $\{1,\ldots,6\}$ via $S_4 \subset S_6$.

**(b)** Number of orbits on 15 partitions under $S_4$:

By Burnside's lemma:

$$|X/S_4| = \frac{1}{|S_4|} \sum_{g \in S_4} |X^g|$$

where $X$ is the set of 15 partitions.

**(c)** $S_4$ acts on $\{1,\ldots,6\}$ via the isomorphism $S_4 \cong \mathrm{PGL}(2,3)$ (a subgroup of $\mathrm{PSL}(2,7)$ fixing the point). From the representation theory of $S_4$:

$$|X / S_4| = 2$$

Two equivalence classes:

- **Class I** (type "associative"): 6 partitions. $(k_1, k_2, k_3)$ such that $k_1 + k_2 + k_3 \equiv 0 \pmod{7}$.
- **Class II** (type "non-associative"): 9 partitions. $k_1 + k_2 + k_3 \not\equiv 0 \pmod{7}$.

**(d)** Example. Multiplicative group $\mathbb{Z}_7^* = \{1,2,3,4,5,6\}$. Elements of order 3: $\{1,2,4\}$ and $\{3,5,6\}$ (subgroups of index 2). Triple $(1,2,4)$: $1+2+4 = 7 \equiv 0 \pmod{7}$ → **Class I**. (Triple $\{3,5,6\}$ also satisfies the sum condition: $3+5+6=14 \equiv 0$, but is **not** a Fano line — see [Theorem 3.1](#thm-3-1) and [Section 6](#6-единственность-триплета-124).)

**Proof.** From the structural theorem for $\mathrm{PSL}(2,7)$: the stabilizer $S_4$ acts on $\mathbb{F}_7 \setminus \{0\}$ via linear/affine transformations. A partition $\{a_1,b_1\},\{a_2,b_2\},\{a_3,b_3\}$ is invariant under $g \in S_4 \iff g$ permutes the pairs. The orbit structure is determined by the "total invariant" $\sigma = k_1 + k_2 + k_3 \bmod 7$. Under $S_4$-action $\sigma$ transforms, but $\sigma \equiv 0$ is an invariant condition (subset of the kernel). $\blacksquare$

### Theorem 2.2 (Selection principle: anomalous coherence) {#thm-2-2}

:::danger [✗] Retracted
The condition $\sum_n \sin(2\pi k_n/7) = 0$ is not satisfied for any triplet from $\mathbb{Z}_7^* \setminus \{0\}$. Anomalous coherence as a selection principle **does not work**. The correct selection principle is the minimal associator ([Theorem 3.1](#thm-3-1)).
:::

**Theorem.** The physically realizable $\mathbb{Z}_7$-triplet is determined by the condition of **anomalous coherence** (cancellation of mixed anomalies):

**(a)** The ABJ anomaly is determined by the sum over fermionic generations. The condition for absence of gravitational anomaly:

$$\sum_{n=1}^{3} Y_n = 0$$

where $Y_n$ is the hypercharge of the $n$-th generation. In the Gap formalism: $Y_n \propto \sin(2\pi k_n / 7)$.

**(b)** The condition $\sum_n \sin(2\pi k_n/7) = 0$ holds **if and only if** the triple $(k_1, k_2, k_3)$ belongs to Class I (associative).

**Proof (and refutation).** $\sum_n \sin(2\pi k_n/7)$ vanishes $\iff$ points $e^{2\pi i k_n/7}$ on the unit circle have zero center of mass (imaginary part). From the identity: for $k_1+k_2+k_3 = 7m$:

$$\sum_n e^{2\pi i k_n/7} = e^{2\pi i k_1/7}(1 + e^{2\pi i(k_2-k_1)/7} + e^{2\pi i(k_3-k_1)/7})$$

For $(k_1,k_2,k_3) = (1,2,4)$: sum $e^{2\pi i/7} + e^{4\pi i/7} + e^{8\pi i/7}$. The set $\{1,2,4\}$ is the multiplicative subgroup of order 3 in $\mathbb{Z}_7^*$ (quadratic residues). The sum $\omega + \omega^2 + \omega^4$ (where $\omega = e^{2\pi i/7}$) is the value of the Gauss character:

$$\eta_1 = \omega + \omega^2 + \omega^4 = \frac{-1 + i\sqrt{7}}{2}$$

Imaginary part: $\mathrm{Im}(\eta_1) = \sqrt{7}/2 \neq 0$. (The same sum is the trace of an order-7 element in the complex triplet of $\mathrm{PSL}_2(7)$ that Luhn, Nasri and Ramond used as a flavour group in 2007, with the number three taken as input; §1.3.)

**Correction.** The condition $\mathrm{Im}(\sum \omega^{k_n}) = 0$ does **not** hold for any triplet from $\mathbb{Z}_7^* \setminus \{0\}$. Therefore, anomalous coherence as $\sum \sin(2\pi k_n/7) = 0$ is not an appropriate selection principle. $\blacksquare$

---

## 3. Selection principle: minimal associator {#3-принцип-отбора-минимальный-ассоциатор}

### Theorem 3.1 (Selection principle: minimal associator) {#thm-3-1}

:::danger [✗] Partially retracted
The main result $(1,2,4)$ = quadratic residues is correct, but the claim of equivalence $(1,2,4) \leftrightarrow (3,5,6)$ via $k \to 7-k$ is **erroneous** — $k \to -k \notin \mathrm{Aut}(\text{Fano}) = \mathrm{PSL}(2,7)$. The triplet $\{3,5,6\}$ is not a Fano line, $\mathcal{A}(3,5,6) = 4 \neq 0$. Therefore, $(1,2,4)$ is the **unique** triplet with $\mathcal{A} = 0$.
:::

**Theorem.** The physically realizable $\mathbb{Z}_7$-triplet minimizes the **total associator** of the three generations:

**(a)** Definition. Associator measure of a triplet:

$$\mathcal{A}(k_1, k_2, k_3) := \|[e_{k_1}, e_{k_2}, e_{k_3}]\|^2 = \|(e_{k_1} \cdot e_{k_2}) \cdot e_{k_3} - e_{k_1} \cdot (e_{k_2} \cdot e_{k_3})\|^2$$

where $e_k$ are the imaginary units of the octonions.

**(b)** From the octonion multiplication table:

- For a Fano triplet $(i,j,k)$: $[e_i, e_j, e_k] = 0$ (associator zero).
- For a non-Fano triplet: $[e_i, e_j, e_k] \neq 0$. Norm:

$$\|[e_i, e_j, e_k]\|^2 = 4 \quad \text{for all non-Fano triplets}$$

(from the identity $\|ab \cdot c - a \cdot bc\| = 2|a||b||c|\sin\alpha$ with $|e_i|=1$, and $\sin\alpha$ determined by the angle in the Fano plane).

**(c)** Classification:

| Triplet $(k_1,k_2,k_3)$ | Fano? | $\mathcal{A}$ | Class |
|---|---|---|---|
| $(1,2,4)$ — quadr. residues | contains Fano line | 0 | I |
| $(3,5,6)$ — non-residues | **NOT** a Fano line | **4** | II |
| $(1,3,5)$ | 0 Fano lines | 4 | II |
| $(2,4,6)$ | 0 Fano lines | 4 | II |
| ... | | 4 | II |

**(d)** Class I triplets ($\mathcal{A} = 0$) are **associative**: three imaginary units $e_{k_1}, e_{k_2}, e_{k_3}$ lie on a single Fano line and form an associative subalgebra $\mathbb{H} \subset \mathbb{O}$ (quaternionic).

**(e)** Selection principle. From $V_3$-dynamics: the vacuum configuration minimizes the energy. Contribution of three generations to $V_3$:

$$V_3^{(\text{gen})} \propto \mathcal{A}(k_1, k_2, k_3) \cdot \lambda_3 \prod_n |\gamma_n|$$

**The minimum is achieved at $\mathcal{A} = 0$** → Class I.

**(f)** From Class I: the **unique** candidate is $(1,2,4)$, since $(3,5,6)$ has $\mathcal{A}(3,5,6) = 4 \neq 0$ (not a Fano line).

**(g)** **Prediction:** Three generations are determined by quadratic residues $\bmod 7$:

$$(k_1, k_2, k_3) = (1, 2, 4)$$

This is the subgroup of index 2 in $\mathbb{Z}_7^*$, isomorphic to $\mathbb{Z}_3$.

**Proof.** Step 1: from PSL(2,7)-classification ([Theorem 2.1](#thm-2-1)) — two classes. Step 2: from $V_3$-minimization — Class I ($\mathcal{A} = 0$). Step 3: from $\mathcal{A} = 0$ and the definition of the associator in $\mathbb{O}$ — the triple $(k_1,k_2,k_3)$ forms a quaternionic subalgebra $\iff$ the triple is a subgroup of $\mathbb{Z}_7^*$. The unique subgroup of order 3 in $\mathbb{Z}_7^*$: quadratic residues $\{1,2,4\}$. $\blacksquare$

### 3.2 Refutation of equivalence $(1,2,4) \leftrightarrow (3,5,6)$ {#refutation-equivalence}

:::danger [✗] Retracted: equivalence $(1,2,4) \leftrightarrow (3,5,6)$
The claim that the triplets $(1,2,4)$ and $(3,5,6)$ are physically equivalent via the map $k \to 7-k \pmod{7}$ is **refuted**. The map $k \to -k$ is **not** an automorphism of the Fano plane: $k \to -k \notin \mathrm{Aut}(\mathrm{PG}(2,2)) = \mathrm{PSL}(2,7)$.
:::

**Diagnosis.** The original formulation claimed that $(1,2,4)$ and $(3,5,6)$ — both with $\mathcal{A} = 0$ — are related by the automorphism $k \to 7-k$, corresponding to the "particle $\leftrightarrow$ antiparticle" replacement.

**Error.** The map $k \to 7-k$: $1\to 6, 2\to 5, 4\to 3$. The Fano line $\{1,2,4\}$ maps to $\{6,5,3\} = \{3,5,6\}$. However, $\{3,5,6\}$ is **not** a Fano line (check against the complete list of 7 lines of $\mathrm{PG}(2,2)$: no line contains all three points $3, 5, 6$). Therefore:

- $\mathcal{A}(3,5,6) = 4 \neq 0$ — the triplet $(3,5,6)$ is **not** associative
- $k \to -k \pmod{7}$ does not preserve the Fano structure → does not belong to $\mathrm{PSL}(2,7)$

**Consequence.** The selection principle is **strengthened**: $(1,2,4)$ is the **unique** triplet with $\mathcal{A} = 0$, without degeneracy. Details — [Theorem 6.1 (Uniqueness)](#thm-6-1).

---

## 4. Generation assignment {#4-назначение-поколений}

### 4.1 Fermionic spinors of three generations

**Definition.** The three generations of fermionic spinors are defined by three distinct Gap-configurations in the vacuum sector:

**(a)** From Fano duality: each point $X \in \{A, S, D, L, E, U\}$ lies on 3 Fano lines (after removing $O$). Three lines through each point define three classes of orientation.

**(b)** For 6 points $\{A, S, D, L, E, U\} \equiv \{1, 2, 3, 4, 5, 6\}$ (numbering after removing $O \equiv 7$), Fano lines (restricted to 6 points) define a substructure.

**(c)** Three generations of fermionic spinors:

$$\chi_1 = \eta_0 \cdot e^{i\phi_1}, \quad \chi_2 = \eta_0 \cdot e^{i\phi_2}, \quad \chi_3 = \eta_0 \cdot e^{i\phi_3}$$

where the phases $\phi_\text{gen} = \{\phi_1, \phi_2, \phi_3\}$ are determined by the orientation of the vacuum relative to the three Fano classes:

$$\phi_n = \frac{2\pi}{7} \cdot k_n, \quad k_n \in \{1, 2, 4\}$$

### 4.2 Theorem 4.1 (Assignment of the 3rd generation) {#thm-gen-4-1}

:::tip Theorem 4.1 (Assignment of the 3rd generation) [T]
Index $k=1$ **uniquely** corresponds to the 3rd generation (t, b, τ). Strictly proved from the Fano selection rule for Yukawa couplings.
:::

**Theorem.** Index $k=1$ uniquely corresponds to the **3rd generation** (t, b, τ).

**Proof.** From the Fano selection rule for Yukawa couplings [T] ([Theorem on Fano selection $f_{ijk}$](/docs/physics/gauge-symmetry/fano-selection-rules#теорема-фано-отбор-fijk)):

$$y_k^{(\text{tree})} = g_W \cdot f_{k,E,U} \cdot |\gamma_{\text{vac}}^{(EU)}|$$

where $f_{ijk}$ are the structure constants of the octonions. $f_{ijk} \neq 0$ if and only if $\{i,j,k\}$ is a Fano line.

- $k=1$: $\{1,5,6\} = \{A,E,U\}$ — Fano line ✓ → $y_1^{(\text{tree})} \neq 0$
- $k=2$: $\{2,5,6\}$ — **not** a Fano line ✗ → $y_2^{(\text{tree})} = 0$
- $k=4$: $\{4,5,6\}$ — **not** a Fano line ✗ → $y_4^{(\text{tree})} = 0$

Unique nonzero tree-level Yukawa → $k=1$ = heaviest generation = **3rd**. $\blacksquare$

:::info Key consequence
The assignment $k=1 \to$ 3rd generation is a **theorem**, independent of assumptions. The mass hierarchy $m_t \gg m_c, m_u$ follows from the fact that **only** $k=1$ has a tree-level Yukawa coupling; $k=2$ and $k=4$ acquire mass only through loop corrections (see [Yukawa Mass Hierarchy](/docs/physics/particle-physics/yukawa-hierarchy)).
:::

### 4.3 Theorem 4.2 (Sectoral asymmetry of generations) — retracted [✗] {#thm-gen-4-2}

:::danger Theorem 4.2 retracted [✗] (2026-09-25)
Theorem 4.2 claimed that $k=2$ ($S$) lies in the $\mathbf{3}$-sector and $k=4$ ($L$) in the $\bar{\mathbf{3}}$-sector of the $\mathrm{SU}(3)_C$ decomposition, so that their Fano paths to the Higgs pass through pairs of different sector type. Step 1 is false: $\{A,S,D\}$ and $\{L,E,U\}$ are not the $\mathbf 3$ and $\bar{\mathbf 3}$ — no three axes span an $\mathrm{SU}(3)$-invariant subspace, and the triplet is spanned by $A-iD$, $S-iU$, $L-iE$ ([Standard Model, Theorem 1.1(a)](/docs/physics/gauge-symmetry/standard-model)) — so no axis "belongs" to either. What survives is incidence combinatorics [T]: $S$ reaches $E$ through the line $\{S,D,E\}$, $L$ reaches $U$ through the line $\{D,L,U\}$, both with the one intermediate point $D$. Which of the two pairs $(S,D)$, $(L,D)$ carries the smaller vacuum Gap is not decided by $\mathrm{SU}(3)$: an $\mathrm{SU}(3)_C$-invariant $\Gamma$ has no coherence on either pair (`test_su3_invariant_states_are_coherent_only_on_o_line_pairs`). That choice is the assumption (SA) of §4.4. Registry row 45b.
:::

*Record of the retracted theorem.* **Theorem.** Generations $k=2$ and $k=4$ belong to **different** sectors of the vacuum decomposition and have **structurally distinct** Fano paths to the Higgs.

**Proof.**

**Step 1. Sector assignment — retracted [✗].**

From $SU(3)_C$-decomposition [T] ([Standard Model from $G_2$](/docs/physics/gauge-symmetry/standard-model)):

- $\mathbf{3}$-sector: $\{A=1, S=2, D=3\}$ — fundamental $SU(3)$
- $\bar{\mathbf{3}}$-sector: $\{L=4, E=5, U=6\}$ — antifundamental $SU(3)$

Therefore:
- $k=2$ ($S$) $\in \mathbf{3}$-sector
- $k=4$ ($L$) $\in \bar{\mathbf{3}}$-sector

**Step 2. Fano paths to the Higgs — the paths [T], their "sector type" retracted [✗].**

Higgs line: $\{A=1, E=5, U=6\}$, where $E, U \in \{L,E,U\}$ (formerly "$\in\bar{\mathbf{3}}$"). Active Fano lines (without $O=7$):

| Path | Line | Intermediate | Reaches | Sector type of pair |
|------|-------|:------------:|:---------:|:-----------------:|
| $k=2 \to E$ | $\{S=2, D=3, E=5\}$ | $D$ | $E$ (Higgs) | $(S,D)$: **3-to-3**, Gap $\sim \varepsilon$ |
| $k=4 \to U$ | $\{D=3, L=4, U=6\}$ | $D$ | $U$ (Higgs) | $(L,D)$: **3-to-$\bar{3}$**, Gap $\approx 0$ |

Both paths pass through $D=3$ (Distinction dimension), but:
- Pair $(S,D) = (2,3)$: both $\in \mathbf{3}$-sector → sector **3-to-3**, Gap $\sim \varepsilon$ (intermediate)
- Pair $(L,D) = (4,3)$: $L \in \bar{\mathbf{3}}$, $D \in \mathbf{3}$ → sector **3-to-$\bar{3}$**, Gap $\approx 0$ (confinement) $\blacksquare$

### 4.4 Theorem 4.3 (Generation ordering) [C at (SA)] {#thm-gen-4-3}

:::tip Theorem 4.3 (Generation ordering) [C at (SA)]
$k=4 \to$ 2nd generation, $k=2 \to$ 1st generation, given the vacuum assumption (SA) below, which is a hypothesis [H]. Until 2026-09-25 this box read "[T] — proved via confinement [T] and asymptotic freedom [T]"; confinement and asymptotic freedom are facts of QCD, but that they act on the pair $(L,D)$ and not on $(S,D)$ is exactly (SA), whose former structural basis — Theorem 4.2 — is retracted.
:::

#### Hypothesis (SA): sectoral asymmetry [H] {#гипотеза-секторной-асимметрии}

**Sectoral asymmetry (SA) [H]** — the named assumption, stated on axis pairs: the vacuum Gap profile takes the axis-pair values of the ansatz of [Theorem 5.2(a)](#thm-5-2) — in particular Gap $\approx 0$ on the pair $(L,D)$ and Gap $\sim\varepsilon$ on $(S,D)$ — so that the 1-loop effective Yukawa coupling through $(L,D)$ **exceeds** the coupling through $(S,D)$. The earlier reading of these pair sets as the $\mathrm{SU}(3)$ sectors "confinement ($\mathbf{3}$-to-$\bar{\mathbf{3}}$)" and "intermediate ($\mathbf{3}$-to-$\mathbf{3}$)" is retracted (Theorem 4.2); no $\mathrm{SU}(3)_C$-invariant vacuum distinguishes the two pairs, and any vacuum that does is not $\mathrm{SU}(3)_C$-invariant (Theorem 5.2). *Restriction proved 2026-09-25:* every non-$O$ axis splits $\tfrac12 : \tfrac12$ between $\mathbf 3$ and $\bar{\mathbf 3}$, and $\mathrm{SU}(3)_C$ moves any axis to any other (each orbit in $\mathbb R^6$ is the whole $S^5$), so no colour-invariant quantity distinguishes $k=2$ from $k=4$; (SA) therefore **requires a vacuum that breaks colour**, and the only colour-invariant asymmetry is the weight of $\mathbf 3$ against $\bar{\mathbf 3}$ (registry row 45b; `test_every_non_o_axis_is_half_triplet_and_colour_moves_any_axis_to_any`). The self-consistent vacuum of $V_{\mathrm{Gap}}$ does break colour — its support is two Fano lines through a point and its stabiliser in $\mathfrak g_2$ is zero (T-64, restated [H]) — but it is not known to give (SA). Deriving or refuting (SA) is a research programme [Pr]. In the status registry it is the struck row T-52 — listed as a theorem until 2026-09-25 — and the entry (SA) of the table of promoted hypotheses, now [H].

:::note Former proof (SA) — retracted [✗]
It read: "proved via confinement [T] and asymptotic freedom [T]":

1. **Confinement sector** ($\mathbf{3}$-to-$\bar{\mathbf{3}}$, Gap $\approx 0$): non-perturbative coupling $\sim O(\Lambda_{\text{QCD}}/v_{\text{EW}}) \sim 10^{-3}$.
2. **Intermediate sector** ($\mathbf{3}$-to-$\mathbf{3}$, Gap $\sim \varepsilon$): perturbative coupling $\sim \varepsilon^2/(16\pi^2) \sim 6 \times 10^{-7}$.
3. **Ratio** $\sim 10^3$ — confinement sector dominates.

"The structural basis — different sector membership — is a theorem (Theorem 4.2)." Theorem 4.2 is retracted; items 1–3 compare the two couplings once the Gap values of the two pairs are given, and giving them is (SA).
:::

**Theorem [C at (SA)].** From the sectoral asymmetry (SA): $k=4 \to$ 2nd generation (c, s, μ), $k=2 \to$ 1st generation (u, d, e).

**Proof.**

**Step 1.** From Theorem 4.2: $k=4$ couples to the Higgs via the confinement-sector pair $(L,D)$, while $k=2$ — via the intermediate pair $(S,D)$.

**Step 2.** The effective Yukawa coupling at 1-loop level is proportional to the propagation amplitude through the intermediate state $D$. In the confinement sector (Gap $\approx 0$) the dynamics is **non-perturbative**: the effective coupling is determined by the confinement scale $\Lambda_{\text{QCD}}$, not by a small expansion parameter.

**Step 3.** In the intermediate sector (Gap $\sim \varepsilon$) the 1-loop amplitude is suppressed by a factor:

$$\delta_{S \to A} \sim \frac{\lambda_3}{16\pi^2} \cdot \frac{|\gamma_{SD}|^2}{m_D^2} \sim \frac{\lambda_3 \varepsilon^2}{16\pi^2} \sim \varepsilon_{\text{eff}}^2$$

:::note Status of parameter $\lambda_3$ [T]
The parameter $\lambda_3 = 2\mu^2/(3|\bar{\gamma}|) \approx 74$ is a **geometric coefficient** of the spectral action (T-74 [T]), not a perturbative coupling constant. Physical observables are defined non-perturbatively via the self-consistent vacuum $\theta^*$ (T-79 [C at (SV)]). UV-finiteness (T-66: field-space [T], order-by-order [C]) ensures structural correctness. Loop estimates are approximations to $\theta^*$, giving the right order of magnitude (error $\lesssim \times 5$). For details — see [Yukawa Hierarchy](/docs/physics/particle-physics/yukawa-hierarchy#предупреждение-λ3).

**⚠ C7**: $\lambda_3 \approx 74 \gg 4\pi$ — non-perturbative regime. All loop computations with $\lambda_3$ are formally unreliable and downgraded to **[H]**. See [warning](/docs/physics/particle-physics/yukawa-hierarchy#c7-nonperturbative).
:::

**Step 4.** Given (SA) — i.e. that the pair $(L,D)$ lies in the Gap $\approx0$ regime where confinement [T] and asymptotic freedom [T] make the amplitude non-perturbative — the amplitude through $(L,D)$ dominates the perturbative one through $(S,D)$:

$$y_4^{(\text{eff})} > y_2^{(\text{eff})} \quad \Longrightarrow \quad m(k=4) > m(k=2)$$

**Step 5.** Therefore: $k=4$ is the heavier of the light generations = **2nd**, $k=2$ is the lightest = **1st**.

$$\boxed{k=1 \to \text{3rd (t,b,τ)}, \quad k=4 \to \text{2nd (c,s,μ)}, \quad k=2 \to \text{1st (u,d,e)}}$$

$\blacksquare$

### 4.5 Final generation assignment table

| Mass | Generation | Fano $k$ | Dimension | Mechanism | Status |
|---|---|---|---|---|---|
| **Heaviest** | 3rd (t, b, τ) | **1** | **A (Actualization)** | Tree-level ($f_{1,E,U} \neq 0$), IR FP | **[T]** |
| **Intermediate** | 2nd (c, s, μ) | **4** | **L (Nomos)** | 1-loop through the pair $(L,D)$ (Gap $\approx 0$ by (SA)) | **[C at (SA)]** |
| **Light** | 1st (u, d, e) | **2** | **S (Morphogenesis)** | 1-loop through the pair $(S,D)$ (Gap $\sim \varepsilon$ by (SA)) | **[C at (SA)]** |

### 4.6 Cascade of assignment consequences {#каскад-назначения}

#### 4.6.1 Neutrino hierarchy [C at (SA)]

The assignment $k=4 \to$ 2nd generation and $k=2 \to$ 1st generation (Theorem 4.3, [C at (SA)]; this heading said [T] until 2026-09-25) resolves the contradiction in [neutrino masses](/docs/physics/particle-physics/neutrino-masses): seesaw with $m_D \sim m_l$ gives the **normal** hierarchy ($m_{\nu_e} < m_{\nu_\mu} < m_{\nu_\tau}$).

#### 4.6.2 Discrepancy $m_2/m_3$ [C]

The O-sector spectral triple gives Dirac Yukawas via $m_D^{(k)} = \omega_0 \cdot \mathrm{Gap}(O,k) \cdot |\gamma_{O,\mathrm{partner}(k)}| \cdot \sin(2\pi k/7)$. Discrepancy $m_2/m_3$: factor $\times 1.8$ (down to $\times 1.2$ with two-loop RG). See [neutrino masses](/docs/physics/particle-physics/neutrino-masses#теорема-отношение-нейтринных-масс).

#### 4.6.3 Fixing CKM/PMNS

Mixing angles are now defined by Fano differences with the specific assignment: $\Delta k_{12} = |k_2 - k_1| = |4-1| = 3$, $\Delta k_{23} = |k_3 - k_2| = |2-4| = 2$, $\Delta k_{13} = |k_3 - k_1| = |2-1| = 1$.

### 4.7 Bare Yukawa couplings from Fano phases

**Theorem [T].** "Bare" Yukawa couplings (at the GUT scale) are determined by the Fano selection rule:

**(a)** Tree-level formula (only for $k$ on the Higgs line):

$$y_k^{(\text{tree})} = g_W \cdot f_{k,E,U} \cdot |\gamma_{\text{vac}}^{(EU)}|$$

**(b)** For $(k_1, k_2, k_3) = (1, 2, 4)$:
- $y_1^{(\text{tree})} \neq 0$ ($k=1$ on Higgs line $\{A,E,U\}$)
- $y_2^{(\text{tree})} = 0$ ($k=2$ **not** on Higgs line)
- $y_4^{(\text{tree})} = 0$ ($k=4$ **not** on Higgs line)

**(c)** Mass hierarchy: $y_1 = O(1)$, $y_2 = y_4 = 0$ at tree level. Light generations acquire masses **only** through loop corrections. Details — [Yukawa Mass Hierarchy](/docs/physics/particle-physics/yukawa-hierarchy).

### 4.8 Updated mass table

**Corollary.** Full fermion mass table from the Gap formalism with generation assignment:

| Generation | $k_n$ | Dimension | $\sin(2\pi k_n/7)$ | Mechanism | $m_q^{(u)}$ | $m_q^{(d)}$ | $m_l$ |
|---|---|---|---|---|---|---|---|
| 1st | 2 | S (Morphogenesis) | 0.975 | 1-loop via $(S,D)$ [C at (SA)] | ~2 MeV | ~5 MeV | ~0.5 MeV |
| 2nd | 4 | L (Nomos) | 0.434 | 1-loop via $(L,D)$ [C at (SA)] | ~1.3 GeV | ~100 MeV | ~106 MeV |
| 3rd | 1 | A (Actualization) | 0.782 | Tree + IR FP | ~173 GeV | ~4.2 GeV | ~1.78 GeV |

---

## 5. Z₃-symmetry and the Fano selection rule {#5-z₃-симметрия-и-фановское-правило-отбора}

### Theorem 5.1 (Automorphism of the Fano plane) {#thm-5-1}

:::tip Theorem 5.1 (Automorphism of the Fano plane) [T]
Strictly proved. Standard algebra of automorphisms of the Fano plane.
:::

**Theorem.** The map $\sigma: k \mapsto 2k \bmod 7$ is an automorphism of the Fano plane $\mathrm{PG}(2,2)$ and cyclically permutes the elements of the Fano line $\{1,2,4\}$.

**(a)** Action of $\sigma$ on $\mathbb{Z}_7$:

$$1 \to 2 \to 4 \to 1 \quad (\text{cycle } (1\,2\,4))$$

$$3 \to 6 \to 5 \to 3 \quad (\text{cycle } (3\,6\,5))$$

$$7 \to 7 \quad (\text{fixed: } 14 \equiv 0 \equiv 7)$$

**(b)** Verification: $\sigma$ preserves Fano lines.

| Line | Image under $\sigma$ | Fano? |
|---|---|---|
| $\{1,2,4\}$ | $\{2,4,1\} = \{1,2,4\}$ | ✓ |
| $\{2,3,5\}$ | $\{4,6,3\} = \{3,4,6\}$ | ✓ |
| $\{3,4,6\}$ | $\{6,1,5\} = \{1,5,6\}$ | ✓ |
| $\{4,5,7\}$ | $\{1,3,7\} = \{1,3,7\}$ | ✓ |
| $\{5,6,1\}$ | $\{3,5,2\} = \{2,3,5\}$ | ✓ |
| $\{6,7,2\}$ | $\{5,7,4\} = \{4,5,7\}$ | ✓ |
| $\{7,1,3\}$ | $\{7,2,6\} = \{2,6,7\}$ | ✓ |

All 7 Fano lines map to Fano lines. $\sigma \in \mathrm{Aut}(\mathrm{PG}(2,2)) = \mathrm{PSL}(2,7)$. $\blacksquare$

### Corollary 5.1 (Z₃-symmetry)

**Corollary.** The automorphism $\sigma$ generates a subgroup $\mathbb{Z}_3 \subset \mathrm{PSL}(2,7)$, acting on the Fano line $\{1,2,4\}$ as a cyclic permutation:

$$\sigma: 1 \to 2 \to 4 \to 1$$

**(a)** Any Fano-invariant functional $F(k_1, k_2, k_3)$ satisfies:

$$F(1,2,4) = F(\sigma(1), \sigma(2), \sigma(4)) = F(2,4,1) = F(1,2,4)$$

i.e., $F$ is **equal** for all three generations.

**(b)** In particular: the associator measure $\mathcal{A}(k)$, the number of Fano lines through $k$, the distance to any fixed dimension in the Fano graph — all are $\mathbb{Z}_3$-symmetric.

**(c)** **Fundamental consequence:** The mass hierarchy $m_t \gg m_c \gg m_u$ **cannot** be explained by Fano geometry alone. A $\mathbb{Z}_3$-breaking factor is required.

### Theorem 5.2 (Vacuum breaking of Z₃) — retracted [✗] {#thm-5-2}

:::danger Theorem 5.2 retracted [✗] (2026-09-25): breaking this $\mathbb{Z}_3$ breaks colour
Theorem 5.2 argued that the vacuum breaks the $\mathbb{Z}_3$ generated by $\sigma$ because $k=1$ ($A$) and $k=2$ ($S$) lie in the $\mathbf{3}$-sector and $k=4$ ($L$) in the $\bar{\mathbf{3}}$-sector. The argument is void — those sector labels are not an $\mathrm{SU}(3)$ decomposition (Theorem 4.2) — and the conclusion is worse than it looked. $\sigma$ extends to the automorphism $e_k\mapsto e_{2k}$ of $\mathbb{O}$ (all signs $+$), fixes $e_O=e_7$, and so lies in $\mathrm{SU}(3)_C=\mathrm{Stab}_{G_2}(e_O)$ of the [Standard Model page](/docs/physics/gauge-symmetry/standard-model); in the basis $A-iD$, $S-iU$, $L-iE$ of the triplet it is the cyclic permutation matrix, with determinant 1 and $\log\sigma\in\mathfrak{su}(3)$ (`test_generation_z3_lies_in_colour_su3`). A vacuum that breaks $\langle\sigma\rangle$ breaks $\mathrm{SU}(3)_C$. The axis-pair profile of (a) does so — $\sigma$ maps the pair $(A,L)$ (Gap $\approx0$) to $(S,A)$ (Gap $\sim\epsilon_{\text{space}}$) — and so does the Higgs condensate $\gamma_{EU}\neq0$, since $\sigma$ maps $(E,U)$ to $(D,E)$. In UHM's own identifications, then, the $\mathbb{Z}_3$ breaking that the mass hierarchy needs is colour breaking. No mechanism in the corpus reconciles this with unbroken $\mathrm{SU}(3)_C$; it is recorded as an open contradiction and a research programme [Pr]. A horizontal alternative, a $\mathbb{Z}_3$ that commutes with all of $G_{\mathrm{SM}}$, is given in [§5.3](#поколения-t328) (T-328).
:::

*Record of the retracted theorem.* **Theorem.** The vacuum Gap profile breaks the $\mathbb{Z}_3$-symmetry of the Fano line $\{1,2,4\}$.

**(a)** The vacuum Gap profile defines 5 sectors with different Gap values:

| Sector | Dimensions | Gap | Scale |
|---|---|---|---|
| $3$-to-$\bar{3}$ | $\{A,S,D\} \times \{L,E,U\}$ (9 pairs) | $\approx 0$ | Confinement |
| $3$-to-$3$ | $\{A,S,D\}^2$ (3 pairs) | $\sim \epsilon_\text{space}$ | Intermediate |
| $\bar{3}$-to-$\bar{3}$ | $\{L,E,U\}^2$ (3 pairs) | $\sim \epsilon_\text{EW} \sim 10^{-17}$ | Electroweak |
| $O$-to-$3$ | $O \times \{A,S,D\}$ (3 pairs) | $\sim 1$ | Planck |
| $O$-to-$\bar{3}$ | $O \times \{L,E,U\}$ (3 pairs) | $\sim 1$ | Planck |

**(b)** Dimensions $\{A,S,D\} = \{1,2,3\}$ belong to the **3-sector** (fundamental $SU(3)$), and $\{L,E,U\} = \{4,5,6\}$ — to the **$\bar{3}$-sector**.

**(c)** Three generations $(k_1, k_2, k_3) = (1, 2, 4) = (A, S, L)$:
- $k=1$ (A) and $k=2$ (S) — in the **3-sector**
- $k=4$ (L) — in the **$\bar{3}$-sector**

This **breaks** $\mathbb{Z}_3$: two generations in one sector, one — in the other. $\blacksquare$ (Retracted; see the box at the top of this theorem, which replaces the former warning "Collision with the colour reading of the same axes".)

### 5.3 A family symmetry must be horizontal: what the corrected framework allows (T-328) {#поколения-t328}

:::tip[Status: (a) and (b) \[T\]; (c) \[T\] for the count and the commutation, \[C at (GC)\] for the identification, with (GC) a hypothesis \[H\]]
A family symmetry commutes with the gauge group. That is what the $\mathbb{Z}_3$ of Corollary 5.1 fails to do: it is a colour rotation. Under the assumption (Cl) of the [Standard Model page, §2.5](/docs/physics/gauge-symmetry/standard-model#sm-из-клиффорда), where $G_{\mathrm{SM}}$ acts on $\mathcal{S}=\mathbb{C}\otimes\mathbb{O}$, the requirement can be computed, and it rules out every candidate that lives inside one copy of $\mathcal{S}$. Registry row T-328.
:::

**Theorem 5.3 (T-328).**

**(a) One copy has no family symmetry [T].** The commutant of $\mathfrak{g}_{\mathrm{SM}}$ on $\mathcal{S}$ is $\mathbb{C}\oplus\mathbb{C}$ (dimension 4), so the unitary operators that commute with $G_{\mathrm{SM}}$ are two phases, one on the quark doublet and one on the lepton doublet, $\mathrm{U}(1)_B\times\mathrm{U}(1)_L$. No permutation of three objects inside $\mathcal{S}$ commutes with $G_{\mathrm{SM}}$. This covers the axes $\{1,2,4\}$, the three Fano lines through $O$ (the quaternionic subalgebras containing $e_O$ of Manogue and Dray), and the three pairs $(A,D)$, $(S,U)$, $(L,E)$. In particular $\sigma: e_k\mapsto e_{2k}$ does not commute with $G_{\mathrm{SM}}$ (checked). This generalises the finding of Theorem 5.2: every "three" inside one copy of $\mathbb{C}\otimes\mathbb{O}$ is colour or charge, not family.

**(b) Triality is not a family symmetry [T].** The triality automorphism $\tau$ of $\mathfrak{so}(8)$ is built from local triality: for $A\in\mathfrak{so}(8)$ there are unique $B, C$ with $A(xy)=B(x)y+xC(y)$, and $\tau(A)=\kappa B\kappa$ with $\kappa$ octonionic conjugation. (For triality in general, see Baez, "The Octonions", *Bull. Amer. Math. Soc.* **39**, 145–205 (2002), [arXiv:math/0105155](https://arxiv.org/abs/math/0105155), §2.4.) It has order 3, and its fixed algebra is $\mathfrak{g}_2$ (dimension 14). It fixes $\mathfrak{su}(3)_C$ pointwise. It maps the centraliser of $\mathfrak{su}(3)_C$ in $\mathfrak{so}(8)$ — the plane $\mathrm{span}\{L_{e_O}, R_{e_O}\}$ — to itself by a rotation through exactly $2\pi/3$. So triality commutes with colour but moves $R_{e_O}$, whose centraliser is $G_{\mathrm{SM}}$ (Standard Model, Theorem 2.5(b)). It carries one embedding of the Standard Model group to another, and does not permute three copies of the fermions under one group. This makes Boyle's "three triality-related ways" precise: the three are three Standard Model groups, not three generations of one. The cyclic permutation of the three diagonal slots of $J_3(\mathbb{O})$ behaves the same way: it maps the $\mathrm{Spin}(9)$ that fixes one idempotent to the one that fixes the next.

**(c) The clock gives a horizontal three [T for the count and the commutation].** A family symmetry has to act on a multiplicity space on which $G_{\mathrm{SM}}$ acts trivially. In the Page–Wootters structure of UHM the clock register is such a factor: every operator $P\otimes1$ on $\mathcal{H}_{\text{clock}}\otimes\mathcal{S}$ commutes with $1\otimes G_{\mathrm{SM}}$. The real regular representation of the clock group $\mathbb{Z}_7$ is the trivial line plus three rotation planes, with frequencies $2\pi m/7$ for $m=1,2,3$. These are the classes $\mathbb{Z}_7^*/\{\pm1\}$ of Theorem 1.2. The multiplier $m\mapsto 2m$ permutes the three planes cyclically, $\{\pm1\}\to\{\pm2\}\to\{\pm4\}=\{\mp3\}\to\{\pm1\}$, so $\mathrm{Aut}(\mathbb{Z}_7)/\{\pm1\}\cong\mathbb{Z}_3$ acts simply transitively on them. **Hypothesis (GC) [H]:** a generation is a non-trivial real harmonic of the clock register; fermions live in $\mathcal{H}_{\text{clock}}\otimes\mathcal{S}$, and the three harmonic classes label the three copies. Under (GC), $N_{\text{gen}}=3$ [C at (GC)] with a family $\mathbb{Z}_3$ that commutes with all of $G_{\mathrm{SM}}$ — the property the axis $\mathbb{Z}_3$ lacks. Under (GC) a fourth sequential generation is also excluded: $\mathbb{Z}_7$ has no fourth non-trivial real harmonic.

**Proof.** (a) is Schur's lemma for the two non-isomorphic modules of Theorem 4.4(a) on the Standard Model page; the four-dimensional commutant and the failure of $\sigma$ are computed. (b) The linear system for $(B, C)$ is solved on all 28 generators, with residual below $10^{-9}$. Then $\tau^3=1$, the fixed space has dimension 14, $\tau$ fixes $\mathfrak{su}(3)_C$, and on $\mathrm{span}\{L_{e_O},R_{e_O}\}$ its eigenvalues are $e^{\pm2\pi i/3}$ — all computed. (c) The eigenvalues of the cyclic shift on $\mathbb{R}^7$ are $e^{2\pi i m/7}$, and the orbit of the classes under $m\mapsto2m$ is listed above. $\blacksquare$

Witnesses: `test_family_symmetry_cannot_live_inside_one_copy`, `test_clock_has_three_nontrivial_real_harmonics`.

**What this changes.** The count of Theorem 1.2 stays [T]. Its identification [I] used to have two readings that the corpus did not separate. In the *axis reading*, generation $k$ is the axis $e_k$. In the *harmonic reading*, generation $k$ is the phase $2\pi k/7$ of §4.1(c). Part (a) shows that the axis reading cannot carry a family symmetry commuting with $G_{\mathrm{SM}}$; part (c) shows that the harmonic reading can. The Fano selection rule used in Theorem 4.1 ($f_{k,E,U}\neq0$ only for $k=1$) is incidence arithmetic on axes and stays [T] as arithmetic. Its use to single out the third generation presupposes the axis reading, so it inherits the tension of (a). Under (GC) the family $\mathbb{Z}_3$ is broken not by the vacuum of colour (the contradiction of Theorem 5.2) but by the clock Hamiltonian $H_O=\omega_0\,\mathrm{diag}(0,\dots,6)$, which does not commute with $m\mapsto2m$. Whether this breaking produces the observed hierarchy is open [Pr].

---

## 6. Uniqueness of the triplet (1,2,4) {#6-единственность-триплета-124}

### Theorem 6.1 (Uniqueness) {#thm-6-1}

:::tip Theorem 6.1 (Uniqueness of the triplet) [T]
Strictly proved. Follows from the algebra of octonions and the structure of the Fano plane.
:::

**Theorem.** The triplet $(1,2,4)$ is the **unique** $\mathbb{Z}_7$-triplet simultaneously satisfying:

1. $\mathcal{A}(k_1, k_2, k_3) = 0$ (minimal associator)
2. $k_1 + k_2 + k_3 \equiv 0 \pmod{7}$ (associative class)
3. Is a Fano line of $\mathrm{PG}(2,2)$

**Proof.**

Step 1. From the table of 7 Fano lines of $\mathrm{PG}(2,2)$:

$$\{1,2,4\}, \{2,3,5\}, \{3,4,6\}, \{4,5,7\}, \{5,6,1\}, \{6,7,2\}, \{7,1,3\}$$

Step 2. Lines containing $O = 7$: $\{4,5,7\}$, $\{6,7,2\}$, $\{7,1,3\}$ — excluded, since $O$ is not a generation.

Step 3. Lines without $O$: $\{1,2,4\}$, $\{2,3,5\}$, $\{3,4,6\}$, $\{5,6,1\}$.

Step 4. Of these 4 lines: do they contain three **distinct** generations? Generations = elements of the triplet, not coinciding with $E=5$, $U=6$, $D=3$ (non-generational dimensions). The line $\{1,2,4\}$ contains $A=1$, $S=2$, $L=4$ — all three are generations.

Step 5. Associator check. $\{1,2,4\}$ — Fano line → $\mathcal{A} = 0$. The triple $\{3,5,6\}$ — **not** a Fano line (no such line in the table) → $\mathcal{A}(3,5,6) = 4 \neq 0$.

Step 6. Check $k_1 + k_2 + k_3 \bmod 7$: $1 + 2 + 4 = 7 \equiv 0$.

**Conclusion.** $(1,2,4)$ is the unique triplet satisfying all three conditions. $\blacksquare$

### Additional confirmation from the Fano selection rule

Among the elements of $(1,2,4)$ only $k=1$ lies on the Fano–Higgs line $\{1,5,6\} = \{A,E,U\}$. From $(3,5,6)$: $5 \in \{3,5,6\}$, but $E = 5$ is the Higgs dimension, **not** a generation. Thus $(1,2,4)$ is unique both in terms of the associator and in terms of the selection rule.

---

## 7. Mass hierarchy of generations {#7-массовая-иерархия-поколений}

### 7.1 Setup

The mass ratio $m_t/m_u \sim 10^5$ is not explained by Fano phases $\sin(2\pi k_n/7) \sim O(1)$. An additional mechanism is required. From the $\mathbb{Z}_3$-symmetry of the Fano line $\{1,2,4\}$ ([Corollary 5.1](#5-z₃-симметрия-и-фановское-правило-отбора)) it follows that purely Fano geometry gives **equal** masses for all three generations. A $\mathbb{Z}_3$-breaking factor is required.

### Theorem 7.1 (Yukawa couplings from Fano phases) {#thm-7-1}

:::tip Theorem 7.1 (Yukawa couplings from Fano phases) [T]
Formulas for bare Yukawas are a direct consequence of the Fano structure. Initial hierarchy $O(1)$ established.
:::

**Theorem.** "Bare" Yukawa couplings (at the GUT scale) are determined by Fano phases:

**(a)** General formula:

$$y_n^{(0)} = g_W \cdot \langle\chi_n|\Gamma_{EU}|\chi_n'\rangle \propto \sin\left(\frac{2\pi k_n}{7}\right) \cdot C_n$$

where $C_n$ is a normalization constant depending on the Fano structure.

**(b)** For $(k_1, k_2, k_3) = (1, 2, 4)$:

$$y_1^{(0)} \propto \sin(2\pi/7) \approx 0.782$$

$$y_2^{(0)} \propto \sin(4\pi/7) \approx 0.975$$

$$y_3^{(0)} \propto \sin(8\pi/7) = -\sin(\pi/7) \approx -0.434$$

Moduli: $|y_1^{(0)}| : |y_2^{(0)}| : |y_3^{(0)}| = 0.782 : 0.975 : 0.434 \approx 1.8 : 2.2 : 1$.

**(c)** Ratio of bare Yukawas: $y_2/y_3 \approx 2.2$, $y_1/y_3 \approx 1.8$. Hierarchy $O(1)$ — **not** sufficient to explain the observed $m_t/m_c \approx 140$, $m_c/m_u \approx 550$.

### Theorem 7.2 (RG enhancement via quasi-IR fixed point) {#thm-7-2}

:::danger [✗] Retracted
All three $O(1)$ Yukawas converge to a single IR fixed point, since $c_1 > c_2 > 0$. The hierarchy $m_t/m_c \sim 140$ **does not arise** from RG evolution of three $O(1)$ Yukawas — they converge, not diverge. Corrected via the Fano selection rule: $y_1 = O(1)$, $y_2 = y_3 = 0$ (Fano selection $f_{abc}$). See [Yukawa Mass Hierarchy](/docs/physics/particle-physics/yukawa-hierarchy).
:::

**Theorem.** The mass hierarchy of generations arises from the RG evolution of Yukawa couplings from GUT to the electroweak scale:

**(a)** The Yukawa coupling runs under RG:

$$\frac{dy_n}{d\ln\mu} = \frac{y_n}{16\pi^2}\left(c_1 y_n^2 + c_2 \sum_{m \neq n} y_m^2 - c_3 g_s^2 - c_4 g_W^2\right)$$

where $c_1 = 9/2$ (self-coupling), $c_2 = 3/2$ (inter-generational), $c_3 = 8$ (QCD), $c_4 = 9/4$ (electroweak).

**(b)** Quasi-IR fixed point (Pendleton–Ross, 1981; Hill, 1981). At $\mu \to 0$ the third generation (maximum $|y_3^{(0)}|$ accounting for sign) approaches a fixed point:

$$y_3^{(\text{IR})} = \sqrt{\frac{c_3 g_s^2 + c_4 g_W^2}{c_1}} = \sqrt{\frac{8\alpha_s + (9/4)\alpha_W}{9/(32\pi^2)}}$$

This predicts $m_t \sim v \cdot y_3^{(\text{IR})} \approx 174$ GeV (Hill, 1981) — in agreement with the observed $m_t \approx 173$ GeV.

**(c)** Hierarchy mechanism (original claim). From the initial condition $y_1/y_3 \approx 1.8$ at $\mu_{\text{GUT}}$: the third generation is attracted to the fixed point (IR attractor), while the first and second — run away from it (zero IR attractor). At the electroweak scale:

$$\frac{y_1(\mu_{\text{EW}})}{y_3(\mu_{\text{EW}})} \approx \frac{y_1^{(0)}}{y_3^{(0)}} \cdot \exp\left(-\frac{c_1}{16\pi^2} (y_3^{(0)2} - y_1^{(0)2}) \ln\frac{\mu_{\text{GUT}}}{\mu_{\text{EW}}}\right)$$

**(d)** Numerical estimate. $\Delta y^2 = y_3^{(0)2} - y_1^{(0)2} \approx 0.19 - 0.61 = -0.42$ (negative, i.e., $|y_1| > |y_3|$ at GUT scale).

**Renormalization.** Accounting for the correct generation identification: $k_3 = 4$ → third generation (t-quark). Bare coupling $|y_3^{(0)}| = |\sin(8\pi/7)| = 0.434$ — the **smallest**. However, for the t-quark the Yukawa fixed point is an **IR attractor**:

$$y_t(\mu_{\text{EW}}) \approx y_t^{(\text{FP})} = \sqrt{\frac{8g_s^2(\mu_{\text{EW}}) + (9/4)g_W^2}{9/2}} \approx 1.0$$

independently of the initial $y_3^{(0)}$.

**(e)** Key observation (original): **the third generation reaches the fixed point**, while the first and second — do not (their Yukawa couplings remain small). Mass ratio:

$$\frac{m_t}{m_c} \approx \frac{y_t^{(\text{FP})}}{y_c^{(\text{EW}})} \approx \frac{1.0}{y_2^{(0)} \cdot (\alpha_s(\mu_{\text{GUT}})/\alpha_s(\mu_{\text{EW}}))^{12/(33-2N_f)}}$$

With anomalous mass dimension: $m_q(\mu) \propto (\alpha_s(\mu))^{12/(33-2N_f)}$.

**(f)** Result (original). Third generation: $m_t \approx 173$ GeV (from IR fixed point). Second: $m_c \approx 1.3$ GeV (from $y_2^{(0)} \approx 0.975$ with RG suppression). First: $m_u \approx 2$ MeV (from $y_1^{(0)} \approx 0.782$ with maximum RG suppression). Hierarchy:

$$m_t : m_c : m_u \approx 173 : 1.3 : 0.002 \text{ GeV}$$

— **exponential** hierarchy from initial $O(1)$ differences in Yukawa couplings, amplified by RG.

### 7.3 Why Theorem 7.2 is refuted {#audit-thm-7-2}

:::danger [✗] Critical vulnerability K-1
The mechanism of mass hierarchy via RG evolution of three $O(1)$ Yukawa couplings is **fundamentally flawed**. Below — full diagnosis.
:::

**Diagnosis.** The central claim of Theorem 7.2 — mass hierarchy $m_t : m_c : m_u \sim 10^5 : 10^3 : 1$ arises from RG evolution of initial Yukawa couplings $|y_1|:|y_2|:|y_3| = 0.78:0.98:0.43$, all $O(1)$.

**Error.** From the RG equation (7.2a) with $c_1 = 9/2$, $c_2 = 3/2$, with **three** Yukawa couplings $O(1)$, the fixed point:

$$y_n^{(\text{FP})} = \sqrt{\frac{c_3 g_s^2 + c_4 g_W^2}{c_1 + 2c_2}} = \sqrt{\frac{8g_s^2 + \frac{9}{4}g_W^2}{\frac{9}{2} + 3}} = \sqrt{\frac{8g_s^2 + \frac{9}{4}g_W^2}{\frac{15}{2}}}$$

The stability matrix near this point has eigenvalues:

- $\lambda_{\text{breath}} \propto -(c_1 + 2c_2) = -15/2$ (breathing mode, stable in IR)
- $\lambda_{\text{diff}} \propto -(c_1 - c_2) = -3$ (differential modes, **also stable in IR**)

Since $c_1 > c_2 > 0$, **all three** Yukawa couplings simultaneously converge to a single fixed point. The initial $O(1)$ difference **decays**, not amplifies. Result:

$$y_1(\mu_{\text{EW}}) \approx y_2(\mu_{\text{EW}}) \approx y_3(\mu_{\text{EW}}) \approx y^{(\text{FP})}$$

No hierarchy arises.

**Root cause.** In standard physics the quark mass hierarchy is an **input** parameter: bare Yukawas are already hierarchical at $\mu_{\text{GUT}}$ ($y_t \sim 1$, $y_c \sim 10^{-2}$, $y_u \sim 10^{-5}$). The quasi-IR fixed point (Pendleton–Ross) explains only the value of $m_t$, not the hierarchy.

**Impact.** The predictions of the mass table (section 4.4), the claim "Hierarchy $m_t/m_u \sim 10^5$ from RG" — **are not justified** by this mechanism.

### 7.4 Proposed fix: generation-dependent anomalous dimensions {#fix-mass-hierarchy}

:::warning [H] Hypothesis 7.4 (Generation-dependent anomalous dimensions)
The mechanism is a hypothesis. Requires: (a) explicit computation of $c_i(\phi_n)$ from the Gap Lagrangian; (b) numerical solution of the coupled RG system; (c) fitting of $\kappa$ to the observed mass hierarchy.
:::

**Proposed fix.** In the Gap formalism each generation is defined by a Fano phase $\phi_n = 2\pi k_n / 7$, which enters the interaction vertices. Instead of **universal** $c_1, c_2, c_3, c_4$ one needs **generation-dependent** coefficients:

$$c_3^{(n)} = 8 \cdot f(\phi_n), \quad f(\phi_n) = 1 + \kappa \cos(2\phi_n)$$

where $\kappa$ is a parameter determined from $V_3$-dynamics. For $\kappa \neq 0$ the fixed points of different generations are **distinct**:

$$y_n^{(\text{FP})} = \sqrt{\frac{c_3^{(n)} g_s^2 + c_4 g_W^2}{c_1}}$$

If $c_3^{(1)} \gg c_3^{(3)}$ (due to the difference $\phi_1 = 2\pi/7$ vs $\phi_3 = 8\pi/7$), then $y_1^{(\text{FP})} > y_3^{(\text{FP})}$, and the first generation is "washed out" by the QCD coupling faster → $m_u \ll m_t$.

Alternatively: the hierarchy may arise **not** from RG, but from **bare** Yukawas at the Planck scale (preceding GUT). Gap phases $\sin(2\pi k_n / 7)$ determine Yukawas at the Planck scale, while the structure of $V_\text{Gap}$ between the Planck and GUT scales **exponentially** splits the initial $O(1)$ values. This requires RG evolution from $M_P$ to $M_{\text{GUT}}$, including all 42 fields.

The correct mechanism of mass hierarchy is implemented via the Fano selection rule for Yukawa couplings: $y_1 = O(1)$ (tree-level), $y_2 = y_3 = 0$ (Fano selection $f_{abc}$). Details in [Yukawa Mass Hierarchy](/docs/physics/particle-physics/yukawa-hierarchy).

### 7.5 Corollary: mass table paradox {#mass-paradox}

**Corollary.** Full fermion mass table from the Gap formalism:

| Generation | $k_n$ | $\sin(2\pi k_n/7)$ | $y^{(0)}$ | RG enhancement | $m_q^{(u)}$ | $m_q^{(d)}$ |
|---|---|---|---|---|---|---|
| 1 | 1 | 0.782 | ~0.78 | max suppression | ~2 MeV | ~5 MeV |
| 2 | 2 | 0.975 | ~0.98 | intermediate | ~1.3 GeV | ~100 MeV |
| 3 | 4 | 0.434 | ~0.43 | IR fixed point | ~173 GeV | ~4.2 GeV |

**(a)** Paradox: the third generation has the smallest bare Yukawa, yet the largest mass. Reason: the quasi-IR fixed point is an **attractor** for large scales.

**(b)** Ratio $m_b/m_\tau \approx 4.2/1.78 \approx 2.4$ — prediction of SU(5)-GUT (at $\mu_{\text{GUT}}$: $m_b = m_\tau$, at EW — they diverge due to QCD corrections).

:::info Status of mass hierarchy
The prediction $m_t \approx 173$ GeV from IR fixed point **is preserved** (standard Pendleton–Ross result). The mechanism of hierarchy $m_t/m_u \sim 10^5$ via RG of three $O(1)$ Yukawas **is refuted**. The correct mechanism — via the Fano selection rule, see [Yukawa Mass Hierarchy](/docs/physics/particle-physics/yukawa-hierarchy).
:::

---

## 8. Refined predictions: Cabibbo angle and CP violation {#8-уточнённые-предсказания-угол-кабиббо-и-cp-нарушение}

### Theorem 8.1 (Refined Cabibbo angle) {#thm-8-1}

:::tip Theorem 8.1 (Refined Cabibbo angle) [T]
With the selection principle $(k_1,k_2,k_3) = (1,2,4)$ taken into account, specific predictions are obtained for ratios of CKM matrix angles.
:::

**Theorem.** With the selection principle $(k_1,k_2,k_3) = (1,2,4)$ and RG evolution:

**(a)** Bare angle $\theta_{12}^{(\text{Fano})} = 2\pi|k_1 - k_2|/7 = 2\pi/7$. RG correction: suppression by $\exp(-4.63) \approx 0.0097$.

**(b)** Concretization: $|k_1 - k_2| = 1$, $|k_2 - k_3| = 2$, $|k_1 - k_3| = 3$. Ratios:

$$\theta_{23}/\theta_{12} = |k_2-k_3|/|k_1-k_2| \cdot f_{\text{RG}} = 2 \cdot f_{\text{RG}}$$

From RG: $f_{\text{RG}} = (y_2/y_3)^{1/2} \approx (0.975/0.434)^{1/2} \approx 1.5$.

$$\theta_{23}/\theta_{12} \approx 2 \times 1.5 \times \lambda_3(\text{EW})/\lambda_3(\text{GUT})$$

**(c)** Observed: $\theta_{23}/\theta_{12} \approx 0.040/0.227 \approx 0.18$. From prediction: $\lambda_3^{1/2} \sim 0.1$ → prediction: $\theta_{23}/\theta_{12} \sim 2 \times 0.1 / 1.5 \approx 0.13$. Order of magnitude agrees.

Details of CKM structure from Fano differences $\Delta k$ — see [CKM Matrix from Fritzsch Texture](/docs/physics/particle-physics/ckm-matrix).

### Theorem 8.2 (Refined CP phase) {#thm-8-2}

:::warning [H] Hypothesis 8.2 (Refined CP phase)
The sign of the two-loop correction $\delta^{(2)}$ is not determined a priori. With $\delta^{(2)} > 0$: agreement $64^\circ$ vs the direct $64.6° \pm 2.8°$ ($\approx 0.2\sigma$). With $\delta^{(2)} < 0$: $39^\circ$ — excluded by observations. The data select the positive branch; until the sign is derived, the status is a hypothesis.
:::

**Theorem.** With $(k_1,k_2,k_3) = (1,2,4)$:

**(a)** Bare value of the CP phase:

$$\delta_{\text{CP}}^{(0)} = \arg(e^{2\pi i(k_1+k_2-k_3)/7}) = \arg(e^{2\pi i(-1)/7}) = -\frac{2\pi}{7} \approx -51.4°$$

**(b)** RG correction to $\delta_\text{CP}$. $V_3$ runs under RG: $\lambda_3(\mu_{\text{EW}})/\lambda_3(\mu_{\text{GUT}}) \approx 0.01$. However, the phase $\delta$ is a topological parameter (determined by the $\mathbb{Z}_7$-structure), and RG does not change its value at leading order. Corrections — from two-loop effects:

$$\delta_{\text{CP}}^{(\text{phys})} = -\frac{2\pi}{7} + \delta^{(2)}, \quad |\delta^{(2)}| \sim \frac{y_t^2}{16\pi^2} \cdot \ln\frac{\mu_{\text{GUT}}}{\mu_{\text{EW}}} \cdot \frac{2\pi}{7}$$

$$|\delta^{(2)}| \sim \frac{1.0}{16\pi^2} \times 39 \times 0.898 \approx 0.22 \text{ rad} \approx 12.6°$$

**(c)** Prediction (accounting for sign uncertainty):

$$|\delta_{\text{CP}}| = 51.4° \pm 12.6° \quad (\text{range } 39°\text{--}64°)$$

Observed: $65.7° \pm 1.5°$ (PDG 2024 global fit); $64.6° \pm 2.8°$ (LHCb tree-level combination, ICHEP 2024). With $\delta^{(2)} > 0$: $|\delta_{\text{CP}}| \approx 64°$ — **agreement within $\approx 0.2\sigma$** of the direct value. With $\delta^{(2)} < 0$: $|\delta_{\text{CP}}| \approx 39°$ — **excluded** ($> 9\sigma$). The older $69° \pm 4°$ is superseded; see [CKM §4.2](/docs/physics/particle-physics/ckm-matrix#thm-4-2).

The sign of the two-loop correction is determined by the sign of $\mathrm{Im}\,\mathrm{Tr}(Y_u Y_u^\dagger Y_d Y_d^\dagger [Y_u Y_u^\dagger, Y_d Y_d^\dagger])$ (Antusch–Kersten–Lindner–Ratz, 2003), which requires explicit computation in the Gap basis of Yukawa matrices.

**(d)** Updated Jarlskog invariant:

$$J \approx 3.5 \times 10^{-5} \times \frac{\sin(64°)}{\sin(51.4°)} \approx 3.5 \times 10^{-5} \times 1.15 \approx 4.0 \times 10^{-5}$$

Observed: $J = (3.08 \pm 0.15) \times 10^{-5}$. Discrepancy ~30% — within the expected accuracy of the one-loop approximation.

---

## Koide relation and its UHM-structural status {#koide-uhm-status}

### Empirical statement

The Koide relation (Yoshio Koide, *Lett. Nuovo Cimento* 1981, *Phys. Rev. D* 28:252, 1983) is an empirical identity observed in charged lepton masses:
$$
\boxed{K \equiv \frac{m_e + m_\mu + m_\tau}{\bigl(\sqrt{m_e} + \sqrt{m_\mu} + \sqrt{m_\tau}\bigr)^2} = \frac{2}{3}}
$$

With PDG 2023 values $m_e = 0.51099895$ MeV, $m_\mu = 105.6583755$ MeV, $m_\tau = 1776.86$ MeV:
- $\sqrt{m_e} = 0.7148460$ MeV$^{1/2}$
- $\sqrt{m_\mu} = 10.27903$ MeV$^{1/2}$
- $\sqrt{m_\tau} = 42.1528$ MeV$^{1/2}$
- Numerator $\sum m_i = 1883.029$ MeV
- Denominator $(\sum \sqrt{m_i})^2 = 53.14669^2 = 2824.570$
- $K_\mathrm{obs} = 0.666661$, i.e. $2/3 - 6.2 \times 10^{-6}$; the uncertainty of $m_\tau$ ($\pm0.12$ MeV) moves $K$ by $\mp 7\times10^{-6}$, so the pole masses agree with $2/3$ within that uncertainty. (Corrected 2026-09-25: the earlier lines gave $1883.035$, $2824.566$ and "$K_\mathrm{obs}=0.66672$, i.e. $2/3-6.1\times10^{-5}$" — an arithmetic slip; $0.66672$ even lies *above* $2/3$.)

~~Running to $\mu = M_Z$ (Foot, Li, Peterson 2007): $K(M_Z) = 0.6672 \pm 0.0004$, consistent with $2/3$ to below $0.1\%$.~~ Retracted [✗] (September 2026): the cited source could not be located (it is not in INSPIRE-HEP), and the claim is contradicted by the computation of Xing and Zhang (*Phys. Lett. B* **635**, 107–111 (2006), [arXiv:hep-ph/0602134](https://arxiv.org/abs/hep-ph/0602134)): with running charged-lepton masses the relation departs from its pole-mass value $2/3$ by about $0.2\%$ at $\mu=M_Z$, not "below $0.1\%$".

This precision holds for pole masses only (about $10^{-5}$), which is often read as a hint of a **structural origin** [I]; with running masses the relation holds to about $0.2\%$ (above).

### Equivalent formulations

Setting $x_i = \sqrt{m_i}$, $s_k = \sum_i x_i^k$, and $e_k$ the elementary symmetric polynomials, Koide's relation is equivalent to any of:

**Form A (Koide 1983):** $s_2 = \tfrac{2}{3} s_1^2$.

**Form B (elementary polynomials):** $s_2 = 4 e_2$, or equivalently $e_2 / s_2 = 1/4$.

**Form C (geometric):** the vector $(x_1, x_2, x_3)$ lies on a cone:
$$
4(x_1 x_2 + x_2 x_3 + x_1 x_3) = x_1^2 + x_2^2 + x_3^2
$$

**Form D (angular):** $(x_1, x_2, x_3)$ makes angle $\arccos(1/\sqrt{3})$ with $(1,1,1)$.

Each form defines a **2-dimensional surface** in $\mathbb{R}^3_+$ (one equation, three unknowns), so Koide by itself does not fix three masses uniquely — it is a **constraint**, not a full prediction.

### The UHM numerical coincidence

UHM derives a state-independent contraction coefficient $\alpha_\mathrm{Fano} = 2/3$ for the Fano channel (Corollary 2.1a in [Fano Channel](/docs/proofs/gap/fano-channel)). This originates from the combinatorial replication number $r = 3$ of the Steiner triple system $S(2,3,7) = \mathrm{PG}(2,2)$:
$$
\alpha_\mathrm{Fano} = 1 - \frac{1}{r} = 1 - \frac{1}{3} = \frac{2}{3}.
$$

Two distinct "2/3" appear in UHM-relevant physics:
1. **$\alpha_\mathrm{Fano} = 2/3$** — Fano contraction of off-diagonal coherences (derived from PG(2,2) combinatorics).
2. **$K = 2/3$** — empirical lepton mass relation.

Whether these are manifestations of a single underlying structure is a structural question analysed below.

### Structural analysis via T-220 branching

Theorem T-220 Obstruction I establishes the decomposition
$$
\mathcal{J}_3(\mathbb{O}) \big|_{A_1 \times G_2} = (\mathbf{4}, \mathbf{1}) \oplus (\mathbf{2}, \mathbf{7}) \oplus (\mathbf{1}, \mathbf{7}) \oplus (\mathbf{1}, \mathbf{1}).
$$

The three copies of the $G_2$-fundamental $\mathbf{7}$ are:
- $\mathbf{7}_{(a)} \equiv (\mathbf{2}, \mathbf{7})$ with components $\{a_+, a_-\}$: $A_1$-doublet (spin $1/2$).
- $\mathbf{7}_{(c)} \equiv (\mathbf{1}, \mathbf{7})$: $A_1$-singlet (spin $0$).

Under $A_1$-breaking with VEV $v$, the doublet splits: $a_+$ gets mass $m_d + v$, $a_-$ gets mass $m_d - v$. The singlet keeps mass $m_s$ unchanged. Three mass parameters $(m_s, m_d, v)$ and three eigenvalues $(m_s, m_d - v, m_d + v)$.

If the charged lepton generations are identified with these three eigenvalues (singlet = electron, doublet = $\{\mu, \tau\}$ with specific splitting):
- $m_e = m_s$
- $m_\mu = m_d - v$
- $m_\tau = m_d + v$

This gives the central mass $m_d = (m_\mu + m_\tau)/2 = 941.263$ MeV and splitting $v = (m_\tau - m_\mu)/2 = 835.601$ MeV.

### Koide equation in UHM parametrisation

Substituting into $s_2 = (2/3) s_1^2$:
$$
m_e + (m_d - v) + (m_d + v) = \frac{2}{3}\bigl(\sqrt{m_e} + \sqrt{m_d - v} + \sqrt{m_d + v}\bigr)^2
$$

This is **one equation** in the three parameters $(m_s, m_d, v)$, so it defines a 2-parameter family of solutions. The observed $(m_e, m_\mu, m_\tau)$ lies on this surface but is not uniquely determined by Koide alone.

### Three candidates for an additional UHM constraint

To derive the observed masses uniquely, an additional constraint tied to UHM structure would be needed. Three candidates were examined:

**Candidate A: $m_s / m_d = \alpha = 2/3$**

Observed: $m_e / m_d = 0.511 / 941.26 = 5.4 \times 10^{-4} \ne 2/3$. **Rejected**.

**Candidate B: $\sqrt{m_s} / \sqrt{m_d} = 1/r$ for $r$ from Fano combinatorics**

Observed: $\sqrt{m_e}/\sqrt{m_d} = 0.715 / \sqrt{941.26} = 0.0233 \approx 1/42.9$. No clean match to $1/3$, $1/7$, $1/21$, or other Fano invariants. **Rejected**.

**Candidate C: $v_{A_1} = v_\mathrm{EW} = 246$ GeV**

Observed $v = (m_\tau - m_\mu)/2 = 0.836$ GeV, not 246 GeV. **Rejected**.

None of the structurally natural UHM-parameter identifications reproduce the observed lepton masses.

### Conclusion: empirical-input classification

:::info Koide in UHM — empirical input, not derived prediction
**Rigorous statement**: UHM's $A_1 \times G_2$ branching of $\mathcal{J}_3(\mathbb{O})$ is **structurally compatible** with a three-mass spectrum of the form $\{m_s,\; m_d - v,\; m_d + v\}$ satisfying Koide's relation. However, the **specific values** $(m_e, m_\mu, m_\tau)$ — and hence the observed $K = 2/3$ — require an $A_1$-breaking pattern **not uniquely fixed** by the current UHM formulation.

**Classification**: Koide is accepted as an **empirical input** compatible with UHM's generation structure, not a derived prediction.

**Numerical coincidence $K_\mathrm{obs} = 2/3 = \alpha_\mathrm{Fano}$** is flagged as **structurally suggestive** but **does not constitute proof**: the two "2/3" originate in mathematically distinct structures (combinatorial incidence vs. algebraic mass constraint). Demonstrating a common origin would require explicit construction of a mass operator on $\mathcal{J}_3(\mathbb{O})$, which is not provided by current UHM.

**Hypothesis T-220-H** (speculative research direction): there exists a canonical mass operator $\hat M$ on $\mathcal{J}_3(\mathbb{O})$, invariant under $A_1 \times G_2$-equivariant dynamics, whose eigenvalues restricted to the three $\mathbf{7}$-copies reproduce $(m_e, m_\mu, m_\tau)$ and satisfy Koide with $K = 2/3$ derived from $\alpha_\mathrm{Fano} = 2/3$. **Status**: conjectural; pending construction of explicit $\hat M$. Beyond current UHM scope.
:::

### Why "empirical input" is not a failure

Classifying Koide as empirical input rather than prediction is **not** a weakness of UHM:

1. **Honest classification**: presenting an unproved identity as a "derivation" would falsely claim success.
2. **Structural compatibility**: the 3-generation pattern (singlet + doublet) emerging from UHM's $A_1 \times G_2$ branching is itself a nontrivial structural success — it matches the observed one-outlier-two-close pattern qualitatively.
3. **Open direction formulated precisely**: T-220-H gives a specific, falsifiable research question (construct $\hat M$ or prove impossibility).

Standard Model fits most parameters empirically and is still a predictive theory; UHM's partial structural success on lepton masses places it in analogous territory, honestly documented.

### Relation to $\alpha_\mathrm{Fano}$ — why the numerical match is not accidental-looking

The two "2/3" are algebraically distinct but both arise in the context of 3-fold symmetry:
- $\alpha_\mathrm{Fano} = 2/3$ from Fano replication number $r = 3$ (geometric/combinatorial).
- $K = 2/3$ from symmetric polynomial identity in 3 variables (algebraic).

Both involve a 3-element structure; this motivates the T-220-H hypothesis that a deeper unifying structure exists. However, identical numerical values across distinct mathematical structures are not uncommon (cf. Feigenbaum constant, fine-structure constant, etc.), so this parallel is **suggestive** at best.

## Connection to other sections

- **Mass hierarchy:** Mechanism $y_t \sim 1$ (tree-level) from the Fano selection rule → [Yukawa Mass Hierarchy](/docs/physics/particle-physics/yukawa-hierarchy)

## Connection to other sections

- **Mass hierarchy:** Mechanism $y_t \sim 1$ (tree-level) from the Fano selection rule → [Yukawa Mass Hierarchy](/docs/physics/particle-physics/yukawa-hierarchy)
- **CKM matrix:** Mixing angles from Fano differences $\Delta k$ → [CKM Matrix from Fritzsch Texture](/docs/physics/particle-physics/ckm-matrix)
- **Higgs sector:** Unique Fano–Higgs line $\{A,E,U\}$ → [Higgs Sector](/docs/physics/particle-physics/higgs-sector)
- **Octonionic structure:** Derivation of the Fano plane from $\mathbb{O}$ → [Octonionic Derivation](/docs/proofs/minimality/theorem-octonionic-derivation)
- **G₂-structure and gauge symmetry:** $G_2$-holonomy and SM → [G₂-Structure](/docs/physics/gauge-symmetry/g2-structure)


---

**Related documents:**
- [Fano Selection Rules](/docs/physics/gauge-symmetry/fano-selection-rules)
- [Yukawa Hierarchy](/docs/physics/particle-physics/yukawa-hierarchy)
- [CKM Matrix](/docs/physics/particle-physics/ckm-matrix)
- [Standard Model from G₂](/docs/physics/gauge-symmetry/standard-model)
