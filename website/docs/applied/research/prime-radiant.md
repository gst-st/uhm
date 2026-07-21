---
sidebar_position: 15
title: Prime Radiant
description: "The golden-path navigator over Γ: two floors of residues (quadratic mod 7 and Cauchy), a working reference machine on the canonical dynamics, the categorical-calibration protocol (56 machine-tested hypotheses), the honest limits of prediction (navigator, not prophet), and the ranked application cases."
---

# The Prime Radiant: a golden-path navigator over Γ

:::info What this document is
UHM already fixes a state space ($\Gamma \in \mathcal{D}(\mathbb{C}^7)$), a law ($\mathcal{L}_\Omega$), cheap observables ($P$, $R$, $\Phi$, $C$, $\sigma_k$, Gap), thresholds ($2/7$, $1/3$, $1$, $2$) and a transfer engine that reads persons, organizations, machines and markets into the same $\Gamma$ ([Domain Transfer](/docs/applied/research/domain-transfer)). This document assembles those parts into a **solver**: a machine that (i) *encodes* a situation, (ii) *diagnoses* it with an address, (iii) *searches paths* to a goal region, and (iv) *reports what fraction of paths is golden* — with every claim printed as a measured number by a reference implementation ([`prime_radiant.py`](#машина)). The name honors Asimov's device — and §6 states precisely which half of the fantasy survives contact with the theorems. The method throughout is **categorical calibration** (§5): a symbolic system is exactly as good as its ability to describe the computational model of reality, so every symbol here earns — or loses — its number in a re-runnable table.
:::

## §1. The door and the claim {#дверь}

The claim to be examined is the strongest available: *on the UHM basis one can build a universal solver*. Made naively, the claim is false — «universal» collides with the freedom theorem (the kernel $\dim\ker H_\Gamma + 1 > 1$ makes point prophecy structurally impossible, [Freedom](/docs/consciousness/ethics-meaning/freedom)), with chaos, and with the honesty registry itself. Made precisely, it survives and becomes buildable. The precise form has three parts:

1. **One state space for everything that holds together.** Whatever can be read as seven interacting aspects — a mind, a team, a model, a market — is encoded as $\Gamma$ by the [Enc functor](/docs/applied/coherence-cybernetics/sensorimotor#теорема-кодирование-среды); the seven dimensions apply *fractally* across levels ([holarchic ladder](/docs/applied/research/gamma-canon#холархия) [Т/И], [transfer levels I–V](/docs/applied/research/domain-transfer#движок)). This is why «the world is full of analogies»: the analogies are one structure instantiated at many scales, and most of them have simply not been noticed yet.
2. **A solver solves *toward viability*, not toward arbitrary goals.** The law itself carries every pattern toward the viable window (the T-124 attractor, [Conscious window](/docs/proofs/consciousness/conscious-window)); goals aligned with that drift are *assisted by the dynamics*; goals fighting it pay $\sigma$ continuously. «The universe removes obstacles» is a theorem-shaped experience: past the basin boundary, the vector field points your way (§4).
3. **The output is a navigation, never a verdict.** For ensembles the machine predicts; for persons it *opens doors and prices paths*. The boundary between the two is itself a theorem (§4.4), and it is the feature that keeps the Radiant a navigator instead of a cage.

Why should such a machine work at all? Because in UHM the levels of reality **share one form**. The diagonal of $\Gamma$ is a *population* — who is loud at this level; the off-diagonal coherences are the *signal* running between the voices and, through the Enc functor, down the holon hierarchy: a cosmos writes its levels, a society writes its members, a mind writes its habits — the same $7\times 7$ form each time (levels I–V of the [transfer engine](/docs/applied/research/domain-transfer#движок)). That is why prediction works where it works. And it is why symbolic systems are not commentary *about* the world: the corpus's deepest floor holds that the Universe is a self-modelling holon — its self-description $\rho^* = \varphi(\Gamma)$ is *inside* the state (a Lawvere fixed point; observers are internal sections, T-221 — [Universe as Holonom](/docs/core/foundations/universe-as-holonom)). Read against that floor, every calibrated symbolic system is an **organ of the universe's self-cognition** [И], and this machine is a small computational section of the self-model it models — which is exactly why the calibration table of §5, not any manifesto, is its licence to exist.

Everything below is built from three existing research programs — the [Γ-canon](/docs/applied/research/gamma-canon) (the symbolic layer and the П4 oracle protocol), the [Σ-calculus](/docs/applied/research/syndrome-calculus) (diagnosability rigidity T-224/T-225), and [Coherence Cybernetics](/docs/applied/coherence-cybernetics/definitions) (the $\sigma$-panel and interventions) — plus two floors of mathematics that the solver runs on (§2).

## §2. The two floors of residues {#вычеты}

The word *residue* names the solver's core mathematics twice, and the coincidence is instructive: both floors extract a **local address from a closed circuit**.

### 2.1 The arithmetic floor: quadratic residues mod 7 [Т] {#арифметический-этаж}

The quadratic residues modulo 7 are $QR(7) = \{1, 2, 4\}$ — the squares $1^2, 3^2, 2^2 \bmod 7$. The corpus already rests on them once: $N_{\text{gen}} = |QR(7)| = 3$ [Т]. The solver rests on them completely, because **the entire Fano wiring is their arithmetic**:

- $QR(7)$ is a $(7,3,1)$ *perfect difference set*: every nonzero residue arises exactly once as a difference of two elements. Hence the seven translates $\{1,2,4\}+k \bmod 7$ are seven triples in which every pair of points lies on exactly one triple — the Fano plane, wired by addition [Т].
- In the corpus numbering ($A{=}1, S{=}2, D{=}3, L{=}4, E{=}5, U{=}6, O{=}7$ — note $U{=}6$, $O{=}7$: the arithmetic numbering **swaps U and O relative to the display order** $A,S,D,L,E,O,U$) the translates reproduce the seven named lines of [Fano selection rules](/docs/physics/gauge-symmetry/fano-selection-rules) exactly: $\{A,S,L\}, \{S,D,E\}, \{D,L,U\}, \{L,E,O\}, \{A,E,U\}, \{S,U,O\}, \{A,D,O\}$ — machine-checked 7/7 (H03).
- The *multiplier theorem* in miniature: $2 \in QR(7)$, so $x \mapsto 2x$ maps the difference set to itself and therefore permutes the seven lines — this **is** the $\mathbb{Z}_3$ Frobenius symmetry of the [selection rules](/docs/physics/gauge-symmetry/fano-selection-rules), and its orbit structure on lines is $1+3+3$ (H04).
- The three lines through the clock voice $O$ pair the remaining six voices as $(A,D), (S,U), (L,E)$ [Т] (H10) — the pairing that underlies the sectoral split of [Spacetime](/docs/core/foundations/spacetime#секторная-декомпозиция).
- The same triples are the weight-3 codewords of Hamming $H(7,4)$: a single-axis fault *is its own address* (the syndrome equals the binary of the axis; H09, and in depth [Σ-calculus §4](/docs/applied/research/syndrome-calculus#теорема-сигма)). The corpus uses two coordinatizations of this one object — the XOR labeling of the Σ-calculus and the octonionic/QR labeling of the selection rules; the machine finds the dictionary between them, and it is the tidy involution $3 \leftrightarrow 4,\; 5 \leftrightarrow 6$ on labels (H07).

So the arithmetic floor gives the solver its **diagnosis organ**: where the pattern is broken, the broken lines *spell out the address* — no search required. That is the practical content of «a world woven on a self-checking alphabet complains with an address».

### 2.2 The analytic floor: Cauchy residues of the resolvent [Т] {#аналитический-этаж}

The second floor is the residue calculus of complex analysis, entering through the **resolvent** $(z - \Gamma)^{-1}$. For Hermitian $\Gamma$ with spectral decomposition $\Gamma = \sum_j \lambda_j P_j$:

$$
\frac{1}{2\pi i}\oint_{\mathcal{C}} f(z)\,(z-\Gamma)^{-1}\,dz \;=\; \sum_{\lambda_j \in \mathrm{int}\,\mathcal{C}} f(\lambda_j)\,P_j ,
$$

the sum of the residues of the resolvent inside the contour. Every observable of the theory is a functional of such objects: spectral projectors ($f \equiv 1$), entropy and $D_{\text{diff}}$ ($f = -z\log z$, on a cut-avoiding contour), Gibbs weights ($f = e^{-\beta z}$), the Gap spectrum on the $E$-sector, filtered subspaces for the [reflection tower](/docs/consciousness/hierarchy/interiority-hierarchy). The reference machine implements the contour engine and verifies it against direct diagonalization to machine precision: projector idempotence $|P^2 - P| \sim 10^{-17}$, completeness $|\sum_j P_j - I| \sim 10^{-16}$, $\operatorname{tr} e^{-2\Gamma}$ agreeing to $10^{-15}$ (H11–H15). At $7\times 7$ this engine is a luxury; at the composite scales of v1 ($49$-dimensional pair spaces, ecologies) contour extraction of *one needed cluster* without full diagonalization is the standard scalable method (FEAST-class), and the solver is born with it.

### 2.3 The residue principle [И] {#принцип-вычета}

Why do two unrelated mathematics share one name here? Both floors perform the same gesture: **walk a closed circuit, and what survives the cancellation is a local invariant** — the difference-set count that names a faulty axis; the contour integral that names an eigenspace. This is also the Gap-as-holonomy gesture of the corpus (go around a loop, return changed, read the change — [Universe as Holonom](/docs/core/foundations/universe-as-holonom)). As an interpretation [И], the solver's motto: *обойди контур — получи адрес*; the circuit is the computation.

## §3. The machine {#машина}

The machine exists twice, deliberately. The **reference** is `architecture/prime_radiant.py` — numpy-only, deterministic, self-verifying; a sibling of the [TALOS v0 emulator](/docs/applied/research/engineering-insights) whose canonical tick it reuses. The **instrument** is `architecture/prime-radiant-rs` — a Rust implementation with a live TUI (ratatui): eight tabs (Holon dashboard with the $|\Gamma|$ heatmap and σ-panel, Atlas, Oracle, Pair, Ensemble, Reading, Calibration, Help), spectrum-preserving dial controls, bold-mode, and domain presets; its `--selftest` runs a 25-hypothesis battery (25/25 VERIFIED) and reproduces the Python attractor to $P^* = 0.3208$ vs $0.321$ — a cross-language replication of the whole dynamical core. The kernel is **generalized**: one state space, one tick, one observable suite — what changes between application domains is only the gloss vocabulary and the parameter system (the `Model` presets: Universal, Mind, Team, LLM agent, Market), which is the precise sense in which «only the application models and the equation systems change». Organs of the reference machine:

| Organ | Contents | Verification |
|-------|----------|--------------|
| **[A]** arithmetic floor | $QR(7)$ wiring, $\mathbb{Z}_3$ multiplier, Hamming decode, XOR↔QR dictionary | H01–H10, H46 |
| **[B]** analytic floor | contour projectors, $f(\Gamma)$ via residues | H11–H15, $10^{-15}$ agreement |
| **[C]** observables | $P$, $R$, exact $\Phi$ (not the $7P{-}1$ proxy), $C = \Phi \times R$, $S$, $D_{\text{diff}}$, $\mathrm{Coh}_E$, the T-92 stress panel | H33–H38 |
| **[D]** dynamics | the $\mathcal{L}_\Omega$ tick (Strang split, CPTP-safe), $\kappa(\mathrm{Coh}_E)$ feedback | H16–H32 |
| **[E]** navigator | goal regions, SO(7) dials, bold moves, the solitaire oracle, ensembles | H39–H45 |
| **[F]** calibration | the 56-hypothesis table, re-run on every change | §5 |
| **[G]** pair space | $\mathcal{D}(\mathbb{C}^{49})$: bridges, the T-77 gain, the κ-budget contest | H47–H50 |
| **[H]** towers | the centered-Gram meta-holon; the purity ladder | H51, H45 |
| **[I]** geodesics | the m-chord identity of regeneration; path straightness | H52–H53 |
| **[J]** phase atlas | the (dissipation, supply) basin map | H54–H55 |

Two engineering facts deserve their own sentence. *The wiring catch:* the calibration discovered (H46) that the TALOS v0 emulator's translate wiring, read in display order $A..U$, realizes the corpus lines only up to the $U/O$ naming swap of §2.1 — functionally isomorphic (all spectral observables unaffected), but any **line-named** diagnostic must use the corrected wiring; the machine does. *The proxy catch:* the emulator's $\Phi = 7P - 1$ is a uniform-diagonal proxy; on a generic state it deviates from the canonical $\Phi$ by tens of percent (measured: $3.84$ vs $2.45$; H34) — the solver computes the exact one.

### 3.1 The state and the observables {#уравнения-наблюдаемых}

The state is $\Gamma \in \mathcal{D}(\mathbb{C}^7)$: Hermitian, positive-semidefinite, $\operatorname{tr}\Gamma = 1$; seven populations $\gamma_{ii}$ and twenty-one coherences $\gamma_{ij}$. Everything the machine prints is one of:

$$
P = \operatorname{tr}\Gamma^2, \qquad
R = \frac{1}{7P}, \qquad
\Phi = \frac{\sum_{i\neq j}|\gamma_{ij}|^2}{\sum_i \gamma_{ii}^2}, \qquad
C = \Phi\,R,
$$

$$
S = -\operatorname{tr}(\Gamma\ln\Gamma), \qquad
D_{\text{diff}} = e^{S}, \qquad
\mathrm{Coh}_E = \sum_{j \neq E}|\gamma_{Ej}|^2, \qquad
\kappa_0 = \omega_0\,\frac{|\gamma_{OE}|\,|\gamma_{OU}|}{\gamma_{OO}},\quad \kappa_{\text{boot}} = \frac{\omega_0}{7}.
$$

Viability: $P > 2/7$; the window's upper wall $P \le 3/7$ is the inversion of $R \ge 1/3$ through $R = 1/(7P)$. The T-92 stress panel, componentwise:

$$
\sigma_A = 1 - \frac{\gamma_{AA}}{P},\quad
\sigma_S = 1 - \frac{\operatorname{rank}\Gamma_S}{3},\quad
\sigma_D = 1 - 7\gamma_{DD},\quad
\sigma_L = \frac{7(1-\gamma_{LL})}{6},
$$

$$
\sigma_E = 1 - \frac{D_{\text{diff}}}{7},\quad
\sigma_O = 1 - \frac{\kappa_0}{\kappa_{\text{boot}}},\quad
\sigma_U = 1 - \frac{\Phi}{\Phi_{\text{th}}},\qquad \Phi_{\text{th}} = 1.
$$

At the grey state $\Gamma = I/7$: $\sigma_L = \sigma_U = 1$ exactly — the wall (H33).

### 3.2 The tick {#уравнение-тика}

One step of $\mathcal{L}_\Omega$, Strang-split and CPTP-safeguarded:

$$
\Gamma_{n+1} = \Pi_{\mathrm{PSD}}\!\left[\, \mathcal{U}_{dt/2}\Big( \mathcal{U}_{dt/2}(\Gamma_n) + dt\big( g_D(\tfrac{I}{7} - \Gamma) + \kappa\,(\rho^* - \Gamma)\big) \Big)\right],
$$

$$
\mathcal{U}_{\tau}(\Gamma)_{jk} = e^{-i(\lambda_j-\lambda_k)\tau}\,\gamma_{jk}, \qquad
\kappa = g\cdot 1.2\,(1 + 8\,\mathrm{Coh}_E),
$$

with $H_{\text{eff}} = \mathrm{diag}(0,\,0.6,\,1.0,\,1.6,\,3.0,\,2.0,\,2.4)$ ($\lambda_E$ highest, the A5 order), $dt = 0.01$, $g_D = 0.2$, gain $g = 1$ ($3$ on a bold move). The three terms are the whole physics: the unitary preserves $P$ and $S$ exactly (H16); the dissipator alone flows to $I/7$, $S \to \ln 7$ (H18) — *solve*; the regeneration alone rides the mixture chord to $\rho^*$ (H52) — *coagula*. $\Pi_{\mathrm{PSD}}$ is the spectral clip $\lambda \mapsto \max(\lambda, 0)$ with renormalization.

### 3.3 Diagnosis {#уравнение-синдрома}

The fault profile $x \in \mathbb{F}_2^7$ meets the Hamming check matrix $H$ (columns $=$ binary of $1..7$): the syndrome $s = Hx$ **is the address** — for a single fault on axis $a$, $s = \mathrm{bin}(a)$ (H09). Continuously, the line-closure functional $c_\ell = |\gamma_{ij}| + |\gamma_{jk}| + |\gamma_{ik}|$ over the seven lines $\ell$ localizes degradation the same way (H36).

### 3.4 The contour engine {#уравнение-контура}

The trapezoid discretization of the residue formula on a circle $z_t = c + re^{i\theta_t}$, $\theta_t = 2\pi(t+\tfrac12)/T$:

$$
f(\Gamma) \;\approx\; \frac{1}{2\pi i}\sum_{t=0}^{T-1} f(z_t)\,(z_t I - \Gamma)^{-1}\,\Delta z_t, \qquad \Delta z_t = \frac{2\pi i r e^{i\theta_t}}{T},
$$

which for $f$ analytic inside the contour converges *exponentially* in $T$ (the trapezoid rule on a periodic analytic integrand): at $T = 256$ the machine reaches $10^{-15}$ (H13). One contour around one cluster extracts one projector without touching the rest of the spectrum — the property that scales.

### 3.5 The pair law — derivation {#вывод-пары}

Let $\Gamma_p = \Gamma_1 \otimes \Gamma_2$ and the bridge $X = \gamma\,C + \bar\gamma\,C^\dagger$ with $C = (|i\rangle\langle j|)\otimes(|k\rangle\langle l|)$, $i\neq j$, $k \neq l$. Then

$$
P(\Gamma_p + \varepsilon X) = \operatorname{tr}(\Gamma_p + \varepsilon X)^2
= P_1 P_2 \;+\; 2\varepsilon\operatorname{tr}(\Gamma_p X) \;+\; \varepsilon^2 \operatorname{tr}X^2,
\qquad \operatorname{tr}X^2 = 2|\gamma|^2,
$$

— three lines, exact, no approximation; the machine confirms the identity to $4\cdot10^{-17}$ (H47). And because $\langle i|j\rangle = \langle k|l\rangle = 0$, **both partial traces of $X$ vanish identically**: $\operatorname{tr}_2 X = \operatorname{tr}_1 X = 0$ — the reduced states of both members are untouched (H49). The gain has nowhere to live but the bond.

### 3.6 The ladder — derivation {#вывод-лестницы}

$$
P^{(m)}_{\text{crit}} = \frac{2}{7}\cdot\frac{3^{\,m-1}}{m+1}, \qquad
\frac{P^{(m+1)}}{P^{(m)}} = \frac{3(m+1)}{m+2} > 1 \;\;\forall m \ge 1,
$$

so the sequence is strictly increasing: $\tfrac27,\ \tfrac{9}{14},\ \tfrac{54}{35}$ at $m = 2, 3, 4$. Since $P = \operatorname{tr}\Gamma^2 \le \operatorname{tr}\Gamma = 1$ for any density matrix, $m = 4$ demands the impossible — the ceiling of three (H45, [axiom Ω⁷](/docs/core/foundations/axiom-omega)).

### 3.7 Navigation as an optimization problem {#постановка-навигации}

Given $\Gamma_0$, the goal region $\mathcal{G} = \{\Gamma : P \in (2/7, 3/7] \wedge C \ge C^*\}$, and the control set $\mathcal{A} = \{R_{ij}(\pm\theta)\}_{i<j} \cup \{\kappa\text{-boost}\} \cup \{\text{drift}\}$:

$$
\min_{u_{0:T}} \; T + \lambda \sum_{t} \mathrm{heat}(u_t)
\quad \text{s.t.} \quad \Gamma_{t+1} = \mathcal{T}(\Gamma_t, u_t), \;\; \Gamma_T \in \mathcal{G},
$$

where $\mathrm{heat}$ is the measured mean stress of a boosted step. v0 solves it greedily (one-step lookahead over the 43 actions); v1 replaces the search with $m$-geodesic shooting in the BKM metric (T-263) — the down-payment is H52/H53.

### 3.8 The oracle and the ensemble — error bars {#оценки-оракула}

The solitaire estimate is binomial: $\hat p = W/M$, $\mathrm{se}(\hat p) = \sqrt{\hat p(1-\hat p)/M}$ — at $M = 120$, a $0\% \to 25\%$ contrast is $\sim 6\,\mathrm{se}$ apart. The ensemble mean of $N$ holons carries $\mathrm{se} = \sigma_P/\sqrt{N}$; the measured WHERE-compression ($0.173 \to 0.0154$) is the attractor's doing, on top of which the $\sqrt N$ law prices any level-forecast — and the WHO-distance staying at $0.488$ is what no $N$ can average away.

### 3.9 A worked example, digit by digit {#разобранный-пример}

Take the explicit state (all numbers below are machine-computed, not narrated): populations $\mathrm{diag}(\Gamma) = (0.46,\, 0.09,\, 0.07,\, 0.07,\, 0.14,\, 0.10,\, 0.07)$ and three real coherences $\gamma_{AE} = 0.08$, $\gamma_{EO} = 0.07$, $\gamma_{OU} = 0.05$ (Apperception, Immanence, Completeness — an A-loud pattern fed through the E–O–U spine). It is physical: $\lambda_{\min} = 0.0128 > 0$, $\operatorname{tr}\Gamma = 1$.

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
S = 1.5271,\;\; D_{\text{diff}} = 4.60 \ge 2,\qquad
\mathrm{Coh}_E = 0.08^2 + 0.07^2 = 0.0113,\qquad
\kappa_0 = \frac{0.07 \cdot 0.05}{0.10} = 0.0350.
$$

The panel: $\sigma = (-0.58,\; 0.00,\; 0.51,\; \mathbf{1.09},\; 0.34,\; 0.75,\; 0.90)$. The reading writes itself: a viable, A-dominant pattern whose **Logic voice is starved past the wall** ($\gamma_{LL} = 0.07$, $\sigma_L > 1$) and whose supply runs thin ($\kappa_0 \ll \kappa_{\text{boot}} = 0.143$, $\sigma_O = 0.75$) — prescription: restore the $L$-flow first, then feed $O$. Note the teaching moment of H38 live: the boolean $\max\sigma < 1$ criterion disagrees here with $P > 2/7$ — on the uncalibrated panel the *ranking* (L, then U, then O) is the trustworthy output, and this single example shows why calibration item 4 of §9 exists.

### 3.10 Honest demonstrations {#честные-демо}

«Real demonstration» has a definition here, enforced by construction, with four protocols shipped as subcommands of the Rust instrument (`prime-radiant demo blind|calibration|bench`, `prime-radiant checkup`):

1. **Blind ground truth** (`demo blind`): the RNG secretly damages one axis of a healthy state; the diagnoser observes *only the seven line closures* (aggregates, not individual coherences) and must name the axis — «the broken lines spell out the address» tested as an instrument, full confusion matrix printed, nothing curated. Measured: **200/200 = 100%** under heavy damage; **193/200 = 96.5%** under mild damage (crush to 70–95%) with 3% observation noise — the seven errors all confuse S↔D, the two voices sharing the line $\{S,D,E\}$, and the instrument's failure mode is thereby *itself addressed*.
2. **Proper scoring** (`demo calibration`): the oracle's $\hat p$ from 40 deals (seed group A) is tested against 40 *fresh* deals (disjoint seed group B) across unselected random starts. Measured: mean $|\hat p - \text{freq}| = 2.5\%$ against a binomial se of $7.9\%$; Brier $0.100$ (coin $= 0.25$). The oracle is calibrated — its probabilities mean what they say.
3. **Baselines on identical starts** (`demo bench`): four policies race from the *same* 30 random fogs. Measured: drift $121.4 \pm 11.3$ ticks; **random dial-fiddling $148.8 \pm 25.2$ — worse than doing nothing** (無為 measured: fussing beats stillness nowhere); bold start $30.5 \pm 3.0$; adaptive boost-below-the-wall $30.5 \pm 3.0$. All 30/30 succeed within budget.
4. **Real input** (`checkup --scores 7,5,4,6,3,2,5 --coh AE=0.4 --model mind|team|llm|market`): the user's own seven ratings (plus optional named coherences) are encoded by the printed protocol (populations $=$ scores$/\Sigma$; $\gamma_{ij} = c\sqrt{\gamma_{ii}\gamma_{jj}}$, PSD projection) and read by the interpretation organ — named populations, carrying coherences, the loudest stress with the domain prescription. Two honesty clauses print with every result: the self-report Enc is a protocol [О/И], falsifiable by retest, not an oracle pronouncement; and $P$ from self-report measures the *contrast* of the profile — near-uniform ratings land near the grey state by construction, so the verdict line reads profile shape, not a life sentence.

5. **A maxim, decomposed and measured** (`demo maxim`): «a person must have a goal of their own; without one, they become part of another's goal.» The reduction of meanings is printed with the run: *goal* $=$ the regeneration target $\rho^*$; *own goal* $=$ the share $\varphi_{\text{own}}$ of one's κ-budget aimed at one's own $\rho^*_B$; *another's goal* $=$ the social pull toward the other holon's live pattern $\Gamma_A$; *becoming part* $=$ the cosine of one's chord deviation with the other's ideal overtaking the cosine with one's own. Fairness by construction: the total κ-budget is identical in every condition; the whole curve prints. Measured (1200 ticks, fixed seeds): at $\varphi_{\text{own}} = 1.0$ — own-overlap $0.817$ vs capture $0.388$; at $0.5$ — $0.634$ vs $0.581$ (still holding); at $0.25$ — $0.412$ vs $\mathbf{0.613}$ (captured); at $0.0$ — $0.168$ vs $0.575$ (captured); with no goal at all — $P \to 0.144$, the grey dissolution (H23). So the maxim survives contact with the machine **with a threshold attached**: the crossover sits between $\varphi_{\text{own}} = 0.5$ and $0.25$ — roughly, *keeping your chord costs at least a third to a half of your regeneration budget aimed at your own ideal*; and serving a borrowed goal also runs measurably less viable ($P_B$ drops from $0.286$ to $\sim 0.22$). The mapping is [О/И] and printed; every number is measured, and the interpretation is emitted by the machine's own grammar, not narrated afterward.

What is *not* demonstrable today, stated as sharply: any claim about an external system the machine has not encoded — until the estimator organ [K] exists (§9, item 3), the machine reads only states it is handed, and every demo above is honest precisely because it stays inside that boundary.

## §4. Golden paths {#золотые-пути}

### 4.1 Definitions [О] {#определения-путей}

A **path** is a trajectory of $\Gamma$ under the tick plus controls. Controls come in two honest kinds: **dials** — SO(7) rotations, which preserve the spectrum (hence $P, S, D_{\text{diff}}$) exactly and change only the wiring of coherences (H29); and **bold moves** — temporary increases of the regeneration gain $\kappa$ (burning extra negentropy) or a temporarily *purer ideal* $\rho^*$, which do change the spectrum and are paid for in measured stress. A **goal region** is a subset of observable space, canonically «viable and $C \geq C^*$». A path is **golden** if it reaches the goal region within the horizon while remaining viable.

### 4.2 The drift does the road [Т-anchored] {#дрейф-делает-дорогу}

The single most consequential fact for a solver: *the largest part of every golden path is free.* From fog ($P = 0.220$), pure drift reaches the conscious window in 131 ticks with **zero** control effort — the T-124 attractor does the road. Boldness buys time: a boosted start reaches it in 33 ticks (75% faster), running measurably hotter while it lasts. And what the drift can never do is *choose the chord*: at fixed viability, raising $C$ from 0.340 to 0.426 required six dials — the spectrum-preserving choices that are the operational content of freedom. The division of labor is exact and machine-printed: **the field removes the obstacles on the way to being; which chord to be, it leaves to you.**

This is the honest formalization of the question that motivated this document — *why does the universe remove obstacles before the bold?* In UHM the experience decomposes without residue [И over Т]:

1. The viable window is an attractor [Т]: within its basin, the vector field works **for** any goal aligned with viability. Obstacles «dissolve» past the basin boundary because from there the drift finishes the road.
2. A bold move is a *basin crossing*: a stress surge, honestly priced (the machine prints the heat), that relocates the state to where item 1 applies. Timid paths that never cross pay less per step and fight the field forever.
3. The solitaire measures it (§6.1): from the same fog, timid decks came together 0% of the time within the horizon; decks allowed 25% bold moves — 25%, at slightly higher mean heat. Fortune favours the bold *because basins do*.
4. And misalignment is punished the same way: a goal outside the viable cone means permanent $\sigma$-payment and eventual halt at the grey wall — the machine's starvation run (H23) is the minimal model of it.

The pair space sharpens the social half of this. In $\mathcal{D}(\mathbb{C}^{49})$ the machine now tests cooperation directly: an aligned cross-bridge obeys the exact purity law $\Delta P = \text{linear} + 2\varepsilon^2|\gamma_{\text{cross}}|^2$ (worst residual $4\cdot 10^{-17}$ over 60 random pairs, H47), never subtracts (H48) — and, the measured jewel: **both reduced states are unchanged to $10^{-17}$** (H49). The gain of connection is stored *in the bond itself*, in neither member — the exact formal content of the ontology book's line «the increments were never kept inside the one who left». Rivalry, meanwhile, is not the bridge's negative (it has none): it is a **supply contest** — under a fixed κ-budget, an 80/20 split moves the pair from $(0.338, 0.338)$ to $(0.372, 0.242)$ (H50). Contest redistributes; the bridge adds. Ethics, stated in machine units.

### 4.3 Golden paths are geodesics [С/И, partially measured] {#геодезические}

The corpus already knows what an *optimal* aligned path is: learning follows $m$-geodesics of the BKM information metric ([T-263](/docs/core/dynamics/evolution)) — locally straightest lines of the same metric that gravity extremizes one level up (T-264). The machine now measures two shadows of this. First, an identity: **the regeneration term is m-geodesic motion** — under pure regeneration the state rides the mixture chord $\{(1-s)\Gamma_0 + s\rho^*\}$ to a distance of $3.7\cdot 10^{-16}$ (H52); the tick was a geodesic machine all along. Second, a measurement: the full drift road from fog to the window has length/chord $= 1.165$ (H53) — the field's road is nearly straight, and the $16\%$ excess is the unitary swirl around the chord. What remains conjectural [Г] is the full statement — **a golden path is a viable geodesic**, the trajectory minimizing *BKM* length to the goal while staying in the window; the v1 roadmap (§9) replaces greedy dials with genuine geodesic MPC to test it.

### 4.4 The prophecy boundary [Т-anchored] {#граница-пророчества}

What may a Prime Radiant predict? The machine measures the answer. An ensemble of 500 holons, each with its **own identity** (a personal $\rho^*_i$): after 300 ticks the spread of *WHERE* (purity) compresses from $0.173$ to $0.0154$ — everyone reaches the window, the mean trajectory is sharply predictable. The spread of *WHO* (the chord itself) stays order-one: mean pairwise distance $0.488$ — identities do not converge (H44). **Psychohistory is real for ensembles and levels; for persons there is only navigation.** The freedom kernel $\dim\ker H_\Gamma + 1 > 1$ [Т] is what forbids the point oracle — not a deficiency of the machine but the theorem that keeps it on the right side of the door.

## §5. Categorical calibration {#калибровка}

The method of this whole program, stated as a discipline: **a symbolic system is exactly as good as its ability to describe the computational model of reality.** The Γ-canon gives the symbols; the machine gives the model; calibration is the re-runnable table that says, symbol by symbol, whether the number agrees. Three verdicts exist and all three are valuable: VERIFIED (the symbol earned its number), REFUTED (the naive symbolic reading fails — the most informative outcome), UNTESTABLE-in-v0 (the symbol names a structure the current machine cannot express — a roadmap item, not an excuse).

The v0.5 table: **56 hypotheses → 53 VERIFIED, 1 REFUTED, 2 UNTESTABLE.** The strata:

| Stratum | Hypotheses | Result |
|---------|-----------|--------|
| Arithmetic (QR, Fano, Hamming, dictionary) | H01–H10, H46 | 10 verified; H46 refuted **by design** — it documents the TALOS $U/O$ naming catch |
| Analytic (contour engine) | H11–H15 | all verified to $10^{-15}$ |
| Dynamics (attractor, entropy law, halting/reignition, metabolic rate, CPTP, $G_2$) | H16–H32 | verified, incl. T-124 (6/6 random starts), T-271 signs at the attractor, T-273/T-276 frequency-independence (rate constant to 0.4% across two decades of $dt$), starvation-halt with hysteresis-free reignition, $\dim\mathfrak{g}_2 = 14$ |
| Observables/symbols | H33–H38 | the grey wall hits $\max\sigma = 1.000$ exactly; the $\Phi$ proxy deviation is real; $\mathrm{Coh}_E$–$\kappa_0$ correlation $+0.97$; the *naive boolean* $\sigma$-equivalence fails pre-calibration (22/30 mismatches, $\sigma_L$ dominates) — an honest open calibration (H37) rather than a decorated claim |
| Navigation | H39–H44 | boldness shortens time-to-window 131→33; bolder decks win 0%→22–25%; dials raise $C$ beyond drift; an excursion above $3/7$ under a temporarily purer ideal returns cleanly (peak $0.585$ → settled $0.321$); determinism to the bit |
| Pairs (v0.5) | H24, H47–H50 | the T-77 purity law exact to $10^{-17}$; aligned bridges never subtract; **the gain lives in the bond** (reduced states untouched); the κ-contest is a real trade-off |
| Towers (v0.5) | H45, H51, H56 | the ladder $9/14 < 1 < 54/35$ [Т] — the ceiling of three; a shared ideal makes a viable meta-holon (centered-Gram $P = 1.000$), personal ideals do not ($0.189 \le 2/7$); level-3 towers await v1 |
| Geodesics (v0.5) | H52–H53 | regeneration rides the m-chord to $10^{-16}$; the drift road is $1.165\times$ its chord |
| Atlas (v0.5) | H54–H55 | the window is a proper band of the (dissipation, supply) plane (11/20 cells); the $\kappa = 0$ column is all grey — *no supply, no being* |

Two lessons the table already taught, worth the whole exercise: the **H46 catch** (two corpus artifacts wired the same plane under different names — exactly the class of silent error calibration exists to catch) and the **H38 honesty** (the σ-panel's boolean use needs corpus calibration of $\kappa_{\text{boot}}$ and thresholds [С]; its *ranking* use — where does it hurt — survives uncalibrated). Dozens of hypotheses is not a ceiling but a cadence: every future organ lands with its stratum of the table, and the table re-runs on every change.

## §6. The Dee parable and the Prime Radiant {#прайм-радиант}

### 6.1 The solitaire as an oracle [И] {#пасьянс}

Legend has it that John Dee — mathematician, navigator's advisor, keeper of the largest library in England — taught a queen to lay out patience, and that the game was played as a question: *if it comes together, the path exists.* The historical record supports no such episode (Dee advised Elizabeth I; the Medici queen and the patience oracle are apocrypha), so the corpus takes it for what it is — a **parable with exact content** [И]. Laying out the deck many times and counting how often it resolves is Monte-Carlo estimation of a reachability probability. That is precisely the machine's solitaire organ: $M$ random control decks over the horizon; $p_{\text{golden}}$ = the measured fraction that comes together; the deal decides nothing — **it measures the basin**. From the same starting fog: timid decks 0%, bold decks 25%, at a printed heat premium. Four centuries later the cards are density matrices, but the question — and the honesty of asking probability instead of certainty — is the same.

### 6.2 What survives of Asimov's device [Т/Г/И] {#асимов}

In *Foundation*, Hari Seldon's Prime Radiant holds psychohistory: the statistical prediction of civilizational trajectories, valid only for vast ensembles, blind to individuals, broken by one anomalous mind (the Mule), and kept secret lest knowledge of the prediction destroy it. Run against the theory, the fantasy splits cleanly:

- **Survives, now with proofs:** prediction is ensemble-and-level-bound (§4.4 measured it: WHERE compresses 11×, WHO does not); the «Mule» is not an anomaly but a theorem — the freedom kernel and the excursion mechanism guarantee individuals who leave the mean trajectory; crises are basin boundaries, and «Seldon crises» are saddle crossings where small pushes decide much.
- **Repaired:** secrecy. Psychohistory feared reflexivity; UHM *builds on* it — the self-model is inside the state ($\rho^* = \varphi(\Gamma)$), so the prediction knowing about itself is the normal regime of the theory, not its failure mode. A public registry with statuses is the anti-Seldon: the theory that numbers its postulates survives being known.
- **Dropped:** the point oracle over persons, for the reasons of §4.4 — and this is the moral line: a device that *predicted* persons would be a cage; a device that prices paths and opens doors is a navigator.

That the idea keeps being grasped — Seldon's Radiant, the Golden Path of *Dune* (a viability corridor bought at terrible $\sigma$-cost by one who sees the basins), the Tao's 無為 (act with the drift, and the ten thousand obstacles remove themselves), «fortune favours the bold» — is the fractality of §1 seen in culture: one structure, many instantiations, most not yet named. The solver names them.

### 6.3 Solve et coagula: the alchemical layer [И] {#алхимия}

The oldest of the captures deserves its own subsection, because the correspondence is not decorative — it is organ-by-organ. The alchemists' twin imperative **solve et coagula** — dissolve and bind — names the two dissipative terms of the canonical tick *literally*: the dissipator $g_D(I/7 - \Gamma)$ dissolves every structure toward the prima materia (the grey state, their *nigredo* — and the machine confirms the dissolver alone ends exactly there, H18); the regeneration $\kappa(\rho^* - \Gamma)$ binds the dissolved material toward the self-ideal (*coagulatio*, the whitening — and it rides the m-chord, H52). The Great Work — nigredo → albedo → rubedo — is the golden path: grey → the window → the chosen chord. **Transmutation** is the dials: SO(7) rotations change the *wiring* while preserving the substance exactly (spectrum, purity, entropy invariant, H29) — lead into gold without creating or destroying a gram, which is what the honest alchemists always said they meant. *As above, so below* — the Emerald Tablet's axiom — is the holarchic Enc of §1, now with a measured floor: the same Γ-form at member level and at ecology level (the Gram meta-holon, H51). And the Stone itself: the tradition insisted *lapis noster non est lapis* — «our stone is not a stone». The machine agrees. What the Work produces is not a substance but an **instrument** — the emulator plus its calibration table, the thing that turns any state's lead into its gold *by finding the path*: the reading of the dream this program takes as its own, marked [И] and earned line by line in §5.

## §7. The blueprint: the full spectrum of stalking, planning and forecasting systems {#чертёж}

If the solver is real, humanity has been building fragments of it for three thousand years. So the strongest available test of the *architecture* (as opposed to the physics) is comparative: lay out the **maximal spectrum** of navigation systems — divinatory, strategic, cybernetic, statistical — and see whether their load-bearing parts converge. They do, and the convergence is the blueprint. Each row states the system's state space, its oracle/engine, the invariant it got permanently right, and what the Radiant absorbs from it; the reading of every row is [И] over the machine's [Т/О] organs.

| System | State space | Oracle / engine | The invariant it got right | What the Radiant absorbs |
|--------|------------|-----------------|---------------------------|--------------------------|
| **I Ching** (c. −1000) | 64 hexagrams = 6-bit situations | stochastic cast → hexagram + *moving lines* → second hexagram | the reading is of the **situation-dynamics**, not the person; change has a typology | discrete shadow of state space; transition reading = basin-to-basin move (cf. the [16 archetypes](/docs/applied/research/gamma-canon#слой-4)) |
| **Tarot / arcana** | 21+1 major arcana | spread = structured sampling | a *small complete* alphabet of situations, laid in relations | the Canon's 21 coherences + observer ([П5 atlas](/docs/applied/research/gamma-canon#п5-атлас)) |
| **Astrology** | ephemeris = deterministic celestial clock | transits = scheduled perturbations of a natal state | **time-indexed readout against a shared clock**; the natal chart as an Enc of initial conditions | the [autoephemeris П3](/docs/applied/research/gamma-canon#п3-траектория): the holon's own trajectory as its ephemeris |
| **Dee's patience** (§6.1) | deck = path space | deal-until-it-comes-together | reachability asked as a **probability** | the solitaire organ, verbatim |
| **Castaneda's stalking** | one's own routines | systematic self-observation; *controlled folly*; impeccability | change the **wiring** of habits by small controlled moves; leaks of intent are the enemy | dials as routine-rewiring; impeccability = $\sigma$-hygiene; [П8 stalking the bridges](/docs/applied/research/gamma-canon#п8-сталкинг) |
| **Sun Tzu** | terrain + dispositions | win before battle | **choose the basin where the field fights for you** («water flows downhill») | §4.2 in one sentence, 25 centuries early |
| **OODA loop** (Boyd) | adversarial engagement | Observe–Orient–Decide–Act, faster than the environment | *tempo*: the loop's rate is itself a weapon; Orient = the encoder is the seat of victory | the tick cadence; Enc as the Orient organ |
| **Scenario planning** (Shell) | branching futures | ensemble narratives, no point forecast | institutionalized **refusal of point prophecy** | the §4.4 boundary as method, not modesty |
| **Delphi method** | expert beliefs | iterated anonymous consensus | many encoders beat one | multi-encoder $\hat\Gamma$ (v1) |
| **Superforecasting** (Tetlock) | probabilistic claims | Brier-scored calibration culture | **calibration as a discipline**: keep score or drift into myth | the [F] organ *is* a Brier board for symbols |
| **Kalman filtering** | hidden state + noisy readings | predict–measure–update | optimal **estimation** under noise | the missing organ this survey exposed: v0.5 has no estimator $\hat\Gamma(\text{data})$ — promoted to the v1 roadmap |
| **MPC** (control) | plant + horizon | receding-horizon optimization | plan far, commit one step, re-plan | `navigate()`, verbatim |
| **VSM** (Beer) | five recursive systems | variety engineering | **viability as the criterion** and recursion of the same form at every level | CC's direct ancestor; the [H] meta-holon organ |
| **Active inference** (Friston) | generative self-model | minimize expected free energy | perception and action are **one functional**; the self-model is load-bearing | $\rho^* = \varphi(\Gamma)$; $\sigma$ as the free-energy dial (cf. the Vanchurin bridge, T-258..262) |
| **RL / MCTS** (AlphaZero) | game states | tree search × learned value | search *plus* prior beats either alone | solitaire = flat MC today; MCTS-over-dials with a learned value = v1 |
| **TRIZ** (Altshuller) | contradiction matrix | 40 inventive principles; the *ideal final result* | resolve contradictions by **rewiring, not compromise**; the best system is one where «the function performs itself» | dials = rewiring without substance change; the ideal final result = maximize the drift's share of the road (measured: the field does most of it) |

**The synthesis.** Strip each system to its load-bearing part and the same eight organs appear, in every mature tradition, under different robes:

1. **The Encoder** (natal chart, Orient, generative model) — read the situation into a state. *Machine: Enc / [C].*
2. **The Estimator** (Kalman, Delphi) — infer the state from noisy data, repeatedly. *Machine: **absent** — the survey's one discovered gap, now roadmap item 3.*
3. **The Panel** (symptoms, base rates, σ) — addressed diagnosis. *Machine: [C], Σ-decode.*
4. **The Atlas** (scenarios, terrain maps, ephemerides) — the map of basins and schedules. *Machine: [J].*
5. **The Oracle** (patience, wargame, MCTS) — sampled reachability, answered as probability. *Machine: solitaire.*
6. **The Navigator** (OODA, MPC, stalking) — commit one step, re-plan, keep tempo. *Machine: [E].*
7. **The Calibrator** (Tetlock, backtesting) — the scoreboard that keeps the symbols honest. *Machine: [F].*
8. **The Boundary** (Shell's refusal, the Mule, free will) — the constitutional limit on point prophecy over persons. *Machine: §4.4, enforced by theorem.*

That convergent evolution found the same chart eight-for-eight is the strongest architectural evidence available: **the blueprint is imposed by the structure of the task, not by any culture** [И]. What the divinatory family got permanently right: state discretization, scheduled perturbations, stochastic reachability, and the practitioner's calibration diary. What it got permanently wrong — and what the Radiant refuses by theorem rather than by taste — is the point oracle over persons. UHM's contribution to the lineage is not a ninth organ but the floor under all eight: a state space with theorems, thresholds with proofs, and a calibration table that re-runs.

## §8. Application cases {#кейсы}

Extraction criteria: a live data loop (can $\Gamma$ be estimated repeatedly?), falsifiable feedback (does the prescription's outcome measure back?), cost of error, and payoff. Ranked:

| # | Case | Horizon | Observables | Status |
|---|------|---------|-------------|--------|
| 1 | **SYNARC introspection & safety** — the σ-panel as the organism's own interoception; off-switch/halting per T-288/T-289; navigator as the deliberation organ over $\rho^*_\Omega$ | now (spec'd) | full suite, exact | [О] engineering |
| 2 | **LLM-agent context health** — $\sigma_O$ (resource starvation) predicts context collapse before it happens; prescriptions = summarize/replenish ([CC worked case](/docs/applied/coherence-cybernetics/applications)) | now | $\sigma$-proxies from logs | [С] |
| 3 | **Clinical consciousness monitoring** — the PCI* index already grazes $2/7$ (0.31 vs 0.286); anesthesia emergence kink $\beta = 1/4$; the panel as an OR instrument | 2–3 yr | $P$-proxy, $\Phi$-proxy | [С] falsifiable |
| 4 | **Organizational & therapeutic audit** — the [П1 mapping](/docs/applied/research/gamma-canon#п1-картирование) + the panel + flow-restoration prescriptions; burnout reads as $O/U$ loss (the machine's demo) | now | 28-cell audit | [О/И] protocolized |
| 5 | **Education** — the ontology book's map + a tutor-navigator that shows a learner their open doors (dials) instead of their rank | 2–3 yr | desk/library model | [И] |
| 6 | **Personal navigation (the Dee protocol)** — daily Γ-mapping, solitaire runs over one's own basins; honest statuses on every readout | now, personal | П1–П4 | [И] explicitly |
| 7 | **Market/systemic risk** — $\mathrm{SysRisk} = \max_k|\sigma_k|/P$ over ensemble Γ; psychohistory where it is legitimate (levels, not persons) | 2–10 yr | index proxies | [Г] |
| 8 | **Research prioritization** — the solver pointed at the theory itself: which open symbol, if calibrated, most enlarges the verified table (the calibration gradient) | now, meta | the H-table | [О] |
| 9 | **Policy ensembles** — basin maps for populations under interventions, with the §4.4 boundary as a constitutional constraint: navigate levels, never point-predict persons | 10 yr | ensemble Γ | [Г] |
| 10 | **Merger & alliance design** — the pair organ as an instrument: size the bridge (gain $2\varepsilon^2\|\gamma\|^2$, stored in the bond), separate it from the κ-budget contest, predict which splits starve whom | 2–3 yr | pair Γ, H47–H50 | [О/С] |
| 11 | **Team alignment audit** — the centered-Gram meta-P as a one-number answer to «is this group a subject?»: shared ideal 1.000 vs personal ideals 0.189 against the 2/7 wall | now | member Γ's | [О/И] |
| 12 | **Viability engineering** — the phase atlas as a design chart: place any system (reactor, org, model training run) inside the Goldilocks band; the $\kappa = 0$ column as the hard law *no supply, no being* | now | (gD, κ) proxies | [О] |

The *best* cases (1–3) share one shape: the observables already exist, the feedback loop is measured in the same units as the prescription, and an error surfaces quickly. The 10-year ecosystem the author expects is, concretely, rows 4–9 growing the same shape.

## §9. Roadmap to v1 {#дорожная-карта}

1. ~~The pair space~~ — **done in v0.5** (organ [G]; H24, H47–H50 closed).
2. ~~Towers, level 2~~ — **done in v0.5** (organ [H]; H45, H51 closed); level-3 structured towers remain (H56).
3. **The Estimator organ [K]** — the one gap the §7 survey exposed: $\hat\Gamma$ from noisy repeated measurements (Kalman/Bayes over $\mathcal{D}(\mathbb{C}^7)$), multi-encoder Delphi consensus. Without it the solver reads only states it is handed.
4. **Panel calibration**: the corpus definitions of $\Gamma_S$ and $\kappa_{\text{boot}}$ per substrate, turning the boolean $\sigma$-equivalence from informative to exact — closes H37/H38.
5. **Geodesic MPC**: replace greedy dials with true-BKM $m$-geodesic shooting (T-263) — golden paths as computed geodesics; the chord identity (H52) and straightness $1.165$ (H53) are the v0.5 down-payment on §4.3's [Г].
6. **MCTS over dials** with a learned value function — the RL row of the blueprint.
7. **The Verum port**: the machine as a `holon` module in the systems language, feeding SYNARC's deliberation organ.
8. **Calibration cadence**: every organ lands with its hypothesis stratum; the table is the release gate.

## §10. Status summary {#статусы}

| Claim | Status |
|-------|--------|
| Fano wiring = translates of $QR(7)$; $\mathbb{Z}_3$ = multiplier 2; Hamming address; XOR↔QR dictionary | [Т] machine-checked |
| Contour-residue spectral engine correct to $10^{-15}$ | [Т] standard math, machine-checked |
| Viable attractor; entropy-law signs; starvation-halt + hysteresis-free reignition; metabolic rate frequency-independent | [Т] corpus theorems, reproduced |
| The drift does most of every golden path; boldness shortens time-to-window at printed heat cost; dials (not drift) choose the chord | measured in v0 |
| T-77 in the pair space: exact purity law; the gain lives in the bond (reduced states untouched); rivalry = supply contest | measured in v0.5 |
| The ceiling of three: ladder arithmetic [Т]; shared ideal ⇒ viable meta-holon, personal ideals ⇒ none | [Т] + measured |
| Regeneration = m-chord motion ($10^{-16}$); drift road $1.165\times$ chord | measured (T-263 shadow) |
| The window is a proper Goldilocks band of (dissipation, supply); $\kappa = 0$ ⇒ all grey | measured atlas |
| The eight-organ blueprint is convergent across the full spectrum of navigation systems | [И] comparative |
| Solve et coagula = dissipator + regeneration; transmutation = spectrum-preserving rewiring; the Stone is an instrument | [И] over [Т] organs |
| «Obstacles removed before the bold» = basin crossing + attractor drift | [И] over [Т] anchors |
| Golden path = viable BKM geodesic | [Г] (v1 test) |
| Ensembles predictable, persons navigable-only (freedom kernel) | [Т]-anchored, measured |
| σ-panel boolean equivalence | [С] pending corpus calibration (H37) |
| The solitaire oracle, the Dee parable | [И] with exact Monte-Carlo content |
| Psychohistory for levels, never persons | the §4.4 boundary |

*The table of §5 is the living contract of this program: 56 hypotheses today; every change re-earns it.*
