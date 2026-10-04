---
sidebar_position: 2.5
title: Reconstruction and Identifiability of Γ
description: Observation models, informational completeness, uncertainty and the limits of empirical reconstruction
---

# Reconstruction and Identifiability of Γ

:::info Scope and correction (2026-10-03)
This page supplies the inverse-problem foundation of the [measurement protocol](/docs/applied/research/measurement-protocol) and [experimental protocol](/docs/applied/research/experimental-protocol). It replaces the withdrawn inference “rigidity of the state space implies uniqueness of a neural encoder”. Theorems below are statements about a **specified observation model**. The correspondence of biological or AI measurements with that model remains an empirical hypothesis [H].
:::

## 1. Four different maps {#observation-model}

Let $\mathsf D_7=\{\Gamma=\Gamma^\dagger\succeq0:\operatorname{Tr}\Gamma=1\}$. Distinguish:

1. An **observation model** $\mathsf O_\theta:\mathsf D_7\to\prod_{a\in\mathsf A}\mathcal P(\mathsf Y_a)$, assigning a probability law to observations for every predeclared measurement or intervention setting $a$. Calibration parameters $\theta$ and the functional frame are fixed before confirmation.
2. A **statistic map** $F_\theta:\mathsf D_7\to\mathbb R^m$, e.g. the means of the measured features. Equality of these statistics implies equality of observation laws only if the model says so, as in a Gaussian location model with known fixed covariance.
3. An **estimator** $\hat\pi_\theta:y\mapsto\hat\Gamma$, or a set-valued reconstruction $y\mapsto\mathcal C(y)\subseteq\mathsf D_7$, using finite noisy data. It need not be linear or invertible.
4. A **physical channel** $\mathcal E:\mathcal B(\mathcal H)\to\mathcal B(\mathbb C^7)$, which must be linear, completely positive and trace-preserving if it is claimed to be CPTP.

Softmax, normalized Cholesky and likelihood optimization produce valid states; this does not make their composite a CPTP channel. A preparation rule can separately define a classical-to-quantum channel $p\mapsto\sum_xp_x\hat\pi_\theta(x)$ on a specified classical input algebra. That channel does not prove that the estimator recovers the system's ontological state. See [Watrous, Chapter 2, Definition 2.13](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf).

If $\theta$ is unknown, identifiability must be checked for the **joint** model $(\Gamma,\theta)\mapsto\mathsf O_\theta(\Gamma)$. Free calibration and a free latent state generally admit compensating changes; fixing a fitted $\theta$ is a protocol choice, not a proof that the latent interpretation is unique.

## 2. The strongest general uniqueness statement {#fiber-theorem}

Define observational equivalence by

$$
\Gamma\sim_\theta\Sigma\quad\Longleftrightarrow\quad
\mathsf O_\theta(\Gamma)=\mathsf O_\theta(\Sigma)
\quad\text{for every }a\in\mathsf A.
$$

:::info Theorem ID-1 (identification by observation fibers) [T]
For a fixed observation model, exact population data identify precisely the equivalence class $[\Gamma]_\theta$. The whole state is identifiable on an admissible set $\mathsf S\subseteq\mathsf D_7$ iff $\mathsf O_\theta|_{\mathsf S}$ is injective. A target quantity $q$ is identifiable iff it is constant on every observation fiber in $\mathsf S$.

**Proof.** Equal laws give the same distribution of every experiment permitted by the design, so they cannot distinguish the two states. Conversely, different laws distinguish states at the population level by definition. A quantity descends to $\mathsf O_\theta(\mathsf S)$ exactly when it has the same value on each fiber. $\square$
:::

