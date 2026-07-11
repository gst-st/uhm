---
sidebar_position: 9
title: "Σ-calculus: the diagnosability rigidity of seven"
description: "A self-contained mathematical treatment. Theorem Σ (T-224): perfect single-fault diagnosability, a nontrivial state grammar and structural rigidity select n = 7 uniquely — a fourth independent derivation track for N = 7, using only sphere packing and design counting. Full proofs: Steiner reconstruction, uniqueness of S(2,3,7), forced linearity, Vasil'ev breakage at n = 15, the van Lint–Tietäväinen ladder. The Σ-compression protocol (T-225): the 21 → 7 → 3 → 1 measurement pyramid with its Lie-algebraic shadow so(7) = g₂ ⊕ Im O. The Steane code [[7,1,3]] as the quantum lift of Shield I, with the complete CSS construction. The Σ-Mor bridge to MSFS intensional grading."
---

# Σ-calculus: the diagnosability rigidity of seven

> *A structure that must diagnose its own single faults perfectly, must distinguish more than two global states, and must not admit rival grammars — has no freedom left: it is the Fano plane on seven axes. Diagnosability is not a bonus feature of the heptad; it is a selector of the heptad.*

:::tip Document status
The core is **Theorem Σ (T-224) [Т]**: classical mathematics — perfect codes, the reconstruction of the Steiner system $S(2,3,7)$, uniqueness of the length-7 perfect code, Vasil'ev's nonlinear codes, the van Lint–Tietäväinen classification. Every proof is given in full, as a chain of numbered lemmas; external results are quoted with exact statements. The identification of UHM axes with diagnosable status bits is **[И]**. The Σ-compression protocol (T-225) is **[С]** (conditional on the measurement model). The Σ-Mor bridge into MSFS is an **[О]** axiomatization plus a **[Г]** conjecture. All statuses are marked in place.
:::

**How this document is organized.** §1 recalls what the corpus already knew — the *forward* direction, from seven axes to the Hamming code — and situates the present result historically. §2 builds the coding-theoretic language from scratch, so that the document is self-sufficient within the corpus. §3 states the diagnosability axioms and motivates each one. §4 is the heart: Theorem Σ with complete proofs (Lemmas Σ.1–Σ.7), the arithmetic remark Σ-QR, and the dictionary between the two Fano presentations used across the corpus. §5 draws the structural corollaries — the fourth derivation track for $N = 7$ and the explanation of "tower, not width". §6 develops the operational layer: the Σ-compression protocol, its triangle geometry, its Lie-algebraic shadow, and a machine-verified reference implementation. §7 lifts the structure to quantum codes (the full CSS construction of the Steane code). §8 formulates the bridge to MSFS intensional grading. §9–§10 give falsifiable predictions, the technology package, and the status summary.

## §1. What was known: the forward direction {#известное}

