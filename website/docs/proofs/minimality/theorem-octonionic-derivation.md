---
slug: /proofs/minimality/theorem-octonionic-derivation
sidebar_position: 2
title: "Octonionic Structure: Conditional Derivations"
description: "Exact channel and orientation theorems, with explicit dimension and instrument assumptions"
---

# Octonionic structure: conditional derivations

The unconditional bridge AP+PH+QG+V ⇒ octonions is withdrawn [✗] (2026-10-03). Several steps used false implications. The substantial pure mathematics and canonical-orientation theorem survive; their application now declares its inputs. Canonical orientation solves the orientation problem **after a Fano plane is given**, not the selection of that plane or of seven physical coordinates.

## §1. Pure Mathematics [T] {#чистая-математика}

### 1.1 Hurwitz Theorem (1898) [T] {#теорема-гурвица}

**Theorem (Hurwitz).** Normed division algebras over $\mathbb{R}$ exist only in dimensions 1, 2, 4, and 8:

$$
\mathbb{R}, \quad \mathbb{C}, \quad \mathbb{H}, \quad \mathbb{O}
$$

No others exist.

**Proof:** Classical — via quadratic forms and the Hurwitz identity. An algebra $\mathcal{A}$ with norm $|ab| = |a||b|$ requires that $n = \dim(\mathcal{A})$ satisfy the sum-of-squares identity. By the Hurwitz theorem this is only possible for $n \in \{1, 2, 4, 8\}$.

### 1.2 Adams Theorem (1960) [T] {#теорема-адамса}

**Theorem (Adams).** The sphere $S^{n-1}$ admits an $H$-space structure (continuous multiplication with a unit) if and only if $n \in \{1, 2, 4, 8\}$.

