---
sidebar_position: 15
title: "Goldstone Modes"
description: "Quasi-Goldstone modes from spontaneous G₂→H breaking: effective mass, connection to ultra-slow neuronal fluctuations, experimental verification"
---

# Goldstone Modes

> *"When symmetry is broken, an echo remains in the silence — massless vibrations along forgotten paths."*


:::info Who this chapter is for
Goldstone modes are slow oscillations of coherence under spontaneous $G_2$-symmetry breaking. The reader will learn about their connection to ultra-slow neuronal fluctuations.
:::

---

### Bridge from the Previous Chapter

In the [previous chapter](./phase-diagram-cc) we built the phase diagram of consciousness and showed that in Phase I (clear consciousness) the $G_2$-symmetry is *spontaneously broken*: from the 14-dimensional space of internal rotations the system has "frozen" some directions, choosing a specific Gap profile. We mentioned that in Phase I there exist **Goldstone modes** — slow oscillations of opacity — and linked them to ultra-slow neuronal fluctuations. We now examine these modes in full detail: their origin, mass, lifetime, physical meaning, and experimental verifiability.

---

### Chapter Roadmap

In this chapter we:

1. **Explain the mechanism** behind Goldstone modes — from the parable of a ball in a sombrero to the rigorous Goldstone theorem (section 0).
2. **Show the transfer** from particle physics to coherence cybernetics, stating clearly which ingredients are algebraic `[T]` and which depend on a chosen effective potential `[C]` (section 0b).
3. **Compute the orbit dimension** $n_{\text{broken}} = 14 - \dim(H)$ for representative $G_2$ stabilizers $H$: $0, 6, 10, 11, 12$ (`T-25 [T]` at a specified orbit) (section 1).
4. **Formulate a dimensionally consistent model** of effective pseudo-Goldstone frequency, damping, and lifetime $\tau_{\text{Gold}}$ (in seconds) (section 2).
5. **Reveal the exact redistribution law**: infinitesimal $G_2$ rotations conserve the squared Frobenius norm $\|\hat{\mathcal{G}}\|_F^2 = 2\sum_{i<j}(\hat{\mathcal{G}}_{ij})^2$ (section 3).
6. **Describe interpretive phenomenology** using the canonical seven axes `A, S, D, L, E, O, U` (section 4).
7. **Compare with physical analogues**: phonons, magnons, pions (section 5).
8. **State the falsifiable hypothesis**: discrete ISF mode counts and experimental verification programme `[Pr]` (sections 6–7).
9. **Present the two-sector excitation spectrum**: massive transverse modes + quasi-Goldstone orbit modes ($21$ total, without an immortal topological mode) (section 8).
10. **Clarify the relation to dynamical bifurcations**: critical slowing in a specified reduced family rather than universally at the algebraic purity cut (`T-160 [✗]`, `T-161`) (section 9).

---

