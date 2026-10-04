---
slug: /proofs/categorical/categorical-formalism
sidebar_position: 1
title: "Categorical Formalism"
format: md
---

# Categorical formalism: processes, sheaves and interpretation

:::info Revised mathematical foundation — 2026-10-03
The process category, the site of open subsets, the numerical state and the phenomenal interpretation have different types. This page proves constructions after their data have been specified. A sheaf topos does not by itself select seven dimensions, a Hamiltonian, a state encoder or a phenomenal bridge. The canonical notation is fixed in the [mathematical kernel](/docs/reference/mathematical-kernel).
:::

Statuses: **[D]** definition or chosen model; **[T]** theorem with stated hypotheses; **[C]** conditional identification; **[H]** hypothesis; **[I]** interpretation; **[Pr]** research programme; **[✗]** withdrawn claim.

## 1. State-preserving process category {#1-категория-densitymat}

Fix finite-dimensional Hilbert spaces, using a small skeleton. In the system category $\mathbf{CPTP}$ an object is a system $\mathcal H$ and an arrow is a linear completely positive trace-preserving map $\Lambda:\mathcal B(\mathcal H)\to\mathcal B(\mathcal K)$. Its state assignment is the functor

$$
\mathcal D:\mathbf{CPTP}\to\mathbf{Set},\qquad \rho\longmapsto\Lambda(\rho).
$$

**Definition 1.1 [D].** The category $\mathbf{DensityMat}=\int\mathcal D$ has objects $(\mathcal H,\rho)$ and arrows $\Lambda:(\mathcal H,\rho)\to(\mathcal K,\sigma)$ satisfying $\Lambda(\rho)=\sigma$. The notation $\mathbf{DensityMat}_N$ means its restriction to the fixed system $\mathbb C^N$.

### Channels and composition {#12-структура-морфизмов-cptp-каналы}

**Theorems 1.1–1.2 [T].** In finite dimension a channel has a Kraus representation

$$
\Lambda(X)=\sum_aK_aXK_a^\dagger,\qquad\sum_aK_a^\dagger K_a=I.
$$

Composition is ordinary function composition; Kraus operators for $\Psi\Lambda$ are $B_bK_a$. The identity has the single Kraus operator $I$. The endpoint condition is preserved since $\Psi\Lambda(\rho)=\Psi(\sigma)$. These facts prove all category axioms, including strict associativity. [Watrous, chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.double.2.pdf).

### Terminal object and tensor product {#13-аксиомы-категории-для-densitymat}

For every pair of states there is a replacement channel $X\mapsto\operatorname{Tr}(X)\sigma$; hom-sets here are never empty. For $N>1$, **no object of $\mathbf{DensityMat}_N$ is terminal**: its endomorphisms include distinct identity and replacement channels. In the category with all system dimensions, $(\mathbb C,1)$ is terminal: the unique channel to it is trace. This terminal system supplies no preferred preparation on $\mathbb C^7$.

The system category and the category with varying dimensions are symmetric monoidal under $\otimes$. Tensoring two seven-dimensional systems produces dimension $49$, so $\mathbf{DensityMat}_7$ is not closed under this tensor product. This tensor is not a Cartesian product. A stationary numerical state is neither a terminal system nor a terminal object of the fixed-dimension process category.

## 2. Defining an experiential category {#2-категория-exp}

A topological space $Y$ of candidate qualities or experiential configurations is additional data [D/I]. One can construct several valid categories from it, but they are different:

- The fundamental groupoid $\Pi_1(Y)$ has points as objects and endpoint-preserving homotopy classes of paths as arrows. Every arrow is invertible.
- The Moore-path category has paths with a specified nonnegative duration. Concatenation adds durations and is strictly associative, with the duration-zero constant path as identity.
- A category of directed physical histories requires a chosen direction, allowable paths and equivalence relation compatible with composition.

### Morphisms and history {#22-морфизмы-в-категории-exp}

Ordinary parametrised paths on $[0,1]$, concatenated by halving the interval, are not strictly associative and do not have strict constant-path identities. Taking homotopy classes gives $\Pi_1(Y)$; using Moore paths gives a strict category. Neither construction is equivalent, without extra hypotheses, to componentwise continuous maps or to CPTP processes. A path inverse in $\Pi_1(Y)$ is topological, not a physical reversal of a dissipative process.

The old assertion that these three definitions of $\mathbf{Exp}$ were equivalent is withdrawn [✗]. History is a supplied or constructed path object once $Y$ and its path rules exist; a symbol $\pi_1(\mathbf{Exp}_2)$ does not construct an unspecified bicategory or derive an arrow of time.

## 3. Object readout and degeneracies {#3-функтор-f-на-объектах}

Choose a readout $q:X_N\to Y$. Its interpretation as experiential content is [I/H]. Spectral decomposition alone gives the basis-independent data

$$
\rho=\sum_{\lambda\in\operatorname{Spec}(\rho)}\lambda\,P_\lambda.
$$

The spectral projections onto distinct eigenspaces are canonical. Individual eigenrays inside a degenerate eigenspace are not: replacing its basis by any unitary leaves $\rho$ unchanged. Hence an eigenray readout needs a gauge or must quotient by this ambiguity; sorted eigenvectors are not a globally continuous coordinate chart.

An $E$ **axis** in the native seven-dimensional space has rank-one projection $P_E$. Its unnormalised block $P_E\Gamma P_E=\gamma_{EE}P_E$ is a scalar weight, and, when $\gamma_{EE}>0$, the normalised block is always $P_E$. It is not a nontrivial $\mathbb{CP}^{n-1}$ quality space. Such a space requires an explicitly enlarged $E$ register of dimension $n>1$, or a different readout. Compressing to a block is CP and trace-nonincreasing; normalising it is generally nonlinear and undefined at zero weight. Partial trace requires a chosen tensor decomposition and differs from conditioning on an axis.

