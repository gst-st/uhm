---
sidebar_position: 4
title: "The Gap Lattice Model and Quantum Gravity"
slug: /physics/gravity/quantum-gravity
description: "Finite-lattice partition integral on (S¹)²¹ (T-37, T-66), conditional spectral action on a supplied 4D spin manifold (T-65), cutoff convention, and CLPW observer-algebra reparametrization (T-348)."
---

# The Gap Lattice Model and Quantum Gravity

This chapter separates mathematically proved finite-lattice and heat-kernel statements from open problems in quantum gravity: (i) finiteness of a lattice phase integral at fixed finite size (`T-37`, `T-66`), (ii) the conditional Einstein–Hilbert term from the spectral action on an externally supplied 4D Riemannian spin manifold (`T-65`), (iii) Wald entropy and why Hawking's temperature formula is not derived from UHM, and (iv) the Type $\mathrm{II}_1$ de Sitter observer-algebra reparametrization (`T-348`).

:::info Scope
At fixed finite lattice size $N$, integrating a bounded measurable integrand over the compact torus $(S^1)^{21N}$ yields a finite partition function (`T-37 [T]`, `T-66 [T at fixed finite N]`). Existence of a continuum limit, ultraviolet finiteness of gravity, and derivation of a dynamical metric remain open `[Pr]`.
:::

---

## 1. Formal Continuum Action vs. Lattice Definition {#функциональный-интеграл}

Writing a continuum phase integral

$$
Z = \int \mathcal{D}[\theta_{ij}] \, e^{-S_{\mathrm{Gap}}[\theta]}, \qquad
S_{\mathrm{Gap}} = \int d^4x \sqrt{-g[\theta]}\left[\frac{1}{2}m_{ij}(\partial_\mu \theta_{ij})^2 + V_{\mathrm{Gap}}(\theta)\right]
$$

already presupposes a four-dimensional spacetime manifold, continuous phase fields $\theta_{ij}(x)$, and an unproved field-to-metric map $g[\theta]$ whose covariance and spin-2 dynamics remain open ([Einstein Equations](/docs/physics/gravity/einstein-equations)).

Moreover, conjugation by $G_2$ on $\mathcal{D}(\mathbb{C}^7)$ generically changes diagonal populations and coherence moduli $|\gamma_{ij}|$, so the fixed-modulus phase torus $(S^1)^{21}$ admits no general continuous $G_2$ quotient. Any lattice model defined on $(S^1)^{21N}$ must also specify how density-matrix positivity constraints are enforced on its field domain.

---

## 2. Finiteness at Fixed Lattice Size and the Spectral Action {#определённость}

### 2.1 Finite-lattice partition integral (`T-37 [T]`)

**Theorem T-37 (Well-definedness of the finite-lattice integral) `[T]`.**
On a finite lattice of $N$ sites with compact phase domain $(S^1)^{21N}$ and normalized Haar measure,

$$
Z_N = \int_{(S^1)^{21N}} \prod_{x=1}^{N} \prod_{i<j} \frac{d\theta_{ij}(x)}{2\pi} \, e^{-S_N[\theta]},
$$

any continuous real action $S_N[\theta]$ is bounded below on $(S^1)^{21N}$, so $e^{-S_N[\theta]}$ is bounded and integrable and $0 < Z_N < \infty$ for every fixed finite $N$.