The corpus has long recorded the **forward** fact [Т]: the incidence structure of the Fano plane $\mathrm{PG}(2,2)$ on the seven axes $[A,S,D,L,E,O,U]$ *is* the parity-check matrix of the Hamming code $H(7,4)$. Concretely: the Lindblad operators of the Γ-dynamics are indexed by Fano lines, and the incidence "point $i$ lies on line $k$" reproduces, entry for entry, the $3 \times 7$ check matrix ([Gap dynamics §2](/docs/core/dynamics/gap-dynamics#код-хэмминга)). On this fact rests Shield I of coherence protection — damage to a single axis is detectable and repairable from the remaining six ([Topological protection §1](/docs/applied/coherence-cybernetics/topological-protection#код-хэмминга)) — and the combinatorial grammar of the Γ-canon: the sixteen archetype signatures are exactly the codewords, with weight distribution $1 + 7x^3 + 7x^4 + x^7$ ([Γ-canon](/docs/applied/research/gamma-canon)).

In all those places the logic runs one way. **The seven axes are given first** — by the octonionic track ($\dim \mathrm{Im}\,\mathbb{O} = 7$), by $G_2$-rigidity, by the minimality theorem — and the code arrives afterwards, as a welcome structural gift. The gift is genuinely remarkable: among all linear codes, $H(7,4)$ is *perfect* — its correction balls tile the ambient cube with no gaps and no overlaps — and perfection is an arithmetic accident, not something one can order at will.

This document asks the converse question:

> **If diagnosability is demanded as an axiom — how much freedom in the number of axes survives?**

The answer is: none. Perfection is so rare that demanding it, together with two mild non-degeneracy conditions, *forces* $n = 7$ and forces the Fano grammar uniquely. Diagnosability is thereby promoted from a consequence of the heptad to an independent **selector** of the heptad — a fourth derivation track alongside number, structure and closure.

### Historical perspective {#история}

| Year | Event | Role here |
|---|---|---|
| 1948–49 | Shannon founds information theory; Golay finds the $[23,12,7]$ code | the only perfect binary code beyond the Hamming ladder |
| 1950 | Hamming constructs the $[2^r{-}1,\,2^r{-}1{-}r,\,3]$ family | the ladder itself |
| 1892/1901 | Fano's axiomatics; Steiner triple systems | $S(2,3,7)$ = the plane $\mathrm{PG}(2,2)$ |
| 1962 | Vasil'ev constructs **nonlinear** perfect codes for $n \geq 15$ | rigidity breaks above seven — part (iv) |
| 1971–73 | van Lint, Tietäväinen (independently Zinoviev–Leontiev) classify all perfect codes over prime-power alphabets | the ladder is *complete* — part (v) |
| 1996 | Calderbank–Shor, Steane: quantum CSS codes; the $[[7,1,3]]$ code | the quantum lift of Shield I (§7) |
| corpus | Shield I; Γ-canon archetypes; Fano selection rules | the forward direction |
| **this doc** | **Theorem Σ: the converse direction** | diagnosability as a selector |

## §2. Preliminaries: codes, balls, designs {#предварительные}

We fix the language; a reader familiar with coding theory may skim to §3. Everything below is over the two-element field $\mathbb{F}_2$; profiles are vectors in $\mathbb{F}_2^n$; $+$ denotes coordinatewise XOR.

**Weight and distance.** The *weight* $|x|$ of $x \in \mathbb{F}_2^n$ is the number of its nonzero coordinates; the *Hamming distance* is $d(x,y) := |x + y|$ — the number of coordinates where $x$ and $y$ disagree. It is a metric. The *ball* $B(x, t) := \{y : d(x,y) \leq t\}$ has cardinality $\sum_{i=0}^{t}\binom{n}{i}$; for $t = 1$ this is $1 + n$.

**Codes.** A *code* is any subset $\mathcal{C} \subseteq \mathbb{F}_2^n$; its *minimum distance* $d(\mathcal{C})$ is the least distance between distinct elements. A code with $d(\mathcal{C}) \geq 2t+1$ *corrects $t$ faults*: balls of radius $t$ around distinct codewords are disjoint, so any profile obtained from a codeword by at most $t$ coordinate flips has a unique nearest codeword. A code is *linear* if it is a linear subspace; then $d(\mathcal{C})$ equals the minimum weight of a nonzero codeword, and $\mathcal{C} = \ker H$ for a *check matrix* $H$. The *dual* $\mathcal{C}^\perp$ is the orthogonal complement under the bilinear form $\langle x, y\rangle = \sum_i x_i y_i \bmod 2$.

**Perfect codes.** A code with $d \geq 2t+1$ is *perfect* if the radius-$t$ balls around codewords **tile** the whole cube:
$$
|\mathcal{C}| \cdot \sum_{i=0}^{t} \binom{n}{i} \;=\; 2^n .
$$
Tiling is the strongest possible form of diagnosability: *every* raw profile has exactly one diagnosis — there is no profile outside all balls (no "undiagnosable" state) and none inside two (no ambiguity). Perfection is exceptional; its complete classification is quoted as Lemma Σ.7 below.

**Designs.** A *Steiner system* $S(2,3,n)$ is a family of 3-element *blocks* of an $n$-element point set such that every 2-element subset of points lies in **exactly one** block ($\lambda = 1$). For $n = 7$ this is the *Fano plane*: 7 points, 7 lines, 3 points on a line, 3 lines through a point, any two points on a unique line, any two lines meeting in a unique point. Its automorphism group is $\mathrm{PGL}(3,2) = \mathrm{GL}(3,2)$, simple of order $168 = (2^3{-}1)(2^3{-}2)(2^3{-}4)$.

Two presentations of the Fano plane circulate in the corpus, and we will need both:

- the **binary (XOR) presentation**: points are the nonzero vectors of $\mathbb{F}_2^3$, labelled $1,\dots,7$ by their binary value; lines are the triples $\{a, b, a \oplus b\}$ — equivalently, the 2-dimensional subspaces with $0$ removed;
- the **cyclic (QR) presentation** used by the [Γ-canon](/docs/applied/research/gamma-canon): points are residues $\bmod\ 7$; lines are the translates $\{1,2,4\} + t$ of the quadratic-residue set $\mathrm{QR}(7) = \{1,2,4\}$, which is a $(7,3,1)$ *difference set* — every nonzero residue is a difference of two of its elements in exactly one way.

Lemma Σ.6 below exhibits an explicit relabeling carrying one presentation to the other, so no corpus statement depends on the choice.

## §3. Diagnosability axioms {#аксиомы}

**Definition Σ.1 [О] (diagnostic system).** A *diagnostic system* is a pair $(n, \mathcal{C})$: $n$ binary status axes and a set $\mathcal{C} \subseteq \mathbb{F}_2^n$ of *grammatically admissible* global profiles ("archetypes"). A *fault* is a flip of one coordinate of an admissible profile; a *diagnosis* of a raw profile $x$ is an admissible profile within distance 1 of $x$, together with the faulty coordinate if $x \notin \mathcal{C}$.

We impose three requirements, and then a fourth of a different kind.

- **(D1) Single-fault correctability:** $d(\mathcal{C}) \geq 3$.

  *Motivation.* If two admissible profiles differ in one axis, a fault is invisible (the corrupted profile is again admissible, and the system silently changes archetype). If they differ in two, a single flip lands exactly between them and the diagnosis is ambiguous. Three is the least separation at which "one broken axis" is always both visible and attributable.

- **(D2) Perfect localizability:** the radius-1 balls around $\mathcal{C}$ partition $\mathbb{F}_2^n$.

  *Motivation.* Coverage (no profile outside every ball) says: *whatever* raw state the system finds itself in, a diagnosis exists — there are no states about which the grammar is speechless. Disjointness (no profile in two balls) says the diagnosis is unique. Together they eliminate both the grey zone and wasted redundancy: the diagnostic capacity is exactly matched to the state space, with no slack. For a viable holon this is the formal shape of the requirement that degradation of an axis be caught *from inside, before it cascades*, with no external arbiter to adjudicate ambiguous readings — the diagnostic act must close operationally within the system itself (cf. [self-observation](/docs/consciousness/foundations/self-observation)).

- **(D3) Nontrivial grammar:** $|\mathcal{C}| > 2$.

  *Motivation.* Two admissible profiles mean the grammar only says "everything intact / everything broken". A holon's archetype layer must distinguish qualitatively different healthy regimes — the Γ-canon's sixteen signatures are the target scale.

And separately:

- **(D4) Rigidity:** the admissible grammar is unique up to relabeling of axes and shift of origin.

  *Motivation.* If several inequivalent grammars share the same parameters, then "what counts as normal" is a convention: two observers of the same system may reconstruct different canons, and no internal experiment distinguishes them. Rigidity is the requirement that the canon be *forced*, not chosen.

## §4. Theorem Σ (T-224): diagnosability rigidity {#теорема-сигма}

#### Theorem Σ — T-224 [Т] {#t-224}

**(i)** (D1)+(D2) $\Rightarrow$ $n = 2^r - 1$ for some $r \geq 1$, and $|\mathcal{C}| = 2^{n-r}$.

**(ii)** (D1)+(D2)+(D3) $\Rightarrow$ $n \geq 7$. At $n = 7$: $|\mathcal{C}| = 16$; after translating so that $0 \in \mathcal{C}$, the weight distribution is $1 + 7x^3 + 7x^4 + x^7$; the supports of the weight-3 codewords form a Fano plane; the symmetry group of the grammar is $\mathrm{PGL}(3,2)$ of order 168.

**(iii)** At $n = 7$, (D4) holds automatically: every code satisfying (D1)+(D2) with $n = 7$ is equivalent (coordinate permutation + translation) to the Hamming code $H(7,4)$. In particular such a code is forced to be linear once it contains $0$.

**(iv)** (D4) **fails at every higher rung of the ladder**: for every $n = 2^r - 1$ with $r \geq 4$ there exist perfect codes inequivalent to the Hamming code — already at $n = 15$, Vasil'ev's nonlinear perfect $(15,\,2^{11},\,3)$ codes.

**(v)** If instead of single faults one demands perfect localization of $t \geq 2$ faults (nontrivially), the binary possibilities are exhausted by the Golay code: $n = 23$, $t = 3$ (van Lint–Tietäväinen; over $\mathbb{F}_3$, additionally $n = 11$, $t = 2$).

**Upshot: $n = 7$ is the only cardinality at which perfect diagnosability (D1–D2), a nontrivial grammar (D3) and rigidity (D4) coexist.** Below seven the grammar is degenerate; above seven it is no longer canonical.

### Proof {#доказательство-сигма}

Throughout, translate the code so that $0 \in \mathcal{C}$; (D1), (D2), (D3) are translation-invariant, and translation is one of the moves allowed by (D4). We write $\mathbf{1}$ for the all-ones vector and identify a vector with its support when convenient.

#### Lemma Σ.1 (sphere packing forces the ladder)

*(D1)+(D2) imply $1 + n = 2^r$ and $|\mathcal{C}| = 2^{n-r}$.*

**Proof.** Each radius-1 ball contains exactly $1 + n$ profiles. (D2) says the balls around the $|\mathcal{C}|$ codewords partition all $2^n$ profiles, so
$$
|\mathcal{C}|\,(1+n) = 2^n .
$$
Hence $1+n$ divides $2^n$; a divisor of a power of two is a power of two, so $1 + n = 2^r$ and $|\mathcal{C}| = 2^n/2^r = 2^{n-r}$. $\blacksquare$

#### Lemma Σ.2 (the bottom of the ladder is degenerate)

*At $r = 1$ ($n=1$): $|\mathcal{C}| = 1$. At $r = 2$ ($n=3$): $|\mathcal{C}| = 2$, and $\mathcal{C}$ is the repetition code $\{000, 111\}$ — the grammar "all intact / all broken". Both violate (D3). The first level compatible with (D3) is $r = 3$: $n = 7$, $|\mathcal{C}| = 16$.*

**Proof.** The cardinalities come from Lemma Σ.1. For $n = 3$: with $0 \in \mathcal{C}$, the second codeword has weight $\geq 3$ by (D1), so it is $111$. $\blacksquare$

#### Lemma Σ.3 (perfectness reconstructs the Fano plane)

*Let $n = 7$, $0 \in \mathcal{C}$, (D1)+(D2). Then $\mathcal{C}$ contains no words of weight 1, 2; it contains exactly seven words of weight 3; and their supports form a Steiner system $S(2,3,7)$ — every pair of coordinates lies in exactly one support.*

**Proof.** Weights 1 and 2 are excluded by (D1) (distance to $0$). Now count the $\binom{7}{2} = 21$ profiles of weight 2. Let $v$ be one of them. By (D2), $v$ lies in the ball of a unique codeword $w$. That $w$ cannot be $0$ ($d(v,0) = 2$), cannot have weight 1 or 2 (none exist), and cannot have weight $\geq 4$: a word of weight $\geq 4$ is at distance $\geq 4 - 2 = 2$ from any weight-2 profile. So $|w| = 3$ and $d(v, w) = 1$, which forces $\mathrm{supp}(v) \subset \mathrm{supp}(w)$.

Conversely, a fixed weight-3 codeword $w$ covers exactly the three weight-2 profiles obtained by deleting one point of its support. Distinct weight-3 codewords cover disjoint triples of weight-2 profiles (disjointness of balls), i.e. **no two supports share a pair of points** — and every pair is covered. Therefore the number of weight-3 codewords is $21/3 = 7$, and their supports cover each pair exactly once: a Steiner system $S(2,3,7)$. $\blacksquare$

#### Lemma Σ.4 (uniqueness of the Fano plane)

*Any two Steiner systems $S(2,3,7)$ are isomorphic; each has exactly 3 lines through every point and 7 lines in total.*

**Proof.** Fix a point $p$. The lines through $p$ cover each pair $\{p, x\}$ exactly once, so they partition the remaining 6 points into pairs: exactly 3 lines through every point, and counting incidences, $7 \cdot 3 / 3 = 7$ lines in total.

Now reconstruct the whole system from choices that are unique up to relabeling. Name the lines through $p$: $\{p,a,b\}$, $\{p,c,d\}$, $\{p,e,f\}$. Consider the line through $a$ and $c$. It cannot contain $p$ (the pair $\{p,a\}$ is already used), nor $b$ (pair $\{a,b\}$ used), nor $d$ (pair $\{c,d\}$ used); so its third point is $e$ or $f$ — say $e$, which merely fixes the labels of $e, f$. From here everything is forced:

- line through $a, d$: third point $\notin \{p, b, c, e\}$ (pairs $\{p,a\}, \{a,b\}, \{c,d\}, \{a,e\}$ used) $\Rightarrow$ it is $f$: $\{a,d,f\}$;
- line through $b, c$: third point $\notin \{p, a, d, e\}$ $\Rightarrow$ $\{b,c,f\}$;
- line through $b, d$: third point $\notin \{p, a, c, f\}$ $\Rightarrow$ $\{b,d,e\}$.

All seven lines are now determined: $\{p,a,b\}, \{p,c,d\}, \{p,e,f\}, \{a,c,e\}, \{a,d,f\}, \{b,c,f\}, \{b,d,e\}$ — and every pair is indeed covered once. Any other $S(2,3,7)$ admits the same reconstruction after naming, giving the isomorphism. $\blacksquare$

#### Lemma Σ.5 (the code is forced to be linear — hence Hamming)

*Under the hypotheses of Lemma Σ.3, $\mathcal{C}$ consists of: $0$; the seven line-vectors; the seven complements of lines; and $\mathbf{1}$. This set is the $\mathbb{F}_2$-span of the lines — a linear $[7,4,3]$ code — and is unique up to coordinate relabeling: the Hamming code $H(7,4)$.*

**Proof.** We work in the binary presentation (any $S(2,3,7)$ may be so labelled, by Lemma Σ.4); lines are $\ell_{a,b} = \{a, b, a \oplus b\}$, i.e. 2-dimensional subspaces of $\mathbb{F}_2^3$ minus $0$.

*Step 1: two lines meet in exactly one point.* Two distinct 2-dimensional subspaces $U, W \leq \mathbb{F}_2^3$ satisfy $\dim(U \cap W) = \dim U + \dim W - \dim(U+W) = 2+2-3 = 1$: exactly one common nonzero point. *(In an abstract $S(2,3,7)$ the same follows from $\lambda = 1$ plus counting.)*

*Step 2: the sum of two lines is the complement of the third line through their meeting point.* Let $\ell, \ell'$ meet at $p$, and let $\ell''$ be the third line through $p$ (Lemma Σ.4: exactly three). The three lines through $p$ partition the six points $\neq p$ into three pairs. Hence, as sets,
$$
\ell \,\triangle\, \ell' \;=\; (\ell \cup \ell') \setminus \{p\} \;=\; \{\text{six points}\} \setminus (\ell'' \setminus \{p\}) \;=\; \overline{\ell''},
$$
so in vector form $\chi_\ell + \chi_{\ell'} = \mathbf{1} + \chi_{\ell''}$, a weight-4 vector. Adding $\chi_{\ell''}$: the sum of the three lines through any point equals $\mathbf{1}$.

*Step 3: the span has dimension exactly 4.* Take $\ell_1 = \{1,2,3\}$, $\ell_2 = \{1,4,5\}$, $\ell_3 = \{2,4,6\}$, $\ell_4 = \{3,4,7\}$. They are independent by a triangular witness: coordinate 5 appears only in $\ell_2$, coordinate 6 only in $\ell_3$, coordinate 7 only in $\ell_4$, and $\ell_1 \neq 0$. The remaining three lines lie in their span — explicitly:
$$
\ell_1 + \ell_2 + \ell_4 = \{2,5,7\}, \qquad
\ell_1 + \ell_2 + \ell_3 = \{3,5,6\}, \qquad
\ell_1 + \ell_3 + \ell_4 = \{1,6,7\}.
$$
So $\dim \mathrm{span} = 4$ and $|\mathrm{span}| = 16$. By Steps 1–2 the span contains $0$, the 7 lines, the 7 complements $\mathbf{1} + \chi_\ell$, and $\mathbf{1}$ — sixteen distinct vectors, i.e. the span is *exactly* this set, with weight distribution $1 + 7x^3 + 7x^4 + x^7$ and minimum weight 3.

*Step 4: the weight census — $\mathcal{C}$ has no words of weight 5 or 6, at most one of weight 7, and its weight-3/4 words are lines and complements only.* We examine each weight class against the constraint $d(c, w) \geq 3$ for the already-forced codewords $w \in \{0\} \cup \{\text{lines}\}$, using $d(c, \chi_\ell) = |c| + 3 - 2\,|{\mathrm{supp}(c) \cap \ell}|$.

- *Weight 3.* If $\mathrm{supp}(c)$ is not a line, pick a pair $\{i,j\} \subset \mathrm{supp}(c)$ and let $\ell$ be the unique line through it (Lemma Σ.3); the third point of $\ell$ is outside $\mathrm{supp}(c)$, so $|\mathrm{supp}(c) \cap \ell| = 2$ and $d(c, \chi_\ell) = 3 + 3 - 4 = 2 < 3$. Hence every weight-3 codeword is a line — all seven are already counted.
- *Weight 4.* The constraint $d \geq 3$ against lines forces $|\mathrm{supp}(c) \cap \ell| \leq 2$ for every line, i.e. $\mathrm{supp}(c)$ **contains no full line**. Count the weight-4 sets containing a line: line + one extra point, $7 \cdot 4 = 28$ sets, all distinct (a 4-set cannot contain two lines, since two lines jointly span $\geq 5$ points by Step 1). So $\binom{7}{4} - 28 = 35 - 28 = 7$ weight-4 sets are line-free — and the seven line-complements are line-free (a line inside $\overline{\ell}$ would be disjoint from $\ell$, contradicting Step 1), so **they are exactly the seven complements**. Weight-4 codewords are therefore complements only.
- *Weight 5.* $\mathrm{supp}(c) = \overline{\{i,j\}}$ for some pair. Lines meeting $\{i,j\}$: three through $i$, three through $j$, minus the one through both — five; hence $7 - 5 = 2$ lines avoid $\{i,j\}$ entirely and lie inside $\mathrm{supp}(c)$, giving $|\cap| = 3$ and $d = 5 + 3 - 6 = 2 < 3$. **No weight-5 codewords.**
- *Weight 6.* Two weight-6 words are complements of singletons $\{i\}, \{j\}$ and differ in exactly $\{i,j\}$: $d = 2 < 3$, so at most **one** weight-6 codeword, say $\overline{\{i\}}$. Against a complement codeword $\overline{\ell}$: $d(\overline{\{i\}}, \overline{\ell}) = d(\{i\}, \ell) = 2$ if $i \in \ell$, else $4$. So a weight-6 word coexists only with complements of the four lines *avoiding* $i$ — capping the weight-4 class at 4.
- *Weight 7.* $\mathbf{1}$ is compatible with everything so far: $d(\mathbf{1}, 0) = 7$, $d(\mathbf{1}, \chi_\ell) = 4$, $d(\mathbf{1}, \overline{\ell}) = 3$.

Now let $a_k$ be the number of weight-$k$ codewords. We have $a_0 = 1$, $a_3 = 7$, $a_5 = 0$, $a_6 \leq 1$, $a_7 \leq 1$, and $\sum_k a_k = 16$ (Lemma Σ.1), so $a_4 + a_6 + a_7 = 8$. If $a_6 = 1$ then $a_4 \leq 4$ and the total is at most $1 + 7 + 4 + 1 + 1 = 14 < 16$ — impossible. Hence $a_6 = 0$, forcing $a_4 + a_7 = 8$ with $a_4 \leq 7$, $a_7 \leq 1$: the only solution is $a_4 = 7$, $a_7 = 1$. **All seven complements and $\mathbf{1}$ are codewords**, and
$$
\mathcal{C} \;=\; \{0\} \,\cup\, \{\text{7 lines}\} \,\cup\, \{\text{7 complements}\} \,\cup\, \{\mathbf{1}\} \;=\; \mathrm{span}\{\text{lines}\}
$$
by Step 3. In particular $\mathcal{C}$ is linear, equal to $\ker H$ in the binary labeling of Lemma Σ.4's reconstruction — the Hamming code. Combined with Lemma Σ.4, this yields (iii): the coordinate permutation aligns the reconstructed Fano plane with the standard one, and the initial translation restores a general origin. *(The same census is the textbook uniqueness proof; cf. MacWilliams–Sloane, Ch. 6.)* $\blacksquare$

#### Lemma Σ.6 (dictionary between the two corpus presentations)

*The relabeling $\sigma:\ 1 \mapsto 2,\ 2 \mapsto 4,\ 3 \mapsto 3,\ 4 \mapsto 6,\ 5 \mapsto 7,\ 6 \mapsto 5,\ 7 \mapsto 1$ carries the cyclic (QR) presentation onto the binary (XOR) presentation: every translate $\{1,2,4\}+t \pmod 7$ maps to a triple $\{a, b, a\oplus b\}$.*

**Proof.** Realize $\mathbb{F}_8 = \mathbb{F}_2[\alpha]/(\alpha^3 = \alpha + 1)$ and read nonzero elements as 3-bit vectors $(c_2 c_1 c_0)$ for $c_2\alpha^2 + c_1\alpha + c_0$:
$$
\alpha^0 = 001,\quad \alpha^1 = 010,\quad \alpha^2 = 100,\quad \alpha^3 = 011,\quad \alpha^4 = 110,\quad \alpha^5 = 111,\quad \alpha^6 = 101 .
$$
Define $\sigma(t) := $ the binary value of $\alpha^{t}$ (indices mod 7, residue 7 read as $t=0$): this is precisely the table above. Multiplication by $\alpha$ is $\mathbb{F}_2$-linear, hence maps 2-dimensional subspaces to 2-dimensional subspaces, i.e. XOR-lines to XOR-lines. The base translate $\{1,2,4\}$ maps to $\{\alpha^1, \alpha^2, \alpha^4\} = \{2, 4, 6\}$, and $2 \oplus 4 = 6$: an XOR-line. Every other translate $\{1,2,4\}+t$ maps to $\alpha^t \cdot \{2,4,6\}$, again an XOR-line. Spot checks: $\{2,3,5\} \mapsto \{4,3,7\}$, $4 \oplus 3 = 7$ ✓; $\{3,4,6\} \mapsto \{3,6,5\}$, $3 \oplus 6 = 5$ ✓. $\blacksquare$

Thus the Γ-canon's cyclic triads and the Gap-dynamics check matrix describe the same grammar; the corpus may use either presentation, and Theorem Σ applies verbatim to both.

#### Lemma Σ.7 (the ladder above: Vasil'ev and van Lint–Tietäväinen)

**(a) Vasil'ev's construction (1962).** *Let $\mathcal{C}$ be a perfect single-error-correcting code of length $n$ with $0 \in \mathcal{C}$, and let $f : \mathcal{C} \to \mathbb{F}_2$ be any function with $f(0) = 0$. Set $\pi(x) := |x| \bmod 2$ and*
$$
V(f) \;:=\; \bigl\{\, (x \oplus y,\; x,\; \pi(x) \oplus f(y)) \;:\; x \in \mathbb{F}_2^{n},\; y \in \mathcal{C} \,\bigr\} \;\subseteq\; \mathbb{F}_2^{2n+1}.
$$
*Then $V(f)$ is a perfect single-error-correcting code of length $2n+1$; it is linear if and only if $f$ is linear on $\mathcal{C}$.*

*Cardinality check:* $|V(f)| = 2^n |\mathcal{C}| = 2^n \cdot 2^{n-r} = 2^{2n-r}$, and $(1 + (2n+1)) \cdot 2^{2n-r} = 2^{r+1} \cdot 2^{2n-r} = 2^{2n+1}$ ✓ — the sphere-packing bound is met with equality, so perfectness reduces to $d \geq 3$, a routine case analysis on the three blocks (see MacWilliams–Sloane, Ch. 6, §"Vasil'ev codes"). For $n = 7$: length 15, $2^{11}$ words. Since there are $2^{15}$ functions $f$ and only $2^{4}$ additive ones, nonlinear choices abound; a nonlinear $V(f)$ is inequivalent to the Hamming $[15,11,3]$ by the following observation:

*Equivalence preserves linearity among codes containing $0$.* If $V' = \tau(V) + a$ is linear for a coordinate permutation $\tau$ and translation $a$, then $0 \in V \Rightarrow a \in V'$, and linearity of $V'$ gives $V' + a = V'$, so $V = \tau^{-1}(V')$ is linear — contradiction. $\blacksquare$

**(b) The classification.** *(van Lint 1971; Tietäväinen 1973; independently Zinoviev–Leontiev 1972.)* *A nontrivial perfect code over an alphabet of prime-power size $q$ has the parameters of a Hamming code ($t = 1$, $n = (q^r - 1)/(q-1)$) or of one of the two Golay codes: binary $[23, 12, 7]$ ($t = 3$) or ternary $[11, 6, 5]$ ($t = 2$).* The proof pivots on Lloyd's theorem: perfectness forces the *Lloyd polynomial* to have $t$ distinct integer roots in $\{1, \dots, n\}$ — an arithmetic constraint so tight that only the listed parameter sets survive. We use the statement as a black box; it seals part (v). $\blacksquare$

Parts (i)–(v) of Theorem Σ now assemble: (i) = Σ.1; (ii) = Σ.2 + Σ.3 + Σ.4 (+ the group of Fano = $\mathrm{PGL}(3,2)$, order $168$, §2); (iii) = Σ.5; (iv) = Σ.7(a) + the doubly-exponential proliferation of inequivalent perfect codes for larger $r$ (same source); (v) = Σ.7(b). $\blacksquare\blacksquare$

#### Remark Σ-QR [Т] {#замечание-qr}

In the classical *systematic* coordinates of $H(7,4)$ — column $j$ of the check matrix is the binary expansion of $j$ — the check positions are those whose column has a single 1: the powers of two, $\{1, 2, 4\}$. But
$$
\{1, 2, 4\} \;=\; \{2^0, 2^1, 2^2\} \;=\; \mathrm{QR}(7),
$$
the quadratic residues modulo 7: indeed $2 \equiv 3^2 \pmod 7$ is the square of a primitive root, so its multiplicative orbit is exactly the index-2 subgroup of squares. Thus the code's check/information split of positions $\{1,\dots,7\}$ is the arithmetic split $\mathrm{QR}(7) \mid \mathrm{QNR}(7) \cup \{7\}$. One and the same three-element set: counts the fermion generations ($N_\mathrm{gen} = |\mathrm{QR}(7)| = 3$ [Т]), generates the Fano lines as a $(7,3,1)$ difference set, and labels the syndrome bits of diagnosis. In the corpus convention the metastructural axes $E, O, U$ carry the checks and the structural axes $A, S, D, L$ carry the information ([Gap dynamics §2.1](/docs/core/dynamics/gap-dynamics#код-хэмминга)); by Lemma Σ.6 the two coordinateizations differ by an explicit relabeling.

## §5. Corollaries {#следствия}

### §5.1. A fourth derivation track for $N = 7$ {#четвёртый-трек}

Until now, seven was derived along three independent tracks: **number** (Hurwitz–Adams: the last normed division algebra $\mathbb{O}$ has $\dim \mathrm{Im}\,\mathbb{O} = 7$), **structure** ($G_2$-rigidity of the coherence grammar at that number), **closure** (the minimality theorem: no proper subset of the seven functional roles closes). Theorem Σ adds a fourth, of an entirely different flavor:

#### Corollary Σ.1 — the diagnosability track [Т]+[И] {#следствие-диагностика}

*If a system must perfectly localize single faults of its own axes (D1–D2), distinguish a nontrivial grammar of global states (D3), and admit no rival grammars (D4) — then the number of axes is seven, and the grammar is the Fano/Hamming one, uniquely.*

Status discipline. The implication is **[Т]** — parts (i)–(iv), proved above with no appeal to algebra, norms, or continuity: nothing enters but counting and sphere packing. The claim that the UHM axes *must* satisfy (D1)–(D4) is the interpretive step **[И]**, and it deserves to be stated carefully rather than smuggled:

- (D1)–(D2) formalize *internal diagnosability of a viable holon*: degradation of an axis must be caught before it cascades through the coherence lattice (this is what Shields I–V protect against), and it must be caught by the system's own reflexive layer — the diagnosis is an act of the $R$-operator, not of an external observer ([self-observation](/docs/consciousness/foundations/self-observation)). Perfectness is precisely "no state about which the grammar is speechless, no state with two conflicting diagnoses".
- (D3) matches the empirical scale of the archetype layer: the Γ-canon's sixteen signatures.
- (D4) is the requirement that the canon be *reconstructible*: any observer, internal or external, recovering the grammar from the system's behavior must arrive at the same sixteen archetypes. Without rigidity, "normal" is a convention and the canon loses its diagnostic authority.

Under these readings, the heptad is not a numerological choice but the unique solution of a well-posed design problem. The track is logically independent of the octonionic one — a hypothetical universe with no division algebras would still be subject to Theorem Σ.

### §5.2. Why above seven one builds a tower, not width {#башня-не-ширина}

#### Corollary Σ.2 [И] {#следствие-башня}

Part (iv) explains a structural choice the corpus has so far treated as a postulate. The hierarchy of subjects ([SAD tower](/docs/consciousness/hierarchy/depth-tower)) scales by **stacking storeys of seven-axis blocks** — $7, 7^{(2)}, \dots$ with the $P_\mathrm{crit}^{(n)}$ rescaling and $\mathrm{SAD}_{\max} = 3$ — rather than by lengthening the axis list to the next Hamming length 15. Theorem Σ supplies the reason. A fifteen-axis "extended psyche" *could* be perfectly diagnosed: $[15,11,3]$ exists. But by Σ.7(a) the grammar at fifteen is no longer unique — nonlinear Vasil'ev grammars share all parameters ($2^{11}$ archetypes, distance 3, perfect tiling) while being inequivalent, and no internal statistic of fault-correction behavior distinguishes them. Diagnosis without a unique grammar is diagnosis without a canon: the system could not certify *which* normality it maintains. Seven is the last level at which "what to repair" and "what counts as normal" are simultaneously and uniquely determined; beyond it, growth must copy the rigid block rather than stretch it.

Open note [Г]: above the whole $t = 1$ ladder there is exactly one more perfect binary rung — Golay's $n = 23$ with $t = 3$. The numerical echo between its correction capacity $t = 3$ and $\mathrm{SAD}_{\max} = 3$ is recorded as a curiosity, with no status, until a structural argument connects the tower height to multi-fault localization.

### §5.3. Weight strata, the sixteen archetypes, and the $G_2$ forms {#весовые-страты}

The grammar $16 = 1 + 7 + 7 + 1$ established in Lemma Σ.5 admits an exceptional-geometric reading [Т]. Recall ([G₂-structure](/docs/physics/gauge-symmetry/g2-structure)) that $G_2 \subset SO(7)$ is the stabilizer of the *associative 3-form* $\varphi = \sum_{\ell} e_i \wedge e_j \wedge e_k$ (one oriented summand per Fano line) with Hodge dual the *coassociative 4-form* $\ast\varphi$ (one summand per line complement).

| Weight | Words | Supports | $G_2$ object | Archetype reading |
|---|---|---|---|---|
| 0 | 1 | $\varnothing$ | vacuum | the null signature |
| 3 | 7 | Fano lines | summands of $\varphi$ | the seven *triads* of the Γ-canon |
| 4 | 7 | line complements | summands of $\ast\varphi$ | the seven *co-triads* |
| 7 | 1 | all axes | volume form $\mathrm{vol}_7$ | full activation |

Explicitly, in the corpus axis order $[A,S,D,L,E,O,U] = [1,\dots,7]$ (binary presentation), the sixteen admissible signatures are:

$$
\varnothing;\quad
\{A{,}S{,}D\},\ \{A{,}L{,}E\},\ \{S{,}L{,}O\},\ \{D{,}L{,}U\},\ \{S{,}E{,}U\},\ \{D{,}E{,}O\},\ \{A{,}O{,}U\};
$$
$$
\text{their seven complements};\quad
\{A{,}S{,}D{,}L{,}E{,}O{,}U\}.
$$

The code's minimum-weight words are the associative triples; their complements the coassociative quadruples. The grammar of admissible profiles and the calendar of $G_2$-calibrations are one structure written in two languages — and by Theorem Σ that structure is not one design option among many, but the unique solution of (D1)–(D4).

## §6. The Σ-compression protocol (T-225): the 21 → 7 → 3 → 1 pyramid {#протокол-сигма}

Full tomography of a state $\Gamma \in \mathcal{D}(\mathbb{C}^7)$ requires $7^2 - 1 = 48$ real parameters ([measurement protocol](/docs/applied/research/measurement-protocol)). For the narrower — and operationally most frequent — task of *localizing a single degraded axis*, Theorem Σ licenses a drastic compression.

#### Σ-compression theorem — T-225 [С] {#t-225}

*Let the coherence dynamics be Fano-compatible ([selection rules](/docs/physics/gauge-symmetry/fano-selection-rules)) and ergodic with spectral gap $\Delta$ (T-114, [evolution](/docs/core/dynamics/evolution)). Then the following monitoring pyramid is sound:*

**(a) 21 → 7 (themes).** The 21 coherences $\mathrm{Coh}_{ij}$ partition **uniquely** into seven line-triples: every axis pair lies on exactly one Fano line — this is the one-theme law, $\lambda = 1$, of Lemma Σ.3. The seven *theme observables*
$$
T_\ell \;:=\; \sum_{\{i,j\} \subset \ell} \bigl|\mathrm{Coh}_{ij}\bigr|^2, \qquad \ell \text{ a Fano line},
$$
constitute the complete content-monitoring layer: no coherence escapes them and none is double-counted.

**(b) 7 → 3 (syndrome).** Binarize each axis status by its viability threshold (the threshold is a convention [О]; the corpus default is the per-axis Gap threshold of [Gap diagnostics](/docs/applied/research/gap-diagnostics)). Three parities of the resulting bits localize any single fault: the *syndrome* $\sigma = (\sigma_1, \sigma_2, \sigma_3) \in \mathbb{F}_2^3$, computed by the rows of $H$, is **the binary address of the damaged axis** — see the table below. The geometry of the three checks is itself Fano-theoretic: the zero-set of each check row is a line ($\{S,L,O\}$, $\{A,L,E\}$, $\{A,S,D\}$ respectively), and these three lines form a **triangle** — three lines with pairwise distinct meeting points $L, S, A$ and no common point. So each check is "parity over the complement of one triangle side". The choice of triangle is exactly the choice of syndrome coordinates: the Fano plane has $\binom{7}{3} - 7 = 35 - 7 = 28$ triangles (35 line-triples minus the 7 concurrent triples, one per point), the group $\mathrm{PGL}(3,2)$ of order $168 = 28 \cdot 6$ acts on them transitively with stabilizer $S_3$ — any triangle serves, and all choices are conjugate.

| Axis | Column of $H$ (binary) | Syndrome $(\sigma_1\sigma_2\sigma_3)$ | Address |
|---|---|---|---|
| $A$ | $001$ | $100$ | 1 |
| $S$ | $010$ | $010$ | 2 |
| $D$ | $011$ | $110$ | 3 |
| $L$ | $100$ | $001$ | 4 |
| $E$ | $101$ | $101$ | 5 |
| $O$ | $110$ | $011$ | 6 |
| $U$ | $111$ | $111$ | 7 |

**(c) 3 → 1 (flag).** The single bit $[\sigma \neq 0]$ is the "fault present" alarm.

**(d) Ergodic reliability.** Under T-114 mixing, the syndrome need not be read from one noisy snapshot. For a persistent fault, average the binarized checks over a trajectory window of length $k$: by spectral-gap concentration for ergodic Markov chains *(Gillman 1993; Lezaud 1998: for a reversible chain with gap $\Delta$ and an observable $|f| \leq 1$, $\ \mathbb{P}\bigl(|\tfrac1k\sum_{t<k} f(X_t) - \pi(f)| \geq \varepsilon\bigr) \leq C\, e^{-c\,k\,\Delta\,\varepsilon^2}$ with absolute $c$ and $C$ depending on the initial distribution)*, each averaged parity settles to its true value with error probability decaying exponentially in $k\Delta$. A window $k \sim \Delta^{-1}$ is already informative; misidentification of the faulty axis decays as $e^{-c k \Delta \varepsilon^2}$ where $\varepsilon$ is the binarization margin.

*Status [С]: (a)–(c) are combinatorics [Т] on top of the binarization model; (d) is standard concentration [Т] granted the T-114 axiomatics; the joint applicability to a live Γ-tomograph is conditional on the measurement model — hence the composite status.*

#### The Lie-algebraic shadow of the pyramid [Т] {#ли-тень}

The pyramid has an invariant meaning inside the coherence algebra. The antisymmetric generators $E_{ij}$ ($1 \leq i < j \leq 7$) span $\mathfrak{so}(7)$, $\dim = 21$ — one generator per coherence. Under the $G_2$ action this space is **not** irreducible; it splits as
$$
\Lambda^2 \mathbb{R}^7 \;=\; \mathfrak{so}(7) \;=\; \mathfrak{g}_2 \,\oplus\, \mathfrak{m}, \qquad 21 = 14 + 7, \qquad \mathfrak{m} \cong \mathrm{Im}\,\mathbb{O},
$$
with an invariant characterization by the operator $\alpha \mapsto \ast(\varphi \wedge \alpha)$ on 2-forms: $\mathfrak{m} = \Lambda^2_7$ is its eigenspace of eigenvalue $+2$, spanned by the contractions $\iota_{e_p}\varphi$, and $\mathfrak{g}_2 = \Lambda^2_{14}$ is the eigenspace of eigenvalue $-1$ *(Bryant; see [G₂-structure](/docs/physics/gauge-symmetry/g2-structure))*. Concretely, $\iota_{e_p}\varphi$ is the signed sum of the three "opposite edges" of the lines through the point $p$ — each axis owns one such combination.

So the 21 coherence directions carry **two canonical grids**: by *lines* — the seven so(3)-triples $\{E_{ij}, E_{jk}, E_{ik}\}_{\{i,j,k\} = \ell}$ feeding the theme observables of layer (a) — and by *points against gauge* — the split $7 \oplus 14$, where the $\mathfrak{g}_2$ part consists of the flows that preserve the grammar $\varphi$ (pure gauge, diagnostically silent) and the $\mathfrak{m}$ part rotates the axes themselves. The protocol monitors themes and parities and provably spends no budget on the 14 gauge directions: they cannot carry single-axis fault information, being $\varphi$-preserving.

#### Reference implementation {#референс-реализация}

The following program verifies, by exhaustive machine check, every finite claim used above: the cardinality $|\mathcal{C}| = 16$, the weight distribution, the identity "weight-3 supports = Fano lines", the one-theme law $\lambda = 1$, and the perfect-decode property (every single-bit corruption of every codeword is localized to the correct axis). It is deterministic and runs in milliseconds.

```python
# sigma_calculus.py — reference implementation of T-224/T-225 (deterministic)
import itertools

AXES = ['A', 'S', 'D', 'L', 'E', 'O', 'U']          # axis a=1..7 <-> bit (7-a): A=MSB
H = [0b1010101, 0b0110011, 0b0001111]                # the H of Gap-dynamics §2:
                                                     # column a = binary of a (row1 = LSB)
LINES = [(1,2,3),(1,4,5),(2,4,6),(3,4,7),(2,5,7),(3,5,6),(1,6,7)]  # a XOR b = c

def syndrome(x):                                     # x: 7-bit status profile
    return tuple(bin(row & x).count('1') & 1 for row in H)

def locate(x):                                       # -> corrupted axis or None
    s = syndrome(x)
    idx = s[0] | (s[1] << 1) | (s[2] << 2)           # syndrome = binary ADDRESS = axis index
    return None if idx == 0 else AXES[idx - 1]

CODE = [c for c in range(128) if syndrome(c) == (0,0,0)]
assert len(CODE) == 16                               # |C| = 16   (T-224 ii)
ws = sorted(bin(c).count('1') for c in CODE)
assert ws == [0]+[3]*7+[4]*7+[7]                     # 1+7+7+1    (§5.3)
supports = {frozenset(i+1 for i in range(7) if c >> (6-i) & 1)
            for c in CODE if bin(c).count('1') == 3}
assert supports == {frozenset(l) for l in LINES}     # weight-3 words = Fano lines
for pair in itertools.combinations(range(1,8), 2):   # one-theme law: λ = 1
    assert sum(set(pair) <= set(l) for l in LINES) == 1
for c in CODE:                                       # perfectness: unique decode
    for i in range(7):                               # flip bit i = corrupt axis 7-i
        assert locate(c ^ (1 << i)) == AXES[6 - i]
print("T-224/T-225 invariants verified: |C|=16, 1+7+7+1, Fano, perfect decode")
```

Output: `T-224/T-225 invariants verified: |C|=16, 1+7+7+1, Fano, perfect decode`.

## §7. The quantum lift: the Steane code as the shadow of Shield I {#квантовый-лифт}

The classical grammar of Theorem Σ is precisely the input demanded by fault-tolerant *quantum* computation. We give the construction in full, since the corpus will lean on it for register realizations.

#### The CSS construction, specialized {#css-конструкция}

**Input data.** A pair of classical linear codes $\mathcal{C}_2^\perp \subseteq \mathcal{C}_1 \subseteq \mathbb{F}_2^n$. The Hamming code supplies the self-dual-containing special case $\mathcal{C}_1 = \mathcal{C}_2 = H(7,4)$: its dual is the simplex code $[7,3,4]$, spanned by the rows of $H$ — and by Lemma Σ.5, Step 2, each row of $H$ (a weight-4 vector, the complement of a triangle side) **is itself a codeword** of $H(7,4)$. Hence $H(7,4)^\perp \subset H(7,4)$: the eight dual words are $0$ and the seven complements.

**Stabilizers.** On $n = 7$ qubits define, for each row $h$ of $H$, two operators:
$$
X^{(h)} := \bigotimes_{i:\,h_i = 1} X_i, \qquad Z^{(h)} := \bigotimes_{i:\,h_i = 1} Z_i .
$$
An $X$-type and a $Z$-type operator commute iff their supports overlap evenly; here $\langle h, h' \rangle = |{\mathrm{supp}(h) \cap \mathrm{supp}(h')}| \bmod 2 = 0$ for all row pairs — the supports $\{A,D,E,U\}, \{S,D,O,U\}, \{L,E,O,U\}$ intersect pairwise in exactly two axes — so the six operators generate an abelian *stabilizer group*.

