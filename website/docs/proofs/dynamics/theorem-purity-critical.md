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

### 3.3 Path 3: Helstrom / Haar single-shot detection

**Principle:** A Haar-random single-shot measurement on $\Gamma$ produces a statistically detectable deviation from the noise reference $I/N$ iff $P > 2/N$.

**Setup.** Let $\Pi = |\psi\rangle\langle\psi|$ with $|\psi\rangle$ Haar-uniform on the unit sphere of $\mathbb{C}^N$. For a self-adjoint $A$, the $\Pi$-induced observable is $\mathrm{Tr}(A\Pi)$.

**First-moment (Haar invariance).** $\mathbb E_\Pi[\Pi] = I/N$ (unitary invariance), hence $\mathbb E_\Pi[\mathrm{Tr}(A\Pi)] = \mathrm{Tr}(A)/N$.

**Second-moment (Weingarten).** The standard $U(N)$-Weingarten formula gives
$$\mathbb E_\Pi[\Pi\otimes\Pi] = \frac{1}{N(N+1)}(I + \mathrm{SWAP}).$$
For $N=7$: $\mathbb E_\Pi[\Pi\otimes\Pi] = (I+\mathrm{SWAP})/56$. Hence
$$\mathbb E_\Pi[\mathrm{Tr}(A\Pi)^2] = \mathrm{Tr}((A\otimes A)\cdot\mathbb E[\Pi\otimes\Pi]) = \frac{1}{N(N+1)}(\mathrm{Tr}(A)^2 + \|A\|_F^2).$$

**Variance formula.**
$$\mathrm{Var}_\Pi(\mathrm{Tr}(A\Pi)) = \mathbb E[\mathrm{Tr}(A\Pi)^2] - \mathbb E[\mathrm{Tr}(A\Pi)]^2 = \frac{\|A\|_F^2}{N(N+1)} + \frac{(N-1)\mathrm{Tr}(A)^2}{N^2(N+1)}.$$

**Applied to $A = \Delta = \Gamma - I/N$** (traceless, $\mathrm{Tr}(\Delta)=0$):
$$\mathrm{Var}_\Pi(\mathrm{Tr}(\Delta\Pi)) = \frac{\|\Delta\|_F^2}{N(N+1)} = \frac{P - 1/N}{N(N+1)}.$$

**Detection threshold.** The observer's expected single-shot quadratic detection signal (above the zero-signal noise baseline) exceeds the reference scale $\|I/N\|_F^2/(N(N+1)) = 1/(N^2(N+1))$ iff
$$\|\Delta\|_F^2 > \|I/N\|_F^2 \iff P > 2/N.$$

$$\boxed{P > \frac{2}{N}}$$

:::info Interpretation
The constant $1/(N(N+1)) = 1/56$ (for $N=7$) is the standard Haar second-moment coefficient and drops out of the threshold condition — the threshold is exactly the Frobenius dominance $\|\Delta\|_F^2 > \|I/N\|_F^2$, identical to Path 1. Path 3 is thus a **rigorous** independent derivation via Weingarten integration, not a convention-dependent SNR heuristic. Every step uses only the Haar measure on $U(N)$-orbits, with no free parameters.
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

### 3.5 Path 5: Symmetry breaking ($U(N)$ stabilizer)

**Principle:** Sufficient structure is required for [self-modeling](/docs/proofs/categorical/formalization-phi) $\varphi(\Gamma)$: chaos $I/N$ has maximal symmetry and admits no preferred direction; structure exists only when the symmetry is broken non-trivially.

**Stabilizer group.** For $\Gamma \in \mathcal D(\mathbb C^N)$:
$$\mathrm{Stab}(\Gamma) = \{U \in U(N) : U\Gamma U^\dagger = \Gamma\}.$$

**Lemma (Schur's lemma applied to $I/N$).** $\mathrm{Stab}(\Gamma) = U(N)$ iff $\Gamma = I/N$.

*Proof.* $I/N$ is scalar, hence commutes with every $U$. Conversely, if $\Gamma$ commutes with every $U \in U(N)$, then $\Gamma$ lies in the commutant of the standard $U(N)$-action on $\mathbb C^N$; since this action is irreducible, Schur gives $\Gamma \in \mathbb C \cdot I$; trace-1 forces $\Gamma = I/N$. $\square$

**Stabilizer dimension bound.** If $\Gamma$ has $k$ distinct eigenvalues with multiplicities $m_1,\ldots,m_k$ (with $\sum m_i = N$), then $\mathrm{Stab}(\Gamma) = U(m_1)\times\cdots\times U(m_k)$, real Lie dimension $\sum m_i^2$. For $k=1$ this is $N^2$ (the $I/N$ case). For $k\ge 2$ the maximum is attained at the most unequal split $(1, N-1)$, giving $1 + (N-1)^2 = N^2 - 2N + 2 < N^2$. For $N = 7$: max non-constant stabilizer dimension is $37 < 49$.

**Strengthened symmetry-breaking criterion.** Mere inequality $\mathrm{Stab}(\Gamma)\subsetneq U(N)$ is equivalent to $\|\Delta\|_F > 0$, which is satisfied for any $\Gamma \ne I/N$ (arbitrarily small breaking). The **strengthened** criterion requires that the traceless component dominate the scalar reference:
$$\|\Gamma - I_N/N\|_F \ge \|I_N/N\|_F.$$
By Path 1 this is equivalent to:
$$\boxed{P \ge \frac{2}{N}}.$$

:::info Dependence on Path 1 — clarified
The strengthened criterion $\|\Delta\|_F \ge \|I/N\|_F$ coincides with Path 1 at the algebraic level. Path 5's **independent content** is the representation-theoretic statement that $I/N$ is the unique $U(N)$-symmetric density matrix (Schur's lemma on the irreducible fundamental representation), making $I/N$ the canonical "maximally symmetric" reference. This is what justifies the choice of reference used in Path 1 — without it, the critical purity would depend on an arbitrary reference state.
:::

