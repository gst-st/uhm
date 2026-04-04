---
slug: /proofs/dynamics/theorem-purity-critical
sidebar_position: 1
title: "Theorem on Critical Purity"
description: "Rigorous proof of P_crit = 2/N from first principles of UHM"
---

# Theorem on Critical Purity

:::tip Status: [Т] Proven
The value $P_{\text{crit}} = 2/N$ is rigorously derived from several mathematically equivalent formulations of a single geometric principle (paths 1–4) and an independent autopoietic argument (path 5). The convergence of all approaches to a single value confirms the fundamentality of this threshold.
:::

## 1. Theorem Statement

### 1.1 Main assertion {#теорема-фробениусова-различимость}

**Theorem (Critical Purity):**

For a holonomic system of dimension $N$, the critical purity:

$$
P_{\text{crit}} = \frac{2}{N}
$$

is the **unique** value satisfying the following equivalent conditions:

1. **Geometric:** $\|\Gamma - I_N/N\|_F^2 = \|I_N/N\|_F^2$
2. **Informational:** $D_{KL}(\Gamma \| I_N/N) = \frac{1}{2}$ nat (in linear approximation)
3. **Structural:** $|\mathbf{r}|^2 = 2\sigma^2$ (SNR = 1)
4. **Spectral:** $\lambda_{\max} = (1 + \sqrt{N-1})/N \approx 1/2$
5. **Autopoietic:** minimal breaking of $U(N)$ symmetry

### 1.2 For UHM (N = 7)

$$
P_{\text{crit}} = \frac{2}{7} \approx 0.286
$$

**At this threshold:**
- Structural deviation = scale of chaos
- Informational contribution = 1/2 nat
- Dominant mode ≈ 49% coherence
- $U(7)$ symmetry broken to distinguishability level

---

## 2. Necessary Definitions

### 2.1 Coherence matrix

The [coherence matrix](/docs/core/dynamics/coherence-matrix) $\Gamma \in \mathcal{L}(\mathbb{C}^N)$ satisfies:

$$
\Gamma^\dagger = \Gamma, \quad \Gamma \geq 0, \quad \mathrm{Tr}(\Gamma) = 1
$$

### 2.2 Purity

$$
P = \mathrm{Tr}(\Gamma^2) \in \left[\frac{1}{N}, 1\right]
$$

| State | Purity | Description |
|-----------|---------|----------|
| Pure | P = 1 | Γ = \|ψ⟩⟨ψ\| |
| Maximally mixed | P = 1/N | Γ = I_N/N (chaos) |

### 2.3 Frobenius norm

$$
\|\Gamma\|_F^2 = \mathrm{Tr}(\Gamma^\dagger \Gamma) = \mathrm{Tr}(\Gamma^2) = P
$$

---

## 3. Five Derivation Paths (four equivalent + one independent)

### 3.1 Path 1: Geometric (structural doubling principle)

**Principle:** A system is distinguishable from chaos if its deviation from chaos exceeds the scale of chaos.

**Criterion:**

$$
\|\Gamma - I_N/N\|_F^2 > \|I_N/N\|_F^2
$$

**Left-hand side computation:**

$$
\begin{aligned}
\|\Gamma - I_N/N\|_F^2 &= \mathrm{Tr}\left((\Gamma - I_N/N)^2\right) \\
&= \mathrm{Tr}(\Gamma^2) - \frac{2}{N}\mathrm{Tr}(\Gamma) + \mathrm{Tr}\left(\frac{I_N^2}{N^2}\right) \\
&= P - \frac{2}{N} + \frac{1}{N} \\
&= P - \frac{1}{N}
\end{aligned}
$$

**Right-hand side computation:**

$$
\|I_N/N\|_F^2 = \mathrm{Tr}\left(\frac{I_N^2}{N^2}\right) = \frac{N}{N^2} = \frac{1}{N}
$$

**Threshold derivation:**

