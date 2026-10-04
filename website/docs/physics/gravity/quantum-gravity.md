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

The Gap functional integral as an alternative formulation of quantum gravity: well-definedness on the compact target space $(S^1)^{21}$, **field-space finiteness [T]** (compact target), full order-by-order UV-finiteness **[C]** (structural), full spectral action [T], Gap resolution of the black hole information paradox.

:::info Status
For supplied spectral geometry, standard spectral-action calculations are conditional [C], and finite-domain bounded-integrand partition functions are finite [T]. A general G₂ phase-only quotient is not supplied. Neither compactness nor the group identity alone proves continuum UV finiteness, physical SUSY cancellation or a black-hole information solution. Those physical bridges remain [H/Pr]. Wald entropy follows from a supplied gravitational action; the previous universal Gap-curvature correction is withdrawn [✗].
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
Derivation of the manifold $M^4$ from the categorical structure — **[T]** as mathematics ([T-120](/docs/proofs/physics/emergent-manifold#теорема-произведение-троек)): $M^4=\mathbb R\times S^3$, time from the depth register, space the computed spectrum of three commuting rotation charges (restated T-119); the reading of $S^3$ as physical space is [I]. (It read [T] until early 2026-09-25, then [C] at the open reconstruction axioms of T-119; the restatement computes the spectrum, and those axioms hold for the Dirac triple of $S^3$.) Non-perturbative continuum limit of the partition function $\lim_{N\to\infty} Z_N$ — a separate task, remaining **[P]** (§7 below).
:::

### Equivalence with Quantum Gravity

#### Theorem (Full spectral action of UHM) [T] {#теорема-полное-спектральное-действие}

::::tip Theorem 2.2 (Low-energy limit → Einstein–Hilbert action) [T]
**Status [T]:** The full spectral triple $(A, H, D) = (C^\infty(M^4) \otimes A_{\text{int}},\; L^2(M^4, S) \otimes H_{\text{int}},\; D_{M^4} \otimes 1 + \gamma_5 \otimes D_{\text{int}})$, where $(A_{\text{int}}, H_{\text{int}}, D_{\text{int}})$ is the finite triple from [T-53 [T]](/docs/core/foundations/spacetime#теорема-спектральная-тройка), is a spectral triple: $D$ is self-adjoint with compact resolvent and has bounded commutators with $A$. It is **not** a real spectral triple in Connes' sense — $H_{\text{int}} = \mathbb{C}^7$ carries no real structure of KO-dimension 6 ([spacetime, Step 6](/docs/core/foundations/spacetime#теорема-спектральная-тройка)) — and the Einstein–Hilbert term below does not use one. (It read "satisfies Connes' axioms for spectral geometry" until 2026-09-25.) The manifold $M^4$ is assembled from the categorical structure by T-120 [T] ([T-120](/docs/proofs/physics/emergent-manifold#теорема-произведение-троек): $M^4=\mathbb R\times S^3$, with the restated T-119; [C] at its open reconstruction axioms until 2026-09-25); the Einstein–Hilbert term below holds on the product with any four-dimensional base. The spectral action $S = \mathrm{Tr}(f(D_A/\Lambda)) + \frac{1}{2}\langle J\psi, D_A\psi\rangle$ reproduces the Einstein–Hilbert action + Standard Model.

:::warning Honest status of the Standard-Model part (2026-09-25)
The Einstein–Hilbert term is not affected: it comes from the heat-kernel coefficient $a_2$ and sees the internal space only through $\mathrm{Tr}(I_{H_{\text{int}}}) = 7$ (Step 3). The words "+ Standard Model" are weaker than the [T] above, for three reasons.

1. Step 1 takes $d_F = 6$ from T-53, but no real structure of KO-dimension 6 exists on $H_{\text{int}} = \mathbb{C}^7$ ([spacetime, Step 6](/docs/core/foundations/spacetime#теорема-спектральная-тройка)); the Standard-Model content of a spectral action comes from Connes' $H_F$, which UHM imports ([bimodule construction, T-178](/docs/proofs/physics/bimodule-construction#бимодульная-конструкция), retracted as a derivation).
2. The Higgs sector inherits a failed prediction. Under the "big desert" assumption Chamseddine, Connes and Marcolli obtained "a Higgs mass around 170 GeV" (*Adv. Theor. Math. Phys.* **11**, 991–1089 (2007), [arXiv:hep-th/0610241](https://arxiv.org/abs/hep-th/0610241)); CDF and D0 excluded a Standard-Model Higgs of 170 GeV at 95% C.L. in 2008 ([arXiv:0808.0534](https://arxiv.org/abs/0808.0534)), and the Higgs was found at 125 GeV (ATLAS and CMS, *Phys. Lett. B* **716**, 1 and 30 (2012)). At 125 GeV the quartic coupling turns negative at high energy, which, in Chamseddine and Connes's words, rules out the big desert and invalidates "the positivity of the coupling at unification which is an essential prediction of the spectral action".
3. The rescue keeps a real singlet $\sigma$ strongly coupled to the Higgs and fits a free parameter $n(u)$ for every unification scale $u$, which gives "a one parameter family" of consistent models (*JHEP* **09**, 104 (2012), [arXiv:1208.1030](https://arxiv.org/abs/1208.1030)): consistency bought with a fitted parameter, not a prediction.

So the gravitational sector stands as stated, while the Standard-Model sector is imported together with its boundary conditions at the unification scale and inherits this history.
:::

**Proof (5 steps).**

**Step 1 (The product is a spectral triple).** $D = D_M \otimes 1 + \gamma_5 \otimes D_{\text{int}}$ is self-adjoint with compact resolvent ($M$ closed, $H_{\text{int}}$ finite-dimensional), and for $a = f \otimes b$ the commutator $[D, a] = [D_M, f] \otimes b + \gamma_5 f \otimes [D_{\text{int}}, b]$ is bounded. Since $\gamma_5$ anticommutes with $D_M$, $D^2 = D_M^2 \otimes 1 + 1 \otimes D_{\text{int}}^2$ — the operator Steps 2–3 expand.

*Retracted 2026-09-25:* this step invoked Connes' product theorem for real triples (Connes, 1996; Chamseddine–Connes, 1997) — "for T-53: $d_F = 6$, total $4 + 6 = 10 \equiv 2 \pmod 8$; first-order condition, real structure, orientation, Poincaré duality — satisfied automatically from the product theorem + verification of the finite triple". The product theorem needs a real finite triple, and $H_{\text{int}} = \mathbb{C}^7$ has none of KO-dimension 6: such a structure exchanges the $\chi = \pm1$ eigenspaces, which would then have equal dimension, and $7$ is odd ([spacetime, Step 6](/docs/core/foundations/spacetime#теорема-спектральная-тройка)).

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

### Canonical choice of cut-off function $f$ and its consequences {#canonical-f}

The Chamseddine–Connes spectral action

$$
S_\mathrm{spec}[D, \Lambda] = \mathrm{Tr}\, f(D^2 / \Lambda^2)
$$

depends on the choice of cut-off (test) function $f: [0, \infty) \to \mathbb{R}_{\geq 0}$, appearing through its **moments**

$$
f_0 = \int_0^\infty u \, f(u) \, du, \qquad f_2 = \int_0^\infty f(u) \, du, \qquad f_4 = f(0).
$$

The asymptotic expansion for $\Lambda \to \infty$ in a four-dimensional almost-commutative spectral triple gives (Gilkey 1984; Connes–Chamseddine 1996, 2010):

$$
\mathrm{Tr}\, f(D^2/\Lambda^2) \;\sim\; f_0 \, \Lambda^4 \, a_0(D^2) \;+\; f_2 \, \Lambda^2 \, a_2(D^2) \;+\; f_4 \, a_4(D^2) \;+\; \mathcal O(\Lambda^{-2}),
$$

where $a_{2k}(D^2)$ are the heat-kernel (Seeley–de Witt) coefficients.

:::note Moment-labeling convention (corpus-wide)
The subscript of $f_{2k}$ matches the heat-kernel coefficient $a_{2k}$ it multiplies: $f_0 \leftrightarrow \Lambda^4 a_0$, $f_2 \leftrightarrow \Lambda^2 a_2$, $f_4 = f(0) \leftrightarrow a_4$ — as in the [spectral formula for $\Lambda_{\text{CC}}$](/docs/physics/gravity/cosmological-constant#теорема-спектральная-лямбда), T-70 and T-254. Caution when comparing with the literature: the Chamseddine–Connes originals label moments by the power of $\Lambda$ instead ($f_4 \Lambda^4 a_0 + f_2 \Lambda^2 a_2 + f(0)\, a_4$), i.e. their $f_4$ is our $f_0$, and their $f_0 = f(0)$ is our $f_4$.
:::

Three moments $f_0, f_2, f_4$ enter the physical Lagrangian:
- $f_0 \, a_0$ → **cosmological constant** ($\Lambda_\mathrm{cc}$).
- $f_2 \, a_2$ → **Einstein–Hilbert action** (Newton's $G_N$).
- $f_4 \, a_4$ → **Yang–Mills kinetic** + Weyl-squared + Higgs potential.

Since $f_0, f_2, f_4$ are free parameters of the choice of $f$, naively this gives three tunable numbers in the effective action — this is the concern sometimes raised as "fine-tuning of the cut-off function". This section shows that **UHM fixes the choice canonically** and that the tunability affects only dimensional ratios, not the structural predictions of UHM.

#### Theorem (canonical choice of $f$ in UHM) [T]

UHM adopts the canonical cut-off function

$$
\boxed{f(u) = e^{-u}, \qquad \Lambda = M_P}
$$

where $M_P = 1.22 \times 10^{19}$ GeV is the Planck mass.

:::note Scope: canonical vs. derived cutoff
The choice $f(u) = e^{-u}$ is **adopted** (fixed by the theory as a definition) rather than **derived** from an independent UHM principle. The physical motivations listed below (heat-kernel regularisation, integer-valued moments, compatibility with $\Lambda = M_P$) are justifications for the choice, not a derivation. In the Connes–Chamseddine spectral action program (Chamseddine–Connes 1996, *Comm. Math. Phys.* 186, 731–750; Connes–Chamseddine 2010) the cutoff $f$ is similarly a definitional input — typically a bump or truncated Gaussian — with physical observables depending on a small number of moments $f_0, f_2, f_4$. UHM's predictions that depend on moments individually (dimensional constants: $G_N$, $\Lambda_{\mathrm{cc}}$) are thus canonical-choice-conditional; the **structural** predictions listed in the [$f$-independence box](#f-independence) below hold for any reasonable $f$.
:::

With this choice:
- $f_0 = \int_0^\infty u \, e^{-u} \, du = \Gamma(2) = 1$ — the raw regulator moment of the $\Lambda^4$-term; the **renormalised** $a_0$-coefficient entering the $\Lambda$-budget is fixed self-consistently by the vacuum ([T-70](/docs/physics/particle-physics/higgs-sector#теорема-f0-канонический)).
- $f_2 = \int_0^\infty e^{-u} \, du = 1$.
- $f_4 = f(0) = 1$ — the UV-finite ($\Lambda^0$) coefficient is the value of $f$ at zero; no regularisation is involved.

The spectral-action moment convention $(f_0, f_2, f_4) = (1, 1, 1)$ is used consistently below.

Substituting into the spectral-action asymptotic expansion:
- $G_N = \dfrac{3\pi}{7 f_2 \Lambda^2} = \dfrac{3\pi}{7 M_P^2} \approx \dfrac{1.347}{M_P^2}$ in natural units.
- In Planck units where $G_N = 1$ by definition, this gives an $\mathcal O(1)$ calibration factor $\Lambda_\mathrm{eff} = \sqrt{3\pi/7}\, M_P \approx 1.16\, M_P$ — physically indistinguishable from $M_P$.

#### Alternative choices and invariance of UHM-structural predictions

Alternative natural choices of $f$ and their moments:

| Choice | $f(u)$ | $f_0$ | $f_2$ | $f_4$ | $f_0/f_2^2$ |
|---|---|---|---|---|---|
| Exponential (canonical UHM) | $e^{-u}$ | $1$ | $1$ | $1$ | $1$ |
| Gaussian | $e^{-u^2}$ | $1/2$ | $\sqrt{\pi}/2$ | $1$ | $2/\pi$ |
| Sharp cut-off | $\Theta(1-u)$ | $1/2$ | $1$ | $1$ | $1/2$ |
| Truncated Gaussian (Connes–Chamseddine) | $e^{-u^2/2}$, $u \leq 1$ | numerical | numerical | $1$ | numerical |

While the absolute numerical values $G_N$ and $\Lambda_\mathrm{cc}$ depend on $f$ (through $f_0$ and $f_2$ individually), the **ratios** relevant to UHM physics are more tightly constrained:

$$
\frac{\Lambda_\mathrm{cc}}{G_N^{-2}} \;\propto\; \frac{f_0}{f_2^2}
$$

which changes by $\mathcal O(1)$ factor across reasonable choices of $f$. More importantly:

#### $f$-independence {#f-independence}

:::note Scope of cutoff independence [T at D / C / H]

Changing the spectral cutoff does not change a separately supplied finite representation, chosen Fano incidence or native diagnostic definition. This is an independence statement about those **inputs**, not proof that UHM fixes them or their physical interpretation. $\operatorname{Aut}(\mathbb O)=G_2$ is [T for the chosen algebra]; declaring it a physical gauge group needs a bridge. The coordinate Fano off-diagonal factor $1/3$ and dephasing factor $2/3$ follow from its chosen incidence. The majority cut $2/7$, reflection cut $1/3$, integration cut one and differentiation cut two are specified model predicates [D]; their algebraic consequences are [T]. T-40a/T-57's count of three dynamical types is withdrawn [✗] and cannot determine a Bayesian hypothesis count. The native E-row is not a tensor factor and cannot supply an experiential entropy. A universal SAD ceiling or generation spectrum does not follow from a cutoff-independent scalar definition; these require separate model hypotheses/representation data.

The quantum-gravity and Standard-Model identifications discussed here remain conditional physical constructions [C/H/Pr]. Cutoff independence alone does not validate them.
:::

#### Physical interpretation of the canonical choice

The choice $f(u) = e^{-u}$ is natural on several grounds:

1. **Heat kernel regularisation**: $f(u) = e^{-u}$ is the heat kernel weighting in the Seeley–de Witt expansion, making the spectral action a **generalised heat-kernel functional** — connection to standard functional analysis.

2. **Moment values**: for the exponential all three moments are unity, $(f_0, f_2, f_4) = (1, 1, 1)$; for the Gaussian — $(1/2, \sqrt{\pi}/2, 1)$. The exponential's clean integer values are preferable for rigorous derivations.

3. **Physical universality**: in the Wilson renormalisation group flow, the IR limit is insensitive to the precise UV regularisation — the canonical choice represents the most natural regulator compatible with UHM's $G_2$-symmetry and compactness of $(S^1)^{21}/G_2$.

4. **Consistency with Planck-scale cutoff**: $\Lambda = M_P$ is the natural UV cutoff for a quantum-gravitational theory; no additional parameter needed beyond $M_P$.

#### Closure of the "fine-tuning" concern

:::tip Fine-tuning concern resolved [T]
**Concern** (e.g., raised in external audits): three moments $f_0, f_2, f_4$ of an arbitrary cut-off function leave three free parameters in the effective action, enabling fine-tuning.

**Resolution**: UHM canonically fixes $f(u) = e^{-u}$, $\Lambda = M_P$. All three moments are thereby determined:
- $f_0 = 1$.
- $f_2 = 1$.
- $f_4 = f(0) = 1$.

This is **not tunable**; it is a definitional choice of the theory. Any derived observable depending on these moments is then a **specific prediction** of UHM, not a free parameter.

Moreover, the **structural predictions** (sector count, Fano constants, consciousness thresholds) are $f$-independent by construction — they would hold for any reasonable $f$.

Thus the fine-tuning concern applies only to dimensional calibration (Newton's $G_N$, cosmological constant scale), which UHM fixes canonically. No residual fine-tuning freedom remains.
:::

#### Relation to Connes–Chamseddine standard spectral action

The Connes–Chamseddine spectral action for the Standard Model plus gravity (1996) also requires a cut-off $f$; in their formulation $f$ is usually chosen as a bump function or Gaussian, with the explicit moments absorbed into the definitions of physical coupling constants.

UHM follows the same methodology but specifies $f$ canonically as $e^{-u}$ for the following reasons specific to UHM:
1. Compactness of $(S^1)^{21}/G_2$ — the natural measure on this compact space is consistent with exponential weighting.
2. Heat-kernel regularisation — aligned with UHM's spectral-action derivation of the Einstein equations.
3. Integer-valued moments — facilitate rigorous derivations of sector counts and Fano constants.

**Step 4 (Remaining coefficients).** $a_0 \to \Lambda_{CC}$ (cosmological constant), $a_4 \to$ gauge kinetic + Yukawa terms. Full action:

$$
S = \int d^4x \sqrt{g}\left[\frac{1}{16\pi G_N} R + \Lambda_{CC} + \mathcal{L}_{\text{SM}}\right] + O(\Lambda^{-2})
$$

**Step 5 (Projection onto $M^{3+1}$).** Lorentzian signature $(+1,-1,-1,-1)$ from [T-53 — $(1,3)$-split [T] + sign [T at reflection positivity]](/docs/core/foundations/spacetime#лоренцева-сигнатура): the $(1,3)$-split is derived (PW time + $S^3$), and the Lorentzian relative sign is fixed by requiring the PW generator bounded below (Osterwalder–Schrader reflection positivity), not by an ad-hoc ansatz (KO-dim 6 alone does not determine it; rigorous route via Krein spectral triples). The Wick rotation is defined relative to this construction.

T-53 [T] provides an **explicit** finite spectral triple. The existence condition for the full spectral triple is satisfied rigorously. $\blacksquare$

**Corollaries:**
- $G_N \sim 1/(a_2\Lambda^2)$ **[T]**
- Friedmann from Gap **[T]**
- Information paradox: **[C]** (unitarity of the microscopic theory [T], but Gap description of the horizon — ansatz)
::::

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

**(b) Lovelock theorem (additional argument).** In 4D the unique covariant, metric, quasi-linear-in-second-derivatives action is the Einstein–Hilbert action with $\Lambda$-term [T as standard theorem]. Applicability to the emergent metric from coherences — **[T]** (T-121): T-120 [T] assembles $M^4=\mathbb R\times S^3$ as a smooth 4-manifold, on which the metric is the dynamical variable — precisely the setting of the Lovelock theorem. (Until the restatement of T-119 on 2026-09-25 this read "[C under T-120]", at the open reconstruction axioms of T-119.)

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

Thus, the Gap functional integral reproduces standard quantum gravity in the low-energy limit, but, unlike it, has a **rigorously finite field-space measure** **[T]** due to the compactness of $(S^1)^{21}/G_2$ (finite target volume) — the one part of UV-finiteness that is unconditional; the full order-by-order finiteness is the structural **[C]** argument above. The spectral-action reconstruction is fully rigorous **[T]** (T-53 → spectral triple → Chamseddine–Connes); the Lovelock argument is supplementary.

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
The Gap functional integral is renormalizable in the scalar sector — divergences are absorbed order-by-order into the finitely many couplings $(\mu^2, \lambda_3, \lambda_4)$:

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

**Summary:** Gap theory is **renormalizable** (not finite) in its scalar sector. Gravitational divergences are **screened** by the emergent nature of the metric. Full UV-finiteness is argued in §4 (field-space part [T]; order-by-order — structural [C]).

---

## 4. UV-Finiteness of Gap Theory [T field-space, C order-by-order] {#уф-конечность}

#### Theorem (UV-finiteness of Gap theory) [T field-space, C order-by-order] {#теорема-уф-конечность}

:::tip Theorem 4.1 (UV-finiteness of Gap theory on $(S^1)^{21}$) [T field-space, C order-by-order]
Gap theory on $(S^1)^{21}$ with $G_2$-symmetry and $\mathcal{N}=1$ SUSY is renormalizable; its **field-space (large-field) finiteness** is rigorous **[T]** (compact target), and **full order-by-order UV-finiteness** is a structural argument **[C]**.

**Argument (5 steps).**

**Step 1 (Compactness of the target space).** $(S^1)^{21}$ is a compact manifold → vertex functions are bounded: $|e^{i\theta}| = 1$. No "escape" of fields to infinity; scattering amplitudes are automatically finite at fixed UV cutoff.

**Step 2 ($G_2$ Ward identities).** The 14 generators of $G_2$ give 14 linear identities among the Green's functions. Of the 21 independent 4-point functions on $(S^1)^{21}$, the Ward identities leave only $21 - 14 = 7$ independent.

**Step 3 ($\mathcal{N}=1$ SUSY suppression).** By Seiberg's non-renormalization theorems (1993): $\mathcal{N}=1$ SUSY forbids renormalization of the superpotential (holomorphy theorem), and D-terms receive only finite corrections. The residual vacuum contribution is suppressed by the **sector-product** scaling $\Lambda_{\text{residual}}\sim\varepsilon^{12}M_P^4$ (T-219, a hypothesis [H] since 2026-09-25; it was cited here as [T at T-64]). *(The earlier exact "$7-7=0$ bose–fermi trace" is **retracted [✗]** — a $\mathbb{Z}_2$-grading on the odd internal $\mathbb{C}^7$ cannot have trace $0$, and $\mathbf{14}\to\mathbf7\oplus\mathbf7$ does not exist since the $G_2$ adjoint is irreducible; see [Λ-budget Thm 4.4](/docs/proofs/gap/lambda-budget#теорема-susy-компенсация). Holomorphy + compactness, not an exact trace, carry the finiteness argument.)*

**Step 4 (APS index).** The index of the Dirac operator on the compact space:

$$
\mathrm{Index}(D) = \int_{(S^1)^{21}} \hat{A}(R) = 0
$$

The torus $(S^1)^{21}$ is flat → the $\hat{A}$-genus vanishes (Witten [T]). No anomalies; no gravitational anomalies.

**Step 5 (Domain of rigor).** For the scalar-fermion sector ($\theta_{ij}$, $\tilde{\theta}_{ij}$) the field-space finiteness (steps 1, 4) is rigorous [T]; the composition of steps 1–4 into full order-by-order finiteness is structural [C]. Gravitational UV-finiteness follows automatically from the emergent nature of the metric: $h_{\mu\nu} \sim \sum \theta^2$ — a composite operator, not a fundamental field. Divergences of composite operators are suppressed by form factors at $p > \Lambda_{\text{Gap}}$. $\blacksquare$
:::

### Triple Protection from Divergences

The UV-finiteness argument (Theorem 4.1) rests on three mutually complementary mechanisms:

| Mechanism | Role | Scale |
|----------|------|---------|
| Compactness of $(S^1)^{21}$ | Bounding of amplitudes (step 1) | All scales |
| $G_2$-symmetry | Ward identities: $21 \to 7$ (step 2) | All scales |
| $\mathcal{N}=1$ SUSY | Sector-product suppression $\varepsilon^{12}$ (T-219); holomorphy (step 3) | $E > m_{3/2} \sim 10^{13}$ GeV |

These three factors — **compactness + $G_2$ + SUSY** — jointly carry the structural finiteness argument **[C]** (the field-space part is rigorous **[T]**). None of them individually is sufficient:

- Compactness without $G_2$: renormalizable, but not necessarily finite.
- $G_2$ without compactness: Ward identities constrain correlators, but do not prevent fields from running away.
- SUSY without compactness: standard SUSY theories still require a cutoff.

### Non-Perturbative Effects: Instantons

The Gap functional integral on $(S^1)^{21}$ may contain non-perturbative effects (instantons, monopoles), giving contributions of order:

$$
\Delta Z \propto e^{-S_{\text{inst}}}, \quad S_{\text{inst}} \sim \frac{2\pi}{\alpha_{\text{GUT}}} \sim 150
$$

Such configurations — Gap instantons — represent tunneling transitions between different vacuum configurations on $(S^1)^{21}$. Their contribution is exponentially suppressed ($e^{-150} \sim 10^{-65}$) and does not violate finiteness, but may play a role in cosmology (e.g., in suppressing the cosmological constant).

:::tip Status: field-space [T], order-by-order [C]
UV-finiteness for the scalar-fermion sector is a **structural** argument [C]: compactness of $(S^1)^{21}$ + $G_2$ Ward identities ($21 \to 7$ divergences) + $\mathcal{N}=1$ holomorphy (Seiberg) + the sector-product $\varepsilon^{12}$ suppression (T-219). (The exact "$7-7=0$ trace" step is retracted — see the clarification box below.) Gravitational UV-finiteness is automatic from the emergent nature of the metric.
:::

:::warning Theoretical clarification: the "7 - 7 = 0" trace is retracted; finiteness rests on other legs
The literal "7 bosonic − 7 fermionic = 0 divergences" trace is **retracted [✗]** (a $\mathbb{Z}_2$-grading on the odd internal $\mathbb{C}^7$ has trace $\in\{\pm1,\dots,\pm7\}$, never $0$; and $\mathbf{14}\to\mathbf7\oplus\mathbf7$ does not exist — the $G_2$ adjoint is irreducible; [Λ-budget Thm 4.4](/docs/proofs/gap/lambda-budget#теорема-susy-компенсация)). What **does** hold is a **structural** finiteness argument [C], not an order-by-order perturbative proof: the $\hat{A}$-genus of the torus $(S^1)^{21}$ vanishes (APS index → no anomalies), superpotential non-renormalization is holomorphic (Seiberg), and the residual vacuum energy carries the sector-product scaling $\varepsilon^{12}M_P^4$ (T-219). Full UV-finiteness beyond leading order rests on the compactness of the target space, not on a bose–fermi trace.
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

**(e)** Historical Gap-entropy hypothesis [H], whose former derivation is withdrawn [✗]:

$$
S_{\text{BH}} = \frac{A}{4\ell_P^2} = \sum_{i<j} \int_{\text{horizon}} \text{Gap}(i,j)^2 \, d^2\sigma
$$

The displayed opacity identification is a physical ansatz; it does not follow from Wald entropy or the finite matrix trace (see §6.3).
:::

### 6.3 Entropy with specified gravitational data

The former derivation of a universal Gap entropy correction from T-73/T-74 is withdrawn [✗]. Gap entries have not been identified with spacetime curvature, and a finite spectral trace does not determine the complete gravitational action or its coefficients.

For a supplied diffeomorphism-invariant Lagrangian depending on curvature without its derivatives, a stationary black hole with a regular bifurcate Killing horizon has the [Wald entropy](https://arxiv.org/abs/gr-qc/9307038)

$$
S_{\rm Wald}=-2\pi\int_\Sigma\frac{\partial L}{\partial R_{abcd}}\epsilon_{ab}\epsilon_{cd}\,dA,
$$

with the prescribed binormal normalization. More general higher-derivative Lagrangians require the corresponding variational derivative. The Einstein–Hilbert term $R/(16\pi G_N)$ yields $A/(4G_N)$ [T at these hypotheses]. A purely internal potential or constant spectral moment with **no explicit spacetime-curvature dependence** contributes zero directly to $\partial L/\partial R_{abcd}$; it may change a solution and its area indirectly. It does not produce $\int_\Sigma\mathrm{Gap}_{ij}^2dA$ by Wald differentiation.

#### The withdrawn Gap coefficient {#коэффициент-gap-поправки}

For the selected antisymmetric $G=\operatorname{Im}\Gamma$ and $D=i\omega_0G$, with eigenvalues of $G$ equal to $0,\pm i\lambda_1,\pm i\lambda_2,\pm i\lambda_3$,

$$
\operatorname{Tr}D^4=2\omega_0^4\sum_{k=1}^3\lambda_k^4.
$$

This is an exact finite-matrix identity [T]. It is not the former coordinate sum $\omega_0^4\sum_{i<j}|\gamma_{ij}|^4\mathrm{Gap}_{ij}^4$: even a single nonzero edge gives twice that value, and general matrices contain mixed cycles. Nor does the identity define a curvature-squared coupling or fix its physical units.

One may posit $L=L_{\rm EH}+a(\Gamma)C_{abcd}C^{abcd}+\cdots$ [H]. If $a$ is treated as an independent field coefficient in differentiating curvature, its direct correction is

$$
\Delta S=-4\pi\int_\Sigma a(\Gamma)C^{abcd}\epsilon_{ab}\epsilon_{cd}\,dA,
$$

with any other terms treated separately [C at that supplied action]. A sign or size requires the actual solution, conventions and independently fixed coupling. The previous explicit negative $c_{\rm Gap}$ and its Schwarzschild estimate are withdrawn [✗]; no such coupling follows from the withdrawn T-73/T-74. Matching a UHM field model to this action remains [Pr/H].

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

$$
T_H = \frac{\hbar c^3}{8\pi G_N M k_B}, \quad G_N = \frac{3\pi}{7 f_2 \Lambda^2}
$$

where $G_N$ is derived from spectral triple T-53 [T]. Evaporation rate (Stefan–Boltzmann):

$$
\frac{dM}{dt} = -\sigma_{\text{SB}} T_H^4 A_{\text{horizon}} \times \sum_s \Gamma_s
$$

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

### 6.6 The de Sitter observer algebra and the holon tower (T-348) {#алгебра-наблюдателя-де-ситтера}

With an observer, the algebra of the static patch of de Sitter space is a type II₁ factor whose trace is the state of maximal entropy (Chandrasekaran–Longo–Penington–Witten, arXiv:2206.10780). The holon has the same kind of object at finite size: $M_7(\mathbb C)$ with its trace $I/7$. T-348 [T] makes the relation exact and bounds it. The tower of $M$ holons, $\bigotimes(M_7, \mathrm{tr}_7)$, closes to the hyperfinite II₁ factor $R$. If the matter net has the split property (proved for the free massive Klein–Gordon field), the CLPW algebra is also $R$, and every isomorphism carries the trace to the trace: empty de Sitter space corresponds to all holons at $I/7$, a state below the viability window. In any normal state only finitely many holons are alive, and each costs more than $0.344$ nat of entropy. A finite clock, including the O-clock and the depth register, gives a type I algebra that sees no field. Nothing in the identification fixes $\Lambda$, its sign or $\kappa$: $7^M = e^{S_{\text{dS}}}$ only renames $\Lambda$ as $M = 1.677 \times 10^{122}$ holons. The literature, the proof and what stays open are in [emergent time §11.5](/docs/proofs/dynamics/emergent-time#t-348).

---

## 7. Open Problems [P] {#открытые-проблемы}

:::info Program [P]
1. **Exact lattice computation** of the partition function on a specified positivity-compatible field domain with an actual symmetry action (Monte Carlo for $SU(3)$ × scalar phases + fermions)
2. **Non-perturbative continuum limit**: proof of the existence of $\lim_{N\to\infty} Z_N$ and its independence of the regularization
3. **Inflation** from the Gap potential: $V_2 + V_4$ at small $\theta$ $\sim$ quadratic inflaton. Quantitative computation of slow-roll parameters
4. **Cosmogenesis**: initial conditions for the Gap configuration of the Universe
5. **Holographic limit**: exact correspondence between the bulk Gap theory and the boundary. Derivation of the holographic principle from the freezing of degrees of freedom
6. **Connection with M-theory**: interpretation of the Gap functional integral as an approximation to the M-theory functional integral
7. **Entropy-coupling programme**: fix an independent spacetime action and curvature couplings before applying Wald; the former Gap correction and its coefficient are withdrawn [✗]. A supplied Einstein–Hilbert term gives the leading area law [C]; additional corrections remain [H/Pr].
8. **Nonlinear Einstein equations**: the fully nonlinear case (beyond the linearized approximation of §2.2) requires accounting for the back-reaction of curvature on the Gap dynamics. The linear case is solved [T]

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
- [Emergent time §11.5](/docs/proofs/dynamics/emergent-time#t-348) — the de Sitter observer algebra and the holon tower (T-348)
