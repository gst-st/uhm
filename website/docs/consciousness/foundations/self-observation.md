---
sidebar_position: 3
title: Self-Observation
description: Consciousness as self-observation of Γ
slug: /consciousness/foundations/self-observation
---

# Self-Observation and Capability

The chapter distinguishes three typed constructions: a **logical support reflector**, a **numerical state model**, and an **operational test of metamodel predictions**. The [mathematical kernel](/docs/reference/mathematical-kernel) fixes their types. Calling a represented inner aspect experience is an interpretive bridge **[I]**; neither contraction nor state similarity proves that identification.

## Self-Modelling Operator φ {#оператор-самомоделирования-φ}

In an $\infty$-topos $\mathcal E$, with a fixed object $G$, the support reflector is

$$
\operatorname{im}_G:\mathcal E_{/G}\rightleftarrows\operatorname{Sub}(G):j,
$$

left adjoint to inclusion, taking a map to its $(-1)$-truncated image **[T]**. It is not a density-matrix channel and has no Kraus representation by this definition.

A numerical model is separately specified as $M:D_7\to D_7$, where $D_7=\mathcal D(\mathbb C^7)$. A fixed **linear** CPTP map $K:M_7(\mathbb C)\to M_7(\mathbb C)$ admits

$$
K(X)=\sum_aK_aXK_a^\dagger,\qquad\sum_aK_a^\dagger K_a=I.
$$

This preserves states, including when extended by an identity channel. It models a state transformation, not simultaneous production of independent copies of an unknown state. Interpreting it as an internal self-model requires an observation protocol **[D/H]**. A nonlinear state-selected map is not automatically a quantum channel.

### Frozen replacement channel {#физическая-реализация-phi}

#### Conditional realisation theorem [T] {#теорема-физическая-реализация-phi}

For **fixed** $\sigma\in D_7$ and $k\in[0,1]$, define

$$
T_{k,\sigma}(X)=(1-k)X+k\operatorname{Tr}(X)\sigma.
$$

This is CPTP. Indeed, if $\sigma=\sum_a p_a|a\rangle\langle a|$, the replacement part has Kraus operators $\sqrt{p_a}|a\rangle\langle b|$; adding $\sqrt{1-k}I$ and scaling those operators by $\sqrt k$ gives completeness. On trace-one states, the formula reduces to $(1-k)\rho+k\sigma$.

If $k=k(\rho)$ or $\sigma=\sigma(\rho)$, this proof applies only with that input's parameters frozen. It does **not** prove that $\rho\mapsto T_{k(\rho),\sigma(\rho)}(\rho)$ is linear, CPTP, or contractive. A logical image does not select a unique numerical anchor without an additional bridge.

For a local fixed channel $K_A$ and joint $\rho_{AB}$,

$$
\operatorname{Tr}_A[(K_A\otimes\mathrm{id}_B)(\rho_{AB})]=\rho_B
$$

**[T]**. Proof: the adjoint fixes $I_A$, so every expectation of $I_A\otimes B$ is unchanged. Selective conditioning and nonlinear joint dynamics require their own no-signalling analysis.

#### Fixed point of the frozen channel [T] {#неподвижная-точка-кк4}

For $k>0$, $T_{k,\sigma}(\rho)=\rho$ iff $\rho=\sigma$. For $k=0$, every state is fixed. This conclusion is about the fixed channel, not all numerical self-models.

#### Attractor hierarchy {#иерархия-аттракторов}

| Object | Exact role |
|---|---|
| $I/7$ | Chosen reference for canonical $R$; purity $1/7$ |
| Fixed $\sigma$ | Unique fixed state of $T_{k,\sigma}$ for $k>0$ |
| $M$-fixed states | Solve $M(\rho)=\rho$ for the specified map |
| Stationary states of a flow | Solve the actual vector-field equation; their stability requires its Jacobian/basin |

A state different from $I/7$ has $P>1/7$ **[T]**, by the HS identity below. This does not establish the existence of such an attractor. The canonical numerical $\varphi_{\mathrm{coh}}$ with anchor $I/7$ has that centre as its fixed state; alternative anchors and maps have separately stated assumptions. See [the numerical formalisation](/docs/proofs/categorical/formalization-phi).

