---
sidebar_position: 2
title: "Einstein Equations in a Supplied Four-Dimensional Geometry"
slug: /physics/gravity/einstein-equations
description: "Conditional Einstein–Hilbert variation on a supplied 4D spin manifold (T-65), failure of the Gap metric ansatz and Fierz–Pauli bridge (T-74 withdrawn), exact QFI pair lemma (T-264), and operational network geometry."
---

# Einstein Equations in a Supplied Four-Dimensional Geometry

This chapter separates four distinct layers: (i) why the proposed Gap-to-metric ansatz, linearized Fierz–Pauli bridge, and universal spectral potential (`T-74`) [✗] fail; (ii) what the heat-kernel variation actually proves on an externally supplied 4D Riemannian spin manifold (`T-65`); (iii) the exact quantum Fisher information pair lemma (`T-264(a),(a')`) on $\mathcal{D}(\mathbb{C}^7)$; and (iv) induced 4D Einstein–Hilbert gravity through quartic order $O(h^4)$ from a covariantly regulated 4D Dirac sea with zero bare gravitational action. Constructive operational distance geometry is developed separately in [Common Limiting Metric](/docs/geometry/common-limit) and [Verified Network Results](/docs/reference/network-results).

---

## 1. Failure of the Gap Metric Ansatz {#1-emergent-metric-from-coherences}

### 1.1 Frame dependence of the 4D coordinate split

