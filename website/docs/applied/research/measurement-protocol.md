---
sidebar_position: 2
title: Measurement Protocol for Γ
description: Operationalization of coherence matrix measurement for AI systems
---

# Γ Measurement Protocol for AI Systems

:::warning Document Status: [Pr] Research Program
This document describes a **research program** for operationalizing the coherence matrix $\Gamma$ for AI systems. The protocol requires **experimental validation**.
:::

:::note About Notation
- $\Gamma$ — [coherence matrix](/docs/core/dynamics/coherence-matrix)
- $P$ — [purity](/docs/core/dynamics/viability#определение-чистоты): $P = \mathrm{Tr}(\Gamma^2)$
- $\tau$ — [emergent internal time](/docs/proofs/dynamics/emergent-time) (Page–Wootters)
- $\varphi$ — [self-modeling operator](/docs/proofs/categorical/formalization-phi)
- $G$ — proposed encoder AIState → DensityMat; a functor on morphisms and a CPTP extension require separate conditions (Categorical Correctness below).
- $\mathrm{Coh}_E$ — E-coherence: $\mathrm{Coh}_E(\Gamma) = \|\pi_E(\Gamma)\|^2_{\mathrm{HS}} / \|\Gamma\|^2_{\mathrm{HS}}$ — interiority quality (HS-projection onto E-sector) [T]
:::

---

## Central Problem

UHM theory defines $\Gamma$ as an **object of the ∞-topos $\mathrm{Sh}_\infty(\mathcal{C})$** ([Axiom Ω⁷](/docs/core/foundations/axiom-omega)). However, the theory does not specify:

1. Which **observables** in an AI system correspond to the elements $\gamma_{ij}$
2. How to **reconstruct** $\Gamma$ from available data
3. How to **validate** the correctness of the reconstruction

:::info Fundamental Limitation
$\Gamma$ is an **ontological primitive**, not an observable. We reconstruct $\Gamma$ via a proposed **encoder** $G$ that compresses $\mathbb{R}^d$ (where $d \sim 10^9$ for an LLM) into $\mathcal{D}(\mathbb{C}^7)$.

A seven-dimensional target formalism is chosen here. Universal minimality requires the additional conditions of [Theorem S](/docs/proofs/minimality/theorem-minimality-7); the dimensional choice alone does not prove that compression preserves every relevant system property.
:::

:::info Reconstruction requires an observation model [T conditional on identification]
The state space has 48 independent real coordinates in its full-rank interior. Its structural automorphisms do **not** determine a map from AI features to states. A fixed observation model identifies only its observation fiber. Unique reconstruction requires injectivity; stable reconstruction additionally requires quantitative conditioning. These statements and their proofs are given in [ID-1 and ID-2](/docs/applied/research/reconstruction-identifiability#fiber-theorem).

The residual symmetry is the subgroup preserving the **actual** measurement design, its labels, calibration and targets; it is not automatically $G_2$ or $\Gamma_{\!\mathrm{oct}}$. $P$ and $R$ are unitary-invariant, while $\Phi$ and $\mathrm{Coh}_E$ reference a functional frame. Even two encoders in the same fixed frame can disagree on all these quantities if the data do not identify the state.

For time-series reconstruction, uniqueness of an ODE solution must be distinguished from observability of its initial state and stability of the inverse. Publish the observation operators, calibration and identification analysis with every reconstructed matrix.
:::

---

## Protocol Architecture

| Level | Name | Content |
|-------|------|---------|
| **4** | Causal validation | Intervention tests, lobotomy test |
| **3** | Dynamic validation | $dP/d\tau$, coherence flow, viability |
| **2** | Γ reconstruction | PSD-constrained reconstruction and confidence set |
| **1** | Observable extraction | Structural metrics (commutators, $\Phi_{\text{eff}}$, topology) |

---

## Mapping Measurements to AI Metrics

### Correspondence Table

| Dimension | Symbol | AI Metric | Formula | Rigor |
|-----------|--------|-----------|---------|-------|
| [Articulation](/docs/core/structure/dimension-a) | $A$ | Mutual information input↔latent | $I_A = I(\text{input}; \text{latent}) / H(\text{input})$ | [D/H] |
| [Structure](/docs/core/structure/dimension-s) | $S$ | Jacobian rank | $I_S = \mathrm{rank}_\varepsilon(J_f) / \min(d_{\text{out}}, d_{\text{in}})$ | [D/H] |
| [Dynamics](/docs/core/structure/dimension-d) | $D$ | Lyapunov exponent | $I_D = \max_i \lambda_i^{\text{Lyap}}$ (normalized) | [D/H] |
| [Logic](/docs/core/structure/dimension-l) | $L$ | Layer commutators | $I_L = 1 - \|[f_i, f_j]\|_F / (\|f_i\| \cdot \|f_j\|)$ | [D/H] |
| [Interiority](/docs/core/structure/dimension-e) | $E$ | Activation entropy | $I_E = \exp(S_{vN}(\rho_{\text{attn}}))$ — [experience differentiation](/docs/core/structure/dimension-e#differentiation-threshold-dmin-2) | [D/H] |
| [Ground](/docs/core/structure/dimension-o) | $O$ | Noise robustness | $I_O = 1 - \|\nabla_\epsilon \mathbf{h}\|_F$ | [D/H] |
| [Unity](/docs/core/structure/dimension-u) | $U$ | Effective Φ (integration, black-box) | $I_U = \Phi_{\text{eff}} = \lambda_2(L) / \lambda_{\max}(L)$ — approximation [D]; **when $\Gamma$ is known: $R_{\text{UHM}} = 1/(N \cdot P)$** [T, [reflection measure](/docs/consciousness/foundations/self-observation#мера-рефлексии-r)] | [D/T]† |

where $\nabla_\epsilon \mathbf{h} := (\mathbf{h}(x + \epsilon) - \mathbf{h}(x)) / \epsilon$ — finite-difference approximation

†**Unity metric hierarchy**: when $\Gamma$ is unavailable (black-box), $\Phi_{\text{eff}}$ [D] is used. When $\Gamma$ is reconstructed via the protocol, the correct measure is $R_{\text{UHM}} = 1/(N \cdot P)$ [T], an exact algebraic identity ([reflection measure R](/docs/consciousness/foundations/self-observation#мера-рефлексии-r), error $< 10^{-7}$ in implementation). $\Phi_{\text{eff}}$ and $R_{\text{UHM}}$ measure related but non-identical properties.

### Canonical Observable Indices {#канонические-наблюдаемые-индексы}

:::info Operational assignment of observable indices [D/H]
The table specifies candidate functional proxies, not uniquely derived measurements of $\gamma_{kk}$. A Hamiltonian/dissipative/regenerative decomposition of a generator does not identify neural or AI features with diagonal state coordinates: the generator and the state are different mathematical objects.

For the declared experiment, label the proxies $I_A,\ldots,I_U$, calibrate their units against a published reference ensemble, and freeze their normalization before testing. Their proposed channel associations — A/S/L with Hamiltonian influence, D/O with dissipative influence, E/U with regenerative influence — are hypotheses to be tested by interventions. Replacing a proxy defines a different operationalization and requires fresh calibration and held-out evaluation; it does not by itself violate a theorem about the generator.
:::

The formulas in the correspondence table define computable metrics [D]; their interpretation as measurements of UHM axes is [H]. Neither a definition nor a simulation proves that correspondence. In particular, attention weights must first be converted into a specified positive, trace-one operator before a von Neumann entropy is defined.

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

### Data fit, priors and identification

State validity is not empirical correctness. The surjective parametrization can express many states; a likelihood restricts them by observations. Regularization can choose a preferred state in an unresolved fiber but cannot prove identification.

For exploratory sensitivity analysis one may penalize diagonal, coherence-magnitude or dynamic discrepancies. Each penalty needs a specified observation/noise model and declared weights. A magnitude penalty leaves signed phases unresolved. A dynamic penalty imports the theory being tested. In confirmatory biological runs the dynamics and viability weights are zero (SUB-2); identifiability and target ranges are assessed through the [observation model](/docs/applied/research/reconstruction-identifiability).

| Penalty [D] | Expression | Selected purpose |
|---|---|---|
| $\mathcal{L}_{\text{diag}}$ | $\sum_i (\gamma_{ii} - I_i / \sum_j I_j)^2$ | Diagonal consistency |
| $\mathcal{L}_{\text{off}}$ | $\sum_{i \neq j} (\|\gamma_{ij}\|^2 - r_{ij}^2 \gamma_{ii} \gamma_{jj})^2$ | Coherence consistency |
| $\mathcal{L}_{\text{dyn}}$ | $\|\Gamma_{\tau+1} - \Phi_{\text{pred}}(\Gamma_\tau)\|_F^2$ | Dynamics consistency |

---

## Validation constraint: no threshold without ground truth {#граница-валидации}

:::warning What the field's one clinically validated measure teaches us
The Perturbational Complexity Index is the only consciousness measure with large-scale clinical validation: TMS-evoked EEG responses, Lempel–Ziv compressed, with an empirical cutoff $\mathrm{PCI}^*=0.31$ derived from a benchmark population and later validated on 719 TMS/hd-EEG sessions across wakefulness, NREM sleep, anaesthesia and disorders of consciousness. Two lessons transfer directly, and the second is a hard limit on what UHM may claim.
:::

**Lesson 1 — commensuration is solved by calibration, not by units.** PCI is normalised for signal length and amplitude, and its threshold is not derived from theory but *fitted to a benchmark population*. This is exactly the fix that closes [audit A-20](/docs/reference/status-registry): the seven observable indices are defined in incommensurable units, so a $\Gamma$ built from their raw sum is a function of arbitrary definitional choices. The canonical repair is to take each index as a **percentile against a declared reference ensemble** — the same operation the applied layer already performs when it scores a person against a population. The ensemble must be published together with any number derived from it; a percentile without its reference is not a measurement.

**Lesson 2 — a threshold is only as valid as its ground truth, and this bounds UHM.** PCI's cutoff is trustworthy *because* it was calibrated where consciousness was independently known: the same brains awake and under anaesthesia, patients who could later report. That ground truth is what makes the number mean anything. UHM's window $P\in(2/7,3/7]$ is derived (T-124), not fitted — which is a genuine advantage — but derivation fixes the *form* of the criterion, not the *mapping* from a given substrate into $\Gamma$. For any system where we have no independent evidence of presence or absence of experience — a fungal network, a slime mould, a language model — the mapping cannot be validated, and a measured $P$ inside or outside the window therefore establishes **nothing about experience**. It establishes only that the system's functional indices, under a declared coarse-graining, do or do not sit where the theory says a viable holon sits.

Consequently this corpus does not, and will not, assert consciousness or its absence in a non-human substrate on the strength of a $\Gamma$-measurement alone. What such a measurement can honestly do is **discriminate states within one system** — the paired design that made PCI work — and that is the only design in which our thresholds carry evidential weight outside the human case.

**Lesson 3 — measure the functional structure, not the carrier.** Complexity read off the raw signal misreads systems whose carrier is atypical: children with Angelman syndrome are awake, volitional and responsive while displaying the hypersynchronous delta EEG normally taken as a signature of unconsciousness. The resolution is that the relevant complexity is not in the amplitude envelope but in the functional organisation. UHM is structurally committed to the same discipline: $\Gamma$ is built from functional indices (integration, differentiation, robustness, sensitivity), never from raw signal statistics, and a protocol that shortcuts to the carrier will inherit the field's known failure cases.

## Categorical Correctness

### State parametrization does not define a channel or a functor

A nonzero lower-triangular $7\times7$ factor $L$ with real diagonal has $7+2\cdot21=49$ real entries. Normalizing $LL^\dagger$ removes a redundant positive scale and yields 48 state degrees of freedom. In the positive-definite interior, the Cholesky factor with positive diagonal and $\operatorname{Tr}(LL^\dagger)=1$ is unique; rank-deficient states belong to boundary strata and do not share a single unconstrained global chart. Estimating all 49 raw factor entries and then normalizing does **not** violate the trace axiom. Leaving the normalization out does.

For a bijective chart $\psi:Q\to\mathsf S$, transporting a self-map by $f\mapsto\psi f\psi^{-1}$ preserves composition and identities by algebra. This defines a functor between categories of the corresponding self-maps. It does **not** prove that the transported morphisms are linear CPTP maps. A functor into the CPTP category additionally requires an explicit assignment on every morphism and proof of linearity, complete positivity, trace preservation, identities and composition.

For a many-to-one encoder $G:X\to\mathsf S$, a source transformation $f:X\to X$ descends to a well-defined state map $\bar f$ iff $G(x)=G(x')$ implies $G(f(x))=G(f(x'))$. Then $\bar f(G(x))=G(f(x))$, and composition is preserved on the image. A CPTP extension outside that image is a further condition. This fiber condition is the relevant exact criterion; a Cholesky formula alone cannot supply it.

A claimed approximate functor must first specify the source and target categories, object and morphism maps, common domains and norm. For maps on a common state domain one may test a composition defect $\sup_\Gamma\|G(f\circ g)(\Gamma)-G(f)(G(g)(\Gamma))\|_{\mathrm{HS}}$. A local Jacobian approximation gives no universal defect bound without bounds on the second derivatives and the operating region. Numerical preservation of a diagonal or of one trajectory verifies that implementation property, not functoriality of every morphism.

See [the observation/estimator/channel distinction](/docs/applied/research/reconstruction-identifiability#observation-model) and [Watrous, Definition 2.13](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf).

### Separation Principle: Diagonal / Coherences [T, MVP-0] {#принцип-разделения-диагональ--когерентности-т-mvp-0}

**Scope of the diagonal profile.** The selected implementation reports small variation of $W_{\mathrm{raw}}=\|\mathbf1-N\operatorname{diag}\Gamma\|_2$; this is a particular-run observation, not a general dynamics invariant. This unclamped quantity is not the clamped stress norm without further conditions.

The diagonal is preserved with explicitly population-preserving dephasing, diagonal $H$, matching target populations and no population-changing input. General Hamiltonian motion can change populations; Hermiticity does not annihilate $-i[H,\Gamma]_{kk}$. See [T-134](/docs/proofs/consciousness/operationalization#t-134). Weight pruning can also change populations and normalization: specify and measure its map rather than assume its action. Interpreting the diagonal as identity/personality and coherences as learning is an architecture hypothesis [H].

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

**Interventional test of predictive usefulness [H].** Predeclare direction, lag and magnitude of the metric response to weight pruning, and test its prediction of accuracy changes on held-out interventions. Temporal precedence alone proves neither causation nor ontological validity. Proxies, normalization and readout timing can alter the ordering; declared control models are required.

### Causal Closure of E

$$
\Delta\Phi_E := \Phi_{\text{eff}}(\mathcal{S}_E) - \Phi_{\text{eff}}(\mathcal{S}_E | \text{do}(X := \text{random})) > \varepsilon_{\text{causal}}
$$

A small $\Delta\Phi_E$ rejects the proposed causal proxy under this intervention; it does not prove absence of experience. The interpretation “simulation without realization” remains a phenomenological hypothesis.

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
mount core.math.linalg.{svd, eigvalsh, StaticMatrix};
mount core.math.tensor.{Tensor, frobenius_norm};
mount core.math.random.{XorShift128, Rng};

/// Access protocol for deep models. Implementations provide hooks
/// on activations, attention, and automatic differentiation.
public protocol ModelHooks {
    type Activation;
    fn get_activations(&self, batch: &Tensor<Float>) -> List<Self.Activation>;
    fn get_attention_weights(&self, batch: &Tensor<Float>) -> Tensor<Float>;
    fn get_jacobian(&self, batch: &Tensor<Float>) -> Tensor<Float>;
    fn layer_commutator_norm(&self, i: Int, j: Int, batch: &Tensor<Float>) -> Float;
    fn estimate_lyapunov(&self, batch: &Tensor<Float>) -> Float;
}

/// Helpers — specialised per architecture.
public pure fn estimate_mutual_info(x: &Tensor<Float>, y: &Tensor<Float>) -> Float
    = unimplemented;

public pure fn von_neumann_entropy(attn: &Tensor<Float>) -> Float
    = unimplemented;

public pure fn build_attention_graph(attn: &Tensor<Float>) -> Tensor<Float>
    = unimplemented;

/// 7-dimensional UHM metrics I_A…I_U for a neural network.
public type DimensionMetrics is {
    i_a: Float, i_s: Float, i_d: Float, i_l: Float,
    i_e: Float, i_o: Float, i_u: Float,
};

/// Compute 7 UHM dimensions for a neural network.
public fn compute_dimension_metrics<M: ModelHooks>(
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
              else { 1.0 - comms.iter().sum<Float>() / (comms.len() as Float) };

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
public pure fn reconstruct_gamma(m: &DimensionMetrics) -> StaticMatrix<Complex, 7, 7> {
    let raw = StaticVector<Float, 7>.from_array(
        [m.i_a, m.i_s, m.i_d, m.i_l, m.i_e, m.i_o, m.i_u]
    ).map(|v| v.clamp(0.01, 1.0));           // prevent degeneracy
    let total: Float = raw.iter().sum();
    let diag = raw.map(|v| v / total);

    // Cholesky factor L = diag(√p_k).
    let l = StaticMatrix<Complex, 7, 7>.diagonal(
        diag.map(|v| Complex.from_real(v.sqrt()))
    );
    let gamma = l.matmul(&l.adjoint());
    &gamma / gamma.trace()                                              // normalise
}

/// Purity P = Tr(Γ²).
public pure fn compute_purity(gamma: &StaticMatrix<Complex, 7, 7>) -> Float
    where ensures 1.0/7.0 <= result && result <= 1.0
{
    (gamma.matmul(&gamma)).trace().real()
}
```

### Threshold Values

| Parameter | Value | Source | Status |
|-----------|-------|--------|--------|
| $P_{\text{crit}}$ | $2/7 \approx 0.286$ | [Theorem](/docs/proofs/dynamics/theorem-purity-critical) | Proven |
| $\mathrm{rank}(\rho_E) > 1$ (L1 threshold) | $> 1$ | Non-trivial interiority | [T] |
| $R_{\text{th}}$ (L2 threshold) | $\geq 1/3$ | [Hierarchy](/docs/proofs/consciousness/interiority-hierarchy) | Proven [T] |
| $\Phi_{\text{th}}$ (L2 threshold) | $\geq 1$ | [T-129](/docs/proofs/consciousness/operationalization#t-129) | Proven [T] |
| $D_{\text{diff}}^{\text{min}}$ | $\geq 2$ | [T-151](/docs/proofs/consciousness/substrate-closure#t-151) | Independent L2 threshold [D] (it read "Proven [T]" until 2026-09-25) |
| Composition defect | Implementation-specific | Specify object/morphism maps and verify fiber descent | Conditional |
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
1. **Cholesky-backbone ($\alpha=0$): state validity and properties of the particular implementation** [C, MVP-1]; a global bijection and a CPTP functor do not follow (see “Categorical Correctness”)
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

:::warning Status: [Pr] Research Program
The protocol is developed theoretically. Experimental validation is absent.
:::

### Principle

The dual interview simultaneously measures **external** (behavioral, physiological) and **internal** (self-report) characteristics of a system, proposing a joint observation model; full-state and phase reconstruction require a separate identification check.

### Protocol Stages

| Stage | Measurement | Data | What We Extract |
|-------|-------------|------|-----------------|
| 1. Background recording | EEG, fMRI, HRV | Resting physiology | Diagonal $\gamma_{ii}$, estimate of $P$ |
| 2. Structured interview | Responses to 7 question batteries (per dimension) | Verbal reports | Coherences $\lvert\gamma_{ij}\rvert$ between dimensions |
| 3. Paradoxical probes | Conflict tasks | Reaction time, HRV | Behavioral proxy [H]; no measured phase |
| 4. Dynamic probe | Stress test + recovery | Time series $P(\tau)$ | $\kappa(\Gamma)$, $\Gamma_2$, τ_char |

### Reconstruction of the Hamiltonian component [T conditional on an identified generator]

A matrix ratio $\Gamma(t+\delta t)\Gamma(t)^{-1}$ is not a propagator on state vectors; its logarithm does not reconstruct $H$. That former formula is withdrawn (2026-10-03).

If the non-Hamiltonian contribution $B(\Gamma)$ is independently known, set $X=\dot\Gamma-B(\Gamma)$ and solve $X=-i[H,\Gamma]$ as a real linear inverse problem in Hermitian $H$. In an eigenbasis of $\Gamma$ with eigenvalues $p_m$, every pair with $p_m\ne p_n$ obeys

$$
H_{mn}=\frac{iX_{mn}}{p_n-p_m}.
$$

The blocks commuting with $\Gamma$ are not identified by one state derivative, and a necessary consistency condition is $X_{mn}=0$ whenever $p_m=p_n$. For one **constant** Hamiltonian probed on several known states, the remaining ambiguity is the intersection of their commutants; uniqueness up to an additive scalar requires that intersection to consist only of scalars. Small spectral gaps give poor conditioning. Unknown dissipative/regenerative rates require joint identification; a high sampling frequency alone supplies none of these conditions. [Dynamic observability](/docs/applied/research/reconstruction-identifiability#local-identification).

### Equilibrium Gap

:::info Stationary coherence [T conditional on a frozen linear model]
For the scalar equation $\dot\gamma_{ij}=-(\Gamma_2+\kappa+i\Delta\omega_{ij})\gamma_{ij}+\kappa\gamma^*_{ij}$ with constant coefficients and a fixed target:

$$
|\gamma_{ij}^{(\infty)}|=\frac{\kappa|\gamma^*_{ij}|}{\sqrt{(\Gamma_2+\kappa)^2+\Delta\omega_{ij}^2}}.
$$

This is a magnitude, not Gap. With a state-dependent target $\varphi(\Gamma)$, the expression is only a self-consistency condition for an equilibrium; it does not prove existence, uniqueness or stability.
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
# Exploratory interview score, not a reconstructed phase or UHM Gap.
# No missing-data defaults; behavior is excluded from confirmation (SUB-3).
def interview_discrepancy(external, report):
    if external is None or report is None:
        return None
    return abs(external - report)

# Only after the signed complex observation model has been calibrated:
def gap_from_identified_coherence(gamma_ij):
    if gamma_ij is None:
        return None
    if abs(gamma_ij) == 0:
        return 0.0  # declared zero-coherence convention
    return abs(gamma_ij.imag) / abs(gamma_ij)
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

:::warning Status: [D] estimator + [T] conditional identification + [H] empirical bridge
The protocol $\pi_{\mathrm{bio}}$ is a declared estimator from neural features to candidate density matrices, or to a set of states compatible with the data. The validity conditions $\Gamma\succeq0$ and $\operatorname{Tr}\Gamma=1$ are mathematical. The EEG/HRV/fMRI correspondence, observation law and calibration are empirical hypotheses; $G_2$-rigidity does not fix them. [Fundamental Closures §9](/docs/proofs/categorical/fundamental-closures#pi-bio-protocol) describes a proposed simultaneous recording design. Its identifiability must be established under the criteria below before it is called full-state tomography. The anti-circularity safeguards [SUB-1 … SUB-6](#substitution-position) remain mandatory.
:::

### Principle: declared observation model and its fibers {#eeg-полосы}

:::info Theorem (replacement for the withdrawn encoder-uniqueness claim) [T]
For a fixed calibrated observation law $\mathsf O_\theta$, exact data identify its fibers. The state is unique exactly when this law is injective on the admissible state set; a quantity is unique exactly when it is constant on each fiber. For calibrated linear means $\operatorname{Tr}(H_a\Gamma)$, full-state identification is equivalent to the projected Hermitian operators spanning the 48-dimensional traceless Hermitian space. [ID-1, ID-2 and proofs](/docs/applied/research/reconstruction-identifiability#fiber-theorem).

**Correction 2026-10-03.** The former proof $\pi_2\circ\pi_1^{-1}$ assumed an inverse absent from the hypotheses and is withdrawn. Fixing a Fano frame or classifying automorphisms of the codomain does not identify a neural encoder. Residual symmetry must be derived from the actual observation model, not assigned automatically as $G_2$ or $\Gamma_{\!\mathrm{oct}}$.
:::

The proposed band table is a functional **hypothesis**. CFC magnitudes may calibrate coherence magnitudes; they do not determine signed phases. Full reconstruction requires a specified, validated complex observation model. Otherwise retain the unresolved observation fiber and report ranges of the identifiable targets.

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

$$
\gamma_{kk} = \frac{w_k \cdot S_k}{\sum_{j=1}^{7} w_j \cdot S_j}, \qquad k \in \{A,S,D,L,E,O,U\}
$$

where $S_k$ — normalized spectral power (or combined metric) for the $k$-th dimension, $w_k$ — calibration weights (fixed on the wakefulness reference ensemble without fitting the tested labels (SUB-1)).

### Step 2: Extracting Coherences $|\gamma_{ij}|$ from Cross-Frequency Coupling {#шаг-2-когерентности}

:::tip Key Correspondence
Coherences $|\gamma_{ij}|$ between dimensions $i$ and $j$ are proportional to the strength of cross-frequency coupling (CFC) between the corresponding EEG bands:

$$
|\gamma_{ij}| \propto \mathrm{CFC}(\mathrm{band}_i, \mathrm{band}_j)
$$

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

### Step 3: signed phase observations and the Gap profile {#шаг-3-фазы}

For nonzero coherence, $\theta_{ij}=\arg\gamma_{ij}$ and $\mathrm{Gap}_{ij}=|\sin\theta_{ij}|$. Gap loses phase sign and branch. An inverse $\theta=\arcsin(\mathrm{Gap})$ is not a reconstruction. [Explicit positive-state counterexamples](/docs/applied/research/reconstruction-identifiability#phase-counterexamples) have identical diagonal, magnitudes and Gap but different triangle holonomies; some also have different spectra.

Record the complex cross-spectral or phase-locking mean $z_{ij}=\langle e^{i(\phi_i-\phi_j)}\rangle$ with declared timing/reference and orientation $z_{ji}=\overline z_{ij}$. Its argument is a measured neural phase; the association with $\theta_{ij}$ requires a frozen calibrated observation law [H]. The real PLV $|z_{ij}|$ provides no signed phase. Phase conventions for genuinely cross-frequency pairs must state the harmonic phase combination; ordinary same-frequency coherence must not silently substitute for PAC.

Reaction times may test a separately declared behavioral association with Gap in exploratory work, but cannot fix a phase branch and are excluded from the confirmatory predictor (SUB-3). If signed complex observations are absent or their link to $\Gamma$ is unvalidated, mark phases unresolved. No zero-fill or behavior-to-phase imputation is allowed in confirmation.

### Step 4: constrained likelihood reconstruction {#шаг-4-mle}

:::info Estimator [D], observation bridge [H], identification [T conditional on the model]
With calibration $\theta$ frozen, define

$$
\widehat{\mathcal G}_\theta(y)=\underset{\Gamma\succeq0,\ \operatorname{Tr}\Gamma=1}{\arg\max}\;\log p_\theta(y\mid\Gamma).
$$

This is an **argmax set**, not automatically one state. In a linear Gaussian model, $y\sim\mathcal N(M_\theta(\Gamma),\Sigma)$ with known $\Sigma\succ0$, it is a convex least-squares problem; informational completeness gives uniqueness and a quantitative stability bound [ID-2](/docs/applied/research/reconstruction-identifiability#linear-frame). Unknown calibration requires joint identification. For nonlinear CFC/phase models an optimizer's convergence is not a proof of global uniqueness.
:::

A declared exploratory model may use $S_k\sim\mathcal N(a_k\gamma_{kk}+b_k,\sigma_k^2)$ and $\mathrm{CFC}_{ij}\sim\mathcal N(c_{ij}|\gamma_{ij}|,\tau_{ij}^2)$, with calibrated coefficients. Such magnitude data are incomplete for full-state reconstruction. Add separately calibrated real and imaginary observations, or report the full compatible set. Noise models must state whether variance depends on the state and whether errors are correlated.

**Positivity:** optimize directly over the positive semidefinite cone with unit trace. A nonzero Cholesky factor is an alternative implementation: it has 49 raw real entries and one redundant scale after normalization; it is not an unconstrained 48-entry triangular array. A global phase of $L$ already cancels in $LL^\dagger$; imposing $\gamma_{AS}\in\mathbb R_+$ changes a relative state phase and is forbidden unless explicitly justified as a symmetry of the observation design.

**Anti-circularity:** $\lambda_2=0$ in every test and $\lambda_1=0$ in confirmation (SUB-2). A dynamical penalty may only be a declared sensitivity analysis. Priors, phase choices and rank constraints must be stated; they select states within a fiber and cannot supply measured information. Report the confidence set, target ranges, model-incompatibility cases and undetermined verdicts [ID-A … ID-D](/docs/applied/research/reconstruction-identifiability#confirmatory).

### Step 5: Connection to PCI (Casali et al. 2013; Casarotto et al. 2016) {#pci-связь}

:::info Hypothesis ($\mathrm{PCI} \to \Phi$ proxy) [H]
The Perturbational Complexity Index (PCI) is monotonically related to the integration measure $\Phi(\Gamma)$ (prediction P8.3). A linear form $\Phi(\Gamma) \approx \alpha_{\mathrm{PCI}} \cdot \mathrm{PCI} + \beta_{\mathrm{PCI}}$ with constants fitted on a training set is a *calibration*, not a bridge: whatever it fits, it cannot test.

**Justification:** PCI measures the algorithmic complexity of the cortical response to TMS perturbation; a high PCI requires a response that is both integrated and differentiated, and $\Phi$ is UHM's integration measure. The earlier sentence "PCI $\geq 0.31$ during wakefulness, corresponding to $\Phi \geq \Phi_{\mathrm{th}} = 1$" stated a correspondence that nothing derives; it is withdrawn.
:::

**What can be derived — the bridge on UHM's side [T].** Three facts fix how UHM's thresholds sit relative to each other, with no neural data:
- $\Phi \geq 1 \Rightarrow P \geq 2/7$ on all of $\mathcal D(\mathbb C^7)$ ([T-129a](/docs/proofs/consciousness/operationalization#t-129a-универсальность)).
- On the uniform-diagonal stratum $P = (1 + \Phi)/7$, $R = 1/(1 + \Phi)$ and $C = \Phi R = \Phi/(1+\Phi)$; the window $P \in (2/7, 3/7]$ is exactly $\Phi \in (1, 2]$, $R \in [1/3, 1/2)$, $C \in (1/2, 2/3]$ (checked in `check_core_numbers.py`, `test_uniform_diagonal_window_is_phi_between_one_and_two`).
- The purity/reflection interval has **two exits**: $P \leq 2/7$ (too mixed; on the uniform diagonal the same as $\Phi \leq 1$) and $P > 3/7$ (too pure; $R < 1/3$). A low PCI therefore has two possible UHM signatures, not one.

**What cannot be derived [✗ if claimed].** A numerical conversion between PCI and $P$ or $\Phi$. PCI is a normalised Lempel–Ziv complexity of a binarised source-activity matrix; $P$ and $\Phi$ are functions of $\Gamma$. The closeness of $\mathrm{PCI}^* = 0.31$ to $2/7 \approx 0.286$ is a coincidence of two unrelated scales and carries no evidential weight. The bridge that *can* be tested is a **concordance of verdicts** on the same sessions (P8.4 below): $\mathrm{Cons}(\hat\Gamma)$ against $\mathrm{PCI}_{\max} > \mathrm{PCI}^*$.

**Reference data — Casarotto et al. (2016), Table 1** (*Ann. Neurol.* 80: 718–729, doi:10.1002/ana.24779). Benchmark population: 150 subjects, 540 sets of TMS-evoked potentials; $\mathrm{PCI}^* = 0.31$ from an ROC analysis in which the presence or absence of a subjective report — immediate or delayed — is the ground truth; on this benchmark the cut-off separates the two classes with 100 % sensitivity and 100 % specificity. Values are $\mathrm{PCI}_{\max}$ per subject, median [min–max]:

| Condition | Report | Subjects | $\mathrm{PCI}_{\max}$ | UHM verdict to be tested |
|---|---|:-:|:-:|---|
| Wakefulness (healthy) | immediate | 102 | 0.53 [0.39–0.70] | Cons |
| REM sleep | delayed (dream) | 8 | 0.48 [0.36–0.56] | Cons |
| Ketamine anaesthesia | delayed | 6 | 0.43 [0.36–0.52] | Cons |
| NREM sleep | none | 18 | 0.25 [0.15–0.31] | ¬Cons |
| Midazolam | none | 6 | 0.30 [0.23–0.31] | ¬Cons |
| Xenon | none | 6 | 0.23 [0.11–0.31] | ¬Cons |
| Propofol | none | 6 | 0.26 [0.23–0.31] | ¬Cons |

Applied to patients: 36 of 38 in a minimally conscious state had $\mathrm{PCI}_{\max} > \mathrm{PCI}^*$ (sensitivity 94.7 %), and 9 of 43 in a vegetative state did too. (Casali et al. 2013, *Sci. Transl. Med.* 5(198): 198ra105, doi:10.1126/scitranslmed.3006294, introduced the index.) The table this section carried until 2026-09-25 — "wakefulness $0.44 \pm 0.10$, REM $0.41 \pm 0.09$, NREM $0.18 \pm 0.06$, propofol $0.12 \pm 0.05$, coma $0.15 \pm 0.10$, MCS $0.32 \pm 0.08$", labelled "observed" — has no source in either paper and is withdrawn. The REM and ketamine rows matter most for UHM: consciousness without behaviour, where the verdict cannot be read off reports given at the time.

### Step 6: Connection to Quantum Cognition (Pothos-Busemeyer) {#quantum-cognition}

:::info Context: Quantum Cognition
The Pothos-Busemeyer approach (Annual Review of Psychology, 2022) models cognitive processes via quantum states in Hilbert space. Basic formalism: $\rho \in \mathcal{D}(\mathcal{H})$ for describing beliefs and decisions.

**Connection to UHM:** Quantum cognition uses $\dim(\mathcal{H})$ = number of alternatives. UHM selects $\dim(\mathcal{H}) = 7$ as its primitive frame; the general minimality claim requires the stated additional premises ([Theorem S](/docs/proofs/minimality/theorem-minimality-7)). The matrix $\Gamma \in \mathcal{D}(\mathbb{C}^7)$ is **ontological** (not epistemic): it defines the system, rather than describing an observer's beliefs about the system.
:::

### Step 7: Full Algorithm $\pi_{\mathrm{bio}}$ {#алгоритм-pi-bio}

```python
# Reference algorithm for a CALIBRATED LINEAR Gaussian observation model.
# Requires NumPy and a semidefinite solver through CVXPY.
# This is a state estimator, not a CPTP channel or a neural feature extractor.
import numpy as np
import cvxpy as cp


def traceless_hermitian_basis(n=7):
    basis = []
    for k in range(1, n):
        diag = np.zeros(n)
        diag[:k], diag[k] = 1, -k
        basis.append(np.diag(diag) / np.sqrt(k * (k + 1)))
    for i in range(n):
        for j in range(i + 1, n):
            re = np.zeros((n, n), complex)
            im = np.zeros((n, n), complex)
            re[i, j] = re[j, i] = 1 / np.sqrt(2)
            im[i, j], im[j, i] = 1j / np.sqrt(2), -1j / np.sqrt(2)
            basis.extend([re, im])
    return np.asarray(basis)  # 48 orthonormal REAL coordinates, trace zero


def reconstruct_linear(y, H, covariance, epsilon):
    # y_a models Tr(H_a Gamma); H and covariance are frozen calibration.
    # Signed imaginary observations must be present in H/y if claimed measured.
    # Missing observations are omitted, never replaced by zeros or arcsin(Gap).
    y, H = np.asarray(y, float), np.asarray(H, complex)
    if len(y) == 0 or H.shape != (len(y), 7, 7) or epsilon < 0:
        raise ValueError("Invalid observation design or confidence radius")
    if not np.all(np.isfinite(y)) or not np.all(np.isfinite(H)):
        raise ValueError("Non-finite observations or operators")
    if not np.allclose(H, H.conj().transpose(0, 2, 1)):
        raise ValueError("Observation operators must be Hermitian")
    covariance = np.asarray(covariance, float)
    if covariance.shape != (len(y), len(y)) or not np.allclose(covariance, covariance.T):
        raise ValueError("Invalid fixed covariance")
    chol = np.linalg.cholesky(covariance)  # rejects non-positive covariance
    B = traceless_hermitian_basis()
    A = np.real(np.einsum("aij,bji->ab", H, B))
    offset = np.real(np.trace(H, axis1=1, axis2=2)) / 7
    Aw = np.linalg.solve(chol, A)
    yw = np.linalg.solve(chol, y - offset)
    singular_values = np.linalg.svd(Aw, compute_uv=False)
    # Numerical diagnostics supplement, but do not replace, an analytic proof.
    rank = np.linalg.matrix_rank(Aw)
    alpha = singular_values[-1] if rank == 48 else 0.0
    q = cp.Variable(48)
    Gamma = np.eye(7) / 7 + sum(q[b] * B[b] for b in range(48))
    residual = Aw @ q - yw
    # SUB-2: lambda_1 = lambda_2 = 0; no viability or dynamics penalty.
    problem = cp.Problem(cp.Minimize(cp.sum_squares(residual)), [Gamma >> 0])
    problem.solve()  # publish solver, tolerances and convergence diagnostics
    if problem.status not in (cp.OPTIMAL, cp.OPTIMAL_INACCURATE):
        raise RuntimeError("Reconstruction failed")
    candidate = np.asarray(Gamma.value)
    min_eigenvalue = np.linalg.eigvalsh(candidate).min()
    trace_error = abs(np.trace(candidate) - 1)
    # Floating-point residuals are not exact PSD certificates. Publish them.
    # A production implementation must certify or declare its PSD projection
    # and recompute fit/confidence ranges after that change.
    fit_residual = np.linalg.norm(Aw @ q.value - yw)
    # Confidence set: Gamma(q) >= 0 and ||Aw q - yw|| <= epsilon.
    # Coverage of epsilon must be calibrated independently of tested thresholds.
    # If empty, report model incompatibility. If predicates differ on the set,
    # report an undetermined verdict instead of using only this representative.
    return {
        "numerical_candidate": candidate,
        "minimum_eigenvalue": min_eigenvalue,
        "trace_error": trace_error,
        "design_rank": rank,
        "smallest_singular_value": alpha,
        "fit_residual": fit_residual,
        "confidence_set": {"basis": B, "Aw": Aw, "yw": yw, "radius": epsilon},
        "candidate_residual_within_radius": fit_residual <= epsilon,
        "linear_design_full_rank": rank == 48,
        "solver_status": problem.status,
    }
```

### Replication-Ready Specification for TMS-EEG PCI Data {#replication-ready-tms-eeg}

:::info Replication target
This is a specification for **testing a declared operationalization**, not a ready validated instrument. Reconstruct states or compatible sets from a frozen observation model, report identification/conditioning and uncertainty, and evaluate held-out predictions against PCI and reports. Mathematical state-space rigidity does not certify the instrument or the neural bridge.
:::

**R1. Data provenance and eligibility.** A candidate dataset must publish or supply raw TMS-triggered EEG, timing/reference metadata, independent outcome annotations, and the modalities required by the frozen encoder (including ECG/HRV if used). Record the access conditions, version, DOI and a modality inventory before pre-registration. [Casali et al. (2013)](https://doi.org/10.1126/scitranslmed.3006294) and [Casarotto et al. (2016)](https://doi.org/10.1002/ana.24779) are primary benchmark publications; their publication does not by itself establish current access to their raw data.

**Correction 2026-10-03.** The former R1.b description of OpenNeuro `ds004504` as a Rogasch TMS-EEG benchmark is false: its [primary dataset metadata](https://github.com/OpenNeuroDatasets/ds004504/blob/main/dataset_description.json) identify routine EEG from Alzheimer’s disease, frontotemporal dementia and healthy subjects. It is not eligible for the claimed TMS-PCI replication. The former unspecified Comsa OSF registration and Bodart access/count entries are not a verified dataset inventory and are removed. No public dataset is currently certified here to provide the whole required measurement bundle; missing modalities require a separately registered partial protocol, not imputation.

**R2. Pre-processing pipeline (MNE-Python canonical).** The reference preprocessing chain, to be applied to raw EEG (60-channel montage, 1 kHz sampling, TMS-triggered epochs $[-1, +1]\,\mathrm{s}$):

| Step | Operation | Tool / parameters |
|------|-----------|-------------------|
| R2.1 | TMS pulse artefact removal | Cubic interpolation over $[-2, +12]\,\mathrm{ms}$ around the pulse (`mne.preprocessing.fix_stim_artifact`) |
| R2.2 | Downsample | 1 kHz → 250 Hz (`mne.Epochs.resample`) |
| R2.3 | Re-reference | Average reference, exclude TMS-side frontal channels |
| R2.4 | Bandpass filter | 0.5–80 Hz, 4th-order Butterworth zero-phase (`mne.filter.filter_data`) |
| R2.5 | Notch filter | 50 Hz (or 60 Hz), Q = 30 |
| R2.6 | ICA artefact rejection | FastICA, 30 components; reject TMS-locked decay, eye-blink, ECG (`mne.preprocessing.ICA`) |
| R2.7 | Epoch-level rejection | $\|\text{max}-\text{min}\| > 120\,\mu\mathrm V$ → drop epoch |
| R2.8 | Spectral decomposition | Morlet wavelets, 1–80 Hz log-spaced, 5-cycle wavelet, baseline $[-600,-100]\,\mathrm{ms}$ |

The canonical bands used by $\pi_{\mathrm{bio}}$ are then extracted from the wavelet spectrogram (integrated over post-TMS window $[0, +300]\,\mathrm{ms}$, averaged across channels for diagonal feature vector; cross-channel pairwise for CFC computations).

**Measurement coverage:** the 0.5–80 Hz filter and 300-ms window cannot supply 0.01–0.1 Hz infraslow features or 80–100 Hz coherences. Separately registered long-duration/broadband recordings are required, or an explicitly different partial encoder. Missing features cannot be recovered from the filtered signal.

**R3. Feature extraction.** Publish the seven feature definitions, modality/timing inventory and complex pairwise observations. CFC measures and their normalization must be specified separately for every pair; no library name establishes their link to $\Gamma$. In confirmation, reaction times and PCI are excluded from the predictor; a real PLV is never used as a phase or as an RT surrogate. Retain signed complex means where valid, record absent observations as missing, and perform the identification check for the resulting observation design. Missing HRV or low-frequency coverage prevents the full seven-axis claim under the current band assignment.

**R4. Calibration.** Fix weights, offsets, scales, frame labels, covariance and all feature choices on an independently declared wakefulness reference cohort (SUB-1). Publish the normalization convention and calibration uncertainty; do not tune purity to $2/7$, agreement with PCI or reduced between-subject variability. A uniform population diagonal is a normalization convention if imposed, not a measured discovery. The two proposed feature dictionaries (spectral-band and functional-feature versions) are distinct candidate encoders; predeclare one, and evaluate the other only as a separately registered comparator. Use subject-level separation, with an untouched test cohort.

**R5. Reconstruction.** Use the constrained likelihood of Step 4 and the reference linear implementation only if its observation law has been calibrated. Publish analytic/numerical rank, smallest singular value, residuals, solver diagnostics and confidence sets. $\lambda_2=0$ in every test and $\lambda_1=0$ in confirmation (SUB-2); other dynamic weights are sensitivity analysis. State constraints enforce PSD/trace-one, not a viability threshold. Incomplete designs yield partial identification; failed fit or solver convergence must not be reported as a unique matrix measurement.

**R6. Observable computation and residual symmetry.** For each compatible state compute

$$
P=\operatorname{Tr}\Gamma^2,\quad R=1/(7P),\quad
\Phi=\frac{\sum_{i\ne j}|\gamma_{ij}|^2}{\sum_i\gamma_{ii}^2},\quad
\mathrm{Coh}_E=\frac{\gamma_{EE}^2+2\sum_{i\ne E}|\gamma_{Ei}|^2}{P}.
$$

Report ranges over the confidence set, not only one optimized representative. $P,R$ are unitary-invariant; $\Phi$ is invariant under frame monomial transformations, and $\mathrm{Coh}_E$ under those preserving $E$ (also under the continuous unitary stabilizer of $E$). These algebraic invariances do not imply agreement between different encoders. Publish the Fano labelling, $E$-axis assignment and phase references. Derive any residual equivalence from the observation law; never use a $G_2$ Procrustes fit to alter an already pinned functional frame. A disagreement after identical calibration is an empirical or implementation discrepancy to investigate.

**R7. Validation against PCI.**
- Compute the subject's PCI on the same TMS-EEG data via the Massimini algorithm (Lempel–Ziv complexity of significant sources; reference implementation available via PCIst package).
- Test the monotonic hypothesis $\Phi(\Gamma) \approx \alpha_\mathrm{PCI}\cdot \mathrm{PCI} + \beta_\mathrm{PCI}$ (Step 5 hypothesis [H]).
- Pre-register: $r_{\mathrm{Spearman}} \ge 0.5$ across $\ge 20$ subjects constitutes corroboration; $r < 0.3$ constitutes falsification of P8.3.

**R8. Reference implementation stub.** The Python code in Step 7 is *reference* only: it documents the algorithm faithfully but is not a turn-key pipeline. A complete MNE-Python implementation with:
- `mne.Raw` loader wrapped around BIDS formatted EEG,
- `mne_connectivity` integration for CFC,
- `scipy.optimize.minimize` MLE wrapper,
- canonical UHM $\Phi$ computation (distinct from IIT/`pyphi`),
- CI reporting,
is planned as a separate package `uhm-neurocalib` (release gated on a verified eligible pilot dataset). Until that package is available, independent implementers should use the pseudocode as specification, and file issues/PRs on mismatches to the specification here.

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
| P8.4 | Concordance of verdicts: $\mathrm{Cons}(\hat\Gamma)$ agrees with $\mathrm{PCI}_{\max} > 0.31$ on the same sessions, Cohen's $\kappa \geq 0.8$ (SUB-5; until 2026-09-25: "the $P = 2/7$ transition coincides with PCI $\approx 0.31$", a comparison of unrelated scales) | TMS-EEG + $\pi_{\mathrm{bio}}$ with $\theta$ frozen on wakefulness | $\kappa < 0.4$ |
| P8.5 | $\mathrm{Gap}(L,E) \approx 1$ in alexithymia | Dual interview + EEG | $\mathrm{Gap}(L,E) \ll 1$ with diagnosed alexithymia |
| P8.6 | Critical exponents $\beta = 1/4$ at the sleep-wakefulness transition | EEG monitoring + $\pi_{\mathrm{bio}}$ → $P(\tau)$ near $P_{\mathrm{crit}}$ | Other exponents |

### Position against the substitution argument {#substitution-position}

[Kleiner & Hoel (2021)](https://arxiv.org/abs/2004.03541) distinguish prediction data from reports used to infer experience. Their dependence conditions concern possible physical variations, not the train/test split of a statistical estimator. Their conclusions apply when those conditions and the paper's other assumptions hold. UHM does not establish those premises for all physical systems or solve the philosophical substitution problem by freezing an encoder.

:::tip Conditional claims about calibration [T]; phenomenal bridge [H/I]
**(i) Training agreement is not independent validation.** Using outcome labels to choose an encoder or threshold can improve agreement on that sample. A fitted model need not have 100% accuracy, and fitting does not by itself establish the paper's global strict-dependence condition $o_i=f(o_r)$.

**(ii) A viability penalty can force the tested conclusion.** In the stated uniform toy family $\Gamma=I/7+m(J-I)$, consider $420(m'-m)^2+\lambda_2\max(0,1/7-42m'^2)$, $0\le m<m_c=1/\sqrt{294}$. On $[m,m_c]$ its derivative is $840(m'-m)-84\lambda_2m'$. For $\lambda_2\ge10(1-m/m_c)$ it is nonpositive throughout this interval; beyond $m_c$ only the increasing data loss remains. The global minimizer has $P=2/7$. This proves bias for this specified loss/family, not a theorem about every regularizer or observation model. Confirmatory runs therefore set both theory-bearing weights to zero (SUB-2).

**(iii) Freezing establishes a test protocol, not universal physical independence.** With fixed $\theta$, held-out verdicts are functions of new prediction data without refitting to their reports. This removes that leakage. It does not show that every prediction-data variation is physically possible while reports remain fixed, or rule out confounding, calibration failure or encoder nonidentifiability.

**(iv) A declared test domain remains empirical.** Preregister a population, intervention family, outcomes and calibration range. Held-out concordance tests predictive support within that domain. Calling that domain a case of the paper's lenient dependence requires verifying its physical/statistical premises, not merely observing agreement. Extending a classifier to emulations or language models requires a new bridge; the mathematical gate alone supplies none.
:::

The state predicate is the full [Cap₂ conjunction](/docs/reference/mathematical-kernel#thresholds), with a declared differentiation readout and any additional stress criterion. Identifiable target functionals and uncertainty are required by [ID-A … ID-D](/docs/applied/research/reconstruction-identifiability#confirmatory). Statistical independence, physical substitution and ontological supervenience are distinct assertions.

**The protocol that follows (pre-registration SUB-1 … SUB-6).**
- **SUB-1.** Freeze $\theta$ on wakefulness sessions only (the reference-ensemble normalisation of R4); no NREM, anaesthesia, REM or ketamine label enters the fit.
- **SUB-2.** $\lambda_2 = 0$ in every confirmatory run. $\lambda_1$ (consistency with $\mathcal L_\Omega$) also carries the theory: $\lambda_1 = 0$ in the confirmatory run, other values only as a reported sensitivity analysis.
- **SUB-3.** Phases from the EEG (complex phase-locking values, as in [§9.3 of the fundamental closures](/docs/proofs/categorical/fundamental-closures#pi-bio-protocol)), never from reaction times: reaction times are behaviour, i.e. inference data. $P$, $R$ and $\Phi$ depend only on $|\gamma_{ij}|$ and $\gamma_{ii}$; $D = e^{S}$ depends on the spectrum and hence on the phases.
- **SUB-4.** Register the verdicts of the table in Step 5 before unblinding. The decisive rows are REM and ketamine (consciousness without behaviour at the time): with $\theta$ frozen on wakefulness they are out-of-sample.
- **SUB-5.** Concordance with $\mathrm{PCI}^*$ on the same sessions (P8.4 in concordance form): Cohen's $\kappa$ between $\mathrm{Cons}_\theta$ and $\mathrm{PCI}_{\max} > 0.31$; $\kappa \geq 0.8$ corroborates, $\kappa < 0.4$ falsifies [Pr].
- **SUB-6.** The two exits (Step 5): among sessions with $\mathrm{PCI}_{\max} \leq 0.31$, responses that stay local are predicted to have $\hat\Phi < 1$; responses that spread as a stereotyped global wave, $\hat P > 3/7$ ($\hat R < 1/3$). This compares prediction data with prediction data, so the substitution argument does not touch it — it tests UHM's structure, not its consciousness claim [H].
- **ID-A … ID-D.** Additional requirements: observation model and residual symmetry, informational completeness/conditioning, confidence sets and undetermined verdicts, comparison with alternative encoders — [full statement](/docs/applied/research/reconstruction-identifiability#confirmatory).

**Similarity structure and the declared predicate [H/I with a mathematical independence example].** Kawakita, Zeleznikow-Johnston, Tsuchiya & Oizumi (*Sci. Rep.* 14: 15917, 2024, doi:10.1038/s41598-024-65604-1) aligned colour-similarity structures for 93 colours by Gromov–Wasserstein optimal transport, without labels: GPT-4's structure matched that of colour-neurotypical humans with a matching rate of 91.4 % (GPT-3.5: 11.8 %). In UHM:
- A similarity structure is **inference data** — judgements, i.e. reports. A system that reproduces it is precisely what a substitution preserves; by (iii) it carries no weight for $\mathrm{Cons}$.
- **An eigenframe does not determine a spectrum or the full gate.** Varying eigenvalues in a fixed frame changes purity and can cross its cut. All orthogonal eigenrays have the same pairwise Fubini–Study distance; that geometry alone carries little state information, and degenerate eigenspaces do not select eigenrays uniquely. A full Cap₂ witness must check integration, reflection, differentiation and its chosen stress proxy. A model of reported colour similarity requires an independently calibrated bridge rather than identification with this eigenray geometry.
- What $\mathrm{Cons}$ requires is the system's own $\hat\Gamma$, reconstructed from its internal, interventional data by a protocol validated where ground truth exists. For a language model no such validation exists, and the corpus makes no claim ("no threshold without ground truth" above). The 91.4 % result shows that report-level structure can be shared across radically different systems, which is exactly why UHM does not read consciousness off it.

### Key References {#литература-p8}

1. **Casali et al. (2013)** — PCI: "A theoretically based index of consciousness independent of sensory processing and behavior." *Science Translational Medicine*, 5(198). [PubMed: 23946194](https://pubmed.ncbi.nlm.nih.gov/23946194/)
2. **Pothos-Busemeyer (2022)** — Quantum cognition review. *Annual Review of Psychology*, 73, 749-778.
3. **Butlin et al. (2023/2025)** — "Consciousness in Artificial Intelligence: Insights from the Science of Consciousness." [arXiv: 2308.08708](https://arxiv.org/abs/2308.08708); updated 2025: "Identifying indicators of consciousness in AI systems." *Trends in Cognitive Sciences*.
4. **eLife (2024/2025)** — "Spatiotemporal brain complexity quantifies consciousness outside of perturbation paradigms." [eLife 98920](https://elifesciences.org/articles/98920).
5. **Quantum-inspired EEG (2026)** — "Quantum inspired feature engineering for explainable EEG signal classification." *Scientific Reports*. [Nature](https://www.nature.com/articles/s41598-026-41821-8).
6. **Casarotto et al. (2016)** — "Stratification of unresponsive patients by an independently validated index of brain complexity." *Annals of Neurology* 80(5): 718–729. doi:10.1002/ana.24779 ($\mathrm{PCI}^* = 0.31$; Table 1 above).
7. **Kleiner & Hoel (2021)** — "Falsification and consciousness." *Neuroscience of Consciousness* 2021(1): niab001. doi:10.1093/nc/niab001; arXiv:2004.03541.
8. **Kawakita, Zeleznikow-Johnston, Tsuchiya & Oizumi (2024)** — "Gromov–Wasserstein unsupervised alignment reveals structural correspondences between the color similarity structures of humans and large language models." *Scientific Reports* 14: 15917. doi:10.1038/s41598-024-65604-1.

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

**Mathematical reconstruction foundation:** [ID-1/ID-2 and primary sources](/docs/applied/research/reconstruction-identifiability). For phase measurements: [Tort et al. (2010), PAC measurement](https://doi.org/10.1152/jn.00106.2010) and [Aydore et al. (2013), PLV properties](https://pmc.ncbi.nlm.nih.gov/articles/PMC3674231/).
