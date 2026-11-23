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

For the four cuts defined in the [kernel](/docs/reference/mathematical-kernel#thresholds), set $\mathcal V_{\mathrm{full}}=\{\Gamma:\mathrm{Cap}_2(\Gamma)\land\forall k\ \sigma_k(\Gamma)<1\}$. The following construction proves non-emptiness with either canonical differentiation readout — the 7D native proxy $D^{7D} = 1 + 6\,\mathrm{Coh}_E(\Gamma)$ ([T-128](/docs/proofs/consciousness/operationalization#t-128) **[D]**, [T-154](/docs/proofs/consciousness/substrate-closure#t-154) **[T]**) or an extended experiential register $\rho_E \in \mathcal{D}(\mathcal{H}_E)$ with $D^{\mathrm{ext}} = \exp S_{vN}(\rho_E)$ — together with the stress proxy $\sigma_k=\mathrm{clamp}(1-7\gamma_{kk},0,1)$. (The full-state global entropy $\exp S_{vN}(\Gamma)$ on $\mathbb{C}^7$ is **not** canonical $D_{\mathrm{diff}}$.) With another experiential lift/readout or stress function, the corresponding inequalities must be checked anew; these choices are not forced by the matrix formalism.

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

**Step 4 ($D_{\mathrm{diff}}$).** We verify both canonical differentiation modes on $\lambda \in (1/\sqrt{6}, 1/\sqrt{3}]$:

- **7D native proxy mode ([T-128](/docs/proofs/consciousness/operationalization#t-128) [D], [T-154](/docs/proofs/consciousness/substrate-closure#t-154) [T]):** Every diagonal entry of $\Gamma_\lambda$ equals $1/7$ and every off-diagonal entry equals $\lambda/7$, so
  $$
  \mathrm{Coh}_E(\Gamma_\lambda) = \frac{\gamma_{EE}^2 + 2\sum_{i\neq E}|\gamma_{Ei}|^2}{P(\Gamma_\lambda)} = \frac{1 + 12\lambda^2}{7(1 + 6\lambda^2)}, \qquad
  D^{7D}(\Gamma_\lambda) = 1 + 6\,\mathrm{Coh}_E(\Gamma_\lambda).
  $$
  Since $\mathrm{Coh}_E(\Gamma_\lambda) = \frac{2}{7} - \frac{1}{7(1+6\lambda^2)}$ increases strictly in $\lambda^2$, over $\lambda \in (1/\sqrt{6}, 1/\sqrt{3}]$ we obtain
  $$
  \mathrm{Coh}_E(\Gamma_\lambda) \in \left(\frac{3}{14},\; \frac{5}{21}\right], \qquad
  D^{7D}(\Gamma_\lambda) \in \left(\frac{16}{7},\; \frac{17}{7}\right] \approx (2.286,\; 2.429],
  $$
  so $D^{7D}(\Gamma_\lambda) > 2$ holds across the entire interval.
- **Extended experiential register mode:** On $\mathbb{C}^7 \otimes \mathcal{H}_E$, pair $\Gamma_\lambda$ as $\rho_{\mathrm{tot}} = \Gamma_\lambda \otimes \rho_E$ with any normalized experiential register state $\rho_E \in \mathcal{D}(\mathcal{H}_E)$ satisfying $S_{vN}(\rho_E) \ge \ln 2$ (for example $\rho_E = I_r/r$ with $r \ge 2$). Then $\operatorname{Tr}_{\mathcal{H}_E}\rho_{\mathrm{tot}} = \Gamma_\lambda$, $\operatorname{Tr}_{\mathbb{C}^7}\rho_{\mathrm{tot}} = \rho_E$, and $D^{\mathrm{ext}} = \exp S_{vN}(\rho_E) \ge 2$.

**Therefore**, $\Gamma_\lambda \in \mathcal{V}_{\mathrm{full}}$ for any $\lambda \in (1/\sqrt{6}, 1/\sqrt{3}]$ in either canonical differentiation mode, and the set is non-empty. $\blacksquare$

**The witness is an attractor** [T]. With the collineation-anchored self-model $\varphi_J(\Gamma) := (1 - R(\Gamma))\,\mathcal{P}_\alpha(\Gamma) + R(\Gamma)\,|\psi\rangle\langle\psi|$ ($k = 1 - R(\Gamma)$, anchored on this same $|\psi\rangle$; contrast the uniform-anchor maps $\varphi_{\mathrm{coh}}(\Gamma) = (1 - R(\Gamma))\,\mathcal{P}_\alpha(\Gamma) + R(\Gamma)\,I/7$ and linear anchor-mixing $\varphi_{\mathrm{lin}}(\Gamma) = R(\Gamma)\,\Gamma + (1 - R(\Gamma))\,I/7$ of [T-249](/docs/proofs/categorical/formalization-phi#дф-производная), whose fixed point $I/7$ is dead) — an isolated holon at $H = 0$ and $\kappa > \kappa_c(\alpha)$ ($16.63$ at $\alpha = 0$, $29.25$ at $\alpha = 1/2$) has exactly one living attractor, and it is $\Gamma_\lambda$ with $\lambda \in (0.42, 1/2)$: a hyperbolic sink inside $\mathcal{V}_{\mathrm{full}}$, persisting for small $H$ ([living attractor in the window](/docs/core/dynamics/evolution#теорема-живой-аттрактор-в-окне)). The anchor is not an extra choice of this proof: $\varphi_J$ is derived, up to the phase gauge of the $H$-free dynamics, from the single principle (Eq-V) — the self-model privileges no axis of the frame and is the most viable such ([T-334](/docs/core/operators/phi-operator#phi-j) [T]; the principle itself is [Pr]). The sink survives rephasing of $|\psi\rangle$, small non-symmetric parts of the anchor and frame detunings up to an explicit bound ([T-335](/docs/core/dynamics/evolution#t-335) [T]); the required $\kappa$ is within a factor $1.41$ of the floor that every self-model of this form needs ([T-336](/docs/core/dynamics/evolution#t-336) [T]).

:::info Numerical witness scope
The displayed family exactly gives a nonempty structural window for the stated readouts. An agent simulation additionally requires the model version, all parameters, the full predicate and a reproducible Jacobian calculation; neither a radius $\sqrt{P-2/7}$ nor “instant recovery” follows from these numbers.
:::

### Corollary (Goldilocks zone) {#зона-голдилокс}

$$
P \in \left(\frac{2}{7}, \frac{3}{7}\right] \text{ — Goldilocks zone for consciousness}
$$

- $P \le2/7$: the chosen strict structural-majority condition fails
- $P > 3/7$: $R = 1/(7P) < 1/3$ — insufficient reflection for L2

### Corollary — voice-multiplicity in the window {#следствие-мультиголосие}

Every state of $\mathcal{V}_{\mathrm{full}}$ is spread across **at least $14/3 \approx 4.67$ of its seven voices [T]**. Since $P = \sum_k \gamma_{kk}^2 + \sum_{i\neq j}|\gamma_{ij}|^2$ and $\Phi = \big(\sum_{i\neq j}|\gamma_{ij}|^2\big)\big/\sum_k \gamma_{kk}^2$, one has the exact identity $\sum_k \gamma_{kk}^2 = P/(1+\Phi)$, hence the diagonal participation

$$
\frac{1}{\sum_k \gamma_{kk}^2} = \frac{1+\Phi}{P} \;\geq\; \frac{2}{3/7} = \frac{14}{3} \approx 4.67,
$$

using $\Phi \geq 1$ and $P \leq 3/7$ (the window). Consciousness is therefore structurally **broad** — never localised on a single voice. This is a *diagonal* statement, distinct from the differentiation criterion $D_{\mathrm{diff}} \geq 2$ of Step 4 (whether evaluated via the 7D native proxy $D^{7D} = 1 + 6\,\mathrm{Coh}_E(\Gamma)$ or the extended-register entropy $D^{\mathrm{ext}} = \exp S_{vN}(\rho_E)$): a state may satisfy one and fail the other (see the [Φ characterisation in dimension U](/docs/core/structure/dimension-u#мера-интеграции-φ)). For the constructed family $\Gamma_\lambda$ the diagonal is uniform, $\gamma_{kk} = 1/7$, so its participation is exactly $(1+\Phi)/P = 7$ — the maximum, all seven voices at once.

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

### Toy-model illustration: basin boundary in a depolarizing flow {#динамическое-чтение-порога}

:::info Scope: depolarizing toy model [D]
The following calculation analyses a **simplified depolarizing toy model** with a **fixed** target state $\rho^*$ and isotropic depolarization toward $\mathrm{grey} := I/7$. It is distinct from the canonical Fano-dephasing flow $\mathcal{D}_\Omega$ and from the state-dependent self-models $\varphi_{\mathrm{coh}}$ and $\varphi_J$ (whose stationary solutions are treated separately in [T-335](/docs/core/dynamics/evolution#t-335)).
:::

Consider the fixed-target depolarizing flow on $\mathcal{D}(\mathbb{C}^7)$:

$$
\dot\Gamma = -i[H, \Gamma] + g_d\,(\mathrm{grey} - \Gamma) + \kappa(\Gamma)\,(\rho^* - \Gamma), \qquad \mathrm{grey} := I/7,
$$

where $g_d > 0$ is a constant isotropic depolarization rate, $\rho^* \in \mathcal{D}(\mathbb{C}^7)$ is a **fixed** target state of purity $P_\rho := P(\rho^*) > 2/7$, and $\kappa(\Gamma) = \omega_0 B(\Gamma)\,g_V(P(\Gamma)) \ge 0$ is a state-dependent regeneration rate with clock scale $\omega_0 > 0$, positive factor $B(\Gamma)$, and a viability gate $g_V(P)$ vanishing for $P \le 2/7$ and increasing linearly with slope $g_V'(2/7^+) = 7$ just above $2/7$.

Three exact algebraic facts hold **within this depolarizing toy model [T for this toy model]**:

1. **Collinearity at $H = 0$.** Every stationary point satisfies $(g_d + \kappa)\Gamma = g_d\,\mathrm{grey} + \kappa\,\rho^*$, hence lies on the convex segment $[\mathrm{grey}, \rho^*]$:
   $$
   \Gamma(m) = (1 - m)\,\mathrm{grey} + m\,\rho^*, \qquad m = \frac{\kappa}{g_d + \kappa} \in [0, 1], \qquad P(m) = \frac{1}{7} + m^2\!\left(P_\rho - \frac{1}{7}\right).
   $$
   The purity threshold $P = 2/7$ sits on this segment at $m^* = (7P_\rho - 1)^{-1/2}$. When $\rho^* = (1-\lambda)\,\mathrm{grey} + \lambda|\psi\rangle\langle\psi|$ has purity $P_\rho = (1+6\lambda^2)/7$, the pure-state weight at $P = 2/7$ is $w = m^*\lambda = 1/\sqrt{6}$.
2. **Closed-form stationary equation for diagonal $H$.** For $H = \operatorname{diag}(H_0,\ldots,H_6)$ with $\omega_{ij} = H_i - H_j$, every stationary point solves element-wise
   $$
   \Gamma_{ij}(\kappa) = \frac{g_d\,\mathrm{grey}_{ij} + \kappa\,\rho^*_{ij}}{g_d + \kappa + i\omega_{ij}},
   $$
   coupled to the single scalar self-consistency condition $\kappa = \omega_0 B(\Gamma(\kappa))\,g_V(P(\Gamma(\kappa)))$. In the bistable parameter regime this scalar equation has three roots: the trivial attractor $\mathrm{grey} = I/7$ ($\kappa = 0$), an intermediate saddle, and a living attractor.
3. **Fast-clock saddle asymptotics at $H = 0$.** Writing $B_\psi := B(\Gamma(m^*)) > 0$ and expanding the saddle condition $g_d m/(1-m) = \omega_0 B(\Gamma(m))\,g_V(P(m))$ around $m = m^*$ as $g_d/\omega_0 \to 0$ gives the first-order saddle purity shift
   $$
   P^* - \frac{2}{7} = C\,\frac{g_d}{\omega_0} + O\!\left((g_d/\omega_0)^2\right), \qquad
   C = \frac{m^*}{7\,B_\psi\,(1 - m^*)}, \qquad
   m^* = \frac{1}{\sqrt{7P_\rho - 1}}.
   $$

Thus, in the $H = 0$, $g_d/\omega_0 \to 0$ limit of this toy model, the saddle separating the basin of $\mathrm{grey} = I/7$ from the living attractor approaches $P = 2/7$ with a target-dependent coefficient $C$ (not a universal constant). For $H \neq 0$, unitary rotation moves the saddle off the segment $[\mathrm{grey}, \rho^*]$ and tilts its stable manifold; determining the resulting separatrix requires a direct numerical calculation for the specific declared parameters and does not yield a universal dynamical law for arbitrary UHM flows.

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

Defining $k=1-R$ gives the identity $R=1-k$. Note that $R$ and $k = 1 - R$ enter with **opposite** roles in the two main self-model families: in linear anchor-mixing $\varphi_{\mathrm{lin}}(\Gamma) := R(\Gamma)\,\Gamma + (1 - R(\Gamma))\,I/7$ ([T-249](/docs/proofs/categorical/formalization-phi#дф-производная) **[T]**), $R$ weights $\Gamma$ and $k = 1-R$ weights $I/7$; whereas in the coherent dephasing-anchor map $\varphi_{\mathrm{coh}}(\Gamma) := (1 - R(\Gamma))\,\mathcal{P}_\alpha(\Gamma) + R(\Gamma)\,I/7$ and collineation-anchored map $\varphi_J(\Gamma) := (1 - R(\Gamma))\,\mathcal{P}_\alpha(\Gamma) + R(\Gamma)\,|\psi\rangle\langle\psi|$ ([T-334](/docs/core/operators/phi-operator#phi-j) **[T]**), $k = 1-R$ weights $\mathcal{P}_\alpha(\Gamma)$ and $R$ weights the anchor. The cut $R\ge1/3$ is a specified access condition [D], equivalent to $P\le3/7$. A decomposition of operator terms into three classes does not make the HS coefficient a Bayesian posterior; such a posterior requires likelihoods and priors. The previous “three independent characterizations” and a uniquely derived Bayesian cut are withdrawn. See the [mathematical kernel](/docs/reference/mathematical-kernel#thresholds).

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

Put $d=P_{\mathrm{diag}}\ge1/7$ and $q=P-d$. By [T-129a](/docs/proofs/consciousness/operationalization#t-129a-универсальность) **[T]**,

$$
\Phi=q/d\ge1\Longrightarrow P=d(1+\Phi)\ge2/7.
$$

This implication is one-way. Strict $P>2/7$ is not redundant because equality is possible: with $u=(1,\ldots,1)/\sqrt7$, $\Gamma_\lambda=(1-\lambda)I/7+\lambda uu^\dagger$ at $\lambda=1/\sqrt6$ has $P=2/7$, $\Phi=1$, $R=1/2$, and $D^{7D} = 16/7 > 2$ (and in extension mode, any register state $\rho_E$ with $\exp S_{vN}(\rho_E) \ge 2$). It satisfies the other cuts but fails strict structural majority. The former examples with $P<2/7$ and $\Phi\ge1$ were impossible.

Dropping integration admits $\operatorname{diag}(1/2,1/12,\ldots,1/12)$ with axis $E$ assigned the $1/2$ entry: $P=7/24>2/7$, $R=24/49>1/3$, $\Phi=0$, and $D^{7D} = 1 + 6\cdot\frac{6}{7} = 43/7 > 2$ (or any $\rho_E$ with $\exp S_{vN}(\rho_E)\ge 2$ in extension mode). Dropping reflection admits $\Gamma_{2/3}$, with $P=11/21$, $\Phi=8/3\ge 1$, $R=3/11<1/3$, and $D^{7D} = 191/77 \approx 2.48 > 2$ (or any $\rho_E$ with $\exp S_{vN}(\rho_E)\ge 2$ in extension mode).

The differentiation cut $D_{\mathrm{diff}} \ge 2$ is also independently necessary in **both** canonical modes:
- **7D native proxy mode ($D^{7D} = 1 + 6\,\mathrm{Coh}_E(\Gamma)$):** placing $\Gamma_{\mathrm{no}\text{-}E} := \frac{1}{2}\frac{I_6}{6} + \frac{1}{2}|u_6\rangle\langle u_6|$ on the six non-$E$ axes ($|u_6\rangle = \frac{1}{\sqrt 6}\sum_{k\neq E}|k\rangle$, $\gamma_{EE}=0$) gives $P = 3/8 \in (2/7, 3/7]$, $R = 8/21 > 1/3$, $\Phi = 5/4 > 1$, and $\mathrm{Coh}_E = 0$, $D^{7D} = 1 < 2$. Mixing $0.99\,\Gamma_{\mathrm{no}\text{-}E} + 0.01\,|E\rangle\langle E|$ even preserves $A_1$ ($\mathrm{Coh}_E > 0$) along with $P \approx 0.368 \in (2/7, 3/7]$, $R \approx 0.389 > 1/3$, and $\Phi \approx 1.25 > 1$, while keeping $D^{7D} \approx 1.002 < 2$.
- **Extended experiential register mode ($D^{\mathrm{ext}} = \exp S_{vN}(\rho_E)$):** pairing any window witness $\Gamma_\lambda$ ($\lambda \in (1/\sqrt{6}, 1/\sqrt{3}]$) as $\Gamma_\lambda \otimes \rho_E$ with a low-entropy rank-2 register state $\rho_E = \operatorname{diag}(0.99, 0.01)$ satisfies $A_1$ ($\operatorname{rank}\rho_E > 1$) and $P, R, \Phi$ while giving $D^{\mathrm{ext}} \approx 1.058 < 2$.

*(Remark on non-canonical full-state entropy:)* Evaluating $\exp S_{vN}(\Gamma)$ on the full $7\times 7$ matrix $\Gamma$ is **not** canonical $D_{\mathrm{diff}}$; moreover, the Rényi inequality $\exp S_{vN}(\Gamma) \ge 1/P = 7R \ge 7/3 > 2$ would make such a full-state cut redundant whenever $R \ge 1/3$. Thus the definition retains all four capability tests under the declared canonical differentiation readout.

---

## §8. Threshold robustness analysis (T-124d) {#t-124d}

### Formulation [T]

The L2 consciousness thresholds $P_{\mathrm{crit}} = 2/7$, $\Phi_{\mathrm{th}} = 1$, $R_{\mathrm{th}} = 1/3$ are **robust** in the following precise sense: perturbations of order $\varepsilon$ in the state $\Gamma$ produce perturbations of the same order $O(\varepsilon)$ in the threshold-crossing observables. No threshold has a **discontinuous** or **divergent** sensitivity.

### Proof (three perturbation bounds)

Let $\Gamma' = \Gamma + \varepsilon \Delta \in \mathcal{D}(\mathbb{C}^7)$ with Hermitian traceless perturbation $\Delta$ ($\operatorname{Tr}\Delta = 0$, $\|\Delta\|_F = 1$) and $\varepsilon \ll 1$.

**Bound 1 (Purity perturbation).**

$$
|P(\Gamma') - P(\Gamma)| = |2\varepsilon \cdot \mathrm{Tr}(\Gamma \Delta) + \varepsilon^2| \leq 2\varepsilon \|\Gamma\|_F + \varepsilon^2 \leq 2\varepsilon\sqrt{P} + \varepsilon^2
$$

At $P = P_{\mathrm{crit}} = 2/7$: $|P' - P| \leq 2\varepsilon\sqrt{2/7} + \varepsilon^2 \approx 1.07\varepsilon$. The sensitivity $\partial P/\partial\varepsilon = O(1)$ — **no divergence** at the threshold. A perturbation $\varepsilon = 0.01$ shifts purity by $\sim 0.01$, not by $0.1$ or $1.0$. $\checkmark$

**Bound 2 (Integration perturbation).** Write $\Phi = P_{\mathrm{coh}}/P_{\mathrm{diag}}$ with orthogonal decomposition $\Gamma = \Gamma_{\mathrm{diag}} + \Gamma_{\mathrm{off}}$ and $\Delta = \Delta_{\mathrm{diag}} + \Delta_{\mathrm{off}}$ ($\|\Delta_{\mathrm{diag}}\|_F^2 + \|\Delta_{\mathrm{off}}\|_F^2 = 1$). Since $\operatorname{Tr}(\Delta_{\mathrm{diag}}) = \operatorname{Tr}\Delta = 0$, we have $\langle \Gamma_{\mathrm{diag}}, \Delta_{\mathrm{diag}}\rangle_F = \langle \Gamma_{\mathrm{diag}} - I/7, \Delta_{\mathrm{diag}}\rangle_F$ and $\|\Gamma_{\mathrm{diag}} - I/7\|_F^2 = P_{\mathrm{diag}} - 1/7$. Differentiating the quotient at $\varepsilon = 0$ gives

$$
\Phi' - \Phi = \frac{2\varepsilon}{P_{\mathrm{diag}}}\bigl(\langle \Gamma_{\mathrm{off}}, \Delta_{\mathrm{off}}\rangle_F - \Phi\,\langle \Gamma_{\mathrm{diag}} - I/7, \Delta_{\mathrm{diag}}\rangle_F\bigr) + O(\varepsilon^2).
$$

By Cauchy–Schwarz on the orthogonal components $(\Delta_{\mathrm{off}}, \Delta_{\mathrm{diag}})$, the exact tangent-space sensitivity bound is

$$
|\Phi' - \Phi| \leq \frac{2\varepsilon}{P_{\mathrm{diag}}}\sqrt{P_{\mathrm{coh}} + \Phi^2\!\left(P_{\mathrm{diag}} - \frac{1}{7}\right)} + O(\varepsilon^2).
$$

On the $\Phi = \Phi_{\mathrm{th}} = 1$ threshold surface ($P_{\mathrm{coh}} = P_{\mathrm{diag}} = P/2$, with $P \ge 2/7$ by [T-129a](/docs/proofs/consciousness/operationalization#t-129a-универсальность)), this simplifies to

$$
|\Phi' - \Phi| \leq \frac{4\varepsilon}{P}\sqrt{P - \frac{1}{7}} + O(\varepsilon^2).
$$

Since $\frac{4}{P}\sqrt{P - 1/7}$ is strictly decreasing for $P \ge 2/7$, it attains its **sharp maximum** on the $\Phi = 1$ boundary at $P = P_{\mathrm{crit}} = 2/7$, where $\Gamma_{\mathrm{diag}} = I/7$ forces the diagonal perturbation term to vanish identically:

$$
|\Phi' - \Phi| \leq \frac{2\varepsilon\sqrt{P_{\mathrm{coh}}}}{P_{\mathrm{diag}}} + O(\varepsilon^2) = \frac{2\sqrt{2}\,\varepsilon}{\sqrt{P}} + O(\varepsilon^2) = 2\sqrt{7}\,\varepsilon + O(\varepsilon^2) \approx 5.29\,\varepsilon \qquad (\text{at } P = 2/7,\ \Phi = 1),
$$

attained along $\Delta = \Gamma_{\mathrm{off}}/\|\Gamma_{\mathrm{off}}\|_F$. **Bounded**, $O(\varepsilon)$, no divergence. $\checkmark$

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
- [Uniqueness theorem](/docs/proofs/categorical/uniqueness-theorem) — conditional representation comparison under (RI) and observation-fiber identifiability
- [Stability](/docs/applied/coherence-cybernetics/stability) — $r_{\mathrm{stab}}$
- [Status registry](/docs/reference/status-registry) — T-123 — T-127, C27
