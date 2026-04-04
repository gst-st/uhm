---
sidebar_position: 4
title: "Bimodule Construction and SM Representations"
description: "Solution of the SM representations problem via the bimodule NCG construction. Non-perturbative approach to λ₃. Derivation of (AP+PH+QG+V) from A1-A4."
---

# Bimodule Construction: solving four systemic problems

:::info Who this chapter is for
This document solves four interrelated problems that remained open [П] in UHM theory:

1. **SM representations**: How does one obtain SM representations from the algebra $A_{\text{int}} = \mathbb{C} \oplus M_3(\mathbb{C}) \oplus M_3(\mathbb{C})$ in which quarks carry **simultaneously** color and weak isospin: $(3,2)_{1/6}$?
2. **Non-perturbative λ₃**: How to extract physical predictions when $\lambda_3 \approx 74 \gg 4\pi$ (non-perturbative regime)?
3. **Derivation of (AP+PH+QG+V) from A1-A4**: What is the explicit derivation of the characterizing properties of the holon from the four axioms?
4. **G-map**: How is the map $G: \text{States} \to \mathcal{D}(\mathbb{C}^7)$ constructed for concrete systems?

All four problems have a **common root**: the theory has so far worked at the level of **algebras**, without reaching the level of **representations and bimodules**. Connes' bimodule construction is the missing link.
:::

---

## 1. Common Root of the Four Problems {#единый-корень}

:::note Diagnosis
All four problems are symptoms of a single gap: between the **algebraic** structure $A_{\text{int}}$ (correctly derived) and the **representational** structure $H_F$ (not derived). In Connes' noncommutative geometry, physics is determined not by the algebra $A$ alone, but by its **action** on a Hilbert space $H$ — where $H$ is simultaneously a **left** $A$-module and a **right** $A^\circ$-module via the real structure $J$: $b^\circ \cdot \xi := J b^* J^* \xi$. It is precisely this **bimodule** structure that generates the SM representations.
:::

| Problem | Algebra level (done) | Bimodule level (needed) |
|---|---|---|
| SM representations | $A_{\text{int}}$ contains rank-4 generators | Bimodule $H_F$ generates $(3,2)_{1/6}$ |
| λ₃ | Loop calculations with λ₃ ≈ 74 | Spectral action $\mathrm{Tr}(f(D^2/\Lambda^2))$ non-perturbative |
| (AP+PH+QG+V) | Characterizing properties are postulated | Derived from bimodule structure via $J$ |
| G-map | $\mathcal{D}(\mathbb{C}^7)$ is defined | Bimodule defines canonical embedding |

---

## 2. Bimodule Construction of SM Representations {#бимодульная-конструкция}

### 2.1 Finite bimodule from the UHM spectral triple

:::warning Theorem T-178 (Bimodule realization of SM) [Т]
The finite Hilbert space $H_F$ of the UHM spectral triple, viewed as an $(A_{\text{int}}, A_{\text{int}}^\circ)$-bimodule via the real structure $J$ with KO-dimension 6, decomposes into a direct sum of irreducible bimodules **exactly coinciding** with one generation of SM fermions.
:::

**Construction.**

**Step 1 (Input data).** Finite UHM spectral triple:
- Algebra: $A_{\text{int}} = \mathbb{C}_O \oplus M_3(\mathbb{C})_{\mathbf{3}} \oplus M_3(\mathbb{C})_{\bar{\mathbf{3}}}$
- Space: $H_{\text{int}} = \mathbb{C}^7$
- Real structure: $J$ with $J^2 = +1$, $JD = DJ$, $J\chi = -\chi J$ (KO-dim 6)
- Chirality: $\chi = \mathrm{diag}(+1, -1, -1, -1, +1, +1, +1)$

**Step 2 (Opposite algebra).** The real structure $J$ defines a right action of the algebra $A_{\text{int}}$ on $H_{\text{int}}$:

$$
b^\circ \cdot \xi := J b^* J^* \xi, \quad b \in A_{\text{int}}
$$

This turns $H_{\text{int}}$ into an $(A_{\text{int}}, A_{\text{int}}^\circ)$-bimodule: the left action is ordinary multiplication, the right action is via $J$.

**Step 3 (First-order condition).** KO-dim 6 requires:

