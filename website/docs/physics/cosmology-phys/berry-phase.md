---
sidebar_position: 2
title: "Berry Phase and Topological Protection"
slug: /physics/cosmology-phys/berry-phase
description: "Berry holonomy, G₂-orbit homotopy (T-25, T-69), canonical Singer cyclic Fano table, exact no-go results (T-17, T-85 withdrawn), and finite PSL(2,7) bilinear winding forms."
---

# Berry Phase and Topological Protection

A Berry phase is defined for an externally specified smooth family of nondegenerate eigenstates over a parameter manifold. This chapter establishes the exact homotopy of $G_2$ flag orbits (`T-25`, `T-69`), fixes the canonical Singer cyclic Fano table on `(A, S, D, L, E, U, O) = (1..7)`, records the exact negative theorems `T-17` (1D Chern–Simons vanishes) and `T-85 [✗]` (Keldysh Berry term vanishes identically), and classifies the bilinear winding forms under the finite collineation group $\mathrm{PSL}(2,7)$ (`T-20`, `T-162`).

## Overview

Neither a 1D Chern–Simons functional (`T-17 [T]`) nor the trace of a Hermitian Keldysh-type generator (`T-85 [✗]`) produces a topological Berry term for Gap phases. What survives rigorously is: (i) orbit homotopy (`T-25`, `T-69`), (ii) positivity bounds on individual coherences (`T-80`), and (iii) exact rank and finite-symmetry classification of chosen bilinear winding forms (`T-20`, `T-162`). Earlier universal phase-diagram/critical-exponent claims (`T-160 [✗]`, `T-161`) and off-topic neuroimaging/clinical sections have been removed.

---

## 1. Berry Connection and Holonomy

Let $\lambda \in M$ parametrize a smooth family of Hamiltonians $H_{\mathrm{eff}}(\lambda)$ with an isolated, nondegenerate normalized eigenstate $|n(\lambda)\rangle$. Along a closed loop $\gamma: [0,T] \to M$, adiabatic transport accumulates the geometric Berry phase

$$
\Phi_B = \oint_\gamma \mathcal{A}(\lambda) \cdot d\lambda \pmod{2\pi}, \qquad
\mathcal{A}(\lambda) = i\langle n(\lambda)|\nabla_\lambda|n(\lambda)\rangle.
$$

On a spanning surface $\Sigma$ in a compatible gauge, Stokes' theorem gives $\oint_{\partial\Sigma} \mathcal{A} = \int_\Sigma \mathcal{F} \pmod{2\pi}$. Two exact limitations apply:

1. **Noncontractible loops do not force a nonzero phase:** Even when $\pi_1(M) \neq 0$, a constant eigenstate has $\mathcal{A} = 0$ and $\Phi_B = 0$; conversely, a contractible loop can enclose nonzero Berry curvature $\mathcal{F}$.
2. **An octonionic 3-form does not supply a Berry bundle:** The associative 3-form on $\mathbb{R}^7$ fixes neither a Hamiltonian family $H_{\mathrm{eff}}(\lambda)$, nor an isolated eigenline, nor a global 1-form on the phase torus $(S^1)^{21}$.

---

## 2. Homotopy of $G_2$ Orbits (`T-25`, `T-69`)

For any closed subgroup $H$ of the compact, simply connected 14-dimensional Lie group $G_2$, the orbit dimension is $\dim(G_2/H) = 14 - \dim H$ (`[T under a specified group action]`), giving for example $G_2/\mathrm{SU}(3) \cong S^6$ (stabilizer of a unit imaginary octonion) and the 12-dimensional flag manifold $G_2/T^2$.

**Theorem T-25 / T-69 (Homotopy of the $G_2$ flag orbit) `[T for the specified target]`.**
Because $G_2$ is simply connected and $T^2$ is connected, the long exact homotopy sequence of $T^2 \to G_2 \to G_2/T^2$ yields

$$
\pi_1(G_2/T^2) = 0, \qquad \pi_2(G_2/T^2) \cong \pi_1(T^2) = \mathbb{Z}^2.
$$

The two winding integers classify based maps **$S^2 \to G_2/T^2$** (`[T]`). A single $7\times 7$ density matrix supplies no map from $S^2$ and no physical energy barrier; establishing a topological barrier requires an explicit field theory, boundary conditions, and action.

