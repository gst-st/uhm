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
- **[D]** Definition — definition by convention
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

### 1.1 Identification of the Higgs field [H] {#отождествление-хиггса}

In UHM the Higgs field is identified with the $E$-$U$ coherence in the $\bar{3}$-to-$\bar{3}$ sector:

$$H \sim \gamma_{EU} = |\gamma_{EU}| e^{i\theta_{EU}}$$

Dimensions $E$ (evaluation) and $U$ (unity) belong to the $\bar{3}$-sector $\{L, E, U\} = \{4, 5, 6\}$. The pair $(E, U)$ defines the electroweak channel: $\text{Gap}(E,U) = 0$ corresponds to a weak doublet, $\text{Gap}(E,U) \neq 0$ — to a singlet.

#### Theorem 1.0 (Identification $H \sim \gamma_{EU}$) — corrected from [T] to [H] {#теорема-отождествление-хиггса}

:::danger Corrected 2026-09-25 (audit A-90): a vacuum value of $\gamma_{EU}$ breaks colour
Checked numerically with $SU(3)_C = \mathrm{Stab}_{G_2}(e_O)$, the colour group of the corpus. The state $\Gamma = I/7 + \varepsilon\,(e^{i\phi}|E\rangle\langle U| + \text{h.c.})$ keeps a subalgebra of $\mathfrak{su}(3)_C$ of dimension 1 at $\phi = \pi/2$ (and $3\pi/2$) and of dimension 0 at the other 23 of 25 sampled phases, against 8 at $\varepsilon = 0$; the coherence $\gamma_{EU}$ has no colour-singlet component, since the $SU(3)_C$-invariant states have coherences only on $(A,D)$, $(S,U)$, $(L,E)$ (`test_gamma_eu_vev_breaks_colour`). So $\langle\gamma_{EU}\rangle \neq 0$ breaks $SU(3)_C$, while the Standard-Model Higgs is a colour singlet. Steps 3 and 4 below fail as well: no $SU(2)$ commutes with $SU(3)_C$ on $\mathbb C^7$ (the commutant is $\mathbb C^3$), so there is no doublet $(2,+1/2)$ to carry, and the vacuum value came from T-64, which is restated as a hypothesis whose vacuum has no sector values; $E$ and $U$ are not in a sector $\bar{\mathbf 3} = \{L,E,U\}$ (T-48a retracted).

