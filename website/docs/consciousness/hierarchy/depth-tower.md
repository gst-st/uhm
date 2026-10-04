---
sidebar_position: 5
title: "Depth Tower"
description: "Typed representation towers, independent predictive certificates and the limits of iteration scores"
---

# Depth Tower {#башня-глубины}

A representation tower and a self-model iteration are different constructions. Neither gives a biological depth merely by counting layers or iterations. This page follows the [typed mathematical kernel](/docs/reference/mathematical-kernel) and the [canonical hierarchy](./interiority-hierarchy): L2 requires $\mathsf{Cap}_2$; L3 additionally requires independent nonconstant metamodel predictions; L4 is a compatible all-order ideal.

:::warning Revision 2026-10-03
The former universal equivalence between SAD and L-levels, cognitive ceiling SAD_MAX = 3, and identification of every depth increase with an $A_4$ catastrophe are **withdrawn [✗]**. An optional score still has a ceiling of three by its definition; this is not a theorem limiting cognition. T-142's old cognitive/spectral identification needs these corrections propagated to its own proof.
:::

## 1. The problem {#проблема}

Canonical $R=1/(7P)$ is normalised proximity to $I/7$, not measured prediction accuracy. An implemented model and independent targets are extra inputs. The same $\Gamma$ can accompany different implemented models, and a model can have high fidelity to a constant target while doing no nontrivial metacognition.

## 2. Typed representations {#иерархия-представлений}

Declare spaces $X_k$, states $s_k\in X_k$, forgetting maps $\pi_k:X_{k+1}\to X_k$, and model maps $M_k:X_k\to X_k$. If $X_0$ is a coordinate chart of $\mathcal D(\mathbb C^7)$, state reconstruction must enforce positivity and trace one. The relative interior has real dimension 48; boundary strata and arbitrary neural representations are not automatically that chart.

The maps may be learned, but their domains, metrics and observation laws must be specified. Compression does not prove an optimal sufficient statistic for survival. A proposed information bottleneck additionally needs random variables, a task loss and a constraint; no universal learning optimum follows from seven coordinates alone.

## 3. Two meanings of depth {#sad}

**Certified depth [D/Pr].** For independently measured targets at each order, use the canonical $\mathsf{MetaCert}_k$ with error $e_k\le\varepsilon_k$ and response variation $v_k\ge a_k>2\varepsilon_k$. Define depth as the greatest **prefix** of passing certificates and compatibility tests, taking zero for an empty prefix. Missing data are unknown. This prevents a single isolated passing score from certifying every lower order.

**Iteration score [D].** One may instead count iterations for which a declared scalar exceeds a declared threshold. Report the channel, initial state, score, indexing and threshold. Such a count is an engineering diagnostic until an independent depth bridge is established.

### No SAD–L equivalence {#sad-l-эквивалентность}

A score determines L exactly only if the L-classification is constant on its fibres. Canonical $\mathsf{Cap}_2$ uses $P,R,\Phi,D_{\mathrm{diff}}$; a purity-only score omits integration and differentiation, and an iteration score omits the metamodel tests. There is no general SAD–L equivalence. A reconstruction score

$$
1-\|M_k(s_k)-s_k\|^2/\|s_k\|^2
$$

can be negative, is undefined at $s_k=0$, and depends on the chosen coordinates. It must not be substituted for canonical $R$.

### Powers and compatibility {#коммутативность}

For one self-map, $M^m\circ M^n=M^{m+n}$ is an iteration identity **[T]**. It does not imply commutativity of a heterogeneous tower. The equation

$$
\pi_kM_{k+1}=M_k\pi_k
$$

is a compatibility condition **[D]**, to be imposed or tested. It is not forced by state preservation or by CPTP contractivity.

### Correct spectral formula {#спектральная-формула-sad}

For a **fixed linear diagonalizable channel** $K$ with spectral projectors $\Pi_j$,

$$
K^n(\rho)=\sum_j\lambda_j^n\Pi_j(\rho).
$$

A general linear channel may require Jordan terms. A projection onto stationary modes is an asymptotic statement requiring decay of the other modes and absence of nontrivial peripheral oscillations; it is not the formula for every finite iterate. A state-dependent model is nonlinear and has no such global channel spectral formula merely by being state preserving.

For the bare Fano dephasing $D_{2/3}$ and nonzero initial off-diagonal norm,

$$
S_n:=\frac{\|\operatorname{offdiag}(D_{2/3}^n\rho)\|_F}{\|\operatorname{offdiag}\rho\|_F}=3^{-n}.
$$

For canonical $M(\rho)=(1-R(\rho))D_{2/3}\rho+R(\rho)I/7$,

$$
S_n=3^{-n}\prod_{j=0}^{n-1}(1-R(\rho_j))\le(2/7)^n.
$$

Neither expression is fidelity or reflective competence. The detection rule $S_n\ge\varepsilon$ gives the bare-channel bound $n\le\lfloor\log(1/\varepsilon)/\log3\rfloor$ **[T]**. It depends on a chosen detection threshold and is not universally three. If the initial off-diagonal norm is zero the ratio is undefined, rather than a depth certificate.

### What the former critical-purity arithmetic proves {#критическая-чистота-sad}

Explicitly **stipulate** the score

$$
s_{n-1}(P):=\frac{P}{2/7}\,3^{-(n-1)},\qquad s_{n-1}>1/(n+1).
$$

Then, by rearrangement,

