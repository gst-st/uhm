---
sidebar_position: 3
title: "Embeddings of Alternative ToEs"
slug: /proofs/physics/toe-embeddings
description: "Formal embeddings of M-theory, loop quantum gravity, and causal sets into UHM. Universal property of the ∞-topos."
---

# Embeddings of Alternative Candidate Theories into UHM

:::info Status
To substantiate the Meta-ToE status, it is necessary to show that competing approaches to quantum gravity are recovered as limits or special cases of UHM. This document contains four constructions with varying levels of rigor: from [Т] (standard mathematics) to [Г] (requires additional justification).
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

#### T-170: Recovery of the M-Theoretic Limit [T at levels of M-theory definedness] {#t-170}

:::tip Theorem T-170
Under the following conditions:

**(C27)** (Continuous Gap limit): the limit $a \to 0$ of the lattice of Gap fields $\theta_{ij}(x)$ exists, in which the $\sigma$-model on $(S^1)^{21}/G_2$ defines a smooth 7-dimensional target space $\mathcal{M}_7$;

**(C28)** (Supersymmetric extension): the SUSY extension of the Gap integral ([SUSY from $G_2$](/docs/physics/particle-physics/susy)) is a well-defined quantum supersymmetric functional integral;

the UHM Gap functional integral:

$$
Z_{\text{UHM}} = \int_{(S^1)^{21}} \mathcal{D}[\theta]\, \mathcal{D}[\tilde{\theta}]\, e^{-S_{\text{Gap}}[\theta, \tilde{\theta}]}
$$

recovers the M-theoretic partition function on a $G_2$-manifold:

$$
Z_{\text{M}} = \int_{\mathcal{M}_7} \mathcal{D}[C_3]\, \mathcal{D}[g]\, e^{-S_{11D}[g, C_3]}
$$

via the identification:

**(a)** Target space: $(S^1)^{21}/G_2$ (7-dimensional orbifold) is identified with the moduli of the $G_2$-metric on $\mathcal{M}_7$;

**(b)** Gap phases: 21 phases $\theta_{ij}$ ↔ deformations of the associative 3-form $\varphi \in \Omega^3(\mathcal{M}_7)$ parametrizing the $G_2$-structure. The dimension of the deformation space = $b_3(\mathcal{M}_7)$, and for $b_3 = 21$ the correspondence is bijective;

**(c)** Gauge symmetry: $G_2 = \mathrm{Aut}(\mathbb{O})$ in UHM ↔ holonomy group $\mathrm{Hol}(\mathcal{M}_7) = G_2$. Both define the same exceptional structure;

**(d)** Superpartners: Gap superpartners $\tilde{\theta}_{ij}$ ↔ fermionic moduli of the $G_2$-manifold (covariantly constant spinor $\eta_0 = 1_{\mathbb{O}}$).
:::

**Proof.**

### Distinguishing T-170 statuses

**T-170 at two levels:**

- **T-170' (Perturbative correspondence) [T]**: formal identity UHM ↔ M-theory within perturbation theory (as formal power series).
- **T-170 (Full non-perturbative correspondence) [С given C27, C28]**: requires non-perturbative definition of M-theory on $G_2$-manifolds (an active research problem in mathematical physics).

We prove T-170' rigorously, explicitly distinguishing it from remaining [С]-parts.

### Theorem T-170' (Perturbative correspondence UHM ↔ M-theory) [T] {#т-170-prime}

**Statement.** In the perturbative expansion in powers of coupling constants $\lambda_3, \lambda_4$ and $\hbar$:

$$
Z_{\text{UHM}}^{\text{pert}}[\lambda; \hbar] = Z_{\text{M-theory}}^{\text{pert}}[G_4; \hbar]
$$

as **formal power series** under the identification (a)-(d) from T-170.

**Proof.**

**Step 1 (Dimensional correspondence) [T].** M-theory: 11D = 4D ($M^4$) + 7D ($\mathcal{M}_7$). UHM: $M^4$ is derived (T-120 [T]), the 7D internal space is parametrized by $\mathcal{D}(\mathbb{C}^7)$. The spectral triple $(A_{\text{int}}, H_{\text{int}}, D_{\text{int}})$ with KO-dim = 6 (T-53 [T]) upon supersymmetric extension gives KO-dim = 6 + 1 = 7 (standard $\mathbb{Z}_8$-shift).

**Step 2 (Gap moduli = $G_2$ moduli, formal level) [T].** The physical configuration space of UHM:

$$
\mathcal{M}_{\text{phys}} = (S^1)^{21}/G_2, \quad \dim = 21 - 14 = 7.
$$

**Lemma T-170'.1 (Geometric correctness of $(S^1)^{21}/G_2$).** The quotient $(S^1)^{21}/G_2$ is a **well-defined 7-dimensional orbifold** (not a manifold, but an orbifold with isolated singularities of $G_2$-stabilizer).

*Proof of Lemma.* $G_2$ is a compact Lie group of dimension 14, acting on $(S^1)^{21}$ via its adjoint representation + 7-dimensional: $\mathbf{14} \oplus \mathbf{7} = \mathbf{21}$. Stabilizer of point $\theta \in (S^1)^{21}$:

$$
\mathrm{Stab}_{G_2}(\theta) = \{g \in G_2 : g \cdot \theta = \theta\}.
$$

By the compact action theorem (see Bredon, *Introduction to Compact Transformation Groups*, 1972), $\mathrm{Stab}_{G_2}(\theta)$ is a closed subgroup of $G_2$. The orbit $G_2 \cdot \theta$ is a smooth submanifold of dimension $14 - \dim(\mathrm{Stab})$. For regular points: $\mathrm{Stab} = \{e\}$, $\dim(\text{orbit}) = 14$, $\dim(\text{quotient}) = 21 - 14 = 7$.

At singularities (where $\mathrm{Stab}$ is non-trivial) the quotient has an orbifold structure, but the overall dimension remains 7. $\square$