Fixing a unit imaginary octonion $e_O$ decomposes $\mathrm{Im}\,\mathbb{O} = \mathbb{R}e_O \oplus \mathbb{R}^6$. Its stabilizer $\mathrm{SU}(3) \subset G_2$ acts irreducibly on the real 6-plane $\mathbb{R}^6$; only after complexification does $\mathbb{C}^6$ split as $\mathbf{3} \oplus \bar{\mathbf{3}}$ (`T-48a [✗]`). No choice of three real coordinate axes inside $\mathbb{R}^6$ spans a colour triplet or is $\mathrm{SU}(3)$-invariant, so any putative projector $\Pi_{\mathrm{ST}} = \Pi_O \oplus \Pi_{\mathrm{Re}}$ onto four coordinates depends on an externally chosen frame ([Spacetime](/docs/core/foundations/spacetime#теорема-секторная-декомпозиция)).

### 1.2 Why the coherence-metric ansatz does not derive a metric

An earlier ansatz (`[H]`) defined a perturbed metric on a prescribed background $\eta_{\mu\nu} = \mathrm{diag}(+1,-1,-1,-1)$ via

$$
g_{\mu\nu}(x) = \eta_{\mu\nu} + h_{\mu\nu}(x), \qquad
h_{\mu\nu}(x) = \sum_{i \in \mu,\, j \in \nu} |\gamma_{ij}|^2\,\mathrm{Gap}(i,j)^2.
$$

This expression is not a derivation of spacetime geometry:

1. **Imported signature:** For any real symmetric $h$ with sufficiently small operator norm, $\eta + h$ inherits the signature of the externally supplied $\eta_{\mu\nu}$.
2. **Imported manifold and field structure:** Promoting $\gamma_{ij}$ to fields $\gamma_{ij}(x)$ presupposes spacetime coordinates $x$, a rule for comparing registers at distinct sites, and a coordinate transformation law. Neither the charge-spectrum construction `T-119` nor the determinant form on $2\times 2$ Hermitian matrices (`T-48c [T]`) derives this formula ([Emergent Geometry](/docs/physics/gravity/emergent-geometry)).
3. **Connes distance:** The spectral distance $d(p,q) = \sup\{|f(p) - f(q)| : \|[D, f]\| \le 1\}$ uses the commutator with the supplied manifold Dirac operator $D$ and therefore recovers the metric already encoded in that external operator.

---

## 2. Failure of the Gap-Action Projection and Linearized Bridge {#2-projection-of-the-gap-action-onto-4d}

The standard four-dimensional Einstein–Hilbert action with matter,

$$
S_{\mathrm{eff}} = \frac{1}{16\pi G}\int (R - 2\Lambda)\sqrt{-g}\,d^4x + S_{\mathrm{matter}}[g, \phi],
$$

already assumes a four-dimensional smooth manifold, a Lorentzian metric $g_{\mu\nu}$, and matter fields $\phi$. Partitioning the 21 internal pairs of $\mathbb{C}^7$ into 6 and 15 after choosing four axes is an index count that yields neither local spin-2 gauge symmetry nor a physical matter action.

### 2.1 Withdrawal of `T-74 [✗]` and failure of the linearized Fierz–Pauli bridge {#21-derivation-chain-for-the-projection-t}

The universal derivation of a unique Gap potential and 4D effective gravitational action from the spectral action (**`T-74 [✗]`**) is withdrawn. The internal phase system has a single evolution parameter; promoting phases $\theta_{ij}$ to 4D fields $\theta_{ij}(x)$ and replacing time derivatives by $\partial_\mu$ imports spacetime by hand. Moreover, an algebraic potential $V_2(\theta)$ can be nonzero on constant configurations, whereas the linearized Ricci scalar $R^{(1)}[h]$ contains second derivatives of $h$ and vanishes identically for constant $h$; no kinematic identification exists between the two.

<a id="лемма-линеаризованный-мост"></a>

**Failure of the linearized bridge lemma.** Defining $h_{\mu\nu} = 2\,\mathrm{Re}\,\delta\gamma_{\mu\nu}/\varepsilon_0$ on six off-diagonal pairs in a chosen frame fails to produce linearized general relativity for three independent reasons:

1. **Component deficit:** Six off-diagonal pairs cannot supply the ten independent components of a general symmetric $4\times 4$ metric perturbation $h_{\mu\nu}$.
2. **No Fierz–Pauli structure or gauge invariance:** A sum of scalar kinetic terms for $\delta\gamma_{\mu\nu}$ lacks the cross-derivative and trace terms of the Fierz–Pauli Lagrangian and has no linearized diffeomorphism symmetry $h_{\mu\nu} \mapsto h_{\mu\nu} + \partial_\mu \xi_\nu + \partial_\nu \xi_\mu$. Imposing de Donder gauge therefore presupposes a gauge symmetry the model does not possess.
3. **Circularity of the coupling:** Substituting the target spin-2 field equation to relate $\partial^2 h$ to a matter source assumes the conclusion.

Consequently, the coupling formula $G_N^{(\mathrm{ST})} = 4\pi\mu^2/\varepsilon_0^2$ is an **unproved bridge assumption**, not a theorem derived from UHM.

---

## 3. Conditional Einstein–Hilbert Variation on a Supplied 4D Spin Manifold {#3-einstein-equations-from-gap-variation}

**Theorem T-65 (`[T under supplied product geometry, elliptic Dirac operator and cutoff]`).**
Let $(M^4, g, S, D_{M^4})$ be an externally supplied compact four-dimensional Riemannian spin manifold with Dirac operator $D_{M^4}$, formed into a product spectral triple with $H_{\mathrm{int}} = \mathbb{C}^7$. In the heat-kernel expansion of the spectral action $\mathrm{Tr}\,f(D_A^2/\Lambda_{\mathrm{cut}}^2)$, the Seeley–DeWitt coefficient $a_2(D^2)$ yields the Einstein–Hilbert term $\int R\sqrt{g}\,d^4x$. In the normalization of [Quantum Gravity](/docs/physics/gravity/quantum-gravity#теорема-полное-спектральное-действие), the effective gravitational coupling is

$$
G_N = \frac{3\pi}{7 f_2 \Lambda_{\mathrm{cut}}^2}.
$$

Here the factor $7 = \dim H_{\mathrm{int}} = \mathrm{Tr}(I_{\mathbb{C}^7})$ is the **only** contribution coming from the 7D UHM register; the manifold $(M^4, g)$, spin bundle $S$, Dirac operator $D_{M^4}$, cutoff scale $\Lambda_{\mathrm{cut}}$, and cutoff moment $f_2$ are all external inputs.

For a Lorentzian Einstein–Hilbert action with matter on a supplied 4-manifold, varying with respect to $g^{\mu\nu}$ (with standard Gibbons–Hawking–York boundary terms) gives

$$
G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi G\,T_{\mu\nu}, \qquad
T_{\mu\nu} = -\frac{2}{\sqrt{-g}}\frac{\delta S_{\mathrm{matter}}}{\delta g^{\mu\nu}},
$$

which satisfies $\nabla_\mu T^{\mu\nu} = 0$ by diffeomorphism invariance (or equivalently by the contracted Bianchi identity at constant $G, \Lambda$). Higher-curvature invariants ($C_{\mu\nu\rho\sigma}^2$, $R^2$) appearing in $a_4$ and higher terms of the full spectral expansion generically modify the purely second-order equation.

### 3.0 Comparison with the Connes–Chamseddine spectral action {#сравнение-connes-chamseddine}

The gravitational $a_2$ term is shared because both constructions place an external 4D spin manifold into a product triple; the finite internal modules differ fundamentally.

| # | Structure | Connes–Chamseddine | UHM product triple | Status |
|---|---|---|---|---|
| 1 | Product triple | External 4D spin geometry $\otimes$ even-dim real module $H_F$ | External 4D spin geometry $\otimes\, H_{\mathrm{int}} = \mathbb{C}^7$ (odd dim forbids KO-6) | Distinct finite modules (`T-178 [✗]`) |
| 2 | Internal algebra | $A_F = \mathbb{C} \oplus \mathbb{H} \oplus M_3(\mathbb{C})$ (centre $\dim_{\mathbb{R}} = 5$) | $A_{\mathrm{int}} = \mathbb{C} \oplus M_3(\mathbb{C}) \oplus M_3(\mathbb{C})$ (centre $\dim_{\mathbb{R}} = 6$) | Not Morita equivalent (`T-175a [✗]`) |
| 3 | $a_2$ → Einstein–Hilbert | $S_{\mathrm{EH}} = \frac{1}{16\pi G_N}\int R\sqrt{g}\,d^4x$ | Same structure with $G_N = 3\pi/(7 f_2 \Lambda_{\mathrm{cut}}^2)$ | Identical mechanism (`T-65`) |
| 4 | $a_0$ (volume term) | Cutoff-dependent $\Lambda_{\mathrm{cut}}^4$ term | Same; mapping opacity to vacuum energy requires a physical readout | `[H]` |
| 5 | $a_4$ & Higgs / matter | Supplied SM bimodule and Yukawa matrices | Seven-register supplies neither electroweak doublets nor Higgs mass | Imported if added (`T-178 [✗]`) |

### 3.1 Exact Quantum Fisher Information Pair Lemma (`T-264`) {#взаимность-обучаемость-гравитация}

The phase-direction quantum Fisher information on $\mathcal{D}(\mathbb{C}^7)$ is an exact, self-contained matrix-geometry theorem that requires no gravitational bridge.

#### Theorem T-264 (QFI pair lemma and eigenvalue sandwich) {#теорема-информационно-гравитационная-взаимность}

**(a) Exact pair lemma `[T]`.** For any state $\Gamma \in \mathcal{D}(\mathbb{C}^7)$ whose $(i,j)$-block is decoupled (arbitrary populations $p = \Gamma_{ii} > 0$, $q = \Gamma_{jj} > 0$, coherence $g = \gamma_{ij}$ up to the PSD boundary $|g|^2 \le pq$), the quantum Fisher information along the phase-shift tangent $X_{ij} = \partial\Gamma/\partial\theta_{ij} = i[\Pi_i, \Gamma]$ (a passport-charge generator, `T-260`) is **exactly**

$$
\mathrm{QFI}(\theta_{ij}) = \frac{4\,|\gamma_{ij}|^2}{\Gamma_{ii} + \Gamma_{jj}}, \qquad
g_{\mathrm{Bures}}(\partial_{\theta_{ij}}, \partial_{\theta_{ij}}) = \frac{1}{4}\,\mathrm{QFI}(\theta_{ij}),
$$

independent of population imbalance.

*Proof.* Diagonalizing the decoupled $2\times 2$ block yields eigenvalues $\lambda_\pm = \frac{p+q}{2} \pm R$ with $R = \sqrt{(p-q)^2/4 + |g|^2}$. In the eigenbasis, $X = i[\Pi_i, \Gamma]$ is purely off-diagonal with $|X_{+-}|^2 = (\lambda_+ - \lambda_-)^2 |\langle +|\Pi_i|-\rangle|^2 = 4R^2 \cdot \frac{|g|^2}{4R^2} = |g|^2$. Substituting into the SLD formula $\mathrm{QFI}_\Gamma(X) = 2\sum_{m,n} |X_{mn}|^2 / (\lambda_m + \lambda_n)$ gives

$$
\mathrm{QFI}(\theta_{ij}) = 2 \cdot \frac{2\,|g|^2}{\lambda_+ + \lambda_-} = \frac{4\,|g|^2}{p + q},
$$

with $R$ cancelling identically. $\blacksquare$

**(a′) Unconditional eigenvalue sandwich `[T]`.** For every full-rank $\Gamma \in \mathcal{D}(\mathbb{C}^7)$ and Hermitian tangent $X$, the spectral formula $\mathrm{QFI}_\Gamma(X) = 2\sum_{m,n} |X_{mn}|^2 / (\lambda_m + \lambda_n)$ immediately yields

$$
\frac{\|X\|_{\mathrm{HS}}^2}{\lambda_{\max}(\Gamma)}
\;\le\; \mathrm{QFI}_\Gamma(X) \;\le\;
\frac{\|X\|_{\mathrm{HS}}^2}{\lambda_{\min}(\Gamma)}.
$$

On a coupled $7\times 7$ state, the **pair-only** tangent ($X_{ij} = i\gamma_{ij}$, $X_{ji} = -i\gamma_{ji}$, $\|X\|_{\mathrm{HS}}^2 = 2|\gamma_{ij}|^2$) and the **full passport charge** ($X_i = i[\Pi_i, \Gamma]$, $\|X_i\|_{\mathrm{HS}}^2 = 2\sum_{k\ne i}|\gamma_{ik}|^2$) coincide only when row $i$ carries no other coherences (for example, $\Gamma = I_3/3 + (E_{02}+E_{20})/12$ has $\gamma_{01}=0$ yet $\mathrm{QFI}(X_0)=1/24 > 0$). If $\delta = \max_i\bigl(|\Gamma_{ii} - 1/7| + \sum_{j\ne i}|\gamma_{ij}|\bigr) < 1/7$, Gershgorin's theorem gives $|\lambda_k - 1/7| \le \delta$, so for any $X \neq 0$ the relative deviation of $\mathrm{QFI}_\Gamma(X)$ from $7\|X\|_{\mathrm{HS}}^2$ is bounded by $7\delta/(1 - 7\delta)$.

**Demotion of `T-264(b)` (algebraic identity on an unproved bridge, not a derivation of $G_N$).**
Near uniform populations $\Gamma_{ii} = 1/7$, part (a) gives $\langle\mathrm{QFI}(\theta_{\mu\nu})\rangle_{\mathrm{ST}} = 14\varepsilon_0^2(1 + O(\bar\varepsilon))$ where $\varepsilon_0^2 := \langle|\gamma_{\mathrm{ST}}|^2\rangle$. Multiplying the *assumed* Fierz–Pauli bridge normalization $G_N^{(\mathrm{ST})} = 4\pi\mu^2/\varepsilon_0^2$ (§2.1) by $14\varepsilon_0^2$ cancels $\varepsilon_0^2$ tautologically, giving $G_N^{(\mathrm{ST})} \cdot \langle\mathrm{QFI}\rangle_{\mathrm{ST}} = 56\pi\mu^2 = 8\pi N\mu^2|_{N=7}$. Because $G_N^{(\mathrm{ST})} = 4\pi\mu^2/\varepsilon_0^2$ is not derived from UHM, this product is an **algebraic identity on an unproved bridge assumption**, **not** a derivation of Newton's constant or of a physical information–gravity law. (Likewise, the effective-fluid drift identity `T-254` on an assumed readout $\rho_{\mathrm{DE}} = C\mathcal{G}_O^2$ is a chain-rule identity whose cosmological identification remains `[H]`; see [Cosmological Constant](/docs/physics/gravity/cosmological-constant#теорема-лямбда-дрейф).)

### 3.2 Independence of candidate $G_N$ normalizations {#33-consistency-of-the-two-definitions-of-g-t}

Equating the assumed bridge normalization $4\pi\mu^2/\varepsilon_0^2$ with the spectral-action coefficient $3\pi/(7 f_2 \Lambda_{\mathrm{cut}}^2)$ merely imposes a constraint on independent input parameters $(\mu, \varepsilon_0, f_2, \Lambda_{\mathrm{cut}})$. No derived matching expansion or $O(\mathrm{Gap}^4)$ error bound exists.

### 3.3 Limitations of Lovelock's theorem {#34-ограничения-аргумента-лавлока}

Lovelock's theorem (`T-121`) classifies local, diffeomorphism-covariant, symmetric, divergence-free tensors constructed from a metric and at most its second derivatives on an *externally supplied* 4-manifold (`T-120`). It singles out $G_{\mu\nu}$ and $g_{\mu\nu}$ in four dimensions without fixing $G_N$, $\Lambda$, or $S_{\mathrm{matter}}$. No nontrivial $\mathrm{SU}(3) \to \mathrm{SO}(3)$ projection exists to transfer Lovelock's theorem to internal phases ([Emergent Manifold](/docs/proofs/physics/emergent-manifold#теорема-лавлок-замыкание)).

---

## 4. Stress–Energy Tensor and Non-Perturbative Spectral Scope {#4-energy-momentum-tensor-from-gap}

For a *supplied* homogeneous scalar matter action $S_{\mathrm{matter}}[g,\theta]$ on a 4D FLRW background with kinetic energy $K = \sum \frac{m_{ij}}{2}\dot\theta_{ij}^2$ and potential $V(\theta)$, standard variation gives $\rho = T_{00} = K + V$, $p = K - V$, equation of state $w = (K-V)/(K+V)$ (approaching $w \to -1$ when $K \ll V$), and covariant conservation $\nabla_\mu T^{\mu\nu} = 0$.

Assigning $\mu \sim 10^{-3}\;\mathrm{eV}$ and $\langle\mathrm{Gap}^2\rangle \sim 0.1$ to match $\rho_{\mathrm{DE}} \sim \mu^4 \sim 10^{-47}\;\mathrm{GeV}^4$ ($\rho_{\mathrm{DE}}^{\mathrm{obs}} \approx 2.6 \times 10^{-47}\;\mathrm{GeV}^4$) is a **two-parameter phenomenological fit (`[H]`)**, not a theorem or conditional prediction (`T-266 [H]`). Neither $\mu$ nor $\langle\mathrm{Gap}^2\rangle$ is derived from UHM.

### Scope of non-perturbative spectral evaluation (`T-184`) {#непертурбативная-извлекаемость}

**Theorem T-184 (`[T under supplied finite Hermitian matrix or compact elliptic Dirac operator, geometry and cutoff]`).**
For a supplied finite Hermitian matrix $D$, exact matrix diagonalization evaluates $\mathrm{Tr}\,f(D^2/\Lambda^2)$ without perturbative loop expansion. For a supplied elliptic Dirac operator on a compact Riemannian manifold with smooth cutoff $f$, heat-kernel asymptotics determine the large-$\Lambda$ expansion under standard analytic hypotheses.

This theorem evaluates a chosen spectral functional on supplied data; it does **not** derive $D$, the cutoff $\Lambda$, physical field content, beta functions, a unique vacuum potential (`T-74 [✗]`), or continuum UV finiteness. Earlier heuristic two-loop $1/\mu^2$ beta functions, claims of a 4D Wilson–Fisher or octonionic fixed point, anomalous-dimension estimates, and quintic catastrophe / clinical narratives have been removed as ungrounded in UHM.

---

## 5. Induced 4D Einstein–Hilbert Gravity Through Quartic Order $O(h^4)$ {#induced-4d-gravity}

Although the naive coherence-to-metric ansatz (§1–§2) fails, a covariantly regulated four-dimensional Dirac sea (matching the spinor matter sector without inserting any bare Einstein–Hilbert term $S_{\mathrm{EH}} = 0$) reproduces the full perturbative tensor structure of 4D general relativity through quartic order $O(h^4)$ (verified in `verify_deep_frontier_v6.py`–`verify_deep_frontier_v11.py` and formalized over constructive rationals in `ToEFrontierV6.lean`–`ToEFrontierV11.lean`):

| Perturbative order & observable | Induced 4D Dirac sea (zero bare $S_{\mathrm{EH}}$) | Exact 4D GR / Adler–Visser | Discrepancy / status |
|---|---|---|---|
| $O(h^2)$ Newton coupling $1/(64\pi G_N)$ (3-term PV, 600-cell) | $+0.005885$ | $+0.005889$ | $0.07\%$ [C] |
| $O(h^2)$ wave speed $c_{\mathrm{grav}}^2$ and spin-2 isotropy $c_2(h_+)/c_2(h_\times)$ | $1.00000004$ / $0.99999991$ | $1$ / $1$ | $< 10^{-7}$ [C] |
| $O(h^2)$ trace/conformal ratios $(\mathrm{tr}_3\,q_0,\; \mathrm{tr}_3\,q_z,\; \mathrm{tr}_4\,q_z)/c_2(h_+)$ | $(-1.991,\; -0.660,\; -1.491)$ | $(-2,\; -2/3,\; -3/2)$ | $< 0.94\%$ (GHP sign) [T] |
| $O(h^2)$ axis-free 3D Poisson causal network ($N=72, k=6$) | $c_2(h_+)/c_2(h_\times) = 0.9789$ | $1$ | $\lvert t \rvert = 0.43\,\sigma$ (removes $14.5\%$ cubic artifact) [C] |
| $O(h^3)$ 8 diagonal + 7 off-diagonal cubic 3-graviton vertices (4-term PV) | Match exact nonlinear 4D GR | $\int d^4x\sqrt{g}R\big\vert_{O(h^3)}$ | $0.0004\%\text{–}0.0083\%$ [T] |
| $O(h^3)$ non-Abelian Ward–Slavnov–Taylor identity ($q_1=1,q_2=2,q_3=-3$) | $S^{(3)} = +0.001751923$, $\delta_\xi S^{(2)} = -0.001751910$ | $S^{(3)} + \delta_\xi S^{(2)} = 0$ | $0.00077\%$ [T] |
| $O(A_{12}^2)$ local Lorentz gauge invariance | $-6.69\times 10^{-8}$ (Cartan $-1/4$) vs $100\%/400\%$ fail | $0$ | Mandatory $\omega_{[abc]}$ [T] |
| $O(h^4)$ collinear & non-collinear $h_+^2 h_\times^2$ and mixed $h_+ h_\times h_{13} h_{02}$ | $+0.00145983$ / $+0.00043792$ / $+0.00021892$ | $+0.00146000$ / $+0.00043800$ / $+0.00021900$ | $0.012\%\text{–}0.035\%$ ($75\%\text{–}225\%$ fail without $\omega_{[abc]}$) [T] |
| $O(h^4)$ non-collinear quartic Ward–Slavnov–Taylor identity (`F-32A`) | $W_4(-1/4) = -2.61\times 10^{-8}$ vs $-0.00226$ (`sc=0`) / $-0.00904$ (`+1/4`) | $W_4 = 0$ (exact $4:1$ anomaly ratio) | $0.0188\%$ (`1624%`/`6496%` fail without Cartan $\omega$) [T] |

### 5.1 Structural theorems and remaining boundaries

1. **Universal axial decoupling at $O(h^3)$ and quartic Ward–Slavnov–Taylor identity (`cubic_axial_spin_connection_decoupling_cq`, `quartic_ward_spin_connection_quadratic_ratio_cq`) [T]:** For every symmetric $4\times 4$ metric perturbation $H_{ij} = H_{ji}$, the Levi-Civita axial contraction $\sum_{\alpha, d}\varepsilon_{\alpha e \beta d} H_{\alpha d} \equiv 0$. Consequently, the non-vanishing antisymmetric spin connection $\omega_{[abc]}^{(2)} \neq 0$ decouples identically from all cubic 3-graviton vertices for symmetric vierbeins (while $h_+^2 h_\times \equiv 0$ identically in 4D GR by 2D Gauss–Bonnet and $SO(2)_{12}$ parity) and becomes dynamically mandatory at local Lorentz invariance $O(A^2)$ and quartic order $O(h^4)$ (`quartic_spin_connection_essential_ratio_cq`: omitting $\gamma^{[a}\gamma^b\gamma^{c]}\omega_{abc}$ causes exact $9/4 = 225\%$ and wrong-sign $900\%$ vertex failures). On a non-collinear 4-momentum diffeomorphism (`verify_deep_frontier_v9.py` V9.1.A, `F-32A`), combining bare $V_{\mathrm{anom}}$, linear triangle cross-term $2(4\,\mathrm{sc})V_{\mathrm{anom}}$, and quadratic spin-spin bubble $(4\,\mathrm{sc})^2 V_{\mathrm{anom}}$ factors into $W_4(\mathrm{sc}) = (4\,\mathrm{sc}+1)^2 V_{\mathrm{anom}}$ with exact Cartan cancellation $W_4(-1/4) = -2.61\times 10^{-8}$ (**$0.0188\%$**, $86\,500\times$ suppression), reflection symmetry $W_4(-1/2) = W_4(0)$, versus **$1623.99\%$** without spin connection (`sc = 0`) and **$6496.15\%$** at wrong sign (`sc = +1/4`, exact $4:1$ ratio).
2. **4-term PV sum rules and 5/6-term Universal ECT Antigravity No-Go (`pv_4term_superconvergent_sum_rules_int`, `pv_five_term_ect_antigravity_witness_cq`, `pv_six_term_cc_weyl_antigravity_vs_escape_cq`) [T]:** The integer weights $c = (7, -14, 9, -2)/7$ at $m = (1, 2, 3, 4)$ satisfy $\sum c_i = \sum c_i m_i^2 = \sum c_i m_i^4 = 0$, removing UV divergences and fixing $1/(16\pi G_N) = \frac{1}{96\pi^2}\sum c_i m_i^2 \ln m_i^2 = +0.0017519921$. However, because $\{1, \ln x, x, x\ln x, x^2\}$ and $\{1, \ln x, x, x\ln x, x^2, x^2\ln x\}$ form Extended Complete Tchebycheff (ECT) systems on $(0,\infty)$, simultaneously eliminating the induced $\mathrm{Weyl}^2$ logarithm ($\sum c_i \ln m_i^2 = 0$) with $c_0 = +1$ (lightest physical fermion) in a 5-term PV system — or in a 6-term zero-CC + zero-$\mathrm{Weyl}^2$ system — **universally forces antigravity $G_{\mathrm{Sak}} < 0$** (`100/100` random spectra; exact witnesses at $m_i = 2^i$: $L_5/(2\ln 2) = -27/4 < 0$, $L_6/(2\ln 2) = -81/16 < 0$) [✗]. Releasing finite CC (handled by unimodular sequestering) opens a **6-term $\mathrm{Weyl}^2$-free escape with $G_{\mathrm{Sak}} > 0$** ($c_1 = -3 \implies L_6/(2\ln 2) = +189/16 > 0$) [C].
3. **All-orders PV spin-2 propagator, universal all-$N$ zero sum rule, and Källén–Lehmann EFT ceiling (`pv_six_term_weyl_free_ir_uv_disjoint_cq`, `pv_all_n_spectral_zero_sum_rule_cq`, `pv_kallen_lehmann_unitarity_obstruction_cq`, `verify_deep_frontier_v10.py` V10.1, `F-36A,B,C`) [T] / [✗]:** Evaluating the all-orders 4D Dirac Pauli–Villars spin-2 self-energy $\Pi_2(q^2)$ (direct 4D 120-cell trace vs. exact Feynman-parameter integral agrees to $1.42\times 10^{-4}$ for `PV4` and $4.72\times 10^{-7}$ for `PV6_esc`) reveals a sharp, universal structural boundary of finite Pauli–Villars gravity: both `PV4` ($M_2 = +3.504\times 10^{-3} \to M_4 = -1.161\times 10^{-1}$) and the 6-term $\mathrm{Weyl}^2$-free escape `PV6_esc` ($M_2 = +3.457\times 10^{-2}$, $M_0 = 9.0\times 10^{-19} \to M_4 = -59.26$) develop a Euclidean spin-2 tachyon/ghost zero ($q_* = 5.5941$ for `PV4`, $q_* = 35.6869$ for `PV6_esc`). By the **Exact 6-Term $\mathrm{Weyl}^2$-Free IR/UV Disjointness Theorem** (`F-36A`), positive Newton gravity requires $t < -1/4$ whereas positive UV asymptote $\Pi_2(\infty) > 0$ requires $t > -1/16$ — strictly disjoint intervals, forcing $L_4 < -2025 < 0$ and a guaranteed Euclidean ghost for **every** positive-$G_{\mathrm{Sak}}$ 6-term $\mathrm{Weyl}^2$-free PV spectrum [✗]. Stronger still, by the **Universal All-$N$ 4D Dirac PV Zero Sum Rule** (`F-36C`), **every** finite $N$-term PV spectrum (arbitrary $N$, arbitrary masses, with or without $\mathrm{Weyl}^2$ cancellation) obeys $\int_0^\infty \Pi_2(q^2)/q^2\,dq = \frac{1}{2}\int_0^\infty \rho_2(s)/s^{3/2}\,ds \equiv 0$, so positive IR gravity $M_2 > 0$ universally forces $\Pi_2(q^2) < 0$ on an open interval of $q^2 > 0$ (verified even on a 7-term `PV7` witness with BOTH $M_2 = +2.111\times 10^{-2} > 0$ and $M_4 = +6.333\times 10^{-1} > 0$, which still dives to $\min \Pi_2 = -0.4548$ with **two** Euclidean ghost zeros $q_* = 3.507, 27.415$) [T/✗]. Simultaneously, the Källén–Lehmann spectral density $\rho_2(s)$ turns negative above the first ghost pair threshold $s > 4m_1^2 = 16$ (zero crossings at $s_* = 30.385$ for `PV4`, $s_* = 24.131$ for `PV6_esc`, `F-36B`), proving that finite-PV induced gravity is strictly a **low-energy effective field theory valid for $E < 2 m_1$** and requires a genuinely non-perturbative UV completion above $2 m_1$.
4. **Universal ALL-$\chi$ spectral-action closure (`Super-F-40`), fixed 4D lattice diffeo-mass audit, and 4D deformed $S^4$ Regge–Schläfli (`ToEFrontierV11.lean`, `verify_deep_frontier_v11.py` V11.1) [T] / [✗] / [P]:** Theorem `Super-F-40` (`super_f40_sharp_cutoff_zero_sum_cq`, `super_f40_all_chi_superposition_zero_sum_cq`) closes **every** 4D Dirac spectral action $\mathrm{Tr}\,\chi(D^2/\Lambda^2)$ — positive, monotone, or signed ($f_0 \le 0$) — via exact zero sum rule $\int_0^\infty \Delta_2^\chi(q)/q^2\,dq \equiv 0$ (checked to $\le 2\times 10^{-12}$ on $e^{-u}$, $\Theta(1-u)$ [$q_*=\sqrt{10/3}$], $e^{-u^2}$, Schwinger $E_1(u)$, and signed $(1-au)e^{-u}$ at $a=0.5, 0.6, 0.75$). Across spins $0, \frac{1}{2}, 1$ (`super_f40_spin_pv_trichotomy_cq`, `super_f40_scalar_xi_tadpole_ghost_cq`), the PV sum-rule residue is $(+\frac{1}{96}, 0, -\frac{5}{96})\sum c_i m_i^3$: Dirac is uniquely zero, Proca spin-1 gives antigravity ($C_{\mathrm{Sak}}^{(1)} = -1/2$), and minimally coupled spin-0 develops a ghost for any $\xi > 0$ [T/✗]. Fixed 4D lattices without PV (naive 4D/3+1D, chiral Neuberger overlap with exact Ginsparg–Wilson symmetry and 0 doublers, and axis-free Poisson–Delaunay / $SO(4)$-averaged frames) recover the universal IR log running $\frac{1}{24\pi}$ ($0.05\%\text{–}0.42\%$) yet universally retain bare diffeo-breaking graviton mass ($\Delta_2^{\mathrm{iso}}(0) = -2/3$, $\Delta_2^{\mathrm{ov}}(0) \neq 0$) and bare $G_{\mathrm{Sak}}/G_{\mathrm{EE}}$ mismatch ($+37.8\%\text{–}60.9\%$) [T/✗]. By contrast, background-free **4D simplicial Regge calculus** on a deformed $S^4$ cross-polytope ($\partial\beta_5$: 10V, 40E, 80T, 80Tet, 32 four-simplices, $\chi(S^4) = 2$) obeys local 4D Schläfli ($1.50\times 10^{-15}$), global 4D Schläfli ($2.33\times 10^{-15}$), and exact 4D Regge EOM ($2.66\times 10^{-15}$), with exact $40\times 40$ Hessian of $-S_R$ cleanly separating **10** negative conformal GHP modes from **30** positive TT spin-2 modes (lifting 3D $S^3$ `V10.1.C` to 4D) [T]. On curved $S^4$ without PV, one-loop Sakharov positivity in $\mathrm{Spin}(10) + 3\times\mathbf{16}_+$ still requires $N_S > 132$ minimally coupled real scalars (`sakharov_spin10_scalar_threshold_cq`) [✗]. Non-perturbative 4D background-free continuum limits (Regge/CDT) remain open [P].

---

## 6. Constructive Path: Operational Network Geometry

Rather than assuming a 4D continuum manifold or fitting coherence entries to $h_{\mu\nu}$, operational distances in UHM are constructed directly from intervention costs, first-arrival fronts, and multi-probe calibration on finite and limiting networks:

- [Response Metric](/docs/geometry/response-metric) — directed and symmetric distances from minimal intervention cost and first-arrival timing
- [Common Limiting Metric](/docs/geometry/common-limit) — scaling limits of network probe metrics (rings and asynchronous products)
- [Verified Network Results](/docs/reference/network-results) — machine-checked Lean and Verum theorems on operational distances, gauge transport, and foundational bounds

---

**Related documents:**
- [Emergent Geometry](/docs/physics/gravity/emergent-geometry)
- [Quantum Gravity](/docs/physics/gravity/quantum-gravity)
- [Cosmological Constant](/docs/physics/gravity/cosmological-constant)
- [Emergent Manifold](/docs/proofs/physics/emergent-manifold)
- [Spacetime](/docs/core/foundations/spacetime)