**Parameters.** The six generators are independent, so the joint $+1$-eigenspace has dimension $2^{7-6} = 2$: **one logical qubit**, $k = n - \mathrm{rk}_X - \mathrm{rk}_Z = 7 - 3 - 3 = 1$. The code distance is the minimum weight of a logical (non-stabilizer) representative, i.e. of a word in $\mathcal{C}_1 \setminus \mathcal{C}_2^\perp = H(7,4) \setminus \{0, \text{7 complements}\} = \{\text{7 lines}, \mathbf{1}\}$ — minimum weight **3**. Result:
$$
\mathrm{CSS}\bigl(H(7,4), H(7,4)\bigr) \;=\; \textbf{the Steane code } [[7,1,3]],
$$
correcting an arbitrary error (bit-flip, phase-flip, or both) on any single qubit; its $X$- and $Z$-syndromes are read by the *same* three Fano parities of §6(b), executed in the two conjugate bases.

**Transversality.** Three classical facts about $H(7,4)$ become three fault-tolerance gifts: (1) self-dual-containment makes the transversal $\mathrm{CNOT}^{\otimes 7}$ preserve the code space (true for every CSS code); (2) $\mathcal{C}^\perp$ has all weights divisible by 4 ($0, 4, 4, \dots$ — *doubly even*), which makes the transversal phase gate $S^{\otimes 7}$ a logical operation; (3) the equality $\mathcal{C}_1 = \mathcal{C}_2$ makes the transversal Hadamard $H^{\otimes 7}$ swap the $X$- and $Z$-stabilizers onto each other. Together: **the entire Clifford group acts transversally** — single faulty gates cannot spread into multi-qubit errors. This is why the Steane code is the canonical workhorse of fault-tolerant architectures.

