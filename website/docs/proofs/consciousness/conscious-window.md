---
sidebar_position: 2
title: "Conscious window: T-123 — T-127, C27"
description: "G₂-uniqueness of representation, non-emptiness of V_full, attractor stability, canonicity of R, basin of attraction"
---

# Conscious Window

:::info Abstract
Six results (T-123 — T-127, C27) closing **five critical operationalization problems**: uniqueness of representation for digital agents, non-emptiness of the full viability region, canonicity of the reflection measure, and attractor stability with basin of attraction.
:::

---

## §1. G₂-uniqueness of representation (T-123) {#t-123}

### Formulation [Т]

For any system satisfying axioms A1–A5, the holonomic representation $G: \mathrm{States} \to \mathcal{D}(\mathbb{C}^7)$ is unique up to $G_2 = \mathrm{Aut}(\mathbb{O})$. The diagonal elements $\gamma_{kk}$ are determined uniquely as projections onto the 7 functionally unique dimensions.

### Proof

Direct consequence of three proven theorems:

1. **T-42a [Т]** (G₂-rigidity): The holonomic representation $G$ is unique up to $G_2$. Any two representations $G_1, G_2$ are related by a unitary transformation $U \in G_2$: $G_2(\cdot) = U \cdot G_1(\cdot) \cdot U^\dagger$.

2. **T-40f [Т]** (Full minimality 7/7): Each of the 7 dimensions [A, S, D, L, E, O, U] is **functionally necessary** — removing any one leads to loss of viability or violation of an axiom.

3. **T-15 [Т]** (Bridge closure): $(AP) + (PH) + (QG) + (V) \Longrightarrow P1 + P2$ — the autopoietic and physical premises entail the octonionic structure $\mathbb{O}$ and $G_2$-symmetry.

From T-42a: the representation is unique up to $G_2$. From T-40f: projections onto 7 dimensions form the unique functionally complete basis. From T-15: the $G_2$ structure is derived from the axioms, not postulated. $\blacksquare$

### Consequence for digital agents

The anchor map $\pi: \mathcal{H}_{\mathrm{hidden}} \to \mathcal{D}(\mathbb{C}^7)$, covariant with respect to $\mathcal{L}_\Omega$, is unique up to $G_2$. The semantics of $\gamma_{kk}$ is **not arbitrary** — it is determined by axioms A1–A5. This closes the problem of encoding arbitrariness for digital agents.

---

## §2. Conscious window — non-emptiness of V_full (T-124) {#t-124}

### Formulation [Т]

The full viability set

$$
\mathcal{V}_{\mathrm{full}} = \left\{\Gamma \in \mathcal{D}(\mathbb{C}^7) : P \in \left(\tfrac{2}{7}, \tfrac{3}{7}\right] \;\land\; \Phi \geq 1 \;\land\; \forall k: \sigma_k < 1\right\}
$$

is **non-empty**.

### Proof (constructive) {#доказательство-t124}

**Step 1.** Consider the family $\Gamma_\lambda = (1-\lambda)\,I/7 + \lambda\,|\psi\rangle\langle\psi|$, where $|\psi\rangle = \frac{1}{\sqrt{7}}\sum_{k=0}^{6}|k\rangle$ is an equal-amplitude vector.

Spectrum: one eigenvalue $\frac{1+6\lambda}{7}$ (multiplicity 1) and six eigenvalues $\frac{1-\lambda}{7}$ (multiplicity 6). From this:

$$
P(\Gamma_\lambda) = \frac{1}{7} + \frac{6\lambda^2}{7}, \quad
R = \frac{1}{7P} = \frac{1}{1 + 6\lambda^2}, \quad
\Phi(\Gamma_\lambda) = 6\lambda^2
$$

**Step 2.** For $\lambda \in (1/\sqrt{6},\; 1/\sqrt{3}]$:

| Indicator | Value | Condition |
|------------|----------|---------|
| $P$ | $(2/7, 3/7]$ | $\checkmark$ |
| $R$ | $[1/3, 1/2]$ | $\geq 1/3\;\checkmark$ |
| $\Phi$ | $[1, 2]$ | $\geq 1\;\checkmark$ |

Boundary values: at $\lambda = 1/\sqrt{6}$ we get $R = 1/2$ (inclusive), at $\lambda = 1/\sqrt{3}$ — $R = 1/3$ (inclusive).