---

## 3. Positivity Bounds (`T-80`) and Canonical Singer Cyclic Fano Table {#секторная-gap-граница}

### 3.1 Refutation of the uniform $\mathrm{Gap} \le 1/2$ claim

In the Fano plane $\mathrm{PG}(2,2)$, every pair of distinct points lies on a unique line. On the canonical ordering $(A, S, D, L, E, U, O) = (1, 2, 3, 4, 5, 6, 7)$, the three lines through $O = e_7$ are $\{L, E, O\}$, $\{U, O, S\}$, and $\{O, A, D\}$. Incidence geometry imposes no upper bound of $1/2$ on individual phase gaps $\mathrm{Gap}(i,j) = |\sin\theta_{ij}|$: a valid positive semidefinite matrix $\Gamma \in \mathcal{D}(\mathbb{C}^7)$ can realize $\mathrm{Gap}(i,j) = 1$ on any chosen pair (for instance, purely imaginary coherences).

### 3.2 Coherence bound and withdrawal of the coordinate-triple sectoral table {#теорема-секторная-gap-граница}

**Theorem T-80 (`[T]` for positivity; `[C under supplied sector amplitudes]` for numerical bounds).**
Positivity of $\Gamma \in \mathcal{D}(\mathbb{C}^7)$ implies the exact pairwise bound

$$
|\gamma_{ij}|^2 \le \Gamma_{ii}\Gamma_{jj}, \qquad \mathrm{Gap}(i,j) \in [0, 1] \qquad \forall\, i \neq j.
$$

Any numerical hierarchy between $O$-pairs and non-$O$ pairs (such as $\mathcal{G}_{\mathrm{total}} = \mathcal{G}_O + O(\bar\varepsilon^2)$) holds **only conditionally** on externally supplied sector amplitudes (`(SV)`). The former sectoral table partitioning the six non-$O$ axes into real coordinate triples labelled $\mathbf{3}$-$\mathbf{3}$, $\bar{\mathbf{3}}$-$\bar{\mathbf{3}}$, and $\mathbf{3}$-$\bar{\mathbf{3}}$ is **deleted**: under $\mathrm{SU}(3) = \mathrm{Stab}_{G_2}(e_O)$, no real coordinate triple spans the complex triplet $\mathbf{3}$ or antitriplet $\bar{\mathbf{3}}$ (`T-48a [✗]`, `T-45b [✗]`), and no $G_2$-invariant potential derives such sector values (`T-64`).

### 3.3 Canonical Singer cyclic Fano table on `(A, S, D, L, E, U, O) = (1..7)`

Matching [Octonions and the Fano plane](/docs/physics/gauge-symmetry/g2-structure), each cyclic triple $(i, j, k)$ denotes $e_i e_j = e_k$ under the identification $(A, S, D, L, E, U, O) = (1, 2, 3, 4, 5, 6, 7)$:

| # | Cyclic index triple | Canonical axis triple |
|---|---|---|
| 1 | $(1, 2, 4)$ | $\{A, S, L\}$ |
| 2 | $(2, 3, 5)$ | $\{S, D, E\}$ |
| 3 | $(3, 4, 6)$ | $\{D, L, U\}$ |
| 4 | $(4, 5, 7)$ | $\{L, E, O\}$ |
| 5 | $(5, 6, 1)$ | $\{E, U, A\}$ |
| 6 | $(6, 7, 2)$ | $\{U, O, S\}$ |
| 7 | $(7, 1, 3)$ | $\{O, A, D\}$ |

---

## 4. Orbit Tangent Modes and Withdrawal of Universal Critical Exponents

For a smooth $G_2$-invariant potential with a critical point on an orbit $G_2/H$, the $14 - \dim H$ directions tangent to the orbit lie in the kernel of the Hessian (`[T under a specified smooth invariant action]`). Interpreting these flat directions as physical Goldstone bosons requires a field-theoretic kinetic term and dispersion relation.

