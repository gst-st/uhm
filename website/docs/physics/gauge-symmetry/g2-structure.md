---
sidebar_position: 1
title: "G₂-Structure and the Fano Plane"
---

# G₂-Structure and the Fano Plane

:::info For whom this chapter is intended
The group $G_2 = \mathrm{Aut}(\mathbb{O})$ and the Fano plane $\mathrm{PG}(2,2)$ as the central algebraic structures of UHM theory. The reader will learn how the multiplication table of the octonions determines the physical architecture of the theory.
:::


## Overview

The group $G_2 = \mathrm{Aut}(\mathbb{O})$ — the automorphism group of the octonions — is the central algebraic structure of UHM theory. The Fano plane $\mathrm{PG}(2,2)$ encodes the multiplication table of the imaginary units of $\mathbb{O}$ and determines the entire physical architecture of the theory: from Lindblad operators to gauge symmetries and selection rules.

---

## 1. Fano Plane PG(2,2)

### 1.1 Definition

The **Fano plane** $\mathrm{PG}(2,2)$ is the minimal finite projective plane. It contains:
- **7 points**, identified with the 7 imaginary units of the octonions $e_1, \ldots, e_7$, and in UHM theory — with the 7 dimensions $\{A, S, D, L, E, U, O\} = \{1, 2, 3, 4, 5, 6, 7\}$
- **7 lines**, each containing exactly 3 points

### 1.2 Table of Fano Lines {#12-таблица-фано-линий}

| # | Fano line | Dimensions |
|---|-----------|-----------|
| 1 | $\{1, 2, 4\}$ | $\{A, S, L\}$ |
| 2 | $\{2, 3, 5\}$ | $\{S, D, E\}$ |
| 3 | $\{3, 4, 6\}$ | $\{D, L, U\}$ |
| 4 | $\{4, 5, 7\}$ | $\{L, E, O\}$ |
| 5 | $\{5, 6, 1\}$ | $\{E, U, A\}$ |
| 6 | $\{6, 7, 2\}$ | $\{U, O, S\}$ |
| 7 | $\{7, 1, 3\}$ | $\{O, A, D\}$ |

### 1.3 Fundamental Properties

1. **Through any two points there passes exactly one line.** This means that every pair of dimensions $(i, j)$ uniquely determines a Fano line $(i, j, k)$.

2. **Each point lies on exactly 3 lines.** Consequently:

$$\sum_{p=1}^{7} \Pi_p = 3I$$

where $\Pi_p = \sum_{i \in \mathrm{line}_p} |i\rangle\langle i|$ is the projector onto the subspace corresponding to Fano line $p$.

3. **Octonion structure constants** $f_{ijk}$: $f_{ijk} = \pm 1$ if and only if $\{i, j, k\}$ is a Fano line, and $f_{ijk} = 0$ otherwise. The multiplication table of $\mathbb{O}$:

$$e_i \cdot e_j = f_{ijk}\, e_k - \delta_{ij}$$

### 1.4 Automorphism Group

$$\mathrm{Aut}(\mathrm{PG}(2,2)) = \mathrm{PSL}(2,7)$$

This is the group of order 168, isomorphic to $\mathrm{GL}(3, \mathbb{F}_2)$. It acts transitively on both points and lines.

---

## 2. Octonionic Multiplication and $G_2$ {#октонионное-умножение-и-g2}

### 2.1 The Octonion Algebra $\mathbb{O}$

The octonions are an 8-dimensional real division algebra. Each octonion is written as:

$$x = x_0 \cdot 1 + \sum_{i=1}^{7} x_i \, e_i, \quad x_0, x_i \in \mathbb{R}$$

where $1$ is the real unit, and $e_1, \ldots, e_7$ are imaginary units satisfying:

$$e_i^2 = -1, \quad e_i \cdot e_j = -e_j \cdot e_i \;\; (i \neq j)$$

In UHM theory the imaginary units are identified with the 7 dimensions: $e_1 = A$, $e_2 = S$, $e_3 = D$, $e_4 = L$, $e_5 = E$, $e_6 = U$, $e_7 = O$.

### 2.2 Octonion Multiplication Table

The multiplication of imaginary units is **completely** determined by the Fano plane. For each Fano line $(i, j, k)$ with canonical ordering:

$$e_i \cdot e_j = e_k, \quad e_j \cdot e_k = e_i, \quad e_k \cdot e_i = e_j$$

| $\times$ | $e_1$ (A) | $e_2$ (S) | $e_3$ (D) | $e_4$ (L) | $e_5$ (E) | $e_6$ (U) | $e_7$ (O) |
|----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
| $e_1$ (A) | $-1$ | $e_4$ | $e_7$ | $-e_2$ | $e_6$ | $-e_5$ | $-e_3$ |
| $e_2$ (S) | $-e_4$ | $-1$ | $e_5$ | $e_1$ | $-e_3$ | $e_7$ | $-e_6$ |
| $e_3$ (D) | $-e_7$ | $-e_5$ | $-1$ | $e_6$ | $e_2$ | $-e_4$ | $e_1$ |
| $e_4$ (L) | $e_2$ | $-e_1$ | $-e_6$ | $-1$ | $e_7$ | $e_3$ | $-e_5$ |
| $e_5$ (E) | $-e_6$ | $e_3$ | $-e_2$ | $-e_7$ | $-1$ | $e_1$ | $e_4$ |
| $e_6$ (U) | $e_5$ | $-e_7$ | $e_4$ | $-e_3$ | $-e_1$ | $-1$ | $e_2$ |
| $e_7$ (O) | $e_3$ | $e_6$ | $-e_1$ | $e_5$ | $-e_4$ | $-e_2$ | $-1$ |

Each row and column contains all 7 imaginary units exactly once (up to sign) — a division algebra.

### 2.3 The Group $G_2 = \mathrm{Aut}(\mathbb{O})$

**Definition.** The group $G_2$ is the group of all $\mathbb{R}$-linear bijections $g: \mathbb{O} \to \mathbb{O}$ preserving multiplication:

$$G_2 = \{g \in \mathrm{GL}(\mathbb{O}) : g(xy) = g(x)g(y) \; \forall x, y \in \mathbb{O}\}$$

Since $g(1) = 1$ for any automorphism, $g$ acts on the 7-dimensional subspace of imaginary octonions $\mathrm{Im}(\mathbb{O}) \cong \mathbb{R}^7$.

:::tip[Status: Theorem \[T\]]
$G_2$ is an exceptional compact simple Lie group with the following characteristics:
- $\dim(G_2) = 14$
- $\mathrm{rank}(G_2) = 2$
- $G_2 \subset \mathrm{SO}(7)$ — a proper subgroup of the rotation group of $\mathbb{R}^7$
:::

**Why $\dim(G_2) = 14$?** The group $\mathrm{SO}(7)$ has dimension $7 \cdot 6 / 2 = 21$. The condition of preserving octonionic multiplication imposes 7 independent constraints (one per Fano line): $g(e_i \cdot e_j) = g(e_i) \cdot g(e_j)$ for all $(i,j,k) \in \mathrm{PG}(2,2)$. Total:

$$\dim(G_2) = 21 - 7 = 14$$

**Why $\mathrm{rank}(G_2) = 2$?** The maximal torus of $G_2$ is two-dimensional: it is generated by two commuting rotations in $\mathbb{R}^7$ compatible with all 7 Fano lines. Two independent angles $(\theta_1, \theta_2)$ parametrise the maximal torus, yielding 2 quantum numbers — Noether charges (see [G₂-Noether Charges](/docs/physics/gauge-symmetry/noether-charges)).

### 2.4 Fourteen Generators of $G_2$ {#генераторы-g2}

The Lie algebra $\mathfrak{g}_2$ has 14 generators, which can be decomposed with respect to the representations of the subgroup $\mathrm{SU}(3) \subset G_2$:

$$\mathfrak{g}_2 = \mathfrak{su}(3) \oplus \mathbb{C}^3$$

| Type | Count | $\mathrm{SU}(3)$ representation | Physical interpretation in UHM |
|-----|-------|-------------------------------|-------------------------------|
| $\mathrm{SU}(3)$ generators | 8 | $\mathbf{8}$ (adjoint) | Unitary rotations of the three complex coordinates $A-iD$, $S-iU$, $L-iE$ among themselves, fixing $O$; analogue of gluon fields. (The earlier gloss "gauge transformations between triples of dimensions on a single Fano line" is retracted [✗]: no generator acts inside a single Fano line, §2.6.) |
| Additional generators | 6 | $\mathbf{3} \oplus \bar{\mathbf{3}}$ | The generators that move the $O$-direction: they span the tangent space of $S^6=G_2/\mathrm{SU}(3)$ at $e_O$. (The earlier gloss "mixing dimensions from different Fano lines" described no invariant property and is withdrawn.) |