**Step 3 (σ-condition).** By canonical definition ([T-92 [Т]](/docs/applied/coherence-cybernetics/theorems#теорема-101-эквивалентность-условий)):

$$\sigma_k = \mathrm{clamp}(1 - 7\gamma_{kk},\; 0,\; 1)$$

For equal-amplitude $\Gamma_\lambda$ all diagonal elements equal $\gamma_{kk} = 1/7$ for all $k$ (since $|\psi\rangle = \frac{1}{\sqrt{7}}\sum_k|k\rangle$ is an equal-amplitude vector). Therefore:

$$\sigma_k = \mathrm{clamp}(1 - 7 \cdot \tfrac{1}{7},\; 0,\; 1) = \mathrm{clamp}(0,\; 0,\; 1) = 0 < 1 \quad \forall k$$

All $\sigma$-conditions ($\sigma_k < 1$) are satisfied **without any perturbation**.

**Step 4 ($D_{\mathrm{diff}}$).** Eigenvalues of $\Gamma_\lambda$: $\{(1+6\lambda)/7\; (\times 1),\; (1-\lambda)/7\; (\times 6)\}$. For $\lambda \in (1/\sqrt{6}, 1/\sqrt{3}]$: two distinct eigenvalues, $\mathrm{rank}(\Gamma_\lambda) = 7$.

Von Neumann entropy: $S_{vN} = -\frac{1+6\lambda}{7}\ln\frac{1+6\lambda}{7} - \frac{6(1-\lambda)}{7}\ln\frac{1-\lambda}{7}$.

At $\lambda = 1/\sqrt{6} \approx 0.408$: eigenvalues $\approx 0.572$ (×1) and $\approx 0.085$ (×6), $S_{vN} \approx 1.55$, $D_{\mathrm{diff}} = e^{S_{vN}} \approx 4.7 \geq 2$. The minimum over $\lambda$ on the interval is reached at $\lambda \to 1/\sqrt{3}$: both types of eigenvalues approach $\approx 1/7$, $S_{vN} \to \ln 7 \approx 1.95$, $D_{\mathrm{diff}} \to 7 \geq 2$. The condition $D_{\mathrm{diff}} \geq 2$ holds over the entire interval.

**Therefore**, $\Gamma_\lambda \in \mathcal{V}_{\mathrm{full}}$ for any $\lambda \in (1/\sqrt{6}, 1/\sqrt{3}]$, and the set is non-empty. $\blacksquare$

:::info Numerical verification of the conscious window (SYNARC)
Attractor of the embodied agent: $P = 0.4286 \approx 3/7$ — at the upper boundary of the
Goldilocks zone $[2/7, 3/7]$. Stability radius $r_{\mathrm{stab}} = \sqrt{3/7 - 2/7} \approx 0.378$.
After an impulse perturbation $\|h\| < r^2_{\mathrm{stab}}$: recovery in $\tau_{\mathrm{recovery}} \approx 0$ ticks
(instantaneous attraction). Exponential convergence (T-125) confirmed with $R^2 > 0.9$.
:::

### Corollary (Goldilocks zone) {#зона-голдилокс}

$$
P \in \left(\frac{2}{7}, \frac{3}{7}\right] \text{ — Goldilocks zone for consciousness}
$$

- $P < 2/7$: system is not viable ($\sigma_A = 1$)
- $P > 3/7$: $R = 1/(7P) < 1/3$ — insufficient reflection for L2

---

## §3. Local asymptotic stability of attractor (T-125) {#t-125}

### Formulation [Т]

When $P(\rho^*_\Omega) > 2/7$ the attractor $\rho^*_\Omega$ is locally asymptotically stable: there exists a neighborhood $U(\rho^*_\Omega) \subset \mathcal{V}_P$ such that for all $\Gamma(0) \in U$:

$$
\|\Gamma(\tau) - \rho^*_\Omega\|_F \leq \|\Gamma(0) - \rho^*_\Omega\|_F \cdot e^{-c\tau}, \quad c > 0
$$

### Proof {#доказательство-t125}

**Step 1 (Lyapunov function).** Define $V(\Gamma) = \|\Gamma - \rho^*_\Omega\|^2_F$.

**Step 2 (Jacobian).** The Jacobian $J = d\mathcal{L}_\Omega/d\Gamma|_{\rho^*_\Omega}$ is a linear operator on the tangent space $T_{\rho^*_\Omega}\mathcal{D}(\mathbb{C}^7)$ (Hermitian traceless matrices). It is smooth when $P(\rho^*_\Omega) > 2/7$, since the gate $g_V(P)$ and the regeneration function are differentiable inside $\mathcal{V}_P$.

**Step 3 (Spectrum).** $\mathrm{Re}(\lambda_k) < 0$ for all eigenvalues of $J$ on the tangent space. This follows from two sources of contractivity:

- **Linear part $\mathcal{L}_0$**: spectral gap $\lambda_{\mathrm{gap}} > 0$ from primitivity [T-39a [Т]](/docs/core/operators/lindblad-operators#примитивность-ℒω).
- **Regeneration $\mathcal{R}$**: adds contractivity $\kappa(\rho^*_\Omega) \cdot g_V(P(\rho^*_\Omega)) > 0$, since $P > 2/7 \Rightarrow g_V > 0$.

Total contractivity: $c \geq \min(\lambda_{\mathrm{gap}},\; \kappa \cdot g_V) > 0$.

**Step 4 (Lyapunov theorem).** Standard linear stability theorem: $\mathrm{Re}(\lambda_k) < 0$ for all $k$ $\Rightarrow$ $\exists U$ neighborhood of $\rho^*_\Omega$ with exponential convergence at rate $c$.

**Step 5 (Radius).** Neighborhood $U = B(\rho^*_\Omega, r_{\mathrm{stab}}/2)$, where $r_{\mathrm{stab}} = \sqrt{P(\rho^*_\Omega) - 2/7}$ from [T-104 [Т]](/docs/applied/coherence-cybernetics/stability#радиус-устойчивости). $\blacksquare$

### Dependencies

| Theorem | Status | Contribution |
|---------|--------|-------|
| [T-39a](/docs/core/operators/lindblad-operators#примитивность-ℒω) | [Т] | Spectral gap $\lambda_{\mathrm{gap}} > 0$ |
| [T-96](/docs/core/dynamics/evolution#теорема-нетривиальность-аттрактора) | [Т] | Existence of $\rho^*_\Omega \neq I/7$ |
| [T-104](/docs/applied/coherence-cybernetics/stability#радиус-устойчивости) | [Т] | Stability radius $r_{\mathrm{stab}}$ |
| [T-149](/docs/proofs/consciousness/substrate-closure#t-149) | [Т] (embodied) | Premise $P(\rho^*_\Omega) > 2/7$ — unconditional for embodied holons |

---

## §4. Canonicity of R = 1/(7P) (T-126) {#t-126}

### Formulation [Т]

The reflection measure $R$ has a unique canonical form:

$$
R(\Gamma) = \frac{1}{7P(\Gamma)}
$$

always using $\rho^*_{\mathrm{diss}} = I/7$ as reference. There are no "three inconsistent formulas" — the three expressions are one algebraic identity.

### Proof {#доказательство-t126}

The original [master definition](/docs/consciousness/foundations/self-observation#мера-рефлексии-r):

$$
R = 1 - \frac{\|\Gamma - I/7\|^2_F}{\|\Gamma\|^2_F}
$$

Compute the numerator:

$$
\|\Gamma - I/7\|^2_F = \mathrm{Tr}(\Gamma^2 - 2\Gamma/7 + I/49)
= \mathrm{Tr}(\Gamma^2) - \frac{2}{7}\mathrm{Tr}(\Gamma) + \frac{1}{7}
= P - \frac{2}{7} + \frac{1}{7} = P - \frac{1}{7}
$$

Denominator: $\|\Gamma\|^2_F = \mathrm{Tr}(\Gamma^2) = P$.

Therefore:

$$
R = 1 - \frac{P - 1/7}{P} = \frac{1/7}{P} = \frac{1}{7P}
$$
$\blacksquare$

### Explanation: uniqueness of canonical form {#пояснение-единственность-r}

| Expression | Formula | Identical to |
|--------|---------|-------------|
| Master definition | $R = 1 - \|\Gamma - I/7\|^2_F / P$ | $= 1/(7P)$ |
| Formula via purity | $R = 1/(7P)$ | algebraic identity |
| Formula via $k$ | $R = 1 - k$, $k = 1 - 1/(7P)$ | [Т](/docs/consciousness/foundations/self-observation#теорема-k-из-r) |

**Key explanation.** The reference $\rho^*_{\mathrm{diss}} = I/7$ is used **always**: $R$ measures the distance from thermal death. The non-trivial attractor $\rho^*_\Omega$ enters the regeneration $\mathcal{R}$ and the formula for $\varphi$, but **not** the definition of $R$.

Implementation approximations ($R_{\mathrm{impl}}$, $\rho_{RC}$) are separate quantities in a different space, related to the canonical $R$ via a CPTP bridge $\pi$. Transfer of thresholds is proven: [T-130+T-133 [Т]](/docs/proofs/consciousness/operationalization#t-130) (H3 CLOSED). The canonical $R$ is unambiguous.

### Physical interpretation {#физическая-интерпретация-r}

$R = 1/(7P)$ is a **relative** measure, not absolute. It measures the fraction of $\Gamma$ "resembling" the chaotic background $I/7$, relative to the total content of the state.

As $P$ (purity) grows:
- The numerator $(P - 1/7)$ in $\|\Gamma - I/7\|^2_F$ grows linearly — deviation from $I/7$ increases
- The denominator $P = \|\Gamma\|^2_F$ also grows — but more slowly in the relative sense
- The ratio $(P - 1/7)/P \to 1$, and $R = 1/(7P) \to 0$

**Savant analogy.** As $P \to 1$ the neural network is maximally specialized. A huge brain structure — but it is all "dedicated" to one thing: no "mirror," no balance for self-modeling. $R \to 1/7$. Conversely: at $P = 1/7$ (maximally mixed) $R = 1$ trivially — $\Gamma = I/7 = \rho^*_{\mathrm{diss}}$, the self-model is ideal, but only because there is nothing to model.

**Consciousness = balance, not maximization.** The consciousness measure $C = \Phi \cdot R$ ([T-140 [Т]](/docs/proofs/consciousness/operational-closure#t-140)) combines integration and reflection. As $P$ grows: $\Phi$ grows (more coherence), $R$ falls (worse self-modeling). $C = \Phi \cdot R$ has an **optimum** inside the Goldilocks zone — consciousness requires balance, not maximization of a single parameter.

---

## §5. Basin of attraction V_full (T-127) {#t-127}

### Formulation {#формулировка-t127}

**Case A (embodied holons) [Т]:** C20 (κ-dominance) follows unconditionally from [T-149 [Т]](/docs/proofs/consciousness/substrate-closure#t-149): embodiment ⟹ $\kappa_{\mathrm{eff}} > \kappa_{\mathrm{bootstrap}}$ ⟹ $P(\rho^*) > P_{\mathrm{crit}}$. T-127 is unconditional.

**Case B (isolated holons) [С at C20]:** C20 is taken as an explicit assumption. T-127 is conditional on the inequality $\kappa_{\mathrm{eff}} > \alpha/(7(f^* - 2/7))$.

| Case | Status of T-127 | Condition |
|--------|-------------|---------|
| Embodied holon | **[Т]** | T-149 proves C20 |
| Isolated holon | **[С at C20]** | C20 as explicit assumption |

When C20 holds, the basin of attraction of $\rho^*_\Omega$ contains $B(\rho^*_\Omega, r_{\mathrm{stab}}) \cap \mathcal{V}_P$. For any $\Gamma(0)$ with $P > 2/7$ and $\|\Gamma(0) - \rho^*_\Omega\| < r_{\mathrm{stab}}$:

$$
\Gamma(\tau) \xrightarrow[\tau \to \infty]{} \rho^*_\Omega \quad \text{exponentially}
$$

### Proof

From three results:

1. **T-125 [Т]** (§3): Local asymptotic stability — in $B(\rho^*_\Omega, r_{\mathrm{stab}}/2)$ convergence is exponential with $c > 0$.

2. **[T-104 [Т]](/docs/applied/coherence-cybernetics/stability#радиус-устойчивости)**: Stability radius $r_{\mathrm{stab}} = \sqrt{P(\rho^*_\Omega) - 2/7}$. Under C20: $P(\rho^*_\Omega) > 2/7$, therefore $r_{\mathrm{stab}} > 0$.

3. **Openness of $\mathcal{V}_{\mathrm{full}}$**: $\mathcal{V}_{\mathrm{full}}$ is an open set in $\mathcal{D}(\mathbb{C}^7)$ (each of the 7 inequalities $\sigma_k < 1$ defines an open condition). By [T-124 [Т]](#t-124): $\mathcal{V}_{\mathrm{full}} \neq \varnothing$.

For $\Gamma(0) \in B(\rho^*_\Omega, r_{\mathrm{stab}}) \cap \mathcal{V}_P$: by T-125, $\|\Gamma(\tau) - \rho^*_\Omega\|_F$ decreases exponentially. Since $\rho^*_\Omega$ is an interior point of $\mathcal{V}_P$ (because $P(\rho^*_\Omega) > 2/7$), the trajectory remains in $\mathcal{V}_P$ for sufficiently small deviations. $\blacksquare$

### Remark

This theorem applies to states **already above** $P_{\mathrm{crit}}$. Genesis from $I/7$ (transition $P = 1/7 \to P > 2/7$) is solved for **embodied holons**: [T-148 [Т]](/docs/proofs/consciousness/substrate-closure#t-148) — backbone injection raises purity above $P_{\mathrm{crit}}$ in finite time $n_{\mathrm{genesis}}$. An isolated holon at $I/7$ is dead forever (T-39a [Т]).

---

## §6. Attractor in conscious window (C27) {#c27}

### Formulation [Т] (upgraded from [С] via T-149) {#формулировка-c27}

For **embodied** holons: the attractor $\rho^*_\Omega \in \mathcal{V}_{\mathrm{full}}$, namely $P(\rho^*_\Omega) \in (2/7, 3/7]$. C20 (κ-dominance) holds unconditionally for embodied holons by [T-149 [Т]](/docs/proofs/consciousness/substrate-closure#t-149).

### Justification

**Lower bound $P > 2/7$:** Follows from C20 [С] (κ-dominance) and [T-98 [Т]](/docs/core/dynamics/evolution#теорема-баланс-чистоты-аттрактора).

**Upper bound $P \leq 3/7$:**

:::warning Clarification of C27 status
The upper bound $P \leq 3/7$ follows **directly** from the definition $R = 1/(7P)$ and the threshold $R \geq 1/3$: from $R = 1/(7P) \geq 1/3$ we get $P \leq 3/7$. This is an **algebraic identity**, requiring no additional conditions on the attractor. Status: **[Т]** (direct consequence of definition of R and threshold R_th).
:::

### Status [Т] (for embodied holons)

C20 is unconditional for embodied holons (T-149 [Т]). For isolated holons C20 remains [С].

### Explicitly NOT proven

**Genesis from $I/7$:** solved — [T-148 [Т]](/docs/proofs/consciousness/substrate-closure#t-148) proves genesis via environmental coupling for embodied holons. T-125/T-127 apply to states **already above** $P_{\mathrm{crit}}$; T-148 closes the transition $I/7 \to P > 2/7$.

---

## Summary

| Problem | Theorem | Status |
|----------|---------|--------|
| Uniqueness of representation $G$ for digital agents | [T-123 [Т]](#t-123) | CLOSED |
| Semantics of $\gamma_{kk}$ (not arbitrary) | [T-123 [Т]](#t-123) | CLOSED |
| Non-emptiness of $\mathcal{V}_{\mathrm{full}}$ (consistency of thresholds) | [T-124 [Т]](#t-124) | CLOSED |
| Canonicity of three forms of $R$ | [T-126 [Т]](#t-126) | CLOSED |
| Basin of attraction and attractor stability | [T-125 [Т]](#t-125) + [T-127](#t-127) | CLOSED ([Т] for embodied, T-149) |

---

**Related documents:**
- [Evolution of Γ](/docs/core/dynamics/evolution) — T-96, T-98, attractor $\rho^*_\Omega$
- [Viability](/docs/core/dynamics/viability) — $\mathcal{V}_P$, $\mathcal{V}_{\mathrm{full}}$
- [Self-observation](/docs/consciousness/foundations/self-observation) — master definition of $R$
- [Uniqueness theorem](/docs/proofs/categorical/uniqueness-theorem) — $G_2$-rigidity
- [Stability](/docs/applied/coherence-cybernetics/stability) — $r_{\mathrm{stab}}$
- [Status registry](/docs/reference/status-registry) — T-123 — T-127, C27