#### Coupling convention for k [D] {#теорема-k-из-r}

The rule $k(\rho):=1-R(\rho)=1-1/(7P)$ is a **chosen state-dependent coupling**. It lies in $[0,6/7]$. The replacement-channel formula alone does not derive it, and uniqueness of a logical reflector does not force it. Other choices of $k$ give equally valid frozen channels.

At $I/7$, $R=1$ and $k=0$; at a pure state, $R=1/7$ and $k=6/7$. These are mathematical proximity values, not levels of self-knowledge.

## Conditional Fixed-Point Results {#теорема-о-неподвижной-точке}

For fixed $\sigma$ and fixed $0<k\le1$,

$$
T_{k,\sigma}^n(\rho)=\sigma+(1-k)^n(\rho-\sigma),\qquad
\|T_{k,\sigma}\rho-T_{k,\sigma}\eta\|=(1-k)\|\rho-\eta\|
$$

in any norm on the trace-one affine hull **[T]**. The state space is complete, so contraction gives the unique fixed point and convergence. A CPTP map need not be a strict contraction: identity and unitary channels are counterexamples. State-dependent parameters invalidate this constant-factor calculation unless separately controlled.

### Closure and phenomenality {#самореферентная-замкнутость}

A fixed-point equation expresses stability of a specified model. The identity fixes every state, including a pure basis state with $\Phi=0$. The replacement channel anchored at $I/7$ converges to a state failing $\mathsf{Cap}_2$. Hence a fixed point, convergence or “self-reference” cannot by themselves certify L2, higher-order knowledge or experience. Lawvere's fixed-point theorem also requires its actual categorical hypotheses, not merely the existence of a self-map.

## Canonical Reflection Coordinate R {#мера-рефлексии-r}

Define $P=\operatorname{Tr}\rho^2$ and

$$
R:=1-\frac{\|\rho-I/7\|_F^2}{P}.
$$

This definition uses a fixed reference and is independent of $M$. Calling $I/7$ a thermodynamic equilibrium needs actual dynamics; the definition itself only singles out the maximally mixed state.

### Algebraic identity [T] {#алгебраическая-эквивалентность-r}

Write $\rho=I/7+\Delta$, $\operatorname{Tr}\Delta=0$. HS orthogonality gives

$$
P=\frac17+\|\Delta\|_F^2,\qquad R=\frac1{7P},\qquad \frac17\le R\le1.
$$

Thus $R$ is a decreasing reparameterisation of $P$, invariant under every unitary conjugation; it carries no independent information about model accuracy. $R=0$ is impossible. $R=1$ occurs at $I/7$, where $\Phi=0$, not at a maximally capable self-knower.

### Distinct diagnostics {#формы-r}

| Quantity | Definition | Interpretation/status |
|---|---|---|
| Canonical $R$ | $1/(7P)$ | HS proximity coordinate [D/T] |
| Reconstruction score $R_M$ (also written $R_\varphi$) | $1-\|\rho-M(\rho)\|_F^2/P$ | Specified-map error score [D]; can be negative |
| Iteration fidelity $F_n$ | $F(M^{n-1}\rho,M^n\rho)$ | State similarity [D], $0\le F_n\le1$ |
| Forecast skill $A$ | $1-\sum_t(y_t-\widehat y_t)^2/\sum_t(y_t-\bar y)^2$ | Centred empirical score [D]; can be negative, undefined at zero variance |

For a fixed replacement map, $R_M=1-k^2\|\rho-\sigma\|_F^2/P$. If $\sigma=I/7$, this is $1-k^2(1-R)$; substituting the convention $k=1-R$ gives $1-(1-R)^3$. This is a statement about this **particular** map. For $\varphi_{\mathrm{coh}}$ including Fano dephasing, the expression is different; use its defined formula. No universal closed relation with $R$ exists for arbitrary $M$.

The cutoff $R\ge1/3$ is a selected component of $\mathsf{Cap}_2$ **[D]**. Its equivalence to $P\le3/7$ is exact **[T]**. Counting three generator terms does not prove that $R$ is a Bayesian classification accuracy: that would require a labelled task, priors, likelihoods and a calibration connecting the score to decisions.