## 4. When a readout defines process arrows {#4-функтор-f-на-морфизмах}

A state map $q$ supplies no automatic action on arrows. Here is a precise criterion.

**Proposition 4.1 (descent of processes) [T].** Assume $q:X_N\twoheadrightarrow Y$ is surjective. A process $\Lambda$ induces a unique set map $f_\Lambda:Y\to Y$ satisfying $q\Lambda=f_\Lambda q$ iff

$$
q(\rho)=q(\sigma)\quad\Longrightarrow\quad q(\Lambda\rho)=q(\Lambda\sigma).\tag{DC}
$$

*Proof.* Necessity follows by applying $f_\Lambda$. Under (DC), define $f_\Lambda(q(\rho))=q(\Lambda\rho)$; it is independent of the representative and is unique by surjectivity. If $q$ is a quotient map and $q\Lambda$ is continuous, the descended map is continuous. $\square$

The channels satisfying (DC) form a monoid under composition. Define a category on points of $Y$ with arrows the actual descended maps sending one endpoint to another. The assignment $(\rho,\Lambda)\mapsto(q(\rho),f_\Lambda)$ is then a functor on the corresponding restricted process category. Descent for all channels is an additional assertion, not a consequence of a norm bound.

For example, reading only $\gamma_{EE}$ fails (DC) for arbitrary channels: two states with the same $E$ weight and different $A$ weights acquire different $E$ weights after swapping $E$ and $A$. Thus arbitrary channels have no well-defined restriction $\Lambda|_E$ as an endomorphism of the readout space.

## 5. Functoriality and higher coherence {#5-доказательство-функториальности}

**Proposition 5.1 [T].** For the descended maps above, $f_{\mathrm{id}}=\mathrm{id}$ and $f_{\Psi\Lambda}=f_\Psi f_\Lambda$.

*Proof.* Both equations hold after composition with the surjection $q$; uniqueness in Proposition 4.1 gives the result. $\square$

This theorem applies to the declared descent category. It does not prove existence of a phenomenal functor for unrestricted quantum processes. Defining $Y=X_N$ and copying the process category produces an isomorphic labelled category, but that formal relabelling does not prove a phenomenal interpretation.

### The former 2-categorical completion {#2-категорный-функтор}

The former Theorem 5.3/T-192 that repaired functoriality by unspecified natural transformations is withdrawn [✗]. A CP map between matrix algebras is a linear map, generally not a $*$-homomorphism or a functor between the algebras viewed as categories. One can always regard an ordinary process category as a locally discrete 2-category, with identity 2-cells only. A richer bicategory requires specified hom-categories, horizontal/vertical composition, associators and unitors, together with the pentagon and triangle identities. Naming these structures does not construct them or prove that $q$ lifts to a pseudofunctor.

## 6. Topos structure and metric enrichment {#6-топосная-структура}

### 6.1 Process categories and sheaf categories

For $N>1$ the missing terminal object already prevents $\mathbf{DensityMat}_N$ from being a topos. No conclusion about an unspecified $\mathbf{Exp}$ follows from that observation. An open-cover sheaf category on a specified space is a separate construction, established in §6.3.

### 6.2 Metric data

A distance between state outputs at one test state is only a pseudometric on channels: distinct channels can agree on that state. Trace distance between all outputs gives a channel metric after taking a supremum; compositional enrichment needs a stated base and composition inequality. The following quality-space result is independent of those channel choices.

#### 6.2.1 The quality space as a Lawvere metric space: enriched Yoneda {#enriched-yoneda}

The enrichment of item 2 can be taken one level down, on the qualities themselves. Lawvere (1973) observed that a metric space *is* a category enriched over $\mathcal V = ([0,\infty], \geq, +, 0)$: the hom-object from $a$ to $b$ is the number $d(a,b)$, composition is the triangle inequality $d(a,b) + d(b,c) \geq d(a,c)$, identities are $0 \geq d(a,a)$ (F. W. Lawvere, "Metric spaces, generalized logic, and closed categories", *Rend. Sem. Mat. Fis. Milano* 43: 135–166, 1973; reprinted in *Repr. Theory Appl. Categ.* 1, 2002). Tsuchiya, Phillips & Saigo (*Conscious. Cogn.* 101: 103319, 2022, doi:10.1016/j.concog.2022.103319) brought enriched categories to qualia: graded dissimilarity as the hom-object and the enriched Yoneda lemma, by which a quale is characterised by its dissimilarities to all other qualia "up to an (enriched) isomorphism". The theorem below is that construction for UHM's own quality space, and what the specific choice of space adds to it.

Let $Q = \mathbb P(\mathcal H_E) \cong \mathbb{CP}^{n-1}$ ($n = \dim \mathcal H_E$) with the Fubini–Study distance $d([\psi],[\varphi]) = \arccos |\langle \psi | \varphi \rangle| \in [0, \pi/2]$. A $\mathcal V$-presheaf on $Q$ is a function $\phi: Q \to [0,\infty]$ with $\phi(a) \leq d(a,b) + \phi(b)$; presheaves form a $\mathcal V$-category $\widehat Q$ with hom $[\phi, \psi] = \sup_{x} (\psi(x) \ominus \phi(x))$, where $y \ominus x = \max(y - x, 0)$ is the internal hom of $\mathcal V$. The Yoneda map is $\mathbf y(a) = d(-, a)$.

