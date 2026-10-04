---
sidebar_position: 3
title: "Embeddings of Alternative ToEs"
slug: /proofs/physics/toe-embeddings
description: "M-theory, loop quantum gravity and causal sets relative to UHM: the G2 coincidence, encodings of spin networks and posets in holonic states, and the universal property of the UHM kinematic object."
---

# Embeddings of Alternative Candidate Theories into UHM

:::info Status
This document relates competing approaches to quantum gravity to UHM. After the audit of 2026-09-26 it proves [T]: a shared symmetry group with M-theory on $G_2$-manifolds (T-170 (i)), injective encodings of finite spin networks and finite causal sets in holonic states (T-171, T-172) and a universal property of the UHM kinematic object (T-174). It does not prove that these theories are recovered as limits of UHM: the correspondence of partition functions with M-theory is a hypothesis [H], and the former receiving map from every theory into UHM is retracted [✗].
:::

---

## 1. M-Theory on $G_2$-Manifolds {#m-теория}

### 1.1 Mathematical Context

M-theory compactified on a 7-dimensional manifold $M_7$ with holonomy $\mathrm{Hol}(M_7) = G_2$ gives $N=1$ supersymmetry in 4D (Acharya, 1998; Atiyah–Witten, 2001; Joyce, 2000). Key results:

- **Acharya (1998, hep-th/9812011):** M-theory on a compact $G_2$-manifold → $N=1$ 4D, gauge groups from singularities.
- **Atiyah–Witten (2001, hep-th/0107177):** M-theory on $G_2$-manifolds with conical singularities → chiral fermions.
- **Halverson–Morrison (2015, 1507.05965):** Systematic extraction of gauge groups from $G_2$-compactifications. $SU(3) \times SU(2) \times U(1)$ from $A$-$D$-$E$ singularities on co-compact submanifolds.
- **Acharya–Witten (2001, hep-th/0109152):** $G_2$-compactification as «M-theory on $G_2$» — a systematic review.

### 1.2 UHM ↔ M-Theory Correspondence {#uhm-m-theory}

#### T-170: The M-theory correspondence — the group coincidence and the finite partition function [T], the correspondence of partition functions [H] {#t-170}

:::warning Corrected 2026-09-26 — audit of T-170
T-170 stood as "[T] at levels of M-theory definedness", resting on T-170' (perturbative identity of partition functions) and T-170'' (non-perturbative correctness of the UHM integral). The audit found four errors:
1. **Lemma T-170'.1 is false [✗].** A continuous action of the connected group $G_2$ on the torus $(S^1)^{21}$ by group automorphisms is trivial, since $\mathrm{Aut}((S^1)^{21}) = GL(21, \mathbb{Z})$ is discrete; the linear representation $\mathbf{14} \oplus \mathbf{7}$ preserves no lattice (otherwise its image, a compact connected group, would lie in $GL(21,\mathbb{Z})$ and be trivial). Even on the vector space $\mathbb{R}^{21} = \mathbf{14} \oplus \mathbf{7}$ the quotient is not an orbifold: the stabiliser of $(0, v)$ is $SU(3)$ (orbit of dimension 6, not 14) and that of $0$ is $G_2$. Nor do the Gap phases $\theta_{ij} = \arg \Gamma_{ij}$ transform among themselves: two states with the same 21 phases and different moduli receive different phases from one $g \in G_2$ (numerically up to 2.65 rad).
2. **T-170' is not a well-posed statement [✗].** $Z_{\text{M}}^{\text{pert}}$ is not a defined formal power series: eleven-dimensional supergravity is perturbatively non-renormalisable, with an ultraviolet divergence at two loops (Bern, Dixon, Dunbar, Perelstein, Rozowsky 1998; Deser, Seminara 1999). Step 5 ("each Feynman diagram is identical") names no map from the diagrams of a $21M$-variable integral to those of 11D supergravity, and the compact $G_2$-manifold "with $b_3 = 21$ (e.g. Joyce's resolution of $T^7/\Gamma$)" is not the cited example — Joyce's first example (1996) has $b_2 = 12$, $b_3 = 43$.
3. **The vacuum state of T-170'' Step 4 is not a state [✗]:** $\omega_{\text{vac}} = \lim_M \mathrm{Tr}_M(\rho^*_M\,\cdot)/M$ gives $\omega(1) = 1/M \to 0$.
4. **The functor $\mathcal{F}_M$ of §1.3 is ill-typed [✗]:** the Gelfand spectrum is defined for commutative $C^*$-algebras; $A_{\text{int}}^{\otimes M}$ is not commutative, and the spectrum of its centre $\mathbb{C}^{3^M}$ is $3^M$ points — zero-dimensional, not a 7-manifold; the morphism part ("CPTP channel $\mapsto$ $G_2$-diffeomorphism") is not defined.

*Routes tried to keep the correspondence at [T].* (i) As formal power series — blocked by item 2: the right-hand side does not exist. (ii) As an identification of classical moduli, 21 Gap phases $\leftrightarrow$ $H^3(\mathcal{M}_7)$ — blocked by item 1: the phases carry no $G_2$-action to be matched, and no compact $G_2$-manifold with $b_3 = 21$ is named. (iii) At the level of the symmetry group — succeeds: part (i) of the theorem below. So the correspondence of partition functions is a hypothesis [H]; what is proved is (i)–(iii).
:::

:::tip Theorem T-170 (restated 2026-09-26) [T] for (i)–(iii); (iv) is a hypothesis [H]
**(i) Group coincidence [T].** Let $\varphi_0(x, y, z) = \langle x, yz \rangle$ be the associative 3-form on $\mathrm{Im}\,\mathbb{O} = \mathbb{R}^7$ of the Fano multiplication. Its stabiliser in $GL(7, \mathbb{R})$ is $G_2 = \mathrm{Aut}(\mathbb{O})$; at the level of Lie algebras, $\{X \in \mathfrak{gl}(7, \mathbb{R}) : X \cdot \varphi_0 = 0\} = \mathrm{Der}(\mathbb{O})$, of dimension 14. This is the group whose holonomy defines a torsion-free $G_2$-structure on a 7-manifold, and $G_2 \subset \mathrm{Spin}(7)$ is the stabiliser of one unit spinor of the 8-dimensional spin representation — the single parallel spinor behind $N = 1$ in 4D.

**(ii) Finite-$M$ partition function [T].** For $M \in \mathbb{N}$ and $S_{\text{Gap}}$ continuous on the torus $(S^1)^{21M}$, the integral $Z^{(M)}_{\text{UHM}} = \int_{(S^1)^{21M}} e^{-S_{\text{Gap}}[\theta]}\, d\theta$ (normalised Haar measure) is finite and strictly positive.

**(iii) Thermodynamic-limit states [T].** Let $\mathfrak{A} = \bigotimes_{v \in \mathbb{N}} M_7(\mathbb{C})$ be the quasi-local (UHF) $C^*$-algebra, and $\omega_M$ the state that is $\mathrm{Tr}(\rho_M\,\cdot)$ on the first $M$ factors and a fixed product state on the rest. The sequence $(\omega_M)$ has a weak-$*$ convergent subsequence, and every limit is a state on $\mathfrak{A}$. Uniqueness of the limit is not claimed.

**(iv) Correspondence [H].** The equality $Z_{\text{UHM}} = Z_{\text{M}}$ under the identification (a)–(d) of the former statement below is a hypothesis, not a theorem at any level of rigor.
:::

:::note Former statement of T-170 (now the hypothesis (iv))
Under the following conditions:

**(C27-M)** (Continuous Gap limit): the limit $a \to 0$ of the lattice of Gap fields $\theta_{ij}(x)$ exists, in which the $\sigma$-model on $(S^1)^{21}/G_2$ defines a smooth 7-dimensional target space $\mathcal{M}_7$; *(labelled **C27-M** to disambiguate from the consciousness-window C27 "attractor in window"; the "-M" marks the M-theory/ToE block C27-M–C30)*

**(C28-M)** (Supersymmetric extension): the SUSY extension of the Gap integral ([SUSY from $G_2$](/docs/physics/particle-physics/susy)) is a well-defined quantum supersymmetric functional integral;

the UHM Gap functional integral $Z_{\text{UHM}} = \int_{(S^1)^{21}} \mathcal{D}[\theta]\, \mathcal{D}[\tilde{\theta}]\, e^{-S_{\text{Gap}}[\theta, \tilde{\theta}]}$ recovers the M-theoretic partition function $Z_{\text{M}} = \int_{\mathcal{M}_7} \mathcal{D}[C_3]\, \mathcal{D}[g]\, e^{-S_{11D}[g, C_3]}$ via the identification: **(a)** $(S^1)^{21}/G_2$ ↔ the moduli of the $G_2$-metric on $\mathcal{M}_7$; **(b)** 21 phases $\theta_{ij}$ ↔ deformations of the associative 3-form, bijective for $b_3 = 21$; **(c)** $G_2 = \mathrm{Aut}(\mathbb{O})$ ↔ $\mathrm{Hol}(\mathcal{M}_7) = G_2$; **(d)** Gap superpartners $\tilde{\theta}_{ij}$ ↔ fermionic moduli (parallel spinor $\eta_0 = 1_{\mathbb{O}}$).

Of (a)–(d), only (c) is a statement that can be proved, and it is part (i) of the restated theorem; (a) is item 1 of the audit; (b) and (d) are identifications without a map.
:::

**Proof of (i).** A linear map preserving $\varphi_0$ preserves the metric, because the metric is determined by $\varphi_0$ through $6\,\langle x, y\rangle\,\mathrm{vol} = (x \lrcorner \varphi_0) \wedge (y \lrcorner \varphi_0) \wedge \varphi_0$ (Bryant 1987, "Metrics with exceptional holonomy", §2), and therefore it preserves the cross product $\langle x \times y, z\rangle = \varphi_0(x, y, z)$ and the octonion product $xy = -\langle x, y\rangle + x \times y$ on $\mathrm{Im}\,\mathbb{O}$; conversely an automorphism of $\mathbb{O}$ preserves $\varphi_0$. So $\mathrm{Stab}_{GL(7)}(\varphi_0) = \mathrm{Aut}(\mathbb{O}) = G_2$. That $G_2$ is the holonomy group of a torsion-free $G_2$-structure and fixes exactly one spinor of $\mathrm{Spin}(7)$ is standard (Bryant 1987; Harvey, *Spinors and Calibrations*, 1990; Joyce 2000). $\square$

