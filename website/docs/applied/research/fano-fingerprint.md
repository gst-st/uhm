---
sidebar_position: 10
title: "The Fano fingerprint of decoherence"
description: "Theorem T-226 [Т]: the 21 pairwise decoherence rates of the Γ-dynamics collapse to 7 values indexed by Fano polarity — r_ij = (G − T_k)/6 with k the third point of the line through i,j. Fourteen exact sum rules (the polar equalities), a closed-form line tomography γ = (½Nᵀ − ⅙J)T with condition number 2√2, the exact spectral gap and cooldown constant, and a selector converse: the sum rules hold identically iff the wiring is the Fano plane. The constraint space is a sign-twist of g₂ — the Lie shadow 21 = 14 + 7 reappears in observable rates, in polar duality to the Σ-compression pyramid."
---

# The Fano fingerprint: polar rates, sum rules, and line tomography

> *Ask a Fano-wired system how fast each of its twenty-one coherences dies, and it can only answer with seven numbers. The other fourteen degrees of freedom are not hidden — they are forbidden, and the forbidden directions are a sign-twist of $\mathfrak{g}_2$. What a system cannot do is as much of a fingerprint as what it does.*

:::tip Document status
The core is **Theorem T-226 [Т]**: elementary linear algebra and finite geometry over the exact channel forms of the corpus; every proof is complete, and every claim has been machine-verified in exact (symbolic) arithmetic. The dynamical premise — the per-coherence decay rate formula — is the canonical [Т] form of the Γ-dynamics. The identification of the mathematical rates with laboratory decoherence rates is **[И]**, as everywhere in the corpus. Technology items are **[С]/[О]**. Statuses are marked in place.
:::