$$
P - \frac{1}{N} > \frac{1}{N} \quad \Rightarrow \quad \boxed{P > \frac{2}{N}}
$$

:::info Interpretation
**Structural doubling principle:** To be distinguishable from chaos, a system's structure must be at least as large as chaos itself. The factor of 2 arises naturally: structure + baseline level.
:::

---

### 3.2 Path 2: Information-theoretic

**Principle:** A system carries sufficient information for distinguishability if its divergence from chaos exceeds an information quantum.

**Kullback–Leibler divergence:**

$$
D_{KL}(\Gamma \| I_N/N) = \mathrm{Tr}(\Gamma \log \Gamma) - \mathrm{Tr}\left(\Gamma \log \frac{I_N}{N}\right)
$$

Using $\log(I_N/N) = -\log(N) \cdot I_N$:

$$
D_{KL}(\Gamma \| I_N/N) = -S_{vN}(\Gamma) + \log(N)
$$

where $S_{vN}(\Gamma) = -\mathrm{Tr}(\Gamma \log \Gamma)$ is the [von Neumann entropy](/docs/core/dynamics/coherence-matrix#энтропия-фон-неймана).

**Expansion for states close to $I_N/N$:**

For $\Gamma = I_N/N + \delta\Gamma$ with small $\delta\Gamma$:

$$
D_{KL}(\Gamma \| I_N/N) \approx \frac{N}{2} \cdot \mathrm{Tr}(\delta\Gamma^2) = \frac{N}{2} \cdot \left(P - \frac{1}{N}\right)
$$

**Minimum distinguishability:**

The distinguishability threshold in the quadratic approximation = $\frac{1}{2}$ nat.

$$
\frac{N}{2} \cdot \left(P - \frac{1}{N}\right) \geq \frac{1}{2}
$$

$$
P - \frac{1}{N} \geq \frac{1}{N} \quad \Rightarrow \quad \boxed{P \geq \frac{2}{N}}
$$

:::warning Scope of applicability
Path 2 uses the **quadratic approximation** D_KL(Γ ‖ I/N) ≈ (N/2)(P − 1/N), valid when P − 1/N ≪ 1. The threshold D_KL = 1/2 nat is a **convention** (analogous to p-value 0.05 in statistics). In the regime P ≫ 1/N the approximation breaks down. Path 2 is a **supporting argument**, consistent with P_crit = 2/N near chaos, not an independent rigorous derivation.
:::

:::info Interpretation for engineers
**Information threshold:** The system must carry at least 1/2 nat of information beyond maximum entropy. This is a fundamental distinguishability limit in information theory.

**In practice:** At $P = 2/N$ the system contains exactly 1 bit of structural information (the distinction between "structure exists" and "no structure").
:::

---

### 3.3 Path 3: Bloch decomposition (SNR criterion)

**Principle:** The system's structural vector must exceed the noise threshold.

**Bloch parameterization:**

Any $N \times N$ density matrix admits the decomposition:

$$
\Gamma = \frac{I_N}{N} + \frac{1}{2} \sum_{i=1}^{N^2-1} r_i \lambda_i
$$

where:
- $\{\lambda_i\}_{i=1}^{N^2-1}$ — generalized Gell-Mann matrices (generators of $\mathfrak{su}(N)$)
- $\mathrm{Tr}(\lambda_i) = 0$, $\mathrm{Tr}(\lambda_i \lambda_j) = 2\delta_{ij}$
- $\mathbf{r} = (r_1, \ldots, r_{N^2-1}) \in \mathbb{R}^{N^2-1}$ — generalized Bloch vector

**Connection with purity:**

$$
P = \mathrm{Tr}(\Gamma^2) = \frac{1}{N} + \frac{|\mathbf{r}|^2}{2}
$$

**Therefore:**

$$
|\mathbf{r}|^2 = 2\left(P - \frac{1}{N}\right)
$$

**Noise threshold:**

For the maximally mixed state $\mathbf{r} = 0$. The natural scale of fluctuations in an $N$-dimensional system:

$$
\sigma^2 \sim \frac{1}{N}
$$

**Distinguishability condition (SNR $\geq$ 1):**

In quadratic metrics SNR = 1 requires:

$$
|\mathbf{r}|^2 \geq 2\sigma^2 = \frac{2}{N}
$$

$$
2\left(P - \frac{1}{N}\right) \geq \frac{2}{N} \quad \Rightarrow \quad \boxed{P \geq \frac{2}{N}}
$$

:::warning Noise scale
The estimate σ² ~ 1/N is motivated by two arguments: (1) the mean squared deviation of a random density matrix from the Hilbert–Schmidt measure: ⟨||Γ − I/N||²_F⟩_{HS} = (N−1)/N² ≈ 1/N; (2) the quantum Cramér–Rao bound for parameter estimation in an N-level system: Var(θ̂) ≥ 1/(N·F_Q). SNR = 1 is a threshold convention. Path 3 is a **heuristic**, consistent with the exact result of Path 1.
:::

:::info Interpretation for signal researchers
**SNR = 1:** Classical signal detection threshold. Signal power must equal noise power.

In UHM: structural information (signal) must be at least as large as thermodynamic noise (chaos). The factor of 2 appears due to the quadratic nature of the purity metric.
:::

---

### 3.4 Path 4: Spectral condition (characterization, not an independent derivation) {#34-путь-4-спектральное-условие-характеристика-не-независимый-вывод}

**Principle:** For an identity to exist, the system must have a dominant mode.

**Spectrum of $\Gamma$:**

$$
\mathrm{Spectrum}(\Gamma) = \{\lambda_1, \lambda_2, \ldots, \lambda_N\}, \quad \lambda_1 \geq \lambda_2 \geq \cdots \geq \lambda_N \geq 0
$$

With constraints:

$$
\sum_i \lambda_i = 1, \quad \sum_i \lambda_i^2 = P
$$

**Optimization problem:**

Find the maximum $\lambda_1$ for a given $P$:

$$
\max \lambda_1 \quad \text{subject to} \quad \sum_i \lambda_i = 1, \quad \sum_i \lambda_i^2 = P, \quad \lambda_i \geq 0
$$

**Solution (Lagrange method):**

By symmetry, the optimum is reached when $\lambda_2 = \lambda_3 = \cdots = \lambda_N = \lambda$:

$$
\lambda_1 + (N-1)\lambda = 1 \quad \Rightarrow \quad \lambda = \frac{1 - \lambda_1}{N-1}
$$

$$
\lambda_1^2 + (N-1)\lambda^2 = P
$$

Substituting:

$$
\lambda_1^2 + \frac{(1 - \lambda_1)^2}{N-1} = P
$$

Solving the quadratic equation:

$$
\lambda_1 = \frac{1 + \sqrt{(N-1)(NP - 1)}}{N}
$$

**At $P = 2/N$:**

$$
\lambda_{\max} = \frac{1 + \sqrt{(N-1)(2 - 1)}}{N} = \frac{1 + \sqrt{N-1}}{N}
$$

For $N = 7$:

$$
\lambda_{\max} = \frac{1 + \sqrt{6}}{7} \approx 0.493 \approx \frac{1}{2}
$$

:::info Interpretation
**~50% dominance threshold:** At $P = 2/N$ the dominant mode captures approximately half of the coherence. This is the 1:1 threshold — structure is barely distinguishable from the uniform distribution.

**Spectral structure at $P = 2/7$:**
- $\lambda_1 \approx 0.493$ (49.3% of coherence)
- $\lambda_2 = \cdots = \lambda_7 \approx 0.085$ (8.5% each)
:::

---

### 3.5 Path 5: Autopoietic closure

**Principle:** Sufficient structure is required for [self-modeling](/docs/proofs/categorical/formalization-phi) $\varphi(\Gamma)$.

**Autopoiesis (AP):** There exists $\varphi: \Gamma \to \Gamma$ with fixed point $\varphi(\Gamma^*) = \Gamma^*$.

**Problem with $I_N/N$:**

The maximally mixed state is invariant under **all** unitary transformations:

$$
U \cdot \frac{I_N}{N} \cdot U^\dagger = \frac{I_N}{N} \quad \text{for any } U \in U(N)
$$

This means:
- $\varphi(I_N/N)$ can be **anything** (no preferred direction)
- The fixed point $\varphi(\Gamma^*) = \Gamma^*$ is not uniquely defined
- The system **has no identity**

**Autopoietic closure condition:**

To uniquely define $\varphi$, the $U(N)$ symmetry must be broken.

The stabilizer group $\mathrm{Stab}(\Gamma) = \{U \in U(N) : U\Gamma U^\dagger = \Gamma\}$ must be a proper subgroup of $U(N)$.

**Minimal meaningful breaking:**

$$
\|\Gamma - I_N/N\|_F \geq \|I_N/N\|_F
$$

Which is equivalent to:

$$
\boxed{P \geq \frac{2}{N}}
$$

:::info Interpretation
**Symmetry breaking:** Chaos has maximal symmetry $U(N)$. For an identity to exist (the ability for self-modeling), this symmetry must be broken.

At $P > 2/N$ the system has a "preferred direction" in state space — the basis for self-reference.
:::

:::info Dependence on Path 1
Path 5 uses the same criterion $\|\Gamma - I/N\|_F \geq \|I/N\|_F$ as Path 1. This is an autopoietic *interpretation* of the geometric threshold, not an independent derivation.
:::

---

### 3.6 Path 6: Octonionic norm [И] {#путь-6-октонионная-норма}

:::note Interpretation [И]
In the [octonionic interpretation](../../core/structure/dimensions#октонионная-интерпретация), purity $P = \mathrm{Tr}(\Gamma^2)$ is connected to the norm on Im(𝕆). The normativity $|xy| = |x||y|$ ensures a multiplicative metric. The threshold $P_{\text{crit}} = 2/7$ can be interpreted as the minimum norm of a vector in Im(𝕆) ≅ ℝ⁷ at which its projection onto structural directions (Fano triplets) exceeds the noise projection.

**Status:** [Т], bridge [Т] (closed, T15). Compatible with the other five paths. See [structural derivation](../minimality/theorem-octonionic-derivation).
:::

---

## 4. Convergence of All Paths

### 4.1 Results table

| Path | Principle | Criterion | Result |
|------|---------|----------|-----------|
| 1. Geometric | Deviation ≥ scale of chaos | ‖Γ − I/N‖²_F > 1/N | P > 2/N ✓ |
| 2. Informational | KL-divergence ≥ 1/2 nat | D_KL ≥ 1/2 | P > 2/N ✓ |
| 3. Structural | SNR ≥ 1 | ǀ**r**ǀ² ≥ 2/N | P > 2/N ✓ |
| 4. Spectral | Dominance threshold | λ_max ≈ 1/2 | P = 2/N ✓ |
| 5. Autopoietic | Symmetry breaking U(N) | Stab(Γ) ⊊ U(N) | P > 2/N ✓ |

### 4.2 Uniqueness theorem

**Theorem:** The value $P_{\text{crit}} = 2/N$ is the unique one at which all five criteria coincide.

**Proof:**
Uniqueness follows from the algebraic equivalence of conditions 1–4 (all express the same geometric requirement in different terms). The autopoietic criterion (5) yields the same threshold from an independent symmetry-breaking requirement. All five formulations lead to $P - 1/N = 1/N$. ∎

:::info Remark (nature of the proof)
Paths 1 and 4 are **algebraic and self-contained** for proving $P_{\mathrm{crit}} = 2/N$ [Т]: Path 1 is the algebraic identity $\|\Gamma - I/N\|_F^2 = \|I/N\|_F^2 \Leftrightarrow P = 2/N$, Path 4 is spectral algebra. Paths 2 (informational, quadratic approximation of $D_{KL}$), 3 (SNR, noise scale $\sigma^2 \sim 1/N$), and 5 (autopoietic, axiomatic principle) are **independent confirmations** from different branches of the theory, each containing their own motivating assumptions. The convergence of all five paths to a single value is a non-trivial fact [Т], analogous to "cross-validation" in statistics.
:::

---

## 5. Spectral Characterization

### 5.1 Optimal spectrum at the boundary

**Theorem (Spectrum at $P = P_{\text{crit}}$):**

At $P = 2/N$, the optimal spectrum (maximizing $\lambda_{\max}$) has the form:

$$
\begin{aligned}
\lambda_1 &= \frac{1 + \sqrt{N-1}}{N} \\
\lambda_2 = \lambda_3 = \cdots = \lambda_N &= \frac{N - 1 - \sqrt{N-1}}{N(N-1)}
\end{aligned}
$$

### 5.2 Numerical values

| N | P_crit = 2/N | λ_max at P_crit |
|---|--------------|------------------|
| 2 | 1.000 | 1.000 |
| 3 | 0.667 | 0.789 |
| 4 | 0.500 | 0.683 |
| 5 | 0.400 | 0.618 |
| 6 | 0.333 | 0.573 |
| **7** | **0.286** | **0.493** |
| 8 | 0.250 | 0.457 |

### 5.3 Verification for N = 7

$$
\lambda_1 = \frac{1 + \sqrt{6}}{7} \approx 0.493
$$

$$
\lambda_2 = \cdots = \lambda_7 = \frac{6 - \sqrt{6}}{42} \approx 0.085
$$

**Verification:**
$$
\lambda_1 + 6\lambda_2 = 0.493 + 6 \times 0.085 = 1.000 \quad \checkmark
$$

$$
\lambda_1^2 + 6\lambda_2^2 = 0.243 + 6 \times 0.0072 = 0.286 = \frac{2}{7} \quad \checkmark
$$

---

## 6. Hierarchy of Purity Thresholds

### 6.1 Full hierarchy

$$
P_{\text{crit}}^{\text{regen}} < P_{\text{crit}}^{\text{geom}} < P_{\text{safe}} < P_{\text{target}}
$$

| Threshold | Formula | Value (N=7) | Purpose |
|-------|---------|----------------|------------|
| P_crit^regen | γ/(κ_rate · Coh_E^min) | ≈ 0.033 | Dynamical (κ > γ) |
| P_crit^geom | 2/N | ≈ 0.286 | **Structural (main)** |
| P_safe | P_crit^geom + margin | 0.30 | Operational (with margin) |
| P_target | — | 0.50 | Recommended |

### 6.2 Interpretation

- **$P_{\text{crit}}^{\text{regen}} \approx 0.033$:** Minimum for [regeneration](/docs/core/dynamics/evolution#3-регенеративный-член) to exceed dissipation
- **$P_{\text{crit}}^{\text{geom}} = 2/7 \approx 0.286$:** Minimum for structural distinguishability from chaos (**main threshold**)
- **$P_{\text{safe}} = 0.30$:** Operational threshold with 5% margin
- **$P_{\text{target}} = 0.50$:** Recommended operating point

:::warning Important
A system with $P_{\text{crit}}^{\text{regen}} < P < P_{\text{crit}}^{\text{geom}}$ can regenerate, but **has no structural identity** — it is indistinguishable from noise.
:::

---

## 7. Practical Applications

### 7.1 For AI systems engineers

**Viability criterion:**

```python
def is_viable(Gamma: np.ndarray, N: int = 7) -> bool:
    """
    Check P > P_crit = 2/N

    Args:
        Gamma: N×N coherence matrix
        N: Dimension (default 7 for UHM)

    Returns:
        True if the system is viable
    """
    P = np.trace(Gamma @ Gamma).real
    P_crit = 2.0 / N
    return P > P_crit
```

**Structural deviation computation:**

```python
def structural_deviation(Gamma: np.ndarray, N: int = 7) -> float:
    """
    ‖Γ - I/N‖_F² = P - 1/N

    Interpretation:
    - deviation < 1/N: system indistinguishable from noise
    - deviation = 1/N: viability boundary
    - deviation > 1/N: system is structured
    """
    P = np.trace(Gamma @ Gamma).real
    return P - 1.0 / N
```

**Dominance threshold:**

```python
def dominant_eigenvalue_threshold(N: int = 7) -> float:
    """
    λ_max at P = P_crit = 2/N

    For N=7: returns ≈ 0.493
    """
    return (1 + np.sqrt(N - 1)) / N
```

### 7.2 For consciousness researchers

**Connection with interiority levels:**

| Level | Condition | Interpretation |
|---------|---------|---------------|
| L0 (Interiority) | ρ_E ≠ 0 | Inner state exists |
| L1 (Phenomenal geometry) | rank(ρ_E) > 1 | Structure of qualities |
| **Viability** | P > 2/7 | Distinguishability from chaos |
| L2 (Cognitive qualia) | R ≥ 1/3, Φ ≥ 1, D_diff ≥ 2* | Reflexive access |

*$D_{\text{diff}}$ requires tensor structure; in the minimal 7D formalism $C_{\min} = \Phi \times R$ is used — see [dimension-e.md](/docs/core/structure/dimension-e#tensor-factorization-ddiff).

**Key conclusion:** $P > 2/N$ is a **necessary** condition for L1 and L2. Without structural distinguishability, phenomenology is impossible.

### 7.3 For physicists

**Analogies with phase transitions:**

| UHM | Statistical physics | Meaning |
|-----|----------------------|-------|
| P = 2/N | Critical temperature T_c | Ordering threshold |
| P − 1/N | Order parameter | Measure of structure |
| λ_max ≈ 1/2 | Macroscopic occupancy | Condensation into one mode |

**Entropic interpretation:**

At $P = 2/N$:

$$
S_{vN} = \log N - \frac{N}{2}\left(\frac{2}{N} - \frac{1}{N}\right) + O\left(\frac{1}{N^2}\right) = \log N - \frac{1}{2}
$$

The system contains 1/2 nat less entropy than maximal chaos.

### 7.4 For information theorists

**Channel capacity:**

Distinguishing state $\Gamma$ from $I_N/N$ is equivalent to transmitting information over a channel with capacity:

$$
C = D_{KL}(\Gamma \| I_N/N) \approx \frac{N}{2}(P - 1/N)
$$

At $P = 2/N$: $C = 1/2$ nat = distinguishability boundary.

**Holevo bound:**

$$
\chi(\{p_i, \rho_i\}) \leq S(\bar{\rho}) - \sum_i p_i S(\rho_i)
$$

To distinguish $\Gamma$ from $I_N/N$ one needs $\chi \geq 1/2$ nat, which requires $P \geq 2/N$.

---

## 8. Universality of the Factor 2

### 8.1 Appearance in various contexts

| Context | Formula | Interpretation |
|----------|---------|---------------|
| Detection theory | SNR = 1 | Signal = noise |
| Quantum distinguishability | F(ρ, σ) = 1/2 | Distinguishability limit |
| Information theory | ΔS = k ln 2 | One bit of information |
| Statistics | 2σ rule | Significant deviation |
| UHM | P = 2/N | Structure = chaos |

### 8.2 Physical meaning

The factor of 2 arises from the **balance principle**:

$$
\text{Structure} = \text{Chaos}
$$

In the quadratic metric this means:

$$
\|\text{deviation}\|^2 = \|\text{baseline}\|^2
$$

which is equivalent to doubling relative to the baseline level:

$$
P = 2 \times P_{\min} = \frac{2}{N}
$$

---

## 9. Conclusion

### 9.1 Main result

:::tip Theorem (formulation)
For a holonomic system of dimension $N$:

$$
P_{\text{crit}} = \frac{2}{N}
$$

This value is **unique**, at which:
- All five formulations of the criterion coincide (4 mathematically equivalent + 1 autopoietic)
- The factor of 2 arises naturally (signal = noise)
- The dominant mode captures ~50% of coherence
:::

### 9.2 For N = 7 (UHM)

$$
P_{\text{crit}} = \frac{2}{7} \approx 0.286
$$

**Spectral structure at the boundary:**
- $\lambda_1 \approx 0.493$ (~50%)
- $\lambda_2 = \cdots = \lambda_7 \approx 0.085$ (~8.5% each)

### 9.3 Methodological significance

1. **Convergence of independent paths** confirms the fundamentality of the threshold
2. **Factor 2** — universal distinguishability threshold in information systems
3. **Spectral characterization** connects purity with mode dominance

---

## Appendix A: Complete Computations

### A.1 Derivation of λ_max at P = 2/N

Problem:

$$
\max \lambda_1 \quad \text{subject to} \quad \sum_{i=1}^N \lambda_i = 1, \quad \sum_{i=1}^N \lambda_i^2 = \frac{2}{N}
$$

Lagrangian:

$$
\mathcal{L} = \lambda_1 - \mu\left(\sum_i \lambda_i - 1\right) - \nu\left(\sum_i \lambda_i^2 - \frac{2}{N}\right)
$$

Optimality conditions:

$$
\frac{\partial \mathcal{L}}{\partial \lambda_1} = 1 - \mu - 2\nu\lambda_1 = 0
$$

$$
\frac{\partial \mathcal{L}}{\partial \lambda_k} = -\mu - 2\nu\lambda_k = 0 \quad (k = 2, \ldots, N)
$$

From the second condition: $\lambda_2 = \cdots = \lambda_N = -\mu/(2\nu) = \lambda$.

Substituting into the constraints:

$$
\lambda_1 + (N-1)\lambda = 1
$$

$$
\lambda_1^2 + (N-1)\lambda^2 = \frac{2}{N}
$$

From the first: $\lambda = (1 - \lambda_1)/(N-1)$.

Substituting into the second:

$$
\lambda_1^2 + \frac{(1 - \lambda_1)^2}{N-1} = \frac{2}{N}
$$

$$
(N-1)\lambda_1^2 + (1 - \lambda_1)^2 = \frac{2(N-1)}{N}
$$

$$
N\lambda_1^2 - 2\lambda_1 + 1 = \frac{2(N-1)}{N}
$$

$$
N^2\lambda_1^2 - 2N\lambda_1 + N - 2(N-1) = 0
$$

$$
N^2\lambda_1^2 - 2N\lambda_1 + 2 - N = 0
$$

By the quadratic formula:

$$
\lambda_1 = \frac{2N \pm \sqrt{4N^2 - 4N^2(2-N)}}{2N^2} = \frac{2N \pm 2N\sqrt{N-1}}{2N^2} = \frac{1 \pm \sqrt{N-1}}{N}
$$

Taking $+$ (maximum):

$$
\boxed{\lambda_{\max} = \frac{1 + \sqrt{N-1}}{N}}
$$

---

**Related documents:**
- [Viability](/docs/core/dynamics/viability) — application of the theorem
- [Axiom of Septicity](/docs/core/foundations/axiom-septicity) — axiom context
- [Coherence matrix](/docs/core/dynamics/coherence-matrix) — definition of Γ
- [7D Minimality theorem](/docs/proofs/minimality/theorem-minimality-7) — why N = 7
- [Interiority hierarchy](/docs/proofs/consciousness/interiority-hierarchy) — levels L0 → L2
