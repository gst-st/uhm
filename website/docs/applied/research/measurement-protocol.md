---
sidebar_position: 3
title: Протокол измерения Γ
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

```python
import numpy as np
import itertools


# ---------------------------------------------------------------------------
# Helper functions (stubs — require implementation)
# ---------------------------------------------------------------------------

def estimate_mutual_info(x: np.ndarray, y: np.ndarray) -> float:
    """Mutual information I(x;y). Requires implementation for the specific architecture."""
    raise NotImplementedError


def compute_jacobian(model, input_batch: np.ndarray) -> np.ndarray:
    """Model Jacobian ∂f/∂x. Requires implementation for the specific architecture."""
    raise NotImplementedError


def estimate_lyapunov(model, input_batch: np.ndarray) -> float:
    """Maximum Lyapunov exponent. Requires implementation for the specific architecture."""
    raise NotImplementedError


def layer_commutator_norm(
    model, i: int, j: int, input_batch: np.ndarray
) -> float:
    """Layer commutator norm ||[f_i, f_j]||. Requires implementation for the specific architecture."""
    raise NotImplementedError


def von_neumann_entropy(attention_weights: np.ndarray) -> float:
    """Von Neumann entropy S_vN(ρ). Requires implementation for the specific architecture."""
    raise NotImplementedError


def build_attention_graph(attention_weights: np.ndarray) -> np.ndarray:
    """Attention graph from attention weights. Requires implementation for the specific architecture."""
    raise NotImplementedError


# ---------------------------------------------------------------------------


def compute_dimension_metrics(
    model,
    input_batch: np.ndarray,
    layer_indices: list[int] = None
) -> dict[str, float]:
    """
    Compute 7 UHM dimensions for a neural network.

    Args:
        model: Model with access to intermediate activations
        input_batch: Input data batch (N, ...)
        layer_indices: Layer indices for analysis (default — all)

    Returns:
        dict with keys I_A, I_S, I_D, I_L, I_E, I_O, I_U
    """
    activations = model.get_activations(input_batch)
    attention_weights = model.get_attention_weights(input_batch)

    # I_A: Mutual information input↔latent
    I_A = estimate_mutual_info(input_batch, activations[-1])

    # I_S: Jacobian rank (via SVD)
    jacobian = compute_jacobian(model, input_batch)
    singular_values = np.linalg.svd(jacobian, compute_uv=False)
    eps_rank = 1e-6
    I_S = np.sum(singular_values > eps_rank) / len(singular_values)

    # I_D: Maximum Lyapunov exponent (estimate)
    I_D = estimate_lyapunov(model, input_batch)

    # I_L: Layer commutators
    commutator_norms = []
    for i, j in itertools.combinations(layer_indices or range(len(activations)), 2):
        comm_norm = layer_commutator_norm(model, i, j, input_batch)
        commutator_norms.append(comm_norm)
    I_L = 1.0 - np.mean(commutator_norms) if commutator_norms else 1.0

    # I_E: Differentiation (attention entropy exponent)
    attn_entropy = von_neumann_entropy(attention_weights)
    I_E = np.exp(attn_entropy)

    # I_O: Noise robustness
    noise_std = 0.01
    perturbed = input_batch + np.random.randn(*input_batch.shape) * noise_std
    delta_h = np.linalg.norm(
        model.get_activations(perturbed)[-1] - activations[-1],
        'fro'
    )
    I_O = max(0, 1.0 - delta_h / noise_std)

    # I_U: Effective Φ (Laplacian spectral gap)
    attn_graph = build_attention_graph(attention_weights)
    laplacian = np.diag(attn_graph.sum(axis=1)) - attn_graph
    eigenvalues = np.linalg.eigvalsh(laplacian)
    lambda_2 = eigenvalues[1] if len(eigenvalues) > 1 else 0
    lambda_max = eigenvalues[-1]
    I_U = lambda_2 / lambda_max if lambda_max > 0 else 0

    return {
        'I_A': I_A, 'I_S': I_S, 'I_D': I_D, 'I_L': I_L,
        'I_E': I_E, 'I_O': I_O, 'I_U': I_U
    }
```

### Γ Reconstruction from Metrics

```python
def reconstruct_gamma(metrics: dict[str, float]) -> np.ndarray:
    """
    Reconstruction of the coherence matrix via Cholesky.

    Returns a 7×7 density matrix.
    """
    # Diagonal elements — normalized metrics
    I_vec = np.array([
        metrics['I_A'], metrics['I_S'], metrics['I_D'],
        metrics['I_L'], metrics['I_E'], metrics['I_O'], metrics['I_U']
    ])
    I_vec = np.clip(I_vec, 0.01, 1.0)  # Prevent degeneracy
    diag = I_vec / I_vec.sum()

    # Initial Cholesky factorization
    L = np.diag(np.sqrt(diag))

    # Regularization (minimize off-diagonal)
    # Simplest case — diagonal matrix
    # Simplest diagonal reconstruction.
    # To recover off-diagonal coherences γ_ij,
    # correlations r_ij from regularizer L_off are required.
    gamma = L @ L.conj().T
    gamma = gamma / np.trace(gamma)  # Normalization

    return gamma


def compute_purity(gamma: np.ndarray) -> float:
    """P = Tr(Γ²)"""
    return np.trace(gamma @ gamma)
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

```python
import numpy as np