Earlier sections asserting a universal three-phase Gap diagram, universal critical exponents ($\beta = 1/2$, $\gamma = 1$, $\nu = 1/2$, tricritical $\beta = 1/4$, $\delta = 5$), a false "logarithmic divergence" at Landau $\alpha = 0$ (Landau mean-field theory has a finite heat-capacity jump at $\alpha = 0$, not a logarithmic divergence), and fMRI/clinical-psychiatry identifications have been **deleted**: universal UHM phase-transition and critical-exponent claims are withdrawn (`T-160 [✗]`, and `T-161` applies strictly to a tuned even sextic scalar mean-field germ $A_5$ with zero quartic coupling).

---

## 5. Exact Negative Results: 1D Chern–Simons (`T-17`) and Keldysh Trace (`T-85 [✗]`) {#9-опровержение-cs-вывода}

### 5.1 Vanishing of the 1D Chern–Simons functional (`T-17 [T]`)

**Theorem T-17 (1D Chern–Simons is a total derivative) `[T]`.**
For any $\mathfrak{g}_2$-valued connection $\mathcal{A}(\tau) = \sum_{a=1}^{14} A_a(\tau) T_a$ (with $\mathrm{Tr}(T_a T_b) = \kappa \delta_{ab}$) on a 1D parameter base $\tau$:

1. The cubic wedge $\mathcal{A} \wedge \mathcal{A} \wedge \mathcal{A}$ vanishes identically because $d\tau \wedge d\tau = 0$.
2. The quadratic term is an exact total derivative:

$$
CS_1[\mathcal{A}] = \frac{1}{2}\mathrm{Tr}(\mathcal{A}\,\dot{\mathcal{A}}) = \frac{\kappa}{2}\sum_{a=1}^{14} A_a \dot{A}_a = \frac{d}{d\tau}\!\left(\frac{\kappa}{4}\sum_{a=1}^{14} A_a^2\right).
$$

For every periodic loop $A_a(\tau + T) = A_a(\tau)$, $\oint CS_1[\mathcal{A}]\,d\tau = 0$ identically. Thus 1D Chern–Simons generates **no** topological phase for winding sectors. $\blacksquare$

### 5.2 Reality of the Keldysh trace (`T-85 [✗]`) {#теорема-l-top-кельдыш}

**Theorem T-85 (Keldysh-to-Berry derivation) — retracted `[✗]`.**
For positive definite density matrices $\rho_+, \rho_-$ and any Hermiticity-preserving generator $\mathcal{L}$, both $\log \rho_-$ and $\mathcal{L}(\rho_+)$ are Hermitian. Because $\overline{\mathrm{Tr}(AB)} = \mathrm{Tr}(BA) = \mathrm{Tr}(AB)$ for every pair of Hermitian matrices $A, B$,

$$
\operatorname{Im}\mathrm{Tr}\!\left[\rho_+ \log \rho_- - \mathcal{L}(\rho_+)\log \rho_-\right] \equiv 0.
$$

