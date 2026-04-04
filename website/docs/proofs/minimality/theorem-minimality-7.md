---
slug: /proofs/minimality/theorem-minimality-7
sidebar_position: 1
title: "Theorem on 7D Minimality"
format: md
---

# Theorem on Minimal Completeness: A Rigorous Proof

## Theorem Statement

:::warning Methodological clarification: Theorem vs Axiom
The dimensionality $N = 7$ is an **axiom** ([Axiom 3](/docs/core/foundations/axiom-omega#аксиоматика)), characterizing the class of systems under study (Holons).

The **theorem** below (Track A) shows that 7 is the **minimum** value at which conditions (AP)+(PH)+(QG) *can be satisfied*. Independently, the [structural derivation via octonions](/docs/proofs/minimality/theorem-octonionic-derivation) (Track B) gives $N = 7$ from theorems P1+P2 (derived from (AP)+(PH)+(QG)+(V)) via the Hurwitz theorem.

**Honest formulation:** "If we study systems with (AP)+(PH)+(QG), then N ≥ 7. We choose N = 7 as the minimal non-trivial case. This value is independently **proven** by the octonionic structure (P1+P2 [Т] via the T15 chain)."
:::

**Theorem (Minimal Completeness of UHM):**
*The number 7 is the minimum number of **functionally independent aspects (dimensions)** required to close a Rosen (M,R)-system that possesses:*
1. *Autopoietic self-maintenance*
2. *Internal phenomenology (interiority)*
3. *A quantum foundation*

:::warning Clarification: dimensions vs dimensionality
The theorem asserts the minimality of the **number of dimensions** (A, S, D, L, E, O, U), not the dimensionality of the Hilbert space. A realization as a tensor product $\mathcal{H} = \bigotimes_{i=1}^{7} \mathcal{H}_i$ gives $\dim(\mathcal{H}) = \prod_i \dim(\mathcal{H}_i) \geq 2^7 = 128$ for minimal $\dim(\mathcal{H}_i) = 2$.

The formulation "$\dim(\mathcal{H}) \geq 7$" is correct only for the **conceptual 7D formalism**, where each dimension is represented by a single basis vector. For the **operational formalism** with partial trace, a tensor structure is required.
:::

:::info Consistency with Page–Wootters (dim = 42)
The Page–Wootters mechanism ([Property 3 of Ω⁷](/docs/core/foundations/axiom-omega#свойство-3)) uses the space:

$$
\mathcal{H}_{total} = \mathcal{H}_O \otimes \mathcal{H}_{6D} = \mathbb{C}^7 \otimes \mathbb{C}^6 = \mathbb{C}^{42}
$$

This **does not contradict** the minimality of 7 dimensions:
- **7** — the number of functionally independent aspects (A, S, D, L, E, O, U)
- **42** — the dimensionality of the state space in a particular tensor realization

The number 42 = 7 × 6 arises from the factorization in which O is singled out as the "clock" for the emergent time mechanism. See [Coherence matrix → Page–Wootters tensor extension](/docs/core/dynamics/coherence-matrix#тензорное-расширение-page-wootters).
:::

**Formally (conceptual formulation):**

Let $\mathbb{H}$ be a self-consistent system. Then:

$$
|\{i : i \text{ — functionally independent aspect of } \mathbb{H}\}| \geq 7
$$

**Equivalently (tensor realization):**

$$
\mathcal{H} = \bigotimes_{i=1}^{n} \mathcal{H}_i \quad \Rightarrow \quad n \geq 7 \text{ for (AP)+(PH)+(QG)}
$$

where:
- **(AP)** — autopoiesis axiom
- **(PH)** — phenomenology axiom
- **(QG)** — quantum foundation axiom

---

## Part I: Formal Definitions

### Definition 1.1 (Autopoietic System)

A system $\mathbb{H}$ is called **autopoietic** if there exists a map:

$$
\varphi: \mathbb{H} \to \mathbb{H}
$$

such that:
1. $\varphi(\mathbb{H})$ generates components that maintain $\mathbb{H}$
2. A fixed point exists: $\varphi(\mathbb{H}^*) = \mathbb{H}^*$ (self-reproduction)

### Definition 1.2 ((M,R)-System of Rosen) {#определение-12-mr-система-розена}

**Definition:** A system is an (M,R)-system if the following conditions are satisfied:

$$
M: A \to B \quad \text{(metabolism: mapping substrates to products)}
$$

$$
\mathcal{F}: B \to M \quad \text{(repair: products generate metabolism)}
$$

$$
\beta: \mathcal{F} \to \mathcal{F} \quad \text{(closure: repair generates itself)}
$$

**Critical closure condition:**

$$
\beta = f(M, \mathcal{F}) \quad \text{where } \beta \in \mathrm{Hom}(\mathcal{F}, \mathcal{F})
$$

:::note On notation
$\mathcal{F}$ — the repair function in Rosen's (M,R)-system. Not to be confused with $\Phi$ — the [integration measure](/docs/core/structure/dimension-u#мера-интеграции-φ).
:::

This creates a causally closed structure without external causes.

### Definition 1.3 (Phenomenological System)

A system $\mathbb{H}$ has **internal phenomenology** if:
1. There exists a subspace $E \subset \mathcal{H}$ ([Interiority dimension](/docs/core/structure/dimension-e))
2. There exists an operator $\rho_E: E \to E$ (experience density matrix)
3. The spectral decomposition of $\rho_E$ defines [interiority](/docs/proofs/consciousness/interiority-hierarchy#уровень-0-интериорность-interiority):

$$
\rho_E |q_k\rangle = \lambda_k |q_k\rangle
$$

$$
\text{Exp}_k := (\lambda_k, [|q_k\rangle], C, H)
$$

where $\text{Exp}_k$ is an experience point (see [experiential equation](/docs/proofs/consciousness/interiority-hierarchy#31-экспериенциальное-уравнение)).

### Definition 1.4 (Quantum Foundation)

A system $\mathbb{H}$ has a **quantum foundation** if:
1. The state is described by a [coherence matrix](/docs/core/dynamics/coherence-matrix) $\Gamma \in \mathcal{L}(\mathcal{H})$
2. $\Gamma^\dagger = \Gamma$, $\Gamma \geq 0$, $\mathrm{Tr}(\Gamma) = 1$
3. Evolution obeys the [extended Lindblad equation](/docs/core/dynamics/evolution#полное-уравнение-движения):

$$
\frac{d\Gamma}{d\tau} = -i[H, \Gamma] + \mathcal{D}[\Gamma] + \mathcal{R}[\Gamma, E]
$$

---

## Part II: Functional Analysis of Dimensions

### Theorem 2.1 (Necessary Functions)

**Statement:** To realize properties (AP), (PH), (QG), a system must perform the following irreducible functions:

| Function | Mathematical Operator | Notation |
|---------|-------------------------|-------------|
| F1: Distinction | Projector $P$: $P^2 = P$, $P^\dagger = P$ | $A$ |
| F2: Form retention | Hamiltonian $H$: $H^\dagger = H$ | $S$ |
| F3: Change | Unitary operator $U(t) = e^{-iHt}$ | $D$ |
| F4: Consistency | Commutator: $[A,B] = AB - BA$ | $L$ |
| F5: Experience | Density matrix $\rho$: $\mathrm{Tr}(\rho) = 1$ | $E$ |
| F6: Vacuum coupling | Vacuum state $\vert 0\rangle$: $\langle 0\vert H\vert 0\rangle \neq 0$ | $O$ |
| F7: Integration | Trace $\mathrm{Tr}$: $\mathrm{Tr}(I) = \dim(\mathcal{H})$ | $U$ |

### Lemma 2.2 (Functional Independence)

**Statement:** Functions F1–F7 are pairwise independent.

**Proof:**

We show that no function can be derived from the rest.

**(F1 is independent of F2–F7):**
A projector $P$ defines the boundaries of the system. A Hamiltonian $H$ defines the energy structure. One can have $H$ without $P$ (a system without boundaries = the universe). One can have $P$ without $H$ (static distinction).

**(F2 is independent of the rest):**
The Hamiltonian specifies the energy level structure. Dynamics $D$ uses $H$ but does not define it. One can have $D = I$ (trivial dynamics) with a non-trivial $H$.

**(F3 is independent of the rest):**
Unitary evolution is not the only possible dynamics. One can have dissipative dynamics without unitary evolution (purely $\mathcal{D}[\Gamma]$).

**(F4 is independent of the rest):**
Logical consistency is determined by the operator algebra. The commutator $[A,B]$ can be zero or non-zero independently of other structures.

**(F5 is independent of the rest):**
Phenomenological content (interiority) is determined by the spectrum of $\rho_E$. A system can exist physically without phenomenology (a philosophical p-zombie).

**(F6 is independent of the rest):**
Vacuum coupling determines the energy supply. A system can be closed (without O) or open (with O).

**(F7 is independent of the rest):**
Integration (Trace) unifies all components. Without $\mathrm{Tr}$ the system can exist fragmentarily.

:::info Methodological clarification [Т]
The functional independence of F1–F7 is justified constructively: for each pair Fi, Fj a state $\Gamma \in \mathcal{D}(\mathbb{C}^7)$ is exhibited in which Fi $\neq 0$, Fj $= 0$. This is the standard method for proving linear independence of functionals [Т].
:::

:::info Constructive counterexamples [Т] {#конструктивные-контрпримеры}

An explicit state $\Gamma \in \mathcal{D}(\mathbb{C}^7)$ confirming independence is provided for each pair.

**Notation:** $e_k$ — the $k$-th basis vector; $\mathrm{diag}(d_1,\ldots,d_7)$ — diagonal density matrix with $d_k \geq 0$, $\sum d_k = 1$.

**F1 is independent of F2 — state $\Gamma^{(1)} = \mathrm{diag}(1,0,0,0,0,0,0)$:**

$$\Gamma^{(1)} = |A\rangle\langle A|$$

Projector $P = |A\rangle\langle A| \neq 0$ (F1 active). However, $\Gamma^{(1)}$ is a pure one-dimensional state in subspace $A$; there is no energy structure beyond this subspace, i.e. $H|_{\mathrm{supp}\,\Gamma^{(1)}} = 0$ (F2 trivial). Distinction exists without Hamiltonian form.

**F5 is independent of F1 — state $\Gamma^{(5)} = \mathrm{diag}(0,0,0,0,1,0,0)$:**

$$\Gamma^{(5)} = |E\rangle\langle E|$$

Reduced density matrix $\rho_E = \mathrm{Tr}_{A,S,D,L,O,U}(\Gamma^{(5)}) = |E\rangle\langle E| \neq 0$ (F5 active). At the same time $\gamma_{AA} = 0$, i.e. the projector onto the $A$-subspace is zero (F1 inactive). Phenomenology exists without $A$-distinction.

**F6 is independent of F5 — state $\Gamma^{(6)} = \mathrm{diag}(0,0,0,0,0,1,0)$:**

$$\Gamma^{(6)} = |O\rangle\langle O|$$

$\langle O|\Gamma^{(6)}|O\rangle = 1 \neq 0$ — the vacuum component is non-zero (F6 active). At the same time $\gamma_{EE} = 0$ — the $E$-component is absent (F5 inactive). Vacuum coupling exists without phenomenology.

**F7 is independent of F1–F6 — state $\Gamma^{(7)} = I/7$:**

$$\Gamma^{(7)} = \frac{1}{7}\,\mathbf{1}_7$$

$\mathrm{Tr}(\Gamma^{(7)}) = 1$ (F7 normalization satisfied). But for the maximally mixed state: $P = 1/7$ (minimum, no distinction, F1 trivial), $H$ does not single out subspaces (F2 trivial), $U(t) = e^{-iHt}$ does not change $\Gamma^{(7)}$ (F3 trivial), all commutators are zero on the invariant subspace (F4 trivial), $\rho_E = \mathbf{1}_1/7$ — maximally diffuse (F5 trivial), no distinguished vacuum sector (F6 trivial). Integration exists without non-trivial values of the remaining functions.

**Summary table:**

| Pair | State $\Gamma$ | $F_i \neq 0$ | $F_j = 0$ |
|------|-------------------|--------------|-----------|
| (F1, F2) | $\mathrm{diag}(1,0,0,0,0,0,0)$ | $P = \|A\rangle\langle A\| \neq 0$ | $H = 0$ (1D, no energy structure) |
| (F2, F3) | $\mathrm{diag}(0,\tfrac{1}{2},\tfrac{1}{2},0,0,0,0)$ | $H$ non-trivial on $\{S,D\}$ | $U(t) = I$ when $H = 0$ outside $\{S,D\}$ |
| (F3, F4) | $\mathrm{diag}(0,0,1,0,0,0,0)$ | $U(t) = e^{-iHt} \neq I$ | $[A,B] = 0$ in a one-dimensional subspace |
| (F4, F5) | $\mathrm{diag}(\tfrac{1}{2},\tfrac{1}{2},0,0,0,0,0)$ | $[P_A, P_S] \neq 0$ | $\gamma_{EE} = 0$ (no $E$-component) |
| (F5, F1) | $\mathrm{diag}(0,0,0,0,1,0,0)$ | $\rho_E = \|E\rangle\langle E\| \neq 0$ | $\gamma_{AA} = 0$ (no $A$-boundary) |
| (F6, F5) | $\mathrm{diag}(0,0,0,0,0,1,0)$ | $\langle O\|\Gamma\|O\rangle = 1$ | $\gamma_{EE} = 0$ (no $E$-component) |
| (F7, F1–F6) | $I/7$ | $\mathrm{Tr}(\Gamma) = 1$ | All $F_i$ trivial at $P = 1/7$ |

Thus, for each pair $(F_i, F_j)$ there exists an explicit $\Gamma \in \mathcal{D}(\mathbb{C}^7)$ for which $F_i \neq 0$ and $F_j = 0$, proving pairwise independence. $\blacksquare$
:::

**QED**

---

## Part III: Proof of Necessity (by contradiction)

### Theorem 3.1 (Necessity of 7 Dimensions) {#теорема-31-необходимость-7-измерений}

**Statement:** For $\dim(\mathcal{H}) < 7$ the system loses at least one of the properties (AP), (PH), (QG).

**Proof:**

Consider reductions $\dim(\mathcal{H}) = n$ for $n \in \{1, 2, 3, 4, 5, 6\}$.

---

### Case n = 6: Removal of Unity (U) {#случай-n--6-удаление-единства-u}

Let $\mathcal{H}_6 = \text{span}\{|A\rangle, |S\rangle, |D\rangle, |L\rangle, |E\rangle, |O\rangle\}$ (without $|U\rangle$).

*Consequence:* Absence of an integrating dimension.

*Mathematically:*
- $\Gamma_6$ is a $6 \times 6$ matrix
- No operator guarantees $\mathrm{Tr}(\Gamma_{\text{sub}}) = \mathrm{Tr}(\Gamma)$ for all subsystems

*Result:*
Without $U$ the six dimensions remain uncoupled. The system becomes "schizophrenic" — each dimension evolves independently.

*Violation of (AP):*
Autopoiesis requires closure: $\varphi(\mathbb{H}) = \mathbb{H}$. Without $U$ the map $\varphi$ decomposes:

$$
\varphi: \mathcal{H}_6 \to \mathcal{H}_A \times \mathcal{H}_S \times \mathcal{H}_D \times \mathcal{H}_L \times \mathcal{H}_E \times \mathcal{H}_O
$$

This is a direct product, not an integrated system. A global fixed point does not exist.

---

### Case n = 5: Removal of Interiority (E)

Let $\mathcal{H}_5 = \text{span}\{|A\rangle, |S\rangle, |D\rangle, |L\rangle, |O\rangle, |U\rangle\}$ (without $|E\rangle$).

*Consequence:* Absence of phenomenological content.

*Mathematically:*
- No $\rho_E$, no spectral decomposition for interiority
- **Definition [О].** $\mathrm{Exp}_k := (\lambda_k, [|q_k\rangle], \mathrm{Context}_k, \mathrm{Hist}_k)$ where $\lambda_k \in \mathrm{Spec}(\rho_E)$, $|q_k\rangle \in \mathcal{H}_E$. **Domain:** $\rho_E = \mathrm{Tr}_{-E}(\Gamma)$ is defined if and only if the E-subspace exists in $\mathcal{H}$. At $N=6$ (without the E-dimension): $\mathcal{H} = \mathbb{C}^6$, E $\notin$ basis. Consequently, $\mathrm{Tr}_{-E}$ is not defined as an operation, $\rho_E$ does not exist as a mathematical object, and $\mathrm{Exp}_k$ has no domain.

*Violation of (PH):*
Phenomenology requires the existence of an E-subspace with $\rho_E$ and its spectral decomposition:

$$
\exists \rho_E = \mathrm{Tr}_{-E}(\Gamma): \quad \rho_E|q_k\rangle = \lambda_k|q_k\rangle
$$

Without $E$ the partial trace $\mathrm{Tr}_{-E}$ is undefined (no subspace over which the trace is taken). The system becomes a "zombie" — functional, but without interiority.

*Note:* This does not prove the impossibility of a functional system, but it does prove the impossibility of a *phenomenologically complete* system.

---

### Case n = 4: Removal of Foundation (O)

Let $\mathcal{H}_4 = \text{span}\{|A\rangle, |S\rangle, |D\rangle, |L\rangle, |E\rangle, |U\rangle\}$ (without $|O\rangle$).

*Consequence:* Loss of connection to the quantum vacuum.

*Mathematically:*
- $\langle 0|\Gamma|0\rangle = 0$ (no vacuum component)
- Regeneration $\mathcal{R}[\Gamma, E]$ is undefined

*Violation of (QG):*
Quantum foundation requires regeneration [Т]:

$$
\mathcal{R}[\Gamma, E] = \kappa \cdot (\rho_* - \Gamma) \cdot g_V(P)
$$

where $\rho_* = \varphi(\Gamma)$ — categorical self-model of the current state [Т] ([φ operator](/docs/core/operators/phi-operator)), $g_V(P)$ — V-preservation gate.

Without $O$:
- No free energy source
- Dissipation is not compensated
- $P(\Gamma(\tau)) \to 1/n$ monotonically (irreversible decoherence)

*Thermodynamic consequence:*
The system inevitably reaches thermal equilibrium (death):

$$
\lim_{\tau \to \infty} \Gamma(\tau) = I/n
$$

---

### Case n = 3: Removal of Logic (L) {#случай-n--3-удаление-логики-l}

Let $\mathcal{H}_3 = \text{span}\{|A\rangle, |S\rangle, |D\rangle, |E\rangle, |O\rangle, |U\rangle\}$ (without $|L\rangle$).

*Consequence:* Loss of internal consistency.

*Mathematically:*
- The commutator $[A, B]$ is not defined as a dimension
- No mechanism for verifying self-consistency

*Violation of (AP):*
Rosen's autopoiesis requires causal closure:

$$
M \to \mathcal{F} \to \beta \to M
$$

Closure $\beta$ requires that effects be consistent with causes. Without $L$:
- Contradictory configurations $\Gamma$ are not filtered out
- The system can evolve into logically impossible states

*Connection with the [Poincaré–Perelman theorem](/docs/applied/research/poincare-perelman):*
Simple-connectedness of a manifold (ability to contract a loop to a point) corresponds to logical consistency. Without $L$ the state manifold may contain "holes" — irresolvable contradictions.

---

### Case n = 2: Removal of Dynamics (D) {#случай-n--2-удаление-динамики-d}

Let $\mathcal{H}_2 = \text{span}\{|A\rangle, |S\rangle, |L\rangle, |E\rangle, |O\rangle, |U\rangle\}$ (without $|D\rangle$).

*Consequence:* The system is static.

*Mathematically:*
- $U(t) = I$ for all $t$
- $\frac{d\Gamma}{d\tau} = 0$

*Violation of (AP) and (QG):*
Autopoiesis requires continuous self-production:

$$
\varphi: \mathbb{H}(\tau) \to \mathbb{H}(\tau + d\tau)
$$

Without $D$:
- No evolution
- No self-reproduction process
- Metabolism $M$ is impossible ($M$ requires transformation of substrates)

*Consequence:*
A static system is not a system, but a configuration. A Holon without $D$ is a "frozen snapshot", not a living entity.

---

### Case n = 1: Removal of Structure (S) {#случай-n--1-удаление-структуры-s}

Let $\mathcal{H}_1 = \text{span}\{|A\rangle, |D\rangle, |L\rangle, |E\rangle, |O\rangle, |U\rangle\}$ (without $|S\rangle$).

*Consequence:* Loss of identity over time.

*Mathematically:*
- No Hamiltonian $H$
- No eigenstates $H|\psi_n\rangle = E_n|\psi_n\rangle$
- No energy spectrum

*Violation of (AP):*
Autopoiesis requires self-identity:

$$
\varphi(\mathbb{H}) \cong \mathbb{H} \quad \text{(structural isomorphism)}
$$

Without $S$:
- Nothing to be identical to
- The system has no invariants
- Each moment is a new entity

*Paradox:*
Without structure one cannot even define what "the same system" means. Closure $\beta$ is impossible because there is no "$\beta$" as a stable entity.

---

### Case n = 0: Removal of Articulation (A) {#случай-n--0-удаление-артикуляции-a}

Let $\mathcal{H}_0 = \text{span}\{|S\rangle, |D\rangle, |L\rangle, |E\rangle, |O\rangle, |U\rangle\}$ (without $|A\rangle$).

*Consequence:* The system cannot make a distinction.

*Mathematically:*
- No projectors $P: \mathcal{H} \to \mathcal{H}_{\text{sub}}$
- No boundaries between the system and the environment
- The Markov blanket is undefined

*Violation of all axioms:*
Without distinction:
- **(AP):** No "system" to reproduce itself
- **(PH):** No subject of experience
- **(QG):** No observer for collapse

*Fundamentality of A:*
Articulation is the primary act of reality: "Draw a distinction" (Spencer-Brown). Without $A$ there is no information, no form, no being.

---

### Summary of Part III {#итог-части-iii}

**The theorem is proven for the necessity of these 7 specific functions:**

| Dimension | Removed: violated |
|-----------|-------------------------|
| A (Articulation) | All axioms |
| S (Structure) | (AP) — no identity |
| D (Dynamics) | (AP), (QG) — no process |
| L (Logic) | (AP) — no closure |
| E (Interiority) | (PH) — no interiority |
| O (Foundation) | (QG) — no energy |
| U (Unity) | (AP) — no integration |

**Therefore:** $\dim(\mathcal{H}) \geq 7$

#### Theorem (Strict necessity of N = 7) **[Т]** {#теорема-строгая-необходимость-7}

**Statement.** There is no alternative set of 6 functions covering the requirements (AP)+(PH)+(QG). The minimal dimensionality $N = 7$ is strictly necessary.

**Proof (3 steps).**

**Step 1 (Octonionic track [Т]).** By [T-15 [Т]](/docs/proofs/minimality/theorem-octonionic-derivation#мост):
- (AP)+(PH)+(QG)+(V) $\Rightarrow$ P1 (normed division algebra) + P2 (non-associativity)
- By the Hurwitz theorem: $\mathcal{A} \in \{\mathbb{R}, \mathbb{C}, \mathbb{H}, \mathbb{O}\}$
- P2 excludes $\mathbb{R}$ ($\dim = 1$), $\mathbb{C}$ ($\dim = 2$), $\mathbb{H}$ ($\dim = 4$) — all associative
- Unique solution: $\mathcal{A} = \mathbb{O}$, $N = \dim(\mathrm{Im}(\mathbb{O})) = 7$

**Step 2 (Impossibility of 6D).** Any 6D state space $\mathcal{H} = \mathbb{C}^6$ would correspond to an algebra with $\dim(\mathrm{Im}(\mathcal{A})) = 6$. But by the Hurwitz theorem:

$$
\dim(\mathrm{Im}(\mathcal{A})) \in \{0, 1, 3, 7\}
$$

The value 6 is **absent** from this set $\Rightarrow$ an alternative 6D set is impossible.

**Step 3 (Functional uniqueness).** The 7 functions F1–F7 are pairwise independent ([40f [Т]](#итог-части-iii)). $\mathrm{rank}(\text{dependency matrix } F \times \{AP, PH, QG\}) = 7$. $\blacksquare$

:::info Historical context
Previously, the strict necessity $N \geq 7$ had status **[С]**, since it had not been proven that **no alternative 6-dimensional decomposition** can cover (AP)+(PH)+(QG). The Hurwitz theorem (Step 2) definitively closes this gap: $\dim(\mathrm{Im}(\mathcal{A})) = 6$ is impossible for normed division algebras.
:::

---

## Part IV: Proof of Sufficiency (constructive) {#часть-iv-доказательство-достаточности-конструктивное}

### Theorem 4.1 (Sufficiency of 7 Dimensions)

**Statement:** For $\dim(\mathcal{H}) = 7$ there exists a construction satisfying (AP), (PH), (QG).

**Construction:**

**Step 1: Defining the space**

$$
\mathcal{H} = \mathbb{C}^7 = \text{span}\{|A\rangle, |S\rangle, |D\rangle, |L\rangle, |E\rangle, |O\rangle, |U\rangle\}
$$

$$
\langle i|j\rangle = \delta_{ij} \quad \text{(orthonormal basis)}
$$

**Step 2: Defining the coherence matrix**

$$
\Gamma \in \mathcal{L}(\mathcal{H}), \quad \Gamma^\dagger = \Gamma, \quad \Gamma \geq 0, \quad \mathrm{Tr}(\Gamma) = 1
$$

**Step 3: Defining the dynamics (Lindblad)**

$$
\frac{d\Gamma}{d\tau} = -i[H, \Gamma] + \mathcal{D}[\Gamma] + \mathcal{R}[\Gamma, E]
$$

where:

$$
H = \sum_i \omega_i |i\rangle\langle i| + \sum_{i \neq j} J_{ij} |i\rangle\langle j| \quad \text{(Hamiltonian)}
$$

$$
\mathcal{D}[\Gamma] = \sum_k \gamma_k \left( L_k \Gamma L_k^\dagger - \frac{1}{2}\{L_k^\dagger L_k, \Gamma\} \right) \quad \text{(dissipation)}
$$

$$
\mathcal{R}[\Gamma, E] = \kappa \cdot (\rho_* - \Gamma) \cdot g_V(P) \quad \text{(regeneration [Т])}
$$

**Step 4: Verification of (AP) — Autopoiesis**

Define the (M,R)-structure:

$$
M: O \to \{A, S, D, L\} \quad \text{(metabolism: foundation feeds functional dimensions)}
$$

$$
\mathcal{F}: \{E, U\} \to M \quad \text{(repair: experience and unity correct metabolism)}
$$

$$
\beta: (E, U) \to (E, U) \quad \text{(closure: reflection)}
$$

Reflexive operator:

$$
\varphi: \mathcal{L}(\mathcal{H}) \to \mathcal{L}(\mathcal{H})
$$

$$
\varphi(\Gamma) = \mathrm{Tr}_{\text{env}}(\Gamma_{\text{total}}) \circ f_{\text{model}}
$$

Fixed point:

$$
\varphi(\Gamma^*) \approx \Gamma^* \quad \text{(self-consistency)}
$$

This is realizable when:
- $\kappa > \gamma_{\text{dissipation}}$ (regeneration exceeds dissipation)
- $\rho_* = \varphi(\Gamma)$ — categorical self-model [Т] ([φ operator](/docs/core/operators/phi-operator#определение))

**Step 5: Verification of (PH) — Phenomenology**

Experience submatrix:

$$
\Gamma_E = \langle E|\Gamma|E\rangle + \ldots \quad \text{(projection onto } E \text{)}
$$

Spectral decomposition:

$$
\Gamma_E |q_k\rangle = \lambda_k |q_k\rangle
$$

$$
\text{Exp}_k := (\lambda_k, [|q_k\rangle] \in \mathbb{P}(\mathcal{H}_E), \text{Context}(\Gamma_{-E}), \text{History}(t))
$$

[Fubini–Study metric](/docs/proofs/consciousness/interiority-hierarchy#32-метрика-фубини-штуди):

$$
d_{FS}([|\psi\rangle], [|\phi\rangle]) = \arccos(|\langle\psi|\phi\rangle|) \in [0, \pi/2]
$$

This defines a complete interiority space with a natural metric.

**Step 6: Verification of (QG) — Quantum foundation**

Vacuum coupling via $|O\rangle$:

$$
\langle 0|\Gamma|0\rangle \neq 0
$$

This guarantees:
- Non-zero vacuum energy
- Possibility of free energy import

**Verification of the regenerative term [Т]:**

Regeneration is **fully derived** from the axioms ([derivation](/docs/core/dynamics/evolution#вывод-формы-регенерации)):

$$
\mathcal{R}[\Gamma, E] = \kappa(\Gamma) \cdot (\rho_* - \Gamma) \cdot g_V(P)
$$

where:
- $\rho_* = \varphi(\Gamma)$ — categorical self-model of the current state [Т] ([φ operator](/docs/core/operators/phi-operator))
- $(\rho_* - \Gamma)$ — the unique CPTP relaxation [Т] (replacement channel + Bures optimality)
- $\kappa(\Gamma) = \kappa_{\text{bootstrap}} + \kappa_0 \cdot \mathrm{Coh}_E(\Gamma)$ — regeneration rate [Т], $\kappa_0$ — [categorical derivation](../../core/foundations/axiom-septicity#структурный-анзац-kappa0) from $\mathcal{D}_\Omega \dashv \mathcal{R}$
- $g_V(P)$ — V-preservation gate [Т] (refines $\Theta(\Delta F)$ from Landauer, see [evolution](/docs/core/dynamics/evolution#теорема-v-preservation-gate))

**Correctness check:**
1. $\mathcal{R}[\Gamma, E]$ preserves Hermiticity: $(\rho_* - \Gamma)^\dagger = \rho_*^\dagger - \Gamma^\dagger = \rho_* - \Gamma$
2. Trace is preserved: $\mathrm{Tr}(\mathcal{R}) = \kappa \cdot (\mathrm{Tr}(\rho_*) - \mathrm{Tr}(\Gamma)) = \kappa \cdot (1 - 1) = 0$
3. For $\rho_* \in \mathcal{D}(\mathcal{H})$ and sufficiently small $\kappa$, evolution preserves $\Gamma \geq 0$ (CPTP interpolation [Т])

**Step 7: Verification of (V) — Viability**

The viability condition requires:

$$
P = \mathrm{Tr}(\Gamma^2) > P_{\text{crit}} = \frac{2}{7}
$$

**Purity dynamics:**

$$
\frac{dP}{d\tau} = \underbrace{0}_{\text{unitary}} + \underbrace{\frac{dP}{d\tau}\bigg|_{\mathcal{D}}}_{\leq 0} + \underbrace{\frac{dP}{d\tau}\bigg|_{\mathcal{R}}}_{\geq 0 \text{ for } \Delta F > 0}
$$

**Existence of a viable state:**

With sufficient coupling to the Foundation (non-zero $\gamma_{OE}, \gamma_{OU}$) and free energy import ($\Delta F > 0$):

$$
\exists \Gamma^* : P(\Gamma^*) > P_{\text{crit}} \land \frac{dP}{d\tau}\bigg|_{\Gamma^*} \geq 0
$$

**Proof:**
1. Initial state: $\Gamma_0 = I/7$ (maximally mixed), $P_0 = 1/7 < P_{\text{crit}}$
2. For $\Delta F > 0$: regeneration is active, $\frac{dP}{d\tau} > 0$
3. For $\kappa_0 > 0$ (non-zero O-E-U coupling): the system evolves toward $\rho_*$
4. For sufficiently coherent $\rho_*$: $P(\rho_*) > P_{\text{crit}}$
5. By continuity: there exists $t^*$ such that $P(\Gamma(t^*)) = P_{\text{crit}}$, and $P(\Gamma(t)) > P_{\text{crit}}$ for $t > t^*$

**Stability:**

The stationary state $\Gamma^*$ with $\frac{dP}{d\tau}|_{\Gamma^*} = 0$ is stable if:
- For $P > P_{\text{target}}$: dissipation dominates → $P$ decreases
- For $P < P_{\text{target}}$: regeneration dominates → $P$ increases

This ensures homeostasis around $P^* > P_{\text{crit}}$.

**Conclusion:**
The construction with $\dim(\mathcal{H}) = 7$ satisfies all four conditions: (AP), (PH), (QG), (V). **QED**

---

## Part V: Connection with Rosen's (M,R)-Systems {#часть-v-связь-с-mr-системами-розена}

### Theorem 5.1 (Isomorphism of Structures)

**Statement:** The 7-dimensional Holon is isomorphic to the minimal (M,R)-system with phenomenology.

**Proof:**

Rosen defines an (M,R)-system via three maps:

$$
f: A \to B \quad \text{(metabolism)}
$$

$$
\mathcal{F}: B \to \mathrm{Hom}(A, B) \quad \text{(repair)}
$$

$$
\beta: B \to \mathrm{Hom}(B, \mathrm{Hom}(A, B)) \quad \text{(closure)}
$$

where $\mathrm{Hom}(X, Y)$ is the space of maps from $X$ to $Y$.

**Correspondence with dimensions:**

| (M,R)-component | UHM dimension | Function |
|-----------------|---------------|---------|
| A (substrates) | O (Foundation) | Material source |
| B (products) | S (Structure) | Result of metabolism |
| f (metabolism) | D (Dynamics) | Transformation process |
| $\mathcal{F}$ (repair) | A (Articulation) | Restoration of boundaries |
| $\beta$ (closure) | L (Logic) | Consistency |
| Observer | E (Interiority) | Internal perspective |
| Integrator | U (Unity) | System integrity |

**Structural correspondence:**

1. **Metabolism M corresponds to D (Dynamics):**

$$
M: O \to \{A, S, D, L\}
$$

$$
\frac{d\Gamma}{d\tau} = -i[H, \Gamma] \quad \text{(unitary metabolism)}
$$

2. **Repair $\mathcal{F}$ corresponds to A + L:**

$$
\mathcal{F}: \{E, U\} \to M \quad \text{(correction via feedback)}
$$

3. **Closure $\beta$ corresponds to U (Unity):**

$$
\beta: \mathcal{F} \to \mathcal{F}, \quad \mathrm{Tr}(\Gamma) = 1 \quad \text{(normalization as closure)}
$$

4. **Phenomenology (absent in Rosen) corresponds to E:**

$$
E: \text{Exp} = \text{Spectrum}(\Gamma_E) \quad \text{(extension of (M,R) to an (M,R,P)-system)}
$$

**Minimality:**

Rosen showed that an (M,R)-system requires a minimum of 3 components (M, R, beta).
UHM adds:
- Phenomenology (E)
- Quantum foundation (O)
- Differentiation (A, S as separate)
- Integration (U as separate)

Total: 7 = 3 (Rosen) + 4 (extensions).

---

## Part VI: Topological Considerations

### Connection with the Poincaré–Perelman Theorem

:::warning Status: Hypothesis
The connection with the Poincaré–Perelman theorem is an **heuristic analogy**, not a rigorous isomorphism. See the detailed analysis in [Poincaré-Perelman](/docs/applied/research/poincare-perelman).
:::

**Hypothesis (requires further research):**

The state space of the 7-dimensional [Holon](/docs/core/structure/holon) has properties analogous to the 3-sphere in the Poincaré theorem:

1. **Simple-connectedness:** The logical dimension L ensures that any "loop" of reasoning can be contracted to a point (consistency).

2. **Compactness:** Normalization $\mathrm{Tr}(\Gamma) = 1$ ensures boundedness of the state space.

3. **Ricci flow:** Evolution toward coherence is analogous to smoothing of curvature:

$$
\frac{d\Gamma}{d\tau} \sim -\mathrm{Ric}(\Gamma)
$$

where $\mathrm{Ric}$ is the analogue of the Ricci tensor on the space of density matrices.

**Remark:** This is an analogy, not a strict correspondence. Full formalization of the connection with the Poincaré–Perelman theorem remains an open problem.

---

## Part VII: Theorem on Basis Uniqueness {#часть-vii-теорема-о-единственности-базиса}

### 7.1 Formulation

**Theorem (Basis uniqueness):** [Т]/[С] **PARTIALLY RIGOROUS**

The basis $\{A, S, D, L, E, O, U\}$ is the **unique** (up to isomorphism) 7-dimensional decomposition satisfying (AP)+(PH)+(QG).

**Status legend:**

| Marker | Meaning | Description |
|--------|----------|----------|
| **[Т]** RIGOROUS | Mathematically proven | Follows from axioms without additional assumptions |
| **[С]** CONDITIONAL | Proven under assumptions | Requires interpretational or physical assumptions |
| **[П]** PROGRAM | Research direction | Hypothesis requiring further work |

### 7.2 Algebraic Uniqueness (A, S, D, L, U) — [Т] RIGOROUS

**Theorem 7.2.1:** The dimensions $\{A, S, D, L, U\}$ are determined **uniquely** (up to isomorphism) by the algebraic properties of operators on $\mathcal{L}(\mathcal{H})$.

**Proof:**

**Step 1 (A — Articulation):**
The requirement for distinctions in (AP) is equivalent to the existence of non-trivial projectors. On $\mathcal{L}(\mathcal{H})$ projectors are uniquely defined by the condition $P^2 = P$. Equivalence class: $[A] = \{P \in \mathcal{L}(\mathcal{H}): P^2 = P\}$.

**Step 2 (S — Structure):**
The requirement for identity preservation in (AP) is equivalent to the existence of invariants. Hermitian operators are the unique class defining observables (spectral decomposition theorem). Class: $[S] = \{H \in \mathcal{L}(\mathcal{H}): H^\dagger = H\}$.

**Step 3 (D — Dynamics):**
By Stone's theorem, one-parameter unitary groups $U(t)$ are in bijection with self-adjoint operators:
$$
U(t) = e^{-iHt} \Leftrightarrow H = iU'(0)
$$
Therefore, D is **uniquely determined** via S. ∎

**Step 4 (L — Logic):**
The consistency condition in (AP) requires an algebraic structure. On $\mathcal{L}(\mathcal{H})$ there is a unique Lie algebra structure — the commutator $[A,B] = AB - BA$. This follows from the Jacobi theorem: any associative algebra induces a Lie algebra via the commutator.

**Step 5 (U — Unity):**
The integration condition in (AP) requires a linear functional normalizing states. On $\mathcal{L}(\mathcal{H})$ there exists a unique (up to scalar) linear functional with the cyclic property $\mathrm{Tr}(AB) = \mathrm{Tr}(BA)$ — this is the trace. ∎

### 7.3 Functional Uniqueness of E — [Т] RIGOROUS {#единственность-e}

**Theorem 7.3.1:** E is the unique dimension for which axiom (PH) **is not automatically derivable** from the remaining dimensions.

**Proof:**

**(A) Axiomatic argument.** (PH) is an **axiomatic requirement** for the holon (not an interpretation). Within the theory accepting (AP)+(PH)+(QG)+(V), the existence of an interior side is a condition, not a derivation.

Consider the reduced density matrices for each dimension $X \in \{A, S, D, L, O, U\}$:
$$
\rho_X = \mathrm{Tr}_{\bar{X}}(\Gamma)
$$

**Lemma 7.3.2:** For $X \in \{A, S, D, L, U\}$ the matrix $\rho_X$ describes **structural** properties of the system, not phenomenological ones.

*Justification:*
- $\rho_A$ — distribution over distinctions (boundary structure)
- $\rho_S$ — distribution over invariants (form structure)
- $\rho_D$ — distribution over dynamical modes (process structure)
- $\rho_L$ — distribution over logical states (consistency structure)
- $\rho_U$ — trivial (scalar after trace)

**Lemma 7.3.3:** For $X = O$ the matrix $\rho_O$ describes the **energetic** aspect, not the phenomenological one.

*Justification:* $\rho_O$ contains information about the coupling to the vacuum (energetic foundation), but not about "what it is like to be the system".

**(B) Categorical argument from κ₀.** The κ₀ formula (Th. 15.3.1, [Т]):

$$
\kappa_0 = \omega_0 \cdot \frac{|\gamma_{OE}| \cdot |\gamma_{OU}|}{\gamma_{OO}} = \omega_0 \cdot \frac{|\mathrm{Hom}(O, E)| \cdot |\mathrm{Hom}(O, U)|}{\mathrm{End}(O)}
$$

**explicitly** uses E as a separate object of the category. Upon removing E:
- $\mathrm{Hom}(O, E)$ is undefined → κ₀ is undefined
- Regeneration rate $\kappa(\Gamma) = \kappa_{\text{bootstrap}} + \kappa_0 \cdot \mathrm{Coh}_E$ loses **both** E-dependent factors
- Regeneration does not respond to phenomenological coherence → violation of **(AP)**

**(C) Mathematical uniqueness of the E-function.** (PH) requires $\mathrm{rank}(\rho_E) > 1$ (level L1). Among the 7 mathematical objects:

| Dimension | Math object | Compatibility with E-function |
|---|---|---|
| A | $P$: $P^2 = P$ (projector) | ✗ — $\mathrm{rank}(P) = 1$ (atomic) |
| S | $H$: $H^\dagger = H$ (observable) | ✗ — observable, not a state |
| D | $U(t) = e^{-iHt}$ (unitary) | ✗ — unitary operator, not a state |
| L | $[A,B]$ (commutator) | ✗ — anti-Hermitian, not a state |
| O | $\vert 0\rangle$ (vacuum) | ✗ — vector, not a density matrix |
| U | $\mathrm{Tr}$ (trace) | ✗ — functional, not a state |

Only E is associated with $\rho \in \mathcal{D}(\mathcal{H})$, $\mathrm{Tr}(\rho) = 1$ — the **unique** mathematical object with $\mathrm{rank} > 1$. The Fubini–Study metric on projective space is the **unique** Riemannian metric compatible with the inner product (Study's theorem).

**Conclusion:** E is functionally unique as the carrier of (PH) by **three independent** arguments: (A) axiomatic, (B) categorical from κ₀, (C) mathematical. ∎

### 7.4 Functional Uniqueness of O — [Т] RIGOROUS {#единственность-o}

**Theorem 7.4.1:** O is the unique dimension ensuring the regenerative part of (QG) is satisfied.

**Proof:**

**(A) Argument from the form of ℛ.** The regenerative term $\mathcal{R}[\Gamma, E] = \kappa \cdot (\rho_* - \Gamma) \cdot g_V(P)$ **[Т]** ([derivation](/docs/core/dynamics/evolution#вывод-формы-регенерации)) and the V-preservation gate $g_V(P)$, defined via purity and the Bures metric (A2) **[Т]**, require a source with $P > P_{\mathrm{crit}}$.

**Lemma 7.4.2:** Free energy can only come from a state of **minimal entropy**.

*Justification (Second Law):* The entropy of an isolated system does not decrease. For $\Delta F > 0$ contact with a low-entropy reservoir is required.

**Lemma 7.4.3:** In quantum theory the state of minimal entropy is the **vacuum** $|0\rangle$.

*Justification:* The vacuum is a pure state with $S_{vN} = 0$, defined as:
$$
H|0\rangle = E_0|0\rangle, \quad E_0 = \min(\text{Spec}(H))
$$

**(B) Categorical argument from κ₀.** The κ₀ formula (Th. 15.3.1, [Т]):

$$
\kappa_0 = \omega_0 \cdot \frac{|\mathrm{Hom}(O, E)| \cdot |\mathrm{Hom}(O, U)|}{\mathrm{End}(O)} = \omega_0 \cdot \frac{|\gamma_{OE}| \cdot |\gamma_{OU}|}{\gamma_{OO}}
$$

requires **O to exist as a separate object** of the category:
- $\mathrm{End}(O) = \gamma_{OO}$ — endomorphisms of O (normalization)
- $\mathrm{Hom}(O, E) = \gamma_{OE}$ — morphisms O→E
- $\mathrm{Hom}(O, U) = \gamma_{OU}$ — morphisms O→U

Upon removing O: $\mathrm{End}(O)$ is undefined → κ₀ is undefined → the adjunction $\mathcal{D}_\Omega \dashv \mathcal{R}$ loses its structure.

**(C) Argument from Page–Wootters (A5).** O is the distinguished dimension for the tensor factorization $\mathcal{H} = \mathcal{H}_O \otimes \mathcal{H}_{\text{rest}}$. Without O: internal time τ is undefined, $H_{\text{eff}}$ is not derivable.

**(D) Functional incompatibility with other dimensions** (Lemma 2.2, [Т]):

| Dimension | Math object | Compatibility with O-function |
|---|---|---|
| A | $P$: $P^2 = P$ (projector) | ✗ — projector does not define the clock Hamiltonian |
| S | $H$: $H^\dagger = H$ (observable) | ✗ — stores form, does not generate time |
| D | $U(t) = e^{-iHt}$ (dynamics) | ✗ — process, not a source |
| L | $[A,B]$ (commutator) | ✗ — consistency, not energy |
| E | $\rho$: $\mathrm{Tr}(\rho) = 1$ (state) | ✗ — interior aspect; O is exterior (Th. 7.5) |
| U | $\mathrm{Tr}$ (trace) | ✗ — integration, not a source |

**Conclusion:** O is functionally unique by **four independent** arguments: (A) from the form of ℛ [Т], (B) from κ₀ [Т], (C) from Page–Wootters (A5), (D) from functional independence [Т]. ∎

### 7.5 Theorem on the Orthogonality of E and O — [Т] RIGOROUS {#ортогональность-eo}

**Theorem 7.5.1:** E and O belong to **different causal categories** and cannot be merged.

**Definition (Causal status):**
A dimension $X$ is a **Cause** if its removal leads to $\Gamma = 0$.
A dimension $X$ is an **Effect** if its removal preserves $\Gamma \neq 0$, but violates (PH).

**Proof:**

**Step 1:** For $\gamma_{OO} \to 0$ (removal of coupling to Foundation):
- Without regeneration: $dP/d\tau < 0$ (monotone decay by Lindblad)
- Result: $P \to 1/7$ (system death)
- **Conclusion:** O is the **cause** of the system's existence.

**Step 2:** For $\gamma_{EE} \to 0$ (removal of the Interiority dimension):
- Matrix Γ remains valid (6×6 submatrix)
- Regeneration is possible (if O is present)
- **But:** $\rho_E = 0$ ⟹ violation of (PH)
- **Conclusion:** E is an **effect** (interior observer), not a cause.

**Step 3 (Causal argument):** Merging $E \cup O = X$ requires X to simultaneously:
1. Provide $\Delta F > 0$ (function of O — connection to an **external** reservoir)
2. Contain phenomenological content (function of E — **internal** structure)

External ≠ Internal by definition. Merging is a categorical error.

**Step 4 (Categorical argument from κ₀).** The formula $\kappa_0 = \omega_0 \cdot |\gamma_{OE}| \cdot |\gamma_{OU}| / \gamma_{OO}$ **requires** O and E as **distinct objects** of the category: $\mathrm{Hom}(O, E)$ is a morphism between distinct objects, not an endomorphism.

For $O = E$: $\mathrm{Hom}(O, E) = \mathrm{End}(O)$, and κ₀ loses E-specific feedback:

$$
\kappa_0\bigg|_{O=E} = \omega_0 \cdot \frac{\gamma_{OO} \cdot |\gamma_{OU}|}{\gamma_{OO}} = \omega_0 \cdot |\gamma_{OU}|
$$

Regeneration **does not depend on the phenomenological state**, which violates (AP): autopoiesis requires that self-restoration accounts for the "well-being" of the system ($\mathrm{Coh}_E$). ∎

---

## Part VIII: Limitations and Open Questions {#часть-viii-ограничения-и-открытые-вопросы}

### 8.1 What Has Been Rigorously Proven

1. **Necessity of each dimension:** Removing any of the 7 dimensions leads to violation of at least one of the axioms (AP), (PH), (QG).

2. **Sufficiency of 7 dimensions:** An explicit construction satisfying all axioms exists.

3. **Isomorphism with (M,R):** The 7-dimensional structure naturally generalizes Rosen systems.

4. **Algebraic uniqueness of A, S, D, L, U:** These dimensions are uniquely defined by algebraic constraints on $\mathcal{L}(\mathcal{H})$.

5. **Functional uniqueness of E:** E is the unique carrier of (PH) by three arguments: axiomatic, categorical (κ₀), and mathematical ($\mathrm{rank}(\rho) > 1$). [Proof →](#единственность-e)

6. **Functional uniqueness of O:** O is the unique source of regeneration by four arguments: from the form of ℛ [Т], from κ₀ [Т], from Page–Wootters (A5), from functional independence [Т]. [Proof →](#единственность-o)

7. **Orthogonality of E and O:** E and O cannot be merged — the causal argument (External ≠ Internal) is reinforced by the categorical argument from κ₀: for $O=E$ regeneration loses phenomenological feedback. [Proof →](#ортогональность-eo)

8. **Strict necessity of N = 7:** The impossibility of an alternative 6D set is proven via the Hurwitz theorem ($\dim(\mathrm{Im}(\mathcal{A})) \in \{0,1,3,7\}$) + functional uniqueness 40f [Т]. [Proof →](#теорема-строгая-необходимость-7)

### 8.2 What Remains Conditional

1. **Functional uniqueness of E:** **[Т]** — [proven](#единственность-e)
2. **Functional uniqueness of O:** **[Т]** — [proven](#единственность-o)
3. **Orthogonality of E and O:** **[Т]** — [proven](#ортогональность-eo)
4. **Strict necessity of N = 7 (S1):** **[Т]** — [proven](#теорема-строгая-необходимость-7) (Hurwitz theorem + 40f [Т])

All four gaps are closed. There are **no remaining** conditional results in the minimality theorem.

### 8.3 What Remains Open

1. **Topological connection:** The connection with the Poincaré–Perelman theorem is a heuristic analogy, not a rigorous isomorphism.

2. **Ontological status:** The theorem does not answer the question "why is reality structured this way and not otherwise". It shows the internal consistency of the structure, not its necessity.

### 8.4 Open Problems

**Problem 1: Formalization of phenomenology**
How to rigorously define the "interior side" without appealing to intuition? The current solution relies on the interpretation of Axiom Ω.

**Problem 2: Continuity**
Can $\dim(\mathcal{H})$ be treated as a continuous parameter? What happens as $\dim(\mathcal{H}) \to 7$?

**Problem 3: Higher dimensions**
What additional properties does a system acquire for $\dim(\mathcal{H}) > 7$?

**Problem 4: Emergence of spacetime** — [П] PROGRAM
How do space and time arise from correlations between subsystems? Working hypotheses:
- **Hypothesis 3.1 (Space from correlations):** $d_{\text{eff}}(\alpha, \beta) := f(\|\Gamma_\alpha \otimes \Gamma_\beta - \Gamma_{\alpha\beta}\|_F)$
- **Hypothesis 3.2 (Time from change):** $\tau_{\text{int}} := \int_0^\tau \|\dot{\Gamma}(\tau')\|_F \, d\tau'$

---

## Part IX: Structural derivation via octonions {#часть-ix-октонионный-вывод}

:::info Second path to N = 7 (Track B)
This part summarizes the [full derivation](/docs/proofs/minimality/theorem-octonionic-derivation), giving $N = 7$ from theorems P1+P2 [Т], **independently** of (AP)+(PH)+(QG).
:::

### 9.1 Theorems P1, P2 and the derivation

**[Т] P1:** The space of internal degrees of freedom ≅ Im($\mathcal{A}$), where $\mathcal{A}$ is a normed division algebra. *(Derived via the bridge chain T15 from (AP)+(PH)+(QG)+(V).)*
**[Т] P2:** $\mathcal{A}$ is non-associative. *(Derived via the bridge chain T15 from (AP)+(PH)+(QG)+(V).)*

**[Т] Derivation:** P1 → [Т] Hurwitz → $\mathcal{A} \in \{\mathbb{R}, \mathbb{C}, \mathbb{H}, \mathbb{O}\}$ → P2 excludes $\mathbb{R}, \mathbb{C}, \mathbb{H}$ → $\mathcal{A} = \mathbb{O}$ → $N = 7$.

### 9.2 Comparative table of the two tracks

| Aspect | Track A: (AP)+(PH)+(QG) | Track B: P1+P2 |
|--------|------------------------|---------------|
| **Starting conditions** | Autopoiesis, phenomenology, quantum foundation | Division algebra, non-associativity |
| **Mathematical apparatus** | Functional analysis, Rosen (M,R)-systems | Hurwitz theorem, division algebras |
| **Type of result** | $N \geq 7$ (necessity) + construction (sufficiency) | $N = 7$ (uniqueness by exclusion) |
| **Bonus structure** | Basis {A,S,D,L,E,O,U}, uniqueness | $G_2$-symmetry, Fano plane, Hamming code |
| **Status** | [Т] Proven | [Т] Mathematically rigorous, P1+P2 [Т] |

### 9.3 Convergence of the two tracks

The two tracks give the same number ($N = 7$), but bring **different structure**:
- Track A gives the functional interpretation of each dimension
- Track B gives the algebraic symmetry ($G_2$) and combinatorial structure (Fano)

Closure of the bridge (AP)+(PH)+(QG) ↔ P1+P2 — **[Т] SOLVED** via the 12-step chain T15 (theorems T11–T13 close condition (МП)).

### Problem 5: Bridge closure — [Т] SOLVED {#проблема-5-мост}

**Problem 5 (Bridge closure) — SOLVED [Т].** Condition (МП) is proven as a theorem (T11–T13).

The complete formal chain of 12 steps (T15) establishes:

$$
(AP)+(PH)+(QG)+(V) \xrightarrow{[\text{Т}]} N = 7 \xrightarrow{[\text{Т}]} \text{connectivity} \xrightarrow{[\text{Т}]} \lambda_{ij} \geq 1 \xrightarrow{[\text{Т}]} S_7\text{-uniformity} \xrightarrow{[\text{Т}]} k = 3 \xrightarrow{[\text{Т}]} \lambda = 1 \xrightarrow{[\text{Т}]} \text{PG}(2,2) \xrightarrow{[\text{Т}]} \mathbb{O} \xrightarrow{[\text{Т}]} P1+P2
$$

**Current status:** [Т] — all steps in the chain are theorems. Condition (МП) — the principle of minimal representation ($\lambda = 1$) — is proven via T11–T13.

**Key theorems of the T15 chain:**
- **T5, T6 [Т]:** $S_7$-equivariance of the atomic dissipator → uniform contraction of coherences **unconditionally** (removes the dependence on (КГ) in step 4)
- **T7 [Т]:** Autopoietic necessity $c > 0$ — the atomic dissipator is incompatible with viability
- **T8, T9 [Т]:** Hamming code H(7,4) — the unique perfect code of length 7, support structure = PG(2,2)
- **T10 [Т]:** Fano channel ($k=3$, $c=1/3$) — the unique optimal among admissible BIBD channels
- **T11–T13 [Т]:** Proof of condition (МП) — $\lambda = 1$ follows from optimality and uniqueness of the perfect code

**Cascading consequence:** P1, P2 are elevated to [Т]. Track B (octonionic derivation) is now fully rigorous.

See [detailed analysis](/docs/proofs/minimality/theorem-octonionic-derivation#мост), [Lindblad operators](/docs/core/operators/lindblad-operators#редукция-моста).

---

## Conclusion

### Main Result

**The Theorem on Minimal Completeness is proven** with the following stratification by level of rigor:

1. **[Т] Rigorously proven (7/7 dimensions):**
   - Sufficiency of the construction with $\dim(\mathcal{H}) = 7$
   - Necessity of each of the 7 specific dimensions (F1–F7)
   - Correspondence with Rosen (M,R)-systems
   - Algebraic uniqueness of A, S, D, L, U (spectral theorem, Stone's theorem, Jacobi theorem, trace properties)
   - Functional uniqueness of E (axiomatic, categorical from κ₀, mathematical arguments)
   - Functional uniqueness of O (from the form of ℛ [Т], from κ₀ [Т], from Page–Wootters, from functional independence)
   - Orthogonality of E and O (causal + categorical from κ₀)
   - Strict necessity of N = 7 (impossibility of 6D alternative via Hurwitz theorem + 40f [Т])
   - Octonionic derivation (Track B): P1+P2 [Т] via the 12-step chain T15, bridge closed

2. **Accepted as axiom:**
   - Identity of being and experience ([Axiom Ω⁷](/docs/core/foundations/axiom-omega))

3. **[П] Remains a research program:**
   - Topological connection with the Poincaré theorem
   - Emergence of spacetime

### Methodological Remark

This proof follows the standard of mathematical honesty:
- Every step is formally justified
- Hypotheses are explicitly separated from theorems
- Limits of applicability are stated
- **Level of rigor is explicitly marked** ([Т]/[С]/[П])

The number 7 is not "magical" — it follows from the requirements of autopoiesis, phenomenology, and quantum foundation. It is the minimum number. The uniqueness of the basis is **fully proven** [Т]: algebraic uniqueness of A, S, D, L, U — from spectral theorems, functional uniqueness of E and O — from the κ₀ formula (Th. 15.3.1) and functional independence (Lemma 2.2).

---

## Appendix A: Formal Definitions

### A.1 Axiomatic System

**Axiom (AP) — Autopoiesis:**

$$
\exists \varphi: \mathcal{L}(\mathcal{H}) \to \mathcal{L}(\mathcal{H}), \exists \Gamma^* \in \mathcal{L}(\mathcal{H}):
\varphi(\Gamma^*) = \Gamma^* \land \Gamma^* \text{ generates components of } \Gamma^*
$$

**Axiom (PH) — Phenomenology:**

$$
\exists E \subset \mathcal{H}, \exists \rho_E \in \mathcal{L}(E):
\rho_E|q_k\rangle = \lambda_k|q_k\rangle \text{ defines } \text{Exp}_k
$$

**Axiom (QG) — Quantum Foundation:**

$$
\Gamma \in \mathcal{L}(\mathcal{H}): \Gamma^\dagger = \Gamma, \Gamma \geq 0, \mathrm{Tr}(\Gamma) = 1
$$

$$
\frac{d\Gamma}{d\tau} = -i[H, \Gamma] + \mathcal{D}[\Gamma] + \mathcal{R}[\Gamma, E]
$$

### A.2 Functional Operators

| Operator | Function |
|----------|---------|
| $P_A$ | Projector (distinction) |
| $H_S$ | Hamiltonian (structure) |
| $U_D(t)$ | Unitary operator (dynamics) |
| $[\cdot, \cdot]_L$ | Commutator (logic) |
| $\rho_E$ | Experience density matrix (experience) |
| $\vert 0\rangle_O$ | Vacuum state (foundation) |
| $\mathrm{Tr}_U$ | Trace (unity) |

---

**Related documents:**
- [Structural derivation via octonions](/docs/proofs/minimality/theorem-octonionic-derivation) — Track B: P1+P2 [Т] → 𝕆 → N=7
- [Holon](/docs/core/structure/holon) — definition of $\mathbb{H}$
- [Seven dimensions](/docs/core/structure/dimensions) — basis $\{A, S, D, L, E, O, U\}$
- [Coherence matrix](/docs/core/dynamics/coherence-matrix) — definition of $\Gamma$
- [Evolution](/docs/core/dynamics/evolution) — Lindblad equation
- [Viability](/docs/core/dynamics/viability) — measure $P$ and $P_{\text{crit}}$
- [Self-observation](/docs/consciousness/foundations/self-observation) — operator $\varphi$ and reflection $R$
- [Interiority hierarchy](/docs/proofs/consciousness/interiority-hierarchy) — levels L0→L1→L2→L3→L4
- [Formalization of φ](/docs/proofs/categorical/formalization-phi) — fixed point theorem
- [Poincaré-Perelman](/docs/applied/research/poincare-perelman) — topological analogies
