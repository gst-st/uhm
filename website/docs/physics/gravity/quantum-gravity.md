---
sidebar_position: 4
title: "The Gap Lattice Model and Quantum Gravity"
slug: /physics/gravity/quantum-gravity
description: "Functional integral over Gap configurations, well-definedness on (S¹)²¹, UV-finiteness, black hole information paradox, holographic principle"
---

# The Gap Lattice Model and Quantum Gravity

This chapter compares a finite lattice integral with the heat-kernel expansion on a specified four-dimensional geometry. The relation between their dynamics remains open.

:::info Status
For supplied spectral geometry, standard spectral-action calculations are conditional [C], and finite-domain bounded-integrand partition functions are finite [T]. A general G₂ phase-only quotient is not supplied. Neither compactness nor the group identity alone proves continuum UV finiteness, physical SUSY cancellation or a black-hole information solution. Those physical bridges remain [H/Pr]. Wald entropy follows from a supplied gravitational action; the previous universal Gap-curvature correction is withdrawn [✗].
:::

---

## 1. Proposed continuum phase action {#функциональный-интеграл}

:::tip Definition (Gap functional integral)
**(a)** Partition function:

$$
Z = \int \mathcal{D}[\theta_{ij}] \, \mathcal{D}[\tilde{\theta}_{ij}] \, e^{-S_{\text{Gap}}[\theta, \tilde{\theta}]}
$$

This formal continuum expression assumes a spacetime, phase fields and fermionic partners. A finite-site definition appears in §2.

**(b)** Action:

$$
S_{\text{Gap}} = \int d^4x \sqrt{-g[\theta]} \left[\frac{1}{2}m_{ij}(\partial_\mu\theta_{ij})^2 + V_{\text{Gap}}(\theta) + \bar{\tilde{\theta}}(i\not{D}[\theta])\tilde{\theta}\right]
$$

Here $g[\theta]$ denotes a proposed field-to-metric map. Its covariance and dynamics are open. [Metric ansatz](/docs/physics/gravity/einstein-equations)

**(c)** Integration measure on $(S^1)^{21}$:

$$
\mathcal{D}[\theta] = \prod_{x \in M_4} \prod_{i<j} \frac{d\theta_{ij}(x)}{2\pi} \cdot |\det J[\theta]|
$$

A Jacobian requires an actual change of variables with specified rank and measure. The phase coordinates at fixed populations and moduli do not carry the usual continuous $G_2$ conjugation action, which changes the moduli and populations. The former subtraction $21-14=7$ for a physical phase quotient is withdrawn. A phase-torus integral may instead be defined as a separate lattice model, with any density-matrix positivity constraints specified.
:::

---

## 2. Finiteness at a fixed lattice cutoff {#определённость}

:::tip Theorem 2.1 (Well-definedness of the Gap integral) [T]
For finitely many sites and bounded measurable integrand on a finite-measure domain the integral is finite. A continuous real action on a compact torus is bounded below, so its exponential meets this criterion. Extra Jacobians and fermion determinants require their own bounds. Orientability alone has no implication for the sign of a proposed Jacobian.
:::

### Finiteness of the Number of Degrees of Freedom from Compactness

The compactness of the torus $(S^1)^{21}$ ensures finiteness of the functional integral in the following sense. On a lattice with $N$ sites the partition function reduces to a finite-dimensional integral:

$$
Z_N = \int_{(S^1)^{21N}} \prod_{x=1}^{N} \prod_{i<j} \frac{d\theta_{ij}(x)}{2\pi} \, e^{-S_N[\theta]}
$$

This gives finiteness for each fixed $N$. Existence of a continuum limit requires uniform estimates and a specified scaling with the lattice spacing.

:::warning Status of the continuum limit
The Gap functional integral $Z_N$ is finite for any $N$ (compactness of $(S^1)^{21}$) **[T]**. Existence of the continuum limit $\lim_{N \to \infty} Z_N$ — **[P]** (open problem, common to all lattice formulations of quantum gravity).
:::