:::tip Theorem (Enriched Yoneda for qualia) [T]
1. **Enriched Yoneda lemma.** $[\mathbf y(a), \phi] = \phi(a)$ for every presheaf $\phi$.
2. **Isometry.** $[\mathbf y(a), \mathbf y(b)] = d(a,b)$; since $d$ is symmetric, also $\sup_x |d(x,a) - d(x,b)| = d(a,b)$ — the Yoneda embedding is the Kuratowski isometric embedding of $Q$ into bounded functions.
3. **Enriched isomorphism is identity.** $a \cong b$ in the $\mathcal V$-category $Q$ iff $d(a,b) = 0 = d(b,a)$ iff $a = b$. For UHM's quality space the "up to enriched isomorphism" of the general lemma is "exactly".
4. **Finite-probe Yoneda.** Let $S \subset Q$ be finite with covering radius $\delta$ (every $a$ has some $s \in S$ with $d(a,s) \leq \delta$). The profile $\mathbf y_S(a) = (d(s,a))_{s \in S}$ satisfies

$$
d(a,b) - 2\delta \;\leq\; \max_{s \in S} |d(s,a) - d(s,b)| \;\leq\; d(a,b).
$$

Dissimilarities to finitely many probes fix a quality up to $2\delta$ plus the measurement error of the profile.
5. **How many probes.** The Fubini–Study ball of radius $r$ in $\mathbb{CP}^{n-1}$ has normalised volume $\sin^{2(n-1)} r$. Hence a probe set with covering radius $\delta$ has at least $\sin^{-2(n-1)}\delta$ elements, and one with at most $\sin^{-2(n-1)}(\delta/2)$ elements exists. For $n = 2$ and $\delta = 0.1$: between 100 and 401 probes; for $n = 3$ and $\delta = 0.2$: between 642 and 10 067. Read backwards: 93 probe colours (the set of Kawakita et al.) cannot give a covering radius below $\arcsin(1/\sqrt{93}) \approx 0.104$ even on $\mathbb{CP}^1$.
6. **Cauchy completeness.** $Q$ is compact, hence complete, hence Cauchy complete as a $\mathcal V$-category (Lawvere 1973): every Cauchy presheaf is representable — a quality defined as the limit of a Cauchy sequence of relational profiles exists in $Q$.
7. **What the commitment excludes.** A finite matrix of dissimilarities $(d_{ij})$ is realised by rays of $\mathbb{CP}^{n-1}$ iff for some phases $\theta_{ij} = -\theta_{ji}$ the Hermitian matrix $G_{ij} = \cos(d_{ij})\, e^{i\theta_{ij}}$, $G_{ii} = 1$, is positive semidefinite of rank at most $n$. In particular at most $n$ qualities can be pairwise at the maximal distance $\pi/2$.
:::

**Proof.** (1) Take $x = a$: $\phi(a) \ominus d(a,a) = \phi(a)$, so $[\mathbf y(a), \phi] \geq \phi(a)$; and for every $x$, $\phi(x) \leq d(x,a) + \phi(a)$ gives $\phi(x) \ominus d(x,a) \leq \phi(a)$. (2) is (1) with $\phi = \mathbf y(b)$, plus symmetry of $d$. (3) Isomorphism in a $\mathcal V$-category means $0 \geq Q(a,b)$ and $0 \geq Q(b,a)$; $d$ separates points. (4) The upper bound is the triangle inequality. For the lower one pick $s$ with $d(s,a) \leq \delta$; then $d(s,b) \geq d(a,b) - \delta$, so $d(s,b) - d(s,a) \geq d(a,b) - 2\delta$. (5) For Haar-random $\psi$, $|\langle \psi | c \rangle|^2$ has the Beta$(1, n-1)$ law, so $\Pr[d(\psi, c) \leq r] = \Pr[|\langle \psi | c\rangle|^2 \geq \cos^2 r] = (1 - \cos^2 r)^{n-1}$. $N$ balls of radius $\delta$ cover only if $N \sin^{2(n-1)}\delta \geq 1$; a maximal $\delta$-separated set is a $\delta$-cover, and its balls of radius $\delta/2$ are disjoint. (6) Lawvere's theorem: for metric spaces Cauchy completion is metric completion. (7) The Gram matrix of unit vectors $v_1, \dots, v_m \in \mathbb C^n$ is positive semidefinite of rank $\leq n$ with $|G_{ij}| = \cos d_{ij}$, and every such matrix is a Gram matrix of vectors in $\mathbb C^n$; $m$ pairwise-orthogonal unit vectors need $m \leq n$. $\square$

Items 1, 2, 4 and 5 are checked in `check_core_numbers.py` (`test_enriched_yoneda_embedding_of_fubini_study_rays_is_an_isometry`: $n = 2, 3, 7$; probe bound on $\mathbb{CP}^1$; ball volumes on $\mathbb{CP}^1$ and $\mathbb{CP}^2$).