This is statistical identification, distinct from precision or finite-sample success. The classical distinction is developed by [Rothenberg, *Identification in Parametric Models* (1971)](https://doi.org/10.2307/1913267).

### Why encoder rigidity does not follow

The former proof formed $\pi_2\circ\pi_1^{-1}$ from continuous maps on a feature space. Continuity supplies neither an inverse nor surjectivity. Even if $\pi_1$ were invertible onto its image, the composition would initially be defined only on that image; it need not extend to a structure-preserving automorphism of all $\mathsf D_7$.

For an elementary counterexample let $\mathsf X=[-1,1]^2$, $A=\operatorname{diag}(1,-1,0,\ldots,0)$ and

$$
\pi_1(x,z)=I/7+x^2A/28,\qquad
\pi_2(x,z)=I/7+x^2A/56.
$$

Both encoders are continuous, positive, trace-one and noninvertible. At $x\ne0$ they have different purities and cannot be related by unitary conjugation. This refutes an inference from continuity and state validity alone; any stronger functional or phenomenological premise must be stated as an explicit constraint and proved sufficient.

Covariance also does not fix an encoder. On $\mathsf D_7\times[0,1]$, both $(\Gamma,s)\mapsto\Gamma$ and $(\Gamma,s)\mapsto(1-s)\Gamma+sI/7$ are equivariant under simultaneous unitary conjugation. They are generally inequivalent and noninvertible.

### Residual symmetry {#residual-symmetry}

Let a declared group $K$ act on states. Uniqueness **up to $K$** requires the separate statement

$$
\mathsf O_\theta(\Gamma)=\mathsf O_\theta(\Sigma)
\quad\Longleftrightarrow\quad \Sigma\in K\cdot\Gamma.
$$

Observation invariance alone gives only the forward inclusion $K\cdot\Gamma\subseteq[\Gamma]_\theta$, not equality. The applicable residual group must preserve the full observation design, its labels, calibration and reported targets. It can be smaller than $G_2$, smaller than $\Gamma_{\!\mathrm{oct}}$, or trivial. An unobserved degree of freedom that changes a physical target is **nonidentifiability**, not automatically gauge. Frame alignment must not rotate an already fixed functional frame or conceal disagreements in $\Phi$ or $\mathrm{Coh}_E$.

## 3. A complete and stable linear observation model {#linear-frame}

Let $H_1,\ldots,H_m$ be calibrated Hermitian observation operators and

$$
M(\Gamma)_a=\operatorname{Tr}(H_a\Gamma),\qquad
\mathsf H_0=\{\Delta=\Delta^\dagger:\operatorname{Tr}\Delta=0\}.
$$

The real dimension of $\mathsf H_0$ is $7^2-1=48$.

:::info Theorem ID-2 (informational completeness and stability) [T]
The following are equivalent:

1. $M$ is injective on all $\mathsf D_7$.
2. $\ker M\cap\mathsf H_0=\{0\}$.
3. The projected operators $H_a-\operatorname{Tr}(H_a)I/7$ span $\mathsf H_0$.

If these conditions hold, define $\alpha=\inf_{\Delta\in\mathsf H_0,\|\Delta\|_{\mathrm{HS}}=1}\|M(\Delta)\|_2>0$. Then

$$
\|\Gamma-\Sigma\|_{\mathrm{HS}}
\leq\alpha^{-1}\|M(\Gamma)-M(\Sigma)\|_2.
$$

**Proof.** Differences of trace-one Hermitian matrices are traceless. If a nonzero traceless $\Delta$ lies in the kernel, $I/7\pm\varepsilon\Delta$ are distinct density matrices for sufficiently small $\varepsilon>0$ and have identical observations. This proves (1) iff (2); orthogonality to all projected operators proves (2) iff (3). Injectivity and compactness of the unit sphere of $\mathsf H_0$ give $\alpha>0$ and the bound. $\square$
:::

This finite-dimensional proof is included here. Operator frames and informationally complete quantum measurements are studied systematically by [Scott (2006)](https://arxiv.org/abs/quant-ph/0604049). For actual quantum measurements the $H_a$ must be implementable observables, or the corresponding effects must form specified POVMs; an arbitrary neural feature is not a known POVM effect merely because it is assigned an axis label.

An explicit coordinate design uses $E_{ij}=|i\rangle\langle j|$ and measures

$$
\operatorname{Tr}(E_{ii}\Gamma)=\gamma_{ii},\quad
\operatorname{Tr}\left(\frac{E_{ij}+E_{ji}}2\Gamma\right)=\operatorname{Re}\gamma_{ij},\quad
\operatorname{Tr}\left(\frac{i(E_{ij}-E_{ji})}2\Gamma\right)=\operatorname{Im}\gamma_{ij}.
$$

There are seven diagonal values with one trace relation, and $21+21$ real and imaginary coherences: **48 independent real coordinates**. In a general full-state linear design $m\geq48$ independent statistics are necessary. A single finite informationally complete POVM needs at least 49 outcomes because their probabilities sum to one. Neither count says that 48 samples suffice, nor that any 48 nonlinear features are globally identifying.

## 4. Phase information cannot be inferred from magnitudes {#phase-counterexamples}

Suppose the observation model depends only on $\gamma_{ii}$, $|\gamma_{ij}|$ and $\mathrm{Gap}_{ij}=|\sin\arg\gamma_{ij}|$ (zero for zero coherence). It is not informationally complete.

Take uniform diagonal $1/7$, $a=1/28$, nonzero coherences on the oriented triangle $(1,2),(2,3),(3,1)$ only, with all three values $ae^{i\pi/6}$ and Hermitian conjugates on the reverse edges. Strict diagonal dominance ($1/7>2a$) guarantees positive definiteness. This matrix and its complex conjugate have the same diagonal, magnitudes and Gap but opposite triangle holonomy

$$
\arg(\gamma_{12}\gamma_{23}\gamma_{31})=\pm\pi/2.
$$

Their spectra are equal; thus this first example demonstrates lost **oriented phase information**, not an entropy difference. To see lost spectral information too, change only the oriented phase on $(3,1)$ to $-\pi/6$. The same diagonal, magnitudes and all pairwise Gap values remain, while the holonomy becomes $\pi/6$. For this family

$$
\operatorname{Tr}(\Gamma^3)=\frac1{49}+\frac{18a^2}{7}+6a^3\cos(\theta_{12}+\theta_{23}+\theta_{31}),
$$

so these latter states have different spectra. An $\arcsin(\mathrm{Gap})$ rule picks a branch; it does not recover the phase. Phase-locking **value** $|\langle e^{i(\phi_i-\phi_j)}\rangle|$ is real and nonnegative. Signed phase requires the **complex** mean $\langle e^{i(\phi_i-\phi_j)}\rangle$, a declared reference and a validated link to $\gamma_{ij}$. Missing signed measurements must remain missing.

$P$, $R$ and the canonical $\Phi$ can be identified from complete diagonal and magnitude information in a fixed frame, even when the whole state is not. Spectral quantities and phase-sensitive targets need separate identification checks; positivity can restrict possible phases but does not remove the counterexamples above.

## 5. Nonlinear, boundary and dynamical identification {#local-identification}

For a $C^1$ statistic map $F_\theta$ near a full-rank state, use any local coordinates $q\in\mathbb R^{48}$. If $D_qF_\theta$ has column rank 48, some 48 output coordinates have an invertible Jacobian. The inverse-function theorem gives **local** identification and a local stability estimate. This is sufficient, not necessary at singular points: $x\mapsto x^3$ is injective although its derivative vanishes at zero. Full rank does not rule out distant states with the same data. Rank deficiency throughout a constant-rank neighborhood gives local fibers; an isolated deficient Jacobian alone does not establish nonidentifiability.

For a Gaussian mean model $y\sim\mathcal N(F_\theta(q),\Sigma)$ with known $\Sigma\succ0$, the Fisher matrix is $J^T\Sigma^{-1}J$. Nonsingularity gives the preceding local criterion. General Fisher-information equivalences require regularity assumptions; they must not be transferred unchanged to rank-deficient boundary states or state-dependent support. Rank-$r$ states form a stratum of real dimension $14r-r^2-1$, and identification under a rank prior must distinguish that stratum from nearby states of other ranks. See [Heinosaari, Mazzarella and Wolf (2013), *Quantum Tomography under Prior Information*](https://arxiv.org/abs/1109.5478).

State reconstruction, dynamic-rate identification and validation of an encoder are different problems. For known linear dynamics $\Gamma(t)=\mathcal T_t(\Gamma_0)$, observations at times $t_k$ identify the initial state iff

$$
\Delta\longmapsto\big(M\mathcal T_{t_k}(\Delta)\big)_k
$$

is injective on $\mathsf H_0$. Unknown rates require joint identification with $\Gamma_0$. A sufficiently rich time series can supply otherwise missing information, but neither existence of an ODE nor uniqueness of its solutions proves observability. A dissipative inverse can also be poorly conditioned despite being unique.

## 6. Reconstruction must carry uncertainty {#uncertainty}

In the linear Gaussian model, solve the convex problem

$$
\hat\Gamma\in\arg\min_{\Gamma\in\mathsf D_7}
\|\Sigma^{-1/2}(M(\Gamma)-y)\|_2^2.
$$

Continuity and compactness ensure a minimizer exists; ID-2 and $\Sigma\succ0$ give a strictly convex objective on the trace-one affine space and hence a unique minimizer. With an incomplete design there can be multiple minimizers. A prior or tie-breaking rule may select one; this is not information obtained from the data.

Report a calibrated confidence set, for example

$$
\mathcal C_\varepsilon(y)=\{\Gamma\in\mathsf D_7:
\|\Sigma^{-1/2}(M(\Gamma)-y)\|_2\leq\varepsilon\},
$$

with the coverage rule for $\varepsilon$ predeclared and verified under the noise and calibration model. If this set is empty, report observation-model incompatibility; do not force a state into the tested viability window. If ID-2 holds and $\alpha$ is calculated for the whitened map, its diameter is at most $2\varepsilon/\alpha$. Also $|P(\Gamma)-P(\Sigma)|\leq2\|\Gamma-\Sigma\|_{\mathrm{HS}}$ and $|R(\Gamma)-R(\Sigma)|\leq7|P(\Gamma)-P(\Sigma)|$ on $\mathsf D_7$.

For each target report its range over $\mathcal C_\varepsilon$. A verdict is determinate only if the predicate is constant on that set; otherwise report **undetermined by this measurement**. An optimizer's representative is not a substitute for this check.

## 7. Confirmatory protocol obligations {#confirmatory}

The [SUB-1 … SUB-6 safeguards](/docs/applied/research/measurement-protocol#substitution-position) remain in force: freeze calibration on wakefulness, exclude PCI and behavior from the confirmatory predictor, and set $\lambda_1=\lambda_2=0$. Add:

- **ID-A:** preregister the observation law, signed phase measurements, functional frame, missing-data handling, noise model and independent setting design; demonstrate global identification on the claimed admissible set or explicitly report partial identification.
- **ID-B:** publish the rank and smallest singular value of the calibrated design/Jacobian, calibration uncertainty, state confidence sets and recovery tests on synthetic states that include the phase counterexamples.
- **ID-C:** preregister target ranges and undetermined verdicts; never replace missing signed phases by zero or by $\arcsin(\mathrm{Gap})$.
- **ID-D:** compare held-out predictive performance with equally specified alternative encoders and models of comparable complexity. Separate performance of the frozen classifier, adequacy of its observation model, and the ontological claim that its state is the system's $\Gamma$.

These requirements strengthen an experiment by making its failure informative. They do not supply a phenomenological or ontological bridge by definition.
