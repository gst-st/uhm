---
sidebar_position: 4
title: "Bimodule Construction and SM Representations"
description: "Solution of the SM representations problem via the bimodule NCG construction. Non-perturbative approach to λ₃. Derivation of (AP+PH+QG+V) from A1-A4."
---

# Bimodule Construction: solving four systemic problems

:::info Who this chapter is for
This document solves four interrelated problems that remained open [P] in UHM theory:

1. **SM representations**: How does one obtain SM representations from the algebra $A_{\text{int}} = \mathbb{C} \oplus M_3(\mathbb{C}) \oplus M_3(\mathbb{C})$ in which quarks carry **simultaneously** color and weak isospin: $(3,2)_{1/6}$?
2. **Non-perturbative λ₃**: How to extract physical predictions when $\lambda_3 \approx 74 \gg 4\pi$ (non-perturbative regime)?
3. **Derivation of (AP+PH+QG+V) from A1-A4**: What is the explicit derivation of the characterizing properties of the holon from the four axioms?
4. **G-map**: How is the map $G: \text{States} \to \mathcal{D}(\mathbb{C}^7)$ constructed for concrete systems?

All four problems have a **common root**: the theory has so far worked at the level of **algebras**, without reaching the level of **representations and bimodules**. Connes' bimodule construction is the missing link.