All 14 generators are anti-Hermitian $7 \times 7$ matrices $T_a \in \mathfrak{so}(7)$ satisfying:

$$[T_a, T_b] = f_{ab}^{\;\;c}\, T_c, \quad a, b, c = 1, \ldots, 14$$

where $f_{ab}^{\;\;c}$ are the structure constants of $\mathfrak{g}_2$.

### 2.5 Example: Octonionic Multiplication and Non-associativity {#пример-октонионное-умножение}

The octonions are the **unique** normed division algebra that is **non-associative**. Let us demonstrate this with a concrete example.

**Problem.** Compute $(e_1 \cdot e_2) \cdot e_3$ and $e_1 \cdot (e_2 \cdot e_3)$ and verify that the results differ.

**Step 1.** From the multiplication table (Fano line $\{1,2,4\}$):

$$e_1 \cdot e_2 = e_4 \quad (\text{A} \cdot \text{S} = \text{L})$$

**Step 2.** Now multiply the result by $e_3$ (Fano line $\{3,4,6\}$):

$$(e_1 \cdot e_2) \cdot e_3 = e_4 \cdot e_3 = -e_6 \quad (\text{L} \cdot \text{D} = -\text{U})$$

(the minus sign — because the canonical orientation of line $\{3,4,6\}$ gives $e_3 \cdot e_4 = e_6$, and we are multiplying in the reverse order).

**Step 3.** Separately compute the right bracket (Fano line $\{2,3,5\}$):

$$e_2 \cdot e_3 = e_5 \quad (\text{S} \cdot \text{D} = \text{E})$$

**Step 4.** Multiply $e_1$ by the result (Fano line $\{5,6,1\}$):

$$e_1 \cdot (e_2 \cdot e_3) = e_1 \cdot e_5 = e_6 \quad (\text{A} \cdot \text{E} = \text{U})$$

**Result:**

$$(e_1 \cdot e_2) \cdot e_3 = -e_6, \quad e_1 \cdot (e_2 \cdot e_3) = +e_6$$

The difference: $(e_1 \cdot e_2) \cdot e_3 - e_1 \cdot (e_2 \cdot e_3) = -2e_6$. The non-associativity is manifest.

:::tip[Physical Interpretation]
In terms of UHM dimensions: the sequence of interactions $A \to S \to D$ yields **different** results depending on the grouping order. This means that the octonionic structure encodes the **contextual dependence** of coherent transitions: the result depends not only on the participating dimensions, but also on the order of their involvement.
:::

### 2.6 Precedents and related programmes {#прецеденты-g2}

