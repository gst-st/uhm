---
sidebar_position: 9
title: "Σ-calculus: the diagnosability rigidity of seven"
description: "A self-contained mathematical treatment. Theorem Σ (T-224): perfect single-fault diagnosability, a nontrivial state grammar and structural rigidity select n = 7 uniquely — a fourth independent derivation track for N = 7, using only sphere packing and design counting. Full proofs: Steiner reconstruction, uniqueness of S(2,3,7), forced linearity, Vasil'ev breakage at n = 15, the van Lint–Tietäväinen ladder. The Σ-compression protocol (T-225): the 21 → 7 → 3 → 1 measurement pyramid with its Lie-algebraic shadow so(7) = g₂ ⊕ Im O. The Steane code [[7,1,3]] as the quantum lift of Shield I, with the complete CSS construction. The Σ-Mor bridge to MSFS intensional grading."
---

# Σ-calculus: the diagnosability rigidity of seven

> *A structure that must diagnose its own single faults perfectly, must distinguish more than two global states, and must not admit rival grammars — has no freedom left: it is the Fano plane on seven axes. Diagnosability is not a bonus feature of the heptad; it is a selector of the heptad.*

:::tip Document status
The core is **Theorem Σ (T-224) [Т]**: classical mathematics — perfect codes, the reconstruction of the Steiner system $S(2,3,7)$, uniqueness of the length-7 perfect code, Vasil'ev's nonlinear codes, the van Lint–Tietäväinen classification. Every proof is given in full, as a chain of numbered lemmas; external results are quoted with exact statements. The identification of UHM axes with diagnosable status bits is **[И]**. The Σ-compression protocol (T-225) is **[С]** (conditional on the measurement model). The Σ-Mor bridge into MSFS is an **[О]** axiomatization plus a **[Г]** conjecture — repaired and sharpened 2026-07-11 (§8-progress): refuted as literally stated at the pair level, proved conditionally as T-229. §7a (T-227) and §8a (T-228) resolve the two quantum/federation open problems. All statuses are marked in place.
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

**Honest boundary [О].** For a *single qudit* $\Gamma \in \mathcal{D}(\mathbb{C}^7)$ — one seven-dimensional system rather than a register of seven two-dimensional ones — there is no Steane code: the CSS lift addresses register realizations only. For the qudit itself, the classical layer of T-225 applies (populations, themes, parities), and quantum error correction would require embedding $\mathbb{C}^7$ into a larger register — a design question resolved in §7a below.

### §7a. The protected qudit: the address embedding and the extremal finite symmetry {#защищённый-кудит}

In plain words, the problem is this: §7 protects a *register* of seven two-level nodes, but the UHM state $\Gamma$ lives on one *seven-level* system — a different animal, and no code was on offer for it. The resolution is to give each axis a three-bit binary name. Then the qudit becomes three qubits minus one unused state, the three Fano parities turn into literal address bits, and protecting the qudit reduces to protecting three qubits — which the Steane code of §7 does canonically. What is spent (one extra state), what is gained (full distance-3 protection), and how much symmetry survives (the largest amount any code allows) — the theorem below answers all three exactly.

The construction starts by giving the qudit that *binary address*. Identify the seven axes with the nonzero vectors of $\mathbb{F}_2^3$ (the binary presentation of Lemma Σ.6) and embed

$$
\mathbb{C}^7 \;=\; \mathrm{span}\{\,|x\rangle : x \in \mathbb{F}_2^3\setminus 0\,\} \;\subset\; (\mathbb{C}^2)^{\otimes 3},
$$

the orthogonal complement of $|000\rangle$ in three qubits. Two structural gifts arrive immediately [Т]:

1. **The parities are the $Z$'s.** $\langle x|Z_b|x\rangle = (-1)^{x_b}$: the three Fano parities of §6(b) *are* the three single-qubit $Z$ operators, and the full parity group $\{Z_v = \mathrm{diag}((-1)^{v\cdot x})\}$ is a diagonal $2^3$ whose sign patterns are exactly the simplex codewords. The syndrome measurement of T-225 is a $Z$-basis address readout, verbatim.
2. **Polarity is addition.** Lines are the $2$-dimensional subspaces minus zero, and the third point of a pair is its sum: $\pi(x,y) = x \oplus y$ — the octonionic triple structure in address form.

#### Theorem T-227 [Т] — the protected qudit and its extremal symmetry {#t-227}

**(i) Protection.** Encoding the three address qubits into three Steane blocks yields a $[[21,3,3]]$ register protection of the qudit: any single physical-qubit fault is corrected, and the Fano parities become the logical $\bar Z_v$ — measured transversally, block by block.

**(ii) The monomial symmetry, computed.** The monomial (signed-permutation) stabilizer of the associative $3$-form $\varphi$ has order exactly $1344 = 2^3 \cdot 168$: *every* one of the $168$ collineations of the Fano plane lifts to a $\varphi$-preserving signed permutation (with exactly $8$ sign choices each), the diagonal subgroup is the simplex $2^3$ of item 1, and every element has determinant $+1$ — so the whole group lies in compact $G_2$, the stabilizer of $\varphi$ in $\mathrm{GL}(7,\mathbb{R})$. The extension $2^3 \cdot \mathrm{PGL}(3,2)$ is **non-split**: an exhaustive search over all $5376$ Hurwitz pairs (an involution and an order-$3$ element with product of order $7$ — every copy of the Hurwitz group $\mathrm{PSL}(2,7)$ must contain one) finds no complement. This is the octonion coordinate-frame group of the literature, re-derived and certified computationally here.

**(iii) Transversal realization, computed.** On the $[[21,3,3]]$ code every element of $2^3\cdot\mathrm{PGL}(3,2)$ acts as a *transversal logical Clifford*: the collineation part is a CNOT circuit on the three logical qubits ($\mathrm{GL}(3,2)$ is generated by transvections $=$ CNOTs, and inter-block CNOT is transversal for CSS codes), and the sign part is a diagonal layer of algebraic degree $\leq 2$ over $\mathbb{F}_2$ — computed profile: $21$ collineations need degree $0$ (logical Pauli $\bar Z$ / global sign), $147$ need degree exactly $2$ (logical $\overline{CZ}$-layers, transversal for Steane), and **none needs degree $3$** — no $CCZ$, which would have broken transversality.

**(iv) Extremality.** By Eastin–Knill, the transversally realizable logical group of an error-detecting code is finite — no code protects a *continuous* subgroup of $G_2$. In the classification of maximal finite subgroups of $G_2$ (Cohen–Wales; Griess), $2^3\cdot\mathrm{PSL}(3,2)$ is maximal; hence the construction of (iii) realizes **the largest protectable octonion-frame symmetry any quantum code can offer**. The design question of the honest boundary closes at its theoretical optimum.

*Status.* (i)–(iii) **[Т]**: exact integer arithmetic, exhaustive searches stated as such, plus standard CSS facts; the maximality citation in (iv) is external mathematics, the Eastin–Knill step standard. Engineering readings **[О]**. Resolves open problem (i) of the SYNARC specification, Appendix K (v2.0).

**Remark (the price and the dividend of the eighth state) [И].** $\log_2 7$ is not an integer: binary addressing costs one extra basis state $|000\rangle$. The construction turns the cost into semantics: $|000\rangle$ is the natural *no-axis flag* — the unique address with zero syndrome under all three parities — and its exclusion from the qudit is precisely the (D3)-nontriviality of the grammar. The federation construction of §8a spends the analogous eighth *coordinate* as the organism's bus.

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

#### Progress (2026-07-11): the bridge repaired and sharpened {#мост-починка}

The route programme has been executed, with an instructive twist: **the conjecture as literally stated is false at the level of abstract diagnostic pairs, and the repair identifies the missing hypothesis — which turns out to be MSFS's own open collapse-stage invariant.**

**Definition Σ.3 [О] (base-coordinatized fiber; the Σ-FIB chart).** A fiber $\mathrm{Int}([F])$ is *base-coordinatized* if there is a finite stage-one base $B$ and a surjective chart $\sigma$ of the finitely-graded part onto $\mathbb{F}_2^B$ such that: **(F1)** $\mathrm{gr}(d) = d_{\mathrm{Hamming}}\bigl(\sigma(d), \sigma(\mathcal{C})\bigr)$ — the grade is the code distance to the equivalences; **(F2)** grade-one data correspond bijectively to single coordinate flips; **(F3)** $|\sigma(\mathcal{C})| \geq 2$ — the (D3) of §3, transported.

**Observation 1 [Т] (the literal biconditional fails for pairs).** Under a chart, perfect localizability in the sense of Definition Σ.2 says exactly $d_{\min}(\sigma(\mathcal{C})) \geq 3$: radius-one repair balls around distinct code points are disjoint iff the minimum distance is at least three, and they always cover the level-$\leq 1$ set — which is all that Definition Σ.2 quantifies over. *Any* code of minimum distance $\geq 3$, over a base of *any* size, therefore yields a diagnostic pair with perfect localizability — a $[5,1,5]$-type display geometry gives it over a five-element base. Perfect localizability alone does **not** force the $2^r - 1$ arithmetic: the sphere-packing *equality* needs the repair balls to tile the whole fault space, not merely the first level.

**Observation 2 [Т] (the missing hypothesis is the collapse stage).** Under (F1) the grade filtration is the ball filtration of the code metric, so it stabilizes exactly at the covering radius:

$$
n_0(F) \;=\; \rho_{\mathrm{cov}}\bigl(\sigma(\mathcal{C})\bigr)
$$

— the minimal collapse stage of MSFS §8.1 (its open question (i)) *is* the covering radius of the display code. And "repair balls tile the fault space" is precisely *packing radius $=$ covering radius $= 1$*: perfectness equals localizability **plus collapse at stage one**.

#### Theorem Σ-Mor′ — T-229 [Т при Σ-FIB] {#t-229}

