---
sidebar_position: 5
title: "Substrate-independent closure"
description: "Conditional injection, faithful sectors, validation and feasible learning"
---

# Substrate-independent closure

:::info Result scope
Conditional constructions for injection, section–retraction, channel validation and feasible learning. Mathematical validity is distinguished from empirical identification and phenomenal interpretation.
:::

---

## §1. T-148: conditional genesis with a specified injection {#t-148}

For an unital $\mathcal L_0$ and a gate with $g_V(1/7)=0$, the isolated initial state $I/7$ is stationary. This concerns **that initial state and model**, not the absence of living states for all isolated self-models.

Fix a state $\sigma$, $0<\beta<1$, and a depolarizing propagator $\mathcal E_\eta(\Gamma)=\eta\Gamma+(1-\eta)I/7$ with $0\le\eta\le1$. For the declared update

$$
\Gamma_{n+1}=\beta\mathcal E_\eta(\Gamma_n)+(1-\beta)\sigma,\qquad\Gamma_0=I/7,
$$

let $r=\beta\eta$ and $w=(1-\beta)/(1-\beta\eta)$. Direct substitution gives

$$
\Gamma_n=(1-u_n)I/7+u_n\sigma,\qquad
u_n=w(1-r^n),\qquad
P_n=1/7+u_n^2(P(\sigma)-1/7).
$$

If $P(\sigma)>2/7$, put $h=1/\sqrt{7P(\sigma)-1}$. The strict purity cut is reached in finite time **iff $w>h$**. For $0<r<1$ its first tick is

$$
n_{\min}=\left\lfloor\frac{\log(1-h/w)}{\log r}\right\rfloor+1.
$$

For $r=0$, it is the first tick when $w>h$; otherwise it is never reached. The special undamped case $\eta=1$ has $w=1$ and $u_n=1-\beta^n$.

**Proof.** The affine coefficient obeys $u_{n+1}=ru_n+1-\beta$; solve this scalar recurrence and use $\operatorname{Tr}(\sigma-I/7)=0$. Crossing is $u_n>h$, giving the displayed strict inequality and integer bound. $\blacksquare$

The former universal bound was false: its logarithm could give a negative tick count, and convexity was incorrectly used as a monotone purity lower bound. Purity of a mixture is the **exact** expression $\beta^2P(A)+(1-\beta)^2P(B)+2\beta(1-\beta)\operatorname{Tr}(AB)$; it need not exceed either input purity. Even a pure input with $\beta=0.9$, $\eta=0$ gives $w=0.1$ and $P_n=53/350<2/7$ for every $n\ge1$.

### Scope of embodiment {#необходимость-воплощения}