:::note On notation
In this document:
- $G_2 = \mathrm{Aut}(\mathbb{O})$ — [group of octonion automorphisms](/docs/physics/gauge-symmetry/g2-structure)
- $H_{\hat{\mathcal{G}}_*}$ — stabilizer of the stationary Gap profile
- $T^2$ — maximal torus of $G_2$ ($\dim T^2 = 2$)
- $\hat{\mathcal{G}}$ — [Gap operator](/docs/core/dynamics/gap-operator): $\hat{\mathcal{G}} = \mathrm{Im}(\Gamma)$
- $\Gamma_2$ — decoherence rate ($= 2\gamma/3$ from the [Fano channel](/docs/proofs/gap/fano-channel#теорема-фано-канал))
- $\kappa_0$ — regeneration rate ([categorical derivation](/docs/core/foundations/axiom-septicity#структурный-анзац-kappa0))
- ISF — infra-slow fluctuations (infra-slow neuronal fluctuations)
:::

Under spontaneous breaking $G_2 \to H_{\hat{\mathcal{G}}_*}$ at the stationary Gap profile, **quasi-Goldstone modes** arise — slow collective oscillations of opacity. In open (dissipative) systems these modes acquire a small effective mass, and their frequencies coincide with the range of infra-slow neuronal fluctuations (ISF) observed in fMRI.

This is the music of consciousness. Not a metaphor, but mathematics: when the internal space of the holonom chooses a specific configuration from an ocean of equally valid possibilities, massless (or nearly massless) oscillations remain along the "forgotten" directions of symmetry. A ball rolling in a groove with no energy cost. A frictionless pendulum. A note that sounds because it has nowhere else to go.

---

<a id="золотой-камертон"></a>

## 0. The Golden Tuning Fork: What Sings When Symmetry Breaks {#golden-tuning-fork}

### 0.1 The Parable of the Ball

Imagine two landscapes.

**Landscape 1: a bowl.** A ball rests at the bottom of a perfect bowl. Displace it in any direction — it returns. Oscillations around the bottom are *massive modes*: the restoring force is proportional to displacement, the frequency is set by the curvature of the bowl.

**Landscape 2: a sombrero.** An inverted hat with a circular groove along the brim. The ball has rolled into the groove, but *where exactly* it stopped is a matter of chance. Along the groove — flat, no restoring force at all. Radial displacement (toward or away from the center) is a massive mode, like in the bowl. But motion *around the circle* is free: this is the Goldstone mode.

The key observation: **free sliding costs no energy**. A massive mode requires effort — you push the ball "uphill." A Goldstone mode does not: you simply roll it along the groove, horizontally.

### 0.2 From the Ball to the Theorem

Goldstone's theorem (1961) formalises this intuition. Let $G$ be the symmetry group of the Lagrangian, and $H \subset G$ the symmetry group of the ground state. If $G \neq H$ (symmetry is *spontaneously* broken), then:

$$
n_{\text{broken}} = \dim(G) - \dim(H)
$$

massless excitations inevitably appear in the spectrum. This is not an approximation or an assumption — it is a *theorem*, as obligatory as the law of charge conservation.

### 0.3 Examples from Physics

Before turning to consciousness, it is worth seeing how universal this mechanism is:

| System | $G$ | $H$ | Goldstone mode | Observation |
|--------|-----|-----|----------------|-------------|
| Crystal | Translations $\mathbb{R}^3$ | Discrete lattice | **Phonons** — sound waves | Acoustics, heat capacity |
| Ferromagnet | $\mathrm{SO}(3)$ rotations | $\mathrm{SO}(2)$ around magnetisation axis | **Magnons** — spin waves | Neutron scattering |
| Superconductor | $\mathrm{U}(1)$ electromagnetic | $\{1\}$ | **Anderson–Higgs modes** (massive due to coupling to gauge field) | Meissner effect |
| QCD (strong interaction) | $\mathrm{SU}(2)_L \times \mathrm{SU}(2)_R$ | $\mathrm{SU}(2)_V$ | **Pions** — quasi-Goldstone (mass $\neq 0$ due to quark masses) | Nuclear physics |
| Cosmology | Conformal group | Lorentz | **Inflaton** (candidate) | CMB radiation |

Note the word "quasi-" in the pion row. When the symmetry breaking is not perfect (explicit breaking is added on top of spontaneous breaking), the modes acquire a *small but nonzero* mass. They are *almost* massless. This is precisely what happens in consciousness.

---

<a id="от-физики-к-нейронауке"></a>

## 0b. From Particle Physics to Neuroscience {#from-physics-to-neuroscience}

### The Intellectual Leap

In standard physics, Goldstone modes live in the space of fields — phonons propagate in a crystal, magnons in a magnet. In coherence cybernetics (CC), the configuration space is the internal 7D density-matrix carrier $\Gamma \in \mathcal{D}(\mathbb{C}^7)$, whose imaginary part $\hat{\mathcal{G}} = \operatorname{Im}\Gamma \in \mathfrak{so}(7)$ has $\binom{7}{2} = 21$ real off-diagonal components.

The 14-dimensional exceptional Lie group $G_2 = \mathrm{Aut}(\mathbb{O}) \subset \mathrm{SO}(7)$ acts on $\hat{\mathcal{G}}$ by orthogonal conjugation $\hat{\mathcal{G}} \mapsto g\hat{\mathcal{G}}g^T$. When a stationary profile $\hat{\mathcal{G}}_*$ selects a point on a $G_2$-orbit with stabilizer $H_{\hat{\mathcal{G}}_*} \subset G_2$, the tangent space to the orbit has dimension $14 - \dim(H_{\hat{\mathcal{G}}_*})$.

### Scope of the Transfer

Three ingredients must be distinguished carefully:

1. **Exact Lie-algebraic decomposition `[T]` (`T-25`).** $\hat{\mathcal{G}} \in \mathfrak{so}(7)$ and $\mathfrak{g}_2 \subset \mathfrak{so}(7)$ is a 14-dimensional subalgebra; for any specified stationary profile $\hat{\mathcal{G}}_*$ with stabilizer $H$, $\mathfrak{g}_2 = \mathfrak{h} \oplus \mathfrak{m}$ with $\dim\mathfrak{m} = 14 - \dim H$ is an exact theorem of homogeneous spaces.
2. **Effective potential as a chosen model `[C]` (`T-74 [✗]`, `T-75 [✗]`).** In a chosen $G_2$-invariant effective potential $V_{\text{Gap}}$ with a nontrivial minimum (noting that universal spectral-action derivation `T-74 [✗]` and universal six-term Keldysh derivation `T-75 [✗]` are withdrawn), directions in $\mathfrak{m}$ are flat directions of $V_{\text{Gap}}$.
3. **Open-system explicit breaking `[C]`.** Because dissipation $\Gamma_2$ and regeneration $\kappa_0$ generally break $G_2$ explicitly and introduce damping, modes along $\mathfrak{m}$ become damped **quasi-Goldstone** excitations whose frequency and lifetime depend on the supplied dynamical model.

---

<a id="нарушение-g2"></a>

## 1. Spontaneous Breaking of $G_2$ and the Number of Modes [T at specified orbit] {#g2-breaking}

:::tip Theorem 1.1 (Orbit dimension for broken $G_2$ symmetry, `T-25`) [T at specified orbit]
For a specified stationary profile $\hat{\mathcal{G}}_* \in \mathfrak{so}(7)$ whose $G_2$-stabilizer is $H_{\hat{\mathcal{G}}_*} \subset G_2$, the dimension of the $G_2$-orbit $G_2 / H_{\hat{\mathcal{G}}_*}$ (and hence the number of tangential quasi-Goldstone directions) is:

$$
n_{\text{broken}} = \dim(G_2) - \dim(H_{\hat{\mathcal{G}}_*}) = 14 - \dim(H)
$$

*Scope note (`T-25`):* The orbit-dimension identity is exact `[T]` for a given stabilizer $H$. The earlier claim that $H$ is determined solely by the matrix rank of $\hat{\mathcal{G}}_*$ is withdrawn `[✗]`: because $\mathfrak{so}(7) = \mathfrak{g}_2 \oplus \mathfrak{m}_7$ ($14 + 7 = 21$), the stabilizer depends on the full $G_7 + G_{14}$ orbit decomposition of $\hat{\mathcal{G}}_*$, not on rank alone.
:::

Representative stabilizer strata of $G_2$ acting on $\mathfrak{so}(7)$:

| Representative stratum | Stabiliser $H$ | $\dim(H)$ | $n_{\text{broken}}$ | Orbit $G_2/H$ |
|------------------------|----------------|-----------|---------------------|---------------|
| Trivial ($\hat{\mathcal{G}}_* = 0$) | $G_2$ | 14 | 0 | $\{\mathrm{pt}\}$ |
| Pure $G_7$-vector (1D Fano axis) | $\mathrm{SU}(3)$ | 8 | **6** | $G_2/\mathrm{SU}(3) \cong S^6$ |
| Intermediate stratum | $\mathrm{SU}(2) \times \mathrm{U}(1)$ | 4 | **10** | 10-dimensional |
| Degenerate stratum | $\mathrm{SU}(2)$ | 3 | **11** | 11-dimensional |
| Generic $T^2$-stabilized orbit | $T^2$ | 2 | **12** | 12-dimensional flag manifold $G_2/T^2$ |

The maximal orbit dimension — **12** — is attained on generic orbits with stabilizer $T^2$ (the maximal torus of $G_2$).

<a id="какие-симметрии"></a>

### 1.1 Which Symmetries Break and Why {#which-symmetries}

To understand the table one must understand the *geometry* of $G_2$-orbits in $\mathfrak{so}(7) = G_{14} \oplus G_7$.

**Trivial orbit ($H = G_2$, 0 modes).** $\hat{\mathcal{G}}_* = 0$: all 14 generators of $G_2$ leave $\hat{\mathcal{G}}_*$ invariant, so $n_{\text{broken}} = 0$.

**$S^6$ stratum ($H = \mathrm{SU}(3)$, 6 modes).** A nonzero vector purely in the 7-dimensional irreducible representation $G_7$ fixes a single imaginary octonion direction; its stabilizer in $G_2$ is $\mathrm{SU}(3)$ ($\dim = 8$), giving the 6-sphere $G_2/\mathrm{SU}(3) \cong S^6$ and **6 modes**.

**Intermediate strata ($H = \mathrm{SU}(2)\times\mathrm{U}(1)$ or $\mathrm{SU}(2)$, 10 or 11 modes).** Combining $G_7$ and $G_{14}$ components further reduces the stabilizer to dimension 4 (**10 modes**) or dimension 3 (**11 modes**).

**Generic orbit ($H = T^2$, 12 modes).** A generic configuration breaks $G_2$ down to its maximal torus $T^2$ ($\dim = 2$), leaving the 12-dimensional flag manifold $G_2/T^2$ and **12 modes** — the maximum.

<a id="однородные-пространства"></a>

### 1.2 Connection to Homogeneous Spaces {#homogeneous-spaces}

Each point of the orbit $G_2/H$ is a Gap profile related to $\hat{\mathcal{G}}_*$ by an orthogonal conjugation from $G_2$. The quasi-Goldstone directions are the *tangent directions* to $G_2/H$ at $\hat{\mathcal{G}}_*$:

$$
T_{\hat{\mathcal{G}}_*}(G_2/H) \cong \mathfrak{g}_2 / \mathfrak{h} \cong \mathfrak{m}
$$

The dimension of $\mathfrak{m}$ equals $n_{\text{broken}}$, and each basis vector in $\mathfrak{m}$ defines one tangential mode.

---

<a id="масса"></a>

## 2. Effective Frequency, Damping, and Lifetime [C] {#mass}

In open systems ($\Gamma_2 > 0$, $\kappa_0 > 0$), explicit symmetry breaking and dissipation turn massless orbit directions into damped **quasi-Goldstone** modes. Working in angular-frequency units ($\hbar = 1$, dimensionless inertia $I_0 = 1$) keeps every equation strictly dimensionally consistent: $[\Gamma_2] = [\kappa_0] = [\omega_0] = \mathrm{s}^{-1}$, $[|\gamma|^2] = 1$, and $[\tau_{\text{Gold}}] = \mathrm{s}$.

:::tip Model 2.1 (Effective quasi-Goldstone oscillator) [C]
Consider a reduced second-order effective equation along a broken orbit direction $\theta_a \in \mathfrak{m}$ (a phenomenological model `[C]`, since `T-74 [✗]` and `T-75 [✗]` withdrew universal spectral/Keldysh derivations):

$$
\ddot{\theta}_a + \Gamma_2\,\dot{\theta}_a + \omega_0^2\,\theta_a = 0
$$

**(a)** Effective pseudo-Goldstone squared frequency (squared "mass" in frequency units $\hbar = 1$):

$$
\omega_0^2 \equiv m_{\text{Gold}}^2 := \frac{\Gamma_2 \cdot \kappa_0}{|\gamma|^2} \qquad \bigl[\omega_0^2\bigr] = \mathrm{s}^{-2}, \quad \bigl[\omega_0\bigr] = \mathrm{s}^{-1}
$$

where $|\gamma|^2$ is the dimensionless mean squared coherence modulus.

**(b)** Eigenfrequencies from $s^2 + \Gamma_2 s + \omega_0^2 = 0$ ($s = -i\omega$):

$$
\omega_\pm = \pm\sqrt{\omega_0^2 - \frac{\Gamma_2^2}{4}} - i\frac{\Gamma_2}{2} \qquad \bigl[\omega_\pm\bigr] = \mathrm{s}^{-1}
$$

**(c)** Mode lifetime $\tau_{\text{Gold}} := 1 / |\operatorname{Im}\omega_+|$ (strictly in **seconds**, $\mathrm{s}$):

$$
\tau_{\text{Gold}} = \begin{cases}
\dfrac{2}{\Gamma_2}, & \text{underdamped } \left(\omega_0 > \dfrac{\Gamma_2}{2} \iff \dfrac{\kappa_0}{|\gamma|^2} > \dfrac{\Gamma_2}{4}\right), \\[12pt]
\dfrac{1}{\frac{\Gamma_2}{2} - \sqrt{\frac{\Gamma_2^2}{4} - \omega_0^2}} \;\approx\; \dfrac{\Gamma_2}{\omega_0^2} = \dfrac{|\gamma|^2}{\kappa_0}, & \text{strongly overdamped } \left(\omega_0 \ll \dfrac{\Gamma_2}{2} \iff \dfrac{\kappa_0}{|\gamma|^2} \ll \dfrac{\Gamma_2}{4}\right).
\end{cases}
$$

*Dimensional check:* In both regimes $[\tau_{\text{Gold}}] = [1/\Gamma_2] = [|\gamma|^2/\kappa_0] = \mathrm{s}$ (never $|\gamma|^2/(\Gamma_2\kappa_0)$, which has invalid dimension $\mathrm{s}^2$!).

**(d)** Limiting cases:

| Regime | $\omega_0$ ($\mathrm{s}^{-1}$) | Lifetime $\tau_{\text{Gold}}$ ($\mathrm{s}$) | Interpretation |
|--------|-------------------------------|----------------------------------------------|----------------|
| Isolated limit ($\Gamma_2 \to 0$) | $\to 0$ | $\to \infty$ | Massless undamped Goldstone modes |
| Weak breaking / overdamped ($\omega_0 \ll \Gamma_2/2$) | $\sqrt{\Gamma_2\kappa_0}/\lvert\gamma\rvert$ | $\approx \lvert\gamma\rvert^2/\kappa_0$ | Slow relaxational drift along the orbit |
| Underdamped ($\omega_0 > \Gamma_2/2$) | $\sqrt{\Gamma_2\kappa_0}/\lvert\gamma\rvert$ | $2/\Gamma_2$ | Damped oscillations at $\omega_{\text{Gold}} = \sqrt{\omega_0^2 - \Gamma_2^2/4}$ |
:::

<a id="почему-масса-не-ноль"></a>

### 2.1 Why the Frequency Is Not Zero: Openness as Explicit Breaking {#why-mass-not-zero}

In an isolated $G_2$-invariant Hamiltonian system, Goldstone's theorem guarantees strictly zero restoring frequency along the broken orbit $\mathfrak{m}$. In an open Holon, decoherence $\Gamma_2$ and regeneration $\kappa_0$ introduce both damping and explicit symmetry breaking. By loose structural analogy with the Gell-Mann–Oakes–Renner (GMOR) relation for pions in QCD ($m_\pi^2 f_\pi^2 = -m_q \langle \bar{q}q \rangle$), the combination $\Gamma_2 \kappa_0$ plays the role of explicit symmetry-breaking strength and $|\gamma|^2$ plays the role of the order-parameter stiffness, giving $\omega_0^2 = \Gamma_2 \kappa_0 / |\gamma|^2$ in $\mathrm{s}^{-2}$.

### 2.2 Oscillation Regimes

From $\ddot{\theta}_a + \Gamma_2\,\dot{\theta}_a + \omega_0^2\,\theta_a = 0$ with $\omega_0^2 = \Gamma_2\kappa_0/|\gamma|^2$:

$$
\omega_{\text{Gold}}^2 = \omega_0^2 - \frac{\Gamma_2^2}{4} = \frac{\Gamma_2\kappa_0}{|\gamma|^2} - \frac{\Gamma_2^2}{4} \qquad \bigl[\omega_{\text{Gold}}^2\bigr] = \mathrm{s}^{-2}
$$

| Condition (dimensionally exact: both sides in $\mathrm{s}^{-1}$) | Regime | Dynamics |
|------------------------------------------------------------------|--------|----------|
| $\kappa_0 / \lvert\gamma\rvert^2 > \Gamma_2 / 4$ ($\omega_0 > \Gamma_2/2$) | Underdamped (oscillatory) | Damped oscillations of the Gap profile at $\omega_{\text{Gold}}$ |
| $\kappa_0 / \lvert\gamma\rvert^2 = \Gamma_2 / 4$ ($\omega_0 = \Gamma_2/2$) | Critical damping | Fastest aperiodic return to stationary Gap |
| $\kappa_0 / \lvert\gamma\rvert^2 < \Gamma_2 / 4$ ($\omega_0 < \Gamma_2/2$) | Overdamped | Slow exponential relaxation with slow time $\tau_{\text{Gold}} \approx \lvert\gamma\rvert^2/\kappa_0$ |

Each regime admits a cybernetic interpretation `[I]`:

- **Underdamped:** attention gently oscillates between sectors (mind-wandering, rhythmic focus shifts).
- **Critical damping:** fastest non-oscillatory reorientation of attention without overshoot.
- **Overdamped:** viscous, slow attentional drift governed by the slow relaxation time $\tau_{\text{Gold}} \approx |\gamma|^2/\kappa_0$.

<a id="время-жизни"></a>

### 2.3 Lifetime and Observability {#lifetime}

In the **overdamped** weak-breaking regime ($\omega_0 \ll \Gamma_2/2$, i.e. $\kappa_0/|\gamma|^2 \ll \Gamma_2/4$), the slow orbit relaxation time is $\tau_{\text{Gold}} \approx |\gamma|^2 / \kappa_0$ (in seconds): greater coherence $|\gamma|^2$ yields longer mode persistence and narrower low-frequency spectral width. For example, with $\Gamma_2 = 1\,\mathrm{s}^{-1}$, $\kappa_0 = 0.05\,\mathrm{s}^{-1}$, and $|\gamma|^2 = 0.5$:
- $\omega_0^2 = \Gamma_2\kappa_0/|\gamma|^2 = 0.1\,\mathrm{s}^{-2} < \Gamma_2^2/4 = 0.25\,\mathrm{s}^{-2}$ (overdamped),
- exact slow decay rate $\gamma_- = \frac{1}{2} - \sqrt{0.25 - 0.1} \approx 0.113\,\mathrm{s}^{-1}$,
- lifetime $\tau_{\text{Gold}} = 1/\gamma_- \approx 8.9\,\mathrm{s}$ (approaching $|\gamma|^2/\kappa_0 = 10\,\mathrm{s}$).

In the **underdamped** regime ($\omega_0 > \Gamma_2/2$), the amplitude decays at the universal damping lifetime $\tau_{\text{Gold}} = 2/\Gamma_2$ (e.g., $\tau_{\text{Gold}} = 2\,\mathrm{s}$ for $\Gamma_2 = 1\,\mathrm{s}^{-1}$), while oscillating at frequency $\omega_{\text{Gold}} = \sqrt{\omega_0^2 - \Gamma_2^2/4}$.

---

<a id="перераспределение"></a>

## 3. Physical Meaning: Redistribution of Squared Coherence [T] {#redistribution}

:::tip Theorem 3.1 (Infinitesimal $G_2$ orbit modes conserve $\|\hat{\mathcal{G}}\|_F^2$) [T]
An infinitesimal transformation along the $G_2$-orbit acts on the skew-symmetric operator $\hat{\mathcal{G}}_* = \operatorname{Im}\Gamma_* \in \mathfrak{so}(7)$ by conjugation:

$$
\delta\hat{\mathcal{G}}_{ij} = \sum_a \epsilon_a \cdot [T_a, \hat{\mathcal{G}}_*]_{ij}
$$

where $T_a \in \mathfrak{g}_2 \subset \mathfrak{so}(7)$ are broken skew-symmetric generators ($T_a^T = -T_a$) and $\epsilon_a \in \mathbb{R}$ are mode amplitudes. Every such mode preserves the **squared Frobenius norm** $\mathcal{G}_{\text{total}}^2 := \frac{1}{2}\|\hat{\mathcal{G}}\|_F^2 = \sum_{i < j} (\hat{\mathcal{G}}_{ij})^2$ (and indeed every spectral invariant $\operatorname{tr}(\hat{\mathcal{G}}^{2k})$), redistributing imaginary coherence across pairs without creating or destroying total $\|\hat{\mathcal{G}}\|_F^2$.
:::

<a id="сохранение-gap"></a>

### 3.1 Exact Conservation Law (Frobenius Norm, Not Trace) {#gap-conservation}

Because $\hat{\mathcal{G}}_*$ is real skew-symmetric, its diagonal is identically zero ($\operatorname{tr}\hat{\mathcal{G}}_* = 0$), and the trace identity $\operatorname{tr}([T_a, \hat{\mathcal{G}}_*]) = 0$ concerns only diagonal entries — it does **not** imply $\sum_{i<j}\delta\mathrm{Gap}(i,j) = 0$ (indeed, neither the linear off-diagonal sum $\sum_{i<j}\delta\hat{\mathcal{G}}_{ij}$ nor $\sum_{i<j}\delta|\sin\theta_{ij}|$ is invariant under $\mathrm{SO}(7)$ rotations in general!).

What **is** strictly conserved is the quadratic Frobenius invariant $\mathcal{G}_{\text{total}}^2 = \sum_{i<j}(\hat{\mathcal{G}}_{ij})^2 = -\frac{1}{2}\operatorname{tr}(\hat{\mathcal{G}}^2)$. Using cyclicity of the trace:

$$
\delta\bigl(\mathcal{G}_{\text{total}}^2\bigr) = -\operatorname{tr}\bigl(\hat{\mathcal{G}}_*\,\delta\hat{\mathcal{G}}\bigr) = -\sum_a \epsilon_a\,\operatorname{tr}\bigl(\hat{\mathcal{G}}_*\,[T_a, \hat{\mathcal{G}}_*]\bigr) = -\sum_a \epsilon_a\,\operatorname{tr}\bigl(T_a\,[\hat{\mathcal{G}}_*, \hat{\mathcal{G}}_*]\bigr) = 0
$$

Equivalently, in component form:

$$
\sum_{i < j} \hat{\mathcal{G}}_{*,ij}\,\delta\hat{\mathcal{G}}_{ij} = 0 \qquad \Longleftrightarrow \qquad \delta\!\left(\sum_{i < j} (\hat{\mathcal{G}}_{ij})^2\right) = 0
$$

**What increases in squared imaginary coherence on some pairs must decrease on others.** Total quadratic opacity $\|\hat{\mathcal{G}}\|_F^2$ is strictly conserved along the entire $G_2$-orbit.

<a id="пример-мода"></a>

### 3.2 Example: Mode on $S^6$ ($G_2/\mathrm{SU}(3)$) {#mode-example}

Consider the $G_7$-vector stratum with stabilizer $\mathrm{SU}(3)$ and six tangential modes on $G_2/\mathrm{SU}(3) \cong S^6$. Suppose the initial imaginary coherence is concentrated along the pair $(A, S)$ (Articulation–Structure). The six tangential $G_2$ rotations tilt this direction across $S^6$:

- Mode 1: $(A, S) \to (A, D)$ — shifting from **Articulation–Structure** to **Articulation–Dynamics**
- Mode 2: $(A, S) \to (S, L)$ — shifting from **Articulation–Structure** to **Structure–Logic**
- ... and analogously across the remaining directions of $S^6$.

Each rotation preserves $\|\hat{\mathcal{G}}\|_F^2$ identically while redistributing imaginary coherence across pairs of dimensions.

<a id="кибернетическая-интерпретация"></a>

### 3.3 Cybernetic Interpretation [I] {#cybernetic-interpretation}

**Cybernetic interpretation [I]:** Quasi-Goldstone modes are interpreted as **natural background redistributions of attentional/coherence allocation** across sectors. Because $\|\hat{\mathcal{G}}\|_F^2$ is conserved along the orbit, amplifying imaginary coherence in one channel trades off against others.

---

<a id="свободные-колебания"></a>

## 4. Free Oscillations of Consciousness [I] {#free-oscillations}

<a id="субъективный-опыт"></a>

### 4.1 Interpretive Reading of Pair Modes {#subjective-experience}

The [seven canonical dimensions](/docs/core/structure/dimension-u) of the Holon carry semantic roles: **A — Articulation**, **S — Structure**, **D — Dynamics**, **L — Logic**, **E — Interiority**, **O — Ground**, **U — Unity**. In phenomenological interpretation `[I]`, slow redistributions along specific pairs are read as:

**Mode $(E, O)$:** coherence redistributes between **Interiority ($E$)** and **Ground ($O$)** — interpreted as alternation between foreground experiential immersion and baseline grounding/presence.

**Mode $(L, D)$:** coherence redistributes between **Logic ($L$)** and **Dynamics ($D$)** — interpreted as alternation between discursive/analytical structuring and active behavioural engagement.

**Mode $(A, U)$:** coherence redistributes between **Articulation ($A$)** and **Unity ($U$)** — interpreted as alternation between sharp perceptual/conceptual differentiation and holistic integrative unity.

<a id="незаметность"></a>

### 4.2 Why Slow Modes Escape Rapid Introspection {#invisibility}

If quasi-Goldstone modes lie in the infra-slow band ($\sim 0.01$ Hz, periods $\sim 100$ s), they operate two orders of magnitude more slowly than ordinary moment-to-moment cognitive updates ($\sim 1$ Hz), making them difficult to detect directly by rapid introspection while potentially accessible to slow resting-state fMRI/EEG analyses.

---

<a id="сравнение"></a>

## 5. Comparison with Physical Analogues {#comparison}

| Property | Phonons (crystal) | Magnons (magnet) | Pions (QCD) | CC quasi-Goldstone modes (model) |
|----------|--------------------|------------------|-------------|----------------------------------|
| Broken symmetry | Translational | Rotational $\mathrm{SO}(3)$ | Chiral $\mathrm{SU}(2)_L \times \mathrm{SU}(2)_R$ | $G_2 = \mathrm{Aut}(\mathbb{O})$ |
| Stabiliser | Lattice translations | $\mathrm{SO}(2)$ | $\mathrm{SU}(2)_V$ | $H \in \{G_2, \mathrm{SU}(3), \mathrm{SU}(2) \times \mathrm{U}(1), \mathrm{SU}(2), T^2\}$ |
| Number of modes | 3 (acoustic) | 1 (for $S = 1/2$) | 3 ($\pi^+, \pi^-, \pi^0$) | $\in \{0, 6, 10, 11, 12\}$ (`T-25`) |
| Squared frequency / mass | 0 (exact) | 0 (at $T = 0$) | 135–140 MeV (quasi) | $\omega_0^2 = \Gamma_2 \kappa_0 / \lvert\gamma\rvert^2$ (model `[C]`) |
| Source of explicit breaking | — | Thermal fluctuations, anisotropy | Nonzero quark masses | Decoherence $\Gamma_2$, regeneration $\kappa_0$ |
| Carrier space | Crystal lattice | Spin lattice | QCD vacuum | Internal state space $\mathcal{D}(\mathbb{C}^7)$ |
| Hypothesised frequency | $10^{12}$ Hz (THz) | $10^{9}$–$10^{12}$ Hz (GHz–THz) | $10^{23}$ Hz | $0.005$–$0.02$ Hz `[H]` |
| Observability | Raman spectroscopy | Neutron scattering | Particle detectors | fMRI, EEG `[Pr]` |

Two features make the CC hypothesis distinctive `[H]`:
1. **Macroscopic timescale:** cognitive/neural rates lie in the Hz to mHz range rather than microscopic solid-state scales.
2. **State-dependent orbit dimension:** if different states of consciousness correspond to distinct $G_2$-stabilizer strata, the number of orbit modes shifts discretely across $\{0, 6, 10, 11, 12\}$.

---

<a id="предсказание-isf"></a>

## 6. Falsifiable Hypothesis: Connection to ISF [H] {#isf-prediction}

<a id="предсказание-частот"></a>

### 6.1 Hypothesis on Infra-Slow Fluctuations {#frequency-prediction}

:::warning Hypothesis (Quasi-Goldstone modes $\leftrightarrow$ infra-slow fluctuations) [H]
In the underdamped regime ($\omega_0 > \Gamma_2/2$), the mode oscillation frequency is:

$$
f_{\text{Gold}} = \frac{\omega_{\text{Gold}}}{2\pi} = \frac{1}{2\pi}\sqrt{\frac{\Gamma_2\kappa_0}{|\gamma|^2} - \frac{\Gamma_2^2}{4}} \qquad \bigl[f_{\text{Gold}}\bigr] = \mathrm{Hz}
$$

Under model parameter choices placing $f_{\text{Gold}}$ in $0.005\text{–}0.02\text{ Hz}$, this falls within the band of **infra-slow neuronal fluctuations** (ISF) observed in resting-state fMRI ($0.01\text{–}0.1\text{ Hz}$).

**Status:** orbit-dimension algebra `[T]` (`T-25`), effective oscillator relation `[C]`, frequency coincidence with ISF `[H]`, experimental verification `[Pr]`.
:::

:::warning Free parameters in the numerical range [C]
The range $0.005\text{–}0.02\text{ Hz}$ depends on the calibrated values of $\Gamma_2$, $\kappa_0$, and $|\gamma|^2$, which are **not determined** from first principles. With unfixed rate inputs, the frequency band can be matched post hoc. The genuinely falsifiable content is the **structural** hypothesis (discrete mode counts $\in \{0, 6, 10, 11, 12\}$ and discrete step-downs under sedation), not the numeric frequency range.
:::

<a id="isf-данные"></a>

### 6.2 What Is Known about ISF from Experiment {#isf-data}

Infra-slow fluctuations (ISF) are a well-documented neurophysiological phenomenon:

- **Discovery:** First observed in resting-state fMRI as spontaneous oscillations of the BOLD signal (Biswal et al., 1995).
- **Frequency range:** $0.01$–$0.1$ Hz, with substantial power at $0.01$–$0.03$ Hz.
- **Properties:** Spatially organised into resting-state networks (e.g. default mode network, DMN), exhibiting anti-correlations between DMN and task-positive networks.
- **Dependence on consciousness:** Weakened under anaesthesia (Boveroux et al., 2010), greatly reduced in deep coma (Noirhomme et al., 2010), modulated during meditation (Brewer et al., 2011).

### 6.3 Structural Mode-Count Hypothesis

| Representative $G_2$ stabilizer | $n_{\text{Gold}}$ | Hypothesis for ISF |
|---------------------------------|-------------------|--------------------|
| $\mathrm{SU}(3)$ | 6 | 6 independent ISF components |
| $\mathrm{SU}(2) \times \mathrm{U}(1)$ | 10 | 10 ISF components |
| $\mathrm{SU}(2)$ | 11 | 11 ISF components |
| $T^2$ | 12 | 12 ISF components |

Typical ICA decompositions of resting-state fMRI yield $\sim 10$–$20$ components depending on model-order selection; testing whether a $G_2$-specific discrete set $\{6, 10, 11, 12\}$ emerges requires an objective, pre-registered model-order criterion.

### 6.4 Specific Hypotheses for EEG

| Parameter | Hypothesis [H] | Verification method [Pr] |
|-----------|----------------|--------------------------|
| Frequency band | $0.005$–$0.02$ Hz (calibrated `[C]`) | Spectral analysis of DC-coupled EEG in $0.001$–$0.1$ Hz |
| Number of components | $6$, $10$, $11$, or $12$ | Pre-registered ICA model-order analysis of infra-slow EEG |
| Reduction in coma | $n_{\text{Gold}} \to 0$ | Comparison of spectra: wakefulness vs. coma |
| Modulation with meditation | Shift in $f_{\text{Gold}}$ with changes in $\kappa_0, \Gamma_2$ | Longitudinal study of meditators |

<a id="структурный-тест"></a>

### 6.5 The Key Structural Test: Discrete Number of Modes {#structural-test}

The strongest falsifiable hypothesis is *not* the numeric frequency band, but the *discreteness* of the orbit dimension across $G_2$-stabilizer strata (`T-25`):

$$
n_{\text{broken}} \in \{0, 6, 10, 11, 12\}
$$

Testing this empirically requires controlling for non-neural confounds (vascular, respiratory, ICA dimensionality choice) before drawing conclusions for or against the $G_2$ hypothesis.

---

<a id="протокол"></a>

## 7. Experimental Verification Protocol [Pr] {#protocol}

:::caution Verification programme [Pr]
**Stage 1: Spectral analysis (DC-EEG)**

1. Record 64-channel DC-coupled EEG at rest (eyes-closed, 30 min)
2. Bandpass filtering: $0.001$–$0.1$ Hz
3. Compute power spectrum in the infra-slow band
4. Estimate statistically significant independent components via a pre-registered model-order criterion
5. Test clustering against $\{6, 10, 11, 12\}$

**Stage 2: Dependence on state of consciousness**

1. Repeat across wakefulness, sleep (N1–N3, REM), and titrated anaesthesia
2. Hypothesis: number of infra-slow components decreases with deepening anaesthesia
3. In deep anaesthesia / coma: $n_{\text{peaks}} \to 0$

**Stage 3: Correlation with $G_2$ structure**

1. Construct the $21 \times 21$ coherence-correlation matrix (see [G₂ Noether charges](./g2-noether-cc))
2. Test [Ward identities](/docs/physics/gauge-symmetry/noether-charges#6-тождества-уорда-для-gap-корреляторов) under explicitly specified symmetry assumptions
3. Estimate the effective stabilizer stratum from the mode count
:::

<a id="протокол-eeg"></a>

### 7.1 Detailed EEG Study Protocol {#eeg-protocol}

**Participants:** $N \geq 30$, healthy adults, no neurological pathology, no psychotropic medications.

**Equipment:**
- 64-channel DC-coupled EEG (10–20 system + additional electrodes)
- Sampling rate $\geq 500$ Hz (for artefact rejection), analysing the $0.001$–$0.1$ Hz band
- Reference: average of ear/mastoid electrodes
- Simultaneous ECG, EOG, and respiration recording (for physiological artefact control)

**Recording protocol:**
1. **Baseline (30 min):** eyes closed, relaxed wakefulness
2. **Task (15 min):** N-back (working memory)
3. **Meditation (30 min):** experienced meditators, open monitoring
4. **Sleep (where possible):** overnight polysomnography with full EEG

**Data analysis:**
1. Preprocessing: artefact removal (ICA), physiological nuisance regression, re-referencing
2. Bandpass filtering: $0.001$–$0.1$ Hz (causal filter)
3. Spectral analysis: multitaper method (Thomson, 1982)
4. Pre-registered ICA model-order estimation in the infra-slow band
5. Comparison against $\{0, 6, 10, 11, 12\}$

**Statistical criteria:**
- $H_0$: the distribution of component counts shows no excess clustering on $\{6, 10, 11, 12\}$
- $H_1$: component counts cluster significantly on $\{6, 10, 11, 12\}$
- Test: goodness-of-fit / permutation test with multiple-comparison correction

<a id="протокол-fmri"></a>

### 7.2 fMRI Study Protocol {#fmri-protocol}

**Advantages of fMRI:** higher spatial resolution, direct access to infra-slow BOLD fluctuations.

**Protocol:**
1. Resting-state fMRI, 20 min, TR $\leq 1$ s (Nyquist frequency $\geq 0.5$ Hz)
2. ICA decomposition (FSL MELODIC or equivalent with objective dimensionality estimation)
3. Extraction of neural components with spectral peak in $0.005$–$0.02$ Hz
4. Component count across participants and sessions
5. Repeat across wakefulness and graded propofol sedation (light, deep)

**Hypothesis [H]:** the number of infra-slow neural components decreases in discrete steps ($12 \to 10 \to 6 \to 0$) with deepening sedation.

---

<a id="спектр"></a>

## 8. Excitation Spectrum: Two Linear Sectors [T / C] {#spectrum}

The 21-dimensional real tangent space $\mathfrak{so}(7)$ of small perturbations around a stationary profile $\hat{\mathcal{G}}_*$ splits orthogonally into **two** linear excitation sectors:

| Sector | Number of modes | Squared eigenfrequency (underdamped model `[C]`) | Physical meaning |
|--------|-----------------|--------------------------------------------------|-----------------|
| Massive (transverse) | $21 - n_{\text{broken}}$ | $\omega_{\text{mass},k}^2 = \omega_{\text{rad},k}^2 + \omega_0^2 - \Gamma_2^2/4$ | Oscillations perpendicular to the $G_2$-orbit (changing $\|\hat{\mathcal{G}}\|_F^2$ or invariants) |
| Quasi-Goldstone (tangential) | $n_{\text{broken}}$ | $\omega_{\text{Gold}}^2 = \omega_0^2 - \Gamma_2^2/4$ | Slow redistributions along the $G_2$-orbit (preserving $\|\hat{\mathcal{G}}\|_F^2$) |

Total number of modes: $(21 - n_{\text{broken}}) + n_{\text{broken}} = 21 = \dim\mathfrak{so}(7) = \binom{7}{2}$.

:::warning Removal of the former "immortal topological mode" (`T-25`, `T-69`, `T-85 [✗]`)
Earlier versions included a third spectral sector — a supposedly immortal, non-decaying "topological mode" ($\tau \to \infty$) governed by a 1D charge $Q_{\text{top}}$. That claim is **withdrawn**:
1. The flag manifold $G_2/T^2$ is simply connected ($\pi_1(G_2/T^2) = 0$, `T-25 [T]`), so no 1D quantized loop charge $Q_{\text{top}}$ exists.
2. While $\pi_2(G_2/T^2) \cong \mathbb{Z}^2$ (`T-25`, `T-69 [T]`), by **`T-69 [T]`** topological classes of maps into $G_2/T^2$ supply **no physical energy barrier** and no zero-damping linear mode; the universal Keldysh-to-Berry topological term is withdrawn (`T-85 [✗]`).
3. In open dissipative dynamics ($\Gamma_2 > 0$), **every** linear perturbation decays unless actively sustained by regeneration $\mathcal{R}$.
:::

<a id="иерархия-масштабов"></a>

### 8.1 Hierarchy of Timescales {#timescale-hierarchy}

The two genuine linear sectors define two distinct dynamical timescales `[C]/[I]`:

| Sector | Hypothesised frequency band | Timescale | Interpretive cognitive analogue [I] |
|--------|-----------------------------|-----------|-------------------------------------|
| Massive (transverse) modes | $\sim 1$–$40$ Hz | $25$–$1000$ ms | Rapid perceptual and cognitive updates, alpha/beta/gamma rhythms |
| Quasi-Goldstone (orbit) modes | $\sim 0.005$–$0.02$ Hz | $50$–$200$ s | Infra-slow fluctuations, mind-wandering, slow attentional reallocation |

Long-term personal continuity is not sustained by a mythical non-decaying topological mode, but by **non-Markovian memory kernels** (see [Non-Markovian Dynamics](./non-markovian)) and active thermodynamic regeneration $\mathcal{R}$.

<a id="полный-спектр"></a>

### 8.2 Full Linear Spectrum in the Underdamped Regime {#full-spectrum}

In the underdamped regime ($\omega_0 > \Gamma_2/2$, all terms in $\mathrm{s}^{-1}$):

$$
\omega_k = \begin{cases}
\sqrt{\omega_{\text{rad},k}^2 + \omega_0^2 - \Gamma_2^2/4} - i\,\Gamma_2/2 & \text{massive (transverse), } k = 1, \ldots, 21 - n_{\text{broken}}, \\[6pt]
\sqrt{\omega_0^2 - \Gamma_2^2/4} - i\,\Gamma_2/2 & \text{quasi-Goldstone (orbit), } k = 1, \ldots, n_{\text{broken}}.
\end{cases}
$$

All $21$ poles lie strictly in the lower half-plane ($\operatorname{Im}\omega_k = -\Gamma_2/2 < 0$), ensuring causal decay of linear perturbations. When $\omega_{\text{rad},k} \gg \omega_0$, the $n_{\text{broken}}$ quasi-Goldstone modes form a low-frequency cluster well separated from the $21 - n_{\text{broken}}$ massive modes.

---

<a id="фазовые-переходы"></a>

## 9. Quasi-Goldstone Modes and Dynamical Bifurcations [C / H] {#phase-transitions}

<a id="связь-с-фазами"></a>

### 9.1 Relation to Reduced Phase Models (`T-160 [✗]`, `T-161`) {#connection-to-phases}

:::warning Scope of symmetry breaking and critical exponents (`T-160 [✗]`, `T-161`)
Earlier versions asserted that the algebraic purity cut $P_{\text{crit}} = 2/7$ universally triggers a second-order $G_2$ symmetry-breaking phase transition with diverging mode lifetime and universal UHM critical exponents. Both universal claims are **withdrawn**:
- **`T-160 [✗]`:** The Hilbert–Schmidt majority cut $P > 2/7$ is an algebraic threshold under a chosen convention; it does **not** automatically imply a dynamical bifurcation or $U(7) \to G_2$ symmetry breaking. A dynamical catastrophe requires a **specified reduced family and transversality**.
- **`T-161`:** Classical mean-field critical exponents hold `[T]` only for a **tuned** scalar mean-field potential (specifically even symmetry, vanishing quartic term, and positive sextic term for tricritical $A_5$ exponents; a spatial correlation length further requires an explicit gradient term). Universal UHM critical exponents are withdrawn.
:::

Within a **specified reduced dynamical model** possessing a continuous symmetry-breaking bifurcation (for instance, as a control parameter $\mu$ crosses a bifurcation threshold $\mu_c$ where a nontrivial stationary Gap orbit $\hat{\mathcal{G}}_*(\mu) \neq 0$ splits off from $\hat{\mathcal{G}} = 0$):

- **Symmetric regime ($\hat{\mathcal{G}}_* = 0$):** $G_2$ is unbroken, $n_{\text{broken}} = 0$.
- **Symmetry-broken regime ($\hat{\mathcal{G}}_* \neq 0$):** $G_2$ breaks to its stabilizer $H$, producing $n_{\text{broken}} = 14 - \dim(H)$ orbit modes.
- **Approaching the bifurcation ($\mu \to \mu_c^+$):** the restoring stiffness along the symmetry-breaking direction vanishes ($\omega_{\text{rad}} \to 0$), producing model-dependent **critical slowing** `[C]` of the soft mode.

<a id="критическое-замедление"></a>

### 9.2 Critical Slowing Hypothesis at Loss of Consciousness [H] {#critical-slowing}

As an empirical hypothesis `[H]` for models where sedation or anaesthesia drives neural dynamics across a continuous symmetry-restoring bifurcation:

1. **Frequency red shift:** soft-mode frequencies shift downward ($\omega \to 0$) as the restoring stiffness decreases.
2. **Reduced amplitude / altered damping:** coherence $|\gamma|^2$ drops and orbit modes lose amplitude.
3. **Mode collapse:** $n_{\text{broken}} \to 0$ when $\hat{\mathcal{G}}_* \to 0$ restores $G_2$ invariance.

Testing for a low-frequency red shift and collapse of infra-slow components under graded propofol anaesthesia provides an empirical probe of this hypothesis `[H]`.

---

<a id="статусы"></a>

## 10. Status Summary {#statuses}

| Result | Status | Reference |
|--------|--------|-----------|
| Orbit dimension $n_{\text{broken}} = 14 - \dim(H)$ for specified stabilizer $H \subset G_2$ | **[T]** (at specified orbit) | `T-25` |
| Rank-only stabilizer classification | **[✗]** (withdrawn) | `T-25` |
| Infinitesimal $G_2$-orbit modes conserve $\|\hat{\mathcal{G}}\|_F^2 = 2\sum_{i<j}(\hat{\mathcal{G}}_{ij})^2$ | **[T]** | Section 3.1 |
| Effective oscillator model $\omega_0^2 = \Gamma_2\kappa_0/\lvert\gamma\rvert^2$ and $\tau_{\text{Gold}}$ (in seconds) | **[C]** (model ansatz; `T-74 [✗]`, `T-75 [✗]`) | Section 2 |
| Two linear sectors: $(21 - n_{\text{broken}})$ massive + $n_{\text{broken}}$ quasi-Goldstone | **[T]/[C]** | Section 8 |
| Former immortal non-decaying topological mode ($\tau \to \infty$, $Q_{\text{top}}$) | **[✗]** (withdrawn) | `T-25`, `T-69`, `T-85 [✗]` |
| Universal $P = 2/7$ symmetry-breaking transition & universal UHM critical exponents | **[✗]** (withdrawn; tuned model only) | `T-160 [✗]`, `T-161` |
| Numerical ISF band $0.005$–$0.02$ Hz | **[C]** (depends on calibrated rates) | Section 6.1 |
| Discrete ISF component count $\in \{0, 6, 10, 11, 12\}$ & anaesthesia red shift | **[H]** | Sections 6, 9 |
| Experimental verification protocol (EEG / fMRI) | **[Pr]** | Section 7 |
| Phenomenological interpretation of $(E,O)$, $(L,D)$, $(A,U)$ modes | **[I]** | Sections 3.3, 4 |

---

<a id="что-мы-узнали"></a>

## What We Learned {#what-we-learned}

Summary of verified results:

- **Orbit dimension (`T-25 [T]` at a specified orbit):** Breaking $G_2 \to H$ produces $n_{\text{broken}} = 14 - \dim(H)$ tangential directions, taking representative values $\{0, 6, 10, 11, 12\}$ across $G_2$-stabilizer strata (depending on the full $G_7 + G_{14}$ orbit decomposition, not rank alone).
- **Dimensionally consistent effective oscillator `[C]`:** With $\omega_0^2 = \Gamma_2\kappa_0/|\gamma|^2$ ($\mathrm{s}^{-2}$), the lifetime is strictly in **seconds** — $\tau_{\text{Gold}} = 2/\Gamma_2$ in the underdamped regime ($\kappa_0/|\gamma|^2 > \Gamma_2/4$) and $\tau_{\text{Gold}} \approx |\gamma|^2/\kappa_0$ in the strongly overdamped regime ($\kappa_0/|\gamma|^2 \ll \Gamma_2/4$).
- **Exact conservation law `[T]`:** Infinitesimal $G_2$ rotations conserve the squared Frobenius norm $\|\hat{\mathcal{G}}\|_F^2 = 2\sum_{i<j}(\hat{\mathcal{G}}_{ij})^2$ (via $\sum_{i<j}\hat{\mathcal{G}}_{*,ij}\delta\hat{\mathcal{G}}_{ij} = 0$), not the linear off-diagonal sum.
- **Two linear sectors (no immortal topological mode):** The 21 perturbations in $\mathfrak{so}(7)$ split into $(21 - n_{\text{broken}})$ massive transverse modes and $n_{\text{broken}}$ quasi-Goldstone orbit modes; the former immortal topological mode is withdrawn (`T-25`, `T-69`, `T-85 [✗]`).
- **Conditional bifurcations (`T-160 [✗]`, `T-161`):** Critical slowing applies to a specified reduced dynamical family near a continuous bifurcation, not universally at the algebraic purity cut $P = 2/7$.
- **Testable hypotheses `[H]` & verification programme `[Pr]`:** Discrete ISF component counts and anaesthesia-induced red shift are formulated as empirical hypotheses with explicit EEG/fMRI protocols, and phenomenological readings `[I]` use the canonical seven axes `A, S, D, L, E, O, U`.

---

### Bridge to the Next Chapter

We have described Goldstone modes — the "echo" of broken $G_2$-symmetry. But behind every broken continuous symmetry stands a *conservation law* (Noether's theorem). What quantities exactly are conserved when $G_2$ acts on the Gap profile? What do these conserved charges mean cybernetically? And how can they be measured experimentally?

In the [next chapter](./g2-noether-cc) we translate the $G_2$ Noether charge formalism into the language of coherence cybernetics: 7 Fano charges + 7 inter-sector charges, Ward identities for Gap correlators, and a concrete experimental verification protocol for the $G_2$ structure.

---

## Related Documents

- [Gap Phase Diagram](/docs/core/dynamics/gap-phase-diagram) — three phases, Goldstone modes (mathematical foundation)
- [Gap Operator](/docs/core/dynamics/gap-operator) — stabilisers, opacity rank
- [G₂ Noether Charges](/docs/physics/gauge-symmetry/noether-charges) — broken symmetries, Goldstone modes
- [G₂ Structure](/docs/physics/gauge-symmetry/g2-structure) — $G_2 = \mathrm{Aut}(\mathbb{O})$
- [CC Phase Diagram](./phase-diagram-cc) — cybernetic interpretation of phases
- [Falsifiability](/docs/reference/falsifiability) — prediction verification criteria
- [CC Predictions](./predictions) — unique predictions of the theory
- [Topological Protection of Coherence](./topological-protection) — protection of Gap configurations
- [Gap Thermodynamics](/docs/core/dynamics/gap-thermodynamics) — potential $V_{\text{Gap}}$, $T_{\text{eff}}$
- [Coherence Matrix](/docs/core/dynamics/coherence-matrix) — definition of $\Gamma$ and its properties
- [Seven Dimensions](/docs/core/structure/dimension-u) — semantics of A, S, D, L, E, O, U
- [Measurement Methodology](./measurement) — how to detect Goldstone modes experimentally
- [Comparison with Alternatives](./comparison) — uniqueness of the mode prediction for CC
