---
slug: /proofs/minimality/theorem-octonionic-derivation
sidebar_position: 2
title: "Structural Derivation of N = 7 via Octonions"
description: "Canonical proof: P1 + P2 → O → N = 7 via the Hurwitz theorem. Bridge (AP)+(PH)+(QG)+(V) → P1+P2 via the T15 chain (15 steps): [T] for the canonical orientation of the Fano lines, the only orientation class the design determines (Theorem T15-canon)"
---

# Structural Derivation of N = 7 via Octonions

## Methodology and status markers

:::warning Status markers for statements
Each statement is marked with one of three statuses (the meanings are those of the [status registry](/docs/reference/status-registry); this page uses a three-letter subset of them):
- **[T]** — **Theorem**: proven in pure mathematics or derived from axioms
- **[C]** — **Conditional theorem**: proven under an explicitly named assumption (the canonical meaning of the [status registry](/docs/reference/status-registry); on this page both assumptions are historical: (Alt) — the multiplication carried by the seven Fano lines is alternative, equivalently normed — discharged by [T15-canon](#каноническая-ориентация), and (МП), $\lambda = 1$). A statement that merely *follows logically* from theorems is itself **[T]**, not [C] — an earlier legend on this page read "[C] — Consequence: logically follows from [T]", which gave the letter a second meaning and is retracted.
- **[I]** — **Interpretation**: substantive connection with UHM
:::

:::info Dual-track status of N = 7: the number and the structure
The dimensionality $N = 7$ and its algebraic structure are established by **two tracks with distinct, complementary roles**:

| Track | Delivers | Path | Status |
|---|---|---|---|
| **Track A** | The **number**: $N = 7$ | [Axiom 3](../../core/foundations/axiom-omega#аксиоматика) + [Theorem S](./theorem-minimality-7): (AP)+(PH)+(QG) → 7 functionally independent aspects → $N \geq 7$, minimality → $N = 7$ | [T] |
| **Track B** | The **structure**: Fano/octonionic, P1 + P2 | The T15 bridge chain (this document): given $N = 7$ (consumed from Track A at [Step T8](#шаг-t8)), (AP)+(PH)+(QG)+(V) force the Fano organization BIBD$(7,3,1)$ [T given Track A]; the octonionic algebra $\mathbb{O}$ follows at [Step T15](#шаг-t15) for the canonical orientation, the only orientation class the design determines ([T15-canon](#каноническая-ориентация)) | [T given Track A] ([C at (Alt)] earlier on 2026-09-25) |
| **Consistency closure** | $\dim \mathrm{Im}(\mathbb{O}) = 8 - 1 = 7$ | The structure returned by Track B has imaginary dimension exactly $7$ — the loop closes on the same number Track A supplied | [T] |

Track A proves the *number*; Track B proves the *structure* of the $N=7$ system; the octonionic closure confirms the two are one coherent whole. (Track B is **not** a second independent derivation of the number — its Step T8 takes $N = 7$ as input; what it derives independently is that the seven-dimensional system is forced to be Fano/octonionic.) The bridge is **[T]** with the canonical orientation ([§5](#мост)): Steps T1–T14 deliver the unordered design BIBD$(7,3,1)$; only 16 of the $2^7=128$ orientations of its lines give a normed algebra, and these 16 form the only orientation class that the design itself determines ([T15-canon](#каноническая-ориентация)). (Until 2026-09-25 this box said "[T] — fully closed" without that argument; the bridge was then lowered to [C at (Alt)], and the theorem restores [T] in this precise form.) A genuinely *independent* second derivation of the number does exist, from another direction entirely: **Theorem Σ** ([T-224](/docs/applied/research/syndrome-calculus#t-224)) forces $N = 7$ from perfect single-fault diagnosability alone, consuming nothing from Track A — and [T-244](/docs/applied/research/syndrome-calculus#отбор-знака) proves that this diagnosability track and Track B are *one* condition (a frame is perfectly diagnosable exactly when it is a division algebra), so the closure loop is not merely consistent but forced from both ends.
:::

---

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

## §2. Theorems P1, P2 [T] {#постулаты}

### 2.1 Theorem P1 (Division Algebra) [T] {#постулат-p1}

:::info Theorem P1 [T] (the T15 bridge chain with the canonical orientation of the Fano lines)
The space of internal degrees of freedom of a viable system is isomorphic to $\text{Im}(\mathcal{A})$ — the imaginary part of some normed division algebra $\mathcal{A}$ over $\mathbb{R}$.
:::

**Derivation of P1:** P1 follows from (AP)+(PH)+(QG)+(V) via the T15 chain (§5) for the algebra that the Fano frame determines. On the Fano support (Alt) and P1 are equivalent — exactly the same 16 of the 128 orientations make the multiplication alternative and make its norm multiplicative (`test_only_16_of_128_fano_orientations_are_normed`) — and these 16 are the only orientation class invariant under the collineations of the design ([T15-canon](#каноническая-ориентация)); each of the other 112 needs a distinguished line, which no step of the chain supplies. (The status [T] stated here before 2026-09-25 rested on "Hall + Hurwitz" alone and was lowered that day to [C at (Alt)]; the canonical-orientation theorem restores [T] in the form just stated.) Original motivation:
- A division algebra guarantees invertibility: every transformation has an inverse (no "traps" in the state space)
- Normedness provides a metric: $|ab| = |a||b|$ ensures a consistent distance measure
- Imaginary part: the real component is singled out (analogue of scalar "unity", dimension $U$), the internal degrees of freedom are the imaginary directions

### 2.2 Theorem P2 (Non-associativity) [T] {#постулат-p2}

:::info Theorem P2 [T] (the T15 bridge chain with the canonical orientation of the Fano lines)
The algebra $\mathcal{A}$ is non-associative:

$$
\exists \, a, b, c \in \mathcal{A}: \quad (ab)c \neq a(bc)
$$
:::

**Derivation of P2:** P2 follows from (AP)+(PH)+(QG)+(V) via the T15 chain (§5) with the canonical orientation: the algebra on the Fano lines is $\mathbb{O}$, which is non-associative — indeed no triple of units on non-collinear points associates ([T15-canon](#каноническая-ориентация)). Original motivation:
- Associative algebras ($\mathbb{R}, \mathbb{C}, \mathbb{H}$) have $\dim(\text{Im}) \in \{0, 1, 3\}$ — insufficient for (AP)+(PH)+(QG) [by Theorem S](./theorem-minimality-7)
- Non-associativity formalizes contextuality: the result depends on the order of grouping of operations, reflecting the non-classical nature of quantum systems
- Artin's theorem [T] guarantees that non-associativity is *minimal* (pairwise interactions are associative)

### 2.3 Connection of P1+P2 with UHM Conditions [T] {#связь-с-угм}

:::info Bridge [T] — closed, with the canonical orientation of the Fano lines
The connection (AP)+(PH)+(QG)+(V) ⟹ P1+P2 goes through the formal chain T15 (15 steps): T1–T14 are [T] as stated (T8 given Track A), and Step T15 takes the canonical orientation ([T15-canon](#каноническая-ориентация); [C at (Alt)] earlier on 2026-09-25). Condition (МП) has become a theorem: it follows from T11–T14 (Choi rank = 7 ⟹ b ≥ 7 ⟹ λ = 1). The three motivational arguments below retain their intuitive role. Details: [§5](#мост). (Until 2026-09-25: "Bridge [T] — fully closed, 15 steps, all [T]".)
:::

| Argument | (AP)+(PH)+(QG) → | → P1+P2 |
|---|---|---|
| **Direct motivation** | Invertibility of transformations (AP) | Division algebra (P1) |
| **Exceptionality** | Minimal required dimensionality (Theorem S) | Non-associativity (P2), since dim Im ≤ 3 for associative algebras |
| **Cayley–Dickson boundary** | Alternativity (minimal nonlinearity of QG) | $\mathbb{O}$ — last alternative division algebra |

---

## §3. Derivation of N = 7 [T] {#вывод-n7}

:::warning Theorem (Structural derivation of N = 7) [T]
From theorems P1 and P2 (obtained from (AP)+(PH)+(QG)+(V) via the T15 chain with the canonical orientation, [T15-canon](#каноническая-ориентация)) it follows that $N = 7$. The number itself is supplied independently by Track A [T]; this section is the Track-B consistency loop.
:::

**Proof (6 steps):**

1. **[T] P1:** $\mathcal{A}$ is a normed division algebra over $\mathbb{R}$ (via the T15 chain)
2. **[T] Hurwitz:** $\dim(\mathcal{A}) \in \{1, 2, 4, 8\}$, i.e. $\mathcal{A} \in \{\mathbb{R}, \mathbb{C}, \mathbb{H}, \mathbb{O}\}$
3. **[T] P2:** $\mathcal{A}$ is non-associative (via the T15 chain)
4. **[T]:** $\mathbb{R}, \mathbb{C}, \mathbb{H}$ are associative ⟹ $\mathcal{A} = \mathbb{O}$
5. **[T]:** $\dim(\mathbb{O}) = 8$, therefore $\dim(\text{Im}(\mathbb{O})) = 8 - 1 = 7$
6. **[T]:** $N = \dim(\text{Im}(\mathbb{O})) = 7$ $\quad\blacksquare$

:::note Proof structure
Steps 1, 3 are [T] (they were [C at (Alt)] until the canonical-orientation theorem): they follow from the axioms via the T15 chain (§5), which **consumes $N = 7$ from Track A at Step T8** (Theorem S, functional minimality) and takes the canonical orientation at Step T15. Steps 2, 4, 5 are pure mathematics [T]. Step 6 is a logical consequence [T]. P1 and P2 are not postulated but derived from (AP)+(PH)+(QG)+(V) given the Track-A dimension; the resulting $\dim\mathrm{Im}(\mathbb{O}) = 7$ closes the consistency loop with the number Track A supplied (see the dual-track box, §0).
:::

---

## §4. Corollaries [T] {#следствия}

### 4.1 $G_2$-Symmetry [T] {#g2-симметрия}

From $\mathcal{A} = \mathbb{O}$ it follows that:

$$
\text{Aut}(\mathbb{O}) = G_2 \subset SO(7)
$$

**Corollary for UHM [T]:** The space $\text{Im}(\mathbb{O}) \cong \mathbb{R}^7$ has $G_2$-symmetry — a 14-parameter group preserving the multiplication structure.

:::info $G_2$ corollary [T]
$\mathrm{Aut}(\mathbb{O})=G_2$ is a theorem [T]. Identifying $G_2$-symmetry with the gauge freedom of UHM rests on the identification $\text{Im}(\mathbb{O}) \cong \{A, S, D, L, E, O, U\}$, which comes from the [bridge](#мост) and has its status: **[T]** with the canonical orientation ([T15-canon](#каноническая-ориентация)). (It was stated as [T], "fully closed by the T15 chain", before 2026-09-25 and was [C at (Alt)] earlier that day.)
:::

### 4.2 Fano Plane and Coherence Structure [T] {#фано-когерентности}

The multiplication structure of $\mathbb{O}$ is defined by the Fano plane PG(2,2):
- **7 points** ↔ 7 imaginary units $e_1, \ldots, e_7$
- **7 lines** (triples) ↔ 7 associative subtriples
- **21 pairs** of points ↔ 21 coherences $\gamma_{ij}$ in the matrix $\Gamma$

**Corollary [T]:** The 7 Fano triples single out 7 "privileged" triples of coherences — subsets closed under octonionic multiplication.

### 4.3 Hamming Code H(7,4) [T] {#хэмминг-структура}

From the coincidence of the combinatorial structure:
- **4 information bits** ↔ 4 "structural" dimensions (A, S, D, L) [I]
- **3 check bits** ↔ 3 "meta-structural" dimensions (E, O, U) [I]
- **Perfect error correction** ↔ optimal noise immunity

:::info Corollary: numbers [T], correspondence [I]
The 4+3 structure of $H(7,4)$ is a theorem [T]: H(7,4) is the unique perfect code of length 7 (T8 [T]), whose support structure = PG(2,2) (T9 [T]). Its correspondence with the division of UHM dimensions into (A,S,D,L) and (E,O,U) is **[I]**, as the list above says. The former wording — "a theorem [T], since the bridge is fully closed by the T15 chain" — is retracted [✗]: no step of the chain assigns data bits to particular dimensions, and the canonical orientation of the bridge does not either.
:::

### 4.4 Cayley–Dickson Boundary [T] {#граница-кд}

**Corollary [T]:** $\mathbb{O}$ is the last normed division algebra. Therefore:
- $N = 7$ is the **maximum** dimensionality of $\text{Im}(\mathcal{A})$ for a division algebra
- Systems with $N > 7$ cannot have the structure of a normed division algebra
- This coincides with the [parsimony principle](./theorem-minimality-7#часть-viii-ограничения-и-открытые-вопросы): $N = 7$ is simultaneously the minimum (Theorem S) and the maximum (C-D boundary) value

---

## §5. Bridge to UHM [T] {#мост}

:::info Status: **[T]** — T1–T14 closed, T15 closed by the canonical orientation
The connection P1+P2 ↔ (AP)+(PH)+(QG)+(V) goes through the formal chain T15 of 15 steps. Condition (МП) has become a theorem: T11 (Choi rank = 7 ⟹ b ≥ 7), T12 (BIBD(7,3,1) from minimal projective decomposition), T13 (b ≥ 7 lines), T14 (λ = 1) — together give λ = 1 without additional conditions. But T12–T14 deliver an **unoriented** design, and the multiplication table needs each line oriented: of the $2^7=128$ orientations, exactly 16 give a normed (equivalently, alternative) algebra — a single orbit of the sign changes $e_i\mapsto -e_i$, all of them $\mathbb{O}$ — and the other 112 give non-alternative algebras whose norm is not multiplicative (`test_only_16_of_128_fano_orientations_are_normed`). Step T15 therefore needed the named input (Alt): the multiplication carried by the lines is alternative (equivalently, normed). That input is discharged by [T15-canon](#каноническая-ориентация): the 16 normed orientations are exactly the one orientation class that is invariant under the collineations of the design, so they are the only orientation the frame delivered by T1–T14 determines; every other class requires choosing one of the seven lines.

**Status evolution:** [I] (three interpretive arguments) → [C] under (МП) (one condition) → "[T] (fully closed)" (2026-07) → [C at (Alt)] (2026-09-25) → **[T] with the canonical orientation** (2026-09-25, T15-canon). The earlier claim that "the step PG(2,2) → $\mathbb{O}$ is a canonical identification, fixed by the uniqueness of BIBD(7,3,1) (Hall) and the Hurwitz theorem" is retracted [✗]: Hall fixes the unordered design, and Hurwitz applies only once the algebra is normed, which is what (Alt) supplies. Problem 5 of §6 asked for a derivation of (Alt); T15-canon gives it in the only form that holds — (Alt) is equivalent to the orientation being determined by the design.
:::

### 5.1 Complete chain of implications (T15, 15 steps: T1–T14 [T], T15 [T] with the canonical orientation) {#цепочка-t15}

$$
\boxed{(AP)+(PH)+(QG)+(V)} \xrightarrow{T1{-}T3} \Gamma \in D(\mathcal{H}),\;\gamma_{ij}\neq 0 \xrightarrow{T4{-}T5} P > 2/N,\;\Phi \geq 1
$$

$$
\xrightarrow{T6{-}T7} \operatorname{rank}(\rho_E)>1,\;c>0 \xrightarrow{T8{-}T10} H(7,4) \to \text{PG}(2,2) \to \text{Fano optimality}
$$

$$
\xrightarrow{T11{-}T14} \Phi_{k=3}=7 \to b\geq 7 \to \lambda=1 \to \text{BIBD}(7,3,1) \xrightarrow{T15} \mathbb{O} \to P1+P2
$$

Below are the 15 bridge steps with full inline proofs. The dependencies of each step are stated explicitly.

---

#### Step T1. (AP) → existence of φ: H → H with a fixed point [T] {#шаг-t1}

**Statement.** From the autopoiesis axiom (AP) it follows that there exists a map $\varphi: \mathcal{H} \to \mathcal{H}$ with a fixed point $\varphi(\rho^*) = \rho^*$.

**Proof.** (AP) defines an autopoietic system as one that reproduces its own organization. Formally: there exists a CPTP map $\varphi$ on the state space $\mathcal{H}$ such that $\varphi(\rho^*) = \rho^*$ for some $\rho^* \in D(\mathcal{H})$. Existence of a fixed point is guaranteed: $D(\mathcal{H})$ is a compact convex subset of a finite-dimensional space, $\varphi$ is continuous ⟹ Brouwer's theorem gives $\exists \rho^*$. $\square$

**Status:** **[T]** — Brouwer's fixed point theorem.

---

#### Step T2. (QG) → Γ ∈ D(H), dim H ≥ 2 [T] {#шаг-t2}

**Statement.** From the quantum foundation axiom (QG) it follows that the state of the system is described by a density matrix $\Gamma \in D(\mathcal{H})$ in a Hilbert space $\mathcal{H}$ with $\dim \mathcal{H} \geq 2$.

**Proof.** (QG) postulates a quantum description: the state is a density operator $\Gamma \geq 0$, $\operatorname{Tr}\Gamma = 1$ in a Hilbert space $\mathcal{H}$. The requirement $\dim \mathcal{H} \geq 2$ follows from non-triviality: for $\dim = 1$ the unique state $\Gamma = |0\rangle\langle 0|$ does not admit coherences and superpositions, contradicting the quantum nature. $\square$

**Status:** **[T]** — direct consequence of (QG).

---

#### Step T3. (AP)+(QG) → Γ is non-trivial: ∃ γ\_{ij} ≠ 0 for i ≠ j [T] {#шаг-t3}

**Statement.** Together (AP) and (QG) require non-trivial coherences: $\exists\, i \neq j$ such that $\gamma_{ij} \neq 0$ in the stationary state $\rho^*$.

**Proof.** From T1 — $\varphi(\rho^*) = \rho^*$; from T2 — $\rho^* \in D(\mathcal{H})$. If $\gamma_{ij} = 0 \;\forall\, i \neq j$, then $\rho^*$ would be diagonal — a classical mixture without quantum correlations. But autopoiesis (AP) requires self-reproduction of organization, which includes the formula $\kappa_0 = \omega_0 \cdot |\gamma_{OE}| \cdot |\gamma_{OU}|/\gamma_{OO}$ (see [axiom of septicity](../../core/foundations/axiom-septicity#категориальный-вывод-kappa0)). For $\gamma_{ij}=0$ we have $\kappa_0=0$, autopoiesis is impossible. $\square$

**Status:** **[T]** — depends on T1, T2. Reference: definition of $\kappa_0$ in `axiom-septicity.md`.

---

#### Step T4. (V) → P > P\_crit = 2/N [T] {#шаг-t4}

**Statement.** From the viability axiom (V) it follows that the purity of the stationary state exceeds the critical threshold: $P > P_\text{crit} = 2/N$.

**Proof.** (V) requires stable existence of the system: balance of decoherence and regeneration. Theorem T-39a (primitivity of $\mathcal{L}_0$ [T]) establishes that the unique stationary state of the linear part is $I/N$, where $P = 1/N$. A viable system requires $P > 1/N$ (otherwise indistinguishable from the maximally mixed state). The exact threshold $P_\text{crit} = 2/N$ [T] is derived from the Frobenius norm: distinguishability $\|\Gamma - I/N\|_F > 0$ at $P = 2/N$, and $\Phi \geq 1$ at $P = P_\text{crit}$ (T-129 [T]). $\square$

**Status:** **[T]** — references: T-39a [T], $P_\text{crit} = 2/7$ [T] (for $N=7$).

---

#### Step T5. T3+T4 → |coherences| > |diagonal| [T] {#шаг-t5}

**Statement.** From T3 ($\gamma_{ij} \neq 0$) and T4 ($P > 2/N$) it follows: $\Phi \geq 1$ at $P = 2/N$, i.e. the integrated information is at least one.

**Proof.** The integration measure $\Phi$ is defined via the ratio of coherences to the diagonal (see [dimension-u.md](../../core/structure/dimension-u#мера-интеграции-φ)). Theorem T-129 [T] proves: at $P = P_\text{crit} = 2/N$ the value $\Phi = 1$ is the unique self-consistent one. For $P > 2/N$ we have $\Phi \geq 1$. This means that coherences contribute no less than diagonal elements — the system is integrated and not a sum of independent parts. $\square$

**Status:** **[T]** — reference: T-129 [T] (uniqueness of $\Phi_\text{th} = 1$).

---

#### Step T6. (PH) → rank(ρ\_E) > 1 [T] {#шаг-t6}

**Statement.** From the phenomenology axiom (PH) it follows that the reduced density matrix of the experiential dimension $\rho_E$ has rank greater than 1.

**Proof.** (PH) requires the presence of non-trivial phenomenal experience. For $\operatorname{rank}(\rho_E) = 1$ the experience of the system reduces to a single pure state — a fixed point without variability, which contradicts (PH): phenomenology requires distinguishable qualia (at least two orthogonal states in the $E$-subspace). Formally: $\operatorname{rank}(\rho_E) = 1$ ⟹ all observables in the $E$-subspace have zero variance ⟹ no phenomenal content. $\square$

**Status:** **[T]** — direct consequence of (PH).

---

#### Step T7. T4 → c > 0 [T] {#шаг-t7}

**Statement.** From $P > 2/N$ (T4) it follows that the Fano parameter must be nonzero: $c > 0$ in the dissipator structure.

**Proof.** The atomic dissipator ($c = 0$) decoheres all coherences: $\gamma_{ij}(t) \to 0$ exponentially (theorem T6 — uniform contraction [T]). For $c = 0$ the autopoiesis formula $\kappa_0 \propto |\gamma_{OE}| \cdot |\gamma_{OU}|$ is suppressed exponentially, the $\mathcal{D}/\mathcal{R}$ balance is broken, and $P \to 1/N$ — a contradiction with $P > 2/N$ (T4). Therefore, a coherence-restoring component with $c > 0$ is necessary. This is theorem T7 (necessity of $c > 0$) [T]. $\square$

**Status:** **[T]** — reference: theorem T7 [T] of this document (§5.2).

---

#### Step T8. T7 + N=7 (Track A) → Hamming code H(7,4) [T] {#шаг-t8}

**Statement.** For the $N = 7$ system (the dimension is **consumed here from Track A**, [Theorem S](./theorem-minimality-7) — functional minimality) with a coherence-restoring structure required by $c > 0$ (T7), the unique minimal-redundancy error-correcting organization is the Hamming code $H(7,4)$.

**Proof.** (i) *Why a perfect code:* the coherence-restoring structure must cover every single-coherence error with **zero redundancy overhead** — coverings that saturate the Hamming bound $\sum_{k=0}^{t}\binom{n}{k} = 2^{n-m}$ are exactly the perfect codes; any non-perfect covering wastes restoring capacity (violates the minimality selector of (V)). (ii) *Why $t=1$:* single-error correction is the minimal nontrivial correction, and $c>0$ (T7) requires at least it. (iii) *Given $n = N = 7$ from Track A:* $2^3 = 8 = 1 + 7 = \binom{7}{0} + \binom{7}{1}$, i.e. $t = 1$, $r = 3$, and $H(7,4)$ is the unique (up to equivalence) perfect binary 1-error-correcting code of length 7 (standard coding theory). $\square$

**Status:** **[Т given N=7 (Track A)]** — Hamming bound + uniqueness; the length input is the Track-A dimension. (Perfect binary 1-error-correcting codes exist only for $n = 2^r - 1$; the functional count of Theorem S selects $n = 7$ among these.)

---

#### Step T9. T8 → support of H(7,4) = PG(2,2) [T] {#шаг-t9}

**Statement.** The codewords of weight 3 of $H(7,4)$ form exactly 7 triples — the lines of the Fano plane PG(2,2); they are the complements of the 7 non-zero words of the simplex code $S(3,7)$, the dual of $H(7,4)$. (Corrected 2026-09-28: the statement placed the weight-3 words in $S(3,7)$, whose non-zero words all have weight 4.)

**Proof.** The parity-check matrix of $H(7,4)$ consists of all 7 nonzero columns of $\mathbb{F}_2^3$. The dual code $S(3,7)$, spanned by the rows of that matrix, has $2^3 - 1 = 7$ non-zero words, all of weight 4; it lies inside $H(7,4)$, which also contains $\mathbf{1}$, so their complements are the 7 codewords of weight 3 of $H(7,4)$ (weight distribution $1 + 7x^3 + 7x^4 + x^7$). Each such word is the characteristic vector of a 3-element subset of $\{1,\ldots,7\}$. These 7 triples are the lines of the projective plane $\text{PG}(2,2)$: each line contains 3 points, each point lies on 3 lines, through any 2 points there is exactly 1 line. Standard result (see §1.5, §1.7). $\square$

**Status:** **[T]** — standard algebra of finite fields.

---

#### Step T10. T9 → autopoietic optimality of the Fano channel among BIBD(7,k,1) [T] {#шаг-t10}

**Statement.** Among all $S_7$-invariant BIBD$(7,k,\lambda)$-channels with $\lambda\geq 1$, the Fano channel ($v=7,k=3,\lambda=1$) is the unique optimal one.

**Proof (with $\lambda=1$ derived, not assumed).**

*(Stage 1: $\lambda$ is forced.)* By T-39a [T] the linear Lindbladian $\mathcal L_0$ is primitive: its unique stationary state is $I/7$ and no repeated eigenspaces exist. A canonical BIBD channel with $\lambda>1$ contains $\lambda$-fold repeated blocks (pairs covered multiple times), which materialise as multiply-copied Lindblad generators and violate primitivity by introducing accidental degeneracies in the Lindbladian spectrum (Evans–Spohn criterion fails; see T-41b). Hence the **minimal** $S_7$-invariant block design compatible with primitivity has $\lambda=1$ — this is derived from T-39a, not assumed. For completeness, $\lambda=1$ is also re-derived in Steps T11–T14 from Choi-rank minimality as an independent check; the two arguments coincide.

*(Stage 2: $k$ selection given $v=7,\lambda=1$.)* BIBD arithmetic $bk(k-1)=v(v-1)\lambda$ with $v=7,\lambda=1$ yields $bk(k-1)=42$. Integer solutions with $k\geq 2$: $(b,k)\in\{(21,2),(7,3)\}$. Larger $k\in\{4,5,6\}$ give non-integer $b$ (e.g., $k=4:b=7/2$), excluded. So admissible designs are $(b,k)=(21,2)$ or $(7,3)$.

*(Stage 3: Dominance of $k=3$.)* Theorem T4 [T]:
- Contraction: $c_{k=3}=(k-1)/(v-1)=1/3$ vs $c_{k=2}=1/6$. ($k=3$ stronger.)
- Number of Lindblad operators: $b_{k=3}=7$ vs $b_{k=2}=21$. ($k=3$ minimal.)
- Purity loss: $\Delta P_{k=3}=8/9$ vs $\Delta P_{k=2}=35/36$. ($k=3$ smaller.)
- ~~Frame-group covariance: the $k=3$ Fano design is covariant under the octonionic frame group $\Gamma_{\!\text{oct}}$ (it permutes the 7 lines); the $k=2$ design has only $S_7\times S_2$ block symmetry, which does not embed in $\Gamma_{\!\text{oct}}$.~~ Retracted [✗] (2026-09-25): both channels equal $c\,\mathrm{id}+(1-c)\,\mathcal{P}_{\mathrm{base}}$ with $c=(k-1)/6$ (Theorem T1), so both are covariant under the same group — every signed permutation, hence all of $\Gamma_{\!\text{oct}}$ (order 1344) — and the criterion does not discriminate. (Neither *pinching* design is fully $G_2$-covariant — Fano-channel Th. 5.1a–b.)

$k=3$ **strictly dominates** by the first three criteria; the decisive selectors are Choi-rank minimality and BIBD closure. $\square$

**Status:** **[T]** — non-circular derivation: $\lambda=1$ forced by primitivity of $\mathcal L_0$ (Stage 1), then $k=3$ selected by dominance (Stage 3). Cf. Steps T11–T14 for the Choi-rank re-derivation of $\lambda=1$.

---

#### Step T11. T10 → Choi rank Φ\_{k=3} = 7 [T] {#шаг-t11}

**Statement.** The Choi representation rank of the Fano channel $\mathcal{D}_\Omega$ equals 7 — the minimum number of Kraus operators.

**Proof.** The Choi representation of channel $\mathcal{D}_\Omega$: $C_{\mathcal{D}} = \sum_\ell L_\ell \otimes \bar{L}_\ell$. The Fano channel with 7 lines of PG(2,2) has 7 Lindblad operators $L_\ell$ of rank 3 (projectors onto Fano lines). The operators $L_\ell$ are linearly independent (each pair differs in at least one position). Therefore, $\operatorname{rank}(C_\mathcal{D}) = 7$. This is the minimum number: fewer than 7 operators cannot cover all $\binom{7}{2} = 21$ coherences for $k = 3$ (each operator covers $\binom{3}{2} = 3$ pairs, and $7 \times 3 = 21$). $\square$

**Status:** **[T]** — reference: theorem T11 [T] of this document (§5.2).

---

#### Step T12. T11 → BIBD(7,3,1) from minimal projective decomposition [T] {#шаг-t12}

**Statement.** L-unification of the dissipator at $k = 3$ and Choi rank = 7 gives BIBD$(7,3,1)$.

**Proof.** L-unification (theorem T12 [T]): all Lindblad operators are rank-3 projective operators $L_\ell = \Pi_{S_\ell}$, where $S_\ell \subset \{1,\ldots,7\}$, $|S_\ell| = 3$. The minimal projective decomposition at rank = 7 requires exactly 7 operators. Coverage completeness (T2 [T]): each pair $(i,j)$ must be covered by at least one $S_\ell$. For $b = 7$ blocks of size $k = 3$ on $v = 7$ points: each block covers 3 pairs, total $7 \times 3 = 21 = \binom{7}{2}$ pairs. The coverage is exact — each pair is covered exactly $\lambda = 1$ time. $\square$

**Status:** **[T]** — reference: theorem T12 [T] of this document (§5.2).

---

#### Step T13. T12 → b ≥ 7 lines [T] {#шаг-t13}

**Statement.** From Choi rank = 7 (T11) it follows that $b \geq 7$.

**Proof.** The Choi representation rank is a lower bound on the number of Kraus operators (Lindblad operators). If $b < 7$, then $\operatorname{rank}(C_\mathcal{D}) \leq b < 7$ — a contradiction with T11. Therefore $b \geq 7$. Together with the upper bound from T12 (the minimal decomposition gives exactly 7), we have $b = 7$. $\square$

**Status:** **[T]** — direct consequence of T11.

---

#### Step T14. T13 → λ = 1 [T] {#шаг-t14}

**Statement.** From $b = 7$, $k = 3$, $v = 7$ it follows that $\lambda = 1$.

**Proof.** BIBD identity: $b \cdot k(k-1) = v(v-1)\lambda$. Substituting: $7 \cdot 3 \cdot 2 = 7 \cdot 6 \cdot \lambda$, so $42 = 42\lambda$, i.e. $\lambda = 1$. This is BIBD$(7,3,1)$, Steiner system $S(2,3,7)$, unique up to isomorphism (Hall, 1967). Condition (МП) becomes a theorem. $\square$

**Status:** **[T]** — BIBD arithmetic + uniqueness (Hall).

---

#### Step T15. T14 → $\mathbb{O}$: P1 (division algebra) + P2 (non-associativity) [T] {#шаг-t15}

**Statement.** From BIBD$(7,3,1) \cong \text{PG}(2,2)$ **and alternativity (Alt)** it follows that the algebraic structure is the octonions $\mathbb{O}$, yielding P1 (division algebra) and P2 (non-associativity). The statement always named alternativity; the chain T1–T14 does not supply it by itself, and the canonical-orientation theorem below shows that alternativity is exactly the condition that the orientation be determined by the design.

**Proof.** (i) BIBD$(7,3,1)$ is unique (Hall, 1967) and isomorphic to PG(2,2) — the Fano plane (§1.5). (ii) The 7 lines of PG(2,2) define a multiplication table of the 7 imaginary units $e_1,\ldots,e_7$ — line $(e_i, e_j, e_k)$ specifies $e_i \cdot e_j = e_k$ (Baez, 2002) — **once each line is given a cyclic orientation**, which the design does not carry. Of the $2^7=128$ orientations, exactly 16 make the norm multiplicative, and the same 16 make the algebra alternative; they form one orbit of the $2^7$ sign changes $e_i\mapsto-e_i$ (stabiliser of order 8: the identity and the seven complements of lines), so all 16 give the same algebra up to isomorphism (`test_only_16_of_128_fano_orientations_are_normed`). (iii) Given (Alt), the resulting algebra $\mathcal{A} = \operatorname{span}\{1, e_1, \ldots, e_7\}$ is normed, hence the unique 8-dimensional normed division algebra (Hurwitz, §1.1), i.e. $\mathcal{A} = \mathbb{O}$. (iv) $\mathbb{O}$ is a division algebra (P1) and non-associative (P2: $\mathbb{R}, \mathbb{C}, \mathbb{H}$ are associative, $\mathbb{O}$ is not, §1.3). Additionally: $\text{Aut}(\mathbb{O}) = G_2$ (§1.6). $\square$

**Status:** **[T]** with the canonical orientation (Theorem T15-canon below); [C at (Alt)] earlier on 2026-09-25. The former status — "[T] — canonical identification: uniqueness of BIBD$(7,3,1)$ (Hall) + uniqueness of $\mathbb{O}$ (Hurwitz)" — is retracted [✗] (2026-09-25): between the two uniqueness theorems sits the choice of one of 128 orientations, and only 16 lead to $\mathbb{O}$.

---

#### Theorem T15-canon: the canonical orientation of the Fano plane is octonionic [T] {#каноническая-ориентация}

*Added 2026-09-25; it discharges the input (Alt) of Step T15 and answers Problem 5 of §6.*

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

**What this does and does not say.** The algebra obtained from the other 112 orientations exists (all of them give one isomorphism type, a non-alternative algebra with split 3-form), so the theorem is not a uniqueness theorem for algebras. It says that such an algebra cannot sit on the Fano frame produced by Steps T1–T14 without an additional datum — a distinguished line — and none of the steps supplies one: every object they use (the line projectors $\Pi_\ell$, the Fano channel, the Hamming code, the BIBD counts) is the same for all 128 orientations. The frame is delivered only up to isomorphism (Hall's uniqueness, Step T14), and the only orientation class that is well defined on it is the octonionic one. In this sense (Alt) is not an extra input but a consequence of canonicity: **(Alt) ⟺ the orientation is determined by the design**.

---

#### Summary table

| Step | Implication | Dependencies | Basis | Status |
|-----|-----------|-------------|-----------|--------|
| T1 | (AP) ⟹ $\exists\,\varphi$ with fixed point | (AP) | Brouwer's theorem | **[T]** |
| T2 | (QG) ⟹ $\Gamma \in D(\mathcal{H})$, $\dim \geq 2$ | (QG) | Definition of quantum foundation | **[T]** |
| T3 | (AP)+(QG) ⟹ $\exists\,\gamma_{ij} \neq 0$ | T1, T2 | $\kappa_0 \propto \|\gamma_{OE}\|\|\gamma_{OU}\|$ | **[T]** |
| T4 | (V) ⟹ $P > 2/N$ | (V) | T-39a primitivity, T-129 $\Phi_\text{th}$ | **[T]** |
| T5 | T3+T4 ⟹ $\Phi \geq 1$ | T3, T4 | T-129 [T] | **[T]** |
| T6 | (PH) ⟹ $\operatorname{rank}(\rho_E) > 1$ | (PH) | Non-triviality of qualia | **[T]** |
| T7 | T4 ⟹ $c > 0$ | T4 | Exponential suppression of $\kappa_0$ at $c=0$ | **[T]** |
| T8 | T7 + $N{=}7$ ⟹ $H(7,4)$ | T7, Theorem S (Track A: $N=7$) | Hamming bound, uniqueness | **[T given Track A]** |
| T9 | T8 ⟹ PG(2,2) | T8 | Weight-3 words of $H(7,4)$ (complements of $S(3,7)$) | **[T]** |
| T10 | T9 ⟹ Fano optimality | T9, T7 | T4 (dominance of $k=3$) | **[T]** |
| T11 | T10 ⟹ Choi rank = 7 | T10 | 7 independent projectors | **[T]** |
| T12 | T11 ⟹ BIBD$(7,3,1)$ | T11 | L-unification + coverage of 21 pairs | **[T]** |
| T13 | T12 ⟹ $b \geq 7$ | T11, T12 | Rank = lower bound | **[T]** |
| T14 | T13 ⟹ $\lambda = 1$ | T13 | BIBD identity: $42 = 42\lambda$ | **[T]** |
| T15 | T14 + canonical orientation ⟹ $\mathbb{O}$ ⟹ P1+P2 | T14, T15-canon | Hall + the unique collineation-invariant orientation class (16 of 128) + Hurwitz + Baez | **[T]** |

:::info Remark on the character of step T15 (PG(2,2) ≅ $\mathrm{Im}(\mathbb{O})$)
That the Fano plane defines the multiplication table of the imaginary units of the octonions is standard algebra (Baez, "The Octonions", 2002) — for the **oriented** Fano plane. The unordered design of T12–T14 fixes the lines, not their orientations (16 of the 128 give $\mathbb{O}$).

However, in the context of the full chain there is a **structural identification**: the transition from "Lindblad operators are organized according to PG(2,2)" to "the state space has an octonionic algebraic structure" requires identifying a combinatorial isomorphism with an algebraic one.

This identification is **not arbitrary**: PG(2,2) is the unique BIBD(7,3,1) (Hall, 1967), and the multiplication table of $\mathrm{Im}(\mathbb{O})$ is the unique non-associative normed division algebra of dimension 7 (Hurwitz). Two rigid constraints (dynamical and algebraic) uniquely single out the same structure. Nevertheless, the transition from combinatorial organization to full algebraic interpretation (division, normedness, alternativity) enriches the structure beyond what strictly follows from the dynamical axioms.

**Status (corrected 2026-09-25):** Steps T1–T14 are [T] as stated (T8 given Track A); Step T15 is **[T]** with the canonical orientation (T15-canon; it was [C at (Alt)] earlier that day). The former lines "Each of the 15 steps is [T]. The complete chain is closed [T]. The structural identification PG(2,2) → $\mathbb{O}$ is fixed by uniqueness on both sides (Hall + Hurwitz), making it a canonical identification" are retracted [✗]: the uniqueness on the left is that of the unordered design, the uniqueness on the right is that of normed algebras, and the orientation between them is an input unless canonicity fixes it — which is what T15-canon proves.
:::

:::warning Resolution of the ℝ⁷ → ℂ⁷ problem (complexification of octonions)
**Problem.** Octonions $\mathbb{O}$ are a real algebra, $\mathrm{Im}(\mathbb{O}) \cong \mathbb{R}^7$. Quantum mechanics requires $\mathbb{C}^7$. Complexification "doubles the degrees of freedom". How does the imaginary unit $i$ of quantum mechanics "coherently embed" into $\mathbb{O}$ without loss of the division algebra property?

**Resolution [T]:**

1. **Complexification is standard and necessary.** $\mathbb{C}^7 = \mathbb{R}^7 \otimes_{\mathbb{R}} \mathbb{C}$. The group $G_2 \subset SO(7)$ canonically embeds into $SU(7)$ (since $G_2$ preserves a real structure compatible with the complex one). All $G_2$-invariants are inherited.

2. **"Doubling" = emergence of quantum content.** The Hermitian matrix $\Gamma \in \mathcal{D}(\mathbb{C}^7)$ contains:
   - **Diagonal** $\gamma_{kk} \in \mathbb{R}$ (7 real): populations (probabilities)
   - **Off-diagonal** $\gamma_{ij} \in \mathbb{C}$ (21 complex): coherences (interference)
   - $|\gamma_{ij}|$ = coherence amplitude, $\arg(\gamma_{ij})$ = phase → $\mathrm{Gap}(i,j) = |\sin(\arg(\gamma_{ij}))|$
   
   Phase IS the quantum content. Without complexification there are no phases, no interference, no quantum mechanics.

3. **Division in $\mathbb{C}^7$ and non-associativity.** $\mathbb{O}_{\mathbb{C}} = \mathbb{O} \otimes_{\mathbb{R}} \mathbb{C}$ is **not** a division algebra (by Hurwitz's theorem, the only normed division algebras are ℝ, ℂ, ℍ, $\mathbb{O}$ — all over ℝ). But this is **not needed**: UHM uses the **automorphism group** $G_2 = \mathrm{Aut}(\mathbb{O})$ and the **Fano plane** $\mathrm{PG}(2,2)$, not the algebra $\mathbb{O}$ itself for calculations. $G_2$ is a compact Lie group defined over $\mathbb{R}$, canonically acting on $\mathbb{C}^7$. The Fano plane is a combinatorial structure independent of the coefficient field.

4. **Spectral triple (T-53 [C])** works in $\mathbb{C}^7$: $(A_{\text{int}}, H_{\text{int}}, D_{\text{int}})$ with $H_{\text{int}} = \mathbb{C}^7$. The real structure $J: \mathbb{C}^7 \to \mathbb{C}^7$ (antilinear involution) provides the connection to $\mathbb{R}^7$. (The KO-dimension 6 claimed for it is retracted: complex conjugation commutes with the real grading, which is KO-dimension 0 — [spacetime, Step 6](/docs/core/foundations/spacetime#теорема-спектральная-тройка).)
:::

### 5.2 Key theorems

**Theorem T1 (Equivalence of BIBD channels) [T].** All $(v,k,\lambda)$-BIBD channels with the same $v,k$ generate the same CPTP channel. The coherence contraction $c = (k-1)/(v-1)$ is independent of $\lambda$. Corollary: the question "why $\lambda=1$?" is replaced by "why $k=3$?".

**Theorem T2 (Coverage completeness) [T].** Connectivity of $G_H$ + primitivity of the linear part $\mathcal{L}_0$ ⟹ $\lambda_{ij} \geq 1$ for all pairs. An uncovered pair makes the channel "blind" to the nonzero coherence $\gamma^*_{ij}$, violating (AP).

**Theorem T3 (Democraticity) [T] under (КГ).** Canonical grouping + $S_7$-invariance of Ω-atoms ⟹ coverage is democratic ($\lambda = \text{const}$).

:::note T3 vs T6: strengthening without (КГ)
Theorem T6 (uniform contraction) [T] proves democraticity of contraction **unconditionally** — from the $S_7$-equivariance of the atomic dissipator (T5 [T]). T6 removes the dependence on condition (КГ) in step 4 of the chain.
:::

**Theorem T4 (Optimality of k=3) [T].** Among admissible BIBD$(7,k,1)$ ($k \in \{2,3\}$): $k=3$ strictly dominates in contraction (1/3 vs 1/6), number of operators (7 vs 21), purity loss (8/9 vs 35/36) (the fourth criterion listed here before, frame-group covariance "$\Gamma_{\!\text{oct}}$ vs $S_7\times S_2$", is retracted: both channels are $\Gamma_{\!\text{oct}}$-covariant). Full $G_2$-covariance is not a discriminator (neither pinching design has it; see Fano-channel Th. 5.1a–b) — the decisive minimal selectors are Choi-rank $=7$ (T11) and BIBD closure (T13).

**Theorem T5 ($S_7$-equivariance of dissipator) [T].** The atomic dissipator $\mathcal{D}_\text{atom}$ with operators $L_k = |k\rangle\langle k|$ commutes with any permutation $\sigma \in S_7$: $\mathcal{D}_\text{atom}[U_\sigma \Gamma U_\sigma^\dagger] = U_\sigma \mathcal{D}_\text{atom}[\Gamma] U_\sigma^\dagger$.

**Theorem T6 (Uniform contraction) [T].** Corollary of T5: $\mathcal{D}_\text{atom}[\Gamma]_{ij} = -\gamma_{ij}$ for **all** $i \neq j$, $\mathcal{D}_\text{atom}[\Gamma]_{ii} = 0$. All coherences decohere at the same rate — **without (КГ)**.

**Theorem T7 (Necessity of $c > 0$) [T].** The atomic dissipator ($c = 0$) is incompatible with autopoiesis (AP): under complete decoherence the formula $\kappa_0 = \omega_0 \cdot |\gamma_{OE}| \cdot |\gamma_{OU}| / \gamma_{OO}$ is suppressed exponentially, violating the $\mathcal{D}/\mathcal{R}$ balance for viability.

**Theorem T8 (Hamming bound) [T] (standard).** Code H(7,4) is the unique perfect single-error binary code of length 7: $2^3 = 7 + 1$.

**Theorem T9 (H(7,4) = PG(2,2)) [T] (standard).** The codewords of weight 3 of H(7,4) — the complements of the 7 non-zero words of its dual, the simplex code $S(3,7)$ — form **exactly 7 triples** = lines of the Fano plane.

**Theorem T10 (Autopoietic optimality of Fano) [T].** Among $S_7$-invariant BIBD$(7,k,1)$-channels satisfying $c > 0$ (T7), coverage completeness (T2), democraticity (T6), the unique optimal one is the Fano channel ($k = 3$, $c = 1/3$).

**Theorem T11 (Choi rank) [T].** The Choi representation rank of channel $\mathcal{D}_\Omega$ equals 7, requiring $b \geq 7$ Lindblad operators.

**Theorem T12 (L-unification) [T].** L-unification of the dissipator at $k=3$ gives rank-3 projective operators.

**Theorem T13 (BIBD closure) [T].** The combinatorial constraints $b=7$, $k=3$, $v=7$, contraction $c=1/3$ uniquely determine $\lambda = 1$, i.e. BIBD$(7,3,1)$. Condition (МП) becomes a consequence of T11–T13.

Detailed proofs: [Lindblad operators](/docs/core/operators/lindblad-operators#редукция-моста).

### 5.3 Closure of condition (МП) [T]

Condition (МП) — the principle of minimal representation — **has become a theorem**. Previously it was the only conditional step of the chain. Theorems T11–T13 close it:

1. **T11 [T]:** Choi representation rank = 7, therefore $b \geq 7$
2. **T12 [T]:** L-unification + $k=3$ gives rank-3 projective operators
3. **T13 [T]:** $b=7$, $k=3$, $v=7$, contraction $1/3$ ⟹ BIBD$(7,3,1)$, i.e. $\lambda = 1$

**Status evolution:**

| Version | Bridge status | Conditions |
|---|---|---|
| Initial | [I] | Three interpretive arguments |
| After T1–T10 | [C] under (МП) | One condition: $\lambda = 1$ |
| After T11–T13 | "[T]" | Claimed fully closed, no conditions |
| 2026-09-25, audit | [C at (Alt)] | (МП) closed; the orientation input (Alt) of Step T15 remains |
| 2026-09-25, T15-canon | **[T]** | the normed orientations are the unique orientation class determined by the design |

**Three independent confirmations of $\lambda = 1$ (now all [T]):**

| # | Argument | Type |
|---|----------|-----|
| 1 | T11+T13: Choi rank + combinatorics ⟹ $b = 7$, $\lambda = 1$ | Structural [T] |
| 2 | BIBD(7,3,1) — unique Steiner system $S(2,3,7)$ | Mathematical [T] |
| 3 | H(7,4) — unique perfect code: syndrome completeness at min redundancy | Informational [T] |

### 5.4 Information-theoretic interpretation {#информационная-интерпретация}

The Hamming code H(7,4) gives an **information-theoretic justification** of the Fano structure:

| H(7,4) component | Holon component | Interpretation |
|---|---|---|
| 7 code positions | 7 dimensions {A,S,D,L,E,O,U} | Information carriers |
| 4 information bits | 4 "free" degrees of freedom | Self-model content |
| 3 check bits | 3 "control" observations | Perturbation syndrome |
| 7 words of $H(7,4)$ of weight 3 | 7 Fano lines | Composite observations |
| $d = 3$ (code distance) | Distinguishability of 1-errors | Minimum for correction |

**The number 3** appears in four independent contexts:
1. **K = 3** — number of dynamical types (triadic decomposition [T])
2. **k = 3** — Fano channel block size
3. **r = 3** — number of Hamming code check bits
4. **d = 3** — code distance

### 5.5 Original motivational arguments [I]

The three original arguments retain their motivational role, although they are now superseded by the formal chain:

| UHM condition | Algebra property | Connection |
|---|---|---|
| (AP) Autopoiesis: invertibility of $\varphi$ | Divisibility: $\forall a \neq 0, \exists a^{-1}$ | Invertibility ↔ divisibility |
| (PH) Phenomenology: $\rho_E \neq 0$ | Normedness: $\lvert ab\rvert = \lvert a\rvert\lvert b\rvert$ | Metric ↔ norm |
| (QG) Quantum foundation: nonlinearity | Non-associativity | Contextuality ↔ non-associativity |

---

## §5.6 Comparative test against alternative incidence structures {#альтернативные-структуры}

A skeptical reading of the T15 chain may ask: is there a **competing** incidence structure (graph, design, or finite geometry) with $N \neq 7$ that also satisfies the constraints? This subsection answers explicitly by enumerating the leading candidates and checking each against the seven structural constraints required by UHM.

**The seven structural constraints (extracted from T1–T15):**

| # | Constraint | Source step | Required value |
|---|---|---|---|
| C1 | Hurwitz dimension: $N+1 \in \{1,2,4,8\}$ | T15 + §1.1 | $N \in \{0,1,3,7\}$ |
| C2 | E-dimension non-trivial: $N \ge 4$ | T6 (rank $\rho_E > 1$) | $N \ge 4$ |
| C3 | Perfect Hamming code of length $N$: $N = 2^r - 1$ | T8 + §1.7 | $N \in \{1,3,7,15,31,\ldots\}$ |
| C4 | Steiner triple system $STS(N)$: $N \equiv 1$ or $3 \pmod 6$ | T9 + Hall | $N \in \{3,7,9,13,15,19,21,\ldots\}$ |
| C5 | BIBD closure $b=v$, $k=3$, $\lambda=1$: $bk(k-1) = v(v-1)\lambda$ with $b=v$ | T11–T14 | $N=7$ only (Hall, [Hall67]) |
| C6 | Normed division algebra exists at $N+1$ | T15 + §1.3 | $N \in \{0,1,3,7\}$ |
| C7 | $G_2$-rigidity: $\mathrm{Aut}$ = exceptional simple Lie group | §1.6 + uniqueness-theorem | $N=7$ only |

**Dependence among the constraints (added 2026-09-25).** C1 and C6 are the same Hurwitz condition (a normed division algebra of dimension $N+1$ exists), and C7 is a property of the algebra that C1/C6 select, so the table contains five independent constraints, not seven; its C6 and C7 columns repeat C1. C1, C6 and C7 come from Step T15 and therefore carry its orientation, which is the canonical one (T15-canon).

**Pass/fail table for candidate structures.**

| $N$ | Candidate | C1 | C2 | C3 | C4 | C5 | C6 | C7 | UHM-viable? |
|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | $\mathbb R$, trivial | ✓ | ✗ | ✓ ($H(1,1)$) | ✗ | ✗ | ✓ ($\mathbb R$) | ✗ | **No** (C2, C4, C5, C7 fail) |
| 3 | $\mathbb H$, $STS(3)$ trivial | ✓ | ✓ | ✓ ($H(3,1)$ rep) | ✓ ($b=1$) | ✗ ($b=1\ne 3$) | ✓ ($\mathbb H$) | ✗ ($\mathrm{Aut}\mathbb H = SO(3)$) | **No** (C5, C7 fail) |
| **7** | **$\mathbb O$, PG(2,2)** | **✓** | **✓** | **✓ ($H(7,4)$)** | **✓ ($STS(7)$)** | **✓ ($b=7,\lambda=1$)** | **✓ ($\mathbb O$)** | **✓ ($G_2$)** | **YES** |
| 9 | $AG(2,3)$ ternary affine | ✗ | ✓ | ✗ | ✓ ($STS(9)$) | ✗ ($b=12$) | ✗ | ✗ | **No** (C1, C3, C5, C6, C7 fail) |
| 13 | PG(2,3) | ✗ | ✓ | ✗ | ✓ ($STS(13)$) | ✗ ($b=26$) | ✗ | ✗ | **No** (C1, C3, C5, C6, C7 fail) |
| 15 | PG(3,2) + $\mathbb S$ sedenions | ✗ ($16\notin$ Hurwitz beyond $\mathbb O$) | ✓ | ✓ ($H(15,11)$) | ✓ ($STS(15)$) | ✗ ($b=35$) | ✗ ($\mathbb S$ has zero divisors) | ✗ ($\mathrm{Aut}\mathbb S \neq$ simple) | **No** (C1, C5, C6, C7 fail) |
| 21 | PG(2,4) | ✗ | ✓ | ✗ | ✓ ($STS(21)$) | ✗ ($b=70$) | ✗ | ✗ | **No** (5 constraints fail) |

**Conclusion (Theorem on uniqueness of $N=7$ under (AP)+(PH)+(QG)+(V)).** The conjunction $C1 \cap C2 \cap C3 \cap C4 \cap C5 \cap C6 \cap C7$ is satisfied by **exactly one** value of $N$, namely $N=7$. Status: the finite check is [T]; as a statement about the axioms it is [T] through C1, C6, C7 with the canonical orientation of Step T15 ([C at (Alt)] until T15-canon), while the route through C5 alone uses T11–T14, which were run at $N=7$ taken from Track A. Until 2026-09-25 the conclusion was marked [T] without this split.

**Proof.** $C1 \cap C3 = \{N : N+1\in\{2,4,8\} \wedge N = 2^r - 1\} = \{1,3,7\}$ (intersection of Hurwitz and Mersenne-1 sets). $C2$ adds $N\ge 4$, removing $1$ and $3$, leaving $\{7\}$. $C5$ independently isolates $N=7$ via Hall's BIBD closure theorem. $C6$ confirms $\mathbb O$ is the relevant division algebra. $C7$ locks the gauge group to $G_2$ via uniqueness of $\mathrm{Aut}(\mathbb O)$ as the unique exceptional simple Lie group obtainable as automorphisms of a Hurwitz algebra at this dimension. All seven constraints converge on $N=7$. $\square$

**Notable near-misses (and why they fail):**

- **$N=3$ ($\mathbb H$ quaternions, $STS(3)$).** Passes C1, C2, C3, C4, C6 but fails C5 (Steiner triple system on 3 points has only one block, $b=1\ne 3$) and C7 ($\mathrm{Aut}(\mathbb H) = SO(3)$, classical not exceptional). Insufficient combinatorial richness for the UHM dynamics.
- **$N=9$ ($AG(2,3)$ ternary affine plane).** A Steiner triple system $STS(9)$ exists with 12 blocks of size 3 covering all 36 pairs. Fails C1 (no normed division algebra of dim 10), C3 (no perfect Hamming code of length 9), C5 (block count $b=12\ne v=9$), C6 and C7. Mathematically fine as a design but cannot host UHM physics.
- **$N=15$ ($PG(3,2)$, $H(15,11)$, $\mathbb S$ sedenions).** Passes C2, C3, C4. Fails C1 (Hurwitz cuts off at dimension 8; $\mathbb S$ has zero divisors), C5 ($b=35$ blocks for $STS(15)$), C6, C7. The sedenion case is particularly instructive: passing the Cayley–Dickson boundary, one loses divisibility, and the automorphism group splits ($\mathrm{Aut}(\mathbb S) = G_2 \times S_3$, no longer simple) — both C6 and C7 fail.

**Operational replication test.** An independent investigator can verify the table by:
1. Running the BIBD identity $b\cdot k(k-1) = v(v-1)\lambda$ for $(v,k,\lambda) = (N,3,1)$ and checking $b = v$.
2. Checking $N+1 \in \{2,4,8\}$ for normed-division-algebra existence (Hurwitz, finite check).
3. Checking $N = 2^r - 1$ for Hamming-code length (finite check).
4. Looking up $\mathrm{Aut}$ of the candidate algebra in any standard reference (e.g., Baez 2002 *The Octonions*, §3) and verifying it is one of the five exceptional simple Lie groups.

The pass/fail outcome of these four mechanical checks is what fixes $N=7$ uniquely. There is no fitting freedom.

---

## §5.7 Precedents and related programmes {#прецеденты-октонионы}

The route "normed division algebra → octonions → seven imaginary units → $G_2$ and the Fano plane" was not opened by UHM. Since 1973 the *octonionic lineage* has followed it to model particles, and since 1983 the division algebras have been used to fix physical dimension counts. What is UHM's own is the claim that the octonions are *forced* — derived from (AP)+(PH)+(QG)+(V) by the T15 chain of §5.1 (registry row 41n) — whereas every programme below takes the division algebras as input. The entries record what each did first, and where it is stronger or weaker than the derivation above.

**Hurwitz as a dimension selector (Kugo and Townsend, 1983; Baez and Huerta, 2010).** Using the Hurwitz theorem of §1.1 to fix a physical number is older than UHM. Kugo and Townsend related supersymmetry to the four division algebras ("Supersymmetry and the division algebras", *Nucl. Phys. B* **221**, 357–380 (1983)); Baez and Huerta prove that Yang–Mills fields minimally coupled to massless spinors are supersymmetric exactly when spacetime has dimension 3, 4, 6 or 10 — the dimension of $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$ or $\mathbb{O}$ plus two ("Division algebras and supersymmetry I", *Proc. Symp. Pure Math.* **81**, 65–80 (2010), [arXiv:0909.0551](https://arxiv.org/abs/0909.0551)). *Standing:* established theorems. *Parallel:* §3 uses the Hurwitz theorem to pass from P1+P2 to $N=7$ [I]. *Difference:* there the count follows from an algebraic identity inside a field theory and counts spacetime dimensions; here it follows from the premises P1 (division algebra) and P2 (non-associativity) and counts the dimensions of a holon.

**Dixon (1994): the algebra $\mathbb{R}\otimes\mathbb{C}\otimes\mathbb{H}\otimes\mathbb{O}$.** Geoffrey Dixon built the first extended model of Standard Model structure on all four division algebras at once (*Division Algebras: Octonions, Quaternions, Complex Numbers and the Algebraic Design of Physics*, Kluwer, Dordrecht 1994, DOI [10.1007/978-1-4757-2315-1](https://doi.org/10.1007/978-1-4757-2315-1)). The 64-real-dimensional algebra $\mathbb{R}\otimes\mathbb{C}\otimes\mathbb{H}\otimes\mathbb{O}$, now called the Dixon algebra, carries there the quarks and leptons with their $\mathrm{U}(1)\times\mathrm{SU}(2)\times\mathrm{SU}(3)$ gauge fields — Baez describes the model, built on $\mathbb{C}\otimes\mathbb{H}\otimes\mathbb{O}$, as one "in which the 3 forces arise naturally from the three factors in this tensor product" — and the model is linked to ten-dimensional spacetime. *Standing:* the founding text of the tensor-product line; later work kept the algebra and changed the construction — Furey: "our implementation of this algebra differs significantly, particularly with respect to chirality and weak isospin, and in our treatment of antiparticles" (thesis, [arXiv:1611.09182](https://arxiv.org/abs/1611.09182)). *Parallel:* the selection of $\mathbb{O}$ in §3 [I]. *Difference:* Dixon needs $\mathbb{C}$, $\mathbb{H}$ and $\mathbb{O}$ together and lets the algebra itself carry particle states; UHM uses only $\mathrm{Im}(\mathbb{O})$, and the box on the $\mathbb{R}^7\to\mathbb{C}^7$ problem in §5.1 states that it uses $G_2$ and the Fano plane, "not the algebra $\mathbb{O}$ itself for calculations". UHM therefore carries less algebraic structure than Dixon and derives no particle representation from it.

**Günaydın and Gürsey (1973, 1974): colour as the stabiliser of one unit.** The corollary of §4.1 — $G_2$ acting on $\mathrm{Im}(\mathbb{O})$ — was read physically long before UHM: Günaydın and Gürsey identified the subgroup $\mathrm{SU}(3)\subset G_2$ that fixes one imaginary unit with quark colour (*J. Math. Phys.* **14**, 1651–1667 (1973), DOI [10.1063/1.1666240](https://doi.org/10.1063/1.1666240)); see [G₂-structure, §2.6](/docs/physics/gauge-symmetry/g2-structure#прецеденты-g2).

**Furey (2014–2025): the complex octonions as a particle algebra.** Furey's programme is the most developed modern form of the lineage. Minimal left ideals of $\mathbb{C}\otimes\mathbb{O}$ — the smallest subspaces that the algebra maps into themselves under left multiplication — reproduce one generation of quarks and leptons under $\mathrm{SU}(3)_c\times\mathrm{U}(1)_{\mathrm{em}}$, with electric charge given by a number operator, $Q=N/3$ (thesis, University of Waterloo 2015, [arXiv:1611.09182](https://arxiv.org/abs/1611.09182)); the 64-complex-dimensional algebra generated by $\mathbb{C}\otimes\mathbb{O}$ acting on itself contains the $\mathrm{SU}(3)_c$ and $\mathrm{U}(1)_{\mathrm{em}}$ representations of exactly three generations (*JHEP* **10** (2014) 046, [arXiv:1405.4601](https://arxiv.org/abs/1405.4601); *Phys. Lett. B* **785**, 84–89 (2018), [arXiv:1910.08395](https://arxiv.org/abs/1910.08395)). With Hughes she places one full generation of Standard Model Weyl representations in a single copy of $\mathbb{R}\otimes\mathbb{C}\otimes\mathbb{H}\otimes\mathbb{O}$ (*Phys. Lett. B* **827**, 136959 (2022), [arXiv:2209.13016](https://arxiv.org/abs/2209.13016)) and reads the breaking chain $\mathrm{Spin}(10)$ → Pati–Salam → left–right symmetric → Standard Model with $B-L$ off $\mathbb{O}$, $\mathbb{H}$ and $\mathbb{C}$ in turn (*Phys. Lett. B* **831**, 137186 (2022), [arXiv:2210.10126](https://arxiv.org/abs/2210.10126)). *Standing:* active; by her own account three generations remain an open checkpoint (*Ann. Phys. (Berlin)* **537**, 2400323 (2025), [arXiv:2312.12799](https://arxiv.org/abs/2312.12799)). *Parallel:* the box of §5.1 that sets the complexified octonions $\mathbb{O}\otimes\mathbb{C}$ aside as not needed [I]. *Difference:* Furey's programme is built on exactly these complexified octonions and extracts from them the representation content — colour, charge, chirality — that UHM's use of $G_2$ and the Fano plane does not produce. Conversely, Furey assumes the division algebras, while UHM claims to derive $\mathbb{O}$.

**The exceptional Jordan algebra (Dubois-Violette 2016; Todorov and Dubois-Violette 2018; Krasnov 2021; Boyle 2026).** This line takes as internal quantum space the exceptional Jordan algebra $J_3(\mathbb{O})$ of Hermitian octonionic $3\times3$ matrices (Dubois-Violette, *Nucl. Phys. B* **912**, 426–449 (2016), [arXiv:1604.01247](https://arxiv.org/abs/1604.01247)). Its automorphism group is $F_4$, and the Standard Model group is the intersection of the maximal subgroups $\mathrm{Spin}(9)$ and $(\mathrm{SU}(3)\times\mathrm{SU}(3))/\mathbb{Z}_3$ of $F_4$, while inside $G_2$ the same method yields only $\mathrm{SU}(3)$ or $\mathrm{U}(2)$ (Todorov and Dubois-Violette, *Int. J. Mod. Phys. A* **33**, 1850118 (2018), [arXiv:1806.09450](https://arxiv.org/abs/1806.09450)); Krasnov characterises $G_{\mathrm{SM}}$ inside $\mathrm{Spin}(9)$ by a complex structure fixed by one unit imaginary octonion (*J. Math. Phys.* **62**, 021703 (2021), [arXiv:1912.11282](https://arxiv.org/abs/1912.11282)); Boyle passes to the complexified algebra, obtains a left–right symmetric extension of the Standard Model and proposes that the three generations come from triality (*J. Math. Phys.* **67**, 071701 (2026), [arXiv:2006.16265](https://arxiv.org/abs/2006.16265)). *Standing:* published; the group theory holds, the physical interpretation is open. *Parallel:* the $G_2$ corollary of §4.1, and T-220, the absence of a structure-preserving reduction from $F_4$ to $G_2$ ([Fundamental closures, §14](/docs/proofs/categorical/fundamental-closures#t-220-three-generations)) [I]. *Difference:* the lineage obtains $G_{\mathrm{SM}}$ by going up from $G_2$ to $F_4$ or $E_6$; UHM stays at $G_2=\mathrm{Aut}(\mathbb{O})$ and must supply the remaining rank elsewhere ([Standard Model from G₂](/docs/physics/gauge-symmetry/standard-model#проблема-ранга)).

**Manogue and Dray (1999, 2010): one preferred unit.** Choosing one preferred imaginary unit reduces octonionic ten-dimensional spacetime to four dimensions and singles out three quaternionic subalgebras, which the authors read as three generations (*Mod. Phys. Lett. A* **14**, 99–103 (1999), [arXiv:hep-th/9807044](https://arxiv.org/abs/hep-th/9807044); *J. Phys. Conf. Ser.* **254**, 012005 (2010), [arXiv:0911.2253](https://arxiv.org/abs/0911.2253)); see [Spacetime](/docs/core/foundations/spacetime#прецеденты-3-плюс-1) and [Fermion generations, §1.3](/docs/physics/particle-physics/fermion-generations#прецеденты-три-поколения).

**Baez (2002): the Fano plane needs orientations.** Step T15 cites Baez's review for the rule "line $(e_i,e_j,e_k)$ specifies $e_i\cdot e_j=e_k$". The review states the rule for a Fano plane whose seven lines each carry a cyclic orientation: with the arrows drawn, the plane "completely describes the algebra structure of the octonions"; equivalently, $\mathbb{O}$ is the group algebra of $\mathbb{Z}_2^3$ twisted by a sign function (*Bull. Amer. Math. Soc.* **39**, 145–205 (2002), [arXiv:math/0105155](https://arxiv.org/abs/math/0105155)). *Standing:* standard; on physics Baez wrote that "there is still no proof that the octonions are useful for understanding the real world". *Difference, and a gap in T15:* Steps T12–T14 derive the unordered design BIBD$(7,3,1)$, and a block design carries no orientation. Of the $2^7=128$ ways to orient the seven lines of this corpus's Fano plane, 16 give a normed algebra — the octonions — and 112 give algebras in which the norm is not multiplicative (direct check). The orientation, and with it P1, is therefore an input of Step T15 rather than an output of T12–T14; the remark after the summary table of §5.1 concedes that the passage "enriches the structure beyond what strictly follows from the dynamical axioms". On 2026-09-25 Step T15, P1, P2 and registry row 41n were lowered to [C at (Alt)] for this reason; the same day [T15-canon](#каноническая-ориентация) showed that the design determines exactly one orientation class, the octonionic one, and they are [T] for it.

**M-theory on $G_2$-holonomy manifolds (Problem 4 below).** The programme that Problem 4 asks about exists. Compactifying eleven-dimensional M-theory on a seven-dimensional manifold whose holonomy group — the group generated by parallel transport around closed loops — is $G_2$ gives four-dimensional theories with one supersymmetry; non-abelian gauge groups and chiral fermions require singularities of the seven-manifold (Acharya and Gukov, *Phys. Rep.* **392**, 121–189 (2004), [arXiv:hep-th/0409191](https://arxiv.org/abs/hep-th/0409191); Atiyah and Witten, *Adv. Theor. Math. Phys.* **6**, 1–106 (2002), [arXiv:hep-th/0107177](https://arxiv.org/abs/hep-th/0107177)). *Standing:* an active programme within string theory, without experimental confirmation. *Difference:* there the seven are the dimensions of a curved space with $G_2$ holonomy, orthogonal to four-dimensional spacetime ($11=4+7$); in UHM they are the dimensions of a state space on which $G_2$ acts by automorphisms of $\mathbb{O}$. The shared ingredient is the group; the corpus establishes no map between the two.

**Critiques that apply.** We found no peer-reviewed critique aimed specifically at octonionic derivations; two published critiques of the wider genre bear on this page. Distler and Garibaldi prove that embedding the Lorentz group and the Standard Model gauge group in a real or complex form of $E_8$, in the way such unified models require, never yields a chiral theory, and that three generations do not even fit by dimension ("There is no 'Theory of Everything' inside $E_8$", *Commun. Math. Phys.* **298**, 419–436 (2010), [arXiv:0905.2658](https://arxiv.org/abs/0905.2658)): an exceptional structure that contains the right numbers need not contain the right representations. Good gives criteria for judging numerical coincidences — prior probability, simplicity, and "consilience" with independent formulas ("A quantal hypothesis for hadrons and the judging of physical numerology", in *Disorder in Physical Systems*, ed. G. Grimmett and D. Welsh, Oxford University Press 1990, 129–165). Both apply here. §5.4 lists four "independent" appearances of the number 3 in a structure rich in small integers (7 points, 7 lines, 3 points per line, 3 lines per point, 168 automorphisms). And the seven constraints of §5.6 are not seven independent tests: C1 and C6 state the same Hurwitz condition, and C7 is a property of the algebra that those two select; the convergence on $N=7$ rests on C5 alone, or on C1, C2 and C3 together.

| Ingredient used on this page | First published | What it means for the claims above |
|---|---|---|
| Hurwitz theorem fixing a physical dimension count | Kugo and Townsend 1983 | the method is prior art; its use for $N=7$ is UHM's own |
| $\mathrm{SU}(3)\subset G_2$ as the stabiliser of one unit; $7=1\oplus3\oplus\bar{3}$ | Günaydın and Gürsey 1973 | prior art for the colour reading and for the sector split |
| Division algebras as the algebra of particle states | Dixon 1994; Furey 2014 onwards | the lineage is stronger on representation content |
| Three generations from the lines through a chosen unit | Manogue and Dray 1999 | prior art for the count used in fermion generations |
| $G_{\mathrm{SM}}$ from exceptional groups | Todorov and Dubois-Violette 2018 | reached through $F_4$, not through $G_2$ |
| Fano plane as a multiplication table | standard; reviewed by Baez 2002 | needs orientations that T12–T14 do not supply |

---

## §6. Open Problems {#открытые-проблемы}

**Problem 1 (Principle of minimal representation) — solved [T].** Theorems T11–T13 prove $\lambda = 1$ from axioms A1–A5. The bridge is closed [T] with the canonical orientation (see Problem 5).

**Problem 2 ($G_2$-covariance).**
Are the UHM evolution equations $G_2$-covariant? If so, $G_2$ provides 14 independent "gauge" degrees of freedom.

**Problem 3 (Fano structure of coherences).**
Are the 7 triples of the Fano plane privileged in the structure of $\Gamma$? Verifiable prediction: coherences within Fano triples correlate more strongly.

**Problem 4 (Physical realization of $G_2$).**
Is the $G_2$ structure related to M-theory compactifications on $G_2$-manifolds (11 = 4 + 7)? That programme exists and is active; what it shares with UHM, and what it does not, is set out in [§5.7](#прецеденты-октонионы).

**Problem 5 (Orientation of the Fano lines) — answered [T] (2026-09-25).** The problem was to derive (Alt) — the choice of one of the 16 normed orientations out of 128 — from (AP)+(PH)+(QG)+(V), or to show that it is independent of them. Both halves have an answer. (Alt) is independent of Steps T1–T14 taken as statements about the unordered design: they are orientation-blind, and all 128 orientations are compatible with them. And (Alt) is exactly the condition that the orientation be determined by the design: the 16 normed orientations are the unique collineation-invariant class, while every other class needs a distinguished line ([T15-canon](#каноническая-ориентация)). The bridge, P1 and P2 are [T] for the canonical orientation.

---

**Related documents:**
- [Hypermathematics: the genesis of the seven](/docs/core/foundations/hypermathematics) — the pre-numeric genesis: $7 = 2^3-1$ as the distinction-spectrum of the terminal viable self-mirror (T-277), the volume law behind the octonion associator (T-278)
- [Theorem on 7D Minimality](./theorem-minimality-7) — Track A: (AP)+(PH)+(QG) → N ≥ 7
- [Axiom Ω⁷](../../core/foundations/axiom-omega) — Axiom 3 (N = 7)
- [Axiom of Septicity](../../core/foundations/axiom-septicity) — conditions (AP)+(PH)+(QG)+(V)
- [Consequences](../../core/foundations/consequences) — octonionic consequences
- [Seven dimensions](../../core/structure/dimensions) — octonionic interpretation of the basis
- [Correspondence with physics](../physics/physics-correspondence) — $G_2$-manifolds and M-theory