$$
P>p_n:=\frac27\frac{3^{n-1}}{n+1}.
$$

For $n=1,2,3,4$, these numbers are $1/7,2/7,9/14,54/35$. Since $P\le1$, this **stipulated score** never reaches order four, and its maximum three is attained for $P>9/14$. This algebra is **[T conditional on the score definition]**. The prefactor $P/(2/7)$ can exceed one and is neither the normalised survival ratio nor canonical $R$. No Fano theorem identifies it with self-model accuracy.

Also $P>9/14$ implies $R<2/9<1/3$: the purported depth-three episode fails the canonical L2 gate. It cannot be L3 under the cumulative hierarchy. A chosen 3-truncation, a Jordan-algebra matrix-rank ceiling or a chosen perfect-code grammar does not independently prove a bound on cognitive recursion; each needs a faithful operational bridge. See corrected [T-217/T-218](/docs/proofs/categorical/fundamental-closures#t-218).

## 4. Biological correlates {#биологические-корреляты}

Assignments of bacteria, insects, mammals, humans or meditators to numerical depths are **[H]** and require species/task-specific probes and reconstruction. Layer count, neuron count and successful navigation alone do not measure the declared certificate. No universal human ceiling of three is established here.

## 5. Consistency and its interpretation

On a declared test domain define

$$
\Delta_k:=\sup_s d_k(\pi_kM_{k+1}(s),M_k\pi_k(s)).
$$

This is a compatibility error **[D]**. Translating it into dissociation, alexithymia or health is an empirical bridge **[H]**, not a diagnosis from a norm. Spectral radius alone is not a one-step operator norm for a nonnormal Jacobian; transient growth and long-term stability must be checked separately.

## 6. Morphological agnosticity {#агностичность}

Learning Enc/Dec and choosing representations through interaction are architectural proposals **[D/Pr]**. Starting from $I/7$ is an initial-state choice: it has canonical $R=1$, not zero, and is not a theorem of zero knowledge. Rates such as $1/7$ require units, a time scale and a dynamical balance. A seven-dimensional register does not universally minimise sample complexity; that depends on a statistical task and hypothesis class.

## 7. Depth dynamics {#динамика-глубины}

### Growth {#рост-башни}

A depth label can change when a prediction error crosses a threshold along a smooth trajectory. A bifurcation requires a separate dynamical degeneracy; $A_4$ additionally requires a scalar smooth reduction, fourth-order stationary degeneracy and a transverse three-parameter unfolding. Three named controls alone are insufficient. See [conditional catastrophe models](./swallowtail-transitions).

### Resource requirements {#энергетическая-стоимость}

If independently implemented orders each consume at least $c>0$ of a resource with total budget $B$, their number is at most $\lfloor B/c\rfloor$ **[T under these assumptions]**. Neither a linear nor a superlinear cost law follows from level count alone; shared computation and symbolic recursion must be considered.

#### Landauer calibration {#ландауэровская-калибровка}

For isothermal logically irreversible erasure of a declared classical memory with entropy decrease $\Delta H$ in nats, the reversible-limit heat lower bound is $k_BT\Delta H$ under the usual thermodynamic assumptions. Bit count must come from a memory/task model, not the ratio of Euclidean representation dimensions. $\operatorname{Tr}(\rho^*-\rho)=0$ cannot supply a positive energy budget. Source: [Landauer's original erasure analysis](https://doi.org/10.1147/rd.53.0183).

### Stress scheduling {#стресс-зависимый-режим}

Hot/warm/cold scheduling can be a declared engineering policy **[D]**. Numerical stress bands and forced depth collapse are not universal biological theorems. Clinical interpretation requires independently measured functional outcomes **[H]**.

### Social depth {#социальная-глубина}

A joint state lies in $\mathcal D(\mathbb C^{49})$, and an aggregate requires a map to the seven-dimensional model. Correlation or local viability alone does not imply additive predictive depth. Test partner-model predictions against independent targets and common-input controls. Phase alignment is not an empathy measurement; topology of $G_2/T^2$ does not give a universal social energy barrier. See [composite systems](/docs/core/dynamics/composite-systems).

### Reinterpretation of the “licensed excursion” {#лицензированная-экскурсия}

A simulated trajectory crossing $P=9/14$ verifies an implementation of the stipulated score above. It does not measure an episode of human reflection, meditation, altered qualia or clinical safety. Its higher purity actually closes canonical access $R\ge1/3$. Report the target, dynamics, time units, score and stability calculation; phenomenal interpretation remains **[H/I]**.

## 8. Architecture and validation {#архитектура-agi}

Design a declared state model, data encoder, self-model and metamodel, independent test targets, compatibility maps and resource accounting. An architecture does not receive an AGI or phenomenal label from passing a static scalar gate.

### Implementation status {#статус-реализации}

Code tests can verify score arithmetic, PSD preservation, iterative decay or diagram errors. They do not validate biological depth or categorical-to-cognitive identification. Operational depth requires held-out predictions; all-order compatibility requires a mathematical certificate rather than three iterations.

## 9. Related documents {#связанные-документы}

- [Typed kernel](/docs/reference/mathematical-kernel)
- [Canonical hierarchy](./interiority-hierarchy)
- [Conditional transition models](./swallowtail-transitions)
- [Self-observation](/docs/consciousness/foundations/self-observation)
- [Formal iteration proofs](/docs/proofs/consciousness/interiority-hierarchy#теорема-4-3)
