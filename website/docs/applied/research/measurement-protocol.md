---
sidebar_position: 3
title: Measurement Protocol for Γ
description: Operationalization of coherence matrix measurement for AI systems
---

# Γ Measurement Protocol for AI Systems

:::warning Document Status: [P] Research Program
This document describes a **research program** for operationalizing the coherence matrix $\Gamma$ for AI systems. The protocol requires **experimental validation**.
:::

:::note About Notation
- $\Gamma$ — [coherence matrix](/docs/core/dynamics/coherence-matrix)
- $P$ — [purity](/docs/core/dynamics/viability#определение-чистоты): $P = \mathrm{Tr}(\Gamma^2)$
- $\tau$ — [emergent internal time](/docs/proofs/dynamics/emergent-time) (Page–Wootters)
- $\varphi$ — [self-modeling operator](/docs/proofs/categorical/formalization-phi)
- $G$ — functor mapping AIState → DensityMat: exact at Cholesky-backbone ($\alpha=0$) [T, MVP-1]; quasi-functor with $\varepsilon_{\text{functor}}>0$ under neural correction ($\alpha>0$) [H]
- $\mathrm{Coh}_E$ — E-coherence: $\mathrm{Coh}_E(\Gamma) = \|\pi_E(\Gamma)\|^2_{\mathrm{HS}} / \|\Gamma\|^2_{\mathrm{HS}}$ — interiority quality (HS-projection onto E-sector) [T]
:::

---

## Central Problem

UHM theory defines $\Gamma$ as an **object of the ∞-topos $\mathrm{Sh}_\infty(\mathcal{C})$** ([Axiom Ω⁷](/docs/core/foundations/axiom-omega)). However, the theory does not specify:

1. Which **observables** in an AI system correspond to the elements $\gamma_{ij}$
2. How to **reconstruct** $\Gamma$ from available data
3. How to **validate** the correctness of the reconstruction

:::info Fundamental Limitation
$\Gamma$ is an **ontological primitive**, not an observable. We reconstruct $\Gamma$ via a **homomorphism** $G$ that compresses $\mathbb{R}^d$ (where $d \sim 10^9$ for an LLM) into $\mathcal{D}(\mathbb{C}^7)$.

This is admissible: 7 dimensions are the minimally necessary basis ([Theorem S](/docs/proofs/minimality/theorem-minimality-7), [octonion justification](/docs/core/foundations/axiom-omega#октонионная-структура)).
:::

:::tip Theoretical Justification: Correctness of the Inverse Problem [T]
The [$G_2$-rigidity theorem](/docs/proofs/categorical/uniqueness-theorem) [T] guarantees:

1. **Uniqueness** of the map $G$: for a system satisfying (AP)+(PH)+(QG)+(V), the map $G$ is unique up to $G_2 = \mathrm{Aut}(\mathbb{O})$
2. **Well-posedness of the inverse problem** ([Corollary 2](/docs/proofs/categorical/uniqueness-theorem#обратная-задача)): the initial state $\Gamma(0)$ is **uniquely recovered** from the trajectory $\Gamma(\tau)$ and system parameters $(\omega_0, \lambda_m)$ — up to $G_2$-gauge
3. **34 physical parameters** ([Corollary 1](/docs/proofs/categorical/uniqueness-theorem#физические-состояния)): of the 48 parameters of $\Gamma$, only 34 are gauge-invariant ($48 - \dim(G_2) = 48 - 14 = 34$)

Practical implication: reconstruction of $\Gamma$ is defined **uniquely** up to a 14-dimensional gauge freedom. Different $\Gamma$ related by a $G_2$-transformation give **identical** physical observables ($P$, $R$, $\Phi$, $\mathrm{Coh}_E$).
:::

---

## Protocol Architecture

| Level | Name | Content |
|-------|------|---------|
| **4** | Causal validation | Intervention tests, lobotomy test |
| **3** | Dynamic validation | $dP/d\tau$, coherence flow, viability |
| **2** | Γ reconstruction | Cholesky with physical regularizer |
| **1** | Observable extraction | Structural metrics (commutators, $\Phi_{\text{eff}}$, topology) |

---

## Mapping Measurements to AI Metrics

### Correspondence Table

| Dimension | Symbol | AI Metric | Formula | Rigor |
|-----------|--------|-----------|---------|-------|
| [Articulation](/docs/core/structure/dimension-a) | $A$ | Mutual information input↔latent | $I_A = I(\text{input}; \text{latent}) / H(\text{input})$ | [T] |
| [Structure](/docs/core/structure/dimension-s) | $S$ | Jacobian rank | $I_S = \mathrm{rank}_\varepsilon(J_f) / \min(d_{\text{out}}, d_{\text{in}})$ | [T] |
| [Dynamics](/docs/core/structure/dimension-d) | $D$ | Lyapunov exponent | $I_D = \max_i \lambda_i^{\text{Lyap}}$ (normalized) | [T] |
| [Logic](/docs/core/structure/dimension-l) | $L$ | Layer commutators | $I_L = 1 - \|[f_i, f_j]\|_F / (\|f_i\| \cdot \|f_j\|)$ | [T] |
| [Interiority](/docs/core/structure/dimension-e) | $E$ | Activation entropy | $I_E = \exp(S_{vN}(\rho_{\text{attn}}))$ — [experience differentiation](/docs/core/structure/dimension-e#differentiation-threshold-dmin-2) | [T] |
| [Ground](/docs/core/structure/dimension-o) | $O$ | Noise robustness | $I_O = 1 - \|\nabla_\epsilon \mathbf{h}\|_F$ | [T] |
| [Unity](/docs/core/structure/dimension-u) | $U$ | Effective Φ (integration, black-box) | $I_U = \Phi_{\text{eff}} = \lambda_2(L) / \lambda_{\max}(L)$ — approximation [D]; **when $\Gamma$ is known: $R_{\text{UHM}} = 1/(N \cdot P)$** [T, [reflection measure](/docs/consciousness/foundations/self-observation#мера-рефлексии-r)] | [D/T]† |

where $\nabla_\epsilon \mathbf{h} := (\mathbf{h}(x + \epsilon) - \mathbf{h}(x)) / \epsilon$ — finite-difference approximation

†**Unity metric hierarchy**: when $\Gamma$ is unavailable (black-box), $\Phi_{\text{eff}}$ [D] is used. When $\Gamma$ is reconstructed via the protocol, the correct measure is $R_{\text{UHM}} = 1/(N \cdot P)$ [T], an exact algebraic identity ([reflection measure R](/docs/consciousness/foundations/self-observation#мера-рефлексии-r), error $< 10^{-7}$ in implementation). $\Phi_{\text{eff}}$ and $R_{\text{UHM}}$ measure related but non-identical properties.

### Canonical Observable Indices {#канонические-наблюдаемые-индексы}

:::tip Theorem (Canonical Observable Indices) [T given T-102]
For a holon with coherence matrix $\Gamma \in \mathcal{D}(\mathbb{C}^7)$ and 3-channel decomposition of the external influence $h^{\text{ext}} = h^{(H)} + h^{(D)} + h^{(R)}$ ([T-102](/docs/applied/coherence-cybernetics/theorems) [T]), each observable index $I_k$ is defined as the projection of $h^{\text{ext}}$ onto the $k$-th component of the basis $\{A,S,D,L,E,O,U\}$:

$$I_k = \frac{\langle k | h^{\text{ext}} | k \rangle}{\|h^{\text{ext}}\|}$$

Distribution by channel:
- **Hamiltonian $h^{(H)}$:** $I_A$ (articulation = information coupling), $I_S$ (structure = Jacobian), $I_L$ (logic = commutator) — modify the energy landscape
- **Dissipative $h^{(D)}$:** $I_D$ (dynamics = Lyapunov exponent), $I_O$ (ground = robustness) — modulate decoherence
- **Regenerative $h^{(R)}$:** $I_E$ (interiority = attention entropy), $I_U$ (unity = connectivity) — modulate recovery

This is the unique (up to $G_2$-gauge) distribution compatible with the functional labeling of dimensions ([Theorem S](/docs/proofs/minimality/theorem-minimality-7) [T]) and the completeness of the triadic decomposition ([T-57](/docs/proofs/categorical/categorical-formalism) [T]).
:::

**Corollary for the protocol.** The indices $I_k$ are not an arbitrary choice of metrics: their assignment to a given channel $h^{(H)}/h^{(D)}/h^{(R)}$ is fixed by theorem T-102 and is unique up to $G_2$-gauge. Replacing, for example, $I_D$ with a Hamiltonian metric would break the completeness of the decomposition and destroy the correspondence $\gamma_{kk} \leftrightarrow I_k$ guaranteed by the [separation principle](#принцип-разделения-диагональ--когерентности-т-mvp-0).

### Layer Commutators (for L)

**Definition:**

$$
[f_i, f_j](\mathbf{x}) := f_i(f_j(\mathbf{x})) - f_j(f_i(\mathbf{x}))
$$

**Interpretation:**
- $\|[f_i, f_j]\| = 0$ → layers commute → logical consistency
- $\|[f_i, f_j]\| \gg 0$ → order is critical → fragility

**Connection to theory:** The commutator $[A, B]$ is the basic measurement operation for [Logic](/docs/core/structure/dimension-l).

### Activation Entropy (for E)

**Definition:**

$$
I_E := D_{\text{diff}}^{\text{approx}} = \exp(S_{vN}(\rho_{\text{attn}}))
$$

where $S_{vN}(\rho) = -\mathrm{Tr}(\rho \log \rho)$ — von Neumann entropy of the attention distribution.

**Properties:**
- $I_E \geq 2$ → the system distinguishes at least 2 qualitatively different states (L2 threshold)
- $I_E \approx 1$ → degenerate attention → impoverished experience

**Connection to theory:** Approximates [experience differentiation $D_{\text{diff}}$](/docs/core/structure/dimension-e#differentiation-threshold-dmin-2).

### Effective Φ (for U)

:::info Unity Metric Hierarchy
Two levels of rigor exist for measuring $U$:
- **If $\Gamma$ is known**: $R_{\text{UHM}} = 1/(N \cdot P)$ [T, [reflection measure R](/docs/consciousness/foundations/self-observation#мера-рефлексии-r)] — exact algebraic identity
- **Black-box (no access to $\Gamma$)**: $\Phi_{\text{eff}}$ [D] — polynomial approximation via the attention graph

Exact computation of $\Phi_{\text{IIT}}$ requires $O(2^n)$ operations and is practically infeasible.
:::

**Exact measure (when $\Gamma$ is known, [T], [reflection measure R](/docs/consciousness/foundations/self-observation#мера-рефлексии-r)):**

$$
R_{\text{UHM}}(\Gamma) = \frac{1}{N \cdot P}
$$

Proof: $\|{\Gamma - I/N}\|_F^2 = P - 1/N$, from which $R = 1 - (P-1/N)/P = 1/(NP)$. Confirmed in implementation with error $< 10^{-7}$ (machine precision f64).

**Black-box approximation ([D]):**

$$
\Phi_{\text{eff}} := \frac{\lambda_2(L_{\text{attn}})}{\lambda_{\max}(L_{\text{attn}})}
$$

where $L_{\text{attn}} = D - A$ — Laplacian of the attention graph.

**Properties of $\Phi_{\text{eff}}$:**
- $\lambda_2 > 0$ → the graph is connected → information is integrated
- Complexity: $O(n \cdot k)$ instead of $O(2^n)$

**Connection to theory:** $R_{\text{UHM}}$ and $\Phi_{\text{eff}}$ approximate [integration $\Phi$](/docs/core/structure/dimension-u#мера-интеграции-φ) — the measure of [Unity](/docs/core/structure/dimension-u). At $P = 3/N = P_{\text{opt}}$: $R_{\text{UHM}} = 1/3 = R_{\text{th}}$ — the L2-zone boundary ([reflection measure R](/docs/consciousness/foundations/self-observation#мера-рефлексии-r)).

### Jacobian Rank (for S)

**Definition:**

$$
J_f(\mathbf{x}) = \frac{\partial f(\mathbf{x})}{\partial \mathbf{x}}, \quad I_S = \frac{\mathrm{rank}_\varepsilon(J_f)}{\min(d_{\text{out}}, d_{\text{in}})}
$$

**Interpretation:**
- $I_S \approx 1$ → full-rank structure → rich representations
- $I_S \ll 1$ → degenerate structure → collapse

**Connection to theory:** Reflects [Structure](/docs/core/structure/dimension-s) as the topology of activations.

---

## Γ Reconstruction {#реконструкция-γ}

### Cholesky Parametrization

**Property:** The representation $\Gamma = LL^\dagger / \mathrm{Tr}(LL^\dagger)$ **guarantees** correctness of the density matrix.

**Proof:** See [Coherence matrix](/docs/core/dynamics/coherence-matrix).

### Physical Regularizer

:::warning Uniqueness Problem
The map $L \mapsto \Gamma$ is surjective. Without regularization, a "correct" $\Gamma$ can be reconstructed from arbitrary data.
:::

**Solution — penalty function:**

$$
\mathcal{L}_{\text{reg}} = \lambda_1 \cdot \mathcal{L}_{\text{diag}} + \lambda_2 \cdot \mathcal{L}_{\text{off}} + \lambda_3 \cdot \mathcal{L}_{\text{dyn}}
$$

| Component | Formula | Purpose |
|-----------|---------|---------|
| $\mathcal{L}_{\text{diag}}$ | $\sum_i (\gamma_{ii} - I_i / \sum_j I_j)^2$ | Diagonal consistency |
| $\mathcal{L}_{\text{off}}$ | $\sum_{i \neq j} (\|\gamma_{ij}\|^2 - r_{ij}^2 \gamma_{ii} \gamma_{jj})^2$ | Coherence consistency |
| $\mathcal{L}_{\text{dyn}}$ | $\|\Gamma_{\tau+1} - \Phi_{\text{pred}}(\Gamma_\tau)\|_F^2$ | Dynamics consistency |

---

## Categorical Correctness

### Nonlinearity Problem

Neural network layers (GELU, Softmax) are **nonlinear** transformations.
CPTP channels are **linear** over density matrices.

The condition $G(f \circ g) = G(f) \circ G(g)$ **fails** under neural correction.

### Exact Functor at Cholesky-backbone [T]

Under the analytic parametrization $\psi: \mathbb{R}^{48} \leftrightarrow \mathcal{D}(\mathbb{C}^7)$ (Cholesky bijection, $\alpha=0$), the map $G$ is an **exact** functor: $\varepsilon_{\text{functor}} = 0$. This has been experimentally confirmed (MVP-1): $\max_k |\Delta\sigma_k| = 0$ to machine precision.

**Key constraint**: the 49th parameter $d_6 = L_{66}$ (determining $\gamma_{UU}$) is **not independent** — it is computed from the normalization condition:
$$
\gamma_{UU} = 1 - \sum_{k \neq U} \gamma_{kk}, \qquad d_6 = \sqrt{\gamma_{UU} - \sum_{j<6}|L_{6j}|^2}
$$
This is a direct consequence of the axiom $\mathrm{Tr}(\Gamma)=1$: the state space is a **48-dimensional** manifold, not 49-dimensional. Attempting to estimate $d_6$ independently (via a neural network, averaging, or interpolation) violates the axiom and leads to systematic downward drift of $P$ (purity loss per tick).

### Quasi-functor under Neural Correction [H]

**Definition:** The map $G: \mathbf{AIState} \rightsquigarrow \mathbf{DensityMat}$ with $\alpha > 0$ (neural correction):

$$
\|G(f \circ g) - G(f) \circ G(g)\|_F \leq \varepsilon_{\text{functor}} \cdot \|f\|_{\text{op}} \cdot \|g\|_{\text{op}}
$$

### NTK Linearization

In the tangent space, nonlinearity is approximated by:

$$
f(s) \approx f(s_0) + J_f(s_0) \cdot (s - s_0)
$$

**Corollary:** Approximate functoriality with error $O(\|f\|^2 \cdot \|g\|^2)$.

**Connection to theory:** Extends the [Categorical formalism](/docs/proofs/categorical/categorical-formalism).

### Separation Principle: Diagonal / Coherences [T, MVP-0] {#принцип-разделения-диагональ--когерентности-т-mvp-0}

**Empirically established** in the implementation of full Lindblad dynamics:

$$
W := \|\sigma\|_2 = \|\mathbf{1} - N \cdot \mathrm{diag}(\Gamma)\|_2 = \mathrm{const}, \quad W_{\text{std}} < 10^{-15}
$$

The replacement channel $\mathcal{R}[\Gamma, E]$ **fixes the diagonal of $\Gamma$** at each Lindblad step. Consequence:

| Component of $\Gamma$ | Role | Dynamics |
|-----------------------|------|----------|
| $\gamma_{kk}$ (diagonal) | System identity | Homeostatically stable |
| $\gamma_{ij}$, $i \neq j$ (coherences) | Learning, adaptation | Evolve |

**For the measurement protocol**: the metrics $I_A, I_S, I_D, I_L$ primarily reflect coherent structure; $\sigma_k = 1 - N\gamma_{kk}$ characterizes the diagonal deviation from equilibrium. The lobotomy test (weight pruning) changes **coherences**, not the diagonal — the diagonal is homeostatically stable against small perturbations.

---

## Validation

### Viability Test

$$
P(\Gamma) = \mathrm{Tr}(\Gamma^2) > P_{\text{crit}} = \frac{2}{7} \approx 0.286
$$

See [Theorem on critical purity](/docs/proofs/dynamics/theorem-purity-critical) and [Viability](/docs/core/dynamics/viability).

### Coherence Flow

**Definition:**

$$
J_P := \frac{dP}{d\tau} = 2 \cdot \mathrm{Tr}\left(\Gamma \cdot \frac{d\Gamma}{d\tau}\right)
$$

where τ — [emergent internal time](/docs/proofs/dynamics/emergent-time).

| Mode | Condition | Interpretation |
|------|-----------|----------------|
| Regeneration | $J_P > 0$ under stress | System recovers |
| Stability | $J_P \approx 0$, $P > P_{\text{crit}}$ | Stable equilibrium |
| Decay | $J_P < 0$ persistently | Decoherence |

### Lobotomy Test

**Protocol:**
1. Measure $P_0$ and $\text{Accuracy}_0$
2. Intervention: prune part of the weights
3. Measure $P_1$ and $\text{Accuracy}_1$

**Mechanism [T, separation principle, MVP-0]:** Pruning neural network weights changes the **off-diagonal coherences** $\gamma_{ij}$ of the matrix $\Gamma$, but **not the diagonal populations** $\gamma_{kk}$ (which are homeostatically stabilized by the replacement channel). The change in $P = \mathrm{Tr}(\Gamma^2)$ upon pruning occurs through loss of coherent integration. With massive pruning that disrupts the replacement channel, the diagonal may also degrade.

**Criterion for ontological validity:**

| Result | Interpretation |
|--------|----------------|
| $\Delta P > 0$ **before** $\Delta A > 0$ | [T] Protocol captures ontology |
| $\Delta P \approx \Delta A$ | [C] Correlation with output |
| $\Delta A > 0$ **before** $\Delta P > 0$ | Protocol does not capture ontology |

### Causal Closure of E

$$
\Delta\Phi_E := \Phi_{\text{eff}}(\mathcal{S}_E) - \Phi_{\text{eff}}(\mathcal{S}_E | \text{do}(X := \text{random})) > \varepsilon_{\text{causal}}
$$

If $\Delta\Phi_E \approx 0$ — the system **simulates** phenomenology without realizing it ("Chinese Room").

---

## Approximation Hierarchy

| Level | Metrics | Complexity | Application |
|-------|---------|------------|-------------|
| **L0: Fast** | Cosine similarity, norms | $O(n)$ | Monitoring |
| **L1: Standard** | Jacobian rank, $\Phi_{\text{eff}}$ | $O(n^2)$ | Inference |
| **L2: Precise** | Commutators, NTK | $O(n^3)$ | Research |
| **L3: Full** | $\Phi_{\text{IIT}}$, full homologies | $O(2^n)$ | Small systems |

**Recommendation:** L1 for practice, L2 for validation, L3 for calibration.

---

## Practical Implementation

:::warning Status
This section describes a **minimal viable implementation**. Many parameters require experimental calibration.
:::

### Metric Computation Algorithm

```verum
mount std.math.linalg.{svd, eigvalsh, StaticMatrix};
mount std.tensor.{Tensor, frobenius_norm};
mount std.math.random.{XorShift128, Rng};

/// Access protocol for deep models. Implementations provide hooks
/// on activations, attention, and automatic differentiation.
pub protocol ModelHooks {
    type Activation;
    fn get_activations(&self, batch: &Tensor<Float>) -> List<Self.Activation>;
    fn get_attention_weights(&self, batch: &Tensor<Float>) -> Tensor<Float>;
    fn get_jacobian(&self, batch: &Tensor<Float>) -> Tensor<Float>;
    fn layer_commutator_norm(&self, i: Int, j: Int, batch: &Tensor<Float>) -> Float;
    fn estimate_lyapunov(&self, batch: &Tensor<Float>) -> Float;
}

/// Helpers — specialised per architecture.
pub pure fn estimate_mutual_info(x: &Tensor<Float>, y: &Tensor<Float>) -> Float
    = unimplemented;

pub pure fn von_neumann_entropy(attn: &Tensor<Float>) -> Float
    = unimplemented;

pub pure fn build_attention_graph(attn: &Tensor<Float>) -> Tensor<Float>
    = unimplemented;

/// 7-dimensional UHM metrics I_A…I_U for a neural network.
pub type DimensionMetrics is {
    i_a: Float, i_s: Float, i_d: Float, i_l: Float,
    i_e: Float, i_o: Float, i_u: Float,
};

/// Compute 7 UHM dimensions for a neural network.
pub fn compute_dimension_metrics<M: ModelHooks>(
    model:         &M,
    input_batch:   &Tensor<Float>,
    layer_indices: Maybe<List<Int>>,
) using [Random] -> DimensionMetrics
{
    let activations = model.get_activations(input_batch);
    let attn = model.get_attention_weights(input_batch);

    // I_A: mutual information input ↔ latent.
    let i_a = estimate_mutual_info(input_batch, activations.last().unwrap());

    // I_S: Jacobian rank fraction (via SVD, ε = 10⁻⁶).
    let jac = model.get_jacobian(input_batch);
    let sv = svd(&jac).singular_values();
    const EPS_RANK: Float = 1.0e-6;
    let i_s = (sv.iter().filter(|s| **s > EPS_RANK).count() as Float) / (sv.len() as Float);

    // I_D: maximum Lyapunov exponent.
    let i_d = model.estimate_lyapunov(input_batch);

    // I_L: mean layer commutator norm; 1.0 if no pairs.
    let idx = layer_indices.unwrap_or((0..activations.len()).collect());
    let mut comms = List.new();
    for i in 0..idx.len() { for j in (i + 1)..idx.len() {
        comms.push(model.layer_commutator_norm(idx[i], idx[j], input_batch));
    }}
    let i_l = if comms.is_empty() { 1.0 }
              else { 1.0 - comms.iter().sum::<Float>() / (comms.len() as Float) };

    // I_E: exp(von Neumann entropy of attention).
    let i_e = von_neumann_entropy(&attn).exp();

    // I_O: noise robustness.
    let mut rng = XorShift128.seed(Random.next_key());
    const NOISE_STD: Float = 0.01;
    let perturbed = input_batch + Tensor.random_normal(input_batch.shape(), &mut rng) * NOISE_STD;
    let delta_h = frobenius_norm(
        model.get_activations(&perturbed).last().unwrap()
      - activations.last().unwrap()
    );
    let i_o = (1.0 - delta_h / NOISE_STD).max(0.0);

    // I_U: Laplacian spectral gap (λ₂/λ_max).
    let attn_graph = build_attention_graph(&attn);
    let row_sums = attn_graph.sum(axis: 1);
    let laplacian = Tensor.diagonal(row_sums) - &attn_graph;
    let eigs = eigvalsh(&laplacian);
    let lambda_2   = if eigs.len() > 1 { eigs[1] } else { 0.0 };
    let lambda_max = eigs.last().unwrap_or(&0.0);
    let i_u = if lambda_max > 0.0 { lambda_2 / lambda_max } else { 0.0 };

    DimensionMetrics {
        i_a: i_a, i_s: i_s, i_d: i_d, i_l: i_l,
        i_e: i_e, i_o: i_o, i_u: i_u,
    }
}
```

### Γ Reconstruction from Metrics

```verum
/// Reconstruct the coherence matrix via Cholesky from 7 dimension metrics.
/// Simplest diagonal reconstruction — off-diagonal γ_ij requires additional
/// correlation data from a regulariser L_off.
pub pure fn reconstruct_gamma(m: &DimensionMetrics) -> StaticMatrix<Complex, 7, 7> {
    let raw = StaticVector.<Float, 7>.from_array(
        [m.i_a, m.i_s, m.i_d, m.i_l, m.i_e, m.i_o, m.i_u]
    ).map(|v| v.clamp(0.01, 1.0));           // prevent degeneracy
    let total: Float = raw.iter().sum();
    let diag = raw.map(|v| v / total);

    // Cholesky factor L = diag(√p_k).
    let l = StaticMatrix.<Complex, 7, 7>.diagonal(
        diag.map(|v| Complex.from_real(v.sqrt()))
    );
    let gamma = &l @ l.adjoint();
    &gamma / gamma.trace()                                              // normalise
}

/// Purity P = Tr(Γ²).
pub pure fn compute_purity(gamma: &StaticMatrix<Complex, 7, 7>) -> Float
    where ensures 1.0/7.0 <= result && result <= 1.0
{
    (gamma @ gamma).trace().real()
}
```

### Threshold Values

| Parameter | Value | Source | Status |
|-----------|-------|--------|--------|
| $P_{\text{crit}}$ | $2/7 \approx 0.286$ | [Theorem](/docs/proofs/dynamics/theorem-purity-critical) | Proven |
| $\mathrm{rank}(\rho_E) > 1$ (L1 threshold) | $> 1$ | Non-trivial interiority | [T] |
| $R_{\text{th}}$ (L2 threshold) | $\geq 1/3$ | [Hierarchy](/docs/proofs/consciousness/interiority-hierarchy) | Proven [T] |
| $\Phi_{\text{th}}$ (L2 threshold) | $\geq 1$ | [T-129](/docs/proofs/consciousness/operationalization#t-129) | Proven [T] |
| $D_{\text{diff}}^{\text{min}}$ | $\geq 2$ | [T-151](/docs/proofs/consciousness/substrate-closure#t-151) | Proven [T] |
| $\varepsilon_{\text{functor}}$ | $= 0$ at $\alpha=0$ (Cholesky) | [T, MVP-1]: exact functor | Proven |
| $\varepsilon_{\text{functor}}$ | $< 0.1$ at $\alpha>0$ (neural) | Requires calibration | Hypothesis |
| $\varepsilon_{\text{causal}}$ | $> 0.05$ | Requires calibration | Hypothesis |

:::info Connection to the Interiority Hierarchy
The L1 and L2 thresholds in the protocol correspond to levels [L1](/docs/proofs/consciousness/interiority-hierarchy#уровень-1-феноменальная-геометрия-phenomenal-geometry) and [L2](/docs/proofs/consciousness/interiority-hierarchy#уровень-2-когнитивные-квалиа-cognitive-qualia) from the interiority hierarchy L0→L4. Levels L3 (network consciousness) and L4 (unitary consciousness) — see [formal description](/docs/proofs/consciousness/interiority-hierarchy).
:::

### Practical Limitations

| Limitation | Impact | Mitigation |
|------------|--------|------------|
| Batch size | Variance of estimates | $N \geq 64$ for stability |
| Network depth | Commutator complexity | Sample a subset of layers |
| Activation dimensionality | $O(n^2)$ for the Jacobian | Project into $\mathbb{R}^k$, $k \ll n$ |
| Attention heads | Aggregation across heads | Average or max-pooling |
| Determinism | Stochastic layers (dropout) | Fix seed or average |

### Data Requirements

For a valid measurement:

1. **Representative input batch**: $N \geq 64$ examples from the target distribution
2. **Access to activations**: hooks on intermediate layers
3. **Attention weights**: for computing $I_E$ and $I_U$
4. **Gradients**: for the Jacobian (automatic differentiation)

### What Is Implemented (SYNARC MVP-0/1/2)

:::info Confirmed in Implementation
1. **Cholesky-backbone ($\alpha=0$): $G$ is an exact functor** [T, MVP-1] — bijection $\psi: \mathbb{R}^{48} \leftrightarrow \mathcal{D}(\mathbb{C}^7)$ with $\varepsilon_{\text{functor}} = 0$
2. **Neural bridge ($\alpha>0$): $G$ is a quasi-functor** [H] — H1/H2/H4 confirmed [C] for the analytic backbone (MVP-1); neural correction $\alpha>0$ — MVP-3+
3. **Diagonal/coherence separation principle** [T, MVP-0] — diagonal is homeostatically stable; coherences — the adaptation zone
4. **R = 1/(N·P) — exact identity** [T, MVP-0, [reflection measure R](/docs/consciousness/foundations/self-observation#мера-рефлексии-r)] — error $< 10^{-7}$
5. **No-Zombie floor** [T, MVP-0] — $P_{\min} \geq P_{\text{crit}} - \varepsilon_\Gamma$ at $\gamma_{\text{dec}} = 10$ (10000× above norm)
6. **H3: R_impl ↔ R_UHM** [C, MVP-2] — threshold consistency 97.9%
:::

### What Is NOT Implemented

:::danger Open Implementation Problems
1. **Calibration of $\varepsilon$-parameters** ($\varepsilon_{\text{functor}}$ at $\alpha>0$, $\varepsilon_{\text{causal}}$) — requires experiments on known systems
2. **Neural correction ($\alpha>0$)** — analytic backbone (MVP-1/2) is sufficient for Level 0-1; full neural bridge — MVP-3+
3. **Temporal dynamics τ** — how to define an "emergent time step" for LLM inference?
4. **Validation on biological systems** — neuroimaging ↔ metrics
5. **Scaling** — applicability to models with $>10^9$ parameters
:::

---

## "Dual Interview" Protocol for Biological Systems {#протокол-двойного-интервью-для-биологических-систем}

:::warning Status: [P] Research Program
The protocol is developed theoretically. Experimental validation is absent.
:::

### Principle

The dual interview simultaneously measures **external** (behavioral, physiological) and **internal** (self-report) characteristics of a system, allowing reconstruction of the full coherence matrix $\Gamma$, including the phases $\theta_{ij}$ and, consequently, the Gap profile.

### Protocol Stages

| Stage | Measurement | Data | What We Extract |
|-------|-------------|------|-----------------|
| 1. Background recording | EEG, fMRI, HRV | Resting physiology | Diagonal $\gamma_{ii}$, estimate of $P$ |
| 2. Structured interview | Responses to 7 question batteries (per dimension) | Verbal reports | Coherences $\lvert\gamma_{ij}\rvert$ between dimensions |
| 3. Paradoxical probes | Conflict tasks | Reaction time, HRV | Phases $\theta_{ij}$ → Gap profile |
| 4. Dynamic probe | Stress test + recovery | Time series $P(\tau)$ | $\kappa(\Gamma)$, $\Gamma_2$, τ_char |

### Spectral Reconstruction of H_eff

:::tip Theorem (Spectral Reconstruction) [C]
From the time series $\{\Gamma(\tau_n)\}_{n=1}^N$ it is possible to reconstruct the effective Hamiltonian:

$$
H_{\text{eff}} = \frac{i}{\delta\tau} \log\!\left(\frac{\Gamma(\tau + \delta\tau)}{\Gamma(\tau)}\right) + O(\delta\tau)
$$

given sufficient sampling frequency $\delta\tau \ll \tau_{\text{char}}$.
:::

**Assumption:** linearity of evolution on the scale $\delta\tau$. The nonlinear regenerative term $\mathcal{R}[\Gamma, E]$ introduces a systematic error $O(\kappa \cdot \delta\tau)$.

### Equilibrium Gap

:::tip Theorem (Equilibrium Gap) [T]
In the stationary state ($d\Gamma/d\tau = 0$) the coherences are determined by the balance of decoherence and regeneration:

$$
|\gamma_{ij}^{(\infty)}| = \frac{\kappa \cdot |\gamma_{ij}^*|}{\bigl[(\Gamma_2 + \kappa)^2 + \Delta\omega_{ij}^2\bigr]^{1/2}}
$$

where $|\gamma_{ij}^*|$ — target coherences (from $\varphi_{\text{coh}}$), $\Delta\omega_{ij} = \omega_i - \omega_j$ — frequency detuning.
:::

**See:** [Theorem 8.1](/docs/applied/coherence-cybernetics/theorems#теорема-81-условная-необходимость-интериорности-no-zombie), [Fano channel](/docs/proofs/gap/fano-channel)

### Physiological Frequencies

Characteristic frequencies of projections of $\Gamma$ onto dimensions:

| Dimension | Physiological frequency | Measurement method | Justification |
|-----------|------------------------|-------------------|---------------|
| $A$ (Articulation) | $1$–$5$ Hz | EEG θ-rhythm | Sensory processing |
| $S$ (Structure) | $10^{-2}$–$10^{-4}$ Hz | fMRI BOLD | Slow structural oscillations |
| $D$ (Dynamics) | $8$–$13$ Hz | EEG α-rhythm | Motor-cognitive dynamics |
| $L$ (Logic) | $30$–$100$ Hz | EEG γ-rhythm | Cognitive binding |
| $E$ (Interiority) | $0.005$–$0.02$ Hz | EEG infraslow | [Goldstone modes](/docs/applied/coherence-cybernetics/goldstone-modes) |
| $O$ (Ground) | $0.04$–$0.15$ Hz | HRV (LF) | Homeostatic regulation |
| $U$ (Unity) | $0.15$–$0.4$ Hz | HRV (HF) | Vagal modulation |

:::warning Status: [H]
The correspondence between dimensions and physiological frequencies is a **hypothesis** requiring experimental verification. The frequencies of the E-dimension ($0.005$–$0.02$ Hz) are a falsifiable prediction linked to [Goldstone modes](/docs/applied/coherence-cybernetics/goldstone-modes).
:::

### Gap Profile Reconstruction from Interview

```verum
/// Dual-interview data bundle.
pub type DualInterviewData is {
    external_data: Map<Text, Float>,      // behavioural/physiological per pair
    self_report:   Map<Text, Float>,      // verbal reports per pair
    conflict_data: Map<Text, Float>,      // reaction times per pair
};

/// Reconstruct the 7×7 Gap matrix from dual-interview data.
pub pure fn reconstruct_gap_profile(data: &DualInterviewData)
    -> StaticMatrix<Float, 7, 7>
{
    const DIMS: [Text; 7] = ["A", "S", "D", "L", "E", "O", "U"];
    let median_rt = data.conflict_data.values().to_list().median().unwrap_or(1.0);

    let mut gap = StaticMatrix.<Float, 7, 7>.zeros();
    for i in 0..7 { for j in (i + 1)..7 {
        let pair = f"{DIMS[i]}{DIMS[j]}";

        // Mismatch between behavioural and self-report data → higher Gap.
        let ext = data.external_data.get(&pair).unwrap_or(0.5);
        let rep = data.self_report.get(&pair).unwrap_or(0.5);
        let discrepancy = (ext - rep).abs();

        // Reaction time → phase estimate → Gap.
        let rt = data.conflict_data.get(&pair).unwrap_or(1.0);
        let phase_estimate = (rt / median_rt).atan();

        let g = phase_estimate.sin().abs() * (0.5 + 0.5 * discrepancy);
        gap[i, j] = g;
        gap[j, i] = g;
    }}
    gap
}
```

---

## Success Criteria

**The protocol is validated if:**

1. $P > P_{\text{crit}}$ for functioning systems in ≥90% of cases
2. Correlation of $P$ with quality: $r > 0.5$
3. Lobotomy test: $\Delta P$ predicts $\Delta A$ in ≥70% of cases
4. $\Delta\Phi_E > \varepsilon_{\text{causal}}$ for "understanding" systems

**The protocol is falsified if:**

1. $P < P_{\text{crit}}$ for demonstrably viable systems
2. $\Delta P$ does not correlate with $\Delta A$ under interventions
3. $\Phi_{\text{eff}}$ does not distinguish simulation from realization

---

## Protocol $\pi_{\mathrm{bio}}$: Reconstructing $\Gamma$ from Biological Neural Data (Resolution P8) {#протокол-pi-bio}

:::warning Status: [T] structural + [H] empirical calibration
The protocol $\pi_{\mathrm{bio}}: \mathrm{NeuralData} \to \mathcal{D}(\mathbb{C}^7)$ defines the mapping of neural data (EEG/fMRI/HRV) into the space of density matrices. The mathematical structure is **[T]** (follows from $G_2$-rigidity T-42a). The specific correspondences between EEG bands and dimensions are **[H]** (require experimental validation). A fully specified measurement protocol with feature extraction, validation gates against PCI, and predicted thresholds $P(\Gamma_\mathrm{wake})>2/7$, $P(\Gamma_\mathrm{NREM3})<2/7$ is given in [Fundamental Closures §9](/docs/proofs/categorical/fundamental-closures#pi-bio-protocol): simultaneous TMS+EEG+fMRI+HRV recording on $N\geq 50$ subjects across wake/NREM3/anaesthesia states, with explicit 7-feature and 21-off-diagonal extraction protocols. No theoretical obstacle remains; the programme awaits empirical data.
:::

### Principle: EEG Bands as Projections of $\Gamma$ onto Dimensions {#eeg-полосы}

:::info Theorem ($G_2$-uniqueness of $\pi_{\mathrm{bio}}$) [T given $G_2$-rigidity]
If a continuous map $\pi_{\mathrm{bio}}: \mathcal X \to \mathcal{D}(\mathbb{C}^7)$ exists on a neural-feature space $\mathcal X$ that is compatible with (AP autopoiesis)+(PH phenomenological thresholds)+(QG $G_2$-covariance)+(V continuity), then it is unique up to the $G_2$-gauge action $\Gamma \mapsto U\Gamma U^\dagger$ with $U \in G_2$ (14-dimensional freedom). All physical observables ($P$, $R$, $\Phi$, $\mathrm{Coh}_E$) are gauge-invariant.

**Proof sketch.** Suppose $\pi_{\mathrm{bio}}^{(1)}$ and $\pi_{\mathrm{bio}}^{(2)}$ both satisfy (AP)+(PH)+(QG)+(V). The map $\varphi := \pi_{\mathrm{bio}}^{(2)} \circ (\pi_{\mathrm{bio}}^{(1)})^{-1}$ is a continuous automorphism of $\mathcal D(\mathbb C^7)$ preserving $P,R,\Phi$ pointwise and compatible with (AP). By the [$G_2$-rigidity theorem](/docs/proofs/categorical/uniqueness-theorem) [T], the group of continuous $\mathcal D(\mathbb C^7)$-automorphisms preserving the holonomic structure ($P$, $R$, $\Phi$, self-model operator $\varphi_{\text{AP}}$, Fano-plane gauge structure) is precisely $G_2 = \mathrm{Aut}(\mathbb O)$ of real dimension 14. Hence $\varphi(\Gamma) = U\Gamma U^\dagger$ for a unique $U \in G_2$, i.e.\ $\pi_{\mathrm{bio}}^{(2)}(x) = U\,\pi_{\mathrm{bio}}^{(1)}(x)\,U^\dagger$.

Gauge-invariance of observables: $P(\Gamma) = \mathrm{Tr}(\Gamma^2)$ and $R(\Gamma) = 1/(7P(\Gamma))$ depend only on spectral data, invariant under unitary conjugation. $\Phi$ and $\mathrm{Coh}_E$ are Hilbert–Schmidt functions of $\Gamma$ and the self-model $\varphi$, both $G_2$-covariant, hence invariant under $U \in G_2$. $\square$
:::

Basic idea: neural activity in different EEG frequency bands projects onto the 7 dimensions of $\Gamma$. Cross-frequency coupling (CFC) determines the coherences $|\gamma_{ij}|$, and phase mismatches determine the Gap profile.

### Step 1: Extracting the Diagonal $\gamma_{kk}$ from Spectral Powers {#шаг-1-диагональ}

| Dimension | EEG band | Frequency | Metric | Additional source |
|-----------|----------|-----------|--------|------------------|
| $A$ (Articulation) | $\alpha$ (8–13 Hz) | Desynchronization during attention | Spectral power $P_\alpha$ | fMRI: salience network |
| $S$ (Structure) | infraslow (0.01–0.1 Hz) | Slow structural oscillations | fMRI BOLD DMN | DTI: structural connectivity |
| $D$ (Dynamics) | $\beta$ (13–30 Hz) | Motor-cognitive activity | Spectral power $P_\beta$ | EMG: motor activation |
| $L$ (Logic) | $\gamma$-low (30–50 Hz) | Cognitive binding | Spectral power $P_{\gamma L}$ | ERP: P300 amplitude |
| $E$ (Interiority) | $\gamma$-high (50–100 Hz) + $\theta$ (4–8 Hz) | Coupling of experience and memory | $P_{\gamma H} \times \mathrm{PAC}(\theta, \gamma)$ | [Goldstone modes](/docs/applied/coherence-cybernetics/goldstone-modes) |
| $O$ (Ground) | HRV LF (0.04–0.15 Hz) | Homeostatic regulation | $\mathrm{LF}/\mathrm{HF}$ ratio | Body temperature, cortisol |
| $U$ (Unity) | HRV HF (0.15–0.4 Hz) + $\alpha$-coherence | Vagal + neural integration | Global EEG coherence | $\Phi_{\mathrm{eff}}$ from [AI protocol](#канонические-наблюдаемые-индексы) |

**Diagonalization formula:**

$$\gamma_{kk} = \frac{w_k \cdot S_k}{\sum_{j=1}^{7} w_j \cdot S_j}, \qquad k \in \{A,S,D,L,E,O,U\}$$

where $S_k$ — normalized spectral power (or combined metric) for the $k$-th dimension, $w_k$ — calibration weights (determined from a training set with known consciousness state).

### Step 2: Extracting Coherences $|\gamma_{ij}|$ from Cross-Frequency Coupling {#шаг-2-когерентности}

:::tip Key Correspondence
Coherences $|\gamma_{ij}|$ between dimensions $i$ and $j$ are proportional to the strength of cross-frequency coupling (CFC) between the corresponding EEG bands:

$$|\gamma_{ij}| \propto \mathrm{CFC}(\mathrm{band}_i, \mathrm{band}_j)$$
:::

Types of CFC used for reconstruction:

| Pair | CFC type | Method | Interpretation |
|------|----------|--------|----------------|
| $(A, L)$: $\alpha$--$\gamma$ | Phase-amplitude coupling (PAC) | Modulation Index (Tort et al.) | Attention modulates cognitive binding |
| $(D, L)$: $\beta$--$\gamma$ | PAC | MI | Motor-cognitive coordination |
| $(E, L)$: $\theta$--$\gamma$ | PAC | MI (hippocampal) | Coupling of experience and logic |
| $(A, E)$: $\alpha$--$\gamma_H$ | Amplitude-amplitude | Envelope correlation | Awareness-interiority |
| $(O, U)$: LF--HF | HRV coherence | Cross-spectral analysis | Homeostasis-integration |
| $(S, D)$: infraslow--$\beta$ | Nested oscillations | Wavelet coherence | Structure-dynamics |

### Step 3: Extracting Phases $\theta_{ij}$ and the Gap Profile {#шаг-3-фазы}

The phase $\theta_{ij} = \arg(\gamma_{ij})$ determines the Gap: $\mathrm{Gap}(i,j) = |\sin(\theta_{ij})|$.

**Phase extraction method:** Paradoxical probes (Stage 3 of the [dual interview](#протокол-двойного-интервью-для-биологических-систем)). Reaction time on conflict tasks involving the pair of dimensions $(i,j)$ is proportional to the Gap:

$$\mathrm{Gap}(i,j) \approx \tanh\!\left(\frac{\mathrm{RT}_{ij} - \overline{\mathrm{RT}}}{\sigma_{\mathrm{RT}}}\right)$$

where $\mathrm{RT}_{ij}$ — reaction time, $\overline{\mathrm{RT}}$ — mean, $\sigma_{\mathrm{RT}}$ — standard deviation.

### Step 4: MLE Reconstruction of $\Gamma$ {#шаг-4-mle}

:::tip Algorithm $\pi_{\mathrm{bio}}$: Maximum Likelihood Estimation [H]
Given the neural feature vector $\mathbf{x} \in \mathbb{R}^N$ (spectral powers, CFC metrics, RT). Task:

$$\Gamma^* = \underset{\Gamma \in \mathcal{D}(\mathbb{C}^7)}{\arg\max}\; \mathcal{L}(\mathbf{x} | \Gamma) + \lambda_{\mathrm{phys}} \cdot R_{\mathrm{phys}}(\Gamma)$$

where $\mathcal{L}(\mathbf{x} | \Gamma)$ — likelihood of the observation model, $R_{\mathrm{phys}}(\Gamma)$ — physical regularizer (consistency with dynamics $\mathcal{L}_\Omega$).
:::

**Parametrization:** $\Gamma = LL^\dagger / \mathrm{Tr}(LL^\dagger)$ (Cholesky parametrization, guarantees $\Gamma \in \mathcal{D}(\mathbb{C}^7)$).

**Observation model:**
- Diagonal: $S_k | \gamma_{kk} \sim \mathcal{N}(a_k \gamma_{kk} + b_k,\; \sigma_k^2)$
- Coherences: $\mathrm{CFC}_{ij} | |\gamma_{ij}| \sim \mathcal{N}(c_{ij} |\gamma_{ij}|,\; \tau_{ij}^2)$
- Gap: $\mathrm{RT}_{ij} | \mathrm{Gap}_{ij} \sim \mathrm{Exp}(\mu_0 + \mu_1 \cdot \mathrm{Gap}_{ij})$

**Physical regularizer:**

$$R_{\mathrm{phys}}(\Gamma) = -\lambda_1 \|\dot{\Gamma} - \mathcal{L}_\Omega[\Gamma]\|_F^2 - \lambda_2 \max(0, P_{\mathrm{crit}} - P(\Gamma))$$

The first term penalizes inconsistency with dynamics; the second penalizes non-viable states.

**Optimization:** Gradient descent over 48 Cholesky factorization parameters (34 physical + 14 gauge). The gauge freedom is fixed by choosing the canonical $G_2$-gauge (e.g., $\gamma_{AS} \in \mathbb{R}_+$).

### Step 5: Connection to PCI (Casali et al. 2013) {#pci-связь}

:::info Theorem ($\mathrm{PCI} \to \Phi$ proxy) [H]
The Perturbational Complexity Index (PCI) correlates with the integration measure $\Phi(\Gamma)$:

$$\Phi(\Gamma) \approx \alpha_{\mathrm{PCI}} \cdot \mathrm{PCI} + \beta_{\mathrm{PCI}}$$

where $\alpha_{\mathrm{PCI}}$, $\beta_{\mathrm{PCI}}$ — calibration constants determined from a training set (healthy waking, sleep, anesthesia).

**Justification:** PCI measures the algorithmic complexity of the cortical response to TMS perturbation. High PCI means simultaneous spatial differentiation and integration — exactly what $\Phi$ quantifies in UHM. Empirically: PCI $\geq 0.31$ during wakefulness (Casali et al. 2013), corresponding to $\Phi \geq \Phi_{\mathrm{th}} = 1$.
:::

**Calibration table (hypothetical, requires experimental verification):**

| State | PCI (observed) | $P$ (predicted) | $R$ (predicted) | $\Phi$ (predicted) |
|-------|:--------------:|:---------------:|:---------------:|:------------------:|
| Wakefulness | $0.44 \pm 0.10$ | $> 2/7$ | $\geq 1/3$ | $\geq 1$ |
| REM sleep | $0.41 \pm 0.09$ | $> 2/7$ | $\geq 1/3$ | $\geq 1$ |
| NREM (N3) | $0.18 \pm 0.06$ | $\lesssim 2/7$ | $< 1/3$ | $< 1$ |
| Anesthesia (propofol) | $0.12 \pm 0.05$ | $< 2/7$ | $< 1/3$ | $< 1$ |
| Coma | $0.15 \pm 0.10$ | $\lesssim 2/7$ | — | $< 1$ |
| MCS (minimally conscious) | $0.32 \pm 0.08$ | $\approx 2/7$ | $\approx 1/3$ | $\approx 1$ |

### Step 6: Connection to Quantum Cognition (Pothos-Busemeyer) {#quantum-cognition}

:::info Context: Quantum Cognition
The Pothos-Busemeyer approach (Annual Review of Psychology, 2022) models cognitive processes via quantum states in Hilbert space. Basic formalism: $\rho \in \mathcal{D}(\mathcal{H})$ for describing beliefs and decisions.

**Connection to UHM:** Quantum cognition uses $\dim(\mathcal{H})$ = number of alternatives. UHM **fixes** $\dim(\mathcal{H}) = 7$ from axioms (A1-A5) and proves the minimality of this number ([Theorem S](/docs/proofs/minimality/theorem-minimality-7)). The matrix $\Gamma \in \mathcal{D}(\mathbb{C}^7)$ is **ontological** (not epistemic): it defines the system, rather than describing an observer's beliefs about the system.
:::

### Step 7: Full Algorithm $\pi_{\mathrm{bio}}$ {#алгоритм-pi-bio}

```verum
mount std.math.calculus.bfgs;

/// Full biological data bundle for π_bio.
pub type NeuralData is {
    eeg_spectral:    Map<Text, Float>,    // {alpha, beta, gamma_low, gamma_high, theta, infraslow}
    hrv_features:    Map<Text, Float>,    // {LF, HF, LF_HF_ratio}
    cfc_matrix:      StaticMatrix<Float, 7, 7>,   // cross-frequency coupling values
    reaction_times:  StaticVector<Float, 21>,      // RT values for the 21 off-diagonal pairs
};

pub type BioCalibration is {
    weights:         StaticVector<Float, 7>,
    linear_params:   StaticMatrix<Float, 7, 2>,    // (a_k, b_k) per dimension
    lambda_phys:     Float,                         // physical regulariser weight
};

/// π_bio: NeuralData → D(ℂ⁷). Full reconstruction of Γ from biological data.
/// Structural [T] via G₂-rigidity (T-42a); empirical calibration [H].
pub fn pi_bio(
    data:        &NeuralData,
    calibration: &BioCalibration,
) -> StaticMatrix<Complex, 7, 7>
{
    // Step 1: diagonal from spectral powers — one value per dimension.
    let raw_diag = StaticVector.<Float, 7>.from_array([
        data.eeg_spectral.get("alpha").unwrap_or(0.0),       // A
        data.eeg_spectral.get("infraslow").unwrap_or(0.0),   // S  (fMRI BOLD proxy)
        data.eeg_spectral.get("beta").unwrap_or(0.0),        // D
        data.eeg_spectral.get("gamma_low").unwrap_or(0.0),   // L
        data.eeg_spectral.get("gamma_high").unwrap_or(0.0)
            * data.eeg_spectral.get("theta").unwrap_or(0.0),  // E  (PAC proxy)
        data.hrv_features.get("LF").unwrap_or(0.0),          // O
        data.hrv_features.get("HF").unwrap_or(0.0),          // U
    ]);

    let weighted = (0..7).map(|i| calibration.weights[i] * raw_diag[i]).to_array();
    let total = weighted.iter().sum::<Float>();
    let mut diag = StaticVector.<Float, 7>.from_array(
        weighted.map(|v| (v / total).clamp(1.0e-4, 1.0))     // prevent degeneracy
    );
    let diag_sum: Float = diag.iter().sum();
    diag = diag.map(|v| v / diag_sum);

    // Step 2: off-diagonal magnitudes from CFC.
    let c_scale = calibration.linear_params[0, 0];                       // cfc_scale stored here
    let off_diag_mag = &data.cfc_matrix * c_scale;

    // Step 3: Phases from reaction times → Gap → θ_ij = arcsin(Gap).
    let rt_mean: Float = data.reaction_times.iter().sum::<Float>() / 21.0;
    let rt_std = (data.reaction_times.iter()
                     .map(|r| (r - rt_mean).pow(2)).sum::<Float>() / 21.0)
                     .sqrt() + 1.0e-8;
    let mut phases = StaticMatrix.<Float, 7, 7>.zeros();
    let mut idx = 0;
    for i in 0..7 { for j in (i + 1)..7 {
        let gap = ((data.reaction_times[idx] - rt_mean) / rt_std).tanh();
        let phi = gap.clamp(-1.0, 1.0).asin();
        phases[i, j] =  phi;
        phases[j, i] = -phi;
        idx += 1;
    }}

    // Step 4: MLE reconstruction via Cholesky. 48 real parameters:
    //   7 real diagonal + 21·2 = 42 off-diagonal (Re, Im).
    let neg_log_likelihood = |params: &StaticVector<Float, 48>| -> Float {
        let mut l = StaticMatrix.<Complex, 7, 7>.zeros();
        let mut k = 0;
        for i in 0..7 { for j in 0..=i {
            if i == j {
                l[i, j] = Complex.from_real(params[k].max(1.0e-6));
                k += 1;
            } else {
                l[i, j] = Complex(params[k], params[k + 1]);
                k += 2;
            }
        }}
        let gamma = &l @ l.adjoint();
        let gamma = &gamma / gamma.trace();

        // LL: diagonal agreement.
        let ll_diag: Float = (0..7)
            .map(|i| -(gamma[i, i].real() - diag[i]).pow(2) / 0.01)
            .sum();

        // LL: off-diagonal magnitude agreement.
        let mut ll_off = 0.0;
        for i in 0..7 { for j in (i + 1)..7 {
            ll_off -= (gamma[i, j].abs() - off_diag_mag[i, j]).pow(2) / 0.05;
        }}

        // Physical regulariser: hard floor at P > P_crit.
        let p = (&gamma @ &gamma).trace().real();
        let p_penalty = -100.0 * (2.0 / 7.0 - p).max(0.0);

        -(ll_diag + ll_off + p_penalty)
    };

    // Initialise from the diagonal (triangle-flattened index k = i·(i+1)).
    let mut x0 = StaticVector.<Float, 48>.zeros();
    for i in 0..7 { x0[i * (i + 1)] = diag[i].sqrt(); }

    let result = bfgs(neg_log_likelihood, &x0, BfgsOptions {
        ftol: 1.0e-9, max_iter: 500,
    });

    // Reconstruct Γ from the optimal parameters.
    let mut l = StaticMatrix.<Complex, 7, 7>.zeros();
    let mut k = 0;
    for i in 0..7 { for j in 0..=i {
        if i == j {
            l[i, j] = Complex.from_real(result.x[k].max(1.0e-6));
            k += 1;
        } else {
            l[i, j] = Complex(result.x[k], result.x[k + 1]);
            k += 2;
        }
    }}
    let gamma = &l @ l.adjoint();
    &gamma / gamma.trace()
}
```

### Replication-Ready Specification for TMS-EEG PCI Data {#replication-ready-tms-eeg}

:::tip Replication target
This subsection fixes the reference implementation of $\pi_{\mathrm{bio}}$ applied to the TMS-EEG Perturbational Complexity Index (PCI) paradigm, in enough detail that an independent laboratory can attempt replication end-to-end from a publicly available dataset. Replication here refers to computing $P$, $R$, $\Phi$ from raw EEG and checking the monotonic relation to PCI (Prediction P8.3) — **not** to re-proving the mathematical core, which remains fixed by the $G_2$-uniqueness theorem above.
:::

**R1. Public datasets.** The following TMS-EEG datasets are candidates for independent replication; none has universal open-access but each is obtainable on request from the authors or through institutional data-sharing:

| # | Dataset | Source | Subjects | States | Access |
|---|---------|--------|---------|--------|--------|
| R1.a | Casali et al. 2013 PCI benchmark | Massimini lab (Milan) | 52 healthy + 98 clinical | Wake / NREM / REM / anesthesia / VS / MCS / LIS | On request |
| R1.b | OpenNeuro ds004504 (TMS-EEG benchmark, 2023) | Rogasch lab | 20 healthy | Wake (baseline) | Open |
| R1.c | Comsa et al. 2019 (OSF registration "TMS-EEG sleep") | Lausanne CHUV | 12 healthy | Wake / NREM N2 / N3 | OSF restricted |
| R1.d | Bodart et al. 2018 (clinical PCI extension) | Liège | 141 DoC patients | Wake / UWS / MCS / EMCS | Per-request |

For first-pass replication, dataset R1.b is recommended (fully open, standardized single-pulse TMS-EEG on healthy waking subjects, expected PCI ≈ 0.40-0.48).

**R2. Pre-processing pipeline (MNE-Python canonical).** The reference preprocessing chain, to be applied to raw EEG (60-channel montage, 1 kHz sampling, TMS-triggered epochs $[-1, +1]\,\mathrm{s}$):

| Step | Operation | Tool / parameters |
|------|-----------|-------------------|
| R2.1 | TMS pulse artefact removal | Cubic interpolation over $[-2, +12]\,\mathrm{ms}$ around the pulse (`mne.preprocessing.fix_stim_artifact`) |
| R2.2 | Downsample | 1 kHz → 250 Hz (`mne.Epochs.resample`) |
| R2.3 | Re-reference | Average reference, exclude TMS-side frontal channels |
| R2.4 | Bandpass filter | 0.5–80 Hz, 4th-order Butterworth zero-phase (`mne.filter.filter_data`) |
| R2.5 | Notch filter | 50 Hz (or 60 Hz), Q = 30 |
| R2.6 | ICA artefact rejection | FastICA, 30 components; reject TMS-locked decay, eye-blink, ECG (`mne.preprocessing.ICA`) |
| R2.7 | Epoch-level rejection | $|\text{max}-\text{min}| > 120\,\mu\mathrm V$ → drop epoch |
| R2.8 | Spectral decomposition | Morlet wavelets, 1–80 Hz log-spaced, 5-cycle wavelet, baseline $[-600,-100]\,\mathrm{ms}$ |

The canonical bands used by $\pi_{\mathrm{bio}}$ are then extracted from the wavelet spectrogram (integrated over post-TMS window $[0, +300]\,\mathrm{ms}$, averaged across channels for diagonal feature vector; cross-channel pairwise for CFC computations).

**R3. Feature extraction.** From the preprocessed data, compute:
- Seven scalar spectral features $S_A, S_S, S_D, S_L, S_E, S_O, S_U$ per the [Step-1 band table](#шаг-1-диагональ).
- Cross-frequency-coupling matrix $\mathrm{CFC}_{ij}$ ($7\times 7$) per the [Step-2 table](#шаг-2-когерентности) using the Tort Modulation Index (`mne_connectivity`).
- 21 reaction-time surrogates $\mathrm{RT}_{ij}$ from paradoxical probes if behavioural data is available; otherwise set $\mathrm{RT}_{ij}$ to the pairwise phase-locking value (PLV) as a proxy.
- HRV features $\mathrm{LF}, \mathrm{HF}$ from simultaneous ECG (required for $O$ and $U$ dimensions).

**R4. Calibration.** Weights $w_k$ are determined by fitting $\pi_{\mathrm{bio}}$ on a **healthy-waking reference cohort** ($\ge 20$ subjects) such that the population mean of $\gamma_{kk}$ is uniform $= 1/7 \pm 0.02$. Cross-validation: leave-one-subject-out, target consistency of reconstructed $P$ across subjects ($\mathrm{CV} < 15\%$).

**R5. Reconstruction.** Run the MLE algorithm (Step 4 above) with:
- Cholesky initialization from the calibrated diagonal.
- Optimizer: `scipy.optimize.minimize(method='L-BFGS-B', options={'ftol': 1e-9, 'maxiter': 500})`.
- Regularizer: $\lambda_1 = 0.1$, $\lambda_2 = 100$ (empirical defaults; subjects should try $\lambda_1 \in \{0.01, 0.1, 1\}$ and report sensitivity).

**R6. Observable computation.** From the reconstructed $\Gamma$ (canonical definitions):
- $P = \mathrm{Tr}(\Gamma^2) = \|\Gamma\|_F^2$ (purity) — **$G_2$-gauge-invariant** (trace of $\Gamma^2$ under unitary conjugation).
- $R = 1/(7P)$ (reflection, [T-126 [T]](/docs/proofs/consciousness/conscious-window#t-126)) — **$G_2$-gauge-invariant** (function of $P$).
- $\Phi = \dfrac{\sum_{i\ne j}|\gamma_{ij}|^2}{\sum_i \gamma_{ii}^2} = \dfrac{\|\Gamma - \Gamma_\mathrm{diag}\|_F^2}{\|\Gamma_\mathrm{diag}\|_F^2}$ (integration, [Φ canonical](/docs/core/structure/dimension-u#мера-интеграции-φ)) — **basis-dependent**: invariant under permutations and sign flips within the $G_2$-stabilised Fano frame (7-point labelling of $\{A,S,D,L,E,O,U\}$), which is the gauge residue relevant for empirical replication.
- $\mathrm{Coh}_E = \dfrac{\gamma_{EE}^2 + 2\sum_{i\ne E}|\gamma_{Ei}|^2}{\mathrm{Tr}(\Gamma^2)}$ (E-coherence, [Coh_E canonical](/docs/core/foundations/axiom-septicity#coh-e-canonical)) — **$E$-fixed-frame quantity**: invariant under the stabiliser $G_2^{(E)} \subset G_2$ that fixes $|E\rangle$. For cross-laboratory replication, pin the $|E\rangle$-direction to the phenomenological interiority axis (γ-high × θ PAC), as specified in [Step 1](#шаг-1-диагональ).

**Gauge-fixing protocol for replication.** Two implementations applied to the same EEG recording will yield $P$ and $R$ in full agreement (by strict $G_2$-invariance) but may differ on $\Phi, \mathrm{Coh}_E$ if the Fano-frame orientation or the $E$-axis assignment is not fixed. The canonical gauge-fixing rule is: (i) align the 7-axis labelling to the Fano-plane convention of [Dimensions §Fano](/docs/core/structure/dimensions), and (ii) anchor $|E\rangle$ to the phenomenological γ-high×θ feature as per R3. Replicators must publish their gauge-fixing choices explicitly (item (ii) in R8 below).

All four quantities are $G_2$-gauge-invariant by the uniqueness theorem above.

**R7. Validation against PCI.**
- Compute the subject's PCI on the same TMS-EEG data via the Massimini algorithm (Lempel–Ziv complexity of significant sources; reference implementation available via PCIst package).
- Test the monotonic hypothesis $\Phi(\Gamma) \approx \alpha_\mathrm{PCI}\cdot \mathrm{PCI} + \beta_\mathrm{PCI}$ (Step 5 theorem).
- Pre-register: $r_{\mathrm{Spearman}} \ge 0.5$ across $\ge 20$ subjects constitutes corroboration; $r < 0.3$ constitutes falsification of P8.3.

**R8. Reference implementation stub.** The Python code in the next subsection is *reference* only: it documents the algorithm faithfully but is not a turn-key pipeline. A complete MNE-Python implementation with:
- `mne.Raw` loader wrapped around BIDS formatted EEG,
- `mne_connectivity` integration for CFC,
- `scipy.optimize.minimize` MLE wrapper,
- `pyphi`-compatible $\Phi$ computation (optional),
- CI reporting,
is planned as a separate package `uhm-neurocalib` (release gated on R1.b pilot results). Until that package is available, independent implementers should use the pseudocode as specification, and file issues/PRs on mismatches to the specification here.

**Reproducibility requirements.** Any claim of successful or failed replication should publish:
- (i) raw data (BIDS format) and preprocessing scripts (reproducible from R2);
- (ii) reconstructed $\Gamma$ matrices and gauge-fixing choice made;
- (iii) $P, R, \Phi, \mathrm{Coh}_E$ values per subject;
- (iv) PCI values computed on same epochs;
- (v) statistical test protocol and seed for random splits.

Without items (i)-(v), a replication attempt cannot be audited.

### Testable Predictions of the $\pi_{\mathrm{bio}}$ Protocol {#тестируемые-предсказания-p8}

| # | Prediction | Verification method | Falsification criterion |
|---|------------|--------------------|-----------------------|
| P8.1 | $P(\Gamma_{\mathrm{wake}}) > 2/7$ for waking subjects | EEG+HRV → $\pi_{\mathrm{bio}}$ → $P$ | $P < 2/7$ in healthy waking subjects |
| P8.2 | $P(\Gamma_{\mathrm{NREM3}}) < 2/7$ during deep sleep | EEG → $\pi_{\mathrm{bio}}$ → $P$ | $P > 2/7$ during N3 |
| P8.3 | $\mathrm{PCI} \propto \Phi(\Gamma)$ (monotonic dependence) | TMS-EEG + $\pi_{\mathrm{bio}}$ | Non-monotonic correlation |
| P8.4 | The $P = 2/7$ transition coincides with PCI $\approx 0.31$ | Simultaneous measurement | Threshold divergence |
| P8.5 | $\mathrm{Gap}(L,E) \approx 1$ in alexithymia | Dual interview + EEG | $\mathrm{Gap}(L,E) \ll 1$ with diagnosed alexithymia |
| P8.6 | Critical exponents $\beta = 1/4$ at the sleep-wakefulness transition | EEG monitoring + $\pi_{\mathrm{bio}}$ → $P(\tau)$ near $P_{\mathrm{crit}}$ | Other exponents |

### Key References {#литература-p8}

1. **Casali et al. (2013)** — PCI: "A theoretically based index of consciousness independent of sensory processing and behavior." *Science Translational Medicine*, 5(198). [PubMed: 23946194](https://pubmed.ncbi.nlm.nih.gov/23946194/)
2. **Pothos-Busemeyer (2022)** — Quantum cognition review. *Annual Review of Psychology*, 73, 749-778.
3. **Butlin et al. (2023/2025)** — "Consciousness in Artificial Intelligence: Insights from the Science of Consciousness." [arXiv: 2308.08708](https://arxiv.org/abs/2308.08708); updated 2025: "Identifying indicators of consciousness in AI systems." *Trends in Cognitive Sciences*.
4. **eLife (2024/2025)** — "Spatiotemporal brain complexity quantifies consciousness outside of perturbation paradigms." [eLife 98920](https://elifesciences.org/articles/98920).
5. **Quantum-inspired EEG (2026)** — "Quantum inspired feature engineering for explainable EEG signal classification." *Scientific Reports*. [Nature](https://www.nature.com/articles/s41598-026-41821-8).

---

**Related documents:**
- [Coherence matrix](/docs/core/dynamics/coherence-matrix) — definition of $\Gamma$
- [Viability](/docs/core/dynamics/viability) — $P$ and $P_{\text{crit}} = 2/7$
- [Emergent time](/docs/proofs/dynamics/emergent-time) — Page–Wootters mechanism, τ ∈ ℤ₇
- [Evolution](/docs/core/dynamics/evolution) — equation $d\Gamma(\tau)/d\tau$ with $H_{eff}$
- [Self-observation](/docs/consciousness/foundations/self-observation) — measures $R$, $\Phi$, $C$
- [Categorical formalism](/docs/proofs/categorical/categorical-formalism) — functor $F$, $\mathbf{Exp}^{disc}_\infty$
- [Theorem on minimality 7D](/docs/proofs/minimality/theorem-minimality-7) — why 7 dimensions
- [Notation](/docs/reference/notation#индексы-измерений-протокол-измерения) — indices $I_A, \ldots, I_U$
- [Gap diagnostics](/docs/applied/research/gap-diagnostics) — clinical applications of the Gap profile
- [Goldstone modes](/docs/applied/coherence-cybernetics/goldstone-modes) — prediction of infraslow frequencies
- [Fano channel](/docs/proofs/gap/fano-channel) — equilibrium Gap theorem