*For a base-coordinatized fiber (F1–F3): perfect localizability of equivalence defects together with grade collapse at stage one holds **iff** $\sigma(\mathcal{C})$ is a perfect $1$-error-correcting code. By Lemma Σ.1 this forces $|B| = 2^r - 1$; under the nontriviality and rigidity clauses of Theorem Σ (Lemmas Σ.2 and Σ.5 applied to the chart) $r = 3$: the stage-one base has seven elements with the Fano incidence — $\mathcal{D}_F$ is Fano-presentable. Conversely, Fano-presentability transports $H(7,4)$ along the chart and yields both clauses ($d_{\min} = 3$, $\rho_{\mathrm{cov}} = 1$).*

**What remains of Σ-Mor [Г].** Over genuine MSFS fibers the original conjecture is now the conjunction of two sharper questions (labelled **ΣQ1/ΣQ2** to avoid collision with the MSFS paper's own open questions Q1–Q5): **(ΣQ1)** does genuine intensionality ($\tau$-nontriviality in the sense of MSFS Theorem I-existence, Step 7) force the Σ-FIB chart? **(ΣQ2)** does it force the stage-one collapse $n_0(F) = 1$? A refutation must break ΣQ1 or ΣQ2 — the coding arithmetic is closed by T-229. **Payoff for MSFS:** the identity $n_0(F) = \rho_{\mathrm{cov}}$ gives the collapse-stage invariant of MSFS open question (ii) a coding-theoretic meaning — foundations with the same binary invariant $\tau$ are separated by the covering radius of their display geometry, and Fano-presentable fibers sit at the extremal value $n_0 = 1$: *perfect normal-form geometry*, every finitely-graded display datum one repair away from an equivalence.

#### The four-rung scale and the internal no-go {#четыре-ступени}

Two further theorems close most of the remaining slack around ΣQ1/ΣQ2.

**Theorem T-230 [Т при Σ-FIB+F4] (the four-rung collapse).** *Call a chart **homomorphic** if, in addition to (F1)–(F3), **(F4)** it carries composition to XOR and is composably full: every pair of chart values is realized by a composable pair of display data whose composite realizes the sum. Then:*

**(a)** *(forced linearity)* $\sigma(\mathcal{C})$ is a linear code: composites of equivalences are equivalences, so the code is closed under realized sums — the chart-level echo of Lemma Σ.5.

**(b)** *(exact law)* *The MSFS composition law $\mathrm{gr}(d_2 \circ d_1) \leq \max(\mathrm{gr}\,d_1, \mathrm{gr}\,d_2) + 1$ holds in the chart **iff** $\rho_{\mathrm{cov}}(\sigma(\mathcal{C})) \leq 3$.* For $\rho_{\mathrm{cov}} \geq 4$, a deep hole $z = c + e_{i_1} + \cdots + e_{i_\rho}$ splits as $z = x \oplus y$ with $\max(\mathrm{gr}\,x,\, \mathrm{gr}\,y) \leq \lceil \rho/2 \rceil \leq \rho - 2$ — violating the law; for $\rho_{\mathrm{cov}} \leq 3$ the law follows by cases from translation invariance: at $\max \leq 1$, $d(x{\oplus}y) \leq d(x) + d(y) \leq 2$; at $\max \geq 2$, $d(x{\oplus}y) \leq \rho_{\mathrm{cov}} \leq 3 \leq \max + 1$.

**(c)** *(four rungs)* *Since the composition law is a theorem of the MSFS grading, every homomorphically charted fiber has*
$$
n_0(F) \;=\; \rho_{\mathrm{cov}} \;\leq\; 3 :
$$
*the intensional tower collapses by stage three, and the Morita-refinement scale is **four-valued**, $n_0 \in \{0, 1, 2, 3\}$ — grade-blind; perfect (Fano-type) normal-form geometry; intermediate; maximal depth. The bound is tight: the Golay display geometry of §8a has $\rho_{\mathrm{cov}} = 3$ and satisfies the law (verified directly), so the top rung is realized.* For the charted case this answers both MSFS grading-remark questions: strictness (question (i)) always fails by stage three, and the refinement invariant beyond $\tau$ (question (ii)) is a two-bit quantity, with the Hamming and Golay geometries at the two nontrivial extremes ($n_0 = 1$ and $n_0 = 3$).

In plain words: the *covering radius* of a code is the distance from the worst-placed point of the space to its nearest codeword — here, the number of elementary repairs separating the most defective display datum from an equivalence. The theorem says this number can only be $0$, $1$, $2$ or $3$ for any homomorphically charted foundation, and each rung has a concrete witness:

| rung $n_0$ | witness geometry | what it means for the fiber |
|---|---|---|
| $0$ | the full code $\mathbb{F}_2^B$ | grade-blind: every display datum is already an equivalence — purely extensional geometry |
| $1$ | Hamming $H(7,4)$ / Fano | perfect normal form: every datum is one repair from an equivalence, uniquely (T-229) |
| $2$ | repetition $[5,1,5]$ | localizable but not perfect — the counterexample geometry of Observation 1 |
| $3$ | Golay $[23,12,7]$ | maximal intensional depth; the federation geometry of §8a, and the bound is attained |

**Theorem T-231 [Т] (internal-chart no-go).** *If equivalence-hood of display data in $\mathrm{Int}([F])$ is not decidable internally to $\mathrm{Eff}$, the fiber admits no $\mathrm{Eff}$-internal Σ-FIB chart with its finite code given: a computable $\sigma$ would decide $\mathrm{gr}(d) = 0 \Leftrightarrow$ "$d$ is an equivalence" (compute $\sigma(d)$, compare against the finite code).* **Instantiation [С]:** for $F = \mathsf{ETT}$ — where conversion is undecidable by the reflection rule, the same fact behind $\tau(\mathbb{I}(\mathsf{ETT})) = 0$ in MSFS Step 7 — every Σ-FIB chart is necessarily external. **Corollary [И]:** the Σ-Mor programme bifurcates constructively. *Internal* syndromic diagnosability of intensional defects is a privilege of normalizing display geometries ($\tau = 1$); a non-normalizing fiber may be charted classically, but its own inhabitants cannot run the diagnosis. This settles the internal reading of ΣQ1 negatively for $\tau = 0$ fibers: diagnosability is not just an arithmetic of bases — it is a constructive resource.

**Where ΣQ2 now stands.** At the chart level the question is settled *negatively, and definitively*: both the repetition geometry $[5,1,5]$ (rung $2$) and the Golay geometry $[23,12,7]$ (rung $3$) satisfy **all** the chart axioms including homomorphy — their covering radii are $2$ and $3$, so the $\max{+}1$ law holds — and both enjoy perfect localizability ($d_{\min} \geq 3$) without being Fano-presentable. So a fiber-level proof of Σ-Mor, if one exists, cannot come from the chart geometry: it must show that *genuine intensionality itself* excludes rungs $2$ and $3$ — which is exactly ΣQ2, now isolated as the entire remaining content of the conjecture. **Refutation programme [Г]:** the natural candidate for a genuine rung-$3$ fiber is a *federated foundation* — three Fano-presentable foundations coupled through a shared gauge word, whose display classes mix by the Turyn sum of §8a; if such a $2$-categorical federation can be constructed with (F1)–(F4) verified, fiber-level Σ-Mor is refuted by exhibition. Either outcome is decisive: a proof of ΣQ2 would reveal an unexpected rigidity of intensionality; a federated counterexample would show that the intensional world genuinely contains multi-organism display geometries.

#### The strictness dichotomy and the canonical repair (T-233) {#строгостная-дихотомия}

One structural question underlies both ΣQ1 and ΣQ2, and it can be answered now: *where do positive grades come from at all?* The generating induction produces new display data by three operations — $2$-pullback, composition, $2$-cell transport — starting from equivalences. Whether anything of grade $\geq 1$ ever appears depends entirely on how "$2$-pullback" is read.

**Theorem T-233 [Т] (strictness dichotomy; the fault alphabet; the canonical repair).**

**(a) Bicategorical collapse.** *If the generating operations are read bicategorically — pullbacks as bipullbacks, transport along invertible $2$-cells — then all three preserve equivalences: composites of equivalences are equivalences, a datum isomorphic to an equivalence is one, and the bipullback of an equivalence along* **any** *morphism is an equivalence (a standard bicategorical fact). Hence $\mathcal{D}_F^{(n)} = \mathcal{D}_F^{(0)}$ for all $n$: the grading is identically zero, $n_0(F) = 0$ for every foundation, and the Σ-Mor hypotheses never engage. The intensional grading is invisible to the bicategorical eye — it is a* **strictness artifact** *in the precise sense that it measures phenomena a homotopy-invariant reading cannot see.* (Consistency check: MSFS's own MLTT/ETT separation at finite stages survives, because it is carried by the normalization invariant $\tau$, which is defined on the data themselves, not on their grades.)

**(b) The fault alphabet, strictly.** *In the strict reading the situation changes at exactly one point: the* strict *pullback of an equivalence along $f$ is an equivalence whenever $f$ is an isofibration (representably: strict pullbacks of isofibrations are bipullbacks — the classical fact that isofibrations are the fibrations of the canonical model structure on $\mathbf{Cat}$, transported along representables $K(X,-)$ to any strict $2$-category with strict pullbacks), and can fail to be one otherwise. Composition and invertible transport still preserve equivalences. Hence every grade-$1$ display datum is a strict pullback $f^*e$ of an equivalence along a non-isofibration:* **single intensional defects are exactly failures of fibrancy**, *and the stage-one base of any would-be chart must enumerate independent fibrancy-failure directions.*

**(c) The canonical repair.** *Every grade-$1$ datum comes with a repair candidate it did not have to be given: the comparison to the bipullback. For $d = f^*e$ there is a canonical $1$-morphism over the base from the strict pullback to the pseudo-pullback, and the pseudo-pullback projection* **is** *an equivalence by (a). Setting $c(f^*e) := $ the pseudo-pullback projection defines a repair operator on the whole grade-$1$ layer — existence and canonicity are free; what Definition Σ.2's perfect localizability adds is precisely* uniqueness *and the partition property of this operator's fibers.*

*Proof.* (a) Composition and invertible transport are immediate; bipullback-stability of equivalences is standard (an equivalence is precisely a morphism all of whose bipullbacks exist and are equivalences in the representable sense). The induction therefore never leaves grade $0$, and the minimal display class containing the equivalences and closed under the three operations is the equivalences. (b) Representably: for each $X$, $K(X, -)$ sends a strict pullback square to a strict pullback in $\mathbf{Cat}$ and an isofibration to an isofibration (this is the representable definition); in $\mathbf{Cat}$, strict pullbacks along isofibrations are bipullbacks, so the pulled-back equivalence is an equivalence; conversely nothing protects a strict pullback along a general $f$. Data produced by composition or transport from grade-$\leq 0$ material stay at grade $0$, so the only entrance to grade $1$ is a fibrancy failure. (c) The comparison morphism from the strict to the pseudo-pullback is part of the universal property of the latter; the pseudo-projection is an equivalence by (a). $\blacksquare$

**What this does to ΣQ1 ∧ ΣQ2 [И].** The two questions become concrete:

- **ΣQ1′.** *Do the fibrancy-failure directions of a genuine foundation form a finite independent base — so that recording "which failures occurred" is a chart onto $\mathbb{F}_2^B$?* T-231 already bounds the constructive side: for $\tau = 0$ fibers any such chart is external. T-233(b) now says what the chart must count.
- **ΣQ2′.** *Is every finitely-graded display datum* one canonical repair *away from an equivalence — i.e., does the operator of (c), iterated, terminate in a single step?* The four-rung scale (T-230) bounds how badly this can fail under homomorphic charts: by at most two further repairs.

And the type-theoretic paradigm case acquires a face: $\mathsf{ETT}$'s equality reflection is the maximal *strictification* — it collapses the judgmental/propositional distinction that fibrancy failures measure — which is why the same foundation is both the $\tau = 0$ pathology of T-231 and the natural habitat of nontrivial grades. Intensionality, in this geometry, is the refusal to strictify; its defects are fibrancy failures; and its diagnosability is the question of whether those failures admit a finite parity grammar. That is Σ-Mor, restated with every term now carrying a categorical definition.

#### The product obstruction: superposition collapses the tower (T-234) {#препятствие-произведений}

Armed with the fault alphabet, one can now *compute* in explicit ambient $2$-categories — and the first computation decides ΣQ2′ on a large natural class.

**The toy that shows the mechanism.** Work in $\mathbf{Cat}^B$, the strict $2$-category of $B$-indexed families of categories, with the three protagonists $\varnothing$ (empty), $\mathbf{1}$ (terminal), $\mathbb{I}$ (the walking isomorphism $0 \cong 1$). The elementary fibrancy failure of T-233(b) is classical: pulling back the equivalence $\mathbf{1} \xrightarrow{\,0\,} \mathbb{I}$ along the non-isofibration $\mathbf{1} \xrightarrow{\,1\,} \mathbb{I}$ gives the *strict* pullback $\varnothing \to \mathbf{1}$ — the objects would have to satisfy $0 = 1$ on the nose, and none do. One defect, one coordinate. Now take **two** coordinates and pull back the *diagonal* equivalence $(\mathbf{1},\mathbf{1}) \xrightarrow{(0,0)} (\mathbb{I},\mathbb{I})$ along $(\mathbf{1},\mathbf{1}) \xrightarrow{(1,1)} (\mathbb{I},\mathbb{I})$: the result is $(\varnothing,\varnothing) \to (\mathbf{1},\mathbf{1})$ — a **two-defect datum produced by a single stage-one pullback**, literally equal to the product of the two one-defect data. Defects *superpose*: wherever the ambient can form products of pullback squares, a single generating step exhibits any finite set of elementary defects simultaneously.

**Theorem T-234 [Т при Σ-FIB + F4× + (P)] (superposition collapse).** *Let a fiber carry a chart satisfying (F1)–(F3), let* **(F4×)** *extend homomorphy to fiber products ($\sigma(d_1 \times_F d_2) = \sigma(d_1) \oplus \sigma(d_2)$ whenever the product exists), and let* **(P)** *hold: the slice admits binary $2$-products (equivalently, the ambient has the corresponding strict pullbacks over $F$ — the same species of limit the display induction already quantifies over). Then:*

**(i)** *Every label is realized at stage one: for $x \in \mathbb{F}_2^B$ write $x = \sum_{b \in \mathrm{supp}(x)} e_b$; the single-flip data $d_b$ exist by (F2), and the iterated fiber product $D_x := \times_{b \in \mathrm{supp}(x)} d_b$ is again a pullback of an equivalence — a product of pullback squares is a pullback square of the products, and a product of equivalences is an equivalence — hence $\mathrm{gr}(D_x) \leq 1$, while $\sigma(D_x) = x$ by (F4×).*

**(ii)** *Consequently $d_H(x, \sigma(\mathcal{C})) = \mathrm{gr}(D_x) \leq 1$ for every $x$: the display code has covering radius $\leq 1$, i.e. $n_0(F) \leq 1$ —* **the stage-one collapse hypothesis of T-229 is not an assumption but a consequence of product-closure.**

**(iii)** *If moreover the fiber has perfect localizability ($d_{\min} \geq 3$), then packing radius $\geq 1$ and covering radius $\leq 1$ force a* **perfect** *single-error-correcting code; Lemma Σ.1 gives $|B| = 2^r - 1$, and the (D3)/rigidity clauses give $r = 3$:* **fiber-level Σ-Mor is true on the product-closed class** *— ΣQ2′ is resolved positively there, and the entire remaining content of the conjecture on that class is ΣQ1′ (the existence of the chart).*

*Proof.* (i) Products of strict pullback squares are strict pullback squares of the product cospans (limits commute with limits); products of equivalences are equivalences (the quasi-inverse and the invertible $2$-cells are built componentwise through the $2$-universal property); iterating the binary case keeps the datum inside "one pullback of one equivalence". If $x \notin \sigma(\mathcal{C})$ the datum is not an equivalence by (F1), so its grade is exactly $1$. (ii) Immediate from (F1). (iii) $d_{\min} \geq 3$ makes radius-$1$ balls disjoint; $\rho_{\mathrm{cov}} \leq 1$ makes them cover; equality is perfection, and the arithmetic is Theorem Σ's. $\blacksquare$

**Corollary (quarantine of the upper rungs) [Т]+[И].** The rung-$2$ and rung-$3$ geometries of the four-rung scale — the repetition $[5,1,5]$, the Golay $[23,12,7]$, everything above $n_0 = 1$ — **cannot occur in any product-closed fiber**. Multi-fault intensional geometry requires *product obstruction*: an ambient in which some fiber products over $F$ fail to exist, so that defects cannot superpose freely. The federated-foundation programme is thereby sharpened from a hope to a specification: a genuine rung-$3$ fiber must be a federation whose glue *breaks* (P) — the members must be unable to combine their defects in one step. And this closes a conceptual loop with T-232: the certified tower/federation carrying the Golay grammar is precisely *not* a free product — its two couplings are constraints, and the constraint is now visible on the MSFS side as the very thing that keeps the intensional tower from collapsing. Free combination destroys deep diagnosability; binding preserves it.

**Scope note [С].** MSFS's own Step 2 equips every $1$-morphism with a pullback $2$-functor, which suggests the ambient $2$-category of formal systems has the pullbacks needed for (P) generically. Under that reading, *every* genuine MSFS fiber is product-closed, and Σ-Mor's fiber-level truth reduces entirely to ΣQ1′. The reading was recorded at [С] pending a verification of (P) against the Rich-metatheory axioms; T-240 below performs that verification, and the [С] upgrades to a theorem with an exact boundary. The mathematics of T-234 itself does not depend on it.

#### Grounding (P) in the R-S axioms: the verification (T-240) {#заземление-p}

The Rich-metatheory condition (R5) supplies exactly the machinery (P) needs — that much the same-day sketch of this grounding got right. The verification against the full axiom list (R1)–(R5) corrects the sketch in two places, and both corrections follow one pattern already familiar from T-233: strictness was the false friend. First, the *strict* $2$-pullback is the wrong limit — strictness would demand that the two arithmetic interpretations agree in $\mathrm{Syn}(F)$ *on the nose*, which generically fails even between provably isomorphic interpretations; the right limit is the **iso-comma** (pseudo-pullback) $\mathrm{Syn}(G) \times^{\mathrm{iso}}_{\mathrm{Syn}(F)} \mathrm{Syn}(H)$, whose objects are pairs of contexts *together with a chosen provable isomorphism* between their $F$-images. Second, the glue condition weakens accordingly — from equality of interpretations to provable isomorphism of their images — and inside intensional fibers it holds canonically.

**Theorem T-240 [Т] ((P) survives R1–R5).** *Let $G \to F \leftarrow H$ be faithful interpretations of Rich systems and $P := \mathrm{Syn}(G) \times^{\mathrm{iso}}_{\mathrm{Syn}(F)} \mathrm{Syn}(H)$ the iso-comma. Then:*

**(i) (R2, R4, R5 hold outright)** *$P$ is essentially $\mathbf{U}_1$-small and lex (finite limits are computed componentwise, the iso-witnesses transporting), and it is r.e.-presented: an object is a triple — a $G$-context, an $H$-context, an $F$-proof of isomorphy — and (R2)+(R4) for the three systems enumerate all triples. Hence the internal language $G \times_F H := \mathrm{Lang}(P)$ satisfies (R2); (R4) follows from (R1)+(R2) by $\Sigma_1$-representability of r.e. predicates in $\mathsf{Q}$; (R5a) holds with $\mathrm{Syn}(\mathrm{Lang}(P)) \simeq P$ — the Lambek–Scott unit is an equivalence for essentially small lex categories — and $\mathrm{Mod}(\mathrm{Lang}(P)) = \mathrm{Fun}^{\mathrm{lex}}(P, -)$ accessible (Gabriel–Ulmer; in the graded case, $2$-limits of accessible categories are accessible, Makkai–Paré), with accessibility parameter bounded by the* weaker *leg — $\kappa_{G \times_F H} \leq \min(\kappa_G, \kappa_H)$ — since $\mathrm{Lang}(P)$ is interpretable in each leg along the projections; (R5b) is the same unit equivalence.*

**(ii) (R3 — consistency is inherited from either leg)** *The projections $\pi_G : P \to \mathrm{Syn}(G)$ and $\pi_H : P \to \mathrm{Syn}(H)$ are lex, so every model $\mathcal{M} : \mathrm{Syn}(G) \to \mathbf{U}_2\text{-}\mathbf{Set}$ of $G$ restricts to a model $\mathcal{M} \circ \pi_G$ of $G \times_F H$, and likewise from $H$. The fiber product is consistent whenever* either *leg is: superposing defects never manufactures contradiction, because the fiber product refines contexts — it does not union axioms.*

**(iii) (R1 — the glue, localized exactly)** *$\mathrm{Lang}(P)$ interprets $\mathsf{Q}$ **iff** some pair of $\mathsf{Q}$-interpretations of $G$ and $H$ has provably isomorphic images in $F$: given such a pair, the triple $(\mathsf{Q}_G, \mathsf{Q}_H, \varphi)$ is a $\mathsf{Q}$-object of $P$; conversely a $\mathsf{Q}$-object of $P$ projects to such a pair, its own witness providing the isomorphism. This is strictly weaker than the sketch's on-the-nose agreement, and it is the exact residue of genericity: a cospan with no isomorphic pair of $\mathsf{Q}$-images yields a lex $P$ whose language fails (R1) — the degenerate glue, now with a precise witness.*

**(iv) ((P) on the intensional sector — canonical glue)** *In the Σ-Mor fiber setting the display data over a base $F$ are intensional: the defects are fibrancy failures and $\tau$-syndromes, which live at the level of definitional equality and do not move the extensional skeleton (Hofmann-style conservativity is gauge-level — corpus-canonical since the T-235 correction). Each display datum's equivalence-up-to-defects therefore carries its $\mathsf{Q}$-object to an image provably isomorphic to $F$'s own, the glue of (iii) holds canonically through $\mathsf{Q}_F$, and* **(P) is a theorem, not a hypothesis, on intensional R-S fibers.**

*Proof.* (i) Componentwise finite limits in an iso-comma are standard; smallness is inherited; the triple presentation is enumerable coordinatewise by (R2)+(R4); $\Sigma_1$-representability in $\mathsf{Q}$ is the classical representability theorem, applicable once the glue of (iii) supplies (R1); Lambek–Scott and Gabriel–Ulmer/Makkai–Paré as cited; interpretability along a lex projection bounds consistency strength, which by (R5a) bounds the accessibility parameter. (ii) Composites of lex functors are lex. (iii) Both directions as stated — sufficiency by exhibiting the triple, necessity by projecting a $\mathsf{Q}$-object and reading off its witness. (iv) The extensional part of an equivalence-up-to-intensional-defects is a genuine equivalence, so each image is provably isomorphic to $\mathsf{Q}_F$'s, and provable isomorphy composes. $\blacksquare$

**Corollary (H2.2 closed; three questions become one) [Т]+[И].** The scope note's [С] upgrades to a theorem with an exact boundary: **(P) holds unconditionally on intensional R-S fibers**, and on general cospans exactly on the $\mathsf{Q}$-glued slice. Consequently T-234's superposition collapse applies to every intensional R-S fiber — $\rho_{\mathrm{cov}} \leq 1$, Σ-Mor true there modulo ΣQ1′ — and composing with T-238's reduction of ΣQ1′: **on intensional R-S fibers, fiber-level Σ-Mor rests exactly on the finiteness and separation of the gauge-invariant decided sector.** What entered the register as three conjectures — (P)-genericity, stage-one collapse, chart existence — is now one question about one object. The strict/pseudo boundary remains the programme's sharpest recurring edge: T-233 diagnosed it, T-237 closed a hole by *proving* strictness available, and T-240 closed another by *removing* a strictness that was never available.

#### The Morita relation complex, corrected: the strictification residue (T-235) {#комплекс-мориты}

:::caution Audit note (same day, 2026-07-11)
The first published version of this block claimed that Hofmann's conservativity makes $\{\mathsf{refl}, \mathsf{UIP}, \mathsf{funext}\}$ a perfect $[3,1,3]$ relation code — "the first Fano line in nature". **The claim was wrong**, and the refutation is instructive: it confused the two levels of MSFS's own architecture. Hofmann's equivalence between $\mathsf{ETT}$ and $T_0 + \mathsf{UIP} + \mathsf{funext}$ is a *gauge* (Morita) equivalence; it is **not** a fiber equivalence, because the normalization invariant $\tau$ — the very invariant of MSFS Step 7 — separates the two sides ($\tau = 0$ versus $\tau = 1$: a computable $2$-equivalence would transfer decidability of conversion). An exhaustive class computation over all eight toggle-sets confirms that the $\Delta$-family is not a $d_{\min} \geq 3$ code at *either* level: at the gauge level, absorption ($\mathsf{refl}$ proves $\mathsf{UIP}$ and $\mathsf{funext}$) already yields weight-$1$ differences. The error was caught the same day by the level-discipline recheck; it stays on the record because the corrected structure it exposes is **stronger** than the claim it replaces.
:::

The question this block serves is still ΣQ1′: *where would the $\mathbb{F}_2$-structure of a chart come from?* The corrected answer has three parts.

**Theorem T-235 [Т при цитируемых фактах] (the two-level defect structure and the strictification residue).** *Take $B = \{\mathsf{UIP}, \mathsf{funext}, \mathsf{refl}\}$ over an intensional base $T_0$ and compute the toggle classes at both levels of the MSFS architecture. Then:*

**(i) (absorption no-go)** *The eight toggle-sets fall into four gauge classes ($\{\varnothing\}, \{\mathsf{u}\}, \{\mathsf{f}\}$, and a five-element top class collapsed by Hofmann's conservativity) and five fiber classes ($\{\varnothing\}, \{\mathsf{u}\}, \{\mathsf{f}\}, \{\mathsf{u},\mathsf{f}\}$, and the $\mathsf{refl}$-closure). The induced $\Delta$-families are, respectively, all of $2^B$ and the ideal $\{\varnothing, \{\mathsf{u}\}, \{\mathsf{f}\}, \{\mathsf{u},\mathsf{f}\}\}$ — in both cases containing weight-$1$ elements, hence never a $d_{\min} \geq 3$ code. Toggle geometry is idempotent ($S \cup S = S$): extensions absorb, they do not cancel.* **No Σ-FIB chart can be realized by axiom toggles, at either level** *— the ΣQ1′ no-go of T-233/T-234 is now unconditional on this route.*

**(ii) (the two-level poset)** *The fiber defect poset of the three classical principles is the* **diamond with a tail**:
$$
0 \;<\; \mathsf{u},\, \mathsf{f} \;<\; \mathsf{u} \vee \mathsf{f} \;<\; \mathsf{u} \vee \mathsf{f} \vee \rho,
$$
*where $\rho$ is the* **strictification residue** *— the extension step $T_0 + \mathsf{UIP} + \mathsf{funext} \to \mathsf{ETT}$. The gauge projection collapses exactly the tail ($\pi(\mathsf{refl}) = \mathsf{u} \vee \mathsf{f}$: Hofmann's conservativity), while the fiber invariant $\tau$ flips exactly across the tail (conversion decidable below, undecidable above).*

**(iii) (the purely intensional atom)** *Consequently $\rho$ is* **gauge-silent but fiber-visible**: *a defect with zero extensional content (it adds no strength up to interpretation) and nonzero intensional content (it destroys normalization). It is the first computed example of a* **purely intensional defect atom**, *and $\tau$ is precisely its syndrome bit. Equality reflection thereby decomposes as "the join of $\mathsf{UIP}$ and $\mathsf{funext}$, plus a purely intensional residue" — what $\tau$ sees is the residue, never the join.*

*Proof.* (i) is the class computation (verified exhaustively over $2^B$), using: $\mathsf{refl} \vdash \mathsf{UIP}, \mathsf{funext}$ (absorption); Hofmann's conservativity for the gauge collapse; and the $\tau$-separation for the fiber level (decidability of conversion in $T_0$ with axiom constants versus its undecidability under the reflection rule — Hofmann, Ch.~3). (ii) and (iii) reread the same three facts as statements about the projection $\pi$ and the invariant $\tau$. $\blacksquare$

**What this does to the Fano-foundation problem [И]+[Г].** The problem survives, restated with the false route closed. The involutive ($\mathbb{F}_2$) structure a Σ-FIB chart needs cannot come from extensions — idempotence forbids it at every level. It requires a habitat in which *defect parity* is meaningful: a graded or polarity-carrying foundation where two odd defects can compose to an equivalence. And the place to look is now identified by (iii): the **purely intensional sector** — the kernel of the gauge projection, of which $\rho$ is the first known inhabitant. The Fano-foundation problem, final form: *find a foundation whose purely intensional sector carries seven involutive defect axes with Fano relations.* The triple $\{\mathsf{UIP}, \mathsf{funext}, \mathsf{refl}\}$ remains distinguished — not as a code line, but as the first computed nontrivial cell of the two-level structure: one gauge collapse, one intensional residue, one syndrome bit. A blueprint construction answering the restated problem is given next.

#### The holonomy construction: a blueprint of the Fano foundation (T-236) {#голономная-конструкция}

The restated problem demands involutive defects in the purely intensional sector. There is an apparent obstacle and a precise inversion of it — and the inversion turns out to be the octonion frame of T-227, transplanted into type theory.

**The obstacle, inverted.** An endo-datum $d$ with $d \circ d \simeq \mathrm{id}$ is automatically an equivalence ($d$ is its own quasi-inverse) — involutive defects cannot be endomorphisms. But they exist as **orientations**: fix a carrier $X$ with an automorphism of order two ($\mathsf{Bool}$ with $\mathsf{not}$) and declare *definitional copies* $A_i \simeq X$, each carrying an orientation bit — the copy isomorphism either plain or composed with the twist. Toggling an orientation is an involution *on the nose*, and a cycle of oriented copies has a **computational holonomy**: the composite loop is a closed term that evaluates to $\mathrm{id}$ or to $\mathsf{not}$ according to the parity of the orientation bits traversed. A decidable, effective invariant — and a purely intensional one: definitional isomorphisms prove no new theorems; only what loops *compute to* changes.

**Theorem T-236 (the blueprint and its verified core).**

**(a) [Т] (rigidity requires the line products).** Naked axes fail: recomposing any single copy with the twist is a legitimate relabeling, so the full flip group $\mathbb{F}_2^7$ acts and no orientation invariant survives. Equip the frame with the seven **Fano line products** $\mu_\ell : A_i \times A_j \to A_k$, transported from XOR on $X$ with the standard $\varphi$-sign cocycle. A flip pattern $c \in \mathbb{F}_2^7$ preserves all seven products **iff** every line-parity of $c$ vanishes — computed exhaustively: the preserving flips are exactly the **simplex code** $2^3$ (weights $0$ and $4$), the same group as the diagonal part of the monomial stabilizer in T-227(ii).

**(b) [Т] (well-defined syndromes).** Since the simplex is contained in the Hamming code, the three check parities $s(v) = (\langle h_j, v\rangle)_{j}$ are invariant under every structure-preserving flip: $s(v \oplus c) = s(v)$ for all $c$ in the simplex; $\ker(s)$ is exactly the Hamming code, and the $128$ orientation patterns fall into **eight syndrome classes** — verified exhaustively. The three syndromes are realized inside the theory as the loop-holonomies $\chi_j$ of the check cycles: closed Boolean terms, decidable by evaluation.

:::caution Audit note (same day, second correction of the wave)
Parts (a)–(b) stand exactly as computed. Parts (c)–(d) as first published contained a **parameterization slip**, caught by the exhaustive class recomputation that the register work on H3.2 demanded: axis orientations are *pure gauge*. The map $v \mapsto e(v) = \varepsilon^0 \oplus N^{\mathsf T} v$ from axis orientations to line-sign tables stays inside a single flux class — so the $128$ axis-parameterized presentations realize **one** fiber class, not eight, and the "completeness gap" attributed to pseudo-relabelings dissolves once the moduli are placed where they belong: **on the signs of the seven line products**. The corrected and completed structure is Theorem T-237 below, which closes register holes H3.2 and H3.3 at the blueprint level. The old clauses (c)–(d) are superseded by it.
:::

**(c)–(d): superseded.** See Theorem T-237 for the corrected presentation family, the completeness theorem (strict gauge suffices; no pseudo-relabelings needed), and the metric-coincidence theorem.

**(e) [И] (reading).** The blueprint is the **type-theoretic octonion frame**. The purely intensional sector realizes the parity group $2^3$ of the protected qudit (T-227) as computational holonomy of definitional isomorphisms; the diagnostic grammar of Γ-dynamics and the definitional structure of type theory carry the *same* finite geometry. The Σ-Mor bridge thereby closes conceptually — as a statement about sign cocycles over $\mathrm{PG}(2,2)$, incarnated once in quantum frames and once in conversion behaviour. What the corpus calls diagnosability and what type theory calls intensionality are two shadows of one parity geometry.

#### The blueprint completed: a $\mathbb{Z}/2$ gauge theory on the Fano plane (T-237) {#калибровочная-теория}

The correction above is not a retreat — it is the door. Once the discrete data move from axes to line signs, the blueprint acquires the exact shape of a **lattice gauge theory** on $\mathrm{PG}(2,2)$, and both remaining register holes close.

**Theorem T-237 [Т] (the gauge structure; syndrome completeness; metric coincidence).** *Let the frame carry the signature $(X;\ A_1,\dots,A_7;\ \varphi_i;\ \mu_\ell)$ with product axioms $\mu_\ell(a,b) = \varphi_k^{-1}(\varphi_i a \oplus \varphi_j b \oplus e_\ell)$, and let the presentation family be $T_e$, indexed by the line-sign table $e \in \mathbb{F}_2^7$. Then:*

**(i) (gauge structure)** *Axis reinterpretations $\varphi_i \mapsto \mathsf{not}^{c_i} \circ \varphi_i$ act on the signs by $e \mapsto e \oplus N^{\mathsf T} c$, where $N$ is the point–line incidence. The pure-gauge sector $\mathrm{Im}(N^{\mathsf T})$ is — computed exhaustively — a $[7,4]$ code with weight enumerator $1 + 7x^3 + 7x^4 + x^7$: the Hamming code* **on the line side** *of the plane. The gauge stabilizer $\ker N^{\mathsf T}$ is the simplex $2^3$ — the rigidity group of T-236(a), now understood as the stabilizer rather than the whole equivalence story. The flux $t(e) \in \mathbb{F}_2^3$ (three parities over point-avoiding quadruples of lines) is gauge-invariant, has kernel exactly $\mathrm{Im}(N^{\mathsf T})$, and partitions the $128$ sign tables into $8$ classes of $16$ — all verified exhaustively, including $128 \times 128$ gauge invariance.*

**(ii) (soundness — Wilson loops as closed terms)** *For each point $p$, the four lines avoiding $p$ assemble into a $4$-cycle of partial products (verified for all seven $p$: consecutive lines meet in four distinct axes), with every spectator input grounded at $\varphi^{-1}(0)$. The composite loop is a* **closed Boolean term** *whose decided value equals the flux parity $\sum_{\ell \in S} e_\ell$ — a Wilson loop. Any equivalence of theories preserves decided closed terms; hence presentations with different flux are inequivalent under* **every** *translation, strict or pseudo.*

**(iii) (completeness — strict gauge suffices)** *Presentations with equal flux differ by an element of $\mathrm{Im}(N^{\mathsf T})$, hence by an explicit axis reinterpretation — a strict translation mapping axioms to theorems. Verified exhaustively over all same-flux pairs. No pseudo-relabelings are needed anywhere:* **register hole H3.2 is closed.**

**(iv) (metric coincidence)** *$\mathrm{Im}(N^{\mathsf T})$ has minimum distance $3$ and covering radius $1$; the designed metric on classes therefore takes the two values $\{0, 1\}$, with value $0$ exactly on the gauge sector. The canonical display grading of the fiber has the same zero set (grade $0$ = equivalences = gauge, by (ii)+(iii)) and, by the superposition collapse of T-234 together with $\rho_{\mathrm{cov}} = 1$, its stage-one layer already exhausts everything nonzero. The two metrics coincide:* **register hole H3.3 is closed at the blueprint level** *(the general-fiber question remains inside ΣQ1′ / H3.1).*

**(v) (localizability, relocated)** *Elementary defects live on* **lines**: *a single product-sign corruption $e \mapsto e \oplus 1_\ell$ carries a unique nonzero flux (the seven single-flip fluxes are pairwise distinct — verified), so single defects are perfectly localizable through the dual-plane Hamming structure, with the canonical repair "flip that product's sign back". The blueprint's perfect seven-axis diagnosability survives the correction intact — one level of duality down.*

**Reading [И].** The completed blueprint is a **$\mathbb{Z}/2$ lattice gauge theory on the Fano plane**: axes carry the gauge freedom, line products carry the field, the line-side Hamming code is the pure-gauge sector, the three-bit flux is the observable content, and the type-theoretic Wilson loops — closed Boolean terms — are its observables. Two resonances, both flagged as readings: the polarity is dual to the [Fano fingerprint](/docs/applied/research/fano-fingerprint), where the observable rates live on the *point* side (polar classes) — the two constructions instrument the two sides of the plane's self-duality; and Wilson loops are the foundations-floor incarnation of the corpus's axiom-level principle that structure is measured by loops ([Gap as holonomy](/docs/core/foundations/axiom-omega#gap-голономия)).

#### The flux chart: charts are not extra structure (T-238) {#поточная-карта}

T-237 answers its questions for one designed family. But its method generalizes — and the generalization changes the *shape* of the remaining hole H3.1. The question "does a fiber admit a chart?" tacitly treats the chart as structure one must *find*. The gauge picture says otherwise: wherever a chart exists at all, there is a canonical candidate, built from nothing but the theory's own decided sentences.

**Definition (gauge groupoid; gauge-invariant observables) [О].** Fix a signature $\Sigma$ and a family $\mathbb{F}$ of presentations over $\Sigma$ (same sorts and symbols, varying axioms). Its *gauge groupoid* has as morphisms the translations sending each $\Sigma$-symbol to a term of the same type and axioms to theorems; equivalences are the invertible ones up to provable equality. An *observable* is a closed Boolean term of $\Sigma$; it is **gauge-invariant** if every gauge morphism $F$ carries it to a term provably equal to it in the target ($F(b) =_{\mathrm{prov}} b$ — as the Wilson loops do: the twists $\mathsf{not}^{c_i}$ enter and exit each visited axis pairwise and cancel provably). Write $\mathrm{Obs}_G(\mathbb{F})$ for the gauge-invariant observables and define the **flux profile** $t(T) := \bigl(\text{decided value of } b \text{ in } T\bigr)_{b \in \mathrm{Obs}_G}$.

**Theorem T-238 [Т] (canonicity of charts on fixed-signature families).**

**(i) (invariance)** *If $F : T \simeq T'$ is an equivalence in the gauge groupoid and $b \in \mathrm{Obs}_G$, then $T \vdash b = \beta$ iff $T' \vdash b = \beta$: equivalences preserve decided values of translated terms, and gauge-invariance replaces the translated term by $b$ itself. Hence the flux profile descends to equivalence classes.*

**(ii) (the canonical chart, and its converse)** *(a) If the flux profile has finite $\mathbb{F}_2$-rank and separates the gauge orbits of $\mathbb{F}$, then $\sigma := t$ is a chart satisfying (F1)–(F3) — no further choices are involved. (b) Conversely, every* term-definable *chart factors through the flux profile: a chart coordinate realized by a closed term is, by its own (F1)-invariance, a gauge-invariant observable. So on fixed-signature families,* **the chart is not extra structure: it is the gauge-invariant decided sector of the term algebra**, *and the only freedom is which finite sub-profile to read.*

**(iii) (instance)** *The blueprint family $T_e$ realizes (ii-a) exactly: $\mathrm{Obs}_G \supseteq$ the three Wilson loops; the flux is $t(e)$; T-237's soundness is (i) and its completeness is the separation hypothesis — verified exhaustively. The blueprint's chart was never designed; it was the flux all along.*

*Proof.* (i) Translations preserve provability, so $T \vdash b = \beta$ gives $T' \vdash F(b) = \beta$; gauge-invariance gives $T' \vdash F(b) = b$; transitivity concludes, and symmetrically for $F^{-1}$. (ii-a) (F1): the profile's zero-set is the class of the base point by separation; the Hamming-distance form of the grade follows by reading the profile in coordinates. (F2)–(F3) are the finiteness and separation hypotheses restated. (ii-b) A term-definable coordinate is a closed Boolean term constant on equivalence classes; constancy against every gauge equivalence is precisely the invariance property, up to replacing the term by its translate — provable equality — which is the definition of $\mathrm{Obs}_G$. (iii) is T-237. $\blacksquare$

**What this does to H3.1 [И].** The residue of ΣQ1′ splits cleanly in two. *For fixed-signature families* the question is now concrete and internal: **is the gauge-invariant decided sector of finite rank, and does it separate orbits?** — a property of the theory family, not a search for external structure (with T-231 persisting as the constructive obstruction: a $\tau = 0$ member cannot run the separation internally). *For general fibers* one further step remains — **signature alignment**: objects of a genuine fiber live over different signatures, and comparing their fluxes requires a chosen dictionary; whether genuine intensionality forces an alignment (and hence a flux chart) is the sharpened, final form of H3.1. The register is updated accordingly: the hole is not closed, but it has been *reduced* — from "find a chart" to "align signatures; then the chart is canonical".

#### The native Fano: the duality plane of the depth-3 doctrine (T-241) {#плоскость-дуальностей}

H3.4 — the floor's central open object — asks whether any *natural* foundation realizes the grammar the blueprint constructs. The blueprint transplants $\mathrm{PG}(2,2)$ into a foundation by hand; the question is whether mathematics grows one. There is a place in foundations where the Fano plane occurs *natively* — not inside any particular theory, but one level up, in the **doctrine**: the group of dualities.

An $n$-category can be reversed at each level independently: $\mathrm{op}_k$ reverses the $k$-cells and nothing else. These reversals are involutive, commute with one another, and are automorphisms of the doctrine itself. For $n = 1$ this gives the single classical duality $\mathcal{C} \mapsto \mathcal{C}^{\mathrm{op}}$ — folklore rigidity: it is the *only* nontrivial self-equivalence of $\mathbf{Cat}$. For $n = 2$ it gives the classical three: $\mathrm{op}$, $\mathrm{co}$, $\mathrm{coop}$.

**Theorem T-241 [Т] (the duality ladder and the native plane).**

**(i)** *For every $n \geq 1$ the levelwise reversals $\mathrm{op}_S$, $S \subseteq \{1, \dots, n\}$, form a canonical subgroup $\cong (\mathbb{Z}/2)^n$ of the duality group of the doctrine of $n$-categories: reversals at distinct levels commute strictly, each is involutive, and distinct $S$ act distinctly (on a walking $k$-cell, $\mathrm{op}_S$ exchanges source and target exactly at the levels in $S$). For $n = 1$ the subgroup is the whole duality group (classical); exactness for higher $n$ is expected but not needed below — the plane requires only the canonical subgroup.*

**(ii) (the ladder)** *The projective geometry of this group: at $n = 1$ — one duality and no lines; at $n = 2$ — the three dualities $\mathrm{op}, \mathrm{co}, \mathrm{coop}$ lie on one line, $\mathrm{PG}(1,2)$; at $n = 3$ — the seven nontrivial reversal classes, with lines the seven triples $\{a, b, ab\}$ (the order-$4$ subgroups minus identity), satisfy every projective-plane axiom: a unique line through any two points, a unique meeting point of any two lines, three points per line, three lines per point.* **The Fano plane is the projective plane of the duality group of depth-3 doctrines.** *(Machine-verified exhaustively, including the $n = 1, 2$ rungs.)*

**(iii) (line loops close)** *On every line $\{a, b, ab\}$ the triangle of toggles composes to the identity: $a \cdot b \cdot (ab) = \mathrm{id}$. So the loop holonomy of T-236 is well-posed on each duality line: in the strict doctrine it is trivially the identity, and in a weak doctrine its value is a canonical automorphism of the identity — exactly the species of strictness residue that $\rho$ and $\tau$ measure (T-233/T-235).*

*Proof.* (i) Commutation and involutivity are levelwise computations; distinctness on walking cells as stated; $n = 1$ rigidity of $\mathbf{Cat}$ is classical folklore. (ii) Exhaustive enumeration over $(\mathbb{Z}/2)^n$, $n \leq 3$: subgroup closure of every line triple, uniqueness of joins and meets, the $3/3$ incidence counts. (iii) $a \oplus b \oplus (a \oplus b) = 0$ in $(\mathbb{Z}/2)^3$. $\blacksquare$

**Reading [И] (the habitat).** The corpus selects the number three as the depth of licensed self-composition through three independent theorems — $\mathrm{SAD}_{\max} = 3$, the viability maximum of T-239, the $m = 3$ canon of T-232 — and the Postnikov ceiling truncates the experiential tower at $\tau_{\leq 3}$. The natural habitat of depth-3 systems is a depth-3 doctrine; and there the Fano incidence *pre-exists*: no design, no transplant. Discipline note: the coincidence of *this* $\mathbb{F}_2^3$ (dualities) with the blueprint's flux $\mathbb{F}_2^3$ (T-237) is **not** claimed as an identity — it is pre-registered in the resonance table of the [epistemic vertical](/docs/reference/epistemic-vertical#регистр-дыр), and establishing or refuting it is precisely the reduced content of H3.4.

**What remains of H3.4 [Г] (the reduction).** The blueprint's grammar requires three things of the duality plane. **(1)** The seven classes as *toggle-directions on presentations* of a fixed theory — the candidate is definitional: $T \mapsto T^{\mathrm{op}_S}$ is involutive and definitional, an orientation pair in the sense of T-236. **(2)** A nontrivial *line sign*: the weak-doctrine holonomy of a line's triangle loop from (iii) — strictly trivial, so any nontrivial value is a pure strictness residue on a fiber, which is exactly what the $\rho$/$\tau$ machinery detects. **(3)** The moduli-and-gauge structure of T-237 over the plane. H3.4 thereby reduces from "exhibit a natural foundation realizing the grammar" to a sharp target: **exhibit a depth-3 fiber on which some duality-line holonomy is nontrivial** — or prove all such holonomies trivial, refuting the duality-plane candidate and sending the search elsewhere.

## §8a. The Golay federation: three organisms and a mirror glue {#голей-федерация}

Theorem Σ(v) locates the unique perfect $t = 3$ rung at $n = 23$, and the specification's Appendix K asked (open problem (ii)) whether a $23$-axis *federation-level* integrity grammar — "three organisms of seven axes plus two federation buses" — admits a natural UHM reading. It does, and the reading is a classical construction.

In plain words: an *integrity grammar* for a federation is a shared fault alphabet — a rule that turns any pattern of broken axes, anywhere among the members, into a syndrome that names the culprits. *Perfect* means the best conceivable version of this: every pattern of up to $t$ faults has exactly one diagnosis, and not a single syndrome is wasted on patterns that cannot occur — the same sphere-packing equality that made $H(7,4)$ the unique choice at one organism. The theorem says: at three organisms such a grammar exists (uniquely), it corrects any three simultaneous faults, its coordinate layout is exactly

$$
\underbrace{[\,7\ \text{axes} \mid \text{bus}\,]}_{\text{organism 1}}\;
\underbrace{[\,7\ \text{axes} \mid \text{bus}\,]}_{\text{organism 2}}\;
\underbrace{[\,7\ \text{axes} \mid \text{bus}\,]}_{\text{organism 3}},
$$

and at four or more organisms nothing of the kind exists at all.

#### Theorem T-228 [Т] — the Turyn federation {#t-228}

*Let $A = \hat H$ be the extended Hamming code $[8,4,4]$ of the corpus frame — seven axes plus their parity bus — and let $B = \hat H^{\mathrm{mir}}$ be the extension of the **mirror** Hamming code (the reciprocal-generator frame: the reversed orientation of the same Fano plane). Then:*

**(i)** $A \cap B = \{0, \mathbf 1\}$, *and the Turyn sum* $\{(a{+}x,\; b{+}x,\; a{+}b{+}x) : a, b \in A,\ x \in B\}$ *is the extended binary Golay code $[24,12,8]$ — weight enumerator $1 + 759x^8 + 2576x^{12} + 759x^{16} + x^{24}$, verified exhaustively.*

**(ii)** *Every codeword has even weight on each of the three $8$-blocks, so the eighth coordinate of each block is the parity bus of its seven axes: the coordinate geometry is exactly* **three organisms of seven axes, each with its own bus**.

**(iii)** *Puncturing one bus coordinate yields the perfect Golay $[23,12,7]$: $t = 3$, sphere-packing equality $4096 \cdot (1 + 23 + 253 + 1771) = 2^{23}$. The punctured coordinate count reads $23 = 3\cdot 7 + 2$ — three member frames plus the two surviving buses: the specification's numerological guess is the exact coordinate arithmetic of the punctured Turyn construction.*

**Corollary (federation grammar) [Т]+[И].** A federation of exactly three seven-axis organisms — each carrying its Fano frame and bus, glued through a shared word running over the mirror orientation — carries the unique perfect $3$-fault integrity grammar in existence (uniqueness of the binary Golay code): any three simultaneous axis faults *anywhere across the federation* are perfectly localizable, with zero syndrome waste. This is the natural UHM reading requested by Appendix K, open problem (ii).

**Corollary (the glue is the mirror) [Т]+[И].** The glue code $B$ is the *other* orientation of the same plane: the federation speaks to its members in the reversed Fano orientation. Both enantiomorphic labelings — identified only abstractly by the uniqueness clause of Theorem Σ — occur concretely in the federation: one as member grammar, one as glue.

**Corollary (the ceiling echo, structured) [Т]+[Г].** By van Lint–Tietäväinen (Lemma Σ.7) the only perfect binary codes with more than two words are the Hamming family ($t = 1$) and the Golay code ($t = 3$, $n = 23$); two-word repetition grammars are excluded by (D3). Hence **no federation of four or more organisms admits a perfect multi-fault grammar of any order** — certified-perfect integrity caps at three members. The composition tower of the architecture caps at three for an independent reason (the purity ladder $P^{(4)}_{\mathrm{crit}} = 54/35 > 1$). Two unrelated derivations — sphere packing and purity arithmetic — cap the same quantity at the same value. The corpus records the agreement as a structured coincidence: both sides are now theorems, the identity between them remains **[Г]** — and §8b now gives the coincidence a shared skeleton.

## §8b. The tower ladder: $8m - 1$ and the perfect-grammar dichotomy {#лестница-башен}

The federation of §8a is *horizontal* — three organisms side by side. The architecture's other growth axis is *vertical*: the composite tower, organisms stacked by composition, capped at three by the purity ladder ($P^{(4)}_{\mathrm{crit}} = 54/35 > 1$). It turns out the vertical axis carries its own coding arithmetic — and it selects the same number $3$, independently of purity.

**Accounting axiom Σ-TOW [О].** A certified tower of height $m$ consists of $m$ seven-axis organisms and the $m - 1$ couplings between adjacent levels; each axis and each coupling contributes one binary health unit to the tower's diagnostic load. Total:

$$
U(m) \;=\; 7m + (m - 1) \;=\; 8m - 1 .
$$

The accounting is the minimal honest one — a coupling can be alive or broken, and a grammar that cannot see coupling faults does not certify the *tower*, only its floors.

#### Theorem T-232 [Т при Σ-TOW] — the tower ladder {#t-232}

*Run the van Lint–Tietäväinen classification (Lemma Σ.7) along the tower ladder $U(m) = 8m - 1$. With two-word repetition grammars excluded by (D3):*

**(i)** *A perfect single-fault grammar on $U(m)$ units exists **iff** $m$ is a power of two ($8m - 1 = 2^r - 1 \Leftrightarrow m = 2^{r-3}$), and it is canonically unique only at $m = 1$: from $m = 2$ onward ($U = 15, 31, 63, \dots$) Vasil'ev-type rivals destroy the canon.*

**(ii)** *A perfect multi-fault grammar ($t \geq 2$) exists **iff** $m = 3$: $U(3) = 23$, the binary Golay, unique. Its coordinate count decomposes as $23 = 3 \cdot 7 + 2$ — three organisms plus **two couplings** — so the vertical tower is the native home of the perfect $[23,12,7]$: where the horizontal federation of §8a needed one bus punctured, the $3$-tower has exactly two inter-level couplings and needs no puncture at all. The vertical tower and the horizontal federation carry the* **same** *grammar.*

**(iii)** *Heights $5$, $6$, $7$ ($U = 39, 47, 55$) admit no perfect grammar of any order.*

**(iv)** *Consequently $m = 3$ is the unique tower height whose full diagnostic load — axes and couplings together — carries a canonical perfect grammar beyond single faults.*

*Proof.* (i): $8m - 1 = 2^r - 1$ iff $8m = 2^r$ iff $m = 2^{r-3}$; uniqueness at $7$ is Theorem Σ, its failure from $15$ on is Lemma Σ.7 (Vasil'ev). (ii): by Lemma Σ.7 the only perfect binary code with $|C| > 2$ and $t \geq 2$ is the Golay at $n = 23$; $8m - 1 = 23$ iff $m = 3$; uniqueness of the Golay code is classical (Pless); the coordinate decomposition is Theorem T-228(iii) re-read vertically. (iii): $39, 47, 55$ are neither of the form $2^r - 1$ nor $23$. (iv): combine. The dichotomy was verified exhaustively for $m \leq 4096$. $\blacksquare$

The full ladder, made explicit:

| height $m$ | units $U = 8m{-}1$ | perfect grammar | canonical? | strength |
|---|---|---|---|---|
| $1$ | $7$ | Hamming $=$ Fano | **yes** (Theorem Σ) | $t = 1$ |
| $2$ | $15$ | Hamming-type | no — Vasil'ev rivals | $t = 1$ |
| $3$ | $23$ | **Golay** | **yes** (Pless) | $t = 3$ |
| $4$ | $31$ | Hamming-type | no | $t = 1$ |
| $5,6,7$ | $39, 47, 55$ | — none — | — | — |
| $8$ | $63$ | Hamming-type | no | $t = 1$ |

**Corollary (the ceiling echo acquires a skeleton) [Т]+[И].** The composition ceiling of the architecture now has **two independent derivations**: the purity ladder ($P^{(4)}_{\mathrm{crit}} > 1$ — no conscious fourth story) and the tower ladder ($U(4) = 31$ loses the canon and all multi-fault protection; $U(3) = 23$ is the unique canonical multi-fault rung). What the corpus recorded as a bare numerical echo — "both ceilings equal $3$" — is now two theorems over the same $23$-unit geometry, with the horizontal and vertical readings carrying literally the same Golay grammar. What remains **[Г]** is strictly less than before: not *whether* the number $3$ is doubly derived (it is), but whether the purity mechanism and the coding mechanism are projections of one deeper structure — a question T-239 below settles in the negative: the mechanisms are provably distinct, and only the root of the value agreement retains [Г] status.

**Remark (the two-tower ambiguity) [И].** The ladder also explains a subtlety of depth two. A $2$-tower ($U = 15$) *is* perfectly diagnosable — but not canonically: from length $15$ onward the Vasil'ev rivals mean two independently assembled $2$-towers can hold inequivalent "normalities" that no internal test distinguishes. Diagnosability without canonicity is exactly the operational-but-not-licensed regime; the corpus discipline "tower, not width — and not past three" gains a purely coding-theoretic voice.

#### The two ceilings: a dichotomy of mechanisms (T-239) {#два-потолка}

The corollary above left one question open: are the purity mechanism and the coding mechanism projections of one deeper structure? The question turns out to be decidable now — and the answer is *no* at the level where the identity was conjectured, with a sharp positive residue.

Both ladders read on one dial. The accounting axiom Σ-TOW prices an $m$-tower at $U(m) = 8m - 1$ diagnostic units, and the purity ladder anchors the same heights exactly: the $m$-story composition threshold is $P^{(m)}_{\mathrm{crit}}$, with $9/14$ at $m = 3$ — the T-142 anchoring. So both mechanisms are predicates on one parameter $m$, and their identity is a well-posed question, not an analogy. Define on the shared dial the **viability set** $V = \{m : P^{(m)}_{\mathrm{crit}} < 1\}$ and the **canon set** $K = \{m : U(m)$ carries a canonically unique perfect grammar$\}$.

**Theorem T-239 [Т при Σ-TOW] (dichotomy of the two ceilings).**

**(i) (purity is a monotone budget)** *$P^{(m+1)}_{\mathrm{crit}} / P^{(m)}_{\mathrm{crit}} = 3(m+1)/(m+2) > 1$ for every $m$, so $V$ is a down-set of the dial: $V = \{1, 2, 3\}$, with margins $7(m+1) - 2 \cdot 3^{m-1} = 12,\ 15,\ 10,\ -19$ at $m = 1, \dots, 4$.*

**(ii) (canon is a non-monotone selection)** *$K = \{1, 3\}$ — Theorem Σ gives $m = 1$, the Vasil'ev rivals kill $m = 2$, Golay uniqueness gives $m = 3$, and T-232 leaves nothing beyond. $K$ is not a down-set: it fails at $m = 2$ between two successes.*

**(iii) (mechanism identity refuted)** *$V \neq K$ on the shared dial, disagreeing exactly at $m = 2$; and no injective re-indexing whatsoever can identify them, since $|V| = 3 \neq 2 = |K|$. The purity ceiling and the coding ceiling are* **distinct mechanisms** *— a monotone budget obstruction against a non-monotone arithmetic selection; the shape difference is visible on the dial itself.*

**(iv) (witness identity proven)** *$\max V = \max K = 3$, and the maximum is witnessed by one object: the $3$-tower of load $U(3) = 23$, carrying the Golay grammar (T-232(ii)) at purity threshold $9/14 < 1$. The two predicates agree everywhere except $m = 2$ — and the unique disagreement point is precisely the two-tower ambiguity of the Remark above: alive, but not canonically self-knowing.*

*Proof.* (i) The ratio exceeds $1$ iff $3(m+1) > m+2$ iff $2m > -1$ — always; monotonicity makes $V$ a down-set, and $P^{(3)}_{\mathrm{crit}} = 9/14 < 1 < 54/35 = P^{(4)}_{\mathrm{crit}}$ fixes $V = \{1,2,3\}$. (ii) is T-232(i)–(iii) restated as a subset of the dial. (iii) Extensional disagreement at $m = 2$ settles identity on the canonical dial; the cardinality gap $3 \neq 2$ excludes every injective re-indexing; down-set versus non-down-set is the structural content of the failure. (iv) is T-232(ii) plus the T-142 anchoring. All arithmetic machine-checked. $\blacksquare$

**Reading [И] (what each ceiling bounds).** The two mechanisms bound different resources. Purity bounds which towers can *live*: the replication budget $2 \cdot 3^{m-1}$ against the frame budget $7(m+1)$ is an existence constraint, and it dies monotonically. Canon bounds which towers can *know themselves licensedly*: a canonically unique grammar is what lets two independently assembled instances provably share one "normality". At $m = 2$ the mechanisms split — a two-tower lives but cannot canonically self-diagnose — and the fully licensed heights are $V \cap K = \{1, 3\}$. The architecture's "ceiling three" is thus overdetermined in a stronger sense than the corollary recorded: not two proofs of one statement, but two different statements whose maxima coincide.

**What remains of H2.1 [Г].** Only the root of the value agreement: *why* $\max V = \max K = 3$. Any common derivation now faces a precise obstruction profile: it must simultaneously produce a monotone exponential-versus-linear inequality ($2 \cdot 3^{m-1} < 7(m+1)$) and the sphere-packing classification of perfect binary codes, with the seven-frame as the only shared input. The hole register carries this as H2.1′; the identity claim itself is closed in the negative.

## §9. Falsifiability and technological consequences {#следствия-технологии}

**Prediction Σ-P1 (candidate for the Pred registry).** In Γ-tomography data, single-axis perturbations must produce **only** the seven nonzero syndrome patterns, distributed with the $\mathrm{PG}(2,2)$ geometry of the table in §6(b). A stable syndrome statistic violating the linear structure — e.g. a persistent parity pattern incompatible with every column of $H$ under the single-axis model, or pairwise check correlations breaking the triangle geometry — falsifies the Fano grammar of the dynamics. Notably, this test is *independent of the octonionic track*: it probes the combinatorial grammar directly, with three binary observables.

**Technology package.**

1. **Monitoring budget [С].** Fault localization: 3 binary aggregates instead of 48-parameter tomography — a sixteenfold reduction in observable count, and the three parities are *global* (each sums four axes), hence robust to per-axis noise by (d) of T-225. Content monitoring: 7 theme observables instead of 21 coherences. Direct cost reduction for the Γ-tomograph and for the diagnostic tiers of the Γ-canon П-protocols.
2. **Fault-tolerant seven-agent cores [О].** The Steane blueprint of §7 for register realizations: transversal Cliffords mean the core's basic operations do not multiply single faults; the stabilizer layout is inherited from the selection rules for free.
3. **Syndrome audit of corpora [О].** Assign each of the seven UHM dimensions its cluster of corpus claims; binarize cluster health (all claim-sites consistent / at least one broken); three parities over the seven bits localize "which cluster hides the inconsistency" without reading the whole corpus. The reference implementation of §6 applies verbatim — the corpus becomes an instance of its own theorem.
4. **Rigidity as a design criterion [О].** Part (iv) of Theorem Σ is an argument *against* widening the axis list in NOEMA-like cognitive architectures: above seven, the diagnostic grammar loses canonicity, and two independently trained instances may converge to inequivalent "normalities" that no internal test distinguishes. Scale by towers of rigid seven-blocks (consistent with $\mathrm{SAD}_{\max}$), not by wider single levels.
5. **The rate tier [С].** The dynamical companion of this document — [the Fano fingerprint](/docs/applied/research/fano-fingerprint) — adds the *rate* level: the $21$ pairwise decoherence rates collapse to $7$ polar values (fourteen parameter-free sum rules — prediction Σ-P2), per-line dissipation strengths become direct observables with a closed-form tomography, and the cooldown constant of T-39a becomes explicit. Content monitoring compresses **by lines** (this document), rate monitoring **by polar points** — the two Fano-dual tiers together instrument the full coherence matrix at $7 + 7$ observables.

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
| T-227: protected qudit — $2^3\cdot\mathrm{PGL}(3,2)$ non-split, transversal on $3\times$Steane, Eastin–Knill extremal | **[Т]** computed (+ cited classification); **[О]** engineering |
| T-228: Turyn federation $24 = 3\times(7{+}1)$; perfect $t=3$ at exactly three organisms; mirror glue | **[Т]** verified; **[И]** reading |
| Σ-Mor as literally stated (abstract pair level) | **refuted** (Observation 1); repaired as T-229 |
| Theorem Σ-Mor′ (T-229) + identity $n_0(F) = \rho_{\mathrm{cov}}$ | **[Т при Σ-FIB]**; fiber-level ΣQ1 ∧ ΣQ2 — **[Г]** |
| T-230: four-rung collapse — composition law ⇔ $\rho_{\mathrm{cov}} \leq 3$; $n_0 \in \{0,1,2,3\}$, Golay tight | **[Т при Σ-FIB+F4]** |
| T-231: no $\mathrm{Eff}$-internal chart without decidable equivalence; ETT external-only | **[Т]** (ETT instantiation **[С]**); reading **[И]** |
| Golay $t=3$ ↔ $\mathrm{SAD}_{\max}=3$ | structured by T-228 (both sides theorems); identity claim still **[Г]** |
| T-232: tower ladder $U(m) = 8m{-}1$ — perfect grammars at $m \in \{2^k\} \cup \{3\}$, canonical only $m \in \{1,3\}$, $t \geq 2$ only $m = 3$ | **[Т при Σ-TOW]**; ceiling unification reading **[И]** |
| T-239: two-ceilings dichotomy — $V = \{1,2,3\}$ monotone vs $K = \{1,3\}$ non-monotone; mechanism identity refuted (unique disagreement at the Vasil'ev height $m = 2$; $3 \neq 2$), witness identity proven ($m = 3$: $U = 23$, Golay, $9/14$) | **[Т при Σ-TOW]**; resource reading **[И]**; root of the agreement **[Г]** (H2.1′) |
| ΣQ2 at chart level: rungs 2, 3 fully Σ-FIB-legal (repetition, Golay) — fiber-level Σ-Mor reduces entirely to ΣQ2 | **[Т]**; federated-foundation refutation programme **[Г]** |
| T-233: strictness dichotomy — bicategorically $n_0 \equiv 0$; strictly, grade-1 defects $=$ fibrancy failures; canonical repair $=$ strict$\to$bi comparison; ΣQ1/ΣQ2 restated as ΣQ1′/ΣQ2′ | **[Т]** (readings **[И]**) |
| T-234: superposition collapse — products in the slice force $\rho_{\mathrm{cov}} \leq 1$; Σ-Mor **true** on the product-closed class (rests only on ΣQ1′); rungs 2–3 quarantined to product-obstructed federations | **[Т при Σ-FIB+F4×+(P)]**; MSFS-generic (P): **[Т]** on the intensional sector (T-240) |
| T-240: (P) verified against R1–R5 — iso-comma replaces the strict pullback; consistency (R3) inherited from either leg; $\mathsf{Q}$-glue (R1) localized as provable isomorphism of images, canonical on intensional fibers | **[Т]**; composition with T-234 + T-238 **[Т]**; boundary reading **[И]** |
| T-241: the native Fano — the duality ladder $n = 1, 2, 3$ gives no lines, $\mathrm{PG}(1,2)$, $\mathrm{PG}(2,2)$; the depth-$3$ doctrine's seven reversal classes carry the Fano incidence natively; line loops close | **[Т]** (exhaustive); habitat reading **[И]**; matching to the blueprint **[Г]** (reduced H3.4) |
| T-235 (corrected same day): two-level defect structure — toggle geometry never yields a chart (absorption no-go, both levels); fiber poset = diamond with a tail; the strictification residue $\rho$ is gauge-silent, fiber-visible, with $\tau$ as its syndrome bit; the $[3,1,3]$ "Fano line" reading **retracted** (gauge/fiber conflation, caught by $\tau$) | **[Т при цит.]**; Fano-foundation problem restated in the purely intensional sector **[Г]** |
| T-236: holonomy blueprint — parts (a)–(b) stand; (c)–(d) corrected same day (axis orientations are pure gauge; superseded by T-237) | **[Т]** core; (c)–(d) **superseded** |
| T-237: the blueprint completed as a $\mathbb{Z}/2$ gauge theory on $\mathrm{PG}(2,2)$ — pure gauge $=$ line-side Hamming, flux $= 3$ bits, Wilson loops $=$ closed Boolean terms; syndrome completeness by strict gauge (H3.2 closed); designed metric $=$ canonical grading on the fiber (H3.3 closed, blueprint level) | **[Т]** (exhaustive verification); readings **[И]** |
| T-238: the flux chart — on fixed-signature families the gauge-invariant decided sector is the canonical chart candidate; term-definable charts factor through it; H3.1 reduced to signature alignment | **[Т]** (fixed signature); reduction reading **[И]** |

## Where this leads {#куда-ведёт}

- [Gap dynamics §2](/docs/core/dynamics/gap-dynamics#код-хэмминга) — the forward direction: the isomorphism $\mathrm{PG}(2,2) \cong H(7,4)$ at the level of Lindblad operators.
- [Topological protection, Shield I](/docs/applied/coherence-cybernetics/topological-protection#код-хэмминга) — the five shields; Σ turns Shield I from a property into a selector.
- [Minimality of N=7](/docs/proofs/minimality/theorem-minimality-7) and the [octonionic derivation](/docs/proofs/minimality/theorem-octonionic-derivation) — the three prior tracks; §9.3 there tabulates Track Σ against Tracks A and B.
- [Γ-canon](/docs/applied/research/gamma-canon) — the sixteen archetypes as codewords; the Σ protocol adds the diagnostic tier to the П-protocols; Lemma Σ.6 is the dictionary between its cyclic triads and the binary presentation.
- [Fano selection rules](/docs/physics/gauge-symmetry/fano-selection-rules), [evolution / T-114](/docs/core/dynamics/evolution) — the dynamical premises of T-225(d).
- [G₂-structure](/docs/physics/gauge-symmetry/g2-structure) — the forms $\varphi, \ast\varphi$ and the $14 \oplus 7$ split behind §6.
- [Status registry](/docs/reference/status-registry) — rows T-224, T-225.
- [The Fano fingerprint](/docs/applied/research/fano-fingerprint) — the dynamical companion: the polar rate law, fourteen sum rules, line tomography, and the $\mathfrak g_2$-shadow in observable decoherence rates (T-226).
- MSFS §8.1 (Intensional Grading) and the Diakrisis correspondence document — the Σ-Mor bridge: repaired and sharpened in §8-progress (T-229 [Т при Σ-FIB], $n_0(F) = \rho_{\mathrm{cov}}$); the fiber-level questions Q1 ∧ Q2 remain [Г].