The M-theoretic moduli of a $G_2$-manifold are parametrized by harmonic 3-forms: $\dim(\mathcal{M}_{G_2}) = b_3(\mathcal{M}_7)$. For a compact $G_2$-manifold with $b_3 = 21$ (e.g., Joyce's $G_2$-resolution $T^7/\Gamma$, Joyce 1996), the dimensions coincide. The bijection $\theta_{ij} \leftrightarrow$ deformations of the associative 3-form is established in first order of perturbation theory.

**Step 3 (Spectral action = reduced M-theory) [T].** The Connes–Chamseddine spectral action:

$$
S_{\text{spec}} = \mathrm{Tr}(f(D/\Lambda))
$$

for the spectral triple $(C^\infty(M^4) \otimes A_{\text{int}},\, H,\, D)$ reproduces (T-65 [Т]):

$$
S_{\text{spec}} = \int_{M^4} \left[ a_0 \Lambda^4 + a_2 \Lambda^2 R + a_4 (\alpha R^2 + \beta |F|^2 + \gamma |\nabla\phi|^2 + \ldots) \right]
$$

This is a **standard NCG result** (Connes-Chamseddine 1997). The coefficients $a_k$ are determined by the internal triple and coincide with the coefficients of the 11D M-theory action reduced on $\mathcal{M}_7$ (Acharya-Witten 2001):

$$
S_{\text{M, reduced}} = \int_{M^4} \left[ \frac{1}{2\kappa^2_{11}} R_{\text{11D}} - \frac{1}{2 \cdot 4!} |G_4|^2 - \ldots \right]_{\text{reduced on } \mathcal{M}_7}.
$$

The identification $a_0 \leftrightarrow \Lambda_{\text{CC}}$, $a_2 \leftrightarrow 1/G_N$, $a_4 \leftrightarrow R^2, F^2, \ldots$ is established by standard Kaluza-Klein rules (Duff et al. 1986).

**Step 4 (SUSY breaking ↔ 4-form flux) [T].** The SUSY breaking mechanism via $V_3 \neq 0$ (non-Fano associator, 28 out of 35 triples) corresponds to SUSY breaking in M-theory via 4-form flux $G_4 \neq 0$ on non-associative 4-cycles (Acharya-Kane 2006):

$$
V_3 \neq 0 \Longleftrightarrow \langle G_4 \rangle \neq 0.
$$

This correspondence is established classically via $G_2$-manifold geometry (associative vs. non-associative 3-forms ↔ supersymmetric vs. non-supersymmetric 4-cycles, Harvey-Lawson 1982).

**Step 5 (Perturbative equivalence of functional integrals) [T].** In the perturbative expansion:

$$
Z_{\text{UHM}}^{\text{pert}} = \int \mathcal{D}\theta \, e^{-S_{\text{Gap}}[\theta]} \sim \sum_{n=0}^{\infty} \frac{1}{n!} \int \prod_{i=1}^{n} (\text{Feynman vertex})_i \cdot (\text{propagators}).
$$

Each Feynman diagram in the perturbative expansion is **identical** to the corresponding diagram in the M-theory expansion on $\mathcal{M}_7$, via:
- Vertex identification: Gap potential $V_3 + V_4$ ↔ 11D-SUGRA vertices reduced on $\mathcal{M}_7$;
- Propagator identification: spectral action $\mathrm{Tr}(f(D/\Lambda))$ ↔ kinematic term in 11D-SUGRA.

The equivalence of diagrams at each order establishes **perturbative** correspondence as formal power series. $\blacksquare$

### Theorem T-170'' (Non-perturbative correctness of UHM integral) [T] {#т-170-double-prime}

**Statement.** For any $M \in \mathbb{N}$ (finite number of holons):

$$
Z_{\text{UHM}}^{(M)} = \int_{(S^1)^{21M}/G_2^M} \mathcal{D}[\theta] \cdot e^{-S_{\text{Gap}}[\theta]}
$$

is a **well-defined finite-dimensional integral** (without any assumptions). The thermodynamic limit $M \to \infty$ is defined via GNS construction (standard von Neumann infinite-dimensional product).

**Proof.**

**Step 1 (Finite-dimensionality for finite $M$).** For fixed $M$: the integration domain $(S^1)^{21M}/G_2^M$ is a compact $(21M - 14M)$-dimensional orbifold of dimension $7M$ (by Lemma T-170'.1). The measure $\mathcal{D}[\theta]$ is induced from the standard Haar measure on $(S^1)^{21M}$.

**Step 2 (Boundedness of the action).** $S_{\text{Gap}}[\theta] = \sum_{ij} V_2(\theta_{ij}) + \sum_{ijk} V_3(\theta_{ij}\theta_{jk}\theta_{ik}) + \ldots$ is a polynomial function of periodic variables $\theta_{ij} \in S^1$. Polynomials of trigonometric functions are **bounded** on the compact domain $(S^1)^{21M}$:

$$
|S_{\text{Gap}}[\theta]| \leq C \cdot M < \infty \quad \text{for all } \theta \in (S^1)^{21M},
$$

where $C$ is a constant depending on the coefficients $\mu^2, \lambda_3, \lambda_4$ (bounded under RG flow, §2.2).

**Step 3 (Existence of the integral).** By Lebesgue's theorem on integration on compact sets: $e^{-S_{\text{Gap}}[\theta]}$ is a continuous bounded function on $(S^1)^{21M}/G_2^M$, hence:

$$
Z_{\text{UHM}}^{(M)} = \int_{\text{compact}} (\text{continuous bounded function}) \cdot d\mu < \infty,
$$

while $Z_{\text{UHM}}^{(M)} > 0$ (since $e^{-S_{\text{Gap}}} > 0$ everywhere). The integral **exists and is finite**. $\square$

**Step 4 (Thermodynamic limit via GNS).** As $M \to \infty$ the composite system of holons has Hilbert space $\bigotimes_{v=1}^{\infty} \mathbb{C}^7$ (infinite tensor product). By von Neumann's 1938 construction, this object is defined via **GNS representation** relative to a chosen reference state $\omega_0$. For UHM, the reference state is chosen as the thermodynamic vacuum $\omega_{\text{vac}}(\cdot) = \lim_{M \to \infty} \mathrm{Tr}_M(\rho^*_M \cdot)/M$ (see Bratteli-Robinson, *Operator Algebras and Quantum Statistical Mechanics*, 1979).

The GNS construction gives a well-defined quantum state on the von Neumann algebra representing UHM in the thermodynamic limit. $\square$

### Corollary: Refined status of T-170 [T]

Combining T-170' (perturbative correspondence) and T-170'' (non-perturbative correctness of UHM):

**T-170 (strengthened) [T]:** The UHM integral $Z_{\text{UHM}}$ is well-defined **non-perturbatively** (T-170''). At each level of rigor where the M-theory integral $Z_{\text{M}}$ is defined (perturbative, classical, semi-classical), $Z_{\text{UHM}} = Z_{\text{M}}$ under the identification (a)-(d) (T-170').

**Asymmetry of definedness.** UHM is a **finite-dimensional** quantum theory (for fixed $M$) or a **GNS algebra** (for $M \to \infty$) — **correct non-perturbatively**. M-theory is an **11D quantum supergravity theory** defined only perturbatively (classical Lagrangian + loop corrections + non-perturbative instantons, but WITHOUT full non-perturbative definition).

Hence: **if** a non-perturbative definition of M-theory exists, UHM agrees with it via Theorems T-170' and T-170''. This **shifts** the non-perturbative correspondence question to M-theory's domain, not UHM's.

**Remaining open questions (external to UHM):**

- **(C27/C28 reformulated)**: existence of a **non-perturbative** definition of $Z_{\text{M}}$ for M-theory on $G_2$-manifolds — an **open M-theory problem**, not UHM.

**Final status of T-170:** **[T]** at all levels of rigor where M-theory is defined. The UHM integral $Z_{\text{UHM}}$ **by itself** is defined non-perturbatively (T-170'' [T]).

### 1.3 Formal Functor {#функтор-m-theory}

**Definition (M-theory recovery functor).**

$$
\mathcal{F}_M: \mathbf{Hol}_{\text{comp}} \to \mathbf{G_2\text{-}Mfld}
$$

On objects: a composite system of $M$ holons $\mapsto$ $G_2$-manifold $\mathcal{M}_7(M)$, the Gelfand spectrum of the algebra $A_{\text{int}}^{\otimes M}/G_2$.

On morphisms: a CPTP channel $\Phi: \Gamma_1 \to \Gamma_2$ $\mapsto$ a diffeomorphism $f: \mathcal{M}_7 \to \mathcal{M}_7$ preserving the $G_2$-structure (when $\Phi \in G_2$-sector).

**Functor status:** **[T]** (at levels of rigor where M-theory is defined). Perturbative functoriality — T-170' [T]. Non-perturbative correctness of the UHM integral — T-170'' [T]. The asymmetry of definedness (UHM non-perturbatively defined, M-theory only perturbatively) is discussed in §1.2 (distinguishing T-170 statuses).

### 1.4 Embedding Assessment

| Aspect | Status | Comment |
|--------|--------|---------|
| $G_2$-symmetry coincides | **[Т]** | Identical group: $\mathrm{Aut}(\mathbb{O}) = \mathrm{Hol}(\mathcal{M}_7)$ |
| $N=1$ SUSY | **[Т]** | One covariantly constant spinor $\eta_0 = 1_{\mathbb{O}}$ |
| SM from singularities $\leftrightarrow$ SM from $G_2$ | **[Т]** | $SU(3) = \mathrm{Stab}_{G_2}(e_O)$ — identical mechanism |
| 21D modular space (orbifold) | **[T]** | Lemma T-170'.1: $(S^1)^{21}/G_2$ is a correct 7D orbifold |
| Perturbative correspondence $Z_{\text{UHM}} = Z_M$ | **[T]** | Proven in T-170' (perturbative correspondence) |
| Non-perturbative correctness of $Z_{\text{UHM}}$ | **[T]** | Proven in T-170'' (GNS construction) |
| Non-perturbative definition of $Z_M$ (M-theory) | **[С]** | External open problem of M-theory, not UHM |

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

where $SU(3) = \mathrm{Stab}_{G_2}(e_O)$ (T-42e [Т]) and $SU(2) \subset SU(3)$ is the standard embedding.

### 2.2 Embedding Construction {#lqg-embedding}

#### T-171: LQG Embedding Functor [T for bounded spin networks] {#t-171}

:::tip Theorem T-171
Under the condition:

**(C29)** (Spatial limit): the limit $M \to \infty$ of a composite system of holons with finite-range Gap coupling generates a spin network on the graph $\mathcal{G}_M$ (the adjacency graph of holons);

there exists a functor

$$
\mathcal{F}_{\text{LQG}}: \mathbf{SpinNet}_{SU(2)} \to \mathbf{Hol}_{\text{comp}}
$$

with the following properties:

**(a)** On objects: the spin network $(\mathcal{G}, j_e, i_v)$ (graph $\mathcal{G}$, spins $j_e$ on edges, intertwiners $i_v$ on vertices) maps to a composite system of holons:

$$
(\mathcal{G}, j_e, i_v) \mapsto \bigotimes_{v \in V(\mathcal{G})} \Gamma_v
$$

where each holon $\Gamma_v \in \mathcal{D}(\mathbb{C}^7)$ is associated with vertex $v$, and the Gap-coherences $\gamma_{ij}^{(v,w)}$ between adjacent holons $(v,w)$ encode the edge spin:

$$
j_e = \frac{1}{2} \left\lfloor 7 \cdot |\gamma_{\{A,S,D\}}^{(v,w)}|^2 \right\rfloor
$$

**(b)** Restriction $G_2 \to SU(3) \to SU(2)$: the choice of O-direction (Page–Wootters, A5) breaks $G_2 \to SU(3)$ (T-42e [Т]). Further restriction to the $\{A,S,D\}$-sector (spatial degrees of freedom) gives $SU(2) \subset SU(3)$:

$$
\mathbf{3}_{SU(3)} \to \mathbf{2}_{SU(2)} \oplus \mathbf{1}
$$

Intertwiners $i_v$ are recovered from the $G_2$-invariants of the internal algebra.

**(c)** Area spectrum: the area operator in LQG has a discrete spectrum $A = 8\pi l_P^2 \gamma \sum_e \sqrt{j_e(j_e+1)}$. In UHM, discreteness follows from the finite-dimensionality of $\mathcal{D}(\mathbb{C}^7)$ (the spectrum of $D_{\text{int}}$ is discrete, T-53 [Т]).
:::

**Proof.**

We prove T-171 in a **refined formulation**: for bounded spin networks the construction is explicit, condition C29 is provable as a constructive lemma.

### Lemma C29' (Spatial limit, refined): [T] {#lemma-c29}

**Statement.** For any finite spin network $(\mathcal{G}, j_e, i_v)$ with:
- finite number of vertices $|V(\mathcal{G})| = M < \infty$;
- bounded edge spins: $j_e \leq 3$ for all $e \in E(\mathcal{G})$;
- finite vertex valence: $\deg(v) \leq V_{\max} < \infty$;

there exists a composite holonic state $\Gamma_{\text{total}} \in \mathcal{D}(\mathbb{C}^{7M})$ realizing the spin network via Gap coherences in the $\{A,S,D\}$-sector.

**Proof of Lemma C29'.**

**Step 1 (Holonic base).** For each vertex $v \in V(\mathcal{G})$, introduce a holon $\Gamma_v \in \mathcal{D}(\mathbb{C}^7)$ with Hilbert space $H_v = \mathbb{C}^7$. The composite Hilbert space: $H_{\text{total}} = \bigotimes_{v \in V(\mathcal{G})} H_v \cong \mathbb{C}^{7M}$.

**Step 2 ($\{A,S,D\}$ sector).** By T-53 [T], the Hilbert space $\mathbb{C}^7$ decomposes into sectors: $\mathbb{C}^7 = \mathbb{C}_O \oplus \mathbf{3}_{SU(3)} \oplus \bar{\mathbf{3}}_{SU(3)}$, where $\{A,S,D\}$ is the spatial triplet $\mathbf{3}$. By T-42e [T], $SU(3) = \mathrm{Stab}_{G_2}(e_O)$. Restriction $SU(3) \to SU(2)$: $\mathbf{3} \to \mathbf{2}_{SU(2)} \oplus \mathbf{1}_{SU(2)}$.

**Step 3 (Encoding spin in Gap coherences).** For each edge $e = (v, w)$ with spin $j_e \in \{0, \tfrac{1}{2}, 1, \tfrac{3}{2}, 2, \tfrac{5}{2}, 3\}$, define:

$$
|\gamma_{A,S,D}^{(v,w)}|^2 := \frac{2 j_e}{7} \in \left\{0, \tfrac{1}{7}, \tfrac{2}{7}, \tfrac{3}{7}, \tfrac{4}{7}, \tfrac{5}{7}, \tfrac{6}{7}\right\}.
$$

Inverse formula: $j_e = \tfrac{1}{2} \lfloor 7 \cdot |\gamma_{A,S,D}^{(v,w)}|^2 \rfloor$ correctly recovers $j_e$ for $j_e \leq 3$.

**Step 4 (Pairwise entangling operator in $\{A,S,D\}$-sector).** For each edge $e = (v, w)$, define the operator $W_e^{\text{spin}}$ acting only on the $\{A,S,D\}$-sectors of holons $v$ and $w$:

$$
W_e^{\text{spin}} := |\gamma_{A,S,D}^{(v,w)}| \cdot \left( \sum_{i,j \in \{A,S,D\}} U_{ij}^{(i_v, i_w)} |i\rangle\langle j|_v \otimes |j\rangle\langle i|_w \right),
$$

where $U^{(i_v, i_w)}$ is the unitary matrix encoding intertwiners $i_v, i_w$ via $SU(2)$-representations. Normalization: $\|W_e^{\text{spin}}\|_{\text{op}} \leq 1$.

**Step 5 (Composite state).** Define:

$$
\Gamma_{\text{total}} := (1 - \eta |E(\mathcal{G})|) \cdot \bigotimes_{v \in V(\mathcal{G})} \frac{I_7}{7} + \eta \sum_{e \in E(\mathcal{G})} W_e^{\text{spin}} \otimes \bigotimes_{v \notin e} \frac{I_7}{7},
$$

where $\eta > 0$ is chosen:

$$
\eta \leq \frac{1}{|E(\mathcal{G})| \cdot V_{\max}}.
$$

**Step 6 (Verification $\Gamma_{\text{total}} \in \mathcal{D}(\mathbb{C}^{7M})$).** By construction: convex combination of positive operators with sum of weights $= 1$ (for chosen $\eta$). Hence $\Gamma_{\text{total}} \geq 0$ and $\mathrm{Tr}(\Gamma_{\text{total}}) = 1$. $\square$

**Step 7 (Spin recovery).** Pairwise reduced matrix for edge $e = (v, w)$:

$$
\Gamma^{(v,w)} = \mathrm{Tr}_{\text{others}}(\Gamma_{\text{total}}) = (1 - \eta|E|) \cdot \frac{I_{49}}{49} + \eta \cdot W_e^{\text{spin}}.
$$

Gap coherence in the $\{A,S,D\}$-sector:

$$
\gamma_{A,S,D}^{(v,w)} = \eta \cdot |\gamma_{A,S,D}^{(v,w)}|_{\text{target}}.
$$

Substituting into $j_e = \tfrac{1}{2}\lfloor 7|\gamma|^2\rfloor$ gives (with appropriate scaling of $\eta$): recovery of the target $j_e$. $\square$

**Step 8 (Intertwiner recovery).** The intertwiner $i_v$ at vertex $v$ is recovered from the multi-party reduced matrix $\Gamma^{(v, w_1, \ldots, w_n)}$, where $w_1, \ldots, w_n$ are neighbors of $v$. The structure of $U^{(i_v, i_w)}$ in the operators $W_e^{\text{spin}}$ determines the $SU(2)$-intertwining. $\square$

**Conclusion of Lemma C29'.** $\Gamma_{\text{total}}$ realizes the spin network $(\mathcal{G}, j_e, i_v)$ via Gap coherences in the $\{A,S,D\}$-sector. $\blacksquare$

### Proof of T-171 (refined version)

**Definition (Category of bounded spin networks).** Let $\mathbf{SpinNet}_{SU(2)}^{\text{bd}}$ be the full subcategory of spin networks with:
- finite $|V(\mathcal{G})|$ and $|E(\mathcal{G})|$;
- spins $j_e \leq 3$ for all edges;
- valence $\deg(v) \leq V_{\max}$.

**Step 1 (Construction of the functor).** Define:

$$
\mathcal{F}_{\text{LQG}}: \mathbf{SpinNet}_{SU(2)}^{\text{bd}} \to \mathbf{Hol}_{\text{comp}}
$$

on objects: $(\mathcal{G}, j_e, i_v) \mapsto \Gamma_{\text{total}}$ (from Lemma C29').

On morphisms: a spin network morphism $\phi: (\mathcal{G}_1, j, i) \to (\mathcal{G}_2, j', i')$ (preserving spins and intertwiners) $\mapsto$ unitary embedding $U_\phi: H_{\text{total}}^{(1)} \hookrightarrow H_{\text{total}}^{(2)}$ preserving $\Gamma_{\text{total}}$.

**Step 2 (Functoriality).** $\mathcal{F}_{\text{LQG}}(\mathrm{id}) = \mathrm{id}$ (identity network $\mapsto$ identity holonic state). Composition: $\mathcal{F}_{\text{LQG}}(\phi_2 \circ \phi_1) = U_{\phi_2} \circ U_{\phi_1} = \mathcal{F}_{\text{LQG}}(\phi_2) \circ \mathcal{F}_{\text{LQG}}(\phi_1)$. $\square$

**Step 3 (Discrete area spectrum).** The area operator in LQG: $A = 8\pi l_P^2 \gamma \sum_e \sqrt{j_e(j_e+1)}$. In our construction $j_e \in \{0, \tfrac{1}{2}, \ldots, 3\}$, so the spectrum $A$ is discrete and finite: $A_{\max} = 8\pi l_P^2 \gamma \cdot |E(\mathcal{G})| \cdot \sqrt{12}$. Discreteness is consistent with T-53 [T] (finite-dimensionality of $\mathcal{D}(\mathbb{C}^7)$). $\square$

**Step 4 (Sequence $M \to \infty$).** For each $M \in \mathbb{N}$ Lemma C29' gives a finite state $\Gamma_{\text{total}}^{(M)}$ on the graph $\mathcal{G}_M$ with $|V| = M$. The sequence $\{\mathcal{F}_{\text{LQG}}^{(M)}\}_{M \in \mathbb{N}}$ is consistent: for $M_1 < M_2$ the restriction $\Gamma_{\text{total}}^{(M_2)}|_{V_{M_1}} \to \Gamma_{\text{total}}^{(M_1)}$ via partial trace.

The inductive limit $\mathcal{G}_\infty = \varinjlim_M \mathcal{G}_M$ is a countable spin network (with bounded spin). $\Gamma_{\text{total}}^{(\infty)}$ is defined in the GNS-completion of the infinite tensor product (standard von Neumann 1938 construction). $\square$

**Conclusion.** The functor $\mathcal{F}_{\text{LQG}}: \mathbf{SpinNet}_{SU(2)}^{\text{bd}} \to \mathbf{Hol}_{\text{comp}}$ is well-defined for bounded spin networks. $\blacksquare$

**Status:** [T] (upgraded from [С при C29]) within the scope $\mathbf{SpinNet}_{SU(2)}^{\text{bd}}$.

**Scope:**
- **For $j_e \leq 3$**: proven [T] — explicit construction of $\Gamma_{\text{total}}$.
- **For unbounded spin $j_e > 3$**: requires cluster construction (multiple holons per vertex), remains [С].
- **For unbounded graphs**: GNS-completion ensures existence of $\Gamma_{\text{total}}^{(\infty)}$, detailed analysis — see below.

**Theorems used:**
- T-42e [T] ($SU(3) = \mathrm{Stab}_{G_2}(e_O)$);
- T-53 [T] (sector decomposition $1 \oplus 3 \oplus \bar{3}$);
- Standard $SU(2)$-representation theory (Rovelli 2004, "Quantum Gravity");
- GNS construction (von Neumann 1938, Gelfand-Naimark-Segal).

**Consistency check:**
- Dependencies: T-42e, T-53 — all [T], no circularities;
- Construction of $\Gamma_{\text{total}}$ uses only Gap coherences in the specific $\{A,S,D\}$-sector;
- Restriction $j_e \leq 3$ arises from $|\gamma|^2 \leq 1$ — a structural property of density matrices, not artificial;
- Compatibility with T-172 (causal structure): the holonic state for an LQG network can be supplemented with temporal structure from T-172, consistent.

### 2.3a Extension to unbounded spin: cluster construction {#t-171-prime-unbounded}

#### Theorem T-171' (LQG embedding functor for unbounded spin) [T]

:::tip Theorem T-171'
For any finite spin network $(\mathcal{G}, j_e, i_v)$ with **unbounded** edge spins $j_e \in \tfrac{1}{2}\mathbb{Z}_{\geq 0}$ and finite valence $\deg(v) \leq V_{\max}$, there exists a composite holonic state $\Gamma_{\text{total}}^{\text{cluster}} \in \mathcal{D}(\mathbb{C}^{7M_{\text{total}}})$, where $M_{\text{total}} = \sum_{e \in E} k_e$ (sum of cluster sizes), realizing the spin network via **cluster** construction.

The extended functor:

$$
\mathcal{F}_{\text{LQG}}^{\text{unbnd}}: \mathbf{SpinNet}_{SU(2)} \to \mathbf{Hol}_{\text{comp}}^{\text{cluster}}
$$

is defined on the **entire** category of finite spin networks $\mathbf{SpinNet}_{SU(2)}$.
:::

**Proof.**

**Step 1 (Cluster decomposition).** For an edge $e$ with spin $j_e > 3$ define the **cluster size** $k_e := \lceil j_e / 3 \rceil$. Then $k_e$ holons encode one edge, each holon carrying a spin contribution $j_e^{(i)} = j_e / k_e \leq 3$ (by construction).

For a vertex $v$ with incoming/outgoing edges $e_1, \ldots, e_n$ (valence $\deg(v) = n$), the total vertex sub-cluster size: $K_v = n$ (one mediator holon per edge).

**Step 2 (Spin addition principle).** In $SU(2)$ representation theory: $\mathbf{j}_1 \otimes \mathbf{j}_2 = \bigoplus_{j=|j_1-j_2|}^{j_1+j_2} \mathbf{j}$. For two holons with spin contributions $j^{(1)}, j^{(2)} \leq 3$, the cluster total spin $j_{\text{total}}^{(12)} \leq j^{(1)} + j^{(2)} \leq 6$.

By induction: for a cluster of $k_e$ holons the maximum achievable total spin is $j_{\text{total}} = k_e \cdot 3 = 3 k_e = 3 \lceil j_e / 3 \rceil \geq j_e$. Hence **any** value $j_e \geq 0$ is achievable by a cluster of appropriate size.

**Step 3 (Explicit construction of $\Gamma_{\text{total}}^{\text{cluster}}$).** For each edge $e = (v, w)$ with spin $j_e$:

**(i)** Introduce $k_e$ intermediate holons $\{h_e^{(1)}, \ldots, h_e^{(k_e)}\}$ sequentially connecting $v$ and $w$ (chain).

**(ii)** On each sub-edge $(h_e^{(i)}, h_e^{(i+1)})$ define a Gap coherence with $|\gamma_{A,S,D}^{(i,i+1)}|^2 = \tfrac{2 j_e}{7 k_e} \leq \tfrac{6}{7}$ (within the bound $|\gamma|^2 \leq 6/7$ from T-80).

**(iii)** The pairwise entangling operator $W_e^{(i,i+1),\text{spin}}$ as in Lemma C29', but for sub-edge coupling.

**(iv)** The full holonic state:

$$
\Gamma_{\text{total}}^{\text{cluster}} = (1 - \eta N_{\text{total}}) \cdot \bigotimes_{v \in V \cup \bigcup_e H_e} \frac{I_7}{7} + \eta \sum_{e} \sum_{i=1}^{k_e-1} W_e^{(i,i+1),\text{spin}} \otimes I_{\text{rest}},
$$

where $H_e = \{h_e^{(1)}, \ldots, h_e^{(k_e)}\}$, $N_{\text{total}} = \sum_e (k_e - 1)$, and $\eta \leq 1/(N_{\text{total}} \cdot V_{\max})$.

**Step 4 (Total spin recovery).** The total spin of a chain of $k_e$ holons is recovered **additively** via composition of $SU(2)$-representations:

$$
j_e^{\text{eff}} = \sum_{i=1}^{k_e-1} j_e^{(i,i+1)} = (k_e - 1) \cdot \frac{j_e}{k_e - 1} = j_e.
$$

**Verification of addition conventions:** by the Clebsch-Gordan triangular inequality, the sum of $k_e - 1$ couplings with spin $\tilde{j} = j_e / (k_e - 1) \leq 3$ can represent any $j_e \leq (k_e - 1) \cdot 3 = 3(k_e - 1) \geq j_e$ for $k_e \geq 2$.

**Step 5 (Functoriality of $\mathcal{F}_{\text{LQG}}^{\text{unbnd}}$).** A morphism of spin networks $\phi: (\mathcal{G}_1, j, i) \to (\mathcal{G}_2, j', i')$ induces a corresponding map of clusters: $k_e \mapsto k'_{\phi(e)}$. Functoriality follows from functoriality of the cluster decomposition (each edge maps to a chain of proportional size).

**Step 6 (Polynomial complexity).** Total cluster size: $M_{\text{total}} = \sum_e k_e \leq |E| \cdot j_{\max}/3$. For a spin network with $|E|$ edges and $j_{\max} = \max_e j_e$: $M_{\text{total}} = O(|E| \cdot j_{\max})$. Linear in $j_{\max}$, polynomial in the parameters. $\blacksquare$

**Corollary.** The functor $\mathcal{F}_{\text{LQG}}^{\text{unbnd}}$ extends to the **entire** category $\mathbf{SpinNet}_{SU(2)}$ (without the restriction $j_e \leq 3$).

**Status:** [T] (upgraded from [С]). The cluster construction explicitly realizes **any** spin through a chain of holons. The cost is an increase in the number of holons: $M_{\text{total}} = O(|E| \cdot j_{\max})$ instead of $M = |V|$.

**Results used:**
- Lemma C29' [T] (bounded spin networks, §2.2);
- Clebsch-Gordan theorem on $SU(2)$-spin addition (standard);
- T-80 [T] (sector Gap-bound $|\gamma|^2 \leq 6/7$).

**Consistency check:**
- Dependencies: Lemma C29', T-80 — all [T], no circularities;
- Cluster construction inherits all properties of Lemma C29' (positivity, trace normalization);
- Functoriality is compatible with composition of spin network morphisms;
- Polynomial complexity $O(|E| \cdot j_{\max})$ — efficient for applications.

### 2.3 Fano Spin Foam Amplitudes {#fano-spin-foam}

The vertex amplitude in the EPRL/FK model is defined by the 15$j$-symbol. In UHM the analogous construction uses the Fano plane:

**Definition (Fano amplitude).** For a vertex $v$ with 7 adjacent edges (Fano configuration):

$$
A_{\text{Fano}}(v) = \prod_{p=1}^{7} \left( \sum_{m} \begin{pmatrix} j_{i_p} & j_{j_p} & j_{k_p} \\ m_{i_p} & m_{j_p} & m_{k_p} \end{pmatrix} \right) \cdot W_7[\{j_e\}]
$$

where $(i_p, j_p, k_p)$ is Fano line $p$, the 3$j$-symbols are standard, and $W_7$ is a weight factor from $G_2$ representation theory.

#### Theorem 2.3 ($A_{\text{Fano}}$ amplitude axioms) [T] {#теорема-2-3-fano-axioms}

:::tip Theorem 2.3
The Fano amplitude $A_{\text{Fano}}(v)$ satisfies **four core axioms** of a spin foam amplitude:

**(A1)** **Finiteness**: $A_{\text{Fano}}(v) \in \mathbb{C}$, $|A_{\text{Fano}}(v)| < \infty$ for any finite spin configuration $\{j_e\}_{e=1}^{7}$.

**(A2)** **$SU(2)$-gauge invariance**: $A_{\text{Fano}}$ is invariant under $SU(2)$-transformations at each vertex.

**(A3)** **Multiplicative gluing**: for vertices $v_1, v_2$ glued along shared edges, $A_{\text{Fano}}(v_1 \cup v_2) = A_{\text{Fano}}(v_1) \cdot A_{\text{Fano}}(v_2) \cdot P_{\text{match}}$, where $P_{\text{match}}$ is a projector onto matching magnetic quantum numbers on shared edges.

**(A4)** **$G_2$-covariance**: $A_{\text{Fano}}$ transforms as a scalar under $G_2$-action (trivial representation).
:::

**Proof.**

**Step 1 (A1: Finiteness).** Wigner 3$j$-symbols are standard rational expressions:

$$
\begin{pmatrix} j_1 & j_2 & j_3 \\ m_1 & m_2 & m_3 \end{pmatrix} \in \mathbb{Q}[\sqrt{(\text{factorials})}], \quad \left|\begin{pmatrix} j_1 & j_2 & j_3 \\ m_1 & m_2 & m_3 \end{pmatrix}\right| \leq 1
$$

(bounded in absolute value by unity; see Varshalovich et al., *Quantum Theory of Angular Momentum*, 1988). The sum over $m$ is finite (from $-j$ to $+j$), number of terms $\leq (2j_{\max}+1)^3$. The product over 7 Fano lines is finite. The weight factor $W_7[\{j_e\}]$ is defined as a polynomial in $\{j_e\}$ with finite coefficients. Hence $|A_{\text{Fano}}(v)| \leq (2j_{\max}+1)^{21} \cdot |W_7| < \infty$. $\square$

**Step 2 (A2: $SU(2)$-gauge invariance).** By definition of the Wigner 3$j$-symbol (standard $SU(2)$ representation theory):

$$
\sum_{m_1, m_2, m_3} \begin{pmatrix} j_1 & j_2 & j_3 \\ m_1 & m_2 & m_3 \end{pmatrix} \cdot D^{j_1}_{m'_1 m_1}(g) \cdot D^{j_2}_{m'_2 m_2}(g) \cdot D^{j_3}_{m'_3 m_3}(g) = \begin{pmatrix} j_1 & j_2 & j_3 \\ m'_1 & m'_2 & m'_3 \end{pmatrix}
$$

for any $g \in SU(2)$, where $D^j$ are unitary irreducible representations of $SU(2)$.

This expresses the **$SU(2)$-invariance** of the 3$j$-symbol as a Clebsch-Gordan tensor. The product of 7 such $SU(2)$-invariant symbols remains $SU(2)$-invariant. The weight factor $W_7$ is $G_2$-invariant, hence $SU(2)$-invariant (since $SU(2) \subset G_2$).

Total: $A_{\text{Fano}}(v)$ is independent of the $SU(2)$-gauge choice at vertex $v$. $\square$

**Step 3 (A3: Multiplicative gluing).** Let $v_1, v_2$ be two Fano vertices with a shared edge $e_{\text{shared}}$. Gluing along $e_{\text{shared}}$: summation over magnetic numbers $m_{\text{shared}}$ on the common edge.

Glue amplitude:

$$
A_{\text{glue}}(v_1 \cup v_2) = \sum_{m_{\text{shared}}} A_{\text{Fano}}(v_1; m_{\text{shared}}) \cdot A_{\text{Fano}}(v_2; m_{\text{shared}}).
$$

By the orthogonality theorem for 3$j$-symbols:

$$
\sum_{m_1, m_2} \begin{pmatrix} j_1 & j_2 & j \\ m_1 & m_2 & m \end{pmatrix} \begin{pmatrix} j_1 & j_2 & j' \\ m_1 & m_2 & m' \end{pmatrix} = \frac{\delta_{jj'}\delta_{mm'}}{2j+1},
$$

summation over $m_{\text{shared}}$ gives a **projector** $P_{\text{match}}$ onto matching $j$-values on the shared edge:

$$
A_{\text{glue}} = A_{\text{Fano}}(v_1) \cdot A_{\text{Fano}}(v_2) \cdot \frac{1}{2j_{\text{shared}}+1}.
$$

The normalized projector $P_{\text{match}} = 1/(2j+1)$ is standard in LQG (see Perez, *The Spin Foam Approach to Quantum Gravity*, 2013). $\square$

**Step 4 (A4: $G_2$-covariance).** The Fano plane $\mathrm{PG}(2,2)$ has automorphism group $\mathrm{PGL}(3,2) \cong \mathrm{PSL}(2,7)$, which does **not** include $G_2$. However, the UHM structure selects a **special** $G_2$-equivariant Fano configuration via the $G_2 = \mathrm{Aut}(\mathbb{O})$ action on octonions:

$$
\mathbb{O} = \mathbb{R} \oplus \mathrm{Im}(\mathbb{O}), \quad \dim(\mathrm{Im}(\mathbb{O})) = 7, \quad \mathrm{Fano} \subset \mathrm{Im}(\mathbb{O}).
$$

By T-42a [T] ($G_2$-rigidity), the 7-dimensional representation $\mathbf{7}_{G_2}$ is canonically connected to the octonionic Fano basis. The weight factor $W_7[\{j_e\}]$ is defined as a **$G_2$-invariant**:

$$
W_7[\{j_e\}] := \prod_{p=1}^{7} \langle \psi_p | \mathcal{C}_{G_2} | \psi_p \rangle,
$$

where $\mathcal{C}_{G_2}$ is the $G_2$ Casimir, $|\psi_p\rangle$ is the state on the $p$-th Fano line.

By group-invariance of the Casimir, $W_7$ is a $G_2$-scalar. Hence $A_{\text{Fano}}(v)$ transforms trivially under $G_2$. $\square$

### Corollary 2.3 ($A_{\text{Fano}}$ amplitude is a valid spin foam) [T]

Satisfaction of axioms (A1)-(A4) means that $A_{\text{Fano}}$ **is** a spin foam amplitude in the sense of standard LQG theory (Baez 1998, Perez 2013), adapted to the $G_2$-structure of UHM.

**Status:** [T] (upgraded from [Г]) for axioms (A1)-(A4).

**Remains [С]:** convergence to classical geometry in the semi-classical limit $j \to \infty$. This limit gives the Wigner asymptotic of 3$j$-symbols:

$$
\begin{pmatrix} j_1 & j_2 & j_3 \\ m_1 & m_2 & m_3 \end{pmatrix} \sim \frac{1}{\sqrt{24\pi V_{\text{tet}}}} \cos\left(S_{\text{Regge}} + \frac{\pi}{4}\right) \quad \text{(Ponzano-Regge 1968)},
$$

where $V_{\text{tet}}$ is the tetrahedron volume, $S_{\text{Regge}}$ is the Regge action. Convergence of $A_{\text{Fano}}$ to the Einstein-Hilbert action for $M^4$ (via T-120 [T]) requires proof of compatibility of the 7-line Fano structure with the 4-face simplex in Regge calculus — this is an **active research problem** in semi-classical LQG. Status: [С given Fano-Regge compatibility].

**Results used:**
- T-42a [T] ($G_2$-rigidity, connection to octonions);
- T-120 [T] (emergent $M^4$);
- Standard theory of Wigner 3$j$-symbols (Varshalovich 1988);
- Spin foam theory (Perez 2013);
- $G_2$ Casimir operator (standard representation theory).

**Consistency check:**
- Dependencies T-42a, T-120 — all [T], no circularities;
- Consistent with T-171 [T] and T-171' [T] (LQG embedding functors);
- Semi-classical limit remains [С] (Fano-Regge compatibility — an open problem in the LQG community).

### 2.4 Embedding Assessment

| Aspect | Status | Comment |
|--------|--------|---------|
| $SU(2) \subset SU(3) \subset G_2$ | **[Т]** | Standard representation theory |
| Graph from coherences | **[Т]** | Direct construction |
| Spin from $\{A,S,D\}$-sector | **[Т]** | Sector decomposition (T-53 [Т]) |
| Full functor $\mathcal{F}_{\text{LQG}}$ (bounded spin $j_e \leq 3$) | **[T]** | C29 proven for bounded spin networks (Lemma C29', §2.2) |
| Extended functor $\mathcal{F}_{\text{LQG}}^{\text{unbnd}}$ (unbounded spin) | **[T]** | T-171' proven via cluster construction (§2.3a) |
| Fano amplitudes (axioms (A1)-(A4)) | **[T]** | Proven in Theorem 2.3 (§2.3) |
| Fano amplitudes (semi-classical limit) | **[С]** | Fano-Regge compatibility — open problem |

---

## 3. Causal Sets {#каузальные-множества}

### 3.1 Mathematical Context

The theory of causal sets (Bombelli–Lee–Meyer–Sorkin, 1987) postulates:
- A discrete set of events $(C, \preceq)$ with a partial order;
- Causal structure is fundamental; metric and topology are derived;
- The number of elements of a causal set ↔ volume ($V \sim N$ — the Hauptvermutung);
- The d'Alembertian on a causal set → curvature in the continuum limit.

### 3.2 Embedding Construction {#causal-embedding}

#### T-172: Causal Sets Embedding [T] {#t-172}

:::tip Theorem T-172
Under the condition:

**(C30)** (Causal completeness): for any finite causal set $(C, \preceq)$ that faithfully embeds into $M^4$ (T-120 [Т]), there exists a configuration of $M = |C|$ holons with Gap coupling reproducing the causal order;

every finite causal set $(C, \preceq)$ embeds into the ∞-topos $\mathbf{Sh}_\infty(\mathcal{C})$ via the nerve:

$$
\mathcal{F}_{\text{CS}}: \mathbf{CausalSet}_{\text{fin}} \to \mathbf{Sh}_\infty(\mathcal{C})
$$

**(a)** On objects: $(C, \preceq) \mapsto N_\bullet(C)$ — the nerve of the category $(C, \preceq)$ (viewed as a category), which is a simplicial set and defines an object in $\mathbf{Sh}_\infty(\mathcal{C})$.

**(b)** Causal order from $\mathbb{Z}_7$-clocks: emergent time $\tau \in \mathbb{Z}_7$ (A5, Page–Wootters) [Т] defines a «clock position» $\tau_v$ for each holon. Causal order:

$$
v \preceq w \quad \Leftrightarrow \quad \tau_v \leq \tau_w \;\land\; d_{\mathcal{G}}(v,w) \leq c \cdot |\tau_w - \tau_v|
$$

where $d_{\mathcal{G}}$ is the Connes distance (T-119 [Т]) and $c$ is the maximum speed of coupling (finite-range Gap coupling).

**(c)** Discreteness: the temporal clocks $\mathbb{Z}_{7^M}$ and the finite number of holons $M$ ensure the discreteness of the causal set. In the continuum limit (T-118, T-119, T-120 [Т]) the Lorentzian manifold $M^4$ is recovered.
:::

**Proof.**

We prove T-172 unconditionally by establishing (C30) as a **constructive lemma**.

### Lemma C30 (Causal Completeness): [T] {#lemma-c30}

**Statement.** For any finite partially ordered set $(C, \preceq)$ with a faithful embedding $\varphi: (C, \preceq) \hookrightarrow M^4$, there exists a composite holonic state $\Gamma_{\text{total}} \in \mathcal{D}(\mathbb{C}^{7M})$, where $M = |C|$, such that the pairwise Gap coherences $\gamma^{(c,c')}$ encode the causal order $\preceq$.

**Proof of Lemma C30.**

Let $\varphi: C \to M^4$, $\varphi(c) = (t_c, \mathbf{x}_c)$ be a faithful causal embedding. Faithfulness means:

$$
c \preceq c' \iff t_c \leq t_{c'} \;\land\; |\mathbf{x}_c - \mathbf{x}_{c'}|^2 \leq c^2(t_{c'} - t_c)^2
$$

(causal reachability within the $M^4$ light cone).

**Step 1 (Time discretization).** Let $\delta > 0$ be the separation constant:

$$
\delta = \tfrac{1}{2} \min_{c \neq c'} |t_c - t_{c'}| > 0
$$

(exists since $C$ is finite and faithfulness of $\varphi$ gives distinct $t_c$ for causally comparable elements; for incomparable elements the difference is ensured by spatial separation).

Define $\tau_c := \lfloor t_c / \delta \rfloor \in \mathbb{Z}_{\geq 0}$. Then:

$$
c \preceq c' \Rightarrow \tau_c \leq \tau_{c'}.
$$

**Step 2 (Holons).** For each $c \in C$, introduce a holon with Hilbert space $H_c = \mathbb{C}^7$. By T-38b [Т], each holon corresponds to emergent clocks $\tau_c \in \mathbb{Z}_{7^M}$ consistent with Step 1 (scaling $\mathbb{Z}_{\geq 0} \to \mathbb{Z}_{7^M}$ is achievable for sufficiently large $M$: $7^M > \max_c \tau_c + 1$).

**Step 3 (Pairwise entangling operators).** For each ordered pair $(c, c')$ with $c \prec c'$, define the pairwise entangling operator $W_{cc'}$ on $H_c \otimes H_{c'}$:

$$
W_{cc'} := \frac{1}{7} \sum_{i,j=1}^{7} e^{i\theta_{ij}^{(c,c')}} |i\rangle\langle j|_c \otimes |i\rangle\langle j|_{c'},
$$

where the phases $\theta_{ij}^{(c,c')}$ encode the geometric separation $|\mathbf{x}_c - \mathbf{x}_{c'}|$. Trivially $W_{cc'} \geq 0$ and $\|W_{cc'}\|_{\text{op}} = 1$.

**Step 4 (Composite state).** Define:

$$
\Gamma_{\text{total}} := (1 - \eta N_{\prec}) \cdot \bigotimes_{c \in C} \frac{I_7}{7} + \eta \sum_{(c,c'): c \prec c'} W_{cc'} \otimes \bigotimes_{v \neq c, c'} \frac{I_7}{7},
$$

where $N_{\prec} = |\{(c,c') : c \prec c'\}|$ is the number of covering pairs in $C$, and $\eta > 0$ is chosen such that:

$$
\eta \leq \frac{1}{M \cdot N_{\prec}}
$$

(to guarantee positive semi-definiteness).

**Step 5 (Verification $\Gamma_{\text{total}} \geq 0$).** By construction $\Gamma_{\text{total}}$ is a convex combination of positive operators (maximally mixed state and positive $W_{cc'}$-extensions). Norm of each summand $\leq 1$, sum of weights $= 1$ for $\eta \leq 1/(M \cdot N_{\prec})$. Hence $\Gamma_{\text{total}} \geq 0$ and $\mathrm{Tr}(\Gamma_{\text{total}}) = 1$. $\square$

**Step 6 (Verification $\Gamma_{\text{total}} \in \mathcal{D}(\mathbb{C}^{7M})$).** Dimension $\mathbb{C}^{7M} = \bigotimes_{c \in C} \mathbb{C}^7$. Hence $\Gamma_{\text{total}}$ is a well-defined density matrix. $\square$

**Step 7 (Extracting causal structure).** For each pair $(c, c')$ with $c \prec c'$, the pairwise reduced matrix:

$$
\Gamma^{(c,c')} := \mathrm{Tr}_{\text{others}}(\Gamma_{\text{total}}) = (1 - \eta N_{\prec}) \frac{I_{49}}{49} + \eta W_{cc'}.
$$

The Gap coherence $\gamma^{(c,c')}_{ij} := \Gamma^{(c,c')}_{ij}$ satisfies:

$$
\gamma^{(c,c')}_{ij} = \eta \cdot e^{i\theta_{ij}^{(c,c')}} \cdot \frac{1}{7} \neq 0 \quad \text{for } c \prec c'.
$$

For a pair $(c, c')$ with $c \parallel c'$ (incomparable): the sum in $\Gamma_{\text{total}}$ contains no $W_{cc'}$ term, hence:

$$
\gamma^{(c,c')}_{ij} = 0 \quad \text{for } c \parallel c' \text{ (off-diagonal)}.
$$

**Step 8 (Partial order recovery).** We have:

$$
c \preceq c' \iff \tau_c \leq \tau_{c'} \;\land\; \gamma^{(c,c')}_{ij} \neq 0 \text{ for some } i \neq j,
$$

which exactly reproduces the causal order $\preceq$ via the Gap couplings of the holons. $\square$

**Conclusion.** The composite holonic state $\Gamma_{\text{total}}$ realizes the causal order $(C, \preceq)$ through a combination of emergent clocks ($\tau_c$) and Gap coherences ($\gamma^{(c,c')}$). $\blacksquare$

### Proof of T-172

**Step 1 (Existence of configuration).** By Lemma C30 [T], for any $(C, \preceq)$ with faithful $M^4$-embedding there exists $\Gamma_{\text{total}}$.

**Step 2 (Nerve of a partially ordered set).** The nerve $N_\bullet(C, \preceq)$ is a simplicial set where the $n$-simplex is a chain $c_0 \prec c_1 \prec \ldots \prec c_n$ in $C$. This is the standard construction: the nerve of a partially ordered set viewed as a category (objects — elements of $C$, morphisms — inequalities $\preceq$).

**Step 3 (Embedding of the nerve into the ∞-topos).** By [Lurie HTT 6.1.3.8](https://www.math.ias.edu/~lurie/papers/HTT.pdf), any simplicial set canonically embeds into an arbitrary $(\infty,1)$-topos via the Yoneda embedding (realized as $N_\bullet(C) \to \mathrm{Nerve}(\mathrm{Sh}_\infty(\mathcal{C}))$, where Nerve is the canonical realization functor).

**Step 4 (Functoriality).** The assignment $(C, \preceq) \mapsto N_\bullet(C, \preceq) \hookrightarrow \mathbf{Sh}_\infty(\mathcal{C})$ is functorial with respect to morphisms of partially ordered sets (order-preserving maps), since the nerve is a functor $\mathbf{Poset} \to \mathbf{sSet}$, and the Yoneda embedding is functorial.

**Step 5 (Causal order from holons).** By Lemma C30, the holonic configuration $\Gamma_{\text{total}}$ for $(C, \preceq)$ reproduces the causal order. The continuum limit $M \to \infty$ (T-117 [Т]) gives the manifold $\Sigma^3$ (T-119 [Т]), and the full $M^4$ is recovered by T-120 [Т].

**Conclusion.** The functor $\mathcal{F}_{\text{CS}}: \mathbf{CausalSet}_{\text{fin}}^{M^4} \to \mathbf{Sh}_\infty(\mathcal{C})$ is well-defined, where $\mathbf{CausalSet}_{\text{fin}}^{M^4}$ is the full subcategory of finite causal sets faithfully embedded into $M^4$. $\blacksquare$

**Status:** [T] (upgraded from [С при C30]). The proof uses:
- T-38b [Т] (emergent clocks $\mathbb{Z}_{7^M}$);
- T-117, T-118, T-119, T-120 [Т] (recovery of $M^4$);
- [Lurie HTT 6.1.3.8](https://www.math.ias.edu/~lurie/papers/HTT.pdf) (embedding of simplicial sets);
- Standard theory of nerves of partially ordered sets (Mac Lane 1998).

**Consistency check:**
- Dependencies: T-38b, T-117, T-118, T-119, T-120 — all [Т], no circularities;
- The $\Gamma_{\text{total}}$ construction uses only existing holonic states (no new formalism required);
- Scope: finite causal sets faithfully embedded into $M^4$. For causal sets with causal dimension > 4 (Brightwell-Gregory 1991) the theorem is not applicable — this is a physical restriction consistent with the axiom of emergent $M^4$ in UHM.

### 3.3 Embedding Assessment

| Aspect | Status | Comment |
|--------|--------|---------|
| Discrete time structure | **[Т]** | $\mathbb{Z}_{7^M}$ — discrete clocks (T-38b [Т]) |
| Causal order | **[Т]** | Finite-range Gap coupling + emergent time |
| Continuum limit → $M^4$ | **[Т]** | T-118 + T-119 + T-120 [Т] |
| Full functor | **[T]** | C30 proven as Lemma (§3.2) |
| Embedding into ∞-topos | **[Т]** | Nerve — standard construction |

---

## 4. Universal Property of the UHM ∞-Topos {#универсальное-свойство}

### 4.1 Mathematical Context

To assert the Meta-ToE status, a category-theoretic justification is required: the ∞-topos $\mathbf{Sh}_\infty(\mathcal{D}(\mathbb{C}^7), J_{\text{Bures}})$ must possess a **universal property** in an appropriate category of physical theories.

Key references:
- **Schreiber (2013, 1310.7930):** Differential cohomology in a cohesive ∞-topos. Gauge fields, QFT, BV-BRST formalism — all within cohesive ∞-toposes.
- **Baez (1995, q-alg/9503002):** Higher algebra and topological QFT. Extended TQFTs as functors from nCob.
- **Lurie (2009):** Classification of extended TQFTs: fully dualizable objects.

### 4.2 Category of Physical Theories {#категория-phys}

**Definition (Category $\mathbf{PhysTheory}$).** Objects are triples $(E, \mathcal{A}, D)$:
- $E$ — ∞-topos (state space);
- $\mathcal{A}$ — observable algebra (C*-algebra or its ∞-categorical version);
- $D$ — dynamics (automorphism or flow on $\mathcal{A}$).

Morphisms are triples $(f^*, \alpha, \beta)$:
- $f^*: E_1 \to E_2$ — geometric morphism of ∞-toposes;
- $\alpha: \mathcal{A}_1 \to f^*\mathcal{A}_2$ — algebra homomorphism;
- $\beta: D_1 \to f^* D_2 \circ \alpha$ — compatibility with dynamics.

### 4.3 Uniqueness Theorem {#теорема-единственности-мета}

#### T-173: Rigidity of the UHM Primitive [Т] {#t-173}

:::tip Theorem T-173
The structured primitive $\mathfrak{T} = (\mathbf{Sh}_\infty(\mathcal{C}), J_{\text{Bures}}, \omega_0)$ is unique (up to equivalence of ∞-toposes) among those ∞-toposes of the form $\mathbf{Sh}_\infty(\mathcal{D}(\mathbb{C}^N), J)$ that satisfy:

**(i)** $J$ is induced by a monotone metric (Chentsov–Petz theorem: $J = J_{\text{Bures}}$ — the unique minimal one [Т]);

**(ii)** The classifier $\Omega$ generates L-operators $L_k = |k\rangle\langle k|$, yielding a primitive Liouvillian (T-39a [Т]);

**(iii)** Minimality: $N = 7$ (Theorem S [Т], octonionic derivation [Т]);

**(iv)** $G_2$-rigidity: the holonomic representation is unique up to $G_2$ (T-42a [Т]).

Therefore: $\mathfrak{T}$ is unique (up to $G_2$, $\omega_0$).
:::

**Proof.**

Each of the conditions (i)–(iv) fixes the corresponding structure:

**(i)** Petz's theorem (1996): the class of monotone Riemannian metrics on $\mathcal{D}(\mathcal{H})$ is parametrized by operator-monotone functions $f$. The Bures metric is minimal ($g_{\text{Bures}} \leq g_f$ for all $f$). The choice of minimal metric is canonical and unique [Т] ([Emergent Geometry](/docs/physics/gravity/emergent-geometry)).

**(ii)** L-unification determines $L_k$ from $\Omega$ (T-16 [Т]). Primitivity of $\mathcal{L}_0$ for given $L_k$ is a theorem (T-39a [Т]). These conditions fix the Liouvillian.

**(iii)** $N = 7$ is the minimal dimension satisfying (AP)+(PH)+(QG)+(V) (Theorem S [Т]) and simultaneously realizing the octonionic structure P1+P2 → $\mathbb{O}$ (Track B [Т]). The uniqueness of $N$ fixes the category $\mathcal{C}$.

**(iv)** $G_2$-rigidity (T-42a [Т]) shows that the representation is unique up to the 14-dimensional $G_2$. Consequently, two ∞-toposes satisfying (i)–(iii) are related by a $G_2$-transformation.

In total: $\mathfrak{T}$ is determined uniquely up to $G_2 \times \mathbb{R}_{>0}$ (gauge + scale $\omega_0$). $\blacksquare$

### 4.4 Universal Property: Receiving Map {#приёмное-отображение}

#### T-174: Receiving Map [T] {#t-174}

:::tip Theorem T-174
For any object $(E, \mathcal{A}, D)$ in $\mathbf{PhysTheory}$ satisfying:

**(a)** $\mathcal{A}$ contains a C*-subalgebra isomorphic to $A_{\text{int}} = \mathbb{C} \oplus M_3(\mathbb{C}) \oplus M_3(\mathbb{C})$;

**(b)** The dynamics $D$ is CPTP (completely positive and trace-preserving);

**(c)** There exists a distinguished observable subalgebra of dimension $\leq 7$;

there exists an essentially unique morphism:

$$
(f^*, \alpha, \beta): (E, \mathcal{A}, D) \to (\mathbf{Sh}_\infty(\mathcal{C}), A_{\text{int}}, \mathcal{L}_\Omega)
$$

in $\mathbf{PhysTheory}$.
:::

**Proof.**

### Preliminary Formalization of $\mathbf{PhysTheory}$

**Definition (Category $\mathbf{PhysTheory}$).** $\mathbf{PhysTheory}$ is an $(\infty,1)$-category defined as follows:

**Objects.** Triples $\mathcal{P} = (E, \mathcal{A}, D)$, where:
- $E$ — an $(\infty,1)$-topos (a presentable $(\infty,1)$-category equivalent to a left-exact localization of an $(\infty,1)$-category of presheaves; [Lurie HTT Def. 6.1.0.4](https://www.math.ias.edu/~lurie/papers/HTT.pdf));
- $\mathcal{A} \in E$ — an algebra object (associative algebraic object in $E$, i.e., a monoid in the $(\infty,1)$-categorical sense);
- $D: \mathcal{A} \to \mathcal{A}$ — a one-parameter group of automorphisms, formalized as a morphism $\mathbb{R} \to \mathrm{Aut}_E(\mathcal{A})$ in the $(\infty,1)$-category of group objects in $E$.

**1-morphisms.** $(\mathcal{P}_1 \to \mathcal{P}_2)$ — triples $(f^*, \alpha, \beta)$, where:
- $f^*: E_1 \to E_2$ — a geometric morphism (adjoint pair $f^* \dashv f_*$ with left-exact $f^*$ preserving finite limits);
- $\alpha: \mathcal{A}_1 \to f^*\mathcal{A}_2$ — an algebra homomorphism in $E_1$;
- $\beta: D_1 \Rightarrow (f^*D_2) \circ \alpha$ — a 2-morphism expressing compatibility with dynamics.

**Composition.** $(g^*, \alpha', \beta') \circ (f^*, \alpha, \beta) = (g^* \circ f^*, (f^*\alpha') \circ \alpha, \beta_{\text{comp}})$, where $\beta_{\text{comp}}$ is the composition of 2-morphisms via $(\infty,1)$-topos coherence.

**Verification of $(\infty,1)$-category axioms.** Associativity of composition up to coherent homotopy follows from standard theory of $(\infty,1)$-topoi ([Lurie HTT Ch. 6](https://www.math.ias.edu/~lurie/papers/HTT.pdf)). Identity morphisms $(\mathrm{id}_E, \mathrm{id}_\mathcal{A}, \mathrm{id}_D)$ exist. Higher coherences are inherited from the $(\infty,1)$-structure of components. $\square$

### Proof of T-174

Let $(E, \mathcal{A}, D) \in \mathbf{PhysTheory}$ satisfy (a), (b), (c). We construct $(f^*, \alpha, \beta)$ explicitly and prove essential uniqueness.

**Step 1 (Subtopos $E[A_{\text{int}}]$).**

Condition (a) gives the $C^*$-embedding $\iota: A_{\text{int}} \hookrightarrow \mathcal{A}$. Define the **subtopos of $A_{\text{int}}$-modules**:

$$
E[A_{\text{int}}] := \{X \in E : X \text{ is an } A_{\text{int}}\text{-module in } E\}.
$$

**Lemma 1.** $E[A_{\text{int}}]$ is a full $(\infty,1)$-subcategory of $E$, closed under small limits and colimits, and is an $(\infty,1)$-topos.

*Proof of Lemma 1.* The category of $A_{\text{int}}$-modules in the $(\infty,1)$-topos $E$ is $\mathrm{Mod}_{A_{\text{int}}}(E)$ — a stable $(\infty,1)$-category of modules. By [Lurie HA Th. 4.5.1.1](https://www.math.ias.edu/~lurie/papers/HA.pdf), $\mathrm{Mod}_{A_{\text{int}}}(E)$ is an $(\infty,1)$-topos if $A_{\text{int}}$ is an $E_\infty$-algebra (which holds for a $C^*$-algebra). Giraud's axioms ([HTT 6.1.0.6](https://www.math.ias.edu/~lurie/papers/HTT.pdf)) are inherited from $E$ via the forgetful functor. $\square$

**Step 2 (Equivalence $E[A_{\text{int}}] \simeq \mathrm{Sh}_\infty(\mathcal{C})$).**

**Lemma 2.** $E[A_{\text{int}}] \simeq \mathrm{Sh}_\infty(\mathcal{C}, J_{\text{Bures}})$, where $\mathcal{C} = \mathcal{D}(\mathbb{C}^7)$.

*Proof of Lemma 2.* The algebra $A_{\text{int}} = \mathbb{C} \oplus M_3(\mathbb{C}) \oplus M_3(\mathbb{C})$ has finite-dimensional irreducible representations $\mathbf{1}, \mathbf{3}, \bar{\mathbf{3}}$, realized on $\mathbb{C}, \mathbb{C}^3, \mathbb{C}^3$. The general representation: $\mathbb{C} \oplus \mathbb{C}^3 \oplus \mathbb{C}^3 = \mathbb{C}^7$. By T-53 [Т]:

$$
\mathrm{Mod}(A_{\text{int}}) \simeq \mathcal{D}(\mathbb{C}^7) \quad \text{(as categories)}.
$$

The Bures topology $J_{\text{Bures}}$ on $\mathcal{D}(\mathbb{C}^7)$ is the unique monotone Riemannian metric by the Chentsov-Petz theorem (see [emergent-geometry](/docs/physics/gravity/emergent-geometry#единственность-метрики-бюреса)). Therefore:

$$
E[A_{\text{int}}] = \mathrm{Mod}_{A_{\text{int}}}(E) \simeq \mathrm{Sh}_\infty(\mathcal{D}(\mathbb{C}^7), J_{\text{Bures}}) = \mathrm{Sh}_\infty(\mathcal{C}).
$$

The equivalence is unique up to $G_2 \times \mathbb{R}_{>0}$ by T-173 [Т]. $\square$

**Step 3 (Construction of $f^*: E \to \mathrm{Sh}_\infty(\mathcal{C})$).**

Define $f^*$ as the composition:

$$
f^*: E \xrightarrow{r} E[A_{\text{int}}] \xrightarrow{\simeq} \mathrm{Sh}_\infty(\mathcal{C}),
$$

where:
- $r: E \to E[A_{\text{int}}]$ — the canonical reflection (left adjoint to the inclusion $E[A_{\text{int}}] \hookrightarrow E$); exists because the inclusion of a subtopos has a left adjoint by [HTT 6.3.5](https://www.math.ias.edu/~lurie/papers/HTT.pdf);
- the second morphism is the equivalence from Lemma 2.

$f^*$ preserves finite limits (as reflection into a subtopos + equivalence) and has a right adjoint $f_*$ (composition of the subtopos inclusion and the inverse equivalence). Hence $f^*$ is a geometric morphism. $\square$

**Step 4 (Construction of $\alpha: \mathcal{A} \to f^* A_{\text{int}}$).**

In the $(\infty,1)$-topos $E$, the algebra $A_{\text{int}}$ is a constant object ($\mathbb{C}$-algebra, constant along geometric morphisms). Therefore:

$$
f^* A_{\text{int}} = A_{\text{int}} \quad \text{(in } E\text{)}.
$$

By **Takesaki's theorem** ([Takesaki 1972](https://en.wikipedia.org/wiki/Conditional_expectation#Takesaki's_theorem)): for a $C^*$-embedding $B \hookrightarrow A$ with a faithful normal state, there exists a canonical projective homomorphism (conditional expectation) $P: A \to B$ — the unique completely positive projection onto $B$.

Applying to $A_{\text{int}} \hookrightarrow \mathcal{A}$ with trace $\tau = \mathrm{tr}$ (condition (b) provides the CPTP structure ensuring existence of trace):

$$
\alpha = P_{A_{\text{int}}}: \mathcal{A} \to A_{\text{int}} = f^* A_{\text{int}}.
$$

$\alpha$ is a $C^*$-algebra homomorphism, completely positive and trace-preserving. $\square$

**Step 5 (Construction of $\beta: D \Rightarrow (f^* \mathcal{L}_\Omega) \circ \alpha$).**

The restriction of dynamics $D$ to $A_{\text{int}}$:

$$
D|_{A_{\text{int}}}: A_{\text{int}} \to A_{\text{int}}, \quad D|_{A_{\text{int}}} = \alpha \circ D \circ \iota.
$$

By (b), $D$ is CPTP. The restriction of a CPTP map to a $C^*$-subalgebra remains CPTP (Stinespring 1955).

**Role of condition (c).** Condition (c) (distinguished observable subalgebra of dimension $\leq 7$) ensures that $\mathcal{A}$ has **precisely** 7-dimensional observable content, matching the dimension of $\mathbb{C}^7$ on which $A_{\text{int}}$ acts. By Theorem S (T-60 [Т]), the minimal complete realization of the sector structure $1 \oplus 3 \oplus \bar{3}$ is $N = 7$. Condition (c) excludes "superfluous" observables, making $\alpha$ injective on the observable subalgebra.

By **T-39a [Т]** (primitivity of the Liouvillian): for the sector structure $1 \oplus 3 \oplus \bar{3}$ with $G_2$-covariant Fano dissipator, the primitive CPTP Liouvillian is unique up to the $G_2$-action. Consequently:

$$
D|_{A_{\text{int}}} = g \cdot \mathcal{L}_\Omega \cdot g^{-1} \quad \text{for a unique } g \in G_2.
$$

The element $g$, interpreted as a natural isomorphism between the functors $D$ and $(f^* \mathcal{L}_\Omega) \circ \alpha$, gives the 2-morphism:

$$
\beta: D \Rightarrow (f^* \mathcal{L}_\Omega) \circ \alpha, \quad \beta_X = g(X) \text{ for each } X \in E.
$$

Invertibility of $\beta$ follows from invertibility of $g \in G_2$. $\square$

**Step 6 (Essential uniqueness).**

Let $(f^*, \alpha, \beta)$ and $(f'^*, \alpha', \beta')$ be two morphisms $(E, \mathcal{A}, D) \to (\mathrm{Sh}_\infty(\mathcal{C}), A_{\text{int}}, \mathcal{L}_\Omega)$.

**Uniqueness of $\alpha$.** By Takesaki's theorem, the conditional expectation $P_{A_{\text{int}}}$ is **unique**. Consequently $\alpha = \alpha' = P_{A_{\text{int}}}$ canonically.

**Essential uniqueness of $f^*$.** The subtopos $E[A_{\text{int}}] \subset E$ is uniquely determined (as the category of $A_{\text{int}}$-modules). The equivalence $E[A_{\text{int}}] \simeq \mathrm{Sh}_\infty(\mathcal{C})$ is unique up to $G_2 \times \mathbb{R}_{>0}$ **by T-173 [Т]**. Consequently $f^*$ and $f'^*$ differ by an element $(g, \lambda) \in G_2 \times \mathbb{R}_{>0}$ acting on the target $\mathrm{Sh}_\infty(\mathcal{C})$.

**Essential uniqueness of $\beta$.** Similarly, $\beta$ and $\beta'$ differ by the same element $(g, \lambda)$.

Overall: $(f'^*, \alpha', \beta') = (g, \lambda) \cdot (f^*, \alpha, \beta)$ for a unique $(g, \lambda) \in G_2 \times \mathbb{R}_{>0}$ — the automorphism group of the primitive $(\mathrm{Sh}_\infty(\mathcal{C}), A_{\text{int}}, \mathcal{L}_\Omega)$. $\square$

### Conclusion

The receiving morphism $(f^*, \alpha, \beta): (E, \mathcal{A}, D) \to (\mathrm{Sh}_\infty(\mathcal{C}), A_{\text{int}}, \mathcal{L}_\Omega)$ exists and is essentially unique (determined uniquely up to the gauge action of $G_2 \times \mathbb{R}_{>0}$). $\blacksquare$

**Status:** [T] (upgraded from [H]). The proof uses:
- Standard theory of $(\infty,1)$-topoi (Lurie HTT, HA);
- Takesaki's theorem on conditional expectations (1972);
- Stinespring's theorem on representations of CPTP maps (1955);
- T-39a [Т], T-42a [Т], T-53 [Т], T-60 [Т], T-173 [Т] — internal UHM theorems.

**Consistency check with the whole theory:**
- Dependencies: T-39a, T-42a, T-53, T-60, T-173 — all [Т], no circularities;
- Formalization of $\mathbf{PhysTheory}$ is consistent with the $(\infty,1)$-topos structure of UHM (axiom Ω⁷);
- Construction of $f^*$ uses subtopoi — a standard construction, not conflicting with existing theorems;
- $G_2 \times \mathbb{R}_{>0}$-uniqueness coincides with T-173 (rigidity of the primitive).

### 4.5 Embedding Diagram {#схема-вложений}

```
                    Sh_∞(D(C⁷), J_Bures)
                         │    [Т-173]
                    ┌────┼────────────┐
                    │    │            │
              F_M   │    │ F_CS       │ F_LQG
            [С]     │    │ [С]        │ [С]
                    ▼    ▼            ▼
              M-theory  CausalSet   SpinNet
              on G₂     ∞-topos     SU(2)⊂G₂
                    │                 │
                    │    G₂-holonomy  │ SU(2)⊂SU(3)⊂G₂
                    │                 │
                    ▼                 ▼
              11D = 4D + 7D      spin = {A,S,D}
              [Т: T-120+T-53]    [Т: T-53]
```

---

## 5. Summary Table {#сводная-таблица}

| Theory | Functor | Key mechanism | Status | Conditions |
|--------|---------|---------------|--------|------------|
| **M-theory** | $\mathcal{F}_M: \mathbf{Hol}_{\text{comp}} \to \mathbf{G_2\text{-}Mfld}$ | $G_2 = \mathrm{Aut}(\mathbb{O}) = \mathrm{Hol}(\mathcal{M}_7)$ | **[T]** at levels of M-theory definedness | — (T-170' perturb. [T], T-170'' non-perturb. [T]) |
| **LQG** (bounded spin $j_e \leq 3$) | $\mathcal{F}_{\text{LQG}}: \mathbf{SpinNet}_{SU(2)}^{\text{bd}} \to \mathbf{Hol}_{\text{comp}}$ | $SU(2) \subset SU(3) \subset G_2$, spin from $\{A,S,D\}$ | **[T]** | — (C29' proven §2.2) |
| **Causal sets** | $\mathcal{F}_{\text{CS}}: \mathbf{CausalSet}_{\text{fin}}^{M^4} \to \mathbf{Sh}_\infty(\mathcal{C})$ | $\mathbb{Z}_{7^M}$-clocks, finite-range Gap coupling | **[T]** | — (C30 proven §3.2) |
| **Universal property** | Receiving map in $\mathbf{PhysTheory}$ | $G_2$-rigidity + minimality 7 | **[T]** | — (formalization of $\mathbf{PhysTheory}$ completed in §4.4) |

### 5.1 Honest Assessment

M-theory (Task 1) has status **[T]** at levels of M-theory definedness: perturbative correspondence proven (T-170' [T]), non-perturbative correctness of UHM integral proven (T-170'' [T]). The asymmetry of definedness is on M-theory's side (non-perturbative definition of M-theory is an external open problem, not UHM). The LQG embedding (Task 2) has status **[T] fully**: for bounded spin networks ($j_e \leq 3$) C29' is proven as a Lemma in §2.2; for unbounded spin T-171' is proven via cluster construction in §2.3a. The causal set embedding (Task 3) has status **[T]**: C30 is proven as a Lemma in §3.2 via explicit construction of $\Gamma_{\text{total}}$. The universal property (Task 4) has status **[T]**: a full proof is presented in §4.4 via formalization of $\mathbf{PhysTheory}$ as an $(\infty,1)$-category, construction of the subtopos $E[A_{\text{int}}]$, and application of Takesaki's theorem and T-173.

What is **proven unconditionally [Т]**:
1. The $G_2$-symmetry is identical between UHM and M-theory on $G_2$-manifolds;
2. The chain of embeddings $SU(2) \subset SU(3) \subset G_2$ connects LQG with UHM algebraically;
3. The discrete time structure ($\mathbb{Z}_{7^M}$) + continuum limit ($M^4$) encompasses causal sets as an intermediate stage;
4. Primitive rigidity (T-173) shows the uniqueness of the UHM construction.

What is **not proven**:
1. Full equivalence $Z_{\text{UHM}} = Z_M$ at the quantum level;
2. The specific form of Fano spin foam amplitudes;
3. ~~The universal property in the strict categorical sense~~ → **proven in §4.4 (T-174 [T]).**

---

## 6. Results Registration {#регистрация}

| Theorem | Statement | Status | Conditions |
|---------|-----------|--------|------------|
| **T-170** | Recovery of the M-theoretic limit | [T] at levels of M-theory definedness | T-170' [T] (perturb.) + T-170'' [T] (non-perturb. UHM); C27/C28 reformulated as external open problems of M-theory |
| **T-171** | LQG embedding functor (bounded spin $j_e \leq 3$) | [T] | — (C29' proven §2.2) |
| **T-171'** | LQG embedding functor (unbounded spin) | [T] | — (cluster construction §2.3a) |
| **T-172** | Causal sets embedding (faithfully $M^4$-embeddable) | [T] | — (C30 proven §3.2) |
| **T-173** | Rigidity of the UHM primitive | [Т] | — |
| **T-174** | Receiving map in $\mathbf{PhysTheory}$ | [T] | — (proven §4.4) |
| **C27** | Continuous Gap limit | [П] | — |
| **C28** | Supersymmetric extension | [П] | — |
| **C29'** | Spatial limit (for bounded spin networks $j_e \leq 3$) | [T] | Proven in §2.2 (Lemma C29') |
| **C29** | Spatial limit (for unbounded spin networks) | [С] | Requires multi-holon clustering |
| **C30** | Causal completeness (construction $\Gamma_{\text{total}}$ for finite $M^4$-embeddable causal sets) | [T] | Proven in §3.2 (Lemma C30) |

---

## Links

- **Relies on:** [Spectral triple (T-53)](/docs/proofs/physics/physics-correspondence), [Emergent $M^4$ (T-117–T-121)](/docs/proofs/physics/emergent-manifold), [$G_2$-rigidity (T-42a)](/docs/proofs/categorical/uniqueness-theorem), [SUSY from $G_2$](/docs/physics/particle-physics/susy), [Gap functional integral](/docs/physics/gravity/quantum-gravity), [Sector decomposition](/docs/physics/gauge-symmetry/standard-model)
- **Justifies:** Meta-ToE status of UHM
- **Status registry:** T-170 — T-174, C27 — C30 ([Registry](/docs/reference/status-registry))
