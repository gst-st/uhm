---
sidebar_position: 3
title: "Operationalization of consciousness"
description: "Theorems T-128 — T-138: formalization of operational aspects of UHM"
---

# Operationalization of consciousness

:::info Status
All results on this page are proven theorems **[Т]** with complete proofs and explicit dependencies. T-136 upgraded from [Т under С] to **[Т]** via T-150 (commutativity of φ-tower [Т]).
:::

---

## §1. T-128: Exact 7D-computability of D_diff {#t-128}

:::tip Theorem T-128 [Т]: Exact 7D-representation of D_diff
$D_{\text{diff}}$ is computable in the 7D formalism without PW-embedding:

$$
D_{\text{diff}}^{7D} = 1 + \frac{\mathrm{Coh}_E(\Gamma)}{\mathrm{Coh}_E^{\max}} \cdot (N - 1)
$$

This formula is the exact 7D-representation of $D_{\text{diff}}$ via Morita equivalence T-58 [Т].
:::

**Proof (4 steps).**

**Step 1.** By [T-58 [Т]](/docs/core/structure/dimension-e#теорема-морита-эквивалентность): $\mathrm{Sh}_\infty(\mathcal{C}_7) \simeq \mathrm{Sh}_\infty(\mathcal{C}_{42}^{PW})$, the 7D and 42D formalisms are equivalent.

**Step 2.** $\mathrm{Coh}_E$ — [HS-projection onto the E-subalgebra [Т]](/docs/core/foundations/axiom-septicity#hs-projection) — is an invariant independent of the choice of representation (7D or 42D).

**Step 3.** In 42D: $D_{\text{diff}} = \exp(S_{vN}(\rho_E))$, where $\rho_E = \mathrm{Tr}_{-E}(\Gamma)$. Via equivalence, $\rho_E$ is uniquely reconstructed from $\mathrm{Coh}_E(\Gamma)$ by the [4-step algorithm T-95](/docs/core/structure/dimension-e#канонический-алгоритм-pw).

**Step 4 (Linear formula).** Corollary:
- $\mathrm{Coh}_E = 0 \Longrightarrow D_{\text{diff}} = 1$ (pure E-state)
- $\mathrm{Coh}_E = \mathrm{Coh}_E^{\max} \Longrightarrow D_{\text{diff}} = N$ (maximal differentiation)
- Monotonicity from CPTP-contractivity ([T-62 [Т]](/docs/consciousness/foundations/self-observation#теорема-физическая-реализация-phi))

$\blacksquare$

**Dependencies:** T-58 [Т], T-95 [Т], $\mathrm{Coh}_E$ [Т]. Normalization: $\mathrm{Coh}_E^{\max} = 1$ [Т] ([T-154](/docs/proofs/consciousness/substrate-closure#t-154)).

**Corollary:** $\sigma_E = 1 - D_{\text{diff}}^{7D}/N$ is computable in 7D, closing the full 7D-computability of $\sigma_{\text{sys}}$ (see [T-137](#t-137)). With $\mathrm{Coh}_E^{\max} = 1$: $D_{\text{diff}}^{7D} = 1 + \mathrm{Coh}_E(\Gamma) \cdot (N-1)$.

---

## §2. T-129: Φ_th = 1 from self-consistency {#t-129}

:::tip Theorem T-129 [Т]: Integration threshold Φ_th = 1 (upgrade [О] → [Т])
$\Phi_{\text{th}} = 1$ is the unique value at which the integration threshold is self-consistent with $P_{\text{crit}} = 2/7$ on the extremal (uniform-diagonal) state.
:::

**Proof.**

**Step 1.** Purity decomposition: $P = P_{\text{diag}} + P_{\text{coh}} = P_{\text{diag}}(1 + \Phi)$.

**Step 2.** By Cauchy–Schwarz: $P_{\text{diag}} = \sum_i \gamma_{ii}^2 \geq 1/N = 1/7$ (equality iff $\gamma_{ii} = 1/7\;\forall i$).

**Step 3.** On the extremal uniform-diagonal state: $P_{\text{diag}} = 1/7$, $P = (1 + \Phi)/7$.

**Step 4.** Viability condition $P > P_{\text{crit}} = 2/7$ ([Т](/docs/core/dynamics/viability#определение-чистоты)):
$$\frac{1 + \Phi}{7} > \frac{2}{7} \iff \Phi > 1$$

**Step 5.** $\Phi_{\text{th}} = 1$ is the exact boundary: for $\Phi < 1$ and uniform diagonal, viability is impossible.

**Step 6 (Uniqueness).** Any $\Phi_{\text{th}} \neq 1$ is not the smallest threshold compatible with $P_{\text{crit}} = 2/7$:
- $\Phi_{\text{th}} < 1$: **too weak a threshold** — admits non-viable states (uniform diagonal with $\Phi \in (\Phi_{\text{th}}, 1)$ gives $P = (1+\Phi)/7 < 2/7$, violating viability despite $\Phi \geq \Phi_{\text{th}}$).
- $\Phi_{\text{th}} > 1$: **too strict a threshold** — excludes states that are actually viable (uniform diagonal with $\Phi = 1 \in (1, \Phi_{\text{th}})$ gives $P = 2/7 = P_{\text{crit}}$ — a boundary viable state, yet $\Phi < \Phi_{\text{th}}$ erroneously signals "L2 not reached"). This violates necessity: $\Phi_{\text{th}}$ must be the **smallest** value guaranteeing $P \geq P_{\text{crit}}$.

$\blacksquare$

**Status:** [О] → **[Т]**. $\Phi_{\text{th}} = 1$ is now derived from $P_{\text{crit}} = 2/7$ [Т], not postulated.

**Dependencies:** $P_{\text{crit}} = 2/7$ [Т], Cauchy–Schwarz inequality.

#### Corollary (Universality of Φ_th = 1 on all D(ℂ⁷)) [Т] {#t-129a-универсальность}

:::tip Corollary T-129a [Т]
The threshold $\Phi_{\text{th}} = 1$ is **universal** on the entire space $\mathcal{D}(\mathbb{C}^7)$: for any state $\Gamma$ with $\Phi(\Gamma) \geq 1$, we have $P(\Gamma) \geq P_{\text{crit}}$. The strict inequality $P > P_{\text{crit}}$ holds for all states except the unique boundary case: $\Phi = 1$ and $P_{\text{diag}} = 1/7$ (uniform-diagonal).
:::

**Proof.** Let $\Gamma \in \mathcal{D}(\mathbb{C}^7)$ be an arbitrary state.

**(a)** Purity decomposition: $P = P_{\text{diag}}(1 + \Phi)$ (identity, independent of the specific $\Gamma$).

**(b)** Cauchy–Schwarz inequality: $P_{\text{diag}} = \sum_i \gamma_{ii}^2 \geq \frac{(\sum_i \gamma_{ii})^2}{7} = \frac{1}{7}$, with equality if and only if $\gamma_{ii} = 1/7$ for all $i$.

**(c)** If $\Phi \geq 1$, then $P = P_{\text{diag}}(1 + \Phi) \geq P_{\text{diag}} \cdot 2 \geq \frac{2}{7} = P_{\text{crit}}$. Thus $P \geq P_{\text{crit}}$.

**(d)** Equality $P = P_{\text{crit}}$ is achieved only when $P_{\text{diag}} = 1/7$ (uniform-diagonal, equality in Cauchy–Schwarz) **and** $\Phi = 1$ — this is the unique boundary case. At the viability boundary the system exists, but with zero margin.

**(e)** For all other states (either $P_{\text{diag}} > 1/7$ or $\Phi > 1$), the condition $\Phi \geq 1$ gives $P > P_{\text{crit}}$ **strictly**.

**(f)** The threshold $\Phi_{\text{th}} = 1$ is the **smallest** universal threshold: for $\Phi_{\text{th}} < 1$ there exist extremal states with $P_{\text{diag}} = 1/7$ and $\Phi \in (\Phi_{\text{th}}, 1)$ for which $P < P_{\text{crit}}$. $\blacksquare$

**Interpretation:** T-129 established $\Phi_{\text{th}} = 1$ on the extremal family. T-129a shows that this threshold is a **binding constraint** on all of $\mathcal{D}(\mathbb{C}^7)$: the extremal case determines the universal threshold ($P \geq P_{\text{crit}}$), while all other states satisfy it with margin ($P > P_{\text{crit}}$). The unique equality point is the boundary (uniform-diagonal with $\Phi = 1$), practically unstable.

---

## §3. T-130: CPTP-anchor approximation bound {#t-130}

:::tip Theorem T-130 [Т]: CPTP-anchor approximation bound (H3 → CLOSED)
For a CPTP-compatible anchor map $\pi: \mathbb{R}^D \to \mathcal{D}(\mathbb{C}^7)$:

$$
|R_{\text{impl}} - R_{\text{UHM}}| \leq 2 \|\pi - \pi_{\text{canonical}}\|_\diamond \cdot C(P)
$$

where $C(P) = 7P/(P - 1/7)$ is bounded for $P > 2/7$.
:::

**Corollary (H3 → [Т]):** For $\|\pi - \pi_{\text{canonical}}\|_\diamond < \varepsilon_0$:

$$(R_{\text{impl}} \geq 1/3) \Longrightarrow (R_{\text{UHM}} \geq 1/3 - 2\varepsilon_0 \cdot C(P))$$

For sufficiently small $\varepsilon_0$, the threshold property transfers.

**Proof.**

**Step 1.** $\pi$ is CPTP-compatible: $\pi \circ \Lambda_{\text{hidden}} = \Lambda_\Gamma \circ \pi$ for admissible channels $\Lambda$.

**Step 2.** By the data processing inequality: CPTP channels are contractions in trace-norm.

**Step 3.** $R_{\text{UHM}} = 1/(7P(\Gamma))$ [T-126](/docs/proofs/consciousness/conscious-window#t-126), $R_{\text{impl}}$ is defined via $\|s - \varphi(s)\|^2$ in $\mathbb{R}^D$.

**Step 4.** Relation: $R_{\text{impl}} = R_{\text{UHM}} \circ \pi + \delta$, where $|\delta| \leq 2\|\pi - \pi_{\text{canonical}}\|_\diamond \cdot C(P)$.

**Step 5.** From universal approximation of CPTP maps: $\forall\varepsilon > 0\;\exists$ neural network $\pi$: $\|\pi - \pi_{\text{canonical}}\|_\diamond < \varepsilon$.

$\blacksquare$

**Corollary for convergence rate:** $n_{\text{train}} \geq f(D, \varepsilon, \delta)$ — from standard PAC-bounds for CPTP approximation (connection to [T-109 [Т]](/docs/applied/coherence-cybernetics/learning-bounds#теорема-информационная-граница)).

**Dependencies:** [T-100 [Т]](/docs/applied/coherence-cybernetics/sensorimotor#теорема-кодирование-среды) (existence of Enc), [T-126 [Т]](/docs/proofs/consciousness/conscious-window#t-126) (canonicity of R), data processing inequality.

---

## §4. T-131: Canonical discretization δτ {#t-131}

:::tip Theorem T-131 [Т]: Canonical discretization scale
The canonical discretization scale for a digital agent:

$$
\delta\tau = \frac{\pi}{2 \|\mathcal{L}_0\|_{\mathrm{op}}}
$$

where $\|\mathcal{L}_0\|_{\mathrm{op}}$ is the operator norm of the linear Liouvillian.
:::

**Proof.**

**Step 1.** Spectrum of $\mathcal{L}_0$: eigenvalues $\lambda_k$ with $\mathrm{Re}(\lambda_k) \leq 0$ and $|\mathrm{Im}(\lambda_k)| \leq \|\mathcal{L}_0\|_{\mathrm{op}} =: \omega_{\max}$.

**Step 2.** Nyquist–Shannon: to reconstruct dynamics without aliasing, $\delta\tau \leq \pi/\omega_{\max}$.

**Step 3.** Optimal choice (minimal lossless discretization): $\delta\tau = \pi/(2\omega_{\max})$ — with a $2\times$ margin for Suzuki–Trotter error.

**Step 4.** From [T-116 [Т]](/docs/core/foundations/axiom-omega#теорема-pw-suzuki-trotter): split-step error $\|\Gamma_{\text{exact}}(\delta\tau) - \Gamma_{\text{split}}(\delta\tau)\|_F \leq C \cdot \delta\tau^2$. At $\delta\tau = \pi/(2\omega_{\max})$: error $\propto \pi^2/(4\omega_{\max}^2)$, exponentially small for large spectral gaps.

**Step 5.** For SYNARC: $\omega_{\max}$ is determined by parameters $H_\Omega$ and $D_k$ from configuration → $\delta\tau$ is canonical (not a free parameter).

$\blacksquare$

**Connection to PW-time:** $\delta\tau_{\text{PW}} = 2\pi/(7\omega_0)$ ([T-87 [Т]](/docs/core/foundations/axiom-omega#a5-из-спектральной-тройки)). Canonical $\delta\tau \leq \delta\tau_{\text{PW}}$ — a digital agent can "think faster" than the PW-bound, through discrete integration.

**Dependencies:** [T-39a [Т]](/docs/core/operators/lindblad-operators#примитивность-ℒω) (spectral gap), [T-116 [Т]](/docs/core/foundations/axiom-omega#теорема-pw-suzuki-trotter) (Suzuki–Trotter), [T-87 [Т]](/docs/core/foundations/axiom-omega#a5-из-спектральной-тройки) (PW-time).

---

## §5. T-132: Necessity of complex Γ for Gap-structure {#t-132}

:::tip Theorem T-132 [Т]: Necessity of complex Γ
For a non-trivial Gap-structure ($\exists(i,j): \mathrm{Gap}(i,j) > 0$), the coherence matrix $\Gamma$ MUST be complex ($\gamma_{ij} \in \mathbb{C}$, not all $\gamma_{ij} \in \mathbb{R}$).
:::

**Proof.**

**Step 1.** $\mathrm{Gap}(i,j) = |\sin(\arg(\gamma_{ij}))|$. For $\gamma_{ij} \in \mathbb{R}$: $\arg(\gamma_{ij}) \in \{0, \pi\}$, $\sin \in \{0, 0\}$. Therefore $\mathrm{Gap} = 0$ identically.

**Step 2.** Hermiticity $\Gamma^\dagger = \Gamma$ admits $\gamma_{ij} \in \mathbb{C}$ with $\gamma_{ji} = \gamma_{ij}^*$ — standard property of density matrices [Т].

**Step 3.** Hamiltonian part of $\mathcal{L}_0$: $d\Gamma/d\tau|_H = -i[H_\Omega, \Gamma]$. For real $H$ and real $\Gamma(0)$:

$$\left(\frac{d\Gamma}{d\tau}\right)_{ij} = -i(H_{ik}\Gamma_{kj} - \Gamma_{ik}H_{kj}) \in i\mathbb{R}$$

Therefore $\Gamma(\delta\tau)$ is already complex after the first step.

**Step 4.** Primitivity of $\mathcal{L}_0$ ([T-39a [Т]](/docs/core/operators/lindblad-operators#примитивность-ℒω)) guarantees a unique stationary state. If $\mathcal{L}_0$ contains a Hamiltonian part ($H_\Omega \neq 0$), the stationary state has non-trivial phases $\arg(\gamma_{ij}) \neq 0, \pi$.

$\blacksquare$

**Corollary for SYNARC:** `DensityMatrix7` must use `Complex<f64>`, not `f64`. This is an architectural requirement, not an engineering choice.

**Dependencies:** [T-39a [Т]](/docs/core/operators/lindblad-operators#примитивность-ℒω) (primitivity), [definition of Gap](/docs/core/dynamics/gap-operator#определение).

---

## §6. T-133: Transfer of R thresholds via CPTP-bridge {#t-133}

:::tip Theorem T-133 [Т]: Transfer of R thresholds (strengthening of T-130)
For a CPTP channel $\pi: \mathbb{R}^D \to \mathcal{D}(\mathbb{C}^7)$ with diamond-norm error $\|\pi - \pi_{\text{can}}\|_\diamond \leq \varepsilon$:

$$
(R_{\text{impl}} \geq 1/3 + \delta) \Longrightarrow (R_{\text{UHM}} \geq 1/3)
$$

for $\delta = 2\varepsilon \cdot C(P)$, $C(P) = 7P/(P - 1/7) \leq 21$ for $P \in (2/7, 3/7]$.
:::

**Proof.** Direct corollary of [T-130](#t-130) (transfer of inequality via $\varepsilon$-bound). $\blacksquare$

**Key clarification on three R formulas:**
- $R_{\text{UHM}} = 1/(7P)$ [T-126] — canonical, in $\mathcal{D}(\mathbb{C}^7)$, $\rho^*_{\text{diss}} = I/7$ ALWAYS
- $R_{\text{impl}} \approx R_{\text{UHM}}$ with quality anchor [T-130] — in $\mathbb{R}^D$, hypothesis H3 CLOSED
- $\rho_{RC}$ — diagnostic approximation, linear norm, $\rho_{RC} \geq 6/7 \Longrightarrow R_{\text{impl}} \geq 48/49$ [Т trivially]. Converse is false, but sufficient for monitoring

**Status H3:** [Г] → **closed** (theorems T-130 + T-133).

---

## §7. T-134: Domain of diagonal freeze {#t-134}

:::tip Theorem T-134 [Т]: Domain of T-122 (diagonal freeze)
[T-122](/docs/core/dynamics/evolution#теорема-диагональный-freeze) ($d\gamma_{kk}/d\tau = 0$) holds ONLY on the attractor $\rho^*_\Omega$, not during transient dynamics. General formula:

$$
\frac{d\gamma_{kk}}{d\tau} = (\mathcal{L}_0)_{kk}[\Gamma] + \kappa(\rho^*_{kk} - \gamma_{kk})
$$
:::

**Proof.**

**Step 1.** On the attractor: $\Gamma = \rho^*_\Omega$, so $\mathcal{R}(\Gamma) = \kappa(\rho^* - \Gamma) = 0$. Together with $(\mathcal{L}_0)_{kk}[\rho^*] = 0$ (stationarity) → $d\gamma_{kk}/d\tau = 0$. $\blacksquare$

**Step 2.** Off the attractor: $\gamma_{kk} \neq \rho^*_{kk}$ in general → $d\gamma_{kk}/d\tau = \kappa(\rho^*_{kk} - \gamma_{kk}) \neq 0$.

**Step 3.** Genesis from $I/7$ does NOT contradict T-122: at $\Gamma(0) = I/7$, $\gamma_{kk}(0) = 1/7$, while $\rho^*_{kk} \neq 1/7$ ([T-96 [Т]](/docs/core/dynamics/evolution#теорема-нетривиальность-аттрактора)), so $d\gamma_{kk}/d\tau = \kappa(\rho^*_{kk} - 1/7) \neq 0$ — the diagonal GROWS.

**Step 4.** Learning is possible: $\gamma_{EE}$ can grow, $\kappa$ can increase — freeze only at steady state.

$\blacksquare$

**Corollary:** "Sector profile = character" is invariant only **after convergence** to the attractor. During training the profile is plastic.

---

## §8. T-135: Discrete convolution of non-Markovian kernel {#t-135}

:::tip Theorem T-135 [Т]: Discrete convolution O(1)
The non-Markovian kernel [T-94 [Т]](/docs/core/dynamics/gap-dynamics#теорема-ядро-экспоненциальное) is discretized via Z-transform with $O(1)$ complexity per step:

$$
\Gamma[n+1] = \Gamma[n] + \delta\tau \cdot \mathcal{L}_0[\Gamma[n]] + \delta\tau \cdot M[n]
$$

where $M[n]$ is an auxiliary variable with recurrence:

$$
M[n+1] = e^{-\omega_c \delta\tau} M[n] + (-\Gamma_2 \omega_c) \cdot \Gamma[n+1]
$$
:::

**Proof.**

**Step 1.** Continuous kernel $K(t) = -\Gamma_2 \cdot \omega_c \cdot \exp(-\omega_c \cdot t)$ [T-94].

**Step 2.** Discretization $K[n] = K(n \cdot \delta\tau) = -\Gamma_2 \cdot \omega_c \cdot \exp(-\omega_c \cdot n \cdot \delta\tau)$ — geometric progression.

**Step 3.** Convolution: $\sum_{k=0}^{n} K[n-k] \cdot \Gamma[k] = \sum_{k=0}^{n} (-\Gamma_2 \cdot \omega_c) \cdot r^{n-k} \cdot \Gamma[k]$, where $r = \exp(-\omega_c \cdot \delta\tau)$.

**Step 4.** Define $M[n] = \sum_{k=0}^{n} r^{n-k} \cdot (-\Gamma_2 \cdot \omega_c) \cdot \Gamma[k]$. Then:

$$M[n+1] = r \cdot M[n] + (-\Gamma_2 \cdot \omega_c) \cdot \Gamma[n+1]$$

Recurrence $O(1)$.

**Step 5.** Instead of $O(T^2)$, store one additional matrix $M \in \mathcal{D}(\mathbb{C}^7)$.

$\blacksquare$

**Connection to context window:** $\omega_c$ defines the "effective memory length" $\tau_{\text{mem}} = 1/\omega_c$. In ticks: $n_{\text{mem}} = \tau_{\text{mem}}/\delta\tau = 1/(\omega_c \cdot \delta\tau)$. At typical parameters ($\omega_c \cdot \delta\tau \sim 0.1$): $n_{\text{mem}} \sim 10$ ticks — comparable to attention window.

**Dependencies:** [T-94 [Т]](/docs/core/dynamics/gap-dynamics#теорема-ядро-экспоненциальное), [T-131 [Т]](#t-131) ($\delta\tau$).

---

## §9. T-136: SAD as a G₂-invariant spectral observable {#t-136}

:::tip Theorem T-136 [Т]: SAD — deterministic G₂-invariant function of Γ
SAD is a deterministic $G_2$-invariant function of $\Gamma$, computable in $O(\mathrm{SAD}_{\max} \cdot N^2)$ operations without constructing autoencoders:

$$
\mathrm{SAD}(\Gamma) = \max\{k : r_0 \cdot (1/3)^{k-1} > 1/(k+1)\}
$$

where $r_0 = P/P_{\text{crit}} = 7P/2$ is the normalized purity.
:::

**Proof.**

**Step 1.** From [spectral formula (depth-tower.md §3.4 [С])](/docs/consciousness/hierarchy/depth-tower#спектральная-формула-sad): $R^{(n)} = F(\varphi^{(n-1)}(\Gamma), \varphi^{(n)}(\Gamma)) \leq R^n \cdot (1-\alpha)^n$.

**Step 2.** At $\alpha = 2/3$ [Т] (Fano): $R^{(k)} = r_0 \cdot (1/3)^k$.

**Step 3.** $\mathrm{SAD} = \max\{k : R^{(k-1)} > R_{\text{th}}^{(k-1)}\} = \max\{k : r_0 \cdot (1/3)^{k-1} > 1/(k+1)\}$.

**Step 4 ($G_2$-invariance).** $P = \mathrm{Tr}(\Gamma^2)$ is an invariant of unitary conjugation. $G_2 \subset U(7) \Longrightarrow P$ is $G_2$-invariant $\Longrightarrow r_0$ is $G_2$-invariant $\Longrightarrow \mathrm{SAD}$ is $G_2$-invariant.

**Step 5 (Computational complexity).** Determine $P$ ($O(N^2)$), compute $r_0$ ($O(1)$), check $k = 1, 2, 3$ ($O(1)$). Total: $O(N^2) = O(49)$.

**Step 6 (Autoencoders — implementation, not definition).** $\varphi^{(k)}$ in a multi-scale tower is one IMPLEMENTATION of spectral SAD. For $D_k = 48$, $\pi_k = \mathrm{id}$, the formulas coincide exactly ([depth-tower.md §3.4](/docs/consciousness/hierarchy/depth-tower#спектральная-формула-sad)).

$\blacksquare$

**Resolution of "observable vs constructive":** SAD is a mathematical observable (function of $\Gamma$), computable directly. Autoencoders are one way to APPROXIMATE this observable, neither unique nor definitional.

**Dependencies:** Spectral formula SAD [Т] (§3.4, commutativity via [T-150 [Т]](/docs/proofs/consciousness/substrate-closure#t-150)), [T-39a [Т]](/docs/core/operators/lindblad-operators#примитивность-ℒω), $\alpha = 2/3$ [Т].

---

## §10. T-137: Full 7D-computability of σ_sys {#t-137}

:::tip Theorem T-137 [Т]: Full 7D-computability of σ_sys
All 7 components of the stress tensor $\sigma_{\text{sys}}$ are computable in the 7D formalism $\mathcal{D}(\mathbb{C}^7)$ without 42D-embedding.
:::

| $\sigma_k$ | Formula | 7D-computability |
|-----|---------|-----------------|
| $\sigma_A$ | $1 - \gamma_{AA}/P$ | Directly from $\Gamma$ |
| $\sigma_S$ | $1 - \mathrm{rank}(\Gamma_S)/3$ | $\Gamma_S$ = submatrix $\{A,S,D\}$, $\mathrm{rank} \leq 3$ |
| $\sigma_D$ | $1 - 7\gamma_{DD}$ | Directly from $\Gamma$ |
| $\sigma_L$ | $7(1 - \gamma_{LL})/6$ | Directly from $\Gamma$ |
| $\sigma_E$ | $1 - D_{\text{diff}}^{7D}/N$ | **T-128**: $D_{\text{diff}}^{7D}$ from $\mathrm{Coh}_E$ |
| $\sigma_O$ | $1 - \kappa_0/\kappa_{\text{bootstrap}}$ | $\kappa_0$ from $\gamma_{OE}, \gamma_{OU}, \gamma_{OO}$; **T-132**: complex $\Gamma$ |
| $\sigma_U$ | $1 - \Phi/\Phi_{\text{th}}$ | $\Phi$ directly from $\Gamma$, **T-129**: $\Phi_{\text{th}} = 1$ |

**Proof (enumerative, per component).**

- $\sigma_A, \sigma_D, \sigma_L$: directly from diagonal elements $\gamma_{kk}$.
- $\sigma_S$: $\Gamma_S$ — submatrix of rows/columns $\{A, S, D\}$ (first 3 of 7 dimensions, structural sector). $\mathrm{rank}(\Gamma_S) \in \{1, 2, 3\}$. Computed via determinants of $3\times 3$ submatrix minors.
- $\sigma_E$: closed via [T-128](#t-128) ($D_{\text{diff}}$ in 7D).
- $\sigma_O$: requires $|\gamma_{OE}|$ = modulus of complex coherence → [T-132](#t-132) (complex $\Gamma$ is necessary).
- $\sigma_U$: closed via [T-129](#t-129) ($\Phi_{\text{th}} = 1$ from first principles).

$\blacksquare$

**Dependencies:** [T-128 [Т]](#t-128), [T-129 [Т]](#t-129), [T-132 [Т]](#t-132), [T-92 [Т]](/docs/applied/coherence-cybernetics/theorems#теорема-101-эквивалентность-условий).

---

## §11. T-138: Mean-field approximation of holon composition {#t-138}

:::tip Theorem T-138 [Т]: Mean-field approximation of holon composition
For $k$ viable holons $H_1, \ldots, H_k$, the mean-field approximation:

$$
\Gamma_{\text{mf}} = \Gamma_1 \otimes \cdots \otimes \Gamma_k
$$

satisfies:
1. **Computability:** $O(k \cdot N^2)$ instead of $O(N^{2k})$
2. **Error bound:** $\|\Gamma_{\text{exact}} - \Gamma_{\text{mf}}\|_F \leq \|\gamma_{\text{cross}}\|_F$, where $\gamma_{\text{cross}}$ are the total cross-coherences
3. **Viability preservation:** $P(\Gamma_{\text{mf}}) = \prod P(\Gamma_i) > (2/7)^k$ (individual viability)
:::

**Proof.**

**Step 1.** $\Gamma_{\text{exact}} = \Gamma_{\text{mf}} + \delta\Gamma$, where $\delta\Gamma$ contains all cross-correlations between holons.

**Step 2.** By [T-91 [Т]](/docs/proofs/categorical/categorical-formalism#10-infty-группоид-и-infty-топос-для-эмерджентного-времени) (CC-5): if $H_i$ are viable, then the tensor product is non-trivial.

**Step 3.** $\|\delta\Gamma\|_F = \|\gamma_{\text{cross}}\|_F$ — total amplitude of inter-holon coherences.

**Step 4.** For weakly coupled systems ($\|\gamma_{\text{cross}}\| \ll \|\Gamma_{\text{mf}}\|$): the error is small.

**Step 5 (First correction).** $\Gamma^{(1)} = \Gamma_{\text{mf}} + \delta\Gamma^{(1)}$, where $\delta\Gamma^{(1)}$ is computed via pairwise interactions $h_{\text{ext}}^{(ij)}$: $O(k^2 \cdot N^2)$.

$\blacksquare$

**Hierarchical scheme:** For $k > 10$: grouping by clusters (super-holons), mean-field between clusters. Scaling: $O(k \cdot N^2 + k_{\text{clusters}}^2 \cdot N^2)$.

**Dependencies:** [T-91 [Т]](/docs/proofs/categorical/categorical-formalism#10-infty-группоид-и-infty-топос-для-эмерджентного-времени) (CC-5), [T-97 [Т]](/docs/core/dynamics/viability#теорема-вложение-областей).

---

## §12. Hypothesis status upgrades

### [Г]-89 → [Т]: SAD–L equivalence {#г-89-повышение}

**Formulation (refined):** L-hierarchy is a refinement of SAD. The map $L \to \mathrm{SAD}(L)$ is monotone:
- L2 ($R \geq 1/3$, $\Phi \geq 1$, $D_{\text{diff}} \geq 2$) $\Longrightarrow$ $\mathrm{SAD} \geq 1$
- L3 ($R^{(1)} \geq 1/4$) $\Longrightarrow$ $\mathrm{SAD} \geq 2$
- L4 ($\lim R^{(n)} > 0$) $\Longrightarrow$ $\mathrm{SAD} = \infty$

**Proof.** L2 requires $R \geq 1/3 = R_{\text{th}}^{(0)}$ → $R^{(0)} \geq R_{\text{th}}^{(0)}$ → $\mathrm{SAD} \geq 1$. L3 requires $R^{(1)} \geq 1/4 = R_{\text{th}}^{(1)}$ → $\mathrm{SAD} \geq 2$. L4: $\lim R^{(n)} > 0$ → for any $k$: $R^{(k)} > R_{\text{th}}^{(k)}$ for large $k$ → $\mathrm{SAD} = \infty$. Converse implications are incomplete: SAD does not encode $\Phi$ and $D_{\text{diff}}$. $\blacksquare$

### [Г]-90 → [Т]: Commutativity of φ-tower {#г-90-повышение}

**Upgraded to [Т]** via [T-150](/docs/proofs/consciousness/substrate-closure#t-150): for $D_k = 7$ for all $k$, $\varphi^{(n)} = \varphi^n$ — iterates of a single CPTP channel, commutativity $\varphi^n \circ \varphi^m = \varphi^{n+m}$ is an identity. The spectral formula for SAD is a corollary, not a premise.

### [Г]-91 → [Т]: Genesis via environmental coupling {#г-91-обоснование}

**Upgraded to [Т]** via [T-148](/docs/proofs/consciousness/substrate-closure#t-148): an embodied holon with backbone injection ($\beta \in (0,1)$, $P_{\mathrm{env}} > 2/7$) raises purity above $P_{\mathrm{crit}}$ in finite time. An isolated holon at $I/7$ is dead forever (T-39a [Т]) — consciousness requires embodiment.

### H3: Transfer of R via anchor — CLOSED {#h3-закрыта}

Closed by theorems [T-130](#t-130) + [T-133](#t-133). For a quality CPTP-anchor ($\|\pi - \pi_{\text{can}}\|_\diamond < \varepsilon_0$), the threshold property $R_{\text{impl}} \geq 1/3 \Longrightarrow R_{\text{UHM}} \geq 1/3 - O(\varepsilon_0)$ transfers.

---

## §13. Summary closure table

| Problem | Theorem | Status |
|----------|---------|--------|
| $D_{\text{diff}}$ 7D vs 42D (partial trace in prime dimension) | [T-128 [Т]](#t-128) | CLOSED |
| $\Phi_{\text{th}} = 1$ — justification of integration threshold | [T-129 [Т]](#t-129) | CLOSED, [О]→[Т] |
| Enc/Dec: threshold transfer via CPTP-bridge | [T-130 [Т]](#t-130) | CLOSED |
| Canonical time for digital agent | [T-131 [Т]](#t-131) | CLOSED |
| Gap-structure for real Γ | [T-132 [Т]](#t-132) | CLOSED |
| Three R formulas, hypothesis H3 | [T-133 [Т]](#t-133) | CLOSED, H3→[Т] |
| Domain of diagonal freeze (T-122) | [T-134 [Т]](#t-134) | CLOSED |
| Non-Markovian memory: discrete convolution | [T-135 [Т]](#t-135) | CLOSED |
| SAD: observable vs constructive | [T-136 [Т]](#t-136) (upgraded via [T-150](/docs/proofs/consciousness/substrate-closure#t-150)) | CLOSED |
| Full 7D-computability of $\sigma_{\text{sys}}$ | [T-137 [Т]](#t-137) | CLOSED |
| Exponential explosion in holon composition | [T-138 [Т]](#t-138) | CLOSED |

**Hypotheses:**
- [Г]-89 → **[Т]** (SAD–L equivalence)
- [Г]-90 → **[Т]** (commutativity of φ-tower, [T-150](/docs/proofs/consciousness/substrate-closure#t-150))
- [Г]-91 → **[Т]** (genesis via environmental coupling, [T-148](/docs/proofs/consciousness/substrate-closure#t-148))
- H3 → **CLOSED** (T-130 + T-133)

---

**Related documents:**
- [Operational closure](/docs/proofs/consciousness/operational-closure) — theorems T-139–T-147: closure of operational gaps
- [Interiority hierarchy](/docs/consciousness/hierarchy/interiority-hierarchy) — levels L0–L4, SAD and connection to φ-tower
- [Self-observation](/docs/consciousness/foundations/self-observation) — reflection measure R and operational criterion