**Engineering consequence [О].** Any **7-node register** realization of UHM-like coherence dynamics — seven-agent SYNARC/NOEMA cores, or prospective quantum realizations of Γ-dynamics — inherits a fault-tolerance blueprint *with no code-design step*: the stabilizer layout is already dictated by the Fano lines the architecture carries for its selection rules. The grammar selected by Theorem Σ at the classical level is exactly the one quantum fault tolerance requests at its input.

**Honest boundary [О].** For a *single qudit* $\Gamma \in \mathcal{D}(\mathbb{C}^7)$ — one seven-dimensional system rather than a register of seven two-dimensional ones — there is no Steane code: the CSS lift addresses register realizations only. For the qudit itself, the classical layer of T-225 applies (populations, themes, parities), and quantum error correction would require embedding $\mathbb{C}^7$ into a larger register — a design question deliberately left open here.

## §8. The Σ-Mor bridge: diagnostic pairs and MSFS grading {#мост-msfs}

The shape that organizes this whole document — *an invariant subset together with a graded distance to it, non-increasing along admissible morphisms, whose zero level is exactly the invariant subset* — has already appeared once in the ecosystem, in a very different habitat: the **intensional grading** of MSFS (paper §8.1). There, inside each intensional fiber $\mathrm{Int}([F])$ over a point of the moduli stack $\mathfrak{M}$, every display datum $d$ carries the grade $\mathrm{gr}(d) = \min\{n : d \in \mathcal{D}_F^{(n)}\}$ — the stage of the generating induction at which it appears — with three proved properties: the filtration is exhaustive; the grade does not increase under pullback along $\mathbb{I}(f)$; grade 0 is exactly the equivalences ("extensionality is grade-blindness").

