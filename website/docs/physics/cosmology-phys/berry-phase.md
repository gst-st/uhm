---
sidebar_position: 2
title: "Berry Phase and Topological Protection"
slug: /physics/cosmology-phys/berry-phase
description: "Berry holonomy, orbit topology, selected winding forms and the limits of their physical interpretation."
---

# Berry Phase and Topological Protection

A Berry phase can be measured for a specified adiabatic eigenstate family. This chapter checks which additional claims follow for Gap variables.

## Overview

Neither the one-dimensional Chern–Simons expression nor the proposed Keldysh argument determines a physical topological term for Gap (T-85 withdrawn in §9.2). The topology of a specified orbit and the arithmetic of a chosen winding form remain computable.

---

## 1. Definition of the Berry Phase

Let the context parameter $\lambda \in M$ (a manifold of contexts) define the effective Hamiltonian $H_{\mathrm{eff}}(\lambda)$. Under adiabatic motion along a closed loop $\gamma: [0,T] \to M$, the system acquires a **geometric Berry phase**:

$$
\Phi_B = \oint_\gamma \mathcal{A}(\lambda) \cdot d\lambda
$$

where $\mathcal{A}(\lambda) = i\langle n(\lambda)|\nabla_\lambda|n(\lambda)\rangle$ is the Berry connection for the $n$-th eigenstate.

---

## 2. Topologically Protected Gap

**Former Theorem 5.1 [✗ as a universal claim].** On a noncontractible loop one can choose a constant, nondegenerate eigenstate, whose Berry phase is zero. With nonzero Berry curvature even contractible loops can acquire different geometric phases. A nonzero fundamental group alone gives no lower bound on a pairwise Gap.

### 2.1 Holonomy in the Space of Gap Configurations

The Berry phase $\Phi_B$ is the **holonomy** of the Berry connection in the space of Gap configurations. Under adiabatic variation of the context parameters $\lambda(\tau)$ along a closed loop $\gamma$, the system returns to the same eigenstate but acquires a phase factor $e^{i\Phi_B}$.

A Hamiltonian family with an isolated eigenline specifies a connection. In a compatible gauge on a spanning surface $\Sigma$, Stokes' theorem gives $\oint_{\partial\Sigma}\mathcal A=\int_\Sigma\mathcal F$ modulo $2\pi$. A three-form on the internal seven-dimensional carrier does not specify this eigenline or its curvature on a torus of phase coordinates.

---

## 3. Connection to Octonionic Structure

For a closed subgroup $H$ of the compact simply connected group $G_2$, the fibration $H\to G_2\to G_2/H$ relates the homotopy groups of a specified orbit. Relating this orbit to a field configuration requires an action and boundary data.

### 3.1 Classification of Stabilisers

**Theorem 3.1 (orbit dimension).** Once the stabilizer $H$ of an actual group action is identified, $\dim(G_2/H)=14-\dim H$. Examples are $G_2/SU(3)\cong S^6$ for the action on a unit imaginary octonion and the flag orbit $G_2/T^2$. The rank of an arbitrary real skew matrix does not specify either action or stabilizer.

### 3.2 Topological Protection from $\pi_1$

