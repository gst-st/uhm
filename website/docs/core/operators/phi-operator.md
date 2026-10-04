---
sidebar_position: 1
title: "φ-operator of self-modelling"
description: "Typed numerical self-models, frozen quantum channels, and their categorical scope"
---

# The Self-Modelling Operator φ

In the evolution equation, $\varphi$ denotes a specified numerical self-model: a map taking a current state $\Gamma$ to a target state. A fixed point $\varphi(\Gamma_*)=\Gamma_*$ expresses consistency of this map. Reading that equality as accurate self-knowledge requires an independent representation/error model [I]. The fixed point is not automatically a stationary state of the full dynamics or a conscious state.

:::info Canonical typing — revised 2026-10-03
The rigorous definitions and proofs are in [Formalization of φ](/docs/proofs/categorical/formalization-phi). A **logical support reflector** $L_G$ in a topos slice, a **numerical map** $M=\varphi$ on density matrices, a **frozen CPTP realization** $\mathcal C_\lambda$, and an **asymptotic basin retraction** $r$ are different constructions. Their former unconditional equivalence is withdrawn [✗].
:::

## Intuition and historical motivation {#интуиция-зеркало}

An internal model is a chosen representation of the system's state. Loss of coherence, a predictive filter, a learned target, and a stabilizing feedback target describe different tasks. Their identification requires a modeling hypothesis. Hofstadter's strange loops, Rosen's closure under efficient causation, and predictive-processing models motivate questions of self-reference; they do not prove a particular anchor or channel. The former claim that the UHM free-energy functional derives $\varphi$ is withdrawn: that functional is cross-entropy and generally has a different minimizer.

## Definition and construction order {#определение}

$$
M:\mathcal D(\mathbb C^7)\longrightarrow\mathcal D(\mathbb C^7),\qquad\varphi=M.
$$

A model law must be specified on all states under study. For the families below first define $P=\mathrm{Tr}\,\Gamma^2$, $R=1/(7P)$, $k=1-R$, a fixed predictive channel $\mathcal P_\alpha$, and an anchor law $\sigma(\Gamma)$. Then

$$
M(\Gamma)=k(\Gamma)\mathcal P_\alpha(\Gamma)+R(\Gamma)\sigma(\Gamma).
$$

This is a continuous state-preserving map when the anchor law is continuous. It is generally nonlinear and **is not one CPTP channel**. For each current state the parameters can be frozen to obtain a linear channel on operators,

$$
\mathcal C_{k,\sigma}(X)=k\mathcal P_\alpha(X)+(1-k)\mathrm{Tr}(X)\sigma.
$$

The trace factor is essential for linearity on arbitrary operators. A state-dependent Kraus family certifies the frozen channels; it does not make the overall adaptive map linear or establish its physical implementation.

| Construction | Type and scope |
|---|---|
| Logical support | $L_G\dashv i_G:\mathrm{Sub}_{\mathcal E}(G)\hookrightarrow\mathcal E_{/G}$; image/$(-1)$-truncation **in the slice** [T] |
| Numerical self-model | $M:\mathcal D(\mathcal H)\to\mathcal D(\mathcal H)$; explicit map [D] |
| Frozen physical channel | $\mathcal C_{k,\sigma}$; CPTP at fixed parameters [T] |
| Long-time limit | $r(\Gamma)=\lim_{t\to\infty}F_t(\Gamma)$; idempotent if a continuous autonomous flow converges to fixed points within the stated domain [T at convergence] |

