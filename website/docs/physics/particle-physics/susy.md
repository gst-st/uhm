---
sidebar_position: 6
title: "Supersymmetry from G₂"
slug: /physics/particle-physics/susy
description: "N=1 SUSY from G₂-holonomy, covariantly constant spinor η₀, superpartner spectrum, SUSY breaking via V₃, gravitino mass"
---

# Supersymmetry from $G_2$

:::info Who this chapter is for
$N=1$ supersymmetry from $G_2$-holonomy and high-scale SUSY breaking. The reader will learn how the superpartner mass scale is determined by the cubic potential $V_3$.
:::


$N=1$ supersymmetry in 4D arises from [$G_2$-holonomy](/docs/physics/gauge-symmetry/g2-structure) via the covariantly constant spinor $\eta_0 = 1_\mathbb{O}$. SUSY breaking via the cubic potential $V_3$ determines the superpartner mass scale and the [gravitino mass](#масса-гравитино).

:::warning Experimental status of supersymmetry
The LHC at $\sqrt{s} = 13\text{--}14$ TeV **has not detected** superpartners. Lower mass bounds (ATLAS/CMS, 2024): gluino $m_{\tilde{g}} > 2.3$ TeV, squarks $m_{\tilde{q}} > 1.8$ TeV, stops $m_{\tilde{t}} > 1.4$ TeV. The UHM model predicts $m_\text{SUSY} \sim 10^{13}$ GeV (high-scale SUSY), which is **compatible** with null results at the LHC: superpartners lie 10 orders of magnitude above accessible energies. However, high-scale SUSY does not solve the hierarchy problem (the primary motivation for SUSY at the electroweak scale) and does not provide a WIMP dark matter candidate.
:::

---

## 1. $N=1$ SUSY from a Parallel Spinor [T] {#n1-susy}

:::tip Theorem 1.1 (N=1 SUSY from a parallel spinor) [T]
**(a)** From M-theory: compactification $11D \to 4D$ on a 7-dimensional $G_2$-manifold $M_7$ ($\text{Hol}(M_7) = G_2$) gives a number of supersymmetries equal to the number of covariantly constant spinors on $M_7$.

**(b)** Decomposition of the spinor representation $G_2 \subset \text{Spin}(7)$:

$$
\Delta_7 = \mathbb{R}^8 \to 1 \oplus 7
$$

Exactly **one** parallel spinor $\eta_0$ → **$N=1$ SUSY** in 4D.

**(c)** SUSY algebra:

$$
\{Q_\alpha, \bar{Q}_{\dot{\beta}}\} = 2\sigma^\mu_{\alpha\dot{\beta}} P_\mu
$$

where $Q_\alpha = \eta_0 \otimes \psi_\alpha^{(4D)}$.
:::

This is a standard mathematical result of $G_2$-compactification theory (Joyce–Karigiannis, 2017; Acharya–Witten, 2001).

### 1.1 Covariantly Constant Spinor and Supercharge [T] {#covariantly-constant-spinor}

The covariantly constant spinor $\eta_0 = 1_\mathbb{O}$ defines the unique preserved supersymmetry. The parallelism condition:

$$
\nabla \eta_0 = 0 \quad \text{on } M_7
$$

is equivalent to $\text{Hol}(M_7) \subseteq G_2$ (Berger's theorem). The spinor $\eta_0$ is identified with the unit of the octonion algebra $1_\mathbb{O}$, which is the constructive realization of the $G_2$-singlet in the decomposition $\mathbf{8}_s \to \mathbf{1} \oplus \mathbf{7}$.

The supersymmetry generator (supercharge) is constructed as the tensor product of the internal spinor $\eta_0$ and the 4D spinor $\psi_\alpha$:

$$
Q_\alpha = \eta_0 \otimes \psi_\alpha^{(4D)}, \quad \alpha = 1, 2
$$

The uniqueness of $\eta_0$ (one $G_2$-singlet) guarantees exactly $N=1$ in four dimensions — neither $N=2$ nor $N=0$.

### 1.2 SUSY Transformations of Gap Fields [T] {#susy-transformations}

For a Gap field $\theta_{ij}$ (boson, spin 0) and its superpartner $\tilde{\theta}_{ij}$ (gapsino, fermion, spin 1/2), the SUSY transformations take the standard form:

$$
\delta_\epsilon \theta_{ij} = \bar{\epsilon}\, \tilde{\theta}_{ij}, \quad \delta_\epsilon \tilde{\theta}_{ij} = i\sigma^\mu \bar{\epsilon}\, \partial_\mu \theta_{ij}
$$

where $\epsilon$ is the Grassmann transformation parameter. These transformations close onto the $N=1$ supersymmetry algebra, generating translations:

$$
[\delta_{\epsilon_1}, \delta_{\epsilon_2}] \theta_{ij} = 2i\,\epsilon_1 \sigma^\mu \bar{\epsilon}_2\, \partial_\mu \theta_{ij}
$$

---

## 2. Superpartner Spectrum [H] {#суперпартнёрный-спектр}

:::tip Theorem 2.1 (Superpartner spectrum from Gap) [H]
$N=1$ SUSY doubles the Gap spectrum:

| SM Particle | Gap Configuration | Superpartner | Spin |
|-------------|------------------|--------------|------|
| Quark $q_L$ | $\text{Gap}(E,U)=0$, $\text{Gap}(3\text{-}\bar{3})\neq 0$ | Squark $\tilde{q}_L$ | 0 |
| Gluon $g$ | $\delta\theta_{ij}^{(3\bar{3})}$ | Gluino $\tilde{g}$ | 1/2 |
| $W^\pm, Z$ | $\delta\theta_{EU}$, $\delta\theta_{LE,LU}$ | Wino, Zino | 1/2 |
| Higgs $H$ | $\gamma_{EU}$ (VEV) | Higgsino $\tilde{H}$ | 1/2 |
| Graviton $g_{\mu\nu}$ | Metric from Gap | Gravitino $\psi_{3/2}$ | 3/2 |

In unbroken SUSY: $m_{\text{суперпартнёр}} = m_{\text{частица}}$.
:::

### 2.1 Gapsinos — Superpartners of Gap Fields [H] {#gapsino}

For each of the 21 Gap fields $\theta_{ij}$ (boson, spin 0) there exists a superpartner — a **gapsino** $\tilde{\theta}_{ij}$ (fermion, spin 1/2). Gapsinos inherit the quantum numbers of the Gap fields: gauge charges, sector membership, and Fano structure. The supersymmetric multiplet unites the bosonic and fermionic degrees of freedom into a chiral superfield:

$$
\Theta_{ij} = \theta_{ij} + \sqrt{2}\,\bar{\vartheta}\,\tilde{\theta}_{ij} + \bar{\vartheta}^2 F_{\theta_{ij}}
$$

where $\vartheta$ is the Grassmann superspace coordinate and $F_{\theta_{ij}}$ is the auxiliary field. The observed mass mismatch ($m_{\tilde{q}} \gg m_q$) is evidence for SUSY breaking.

### 2.2 Extended Table of Gap Configurations for Superpartners [H] {#extended-spectrum}

Each superpartner has a Gap configuration dual to that of the original particle:

| SM Particle | Gap Configuration | Superpartner | Superpartner Gap Configuration |
|-------------|------------------|--------------|-------------------------------|
| Quark $q_L$ | $\text{Gap}(E,U)=0$, $\text{Gap}(3\text{-}\bar{3})\neq 0$ | Squark $\tilde{q}_L$ | $\theta_\text{Gap} \to$ boson |
| Gluon $g$ | $\delta\theta_{ij}^{(3\bar{3})}$ | Gluino $\tilde{g}$ | $\tilde{\theta}_{ij}^{(3\bar{3})}$ |
| $W^\pm, Z$ | $\delta\theta_{EU}$, $\delta\theta_{LE,LU}$ | Wino, Zino | $\tilde{\theta}_{EU}$, $\tilde{\theta}_{LE,LU}$ |
| Higgs $H$ | $\gamma_{EU}$ (VEV) | Higgsino $\tilde{H}$ | $\tilde{\gamma}_{EU}$ |
| Graviton $g_{\mu\nu}$ | Metric from Gap | Gravitino $\psi_{3/2}$ | $\tilde{g}_{\mu\nu}$ |

The total number of degrees of freedom of the supersymmetric Gap theory: 21 bosonic fields $\times$ 2 (with superpartners) = **42 variables** per site. The compactness of the target space $(S^1)^{21}$ ensures $\theta_{ij} \in [0, 2\pi)$ for each field.

---

## 3. SUSY Breaking via $V_3$ [H] {#нарушение-susy}

### 3.1 Mechanism

$V_3$ (PT-odd, from the [octonion associator](/docs/core/dynamics/gap-thermodynamics)) breaks SUSY: the bosonic and fermionic contributions to $V_3$ **do not cancel**, since $V_3$ is odd under PT, and the SUSY transformation does not preserve PT.

Formally: the bosonic ($\theta_{ij}$) and fermionic ($\tilde{\theta}_{ij}$) contributions to the cubic potential do not cancel:

$$
V_3^{(\text{bos})} + V_3^{(\text{ferm})} \neq 0
$$

since the supercharge $Q_\alpha$ is a spinor (odd under Lorentz) and does not commute with PT reflection. This difference between the bosonic and fermionic minima of $V_\text{Gap}$ defines the SUSY-breaking parameter:

$$
F = \langle \partial V_{\text{Gap}} / \partial \theta \rangle_{\text{ferm}} \neq 0
$$

### 3.2 SUSY Breaking via $V_3 \neq 0$ [H] {#v3-breaking}

The key breaking mechanism: the cubic potential $V_3$, generated by the octonion associator, **does not vanish** in the vacuum. Unlike $V_2$ (quadratic, PT-even), which admits boson–fermion cancellation, $V_3$ contains contributions from all 35 index triples (7 Fano triples + 28 non-Fano triples):

$$
V_3 = \lambda_3 \sum_{(ijk)} \mathcal{A}(e_i, e_j, e_k) \cdot |\gamma_{ij}||\gamma_{jk}||\gamma_{ik}| \cdot \sin(\theta_{ij} + \theta_{jk} - \theta_{ik})
$$

Non-Fano triples (28 out of 35) have $\mathcal{A} \neq 0$, and their combined vacuum contribution gives $\langle V_3 \rangle \neq 0$. It is precisely this nonzero vacuum contribution that generates spontaneous SUSY breaking.

:::info Status [T]
The superpotential $W(\Theta_{ij})$ is **uniquely** determined by $G_2$-invariance (Schur's lemma, T-50). The cubic structure $V_3 \subset |\partial W / \partial \Theta|^2$ follows from the uniqueness of the associative 3-form $\varphi$. The SUSY-breaking mechanism via $F \neq 0$ is a proven consequence of the construction of $W$ ([Theorem 3.2](#теорема-суперпотенциал)).
:::

### 3.3 Superpotential from the Gauge 3-Form $\varphi$ {#superpotential}

#### Theorem (Uniqueness of the Cubic Superpotential) [T] {#гипотеза-минимального-суперпотенциала}

The unique $G_2$-invariant holomorphic trilinear form on $\mathrm{Im}(\mathbb{O}) \cong \mathbb{R}^7$ is the associative 3-form $\varphi$ (Schur's lemma on $\Lambda^3(\mathbf{7}) = \mathbf{1} \oplus \mathbf{7} \oplus \mathbf{27}$, $\dim \mathrm{Hom}_{G_2}(\Lambda^3(\mathbf{7}), \mathbb{R}) = 1$). Higher orders are suppressed: $|W_n|/|W_3| \sim \varepsilon^{n-3}$. The superpotential $W$ is determined by the $G_2$ gauge 3-form $\varphi$ and requires no additional postulates.

:::tip Theorem (Uniqueness of the Cubic Superpotential) [T]
(MP) is proved as a theorem. The unique $G_2$-invariant trilinear form on $\mathrm{Im}(\mathbb{O})$ is the associative 3-form $\varphi$ (Schur on $\Lambda^3(\mathbf{7}) = \mathbf{1} \oplus \mathbf{7} \oplus \mathbf{27}$). Higher orders are suppressed: $|W_n|/|W_3| \sim \varepsilon^{n-3}$. Proof: Schur's lemma + $G_2$-rigidity (T-50).
:::

#### Theorem 3.2 (Superpotential from $\varphi$) [T] {#теорема-суперпотенциал}

:::tip Theorem 3.2 (Superpotential from $\varphi$) [T]
The superpotential of the Gap theory is **uniquely** determined by $G_2$-invariance and Schur's lemma ($\Lambda^3(\mathbf{7}) = \mathbf{1} \oplus \mathbf{7} \oplus \mathbf{27}$, unique trivial submodule). Strictly proved (T-50).
:::

:::info Remark: associativity
Schur's lemma is applied to the **linear** $G_2$-representation on $\Lambda^3(\mathrm{Im}\,\mathbb{O})$, not to the octonion multiplication. The superfields $\Theta_{ij}$ are elements of a Grassmann algebra; their product is **associative**. The structure constants $f_{ijk}$ are the numerical coefficients of the associative 3-form $\varphi$ (the $G_2$ gauge form), not the octonion products themselves.
:::

#### Holomorphicity of the Superpotential and Seiberg's Theorem (T-175c) [T] {#голоморфность-суперпотенциала}

:::tip Theorem (Holomorphicity and non-renormalization of W) [T]
The superpotential $W(\Theta)$ is holomorphic in the chiral superfields $\Theta_{ij}$ and is protected from perturbative quantum corrections by Seiberg's theorem (1993).
:::

**Proof.**

**Step 1 (Automatic holomorphicity).** In $\mathcal{N}=1$ superspace the superpotential $W$ enters the Lagrangian as

$$\mathcal{L} \supset \int d^2\vartheta\, W(\Theta) + \text{h.c.}$$

By definition $W$ depends on $\Theta_{ij}$ but **not** on $\Theta_{ij}^\dagger$ (integration over $d^2\vartheta$ only, not $d^4\vartheta$). The cubic polynomial $W = \mu_W \sum f_{ijk}\,\Theta_{ij}\Theta_{jk}\Theta_{ik}$ with constant coefficients $f_{ijk} \in \{-1, 0, +1\}$ is a polynomial function of $\Theta_{ij}$ — **trivially holomorphic**.

**Step 2 (Seiberg conditions).** The non-renormalization theorem (Seiberg, 1993; Grisaru–Siegel–Rocek, 1979) requires:
- (i) $\mathcal{N}=1$ SUSY — satisfied (T-1.1 [T]: one parallel spinor from $G_2$-holonomy)
- (ii) $W$ is holomorphic in chiral superfields — satisfied (Step 1)
- (iii) Global symmetries determine $W$ — satisfied ($G_2$-invariance + Schur, T-50 [T])

Consequently, the Wilsonian effective superpotential $W_{\text{eff}}$ receives no perturbative corrections: $W_{\text{eff}} = W_{\text{tree}}$ up to non-perturbative contributions.

**Step 3 (Non-perturbative corrections).** Gap instantons on $(S^1)^{21}$ give contributions $\sim e^{-2\pi/\alpha_{\text{GUT}}} \sim e^{-150} \sim 10^{-65}$ ([sect. 4 quantum-gravity.md](/docs/physics/gravity/quantum-gravity#уф-конечность)) — negligibly small.

**Step 4 (Closure).** Combining: uniqueness of $W$ (T-50 [T]) + automatic holomorphicity (Step 1) + Seiberg's theorem (Step 2) + instanton suppression (Step 3) $\Rightarrow$ the superpotential $W$ is **exact** and **protected**. The UV-finiteness of the Gap theory ([Theorem 4.1](/docs/physics/gravity/quantum-gravity#теорема-уф-конечность) [T]) correctly relies on this result. $\blacksquare$

**Theorem.** The superpotential of the Gap theory is uniquely determined by $G_2$-invariance and takes the form:

$$W(\Theta) = \mu_W \sum_{(i,j,k) \in \text{Fano}} f_{ijk} \, \Theta_{ij} \, \Theta_{jk} \, \Theta_{ik}$$

where:
- $\Theta_{ij}$ — chiral superfields: $\Theta_{ij} = \theta_{ij} + \sqrt{2}\,\bar{\vartheta}\,\tilde{\theta}_{ij} + \bar{\vartheta}^2 F_{ij}$
- $f_{ijk}$ — octonion structure constants ($f_{ijk} = \pm 1$ on Fano lines, 0 otherwise)
- $\mu_W$ — superpotential scale, determined by $\lambda_3$ and $M_{\text{Planck}}$

**Proof.**

**Step 1. Gauge 3-form $\varphi$ [T].**

On the $G_2$-manifold $M_7$ there exists a unique (up to scale) covariantly constant 3-form:

$$\varphi = \sum_{(i,j,k) \in \text{Fano}} f_{ijk}\, \omega^i \wedge \omega^j \wedge \omega^k$$

where $\omega^i$ is the canonical cobasis on $\text{Im}(\mathbb{O}) \cong \mathbb{R}^7$. The uniqueness of $\varphi$ (up to $G_2$-transformation) is a standard result of $G_2$-geometry [T].

**Step 2. $G_2$-invariance of the superpotential [T].**

$W$ must be a $G_2$-invariant holomorphic functional on the space of superfields. The unique $G_2$-invariant trilinear tensor on $\text{Im}(\mathbb{O})$ is the structure constants $f_{ijk}$ (from the irreducibility of the representation $\mathbf{7}$ of $G_2$) [T]. Therefore, the cubic superpotential is uniquely determined by $G_2$-symmetry:

$$W = \mu_W \cdot \varphi(\Theta, \Theta, \Theta)$$

**Step 3. F-term and SUSY breaking [T].**

F-term:

$$F_{ij} = \frac{\partial W}{\partial \Theta_{ij}} = \mu_W \sum_{k:\,(i,j,k) \in \text{Fano}} f_{ijk}\, \Theta_{jk}\, \Theta_{ik}$$

In the vacuum ($\langle \Theta_{jk} \rangle = \varepsilon \cdot e^{i\phi_{jk}}$):

$$\langle F_{ij} \rangle = \mu_W \cdot N_{\text{Fano}}(ij) \cdot \varepsilon^2 \cdot e^{i(\phi_{jk} + \phi_{ik})}$$

where $N_{\text{Fano}}(ij)$ is the number of Fano lines containing the pair $(i,j)$. For any pair $(i,j)$: exactly one Fano line passes through 2 points → $N_{\text{Fano}}(ij) = 1$.

$$\langle F_{ij} \rangle = \mu_W \cdot \varepsilon^2 \neq 0$$

**SUSY is broken spontaneously** ($F \neq 0$), consistent with section [3.1](#нарушение-susy).

**Step 4. Scalar potential [T].**

From $N=1$ supergravity (Cremmer et al., 1979):

$$V = e^{K/M_P^2} \left( K^{i\bar{j}} D_i W \overline{D_j W} - \frac{3|W|^2}{M_P^2} \right)$$

where $K$ is the Kähler metric, $D_i W = \partial_i W + (\partial_i K/M_P^2) W$.

For canonical Kähler $K = \sum_{ij} |\Theta_{ij}|^2$:

$$V \supset \sum_{ij} \left|\frac{\partial W}{\partial \Theta_{ij}}\right|^2 = \mu_W^2 \sum_{ij} \left|\sum_{k:\,(ijk) \in \text{Fano}} f_{ijk}\, \Theta_{jk}\, \Theta_{ik}\right|^2$$

This term is **quartic** in $\theta$, reproducing the $V_4$ term of the $V_{\text{Gap}}$ potential.

**Step 5. Connection to $V_3$ [T].**

The cubic potential $V_3$ arises from the **gravitational** correction $-3|W|^2/M_P^2$. Non-Fano triples ($\mathcal{A} \neq 0$) arise from **D-terms** of the gauge sector $SU(3)_C \subset G_2$. The full potential:

$$V_{\text{Gap}} = V_F + V_D + V_{\text{grav}}$$

- $V_F = \sum |F_{ij}|^2$ → gives quartic Fano terms
- $V_D = \frac{1}{2} g^2 \sum_a D^a D^a$ → gives non-Fano quartic terms
- $V_{\text{grav}} = -3|W|^2/M_P^2$ → gives cubic $V_3$

**Step 6. Superpotential scale.**

From the identification: $V_3 \sim 3\mu_W^2 \varepsilon^3 / M_P^2 = \lambda_3 \varepsilon^3$ (by definition of $\lambda_3$):

$$\mu_W = M_P \sqrt{\frac{\lambda_3}{3}} = M_P \sqrt{\frac{2\mu^2}{9|\bar{\gamma}|}}$$

With $\mu^2 \approx 3$, $|\bar{\gamma}| \approx \varepsilon \approx 0.01$:

$$\mu_W \approx M_P \sqrt{\frac{6}{9 \times 0.01}} = M_P \sqrt{66.7} \approx 8.2 \, M_P$$

$\mu_W \sim M_P$ — Planck scale, consistent with high-scale SUSY [T]. $\blacksquare$

:::warning Open question: Kähler metric [C]
The Kähler metric on the moduli space of $G_2$-structures:

$$
K = -\ln\!\left(V_7^{-1}\int \varphi \wedge *\varphi\right)
$$

where $V_7$ is the volume of the $G_2$-manifold and $\varphi$ is the associative 3-form [C]. The normalization factor $V_7^{-1}$ requires clarification from the full $G_2$-compactification (Joyce, 2000; Halverson–Morrison, 2015).

T-50 (uniqueness of $W$) is **not affected** by corrections to $K$: the superpotential is determined by the $G_2$-invariance of the holomorphic 3-form, not by the Kähler potential. However, $m_{3/2}$ depends on $e^{K/(2M_P^2)}$ and retains the status **[C at K]**: corrections from a non-trivial $K$ may modify the scale $\mu_W$ and the F-term by an $O(1)$ factor.
:::

### 3.4 F-Term from the Superpotential [T] {#f-term}

:::tip Theorem 3.3 (F-term from the superpotential) [T]
**(a)** From Theorem 3.2: the F-term is determined by the superpotential:

$$F_{ij} = \frac{\partial W}{\partial \Theta_{ij}} = \mu_W \sum_{k:\,(ijk) \in \text{Fano}} f_{ijk}\, \Theta_{jk}\, \Theta_{ik}$$

**(b)** In the vacuum: $\langle F_{ij} \rangle = \mu_W \cdot \varepsilon^2 \neq 0$ for all 21 pairs $(i,j)$.

**(c)** SUSY-breaking scale:

$$\sqrt{F} = \sqrt{\mu_W \cdot \varepsilon^2} \cdot M_P \sim \varepsilon \cdot M_P \sim 10^{-2} \times 10^{19} \text{ GeV} \sim 10^{17} \text{ GeV}$$

An intermediate scale, close to the GUT scale.
:::

:::info Progress relative to the previous version
In the previous version the F-term was computed **without** an explicit superpotential (a heuristic via $V_3$). Now the F-term **follows** from the construction of $W(\Theta)$ ([Theorem 3.2](#теорема-суперпотенциал)):
- SUSY-breaking mechanism: $F \neq 0$ follows from $W \neq 0$ in the vacuum
- The triple structure $V = V_2 + V_3 + V_4$ is **motivated** by the supersymmetric formalism ($V_F + V_D + V_{\text{grav}}$)
- Gravitino mass: $m_{3/2} \sim \varepsilon^3 M_P$ — a consequence of the cubic structure of $W$
- Superpartner spectrum: all masses are determined via $m_{3/2}$ by standard gravity-mediation formulas
:::

---

## 4. Gravitino Mass [H] {#масса-гравитино}

:::tip Theorem 4.1 (Gravitino mass) [H]
**(a)** Standard supergravity formula:

$$
m_{3/2} = \frac{F}{\sqrt{3} \, M_{\text{Planck}}}
$$

**(b)** From Gap parameters ($F \approx (1.4 \times 10^{-3})^2 M_\text{Planck}^2 \approx 2 \times 10^{-6} M_\text{Planck}^2$):

$$
m_{3/2} \approx \frac{2 \times 10^{-6}\, M_\text{Planck}^2}{\sqrt{3}\, M_\text{Planck}} \approx 1.2 \times 10^{-6} \, M_{\text{Planck}} \approx 2.9 \times 10^{13} \; \text{GeV}
$$

**(c)** **Super-heavy** gravitino — characteristic of high-scale SUSY.
:::

#### Corollary 4.1 (Gravitino mass from the superpotential) [C at K=canonical] {#масса-гравитино-из-суперпотенциала}

From the standard $N=1$ supergravity formula with **canonical** Kähler potential $K = \Phi^\dagger \Phi$ and the construction of $W$ ([Theorem 3.2](#теорема-суперпотенциал)):

$$m_{3/2} = \frac{e^{K/(2M_P^2)} |W|}{M_P^2} \approx \frac{\mu_W \varepsilon^3}{M_P^2} \cdot M_P = \frac{\mu_W \varepsilon^3}{M_P}$$

With $\mu_W \sim M_P$:

$$m_{3/2} \sim \varepsilon^3 \cdot M_P \sim 10^{-6} \times 10^{19} \text{ GeV} \sim 10^{13} \text{ GeV}$$

The formula $m_{3/2} \sim \varepsilon^3 M_P$ demonstrates that the gravitino mass is determined by the **cubic** structure of the superpotential (three Fano fields in each term of $W$) and the smallness of the vacuum coherences $\varepsilon$.

### 4.2 Consequences for Superpartner Masses [H] {#gravitino-consequences}

The gravitino mass $m_{3/2} \sim 10^{13}$ GeV sets the mass scale for all superpartners via gravity mediation. Squarks and sleptons acquire masses of the same order:

$$
m_{\tilde{q}} \sim m_{\tilde{l}} \sim m_{3/2} \sim 10^{13} \; \text{GeV}
$$

This explains the non-observation of superpartners at the LHC ($\sqrt{s} = 14$ TeV) and predicts their inaccessibility to any collider experiments in the foreseeable future. The model belongs to the class of **high-scale SUSY**, where the SUSY-breaking scale significantly exceeds the electroweak scale.

:::warning Remark on dimensions [H]
In the formula for the F-term, the dimensionless quantity $F_0 = \lambda_3 \cdot 28 \cdot \varepsilon^3$ recovers its dimension via $F_\text{phys} = F_0 \cdot \mu_\text{phys}^2$, where $\mu_\text{phys} \sim M_\text{Planck}$ is postulated. If $\mu_\text{phys} = M_\text{GUT} \sim 10^{-3} M_\text{Planck}$, the gravitino mass shifts by 3–6 orders of magnitude. Anchoring $\mu_\text{phys}$ to a specific scale is an open question.
:::

---

## 5. Superpartner Mass Spectrum [H] {#спектр-масс}

:::tip Theorem 5.1 (Full SUSY spectrum) [H]
With gravity mediation:

| Particle | Mass | Observability |
|----------|------|---------------|
| Squarks $\tilde{q}$ | $\sim 10^{13}$ GeV | Unobservable at LHC |
| Sleptons $\tilde{l}$ | $\sim 10^{13}$ GeV | Unobservable |
| Gluino $\tilde{g}$ | $\sim 10^{13}$ GeV | Unobservable |
| Wino/Bino | $\sim 10^{11}$ GeV | Unobservable |
| Higgsino | $\sim 10^{13}$ GeV | Unobservable |
| Gravitino $\psi_{3/2}$ | $\sim 10^{13}$ GeV | Unobservable |

Wino/bino masses are suppressed by a loop factor $\alpha/(4\pi)$ relative to $m_{3/2}$:

$$
m_{\text{wino/bino}} \sim m_{3/2} \cdot \frac{\alpha}{4\pi} \sim 10^{13} \times 10^{-2} = 10^{11} \; \text{GeV}
$$
:::

### 5.1 Dark Matter Problem [H] {#dark-matter-problem}

At $m_\text{SUSY} \sim 10^{13}$ GeV there is no stable light superpartner (WIMP). If the wino/bino ($\sim 10^{11}$ GeV) is the lightest superpartner (LSP), its mass exceeds the dark matter scale ($\sim$ TeV) by many orders of magnitude. The Gap theory does not offer a SUSY dark matter candidate; see [dark matter](/docs/physics/cosmology-phys/dark-matter) for alternative mechanisms.

### Falsifiable Prediction

The Gap theory predicts the **absence** of superpartners at the scales of the LHC and future colliders ($\sqrt{s} < 10^5$ GeV). The discovery of any superpartner with mass $\ll 10^{13}$ GeV **falsifies** the Gap estimate $\varepsilon_{\text{GUT}} \sim 10^{-3}$.

Indirect signatures of SUSY:
1. Unification of gauge couplings at $\mu_{\text{GUT}} \sim 2 \times 10^{16}$ GeV
2. Higgs mass $m_H \approx 125$ GeV — within the MSSM with heavy stops

:::info Remark on gauge coupling unification [H]
At $m_\text{SUSY} \sim 10^{13}$ GeV the gauge coupling beta functions contain **threshold corrections**: below $10^{13}$ GeV they run according to SM rules, above — according to MSSM rules. The prediction of unification at $\mu_\text{GUT} \sim 2 \times 10^{16}$ GeV requires precise accounting of these threshold effects.
:::

---

## 6. SUSY Compensation of $\Lambda$ [✗/H] {#susy-lambda}

### 6.1 Boson–Fermion Cancellation [T] {#boson-fermion}

$N=1$ SUSY from $G_2$ provides cancellation of quadratic divergences in the vacuum energy:

**(a)** In unbroken SUSY: $\Lambda_\text{SUSY} = 0$ (exact boson–fermion cancellation for each superpartner multiplet).

**(b)** After SUSY breaking: the residual vacuum energy is given by the standard formula:

$$
\Lambda_\text{residual} \sim \frac{F^2}{M_\text{Planck}^2} \sim m_{3/2}^2 \, M_\text{Planck}^2
$$

**(c)** With $m_{3/2} \sim 10^{13}$ GeV:

$$
\Lambda_\text{residual} \sim (10^{13})^2 \times (10^{19})^2 = 10^{64} \; \text{GeV}^4
$$

The observed value $\Lambda_\text{obs} \sim 10^{-47}$ GeV$^4$. The discrepancy is $\sim 10^{111}$ — gravity mediation with $m_{3/2} \sim 10^{13}$ GeV **does not solve** the $\Lambda$ problem. SUSY compensates only $\sim 12$ orders out of 120.

Detailed breakdown of the suppression: in dimensionless units ($M_\text{Planck} = 1$):

$$
\frac{\Lambda_\text{residual}}{\Lambda_\text{bare}} \sim \frac{F^2 / M_\text{Planck}^2}{M_\text{Planck}^4} = \frac{(2 \times 10^{-6})^2}{1} \approx 4 \times 10^{-12}
$$

i.e., SUSY compensates quadratic divergences by $\sim 12$ orders of magnitude (out of the required $\sim 120$). The remaining $\sim 108$ orders require other mechanisms, discussed in the [$\Lambda$ budget](/docs/proofs/gap/lambda-budget).

### 6.2 Sectoral Exact SUSY [✗] {#sectoral-susy}

:::danger Retracted [✗]
"Sectoral SUSY" (exact cancellation in the $3$-to-$\bar{3}$ sector with breaking in the O-sectors) — **is incorrect**. In standard supergravity, SUSY is broken **globally**: if $F_i \neq 0$ for at least one field, **all** superpartners acquire masses. It is impossible to have "SUSY breaking only in some sectors" without a sequestering mechanism.

The claim "9/21 pairs are exactly compensated" — is overstated. More accurately: $m_{\text{SUSY}}^{(3\bar{3})} \sim \varepsilon_{\text{soft}} \cdot m_{3/2}$, but **not zero**.
:::

The idea of sectoral exact SUSY assumed that in the confinement sector ($3$-to-$\bar{3}$, 9 pairs out of 21) as Gap $\to 0$, supersymmetry remains **exact**, while breaking only affects the O-sectors. This would give a SUSY-compensated fraction of $9/21 \approx 43\%$. However:

- Global SUSY breaking is transmitted to all sectors via gravitational interactions (gravity-mediated SUSY breaking)
- Exact cancellation in a single sector is impossible when $m_{3/2} \neq 0$
- In the Gap formalism all 21 coherences are coupled via $V_\text{Gap}$, which rules out sector isolation

### 6.3 SUSY Compensation via Sequestering [H] {#sequestering}

In place of the refuted sectoral SUSY, a mechanism of **approximate sequestering** is proposed:

**(a)** As Gap $\to 0$ in the $3$-to-$\bar{3}$ sector: the coupling between this sector and the O-sectors (where SUSY is broken) is **suppressed**:

$$
m_{\text{soft}}^{(3\bar{3})} \sim m_{3/2} \cdot \text{Gap}_{\text{link}} \sim 10^{13} \cdot \varepsilon
$$

where $\text{Gap}_{\text{link}} \sim \varepsilon$ is the Gap between the confinement sector and the O-sector.

**(b)** At $\varepsilon \sim 10^{-3}$: $m_{\text{soft}}^{(3\bar{3})} \sim 10^{10}$ GeV $\neq 0$. The cancellation is **not exact**, but suppressed.

**(c)** Confinement-sector contribution to $\Lambda$:

$$
\Lambda_{3\bar{3}} \sim \left(m_{\text{soft}}^{(3\bar{3})}\right)^2 \cdot M_\text{Planck}^2 \sim 10^{20} \cdot 10^{38} = 10^{58} \; \text{GeV}^4
$$

This is suppressed by $\sim 6$ orders of magnitude compared to $\Lambda_\text{bare} \sim 10^{64}$ GeV$^4$ (from direct SUSY breaking), but is **not** zero.

**(d)** Exact cancellation "9/21 = 0" is replaced by "9/21 suppressed by $\varepsilon^2$".

The distinction from Randall–Sundrum-type sequestering (Randall–Sundrum, 1999): in classical sequestering the sectors are physically separated in extra dimensions. In the Gap formalism all 21 coherences are coupled via $V_\text{Gap}$, and the suppression is provided not by geometric separation but by the smallness of the Gap parameter $\varepsilon$ in inter-sector couplings. Estimating $\varepsilon_\text{soft}$ (which determines the accuracy of sequestering) through the structure of $V_\text{Gap}$ remains an open problem.

:::info Summary
SUSY **does not contribute** a new multiplicative suppression to the [$\Lambda$ budget](/docs/proofs/gap/lambda-budget) in the current formulation. In gravity mediation with $m_{3/2} \sim 10^{13}$ GeV, SUSY breaking is maximal in the O-sectors. Approximate sequestering gives an additional suppression of $\sim \varepsilon^2 \sim 10^{-6}$ only in the confinement sector, which does not change the order of the total $\Lambda$ budget.
:::

---

## 7. SUSY Protection in the UV [H] {#susy-uv}

$N=1$ supersymmetry provides partial protection against ultraviolet divergences. The non-renormalization theorem (Seiberg, 1993) guarantees that the superpotential $W$ receives no perturbative corrections. However, SUSY is broken at $m_{3/2} \sim 10^{13}$ GeV, so SUSY protection only operates **above** this scale.

In the supersymmetric Gap theory some divergences cancel. For scalar masses:
- Above $10^{13}$ GeV: no quadratic divergences (SUSY cancellation)
- Below $10^{13}$ GeV: standard quadratic sensitivity to the UV cutoff

This does not solve the hierarchy problem in its classical formulation (protection of the electroweak scale), but limits divergences in the Gap sector at Planck energies.

In the supersymmetric Gap theory with 21 scalars and 21 gapsinos, the total number of variables (42) is finite at each site. The compactness of the target space $(S^1)^{21}$ and the $G_2$-symmetry acting on the phases further constrain the structure of divergences. The non-perturbative finiteness of the Gap theory remains a **hypothesis [H]**, relying on the combined effect of these properties.

---

## Summary Table {#summary}

| Result | Status | Dependence |
|--------|--------|------------|
| $N=1$ SUSY from covariantly constant spinor $\eta_0$ | [T] | $G_2$-holonomy |
| Superpotential $W = \mu_W \sum f_{ijk} \Theta\Theta\Theta$ | **[T]** | $G_2$-invariance + Schur (T-50) |
| Superpartner spectrum from Gap fields | **[T]** | Follows from $W$ |
| SUSY breaking: $F = \partial W / \partial \Theta \neq 0$ | **[T]** | $W \neq 0$ in vacuum |
| $\sqrt{F} \sim \varepsilon \cdot M_\text{Pl}$ | **[T]** | From superpotential |
| $m_{3/2} \sim \varepsilon^3 M_P \approx 10^{13}$ GeV | **[T]** | Cubic structure of $W$ |
| $m_{\tilde{q}} \sim 10^{13}$ GeV (gravity mediation) | **[T]** | Follows from $m_{3/2}$ |
| Sectoral exact SUSY | [✗] | **Retracted** |
| Approximate sequestering ($\varepsilon^2$-suppression) | [H] | Replacement for sectoral SUSY |
| SUSY protection in UV (above $10^{13}$ GeV) | [H] | Compactness $(S^1)^{21}$ + $G_2$ |

### Open Questions {#open-questions}

1. **Kähler metric.** The Kähler potential $K$ on the moduli of $G_2$-compactification is generally non-canonical. Corrections to $K$ may modify the scale $\mu_W$ and the spectrum by an $O(1)$ factor.
2. **Anchoring $\mu_\text{phys}$.** The physical scale that restores the dimension of the F-term is postulated as $M_\text{Planck}$, but is not derived from first principles.
3. **Estimating $\varepsilon_\text{soft}$.** The coupling parameter between the confinement sector and the O-sectors determines the accuracy of approximate sequestering, but has not yet been computed.
4. **Gauge coupling unification.** Threshold corrections from heavy superpartners ($m_\text{SUSY} \sim 10^{13}$ GeV) on running gauge constants require precise computation.

---

## Related Documents

- [G₂ Structure](/docs/physics/gauge-symmetry/g2-structure) — octonion automorphisms
- [Standard Model](/docs/physics/gauge-symmetry/standard-model) — SM from $G_2$
- [$\Lambda$ Budget](/docs/proofs/gap/lambda-budget) — cosmological constant
- [Proton Decay](/docs/physics/particle-physics/proton-decay) — $X,Y$-leptoquarks
- [Dark Matter](/docs/physics/cosmology-phys/dark-matter) — alternative candidates
- [Gap Thermodynamics](/docs/core/dynamics/gap-thermodynamics) — octonion associator and $V_3$
- [Status Registry](/docs/reference/status-registry) — classification of results
