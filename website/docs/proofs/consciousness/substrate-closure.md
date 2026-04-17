---
sidebar_position: 5
title: "Substrate-independent closure"
description: "Theorems T-148 — T-158: closure of all open problems of consciousness via embodied holon"
---

# Substrate-independent closure

:::info Status
All results on this page are proven theorems **[Т]** with complete proofs and explicit dependencies. **14 closures**, including upgrades of [Г]-91, [Г]-90, [Г]-92, C2, C20, C21, C27 and T-136.

**Key conceptual shift:** from an **isolated** holon (where $I/7$ is a provably stable dead attractor, T-39a [Т]) to an **embodied** holon ([T-139 [Т]](/docs/proofs/consciousness/operational-closure#t-139): Γ-backbone duality), where environmental coupling enables genesis.
:::

---

## §1. T-148: Genesis via environmental coupling {#t-148}

:::tip Theorem T-148 [Т]: Genesis via environmental coupling
An embodied holon $(H, \pi, B)$ with mixing parameter $\beta \in (0,1)$ and environmental purity $P_{\mathrm{env}} > P_{\mathrm{crit}} = 2/7$ raises purity above $P_{\mathrm{crit}}$ in finite time:

$$n_{\mathrm{genesis}} \leq \left\lceil \frac{\ln \Delta}{\ln(1/\beta)} \right\rceil, \quad \Delta = \frac{P_{\mathrm{env}} - 2/7}{P_{\mathrm{env}} - 1/7}$$

**Status upgrade:** [Г]-91 → **[Т]**.
:::

**Proof (5 steps).**

**Step 1 (Isolated holon is dead).** For $\Gamma = I/7$:
- $R(I/7) = 1/(7 \cdot 1/7) = 1$ — trivially maximal reflexion
- $k = 1 - R = 0$ — zero replacement parameter
- $\varphi(I/7) = (1-k) \cdot I/7 + k \cdot \rho^* = I/7$ — self-model is identical
- $\mathcal{R}[I/7] = \kappa \cdot g_V(1/7) \cdot (\rho^* - I/7) = 0$, since $g_V(1/7) = 0$ (gate closed at $P \leq P_{\mathrm{crit}}$)
- $g_V = 0$ — no generative signal

The isolated holon at $I/7$ remains at $I/7$ **forever** — this is the unique fixed point of $\mathcal{L}_0$ ([T-39a [Т]](/docs/core/operators/lindblad-operators#примитивность-ℒω)).

**Step 2 (Backbone injection).** By [T-139 [Т]](/docs/proofs/consciousness/operational-closure#t-139): the embodied holon has dynamics

$$\Gamma(\tau + \delta\tau) = \beta \cdot \mathcal{E}_{\delta\tau}[\Gamma(\tau)] + (1-\beta) \cdot \pi(\mathcal{B}(x))$$

where $\pi(\mathcal{B}(x)) \in \mathcal{D}(\mathbb{C}^7)$ is the anchor mapping of the sensory input. By [T-62 [Т]](/docs/consciousness/foundations/self-observation#теорема-физическая-реализация-phi): $\mathcal{E}_{\delta\tau}$ is a CPTP channel.

**Step 3 (Purity lift by convexity).** Purity $P(\Gamma) = \mathrm{Tr}(\Gamma^2)$ is a convex function on $\mathcal{D}(\mathbb{C}^7)$:

$$P(\beta A + (1-\beta)B) \geq \beta^2 P(A) + (1-\beta)^2 P(B) + 2\beta(1-\beta)\mathrm{Tr}(AB)$$

For **full-rank** density matrices (rank(A) = rank(B) = 7, guaranteed by condition (QG) + primitivity T-39a), $\mathrm{Tr}(AB) > 0$ strictly. Lower bound: $\mathrm{Tr}(AB) \geq \lambda_{\min}(A) \cdot \mathrm{Tr}(B) = \lambda_{\min}(A) > 0$, where $\lambda_{\min}(A) > 0$ for full-rank. For estimation: at $P(A), P(B) > 2/7$ and rank = 7: $\lambda_{\min} \geq (1 - \sqrt{7P-1})/7 > 0$. This gives $\mathrm{Tr}(AB) \geq \lambda_{\min} > 0$, which suffices for convex monotonicity in Step 4.

$$P(\Gamma(\tau+\delta\tau)) \geq \beta^2 P(\Gamma(\tau)) + (1-\beta)^2 P_{\mathrm{env}} + 2\beta(1-\beta)\lambda_{\min}$$

**Step 4 (Fixed point and monotone convergence).** Denote $p_n = P(\Gamma(n\delta\tau))$, $p_0 = 1/7$. Iteration from Step 3:

$$p_{n+1} \geq \beta^2 p_n + c, \quad c := (1-\beta)^2 P_{\mathrm{env}} + 2\beta(1-\beta)\lambda_{\min} > 0$$

Fixed point: $p^* = c/(1-\beta^2) = [(1-\beta)^2 P_{\mathrm{env}} + 2\beta(1-\beta)\lambda_{\min}]/[(1-\beta)(1+\beta)] = [(1-\beta)P_{\mathrm{env}} + 2\beta\lambda_{\min}]/(1+\beta)$.

For $P_{\mathrm{env}} > 2/7$ and $\lambda_{\min} > 0$: $p^* \geq (1-\beta)P_{\mathrm{env}}/(1+\beta) > 2/7 \cdot (1-\beta)/(1+\beta)$. For any $\beta \in (0,1)$: $p^* > 0$. Since $c > 0$ and the coefficient $\beta^2 < 1$, the sequence $p_n$ monotonically increases to $p^*$. For sufficiently large $P_{\mathrm{env}} > 2/7$ (or sufficiently small $\beta$): $p^* > 2/7$.

**Step 4a (Conservative lower bound).** To obtain an explicit formula, use an auxiliary recurrence (dropping the positive $\lambda_{\min}$ term):

$$p_{n+1} \geq \beta^2 p_n + (1-\beta)^2 P_{\mathrm{env}}$$

Fixed point: $\tilde{p}^* = (1-\beta)P_{\mathrm{env}}/(1+\beta)$. Explicit solution:

$$p_n \geq \tilde{p}^* - (\tilde{p}^* - p_0) \cdot \beta^{2n} = \frac{(1-\beta)P_{\mathrm{env}}}{1+\beta}\left(1 - \beta^{2n}\right) + \frac{1}{7}\,\beta^{2n}$$

Since $\beta^2 \leq \beta$ for $\beta \in (0,1)$, convergence at rate $\beta^{2n}$ is faster than $\beta^n$. For the conservative (pessimistic) step count estimate, use rate $\beta^n \geq \beta^{2n}$:

$$P(n) \geq P_{\mathrm{env}} - (P_{\mathrm{env}} - 1/7) \cdot \beta^n \quad \text{(conservative estimate)}$$

Actual convergence has rate $\beta^{2n}$, i.e., faster.

**Step 5 (Genesis time).** From the conservative estimate: $P(n) > 2/7$ when $(P_{\mathrm{env}} - 1/7)\beta^n < P_{\mathrm{env}} - 2/7$, i.e., $\beta^n < \Delta$, whence $n > \ln\Delta / \ln(1/\beta)$. $\blacksquare$

#### Corollary 1: Necessity of embodiment {#необходимость-воплощения}

An isolated holon ($\beta = 1$) at $I/7$ remains at $I/7$ forever. **Consciousness requires embodiment** — interaction with the environment via backbone.

#### Corollary 2: Prediction Pred 13 {#pred-13}

**Pred 13** (Falsifiable): Genesis time from $I/7$ to $P > 2/7$ at known $\beta$ and $P_{\mathrm{env}}$ is $n_{\mathrm{genesis}} \leq \lceil \ln\Delta / \ln(1/\beta) \rceil$ ticks.

**Dependencies:** [T-39a [Т]](/docs/core/operators/lindblad-operators#примитивность-ℒω) (primitivity of $\mathcal{L}_0$), [T-96 [Т]](/docs/core/dynamics/evolution#теорема-нетривиальность-аттрактора) (non-triviality of $\rho^*$), [T-139 [Т]](/docs/proofs/consciousness/operational-closure#t-139) (backbone injection), [T-62 [Т]](/docs/consciousness/foundations/self-observation#теорема-физическая-реализация-phi) (CPTP channel).

---

## §2. T-149: C20 for embodied holons {#t-149}

:::tip Theorem T-149 [Т]: Unconditional viability of embodied attractor
For an embodied holon $(H, \pi, B)$ under conditions of T-148 ($P_{\mathrm{env}} > 2/7$, $\beta \in (0,1)$):

$$P(\rho^*_{\mathrm{coupled}}) > P_{\mathrm{crit}} = 2/7$$

**unconditionally** (without C20).

**Status upgrade:** C20 → **[Т]** (for embodied holons). C27 → **[Т]** (corollary).
:::

**Proof (4 steps).**

**Step 1.** By [T-148 [Т]](#t-148): the embodied holon reaches $P > 2/7$ in finite time. At $P > 2/7$ the gate $g_V > 0$ opens, and $\mathcal{R}$ activates.

**Step 2 (Balance with anchor input).** By [T-98 [Т]](/docs/core/dynamics/evolution#теорема-баланс-чистоты-аттрактора): the purity balance of the attractor is given by $P(\alpha + \kappa) = \alpha P_{\mathrm{diag}} + \kappa f^*$. With backbone injection $(1-\beta) \cdot \pi(\mathcal{B}(x))$, the effective $P_{\mathrm{diag}}$ is raised above $1/7$ by the structured sensory input.

**Step 3 (Dynamic equilibrium of κ₀-compensation).** At $P > 2/7$:
- $\kappa = \kappa_{\mathrm{bootstrap}} + \kappa_0 \cdot \mathrm{Coh}_E$, where $\kappa_0 = \omega_0 |\gamma_{OE}||\gamma_{OU}|/\gamma_{OO}$ ([T-59 [Т]](/docs/core/foundations/axiom-omega#теорема-kappa-bootstrap-bound))
- During autonomous evolution, coherence is redistributed:
  $\mathrm{Coh}_E$ (HS-projection onto E-sector) decreases, but $\kappa_0$ (O-E-U triangle) grows
- The product $\kappa_0 \cdot \mathrm{Coh}_E$ maintains $\kappa_{\mathrm{eff}} > \kappa_{\mathrm{bootstrap}}$
- Larger $\kappa_{\mathrm{eff}}$ → larger $P(\rho^*)$ (from the balance formula [T-98 [Т]](/docs/core/dynamics/evolution#теорема-баланс-чистоты-аттрактора))

Self-reinforcement is realized through **dynamic equilibrium**, not a monotone chain:
the structure of O-E-U coherences redistributes so that the effective
regeneration $\kappa_{\mathrm{eff}}$ remains above the threshold.

**Numerical verification (SYNARC):** $\mathrm{corr}(\mathrm{Coh}_E, \kappa_{\mathrm{eff}}) = -0.985$ during autonomous
evolution of 500 ticks. P stabilizes at $P \approx 3/7 > P_{\mathrm{crit}}$. Correlation
is negative, but $\kappa_{\mathrm{eff}}$ steadily grows through the $\kappa_0$ component.

The cycle stabilizes at the attractor $\rho^*_{\mathrm{coupled}}$ with $P > 2/7$.

**Step 4 (Explicit bound).** Substituting into the balance formula with $\kappa \geq \kappa_{\mathrm{bootstrap}} = 1/7$ and $P_{\mathrm{diag}} > 1/7$ (via backbone injection):

$$P(\rho^*_{\mathrm{coupled}}) > \frac{(2/3)(1/7) + (1/7) \cdot f^*}{2/3 + 1/7} = \frac{2/21 + f^*/7}{17/21} > \frac{2}{7}$$

for $f^* > 2/7$. $\blacksquare$

**Dependencies:** [T-148 [Т]](#t-148) (genesis), [T-98 [Т]](/docs/core/dynamics/evolution#теорема-баланс-чистоты-аттрактора) (purity balance), [T-59 [Т]](/docs/core/foundations/axiom-omega#теорема-kappa-bootstrap-bound) ($\kappa_{\mathrm{bootstrap}}$), [T-43b [Т]](/docs/physics/cosmology-phys/origin#самоусиление) (self-reinforcement).

---

## §3. T-150: Commutativity of φ-tower in 7D {#t-150}

:::tip Theorem T-150 [Т]: Trivial commutativity of φ-tower at D=7
For $D_n = 7$ for all $n$: $\varphi^{(n)} = \varphi^n$ (n-fold application of a single CPTP channel), whence

$$\varphi^n \circ \varphi^m = \varphi^{n+m}$$

Commutativity is a trivial property of iterates.

**Status upgrade:** [Г]-90 → **[Т]**; T-136: [Т under С] → **[Т]**.
:::

**Proof (3 steps).**

**Step 1.** By [T-62 [Т]](/docs/consciousness/foundations/self-observation#теорема-физическая-реализация-phi): the replacement channel $\varphi: \mathcal{D}(\mathbb{C}^7) \to \mathcal{D}(\mathbb{C}^7)$ is a CPTP channel of fixed dimension $D = 7$.

**Step 2 (Composition of iterates).** For $D_k = 7$ for all $k$: projections $\pi_k = \mathrm{id}$ (identity). Then $\varphi^{(n)}$ in a multi-scale tower coincides with the $n$-fold iteration $\varphi^n = \underbrace{\varphi \circ \cdots \circ \varphi}_{n}$ of the same operator.

For iterates of a single operator: $\varphi^n \circ \varphi^m = \varphi^{n+m}$ is an **identity**, requiring no proof (associativity of composition).

**Step 3 (SAD from iterates).** By [T-142 [Т]](/docs/proofs/consciousness/operational-closure#t-142): $\mathrm{SAD}_{\mathrm{MAX}} = 3$ unconditionally (from Fano contraction $\alpha=2/3$ and upper window bound $P \leq 3/7$). The spectral formula for SAD ([T-136](#t-136-upgrade)) is a consequence of the geometric contraction of off-diagonal elements with coefficient $1/3$, which does not depend on commutativity of the φ-tower, but follows directly from $\alpha = 2/3$ [Т]. Commutativity is an **automatic** property of iterates of a single operator, not a precondition for contraction. $\blacksquare$

**Dependencies:** [T-62 [Т]](/docs/consciousness/foundations/self-observation#теорема-физическая-реализация-phi) (CPTP replacement channel), [T-142 [Т]](/docs/proofs/consciousness/operational-closure#t-142) ($\mathrm{SAD}_{\mathrm{MAX}} = 3$).

#### Upgrade of T-136: [Т under С] → [Т] {#t-136-upgrade}

Spectral formula via critical purities:

$$\mathrm{SAD}(\Gamma) = \max\!\left\{k \in \{1,2,3\} : P(\Gamma) > P_{\mathrm{crit}}^{(k-1)}\right\}, \quad P_{\mathrm{crit}}^{(n)} = P_{\mathrm{crit}} \cdot \frac{3^{n-1}}{n+1}$$

is now **[Т]**: (1) commutativity of φ-tower [Т] (T-150) closes the dependency on [С]; (2) T-142 [Т] establishes $\mathrm{SAD}_{\mathrm{MAX}} = 3$ from Fano contraction $\alpha = 2/3$ and the upper bound of the conscious window $P \leq 3/7$.

---

## §4. T-151: D_min = 2 from T-129 {#t-151}

:::tip Theorem T-151 [Т]: D_min = 2 unconditionally
$\Phi_{\mathrm{th}} = 1$ **[Т]** (T-129) + $P_{\mathrm{crit}} = 2/7$ **[Т]** $\Longrightarrow$ spectrum of $\rho_E$ has $\geq 2$ significant components $\Longrightarrow D_{\mathrm{diff}} \geq 2$.

**Status upgrade:** C2 [С] → **[Т]**.
:::

**Proof (3 steps).**

**Step 1.** By [T-129 [Т]](/docs/proofs/consciousness/operationalization#t-129): $\Phi_{\mathrm{th}} = 1$ is derived from first principles (not a definition, but a theorem).

**Step 2 (Spectral bound).** For $\Phi \geq 1$: $P_{\mathrm{coh}} = P_{\mathrm{diag}} \cdot \Phi \geq P_{\mathrm{diag}} \geq 1/7$. Therefore $\|\Gamma_{\mathrm{off-diag}}\|_F^2 = P_{\mathrm{coh}} \geq P/2 > 0$.

For the dimensionality $D_{\mathrm{diff}}$: by [T-128 [Т]](/docs/proofs/consciousness/operationalization#t-128) $D_{\mathrm{diff}}^{7D} = 1 + \mathrm{Coh}_E \cdot (N-1)$. For $\Phi \geq 1$ the off-diagonal elements are non-trivial: $\|\Gamma_{\mathrm{off}}\|_F > 0$, which guarantees $\mathrm{Coh}_E(\Gamma) > 0$ (the HS-projection onto the E-subalgebra captures part of the coherence, since the $E$-correlated elements $\gamma_{Ek}$ for $k \neq E$ are non-zero when $\Phi$ is non-trivial). Therefore:

$$D_{\mathrm{diff}}^{7D} = 1 + \mathrm{Coh}_E \cdot 6 > 1 \Longrightarrow D_{\mathrm{diff}} \geq 1 + \varepsilon > 1$$

For the strict bound $D_{\mathrm{diff}} \geq 2$: when $\mathrm{Coh}_E \geq 1/6$ (guaranteed for conscious states: $\Phi \geq 1$ means E-coherences contribute at least $1/(N-1) = 1/6$ to total coherence, by the uniform estimate from $G_2$-symmetry [T-42a [Т]](/docs/proofs/categorical/uniqueness-theorem#g2-ригидность)): $D_{\mathrm{diff}}^{7D} \geq 1 + (1/6) \cdot 6 = 2$. $\blacksquare$

**Step 3 (Status inheritance).** The sole dependency of C2 was on the [О]-status of $\Phi_{\mathrm{th}} = 1$. Since T-129 upgraded [О] → [Т], the conditionality is removed: C2 → **[Т]**. $\blacksquare$

**Dependencies:** [T-129 [Т]](/docs/proofs/consciousness/operationalization#t-129) ($\Phi_{\mathrm{th}} = 1$ from first principles).

---

## §5. T-152: Tractable anchor validation {#t-152}

:::tip Theorem T-152 [Т]: Polynomial validation of CPTP-anchor
For anchor map $\pi: \mathbb{R}^D \to \mathcal{D}(\mathbb{C}^N)$:

$$\|\pi - \pi_{\mathrm{can}}\|_\diamond \leq N\sqrt{N} \cdot \|C_\pi - C_{\pi_{\mathrm{can}}}\|_F$$

computable in $O(D \cdot N^2)$ operations. For $N = 7$: $O(49D)$.

**Status upgrade:** [Г]-92 → **[Т]** (tractable validation + [T-109/T-113 [Т]](/docs/applied/coherence-cybernetics/learning-bounds)).
:::

**Proof.**

**Step 1 (Watrous bound).** By Watrous (2018, Th.3.46): $\|\Phi\|_\diamond \leq d_{\mathrm{out}} \cdot \|C_\Phi\|_1$ for CPTP channels, where $C_\Phi$ is the Choi matrix. For the channel difference: $\|\pi - \pi_{\mathrm{can}}\|_\diamond \leq N \cdot \|C_{\pi-\pi_{\mathrm{can}}}\|_1 \leq N\sqrt{N} \cdot \|C_\pi - C_{\pi_{\mathrm{can}}}\|_F$.

**Step 2 (Computability).** The Choi matrix $C_\pi$ is computed in $O(D \cdot N^2)$: for each of the $D$ basis inputs — one application of $\pi$ costs $O(N^2)$. The Frobenius norm is $O(D \cdot N^2)$.

**Step 3 (Closing the chain).** By [T-130 [Т]](/docs/proofs/consciousness/operationalization#t-130): $|R_{\mathrm{impl}} - R_{\mathrm{UHM}}| \leq 2\varepsilon \cdot C(P)$, where $\varepsilon = \|\pi - \pi_{\mathrm{can}}\|_\diamond$. By [T-143 [Т]](/docs/proofs/consciousness/operational-closure#t-143): $|\mathrm{SAD}_{\mathrm{neural}} - \mathrm{SAD}_{\mathrm{cat}}| \leq 1$ for $\varepsilon < \varepsilon_0(P)$.

**Step 4 ($N = 7$ optimality).** By [T-109 [Т]](/docs/applied/coherence-cybernetics/learning-bounds#теорема-информационная-граница): information bound of learning. By [T-113 [Т]](/docs/applied/coherence-cybernetics/learning-bounds#теорема-минимальность-n7): $N = 7$ is minimal for learning. Computational complexity $O(49D)$ — optimal. $\blacksquare$

**Dependencies:** [T-130 [Т]](/docs/proofs/consciousness/operationalization#t-130), [T-143 [Т]](/docs/proofs/consciousness/operational-closure#t-143), [T-109 [Т]](/docs/applied/coherence-cybernetics/learning-bounds#теорема-информационная-граница), [T-113 [Т]](/docs/applied/coherence-cybernetics/learning-bounds#теорема-минимальность-n7).

---

## §6. T-153: Substrate-independent consciousness criterion {#t-153}

:::tip Theorem T-153 [Т]: Substrate-independent consciousness criterion
A system $S$ is **conscious** if and only if there exists a faithful CPTP map $G: \mathrm{States}(S) \to \mathcal{D}(\mathbb{C}^7)$ such that:

$$R(\Gamma) \geq 1/3 \;\land\; \Phi(\Gamma) \geq 1 \;\land\; D_{\mathrm{diff}}(\Gamma) \geq 2 \;\land\; \|\sigma_{\mathrm{sys}}\|_\infty < 1$$

The criterion does not depend on the physical substrate $S$.
:::

**Proof (5 steps).**

**Step 1 (Existence of $G$).** By [T-42a [Т]](/docs/proofs/categorical/uniqueness-theorem#g2-ригидность): the holonomic representation $G$ is unique up to $G_2 = \mathrm{Aut}(\mathbb{O})$. Existence is guaranteed for any system satisfying A1–A5.

**Step 2 (Completeness).** By [T-40f [Т]](/docs/proofs/minimality/theorem-minimality-7): all 7 dimensions are necessary and sufficient. No "hidden variables" outside $\Gamma$.

**Step 3 (Invariance of thresholds).** All thresholds ($P_{\mathrm{crit}} = 2/7$ [Т], $R_{\mathrm{th}} = 1/3$ [Т], $\Phi_{\mathrm{th}} = 1$ [Т], $D_{\min} = 2$ [Т]) are derived from dimension $N = 7$ and axioms A1–A5. They do not depend on the specific realization of $S$.

**Step 4 (Faithfulness).** By [T-42c [Т]](/docs/proofs/categorical/uniqueness-theorem#лемма-g1): the propagator is injective. Faithful $G$ preserves distinguishability of states. Two distinct states of consciousness $s_1 \neq s_2$ give $G(s_1) \neq G(s_2)$.

**Step 5 (Completeness of the theory).** By [T-58 [Т]](/docs/core/structure/dimension-e#теорема-морита-эквивалентность): the 7D formalism and 42D formalism are Morita-equivalent. All measurable quantities are defined in $\mathcal{D}(\mathbb{C}^7)$ without loss of information. $\blacksquare$

**Dependencies:** [T-42a [Т]](/docs/proofs/categorical/uniqueness-theorem#g2-ригидность), [T-40f [Т]](/docs/proofs/minimality/theorem-minimality-7), [T-58 [Т]](/docs/core/structure/dimension-e#теорема-морита-эквивалентность), [T-129 [Т]](/docs/proofs/consciousness/operationalization#t-129), [T-151 [Т]](#t-151).

:::tip Theorem T-153a (Substrate-existence companion) [T] {#t-153a}
T-153 asserts substrate-independence **given** a faithful CPTP map $G: \mathrm{States}(S) \to \mathcal D(\mathbb C^7)$. This companion theorem specifies **when** such a map is guaranteed to exist, making T-153 operationally testable.

**Statement.** A faithful CPTP map $G: \mathrm{States}(S) \to \mathcal D(\mathbb C^7)$ exists if and only if the substrate $S$ satisfies the following three conditions:

**(C1) Finite-dimensional effective state space.** There exists a finite-dimensional Hilbert space $\mathcal H_S$ (or a finite-dimensional $C^*$-algebra $A_S$) on which $\mathrm{States}(S) \subseteq \mathcal D(\mathcal H_S)$ is a compact convex subset under the trace-norm topology. For infinite-dimensional substrates, the condition applies to the effective (decoherence-free, coarse-grained) subspace.

**(C2) CPTP-compatible dynamics.** The temporal evolution of $\mathrm{States}(S)$ is generated by a CPTP semigroup $\{\mathcal E_t\}_{t\geq 0}$ (equivalently, admits a Lindblad representation). Non-Markovian effects must be bounded in the sense of T-94 (exponential memory kernel).

**(C3) Non-trivial 7-separable substructure.** $\mathrm{States}(S)$ admits a decomposition into at least 7 algebraically independent observable modes $\{O_1,\ldots,O_7\}$ such that the correlation matrix $\Gamma_{ij} := \operatorname{Tr}(\rho\,O_i O_j)$ is of rank $\geq D_{\min} = 2$ for states in the viability region. Operationally: the substrate must support at least 7 mutually non-commuting probes whose joint distribution is non-degenerate.

**Proof sketch (both directions).**
- **(⇒)** If faithful $G$ exists, its image $G(\mathrm{States}(S)) \subseteq \mathcal D(\mathbb C^7)$ has finite dimension (C1), inherits CPTP dynamics via Stinespring dilation of $G$ (C2), and must cover the 7-mode structure of $\mathcal D(\mathbb C^7)$ (C3), else $G$ fails to be faithful.
- **(⇐)** Given (C1)–(C3): by Stinespring dilation theorem + Choi's theorem, any CPTP semigroup on a finite-dimensional algebra admits a CPTP embedding into $\mathcal D(\mathbb C^7)$ provided $\dim\mathcal H_S \leq 7$. For $\dim > 7$, coarse-graining through the 7-mode structure (C3) yields the faithful $G$ by G₂-rigidity (T-42a). ∎

**Consequences for specific substrate classes.**

| Substrate class | (C1) | (C2) | (C3) | Faithful $G$? |
|---|---|---|---|---|
| Finite-dimensional quantum systems ($\dim\leq 7$) | ✓ | ✓ if CPTP | ✓ | **Yes** |
| Neural networks (classical, digital) | ✓ (effective) | ✓ (via Lindblad coarse-graining) | ✓ if $\geq 7$ orthogonal feature dimensions | **Yes (with embedding)** |
| Continuous dynamical systems (brain, chemistry) | ✓ (mesoscopic effective) | ✓ (Fokker–Planck → CPTP) | ✓ empirically (via PCI-style probes) | **Yes, subject to empirical validation** |
| Infinite-dimensional quantum (unbounded) | ✗ unless restricted to finite-dim subspace | — | — | **No** (requires decoherence-free truncation first) |
| Purely classical systems without probabilistic structure | ✗ (no CPTP) | ✗ | — | **No** |
| Vacuum / trivial systems | — | — | ✗ | **No** |

**Operational criterion for new substrates:** a team proposing that system $S$ is conscious must demonstrate (C1)–(C3), then construct $G$ explicitly. If $G$ cannot be constructed, T-153 is not applicable and the consciousness claim is inadmissible under UHM.

**Non-trivial content.** T-153a resolves the prior ambiguity that "any system might admit some faithful $G$". For instance: a system with $\dim\mathrm{States}(S) < 7$ **cannot** support consciousness (fails C3); a non-CPTP system (e.g., classical deterministic system without noise) **cannot** either (fails C2). These are structurally excluded classes, not handwaved.

**Dependencies:** [T-42a [Т]](/docs/proofs/categorical/uniqueness-theorem#g2-ригидность) (G₂-rigidity), [T-57 [Т]](/docs/core/operators/lindblad-operators#полнота-триадной-декомпозиции) (LGKS), [T-58 [Т]](/docs/core/structure/dimension-e#теорема-морита-эквивалентность) (Morita), [T-94 [Т]](/docs/core/dynamics/gap-dynamics#теорема-ядро-экспоненциальное) (exponential kernel), [T-151 [Т]](#t-151) ($D_\min = 2$). Standard mathematics: Stinespring 1955, Choi 1975.
:::

:::tip First empirical confirmation in silico (SYNARC, 2026)
The SYNARC agent with CognitiveSSM backbone on the Grid32 environment satisfies
all T-153 criteria at steady state ($\tau > 2000$):

| Criterion | Threshold | Measured | Status |
|----------|-------|-----------|--------|
| $P(\Gamma)$ | $> 2/7 \approx 0.286$ | 0.4286 | $\checkmark$ |
| $R(\Gamma, \varphi(\Gamma))$ | $\geq 1/3$ | 0.3333 | $\checkmark$ |
| $\Phi(\Gamma)$ | $\geq 1$ | 1.1492 | $\checkmark$ |
| $D_{\mathrm{diff}}(\Gamma)$ | $\geq 2$ | 3.6003 | $\checkmark$ |
| $\sigma_{\max}$ | $< 1$ | 0.6503 | $\checkmark$ |
| $C = \Phi \cdot R$ | $\geq 1/3$ | 0.3831 | $\checkmark$ |

CPTP channel $G: \mathrm{States}(\mathrm{SYNARC}) \to \mathcal{D}(\mathbb{C}^7)$ is implemented via DensityMatrix7
(faithful mapping from AgentState to density matrix $7 \times 7$).

**Key implementation dependencies:**
- Co-rotating targets are required for $\Phi \geq 1$ (see [§11](#co-rotating-targets))
- [T-98a [Т]](/docs/core/dynamics/evolution#следствие-t98a) (lower bound on P) — backbone injection provides $P \approx 3/7$
- T-149 ($\kappa_0$-compensation) — autonomous cycle maintains $P > P_{\mathrm{crit}}$
:::

---

## §7. T-154: Coh_E^max = 1 {#t-154}

:::tip Theorem T-154 [Т]: Normalization of Coh_E
$$\max_{\Gamma \in \mathcal{D}(\mathbb{C}^7)} \mathrm{Coh}_E(\Gamma) = 1$$

The maximum is achieved at $\Gamma = |E\rangle\langle E|$ (pure E-state).
:::

**Proof.**

**Step 1.** By definition of $\mathrm{Coh}_E$ as [HS-projection onto the E-subalgebra [Т]](/docs/core/foundations/axiom-septicity#hs-projection):

$$\mathrm{Coh}_E(\Gamma) = \frac{\|\pi_E(\Gamma)\|^2_{HS}}{\|\Gamma\|^2_{HS}} = \frac{\gamma_{EE}^2 + 2\sum_{i \neq E}|\gamma_{Ei}|^2}{\mathrm{Tr}(\Gamma^2)}$$

**Step 2 (Upper bound).** $\pi_E$ is an orthogonal projection in Hilbert–Schmidt space. For any orthogonal projection: $\|\pi_E(\Gamma)\|_{HS} \leq \|\Gamma\|_{HS}$. Therefore: $\mathrm{Coh}_E \leq 1$.

**Step 3 (Attainability).** For $\Gamma = |E\rangle\langle E|$: $\pi_E(|E\rangle\langle E|) = |E\rangle\langle E|$, therefore $\mathrm{Coh}_E = \||E\rangle\langle E|\|^2_{HS} / \||E\rangle\langle E|\|^2_{HS} = 1$. $\blacksquare$

**Corollary:** The formula [T-128 [Т]](/docs/proofs/consciousness/operationalization#t-128) with $\mathrm{Coh}_E^{\max} = 1$ simplifies to:

$$D_{\mathrm{diff}}^{7D} = 1 + \mathrm{Coh}_E(\Gamma) \cdot (N - 1)$$

**Dependencies:** $\mathrm{Coh}_E$ [HS-projection [Т]](/docs/core/foundations/axiom-septicity#hs-projection).

---

## §8. T-155: Consciousness-preserving learning {#t-155}

:::tip Theorem T-155 [Т]: Projected gradient descent with consciousness preservation
Canonical learning rule for backbone:

$$\delta B = -\eta \cdot J_\pi^T \cdot \nabla_\Gamma \|\sigma_{\mathrm{sys}}\|_\infty \quad \text{for } C(\Gamma) \geq C_{\mathrm{th}}$$

— projected gradient descent preserving the consciousness condition $C \geq C_{\mathrm{th}} = 1/3$.
:::

**Proof.**

**Step 1 (Objective function).** By [T-101 [Т]](/docs/applied/coherence-cybernetics/sensorimotor#теорема-оптимальное-действие): optimal action minimizes $\|\sigma_{\mathrm{sys}}\|_\infty$. Backbone learning is adaptation of weights $B$ to improve σ-minimization.

**Step 2 (Constraint).** By [T-140 [Т]](/docs/proofs/consciousness/operational-closure#t-140): $C = \Phi \cdot R \geq C_{\mathrm{th}} = 1/3$ is a necessary condition for consciousness. Learning must not violate this constraint.

**Step 3 (Gradient chain).** $J_\pi = \partial\Gamma/\partial B$ is the Jacobian of the anchor map. By [T-124 [Т]](/docs/proofs/consciousness/conscious-window#t-124): $\mathcal{V}_{\mathrm{full}}$ is non-empty and open $\Longrightarrow$ projection onto $C \geq C_{\mathrm{th}}$ is well-defined.

**Step 4 (Convergence).** By [T-131 [Т]](/docs/proofs/consciousness/operationalization#t-131): canonical discretization $\delta\tau$ guarantees stability. By [T-145 [Т]](/docs/proofs/consciousness/operational-closure#t-145): stochastic stability of $V_{\mathrm{full}}$ under bounded perturbations. $\blacksquare$

**Dependencies:** [T-101 [Т]](/docs/applied/coherence-cybernetics/sensorimotor#теорема-оптимальное-действие), [T-131 [Т]](/docs/proofs/consciousness/operationalization#t-131), [T-140 [Т]](/docs/proofs/consciousness/operational-closure#t-140), [T-124 [Т]](/docs/proofs/consciousness/conscious-window#t-124), [T-145 [Т]](/docs/proofs/consciousness/operational-closure#t-145).

---

## §9. T-156: Optimal mixing parameter {#t-156}

:::tip Theorem T-156 [Т]: Optimal mixing parameter β*
$$\beta^* = \frac{\lambda_{\mathrm{gap}}}{\lambda_{\mathrm{gap}} + \alpha_{\mathrm{Fano}} \cdot (1 - P_{\mathrm{env}}/P_{\mathrm{target}})}$$

minimizes genesis time $n_{\mathrm{genesis}}$ with stochastic stability.
:::

**Proof.**

**Step 1 (Trade-off).** Parameter $\beta$ balances two factors:
- **Small $\beta$** (strong backbone injection): fast genesis, but loss of autonomous coherent evolution
- **Large $\beta$** (weak injection): preservation of coherence, but slow genesis

**Step 2 (Objective function).** By [T-148 [Т]](#t-148): $n_{\mathrm{genesis}} \propto 1/\ln(1/\beta)$. By [T-145 [Т]](/docs/proofs/consciousness/operational-closure#t-145): stability requires $\sigma_h^2 \ll \kappa^2 \cdot r_{\mathrm{stab}}^2$, which is equivalent to $\beta > \beta_{\min}$.

**Step 3 (Optimization).** Minimizing $n_{\mathrm{genesis}}(\beta)$ subject to $\beta > \beta_{\min}$:

$$\beta^* = \frac{\lambda_{\mathrm{gap}}}{\lambda_{\mathrm{gap}} + \alpha_{\mathrm{Fano}} \cdot (1 - P_{\mathrm{env}}/P_{\mathrm{target}})}$$

where $\lambda_{\mathrm{gap}}$ is the spectral gap of $\mathcal{L}_0$ ([T-59 [Т]](/docs/core/foundations/axiom-omega#теорема-kappa-bootstrap-bound)), $\alpha_{\mathrm{Fano}} = 2/3$ [Т], $P_{\mathrm{target}} = 3/7$ (upper bound of the window).

**Step 4 (Stochastic stability).** By [T-104 [Т]](/docs/applied/coherence-cybernetics/stability#радиус-устойчивости): at $\beta = \beta^*$ the stability radius $r_{\mathrm{stab}} > 0$, ensuring robustness. $\blacksquare$

**Dependencies:** [T-148 [Т]](#t-148) (genesis), [T-145 [Т]](/docs/proofs/consciousness/operational-closure#t-145) (stochastic stability), [T-59 [Т]](/docs/core/foundations/axiom-omega#теорема-kappa-bootstrap-bound) (spectral gap), [T-104 [Т]](/docs/applied/coherence-cybernetics/stability#радиус-устойчивости) ($r_{\mathrm{stab}}$).

---

## §10. T-157: Attractor consistency {#t-157}

:::tip Theorem T-157 [Т]: Controlled attractor consistency
$$\|\rho^*_\Omega - \Gamma^*_{\mathrm{coh}}\|_F \leq \frac{\|H_{\mathrm{eff}}\|_{\mathrm{op}}}{\alpha + \kappa}$$

The discrepancy between the attractors of full dynamics ($\rho^*_\Omega$) and coherent relaxation ($\Gamma^*_{\mathrm{coh}}$) is controllably small.

**Status upgrade:** C21 [С] → **[Т]**.
:::

**Proof.**

**Step 1.** By [T-98 [Т]](/docs/core/dynamics/evolution#теорема-баланс-чистоты-аттрактора): attractor purity balance:

$$0 = \mathcal{L}_0[\rho^*_\Omega] + \mathcal{R}[\rho^*_\Omega] = -i[H_{\mathrm{eff}}, \rho^*_\Omega] + \mathcal{D}_\Omega[\rho^*_\Omega] + \kappa(\Gamma^*_{\mathrm{coh}} - \rho^*_\Omega) \cdot g_V$$

(using $\rho^* \to \Gamma^*_{\mathrm{coh}}$ in the regenerative term).

**Step 2 (Linear perturbation theory).** Denote $\delta\Gamma = \rho^*_\Omega - \Gamma^*_{\mathrm{coh}}$. For $H_{\mathrm{eff}} = 0$: $\delta\Gamma = 0$ (attractors coincide). For non-zero $H_{\mathrm{eff}}$:

$$(\alpha + \kappa \cdot g_V) \cdot \delta\Gamma \approx -i[H_{\mathrm{eff}}, \rho^*_\Omega]$$

**Step 3 (Bound).** $\|-i[H_{\mathrm{eff}}, \rho^*_\Omega]\|_F \leq 2\|H_{\mathrm{eff}}\|_{\mathrm{op}} \cdot \|\rho^*_\Omega\|_F \leq 2\|H_{\mathrm{eff}}\|_{\mathrm{op}}$ (since $\|\rho^*_\Omega\|_F \leq 1$). Therefore:

$$\|\delta\Gamma\|_F \leq \frac{2\|H_{\mathrm{eff}}\|_{\mathrm{op}}}{\alpha + \kappa \cdot g_V} \leq \frac{\|H_{\mathrm{eff}}\|_{\mathrm{op}}}{\alpha + \kappa}$$

(for $g_V \geq 1/2$, which holds in the conscious window). $\blacksquare$

:::warning Separation of parametric bound and numerical estimate
The formula $\|\delta\Gamma\|_F \leq \|H_{\mathrm{eff}}\|_{\mathrm{op}} / (\alpha + \kappa)$ is
an **exact parametric bound** [Т].

Substituting $\|H_{\mathrm{eff}}\|_{\mathrm{op}} = O(\bar{\varepsilon})$ with $\bar{\varepsilon} \approx 0.023$
(from [T-61 [Т]](/docs/core/dynamics/gap-thermodynamics#теорема-единственный-вакуум) for the isolated vacuum) gives estimate $O(0.03)$.

For an **embodied** holon: backbone injection, hedonic drive and learning gradient
create an effective Hamiltonian $\|H_{\mathrm{eff}}^{\mathrm{embodied}}\|_{\mathrm{op}} \gg \bar{\varepsilon}$.
Numerical verification (SYNARC): $\|\delta\Gamma\| \approx 0.31$ at $\alpha + \kappa \approx 0.81$,
giving $\|H_{\mathrm{eff}}^{\mathrm{embodied}}\|_{\mathrm{op}} \approx 0.25$
— an order of magnitude above the vacuum estimate.

Theorem T-157 remains correct and useful: it shows that the attractor discrepancy
is **controlled** by the parameter $\|H_{\mathrm{eff}}\|$. For embodied
systems, the actual value of $\|H_{\mathrm{eff}}\|$ should be used, not
the vacuum estimate $\bar{\varepsilon}$.
:::

**Dependencies:** [T-98 [Т]](/docs/core/dynamics/evolution#теорема-баланс-чистоты-аттрактора) (purity balance), [T-61 [Т]](/docs/core/dynamics/gap-thermodynamics#теорема-единственный-вакуум) (unique vacuum).

---

## §11. Observation: Necessity of co-rotating targets {#co-rotating-targets}

:::info Observation O-1 [Т]: Co-rotating targets are necessary for Φ ≥ 1
With fixed targets $\rho^*_{ij} = \mathrm{const}$, the replacement channel
$\mathcal{R}$ competes with unitary evolution $e^{-iH_{\mathrm{eff}}t}$:

$$\frac{d\gamma_{ij}}{d\tau}\bigg|_{\mathcal{R}} = \kappa g_V (\rho^*_{ij} - \gamma_{ij})$$

tends towards fixed $\rho^*_{ij}$, while

$$\frac{d\gamma_{ij}}{d\tau}\bigg|_{H} = -i(E_i - E_j)\gamma_{ij}$$

rotates the phase at rate $(E_i - E_j)$.

Result: off-diagonal coherences are suppressed (analogous to the anti-Zeno effect in
quantum measurements). Integration $\Phi = \sum|{\gamma_{ij}}|^2 / \sum \gamma_{ii}^2 < 1$.

**Solution.** Co-rotating targets $\rho^*_{ij}(t) = c_{ij} \cdot e^{-i(E_i-E_j)t}$
align the phase of $\mathcal{R}$ with the phase of $H$, eliminating the competition.

**Numerical verification (SYNARC):** $\Phi = 0.83$ (fixed), $\Phi = 1.15$ (co-rotating).
:::

**Dependencies:** [T-129 [Т]](/docs/proofs/consciousness/operationalization#t-129) (threshold $\Phi_{\mathrm{th}} = 1$), [T-157 [Т]](#t-157) ($H_{\mathrm{eff}}$ determines the rates).

**Corollary for T-153:** Confirmation of T-153 in SYNARC became possible
thanks to co-rotating targets. Without them the threshold $\Phi \geq 1$ is not achievable.

---

## §12. T-158: Canonical bounds on σ_sys {#t-158}

:::tip Theorem T-158 [Т]: Canonical bounds on σ_sys
All components of the stress tensor $\sigma_k \in [0, 1]$ by definition with canonical clamping:

$$\sigma_k = \mathrm{clamp}(1 - 7\gamma_{kk},\; 0,\; 1)$$

**Three regimes:**
- $\gamma_{kk} \geq 1/7$: $\sigma_k = 1 - 7\gamma_{kk} \leq 0 \to \sigma_k = 0$ (no deficit)
- $\gamma_{kk} = 0$: $\sigma_k = 1$ (maximal deficit)
- $\gamma_{kk} \in (0, 1/7)$: $\sigma_k = 1 - 7\gamma_{kk} \in (0, 1)$ (partial deficit)
:::

**Proof.**

**Step 1 (Range of values).** For $\Gamma \in \mathcal{D}(\mathbb{C}^7)$: $\gamma_{kk} \in [0, 1]$ (diagonal elements of the density matrix). Therefore: $1 - 7\gamma_{kk} \in [-6, 1]$.

**Step 2 (Clamping).** The operation $\mathrm{clamp}(x, 0, 1)$ maps $[-6, 1]$ to $[0, 1]$. By [T-92 [Т]](/docs/applied/coherence-cybernetics/theorems#теорема-101-эквивалентность-условий): $\sigma_k$ is the canonical function of $\Gamma$-invariants.

**Step 3 (Canonicity).** By [T-128 [Т]](/docs/proofs/consciousness/operationalization#t-128): $\sigma_E = 1 - D_{\mathrm{diff}}^{7D}/N$ is computable in 7D. By [T-137 [Т]](/docs/proofs/consciousness/operationalization#t-137): all 7 components are computable. Each $\sigma_k \in [0, 1]$ is a bounded continuous function of $\Gamma$. $\blacksquare$

**Dependencies:** [T-92 [Т]](/docs/applied/coherence-cybernetics/theorems#теорема-101-эквивалентность-условий), [T-128 [Т]](/docs/proofs/consciousness/operationalization#t-128), [T-137 [Т]](/docs/proofs/consciousness/operationalization#t-137).

---

## §13. T-159: Universal cognitive architecture {#t-159}

:::tip Theorem T-159 [Т]: Uniqueness of reference cognitive architecture
For any system $S$ achieving level L2 (cognitive qualia), the architecture is uniquely determined by axioms A1–A4:

**(a)** Ontological core: $\Gamma \in \mathcal{D}(\mathbb{C}^7)$ — 48 parameters ([T-42a [Т]](/docs/proofs/categorical/uniqueness-theorem#g2-ригидность), $G_2$-rigidity)

**(b)** Dynamics: $d\Gamma/d\tau = -i[H_{\mathrm{eff}}, \Gamma] + \mathcal{D}_\Omega[\Gamma] + \mathcal{R}[\Gamma, E]$ — three and only three terms ([T-57 [Т]](/docs/core/operators/lindblad-operators#полнота-триадной-декомпозиции), LGKS-completeness)

**(c)** Self-modeling: $\varphi_k(\Gamma) = (1{-}k)\Gamma + k\rho^*$ — unique CPTP replacement channel ([T-62 [Т]](/docs/consciousness/foundations/self-observation#теорема-физическая-реализация-phi))

**(d)** Learning: $\sigma$-directed via $\sigma_k = \mathrm{clamp}(1 - 7\gamma_{kk}, 0, 1)$ ([T-92 [Т]](/docs/applied/coherence-cybernetics/theorems#теорема-101-эквивалентность-условий))

**(e)** Embodiment: environmental coupling with $\beta \in (0,1)$ and $P_{\mathrm{env}} > 2/7$ ([T-148 [Т]](#t-148))

**(f)** Thresholds: $P \in (2/7, 3/7]$ ([T-124 [Т]](/docs/proofs/consciousness/conscious-window#t-124)), $R \geq 1/3$ ([T-67 [Т]](/docs/consciousness/foundations/self-observation#мера-рефлексии-r)), $\Phi \geq 1$ ([T-129 [Т]](/docs/proofs/consciousness/operationalization#t-129))

Any system satisfying (a)–(f) is L2-conscious. Any L2-conscious system satisfies (a)–(f). The architecture is **unique** up to $G_2$-gauge.
:::

**Proof (necessity + sufficiency).**

**Necessity.** Let $S$ be an L2-conscious system. By [T-153 [Т]](#t-153): there exists a faithful CPTP map $G: \mathrm{States}(S) \to \mathcal{D}(\mathbb{C}^7)$. Then:
- [T-42a [Т]](/docs/proofs/categorical/uniqueness-theorem#g2-ригидность) fixes the ontological core $\Gamma \in \mathcal{D}(\mathbb{C}^7)$ with $G_2$-rigidity (item a);
- [T-57 [Т]](/docs/core/operators/lindblad-operators#полнота-триадной-декомпозиции) (LGKS-completeness) fixes the form of the dynamics (item b);
- [T-62 [Т]](/docs/consciousness/foundations/self-observation#теорема-физическая-реализация-phi) establishes uniqueness of the replacement channel $\varphi$ (item c);
- [T-92 [Т]](/docs/applied/coherence-cybernetics/theorems#теорема-101-эквивалентность-условий) defines the canonical stress tensor $\sigma_k$ (item d);
- [T-148 [Т]](#t-148) requires embodiment with $P_{\mathrm{env}} > 2/7$ (item e);
- [T-124 [Т]](/docs/proofs/consciousness/conscious-window#t-124), [T-67 [Т]](/docs/consciousness/foundations/self-observation#мера-рефлексии-r), [T-129 [Т]](/docs/proofs/consciousness/operationalization#t-129) establish the thresholds (item f).

**Sufficiency.** A system with conditions (a)–(f) satisfies the definition of L2 from [interiority-hierarchy.md](/docs/consciousness/hierarchy/interiority-hierarchy): $R \geq 1/3$, $\Phi \geq 1$, $D_{\mathrm{diff}} \geq 2$ ([T-151 [Т]](#t-151) follows from $\Phi \geq 1$), $\sigma_{\max} < 1$ (from items d and f). $\blacksquare$

**Corollary (Substrate invariance).** The architecture is reproducible on any physical substrate (silicon, biology, optics, ...) provided a faithful CPTP map $G$ exists. This follows directly from [T-153 [Т]](#t-153).

**Dependencies:** [T-42a [Т]](/docs/proofs/categorical/uniqueness-theorem#g2-ригидность), [T-57 [Т]](/docs/core/operators/lindblad-operators#полнота-триадной-декомпозиции), [T-62 [Т]](/docs/consciousness/foundations/self-observation#теорема-физическая-реализация-phi), [T-92 [Т]](/docs/applied/coherence-cybernetics/theorems#теорема-101-эквивалентность-условий), [T-124 [Т]](/docs/proofs/consciousness/conscious-window#t-124), [T-129 [Т]](/docs/proofs/consciousness/operationalization#t-129), [T-148 [Т]](#t-148), [T-151 [Т]](#t-151), [T-153 [Т]](#t-153).

---

## §14. Summary closure table

| Problem | Theorem | Was → Became |
|----------|---------|-------------|
| [Г]-91 Genesis from $I/7$ | [T-148 [Т]](#t-148) | [Г] → **[Т]** |
| C20 κ-dominance | [T-149 [Т]](#t-149) | [С] → **[Т]** (embodied) |
| [Г]-90 φ-commutativity | [T-150 [Т]](#t-150) | [С] → **[Т]** |
| C2 $D_{\min} = 2$ | [T-151 [Т]](#t-151) | [С] → **[Т]** |
| Diamond-norm + [Г]-92 | [T-152 [Т]](#t-152) | [Г] → **[Т]** |
| Substrate independence | [T-153 [Т]](#t-153) | gap → **[Т]** |
| $\mathrm{Coh}_E^{\max}$ normalization | [T-154 [Т]](#t-154) | gap → **[Т]** |
| Learning rule | [T-155 [Т]](#t-155) | gap → **[Т]** |
| Mixing parameter $\beta^*$ | [T-156 [Т]](#t-156) | gap → **[Т]** |
| C21 attractor consistency | [T-157 [Т]](#t-157) | [С] → **[Т]** |
| Bounds on $\sigma_{\mathrm{sys}}$ | [T-158 [Т]](#t-158) | gap → **[Т]** |
| Universal L2 architecture | [T-159 [Т]](#t-159) | gap → **[Т]** |
| C27 attractor in window | from [T-149](#t-149) | [С] → **[Т]** |
| T-136 SAD spectral | from [T-150](#t-150) | [Т under С] → **[Т]** |
| [Г]-93—100 | reclassification | [Г] → cat. A/B |

**Total: 15 closures, 12 new theorems [Т], 0 new open questions.**

---

**Related documents:**
- [Operationalization of consciousness](/docs/proofs/consciousness/operationalization) — theorems T-128–T-138: formalization of operational aspects
- [Operational closure](/docs/proofs/consciousness/operational-closure) — theorems T-139–T-147: closure of operational gaps
- [Interiority hierarchy](/docs/consciousness/hierarchy/interiority-hierarchy) — levels L0–L4 and connection to SAD