A support reflector neither chooses a density matrix nor minimizes a metric distance. No zero-mode projection of a nonlinear stability Jacobian defines $M$: at a hyperbolic attracting equilibrium its trace-zero tangent Jacobian has no zero eigenvalue. Idempotency by itself supplies no adjunction. [Full proof and withdrawal](/docs/proofs/categorical/formalization-phi#эквивалентность-определений-phi).

## Bootstrap and fixed points {#бутстрап}

The explicit anchor laws below are evaluated on the current $\Gamma$; they do not use the unknown attractor in their own definition. This removes the apparent circularity directly. A continuous $M$ has a fixed point by Brouwer; uniqueness and convergence require further evidence. For $M_{\mathrm{coh}}$ the unique fixed point is $I/7$, and its iterates converge by an estimate of deviation from that state. This estimate is not a global Banach contraction. A hyperbolic equilibrium of the full regenerative flow must instead be found and checked for that flow.
<a id="три-отображения-сжатие"></a>

:::note Which φ contracts: three maps, and the fed loop
Three maps called φ in the corpus behave differently in the Frobenius norm. Write $x = \Gamma - I/7$, $t = 7\lVert x\rVert_F^2$, so that $P = (1+t)/7$ and $R = 1/(7P) = 1/(1+t)$ ([T-126](/docs/proofs/consciousness/conscious-window#t-126)).

| Map | Deviation from $I/7$ | Lipschitz constant | Fixed point |
|---|---|---|---|
| canonical $\varphi_{\mathrm{coh}} = k\,\mathcal{P}_\alpha(\Gamma) + (1-k)\,I/7$, $k = 1 - R$ | $k\,\mathcal{P}_\alpha x$, factor $\leq 6/7$ | $9/8$ for every $\alpha$: radial derivative $t(t+3)/(1+t)^2$, largest at $t = 3$, $P = 4/7$; $54/49$ at pure states | $I/7$ |
| dissipative replacement form (T-62, T-249), $R\,\Gamma + (1-R)\,I/7$ | $R\,x$ | $1$: radial derivative $(1-t)/(1+t)^2 \in [-1/8, 1]$ | $I/7$ |
| replacement toward the previous map, $(1-k^2)\,\Gamma + k^2\,I/7$ | $\bigl(1 - (1-R)^2\bigr)\,x$ | $1$: radial derivative $1 - t^2(t+5)/(1+t)^3 \in [-17/108, 1]$ | $I/7$ |

The third map is the one on which the closed form $R_\varphi = 1 - (1-R)^4\,\lVert\Gamma - I/7\rVert_F^2/\lVert\Gamma\rVert_F^2$ of the [self-observation table](/docs/consciousness/foundations/self-observation#мера-рефлексии-r) holds exactly; the second gives $R_\varphi = 1 - (1-R)^3$, and $\varphi_{\mathrm{coh}}$ gives neither. It is also the "canonical φ of UHM" of Foundations of Mathematics, Part XVIII, ch. 9 (Theorems 9.5–9.8, "radial contraction", "global Banach of the loop"). The two corpora therefore do not contradict each other: "not a contraction, $54/49$" concerns $\varphi_{\mathrm{coh}}$, "non-expanding" concerns the replacement forms. For the fed loop $L_H(\Gamma) = U\,[(1-\mu)\,\varphi(\Gamma) + \mu\,\Theta]\,U^\dagger$ with $U = e^{-iHt}$ the feed cancels in differences and $U$ is an isometry, so $\mathrm{Lip}(L_H) = (1-\mu)\,\mathrm{Lip}(\varphi)$: at most $1 - \mu$ for the replacement forms, a Banach contraction for every $\mu > 0$ and every $H$; at most $\tfrac98(1-\mu)$ for $\varphi_{\mathrm{coh}}$, a contraction for $\mu > 1/9$ — at $\mu = 0.05$ two diagonal states near $P = 4/7$ move apart by the factor $1.069$. All three maps have the single fixed point $I/7$, and none of them keeps an isolated holon alive ([dead isolation](/docs/core/dynamics/evolution#теорема-мёртвая-изоляция); the living self-models are $\varphi_s$ and $\varphi_J$, [below](#phi-s)). Numbers: `test_three_self_model_maps_lipschitz_constants_and_the_fed_loop`.
:::

---
## Base dephasing and actual scope {#phi-base}

$$
M_{\mathrm{base}}(\Gamma)=\Delta(\Gamma)=\sum_i|i\rangle\langle i|\Gamma|i\rangle\langle i|.
$$

This is a linear unital CPTP channel and is idempotent. It removes all coherences. Its fixed points are all diagonal states, not only $I/7$. A nonuniform diagonal state can have $P>2/7$, so dephasing is incompatible with the full integrated predicate $\Phi\geq1$, rather than with purity-based viability in every state.

For the separate mixed map $M_{\mathrm{coh}}=k\mathcal P_\alpha+R I/7$, all frozen realizations are unital and the nonlinear map preserves $I/7$; this usage of "unital target" does not assert linearity. Its purity cannot exceed the input purity: $\|M_{\mathrm{coh}}\Gamma-I/7\|_F\leq k\|\Gamma-I/7\|_F$.

<a id="свойства"></a>

### Fixed point of the uniform-anchor model {#неподвижная-точка-phi-coh}

**Theorem [T].** $M_{\mathrm{coh}}$ has the unique fixed point $I/7$ with $P=1/7$. Indeed, off-diagonal fixed-point equations are $\gamma_{ij}=kc\gamma_{ij}$ with $kc<1$, and the diagonal equations give $\gamma_{ii}=k\gamma_{ii}+R/7$, hence $\gamma_{ii}=1/7$. The iterated limit is the constant reset to $I/7$, but a finite step is not idempotent. This uniform-anchor model cannot sustain isolated life in the stated regenerative dynamics. Living constructions need a different anchor law or environmental drive.

## Fano filtering and integration {#каноническая-конструкция-φ_coh-из-фано-структуры}

### Coherence preservation is not preservation of life {#интуиция-фано}

Fano line filtering attenuates rather than erases nonzero pair coherences. This is an algebraic property of the filter. A nonzero coherence is insufficient for viability or consciousness; a target can retain coherences and still have $P\leq2/7$ or $\Phi<1$.

#### Exact attenuation bounds {#математика-смешивания}

Put $d=\sum_i\gamma_{ii}^2$, $s=\sum_{i\ne j}|\gamma_{ij}|^2$ and $\Phi=s/d$. Since $d\geq1/7$ and $P=d+s\leq1$, $\Phi\leq6$. The equal-weight Fano channel preserves $d$ and sends $s$ to $s/9$, so

$$
\Phi(\mathcal P_{\mathrm{Fano}}\Gamma)=\Phi(\Gamma)/9\leq2/3<1.
$$

At a uniform diagonal its output purity is at most $5/21<2/7$. Thus the former assertion that the Fano channel itself preserves life or the integrated predicate is withdrawn [✗]. For $\mathcal P_\alpha$, the bound is even smaller when $\alpha>0$.

**Theorem (Uniform-anchor self-model is never an integrated target) [T].** For every state and $0\leq\alpha\leq1$,

$$
\Phi(M_{\mathrm{coh}}\Gamma)=
\frac{k^2c^2s}{1/7+k^2(d-1/7)}\leq6k^2c^2\leq24/49<1,
\qquad c=(1-\alpha)/3.
$$

*Proof.* Use $s\leq1-d$. For fixed $k,c$ the resulting ratio decreases with $d\geq1/7$, so its maximum is $6k^2c^2$. Now $k\leq6/7$ and $c\leq1/3$. Equality in the final bound is attained by a uniform-amplitude pure state at $\alpha=0$. $\square$ A self-model target need not itself satisfy the current system's full predicate; such a requirement would be an additional hypothesis. The result identifies the limitations of this target law without changing $M_s$ or $M_J$.
### Chosen atomic and Fano filters

:::note DRY: Master definition
Complete definitions of atomic and Fano Lindblad operators are in [Lindblad Operators](/docs/core/operators/lindblad-operators#атомы-классификатора). Below are the key formulas needed for the construction of φ_coh.
:::

The numerical model specifies atomic projectors $|k\rangle\langle k|$ and composite filters. They are not identified with the subobject classifier without realization data. The [Fano plane](/docs/physics/gauge-symmetry/fano-selection-rules) $PG(2,2)$ defines 7 linear subobjects — projections onto 3-dimensional subspaces:

$$
\Pi_p = \sum_{i \in \mathrm{line}_p} |i\rangle\langle i|, \quad p = 1, \ldots, 7
$$

:::tip Theorem: Completeness of Fano atoms
Each dimension lies on exactly 3 Fano lines. Therefore: $\sum_{p=1}^{7} \Pi_p = 3I$.
[Proof →](/docs/proofs/gap/fano-channel#фано-канал) | Status: **[T]**
:::

### Fano predictive channel $\mathcal{P}_{\text{Fano}}$

For each Fano line $p = (i,j,k)$ a [Lindblad operator](/docs/core/operators/lindblad-operators) is defined:

$$
L_p^{\text{Fano}} := \frac{1}{\sqrt{3}}\,\Pi_p = \frac{1}{\sqrt{3}}(|i\rangle\langle i| + |j\rangle\langle j| + |k\rangle\langle k|)
$$

The Fano predictive channel:

$$
\mathcal{P}_{\text{Fano}}(\Gamma) := \sum_{p=1}^{7} L_p^{\text{Fano}}\,\Gamma\,(L_p^{\text{Fano}})^\dagger = \frac{1}{3}\sum_{p=1}^{7} \Pi_p\,\Gamma\,\Pi_p
$$

:::info CPTP verification
$\sum (L_p^{\text{Fano}})^\dagger L_p^{\text{Fano}} = I$ — full proof in [Lindblad Operators](/docs/core/operators/lindblad-operators#фано-операторы).
:::

### Theorem: The Fano channel preserves coherences

:::tip Theorem: Preservation of coherences by the Fano channel
For an arbitrary coherence matrix $\Gamma$:

**(a)** Diagonal elements are preserved exactly: $[\mathcal{P}_{\text{Fano}}(\Gamma)]_{ii} = \gamma_{ii}$

**(b)** Coherences are preserved with coefficient $1/3$: $[\mathcal{P}_{\text{Fano}}(\Gamma)]_{ij} = \frac{1}{3}\gamma_{ij}$ for $i \neq j$

**(c)** For nonzero input coherences, phases are preserved exactly: $\arg([\mathcal{P}_{\text{Fano}}(\Gamma)]_{ij}) = \arg(\gamma_{ij})$

Key difference from $\varphi_{\text{base}}$: the Fano channel **scales** coherence amplitudes without phase distortion, whereas $\varphi_{\text{base}}$ destroys them entirely.
[Proof →](/docs/proofs/gap/fano-channel#теорема-фано-канал) | Status: **[T]**
:::

### Canonical form of φ_coh

:::info Definition: Uniform-anchor form of φ_coh [D]
Canonical coherence-preserving self-modelling:

$$
\varphi_{\text{coh}}(\Gamma) = k \cdot \left[\alpha \cdot \mathcal{P}_{\text{base}}(\Gamma) + (1 - \alpha) \cdot \mathcal{P}_{\text{Fano}}(\Gamma)\right] + (1 - k) \cdot \Gamma_{\text{anchor}}
$$

where:
- $\mathcal{P}_{\text{base}}(\Gamma) = \sum_m P_m\,\Gamma\,P_m = \mathrm{diag}(\Gamma)$ — atomic channel (from [φ formalisation](/docs/proofs/categorical/formalization-phi))
- $\mathcal{P}_{\text{Fano}}(\Gamma) = \frac{1}{3}\sum_p \Pi_p\,\Gamma\,\Pi_p$ — Fano channel
- $\alpha \in [0, 1]$ — **decoherence depth parameter** (balance between atomic and Fano observation)
- $k = 1 - R$ — compression parameter determined by the [reflexion measure](/docs/consciousness/foundations/self-observation#теорема-k-из-r) $R=1/(7P)=1-\|\Gamma-I/7\|_F^2/P$ **[T]**. Not a free parameter
- $\Gamma_{\text{anchor}} = \rho^*_{\mathrm{diss}} = I/7$ — **anchor state**, coinciding with the attractor of the dissipative part $\mathcal{L}_0$. This is an explicit dissipative-reference anchor [D]. A specified primitive unital linear generator has stationary state $I/7$; that fact does not force the feedback anchor. As an independently varied constant weight $k$ tends to one, the formula tends to $\mathcal P_\alpha(\Gamma)$, not $I/7$; in the adaptive law $k\leq6/7$.

$\mathcal{P}_\alpha = \alpha\,\mathcal{P}_{\text{base}} + (1-\alpha)\,\mathcal{P}_{\text{Fano}}$ — a convex combination of CPTP channels, hence CPTP.
[Proof →](/docs/proofs/gap/fano-channel#phi-coh) | Status: **[T]**
:::

### Target coherences of φ_coh

:::tip Theorem: Target coherences of φ_coh
**(a)** Magnitude of the target coherence (with diagonal anchor): $|\gamma_{ij}^{\text{target}}| = \frac{k(1-\alpha)}{3} \cdot |\gamma_{ij}|$

**(b)** If $kc\gamma_{ij}\ne0$, target phase is **preserved**: $\theta_{ij}^{\text{target}} = \theta_{ij}$

**(c)** Under the same nonzero-coherence condition, target Gap is **preserved**: $\mathrm{Gap}^{\text{target}}(i,j) = \mathrm{Gap}(i,j)$

The canonical $\varphi_{\text{coh}}$ **does not seek to change the Gap** — it reproduces the Gap with a reduced amplitude, scaling coherences without phase distortion.
[Proof →](/docs/proofs/gap/fano-channel#phi-coh) | Status: **[T]**
:::

---

## Explicit coefficients $c_{mn}$

General form of the coherence-preserving channel from the definition of $\varphi_{\text{coh}}$:

$$
\mathcal{P}_{\text{coh}}(\Gamma) = \sum_{m,n} c_{mn}\,|m\rangle\langle n|\,\Gamma\,|n\rangle\langle m|
$$

:::tip Theorem: Explicit coefficients $c_{mn}$
The coefficients of the canonical $\varphi_{\text{coh}}$, given the Fano weight $\alpha$:

$$
c_{mn} = \begin{cases} k & m = n \text{ (the atomic and the Fano channel both keep the diagonal)} \\ (1-\alpha) k / 3 & m \neq n \end{cases}
$$

and the anchor adds $(1-k)\,[\Gamma_{\text{anchor}}]_{mn}$. Every pair $(m,n)$ lies on exactly one Fano line, so a third case "$0$ for $(m,n)$ not on a common Fano line" is empty. *Corrected 2026-09-25:* the box printed $c_{mm} = \alpha^* k$ and that empty third case; the diagonal coefficient is $\alpha k + (1-\alpha)k = k$ (as in [$G_2$-structure, Theorem 10.5](/docs/physics/gauge-symmetry/g2-structure)), and $\alpha^*$ is retracted.

The coefficients are determined through:
- The [Fano structure](/docs/physics/gauge-symmetry/fano-selection-rules) $PG(2,2)$ (algebraic geometry)
- The Fano weight $\alpha$ — a free parameter; its variational value $\alpha^* \approx 1 - 2/(7P)$ is retracted (see below)
- The compression parameter $k$ (from [φ formalisation](/docs/proofs/categorical/formalization-phi))

[Proof →](/docs/proofs/gap/fano-channel#phi-coh) | Status: **[T]**
:::

:::info Frozen-channel Kraus operators (7 + 7 + 49; corrected 2026-09-25)
The weight $k$ and anchor are held fixed in this linear channel. Evaluating them anew on each input produces a nonlinear state map, not one channel.
Atomic operators (7): $K_m^{(\text{atom})} = \sqrt{\alpha k} \cdot |m\rangle\langle m|$. Fano operators (7): $K_p^{(\text{Fano})} = \sqrt{(1-\alpha) k / 3} \cdot \Pi_p$. Anchor operators (49), with $\Gamma_{\text{anchor}} = \sum_i \lambda_i |\psi_i\rangle\langle\psi_i|$: $K_{ij}^{(\text{anch})} = \sqrt{(1-k)\lambda_i} \cdot |\psi_i\rangle\langle j|$. Verification: $\sum_m (K_m^{(\text{atom})})^\dagger K_m^{(\text{atom})} = \alpha k \cdot I$; $\sum_p (K_p^{(\text{Fano})})^\dagger K_p^{(\text{Fano})} = \tfrac{(1-\alpha)k}{3} \cdot 3I$ (every point lies on three lines); $\sum_{i,j} (K_{ij}^{(\text{anch})})^\dagger K_{ij}^{(\text{anch})} = (1-k) \cdot I$; total $I$. The 63 operators reproduce $\varphi_{\text{coh}}$ to $3 \times 10^{-16}$ on 50 random states. The former set — $K_m^{(\text{atom})} = \sqrt{\alpha^* k/7}\,|m\rangle\langle m|$, one anchor $K_0 = \sqrt{(1-k)/7}\,I$ — was not trace-preserving: $\sum_m |m\rangle\langle m| = I$, not $7I$, and $K_0^\dagger K_0 = \tfrac{1-k}{7}\,I$; for $\alpha = 0.4$, $k = 0.8$ it misses $I$ by $1.18$ in Frobenius norm, and a single multiple of $I$ cannot implement the replacement $\Gamma \mapsto (1-k)\,\Gamma_{\text{anchor}}$. Same correction as [$G_2$-structure, Theorem 10.5](/docs/physics/gauge-symmetry/g2-structure).
:::

---
## Free Fano weight and retracted variational formula {#эскиз-вывода-alpha}

The weight $\alpha\in[0,1]$ remains a model parameter. For full-rank $\Gamma$, the former functional equals $-\mathrm{Tr}(\mathcal P_\alpha(\Gamma)\log\Gamma)$ and is affine in $\alpha$ with nonnegative slope
$\tfrac13[D(\Gamma\Vert\Delta\Gamma)+D(\Delta\Gamma\Vert\Gamma)]$.
Its minimum is at $\alpha=0$ whenever there are coherences; it has no derived interior optimum $1-2/(7P)$. That formula and the associated prediction-accuracy ranking are withdrawn [✗]. A filter's predictive accuracy requires a specified prediction task, data and loss.

### Example with a chosen parameter {#числовой-пример-phi}

At $P=0.4$, $R=5/14$, $k=9/14$. Choosing $\alpha=2/7$ gives off-diagonal attenuation $kc=15/98\approx0.1531$ for the uniform-anchor model. This is a calculation conditional on the chosen $\alpha$, not an optimum derived from purity. Its iterated limit remains $I/7$.
## Why an isolated holon needs a non-unital self-model: the self-registering form φ_s {#phi-s}

The canonical $\varphi_{\mathrm{coh}}$ preserves coherences, which is insufficient for an integrated viable target. Coherences are necessary for the integrated predicate $\Phi\geq1$, not for purity alone. Its anchor $I/7$ makes it unital, and a unital self-model cannot raise purity: an isolated holon regenerating toward $\varphi_{\mathrm{coh}}(\Gamma)$ dies whatever $\kappa$ is ([dead isolation](/docs/core/dynamics/evolution#теорема-мёртвая-изоляция) [T]).

:::tip Theorem (Symmetric linear self-models are unital) [T]
A linear CPTP self-model covariant under $G_2$, or under the frame group $\Gamma_{\mathrm{oct}}$, is unital. So is $\varphi_{\mathrm{coh}}$ for every $\alpha$ and $k$.
:::

Here the first assertion concerns linear channels; the second concerns each frozen realization of the nonlinear $M_{\mathrm{coh}}$.

*Proof.* $\Phi(I)$ commutes with an irreducible representation, so it is a multiple of $I$ (Schur), equal to $I$ by trace preservation; $G_2$ and $\Gamma_{\mathrm{oct}}$ act irreducibly on $\mathbb{C}^7$ ([evolution, dead isolation, item 3](/docs/core/dynamics/evolution#теорема-мёртвая-изоляция)). $\blacksquare$

So an anchor that keeps a holon alive either breaks the symmetry from outside — the environmental anchor of an embodied holon ([T-148](/docs/proofs/consciousness/substrate-closure#t-148)) — or depends on the state itself, which lets a covariant law have non-symmetric fixed points.

:::tip Lemma (Intrinsic anchors are spectral) [T]
Let $\sigma$ send states to states with $\sigma(U\Gamma U^\dagger) = U\sigma(\Gamma)U^\dagger$ for every unitary $U$ — the anchor refers to nothing outside the holon. If $\Gamma = \sum_i \lambda_i |i\rangle\langle i|$ has distinct eigenvalues, then $\sigma(\Gamma) = \sum_i s_i |i\rangle\langle i|$ is diagonal in the eigenbasis of $\Gamma$, and $\mathrm{Tr}(\Gamma\sigma(\Gamma)) = \sum_i \lambda_i s_i$. The constant anchor $s_i = 1/7$ gives overlap $1/7 < P$ for every $\Gamma \neq I/7$; the choice $s_i = \lambda_i$ ($\sigma(\Gamma) = \Gamma$) makes the regeneration target at $\Gamma$ equal to the image of $\Gamma$ under the unital $k\mathcal{P}_\alpha + R\,\mathrm{id}$; the choice $s_i = \lambda_i^2/\sum_j \lambda_j^2$ gives $\mathrm{Tr}\,\Gamma^3/\mathrm{Tr}\,\Gamma^2 \geq P$, with equality only for a flat spectrum.
:::

*Proof.* The unitaries $U = \sum_i e^{i\theta_i}|i\rangle\langle i|$ fix $\Gamma$, so $U\sigma(\Gamma)U^\dagger = \sigma(\Gamma)$ for all phases $\theta_i$, which forces $\sigma(\Gamma)$ to be diagonal in $\{|i\rangle\}$. The overlap is then $\sum_i\lambda_i s_i$. For $s_i \propto \lambda_i^2$ the inequality $\sum_i\lambda_i^3 \geq (\sum_i\lambda_i^2)^2$ is Chebyshev's sum inequality with the weights $\lambda_i$. $\blacksquare$

The weights $s \propto \lambda^q$ order the intrinsic anchors: $q=0$ is defined separately as $I/7$ (including at rank-deficient states), $q = 1$ is the state itself, and both are dead by the theorem of dead isolation; $q = 2$ is the lowest integer exponent greater than one; all real $q>1$ sharpen a nonflat spectrum. At $q \to \infty$ the anchor becomes the normalized projector onto the top eigenspace of $\Gamma$ (rank one only for a nondegenerate largest eigenvalue) — the minimiser, over CPTP channels, of the cross-entropy $-\mathrm{Tr}(\psi(\Gamma)\log\Gamma)$ of the [retracted variational principle](/docs/proofs/dynamics/fep-derivation) — which is discontinuous where the top eigenvalue is degenerate.

**Definition [D] (self-registering self-model).**

$$
\varphi_s(\Gamma) = k\,\mathcal{P}_\alpha(\Gamma) + R\,\frac{\Gamma^2}{\mathrm{Tr}\,\Gamma^2}, \qquad R = \frac{1}{7P},\quad k = 1 - R .
$$

The anchor $\Gamma^2/\mathrm{Tr}\,\Gamma^2 = \sqrt{\Gamma}\,\Gamma\,\sqrt{\Gamma}/\mathrm{Tr}(\Gamma^2)$ is the Lüders update of $\Gamma$ on the effect $\Gamma$: a formal state-dependent conditional update. Interpreting it as physical self-registration requires a controller/readout premise [I]/[H]; a fixed instrument cannot access an arbitrary unknown $\Gamma$ as its own effect automatically. It is smooth on all states ($\mathrm{Tr}\,\Gamma^2 \geq 1/7$) and differs from $\varphi_{\mathrm{coh}}$ only in the anchor. With it an isolated holon has at least seven self-sustaining attractors with $P > 2/7$ ([evolution](/docs/core/dynamics/evolution#теорема-самоподдерживающийся-аттрактор) [T]); at $H = 0$ they are the basis projectors, where $\varphi_s(|e_m\rangle\langle e_m|)=|e_m\rangle\langle e_m|$. Interpreting this equality as self-knowledge is [I]. That the self-model of a physical holon is $\varphi_s$ rather than $\varphi_{\mathrm{coh}}$ is not derived from the axioms [Pr]; that it must be non-unital for an isolated holon to live is [T].

## What the axioms fix about the anchor, and the collineation anchor φ_J {#phi-j}

The attractors of $\varphi_s$ lie above the conscious window, and they are localised. The reason is not the choice $q = 2$: a self-model covariant under the diagonal unitaries — every intrinsic anchor, every anchor built from the Fano projectors — holds no hyperbolic attractor in $\mathcal{V}_{\mathrm{full}}$ near $H = 0$ ([phase-reference obstruction](/docs/core/dynamics/evolution#теорема-фазовое-препятствие) [T]). Such a self-model can reach the window by purity — the Fano-line registration of the same theorem holds $P = 1/3$ for every $\kappa$ — but not $\Phi \geq 1$.

:::tip Theorem (Symmetric anchors) [T]
Let a self-model have the replacement form $\varphi(\Gamma) = k\,\mathcal{P}_\alpha(\Gamma) + R\,\rho_a$ with an anchor $\rho_a$ independent of $\Gamma$.

1. If $\varphi$ is covariant under $G_2$, under the signed frame group $\Gamma_{\mathrm{oct}}$, or under the full group of monomial unitaries that permute the Fano lines (permutations with arbitrary phases), then $\rho_a = I/7$ and $\varphi$ is unital.
2. If $\varphi$ is covariant under the 168 collineations of the Fano plane acting as permutations of the basis, then $\rho_a = (1 - t)\,I/7 + t\,uu^\dagger$ with $u = (1, \dots, 1)/\sqrt7$ and $t \in [-1/6, 1]$; it is unital only for $t = 0$ and pure only for $t = 1$.
:::

*Proof.* $\mathcal{P}_\alpha$ is covariant under each of these groups (they map Fano lines to lines, and $\mathcal{P}_{\mathrm{base}}$ commutes with monomial unitaries), so covariance of $\varphi$ is $M\rho_aM^\dagger = \rho_a$ for every $M$ of the group, i.e. $\rho_a$ lies in the commutant. For $G_2$ and $\Gamma_{\mathrm{oct}}$ the commutant is $\mathbb{C}I$ ([dead isolation, item 3](/docs/core/dynamics/evolution#теорема-мёртвая-изоляция)); for the monomial group the diagonal phases force $\rho_a$ diagonal and the 2-transitive permutations force its diagonal constant. The 168 collineations act 2-transitively on the points, so the permutation representation has two orbits on pairs of indices — equal and distinct — and its commutant is spanned by $I$ and $J$ ($J/7 = uu^\dagger$). The eigenvalues of $(1 - t)I/7 + t\,uu^\dagger$ are $(1 + 6t)/7$ and $(1 - t)/7$, which gives $t \in [-1/6, 1]$. $\blacksquare$

**What categorical structure leaves open.** The support adjunction lives in a topos slice and derives no numerical anchor, CPTP feedback law or rate. In the category of quantum channels the terminal system is one-dimensional; the unique discard map does not pick a unique preparation of a seven-dimensional state. The reference $I/7$ follows instead from maximum entropy or irreducible covariance, if imposed. Lawvere's fixed-point theorem requires its own point-surjectivity hypothesis; Brouwer supplies existence for continuous state maps, not a preferred anchor. The numerical law and its frozen channel compilation are specified separately. See [typed formalization](/docs/proofs/categorical/formalization-phi#категориальное-определение-φ).

What does fix the anchor is the frame group read at the level where it is compatible with life.

<a id="t-334"></a>

:::tip Theorem T-334 (The collineation anchor, derived up to gauge) [T]
Let the self-model have the replacement form $\varphi(\Gamma) = k\,\mathcal{P}_\alpha(\Gamma) + R\,\rho_a$ with a $\Gamma$-independent anchor, and let the isolated holon evolve by the gated dynamics with the Fano dissipator ([evolution](/docs/core/dynamics/evolution#теорема-живой-аттрактор-в-окне)); $c = (1 - \alpha)/3$.

1. **Frame covariance and life.** $\varphi$ is $\Gamma_{\mathrm{oct}}$-covariant, or $\mathcal{P}_\alpha \circ \varphi$ is ($\alpha \lt 1$), only for $\rho_a = I/7$, which is dead. The atomic reading $\mathcal{P}_{\mathrm{base}} \circ \varphi$ is $\Gamma_{\mathrm{oct}}$-covariant if and only if $\mathrm{diag}\,\rho_a = I/7$; the stationary diagonal at $H = 0$ then is $I/7$ as well, so $\sigma_k = 0$ on every axis.
2. **Viability depends on one number.** If $\mathrm{diag}\,\rho_a = I/7$, a hyperbolic sink in $\mathcal{V}_{\mathrm{full}}$ at $H = 0$ exists exactly for $\kappa > \kappa_c(s)$, where $s = P(\rho_a) - 1/7$ is the coherent purity of the anchor; $\kappa_c(s)$ is that of the family $(1-t)I/7 + t\,uu^\dagger$ with $t = \sqrt{7s/6}$, strictly decreasing in $s$, and finite exactly for $s > (2 - c)^2/7$.
3. **Most viable = most informative.** Hence among anchors that privilege no axis the one whose living range of $\kappa$ contains every other one's is a pure state with uniform diagonal, $\rho_a = D\,uu^\dagger D^\dagger$ with $D$ a diagonal unitary, $u = (1, \dots, 1)/\sqrt7$. Maximal viability and maximal information (purity) select the same anchor.
4. **Gauge.** Diagonal unitaries commute with $\mathcal{D}_\Omega$ and $\mathcal{P}_\alpha$ and leave $P$, $R$, $g_V$ invariant, so conjugation by $D$ carries the dynamics with anchor $uu^\dagger$ and Hamiltonian $D^\dagger H D$ onto that with anchor $D\,uu^\dagger D^\dagger$ and $H$. At $H = 0$ the anchors $D\,uu^\dagger D^\dagger$ give conjugate flows; $\varphi_J$ is unique up to this gauge of the $H$-free dynamics (and the weight $\alpha$).
5. **Symmetry.** $uu^\dagger$ is fixed by all $5040$ permutation matrices, and the $H$-free dynamics is covariant under all of them (every pair of axes lies on exactly one Fano line, so $\mathcal{D}_\Omega$ and $\mathcal{P}_\alpha$ treat all pairs alike — [Fano channel, Theorem 11.1](/docs/proofs/gap/fano-channel#s7-эквивариантность)). Of the 168 collineations acting as permutations only 21 (the group $7{:}3$) lie in $\Gamma_{\mathrm{oct}}$; the whole $\Gamma_{\mathrm{oct}}$ moves $uu^\dagger$ over its 64 sign rephasings $D\,uu^\dagger D$, $D = \mathrm{diag}(\pm1)$. The states whose $\Gamma_{\mathrm{oct}}$-orbit stays inside their gauge orbit are exactly $D\bigl((1-t)I/7 + t\,uu^\dagger\bigr)D^\dagger$, $t \in [-1/6, 1]$.
6. **One clause.** The following are equivalent: (Eq-V) below; $\rho_a = D\,uu^\dagger D^\dagger$ for a diagonal unitary $D$; the anchor has the largest integration of any state, $\Phi(\rho_a) = P_{\mathrm{coh}}/P_{\mathrm{diag}} = 6$; it is maximally coherent in the frame, $C_{\mathrm{rel}}(\rho_a) = S(\mathrm{diag}\,\rho_a) - S(\rho_a) = \log 7$; its coherent purity is $s = 6/7$. Neither half of (Eq-V) suffices alone: (Eq) leaves every anchor with uniform diagonal, and viability alone, over all constant anchors, does not pick $\varphi_J$ — anchors with non-uniform diagonal come arbitrarily close to the $H = 0$ rate floor of [T-336](/docs/core/dynamics/evolution#t-336), $1.25$–$1.27$ times below $\kappa_c(\alpha)$, and reach it only in the limit where their attractor tends to $\Phi = 1$. (Eq) is the chosen uniform atomic-readout constraint $\mathrm{diag}\,\rho_a=I/7$, not a consequence of terminality.
:::

*Proof.* (1) Covariance of $\varphi$ puts $\rho_a$ in the commutant $\mathbb{C}I$ (theorem above). $\mathcal{P}_\alpha \circ \varphi = k\,\mathcal{P}_\alpha^2 + R\,\mathcal{P}_\alpha(\rho_a)$ is covariant iff $\mathcal{P}_\alpha(\rho_a)$ is $\Gamma_{\mathrm{oct}}$-invariant, i.e. $\mathcal{P}_\alpha(\rho_a) = I/7$; $\mathcal{P}_\alpha$ keeps the diagonal and multiplies coherences by $c \neq 0$, so $\rho_a = I/7$. $\mathcal{P}_{\mathrm{base}} \circ \varphi = k\,\mathcal{P}_{\mathrm{base}} + R\,\mathrm{diag}\,\rho_a$: signs act trivially on diagonals and the permutation part is transitive on the axes, so covariance is $\mathrm{diag}\,\rho_a = I/7$. The diagonal of the stationarity equation is $\kappa g_V R\,(\mathrm{diag}\,\rho_a - \mathrm{diag}\,\Gamma) = 0$ ([T-335](/docs/core/dynamics/evolution#t-335)). (2) By T-335 the stationary states with $P > 2/7$ are $(1 - \eta)I/7 + \eta\rho_a$ with $P = 1/7 + \eta^2 s$, and every coherence obeys the same scalar equation; with $\xi = \eta t$ it is the equation $\kappa Q_t(\xi) = 2/3$ of the family, $Q_t(\xi) = (6\xi^2 - 1)\bigl[(t - c\xi)/(\xi(1 + 6\xi^2)) - (1 - c)\bigr]$. $Q_t$ grows strictly with $t$ at each $\xi > 1/\sqrt6$, so $\max Q_t$ grows and $\kappa_c = 2/(3\max Q_t)$ falls; the threshold $t > (2 - c)/\sqrt6$ is the one of the [living attractor theorem](/docs/core/dynamics/evolution#теорема-живой-аттрактор-в-окне), i.e. $s > (2-c)^2/7$. The upper edge $P \le 3/7$ and $\Phi = 7P - 1 \ge 1$ hold as there. (3) $s \le 6/7$ with equality iff $\rho_a$ is pure; a pure state $\psi\psi^\dagger$ with $|\psi_k|^2 = 1/7$ is $D\,uu^\dagger D^\dagger$. (4) Direct. (5) $u$ is fixed by every permutation matrix. The rest is a finite check (`test_frame_covariance_modulo_gauge_fixes_the_collineation_anchor`) plus the following argument. A Hermitian matrix with all off-diagonal moduli nonzero is fixed up to diagonal gauge by its diagonal, the moduli $|\rho_{ij}|$ and the triangle fluxes $\arg(\rho_{ij}\rho_{jk}\rho_{ki})$, and signs in $\Gamma_{\mathrm{oct}}$ do not change these. $\mathrm{GL}(3,2)$ is 2-transitive on points, so the diagonal and the moduli are constant; it is transitive on lines and on ordered non-collinear triples, and contains elements reversing the orientation of a triangle of each kind, so each kind carries one flux $f_L$ or $f_N$ in $\{0, \pi\}$. Four points containing a line bound a tetrahedron with one collinear and three non-collinear faces, so $f_L = f_N$ (enumeration of all $2^{15}$ gauge classes of signings of $K_7$ gives exactly the two patterns). Flux $0$ is $t > 0$, flux $\pi$ is $t \lt 0$; if some modulus vanishes all do, $t = 0$. (6) (Eq-V) $\Leftrightarrow$ $\rho_a = D\,uu^\dagger D^\dagger$ is items 1–3: uniform diagonal is (Eq), and among such anchors $\kappa_c(s)$ decreases strictly in $s \leq 6/7$, with equality only for a pure anchor. $\Phi = s/P_{\mathrm{diag}}$ with $s = P - P_{\mathrm{diag}} \leq 1 - P_{\mathrm{diag}}$ and $P_{\mathrm{diag}} \geq 1/7$, so $\Phi \leq 6$, with equality iff $P = 1$ and $P_{\mathrm{diag}} = 1/7$; $S(\mathrm{diag}\,\rho) \leq \log 7$ with equality iff the diagonal is uniform, and $S(\rho) \geq 0$ with equality iff $\rho$ is pure (T. Baumgratz, M. Cramer, M. B. Plenio, "Quantifying coherence", *Phys. Rev. Lett.* **113**, 140401 (2014)). Anchors with uniform diagonal need $\kappa > \kappa_c(\alpha)$ by items 2–3, so those approaching the floor have non-uniform diagonal; the ratios are $16.63/13.11$, $29.25/23.21$, $59.34/47.35$ at $\alpha = 0, 1/2, 1$ (`test_one_clause_principle_for_the_anchor_is_maximal_integration`). $\blacksquare$

**The remaining principle.** What the axioms, the frame decision and the theorems above leave is one principle [Pr], weaker than the two it replaces:

- **(Eq-V)** the self-model privileges no axis of the frame — its atomic reading is $\Gamma_{\mathrm{oct}}$-covariant — and among such self-models it is the most viable.

(Eq-V) gives $\varphi_J$ up to gauge by T-334; the former **(Col)** (covariance under the 168 collineations) now follows [T], with $S_7$ in place of the 168, and the former **(Pure)** (a pure anchor) is equivalent [T] to maximal viability once the first half of the principle — call it (Eq) — holds. The strict form of frame covariance — of $\varphi$ itself — is excluded by life (item 1), which is why the atomic reading is the strongest reading at which the frame decision [D-0910](/docs/proofs/categorical/uniqueness-theorem#g2-ригидность) can hold for an isolated living holon. With the gauge fixed,

$$
\varphi_J(\Gamma) = k\,\mathcal{P}_\alpha(\Gamma) + R\,uu^\dagger ,
$$

unique up to the Fano weight $\alpha$. With it an isolated holon at $H = 0$ has, for $\kappa > \kappa_c(\alpha)$, a single living attractor, which persists for small $H$ and lies in $\mathcal{V}_{\mathrm{full}}$: $P \in (2/7, 5/14)$, $\Phi \in (1, 3/2]$, uniform diagonal ([living attractor in the window](/docs/core/dynamics/evolution#теорема-живой-аттрактор-в-окне) [T]); its perturbations and the admissible range of $\kappa$ are given by [T-335 and T-336](/docs/core/dynamics/evolution#t-335). The price that stays is the phase reference: for the $H$-free holon the phases of $u$ are a gauge, but a Hamiltonian that is not diagonal in the frame makes the relative orientation of $D$ and $H$ physical. The attractor exists for every $D$ with the same bound on $\|H\|$ (T-334, item 4), so the reference is a free datum, not a condition of life. Whether a physical holon's self-model is $\varphi_{\mathrm{coh}}$, $\varphi_s$ or $\varphi_J$ is not decided by the axioms: $\varphi_J$ is the self-model fixed by (Eq-V) [Pr].

**One clause.** By item 6, (Eq-V) is equivalent [T] to a single condition on the anchor, stated in the corpus's own measure of integration:

- **(MaxΦ)** the anchor of the self-model is a state of maximal integration, $\Phi(\rho_a) = 6$ [Pr].

It mentions neither viability nor the frame group and yields both: an anchor of maximal integration has uniform diagonal, so it privileges no axis (item 1), and it is pure, so it is the most viable among such anchors (items 2–3). Routes tried to derive it, none sufficient: covariance of the anchor's gauge class under the symmetry group of the dynamics it regulates — Curie's principle for an isolated holon, with $S_7$ or with $\Gamma_{\mathrm{oct}}$ — gives the family $D\bigl((1-t)I/7 + t\,uu^\dagger\bigr)D^\dagger$ (item 5) but not $t = 1$; uniform atomic readout gives the atomic half, $\mathrm{diag}\,\rho_a=I/7$, as a premise and says nothing about purity; Brouwer's theorem gives fixed points, not anchors; Lawvere additionally requires its point-surjectivity hypothesis; viability alone does not pick $\varphi_J$ (item 6); the largest integration of the living attractor, rather than of the anchor, fails in a band — the attractor of a constant anchor at $H = 0$ depends only on $d = \sum_i(\rho_a)_{ii}^2$ and $s = P(\rho_a) - d$, its integration $\eta^2 s/d$ grows with $s$ at fixed $d$, so the maximiser is pure, but for $\kappa_c(\alpha) < \kappa < \kappa_* \approx 1.012\,\kappa_c(\alpha)$ a pure anchor with slightly non-uniform diagonal beats $uu^\dagger$ ($\alpha = 0$, $\kappa = 16.8$: $d = 1/7 + 10^{-4}$ gives $\Phi_{\mathrm{att}} = 1.25155$ against $1.25148$), above the band $uu^\dagger$ wins on the tested grid [H as a global statement], and below $\kappa_c$ only non-uniform anchors live, so there the principle contradicts (MaxΦ) ([premises, §7](/docs/reference/premises#максфи-и-вариационные-принципы); `test_anchor_principle_is_independent_and_attractor_integration_does_not_replace_it`). The two halves of (MaxΦ) are independent [T]: a pure anchor with non-uniform diagonal (amplitudes $1 \pm 0.3$, a sink at $\kappa = 50$, T-335) satisfies (Pure) and not (Eq), and $(1-t)I/7 + t\,uu^\dagger$ with $t = 0.9$ satisfies (Eq) and not (Pure) while holding a living sink in the window at $\alpha = \tfrac12$, $\kappa = 100$; so neither half follows from the other, and a derivation of (MaxΦ) has to supply both. (MaxΦ) is the smallest form of the principle found.

---
## Unified numerical statement {#единая-теорема-самонаблюдения}

For a **chosen** $\alpha$ and anchor law, the Fano/atomic formula defines a continuous state-preserving $M$ [D]; the frozen realization is CPTP [T]. The uniform-anchor version attenuates off-diagonal entries by $kc$ and retains their phase only when the output is nonzero. Its only fixed point is $I/7$. The distinct $M_s$ and $M_J$ laws have the separate dynamical results stated above. The (MaxΦ) premise selecting $M_J$ remains [Pr]. No derivation of $\alpha$ or the physical anchor follows from categorical support.

A stationary phase-offset formula for a coherence driven by a **fixed external target** cannot be reused after setting that target phase equal to the evolving input phase. That substitution changes the differential equation into phase-aligned damping. For uniform-anchor $M_{\mathrm{coh}}$, the regenerative contribution to an off-diagonal element is a real negative scalar times that element; it introduces no independent phase drive. The former universal stationary-Gap formula after this substitution is withdrawn [✗]. Stationary coherences for nonunital anchors must be solved from their actual feedback equation.

## Distinct constructions and the withdrawn links {#три-определения}

The categorical support reflector $L_G$, finite-step numerical $M$, and fixed-parameter replacement channel remain well-defined on their respective domains. Their unconditional equivalence and the variational links through $S+D$ are withdrawn. For full-rank input the latter functional is cross-entropy; its minimizing output is supported on the top eigenspace, generally different from the feedback targets above. The three-map table also distinguishes opposite conventions for the symbol $k$; every formula must declare which weight multiplies the current state and which multiplies the anchor.

## Connections

- [Typed mathematical kernel](/docs/reference/mathematical-kernel): state geometry, process category and topos realization.
- [Formalization of φ](/docs/proofs/categorical/formalization-phi): exact slice adjunction, frozen channels, conditional limits and derivative bounds.
- [Evolution](/docs/core/dynamics/evolution): full vector field and actual equilibrium stability.
- [Self-observation](/docs/consciousness/foundations/self-observation): canonical $R$ versus self-model mismatch $R_\varphi$.
- [Fano channel](/docs/proofs/gap/fano-channel): filter geometry and its symmetry restrictions.
- [FEP derivation](/docs/proofs/dynamics/fep-derivation): withdrawn variational identification.
