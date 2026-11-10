---
sidebar_position: 1
title: "Emergent Geometry"
slug: /physics/gravity/emergent-geometry
description: "State distinguishability, the spectrum of three charges, and the operational conditions for a common distance."
---

# Emergent Geometry

The Frobenius and Bures metrics compare preparations. A physical distance compares locations through an operation such as timing a signal. These measurements can vary independently.

:::note Historical precursors
The idea of the emergence of geometry traces back to several traditions:

- **Bernhard Riemann** (1854) suggested that the metric of space could be determined by the physical content — the "binding force" determines the geometry.
- **John Wheeler** (1960s) formulated the program of "geometrodynamics": spacetime is not an arena but a participant in physics.
- **Alain Connes** (1994) showed that all geometry (metric, differential structure, integration) can be recovered from **algebraic data** — the spectral triple $(\mathcal{A}, \mathcal{H}, D)$.
- **Ted Jacobson** (1995) derived the Einstein equations from horizon thermodynamics — the first example of "gravity from entropy".

The spectral construction below uses a Dirac operator on a chosen metric manifold. Its gravitational interpretation requires an observable that identifies the points of the manifold.
:::

## Overview

T-118–T-120 construct a mathematical product $\mathbb R\times S^3$ from a depth clock and a specified algebra of charge fluctuations. Two of the three charges carry colour information. Reading their joint spectrum as physical space is [I]. [Manifold construction](/docs/proofs/physics/emergent-manifold)

A different construction starts with achievable transfers between distinguishable stations. With a complete protocol class, finite attained costs, zero-cost separation and relay composition, the minimum cost is a directed distance. Reciprocity makes it symmetric. Agreement across probes and refinements needs further tests. Periodic examples realize a circle and a product of circles. A common physical distance in three space dimensions and a Lorentzian spacetime remain open. [Verified network results](/docs/reference/network-results)

---

## 1. Space as a Structure of Distinctions

Two distinct stations can prepare identical matrices. Their Frobenius distance is then zero even if a signal takes several ticks to travel between them.

### 1.1 Pre-metric from Coherence

For $M$ labelled preparations, pulling back the Frobenius distance gives a pseudometric on the labels.

$$
d_{\mathcal{G}}(m, n) := \|\Gamma_m - \Gamma_n\|_F = \sqrt{\mathrm{Tr}\!\left((\Gamma_m - \Gamma_n)^2\right)}
$$

Restricting the matrix to selected coordinates defines another readout. There is no invariant real spatial triplet of the six non-clock axes (§4.3).

### 1.2 From Pre-metric to Metric: Thermodynamic Limit