**Related statement:** Parallelizable spheres are only $S^0, S^1, S^3, S^7$ (Bott–Milnor and Kervaire 1958; also a consequence of Adams's work). These are the unit spheres $S^{n-1}$ of the four normed division algebras, $n \in \{1, 2, 4, 8\}$.

**Corollary — corrected (2026-09-25).** The unit sphere of $\mathcal{A}$ itself, $S^{n-1}$, is parallelizable exactly for $n \in \{1, 2, 4, 8\}$. The unit sphere of $\text{Im}(\mathcal{A})$, $S^{n-2}$, is **not**: for $n=4$ and $n=8$ it is $S^2$ and $S^6$, and neither is parallelizable (only $S^0, S^1, S^3, S^7$ are; $S^6$ carries an almost complex structure from $\mathbb{O}$, not a trivialisation of its tangent bundle). The former corollary — "the imaginary unit sphere $S^{n-2}$ is parallelizable only for $n \in \{1,2,4,8\}$" — is retracted [✗].

### 1.3 Cayley–Dickson Construction [T] {#кэли-диксон}

Division algebras form a chain of doublings:

$$
\mathbb{R} \xrightarrow{\text{CD}} \mathbb{C} \xrightarrow{\text{CD}} \mathbb{H} \xrightarrow{\text{CD}} \mathbb{O} \xrightarrow{\text{CD}} \mathbb{S}
$$

| Algebra | dim | Commutativity | Associativity | Alternativity | Divisibility |
|---|---|---|---|---|---|
| $\mathbb{R}$ | 1 | + | + | + | + |
| $\mathbb{C}$ | 2 | + | + | + | + |
| $\mathbb{H}$ | 4 | — | + | + | + |
| $\mathbb{O}$ | 8 | — | — | + | + |
| $\mathbb{S}$ | 16 | — | — | — | — |

**Cayley–Dickson boundary [T]:** At each step an algebraic property is lost. $\mathbb{O}$ is the last division algebra. Sedenions $\mathbb{S}$ and all further doublings contain zero divisors.

### 1.4 Octonions $\mathbb{O}$ [T] {#октонионы}

**Definition.** Octonions are the 8-dimensional normed division algebra over $\mathbb{R}$:

$$
\mathbb{O} = \{a_0 + a_1 e_1 + a_2 e_2 + \cdots + a_7 e_7 \mid a_i \in \mathbb{R}\}
$$

where $e_1, \ldots, e_7$ are imaginary units.

**Multiplication table** is defined by 7 associative triples (cycles of the Fano plane):

$$
e_i \cdot e_j = -\delta_{ij} + \varepsilon_{ijk} e_k
$$

where $\varepsilon_{ijk}$ is the fully antisymmetric tensor, nonzero on the 7 Fano triples.

**Key properties:**
- **Non-associativity:** $(e_i e_j) e_k \neq e_i (e_j e_k)$ in general
- **Alternativity:** $x(xy) = x^2 y$ and $(xy)y = x y^2$ (Artin's theorem)
- **Norm:** $|xy| = |x||y|$ (normed division algebra)

### 1.5 Fano Plane PG(2,2) [T] {#плоскость-фано}

**Definition.** The Fano plane is the minimal finite projective plane with 7 points and 7 lines.

```
        e₁
       / \
      /   \
    e₃—--e₂
    / \ ○ / \
   /   \ /   \
  e₅—e₆—e₄
       |
       e₇
```

**Properties [T]:**
- 7 points, 7 lines
- Each line contains 3 points
- Each point lies on 3 lines
- Through any 2 points there passes exactly 1 line
- Automorphism group: $\text{Aut}(\text{PG}(2,2)) = GL(3, \mathbb{F}_2) \cong PSL(2,7)$, order 168

**Connection with $\mathbb{O}$:** The 7 triples (lines) of the Fano plane define the multiplication table of the imaginary units of the octonions. Each line $(e_i, e_j, e_k)$ specifies the rule: $e_i \cdot e_j = e_k$ (with orientation taken into account).

### 1.6 Group $G_2$ [T] {#группа-g2}

**Theorem.** The automorphism group of the octonion algebra:

$$
\text{Aut}(\mathbb{O}) = G_2
$$

$G_2$ is the minimal exceptional Lie group, 14-dimensional, of rank 2.

**Properties of $G_2$ [T]:**
- $\dim(G_2) = 14$
- $\text{rank}(G_2) = 2$
- $G_2 \subset SO(7)$ — subgroup of rotations in $\text{Im}(\mathbb{O}) \cong \mathbb{R}^7$
- $G_2$ preserves the multiplication structure of the octonions and the Fano plane
- $G_2$-manifolds admit a metric with $G_2$ holonomy (the unique exceptional holonomy by Berger's classification)

### 1.7 Hamming Code H(7,4) [T] {#код-хэмминга}

**Theorem.** The Hamming code $H(7,4)$ is a perfect linear binary code:
- 7 bits, 4 information + 3 check
- Corrects 1 error
- The Hamming bound is achieved (perfect code)

**Connection with the Fano plane [T]:** The parity-check matrix of $H(7,4)$ is defined by the 7 nonzero columns of $\mathbb{F}_2^3$, which correspond to the 7 points of the Fano plane.

**Structure 4+3:** Information part (4 bits) + check part (3 bits) = 7 bits.

### 1.8 Artin's Theorem [T] {#теорема-артина}

**Theorem (Artin).** Any two elements of an alternative algebra generate an associative subalgebra.

**Corollary for $\mathbb{O}$:** The non-associativity of octonions is **minimal**: it manifests only when three or more elements interact. Any pair of elements behaves associatively.

---

## Algebraic premises {#постулаты}

Assume a finite-dimensional real **unital normed division algebra** with multiplicative positive-definite norm (P1) and nonassociativity (P2). Hurwitz then gives $\mathbb O$ and its imaginary dimension seven [T at these inputs]. Arbitrary real division algebras without a multiplicative norm are outside this theorem. Neither density matrices nor autopoiesis supplies P1/P2.

The [minimality page](/docs/proofs/minimality/theorem-minimality-7) gives distinct conditional lower bounds, using perfect binary diagnosability or a faithful representation of a selected algebra. The length-15 Hamming code is perfect but does not produce a normed 16-dimensional division algebra. Thus perfect diagnosability alone is not equivalent to octonionic multiplication.

## Valid state and channel statements {#цепочка-t15}

For $\rho\in D_N$, $P=\operatorname{Tr}\rho^2$, $d=\sum_i\rho_{ii}^2$, $\Phi=P/d-1$,

$$
P=1/N+\|\rho-I/N\|_F^2,\qquad\Phi\le NP-1.
$$

The chosen structural-majority rule gives $P>2/N$. It does not imply $\Phi\ge1$: a diagonal pure state is a counterexample. A small coherent perturbation of that state gives $P>2/N$ and $0<\Phi<1$, so even adding nonzero coherences does not repair the old T5.

Rank-one states do not have zero variance for every observable: $|0\rangle$ has variance one for a Pauli $X$ observable. In $\mathbb C^7$ a named $E$ basis vector is not a nontrivial tensor subsystem. Experiential reduction must use a declared extension, as in the [hierarchy](/docs/consciousness/hierarchy/interiority-hierarchy).

A fixed point of a continuous self-model follows from compact convexity and Brouwer, rather than from the word AP. A nonunital coherent anchor can restore off-diagonal entries even with atomic dephasing ($c=0$). Consequently the old universal necessity of $c>0$ is withdrawn. Particular dissipative/regenerative balances require their actual anchor and rate regime.

## Designs and their channels {#шаг-t10}

Given a $(v,k,\lambda)$-BIBD with replication $r$, define the **chosen** sharp instrument $K_B=\Pi_B/\sqrt r$. Then

$$
\sum_BK_B^\dagger K_B=I,\qquad
T_c(\rho)=\sum_BK_B\rho K_B^\dagger=c\rho+(1-c)\operatorname{diag}\rho,
\quad c=\lambda/r=(k-1)/(v-1).
$$

This exact channel depends on $v,k$, not on $\lambda$ or the particular design [T]. The instrument, including its recorded outcomes, contains extra information that the unrecorded channel discards.

**Restricted optimum [T].** For nontrivial BIBD$(7,k,1)$, $k\in\{2,3\}$. The Fano design ($k=3,b=7,c=1/3$) preserves more coherence and uses fewer instrument operators than the pair design ($k=2,b=21,c=1/6$). This is an optimum in the stated class, not over all channels. The complement design $(7,4,2)$ gives $c=1/2$ and the six-point design $(7,6,5)$ gives $c=5/6$; both also have seven sharp Kraus operators. Thus neither sharp minimality nor primitivity alone forces $c=1/3$ or $\lambda=1$.

Primitivity does not mean a simple nonzero spectrum. The depolarizing generator $\rho\mapsto I\operatorname{Tr}\rho/7-\rho$ is primitive and has eigenvalue $-1$ with multiplicity 48. Duplicating every Kraus or Lindblad operator with coefficient $1/\sqrt2$ leaves the channel or generator unchanged. Repeated blocks cannot be ruled out by an invented spectral-degeneracy condition.

## Sharp minimal instruments [T] {#шаг-t11}

For $0\le c<1$, the Choi matrix of $T_c$ is supported on $\operatorname{span}\{|ii\rangle\}$ and has restriction

$$
C=(1-c)I_7+cJ_7.
$$

Its eigenvalues are $1+6c$ and $1-c$ (multiplicity six), so its rank is seven. The Choi matrix is $\sum_a|K_a\rangle\rangle\langle\langle K_a|$, not the Liouville matrix $\sum_aK_a\otimes\bar K_a$.

For the **specified channel** $T_{1/3}$, a representation with seven Kraus operators each proportional to a projector is necessarily a Fano-line instrument. No rank or equal-weight premise is needed. Let $N$ be its incidence matrix and $X$ its positive weight diagonal. Since $NXN^{\mathsf T}=C$ and $N$ is invertible,

$$
X^{-1}=N^{\mathsf T}C^{-1}N,\quad C^{-1}=\tfrac32(I-J/9),\quad
|S\cap T|=|S||T|/9\quad(S\ne T).
$$

Every support size is a multiple of three: otherwise intersection integrality would force the other six sizes to be at least nine. Thus sizes are three or six; the diagonal identity gives all weights $1/3$. The trace identity $\sum_S|S|/3=7$ forces all sizes three. Off-diagonal channel entries give pair multiplicity one. This is BIBD$(7,3,1)$, the Fano plane, with 30 labelled realizations. Conversely each realizes $T_{1/3}$. See the [full instrument theorem](/docs/core/operators/lindblad-operators#t13-sharp).

Choosing seven physical coordinates, this attenuation, sharpness and minimality supplies the Fano design. Selecting a fixed octonionic frame group additionally selects one of the 30 labelled instruments; it must not then be used as an independent proof that the octonionic structure had no inputs.

## Coding route {#шаг-t8}

For a chosen binary length-seven code with minimum distance three and perfect radius-one decoding, the parity-check columns are the seven nonzero elements of $\mathbb F_2^3$. Its weight-three codewords are the triples $\{x,y,x+y\}$, the Fano lines. The perfect-decoding premise is not a consequence of an arbitrary quantum self-model or matrix purity. Generic CPTP processes are not binary single-fault codes.

## Canonical orientation {#шаг-t15}

Given the Fano plane and the premise that its orientation **class** is selected naturally under every collineation, the following theorem yields the octonionic class. It does not select a particular signed basis or prove an empirical identification.

#### Theorem T15-canon: the canonical orientation of the Fano plane is octonionic [T] {#каноническая-ориентация}

*The canonicity premise is explicit. The finite classifications are independently checked by the orientation tests in `check_core_numbers.py`.*

**Setting.** An *orientation* $s$ of the Fano plane $D = \mathrm{PG}(2,2)$ is a cyclic order on each of its seven lines. It defines the algebra $\mathcal{A}_s = \mathrm{span}_{\mathbb{R}}\{1, e_1, \dots, e_7\}$ with $e_i^2 = -1$ and $e_i e_j = -e_j e_i = e_k$ for $(i, j, k)$ in the cyclic order of an oriented line. A *sign change* $e_p \mapsto -e_p$ is an isomorphism $\mathcal{A}_s \cong \mathcal{A}_{s'}$, where $s'$ reverses the three lines through $p$; the $2^7$ sign changes act on the $2^7 = 128$ orientations with a kernel of order 8 (the empty set and the seven complements of lines, which meet every line in an even number of points), so the *gauge classes* have 16 elements each and there are 8 of them. The collineation group $\mathrm{Aut}(D) \cong GL(3, \mathbb{F}_2)$, of order 168, permutes the classes.

:::tip Theorem T15-canon [T]
1. Exactly one gauge class is fixed by every collineation of $D$; the other seven form a single orbit, and each of them is fixed only by the stabiliser of one line (order 24).
2. The fixed class consists precisely of the 16 orientations for which $\mathcal{A}_s$ is normed (equivalently alternative), i.e. $\mathcal{A}_s \cong \mathbb{O}$.
3. The fixed class is also characterised by each of the following, and the other seven classes fail each of them:
   - (no associating triple) no three units $e_a, e_b, e_c$ on non-collinear points associate; in every other class 96 of the 168 ordered non-collinear triples do;
   - (definite 3-form) the 3-form $\varphi_s = \sum_{\text{lines}} \pm\, e^{ijk}$ has a definite Bryant metric, $(x \lrcorner \varphi)\wedge(y \lrcorner \varphi)\wedge\varphi \propto \delta(x,y)\,\mathrm{vol}$, signature $(7,0)$; in every other class the signature is $(4,3)$, the split form, with the three negative directions on the distinguished line;
   - (symmetric frame) the signed permutations of $e_1, \dots, e_7$ that are automorphisms of $\mathcal{A}_s$ form a group of order $1344$ mapping onto $GL(3, \mathbb{F}_2)$; in every other class the group has order $192$ and maps onto a line stabiliser.
4. Consequently, a rule that attaches to a Fano plane an orientation class *of that plane*, using nothing but the plane — so that isomorphic planes receive corresponding classes — attaches the octonionic class. Every other class can be placed on the seven points only by choosing a line.
:::

**Proof.** *Invariants.* For a point $p$ let $\chi_p(s)$ be the product of the signs of the four lines that miss $p$. A sign change at $q \neq p$ reverses the three lines through $q$, exactly two of which miss $p$; at $q = p$ it reverses none of them. So the seven $\chi_p$ are gauge invariants. In coordinates the class of $s$ is its image in the cokernel of the point–line incidence map $\mathbb{F}_2^7 \to \mathbb{F}_2^7$, whose image is the $[7,4]$ Hamming code; the cokernel is $\mathbb{F}_2^3$, which gives the 8 classes.

*Associators.* Label the points by the non-zero vectors of $\mathbb{F}_2^3$, lines being $\{x, y, x+y\}$. For independent $a, b, c$ the two products $(e_a e_b) e_c$ and $e_a (e_b e_c)$ are $\pm e_{a+b+c}$, and their ratio is the product of the signs of the lines $\{a, b, a{+}b\}$, $\{b, c, b{+}c\}$, $\{a{+}b, c, a{+}b{+}c\}$, $\{a, b{+}c, a{+}b{+}c\}$ times a sign fixed by the combinatorics. These four lines are exactly the four lines that miss the point $a + c$, so whether the triple associates is decided by $\chi_{a+c}(s)$.

*Item 1.* $\mathbb{O}$ has signed-permutation automorphisms covering every collineation (the frame group $\Gamma_{\!\text{oct}}$ of order 1344 maps onto $GL(3,\mathbb{F}_2)$), so the octonionic class is fixed. If two classes $c \neq c'$ were fixed, their difference would be a non-zero vector of the cokernel $\mathbb{F}_2^3$ fixed by $GL(3,\mathbb{F}_2)$; the group acts on it by its natural three-dimensional representation (or its dual), which fixes only $0$. So the fixed class is unique. The seven remaining classes differ from it by the seven non-zero vectors of $\mathbb{F}_2^3$, on which $GL(3,\mathbb{F}_2)$ acts transitively with stabilisers of order 24.

*Items 2–3* are finite statements about 128 orientations and 168 collineations and are verified exhaustively (`test_octonionic_orientation_is_the_unique_collineation_invariant_class`, together with `test_only_16_of_128_fano_orientations_are_normed`): the fixed class equals the set of normed orientations; its units associate on 0 of the 168 ordered non-collinear triples against 96 for every other class; the Bryant form is diagonal in the basis with signature $(7,0)$ against $(4,3)$; the automorphism groups have orders 1344 and 192.

*Item 4.* A rule that uses nothing but the plane is equivariant under isomorphisms of planes; applied to an automorphism $g$ of $D$, it gives $\mathrm{rule}(D) = g_*\,\mathrm{rule}(D)$ up to gauge, so the class it attaches is fixed by $\mathrm{Aut}(D)$, and by item 1 it is the octonionic class. $\blacksquare$

**Scope.** The theorem applies to a given Fano plane. The other seven gauge classes require a distinguished line. Selecting the collineation-invariant class is additional canonicity data; it does not restore the withdrawn upstream AP→Fano proof.

## Research tasks {#открытые-проблемы}

Physical selection of the algebra, dimension, instrument and observation model remains to be justified independently. A derivation of matter or spacetime must also retain its explicit (Mod)/(Cl₀)/(P) bridges. Group-theoretic compatibility is evidence of compatibility, not an observation law.

Primary source: John Baez, [The Octonions](https://arxiv.org/abs/math/0105155). The channel identities and finite orientation classifications have reproducible checks; those checks do not prove the physical bridges.

## Historical addresses

The former unconditional implications are withdrawn; the replacement scopes are stated above.

<a id="g2-симметрия"></a>
<a id="альтернативные-структуры"></a>
<a id="вывод-n7"></a>
<a id="граница-кд"></a>
<a id="информационная-интерпретация"></a>
<a id="мост"></a>
<a id="постулат-p1"></a>
<a id="постулат-p2"></a>
<a id="прецеденты-октонионы"></a>
<a id="связь-с-угм"></a>
<a id="следствия"></a>
<a id="фано-когерентности"></a>
<a id="хэмминг-структура"></a>
<a id="шаг-t1"></a>
<a id="шаг-t12"></a>
<a id="шаг-t13"></a>
<a id="шаг-t14"></a>
<a id="шаг-t2"></a>
<a id="шаг-t3"></a>
<a id="шаг-t4"></a>
<a id="шаг-t5"></a>
<a id="шаг-t6"></a>
<a id="шаг-t7"></a>
<a id="шаг-t9"></a>
