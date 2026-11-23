---
sidebar_position: 4
title: "Obstructions to a 7D NCG Bimodule and Requirements of the Spin(10) Extension"
description: "Proven algebraic obstructions to a 7D KO-dim-6 bimodule (withdrawn T-178, T-175a, T-179), external spinor requirements of T-326/T-327/T-329 against T-350, and exact scope of T-180, T-181, and T-123."
---

# Obstructions to a 7D NCG Bimodule and Requirements of the Spin(10) Extension

This page records the algebraic obstructions showing that the 7-dimensional internal carrier $\mathbb{C}^7$ of UHM cannot by itself supply Connes' Standard Model bimodule, states the exact external inputs required by the $\mathrm{Spin}(9)/\mathrm{Spin}(10)$ spinor extension (`T-326`, `T-327`, `T-329`) alongside the non-inducibility theorem (`T-350`), and fixes the exact scope of `T-180`, `T-181`, and `T-123`.

---

## 1. The Algebra–Representation Gap {#единый-корень}

Working on the coherence state space $\mathcal{D}(\mathbb{C}^7)$ and the internal algebra $A_{\mathrm{int}} = \mathbb{C} \oplus M_3(\mathbb{C}) \oplus M_3(\mathbb{C})$ (induced by the $\mathrm{SU}(3) \subset G_2$ splitting $\mathbb{C}^7 = \mathbf{1} \oplus \mathbf{3} \oplus \bar{\mathbf{3}}$) does not determine a chiral Standard Model fermion module, a dynamical mass spectrum, the characterizing holon requirements, or a unique empirical encoder. Earlier claims that a 7D noncommutative-geometry bimodule resolved all four issues have been withdrawn; the exact separation between retracted claims and surviving results is summarized below.

| Topic | Withdrawn claim | Proven status |
|---|---|---|
| SM bimodule on $\mathbb{C}^7$ | `T-178 [✗]`, `T-175a [✗]` | Odd dimension 7 forbids KO-dim 6; centres of $A_{\mathrm{int}}$ and $A_F$ have real dimensions 6 vs. 5. |
| Hypercharges from anomalies alone | `T-179 [✗]` | Homogeneous anomaly equations underdetermine hypercharges (e.g. $Y + c(B-L)$ with $\nu_R$). |
| Spinor extension | Imported $H_F$ | `T-326`, `T-327`, `T-329` `[T / C]` require external `(Cl₀)` + complexification `(W₀)` + manual $\nu^c$ breaking; `T-350 [T]` proves no spinor module is induced from $\mathcal{D}(\mathbb{C}^7)$ or $(\mathbb{C}^7)^{\otimes M}$. |
| Spectral mass ratios | Diagonal `0/0` formula & "PG(2,2) distances" | `T-180 [T]`: tree-level mass ratios are singular values of **specified** Yukawa matrices in a supplied $D_{\mathrm{int}}$ (`T-184 [T]`). |
| Holon requirements `(AP+PH+QG+V)` | `T-181 [✗]` | Independent modeling requirements, not consequences of topos terminality. |
| Empirical encoder $G$ | `T-123 [✗]` | Cholesky parameterization ensures PSD when nonzero; identifiability depends on the observation law. |

---

## 2. Algebraic Obstructions and the Spin(10) Spinor Extension {#бимодульная-конструкция}

### 2.1 Proven algebraic obstructions on $\mathbb{C}^7$

**Theorem T-178 (7D NCG bimodule realization of SM) — retracted `[✗]`.**
The finite carrier $H_{\mathrm{int}} = \mathbb{C}^7$ with algebra $A_{\mathrm{int}} = \mathbb{C}_O \oplus M_3(\mathbb{C})_{\mathbf{3}} \oplus M_3(\mathbb{C})_{\bar{\mathbf{3}}}$ cannot realize one generation of Standard Model fermions as a KO-dimension-6 spectral triple:

1. **Odd-dimension KO-6 obstruction:** KO-dimension 6 requires an antiunitary real structure $J$ and a $\mathbb{Z}_2$-grading $\chi$ ($\chi^2 = I$, $\chi^\dagger = \chi$) obeying $J\chi = -\chi J$. Because $J$ is antiunitary and anticommutes with $\chi$, it maps the $+1$ eigenspace of $\chi$ bijectively onto the $-1$ eigenspace, forcing $\dim \ker(\chi - I) = \dim \ker(\chi + I)$ and therefore forcing $\dim_{\mathbb{C}} H_{\mathrm{int}}$ to be **even**. No grading on $\mathbb{C}^7$ admits a KO-dimension-6 real structure ([Spacetime](/docs/core/foundations/spacetime#теорема-спектральная-тройка)).
2. **State-count obstruction:** One Standard Model generation with $\nu_R$ requires 16 Weyl fermions and 16 conjugates ($\dim_{\mathbb{C}} H_F = 32$), which does not embed into $\mathbb{C}^7$.
3. **No Morita equivalence (`T-175a [✗]`):** The centre of the real $*$-algebra $A_{\mathrm{int}} = \mathbb{C} \oplus M_3(\mathbb{C}) \oplus M_3(\mathbb{C})$ is $\mathbb{C}^3$ (real dimension **6**), whereas the centre of Connes' Standard Model algebra $A_F = \mathbb{C} \oplus \mathbb{H} \oplus M_3(\mathbb{C})$ is $\mathbb{C} \oplus \mathbb{R} \oplus \mathbb{C}$ (real dimension **5**). Because Morita equivalence preserves the centre, $A_{\mathrm{int}}$ and $A_F$ are not Morita equivalent ([Spacetime](/docs/core/foundations/spacetime#алгебра-морита)).

What remains mathematically valid is solely the standard Chamseddine–Connes–Marcolli (2007) / Barrett (2007) bimodule decomposition of Connes' externally imported $H_F$ over $A_F$, where left $\mathbb{H}$-action and right $M_3(\mathbb{C})^\circ$-action intersect on $\mathbf{2}_L \otimes \mathbf{3}$. That construction imports $A_F$ and $H_F$ rather than deriving them from $\mathbb{C}^7$.

**Theorem T-179 (Hypercharge fixation from anomalies alone) — retracted `[✗]`.**
The anomaly cancellation equations alone do not uniquely fix the Standard Model hypercharges. Two equations ($\mathrm{Tr}\,Y = 0$, $\mathrm{Tr}\,Y^3 = 0$) cannot determine five (or six, with $\nu_R$) hypercharges. Even all four linear/cubic gauge and gravitational anomaly conditions ($\mathrm{Tr}\,Y = 0$, $\mathrm{Tr}\,Y^3 = 0$, $\mathrm{Tr}_{SU(3)} Y = 0$, $\mathrm{Tr}_{SU(2)} Y = 0$) are homogeneous and admit alternative solutions: without $\nu_R$, the assignment $y_Q = y_L = y_e = 0$, $y_u = -y_d$ satisfies all four; with $\nu_R$, every one-parameter shift $Y + c(B-L)$ satisfies all four (Boyle & Farnsworth, *New J. Phys.* **22**, 073023 (2020)). Selecting the Standard Model hypercharges additionally requires Yukawa couplings to a single Higgs doublet and, when $\nu_R$ is present, a Majorana mass term for $\nu_R$ (Babu & Mohapatra, *Phys. Rev. Lett.* **63**, 938 (1989)).

### 2.2 Requirements of the $\mathrm{Spin}(9)/\mathrm{Spin}(10)$ extension (`T-326`, `T-327`, `T-329`) and non-inducibility (`T-350`)

A separate algebraic route constructs a Standard Model generation without importing Connes' $H_F$, but only after introducing explicit external spinor and symmetry-breaking premises:

- **External spinor module `(Cl₀)` and $\mathrm{Spin}(9)$ (`T-326`, `T-327` `[T]`, `[C under (Cl₀)]`):** Given the independent physical premise `(Cl₀)` — supplying a real 16-dimensional $\mathrm{Spin}(9)$ spinor module $\mathcal{S} \cong \mathbb{O}^2$ on which octonionic Clifford generators act (`T-347 [T]/[H]`) — selecting Krasnov's complex structure yields a centralizer isomorphic to $(\mathrm{SU}(3)\times\mathrm{SU}(2)\times\mathrm{U}(1))/\mathbb{Z}_6$ (`T-326`) and the left-handed doublet charges $(3,2)_{1/6}\oplus(1,2)_{-1/2}$ (`T-327`). Physical chirality requires an external spacetime and chiral matter action ([Standard Model §2.5](/docs/physics/gauge-symmetry/standard-model#sm-из-клиффорда)).
- **Complexification `(W₀)` and manual $\nu^c$ breaking (`T-329` `[T]`, `[C under (Cl₀) + (W₀) + \nu^c breaking]`):** Right-handed singlets do not fit inside the real $\mathrm{Spin}(9)$ spinor $\mathcal{S}$. Obtaining one complete 16-state anomaly-free generation requires **complexifying** the module to $\mathcal{S}\otimes_{\mathbb{R}}\mathbb{C}$ (premise `(W₀)`, supplying the complex Weyl spinor factor and a tenth Clifford generator lifting $\mathrm{Spin}(9)$ to $\mathrm{Spin}(10)$) together with a **manual breaking** in the sterile-neutrino $\nu^c$ direction to select the Standard Model subgroup and hypercharges. Once that representation is supplied, its decomposition into the 16-plet and vanishing of the gauge anomaly traces are verified directly (`T-329`, [Standard Model §2.6](/docs/physics/gauge-symmetry/standard-model#поколение-t329)).

**Theorem T-350 (Non-inducibility of spinors from $\mathcal{D}(\mathbb{C}^7)$) `[T]`.**
Although a Clifford/spinor module can be constructed algebraically from a supplied seven-axis frame and octonionic three-form, **no spinor module carrying the required electroweak doublets can be induced from transformations of $\Gamma \in \mathcal{D}(\mathbb{C}^7)$ or from any tensor power $(\mathbb{C}^7)^{\otimes M}$**:

1. On a single site $\mathbb{C}^7 = \mathbf{1} \oplus \mathbf{3} \oplus \bar{\mathbf{3}}$, the three $\mathrm{SU}(3)$ summands are pairwise inequivalent and multiplicity-free; by Schur's lemma the commutant of $\mathrm{SU}(3)$ is abelian ($\mathbb{C}^3$) and cannot host a non-abelian weak $\mathrm{SU}(2)$.
2. Every tensor power $(\mathbb{C}^7)^{\otimes M}$ transforms in representations that factor through $\mathrm{SO}(7) \supset G_2$ (trivial action of the central element $-1 \in \mathrm{Spin}(7)$), whereas genuine spinor modules of $\mathrm{Spin}(7)$, $\mathrm{Spin}(9)$, or $\mathrm{Spin}(10)$ are double-valued representations on which $-1 \in \mathrm{Spin}$ acts as $-I$.

Consequently, `(Cl₀)` and `(W₀)` cannot be derived from the 7D holon state axioms; they enter as independent physical hypotheses `[H]` ([Premises §7](/docs/reference/premises#t-350)).

---

## 3. Spectral Mass Ratios and Scope of T-180 {#непертурбативный}

**Theorem T-180 (Yukawa singular values in a supplied Dirac operator) `[T]`.**
For a supplied finite Dirac operator $D_{\mathrm{int}}$ containing specified Yukawa matrices $Y_f$ coupling left- and right-handed sectors of a supplied chiral matter module, the tree-level fermion mass ratios are determined by the **singular values** of those Yukawa matrices, subject to the required electroweak and renormalization-group scale matching.

Two earlier claims under this heading are mathematically invalid and withdrawn:

1. **Undefined `0/0` diagonal formula:** For a zero-diagonal Hermitian internal operator (such as the antisymmetric Gap operator $\hat{\mathcal{G}}$ or an off-diagonal chiral mass matrix $D_{\mathrm{int}}$), every diagonal matrix element $[D_{\mathrm{int}}]_{ii}$ vanishes identically. The previously written expression $|[D_{\mathrm{int}}]_{ii}|/|[D_{\mathrm{int}}]_{jj}|$ evaluates to $0/0$ and is replaced by the singular values of the off-diagonal Yukawa blocks.
2. **False "different distances on $\mathrm{PG}(2,2)$" claim:** Every pair of distinct points in the Fano plane $\mathrm{PG}(2,2)$ lies on a unique line, so its point-collinearity graph is the complete graph $K_7$ (distance 1 between every pair of distinct points) and $\mathrm{PGL}(3,2)$ acts flag-transitively. The incidence geometry of $\mathrm{PG}(2,2)$ therefore has no metric distinction between distinct pairs and does not by itself generate a fermion mass hierarchy.

Likewise, evaluating $S_{\mathrm{spec}}[D] = \mathrm{Tr}\,f(D^2/\Lambda^2)$ by matrix diagonalization for a *supplied* finite Hermitian matrix $D$ (`T-184 [T]`) requires no loop expansion in $\lambda_3$, but does not derive $D$, the Yukawa entries, or a unique physical vacuum potential (`T-64`, `T-74 [✗]`, `T-176`).

---

## 4. Characterizing Requirements Are Independent Premises (T-181 `[✗]`) {#вывод-apphqgv}

The former derivation `T-181` of `(AP+PH+QG+V)` from `A1–A4` is retracted **`[✗]`**. A sheaf topos is not the category of density matrices: its objects are sheaves, and its terminal object has a terminal space of global sections. The support reflector is defined in a slice, not as a numerical CPTP attractor; Stinespring dilation does not identify sheaf morphisms with channels; seven chosen matrix axes do not prove experiential content or tensor-factor reduction; and Bures separation does not select the structural-majority cut.

`AP`, `PH`, `QG`, and `V` are explicit modeling requirements and bridges in the [Axiom of Septicity](/docs/core/foundations/axiom-septicity). The state model, frame, self-model, rates, Page–Wootters clock extension, and phenomenal identification must each be supplied separately.

---

## 5. Observation Encoders and Identifiability (T-123 `[✗]`) {#g-отображение}

For a system with state $s \in \mathcal{S}$, a Cholesky parameterization produces a valid density matrix wherever the denominator is nonzero:

$$
G(s) = \pi(s) := \frac{L(s) L(s)^\dagger}{\mathrm{Tr}\!\left(L(s) L(s)^\dagger\right)},
$$

where $L: \mathcal{S} \to \mathbb{C}^{7 \times 7}_{\mathrm{lower\text{-}triangular}}$ is a chosen parameterization.

The universal encoder-uniqueness claim **`T-123 [✗]`** is retracted. Normalizing $L(s)L(s)^\dagger$ ensures positive semidefiniteness and unit trace, not that distinct physical states are distinguishable in the observations or that two learned encoders differ by a $G_2$ symmetry. Complete positivity (CPTP) applies to linear maps of operator algebras, not to arbitrary nonlinear feature estimators. Empirical identifiability requires specifying the observation law and checking its fibres via [Reconstruction Identifiability](/docs/applied/research/reconstruction-identifiability).

| System | Parameterization of $G$ | Status |
|---|---|---|
| Neural network | Probe $h \to L \to \Gamma$ via Cholesky (`C25`) | `[C]` |
| Brain (EEG) | Band-power and coherence map into $\mathcal{D}(\mathbb{C}^7)$ | `[Pr]` |
| Organism | Physiological indicator panel (`T-92 [D]`) | `[D]` |

---

## 6. Equalizer Predicates and Conditional Iteration Bounds {#глубинная-структура}

### 6.1 Distinct maps: fixed predicates (`T-54`, `T-55`) vs. real structure $J$

For an endomorphism $m: G \to G$ in the ordinary part of a specified topos, precomposition acts on predicates by $m^*: \Omega^G \to \Omega^G$, defining the fixed-predicate equalizer $\mathrm{Th}_m := \mathrm{Eq}(m^*, \mathrm{id}_{\Omega^G}) \hookrightarrow \Omega^G$ (`T-54 [T]/[D]`). Under separating predicates and $m \neq \mathrm{id}$, $\mathrm{Th}_m$ is a proper subobject (`T-55 [T]`).

| Construction | Carrier | Specified map | Exact scope |
|---|---|---|---|
| Holon iteration | $\Gamma \in \mathcal{D}(\mathbb{C}^7)$ | Chosen $M: \mathcal{D}(\mathbb{C}^7) \to \mathcal{D}(\mathbb{C}^7)$ | Iteration depth depends on a declared detector or operational certificate; finite dimension imposes no universal ceiling |
| Fixed predicates | $\mathrm{Th}_m \hookrightarrow \Omega^G$ | $m^*: p \mapsto p \circ m$ | Proper iff predicates separate and $m \neq \mathrm{id}$ (`T-55 [T]`); not Gödel incompleteness and not a state-space theorem |
| NCG bimodule | Imported $H_F$ | Antiunitary $J: H_F \to H_F$ | $J^2 = +1$ in KO-dim 6 on even-dimensional $H_F$; not an estimator or recursion bound |

These three constructions act on different domains with distinct mathematical roles; grouping them as a unified self-referential mechanism is purely interpretive (`[I]`) and yields no dynamical or mass predictions.

<a id="63-why-exactly-3-levels-of-recursion"></a>

### 6.2 Conditional detector cutoff for contractive iterations

The universal `SAD_MAX = 3` claim is withdrawn: finite dimension and compactness of $\mathcal{D}(\mathbb{C}^7)$ do not bound iteration depth (the identity map iterates arbitrarily far). The Fano incidence fraction $\alpha = 2/3$ enters a specific discrete dephasing channel $\mathcal{D}_{2/3}$; for a continuous dephasing rate $\Gamma_2$ sampled at interval $\Delta t$, the contraction factor is $q = e^{-\Gamma_2 \Delta t}$.

If a specified map obeys $A_n := \|\operatorname{offdiag} M^n(\rho)\| \le q^n A_0$ with $0 < q < 1$ and a detector requires $A_n \ge \varepsilon > 0$ (with $A_0 \ge \varepsilon$), then

$$
n \le \left\lfloor \frac{\log(A_0/\varepsilon)}{\log(1/q)} \right\rfloor.
$$

This is a conditional signal-to-threshold bound for the stated contraction and detector, not a universal cognitive ceiling; see [Depth Tower](/docs/consciousness/hierarchy/depth-tower).

---

## Related documents

- [Premises of UHM](/docs/reference/premises#t-350) — independence of `(Cl₀)`, `(W₀)`, and `T-347`/`T-350`
- [Standard Model](/docs/physics/gauge-symmetry/standard-model) — colour stabilizer and spinor constructions (`T-326`, `T-327`, `T-329`)
- [Spacetime](/docs/core/foundations/spacetime#алгебра-морита) — odd-dimension KO-6 obstruction and `T-175a`
- [Einstein Equations](/docs/physics/gravity/einstein-equations#непертурбативная-извлекаемость) — scope of `T-184`
- [Reconstruction Identifiability](/docs/applied/research/reconstruction-identifiability) — observation fibres replacing `T-123`
- [Axiom of Septicity](/docs/core/foundations/axiom-septicity) — explicit specification of `AP`, `PH`, `QG`, `V`
- [Depth Tower](/docs/consciousness/hierarchy/depth-tower) — conditional detector bounds
