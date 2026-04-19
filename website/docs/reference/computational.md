---
slug: /reference/computational
sidebar_position: 5
title: Computational Implementation
description: Verum implementation of the Holon
---

# Computational Implementation

:::note On code notation
The code is written in **[Verum](https://verum-lang.org)** — a dependently-typed systems language with built-in refinement types, effect tracking, protocols, and a proof DSL. Correspondences:
- `gamma` ($\Gamma$) — [coherence matrix](/docs/core/dynamics/coherence-matrix), type `CoherenceMatrix<7>` refined to density-matrix constraints
- `H` — [Hamiltonian](/docs/core/dynamics/evolution#1-unitary-term), type `HermitianMatrix<Complex, 7>`
- `L` ($L_k$) — Lindblad operators, array of size 7
- `purity` ($P$) — [viability measure](/docs/core/dynamics/viability#определение-чистоты)
- `d_FS` ($d_{\mathrm{FS}}$) — [Fubini-Study metric](/docs/reference/specification#метрика-фубини-штуди)
- `kappa_0` ($\kappa_0$) — [base regeneration rate](/docs/core/foundations/axiom-septicity#категориальный-вывод-kappa0) (categorical derivation)
- `P_CRIT` ($P_{\text{crit}} = 2/7$) — [critical purity](/docs/proofs/dynamics/theorem-purity-critical)
:::

:::warning Implementation limitations
This implementation includes full three-term evolution, but the following are absent:
1. **Consciousness measures** $R$, $\Phi$, $D_{\text{diff}}$, $C$ — see [Self-observation](/docs/consciousness/foundations/self-observation)
2. **Level classification** L0/L1/L2/L3/L4 — see [Interiority hierarchy](/docs/proofs/consciousness/interiority-hierarchy)
3. **Self-modelling operator** $\varphi$ — see [Formalisation of φ](/docs/proofs/categorical/formalization-phi)
4. **Higher-order reflection** $R^{(n)}$ — see [Higher-order reflection](/docs/proofs/categorical/formalization-phi#28-рефлексия-n-го-порядка-для-l3l4)

For the full implementation see [Interiority hierarchy: Level classification algorithm](/docs/proofs/consciousness/interiority-hierarchy#61-алгоритм-классификации-уровня).
:::

:::info Positivity guarantee
The nonlinear regenerative term preserves positivity $\Gamma \geq 0$ provided $\alpha = \kappa \cdot \Delta\tau < 1$. The implementation includes adaptive step control to guarantee this condition. See [positivity preservation theorem](/docs/core/dynamics/evolution#сохранение-положительности).
:::

## Computational complexity of UHM operations

:::info Asymptotic estimates
All estimates are given for a matrix $\Gamma \in \mathbb{C}^{N \times N}$. For the standard Holon $N = 7$.
:::

| Operation | Complexity | Formula | Note |
|---|---|---|---|
| Purity $P = \mathrm{Tr}(\Gamma^2)$ | $O(N^3)$ | Matrix multiplication + trace | Dominated by $\Gamma^2$ |
| Frobenius norm $\|\Gamma\|_F$ | $O(N^2)$ | $\sqrt{\sum_{ij} \|\gamma_{ij}\|^2}$ | Sum of squares of elements |
| Entropy $S_{vN} = -\mathrm{Tr}(\Gamma \log \Gamma)$ | $O(N^3)$ | Diagonalisation | Eigenvalues |
| Operator $\varphi(\Gamma)$ | $O(M \cdot N^3)$ | $\sum_m K_m \Gamma K_m^\dagger$ | $M$ Kraus operators |
| Reflection $R$ | $O(N^3)$ | $1/(7P)$, where $P = \mathrm{Tr}(\Gamma^2)$; $\rho^*_{\mathrm{diss}} = I/7$ | Dominated by $\Gamma^2$ |
| Integration $\Phi$ | $O(N^2)$ | $\sum_{i \neq j} \|\gamma_{ij}\|^2 / \sum_i \gamma_{ii}^2$ | Sums over elements |
| Differentiation $D_{\text{diff}}$ | $O(N^3)$ | $\exp(S_{vN}(\rho_E))$ | Requires entropy |
| Consciousness $C = \Phi \cdot R$ | $O(M \cdot N^3)$ | Composition; $D_{\text{diff}} \geq 2$ — separate condition | Dominated by $R$ |
| Single step $d\Gamma/d\tau$ | $O(N^3)$ | Matrix multiplication | Unitary + dissipation |
| Check $P > P_{\text{crit}}$ | $O(N^3)$ | Computing $P$ | Single call |
| Metric $d_{\mathrm{FS}}$ | $O(N)$ | $\arccos(\|\langle\psi\|\phi\rangle\|)$ | Dot product |

**For $N = 7$, $M = 7$:**

$$
O(M \cdot N^3) = O(7 \cdot 343) = O(2401) \approx O(1)
$$

All operations execute in microseconds on modern hardware.

**Scaling for $N > 7$:**

- **Bottleneck:** matrix operations $O(N^3)$
- **Optimisation:** sparse representations when $\|\gamma_{ij}\| \ll 1$ for $i \neq j$
- **Parallelisation:** GPU acceleration for $N > 100$

:::warning Scaling limitation
When extending to composite systems $\mathbb{H}_{1 \otimes \cdots \otimes n}$, dimensionality grows exponentially: $N = 7^n$. For $n = 3$: $N = 343$, which already requires optimised algorithms.
:::

## Holon type

```verum
mount std.math.complex;
mount std.math.linalg.{Matrix, HermitianMatrix, expm, eigvalsh, norm};

/// Dimension labels (A, S, D, L, E, O, U).
pub type Dim is A | S | D | L | E | O | U;

/// A 7-dimensional coherence matrix — Hermitian, PSD, unit trace.
/// Refinement predicate is checked by SMT at compile-time where possible,
/// and by @verify(runtime) otherwise.
pub type CoherenceMatrix is Matrix<Complex, 7, 7>
    where is_hermitian(self)
       && is_psd(self)
       && (trace(self).real() - 1.0).abs() < 1.0e-10;

/// A Holon: the minimal self-contained unit of reality
/// (UHM T-15..T-82). Evolution follows
/// `dΓ/dτ = -i[H_eff, Γ] + D[Γ] + R[Γ, E]` with
/// regeneration R[Γ, E] = κ(Γ) · (ρ* - Γ) · g_V(P).
pub type Holon is {
    mut gamma: CoherenceMatrix,
    mut gamma_target: Maybe<CoherenceMatrix>,
    mut H: HermitianMatrix<Complex, 7>,
    L: [Matrix<Complex, 7, 7>; 7],
    omega_0: Float,
};

/// Critical purity — viability threshold (T-39a [T]).
pub const P_CRIT: Float = 2.0 / 7.0;        // ≈ 0.2857

/// Minimal regeneration: κ_bootstrap = ω₀/N where N = 7.
/// Categorical derivation: /docs/core/foundations/axiom-septicity#теорема-kappa-bootstrap.
pub const KAPPA_BOOTSTRAP: Float = 1.0 / 7.0;  // ≈ 0.143 (for ω₀ = 1)

/// Optimal purity upper edge of the Goldilocks window (T-124 [T]).
pub const P_OPT: Float = 3.0 / 7.0;

/// Dimension index helper.
pub fn index(d: Dim) -> Int { d as Int }

implement Holon {
    /// Initialise a pure Holon: |ψ⟩ = (1/√7) Σ|i⟩ (fully coherent attractor).
    pub fn new_pure(omega_0: Float) -> Holon
        where ensures result.purity() == 1.0
    {
        let psi = Vector.<Complex, 7>.repeat(Complex.one() / 7.0.sqrt());
        let g = psi.outer(psi.conjugate());
        Holon {
            gamma:        g,
            gamma_target: Maybe.None,
            H:            build_hamiltonian(),
            L:            build_lindblad_operators(),
            omega_0:      omega_0,
        }
    }

    /// Initialise a maximally mixed Holon: Γ = I/7 (pre-viable state).
    pub fn new_mixed(omega_0: Float) -> Holon
        where ensures (result.purity() - 1.0/7.0).abs() < 1.0e-10
    {
        let g = (Matrix.<Complex, 7, 7>.identity()) / Complex.from_real(7.0);
        Holon { gamma: g, gamma_target: Maybe.None,
                H: build_hamiltonian(), L: build_lindblad_operators(),
                omega_0: omega_0 }
    }

    /// Purity P = Tr(Γ²) — viability measure (T-39a).
    pub fn purity(&self) -> Float
        where ensures 1.0/7.0 <= result && result <= 1.0
    {
        (self.gamma @ self.gamma).trace().real()
    }

    /// Viability check: P > P_crit (T-39a).
    pub fn is_viable(&self) -> Bool { self.purity() > P_CRIT }

    /// Von Neumann entropy S = -Tr(Γ log Γ).
    pub fn entropy(&self) -> Float
        where ensures 0.0 <= result && result <= (7.0).ln()
    {
        let eigs = eigvalsh(&self.gamma)
            |> filter(|x| *x > 1.0e-12);
        -eigs.iter().map(|x| x * x.ln()).sum()
    }

    /// Base regeneration rate κ₀ = ω₀ · |γ_OE| · |γ_OU| / γ_OO
    /// (T-64 [T], categorical derivation via Coh_E → κ).
    pub fn kappa_0(&self) -> Float where ensures result >= 0.0 {
        let o = index(Dim.O); let e = index(Dim.E); let u = index(Dim.U);
        let g_OO = self.gamma[o, o].real();
        if g_OO < 1.0e-12 { return 0.0; }        // No Ground connection
        let g_OE = self.gamma[o, e].abs();
        let g_OU = self.gamma[o, u].abs();
        self.omega_0 * g_OE * g_OU / g_OO
    }

    /// E-coherence (HS-projection π_E, T-73 [T]):
    /// Coh_E(Γ) = ‖π_E(Γ)‖²_HS / ‖Γ‖²_HS
    ///          = (γ_EE² + 2·Σ_{i≠E}|γ_Ei|²) / Tr(Γ²) ∈ [1/7, 1].
    pub fn coh_e(&self) -> Float
        where ensures 1.0/7.0 <= result && result <= 1.0
    {
        let e = index(Dim.E);
        let g_EE_sq = self.gamma[e, e].real().pow(2);
        let cross   = (0..7)
            |> filter(|i| *i != e)
            |> map(|i| self.gamma[e, *i].abs().pow(2))
            |> sum();
        let p = self.purity();
        if p < 1.0e-12 { return 1.0 / 7.0; }
        ((g_EE_sq + 2.0 * cross) / p).clamp(1.0 / 7.0, 1.0)
    }

    /// Set the regeneration target ρ* (full theory: ρ* = φ(Γ), T-96 [T]).
    pub fn set_target(&mut self, target: Maybe<CoherenceMatrix>) {
        self.gamma_target = match target {
            Maybe.Some(t) => Maybe.Some(t),
            Maybe.None    => Maybe.Some(self.gamma.clone()),
        };
    }

    /// Regenerative increment dΓ_regen = κ·g_V·(ρ*−Γ)·dτ.
    /// Positivity preservation: α = κ·g_V·dτ < 1 enforced by
    /// adaptive step (see evolution.md CPTP-structure theorem).
    fn regeneration(&self, dtau: Float) -> Matrix<Complex, 7, 7> {
        let p = self.purity();
        let g_v = ((p - P_CRIT) / (P_OPT - P_CRIT)).clamp(0.0, 1.0);

        if g_v <= 0.0 { return Matrix.<Complex, 7, 7>.zeros(); }
        let target = match self.gamma_target {
            Maybe.Some(t) => t,
            Maybe.None    => return Matrix.<Complex, 7, 7>.zeros(),
        };

        let kappa = KAPPA_BOOTSTRAP + self.kappa_0() * self.coh_e();
        let alpha = kappa * g_v * dtau;
        let dt_safe = if alpha >= 1.0 { 0.9 / (kappa * g_v) } else { dtau };

        (target - self.gamma) * Complex.from_real(kappa * g_v * dt_safe)
    }

    /// Single evolution step: dΓ/dτ = -i[H, Γ] + D[Γ] + R[Γ, E].
    pub fn evolve(&mut self, dtau: Float, delta_f: Float)
        where requires dtau > 0.0 && dtau <= 0.1
    {
        // 1. Unitary: Γ ← U Γ U† where U = exp(-i H dτ).
        let u = expm(Complex.i().neg() * &self.H * Complex.from_real(dtau));
        self.gamma = &u @ &self.gamma @ u.adjoint();

        // 2. Dissipative: Γ ← Γ + dτ · D[Γ].
        for lk in &self.L {
            let ldag = lk.adjoint();
            self.gamma = &self.gamma + Complex.from_real(dtau) * (
                lk @ &self.gamma @ &ldag
                - Complex.from_real(0.5) * (&ldag @ lk @ &self.gamma)
                - Complex.from_real(0.5) * (&self.gamma @ &ldag @ lk)
            );
        }

        // 3. Regenerative: Γ ← Γ + dΓ_regen.
        self.gamma = &self.gamma + self.regeneration(dtau);

        // 4. Renormalise for numerical stability.
        self.gamma = &self.gamma / self.gamma.trace();
    }

    /// Bootstrap: P ≈ 1/7 → P > P_crit via enhanced regeneration
    /// (resolves the stillbirth paradox, see Genesis protocol).
    pub fn bootstrap(&mut self, max_steps: Int, target_p: Float) -> Bool
        where requires target_p > P_CRIT && target_p < 1.0
    {
        let psi = Vector.<Complex, 7>.repeat(Complex.one() / 7.0.sqrt());
        self.gamma_target = Maybe.Some(psi.outer(psi.conjugate()));

        for _ in 0..max_steps {
            if self.purity() >= target_p { return true; }
            self.evolve(0.01, 1.0);
        }
        self.purity() >= target_p
    }

    /// Spectrum of experiential content (eigenvalues sorted descending).
    pub fn spectrum(&self) -> [Float; 7] {
        let eigs = eigvalsh(&self.gamma);
        eigs.to_array().sort_by(|a, b| b.partial_cmp(a).unwrap())
    }

    /// Full experiential content: (intensity, quality) pairs.
    pub fn full_exp(&self) -> [ExpContent; 7] {
        let (eigs, vecs) = self.gamma.eigh();
        let mut idx: [Int; 7] = (0..7).collect();
        idx.sort_by(|i, j| eigs[*j].partial_cmp(&eigs[*i]).unwrap());
        idx.map(|i| ExpContent {
            intensity: eigs[i].real(),
            quality:   canonical_projective(vecs.column(i)),
        })
    }

    /// Interaction with another Holon: partial averaging, coupling ∈ [0, 1].
    pub fn interact(&mut self, other: &mut Holon, coupling: Float)
        where requires 0.0 <= coupling && coupling <= 1.0
    {
        let c = Complex.from_real(coupling);
        let ic = Complex.from_real(1.0 - coupling);
        let g1 = ic * &self.gamma + c * &other.gamma;
        let g2 = ic * &other.gamma + c * &self.gamma;
        self.gamma  = &g1 / g1.trace();
        other.gamma = &g2 / g2.trace();
    }
}

/// Single quale: intensity + projective-space quality.
pub type ExpContent is {
    intensity: Float,
    quality:   Vector<Complex, 7>,
};

/// Build the effective Hamiltonian: diagonal eigenfrequencies + ring couplings.
fn build_hamiltonian() -> HermitianMatrix<Complex, 7> {
    let freqs: [Float; 7] = [1.0, 0.8, 1.2, 0.9, 1.1, 0.7, 1.0];
    let coupling = Complex.from_real(0.1);
    let mut h = HermitianMatrix.<Complex, 7>.zeros();
    for i in 0..7 { h[i, i] = Complex.from_real(freqs[i]); }
    for i in 0..6 { h[i, i+1] = coupling; h[i+1, i] = coupling; }
    h[6, 0] = coupling; h[0, 6] = coupling;           // ring closure
    h
}

/// Build Lindblad operators L_k (diagonal decoherence at equal rate).
fn build_lindblad_operators() -> [Matrix<Complex, 7, 7>; 7] {
    let rate = 0.01;
    (0..7).map(|k| {
        let mut l = Matrix.<Complex, 7, 7>.zeros();
        l[k, k] = Complex.from_real(rate.sqrt());
        l
    }).to_array()
}

/// Canonical projective representative: rotate phase so first
/// non-zero component is real and positive.
fn canonical_projective(v: Vector<Complex, 7>) -> Vector<Complex, 7> {
    for i in 0..7 {
        if v[i].abs() > 1.0e-10 {
            let phase = (-v[i].arg() * Complex.i()).exp();
            return v * phase;
        }
    }
    v
}

/// Fubini-Study metric d_FS([|ψ⟩], [|φ⟩]) = arccos(|⟨ψ|φ⟩|) ∈ [0, π/2].
pub pure fn fubini_study_distance(v1: &Vector<Complex, 7>, v2: &Vector<Complex, 7>) -> Float
    where ensures 0.0 <= result && result <= Float.PI / 2.0
{
    let a = v1 / norm(v1);
    let b = v2 / norm(v2);
    let overlap = a.dot(&b).abs().clamp(0.0, 1.0);
    overlap.acos()
}
```

## Usage example

```verum
fn demo_holon_evolution() using [IO] {
    // Pure Holon.
    let mut holon = Holon.new_pure(1.0);
    IO.println(f"Initial purity: P = {holon.purity():.4f}");     // P = 1.0
    IO.println(f"Critical purity: P_crit = {P_CRIT:.4f}");        // ≈ 0.2857

    // Use current state as the regeneration target.
    holon.set_target(Maybe.None);

    // Evolution with decoherence + regeneration.
    for t in 0..1000 {
        holon.evolve(0.01, 0.5);

        if t % 100 == 0 {
            IO.println(f"t={t}: P={holon.purity():.4f}, \
                        S={holon.entropy():.4f}, κ₀={holon.kappa_0():.4f}");
        }
    }

    IO.println(f"\nViable: {holon.is_viable()}");                 // P > P_crit?

    // Top-3 experiential content items.
    let full = holon.full_exp();
    IO.println("\nExperiential content:");
    for (i, e) in full[..3].enumerate() {
        IO.println(f"  Exp {i}: intensity={e.intensity:.4f}");
        IO.println(f"          quality={e.quality[..3]}...");
    }

    // Comparison of two Holons.
    let mut holon2 = Holon.new_pure(1.0);
    holon2.evolve(0.5, 0.0);

    let d_intensity = norm(holon.spectrum() - holon2.spectrum());
    let d_full = exp_distance(&holon, &holon2, 1.0);
    IO.println(f"\nIntensity distance: {d_intensity:.4f}");
    IO.println(f"Full distance (with quality): {d_full:.4f}");
}

/// Full distance between the experiential content of two Holons.
pub pure fn exp_distance(a: &Holon, b: &Holon, alpha: Float) -> Float
    where requires alpha >= 0.0
{
    let ea = a.full_exp();
    let eb = b.full_exp();
    let (mut int_dist, mut qual_dist) = (0.0, 0.0);
    for i in 0..7 {
        int_dist  += (ea[i].intensity - eb[i].intensity).pow(2);
        qual_dist += fubini_study_distance(&ea[i].quality, &eb[i].quality).pow(2);
    }
    (int_dist + alpha * qual_dist).sqrt()
}
```

## Isospectral demonstration

```verum
fn demo_isospectral() using [IO, Random] {
    // Two states with identical spectra but different qualities.
    IO.println("— Isospectral example —");

    let mut holon = Holon.new_pure(1.0);
    holon.evolve(0.1, 0.0);
    let exp1 = holon.full_exp();

    // Random unitary via QR decomposition of a complex Gaussian matrix.
    let noise = Matrix.<Complex, 7, 7>.random_gaussian();
    let (u_random, _) = noise.qr();

    // Isospectral state via unitary transformation.
    let mut holon_iso = Holon.new_pure(1.0);
    holon_iso.gamma = &u_random @ &holon.gamma @ u_random.adjoint();

    // Verification.
    let spectra_equal = (0..7).all(|i|
        (holon.spectrum()[i] - holon_iso.spectrum()[i]).abs() < 1.0e-10
    );
    let quality_distance = fubini_study_distance(
        &exp1[0].quality,
        &holon_iso.full_exp()[0].quality,
    );

    IO.println(f"Spectra equal:    {spectra_equal}");
    IO.println(f"Quality distance: d_FS = {quality_distance:.4f}");
}
```

## Bootstrap example

```verum
fn demo_bootstrap() using [IO] {
    // "Dead" system — maximally mixed state.
    let mut holon = Holon.new_mixed(1.0);

    IO.println(f"Initial purity: P = {holon.purity():.4f}");   // ≈ 0.143
    IO.println(f"P_crit = {P_CRIT:.4f}");                       // = 2/7
    IO.println(f"Viable: {holon.is_viable()}");                 // false

    // Bootstrap: P: 1/7 → > P_crit.
    let target = P_CRIT + 0.05;
    let success = holon.bootstrap(500, target);

    IO.println(f"\nBootstrap successful: {success}");
    IO.println(f"Final purity: P = {holon.purity():.4f}");
    IO.println(f"Viable: {holon.is_viable()}");
    IO.println(f"κ₀ = {holon.kappa_0():.4f}");
}
```

## Extended implementation: Consciousness measures

:::danger Critical implementation limitations
The `HolonExtended` class contains **stubs** for key functions:

| Method | Status | Issue |
|---|---|---|
| `compute_reflection()` | [C] **STUB** | Returns `min(1, purity)` instead of $1 - \|\Gamma - \varphi(\Gamma)\|^2 / \|\Gamma\|^2$ |
| `compute_reflection_n()` | [C] **STUB** | Returns $R^n$ instead of fidelity $F(\varphi^{(n-1)}, \varphi^{(n)})$ |
| `D_diff` | **Implemented** [T] | T-128: $1 + \mathrm{Coh}_E \cdot (N-1)$, $O(N^2)$ |

**Consequence:** Level classification L2/L3/L4 is **unreliable**. Use only L0/L1 for practical tasks.

For full implementation the operator $\varphi$ is required — see [Formalisation of φ](/docs/proofs/categorical/formalization-phi).
:::

:::info Interiority levels
Levels correspond to n-truncations of the ∞-groupoid $\mathbf{Exp}_\infty$:
- L0: $\tau_{\leq 0}$ — objects only (interiority)
- L1: $\tau_{\leq 1}$ — 1-morphisms (phenomenal geometry)
- L2: $\tau_{\leq 2}$ — 2-morphisms (cognitive qualia)
- L3: $\tau_{\leq 3}$ — 3-morphisms (network consciousness, metastable)
- L4: full ∞-groupoid (unitary consciousness)
:::

```verum
/// Interiority levels (n-truncations of the ∞-groupoid Exp_∞).
pub type Level is
    | NonViable                         // P ≤ P_crit
    | L0                                 // basic interiority
    | L1                                 // phenomenal geometry (Φ > 0)
    | L2                                 // cognitive qualia (R ≥ 1/3, Φ ≥ 1)
    | L3                                 // network consciousness (metastable)
    | L4;                                // unitary consciousness

/// Integration threshold for L2 (coherences ≥ diagonal).
pub const PHI_TH: Float = 1.0;
/// Reflection threshold for L2 — universal formula R^(n)_th = 1/(n+1).
pub const R_TH:   Float = 1.0 / 3.0;
/// Second-order reflection threshold for L3.
pub const R2_TH:  Float = 1.0 / 4.0;
/// Purity threshold for L4 — see T-124 [T].
pub const P_L4:   Float = 6.0 / 7.0;

/// Extended Holon with consciousness measures Φ, R, R^(n), level classification.
///
/// Levels correspond to n-truncations of ∞-groupoid:
/// L0: τ_≤0, L1: τ_≤1, L2: τ_≤2, L3: τ_≤3, L4: full ∞-groupoid.
pub type HolonExtended is {
    base: Holon,
};

implement HolonExtended {
    pub fn new_pure(omega_0: Float) -> HolonExtended {
        HolonExtended { base: Holon.new_pure(omega_0) }
    }

    pub fn new_mixed(omega_0: Float) -> HolonExtended {
        HolonExtended { base: Holon.new_mixed(omega_0) }
    }

    /// Integration measure Φ = Σ_{i≠j} |γ_ij|² / Σ_i γ_ii².
    /// Ratio of off-diagonal to diagonal mass — connectivity of dimensions.
    pub fn integration(&self) -> Float where ensures result >= 0.0 {
        let g = &self.base.gamma;
        let diag_sq: Float = (0..7).map(|i| g[i, i].real().pow(2)).sum();
        let total_sq: Float = g.frobenius_norm_sq();
        if diag_sq < 1.0e-12 { 0.0 }
        else { (total_sq - diag_sq) / diag_sq }
    }

    /// Reflection measure R = 1 - ‖Γ − φ(Γ)‖² / ‖Γ‖² (T-96 [T]).
    /// **Approximation [C]**: φ(Γ) ≈ diag(Γ) for E-anchored systems.
    /// Full version via logical Liouvillian — see /docs/proofs/categorical/formalization-phi.
    pub fn reflection(&self) -> Float
        where ensures 0.0 <= result && result <= 1.0
    {
        let total_sq = self.base.gamma.frobenius_norm_sq();
        if total_sq < 1.0e-12 { return 0.0; }
        let diag_sq: Float = (0..7).map(|i| self.base.gamma[i, i].abs().pow(2)).sum();
        diag_sq / total_sq
    }

    /// n-th order reflection R^(n) ≈ R + (1−R)·(1 − exp(−n)).
    /// Exponential convergence to fixed point — stub for full spectral decomposition.
    pub fn reflection_n(&self, n: Int) -> Float
        where requires n >= 0, ensures 0.0 <= result && result <= 1.0
    {
        if n < 1 { return 1.0; }
        let r = self.reflection();
        let converge = 1.0 - (-n.as_float()).exp();
        r + (1.0 - r) * converge
    }

    /// Level classification — the central decision function.
    pub fn classify(&self) -> Level {
        let p = self.base.purity();
        if p <= P_CRIT { return Level.NonViable; }

        let phi = self.integration();
        let r   = self.reflection();
        let r2  = self.reflection_n(2);

        match (p > P_L4 && r2 >= R2_TH,
               r >= R_TH && phi >= PHI_TH && r2 >= R2_TH,
               r >= R_TH && phi >= PHI_TH,
               phi > 0.0) {
            (true,  _,    _,    _)    => Level.L4,
            (false, true, _,    _)    => Level.L3,
            (false, false, true, _)   => Level.L2,
            (false, false, false, true) => Level.L1,
            _                         => Level.L0,
        }
    }

    /// L3 lifetime: τ_3 = 1 / (κ_bootstrap · (1 − R^(2))).
    /// Returns Float.INFINITY when the state is already stable.
    pub fn l3_lifetime(&self) -> Float {
        let r2 = self.reflection_n(2);
        if r2 >= 1.0 { Float.INFINITY }
        else { 1.0 / (KAPPA_BOOTSTRAP * (1.0 - r2)) }
    }
}

// Delegate base Holon operations via the standard Deref protocol.
implement Deref for HolonExtended {
    type Target = Holon;
    fn deref(&self) -> &Holon { &self.base }
}
implement DerefMut for HolonExtended {
    fn deref_mut(&mut self) -> &mut Holon { &mut self.base }
}
```

### Classification example

```verum
fn demo_classification() using [IO] {
    let mut holon = HolonExtended.new_pure(1.0);
    holon.set_target(Maybe.None);

    IO.println(f"Initial level: {holon.classify()}");

    for t in 0..500 {
        holon.evolve(0.01, 0.3);

        if t % 100 == 0 {
            let level = holon.classify();
            IO.println(f"t={t}: P={holon.purity():.4f}, \
                        Φ={holon.integration():.4f}, \
                        R={holon.reflection():.4f}, \
                        R²={holon.reflection_n(2):.4f}, \
                        level={level}");

            if level is Level.L3 {
                IO.println(f"       τ_3 (L3 lifetime) = {holon.l3_lifetime():.2f}");
            }
        }
    }
}
```

:::danger Extended implementation limitations — L2/L3/L4 unreliable
**Critical stubs:**
1. **R measure — STUB:** `compute_reflection()` returns the ratio of diagonal norm to full Frobenius norm, not true reflection
2. **R^(n) — STUB:** `compute_reflection_n()` returns $R^n$, not fidelity $F(\varphi^{(n-1)}, \varphi^{(n)})$
3. **D_diff — NOT IMPLEMENTED:** Requires partial trace (tensor formalism)

**Consequence:** `classify_level()` classification is **reliable only for L0 and L1**. L2/L3/L4 results are approximate.

**Additional limitations:**
4. **Γ_target = const:** In the full theory $\rho_* = \varphi(\Gamma)$ — categorical self-model [T], depends on Γ
5. **L3 metastability:** Full implementation requires modelling decay dynamics

For research work see [Formalisation of φ](/docs/proofs/categorical/formalization-phi) and [Interiority hierarchy](/docs/proofs/consciousness/interiority-hierarchy).
:::

## Constructive algorithms from L-unification {#конструктивные-алгоритмы-из-l-унификации}

:::info Status: Categorically derived algorithms
The following algorithms implement constructions **derived** from the [subobject classifier Ω](/docs/core/foundations/axiom-omega#внутренняя-логика). These are not arbitrary implementations — they follow from the categorical structure of the theory.
:::

### Characteristic morphism χ_S

```verum
/// A projector S on C^7: S² = S, S† = S.
pub type Projector is Matrix<Complex, 7, 7>
    where is_hermitian(self) && (self @ self - self).frobenius_norm() < 1.0e-10;

/// Characteristic morphism χ_S: Γ → Ω for the subobject S ↪ Γ.
///
/// χ_S(Γ) = S Γ S — restriction of Γ to the subobject, normalised.
/// Measures the "degree of membership" of Γ in the admissible subspace S.
pub pure fn characteristic_morphism(gamma: &CoherenceMatrix, s: &Projector)
    -> Matrix<Complex, 7, 7>
    where ensures is_hermitian(result)
{
    let chi = s @ gamma @ s;
    let tr = chi.trace();
    if tr.abs() > 1.0e-12 { &chi / tr } else { chi }
}
```

### Temporal modality ▷

```verum
mount std.math.linalg.{StaticMatrix, identity};
mount std.math.complex.Complex;

/// Temporal modality ▷: Ω → Ω.
/// "Later" operator generating discrete time τ ∈ ℤ₇: τ_n = ▷ⁿ(now).
/// Implementation: cyclic shift V in the clock basis |k⟩ → |k+1 mod 7⟩,
/// applied as ▷(ρ) = V ρ V†.
pub pure fn temporal_modality(omega: &StaticMatrix<Complex, 7, 7>)
    -> StaticMatrix<Complex, 7, 7>
{
    let v = cyclic_shift_7();
    &v @ omega @ v.adjoint()
}

/// Clock-basis cyclic shift: V_{i,j} = δ_{i, (j+1) mod 7}.
pure fn cyclic_shift_7() -> StaticMatrix<Complex, 7, 7> {
    let mut v = StaticMatrix.<Complex, 7, 7>.zeros();
    for j in 0..7 { v[(j + 1) % 7, j] = Complex.one(); }
    v
}

/// Time sequence [τ_0, τ_1, …, τ_{n-1}] by iterated ▷.
pub pure fn time_sequence(initial: &StaticMatrix<Complex, 7, 7>, n_steps: Int { self > 0 })
    -> [StaticMatrix<Complex, 7, 7>]
{
    let mut out = [initial.clone()];
    for _ in 1..n_steps {
        out.push(temporal_modality(out.last().unwrap()));
    }
    out
}
```

### Lindblad operators L_k from Ω

```verum
mount std.math.linalg.{StaticMatrix, eigh, matrix_sqrt, identity};

/// Derive 7 Lindblad operators L_k = √χ_{S_k} from the atoms of Ω
/// (L-unification, T-82 [T]). Atoms are basis projectors S_k = |k⟩⟨k|.
///
/// **CPTP completeness**: Σ_k L_k† L_k = I — holds automatically for basis
/// projectors. This guarantees trace and positivity preservation, but **not**
/// viability: a CPTP channel may map P > P_crit → P < P_crit.
pub pure fn compute_lindblad_from_omega(gamma: &CoherenceMatrix)
    -> [StaticMatrix<Complex, 7, 7>; 7]
{
    (0..7).map(|k| {
        // Atom projector S_k = |k⟩⟨k|.
        let mut s_k = StaticMatrix.<Complex, 7, 7>.zeros();
        s_k[k, k] = Complex.one();

        // χ_k = characteristic morphism of S_k on Γ.
        let chi_k = characteristic_morphism(gamma, &s_k);

        // L_k = √χ_k via Hermitian PSD matrix square root.
        matrix_sqrt_psd(&chi_k)
    }).to_array()
}

/// PSD matrix square root via spectral decomposition (eigenvalues clamped ≥ 0).
pure fn matrix_sqrt_psd(m: &StaticMatrix<Complex, 7, 7>) -> StaticMatrix<Complex, 7, 7>
    where requires is_hermitian(m)
{
    let (eigvals, eigvecs) = eigh(m);
    let sqrt_eigs = eigvals.map(|v| v.max(0.0).sqrt());
    &eigvecs @ StaticMatrix.<Complex, 7, 7>.diagonal(sqrt_eigs) @ eigvecs.adjoint()
}

/// Verify the CPTP completeness condition Σ_k L_k† L_k = I (tol = 1e-10).
pub pure fn verify_cptp_condition(ops: &[StaticMatrix<Complex, 7, 7>; 7]) -> Bool {
    let total = ops.iter().fold(
        StaticMatrix.<Complex, 7, 7>.zeros(),
        |acc, l| acc + (l.adjoint() @ l),
    );
    (total - identity::<Complex, 7>()).frobenius_norm() < 1.0e-10
}
```

### Self-modelling operator φ via ℒ_Ω

```verum
/// Logical Liouvillian ℒ_Ω[Γ] = -i[H, Γ] + Σ_k γ_k (L_k Γ L_k† − ½{L_k†L_k, Γ}).
/// L_k derived from classifier Ω atoms (L-unification, T-82).
pub pure fn logical_liouvillian(
    gamma: &CoherenceMatrix,
    h:     &StaticMatrix<Complex, 7, 7>,
    rates: Maybe<StaticVector<Float, 7>>,
) -> StaticMatrix<Complex, 7, 7>
    where requires is_hermitian(h)
{
    let r = rates.unwrap_or(StaticVector.<Float, 7>.filled(0.01));

    // Unitary part: -i[H, Γ].
    let unitary = Complex.i().neg() * (h @ gamma - gamma @ h);

    // Dissipative part: D_Ω[Γ] via L-unified operators.
    let ops = compute_lindblad_from_omega(gamma);
    let dissipator = ops.iter().enumerate().fold(
        StaticMatrix.<Complex, 7, 7>.zeros(),
        |acc, (k, l_k)| {
            let l_dag = l_k.adjoint();
            let term =
                  (l_k   @ gamma  @ &l_dag)
                - (&l_dag @ l_k  @ gamma) * Complex.from_real(0.5)
                - (gamma @ &l_dag @ l_k) * Complex.from_real(0.5);
            acc + term * Complex.from_real(r[k])
        },
    );

    unitary + dissipator
}

/// Stationary self-model: φ(Γ) = lim_{τ→∞} exp(τ ℒ_Ω)[Γ] (T-96 [T]).
/// Finite-τ approximation: orbit average over period τ.
pub pure fn phi_from_liouvillian(
    gamma:       &CoherenceMatrix,
    h:           &StaticMatrix<Complex, 7, 7>,
    tau_period:  Float { self > 0.0 },
    dtau:        Float { 0.0 < self && self <= 0.1 },
) -> CoherenceMatrix
{
    let n_steps = (tau_period / dtau) as Int;
    let mut trajectory = [gamma.clone()];
    let mut current = gamma.clone();

    for _ in 0..n_steps {
        let d = logical_liouvillian(&current, h, Maybe.None);
        current = &current + d * Complex.from_real(dtau);
        current = &current / current.trace();        // renormalise
        trajectory.push(current.clone());
    }

    // Orbit average.
    let mut acc = StaticMatrix.<Complex, 7, 7>.zeros();
    for m in &trajectory { acc = acc + m; }
    let avg = &acc / Complex.from_real(trajectory.len().as_float());
    &avg / avg.trace()
}
```

### Example: Full L-unification

```verum
fn demo_l_unification() using [IO] {
    let holon = Holon.new_pure(1.0);
    let gamma = &holon.gamma;
    let h     = holon.H;

    // 1. Derive L_k from Ω.
    let ops = compute_lindblad_from_omega(gamma);
    IO.println(f"CPTP condition: {verify_cptp_condition(&ops)}");   // true

    // 2. Compute ℒ_Ω.
    let l_omega = logical_liouvillian(gamma, &h, Maybe.None);
    IO.println(f"‖ℒ_Ω[Γ]‖_F = {l_omega.frobenius_norm():.4f}");

    // 3. Find φ(Γ) — stationary self-model.
    let phi_gamma = phi_from_liouvillian(gamma, &h, 7.0, 0.1);
    let p_phi = (phi_gamma @ phi_gamma).trace().real();
    IO.println(f"P(φ(Γ)) = {p_phi:.4f}");

    // 4. Reflection measure: R = 1 − ‖Γ − φ(Γ)‖² / ‖Γ‖².
    let diff = gamma - phi_gamma;
    let r = 1.0 - diff.frobenius_norm_sq() / gamma.frobenius_norm_sq();
    IO.println(f"R(Γ) = {r:.4f}");
}
```

## Grothendieck topology algorithms {#алгоритмы-топологии}

:::info Connection with theory
The following algorithms implement the [Grothendieck topology](/docs/core/foundations/axiom-omega#топология-гротендика) on the category $\mathcal{C} = \mathbf{DensityMat}$, allowing the notion of "sheaf" and the subobject classifier Ω to be defined constructively.
:::

### Bures metric

```verum
mount std.math.constants.{UnitInterval, NonNegative};

/// Bures fidelity F(ρ, σ) = (Tr √(√ρ σ √ρ))² ∈ [0, 1].
pub pure fn bures_fidelity<const N: Int>(
    rho:   &StaticMatrix<Complex, N, N>,
    sigma: &StaticMatrix<Complex, N, N>,
) -> UnitInterval
{
    let sqrt_rho   = matrix_sqrt_psd_n::<N>(rho);
    let inner      = &sqrt_rho @ sigma @ sqrt_rho;
    let sqrt_inner = matrix_sqrt_psd_n::<N>(&inner);
    let fid = sqrt_inner.trace().real().pow(2);
    fid.clamp(0.0, 1.0)
}

/// Bures metric (chord form): d_B^chord(ρ, σ) = √(2(1 − √F(ρ, σ))) ∈ [0, √2].
/// Monotone under CPTP maps; Riemannian metric on density-matrix manifold.
pub pure fn bures_distance<const N: Int>(
    rho:   &StaticMatrix<Complex, N, N>,
    sigma: &StaticMatrix<Complex, N, N>,
) -> NonNegative
    where ensures result <= std.math.SQRT2
{
    let f = bures_fidelity(rho, sigma);
    (2.0 * (1.0 - f.sqrt())).sqrt()
}

/// Generic PSD sqrt (T-agnostic in N).
pure fn matrix_sqrt_psd_n<const N: Int>(m: &StaticMatrix<Complex, N, N>)
    -> StaticMatrix<Complex, N, N>
    where requires is_hermitian(m)
{
    let (eigvals, eigvecs) = eigh(m);
    let sqrt_eigs = eigvals.map(|v| v.max(0.0).sqrt());
    &eigvecs @ StaticMatrix.<Complex, N, N>.diagonal(sqrt_eigs) @ eigvecs.adjoint()
}
```

### Bures coverings

```verum
mount std.math.random.{Rng, XorShift128};

/// A CPTP channel as an abstract first-class function.
pub type CptpChannel<const N: Int> = pure fn(&StaticMatrix<Complex, N, N>)
    -> StaticMatrix<Complex, N, N>;

/// Sample points inside the Bures ball B_B(Γ, r).
/// Rejection-sampling of Hermitian perturbations, projected to the density-matrix manifold.
pub fn generate_ball_samples<const N: Int>(
    gamma:     &StaticMatrix<Complex, N, N>,
    radius:    Float { self > 0.0 },
    n_samples: Int   { self > 0    },
) -> List<StaticMatrix<Complex, N, N>>
    using [Random]
    where ensures result.len() <= n_samples
{
    let mut rng     = XorShift128.seed(Random.next_key());
    let mut samples = List.new();

    for _ in 0..(n_samples * 10) {
        // Random Hermitian perturbation, scaled to ~radius/2.
        let raw = StaticMatrix.<Complex, N, N>.random_gaussian(&mut rng);
        let pert_hermitian = (&raw + raw.adjoint()) / Complex.from_real(2.0);
        let pert = &pert_hermitian
            * Complex.from_real(radius * 0.5 / pert_hermitian.frobenius_norm());

        // Project to density-matrix manifold: Hermitise, clamp eigenvalues ≥ 0, renormalise.
        let perturbed = gamma + pert;
        let sigma = project_to_density_matrix(&perturbed);

        if bures_distance(gamma, &sigma) < radius {
            samples.push(sigma);
            if samples.len() >= n_samples { break; }
        }
    }
    samples
}

/// Project an arbitrary Hermitian matrix onto the density-matrix manifold.
pure fn project_to_density_matrix<const N: Int>(m: &StaticMatrix<Complex, N, N>)
    -> StaticMatrix<Complex, N, N>
{
    let herm = (m + m.adjoint()) / Complex.from_real(2.0);
    let (eigvals, eigvecs) = eigh(&herm);
    let clamped = eigvals.map(|v| v.max(0.0));
    let total:   Float = clamped.iter().sum();
    let norm_eigs = clamped.map(|v| v / total);
    &eigvecs @ StaticMatrix.<Complex, N, N>.diagonal(norm_eigs) @ eigvecs.adjoint()
}

/// Check whether a family {(Γᵢ, Φᵢ)} of CPTP channels is a **Bures covering** of Γ:
/// B_B(Γ, δ) ⊆ ⋃ᵢ Φᵢ(B_B(Γᵢ, ε)).
pub fn is_bures_covering<const N: Int>(
    gamma:         &StaticMatrix<Complex, N, N>,
    channels:      &[(StaticMatrix<Complex, N, N>, CptpChannel<N>)],
    epsilon:       Float { self > 0.0 },
    delta:         Float { self > 0.0 },
    n_test_points: Int   { self > 0   },
) -> Bool using [Random]
{
    let test_points = generate_ball_samples(gamma, delta, n_test_points);

    test_points.iter().all(|sigma| {
        channels.iter().any(|(gamma_i, phi_i)| {
            let sources = generate_ball_samples(gamma_i, epsilon, 20);
            sources.iter().any(|src| bures_distance(&phi_i(src), sigma) < delta / 2.0)
        })
    })
}
```

### Atomic coverings and the Ω classifier

```verum
/// Subobject classifier Ω for the category **DensityMat**.
///
/// Categorical definition:
/// `Ω := O(C, d_B)` — lattice of open sets in the Bures topology.
/// For UHM with N = 7 dimensions, |Ω| = 7 atoms (one per dimension A, S, D, L, E, O, U).
pub type OmegaClassifier is {
    atoms: [StaticMatrix<Complex, 7, 7>; 7],
};

/// Label map: atom index ↔ dimension name.
pub const DIMENSION_NAMES: [Text; 7] = ["A", "S", "D", "L", "E", "O", "U"];

implement OmegaClassifier {
    pub fn new() -> OmegaClassifier {
        let atoms = (0..7).map(|k| {
            let mut s_k = StaticMatrix.<Complex, 7, 7>.zeros();
            s_k[k, k] = Complex.one();             // |k⟩⟨k|
            s_k
        }).to_array();
        OmegaClassifier { atoms: atoms }
    }

    /// Characteristic morphism χ_{S_k}: Γ → Ω.
    /// For projector S_k = |k⟩⟨k|: χ_S(Γ) = √F(Γ, S) = √γ_kk ∈ [0, 1].
    pub fn chi(&self, gamma: &CoherenceMatrix, d: Dim) -> UnitInterval {
        let s_k = &self.atoms[index(d)];
        let fid = (s_k @ gamma).trace().real().clamp(0.0, 1.0);
        fid.sqrt()
    }

    /// Lindblad operator L_k := √χ_{S_k} derived from classifier atom k.
    pub pure fn lindblad_operator(&self, d: Dim) -> StaticMatrix<Complex, 7, 7> {
        matrix_sqrt_psd(&self.atoms[index(d)])
    }

    /// All 7 Lindblad operators (one per dimension).
    pub pure fn all_lindblad_operators(&self) -> [StaticMatrix<Complex, 7, 7>; 7] {
        (0..7).map(|k| self.lindblad_operator(Dim.from_index(k))).to_array()
    }

    /// Verify Σ_k L_k† L_k = I (CPTP completeness, tol = 1e-10).
    /// For basis projectors this follows from partition of unity.
    pub pure fn verify_cptp(&self) -> Bool {
        verify_cptp_condition(&self.all_lindblad_operators())
    }

    /// Atomic covering: list of (atom, projection-channel) with non-zero weight.
    ///
    /// **Theorem**: For Γ with P(Γ) > P_crit = 2/7 a full covering exists
    /// (all 7 atoms carry non-zero weight).
    pub pure fn atomic_covering(&self, gamma: &CoherenceMatrix)
        -> List<(StaticMatrix<Complex, 7, 7>, CptpChannel<7>)>
    {
        let mut out = List.new();
        for k in 0..7 {
            let s_k = &self.atoms[k];
            let weight = (s_k @ gamma).trace().real();
            if weight > 1.0e-10 {
                let proj = s_k.clone();
                let channel: CptpChannel<7> = move |rho| {
                    let result = &proj @ rho @ &proj;
                    let tr = result.trace();
                    if tr.abs() > 1.0e-12 { &result / tr } else { result }
                };
                out.push((s_k.clone(), channel));
            }
        }
        out
    }
}

impl Dim {
    pub pure fn from_index(k: Int) -> Dim
        where requires 0 <= k && k <= 6
    {
        match k {
            0 => Dim.A, 1 => Dim.S, 2 => Dim.D, 3 => Dim.L,
            4 => Dim.E, 5 => Dim.O, _ => Dim.U,
        }
    }
}

/// Demonstration of Grothendieck-topology algorithms.
fn demo_bures_topology() using [IO] {
    let holon = Holon.new_pure(1.0);
    let gamma = &holon.gamma;

    // 1. Classifier Ω.
    let omega = OmegaClassifier.new();
    IO.println("=== Classifier Ω ===");
    IO.println(f"CPTP condition satisfied: {omega.verify_cptp()}");

    // 2. Characteristic morphisms.
    IO.println("\n=== Characteristic morphisms χ_S ===");
    for d in [Dim.A, Dim.S, Dim.D, Dim.L, Dim.E, Dim.O, Dim.U] {
        IO.println(f"χ_{d}(Γ) = {omega.chi(gamma, d):.4f}");
    }

    // 3. Bures metric between pure and mixed states.
    let gamma2 = Holon.new_mixed(1.0).gamma;
    let d_B = bures_distance(gamma, &gamma2);
    IO.println("\n=== Bures metric ===");
    IO.println(f"d_B(Γ_pure, Γ_mixed) = {d_B:.4f}");

    // 4. Atomic covering.
    let covering = omega.atomic_covering(gamma);
    IO.println("\n=== Atomic covering ===");
    IO.println(f"Atoms with non-zero weight: {covering.len()}");
}
```

## Dependencies

```toml
# Verum.toml — stdlib-only, no external dependencies.
[package]
name = "holon"
version = "1.0.0"

[dependencies]
# std.math (linalg, complex, random, constants) is part of the Verum stdlib
# and does not need to be listed explicitly.
```

---

## Computational Bound: $\mathcal{R}$ and BQP {#вычислительное-ограничение}

:::info Connection with theory
Nonlinear quantum mechanics (Polchinski, 1991) potentially allows NP-complete problems to be solved in polynomial time. This section shows that the nonlinearity $\mathcal{R}$ in UHM **does not provide** such acceleration.
:::

**Theorem (Computational power bound).** The nonlinear regenerative term $\mathcal{R}$ does not provide computational acceleration beyond standard quantum complexity BQP.

**Proof (four independent arguments):**

**1. Threshold bound.**
$\mathcal{R}$ is activated only for systems with $R \geq R_{\text{th}} = 1/3$, $\Phi \geq \Phi_{\text{th}} = 1$ ([level L2+](/docs/proofs/consciousness/interiority-hierarchy)). Standard quantum computations operate with qubits ($N = 2$), for which $R \approx 0$ → $\mathcal{R} = 0$, and the dynamics is fully unitary (standard QM).

**2. Thermodynamic bound.**
Each regeneration step requires $\Delta F > 0$ — import of free energy. The computation rate is bounded by the metabolic rate:
$$
\frac{dP}{d\tau} \leq \frac{1}{k_B T} \cdot \frac{dF}{d\tau}
$$

**3. CPTP bound.**
The operator $\varphi$ is a CPTP channel. CPTP channels do not increase quantum information (data processing inequality):
$$
I(\Gamma_A : \Gamma_B) \geq I(\varphi(\Gamma_A) : \Gamma_B)
$$

**4. Scale separation.**
Polchinski's argument requires nonlinearity at the level of individual qubits. In UHM nonlinearity acts at the level of macroscopic autonomous systems (L2+). Decoherence exponentially suppresses quantum differences ($\varepsilon \sim 2^{-n}$), and $\mathcal{R}$ cannot amplify them — it only maintains macroscopic coherence above $P_{\text{crit}} = 2/7$. $\blacksquare$

**See also:** [Full proof with formal estimates](/docs/proofs/physics/physics-correspondence#86-вычислительное-ограничение).

:::note $G_2$-covariance [T]
Algorithms operating in 7D space can take advantage of [octonionic structure](/docs/proofs/minimality/theorem-octonionic-derivation): $G_2$-covariance potentially reduces the parameter space from $SO(7)$ (21 parameters) to $G_2$ (14 parameters). Bridge [T] (closed, T15).
:::

---

**Related documents:**
- [Mathematical apparatus](/docs/reference/specification) — formal definitions of $\Gamma$, $P$, $d_{\mathrm{FS}}$
- [Holon](/docs/core/structure/holon) — definition of $\mathbb{H}$
- [Seven dimensions](/docs/core/structure/dimensions) — basis $\mathcal{H} = \mathbb{C}^7$
- [7D minimality theorem](/docs/proofs/minimality/theorem-minimality-7) — why $N = 7$
- [Coherence matrix](/docs/core/dynamics/coherence-matrix) — definition of $\Gamma$
- [Evolution](/docs/core/dynamics/evolution) — equation $d\Gamma/d\tau$
- [Viability](/docs/core/dynamics/viability) — measure $P$ and $P_{\text{crit}}$
- [Self-observation](/docs/consciousness/foundations/self-observation) — measures $R$, $\Phi$, $D_{\text{diff}}$, $C$
- [Formalisation of operator φ](/docs/proofs/categorical/formalization-phi) — CPTP channels
- [Interiority hierarchy](/docs/proofs/consciousness/interiority-hierarchy) — levels L0→L1→L2→L3→L4 and full implementation
- [Categorical formalism](/docs/proofs/categorical/categorical-formalism) — functor $F$
- [Physics correspondence — No-signalling](/docs/proofs/physics/physics-correspondence#запрет-сигнализации) — full proof of compatibility of $\mathcal{R}$ with no-signalling