**T-117.** For bounded single-site observables, the commutator of their site averages scales as $O(M^{-1})$: only the $M$ same-site terms survive the $1/M^2$ normalization. The use of a fluctuation central limit theorem for interacting dynamics separately requires clustering. [T-117](/docs/proofs/physics/emergent-manifold#теорема-коммутативность-макроалгебры)

**T-119.** Generic commutativity gives a spectrum, without fixing its dimension. Here one chooses three commuting generators of a maximal torus of $\mathrm U(3)$. Their averages fill an octahedron, their centered $\sqrt M$-scaled fluctuations fill $\mathbb R^3$, and the minimal unitization of $C_0(\mathbb R^3)$ has spectrum $S^3$. This identifies the algebra used in T-120. A metric still enters through the Dirac operator $D$. [T-119](/docs/proofs/physics/emergent-manifold#теорема-эмерджентное-пространство)

$$
d_{\text{Connes}}(x, y) = \sup\{|f(x) - f(y)| : \|[D, f]\| \leq 1, \; f \in \mathcal{A}_{\text{macro}}\}
$$

---

## 2. Pre-metric on the Space of States

### 2.1 Frobenius Metric

:::tip Theorem 4.1 [T]
The space $\mathcal{D}(\mathcal{H})$ of density matrices with metric

$$
d_F(\rho_1, \rho_2) := \|\rho_1 - \rho_2\|_F = \sqrt{\mathrm{Tr}\!\left((\rho_1 - \rho_2)^2\right)}
$$

is a complete metric space.
:::

**Proof.** The Frobenius norm is the Hilbert–Schmidt norm, inducing a complete metric on $\mathcal{L}(\mathcal{H})$. Restriction to $\mathcal{D}(\mathcal{H})$ (a closed subset) preserves completeness. $\blacksquare$

Spatial localization would require an independently specified map from preparations to physical positions.

---

## 3. Information Geometry

### 3.1 Fisher–Rao Metric

:::tip [T] Quantum Fisher metric (standard result)
The natural Riemannian metric on $\mathcal{D}(\mathcal{H})$ is the quantum Fisher metric:

$$
g_{ij}^{(F)}(\rho) = \frac{1}{2}\mathrm{Tr}\!\left(\rho\{L_i, L_j\}\right)
$$

where $L_i$ are logarithmic derivatives: $\partial_i \rho = \frac{1}{2}\{\rho, L_i\}$.
:::

This metric defines the "distance" between quantum states and is connected to quantum estimation via the Cramér–Rao inequality:

$$
\mathrm{Var}(\hat{\theta}_i) \geq [g^{(F)}(\rho)]^{-1}_{ii}
$$

### 3.2 Uniqueness of the Bures Metric {#единственность-метрики-бюреса}

In the **classical** case the Fisher–Rao metric is the unique (up to normalization) monotone Riemannian metric on the simplex of probability distributions (Chentsov theorem, 1982). In the **quantum** case uniqueness is broken: by the Petz theorem (1996), on $\mathcal{D}(\mathcal{H})$ there exists an entire **family** of monotone metrics, parametrized by operator-monotone functions $f$.

:::warning Theorem (Privileged status of the Bures metric) [T]
The Bures metric (Axiom A2 of UHM) is distinguished within the Petz class as the **minimal** monotone metric:

$$
g_{\text{Bures}}(\rho) \leq g_f(\rho) \quad \text{for any monotone } g_f \text{ (Petz, 1996)}
$$

Explicit formula:

$$
d_B(\rho_1, \rho_2) = \sqrt{2\left(1 - \mathrm{Tr}\sqrt{\sqrt{\rho_1}\rho_2\sqrt{\rho_1}}\right)}
$$

:::

Minimality compares normalized monotone metrics on the state space. It supplies no physical length scale.

### 3.3 From Information Geometry to the Spacetime Metric

The finite internal data used in the product triple are

$$
(\mathcal{A}_{\text{int}}, \mathcal{H}_{\text{int}}, D_{\text{int}}) = \left(\mathbb{C} \oplus M_3(\mathbb{C}) \oplus M_3(\mathbb{C}), \; \mathbb{C}^7, \; D_{\text{Gap}}\right)
$$

Computing the Connes distance on a manifold uses the **external** Dirac operator $D_M$ of its metric. The finite $D_{\rm int}$ acts on a different factor. No equality of Bures distances and physical spacetime intervals follows from forming this product.

| Level | Metric | Space | Determines |
|---------|---------|--------------|------------|
| Quantum | $d_B(\rho_1, \rho_2)$ | $\mathcal{D}(\mathbb{C}^7)$ | State distinguishability |
| Spectral | $d_{\text{Connes}}(x, y)$ | $\Sigma^3$ | Spatial distance |
| Full | $ds^2 = g_{\mu\nu}dx^\mu dx^\nu$ | $M^4$ | Spacetime metric |

---

## 4. Emergent Dimensionality

### 4.1 Derivation of 3+1 Dimensions [C]

The macroscopic fluctuations of the three selected commuting charges fill $\mathbb R^3$. Minimal unitization gives $C(S^3)$. Two charges are colour Cartan generators, so interpreting the spectrum as ordinary space is an additional premise. T-118 supplies a time coordinate in the depth-clock scaling limit. [T-119 and T-120](/docs/proofs/physics/emergent-manifold#теорема-эмерджентное-пространство)

### 4.2 Resolved Questions

| Question | Answer | Theorem |
|--------|-------|---------|
| Why is the charge spectrum three-dimensional? | Three independent commuting charges have fluctuation spectra filling $\mathbb R^3$. | T-119 [T] |
| What fixes a Lorentzian signature? | The product has a one-dimensional clock factor. A Lorentzian realization requires metric and causality data. | T-53 [C] |
| How is the four-manifold constructed? | Combine the depth clock and the minimally unitized charge algebra. | T-120 [T] |

### 4.3 Sector Decomposition

With $\mathrm{SU}(3)=\mathrm{Stab}_{G_2}(e_O)$ the real representation is $\mathbb R e_O\oplus\mathbb R^6$, with irreducible complement. Only after complexification does it split as $\mathbb C e_O\oplus\mathbf3\oplus\bar{\mathbf3}$. A choice of real and imaginary coordinate axes breaks this symmetry. The colour-singlet spin factor in 48c has a determinant of signature $(1,3)$ under its stated algebraic inputs. Its identification with physical spacetime requires the additional locality premise. [48c](/docs/core/foundations/spacetime#теорема-48c)

---

## 5. Connection with General Relativity

### 5.1 Spectral Action

For a supplied four-dimensional spin geometry and internal operator, the spectral action is

$$
S_{\text{spec}}[\mathcal{A}, D] = \mathrm{Tr}\!\left(f(D^2/\Lambda^2)\right) + \frac{1}{2}\langle\psi, D\psi\rangle
$$

where $f$ is a smooth cutoff function, $\Lambda$ is the scale. Expansion in a series in $\Lambda$ gives:

$$
S_{\rm grav}=\frac{1}{16\pi G}\int_{M^4}(R-2\Lambda_{\rm CC})\sqrt g\,d^4x .
$$

This is the volume and Einstein–Hilbert part of the heat-kernel expansion. Other coefficients can include curvature-squared and internal-field terms. Their content depends on the supplied triple and cutoff. A Standard Model matter action needs its fermion module, representation and couplings. The seven-dimensional register supplies none of that spectrum. [Spectral action and matter inputs](/docs/physics/gravity/quantum-gravity#теорема-полное-спектральное-действие)

### 5.2 Summary of Results

| Result | Status | Theorem |
|-----------|--------|---------|
| Product $\mathbb R\times S^3$ | [T] for the selected algebras | [T-120](/docs/proofs/physics/emergent-manifold#теорема-произведение-троек) |
| Einstein equations from spectral action | **[T]** | [T-65](/docs/physics/gravity/einstein-equations) |
| Cosmological constant $\Lambda_{\text{CC}} > 0$ | **[H]** physical bridge; positivity follows conditionally for the selected positive readout | [T-71](/docs/core/foundations/consequences#теорема-лямбда-положительна) |
| Lovelock classification | [T] under the four-dimensional metric and differential hypotheses | [T-121](/docs/proofs/physics/emergent-manifold#теорема-лавлок-замыкание) |
| Vacuum topology $\Sigma^3 \cong S^3$ | **[T]** for the selected spatial algebra (T-119); round metric and $k=+1$ slicing **[C at supplied field, symmetry and global conditions]** | [T-120b](/docs/proofs/physics/emergent-manifold#следствие-вакуумная-топология) |

### 5.3 Lovelock Gaps and Their Closure

The Lovelock theorem (1971) states: the unique second-order tensor constructed from the metric and its derivatives up to second order, that is divergence-free, is the Einstein tensor $G_{\mu\nu} + \Lambda g_{\mu\nu}$. But the theorem **does not explain**:

| Gap | Question | UHM answer | Theorem |
|--------|--------|-----------|---------|
| 1 | Why $d=4$? | The clock and the three selected charge fluctuations give a mathematical product of dimension four. | T-120 [T] |
| 2 | Why Lorentzian signature? | The heat-kernel expansion uses Riemannian geometry. A Lorentzian model requires additional analytic data. | T-53 [C] |
| 3 | Why $\Lambda > 0$? | A supplied energy readout may have positive sign under explicit state and parameter conditions; autopoiesis and cohomology do not fix it | T-71 [H] |

---

## 6. Connection with Other Sections

| Topic | Page | Connection |
|------|----------|-------|
| Emergent manifold $M^4$ | [Emergent manifold](/docs/proofs/physics/emergent-manifold) | Derivation of $M^4$ from categorical structure (T-117 — T-121) |
| Einstein equations | [Einstein equations from Gap](/docs/physics/gravity/einstein-equations) | Derivation of $G_{\mu\nu}$ from spectral action |
| Cosmological constant | [Cosmological constant](/docs/physics/gravity/cosmological-constant) | Computation of $\Lambda$ and suppression mechanisms |
| Berry phase | [Berry phase](/docs/physics/cosmology-phys/berry-phase) | Holonomy for a specified connection |
| $G_2$ | [Octonionic structure](/docs/physics/gauge-symmetry/g2-structure) | Stabilizer of the chosen clock axis |
| Coherence matrix | [Coherence matrix](/docs/core/dynamics/coherence-matrix) | Definition of $\Gamma$ and coherences $\gamma_{ij}$ |

---

**Related documents:**
- [Einstein equations from Gap](/docs/physics/gravity/einstein-equations)
- [Quantum gravity](/docs/physics/gravity/quantum-gravity)
- [Spacetime](/docs/core/foundations/spacetime)
- [Emergent manifold $M^4$](/docs/proofs/physics/emergent-manifold)
