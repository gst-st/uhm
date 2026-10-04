---
sidebar_position: 4
title: "Confinement"
---

# Confinement

:::note Scope of the confinement proposal [H/Pr]
A selected positive three-form and a selected unit vector have stabilizer $SU(3)$ [T]. Identifying it with physical colour, supplying a spacetime gauge connection and identifying density-state phases with that connection are additional field-model assumptions. Universal T-73 (Gap equals curvature) is withdrawn [✗]. The homotopy identity $\pi_2(G_2/T^2)=\mathbb Z^2$ classifies maps into that supplied homogeneous space; it neither creates a flux tube nor proves a Wilson-loop area law. The corrected invariant potential instead has the stated $S^6$ vacuum manifold with $\pi_2=0$.

The former topological area-law derivation and the claim of a derived 457 MeV tension are withdrawn [✗]. The numerical formulas below are conditional phenomenological ansätze [H] with independent couplings, sector values and physical scale. The standard QCD formulas retained later require the specified gauge/fermion content; deriving that content from UHM remains a separate question. Strong CP is open [Pr] (the earlier vanishing theorem was already retracted).
:::

## 1. Wilson Loop and Non-Perturbative Gap Dynamics

### 1.1 Supplied gauge data

Choose a spacetime, an $SU(3)$ bundle/connection and a field action [D/H]. The algebraic stabilizer $SU(3)_v\subset G_2$ is known after choosing $v$; it does not derive eight spacetime gauge fields or their dynamics from seven density coordinates. A relation $A_\mu^a\sim\partial_\mu\theta_{ij}$ would need a specified covariant map, gauge transformations and physical units. Zero numerical phase Gap does not imply flatness of such a connection.

### 1.2 Wilson loop for the supplied connection

For a representation and closed spacetime contour, define

$$
W(C)=\frac1{\dim R}\operatorname{Tr}_R\mathcal P\exp\oint_C A.
$$

Its expectation requires a field measure or quantum state. A single finite density matrix, its phase chart and its topological stabilizer do not supply that measure. Choosing an identification with a Gap field is a model hypothesis [H].

### 1.3 Area-law claim: former proof withdrawn [✗] {#теорема-закон-площади}

The old proof used three unavailable implications: numerical Gap as spacetime curvature (T-73 [✗]); nonzero $\pi_2$ as a flux-tube energy barrier; and a cubic finite-state potential as a linearly growing spatial source energy. None follows from the preceding matrix or group identities. A homotopy class needs a field configuration, boundary conditions and a target; a lower energy bound needs an energy functional on those fields. In particular a nontrivial $\pi_2$ alone gives neither a positive string tension nor suppression of quantum tunnelling.

A correct conditional connection is available **after** supplying a positive transfer matrix and nonzero ground-state overlap for a rectangular Wilson observable:

$$
\langle W(L,T)\rangle=\sum_n c_n(L)e^{-E_n(L)T},\quad c_n(L)\ge0,\quad c_0(L)>0.
$$

Then $-\lim_{T\to\infty}T^{-1}\log\langle W(L,T)\rangle=E_0(L)$ [T at these spectral hypotheses, after the chosen source-energy subtraction]. If one independently proves $E_0(L)=\sigma L+O(1)$ as $L\to\infty$, a leading area law follows in that order of limits [C]. Proving the linear ground-state energy is the confinement problem; writing that energy as $\sigma L$ is an ansatz, not its proof.

The old $\sqrt\sigma\simeq457$ MeV follows only from supplied phenomenological values in §2. A small Hessian eigenvalue describes local susceptibility; it does not determine a vacuum coherence without a covariance/noise law, nor a physical string tension without a gauge-field bridge. No universal factor 2.8 or 457 MeV is derived by T-64/T-73/T-74.

## 2. String Tension $\sigma$ from Gap Parameters

### 2.1 Theorem 1.2 (String tension from Gap parameters)

:::note Tension formulas are phenomenological [H]
The formulas below define a proposed model with supplied sector amplitudes, rates and physical scale. Evaluating them is arithmetic [T at these choices]; identifying them with QCD tension, independently fixing inputs and obtaining a gauge-field continuum limit remain unproved. They are not consequences of the withdrawn area-law proof.
:::

**(a)** Formula:

$$
\sigma = \frac{\lambda_3^2 \bar{A}^2}{\mu^2} \cdot \mu_{\mathrm{phys}}^2
$$

where $\mu_{\mathrm{phys}} = \mu \cdot \omega_0$ is the physical scale.