**What this adds to Tsuchiya–Phillips–Saigo — and what it does not.** Their enriched Yoneda lemma holds for any quality space that experiments may find; it identifies a quale up to enriched isomorphism. UHM commits in advance to one space, and the commitment buys three things: identification is exact (item 3); it is quantitative for finitely many probes, with an explicit design count (items 4–5); and it is refutable — item 7 names dissimilarity matrices that no ray configuration realises. The refutation needs a calibration $f$ from perceived dissimilarity to $d$, which is not fixed; with $f$ only assumed monotone, the test is ordinal and weaker. Two further links: an enriched equivalence between two separated metric spaces is an isometric bijection, so the Gromov–Wasserstein alignment used by Kawakita et al. (a distance that vanishes exactly on isomorphic metric measure spaces — F. Mémoli, *Found. Comput. Math.* 11: 417–487, 2011) is a relaxed test of enriched equivalence between two subjects' quality spaces; and none of this touches whether a system is conscious — the quality geometry and the predicate $\mathrm{Cons}(S)$ are independent (the eigenrays of $\Gamma$ do not depend on its spectrum, $P$ does not depend on the eigenrays; [measurement protocol](/docs/applied/research/measurement-protocol#substitution-position)). The identification of experiences with rays remains [I].

### 6.3 The state-space site and continuous channel maps {#63-топология-гротендика-на-densitymat-и-exp}

:::info Canonical construction — revised 2026-10-03
The process category of states and CPTP arrows is separate from the site of open subsets of the state space. The site below constructs an $\infty$-topos rigorously. CPTP contractivity ensures continuity of process maps; it does not give categorical pullbacks of channels or a covering topology on their process category.
:::

#### 6.3.1 Bures open-cover site {#631-bures-топология-на-densitymat}

Fix $N<\infty$ and $X_N=\mathcal D(\mathbb C^N)$. With squared Uhlmann fidelity

$$
F(\rho,\sigma)=\left(\mathrm{Tr}\sqrt{\sqrt\rho\,\sigma\sqrt\rho}\right)^2,
\qquad d_B(\rho,\sigma)=\sqrt{2(1-\sqrt{F(\rho,\sigma)})},
$$

$X_N$ is a compact metric space whose topology agrees with the usual finite-dimensional state-space topology. The metric is defined also at rank-deficient states; its smooth Riemannian description requires the full-rank stratum. A linear CPTP channel $\Lambda$ is Bures nonexpansive by fidelity monotonicity and therefore continuous. [Watrous, *The Theory of Quantum Information*, chapter 3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.double.3.pdf).

**Definition 6.2 (revised) [D].** Let

$$
\mathcal C_N=\operatorname{Open}_B(X_N),
$$

the poset category of Bures-open subsets, with a unique arrow $V\to U$ when $V\subseteq U$. A family $\{U_i\hookrightarrow U\}$ covers if $\bigcup_iU_i=U$. The corresponding covering-sieve topology is $J_B$. In the revised canonical primitive, $J_B$ refers to this open-cover topology, not the former family of CPTP arrows with prescribed local images.

**Theorem 6.1 (open-cover site; revised T-76) [T].** $(\mathcal C_N,J_B)$ is a small Grothendieck site (within a fixed universe) and $\mathcal E_N=\operatorname{Sh}_\infty(X_N)=\operatorname{Sh}_\infty(\mathcal C_N,J_B)$ is an $\infty$-topos.