**Definition Σ.2 [О] (diagnostic pair).** A *diagnostic pair* on a class $\mathcal{X}$ with admissible morphisms is a pair $(\mathcal{C}, d)$: a subclass $\mathcal{C} \subseteq \mathcal{X}$ and a functional $d : \mathcal{X} \to \mathbb{N}$ such that (i) $d^{-1}(0) = \mathcal{C}$; (ii) the sublevels $\{d \leq n\}$ filter $\mathcal{X}$ exhaustively; (iii) $d$ does not increase along admissible morphisms. The pair has *perfect localizability* if every $x$ with $d(x) = 1$ admits a unique "repair" — a distinguished $c(x) \in \mathcal{C}$ — and the repair balls $\{x : d(x) \leq 1,\ c(x) = c\}$ partition the level $\{d \leq 1\}$.

Two realizations, now side by side:

| | $(\mathcal{C}, d)$ | admissible morphisms | non-increase | collapse statement |
|---|---|---|---|---|
| UHM / codes | $\bigl(H(7,4),\ d_{\mathrm{Hamming}}(\,\cdot\,, \mathcal{C})\bigr)$ on $\mathbb{F}_2^7$ | Fano-compatible dynamics | code-preserving flows do not create faults | gauge sees only the code subspace |
| MSFS | $\bigl(\text{equivalences},\ \mathrm{gr}\bigr)$ on the fiber $\mathrm{Int}([F])$ | pullback along $\mathbb{I}(f)$ | prop. grading (b) | "extensionality is grade-blindness" |