**(a')** A second chosen scaling is $\sigma\sim(\lambda_3|\varepsilon|/2)\mu_{\rm phys}^2$ [H]. The scale factor is needed for physical units if $\lambda_3,\varepsilon$ are dimensionless. It is independent of formula (a) until a matching relation is proved. Taking $\varepsilon\to0$ in this ansatz does not prove QCD deconfinement.

**(b)** At the chosen relation between parameters: $\lambda_3 = 2\mu^2/(3\bar{|\gamma|})$, $\bar{A} \sim \bar{|\gamma|}^3$, therefore:

$$
\sigma \sim \frac{4\mu^4 \bar{|\gamma|}^6}{9\bar{|\gamma|}^2 \mu^2} \cdot \mu_{\mathrm{phys}}^2 = \frac{4\mu^2 \bar{|\gamma|}^4}{9} \cdot \mu_{\mathrm{phys}}^2
$$

**(c)** Numerical estimate. $\sqrt{\sigma}_{\mathrm{exp}} \approx 440$ MeV (from lattice QCD computations). In Gap units:

$$
\sqrt{\sigma} = \frac{2\mu \bar{|\gamma|}^2}{3} \cdot \mu_{\mathrm{phys}}
$$

With parameters: $\mu^2 \approx 16.6$ $\to$ $\mu \approx 4.1$, $\bar{|\gamma|} \approx 0.047$, $\mu_{\mathrm{phys}} \approx 10$ GeV (QCD scale):

$$
\sqrt{\sigma} \approx \frac{2 \times 4.1 \times (0.047)^2}{3} \times 10 \approx \frac{2 \times 4.1 \times 0.0022}{3} \times 10 \approx 0.06 \text{ GeV}
$$

**(d)** Result $\sim 60$ MeV, experimental value $\sim 440$ MeV (factor $\sim 7$). Sources of the discrepancy:
- $\bar{|\gamma|}$ in the QCD vacuum may differ from the typical value
- Non-perturbative corrections to $\sigma$ (instanton configurations, §3)
- Necessity of a self-consistent determination of $\mu_{\mathrm{phys}}$ via $\Lambda_{\mathrm{QCD}}$

### 2.2 Hadron Spectrum

From the confinement mechanism it follows that observable hadrons are colourless Gap configurations:

**(a)** **Mesons:** $q$-$\bar{q}$ pair bound by a Gap tube in the 3-to-$\bar{3}$ sector. Meson mass $\sim \sqrt{\sigma} \cdot n$ (string excitations, $n = 0, 1, 2, \ldots$).

**(b)** **Baryons:** three quarks bound by a Y-shaped Gap tube. Three colour Gap tubes converge at a single point (baryon vertex).

**(c)** **Glueballs:** closed Gap tubes (loops in the 3-to-$\bar{3}$ sector) without quarks. Mass $\sim 2\sqrt{\sigma} \sim 1$ GeV.

### 2.3 What the numerical discrepancy establishes {#диагностика-расхождения-σ}

At fixed remaining inputs of formula (a), $\sqrt\sigma\propto|\bar\gamma|^2$. Thus replacing $0.047$ by $0.13$ multiplies the value by $(0.13/0.047)^2\simeq7.65$ [T]. A scenario value near 60 MeV then becomes roughly 459 MeV (rounding the older inputs led to 457 MeV). This is a sensitivity calculation; it does not derive the replacement amplitude or explain a physical discrepancy. Using an observed tension to select $0.13$ is fitting.

Nor can one infer a multiplicative factor eight simply from eight gluons: channel contributions and correlations depend on the action and flux solution. A soft Hessian mode does not set the mean coherence by itself. Independent vacuum/field/noise data and an out-of-sample tension prediction are required [Pr/H]. The former theorem that the numerical agreement follows from T-64 is withdrawn [✗].

## 3. Structural Resolution of the Strong CP Problem

### 3.0 Problem Statement {#постановка-сильного-cp}

In the Standard Model the QCD Lagrangian allows a $\theta$-term:

$$
\mathcal{L}_\theta = \frac{\theta_{\mathrm{QCD}}}{32\pi^2}\, G_{\mu\nu}^a \tilde{G}^{a,\mu\nu}
$$

Experimental bound from the neutron electric dipole moment (nEDM): $|\theta_{\mathrm{QCD}}| < 10^{-10}$ (PSI 2020). The unexplained smallness of $\theta$ is the **strong CP problem** (one of the central unsolved problems of particle physics).

Three standard approaches: (1) Peccei–Quinn axion (dynamical relaxation), (2) massless $u$-quark (excluded by mass data), (3) fine-tuning (inelegant).

**Gap approach:** $\theta_{\mathrm{QCD}} = 0$ **exactly** — a structural consequence of the octonionic algebra. No axion required for CP, no fine-tuning. This is a genuine prediction of the theory, distinguishing it from standard approaches. *(Status since 2026-09-25: [C at (SV)] through the $V_3$ chain only; the route through the symmetry of the corrected vacuum is closed by T-333, §3.1a.)*

:::warning[Retracted 2026-09-26 (T-99): $\theta_{\mathrm{QCD}} = 0$ is not a prediction of UHM]
The paragraph above is kept as the former claim. The $V_3$ chain fails at step 4 for $V_3$ itself, at every value of the sector moduli, so (SV) cannot rescue it; the corrected potential is PT-even and fixes no $\bar\theta$; and with the fields that (Cl) forces none of the three standard routes is available (§3.1a–§3.1b). $\bar\theta$ is a free parameter of UHM, bounded only by experiment, and the strong CP problem is open [Pr] — [§3.1c](#тета-не-из-потенциала).
:::

### 3.1 Theorem T-99 (Structural vanishing of $\theta_{\mathrm{QCD}}$) — former derivation, retracted [✗] 2026-09-26 {#теорема-структурное-theta-qcd}

:::warning[Correction 2026-09-26 (T-99): the conclusion is retracted, not conditional]
Until today the conclusion stood as [C at (SV)] (heading: [T]+[C at (SV)]). It is retracted [✗], because step 4 is false for the potential it uses, and (SV) — the sector *moduli* of the vacuum — does not touch that step. On every real $\Gamma$ (all $\theta_{ij} \in \{0,\pi\}$) the page's $V_2 + V_3 + V_4$ vanishes identically ($\mathcal G_{\text{total}} = \lVert\mathrm{Im}\,\Gamma\rVert^2 = 0$, $V_3 = 0$), while the first variation of $V_3$ in a direction $iX$ is non-zero (0.028 on the witness state). So for every $\lambda_3 \neq 0$ a small imaginary shift lowers $V$ below zero, and no vacuum has all phases zero. Minimising over all states: at the page's constants $\lambda_3/\mu^2 = 9.25$, $\lambda_4/\mu^2 = 32.2$ the minimum is $V = -0.197\mu^2$ with $\mathcal G_{\text{total}} = 0.0155$; at $\lambda_3/\mu^2 = 0.01$, $\lambda_4/\mu^2 = 10$ it is $-2.3\times10^{-6}\mu^2$ with $\mathcal G_{\text{total}} = 2.4\times10^{-6}$. A PT-odd term is minimised at phases away from zero; it does not set them to zero. Step 5 has no ground in the Clifford content either: there $\bar\theta = \theta + \arg\det(M_uM_d)$ with $M_{u,d}$ from Yukawa inputs (T-333(h)), not from $\lambda_3$ and moduli of Gap coherences. What holds instead, and the list of routes tried, is [§3.1c](#тета-не-из-потенциала). Witness: `test_theta_route_through_the_gap_potential_fails_for_v3_and_for_pt_odd_quartics`. The text below is the former derivation.
:::

:::tip[Status: \[T\] for step 2, \[C at (SV)\] for the conclusion (T-99, stratified 2026-09-25)]
Step 2 ($V_3$ is the only $PT$-odd term of $V_{\text{Gap}}$) is exact for the retracted cubic $V_3$; the $G_2$-invariant potential has no $PT$-odd term (T-331). The conclusion uses the unique sector vacuum, which is the hypothesis (SV): the corrected T-64 gives a different vacuum. So $\theta_{\mathrm{QCD}} = 0$ is conditional on (SV). Earlier summary: 7-step derivation of $\theta_{\mathrm{QCD}} = 0$ from axioms A1–A5. Reality of $f_{ijk} \in \mathbb{R}$ (A1) → uniqueness of the PT-odd $V_3$ → unique vacuum (T-64) → isotropy of phases → $\theta = 0$ exactly. Non-perturbative stability from T-69, radiative from T-66.
:::

**Theorem.** In the Gap formalism $\theta_{\mathrm{QCD}} = 0$ **exactly** (not approximately). Proof in 7 steps:

**Step 1** (Reality of structure constants). Axiom A1 (septicity) fixes the inner space $\mathrm{Im}(\mathbb{O}) \cong \mathbb{R}^7$. The octonionic structure constants $f_{ijk} \in \{0, \pm 1\} \subset \mathbb{R}$ are defined by the Fano plane $\mathrm{PG}(2,2)$. All coefficients of the potential $V_{\mathrm{Gap}}$ are real. Cross-references: [Septicity axiom](/docs/core/foundations/axiom-septicity), [Fano selection rules](/docs/physics/gauge-symmetry/fano-selection-rules#теорема-фано-отбор-fijk).

**Step 2** (Uniqueness of the PT-odd potential). The potential $V_{\mathrm{Gap}}$ contains three terms: $V_2$, $V_3$, $V_4$. Of these:

- $V_2 = \mu^2 \sum_{i < j} |\gamma_{ij}|^2 (1 - \cos 2\theta_{ij})$ — **PT-even** (depends on $\cos\theta$, invariant under $\theta \to -\theta$).
- $V_4 = \lambda_4 \sum |\gamma_{ij}|^4$ — **PT-even** (depends only on moduli).
- $V_3 = \lambda_3 \sum_{(i,j,k) \notin \mathrm{Fano}} |\gamma_{ij}||\gamma_{jk}||\gamma_{ik}| \sin(\theta_{ij} + \theta_{jk} - \theta_{ik})$ — the **unique PT-odd** term ($\sin$ changes sign under $T$-reversal).

Consequently, $V_3$ is the **unique** source of phase dependence in the potential. Cross-reference: [Gap thermodynamics](/docs/core/dynamics/gap-thermodynamics).

:::warning What the corrected potential gives instead (2026-09-25, T-331, T-64)
Step 2 is a property of the retracted cubic $V_3$ only. Every $G_2$-invariant cubic is PT-even ([T-331](/docs/core/dynamics/gap-thermodynamics#g2-инвариантный-кубик) [T]), so the corrected potential $V_{\text{Gap}} = \mu^2\mathcal G + \lambda_4\mathcal G^2 - \kappa\mathcal A$ has no PT-odd term at all, and step 4 ("$V_3$ fixes all phases") has nothing to act with. What the corrected potential does give is a vacuum with an unbroken antiunitary symmetry: $I/7$ is PT-invariant ([T] for $0 < \kappa \le \mu^2/48$), and the colour-invariant vacuum $\Gamma_v$ of the Gap phase is invariant under $g_v\circ\mathrm{PT}$ with $g_v \in G_2$, $g_vv = -v$ ([T], [T-64](/docs/core/dynamics/gap-thermodynamics#теорема-глобальная-минимизация)). Turning this into $\theta_{\mathrm{QCD}} = 0$ needs one more step, and it is the precise obstruction: the antiunitary symmetry must be identified with CP of the colour sector, and $\theta_{\mathrm{QCD}}$ of step 5 is the phase of $\det(M_uM_d)$, which requires the quark mass matrices — the Yukawa structure, which is open ([standard model, Theorem 2.6(f)](/docs/physics/gauge-symmetry/standard-model#поколение-t329)). Until it is closed, $\theta_{\mathrm{QCD}} = 0$ stays [C at (SV)].

*Resolved negatively (T-333, [§3.1a](#pt-на-фермионах-t341)):* with the Yukawa couplings classified (T-332), no lift of this antiunitary symmetry to the fermions can give $\bar\theta = 0$ while keeping $m_t \neq m_b$ and the observed CKM phase. The route through the vacuum symmetry is closed [✗]. $\theta_{\mathrm{QCD}} = 0$ keeps only the $V_3$ chain of steps 3–5, [C at (SV)], and the $G_2$-invariant potential no longer contains $V_3$.
:::

**Step 3** (Uniqueness of the vacuum). From T-64 [T] (corrected to the $G_2$-invariant potential; its vacuum has no sector values — hypothesis (SV)) ([global minimisation of $V_{\mathrm{Gap}}$](/docs/core/dynamics/gap-thermodynamics#теорема-глобальная-минимизация)): $G_2$-orbital reduction $21D \to 5D$ leads to a **unique** global minimum with positive-definite Hessian ($\mathrm{Hess}(V_{\mathrm{Gap}})|_{\min} > 0$). The vacuum is uniquely determined.

**Step 4** (Isotropy of phases at the minimum). At the minimum of $V_{\mathrm{Gap}}$:

- From $V_2$: $\sin^2\theta_{ij}$ is minimised at $\theta_{ij} = 0$ or $\pi$ for all $(i,j) \in 3\text{-to-}\bar{3}$.
- From $V_3$: for Fano triplets $\sin(\theta_{ij} + \theta_{jk} - \theta_{ik})$ is minimised at $\theta_{ij} = \theta_{jk} = \theta_{ik} = 0$ (not $\pi$, which increases $V_3$).
- Hessian: eigenvalue $\lambda_1 = 18\mu^2 > 0$ confirms that $\theta_{ij} = 0 \;\forall (i,j) \in 3\text{-to-}\bar{3}$ is a **stable** minimum.

Conclusion: **all phases vanish** in the vacuum.

*Refuted 2026-09-26 [✗]:* $\sin$ is not minimised at $0$; real states are not even stationary points of $V_2 + V_3 + V_4$ when $\lambda_3 \neq 0$, and the vacuum has $\mathcal G_{\text{total}} > 0$ (box at the head of §3.1).

**Step 5** (Vanishing of $\theta_{\mathrm{QCD}}$). The parameter $\theta_{\mathrm{QCD}}$ in the Gap formalism:

$$
\theta_{\mathrm{QCD}} = \arg\left(\det(M_u \cdot M_d)\right) = \arg\left(\lambda_3^2 \cdot \prod_{(i,j) \in 3\text{-to-}\bar{3}} |\gamma_{ij}|\right)
$$

From steps 1–4: $\lambda_3 \in \mathbb{R}$ (step 1), $|\gamma_{ij}| \in \mathbb{R}_+$ (moduli are real), all phases $\theta_{ij} = 0$ (step 4). Consequently, the argument of the product of real positive numbers is **identically zero**:

$$
\theta_{\mathrm{QCD}} = 0 \quad \text{(exactly, not approximately)}
$$

*Retracted 2026-09-26 [✗]:* the formula identifies the quark mass matrices with $\lambda_3$ and the moduli of Gap coherences; with the fields that (Cl) forces the quark masses come from Yukawa couplings whose phases are inputs (T-333(h)), and the $\theta$ of the gauge action enters $\bar\theta$ on its own.

**Step 6** (Non-perturbative stability). From T-69 [T] ([topological protection](/docs/core/dynamics/composite-systems#теорема-тополог-защита)): $\pi_2(G_2/T^2) \cong \mathbb{Z}^2$ guarantees **topological stability** of the vacuum. Energy barrier:

$$
\Delta V \geq 6\mu^2 > 0
$$

Instanton configurations (§3.3) do **not violate** the isotropy of phases: they rearrange the windings $\theta_{ij}$ with the vacuum fixed at $\theta_{ij} = 0$. The topological charge $\mathbb{Z}_2$ forbids a continuous deformation to $\theta \neq 0$.

**Step 7** (Radiative stability). From T-66 ([UV finiteness](/docs/physics/gravity/quantum-gravity#теорема-уф-конечность): field-space [T], order-by-order [C]): radiative corrections preserve $G_2$-symmetry. The coefficient $\lambda_3$ runs under RG but **remains real** (RG preserves the reality of coefficients of a real potential). Phase isotropy $\theta_{ij} = 0$ is a property of the minimum, not violated by loop corrections.

$\blacksquare$

### 3.1a The vacuum's antiunitary symmetry on the fermions (T-333) {#pt-на-фермионах-t341}

:::tip[Status: Theorem 3.1a is \[T\] as mathematics and \[C at (Cl)\] in UHM; the comparison with the data uses the measured $m_t/m_b$ and $J$]
The corrected vacuum keeps an antiunitary symmetry: $\mathrm{PT}$ at $I/7$, $\Theta_v = g_v\circ\mathrm{PT}$ on the orbit $S^6$. The box after step 2 asked whether this symmetry acts as CP on quarks once the Yukawa structure is fixed. It does not, in any lift that the data allow. Registry row T-333; checks in `website/scripts/check_core_numbers.py`.
:::

**Theorem 3.1a (T-333).**

**(a) The lifts [T].** On $\mathbb C^7$, $\mathrm{PT}$ is complex conjugation, which on $\mathcal S = \mathbb C\otimes\mathbb O$ is $J = \gamma_8$, a Clifford generator in the charged directions of the Higgs plane. Take $g_v \in G_2$ of order 2, the identity on a quaternionic line not through $e_O$ and $-1$ on its complement, so $g_ve_O = -e_O$. Then $\Theta_v = g_vJ$ keeps the vacuum $\Gamma_v$ of T-64, and $\mathrm{PT}$ alone does not. On $\mathcal S_{\mathbb C} = \mathcal S\otimes\mathbb C'$ each has a $\mathbb C'$-linear lift ($\otimes 1$) and a $\mathbb C'$-antilinear lift ($\otimes K'$):

| lift | field unit $\omega$ | halves $V_L$, $V_R$ | on the vector $\mathbb R^{10}$ | type |
|---|---|---|---|---|
| $J\otimes1$ | commutes | kept | rotation, det $+1$ | element of $\mathrm{Spin}(10)$ |
| $\Theta_v\otimes1$ | commutes | exchanged; $\mathfrak{su}(2)_L\to\mathfrak{su}(2)_R$ | rotation, det $+1$; fixes $\gamma_{10}$, $iL_{e_O}$ | element of $\mathrm{Spin}(10)$, left–right exchange |
| $J\otimes K'$ | anticommutes | exchanged | reflection, det $-1$ | P-type |
| $\Theta_v\otimes K'$ | anticommutes | kept; normalises $\mathfrak g_{\mathrm{SM}}$ | reflection; fixes $iL_{e_O}$, reverses $\gamma_{10}$ | CP-type |

**(b) The linear lifts do not act on $\theta$ [T].** $J\otimes1$ and $\Theta_v\otimes1$ are unitary internal transformations of the $\mathbf{16}$ in the connected group $\mathrm{Spin}(10)$. They leave the $\theta$-term unchanged, so they cannot set $\theta = 0$. The canonical lift of an operator on $\mathcal S$ is the $\mathbb C'$-linear one, so the canonical action of the vacuum's symmetry on fermions is a gauge-group element, not CP.

**(c) Exchanging lifts force $m_t = m_b$ [T].** $J\otimes K'$ and $\Theta_v\otimes1$ map $\mathfrak g_{\mathrm{SM}}$ to its mirror. Together with $\mathfrak g_{\mathrm{SM}}$ the mirror generates the left–right algebra $\mathfrak{su}(3)\oplus\mathfrak{su}(2)_L\oplus\mathfrak{su}(2)_R\oplus\mathfrak u(1)_{B-L}$ (dimension 15). A Yukawa coupling invariant under $G_{\mathrm{SM}}$ and under such a lift is therefore left–right equivariant. With the one real doublet, [T-332(b)](/docs/physics/particle-physics/higgs-sector#юкавы-t340) then gives $\lvert m_u\rvert = \lvert m_d\rvert$ and $\lvert m_\nu\rvert = \lvert m_e\rvert$, refuted by $y_t/y_b \approx 68$.

**(d) The CP-type lift forces $J = 0$ [T].** Suppose $\Theta_v\otimes K'$, combined with any unitary action on the families (a generalised CP), is an unbroken symmetry of the quark Yukawa couplings. Then every CP-odd weak-basis invariant vanishes: $\bar\theta$, and also the Jarlskog invariant (Bernabéu, Branco and Gronau, *Phys. Lett. B* **169**, 243 (1986)). The measured value is $J = (3.12^{+0.13}_{-0.12})\times10^{-5}$ (PDG 2024, CKM review, §12).

So under (Cl) with one doublet, no lift of the vacuum's antiunitary symmetry makes $\bar\theta = 0$ while keeping $m_t \neq m_b$ and $J \neq 0$. Fixing the Yukawa structure resolves the obstruction named after step 2, and negatively: the route "vacuum symmetry → $\theta = 0$" is closed [✗]. Three routes survive, each as a hypothesis [H]. (i) Left–right parity with a complex bidoublet (two doublets, against T-296), Hermitian Yukawa matrices and relatively real vacuum values. Hermitian mass matrices have a real determinant and can still carry $J \neq 0$ (Babu and Mohapatra, *Phys. Rev. D* **41**, 1286 (1990)). (ii) Spontaneous CP violation of Nelson–Barr type, which the corpus does not contain. (iii) A Peccei–Quinn axion, with the Gap axion of §3.2 then required to relax $\theta$. With the corrected potential PT-even (T-331), the Gap sector has no source of CP violation at all. The CKM phase must be an input of the Yukawa sector, so §3.3(b) no longer holds for the corrected potential.

**Proof.** (a) The table is computed: each lift is tested against $\omega$ and against the volume $\omega_4$ of the colour-free plane, and conjugation by it is expanded in the ten Clifford vectors. The rotation and its determinant are read off from that expansion. The images of $\mathfrak{su}(2)_L$ and $\mathfrak g_{\mathrm{SM}}$ are computed. (b) Elements of a connected gauge group preserve $\int G\tilde G$. (c) The Lie closure is computed. If $Y$ is equivariant under $G$ and under $T$, it is equivariant under $TGT^{-1}$ and hence under the group they generate. (d) This is the cited theorem; it is checked on random generalised-CP-invariant Yukawa matrices, $\lvert J\rvert < 10^{-12}$. Hermitian ones give $\mathrm{Im}\det M_uM_d = 0$ with $\lvert J\rvert > 10^{-3}$. $\blacksquare$

Witnesses: `test_vacuum_antiunitary_lifts_are_gauge_parity_or_cp`, `test_an_unbroken_cp_or_lr_symmetry_contradicts_the_quark_data`.

### 3.1b Peccei–Quinn and Nelson–Barr in the Clifford content (T-333, continued) {#пк-и-нб}

:::tip[Status: Theorem 3.1b is \[T\] as mathematics and \[C at (Cl)\] in UHM; with the fields that (Cl) forces, $\bar\theta$ is a free parameter and the strong CP problem is open in UHM \[Pr\]]
T-333 left three routes to $\bar\theta=0$: left–right parity with two doublets, Nelson–Barr, and an axion. This section tests the last two against the fields that the Clifford frame forces — three generations of the $\mathbf{16}$ ([T-329](/docs/physics/gauge-symmetry/standard-model#поколение-t329)) and one doublet in the colour-free plane — and checks the axion of the dark-matter page. Registry row T-333, items (e)–(h); checks in `website/scripts/check_core_numbers.py`.
:::

**Theorem 3.1b (T-333(e)–(h)).**

**(e) No Peccei–Quinn symmetry [T].** Let $Y_u$ and $Y_d$ be the $3\times3$ matrices of $Q\tilde Hu^c$ and $QHd^c$, with $\det Y_u\neq0$ and $\det Y_d\neq0$. Every phase rotation of $Q_i$, $u^c_i$, $d^c_i$ and $H$ that keeps all their non-zero entries has zero colour anomaly, $\sum_i(2q_{Q_i}+q_{u_i}+q_{d_i})=0$. All six quarks are massive ($m_u\approx2.2$ MeV, PDG), so the Clifford content with one doublet has no Peccei–Quinn symmetry and no axion. In one generation this is [T-332(i)](/docs/physics/particle-physics/higgs-sector#голоморфность-вп): a coupling with $\lvert\beta\rvert\neq\lvert\alpha\rvert$ keeps only hypercharge, $B$ and $L$. A colour-anomalous phase appears only at $\beta=\pm\alpha$, where a whole charge type is massless. That is the massless-quark solution, which the data exclude.

**(f) What an axion needs [T for the statement].** A colour-anomalous $\mathrm{U}(1)$ that survives the quark masses needs new fields of one of two kinds. The first kind is a second doublet, so that $Q\tilde H_uu^c$ and $QH_dd^c$ carry independent phases (Peccei and Quinn, *Phys. Rev. Lett.* **38**, 1440 (1977)). With $f_a=v$ this is the Weinberg–Wilczek axion (*Phys. Rev. Lett.* **40**, 223 and 279 (1978)), long excluded. The invisible version adds a singlet with $f_a\gg v$ (Dine, Fischler and Srednicki, *Phys. Lett. B* **104**, 199 (1981); Zhitnitsky, *Sov. J. Nucl. Phys.* **31**, 260 (1980)). The second kind is new coloured fermions whose mass comes from a singlet (Kim, *Phys. Rev. Lett.* **43**, 103 (1979); Shifman, Vainshtein and Zakharov, *Nucl. Phys. B* **166**, 493 (1980)). The first kind is the complex bidoublet of [T-332(c)](/docs/physics/particle-physics/higgs-sector#юкавы-t340), against T-296. The second is not in $\mathcal S_{\mathbb C}$: its 32 real components are one chiral $\mathbf{16}$, forced by T-329, and the hypercharges of its coloured states are not closed under a change of sign.

**(g) The Gap axion is not a QCD axion in this content [T for the implication].** The [dark-matter page](/docs/physics/cosmology-phys/dark-matter#3-qcd-аксион-из-компактификации-s121) defines the axion as a zero mode of Gap phases "possessing an axial anomaly with QCD". A coupling to $G\tilde G$ through an anomaly is the anomaly of a fermion current, so by (e) no Gap phase acquires one in the Clifford content. The mass formula $m_a\propto m_\pi f_\pi/f_a$ also needs the potential of $a$ to come from QCD alone. The same page (§3.5) gives all 21 phases a mass from $V_{\mathrm{Gap}}$, with no flat direction. A QCD axion needs the non-QCD part of its potential below about $10^{-10}\chi_{\mathrm{top}}$, where $\chi_{\mathrm{top}}^{1/4}\approx75.6$ MeV (Borsanyi *et al.*, *Nature* **539**, 69 (2016)). The arithmetic of the page is right: $f_a=2\times10^{15}$ GeV gives $m_a=2.9$ neV. Its relic estimate takes $\theta_i=H_I/(2\pi f_a)$, a pure inflationary fluctuation around $\theta=0$. The axion density is then an isocurvature mode with relative amplitude of order one. The Planck limit on uncorrelated dark-matter isocurvature (Planck Collaboration, *Astron. Astrophys.* **641**, A10 (2020)), taken as $\beta_{\mathrm{iso}}<0.038$, allows $\Omega_a/\Omega_c\lesssim3\times10^{-5}$ with the relative power $4/N$ at $N=60$ e-folds, not $10^{-2}$.

**(h) No spontaneous CP violation, so no Nelson–Barr [T].** Nelson–Barr (Nelson, *Phys. Lett. B* **136**, 387 (1984); Barr, *Phys. Rev. Lett.* **53**, 329 (1984)) keeps CP exact in the Lagrangian, so that $\theta=0$ there. It breaks CP only by complex vacuum values of heavy singlets that couple the light quarks to vector-like heavy quarks. The Clifford content has none of this. (1) It has no vector-like quark, by (f). (2) The Gap vacuum does not break CP. It is invariant under the CP-type lift $\Theta_v\otimes K'$ ([T-333](#pt-на-фермионах-t341)), which fixes $iL_{e_O}$ and reverses $\gamma_{10}$. Hypercharge rotates the neutral plane of the Higgs ([T-332(h)](/docs/physics/particle-physics/higgs-sector#голоморфность-вп)) and acts on $\mathcal S$ as $(B-L)/2$, which commutes with $\Gamma_v$. So a hypercharge rotation composed with $\Theta_v\otimes K'$ fixes both $\Gamma_v$ and any neutral Higgs vacuum value. CP is broken spontaneously only when no generalised CP leaves the vacuum invariant (Branco, Lavoura and Silva, *CP Violation*, Oxford University Press (1999)). If CP were exact in the Lagrangian it would therefore stay unbroken, and T-333(d) would give $J=0$, against $J=3.12\times10^{-5}$. So CP must be broken explicitly in the Yukawa couplings, and then nothing protects $\theta$.

So under (Cl) none of the three routes of T-333 is open without a field that the frame does not contain. Parity needs a second doublet. Nelson–Barr needs vector-like quarks and a CP-breaking singlet. An axion needs a second doublet and a singlet, or new coloured fermions. With the forced content $\bar\theta$ is a free parameter of the Yukawa sector, and the strong CP problem is open in UHM [Pr]. Each extension is falsifiable: a charged Higgs (parity, DFSZ), a vector-like quark (Nelson–Barr, KSVZ), or an axion signal.

**Proof.** (e) If $\det Y_u\neq0$, some permutation $\sigma$ has $(Y_u)_{i\sigma(i)}\neq0$ for every $i$. Invariance of those entries gives $q_{Q_i}-q_H+q_{u_{\sigma(i)}}=0$, so $\sum q_u=-\sum q_Q+3q_H$. In the same way $\sum q_d=-\sum q_Q-3q_H$, and the sum gives the claim. It is checked on 300 random supports with non-singular matrices. (f) The hypercharges of the coloured states of $\mathcal S_{\mathbb C}$ are computed. (g) The numbers use $m_u=2.16$ MeV, $m_d=4.67$ MeV, $m_\pi=135$ MeV, $f_\pi=92$ MeV, $A_s=2.1\times10^{-9}$ and $r<0.036$, which give $H_I/(2\pi f_a)=3.7\times10^{-3}$ as on the dark-matter page. (h) $\Gamma_v$, extended to $\mathcal S$, commutes with $(B-L)/2$ (computed). The rest is T-333 and the cited criterion. $\blacksquare$

Witness: `test_no_peccei_quinn_symmetry_in_the_clifford_content`.

### 3.1c What the Gap potential says about $\bar\theta$ (T-99, corrected) {#тета-не-из-потенциала}

:::tip[Status: Theorem 3.1c is \[T\] as mathematics and \[C at (Cl)\] in UHM; $\theta_{\mathrm{QCD}} = 0$ is not derived, strong CP is open \[Pr\] (2026-09-26)]
This replaces the conclusion of T-99. T-99 set out to show that the Gap sector makes $\bar\theta$ vanish. The true statement is weaker and exact: the Gap sector is CP-neutral, and no term of a $G_2$-invariant Gap potential can make $\bar\theta$ vanish. Registry row T-99; checks in `website/scripts/check_core_numbers.py`.
:::

**Theorem 3.1c (T-99, corrected).**

**(a) The corrected Gap sector is CP-neutral [T].** Every $G_2$-invariant polynomial of degree $\le 3$ on $\mathrm{Herm}(\mathbb C^7)$ is PT-even ([T-331](/docs/core/dynamics/gap-thermodynamics#g2-инвариантный-кубик)), so $V_{\text{Gap}} = \mu^2\mathcal G + \lambda_4\mathcal G^2 - \kappa\mathcal A$ is PT-invariant. Each of its vacua keeps an antiunitary symmetry: $\mathrm{PT}$ at $I/7$, $g_v\circ\mathrm{PT}$ on the orbit $S^6$ ([T-64](/docs/core/dynamics/gap-thermodynamics#теорема-глобальная-минимизация)). The Gap sector carries no CP-odd phase of its own.

**(b) CP-neutrality does not reach $\bar\theta$ [T].** The canonical lift of that symmetry to the fermions is an element of $\mathrm{Spin}(10)$ and leaves the $\theta$-term unchanged; the lifts that act as P or CP contradict $m_t \neq m_b$ or $J \neq 0$ ([§3.1a](#pt-на-фермионах-t341)). With one doublet and three $\mathbf{16}$ CP must be broken explicitly in the Yukawa couplings, and then nothing protects $\bar\theta = \theta + \arg\det(M_uM_d)$ ([§3.1b](#пк-и-нб)).

**(c) A PT-odd Gap term is a source of phases, not a guard [T].** The first PT-odd $G_2$-invariants appear in degree 4. There are three (T-331), of types $SX_{\mathbf 7}^2X_{\mathbf{14}}$, $SX_{\mathbf 7}X_{\mathbf{14}}^2$ and $S^3X_{\mathbf 7}$, where $S$ is the traceless part of $\mathrm{Re}\,\Gamma$ and $X = \mathrm{Im}\,\Gamma$. The last one is $Q_{\rm odd} = \langle \varphi\cdot X, \varphi\cdot(NS)\rangle$ with $N_{pq} = \varphi_{pab}S_{ac}S_{bd}\varphi_{qcd}$. A potential containing any PT-odd term is invariant under no $g\circ\mathrm{PT}$ with $g \in G_2$, since $f(g\bar\Gamma g^{-1}) = f(\bar\Gamma) = -f(\Gamma)$. $Q_{\rm odd}$ is linear in $X$; on a real state with $S \neq 0$ its first variation in $\mathrm{Im}\,\Gamma$ is non-zero (0.0019 on the witness state). So $\mu^2\mathcal G + \lambda_4\mathcal G^2 + \varepsilon Q_{\rm odd}$ goes below zero off the real states (minimum $-0.0042\mu^2$ with $\mathcal G = 0.0034$ at $\varepsilon = 0.5\mu^2$, $\lambda_4 = 10\mu^2$). The cubic $V_3$ of the former derivation behaves the same way (box at the head of §3.1).

**(d) Consequence.** In UHM with the fields that (Cl) forces, $\bar\theta$ is a free parameter, fixed by no axiom, no Gap potential and no symmetry of the vacuum. UHM predicts no value of the neutron EDM; the bound $\lvert\bar\theta\rvert \lesssim 10^{-10}$ is an input. The strong CP problem is open in UHM [Pr].

**Routes tried before the retraction.**

| route | outcome | where |
|---|---|---|
| $V_3$ chain of T-99 under (SV) | step 4 false for every $\lambda_3 \neq 0$; (SV) fixes moduli, not phases | box at the head of §3.1 |
| antiunitary symmetry of the corrected vacuum | the linear lift is a gauge element; P- or CP-type lifts give $m_t = m_b$ or $J = 0$ | §3.1a, T-333(a)–(d) |
| PT-odd $G_2$-invariant quartics | break every $g\circ\mathrm{PT}$; move the vacuum off the real states | (c) above |
| Peccei–Quinn axion | no colour-anomalous $\mathrm U(1)$ with all quarks massive; needs a second doublet or new coloured fermions | §3.1b(e)–(g) |
| Nelson–Barr | no vector-like quark, no spontaneous CP violation | §3.1b(h) |
| left–right parity | needs a complex bidoublet (two doublets, against T-296) | §3.1a, T-332(c) |
| massless $u$ quark | $m_u = 2.16$ MeV (PDG) | §3.1b(e) |

**Proof.** (a) is T-331 with T-64. (b) is T-333. (c): invariance under $G_2$ and the sign under PT are computed on random states; the first variation at a real state is linear in $X$ and is evaluated directly, and a shift $R \to R + itX$ with the sign of $t$ opposite to it lowers $V$ below its value $0$ on the real states. (d) follows from (a)–(c) and T-333(e)–(h). $\blacksquare$

Witness: `test_theta_route_through_the_gap_potential_fails_for_v3_and_for_pt_odd_quartics`.

### 3.2 Corollary: Axion without PQ Mechanism {#следствие-аксион-без-pq}

:::info[Reinterpretation of the axion's role]
In standard physics the Peccei–Quinn axion solves the strong CP problem via dynamical relaxation $\theta \to 0$. In the Gap formalism $\theta_{\mathrm{QCD}} = 0$ follows **structurally** (T-99), so an axion is **not needed** for CP. Its role is purely as a DM candidate.
*Conditional (2026-09-25):* this holds only through the $V_3$ chain of T-99, [C at (SV)]. The route through the vacuum's antiunitary symmetry is closed (T-333), and a Peccei–Quinn axion is one of the three routes left open. *Update (T-333(e)–(h), [§3.1b](#пк-и-нб)):* in the Clifford content no $\mathrm{U}(1)$ with a colour anomaly survives the quark masses, so the Gap axion has no $G\tilde G$ coupling there. It is not a QCD axion and relaxes nothing. The table below describes it only on the hypothesis (PQ) of an added Peccei–Quinn sector.
*Update 2026-09-26 (T-99 corrected, [§3.1c](#тета-не-из-потенциала)):* the $V_3$ chain is retracted [✗] as well, so the premise of this box — "$\theta_{\mathrm{QCD}} = 0$ follows structurally" — no longer holds; strong CP is open [Pr].
:::

The Gap axion (§3.4, definition in [dark matter, §3.1](/docs/physics/cosmology-phys/dark-matter#31-определение)) — a pseudoscalar field $a(x)$, the zero mode of phases $\theta_{ij}$ in the 3-to-$\bar{3}$ sector — **exists** as a particle (Goldstone boson from the $(S^1)^{21}$ compactification). But its role is **fundamentally different**:

| | Standard axion | Gap axion |
|---|---|---|
| Solves strong CP? | Yes (dynamical relaxation) | **No** (T-99: $\theta = 0$ structurally — retracted 2026-09-26; strong CP open [Pr], §3.1c) |
| DM candidate? | Yes ($\sim 100\%$ at $f_a \sim 10^{12}$ GeV) | Yes, **subdominant** ($\sim 1\%$ DM) |
| Mass | $m_a \sim 10^{-5}$ eV | $m_a \sim 3$ neV (from $f_a \sim 2 \times 10^{15}$ GeV) |
| $f_a$ | Free parameter | **Fixed**: $f_a = \varepsilon \cdot M_P$ |

Cross-reference: [dark matter from Gap, §3](/docs/physics/cosmology-phys/dark-matter#3-qcd-аксион-из-компактификации-s121).

### 3.3 Corollary: Dual Role of $V_3$ {#следствие-двойная-роль-v3}

The cubic potential $V_3$ (octonionic associator) plays a **dual role**:

**(a)** Cause of $\theta_{\mathrm{QCD}} = 0$ (as argued with the retracted cubic; see the box after step 2 of T-99). $V_3$ is the unique PT-odd term of the potential. At the minimum of $V_{\mathrm{Gap}}$ it fixes **all** phases to $\theta_{ij} = 0$, making $\theta_{\mathrm{QCD}} = 0$ a structural result (T-99, steps 2 and 4). *Retracted [✗] 2026-09-26:* a PT-odd term does not fix the phases at zero; the vacuum of $V_2 + V_3 + V_4$ has $\mathcal G_{\text{total}} > 0$ ([§3.1c](#тета-не-из-потенциала)).

**(b)** Unique source of CP violation in CKM. *(For the retracted $V_3$ only: the $G_2$-invariant potential is PT-even (T-331) and contains no source of CP violation, so the CKM phase is an input of the Yukawa sector, T-333.)* The same $V_3$ generates complex phases in the Yukawa matrices $Y^u$, $Y^d$ via generation mixing, giving a non-zero phase $\delta_{\mathrm{CP}} \neq 0$ in the CKM matrix.

This explains the **CP paradox**: why strong CP violation is **zero** ($\theta_{\mathrm{QCD}} = 0$), while weak CP violation is **non-zero** ($\delta_{\mathrm{CP}} \approx 64.6°$). Answer: $V_3$ sets the **vacuum phases** to zero ($\theta_{ij} = 0$), but generates **inter-generational** phases via loop corrections. Cross-reference: [CKM matrix, §4](/docs/physics/particle-physics/ckm-matrix#4-фаза-cp-нарушения).

### 3.4 Gap Instantons and the $\theta$-Vacuum {#gap-инстантоны}

**(a)** Topology: $\pi_3(\mathrm{SU}(3)) = \mathbb{Z}$. An instanton is a map $S^3 \to \mathrm{SU}(3)$ with non-zero winding number $n$.

**(b)** Gap instanton. In Gap language: an instanton is a configuration $\theta_{ij}(x)$ in the 3-to-$\bar{3}$ sector in which all 8 phases complete a full rotation from 0 to $2\pi$ upon traversal of a three-dimensional sphere in spatial coordinates.

**(c)** Instanton action:

$$
S_{\mathrm{inst}} = \frac{8\pi^2}{g_s^2} = \frac{8\pi^2}{4\pi\,\alpha_s} = \frac{2\pi}{\alpha_s}
$$

In Gap parameters: $\alpha_s = g_s^2/(4\pi)$ is determined via the Gap coupling constant in the 3-to-$\bar{3}$ sector. From the relation $g_s \sim 1/\sqrt{\lambda_4 \cdot N_{\mathrm{eff}}}$:

$$
\alpha_s(\mu) = \frac{\lambda_4(\mu)}{4\pi \cdot 9}
$$

where 9 is the number of coherences in the 3-to-$\bar{3}$ sector.

**(d)** $\theta$-vacuum. The full vacuum is a superposition of instanton sectors:

$$
|\theta\rangle = \sum_{n=-\infty}^{\infty} e^{in\theta} |n\rangle
$$

From T-99 (step 5): $\theta_{\mathrm{QCD}} = 0$ **exactly**, so the physical vacuum = $|0\rangle$ — the unique instanton sector without a phase factor. *Retracted 2026-09-26:* step 5 is retracted [✗]; the physical vacuum is $|\bar\theta\rangle$ with $\bar\theta$ a free parameter ([§3.1c](#тета-не-из-потенциала)).

---

## 4. Deconfinement and Phase Transition

### 4.1 Theorem 2.1 (Deconfinement as a Gap Phase Transition)

:::warning[Statuses of §4]
Polyakov loop as order parameter — **[T]** (from the $\mathbb{Z}_3$ centre of $\mathrm{SU}(3)_C$ [T-42e]). Critical temperature $T_c \sim 170$ MeV — **[C at (SV)]** (depends on vacuum parameters). Crossover with dynamical quarks — **[H]** (qualitative model).
:::

As $T_{\mathrm{eff}}$ rises above the critical value $T_{\mathrm{deconf}}$ the system undergoes a phase transition from the confinement phase to the deconfinement phase:

**(a)** **Confinement phase** ($T < T_{\mathrm{deconf}}$):
- $\mathrm{Gap} \to 0$ in the 3-to-$\bar{3}$ sector
- Area law
- Linear potential $V(L) = \sigma \cdot L$
- Quarks confined in colourless hadrons

**(b)** **Deconfinement phase** ($T > T_{\mathrm{deconf}}$):
- $\mathrm{Gap} > 0$ in the 3-to-$\bar{3}$ sector (thermal fluctuations break isotropy)
- Perimeter law: $W(C) \sim \exp(-\mu \cdot P(C))$
- Potential screened: $V(L) = \sigma \cdot L \cdot \exp(-L/\lambda_D)$
- Free quarks and gluons

**(c)** Critical temperature:

$$
T_{\mathrm{deconf}} = T_c^{(3\bar{3})} = \frac{\mu^2_{3\bar{3}}}{\Gamma_2 / \kappa_0 \cdot k_B \ln 9}
$$

from the Gap-theory phase diagram restricted to the 3-to-$\bar{3}$ sector ($N_{\mathrm{eff}} = 9$, not 21).

**(d)** Prediction. For 3-to-$\bar{3}$: $N_{\mathrm{eff}} = 9$, $\mu^2 \approx 16.6$ in Gap units. Translation to physical units via $\Lambda_{\mathrm{QCD}}$:

$$
T_{\mathrm{deconf}} \sim \Lambda_{\mathrm{QCD}} \sim 170 \text{ MeV}
$$

— consistent with lattice QCD computations ($T_c \approx 150\text{--}170$ MeV for the crossover transition).

### 4.2 Order Parameter of Deconfinement (Polyakov Loop)

The confinement–deconfinement phase transition is characterised by an order parameter — the Polyakov loop $\langle P \rangle$:

$$
P = \frac{1}{N_c}\mathrm{Tr}\left[\mathcal{P}\exp\left(i\oint_0^{1/T} A_0^a T_a \, d\tau\right)\right]
$$

In the Gap formalism $A_0^a \sim \partial_\tau \theta_{ij}^{(a)}$, and the Polyakov loop measures the holonomy of the Gap connection along the temporally compactified coordinate $\tau \in [0, 1/T]$.

<a id="теорема-полякова-порядок"></a>

:::tip Theorem (Polyakov loop as order parameter) [T]
The Polyakov loop $\langle P \rangle$ is the order parameter of deconfinement for pure $\mathrm{SU}(3)_C$. Proof: $\mathrm{SU}(3)_C = \mathrm{Stab}_{G_2}(e_O)$ [T-42e [T]]. The centre $Z(\mathrm{SU}(3)) = \mathbb{Z}_3$ acts on the Polyakov loop as $P \mapsto e^{2\pi i k/3} P$, $k=0,1,2$. In the confinement phase $\mathbb{Z}_3$-symmetry is exact → $\langle P \rangle = 0$ (the unique $\mathbb{Z}_3$-invariant value). Deconfinement = spontaneous breaking of $\mathbb{Z}_3$ → $\langle P \rangle \neq 0$. This is the standard result (Svetitsky–Yaffe, 1982), applied to $\mathrm{SU}(3)_C$ derived from the $G_2$-structure. $\blacksquare$
:::

**(a)** At $T < T_c$: $\langle P \rangle = 0$ — the centre $\mathbb{Z}_3$-symmetry of $\mathrm{SU}(3)_C$ is unbroken. The Gap phases $\theta_{ij}$ average to zero upon traversal of the thermal circle. The free energy of a single quark is infinite: $F_q = -T\ln\langle P \rangle \to \infty$.

**(b)** At $T > T_c$: $\langle P \rangle \neq 0$ — the centre $\mathbb{Z}_3$-symmetry is spontaneously broken. Thermal fluctuations break the isotropy of the Gap vacuum in the 3-to-$\bar{3}$ sector, Gap acquires a non-zero value, and the holonomy becomes non-trivial. The quark free energy is finite.

**(c)** Critical temperature [C at (SV)]. The formula for $T_c$ (§4.1) depends on the vacuum parameters T-64 [T] (corrected to the $G_2$-invariant potential; its vacuum has no sector values — hypothesis (SV)); qualitatively $T_c \sim \Lambda_{\mathrm{QCD}} \sim 170$ MeV.

**(d)** Nature of the transition [H]. For pure $\mathrm{SU}(3)$ (without dynamical quarks) the transition is first order — $\langle P \rangle$ undergoes a jump. With $N_f = 2+1$ dynamical quarks the transition broadens into a crossover. In the Gap formalism: dynamical quarks are fermionic Gap configurations, their presence explicitly breaks $\mathbb{Z}_3$-symmetry ($\langle P \rangle \neq 0$ already at $T < T_c$), turning the phase transition into an analytic crossover.

Computational problem C18: finite-temperature Gap lattice. Realisable as MVP-12 in SYNARC.

**(d)** Quark–gluon plasma (QGP). At $T \gg T_c$ the system enters the quark–gluon plasma phase, where:
- $\mathrm{Gap}(\text{3-to-}\bar{3}) \sim O(1)$ — colour degrees of freedom are deconfined
- QGP pressure: $p \approx \frac{\pi^2}{90}\left(2(N_c^2-1) + \frac{7}{2}N_c N_f\right)T^4$ — ideal Stefan–Boltzmann gas
- Corrections $\sim \alpha_s(T)$ are computed by standard perturbative RG (see [Gap renormalisation group](/docs/physics/gauge-symmetry/rg-flow))

---

## 5. Asymptotic Freedom

Asymptotic freedom — the decrease of the coupling constant $\alpha_s$ with increasing energy — is a fundamental property of $\mathrm{SU}(3)_C$, ensuring the transition from confinement (IR) to free quarks (UV). In the Gap formalism asymptotic freedom follows from the [general RG structure](/docs/physics/gauge-symmetry/rg-flow): the beta function of $\lambda_4$ in the 3-to-$\bar{3}$ sector, restricted to $N_{\mathrm{eff}} = 9$ coherences, reproduces the standard one-loop QCD result.

### 5.1 Theorem 3.1 (Running Coupling Constant)

:::tip[Status: Theorem \[T\]]
The $\mathrm{SU}(3)_C$ coupling constant in the Gap formalism runs under RG according to the standard formula.
:::

**(a)** One-loop beta function for $\alpha_s$ in the 3-to-$\bar{3}$ sector:

$$
\beta_{\alpha_s} = -\frac{\alpha_s^2}{2\pi}\left(\frac{11}{3}N_c - \frac{2}{3}N_f\right)
$$

In the Gap formalism: $N_c = 3$ (number of colours $= \dim(\text{3-sector})$), $N_f$ — number of active fermion generations.

**(b)** Sign: for $N_f < 33/2 = 16.5$ (satisfied for the SM with $N_f = 6$): $\beta_{\alpha_s} < 0$ $\to$ **asymptotic freedom**. At lower energy (larger distance) $\alpha_s$ grows $\to$ confinement.

**(c)** Relation to Gap parameters:

$$
\alpha_s(\mu) = \frac{\lambda_4(\mu)}{4\pi \cdot 9} = \frac{4\pi^2/63}{4\pi \cdot 9} \cdot \left(1 + \beta_{\lambda_4} \ln(\mu/\Lambda)\right)^{-1} = \frac{\pi}{567}\cdot\left(1 + \beta_{\lambda_4} \ln(\mu/\Lambda)\right)^{-1}
$$

using the Wilson–Fisher value $\lambda_4^* = 4\pi^2/63$.

**(d)** $\Lambda_{\mathrm{QCD}}$ from Gap:

$$
\Lambda_{\mathrm{QCD}} = \mu_{\mathrm{phys}} \cdot \exp\left(-\frac{2\pi}{(11 - 2N_f/3)\, \alpha_s(\mu_{\mathrm{phys}})}\right)
$$

### 5.1a Relation to the Gap RG Flow [T]

The running coupling constant $\alpha_s$ is a special case of the [RG flow of $V_{\mathrm{Gap}}$ parameters](/docs/physics/gauge-symmetry/rg-flow). The correspondence is established as follows:

**(a)** General one-loop $\beta$-function for $\lambda_4$ (see [Gap renormalisation group, §2](/docs/physics/gauge-symmetry/rg-flow#однопетлевые)):

$$
\beta_{\lambda_4} = -\epsilon\lambda_4 + \frac{(N+8)}{6}\frac{\lambda_4^2}{8\pi^2}
$$

Upon restriction to the 3-to-$\bar{3}$ sector: $N = N_{\mathrm{eff}} = 9$. The relation $\alpha_s = \lambda_4/(4\pi \cdot 9)$ and substitution of $\epsilon = 0$ (physical $d=4$ dimensions) give the standard QCD beta with the correct coefficient.

**(b)** The Wilson–Fisher fixed point $\lambda_4^* = 4\pi^2/63$ (from [RG analysis](/docs/physics/gauge-symmetry/rg-flow)) determines the value of $\alpha_s$ at the confinement scale:

$$
\alpha_s^* = \frac{\lambda_4^*}{4\pi \cdot 9} = \frac{4\pi^2}{63 \cdot 36\pi} = \frac{\pi}{567} \approx 0.0055
$$

This value corresponds to the deep perturbative regime. Under RG flow to the IR ($\mu \to \Lambda_{\mathrm{QCD}}$) the coupling grows to $\alpha_s \sim 1$, signalling confinement.

**(c)** Two-loop corrections (see [RG flow, §3](/docs/physics/gauge-symmetry/rg-flow)) modify the running of $\alpha_s$ at intermediate energies. RG suppression of $\lambda_3$ in the flow from $\mu_{\mathrm{Planck}}$ to $\mu_{\mathrm{EW}}$ (factor $\sim 10^{-14.5}$) is critical for quantitative predictions of CKM mixing angles and the $\Lambda$ budget.

### 5.2 Corollary (Running of Quark Masses)

Quark masses (defined via the Higgs coupling) run under RG:

$$
m_q(\mu) = m_q(\mu_0) \cdot \left(\frac{\alpha_s(\mu)}{\alpha_s(\mu_0)}\right)^{12/(33 - 2N_f)}
$$

The anomalous mass dimension $\gamma_m = 12/(33 - 2N_f)$ is the standard QCD result. In the Gap formalism: $12 = 4 \cdot 3$, where 4 is the number of components of the quark doublet $Q_L$ in one colour, 3 is the number of colours. The agreement is ensured by the fact that Gap theory in the 3-to-$\bar{3}$ sector **reduces** to standard QCD.

---

## 6. ABJ Axial Anomaly from Cliff(7)

The Adler–Bell–Jackiw (ABJ, 1969) axial anomaly — quantum violation of the classical conservation of the axial current — is reproduced in the Gap formalism via the Clifford algebra $\mathrm{Cliff}(7)$ underlying the 7-dimensional internal structure.

### 6.1 Axial Current in the Gap Formalism [T]

:::tip[Status: Theorem \[T\]]
The axial current and its anomaly are fully reproduced from the $\mathrm{Cliff}(7)$-structure of Gap fermions.
:::

**(a)** The chiral operator in the Gap formalism is defined via $\mathrm{Cliff}(7)$-elements:

$$
\gamma_5 = i\,\Gamma_O\,\Gamma_A\,\Gamma_S\,\Gamma_D
$$

where $\Gamma_X$ are generators of $\mathrm{Cliff}(7)$ associated with the 7 coherence dimensions. Axial current:

$$
j_5^\mu = \sum_{\mathrm{fermions}} \bar{\chi}\,\gamma^\mu\,\gamma_5\,\chi = n_L^\mu - n_R^\mu
$$

where $n_L$ is the number of configurations with $\mathrm{Gap}(E,U) = 0$ (left-handed), $n_R$ — with $\mathrm{Gap}(E,U) \neq 0$ (right-handed).

**(b)** Classical conservation: in the absence of gauge fields chirality is conserved ($\partial_\mu j_5^\mu = 0$). In Gap language: $\mathrm{Gap}(E,U) = 0$ cannot spontaneously become $\mathrm{Gap}(E,U) \neq 0$ without interaction.

### 6.2 Quantum Anomaly from the Index Theorem [T]

**(a)** Dirac operator on Gap space:

$$
D_{\mathrm{Gap}} = \sum_{\mu=0}^{3}\gamma^\mu D_\mu, \qquad D_\mu = \partial_\mu + A_\mu^a T_a
$$

where $A_\mu^a$ is the Gap gauge field (as in §1.2).

**(b)** Dirac index (Atiyah–Singer theorem):

$$
\mathrm{ind}(D) = n_+ - n_- = \frac{1}{32\pi^2}\int d^4x\, F_{\mu\nu}^a\,\tilde{F}^{a,\mu\nu}
$$

where $n_\pm$ are the numbers of zero modes with positive/negative chirality, $\tilde{F}^{\mu\nu} = \frac{1}{2}\epsilon^{\mu\nu\rho\sigma}F_{\rho\sigma}$ is the dual tensor.

**(c)** Anomalous divergence of the axial current:

$$
\partial_\mu j_5^\mu = \frac{N_f \cdot g_s^2}{16\pi^2}\, G_{\mu\nu}^a\,\tilde{G}^{a,\mu\nu}
$$

The coefficient $N_f = 3$ is the number of fermion generations. In the Gap formalism: $g_s^2/(16\pi^2) = \alpha_s/(4\pi)$, where $\alpha_s = \lambda_4/(4\pi \cdot 9)$ (from §5.1).

**(d)** Role of $\mathrm{Cliff}(7)$ [T]. The standard proof of the anomaly (Fujikawa, 1979) is based on the non-invariance of the path integral measure. Adaptation to the Gap formalism: replacing the ordinary Dirac operator by the Gap-Dirac operator does not change the topological nature of the anomaly. The coefficient is determined by the structure of the Clifford algebra; for the physical subspace $\mathrm{Cliff}(1,3) \subset \mathrm{Cliff}(7)$ the result coincides with the standard one. Key point: $\gamma_5$ is defined via **four** of the seven generators of $\mathrm{Cliff}(7)$ ($O, A, S, D$), and its anticommutation with $D_{\mathrm{Gap}}$ guarantees the existence of a chiral symmetry, broken at the quantum level.

### 6.3 Decay $\pi^0 \to \gamma\gamma$ [T]

The decay of the neutral pion is the classical confirmation of the ABJ anomaly and the number of colours $N_c = 3$.

**(a)** Amplitude:

$$
\mathcal{A}(\pi^0 \to \gamma\gamma) = \frac{\alpha\, N_c}{2\pi\, f_\pi}\,\epsilon_{\mu\nu\rho\sigma}\,\epsilon_1^\mu\, k_1^\nu\, \epsilon_2^\rho\, k_2^\sigma
$$

where $N_c = 3 = \dim(\{A,S,D\})$ is the number of colours from the Gap structure, $f_\pi \approx 93$ MeV is the pion decay constant.

**(b)** Lifetime:

$$
\tau(\pi^0) = \frac{64\pi}{\left(\alpha N_c / (\pi f_\pi)\right)^2 m_\pi^3} \approx 8.4 \times 10^{-17}\;\text{s}
$$

Observed value: $(8.5 \pm 0.5) \times 10^{-17}$ s. **Exact agreement** — confirms $N_c = 3$ from the $G_2$ decomposition.

**(c)** Interpretation in the Gap formalism. $\pi^0$ is a superposition of quark–antiquark Gap configurations $(u\bar{u} - d\bar{d})/\sqrt{2}$. The decay $\pi^0 \to \gamma\gamma$ is a rearrangement of the Gap profile: from a configuration with $\mathrm{Gap}(\text{3-to-}\bar{3}) \neq 0$ (quark pair) to a configuration with $\mathrm{Gap} = 0$ (photons — massless, colourless). The anomaly ensures non-conservation of the axial current, permitting this transition.

### 6.4 Anomalous Ward Identities [T]

From the ABJ anomaly the modified Ward identities for axial vertices follow:

$$
q_\mu\,\Gamma_5^{\mu,ab}(p,q) = 2m\,\Gamma_5^{ab}(p,q) + \frac{\alpha_s}{2\pi}\,\delta^{ab}\,\epsilon_{\mu\nu\rho\sigma}\,p^\mu q^\nu\epsilon_1^\rho\epsilon_2^\sigma
$$

The second term is the anomalous contribution, absent classically. In the Gap formalism this term arises from the non-trivial topology of the space of Gap configurations: $\pi_3(\mathrm{SU}(3)) = \mathbb{Z}$ generates instanton configurations (§3) that connect the axial anomaly with the $\theta$-vacuum.

### 6.5 Cancellation of Gauge Anomalies (T-175b) [T] for the Standard-Model content; [C at (FE)] as a UHM result {#теорема-отмена-калибровочных-аномалий}

:::tip Theorem (Cancellation of gauge anomalies) [T] for the representation content of Step 3; [C at (FE)] as a UHM result
For the one-generation fermion content of Step 3 — the Standard-Model fermions, which UHM imports with Connes' $H_F$ — the $\mathrm{SU}(3)_C \times \mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$ gauge anomalies cancel **completely**. (Until 2026-09-25 the statement read: "The UHM spectral triple (T-53) with unimodularity guarantees complete cancellation"; that derivation is retracted in Step 2 below.)

$$
\mathrm{tr}(T^a \{T^b, T^c\}) = 0 \quad \text{for all gauge generators}
$$

:::

**Frame of the premise (2026-09-26).** (FE) is the premise of the axis frame. In the Clifford frame it is replaced by (Cl₀), and there the cancellation is no longer imported: the generation $\mathcal S_{\mathbb C}$ is the $\mathbf{16}$ of $\mathrm{Spin}(10)$, which has no cubic invariant, so every anomaly vanishes (T-329(e), [T] as mathematics, [C at (Cl)] in UHM; [Standard Model §2.6](/docs/physics/gauge-symmetry/standard-model#поколение-t329), [Premises of UHM](/docs/reference/premises#гипотезы-отождествления)).

**Proof.**

**Step 1 (Unimodularity = anomaly cancellation).** Alvarez, Gracia-Bondia, Martin (Phys. Lett. B364, 1995) proved: in the NCG model of the Standard Model the unimodularity condition $\det(u)|_{\mathcal{H}_{\text{int}}} = 1$ is **strictly equivalent** to the cancellation of gauge anomalies (in the absence of right-handed neutrinos; with right-handed neutrinos — also true with automatic adjustment of hypercharges).

**Step 2 (UHM satisfies unimodularity) — retracted [✗] (2026-09-25).** Former text: "The spectral triple T-53 has $A_{\text{int}} = \mathbb{C} \oplus M_3(\mathbb{C}) \oplus M_3(\mathbb{C})$, real structure $J$ (KO-dim 6) and is Morita-equivalent to the Connes algebra $\mathbb{C} \oplus \mathbb{H} \oplus M_3(\mathbb{C})$ ([T-175a](/docs/core/foundations/spacetime#алгебра-морита)). The unitary group $U(A_{\text{int}}) = U(1) \times U(3) \times U(3)$ after unimodularity gives:

$$
SU(A_{\text{int}}) = \{u : \det(u)|_{\mathcal{H}_{\text{int}}} = 1\} \to \mathrm{SU}(3)_C \times \mathrm{SU}(2)_L \times \mathrm{U}(1)_Y\text{."}
$$

Three of its inputs fail: no real structure of KO-dimension 6 exists on $\mathbb{C}^7$ — its $\chi = \pm 1$ eigenspaces would need equal dimension, and 7 is odd ([spacetime, Step 6](/docs/core/foundations/spacetime#теорема-спектральная-тройка)); the Morita equivalence T-175a is retracted (the centres $\mathbb{C}^3$ and $\mathbb{C}\oplus\mathbb{R}\oplus\mathbb{C}$ differ); and unimodularity cannot produce an $\mathrm{SU}(2)$ from $U(1) \times U(3) \times U(3)$ — the condition $\det u = 1$ is a single constraint that cuts the rank from 7 to 6 and leaves $\mathrm{U}(1)^{2} \times \mathrm{SU}(3)^{2}$ up to finite quotients, with no $\mathrm{SU}(2)$ factor at all. The anomaly cancellation of Step 1 is a theorem about Connes' model with its imported $H_F$; UHM inherits it only together with that import, with the electroweak group [C at (FE)] ([Standard Model](/docs/physics/gauge-symmetry/standard-model#теорема-фэ)).

**Step 3 (Explicit verification).** The UHM fermion representation (from the sectoral decomposition + [HE](/docs/physics/gauge-symmetry/standard-model#теорема-фэ)) for one generation:

| Fermion | $(\mathrm{SU}(3)_C, \mathrm{SU}(2)_L, Y)$ | Multiplicity |
|---------|------|------|
| $Q_L$ | $(3, 2, +1/6)$ | 6 |
| $u_R$ | $(3, 1, +2/3)$ | 3 |
| $d_R$ | $(3, 1, -1/3)$ | 3 |
| $L_L$ | $(1, 2, -1/2)$ | 2 |
| $e_R$ | $(1, 1, -1)$ | 1 |

Verification of all 5 cancellation conditions ($N_g = 3$ generations factor out):

- $\mathrm{tr}(Y) = 6 \cdot \frac{1}{6} + 3 \cdot \frac{2}{3} + 3 \cdot (-\frac{1}{3}) + 2 \cdot (-\frac{1}{2}) + 1 \cdot (-1) = 1 + 2 - 1 - 1 - 1 = 0$ $\checkmark$
- $\mathrm{tr}(Y^3) = 6 \cdot (\frac{1}{6})^3 + 3 \cdot (-\frac{2}{3})^3 + 3 \cdot (\frac{1}{3})^3 + 2 \cdot (-\frac{1}{2})^3 + 1\cdot(1)^3 = \frac{1}{36} - \frac{8}{9} + \frac{1}{9} - \frac{1}{4} + 1 = 0$ $\checkmark$ (all fields written as **left-handed** Weyl: the right-handed $u,d,e$ enter via their conjugates $Y\to-Y$; the earlier line used unconjugated $Y$ and summed to $-4/9$)
- $\mathrm{SU}(3)^2 \times \mathrm{U}(1)_Y$: $2 \cdot \frac{1}{6} - \frac{2}{3} + \frac{1}{3} = 0$ $\checkmark$
- $\mathrm{SU}(2)^2 \times \mathrm{U}(1)_Y$: $3 \cdot \frac{1}{6} + (-\frac{1}{2}) = 0$ $\checkmark$
- Gravitational $\mathrm{tr}(Y) = 0$ — coincides with the first. $\checkmark$

All anomaly coefficients vanish. $\blacksquare$

:::info Relation to the ABJ anomaly
Sections 6.1–6.4 prove the **chiral** ABJ anomaly ($\partial_\mu j_5^\mu \neq 0$) — the correct anomaly that **must** exist. T-175b proves the **cancellation of gauge** anomalies ($\mathrm{tr}(T^a\{T^b,T^c\}) = 0$) — the consistency condition that **must be satisfied**. Both results are consistent: the chiral anomaly breaks a global symmetry, the gauge anomalies are cancelled for the local symmetry.
:::

---

## 7. Complete Picture of Confinement in the Gap Formalism

### 7.1 Diagram

```
 UV (high energies) IR (low energies)
 Gap(3-to-3̄) ~ O(1) Gap(3-to-3̄) → 0
 αs ≪ 1 αs ~ 1
 ─────────────────────────────────────────────────→
 Free quarks Confinement
 Perimeter law W(C) Area law W(C)
 V(L) → const V(L) = σ·L

 ←── Asymptotic freedom ───→
 ←── RG: βα < 0 ───────────────→
```

### 7.2 Self-Consistency

The proposed confinement interpretation needs independent gauge dynamics and physical matching [H/Pr]:

1. A selected positive form/vector has stabilizer $SU(3)$ [T]; its colour interpretation is [I/H].
2. A physical eight-gluon action is additional data [H].
3. A limit of numerical phase Gap alone establishes no confinement [✗ as the former implication].
4. The topological area-law proof is withdrawn [✗]; a transfer-matrix/linear-energy result requires the field-model hypotheses of §1.3.
5. The tension values in §2 are calibrated scenarios [H], not an output fixed by T-64/T-73/T-74.
6. $\theta_{\mathrm{QCD}} = 0$ — retracted [✗] 2026-09-26, strong CP open [Pr]: the Gap sector is CP-neutral but fixes no $\bar\theta$ ([§3.1c](#тета-не-из-потенциала)). Earlier: [C at (SV)] (T-99: step 2 holds for the retracted cubic only; the corrected potential is PT-even, and no lift of its vacuum's antiunitary symmetry gives $\bar\theta = 0$ with $m_t \neq m_b$ and $J \neq 0$ — T-333)
7. Deconfinement at $T_c \sim \Lambda_{\mathrm{QCD}} \sim 170$ MeV [C at (SV)]; order parameter — Polyakov loop [T] (from $\mathbb{Z}_3$ centre of $\mathrm{SU}(3)_C$ = Stab$_{G_2}(e_O)$ [T-42e]); crossover with quarks [H]
8. Asymptotic freedom reproduced in the standard way [T]; relation to [RG flow](/docs/physics/gauge-symmetry/rg-flow) via $\lambda_4$ [T]
9. ABJ anomaly from $\mathrm{Cliff}(7)$: $\partial_\mu j_5^\mu = (N_f g_s^2/16\pi^2)\,G\tilde{G}$ [T]
10. Decay $\pi^0 \to \gamma\gamma$: $\tau = 8.4 \times 10^{-17}$ s (agreement with PDG) [T]
11. Cancellation of **gauge** anomalies: $\mathrm{tr}(T^a\{T^b,T^c\}) = 0$ for the Standard-Model content (T-175b: the arithmetic [T]; as a UHM result [C at (FE)] with the imported $H_F$ — the derivation "from the spectral triple + unimodularity" is retracted)

---

## 8. Status Summary

| Result | Status |
|-----------|--------|
| Wilson-loop area law from numerical Gap | [✗] former proof; [H/Pr] field-model programme |
| Tension values from the chosen formulas in §2 | [H] physical identification and independent inputs required |
| Tension values from the chosen formulas in §2 | [H] physical identification and independent inputs required |
| Structural $\theta_{\mathrm{QCD}} = 0$ (T-99): 7-step derivation from A1–A5 | [✗] (retracted 2026-09-26: step 4 false for $V_3$; earlier [C at (SV)], step 2 [T] for $V_3$ only; the vacuum-symmetry route closed, T-333) |
| Gap sector CP-neutral; no $G_2$-invariant Gap term fixes $\bar\theta$ (T-99 corrected, §3.1c) | [T] as mathematics, [C at (Cl)] in UHM; strong CP open [Pr] |
| Polyakov loop as deconfinement order parameter (from $\mathbb{Z}_3$ centre of $\mathrm{SU}(3)_C$ [T-42e]) | [T] |
| Critical temperature $T_c \sim 170$ MeV | [C at (SV)] |
| Crossover with dynamical quarks ($N_f = 2+1$) | [H] |
| Asymptotic freedom (relation to [RG flow](/docs/physics/gauge-symmetry/rg-flow)) | [T] |
| Running of quark masses | [T] |
| ABJ anomaly (chiral) from $\mathrm{Cliff}(7)$; index theorem | [T] |
| Cancellation of gauge anomalies $\mathrm{tr}(T^a\{T^b,T^c\}) = 0$ (T-175b) | [T] for the Standard-Model content; [C at (FE)] as a UHM result |
| Decay $\pi^0 \to \gamma\gamma$: $\tau = 8.4 \times 10^{-17}$ s | [T] |
| Anomalous Ward identities for axial vertices | [T] |

:::warning[Open problems]
1. **Glueball spectrum.** Prediction of glueball masses from Gap parameters is a non-perturbative problem.
2. **Anomaly in the gravitational sector.** The mixed gravitational–axial anomaly $\partial_\mu j_5^\mu \supset R\tilde{R}$ in the Gap formalism requires full accounting of the $\mathrm{Cliff}(7)$-spectrum, including the O-direction. The connection to emergent gravity is an open question [D].
:::

---

**Related documents:**
- [G₂-structure and Fano plane](/docs/physics/gauge-symmetry/g2-structure)
- [Standard Model from G₂](/docs/physics/gauge-symmetry/standard-model)
- [RG flow](/docs/physics/gauge-symmetry/rg-flow)
- [Vacuum uniqueness](/docs/proofs/categorical/uniqueness-theorem)
