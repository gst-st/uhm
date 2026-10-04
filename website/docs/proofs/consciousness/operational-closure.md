---
sidebar_position: 4
title: "Operational closure"
description: "Conditional reconstruction, feedback, finite-horizon stability and operational feature models"
---

# Operational closure

This page distinguishes model definitions [D], their exact mathematical consequences [T under stated premises] and empirical/phenomenal bridges [H/I]. A numerical construction is not evidence for a universal ontological identification. Thresholds use the [mathematical kernel](/docs/reference/mathematical-kernel#thresholds).

## §1. T-139: a specified Γ-backbone update {#t-139}

For a CPTP propagator $\mathcal E_h$, state-valued encoder $\pi$ and $\alpha\in[0,1]$, define

$$
\Gamma'=\alpha\mathcal E_h(\Gamma)+(1-\alpha)\pi(\mathcal B(x)).
$$

The result is positive with trace one by convexity. For fixed external $x$, target and state-independent $\alpha$, its operator-linear extension is a convex combination of $\mathcal E_h$ and a replacement channel, hence CPTP. With coefficients or input records selected from $\Gamma$, the update is generally nonlinear and only state preservation follows.

The update is a choice [D]; neither it nor the encoder is unique up to $G_2$. The withdrawn T-123 argument is replaced by [observation-fiber identifiability](/docs/applied/research/reconstruction-identifiability). A nonlinear map $\mathbb R^D\to\mathcal D_7$ is not a CPTP channel without a separate operator-algebra encoding. Equal backbone snapshots need not give equal $\Gamma$ when histories or initial states differ. Identification of $\Gamma$ with experience remains the stated ontological bridge.

## §2. T-140: full capability gate and summary score {#t-140}

The definition is

$$
\mathrm{Cap}_2=(P>2/7)\land(R\ge1/3)\land(\Phi\ge1)\land(D_{\mathrm{diff}}\ge2).
$$

An optional full viable-domain predicate also tests the declared stress bounds. Each empirical verdict requires identified quantities or a confidence set on which the predicate is constant.

Retain $C:=\Phi R$ as a dimensionless summary score [D]. The scalar cuts imply $C\ge1/3$, but the converse fails. For example, an equal-amplitude mixed state with $P=4/7$ has $\Phi=3$, $R=1/4$, $C=3/4$ and fails reflection. Thus $C$ cannot certify the conjunction, even with a differentiation bound.

$C=0$ is equivalent to $\Phi=0$ because $R\ge1/7>0$; it is not equivalent to failure of either access threshold. Dimensional neutrality and monotonicity do not select the exponents in $\Phi^aR^b$: every $a,b>0$ is dimensionless and has the threshold product $1^a(1/3)^b$. The claimed unique product choice is withdrawn. Differentiation and all other conjuncts remain separately tested.

## §3. T-141: comparison of specified self-models {#t-141}

Let $D$ be diagonalization in a fixed physical frame, $\mathcal P=(1/3)\mathrm{id}+(2/3)D$, and fix a mixing value $k\in[0,1]$. The two maps

$$
\varphi_B(\Gamma)=kD(\Gamma)+(1-k)I/7,\qquad
\varphi_C(\Gamma)=k\mathcal P(\Gamma)+(1-k)I/7
$$

are generally different. Their exact difference is

$$
\varphi_B(\Gamma)-\varphi_C(\Gamma)=-\tfrac k3\Gamma_{\mathrm{off}}.
$$

With state-dependent $k$ this identity still holds pointwise, while the overall maps are generally nonlinear. A third map $(1-k)\Gamma+k\rho_a$ with a different anchor is not equivalent to them merely because it is a convex interpolation.

### Off-diagonal HS bound {#лемма-фробениус-off-diag}

Orthogonality of diagonal and off-diagonal parts gives

$$
\|\Gamma_{\mathrm{off}}\|_F^2=P-\sum_i\gamma_{ii}^2\le P-1/7,
$$

hence $\|\varphi_B-\varphi_C\|_F\le(k/3)\sqrt{P-1/7}$. This controls a Lipschitz observable only after specifying that observable and its Lipschitz constant. Canonical $R(\Gamma)=1/(7P)$ does not depend on which map is named; an output score $R(\varphi_B(\Gamma))$ is a different quantity. The former assertion that all three maps equal a nontrivial dynamical attractor is withdrawn: the unital maps have fixed point $I/7$ in the stated contracting case.

## §4. T-142: Fano attenuation and a declared depth score {#t-142}

For the bare Fano channel, when the initial off-diagonal norm is nonzero,

$$
S_n:=\frac{\|\operatorname{offdiag}(\mathcal P^n\Gamma)\|_F}{\|\operatorname{offdiag}\Gamma\|_F}=3^{-n}.
$$

For the specified canonical map $M(\rho)=(1-R(\rho))\mathcal P(\rho)+R(\rho)I/7$,

$$
S_n=3^{-n}\prod_{j<n}(1-R(\rho_j))\le(2/7)^n.
$$

These are attenuation identities, not fidelity or a consciousness-depth theorem. A detector $S_n\ge\varepsilon$ has a finite depth depending on $\varepsilon$; for bare Fano it is $n\le\lfloor\log(1/\varepsilon)/\log3\rfloor$.

### Arithmetic of the historical score {#лемма-контракция-sad}

If one **stipulates** $s_{n-1}=(P/(2/7))3^{-(n-1)}$ and a gate $s_{n-1}>1/(n+1)$, its cuts are

$$
P>p_n:=\frac27\frac{3^{n-1}}{n+1},\qquad
p_1=1/7,\quad p_2=2/7,\quad p_3=9/14,\quad p_4=54/35.
$$

Since $P\le1$, this chosen score admits at most level three. Inside $P\le3/7$ it admits at most level two. The score can exceed one and is not a normalized survival probability or the reflection measure. The former universal $\mathrm{SAD}_{\max}=3$ and inference from attenuation to inter-iterate fidelity are withdrawn. See the [revised depth tower](/docs/consciousness/hierarchy/depth-tower#критическая-чистота-sad) for independently certified meta-observation levels.

## §5. T-143: threshold transfer requires a margin {#t-143}

Suppose the **same defined observable** $q_j$ and cut $t_j$ are used at each of finitely many levels, with certified errors $|\widehat q_j-q_j|\le\epsilon_j$. If $|q_j-t_j|>\epsilon_j$ for every tested level, all threshold verdicts agree, and a longest-prefix depth agrees exactly.

**Proof.** An error smaller than the distance to the cut cannot change the sign of $q_j-t_j$. Apply this to each level. $\blacksquare$

Without a margin, arbitrarily small error can cross a cut; spacing between cuts at **different** levels supplies no margin for any individual observable. Comparing a feature-space residual with state-space fidelity additionally requires a proved observation bridge. A diamond norm is applicable to linear channels on specified operator algebras, not to an arbitrary feature encoder. The former universal depth error “at most one” is withdrawn.

## §6. T-144: evaluating and optimizing a specified action model {#t-144}

For a finite action set $A$ of size $K$, evaluating a declared cost $J(a)$ for each action finds a minimizer with exactly $K$ evaluations; if each evaluation has error at most $\eta$, the selected action has cost at most $\min J+2\eta$. The total computation is $K$ times the cost of simulation and readout, not automatically $O(KN^2)$.

For a convex cost on a closed convex action set of diameter $D_A$, with subgradient norms at most $L$ and computable projections, projected subgradient descent with the standard step size gives an averaged iterate with suboptimality at most $LD_A/\sqrt k$. Thus $k\ge(LD_A/\varepsilon)^2$ suffices **under these convexity assumptions**. General nonlinear trajectory costs and clamped maximum stress need not be convex. Lipschitz continuity and compactness alone do not imply efficient global optimization or exclude NP-hard instances.

## §7. T-145: finite-horizon stochastic viability {#t-145}

:::warning Original T-145 withdrawn
A one-time second-moment bound implies neither an exponential tail nor survival for every future time. Independent rare exits with probability $p>0$ at each tick have survival $(1-p)^n\to0$, even when their one-time variance is small. Distance to only the purity surface is not a radius to the full predicate boundary.
:::

**Conditional theorem.** Specify a continuous, adapted, state-preserving Itô process, its drift $F$ and diffusion columns $G_j$, and a stationary reference $\Gamma_*$. Let $V=\|\Gamma-\Gamma_*\|_F^2$ and choose $r>0$ so that the state ball $V<r^2$ lies inside **all** declared capability/stress conditions. Define $\tau_r=\inf\{t\ge0:V(\Gamma_t)\ge r^2\}$. Suppose the process is well posed and, before exit,

$$
\mathscr L V=2\operatorname{Tr}(\Gamma-\Gamma_*)F(\Gamma)
+\sum_j\|G_j(\Gamma)\|_F^2\le\nu^2.
$$

Then for each specified finite $T$ and $V(\Gamma_0)<r^2$,

$$
\mathbb P(\tau_r\le T)\le
\min\!\left(1,\frac{V(\Gamma_0)+\nu^2T}{r^2}\right).
$$

**Proof.** The stopped Itô formula, localization and the stated moment bounds give $\mathbb E V(\Gamma_{T\wedge\tau_r})\le V(\Gamma_0)+\nu^2T$. Continuity gives $V(\Gamma_{\tau_r})=r^2$ on exit, so the left expectation is at least $r^2\mathbb P(\tau_r\le T)$. $\blacksquare$

A stronger premise $\mathscr LV\le-2cV+\nu^2$ implies the displayed generator bound, and can supply one-time moment control while the inequality holds. It still does not give an infinite-time no-exit probability. Exponential finite-horizon estimates require an **additional verified exponential supermartingale**: if $W=e^{\theta V}$ and $\mathscr LW\le\lambda W$ in the ball, with $\theta>0$, $\lambda\ge0$ and valid stopping/integrability hypotheses, then

$$
\mathbb P(\tau_r\le T)\le
\min(1,\exp(\theta(V(\Gamma_0)-r^2)+\lambda T)).
$$

This follows by stopping $e^{-\lambda t}W(\Gamma_t)$. The generator condition includes the quadratic-variation term and must be checked for the specified diffusion. It does not follow from small $\mathbb E\|h\|^2$. Additive matrix white noise is not automatically state-preserving; the physical stochastic realization and boundary behavior must be supplied.

For a single perturbation $Z$ with $\mathbb E\|Z\|^2\le\sigma^2$, the valid universal conclusion is only $\mathbb P(\|Z\|\ge r)\le\sigma^2/r^2$. Simulations and confidence statements must report the horizon, process law and full margin.

## §8. T-146: structural grouping and phenomenal interpretation {#t-146}

Given the named partition $\{A,S,D\}$, $\{L,E\}$, $\{O,U\}$, the 21 unordered pairs divide into three structural, one cognitive, one reflexive and sixteen cross-sector pairs. This is an exact combinatorial grouping **given the labels**. The labels are functional assignments [D/I], not a theorem that seven biological roles are uniquely forced by axioms. The phenomenal interpretation of a pair, such as assigning “affect” to $DE$, is a hypothesis requiring observations.

An individual complex coherence is not invariant under general $G_2$ conjugation. Its phase and magnitude are frame-dependent, and persistent coherences may be driven by structured inputs or correlated noise. Primitivity alone does not distinguish phenomenal structure from noise. Neither codomain symmetry nor this grouping fixes an encoder or experiential correspondence.

## §9. T-147: a 30-component feature model {#t-147}

Define, for a specified sufficiently smooth dynamics and stress/coherence readouts,

$$
\mathbf e(\Gamma)=\left(\dot\gamma_{kk},\ddot\gamma_{kk},\sigma_k,
\dot P_{\mathrm{coh}}^{(k)},\dot P,\dot\Phi\right)\in\mathbb R^{30}.
$$

This is a proposed descriptive feature vector [D/H], not a complete theorem of emotion. Normalization gives **two** constant output constraints,

$$
\sum_k\dot\gamma_{kk}=0,\qquad \sum_k\ddot\gamma_{kk}=0.
$$

Thus its Jacobian has rank at most $28$ wherever it exists. Generic equality needs an actual specified model and a rank calculation; additional dependencies or clamp singularities may lower it. The previous rank $29$ and identity $\dot P=\sum_k\dot\gamma_{kk}$ are false: $\dot P=2\operatorname{Tr}\Gamma\dot\Gamma$, and dephasing changes it even with all populations stationary. A scalar purity derivative is a possible summary; neither it nor this vector alone certifies full viability or phenomenal completeness.

### Rank scope {#ранговый-анализ-30d}

The bounds concern a deterministic feature map under declared dynamics. Estimating accelerations and complex-coherence changes from noisy recordings requires independent temporal resolution, uncertainty and identifiability checks. No universal $O(N^2)$ evaluation cost follows for arbitrary generators or readouts.

## §10. Conditional checking of C20 {#c20-конструктивизация}

For a found stationary state in the isotropic Fano model, compute $a=\kappa g_V$, $f^*=\operatorname{Tr}\Gamma_*\varphi(\Gamma_*)$ and $P_{\mathrm{diag}}$. Without extra inputs, the exact balance is

$$
P_*=(\alpha_D P_{\mathrm{diag}}+af^*)/(\alpha_D+a),\qquad\alpha_D=2/3.
$$

This can test the lower purity cut. An additional input contributes its actual purity flux, as in [T-98a](/docs/core/dynamics/evolution#следствие-t98a). Numerical integration from one initial state does not prove a unique global attractor; report residuals, the Jacobian, the basin tested and all capability conjuncts. Embodiment alone does not close C20, and isolated alternative self-models can have living attractors.

## §11. Result scope

The exact results are convex state validity, specified-channel attenuation, observable margin transfer, conditional optimization bounds and stopped-process survival bounds. Encoders, feature semantics, action costs, threshold schedules and experiential readouts remain explicit model inputs. The full capability conjunction is the operational target; support for a frozen model on held-out data is distinct from its ontological interpretation.