The axioms (i)–(iii) are literally the clauses of the MSFS grading proposition; the code instance satisfies them by construction and — this is the content of Theorem Σ — enjoys perfect localizability precisely because of its Fano base. Whether the *converse* transfer holds is the natural next question:

**Conjecture Σ-Mor [Г].** *A fiber $\mathrm{Int}([F])$ admits perfect localizability of equivalence defects, in the sense of Definition Σ.2, if and only if the canonical minimal display class $\mathcal{D}_F$ is Fano-presentable: generated, at stage one of its inductive construction, by a seven-element incidence base with $\lambda = 1$.*

*Route to a proof:* match the generating stages $\mathcal{D}_F^{(n)}$ with the ball filtration of a code metric and apply Lemma Σ.1 to the stage-one base — perfectness of the repair tiling should force the $2^r - 1$ arithmetic on the base, and (D3)-nontriviality of a genuinely intensional fiber should then force $r = 3$ via Lemma Σ.2. *Route to a refutation:* exhibit a fiber with perfect localizability over a stage-one base of cardinality $\neq 2^r - 1$ — a single counterexample kills the arithmetic. Either outcome is informative; the conjecture is registered as a candidate for new Diakrisis N.T entries (correspondence document, "import opportunity").

## §9. Falsifiability and technological consequences {#следствия-технологии}

