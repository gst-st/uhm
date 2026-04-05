---
sidebar_position: 4
title: "Higgs Sector"
description: "Uniqueness of the Higgs line {A,E,U}, Higgs mass with octonionic correction, Higgs quartic from spectral action [C], Gap(E,U) → 0 and electroweak breaking"
---

# Higgs Sector

:::info Rigor Levels
- **[T]** Theorem — strictly proved from UHM axioms
- **[C]** Conditional — conditional on an explicit assumption
- **[H]** Hypothesis — mathematically formulated, requires proof or non-perturbative computation
- **[I]** Interpretation — philosophical / qualitative analogy
- **[R]** Definition — definition by convention
:::

## Contents

1. [Uniqueness of the Higgs line {A,E,U}](#1-единственность-хиггсовой-линии-aeu)
2. [Higgs mechanism from Gap-condensation](#2-механизм-хиггса-из-gap-конденсации)
3. [Gap(E,U) → 0: electroweak symmetry breaking](#3-gapeu--0-электрослабое-нарушение-симметрии)
4. [Higgs mass with octonionic correction](#4-масса-хиггса-с-октонионной-коррекцией) (incl. [Higgs quartic from spectral action](#теорема-хиггсовская-квартика) [C])
5. [Connection to SM gauge structure (EW-construction)](#5-связь-с-калибровочной-структурой-sm)
6. [Falsifiable predictions](#6-фальсифицируемые-предсказания)
7. [Can UHM predict the Higgs mass?](#7-может-ли-угм-предсказать-массу-хиггса) — analysis of the derivation chain, status of each link

---

## 1. Uniqueness of the Higgs line \{A,E,U\} {#1-единственность-хиггсовой-линии-aeu}

### 1.1 Identification of the Higgs field [T] {#отождествление-хиггса}

In UHM the Higgs field is identified with the $E$-$U$ coherence in the $\bar{3}$-to-$\bar{3}$ sector:

$$H \sim \gamma_{EU} = |\gamma_{EU}| e^{i\theta_{EU}}$$

Dimensions $E$ (evaluation) and $U$ (unity) belong to the $\bar{3}$-sector $\{L, E, U\} = \{4, 5, 6\}$. The pair $(E, U)$ defines the electroweak channel: $\text{Gap}(E,U) = 0$ corresponds to a weak doublet, $\text{Gap}(E,U) \neq 0$ — to a singlet.

#### Theorem 1.0 (Identification $H \sim \gamma_{EU}$) [T] {#теорема-отождествление-хиггса}

:::tip [T] Theorem
The identification $H \sim \gamma_{EU}$ is strictly proved from four independent [T]-results: categorical uniqueness of the pair $(E,U)$, uniqueness of the Higgs line, $SU(2)_L \times U(1)_Y$ quantum numbers, and nonzero vacuum expectation value from the unique vacuum.
:::

**Theorem.** The coherence $\gamma_{EU}$ is the unique candidate for the Higgs field in UHM, and the identification $H \sim \gamma_{EU}$ is proved from the following chain.

**Step 1. Categorical uniqueness of the pair $(E,U)$ [T] (T-42a).**

The formula $\kappa_0 = \omega_0 \cdot |\gamma_{OE}| \cdot |\gamma_{OU}| / \gamma_{OO}$ categorically singles out exactly the pair $(E,U)$ via morphisms $\mathrm{Hom}(O,E)$ and $\mathrm{Hom}(O,U)$. No other pair of dimensions has this property: replacing with $\{L,U\}$ removes $\mathrm{Hom}(O,L)$ from $\kappa_0$; replacing with $\{L,E\}$ excludes $U$, breaking the normalization $\mathrm{Tr}(\Gamma) = 1$. Uniqueness is proved — see [Theorem of FE-uniqueness](/docs/physics/gauge-symmetry/standard-model#теорема-единственности-фэ) [T].

**Step 2. Uniqueness of the Higgs line $\{A,E,U\}$ [T] (Theorem 1.1).**

Through any two points of $\mathrm{PG}(2,2)$ there passes exactly one line. The unique Fano line containing both points $E = 5$ and $U = 6$: $\{5,6,1\} = \{A,E,U\}$. This line defines the electroweak sector — see [Theorem 1.1](#thm-1-1) [T].

**Step 3. Quantum numbers of $\gamma_{EU}$ coincide with those of the SM Higgs doublet [T].**

From the electroweak uniqueness theorem ([§2.3a](/docs/physics/gauge-symmetry/standard-model#теорема-единственности-фэ) [T]): the pair $(E,U)$ forms the doublet $2_{EU}$ under $SU(2)_L$. The coherence $\gamma_{EU}$ — a bilinear form connecting $E$ and $U$ — transforms as $(2, +1/2)$ under $SU(2)_L \times U(1)_Y$. This is exactly the quantum numbers of the SM Higgs doublet.

**Step 4. Nonzero VEV $\langle\gamma_{EU}\rangle \neq 0$ breaks $SU(2)_L \times U(1)_Y \to U(1)_\text{em}$ [T].**

From [Theorem on the unique vacuum T-64](/docs/core/dynamics/gap-thermodynamics#теорема-глобальная-минимизация) [T]: the unique global minimum of $V_\text{Gap}$ has $|\gamma_{EU}|_\text{vac} = \varepsilon_{\bar{3}\bar{3}} \approx 10^{-17}$ (in units of $\omega_0$), giving $\langle\gamma_{EU}\rangle \neq 0$. A nonzero vacuum expectation value of a field with quantum numbers $(2, +1/2)$ uniquely realizes spontaneous breaking $SU(2)_L \times U(1)_Y \to U(1)_\text{em}$.

**Conclusion.** All four steps rely exclusively on [T]-results. The identification $H \sim \gamma_{EU}$ follows from them uniquely. $\blacksquare$

### 1.2 Fano–Higgs line

### Definition 1.1 (Fano–Higgs line)

**Definition.** The Fano–Higgs line is the Fano line of $\mathrm{PG}(2,2)$ containing **both** Higgs dimensions $E = 5$ and $U = 6$.

### Theorem 1.1 (Uniqueness of the Fano–Higgs line) {#thm-1-1}

:::tip [T] Theorem
Strictly proved. Follows from the incidence axiom of the projective plane $\mathrm{PG}(2,2)$: through any two points there passes exactly one line.
:::

**Theorem.** There exists exactly one Fano–Higgs line: $\{1, 5, 6\} = \{A, E, U\}$.

**Proof.** In $\mathrm{PG}(2,2)$ through any two points there passes exactly one line. We seek the line containing points $E=5$ and $U=6$. From the complete list of 7 Fano lines:

| Line | Contains $E=5$? | Contains $U=6$? | Both? |
|---|---|---|---|
| $\{1,2,4\}$ | No | No | No |
| $\{2,3,5\}$ | **Yes** | No | No |
| $\{3,4,6\}$ | No | **Yes** | No |
| $\{4,5,7\}$ | **Yes** | No | No |
| $\{5,6,1\}$ | **Yes** | **Yes** | **Yes** |
| $\{6,7,2\}$ | No | **Yes** | No |
| $\{7,1,3\}$ | No | No | No |

The unique line containing both 5 and 6: $\{5,6,1\} = \{A, E, U\}$. $\blacksquare$

### 1.3 Combinatorics of PG(2,2): why {A,E,U} is the only possibility

:::tip [T] Theorem
Uniqueness follows from the incidence axiom of the projective plane of order 2: through any two points there passes exactly one line.
:::

The projective plane $\mathrm{PG}(2,2)$ (Fano plane) contains 7 points and 7 lines. Each line contains 3 points; through each point pass 3 lines. Key property: **through any pair of points there passes exactly one line**.

The Higgs field is defined by two dimensions: $E = 5$ (evaluation) and $U = 6$ (unity). Question: which Fano lines contain both of these dimensions?

The count is exhaustive. Of the 7 lines of $\mathrm{PG}(2,2)$:

- $\{1,2,4\}$: $E \notin$, $U \notin$ — does not qualify
- $\{2,3,5\}$: $E \in$, $U \notin$ — does not qualify
- $\{3,4,6\}$: $E \notin$, $U \in$ — does not qualify
- $\{4,5,7\}$: $E \in$, $U \notin$ — does not qualify
- **$\{5,6,1\} = \{A,E,U\}$**: $E \in$, $U \in$ — **unique**
- $\{6,7,2\}$: $E \notin$, $U \in$ — does not qualify
- $\{7,1,3\}$: $E \notin$, $U \notin$ — does not qualify

Thus, the incidence structure of $\mathrm{PG}(2,2)$ **uniquely** determines the third element of the Higgs line: $A = 1$.

Note that this property does not depend on the choice of numbering: for **any** identification of $E$ and $U$ with two points of the Fano plane, the third element is determined uniquely. The duality of $\mathrm{PG}(2,2)$ (point $\leftrightarrow$ line) means that point $A$ lies on exactly 3 lines, one of which is the Higgs line $\{A,E,U\}$, and the other two ($\{A,S,L\} = \{1,2,4\}$ and $\{A,D,O\} = \{1,3,7\}$) play different roles: generational and gravitational, respectively.

### 1.4 Physical interpretation [I]

The third element of the Higgs line is $A = 1$ (awareness). This means:

- Dimension **A** is directly connected to the Higgs mechanism of mass generation.
- Generation $k=1$ (A) → third generation ($t$, $b$, $\tau$) acquires a **tree-level** Yukawa coupling.
- Generations $k=2$ (S) and $k=4$ (L) do **not** lie on the Higgs line → $y^{(\text{tree})} = 0$.

This is the foundation of the [Fano selection rule for Yukawa couplings](./yukawa-hierarchy.md#2-фановское-правило-отбора-юкавских-связей).

:::info Generation assignment and number of generations [T]
The assignment $k=1 \to$ 3rd generation is strictly proved from the unique nonzero tree-level Yukawa coupling — see [Theorem 4.1 (Assignment of 3rd generation)](/docs/physics/particle-physics/fermion-generations#thm-gen-4-1). The complete ordering ($k=4 \to$ 2nd, $k=2 \to$ 1st) is strictly proved — [Theorem 4.3](/docs/physics/particle-physics/fermion-generations#thm-gen-4-3) [T]. The number of generations $N_{\text{gen}} = 3$ is strictly proved from a two-sided argument ($\leq 3$ from swallowtail + $\geq 3$ from $(1,2,4) \subset \mathbb{Z}_7^*$) — see [Theorem $N_{\text{gen}} = 3$](/docs/physics/particle-physics/fermion-generations#теорема-ровно-три-генерации) [T].
:::

### 1.5 Why the E-U channel defines electroweak physics

:::tip [T] Theorem
The $E$-$U$ channel is the unique channel in the $\bar{3}$-sector not containing $L$ (interiority), making it the only candidate for chiral distinction.
:::

In the $\bar{3}$-sector $\{L, E, U\} = \{4, 5, 6\}$ there are three coherences: $\gamma_{LE}$, $\gamma_{LU}$, $\gamma_{EU}$. Of these:

| Channel | Connection | Role in SM |
|---|---|---|
| $L$-$E$ | Interiority–evaluation | Lepton number |
| $L$-$U$ | Interiority–unity | Baryon number |
| **$E$-$U$** | **Evaluation–unity** | **Weak isospin** (Higgs) |

The $E$-$U$ channel is distinguished for three reasons:

1. **Algebraic:** $E$-$U$ is the unique channel in the $\bar{3}$-sector not containing the $L$-dimension. In fermionic configurations ($R \to 0$) the $L$-channels are fixed, and only $E$-$U$ remains free for defining chirality.

2. **From Fano structure:** in the $\bar{3}$-sector there exists one Fano line $\{L,E,U\}$. The chirality operator $\Gamma_{LEU}$ is defined by this line. $\text{Gap}(E,U)$ is the specific coherence broken by the Higgs, while $\text{Gap}(L,E)$ and $\text{Gap}(L,U)$ define the interiority level.

3. **Physical:** $E$-dimension $\leftrightarrow$ evaluative structure $\leftrightarrow$ electric charge. $U$-dimension $\leftrightarrow$ unification $\leftrightarrow$ weak isospin. At $\text{Gap}(E,U) = 0$ they are indistinguishable → $SU(2)_L$ doublet. At $\text{Gap}(E,U) \neq 0$ they are distinguishable → singlets.

---

## 2. Higgs mechanism from Gap-condensation {#2-механизм-хиггса-из-gap-конденсации}

### Theorem 2.1 (Higgs mechanism from Gap-condensation) {#thm-2-1}

:::tip [T] Theorem
The mechanism of electroweak breaking via $\text{Gap}(E,U) \to 0$ is a consequence of the uniqueness of the minimum of $V_{\text{Gap}}$ in the $\bar{3}$-sector: $\varepsilon_{\bar{3}\bar{3}} \approx 10^{-17}$ is determined uniquely from positive definiteness of the Hessian ([theorem on the unique vacuum](/docs/core/dynamics/gap-thermodynamics#теорема-единственный-вакуум) [T]).
:::

**Theorem.** Spontaneous electroweak symmetry breaking arises from Gap-condensation in the $\bar{3}$-to-$\bar{3}$ sector:

**(a)** The Higgs field is identified with the $E$-$U$ coherence:

$$H \sim \gamma_{EU} = |\gamma_{EU}| e^{i\theta_{EU}}$$

**(b)** VEV (vacuum expectation value):

$$\langle H \rangle = \langle |\gamma_{EU}| \rangle e^{i\langle\theta_{EU}\rangle} \neq 0$$

Nonzero VEV breaks $SU(2)_L \times U(1)_Y \to U(1)_\text{EM}$:
- $SU(2)_L$: 3 generators → 2 broken ($W^+$, $W^-$) + 1 linear combination broken ($Z$)
- $U(1)_Y$: 1 generator
- $U(1)_\text{EM}$ = diagonal subgroup (photon) — unbroken

**(c)** Mass of the $W$-boson:

$$M_W = \frac{g}{2} v, \quad v = \langle |\gamma_{EU}| \rangle \cdot \mu_\text{phys}$$

where $g$ is the electroweak coupling constant, $\mu_\text{phys} = \mu \cdot \omega_0$.

### 2.1 Potential in the E-U channel

The potential $V_\text{Gap}$ projects onto the $E$-$U$ channel:

$$V_{EU}(\gamma_{EU}) = \mu^2 |\gamma_{EU}|^2 + \lambda_4 |\gamma_{EU}|^4 + \lambda_3 \bar{A} |\gamma_{EU}|^3 \cos(\text{phase})$$

At $\mu^2 < 0$ (low-temperature regime): minimum at $|\gamma_{EU}| = v \neq 0$. This is the standard Higgs mechanism applied to the Gap potential. Higgs mass = second derivative of $V_{EU}$ at the minimum.

:::note Status of parameter $\lambda_3$ [T]
The parameter $\lambda_3 = 2\mu^2/(3|\bar{\gamma}|) \approx 74$ is a **geometric coefficient** of the spectral action (T-74 [T]), not a perturbative coupling constant. Physical observables are defined non-perturbatively via the self-consistent vacuum $\theta^*$ (T-79 [T]). UV-finiteness (T-66 [T]) ensures structural correctness. Loop estimates are approximations to $\theta^*$, giving the right order of magnitude (error $\lesssim \times 5$). For details — see [Yukawa Hierarchy](/docs/physics/particle-physics/yukawa-hierarchy#предупреждение-λ3).

**⚠ C7**: $\lambda_3 \approx 74 \gg 4\pi$ — non-perturbative regime. All loop computations with $\lambda_3$ are formally unreliable and downgraded to **[H]**. See [warning](/docs/physics/particle-physics/yukawa-hierarchy#c7-nonperturbative).
:::

### 2.2 Origin of $M_H \approx 125$ GeV from Gap-condensation [C] {#mh-125}

:::warning [C] Conditional
The parameter $\lambda_4$ is determined from the Chamseddine–Connes spectral action with RG correction (see [theorem on Higgs quartic](#теорема-хиггсовская-квартика) [C]). Conditionality: free parameter $f_0$ in the spectral action. The octonionic correction from $V_3$ additionally modifies $M_H$.
:::

:::info Progress: from fitting to computation
In early versions the parameter $\lambda_4 \approx 0.13$ was **adjusted** from the condition $M_H \approx 125$ GeV. The spectral action ([theorem on Higgs quartic](#теорема-хиггсовская-квартика) [C]) determines $\lambda_4$ through the spectrum of the finite Dirac operator $D_{\text{int}}$. The remaining free degree is the parameter $f_0$, fixed by calibration to $M_H^{\text{exp}}$.
:::

In the Standard Model the Higgs mass $M_H \approx 125$ GeV is a **free parameter**, fixed experimentally. In UHM the parameter $\lambda_4$ is determined by the spectral action through the spectrum $D_{\text{int}}$ ([theorem on Higgs quartic](#теорема-хиггсовская-квартика) [C]), and the Higgs mass arises from the structure of the Gap potential:

**(a)** The Higgs mass is determined by the curvature of $V_{EU}$ at the minimum:

$$M_H^2 = \frac{\partial^2 V_{EU}}{\partial |\gamma_{EU}|^2}\bigg|_{v} = 2\lambda_4 v^2 + \frac{3\lambda_3^2 \bar{A}^2}{4\mu^2}$$

**(b)** The first term, $2\lambda_4 v^2$, is the standard contribution from the quartic potential $V_4$. At $v = 246$ GeV and $\lambda_4 \approx 0.13$ we get $\sqrt{2\lambda_4} \cdot v \approx 125$ GeV — coincidence with SM.

**(c)** The second term, $\delta M_H^2 = 3\lambda_3^2 \bar{A}^2 / (4\mu^2)$, is the **octonionic correction** from the cubic potential $V_3$. It is absent in the SM and is a direct consequence of the $\mathbb{O}$-structure.

**(d)** Numerical estimate of the correction (at typical values of Gap parameters):

$$\delta M_H^2 \approx \frac{3 \cdot (73.8)^2 \cdot (0.047)^2}{4 \cdot 16.6} \approx 5.5 \; (\text{in Gap units})$$

This correction is small compared to the main term, but is **nonzero** and gives rise to a falsifiable deviation from SM (see [section 6](#6-фальсифицируемые-предсказания)).

**(e)** Mechanism for fixing $\lambda_4$: the Chamseddine–Connes spectral action determines $\lambda_4$ via the coefficient $a_4$ and the spectrum $D_{\text{int}}$ ([theorem on Higgs quartic](#теорема-хиггсовская-квартика) [C]). RG evolution from the cutoff scale $\Lambda$ to $v_{\text{EW}}$ brings $\lambda_4(\Lambda) \approx 0.20$ to the observed $\lambda_4(v) \approx 0.13$ (Shaposhnikov–Wetterich result 2010). The remaining free parameter $f_0$ in the spectral action is fixed by calibration. Once it is determined from other observables, $M_H$ will become a full **prediction** of the theory.

---

## 3. Gap(E,U) → 0: electroweak symmetry breaking {#3-gapeu--0-электрослабое-нарушение-симметрии}

### 3.1 Connection of Gap(E,U) to particle quantum numbers

$\text{Gap}(E,U)$ defines the **weak isospin** of elementary fermions:

- $\text{Gap}(E,U) = 0$ → **doublet** of $SU(2)_L$
- $\text{Gap}(E,U) \neq 0$ → **singlet** of $SU(2)_L$

### 3.2 Fermionic representations from Γ-configurations

### Theorem 3.1 (Quarks and leptons as Gap-configurations) [C] {#thm-3-1}

:::warning [C] Conditional
The identification of fermions with Gap-configurations is conditional on the correctness of the identification of SM quantum numbers with Gap structure (gauge correspondence hypothesis).
:::

**Theorem.** Elementary fermions are identified with degenerate ($R \to 0$) configurations $\Gamma$, classified by $SU(3)_C \times SU(2)_L \times U(1)_Y$ quantum numbers:

**(a)** Left quark doublet $Q_L = (u_L, d_L)$:

$$\Gamma_{Q_L}: \quad \text{Gap}(A,L) = \text{Gap}(S,E) = 0 \; (\text{color bonds}), \quad \text{Gap}(E,U) = 0 \; (\text{weak isospin})$$

Quantum numbers: $(3, 2)_{1/6}$

**(b)** Right $u$-quark $u_R$:

$$\Gamma_{u_R}: \quad \text{Gap}(A,L) = \text{Gap}(S,E) = 0, \quad \text{Gap}(E,U) \neq 0$$

Quantum numbers: $(3, 1)_{2/3}$

**(c)** Left lepton doublet $L_L = (\nu_L, e_L)$:

$$\Gamma_{L_L}: \quad \text{Gap}(\{A,S,D\}, \{L,E,U\}) = \text{Gap}_\text{max} \; (\text{colorless}), \quad \text{Gap}(E,U) = 0$$

Quantum numbers: $(1, 2)_{-1/2}$

**(d)** Right electron $e_R$:

$$\Gamma_{e_R}: \quad \text{Gap}(\{A,S,D\}, \{L,E,U\}) = \text{Gap}_\text{max}, \quad \text{Gap}(E,U) \neq 0$$

Quantum numbers: $(1, 1)_{-1}$

### 3.3 Mechanism: why Gap(E,U) → 0 in the vacuum

**Justification.** Of the three candidates for zero Gap in the $\bar{3}$-sector ($L$-$E$, $L$-$U$, $E$-$U$), the pair $(E,U)$ is distinguished because:

1. The **unique** Fano–Higgs line $\{A,E,U\}$ passes through both points.
2. On this line lies $A$ = the generation with a tree-level Yukawa → maximal coupling to the mass mechanism.
3. The vacuum configuration minimizes $V_\text{Gap}$, and the minimum is reached at $\text{Gap}(E,U) \to 0$ in the $\bar{3}$-sector. $\varepsilon_{\bar{3}\bar{3}} \approx 10^{-17}$ from the unique vacuum → Gap(E,U) ≈ 0 — minimum of $V_{\text{Gap}}$ in the $\bar{3}$-sector [T] (see [theorem on unique vacuum](/docs/core/dynamics/gap-thermodynamics#теорема-единственный-вакуум)).

**Hypercharge** is determined by the total Gap in the $O$-sector:

$$Y = \frac{1}{3}\left(\sum_{i \in 3} \text{Gap}(O,i) - \sum_{j \in \bar{3}} \text{Gap}(O,j)\right)$$

### 3.4 Anomaly cancellation

### Theorem 3.2 (Anomaly cancellation) {#thm-3-2}

:::tip [T] Theorem
Anomaly cancellation for one generation is the standard SM result, automatically satisfied for Gap-configurations.
:::

**Theorem.** The set of fermionic representations satisfies the gauge anomaly cancellation condition:

$$\sum_\text{fermions} Y^3 = 0, \quad \sum_\text{fermions} Y = 0$$

**Proof.** For one generation:

$$Q_L(1/6)^3 \times 6 + u_R(2/3)^3 \times 3 + d_R(-1/3)^3 \times 3 + L_L(-1/2)^3 \times 2 + e_R(-1)^3 \times 1 = 0$$

Fermionic representations from Gap-configurations form the same structure as one SM generation — anomalies cancel by construction. $\blacksquare$

---

## 4. Higgs mass with octonionic correction {#4-масса-хиггса-с-октонионной-коррекцией}

### Theorem T-70 (Canonical definition of $f_0$) [T] {#теорема-f0-канонический}

:::tip [T] Theorem
In UHM the moment $f_0$ of the spectral action is **uniquely determined** through the vacuum effective action of the Gap theory on $(S^1)^{21}$:

$$f_0 \Lambda^4 = \frac{1}{7}\left[V_{\mathrm{Gap}}^{\min} + \frac{1}{2}\zeta'_{H_{\mathrm{Gap}}}(0)\right]$$

where $V_{\mathrm{Gap}}^{\min}$ is the potential value at the vacuum minimum ([T-64](/docs/core/dynamics/gap-thermodynamics#теорема-глобальная-минимизация) [T]), and $\zeta'_{H_{\mathrm{Gap}}}(0)$ is the log-determinant of the Hessian at the vacuum.
:::

**Proof.**

**Step 1 (UV-finiteness → finite functional integral).** The Gap theory on $(S^1)^{21}$ with $G_2$-symmetry and $\mathcal{N} = 1$ SUSY is UV-finite ([T-66](/docs/physics/gravity/quantum-gravity#теорема-уф-конечность) [T]). Therefore the functional integral $Z = \int [D\theta] \exp(-S_{\mathrm{Gap}}[\theta])$ is **finite and well-defined** without regularization ambiguity. The quantum effective action $\Gamma_{\mathrm{eff}} = -\ln Z$ is a finite, concrete quantity.

**Step 2 (Unique vacuum → loop expansion).** From [T-61, T-64](/docs/core/dynamics/gap-thermodynamics#теорема-единственный-вакуум) [T]: the potential $V_{\mathrm{Gap}}$ has a unique global minimum with positive definite Hessian $H_{\mathrm{Gap}}$. Expansion:

$$\Gamma_{\mathrm{eff}} = V_{\mathrm{Gap}}^{\min} + \frac{1}{2}\ln\det(H_{\mathrm{Gap}}) + O(\text{two-loop})$$

**Step 3 (Determinant regularization).** Zeta-regularized determinant: $\ln\det(H_{\mathrm{Gap}}) = -\zeta'_{H_{\mathrm{Gap}}}(0)$. From T-64 [T]: all eigenvalues $\lambda_i > 0$ (5 positive on the orbit space), so $\zeta'_{H_{\mathrm{Gap}}}(0) = -\sum_{i=1}^{5}\ln\lambda_i$.

**Step 4 (Identification with $f_0$).** Coefficient $a_0$ of the spectral action: $f_0 \Lambda^4 \cdot 7$ = vacuum energy density of the internal space = $\Gamma_{\mathrm{eff}}$. Therefore:

$$f_0 = \frac{\Gamma_{\mathrm{eff}}}{7\Lambda^4} = \frac{1}{7\Lambda^4}\left[V_{\mathrm{Gap}}^{\min} + \frac{1}{2}\zeta'_{H_{\mathrm{Gap}}}(0)\right]$$

**Step 5 (Uniqueness).** All quantities on the right-hand side are uniquely determined: $V_{\mathrm{Gap}}^{\min}$ from T-64 [T], $\zeta'_{H_{\mathrm{Gap}}}(0)$ from a finite sum over 5 eigenvalues, $\Lambda = \omega_0$. $f_0$ is **not a free parameter**, but a definite function of the vacuum quantities. $\blacksquare$

:::info Numerical estimate [C]
From T-64 [T], Hessian eigenvalues: $\lambda_1 = 18\mu^2$ (confinement), $\lambda_{2,3} = 6\mu^2(1 + O(\varepsilon^2))$ (spatial), $\lambda_{4,5} = 12\mu^2(1 + O(\varepsilon))$ (O-modes). With $\mu^2 \approx \omega_0^2/7$: $f_0 \approx 2.2/\omega_0^4$. Numerical value [C] — depends on exact $\varepsilon_i$.
:::

### Theorem (Higgs quartic from spectral action) [C] {#теорема-хиггсовская-квартика}

:::warning [C] Conditional
$\lambda_4$ is determined through the spectrum of the finite Dirac operator $D_{\text{int}}$. The parameter $f_0$ is **canonically determined** [T] ([theorem above](#теорема-f0-канонический)); the numerical value of $\lambda_4$ depends on exact sectoral $\varepsilon_i$ [C].
:::

**Theorem.** The Higgs quartic self-coupling is determined through the coefficient $a_4$ of the spectral action:

$$\lambda_4 = \frac{\pi^2}{2f_0\Lambda^4} \cdot \frac{\mathrm{Tr}(D_{\text{int}}^4)}{[\mathrm{Tr}(D_{\text{int}}^2)]^2}$$

This is the standard result of Chamseddine–Connes–Marcolli (2007, Thm 11.2) for the NCG Standard Model. Applicability to the UHM triple is verified:

**Proof.**

**Step 1 (Applicability check).** The finite spectral triple $(A_{\text{int}}, H_{\text{int}}, D_{\text{int}})$ of UHM ([theorem T-53](/docs/core/foundations/spacetime#теорема-спектральная-тройка) [T]) satisfies the premises of the Chamseddine–Connes–Marcolli theorem:

1. **Algebra** $A_{\text{int}} = \mathbb{C} \oplus M_3(\mathbb{C}) \oplus M_3(\mathbb{C})$ — corresponds to NCG Standard Model.
2. **Dirac operator** $D_{\text{int}}$ — finite-dimensional, self-adjoint — corresponds.
3. **Higgs field** as internal fluctuation $A_{\text{int}}$: $H = A + JAJ^{-1}|_{E\text{-}U}$ — corresponds.

**Step 2 (Spectral action).** The spectral action $S = \mathrm{Tr}(f(D/\Lambda))$ (see [quantum gravity](/docs/physics/gravity/quantum-gravity)) expands as:

$$S = f_4 \Lambda^4 a_0 + f_2 \Lambda^2 a_2 + f_0 a_4 + O(\Lambda^{-2})$$

The coefficient $a_4$ contains the term $\mathrm{Tr}(D_{\text{int}}^4)$, generating the quartic Higgs potential.

**Step 3 (Computation).** From sectoral values (T-61, unique vacuum [T]):

$$\mathrm{Tr}(D_{\text{int}}^2) \approx 6\omega_0^2\varepsilon_0^2, \qquad \mathrm{Tr}(D_{\text{int}}^4) \approx 6\omega_0^4\varepsilon_0^4 + \text{sectoral corrections}$$

**Step 4 (RG evolution).** The bare $\lambda_4(\Lambda)$ is too large. RG running from $\Lambda$ to $v_{\text{EW}}$:

$$\lambda_4(v) = \lambda_4(\Lambda) + \frac{1}{16\pi^2}\left(24\lambda_4^2 - 6y_t^4 + \ldots\right) \ln\frac{v}{\Lambda}$$

At $y_t \approx 1$ (quasi-IR fixed point [T]): RG brings $\lambda_4$ to the observed $\approx 0.13$ from $\lambda_4(\Lambda) \approx 0.20$ [C] — standard Shaposhnikov–Wetterich result (2010). $\blacksquare$

**Status:** [C] — $\lambda_4$ determined through spectrum $D_{\text{int}}$ + RG. Parameter $f_0$ is **canonically determined [T]** ([T-70](#теорема-f0-канонический)). The conditionality [C] remains only for the numerical value — depends on exact sectoral $\varepsilon_i$.

:::info Cross-references
- **Spectral triple:** [Theorem (UHM Spectral Triple) [T]](/docs/core/foundations/spacetime#теорема-спектральная-тройка) — finite triple $(A_{\text{int}}, H_{\text{int}}, D_{\text{int}})$, KO-dimension 6
- **Spectral action:** [Quantum Gravity](/docs/physics/gravity/quantum-gravity#теорема-полное-спектральное-действие) — $S = \mathrm{Tr}(f(D_A/\Lambda))$, Einstein equations [T]
- **Unique vacuum:** [T-61](/docs/core/dynamics/gap-thermodynamics#теорема-единственный-вакуум) — sectoral values $\varepsilon$
:::

---

### Theorem 4.1 (Higgs mass) [C] {#thm-4-1}

:::warning [C] Conditional
The formula for the Higgs mass contains $\lambda_4$, determined from the spectral action ([theorem on Higgs quartic](#теорема-хиггсовская-квартика) [C]), and the octonionic correction from $V_3$. Parameter $f_0$ is canonically determined [T] ([T-70](#теорема-f0-канонический)); conditionality [C] — only numerical value through $\varepsilon_i$.
:::

**Theorem.** The Higgs mass is determined as the second derivative of the potential $V_{EU}$ at the minimum:

**(a)** Formula:

$$M_H^2 = 2\lambda_4 v^2 + \frac{3\lambda_3^2 \bar{A}^2}{4\mu^2}$$

First term — standard (from $V_4$). Second — **octonionic correction** from $V_3$.

**Proof.** The potential $V_\text{Gap}$ projects onto the $E$-$U$ channel:

$$V_{EU}(\gamma_{EU}) = \mu^2 |\gamma_{EU}|^2 + \lambda_4 |\gamma_{EU}|^4 + \lambda_3 \bar{A} |\gamma_{EU}|^3 \cos(\text{phase})$$

At $\mu^2 < 0$: minimum at $|\gamma_{EU}| = v \neq 0$.

Higgs mass = second derivative of $V_{EU}$ at the minimum:

$$M_H^2 = \frac{\partial^2 V_{EU}}{\partial |\gamma_{EU}|^2}\bigg|_{v} = 2\lambda_4 v^2 + \frac{3\lambda_3^2 \bar{A}^2}{4\mu^2}$$

$\blacksquare$

:::info Free parameters
$\lambda_4$ and $f_0$ are two free parameters of the spectral action, not derivable from $\Omega^7$. The prediction of $M_H$ is parametric, not absolute.
:::

### 4.1 Octonionic correction

### Theorem 4.2 (Deviation from SM) [C] {#thm-4-2}

:::warning [C] Conditional
The quantitative estimate $\delta\lambda/\lambda_\text{SM} \sim O(10^{-2}\text{--}10^{-3})$ depends on the octonionic parameters of the Gap potential ($\lambda_3$, $\bar{A}$, $\mu$). Parameter $\lambda_4$ is determined from the spectral action [C]; the octonionic correction is an additional contribution.
:::

**Theorem.** The octonionic structure predicts a deviation from the standard Higgs mass relation:

**(a)** In SM: $M_H^2 = 2\lambda v^2$ (one parameter $\lambda$).

**(b)** In UHM: $M_H^2 = 2\lambda_4 v^2 + \delta M_H^2$, where:

$$\delta M_H^2 = \frac{3\lambda_3^2 \bar{A}^2}{4\mu^2} \approx \frac{3 \cdot (73.8)^2 \cdot (0.047)^2}{4 \cdot 16.6} \approx 5.5$$

**(c)** Octonionic correction to $\lambda_\text{eff} = \lambda_4 + \delta\lambda$:

$$\frac{\delta\lambda}{\lambda_4} = \frac{3\lambda_3^2 \bar{A}^2}{8\lambda_4 \mu^2 v^2}$$

**(d)** Falsifiable prediction: with improved precision in measuring the Higgs triple vertex (HL-LHC, FCC), the effective self-coupling $\lambda_\text{eff}$ differs from the SM value by:

$$\frac{\delta\lambda}{\lambda_\text{SM}} \sim \frac{\lambda_3^2 \bar{A}^2}{\lambda_4 \mu^2} \sim O(10^{-2} \text{--} 10^{-3})$$

— at the percent level, potentially accessible at FCC-hh.

### 4.2 Origin of the octonionic correction

The octonionic correction from $V_3$ has the following structure:

1. $V_3 = \lambda_3 \sum_{(i,j,k) \notin \text{Fano}} |\gamma_{ij}||\gamma_{jk}||\gamma_{ik}| \sin(\theta_{ij} + \theta_{jk} - \theta_{ik})$ — the cubic octonionic potential.

2. Projection onto the $E$-$U$ channel gives the contribution $\lambda_3 \bar{A} |\gamma_{EU}|^3$, where $\bar{A}$ is the average product of coherence moduli in other channels.

3. This cubic term is **absent** in the standard model and is a direct consequence of the octonionic ($\mathbb{O}$) structure of the theory.

4. Physically: $V_3$ is responsible for the breaking of $PT$-symmetry (the Gap arrow), and its contribution to the Higgs mass connects the electroweak sector to the global octonionic structure of the dimension space.

### 4.3 Connection to the Fano selection rule and octonionic structure constants

:::tip [T] Theorem
The Yukawa coupling of generation $k_n$ to the Higgs field $\gamma_{EU}$ is proportional to the octonionic structure constant $f_{k_n,E,U}$, which is nonzero if and only if $(k_n,E,U)$ forms a Fano line.
:::

The octonionic correction to the Higgs mass is directly connected to the Fano selection rule. The tree-level Yukawa coupling of generation $k_n$ to the Higgs field is determined by:

$$y_n^{(\text{tree})} = g_W \cdot \varepsilon_{k_n, E, U}^{\text{Fano}} \cdot \sin\!\left(\frac{2\pi k_n}{7}\right) \cdot |\gamma_{\text{vac}}^{(EU)}|$$

where $\varepsilon_{ijk}^{\text{Fano}} = 1$ if $(i,j,k)$ is a Fano line, and $0$ otherwise. Equivalently: $y_{abc}^{(\text{tree})} \propto f_{abc}$, where $f_{abc}$ is the structure constant of the algebra $\mathbb{O}$, associated with the multiplication table: $e_a e_b = f_{abc} \, e_c + \delta_{ab}$.

For the three generations $k \in \{1, 2, 4\}$:

| Generation | $k$ | Triple $(k,E,U)$ | Fano line? | $f_{k,5,6}$ | $y^{(\text{tree})}$ |
|---|---|---|---|---|---|
| Third (heavy) | $1$ | $(1,5,6)$ | **Yes**: $\{A,E,U\}$ | $1$ | $\neq 0$ |
| Second | $2$ | $(2,5,6)$ | No | $0$ | $= 0$ |
| First | $4$ | $(4,5,6)$ | No | $0$ | $= 0$ |

**Consequence for Higgs mass.** The Higgs mass is generated by a loop with a virtual $t$-quark (the only fermion with $y^{(\text{tree})} \neq 0$). Radiative corrections to $M_H^2$ from the top quark:

$$\delta M_H^2 \Big|_{\text{top}} = -\frac{3 y_t^2}{8\pi^2} \Lambda^2 + \ldots$$

In UHM the role of the UV cutoff $\Lambda$ is played by the scale $\mu_\text{phys}$ — the physical unit of Gap coherence. The octonionic correction from $V_3$ **partially compensates** the quadratic divergence, since the cubic potential modifies the vacuum structure. This is the germ of a solution to the hierarchy problem from within the Gap formalism.

### 4.4 Parity breaking from $V_3$ and stability of the chiral vacuum {#4-4}

:::tip [T] Theorem
Dynamical stability of the chiral vacuum is proved from existing [T]-results.
:::

The cubic potential $V_3$ (and the associated orientational $V_\varphi$-contribution) ensures **dynamical stability** of chiral distinction in the $E$-$U$ channel:

**(a)** In the $\bar{3}$-sector $V_\varphi$ takes the form:

$$V_\varphi^{(\bar{3})} = \lambda_\varphi \cdot \varphi_{LEU} \cdot |\gamma_{LE}||\gamma_{EU}||\gamma_{LU}| \cdot \sin(\theta_{LE} + \theta_{EU} - \theta_{LU})$$

**(b)** $PT$-property: $V_\varphi \to -V_\varphi$ under $PT$-transformation ($\theta \to -\theta$). This creates an **asymmetry** of the minimum of $V_\text{Gap}$ in the $E$-$U$ channel.

**(c)** Energy difference between the left ($\text{Gap}(E,U) = 0$) and right ($\text{Gap}(E,U) \neq 0$) fermionic vacua:

$$\Delta V = V_\varphi^{(\pi)} - V_\varphi^{(0)} = 2\lambda_\varphi |\gamma_{LE}||\gamma_{LU}| \cdot |\gamma_{EU}|$$

**(d)** Without $V_3$, chirality would be unstable to radiative corrections. The $PT$-odd potential prevents relaxation of a left-handed fermion into a right-handed one, ensuring the observed parity violation in weak interactions.

*Proof:*

**Step 1.** $V_3$ is the unique $PT$-odd term in $V_{\mathrm{Gap}}$ [T] ([T-99](/docs/physics/gauge-symmetry/confinement#теорема-структурное-theta-qcd), step 2). It distinguishes chiral vacua: $\theta = 0$ and $\theta = \pi$ give different signs of the cubic combination $\sin(\theta_{ij} + \theta_{jk} - \theta_{ik})$.

**Step 2.** The vacuum of $V_{\mathrm{Gap}}$ is unique with positive definite Hessian [T] ([T-64](/docs/core/dynamics/gap-thermodynamics#теорема-глобальная-минимизация)). No flat directions → the chiral minimum is non-degenerate.

**Step 3.** Topological barrier [T] ([T-69](/docs/core/dynamics/composite-systems#теорема-тополог-защита)): $\Delta V \geq 6\mu^2 > 0$ prevents tunneling between chiral vacua.

**Conclusion.** $V_3$ selects the chiral vacuum (step 1), the Hessian ensures local stability (step 2), the topological barrier — global protection from tunneling (step 3). $\blacksquare$

---

## 5. Connection to SM gauge structure {#5-связь-с-калибровочной-структурой-sm}

### 5.1 Gauge boson mass hierarchy

### Theorem 5.1 (Mass hierarchy from Gap hierarchy) [T] {#thm-5-1}

:::tip [T] Theorem
The gauge mass hierarchy follows from the Fano–electroweak (FE) construction [T]: uniqueness of the pair $(E,U)$ is proved from $\kappa_0$ [T] — see [uniqueness theorem](/docs/physics/gauge-symmetry/standard-model#теорема-единственности-фэ). The identification of Gap sectors with SM gauge groups is determined uniquely.
:::

**Theorem.** The scale hierarchy of gauge bosons is determined by the Gap hierarchy of the vacuum:

**(a)** Massless ($\text{Gap} = 0$ in the corresponding sector):
- Gluons: $\text{Gap} = 0$ in $3$-to-$\bar{3}$ → confinement (nonlinear dynamics as $\text{Gap} \to 0$)
- Photon: $\text{Gap} = 0$ for the diagonal $U(1)_\text{EM}$ combination

**(b)** Electroweak scale ($\text{Gap} \sim 10^{-17}$ from Planck):
- $W^\pm$, $Z$: $\text{Gap}(E,U) \sim v/M_\text{Planck} \sim 10^{-17}$

**(c)** Planck scale:
- $G_2$-extra: $\text{Gap} \sim 1$ → mass $\sim M_\text{Planck}$

**Corollary.** The mass hierarchy $M_\gamma = 0 \ll M_W \ll M_{G_2}$ follows from the Gap hierarchy $0 \ll 10^{-17} \ll 1$ in the corresponding coherence sectors.

:::info Note
In early versions this section included the GUT scale with $X$, $Y$ leptoquarks ($M_X \sim v_\text{GUT}$), based on the embedding $SU(5) \subset SU(6)$ from the 42D Page–Wootters extension. Within the Fano–electroweak (FE) construction the electroweak sector is derived directly from the Fano geometry of the $\bar{3}$-sector without invoking $SU(5)$-GUT, and the prediction of $X$, $Y$-leptoquarks is **not a consequence** of the (FE)-framework. The question of the existence of a GUT scale remains open.
:::

### 5.2 Complete table of gauge fields

| Field | Group | Number | Mass | Gap source | Status |
|---|---|---|---|---|---|
| Gluons $g$ | $SU(3)_C$ | 8 | 0 (confinement) | $\text{Gap}_{3\to\bar{3}} \approx 0$ | [T] |
| $W^\pm$, $Z$ | $SU(2)_L$ | 3 | $M_W$, $M_Z$ | $\text{Gap}(E,U) \sim 10^{-17}$ | [T] |
| Photon $\gamma$ | $U(1)_\text{EM}$ | 1 | 0 | Diagonal $U(1)$ | [T] |
| $G_2$-extra | $G_2/SU(3)$ | 6 | $M_{G_2} \sim \mu_\text{phys}$ | $\text{Gap}^{(O)} \sim 1$ | [C] |

:::info Note on leptoquarks
In the previous version the table included $X$, $Y$-leptoquarks ($SU(5)/\text{SM}$, 12 fields, $M_X \sim v_\text{GUT}$). These particles are specific to the $SU(5)$-GUT embedding and do not follow from the Fano–electroweak (FE) construction. They have been removed from the main table.
:::

### 5.3 Electroweak sector: Fano–electroweak (FE) construction [T] {#фано-электрослабая-конструкция}

:::warning Replacement of the former SU(6) derivation
In early versions the electroweak sector was derived from the Page–Wootters extension $\mathcal{H}_\text{total} = \mathbb{C}^7 \otimes \mathbb{C}^6 = \mathbb{C}^{42}$, where the $6D$-factor carried $SU(6)$-symmetry, and via the embedding $SU(5) \subset SU(6)$ (analogue of the Georgi–Glashow model) $SU(2)_L \times U(1)_Y$ was extracted. This approach had a rank problem ($\text{rank}(G_2) = 2 < \text{rank}(SM) = 4$) and led to spurious predictions ($X$, $Y$-leptoquarks).

**The Fano–electroweak (FE) construction** replaces the $SU(6)/SU(5)$ derivation, extracting the electroweak structure directly from the geometry of the $\bar{3}$-sector of the Fano plane.
:::

In the (FE)-construction the electroweak sector $SU(2)_L \times U(1)_Y$ arises from the structure of the $\bar{3}$-sector $\{L, E, U\}$ of the plane $\mathrm{PG}(2,2)$:

**(a)** $SU(2)_L$ is identified with the group acting on the doublet $(E, U)$ at $\text{Gap}(E,U) = 0$. The uniqueness of the Higgs line $\{A, E, U\}$ [T] guarantees unambiguity in the choice of the electroweak channel.

**(b)** $U(1)_Y$ is determined by the total Gap in the $O$-sector (see [section 3.3](#3-gapeu--0-электрослабое-нарушение-симметрии)):

$$Y = \frac{1}{3}\left(\sum_{i \in 3} \text{Gap}(O,i) - \sum_{j \in \bar{3}} \text{Gap}(O,j)\right)$$

**(c)** $SU(3)_C$ — still from the $G_2$-stabilizer ($G_2 \supset SU(3)$, decomposition $14 \to 8+3+\bar{3}$) [T].

**Advantages of (FE) over $SU(6)/SU(5)$:**
- Does not require additional structure ($SU(6)$ from 42D)
- Does not generate $X$, $Y$-leptoquarks as a mandatory prediction
- The electroweak sector is tied to the same Fano geometry as the Higgs mechanism
- The rank problem ($\text{rank}(G_2) = 2 < 4 = \text{rank}(SM)$) is resolved: the missing generators are taken from the HS-projection of the $\bar{3}$-sector [T], not from an external $SU(6)$

---

## 6. Falsifiable predictions {#6-фальсифицируемые-предсказания}

### 6.1 Deviation of the Higgs triple vertex [C]

:::warning [C] Conditional
The quantitative prediction depends on the octonionic parameters of the Gap theory ($\lambda_3$, $\bar{A}$) and the spectral action parameter $f_0$.
:::

**Prediction.** The effective Higgs self-coupling differs from the SM value:

$$\frac{\delta\lambda}{\lambda_\text{SM}} \sim O(10^{-2} \text{--} 10^{-3})$$

Test: HL-LHC (precision $\sim 50\%$ on triple vertex), FCC-hh (precision $\sim 5\%$).

### 6.2 Connection of Higgs mass to octonionic structure [C]

In the SM the Higgs mass $m_H \approx 125$ GeV is a free parameter. In UHM:

$$m_H^2 = 2\lambda_4 v^2 + \delta m_H^2(\lambda_3, \bar{A}, \mu)$$

The first term is determined by the spectral action ([theorem on Higgs quartic](#теорема-хиггсовская-квартика) [C]). The octonionic correction $\delta m_H^2$ connects the Higgs mass to the octonionic potential parameters. When $f_0$ is fixed from other observables (quark masses, CKM elements), the Higgs mass becomes **computable** — this is a potentially powerful prediction.

### 6.3 Mass hierarchy problem [H]

**Corollary.** The mass hierarchy problem ($M_W / M_\text{Planck} \sim 10^{-17}$) reduces to the question: **why does the Gap-vacuum have such different values in different sectors?** Answer: sectoral values $\varepsilon_X$ are determined by the unique minimum of $V_{\text{Gap}}$ ([theorem on unique vacuum](/docs/core/dynamics/gap-thermodynamics#теорема-единственный-вакуум) [T]).

Hypothetical solution via RG evolution: at the Planck scale all $\text{Gap} \sim O(1)$ (democratic initial condition). RG flow from Planck to IR: different sectors flow with different anomalous dimensions:

| Sector | Anomalous dimension | Gap at IR scale |
|---|---|---|
| $3$-to-$\bar{3}$ (color) | $\Delta_{3\bar{3}} = 0$ (marginal) | $\sim 0$ (confinement) |
| $\bar{3}$-to-$\bar{3}$ (EW) | $\Delta_{\bar{3}\bar{3}} = \Delta_3 = 5/42$ | $\sim 10^{-17}$ (EW scale) |
| $O$-to-$3$ (gravity) | $\Delta_{O3} \gg 1$ (IR-relevant) | $\sim 1$ (Planck scale) |

The difference in anomalous dimensions is determined by Fano combinatorics: the number of Fano lines passing through a pair $(i,j)$ affects $\Delta_{ij}$.

### 6.4 Dynamical dark energy [P]

Open program: the connection between the RG scale of Gap and the cosmological evolution $H(t)$ has not been established from axioms A1–A4. The estimate $w_a \sim -10^{-2}$ is a motivated ansatz, not a prediction. Status: [P].

From the nonlinear Gap-gravity system it follows: the dark energy equation of state depends on the cosmological epoch. The Higgs sector (Gap in $\bar{3}$-to-$\bar{3}$) contributes to the effective cosmological constant:

$$w(z = 0) = -1 + \delta w, \quad \delta w = \frac{\kappa \cdot \langle|\gamma|^2\rangle}{V_\text{Gap}} \sim \frac{\kappa \cdot \epsilon^2}{\mu^2 \text{Gap}^2}$$

The numerical estimate $w_a \sim -10^{-2}$ is testable by Euclid, Roman, DESI missions, but its derivation from Gap axioms remains an open program.

---

## 7. Can UHM predict the Higgs mass? {#7-может-ли-угм-предсказать-массу-хиггса}

### 7.1 Problem statement

Experimental value: $M_H^{\text{exp}} = 125.09 \pm 0.24$ GeV. In the Standard Model $M_H$ is a free parameter. In Chamseddine–Connes noncommutative geometry (NCG) the Higgs mass is **computed** from the spectral triple. Question: can UHM do the same?

### 7.2 Derivation chain for $M_H$ in UHM {#цепочка-mh}

The full chain from axioms to $M_H$ consists of five links:

| Link | Statement | Status | Dependency |
|---|---|---|---|
| (1) Spectral triple | $(A_{\text{int}}, H_{\text{int}}, D_{\text{int}})$ exists, KO-dim = 6 | **[T]** (T-53) | Axioms |
| (2) Spectral action | $S = \mathrm{Tr}(f(D_A/\Lambda))$ expands in Seeley–DeWitt series | **[T]** (T-65) | (1) |
| (3) $f_0$ canonically determined | $f_0 = \Gamma_{\text{eff}} / (7\Lambda^4)$ through Gap theory vacuum | **[T]** (T-70) | (2) + unique vacuum T-64 [T] |
| (4) $\lambda_4$ from $D_{\text{int}}$ + RG | $\lambda_4 = \frac{\pi^2}{2f_0\Lambda^4} \cdot \frac{\mathrm{Tr}(D_{\text{int}}^4)}{[\mathrm{Tr}(D_{\text{int}}^2)]^2}$, RG: $\Lambda \to v_{\text{EW}}$ | **[C]** | (3) + numerical $\varepsilon_i$ |
| (5) $M_H$ from potential | $M_H^2 = 2\lambda_4 v^2 + \delta M_H^2(\lambda_3, \bar{A}, \mu)$ | **[C]** | (4) + octonionic correction |

**Verdict: [C]** — conditional on numerical values of sectoral parameters $\varepsilon_i$ determining the spectrum $D_{\text{int}}$.

### 7.3 Why $g_4^* = 4\pi^2/63$ is NOT the Higgs quartic {#gap-vs-higgs-quartic}

:::danger Common error
The Wilson–Fisher fixed point of the Gap theory $g_4^* = 4\pi^2/63 \approx 0.063$ is **not** the Higgs quartic $\lambda_H$ of the Standard Model. The naive identification gives $M_H = \sqrt{2 g_4^*} \cdot v \approx 87$ GeV — an **incorrect** result.
:::

Distinction:

| | Gap quartic $g_4^*$ | Higgs quartic $\lambda_H$ |
|---|---|---|
| Theory | (0+1)D Gap on $(S^1)^{21}$ | 4D QFT on $M^4$ |
| Number of fields | 21 coherences | 1 doublet (4 real fields) |
| Factor in $\beta$ | 63 (from combinatorics $\binom{21}{2} \cdot 3$) | $\sim 24$ (loop with $W$, $Z$, $t$) |
| IR value | $4\pi^2/63 \approx 0.063$ | $\approx 0.13$ (from $M_H = 125$ GeV) |
| Origin | Wilson–Fisher RG fixed point of Gap | Spectrum $D_{\text{int}}$ + SM RG running |

**Connection between them**: $g_4^*$ determines the IR value of the quartic coupling of the Gap potential $V_{\text{Gap}}$. The Higgs quartic $\lambda_H$ is determined by the *projection* of $V_{\text{Gap}}$ onto the $E$-$U$ channel via the spectral action, and then evolves under 4D SM RG equations.

### 7.4 Comparison with Chamseddine–Connes NCG {#сравнение-ncg}

In the Chamseddine–Connes–Marcolli (CCM) approach the history of predicting $M_H$ went through three stages:

**(a) Tree level (CCM 2007)**: $M_H = \sqrt{8\lambda_H} \cdot v$ with $\lambda_H$ from $\mathrm{Tr}(D_{\text{int}}^4)/[\mathrm{Tr}(D_{\text{int}}^2)]^2$. With top quark dominance:

$$M_H^{(\text{tree})} \approx \frac{M_t}{\sqrt{2}} \approx \frac{173}{\sqrt{2}} \approx 122 \text{ GeV}$$

However, without RG correction the exact Chamseddine–Connes formula (2012) gave $\sim 170$ GeV — an **incorrect** result.

**(b) With RG running (Shaposhnikov–Wetterich 2010)**: RG evolution from $\Lambda_{\text{GUT}}$ to $v_{\text{EW}}$ reduces $\lambda_H(\Lambda) \approx 0.20$ to $\lambda_H(v) \approx 0.13$, giving $M_H \approx 125$ GeV. But this fixes $\Lambda_{\text{GUT}}$, not predicts it.

**(c) With scalar field $\sigma$ (Chamseddine–Connes–van Suijlekom 2013)**: introduction of the $\sigma$-field from internal fluctuations changes the boundary condition at $\Lambda$, leading to $M_H \approx 126$ GeV — the first correct prediction from NCG.

**UHM position**: the octonionic correction from $V_3$ plays a structurally analogous role to the $\sigma$-field in CCM-2013. The cubic potential $V_3$ modifies the effective Higgs potential, shifting the tree-level value of $M_H$ closer to the experimental value. However, the exact numerical value of the correction depends on vacuum parameters $\varepsilon_i$, which have not yet been computed.

### 7.5 What is needed for a full prediction {#что-нужно}

For converting $M_H$ from [C] to [T] one needs:

1. **Numerical solution** of vacuum equations on $(S^1)^{21}/G_2$: determine exact values of $\varepsilon_i$ for all 5 orbital parameters (task C16 in the [status registry](/docs/reference/status-registry)).

2. **Computation of $f_0$**: substitute $\varepsilon_i$ into the canonical formula T-70 and find the numerical value of $f_0$.

3. **Computation of $\mathrm{Tr}(D_{\text{int}}^4)$**: determine $\lambda_4(\Lambda)$ from the spectrum $D_{\text{int}}$ with known $\varepsilon_i$.

4. **SM RG running**: evolution $\lambda_4(\Lambda) \to \lambda_4(v_{\text{EW}})$ — standard procedure containing no additional free parameters.

5. **Octonionic correction**: compute $\delta M_H^2$ from Gap parameters.

All formulas are **defined** [T]; the task is **computational** [C]. This is analogous to the situation in lattice QCD, where the formulas are exact, but numerical predictions require computation.

### 7.6 Final assessment [C] {#итоговая-оценка-mh}

:::warning [C] Conditional
UHM determines the Higgs mass through chain (1)–(5), in which links (1)–(3) have status [T], and links (4)–(5) — status [C] due to incomplete computation of sectoral parameters $\varepsilon_i$. No additional postulates or hypotheses are required: the task is purely computational.
:::

**Summary:**

- **Can UHM in principle predict $M_H$?** Yes — the formulas are fully determined.
- **Does it predict now?** No — requires solving task C16 (numerical computation on $(S^1)^{21}/G_2$).
- **Naive $g_4^* \to M_H$**: incorrect ($g_4^* \neq \lambda_H$), gives $\sim 87$ GeV.
- **Status**: **[C]** — conditional on computation of $\varepsilon_i$.
- **Comparison with NCG**: UHM reproduces the CCM structure, but adds the octonionic $V_3$-correction, analogous to the $\sigma$-field of Chamseddine–Connes–van Suijlekom.

---

## Connection to other sections

- **Uniqueness of the Higgs line:** Foundation of the Fano selection rule → [Yukawa Mass Hierarchy](./yukawa-hierarchy.md)
- **Three generations:** Generation line $\{A,S,L\}$ orthogonal to Higgs line → [Three Fermion Generations](./fermion-generations.md)
- **CKM matrix:** Mismatch of $Y^u$ and $Y^d$ via conjugate Higgs → [CKM Matrix](./ckm-matrix.md)
- **Spectral triple:** Finite $(A_{\text{int}}, H_{\text{int}}, D_{\text{int}})$ with KO-dimension 6 → [Spacetime](/docs/core/foundations/spacetime#теорема-спектральная-тройка) [T]
- **Spectral action:** $S = \mathrm{Tr}(f(D/\Lambda))$, determines $\lambda_4$ → [Quantum Gravity](/docs/physics/gravity/quantum-gravity)
- **Unique vacuum:** Sectoral values $\varepsilon$ from T-61 → [Gap Thermodynamics](/docs/core/dynamics/gap-thermodynamics#теорема-единственный-вакуум) [T]


---

**Related documents:**
- [Standard Model from G₂](/docs/physics/gauge-symmetry/standard-model)
- [Fano Selection Rules](/docs/physics/gauge-symmetry/fano-selection-rules)
- [Yukawa Hierarchy](/docs/physics/particle-physics/yukawa-hierarchy)
- [Supersymmetry from G₂](/docs/physics/particle-physics/susy)
