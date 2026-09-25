---
slug: /proofs/physics/physics-correspondence
sidebar_position: 1
title: "Correspondence with Physics"
description: Formal connection of UHM with fundamental physical theories
---

# UHM Correspondence with Fundamental Physics

## Section Status

:::info Section Status
The main results are formalized and proven **[T]**: L-unification, reduction of the evolution equation to the von Neumann equation (Theorem 3.1), emergent geometry ($M^4$), Einstein equations, SM gauge group. No-signalling is proven as the marginal identity of Theorem 8.1; for the full nonlinear dynamics it holds only in the non-selective reading of §8.5 [C]. The category equivalence of §3.3 and the computational bound of §8.6 are retracted. An earlier version of this box listed "reduction to QM" and "no-signaling" among the [T] results without these limits; that is retracted. Open directions: concrete SM parameters, non-perturbative partition function.
:::

## Contents

1. [Categorical Structure of Connections](#1-категорная-структура-связей)
2. [L-Unification: the Logical Origin of Physics](#2-l-унификация)
3. [Reduction to Quantum Mechanics](#3-редукция-к-квантовой-механике)
4. [Emergent Geometry](#4-эмерджентная-геометрия)
5. [Connection to General Relativity](#5-связь-с-общей-теорией-относительности)
6. [Gauge Symmetries and the Standard Model](#6-калибровочные-симметрии-и-стандартная-модель)
7. [Correspondence of 7 Dimensions to Physical Structures](#7-соответствие-7-измерений-физическим-структурам)

---

## 1. Categorical Structure of Connections {#1-категорная-структура-связей}

:::info L-unification as the foundation
The entire categorical structure connecting UHM with physics is based on **L-unification** — the derivation of Lindblad operators from the subobject classifier Ω. This provides a **unified logical foundation** for all physical theories.
:::

### 1.1 Hierarchy of Physical Categories

**Definition 1.1 (Category hierarchy).**
UHM generates the following commutative diagram of categories:

```
      Sh_∞(C)
         │
         │ Ω (classifier)
         ▼
                    π_QM
      Hol ─────────────────────▶ QM
       │                         │
       │ π_Class                 │ ℏ→0
       ▼                         ▼
    DensityMat ────────────────▶ ClassMech
                    ℏ→0
       │
       │ π_Space [C] (T-119, T-120)
       ▼
    Riem (M⁴ = ℝ × Σ³)
```

**Key role of Ω:**
- The ∞-topos $\text{Sh}_\infty(\mathcal{C})$ contains the classifier Ω
- Lindblad operators are derived from Ω: $L_k = \sqrt{\chi_{S_k}}$
- All physical dynamics is determined by the logical structure of Ω

where:
- $\mathbf{Hol}$ — category of [Holons](/docs/core/structure/holon)
- $\mathbf{QM}$ — category of quantum-mechanical systems
- $\mathbf{DensityMat}$ — category of [density matrices](/docs/core/dynamics/coherence-matrix)
- $\mathbf{ClassMech}$ — category of classical mechanical systems
- $\mathbf{Riem}$ — category of Riemannian manifolds ($M^4$ assembled at T-120 [C]: an aperiodic clock and the open reconstruction axioms of T-119)

### 1.2 Forgetful Functor

**Definition 1.2 (Forgetful functor).**

$$
\mathcal{U}: \mathbf{Hol} \to \mathbf{DensityMat}
$$

is defined on objects:

$$
\mathcal{U}(\mathbb{H}) := \Gamma_{\mathbb{H}}^{(7)}
$$

and on morphisms:

$$
\mathcal{U}(f: \mathbb{H}_1 \to \mathbb{H}_2) := \Phi_f
$$

where $\Phi_f$ is the CPTP channel induced by morphism $f$.

**[T] Theorem 1.1 (Functoriality of forgetting).**
$\mathcal{U}$ is a functor preserving identities and composition.

*Proof:* Direct consequence of the definition of morphisms in $\mathbf{Hol}$ as CPTP channels preserving structure. ∎

---

## 2. L-Unification: the Logical Origin of Physics {#2-l-унификация}

:::info Central result
**L-unification** is the key achievement of UHM, showing that Lindblad operators $L_k$ (which define dissipative dynamics) are **derived** from the subobject classifier Ω, not postulated.

This means: **physical dynamics has a logical origin**.
:::

### 2.1 Dependency Hierarchy

**[T] Theorem 2.0 (Derivation chain).**
Fundamental physical objects are derived in the following order:

```mermaid
graph LR
    O["Ω — subobject<br/>classifier"] --> CHI["χ_S — characteristic<br/>morphisms"]
    CHI --> LK["L_k = √χ_Sₖ<br/>Lindblad operators"]
    LK --> LO["ℒ_Ω — logical<br/>Liouvillian"]
    LO --> PHI["φ — self-modeling<br/>operator"]

    style O fill:#e1f5fe
    style LK fill:#fff3e0
    style PHI fill:#e8f5e9
```

**Definitions:**

1. **Ω** — subobject classifier of the ∞-topos $\text{Sh}_\infty(\mathcal{C})$
2. **χ_S: Γ → Ω** — characteristic morphism for the subobject $S \hookrightarrow \Gamma$
3. **L_k = √χ_{S_k}** — Lindblad operators, where $\{S_k\}$ are atoms of the classifier
4. **ℒ_Ω** — logical Liouvillian constructed from $\{L_k\}$
5. **φ** — self-modeling operator from the dynamics of ℒ_Ω

### 2.2 Logical Liouvillian

**[T] Theorem 2.0.1 (Logical Liouvillian).**
Dissipative dynamics is defined via the logical structure of Ω:

$$
\mathcal{L}_\Omega[\Gamma] = -i[H_{eff}, \Gamma] + \sum_k \gamma_k \left( L_k \Gamma L_k^\dagger - \frac{1}{2}\{L_k^\dagger L_k, \Gamma\} \right)
$$

where $L_k = \sqrt{\chi_{S_k}}$, $\{S_k\}$ are atoms of Ω.

*Proof:* See [Axiom Ω⁷](/docs/core/foundations/axiom-omega#внутренняя-логика). ∎

### 2.3 Physical Interpretation

**[T] Theorem 2.0.2 (Dissipation as logical uncertainty).**
The dissipative term $\mathcal{D}[\Gamma]$ reflects the **logical uncertainty** of the state relative to the structure of distinctions of Ω:

$$
\mathcal{D}[\Gamma] = \sum_k \gamma_k \cdot \text{(interaction of Γ with atom } S_k \text{ of classifier Ω)}
$$

*Physical consequence:* Decoherence is not external noise, but the **internal logical dynamics** of the system.

### 2.4 Constructive Algorithms

L-unification provides **computable** formulas:

```verum
/// χ_S: Γ → Ω for the subobject S.
public pure fn characteristic_morphism<const N: Int>(
    gamma: &StaticMatrix<Complex, N, N>,
    s:     &Subspace<N>,
) -> StaticMatrix<Complex, N, N>
{
    let p_s = projector_onto_subspace(s);
    p_s.matmul(&gamma).matmul(&p_s)
}

/// L_k = √χ_{S_k} for atoms of Ω. For basis projectors √P = P, so L_k = χ_k.
public pure fn lindblad_from_omega<const N: Int>(_gamma: &StaticMatrix<Complex, N, N>)
    -> [StaticMatrix<Complex, N, N>; N]
{
    (0..N).map(|k| {
        let mut chi_k = StaticMatrix<Complex, N, N>.zeros();
        chi_k[k, k] = Complex.one();        // atom = basis projector
        chi_k
    }).to_array()
}
```

**See:** [Constructive Algorithms](/docs/reference/computational#конструктивные-алгоритмы-из-l-унификации)

### 2.5 Connection to Physical Theories

| Physical theory | How L-unification explains it | Status |
|-----------------|-------------------------------|--------|
| Quantum decoherence | Dissipation = logical uncertainty relative to Ω | [T] |
| Second law of thermodynamics | $dS/dt \geq 0$ for the unital part $\mathcal{L}_0$ (Hermitian Lindblad operators); with regeneration the Lyapunov functional is the free energy (T-261) | [T] |
| Measurement in QM | Reduction = projection onto atom χ_{S_k} | [T] |
| Arrow of time | Monotone in the parameter $t$ of the dissipative semigroup; not supplied by the ▷-clock (T-53b) | [T] in $t$; [C] as emergent |

---

## 3. Reduction to Quantum Mechanics {#3-редукция-к-квантовой-механике}

:::info Connection to L-unification
Reduction to standard QM occurs when the **logical structure Ω trivializes**: at $R_\varphi \to 0$ the system loses its capacity for self-modeling, and the dissipative dynamics ℒ_Ω reduces to purely unitary.
:::

### 3.1 Limit Functor

**[T] Theorem 3.1 (Reduction to the Schrödinger equation).**
Let $\mathbb{H}$ be a Holon with $R_\varphi \to 0$. Then the [evolution equation](/docs/core/dynamics/evolution) with [emergent internal time](/docs/proofs/dynamics/emergent-time) τ:

$$
\frac{d\Gamma(\tau)}{d\tau} = -i[H_{eff}, \Gamma(\tau)] + \mathcal{D}[\Gamma] + \mathcal{R}[\Gamma, E]
$$

reduces to the von Neumann equation:

$$
\frac{d\rho}{dt} = -i[H, \rho]
$$

for mixed states, or to the Schrödinger equation:

$$
i\hbar\frac{d|\psi\rangle}{dt} = H|\psi\rangle
$$

for pure states $\Gamma = |\psi\rangle\langle\psi|$.

*Proof:*

1. At $R_\varphi \to 0$ the system has no significant self-modeling
2. The regenerative term $\mathcal{R}[\Gamma, E] \propto \kappa(\Gamma) \to 0$ as $\kappa_0 \to 0$, where $\kappa_0 = \|\mathrm{Nat}(\mathcal{D}_\Omega, \mathcal{R})\|$ — [categorical derivation](/docs/core/foundations/axiom-septicity#структурный-анзац-kappa0)
3. The dissipative term $\mathcal{D}[\Gamma] = \mathcal{L}_\Omega[\Gamma] + i[H_{eff}, \Gamma] \to 0$ for isolated systems (the logical structure Ω "freezes")
4. The unitary term remains: $\frac{d\Gamma(\tau)}{d\tau} = -i[H_{eff}, \Gamma]$, where $H_{eff}$ is the [effective Hamiltonian](/docs/core/dynamics/evolution#вывод-h_eff)
5. For $\Gamma = |\psi\rangle\langle\psi|$: $\frac{d|\psi\rangle\langle\psi|}{dt} = |d\psi\rangle\langle\psi| + |\psi\rangle\langle d\psi|$
6. Substituting into the equation: $i\hbar\frac{d|\psi\rangle}{dt} = H|\psi\rangle$ ∎

**Interpretation via L-unification:** Unitary QM is the limit in which the logical structure Ω is fully determined and admits no uncertainty (all $\chi_{S_k}$ are trivial).

### 3.2 Category of Quantum-Mechanical Systems

**Definition 3.1 (Category QM).**

$$
\mathrm{Ob}(\mathbf{QM}) = \{(\mathcal{H}, H, \rho_0) : \mathcal{H} \text{ is a Hilbert space}, H = H^\dagger, \rho_0 \text{ — initial state}\}
$$

$$
\mathrm{Mor}_{\mathbf{QM}}((H_1, \rho_1), (H_2, \rho_2)) = \{U : U^\dagger U = I, U\rho_1 U^\dagger = \rho_2\}
$$

### 3.3 Reduction Functor

**Definition 3.2 (Reduction functor).**

$$
\pi_{\text{QM}}: \mathbf{Hol}_{R \to 0} \to \mathbf{QM}
$$

$$
\pi_{\text{QM}}(\mathbb{H}) := (\mathcal{H}_{\mathbb{H}}, H_{\mathbb{H}}, \Gamma_{\mathbb{H}})
$$

:::warning Retracted: Theorem 3.2 (Equivalence of categories $\mathbf{Hol}_{R=0} \simeq \mathbf{QM}$) [✗]
An earlier version stated as [T] that $\pi_{\text{QM}}|_{\mathbf{Hol}_{R=0}}$ is an equivalence of categories. It is not. Essential surjectivity fails: $\mathbf{QM}$ contains a qubit and the state $I/7$ with $P = 1/7$, while objects of $\mathbf{Hol}$ are seven-dimensional with $P > 2/7$, and unitary isomorphisms preserve dimension and purity (under $R = 1/(7P) \geq 1/7$ the category $\mathbf{Hol}_{R=0}$ is even empty). "At $R = 0$ morphisms are unitary" is not justified: the replacement channel onto a fixed point of self-modelling is a non-unitary morphism of $\mathbf{Hol}$. Full faithfulness was asserted without a functor on morphisms. What holds is an identification by definition of the unitary part of $\mathbf{Hol}$ with the full subcategory of $\mathbf{QM}$ on seven-dimensional systems with $P > 2/7$ [D]. Details: [reduction to QM, §4.2](/docs/physics/quantum-mechanics/qm-reduction#4-функтор-редукции).
:::

### 3.4 Taxonomy of Physical Systems via L-Unification

**[I] Theorem 3.3 (Classification by $R$ and structure of Ω).** (Status [I]: under the master definition $R = 1/(7P) \in [1/7, 1]$ the row $R = 0$ describes no state; the table is a classification scheme. An earlier label [T] is retracted.)

| Parameter $R$ | Structure of Ω | Dynamics | Physical system |
|---------------|---------------|----------|-----------------|
| $R = 0$ | Trivial (all χ_S defined) | $\frac{d\Gamma}{dt} = -i[H, \Gamma]$ | Unitary QM (quarks, leptons, bosons) |
| $R \ll 1/3$ | Partially defined | $\frac{d\Gamma}{dt} = -i[H, \Gamma] + \mathcal{L}_\Omega[\Gamma]$ | Open QM (atoms in a medium) |
| $R \geq 1/3$ | Reflexive (Ω models itself) | Full equation with $\mathcal{R}[\Gamma, E]$ | Living systems (cells, organisms) |

**Physical consequence:** The difference between "dead" and "living" matter lies in the structure of the logical classifier Ω: living systems are capable of modeling their own logical structure.

### 3.6 Discreteness of Time and Page–Wootters

:::info Connection to L-unification
In [Axiom Ω⁷](/docs/core/foundations/axiom-omega), time is **derived** from the [Page–Wootters mechanism](/docs/proofs/dynamics/emergent-time) via the **temporal modality ▷** on the classifier Ω.

$$
\tau_n = \rhd^n(\text{now}), \quad n \in \mathbb{Z}_7
$$

The discreteness of time is a consequence of the finite structure of Ω.
:::

**[T] Theorem 3.4 (Discreteness of internal time).**
For a finite-dimensional system with $\dim(\mathcal{H}_O) = N$, internal time takes values from the cyclic group:

$$
\tau \in \mathbb{Z}_N = \{0, 1, 2, \ldots, N-1\}
$$

For UHM with $N = 7$: $\tau \in \mathbb{Z}_7$.

*Proof:* Follows from the finite-dimensionality of the [clock algebra](/docs/core/structure/dimension-o#алгебра-часов) $\mathcal{A}_O \cong M_7(\mathbb{C})$. ∎

**Physical consequences:**

| Consequence | Formula | Status |
|-------------|---------|--------|
| Quantum of time (chronon) | $\delta\tau = 2\pi/(7\omega_0)$ | [T] Corollary |
| Continuous limit | $N \to \infty \Rightarrow \tau \in \mathbb{R}$ | [T] Proven |
| Discrete ∞-groupoid | $\mathbf{Exp}^{disc}_\infty$ for $N < \infty$ | [T] [Formalized](/docs/proofs/categorical/categorical-formalism#exp-disc-infty) |

**Connection to the 42D formalism:**

Full Page–Wootters state space:
$$
\mathcal{H}_{total} = \mathcal{H}_O \otimes \mathcal{H}_{6D}, \quad \dim = 7 \times 6 = 42
$$

The minimal 7D formalism is obtained via diagonal embedding — see [Coherence Matrix](/docs/core/dynamics/coherence-matrix#two-levels-of-formalization).

---

## 4. Emergent Geometry {#4-эмерджентная-геометрия}

:::info Connection to L-unification
Spatial geometry emerges from the **structure of distinctions** defined by classifier Ω. The metric reflects the "logical distance" between configurations Γ.
:::

### 4.1 Space as a Structure of Distinctions

**[T] Theorem (Spatial metric, T-119).**
In the thermodynamic limit $M \to \infty$, the macroscopic algebra of observables in the $\{A,S,D\}$-sector is commutative (T-117 [T]). By Gelfand–Naimark duality it is isomorphic to $C(\Sigma^3)$ for the unique smooth compact 3-manifold $\Sigma^3$.

The metric on $\Sigma^3$ is induced by the Connes distance from the spectral triple. See [Emergent Manifold $M^4$](/docs/proofs/physics/emergent-manifold#теорема-эмерджентное-пространство).

### 4.2 Pre-metric on the State Space

**[T] Theorem 4.1 (Frobenius metric).**
The space $\mathcal{D}(\mathcal{H})$ of density matrices with metric

$$
d_F(\rho_1, \rho_2) := \|\rho_1 - \rho_2\|_F = \sqrt{\mathrm{Tr}((\rho_1 - \rho_2)^2)}
$$

is a complete metric space.

*Proof:* The Frobenius norm is the Hilbert–Schmidt norm, inducing a complete metric on $\mathcal{L}(\mathcal{H})$. Restriction to $\mathcal{D}(\mathcal{H})$ (a closed subset) preserves completeness. ∎

### 4.3 Information Geometry

**[T] Quantum Fisher metric (standard result).**
The natural Riemannian metric on $\mathcal{D}(\mathcal{H})$ is the quantum Fisher metric:

$$
g_{ij}^{(F)}(\rho) = \frac{1}{2}\mathrm{Tr}\left(\rho\{L_i, L_j\}\right)
$$

where $L_i$ are logarithmic derivatives: $\partial_i \rho = \frac{1}{2}\{\rho, L_i\}$. The unique monotone Chentsov metric on the space of quantum states (Petz, 1996).

### 4.4 Emergent Dimensionality

**[C] Theorem (Dimension 3+1, T-119 + T-120).**

The dimension of macroscopic space is derived under named conditions (the heading read [T] until 2026-09-25):
- $\dim(\Sigma^3) = 3$ — from the rank count of T-119, Step 2c′ (T-119 [C]); the axis triple $\{A,S,D\}$ is not an $SU(3)$ sector (row 48a, retracted), and reading the colour triplet as space is [I]
- Lorentzian signature $(+,-,-,-)$ — [C] (registry row T-53): one time direction [T] (PW clock), three spatial directions at T-119 ($S^3$), the sign at reflection positivity (bounded-below PW generator / Osterwalder–Schrader; Krein route). KO-dimension does not fix the signature, and the KO-dimension-6 claim for $\mathbb{C}^7$ is retracted
- Product $M^4 = \mathbb{R} \times \Sigma^3$ — T-120 [C], at an aperiodic clock and the open reconstruction axioms of T-119 (an earlier line derived it "from the sector decomposition $7 = 1_O \oplus 3 \oplus \bar{3}$ (T-120 [T])"; the axis-labelled decomposition is retracted, row 48a)

See [Emergent Manifold](/docs/proofs/physics/emergent-manifold)

---

## 5. Connection to General Relativity {#5-связь-с-общей-теорией-относительности}

:::tip Status: Einstein equations [T] on the product triple; the derivation of $M^4$ [C]
The Einstein equations are obtained from the spectral action (T-65 [T]), and the cosmological constant is computed (T-65 [T]); the manifold $M^4$ on which they live is assembled from the categorical structure only under two conditions — an aperiodic clock and the open reconstruction axioms of T-119 (T-120 [C]). An earlier version read "fully formalized [T] … the manifold $M^4$ is derived (T-120 [T])"; retracted with the status of T-120.
:::

### 5.1 Emergent Manifold

**[C] Theorem (Product of spectral triples, T-120)** — at an aperiodic clock (T-118) and the open reconstruction axioms of T-119; the heading read [T] until 2026-09-25.
In the thermodynamic limit the effective spectral triple factorizes:

$$
(C^\infty(M^4) \otimes A_{\text{int}},\; L^2(M^4,S) \otimes H_{\text{int}},\; D_{M^4} \otimes 1 + \gamma_5 \otimes D_{\text{int}})
$$

where $M^4 = \mathbb{R} \times \Sigma^3$ is assembled from the categorical structure under these conditions, not postulated. See [Emergent Manifold](/docs/proofs/physics/emergent-manifold#теорема-произведение-троек).

### 5.2 Einstein Equations

**[T] Theorem (Spectral action, T-65).**
The Chamseddine–Connes spectral action for the product $M^4 \times F_{\text{int}}$ reproduces:

$$
R_{\mu\nu} - \frac{1}{2}g_{\mu\nu}R + \Lambda g_{\mu\nu} = \frac{8\pi G}{c^4} T_{\mu\nu}
$$

with $G_N = 3\pi/(7 f_2 \Lambda^2)$. Details: [Einstein Equations](/docs/physics/gravity/einstein-equations).

### 5.3 Cosmological Constant

**[T]** The cosmological constant is computed from the Gap of the O-sector: $\Lambda_{\text{Gap}} > 0$ (T-71 [T]), which determines the vacuum topology $\Sigma^3 \cong S^3$ (T-120b [C], inheriting T-119). Details: [Cosmological Constant](/docs/physics/gravity/cosmological-constant).

---

## 6. Gauge Symmetries and the Standard Model {#6-калибровочные-симметрии-и-стандартная-модель}

:::info Section Status
$SU(3)_C$ is the stabiliser of the $O$-direction in $G_2 = \mathrm{Aut}(\mathbb{O})$ [T]; the electroweak factor $SU(2)_L \times U(1)_Y$ comes from the Fano-electroweak construction [C at (FE)], and its uniqueness is [H]. The former sentence — the whole group $SU(3) \times SU(2) \times U(1)$ "derived from $G_2$ via the sector decomposition and spectral triple [T]" — is retracted [✗]: $\mathrm{rank}\,G_2 = 2 < 4$ (registry row T-275), and the axis-labelled decomposition is retracted (row 48a). Specific parameters (masses, mixing angles) — partially derived, partially remain [P].
:::

### 6.1 Symmetries of the Coherence Matrix

**[T] Theorem 6.1 (Unitary symmetry group).**
The symmetry group of $\Gamma$:

$$
\text{Sym}(\Gamma) := \{U \in U(7) : U\Gamma U^\dagger = \Gamma\}
$$

is isomorphic to the stabilizer of $\Gamma$ in $U(7)$.

*Proof:* Direct consequence of the definition. ∎

### 6.2 Gauge Group from $G_2$

**Gauge group: $SU(3)_C$ [T]; $SU(2)_L \times U(1)_Y$ [C at (FE)]; the former theorem is retracted [✗] (2026-09-25).**

Former statement, "[T] Theorem (Gauge group, T-53 + sector decomposition)": from $G_2 = \mathrm{Aut}(\mathbb{O})$ and the sector decomposition $7 = 1_O \oplus 3 \oplus \bar{3}$,

$$
G_2 \supset SU(3) \xrightarrow{\text{Gap hierarchy}} SU(3)_C \times SU(2)_L \times U(1)_Y
$$

Retracted: symmetry breaking leads from a group to a subgroup, and $SU(3)$ (rank 2) has no subgroup $SU(3) \times SU(2) \times U(1)$ (rank 4); neither has $G_2$, since $\mathrm{rank}\,G_2 = 2 < 4$ (I. Todorov, M. Dubois-Violette, *Int. J. Mod. Phys. A* **33**, 1850118 (2018), eq. (4.2); registry row T-275). What holds: $SU(3)_C = \mathrm{Stab}_{G_2}(e_O) \subset G_2$ [T]; $SU(2)_L \times U(1)_Y$ from the Fano-electroweak construction on the Page–Wootters system factor [C at (FE)], acting on a different tensor factor, so that the ranks add to $2 + 2 = 4$; the uniqueness of this group is [H].

Details: [$G_2$-structure](/docs/physics/gauge-symmetry/g2-structure), [Standard Model](/docs/physics/gauge-symmetry/standard-model).

### 6.3 Particles as Configurations Γ

Elementary particles are degenerate ($R \to 0$) configurations $\Gamma$. Three generations of fermions are derived from the triadic Fano structure [T]. Details: [Three Generations of Fermions](/docs/physics/particle-physics/fermion-generations).

---

## 7. Correspondence of 7 Dimensions to Physical Structures {#7-соответствие-7-измерений-физическим-структурам}

:::info Connection to L-unification
Each of the 7 dimensions has a **dual role**: physical (as an operator) and logical (as an aspect of classifier Ω).
:::

### 7.1 Full Correspondence Table

**[T] Theorem 7.1 (Physical operators of dimensions).**

| Dimension | Operator | Physical role | Status |
|-----------|----------|---------------|--------|
| **A** (Articulation) | Projector $P: P^2 = P, P^\dagger = P$ | Quantum measurements, subspace selection | Formalized |
| **S** (Structure) | Hamiltonian $H: H^\dagger = H$ | Energy spectrum, stationary states | Formalized |
| **D** (Dynamics) | $U(\tau) = e^{-iH_{eff}\tau}$, Lindblad operators $L_k$ | Unitary evolution in [internal time](/docs/proofs/dynamics/emergent-time), $H_{eff}$ — [effective Hamiltonian](/docs/core/dynamics/evolution#вывод-h_eff) | Formalized |
| **L** (Logic) | Commutator $[A, B]$, anticommutator $\{A, B\}$ | Lie algebras, Heisenberg uncertainty | Formalized |
| **E** (Interiority) | $\rho_E = \mathrm{Tr}_{-E}(\Gamma)$ | Reduced density matrix | Formalized |
| **O** (Foundation) | $\vert 0\rangle\langle 0\vert$, $E_0 = \frac{1}{2}\hbar\omega$ | Vacuum, zero-point oscillations | Formalized |
| **U** (Unity) | $\mathrm{Tr}(\cdot)$, $P = \mathrm{Tr}(\Gamma^2)$ | Normalization, purity measure | Formalized |

### 7.2 Algebraic Structure

**[T] Theorem 7.2 (Algebra of dimensions).**
The operators of dimensions form an algebra:

$$
\mathcal{A}_{\text{dim}} := \text{span}\{P_A, H_S, U_D, [,]_L, \rho_E, |0\rangle\langle 0|_O, \mathrm{Tr}_U\}
$$

with commutation relations determined by the quantum-mechanical algebra of operators.

### 7.3 Connection to Symmetry Groups

**[T] Theorem (Symmetry group, T-53).**
The full automorphism group $G_2 = \mathrm{Aut}(\mathbb{O})$ acts on the 7 dimensions. The stabilizer of the $O$-direction is $SU(3)$, determining the gauge structure. Each dimension has a dual role: physical (as an operator) and logical (as an aspect of classifier Ω).

---

## 8. No-Signaling {#запрет-сигнализации}

:::info What is proven and what is not
**Proven [T]:** the regenerative term of a holon $A$ leaves the unconditioned reduced state of a distant system $B$ unchanged, $\mathrm{Tr}_A[\tilde{\mathcal{R}}_A[\Gamma_{AB}]] = 0$ (Theorem 8.1), and so do local unitaries at $A$ (Corollary 8.1). **Not proven, and false under the measurement rule the corpus adopts:** that the full nonlinear dynamics forbids signalling. If $A$ performs a projective measurement with the Lüders update of [measurement, Theorem 2.1, step 4](/docs/physics/quantum-mechanics/measurement#2-измерение-из-omega), the state of $B$ becomes one of the conditional states $\rho_B^{(k)}$ with probabilities $p_k$, and the state-dependent regenerative term of $B$ acts on each of them; for a nonlinear term the resulting ensemble depends on what $A$ chose to do (§8.5). No-signalling of the full dynamics holds only in the non-selective reading of NS2, at the price named in §8.5 [C]. An earlier version of this box said that no-signalling is a consequence of the CPTP structure of $\varphi$ and that the nonlinearity "does not violate" it; that is retracted.
:::

### 8.1 Problem Statement

Introducing nonlinearity into quantum mechanics typically violates the no-signaling principle (Gisin, 1990; Polchinski, 1991). The UHM evolution equation contains a nonlinear regenerative term $\mathcal{R}[\Gamma, E]$, where the nonlinearity arises from $\kappa(\Gamma)$ and $\varphi(\Gamma)$.

**The fundamental difference of UHM** from Weinberg's nonlinear QM:

| Property | Nonlinear QM (Weinberg) | UHM |
|----------|-------------------------|-----|
| Defined on | Wave functions $\vert\psi\rangle$ | Density matrices $\Gamma$ |
| Extension to $A \otimes B$ | Not canonical | $\varphi_A \otimes \mathrm{id}_B$ (CPTP) |
| Ensemble dependence | Yes (different decompositions → different evolution) | The map depends on $\Gamma$ alone, but a proper mixture prepared by a remote measurement evolves branch by branch (§8.5) |
| Domain of applicability | All quantum systems | Only autonomous L2+ systems |

### 8.2 Canonical Extension of Regeneration to Composite Systems

**[T] Definition 8.1 (Canonical extension).**

For a composite system $A \otimes B$, where $A$ is an [autonomous holon](/docs/core/foundations/axiom-septicity#определение-автономная-подсистема):

$$
\tilde{\mathcal{R}}_A[\Gamma_{AB}] := \kappa_A(\Gamma_A) \cdot \left((\varphi_A \otimes \mathrm{id}_B)(\Gamma_{AB}) - \Gamma_{AB}\right) \cdot g_V(P_A)
$$

where $\Gamma_A = \mathrm{Tr}_B(\Gamma_{AB})$.

### 8.3 Central Theorem

**[T] Theorem 8.1 (Regeneration of $A$ leaves the marginal of $B$ unchanged).**

For two spatially separated autonomous holons $A$ and $B$ with joint state $\Gamma_{AB}$:

$$
\mathrm{Tr}_A[\tilde{\mathcal{R}}_A[\Gamma_{AB}]] = 0
$$

*Proof:*

$$
\mathrm{Tr}_A[\tilde{\mathcal{R}}_A[\Gamma_{AB}]] = \kappa_A \cdot g_V(P_A) \cdot \left(\mathrm{Tr}_A[(\varphi_A \otimes \mathrm{id}_B)(\Gamma_{AB})] - \mathrm{Tr}_A[\Gamma_{AB}]\right)
$$

For a CPTP channel $\varphi_A$ with Kraus representation $\varphi_A(\cdot) = \sum_m K_m (\cdot) K_m^\dagger$:

$$
\mathrm{Tr}_A[(\varphi_A \otimes \mathrm{id}_B)(\Gamma_{AB})] = \mathrm{Tr}_A\left[\sum_m (K_m \otimes I_B)\Gamma_{AB}(K_m^\dagger \otimes I_B)\right]
$$

$$
= \mathrm{Tr}_A\left[(\sum_m K_m^\dagger K_m \otimes I_B)\Gamma_{AB}\right] = \mathrm{Tr}_A[(I_A \otimes I_B)\Gamma_{AB}] = \Gamma_B
$$

Therefore: $\mathrm{Tr}_A[\tilde{\mathcal{R}}_A[\Gamma_{AB}]] = \kappa_A \cdot g_V(P_A) \cdot (\Gamma_B - \Gamma_B) = 0$. ∎

The identity concerns the unconditioned marginal $\Gamma_B = \mathrm{Tr}_A\Gamma_{AB}$. An earlier title of this theorem, "No-signaling in UHM", claimed more than it proves; see §8.5 for what a measurement at $A$ does.

**[T] Corollary 8.1 (Invariance under local operations).**

For any local unitary operation $U_A$ by Alice, the contribution of $\tilde{\mathcal{R}}_A$ to Bob's state remains zero:

$$
\mathrm{Tr}_A[\tilde{\mathcal{R}}_A[(U_A \otimes I_B)\Gamma_{AB}(U_A^\dagger \otimes I_B)]] = 0
$$

regardless of changes in $\kappa_A$ and $\Delta F_A$.

**[T] Theorem 8.2 (Full evolution of subsystem B).**

The reduced state $\Gamma_B(\tau) = \mathrm{Tr}_A[\Gamma_{AB}(\tau)]$ obeys:

$$
\frac{d\Gamma_B}{d\tau} = \mathrm{Tr}_A[\mathcal{L}_{lin}[\Gamma_{AB}]] + \mathcal{R}_B[\Gamma_B]
$$

where $\mathcal{R}_B[\Gamma_B] = \kappa_B(\Gamma_B) \cdot (\varphi_B(\Gamma_B) - \Gamma_B) \cdot g_V(P_B)$ — depends **only on the local state** $\Gamma_B$.

### 8.4 No-Signaling Conditions (NS1–NS3)

The proof rests on three structural conditions:

| Condition | Statement | Follows from |
|-----------|-----------|-------------|
| **NS1** (Locality of φ) | $\tilde{\varphi}_A = \varphi_A \otimes \mathrm{id}_B$ | [Autonomy (A1)](/docs/core/foundations/axiom-septicity#определение-автономная-подсистема), categorical structure |
| **NS2** (Locality of κ) | $\kappa_A(\Gamma_{AB}) = \kappa_A(\mathrm{Tr}_B(\Gamma_{AB}))$ | [Definition of κ₀](/docs/core/foundations/axiom-septicity#структурный-анзац-kappa0) via local coherences |
| **NS3** (CPTP φ) | $\varphi$ is a CPTP channel | [Definition of φ](/docs/consciousness/foundations/self-observation#оператор-самомоделирования-φ) |

NS2 makes $\kappa_A$ a function of the *unconditioned* marginal. Whether that marginal is updated when a distant partner is measured decides between the two readings of §8.5.

### 8.5 Ensemble Independence {#85-ансамблевая-независимость}

**[D] Theorem 8.3 (The evolution map is a function of $\Gamma$).**

The UHM evolution is defined on the density matrix $\Gamma$, not on its ensemble decomposition.

*Proof:* All components of the equation ($H_{eff}$, $\mathcal{D}_\Omega$, $\kappa$, $\varphi$, $g_V(P)$) are functions of $\Gamma$, not of any specific decomposition $\Gamma = \sum_i p_i |\psi_i\rangle\langle\psi_i|$. ∎ (This holds by the definition of the terms, hence [D].)

:::warning Retracted: "two preparations of the same Γ evolve identically" and "resolving the Gisin problem"
An earlier version concluded from Theorem 8.3 that two different preparations of the same $\Gamma$ evolve identically, and the conclusion of this page called that "resolving the Gisin problem". Both are retracted. A preparation that is a proper mixture — a coin toss, or a measurement on a distant partner with the Lüders update — produces in each run one of the states $\rho_k$, and the regenerative term acts on that state; the ensemble then evolves as $\sum_k p_k\,\Phi_t(\rho_k)$, not as $\Phi_t(\sum_k p_k \rho_k)$, and for a nonlinear $\Phi_t$ the two differ. This is the scenario of N. Gisin ("Weinberg's non-linear quantum mechanics and supraluminal communications", *Phys. Lett. A* **143**, 1 (1990)): $A$ measures one half of an entangled pair in a basis of her choice, the conditional ensemble at $B$ depends on that choice, and a nonlinear local evolution at $B$ turns the difference into different statistics. A map that depends on $\Gamma$ alone can still be nonlinear, and C. Simon, V. Bužek and N. Gisin proved that with Hilbert-space states, the trace rule and no signalling the dynamics must be linear and completely positive (*Phys. Rev. Lett.* **87**, 170405 (2001)).

*Example* (regression check in `website/scripts/check_core_numbers.py`). $A$ is a qutrit, $B$ a holon, the joint state $\tfrac{1}{\sqrt 3}(|0\rangle|e_0\rangle + |1\rangle|e_1\rangle + |2\rangle|e_2\rangle)$. If $A$ does not measure, the state of $B$ is $\rho_B = \tfrac13(|e_0\rangle\langle e_0| + |e_1\rangle\langle e_1| + |e_2\rangle\langle e_2|)$ with $P = 1/3$, and the viability gate $g_V(P) = \mathrm{clamp}(7P - 2, 0, 1)$ equals $1/3$. If $A$ measures in the basis $\{|0\rangle, |1\rangle, |2\rangle\}$, the states of $B$ are the pure $|e_k\rangle\langle e_k|$ with $g_V = 1$. With $\kappa$ fixed, the initial drift of $B$'s averaged state is $\tfrac{\kappa}{3}(\rho_* - \rho_B)$ in the first case and $\kappa(\rho_* - \rho_B)$ in the second: $B$'s statistics depend on whether $A$ measured. With $\kappa$ depending on $\mathrm{Coh}_E$, two measurement bases of $A$ that both leave $B$'s branches pure already give different drifts.
:::

**What would restore no-signalling.** (a) *The non-selective reading* [C]: the nonlinear terms act on unconditioned marginals and never on remotely conditioned sub-ensembles — NS2 kept after a remote measurement. Then no signal passes, but the evolution inside one branch depends on the branches that did not occur; J. Polchinski, who built this construction for Weinberg's nonlinear quantum mechanics, named the price — a channel between branches of the wave function, the "Everett phone" ("Weinberg's nonlinear quantum mechanics and the Einstein–Podolsky–Rosen paradox", *Phys. Rev. Lett.* **66**, 397 (1991)) — and the reading also gives up the Lüders update for remote partners that the corpus uses. (b) *Convex quasi-linearity*: J. Rembieliński and P. Caban showed that deterministic nonlinear evolutions mapping a mixture to a mixture of the images, $f(\lambda\rho_1 + (1-\lambda)\rho_2) = p\,f(\rho_1) + (1-p)\,f(\rho_2)$ for some $p \in [0,1]$, do not allow signalling and "cannot be ruled out by a standard argument" ("Nonlinear evolution and signaling", *Phys. Rev. Research* **2**, 012027 (2020)), and built a nonlinear extension of the Lindblad generator of this kind ("Nonlinear extension of the quantum dynamical semigroup", *Quantum* **5**, 420 (2021), arXiv:2003.09170); A. Kent gave another route ("Nonlinearity without superluminality", *Phys. Rev. A* **72**, 012108 (2005)). The regenerative flow of UHM is not convex quasi-linear: on 30 random pairs of pure states, with the canonical $\kappa(\Gamma)$, $g_V$ and a dephasing linear part, the image of a mixture lies off the segment between the images of its components by 4–26 % of that segment's length (numerical check). Route (b) is therefore not available as the term is written, and the no-signalling statement of UHM is **[C] under the non-selective reading (a)**. Which reading the corpus adopts, and whether $\mathcal{R}$ can be recast in convex quasi-linear form, is an open problem.

### 8.6 Computational Bound {#86-вычислительное-ограничение}

:::warning Retracted: Theorem 8.4 (Absence of computational speedup) [T]
An earlier version stated as a theorem that the nonlinear regenerative term provides no computational speed-up beyond BQP, on four grounds: (1) $\mathcal{R}$ is active only for L2+ systems, qubits have $R \approx 0$; (2) each regeneration step requires $\Delta F > 0$; (3) $\varphi$ does not increase quantum information; (4) decoherence suppresses exponentially small differences. None of the four bounds what a nonlinear evolution can compute, and the claim collides with D. S. Abrams and S. Lloyd, who showed that generic deterministic nonlinear quantum evolution solves NP-complete and #P problems in polynomial time by amplifying exponentially small differences between states ("Nonlinear quantum mechanics implies polynomial-time solution for NP-complete and #P problems", *Phys. Rev. Lett.* **81**, 3992 (1998), arXiv:quant-ph/9801041). (1) restricts which systems are active, not what an active system can do; holons are seven-level systems, and $R = 1/(7P)$ never vanishes. (2) is an energy cost, not a bound on complexity. (3) constrains the channel $\varphi$, while the nonlinearity sits in the scalar weights $\kappa(\Gamma)\,g_V(P(\Gamma))$. (4) states the question rather than answering it: whether the nonlinear term amplifies small differences faster than decoherence erases them. The gate $g_V$ makes the regenerative flow bistable — for $\kappa$ above the existence threshold the dead state $I/7$ (T-148) and the attractor $\rho_*$ (T-96) both attract, and trajectories that start on either side of the boundary between their basins end a finite distance apart however close they started — which is the kind of amplification Abrams and Lloyd use. The theorem is retracted.
:::

**Open question [H].** Whether the regenerative term, under its thresholds and with decoherence, permits a speed-up beyond BQP. The corpus contains neither a proof of the bound nor a construction of the speed-up.

---

## 9. Summary Table of Correspondences

| Physical theory | Connection to UHM | Status | Reference |
|-----------------|-------------------|--------|-----------|
| **L-unification** | Dissipation from logical structure Ω: $L_k = \sqrt{\chi_{S_k}}$ | [T] Proven | §2 |
| **Quantum mechanics** | The equation reduces to the von Neumann equation when $\mathcal{D}$ and $\mathcal{R}$ vanish (Theorem 3.1); the category equivalence $\mathbf{Hol}_{R=0} \simeq \mathbf{QM}$ is retracted (§3.3) | [T] (Theorem 3.1) | §3 |
| **Schrödinger equation** | $\frac{d\Gamma(\tau)}{d\tau} = -i[H_{eff},\Gamma]$ | [T] Proven | Theorem 3.1 |
| **Lindblad equation** | $\mathcal{L}_\Omega[\Gamma]$ — logical Liouvillian from Ω | [T] Formalized | [evolution.md](/docs/core/dynamics/evolution) |
| **Thermodynamics** | $dS_{vN}/dt \geq 0$ for the unital part $\mathcal{L}_0$; with regeneration the free energy is the Lyapunov functional (T-261). (An earlier entry read "$dS_{vN}/dt \geq 0$ from the structure of ℒ_Ω"; that is false for non-unital channels and is retracted.) | [T] Proven | [emergent time §7.1](/docs/proofs/dynamics/emergent-time#7-теорема-о-стреле-времени) |
| **Decoherence** | Logical uncertainty relative to Ω | [T] Formalized | §2.3 |
| **Marginal identity** | $\mathrm{Tr}_A[\tilde{\mathcal{R}}_A[\Gamma_{AB}]] = 0$ | [T] Proven | §8, Theorem 8.1 |
| **No-signalling of the full dynamics** | Holds in the non-selective reading only; fails with the Lüders update (§8.5) | [C] | §8.5 |
| **Ensemble independence** | The evolution map is a function of $\Gamma$; the physical reading "same $\Gamma$, same evolution" is retracted | [D] | §8.5 |
| **Computational bound** | Retracted; open question | [H] | §8.6 |
| **Space** | $\Sigma^3$ from Gelfand–Connes, $M^4 = \mathbb{R} \times \Sigma^3$ | [C] (T-119: first-order condition, Poincaré duality; T-120: also an aperiodic clock) | [T-119, T-120](/docs/proofs/physics/emergent-manifold) |
| **Time** | Cyclic clock τ ∈ ℤ₇ via modality ▷ on Ω [T]; the aperiodic parameter of the dynamics is assumed [C] (T-53b) | [T] / [C] | [emergent-time.md](/docs/proofs/dynamics/emergent-time) |
| **Discreteness of time** | $\tau \in \mathbb{Z}_7$ from the structure of Ω | [T] Corollary | §3.6 |
| **GR / Einstein** | Spectral action → $G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi G T_{\mu\nu}$ | [T] Proven | [T-65](/docs/physics/gravity/einstein-equations) |
| **Standard Model** | $SU(3)_C = \mathrm{Stab}_{G_2}(e_O)$; $SU(2)_L \times U(1)_Y$ from (FE); the former "$G_2 \supset SU(3) \to SU(3)_C \times SU(2)_L \times U(1)_Y$" is retracted (rank) | [T] / [C at (FE)]; uniqueness [H] | [SM](/docs/physics/gauge-symmetry/standard-model) |

---

## Conclusion

### Key Achievement: L-Unification

**L-unification** shows that physical dynamics has a **logical origin**:

$$
\Omega \xrightarrow{\chi_S} L_k = \sqrt{\chi_{S_k}} \xrightarrow{} \mathcal{L}_\Omega \xrightarrow{} \text{Lindblad equation}
$$

This means: **physics is a consequence of the structure of logical distinctions**.

### What Has Been Formalized [T]

1. **L-unification:** Lindblad operators $L_k = \sqrt{\chi_{S_k}}$ are derived from classifier Ω
2. **Logical Liouvillian:** $\mathcal{L}_\Omega[\Gamma]$ defines dissipation via the logical structure
3. **Reduction to QM:** with the dissipator and the regenerator switched off, the UHM equation is the von Neumann equation (Theorem 3.1); the claim that UHM contains quantum mechanics as a category equivalence is retracted (§3.3)
4. **Thermodynamics:** entropy grows under the unital part of ℒ_Ω; the full flow has the free energy as Lyapunov functional
5. **Metric on states:** The Frobenius norm defines a complete metric
6. **Discreteness of time:** $\tau \in \mathbb{Z}_7$ from the temporal modality ▷ on Ω
7. **Marginal identity:** $\mathrm{Tr}_A[\tilde{\mathcal{R}}_A[\Gamma_{AB}]] = 0$ — regeneration of $A$ does not change $B$'s unconditioned marginal; no-signalling of the full dynamics is [C] (§8.5)
8. **Ensemble independence:** the evolution map is defined on $\Gamma$ [D]; the earlier claim that this resolves the Gisin problem is retracted (§8.5)
9. **Computational bound:** retracted; whether $\mathcal{R}$ gives a speed-up beyond BQP is open [H] (§8.6)
10. **Emergent geometry:** $M^4 = \mathbb{R} \times \Sigma^3$ assembled from categorical structure (T-117—T-120) — conditional [C] on an aperiodic clock and the open reconstruction axioms of T-119
11. **Einstein equations:** The spectral action reproduces $G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi G T_{\mu\nu}$ (T-65)
12. **Gauge group:** $SU(3)_C$ from $G_2 = \mathrm{Aut}(\mathbb{O})$ [T]; $SU(2)_L \times U(1)_Y$ from (FE) [C at (FE)]. The former item — the whole group from $G_2$ (T-53) — is retracted (rank $G_2 = 2 < 4$)

### Open Directions

1. **Standard Model parameters:** Specific values of masses and mixing angles from the vacuum configuration $\Gamma_{\text{vac}}$
2. **Non-perturbative partition function:** The limiting transition $Z_N \to Z$ as $N \to \infty$ [P]
3. **Quantum gravity:** The strong-field limit and quantum corrections to the spectral action

:::info Open problem: concrete parameters of the Standard Model
UHM derives the **structure** of the Standard Model: the gauge group $SU(3)_C \times SU(2)_L \times U(1)_Y$ from $G_2$ [T], three generations of fermions from the Fano plane [T], and the Einstein equations from the spectral action [T]. However, **specific parameters** are only partially computed:

| Parameter | Status in UHM | Reference |
|-----------|--------------|-----------|
| Number of generations (3) | **[T] Derived** | [Three Generations](/docs/physics/particle-physics/fermion-generations) |
| Yukawa mass hierarchy | **[T] Derived** | [Yukawa Hierarchy](/docs/physics/particle-physics/yukawa-hierarchy) |
| Electron mass $m_e$ | Not derived | Requires $\Gamma_{\text{vac}}$ |
| Fine structure constant $\alpha$ | Not derived | Requires non-perturbative analysis |
| Exact CKM/PMNS angles | Partial | [CKM Matrix](/docs/physics/particle-physics/ckm-matrix) |

This limitation is **not unique** to UHM: string theory, loop quantum gravity, and IIT also do not derive all SM parameters from first principles.
:::

## $G_2$-Manifolds and M-Theory {#g2-многообразия}

::::info Compactification 11 → 4 + 7 [I]
In the [structural derivation of N=7](../minimality/theorem-octonionic-derivation), the group $G_2 = \text{Aut}(\mathbb{O})$ arises. In M-theory, $G_2$-manifolds play a central role:

**M-theory compactification [I]:**
11-dimensional M-theory admits a compactification $M^{11} = M^4 \times X^7$, where $X^7$ is a compact $G_2$-manifold (holonomy = $G_2$). This gives:
- 4 non-compact dimensions → observable spacetime
- 7 compact dimensions with $G_2$-holonomy → internal degrees of freedom
- $\mathcal{N} = 1$ supersymmetry in 4D (the unique exceptional holonomy preserving exactly 1/8 of supercharges)

**Numerical coincidence [I]:**
- UHM: 7 Holon dimensions, $G_2$-symmetry
- M-theory: 7 internal dimensions, $G_2$-holonomy
- Dimensions coincide: $11 - 4 = 7 = \dim(\text{Im}(\mathbb{O}))$

**Decomposition 42 [I]:**
$\dim(\mathcal{H}_{total}) = 42 = 7 \times 6$ in UHM. In M-theory: $42 = \binom{9}{2} + 6$ arises in a number of contexts.

:::tip Bridge [T] — fully closed (T15)
This is a **substantive analogy**, proven by theorems T1–T15 (the bridge is fully closed). The formal connection between the 7D structure of UHM and the $G_2$-compactification of M-theory is an [open problem](../minimality/theorem-octonionic-derivation#открытые-проблемы). Bridge [T] (closed, T15).
:::

**Potential consequences [I]:**
- If the connection is physical, the $G_2$-manifold determines the gauge group and mass spectrum in 4D
- Singularities of the $G_2$-manifold → non-perturbative effects (condensates)
- Joyce metric on $X^7$ → internal metric of the space of dimensions

[More: structural derivation →](../minimality/theorem-octonionic-derivation)
::::

---

**Related documents:**
- [Axiom Ω⁷](/docs/core/foundations/axiom-omega) — L-unification: Ω → χ_S → L_k → ℒ_Ω → φ
- [Coherence Matrix](/docs/core/dynamics/coherence-matrix) — definition of $\Gamma$, connection between formalisms
- [Evolution](/docs/core/dynamics/evolution) — equation $d\Gamma(\tau)/d\tau$ with derivation of $H_{eff}$
- [Emergent Time](/docs/proofs/dynamics/emergent-time) — Page–Wootters mechanism, temporal modality ▷
- [Emergent Manifold $M^4$](/docs/proofs/physics/emergent-manifold) — derivation of $M^4$ from categorical structure (T-117—T-121)
- [Dimension O](/docs/core/structure/dimension-o) — clock algebra $H_O$, $V_O$, $\mathcal{A}_O$
- [Dimension L](/docs/core/structure/dimension-l) — logical dimension, L = Ω ∩ Γ
- [Constructive Algorithms](/docs/reference/computational#конструктивные-алгоритмы-из-l-унификации) — computation of χ_S, L_k, ℒ_Ω
- [Spacetime](/docs/core/foundations/spacetime) — emergence
- [Categorical Formalism](/docs/proofs/categorical/categorical-formalism) — functor F, $\mathbf{Exp}^{disc}_\infty$
- [Minimality Theorem](/docs/proofs/minimality/theorem-minimality-7) — proof of 7D
- [Coherence Cybernetics](/docs/applied/coherence-cybernetics/axiomatics) — L-unification in CC
- [Theory Boundaries](/docs/reference/falsifiability#границы-теории) — open questions