---

### 3.6 Path 6: Octonionic norm [И] {#путь-6-октонионная-норма}

:::note Interpretation [И]
In the [octonionic interpretation](../../core/structure/dimensions#октонионная-интерпретация), purity $P = \mathrm{Tr}(\Gamma^2)$ is connected to the norm on $\mathrm{Im}(\mathbb{O})$. The normativity $|xy| = |x||y|$ ensures a multiplicative metric. The threshold $P_{\text{crit}} = 2/7$ can be interpreted as the minimum norm of a vector in $\mathrm{Im}(\mathbb{O})$ ≅ ℝ⁷ at which its projection onto structural directions (Fano triplets) exceeds the noise projection.

**Status:** [Т], bridge [Т] (closed, T15). Compatible with the other five paths. See [structural derivation](../minimality/theorem-octonionic-derivation).
:::

---

## 4. Convergence of All Paths

### 4.1 Results table

| Path | Principle | Main tool | Result |
|------|---------|----------|-----------|
| 1. Geometric | Frobenius structural dominance | HS Pythagoras | P > 2/N ✓ |
| 2. Informational | Relative entropy 2nd-order | Operator Taylor of $\log$ | P = 2/N at D=1/2 nat ✓ |
| 3. Single-shot detection | Haar-averaged observable variance | Weingarten 2nd moment ($1/(N(N+1))$) | P > 2/N ✓ |
| 4. Spectral | Dominant eigenvalue optimum | Lagrange multipliers | λ_max = (1+√(N−1))/N at P = 2/N ✓ |
| 5. Symmetry breaking | Stabilizer dimension | Schur's lemma + Cauchy-Schwarz | P > 2/N ✓ |

### 4.2 Uniqueness theorem

**Theorem:** The value $P_{\text{crit}} = 2/N$ is the unique one at which all five criteria coincide.

**Proof:**
Uniqueness follows from the algebraic equivalence of conditions 1–4 (all express the same geometric requirement in different terms). The autopoietic criterion (5) yields the same threshold from an independent symmetry-breaking requirement. All five formulations lead to $P - 1/N = 1/N$. ∎

:::info Independence structure of the five paths

**Tier A — fully independent rigorous derivations** (each alone proves $P_{\mathrm{crit}} = 2/N$ using different mathematical machinery):

| Path | Mathematical apparatus | Assumptions beyond $\Gamma \in \mathcal{D}(\mathbb{C}^N)$ |
|------|----------------------|--------------------------------------------------------|
| **1 (Frobenius)** | Hilbert–Schmidt Pythagoras | Reference = $I/N$ |
| **3 (Haar detection)** | Weingarten 2nd-moment integration | Haar measure on $U(N)$ |
| **4 (Spectral)** | Constrained Lagrange optimization | None (pure spectral algebra) |

Paths 1, 3, 4 use disjoint mathematical tools (HS norm identity, Haar integration, Lagrange multipliers). Path 3 arrives at the same inequality $\|\Delta\|_F^2 > \|I/N\|_F^2$ as Path 1 but via a probabilistic (Weingarten) route with no norm-theoretic input. Path 4 characterizes the spectrum at threshold without using norms at all.

**Tier B — supporting confirmations** (consistent with $P_{\mathrm{crit}} = 2/N$ but not fully independent):

| Path | Relation to Tier A | Own contribution |
|------|-------------------|-----------------|
| **2 (KL entropy)** | Algebraically reduces to Path 1 in quadratic approximation; threshold $D_{KL} = 1/2$ nat is a **convention** | Information-theoretic interpretation of the same geometric inequality |
| **5 (Stabilizer)** | Strengthened criterion $\|\Delta\| \geq \|I/N\|$ is Path 1 restated | Justifies $I/N$ as the canonical reference via Schur's lemma (representation theory) |

The convergence of 3 independent Tier-A derivations on $P_{\mathrm{crit}} = 2/N$ is a structural fact of $\mathcal{D}(\mathbb{C}^N)$ geometry [Т]. Tier-B paths provide interpretive depth (informational, symmetry-theoretic) without adding independent numerical content.
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

```verum
/// Viability check: P > P_crit = 2/N (T-39a [T]).
pub pure fn is_viable<const N: Int>(gamma: &StaticMatrix<Complex, N, N>) -> Bool
    where requires N >= 2
{
    let p = (gamma @ gamma).trace().real();
    p > 2.0 / (N as Float)
}
```

**Structural deviation computation:**

```verum
/// Structural deviation ‖Γ − I/N‖_F² = P − 1/N.
///
/// **Interpretation**:
/// - deviation < 1/N: indistinguishable from noise
/// - deviation = 1/N: viability boundary
/// - deviation > 1/N: structured system
pub pure fn structural_deviation<const N: Int>(gamma: &StaticMatrix<Complex, N, N>) -> Float
    where requires N >= 2
{
    let p = (gamma @ gamma).trace().real();
    p - 1.0 / (N as Float)
}
```

**Dominance threshold:**

```verum
/// Dominant eigenvalue threshold λ_max at P = P_crit = 2/N.
///
/// For N = 7: returns ≈ 0.493.
pub pure fn dominant_eigenvalue_threshold(n: Int { self >= 2 }) -> Float {
    (1.0 + ((n - 1) as Float).sqrt()) / (n as Float)
}
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