**How this document is organized.** The document is self-contained given school linear algebra; the coding-theoretic and finite-geometric background, if wanted, is built from scratch in the [Σ-calculus primer §2](/docs/applied/research/syndrome-calculus#предварительные). §1 states the known premise — the exact per-coherence decay rates — and poses the question: as the seven line rates vary, what part of the 21-dimensional rate space is reachable? §2 proves the lemma chain; §3 assembles Theorem T-226 with all seven parts. §4 identifies the forbidden subspace with a sign-twist of $\mathfrak{g}_2$ — the second, dynamical apparition of the Lie shadow of the [Σ-calculus](/docs/applied/research/syndrome-calculus). §5 draws the protection reading. §6 gives the falsifiable prediction and the technology package; §7 records the machine verification; §8 is the status summary.

## §0. The first-order blind spot [Т] {#слепое-пятно}

Before the rates of §1, one layer down: the **linear** statistics of the seven lines see *nothing* of the plane's structure. Let $A(\ell)$ be the adjacency matrix of a line $\ell$ — the all-ones-off-diagonal on its three points, zero elsewhere. Summing over the seven lines,

$$
\sum_{p=1}^{7} A(\ell_p) \;=\; J - I,
$$

the adjacency matrix of the complete graph $K_7$: each of the $\binom{7}{2}=21$ pairs lies on exactly one line (Steiner $\lambda=1$), so every off-diagonal entry is hit exactly once. Its spectrum is $\{6,\,(-1)^{6}\}$ — one eigenvalue $6$ (the all-ones direction) and $-1$ with multiplicity six.

**Consequence [Т].** Any equal-weight quadratic form built from the lines — any pairwise covariance, any two-point statistic symmetric in the seven lines — is a function of $J-I$ alone, hence *indistinguishable from unstructured full connectivity*. The Fano wiring is invisible at first (pairwise) order; it becomes visible only on **triples** (the polar collapse of §3) and in the rate quadratics of §1–§2. This is the precise content of the "third-order principle": **structure begins at three.** (Machine-checked: `fanos_verify.py` V11.)

This static blind spot is the adjacency-level companion of the dynamical $\mathfrak g_2$-shadow of §4 (fourteen rate dimensions a two-point experiment can never reach): in both, what pairwise observation cannot see is exactly the structural content of the seven. It is also the theorem the [FANOS overlay](/docs/applied/fanos/fanos-specification) turns on — a heartbeat/ping mesh is a first-order statistic, so it is Fano-blind and cannot localise the faults that matter (equivocation); FANOS therefore diagnoses on triples.

## §1. The premise and the question {#вопрос}

The corpus fixes the dissipative half of the Γ-dynamics by the seven Fano projectors: one Lindblad channel per line $\ell_p = \{p,\, p{+}1,\, p{+}3\} \pmod 7$ of $\mathrm{PG}(2,2)$, with a nonnegative rate $\gamma_p$ per line ([Gap dynamics §2](/docs/core/dynamics/gap-dynamics#код-хэмминга), [Evolution](/docs/core/dynamics/evolution)). The exact channel form — the closed-form exponential established in the v2.2 canon — gives every off-diagonal coherence $(i,j)$, $i \neq j$, a pure exponential decay $e^{-r_{ij} t}$ with

$$
r_{ij} \;=\; \frac{1}{6} \sum_{p\,:\, |\ell_p \cap \{i,j\}| = 1} \gamma_p .
$$

In words: a line damages a coherence only if it *separates* the pair — contains exactly one of its endpoints. For the uniform assignment $\gamma_p = \bar\gamma$ this reproduces the corpus constant $r = \tfrac{2}{3}\bar\gamma$, consistent with the discrete Lüders multiplier $1/3$ per full cycle (T-110) and the cycle-time identity $\bar\gamma\tau_{\mathrm{cycle}} = \tfrac{3}{2}\ln 3$.

The seven $\gamma_p$ are the system's microscopic dials; the twenty-one $r_{ij}$ are what a rate experiment sees. So the natural — and, it turns out, sharply answerable — questions are:

> As $\gamma \in \mathbb{R}^7$ ranges over all line-rate assignments, **which vectors $r \in \mathbb{R}^{21}$ occur?** Which linear identities must every realizable $r$ satisfy? Can $\gamma$ be reconstructed from $r$, exactly and stably? And do the answers *detect* the Fano wiring itself?

## §2. The lemma chain {#леммы}

Throughout, $G := \sum_p \gamma_p$ is the **total flux** and $T_m := \sum_{p\,:\, m \in \ell_p} \gamma_p$ is the **point flux** of the axis $m$ — the sum of the rates of the three lines through $m$.

#### Lemma Φ.1 (line-sum identity) {#лемма-ф1}

*For every Fano line $\ell$:* $\displaystyle\sum_{m \in \ell} T_m = G + 2\gamma_\ell$.

**Proof.** $\sum_{m\in\ell} T_m = \sum_p \gamma_p\,|\ell_p \cap \ell|$. The line $\ell$ meets itself in $3$ points and every other line in exactly $1$ point (two distinct lines of a projective plane meet in one point). Hence the sum equals $3\gamma_\ell + \sum_{p \neq \ell}\gamma_p = 3\gamma_\ell + (G - \gamma_\ell) = G + 2\gamma_\ell$. $\blacksquare$

#### Lemma Φ.2 (general pair form) {#лемма-ф2}

*For an arbitrary $3$-uniform wiring (any family of $3$-element "lines", not necessarily Fano),*

$$
r_{ij} \;=\; \tfrac{1}{6}\bigl(T_i + T_j - 2 S_{ij}\bigr),
\qquad S_{ij} := \sum_{p\,:\,\{i,j\} \subseteq \ell_p} \gamma_p .
$$

**Proof.** Inclusion–exclusion on the endpoint count: the lines meeting $\{i,j\}$ in exactly one point are those through $i$, plus those through $j$, minus *twice* those through both. $\blacksquare$

#### Lemma Φ.3 (polar identity) {#лемма-ф3}

*In the Fano wiring, let $\lambda = \lambda(i,j)$ be the unique line through the pair $\{i,j\}$ and let $k$ be its third point. Then*

$$
r_{ij} \;=\; \frac{G - T_k}{6}.
$$

**Proof.** By Fano incidence $S_{ij} = \gamma_\lambda$ (exactly one line through the pair). Lemma Φ.1 for $\lambda = \{i,j,k\}$ gives $T_i + T_j = G + 2\gamma_\lambda - T_k$. Substituting into Lemma Φ.2: $r_{ij} = \tfrac{1}{6}(G + 2\gamma_\lambda - T_k - 2\gamma_\lambda) = (G - T_k)/6$. $\blacksquare$

#### Definition (polar partition) {#полярное-разбиение}

For a pair $\{i,j\}$ write $\pi(i,j) :=$ the third point of $\lambda(i,j)$ — its **polar point**. The **polar class** of an axis $k$ is $P_k := \{\ell \setminus \{k\} : \ell \ni k\}$ — the three pairs completing the three lines through $k$. The seven classes have three pairs each and partition all $\binom{7}{2} = 21$ pairs. This is the point–pair polarity of $\mathrm{PG}(2,2)$: the same triple structure that underlies the octonion product ($e_i e_j = \pm e_{\pi(i,j)}$) and the sixteen-archetype grammar of the [Γ-canon](/docs/applied/research/gamma-canon).

#### Lemma Φ.4 (image and injectivity) {#лемма-ф4}

*The linear map $M : \gamma \mapsto r$ has rank $7$; its image is exactly the space of functions constant on each polar class.*

**Proof.** By Lemma Φ.3, $r_{ij} = \rho_{\pi(i,j)}$ with $\rho_k := (G - T_k)/6$, so the image lies in the class-constant subspace, which has dimension $7$. For equality and injectivity it suffices to invert: Lemma Φ.5 reconstructs $\gamma$ linearly from $\rho$, so $M$ is injective and the image is the full class-constant space. $\blacksquare$

#### Lemma Φ.5 (line tomography) {#лемма-ф5}

*Let $N$ be the $7 \times 7$ point–line incidence matrix ($N_{kp} = 1$ iff $k \in \ell_p$; for the cyclic labeling it is the circulant with symbol $\{0,1,3\}$, $\det N = 24$). Then*

$$
N^{-1} \;=\; \tfrac{1}{2}N^{\mathsf T} - \tfrac{1}{6}J,
$$

*and the line rates are recovered from the seven polar values $\rho_k$ by*

$$
G = \tfrac{3}{2}\sum_k \rho_k, \qquad T_k = G - 6\rho_k, \qquad
\boxed{\;\gamma_p \;=\; 3\Bigl(\tfrac{1}{2}\sum_{k}\rho_k \;-\; \sum_{k \in \ell_p}\rho_k\Bigr).\;}
$$

**Proof.** $(N^{\mathsf T} N)_{pq} = |\ell_p \cap \ell_q|$ equals $3$ on the diagonal and $1$ off it, i.e. $N^{\mathsf T}N = 2I + J$; and $JN = 3J$ since every line has three points. Hence $(\tfrac12 N^{\mathsf T} - \tfrac16 J)N = \tfrac12(2I+J) - \tfrac12 J = I$. Summing $\rho_k = (G-T_k)/6$ over $k$ and using $\sum_k T_k = 3G$ gives $\sum_k \rho_k = \tfrac{2}{3}G$, i.e. the $G$-recovery; then $T = G\mathbf{1} - 6\rho$ and $\gamma = N^{-1}T = \tfrac12 N^{\mathsf T}T - \tfrac16 (\mathbf 1^{\mathsf T}T) \mathbf 1 = \tfrac12\sum_{k\in\ell_p}T_k - \tfrac12 G$, which simplifies to the boxed formula. $\blacksquare$

#### Lemma Φ.6 (conditioning) {#лемма-ф6}

*$M^{\mathsf T} M = \tfrac{1}{6}(I + J)$. Consequently the singular values of $M$ are $\tfrac{2}{\sqrt 3}$ (once, on the total-flux direction) and $\tfrac{1}{\sqrt 6}$ (multiplicity six), and the condition number is $2\sqrt2 \approx 2.83$.*

**Proof.** $(36\,M^{\mathsf T}M)_{pq}$ counts pairs meeting $\ell_p$ *and* $\ell_q$ in exactly one point each. For $p = q$: one endpoint on the line, one off it — $3 \cdot 4 = 12$ pairs. For $p \neq q$, with $z$ the intersection point: either one endpoint in $\ell_p \setminus z$ and the other in $\ell_q \setminus z$ ($2 \cdot 2 = 4$ pairs), or one endpoint equal to $z$ — which lies on both lines, so the other endpoint must avoid both ($7 - 5 = 2$ pairs); total $6$. Hence $36\,M^{\mathsf T}M = 12I + 6(J - I) = 6(I+J)$. The eigenvalues of $\tfrac16(I+J)$ are $\tfrac{8}{6} = \tfrac43$ on constants and $\tfrac16$ on the six-dimensional complement. $\blacksquare$

#### Lemma Φ.7 (selector converse) {#лемма-ф7}

*For a $3$-uniform wiring of $7$ lines on $7$ axes, the fourteen polar equalities (§3(ii)) hold identically in $\gamma$ **iff** every pair of axes lies on exactly one line — i.e. iff the wiring is a $2$-$(7,3,1)$ design, hence the Fano plane.*

**Proof.** ($\Leftarrow$) is Lemma Φ.3. ($\Rightarrow$) The total pair-coverage satisfies $\sum_{\{i,j\}} S^{\#}_{ij} = 7\binom{3}{2} = 21$, where $S^{\#}_{ij}$ is the number of lines through the pair; so if the coverage is not identically $1$, some pair is covered $0$ times. For such a pair Lemma Φ.2 gives $r_{ij} = \tfrac16(T_i + T_j)$ — a functional of $\gamma$ supported on the *six* lines through $i$ or $j$, while any pair with coverage $1$ has the four-line polar form. Two linear functionals with different coefficient vectors cannot be identically equal, and a direct check shows no assignment of the $21$ pairs into $7$ equality-triples survives (in the explicit one-line rewiring of §7, seven of the fourteen equalities already fail identically). A $2$-$(7,3,1)$ design is the Fano plane up to relabeling — the uniqueness chain of [Theorem Σ, Lemmas Σ.1–Σ.2](/docs/applied/research/syndrome-calculus#t-224). $\blacksquare$

## §3. Theorem T-226 (the Fano fingerprint) {#t-226}

**Theorem T-226 [Т].** *Let the dissipative Γ-dynamics carry line rates $\gamma \in \mathbb{R}^7_{\geq 0}$ on the Fano wiring, and let $r \in \mathbb{R}^{21}$ be the exact per-coherence decay rates. Then:*

**(i) Polar law.** $r_{ij} = \rho_{\pi(i,j)}$ where $\rho_k = (G - T_k)/6$: the twenty-one rates take **at most seven values**, constant on the polar classes; a rate depends on the pair only through its polar point.

**(ii) Fourteen sum rules (polar equalities).** The realizable set is exactly the $7$-dimensional subspace of class-constant vectors. Equivalently: within each polar class the three rates coincide —

$$
r_{ij} = r_{i'j'} \quad\text{whenever}\quad \pi(i,j) = \pi(i',j'),
$$

fourteen independent linear identities that every Fano-wired system must satisfy for **every** value of the line rates.

**(iii) Line tomography.** The map $\gamma \mapsto r$ is injective, and inverts in closed form: measuring the seven polar values $\rho_k$ yields $\gamma_p = 3\bigl(\tfrac12 \sum_k \rho_k - \sum_{k \in \ell_p} \rho_k\bigr)$ exactly (Lemma Φ.5). The per-line dissipation strengths are *observables*, not fit parameters.

**(iv) Conditioning.** $M^{\mathsf T}M = \tfrac16(I+J)$; singular values $2/\sqrt3$ and $1/\sqrt6$ ($\times 6$); condition number $2\sqrt2$. Rate noise propagates into $\gamma$ with amplification at most $\sqrt6 \approx 2.45$ — the tomography is numerically benign.

**(v) Exact gap and cooldown.** On the coherence sector, the dissipative generator has spectrum $\{-\rho_k\}$ with multiplicity $6$ per polar class (three pairs, real and imaginary parts; classes with equal $\rho_k$ merge); its spectral gap is

$$
\Delta \;=\; \min_k \rho_k \;=\; \frac{G - \max_k T_k}{6},
$$

so the neurogenesis cooldown bound of T-39a becomes fully explicit: $\tau_{\mathrm{cool}} \geq 1/\Delta = 6/(G - \max_k T_k)$. Uniform rates give $\Delta = \tfrac23\bar\gamma$.

**(vi) Selector.** The fourteen polar equalities hold identically in $\gamma$ **iff** the wiring is the Fano plane (Lemma Φ.7). The sum rules are therefore not bookkeeping but a *fingerprint*: they detect the combinatorial grammar of the dynamics itself, independently of the octonionic track — an operational companion to the diagnosability selector of [Theorem Σ](/docs/applied/research/syndrome-calculus#t-224).

**(vii) Two-sided budget.** Measuring rates costs $7$ numbers, not $21$; the other $14$ dimensions are consistency checks for free. Dually, the seven $\rho_k$ determine and are determined by the seven $\gamma_p$ — the rate spectrum and the line spectrum are linearly equivalent charts of the same dial space.

*Proof.* Parts (i)–(iv) are Lemmas Φ.3–Φ.6; (v) follows from the exact channel form (each coherence is an eigenvector of the dissipative factor with eigenvalue $-r_{ij}$, populations are preserved) together with (i); (vi) is Lemma Φ.7; (vii) restates (ii)–(iii). $\blacksquare$

**Remark (what is [Т] and what is [И]).** The theorem is exact linear algebra over the [Т] channel forms. Its *empirical* use — reading measured decoherence rates of a candidate septarchitecture as the $r_{ij}$ — inherits the usual [И] identification of axes with measured channels, as in every prediction of the corpus.

## §3a. A worked example, end to end {#разобранный-пример}

Abstract theorems earn their keep on concrete numbers. Take the seven line rates to be simply $\gamma_p = p + 1$ (in whatever units the dissipation is measured), $p = 0, \dots, 6$ — deliberately non-uniform, so that all the structure is visible. Then $G = 1 + 2 + \cdots + 7 = 28$.

**Step 1 — point fluxes.** The axis $k$ lies on the three lines $\ell_k, \ell_{k-1}, \ell_{k-3}$ (indices mod 7), so $T_k = \gamma_k + \gamma_{k-1} + \gamma_{k-3}$:

| axis $k$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| lines through $k$ | $\ell_0,\ell_6,\ell_4$ | $\ell_1,\ell_0,\ell_5$ | $\ell_2,\ell_1,\ell_6$ | $\ell_3,\ell_2,\ell_0$ | $\ell_4,\ell_3,\ell_1$ | $\ell_5,\ell_4,\ell_2$ | $\ell_6,\ell_5,\ell_3$ |
| $T_k$ | $13$ | $9$ | $12$ | $8$ | $11$ | $14$ | $17$ |
| $\rho_k = \tfrac{28 - T_k}{6}$ | $\tfrac{5}{2}$ | $\tfrac{19}{6}$ | $\tfrac{8}{3}$ | $\tfrac{10}{3}$ | $\tfrac{17}{6}$ | $\tfrac{7}{3}$ | $\tfrac{11}{6}$ |

Consistency checks land exactly: $\sum_k T_k = 84 = 3G$ and $\sum_k \rho_k = \tfrac{56}{3} = \tfrac{2}{3}G$ (Lemma Φ.5's $G$-recovery).

**Step 2 — the twenty-one rates are these seven numbers.** Every coherence $(i,j)$ decays at $\rho_{\pi(i,j)}$. For instance the pair $\{1,3\}$ lies on $\ell_0 = \{0,1,3\}$, its polar point is $0$, so $r_{13} = \rho_0 = \tfrac{5}{2}$ — and the *same* value is shared by the other two pairs polar to $0$: $\{4,5\}$ (the rest of $\ell_4 = \{4,5,0\}$) and $\{2,6\}$ (the rest of $\ell_6 = \{6,0,2\}$). One pair from each of the three lines through the polar point; three rates per point, seven values in all, fourteen equalities for free.

**Step 3 — tomography, run backwards.** Reconstruct $\gamma_0$ from the seven polar values: $\tfrac12\sum_k \rho_k = \tfrac{28}{3}$, the line $\ell_0 = \{0,1,3\}$ has polar sum $\rho_0 + \rho_1 + \rho_3 = \tfrac{5}{2} + \tfrac{19}{6} + \tfrac{10}{3} = 9$, and

$$
\gamma_0 \;=\; 3\Bigl(\tfrac{28}{3} - 9\Bigr) \;=\; 28 - 27 \;=\; 1. \checkmark
$$

All seven $\gamma_p$ come back exactly this way (machine-checked in rational arithmetic) — the dials are read off the rates with no fitting.

**Step 4 — gap, cooldown, protection.** The largest point flux is $T_6 = 17$, so the *slowest* rate is $\rho_6 = \tfrac{11}{6}$: the spectral gap is $\Delta = \tfrac{11}{6}$ and the exact cooldown constant is $\tau_{\mathrm{cool}} = 1/\Delta = \tfrac{6}{11}$ (in the same units). The three longest-lived coherences are the polar class of axis $6$: the pairs $\{3,4\}, \{1,5\}, \{0,2\}$ — sitting on the three strongest lines of the example, yet themselves untouched by them: guarded, vicariously, by the very flux that flows *through* their polar point. That is the protection reading of §5 in numbers.

## §4. The $\mathfrak{g}_2$-shadow of the forbidden space {#g2-тень}

The [Σ-calculus](/docs/applied/research/syndrome-calculus#t-225) records the Lie shadow $\mathfrak{so}(7) = \mathfrak{g}_2 \oplus \mathrm{Im}\,\mathbb{O}$, the split $21 = 14 + 7$ of the *generator* algebra. The fingerprint produces the same split in the *observable rate space* — and the two are the same split, up to an explicit sign twist.

Identify $\mathbb{R}^{21}$ with the space of off-diagonal patterns indexed by pairs. Let $\varphi$ be the associative $3$-form of the octonion frame aligned with the corpus labeling ($e_i e_j = \varepsilon_{ij}\, e_{\pi(i,j)}$ on lines, $\varepsilon_{ij} = \varphi_{ij\pi(i,j)} \in \{\pm1\}$), and let $W = \mathrm{diag}(\varepsilon_{ij})$ be the **orientation twist** of pair space.

**Proposition C-226 [Т].** *Let $c : \mathbb{R}^{21} \to \mathbb{R}^7$ be the unsigned polar collapse ($(c\,r)_k = \sum_{\pi(i,j)=k} r_{ij}$) and $c_\varphi : \Lambda^2\mathbb{R}^7 \to \mathbb{R}^7$ the $\varphi$-contraction $\omega \mapsto \sum_{i<j} \varphi_{ijk}\,\omega_{ij}$. Then $c_\varphi = c \circ W$. Consequently $W$ carries the standard $G_2$-decomposition $\mathfrak{so}(7) \cong \Lambda^2\mathbb{R}^7 = \mathfrak{g}_2 \oplus \iota_\varphi(\mathrm{Im}\,\mathbb{O})$ — with $\mathfrak{g}_2 = \ker c_\varphi$ and $\iota_\varphi(v) = v \lrcorner \varphi$ — onto the fingerprint decomposition*

$$
\mathbb{R}^{21} \;=\; \underbrace{\{\text{forbidden directions}\}}_{W(\mathfrak g_2),\ \dim 14} \;\oplus\; \underbrace{\{\text{realizable rates}\}}_{W(\iota_\varphi(\mathrm{Im}\,\mathbb O)),\ \dim 7}.
$$

**Proof.** $c_\varphi = c \circ W$ holds entry by entry, since $\varphi_{ijk} \neq 0$ exactly when $k = \pi(i,j)$, with value $\varepsilon_{ij}$; the kernel/image correspondence follows because $W$ is an involution. The identification $\mathfrak g_2 = \ker c_\varphi$ and the complement $\iota_\varphi$ are the standard $G_2$-module decomposition of $\Lambda^2\mathbb{R}^7$. $\blacksquare$

**Reading [И].** The fourteen dimensions a rate experiment can never see are the sign-twisted $\mathfrak{g}_2$: *the symmetry algebra of the theory is exactly the diagnostically dark subspace of its own decoherence spectrum*. And the duality is polar: the Σ-compression pyramid of T-225 aggregates coherences **by lines** (content monitoring), while the dynamics collapses rates **by polar points**. Lines and points are exchanged by the self-duality of $\mathrm{PG}(2,2)$ — the measurement pyramid and the decay spectrum are Fano-dual faces of the same $21 = 14 + 7$.

## §5. The protection reading {#охрана}

Two structural facts fall out of the polar law and deserve their own sentences.

**Intra-line immunity [Т].** A line never damages its own coherences: if both endpoints of a pair lie on $\ell$, then $|\ell \cap \{i,j\}| = 2$ and $\ell$ contributes nothing to $r_{ij}$. This is Shield I of [topological protection](/docs/applied/coherence-cybernetics/topological-protection#код-хэмминга) surfacing at the *rate* level: the dissipative grammar is structurally incapable of eroding the coherence of its own syndrome triples.

**Polar guardianship [Т math, И reading].** $r_{ij} = (G - T_{\pi(i,j)})/6$ is *anti-monotone* in the polar point's flux: strengthening the three lines through an axis $k$ slows the decay of the three coherences polar to $k$. Each axis guards not its own coherences but the polar ones — protection in $\mathrm{PG}(2,2)$ is always vicarious. The best-protected coherences of a Γ-state are those polar to its highest-flux axis — and those same coherences *set the spectral gap* (T-226(v)): the strongest guardian's wards decay slowest, so maximal protection and slow late-time convergence are two faces of one number. The worked example of §3a shows both faces concretely.

## §6. Falsifiability and technology {#следствия-технологии}

**Prediction Σ-P2 (candidate for the Pred registry).** In any rate-resolved Γ-tomography of a candidate septarchitecture, the measured pairwise decoherence rates must satisfy the fourteen polar equalities within experimental error, for *every* dissipation regime — the identities are parameter-free. A stable, reproducible violation in even one polar class falsifies the Fano wiring of the dissipative dynamics directly, independently of the octonionic track. Conversely, verifying the fourteen identities across *two or more distinct* dissipation regimes (different $\gamma$) is strong evidence for the wiring, by the selector (T-226(vi)): a single one-line rewiring already breaks seven of the fourteen identically.

**Technology package.**

1. **Rate-monitoring budget [С].** Seven polar values instead of twenty-one pairwise rates — a threefold reduction, with the remaining fourteen dimensions repurposed as built-in consistency alarms. This composes with the Σ-compression pyramid of [T-225](/docs/applied/research/syndrome-calculus#t-225): content monitoring compresses by lines, rate monitoring by polar points — together they instrument both Fano-dual faces of the coherence matrix at $7 + 7$ observables.
2. **Line-resolved dissipation spectroscopy ("Fano tomography") [С].** The boxed formula of Lemma Φ.5 turns per-line dissipation strengths $\gamma_p$ into direct observables with noise amplification $\leq \sqrt6$ (T-226(iv)) — no fitting, no regularization. For the Γ-tomograph tiers this yields the per-line health of the dissipative grammar from the same data that currently yields only aggregate decay.
3. **Exact cooldown budget for SYNARC [О].** T-39a's neurogenesis cooldown becomes the explicit runtime constant $\tau_{\mathrm{cool}} = 6/(G - \max_k T_k)$, computable from the current line rates in $O(1)$; the runtime can *tighten* its cooldown adaptively as the dissipation profile shifts, instead of using the worst-case constant.
4. **Design rule [О].** To protect a chosen coherence $(i,j)$ passively, invest flux in the lines through its polar point — not in its own line (which is neutral to it) and not in the remaining four (which erode it). Vicarious protection is a design lever unavailable to architectures without the $\lambda = 1$ grammar.

## §7. Machine verification {#верификация}

All claims were verified in exact arithmetic (symbolic $\gamma$, rational linear algebra):

| Check | Result |
|---|---|
| Every pair meets exactly $4$ lines once; $S_{ij} \equiv 1$ line | ✓ |
| $r_{ij} - (G - T_{\pi(i,j)})/6 = 0$ symbolically, all $21$ pairs | ✓ |
| $\operatorname{rank} M = 7$; image $=$ class-constant space | ✓ |
| $N^{-1} = \tfrac12 N^{\mathsf T} - \tfrac16 J$; $\det N = 24$; tomography exact | ✓ |
| $M^{\mathsf T}M = \tfrac16(I+J)$; singular values $2/\sqrt3,\ 1/\sqrt6^{(\times 6)}$ | ✓ |
| $c_\varphi = c \circ W$; both kernels $14$-dimensional | ✓ |
| One-line rewiring ($\{0,2,6\} \to \{0,1,6\}$): $7/14$ polar equalities fail identically | ✓ |

The verification scripts follow the M1 discipline of the SYNARC programme: independent implementation, exact arithmetic, and the falsifying counter-model (the rewired plane) checked alongside the theorem. A **third**, independent-language verification also passes: a Verum program (integer arithmetic only, `sigma_wave_check.vr` in the SYNARC repository) re-derives the polar law on all 21 pairs, the line-sum tomography identity, and the polar partition — alongside the Turyn–Golay enumerator of the Σ-calculus §8a — reporting `ALL PASS`.

## §8. Status summary {#сводка}

| Claim | Status |
|---|---|
| Lemmas Φ.1–Φ.7 | **[Т]** |
| Theorem T-226 (i)–(vii) | **[Т]** |
| Proposition C-226 ($\mathfrak g_2$-shadow, $c_\varphi = c \circ W$) | **[Т]** (reading — [И]) |
| Intra-line immunity; polar guardianship | **[Т]** (guardianship reading — [И]) |
| Prediction Σ-P2 (polar equalities in tomography) | falsifiable, **[И]** identification |
| Rate budget $21 \to 7$; Fano tomography; adaptive cooldown | **[С]/[О]** |

## Where this leads {#куда-ведёт}

- [Σ-calculus](/docs/applied/research/syndrome-calculus) — the static selector (T-224) and the measurement pyramid (T-225); this document is their dynamical, rate-level companion, in polar duality to the pyramid.
- [Gap dynamics §2](/docs/core/dynamics/gap-dynamics#код-хэмминга) — the Fano–Hamming wiring of the Lindblad operators whose exact channel forms feed §1.
- [Topological protection, Shield I](/docs/applied/coherence-cybernetics/topological-protection#код-хэмминга) — intra-line immunity is Shield I at the rate level.
- [Γ-canon](/docs/applied/research/gamma-canon) — the polar (octonionic) triple structure $e_i e_j = \pm e_{\pi(i,j)}$ that indexes the rate classes.
- [Measurement protocol](/docs/applied/research/measurement-protocol) — where the polar-rate observables and the $\gamma$-tomography slot into the experimental tiers.
- [Status registry](/docs/reference/status-registry) — row T-226.
