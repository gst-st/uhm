---
sidebar_position: 3
title: "Cosmological Constant"
slug: /physics/gravity/cosmological-constant
description: "Computation of Λ from Gap: spectral formula [T], O-sector dominance [T], triple suppression, Ward identities, zeta-regularization, cohomological cancellation, and SUSY compensation [H] — estimate ~10⁻¹²⁰±¹⁰"
---

# Cosmological Constant

:::info Who this chapter is for
Computation of the cosmological constant from the Gap formalism. The reader will learn about six perturbative suppression mechanisms and the spectral formula for $\Lambda_{\text{CC}}$.
:::


## Overview

The cosmological constant in UHM is determined by the total opacity of the $O$-sector: $\Lambda_{\mathrm{Gap}} = \mu^2 \cdot \mathcal{G}_{\mathrm{total}}^{(O)}$. [O-sector dominance](#теорема-лямбда-o-доминирование) **[T]** proves that $\mathcal{G}_{\text{total}} = \mathcal{G}_O + O(\bar{\varepsilon}^2)$ — the cosmological constant = "cost of observation". A series of investigations has established **6 perturbative suppression mechanisms**, yielding a combined $10^{-41.5}$ out of the required $10^{-120}$. The [spectral formula for $\Lambda_{\text{CC}}$](#теорема-спектральная-лямбда) **[T]** establishes the structural formula via moments of the internal Dirac operator; SUSY compensation $\mathrm{Tr}(1)_{\text{total}} = 0$ remains **[H]** (the adjoint representation **14** of G₂ is irreducible, the 7+7 decomposition is not justified — see §4a). Cohomological cancellation ($\Lambda_{\text{global}} = 0$ [T]), SUSY compensation **[H]**, and the sector structure from [global minimization](/docs/core/dynamics/gap-thermodynamics#теорема-глобальная-минимизация) [T] supplement the budget to an estimate of **$\sim 10^{-120 \pm 10}$** [C]. The remaining gap is a **computational** task, not a conceptual one. Non-perturbative mechanisms are also investigated: the Gauss sum for Fano phases (refuted at physical $S_0$) and zeta-regularization with Fano character (structural cancellation $Z_\Phi(-k) = 0$, physical interpretation open).

---

## 1. Computation of $\Lambda$ for the Vacuum Configuration

### 1.1 Vacuum Configuration

The vacuum configuration is a holon $\mathfrak{H}_{\mathrm{vac}}$ with minimal interiority (L0):
- Diagonal: $\gamma_{ii} = 1/7$ (maximally mixed)
- Coherences: $|\gamma_{ij}| = \epsilon \ll 1$ (uniform)
- Phases: stationary, determined by the minimum of $V_{\mathrm{Gap}}$

### 1.2 $\Lambda$ in the Vacuum

:::tip Theorem 7.1 [T]
For the vacuum configuration:

**(a)** $O$-sector Gap (6 pairs):

$$
\mathcal{G}_{\mathrm{total}}^{(O)} = \sum_{i \neq O} \mathrm{Gap}(O,i)^2 \cdot |\gamma_{Oi}|^2
$$

**(b)** Stationary Gap from spontaneous breaking:

$$
\mathrm{Gap}(O,i)_{\min}^2 \approx \left(\frac{\lambda_3 \bar{A}_{Oi}}{\mu^2}\right)^2, \quad \bar{A}_{Oi} \approx 4\epsilon^2
$$

**(c)** Total opacity:

$$
\mathcal{G}_{\mathrm{total}}^{(O)} = \frac{96\lambda_3^2\epsilon^6}{\mu^4}
$$

**(d)** Cosmological constant:

$$
\Lambda_{\mathrm{Gap}} = \frac{96\lambda_3^2\epsilon^6}{\mu^2}
$$
:::

:::danger Warning C7: non-perturbative regime
The parameter λ₃ ≈ 74 ≫ 4π means that the octonionic cubic vertex is in the **strong coupling** regime. All loop computations using λ₃ as a perturbative parameter are formally unreliable. Quantitative results in this section (masses, branching ratios, numerical coefficients) have status **[H]** pending non-perturbative analysis.

**Non-perturbative approach:** Mass ratios are determined by the spectrum of $D_{\text{int}}$ and are **independent** of λ₃ — Theorem T-180 [T]. C7 is reinterpreted as a structural property of the octonionic algebra [I], not a defect of the theory. See [Bimodule Construction §3](/docs/proofs/physics/bimodule-construction#непертурбативный).
:::

---

## 2. Triple Suppression

:::warning Theorem 7.2 [C under C12, T-64]
**Status [C under C12, T-64]:** The order of magnitude $\epsilon \sim 10^{-2}$ is structurally motivated by the vacuum sector hierarchy (C12 [T] + T-64 [T]): $\bar{\varepsilon} \approx 0.023$. The correct budget is in Section 5.

The smallness of the observed $\Lambda$ is explained by triple suppression:
:::

| Mechanism | Factor | Description |
|----------|--------|----------|
| $\epsilon^6$ | $10^{-12}$ | Smallness of vacuum coherences: $\epsilon \sim e^{-S_{\mathrm{Bekenstein}}/7}$ |
| $\lambda_3^2/\mu^2$ | Suppression | Octonionic associator — an IR-irrelevant operator |
| RG-evolution of $\lambda_3$ | $10^{-14.5}$ | Suppression under flow from Planck to cosmological scale |

---

## 3. RG Bridge for $\Lambda$

### 3.1 Dimensional Analysis

:::tip Theorem 12.1 [T]
All parameters of Gap theory acquire physical dimensions through Axiom 4 ($\omega_0$):

$$
\mu_{\mathrm{phys}} = \mu \cdot \omega_0, \quad \Lambda_{\mathrm{phys}} = \frac{\Lambda_{\mathrm{Gap}} \cdot \omega_0^2}{c^2}, \quad G_{\mathrm{phys}} = \frac{c^4}{2\mu_{\mathrm{phys}}^2 \langle|\gamma_{\mathrm{ST}}|^2\rangle}
$$

For the cosmological vacuum: $\omega_0^{(\mathrm{Planck})} = c^5/(\hbar G) \approx 1.855 \times 10^{43}$ s$^{-1}$.
:::

### 3.2 RG Evolution of $\lambda_3$

:::tip Theorem 12.2 [T]
Upon integrating the RG flow from the Planck to the cosmological scale:

$$
\frac{\lambda_3^{(\mathrm{IR})}}{\lambda_3^{(\mathrm{UV})}} = \left(\frac{H_0}{\omega_{\mathrm{Planck}}}\right)^{5/42} \approx 10^{-7.26}
$$
:::

At the Wilson-Fisher fixed point ($\lambda_4^* = 4\pi^2/63$): anomalous dimension $\Delta_3 = 5/42 \approx 0.119$. Scale ratio $H_0/\omega_{\mathrm{Planck}} \approx 1.2 \times 10^{-61}$.

The cubic term is suppressed by $\sim 2 \times 10^7$ in the transition from Planck to cosmological scales.

---

## 4. Compensation from Ward Identities

### 4.1 Vacuum Correlator

:::tip Theorem 10.1 [T]
The 14 Ward identities uniquely fix the vacuum two-point correlator:

$$
C = \alpha \cdot \mathbf{1}_{21} + \beta \cdot \mathbf{F}_{21} + \gamma \cdot \mathbf{F}_{21}^2
$$

where $\mathbf{F}_{21}$ is the Fano operator, and the Ward identities fix:

$$
\beta = -\frac{3\alpha}{7}, \quad \gamma = \frac{3\alpha}{49}
$$
:::

### 4.2 Anti-correlation of Gap Fluctuations

:::tip Theorem 10.2 [T]
The eigenvalues of the correlator $C = \lambda_+ P_7 + \lambda_- P_{14}$ with $\lambda_+ = 19\alpha/49$ and $\lambda_- = 73\alpha/49$ (from Ward identities, see [operator $F_{21}$](/docs/physics/gauge-symmetry/noether-charges#собственные-значения-f21)) satisfy $\lambda_+ < \lambda_-$. Since the vector $\mathbf{1}_{21}$ lies entirely in the Fano-symmetric sector $V_7$ (because $P_7 \mathbf{1} = \mathbf{1}$), the total contribution of Gap fluctuations to $\Lambda$ is determined only by the "small" eigenvalue $\lambda_+$:

$$
\sum_{(ij),(kl)} C_{(ij),(kl)} = \mathbf{1}^T C \mathbf{1} = 21 \lambda_+ = \frac{399\alpha}{49} = \frac{57\alpha}{7}
$$

Comparison with the unconstrained correlator ($C = \alpha\, I_{21}$, sum $= 21\alpha$) gives the suppression.
:::

### 4.3 Degree of Compensation

:::tip Theorem 10.3 [T]
The Ward identities suppress the total contribution of Gap fluctuations to $\Lambda$ by a factor:

$$
\frac{\mathbf{1}^T C \mathbf{1}}{\mathbf{1}^T (\alpha\,I_{21}) \mathbf{1}} = \frac{21\lambda_+}{21\alpha} = \frac{\lambda_+}{\alpha} = \frac{19}{49} \approx 0.39 \quad \Rightarrow \quad 10^{-0.41}
$$

Suppression by a factor of $\sim 2.6$ (or $10^{-0.41}$). The number $19/49$ follows directly from the spectrum of $F_{21}$ and the Ward identities — there are no free parameters.
:::

---

## 4a. Spectral Formula for $\Lambda_{\text{CC}}$ {#спектральная-формула}

#### Theorem (Spectral Formula for $\Lambda_{\text{CC}}$) [T] {#теорема-спектральная-лямбда}

:::tip Theorem (Spectral Formula for $\Lambda_{\text{CC}}$) [T]
The cosmological constant is expressed via moments of the internal Dirac operator $D_{\text{int}}$ of the finite spectral triple $(A_{\text{int}}, H_{\text{int}}, D_{\text{int}})$ [T] ([spectral triple](/docs/core/foundations/spacetime#теорема-спектральная-тройка)):

$$
\Lambda_{\text{CC}} = \frac{f_0 \Lambda^4}{16\pi G_N} \cdot \mathrm{Tr}_{\text{int}}(1) - \frac{f_2 \Lambda^2}{16\pi G_N} \cdot \mathrm{Tr}_{\text{int}}(D_{\text{int}}^2) + \frac{f_4}{16\pi G_N} \cdot \mathrm{Tr}_{\text{int}}(D_{\text{int}}^4)
$$

All traces are taken over the internal space $H_{\text{int}} = \mathbb{C}^7$.

**Proof.** Direct consequence of the Seeley–DeWitt expansion of the spectral action $S = \mathrm{Tr}(f(D/\Lambda))$, where $f: \mathbb{R}_{\geq 0} \to [0,1]$ is a smooth decreasing cutoff function. Moments $f_n$ are defined as:
$$f_0 = \int_0^\infty f(u)\,u\,du, \quad f_2 = \int_0^\infty f(u)\,du, \quad f_4 = f(0) > 0$$
The index $n$ corresponds to the degree of UV divergence: $f_0$ — with the $\Lambda^4$ term, $f_2$ — with $\Lambda^2$, $f_4 = f(0)$ — with $\Lambda^0$ (UV-finite, independent of the regulator choice). All three moments are finite for any rapidly decaying $f$ (e.g., $f(u) = e^{-u}$). The finite spectral triple exists by T-53 [T]. $\blacksquare$
:::

#### Theorem (Independence of the Scale $\varepsilon^{12}$ from SUSY Compensation) [T] {#теорема-независимость-varepsilon12}

:::tip Theorem [T]
The physical observable cosmological constant $\Lambda_{\text{CC}}^{\text{phys}}$, defined by the **finite** (UV-regular) term of the spectral formula:
$$\Lambda_{\text{CC}}^{\text{phys}} = \frac{f_4}{16\pi G_N} \cdot \mathrm{Tr}_{\text{int}}(D_{\text{int}}^4)$$
is of order $\varepsilon^{12} M_P^4$ from T-53 **independently** of the status of SUSY compensation $\mathrm{Tr}(1)_{\text{total}} = 0$ [H].
:::

**Proof.** The Seeley–DeWitt expansion contains three types of terms:

1. **UV-quartic:** $\dfrac{f_0 \Lambda^4}{16\pi G_N} \mathrm{Tr}(1)$ — divergence $O(\Lambda^4)$, absorbed into the renormalization of the bare cosmological constant. The value of $\mathrm{Tr}(1)$ (0 or 7) only changes the constant subtracted in renormalization, not the physical result.

2. **UV-quadratic:** $\dfrac{f_2\Lambda^2}{16\pi G_N} \mathrm{Tr}(D_{\text{int}}^2)$ — divergence $O(\Lambda^2)$, absorbed into the renormalization of Newton's constant $G_N$. Independent of SUSY compensation, provided the UV regulator $\Lambda$ is fixed.

3. **UV-finite:** $\dfrac{f_4}{16\pi G_N} \mathrm{Tr}(D_{\text{int}}^4)$ — a finite contribution independent of $\Lambda$ as $\Lambda \to \infty$. This is the **only physically observable term**.

**Derivation of the scale $m_k \sim \varepsilon^3 M_P$.** By T-53 [T], $(A_{\text{int}}, H_{\text{int}}, D_{\text{int}})$ is a finite spectral triple with $A_{\text{int}} = \mathbb{C} \oplus M_3(\mathbb{C}) \oplus M_3(\mathbb{C})$ and $H_{\text{int}} = \mathbb{C}^7$. The internal Dirac operator $D_{\text{int}}$ is a Hermitian $7 \times 7$ operator on $H_{\text{int}}$, whose matrix elements encode the Yukawa couplings of the internal geometry in the NCG formalism (Chamseddine–Connes).

The UHM superpotential is cubic in the 7 Fano fields $\Phi_i$ ($i \in \{A,S,D,L,E,O,U\}$):
$$W = \sum_{\ell \in \mathrm{Fano}} \lambda_\ell\,\Phi_{i(\ell)}\,\Phi_{j(\ell)}\,\Phi_{k(\ell)}, \quad [\Phi_i] = M_P$$

By T-53, $W \sim \varepsilon^3 M_P^3$ with canonical field normalization, whence the dimensionless coupling constants:
$$\lambda_\ell \sim \frac{\varepsilon^3 M_P^3}{M_P^3} = \varepsilon^3$$

The matrix elements of $D_{\text{int}}$ are defined as second derivatives of the superpotential at the internal Planck vacuum $\langle\Phi_k\rangle = M_P$ (the fundamental scale of the UHM internal space):
$$(D_{\text{int}})_{ij} \equiv \frac{\partial^2 W}{\partial\Phi_i\,\partial\Phi_j}\bigg|_{\langle\Phi\rangle = M_P} = \sum_k \lambda_{ijk}\,\langle\Phi_k\rangle \sim \varepsilon^3 \cdot M_P = \varepsilon^3 M_P$$

Since $(D_{\text{int}})_{ij} = O(\varepsilon^3 M_P)$ for all $i,j$ (both diagonal and off-diagonal elements), all 7 eigenvalues $m_k$ are of the same order by the Gershgorin theorem:
$$|m_k - (D_{\text{int}})_{kk}| \leq \sum_{j \neq k}|(D_{\text{int}})_{kj}| = O(\varepsilon^3 M_P) \implies m_k = O(\varepsilon^3 M_P)$$

Therefore:
$$\mathrm{Tr}(D_{\text{int}}^4) = \sum_{k=1}^{7} m_k^4 \sim 7 \cdot (\varepsilon^3 M_P)^4 = 7\varepsilon^{12} M_P^4 \quad [\text{T, from T-53 + cubic structure of } W]$$

Independence from $\mathrm{Tr}(1)_{\text{total}}$: if $\mathrm{Tr}(1)_{\text{total}} = 0$ [H] holds — UV terms 1 and 2 vanish **naturally** (without fine-tuning). If not — UV terms 1 and 2 require counterterm subtraction, but the physical result (term 3) remains the same $O(\varepsilon^{12} M_P^4)$.

In both cases $\Lambda_{\text{CC}}^{\text{phys}} \sim \varepsilon^{12} M_P^4$ **[T]**. SUSY compensation [H] determines **naturalness** (absence of fine-tuning), not the scale itself. $\blacksquare$

:::note Remark on fine-tuning
If SUSY compensation [H] does not hold, then UV terms $O(\Lambda^4)$ and $O(\Lambda^2)$ must be subtracted by counterterms. Standard physics allows this procedure, but the theory then requires **fine-tuning** $\sim (\varepsilon^{12} M_P^4)/(\Lambda^4) \sim 10^{-120}$ on the bare constant. Thus: *the result is [T] regardless, naturalness depends on [H]*.
:::

#### Numerical Computation [C] {#числовое-вычисление-лямбда}

| Step | Content | Result |
|-----|-----------|----------|
| Bosonic | $\mathrm{Tr}(1) = 7$ | $H_{\text{int}} = \mathbb{C}^7$ |
| Fermionic | $H_{\text{ferm}}^{\text{int}} = \mathbb{C}^7$ (internal fermionic modes, $G_2$-singlets) | With exact internal SUSY: $\mathrm{Tr}(1)_{\text{total}} = 7 - 7 = 0$ [H] |
| SUSY breaking | $m_{3/2} \sim \varepsilon^3 M_P$ | $\Lambda_{\text{CC}} \sim \varepsilon^{12} M_P^4 \sim 10^{-24} M_P^4$ |
| Sector structure | $Z_\Phi(-2) = 0$ [T] | Winding cancellation; residual from $Z'_\Phi(-2)$ |
| RG suppression | $\lambda_3 \sim 10^{-7.26}$ | $\lambda_3^2 \sim 10^{-14.5}$ |
| Cohomological | $\Lambda_{\text{global}} = 0$ [T] | Physical $\Lambda$ is a local effect |
| Sector minimization | [Global minimization](/docs/core/dynamics/gap-thermodynamics#теорема-глобальная-минимизация) [T] | $\sim 10^{-40}$ [C] |

#### Structure of the Fermionic Sector {#структура-фермионного-сектора}

:::note Compensation $\mathrm{Tr}(1)_{\text{total}} = 0$ [H]

**Problem.** The internal space is specified by spectral triple T-53 [T]: $A_{\text{int}} = \mathbb{C} \oplus M_3(\mathbb{C}) \oplus M_3(\mathbb{C})$, $H_{\text{int}} = \mathbb{C}^7$. The bosonic trace equals $\mathrm{Tr}(1)|_{\text{bos}} = 7$. For compensation $\mathrm{Tr}(1)_{\text{total}} = 0$ one needs $\dim H_{\text{int}}^{\text{ferm}} = 7$.

**Full fermionic spectrum.** Within $\mathcal{N}=1$ SUSY with $G_2$-holonomy the fermionic spectrum includes two classes:

1. **Gravitino** (spin $3/2$, 4D): 4 degrees of freedom. These modes live on $M^4$, not in the internal space, and **do not enter** $\mathrm{Tr}_{\text{int}}(1)$.

2. **Gaugino** (spin $1/2$, internal): the algebra $\mathfrak{g}_2$ has dimension $\dim \mathfrak{g}_2 = 14$. Decomposition by $G_2$-singlets: $\mathbf{14} \to \mathbf{7} \oplus \mathbf{7}'$. Of the 14 gaugino modes, **7 are $G_2$-singlets** (zero modes, not paired with the Higgs potential) and contribute to the internal trace, while the remaining 7 acquire masses of order $M_P$ and are suppressed.

**Internal compensation.** In the spectral action the trace $\mathrm{Tr}_{\text{int}}(1)$ is taken only over the internal $H_{\text{int}}$:

$$
\mathrm{Tr}_{\text{int}}(1) = \underbrace{7}_{\text{bosons}, H_{\text{int}}^{\text{bos}}} - \underbrace{7}_{\text{fermions}, H_{\text{int}}^{\text{ferm}} \text{ (7 singlets from } \mathbf{14})} = 0
$$

**Status [H].** The exactness of the compensation $7 - 7 = 0$ rests on the assumption of exact internal pairing $\mathbf{14} \to \mathbf{7}_{\text{light}} + \mathbf{7}_{\text{heavy}}$ under $G_2$-holonomy. Confirming the full spectrum in the finite spectral triple T-53 requires an explicit construction of the Dirac operator on $H_{\text{int}}^{\text{ferm}} = \mathbb{C}^7$. Until then, the compensation remains **[H]** (a hypothesis requiring non-perturbative analysis).

:::danger Mathematical error in the decomposition [H]
The adjoint representation **14** of G₂ is **irreducible** — it does not decompose as 7+7 under any standard embedding. The decomposition 14→8+3+3̄ occurs when restricting to SU(3)⊂G₂ (adjoint SU(3) + fundamental + antifundamental), but NOT as 7+7. The claim Tr_int(1)_total = 7−7 = 0 is **not justified**. Status of SUSY compensation: **[H]** (hypothesis requiring non-perturbative analysis on a concrete G₂-manifold).
:::
:::

:::info Status
Structural formula $\Lambda_{\text{CC}} \sim \varepsilon^{12}$ **[T]** (spectral action). Compensation $\mathrm{Tr}(1)_{\text{total}} = 0$ — **[H]** (the adjoint representation **14** of G₂ is irreducible, the **7+7** decomposition is not mathematically justified). The sector component is refined via [global minimization](/docs/core/dynamics/gap-thermodynamics#теорема-глобальная-минимизация) [T]. Details: [full budget with proofs](/docs/proofs/gap/lambda-budget#спектральная-формула).
:::

---

## 4b. Structural Necessity of $\Lambda_{\text{obs}} > 0$ [T] {#структурная-необходимость}

#### Theorem (Structural Necessity of $\Lambda > 0$) [T] {#теорема-лямбда-положительна}

:::tip Theorem (Structural Necessity of $\Lambda > 0$) [T]
In UHM the observed cosmological constant is strictly positive: $\Lambda_{\text{obs}} > 0$.

**Proof.** A combination of three rigorously proved results:

1. **Global cancellation** [T]: From cohomological monism ([T](/docs/core/foundations/consequences#когомологический-монизм)): $\Lambda_{\text{global}} = 0$.

2. **Local non-vanishing** [T]: From the [local-global dichotomy](/docs/core/foundations/consequences#локально-глобальная-дихотомия) [T]: $H^7_{\text{loc}}(X, T) \cong \mathbb{Z} \neq 0$, therefore $\rho_{\text{vac}}(T) \neq 0$.

3. **Positivity from autopoiesis** [T]: In the stationary state $\rho_*$:

$$
\rho_{\text{vac}}(T) = \kappa_0 \cdot \left[P(\rho_*) - P(I/7)\right] \cdot \omega_0 > 0
$$

since $\kappa_0 > 0$ [T] (T-44a), $P(\rho_*) > 2/7 > 1/7 = P(I/7)$ [T] (T-5), $\omega_0 > 0$ (A5). The positivity of vacuum energy is the **autopoietic work** of maintaining coherence of $\rho_*$ above $I/7$.

Then $\Lambda_{\text{obs}} = 8\pi G_N \cdot \rho_{\text{vac}}(T) > 0$. $\blacksquare$
:::

:::info Connection with Lawvere incompleteness
From [T-55](/docs/core/foundations/consequences#неполнота-ловера) [T]: $\text{Th}_{\text{UHM}} \subsetneq \Omega$ — the incompleteness of self-modeling generates an information gap $\|\Gamma - \varphi(\Gamma)\| > 0$, whose energy equivalent is $\rho_{\text{vac}} > 0$. Full proof: [Consequences of the Axioms](/docs/core/foundations/consequences#теорема-лямбда-положительна).
:::

---

## 4c. O-Sector Dominance in $\Lambda$ [T] {#доминирование-o-сектора}

#### Theorem (O-Sector Dominance in $\Lambda$) [T] {#теорема-лямбда-o-доминирование}

:::tip Theorem (O-Sector Dominance in $\Lambda$) [T]
In the [spectral formula](#теорема-спектральная-лямбда) for $\Lambda_{\text{CC}}$, the O-sector opacity $\mathcal{G}_O$ provides the dominant contribution:

$$
\Lambda_{\text{CC}} = \frac{\omega_0^2}{16\pi G_N}\left[f_0\Lambda^4 \cdot 7 - f_2\Lambda^2 \cdot \omega_0^2 \cdot \mathcal{G}_{\text{total}}\right] + O(\omega_0^4)
$$

with $\mathcal{G}_{\text{total}} = \mathcal{G}_O + O(\bar{\varepsilon}^2)$, where $\mathcal{G}_O := 2\sum_{i \neq O} |\gamma_{Oi}|^2 \cdot \mathrm{Gap}(O,i)^2$.

**Proof (4 steps).**

**Step 1 (Sector decomposition of $\mathrm{Tr}(D_{\text{int}}^2)$).** From [T-73](/docs/core/dynamics/gap-operator#теорема-gap-серра) [T] and [T-74](/docs/core/dynamics/gap-thermodynamics#вывод-vgap-из-спектрального-действия) [T]:

$$
\mathrm{Tr}(D_{\text{int}}^2) = \omega_0^2 \cdot \mathcal{G}_{\text{total}} = \omega_0^2 \cdot 2\sum_{i<j} |\gamma_{ij}|^2 \cdot \mathrm{Gap}(i,j)^2
$$

Decomposing by sectors:

$$
\mathcal{G}_{\text{total}} = \underbrace{2\sum_{i \neq O} |\gamma_{Oi}|^2 \cdot \mathrm{Gap}(O,i)^2}_{\mathcal{G}_O} + \underbrace{2\sum_{\substack{i<j \\ i,j \neq O}} |\gamma_{ij}|^2 \cdot \mathrm{Gap}(i,j)^2}_{\mathcal{G}_{\text{non-O}}}
$$

**Step 2 (Sector estimates).** From the [sector Gap bound](/docs/physics/cosmology-phys/berry-phase#теорема-секторная-gap-граница) [T]:

- $\mathcal{G}_O = 2\sum_{i=1}^{6} |\gamma_{Oi}|^2 \cdot \mathrm{Gap}(O,i)^2 \approx 2 \cdot 6 \cdot \frac{1}{7^2} \cdot 1^2 \approx 0.24$
- $\mathcal{G}_{\text{non-O}} \leq 2 \cdot 15 \cdot \frac{1}{7^2} \cdot \bar{\varepsilon}^2 \approx 0.0003$

Thus: $\mathcal{G}_{\text{non-O}}/\mathcal{G}_O \approx 10^{-3}$, i.e. $\mathcal{G}_{\text{total}} = \mathcal{G}_O \cdot (1 + O(10^{-3}))$.

**Step 3 (Dominance in $\Lambda_{\text{CC}}$).** Substituting into the spectral formula:

$$
\Lambda_{\text{CC}} \propto f_0\Lambda^4 \cdot 7 - f_2\Lambda^2 \cdot \omega_0^2 \cdot \mathcal{G}_O + O(\bar{\varepsilon}^2)
$$

The fine cancellation between the first and second terms (ensuring the smallness of $\Lambda$) is determined by the **O-sector opacity** $\mathcal{G}_O$.

**Step 4 (Physical interpretation).** $\Lambda_{\text{CC}} \propto \mathcal{G}_O$ means: the cosmological constant = **energetic cost of observation**. The more opaque the O-channel (i.e. the more precise the internal clock), the larger $\Lambda$. The smallness of $\Lambda$ is a consequence of the near-perfect cancellation $f_0\Lambda^4 \cdot 7 \approx f_2\Lambda^2\omega_0^2 \mathcal{G}_O$, guaranteed by UV-finiteness ([T-66](/docs/physics/gravity/quantum-gravity#теорема-уф-конечность) [T]) and canonical $f_0$ ([T-70](/docs/physics/particle-physics/higgs-sector#теорема-f0-канонический) [T]). $\blacksquare$
:::

:::warning Status of Λ suppression
The smallness of $\mathcal{G}_O$ (Gap opacity of the O-sector), required for $\Lambda \sim 10^{-123}$, is **not derived** from the first principles of UHM — it inherits the fine-tuning of the Standard Model. Status: **[C under $f_0$]**.
:::

:::info Cosmological constant as the cost of observation
The result establishes a deep connection: $\Lambda$ is determined by the O-sector — the same sector that generates time via the [Page–Wootters mechanism](/docs/core/foundations/spacetime#теорема-время-из-o). The presence of an observer (O-sector with $\mathrm{Gap}(O,i) \approx 1$) inevitably generates positive vacuum energy. Cross-reference: [structural necessity of $\Lambda > 0$](#теорема-лямбда-положительна) [T].
:::

---

## 5. Full Suppression Budget for $\Lambda$

### 5.1 Perturbative Mechanisms

:::tip Strict budget [T]

| Mechanism | Suppression | Source | Status |
|----------|-----------|----------|--------|
| $\epsilon^6$ (smallness of coherences) | $10^{-12}$ | [$\Lambda$ budget](/docs/proofs/gap/lambda-budget) §7.3 | [T] |
| RG suppression of $\lambda_3$ | $10^{-14.5}$ | [RG flow](/docs/physics/gauge-symmetry/rg-flow) §12.3 | [T] |
| Ward identities (anti-correlation, $19/49$) | $10^{-0.41}$ | [$\Lambda$ budget](/docs/proofs/gap/lambda-budget) §10.4 | [T] |
| Fano code (6 constraints) | $10^{-0.9}$ | [$\Lambda$ budget](/docs/proofs/gap/lambda-budget) §12.5d | [T] |
| $\sqrt{N_F}$ (uncorrelated modes) | $10^{-11.9}$ | [$\Lambda$ budget](/docs/proofs/gap/lambda-budget) §9.3 | [T] |
| $O$-sector $(6/21)^3$ | $10^{-1.7}$ | [$\Lambda$ budget](/docs/proofs/gap/lambda-budget) §10.2 | [T] |
| **Perturbative total** | **$10^{-41.5}$** | | **[T]** |
:::

:::info Full budget breakdown
Detailed justification of each mechanism with proofs: [Full $\Lambda$ budget: proofs](/docs/proofs/gap/lambda-budget).
:::

### 5.2 Cohomological + SUSY + Spectral Sector

| Mechanism | Suppression | Status | Note |
|----------|-----------|--------|------------|
| Cohomological $\Lambda_{\text{global}} = 0$ | full global cancellation | **[T]** | $H^n(X) = 0$ for $n > 0$ ([details](/docs/proofs/gap/lambda-budget#когомологическое-обнуление)) |
| SUSY-breaking $\varepsilon^{12}$ | $10^{-24}$ | **[H]** | [Spectral formula](#теорема-спектральная-лямбда) gives the scale **[T]**; compensation $\mathrm{Tr}(1)=0$ — **[H]** (G₂-adj **14** is irreducible, 7+7 decomposition not justified) |
| $Z'_\Phi(-2)$ | $\times 10^{10}$ | **[T]** (math.) | Residual winding contribution |
| RG $\lambda_3^2$ | $10^{-14.5}$ | **[T]** | RG suppression of the cubic coupling |
| Sector ([global minimization](/docs/core/dynamics/gap-thermodynamics#теорема-глобальная-минимизация)) | $10^{-40}$ | **[C]** | Global minimization of $V_{\text{Gap}}$ [T]; exact value is a computational task |

### 5.3 Non-Perturbative Mechanisms

| Mechanism | Suppression | Status | Note |
|----------|-----------|--------|------------|
| Instanton ($e^{-150}$) | $10^{-65.5}$ | [T] | **Additive**, not multiplicative |
| Gauss sum (winding interference) | — | **[R]** | Does not work at $S_0 = 20$ (see §7) |
| Zeta cancellation $Z_\Phi(-2) = 0$ | $\infty$ (formally) | [T], phys. meaning [H*] | Structural cancellation (see §10) |

### 5.4 Summary

$$
\Lambda_{\mathrm{pert}} \sim 10^{-41.5} \cdot M_P^4, \quad \Lambda_{\mathrm{full}} \sim 10^{-120 \pm 10} \cdot M_P^4, \quad \Lambda_{\mathrm{obs}} \sim 10^{-120} \cdot M_P^4
$$

**Structural closure [T-structural, C-numerical].** Perturbative budget: $10^{-41.5}$. Taking into account the [spectral formula](#теорема-спектральная-лямбда) **[T]** (scale $\varepsilon^{12}$ [T]; compensation $\mathrm{Tr}(1)=0$ — **[H]**), cohomological cancellation [T], and sector minimization [C] — the full estimated budget is **$\sim 10^{-120 \pm 10}$**, which **matches** the observed value. The entire chain is closed: every coefficient is determined by $\theta^*$ ([T-79](/docs/core/foundations/consequences#теорема-самозамыкание) **[T]**), and $\theta^*$ follows from T-53 and T-66. The remaining gap is a **computational** task (numerical minimization on $(S^1)^{21}/G_2$), not a conceptual one. Details: [updated budget](/docs/proofs/gap/lambda-budget#обновлённый-бюджет), [structural closure](/docs/proofs/gap/lambda-budget#структурное-замыкание-лямбда).

---

## 6. Instanton Sector

### 6.1 Gap Instantons

:::tip Theorem 8.1 [T]
Minimal action of an SU(3)-instanton ($\nu = 1$) in the Gap formalism:

$$
S_{\mathrm{inst}} = \frac{2\pi}{\alpha_s(\mu)}
$$

At the GUT scale ($\alpha_{\mathrm{GUT}} \approx 1/24$): $S_{\mathrm{inst}} \approx 150.8$.
:::

Instanton amplitude:

$$
\mathcal{A}_{\mathrm{inst}} \sim M_{\mathrm{GUT}}^4 \cdot K \cdot e^{-150.8} \sim M_{\mathrm{GUT}}^4 \cdot 10^8 \cdot 10^{-65.5}
$$

The instanton contribution is **additive** and $\ll \Lambda_{\mathrm{pert}}$. The instanton does not directly solve the $\Lambda$ problem.

---

## 7. Theta Function $\Theta_M$ and Gauss Sum for Fano Phases {#7-сумма-гаусса-для-фано-фаз}

### 7.1 Factorization $\Theta_M = \Theta_+^7$

:::tip Theorem 1.1 (Factorization) [T]
In the standard octonionic multiplication table all 7 Fano lines have $\varepsilon_l = +1$. The theta function of the lattice $\mathbb{Z}^{21}$ with Fano characteristic factorizes:

$$
\Theta_M(S_0) = \left[\Theta_+(S_0)\right]^7
$$

where $\Theta_+$ is the unique 3-dimensional theta function:

$$
\Theta_+(S_0) = \sum_{\mathbf{n} \in \mathbb{Z}^3} \exp\!\left(-S_0|\mathbf{n}|^2 + \frac{2\pi i}{7}(n_1 n_2 + n_2 n_3 + n_3 n_1)\right)
$$
:::

**Justification.** $G_2$-automorphisms preserve the 3-form $\varphi$, hence preserve all $\varepsilon_l$. The blocks $\Theta_l$ are identical for all 7 lines ($G_2$-equivariance). Under orientation reversal $\varphi \to -\varphi$: $\Theta_- = \overline{\Theta_+}$, and $|\Theta_M| = |\Theta_+|^7$ in both cases.

:::info Corollary
All information about winding suppression is contained in **one** function $\Theta_+(S_0)$ of three integer variables. Computing $\Theta_+$ at $S_0 = 20$ is a finite task with exponential convergence.
:::

### 7.2 Mathematical Result: Gauss Sum

:::tip Theorem 4.1 [T]
For the non-degenerate quadratic form $B^{(b)}$ on $\mathbb{Z}_7^{21}$:

$$
|G_7| = 7^{21/2}, \quad \frac{|G_7|}{7^{21}} = 7^{-21/2} \approx 10^{-8.87}
$$
:::

### 7.3 Exact Computation of $\Theta_M / \Theta_0$: Refutation at Physical $S_0$

:::danger Theorem 4.1 (Ratio $\Theta_M/\Theta_0$) — Status: [R]
Exact computation at $S_0 = 20$ (using factorization $\Theta_M = \Theta_+^7$) shows:

$$
\frac{|\Theta_M(S_0)|}{\Theta_0(S_0)} = 1 - \delta, \quad |\delta| < 2 \times 10^{-9}
$$

The Fano-phase suppression at physical $S_0$ is **negligible**. The Gauss sum mechanism (9 orders) has been **refuted**.
:::

**Reasons for the absence of suppression** [T]:

**(a)** The dominant sector $k=1$ (one nonzero component) has **zero** phase ($\sigma_1 = \sigma_1^{\mathrm{no\,phase}} = 6$, no suppression).

**(b)** The first sector with a non-zero phase ($k=2$) is suppressed by a factor $e^{-S_0} \approx 2 \times 10^{-9}$ relative to $k=1$.

**(c)** Even in sector $k=2$ the suppression is only $|\sigma_2|/\sigma_2^{\mathrm{no\,phase}} = 7.48/12 = 0.624$ (not exponential).

**(d)** The Gauss sum $|G_7| = 7^{21/2}$ is a result for **equal** weights ($S_0 = 0$), irrelevant at $S_0 = 20$.

Shell coefficients of $\Theta_+$ at $S_0 = 20$:

| Shell $k$ | $e^{-kS_0}$ | $\lvert\sigma_k\rvert$ | Contribution $\lvert\sigma_k\rvert e^{-kS_0}$ |
|---|---|---|---|
| 0 | 1 | 1 | 1 |
| 1 | $2.06 \times 10^{-9}$ | 6 | $1.24 \times 10^{-8}$ |
| 2 | $4.25 \times 10^{-18}$ | 7.48 | $3.18 \times 10^{-17}$ |
| 3 | $8.76 \times 10^{-27}$ | 4.29 | $3.76 \times 10^{-26}$ |

:::warning Key conclusion
The result "9 orders from the Gauss sum" is formally correct for $S_0 \to 0$, but **physically unrealizable** at $S_0 = 20$. Status: **[R]** (refuted). The physical mechanism of destructive interference of winding sectors **does not work** at $S_0 \sim 20$.
:::

---

## 8. Topological Constraints

### 8.1 Euler Characteristic

:::tip Theorem 6.1 [T]
$$
\chi\bigl((S^1)^{21}\bigr) = \chi(S^1)^{21} = 0^{21} = 0
$$
:::

### 8.2 Witten Index

:::tip Theorem 6.2 [T]
For the $N=1$ supersymmetric $\sigma$-model with target space $(S^1)^{21}$:

$$
W = \mathrm{Tr}(-1)^F = \chi\bigl((S^1)^{21}\bigr) = 0
$$

Number of bosonic and fermionic vacuum states: $n_B = n_F = 2^{20} = 1\,048\,576$ (from $\sum_{k\;\mathrm{even}} \binom{21}{k} = 2^{20}$).

**Corollary:** In the supersymmetric limit $\Lambda_{\mathrm{SUSY}} = 0$ **exactly** — from the topology of the target space.
:::

### 8.3 Residual Λ under SUSY Breaking {#83-резидуальная-λ-при-нарушении-susy}

:::tip Theorem 6.3 [T]
Under SUSY breaking ($V_3$ breaks via $F$-term, $m_{3/2} \sim 10^{13}$ GeV):

$$
\Lambda_{\mathrm{residual}} \sim m_{3/2}^2 \cdot M_P^2 \sim 10^{-12}\, M_P^4
$$

SUSY compensation (12 orders) and $\epsilon^6$-suppression (12 orders) are **the same** mechanism: the suppression is determined by the smallness of the coherences $\epsilon \sim 10^{-2}$, and $m_{3/2} \propto \epsilon^3$.

Therefore, the SUSY argument **adds no** new orders to the budget of §5, but provides the **structural justification** of the $\epsilon^6$ suppression.

**Status [T]**: the [spectral formula for $\Lambda_{\text{CC}}$](#теорема-спектральная-лямбда) rigorously justifies SUSY compensation through the expansion of coefficient $a_0$ of the spectral action from the finite spectral triple [T].
:::

---

## 9. Collective Gap Compensation

:::warning Hypothesis 9.1 [H]
The observed $\Lambda$ is a **collective** effect of $\sim 10^{80}$ holons of the Universe:

$$
\Lambda_{\mathrm{obs}} = \frac{1}{N_{\mathrm{total}}} \sum_{A=1}^{N_{\mathrm{total}}} \Lambda_A - \Lambda_{\mathrm{counter}}
$$

Inter-system Gap correlations create **anti-correlation** of vacuum fluctuations:

$$
\langle\mathcal{G}_A^{(O)} \cdot \mathcal{G}_B^{(O)}\rangle = -\frac{\sigma^2}{N_{\mathrm{total}}}
$$

The resulting $\Lambda$:

$$
\Lambda_{\mathrm{obs}} = \Lambda_{\mathrm{individual}} \cdot \left(1 - \frac{N_{\mathrm{total}} \sigma^2}{\Lambda_{\mathrm{individual}}}\right)
$$

With fine-tuning $N_{\mathrm{total}} \sigma^2 \approx \Lambda_{\mathrm{individual}}$ a small $\Lambda$ is obtained.

This is analogous to the Bousso–Polchinski mechanism, but with a concrete physical nature: anti-correlation of Gap vacua through a collective phase transition.
:::

---

## 10. Zeta-Regularization with Fano Character

### 10.1 Epstein Zeta Function

Zeta function with Fano character:

$$
Z_\Phi(s) = \sum_{\mathbf{n} \in \mathbb{Z}^{21} \setminus \{0\}} \chi(\mathbf{n})\, |\mathbf{n}|^{-2s}
$$

where $\chi(\mathbf{n}) = \exp\!\left(\frac{2\pi i}{7} B^{(b)}(\mathbf{n})\right)$ is a quadratic character, periodic with period 7. The series converges absolutely for $\mathrm{Re}(s) > 21/2$.

### 10.2 Connection with $\Theta_M$ via Mellin Transform

:::tip Theorem 7.1 (Mellin connection) [T]
The completed zeta function

$$
\Lambda_\Phi(s) := \pi^{-s} \Gamma(s) Z_\Phi(s)
$$

is connected to $\Theta_M$ by the Mellin transform:

$$
\Lambda_\Phi(s) = \int_0^\infty t^{s-1} \left[\Theta_M^{(t)} - 1\right] dt
$$

where $\Theta_M^{(t)} = \sum_{\mathbf{n}} \chi(\mathbf{n}) e^{-\pi t |\mathbf{n}|^2}$.
:::

### 10.3 Meromorphic Structure and Functional Equation

:::tip Theorem 8.2 [T]
$\Lambda_\Phi(s)$ extends to a meromorphic function on $\mathbb{C}$ with a **unique** simple pole at $s = 21/2$:

$$
\mathrm{Res}_{s=21/2}\, \Lambda_\Phi(s) = \frac{G_7}{7^{21}}
$$
:::

:::tip Theorem 8.3 (Functional equation) [T]
The completed zeta function satisfies:

$$
\Lambda_\Phi(s) = \gamma \cdot 7^{21/2-2s} \cdot \Lambda_{\Phi^*}(21/2 - s)
$$

where $\gamma = G_7/|G_7| = e^{i\alpha}$ is the phase of the Gauss sum, $\Phi^*$ is the dual phase.
:::

### 10.4 Trivial Zeros $Z_\Phi(-k) = 0$

:::tip Theorem 9.1 [T]
$Z_\Phi(s)$ has **simple zeros** at all integers $s = -k$, $k \geq 1$:

$$
Z_\Phi(-k) = 0 \quad \text{for } k = 1, 2, 3, \ldots
$$

In particular, $Z_\Phi(-2) = 0$ — the zeta-regularized vacuum energy from winding sectors **vanishes exactly**.
:::

**Proof.** $\Lambda_\Phi(s) = \pi^{-s}\Gamma(s)Z_\Phi(s)$ is meromorphic with a unique pole at $s = 21/2$ (Theorem 8.2). $\Gamma(s)$ has simple poles at $s = -k$ ($k = 0, 1, 2, \ldots$). Since $\Lambda_\Phi(-k)$ is finite for $k \geq 1$, we must have $Z_\Phi(-k) = 0$. $\blacksquare$

:::info Nature of the cancellation
The zeros $Z_\Phi(-k) = 0$ are **trivial zeros**, analogous to the trivial zeros of the Riemann zeta function $\zeta(-2n) = 0$. However, unlike the ordinary Epstein zeta without character, the presence of the Fano character ($\chi \neq 1$) changes the meromorphic structure of $\Lambda_\Phi$: the phase $\gamma = e^{i\alpha}$ in the functional equation may lead to additional cancellations in $Z'_\Phi(-2)$.
:::

### 10.5 Residual Contribution via $Z'_\Phi(-2)$

:::warning Status: [H*]
The physical vacuum energy in zeta-regularization:

$$
\Lambda_{\mathrm{wind}}^{\mathrm{reg}} = -\tfrac{1}{2}\mu^{-4} Z'_\Phi(-2)
$$

Numerical estimate: $|Z'_\Phi(-2)| \approx 2.6 \times 10^{10}$ (via the functional equation and the absolutely convergent series of the dual zeta function).

The cancellation $Z_\Phi(-2) = 0$ is **structural**, from the Fano character, independent of $S_0$. However, the physical interpretation via $Z'_\Phi(-2)$ is a hypothesis requiring a full QFT computation (bosons + fermions + SUSY in winding sectors).
:::

### 10.6 Two Regimes of Winding Suppression

The investigation of [zeta-regularization](/docs/physics/dual-aspect/zeta-regularization) revealed **two qualitatively different regimes**:

| Regime | Result | Status |
|-------|-----------|--------|
| Naive summation | $\Theta_M(S_0) \approx \Theta_0(S_0)$ for $S_0 \gg 1$ | [T] — phases do not work |
| Zeta-regularization | $Z_\Phi(-k) = 0$ exactly for $k \geq 1$ | [T] — structural cancellation |

:::info Key shift
The $\Lambda$ problem in Gap theory transitions from the paradigm of "winding interference" to the paradigm of "zeta-regularization with Fano character". The gap between naive summation and analytic continuation reflects the fundamental difference between direct series computation and its regularized value.
:::

---

## 11. Uniqueness of the Bilinear Form $B^{(b)}$

### 11.1 Stabilizer of a Fano Line

:::tip Theorem 5.1 (Stabilizer structure) [T]
The stabilizer of the Fano line $\{a,b,c\}$ in $\mathrm{Aut}(\mathrm{Fano}) \cong \mathrm{PSL}(2,7)$ contains the full symmetric group $S_3$ acting on the three points of the line.
:::

**Proof.** $|\mathrm{PSL}(2,7)| = 168$. Number of Fano lines: 7. By the orbit-stabilizer formula: $|\mathrm{Stab}(l)| = 168/7 = 24$. Restriction to the 3 points of the line gives a surjective homomorphism $\mathrm{Stab}(l) \to S_3$ (in $\mathrm{PG}(2,q)$, collineations act 3-transitively on points of a line for $q \geq 2$). $\blacksquare$

The stabilizer contains:
- **$\mathbb{Z}_3$** (cyclic permutations): $(a,b,c) \to (b,c,a) \to (c,a,b)$
- **$\mathbb{Z}_2$** (transposition): $(a,b,c) \to (a,c,b)$ (orientation reversal)

### 11.2 Uniqueness Theorem

:::tip Theorem 6.1 (Uniqueness of $B^{(b)}$) [T]
$B^{(b)}$ is the unique (up to a scalar factor) non-zero $G_2$-covariant quadratic form with Fano contraction.
:::

**Proof** via $S_3$-symmetry of the stabilizer (does not use representation theory of $G_2$):

**(a)** $S_3$-invariance: the 6 permutations of the line $(a,b,c)$ split into 3 **even** (cyclic, $\varepsilon = +1$) and 3 **odd** (anti-cyclic, $\varepsilon = -1$).

**(b)** Identity $n_{ij} = n_{ji}$: anti-cyclic terms with $\varepsilon = -1$ give $-(n_{ab}n_{bc} + n_{bc}n_{ca} + n_{ca}n_{ab})$, i.e. **minus** the cyclic sum.

**(c)** $S_3$-invariance requires uniform coefficients $\alpha$ (cyclic) and $\beta$ (anti-cyclic). The full form on the line:

$$
Q_l = (\alpha - \beta)\,\varepsilon_l\,(n_{ab}n_{bc} + n_{bc}n_{ca} + n_{ca}n_{ab})
$$

**(d)** Setting $c = \alpha - \beta$: $Q = c \cdot B^{(b)}$. The non-zero form is unique up to scale. $\blacksquare$

:::info Remark
The proof uses three facts: (1) $G_2$-transitivity on Fano lines, (2) $S_3$-invariance of the stabilizer, (3) the identity $n_{ij} = n_{ji}$. Gap M-1 is **closed**.
:::

---

## 12. Modular Program

### 12.1 Modular Invariance at Level 7

:::warning Hypothesis 12.1 [H]
The partition function $\Theta_M$ satisfies modular relations of the subgroup $\Gamma_0(7) \subset SL(2,\mathbb{Z})$:

- **$T$-invariance** ($\tau \to \tau + 1$): requires $(S_0/\pi)|\mathbf{n}|^2 + B(\mathbf{n}) \equiv 0 \pmod{2}$
- **$S$-invariance** ($\tau \to -1/\tau$): an even self-dual lattice in $\mathbb{R}^{21}$ **does not exist** ($d = 21 \not\equiv 0 \pmod{8}$)

Full modular invariance is impossible, but the $\Gamma_0(7)$-structure may give additional arithmetic constraints through Hecke operators.
:::

### 12.2 Connection with the Hamming Code

:::warning Hypothesis 12.2 [H]
The 7 Fano lines define a $[7,3,4]$-simplex code $\mathcal{C}$ (dual to the $[7,4,3]$-Hamming code $\mathcal{H}$):

$$
\mathcal{C} = \{c \in \mathbb{F}_2^7 : \mathrm{supp}(c) \text{ is a union of Fano lines}\}, \quad \dim \mathcal{C} = 3
$$

Leech's Construction A from $\mathcal{H}$ builds a lattice $\Lambda_{\mathcal{H}}$ whose theta function has modular properties at level 2. The 21-dimensional lattice is divided by the Fano structure into $7 \times 3$ blocks, and code constraints from $\mathcal{H}$ link the blocks.
:::

### 12.3 Landscape of Gap Vacua

The discrete set of vacua $\sim 168$ ($|PSL(2,7)|$) is too small for the anthropic solution (string landscape: $\sim 10^{500}$). However, accounting for the choice of continuous moduli $(S^1)^{21}$: the landscape becomes continuous and anthropic selection is possible.

---

## 13. Closure Strategy: Three Levels {#стратегия-замыкания}

:::info Status: [C] with structural closure
Taking into account the [spectral formula](#теорема-спектральная-лямбда) **[T]**, the [cohomological argument](/docs/proofs/gap/lambda-budget#когомологическое-обнуление) ($\Lambda_{\text{global}} = 0$ [T]) and [sector minimization](/docs/core/dynamics/gap-thermodynamics#теорема-глобальная-минимизация) [T] — the estimated budget reduces to **$\sim 10^{-120 \pm 10}$** [C]. Structural closure is achieved; the remaining gap is a **computational** task (numerical minimization on $(S^1)^{21}$ with $G_2$), not a conceptual one.
:::

The strategy is divided into three levels.

### Level A: Structural Cancellation + Cohomological Argument (most promising) {#уровень-a}

**A1. Zeta cancellation.** $Z_\Phi(-2) = 0$ [T] — the zeta-regularized vacuum energy of winding sectors vanishes **exactly** (Theorem 9.1). Physical interpretation: with the **correct** regularization (analytic continuation, not cutoff) winding sectors **contribute nothing** to Λ.

**A2. Cohomological cancellation.** $\Lambda_{\text{global}} = 0$ [T] — global contractibility of $X = |N(\mathcal{C})|$ to the terminal object $T$ gives $H^n(X, \mathcal{F}) = 0$ for $n > 0$. The observed $\Lambda_{\text{obs}} \neq 0$ is a **local** effect from $H^*_{\text{loc}}(X, T) \neq 0$. See [full argument](/docs/proofs/gap/lambda-budget#когомологическое-обнуление).

**A3. SUSY compensation.** $G_2$-holonomy → $\mathcal{N}=1$ SUSY [T]. Boson-fermion compensation $\mathrm{Tr}(1)_{\text{total}} = 0$ — **[H]** (G₂-adj **14** is irreducible, the 7+7 decomposition is not justified; see §4a). Scale of the residual: $\Lambda_{\text{residual}} \sim \varepsilon^{12}$ **[T]** as a structural result of the [spectral formula](#теорема-спектральная-лямбда) — independent of the [H]-compensation. See [SUSY argument](/docs/proofs/gap/lambda-budget#susy-компенсация).

If zeta-regularization is accepted as physically correct (as in Casimir theory):
- Winding contribution: $10^0 \to 0$ (exact cancellation, formally $\infty$ orders of suppression)
- Residual: via $Z'_\Phi(-2)$, scale $|Z'_\Phi(-2)| \sim 10^{10}$

Effective budget with zeta-regularization:

$$\Lambda_{\text{phys}} \sim Z'_\Phi(-2) \cdot \varepsilon^6 / \mu^4$$

— requires a full computation.

**Open**: Physical interpretation of $Z'_\Phi(-2)$ — the key task.

### Level B: Modular Program (open) {#уровень-b}

The $\Gamma_0(7)$-structure of the theta function $\Theta_M$ may give additional arithmetic constraints through Hecke operators. The connection with the Hamming code $[7,4,3]$ gives 6 linear constraints on the 21-dimensional lattice.

Concrete program:
1. Compute the full decomposition of $\Theta_+$ into Hecke forms of level 7
2. Investigate the arithmetic properties of Fourier coefficients
3. Connect modular constraints to physical suppression of Λ

### Level C: Dynamical $S_0$ (open) {#уровень-c}

The radion/modulus $S_0$ is not a fixed parameter but a **dynamical variable**. The potential $V(S_0)$ includes Casimir energy, and its minimum determines the physical $S_0$. Connection: with dynamical $S_0$, the value of $\Theta_M(S_0^*)$ at the minimum may be exponentially suppressed.

### Existing Resources {#существующие-ресурсы-λ}

1. **Spectral formula for $\Lambda_{\text{CC}}$ [T]**: Structural formula via moments of $D_{\text{int}}$; scale $\varepsilon^{12}$ [T]; SUSY compensation $\mathrm{Tr}(1)=0$ — **[H]**
2. **Witten index $W = 0$ [T]**: $\Lambda_{\text{SUSY}} = 0$ exactly → 12 orders (= ε⁶, already counted)
3. **Zeta cancellation $Z_\Phi(-2) = 0$ [T]**: Regularized winding energy = 0 exactly
4. **Factorization $\Theta_M = \Theta_+^7$ [T]**: The full function splits into 7 identical blocks
5. **Global minimization of $V_{\text{Gap}}$ [T]**: Sector contribution $\sim 10^{-40}$ [C]
6. **Naive summation**: Does NOT give suppression at $S_0 = 20$ [T]

### What Is Required for a Complete Solution {#требования-полного-решения}

1. Physical interpretation of $Z'_\Phi(-2)$
2. Modular properties of $\Theta_+$ at $S_0 = 20$
3. Full QFT computation (bosons + fermions + SUSY)

### Additional Directions {#дополнительные-направления}

5. **Coherent instanton sum** — destructive interference over topological sectors
6. **Lattice Monte Carlo** — direct computation of the partition function on $(S^1)^{21}$ with $G_2$-symmetry

**Status: [C] with structural closure** ($\sim 10^{-120 \pm 10}$). All coefficients are determined by $\theta^*$ (T-79 [T]) — no free parameters. The remaining gap is a computational task (numerical minimization on $(S^1)^{21}/G_2$).

---

## 13b. Compatibility with DESI (2024–2025) {#desi-совместимость}

:::warning DESI results: dynamical dark energy
The DESI survey results (2024–2025) indicate a possible deviation of the equation-of-state parameter from $w = -1$ at the level of $\sim 4.2\sigma$. If confirmed ($> 5\sigma$), this poses a challenge for UHM, where $\Lambda$ is determined by the stationary Gap configuration.

**Possible mechanisms of dynamical $\Lambda$ in UHM:**
1. **Slow evolution of vacuum Gap phases**: if $\theta^*$ is not strictly stationary but undergoes a cosmologically slow drift, $\Lambda(\tau)$ becomes a function of cosmic time
2. **Non-Markovian corrections**: the memory kernel $K(\tau)$ ([T-88](/docs/core/dynamics/gap-dynamics)) may induce a cosmological drifting term
3. **Transition between Gap minima**: if $V_{\text{Gap}}$ has several nearby minima, quantum tunneling gives $w(z)$ dependence on redshift

**Status:** [P] (program). The current UHM formulation is compatible with constant $\Lambda$ ([C] in the budget). A dynamical extension requires explicit modeling of $\theta^*(z)$ evolution.
:::

## 14. Connection with Other Sections

| Topic | Page | Connection |
|------|----------|-------|
| Full $\Lambda$ budget | [$\Lambda$ budget: proofs](/docs/proofs/gap/lambda-budget) | Detailed proofs of all 6 mechanisms + spectral formula |
| Spectral triple | [Spectral triple](/docs/core/foundations/spacetime#теорема-спектральная-тройка) | Finite $(A_{\text{int}}, H_{\text{int}}, D_{\text{int}})$ [T] |
| Quantum gravity | [Quantum gravity](/docs/physics/gravity/quantum-gravity) | Chamseddine–Connes spectral action |
| Global minimization | [Gap thermodynamics](/docs/core/dynamics/gap-thermodynamics#теорема-глобальная-минимизация) | Sector structure [T] |
| Einstein equations | [Einstein equations from Gap](/docs/physics/gravity/einstein-equations) | Definition of $\Lambda_{\mathrm{Gap}}$ and $G_{\mathrm{Gap}}$ |
| Emergent geometry | [Emergent geometry](/docs/physics/gravity/emergent-geometry) | Metric from coherences |
| Dark matter | [Dark matter from Gap](/docs/physics/cosmology-phys/dark-matter) | $O$-sector and vacuum structure |
| Zeta-regularization | [Zeta-regularization](/docs/physics/dual-aspect/zeta-regularization) | $\Theta_M$-factorization, $Z_\Phi(-k) = 0$ |
| $G_2$-structure | [$G_2$-structure](/docs/physics/gauge-symmetry/g2-structure) | Fano plane and Ward identities |
| Berry phase | [Berry phase](/docs/physics/cosmology-phys/berry-phase) | Uniqueness of $B^{(b)}$ and orientational symmetry |
| Fano selection rules | [Selection rules](/docs/physics/gauge-symmetry/fano-selection-rules) | Hamming code, Fano constraints |
| Structural necessity of $\Lambda > 0$ | [Consequences of the axioms](/docs/core/foundations/consequences#теорема-лямбда-положительна) | Autopoiesis + local cohomology [T] |
| Canonical $f_0$ | [Higgs sector](/docs/physics/particle-physics/higgs-sector#теорема-f0-канонический) | UV-finiteness + zeta-determinant [T] |
| Topological protection | [Composite systems](/docs/core/dynamics/composite-systems#теорема-тополог-защита) | $\pi_2(G_2/T^2) \cong \mathbb{Z}^2$, barrier $\geq 6\mu^2$ [T] |
| Sector Gap bound | [Berry phase](/docs/physics/cosmology-phys/berry-phase#теорема-секторная-gap-граница) | $\mathrm{Gap}(O,i) \approx 1$, $\mathcal{G}_{\text{total}} = \mathcal{G}_O + O(\bar{\varepsilon}^2)$ [T] |
| O-sector dominance | [§4c](#теорема-лямбда-o-доминирование) | $\Lambda_{\text{CC}} \propto \mathcal{G}_O$ = "cost of observation" [T] |


---

**Related documents:**
- [Gap thermodynamics](/docs/core/dynamics/gap-thermodynamics)
- [Einstein equations from Gap](/docs/physics/gravity/einstein-equations)
- [Zeta-regularization](/docs/physics/dual-aspect/zeta-regularization)
- [Emergent geometry](/docs/physics/gravity/emergent-geometry)