**Prediction Σ-P1 (candidate for the Pred registry).** In Γ-tomography data, single-axis perturbations must produce **only** the seven nonzero syndrome patterns, distributed with the $\mathrm{PG}(2,2)$ geometry of the table in §6(b). A stable syndrome statistic violating the linear structure — e.g. a persistent parity pattern incompatible with every column of $H$ under the single-axis model, or pairwise check correlations breaking the triangle geometry — falsifies the Fano grammar of the dynamics. Notably, this test is *independent of the octonionic track*: it probes the combinatorial grammar directly, with three binary observables.

**Technology package.**

1. **Monitoring budget [С].** Fault localization: 3 binary aggregates instead of 48-parameter tomography — a sixteenfold reduction in observable count, and the three parities are *global* (each sums four axes), hence robust to per-axis noise by (d) of T-225. Content monitoring: 7 theme observables instead of 21 coherences. Direct cost reduction for the Γ-tomograph and for the diagnostic tiers of the Γ-canon П-protocols.
2. **Fault-tolerant seven-agent cores [О].** The Steane blueprint of §7 for register realizations: transversal Cliffords mean the core's basic operations do not multiply single faults; the stabilizer layout is inherited from the selection rules for free.
3. **Syndrome audit of corpora [О].** Assign each of the seven UHM dimensions its cluster of corpus claims; binarize cluster health (all claim-sites consistent / at least one broken); three parities over the seven bits localize "which cluster hides the inconsistency" without reading the whole corpus. The reference implementation of §6 applies verbatim — the corpus becomes an instance of its own theorem.
4. **Rigidity as a design criterion [О].** Part (iv) of Theorem Σ is an argument *against* widening the axis list in NOEMA-like cognitive architectures: above seven, the diagnostic grammar loses canonicity, and two independently trained instances may converge to inequivalent "normalities" that no internal test distinguishes. Scale by towers of rigid seven-blocks (consistent with $\mathrm{SAD}_{\max}$), not by wider single levels.

