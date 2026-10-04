---
sidebar_position: 2
title: "Conscious window: T-123 — T-127, C27"
description: "Identifiability, conditional window witnesses, stability and threshold dependence"
---

# Conscious Window

:::info Scope
Explicit conditions for reconstruction, nonempty window witnesses, local stability and a viable basin. Matrix identities are distinguished from threshold choices and empirical interpretations.
:::

---

## §1. Reconstruction and identifiability (replacement for T-123) {#t-123}

:::warning T-123 withdrawn, 2026-10-03
A seven-dimensional state space and its symmetry group do not prove a unique neural or digital encoder, canonical empirical axis meanings or equivalence of all representations. The former proof invoked the withdrawn universal readings of T-42a and T-40f. A comparison $\pi_2\circ\pi_1^{-1}$ also requires an inverse of $\pi_1$, which continuity does not provide.
:::

The valid replacement is the [observation-fiber theorem](/docs/applied/research/reconstruction-identifiability#fiber-theorem): with a calibrated observation-law map $\mathcal O$, exact data determine the fiber $\mathcal O^{-1}(\mathcal O(\Gamma))$. The state is unique if this fiber is a singleton; a particular functional is identifiable if it is constant on the fiber. For linear Hermitian means, a complete traceless frame of rank $48$ is sufficient for unique reconstruction of a general state in $\mathcal D(\mathbb C^7)$; conditioning and finite noise determine uncertainty. Covariance is a codomain property, not an injectivity theorem for the encoder.

A residual group is allowed only when its orbits coincide with the observation fibers for the stated target and calibration. Labels or phase-sensitive observations can reduce that group to the identity. An empirical encoder is therefore a declared model whose identifiability and held-out performance must be demonstrated. Ontological interpretation remains a separate bridge; numerical state validity does not establish it.

---

## §2. Non-emptiness of a realized window (T-124) {#t-124}

For the four cuts defined in the [kernel](/docs/reference/mathematical-kernel#thresholds), set $\mathcal V_{\mathrm{full}}=\{\Gamma:\mathrm{Cap}_2(\Gamma)\land\forall k\ \sigma_k(\Gamma)<1\}$. The following construction proves non-emptiness with the stated readouts: $\rho_E=\Gamma$, $D_{\mathrm{diff}}=e^{S(\Gamma)}$ and the stress proxy $\sigma_k=\mathrm{clamp}(1-7\gamma_{kk},0,1)$. With another experiential lift/readout or stress function, the corresponding inequalities must be checked anew; these choices are not forced by the matrix formalism.

### Proof (constructive) {#доказательство-t124}

**Step 1.** Consider the family $\Gamma_\lambda = (1-\lambda)\,I/7 + \lambda\,|\psi\rangle\langle\psi|$, where $|\psi\rangle = \frac{1}{\sqrt{7}}\sum_{k=0}^{6}|k\rangle$ is an equal-amplitude vector.

Spectrum: one eigenvalue $\frac{1+6\lambda}{7}$ (multiplicity 1) and six eigenvalues $\frac{1-\lambda}{7}$ (multiplicity 6). From this:

$$
P(\Gamma_\lambda) = \frac{1}{7} + \frac{6\lambda^2}{7}, \quad
R = \frac{1}{7P} = \frac{1}{1 + 6\lambda^2}, \quad
\Phi(\Gamma_\lambda) = 6\lambda^2
$$

**Step 2.** For $\lambda \in (1/\sqrt{6},\; 1/\sqrt{3}]$:

| Indicator | Value | Condition |
|------------|----------|---------|
| $P$ | $(2/7, 3/7]$ | $\checkmark$ |
| $R$ | $[1/3, 1/2]$ | $\geq 1/3\;\checkmark$ |
| $\Phi$ | $[1, 2]$ | $\geq 1\;\checkmark$ |

Boundary values: at $\lambda = 1/\sqrt{6}$ we get $R = 1/2$ (inclusive), at $\lambda = 1/\sqrt{3}$ — $R = 1/3$ (inclusive).

**Step 3 (σ-condition).** By canonical definition ([T-92 [D]](/docs/applied/coherence-cybernetics/theorems#теорема-101-эквивалентность-условий)):

$$
\sigma_k = \mathrm{clamp}(1 - 7\gamma_{kk},\; 0,\; 1)
$$

For equal-amplitude $\Gamma_\lambda$ all diagonal elements equal $\gamma_{kk} = 1/7$ for all $k$ (since $|\psi\rangle = \frac{1}{\sqrt{7}}\sum_k|k\rangle$ is an equal-amplitude vector). Therefore:

$$
\sigma_k = \mathrm{clamp}(1 - 7 \cdot \tfrac{1}{7},\; 0,\; 1) = \mathrm{clamp}(0,\; 0,\; 1) = 0 < 1 \quad \forall k
$$

All $\sigma$-conditions ($\sigma_k < 1$) are satisfied **without any perturbation**.

**Step 4 ($D_{\mathrm{diff}}$).** Eigenvalues of $\Gamma_\lambda$: $\{(1+6\lambda)/7\; (\times 1),\; (1-\lambda)/7\; (\times 6)\}$. For $\lambda \in (1/\sqrt{6}, 1/\sqrt{3}]$: two distinct eigenvalues, $\mathrm{rank}(\Gamma_\lambda) = 7$.

Von Neumann entropy: $S_{vN} = -\frac{1+6\lambda}{7}\ln\frac{1+6\lambda}{7} - \frac{6(1-\lambda)}{7}\ln\frac{1-\lambda}{7}$.

At $\lambda = 1/\sqrt{6} \approx 0.408$: eigenvalues $\approx 0.493$ (×1) and $\approx 0.085$ (×6), $S_{vN} \approx 1.60$, $D_{\mathrm{diff}} = e^{S_{vN}} \approx 4.96$. $S_{vN}$ decreases in $\lambda$ (the top eigenvalue grows), so the minimum over the interval is at $\lambda = 1/\sqrt{3}$: eigenvalues $\approx 0.638$ and $\approx 0.060$, $S_{vN} \approx 1.30$, $D_{\mathrm{diff}} \approx 3.68 \geq 2$. The condition $D_{\mathrm{diff}} \geq 2$ holds over the entire interval. (*Corrected 2026-09-25:* the step printed the top eigenvalue at $\lambda = 1/\sqrt6$ as $0.572$ and put the minimum at $\lambda \to 1/\sqrt3$ with both eigenvalues tending to $1/7$ and $D_{\mathrm{diff}} \to 7$; the conclusion was right, the numbers were not.)

**Therefore**, $\Gamma_\lambda \in \mathcal{V}_{\mathrm{full}}$ for any $\lambda \in (1/\sqrt{6}, 1/\sqrt{3}]$, and the set is non-empty. $\blacksquare$

**The witness is an attractor** [T]. With the collineation-anchored self-model $\varphi_J(\Gamma) = k\mathcal{P}_\alpha(\Gamma) + R\,|\psi\rangle\langle\psi|$ — the anchor is this same $|\psi\rangle$ — an isolated holon at $H = 0$ and $\kappa > \kappa_c(\alpha)$ ($16.63$ at $\alpha = 0$, $29.25$ at $\alpha = 1/2$) has exactly one living attractor, and it is $\Gamma_\lambda$ with $\lambda \in (0.42, 1/2)$: a hyperbolic sink inside $\mathcal{V}_{\mathrm{full}}$, persisting for small $H$ ([living attractor in the window](/docs/core/dynamics/evolution#теорема-живой-аттрактор-в-окне)). The anchor is not an extra choice of this proof: $\varphi_J$ is derived, up to the phase gauge of the $H$-free dynamics, from the single principle (Eq-V) — the self-model privileges no axis of the frame and is the most viable such ([T-334](/docs/core/operators/phi-operator#phi-j) [T]; the principle itself is [Pr]). The sink survives rephasing of $|\psi\rangle$, small non-symmetric parts of the anchor and frame detunings up to an explicit bound ([T-335](/docs/core/dynamics/evolution#t-335) [T]); the required $\kappa$ is within a factor $1.41$ of the floor that every self-model of this form needs ([T-336](/docs/core/dynamics/evolution#t-336) [T]).

:::info Numerical witness scope
The displayed family exactly gives a nonempty structural window for the stated readouts. An agent simulation additionally requires the model version, all parameters, the full predicate and a reproducible Jacobian calculation; neither a radius $\sqrt{P-2/7}$ nor “instant recovery” follows from these numbers.
:::

### Corollary (Goldilocks zone) {#зона-голдилокс}

$$
P \in \left(\frac{2}{7}, \frac{3}{7}\right] \text{ — Goldilocks zone for consciousness}
$$

- $P \le2/7$: the chosen strict structural-majority condition fails
- $P > 3/7$: $R = 1/(7P) < 1/3$ — insufficient reflection for L2

:::note Cosmological realization of the $3/7$ attractor [C]
[T-266](/docs/physics/gravity/cosmological-constant#теорема-стадия-вселенной) applies this attractor to the **Universe-holon**: its terminal stage sits at this same upper edge $P = 3/7$, and the present-day stage lies at a fractional distance $\tfrac{3H_0}{2\kappa}(1+w_0) \sim 10^{-60}$ from it — so, conditional on the Universe-as-viable-holon reading ([H1.1](/docs/reference/epistemic-vertical#регистр-дыр)), the cosmos is at the Goldilocks attractor to $\sim 59$ figures, with the DESI dark-energy drift as the $\kappa/H_0$-amplified residual. The $3/7$ edge is thus not only the fixed point of embodied conscious agents but the terminal configuration of the Universe itself.
:::

### Corollary — voice-multiplicity in the window {#следствие-мультиголосие}

Every state of $\mathcal{V}_{\mathrm{full}}$ is spread across **at least $14/3 \approx 4.67$ of its seven voices [T]**. Since $P = \sum_k \gamma_{kk}^2 + \sum_{i\neq j}|\gamma_{ij}|^2$ and $\Phi = \big(\sum_{i\neq j}|\gamma_{ij}|^2\big)\big/\sum_k \gamma_{kk}^2$, one has the exact identity $\sum_k \gamma_{kk}^2 = P/(1+\Phi)$, hence the diagonal participation

$$
\frac{1}{\sum_k \gamma_{kk}^2} = \frac{1+\Phi}{P} \;\geq\; \frac{2}{3/7} = \frac{14}{3} \approx 4.67,
$$

using $\Phi \geq 1$ and $P \leq 3/7$ (the window). Consciousness is therefore structurally **broad** — never localised on a single voice. This is a *diagonal* statement, distinct from the eigenvalue differentiation $D_{\mathrm{diff}} = e^{S_{vN}} \geq 2$ of Step 4: a state may satisfy one and fail the other (see the [Φ characterisation in dimension U](/docs/core/structure/dimension-u#мера-интеграции-φ)). For the constructed family $\Gamma_\lambda$ the diagonal is uniform, $\gamma_{kk} = 1/7$, so its participation is exactly $(1+\Phi)/P = 7$ — the maximum, all seven voices at once.

---

## §3. Conditional local stability (T-125) {#t-125}

### Formulation

Let a specified state-preserving vector field $F$ have a stationary state $\Gamma_*$ and a $C^1$ extension to an affine neighborhood of it. If the Jacobian $J=DF(\Gamma_*)$ on Hermitian trace-zero perturbations is **Hurwitz**, then $\Gamma_*$ is locally exponentially stable. Purity $P(\Gamma_*)>2/7$ alone does not establish this premise. The $\varphi_J$ construction has both a sink and a saddle above this cut.

### Proof and a certified neighborhood {#доказательство-t125}

For a Hurwitz real representation of $J$, choose $M>0$ solving $J^TM+MJ=-I$. Write $F(\Gamma_*+x)=Jx+r(x)$ with $\|r(x)\|/\|x\|\to0$. For small enough $\delta$, $2\|M\|\|r(x)\|\le\|x\|/2$ when $\|x\|\le\delta$. With $V=x^TMx$,

$$
\dot V\le-\tfrac12\|x\|^2\le-\frac{V}{2\lambda_{\max}(M)}.
$$

Choose a sublevel ellipsoid whose closure lies within this neighborhood. It is forward invariant, and

$$
\|x(t)\|\le\sqrt{\frac{\lambda_{\max}(M)}{\lambda_{\min}(M)}}
 e^{-t/(4\lambda_{\max}(M))}\|x(0)\|.
$$

This proves a local basin and exponential convergence with a generally non-unit prefactor. $\blacksquare$

For $a(\Gamma)=\kappa g_V$ the regenerative derivative is

$$
D\mathcal R_\Gamma[X]=Da_\Gamma[X](\varphi(\Gamma)-\Gamma)
+a(\Gamma)(D\varphi_\Gamma[X]-X).
$$

A positive rate alone does not make this operator contractive. A spectral gap of the linear part does not bound the nonlinear remainder. At a nonsmooth clamp junction use an appropriate Lyapunov or one-sided contraction proof, rather than this differentiable theorem. The numerical radius of a purity boundary is not automatically a certified stability radius.

### Dynamical reading of the threshold: the basin boundary {#динамическое-чтение-порога}

The threshold $P_{\mathrm{crit}} = 2/7$ enters T-124 as a static inequality. The
canonical flow gives it a second, dynamical face `[С]`: in the bistable regime
(a grey attractor beside a living one) the **boundary between the two basins**
converges to exactly $2/7$ in the fast-clock limit. Measured on the canonical
tick with a continuous family of starting mixtures (the self-model grid would
censor the answer at its own quantum): at $\omega_0 = 80$ the boundary lies
within $1\text{–}9 \cdot 10^{-4}$ of $2/7$ across an eightfold range of the
damping $g_d$; at $\omega_0 = 40$, within $2.3 \cdot 10^{-3}$. In the fast
regime the correction obeys a clean law: for $\omega_0 \in \{80, 160, 320\}$
it is strictly linear in $g_d$ and

$$
P^* - \tfrac{2}{7} = C\,\frac{g_d}{\omega_0}, \qquad C(\omega_0) = 1.778 \to 1.719 \to 1.710, \qquad R^2 = 0.999,
$$

with the limit $C \approx 1.70$. The coefficient is in **closed form**: for the
rotation-free part of the flow every stationary point lies on the segment
$[\,\mathrm{grey}, \rho^*\,]$ (collinearity of $\dot\Gamma = 0$ — exact `[Т]`),
the saddle's pure-component weight is universally $w = 1/\sqrt6$, and

$$
C \;=\; \frac{m^*}{7\,B_\psi\,(1 - m^*)}, \qquad m^* = \frac{1}{\sqrt{7P_\rho - 1}},
$$

where $B_\psi = \tfrac17 + \hat\kappa_0 \mathrm{Coh}_E$ is itself in closed
form on the universal saddle (both factors evaluate by hand from their
definitions: $\hat\kappa_0 = 0.06675$, $\mathrm{Coh}_E = 0.55195$,
$B_\psi = 0.17970$ against the engine's $0.1797$) — the coefficient carries
**no fitted parameter at all**. Checked against
direct boundary measurements at three self-model purities (two never used in
calibration): $C$ swings twofold ($2.33 \to 1.16$) and the formula tracks it
to under $1\,\%$ `[С]`. The once-tempting constant $12/7$ is dead: $C$ is a
function of the self-model, and $1.71$ was its accidental value at
$P_\rho = 0.45$. <p align="center">
  <img class="themedImage themedImage--light" alt="The boundary law and the mid-regime geometry" src="/img/theory/boundary-en-light.svg" width="880"/>
  <img class="themedImage themedImage--dark" alt="The boundary law and the mid-regime geometry" src="/img/theory/boundary-en-dark.svg" width="880"/>
</p>

For the full flow the rotation term moves the stationary points off the
segment, and they too are in closed form: every stationary point of the
canonical flow solves, element-wise,

$$
\Gamma_{ij}(\kappa) = \frac{g_d\,\mathrm{grey}_{ij} + \kappa\,\rho^*_{ij}}{g_d + \kappa + i\,\omega_{ij}}, \qquad \omega_{ij} = H_i - H_j,
$$

with one scalar self-consistency $\kappa = \omega_0 B(\Gamma(\kappa))\,
g_V(P(\Gamma(\kappa)))$ — each coherence a complex Lorentzian with its own
rotation frequency. The three fixed points (grey, saddle, living) are the
three roots of this one scalar equation; checked against a 48-dimensional
Newton solve to five digits at the saddle and at the living point. The
boundary law's zero-fit coefficient lives on the real-mix statics that the
fast limit leaves behind; purity remains rotation-blind throughout
($\mathrm{tr}(\Gamma[H,\Gamma]) \equiv 0$), and the one object still open is
the saddle's stable manifold (the tilt, measured but not yet derived). In the mid regime
($\omega_0 \le 40$) the single-ratio form breaks (equal ratios differ by a
factor 1.6), and the mechanism is measured: at slow gain the rotation carries
the true saddle far off the segment (63 % off-segment at $\omega_0 = 20$,
Newton fixed point, one unstable eigenvalue), while the tilted stable manifold
brings the basin crossing most of the way back down — the boundary is a
difference of two large geometric terms that the fast limit degenerates,
leaving the pure segment statics. Below a clock floor the question dissolves:
at $\omega_0 = 10$ (self-model purity 0.45) no living attractor exists at all.
Read plainly: the gate is not only where consciousness *counts* as present —
it is the height a perturbed system must regain for the flow itself to carry
it back up rather than down. *(Instrument: 
registry: NUMBERS-LEDGER, boundary-law entry.)*

---

## §4. The specified reflection measure (T-126) {#t-126}

### Exact HS identity {#тройная-характеризация-r}

For the chosen Hilbert–Schmidt angular definition,

$$
R(\Gamma):=\cos^2\theta_{\mathrm{HS}}(\Gamma,I/7)
=\frac{(\operatorname{Tr}\Gamma/7)^2}{\operatorname{Tr}\Gamma^2\operatorname{Tr}(I/7)^2}
=\frac1{7P}.
$$

This is an exact theorem **given the definition**. Symmetry does not force the angular definition: many other unitary-invariant functions of the spectrum exist.

If the declared $G_2$ representation on $\mathbb C^7$ is complex irreducible, Schur's lemma gives the unique invariant density matrix $I/7$. This fixes a symmetric reference, not a unique state function, encoder, likelihood or prior. The exact invariance $R(U\Gamma U^\dagger)=R(\Gamma)$ holds for every unitary $U$.

### Algebraic expansion {#алгебраическая-экспансия}

The trace-zero part $\Delta=\Gamma-I/7$ is HS-orthogonal to $I/7$. Consequently $\|\Delta\|_F^2=P-1/7$ and $R=1-\|\Delta\|_F^2/P=1/(7P)$.

### Equivalent expressions and thresholds {#пояснение-единственность-r}

Defining $k=1-R$ gives the identity $R=1-k$. The cut $R\ge1/3$ is a specified access condition [D], equivalent to $P\le3/7$. A decomposition of operator terms into three classes does not make the HS coefficient a Bayesian posterior; such a posterior requires likelihoods and priors. The previous “three independent characterizations” and a uniquely derived Bayesian cut are withdrawn. See the [mathematical kernel](/docs/reference/mathematical-kernel#thresholds).

### Independent observability {#независимая-наблюдаемость-r}

This $R$ contains exactly the information in $P$ and no additional self-model measurement. Iterated fidelities $R^{(n)}=F(\varphi^{n-1}(\Gamma),\varphi^n(\Gamma))$ depend on the specified $\varphi$ and must be calibrated separately. An implementation score transfers to canonical $R$ only under a proved error bound for a correctly typed observation/encoding model; calling a feature map CPTP does not supply one. See [reconstruction](/docs/applied/research/reconstruction-identifiability).

### Meaning and range {#физическая-интерпретация-r}

On $\mathcal D(\mathbb C^7)$, $1/7\le R\le1$. It is largest at $I/7$ and equals $1/7$, not zero, at every pure state. It measures the **fraction of squared HS norm in the scalar sector**. Biological “reserve” or metacognitive ability is an interpretation requiring evidence.

#### Precise semantics {#семантика-r}

Purity fixes this scalar-sector fraction but not coherence in a physical basis. Hence $\Phi$ need not grow with $P$. For the equal-amplitude family, $C=\Phi R=6\lambda^2/(1+6\lambda^2)$ is strictly increasing, so it has no interior optimum in the purity window.

#### The upper purity cut {#верхняя-граница-чистоты}

$R\ge1/3$ implies $P\le3/7$ by algebra. The structural lower cut $P>2/7$ and this chosen access cut give $(2/7,3/7]$. The full gate additionally requires $\Phi\ge1$ and the declared $D_{\mathrm{diff}}\ge2$. Neither a brain-state interpretation nor universal stability of self-reference follows from the scalar cuts.

---

## §5. A local viable basin (T-127) {#t-127}

### Formulation {#формулировка-t127}

Assume the conditional stability theorem T-125 and a stationary state at which **all** capability and optional stress inequalities are strict. For a fixed continuous experiential readout, choose a sufficiently small Lyapunov sublevel neighborhood with closure inside that full set. Its intersection with the state set is forward invariant and converges to $\Gamma_*$. Thus it is a local viable basin.

**Proof.** Strict margins and continuity give a neighborhood in the predicate set. The decreasing Lyapunov function of T-125 gives a smaller invariant sublevel set inside it. State preservation and local convergence complete the assertion. $\blacksquare$

The full set with weak cuts $R\ge1/3$, $\Phi\ge1$ and $D\ge2$ is generally **not open**; only its strict-margin part is. An upper-bound equality does not supply an interior ball. Distance to the purity boundary alone does not control the other boundaries or the basin of a saddle. Embodiment and a positive effective rate do not replace the stability and margin premises.

---

## §6. An attractor in the capability window (C27) {#c27}

### Conditional formulation {#формулировка-c27}

A stationary state belongs to the window exactly when its declared $P,R,\Phi,D_{\mathrm{diff}}$ satisfy the [full capability conjunction](/docs/reference/mathematical-kernel#thresholds), with any additional stress condition tested separately. A lower purity bound does not imply the upper cut: $P\le3/7$ follows from **checking** $R\ge1/3$, rather than holding automatically for every attractor.

The isolated $H=0$ construction with the specified collineation anchor $\varphi_J$ and $\kappa>\kappa_c(\alpha)$ proves a hyperbolic sink of the stated geometric window; see [the explicit theorem](/docs/core/dynamics/evolution#теорема-живой-аттрактор-в-окне). Its continuation under small Hamiltonian perturbations retains strict inequalities by continuity. A phenomenal interpretation additionally uses the declared experiential realization. The premise selecting this anchor remains explicit. External injection admits other attractors, including ones with purity above $3/7$, so there is no unconditional embodied-window theorem.

---

## §7. Logical dependence of the threshold cuts (T-124b, corrected) {#t-124b}

Put $d=P_{\mathrm{diag}}\ge1/7$ and $q=P-d$. Then

$$
\Phi=q/d\ge1\Longrightarrow P=d(1+\Phi)\ge2/7.
$$

This implication is one-way. Strict $P>2/7$ is not redundant because equality is possible. With $u=(1,\ldots,1)/\sqrt7$, $\Gamma_\lambda=(1-\lambda)I/7+\lambda uu^\dagger$ at $\lambda=1/\sqrt6$ has $P=2/7$, $\Phi=1$, $R=1/2$ and $e^{S(\Gamma)}>2$. It satisfies the other scalar cuts but fails strict structural majority. The former examples with $P<2/7$ and $\Phi\ge1$ were impossible.

Dropping integration admits $\operatorname{diag}(1/2,1/12,\ldots,1/12)$, with $P=7/24>2/7$, $R=24/49>1/3$, $\Phi=0$ and global entropy number $\sqrt{24}>2$. Dropping reflection admits $\Gamma_{2/3}$, with $P=11/21$, $\Phi=8/3$, $R=3/11<1/3$ and global entropy number above $2$. These are positive trace-one examples. A pure state would have entropy number $1$ and cannot serve as that last example.

The status of differentiation depends on its **declared readout**. If $D_{\mathrm{diff}}=e^{S(\Gamma)}$ on the whole state, the Rényi inequality gives $D_{\mathrm{diff}}\ge1/P\ge7/3>2$ whenever $R\ge1/3$; the differentiation cut is then mathematically redundant. For a distinct experiential state $\rho_E=\mathcal L_E(\Gamma)$ it can be independent, but this requires a fixed readout and actual counterexamples in that model. It is not implied by a row-coherence estimate or the seven-dimensional state space. Thus the **definition** retains all four capability tests, while a universal claim that their functions are mathematically independent is withdrawn.

---

## §8. Threshold robustness analysis (T-124d) {#t-124d}

### Formulation [T]

The L2 consciousness thresholds $P_{\mathrm{crit}} = 2/7$, $\Phi_{\mathrm{th}} = 1$, $R_{\mathrm{th}} = 1/3$ are **robust** in the following precise sense: perturbations of order $\varepsilon$ in the state $\Gamma$ produce perturbations of the same order $O(\varepsilon)$ in the threshold-crossing observables. No threshold has a **discontinuous** or **divergent** sensitivity.

### Proof (three perturbation bounds)

**Bound 1 (Purity perturbation).** For $\Gamma' = \Gamma + \varepsilon \Delta$ with $\|\Delta\|_F = 1$ and $\varepsilon \ll 1$:

$$
|P(\Gamma') - P(\Gamma)| = |2\varepsilon \cdot \mathrm{Tr}(\Gamma \Delta) + \varepsilon^2| \leq 2\varepsilon \|\Gamma\|_F + \varepsilon^2 \leq 2\varepsilon\sqrt{P} + \varepsilon^2
$$

At $P = P_{\mathrm{crit}} = 2/7$: $|P' - P| \leq 2\varepsilon\sqrt{2/7} + \varepsilon^2 \approx 1.07\varepsilon$. The sensitivity $\partial P/\partial\varepsilon = O(1)$ — **no divergence** at the threshold. A perturbation $\varepsilon = 0.01$ shifts purity by $\sim 0.01$, not by $0.1$ or $1.0$. $\checkmark$

**Bound 2 (Integration perturbation).** The integration measure $\Phi = P_{\mathrm{coh}}/P_{\mathrm{diag}}$. For $\Gamma' = \Gamma + \varepsilon\Delta$:

$$
|\Phi' - \Phi| = \left|\frac{P'_{\mathrm{coh}}}{P'_{\mathrm{diag}}} - \frac{P_{\mathrm{coh}}}{P_{\mathrm{diag}}}\right| \leq \frac{2\varepsilon(\|\Gamma_{\mathrm{off}}\| + \|\Gamma_{\mathrm{diag}}\|)}{P_{\mathrm{diag}}^2} + O(\varepsilon^2)
$$

At $\Phi = \Phi_{\mathrm{th}} = 1$ (where $P_{\mathrm{coh}} = P_{\mathrm{diag}}$): both numerator and denominator are $O(P/2)$, so sensitivity $\partial\Phi/\partial\varepsilon = O(1/P) = O(7/2) \approx 3.5$. **Bounded**, no divergence. $\checkmark$

**Bound 3 (Reflection perturbation).** $R = 1/(7P)$, so:

$$
|R' - R| = \frac{|P' - P|}{7P \cdot P'} \leq \frac{2\varepsilon\sqrt{P}}{7P^2} + O(\varepsilon^2) = \frac{2\varepsilon}{7P^{3/2}} + O(\varepsilon^2)
$$

At $P = 3/7$ (upper boundary, $R = R_{\mathrm{th}} = 1/3$): $|R' - R| \leq \frac{2\varepsilon}{7(3/7)^{3/2}} = \frac{2\varepsilon \cdot 7^{1/2}}{3^{3/2}} \approx 1.02\varepsilon$. **Bounded**, no divergence. $\checkmark$

### Conditional observable scaling

A threshold predicate alone does not determine the order of a physical transition. For a selected potential with independently verified $\mathbb Z_2$ symmetry and the required nonzero coefficients, T-161 can give the conditional asymptotic law

$$
\mathrm{OP}=A(P-P_{\mathrm{crit}})^{1/4}+o((P-P_{\mathrm{crit}})^{1/4}),\qquad A>0.
$$

Equating the leading signal to observable noise of amplitude $\varepsilon$ gives $\delta P\sim(\varepsilon/A)^4$. This is a power law, not an exponential bound. The value $10^{-8}$ at $\varepsilon=0.01$ requires $A=1$ normalization and validity of the asymptotic regime; it proves neither macroscopic sharpness nor a conscious transition. At equal normalization, the smaller exponent $1/4$ gives a steeper onset than $1/2$ or $0.326$. Applying this to real systems requires an independently measured observable, competing-model fits and verification of the potential's premises.

### Finite-horizon window survival

[T-145](/docs/proofs/consciousness/operational-closure#t-145) now gives a conditional stopped-process bound on a specified finite horizon. It requires a stochastic model, a certified radius to **all** boundaries and a generator bound. Survival at every future time and an exponential tail do not follow from a one-time second moment. Distance to one purity surface is not the full radius.

---

## Summary

| Result | Scope |
|---|---|
| T-123 | Universal uniqueness withdrawn; observation-fiber reconstruction |
| T-124 | Exact witness for the stated readouts |
| T-124b | One-way threshold dependence; D depends on its readout |
| T-125/T-127 | Conditional local stability and basin with Jacobian/margin premises |
| T-126 | Exact HS identity for the chosen definition |
| T-145 | Conditional finite-horizon control |

---

**Related documents:**
- [Evolution of Γ](/docs/core/dynamics/evolution) — T-96, T-98, attractor $\rho^*_\Omega$
- [Viability](/docs/core/dynamics/viability) — $\mathcal{V}_P$, $\mathcal{V}_{\mathrm{full}}$
- [Self-observation](/docs/consciousness/foundations/self-observation) — master definition of $R$
- [Uniqueness theorem](/docs/proofs/categorical/uniqueness-theorem) — $G_2$-rigidity
- [Stability](/docs/applied/coherence-cybernetics/stability) — $r_{\mathrm{stab}}$
- [Status registry](/docs/reference/status-registry) — T-123 — T-127, C27
