---
sidebar_position: 2
title: Lindblad Generators and Specified Instruments
description: Exact dephasing, conditional primitivity, instrument classification and covariance
---

# Lindblad generators and specified instruments

The revision of 2026-10-03 retains the explicit atomic/Fano model and its exact algebra, while withdrawing the assertion that a topos classifier uniquely supplies its operators. The state model, observation frame, rates and instrument are input data. A CPTP channel, its recorded instrument and its infinitesimal generator are distinct objects.

## GKSL scope {#деривация-из-классификатора}

A norm-continuous **linear** CPTP semigroup in finite dimension has a generator

$$
\mathcal L_0(X)=-i[H,X]+\sum_a\bigl(L_aXL_a^\dagger-\tfrac12\{L_a^\dagger L_a,X\}\bigr).
$$

This theorem does not cover arbitrary nonlinear feedback. The $L_a$ have units of inverse square-root time; no requirement $\sum_aL_a^\dagger L_a=I$ applies to a general GKSL representation. That identity instead normalizes Kraus operators of a channel. Specifying a channel $T$ and a rate $\gamma$ gives the valid generator $\gamma(T-\mathrm{id})$ by using $L_a=\sqrt\gamma K_a$.

The classifier $\Omega$ classifies subobjects; it has no universally given seven Boolean atoms. Its existence supplies neither Hilbert-space projectors nor rates. “L-unification” of semantic logic, an instrument and a generator is an interpretation [I], rather than an equivalence of categories or a unique physical derivation. See the [typed kernel](/docs/reference/mathematical-kernel#support-reflector).

## Atomic and Fano choices {#фано-операторы}

Fix a frame and a Fano plane. Set $P_i=|i\rangle\langle i|$, $\Pi_\ell=\sum_{i\in\ell}P_i$, $K_\ell=\Pi_\ell/\sqrt3$. Each point lies on three lines, so $\sum_\ell K_\ell^\dagger K_\ell=I$. Each pair lies on one line, giving

$$
T_F(\rho)=\tfrac13\rho+\tfrac23\Delta\rho,\qquad
\mathcal D_F=T_F-\mathrm{id}=\tfrac23(\Delta-\mathrm{id})=\tfrac23\mathcal D_A,
$$

where $\Delta$ is diagonal pinching. Pure atomic dephasing preserves every diagonal population; without a suitable Hamiltonian it does **not** converge to $I/7$. Fano dephasing also ultimately removes all off-diagonal entries when repeated; its one-step attenuation $1/3$ does not imply permanent coherence survival.

For a $(v,k,\lambda)$-BIBD with replication $r$ the same calculation yields

$$
T_c=c\,\mathrm{id}+(1-c)\Delta,\qquad c=\lambda/r=(k-1)/(v-1).
$$

This proves channel equivalence, not instrument equivalence [T]. With unnormalized $L_B=\Pi_B$ at unit rate the decay is $r-\lambda$; with normalized $K_B=\Pi_B/\sqrt r$ it is $1-c$. Comparisons must use the same convention and time scale.

## Conditional primitivity {#примитивность-ℒω}

Assume $0\le c<1$, $\gamma>0$, a fixed Hermitian $H$, and a **connected graph** whose edges are the nonzero off-diagonal $H_{ij}$. Then

$$
\mathcal L_0=-i[H,\cdot]+\gamma(T_c-\mathrm{id})
$$

has unique stationary state $I/7$ and converges to it from every initial state [T at the stated graph assumption]. This applies to both atomic and Fano dephasing.

**Proof.** For every matrix $X$,

$$
\operatorname{Re}\langle X,\mathcal L_0X\rangle_F=-\gamma(1-c)\|X-\Delta X\|_F^2.
$$

A stationary matrix or an eigenmatrix with purely imaginary eigenvalue is therefore diagonal. Its commutator has zero diagonal; hence that eigenvalue is zero and $[H,X]=0$. Connectedness forces all diagonal entries equal. The semigroup is HS contractive, so zero has no nontrivial Jordan block. Every other eigenvalue has strictly negative real part, proving convergence. $\square$

Connectedness is an independent model assumption; AP labels do not prove it. Primitivity allows repeated nonzero eigenvalues: depolarization has eigenvalue $-1$ of multiplicity 48. The nonlinear regenerative extension can have other attractors and does not inherit linear uniqueness.

## Withdrawn necessity claims {#теорема-полнота-покрытия}

The claim that primitivity forces pair coverage is false: singleton pinching plus a connected Hamiltonian satisfies the preceding theorem while $\lambda_{ij}=0$ for every distinct pair. The old necessity $c>0$ is likewise withdrawn [✗]: coherent nonunital feedback can counteract atomic dephasing. An argument using exponential decay from the *bare* dissipator cannot ignore Hamiltonian sources or the feedback anchor.

Among nontrivial BIBD$(7,k,1)$ the only sizes are two and three; the Fano size three preserves more coherence and uses fewer Kraus operators. This is a restricted optimum with $\lambda=1$ assumed. Complementary $(7,4,2)$ and $(7,6,5)$ designs give $c=1/2$ and $5/6$ with seven sharp Kraus operators. Duplicating operators with coefficient $1/\sqrt2$ changes no channel or generator. Neither primitivity nor the nonzero spectrum forces $\lambda=1$.

## Exact instrument theorem {#теорема-bibd-из-хои}

The Choi rank of $T_c$ for $0\le c<1$ is seven: its nonzero restriction is $(1-c)I+cJ$, with eigenvalues $1+6c,1-c,\ldots,1-c$. The following classification applies to a **given** $T_{1/3}$ and declared sharp/minimal/covariant instrument. It does not derive these inputs from $\Omega$.

<a id="t13-sharp"></a>

:::tip T13, strengthened (2026-09-26): the sharp minimal instrument of the Fano channel [T]
Let $\Phi_c(\Gamma) = c\,\Gamma + (1-c)\,\mathrm{diag}\,\Gamma$ on $\mathbb C^7$, $0 \le c < 1$; then $\Phi_{1/3} = \mathcal P_{\text{Fano}} = \mathrm{id} + \mathcal D_\Omega$ and $\mathcal P_\alpha = \Phi_{(1-\alpha)/3}$. Call a Kraus representation **sharp** if each Kraus operator is a positive multiple of an orthogonal projector (the Lüders coarsening of T12) and **minimal** if it has as many operators as the Choi rank, $7$ (T11).

**(a)** Every Kraus operator of $\Phi_c$ is diagonal, so a sharp one is $\sqrt{x_S}\,\Pi_S$ for a set $S$ of axes.

**(b)** The sharp minimal representations of $\Phi_{1/3}$ are exactly $\{\Pi_p/\sqrt3\}_{p \in \mathcal P}$, $\mathcal P$ one of the $30$ Fano planes on the seven axes. Ranks and weights are not assumed: they come out as $3$ and $1/3$.

**(c)** For $0 < c < 1$ a sharp minimal representation exists only at $c \in \{1/3, 1/2, 5/6\}$, by the symmetric designs $(7,3,1)$, $(7,4,2)$, $(7,6,5)$; at $c = 0$ it is the seven axis projectors. In the family $\mathcal P_\alpha$ only $\alpha = 0$ (Fano) and $\alpha = 1$ (atomic) have one.

**(d)** Exactly one of the $30$ planes is invariant under the collineation image of $\Gamma_{\!\text{oct}}$: the octonionic lines. Hence the instrument of $\mathcal D_\Omega$ that is sharp, minimal and $\Gamma_{\!\text{oct}}$-covariant is unique — the line instrument $\{L_p^{\text{Fano}}\}$.

**(e)** No clause can be dropped. Without minimality: $\sqrt{1/3}\,I$ with $\sqrt{2/3}\,|i\rangle\langle i|$ (eight sharp operators — the axis resolution of [T-331(f)(d)](/docs/core/dynamics/gap-thermodynamics#t-331f)), and mixtures over planes. Without sharpness: the unitary mixtures of the line operators, e.g. $\sqrt{3/7}\,I$ and $\sqrt{2/21}\,\mathrm{diag}(\omega^{ai})$, $a = 1, \dots, 6$, $\omega = e^{2\pi i/7}$, whose outcome probabilities $3/7$ and $2/21$ do not depend on $\Gamma$. Without $\Gamma_{\!\text{oct}}$: the other $29$ planes.

**(f)** The syndrome measurements of the Hamming code do not give $\Phi_{1/3}$: a single parity check is the sharp pair $\{\Pi_p, I - \Pi_p\}$, a check chosen uniformly gives $\Phi_{3/7}$, which by (c) has no sharp minimal representation, and the full syndrome, which tells every axis apart, gives $\Phi_0$.
:::

**Proof.** (a) The Choi matrix $\sum_{ij}C_{ij}|ii\rangle\langle jj|$, $C = (1-c)I + cJ$, lives on $\mathrm{span}\{|ii\rangle\}$, and the Kraus operators are the vectors of its range read as matrices; a diagonal projector is a coordinate projector. (b) With the $7\times7$ incidence matrix $N$ ($N_{iS} = 1$ iff $i \in S$) and $X = \mathrm{diag}(x_S)$ the representation reads $NXN^{\mathsf T} = C$. Minimality makes the seven operators linearly independent, so $N$ is invertible and $X^{-1} = N^{\mathsf T}C^{-1}N$ with $C^{-1} = (I - tJ)/(1-c)$, $t = c/(1+6c)$. Off the diagonal this reads $|S \cap T| = t\,k_Sk_T$, $k_S = |S|$; on it, $x_S = (1-c)/(k_S(1 - tk_S))$. At $c = 1/3$, $t = 1/9$: $9$ divides $k_Sk_T$ for all $S \ne T$, and as $k \le 7$ every $k_S \in \{3, 6\}$, so $x_S = 1/3$; the trace $\sum_S x_Sk_S = \mathrm{Tr}\,C = 7$ gives $\sum_S k_S = 21$, so all $k_S = 3$. Then any two blocks meet in one point, and $C_{ij} = 1/3$ puts every pair of axes on exactly one block: a $(7,3,1)$ design, the Fano plane (T13 above), with $7!/168 = 30$ labellings. Conversely every Fano plane gives $\Phi_{1/3}$ (T-78). (c) $t\,k_Sk_T$ is a positive integer, so $t$ is rational and at most $7/(k_Sk_T)$; a finite search over the block sizes, the admissible $t$ and the set systems with these intersections finds exactly the three designs. (d) A plane invariant under the $168$ collineations $G_0$ of the octonionic plane is a union of $G_0$-orbits of triples. $G_0$ has two orbits on the $35$ triples, the $7$ lines and the $28$ triangles (it acts regularly on the $168$ ordered non-collinear triples, the bases of $\mathbb F_2^3$), so the plane is the set of lines. The collineation image of $\Gamma_{\!\text{oct}}$ is $G_0$ ([Theorem 5.1b](/docs/proofs/gap/fano-channel#g2-ковариантность)). (e) For $i \ne j$, $\tfrac37 + \tfrac2{21}\sum_{a=1}^6\omega^{a(i-j)} = \tfrac37 - \tfrac2{21} = \tfrac13$, and $\tfrac37 + \tfrac{12}{21} = 1$ for $i = j$. (f) Label the axes and the checks by the nonzero vectors of $\mathbb F_2^3$; the check $h$ reads $h\cdot i$, $\{i : h\cdot i = 0\}$ is a line, and two distinct axes agree on the $3$ checks with $h\cdot(i+j) = 0$. $\blacksquare$

Check: `test_sharp_minimal_kraus_representations_are_the_fano_planes`. The generator $\mathcal D_\Omega$ as a map fixes only $\Phi_{1/3}$, which does not know the lines; the physical instrument that resolves them — the one the associator weight needs — is fixed by sharpness, minimality and the frame group. What this does and does not give for $\kappa$: [T-331(g)](/docs/core/dynamics/gap-thermodynamics#t-331g).

## Three terms are a model decomposition {#триадная-декомпозиция}

The displayed grouping into Hamiltonian, dissipation and regeneration is a chosen decomposition [D]. There is no categorical exhaustion into automorphism/left-adjoint/right-adjoint actions. A fixed replacement term $a(\rho_a-\rho)$ itself has GKSL form, so it does not furnish a third irreducible class. Several baths or controls can be grouped differently. The old uniqueness/completeness theorem and its deduction of three Bayesian hypotheses are withdrawn [✗]. A calibrated three-hypothesis observation model can still be chosen, but its posterior is additional data.

## Composition: a finite intersection semilattice {#композиционные-фано-морфизмы}

For the unnormalized outcome maps $m_\ell(X)=\Pi_\ell X\Pi_\ell$,

$$
m_{\ell_n}\circ\cdots\circ m_{\ell_1}(X)=P_{\cap_j\ell_j}XP_{\cap_j\ell_j}.
$$

All coordinate projectors commute and are idempotent. Intersections of Fano lines are a line, a point or the empty set; the empty word gives all seven points. Thus there are at most **16** maps including the identity (at most 15 for nonempty words), independent of word length and of $\rho$. For normalized nonzero outcomes there are at most 14 supports. Multiplying actual Kraus operators adds a common scalar at fixed length, not exponential distinguishability. The former T-115 assertion $7^n$ and its “generic” proof are withdrawn [✗]: permuted words already collide for **every** state.

### A separate word process {#теорема-фано-грамматика}

For a chosen $\lambda\ge0$, the Markov matrix

$$
M_{ij}=\frac{1+\lambda|\ell_i\cap\ell_j|}{7+9\lambda}
$$

is strictly positive, symmetric and stochastic. It therefore has a unique uniform stationary law and converges to it [T]. Its syntactic word language contains $7^n$ words, but the recorded words must not be identified with distinct projected states. This repairs T-114's diagonal normalization and separates language from channel composition.

## Covariance and conserved quantities {#g2-ковариантность}

For positive line rates, the bare diagonal-projector dissipator acts on entries by $X_{ij}\mapsto-r_{ij}X_{ij}$, with $r_{ij}>0$ for $i\ne j$. Its kernel is the diagonal algebra. A unitary symmetry must preserve that algebra and hence is monomial; conversely a monomial unitary is a symmetry iff its permutation preserves $r$. The group is $U(1)^7\rtimes\operatorname{Aut}(r)$, and for equal rates it is $U(1)^7\rtimes S_7$ [T]. Its intersection with a specified real octonionic $G_2$ is the finite frame group of order 1344. It is not full $G_2$ covariance.

### Torus and rates {#теорема-происхождение-тора}

The diagonal algebra exponentiates to a compact torus. The chosen projectors have integral spectrum and satisfy $e^{2\pi iP_i}=I$; this supplies these particular periods. Compactness of the full group is not equivalent to integrality of every possible generator: an irrational combination can have a dense one-parameter orbit inside the same compact torus. Bare-dissipator populations cease to be seven conserved charges when a connected Hamiltonian is added; only scalar diagonal charges commute with that Hamiltonian. A matter-ledger interpretation remains [I].

A fully $G_2$-covariant dissipator can separately be constructed from a specified octonionic three-form, $(A_a)_{bc}=\varphi_{abc}/\sqrt6$, for which $\sum_aA_a^\dagger A_a=I$. This is an alternative model, not a derivation selecting the pinching channel. The classification of a codomain symmetry does not imply a unique encoder of experimental data; see [reconstruction](/docs/applied/research/reconstruction-identifiability).

Primary source for the linear semigroup theorem: Yui Kuramochi, [GKSL derivation from Kraus representations](https://arxiv.org/abs/2406.03775). Exact finite channel and instrument checks remain in `check_core_numbers.py`; counterexamples to the withdrawn implications are in `check_mathematical_kernel.py`.

## Historical addresses

Former claims at these addresses have the corrected scope above; the unconditional bridge is withdrawn.

<a id="s7-эквивариантность"></a>
<a id="атомы-классификатора"></a>
<a id="единственность-фано"></a>
<a id="замыкание-моста"></a>
<a id="интуиция-атомы"></a>
<a id="интуиция-ветер"></a>
<a id="полнота-триадной-декомпозиции"></a>
<a id="разграничение-форм-lk"></a>
<a id="редукция-моста"></a>
<a id="следствие-k3"></a>
<a id="теорема-bibd-эквивалентность"></a>
<a id="теорема-maxmin"></a>
<a id="теорема-граница-хемминга"></a>
<a id="теорема-демократичность"></a>
<a id="теорема-единственность-фано"></a>
<a id="теорема-необходимость-c"></a>
<a id="теорема-оптимальность-фано"></a>
<a id="теорема-оптимальный-k"></a>
<a id="теорема-проективная-декомпозиция"></a>
<a id="теорема-равномерная-контракция"></a>
<a id="теорема-различимость-композиций"></a>
<a id="теорема-ранг-хои"></a>
<a id="теорема-хемминг-фано"></a>
<a id="фано-канал"></a>
