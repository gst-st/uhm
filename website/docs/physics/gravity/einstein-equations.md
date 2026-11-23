---
sidebar_position: 2
title: "Einstein Equations in a Supplied Four-Dimensional Geometry"
slug: /physics/gravity/einstein-equations
description: "Conditional Einstein–Hilbert variation on a supplied 4D spin manifold (T-65), failure of the Gap metric ansatz and Fierz–Pauli bridge (T-74 withdrawn), exact QFI pair lemma (T-264), and operational network geometry."
---

# Einstein Equations in a Supplied Four-Dimensional Geometry

This chapter separates three distinct layers: (i) why the proposed Gap-to-metric ansatz, linearized Fierz–Pauli bridge, and universal spectral potential (`T-74 [✗]`) fail; (ii) what the heat-kernel variation actually proves on an externally supplied 4D Riemannian spin manifold (`T-65`); and (iii) the exact quantum Fisher information pair lemma (`T-264(a),(a')`) on $\mathcal{D}(\mathbb{C}^7)$. Constructive operational distance geometry is developed separately in [Common Limiting Metric](/docs/geometry/common-limit) and [Verified Network Results](/docs/reference/network-results).

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

## 5. Constructive Path: Operational Network Geometry

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
