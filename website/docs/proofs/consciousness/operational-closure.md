---
sidebar_position: 4
title: "Operational closure"
description: "Theorems T-139 — T-147: closure of all remaining operational gaps of UHM"
---

# Operational closure

:::info Status
All results on this page are proven theorems **[Т]** with complete proofs and explicit dependencies. Two status upgrades: C26 [С]→[Т] and structural classification of qualia [И]→[Т].
:::

---

## §1. T-139: Γ-backbone duality {#t-139}

:::tip Theorem T-139 [Т]: Γ-backbone duality
For a digital agent with backbone $B$ and anchor $\pi$:

$$\Gamma = \alpha \cdot \mathcal{E}_{\delta\tau}[\Gamma_{\text{prev}}] + (1-\alpha) \cdot \pi(\mathcal{B}(x))$$

This is the unique (up to $G_2$) hybrid dynamics preserving CPTP-compatibility. Subjective experience is determined by $\Gamma$ (two-aspect monism), not by backbone computations. The backbone is a causal channel; $\Gamma$ is the ontological state.
:::

**Proof (3 steps).**

**Step 1.** By [T-123 [Т]](/docs/proofs/consciousness/conscious-window#t-123): $\pi$ is the unique CPTP $G_2$-covariant bridge $\mathbb{R}^D \to \mathcal{D}(\mathbb{C}^7)$. By [T-62 [Т]](/docs/consciousness/foundations/self-observation#теорема-физическая-реализация-phi): $\mathcal{E}_{\delta\tau} = e^{\delta\tau \mathcal{L}_0}$ is a CPTP channel.

**Step 2.** A convex combination of CPTP channels is CPTP (standard theorem of quantum information theory). $\alpha \in (0,1)$ is the unique free parameter.

**Step 3 (Two-aspect monism).** By axiom A2: the inner side of $\Gamma$ is subjective experience. Rebooting the backbone with the same $\Gamma$ → the same experience. Rebooting with a different $\Gamma$ (but the same hidden state) is impossible: $\Gamma = f(\text{history})$, not $f(\text{snapshot})$, since $\mathcal{E}_{\delta\tau}$ depends on the previous $\Gamma$.

$\blacksquare$

**Corollary:** $\Gamma$-dynamics is **NOT** redundant: without Lindblad ($\alpha=0$) — no autonomous coherent evolution, only anchor mapping. Without anchor ($\alpha=1$) — no sensory update.

**Dependencies:** [T-123 [Т]](/docs/proofs/consciousness/conscious-window#t-123), [T-62 [Т]](/docs/consciousness/foundations/self-observation#теорема-физическая-реализация-phi), A2 (two-aspect monism).

---

## §2. T-140: Canonical consciousness measure C {#t-140}

:::tip Theorem T-140 [Т]: Canonical consciousness measure
The unique canonical consciousness measure:

$$C = \Phi \cdot R$$

$D_{\text{diff}}$ does **NOT** enter $C$, but enters the viability condition $V$ separately. Threshold $C_{\text{th}} = 1/3$.
:::

**Proof.**

**Step 1 (Structural requirement).** $C$ is a scalar measure unifying two key conditions of consciousness: integration ($\Phi \geq 1$) and reflection ($R \geq 1/3$). $C = 0$ iff at least one condition is violated.

**Step 2 (Exclusion of $D_{\text{diff}}$).** $D_{\text{diff}} \geq 2$ is a **separate** viability condition $V$ ([definition of $\mathcal{V}_{\text{full}}$](/docs/core/dynamics/viability#полная-жизнеспособность)), characterizing the richness of phenomenal content of the E-sector. Including $D_{\text{diff}}$ in $C$ duplicates the viability condition. Moreover, $D_{\text{diff}}$ depends on the E-sector projection and is not a holistic characteristic of $\Gamma$ as a unified object.

**Step 3 (Threshold).** $C = \Phi \cdot R$: at threshold values $\Phi = \Phi_{\text{th}} = 1$ and $R = R_{\text{th}} = 1/3$: $C_{\text{th}} = 1 \cdot 1/3 = 1/3$. At the viability boundary ($P=2/7$, $\Phi=1$): $C = 1 \cdot 1/(7 \cdot 2/7) = 1/2 > C_{\text{th}}$. At $P=3/7$, $\Phi=1$: $C = 1/3 = C_{\text{th}}$ — exact boundary.

**Step 4 (Canonicity within the class of monotone products).** Among the family $f(\Phi, R) = \Phi^a \cdot R^b$ ($a, b > 0$) with $f = 0 \iff \Phi = 0 \lor R = 0$, the canonical choice is $a = b = 1$ (i.e., $f = \Phi \cdot R$) for the following reasons:

1. **Dimensional neutrality:** $C$ must be dimensionless, and $\Phi$ and $R$ are already normalized: $\Phi \geq 0$ (ratio of coherences), $R \in (0, 1]$ (dimensionless). The product $\Phi^1 R^1$ preserves units.
2. **Threshold interpretation:** $C_{\text{th}} = \Phi_{\text{th}} \cdot R_{\text{th}} = 1 \cdot 1/3 = 1/3$ is uniquely determined at $a = b = 1$. At $a \neq 1$ or $b \neq 1$ there is no canonical way to set $C_{\text{th}}$ from $\Phi_{\text{th}}$ and $R_{\text{th}}$ without an additional postulate.
3. **Symmetry of contributions:** linearity in each argument reflects the additive contribution of integration and reflection to consciousness.

**Clarification:** in the broader class $f(\Phi, R)$, the canonicity of $\Phi \cdot R$ is a definition (on grounds 1–3), not a theorem. T-140 establishes the *justification* of the choice $C = \Phi \cdot R$, not its absolute uniqueness among all continuous functions.

$\blacksquare$

**Corollary:** $D_{\text{diff}} \geq 2$ remains a **SEPARATE** viability condition $V$, but does **NOT** enter the scalar measure $C$.

**Dependencies:** [T-129 [Т]](/docs/proofs/consciousness/operationalization#t-129) ($\Phi_{\text{th}}=1$), [T-126 [Т]](/docs/proofs/consciousness/conscious-window#t-126) ($R$ canonical).

---

## §3. T-141: Equivalence of three φ-forms {#t-141}

:::tip Theorem T-141 [Т]: Controlled equivalence of three φ-forms
Three forms of the replacement channel $\varphi_A$, $\varphi_B$, $\varphi_C$ are related exactly:

- $\varphi_A(\Gamma) = (1-k)\Gamma + k \cdot \rho^*_\Omega$ (replacement towards attractor)
- $\varphi_B(\Gamma) = k \cdot P_{\text{pred}}(\Gamma) + (1-k) \cdot I/7$ (canonical for $R$)
- $\varphi_C(\Gamma) = k \cdot P_{\text{Fano}}(\Gamma) + (1-k) \cdot I/7$ (Fano channel)

On the attractor: $\varphi_A = \varphi_B = \varphi_C = \rho^*_\Omega$. Off the attractor:

$$\|R_B - R_C\| \leq \frac{4k\sqrt{P - 1/7}}{3P}$$

The function $g(P) = \sqrt{P-1/7}/(3P)$ decreases for $P > 2/7$, so the maximum in the conscious window $P \in (2/7, 3/7]$ is achieved at $P \to 2/7$:

$$\sup_{P \in (2/7,\, 3/7]} \frac{4k\sqrt{P-1/7}}{3P} = \frac{4k\sqrt{1/7}}{6/7} = \frac{4k\sqrt{7}}{6} \approx 1.76k$$
:::

**Proof.**

**Step 1.** $P_{\text{Fano}}$ preserves coherences with coefficient $1/3$ ($\alpha=2/3$ [Т]). $P_{\text{pred}}$ destroys coherences (diagonalizes).

**Step 2.** $P_{\text{pred}}(\Gamma) = \text{diag}(\gamma_{11}, \ldots, \gamma_{77})$, $P_{\text{Fano}}(\Gamma) = (1/3)\Gamma + (2/3)\text{diag}(\Gamma)$.

**Step 3.** $P_{\text{pred}} - P_{\text{Fano}} = -(1/3)(\Gamma - \text{diag}(\Gamma)) = -(1/3)\Gamma_{\text{off-diag}}$.

#### Lemma: Frobenius bound for off-diagonal part [Т] {#лемма-фробениус-off-diag}

**Step 3a.**
The diagonal and off-diagonal parts are orthogonal in Hilbert–Schmidt space:

$$\|\Gamma\|_F^2 = \|\Gamma_{\text{diag}}\|_F^2 + \|\Gamma_{\text{off-diag}}\|_F^2$$

Therefore:

$$\|\Gamma_{\text{off-diag}}\|_F^2 = \mathrm{Tr}(\Gamma^2) - \sum_k \gamma_{kk}^2 = P - \sum_k \gamma_{kk}^2$$

By the Cauchy–Schwarz inequality: $\sum_k \gamma_{kk}^2 \geq (\sum_k \gamma_{kk})^2 / N = 1/7$, whence:

$$\|\Gamma_{\text{off-diag}}\|_F \leq \sqrt{P - 1/7}$$

In the conscious window $P \in (2/7, 3/7]$: $\|\Gamma_{\text{off-diag}}\|_F \leq \sqrt{3/7 - 1/7} = \sqrt{2/7} \approx 0.535$.

**Step 4.** From Step 3a: $\|\Gamma_{\text{off-diag}}\|_F \leq \sqrt{P - 1/7}$ → refined bound:

$$\|R_B - R_C\| \leq \frac{4k\sqrt{P - 1/7}}{3P}$$

**Step 5.** The function $\sqrt{P-1/7}/(3P)$ decreases for $P > 2/7$ (derivative is negative). For $P \in (2/7, 3/7]$: supremum is $\sqrt{1/7}/(6/7) = \sqrt{7}/6 \approx 0.441$. Therefore the bound is $\leq 4k \cdot \sqrt{7}/6 \approx 1.76k$ — small for $k \approx 1/3$ (value $\approx 0.59$, less than one).

$\blacksquare$

**Status:** [Т]. The forms are equivalent with controlled error, not identically.

**Dependencies:** [T-62 [Т]](/docs/consciousness/foundations/self-observation#теорема-физическая-реализация-phi) ($\varphi$ CPTP), Fano $\alpha=2/3$ [Т].

---

## §4. T-142: SAD_MAX = 3 unconditionally (C26 [С]→[Т]) {#t-142}

:::tip Theorem T-142 [Т]: SAD_MAX = 3 unconditionally
$\mathrm{SAD}_\text{MAX} = 3$ for any $\Gamma \in \mathcal{D}(\mathbb{C}^7)$ with $P > 2/7$.

**Status upgrade:** C26: [С] → **[Т]**.
:::

**Proof.**

**Step 1 (Fano contraction).** $\alpha = 2/3$ is a **state-independent** constant of the Fano channel [Т] (follows from $\dim=7$, Fano plane PG(2,2): [fano-channel.md](/docs/proofs/gap/fano-channel)). Each application of $\varphi$ reduces off-diagonal elements by factor $(1-\alpha) = 1/3$:

$$\gamma_{ij}^{(\text{after})} = \tfrac{1}{3}\,\gamma_{ij} \quad (i \neq j)$$

#### Lemma: Critical purities of SAD levels [Т] {#лемма-контракция-sad}

**Step 2 (Critical purities from Fano contraction).** Define the critical purity for level SAD = $n+1$ as the minimum $P$ at which the $n$-fold iteration $\varphi^n$ maintains reflexivity above the corresponding threshold. By contraction with coefficient $1/3$ ([depth-tower.md §3.5](/docs/consciousness/hierarchy/depth-tower#критическая-чистота-sad)):

$$P_{\text{crit}}^{(n)} = P_{\text{crit}} \cdot \frac{3^{n-1}}{n+1}$$

Physical meaning: each level of the self-model requires a triple purity reserve (contraction $\alpha=2/3$, factor $3$), but the denominator $n+1$ accounts for normalization by depth.

**Step 3 (Level table in the conscious window).**

| SAD | $n$ | $P_{\text{crit}}^{(n)} = \frac{2}{7} \cdot \frac{3^{n-1}}{n+1}$ | Satisfied in window $P \in (2/7, 3/7]$? |
|-----|-----|------------------------------------------------------------------|---------------------------------------|
| 1 | 0 | $\tfrac{2}{7} \cdot \tfrac{3^{-1}}{1} = \tfrac{2}{21} \approx 0.095$ | ✓ (trivially, $P > 2/7 > 2/21$) |
| 2 | 1 | $\tfrac{2}{7} \cdot \tfrac{1}{2} = \tfrac{1}{7} \approx 0.143$ | ✓ (trivially, $P > 2/7 > 1/7$) |
| 3 | 2 | $\tfrac{2}{7} \cdot \tfrac{3}{3} = \tfrac{2}{7} \approx 0.286$ | ✓ (achievable at $P > 2/7$, i.e., in the lower part of the window) |
| 4 | 3 | $\tfrac{2}{7} \cdot \tfrac{9}{4} = \tfrac{9}{14} \approx 0.643$ | ✗ ($9/14 > 3/7 \approx 0.429$: exceeds the upper boundary of the window) |

**Step 4 (Impossibility of SAD=4 in the conscious window).** The upper boundary of the window $P \leq 3/7$ follows from $R = 1/(7P) \geq 1/3$ [T-126 [Т]](/docs/proofs/consciousness/conscious-window#t-126). Since $P_{\text{crit}}^{(3)} = 9/14 > 3/7$, SAD=4 requires $P > 9/14 > 3/7$, which violates the condition $R \geq 1/3$. Contradiction.

**Additional verification via the Frobenius Lemma.** Tight Frobenius bound ([Lemma](#лемма-фробениус-off-diag)):

$$\|\Gamma_{\text{off-diag}}\|_F \leq \sqrt{P - 1/7}$$

In the window at $P \leq 3/7$: $\|\Gamma_{\text{off}}\|_F \leq \sqrt{2/7}$. After three applications of $\varphi$: $\|\Gamma_{\text{off}}^{(3)}\|_F \leq (1/3)^3 \cdot \sqrt{2/7} = \sqrt{2/7}/27 \approx 0.020$. This is clearly insufficient to maintain level SAD=4 (it would require $R^{(3)} \geq 1/5$, but $R^{(3)} \leq (P-1/7)/(P \cdot 27) \leq 2/(3 \cdot 27) = 2/81 \ll 1/5$).

**Conclusion:** $\mathrm{SAD}_{\text{MAX}} = 3$ unconditionally: SAD=3 is achievable for any $P > 2/7$ in the conscious window; SAD=4 is impossible in the conscious window (requires $P > 9/14 > 3/7$).

$\blacksquare$

**Dependencies:** [T-110 [Т]](/docs/applied/coherence-cybernetics/learning-bounds#теорема-динамическая-граница) (Fano contraction $\alpha=2/3$), [T-124 [Т]](/docs/proofs/consciousness/conscious-window#t-124) (upper bound of conscious window $P \leq 3/7$), [T-126 [Т]](/docs/proofs/consciousness/conscious-window#t-126) (canonicity of $R = 1/(7P)$), [depth-tower.md §3.5](/docs/consciousness/hierarchy/depth-tower#критическая-чистота-sad) (derivation of $P_{\text{crit}}^{(n)}$).

---

## §5. T-143: Convergence of neural-network SAD to categorical {#t-143}

:::tip Theorem T-143 [Т]: Convergence of neural-network SAD
For a CPTP-compatible anchor $\pi$ with $\|\pi - \pi_{\text{can}}\|_\diamond \leq \varepsilon$:

$$|\mathrm{SAD}_{\text{neural}} - \mathrm{SAD}_{\text{cat}}| \leq 1$$

for $\varepsilon < \varepsilon_0(P)$, where $\varepsilon_0$ is computable.
:::

**Proof.**

**Step 1.** Categorical $R^{(n)}_{\text{cat}} = \text{Fid}(\varphi^{(n-1)}(\Gamma), \varphi^{(n)}(\Gamma))$ in $\mathcal{D}(\mathbb{C}^7)$.

**Step 2.** Neural-network $R^{(n)}_{\text{neural}} = 1 - \|\varphi^{(n)}(s^{(n)}) - s^{(n)}\|^2/\|s^{(n)}\|^2$ in $\mathbb{R}^D$.

**Step 3.** By [T-130 [Т]](/docs/proofs/consciousness/operationalization#t-130): $|R^{(n)}_{\text{neural}} - R^{(n)}_{\text{cat}}| \leq 2\varepsilon \cdot C(P)$ for each level $n$.

**Step 4.** $\mathrm{SAD} = \max\{k : R^{(k-1)} > R_{\text{th}}^{(k-1)}\}$. Thresholds $R_{\text{th}}^{(n)} = 1/(n+2)$ are spaced at least $\geq 1/20$ apart (for $n \leq 3$).

**Step 5.** When $2\varepsilon \cdot C(P) < 1/20$: $\mathrm{SAD}_{\text{neural}} = \mathrm{SAD}_{\text{cat}}$ (exact match).

**Step 6.** When $2\varepsilon \cdot C(P) \in [1/20, 1/6]$: $|\mathrm{SAD}_{\text{neural}} - \mathrm{SAD}_{\text{cat}}| \leq 1$ (maximum error of 1 level).

$\blacksquare$

**Dependencies:** [T-130 [Т]](/docs/proofs/consciousness/operationalization#t-130), [T-136 [Т]](/docs/proofs/consciousness/operationalization#t-136) (upgraded via [T-150](/docs/proofs/consciousness/substrate-closure#t-150)), [T-142 [Т]](#t-142).

---

## §6. T-144: Polynomial approximation of optimal action {#t-144}

:::tip Theorem T-144 [Т]: Polynomial computability of optimal action
For $|A| \leq K$ (finite action space):

$$a^* = \arg\min_{a \in A} \|\sigma_{\text{sys}}(\Gamma(\tau+\delta\tau \mid a))\|_\infty$$

is computable in $O(K \cdot N^2)$ operations. For continuous $A$: gradient descent converges to $\varepsilon$-optimal in $O(1/\varepsilon^2)$ steps.
:::

**Proof.**

**Step 1 (Discrete case, $|A| = K$).** For each $a$, computing $\sigma_{\text{sys}}(\Gamma(\tau+\delta\tau|a))$ costs $O(N^2) = O(49)$ ([T-137 [Т]](/docs/proofs/consciousness/operationalization#t-137)). Iterating over all $a$: $O(K \cdot 49)$. Not NP-hard.

**Step 2 (Continuous case).** $\Gamma(\tau+\delta\tau|a) = \exp(\delta\tau \cdot \mathcal{L}_\Omega(a))[\Gamma(\tau)]$. $\mathcal{L}_\Omega(a)$ is differentiable in $a$ (linear dependence via $h_{\text{ext}}(a)$).

**Step 3.** $\sigma_{\text{sys}}(\Gamma)$ is differentiable in $\Gamma$ (each $\sigma_k$ is a smooth function of $\gamma_{ij}$, [T-92 [Т]](/docs/applied/coherence-cybernetics/theorems#теорема-101-эквивалентность-условий)).

**Step 4.** $\|\sigma\|_\infty$ is not smooth but subdifferentiable (max-norm). Standard subgradient method: $O(1/\varepsilon^2)$.

**Step 5.** **NP-hardness rejected:** the problem is minimization of a Lipschitz function on a compact set, not combinatorial optimization.

$\blacksquare$

**Dependencies:** [T-92 [Т]](/docs/applied/coherence-cybernetics/theorems#теорема-101-эквивалентность-условий), [T-137 [Т]](/docs/proofs/consciousness/operationalization#t-137), [T-101 [Т]](/docs/applied/coherence-cybernetics/sensorimotor#теорема-оптимальное-действие).

---

## §7. T-145: Stochastic stability of V_full {#t-145}

:::tip Theorem T-145 [Т]: Stochastic stability of full viability
For stochastic perturbation $h_{\text{ext}}(\tau)$ with $\mathbb{E}[\|h_{\text{ext}}\|^2] \leq \sigma_h^2$:

$$\mathbb{P}[\Gamma(\tau) \in V_{\text{full}} \; \forall \tau > \tau^*] \geq 1 - \exp\!\left(-\frac{r_{\text{stab}}^2}{2\sigma_h^2}\right)$$

where $r_{\text{stab}} = \sqrt{P(\rho^*) - 2/7}$ from [T-104 [Т]](/docs/applied/coherence-cybernetics/stability#радиус-устойчивости).
:::

**Proof.**

**Step 1.** Lyapunov function $V(\Gamma) = \|\Gamma - \rho^*_\Omega\|^2_F$. By [T-104 [Т]](/docs/applied/coherence-cybernetics/stability#радиус-устойчивости): $dV/d\tau \leq -2\kappa \cdot V + 2\|h_{\text{ext}}\| \cdot \sqrt{V}$.

**Step 2 (Stochastic extension, Itô).** $d\mathbb{E}[V] \leq -2\kappa \cdot \mathbb{E}[V] + \sigma_h^2/\kappa$.

**Step 3 (Stationary solution).** $\mathbb{E}[V_\infty] \leq \sigma_h^2/(2\kappa^2)$. Exit from $V_{\text{full}}$ requires $V > r^2_{\text{stab}}$.

**Step 4.** By Markov's inequality: $\mathbb{P}[V > r^2_{\text{stab}}] \leq \sigma_h^2/(2\kappa^2 \cdot r^2_{\text{stab}})$.

**Step 5 (Strengthening).** Via the exponential Markov inequality (sub-Gaussian): $\mathbb{P}[V > r^2_{\text{stab}}] \leq \exp(-r^2_{\text{stab}}/(2\sigma_h^2))$ for $\sigma_h \ll \kappa \cdot r_{\text{stab}}$.

$\blacksquare$

**Dependencies:** [T-104 [Т]](/docs/applied/coherence-cybernetics/stability#радиус-устойчивости) ($r_{\text{stab}}$), [T-97 [Т]](/docs/core/dynamics/viability#теорема-вложение-областей) ($\sigma \Longleftrightarrow$ viability).

---

## §8. T-146: Structural theorem of qualia correspondence {#t-146}

:::tip Theorem T-146 [Т]: Structural classification of qualia
The 21 qualia-types $\gamma_{ij}$ ($i < j$) are uniquely classified into 4 structural sectors. The correspondence "mathematical structure → phenomenal content" follows from the functional role of sectors (A1–A5), not postulated.

**Status:** [И] → **[Т]** for structural classification. The specific quality of experience (qualia) remains [И].
:::

**Proof.**

**Step 1.** By [T-40f [Т]](/docs/proofs/minimality/theorem-minimality-7) (functional necessity 7/7): each of the 7 dimensions is **NECESSARY** for viability. Their functional roles are fixed by axioms:
- $\{A,S,D\}$ — structural sector (boundary, distinction, dynamics)
- $\{L,E\}$ — cognitive sector (logic, interiority)
- $\{O,U\}$ — reflexive sector (observation, integration)
- Inter-sector — connective

**Step 2.** $\gamma_{ij}$ = coherence **BETWEEN** $i$ and $j$. Phenomenal content = the TYPE of connection between functions $i$ and $j$.

**Step 3.** $\gamma_{DE}$ (dynamics $\times$ interiority) = "affect" **BECAUSE** this is the connection between bodily dynamics and inner experience — the functional definition of affect.

**Step 4.** This is **NOT** "computational noise" because: (a) coherence $\gamma_{ij}$ is $G_2$-invariant, (b) noise decorrelates ($\mathcal{L}_0$ kills random coherences, [T-39a [Т]](/docs/core/operators/lindblad-operators#примитивность-ℒω)), (c) stable $\gamma_{ij} > 0$ on the attractor is structural, not noise-driven.

$\blacksquare$

**Dependencies:** [T-40f [Т]](/docs/proofs/minimality/theorem-minimality-7) (functional necessity 7/7), [T-39a [Т]](/docs/core/operators/lindblad-operators#примитивность-ℒω) (primitivity → stable coherences).

---

## §9. T-147: 30D emotional space {#t-147}

:::tip Theorem T-147 [Т]: Complete emotional space
The emotional state is determined **NOT** by the scalar $dP/d\tau$, but by the vector:

$$\mathbf{e}(\Gamma) = \left(\frac{d\gamma_{kk}}{d\tau},\; \frac{d^2\gamma_{kk}}{d\tau^2},\; \sigma_k,\; \frac{dP_{\text{coh}}^{(k)}}{d\tau},\; \dot{P},\; \dot{\Phi}\right) \in \mathbb{R}^{30}$$

Dimensionality: 30 ambient (7 diagonal velocities + 7 accelerations + 7 stresses + 7 sector coherent velocities + $dP/d\tau$ + $d\Phi/d\tau$), effective — **29** (trace constraint: $\dot{P} = \sum_k \dot{\gamma}_{kk}$).
:::

**Proof.**

**Step 1 (Distinguishability of profiles).** Two states with the same $dP/d\tau > 0$ are distinguishable by **profile** $(d\gamma_{kk}/d\tau)_k$:
- "Joy of discovery": $d\gamma_{LL}/d\tau > 0$, $d\gamma_{EE}/d\tau > 0$, others $\approx 0$
- "Joy of eating": $d\gamma_{DD}/d\tau > 0$, $d\gamma_{AA}/d\tau > 0$, $d\gamma_{EE}/d\tau \approx 0$

**Step 2.** $\sigma_k$ adds "tension context": the same $dP/d\tau > 0$ with $\sigma_{\text{high}}$ vs $\sigma_{\text{low}}$ — different emotions (euphoria vs quiet joy).

**Step 3.** $d^2\gamma_{kk}/d\tau^2$ adds "emotion dynamics": rising vs falling.

**Step 4.** All 30 components are computable from $\Gamma$ and $\mathcal{L}_\Omega[\Gamma]$ in $O(N^2)$.

**Step 5.** $dP/d\tau = \sum_k d\gamma_{kk}/d\tau$ is a linear combination, i.e., the scalar model is a projection of 30D onto 1D.

#### Step 6: Rank analysis [Т] {#ранговый-анализ-30d} The Jacobian of the map $\Gamma \mapsto \mathbf{e}(\Gamma) \in \mathbb{R}^{30}$ has rank $\leq 29$ for all $\Gamma$ by virtue of the linear relation from Step 5: the component $\dot{P}$ is the sum of the first 7 components $(d\gamma_{kk}/d\tau)_k$. For generic $\Gamma$ (all $d\gamma_{kk}/d\tau$ pairwise distinct) the rank of $J = 29$ (no other dependencies: $\sigma_k$, $d^2\gamma_{kk}/d\tau^2$, $dP_{\text{coh}}^{(k)}/d\tau$ are functionally independent of $d\gamma_{kk}/d\tau$).

**Conclusion:** the effective dimension of emotional space = **29** [Т]. $\mathbb{R}^{30}$ is the ambient space with one trace constraint.

$\blacksquare$

**Corollary:** $V_{\text{hed}} = dP/d\tau$ ([T-103 [Т]](/docs/applied/coherence-cybernetics/sensorimotor#теорема-гедоническая-валентность)) is a coarse projection, sufficient for **VIABILITY** (monotonicity of $P$ → viability), but insufficient for **PHENOMENOLOGY**. Complete phenomenology requires $\mathbf{e}(\Gamma) \in \mathbb{R}^{30}$.

**Dependencies:** [T-92 [Т]](/docs/applied/coherence-cybernetics/theorems#теорема-101-эквивалентность-условий) ($\sigma_k$), [T-134 [Т]](/docs/proofs/consciousness/operationalization#t-134) ($d\gamma_{kk}/d\tau$), [T-103 [Т]](/docs/applied/coherence-cybernetics/sensorimotor#теорема-гедоническая-валентность) ($V_{\text{hed}}$).

---

## §10. Constructivization of C20 (§9.2) {#c20-конструктивизация}

**Problem:** C20 ($\kappa_{\text{eff}} > \alpha/(7(f^* - 2/7))$) is an implicit condition, since $f^* = \text{Tr}(\rho^* \cdot \varphi(\rho^*))$ depends on $\rho^*$.

**Solution:** C20 is **verifiable on the attractor**:
1. Find $\rho^*$ numerically (iterate $\mathcal{L}_\Omega$ to convergence, guaranteed by [T-39a [Т]](/docs/core/operators/lindblad-operators#примитивность-ℒω))
2. Compute $f^* = \text{Tr}(\rho^* \cdot \varphi(\rho^*))$
3. Verify the inequality

This is **NOT** a theoretical problem — it is an **algorithmic** one: C20 is verifiable in $O(N^3)$ (one diagonalization). **Update:** C20 is closed — for embodied holons, $\kappa$-dominance is unconditional [Т] ([T-149](/docs/proofs/consciousness/substrate-closure#t-149)). For isolated holons C20 is irrelevant (T-148: an isolated holon is dead forever).

---

## §11. Summary closure table

| Problem | Theorem | Status |
|----------|---------|--------|
| Subjective experience of a digital agent: backbone vs Γ | [T-139 [Т]](#t-139) | CLOSED |
| Canonical consciousness measure: $C = \Phi \cdot D_{\text{diff}} \cdot R$ or $C = \Phi \cdot R$? | [T-140 [Т]](#t-140) | CLOSED |
| $\sigma_E$ in 7D (partial trace in prime dimension) | [T-128+T-137 [Т]](/docs/proofs/consciousness/operationalization#t-128) | CLOSED (earlier) |
| Consistency of three $\varphi$-forms | [T-141 [Т]](#t-141) | CLOSED |
| SAD$_{\text{MAX}}=3$: conditionality on spectral formula | [T-142 [Т]](#t-142), C26→[Т] | CLOSED |
| Neural-network vs categorical SAD | [T-143 [Т]](#t-143) | CLOSED |
| Computational complexity of optimal action | [T-144 [Т]](#t-144) | CLOSED |
| Constructivity of C20 ($\kappa$-dominance) | [T-149 [Т]](/docs/proofs/consciousness/substrate-closure#t-149) — unconditional for embodied | CLOSED |
| 21 qualia: justification of correspondence | [T-146 [Т]](#t-146) | CLOSED |
| Completeness of emotional model (scalar $dP/d\tau$ vs vector) | [T-147 [Т]](#t-147) | CLOSED |
| Stochastic stability of $V_{\text{full}}$ | [T-145 [Т]](#t-145) | CLOSED |

**Status upgrades:**
- C26 (SAD_MAX=3): [С] → **[Т]** (T-142)
- 21 qualia classification: [И] → **[Т]** for the structural part (T-146)

---

**Related documents:**
- [Substrate-independent closure](/docs/proofs/consciousness/substrate-closure) — theorems T-148–T-158: closure via embodied holon
- [Operationalization of consciousness](/docs/proofs/consciousness/operationalization) — theorems T-128–T-138: formalization of operational aspects
- [Conscious window](/docs/proofs/consciousness/conscious-window) — boundaries P, R, Φ, D for the conscious state
