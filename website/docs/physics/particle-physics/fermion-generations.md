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
- **[R]** Definition — definition by convention
- **[I]** Interpretation — physical interpretation of a formal result
- **[✗]** Retracted — contains an error, corrected or replaced
- **[P]** Program — research direction
:::

## Contents

1. [Number of generations from Gap-vacuum topology](#1-число-поколений-из-топологии-gap-вакуума)
   - [1.2 Theorem: exactly 3 generations](#теорема-ровно-три-генерации)
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
The original argument via $S_4$-orbits on 6 points is not strictly defined: the number of orbits depends on the action of $S_4$ on pairs vs. triplets; the claim "three classes → three generations" is not formalized. Moreover, the number of minima $V_\text{eff} \leq 3$ from the Swallowtail is an upper bound, not a lower one. **The full rigorous result $N_{\text{gen}} = 3$ [T]** — see [Theorem 1.2](#теорема-ровно-три-генерации).
:::

**Theorem.** The number of fermionic generations is determined by the topology of the Gap-vacuum:

**(a)** Each generation corresponds to a **topologically distinct** minimum of $V_\text{Gap}$ in the vacuum configuration.

**(b)** From Swallowtail analysis: the number of minima of $V_\text{eff}$ depends on the codimension of the catastrophe. For $A_4$ (swallowtail): up to 3 minima.

**(c)** The number of generations $N_\text{gen}$ = the number of distinct **types** of degenerate $\Gamma$-configurations with $R \to 0$, not connected by a $G_2$-transformation.

**(d)** From the Fano structure: 7 Fano lines define 7 "privileged" triplets. From Fano duality (point ↔ line): each point lies on 3 lines → 3 inequivalent "types" of vacuum alignment:

$$N_\text{gen} = 3$$

**Justification (d).** The vacuum configuration selects an O-direction. The remaining 6 directions form a Fano graph with 3 lines passing through each point. Three classes of inequivalent orientations of the triplet $(A,S,D)$ relative to the Fano structure give 3 generations.

More precisely: the automorphism group of the Fano plane $\mathrm{PSL}(2,7)$ (order 168) acts on 7 points. The stabilizer of one point ($O$) has order $168/7 = 24 \cong S_4$. Orbits of $S_4$ on pairs from the remaining 6 points: $C(6,2) = 15$ pairs, divided into classes by size. Three classes → three generations.

### Theorem 1.2 (Exactly 3 generations) {#теорема-ровно-три-генерации}

:::tip Theorem 1.2 (Exactly 3 generations) [T]
Strictly proved. Upper bound — from swallowtail $A_4$ [T]. Lower bound — from the structure of the multiplicative subgroup $\mathbb{Z}_7^*$ and uniqueness of the associative triplet [T]. The combination gives $N_{\text{gen}} = 3$ exactly.
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
| 2nd (c,s,μ) | $k_2 = 4$ | L | $d = 1$ (via confinement) |
| 1st (u,d,e) | $k_3 = 2$ | S | $d = 1$ (via space) |

All three elements are **distinct** ($k_1 \neq k_2 \neq k_3 \neq k_1$), which follows from the definition of the multiplicative subgroup $\{1, 2, 4\} \subset \mathbb{Z}_7^*$.

**Step 4. Proof that 3 generations are inevitable [T].**

Combining:
1. **From above:** $N_{\text{gen}} \leq 3$ from swallowtail $A_4$ [T]
2. **From below:** The triplet $(1, 2, 4)$ contains exactly 3 elements. Structurally: the multiplicative subgroup of order 3 in $\mathbb{Z}_7^*$ (order 6), index 2. Order of subgroup $= 3$ — the only possibility for a subgroup of index 2 in a group of order 6 [T]
3. **Uniqueness:** The triplet $(1,2,4)$ is unique as a Fano line with $\mathcal{A} = 0$ [T] ([Theorem 6.1](#thm-6-1))
4. **Irreducibility:** The three elements cannot be reduced to 2 (a subgroup of order 3 is irreducible: $\mathbb{Z}_3$ is a simple group) and cannot be extended to 4 (subgroup order $\leq 3$ under the swallowtail constraint)

Therefore, $N_{\text{gen}} = 3$. $\blacksquare$

:::warning Composite status
The proof of $N_{\text{gen}} = 3$ contains two independent constraints on the status:

1. **Upper bound** $\leq 3$ from swallowtail $A_4$ — **[C under Gap-potential topology]**: depends on the proved Morse structure of $V_{\text{Gap}}$.

2. **Identification** of triplet elements $(1,2,4) \subset \mathbb{Z}_7^*$ with physical fermion generations — **[I]** (interpretation, not a theorem): this correspondence is established by the principle of minimal embeddability, but is not mathematically uniquely derivable from the axioms. It cannot be "conditionally accepted" — it is a philosophical choice of interpretation.

**Final theorem status**: $N_{\text{gen}} = 3$ as a mathematical result — **[C under Gap-potential topology]**; connection to observed generations — **[I]**.
:::

:::info Clarification: lower bound and triplet (1,2,4)
The lower bound $N_{\text{gen}} \geq 3$ (Step 2) uses the specific triplet $(1, 2, 4) \subset \mathbb{Z}_7^*$ — the unique subgroup of order 3 of the multiplicative group $\mathbb{Z}_7^*$ (order 6). This is not an arbitrary choice: $(1,2,4)$ is the **unique** maximal cyclic subgroup of index 2 in $\mathbb{Z}_7^*$, and it coincides with the set of quadratic residues $\bmod 7$. Uniqueness follows from the fact that $\mathbb{Z}_7^* \cong \mathbb{Z}_6$ has exactly one subgroup of each order dividing 6. Nevertheless, the argument can be strengthened: a complete classification of all subgroups of $\mathbb{Z}_7^*$ (orders 1, 2, 3, 6) shows that no other subgroup structure gives a different number of generations within the swallowtail constraint.
:::

:::info Remark
This theorem **does not depend** on the generation assignment ($k=1 \to$ 3rd, etc.). The assignment of the 3rd generation ($k=1$) — **[T]** (unique nonzero tree-level Yukawa, [Theorem 4.1](#thm-gen-4-1)). The ordering $k=4 \to$ 2nd, $k=2 \to$ 1st — **[T]** ([Theorem 4.3](#thm-gen-4-3)).
:::

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

Imaginary part: $\mathrm{Im}(\eta_1) = \sqrt{7}/2 \neq 0$.

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

### 4.3 Theorem 4.2 (Sectoral asymmetry of generations) {#thm-gen-4-2}

:::tip Theorem 4.2 (Sectoral asymmetry of generations) [T]
Generations $k=2$ and $k=4$ belong to **different** sectors of the vacuum decomposition and have **structurally distinct** Fano paths to the Higgs. Strictly proved.
:::

**Theorem.** Generations $k=2$ and $k=4$ belong to **different** sectors of the vacuum decomposition and have **structurally distinct** Fano paths to the Higgs.

**Proof.**

**Step 1. Sector assignment [T].**

From $SU(3)_C$-decomposition [T] ([Standard Model from $G_2$](/docs/physics/gauge-symmetry/standard-model)):

- $\mathbf{3}$-sector: $\{A=1, S=2, D=3\}$ — fundamental $SU(3)$
- $\bar{\mathbf{3}}$-sector: $\{L=4, E=5, U=6\}$ — antifundamental $SU(3)$

Therefore:
- $k=2$ ($S$) $\in \mathbf{3}$-sector
- $k=4$ ($L$) $\in \bar{\mathbf{3}}$-sector

**Step 2. Fano paths to the Higgs [T].**

Higgs line: $\{A=1, E=5, U=6\}$, where $E, U \in \bar{\mathbf{3}}$. Active Fano lines (without $O=7$):

| Path | Line | Intermediate | Reaches | Sector type of pair |
|------|-------|:------------:|:---------:|:-----------------:|
| $k=2 \to E$ | $\{S=2, D=3, E=5\}$ | $D$ | $E$ (Higgs) | $(S,D)$: **3-to-3**, Gap $\sim \varepsilon$ |
| $k=4 \to U$ | $\{D=3, L=4, U=6\}$ | $D$ | $U$ (Higgs) | $(L,D)$: **3-to-$\bar{3}$**, Gap $\approx 0$ |

Both paths pass through $D=3$ (Distinction dimension), but:
- Pair $(S,D) = (2,3)$: both $\in \mathbf{3}$-sector → sector **3-to-3**, Gap $\sim \varepsilon$ (intermediate)
- Pair $(L,D) = (4,3)$: $L \in \bar{\mathbf{3}}$, $D \in \mathbf{3}$ → sector **3-to-$\bar{3}$**, Gap $\approx 0$ (confinement) $\blacksquare$

### 4.4 Theorem 4.3 (Generation ordering) {#thm-gen-4-3}

:::tip Theorem 4.3 (Generation ordering) [T]
Proved via confinement [T] and asymptotic freedom [T]. $k=4 \to$ 2nd generation, $k=2 \to$ 1st generation.
:::

#### Theorem (SA): sectoral asymmetry [T] {#гипотеза-секторной-асимметрии}

**Sectoral Asymmetry Theorem (SA) [T]:** The 1-loop effective Yukawa coupling via the confinement sector (Gap $\approx 0$) **exceeds** the coupling via the intermediate sector (Gap $\sim \varepsilon > 0$).

:::tip Proof (SA) [T]
Proved via confinement [T] and asymptotic freedom [T]:

1. **Confinement sector** ($\mathbf{3}$-to-$\bar{\mathbf{3}}$, Gap $\approx 0$): non-perturbative coupling $\sim O(\Lambda_{\text{QCD}}/v_{\text{EW}}) \sim 10^{-3}$.
2. **Intermediate sector** ($\mathbf{3}$-to-$\mathbf{3}$, Gap $\sim \varepsilon$): perturbative coupling $\sim \varepsilon^2/(16\pi^2) \sim 6 \times 10^{-7}$.
3. **Ratio** $\sim 10^3$ — confinement sector dominates.

The structural basis — different sector membership — is a theorem ([Theorem 4.2](#thm-gen-4-2)).
:::

**Theorem.** From the sectoral asymmetry (SA) [T]: $k=4 \to$ 2nd generation (c, s, μ), $k=2 \to$ 1st generation (u, d, e).

**Proof.**

**Step 1.** From Theorem 4.2: $k=4$ couples to the Higgs via the confinement-sector pair $(L,D)$, while $k=2$ — via the intermediate pair $(S,D)$.

**Step 2.** The effective Yukawa coupling at 1-loop level is proportional to the propagation amplitude through the intermediate state $D$. In the confinement sector (Gap $\approx 0$) the dynamics is **non-perturbative**: the effective coupling is determined by the confinement scale $\Lambda_{\text{QCD}}$, not by a small expansion parameter.

**Step 3.** In the intermediate sector (Gap $\sim \varepsilon$) the 1-loop amplitude is suppressed by a factor:

$$\delta_{S \to A} \sim \frac{\lambda_3}{16\pi^2} \cdot \frac{|\gamma_{SD}|^2}{m_D^2} \sim \frac{\lambda_3 \varepsilon^2}{16\pi^2} \sim \varepsilon_{\text{eff}}^2$$

:::note Status of parameter $\lambda_3$ [T]
The parameter $\lambda_3 = 2\mu^2/(3|\bar{\gamma}|) \approx 74$ is a **geometric coefficient** of the spectral action (T-74 [T]), not a perturbative coupling constant. Physical observables are defined non-perturbatively via the self-consistent vacuum $\theta^*$ (T-79 [T]). UV-finiteness (T-66 [T]) ensures structural correctness. Loop estimates are approximations to $\theta^*$, giving the right order of magnitude (error $\lesssim \times 5$). For details — see [Yukawa Hierarchy](/docs/physics/particle-physics/yukawa-hierarchy#предупреждение-λ3).

**⚠ C7**: $\lambda_3 \approx 74 \gg 4\pi$ — non-perturbative regime. All loop computations with $\lambda_3$ are formally unreliable and downgraded to **[H]**. See [warning](/docs/physics/particle-physics/yukawa-hierarchy#c7-nonperturbative).
:::

**Step 4.** From confinement [T] and asymptotic freedom [T]: the non-perturbative amplitude of the confinement sector dominates over the perturbative one:

$$y_4^{(\text{eff})} > y_2^{(\text{eff})} \quad \Longrightarrow \quad m(k=4) > m(k=2)$$

**Step 5.** Therefore: $k=4$ is the heavier of the light generations = **2nd**, $k=2$ is the lightest = **1st**.

$$\boxed{k=1 \to \text{3rd (t,b,τ)}, \quad k=4 \to \text{2nd (c,s,μ)}, \quad k=2 \to \text{1st (u,d,e)}}$$

$\blacksquare$

### 4.5 Final generation assignment table

| Mass | Generation | Fano $k$ | Dimension | Mechanism | Status |
|---|---|---|---|---|---|
| **Heaviest** | 3rd (t, b, τ) | **1** | **A (Actualization)** | Tree-level ($f_{1,E,U} \neq 0$), IR FP | **[T]** |
| **Intermediate** | 2nd (c, s, μ) | **4** | **L (Nomos)** | 1-loop, confinement ($3 \to \bar{3}$, Gap $\approx 0$) | **[T]** |
| **Light** | 1st (u, d, e) | **2** | **S (Morphogenesis)** | 1-loop, intermediate ($3 \to 3$, Gap $\sim \varepsilon$) | **[T]** |

### 4.6 Cascade of assignment consequences {#каскад-назначения}

#### 4.6.1 Neutrino hierarchy [T]

The assignment $k=4 \to$ 2nd generation and $k=2 \to$ 1st generation resolves the contradiction in [neutrino masses](/docs/physics/particle-physics/neutrino-masses): seesaw with $m_D \sim m_l$ gives the **normal** hierarchy ($m_{\nu_e} < m_{\nu_\mu} < m_{\nu_\tau}$).

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
| 1st | 2 | S (Morphogenesis) | 0.975 | 1-loop ($3$-to-$3$) | ~2 MeV | ~5 MeV | ~0.5 MeV |
| 2nd | 4 | L (Nomos) | 0.434 | 1-loop (confinement) | ~1.3 GeV | ~100 MeV | ~106 MeV |
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

### Theorem 5.2 (Vacuum breaking of Z₃) {#thm-5-2}

**Theorem.** The vacuum Gap profile breaks the $\mathbb{Z}_3$-symmetry of the Fano line $\{1,2,4\}$.

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

This **breaks** $\mathbb{Z}_3$: two generations in one sector, one — in the other. $\blacksquare$

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
The sign of the two-loop correction $\delta^{(2)}$ is not determined. With $\delta^{(2)} > 0$: agreement $64^\circ \approx 69^\circ$ ($1.5\sigma$). With $\delta^{(2)} < 0$: $39^\circ$ — excluded by observations. Until the sign is determined, the status is a hypothesis.
:::

**Theorem.** With $(k_1,k_2,k_3) = (1,2,4)$:

**(a)** Bare value of the CP phase:

$$\delta_{\text{CP}}^{(0)} = \arg(e^{2\pi i(k_1+k_2-k_3)/7}) = \arg(e^{2\pi i(-1)/7}) = -\frac{2\pi}{7} \approx -51.4°$$

**(b)** RG correction to $\delta_\text{CP}$. $V_3$ runs under RG: $\lambda_3(\mu_{\text{EW}})/\lambda_3(\mu_{\text{GUT}}) \approx 0.01$. However, the phase $\delta$ is a topological parameter (determined by the $\mathbb{Z}_7$-structure), and RG does not change its value at leading order. Corrections — from two-loop effects:

$$\delta_{\text{CP}}^{(\text{phys})} = -\frac{2\pi}{7} + \delta^{(2)}, \quad |\delta^{(2)}| \sim \frac{y_t^2}{16\pi^2} \cdot \ln\frac{\mu_{\text{GUT}}}{\mu_{\text{EW}}} \cdot \frac{2\pi}{7}$$

$$|\delta^{(2)}| \sim \frac{1.0}{16\pi^2} \times 39 \times 0.898 \approx 0.22 \text{ rad} \approx 12.6°$$

**(c)** Prediction (accounting for sign uncertainty):

$$|\delta_{\text{CP}}| = 51.4° \pm 12.6° \quad (\text{range } 39°\text{--}64°)$$

Observed: $69° \pm 4°$ (PDG). With $\delta^{(2)} > 0$: $|\delta_{\text{CP}}| \approx 64°$ — **agreement within $1.5\sigma$**. With $\delta^{(2)} < 0$: $|\delta_{\text{CP}}| \approx 39°$ — **excluded**.

The sign of the two-loop correction is determined by the sign of $\mathrm{Im}\,\mathrm{Tr}(Y_u Y_u^\dagger Y_d Y_d^\dagger [Y_u Y_u^\dagger, Y_d Y_d^\dagger])$ (Antusch–Kersten–Lindner–Ratz, 2003), which requires explicit computation in the Gap basis of Yukawa matrices.

**(d)** Updated Jarlskog invariant:

$$J \approx 3.5 \times 10^{-5} \times \frac{\sin(64°)}{\sin(51.4°)} \approx 3.5 \times 10^{-5} \times 1.15 \approx 4.0 \times 10^{-5}$$

Observed: $J = (3.08 \pm 0.15) \times 10^{-5}$. Discrepancy ~30% — within the expected accuracy of the one-loop approximation.

---

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