Repairs tried. (i) Correct complex triplets: $\gamma_{EU}$ has zero singlet weight, as above. (ii) Another colour group: $\gamma_{EU}$ is invariant under $\mathrm{Stab}_{G_2}(e_A)$, but only inside the combination with equal coherences on $(S,L)$ and $(D,O)$ — the pairs of the lines through $A$ — and this moves colour from $O$ to $A$, against the rest of the corpus. (iii) A doublet on $\mathbb C^7$: impossible for any $SU(3)$, for the commutant reason above. (iv) The Clifford frame of [T-326](/docs/physics/gauge-symmetry/standard-model#sm-из-клиффорда) restricted to $\mathrm{Spin}(9)$, where an $SU(2)$ does exist — the centraliser of colour in the $\mathrm{Spin}(9)$ of $\mathcal S = \mathbb C\otimes\mathbb O$, which T-329 shows to be the diagonal of $SU(2)_L\times SU(2)_R$: it gives $H \sim \gamma_{EU}$ no support. $\mathcal S = (\mathbf 3,\mathbf 2)_{1/6} \oplus (\mathbf 1,\mathbf 2)_{-1/2}$ contains doublets only, so every operator on $\mathcal S$ — every coherence of $\Gamma$, $\gamma_{EU}$ included — carries integer $SU(2)_L$ spin ($\mathbf 2\otimes\mathbf 2 = \mathbf 1\oplus\mathbf 3$); and the vector $\mathbb R^9$ of the Clifford system is $(\mathbf 3\oplus\bar{\mathbf 3},\mathbf 1)_{\pm1/3} \oplus (\mathbf 1,\mathbf 3)_0$ — no doublet either (`test_no_higgs_doublet_in_the_clifford_frame`). *(Narrowed 2026-09-25: this absence holds for $\mathrm{Spin}(9)$ only.)* In the $\mathrm{Spin}(10)$ completion, where the tenth Clifford generator is forced, the colour-free Clifford plane $\{iL_{e_O}, J, iJ, \gamma_{10}\}$ is one Higgs doublet with $Y = \pm\tfrac12$ — [T] as a representation, the identification [H] — and a vacuum in the plane $\{iL_{e_O}, \gamma_{10}\}$ leaves exactly $SU(3)\times U(1)_Q$ ([standard model, Theorem 2.6(f)](/docs/physics/gauge-symmetry/standard-model#поколение-t329)). That doublet is a direction of the Clifford vector, not a coherence of $\Gamma$, so it gives $H \sim \gamma_{EU}$ no support either. What stands [T]: Step 1 (T-42a) and Step 2 (Theorem 1.1). The identification $H \sim \gamma_{EU}$ is a hypothesis [H] with three named obstructions: colour breaking under $SU(3)_C = \mathrm{Stab}(e_O)$, the absence of a doublet on $\mathbb C^7$, and the absence of a doublet among the operators on $\mathcal S$ and in the vector of $\mathrm{Spin}(9)$. The Higgs doublet of the corpus is the one of Theorem 2.6(f).
:::

:::info Remark (the Gap vacuum and the Higgs plane) [I]
Under [T-64](/docs/core/dynamics/gap-thermodynamics#теорема-глобальная-минимизация) in its corrected form ([T] in the Gap phase) the imaginary part of the vacuum is $\mathrm{Im}\,\Gamma_v = \tfrac{b-c}{2}L_{e_O}$: the restriction to $\mathbb C^7$ of the clock generator $L_{e_O}$, one of the four directions of the colour-free Clifford plane of Theorem 2.6(f). Its stabiliser in $G_2$ is $\mathrm{SU}(3)_{e_O}$, and the stabiliser in $\mathfrak g_{\mathrm{SM}}$ of a vector of the plane $\{iL_{e_O}, \gamma_{10}\}$ is $\mathfrak{su}(3)\oplus\mathfrak u(1)_Q$. That the Gap condensate and the Higgs vacuum point along the same clock direction is a reading, not a derivation: $\Gamma$ lives on $\mathbb C^7$, the doublet on the Clifford vector $\mathbb R^{10}$, and no map between them is given.
:::

:::note Earlier statement (Theorem 1.0, stated as [T] until 2026-09-25)
The identification $H \sim \gamma_{EU}$ is strictly proved from four independent [T]-results: categorical uniqueness of the pair $(E,U)$, uniqueness of the Higgs line, $SU(2)_L \times U(1)_Y$ quantum numbers, and nonzero vacuum expectation value from the unique vacuum. *(Corrected: see the box above.)*
:::

**Theorem.** The coherence $\gamma_{EU}$ is the unique candidate for the Higgs field in UHM, and the identification $H \sim \gamma_{EU}$ is proved from the following chain.

**Step 1. Categorical uniqueness of the pair $(E,U)$ [T] (T-42a).**

The formula $\kappa_0 = \omega_0 \cdot |\gamma_{OE}| \cdot |\gamma_{OU}| / \gamma_{OO}$ categorically singles out exactly the pair $(E,U)$ via morphisms $\mathrm{Hom}(O,E)$ and $\mathrm{Hom}(O,U)$. No other pair of dimensions has this property: replacing with $\{L,U\}$ removes $\mathrm{Hom}(O,L)$ from $\kappa_0$; replacing with $\{L,E\}$ excludes $U$, breaking the normalization $\mathrm{Tr}(\Gamma) = 1$. Uniqueness is proved — see [Theorem of FE-uniqueness](/docs/physics/gauge-symmetry/standard-model#теорема-единственности-фэ) [T].

**Step 2. Uniqueness of the Higgs line $\{A,E,U\}$ [T] (Theorem 1.1).**

Through any two points of $\mathrm{PG}(2,2)$ there passes exactly one line. The unique Fano line containing both points $E = 5$ and $U = 6$: $\{5,6,1\} = \{A,E,U\}$. This line defines the electroweak sector — see [Theorem 1.1](#thm-1-1) [T].

**Step 3. Quantum numbers of $\gamma_{EU}$ coincide with those of the SM Higgs doublet [T].**

From the electroweak uniqueness theorem ([§2.3a](/docs/physics/gauge-symmetry/standard-model#теорема-единственности-фэ) [T]): the pair $(E,U)$ forms the doublet $2_{EU}$ under $SU(2)_L$. The coherence $\gamma_{EU}$ — a bilinear form connecting $E$ and $U$ — transforms as $(2, +1/2)$ under $SU(2)_L \times U(1)_Y$. This is exactly the quantum numbers of the SM Higgs doublet.

**Step 4. Nonzero VEV $\langle\gamma_{EU}\rangle \neq 0$ breaks $SU(2)_L \times U(1)_Y \to U(1)_\text{em}$ [T].**

From [Theorem on the unique vacuum T-64](/docs/core/dynamics/gap-thermodynamics#теорема-глобальная-минимизация) [T] (corrected to the $G_2$-invariant potential; its vacuum has no sector values — hypothesis (SV)): the unique global minimum of $V_\text{Gap}$ has $|\gamma_{EU}|_\text{vac} = \varepsilon_{\bar{3}\bar{3}} \approx 10^{-17}$ (in units of $\omega_0$), giving $\langle\gamma_{EU}\rangle \neq 0$. A nonzero vacuum expectation value of a field with quantum numbers $(2, +1/2)$ uniquely realizes spontaneous breaking $SU(2)_L \times U(1)_Y \to U(1)_\text{em}$.

**Conclusion (earlier, corrected 2026-09-25).** The earlier text read: "All four steps rely exclusively on [T]-results. The identification $H \sim \gamma_{EU}$ follows from them uniquely." Steps 3 and 4 are withdrawn (box above), so the identification is a hypothesis [H].

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
The assignment $k=1 \to$ 3rd generation is strictly proved from the unique nonzero tree-level Yukawa coupling — see [Theorem 4.1 (Assignment of 3rd generation)](/docs/physics/particle-physics/fermion-generations#thm-gen-4-1). The complete ordering ($k=4 \to$ 2nd, $k=2 \to$ 1st) is strictly proved — [Theorem 4.3](/docs/physics/particle-physics/fermion-generations#thm-gen-4-3) [T]. The number of generations $N_{\text{gen}} = 3$ has composite status **count [T], identification [I]**: the count is the exact cardinality $|\mathrm{QR}(7)| = (7-1)/2 = 3$ **[T]** (group-theoretic, topology-independent), and only the physical identification of the classes with generations is [I] — see [Theorem $N_{\text{gen}} = 3$](/docs/physics/particle-physics/fermion-generations#теорема-ровно-три-генерации).
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

2. **From Fano structure:** the unique Fano line through $E$ and $U$ is $\{A,E,U\}$ (the registry-canonical Higgs line, T.1.3; its third point $A$ lies in the $3$-sector — **no** Fano line lies entirely within $\bar 3=\{L,E,U\}$, since $\{L,E,U\}=\{4,5,6\}$ is not a line). The chirality operator $\Gamma_{AEU}$ is defined by this line. $\text{Gap}(E,U)$ is the specific coherence broken by the Higgs, while the remaining line-coherences $\text{Gap}(A,E)$ and $\text{Gap}(A,U)$ fix the doublet embedding.

3. **Physical:** $E$-dimension $\leftrightarrow$ evaluative structure $\leftrightarrow$ electric charge. $U$-dimension $\leftrightarrow$ unification $\leftrightarrow$ weak isospin. At $\text{Gap}(E,U) = 0$ they are indistinguishable → $SU(2)_L$ doublet. At $\text{Gap}(E,U) \neq 0$ they are distinguishable → singlets.

### 1.6 Yukawa couplings in the Clifford frame: what splits up from down (T-332) {#юкавы-t340}

:::tip[Status: Theorem 1.6 (a)–(e) is \[T\] as mathematics and \[C at (Cl)\] in UHM; the hypothesis (UP) of (f) is \[H\] at leading order and refuted \[✗\] in its exact form (T-332(h)–(k), §1.7); the Yukawa structure itself — $m_t/m_b$, $y_t$, CKM — stays open \[Pr\]]
[Theorem 2.6(f)](/docs/physics/gauge-symmetry/standard-model#поколение-t329) of the Standard Model page puts the Higgs doublet in the colour-free Clifford plane of $\mathrm{Spin}(10)$ and notes that one Clifford multiplication gives $m_t=m_b=m_\tau$. This section finds what in UHM can separate up from down, classifies every Yukawa coupling by the stage of the clock's symmetry breaking, and compares with the masses. Registry row T-332; checks in `website/scripts/check_core_numbers.py`.
:::

**Setting.** Notation of the Standard Model page, §2.6: $\mathcal S_{\mathbb C}=V_L\oplus V_R$, field unit $\omega$, Clifford vectors $\gamma_a$, colour-free plane $P=\{iL_{e_O},J,iJ,\gamma_{10}\}$ with neutral directions $\{iL_{e_O},\gamma_{10}\}$. A Yukawa coupling is a real-linear map $h\mapsto M(h)$ from $P$ to $\omega$-antilinear operators $V_L\to V_R$ — the Dirac form of Theorem 2.6(f) — that is equivariant under a group $G$: $M(gh)=gM(h)g^{-1}$. The masses of $u,d,\nu,e$ are the singular values of $M(\langle h\rangle)$ between the matching components.

**Theorem 1.6 (T-332).**

**(a) Up and down are where the two units meet [T].** The operator $\tau := -iL_{e_O}$ on $\mathcal S_{\mathbb C}$ is a symmetric involution. It equals $+1$ on $u_L,\nu_L,u^c,\nu^c$ and $-1$ on $d_L,e_L,d^c,e^c$, on both halves alike. So the up-type fields are the vectors on which the imaginary unit of $\mathcal H$ acts as the clock's left multiplication, $i=L_{e_O}$, and the down-type fields those with $i=-L_{e_O}$. On $\mathbb C^7\subset\mathcal S$ the two eigenspaces of $L_{e_O}$ on $e_O^\perp$ — the "triplet" $P_{\mathbf 3}$ ($L_{e_O}=-i$) and "antitriplet" $P_{\bar{\mathbf 3}}$ ($L_{e_O}=+i$) of [T-64](/docs/core/dynamics/gap-thermodynamics#теорема-глобальная-минимизация) — are the down and up components of the left-handed quark doublet. In the field's complex structure both are colour triplets. $\tau_R:=\tau|_{V_R}$ commutes with $\mathfrak g_{\mathrm{SM}}$. On $V_L$, $\tau$ is twice $T_{3L}$ and does not commute with $\mathfrak{su}(2)_L$.

**(b) Classification by the stages of the clock's breaking [T].** The real dimension of the space of Yukawa couplings is:

| symmetry of the coupling | dimension | relations for every vacuum in the neutral plane |
|---|---|---|
| Pati–Salam, $\mathfrak c(L_{e_O})$ (21) | 2 | $m_u=m_d=m_\nu=m_e$ (as for $\mathrm{Spin}(10)$) |
| left–right, $\mathfrak c(L_{e_O},R_{e_O})$ (15) | 4 | $\lvert m_u\rvert=\lvert m_d\rvert$, $\lvert m_\nu\rvert=\lvert m_e\rvert$ |
| $\mathfrak g_{\mathrm{SM}}$ (12) | 8 | none: four independent masses |

At the last stage every coupling is $M(h)=p(B-L,\tau_R)\,\gamma(h)$, with $p$ a polynomial whose coefficients lie in $\mathrm{span}\{1,\omega\}$. The eight operators $\{1,\omega\}\otimes\{1,B-L\}\otimes\{1,\tau_R\}$ applied to $\gamma(h)$ span the space. Up is separated from down only by $\tau_R$, the imaginary unit of $\mathcal H$ on the right-handed half. It is the same operator that defines the hypercharge, $Y=(B-L)/2+(i/2)|_{V_R}$ (Theorem 2.6(d)). In Standard-Model language the coupling $\gamma(h)(1-\tau_R)/2$ is $Q\tilde H u^c$ and $\gamma(h)(1+\tau_R)/2$ is $QHd^c$.

**(c) Real versus complex vacuum [T].** With any coupling invariant under $\mathrm{SU}(2)_R$, a real vacuum in the neutral plane gives equal moduli. Its angle in the plane is a hypercharge rotation, and it moves only the phases, $m_u\propto e^{\omega\vartheta}$, $m_d\propto e^{-\omega\vartheta}$. The complexified plane contains the isotropic vectors $\gamma_{10}\pm\omega\,iL_{e_O}$. The first gives mass only to $u$ and $\nu$, the second only to $d$ and $e$. These are the two doublets of a complex bidoublet, with $m_t/m_b=\lvert h_u/h_d\rvert=\tan\beta$. This is the complex $\mathbf{10}$ of $\mathrm{SO}(10)$, and its price is a second doublet (T-296, [§6.0](#запрет-второго-дублета)).

**(d) The clock phase does not split the moduli [T].** Dressing the coupling by $e^{\varphi X}$, $X\in\{i, L_{e_O},\omega,B-L\}$ — among them the Page–Wootters phase generated by $i$ — keeps $\lvert m_u\rvert=\lvert m_d\rvert$ and $\lvert m_\nu\rvert=\lvert m_e\rvert$. It changes only the arguments of the masses.

**(e) The Gap vacuum does not split in the observed way [T for the identities; the scan is numerical].** The colour-invariant vacuum of T-64 is
$$\Gamma_v=a\,|O\rangle\langle O|+\tfrac{b+c}{2}\,\Pi_6-\tfrac{b-c}{2}\,\tau|_{\mathbb C^7},\qquad \mathcal G_{\text{total}}=\lVert\mathrm{Im}\,\Gamma_v\rVert^2=\tfrac32(b-c)^2 .$$
Its imaginary part points along $iL_{e_O}$, one real neutral direction, so by (c) it gives equal moduli (the remark of §1.1). Its Gap parameter $b-c$ is the $T_{3L}$-component of $\Gamma_v$ on the quark doublet. Extended to $\mathcal S$ with weight $t$ on $\eta_0$, $\Gamma_v$ commutes with $\mathfrak{su}(2)_L$ only for $b=c$ and $t=a$; even $I/7$ with $t=0$ does not. Read as population weights of a Yukawa coupling ($u$: weight $c$; $d$: $b$; $\nu$ and $e$: $a/2$ each, since $e_O$ is half $\nu_L$ and half $e_L$), the vacuum gives a lepton-to-heavy-quark ratio between $0.46$ and $0.95$ on 99 points of the Gap phase. On the rank-4 branch at $\lambda_4=0$ the ratio is at least $1/2$ analytically. The data give $m_\tau/m_t=0.022$, and $m_\nu=m_e$ is excluded as well.

**(f) What the data ask for [numbers; hypothesis (UP) [H]].** One-loop Standard-Model running from $M_Z$ (inputs $m_t(m_t)=162.5$ GeV, $m_b(m_b)=4.18$ GeV, $m_\tau=1.777$ GeV, $\alpha_s(M_Z)=0.118$) gives $m_t/m_b\approx55$ at $M_Z$. At $2\times10^{16}$ GeV it gives $y_t=0.443$, $y_t/y_b\approx68$ and $y_b/y_\tau\approx0.66$. The Clifford relations $m_t=m_b$ and $m_b=m_\tau$ therefore fail by a factor of 68 and by 34%. Written as $(\alpha+\beta\tau_R)\gamma(h)$, the data require $\beta/\alpha=(y_t-y_b)/(y_t+y_b)=0.971$. At the unification scale the coupling is the projection onto $i=L_{e_O}$ to within 1.5%: at leading order only up-type fields couple. **Hypothesis (UP):** *the tree-level Yukawa coupling is $\gamma(h)$ followed by the projection onto $V_R\cap\{i=L_{e_O}\}$.* Its consequences: $y_b=y_\tau=0$ at tree level; one $O(1)$ coupling $y_t$; and a Dirac neutrino coupling $y_\nu^D=y_t$. With $m_{\nu_3}\approx0.05$ eV the seesaw then puts $M_R=m_D^2/m_{\nu_3}\approx1.2$–$1.4\times10^{14}$ GeV, the order of the [neutrino page](/docs/physics/particle-physics/neutrino-masses#seesaw). (UP) is not derived. No principle of UHM found so far fixes $\beta/\alpha$, and $m_t/m_b$ is not predicted. *Update (T-332(h)–(k), [§1.7](#голоморфность-вп)):* (UP) is holomorphy of the coupling in one complex doublet. In its exact form it leaves $e$, $\mu$ and $\tau$ massless to all orders and is refuted [✗]. Only the leading-order statement, with a breaking $\varepsilon=1-\beta/\alpha\approx0.03$, remains [H].

**(g) Mixing [T for the statement].** Suppose every generation couples through one flavour matrix times the same internal operator. Then $M_u\propto M_d$ and $V_{\mathrm{CKM}}=1$, which $\lvert V_{us}\rvert=0.2243$ refutes. Mixing needs at least two flavour matrices carrying different internal operators. In $\mathrm{SO}(10)$ language these are the $\mathbf{10}$ with the $\overline{\mathbf{126}}$ or the $\mathbf{120}$; the bidoublet coupling of the $\overline{\mathbf{126}}$ is the $(B-L)$-dressed one, with lepton-to-quark ratio $-3$. Under (GC) the family index lives on the clock register ([T-328](/docs/physics/particle-physics/fermion-generations#поколения-t328)). Nothing here fixes the flavour matrices, so the CKM hierarchy stays open.

**Proof.** (a) $i$ and $L_{e_O}$ commute and both square to $-1$, so $\tau$ is a symmetric involution. Its sign on each component is computed from the charges $T_{3L}$, $T_{3R}$, $B-L$ of Theorem 2.6(d). (b) The dimensions solve the linear equivariance system on $\mathrm{Hom}(P,\mathrm{Hom}(V_L,V_R))$ restricted to $\omega$-antilinear maps. For the Pati–Salam value, $(\mathbf 1,\mathbf 2,\mathbf 2)$ meets $(\mathbf 4,\mathbf 2,\mathbf 1)\otimes(\mathbf 4,\mathbf 1,\mathbf 2)$ once. For the left–right value, $B-L$ commutes with the algebra. The equal moduli at the left–right stage: the bidoublet occurs once in each sector's Hom-space, and a real bidoublet satisfies $\tilde\Phi=\Phi$, so only one coupling per sector exists. (c), (d) Clifford multiplication by a unit vector is an isometry, and the dressings are unitary and preserve every component. The isotropic vectors are $\gamma_{10}(1\pm\tau)$ on $V_L$. (e) The formula for $\Gamma_v$ is the colour-invariant family of T-64 with $iL_{e_O}=-\tau$ on $\mathbb C^7$. The scan uses the closed-form sector minimum of T-64(e). On the rank-4 branch $s=b=\tfrac14-\mu^2/(384\kappa)$ and $a=1-3s$, so $(a/2)/b\ge\tfrac12$. $\blacksquare$

Witnesses: `test_up_and_down_are_where_the_hilbert_unit_meets_the_clock`, `test_clifford_yukawas_split_up_from_down_only_through_tau_r`, `test_clock_phase_and_gap_vacuum_dressings_do_not_fit_the_masses`, `test_the_data_ask_for_an_up_projector_at_one_percent`.

**Routes tried and what they give.** (i) One Clifford multiplication: $m_t=m_b=m_\tau$ — fails by a factor of 68. (ii) The Page–Wootters clock phase: phases only (d). (iii) The associator vacuum of T-331/T-64: a real direction, and its populations give $m_\tau\gtrsim m_t/2$ (e). (iv) Two components of the bidoublet with independent vacua: they split, but $\tan\beta$ is free and a second doublet is needed (c). (v) The $\overline{\mathbf{126}}$/$\mathbf{120}$ channels: they give $B-L$ dressing and mixing, not the up–down split, which in every channel with one real doublet comes from $\tau_R$ alone (b). No route fixes $m_t/m_b$.

**Reconciliation with T-296 and with (GC).** The real colour-free plane is exactly one doublet. A scalar needs no complexification, unlike the Weyl field of Theorem 2.6(a), so "one doublet" (T-296) is what the Clifford frame gives when the Higgs field is real. With one doublet the split must come from $\tau_R$ — (UP), or any $\beta\ne0$ — and the two-doublet route (c) contradicts T-296. T-296 stays [H] with this new basis. Under (GC) statement (b) holds generation by generation, and the flavour matrices carry the family index. With the family $\mathbb Z_3$ exact, T-328(d) makes $V_{\mathrm{CKM}}$ a permutation matrix; (UP) does not change this. The Fano selection rule "only the generation on the Higgs line couples at tree level" ([Yukawa hierarchy §2](/docs/physics/particle-physics/yukawa-hierarchy#2-фановское-правило-отбора-юкавских-связей)) belongs to the axis identification $H\sim\gamma_{EU}$, which is [H].

### 1.7 The hypothesis (UP) is holomorphy, and its exact form is refuted (T-332, continued) {#голоморфность-вп}

:::tip[Status: Theorem 1.7 (h), (i), (k) are \[T\] as mathematics and \[C at (Cl)\] in UHM; (j) is numerical; the exact hypothesis (UP) is refuted \[✗\]; its leading-order form, with a breaking of about 3%, stays \[H\]]
The hypothesis (UP) of §1.6(f) says that the tree-level Yukawa coupling is the projection onto the clock-aligned complex structure $i=L_{e_O}$. This section tries to derive it from UHM, finds what it is equivalent to, and shows that in its exact form it cannot hold. Registry row T-332, items (h)–(k); checks in `website/scripts/check_core_numbers.py`.
:::

**Theorem 1.7 (T-332(h)–(k)).**

**(h) (UP) is holomorphy in one complex doublet [T].** Hypercharge acts on the colour-free plane $P$ as $\tfrac12 j$ with $j^2=-1$, and on maps $V_L\to V_R$
$$\tau_R\,\gamma(h)=\omega\,\gamma(jh)\qquad(h\in P).$$
Hence $\tfrac12(1\pm\tau_R)\gamma(h)=\gamma(\pi_\pm h)$, where $\pi_\pm=\tfrac12(1\pm\omega j)$ act on $P_{\mathbb C}=P\otimes\mathbb C_\omega$. Each $\pi_\pm$ has real rank 4, one doublet. So (UP) says that the coupling depends on the Higgs field only through $\pi_+h$, the doublet of hypercharge $-\tfrac12$ (the $\tilde H$ of the Standard Model), and does so $\omega$-linearly. The coupling is holomorphic in one complex doublet. This agrees with T-296, since $P_+$ is one doublet, not two. It is the holomorphic alternative to the real reading of §1.6(c). In Standard-Model language (UP) is $y_u\,Q\tilde Hu^c$ with no $QHd^c$ and no $LHe^c$.

**(i) The exact form keeps the charged leptons massless [T].** Take one generation, the six fields $Q,L,u^c,d^c,\nu^c,e^c$, and the doublet. Which phase rotations that commute with $\mathfrak g_{\mathrm{SM}}$ keep the coupling $(\alpha+\beta\tau_R)\gamma(h)$? For $\lvert\beta\rvert\neq\lvert\alpha\rvert$, with or without a $(B-L)$ dressing, there are three: hypercharge, $B$ and $L$. Each has zero colour anomaly. For $\beta=\alpha$ — exact (UP) — there are five. The two new ones are the phase of $d^c$, with colour anomaly $\tfrac12$ per generation, and the phase of $e^c$, with neither a colour nor an $\mathrm{SU}(2)_L$ anomaly. The phase of $e^c$ is then an exact symmetry of every $\mathfrak g_{\mathrm{SM}}$ gauge theory whose only chirality-flipping coupling is the (UP) Yukawa. Its only anomaly is with hypercharge, and an abelian anomaly has no instantons. It forbids masses for $e$, $\mu$ and $\tau$ at every order and non-perturbatively. The phase of $d^c$ forbids $m_d$, $m_s$ and $m_b$ at every order of perturbation theory; only QCD instantons break it. **So exact (UP) is refuted by $m_\tau=1.777$ GeV [✗].** The pattern "tree-level $y_b=y_\tau=0$, radiative $b$ and $\tau$ masses" is impossible in the Clifford content: loops of the gauge bosons, of the Higgs and of the up-type coupling keep both phases.

**(j) The size of the breaking [numbers].** Write $\varepsilon:=1-\beta/\alpha$. Then $y_b/y_t=\varepsilon/(2-\varepsilon)$ at the scale where the coupling is set. One-loop Standard-Model running with the inputs of §1.6(f) gives $\varepsilon=0.0357$ at $M_Z$, $0.0292$ at $10^{14}$ GeV and $0.0288$ at $2\times10^{16}$ GeV. A breaking without $(B-L)$ dressing gives $y_b=y_\tau$ where it is set. The ratio $y_b/y_\tau$ falls from $1.73$ at $M_Z$ to $0.655$ at $2\times10^{16}$ GeV and passes $1$ at about $6.3\times10^{6}$ GeV. So $b$–$\tau$ equality holds only near $6\times10^{6}$ GeV, ten orders below unification. Set at $2\times10^{16}$ GeV, the down-type breaking needs a dressing $p+q(B-L)$ with $q/p=-0.349$. In $\mathrm{SO}(10)$ language this is a $\overline{\mathbf{126}}$ admixture of $-0.116$ relative to the $\mathbf{10}$. These are one-loop numbers. Nothing found in UHM fixes either $\varepsilon$ or $q/p$.

**(k) The routes to a derivation, and where each ends [T for the statements].**
(1) *The Higgs direction in the real plane $\{iL_{e_O},\gamma_{10}\}$.* A real vacuum gives equal moduli (§1.6(c)), not a projection.
(2) *The Higgs as the isotropic vector $\gamma_{10}+\omega\,iL_{e_O}$.* By (h) this is (UP) exactly, and (i) refutes it.
(3) *The Gap vacuum, $\mathrm{Im}\,\Gamma_v\propto L_{e_O}$ (T-331, T-64).* On 94 of the 99 points of the Gap phase scanned in §1.6(e), the vacuum lies on the rank-4 branch: $c=0$, so one component of the quark doublet is not populated at all. Read as population weights, this is an exact quark projection. Which component is empty depends on the sign of $\mathrm{Im}\,\Gamma_v$. The two signs are degenerate vacua exchanged by PT, since the potential is PT-even (T-331). On the other 5 points the smaller weight is up to $0.75$ of the larger. The same reading gives equal $\nu$ and $e$ weights and a lepton-to-quark ratio of at least $0.46$ (§1.6(e)), so it fails for leptons. In its exact form (i) refutes it as well.
(4) *The self-model or the regenerator coupling only to the clock-aligned part.* The clock-aligned part of $\mathcal S_{\mathbb C}$ is $\tau=+1$ (§1.6(a)), so this is the exact projection again, refuted by (i).
(5) *The Page–Wootters clock as the source of the Hilbert unit.* It fixes the sign of $i$ through $H_O\ge0$, and with it which fields are up-type. It does not supply a coupling: by §1.6(d) the clock phase moves only phases.
No route gives (UP) as a theorem, and every route that gives it exactly is refuted by (i). What survives is the leading-order statement that the up-type coupling dominates, by $2/\varepsilon\approx68$ at unification. That restates the data and stays [H].

**Proof.** (h) $j$ is $2\,\mathrm{ad}(Y)$ on the plane, expanded in the Clifford vectors. The identity is checked on the four basis vectors of $P$, and $\pi_\pm$ are idempotents of trace 4 on $P_{\mathbb C}\cong\mathbb R^8$. (i) The phases are $\omega P_f$, with $P_f$ the projector onto the field $f$. The conditions $[X,M(h)]=q_H\,M(jh)$ form a linear system in seven unknowns, the six field charges and $q_H$. Its null space is computed for $\beta/\alpha=0.971$ and $0.5$, for a coupling with $(B-L)$ dressing, and for $\beta=\pm\alpha$. The colour anomaly of $X$ is $\sum q\,T(R)$ over the coloured fields, read from the charge operator $-\omega X$. A symmetry without anomaly under a non-abelian gauge group is not broken by instantons. The hypercharge anomaly $\propto F\tilde F$ integrates to zero on finite-action configurations. (j) The running is that of §1.6(f). The point $y_b=y_\tau$ is found by root finding. The dressing solves $(p+q/3)/(p-q)=y_b/y_\tau$ with $B-L=1/3$ and $-1$. (k)(3) uses the closed-form sector minimum of T-64(e). $\blacksquare$

Witnesses: `test_up_projection_is_holomorphy_in_one_complex_doublet`, `test_an_exact_up_projection_leaves_the_tau_massless_to_all_orders`, `test_b_tau_and_the_size_of_the_up_projector_breaking`.

**What this changes.** In T-332(f) the exact (UP) is refuted [✗], and the leading-order statement stays [H] as a description of the data. The loop mechanisms for $m_b$ on the [Fano selection-rule page](/docs/physics/gauge-symmetry/fano-selection-rules) (§12.4) and in [Yukawa hierarchy §7.3](/docs/physics/particle-physics/yukawa-hierarchy#теорема-mb-mt) start from $y_b^{(\text{tree})}=0$ and generate $y_b$ through the retracted cubic $V_3$. The corrected $G_2$-invariant potential has no such vertex, and by (i) the Clifford content cannot generate $y_b$ from $y_b^{(\text{tree})}=0$. The neutrino relation $y_\nu^D=y_t$ uses only the leading order and is unchanged. With all down-type quarks exactly massless, $\bar\theta$ would be unphysical — the massless-quark solution of strong CP. The data exclude that as well; see [confinement §3.1b](/docs/physics/gauge-symmetry/confinement#пк-и-нб).


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
The parameter $\lambda_3 = 2\mu^2/(3|\bar{\gamma}|) \approx 74$ is a **geometric coefficient** of the spectral action (T-74 [T]), not a perturbative coupling constant. Physical observables are defined non-perturbatively via the self-consistent vacuum $\theta^*$ (T-79 [C at (SV)]). UV-finiteness (T-66: field-space [T], order-by-order [C]) ensures structural correctness. Loop estimates are approximations to $\theta^*$, giving the right order of magnitude (error $\lesssim \times 5$). For details — see [Yukawa Hierarchy](/docs/physics/particle-physics/yukawa-hierarchy#предупреждение-λ3).

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

$$\delta M_H^2 \approx \frac{3 \cdot (73.8)^2 \cdot (0.047)^2}{4 \cdot 16.6} \approx 0.54 \; (\text{in Gap units})$$

This correction is small compared to the main term, but is **nonzero** and gives rise to a falsifiable deviation from SM (see [section 6](#6-фальсифицируемые-предсказания)). (The stated inputs give $0.54$; $\approx 5.5$ would require $\bar A\approx0.15$, the confinement-sector coherence, rather than the average $0.047$.)

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

### Theorem T-70 (Canonical definition of $f_0$) [C at (SV)] {#теорема-f0-канонический}

*Corrected 2026-09-25 from [T]: Steps 2, 3 and 5 take the unique vacuum and its five Hessian eigenvalues from the sector form of T-64; the corrected T-64 has a vacuum with none of these sector values (see [Gap thermodynamics §14](/docs/core/dynamics/gap-thermodynamics#теорема-глобальная-минимизация)); the formula holds conditional on the sector-vacuum hypothesis (SV).*

:::tip [C at (SV)] Theorem
In UHM the moment $f_0$ of the spectral action is **uniquely determined** through the vacuum effective action of the Gap theory on $(S^1)^{21}$:

$$f_0 \Lambda^4 = \frac{1}{7}\left[V_{\mathrm{Gap}}^{\min} + \frac{1}{2}\zeta'_{H_{\mathrm{Gap}}}(0)\right]$$

where $V_{\mathrm{Gap}}^{\min}$ is the potential value at the vacuum minimum ([T-64](/docs/core/dynamics/gap-thermodynamics#теорема-глобальная-минимизация) [T] (corrected to the $G_2$-invariant potential; its vacuum has no sector values — hypothesis (SV))), and $\zeta'_{H_{\mathrm{Gap}}}(0)$ is the log-determinant of the Hessian at the vacuum.
:::

**Proof.**

**Step 1 (Field-space finiteness → finite functional integral).** The Gap partition function on the compact target $(S^1)^{21}$ is finite — field-space finiteness **[T]**; full order-by-order UV-finiteness is structural [C] ([T-66](/docs/physics/gravity/quantum-gravity#теорема-уф-конечность)). Therefore the functional integral $Z = \int [D\theta] \exp(-S_{\mathrm{Gap}}[\theta])$ is **finite and well-defined** without regularization ambiguity. The quantum effective action $\Gamma_{\mathrm{eff}} = -\ln Z$ is a finite, concrete quantity.

**Step 2 (Unique vacuum → loop expansion).** From [T-61, T-64](/docs/core/dynamics/gap-thermodynamics#теорема-единственный-вакуум) [T] (corrected to the $G_2$-invariant potential; its vacuum has no sector values — hypothesis (SV)): the potential $V_{\mathrm{Gap}}$ has a unique global minimum with positive definite Hessian $H_{\mathrm{Gap}}$. Expansion:

$$\Gamma_{\mathrm{eff}} = V_{\mathrm{Gap}}^{\min} + \frac{1}{2}\ln\det(H_{\mathrm{Gap}}) + O(\text{two-loop})$$

**Step 3 (Determinant regularization).** Zeta-regularized determinant: $\ln\det(H_{\mathrm{Gap}}) = -\zeta'_{H_{\mathrm{Gap}}}(0)$. From T-64 [T] (corrected to the $G_2$-invariant potential; its vacuum has no sector values — hypothesis (SV)): all eigenvalues $\lambda_i > 0$ (5 positive on the orbit space), so $\zeta'_{H_{\mathrm{Gap}}}(0) = -\sum_{i=1}^{5}\ln\lambda_i$.

**Step 4 (Identification with $f_0$).** Coefficient $a_0$ of the spectral action: $f_0 \Lambda^4 \cdot 7$ = vacuum energy density of the internal space = $\Gamma_{\mathrm{eff}}$. Therefore:

$$f_0 = \frac{\Gamma_{\mathrm{eff}}}{7\Lambda^4} = \frac{1}{7\Lambda^4}\left[V_{\mathrm{Gap}}^{\min} + \frac{1}{2}\zeta'_{H_{\mathrm{Gap}}}(0)\right]$$

**Step 5 (Uniqueness).** All quantities on the right-hand side are uniquely determined: $V_{\mathrm{Gap}}^{\min}$ from T-64 [T] (corrected to the $G_2$-invariant potential; its vacuum has no sector values — hypothesis (SV)), $\zeta'_{H_{\mathrm{Gap}}}(0)$ from a finite sum over 5 eigenvalues, $\Lambda = \omega_0$. $f_0$ is **not a free parameter**, but a definite function of the vacuum quantities. $\blacksquare$

:::info Numerical estimate [C]
From T-64 [T] (corrected to the $G_2$-invariant potential; its vacuum has no sector values — hypothesis (SV)), Hessian eigenvalues: $\lambda_1 = 18\mu^2$ (confinement), $\lambda_{2,3} = 6\mu^2(1 + O(\varepsilon^2))$ (spatial), $\lambda_{4,5} = 12\mu^2(1 + O(\varepsilon))$ (O-modes). With $\mu^2 \approx \omega_0^2/7$: $f_0 \approx 2.2/\omega_0^4$. Numerical value [C] — depends on exact $\varepsilon_i$.
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

$$S = f_0 \Lambda^4 a_0 + f_2 \Lambda^2 a_2 + f_4 a_4 + O(\Lambda^{-2})$$

The coefficient $a_4$ contains the term $\mathrm{Tr}(D_{\text{int}}^4)$, generating the quartic Higgs potential.

**Step 3 (Computation).** From sectoral values (hypothesis (SV) [H]; T-61 restated):

$$\mathrm{Tr}(D_{\text{int}}^2) \approx 6\omega_0^2\varepsilon_0^2, \qquad \mathrm{Tr}(D_{\text{int}}^4) \approx 6\omega_0^4\varepsilon_0^4 + \text{sectoral corrections}$$

**Step 4 (RG evolution).** The bare $\lambda_4(\Lambda)$ is too large. RG running from $\Lambda$ to $v_{\text{EW}}$:

$$\lambda_4(v) = \lambda_4(\Lambda) + \frac{1}{16\pi^2}\left(24\lambda_4^2 - 6y_t^4 + \ldots\right) \ln\frac{v}{\Lambda}$$

At $y_t \approx 1$ (quasi-IR fixed point [T]): RG brings $\lambda_4$ to the observed $\approx 0.13$ from $\lambda_4(\Lambda) \approx 0.20$ [C] — standard Shaposhnikov–Wetterich result (2010). $\blacksquare$

**Status:** [C] — $\lambda_4$ determined through spectrum $D_{\text{int}}$ + RG. Parameter $f_0$ is **canonically determined [C at (SV)]** ([T-70](#теорема-f0-канонический)). The conditionality [C] remains only for the numerical value — depends on exact sectoral $\varepsilon_i$.

:::info Cross-references
- **Spectral triple:** [Theorem (UHM Spectral Triple)](/docs/core/foundations/spacetime#теорема-спектральная-тройка) — finite triple $(A_{\text{int}}, H_{\text{int}}, D_{\text{int}})$; its KO-dimension-6 claim is retracted: no real structure of KO-dimension 6 exists on $\mathbb{C}^7$ — its $\chi = \pm 1$ eigenspaces would need equal dimension, and 7 is odd ([spacetime, Step 6](/docs/core/foundations/spacetime#теорема-спектральная-тройка))
- **Spectral action:** [Quantum Gravity](/docs/physics/gravity/quantum-gravity#теорема-полное-спектральное-действие) — $S = \mathrm{Tr}(f(D_A/\Lambda))$, Einstein equations [T]
- **Unique vacuum:** [T-61](/docs/core/dynamics/gap-thermodynamics#теорема-единственный-вакуум) — sectoral values $\varepsilon$
:::

---

### Theorem 4.1 (Higgs mass) [C] {#thm-4-1}

:::warning [C] Conditional
The formula for the Higgs mass contains $\lambda_4$, determined from the spectral action ([theorem on Higgs quartic](#теорема-хиггсовская-квартика) [C]), and the octonionic correction from $V_3$. Parameter $f_0$ is canonically determined [C at (SV)] ([T-70](#теорема-f0-канонический)); conditionality [C] — only numerical value through $\varepsilon_i$.
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

$$\delta M_H^2 = \frac{3\lambda_3^2 \bar{A}^2}{4\mu^2} \approx \frac{3 \cdot (73.8)^2 \cdot (0.047)^2}{4 \cdot 16.6} \approx 0.54$$

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

:::tip [C at (SV)] Theorem
Dynamical stability of the chiral vacuum follows conditional on the sector-vacuum hypothesis (SV): Step 2 uses the unique sector vacuum with positive-definite Hessian (hypothesis (SV); the corrected T-64 gives a different vacuum) and Step 3 the barrier of T-69, both conditional on (SV) since 2026-09-25 (earlier stated as proved from [T]-results).
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

**Step 2.** The vacuum of $V_{\mathrm{Gap}}$ is unique with positive definite Hessian — hypothesis (SV) [H] (T-64, corrected to the $G_2$-invariant potential, gives a vacuum unique up to $G_2$ — [T] for every $\kappa > 0$ off the transition lines — but not the sector one). No flat directions → the chiral minimum is non-degenerate.

**Step 3.** Topological barrier [C at (SV)] ([T-69](/docs/core/dynamics/composite-systems#теорема-тополог-защита)): $\Delta V \geq 6\mu^2 > 0$ prevents tunneling between chiral vacua.

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

### 6.0 Prohibition of a second Higgs doublet [H] {#запрет-второго-дублета}

*Corrected 2026-09-25 from [T] to [H]: step (i) takes "$\langle\gamma_{ij}\rangle \neq 0$ only for the $\kappa_0$ pair" from T-64, which never stated it and is now a hypothesis, and the whole argument presupposes the identification $H \sim \gamma_{EU}$ of Theorem 1.0, now a hypothesis with a colour-breaking obstruction. The exclusion of 2HDM spectra is a prediction of that hypothesis, not a theorem.*

*New basis (T-332, [§1.6](#юкавы-t340)).* In the Clifford frame the colour-free plane of $\mathrm{Spin}(10)$ is exactly one real doublet, so a real Higgs field gives one doublet without reference to $\gamma_{EU}$. The price is the up–down split. With one real doublet it must come from the operator $\tau_R$ (the imaginary unit of $\mathcal H$ on $V_R$), that is from a coupling that breaks $\mathrm{SU}(2)_R$. The alternative is the complex bidoublet — two doublets with $m_t/m_b=\tan\beta$ — which this prohibition excludes. The data require the $\tau_R$-coefficient $\beta/\alpha=0.971$ (T-332(f)). T-296 stays [H]. A charged Higgs would now refute the real-plane reading together with it.

:::tip [H] Structural prohibition (T-296)
UHM forbids a second Higgs doublet. The categorical uniqueness that *selects* the pair $(E,U)$ simultaneously *excludes* every other scalar candidate.
:::

**Theorem (no-2HDM).** In UHM there is exactly one condensing scalar channel — $\gamma_{EU}$. No second Higgs doublet (and hence no 2HDM spectrum $H^\pm, A^0, H^0$ of the MSSM type) exists.

**Proof.** (i) Condensation requires the $\kappa_0$-channel: the vacuum theorem T-64 gives $\langle\gamma_{ij}\rangle \neq 0$ only for the pair singled out by $\kappa_0 = \omega_0|\gamma_{OE}||\gamma_{OU}|/\gamma_{OO}$, whose morphism content is exactly $\mathrm{Hom}(O,E)\cdot\mathrm{Hom}(O,U)$ (T-42a). (ii) The only other $\bar 3$-pairs are $(L,E)$ and $(L,U)$; neither enters $\kappa_0$ ($\mathrm{Hom}(O,L)$ is absent from it), so neither acquires a VEV. (iii) By incidence ($\lambda=1$) the pair $(L,U)$ lies on the single line $\{D,L,U\}$, already exhausted as the Color-U Yukawa channel of the 2nd generation ([selection rules](/docs/physics/gauge-symmetry/fano-selection-rules)) — it is a mass channel, not a scalar sector. $\blacksquare$

**Falsification.** Discovery of a charged Higgs $H^\pm$ or of a second CP-even/odd neutral scalar of doublet type at the LHC/HL-LHC would refute the categorical uniqueness of $(E,U)$ — i.e. strike at $\kappa_0$ itself, not at a peripheral fit. UHM stakes the entire class of 2HDM/MSSM Higgs sectors on this.


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

### 6.4 Dynamical dark energy [T at the O-channel; P for the non-O residue]

The drift of the dark-energy equation of state is now **derived** at the state level: $1 + w_{\text{eff}} = -\tfrac{2}{3}\,d\ln\mathcal{G}_O/d\ln a$ with a positive floor and a three-branch shape classification — [the Λ-drift law, T-254/T-255](/docs/physics/gravity/cosmological-constant#теорема-лямбда-дрейф). The Higgs-sector channels considered here ($\bar{3}$-to-$\bar{3}$ — non-O) contribute to that drift only through the sector-suppressed correction $O(\mathcal{G}_{\text{non-O}}/\mathcal{G}_O) \sim 10^{-3}$ ([sector Gap bound](/docs/physics/cosmology-phys/berry-phase#теорема-секторная-gap-граница) [T]) — a subdominant channel. The earlier ansatz is kept for the record:

$$w(z = 0) = -1 + \delta w, \quad \delta w = \frac{\kappa \cdot \langle|\gamma|^2\rangle}{V_\text{Gap}} \sim \frac{\kappa \cdot \epsilon^2}{\mu^2 \text{Gap}^2}$$

What remains open **[P]** is the RG-scale ↔ $H(t)$ bridge for the *non-O* channels; the O-channel drift needs no such bridge — it passes through the M3 identification $a = 1/\mathrm{Gap}_s$ directly. The old numerical ansatz $w_a \sim -10^{-2}$ is superseded by the T-255 shape constraints (the DESI quadrant requires the oscillatory branch with a genuine $-1$-crossing).

---

### 6.5 Chirality tunneling rate [C at (SV)] {#скорость-хирального-туннелирования}

:::tip Theorem T-185b [C at (SV)]: Chirality stability prediction
The chiral vacuum is stable against tunneling with a lifetime vastly exceeding the age of the universe:

$$\tau_{\text{chiral}} \sim \frac{1}{\mu} \exp\!\left(\frac{B}{\hbar}\right) \gg \tau_{\text{universe}} \approx 4.4 \times 10^{17}\;\text{s}$$

where $B \geq \pi\sqrt{12}\,\mu \approx 10.88\,\mu$ is the WKB bounce action through the barrier $\Delta V \geq 6\mu^2$ (T-69 [C at (SV)]).
:::

**Derivation.** The WKB tunneling rate between the chiral vacua $\theta = 0$ and $\theta = \pi$:

$$\Gamma_{\text{tunnel}} = \mu \cdot \exp\!\left(-\frac{B}{\hbar}\right), \quad B = \int_0^{\pi} \sqrt{2\Delta V(\theta)}\,d\theta \geq \pi\sqrt{2 \cdot 6\mu^2} = \pi\sqrt{12}\,\mu$$

In physical units with $\mu \sim M_{\text{Planck}}$: the exponent $e^{10.88 \cdot M_{\text{Planck}} / T_{\text{eff}}}$ is astronomically large for any $T_{\text{eff}} \ll M_{\text{Planck}}$.

**Falsifiable prediction.** Observation of spontaneous chirality flipping (a right-handed neutrino appearing from a left-handed one without a mass insertion) at any sub-Planckian energy would falsify the topological protection theorem T-69 [C at (SV)] and the cubic potential $V_3$ (T-99 [T]).

**Status.** [C at (SV)] — follows from T-69 [C at (SV)] (topological barrier), the hypothesis (SV) [H] (unique vacuum with positive Hessian; the corrected T-64 does not give its values), and step 2 of T-99 ($V_3$ is the unique $PT$-odd term — true of the retracted cubic only; the corrected potential is PT-even, T-331); corrected from [T] on 2026-09-25.

---

## 7. Can UHM predict the Higgs mass? {#7-может-ли-угм-предсказать-массу-хиггса}

### 7.1 Problem statement

Experimental value: $M_H^{\text{exp}} = 125.20 \pm 0.11$ GeV (PDG 2024). In the Standard Model $M_H$ is a free parameter. In Chamseddine–Connes noncommutative geometry (NCG) the Higgs mass is **computed** from the spectral triple. Question: can UHM do the same?

### 7.2 Derivation chain for $M_H$ in UHM {#цепочка-mh}

The full chain from axioms to $M_H$ consists of five links:

| Link | Statement | Status | Dependency |
|---|---|---|---|
| (1) Spectral triple | $(A_{\text{int}}, H_{\text{int}}, D_{\text{int}})$ exists **[T]** (T-53); "KO-dim = 6" is retracted — no real structure of KO-dimension 6 exists on $\mathbb{C}^7$ — its $\chi = \pm 1$ eigenspaces would need equal dimension, and 7 is odd ([spacetime, Step 6](/docs/core/foundations/spacetime#теорема-спектральная-тройка)) | **[T]** (T-53), without the real structure | Axioms |
| (2) Spectral action | $S = \mathrm{Tr}(f(D_A/\Lambda))$ expands in Seeley–DeWitt series | **[T]** (T-65) | (1) |
| (3) $f_0$ canonically determined | $f_0 = \Gamma_{\text{eff}} / (7\Lambda^4)$ through Gap theory vacuum | **[C at (SV)]** (T-70) | (2) + sector vacuum (SV) [H] |
| (4) $\lambda_4$ from $D_{\text{int}}$ + RG | $\lambda_4 = \frac{\pi^2}{2f_0\Lambda^4} \cdot \frac{\mathrm{Tr}(D_{\text{int}}^4)}{[\mathrm{Tr}(D_{\text{int}}^2)]^2}$, RG: $\Lambda \to v_{\text{EW}}$ | **[C]** | (3) + numerical $\varepsilon_i$ |
| (5) $M_H$ from potential | $M_H^2 = 2\lambda_4 v^2 + \delta M_H^2(\lambda_3, \bar{A}, \mu)$ | **[C]** | (4) + octonionic correction |

**Verdict: [C]** — conditional on numerical values of sectoral parameters $\varepsilon_i$ determining the spectrum $D_{\text{int}}$.

### 7.3 Why $g_4^* = 4\pi^2/63$ is NOT the Higgs quartic {#gap-vs-higgs-quartic}

:::danger Common error
The Wilson–Fisher fixed point of the Gap theory $g_4^* = 4\pi^2/63 \approx 0.627$ is **not** the Higgs quartic $\lambda_H$ of the Standard Model. The naive identification gives $M_H = \sqrt{2 g_4^*} \cdot v \approx 275$ GeV — an **incorrect** result (the printed "$0.063$"/"$87$ GeV" in earlier drafts mis-evaluated $4\pi^2/63$ by a factor of 10; the correct value $0.627$ still fails to reproduce $M_H=125$ GeV, so the conclusion "$g_4^*\neq\lambda_H$" stands).
:::

Distinction:

| | Gap quartic $g_4^*$ | Higgs quartic $\lambda_H$ |
|---|---|---|
| Theory | (0+1)D Gap on $(S^1)^{21}$ | 4D QFT on $M^4$ |
| Number of fields | 21 coherences | 1 doublet (4 real fields) |
| Factor in $\beta$ | 63 (from combinatorics $\binom{21}{2} \cdot 3$) | $\sim 24$ (loop with $W$, $Z$, $t$) |
| IR value | $4\pi^2/63 \approx 0.627$ | $\approx 0.13$ (from $M_H = 125$ GeV) |
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
- **Naive $g_4^* \to M_H$**: incorrect ($g_4^* \neq \lambda_H$), gives $\sim 275$ GeV.
- **Status**: **[C]** — conditional on computation of $\varepsilon_i$.
- **Comparison with NCG**: UHM reproduces the CCM structure, but adds the octonionic $V_3$-correction, analogous to the $\sigma$-field of Chamseddine–Connes–van Suijlekom.

---

## Connection to other sections

- **Uniqueness of the Higgs line:** Foundation of the Fano selection rule → [Yukawa Mass Hierarchy](./yukawa-hierarchy.md)
- **Three generations:** Generation line $\{A,S,L\}$ orthogonal to Higgs line → [Three Fermion Generations](./fermion-generations.md)
- **CKM matrix:** Mismatch of $Y^u$ and $Y^d$ via conjugate Higgs → [CKM Matrix](./ckm-matrix.md)
- **Spectral triple:** Finite $(A_{\text{int}}, H_{\text{int}}, D_{\text{int}})$ → [Spacetime](/docs/core/foundations/spacetime#теорема-спектральная-тройка) [T]; the former "with KO-dimension 6" is retracted — no real structure of KO-dimension 6 exists on $\mathbb{C}^7$ — its $\chi = \pm 1$ eigenspaces would need equal dimension, and 7 is odd ([spacetime, Step 6](/docs/core/foundations/spacetime#теорема-спектральная-тройка))
- **Spectral action:** $S = \mathrm{Tr}(f(D/\Lambda))$, determines $\lambda_4$ → [Quantum Gravity](/docs/physics/gravity/quantum-gravity)
- **Unique vacuum:** Sectoral values $\varepsilon$ — hypothesis (SV) [H] (T-61 restated) → [Gap Thermodynamics](/docs/core/dynamics/gap-thermodynamics#теорема-единственный-вакуум)


---

**Related documents:**
- [Standard Model from G₂](/docs/physics/gauge-symmetry/standard-model)
- [Fano Selection Rules](/docs/physics/gauge-symmetry/fano-selection-rules)
- [Yukawa Hierarchy](/docs/physics/particle-physics/yukawa-hierarchy)
- [Supersymmetry from G₂](/docs/physics/particle-physics/susy)