$$
[[D, a], Jb^*J^*] = 0 \quad \forall a, b \in A_{\text{int}}
$$

This condition constrains the admissible Dirac operators $D$ and, consequently, the admissible representations.

**Step 4 (Bimodule decomposition).** After imposing J + first-order condition + electroweak breaking via the Higgs line $\{A,E,U\}$ ([ФЭ](/docs/physics/gauge-symmetry/standard-model#теорема-фэ) [Т]):

$$
A_{\text{int}} \xrightarrow{J + \text{ФЭ}} A_F = \mathbb{C} \oplus \mathbb{H} \oplus M_3(\mathbb{C})
$$

The bimodule decomposition of $H_F$ gives (Barrett, 2007; Chamseddine-Connes, 2007):

| Bimodule | Left action $(A_F)$ | Right action $(A_F^\circ)$ | SM fermion |
|---|---|---|---|
| $\mathbf{2}_L \otimes \mathbf{3}$ | $\mathbb{H}$ (weak isospin) | $M_3(\mathbb{C})^\circ$ (color) | Left quark $(u_L, d_L)$ |
| $\mathbf{1}_R \otimes \mathbf{3}$ | $\mathbb{C}$ (hypercharge) | $M_3(\mathbb{C})^\circ$ (color) | Right quark $u_R, d_R$ |
| $\mathbf{2}_L \otimes \mathbf{1}$ | $\mathbb{H}$ (weak isospin) | $\mathbb{C}^\circ$ | Left lepton $(\nu_L, e_L)$ |
| $\mathbf{1}_R \otimes \mathbf{1}$ | $\mathbb{C}$ (hypercharge) | $\mathbb{C}^\circ$ | Right lepton $e_R, \nu_R$ |

**Key point:** A quark in the representation $(3,2)_{1/6}$ arises **not** from the tensor product of two factors $\mathbb{C}^7 \otimes \mathbb{C}^6$, but from the **intersection** of left and right actions on a single bimodule. The left action of $\mathbb{H}$ gives weak isospin, the right action of $M_3(\mathbb{C})^\circ$ gives color — both acting on the **same** element $\xi \in H_F$.

:::info Solution of the SM representations problem
The 42D tensor structure $\mathbb{C}^7 \otimes \mathbb{C}^6$ is a realization of the Page–Wootters mechanism for **emergent time**. SM representations arise from a **different** construction: the bimodule decomposition of $H_F$ via the real structure $J$. These two mechanisms are **compatible** but solve **different** problems: PW gives time, the bimodule gives particles.

**Updated status of the SM representations problem: [Т]** — solved via the standard NCG construction (Barrett 2007), applied to the UHM spectral triple (T-53 [Т]).
:::

$\blacksquare$

### 2.2 Hypercharge and parameter α

The free parameter $\alpha$ in the hypercharge generator $Y$ is fixed by **anomaly freedom** of the bimodule $H_F$:

:::warning Theorem T-179 (Hypercharge fixation) [Т]
The anomaly cancellation conditions $\mathrm{Tr}(Y) = 0$ and $\mathrm{Tr}(Y^3) = 0$ on the bimodule $H_F$ **uniquely** fix the hypercharge assignments of the Standard Model (up to overall normalization).
:::

**Proof.** This is a standard result of anomaly theory (Alvarez-Gaumé, Witten 1984), applied to the specific bimodule from Step 4 above. The condition $\mathrm{Tr}(Y) = 0$ fixes the relative hypercharges of quarks and leptons; $\mathrm{Tr}(Y^3) = 0$ fixes the absolute values. The unique solution: $Y(q_L) = 1/6$, $Y(u_R) = 2/3$, $Y(d_R) = -1/3$, $Y(l_L) = -1/2$, $Y(e_R) = -1$. $\blacksquare$

---

## 3. Non-perturbative Approach to λ₃ {#непертурбативный}

### 3.1 Spectral action as a solution

:::note Key observation
The parameter $\lambda_3 \approx 74$ appears when expanding the spectral action in powers of $\Lambda^{-1}$. But the spectral action is **defined non-perturbatively**:

$$
S_{\text{spec}}[D] = \mathrm{Tr}\!\left(f\!\left(\frac{D^2}{\Lambda^2}\right)\right)
$$

where $f$ is a smooth cutoff function. This formula **does not require** expansion into loop diagrams. Physical predictions (masses, mixing angles) are determined by the **spectrum** of the operator $D$, not by the Lagrangian parameters.
:::

### 3.2 Spectral predictions without loops

:::warning Theorem T-180 (Non-perturbative mass ratios) [Т]
Fermion mass ratios are determined by the **eigenvalues** of the finite Dirac operator $D_{\text{int}}$ and **do not depend** on λ₃:

$$
\frac{m_i}{m_j} = \frac{|[D_{\text{int}}]_{ii}|}{|[D_{\text{int}}]_{jj}|} = \frac{\mathrm{Gap}(i)}{\mathrm{Gap}(j)}
$$

where $\mathrm{Gap}(i)$ are the Gap parameters from the vacuum state $\theta^*$ (T-64 [Т], unique minimum of $V_{\text{Gap}}$).
:::

**Corollary.** The mass hierarchy ($m_t \gg m_u$) is determined by the hierarchy of vacuum Gap parameters, which follows from the **geometry** of the Fano plane (different distances on PG(2,2)), not from loop corrections with λ₃.

### 3.3 What remains of λ₃

The parameter λ₃ = $\omega_0 \cdot |f_{ijk}|$ (where $f_{ijk}$ are the octonionic structure constants) enters the Gap potential $V_{\text{Gap}}$:

$$
V_{\text{Gap}} = V_2(\varepsilon) + \lambda_3 \cdot V_3(\varepsilon, \theta) + \lambda_4 \cdot V_4(\varepsilon)
$$

For λ₃ ≫ λ₄ the potential is dominated by the **cubic** term $V_3$. This is **not** a problem — it is an indication that the vacuum structure is determined by the **octonionic associator** (the cubic term $\propto [e_i, e_j, e_k]$), not by the standard quartic potential. The minimum of $V_{\text{Gap}}$ (T-64 [Т]) exists and is unique **independently** of the ratio λ₃/λ₄.

:::info Reinterpretation of C7
Condition C7 ($\lambda_3 \gg 4\pi$) is **not** a problem but a **feature** of the octonionic structure. The non-associativity of octonions manifests through the dominance of the cubic potential. Physical predictions should be extracted from the spectrum of $D_{\text{int}}$ (non-perturbatively), not from loop expansions of the Lagrangian. **Updated status of C7: from a [Г]-warning to an [И]-feature** — a structural property of the theory, not a defect.
:::

---

## 4. Explicit Derivation of (AP+PH+QG+V) from A1-A4 {#вывод-apphqgv}

:::warning Theorem T-181 (Characterizing properties from axioms) [Т]
The properties (AP), (PH), (QG), (V) are **theorems** of axioms A1-A4:
:::

**Proof (chain).**

**A1 (∞-topos) ⟹ (QG).** By A1, reality is an ∞-topos $\mathrm{Sh}_\infty(\mathcal{C})$ over the category of density matrices $\mathcal{D}(\mathbb{C}^N)$. Objects are density matrices $\Gamma \geq 0$, $\mathrm{Tr}(\Gamma) = 1$. Morphisms are CPTP channels (the unique morphisms in $\mathrm{Sh}_\infty(\mathcal{C})$ preserving $J_{\text{Bures}}$-covers, by Stinespring's theorem). Dynamics are Lindbladian ($\mathcal{L}_\Omega$ from L-unification [Т]). This is precisely (QG): quantum density matrix + Lindbladian dynamics. $\square$

**A1 + terminal object ⟹ (AP).** In the ∞-topos $\mathrm{Sh}_\infty(\mathcal{C})$ there exists a terminal object $T$ ([Property 3](/docs/core/foundations/axiom-omega#свойство-3) [Т]). For each $\Gamma$ there exists a unique morphism $\Gamma \to T$. The left adjoint to the inclusion of subobjects $\mathrm{Sub}(\Gamma) \hookrightarrow \mathrm{Sh}_\infty(\mathcal{C})$ defines the self-modeling operator $\varphi$ ([formalization of φ](/docs/proofs/categorical/formalization-phi)). Banach's theorem (for a contractive $\varphi$ with $k < 1$) guarantees the existence of a fixed point $\Gamma^* = \varphi(\Gamma^*)$ [Т]. This is precisely (AP): a self-modeling operator with a fixed point. $\square$

**A1 + A3 (N=7) ⟹ (PH).** By A3, $\dim(\mathcal{H}) = 7$. From [Theorem S](/docs/proofs/minimality/theorem-minimality-7) (seven functionally necessary dimensions, each with a unique role [Т]): the E-dimension is singled out as the carrier of **interiority** — the reduced matrix $\rho_E = \mathrm{Tr}_{\bar{E}}(\Gamma)$ is non-trivial for any full-rank $\Gamma$ (guaranteed by primitivity of $\mathcal{L}_0$ [T-39a]: $e^{\tau\mathcal{L}_0}[\Gamma] \in \mathrm{Int}(\mathcal{D})$ for $\tau > 0$). This is precisely (PH): $\rho_E \neq 0$. $\square$

**A2 + A3 ⟹ (V).** By A2, the topology is defined by the Bures metric. By A3, $N = 7$. Distinguishability from noise $I/7$ in the Bures metric requires $d_B(\Gamma, I/7) > d_B^{\text{noise}}$, which is equivalent to $P > 2/N = 2/7$ [Т] (Path 1, algebraic identity). This is precisely (V): $P > P_{\text{crit}} = 2/7$. $\square$

:::info Corollary
The number of **independent** primitives of UHM: **4 axioms** (A1-A4). Everything else is theorems:
- A5 (PW) — T-87 [Т]
- (AP) — from A1 (terminal object + adjunction) [Т]
- (PH) — from A1+A3 (functional necessity of E) [Т]
- (QG) — from A1 (∞-topos over D(ℂ^N)) [Т]
- (V) — from A2+A3 (Bures distinguishability) [Т]
:::

---

## 5. G-map: Constructive Protocol {#g-отображение}

### 5.1 Canonical embedding via the anchor function

For a system with state $s \in \mathcal{S}$ (neural network, brain, organism), the G-map $G: \mathcal{S} \to \mathcal{D}(\mathbb{C}^7)$ is constructed via the **anchor function** $\pi$:

$$
G(s) = \pi(s) := \frac{L(s) \cdot L(s)^\dagger}{\mathrm{Tr}(L(s) \cdot L(s)^\dagger)}
$$

where $L: \mathcal{S} \to \mathbb{C}^{7 \times 7}_{\text{lower-triangular}}$ is a trainable map (MLP or linear projection), and the normalization guarantees $G(s) \in \mathcal{D}(\mathbb{C}^7)$.

### 5.2 Uniqueness up to G₂

:::warning Theorem T-123 (G₂-uniqueness) [Т]
The anchor map $\pi: \mathcal{S} \to \mathcal{D}(\mathbb{C}^7)$, covariant with respect to $\mathcal{L}_\Omega$, is unique up to $G_2 = \mathrm{Aut}(\mathbb{O})$. The semantics of $\gamma_{kk}$ is **defined by the axioms** — not arbitrary.

[Proof →](/docs/proofs/consciousness/conscious-window#t-123)
:::

### 5.3 Protocol for concrete systems

| System | Method for constructing G | Status |
|---|---|---|
| **Neural network** | Linear probe $h \to L \to \Gamma$ via Cholesky (C25 [С]) | Feasible |
| **Brain (EEG)** | 7 frequency bands → $\gamma_{kk}$, coherence → $\gamma_{ij}$ | [П] Research program |
| **Organism** | Physiological markers → 7 sectors (T-92 [Т]) | [П] Measurement protocol |

:::info Key observation
The G-map is **not** a problem unique to UHM. An analogous task exists in IIT ($\Phi$-structure), GNW (global workspace), FEP (Markov blanket identification). Every theory of consciousness needs a bridge from the formalism to a concrete system. UHM has an **advantage**: T-123 guarantees uniqueness up to $G_2$, whereas in IIT the $\Phi$-structure depends on an arbitrary choice of partition.
:::

---

## 6. Deep Structure: Fractal Recurrence {#глубинная-структура}

:::note Meta-level
The four solved problems point to a single **deep structure**: self-reference. The theory describes reality ($\Gamma$) through mathematics (∞-topos), which is itself a configuration of $\Gamma$ (T-54: $\mathrm{Th}_{\text{UHM}} = \mathrm{Fix}(\varphi^*) \subseteq \Omega$). The map **is** the territory.
:::

### 6.1 Three levels of self-reference

| Level | Object | Self-modeling | Recursion limit |
|---|---|---|---|
| **Holon** | $\Gamma \in \mathcal{D}(\mathbb{C}^7)$ | $\varphi: \Gamma \to \Gamma$ | SAD_MAX = 3 (Fano contraction) |
| **Theory** | $\mathrm{Th}_{\text{UHM}} \subseteq \Omega$ | $\varphi^*: \Omega \to \Omega$ | $\mathrm{Th}_{\text{UHM}} \subsetneq \Omega$ (T-55, Lawvere incompleteness) |
| **Bimodule** | $H_F$ as $(A, A^\circ)$-bimodule | $J: H_F \to H_F$ (real structure) | $J^2 = +1$ (KO-dim 6) |

At each level:
- The system models **itself** ($\varphi$, $\varphi^*$, $J$)
- The modeling is **incomplete** (SAD < ∞, $\mathrm{Th} \subsetneq \Omega$, KO is finite)
- Incompleteness is the **source of dynamics** (Gap, evolutionary openness, fermion masses)

### 6.2 Correspondence with knowledge traditions

| Tradition | Concept | Formalization in UHM |
|---|---|---|
| **Vedanta** | Brahman = Atman | $\Gamma_{\text{global}}$ (single substance) ≡ $\varphi(\Gamma)$ (self-model) at $R = 1$ |
| **Buddhism** | Śūnyatā (emptiness) | $\mathrm{Th}_{\text{UHM}} \subsetneq \Omega$ — no predicate is "self-existent" |
| **Kabbalah** | Tzimtzum (contraction) | $\Gamma_\odot \to \rho^*$ — spontaneous breaking of $S_7$-symmetry |
| **Taoism** | The Tao that can be expressed | $L \subsetneq \Gamma$ — logic (L-dimension) does not encompass the whole |
| **Alchemy** | Solve et Coagula | $\mathcal{D}[\Gamma]$ (decoherence = solve) + $\mathcal{R}[\Gamma]$ (regeneration = coagula) |
| **Fractals** | Self-similarity | SAD tower: $\varphi \to \varphi^{(2)} \to \varphi^{(3)}$ — recursion of depth 3 |

### 6.3 Why exactly 3 levels of recursion

SAD_MAX = 3 is not an arbitrary number. It follows from the **geometry** of the state space:

1. **Fano contraction** $\alpha = 2/3$ means: each act of self-observation preserves 1/3 of coherence
2. **The space D(ℂ⁷) is compact**: $P \in [1/7, 1]$
3. After 3 iterations: $R^{(3)} \sim r_0 \cdot (1/3)^3 \approx r_0/27$
4. Threshold $R_{\text{th}}^{(3)} = 1/6$: $r_0/27 > 1/6$ requires $r_0 > 4.5$, i.e. $P > 4.5 \cdot 2/7 \approx 1.29 > 1$ — **impossible**

Compactness of D(ℂ⁷) × Fano contraction = finite recursion. Infinite self-reference is impossible in a finite-dimensional quantum system — and this is the mathematical formalization of what mystical traditions call the "inexpressible": L4 (complete transparency) exists as a limit but is unattainable.

---

## Related documents

- [UHM Spectral Triple](/docs/core/foundations/spacetime#теорема-спектральная-тройка) — construction of $(A_{\text{int}}, H_{\text{int}}, D_{\text{int}})$
- [Standard Model](/docs/physics/gauge-symmetry/standard-model) — gauge groups from $G_2$
- [Cosmological Constant](/docs/physics/gravity/cosmological-constant) — Λ-budget
- [Gap Thermodynamics](/docs/core/dynamics/gap-thermodynamics) — $V_{\text{Gap}}$ and minimum $\theta^*$
- [Axiom Ω⁷](/docs/core/foundations/axiom-omega) — 4 axioms A1-A4
- [Consciousness Window](/docs/proofs/consciousness/conscious-window) — T-123 (G₂-uniqueness)
- [Formalization of φ](/docs/proofs/categorical/formalization-phi) — self-modeling operator
- [Depth Tower](/docs/consciousness/hierarchy/depth-tower) — SAD_MAX = 3
