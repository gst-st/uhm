---
sidebar_position: 2
title: "Einstein Equations in a Supplied Four-Dimensional Geometry"
slug: /physics/gravity/einstein-equations
description: "Einstein–Hilbert variation on a supplied geometry, the failed Gap projection, and the scope of the phase-information estimates."
---

# Einstein Equations in a Supplied Four-Dimensional Geometry

This chapter traces the curvature term to the external Dirac operator and tests the proposed identification with the finite coherence variables.

## Overview

A four-dimensional spectral action contains an Einstein–Hilbert term [T under the spectral and analytic inputs]. Its variation gives the Einstein tensor. Deriving a physical metric, its dynamics or Standard Model matter from a single finite register remains open. [Product geometry](/docs/proofs/physics/emergent-manifold)

---

## 1. A proposed metric from coherences {#1-emergent-metric-from-coherences}

### 1.1 Projection onto the 4D Sector

Fixing $e_O$ gives the real representation $\mathbb R e_O\oplus\mathbb R^6$. The $\mathrm{SU}(3)$ stabilizer acts irreducibly on the six-dimensional complement. Selecting three real coordinates inside it therefore adds a frame. The putative projector $\Pi_{\mathrm{ST}}=\Pi_O\oplus\Pi_{\mathrm{Re}}$ depends on that frame (48a). [Sector decomposition](/docs/core/foundations/spacetime#секторная-декомпозиция)

### 1.2 Metric Tensor

:::note Model 1.1 [H, metric ansatz]
On a prescribed background, define

$$
g_{\mu\nu}(x) = \eta_{\mu\nu} + h_{\mu\nu}(x)
$$

where $\eta_{\mu\nu} = \mathrm{diag}(+1, -1, -1, -1)$, and the perturbation:

$$
h_{\mu\nu}(x) = \sum_{i \in \mu,\, j \in \nu} |\gamma_{ij}|^2 \cdot \mathrm{Gap}(i,j)^2
$$

summation over holon dimensions belonging to the given 4D direction.
:::

**Properties:**

**(a)** Linear order at $\mathrm{Gap} \ll 1$:

$$
h_{\mu\nu} \approx \sum_{i \in \mu,\, j \in \nu} |\gamma_{ij}|^2 \sin^2(\theta_{ij})
$$

For real symmetric $h$ of sufficiently small operator norm, $\eta+h$ inherits the signature of the supplied $\eta$. Thus the signature in this expression is an input. Making $h$ a field already requires arguments $x$, a rule for comparing measurements at distinct sites and a transformation law. T-119 computes a charge spectrum. The alternative clock-complex spin factor of 48c has a Lorentzian determinant with its own inputs. Neither construction establishes the displayed formula for a physical metric. [Emergent geometry](/docs/physics/gravity/emergent-geometry)

**(c)** Connes distance:

$$
d(p, q) = \sup\{|f(p) - f(q)| : \|[D_\alpha, f]\| \leq 1\}
$$

uses the commutators of the supplied Dirac operator with the algebra. On the external manifold these depend on its metric.

---

## 2. Inputs of the four-dimensional action {#2-projection-of-the-gap-action-onto-4d}

A candidate effective action can be specified on a Lorentzian manifold as

$$
S_{\rm eff}=\frac1{16\pi G}\int (R-2\Lambda)\sqrt{-g}\,d^4x+S_{\rm matter}[g,\phi].
$$

This expression already assumes a four-dimensional integration domain, a differentiable metric and fields $\phi$ with a matter action. Partitioning the 21 internal pairs into 6 and 15 is possible after choosing four axes. That count establishes neither local spin-two gauge symmetry nor a matter representation.

### 2.1 Status of the proposed projection {#21-derivation-chain-for-the-projection-t}

The internal phase action has one evolution parameter. Promoting each $\theta_{ij}$ to a field $\theta_{ij}(x)$ and replacing time derivatives by $\partial_\mu$ introduces spacetime. An algebraic potential $V_2(\theta)$ can be nonzero for a constant field, whereas the linearized scalar curvature, containing second derivatives of $h$, vanishes for constant $h$. There is no kinematic identification of the two.

<a id="лемма-линеаризованный-мост"></a>

**Linearized bridge lemma (scope).** One can define $h_{\mu\nu}=2\,\mathrm{Re}\,\delta\gamma_{\mu\nu}/\varepsilon_0$ in a selected frame. The six off-diagonal pairs do not supply the ten components of a general symmetric four-tensor. A sum of their scalar kinetic terms does not establish the constraints, trace terms or gauge symmetry of a Fierz–Pauli field. A de Donder gauge presupposes that symmetry. Inserting the desired spin-two field equation to relate $\partial^2 h$ to its source would assume the conclusion.

If a Fierz–Pauli action and normalization $G_{\rm eff}=4\pi\mu^2/\varepsilon_0^2$ are supplied, the substitutions in T-264(b) can be evaluated. Identifying this coupling with measured Newtonian gravity is open.

---

## 3. Variation of the Einstein–Hilbert action {#3-einstein-equations-from-gap-variation}

**Theorem 1.3 / T-65 [T for the supplied product Dirac operator].** The $a_2$ heat-kernel coefficient contributes a term proportional to $\int R\sqrt g\,d^4x$ on a Riemannian four-dimensional spin geometry. With the conventions of §2 of the spectral-action chapter, $G_N=3\pi/(7f_2\Lambda_{\rm cut}^2)$. The factor seven counts internal components. The cutoff scale and its moment set the dimensional normalization. [Spectral action](/docs/physics/gravity/quantum-gravity#теорема-полное-спектральное-действие)

For the Lorentzian action of §2, varying $g^{\mu\nu}$ with appropriate boundary terms gives

$$
G_{\mu\nu}+\Lambda g_{\mu\nu}=8\pi G T_{\mu\nu},\qquad
T_{\mu\nu}=-\frac{2}{\sqrt{-g}}\frac{\delta S_{\rm matter}}{\delta g^{\mu\nu}} .
$$

Higher-curvature terms in the full spectral expansion generally modify this equation. Lovelock's classification of second-order metric equations on a supplied four-manifold neither fixes the constants nor identifies $S_{\rm matter}$.

### 3.0 Comparison with the Connes–Chamseddine spectral action program {#сравнение-connes-chamseddine}

The product constructions share the gravitational heat-kernel term. Their internal representations differ.

**Comparison table (UHM ↔ CC).**

| # | Structure | CC (1996, 2007, 2010) | UHM | Status |
|---|---|---|---|---|
| 1 | Product triple | External spin geometry and a finite real module | Same product construction with $H_{\rm int}=\mathbb C^7$. Its odd dimension precludes KO-dimension six. | Distinct finite modules |
| 2 | Internal algebra | $\mathbb C\oplus\mathbb H\oplus M_3(\mathbb C)$ | $\mathbb C\oplus M_3(\mathbb C)\oplus M_3(\mathbb C)$, generated by the chosen colour action on $\mathbb C e_O\oplus\mathbf3\oplus\bar{\mathbf3}$ | Distinct real centres preclude Morita equivalence |
| 3 | Gauge group | Standard Model group for the specified module | The unitary group $U(1)\times U(3)\times U(3)$ has dimension 19. One determinant condition removes one dimension. | No electroweak group selected by that condition |
| 4 | $a_2$ → Einstein–Hilbert | $S_{EH} = (1/16\pi G_N)\int R\sqrt g\,d^4x$, $G_N \sim 1/(a_2\Lambda^2)$ | Same; explicit $G_N = 3\pi/(7 f_2 \Lambda^2)$, factor $7 = \dim H_\mathrm{int}$ | **Identical** [T] ([T-65](/docs/physics/gravity/quantum-gravity#теорема-полное-спектральное-действие)) |
| 5 | $a_0$ | Volume term | Mapping an opacity statistic to vacuum energy requires a physical readout | [H] |
| 6 | $a_4$ | Terms for supplied gauge and internal fields | Their representations and couplings enter the operator | Input-dependent |
| 7 | Higgs sector | The big-desert model gave about 170 GeV. The extended model can fit 125 GeV | No Higgs mass selected by the seven-register | [Spectral-action comparison](/docs/physics/gravity/quantum-gravity#теорема-полное-спектральное-действие) |
| 8 | Fermions | The Standard Model module and Yukawa data are specified | Importing that module imports its field content | [T-178](/docs/proofs/physics/bimodule-construction#бимодульная-конструкция) |

The measured particle spectrum and gauge group do not follow from the common Einstein–Hilbert coefficient. The network construction gives a separate result for matter transport. Given site frames, an oriented link representation and a moving register, each transported move respects simultaneous frame changes. The group and representation are inputs, and a physical matter spectrum remains open. [Verified network results](/docs/reference/network-results)

---

### 3.1 Corollary: Gravity is a Gap Effect [I]

The proposed correspondence assigns spacetime curvature to a projection of internal curvature [I]. An invariant projection, field dynamics and comparisons with gravitational observations are needed to test it.

### 3.2 Connection of Newton's Constant with Gap Parameters

The model normalization $G_{\rm eff}=4\pi\mu^2/\langle|\gamma|^2\rangle$ increases as the specified coherence decreases. Interpreting it as a physical $G_N$ requires consistent units for $\mu$ and an independent matching measurement. Putting the measured Planck scale into the cutoff supplies a gravitational scale. A formal divergence at zero coherence gives no horizon solution.

### 3.2a Information–Gravity Reciprocity: $G_N$ as Inverse Learnability (T-264) {#взаимность-обучаемость-гравитация}

Phase estimability can be calculated directly on the register. The following gravitational reading additionally assumes the normalization in §2.1.

#### Theorem T-264 (information–gravity reciprocity) [T at FP-lemma, leading order] {#теорема-информационно-гравитационная-взаимность}

:::tip Theorem
**(a) Exact pair lemma [T].** For a state whose $(i,j)$-block is decoupled (arbitrary populations $\Gamma_{ii}, \Gamma_{jj}$; coherence $\gamma_{ij}$ up to the PSD boundary), the quantum Fisher information of the phase direction $X_{ij} = \partial\Gamma/\partial\theta_{ij} = i[\Pi_i, \Gamma]$ (a passport-charge tangent, T-260) is **exactly**

$$
\mathrm{QFI}(\theta_{ij}) = \frac{4\,|\gamma_{ij}|^2}{\Gamma_{ii} + \Gamma_{jj}}, \qquad g_{\mathrm{Bures}}(\partial_{\theta_{ij}}, \partial_{\theta_{ij}}) = \tfrac14\,\mathrm{QFI},
$$

independently of the population imbalance ($R$-cancellation). For a full $7\times 7$ state, pair-only phase variation and the full passport charge must be distinguished; (a′) gives universal bounds.

**(a′) Unconditional sandwich [T].** For every full-rank $\Gamma$ and Hermitian tangent $X$:
$$
\frac{\|X\|_{\mathrm{HS}}^2}{\lambda_{\max}(\Gamma)}
\le \mathrm{QFI}_\Gamma(X)\le
\frac{\|X\|_{\mathrm{HS}}^2}{\lambda_{\min}(\Gamma)}.
$$
This follows from $\mathrm{QFI}_\Gamma(X)=2\sum_{m,n}|X_{mn}|^2/(\lambda_m+\lambda_n)$.
For the **pair-only** tangent with entries $X_{ij}=i\gamma_{ij}$ and
$X_{ji}=-i\gamma_{ji}$, the squared norm is $2|\gamma_{ij}|^2$.
For the **full charge** $X_i=i[\Pi_i,\Gamma]$, it is
$2\sum_{k\ne i}|\gamma_{ik}|^2$. These tangents coincide only when row $i$
has no other coherences. For example, $\Gamma=I_3/3+(E_{02}+E_{20})/12$, $i=0,j=1$ gives $\gamma_{01}=0$ and $\mathrm{QFI}(X_0)=1/24>0$.

If $\delta=\max_i(|\Gamma_{ii}-1/7|+\sum_{j\ne i}|\gamma_{ij}|)<1/7$,
Gershgorin gives $|\lambda_k-1/7|\le\delta$. For $X\ne0$ the relative
QFI deviation from $7\|X\|_{\mathrm{HS}}^2$ is at most
$7\delta/(1-7\delta)$. This analytical bound is not replaced by sampled
checks, and those checks do not identify the two distinct tangents.

**(b) Reciprocity [T at FP-lemma, leading order].** At vacuum populations $\Gamma_{ii} = 1/7 + O(\varepsilon^2)$ the ST-sector mean satisfies $\langle|\gamma_{\mathrm{ST}}|^2\rangle = \varepsilon_0^2 = \tfrac{1}{14}\langle\mathrm{QFI}\rangle_{\mathrm{ST}}$, and the Fierz–Pauli constant $G_N^{(ST)} = 4\pi\mu^2/\varepsilon_0^2$ becomes

$$
\boxed{\; G_N^{(ST)} \cdot \big\langle \mathrm{QFI}(\theta_{\mu\nu}) \big\rangle_{\mathrm{ST}} \;=\; 56\pi\mu^2 \;=\; 8\pi N \mu^2 \big|_{N=7} \;}
$$

This is a leading-order substitution for the selected normalization and phase tangents.

**(c) T-254.** A separately conserved effective fluid with a specified positive energy readout $\rho_{\rm DE}=C\mathcal G_O^2$ obeys the drift identity of T-254. Its identification with a cosmological observable is an additional hypothesis. [Energy readout](/docs/physics/gravity/cosmological-constant#теорема-лямбда-дрейф)
:::

**Proof.** *(a)* For the decoupled block the SLD tangent formula $\mathrm{QFI} = 2\sum_{m,n}|X_{mn}|^2/(\lambda_m + \lambda_n)$ reduces to the block. Diagonalise the block with populations $p = \Gamma_{ii}$, $q = \Gamma_{jj}$, coherence $g$: eigenvalues $\lambda_\pm = \tfrac{p+q}{2} \pm R$ with $R = \sqrt{(p-q)^2/4 + |g|^2}$; the tangent $X = i[\Pi_i, \Gamma]$ is purely off-diagonal in the eigenbasis with $|\langle +|\Pi_i|-\rangle|^2 = |g|^2/(4R^2)$, and $(\lambda_+ - \lambda_-)^2 = 4R^2$. Hence $\mathrm{QFI} = 2 \cdot 2 \cdot \frac{4R^2}{p+q} \cdot \frac{|g|^2}{4R^2} = \frac{4|g|^2}{p+q}$ — $R$ cancels, so the result holds at any imbalance and any admissible $|g|$. *(b)* Substitute the pair lemma at $\Gamma_{ii} = 1/7$ into the bridge-lemma constant $G_N^{(ST)} = 4\pi\mu^2/\varepsilon_0^2$ (§2.1): $\langle\mathrm{QFI}\rangle_{\mathrm{ST}} = 14\varepsilon_0^2(1 + O(\bar\varepsilon))$. *(c)* is T-254 [T] plus the [I]-reading. $\blacksquare$

**Machine verification**: balanced-block identity to $6.7 \cdot 10^{-16}$; decoupled-pair identity in $\mathbb{C}^7$ — ratio $1.000000$ across random populations/coherences; cross-coherence correction scaling measured ($0.23\%/0.8\%/4.4\%$ at $\bar\varepsilon = 0.005/0.01/0.02$); substitution chain (b) exact.

The numerical checks concern QFI and the substitution in (b). There is no independent gravitational measurement in this calculation.

### 3.3 Matching the two definitions of $G$ {#33-consistency-of-the-two-definitions-of-g-t}

**Theorem 3.2 (matching claim open).** Equating $4\pi\mu^2/\varepsilon_0^2$ and $3\pi/(7f_2\Lambda_{\rm cut}^2)$ imposes a relation on independent inputs. The claimed $O(\mathrm{Gap}^4)$ residual would require a derived matching expansion with controlled error.

### 3.4 Limitations of the Lovelock Argument {#34-ограничения-аргумента-лавлока}

T-120 constructs a smooth product for each selected Riemannian metric. Diffeomorphism invariance of a supplied spectral metric action gives covariance. Lovelock's classification applies to local natural symmetric divergence-free second-order metric tensors in four dimensions. It singles out the Einstein and cosmological terms at that order. No nontrivial $SU(3)\to SO(3)$ projection exists to transfer this result to the internal phases. [T-121](/docs/proofs/physics/emergent-manifold#теорема-лавлок-замыкание)

---

## 4. Stress–energy for a specified matter action {#4-energy-momentum-tensor-from-gap}

:::note Theorem 2.1 [C for a supplied homogeneous scalar matter action]
The following energy and pressure require a kinetic term, potential and metric coupling. Their interpretation as dark energy is [H].
:::

**(a)** Energy of Gap excitations:

$$
T_{00}^{(\mathrm{Gap})} = \sum_{\mathrm{Gap\text{-}pairs}} \left[\frac{m_{ij}}{2}\dot{\theta}_{ij}^2 + V_{\mathrm{Gap}}^{(\mathrm{Gap\text{-}pairs})}(\theta)\right]
$$

This is **dark energy** in UHM [I]: the energy of invisible Gap dynamics in the Im-sector.

**(b)** Pressure:

$$
T_{ab}^{(\mathrm{Gap})} = -\delta_{ab} \cdot p_{\mathrm{Gap}}, \quad p_{\mathrm{Gap}} = \sum \left[\frac{m_{ij}}{2}\dot{\theta}_{ij}^2 - V_{\mathrm{Gap}}(\theta)\right]
$$

**(c)** Equation of state:

$$
w = \frac{p_{\mathrm{Gap}}}{\rho_{\mathrm{Gap}}} = \frac{\langle\dot{\theta}^2\rangle/2 - V}{|\langle\dot{\theta}^2\rangle/2 + V|}
$$

| Regime | $w$ | Interpretation |
|-------|-----|---------------|
| $V \gg$ kinetic | $w \to -1$ | Cosmological constant |
| Balance | $w \in (-1, 1)$ | Quintessence |

At $K\ll V$, $w=(K-V)/(K+V)$ is near $-1$ in this field model. Inferring purity or a relaxation rate would require a separate cosmological readout. [T-266](/docs/physics/gravity/cosmological-constant#теорема-стадия-вселенной)

**(d) [C]** At $\mu \sim 10^{-3}$ eV (neutrino mass scale) and $\langle\mathrm{Gap}^2\rangle \sim 0.1$:

$$
\rho_{\mathrm{DE}} \sim (10^{-3}\;\text{eV})^4 \sim 10^{-47}\;\text{GeV}^4
$$

— the order of magnitude of the observed dark energy ($\rho_{\mathrm{DE}}^{\mathrm{obs}} \approx 2.6 \times 10^{-47}$ GeV$^4$).

:::warning Tuning vs. derivation
The value $\mu \sim 10^{-3}$ eV is **not derived** from the first principles of Gap theory, but chosen phenomenologically to match the observed $\rho_{\mathrm{DE}}$. Similarly, $\langle\mathrm{Gap}^2\rangle \sim 0.1$ is a tuned parameter. Thus $\rho_{\mathrm{DE}} \sim 10^{-47}$ GeV$^4$ is a result of **fitting** two free parameters, not a prediction. An independent justification of $\mu$ (e.g. from neutrino masses) would elevate the status to [T].
:::

---

## 5. Covariant Conservation

:::tip Theorem 3.1 [T]
The tensor $T_{\mu\nu}^{(\mathrm{Gap})}$ satisfies the covariant conservation condition:

$$
\nabla_\mu T^{\mu\nu} = 0
$$

:::

For a diffeomorphism-invariant matter action, its metric stress tensor is covariantly conserved on the matter equations of motion. Equivalently the Einstein equations with constant $G,\Lambda$ imply conservation by the contracted Bianchi identity.

---

## 6. Two-Loop Renormalization Group

### 6.1 Beta Functions with Fano Combinatorics

:::note Coupling input and perturbative scope [D/H/Pr]
The relation $\lambda_3=2\mu^2/(3|\bar\gamma|)$ and the value $\lambda_3\approx74$ are chosen effective-model inputs, not coefficients uniquely derived from the spectral action. A self-consistency equation determines a value only after its functional, other couplings and state/field space are supplied. Compactness of a finite integration domain does not establish continuum UV finiteness, perturbative convergence or a universal factor-five error bound.

Quantitative mass, mixing or gravitational predictions require independently fixed spectral data, renormalization/matching scales and physical readouts. If $\bar\gamma$ or $\lambda_3$ is inferred from those same observables, the result is calibration; held out data are needed for prediction. A small proposed $\lambda_3\varepsilon/(4\pi)$ is a power-counting estimate only after a definite action and propagators are supplied; factorially many diagrams can still yield a divergent asymptotic expansion. [The coupling discussion](/docs/physics/particle-physics/yukawa-hierarchy#c7-nonperturbative) records these conditions.
:::

#### T-184: scope of non-perturbative spectral evaluation {#непертурбативная-извлекаемость}

For a **supplied finite Hermitian matrix** $D$, diagonalization exactly gives $\operatorname{Tr}f(D^2/\Lambda^2)$ at any chosen coupling [T]. For a supplied elliptic operator on a compact manifold with suitable boundary conditions and cutoff, heat-kernel asymptotics are available under their analytic hypotheses [T/C]. Compactness of a phase parameter domain alone does not ensure compact resolvent for an arbitrary operator.

These statements compute a chosen functional. They do not derive the operator, cutoff, physical field content, correlation measure, masses or coupling matching. Heat-kernel asymptotics are not a convergence theorem for a loop series. A Euclidean finite matrix has no canonical Lorentzian spacetime or universal Wick rotation; a real structure/KO-dimension and positivity/causality data must be checked in the supplied geometry.

The beta-functions displayed below are effective-model hypotheses [H] until an action, propagators, regulator, diagrams and renormalization conditions derive their coefficients. The equalities $441=21^2$, $147=21\cdot7$, $49=7^2$ are arithmetic [T]; those counts alone do not establish the associated loop coefficients, errors or physical mass spectrum.

:::note Proposed two-loop beta functions [H]
:::

**(a)** Mass parameter:

$$
\beta_{\mu^2}^{(2)} = -\frac{21\lambda_4}{8\pi^2}\mu^2 + \frac{7\lambda_3^2}{16\pi^2} + \frac{1}{(8\pi^2)^2}\left[-\frac{441\lambda_4^2}{2}\mu^2 + 147\lambda_3^2\lambda_4 - \frac{49\lambda_3^4}{4\mu^2}\right]
$$

Two-loop factors are determined by the combinatorics of the [Fano plane](/docs/physics/gauge-symmetry/g2-structure):

| Factor | Value | Origin |
|-----------|----------|---------------|
| 441 | $21^2$ | Pairs-in-pairs |
| 147 | $21 \times 7$ | Triples-in-pairs |
| 49 | $7^2$ | Triples-in-triples |

**(b)** Cubic constant:

$$
\beta_{\lambda_3}^{(2)} = -\frac{15\lambda_3\lambda_4}{8\pi^2} + \frac{1}{(8\pi^2)^2}\left[-\frac{315\lambda_3\lambda_4^2}{2} + \frac{35\lambda_3^3}{2\mu^2}\right]
$$

Two-loop factors: $315 = 15 \times 21$, $35 = C(7,3)$ (triples of the Fano complement).

**(c)** Quartic constant:

$$
\beta_{\lambda_4}^{(2)} = \frac{63\lambda_4^2}{4\pi^2} - \frac{7\lambda_3^2}{8\pi^2\mu^2} + \frac{1}{(8\pi^2)^2}\left[-\frac{63^2\lambda_4^3}{3} + 441\frac{\lambda_3^2\lambda_4}{\mu^2} - \frac{49\lambda_3^4}{4\mu^4}\right]
$$

### 6.2 Octonionic Fixed Point

:::tip Theorem 4.2 [T]
In the two-loop approximation:

**(a)** The Wilson-Fisher fixed point receives a correction of ~0.3% — **stable**.

**(b)** The octonionic fixed point ($\lambda_3^* \neq 0$) **exists** for $\lambda_4 < \lambda_4^{(\mathrm{crit})} \approx 0.0028$ — it is a saddle point (1 unstable + 2 stable directions).
:::

**Interpretation [I].** The octonionic fixed point describes a universal class of "octonionic phase transition" — a transition from the PT-invariant ($\lambda_3 = 0$) to the PT-breaking ($\lambda_3 \neq 0$) regime: from "unconscious" to "conscious" dynamics.

### 6.3 Anomalous Dimension

:::tip Theorem 4.3 [T]
Anomalous dimension of the Gap field in the two-loop approximation:

$$
\eta_{\mathrm{Gap}} = \frac{7\lambda_4^2}{2(8\pi^2)^2} - \frac{\lambda_3^2}{4(8\pi^2)^2 \mu^2} \approx 1.1 \times 10^{-4}
$$

:::

The mean-field approximation remains accurate to ~0.01%.

---

## 7. Swallowtail Catastrophe and L-Transitions

### 7.1 Gap Tristability

:::note Theorem 5.1 (bound on the number of interior minima)
The proposed one-dimensional normal form is

$$
V_{\mathrm{eff}}(G) = G^5 + aG^3 + bG^2 + cG
$$

where $G = \mathrm{Gap}(i,j)$ for a selected channel:
- $a = a(\kappa, \mu^2, \lambda_4)$ — function of regeneration and self-interaction
- $b = b(\lambda_3, \bar{A})$ — function of the octonionic associator
- $c = c(\Gamma_2, \kappa, h_{\mathrm{ext}})$ — function of decoherence and external force

Its derivative has degree four. Three distinct strict interior minima would require two additional intervening maxima and at least five critical points, which is impossible for this polynomial. Boundary minima require a defined admissible interval and boundary conditions.
:::

### 7.2 Connection with L-Levels

:::note Theorem 5.2 (proposed interpretation [H])
The table assigns labels to three putative profiles. Neither the quintic above nor a clinical measurement establishes these assignments.
:::

| Minimum | Gap | Interpretation | L-level |
|---------|-----|---------------|-----------|
| $G_{\mathrm{low}} \approx 0.1$ | Low | High transparency | L3+ (reflexive consciousness) |
| $G_{\mathrm{mid}} \approx 0.4$ | Medium | Intermediate opacity | L2 (conscious experience) |
| $G_{\mathrm{high}} \approx 0.8$ | High | High opacity | L1/L0 (basic interiority) |

The following transition rules would be additional model hypotheses.

| Transition | Mechanism | Hysteresis width |
|---------|----------|-------------------|
| L1 $\to$ L2 | fold bifurcation at $\kappa > \kappa_{\mathrm{fold}}$ | $\Delta\kappa_{L1 \to L2} = \lambda_3 \bar{A}_1 / \mu^2$ |
| L2 $\to$ L3 | fold bifurcation at $\kappa > \kappa_{\mathrm{fold}}'$ | $\Delta\kappa_{L2 \to L3} = \lambda_3 \bar{A}_2 / \mu^2$ |

**Prediction [H].** With simultaneous change of all three control parameters, a **direct jump L0 $\to$ L3** is possible — the swallowtail effect, bypassing the intermediate minimum.

---

## 8. Model System: Alexithymia → Insight

For the S$\leftrightarrow$E channel (Structure $\leftrightarrow$ Interiority) with parameters of a typical L2 system ($P \approx 0.5$): $\mu^2 \approx 16.6$, $\lambda_3 \approx 73.8$, $\lambda_4 \approx 27.7$.

The three tabulated points cannot all be interior minima of this quintic.

| Minimum | $G$ | $V_{\mathrm{eff}}$ | L-level | Clinical |
|---------|-----|---------------------|-----------|---------|
| 1 | 0.12 | $-0.41$ | L3 | Full integration |
| 2 | 0.48 | $-0.28$ | L2 | Normal functioning |
| 3 | 0.82 | $-0.35$ | L1 | Alexithymia |

The energies alone do not determine transition barriers. Clinical or cognitive classifications require separate observations.

---

## 9. Connection with Other Sections

| Topic | Page | Connection |
|------|----------|-------|
| Emergent geometry | [Emergent geometry](/docs/physics/gravity/emergent-geometry) | Pre-metric and functor $\mathcal{G}$ |
| Cosmological constant | [Cosmological constant](/docs/physics/gravity/cosmological-constant) | Computation of $\Lambda_{\mathrm{Gap}}$ and suppression mechanisms |
| $G_2$-structure | [$G_2$-structure](/docs/physics/gauge-symmetry/g2-structure) | Fano plane and combinatorics of beta functions |
| Berry phase | [Berry phase](/docs/physics/cosmology-phys/berry-phase) | Topological protection of Gap |

---

**Related documents:**
- [Emergent geometry](/docs/physics/gravity/emergent-geometry)
- [Quantum gravity](/docs/physics/gravity/quantum-gravity)
- [Cosmological constant](/docs/physics/gravity/cosmological-constant)
- [Spacetime](/docs/core/foundations/spacetime)
