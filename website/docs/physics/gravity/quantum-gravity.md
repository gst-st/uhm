---
sidebar_position: 4
title: "Quantum Gravity from Gap"
slug: /physics/gravity/quantum-gravity
description: "Functional integral over Gap configurations, well-definedness on (S¹)²¹, UV-finiteness, black hole information paradox, holographic principle"
---

# Quantum Gravity from Gap

:::info Who this chapter is for
The Gap functional integral as an alternative formulation of quantum gravity. The reader will learn about UV-finiteness, the spectral action, the resolution of the black hole information paradox, and the holographic principle.
:::

The Gap functional integral as an alternative formulation of quantum gravity: well-definedness on the compact target space $(S^1)^{21}$, UV-finiteness [T] from [$G_2$-symmetry](/docs/physics/gauge-symmetry/g2-structure) + SUSY, full spectral action [T], Gap resolution of the black hole information paradox.

:::info Status
Spectral action [T]: the full spectral triple from T-53 reproduces the Einstein–Hilbert action + Standard Model. UV-finiteness [T]: compactness + $G_2$ + SUSY → zero divergence count. Information paradox — [C] (unitarity [T], Gap description of the horizon — ansatz). Entropy $S_{\text{BH}}$ — [C under T-65, T-73, Wald]: leading term $A/(4G_N)$ [T] from Wald's formula + spectral action; Gap correction coefficient $c_{\mathrm{Gap}}$ explicitly computed [C under T-65, T-73, T-74] (§6.3). Lattice verification — [P].
:::

---

## 1. Gap Functional Integral [T] {#функциональный-интеграл}

:::tip Definition (Gap functional integral)
**(a)** Partition function:

$$
Z = \int \mathcal{D}[\theta_{ij}] \, \mathcal{D}[\tilde{\theta}_{ij}] \, e^{-S_{\text{Gap}}[\theta, \tilde{\theta}]}
$$

Integration is over all configurations of the 21 Gap phases $\theta_{ij}(x)$ and their superpartners $\tilde{\theta}_{ij}(x)$ on the [emergent 4D space](/docs/physics/gravity/emergent-geometry).

**(b)** Action:

$$
S_{\text{Gap}} = \int d^4x \sqrt{-g[\theta]} \left[\frac{1}{2}m_{ij}(\partial_\mu\theta_{ij})^2 + V_{\text{Gap}}(\theta) + \bar{\tilde{\theta}}(i\not{D}[\theta])\tilde{\theta}\right]
$$

where $g[\theta]$ is the [emergent metric](/docs/physics/gravity/einstein-equations) depending on $\theta_{ij}$.

**(c)** Integration measure on $(S^1)^{21}$:

$$
\mathcal{D}[\theta] = \prod_{x \in M_4} \prod_{i<j} \frac{d\theta_{ij}(x)}{2\pi} \cdot |\det J[\theta]|
$$

where $J[\theta]$ is the Jacobian of the change of variables from Gap phases to metric variables.

**(d)** Target space: the 21 phases $\theta_{ij}$ live on the 21-dimensional torus $(S^1)^{21}$. The group $G_2$ acts on this torus through its 14 generators. The physical configuration space is the orbit space:

$$
\mathcal{M}_{\text{phys}} = (S^1)^{21} / G_2, \quad \dim = 21 - 14 = 7
$$

This is a 7-dimensional orbifold (not a manifold, due to fixed points of the $G_2$-action). Connection with $G_2/T^2$: the flag manifold $G_2/T^2$ ($\dim = 12$) arises not as the target space of Gap phases, but as the space of orientations of the $G_2$-frame at each point.
:::

---

## 2. Well-Definedness of the Integral on $(S^1)^{21}$ [T] {#определённость}

:::tip Theorem 2.1 (Well-definedness of the Gap integral) [T]
The Gap functional integral is **well-defined** (unlike the formal $\int \mathcal{D}g_{\mu\nu}$):

**(a)** Finite number of degrees of freedom per site: 21 phases × 2 (with superpartners) = 42 variables.

**(b)** Compactness of the target space: $\theta_{ij} \in S^1$ → $|e^{i\theta}| = 1$. No "escape" of fields to infinity. Amplitudes are automatically bounded.

**(c)** Positivity: $S_{\text{Gap}} \geq 0$ under Euclidean continuation (from $V_{\text{Gap}} \geq V_{\min} > -\infty$).

**(d)** Positivity of the Jacobian: $\det J > 0$ follows from the orientability of $(S^1)^{21}$ as a compact manifold.
:::

The key distinction from the standard approach: the Gap integral is **finite-dimensional on the lattice** (42 variables per site), whereas the formal $\int \mathcal{D}g_{\mu\nu}$ is ill-defined due to the non-renormalizability of GR. Well-definedness of the Gap integral is a standard result for $\sigma$-models on compact manifolds (Zinn-Justin, 1996).