#### Centred forecast skill {#центрирование-a-phi}

A forecast of the sample mean gives $A=0$ when the denominator is nonzero; a perfect forecast gives $A=1$; worse forecasts may have $A<0$. For illustrative deterministic predictions $\widehat y_t=\bar y+w(y_t-\bar y)$, one gets exactly $A=1-(1-w)^2$. Dividing by $\sum y_t^2$ instead can reward predicting a nonzero baseline. For a prospective task, estimate the baseline on training data and evaluate held-out errors; report missing/zero-variance data. A chosen minimum of five matched days is an instrument rule **[D]**, not a mathematical identifiability theorem. A diary forecast is not automatically a measurement of a density-matrix self-model.

#### Whole-state versus diagonal reconstruction {#r-phi-по-связкам}

Let $\delta=\rho-M(\rho)$. Then

$$
\|\delta\|_F^2=\sum_i|\delta_{ii}|^2+\sum_{i\ne j}|\delta_{ij}|^2.
$$

A diagonal-only test misses the second term. With $Q=\sum_i\rho_{ii}^2$, the diagonal share of state HS mass is $Q/P=1/(1+\Phi)$ and the off-diagonal share is $\Phi/(1+\Phi)$ **[T]**. Report the measured component and its denominator; this identity alone does not validate a questionnaire-to-matrix bridge.

If $M$ is differentiable along a trajectory, the exact derivative is

$$
\dot R_M=(1-R_M)\frac{\dot P}{P}-\frac2P\operatorname{Re}\langle\rho-M\rho,(\mathrm{Id}-DM)_\rho[\dot\rho]\rangle_F.
$$

State dependence of model parameters belongs in $DM$. Fixed-parameter CPTP structure does not eliminate those terms.

## Higher-Order Iteration Diagnostics {#рефлексия-высших-порядков-rn}

Use a specified numerical self-map $M:\mathcal D(\mathbb C^7)\to\mathcal D(\mathbb C^7)$; the logical support reflector is a different typed construction. Define $\rho_n=M^n(\Gamma)$ and the squared-fidelity diagnostic

$$
F_n:=F(\rho_{n-1},\rho_n),\qquad
F(\rho,\sigma)=\left[\operatorname{Tr}\sqrt{\sqrt\rho\,\sigma\sqrt\rho}\right]^2.
$$

The root fidelity is $f=\sqrt F$, and $d_B^2=2(1-f)$. $F_n$ is a similarity of consecutive iterates **[D]**, not independently measured accuracy of a model of a model. It is distinct from canonical $R=1/(7P)$ and the HS reconstruction score $R_M$.

**Conditional monotonicity [T].** For a **fixed linear CPTP channel** $K$, fidelity data processing gives $F(K\rho,K\sigma)\ge F(\rho,\sigma)$, hence $F_{n+1}\ge F_n$. See [Watrous, Theorem 3.27](https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf). The inequality need not be strict; a unitary preserves fidelity. A nonlinear state-selected map does not automatically satisfy this channel theorem.

**Conditional convergence [T].** If $\rho_n\to\rho_*$, continuity of fidelity gives $F_n\to1$. At a fixed point, $F_n=1$ from the start; the identity channel gives this for every state. Canonical $\varphi_{\mathrm{coh}}$ with anchor $I/7$ converges to $I/7$, whose capability gate fails. Thus convergence to high similarity cannot certify cognitive depth or phenomenal access.

The former universal inequality connecting $F_1$ to canonical $R$ via Fuchs–van de Graaf is **withdrawn [✗]**: the measures compare different pairs. A pure state with $M=\mathrm{id}$ has $F_1=1$ and $R=1/7$, directly refuting the displayed lower bound on $\sqrt R$. The valid inequalities for the **same** pair are

$$
1-\sqrt F\le\tfrac12\|\rho-\sigma\|_1\le\sqrt{1-F}.
$$