*Proof.* Identity covers. Pullback of an inclusion is intersection: for $V\subseteq U$, $\bigcup_i(V\cap U_i)=V$. For covers $U_i=\bigcup_jV_{ij}$, one has $U=\bigcup_{i,j}V_{ij}$. These prove identity, base-change stability and transitivity. The opens form a set, hence the site is small. The sheafification theorem identifies sheaves of spaces on this site as a left-exact localization of presheaves of spaces, giving an $\infty$-topos. This is the usual topological-space construction; see Lurie, [*Higher Topos Theory*](https://arxiv.org/abs/math/0608040), §6.2.2 and §7.1. $\square$

A countable basis of balls, with centers in a countable dense set and positive rational radii, presents the same sheaf category with the induced covers. The objects of this basis site are **open balls**, not the dense points viewed as states. Restricting a CPTP process category to countably many density matrices does not establish an equivalent sheaf topos.

**Withdrawn [✗]: the former process-category site proof.** CPTP contractivity does not imply that categorical pullbacks of channels exist, or that inverse images of balls are contained in bounded-radius balls. A constant reset has the whole state space as inverse image of any neighborhood of its output. The old local-image covering proof used both implications without justification. Its asserted equivalence to a dense-point skeleton also lacked a comparison theorem with a dense subsite. The construction above replaces that proof; it does not validate it retroactively.

#### 6.3.2 Channels induce geometric morphisms

For a CPTP map $\Lambda:X_N\to X_M$, inverse image of opens is the functor

$$
\Lambda^{-1}:\operatorname{Open}_B(X_M)\to\operatorname{Open}_B(X_N).
$$

It preserves finite intersections and arbitrary unions, in particular covers. Thus the continuous map induces a geometric morphism

$$
\Lambda:\mathcal E_N\to\mathcal E_M,
\qquad\Lambda^*\dashv\Lambda_*.
$$

Here $\Lambda^*$ is left exact and $\Lambda_*F(U)=F(\Lambda^{-1}U)$. These are functors **between sheaf topoi**, not an automatic internal state morphism of one topos. Additional internalization/realization data are needed for that identification. A noninvertible channel can induce a geometric morphism without becoming an isomorphism or a reversible physical process.

#### 6.3.3 Experiential space and its site

If a specific topological experiential space $Y$ is supplied, its open-cover site $\operatorname{Open}(Y)$ defines $\operatorname{Sh}_\infty(Y)$ by the same theorem [T at the specified space]. A continuous readout $q:X_N\to Y$ induces a geometric morphism using **inverse images** of opens. Continuity alone does not imply that direct images of open covers cover open neighborhoods, since a continuous map need not be open or surjective. The former Theorem 6.2 asserting forward preservation of covers from a Lipschitz bound is withdrawn [✗]. Neither the topology nor the physical/phenomenal validity of $q$ is thereby derived.

Constructing a sheaf topos does not make a separately defined process category $\mathbf{Exp}$ itself a topos. If one instead wants sheaves on that process category, a Grothendieck topology must be specified and verified there; the open-space construction does not silently provide it. Giraud conditions are a characterization of a topos, not extra obligations after a verified small site has already been supplied.

#### 6.3.4 Subobject classifier and realization

In the open-space topos the subobject classifier is the **sheaf**

$$
\Omega_N(U)=\operatorname{Open}(U),\qquad
\Omega_N(U\supseteq V)(W)=W\cap V.
$$

Its global sections are opens of $X_N$; it is not the constant object given by that one lattice. For a subsheaf $A\hookrightarrow F$ and section $s\in F(U)$, $\chi_A(s)$ is the largest open $V\subseteq U$ on which $s|_V$ belongs to $A(V)$. This classifies the subobject. In the $\infty$-topos the same classifier is $0$-truncated and classifies $(-1)$-truncated morphisms.

The former formula using a supremum of radii with $B_B(\Gamma',r)\cap S\ne\varnothing$ does not define this characteristic morphism. For a sufficiently large ball the intersection can occur even outside the subset, and truth values here are opens, not real numbers in $[0,1]$. Taking a square root of such a truth value does not produce a Kraus or Lindblad operator. A numerical filter realization must be explicitly specified, as in [typed mathematical kernel](/docs/reference/mathematical-kernel) and [formalization of φ](/docs/proofs/categorical/formalization-phi#категориальное-определение-φ).

## 7. Faithfulness, alternatives and limits {#7-ограничения-и-альтернативы}

A functor is **faithful** when each map on hom-sets is injective; injectivity of its object map is a different property. A descended process functor can identify distinct channels. If $q$ is bijective, the assignment $\Lambda\mapsto q\Lambda q^{-1}$ is faithful, since equality after conjugation implies equality on all states, which linearly span Hermitian matrices. This is a conditional theorem about a specified encoder. It does not follow from uniqueness of a forward flow, contraction or covariance.

The former unconditional faithfulness claim based on T-42a/T-123 is withdrawn [✗]. See the [corrected representation theorem](/docs/proofs/categorical/uniqueness-theorem#теорема-единственности): reversible CPTP comparison, coverage of the state space, and preservation of the specified octonionic form are explicit bridge assumptions. A constant map into a stationary state can intertwine dynamics without being injective.

The Hilbert–Schmidt adjoint $\Lambda^*$ of a CPTP channel is CP and unital, but is generally not trace-preserving and need not reverse the distinguished endpoint state. Thus it does not define a dagger on this state-preserving category. Work with all CP maps between systems if a dagger structure is needed, and impose trace preservation separately. Tensor products of systems supply monoidal composition; they do not prove a tensor product of phenomenologies.

## 8. Phenomenal completeness {#8-феноменальная-полнота}

A phenomenal bridge can be formulated as specified data $(Y,q,W)$, where $q$ is a model readout and $W$ interprets it as experience. Coverage of a class of experiences, injectivity up to a declared equivalence, and compatibility with interventions are separate hypotheses [H]. They require operational criteria for comparing experiences and validating $q$.

Nonzero $\gamma_{EE}$ proves nonzero numerical weight; it does not prove phenomenality. A formal consciousness predicate is a definition within a model; its empirical and phenomenal validity is an additional claim. Neither a universal phenomenal bridge nor its uniqueness follows from constructing $\operatorname{Sh}_\infty(X_N)$.

## 9. AI encoding and controlled approximation {#9-квази-функтор-для-ии-систем}

Nonlinearity of a neural layer does not violate the axioms of its own category: composition of nonlinear functions is associative. What needs justification is a chosen representation by **linear CPTP** arrows. A state encoder $G:S\to X_N$ is not itself an assignment of neural layers to channels.

A well-typed operational test chooses $\Lambda_f$ for a layer $f$ and evaluates

$$
\epsilon_f=\sup_{s\in K}\|G(f(s))-\Lambda_f(G(s))\|_1.
$$

For composable $f,g$ on suitable domains, contractivity gives

$$
\|G(f(g(s)))-\Lambda_f\Lambda_gG(s)\|_1\leq\epsilon_f+\epsilon_g.
$$

This is a state-prediction bound. Approximate functoriality on **channels**, e.g. a diamond-norm bound between $\Lambda_{fg}$ and $\Lambda_f\Lambda_g$, is stronger and requires probes spanning the operator space (including an ancilla for direct diamond-norm certification). It is not implied by one observed trajectory.

### Corrected Taylor theorem 9.1 [T]

Let $f,g$ be $C^2$ on the relevant neighbourhoods. Put $x=x_0+h$, $\|h\|\leq r$, $A=Dg(x_0)$, $B=Df(g(x_0))$. If the Hessian norms on the relevant segments are bounded by $M_g,M_f$, then, for the composition of the corresponding affine tangent maps,

$$
\|f(g(x))-f(g(x_0))-BAh\|
\leq \tfrac12\|B\|M_g r^2
+\tfrac12M_f(\|A\|r+\tfrac12M_gr^2)^2.
$$

*Proof.* The integral Taylor remainder gives $g(x)=g(x_0)+Ah+r_g$, with $\|r_g\|\leq M_gr^2/2$. Apply the same formula to $f$ with increment $u=Ah+r_g$. The difference is $Br_g+r_f$, bounded by the displayed expression. This proof uses no scalar intermediate-point formula for a vector-valued Hessian and no unjustified $O(r^3)$ remainder from merely $C^2$ regularity. $\square$

**Withdrawn [✗]: automatic CPTP linearization.** The old formula $X\mapsto X+J_fXJ_f^T$ generally has trace $\operatorname{Tr}X+\operatorname{Tr}(J_f^TJ_fX)$ and is not trace-preserving. A fitted channel must separately satisfy positivity of its Choi matrix and the partial-trace condition. Ordinary input-state Jacobians or NTK linearization prove neither condition. The encoding and channel-fitting problem remains [Pr]; see the [measurement protocol](/docs/applied/research/measurement-protocol).

## 10. Singular complexes and emergent time {#10-infty-группоид-и-infty-топос-для-эмерджентного-времени}

**T-91, mathematical part [T].** For a specified topological space $Y$, the singular simplicial set $\operatorname{Sing}(Y)$ is a Kan complex and hence models an $\infty$-groupoid. Its $n$-simplices are continuous maps $\Delta^n\to Y$ with the usual face and degeneracy maps. This is a homotopy model of a space, not a reconstruction of dissipative process arrows. [Lurie, *Higher Topos Theory*, §1.2.5](https://arxiv.org/abs/math/0608040).

### Sheaves and truncations {#104-infty-топос-пучков}

The open-cover site of $Y$ gives $\operatorname{Sh}_\infty(Y)$ [T at supplied $Y$], as in §6.3. Postnikov truncations $\tau_{\leq n}$ exist there. Identifying a phenomenological level with such a truncation requires a specified object and a proved comparison; cognitive depth is not automatically a homotopy degree. A contractible quality space has trivial higher homotopy even if the model contains many numerical qualities or long histories.

Clock registers and Page–Wootters or Feynman–Kitaev constraints are separately supplied dynamical data. A loop in an $\infty$-groupoid is invertible; it does not establish a causal, aperiodic clock or physical information loss.

## 11. Discrete histories {#exp-disc-infty}

A sequence of states with chosen transition channels defines a diagram on the ordered category $0\to1\to\cdots\to m$. Its nerve need not be Kan: the nerve of an ordinary category is Kan iff that category is a groupoid. Channel irreversibility therefore cannot be encoded merely by declaring this nerve an $\infty$-groupoid. Passing to groupoid completion removes the directed-process information.

A cyclic register $\mathbb Z_N$ and an ordered depth register are different constructions. Taking a dense limit of equally spaced readings on a circle yields a circle, not an unbounded time line. The interpretation of a constraint register as the system's physical time requires the additional clock-and-constraint model; see [emergent time](/docs/proofs/dynamics/emergent-time).

## 12. Structured holon processes {#категория-голономов-hol}

Let a **structured model** be $A=(\mathcal H_A,M_A,V_A)$, where $M_A:X_A\to X_A$ is a declared self-model and $V_A\subseteq X_A$ is a declared viable region [D]. An arrow $\Lambda:A\to B$ is CPTP and satisfies

$$
\Lambda(V_A)\subseteq V_B,\qquad\Lambda M_A=M_B\Lambda.
$$

### Closure theorem 12.1 [T] {#122-теорема-о-подкатегории}

Identities satisfy both conditions. If $\Lambda:A\to B$ and $\Psi:B\to C$ satisfy them, then $\Psi\Lambda(V_A)\subseteq V_C$ and $\Psi\Lambda M_A=M_C\Psi\Lambda$. Thus the structured objects and arrows form a category. Its forgetful functor to systems is faithful. Including a distinguished viable state gives a faithful forgetful functor to $\mathbf{DensityMat}$. If several structures occur on the same state, this is not an object-injective inclusion until a structure assignment is fixed.

### Interiority assignment {#123-функтор-интериорности}

If a functor $F$ on the underlying process category has actually been supplied, restricting it gives $\mathcal I=F\circ U$ [T]. Existence of $\mathcal I$ is conditional on this input; it is not a new proof of the phenomenal bridge. Normalised $E$ conditioning does not commute with arbitrary channels, as §4 shows.

## 13. Derived and local cohomology {#производные-категории}

The rank-$r$ locus of $X_N$ is a smooth manifold of real dimension $2Nr-r^2-1$: a rank-$r$ positive matrix is $ZZ^\dagger$ for a full-rank $N\times r$ complex matrix $Z$, modulo the free $U(r)$ action, with one trace constraint. For $N=7$, rank one has dimension $12$ and full rank dimension $48$. The selected point $I_7/7$ is not the whole full-rank stratum.

The full state space is convex and contractible via $H_t(\rho)=(1-t)\rho+tI_N/N$. Ordinary constant-coefficient cohomology in positive degrees therefore vanishes. Local cohomology or cohomology with nonconstant/constructible coefficients may differ, but requires a specified sheaf, support condition and stratification. Nontriviality of such groups does not imply nonzero physical vacuum energy, and their vanishing does not cancel a degree-zero energy density.

Intersection complexes and decomposition theorems require their respective geometric and sheaf-theoretic hypotheses; an arbitrary Bures space or a numerical rank stratification does not automatically meet them. The claimed universal physical IC identification is [Pr], not a consequence of the construction of a derived category.

## 14. What the $\infty$-topos supplies {#infty-топос-как-истинный-примитив}

The specified site supplies an $\infty$-topos with limits, colimits, internal mapping objects, a subobject classifier and truncations. These are mathematical constructions [T]. Choosing it as an ontological primitive is [I/D]. Other sites also supply $\infty$-topoi; their existence is not excluded by a universal property of this construction.

The terminal object $1_{\mathcal E}$ satisfies $\operatorname{Map}(A,1_{\mathcal E})\simeq *$. This says that maps to it form a contractible space; it does not identify a maximally mixed numerical state or supply multiple physically different choices. At a hyperbolic attracting equilibrium on the trace-one tangent space the Jacobian has no zero mode. Neither this terminal-object statement nor a Hessian kernel by itself proves free will.

## 15. Logical structure and numerical realization {#l-унификация}

### 15.1 Types and the former L-unification

In $\mathcal E_N=\operatorname{Sh}_\infty(X_N)$, $\Omega$ is the sheaf of opens described in §6.3.4. A characteristic morphism $\chi_S:G\to\Omega$ is a logical predicate. A matrix state, a Hilbert-space projection and a GKSL operator have other types. An expression $L=\Omega\cap\Gamma$ or $\sqrt{\chi_S}$ does not bridge these types.

**Withdrawn [✗]:** the former universal identification of $L$, internal logic, dissipator and self-model; $\operatorname{Dec}(\Omega)\cong2^7$; and the derivation of numerical operators or rates from this classifier alone. In fact $X_N$ is connected, so its global decidable opens (clopen subsets) are only $\varnothing$ and $X_N$. Internally there can be more local decidable propositions, but no seven-atom basis follows.

### 15.2 A valid finite-frame construction {#l-ops-from-omega}

Choose an orthonormal basis $e_1,\ldots,e_N$ [D]. The Boolean algebra of subsets of that **finite frame** has the representation

$$
S\subseteq\{1,\ldots,N\}\quad\longmapsto\quad P_S=\sum_{i\in S}|e_i\rangle\langle e_i|.
$$

These commuting projections obey $P_SP_T=P_{S\cap T}$ and $P_{S^c}=I-P_S$. This is one classical measurement context; it is not the entire quantum projection lattice or the topological classifier $\Omega$.

More generally, chosen positive effects $E_a$ with $\sum_aE_a=I$ give a POVM and the nonselective Lüders channel

$$
\Lambda(X)=\sum_a\sqrt{E_a}\,X\sqrt{E_a}.
$$

The channel is CPTP by the Kraus condition. Numerical realization of a logical predicate as an effect requires a separately defined map and checks that it preserves the intended structure. The site alone supplies no such map.

For the chosen seven Fano coordinate line projectors, all products reduce to intersections. There are at most fifteen distinct nonempty words as operators: seven line projections, seven point projections and zero; the empty word additionally gives $I$. Hence the former T-115 claim of $7^n$ distinct generic-state compositions is false, including off-diagonal states. A stochastic or grammar-based history can still have many distinct **labels**; those labels are not distinct projector products.

### 15.3 Adjunctions and rates {#сопряжение-adjunction}

The canonical logical self-support reflector is

$$
L_G:\mathcal E_{/G}\rightleftarrows\operatorname{Sub}_{\mathcal E}(G):i_G,\qquad L_G\dashv i_G.
$$

It takes the effective-image support of a map to $G$. The hom-space proof and unit are given in [formalization of φ](/docs/proofs/categorical/formalization-phi#категориальное-определение-φ). Its induced idempotent monad is logical support, not a dissipative state map or a numerical prediction model.

The former $(\mathcal D_\Omega,\mathcal R)$ adjunction has no stated categories or hom-set bijection and is withdrawn [✗]. No regeneration rate $\kappa_0$, bootstrap scale or Hamiltonian follows from it. Rates require specified dynamics, units and couplings. Units/counits of a categorical adjunction cannot be identified with channel probabilities or amplitudes without a declared realization theorem.

## Nonassociativity and process composition {#неассоциативная-категориальная-структура}

Octonion multiplication can be nonassociative. Composition of functions, channels, and endofunctors remains associative. A bicategory permits a coherent associator between composites, with the pentagon identity; it does not license arbitrary failure of associativity. Octonionic structure must enter explicitly as algebraic data on an object or in a specified enriched construction, not by treating ordinary composition as octonion multiplication.

## Local channels and no-signalling {#категориальная-формализация-запрета-сигнализации}

### Local marginal theorem [T] {#запрет-сигнализации-естественная-трансформация}

For a **linear CPTP** local channel,

$$
\operatorname{Tr}_A[(\Lambda_A\otimes\mathrm{id}_B)(\rho_{AB})]=\operatorname{Tr}_A\rho_{AB}.
$$

*Proof.* Write the channel in Kraus form. Partial-trace cyclicity for operators on $A$ gives $\sum_a\operatorname{Tr}_A(\rho_{AB}(K_a^\dagger K_a\otimes I))=\operatorname{Tr}_A\rho_{AB}$. The equality holds for every joint state, including entangled states. $\square$

### Numerical self-models on composites {#тензорная-факторизация-phi}

Frozen-parameter channels $C_{\lambda_A}\otimes C_{\lambda_B}$ are well-defined. A nonlinear state-dependent map $M_A$ is not a linear channel and has no automatic extension $M_A\otimes\mathrm{id}_B$ on entangled inputs. An extension can be prescribed by using local marginals to select channel parameters; the marginal theorem then holds pointwise for that prescription. Other prescriptions need a separate no-signalling proof. Also $\operatorname{Sub}(G\times H)\not\cong\operatorname{Sub}(G)\times\operatorname{Sub}(H)$ in general (a diagonal subset already disproves it in sets). Logical support reflection does not imply tensor factorization of numerical self-models.

## Phenomenal interpretation and Yoneda {#феноменальный-функтор}

Yoneda embeds a **specified** category fully faithfully into its presheaves. It says that objects of that category are determined, up to isomorphism, by their represented hom-functors. It does not construct an empirical category of experience, identify it with density matrices or prove that a proposed bridge $F$ is faithful. The precise metric result for a chosen ray-quality space is [enriched Yoneda](#enriched-yoneda); its phenomenal interpretation remains [I].

## 16. Self-reference with explicit hypotheses {#самореферентное-замыкание}

To define a closure operation on propositions one needs a typed endomorphism $j:\Omega\to\Omega$ and its axioms, e.g. those of a Lawvere–Tierney topology. The numerical map $M:X_N\to X_N$ is not such an endomorphism. A collection of $M$-invariant predicates can be defined after specifying an internal realization of $M$, but is not automatically a subobject of $\Omega$ named $\mathrm{Sub}_{\mathrm{closed}}(\Omega)$: that notation denotes a collection of subobjects unless additional internal representation is given.

Lawvere's fixed-point theorem requires a weakly point-surjective map $e:A\to Y^A$ in a Cartesian closed category. Under that hypothesis each endomorphism of $Y$ has a fixed point: apply the diagonal argument to $h(a)=f(e(a)(a))$. Cartesian closedness alone does not provide $e$. [Lawvere, 1969](https://www.its.caltech.edu/~matilde/LawvereDiagonalArgCartesianClosedCats.pdf). If $Y$ has a fixed-point-free endomorphism, the conclusion is that no such $e$ exists. This does not entail phenomenal externality, a strictly smaller internal theory, physical vacuum energy, or incompleteness of an unspecified proof calculus.

## Scope of categorical closure {#категориальная-полнота}

### Closure of declared constructions {#замкнутость-аксиоматики}

Finite-dimensional states/channels, the open-cover site, its sheaf $\infty$-topos and the slice support reflector form a rigorous mathematical kernel after their inputs are fixed. Further chosen structures include dimension, frame, octonionic form, Hamiltonian/rates, numerical self-model, encoder, clock constraint and phenomenal bridge. Their being expressible in one internal language is not a derivation of their values or existence. The former zero-axiom or all-phenomena closure claim is withdrawn [✗].

### Relation to cohesive-topos programmes {#связь-с-лурье-шульманом}

A Grothendieck topology is not cohesion. Cohesion needs an adjoint quadruple $\Pi\dashv\mathrm{Disc}\dashv\Gamma\dashv\mathrm{coDisc}$ and its further axioms; differential cohesion adds infinitesimal structure. A state space may be modelled as an object of a separately supplied cohesive ambient topos without proving that its open-cover sheaf topos has that structure. See [Schreiber's primary construction](https://arxiv.org/abs/1310.7930). Interpretation of homotopy type theory in an $\infty$-topos likewise does not derive quantum, phenomenal or dynamical bridge data.

### Homotopy truncations and the L hierarchy {#hott-l-иерархия}

The mathematical truncation functors are [T]. The former universal theorem $L_n\cong\tau_{\leq n}\operatorname{Sing}(Y)$ is withdrawn [✗]: the functional criteria defining cognitive levels supply no comparison equivalences with these homotopy types. A proposed comparison must define both sides and prove it for a specified model. See the [interiority hierarchy](/docs/consciousness/hierarchy/interiority-hierarchy) for its own criteria and status.

## Precedents and related programmes {#прецеденты-и-родственные-программы}

### Topos quantum theory {#прецеденты-топосы}

The context-topos programmes use commutative observable algebras as the base, not opens of a density-matrix space. Isham–Butterfield's [primary paper](https://arxiv.org/abs/quant-ph/9803055) relates Kochen–Specker obstruction to absence of global sections; Heunen–Landsman–Spitters' [Bohrification](https://arxiv.org/abs/0709.4364) builds a commutative algebra internally. Their specific theorems do not transfer to $\operatorname{Sh}_\infty(X_N)$ without a comparison theorem. Fano coordinate projections commute and admit the joint distribution $p_i=\gamma_{ii}$; they cannot give Kochen–Specker contextuality by themselves.

### Categorical quantum mechanics {#прецеденты-cqm}

[Abramsky–Coecke](https://arxiv.org/abs/quant-ph/0402130) describe composition of quantum protocols categorically. [Coecke–Pavlović–Vicary](https://arxiv.org/abs/0810.0812) characterize an orthogonal basis by a commutative dagger-Frobenius structure. These give tools for a **chosen** frame and process calculus; they do not derive a universal UHM encoder or a phenomenal bridge. The distinction between systems and states, and between CP and CPTP arrows, must be retained when importing this structure.

### Cohesive physics {#прецеденты-когезия}

[Schreiber](https://arxiv.org/abs/1310.7930) develops differential cohomology under explicit cohesive hypotheses. The proposed pairing of that programme with UHM is [I/C] until those hypotheses and the physical bridge are supplied. No seven-dimensional choice follows from the general sheaf or cohesive construction.

Related: [typed kernel](/docs/reference/mathematical-kernel), [self-model typing](/docs/proofs/categorical/formalization-phi), [representation and tomography](/docs/proofs/categorical/uniqueness-theorem), [measurement protocol](/docs/applied/research/measurement-protocol), [premise ledger](/docs/reference/premises).

## Legacy section links

These anchors preserve existing links. The former assertions are replaced by the typed definitions, conditional results and withdrawals above.

<a id="1451-completeness"></a>
<a id="1451-полнота"></a>
<a id="33-проблема-вырождения-спектра"></a>
<a id="43-адиабатическое-продолжение-для-вырождения"></a>
<a id="infty-топос-голономов"></a>
<a id="t-192-exp2-2-категория"></a>
<a id="связь-с-иерархией-интериорности"></a>