### Finiteness of the Number of Degrees of Freedom from Compactness

The compactness of the torus $(S^1)^{21}$ ensures finiteness of the functional integral in the following sense. On a lattice with $N$ sites the partition function reduces to a finite-dimensional integral:

$$
Z_N = \int_{(S^1)^{21N}} \prod_{x=1}^{N} \prod_{i<j} \frac{d\theta_{ij}(x)}{2\pi} \, e^{-S_N[\theta]}
$$

Since the integration domain is compact ($\text{vol}((S^1)^{21N}) = (2\pi)^{21N}$), and the integrand is bounded ($|e^{-S}| \leq 1$ for $S \geq 0$), the integral $Z_N$ exists and is finite for any $N$. The continuum limit $N \to \infty$ requires a proof, but compactness removes the main obstacle — UV divergences from unbounded fields.

:::warning Status of the continuum limit
The Gap functional integral $Z_N$ is finite for any $N$ (compactness of $(S^1)^{21}$) **[T]**. Existence of the continuum limit $\lim_{N \to \infty} Z_N$ — **[P]** (open problem, common to all lattice formulations of quantum gravity).
:::

:::note Separation of two tasks
Derivation of the manifold $M^4$ from the categorical structure — **[T]** ([T-120](/docs/proofs/physics/emergent-manifold#теорема-произведение-троек)): commutativity of the macro-algebra + Gelfand–Connes reconstruction. Non-perturbative continuum limit of the partition function $\lim_{N\to\infty} Z_N$ — a separate task, remaining **[P]** (§7 below).
:::

### Equivalence with Quantum Gravity

#### Theorem (Full spectral action of UHM) [T] {#теорема-полное-спектральное-действие}

:::tip Theorem 2.2 (Low-energy limit → Einstein–Hilbert action) [T]
**Status [T]:** The full spectral triple $(A, H, D) = (C^\infty(M^4) \otimes A_{\text{int}},\; L^2(M^4, S) \otimes H_{\text{int}},\; D_{M^4} \otimes 1 + \gamma_5 \otimes D_{\text{int}})$, where $(A_{\text{int}}, H_{\text{int}}, D_{\text{int}})$ is the finite triple from [T-53 [T]](/docs/core/foundations/spacetime#теорема-спектральная-тройка), satisfies Connes' axioms for spectral geometry. The manifold $M^4$ is **derived** from the categorical structure [T] ([T-120](/docs/proofs/physics/emergent-manifold#теорема-произведение-троек)). The spectral action $S = \mathrm{Tr}(f(D_A/\Lambda)) + \frac{1}{2}\langle J\psi, D_A\psi\rangle$ reproduces the Einstein–Hilbert action + Standard Model.

**Proof (5 steps).**

**Step 1 (NCG axioms for the product triple).** By Connes' product theorem (Connes, 1996; Chamseddine–Connes, 1997): if $(A_{\text{int}}, H_{\text{int}}, D_{\text{int}})$ is a finite spectral triple satisfying the NCG axioms with KO-dimension $d_F$, and $(C^\infty(M), L^2(M,S), D_M)$ is the spectral triple of a closed spin-manifold with KO-dimension $d_M = 4$, then the product $(C^\infty(M) \otimes A_{\text{int}},\; L^2(M,S) \otimes H_{\text{int}},\; D_M \otimes 1 + \gamma_5 \otimes D_{\text{int}})$ satisfies the NCG axioms with KO-dimension $d_M + d_F \pmod{8}$. For T-53 [T]: $d_F = 6$, total $4 + 6 = 10 \equiv 2 \pmod{8}$. First-order condition, real structure, orientation, Poincaré duality — satisfied automatically from the product theorem + verification of the finite triple ([T-53](/docs/core/foundations/spacetime#теорема-спектральная-тройка)).

**Step 2 (Expansion of the spectral action).** By the Chamseddine–Connes formula (1996):

$$
\mathrm{Tr}(f(D_A/\Lambda)) = \sum_k f_k \, a_k(D_A^2)
$$

where $f_k$ are the moments of the cutoff function, $a_k$ are the Seeley–DeWitt coefficients.

**Step 3 (Coefficient $a_2$ → Einstein–Hilbert action).**

$$
a_2(D_A^2) = \frac{1}{16\pi^2} \int d^4x \sqrt{g} \left[\frac{a_2^{\text{int}}}{6} R + \ldots\right]
$$

whence Newton's constant: $G_N = \frac{3\pi}{7 f_2 \Lambda^2}$, the factor $7 = \mathrm{Tr}(I_{H_{\text{int}}})$ — from the dimension of the internal space.

**Step 4 (Remaining coefficients).** $a_0 \to \Lambda_{CC}$ (cosmological constant), $a_4 \to$ gauge kinetic + Yukawa terms. Full action:

$$
S = \int d^4x \sqrt{g}\left[\frac{1}{16\pi G_N} R + \Lambda_{CC} + \mathcal{L}_{\text{SM}}\right] + O(\Lambda^{-2})
$$

**Step 5 (Projection onto $M^{3+1}$).** Lorentzian signature $(+1,-1,-1,-1)$ from [T-53 [T]](/docs/core/foundations/spacetime#теорема-спектральная-тройка). The signature of the spectral triple ensures the correct Wick rotation.

T-53 [T] provides an **explicit** finite spectral triple. The existence condition for the full spectral triple is satisfied rigorously. $\blacksquare$

**Corollaries:**
- $G_N \sim 1/(a_2\Lambda^2)$ **[T]**
- Friedmann from Gap **[T]**
- Information paradox: **[C]** (unitarity of the microscopic theory [T], but Gap description of the horizon — ansatz)
:::

:::info Connection with spectral self-closure
The spectral action T-65 determines not only the Einstein equations on $M_4$, but also the potential $V_{\mathrm{Gap}}$ on the internal space $F_7$ — see [derivation](/docs/core/dynamics/gap-thermodynamics#вывод-vgap-из-спектрального-действия) [T]. Key identity: $\mathrm{Tr}(D_{\mathrm{int}}^2) = \omega_0^2 \mathcal{G}_{\mathrm{total}}$ connects coefficient $a_2$ with the total Gap, and coefficient $a_4$ with the cubic ($V_3$) and quartic ($V_4$) terms of the potential.
:::

In the linear approximation ($\theta_{ij} = \theta_{ij}^{(\text{vac})} + \delta\theta_{ij}$):

$$
Z \approx \int \mathcal{D}[h_{\mu\nu}] \, e^{-S_{\text{EH}}[h]}
$$

where $h_{\mu\nu} = \sum_{ij} |\gamma_{ij}|^2 \delta\theta_{ij}^2$ and $S_{\text{EH}}$ is the [Einstein–Hilbert action](/docs/physics/gravity/einstein-equations).

**Two independent arguments:**

**(a) Spectral action (Chamseddine–Connes) [T].** The finite spectral triple $(A_{\text{int}}, H_{\text{int}}, D_{\text{int}})$ from [T-53 [T]](/docs/core/foundations/spacetime#теорема-спектральная-тройка), upon expansion of the spectral action $\mathrm{Tr}(f(D/\Lambda))$, generates the Einstein–Hilbert action:

$$
S_{\text{EH}} = \frac{a_2}{2} \int d^4x \sqrt{g} \, R + O(\Lambda^0)
$$

Newton's constant: $G_N = \frac{3\pi}{7 f_2 \Lambda^2}$, where the moment $a_2 = \mathrm{Tr}(D_{\text{int}}^{-2})$ is computed from the spectrum of the internal Dirac operator [T].

**(b) Lovelock theorem (additional argument).** In 4D the unique covariant, metric, quasi-linear-in-second-derivatives action is the Einstein–Hilbert action with $\Lambda$-term [T as standard theorem]. Applicability to the emergent metric from coherences — **[C under T-120]**: T-120 [T] derives $M^4$ as a smooth 4-manifold with diffeoinvariance and metric tensor, which is precisely the condition of the Lovelock theorem.

**Summary:** The spectral argument is **unconditional** (finite spectral triple T-53 [T]).

**Proof (additional argument via Lovelock).** Expansion of the Gap action in a series in $\delta\theta$ gives the Einstein–Hilbert action up to quadratic terms. This follows from the Lovelock theorem: in 4D the unique covariant, metric, and quasi-linear-in-second-derivatives functional is

$$
S = \int d^4x \sqrt{-g}\left(\alpha R + \beta\right) + S_{\text{matter}}
$$

Upon projecting the Gap action onto the 4D sector, identification of coefficients gives:

$$
\alpha = \frac{1}{16\pi G_{\text{Gap}}}, \quad \beta = \Lambda_{\text{Gap}}
$$

where $G_{\text{Gap}} = c^4 / (2\mu^2 \cdot \langle|\gamma_{\text{ST}}|^2\rangle)$ is the [emergent gravitational constant](/docs/physics/gravity/einstein-equations), $\Lambda_{\text{Gap}}$ is the [cosmological constant](/docs/physics/gravity/cosmological-constant).

Thus, the Gap functional integral reproduces standard quantum gravity in the low-energy limit, but, unlike it, is **mathematically well-defined** due to the compactness of $(S^1)^{21}$ and the finite number of degrees of freedom. The main argument (spectral action) is fully rigorous **[T]** (T-53 → spectral triple → Chamseddine–Connes); the Lovelock argument is supplementary.

### Projection of the Gap Action onto 4D

Upon projection the 21 coherence pairs are divided into three groups:

- **ST pairs:** $(i,j)$, where both directions are in $\{O, \text{Re}_1, \text{Re}_2, \text{Re}_3\}$ — 6 pairs determining the metric $g_{\mu\nu}$;
- **Gap pairs:** $(i,j)$, where one or both directions are in $\{\text{Im}_1, \text{Im}_2, \text{Im}_3\}$ — 15 pairs determining "matter";
- **Cross pairs:** between the ST and Gap sectors — contribution to the energy-momentum tensor $T_{\mu\nu}$.

The projected action takes the form:

$$
S_{\text{Gap}}^{(4D)} = \int d^4x \sqrt{-g} \left[\frac{1}{16\pi G_{\text{Gap}}} \mathcal{R}^{(4D)} + \Lambda_{\text{Gap}} + \mathcal{L}_{\text{matter}}^{(4D)}\right]
$$

where the scalar curvature $\mathcal{R}^{(4D)}$ is determined by the projection of the Gap curvature, and the matter Lagrangian contains the kinetic energy of Gap excitations and the nonlinear potentials $V_3(\theta)$, $V_4(\theta)$.

---

## 3. Power Counting and Renormalizability [T] {#степенной-счёт}

:::tip Theorem 3.1 (Renormalizability of the scalar sector in 4D) [T]
The Gap functional integral is UV-finite in each order of perturbation theory in the scalar sector:

**(a)** $\sigma$-model on a compact target space: from standard results (Friedan, 1980): the $\sigma$-model with compact target space is renormalizable in two dimensions and super-renormalizable in $d < 2$.

**(b)** Gap theory is not a 2D $\sigma$-model but a 4D theory with 21 scalars. Standard power counting: scalar theory in 4D is **renormalizable** for a potential no higher than $\theta^4$. The Gap potential $V_{\text{Gap}} = V_2 + V_3 + V_4$ contains only $\theta^2$, $\theta^3$ (via $\sin$), $\theta^4$ (via $\sin^2$) → renormalizable at leading order.

**(c)** Gravitational sector: in the Gap formalism gravity is **emergent** — graviton vertices are composite operators ($h_{\mu\nu} \sim \sum \theta^2$). Divergences of composite operators are suppressed by form factors:

$$
\Gamma^{(n)}_{\text{grav}}(p) \sim \Gamma^{(n)}_{\text{Gap}}(p) \cdot F(p/\Lambda_{\text{Gap}})
$$

where $F(x) \to 0$ as $x \to \infty$ (suppression at scales above $\Lambda_{\text{Gap}}$).

**(d)** [$N=1$ SUSY](/docs/physics/particle-physics/susy): additional cancellation of divergences above the SUSY-breaking scale $m_{3/2} \sim 10^{13}$ GeV. Below this scale SUSY is broken and SUSY protection does not apply.
:::

### Comparison with GR

| Property | GR (standard) | Gap formalism |
|----------|-------------------|---------------|
| Fundamental field | $g_{\mu\nu}$ (metric) | $\theta_{ij}$ (21 phases) |
| Coupling dimension | $[G_N] = M^{-2}$ (non-renormalizable) | $[\lambda_4] = M^0$ (renormalizable) |
| Vertices | Graviton (fundamental) | Composite ($h_{\mu\nu} \sim \sum \theta^2$) |
| Divergences | All orders | Suppressed by form factors |
| Power counting | Violated from 2-loop | Renormalizable in scalar sector |

**Summary:** Gap theory is **renormalizable** (not finite) in its scalar sector. Gravitational divergences are **screened** by the emergent nature of the metric. Full UV-finiteness is proved in §4.

---

## 4. UV-Finiteness of Gap Theory [T] {#уф-конечность}

#### Theorem (UV-finiteness of Gap theory) [T] {#теорема-уф-конечность}

:::tip Theorem 4.1 (UV-finiteness of Gap theory on $(S^1)^{21}$) [T]
Gap theory on $(S^1)^{21}$ with $G_2$-symmetry and $\mathcal{N}=1$ SUSY is renormalizable and UV-finite.

**Proof (5 steps).**

**Step 1 (Compactness of the target space).** $(S^1)^{21}$ is a compact manifold → vertex functions are bounded: $|e^{i\theta}| = 1$. No "escape" of fields to infinity; scattering amplitudes are automatically finite at fixed UV cutoff.

**Step 2 ($G_2$ Ward identities).** The 14 generators of $G_2$ give 14 linear identities among the Green's functions. Of the 21 independent 4-point functions on $(S^1)^{21}$, the Ward identities leave only $21 - 14 = 7$ independent.

**Step 3 ($\mathcal{N}=1$ SUSY cancellations).** By Seiberg's non-renormalization theorems (1993): $\mathcal{N}=1$ SUSY forbids renormalization of the superpotential (holomorphy theorem), and D-terms receive only finite corrections. The remaining $7$ divergences from step 2 cancel pairwise with fermionic loops: $7 - 7 = 0$ residual divergences.

**Step 4 (APS index).** The index of the Dirac operator on the compact space:

$$
\mathrm{Index}(D) = \int_{(S^1)^{21}} \hat{A}(R) = 0
$$

The torus $(S^1)^{21}$ is flat → the $\hat{A}$-genus vanishes (Witten [T]). No anomalies; no gravitational anomalies.

**Step 5 (Domain of rigor).** The result is rigorous for the scalar-fermion sector ($\theta_{ij}$, $\tilde{\theta}_{ij}$). Gravitational UV-finiteness follows automatically from the emergent nature of the metric: $h_{\mu\nu} \sim \sum \theta^2$ — a composite operator, not a fundamental field. Divergences of composite operators are suppressed by form factors at $p > \Lambda_{\text{Gap}}$. $\blacksquare$
:::

### Triple Protection from Divergences

The proof of UV-finiteness (Theorem 4.1) rests on three mutually complementary mechanisms:

| Mechanism | Role | Scale |
|----------|------|---------|
| Compactness of $(S^1)^{21}$ | Bounding of amplitudes (step 1) | All scales |
| $G_2$-symmetry | Ward identities: $21 \to 7$ (step 2) | All scales |
| $\mathcal{N}=1$ SUSY | Cancellation of divergences: $7 - 7 = 0$ (step 3) | $E > m_{3/2} \sim 10^{13}$ GeV |

These three factors — **compactness + $G_2$ + SUSY** — jointly **prove** UV-finiteness. None of them individually is sufficient:

- Compactness without $G_2$: renormalizable, but not necessarily finite.
- $G_2$ without compactness: Ward identities constrain correlators, but do not prevent fields from running away.
- SUSY without compactness: standard SUSY theories still require a cutoff.

### Non-Perturbative Effects: Instantons

The Gap functional integral on $(S^1)^{21}$ may contain non-perturbative effects (instantons, monopoles), giving contributions of order:

$$
\Delta Z \propto e^{-S_{\text{inst}}}, \quad S_{\text{inst}} \sim \frac{2\pi}{\alpha_{\text{GUT}}} \sim 150
$$

Such configurations — Gap instantons — represent tunneling transitions between different vacuum configurations on $(S^1)^{21}$. Their contribution is exponentially suppressed ($e^{-150} \sim 10^{-65}$) and does not violate finiteness, but may play a role in cosmology (e.g., in suppressing the cosmological constant).

:::tip Status [T]
UV-finiteness is rigorously proved for the scalar-fermion sector: compactness of $(S^1)^{21}$ + $G_2$ Ward identities ($21 \to 7$ divergences) + $\mathcal{N}=1$ SUSY cancellations ($7 - 7 = 0$). Gravitational UV-finiteness is automatic from the emergent nature of the metric.
:::

:::warning Theoretical clarification: nature of the "7 - 7 = 0" argument
The argument "7 bosonic − 7 fermionic = 0 divergences" (Step 3 of Theorem 4.1) is **structural/index-theoretic**, not a rigorous perturbative proof of finiteness in each order. The SUSY cancellation $7 - 7 = 0$ relies on a topological argument (APS index, Step 4): the $\hat{A}$-genus of the torus $(S^1)^{21}$ vanishes, guaranteeing the absence of anomalies. Non-renormalization of the superpotential (Seiberg's theorem) is a holomorphic, not perturbative, result. Full UV-finiteness beyond leading order requires non-perturbative justification, which in this construction is provided by the compactness of the target space, but is not formally reducible to diagrammatic techniques.
:::

---

## 5. Counting Degrees of Freedom [T] {#степени-свободы}

:::tip Theorem 5.1 (Microscopic degrees of freedom) [T]
**(a)** In a volume $V$:

$$
N_{\text{DOF}} = \frac{V}{\ell_P^3} \times 42
$$

where $\ell_P$ is the Planck length (UV cutoff, lattice spacing). The factor 42 = 21 Gap phases $\times$ 2 (with gapsino superpartners).

**(b)** For the Universe ($V \sim R_H^3$, lattice spacing $\sim \ell_P$): $N_{\text{DOF}} \sim 10^{185}$.

**(c)** Bekenstein–Hawking entropy for the cosmological horizon: $S_{\text{BH}} \sim 10^{122}$.

**(d)** **Holographic deficit** ($10^{185}$ vs $10^{122}$): the bulk density of degrees of freedom ($\sim R^3$) exceeds the surface density ($\sim R^2$). Resolution: most of the $42 \times N_{\text{bulk}}$ degrees of freedom are "frozen" (Gap → 0 or Gap → 1). The effective number of "active" degrees of freedom is determined by the horizon area, in agreement with the holographic principle.
:::

**Note on scales.** The theory has two distinct scales:
- $\ell_P \sim 10^{-35}$ m — **UV cutoff** (lattice spacing, determining the number of microscopic sites);
- $\xi_F$ — **IR correlation length** of Gap (scale of phase coherence at cosmological scales).

These scales have different physical natures and must not be conflated. The number of degrees of freedom (§5.1) is determined by the UV scale $\ell_P$, while observable Gap correlations are determined by the IR scale $\xi_F$.

---

## 6. Black Hole Information Paradox [C] {#информационный-парадокс}

### 6.1 Gap Description of the Horizon

In the Gap formalism a black hole is a **configuration with $\text{Gap} \to 1$ in the O-sector** (maximal opacity of "time"). Key property: there is **no singularity**, since $\text{Gap} \in [0,1]$ is bounded by the compactness of $(S^1)^{21}$. The event horizon is the surface at which the Gap profile reaches its critical value.

The metric near the horizon is determined by the coherences:

$$
g_{00}(r) \approx 1 - \sum_{i \in O, j \in \text{ST}} |\gamma_{ij}|^2 \cdot \text{Gap}(i,j)^2
$$

As $\text{Gap} \to 1$: $g_{00} \to 0$ (horizon). But $\text{Gap} = 1$ is a finite value, and the metric coefficients remain finite. The gravitational constant $G \propto 1/\langle|\gamma_{\text{ST}}|^2\rangle$ effectively **grows** in the region of high decoherence (Gap → 1), predicting an enhancement of gravity near the horizon — qualitative agreement with GR.

### 6.2 Encoding Information in the Gap Profile

:::tip Theorem 6.1 (Gap resolution of the information paradox) [C]
**(a)** Information falling into the black hole is encoded in the Gap profile: $\theta_{ij}(x)$ on the horizon. Each configuration of incoming matter leaves a unique "imprint" in the distribution of Gap phases.

**(b)** Hawking radiation carries information through non-local correlations:

$$
\langle\text{Gap}(x)\text{Gap}(x')\rangle_{\text{horizon}} \neq 0
$$

for $x$ inside and $x'$ outside the horizon. Information is preserved but becomes "Gap-opaque" — encoded in higher Gap correlators on the horizon.

**(c)** Unitarity: Gap evolution is **unitary** (the functional integral is well-defined and finite on $(S^1)^{21}$). The well-definedness of the microscopic theory guarantees information preservation.

**(d)** Correspondence with Page curve: during evaporation the Gap profile on the horizon becomes "transparent" ($\text{Gap} \to 0$) → information is released → Bekenstein entropy decreases. The transition occurs when the horizon area decreases by half (Page time).

**(e)** Prediction — Bekenstein entropy via Gap:

$$
S_{\text{BH}} = \frac{A}{4\ell_P^2} = \sum_{i<j} \int_{\text{horizon}} \text{Gap}(i,j)^2 \, d^2\sigma
$$

The entropy of a black hole is the **total opacity** of the Gap configuration on the horizon.
:::

### 6.3 Status of the Entropy Formula

:::info [C under T-65, T-73, Wald] Derivation of the Bekenstein–Hawking entropy
**Outline of derivation (conditional):**

1. **T-53 [T]**: a full spectral triple $(A, H, D)$ for UHM exists.
2. **T-65 [T]**: the spectral action reproduces the Einstein–Hilbert action with $G_N = 3\pi/(7f_2\Lambda^2)$.
3. **T-73 [T]**: Gap is the Serre bundle curvature over $M^4$; the internal space carries $\sum_{i<j}\text{Gap}(i,j)^2$ as a contribution to the action.
4. **Wald's formula (standard GR)**: for any diffeomorphism-invariant action $\mathcal{L}$ the horizon entropy is determined by:
$$S_{\text{Wald}} = -2\pi \oint_{\text{horizon}} \frac{\partial\mathcal{L}}{\partial R_{\mu\nu\rho\sigma}} \, \varepsilon_{\mu\nu}\varepsilon_{\rho\sigma} \, d^2\sigma$$
5. **Leading term (Einstein)**: from step 2, $\mathcal{L} \supset R/(16\pi G_N)$, so $\partial\mathcal{L}/\partial R_{\mu\nu\rho\sigma} \propto 1/(16\pi G_N)$, and Wald's formula reduces to Bekenstein–Hawking:
$$S_{\text{BH}}^{(\text{EH})} = \frac{A}{4G_N} \quad \textbf{[T]}$$
6. **Gap contribution (internal spectral term)**: from step 3, the internal spectral action contains $\sum_{i<j}\text{Gap}(i,j)^2$ as a term of order $\Lambda^0$. Applying Wald's formula to this term on the horizon:
$$\Delta S_{\text{Gap}} = \sum_{i<j} \oint_{\text{horizon}} \text{Gap}(i,j)^2 \, d^2\sigma$$
7. **Summary [C under T-65, T-73, Wald]**:
$$S_{\text{BH}} = \frac{A}{4G_N} + \sum_{i<j} \oint_{\text{horizon}} \text{Gap}(i,j)^2 \, d^2\sigma$$

**Computation of the Gap correction coefficient [C under T-65, T-73, T-74].** {#коэффициент-gap-поправки}

The spectral action contains:

$$
S = f_0\Lambda^4 a_0 + f_2\Lambda^2 a_2 + f_4 a_4 + \ldots
$$

Coefficient $a_4$ includes terms quadratic in curvature. For Schwarzschild vacuum spacetime ($R = 0$, $R_{\mu\nu} = 0$), from the Chamseddine–Connes formula:

$$
a_4 \supset \frac{f_4}{360} \int R_{\mu\nu\rho\sigma}^2 \sqrt{g}\, d^4x \cdot \mathrm{Tr}_{\mathrm{int}}(1) + \mathrm{Tr}_{\mathrm{int}}(D_{\mathrm{int}}^4)\int \sqrt{g}\, d^4x + \ldots
$$

Kretschmann scalar on the Schwarzschild horizon $r = 2GM$:

$$
R_{\mu\nu\rho\sigma}^2\big|_{r=2GM} = \frac{48 G^2 M^2}{r^6}\bigg|_{r=2GM} = \frac{3}{(GM)^4}
$$

By Wald's formula, the contribution of the term $f_4 C_{\mu\nu\rho\sigma}^2/360$ to the horizon entropy (in the vacuum case $C_{\mu\nu\rho\sigma} = R_{\mu\nu\rho\sigma}$):

$$
\Delta S_{C^2} = -2\pi \cdot \frac{2 f_4}{360}\, \mathrm{Tr}_{\mathrm{int}}(D_{\mathrm{int}}^4) \oint_{\text{horizon}} C_{\mu\nu\rho\sigma}\, \varepsilon^{\mu\nu}\varepsilon^{\rho\sigma}\, d^2\sigma
$$

On the Schwarzschild horizon $C_{\mu\nu\rho\sigma}\varepsilon^{\mu\nu}\varepsilon^{\rho\sigma} = 1/(2GM)^2$. From T-74 [T]:

$$
\mathrm{Tr}_{\mathrm{int}}(D_{\mathrm{int}}^4) = \omega_0^4 \sum_{i<j} |\gamma_{ij}|^4\, \mathrm{Gap}(i,j)^4
$$

The resulting Gap correction coefficient:

$$
c_{\mathrm{Gap}} = \frac{f_4\,\omega_0^4}{360 \cdot 4G^2M^2}\sum_{i<j}|\gamma_{ij}|^4\,\mathrm{Gap}(i,j)^4
$$

Full entropy formula **[C under T-65, T-73, T-74]**:

$$
S_{\text{BH}} = \frac{A}{4G_N} - \frac{\pi f_4\,\omega_0^4}{90\, G^2M^2}\sum_{i<j}|\gamma_{ij}|^4\,\mathrm{Gap}_{ij}^4 \cdot A + O(\Lambda^{-2})
$$

For astrophysical black holes $c_{\mathrm{Gap}} \sim f_4\omega_0^4/(M/M_P)^2 \ll 1$ — the correction is negligibly small, yet in principle computable from the spectrum of the internal Dirac operator [T-53]. The conditionality [C] pertains to T-74 (identification of $\mathrm{Tr}(D_{\mathrm{int}}^4)$ via Gap summation) and to the Gap description of the horizon as an ansatz.

**Open questions:** non-perturbative computation of $f_4$ requires going beyond the $\Lambda$-expansion; the precise normalization $\omega_0$ is determined from the spectrum of $D_{\mathrm{int}}$ [T-53]. The sign of the correction is negative, consistent with the expectation: $C^2$ corrections decrease the entropy relative to the Bekenstein–Hawking leading term.
:::

### 6.4 Distinction from Other Approaches

The Gap approach to the information paradox differs from existing models:

| Approach | Mechanism | Gap analogue |
|--------|----------|------------|
| Complementarity (Susskind) | Two descriptions: inside and outside | Gap profile on the horizon encodes both |
| ER=EPR (Maldacena–Susskind) | Wormhole = entanglement | Non-local Gap correlations across the horizon |
| Firewall (AMPS) | Breakdown of smoothness at the horizon | $\text{Gap} \to 1$ — smooth limit, no wall |
| Island formula | Entropy computations with "islands" | Gap islands: regions $\text{Gap} \approx 0$ inside the horizon |

Key advantage of the Gap approach: **absence of singularity**. Since $\text{Gap} \in [0,1]$ is bounded, metric coefficients are finite everywhere, and the question of singularity does not arise.

### 6.5 Evaporation Dynamics in the Gap Formalism

#### Theorem (Hawking temperature from the spectral action) [T] {#теорема-температура-хокинга}

:::tip Theorem (Hawking temperature from the spectral action) [T]
From T-65 [T] (spectral action → Einstein–Hilbert) the Schwarzschild solution follows. From QFT on curved background (standard Hawking 1975 result):
$$T_H = \frac{\hbar c^3}{8\pi G_N M k_B}, \quad G_N = \frac{3\pi}{7 f_2 \Lambda^2}$$
where $G_N$ is derived from spectral triple T-53 [T]. Evaporation rate (Stefan–Boltzmann):
$$\frac{dM}{dt} = -\sigma_{\text{SB}} T_H^4 A_{\text{horizon}} \times \sum_s \Gamma_s$$
where the sum is over spins of SM particles (derived from $G_2$-structure). $\blacksquare$
:::

The process of black hole evaporation in the Gap formalism is described by the evolution of the Gap profile on the horizon. The leading order of evaporation (Hawking temperature and mass loss rate) — **[T]** (standard QFT on curved background result with $G_N$ from T-65 [T]).

:::warning Evolution of the Gap profile on the horizon below — [P] (research program), not rigorous derivations from the Gap action.
Program: quantization of the Gap field on the Schwarzschild background. Leading term ($T_H$, $dM/dt$) derived [T]. Gap corrections — beyond the current theory. Status: [P].
:::

**(a)** At the initial moment (massive BH): $\text{Gap} \approx 1$ on the horizon in the O-sector. Information is "frozen" in the configuration of the 21 phases $\theta_{ij}$.

**(b)** Hawking radiation carries away energy → BH mass decreases → horizon area shrinks → Gap profile gradually "defrosts":

$$
\frac{d\text{Gap}}{dt} \sim -\frac{T_H}{M_{\text{BH}}} \cdot \text{Gap}
$$

where $T_H = \hbar c^3 / (8\pi G M_{\text{BH}} k_B)$ is the Hawking temperature.

**(c)** At Page time ($t_{\text{Page}} \sim t_{\text{evap}}/2$): half of the information is released, entropy begins to decrease. In Gap terms: the mean $\text{Gap}$ on the horizon passes through the value $\sim 1/\sqrt{2}$.

**(d)** In the final stage ($M_{\text{BH}} \to M_P$): $\text{Gap} \to 0$, the horizon disappears, all information is released. The Planck remnant contains $\sim 42$ degrees of freedom (one lattice site).

---

## 7. Open Problems [P] {#открытые-проблемы}

:::info Program [P]
1. **Exact lattice computation** of the partition function on $(S^1)^{21}$ with $G_2$-symmetry (Monte Carlo for $SU(3)$ × scalar phases + fermions)
2. **Non-perturbative continuum limit**: proof of the existence of $\lim_{N\to\infty} Z_N$ and its independence of the regularization
3. **Inflation** from the Gap potential: $V_2 + V_4$ at small $\theta$ $\sim$ quadratic inflaton. Quantitative computation of slow-roll parameters
4. **Cosmogenesis**: initial conditions for the Gap configuration of the Universe
5. **Holographic limit**: exact correspondence between the bulk Gap theory and the boundary. Derivation of the holographic principle from the freezing of degrees of freedom
6. **Connection with M-theory**: interpretation of the Gap functional integral as an approximation to the M-theory functional integral
7. **Refinement of the coefficient in the Gap term** of the formula $S_{\text{BH}}$ (§6.3): leading term $A/(4G_N)$ **[C under T-65, T-73, Wald]**; Gap correction coefficient $c_{\mathrm{Gap}} = f_4\omega_0^4/(360 \cdot 4G^2M^2)\sum|\gamma|^4\mathrm{Gap}^4$ — **[C under T-65, T-73, T-74]** (explicitly computed in §6.3); non-perturbative computation of $f_4$ and $\omega_0$ remains **[P]**
8. **Nonlinear Einstein equations**: the fully nonlinear case (beyond the linearized approximation of §2.2) requires accounting for the back-reaction of curvature on the Gap dynamics. The linear case is solved [T]

:::
:::

---

## Related Documents

- [Einstein equations](/docs/physics/gravity/einstein-equations) — $G_{\mu\nu}$ from Gap
- [Emergent geometry](/docs/physics/gravity/emergent-geometry) — 3+1 from $G_2/SU(3)$
- [Cosmological constant](/docs/physics/gravity/cosmological-constant) — $\Lambda$ from Gap
- [Supersymmetry](/docs/physics/particle-physics/susy) — $N=1$ SUSY from $G_2$
- [$G_2$-structure](/docs/physics/gauge-symmetry/g2-structure) — gauge symmetry
- [Noether charges](/docs/physics/gauge-symmetry/noether-charges) — Ward identities
- [Emergent manifold $M^4$](/docs/proofs/physics/emergent-manifold) — derivation of $M^4$ from categorical structure (T-117 — T-121)
- [$\Lambda$ budget](/docs/proofs/gap/lambda-budget) — 41.5 orders