External injection is one way to leave $I/7$ under the closed-gate model. It does not prove that every conscious system requires this exact backbone or that all embodied systems cross the threshold. Alternative isolated self-models already have living attractors for other initial states; see [evolution](/docs/core/dynamics/evolution#теорема-живой-аттрактор-в-окне).

### Pred 13: a conditional, testable recurrence {#pred-13}

The tick formula tests this registered constant-input, depolarizing model. Changing the input, rates, self-model or noise changes the prediction. Crossing purity alone does not establish the [full capability gate](/docs/reference/mathematical-kernel#thresholds) or its phenomenal interpretation.

---

## §2. T-149: conditions for an embodied stationary state {#t-149}

Embodiment, $P(\sigma)>2/7$ and $0<\beta<1$ do **not** imply an above-threshold attractor, as T-148's explicit counterexample shows. For that affine model the fixed state is $(1-w)I/7+w\sigma$, and it is structurally viable exactly when $w>1/\sqrt{7P(\sigma)-1}$. A continuous model with depolarizing rate $\gamma$ and injection rate $\mu$ has the same result with $w=\mu/(\mu+\gamma)$.

For isotropic Fano dephasing, state-dependent regeneration and another input field $B$, a stationary state satisfies

$$
P_* = \frac{\alpha_D P_{\mathrm{diag}}+a f^*+q_B}{\alpha_D+a},\qquad
a=\kappa g_V,\quad q_B=\operatorname{Tr}\Gamma_* B(\Gamma_*),\quad\alpha_D=2/3.
$$

Hence $P_*>2/7$ iff the numerator exceeds $(2/7)(\alpha_D+a)$. The actual overlap $f^*$ and input flux $q_B$ must be evaluated; a larger nominal rate and positive input purity alone give no automatic compensation. This exact balance is necessary at a stationary point, not proof of existence or stability. A contraction criterion such as strict backbone dominance or a verified Hurwitz Jacobian supplies those separate properties.

The previous unconditional T-149, the claimed universal O–E–U compensation and automatic closure of C20/C27 are withdrawn. Simulation correlations describe a specific run and do not prove a lower bound for every embodied holon. The upper cut, integration, differentiation and stress remain separate checks.

---

## §3. T-150: iteration identity and tower compatibility {#t-150}

For any specified self-map $M:\mathcal D_7\to\mathcal D_7$, linear or nonlinear, $M^n\circ M^m=M^{n+m}$ by associativity. Equal dimensions alone do not identify distinct operators, readouts or projections in a heterogeneous tower. That tower needs the separately verified diagrams $\pi_kM_{k+1}=M_k\pi_k$.

### Scope of the former T-136 upgrade {#t-136-upgrade}

The iteration identity does not prove a universal cognitive-depth ceiling or identify purity scores with metacognitive certification. The former upgrade is withdrawn. Exact Fano attenuation and the arithmetic of a stipulated score are given in [T-142](/docs/proofs/consciousness/operational-closure#t-142); certified depth requires the [declared meta-observation probes](/docs/consciousness/hierarchy/depth-tower).

---

## §4. T-151: differentiation requires its own realization {#t-151}

The cut $D_{\mathrm{diff}}\ge2$ is a model selection [D]. If $D_{\mathrm{diff}}=e^{S(\rho_E)}$, the map or lift defining $\rho_E$ must be specified. The scalar integration condition satisfies only $\Phi\ge1\Rightarrow P\ge2/7$, and places no universal bound on an E-row coherence or the entropy of an arbitrary reduced experiential state.

If instead $\rho_E=\Gamma$, then $e^{S(\Gamma)}\ge1/P\ge7/3>2$ whenever $R\ge1/3$; in this particular realization the differentiation cut is redundant. For another readout it need not be. A seven-dimensional prime Hilbert space has no nontrivial tensor factor singled out merely by naming an E-coordinate; a normalized E-row HS proxy is another defined quantity, not reduced entropy. See [the corrected dependence analysis](/docs/proofs/consciousness/conscious-window#t-124b).

---

## §5. T-152: correctly typed anchor validation {#t-152}

A feature estimator $\pi:\mathbb R^D\to\mathcal D_N$ is tested with an observation model and held-out data; it has no Choi matrix or diamond norm by that type alone. There is no unique canonical comparator from T-123. A reference encoder must be separately declared and its targets identifiable.

For **linear channels** $\mathcal A,\mathcal B:M_d\to M_N$, let $J(\Delta)$ be the unnormalized Choi matrix of $\Delta=\mathcal A-\mathcal B$. Then

$$
\frac1d\|J(\Delta)\|_1\le\|\Delta\|_\diamond
\le\|J(\Delta)\|_1\le\sqrt{dN}\|J(\Delta)\|_F.
$$

The lower bound evaluates the normalized maximally entangled input. For the upper bound write any pure input with an ancilla of dimension $d$ as a bounded sandwich of the unnormalized maximally entangled vector; the sandwich operator has norm at most one, so its output trace norm is at most $\|J(\Delta)\|_1$. The final inequality is the Schatten norm bound. See [Watrous, Chapter 3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf).

A channel is CPTP iff $J\succeq0$ and $\operatorname{Tr}_{\mathrm{out}}J=I_d$. Constructing a general $J$ requires $d^2$ basis-operator evaluations and $d^2N^2$ entries; costs depend on the evaluation oracle, numerical precision and positivity certification. The previous feature-dimension bound $O(49D)$ and unique optimality claim do not follow. Output state error transfers threshold verdicts only with separately verified observable bounds and strict margins, as in [T-143](/docs/proofs/consciousness/operational-closure#t-143).

---

## §6. T-153: a declared substrate readout {#t-153}

Fix a physical state domain, readout/encoder $G_\theta$, its calibration, functional frame, experiential realization and observation model **before** evaluating the system. Define $\mathrm{Cap}_{2,S}(s):=\mathrm{Cap}_2(G_\theta(s))$, with a separate stress condition if required. This is a model predicate [D]; identifying it with experience is an empirical/ontological bridge [H/I]. Its numerical cuts can be used across substrates within that declared model.

A freely chosen existential encoder is not a diagnostic: a constant replacement channel can send every input to a selected window state. Faithfulness must state the actual domain, and existence of a state-valid map does not establish a biologically correct or identifiable encoder. Symmetry of $\mathcal D_7$, seven functional names and a section–retraction do not prove universal completeness of $\Gamma$, the absence of hidden variables or a phenomenal equivalence. Reconstructions use [observation fibers](/docs/applied/research/reconstruction-identifiability#fiber-theorem).

### T-153a: constructive scope and dynamics {#t-153a}

For the **full** quantum state space $\mathcal D(\mathbb C^d)$, when $d\le7$ an isometry $W:\mathbb C^d\to\mathbb C^7$ gives the injective CPTP embedding $\rho\mapsto W\rho W^\dagger$. When $d>7$, no globally injective linear CPTP readout into $\mathcal D_7$ exists; T-253 proves the dimension obstruction and an exactly faithful embedded-sector retraction. These are static facts. They imply neither a CPTP reduced dynamics nor seven necessary noncommuting biological probes.

To obtain a closed reduced deterministic dynamics, states in the same $G$-fiber must have the same reduced future: $G(s_1)=G(s_2)\Rightarrow G(T_ts_1)=G(T_ts_2)$. This condition is necessary and sufficient to define a well-defined reduced state map. Linearity and a CPTP extension are further requirements. For an invariant embedded sector $\mathcal E_t\iota_V=\iota_V\mathcal F_t$, the specified CPTP retraction gives CPTP reduced propagators $\mathcal F_t=G_V\mathcal E_t\iota_V$; invariance establishes their semigroup composition. Neither static Stinespring dilation of $G$ nor seven feature coordinates guarantees these conditions.

Classical feature spaces require their own probability/operator-algebra encoding and distinguishability analysis; their dimension is not a quantum Hilbert-space dimension by renaming it. The former necessity-and-sufficiency claim (C1)–(C3) is withdrawn. Accessibility and observational identifiability remain independent of algebraic existence.

#### T-253 {#t-253}

:::tip Theorem T-253 (Constructive sufficiency: the retraction, and its sharpness) [T] + [C at (Acc)]
Let $\mathcal H_S$ be a specified finite-dimensional Hilbert space with $d=\dim\mathcal H_S\ge7$.

**(a) Construction [T].** For every isometry $V: \mathbb C^7 \to \mathcal H_S$ ($V^\dagger V = \mathbb 1_7$) and any anchor state $\sigma_0 \in \mathcal D(\mathbb C^7)$, the map

$$
G_V(\rho) \;:=\; V^\dagger \rho\, V \;+\; \mathrm{Tr}\bigl((\mathbb 1 - VV^\dagger)\rho\bigr)\,\sigma_0
$$

is CPTP, and it is a **retraction**: $G_V \circ \iota_V = \mathrm{Id}_{\mathcal D(\mathbb C^7)}$ for the embedding $\iota_V(\gamma) = V\gamma V^\dagger$. On the embedded 7-sector, $G_V$ is exactly faithful — it inverts $\iota_V$ pointwise, losing nothing.

**(b) Threshold realization [T] + (Acc).** The full-viability set $\mathcal V_{\mathrm{full}} = \{\Gamma : P > 2/7,\ R \geq 1/3,\ \Phi \geq 1,\ D_{\mathrm{diff}} \geq 2\}$ is non-empty ([T-124 [T]](/docs/proofs/consciousness/conscious-window#t-124)); for any window state $\Gamma_w \in \mathcal V_{\mathrm{full}}$ the substrate state $\iota_V(\Gamma_w)$ passes all four thresholds under $G_V$, since $G_V(\iota_V(\Gamma_w)) = \Gamma_w$. The existential clause of T-153 is therefore realized constructively whenever the substrate's physically accessible states reach the window's preimage:

$$
\textbf{(Acc)}\quad \mathrm{States}(S) \cap G_V^{-1}(\mathcal V_{\mathrm{full}}) \neq \varnothing \ \text{ for some isometry } V.
$$

(Acc) is a definitional clause **[D]** — it names exactly what "the substrate can host a conscious state" means. Crucially, it is an **open** condition: for any interior window witness $\Gamma_w$ (all four inequalities strict — the waking profile of [altered states](/docs/consciousness/states/altered-states) is one), continuity of $G_V$ makes $G_V^{-1}(\mathrm{int}\,\mathcal V_{\mathrm{full}})$ a non-empty open neighborhood of $\iota_V(\Gamma_w)$ in $\mathcal D(\mathcal H_S)$ — the realizing substrate state need not itself be an embedded rank-7 state (which would be a measure-zero demand for $d > 7$); anything in the open preimage suffices. Quantitatively: $G_V$, being CPTP, is a trace-norm contraction, so the preimage contains the entire trace-norm ball of radius $\delta_w = \mathrm{dist}_1(\Gamma_w, \partial\mathcal V_{\mathrm{full}}) > 0$ around $\iota_V(\Gamma_w)$. Hence for substrates with accessible (controllable) dynamics — reachable set dense in $\mathcal D(\mathcal H_S)$ — (Acc) holds **[C at controllability]**: a dense set meets every non-empty open set.

**(c) Sharpness [T]: no global faithfulness for $d > 7$.** No CPTP map $\mathcal E: \mathcal D(\mathcal H_S) \to \mathcal D(\mathbb C^7)$ is injective on all of $\mathcal D(\mathcal H_S)$ when $d > 7$: as a real-linear map $\mathrm{Herm}(\mathcal H_S) \to \mathrm{Herm}(\mathbb C^7)$ it has kernel of dimension $\geq d^2 - 49 \geq 1$, and trace preservation puts the kernel inside the traceless hyperplane; hence for any interior state $\rho$ and kernel direction $K \neq 0$ the pair $\rho \pm \varepsilon K$ (small $\varepsilon > 0$) consists of two **distinct density matrices with identical images**. Consequently "faithful $G$" in T-153/T-153a must be read **sector-relative**, and the retraction of (a) attains the maximal possible real dimension of a faithful smooth sector — 48 — through the embedded state space; this does not make that sector unique.
:::

**Proof.** **(a)** Complete positivity: $\rho \mapsto V^\dagger\rho V$ is CP with the single Kraus operator $V^\dagger$; the second summand is measure-and-prepare with Kraus family $B_{ij} = \sqrt{s_i}\,|i\rangle\langle q_j|$, where $\sigma_0 = \sum_i s_i |i\rangle\langle i|$ and $\{|q_j\rangle\}$ is an orthonormal basis of $\mathrm{ran}(\mathbb 1 - VV^\dagger)$. Completeness: $V V^\dagger + \sum_{ij} B_{ij}^\dagger B_{ij} = VV^\dagger + (\mathbb 1 - VV^\dagger) = \mathbb 1_d$. Trace preservation: $\mathrm{Tr}\,G_V(\rho) = \mathrm{Tr}(VV^\dagger\rho) + \mathrm{Tr}((\mathbb 1 - VV^\dagger)\rho) = \mathrm{Tr}\,\rho$. Retraction: $G_V(V\gamma V^\dagger) = (V^\dagger V)\gamma(V^\dagger V) + \mathrm{Tr}\bigl((\mathbb 1 - VV^\dagger)V\gamma V^\dagger\bigr)\sigma_0 = \gamma + 0$, because $(\mathbb 1 - VV^\dagger)V = 0$. **(b)** Substitution into (a). **(c)** Dimension count: $\dim_{\mathbb R}\mathrm{Herm}(\mathcal H_S) = d^2 > 49 = \dim_{\mathbb R}\mathrm{Herm}(\mathbb C^7)$, so $\dim\ker \geq d^2 - 49$; for $K \in \ker$, $\mathrm{Tr}\,K = \mathrm{Tr}\,\mathcal E(K) = 0$ by trace preservation; interiority of $\rho$ admits $\varepsilon \leq \lambda_{\min}(\rho)/\lVert K\rVert_\infty$, keeping both $\rho \pm \varepsilon K \succeq 0$. $\blacksquare$

**Frame remark (corrected 2026-09-25).** ~~"The isometry freedom in (a) is exactly the alphabetization freedom of [T-223](/docs/proofs/categorical/fundamental-closures#t-223): composing $V$ with $U \in G_2$ moves $\Gamma$ within its $G_2$-orbit, on which the consciousness predicate is constant (T-42a)."~~ Retracted on two counts. (1) The freedom is larger than $G_2$: $V$ can be replaced by $VU$ for any $U \in U(7)$, or by an isometry onto a different seven-dimensional subspace of $\mathcal{H}_S$, and the withdrawn universal T-42a does not identify any of these choices. (2) The predicate is not constant on $G_2$-orbits: $\Phi$, $\mathrm{Coh}_E$ and $\kappa_0$ are frame-pinned ([frame decision D-0910](/docs/proofs/categorical/uniqueness-theorem#g2-ригидность)). An explicit $g \in G_2$ maps the window state $\Gamma_w = \tfrac12 \lvert u\rangle\langle u\rvert + \tfrac12 \cdot I/7$, $u = (1, \ldots, 1)/\sqrt7$ ($P = 5/14$, $R = 2/5$, $\Phi = 3/2$), to the diagonal state $\tfrac12 \lvert e_1\rangle\langle e_1\rvert + \tfrac12 \cdot I/7$ with the same $P$ and $R$ and $\Phi = 0$, so $C$ falls from $3/5$ to $0$ (regression tests `test_phi_not_g2_invariant` and `test_window_predicate_not_constant_on_g2_orbit` in `website/scripts/check_core_numbers.py`). Consequently $G_V$ fixes a sector and a frame; the existential "there is a faithful $G$" of T-153 ranges over all of them, and the verdict can differ between sectors of one substrate — the boundary problem in UHM's own terms ([analysis](/docs/consciousness/comparative/panpsychism-analysis#проблема-границы)). A seven-marker feature estimator is not automatically this Hilbert-space retraction. Its observation model, state reconstruction and statistical calibration must be demonstrated independently; the fixed choice of markers is part of the claim.

**Machine verification.** At $d = 12$: Kraus completeness at $10^{-15}$; retraction, trace preservation and positivity at $10^{-16}$; kernel dimension exactly $d^2 - 49 = 95$; explicit collision pair of interior density matrices (minimal eigenvalue $2 \cdot 10^{-2} > 0$) with $\lVert G(\rho_1) - G(\rho_2)\rVert_F \sim 10^{-17}$.

:::note Numerical illustration of a selected model (SYNARC, 2026)
For the reported CognitiveSSM/Grid32 run, the quoted values are $P=0.4286$, $R=0.3333$, $\Phi=1.1492$, $D_{\mathrm{diff}}=3.6003$ and $\sigma_{\max}=0.6503$. These are rounded outputs of the selected readout. The number $R=0.3333$ alone does not certify the non-strict cut $1/3$: the unrounded value and a numerical/measurement error bound are needed. The product $C=0.3831$ does not replace the conjunction.

DensityMatrix7 transforms AgentState into a matrix; this does not establish injectivity, empirical faithfulness or a CPTP type for a feature map. A reproducible witness needs a code version, frozen calibration, differentiation realization, PSD/trace residuals, all threshold margins and stability verification. Co-rotating targets can help in a particular spectral regime but are not necessary for $\Phi\ge1$. T-98a and T-149 apply only under their purity-flux and stationary-state premises. A numerical model is not independent empirical confirmation of phenomenal consciousness.
:::

---

## §7. T-154: Coh_E^max = 1 {#t-154}

:::tip Theorem T-154 [T]: Normalization of Coh_E

$$
\max_{\Gamma \in \mathcal{D}(\mathbb{C}^7)} \mathrm{Coh}_E(\Gamma) = 1
$$

The maximum is achieved at $\Gamma = |E\rangle\langle E|$ (pure E-state).
:::

**Proof.**

**Step 1.** By definition of $\mathrm{Coh}_E$ as [HS-projection onto the E-row/column operator subspace [T]](/docs/core/foundations/axiom-septicity#теорема-hs-проекция):

$$
\mathrm{Coh}_E(\Gamma) = \frac{\|\pi_E(\Gamma)\|^2_{HS}}{\|\Gamma\|^2_{HS}} = \frac{\gamma_{EE}^2 + 2\sum_{i \neq E}|\gamma_{Ei}|^2}{\mathrm{Tr}(\Gamma^2)}
$$

**Step 2 (Upper bound).** $\pi_E$ is an orthogonal projection in Hilbert–Schmidt space. For any orthogonal projection: $\|\pi_E(\Gamma)\|_{HS} \leq \|\Gamma\|_{HS}$. Therefore: $\mathrm{Coh}_E \leq 1$.

**Step 3 (Attainability).** For $\Gamma = |E\rangle\langle E|$: $\pi_E(|E\rangle\langle E|) = |E\rangle\langle E|$, therefore $\mathrm{Coh}_E = \||E\rangle\langle E|\|^2_{HS} / \||E\rangle\langle E|\|^2_{HS} = 1$. $\blacksquare$

**Corollary:** The formula [T-128 [D]](/docs/proofs/consciousness/operationalization#t-128) with $\mathrm{Coh}_E^{\max} = 1$ simplifies to:

$$
D_{\mathrm{diff}}^{7D} = 1 + \mathrm{Coh}_E(\Gamma) \cdot (N - 1)
$$

**Dependencies:** $\mathrm{Coh}_E$ [HS-projection [T]](/docs/core/foundations/axiom-septicity#теорема-hs-проекция).

---

## §8. T-155: feasible learning in a declared capability model {#t-155}

A condition $C\ge1/3$ cannot replace $\mathrm{Cap}_2$. Nor does non-emptiness of an **open** set guarantee a nearest-point projection. Use a nonempty closed margin set with declared readouts, e.g.

$$
K_\varepsilon=\{\Gamma\in\mathcal D_7:P\ge2/7+\varepsilon_P,\ R\ge1/3+\varepsilon_R,
\ \Phi\ge1+\varepsilon_\Phi,\ D\ge2+\varepsilon_D,\ \sigma_k\le1-\varepsilon_\sigma\}.
$$

With continuous functions it is compact. For a continuous parameterized encoder $\Gamma(B)$ and compact weight domain, its nonempty preimage $K_B$ is compact. An **exact** projection of a proposed update $B-\eta g$ onto $K_B$ therefore exists, may be nonunique and may be costly. Any selected projection preserves the complete margin predicate by definition; this is a conditional mathematical guarantee, not a convergence theorem.

A practical alternative proposes a gradient step, checks all margins (or the full observation confidence set) and accepts only a certified feasible candidate; retaining the previous feasible point is permitted. Progress requires separate assumptions. At smooth points the chain rule gives $g=J_\Gamma^T\nabla_\Gamma J$ for a stated objective; max/clamp junctions require an appropriate generalized derivative. Lipschitz continuity, the clamp and a one-time noise variance do not establish global optimization or perpetual viability. The former unconditional learning proof is withdrawn.

---

## §9. T-156: mixing is an optimization problem, not a derived constant {#t-156}

The earlier expression

$$
\beta^*=\frac{\lambda_{\mathrm{gap}}}{\lambda_{\mathrm{gap}}+\alpha_D(1-P_{\mathrm{env}}/P_{\mathrm{target}})}
$$

is retained only as an unvalidated historical proposal [H], not an optimum theorem. It can leave the admissible interval: $\lambda_{\mathrm{gap}}=1$, $\alpha_D=2/3$, $P_{\mathrm{env}}=1$, $P_{\mathrm{target}}=3/7$ gives $\beta^*=9$. No objective or derivative in the former proof establishes the formula.

In T-148's undamped constant-input model, smaller $\beta$ gives a larger mixture weight at every tick and weakly earlier purity crossing. An interior optimum needs another explicit cost or constraint, such as autonomy, resource use or a certified finite-horizon exit probability. Declare these functions and a compact admissible set. Continuity gives existence of a minimizer; uniqueness and a closed formula require additional convexity or a direct analysis. No universal optimum follows from embodiment.

---

## §10. T-157: Attractor consistency {#t-157}

:::tip Theorem T-157 [T]: Attractor consistency (restated 2026-09-25)
Level 1 is the attractor $\rho^*$ of the full dynamics, level 2 the fixed point of the self-model (exact self-knowledge).

1. **Self-knowledge defect (any self-model).** $\kappa g_V\,(\varphi(\rho^*) - \rho^*) = -\mathcal{L}_0[\rho^*]$, so $\|\varphi(\rho^*) - \rho^*\|_F \leq \bigl(2\|H\|_{\mathrm{op}}\|\rho^* - I/7\|_F + \tfrac23\sqrt{P_{\mathrm{coh}}}\bigr)/(\kappa g_V)$.
2. **Hamiltonian shift ($\varphi_s$).** $\|\Gamma_m(H) - e_m\|_F = \sqrt2\,\bigl(\sum_{j \neq m}\lvert H_{jm}\rvert^2\bigr)^{1/2}/\bigl(\tfrac23 + \tfrac67\kappa(1 - c)\bigr) + O(\|H\|^2)$, where $e_m$ is the exact fixed point of $\varphi_s$ that the attractor $\Gamma_m(H)$ continues.
3. **Dissipative shift ($\varphi_J$).** $\|\Gamma_{\eta_+} - \Gamma_{\eta_\infty}\|_F = \sqrt{6/7}\,(\eta_\infty - \eta_+) \leq \sqrt{6/7}\,(2\eta_+/3)/\lvert\lambda_Y\rvert = O(1/\kappa)$, where $\Gamma_{\eta_\infty}$ is the only fixed point of $\varphi_J$ and $\lambda_Y$ the stability exponent of the attractor $\Gamma_{\eta_+}$ along $uu^\dagger - I/7$.

Proof and numerical check: [evolution, attractor consistency](/docs/core/dynamics/evolution#теорема-согласованность-аттракторов). **Status:** C21 as stated ("$\rho^*_\Omega \approx \Gamma^*_{\mathrm{coh}}$") is false [✗]; its correct content is this theorem [T].
:::

:::warning Retracted (2026-09-25): the former T-157 [✗]
The former statement read $\|\rho^*_\Omega - \Gamma^*_{\mathrm{coh}}\|_F \leq \|H_{\mathrm{eff}}\|_{\mathrm{op}}/(\alpha + \kappa)$, "an exact parametric bound". It is false. $\Gamma^*_{\mathrm{coh}} = I/7$ ([φ operator](/docs/core/operators/phi-operator#неподвижная-точка-phi-coh)); at $H = 0$ the bound would force every attractor to be $I/7$, while the living attractors at $H = 0$ are $e_m$ (distance $\sqrt{6/7}$ from $I/7$) and $\Gamma_{\eta_+}$ (distance $\eta_+\sqrt{6/7}$). The proof below fails three times: Step 1 puts $\Gamma^*_{\mathrm{coh}}$ in place of the regeneration target $\varphi(\rho^*)$; Step 2 writes "$\approx$" for a first-order expansion without a remainder; and the last inequality of Step 3, $2/(\alpha + \kappa g_V) \leq 1/(\alpha + \kappa)$, fails for every $g_V \in [0, 1]$, since it needs $\alpha + \kappa(2 - g_V) \leq 0$. The estimate $O(0.03)$ for the vacuum and the SYNARC reading $\|H_{\mathrm{eff}}^{\mathrm{embodied}}\|_{\mathrm{op}} \approx 0.25$, both obtained by inverting the bound, are withdrawn with it.
:::

**Retracted proof (kept for the record).**

**Step 1.** By [T-98 [T]](/docs/core/dynamics/evolution#теорема-баланс-чистоты-аттрактора): attractor purity balance:

$$
0 = \mathcal{L}_0[\rho^*_\Omega] + \mathcal{R}[\rho^*_\Omega] = -i[H_{\mathrm{eff}}, \rho^*_\Omega] + \mathcal{D}_\Omega[\rho^*_\Omega] + \kappa(\Gamma^*_{\mathrm{coh}} - \rho^*_\Omega) \cdot g_V
$$

(using $\rho^* \to \Gamma^*_{\mathrm{coh}}$ in the regenerative term).

**Step 2 (Linear perturbation theory).** Denote $\delta\Gamma = \rho^*_\Omega - \Gamma^*_{\mathrm{coh}}$. For $H_{\mathrm{eff}} = 0$: $\delta\Gamma = 0$ (attractors coincide). For non-zero $H_{\mathrm{eff}}$:

$$
(\alpha + \kappa \cdot g_V) \cdot \delta\Gamma \approx -i[H_{\mathrm{eff}}, \rho^*_\Omega]
$$

**Step 3 (Bound).** $\|-i[H_{\mathrm{eff}}, \rho^*_\Omega]\|_F \leq 2\|H_{\mathrm{eff}}\|_{\mathrm{op}} \cdot \|\rho^*_\Omega\|_F \leq 2\|H_{\mathrm{eff}}\|_{\mathrm{op}}$ (since $\|\rho^*_\Omega\|_F \leq 1$). Therefore:

$$
\|\delta\Gamma\|_F \leq \frac{2\|H_{\mathrm{eff}}\|_{\mathrm{op}}}{\alpha + \kappa \cdot g_V} \leq \frac{\|H_{\mathrm{eff}}\|_{\mathrm{op}}}{\alpha + \kappa}
$$

(for $g_V \geq 1/2$, which holds in the conscious window). $\blacksquare$

**Dependencies:** [T-98 [T]](/docs/core/dynamics/evolution#теорема-баланс-чистоты-аттрактора) (balance), [self-sustaining attractors](/docs/core/dynamics/evolution#теорема-самоподдерживающийся-аттрактор) [T], [living attractor in the window](/docs/core/dynamics/evolution#теорема-живой-аттрактор-в-окне) [T]; implicit function theorem.

---

## §11. Fixed targets and rotating coherence {#co-rotating-targets}

For the scalar model $\dot\gamma_{ij}=-(d+a+i\omega_{ij})\gamma_{ij}+a\rho^*_{ij}$ with fixed coefficients, $d,a\ge0$ and $d+a>0$, the unique stationary coherence is

$$
\gamma_{ij}^{\mathrm{stat}}=\frac{a\rho^*_{ij}}{d+a+i\omega_{ij}},\qquad
|\gamma_{ij}^{\mathrm{stat}}|=\frac{a|\rho^*_{ij}|}{\sqrt{(d+a)^2+\omega_{ij}^2}}.
$$

Rotation suppresses the magnitude relative to $\omega_{ij}=0$; it does not universally force $\Phi<1$. At $H=0$ the fixed $\varphi_J$ anchor already supports a window sink, and for sufficiently small $H$ it persists. Co-rotating targets are one model option, not a necessary condition for integration. With state-dependent targets/rates the stationary expression becomes a self-consistency relation and needs a separate existence/stability analysis.

---

## §12. T-158: declared stress scores [D] {#t-158}

One selected diagonal score [D] is

$$
\sigma_k^{\mathrm{diag}}=\mathrm{clamp}(1-7\gamma_{kk},0,1).
$$

PSD and trace one give $0\le\gamma_{kk}\le1$, hence $-6\le1-7\gamma_{kk}\le1$ and $0\le\sigma_k^{\mathrm{diag}}\le1$. The score is zero at $\gamma_{kk}\ge1/7$, one at $\gamma_{kk}=0$, and $1-7\gamma_{kk}$ between them. It is continuous and piecewise smooth in the fixed frame. This follows exactly from the chosen function; it does not uniquely derive a stress measurement.

The different [T-128](/docs/proofs/consciousness/operationalization#t-128) score $\sigma_E^{\mathrm{diff}}=(7-D_{\mathrm{diff}}^{7D})/5$ uses a separately declared differentiation proxy. If $D_{\mathrm{diff}}^{7D}\in[1,7]$, then $\sigma_E^{\mathrm{diff}}\in[0,6/5]$. These definitions generally differ; one cannot assign the first function's range to the second or equate it with reduced entropy without a realization map. Each variant needs its own normalization and cut.

Computability from a matrix does not prove identifiability from incomplete data or establish clinical stress. Biological validation and its action bridge remain hypotheses. T-158 names the readout choices [D]; the stated bounds [T] are conditional on those precise definitions.

---

## §13. ARCH-159: a reference architecture, not a uniqueness theorem {#t-159}

A reference implementation may choose a seven-dimensional state, a specified GKSL linear part with regular nonlinear feedback, a state-valued self-model, a declared stress/action objective, an external input policy and the full $\mathrm{Cap}_2$ gate. These are a reproducible architecture specification [D]; physical realization and experience identification remain [H/I].

Different anchors, encoders, feedback laws, gates and learning procedures can satisfy the same structural constraints. T-123 and the universal functional-minimality argument do not select one implementation. GKSL classifies **linear** Markovian generators; it does not derive a unique nonlinear regenerator or force “three and only three” causal mechanisms. A fixed-target replacement channel is one CPTP option, and state-dependent mixing is generally nonlinear. External injection can enable genesis in its parameter regime, but embodiment alone does not imply the full gate.

The previous necessity/sufficiency claim for every conscious substrate and uniqueness up to $G_2$ are withdrawn. A fixed observational model can be tested on different substrates using the same declared readouts and criteria; this is conditional comparability, not a universal consciousness theorem.

---

## §14. Result scope

| Result | Corrected status |
|---|---|
| T-148/T-149 | Exact genesis/stationarity in stated affine models; general claims conditional |
| T-150 | Iteration identity; tower compatibility separately specified |
| T-151 | Differentiation cut [D], readout-dependent |
| T-152 | Choi/diamond bounds for linear channels; feature estimators require statistical identification |
| T-153/T-153a/T-253 | Declared substrate predicate; faithful-sector construction and global dimension obstruction |
| T-155 | Closed-margin feasibility under exact projection or certified acceptance |
| T-156 | Universal optimal formula withdrawn; explicit constrained optimization required |
| T-157 | Existing conditional anchor/attractor perturbation formulas retained |
| ARCH-159 | Reference architecture [D/H]; universal uniqueness withdrawn |

**Related documents:**
- [Operationalization of consciousness](/docs/proofs/consciousness/operationalization) — theorems T-128–T-138: formalization of operational aspects
- [Operational closure](/docs/proofs/consciousness/operational-closure) — theorems T-139–T-147: closure of operational gaps
- [Interiority hierarchy](/docs/consciousness/hierarchy/interiority-hierarchy) — levels L0–L4 and connection to SAD