## §10. Status summary {#сводка}

| Claim | Status |
|---|---|
| Theorem Σ (T-224), parts (i)–(v); Lemmas Σ.1–Σ.7 | **[Т]** |
| Remark Σ-QR (check positions = QR(7)); dictionary Lemma Σ.6 | **[Т]** |
| Corollary Σ.1: the diagnosability track for $N=7$ | **[Т]** mathematics + **[И]** identification |
| Corollary Σ.2: "tower, not width" | **[И]** (rests on (iv) [Т]) |
| Weight strata ↔ $(\varphi, \ast\varphi)$; 16-archetype table | **[Т]** |
| T-225: Σ-compression, the 21→7→3→1 pyramid | **[С]** |
| Lie shadow: $21 = 14 + 7$, eigenvalue characterization | **[Т]** (diagnostic reading — [И]) |
| Steane $[[7,1,3]]$ = CSS of Shield I; transversal Cliffords | **[Т]** mathematics; **[О]** engineering |
| Conjecture Σ-Mor | **[Г]** |
| Golay $t=3$ ↔ $\mathrm{SAD}_{\max}=3$ | curiosity, **[Г]** note |

## Where this leads {#куда-ведёт}

- [Gap dynamics §2](/docs/core/dynamics/gap-dynamics#код-хэмминга) — the forward direction: the isomorphism $\mathrm{PG}(2,2) \cong H(7,4)$ at the level of Lindblad operators.
- [Topological protection, Shield I](/docs/applied/coherence-cybernetics/topological-protection#код-хэмминга) — the five shields; Σ turns Shield I from a property into a selector.
- [Minimality of N=7](/docs/proofs/minimality/theorem-minimality-7) and the [octonionic derivation](/docs/proofs/minimality/theorem-octonionic-derivation) — the three prior tracks; §9.3 there tabulates Track Σ against Tracks A and B.
- [Γ-canon](/docs/applied/research/gamma-canon) — the sixteen archetypes as codewords; the Σ protocol adds the diagnostic tier to the П-protocols; Lemma Σ.6 is the dictionary between its cyclic triads and the binary presentation.
- [Fano selection rules](/docs/physics/gauge-symmetry/fano-selection-rules), [evolution / T-114](/docs/core/dynamics/evolution) — the dynamical premises of T-225(d).
- [G₂-structure](/docs/physics/gauge-symmetry/g2-structure) — the forms $\varphi, \ast\varphi$ and the $14 \oplus 7$ split behind §6.
- [Status registry](/docs/reference/status-registry) — rows T-224, T-225.
- MSFS §8.1 (Intensional Grading) and the Diakrisis correspondence document — the Σ-Mor bridge, conjecture [Г].