They do not identify canonical proximity to $I/7$ with model fidelity. Source: [Fuchs–van de Graaf (1997)](https://arxiv.org/abs/quant-ph/9712042).

No universal sequence $1/(n+1)$ or $1/(n+2)$ follows from counting generator terms or categorical cells. One may declare calibrated diagnostic thresholds **[D]**; the [canonical hierarchy](/docs/consciousness/hierarchy/interiority-hierarchy) instead tests nonconstant predictions against independent metamodel targets. L3 inherits L2 and adds $\mathsf{MetaCert}_2$; L4 requires compatible certificates at every higher order. Their biological/phenomenal interpretation remains a separate bridge.

Finite-iterate spectral formulas apply to a specified linear channel, with eigenvalue powers and possible Jordan terms. The stationary projection of a relaxing semigroup is an asymptotic construction, not every $M^n$. A support reflector or generic nonlinear model has no channel spectrum simply by being called $\varphi$.

## Retro-completion of a process category {#ретро-пополнение-времени}

For a specified map $M$, the forward-orbit category has arrows labelled by $n\in\mathbb N_0$ with $M^n\rho=\sigma$; composition adds labels. Its nerve is a Kan complex iff this ordinary category is a groupoid **[T]**. A noninvertible positive-time arrow therefore prevents the nerve itself from being Kan. The singular complex of its geometric realisation is Kan regardless of this directed obstruction, as explained in [T-218](/docs/proofs/categorical/fundamental-closures#t-218).

### Limits of the retrospection bridge {#теорема-кандидат-r-полнота}

The one-object monoid category $\mathbb N_0$ admits group completion to $\mathbb Z$; the latter is a groupoid with Kan nerve **[T]**. Extending a particular forward state action to a $\mathbb Z$-action requires invertibility; merely storing a past state does not supply a two-sided inverse to a dissipative channel. Formal localisation can add inverse arrows, but their physical implementation is an extra bridge **[D/H]**. A refusal count on a selected finite grid depends on its sampling measure and is not a universal proportion of impossible thoughts. Canonical $R$ does not determine group completion, horn fillers or memory access.

## Interiority Hierarchy

The cumulative predicates follow the [canonical typed definition](/docs/consciousness/hierarchy/interiority-hierarchy), not an iteration-fidelity threshold.

| Capability | Required data and test |
|---|---|
| L0 | Valid state; calling an inner aspect interiority is [I] |
| L1 | Declared proxy $\mathrm{Coh}_E>0$, or normalised extension $\rho_E$ with rank greater than one |
| L2 | $\mathsf{Cap}_2=(P>2/7)\land(R\ge1/3)\land(\Phi\ge1)\land(D_{\mathrm{diff}}\ge2)$ |
| L3 | L2 plus an independent nonconstant metamodel-prediction certificate |
| L4 | L3 plus compatible nontrivial certificates at all higher orders |

A named basis axis is not a tensor subsystem. Extension entropy needs a specified lift/factorisation or conditioned block. The 7D proxy $D^{7D}=1+6\mathrm{Coh}_E$ is separately stipulated, not equal to every extension entropy. Unknown data are reported as unknown rather than supplied by a self-map iteration.

The old $K=3+1$ derivation of the universal fidelity threshold $1/4$, fixed-point criterion for L4, L3 retention-time formula and stable L4 clause $P>6/7$ are **withdrawn [✗]**. The last clause contradicts L2's inherited $P\le3/7$. Stability needs the specified flow, basin, Jacobian and noise/escape conditions; a level label alone does not give it.

A [depth-tower score](/docs/consciousness/hierarchy/depth-tower) may have a ceiling of three under its own arithmetic definition. It is not equivalent to L3 or a universal bound on self-awareness. Predictions and biological assignments require independent calibration **[Pr/H]**. Passing the definitions does not mathematically prove consciousness; the phenomenal bridge is **[I/H]**.

## Conditional Grounding Monotonicity {#grounding-монотонность}

Let $L(w)\ge0$ be a specified differentiable loss with an $L_g$-Lipschitz gradient, and define $G(w)=1-L(w)/L_{\max}$ with fixed $L_{\max}>0$ **[D]**. Gradient descent $w'=w-\eta\nabla L(w)$ satisfies

$$
L(w')\le L(w)-\eta(1-L_g\eta/2)\|\nabla L(w)\|^2
$$

for $0<\eta<2/L_g$ **[T]**. Thus $G$ is nondecreasing, strictly increasing only when the gradient is nonzero. A positive loss can have zero gradient, and sensorimotor input may change the loss between steps. CPTP structure alone guarantees neither smoothness in weights, nonzero gradients nor monotone learning. Identifying $G$ with semantic grounding requires an independent behavioural test **[H]**. The former unconditional C23 statement is restricted to these hypotheses.

## Integration–Reflection Summary C {#мера-сознательности-c}

Set $Q=\sum_i\rho_{ii}^2$ and $\Phi=(P-Q)/Q$ in the declared frame. Define

$$
C:=\Phi R=\frac1{7Q}-R\qquad\text{[D/T]}.
$$

Since $Q\ge1/7$, one obtains $0\le\Phi\le7P-1$ and $0\le C\le1-R\le6/7$. Under $\mathsf{Cap}_2$, necessarily $P\in(2/7,3/7]$ and $1/3\le C\le2/3$ **[T]**. Thus $C\ge1/3$ is a necessary scalar consequence of the chosen gate, **not sufficient**: a uniform real pure state has $C=6/7$ and fails $R\ge1/3$.

The complete gate remains

$$
\mathsf{Cap}_2=(P>2/7)\land(R\ge1/3)\land(\Phi\ge1)\land(D_{\mathrm{diff}}\ge2).
$$

The entropy-derived $D_{\mathrm{diff}}=e^{S(\rho_E)}$ requires a specified normalised experiential extension. The 7D score $D^{7D}=1+6\mathrm{Coh}_E$ is separately defined, not an entropy identity. Clinical or diary values cannot be substituted for either without a validated measurement bridge. The old waking example $\Phi=3,R=0.4$ violates $\Phi\le7P-1=1.5$, and the old sleeping $R=0.1$ violates $R\ge1/7$; both are withdrawn.

## Operational use

An implementation must declare the state estimator, frame, numerical map, differentiation construction and metamodel test. Compute canonical $R$ from $P$, retain all four gate inequalities, and record missing quantities as unknown. In code the numerical gate is `P > 2/7 and R >= 1/3 and Phi >= 1 and D_diff >= 2`; additional level predicates remain cumulative.

Metacognition and introspection are hypotheses about independently measured task performance. They are not automatically synonyms for $R$, $\Phi$ or a fixed point. Static scalar values alone do not establish alexithymia, dissociation, sleep, meditation or a clinical diagnosis. Any such assignment needs labelled observations and out-of-sample validation **[H]**.

## CRL — a proposed reflexive language {#crl-теоретическое-основание}

A proposed compile map sends a declared symbolic instruction to a state perturbation $\delta\rho$ with $\delta\rho=\delta\rho^\dagger$ and $\operatorname{Tr}\delta\rho=0$ **[D]**. This is a tangent vector in the trace-one affine hull, not an endomorphism of the state space. The update $\rho+\epsilon\delta\rho$ also needs positivity; an implemented CPTP action or a verified state-preserving update is a safer executable type.

The engineering cycle is `estimate state → select instruction → compile action → apply → measure`. To claim reflective capability, evaluate nonconstant predictions against independent targets. A rule enabling CRL only after $\mathsf{Cap}_2$ is a design choice **[D]**, not a theorem that symbols or self-modification are impossible at lower scores. The phase diagram, code geometry and $2/7$ cutoff alone do not prove semantic grounding or therapeutic efficacy.

The valid mathematical backbone is the HS identity, fixed-parameter channel theorem, conditional contraction and same-pair fidelity estimates. The capability hierarchy adds independently testable operational certificates; its phenomenal reading remains a separate bridge.

Related: [typed kernel](/docs/reference/mathematical-kernel), [numerical φ formalisation](/docs/proofs/categorical/formalization-phi), [canonical hierarchy](/docs/consciousness/hierarchy/interiority-hierarchy), [depth tower](/docs/consciousness/hierarchy/depth-tower), [measurement identifiability](/docs/applied/research/reconstruction-identifiability).