:::note Separation of two tasks
Derivation of the manifold $M^4$ from the categorical structure — **[T]** as mathematics ([T-120](/docs/proofs/physics/emergent-manifold#теорема-произведение-троек)): $M^4=\mathbb R\times S^3$, time from the depth register, space the computed spectrum of three commuting rotation charges (restated T-119); the reading of $S^3$ as physical space is [I]. (It read [T] until early 2026-09-25, then [C] at the open reconstruction axioms of T-119; the restatement computes the spectrum, and those axioms hold for the Dirac triple of $S^3$.) Non-perturbative continuum limit of the partition function $\lim_{N\to\infty} Z_N$ — a separate task, remaining **[P]** (§7 below).
:::

### Equivalence with Quantum Gravity

#### Theorem (Full spectral action of UHM) [T] {#теорема-полное-спектральное-действие}

::::tip Theorem 2.2 (Low-energy limit → Einstein–Hilbert action) [T]
**T-65 [T under the product and heat-kernel hypotheses].** On a closed Riemannian spin four-manifold with specified metric, the external Dirac operator and a finite internal operator form a product whose $a_2$ coefficient contains the Einstein–Hilbert term. On noncompact $\mathbb R\times S^3$ one needs separate trace or localization hypotheses. The dimension-seven multiplicity is sufficient for this calculation. A Standard Model fermion representation is additional input.

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
- $f_0=\int_0^\infty u e^{-u}\,du=1$. The renormalized vacuum coefficient also requires a subtraction prescription.
- $f_2 = \int_0^\infty e^{-u} \, du = 1$.
- $f_4 = f(0) = 1$ — the UV-finite ($\Lambda^0$) coefficient is the value of $f$ at zero; no regularisation is involved.

The spectral-action moment convention $(f_0, f_2, f_4) = (1, 1, 1)$ is used consistently below.

Substituting into the spectral-action asymptotic expansion:
- $G_N = \dfrac{3\pi}{7 f_2 \Lambda^2} = \dfrac{3\pi}{7 M_P^2} \approx \dfrac{1.347}{M_P^2}$ in natural units.
- In natural units $M_P=G_N^{-1/2}$ for the unreduced Planck mass. Matching the measured $G_N$ fixes $\Lambda_{\rm eff}=\sqrt{3\pi/7}\,M_P$ when $f_2=1$. This is a calibration.

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

A regulator-independent low-energy limit would require a renormalization argument for the specified dynamics.

#### Closure of the "fine-tuning" concern

Choosing $f(u)=e^{-u}$ fixes three moments. A prediction for the dimensional $G_N$ would require an independently determined cutoff scale. The renormalized vacuum energy also requires a physical normalization.

#### Relation to Connes–Chamseddine standard spectral action

The Connes–Chamseddine spectral action for the Standard Model plus gravity (1996) also requires a cut-off $f$; in their formulation $f$ is usually chosen as a bump function or Gaussian, with the explicit moments absorbed into the definitions of physical coupling constants.

**Step 4.** The remaining coefficients depend on the cutoff moments, the curvature and the specified internal fields. Inserting the Standard Model module reproduces terms for the fields in that module.

**Step 5.** The expansion is Riemannian. A Lorentzian interpretation requires causal or reflection-positivity data and a choice of state. Cosmological solutions require matter, a metric ansatz and initial conditions. None of these is selected by the internal trace.
::::

For a specified finite $D_{\rm int}$, $\mathrm{Tr}(D_{\rm int}^2)$ is an internal spectral statistic. The withdrawn T-74 does not determine a universal internal potential or measure. Replacing a phase integral by an Einstein–Hilbert metric integral would require a demonstrated map of domains, action and measure. The Lovelock theorem on a four-manifold supplies none of these. [Metric projection](/docs/physics/gravity/einstein-equations)

### Projection of the Gap Action onto 4D

The former projection used three real components of a colour triplet as spatial axes and the remaining components as matter. The real six-dimensional representation of the stabilizer $SU(3)$ is irreducible. Counting the 21 pairs after a choice of axes does not identify a metric or a field spectrum. A constructive network alternative defines distances from transfer costs under relay, separation and calibration assumptions. Its ring and product examples admit common metric limits under the specified refinements. They supply no Einstein dynamics. [Limiting network geometry](/docs/geometry/common-limit)

---

## 3. Power counting for the polynomial truncation {#степенной-счёт}

**Theorem 3.1 [T for the polynomial truncation].** On a supplied four-dimensional flat background, canonically normalized scalar fields have mass dimension one. Local potential operators through degree four have nonnegative coupling dimension. Power-counting renormalizability concerns a scalar theory with all allowed counterterms. It does not prove that a complete periodic nonlinear theory, a composite metric or a gravity sector has a finite continuum limit.

### Comparison with GR

In four-dimensional Einstein gravity $[G_N]=M^{-2}$. Calling a putative graviton composite does not bound its high-momentum amplitudes. Any proposed form factor must be obtained from the actual propagators and vertices.

---

## 4. The open continuum limit {#уф-конечность}

#### Theorem 4.1 (scope of finiteness) {#теорема-уф-конечность}

The bound on the finite-lattice integral in Theorem 2.1 controls the field amplitude at fixed resolution. Removing the lattice cutoff introduces arbitrarily short wavelengths. A renormalized continuum limit and order-by-order gravitational finiteness remain open.

### Triple Protection from Divergences

A Ward identity requires a specified symmetry of the action and measure. The finite phase torus alone supplies no continuous $G_2$ action. An $\mathcal N=1$ non-renormalization theorem presupposes supersymmetric field content and constrains a superpotential. The absence of all ultraviolet divergences is a stronger claim.

### Non-Perturbative Effects: Instantons

The Gap functional integral on $(S^1)^{21}$ may contain non-perturbative effects (instantons, monopoles), giving contributions of order:

$$
\Delta Z \propto e^{-S_{\text{inst}}}, \quad S_{\text{inst}} \sim \frac{2\pi}{\alpha_{\text{GUT}}} \sim 150
$$

Such configurations — Gap instantons — represent tunneling transitions between different vacuum configurations on $(S^1)^{21}$. Their contribution is exponentially suppressed ($e^{-150} \sim 10^{-65}$) and does not violate finiteness, but may play a role in cosmology (e.g., in suppressing the cosmological constant).

The trace cancellation previously used in this argument was withdrawn. The trace of a grading on an odd-dimensional space cannot vanish, and the adjoint $\mathbf{14}$ of $G_2$ is irreducible. An index of a chosen operator does not by itself cancel physical anomalies. [Vacuum-energy budget](/docs/proofs/gap/lambda-budget#теорема-susy-компенсация)

---

## 5. Counting degrees of freedom in a specified lattice model {#степени-свободы}

:::note Theorem 5.1 [C under a three-dimensional Planck lattice and supplied partners]
**(a)** In a volume $V$:

$$
N_{\text{DOF}} = \frac{V}{\ell_P^3} \times 42
$$

where $\ell_P$ is the Planck length (UV cutoff, lattice spacing). The factor 42 = 21 Gap phases $\times$ 2 (with gapsino superpartners).

**(b)** For the Universe ($V \sim R_H^3$, lattice spacing $\sim \ell_P$): $N_{\text{DOF}} \sim 10^{185}$.

**(c)** Bekenstein–Hawking entropy for the cosmological horizon: $S_{\text{BH}} \sim 10^{122}$.

**(d)** The two counts scale with volume and area respectively. A mechanism relating the number of active sites to the horizon area has not been derived.
:::

**Note on scales.** The theory has two distinct scales:
- $\ell_P \sim 10^{-35}$ m — **UV cutoff** (lattice spacing, determining the number of microscopic sites);
- $\xi_F$ — **IR correlation length** of Gap (scale of phase coherence at cosmological scales).

These scales have different physical natures and must not be conflated. The number of degrees of freedom (§5.1) is determined by the UV scale $\ell_P$, while observable Gap correlations are determined by the IR scale $\xi_F$.

---

## 6. Black hole information [Pr] {#информационный-парадокс}

### 6.1 Gap Description of the Horizon

A proposed model assigns large $O$-sector opacity to the horizon [H]. A horizon is defined by the causal structure of a spacetime solution. A bounded internal variable neither constructs this solution nor bounds curvature or establishes geodesic completeness.

### 6.2 Encoding Information in the Gap Profile

:::note Theorem 6.1 (information-recovery proposal) [H/Pr]
A recovery claim requires a microscopic evolution, an encoding of incoming states, an outgoing radiation channel and a proof that the relevant states can be recovered. Nonzero correlations between two readouts do not by themselves give such recovery. A finite partition function does not establish unitarity. The Page curve for a Gap horizon has not been derived.

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

The following analogies are hypotheses about a possible horizon model.

| Approach | Mechanism | Gap analogue |
|--------|----------|------------|
| Complementarity (Susskind) | Two descriptions: inside and outside | Gap profile on the horizon encodes both |
| ER=EPR (Maldacena–Susskind) | Wormhole = entanglement | Non-local Gap correlations across the horizon |
| Firewall (AMPS) | Breakdown of smoothness at the horizon | $\text{Gap} \to 1$ — smooth limit, no wall |
| Island formula | Entropy computations with "islands" | Gap islands: regions $\text{Gap} \approx 0$ inside the horizon |

The proposed correspondences require an explicit spacetime solution and its quantum dynamics.

### 6.5 Evaporation Dynamics in the Gap Formalism

#### Theorem (Hawking temperature from the spectral action) [T] {#теорема-температура-хокинга}

:::tip Theorem (Hawking temperature from the spectral action) [T]
On a supplied asymptotically flat Schwarzschild background, semiclassical quantum field theory gives the Hawking temperature

$$
T_H = \frac{\hbar c^3}{8\pi G_N M k_B}, \quad G_N = \frac{3\pi}{7 f_2 \Lambda^2}
$$

Here the normalization of $G_N$ uses the prescribed spectral cutoff. The schematic evaporation rate involves the emitted species and their greybody factors.

$$
\frac{dM}{dt} = -\sigma_{\text{SB}} T_H^4 A_{\text{horizon}} \times \sum_s \Gamma_s
$$

The field species and their spins are supplied. Precise fluxes require integration over the frequency-dependent greybody factors.
:::

The usual Hawking temperature requires the chosen Schwarzschild solution and semiclassical fields. A Gap-specific evaporation calculation [Pr] would need a dynamical horizon, an emission channel and a relation between outgoing entropy and the proposed phase profile. Neither a Page time at a fixed opacity nor an endpoint with 42 remnant modes has been established.

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
8. **Gravitational dynamics.** Derive a physical metric and its spin-two kinetic term from microscopic dynamics. The linear Fierz–Pauli action and the nonlinear Einstein–Hilbert action used here are supplied.

:::

---

## Related Documents

- [Einstein equations](/docs/physics/gravity/einstein-equations) — variation of the supplied metric action
- [Emergent geometry](/docs/physics/gravity/emergent-geometry) — state distance, charge spectra and operational distance
- [Cosmological constant](/docs/physics/gravity/cosmological-constant) — conditions on a vacuum-energy readout
- [Supersymmetry](/docs/physics/particle-physics/susy) — additional field content
- [$G_2$-structure](/docs/physics/gauge-symmetry/g2-structure) — gauge symmetry
- [Noether charges](/docs/physics/gauge-symmetry/noether-charges) — Ward identities
- [Emergent manifold $M^4$](/docs/proofs/physics/emergent-manifold) — derivation of $M^4$ from categorical structure (T-117 — T-121)
- [$\Lambda$ budget](/docs/proofs/gap/lambda-budget) — 41.5 orders
- [Emergent time §11.5](/docs/proofs/dynamics/emergent-time#t-348) — the de Sitter observer algebra and the holon tower (T-348)