def reconstruct_gap_profile(
    external_data: dict,
    self_report: dict,
    conflict_data: dict,
) -> np.ndarray:
    """
    Reconstruction of the 7×7 Gap matrix from dual interview data.

    Returns:
        gap_matrix: 7×7 matrix Gap(i,j) ∈ [0, 1]
    """
    dimensions = ['A', 'S', 'D', 'L', 'E', 'O', 'U']
    n = len(dimensions)
    gap = np.zeros((n, n))

    for i in range(n):
        for j in range(i + 1, n):
            pair = f"{dimensions[i]}{dimensions[j]}"
            # Mismatch between external and internal data → high Gap
            ext = external_data.get(pair, 0.5)
            rep = self_report.get(pair, 0.5)
            discrepancy = abs(ext - rep)

            # Reaction time on conflict probes → phase θ_ij
            rt = conflict_data.get(pair, 1.0)
            phase_estimate = np.arctan(rt / np.median(list(conflict_data.values())))

            gap[i, j] = abs(np.sin(phase_estimate)) * (0.5 + 0.5 * discrepancy)
            gap[j, i] = gap[i, j]

    return gap
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

:::warning Status: [H] Research Program
The protocol $\pi_{\mathrm{bio}}: \mathrm{NeuralData} \to \mathcal{D}(\mathbb{C}^7)$ defines the mapping of neural data (EEG/fMRI/HRV) into the space of density matrices. The mathematical structure is **[T]** (follows from $G_2$-rigidity). The specific correspondences between EEG bands and dimensions are **[H]** (require experimental validation).
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

```python
import numpy as np
from scipy.optimize import minimize


def pi_bio(
    eeg_spectral: dict[str, float],     # {alpha, beta, gamma_low, gamma_high, theta, infraslow}
    hrv_features: dict[str, float],      # {LF, HF, LF_HF_ratio}
    cfc_matrix: np.ndarray,              # 7x7 CFC values
    reaction_times: np.ndarray,          # 21 RT values for pairs
    calibration: dict,                   # {weights, linear_params, ...}
) -> np.ndarray:
    """
    pi_bio: NeuralData -> D(C^7)

    Full reconstruction of coherence matrix Gamma from biological data.

    Returns:
        7x7 complex density matrix Gamma
    """
    # Step 1: Diagonal from spectral powers
    raw_diag = np.array([
        eeg_spectral['alpha'],           # A
        eeg_spectral['infraslow'],       # S (fMRI BOLD proxy)
        eeg_spectral['beta'],            # D
        eeg_spectral['gamma_low'],       # L
        eeg_spectral['gamma_high'] * eeg_spectral['theta'],  # E (PAC proxy)
        hrv_features['LF'],              # O
        hrv_features['HF'],              # U
    ])
    w = calibration['weights']
    diag = (w * raw_diag) / (w * raw_diag).sum()
    diag = np.clip(diag, 1e-4, 1.0)  # Prevent degeneracy
    diag = diag / diag.sum()

    # Step 2: Off-diagonal magnitudes from CFC
    c_scale = calibration['cfc_scale']
    off_diag_mag = c_scale * cfc_matrix[:7, :7]

    # Step 3: Phases from reaction times
    rt_mean = np.mean(reaction_times)
    rt_std = np.std(reaction_times) + 1e-8
    idx = 0
    phases = np.zeros((7, 7))
    for i in range(7):
        for j in range(i + 1, 7):
            gap = np.tanh((reaction_times[idx] - rt_mean) / rt_std)
            phases[i, j] = np.arcsin(np.clip(gap, -1, 1))
            phases[j, i] = -phases[i, j]
            idx += 1

    # Step 4: MLE reconstruction via Cholesky
    def neg_log_likelihood(params):
        L = np.zeros((7, 7), dtype=complex)
        k = 0
        for i in range(7):
            for j in range(i + 1):
                if i == j:
                    L[i, j] = max(params[k], 1e-6)
                else:
                    L[i, j] = params[k] + 1j * params[k + 1]
                    k += 1
                k += 1
        Gamma = L @ L.conj().T
        Gamma = Gamma / np.trace(Gamma)

        # Log-likelihood: diagonal agreement
        ll_diag = -np.sum((np.real(np.diag(Gamma)) - diag) ** 2) / 0.01

        # Log-likelihood: off-diagonal magnitude agreement
        ll_off = 0.0
        for i in range(7):
            for j in range(i + 1, 7):
                ll_off -= (abs(Gamma[i, j]) - off_diag_mag[i, j]) ** 2 / 0.05

        # Physical regularizer: P > P_crit
        P = np.real(np.trace(Gamma @ Gamma))
        P_penalty = -100 * max(0, 2 / 7 - P)

        return -(ll_diag + ll_off + P_penalty)

    # Initialize from diagonal
    x0 = np.zeros(48)
    for i in range(7):
        x0[i * (i + 1)] = np.sqrt(diag[i])

    result = minimize(neg_log_likelihood, x0, method='L-BFGS-B')

    # Reconstruct Gamma from optimal params
    L = np.zeros((7, 7), dtype=complex)
    k = 0
    for i in range(7):
        for j in range(i + 1):
            if i == j:
                L[i, j] = max(result.x[k], 1e-6)
            else:
                L[i, j] = result.x[k] + 1j * result.x[k + 1]
                k += 1
            k += 1
    Gamma = L @ L.conj().T
    Gamma = Gamma / np.trace(Gamma)

    return Gamma
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