### Former Theorem T-170' (perturbative correspondence) [✗ as a theorem; part of the hypothesis (iv)] {#т-170-prime}

**Former statement.** $Z_{\text{UHM}}^{\text{pert}}[\lambda; \hbar] = Z_{\text{M-theory}}^{\text{pert}}[G_4; \hbar]$ as formal power series under the identification (a)–(d).

**Verdict by step.** Step 1 (four-dimensional base from T-120 [T], internal space parametrised by $\mathcal{D}(\mathbb{C}^7)$) is a description, not a correspondence; the $KO$-dimension-7 sentence was already retracted [✗] (no real structure of $KO$-dimension 6 exists on $\mathbb{C}^7$, [spacetime, Step 6](/docs/core/foundations/spacetime#теорема-спектральная-тройка)). Step 2 rests on Lemma T-170'.1, which is false (audit item 1). Step 3 cites the Connes–Chamseddine expansion of $\mathrm{Tr}\,f(D/\Lambda)$ (T-65) but computes no coefficient of the reduced 11D action to compare with. Step 4 ($V_3 \neq 0 \Leftrightarrow \langle G_4\rangle \neq 0$) names no map between the associator of the Fano multiplication and a 4-form flux. Step 5 asserts identity of Feynman diagrams of an object that does not exist (audit item 2). None of the steps can be repaired into a proof of the equality, because its right-hand side is undefined.

### Theorem T-170'' (restated 2026-09-26: finiteness at finite $M$, limit states) [T] {#т-170-double-prime}

The statement is parts (ii) and (iii) of T-170. The former domain $(S^1)^{21M}/G_2^M$ is replaced by the torus $(S^1)^{21M}$ (there is no $G_2$-action to divide by, audit item 1), and the former vacuum formula by weak-$*$ limit points (audit item 3).

**Proof of (ii).** The torus $(S^1)^{21M}$ is compact and $S_{\text{Gap}}$ is continuous on it (a trigonometric polynomial in the phases), so $\lvert S_{\text{Gap}} \rvert \leq C$ for some $C < \infty$. The integrand lies in $[e^{-C}, e^{C}]$ and the normalised Haar measure has total mass 1, so $e^{-C} \leq Z^{(M)}_{\text{UHM}} \leq e^{C}$. $\square$

**Proof of (iii).** The state space of the unital $C^*$-algebra $\mathfrak{A}$ is weak-$*$ compact (Banach–Alaoglu) and, $\mathfrak{A}$ being separable, metrisable; hence $(\omega_M)$ has a convergent subsequence. Positivity and $\omega(1) = 1$ pass to weak-$*$ limits, so every limit is a state (Bratteli–Robinson, *Operator Algebras and Quantum Statistical Mechanics*, Vol. 1). $\square$

**Results used:** Bryant 1987 and Harvey 1990 (the stabiliser of $\varphi_0$); Joyce 2000 ($G_2$-holonomy); Banach–Alaoglu; Bratteli–Robinson 1979. Not used any more: T-53, T-65, T-120, Kaluza–Klein reduction, Acharya–Witten, Harvey–Lawson — they entered only the retracted steps of T-170'.

Numerical check: `check_core_numbers.py`, `test_t170_gap_phases_carry_no_g2_action_and_the_torus_quotient_is_not_an_orbifold` — the stabiliser of $\varphi_0$ in $\mathfrak{gl}(7)$ has dimension 14 and is annihilated exactly by the 14 derivations of $\mathbb{O}$; on $\mathbf{14} \oplus \mathbf{7}$ the $G_2$-orbits of a generic point, of $(0, v)$ and of $0$ have dimensions 14, 6 and 0; two states with equal phases and different moduli get phases differing by more than 0.5 rad under one $g \in G_2$.

*Status history:* [C at C27, C28] originally; [T] "at levels of M-theory definedness" until 2026-09-26; restated 2026-09-26: (i)–(iii) [T], the correspondence (iv) [H], Lemma T-170'.1 and T-170' as a theorem [✗].

### 1.3 Formal Functor {#функтор-m-theory}

**Former definition [✗].** $\mathcal{F}_M: \mathbf{Hol}_{\text{comp}} \to \mathbf{G_2\text{-}Mfld}$, sending $M$ holons to "the Gelfand spectrum of $A_{\text{int}}^{\otimes M}/G_2$" and a CPTP channel to a $G_2$-diffeomorphism. It is ill-typed (audit item 4): the Gelfand spectrum of the centre of $A_{\text{int}}^{\otimes M}$ is a finite set of $3^M$ points, and no rule assigns a diffeomorphism to a channel.

**What survives.** No functor is claimed. The correspondence that is proved is the coincidence of symmetry groups, T-170 (i): the group that acts on the holon, $\mathrm{Aut}(\mathbb{O})$, is the group that fixes the associative 3-form, $\mathrm{Stab}_{GL(7)}(\varphi_0)$, which is the holonomy group of a torsion-free $G_2$-structure.

### 1.4 Embedding Assessment

| Aspect | Status | Comment |
|--------|--------|---------|
| $G_2$-symmetry coincides | **[T]** | T-170 (i): $\mathrm{Stab}_{GL(7)}(\varphi_0) = \mathrm{Aut}(\mathbb{O})$, Lie algebra of dimension 14 |
| $N=1$ SUSY | **[T]** at the group level | $G_2 \subset \mathrm{Spin}(7)$ fixes exactly one spinor; the physical identification $\eta_0 = 1_{\mathbb{O}}$ is part of (iv) [H] |
| $SU(3) = \mathrm{Stab}_{G_2}(e_O)$ | **[T]** | T-42e; "the same mechanism as the singularity gauge groups of Acharya and Halverson–Morrison" is not proved [H] |
| Moduli space $(S^1)^{21}/G_2$ as a 7D orbifold | **[✗]** | No $G_2$-action on the torus; $\mathbb{R}^{21}/G_2$ is not an orbifold (audit item 1) |
| Perturbative correspondence $Z_{\text{UHM}} = Z_M$ | **[✗]** as a theorem | $Z_M^{\text{pert}}$ is not defined; the equality is part of (iv) [H] |
| Finiteness of $Z_{\text{UHM}}^{(M)}$ | **[T]** | T-170'' (ii), on the torus $(S^1)^{21M}$ |
| Thermodynamic-limit states | **[T]** existence | T-170'' (iii); uniqueness open |
| Non-perturbative definition of $Z_M$ (M-theory) | open | External open problem of M-theory |

---

## 2. Loop Quantum Gravity {#пкг}

### 2.1 Mathematical Context

Loop quantum gravity (LQG) is based on:
- **Spin networks** (Penrose, 1971; Rovelli–Smolin, 1995): graphs with edges labeled by $SU(2)$ representations and vertices labeled by intertwiners.
- **Spin foams** (Baez, 1998; Perez, 2013): 2-complexes as the «evolution» of spin networks, defining transition amplitudes.
- **Key algebra:** $SU(2)$ — gauge group in the Ashtekar formalism.

Connection $SU(2) \subset G_2$: the chain of embeddings

$$
SU(2) \subset SU(3) \subset G_2
$$

where $SU(3) = \mathrm{Stab}_{G_2}(e_O)$ (T-42e [T]) and $SU(2) \subset SU(3)$ is the standard embedding.

### 2.2 Embedding Construction {#lqg-embedding}

#### T-171: Spin networks are encoded in holonic states [T] {#t-171}

:::warning Corrected 2026-09-26 — audit of T-171, Lemma C29' and T-171'
T-171 stood as an "LQG embedding functor $\mathbf{SpinNet}^{\text{bd}}_{SU(2)} \to \mathbf{Hol}_{\text{comp}}$" for spins $j_e \leq 3$ (via Lemma C29'), extended to all spins by the cluster construction T-171'. The audit found:
1. **The state of Lemma C29' is not a density matrix [✗].** $W_e^{\text{spin}} = \lvert\gamma\rvert \sum_{i,j} U_{ij}\, \lvert i\rangle\langle j\rvert_v \otimes \lvert j\rangle\langle i\rvert_w$ with $U$ unitary is not Hermitian in general and has trace $\lvert\gamma\rvert \sum_i U_{ii} \neq 1$, so Step 6 ("convex combination of positive operators with weights summing to 1") is false; numerically, for a random unitary $U$ the Hermiticity defect is $2.9$ and the trace is $-1.51 - 0.78i$.
2. **The spin is not recovered [✗].** Step 7 gives a coherence $\eta\,\lvert\gamma\rvert_{\text{target}}$, so $j = \tfrac12\lfloor 7\lvert\gamma\rvert^2\rfloor$ returns $\tfrac12\lfloor 2 j \eta^2\rfloor$; with $\eta \leq 1/(\lvert E\rvert V_{\max})$ forced by Step 5, every $j \leq 3$ decodes as $0$ once $\eta \leq 1/4$. "Appropriate scaling of $\eta$" is not available.
3. **No functor of the stated kind [✗].** "Unitary embedding $U_\phi$ preserving $\Gamma_{\text{total}}$" does not exist: a state of full rank $7^{M_2}$ is not the image $V\Gamma V^\dagger$ of a state on a space of dimension $7^{M_1} < 7^{M_2}$.
4. **Part (c) derives nothing.** The LQG area formula $8\pi l_P^2 \gamma \sum_e \sqrt{j_e(j_e+1)}$ is a function of the labels; finite-dimensionality of $\mathcal{D}(\mathbb{C}^7)$ does not produce it. Withdrawn as a claim.
5. **The cluster construction of T-171' is false [✗].** The sub-spins $j_e/k_e$ need not be half-integers ($j_e = 7/2$, $k_e = \lceil 7/6\rceil = 2$: $7/4$); for $k_e = 1$ Step 4 divides by $k_e - 1 = 0$; and spins do not add along a chain — the Clebsch–Gordan series gives the range $\lvert j_1 - j_2\rvert, \dots, j_1 + j_2$, not the sum.
6. **The bound $j_e \leq 3$ was an artefact** of reading the spin from $\lvert\gamma\rvert^2 \leq 6/7$. Read from a *ratio* of two coherences, the spin is unbounded and independent of the weights.

*Route taken.* The encoding is rebuilt so that every summand is a state and every label is a ratio of two matrix elements that no other summand touches. This proves more than before — all finite spin networks with $M = \lvert V\rvert$ holons, no bound on $j$, no clusters — so the status stays [T] with a stronger statement, and T-171' becomes a corollary.
:::

:::tip Theorem T-171 (restated 2026-09-26) [T]
Let $\mathcal{S} = (G, j, k)$ be a finite spin network: a finite directed graph $G = (V, E)$ without loops and with at most one edge between two vertices, spins $j_e \in \tfrac12\mathbb{Z}_{\geq 0}$ (unbounded), and at each vertex $v$ a label $k_v \in \mathbb{Z}_{\geq 0}$ — the index of an intertwiner in a fixed orthonormal basis of $\mathrm{Inv}\big(\bigotimes_{e \ni v} V_{j_e}\big)$. Put $M = \lvert V\rvert$, choose weights $\eta, \kappa > 0$ with $\eta\lvert E\rvert + \kappa M \leq 1$, and

$$
\Gamma_{\mathcal{S}} := (1 - \eta\lvert E\rvert - \kappa M)\,\frac{\mathbb{1}}{7^M} + \eta \sum_{e = (v,w) \in E} \psi_{j_e}^{(v,w)} \otimes \frac{\mathbb{1}}{7^{M-2}} + \kappa \sum_{v \in V} \chi_{k_v}^{(v)} \otimes \frac{\mathbb{1}}{7^{M-1}},
$$

where $\psi_j = \lvert\psi_j\rangle\langle\psi_j\rvert$ acts on the ordered pair (source, target), $\lvert\psi_j\rangle \propto \lvert 01\rangle + \lvert 12\rangle + (2j+1)\lvert 23\rangle$, and $\chi_k = \lvert\chi_k\rangle\langle\chi_k\rvert$, $\lvert\chi_k\rangle \propto \lvert 3\rangle + \lvert 4\rangle + (k+1)\lvert 5\rangle$ (unit vectors). Then:

**(a) State.** $\Gamma_{\mathcal{S}} \in \mathcal{D}\big((\mathbb{C}^7)^{\otimes M}\big)$; it has full rank when $\eta\lvert E\rvert + \kappa M < 1$.

**(b) Local decoding.** For an ordered pair $v \neq w$ with two-body marginal $\rho_{vw}$, and a vertex $v$ with one-body marginal $\rho_v$:
$(v, w) \in E \iff \langle 01\rvert\rho_{vw}\lvert 12\rangle \neq 0$; then $2j_{(v,w)} + 1 = \langle 01\rvert\rho_{vw}\lvert 23\rangle / \langle 01\rvert\rho_{vw}\lvert 12\rangle$; and $k_v + 1 = \langle 3\rvert\rho_v\lvert 5\rangle / \langle 3\rvert\rho_v\lvert 4\rangle$.
Hence $\mathcal{S} \mapsto \Gamma_{\mathcal{S}}$ is injective, and the decoding does not use $\eta$, $\kappa$.

**(c) Restriction.** For $W \subset V$, the decoding of $\mathrm{Tr}_{V \setminus W}\,\Gamma_{\mathcal{S}}$ is the induced subnetwork $\mathcal{S}\vert_W$ (the edges with both ends in $W$, their spins, the labels on $W$). Encoding followed by decoding thus turns partial trace into restriction to induced subnetworks.

**(d) No state-preserving covariant functor.** For $M_1 < M_2$ and full-rank $\Gamma_{\mathcal{S}_2}$, no isometry $V: (\mathbb{C}^7)^{\otimes M_1} \to (\mathbb{C}^7)^{\otimes M_2}$ satisfies $V\,\Gamma_{\mathcal{S}_1} V^\dagger = \Gamma_{\mathcal{S}_2}$.

**(e) Group chain.** $SU(3) = \mathrm{Stab}_{G_2}(e_O)$ (T-42e) and the standard $SU(2) \subset SU(3)$ give, as complex representations, $\mathbf{7} \to \mathbf{1} \oplus \mathbf{3} \oplus \bar{\mathbf{3}} \to \mathbf{1} \oplus (\mathbf{2} \oplus \mathbf{1}) \oplus (\mathbf{2} \oplus \mathbf{1})$. (The split is of representations over $\mathbb{C}$, not a split of the seven coordinate axes; `check_core_numbers.py`, `test_no_axis_triple_is_su3_invariant`.)
:::

A graph with loops or multiple edges is encoded after subdividing each edge once (both halves carry $j_e$) and marking the subdivision vertices by $\lvert\chi\rangle \propto \lvert 3\rangle + \lvert 4\rangle$, whose ratio in (b) is $0$; then $M = \lvert V\rvert + \lvert E\rvert$.

### Lemma C29' (restated: the encoding of Theorem T-171) [T] {#lemma-c29}

**Statement.** Parts (a)–(c) of T-171. The former Lemma C29' (bounded spins $j_e \leq 3$, state built from $W_e^{\text{spin}}$) is retracted [✗] (audit items 1–2); the restated lemma has no bound on the spins.

**Proof.** *(a)* $\psi_j$, $\chi_k$ and $\mathbb{1}/7^{m}$ are density matrices, and so are their tensor products; the coefficients $1 - \eta\lvert E\rvert - \kappa M$, $\eta$, $\kappa$ are non-negative and sum to 1 over the $1 + \lvert E\rvert + M$ summands, so $\Gamma_{\mathcal{S}}$ is a convex combination of states. If the first coefficient $c$ is positive, $\Gamma_{\mathcal{S}} \geq c\,\mathbb{1}/7^M > 0$.

*(b)* Every matrix element used is of the form $\langle ab\rvert X \otimes Y\lvert cd\rangle = \langle a\rvert X\lvert c\rangle\langle b\rvert Y\lvert d\rangle$ with $a \neq c$ and $b \neq d$ (two-body) or $\langle a\rvert X \lvert c\rangle$ with $a \neq c$ (one-body). Compute the contributions of each summand of $\Gamma_{\mathcal{S}}$ to $\rho_{vw}$:
- the identity term gives $\mathbb{1}/49$ — diagonal, contributes 0;
- $\psi_{j_e}$ for $e = (v, w)$ gives $\eta\,\psi_{j_e}$ itself: $\langle 01\rvert\psi_j\lvert 12\rangle = 1/n_j^2$ and $\langle 01\rvert\psi_j\lvert 23\rangle = (2j+1)/n_j^2$, $n_j^2 = 2 + (2j+1)^2$;
- $\psi$ on the reversed pair $(w, v)$ cannot occur (at most one edge between two vertices); in any case $\langle 10\rvert\psi\lvert 21\rangle = 0$, since $\lvert\psi\rangle$ has components only on $\lvert 01\rangle, \lvert 12\rangle, \lvert 23\rangle$;
- $\psi$ on an edge sharing one vertex with $\{v, w\}$ gives (one-body marginal of $\psi$) $\otimes\, \mathbb{1}/7$; both one-body marginals of $\lvert\psi_j\rangle$ are diagonal, because the three components have pairwise different first and pairwise different second factors — contributes 0;
- edges disjoint from $\{v, w\}$ give $\mathbb{1}/49$; vertex terms give $\chi \otimes \mathbb{1}/7$ or $\mathbb{1}/7 \otimes \chi$, whose second or first factor is diagonal — contribute 0.
So $\langle 01\rvert\rho_{vw}\lvert 12\rangle = \eta/n_j^2$ if $(v, w) \in E$ and $0$ otherwise, and the ratio is $2j + 1$. For $\rho_v$: edge terms give diagonal one-body marginals, the identity is diagonal, other vertices give $\mathbb{1}/7$; only $\kappa\chi_{k_v}$ contributes to $\langle 3\rvert\rho_v\lvert 4\rangle = \kappa/m_k^2$ and $\langle 3\rvert\rho_v\lvert 5\rangle = \kappa(k_v+1)/m_k^2$.

*(c)* The two- and one-body marginals of $\mathrm{Tr}_{V\setminus W}\Gamma_{\mathcal{S}}$ on $W$ are those of $\Gamma_{\mathcal{S}}$; by (b) they decode to the edges, spins and labels inside $W$. $\blacksquare$

### Proof of T-171

(a)–(c) are Lemma C29'. *(d)* $\mathrm{rank}\,(V\Gamma_{\mathcal{S}_1}V^\dagger) \leq 7^{M_1} < 7^{M_2} = \mathrm{rank}\,\Gamma_{\mathcal{S}_2}$. *(e)* $SU(3) = \mathrm{Stab}_{G_2}(e_O)$ is T-42e; the restriction of the 7-dimensional representation of $G_2$ to $SU(3)$ is $\mathbf{1} \oplus \mathbf{3} \oplus \bar{\mathbf{3}}$ after complexification (the real $\mathbf{6} = e_O^\perp$ becomes $\mathbb{C}^3$ with the complex structure $x \mapsto e_O x$), and $\mathbf{3}\vert_{SU(2)} = \mathbf{2} \oplus \mathbf{1}$ for the standard embedding. $\blacksquare$

Numerical check: `check_core_numbers.py`, `test_t171_spin_networks_with_unbounded_spin_are_decoded_from_ratios_of_coherences` — random directed graphs on 2 and 3 vertices with spins up to 20 and labels up to 5: $\Gamma_{\mathcal{S}}$ is a full-rank state, edges, directions, spins and labels are decoded exactly, and the partial trace over one vertex decodes to the induced subnetwork; the old $W_e^{\text{spin}}$ is not Hermitian and has trace $\neq 1$; the old floor decoding returns 0 for every $j \leq 3$ at $\eta = 1/4$ and $\eta = 1/10$; the cluster sub-spin of $j = 7/2$ is $7/4$.

**Theorems used:** T-42e [T] (only for (e)). The encoding (a)–(d) uses no UHM theorem. Removed: T-53 (the "$\{A,S,D\}$-sector" reading), T-80, GNS completion (the restated statement is about finite networks).

*Status history:* [C at C29] originally; [T for $j_e \leq 3$] via Lemma C29' until 2026-09-26; restated 2026-09-26 — [T] for all finite spin networks, the former Lemma C29' and its functor [✗].

### 2.3a Extension to unbounded spin {#t-171-prime-unbounded}

#### Theorem T-171' (unbounded spin) [T] — a corollary of the restated T-171

:::tip Theorem T-171'
Every finite spin network with unbounded spins $j_e \in \tfrac12\mathbb{Z}_{\geq 0}$ is encoded injectively in a state of $M = \lvert V\rvert$ holons, with local decoding and restriction as in T-171 (a)–(c).
:::

**Proof.** T-171 (a)–(c) put no bound on $j_e$. $\blacksquare$

The former proof by a cluster construction ($k_e = \lceil j_e/3\rceil$ holons per edge, "additive" spin along the chain, $M_{\text{total}} = O(\lvert E\rvert\, j_{\max})$) is retracted [✗] (audit item 5): its sub-spins are not half-integers in general, it divides by zero for $k_e = 1$, and spins do not add along a chain. The statement survives with a smaller register, $M = \lvert V\rvert$ instead of $O(\lvert E\rvert\, j_{\max})$.

### 2.3 Fano amplitudes: finite ansatz and invariant tensors {#fano-spin-foam}

The finite incidence diagram can label an amplitude ansatz after spins, contractions and weights are specified. This is not an embedding theorem for spin-foam dynamics.

#### Corrected scope of Theorem 2.3 {#теорема-2-3-fano-axioms}

The former proof of axioms (A1)–(A4) is withdrawn [✗], except its elementary **finite-sum finiteness** statement: any finite product of finite magnetic-index sums with finite chosen weights is finite [T]. The errors are substantive:

1. A Wigner $3j$ symbol is an invariant **tensor**, but summing its entries against a fixed vector of ones is not automatically an invariant contraction. Each internal index must have a declared representation and an invariant pairing/intertwiner. A finite scalar expression alone supplies no action on boundary states.
2. Gluing tensor networks is contraction over boundary indices. In general $\sum_m a_mb_m\ne (\sum_m a_m)(\sum_m b_m)/(2j+1)$. The cited orthogonality relation sums **two** magnetic indices with the required matched representations; it does not prove the former one-index product formula. Nor is the number $1/(2j+1)$ a projector: its square differs from itself for $j>0$.
3. A fixed seven-point Fano frame is not invariant under continuous $G_2$. Its incidence automorphism group is finite. A $G_2$-invariant amplitude requires declared $G_2$ representation labels and invariant tensor contractions, or covariant transport of the entire frame. The withdrawn universal T-42a encoder rigidity cannot supply this data.
4. A Casimir on the irreducible fundamental $\mathbf7$ is $cI$. Thus $\prod_p\langle\psi_p|\mathcal C_{G_2}|\psi_p\rangle=c^7$ for normalized $\psi_p$ in that representation. This invariant is a constant and does not define a nontrivial spin-dependent weight or a map from $SU(2)$ spin labels to these vectors.

A valid replacement programme [Pr] chooses boundary representation spaces and intertwiners, contracts matching indices by invariant pairings, and defines gluing as that contraction. Under these choices invariance follows from invariance of the constituent tensors [T]; physical correspondence, convergence and any specific nontrivial weight remain additional claims. This retains ordinary representation mathematics without identifying arbitrary products of line labels with a quantum-gravity amplitude.

The old tetrahedral Ponzano–Regge asymptotic was also attached to a $3j$ symbol incorrectly: the tetrahedral formula concerns a $6j$ symbol under its nondegenerate asymptotic hypotheses. It gives no Einstein–Hilbert limit for the former seven-line ansatz. Neither finite kinematic encoding (T-171) nor a spacetime bridge proves that dynamical limit. [Roberts, *Classical 6j-symbols and the tetrahedron*](https://arxiv.org/abs/math-ph/9812013).

### 2.4 Embedding Assessment

| Aspect | Status | Comment |
|--------|--------|---------|
| $SU(2) \subset SU(3) \subset G_2$ | **[T]** | T-171 (e): branching of representations over $\mathbb{C}$ |
| Graph, directions, spins, intertwiner labels in one state | **[T]** | T-171 (a)–(b): read from ratios of coherences, $M = \lvert V\rvert$ holons |
| Restriction to induced subnetworks = partial trace | **[T]** | T-171 (c) |
| Unbounded spin | **[T]** | T-171' as a corollary; the cluster construction is retracted [✗] |
| Former Lemma C29' ($W_e^{\text{spin}}$, $j_e \leq 3$) and its covariant functor | **[✗]** | Not a density matrix; spin not recovered; no state-preserving isometry (T-171 (d)) |
| Area spectrum "from finite-dimensionality" | withdrawn | The LQG area formula is a function of the labels, not derived |
| Fano amplitudes (A1)–(A4) | **[✗] / [Pr]** | Finite sums retained; invariant contractions and gluing must be supplied (§2.3) |
| Fano amplitudes (semi-classical limit) | **[C]** | Fano-Regge compatibility — open problem |

---

## 3. Causal Sets {#каузальные-множества}

### 3.1 Mathematical Context

The theory of causal sets (Bombelli–Lee–Meyer–Sorkin, 1987) postulates:
- A discrete set of events $(C, \preceq)$ with a partial order;
- Causal structure is fundamental; metric and topology are derived;
- The number of elements of a causal set ↔ volume ($V \sim N$ — the Hauptvermutung);
- The d'Alembertian on a causal set → curvature in the continuum limit.

### 3.2 Embedding Construction {#causal-embedding}

#### T-172: Causal sets — encoding in holonic states and embedding as internal categories [T] {#t-172}

:::warning Corrected 2026-09-26 — audit of T-172 and Lemma C30
T-172 stated that every finite causal set faithfully embeddable into $M^4$ "embeds into the ∞-topos $\mathbf{Sh}_\infty(\mathcal{C})$ via the nerve", with the causal order realised by Gap coherences (Lemma C30). The audit found:
1. **The nerve is not an embedding into the ∞-topos [✗].** There is no "Yoneda embedding of simplicial sets into an arbitrary ∞-topos" (HTT 6.1.3.8 is not such a statement). The canonical functor $\mathbf{sSet} \to \mathcal{S} \xrightarrow{\pi^*} \mathbf{Sh}_\infty(\mathcal{C})$ (realisation, then constant sheaf) inverts weak equivalences: every poset with a least element has a contractible nerve and goes to the terminal object, and $C$ and $C^{\mathrm{op}}$ have the same realisation. The one-element poset and the two-element chain both go to $1$, and the two maps from the first to the second become one map. So "embeds" in (a) and the functor of Step 4 are false as stated.
2. **$W_{cc'} \geq 0$ is false for general phases [✗].** $W_{cc'} = \tfrac17\sum_{ij} e^{i\theta_{ij}}\lvert i\rangle\langle j\rvert \otimes \lvert i\rangle\langle j\rvert$ is positive only for $\theta_{ij} = \phi_i - \phi_j$; for random antisymmetric phases its least eigenvalue is $-0.31$. Step 5 ("convex combination of positive operators") fails with it.
3. **Step 1 fails for equal times [✗].** $\delta = \tfrac12\min_{c\neq c'}\lvert t_c - t_{c'}\rvert$ is $0$ when two spacelike elements have equal times, which faithful embeddings allow; "the difference is ensured by spatial separation" is false.
4. **The hypothesis (C30) is not used.** Apart from the phases, the construction never uses the embedding $\varphi: C \to M^4$; it can be dropped.

*Route taken.* The encoding is rebuilt with an ordered pair state that carries the direction of the order, so no clock labels and no $M^4$-embedding are needed; and the topos statement is replaced by the correct fully faithful one — posets as internal categories (Segal objects) of $\mathbf{Sh}_\infty(\mathcal{C})$, which exists because $\mathcal{D}(\mathbb{C}^7)$ is connected. The status stays [T] with a stronger statement.
:::

:::tip Theorem T-172 (restated 2026-09-26) [T]
Let $(C, \preceq)$ be a finite partially ordered set — any, no embedding into $M^4$ assumed; $M = \lvert C\rvert$, $N_\prec = \#\{(c, c') : c \prec c'\}$.

**(a) Encoding.** For $\eta \in (0, 1/N_\prec]$ put

$$
\Gamma_C := (1 - \eta N_\prec)\,\frac{\mathbb{1}}{7^M} + \eta \sum_{c \prec c'} \psi^{(c,c')} \otimes \frac{\mathbb{1}}{7^{M-2}}, \qquad \lvert\psi\rangle = \tfrac{1}{\sqrt2}\big(\lvert 01\rangle + \lvert 12\rangle\big) \text{ on the ordered pair } (c, c').
$$

Then $\Gamma_C \in \mathcal{D}\big((\mathbb{C}^7)^{\otimes M}\big)$, and for $c \neq c'$ with two-body marginal $\rho_{cc'}$: $c \prec c' \iff \langle 01\rvert\rho_{cc'}\lvert 12\rangle \neq 0$ (the value is then $\eta/2$). For $D \subset C$, the decoding of $\mathrm{Tr}_{C \setminus D}\,\Gamma_C$ is the induced order on $D$.

**(b) Internal categories.** Let $X = \mathcal{D}(\mathbb{C}^7)$ with the topology of the Bures metric, $\mathcal{E} = \mathbf{Sh}_\infty(X)$ and $\pi^*: \mathcal{S} \to \mathcal{E}$ the constant-sheaf functor. The functor

$$
\mathbf{Poset}_{\text{fin}} \to \mathrm{Fun}(\Delta^{\mathrm{op}}, \mathcal{E}), \qquad C \mapsto \pi^* N_\bullet(C)
$$

(levelwise constant sheaf on the finite sets of $n$-chains $c_0 \preceq \dots \preceq c_n$) is fully faithful: each mapping space $\mathrm{Map}(\pi^*N_\bullet C, \pi^*N_\bullet C')$ is discrete and equals the set of order-preserving maps $C \to C'$. Its values are Segal objects (internal categories) of $\mathcal{E}$.

**(c) The realisation forgets the order.** $C \mapsto \pi^*\lvert N_\bullet(C)\rvert \in \mathcal{E}$ is neither faithful nor injective on isomorphism classes.

**(d) Clock labels.** The rank $\tau_c$ of $c$ in a linear extension of $\preceq$ is strictly monotone ($c \prec c' \Rightarrow \tau_c < \tau_{c'}$) and takes $M$ values, which the $6M + 1$ readings of the summed clock of $M$ holons accommodate ([composite clocks](/docs/proofs/dynamics/emergent-time#композитные-часы)). (a) does not need them.
:::

The former part (b), "$v \preceq w \Leftrightarrow \tau_v \leq \tau_w \wedge d_{\mathcal{G}}(v, w) \leq c\,\lvert\tau_w - \tau_v\rvert$", defines a derived relation from clock labels and a distance; it is a definition, not a theorem, and nothing below uses it. The continuum remark (recovery of $M^4$ under T-118, T-119, T-120) is not part of T-172.

### Lemma C30 (restated: the encoding (a)) [T] {#lemma-c30}

**Statement.** Part (a) of T-172, for every finite poset. The former Lemma C30 (faithful $M^4$-embedding, $W_{cc'}$ with geometric phases, time discretisation $\tau_c = \lfloor t_c/\delta\rfloor$) is retracted [✗] (audit items 2–3).

**Proof.** $\psi$ and $\mathbb{1}/7^m$ are states and the coefficients are non-negative with sum 1, so $\Gamma_C$ is a state. For the marginal $\rho_{cc'}$, the matrix element $\langle 01\rvert X \otimes Y \lvert 12\rangle = \langle 0\rvert X\lvert 1\rangle\langle 1\rvert Y\lvert 2\rangle$ vanishes whenever $X$ or $Y$ is diagonal. The summand for the pair $(c, c')$ itself gives $\eta\,\langle 01\rvert\psi\rangle\langle\psi\lvert 12\rangle = \eta/2$. The summand for the reversed pair $(c', c)$, read in the order $(c, c')$, gives $\eta\,\langle 10\rvert\psi\rangle\langle\psi\lvert 21\rangle = 0$ (and it is absent anyway, by antisymmetry of $\prec$). A summand for a pair sharing one element with $\{c, c'\}$ gives a one-body marginal of $\psi$ tensored with $\mathbb{1}/7$; the one-body marginals $\tfrac12(\lvert 0\rangle\langle 0\rvert + \lvert 1\rangle\langle 1\rvert)$ and $\tfrac12(\lvert 1\rangle\langle 1\rvert + \lvert 2\rangle\langle 2\rvert)$ are diagonal. All other summands give $\mathbb{1}/49$. Hence $\langle 01\rvert\rho_{cc'}\lvert 12\rangle = \eta/2$ if $c \prec c'$ and $0$ otherwise. Marginals of $\mathrm{Tr}_{C\setminus D}\Gamma_C$ on $D$ are those of $\Gamma_C$. $\blacksquare$

### Proof of T-172

*(a)* is Lemma C30.

*(b)* The nerve $N: \mathbf{Cat} \to \mathbf{sSet}$ is fully faithful, so order-preserving maps $C \to C'$ are exactly the simplicial maps $N_\bullet C \to N_\bullet C'$. $X$ is connected (a convex subset of the Hermitian matrices, hence path-connected). For finite sets $A, B$: $\mathrm{Map}_{\mathcal{E}}(\pi^*A, \pi^*B) \simeq \mathrm{Map}_{\mathcal{S}}(A, \pi_*\pi^*B)$, and $\pi_*\pi^*B$ is the set of locally constant functions $X \to B$ — which, $X$ being connected, is $B$. So $\pi^*$ is fully faithful on finite sets, with discrete mapping spaces. A map of simplicial objects between levelwise images $\pi^*A_\bullet \to \pi^*B_\bullet$ is computed by the end $\int_{[n]}\mathrm{Map}_{\mathcal{E}}(\pi^*A_n, \pi^*B_n) = \int_{[n]}\mathrm{Hom}(A_n, B_n) = \mathrm{Hom}_{\mathbf{sSet}}(A_\bullet, B_\bullet)$. The Segal maps $N_n C \to N_1 C \times_{N_0 C} \dots \times_{N_0 C} N_1 C$ are bijections, and $\pi^*$ preserves finite limits, so $\pi^*N_\bullet C$ satisfies the Segal condition.

*(c)* A poset with a least element $\bot$ has a contractible realisation (the nerve is a cone with apex $\bot$). So the one-element poset $\{\ast\}$ and the chain $\{0 \prec 1\}$ both go to the terminal object $1 \in \mathcal{E}$, and the two order-preserving maps $\{\ast\} \to \{0 \prec 1\}$ go to the one map $1 \to 1$: not faithful. The chains of $C$ and of $C^{\mathrm{op}}$ are the same subsets, so $\lvert N_\bullet C\rvert \cong \lvert N_\bullet C^{\mathrm{op}}\rvert$; the poset $\{\bot \prec a, \bot \prec b\}$ and its opposite are not isomorphic and have the same image, and so do the chains of one and of two elements (both go to $1$): not injective on isomorphism classes.

*(d)* Every finite poset has a linear extension (Szpilrajn); its rank function is strictly monotone. $\blacksquare$

Numerical check: `check_core_numbers.py`, `test_t172_every_finite_poset_is_encoded_and_realisation_forgets_order` — random posets on 2–4 elements: $\Gamma_C$ is a state, the order is decoded exactly, and the partial trace over one element decodes to the induced order; the old $W_{cc'}$ with random antisymmetric phases has a negative eigenvalue; the order complex of a chain of 1–4 elements has Euler characteristic 1, and a random poset and its opposite have the same chains.

**Status:** [T]. Uses: nerves of categories (Mac Lane 1998); the global-sections geometric morphism $\pi: \mathcal{E} \to \mathcal{S}$ (HTT Prop. 6.3.4.1) and constant sheaves on a connected space; Szpilrajn's extension theorem; [composite clocks](/docs/proofs/dynamics/emergent-time#композитные-часы) (only for (d)). Removed: HTT 6.1.3.8 (misquoted), T-38b as a clock construction (only the reading count is used), T-117–T-120 (the continuum remark is not part of the theorem).

*Status history:* [C at C30] originally; [T] from the former Lemma C30 until 2026-09-26; restated 2026-09-26 — [T] for every finite poset, the nerve-as-object "embedding" and the former Lemma C30 [✗].

### 3.3 Embedding Assessment

| Aspect | Status | Comment |
|--------|--------|---------|
| Order of any finite poset in one state | **[T]** | T-172 (a): read from $\langle 01\rvert\rho_{cc'}\lvert 12\rangle$; no $M^4$-embedding needed |
| Posets as internal categories of $\mathbf{Sh}_\infty(\mathcal{C})$ | **[T]** | T-172 (b): fully faithful, because $\mathcal{D}(\mathbb{C}^7)$ is connected |
| Nerve realised as an object of the ∞-topos | **[✗]** as an embedding | T-172 (c): contractible for any poset with a least element |
| Discrete time structure | **[T]** | $6M+1$ readings of the summed clock (T-38b [T] per holon); linear-extension ranks fit (T-172 (d)) |
| Continuum limit → $M^4$ | not part of T-172 | T-118, T-119, T-120 are separate theorems |

---

## 4. Universal Property of the UHM ∞-Topos {#универсальное-свойство}

### 4.1 Mathematical Context

A category-theoretic justification of the Meta-ToE status asks which **universal property** the UHM primitive has in an appropriate category of physical theories. T-174 answers it: the property that holds is carried by the kinematic object $(A_{\text{int}}, \text{trivial dynamics})$ and goes *from* UHM *to* the theories that contain its structure; the former "receiving map from every theory into $\mathbf{Sh}_\infty(\mathcal{D}(\mathbb{C}^7), J_{\text{Bures}})$" is false.

Key references:
- **Schreiber (2013, 1310.7930):** Differential cohomology in a cohesive ∞-topos. Gauge fields, QFT, BV-BRST formalism — all within cohesive ∞-toposes.
- **Baez (1995, q-alg/9503002):** Higher algebra and topological QFT. Extended TQFTs as functors from nCob.
- **Lurie (2009):** Classification of extended TQFTs: fully dualizable objects.

### 4.2 Category of Physical Theories {#категория-phys}

**Definition (Category $\mathbf{PhysTheory}$).** $\mathbf{PhysTheory}$ is the ∞-category of [T-211](/docs/proofs/categorical/fundamental-closures#t-211): the cartesian unstraightening over $\mathbf{Topoi}_\infty$ of $E \mapsto \mathrm{Dyn}(E) = \mathrm{Fun}(B\mathbb{R}, \mathrm{Alg}(E))$. Objects are triples $(E, \mathcal{A}, D)$:
- $E$ — an ∞-topos;
- $\mathcal{A}$ — an associative algebra (monoid) object of $E$ for its cartesian structure;
- $D$ — an action of the group $\mathbb{R}$ on $\mathcal{A}$ by algebra automorphisms.

A morphism $(E_1, \mathcal{A}_1, D_1) \to (E_2, \mathcal{A}_2, D_2)$ is a triple $(f, \alpha, \beta)$:
- $f: E_1 \to E_2$ — a geometric morphism, with inverse image $f^*: E_2 \to E_1$;
- $\alpha: \mathcal{A}_1 \to f^*\mathcal{A}_2$ — a map of algebra objects in $E_1$;
- $\beta$ — the coherent family of homotopies $\beta_t: \alpha \circ D_1(t) \simeq f^*D_2(t) \circ \alpha$, $t \in \mathbb{R}$ (T-211 (b)).

*Typing (2026-09-26).* The former definition read "$\alpha$ — algebra homomorphism" and "$\beta: D_1 \to f^*D_2 \circ \alpha$"; the second is ill-typed ($D_1$ acts on $\mathcal{A}_1$, $f^*D_2 \circ \alpha$ is a map out of $\mathcal{A}_1$ into $f^*\mathcal{A}_2$). In T-211, $\alpha$ is a map of *monoids*: nothing makes it linear or $*$-preserving. Statements about $C^*$-algebras therefore use the $C^*$-typed subcategory of §4.4, where $\alpha$ is a unital $*$-homomorphism, or state explicitly that $\alpha$ is a completely positive map, which is not a morphism of $\mathbf{PhysTheory}$.

### 4.3 Scope of primitive uniqueness {#теорема-единственности-мета}

#### T-173: former universal rigidity [✗] {#t-173}

The former proof did not determine a unique structured physical primitive. Monotone quantum metrics form a family; choosing the normalized minimal Bures metric is a definition, not uniqueness of all monotone metrics. Its open-cover site gives a sheaf topos on the **specified** state space. The classifier is a sheaf of opens and does not generate basis projectors, a primitive Liouvillian, a Hamiltonian or numerical rates. Pointer dephasing alone is not primitive: it preserves every diagonal population.

Dimension seven requires the explicit premises of the [minimality theorem](/docs/proofs/minimality/theorem-minimality-7). A positive octonionic form has stabilizer $G_2$, but this codomain symmetry does not identify physical encoders. The former T-42a/T-123 universal rigidity is withdrawn; RI gives a conditional comparison for supplied encoders, not an equivalence of arbitrary topoi or uniqueness of their dynamical structure.

For fixed $N$ and the specified open-cover site, $\operatorname{Sh}_\infty(X_N)$ is determined up to equivalence by that construction [T]. Further frame, form, dynamics, clock scale and interpretation are separate input. Many different Hamiltonians and rates share the same site and state space. Thus the former uniqueness up to only $G_2\times\mathbb R_{>0}$ is false as a conclusion of (i)–(iii).

### 4.4 Universal Property: Receiving Map {#приёмное-отображение}

#### T-174: Universal property of the UHM kinematic object [T] {#t-174}

:::warning Corrected 2026-09-26 — audit of T-174
T-174 stated: for every $(E, \mathcal{A}, D)$ with (a) a $C^*$-subalgebra $\cong A_{\text{int}} = \mathbb{C} \oplus M_3(\mathbb{C}) \oplus M_3(\mathbb{C})$ in $\mathcal{A}$, (b) CPTP dynamics, (c) a distinguished observable subalgebra of dimension $\leq 7$, there is an essentially unique morphism $(f^*, \alpha, \beta): (E, \mathcal{A}, D) \to (\mathbf{Sh}_\infty(\mathcal{C}), A_{\text{int}}, \mathcal{L}_\Omega)$, unique up to $G_2 \times \mathbb{R}_{>0}$. Every step of the proof fails:
1. **Lemma 1 [✗].** "$\mathrm{Mod}_{A_{\text{int}}}(E)$ — a stable $(\infty,1)$-category — is an $(\infty,1)$-topos." A non-trivial stable ∞-category is never an ∞-topos: in an ∞-topos the initial object is strict (every map $X \to \emptyset$ is an equivalence — pull the empty colimit back along it, by universality of colimits, HTT Thm. 6.1.0.6), while in a stable ∞-category every $X$ maps to the zero object, so $X \simeq 0$. Moreover $A_{\text{int}}$ is not $E_\infty$ ($M_3(\mathbb{C})$ is not commutative), HA 4.5.1.1 does not say this, and modules are not a subcategory of $E$ — the forgetful functor is not fully faithful — so "subtopos $E[A_{\text{int}}]$" has no meaning.
2. **Lemma 2 [✗].** "$\mathrm{Mod}(A_{\text{int}}) \simeq \mathcal{D}(\mathbb{C}^7)$ by T-53." The finite-dimensional modules form a semisimple additive category with three simple objects ($\mathbb{C}, \mathbb{C}^3, \mathbb{C}^3$), Morita equivalent to $\mathrm{Vect}^3$; $\mathcal{D}(\mathbb{C}^7)$ is a convex set of matrices, not a category of modules, and $\mathbf{Sh}_\infty(\mathcal{D}(\mathbb{C}^7))$ is not additive (its initial and terminal objects differ). T-53 contains no such statement.
3. **Step 4 [✗].** A conditional expectation is not an algebra homomorphism: on $M_2(\mathbb{C})$ the expectation onto the diagonal sends $\sigma_x \mapsto 0$ but $\sigma_x^2 = 1 \mapsto 1$. It is also not unique without a state: $A_{\text{int}} \otimes \mathbb{C}^2 \to A_{\text{int}}$, $a \otimes (x, y) \mapsto a(\lambda x + (1-\lambda)y)$ is a conditional expectation for every $\lambda \in [0,1]$. Takesaki's theorem is about a *state-preserving* expectation, which exists iff the subalgebra is invariant under the modular group. "$f^*A_{\text{int}} = A_{\text{int}}$ in $E$" also inverts the direction: $f^*$ goes from the target topos to $E$.
4. **The target is not an object [✗].** $\mathcal{L}_\Omega = -i[H_{\text{eff}}, \cdot] + \mathcal{D}_\Omega + \mathcal{R}[\cdot, E]$ contains the non-linear regeneration $\mathcal{R}$, and its linear part generates a dissipative semigroup, not an action $\mathbb{R} \to \mathrm{Aut}(A_{\text{int}})$ by algebra automorphisms (a unital multiplicative $*$-map of a matrix algebra is $\mathrm{Ad}\,u$, whose generator has purely imaginary spectrum; a primitive Liouvillian has eigenvalues with negative real part).
5. **Step 5 [✗].** "$D\vert_{A_{\text{int}}} = g\,\mathcal{L}_\Omega\,g^{-1}$ for a unique $g \in G_2$" is false: $(\mathcal{S}, A_{\text{int}}, \mathrm{id})$ satisfies (a)–(c) and its dynamics fixes all 19 dimensions of $A_{\text{int}}$, while a primitive dynamics fixes a 1-dimensional subspace. Condition (c) is vacuous — every algebra has the subalgebra $\mathbb{C}1$ of dimension $1 \leq 7$ — and cannot make $\alpha$ "injective on observables".
6. **Step 6 [✗].** The geometric-morphism part is not unique up to $G_2 \times \mathbb{R}_{>0}$: geometric morphisms from the point $\mathcal{S}$ to $\mathbf{Sh}_\infty(X)$, $X = \mathcal{D}(\mathbb{C}^7)$ sober, are the points of $X$ (HTT §6.4.5, 0-localic ∞-topoi) — a 48-dimensional family — while the $G_2$-orbits in $X$ have dimension at most 14 and $\mathbb{R}_{>0}$ (the scale $\omega_0$) does not act on $X$.
7. **The statement itself is false in both typings [✗].** With $\alpha$ a unital $*$-homomorphism, no morphism $(\mathcal{S}, M_7(\mathbb{C}), D) \to (\mathcal{S}, A_{\text{int}}, \cdot)$ exists for any $D$, although $M_7(\mathbb{C}) \supset A_{\text{int}}$ satisfies (a)–(c): there is no non-zero $*$-homomorphism $M_7(\mathbb{C}) \to A_{\text{int}}$. With $\alpha$ a map of monoids (T-211 as it stands), such morphisms exist but are not essentially unique: $a \mapsto \det(a)^k\,1$, $k = 0, 1, 2, \dots$, are pairwise distinct modulo $\mathrm{Aut}(A_{\text{int}}, \cdot)$.
8. **The coherence paragraph** cited "full embedding into $\mathbf{Topoi}_\infty$ … fully faithful by T-173 … HTT 5.2.7"; that claim is retracted in [T-211](/docs/proofs/categorical/fundamental-closures#t-211), which supplies the coherences as a Grothendieck construction instead.

*Routes tried to keep a receiving map* $x \to \text{UHM}$: (i) $*$-homomorphisms — no existence (item 7); (ii) monoid maps — no uniqueness (item 7); (iii) completely positive maps (conditional expectations) — existence always (finite-dimensional $C^*$-algebras are injective), uniqueness only after fixing a faithful trace, and the target dynamics must be the restriction of the source dynamics, so there is no single target object — this route survives as part (d) below; (iv) the opposite direction, UHM $\to x$ — succeeds and gives the universal property (a)–(c). The old statement is retracted [✗]; the restated T-174 is [T].
:::

**Setting.** Consider the fibre of $\mathbf{PhysTheory}$ over the terminal ∞-topos $\mathcal{S}$ (theories over a point). Its subcategory $\mathbf{PhysTheory}^{C^*}_{\mathrm{pt}}$ has as objects $x = (\mathcal{S}, A, \sigma)$ with $A$ a unital $C^*$-algebra (entering T-211 through its multiplicative monoid) and $\sigma: \mathbb{R} \to \mathrm{Aut}(A)$ a group of $*$-automorphisms, and as morphisms $(\mathrm{id}, \alpha, \beta)$ with $\alpha$ a unital $*$-homomorphism; identities and composites of such are such, so this is a (non-full) subcategory. Because the objects are 0-truncated, the fibre of T-211 (b) is a set: $\beta$ exists iff $\alpha \circ \sigma_1(t) = \sigma_2(t) \circ \alpha$ for all $t$, and is then unique — compatibility with dynamics is a property, not data. Put

$$
u_0 := (\mathcal{S}, A_{\text{int}}, \mathrm{id}), \qquad x_n := (\mathcal{S}, M_n(\mathbb{C}), \mathrm{id}), \qquad A^\sigma := \{a \in A : \sigma_t(a) = a \ \forall t\}.
$$

:::tip Theorem T-174 (restated 2026-09-26) [T]
**(a) Corepresentation.** For every object $x = (\mathcal{S}, A, \sigma)$, morphisms $u_0 \to x$ are in bijection with the $A_{\text{int}}$-structures in $A^\sigma$: families $\big(p;\ (e_{ij})_{i,j=1}^3;\ (f_{ij})_{i,j=1}^3\big)$ in $A^\sigma$ with $p = p^* = p^2$, $e_{ij}^* = e_{ji}$, $e_{ij}e_{kl} = \delta_{jk}e_{il}$, the same for $f$, all products between $p$, $e$, $f$ equal to zero, and $p + \sum_i e_{ii} + \sum_i f_{ii} = 1$. The morphism is faithful (injective $\alpha$) iff $p$, $e_{11}$, $f_{11}$ are all non-zero. The former condition (a) — a copy of $A_{\text{int}}$ in $A$ — is necessary for a faithful morphism but not sufficient: the copy must contain $1_A$ and lie in $A^\sigma$.

**(b) Classification and rigidity at 7.** Up to conjugation by $U(n)$, morphisms $u_0 \to x_n$ correspond to triples $(a, b, c) \in \mathbb{Z}_{\geq 0}^3$ with $a + 3b + 3c = n$ (the multiplicities of the three summands). Faithful morphisms exist iff $n \geq 7$; they form exactly one conjugacy class iff $n \in \{7, 8, 9\}$ (for $n = 10$: three). The **multiplicity-free** faithful morphism ($a = b = c = 1$; commutant $\cong \mathbb{C}^3$, abelian) exists iff $n = 7$. For $n = 7$ the faithful morphisms $u_0 \to x_7$ form one $U(7)$-orbit, $U(7)/U(1)^3$, of real dimension 46.

**(c) Dynamics.** For $x = (\mathcal{S}, M_n(\mathbb{C}), \mathrm{Ad}\,e^{itH})$, $A^\sigma = \{H\}'$, and a faithful morphism $u_0 \to x$ exists iff the eigenspace dimensions $m_1, \dots, m_r$ of $H$ admit decompositions $m_i = a_i + 3b_i + 3c_i$ with $\sum_i a_i, \sum_i b_i, \sum_i c_i \geq 1$. For $n = 7$ the multiplicity-free morphism $\alpha_0$ (sector projections $P_0, P_1, P_2$ of ranks 1, 3, 3) is a morphism into $x$ iff $H \in \mathrm{span}(P_0, P_1, P_2)$; if $H$ has simple spectrum there is no faithful morphism at all. In the extension of the fibre to semigroups of unital completely positive maps (the group $B\mathbb{R}$ replaced by the monoid $\mathbb{R}_{\geq 0}$ — outside T-211 as stated), for a primitive semigroup $T$ on $M_n(\mathbb{C})$ the only morphism $u_0 \to (M_n(\mathbb{C}), T)$ is $\lambda \oplus A \oplus B \mapsto \lambda\,1$, which is not faithful. In particular a primitive linear part of the UHM Liouvillian (T-39a) fixes no faithful $A_{\text{int}}$-structure.

**(d) The receiving map on states.** Let $\alpha: u_0 \to x$ be faithful, $A$ finite-dimensional and $\tau$ a faithful tracial state on $A$. There is exactly one unital completely positive map $E: A \to A_{\text{int}}$ with $E \circ \alpha = \mathrm{id}$ and $\tau \circ \alpha \circ E = \tau$ — the $\tau$-preserving conditional expectation onto $\alpha(A_{\text{int}})$. If $\sigma_t$ preserves $\tau$ and $\alpha(A_{\text{int}})$ as a set, then $E \circ \sigma_t = (\alpha^{-1}\sigma_t\alpha) \circ E$. For $A = M_n(\mathbb{C})$, $E$ is never a homomorphism. For $n = 7$, $\alpha_0$ and $\tau = \mathrm{tr}/7$: $E(a) = (a_{00},\ P_1 a P_1,\ P_2 a P_2)$, and the induced map on states, $\rho \mapsto \rho \circ \alpha_0$, is the sector pinching $\rho \mapsto (\rho_{00}, P_1\rho P_1, P_2\rho P_2)$. This — a channel on states dual to the $*$-homomorphism $\alpha$, not a homomorphism $A \to A_{\text{int}}$ — is the correct content of the former "receiving map".

**(e) What the former statement becomes.** Receiving morphisms $x \to \text{UHM}$ in $\mathbf{PhysTheory}$ do not have the universal property: none exists for $x = x_7$ with $\alpha$ a $*$-homomorphism, and infinitely many pairwise inequivalent ones exist with $\alpha$ a monoid map. The universal property is carried by $u_0$ and goes in the opposite direction, (a)–(c).
:::

**Proof.**

*(a)* $A_{\text{int}}$ is the universal $C^*$-algebra on the generators $p, e_{ij}, f_{ij}$ with the stated relations: the relations say that $p$, $\sum e_{ii}$, $\sum f_{ii}$ are orthogonal projections with sum 1 and that $(e_{ij})$, $(f_{ij})$ are systems of $3 \times 3$ matrix units in the corners they cut out; the $*$-algebra they span has dimension at most $1 + 9 + 9 = 19$, and it maps onto $A_{\text{int}}$ (where the standard matrix units satisfy the relations), so it is $A_{\text{int}}$. Given such a family in $A^\sigma$, $\alpha(\lambda, (a_{ij}), (b_{ij})) := \lambda p + \sum a_{ij}e_{ij} + \sum b_{ij}f_{ij}$ is a unital $*$-homomorphism; since $u_0$ has trivial dynamics, the compatibility $\alpha = \sigma_t \circ \alpha$ says exactly that the image lies in $A^\sigma$. Conversely the images of the standard generators under a morphism form such a family. The ideals of $A_{\text{int}}$ are sums of its three summands, and $\alpha$ kills a summand iff it kills its unit $p$, $\sum e_{ii}$ or $\sum f_{ii}$ — equivalently $p$, $e_{11}$ or $f_{11}$ (as $e_{ii} = e_{i1}e_{11}e_{1i}$).

*(b)* A unital $*$-representation of $A_{\text{int}}$ on $\mathbb{C}^n$ is a direct sum of irreducibles — $\mathbb{C}$ (through the first summand), $\mathbb{C}^3$ (through the first $M_3$), $\mathbb{C}^3$ (through the second) — with multiplicities $(a, b, c)$, $a + 3b + 3c = n$; two are unitarily equivalent iff their multiplicities agree (semisimplicity). Faithful means $a, b, c \geq 1$, so $n \geq 7$. Faithful classes: $n = 7$: $(1,1,1)$; $n = 8$: $(2,1,1)$; $n = 9$: $(3,1,1)$; for $n \geq 10$ at least $(n-6,1,1)$, $(n-9,2,1)$, $(n-9,1,2)$. The commutant of the class $(a, b, c)$ is $M_a \oplus M_b \oplus M_c$, abelian iff $a, b, c \leq 1$; with faithfulness this forces $a = b = c = 1$, $n = 7$. The stabiliser of $\alpha_0$ under conjugation is the unitary group of the commutant, $U(1)^3$, so the orbit is $U(7)/U(1)^3$, of dimension $49 - 3 = 46$.

*(c)* The fixed-point algebra of $\{\mathrm{Ad}\,e^{itH}\}_{t \in \mathbb{R}}$ is the commutant $\{H\}' = \bigoplus_i M_{m_i}(\mathbb{C})$ over the eigenspaces. A unital $*$-homomorphism into it is a family of unital representations of $A_{\text{int}}$ on the eigenspaces, one per block, with multiplicities $(a_i, b_i, c_i)$; it is faithful iff each summand of $A_{\text{int}}$ appears in some block. For $\alpha_0$: $\alpha_0(A_{\text{int}}) \subset \{H\}'$ iff $H \in \alpha_0(A_{\text{int}})' = \mathrm{span}(P_0, P_1, P_2)$. Simple spectrum: $\{H\}'$ is abelian, and $M_3(\mathbb{C})$ has no non-zero $*$-homomorphism into an abelian algebra (its irreducible representations are 3-dimensional). For a primitive semigroup $T_t = e^{t\mathcal{L}^\dagger}$ on $M_n(\mathbb{C})$: primitivity means $\dim\ker\mathcal{L} = 1$ with a faithful stationary state; in finite dimensions $\dim\ker\mathcal{L}^\dagger = \dim\ker\mathcal{L} = 1$, and $\mathcal{L}^\dagger(1) = 0$ (unitality), so the fixed points are $\mathbb{C}1$. A morphism has image in the fixed points, so it is a character of $A_{\text{int}}$ times $1$; the only character is $\lambda \oplus A \oplus B \mapsto \lambda$ (the $M_3$ summands have no characters).

*(d)* On the finite-dimensional Hilbert space $L^2(A, \tau)$ let $E$ be the orthogonal projection onto $\alpha(A_{\text{int}})$, composed with $\alpha^{-1}$. It is the $\tau$-preserving conditional expectation (Umegaki 1954; Takesaki 1972 — the modular group of a trace is trivial, so the invariance condition holds), in particular unital completely positive with $E \circ \alpha = \mathrm{id}$. Uniqueness: if $E'$ is unital completely positive with $E' \circ \alpha = \mathrm{id}$, then $\alpha \circ E'$ is a projection of norm one onto $\alpha(A_{\text{int}})$, hence a conditional expectation (Tomiyama 1957), in particular $\alpha(A_{\text{int}})$-bimodular; if also $\tau \circ \alpha \circ E' = \tau$, then $\tau\big(\alpha(E'(a))\,\alpha(b)\big) = \tau\big(\alpha(E'(a\,\alpha(b)))\big) = \tau(a\,\alpha(b))$ for all $b \in A_{\text{int}}$, which is the defining property of $E$, so $E' = E$. Equivariance: for $b \in A_{\text{int}}$, $\tau(\alpha E(\sigma_t a)\,\alpha(b)) = \tau(\sigma_t(a)\,\alpha(b)) = \tau(a\,\sigma_{-t}\alpha(b)) = \tau(\alpha E(a)\,\sigma_{-t}\alpha(b)) = \tau(\sigma_t\alpha E(a)\,\alpha(b))$, using $\tau \circ \sigma_t = \tau$ and $\sigma_{-t}\alpha(b) \in \alpha(A_{\text{int}})$. Not a homomorphism for $A = M_n(\mathbb{C})$: a multiplicative $E$ has a two-sided ideal as kernel; $M_n(\mathbb{C})$ is simple and $E \neq 0$, so $E$ would be injective, $n^2 \leq 19$, contradicting $n \geq 7$. The formula for $n = 7$ satisfies $E \circ \alpha_0 = \mathrm{id}$ and $\mathrm{tr}(E(a)\,b) = \mathrm{tr}(a\,b)$ for block-diagonal $b$; by uniqueness it is $E$. The dual map on states is restriction along $\alpha_0$, which reads off the three diagonal blocks.

*(e)* A $*$-homomorphism $M_7(\mathbb{C}) \to A_{\text{int}}$ followed by the projection onto a summand $M_m$ ($m \in \{1, 3\}$) is a $*$-homomorphism $M_7(\mathbb{C}) \to M_m(\mathbb{C})$, which is zero because a non-zero one is a multiple of the 7-dimensional irreducible representation and $7 > m$; so the only $*$-homomorphism is $0$, which is not unital. Monoid maps: $a \mapsto \det(a)^k\,1$ is unital and multiplicative. If a monoid automorphism $\psi$ of $(A_{\text{int}}, \cdot)$ carried $\det^k 1$ to $\det^m 1$ with $k \neq m$, then $\psi(z^k 1) = z^m 1$ for all $z \in \mathbb{C}$ (take $a = \mathrm{diag}(z, 1, \dots, 1)$); for $k = 0$ this is false at $z = 0$; for $k, m \geq 1$, a primitive root of unity of order $k$ gives $z^m = 1$, so $k \mid m$, symmetrically ($\psi^{-1}$) $m \mid k$, so $k = m$. $\blacksquare$

Numerical check: `check_core_numbers.py`, `test_t174_a_int_corepresents_structures_and_the_old_receiving_map_fails` — the commutant of $\alpha_0(A_{\text{int}})$ in $M_7(\mathbb{C})$ has dimension 3; the numbers of faithful classes for $n = 1, \dots, 12$ are $0,0,0,0,0,0,1,1,1,3,3,3$, and $(1,1,1)$ occurs only at $n = 7$; $E$ is completely positive (Choi matrix $\geq 0$), keeps the trace against $A_{\text{int}}$, satisfies $E \circ \alpha_0 = \mathrm{id}$ and has a multiplicativity defect $> 1$ on random matrices; a random primitive Lindbladian on $\mathbb{C}^7$ has one stationary state and Heisenberg fixed points $\mathbb{C}1$; $H$ with simple spectrum commutes with none of the 12 off-diagonal matrix units, $H \in \mathrm{span}(P_0, P_1, P_2)$ commutes with all 19 generators; the $G_2$-orbit of a random state has dimension 14 in the 48-dimensional $\mathcal{D}(\mathbb{C}^7)$.

**What T-174 uses:** T-211 (the ∞-category and the form of its mapping spaces); Umegaki 1954, Takesaki 1972, Tomiyama 1957 (conditional expectations); the representation theory of finite-dimensional $C^*$-algebras; HTT Thm. 6.1.0.6 and §6.4.5 (only for the audit); T-39a (only for the remark on the UHM Liouvillian in (c)). **No longer used:** T-173 (rigidity is not needed, and does not give uniqueness of morphisms), T-53, T-60, T-42a, Stinespring, and the "subtopos of modules".

*Status history:* [T] from its introduction until 2026-09-26; audited 2026-09-26: the former statement and every step of its proof [✗] (items 1–8); restated as (a)–(e) [T].

### 4.5 Embedding Diagram {#схема-вложений}

```
     u0 = (A_int, trivial dynamics)  -- corepresents A_int-structures (T-174 a) --
        |                    |                       |
        | *-hom into A^sigma | unique up to U(7)     | E: tau-preserving expectation
        v                    v   iff n = 7, 8, 9     v   (UCP, not a *-hom; T-174 d)
   any theory x       M_n(C), n >= 7          states of x --> states of A_int

   spin networks (all j)  --Gamma_S-->  states of |V| heptads   [T-171]
   finite posets          --Gamma_C-->  states of |C| heptads   [T-172 a]
   finite posets          --pi* N-->    Segal objects of Sh(D(C^7)), fully faithful [T-172 b]
   M-theory on G2         :  Stab(phi_0) = Aut(O) = G2 [T-170 i];  Z_UHM = Z_M  [H]
```

---

## 5. Summary Table {#сводная-таблица}

| Theory | Map | Key mechanism | Status | Conditions |
|--------|-----|---------------|--------|------------|
| **M-theory** | none claimed (former $\mathcal{F}_M$ [✗]) | $\mathrm{Stab}_{GL(7)}(\varphi_0) = \mathrm{Aut}(\mathbb{O}) = G_2$ | **[T]** for T-170 (i)–(iii); correspondence **[H]** | $Z_M$ undefined perturbatively and non-perturbatively |
| **LQG** (all finite spin networks) | $\mathcal{S} \mapsto \Gamma_{\mathcal{S}}$, $M = \lvert V\rvert$ | spins and labels as ratios of coherences | **[T]** | — (T-171, T-171') |
| **Causal sets** (all finite posets) | $C \mapsto \Gamma_C$; $C \mapsto \pi^*N_\bullet C$ | ordered pair state; connectedness of $\mathcal{D}(\mathbb{C}^7)$ | **[T]** | — (T-172) |
| **Universal property** | $u_0 = (A_{\text{int}}, \mathrm{id})$ corepresents $A_{\text{int}}$-structures | universal $C^*$-algebra; multiplicity-free only at $n = 7$ | **[T]** | the former receiving map into UHM [✗] |

### 5.1 Honest Assessment

M-theory (Task 1): what is proved is the coincidence of the symmetry group — the stabiliser of the associative 3-form is $\mathrm{Aut}(\mathbb{O}) = G_2$ — together with finiteness of the UHM integral at finite $M$ on the torus $(S^1)^{21M}$ and existence of thermodynamic-limit states (T-170 (i)–(iii) [T]). The equality of partition functions is a hypothesis [H]: its M-theory side is not defined, the former moduli lemma is false, and the former functor is ill-typed. LQG (Task 2): every finite spin network, with unbounded spin, is encoded injectively in a state of $\lvert V\rvert$ holons with local decoding and restriction to induced subnetworks (T-171, T-171' [T]); the former state of Lemma C29' was not a density matrix and the cluster construction was false. Causal sets (Task 3): every finite poset is encoded in a state, and finite posets embed fully faithfully as internal categories of $\mathbf{Sh}_\infty(\mathcal{D}(\mathbb{C}^7))$ (T-172 [T]); the former "embedding of the nerve" collapses every poset with a least element to a point. Universal property (Task 4): the former receiving map into UHM does not exist as a $*$-homomorphism and is not unique as a monoid map; the property that holds is the corepresentation of $A_{\text{int}}$-structures by $u_0$, with rigidity exactly at $n = 7$, and the $\tau$-preserving conditional expectation as the map on states (T-174 [T]).

What is **proven [T]**:
1. $\mathrm{Stab}_{GL(7)}(\varphi_0) = \mathrm{Aut}(\mathbb{O}) = G_2$, the holonomy group of torsion-free $G_2$-structures (T-170 (i));
2. The chain $SU(2) \subset SU(3) \subset G_2$ with $\mathbf{7} \to \mathbf{1} \oplus \mathbf{3} \oplus \bar{\mathbf{3}}$ over $\mathbb{C}$ (T-171 (e));
3. Injective, locally decodable encodings of finite spin networks and finite posets in holonic states (T-171, T-172);
4. $u_0$ corepresents $A_{\text{int}}$-structures; the multiplicity-free faithful one exists only on $\mathbb{C}^7$ and is unique there up to $U(7)$ (T-174).

What is **not proven**:
1. $Z_{\text{UHM}} = Z_M$ at any level (T-170 (iv) [H]);
2. The specific form of Fano spin foam amplitudes and their semi-classical limit;
3. A universal property *into* UHM from every theory of a class — false as stated (T-174 (e)).

---

## 6. Results Registration {#регистрация}

| Theorem | Statement | Status | Conditions |
|---------|-----------|--------|------------|
| **T-170** | $G_2$ coincidence; finite-$M$ partition function; limit states; correspondence of partition functions | [T] for (i)–(iii); (iv) [H] | Lemma T-170'.1, T-170' as a theorem and $\mathcal{F}_M$ [✗] (2026-09-26) |
| **T-171** | Encoding of all finite spin networks in states of $\lvert V\rvert$ holons | [T] | — (restated 2026-09-26; former Lemma C29' [✗]) |
| **T-171'** | Unbounded spin | [T] | Corollary of T-171; cluster construction [✗] |
| **T-172** | Encoding of all finite posets; internal-category embedding into $\mathbf{Sh}_\infty(\mathcal{C})$ | [T] | — (restated 2026-09-26; nerve-as-object embedding [✗]) |
| **T-173** | Former universal primitive rigidity | [✗] | Specified-site construction [T]; dynamics and bridges are input (§4.3) |
| **T-174** | $u_0$ corepresents $A_{\text{int}}$-structures; rigidity at $n = 7$; dynamics criterion; $\tau$-preserving expectation on states | [T] | — (restated 2026-09-26; the former receiving map [✗]) |
| **C27-M** | Continuous Gap limit | [P] | Part of the hypothesis T-170 (iv) |
| **C28-M** | Supersymmetric extension | [P] | Part of the hypothesis T-170 (iv) |
| **C29'** | Spatial encoding (restated: all finite spin networks) | [T] | Lemma C29' = T-171 (a)–(c) |
| **C29** | Spatial limit for unbounded spin networks | [T] | Closed by T-171 (no bound on $j_e$) |
| **C30** | Causal encoding (restated: all finite posets, no $M^4$-embedding) | [T] | Lemma C30 = T-172 (a) |

---

## Links

- **Relies on:** [Spectral triple (T-53)](/docs/proofs/physics/physics-correspondence), [Emergent $M^4$ (T-117–T-121)](/docs/proofs/physics/emergent-manifold), [specified octonionic symmetry and conditional RI](/docs/proofs/categorical/uniqueness-theorem), [SUSY from $G_2$](/docs/physics/particle-physics/susy), [Gap functional integral](/docs/physics/gravity/quantum-gravity), [Sector decomposition](/docs/physics/gauge-symmetry/standard-model)
- **Justifies:** Meta-ToE status of UHM
- **Status registry:** T-170 — T-174, C27-M — C30 ([Registry](/docs/reference/status-registry))