Nothing in §§1–2 is new mathematics, and much of its physical reading is not new either. Since 1973 a line of work — here called the *octonionic lineage* — has used $G_2=\mathrm{Aut}(\mathbb{O})$, its subgroup $\mathrm{SU}(3)$ and the Fano plane to model quarks and the Standard Model. This subsection names the works that first did what this page does, so that the reader can tell what UHM takes over from what it adds. The whole lineage, with the current standing of each programme, is reviewed in [Octonionic derivation, §5.7](/docs/proofs/minimality/theorem-octonionic-derivation#прецеденты-октонионы).

**Günaydın and Gürsey (1973, 1974): colour inside $G_2$.** Murat Günaydın and Feza Gürsey were the first to read the subgroup of $G_2$ that fixes one imaginary unit as the colour group of quarks — the reading that this page and the [Standard Model page](/docs/physics/gauge-symmetry/standard-model) give to $\mathrm{SU}(3)\subset G_2$. In "Quark structure and octonions" (*J. Math. Phys.* **14**, 1651–1667 (1973), DOI [10.1063/1.1666240](https://doi.org/10.1063/1.1666240)) they wrote $\mathbb{O}$ in a *split basis* — complex combinations of pairs of imaginary units, adapted to one chosen unit $u$ — and reduced $G_2$ to $\mathrm{SU}(3)=\mathrm{Stab}_{G_2}(u)$, the automorphisms that leave $u$ fixed. Under this subgroup the seven imaginary units become a singlet ($u$ itself) plus a colour triplet and anti-triplet, $7=1\oplus3\oplus\bar{3}$, and the fourteen generators become $8\oplus3\oplus\bar{3}$ — the decomposition of §2.4. In "Quark statistics and octonions" (*Phys. Rev. D* **9**, 3387–3391 (1974), DOI [10.1103/PhysRevD.9.3387](https://doi.org/10.1103/PhysRevD.9.3387)) they went on to treat quark fields as octonionic fields. *Standing:* the group theory is standard and uncontested; as a model of quarks the programme was not adopted — quantum chromodynamics uses $\mathrm{SU}(3)_c$ with no octonionic structure — and it survives as the starting point of later work: Furey's thesis calls it "one of the earliest breakthroughs" of the field and extends it ([arXiv:1611.09182](https://arxiv.org/abs/1611.09182)). *Parallel in UHM:* the table of §2.4 (the $\mathfrak{su}(3)$ generators as an "analogue of gluon fields"), the gauge analogy of §3b, and $\mathrm{SU}(3)_C$ as the stabiliser of the $O$-direction [I]. *Difference:* the decomposition and its reading as colour are prior art from 1973; UHM cannot count either among its own results. What is UHM's own on this page is the use of $G_2$ as a symmetry of a $7\times7$ coherence matrix and its breaking by the pinching dynamics to the finite frame group $\Gamma_{\!\text{oct}}$ (§7); nothing in the lineage corresponds to that.

The precedent also fixes what the triplet is, and this corrects the gloss of §2.4. Take the table of §2.2 and fix the unit $O=e_7$. Left multiplication by $e_7$ squares to $-1$ on the six remaining axes, so it serves as the imaginary unit of a complex structure, and it pairs these axes along the three Fano lines through $O$: $A\leftrightarrow D$, $S\leftrightarrow U$, $L\leftrightarrow E$. The three pairs are the three complex coordinates on which $\mathrm{SU}(3)$ acts as on $\mathbb{C}^3$; Todorov and Dubois-Violette write the same split with the same Fano labelling (eq. 2.5 of the paper cited below). In these coordinates every nonzero element of $\mathfrak{su}(3)$ is a traceless $3\times3$ matrix and therefore acts on at least two of the three lines through $O$; no generator acts inside a single Fano line (a direct check against the table finds none for any of the seven lines). The description "gauge transformations between triples of dimensions on a single Fano line" in §2.4 is therefore retracted there. The same precedent refutes the axis-labelled sector split $7=1_O\oplus3_{\{A,S,D\}}\oplus\bar3_{\{L,E,U\}}$ used elsewhere in the corpus; it is retracted in [Spacetime](/docs/core/foundations/spacetime#секторная-декомпозиция) and on the [Standard Model page](/docs/physics/gauge-symmetry/standard-model), Theorem 1.1(a).

**Holland, Minkowski, Pepe and Wiese (2003): $G_2$ as a gauge group.** Lattice field theorists study a gauge theory whose gauge group is $G_2$ itself, to learn how quarks are confined when the centre symmetry of $\mathrm{SU}(3)$ is absent: the centre of $G_2$ is trivial. In "Exceptional confinement in G(2) gauge theory" (*Nucl. Phys. B* **668**, 207–236 (2003), [arXiv:hep-lat/0302023](https://arxiv.org/abs/hep-lat/0302023)) the fourteen gauge bosons transform under $\mathrm{SU}(3)\subset G_2$ as $8\oplus3\oplus\bar{3}$ — "gluons" plus vectors with the colour quantum numbers of quarks and antiquarks — and a Higgs field in the $7$ breaks $G_2$ to $\mathrm{SU}(3)$, giving the six extra vectors a mass; the lattice results show that $G_2$ confines without a centre. *Standing:* an established laboratory for confinement mechanisms — a model, not a claim about nature. *Parallel:* the six "additional generators" of §2.4 and the "$G_2$-extra bosons" of the Standard Model page [I]. *Difference:* six extra vectors in $3\oplus\bar{3}$ that become massive when a Higgs mechanism breaks $G_2$ to $\mathrm{SU}(3)$ are a property of every such gauge theory; their existence is therefore not a prediction specific to UHM — only their masses and couplings could be.

**Todorov and Dubois-Violette (2018): what $G_2$ alone can give.** Ivan Todorov and Michel Dubois-Violette asked which Standard Model groups follow from the octonions by group theory alone ("Deducing the symmetry of the standard model from the automorphism and structure groups of the exceptional Jordan algebra", *Int. J. Mod. Phys. A* **33**, 1850118 (2018), [arXiv:1806.09450](https://arxiv.org/abs/1806.09450)). They use Borel–de Siebenthal theory, which lists the maximal connected subgroups of full rank (the rank is the dimension of a maximal torus) of a compact Lie group. For $G_2$ these are $\mathrm{SU}(3)$ and $(\mathrm{SU}(2)\times\mathrm{SU}(2))/\mathbb{Z}_2$; their intersection is $\mathrm{U}(2)$, the electroweak group, which has lost colour, and the only one that keeps colour is $\mathrm{SU}(3)$ itself. The full group $G_{\mathrm{SM}}=S(\mathrm{U}(2)\times\mathrm{U}(3))=(\mathrm{SU}(3)\times\mathrm{SU}(2)\times\mathrm{U}(1))/\mathbb{Z}_6$ appears one level up, as the intersection of the maximal subgroups $\mathrm{Spin}(9)$ and $(\mathrm{SU}(3)\times\mathrm{SU}(3))/\mathbb{Z}_3$ of $F_4$, the automorphism group of the exceptional Jordan algebra $J_3(\mathbb{O})$ of Hermitian octonionic $3\times3$ matrices. *Standing:* a published group-theoretic result, followed up by Krasnov (*J. Math. Phys.* **62**, 021703 (2021)) and Boyle (*J. Math. Phys.* **67**, 071701 (2026)); its physical meaning remains a research programme. *Parallel:* the rank problem acknowledged on the [Standard Model page](/docs/physics/gauge-symmetry/standard-model#проблема-ранга), $\mathrm{rank}\,G_2 = 2 < 4 = \mathrm{rank}\,G_{\mathrm{SM}}$ [I]. *Difference:* the lineage reaches $G_{\mathrm{SM}}$ by enlarging the symmetry from $G_2$ to $F_4$, a theorem of Lie theory; UHM keeps $G_2$ and supplied the missing rank by constructions outside $G_2$ (the Fano-electroweak construction and a Page–Wootters tensor factor); no result in the corpus shows that route equivalent to the $F_4$ one. *Corrected embedding (2026-09-25, [T-326](/docs/physics/gauge-symmetry/standard-model#sm-из-клиффорда)):* the rank is supplied correctly one step up, through $\mathrm{Spin}(9)$ rather than inside $G_2$. On $\mathcal S = \mathbb C\otimes\mathbb O$ — the holon's $\mathbb C^7$ plus the $G_2$-parallel spinor — the operators $iL_{e_k}$, $J$, $iJ$ form a Clifford system of nine generators, forced and maximal, which generates $\mathfrak{spin}(9)$; the centraliser of colour $\mathrm{SU}(3)_C = \mathrm{Stab}_{G_2}(e_O)$ in it is $\mathfrak u(2)$, and the normaliser of colour is $G_{\mathrm{SM}} = (\mathrm{SU}(3)\times\mathrm{SU}(2)\times\mathrm{U}(1))/\mathbb Z_6$, equal to the centraliser of $R_{e_O}$ (Krasnov 2021). This is [T] as mathematics and [C at (Cl)] as a result of UHM; it is the $\mathrm{Spin}(9)$ half of the route of Todorov–Dubois-Violette and Krasnov, not a new route. The Fano-electroweak axis construction stays [C at (FE)] with its uniqueness [H].

**Baez (2002): the Fano plane as a multiplication table.** John Baez's review "The Octonions" (*Bull. Amer. Math. Soc.* **39**, 145–205 (2002), [arXiv:math/0105155](https://arxiv.org/abs/math/0105155)) is the standard modern reference for §§1–2. It shows that the Fano plane, with each of its seven lines given a cyclic orientation, "completely describes the algebra structure of the octonions", and that doubling every index, $e_i\mapsto e_{2i}$, is a symmetry of the picture. *Standing:* standard and uncontested as mathematics; on physics its author wrote that "there is still no proof that the octonions are useful for understanding the real world". *Parallel:* the table of Fano lines in §1.2 and the multiplication table of §2.2. *Difference:* the orientation of each line is data beyond the seven unordered triples; what this means for the derivation of $\mathbb{O}$ is discussed in [Octonionic derivation, §5.7](/docs/proofs/minimality/theorem-octonionic-derivation#прецеденты-октонионы).

### 2.7 Space is not a subspace of $\mathrm{Im}\,\mathbb O$ {#пространство-не-в-im-o}

Colour cannot be read as space, and this has a sharp form: the centraliser of $\mathrm{SU}(3)=\mathrm{Stab}_{G_2}(e_O)$ is finite in $G_2$, is $\mathrm U(1)$ in $\mathrm{SO}(7)$ and $\mathrm U(1)^3$ in $\mathrm U(7)$. So no $\mathrm{SO}(3)$ acting on the seven axes commutes with colour. This covers the associative 3-planes too. The rotations of the span of a Fano line lie in its $\mathfrak{so}(4)$ stabiliser, which meets $\mathfrak{su}(3)$ in $\mathfrak u(2)$ (the three lines through $O$) or in an $\mathfrak{so}(3)$ (the other four). What does commute with colour is found one level up, in the spin factor $\mathfrak h_2(\mathbb O)\cong\mathbb R^{1,9}$. There the fixed part of $\mathrm{SU}(3)$ is $\mathfrak h_2(\mathbb C_O)\cong\mathbb R^{1,3}$, with $\mathbb C_O=\mathrm{span}\{1,e_O\}$, and the centraliser of $\mathfrak{su}(3)$ in $\mathfrak{so}(1,9)$ is $\mathfrak{so}(1,3)\oplus\mathfrak u(1)$: [Spacetime, Theorem 48c](/docs/core/foundations/spacetime#теорема-48c) — [T] as mathematics, [C at (Q)] as spacetime.

---

## 3. $G_2 = \mathrm{Aut}(\mathbb{O})$ and its Action on Coherences {#g2-действие}

### 3.1 Action of $G_2$ on the Space of Coherences

Upon identifying $e_i \leftrightarrow$ dimensions (from the `dimensions.md` table), the group $G_2$ acts on the $7D$ space:

$$g \in G_2: \quad |i\rangle \mapsto \sum_j D_{ji}(g) |j\rangle$$

where $D(g)$ is the 7-dimensional (fundamental) representation of $G_2$.

**Action on the coherence matrix:**

$$g: \Gamma \mapsto D(g)\, \Gamma\, D(g)^\dagger$$

**Action on coherences:**

$$g: \gamma_{ij} \mapsto \sum_{k,l} D_{ki}(g)\, D_{lj}^*(g)\, \gamma_{kl}$$

### 3.2 $G_2$ Preserves the Fano Structure

Since $G_2 = \mathrm{Aut}(\mathbb{O})$ preserves octonionic multiplication, it preserves the structure constants $f_{ijk}$ as a **tensor** (the associative 3-form $\varphi$). It does **not** permute the seven coordinate Fano lines — that is done only by the finite frame subgroup $\Gamma_{\!\text{oct}}\subset G_2$ of signed permutation matrices, of order $1344=2^3\cdot168$, which acts on the lines through its quotient $\mathrm{Aut}(PG(2,2))\cong PSL(2,7)$ of order 168 (`test_frame_group_order_and_singer_subgroups`; [uniqueness theorem](/docs/proofs/categorical/uniqueness-theorem#g2-ригидность)); a generic $g\in G_2$ rotates the coordinate axes (irreducibility of $\mathbf 7$):

$$g \in G_2 \ \Rightarrow\ g^\ast\varphi = \varphi; \qquad g \in \Gamma_{\!\text{oct}} \ \Rightarrow\ g \text{ permutes the Fano lines}.$$

~~More precisely: for each $g \in G_2$ there exists a permutation $\sigma_g$ on the set $\{1, \ldots, 7\}$ of lines with $g\, \Pi_p\, g^\dagger = \Pi_{\sigma_g(p)}$.~~ Retracted [✗] (2026-09-25): this holds only for $g\in\Gamma_{\!\text{oct}}$, as the paragraph above and Theorem 11.2 say; for a generic $g\in G_2$ no $g\,\Pi_p\,g^\dagger$ is a coordinate line projector, because $\mathbb{C}^7$ is irreducible under $G_2$. (The identification "$\Gamma_{\!\text{oct}}\cong PSL(2,7)$" written here earlier confused the frame group with its image on the lines.)

---

## 3b. Physical Interpretation of $G_2$-Symmetry {#физическая-интерпретация-g2}

### What $G_2$-Invariance Preserves

$G_2$-symmetry is the **continuous kinematic symmetry** of UHM theory, which is **spontaneously broken** upon dynamical vacuum fixation. Before minimization of $V_{\text{Gap}}$: $G_2$ transformations rename the basis $\{A, S, D, L, E, U, O\}$, preserving the octonionic structure and all $G_2$-invariants ($P$, $R$, spectrum of $\Gamma$; not $\Phi$, see the table below). **After** minimization (T-64 [H] (restated; sector values: hypothesis (SV))): a specific vacuum $\Gamma_{\text{vac}}$ is fixed, breaking $G_2 \to H$ (vacuum stabilizer). The Boolean fragment $\mathrm{Dec}(\Omega) \cong 2^7$ crystallizes as the pointer basis selected by spontaneous symmetry breaking — analogous to the Higgs mechanism $SU(2) \times U(1) \to U(1)_{\text{em}}$. [Goldstone modes](/docs/applied/coherence-cybernetics/goldstone-modes) — massless excitations along the broken directions $G_2/H$.

:::tip[Status: Theorem \[T\]]
The $G_2$-transformation $g: \Gamma \mapsto D(g)\,\Gamma\,D(g)^\dagger$ preserves the following physical quantities:

| Invariant | Formula | Physical meaning |
|-----------|---------|-----------------|
| Total purity | $P = \mathrm{Tr}(\Gamma^2)$ | Degree of consciousness integration |
| Reflection measure | $R = R(\Gamma)$ | Depth of self-observation |
| ~~Integration~~ | ~~$\Phi = \Phi(\Gamma)$~~ | **Not invariant — retracted [✗]:** an explicit $g\in G_2$ takes $\Phi$ from 0 to 1 (`test_phi_not_g2_invariant`) |
| Spectrum of $\Gamma$ | $\lambda_1 \geq \cdots \geq \lambda_7$ | Eigenvalue populations |
| ~~Total coherence~~ | ~~$\sum_{i < j} \|\gamma_{ij}\|^2$~~ | **Not invariant — retracted [✗]:** it equals $\tfrac12(P-\sum_i\gamma_{ii}^2)$, and the same $g$ takes it from 0 to $\tfrac14$ at fixed $P=1$ |
| Fano structure | $f_{ijk}$ | Octonion multiplication table |
:::

### What $G_2$ Does NOT Preserve

The $G_2$-transformation **mixes** specific dimensions. In general:

- **Populations of individual dimensions** $\gamma_{ii}$ are not invariant: $G_2$ can transfer population from $A$ to $S$.
- **Specific coherences** $\gamma_{ij}$ are not invariant: the $A \leftrightarrow S$ coupling can transform into $D \leftrightarrow L$.
- **Gap profile** $\{\mathrm{Gap}(i,j)\}_{i<j}$ is not invariant elementwise (although the total Gap is invariant).
- **Stress vector** $\sigma_k = 1 - 7\gamma_{kk}$ is not invariant componentwise.

### Geometric Meaning: Rotations in $\{A, S, D, L, E, U, O\}$

A $G_2$-transformation can be viewed as a **rotation** of the 7-dimensional space that:

1. **Preserves the octonionic 3-form:** it maps the span of each Fano line (an associative 3-plane) to an associative 3-plane — in general **not** to the span of one of the seven coordinate lines; only the finite frame group $\Gamma_{\!\text{oct}}$ permutes those (§3.2). The earlier wording "if $\{i,j,k\}$ is a Fano line, then the image $\{g(i), g(j), g(k)\}$ is also a Fano line" is retracted [✗].
2. **Is not arbitrary:** of the 21 possible rotations in $\mathrm{SO}(7)$, only the 14-dimensional submanifold $G_2$ preserves octonionic multiplication.
3. **Physically:** a $G_2$-transformation is a change of 'coordinate system' in the space of dimensions: the multiplication table written in the rotated basis $\{g e_1,\dots,g e_7\}$ is the same table. The coordinate lines themselves, and quantities read off them ($\Phi$, the Gap profile, populations), are not preserved.

:::warning[$G_2$-Covariance Principle]
The physical laws of UHM theory (evolution, consciousness thresholds, Lindblad operators) must be formulated in terms of $G_2$-invariants. The specific 'label' of a dimension ($A$, $S$, $D$, ...) is a matter of basis choice, not of physics.
:::

### Analogy with Gauge Theories

| Theory | Gauge group | What is preserved | What is mixed |
|--------|---------------------|-----------------|-------------------|
| Electrodynamics | $U(1)$ | Charge | Phase of the wave function |
| Chromodynamics | $SU(3)$ | Color singlet | Quark color (r, g, b) |
| **UHM** | $G_2$ | $P$, $R$, spectrum, Fano structure (not $\Phi$) | Dimension labels $\{A,S,D,L,E,U,O\}$ |

In this sense $G_2$ for UHM theory is the analogue of $SU(3)_c$ for QCD: specific 'colors' (dimensions) are not directly observable; only invariant combinations are observable.

---

## 4. $G_2$-Invariants of the Gap Profile

### Theorem 2.1 ($G_2$-Invariants of the Gap Profile)

:::tip[Status: Theorem \[T\]]
The following quantities are $G_2$-invariants (unchanged under $G_2$ transformations).
:::

**(a)** Total purity: $P = \mathrm{Tr}(\Gamma^2)$ — invariant under $\mathrm{SO}(7) \supset G_2$.

**(b)** Total Gap:

$$\mathcal{G}_{\mathrm{total}} := \sum_{i<j} |\gamma_{ij}|^2 \cdot \mathrm{Gap}(i,j)^2 = \sum_{i<j} |\mathrm{Im}(\gamma_{ij})|^2$$

The total 'imaginary energy' of coherences is invariant under $\mathrm{SO}(7)$.

**(c)** However, the **distribution** of Gap over pairs $(i,j)$ is **not** a $G_2$-invariant. $G_2$ 'mixes' Gap between pairs, preserving only the total.

**Proof.** (a) and (b) follow from the unitary invariance of the Frobenius norm. (c) follows from the fact that $G_2$ is not diagonal in the basis $\{|i\rangle\}$. $\blacksquare$

### Theorem 2.2 ($G_2$-Orbits of Gap Profiles)

:::tip[Status: Theorem \[T\]]
The set of all possible Gap profiles $\{\mathrm{Gap}(i,j)\}_{i<j}$ for a fixed $\Gamma$ decomposes into $G_2$-orbits.
:::

**(a)** The total number of $G_2$-invariants for a Hermitian $7 \times 7$ matrix: $48 - 14 = 34$, where $14 = \dim(G_2)$. These are the **kinematic** invariants (spectrum and $\varphi_3$-relative angles); they are *not* the physically distinguishable configurations, because the pinching dynamics breaks $G_2$ to the finite frame group $\Gamma_{\!\text{oct}}$ (Theorem 11.2 below), so all 48 parameters are physical and the Gap profile is read in the pinned frame ([frame decision D-0910](/docs/proofs/categorical/uniqueness-theorem#g2-ригидность)). The [$G_2$-rigidity theorem](/docs/proofs/categorical/uniqueness-theorem#физические-состояния) [T] proves that $G_2$ is the **maximal** subgroup of $U(7)$ preserving the octonionic 3-form (Lemma G4), while the frame data are preserved only by the finite $\Gamma_{\!\text{oct}}$. The count $48 \to 34$ is not an arbitrary choice, but a **kinematic** consequence of the uniqueness of the holonomy representation.

**(b)** Of the 21 Gap values, only $34 - 7 = $ **up to 27** are 'physically distinguishable' (7 populations are subtracted from the invariants).

**(c)** This means that $21 - (27 - 21) = $ **all 21 Gaps** can be distinguishable, but with 14 relations between them. These 14 relations hold among the kinematic $G_2$-invariants only; in the pinned physical frame (D-0910) all 21 Gaps are independent observables.

### Corollary: $G_2$-Reduction of Diagnostics

If the UHM evolution equations are $G_2$-covariant, a full diagnostic requires measuring only:

- 7 populations $\gamma_{ii}$
- 7 moduli $|\gamma_{ij}|$ for one 'base set' of pairs
- 7 phases $\theta_{ij}$ for the same set

The remaining 27 parameters are computed from $G_2$ relations.

:::warning[Status: premise false — the corollary does not apply]
The evolution equations are **not** $G_2$-covariant: the pinching dissipator is covariant only under the finite frame group $\Gamma_{\!\text{oct}}$ (Theorem 11.2), and the degree of $G_2$ breaking is $\tfrac{2+\alpha}{3}\Delta_{\max} > 0$ for every $\alpha$ (Theorem 11.3 below). So the reduction to 21 measured parameters never applies: all 48 are measured ([frame decision D-0910](/docs/proofs/categorical/uniqueness-theorem#g2-ригидность)). This box used to be labelled "Open Problem [H]"; the question is settled in the negative.
:::

---

## 5. Fano-Structured Lindblad Operators

### 5.1 Two Types of Classifier Atoms

From L-unification: Lindblad operators $L_k = \sqrt{\chi_{S_k}}$ are derived from **atoms** of the classifier $\Omega$. There are two types:

**Basis atoms** (7 in total):

$$S_k = |k\rangle\langle k|, \quad k \in \{A, S, D, L, E, U, O\}$$

**Composite atoms** (7 in total): the Fano lines define 7 **linear subobjects** — projections onto 3-dimensional subspaces:

$$\Pi_p = \sum_{i \in \mathrm{line}_p} |i\rangle\langle i|, \quad p = 1, \ldots, 7$$

Each Fano line $p = (i, j, k)$ generates a **composite atom** $S_p = \mathrm{span}\{|i\rangle, |j\rangle, |k\rangle\}$.

### Theorem 10.0 (Completeness of Fano Atoms)

:::tip[Status: Theorem \[T\]]
Each dimension lies on exactly 3 Fano lines.
:::

$$\sum_{p=1}^{7} \Pi_p = 3I$$

**Proof.** A property of the Fano plane: each of the 7 points is incident to exactly 3 lines. $\blacksquare$

### 5.2 Definition (Fano-Structured Lindblad Operators)

For each Fano line $p = (i, j, k)$, a Lindblad operator is defined:

$$L_p^{\mathrm{Fano}} := \frac{1}{\sqrt{3}} \Pi_p = \frac{1}{\sqrt{3}}(|i\rangle\langle i| + |j\rangle\langle j| + |k\rangle\langle k|)$$

**CPTP verification:**

$$\sum_{p=1}^{7} (L_p^{\mathrm{Fano}})^\dagger L_p^{\mathrm{Fano}} = \frac{1}{3}\sum_{p=1}^{7} \Pi_p = \frac{1}{3} \cdot 3I = I \quad \checkmark$$

### 5.3 Definition (Fano Predictive Channel)

$$\mathcal{P}_{\mathrm{Fano}}(\Gamma) := \sum_{p=1}^{7} L_p^{\mathrm{Fano}} \, \Gamma \, (L_p^{\mathrm{Fano}})^\dagger = \frac{1}{3}\sum_{p=1}^{7} \Pi_p \, \Gamma \, \Pi_p$$

---

## 6. Properties of the Fano Channel

### Theorem 10.1 (Fano Channel Preserves Coherences)

:::tip[Status: Theorem \[T\]]
For an arbitrary coherence matrix $\Gamma$:
:::

**(a)** Diagonal elements are preserved exactly:

$$[\mathcal{P}_{\mathrm{Fano}}(\Gamma)]_{ii} = \gamma_{ii}$$

**(b)** Off-diagonal elements (coherences) are preserved with a factor of $1/3$:

$$[\mathcal{P}_{\mathrm{Fano}}(\Gamma)]_{ij} = \frac{1}{3}\gamma_{ij} \quad \text{for all } i \neq j$$

**(c)** Phases of coherences are preserved exactly:

$$\arg([\mathcal{P}_{\mathrm{Fano}}(\Gamma)]_{ij}) = \arg(\gamma_{ij}) = \theta_{ij}$$

**Proof.**

**(a)** $[\sum_p \Pi_p \Gamma \Pi_p]_{ii} = \sum_{p:\, i \in \mathrm{line}_p} \gamma_{ii} = 3\gamma_{ii}$. With factor $1/3$: $\gamma_{ii}$. $\checkmark$

**(b)** In $\mathrm{PG}(2,2)$ any two points lie on exactly one line. For the pair $(i,j)$, $i \neq j$: exactly one line $p^*$ contains both points.

$$\left[\sum_p \Pi_p \Gamma \Pi_p\right]_{ij} = \sum_{p:\, i,j \in \mathrm{line}_p} \gamma_{ij} = 1 \cdot \gamma_{ij}$$

With factor $1/3$: $\gamma_{ij}/3$. $\checkmark$

**(c)** $\arg(\gamma_{ij}/3) = \arg(\gamma_{ij})$, since $1/3 > 0$. $\checkmark$ $\blacksquare$

### Theorem 10.2 (Canonical Form of $\varphi_{\mathrm{coh}}$)

:::tip[Status: Theorem \[T\]]
Canonical coherence-preserving self-modelling is determined by a two-component structure.
:::

$$\varphi_{\mathrm{coh}}(\Gamma) = k \cdot \left[\alpha \cdot \mathcal{P}_{\mathrm{base}}(\Gamma) + (1 - \alpha) \cdot \mathcal{P}_{\mathrm{Fano}}(\Gamma)\right] + (1 - k) \cdot \Gamma_{\mathrm{anchor}}$$

where:
- $\mathcal{P}_{\mathrm{base}}(\Gamma) = \sum_m P_m \Gamma P_m = \mathrm{diag}(\Gamma)$ — atomic channel (decohering observation)
- $\mathcal{P}_{\mathrm{Fano}}(\Gamma) = \frac{1}{3}\sum_p \Pi_p \Gamma \Pi_p$ — Fano channel
- $\alpha \in [0, 1]$ — **decoherence depth parameter** (balance between atomic and Fano observation)
- $k < 1$ — contraction parameter
- $\Gamma_{\mathrm{anchor}}$ — E-accented anchor

**CPTP verification:** For arbitrary $\alpha \in [0,1]$:

$$\varphi_{\mathrm{coh}} = k \cdot \mathcal{P}_\alpha + (1-k) \cdot \mathrm{const}$$

where $\mathcal{P}_\alpha = \alpha \mathcal{P}_{\mathrm{base}} + (1-\alpha) \mathcal{P}_{\mathrm{Fano}}$ is a convex combination of CPTP channels, hence CPTP. $\checkmark$

### Theorem 10.3 (Target Coherences of $\varphi_{\mathrm{coh}}$)

:::tip[Status: Theorem \[T\]]
For canonical $\varphi_{\mathrm{coh}}$ the target coherences are determined as follows.
:::

**(a)** Modulus of the target coherence:

$$|\gamma_{ij}^{\mathrm{target}}| = \left[\frac{k(1-\alpha)}{3}\right] \cdot |\gamma_{ij}| + (1-k) \cdot [\Gamma_{\mathrm{anchor}}]_{ij}$$

For a diagonal anchor ($[\Gamma_{\mathrm{anchor}}]_{ij} = 0$ for $i \neq j$):

$$|\gamma_{ij}^{\mathrm{target}}| = \frac{k(1-\alpha)}{3} \cdot |\gamma_{ij}|$$

**(b)** Target phase:

$$\theta_{ij}^{\mathrm{target}} = \theta_{ij} \quad \text{(phase is preserved!)}$$

**(c)** Target Gap:

$$\mathrm{Gap}^{\mathrm{target}}(i,j) = |\sin(\theta_{ij})| = \mathrm{Gap}(i,j) \quad \text{(Gap is preserved!)}$$

**Fundamental corollary.** Canonical $\varphi_{\mathrm{coh}}$ **does not tend to change the Gap** — it tends to reproduce the Gap with reduced amplitude. The target state does **not destroy** coherences, but scales them.

### Theorem 10.4 (Variational Determination of $\alpha^*$) — retracted [✗]

:::danger[Status: Retracted \[✗\] (2026-09-25)]
The theorem claimed that the Fano weight has a variational optimum $\alpha^* \approx 1 - 2/(7P)$ inside $(0,1)$. It is false: $S_{\mathrm{spec}}(\rho) + D_{KL}(\rho\|\Gamma) = -\mathrm{Tr}(\rho\log\Gamma)$ is linear in $\rho$, and with $\mathcal{P}_\alpha(\Gamma) = \tfrac13[(2+\alpha)\,\Delta\Gamma + (1-\alpha)\,\Gamma]$, $\Delta\Gamma := \mathcal{P}_{\mathrm{base}}(\Gamma)$, the functional is affine in $\alpha$:

$$\mathcal{F}(\alpha) = \mathcal{F}(0) + \tfrac{\alpha}{3}\left[D_{KL}(\Gamma\|\Delta\Gamma) + D_{KL}(\Delta\Gamma\|\Gamma)\right],$$

so its minimum on $[0,1]$ is $\alpha = 0$ for every non-diagonal $\Gamma$ (400 random states: the identity and a positive slope in 400 of 400). No variational $\alpha^*$ exists; the Fano weight $\alpha$ is a free parameter of $\varphi_{\mathrm{coh}}$ ([status registry](/docs/reference/status-registry), row 36). The statement and proof below are kept as the record of the retracted claim.
:::

$$\alpha^* = \arg\min_{\alpha \in [0,1]} \mathcal{F}[\mathcal{P}_\alpha; \Gamma] = \arg\min_{\alpha} \left[S_{\mathrm{spec}}(\mathcal{P}_\alpha(\Gamma)) + D_{KL}(\mathcal{P}_\alpha(\Gamma) \| \Gamma)\right]$$

**(a)** At $\alpha = 1$ (purely atomic): $\mathcal{P}_1 = \mathcal{P}_{\mathrm{base}}$, destroys all coherences. $D_{KL}$ is large (information about coherences is lost). $S_{\mathrm{spec}}$ is maximal (complete decoherence).

**(b)** At $\alpha = 0$ (purely Fano): $\mathcal{P}_0 = \mathcal{P}_{\mathrm{Fano}}$, preserves coherences with factor $1/3$. $D_{KL}$ is small (little information is lost). But $S_{\mathrm{spec}}$ is not minimal (the predictive model is less precise).

**(c)** The optimum $\alpha^* \in (0, 1)$ is a balance between predictive accuracy (atomic observation) and structure preservation (Fano observation).

**(d)** For a system with purity $P > P_{\mathrm{crit}}$:

$$\alpha^* \approx 1 - \frac{P_{\mathrm{crit}}}{P} = 1 - \frac{2}{7P}$$

At $P = 1$ (pure state): $\alpha^* \approx 5/7 \approx 0.71$ — significant Fano contribution.

At $P \to P_{\mathrm{crit}}$: $\alpha^* \to 0$ — almost entirely Fano (minimal destruction of coherences for survival).

**Proof.** Minimisation of $\mathcal{F}$ over $\alpha$ at fixed $P$ determines the balance: increasing $\alpha$ improves predictive accuracy ($S_{\mathrm{spec}}$ decreases), but increases coherence loss ($D_{KL}$ grows). The condition $P > P_{\mathrm{crit}}$ requires preserving a sufficient number of coherences, which bounds $\alpha$ from above. The optimum is found from $\partial \mathcal{F}/\partial \alpha = 0$. $\blacksquare$

**Where the proof fails.** It assumes that raising $\alpha$ lowers $S_{\mathrm{spec}}$ while raising $D_{KL}$, and solves $\partial\mathcal{F}/\partial\alpha = 0$. But $\partial\mathcal{F}/\partial\alpha$ is the constant $\tfrac13[D_{KL}(\Gamma\|\Delta\Gamma) + D_{KL}(\Delta\Gamma\|\Gamma)] \geq 0$, which vanishes only for diagonal $\Gamma$. Items (c)–(d), with $\alpha^* \approx 5/7$ at $P = 1$ and $\alpha^* \to 0$ at $P \to P_{\mathrm{crit}}$, are retracted [✗] with it.

### Theorem 10.5 (Explicit Coefficients of $\varphi_{\mathrm{coh}}$)

:::tip[Status: Theorem \[T\]]
The Kraus operators of canonical $\varphi_{\mathrm{coh}}$ take a specific form.
:::

**Atomic operators (7 in total):**

$$K_m^{(\mathrm{atom})} = \sqrt{\alpha k} \cdot |m\rangle\langle m|, \quad m = 1, \ldots, 7$$

**Fano operators (7 in total):**

$$K_p^{(\mathrm{Fano})} = \sqrt{(1-\alpha) k / 3} \cdot \Pi_p, \quad p = 1, \ldots, 7$$

**Anchor operators (49 in total),** with $\Gamma_{\mathrm{anchor}} = \sum_i \lambda_i |\psi_i\rangle\langle\psi_i|$:

$$K_{ij}^{(\mathrm{anch})} = \sqrt{(1-k)\,\lambda_i} \cdot |\psi_i\rangle\langle j|, \quad i, j = 1, \ldots, 7$$

**CPTP verification:**

$$\sum_{m=1}^{7} (K_m^{(\mathrm{atom})})^\dagger K_m^{(\mathrm{atom})} + \sum_{p=1}^{7} (K_p^{(\mathrm{Fano})})^\dagger K_p^{(\mathrm{Fano})} + \sum_{i,j=1}^{7} (K_{ij}^{(\mathrm{anch})})^\dagger K_{ij}^{(\mathrm{anch})}$$

First term: $\alpha k \sum_m |m\rangle\langle m| = \alpha k \cdot I$.

Second term: $(1-\alpha) k / 3 \cdot 3I = (1-\alpha) k \cdot I$ (every point lies on three lines).

Third term: $(1-k) \sum_{i,j} \lambda_i\, |j\rangle\langle j| = (1-k) \cdot I$.

**Total = $I$. $\checkmark$** The 63 operators reproduce $\varphi_{\mathrm{coh}}$ of Theorem 10.2 (numerically to $3\times10^{-16}$ on 50 random states).

:::note Corrected 2026-09-25 — the former Kraus set was not trace-preserving
The box printed $K_m^{(\mathrm{atom})} = \sqrt{\alpha^* k/7}\,|m\rangle\langle m|$, $K_p^{(\mathrm{Fano})} = \sqrt{(1-\alpha^*)k/3}\,\Pi_p$ and one anchor operator $K_0^{(\mathrm{anch})} = \sqrt{1-k}\,\Gamma_{\mathrm{anchor}}^{1/2}$, with "first term $\alpha^* k/7 \cdot 7I$" and "third term $(1-k)\cdot I$". Both steps are wrong: $\sum_m |m\rangle\langle m| = I$, not $7I$, so the atomic part got weight $\alpha k/7$; and $K_0^\dagger K_0 = (1-k)\,\Gamma_{\mathrm{anchor}} \neq (1-k)\,I$ — a single operator gives $\Gamma \mapsto (1-k)\,\Gamma_{\mathrm{anchor}}^{1/2}\,\Gamma\,\Gamma_{\mathrm{anchor}}^{1/2}$, not the replacement $\Gamma \mapsto (1-k)\,\Gamma_{\mathrm{anchor}}$. For $\alpha = 0.4$, $k = 0.8$ the printed set misses $I$ by $1.18$ in Frobenius norm. The printed coefficient $c_{mm} = \alpha^* k$ was wrong for the same reason, and $\alpha^*$ itself is retracted (Theorem 10.4).
:::

**Corollary.** In $\varphi_{\mathrm{coh}}(\Gamma)$ each entry $\gamma_{mn}$ is multiplied by

$$c_{mn} = \begin{cases} k & \text{for } m = n \text{ (both channels keep the diagonal)} \\ (1-\alpha) k / 3 & \text{for } m \neq n \end{cases}$$

and the anchor adds $(1-k)\,[\Gamma_{\mathrm{anchor}}]_{mn}$. Every pair $(m,n)$ lies on exactly one Fano line, so the former third case "$0$ for $(m,n)$ not on a common Fano line" is empty.

The coefficients are fully determined by:
- The Fano structure $\mathrm{PG}(2,2)$ (algebraic geometry)
- ~~The variational principle ($\alpha^*$ via $P$ and $P_{\mathrm{crit}}$)~~ — retracted with Theorem 10.4: the Fano weight $\alpha$ is a free parameter
- The contraction parameter $k$

---

## 7. $G_2$-Covariance

### Theorem 11.1 (Atomic Dissipator is NOT $G_2$-Covariant)

:::danger[Status: Theorem — negative result \[T\]]
The dissipative channel with atomic Lindblad operators $L_k = |k\rangle\langle k|$ is **not** $G_2$-covariant.
:::

$$\exists g \in G_2: \quad \mathcal{D}_{\mathrm{atom}}[g\Gamma g^\dagger] \neq g \, \mathcal{D}_{\mathrm{atom}}[\Gamma] \, g^\dagger$$

**Proof.**

**(a)** Atomic dissipator:

$$\mathcal{D}_{\mathrm{atom}}[\Gamma] = \sum_{k=1}^{7} L_k \Gamma L_k^\dagger - \Gamma = \sum_k |k\rangle\langle k| \Gamma |k\rangle\langle k| - \Gamma = \mathrm{diag}(\Gamma) - \Gamma$$

**(b)** Action of $G_2$: for $g \in G_2$, $g\Gamma g^\dagger \mapsto D(g)\Gamma D(g)^\dagger$, where $D(g)$ is the 7-dimensional representation of $G_2$.

**(c)** We check covariance:

$$\mathcal{D}_{\mathrm{atom}}[g\Gamma g^\dagger] = \mathrm{diag}(g\Gamma g^\dagger) - g\Gamma g^\dagger$$

$$g \, \mathcal{D}_{\mathrm{atom}}[\Gamma] \, g^\dagger = g[\mathrm{diag}(\Gamma) - \Gamma]g^\dagger = g \cdot \mathrm{diag}(\Gamma) \cdot g^\dagger - g\Gamma g^\dagger$$

**(d)** Equality requires:

$$\mathrm{diag}(g\Gamma g^\dagger) = g \cdot \mathrm{diag}(\Gamma) \cdot g^\dagger \quad \forall \Gamma$$

This means: 'diagonal of the transformed matrix = transform of the diagonal'. This holds **only** for diagonal $g$ (permutations + phases), but NOT for general $g \in G_2$.

**(e)** Counterexample: take $g$ = rotation by angle $\pi/4$ in the plane $(e_1, e_2)$. For a matrix $\Gamma$ with $\gamma_{12} \neq 0$:

$$\mathrm{diag}(g\Gamma g^\dagger) \neq g \cdot \mathrm{diag}(\Gamma) \cdot g^\dagger$$

since the left-hand side annihilates the coherence $\gamma_{12}$ in the rotated basis, while the right-hand side does not. $\blacksquare$

### Theorem 11.2 (Covariance group of the Fano dissipator)

:::tip[Status: Theorem \[T\]]
By the Fano–atomic proportionality $\mathcal{D}_{\mathrm{Fano}} = \tfrac23\mathcal{D}_{\mathrm{atom}}$, the Fano dissipator is covariant under the finite octonionic frame group $\Gamma_{\!\text{oct}}\subset G_2$ — the signed permutation matrices in $G_2$, order $1344=2^3\cdot168$, acting on the lines through $\mathrm{Aut}(PG(2,2))\cong PSL(2,7)$ (order 168); the earlier "$\Gamma_{\!\text{oct}}=\mathrm{Aut}(PG(2,2))\cong PSL(2,7)$" confused the group with its image — and **not** under the full continuous $G_2$. The canonical fully $G_2$-covariant dissipator is $\mathcal{D}_{G_2}$ (structure-constant construction, $(A_a)_{bc}=\varphi_{abc}/\sqrt6$). Full treatment: [Fano channel §5](/docs/proofs/gap/fano-channel#g2-ковариантность).
:::

$$\forall g \in \Gamma_{\!\text{oct}}: \quad \mathcal{D}_{\mathrm{Fano}}[g\Gamma g^\dagger] = g \, \mathcal{D}_{\mathrm{Fano}}[\Gamma] \, g^\dagger$$

**Proof.**

**(a)** For $g\in\Gamma_{\!\text{oct}}$, $g$ permutes the seven coordinate Fano lines: there is a permutation $\sigma_g$ on $\{1,\ldots,7\}$ with

$$g\, \Pi_p\, g^\dagger = \Pi_{\sigma_g(p)}.$$

A generic $g\in G_2$ does **not** do this: $\mathbb{C}^7$ is an irreducible $G_2$-module (Schur), so no coordinate 3-subspace $\mathrm{span}(\text{line }p)$ is $G_2$-invariant. Hence the covariance below is exact only for the finite subgroup $\Gamma_{\!\text{oct}}$.

**(b)** Fano dissipator:

$$\mathcal{D}_{\mathrm{Fano}}[\Gamma] = \frac{1}{3}\sum_{p=1}^{7} \Pi_p \Gamma \Pi_p - \Gamma$$

**(c)** Substituting $g\Gamma g^\dagger$:

$$\mathcal{D}_{\mathrm{Fano}}[g\Gamma g^\dagger] = \frac{1}{3}\sum_p \Pi_p (g\Gamma g^\dagger) \Pi_p - g\Gamma g^\dagger$$

**(d)** Using $g^\dagger \Pi_p g = \Pi_{\sigma_g^{-1}(p)}$ (from (a)):

$$= \frac{1}{3}\sum_p \Pi_p g \Gamma g^\dagger \Pi_p = \frac{1}{3}\sum_p g (g^\dagger \Pi_p g) \Gamma (g^\dagger \Pi_p g) g^\dagger$$

$$= \frac{1}{3}g\left[\sum_p \Pi_{\sigma_g^{-1}(p)} \Gamma \Pi_{\sigma_g^{-1}(p)}\right]g^\dagger$$

Since $\sigma_g$ is a permutation: $\sum_p \Pi_{\sigma_g^{-1}(p)} = \sum_q \Pi_q$ (reindexing). Therefore:

$$= g \left[\frac{1}{3}\sum_q \Pi_q \Gamma \Pi_q\right] g^\dagger = g \, \mathcal{P}_{\mathrm{Fano}}(\Gamma) \, g^\dagger$$

And:

$$\mathcal{D}_{\mathrm{Fano}}[g\Gamma g^\dagger] = g \, \mathcal{P}_{\mathrm{Fano}}(\Gamma) \, g^\dagger - g\Gamma g^\dagger = g[\mathcal{P}_{\mathrm{Fano}}(\Gamma) - \Gamma]g^\dagger = g \, \mathcal{D}_{\mathrm{Fano}}[\Gamma] \, g^\dagger$$

$\blacksquare$

### Theorem 11.3 (Degree of $G_2$ Breaking is Determined by $\alpha$)

:::tip[Status: Theorem \[T\]]
For canonical $\varphi_{\mathrm{coh}}$ with parameter $\alpha$, the degree of $G_2$-covariance is determined as follows.
:::

**(a)** At $\alpha = 0$ (purely Fano): covariance under the finite frame group $\Gamma_{\!\text{oct}}$ only — $\mathcal{D}_{\mathrm{Fano}} = \tfrac23\mathcal{D}_{\mathrm{atom}}$ has the same symmetry group as the atomic dissipator (Theorem 11.2, [Theorem 5.1b](/docs/proofs/gap/fano-channel#g2-ковариантность)). No $48 \to 34$ gauge reduction is realised at any $\alpha$ ([frame decision D-0910](/docs/proofs/categorical/uniqueness-theorem#g2-ригидность)).

**(b)** At $\alpha = 1$ (purely atomic): $G_2$ is **fully broken**. No gauge reduction.

**(c)** For intermediate $\alpha \in (0, 1)$: **partial** $G_2$-covariance. Mixed channel:

$$\mathcal{P}_\alpha = \alpha \, \mathcal{P}_{\mathrm{base}} + (1 - \alpha) \, \mathcal{P}_{\mathrm{Fano}}$$

Measure of $G_2$-symmetry breaking:

$$\Delta_{G_2}(\alpha) := \sup_{g \in G_2} \|\mathcal{P}_\alpha \circ \mathrm{Ad}_g - \mathrm{Ad}_g \circ \mathcal{P}_\alpha\|_{\mathrm{op}}$$

where $\mathrm{Ad}_g(\Gamma) = g\Gamma g^\dagger$.

**(d)** $\Delta_{G_2}(\alpha)$ increases monotonically with $\alpha$:

$$\Delta_{G_2}(0) = \tfrac23\Delta_{\max} > 0, \quad \Delta_{G_2}(1) = \Delta_{\max}$$

**(e)** For every value of the free Fano weight $\alpha$:

$$\Delta_{G_2}(\alpha) = \tfrac{2+\alpha}{3} \cdot \Delta_{\max} \geq \tfrac23\,\Delta_{\max}$$

(Until 2026-09-25 this item read "at optimal $\alpha^* \approx 1 - 2/(7P)$: $\Delta_{G_2}(\alpha^*) = \tfrac{2+\alpha^*}{3}\Delta_{\max}$"; the variational $\alpha^*$ is retracted, Theorem 10.4, so the purity $P$ does not fix the breaking.)

**Proof.** (a)–(b): direct consequence of Theorems 11.1 and 11.2. (c)–(e): $\mathcal{P}_\alpha$ is a convex combination of two channels with the same finite covariance group $\Gamma_{\!\text{oct}}$; since $\mathcal{D}_\alpha = \tfrac{2+\alpha}{3}\mathcal{D}_{\mathrm{atom}}$ ([Lindblad operators](/docs/core/operators/lindblad-operators#g2-ковариантность)), the breaking measure is $\Delta_{G_2}(\alpha) = \tfrac{2+\alpha}{3}\Delta_{\max}$ — affine in $\alpha$ and strictly positive on $[0,1]$. $\blacksquare$

:::warning Limits of $G_2$-Covariance
- Fano dissipator $\mathcal{D}_{\text{Fano}} = \tfrac23\mathcal{D}_{\text{atom}}$: covariant under the frame group $\Gamma_{\!\text{oct}}$, **not** full $G_2$ **[T]** (T-11.2)
- Atomic dissipator $\mathcal{D}_{\text{atom}}$: **NOT** $G_2$-covariant **[T]** (T-11.1)
- Canonical $G_2$-covariant dissipator $\mathcal{D}_{G_2}$ (structure constants $\varphi_{abc}$) **[T]**
- Full dynamics $\mathcal{L}_\Omega = \mathcal{D}_{\text{atom}} + \mathcal{D}_{\text{Fano}} + \mathcal{R}$: **not** $G_2$-covariant at any $\alpha$ — **[T]** (both dissipators are only $\Gamma_{\!\text{oct}}$-covariant, Theorem 5.1b; $\mathcal{R}$ references the O, E, U axes; [frame decision D-0910](/docs/proofs/categorical/uniqueness-theorem#g2-ригидность))
:::

### Theorem 11.4 (Modified Gauge Reduction) — retracted [✗]

:::danger[Status: Retracted \[✗\]]
Superseded by the frame decision D-0910: the parameter space of Gap profiles is **not** reduced by $G_2$ at any $\alpha$; the interpolation below is retained only as a record of the retracted claim. (This box carried the header "Theorem [T]" until 2026-09-25 while stating the retraction.)
:::

**(a)–(c) Retracted (D-0910).** Earlier drafts interpolated "$34$ parameters at $\alpha = 0$, $34 + 14\alpha^*$ at optimal $\alpha^*$, $48$ at $\alpha = 1$" (for $P \approx 0.5$: $\approx 40$). The premise — a $G_2$-covariant Fano channel at $\alpha = 0$ — is false (Theorem 11.2): the pinching dynamics is only $\Gamma_{\!\text{oct}}$-covariant for every $\alpha \in [0,1]$, so the physical parameter space of Gap profiles is the full 48-dimensional $\mathcal{D}(\mathbb{C}^7)$ modulo a finite group at every $\alpha$. The number 34 survives only as the count of kinematic $G_2$-invariants ([uniqueness theorem, Corollary 1](/docs/proofs/categorical/uniqueness-theorem#физические-состояния)). The "optimal $\alpha^*$" of that interpolation is retracted as well (Theorem 10.4).

~~**For a highly coherent system** with $P \approx 0.8$: $\alpha^* \approx 0.64$, number of parameters $\approx 34 + 9 = 43$. The reduction is even more moderate.~~ Retracted [✗] with (a)–(c): the count is 48 at every $\alpha$.

**Interpretation (revised).** Self-observation (nonzero $\alpha$) increases the measure of $G_2$ breaking, $\Delta_{G_2}(\alpha)=\tfrac{2+\alpha}{3}\Delta_{\max}$ (Theorem 11.3). The number of parameters does not change with $\alpha$: it is 48 throughout. The former reading "the deeper the self-knowledge, the more parameters are needed — the price of self-knowledge" is retracted [✗] with (a)–(c).

### Updated Diagnostic Protocol

After the frame decision D-0910:

| Mode | Number of parameters | Protocol |
|-------|-----------------|----------|
| every $\alpha\in[0,1]$ (L0 to L4) | 48 | Full tomography: all 48 parameters, read in the pinned frame |

The former rows "$\alpha = 0$: 34 (full $G_2$), minimal tomography with $G_2$ relations" and "$\alpha^* \approx 0.4$: $\sim$40, partial $G_2$ relations" are retracted [✗] (D-0910): the dynamics is covariant only under $\Gamma_{\!\text{oct}}$ at every $\alpha$, so no $G_2$ relation reduces the count; the $\alpha^*$ of the second row is retracted as well (Theorem 10.4).

---

## 8. Unified Theorem of Self-Observation and Gap

### Theorem 12.1 (Fano-Coherent Self-Modelling)

:::tip[Status: Theorem \[T\]]
Canonical coherence-preserving self-modelling for UHM theory is determined up to two free parameters, the contraction $k$ and the Fano weight $\alpha$. (Until 2026-09-25 the box said "uniquely, up to the contraction parameter $k$"; that relied on the variational $\alpha^*$ of Theorem 10.4, which is retracted.)
:::

**(a)** **Algebraic structure:** The Fano plane $\mathrm{PG}(2,2)$ determines the composite atoms of the classifier $\Omega$, generating the Fano–Lindblad operators $L_p^{\mathrm{Fano}}$.

**(b)** ~~**Variational principle:** The balance of atomic and Fano observation $\alpha^*$ minimises the functional $\mathcal{F} = S_{\mathrm{spec}} + D_{KL}$.~~ Retracted [✗] (Theorem 10.4): $\mathcal{F}$ is affine in $\alpha$ and minimal at $\alpha = 0$; the balance $\alpha$ is a free parameter.

**(c)** **Phase properties:** Canonical $\varphi_{\mathrm{coh}}$ **preserves** the phases of coherences. The target Gap coincides with the current Gap (amplitude scaling without phase distortion).

**(d)** **Symmetry:** $G_2$-covariance is broken at every $\alpha$; the degree of breaking is $\Delta_{G_2} = \tfrac{2+\alpha}{3}\,\Delta_{\max}$ (Theorem 11.3(e)) for the free Fano weight $\alpha$; the earlier dependence on the purity $P$ through $\alpha^*$ is retracted with Theorem 10.4. The earlier value $\alpha^*\cdot\Delta_{\max}$, which vanished at $\alpha^*=0$, is retracted [✗]: $\mathcal{P}_{\mathrm{Fano}}=\tfrac13\,\mathrm{id}+\tfrac23\mathcal{P}_{\mathrm{base}}$, so even the pure Fano channel breaks $G_2$ by $\tfrac23\Delta_{\max}$.

**(e)** **Stationary Gap:** Substituting into the stationary equation with $\theta_{ij}^{\mathrm{target}} = \theta_{ij}$ gives:

$$\mathrm{Gap}^{(\infty)}(i,j) = \left|\sin\left(\theta_{ij} - \arctan\left(\frac{\Delta\omega_{ij}}{\Gamma_2 + \kappa}\right)\right)\right|$$

The stationary Gap is **shifted** relative to the current one by the angle $\arctan(\Delta\omega/(\Gamma_2 + \kappa))$ — even with phase-preserving $\varphi_{\mathrm{coh}}$, unitary rotation creates a difference between the target and the stationary.


---

**Related documents:**
- [Standard Model from G₂](/docs/physics/gauge-symmetry/standard-model)
- [Fano Selection Rules](/docs/physics/gauge-symmetry/fano-selection-rules)
- [G₂-Noether Charges](/docs/physics/gauge-symmetry/noether-charges)
- [Confinement](/docs/physics/gauge-symmetry/confinement)