This controls field amplitudes at fixed finite resolution; it establishes neither the existence of a continuum limit $\lim_{N\to\infty} Z_N$ (`[Pr]`) nor a dynamical correspondence with the algebraic product $\mathbb{R}\times S^3$ of `T-120` ([Emergent Manifold](/docs/proofs/physics/emergent-manifold#теорема-произведение-троек)).

### 2.2 Spectral action on a supplied 4D spin manifold (`T-65`) {#теорема-полное-спектральное-действие}

**Theorem T-65 (Conditional Einstein–Hilbert coefficient from the product spectral action) `[T under supplied product geometry, elliptic Dirac operator and cutoff]`.**
Let $(M^4, g, S, D_{M^4})$ be an **externally supplied** closed four-dimensional Riemannian spin manifold with spinor bundle $S$ ($\mathrm{rank}\,S = 4$) and spin Dirac operator $D_{M^4}$, tensored with a finite internal space $H_{\mathrm{int}} = \mathbb{C}^7$ carrying a Hermitian operator $D_{\mathrm{int}}$. Define the product Dirac operator

$$
D = D_{M^4} \otimes I_{\mathbb{C}^7} + \gamma_5 \otimes D_{\mathrm{int}},
$$

and its fluctuated version $D_A = D + A + JAJ^{-1}$ where applicable. Then the asymptotic expansion of the spectral action $\mathrm{Tr}\,f(D_A^2/\Lambda^2)$ as $\Lambda \to \infty$ contains the Einstein–Hilbert action with Newton's constant $G_N = 3\pi / (7 f_2 \Lambda^2)$.

**Proof.**

**Step 1 (Product spectral triple).** Because $M^4$ is closed and $H_{\mathrm{int}} = \mathbb{C}^7$ is finite-dimensional, $D$ is self-adjoint with compact resolvent and bounded commutators with $C^\infty(M^4)\otimes \mathcal{A}_{\mathrm{int}}$. Since $\{D_{M^4}, \gamma_5\} = 0$ and $\gamma_5^2 = I_S$,

$$
D^2 = D_{M^4}^2 \otimes I_{\mathbb{C}^7} + I_S \otimes D_{\mathrm{int}}^2.
$$

By Lichnerowicz's formula, $D_{M^4}^2 = \nabla^*\nabla + \frac{1}{4} R\, I_S$, so $D^2 = \Delta - E$ is a Laplace-type operator on the rank-$28$ bundle $V = S \otimes \mathbb{C}^7$ with endomorphism

$$
E = -\frac{1}{4} R\, I_S \otimes I_{\mathbb{C}^7} - I_S \otimes D_{\mathrm{int}}^2.
$$

**Step 2 (Asymptotic expansion of the spectral action).** For a smooth rapid-decay cutoff $f: [0,\infty) \to \mathbb{R}_{\ge 0}$, the Chamseddine–Connes spectral action with **squared** argument $D_A^2/\Lambda^2$ admits the heat-kernel expansion (Gilkey 1984; Chamseddine–Connes 1996)

$$
S_{\mathrm{spec}}[D_A, \Lambda] = \mathrm{Tr}\,f\!\left(\frac{D_A^2}{\Lambda^2}\right)
\;\sim\; f_0 \Lambda^4 a_0(D_A^2) + f_2 \Lambda^2 a_2(D_A^2) + f_4 a_4(D_A^2) + \mathcal{O}(\Lambda^{-2}),
$$

with moments $f_0 = \int_0^\infty u\,f(u)\,du$, $f_2 = \int_0^\infty f(u)\,du$, and $f_4 = f(0)$.

**Step 3 (Exact Lichnerowicz–Gilkey $a_2$ coefficient).** For any Laplace-type operator $\Delta - E$ on a rank-$r$ bundle $V$ over a closed 4D Riemannian manifold, Gilkey's theorem gives $a_2 = \frac{1}{16\pi^2}\int_{M^4} \mathrm{Tr}_V\!\left(\frac{R}{6} I_V + E\right)\sqrt{g}\,d^4x$. Since $\mathrm{Tr}_S(I_S) = 4$ and $\mathrm{Tr}_{\mathbb{C}^7}(I_{\mathbb{C}^7}) = 7$ (so $\mathrm{Tr}_V(I_V) = 28$),

$$
\mathrm{Tr}_V\!\left(\frac{R}{6} I_V + E\right)
= 28\left(\frac{1}{6} - \frac{1}{4}\right) R - 4\,\mathrm{Tr}_{\mathbb{C}^7}(D_{\mathrm{int}}^2)
= -\frac{7}{3} R - 4\,\mathrm{Tr}(D_{\mathrm{int}}^2),
$$

yielding the exact coefficient

$$
a_2(D^2) = \frac{1}{16\pi^2} \int_{M^4} \left(-\frac{7}{3} R - 4\,\mathrm{Tr}\,D_{\mathrm{int}}^2\right)\sqrt{g}\,d^4x.
$$

Matching the gravitational term $f_2 \Lambda^2 \cdot \left(-\frac{7}{48\pi^2}\right)\int R\sqrt{g}\,d^4x$ to the Euclidean Einstein–Hilbert action $-\frac{1}{16\pi G_N}\int R\sqrt{g}\,d^4x$ gives

$$
G_N = \frac{3\pi}{7 f_2 \Lambda^2}, \qquad \frac{3\pi}{7} \approx 1.346.
$$

**Step 4 (Scope of inputs).** The multiplicity $\mathrm{Tr}(I_{\mathbb{C}^7}) = 7$ is the **only** input from the 7D UHM register. The four-manifold $(M^4, g)$, spin structure $S$, Dirac operator $D_{M^4}$, cutoff scale $\Lambda$, cutoff moments $(f_0, f_2, f_4)$, and any Standard Model matter module are externally supplied. On $\mathbb{C}^7$, odd dimension forbids a KO-dimension-6 real structure (`T-178 [✗]`), and importing Connes' Standard Model bimodule imports its matter content and unification boundary conditions (including the well-known 170 GeV vs. 125 GeV Higgs-quartic history of Chamseddine–Connes–Marcolli 2007 and Chamseddine–Connes 2012). On noncompact $\mathbb{R}\times S^3$, separate trace or localization hypotheses are required.

**Step 5 (Riemannian signature).** The heat-kernel expansion is strictly Euclidean/Riemannian; obtaining Lorentzian field equations and cosmological solutions requires separate analytic, causal, and matter inputs. $\blacksquare$

### 2.3 Cutoff function convention {#canonical-f}

:::note Moment-labeling convention (corpus-wide)
The subscript of $f_{2k}$ matches the Seeley–DeWitt coefficient $a_{2k}$ it multiplies: $f_0 \leftrightarrow \Lambda^4 a_0$, $f_2 \leftrightarrow \Lambda^2 a_2$, $f_4 = f(0) \leftrightarrow a_4$ (consistent with [Cosmological Constant](/docs/physics/gravity/cosmological-constant#теорема-спектральная-лямбда) and `T-70`). In the original Chamseddine–Connes papers, moments are indexed by the power of $\Lambda$ instead (their $f_4$ is our $f_0$; their $f_0 = f(0)$ is our $f_4$).
:::

#### Definition (Canonical cutoff convention) `[D]`

As a **definitional convention** (not a theorem derived from UHM), this corpus fixes the heat-kernel test function

$$
f(u) = e^{-u},
$$

for which $(f_0, f_2, f_4) = (1, 1, 1)$. Setting $\Lambda = M_P$ gives $G_N = \frac{3\pi}{7 M_P^2} \approx \frac{1.346}{M_P^2}$; conversely, calibrating $G_N = M_P^{-2}$ fixes $\Lambda_{\mathrm{eff}} = \sqrt{3\pi/7}\,M_P \approx 1.160\,M_P$. Both are parameter conventions/calibrations rather than predictions of $G_N$ or $\Lambda_{\mathrm{cc}}$.

| Choice | $f(u)$ | $f_0$ | $f_2$ | $f_4$ | $f_0/f_2^2$ |
|---|---|---|---|---|---|
| Exponential (convention) | $e^{-u}$ | $1$ | $1$ | $1$ | $1$ |
| Gaussian | $e^{-u^2}$ | $1/2$ | $\sqrt{\pi}/2$ | $1$ | $2/\pi$ |
| Sharp cutoff | $\Theta(1-u)$ | $1/2$ | $1$ | $1$ | $1/2$ |

#### Scope of cutoff independence {#f-independence}

Changing the test function $f$ preserves purely algebraic data (the input representation and Fano incidence table) and alters dimensionless moment ratios such as $f_0/f_2^2$ by $\mathcal{O}(1)$ factors. Cutoff independence does **not** establish any dynamical physical identification (`[C]`/`[H]`/`[Pr]`), nor does it fix the renormalized cosmological constant.

---

## 3. Power Counting for Polynomial Scalar Truncations {#степенной-счёт}

On an externally supplied flat 4D background, canonically normalized scalar fields have mass dimension $1$, so local polynomial interaction operators up to degree $4$ have nonnegative mass-dimension couplings (`[T for the polynomial truncation]`). This standard scalar power-counting fact does **not** prove that a nonlinear periodic phase theory, a composite metric, or four-dimensional gravity ($[G_N] = M^{-2}$) possesses a finite continuum limit.

---

## 4. Open Continuum Limit (`T-66`) {#уф-конечность}

#### Theorem T-66 (Finiteness at fixed finite lattice cutoff; continuum limit open) `[T at fixed finite N]` {#теорема-уф-конечность}

For every fixed finite number of sites $N$, finite Haar measure on $(S^1)^{21N}$, and bounded measurable integrand $e^{-S_N[\theta]}$, the lattice partition function $Z_N$ is finite (`T-37`).

Removing the lattice cutoff ($N \to \infty$, lattice spacing $a \to 0$) introduces arbitrarily short wavelengths and requires uniform renormalization estimates and a scaling law. **Continuum UV finiteness, all-orders cancellation of gravitational divergences, and a quantum theory of gravity remain completely open (`[Pr]`).** In particular:

- A Ward identity requires a verified symmetry of both action and measure, whereas the fixed-modulus phase torus $(S^1)^{21}$ carries no continuous $G_2$ action.
- Non-renormalization theorems require an explicitly constructed $\mathcal{N}=1$ supersymmetric field theory and constrain only holomorphic superpotentials, not arbitrary gravitational counterterms.
- No GUT instanton action or exponential suppression factor is derived from UHM.

---

## 5. Degrees-of-Freedom Count vs. Horizon Scaling {#степени-свободы}

On an arbitrary finite lattice of $N$ sites where each site carries $21$ phase angles on $(S^1)^{21}$, the kinematic phase-variable count is $21N$ (scaling linearly with the number of sites, i.e., with spatial volume if sites are assigned to a 3D mesh). Neither supersymmetric partners nor a Planck-scale spatial lattice are derived from UHM from the phase torus alone.

### 5.1 Microscopic area law, $G_{\mathrm{EE}} = G_{\mathrm{Sak}}$, unitary QCA bounds, and dynamical graph diagnostics {#microscopic-area-law}

Moving from the bare phase torus to the fermionic Dirac-sea / unitary tetrad QCA layer yields four verified structural results (`verify_six_problems.py`, `verify_deep_frontier_v7.py`–`verify_deep_frontier_v9.py`, `ToEFrontierV8.lean`–`ToEFrontierV9.lean`):

1. **Exact microscopic equality $G_{\mathrm{EE}} = G_{\mathrm{Sak}}$ (`gee_equals_gsak_pv_exact_cq`) [T]:** For any positive 4-term super-convergent Pauli–Villars log-moment $L = \sum c_i m_i^2 \ln m_i^2 > 0$, the Sakharov induced Newton coupling $1/(4G_{\mathrm{Sak}}) = 4\pi \cdot L/(96\pi^2)$ and the continuum entanglement-entropy area-law coefficient $1/(4G_{\mathrm{EE}}) = L/(24\pi)$ coincide identically ($+0.02201618$ for $c=(7,-14,9,-2)/7$, $m=(1,2,3,4)$). On a chiral 3+1D Peschel lattice, $1/(4G_{\mathrm{EE}})$ converges at $O(a^2)$ ($+0.022231$ at $a=0.050$, $+0.022069$ at $a=0.025$) to a Richardson continuum limit of $+0.02201439$ (**$0.0081\%$ exact match** with $1/(4G_{\mathrm{Sak}})$), whereas bare Wilson fermions incur $14.9\%\text{–}23.3\%$ $O(Ma)$ chiral-breaking error [C].
2. **Curved-background covariant $\delta S_{\mathrm{EE}}^{\mathrm{PV}} / \delta\mathrm{Area}$ and Weyl$^2$ Wald entropy (`verify_deep_frontier_v9.py` V9.1.B, `F-32B,C`) [T] / [C]:** On a static curved metric $ds^2 = -dt^2 + \Omega^2(x)d\vec{x}^2$ with $\Omega(x) = 1 + \epsilon\cos(k_0 x)$ (non-zero spatial Ricci scalar $R^{(3)}(0) = 4\epsilon k_0^2 \neq 0$ and 4D Weyl component $C_{txtx}(0) = -\frac{1}{3}\epsilon k_0^2 \neq 0$), the PV-regulated chiral Peschel lattice cleanly separates into $\frac{1}{4G_{\mathrm{Sak}}} + \frac{\sum c_i\ln m_i^2}{240\pi} k_0^2 + O(k_0^4/m^2)$, matching the exact 4D Dirac $\mathrm{Weyl}^2$ Wald entropy slope (`-0.000956` isotropic / **`-0.000967`** fixed-proper-spacing pure-transverse vs. `-0.000981`, **$2.56\%$ / $1.48\%$**). While 5-term (and zero-CC 6-term) $\mathrm{Weyl}^2$-free PV systems universally force antigravity $G_{\mathrm{Sak}} < 0$ by the Extended Complete Tchebycheff (ECT) no-go theorem (`pv_five_term_ect_antigravity_witness_cq`, $L_5/(2\ln 2) = -27/4 < 0$) [✗], releasing finite CC to unimodular sequestering yields a **6-term $\mathrm{Weyl}^2$-free positive-$G_{\mathrm{Sak}}$ escape** (`pv_six_term_cc_weyl_antigravity_vs_escape_cq`) under which the curved-metric deviation collapses **$38.5\times$** on the lattice (`8.85% → 0.23%`) [C].
3. **Unitary QCA singularity bound, Schläfli identity, and Page curve [T]:** A finite-dimensional unitary tetrad QCA ($d_{\mathrm{site}} = 32$, $0 \le c_{\mathrm{eff}}(x) = \sin\theta(x) \le 1$) bounds local energy, entropy ($\le 32\ln 2$ per site), and discrete curvature unconditionally, preventing classical $r = 0$ singularities; simplicial deformations obey the exact Schläfli identity $\max\lvert\sum_e \ell_e d\theta_e/d\lambda\rvert = 5.79\times 10^{-10}$, and a globally pure unitary scrambler ($N = 10$ qubits) reproduces the analytic Page curve with final radiation entropy $S(R_{10}) = 1.78\times 10^{-15}$.
4. **Dynamical graph boundary dominance vs. bare-graph UV obstruction [C] / [P]:** On a background-free $6\times 6$ Wilson–Dirac graph (72 dynamic edge weights, $\lvert\partial A\rvert = 12$), entanglement variation is strictly boundary-dominated ($\partial S_{\mathrm{EE}}/\partial w_{\mathrm{bdry}} = +0.27081$ vs. bulk $+0.01312$, **$20.6\times$ boundary dominance**, additivity $9.95\times 10^{-6}$). However, both bare ($\partial S_{\mathrm{EE}}/\partial E_{\mathrm{vac}} = -0.438 \to -0.821$ vs. $m_0$) and PV-regulated single-bond ratios on an $8\times 8$ graph ($+1356.4, -2.18, +25.7$ vs. $\mu$) fail universality because single-bond perturbations shift bare vacuum energy rather than Ricci curvature; deriving a covariant background-free variational principle $\delta S_{\mathrm{gen}}\vert_V = 0$ beyond $O(R^2)$ remains open [P].

Operational network geometry constructs metric limits directly from transfer costs and first-arrival timing without assuming a Planck lattice ([Common Limiting Metric](/docs/geometry/common-limit)).

---

## 6. Horizons, Wald Entropy, and the de Sitter Observer Algebra (`T-348`) {#информационный-парадокс}

A black-hole horizon is a global causal property of a spacetime solution. Bounded internal matrix entries $\mathrm{Gap}(i,j) \in [0,1]$ construct neither a black-hole metric, nor a singularity bound, nor a microscopic Page curve. Any information-recovery claim or opacity-to-area ansatz $S_{\mathrm{BH}} = \sum \int \mathrm{Gap}^2\,d^2\sigma$ (`[H]`) remains an unproved research program (`[Pr]`).

### 6.1 Wald entropy and exact internal trace identity {#коэффициент-gap-поправки}

For an externally supplied diffeomorphism-invariant gravitational Lagrangian $L(g_{ab}, R_{abcd})$ (depending on curvature without its derivatives) and a stationary black hole with a regular bifurcate Killing horizon $\Sigma$, [Wald's entropy formula](https://arxiv.org/abs/gr-qc/9307038) gives

$$
S_{\mathrm{Wald}} = -2\pi \int_\Sigma \frac{\partial L}{\partial R_{abcd}}\,\epsilon_{ab}\epsilon_{cd}\,dA,
$$

reducing to $A/(4G_N)$ for $L_{\mathrm{EH}} = R/(16\pi G_N)$ (`[T under supplied gravitational action and horizon solution]`). A purely internal potential or constant spectral moment with **no explicit curvature coupling** contributes zero directly to $\partial L/\partial R_{abcd}$ and does not generate $\int_\Sigma \mathrm{Gap}_{ij}^2\,dA$.

For the antisymmetric imaginary part $G = \operatorname{Im}\Gamma$ with eigenvalues $\{0, \pm i\lambda_1, \pm i\lambda_2, \pm i\lambda_3\}$ and $D = i\omega_0 G$, the exact finite-matrix trace identity is

$$
\mathrm{Tr}\,D^4 = 2\omega_0^4 \sum_{k=1}^3 \lambda_k^4,
$$

which includes closed four-step matrix walks and does **not** reduce to a sum of fourth powers of individual off-diagonal entries. Positing a direct Weyl-squared coupling $L = L_{\mathrm{EH}} + a(\Gamma) C_{abcd}C^{abcd}$ (`[H]`) with independent field coefficient $a(\Gamma)$ would yield $\Delta S = -4\pi \int_\Sigma a(\Gamma) C^{abcd}\epsilon_{ab}\epsilon_{cd}\,dA$, whose sign and magnitude depend entirely on the supplied coupling and solution.

### 6.2 Note on Hawking's 1974 temperature formula (not derived from UHM) {#теорема-температура-хокинга}

:::note Demotion: Hawking temperature is not a UHM theorem
On an **externally supplied** asymptotically flat Schwarzschild background, standard semiclassical quantum field theory (Hawking 1974) yields $T_H = \frac{\hbar c^3}{8\pi G_N M k_B}$. Substituting the spectral-action normalization $G_N = 3\pi/(7 f_2 \Lambda^2)$ from `T-65` into Hawking's 1974 formula is a purely algebraic substitution into textbook QFT on a supplied black-hole metric — **not** a derivation of black-hole thermodynamics or evaporation dynamics from UHM. Neither a Gap-driven evaporation channel nor a Page time has been derived.
:::

### 6.3 The de Sitter observer algebra and the holon tower (`T-348 [T]+[I]`) {#алгебра-наблюдателя-де-ситтера}

In Chandrasekaran–Longo–Penington–Witten (CLPW, [arXiv:2206.10780](https://arxiv.org/abs/2206.10780)), the dressed algebra of observables in the static patch of de Sitter space with an observer is a Type $\mathrm{II}_1$ factor whose normalized trace corresponds to the maximal-entropy empty de Sitter state.

**Theorem T-348 (`[T]` as mathematics under the split property of the matter net and CLPW assumption $\mathcal{A}^H = \mathbb{C}$; physical reading `[I]`).**
The infinite tensor product of $7$-dimensional holon algebras $\bigotimes (M_7(\mathbb{C}), \mathrm{tr}_7)$ closes in the GNS representation to the unique hyperfinite Type $\mathrm{II}_1$ factor $\mathcal{R}$. Under the split property of the external matter net (proved for the free massive Klein–Gordon field) and the CLPW assumption $\mathcal{A}^H = \mathbb{C}$, the de Sitter observer algebra is also isomorphic to $\mathcal{R}$, and every isomorphism carries the unique normalized trace to the unique normalized trace: empty de Sitter space maps to all holons at $I/7$ (outside the viability window), and in any normal state only finitely many holons can be viable, each costing more than $0.344$ nat of entropy.

Crucially, `T-348` is a **Type $\mathrm{II}_1$ reparametrization**: a finite clock gives only a Type $\mathrm{I}$ algebra, and matching $7^M = e^{S_{\mathrm{dS}}}$ merely renames an externally given cosmological constant as $M \approx 1.677 \times 10^{122}$ holons — it fixes **neither the sign nor the magnitude of $\Lambda$** (nor $\kappa$). See [Emergent Time §11.5](/docs/proofs/dynamics/emergent-time#t-348) for the full proof and hypotheses.

---

## 7. Open Problems [P] {#открытые-проблемы}

1. **Continuum limit and all-orders quantum gravity:** Perturbative induced 4D Einstein–Hilbert gravity is verified through $O(h^4)$ ([Einstein Equations §5](/docs/physics/gravity/einstein-equations#induced-4d-gravity)), while quartic $O(h^4)$ diffeomorphism Ward identities, positivity-compatible lattice limits $\lim_{N\to\infty} Z_N$, and non-perturbative UV completion remain open.
2. **Covariant background-free graph dynamics:** Derive a covariant variational principle $\delta S_{\mathrm{gen}}\vert_V = 0$ on a dynamical holon graph without bare single-bond vacuum-energy contamination (§5.1).
3. **Vacuum energy scale ($10^{-123}$):** Given the unconditional WGC–quintessence ceiling $S < 12$ / $\Lambda_{\mathrm{UV}} \le 38.54\,\mathrm{meV}$ ([Cosmological Constant](/docs/physics/gravity/cosmological-constant#wgc-quintessence-boundary)), determine whether an external decoupled dark factor or sequestered meV-scale dynamics supplies the physical scale of $\Lambda$.
4. **Curved-background horizon microphysics:** Extend the exact flat-space $G_{\mathrm{EE}} = G_{\mathrm{Sak}}$ area law and finite-qubit Page curve to a self-consistent curved black-hole horizon solution.

---

## Related Documents

- [Einstein Equations](/docs/physics/gravity/einstein-equations) — conditional variation on supplied 4D geometry (`T-65`) and failure of the Gap metric bridge
- [Emergent Geometry](/docs/physics/gravity/emergent-geometry) — state distinguishability, charge spectra, and operational distance
- [Cosmological Constant](/docs/physics/gravity/cosmological-constant) — volume-response identifiability and open sign/magnitude of $\Lambda$ (`T-70`, `T-254`)
- [$\Lambda$ Budget](/docs/proofs/gap/lambda-budget) — identifiability proof and conditional spectral bounds
- [Emergent Manifold](/docs/proofs/physics/emergent-manifold) — product triple (`T-120`) and its supplied-geometry assumptions
- [Emergent Time §11.5](/docs/proofs/dynamics/emergent-time#t-348) — de Sitter observer algebra and the holon tower (`T-348`)
- [Common Limiting Metric](/docs/geometry/common-limit) — constructive operational scaling limits on networks