**Theorem 3.2 / T-69 [T for the specified target].** For the connected torus $T^2$ the exact sequence gives $\pi_1(G_2/T^2)=0$ and $\pi_2(G_2/T^2)\cong\pi_1(T^2)=\mathbb Z^2$. The two integers classify based maps **from $S^2$**. A solitary density matrix supplies no such map. A continuous potential with a minimum set disjoint from a compact forbidden set has a positive excess there when all minimizers are excluded. Its size depends on the potential. The earlier numerical barriers and protection of individual states are withdrawn. [T-69](/docs/core/dynamics/composite-systems#теорема-тополог-защита)

---

## 4. Five Types of Gap Protection

Code distance is defined for codewords, the octonionic associator for algebra elements, the potential for specified fields, a fixed-point theorem for a specified map, and the homotopy class for a sphere of field values. Relating any of these five quantities to a nonzero measured Gap requires a map between their domains. For example, the diagonal state $I/7$ has no imaginary off-diagonal entries.

---

## 5. Sectoral Gap Bound {#секторная-gap-граница}

### 5.1 Retraction of the Original Fano Bound [✗]

:::danger Retraction: Theorem 6.1 (Fano Bound $\leq 1/2$) [✗]
The original formulation claimed: $\mathrm{Gap}_{\mathrm{intra}}(i,j) \leq 1/2$ for all pairs $(i,j)$ on the same line of the Fano plane.

**Counterexample:** In $\mathrm{PG}(2,2)$ **every** pair lies on exactly one Fano line (any two points of the projective plane determine a line). The lines containing O: $\{A, O, U\}$, $\{S, L, O\}$, $\{D, E, O\}$. For the pairs $(A,O)$, $(S,O)$, $(D,O)$, $(E,O)$, $(L,O)$, $(U,O)$ on these lines, $\mathrm{Gap}(O,i) \approx 1$ (from the Page–Wootters mechanism: the O-sector serves as an internal clock with maximal phase). This is a **direct counterexample** to the original formulation $\leq 1/2$.

Replacing theorem: [Sectoral Gap Bound](#теорема-секторная-gap-граница) [T].
:::

### 5.2 Theorem (Sectoral Gap Bound) [T] {#теорема-секторная-gap-граница}

:::note T-80 [conditional on the sector-vacuum profile (SV)]
Using the numerical profile of the table below gives the following bounds and estimates.

**(a)** For all non-O pairs ($i,j \in \{A,S,D,L,E,U\}$):

$$
\mathrm{Gap}(i,j) \leq \varepsilon_{\max}\approx 0.06 < 1/2
$$

**(b)** For O-sectoral pairs ($i \in \{A,S,D,L,E,U\}$):

$$
\mathrm{Gap}(O,i) = 1 - O(\bar{\varepsilon}^2) \approx 1
$$

**(c)** The total Gap is dominated by the O-sector:

$$
\mathcal{G}_{\text{total}} = \mathcal{G}_O + O(\bar{\varepsilon}^2), \quad \mathcal{G}_O := 2\sum_{i \neq O} |\gamma_{Oi}|^2 \cdot \mathrm{Gap}(O,i)^2
$$

:::

**Proof.**

**Step 1.** The table supplies the sector values. The corrected invariant potential of T-64 does not derive this profile.

| Sector | Pairs | $\varepsilon$ | Gap |
|--------|------|--------------|-----|
| O-to-all | 6 pairs | $\varepsilon_O \approx 1$ | $\approx 1$ |
| $\mathbf{3}$-$\mathbf{3}$ | 3 pairs | $\varepsilon_{33} \approx 0.06$ | $\approx 0.06$ |
| $\bar{\mathbf{3}}$-$\bar{\mathbf{3}}$ | 3 pairs | $\varepsilon_{\bar{3}\bar{3}} \approx 10^{-17}$ | $\approx 10^{-17}$ |
| $\mathbf{3}$-$\bar{\mathbf{3}}$ | 9 pairs | $\varepsilon_{3\bar{3}} \approx 0$ | $\approx 0$ |

**Step 2 (Upper bound for non-O pairs).** The potential $V_2 = \mu^2 \mathcal{G}_{\text{total}}$ quadratically suppresses large phases. The competing $V_3$ (cubic) and $V_4$ (quartic) terms generate a non-zero minimum, but:

$$
\mathrm{Gap}(i,j) \leq \varepsilon_{\max} = \varepsilon_{33} \approx 0.06 \ll \frac{1}{2}
$$

The mean coherence $\bar{\varepsilon} = \bigl(\frac{1}{15}\sum_{i<j, \, i,j \neq O} \varepsilon_{ij}^2\bigr)^{1/2} = \varepsilon_{33}/\sqrt5 \approx 0.027$ ([C at (SV)]; the value $0.023$ written here until 2026-09-25 is retracted with the audit A-83), and the maximum $\varepsilon_{\max} = \varepsilon_{33} \approx 0.06 \ll 1/2$.

**Step 3.** A nonzero clock rate in a readout proportional to $\sqrt{\sum_i|\gamma_{Oi}|^2\mathrm{Gap}(O,i)^2}$ requires at least one nonzero term. It does not force all six phases to be near maximal opacity. This last feature is part of (SV).

### 5.3 Map of Fano Triplets

| # | Triplet | Dimensions | Interpretation |
|---|---------|-----------|---------------|
| 1 | $(e_1, e_2, e_3)$ | $A, S, D$ | Material block |
| 2 | $(e_1, e_4, e_5)$ | $A, L, E$ | Cognitive block |
| 3 | $(e_1, e_6, e_7)$ | $A, O, U$ | Transcendent block |
| 4 | $(e_2, e_4, e_6)$ | $S, L, O$ | Structural-logical block |
| 5 | $(e_2, e_5, e_7)$ | $S, E, U$ | Somatic-integrative block |
| 6 | $(e_3, e_4, e_7)$ | $D, L, U$ | Active-holistic block |
| 7 | $(e_3, e_5, e_6)$ | $D, E, O$ | Dynamic-foundational block |

### 5.4 Updated Falsifiable Prediction

Under the sector profile, the mean Gap for the non-clock pairs is predicted to be smaller than for the clock pairs.

$$
\langle\mathrm{Gap}_{\text{non-O}}\rangle \ll \langle\mathrm{Gap}_O\rangle \approx 1
$$

Specifically: $\langle\mathrm{Gap}_{\text{non-O}}\rangle \leq \bar{\varepsilon} \approx 0.027$, i.e. non-O pairs are nearly transparent while O-pairs are maximally opaque.

---

## 6. Spontaneous Breaking and Goldstone Modes

### 6.1 Broken Symmetries under Spontaneous Gap

**Theorem 4.1 [T under a specified group action].** An orbit with stabilizer $H$ has $14-\dim H$ tangent directions. For a smooth invariant potential these directions have zero Hessian at a critical point on the orbit. Interpreting them as Goldstone particles requires field dynamics, a dispersion relation and symmetry-breaking conditions.

### 6.2 Modification for Dissipative Systems

:::note Theorem 4.2 [H, dissipative model]
One proposed choice of mass and decay time is

$$
m_{\mathrm{Gold}}^2 = \Gamma_2 \cdot \kappa_0 / |\gamma|^2
$$

$$
\tau_{\mathrm{Gold}} = \frac{1}{\Gamma_2} \cdot \frac{|\gamma|^2}{\kappa_0}
$$

- When $\Gamma_2 \to 0$ (isolated system): $m_{\mathrm{Gold}} \to 0$ — standard Goldstone regime.
- When $\Gamma_2 \to \infty$ (strong dissipation): $m_{\mathrm{Gold}} \to \infty$ — modes are frozen.
:::

### 6.3 Excitation Spectrum

:::note Theorem 5.1 [H, excitation model]
The following grouping assumes a specific vacuum, kinetic law and mode content.

**(a)** **Massive modes** ($n_{\mathrm{massive}}$ in total): directions perpendicular to the $G_2$-orbit, $\omega_{\mathrm{massive}}^2 = \mu_{\mathrm{eff}}^2 + \kappa/m$.

**(b)** **Quasi-Goldstone modes** ($n_{\mathrm{broken}}$ in total): broken generators of $G_2$, $\omega_{\mathrm{Gold}}^2 = \kappa/m - \Gamma_2^2/(4m^2)$.

**(c)** **Topologically protected mode** (0 or 1): when $Q_{\mathrm{top}} \neq 0$ — cannot decay without a phase transition.

**(d)** Total count: $n_{\mathrm{massive}} + n_{\mathrm{broken}} + n_{\mathrm{top}} = 21$.
:::

### 6.4 Physical Interpretation: ISF

The quasi-Goldstone modes are **slow collective oscillations** of the Gap profile along the $G_2$-orbit, redistributing the Gap among pairs while conserving $\mathcal{G}_{\mathrm{total}}$:

$$
\delta\mathrm{Gap}(i,j) = \sum_a \epsilon_a \cdot [T_a, \hat{\mathcal{G}}_*]_{ij}
$$

Frequency of Goldstone modes for a neural system [C]:

$$
f_{\mathrm{Gold}} \approx \frac{1}{2\pi}\sqrt{\frac{\kappa}{m}} \sim 0.005\text{--}0.02\;\text{Hz}
$$

This matches in order of magnitude the **infra-slow neuronal fluctuations** (ISF) observed in fMRI (0.01–0.1 Hz).

:::warning Parameter Fitting
The values of $\kappa$ and $m$ are not derived from microscopic theory but are chosen so that $f_{\mathrm{Gold}}$ falls within the ISF range. The coincidence with observed frequencies of 0.01–0.1 Hz is a consequence of fitting, not a prediction.
:::

:::info Falsifiable Prediction (ISF)
The number of independent ISF components depends on the opacity rank:

| Rank | $n_{\mathrm{Gold}}$ | ISF prediction |
|------|--------|---------------------|
| 1 | 6 | 6 independent ISF components |
| 2 | 10 | 10 ISF components |
| 3 | 12 | 12 ISF components |

Typical number of ICA components in resting-state fMRI: $\sim 10$–$20$, consistent with rank 2–3.
:::

---

## 7. Gap Phase Diagram

### 7.1 Control Parameters

Two dimensionless parameters:
- **Dimensionless temperature:** $t := T_{\mathrm{eff}}/T_c = (\Gamma_2/\kappa_0) \cdot (k_B T_{\mathrm{phys}} \ln 21) / \mu^2$
- **Viability:** $r := \kappa / \Gamma_2$

### 7.2 Three Phases

:::tip Theorem 6.1 (Phase Diagram) [T]
**(a) Phase I: Ordered Gap** ($t < 1$, $r > r_c$). Several channels with high Gap, the rest transparent. $G_2 \to H$ spontaneously broken. Goldstone modes exist.

**(b) Phase II: Disordered Gap** ($t > 1$, $r > r_c$). Gap is uniform: $\mathrm{Gap}(i,j) \approx \mathrm{const}$. $G_2$ approximately conserved.

**(c) Phase III: Dead Zone** ($r < r_c$). Coherences decay: $|\gamma_{ij}| \to 0$.

**(d)** I↔II: **second-order** (continuous), $\beta = 1/2$.
**(e)** I↔III: **first-order** (discontinuous).
**(f)** Tricritical point: $(t^*, r^*) = (1, r_c)$, exponents $\beta = 1/4$, $\gamma = 1$, $\delta = 5$.
:::

```
    t (T_eff/T_c)
    │
  2 ┤         Phase II: Disordered Gap
    │        (uniform, recoverable)
    │
  1 ┤─ ─ ─ ─ ─ ─ ─ ─ ╋ ─ ─ ─ ─ ─ ─ ─ ─ ─
    │               ╱ (t*,r*)
    │   Phase I   ╱   ← 2nd-order (continuous)
    │  Ordered   ╱
    │   Gap     ╱
    │          ╱
  0 ┤─────────╱─────────────────────────────
    │ Ph. III│
    │  Dead  │
    └────────┼────────┼─────────────────── r (κ/Γ₂)
             r_c      1
```

### 7.3 Clinical Correspondence

| Phase | Clinical correspondence | Characteristic |
|------|--------------------------|----------------|
| I (ordered) | Normal functioning | Specific opacities, transparency in other channels |
| II (disordered) | Diffuse dissociative state | All channels equally opaque |
| III (dead) | Dementia, coma | Loss of coherences, breakdown of bonds |
| I↔II transition | Psychotic episode | Sudden "melting" of structured opacity |
| I↔III transition | Acute decompensation | Abrupt breakdown upon resource exhaustion |
| Tricritical | Borderline state | Oscillation between ordered and chaotic Gap |

---

## 8. Critical Phenomena

:::tip Theorem 7.1 (Critical Exponents) [T]
Near $t = 1$ (I↔II transition):

| Exponent | Value | Physical meaning |
|-----------|---------|------------------|
| $\beta = 1/2$ | $\sigma_{\mathrm{Gap}}^2 \propto (1-t)^{2\beta}$ | Gap anisotropy |
| $\gamma = 1$ | $\chi \propto \lvert 1-t\rvert^{-\gamma}$ | Susceptibility |
| $\nu = 1/2$ | $\xi \propto \lvert 1-t\rvert^{-\nu}$ | Correlation length |
| $\alpha = 0$ | Logarithmic divergence | Heat capacity |

Scaling relations are satisfied:
- Rushbrooke's law: $\alpha + 2\beta + \gamma = 0 + 1 + 1 = 2$ ✓
- Inserting $\nu=1/2$ and $\alpha=0$ into the hyperscaling relation $d\nu=2-\alpha$ would give $d=4$. In this model hyperscaling and an independently measured length exponent have not been established. The substitution cannot select physical spacetime dimension.
:::

**Theorem 7.2 (scope).** The exponents in the table characterize a specified mean-field model. Counting 21 pairs supplies an internal component count. Spatial fluctuations and the applicability of mean-field exponents to an extended physical system need a separate analysis.

---

## 9. Refutation of the CS Derivation {#9-опровержение-cs-вывода}

### 9.1 Refutation of the CS Derivation of the Topological Term

:::danger Theorem 2.1 (CS on 1D — Total Derivative) [T]
The Chern-Simons functional for a $\mathfrak{g}_2$-connection on a 1D base is a **total derivative** and does not generate a topological phase:

$$
CS_1[\mathcal{A}] = \frac{\kappa}{2}\sum_a A_a \dot{A}_a = \frac{d}{d\tau}\!\left(\frac{\kappa}{4}\sum_a A_a^2\right)
$$

:::

**Proof.**

**(a)** In the 1D case, the triple wedge $\mathcal{A} \wedge \mathcal{A} \wedge \mathcal{A}$ **vanishes identically** (all 1-forms are proportional to $d\tau$, and $d\tau \wedge d\tau = 0$). Only the quadratic part remains:

$$
CS_1[\mathcal{A}] = \frac{1}{2}\mathrm{Tr}(\mathcal{A}\,\dot{\mathcal{A}})
$$

**(b)** The $\mathfrak{g}_2$-connection is expanded in orthonormal generators $T_a$ ($a = 1,\ldots,14$):

$$
\mathcal{A} = \sum_a A_a\,T_a, \quad \mathrm{Tr}(T_a\,T_b) = \kappa\,\delta_{ab}
$$

**(c)** Substituting:

$$
CS_1 = \frac{\kappa}{2}\sum_a A_a\,\dot{A}_a = \frac{d}{d\tau}\!\left(\frac{\kappa}{4}\sum_a A_a^2\right)
$$

This is a **total derivative** with respect to $\tau$. Upon integration over a closed loop (compactification of $\tau$ on $S^1$) the contribution is a boundary term — **zero** for periodic fields $A_a(\tau + T) = A_a(\tau)$. $\blacksquare$

:::warning Corollary [T]
$CS_1$ on a 1D base **does not generate** a topological phase for winding sectors. The identification "$CS_1 = \sum_{\mathrm{Fano}} \theta_{ij}\dot{\theta}_{jk}$" does not follow from $\mathrm{Tr}(\mathcal{A}\dot{\mathcal{A}})$, since the latter is a total derivative.
:::

### 9.2 Audit of the Keldysh/Berry proposal [✗; replacement Pr] {#теорема-l-top-кельдыш}

The claimed unique topological term and coefficient $\beta=\lambda_3/(2\pi)$ do not follow from the written expression or T-75 (withdrawn [✗]). There is a direct obstruction. For positive definite density matrices $\rho_-,\rho_+$ and a Hermiticity-preserving generator $\mathcal L$, both $\log\rho_-$ and $\mathcal L(\rho_+)$ are Hermitian. For any two Hermitian matrices $A,B$,

$$
\overline{\operatorname{Tr}(AB)}=\operatorname{Tr}(BA)=\operatorname{Tr}(AB).
$$

Thus

$$
\operatorname{Im}\operatorname{Tr}\big[\rho_+\log\rho_--\mathcal L(\rho_+)\log\rho_-\big]=0.
$$

The former linear phase formula for this imaginary trace is false. At singular $\rho_-$ the logarithm also requires a support restriction or regularization. Taking a real part and then claiming a nonzero imaginary part is not a microscopic Keldysh construction.

A Berry term can be defined separately for a specified smooth nondegenerate eigenline over a parameter region. In a local normalized gauge $u(x)$, choose

$$
\mathcal A=i\langle u,du\rangle,\qquad \gamma(C)=\oint_C\mathcal A\pmod{2\pi}.
$$

Gauge changes alter $\mathcal A$ by an exact form; global consistency uses transition functions and a supplied line bundle. Degeneracies need a higher-rank bundle/non-Abelian connection. Its existence, adiabatic regime and relation to UHM's physical fields are additional model hypotheses [H/Pr]. A local polynomial $\beta B_{ab}\theta_a\dot\theta_b$ on lifted angular coordinates is not automatically a global one-form on a torus or a quantized topological term.

The fixed coordinate phase torus has no general continuous $G_2$ conjugation action: conjugation changes coherence moduli and populations. A selected positive three-form therefore does not make these phase polynomials $G_2$ invariant or determine their coefficient. Even for three variables permuted by $S_3$, symmetric quadratic forms have two independent terms $a\sum x_i^2+b\sum_{i<j}x_ix_j$; symmetry alone does not fix an off-diagonal ansatz. Finite cyclic-sum arithmetic in the next sections remains a chosen-form calculation; the former continuous covariance/unique physical derivation is withdrawn [✗].

A controlled open-system action must be derived from its microscopic dynamics and noise, as in [Sieberer–Buchhold–Diehl](https://arxiv.org/abs/1512.00637). That method does not establish the previously displayed UHM action.

## 10. $G_2$-Orientational Symmetry

### 10.1 Three Summation Variants

When computing the winding phase $\Phi(\mathbf{n})$ from the topological term, the question arises as to the range of summation:

| Variant | Terms | Rank | Chosen-form symmetry (continuous $G_2$ claim withdrawn) |
|---------|-----------|------|---------------------|
| (a) Full antisymmetrisation | 42 | **0** (identically zero) | Yes |
| (b) Cyclic sum | 21 | **21** (non-degenerate) | **Yes** |
| (c) Monomial ($i<j<k$) | 7 | 14 (degenerate) | No |

### 10.2 Full Antisymmetrisation Yields Zero

:::tip Theorem 3.1 [T]
Full antisymmetrisation (variant (a), all 6 permutations per line) gives an identically zero quadratic winding phase:

$$
B^{(a)}(\mathbf{n}) = \frac{1}{6}\sum_{i,j,k=1}^{7} \varepsilon_{ijk}\,n_{ij}\,n_{jk} \equiv 0
$$

for all $\mathbf{n}$ with symmetric $n_{ij} = n_{ji}$.
:::

**Proof.** For each Fano line $\{a,b,c\}$ with $\varepsilon_l = \varepsilon_{abc}$, expanding the 6 permutations (using $n_{ij} = n_{ji}$):

| Permutation | $\varepsilon$ | Product $n \cdot n$ |
|-------------|---|----------|
| $(a,b,c)$ | $+\varepsilon_l$ | $n_{ab}n_{bc}$ |
| $(b,c,a)$ | $+\varepsilon_l$ | $n_{bc}n_{ac}$ |
| $(c,a,b)$ | $+\varepsilon_l$ | $n_{ac}n_{ab}$ |
| $(a,c,b)$ | $-\varepsilon_l$ | $n_{ac}n_{bc}$ |
| $(c,b,a)$ | $-\varepsilon_l$ | $n_{bc}n_{ab}$ |
| $(b,a,c)$ | $-\varepsilon_l$ | $n_{ab}n_{ac}$ |

Sum: $+\varepsilon_l(n_{ab}n_{bc} + n_{bc}n_{ac} + n_{ac}n_{ab}) - \varepsilon_l(n_{ac}n_{bc} + n_{bc}n_{ab} + n_{ab}n_{ac}) = 0$. $\blacksquare$

### 10.3 Cyclic Formula

:::tip Theorem 3.2 [T]
At the declared oriented cyclic convention, the sum gives a **non-zero non-degenerate** quadratic form [T at that convention]:

$$
B^{(b)}(\mathbf{n}) = \sum_{l=1}^{7} \varepsilon_l \left(n_{ab}n_{bc} + n_{bc}n_{ca} + n_{ca}n_{ab}\right)
$$

with matrix $\tilde{M} = \bigoplus_{l=1}^{7} \varepsilon_l(J_3 - I_3)$, rank $= 21$.
:::

Each block $(J_3 - I_3)$ has eigenvalues $2$ (multiplicity 1), $-1$ (multiplicity 2) — non-degenerate.

### 10.4 Monomial Formula — Degenerate

:::tip Theorem 3.3 [T]
The canonical monomial formula (variant (c), only $i<j<k$) gives a **degenerate** quadratic form:

$$
B^{(c)}(\mathbf{n}) = \sum_{l:\,a<b<c} \varepsilon_{abc}\,n_{ab}\,n_{bc}
$$

with rank 14 and $\dim\ker = 7$.
:::

**Proof.** For each line $\{a,b,c\}$ ($a<b<c$): the single term $n_{ab}n_{bc}$ connects edges $(a,b)$ and $(b,c)$ through the middle vertex $b$. The edge $(a,c)$ **does not participate** — it is "orphaned".

The symmetrised matrix for block $l$ in the basis $(n_{ab}, n_{ac}, n_{bc})$:

$$
\tilde{M}_l^{(c)} = \frac{\varepsilon_l}{2}\begin{pmatrix} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 0 \end{pmatrix}
$$

Eigenvalues: $\pm\varepsilon_l/2$ (multiplicity 1 each), $0$ (multiplicity 1). Block rank = 2. Full rank: $2 \times 7 = 14$. Kernel: 7 orphaned edges. $\blacksquare$

### 10.5 Violation of $G_2$-Covariance by the Monomial Formula

The canonical ordering $i<j<k$ singles out the middle vertex $b$, breaking the **cyclic** $\mathbb{Z}_3$-symmetry of the Fano line. The stabiliser of the line in $\mathrm{PSL}(2,7) \cong \mathrm{Aut}(\mathrm{Fano})$ contains $\mathbb{Z}_3$:

$$
(a,b,c) \to (b,c,a) \to (c,a,b)
$$

The monomial formula is **not invariant** under $\mathbb{Z}_3$ — this is a coordinate artefact, not a physical structure.

---

## 11. Chosen bilinear form and the failed uniqueness argument

#### Scope of former Theorem 4.1 {#единственность-билинейной-формы-bb}

The universal unique $G_2$-covariant winding-form claim is withdrawn [✗]. There is no such continuous action on the fixed-modulus phase torus. Even a single line with its three **unsigned unordered edge variables** has the two-dimensional space of $S_3$-invariant quadratic forms

$$
Q=a(x_1^2+x_2^2+x_3^2)+b(x_1x_2+x_2x_3+x_3x_1).
$$

Permutations impose equality of diagonal entries and equality of off-diagonal entries, leaving $a,b$ independent [T]. The identity $n_{ij}=n_{ji}$ does not remove diagonal terms. An oriented weight acquires signs under orientation-reversing permutations, so it needs an explicitly supplied representation/action before invariance is tested.

If one **declares** zero diagonal, independent line blocks, common line coefficient and an oriented cyclic ordering, its off-diagonal cyclic form is fixed up to that coefficient [T at those additional restrictions]. Those restrictions are model data [D], not consequences of $G_2$, Keldysh or physical vacuum uniqueness. The finite rank/Gauss-sum calculations below concern this chosen arithmetic form; their use for physical winding sectors requires a measure and energy bridge [H].

### 11.1 Recovery of 9 Orders

With the three-term formula ($B^{(b)}$, rank 21) the Gaussian sum gives:

$$
|G_7| = 7^{21/2}, \quad \frac{|G_7|}{7^{21}} = 7^{-21/2} \approx 10^{-8.87}
$$

| Aspect | Monomial (c) | Cyclic (b) |
|--------|-----------------|-----------------|
| Rank | 14 | **21** |
| Suppression | $10^{-5.9}$ | **$10^{-8.9}$** |
| Chosen-form symmetry (continuous $G_2$ claim withdrawn) | No | **Yes** |

:::info Caveat
Although the mathematical result of the Gaussian sum is rigorous, at physical $S_0 = 20$ destructive interference **does not work** (dominant sectors have zero phase). See the [Cosmological Constant](/docs/physics/gravity/cosmological-constant#7-сумма-гаусса-для-фано-фаз) page for details.
:::

---

## 12. Connection to Other Sections

| Topic | Page | Connection |
|------|----------|-------|
| $G_2$-Structure | [$G_2$-Structure and the Fano Plane](/docs/physics/gauge-symmetry/g2-structure) | Associative 3-form $\varphi$ and Fano triplets |
| Cosmological constant | [Cosmological constant](/docs/physics/gravity/cosmological-constant) | Gauss sum of the selected form |
| Dark matter | [Dark matter](/docs/physics/cosmology-phys/dark-matter) | Open protection of a proposed relic |
| Einstein equations | [Einstein equations](/docs/physics/gravity/einstein-equations) | Conditions for metric dynamics |
| Emergent geometry | [Emergent geometry](/docs/physics/gravity/emergent-geometry) | State and spatial distances |
| Gap Dynamics | [Gap Dynamics](/docs/core/dynamics/gap-dynamics) | Topological term $\mathcal{L}_{\mathrm{top}}$ in the Gap Lagrangian |
| Fano Selection Rules | [Fano Selection Rules](/docs/physics/gauge-symmetry/fano-selection-rules) | Fano triplets and cyclic orientation |

---

**Related documents:**
- [Gap Semantics: 49 Elements](/docs/physics/dual-aspect/gap-semantics)
- [G₂-Structure and the Fano Plane](/docs/physics/gauge-symmetry/g2-structure)
- [Topological Protection of Coherence](/docs/applied/coherence-cybernetics/topological-protection)
- [Vacuum Uniqueness](/docs/proofs/categorical/uniqueness-theorem)
