---
sidebar_position: 11
title: Prime Radiant
description: "A trajectory-navigation prototype over Γ: two floors of residues (quadratic mod 7 and Cauchy), a working reference machine on the canonical dynamics, a 66-hypothesis calibration table, honest forecast boundaries, and ranked application cases."
---

# The Prime Radiant: a trajectory navigator over Γ

:::info What this document is
UHM fixes a state space ($\Gamma \in \mathcal{D}(\mathbb{C}^7)$), a dynamical law ($\mathcal{L}_\Omega$), computable observables ($P$, $R$, $\Phi$, $C$, $\sigma_k$, Gap), formal thresholds ($2/7$, $1/3$, $1$, $2$), and a cross-domain transfer template ([Domain Transfer](/docs/applied/research/domain-transfer)). This document assembles those parts into a **prototype solver**: a numerical engine that (i) *encodes* a declared task state, (ii) *diagnoses* single-axis degradation with an exact syndrome address, (iii) *searches control trajectories* toward a target region, and (iv) *estimates reachability probabilities* via Monte Carlo rollouts — with every numerical claim printed by a re-runnable reference implementation ([§3, the machine](#машина)). The method throughout is **quantitative calibration** (§5): any symbolic or structural mapping earns — or fails — its status in an automated test table.
:::

## §1. The door and the claim {#дверь}

The proposal is a solver for explicitly encoded tasks under a specified dynamical and observation model `[H]`/`[Pr]`. No universal solver or point-prediction impossibility follows from a Hessian zero mode. A locally Lipschitz deterministic flow has a unique trajectory for a known initial state; uncertainty, observability, chaos, and control policies determine the actual forecast limits. The following architecture must be read with those conditions.

1. **A declared encoding.** Seven-role state features can be proposed for a task, but their observation law, information loss, and retained targets must be validated separately at each scale. An encoder is not automatically a functor or an identifiable physical state.
2. **A specified objective and dynamics.** A chosen viable window may be used as a control target. Neither every admissible field nor every initial state reaches it; invariant domains, attainable controls, resources, and attractor conditions must be established for the actual model.
3. **Calibrated forecasts and policy options.** Predictions for individuals and ensembles both require a specified observation model and uncertainty quantification. Policy navigation is a design choice, not a universal categorical prohibition on individual prediction.

A common seven-role notation is a proposed effective architecture `[D]`/`[I]`, not proof that different physical scales share a lossless state space or a predictive law. Each domain needs an identifiable observation model and independent held-out validation. The universe-as-holon reading is an ontological interpretation `[I]`/`[H]`; it does not certify the solver. The calibration table concerns only the specified prototype.

Everything below integrates three components of the corpus — the [Σ-calculus](/docs/applied/research/syndrome-calculus) (diagnosability rigidity `T-224` `[T]`, diagnostic pyramid `T-225` `[C]`), [Coherence Cybernetics](/docs/applied/coherence-cybernetics/definitions) (the `T-92` `[D]` stress panel and control interventions), and [Domain Transfer](/docs/applied/research/domain-transfer) (structured cross-domain templates `[I]`/`[Pr]`) — atop two mathematical residue constructions (§2).

## §2. The two floors of residues {#вычеты}

The word *residue* names two distinct mathematical tools used by the solver, both extracting a **local address from a closed structure**.

### 2.1 The arithmetic floor: quadratic residues mod 7 `[T]` {#арифметический-этаж}

The quadratic residues modulo 7 are $QR(7) = \{1, 2, 4\}$ — the nonzero squares $1^2, 3^2, 2^2 \bmod 7$. The entire canonical Singer cyclic Fano wiring is their modular arithmetic:

- $QR(7)$ is a $(7,3,1)$ *perfect difference set*: every nonzero residue mod 7 arises exactly once as a difference of two elements. Hence the seven cyclic translates $\{1,2,4\}+k \bmod 7$ form seven triples in which every pair of points lies on exactly one triple — the projective plane $\mathrm{PG}(2,2)$ (`[T]`).
- Under the Singer cyclic arithmetic numbering $(A,S,D,L,E,U,O) = (1,2,3,4,5,6,7)$ (note $U=6$, $O=7$ relative to the display order $A,S,D,L,E,O,U$), the seven translates reproduce the canonical Singer cyclic Fano lines of [Fano selection rules](/docs/physics/gauge-symmetry/fano-selection-rules) verbatim: $\{A,S,L\}$, $\{S,D,E\}$, $\{D,L,U\}$, $\{L,E,O\}$, $\{E,U,A\}$, $\{U,O,S\}$, $\{O,A,D\}$ — machine-checked 7/7 (H03).
- *Multiplier symmetry*: $2 \in QR(7)$, so $x \mapsto 2x \pmod 7$ maps the difference set to itself and permutes the seven lines — this is the $\mathbb{Z}_3$ Frobenius symmetry of the [selection rules](/docs/physics/gauge-symmetry/fano-selection-rules), with line-orbit decomposition $1+3+3$ (H04).
- The three lines through $O$ ($\{L,E,O\}$, $\{U,O,S\}$, $\{O,A,D\}$) partition the remaining six axes into the three pairs $(A,D)$, $(S,U)$, $(L,E)$ `[T]` (H10).
- The same seven triples are the weight-3 codewords of Hamming $H(7,4)$: a single-axis fault *is its own syndrome address* (H09; in depth, [Σ-calculus §4](/docs/applied/research/syndrome-calculus#теорема-сигма)). Explicitly, mapping the Singer cyclic indices $(1,2,3,4,5,6,7) = (A,S,D,L,E,U,O)$ to nonzero 3-bit vectors via the permutation $(3\,4)(5\,6\,7)$ — i.e. $A\mapsto 001$, $S\mapsto 010$, $D\mapsto 100$, $L\mapsto 011$, $E\mapsto 110$, $U\mapsto 111$, $O\mapsto 101$ (equivalently $\alpha^{k-1}$ in $\mathbb{F}_2[x]/(x^3+x+1)$) — makes the XOR sum vanish identically on every one of the seven canonical lines (H07).

Thus the arithmetic floor supplies the solver's **diagnostic organ**: when a single axis degrades, the broken line-checks directly encode its binary address without search.

### 2.2 The analytic floor: Cauchy residues of the resolvent `[T]` {#аналитический-этаж}

The second floor is complex contour integration via the **resolvent** $(z - \Gamma)^{-1}$. For Hermitian $\Gamma$ with spectral decomposition $\Gamma = \sum_j \lambda_j P_j$:

$$
\frac{1}{2\pi i}\oint_{\mathcal{C}} f(z)\,(z-\Gamma)^{-1}\,dz \;=\; \sum_{\lambda_j \in \mathrm{int}\,\mathcal{C}} f(\lambda_j)\,P_j ,
$$

the sum of the residues of the resolvent inside $\mathcal{C}$. Matrix functionals of $\Gamma$ follow directly from this representation: spectral projectors ($f \equiv 1$), von Neumann entropy $S(\Gamma)$ and spectral effective rank $D_{\mathrm{eff}}(\Gamma) = e^{S(\Gamma)}$ ($f = -z\log z$, on a branch-cut-avoiding contour), Gibbs weights ($f = e^{-\beta z}$), and filtered subspaces for multi-scale analysis. The reference machine implements this contour engine and verifies it against direct diagonalization to machine precision: projector idempotence $|P^2 - P| \sim 10^{-17}$, completeness $|\sum_j P_j - I| \sim 10^{-16}$, and $\operatorname{tr} e^{-2\Gamma}$ matching to $10^{-15}$ (H11–H15). At $7\times 7$, contour integration is an exactness check; at composite dimensions ($49$-dimensional pair spaces and larger networks), FEAST-class contour extraction of a target spectral cluster avoids full diagonalization.

### 2.3 The residue principle `[I]` {#принцип-вычета}

Both floors share a single structural pattern: **evaluate a closed invariant to isolate a local coordinate** — the difference-set syndrome naming a degraded axis, and the Cauchy contour integral isolating an eigenspace. As an interpretation `[I]`, this parallels the holonomy perspective of [Universe as Holonom](/docs/core/foundations/universe-as-holonom): *traverse the contour, extract the address*.

## §3. The machine {#машина}

The prototype is implemented twice for cross-language verification. The **reference** is a deterministic NumPy implementation reusing the canonical tick of the [TALOS v0 emulator](/docs/applied/research/engineering-insights). The **instrument** is a Rust implementation with a terminal UI (`ratatui`) exposing eight views (Holon dashboard with $|\Gamma|$ heatmap and $\sigma$-panel, Atlas, Reachability Sampler, Pair, Ensemble, Reading, Calibration, Help), spectrum-preserving rotation controls, boost moves, and domain presets; its `--selftest` runs a 28-hypothesis battery (28/28 VERIFIED) and reproduces the Python attractor purity ($P^* = 0.3208$ vs $0.321$). The dynamical kernel is shared across presets (`Universal`, `Mind`, `Team`, `LLM agent`, `Market`), while only the feature glosses and parameter tuples change. Modules of the reference machine:

| Module | Contents | Verification |
|--------|----------|--------------|
| **[A]** arithmetic floor | $QR(7)$ wiring, $\mathbb{Z}_3$ multiplier, Hamming decode, XOR↔QR map | H01–H10, H46 |
| **[B]** analytic floor | contour projectors, $f(\Gamma)$ via residues | H11–H15, $10^{-15}$ agreement |
| **[C]** observables | $P$, $R$, exact $\Phi$ (not the $7P{-}1$ proxy), $C = \Phi \times R$, $S$, $D_{\mathrm{eff}}$ / $D^{7D}$, $\mathrm{Coh}_E$, the `T-92` stress panel | H33–H38 |
| **[D]** dynamics | Strang-split $\mathcal{L}_\Omega$ tick (PSD-projected), $\kappa(\mathrm{Coh}_E)$ feedback | H16–H32 |
| **[E]** navigator | target regions, $\mathrm{SO}(7)$ dials, boost moves, Monte Carlo reachability sampler, ensembles | H39–H45 |
| **[F]** calibration | 66-hypothesis test suite, re-run on every code change | §5 |
| **[G]** pair space | $\mathcal{D}(\mathbb{C}^{49})$: specified perturbations, quadratic purity identity, $\kappa$-budget allocation | H47–H50 |
| **[H]** towers | centered-Gram aggregate; attenuation-score ladder | H51, H45 |
| **[I]** geodesics | affine $m$-chord identity of replacement flow; path length ratios | H52–H53 |
| **[J]** phase atlas | (dissipation, supply) basin map | H54–H55 |
| **[K]** estimator | predict–measure–update filter over $\mathcal{D}(\mathbb{C}^7)$: full and partial noisy readouts, process noise | R26–R27, demo 6 |
| **[S]** domain sensor | external system $\to$ observation stream; git repository metadata sensor | §3.10 item 7, held-out $p = 0.014$ |
| **[L]** BKM floor | Kubo–Mori metric, $m$/$e$-geodesic lengths, geodesic MPC | H60–H64 |

The emulator uses the calibrated input wiring. The scalar identity $\Phi = 7P - 1$ holds only when the diagonal is uniform ($\gamma_{ii} = 1/7$); for arbitrary diagonals the solver computes exact $\Phi$ directly (H34).

### 3.1 The state and the observables {#уравнения-наблюдаемых}

The state is $\Gamma \in \mathcal{D}(\mathbb{C}^7)$: Hermitian, positive-semidefinite, $\operatorname{tr}\Gamma = 1$; seven populations $\gamma_{ii}$ and twenty-one coherences $\gamma_{ij}$. Under the canonical linear anchor-mixing self-model $\varphi_{\mathrm{lin}}(\Gamma) = R\,\Gamma + (1-R)\,I/7$ (`T-249` `[T]`), the primary observables are:

$$
P = \operatorname{tr}\Gamma^2, \qquad
R = \frac{1}{7P}, \qquad
\Phi = \frac{\sum_{i\neq j}|\gamma_{ij}|^2}{\sum_i \gamma_{ii}^2}, \qquad
C = \Phi\,R,
$$

$$
S = -\operatorname{tr}(\Gamma\ln\Gamma), \qquad
D_{\mathrm{eff}}(\Gamma) = e^{S}, \qquad
D^{7D}(\Gamma) = 1 + 6\,\mathrm{Coh}_E,
$$

$$
\mathrm{Coh}_E = \frac{\|\pi_E(\Gamma)\|_{\mathrm{HS}}^2}{\|\Gamma\|_{\mathrm{HS}}^2}
     = \frac{\gamma_{EE}^2 + 2\sum_{i \neq E}|\gamma_{Ei}|^2}{\operatorname{tr}\Gamma^2}, \qquad
\kappa_0 = \omega_0\,\frac{|\gamma_{OE}|\,|\gamma_{OU}|}{\gamma_{OO}},\quad \kappa_{\text{boot}} = \frac{\omega_0}{7}.
$$

:::note Distinction between $D_{\mathrm{diff}}$, $D^{7D}$, and $D_{\mathrm{eff}}$
In canonical UHM, experiential differentiation $D_{\mathrm{diff}} = \exp S_{vN}(\rho_E)$ is defined on an extended experiential register $\mathcal{H}_E$, with the native 7D proxy $D^{7D} = 1 + 6\,\mathrm{Coh}_E(\Gamma)$ — **not** $\exp S_{vN}(\Gamma)$ on the full $7\times 7$ matrix $\Gamma$. In this prototype, $D_{\mathrm{eff}}(\Gamma) = e^{S(\Gamma)}$ is the **full-matrix spectral effective rank** used as a numerical surrogate in the uncalibrated panel below; exact Cap2 monitoring uses the canonical extended-register $D_{\mathrm{diff}}$ or $D^{7D}$ directly.
:::

Viability threshold: $P > 2/7$; the window's upper boundary $P \le 3/7$ is the inversion of $R \ge 1/3$ under $R = 1/(7P)$. The `T-92` `[D]` seven-component stress panel (using the prototype's effective-rank readout $D_{\mathrm{eff}}$ in $\sigma_E$, or $D^{7D}$ in the native 7D convention):

$$
\sigma_A = 1 - \frac{\gamma_{AA}}{P},\quad
\sigma_S = 1 - \frac{\operatorname{rank}\Gamma_S}{3},\quad
\sigma_D = 1 - 7\gamma_{DD},\quad
\sigma_L = \frac{7(1-\gamma_{LL})}{6},
$$

$$
\sigma_E = 1 - \frac{D_{\mathrm{eff}}}{7},\quad
\sigma_O = 1 - \frac{\kappa_0}{\kappa_{\text{boot}}},\quad
\sigma_U = 1 - \frac{\Phi}{\Phi_{\text{th}}},\qquad \Phi_{\text{th}} = 1.
$$

At the maximally mixed state $\Gamma = I/7$: $\sigma_L = \sigma_U = 1$ exactly (H33). Per `T-92` `[D]`, this raw panel is a diagnostic dashboard rather than an exact equivalent of the four-margin Cap2 viability gate.

### 3.2 The tick {#уравнение-тика}

One step of $\mathcal{L}_\Omega$, Strang-split and PSD-safeguarded:

$$
\Gamma_{n+1} = \Pi_{\mathrm{PSD}}\!\left[\, \mathcal{U}_{dt/2}\Big( \mathcal{U}_{dt/2}(\Gamma_n) + dt\big( g_D(\tfrac{I}{7} - \Gamma) + \kappa\,(\rho^* - \Gamma)\big) \Big)\right],
$$

$$
\mathcal{U}_{\tau}(\Gamma)_{jk} = e^{-i(\lambda_j-\lambda_k)\tau}\,\gamma_{jk}, \qquad
\kappa = g\cdot 1.2\,(1 + 8\,\mathrm{Coh}_E),
$$

with $H_{\text{eff}} = \mathrm{diag}(0,\,0.6,\,1.0,\,1.6,\,3.0,\,2.0,\,2.4)$ ($\lambda_E$ highest), $dt = 0.01$, $g_D = 0.2$, and gain $g = 1$ ($3$ on a boosted step). The three terms play distinct dynamical roles: the unitary step preserves $P$ and $S$ exactly (H16); the depolarizing dissipator alone flows to $I/7$ with $S \to \ln 7$ (H18); the replacement term alone follows the affine mixture chord to $\rho^*$ (H52). $\Pi_{\mathrm{PSD}}$ clips eigenvalues $\lambda \mapsto \max(\lambda, 0)$ and renormalizes to unit trace.

### 3.3 Diagnosis {#уравнение-синдрома}

A binary fault profile $x \in \mathbb{F}_2^7$ multiplies the Hamming parity-check matrix $H$ (whose columns are the seven nonzero vectors of $\mathbb{F}_2^3$ matching the canonical Singer cyclic Fano lines via the bijection of §2.1): the syndrome $s = Hx$ **is the fault address** — for a single fault on axis $a$, $s$ equals column $a$ of $H$ (H09). Continuously, the line-closure functional $c_\ell = |\gamma_{ij}| + |\gamma_{jk}| + |\gamma_{ik}|$ over the seven canonical lines $\ell$ localizes single-axis degradation by the same incidence structure (H36).

### 3.4 The contour engine {#уравнение-контура}

Trapezoidal discretization of the Cauchy residue formula on a circle $z_t = c + re^{i\theta_t}$, $\theta_t = 2\pi(t+\tfrac12)/T$:

$$
f(\Gamma) \;\approx\; \frac{1}{2\pi i}\sum_{t=0}^{T-1} f(z_t)\,(z_t I - \Gamma)^{-1}\,\Delta z_t, \qquad \Delta z_t = \frac{2\pi i r e^{i\theta_t}}{T}.
$$

For $f$ analytic inside the contour, convergence is geometric in $T$ (periodic analytic trapezoidal rule): at $T = 256$ the reference code reaches $10^{-15}$ precision (H13). A single contour enclosing one spectral cluster extracts its projector without full diagonalization.

### 3.5 The pair law — derivation {#вывод-пары}

Let $\Gamma_p = \Gamma_1 \otimes \Gamma_2$ and $X = \gamma\,C + \bar\gamma\,C^\dagger$ with $C = (|i\rangle\langle j|)\otimes(|k\rangle\langle l|)$, $i\neq j$, $k \neq l$. Then

$$
P(\Gamma_p + \varepsilon X) = \operatorname{tr}(\Gamma_p + \varepsilon X)^2
= P_1 P_2 \;+\; 2\varepsilon\operatorname{tr}(\Gamma_p X) \;+\; \varepsilon^2 \operatorname{tr}X^2,
\qquad \operatorname{tr}X^2 = 2|\gamma|^2,
$$

exact to machine precision ($4\cdot10^{-17}$ residual, H47). Because $\langle i|j\rangle = \langle k|l\rangle = 0$, **both partial traces of $X$ vanish identically**: $\operatorname{tr}_2 X = \operatorname{tr}_1 X = 0$ — the reduced states of both subsystems are unchanged (H49). The purity change resides strictly in the cross-subsystem correlation block (positivity of $\Gamma_p + \varepsilon X$ is checked separately).

### 3.6 The attenuation-score ladder — derivation {#вывод-лестницы}

Under the stipulated geometric attenuation score convention of `T-142` `[T]` (with base $3$), the algebraic threshold sequence is

$$
P^{(m)}_{\text{crit}} = \frac{2}{7}\cdot\frac{3^{\,m-1}}{m+1}, \qquad
\frac{P^{(m+1)}_{\text{crit}}}{P^{(m)}_{\text{crit}}} = \frac{3(m+1)}{m+2} > 1 \;\;\forall m \ge 1,
$$

yielding $\tfrac27,\ \tfrac{9}{14},\ \tfrac{54}{35}$ at $m = 2, 3, 4$. Because $P = \operatorname{tr}\Gamma^2 \le 1$ for every density matrix, $P^{(4)}_{\text{crit}} = 54/35 > 1$ is unreachable *within that stipulated score convention* (H45, `T-142` `[T]`). Note explicitly the corpus status boundary: this is an algebraic property of the specified score formula, **not** a universal ceiling on cognitive depth, metamodels, or experiential hierarchy (`T-217 [✗]` withdrawn).

### 3.7 Navigation as an optimization problem {#постановка-навигации}

Given $\Gamma_0$, the target region $\mathcal{G} = \{\Gamma : P \in (2/7, 3/7] \wedge C \ge C^*\}$, and the discrete control set $\mathcal{A} = \{R_{ij}(\pm\theta)\}_{i<j} \cup \{\kappa\text{-boost}\} \cup \{\text{drift}\}$:

$$
\min_{u_{0:T}} \; T + \lambda \sum_{t} \mathrm{heat}(u_t)
\quad \text{s.t.} \quad \Gamma_{t+1} = \mathcal{T}(\Gamma_t, u_t), \;\; \Gamma_T \in \mathcal{G},
$$

where $\mathrm{heat}$ is the measured mean stress of a boosted step. Version v0 solves this greedily (one-step lookahead over the 43 actions); v1 compares greedy search against $m$-geodesic shooting in the BKM metric (`T-263` `[T]` at frozen target and fixed BKM speed; H52/H53, H60–H64).

### 3.8 Monte Carlo reachability and ensemble error bars {#оценки-оракула}

The Monte Carlo reachability estimate is binomial: $\hat p = W/M$, $\mathrm{se}(\hat p) = \sqrt{\hat p(1-\hat p)/M}$ — at $M = 120$, a $0\% \to 25\%$ contrast exceeds $6\,\mathrm{se}$. The ensemble mean of $N$ simulated holons has $\mathrm{se} = \sigma_P/\sqrt{N}$; in the prototype run H44, attractor contraction reduces purity spread from $0.173$ to $0.0154$ while mean pairwise state distance stays at $0.488$.

### 3.9 A worked example, digit by digit {#разобранный-пример}

Consider the explicit state (all values numerically verified) with populations $\mathrm{diag}(\Gamma) = (0.46,\, 0.09,\, 0.07,\, 0.07,\, 0.14,\, 0.10,\, 0.07)$ in display order $(A,S,D,L,E,O,U)$ and three real coherences $\gamma_{AE} = 0.08$, $\gamma_{EO} = 0.07$, $\gamma_{OU} = 0.05$. The matrix is physical: $\lambda_{\min} = 0.0128 > 0$, $\operatorname{tr}\Gamma = 1$.

$$
\textstyle\sum_i \gamma_{ii}^2 = 0.2640,\qquad
\sum_{i\neq j}|\gamma_{ij}|^2 = 2(0.08^2 + 0.07^2 + 0.05^2) = 0.0276,
$$

$$
P = 0.2916 \in (2/7, 3/7] \;\text{(viable)},\quad
R = \frac{1}{7\cdot 0.2916} = 0.4899,\quad
\Phi = \frac{0.0276}{0.2640} = 0.1045,\quad
C = 0.0512,
$$

$$
S = 1.5271,\;\; D_{\mathrm{eff}} = e^S = 4.60,\;\; D^{7D} = 1 + 6\,\mathrm{Coh}_E = 1.87,
$$

$$
\mathrm{Coh}_E = \frac{0.14^2 + 2(0.08^2 + 0.07^2)}{0.2916} = \frac{0.0422}{0.2916} = 0.1447,\qquad
\kappa_0 = \frac{0.07 \cdot 0.05}{0.10} = 0.0350.
$$

Evaluating the prototype `T-92` stress panel (with $D_{\mathrm{eff}}$ in $\sigma_E$): $\sigma = (-0.58,\; 0.00,\; 0.51,\; \mathbf{1.09},\; 0.34,\; 0.75,\; 0.90)$. The diagnostic readout identifies a viable, $A$-dominant state whose $L$-population exceeds the raw panel cutoff ($\gamma_{LL} = 0.07$, $\sigma_L = 1.09 > 1$) and whose $\kappa_0$ supply is low ($\kappa_0 \ll \kappa_{\text{boot}} = 0.143$, $\sigma_O = 0.75$). This example directly illustrates H38 and `T-92` `[D]`: the boolean criterion $\max_k \sigma_k < 1$ disagrees with $P > 2/7$, so the raw panel serves as a componentwise priority ranking ($L$, then $U$, then $O$) rather than a substitute for the four exact Cap2 margins.

### 3.10 Honest demonstrations {#честные-демо}

Four reproducible benchmark protocols are shipped as subcommands of the Rust prototype (`prime-radiant demo blind|calibration|bench`, `prime-radiant checkup`):

1. **Blind ground truth** (`demo blind`): the RNG degrades one randomly chosen axis of a viable state; the diagnoser observes *only the seven canonical line closures* (aggregates, not individual coherences) and must identify the axis, printing the full confusion matrix. Measured: **200/200 = 100%** under heavy damage; **193/200 = 96.5%** under mild damage (attenuation to 70–95%) with 3% observation noise — all seven errors confuse $S \leftrightarrow D$, which share the canonical line $\{S,D,E\}$.
2. **Proper scoring** (`demo calibration`): the Monte Carlo reachability estimate $\hat p$ from 40 rollouts (seed group A) is evaluated against 40 *fresh* rollouts (disjoint seed group B) across unselected random starts. Measured: mean $|\hat p - \text{freq}| = 2.5\%$ vs. binomial se $7.9\%$; Brier score $0.100$ (uniform coin baseline $= 0.25$).
3. **Baselines on identical starts** (`demo bench`): four control policies race from the same 30 low-purity starts. Measured: passive drift $121.4 \pm 11.3$ ticks; random rotation perturbations $148.8 \pm 25.2$ ticks (worse than passive drift); boosted start $30.5 \pm 3.0$ ticks; adaptive boost-below-wall $30.5 \pm 3.0$ ticks. All 30/30 reach the target region within budget.
4. **Structured input checkup** (`checkup --scores 7,5,4,6,3,2,5 --coh AE=0.4 --model mind|team|llm|market`): seven user-supplied ratings (plus optional pairwise coherence weights) are mapped via a printed normalization protocol (populations $=$ scores$/\Sigma$; $\gamma_{ij} = c\sqrt{\gamma_{ii}\gamma_{jj}}$, followed by PSD projection). Two scope caveats print on every run: the self-report encoder is a declared protocol `[D]`/`[I]`, falsifiable by test–retest rather than a physical measurement; and $P$ from self-report measures profile *contrast* (near-uniform ratings automatically sit near $I/7$).
5. **Goal-retention trade-off simulation** (`demo maxim`): a controlled two-holon coupling experiment comparing self-target weight $\varphi_{\text{own}}$ (fraction of a fixed $\kappa$-budget directed to one's own target $\rho^*_B$) against coupling to another holon $\Gamma_A$. Measured (1200 ticks, fixed seeds, identical total $\kappa$-budget across conditions): at $\varphi_{\text{own}} = 1.0$, own-target overlap $0.817$ vs. external capture $0.388$; at $0.5$, $0.634$ vs. $0.581$; at $0.25$, $0.412$ vs. $\mathbf{0.613}$ (captured); at $0.0$, $0.168$ vs. $0.575$; with zero target, $P \to 0.144$ (maximally mixed decay, H23). In this specific model, the retention crossover lies in $\varphi_{\text{own}} \in (0.25, 0.5)$ and external capture lowers $P_B$ from $0.286$ to $\sim 0.22$. The mapping is explicitly `[D]`/`[I]`.
6. **State estimator under noise** (`demo estimator`): a hidden holon evolves with unmodeled process noise (random $\mathrm{SO}(7)$ perturbation per step) and is observed through noisy measurements; filter gains are tuned on seed-A trajectories and evaluated on fresh seed-B runs against two baselines. With full-matrix observations, the filter beats both baselines across noise levels (at $\sigma_{\text{obs}} = 0.005$: error $0.022$ vs. observation-only $0.048$ vs. open-loop prediction $0.080$). With *magnitude-only* observations (the scalar-questionnaire regime), scalar invariants remain accurate ($|\hat P - P| \approx 0.0016$, $|\hat\Phi - \Phi| \approx 0.019$) while full-matrix reconstruction hits an irreducible floor $\sim 0.08$ because **phases are unobservable from magnitudes**. End-to-end blind axis diagnosis through the estimator (reading peak line-drop in a 40-step acute window): **62%** through the filter vs. **22%** on raw snapshots vs. 14.3% chance.
7. **Domain sensor on a real external system** (`sense-git --repo P --window N`): a metadata-only sensor applied to 276 commits of the `holon` repository (13 windows of 20 commits). The feature dictionary is fixed and versioned (`[D]`/`[I]`: $A$ novelty intake, $S$ structural retention, $D$ commit activity, $L$ first-pass stability $= 1 - \text{re-touch share}$, $E$ internal-architecture share, $O$ cadence rhythm, $U$ cross-module span) and consumes commit **metadata only** — commit messages are held out as independent human labels. Populations-only sensing leaves $\sigma_O/\sigma_U$ unidentifiable (they require off-diagonal coherences). On the held-out pre-registered test, fix-heavy windows (labeled solely from held-out messages) show higher metadata-sensed $\sigma_L$: $+0.960$ vs. $+0.899$, permutation $p = 0.014$.

What is *not* yet validated is equally clear: external domains without a tested encoder remain open; coherence-bearing sensing (co-change correlations estimating $|\gamma_{ij}|$ to unlock $\sigma_O/\sigma_U$), additional sensor domains (LLM telemetry, physiological time series), and multi-encoder consensus remain active research items `[Pr]`.

## §4. Golden paths {#золотые-пути}

### 4.1 Definitions `[D]` {#определения-путей}

A **path** is a discrete trajectory of $\Gamma$ under the tick plus controls. Controls come in two classes: **dials** — $\mathrm{SO}(7)$ rotations, which preserve the spectrum (hence $P$, $S$, and $D_{\mathrm{eff}}$) exactly and alter only coherence wiring (H29); and **boost moves** — temporary increases of the regeneration gain $\kappa$ or a temporarily purer target $\rho^*$, which change the spectrum at a measured stress cost. A **target region** is a subset of state space, canonically $\{\Gamma : P \in (2/7, 3/7] \wedge C \ge C^*\}$. A trajectory is **golden** if it reaches the target region within the horizon while remaining viable.

### 4.2 Drift vs. control `[C]` {#дрейф-делает-дорогу}

In the prototype dynamics, most of the convergence toward the viable window is driven by the autonomous drift: starting from a low-purity state ($P = 0.220$), passive drift enters the viable window (`T-124` `[T]`) in 131 ticks with zero control input. A boosted start shortens entry to 33 ticks (75% faster) at higher transient stress. Conversely, passive drift does not select the angular coherence configuration: raising $C$ from $0.340$ to $0.426$ at fixed purity required six $\mathrm{SO}(7)$ rotations.

Within this specific dynamical model `[I]` over `[T]`/`[C]` components:

1. A selected attractor supports convergence only inside its proved basin toward its specified target (`[C]` under the declared vector field and basin). It does not optimize arbitrary goals.
2. A boost move acts as a *basin-crossing impulse* — a transient stress increase that transfers the state into the attractor's fast-convergence region.
3. In the Monte Carlo reachability benchmark (§6.1), from the same low-purity start, passive/timid control sequences reached the target in 0% of rollouts within the horizon, whereas sequences permitting 25% boosted moves succeeded in 25% of rollouts at modestly higher mean stress.
4. Targets outside the viable cone incur persistent stress and collapse toward $I/7$ under loss of regeneration supply (H23).

In pair space $\mathcal{D}(\mathbb{C}^{49})$, an aligned off-diagonal perturbation obeys the exact quadratic identity $\Delta P = 2\varepsilon\operatorname{tr}(\Gamma_p X) + 2\varepsilon^2|\gamma_{\text{cross}}|^2$ (residual $4\cdot 10^{-17}$ across 60 random pairs, H47) with vanishing partial traces ($\operatorname{tr}_1 X = \operatorname{tr}_2 X = 0$ to $10^{-17}$, H49), leaving both marginals invariant. By contrast, a fixed-budget resource allocation contest ($\kappa$-split 80/20) redistributes purity from $(0.338, 0.338)$ to $(0.372, 0.242)$ (H50).

### 4.3 Geodesic comparisons `[C]` / `[I]` (partially measured) {#геодезические}

With a fixed target $\sigma$, pure replacement follows $(1-s)\Gamma_0 + s\sigma$: this is an affine $m$-connection geodesic `[T]`, not in general a shortest curve of the BKM Riemannian metric. The reported H52–H64 experiments compare selected trajectories and controllers: H52 chord residual $3.7\cdot10^{-16}$, H53 length/chord ratio $1.165$, H61–H62 tested lengths $1.1435, 1.1479, 1.2613$, H64 window entry at 33 ticks. Such finite prototype comparisons `[H]` establish neither global variational minimality nor universal learning, gravity, or life dynamics. State-dependent targets require a separate trajectory calculation.

### 4.4 Forecast boundary `[H]` {#граница-пророчества}

The reported H44 prototype run simulates 500 holons with distinct personal anchors. Ensemble purity spread contracts from $0.173$ to $0.0154$ after 300 ticks, while mean pairwise state distance remains $0.488$. These are empirical properties of that chosen simulation, not validation of psychohistory or a universal forecast prohibition `[H]`. A zero Hessian mode does not forbid point prediction: for a known initial state, a locally Lipschitz flow is deterministic. Both population and individual forecasts require explicit observability, noise models, and held-out predictive validation.

## §5. Quantitative calibration {#калибровка}

The discipline of the prototype is straightforward: **every structural claim is tested numerically in a re-runnable verification table.** Three verdicts exist: `VERIFIED` (passes the numerical test), `REFUTED` (fails — surfacing a genuine discrepancy), and `UNTESTABLE` (not expressible in the current prototype).

The v1 calibration suite: **66 hypotheses $\to$ 65 VERIFIED, 1 REFUTED (H46, intentionally retained to document an axis-index swap), 0 UNTESTABLE.** Summary by stratum:

| Stratum | Hypotheses | Result |
|---------|-----------|--------|
| Arithmetic ($QR(7)$, Fano, Hamming, XOR↔QR map) | H01–H10, H46 | 10 verified; H46 refuted **by design** — documents the $U/O$ display-vs-Singer indexing distinction |
| Analytic (contour engine) | H11–H15 | all verified to $10^{-15}$ |
| Dynamics (attractor, entropy law, halting/reignition, metabolic rate, PSD/CPTP, $G_2$) | H16–H32 | verified, incl. `T-124` (6/6 random starts), `T-271` entropy-flux signs at the attractor, `T-273`/`T-276` step-size independence (rate constant to 0.4% across two decades of $dt$), starvation-halt with hysteresis-free reignition, $\dim\mathfrak{g}_2 = 14$ |
| Observables / panel | H33–H38 | maximally mixed state hits $\max\sigma = 1.000$ exactly; $\Phi$ proxy deviation confirmed; $\mathrm{Coh}_E$–$\kappa_0$ correlation $+0.97$; raw boolean $\sigma$-equivalence fails pre-calibration (22/30 mismatches, $\sigma_L$ dominates — H37) |
| Navigation | H39–H44 | boost shortens entry 131$\to$33; boosted rollouts succeed 0%$\to$22–25%; dials raise $C$ beyond drift; transient excursion above $3/7$ returns cleanly ($0.585 \to 0.321$); bitwise determinism |
| Pairs (v0.5) | H24, H47–H50 | quadratic purity identity to $10^{-17}$; nonnegative increment enforced by perturbation sign choice with PSD checked separately; zero partial traces preserve marginals; $\kappa$-split tested in the declared resource model |
| Towers (v0.5) | H45, H51, H56 | algebraic score sequence `T-142` ($9/14 < 1 < 54/35$, H45; not a universal depth ceiling, `T-217 [✗]`); shared target yields high centered-Gram purity ($1.000$) vs. distinct targets ($0.189 \le 2/7$) |
| Geodesics (v0.5) | H52–H53 | replacement follows the affine $m$-chord to $10^{-16}$; drift path is $1.165\times$ its chord |
| Atlas (v0.5) | H54–H55 | viable window forms a proper band in the $(g_D, \kappa)$ plane (11/20 cells); $\kappa = 0$ collapses to $I/7$ |
| Panel calibration | H57–H59 | raw `T-92` panel and exact four-margin Cap2 gate use distinct predicates; both directions checked on explicit witness states |
| BKM floor (v1) | H60–H64 | BKM metric matches classical Fisher on commuting states ($10^{-19}$); $L_m < L_e < L_{\text{drift}}$; $m$-chord stays viable inside window; geodesic MPC recovers boost strategy (33 ticks) |
| Towers-3 (v1) | H65 | 3-level aggregation evaluated on collective states ($1.000$ aligned vs. $0.561$ distinct); member-index Gram matrices alone are target-blind |
| Rollout search (v1) | H66 | rollout-guided search matches greedy at equal budget ($C = 0.4164$ both) |

For a Hermitian $X$, the perturbation identity is $P(\rho+\varepsilon X)-P(\rho)=2\varepsilon\operatorname{Tr}(\rho X)+\varepsilon^2\operatorname{Tr}(X^2)$. It reduces to a pure squared-norm increment only when the cross term vanishes; it is therefore distinct from the [pinching comparison T-77](/docs/consciousness/ethics-meaning/value-consciousness#теорема-кооперация). Choosing the sign of $X$ to make the cross term nonnegative is a construction rule, not evidence that real-world cooperation is universally beneficial. Each interpreted state must also retain positivity and trace one.

H46 checks whether state preparation and readout share the same axis wiring. H57–H59 check explicit witnesses for the raw panel rules. Passing these internal tests certifies only the corresponding properties of the software prototype.

## §6. Monte Carlo reachability and cybernetic analogues {#прайм-радиант}

### 6.1 Monte Carlo reachability sampling `[D]` {#пасьянс}

Evaluating whether a control goal is attainable under bounded control authority is a standard **Monte Carlo reachability estimation** problem. Generating $M$ randomized control sequences over horizon $T$ and recording the empirical success fraction $\hat{p}_{\text{golden}} = W/M$ directly estimates the measure of reachable trajectories from $\Gamma_0$ under the specified action distribution. From the benchmark low-purity start (§3.10), purely conservative action policies achieved $\hat{p}_{\text{golden}} = 0\%$, whereas policies admitting 25% boosted moves achieved $\hat{p}_{\text{golden}} = 25\%$ at a quantified transient stress premium. The sampler issues no deterministic prophecy — it estimates basin reachability probabilistically with binomial error bars (§3.8).

### 6.2 Forecast boundaries and reflexive models `[H]` / `[I]` {#асимов}

The document's title alludes to Asimov's fictional *Prime Radiant* (statistical modeling of large ensembles vs. individual trajectories). Tested against the actual mathematics of UHM, the literary analogy separates cleanly:

- **Open research question `[H]`:** selected simulations (H44) motivate comparing ensemble-level and individual-level forecast errors under explicit noise and observation models. No Hessian theorem restricts forecasting to ensembles or guarantees agents escape a mean trajectory; any such separation must be derived from a specified stochastic control model.
- **Reflexivity by construction `[I]`:** unlike classical black-box models disrupted when agents observe the model, UHM embeds a self-model map $\varphi(\Gamma)$ inside the dynamics itself; transparent status registries and explicit assumptions are therefore consistent with reflexive modeling.
- **Policy boundary `[D]`/`[I]`:** treating the solver as a decision-support navigator (comparing control costs and reachability probabilities) rather than a deterministic oracle over persons is an explicit engineering and governance choice.

<a id="алхимия"></a>

## §7. Architectural blueprint: control, estimation, and forecasting analogues {#чертёж}

To audit the prototype's *software architecture* (independently of any ontological interpretation), we compare its modules against established control, estimation, forecasting, and cybernetic frameworks. Every row below maps a standard discipline's state space, core algorithm, structural lesson, and corresponding prototype module (`[I]` architectural comparison over `[T]`/`[D]` modules).

| Framework | State space | Core engine | Structural invariant | Prototype counterpart |
|-----------|------------|-------------|----------------------|-----------------------|
| **OODA loop** (Boyd) | adversarial engagement | Observe–Orient–Decide–Act cadence | loop tempo and orientation (state representation) govern responsiveness | tick cadence; encoder `Enc` as the Orient module |
| **Scenario planning** (Shell) | branching futures | ensemble scenarios without point overconfidence | explicit separation of ensemble envelopes from point forecasts | §4.4 uncertainty boundary as method |
| **Delphi method** | expert estimates | iterated structured consensus | aggregating independent encoders reduces individual bias | multi-encoder $\hat\Gamma$ roadmap (v1+) |
| **Superforecasting** (Tetlock) | probabilistic forecasts | Brier-scored calibration discipline | continuous proper scoring prevents drift into untestable claims | module `[F]` calibration suite and Brier score (`demo calibration`) |
| **Kalman filtering** | hidden state + noisy measurements | predict–measure–update recursion | optimal recursive state estimation under process and measurement noise | module `[K]` state estimator (`demo estimator`) |
| **Model Predictive Control (MPC)** | dynamical plant + horizon | receding-horizon constrained optimization | plan over horizon, execute one step, re-optimize | `navigate()` and BKM geodesic MPC (`[E]`, `[L]`) |
| **Viable System Model (VSM, Beer)** | five recursive control layers | requisite variety engineering | viability margins and recursive organization across scales | direct cybernetic ancestor of CC; aggregate module `[H]` |
| **Active inference** (Friston) | generative model + beliefs | expected free-energy minimization | unified objective linking inference and control via a self-model | $\rho^* = \varphi(\Gamma)$; BKM gradient links ([Vanchurin bridge](/docs/applied/research/vanchurin-bridge), `T-261`, `T-263`, `T-293`) |
| **RL / MCTS** (AlphaZero) | decision states | tree search combined with learned value priors | search plus value prior outperforms either alone | flat MC reachability sampler today; tree search over controls in v1+ |
| **TRIZ** (Altshuller) | engineering contradictions | structural reconfiguration principles | resolving trade-offs by re-wiring interactions rather than brute force | $\mathrm{SO}(7)$ dials (spectrum-preserving rewiring) + exploiting autonomous drift |

**Architectural synthesis.** Across these engineering and cybernetic traditions, the same eight functional organs recur because they are dictated by closed-loop decision-making under uncertainty `[I]`:

1. **Encoder** (Orient, generative state map) — map domain observations to a structured state. *Prototype: `Enc` / `[C]`.*
2. **Estimator** (Kalman, Delphi) — filter hidden states from noisy sequential data. *Prototype: `[K]` (demo 6) and first metadata sensor `[S]` (git, held-out $p = 0.014$); coherence-bearing sensing remains open.*
3. **Diagnostic panel** (syndrome check, stress metrics) — addressed fault localization. *Prototype: `[C]`, Hamming syndrome decode.*
4. **Phase atlas** (regime maps, basin charts) — map stability and viability regions over parameter space. *Prototype: `[J]`.*
5. **Reachability sampler** (Monte Carlo rollouts, MCTS) — estimate attainment probabilities under control policies. *Prototype: `[E]` Monte Carlo sampler.*
6. **Controller / Navigator** (OODA, MPC) — execute receding-horizon updates at maintained tempo. *Prototype: `[E]`, `[L]`.*
7. **Calibrator** (proper scoring, backtesting) — automated test bench keeping claims empirically honest. *Prototype: `[F]`.*
8. **Governance boundary `[D]`/`[I]`:** individual forecasts and interventions are governed by explicit uncertainty quantification and user decision policies; §4.4 does not claim mathematical impossibility of individual prediction.

The same structural comparison applied to software architecture frameworks (UML$\to$C4, DDD, VSM, MAPE-K, modern agentic stacks) yields the companion specification [HOLARCH](./holarch.md).

## §8. Application cases {#кейсы}

Selection criteria: a repeated data loop (can $\Gamma$ be estimated sequentially?), measurable feedback in commensurate units, explicit error cost, and decision payoff. Ranked:

| # | Case | Horizon | Observables | Status |
|---|------|---------|-------------|--------|
| 1 | **SYNARC introspection & safety** — the $\sigma$-panel as internal monitoring; halting/reignition checks per `T-288`/`T-289`; navigator as deliberation module over $\rho^*_\Omega$ | now (specified) | full suite, exact | `[D]` engineering |
| 2 | **LLM-agent context health** — $\sigma_O$ (resource starvation) flags context degradation before failure; actions = summarize/replenish ([CC worked case](/docs/applied/coherence-cybernetics/applications)) | now | $\sigma$-proxies from logs | `[C]` |
| 3 | **Clinical comparison** — compare an independently calibrated model readout with external clinical records on held-out data (PCI and matrix purity use distinct scales) | 2–3 yr | specified model readouts | `[H]` |
| 4 | **Organizational & team workflow audit** — structured 7-axis / 28-entry state encoding + stress panel + bottleneck remediation; overload read as $O/U$ drop | now | 28-entry structured audit | `[D]` / `[I]` protocolized |
| 5 | **Adaptive tutoring** — state-tracked learning support highlighting available structural transitions (dials) rather than single scalar rankings | 2–3 yr | structured learner state model | `[I]` |
| 6 | **Personal state tracking & self-calibration** — longitudinal self-report encoding, Monte Carlo reachability checks over modeled basins; explicit `[I]` status on every readout | now, personal | self-report time series | `[I]` explicitly |
| 7 | **Market / systemic risk** — $\mathrm{SysRisk} = \max_k\|\sigma_k\|/P$ over ensemble correlation matrices; regime monitoring at aggregate level | 2–10 yr | index proxies | `[H]` |
| 8 | **Research prioritization** — pointing the calibration suite at open hypotheses to identify which test maximally expands verified coverage | now, meta | calibration H-table | `[D]` |
| 9 | **Policy ensemble modeling** — basin maps for population aggregates under candidate interventions with explicit uncertainty envelopes | 10 yr | ensemble $\Gamma$ | `[H]` |
| 10 | **Merger & alliance modeling** — pair-space module separating cross-entity coupling perturbations (H47–H49) from fixed-budget resource competition (H50) | 2–3 yr | pair $\Gamma$, H47–H50 | `[D]` / `[C]` |
| 11 | **Team alignment audit** — centered-Gram aggregate purity comparing aligned targets ($1.000$) against divergent targets ($0.189$) relative to the $2/7$ cut | now | member $\Gamma$ estimates | `[D]` / `[I]` |
| 12 | **Viability engineering** — phase atlas mapping parameter pairs $(g_D, \kappa)$ into the viable band; $\kappa = 0$ boundary demonstrating loss of structure without supply | now | $(g_D, \kappa)$ proxies | `[D]` |

The strongest near-term cases (1–3) share one property: observables already exist digitally, feedback is measured in the same units as interventions, and calibration errors surface rapidly.

## §9. Implemented controls and open measurements {#дорожная-карта}

- Pair readouts (H24, H47–H50) and two-level aggregates (H45, H51) have finite numerical tests. For the third level, H65 operates on collective states; member-index Gram matrices alone can fail to distinguish distinct internal patterns.
- The state estimator handles noisy full-matrix and magnitude-only readouts (R26–R27, demo 6), achieving 62% blind-diagnosis accuracy vs. 22% on raw noisy snapshots in the acute-window simulation. The metadata-only repository sensor passed a pre-registered held-out comparison ($p=0.014$).
- H57–H59 compare the raw `T-92` stress panel against the exact Cap2 gate on explicit witnesses. H60–H64 benchmark geodesic MPC strategies, and H66 compares rollout-guided against greedy search at equal budgets.
- The Verum specification records typed contracts and finite checks; every reported result is strictly scoped to its declared test conditions.

## §10. Status summary {#статусы}

| Claim | Status |
|-------|--------|
| Canonical Fano wiring = translates of $QR(7)$; $\mathbb{Z}_3$ = multiplier 2; Hamming address; XOR↔QR bijection $(3\,4)(5\,6\,7)$ | `[T]` machine-checked |
| Contour-residue spectral engine accurate to $10^{-15}$ | `[T]` standard analysis, machine-checked |
| Viable attractor (`T-124`); entropy-flux signs (`T-271`); starvation-halt + hysteresis-free reignition (`T-288`/`T-289`); step-size invariance (`T-273`/`T-276`) | `[T]` / `[C]` corpus results, numerically reproduced |
| Passive drift performs most of window entry; boost shortens entry at printed stress cost; $\mathrm{SO}(7)$ dials select coherence configuration | measured in prototype v0 |
| Pair space: quadratic identity, chosen sign and PSD check; marginal preservation under zero partial traces; distinct from `T-77` pinching and not a universal cooperation-benefit theorem | measured in prototype v0.5 |
| Attenuation-score sequence (`T-142` `[T]` for stipulated convention, H45; universal depth ceiling withdrawn `T-217 [✗]`); shared vs. distinct targets in centered-Gram aggregate | `[T]` (stipulated score) + measured |
| Replacement flow = affine $m$-chord ($10^{-16}$); drift path $1.165\times$ chord | `[T]` (fixed-target $m$-chord) + measured (`T-263`) |
| Viable window forms a bounded band in $(g_D, \kappa)$; $\kappa = 0 \implies I/7$ | measured in phase atlas |
| Eight-organ architectural convergence across control, filtering, and forecasting disciplines | `[I]` comparative engineering analysis |
| Golden path = globally minimal BKM geodesic | `[H]` (H60–H64 compare finite controllers: $L_m < L_e < L_{\text{drift}}$, MPC enters window in 33 ticks; global variational minimality open) |
| Ensemble vs. individual predictability | `[H]` reported for selected simulation H44; requires independent forecast calibration |
| Stress-panel readout (`T-92` `[D]`) | H37 and H57–H59 test the declared panel and explicit witnesses; distinct from Cap2 gate and biological viability |
| Monte Carlo reachability sampler | `[D]` standard binomial reachability estimation |

*The table of §5 is the executable contract of this prototype: 66 hypotheses in v1, re-run on every revision.*