*Correction 2026-09-25:* problem 1 is **not** solved here — T-178 below is retracted as a derivation; the Standard Model representations come from Connes' Hilbert space $H_F$, which UHM imports. Half of problem 1 is solved elsewhere, without the import. Under the assumption (Cl), the left-handed doublets $(3,2)_{1/6}\oplus(1,2)_{-1/2}$ arise on $\mathbb{C}\otimes\mathbb{O}$ — UHM's Hilbert space plus the parallel spinor — as the spinor of the forced octonionic Clifford system, with the group $(\mathrm{SU}(3)\times\mathrm{SU}(2)\times\mathrm{U}(1))/\mathbb{Z}_6$ ([Standard Model, §2.5](/docs/physics/gauge-symmetry/standard-model#sm-из-клиффорда), T-326, T-327). The right-handed singlets do not fit there. They come with the complexification of that spinor: a Weyl field with values in it is valued in $\mathcal{S}\otimes_{\mathbb{R}}\mathbb{C}$, where a tenth Clifford generator is forced and $\mathrm{Spin}(10)$ gives one complete, anomaly-free generation with $\nu_R$ and the Standard Model hypercharges ([Standard Model, §2.6](/docs/physics/gauge-symmetry/standard-model#поколение-t329), T-329, [C at (Cl)]). The other half of problem 1 is thereby solved too, without $H_F$.
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

:::danger Theorem T-178 (Bimodule realization of SM) — retracted [✗] as a derivation (2026-09-25)
Retracted statement: the finite Hilbert space $H_F$ of the UHM spectral triple, viewed as an $(A_{\text{int}}, A_{\text{int}}^\circ)$-bimodule via the real structure $J$ with KO-dimension 6, decomposes into a direct sum of irreducible bimodules **exactly coinciding** with one generation of SM fermions.

It is not derived, for three reasons. (i) The UHM triple has $H_{\text{int}} = \mathbb{C}^7$, while one generation needs $32$ states (16 Weyl fermions and their conjugates); the $H_F$ used below is Connes' Hilbert space, imported, and "$7 \cdot 2 = 14 + 2$" in the reduction note is a count, not a map. (ii) KO-dimension 6 cannot occur on $\mathbb{C}^7$: it needs $J\chi = -\chi J$, so the antiunitary $J$ maps the $+1$ eigenspace of $\chi$ onto the $-1$ eigenspace and the two have equal dimension, which no grading of an odd-dimensional space provides (with the $\chi$ of Step 1 they are $4$ and $3$; [spacetime, Step 6](/docs/core/foundations/spacetime#теорема-спектральная-тройка)). (iii) The reduction $A_{\text{int}} \to A_F$ is not a homomorphism, and its "Morita compatibility" is T-175a, retracted: Morita equivalence preserves the centre, $\mathbb{C}^3$ for $A_{\text{int}}$ against $\mathbb{C}\oplus\mathbb{R}\oplus\mathbb{C}$ for $A_F$ ([spacetime](/docs/core/foundations/spacetime#алгебра-морита)). What stands is the standard bimodule decomposition of Connes' $H_F$ over $A_F = \mathbb{C}\oplus\mathbb{H}\oplus M_3(\mathbb{C})$ (Chamseddine–Connes–Marcolli 2007; Barrett 2007), which UHM imports rather than derives.
:::

**Construction.**

**Step 1 (Input data).** Finite UHM spectral triple:
- Algebra: $A_{\text{int}} = \mathbb{C}_O \oplus M_3(\mathbb{C})_{\mathbf{3}} \oplus M_3(\mathbb{C})_{\bar{\mathbf{3}}}$
- Space: $H_{\text{int}} = \mathbb{C}^7$
- Real structure: $J$ with $J^2 = +1$, $JD = DJ$, $J\chi = -\chi J$ (KO-dim 6) — retracted [✗]: no real structure of KO-dimension 6 exists on $\mathbb{C}^7$ — its $\chi = \pm 1$ eigenspaces would need equal dimension, and 7 is odd ([spacetime, Step 6](/docs/core/foundations/spacetime#теорема-спектральная-тройка))
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

:::note Scope: first-order condition verification
The first-order (order-one) condition is the seventh of Connes' reconstruction axioms and is the step most commonly flagged in external audits of NCG-based derivations (cf. Chamseddine–Connes 2008 on the "first-order / one-form" weakening). In this proof it is **imposed** as a structural constraint on $D$ (the admissible Dirac operators are those for which the condition holds) rather than derived from the algebra $A_{\text{int}}$ alone. Verification for the specific $D_{\text{int}}$ of T-53 reduces to a computation on the Higgs-line $\{A,E,U\}$ restriction of the product triple; this computation is sketched but not fully written out here (the same gap T-119 had until its restatement of 2026-09-25, flagged as framework-conditional in the [Rigour Stratification table](/docs/reference/status-registry#стратификация-строгости)).
:::

**Step 4 (Bimodule decomposition).** After imposing $J$ + first-order condition + electroweak breaking via the Higgs line $\{A,E,U\}$ ([ФЭ](/docs/physics/gauge-symmetry/standard-model#теорема-фэ) [T]):

$$
A_{\text{int}} \xrightarrow{J + \text{ФЭ}} A_F = \mathbb{C} \oplus \mathbb{H} \oplus M_3(\mathbb{C})
$$

:::info Explicit reduction $M_3(\mathbb C)\to\mathbb H$
The arrow $A_\mathrm{int}\to A_F$ is **not** an algebra isomorphism — it is a reduction induced by the real structure $J$ plus the ФЭ breaking. $A_\mathrm{int}=\mathbb C\oplus M_3(\mathbb C)_{\mathbf 3}\oplus M_3(\mathbb C)_{\bar{\mathbf 3}}$ has $\dim_\mathbb R=1+18+18=37$; $A_F=\mathbb C\oplus\mathbb H\oplus M_3(\mathbb C)$ has $\dim_\mathbb R=1+4+18=23$. The reduction:
1. The first $M_3(\mathbb C)_{\mathbf 3}$ factor carries the $SU(3)_C$ colour action — retained in $A_F$ as $M_3(\mathbb C)$.
2. The second $M_3(\mathbb C)_{\bar{\mathbf 3}}$ factor is reduced to $\mathbb H\subset M_2(\mathbb C)\subset M_3(\mathbb C)$ via the $J$-compatibility + Higgs-line $\{A,E,U\}$ constraint (T-1a): the 2-dimensional weak-isospin subspace $\mathrm{span}\{|E\rangle,|U\rangle\}$ supports an anti-commuting real structure $J^2=+1,\ [J,\gamma]=0$, whose commutant is $\mathbb H$ (Barrett 2007, §3.2; Chamseddine–Connes 2007). *Retracted 2026-09-25:* an antiunitary $J$ with $J^2 = +1$ on $\mathbb{C}^2$ is complex conjugation in a suitable basis, and its commutant in $M_2(\mathbb{C})$ is $M_2(\mathbb{R})$; $\mathbb{H}$ is the commutant of a $J$ with $J^2 = -1$. Barrett's paper has four sections and no subsections, so there is no §3.2, and it takes $A_F = \mathbb{C}\oplus\mathbb{H}\oplus M_3(\mathbb{C})$ as given. The remaining $M_3(\mathbb C)_{\bar{\mathbf 3}}\setminus\mathbb H$ content is projected out as it fails the first-order condition with the Dirac operator restricted to the Higgs line.
3. ~~The net effect is a **Morita-compatible** reduction: $A_F$ and $A_\mathrm{int}$ have the **same** category of bimodule representations realising SM fermions (Alvarez–Gracia-Bondía–Martín 1995), i.e., the bimodule structure is preserved.~~ Retracted 2026-09-25 with T-175a: the centres differ ($\mathbb{C}^3$ against $\mathbb{C}\oplus\mathbb{R}\oplus\mathbb{C}$), so the bimodule categories are not equivalent.
4. ~~Verification: dimensional accounting — $H_F$ fermion count from $A_F$ bimodules = 16 per generation (SM), matching $\dim H_F = 7 \cdot 2 = 14 + 2$ right-handed neutrinos.~~ Retracted 2026-09-25: $H_{\text{int}} = \mathbb{C}^7$ has dimension 7; "$7 \cdot 2 + 2 = 16$" does not construct the 16 states of a generation.

~~This resolves the concern that $A_\mathrm{int}$ and $A_F$ differ as algebras: the equivalence is at the level of bimodule categories (Morita), not objects.~~ Retracted 2026-09-25: there is no such equivalence (item 3).
:::

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

~~**Updated status of the SM representations problem: [T]** — solved via the standard NCG construction (Barrett 2007), applied to the UHM spectral triple (T-53 [T]).~~ Retracted 2026-09-25: the construction is applied to Connes' imported $H_F$, not to the UHM triple, whose $\mathbb{C}^7$ carries no KO-dimension-6 structure (T-178 above). Deriving the SM representations from UHM remains an open problem [Pr].
:::

$\blacksquare$

### 2.2 Hypercharge and parameter α

The free parameter $\alpha$ in the hypercharge generator $Y$ is fixed by **anomaly freedom** of the bimodule $H_F$:

:::danger Theorem T-179 (Hypercharge fixation) — retracted [✗] as stated (2026-09-25)
Retracted statement: the anomaly cancellation conditions $\mathrm{Tr}(Y) = 0$ and $\mathrm{Tr}(Y^3) = 0$ on the bimodule $H_F$ **uniquely** fix the hypercharge assignments of the Standard Model (up to overall normalization).

Two equations cannot fix the five hypercharges of a generation (six with $\nu_R$). Even all four anomaly conditions — gravitational, $U(1)_Y^3$, $SU(3)^2\,U(1)_Y$ and $SU(2)^2\,U(1)_Y$ — are solved both by the Standard Model values and by $y_Q = y_L = y_e = 0$, $y_u = -y_d$; and with a right-handed neutrino every combination $Y + c\,(B-L)$ passes all four (checked in exact arithmetic for $c = 1/7,\ 1/2,\ 3$; $B-L$ is the anomaly-free outer automorphism noted by Boyle and Farnsworth, *New J. Phys.* **22**, 073023 (2020)). Fixing the hypercharges needs further input: the Yukawa couplings to one Higgs doublet and, when $\nu_R$ is present, a Majorana mass for it (Babu and Mohapatra, *Phys. Rev. Lett.* **63**, 938 (1989)). The bimodule it is applied to is Connes' imported $H_F$ (T-178 above), so no part of the result is derived from UHM.
:::

**Former proof (retracted with the statement).** This is a standard result of anomaly theory (Alvarez-Gaumé, Witten 1984), applied to the specific bimodule from Step 4 above. The condition $\mathrm{Tr}(Y) = 0$ fixes the relative hypercharges of quarks and leptons; $\mathrm{Tr}(Y^3) = 0$ fixes the absolute values. The unique solution: $Y(q_L) = 1/6$, $Y(u_R) = 2/3$, $Y(d_R) = -1/3$, $Y(l_L) = -1/2$, $Y(e_R) = -1$. $\blacksquare$

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

:::warning Theorem T-180 (Non-perturbative mass ratios) [C at (SV)]
*Corrected 2026-09-25 from [T]: the vacuum state $\theta^*$ is taken with the sector values of the hypothesis (SV); T-64 is restated as a hypothesis whose vacuum has none of them.*

Fermion mass ratios are determined by the **eigenvalues** of the finite Dirac operator $D_{\text{int}}$ and **do not depend** on λ₃:

$$
\frac{m_i}{m_j} = \frac{|[D_{\text{int}}]_{ii}|}{|[D_{\text{int}}]_{jj}|} = \frac{\mathrm{Gap}(i)}{\mathrm{Gap}(j)}
$$

where $\mathrm{Gap}(i)$ are the Gap parameters from the vacuum state $\theta^*$ (T-64 [T] (corrected to the $G_2$-invariant potential; its vacuum has no sector values — hypothesis (SV)), unique minimum of $V_{\text{Gap}}$).
:::

**Corollary.** The mass hierarchy ($m_t \gg m_u$) is determined by the hierarchy of vacuum Gap parameters, which follows from the **geometry** of the Fano plane (different distances on PG(2,2)), not from loop corrections with λ₃.

### 3.3 What remains of λ₃

The parameter λ₃ = $\omega_0 \cdot |f_{ijk}|$ (where $f_{ijk}$ are the octonionic structure constants) enters the Gap potential $V_{\text{Gap}}$:

$$
V_{\text{Gap}} = V_2(\varepsilon) + \lambda_3 \cdot V_3(\varepsilon, \theta) + \lambda_4 \cdot V_4(\varepsilon)
$$

For λ₃ ≫ λ₄ the potential is dominated by the **cubic** term $V_3$. This is **not** a problem — it is an indication that the vacuum structure is determined by the **octonionic associator** (the cubic term $\propto [e_i, e_j, e_k]$), not by the standard quartic potential. The minimum of $V_{\text{Gap}}$ (T-64 [T] (corrected to the $G_2$-invariant potential; its vacuum has no sector values — hypothesis (SV))) exists and is unique **independently** of the ratio λ₃/λ₄.

:::info Reinterpretation of C7
Condition C7 ($\lambda_3 \gg 4\pi$) is **not** a problem but a **feature** of the octonionic structure. The non-associativity of octonions manifests through the dominance of the cubic potential. Physical predictions should be extracted from the spectrum of $D_{\text{int}}$ (non-perturbatively), not from loop expansions of the Lagrangian. **Updated status of C7: from a [H]-warning to an [I]-feature** — a structural property of the theory, not a defect.
:::

---

## 4. Requirements are not automatic consequences {#вывод-apphqgv}

The former T-181 proof is withdrawn [✗]. A sheaf topos is not the category of density matrices: its objects are sheaves, and its terminal object has a terminal space of global sections. The support reflector is defined in a slice, not as a numerical CPTP attractor. Stinespring does not identify sheaf morphisms with channels. Seven chosen matrix axes do not prove experiential content or tensor-factor reduction. Bures separation does not select the structural-majority cut.

AP, PH, QG and V are explicit requirements/bridges in the [corrected specification](/docs/core/foundations/axiom-septicity). The numerical state model, frame, self-model, rates, clock extension and phenomenal identification must each be provided. These data may define a consistent model; their existence does not follow from terminality. The Page–Wootters constraint also remains independent. No count of four independent primitives is asserted.

## 5. G-map: Constructive Protocol {#g-отображение}

### 5.1 Canonical embedding via the anchor function

For a system with state $s \in \mathcal{S}$ (neural network, brain, organism), the G-map $G: \mathcal{S} \to \mathcal{D}(\mathbb{C}^7)$ is constructed via the **anchor function** $\pi$:

$$
G(s) = \pi(s) := \frac{L(s) \cdot L(s)^\dagger}{\mathrm{Tr}(L(s) \cdot L(s)^\dagger)}
$$

where $L: \mathcal{S} \to \mathbb{C}^{7 \times 7}_{\text{lower-triangular}}$ is a trainable map (MLP or linear projection), and the normalization guarantees $G(s) \in \mathcal{D}(\mathbb{C}^7)$.

### 5.2. Identifiability of the observation model

The universal T-123 uniqueness claim is withdrawn [✗]. A Cholesky parameterization guarantees a state only when its denominator is nonzero; it does not guarantee that different states are distinguishable in the observations or that two learned encoders differ by a symmetry. Specify the observation law, test its fibres, and use the [reconstruction theorem](/docs/applied/research/reconstruction-identifiability). CPTP applies to linear maps of operator algebras, not to an arbitrary estimator from feature vectors.

### 5.3 Protocol for concrete systems

| System | Method for constructing G | Status |
|---|---|---|
| **Neural network** | Linear probe $h \to L \to \Gamma$ via Cholesky (C25 [C]) | Feasible |
| **Brain (EEG)** | 7 frequency bands → $\gamma_{kk}$, coherence → $\gamma_{ij}$ | [Pr] Research program |
| **Organism** | Physiological markers → 7 sectors (T-92 [D]) | [P] Measurement protocol |

:::note Measurement bridge
Every empirical formalism requires an observation model. UHM now treats this bridge as an identifiable statistical problem, with no universal encoder uniqueness.
:::

---

## 6. Deep Structure: Fractal Recurrence {#глубинная-структура}

:::note Meta-level
Self-reference is a proposed interpretation **[I]** of several different constructions. For T-54, choose $m:G\to G$ in the ordinary part of a specified topos. Its precomposition map acts on predicates: $m^*:\Omega^G\to\Omega^G$, and $\mathrm{Th}_m:=\operatorname{Eq}(m^*,\mathrm{id}_{\Omega^G})\hookrightarrow\Omega^G$ **[D/T]**. This equalizer does not identify a formal theory, the whole topos or mathematics with a density-matrix state. Those realizations and interpretations are separate inputs.
:::

### 6.1 Three levels of self-reference

| Level | Object | Specified map | Conditional property |
|---|---|---|---|
| **Holon** | $\Gamma \in D_7$ | Chosen $M:D_7\to D_7$ | Iteration depth requires a declared detector or operational certificate; finite dimension alone supplies no ceiling |
| **Fixed predicates** | $\mathrm{Th}_m\hookrightarrow\Omega^G$ | $m^*:p\mapsto p\circ m$ | Proper only with separating predicates and $m\ne\mathrm{id}$ (T-55); identity fixes every predicate |
| **Bimodule** | $H_F$ as $(A, A^\circ)$-bimodule | Antiunitary real structure $J:H_F\to H_F$ | $J^2=+1$ in the supplied KO-dimension-6 structure; this is not a self-model accuracy or recursion bound |

These maps have different domains and mathematical roles. T-55's properness is not Gödel incompleteness and does not prove unavoidable dynamics or a mismatch at every state. A nonidentity map may have fixed states; $J$ is a real structure, not an estimator. Reading the constructions as a common self-referential mechanism is **[I]**; a concrete physical coupling is needed before that reading predicts evolution or masses.

### 6.2 Correspondence with knowledge traditions

| Tradition | Concept | Formalization in UHM |
|---|---|---|
| **Vedanta** | Brahman = Atman | $\Gamma_{\text{global}}$ (single substance) ≡ $\varphi(\Gamma)$ (self-model) at $R = 1$ |
| **Buddhism** | Śūnyatā (emptiness) | Analogy [I] with conditional predicate noninvariance; T-55 does not prove that no predicate is "self-existent" |
| **Kabbalah** | Tzimtzum (contraction) | $\Gamma_\odot \to \rho^*$ — spontaneous breaking of $S_7$-symmetry |
| **Taoism** | The Tao that can be expressed | $L \subsetneq \Gamma$ — logic (L-dimension) does not encompass the whole |
| **Alchemy** | Solve et Coagula | $\mathcal{D}[\Gamma]$ (decoherence = solve) + $\mathcal{R}[\Gamma]$ (regeneration = coagula) |
| **Fractals** | Self-similarity | Iteration analogy [I]; measured depth requires a detector and independently passing operational certificates |

<a id="63-why-exactly-3-levels-of-recursion"></a>

### 6.3 Conditional limits of iteration

The universal SAD_MAX = 3 claim is removed. A finite dimension and compact state space do not bound iteration depth: the identity on $D_7$ can be iterated to any depth. This example certifies repeated iteration, not progressively stronger metamodel competence.

The Fano incidence fraction $\alpha=2/3$ can enter a specified generator's decay **rate**; it does not determine an iteration multiplier. For a declared continuous dephasing rate $\Gamma_2$, a sampling interval $\Delta t$ gives $q=e^{-\Gamma_2\Delta t}$. The multiplier $1/3$ belongs to the separately chosen discrete channel $\mathcal D_{2/3}$, not to every act of observation.

If a specified map satisfies $A_n:=\|\operatorname{offdiag}M^n(\rho)\|\le q^nA_0$ with $0<q<1$, and a detector requires $A_n\ge\varepsilon>0$ with $A_0\ge\varepsilon$, then

$$
n\le\left\lfloor\frac{\log(A_0/\varepsilon)}{\log(1/q)}\right\rfloor.
$$

This is a conditional detector cutoff. Resource budgets and independent operational certificates can impose other bounds. It is not a universal cognitive ceiling, a claim about canonical $R$, or a proof that L4 is impossible; see the [revised depth tower](/docs/consciousness/hierarchy/depth-tower).

---

## 6.3 Why exactly 3 levels of recursion

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
- [Consciousness Window](/docs/proofs/consciousness/conscious-window) — reconstruction identifiability
- [Formalization of φ](/docs/proofs/categorical/formalization-phi) — self-modeling operator
- [Depth Tower](/docs/consciousness/hierarchy/depth-tower) — conditional detector bounds and certified operational depth