Hermitian traces therefore cannot generate an imaginary topological Berry term $\mathcal{L}_{\mathrm{top}}$ for Gap phases. Constructing an open-system Berry term requires an explicitly specified smooth eigenline bundle and microscopic derivation (cf. [Sieberer–Buchhold–Diehl](https://arxiv.org/abs/1512.00637)). $\blacksquare$

---

## 6. Finite Collineation Symmetry $\mathrm{PSL}(2,7)$ and Selected Bilinear Winding Forms

Because conjugation by continuous $G_2$ on $\mathcal{D}(\mathbb{C}^7)$ changes populations and coherence moduli $|\gamma_{ij}|$, the fixed-modulus phase torus $(S^1)^{21}$ carries **no** continuous $G_2$ action. The combinatorial symmetries acting on the 21 unordered edge variables $n_{ij} = n_{ji}$ are permutations in the **finite collineation group** $\mathrm{Aut}(\mathrm{PG}(2,2)) \cong \mathrm{PSL}(2,7)$ of order 168.

### 6.1 Exact ranks of three summation conventions `[T]`

| Convention | Terms | Matrix / eigenvalues | Rank | $\mathbb{Z}_3$-cyclic on each line |
|---|---|---|---|---|
| (a) Full antisymmetrization (all 6 perms/line) | 42 | Identically zero | **0** | Yes |
| (b) Oriented cyclic sum $B^{(b)}(\mathbf{n})$ | 21 | $\bigoplus_{l=1}^7 \varepsilon_l(J_3 - I_3)$; eigenvalues $2$ ($\times 7$), $-1$ ($\times 14$) | **21** | Yes |
| (c) Monomial ordering ($a<b<c$) $B^{(c)}(\mathbf{n})$ | 7 | 7 blocks of rank 2 + 7 orphaned edges | **14** | No |

1. **Full antisymmetrization vanishes (`[T]`):** For symmetric $n_{ij} = n_{ji}$ on any Fano line $\{a,b,c\}$, the 3 even permutations give $+\varepsilon_l(n_{ab}n_{bc} + n_{bc}n_{ca} + n_{ca}n_{ab})$ and the 3 odd permutations give its exact negative, summing to $0$.
2. **Cyclic sum is nondegenerate (`[T]`, cf. `T-162`):** Declaring an oriented cyclic ordering per line gives
   $$
   B^{(b)}(\mathbf{n}) = \sum_{l=1}^7 \varepsilon_l\left(n_{ab}n_{bc} + n_{bc}n_{ca} + n_{ca}n_{ab}\right)
   $$
   with block-diagonal symmetric matrix $\bigoplus_{l=1}^7 \varepsilon_l(J_3 - I_3)$ of full rank 21 (unsigned spectrum matching `T-162`).
3. **Monomial sum is degenerate (`[T]`):** Keeping only $a < b < c$ omits edge $(a,c)$ on every line, leaving 7 orphaned edges and $\dim\ker = 7$ (rank 14).

### 6.2 Breaking of Finite Collineation Symmetry $\mathrm{PSL}(2,7)$ by the Monomial Formula

The coordinate ordering $a < b < c$ singles out the middle vertex $b$ on each line, breaking the cyclic $\mathbb{Z}_3$ subgroup inside the line stabilizer of the finite collineation group $\mathrm{PSL}(2,7) \cong \mathrm{Aut}(\mathrm{PG}(2,2))$ (order 168). The degeneracy of $B^{(c)}$ is thus an artefact of breaking finite $\mathrm{PSL}(2,7)$ collineation symmetry, not a violation of continuous $G_2$ covariance.

### 6.3 Scope of bilinear form selection (`T-20`) {#единственность-билинейной-формы-bb}

**Theorem T-20 (`[T in the off-diagonal one-line ansatz]`).**
On three unordered edge variables $(x_1, x_2, x_3)$ of a single Fano line, $S_3$-invariant quadratic forms form a **two-dimensional** space:

$$
Q(x_1, x_2, x_3) = a(x_1^2 + x_2^2 + x_3^2) + b(x_1 x_2 + x_2 x_3 + x_3 x_1).
$$

Symmetry alone does not eliminate diagonal squares ($a \neq 0$). Declaring zero diagonal ($a = 0$), independent line blocks, and common cyclic line orientation fixes $B^{(b)}$ up to overall scale as a model convention (`[D]`), not a consequence of $G_2$ or Keldysh dynamics. While the finite mod-7 Gauss sum of the rank-21 form obeys $|G_7|/7^{21} = 7^{-21/2} \approx 10^{-8.87}$, at physical Gaussian weighting $S_0 = 20$ the zero-winding sector dominates and yields negligible suppression (`T-19`, [Cosmological Constant](/docs/physics/gravity/cosmological-constant#7-сумма-гаусса-для-фано-фаз)).

---

## Related Documents

- [Octonions and the Fano plane](/docs/physics/gauge-symmetry/g2-structure) — canonical Singer cyclic table and $G_2$
- [Noether charges](/docs/physics/gauge-symmetry/noether-charges) — exact spectrum of $F_{21}$ (`T-162`)
- [Cosmological constant](/docs/physics/gravity/cosmological-constant#7-сумма-гаусса-для-фано-фаз) — Gauss sum at $S_0 = 20$ (`T-19`)
- [Dark matter](/docs/physics/cosmology-phys/dark-matter) — refutation of $O$-parity and coordinate-triple partitions
- [Zeta regularization](/docs/physics/dual-aspect/zeta-regularization) — lattice sum and `T-20`
