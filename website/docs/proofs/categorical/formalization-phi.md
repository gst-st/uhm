---
slug: /proofs/categorical/formalization-phi
sidebar_position: 2
title: "Typed formalization of self-modelling φ"
format: md
---

# Typed Formalization of Self-Modelling φ

:::info Canonical definitions — revised 2026-10-03
This page distinguishes logical support, a numerical self-model, and a dynamical limit. They have different domains and universal properties. The symbol $\varphi$ in an evolution equation denotes the numerical map $M$ defined below; it never denotes the support reflector without an explicitly specified realization bridge.
:::

## Types and definitions {#сводная-таблица-определений}

| Object | Type | Proven property |
|---|---|---|
| Logical support $L_G$ | $\mathcal E_{/G}\to\mathrm{Sub}_{\mathcal E}(G)$ | Left adjoint to inclusion **in the slice**, idempotent up to equivalence [T] |
| Numerical self-model $M$ (also $\varphi$) | $\mathcal D(\mathcal H)\to\mathcal D(\mathcal H)$ | A specified state-preserving map [D]; continuity gives existence of a fixed point [T] |
| Frozen realization $\mathcal C_\lambda$ | $\mathcal L(\mathcal H)\to\mathcal L(\mathcal H)$ | Linear CPTP channel for fixed classical parameters $\lambda$ [T] |
| Basin limit $r$ | $D\to\mathrm{Fix}(F)$ | Retraction if every trajectory in the invariant domain $D$ converges [T at convergence] |
| Linear reset $\Pi_0$ | $X\mapsto\mathrm{Tr}(X)\rho_0$ | Asymptotic projector of a relaxing linear quantum Markov semigroup [T at relaxation] |

## Stratification without circularity {#стратификация-определений}

First specify $\mathcal H$, a predictive channel, an anchor law and a feedback weight. Then evaluate $M(\Gamma)$ on the current state. Next define a vector field using $M$, and only after that study its equilibria and limits. The reference $I/7$ and $R=1/(7P)$, $P=\mathrm{Tr}\,\Gamma^2$, can be defined directly, independently of a nonlinear attractor. Primitivity of a specified unital linear generator can establish that $I/7$ is its stationary state; it does not determine the nonlinear feedback anchor or its rate.

The categorical construction starts with an $\infty$-topos $\mathcal E$ and an object $G\in\mathcal E$. A numerical density matrix $\Gamma$ and a topos object $G$ are not identified implicitly. Interpreting $G$ as an internal state object requires separate realization data.

## Logical support in the slice {#категориальное-определение-φ}

### Correct adjunction {#φ-как-левый-сопряжённый-к-включению-подобъектов}

Let $\mathcal E$ be an $\infty$-topos and $G\in\mathcal E$. Its slice $\mathcal E_{/G}$ is an $\infty$-topos. A subobject $S\hookrightarrow G$ is a $(-1)$-truncated object of this slice. The full subcategory of these objects, denoted $\mathrm{Sub}_{\mathcal E}(G)$, is equivalent to the poset of subobjects. Define

$$
L_G:=\tau_{\leq-1}^{\mathcal E_{/G}},\qquad
L_G\dashv i_G:\mathrm{Sub}_{\mathcal E}(G)\hookrightarrow\mathcal E_{/G}.
$$

For $p:X\to G$, factor $p$ as

$$
X\xrightarrow{e_p}\operatorname{im}(p)\xrightarrow{m_p}G,
$$

where $e_p$ is an effective epimorphism and $m_p$ a monomorphism. Then $L_G(p)=m_p$. This is the effective-epimorphism/monomorphism factorization, unique up to a contractible space of compatible choices. See Lurie, [*Higher Topos Theory*](https://arxiv.org/abs/math/0608040), §§5.5.6, 6.2.3, and the slice-truncation construction.

**Theorem (Support reflector) [T].** For every $p:X\to G$ and $m:S\hookrightarrow G$ there is a natural equivalence of mapping spaces

$$
\operatorname{Map}_{\mathrm{Sub}_{\mathcal E}(G)}(L_Gp,m)
\simeq\operatorname{Map}_{\mathcal E_{/G}}(p,i_Gm).
$$

*Proof.* A map over $G$ from $X$ to $S$ exists exactly when $p$ factors through $m$. Effective epimorphisms are left orthogonal to monomorphisms, so such a factorization descends uniquely up to contractible choice through $e_p$ to a factorization of $m_p$ through $m$. Both mapping spaces are therefore empty if $\operatorname{im}(p)\nleq S$ and contractible otherwise. This equivalence is natural in both arguments. $\square$

**Consequences [T].** $L_Gi_G\simeq\mathrm{id}$, so the endofunctor $i_GL_G$ is idempotent up to coherent equivalence. $\operatorname{im}(p)$ is the *least* subobject of $G$ through which $p$ factors. Image factorization is stable under pullback, hence for $f:G'\to G$, $f^*L_Gp\simeq L_{G'}f^*p$.

### What the universal property means {#φ-как-наилучшее-приближение}

The reflector forgets witness multiplicity and higher homotopy while retaining logical support over a specified base. It gives a least support in the order of subobjects. It does not minimize Bures distance, predict a density matrix, choose a rate, or select a pure or mixed anchor. Applying it to the identity $G\to G$ returns that identity; this is not a numerical attractor calculation. Restricted classes of "admissible subobjects" need their own closure/reflection hypothesis; internal logical consistency alone does not supply one.

### Withdrawal of the untyped equivalence {#эквивалентность-определений-phi}

:::warning Withdrawn 2026-10-03 [✗]: categorical ⇔ dynamical ⇔ idempotent
The former inclusion $\mathrm{Sub}(G)\hookrightarrow\mathcal E$ cannot have the stated left adjoint for an arbitrary $G$. Its terminal object is $G\hookrightarrow G$; a right adjoint preserves terminal objects, forcing $G$ to be terminal in $\mathcal E$. Equivalently, the former Hom formula with $S=G$ forces $\operatorname{Map}_{\mathcal E}(X,G)\simeq *$ for every $X$. The corrected adjunction lives in $\mathcal E_{/G}$, whose terminal object is $G\to G$. [Right adjoints preserve limits — Kerodon](https://kerodon.net/tag/02KE).

Idempotence of a state map is insufficient for an adjunction: it provides no functor on morphisms, unit, or universal mapping-space equivalence. Even an idempotent functor need not be a reflector. In a discrete category with objects $x,y$, the constant functor to $y$ is idempotent, but the inclusion of $\{y\}$ has no such left adjoint because $\operatorname{Hom}(x,y)=\varnothing$ while $\operatorname{Hom}(y,y)=\{\mathrm{id}\}$. Conversely, finite-step $M_{\mathrm{coh}}$ is not idempotent. There is no proven equivalence between $L_G$, $M$, and a dynamical limit.
:::

Contractibility of maps to a terminal object gives uniqueness up to coherent homotopy. It supplies no physical multiplicity of decisions or theorem about free will.

<a id="типы-самомоделирования"></a>

## Numerical self-models {#2-формальное-определение-φ}

### Domain

$$
\mathcal D(\mathcal H)=\{\rho=\rho^\dagger\succeq0:\mathrm{Tr}\rho=1\}.
$$

It is a compact convex subset of the real affine space of Hermitian trace-one matrices. Its interior has tangent space $\mathrm{Herm}_0(\mathcal H)=\{V=V^\dagger:\mathrm{Tr}V=0\}$. At the boundary only admissible directions yield state paths; differential statements there require an extension to an affine neighborhood.

### Reduction requires a tensor product

A reduced model $\mathrm{Tr}_{\bar M}\rho$ requires an explicit factorization $\mathcal H_{\mathrm{ext}}=\mathcal H_M\otimes\mathcal H_{\bar M}$. A linear subspace $M\subset\mathcal H$ is not a tensor factor, and set subtraction $\mathcal H\setminus M$ is not a model environment. Returning to $\mathcal D(\mathcal H)$ requires a specified preparation/decoding map. In particular $\mathbb C^7$ has no nontrivial tensor factorization into smaller finite-dimensional systems.

### Frozen channels and adaptive maps {#23-определение-через-предиктивную-модель-основное-определение}

A CPTP map is **linear on operators**. For fixed Kraus operators,

$$
\mathcal P(X)=\sum_a K_aXK_a^\dagger,\qquad\sum_aK_a^\dagger K_a=I.
$$

For fixed $0\leq k<1$ and $\sigma\in\mathcal D(\mathcal H)$ define the channel

$$
\mathcal C_{k,\sigma}(X)=k\mathcal P(X)+(1-k)\mathrm{Tr}(X)\sigma.
$$

Writing $\sigma=\sum_i s_i|u_i\rangle\langle u_i|$, the reset part has Kraus operators $\sqrt{(1-k)s_i}|u_i\rangle\langle j|$, alongside $\sqrt{k}K_a$. Their squared adjoints sum to $I$. Thus $\mathcal C_{k,\sigma}$ is CPTP [T]. On states the trace factor is one. This realizes a *given* target; it does not derive that target from $L_G$. [Watrous, *The Theory of Quantum Information*, chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.double.2.pdf).

For a state-dependent parameter law $\lambda(\Gamma)$ set

$$
M(\Gamma)=\mathcal C_{\lambda(\Gamma)}(\Gamma).
$$

Each frozen $\mathcal C_\lambda$ is CPTP, while $M$ generally is nonlinear, non-affine on mixtures, and is **not one CPTP channel**. Frozen channel contractivity cannot be applied to two states with different parameters. Physical execution of an adaptive law requires a specified classical readout/controller or a further ontological postulate; exact access to an unknown input density matrix is not supplied by the Kraus representation.

A same-system channel is not a cloning map. No-cloning concerns producing two faithful copies of arbitrary unknown states, including CPTP implementations; it is not evaded merely by using a nonunitary map. CPTP maps can increase purity (a pure reset is an example); Hilbert–Schmidt purity is non-increasing for **unital** channels, not arbitrary ones.

### Fixed-parameter contraction {#25-сжимающий-оператор-самомоделирования}

**Lemma 2.1 [T].** For fixed $k,\sigma,\mathcal P$,

$$
\|\mathcal C_{k,\sigma}(\rho)-\mathcal C_{k,\sigma}(\eta)\|_1
\leq k\|\rho-\eta\|_1.
$$

*Proof.* The reset cancels in differences; trace-norm contractivity of a CPTP map on Hermitian differences gives the bound. If $\mathcal P$ is also unital on the same matrix algebra, the Frobenius bound with factor $k$ follows from Kadison–Schwarz and trace preservation. General nonunital channels need not contract the Frobenius norm. $\square$

### Canonical families and their status {#26-каноническая-форма-φ-для-угм}

Let $\Delta(\Gamma)=\operatorname{diag}\Gamma$ and

$$
\mathcal P_{\mathrm{Fano}}=\tfrac13\sum_{p=1}^7\Pi_p(\cdot)\Pi_p,
\quad\mathcal P_\alpha=\alpha\Delta+(1-\alpha)\mathcal P_{\mathrm{Fano}},\quad0\leq\alpha\leq1.
$$

The diagonal is fixed and off-diagonal entries are multiplied by $c=(1-\alpha)/3$. The equally weighted Fano channel therefore equals $\tfrac13\mathrm{id}+\tfrac23\Delta$; pairwise damping alone does not reveal the incidence structure. Define $R=1/(7P)$, $k=1-R$. These weights and the following anchors are explicit specifications [D], with properties proved conditionally on them:

$$
M_{\mathrm{coh}}(\Gamma)=k\mathcal P_\alpha(\Gamma)+R I/7,
$$

$$
M_s(\Gamma)=k\mathcal P_\alpha(\Gamma)+R\Gamma^2/P,
\qquad M_J(\Gamma)=k\mathcal P_\alpha(\Gamma)+Ruu^\dagger,
\quad u=(1,\ldots,1)/\sqrt7.
$$

Each is continuous, state-preserving, and generally nonlinear. The frozen realization is the channel above with the current weight and anchor held fixed. The spectral-sharpening law of $M_s$ is not a state-independent Lüders instrument: the effect itself depends on $\Gamma$, and the normalized update is conditional.

$M_{\mathrm{coh}}$ has the unique fixed point $I/7$ and
$\|M_{\mathrm{coh}}(\Gamma)-I/7\|_F\leq(6/7)\|\Gamma-I/7\|_F$.
This proves convergence of its iterates to $I/7$, but not contraction of arbitrary pairs: its Lipschitz constant is $9/8$. The full regenerative dynamics using this unital target cannot sustain an isolated viable holon. The separate $M_s$ and $M_J$ constructions and their actual attractors are described in [φ operator](/docs/core/operators/phi-operator#phi-s) and [evolution](/docs/core/dynamics/evolution#теорема-живой-аттрактор-в-окне). A fixed point of $M$ need not be a stationary state of the full vector field.

#### Anchor constraints {#жизнеспособный-якорь}

For fixed $k<1$ and a **diagonal** anchor $\sigma=\sum_iw_i|i\rangle\langle i|$, the map $k\Delta+(1-k)\sigma$ has the unique fixed point $\sigma$ (Theorem 2.1). For a general fixed anchor and fixed channel, the fixed point is

$$
\rho_*=(1-k)(I-k\mathcal P)^{-1}\sigma
=(1-k)\sum_{n\geq0}k^n\mathcal P^n(\sigma).
$$

The positive series has trace one; it equals $\sigma$ only if $\mathcal P(\sigma)=\sigma$.

**Withdrawn 2026-10-03 [✗]: Theorem 2.2, compulsory E-accentuation.** The scalar conditions $R\geq1/3$, $\Phi\geq1$, and differentiation of a specified subsystem do not force $w_E>1/7$ in a feedback anchor. State conditions do not constrain an independent anchor law without a linking premise. The former $\alpha^*=37/49$ had no valid derivation. An E-accentuated anchor can be an explicit hypothesis; it is not a consequence of L2.

For the family $\sigma(a)=a|E\rangle\langle E|+(1-a)\sum_{i\ne E}|i\rangle\langle i|/6$, the exact purity is $a^2+(1-a)^2/6$. For $a\geq1/7$, $P(\sigma)>2/7$ holds iff $a>(1+\sqrt6)/7\approx0.4928$ [T within this family]. A diagonal anchor has $\Phi=0$, so its viable purity does not establish an integrated conscious fixed point. The maximal-integration anchor of $M_J$ follows from (MaxΦ)/(Eq-V) [Pr], not from the support adjunction.
#### Theorem T-191 (Convergence of the φ-tower; restated 2026-09-25) [T] {#t-191-сходимость-φ-башни}

:::warning Retracted (2026-09-25): convergence "from any anchor" for every holon, $q = \kappa_{\max}/(\lambda_{\mathrm{gap}} + \kappa_{\min})$ [✗]
The former statement — the tower converges for every holon, from any anchor, with rate $q = \kappa_{\max}/(\lambda_{\mathrm{gap}} + \kappa_{\min}) < 1$ — is retracted with its proof, which is the retracted proof of T-124c in another dress. Step 1 called $\mathcal{L}_0 + \kappa(\Gamma)g_V(P)(\varphi^{(n)}(\Gamma) - \Gamma)$ a generator of a contractive CPTP semigroup with a unique stationary state; the scalars depend on $\Gamma$, and the gate makes the flow bistable. For an isolated holon with a fixed target $|0\rangle\langle 0|$ and $\kappa = 3$ the flow from $I/7$ stays at $I/7$ (the gate is closed) while the flow from $|0\rangle$ ends at a living state with $P \approx 0.98$, so $\varphi^{(n+1)} = \lim_\tau \exp(\tau\mathcal{L}^{(n)})$ is not defined. Step 3 used $\kappa_{\max} < \lambda_{\mathrm{gap}}$, "verified in T-96" — T-96 verifies no such bound. For the canonical unital $\varphi_{\mathrm{coh}}$ the tower started at $I/7$ stays at the dead replacement channel $\Gamma \mapsto I/7$ ([dead isolation](/docs/core/dynamics/evolution#теорема-мёртвая-изоляция)).
:::

:::tip Theorem T-191 (restated) [T]
Let an embodied holon carry the backbone term $\mu(\sigma - \Gamma)$ ([T-148](/docs/proofs/consciousness/substrate-closure#t-148)); let $L_{\mathcal{R}}$ be a trace-norm Lipschitz constant on $\mathcal{D}(\mathbb{C}^7)$ of $\Gamma \mapsto \kappa(\Gamma)g_V(P)(a - \Gamma)$, uniform in the target state $a$, and $\kappa_{\max} = \sup \kappa\,g_V$. If

$$
\mu > L_{\mathcal{R}} + \kappa_{\max},
$$

then the tower of self-models — $a_0$ any state, $a_{n+1}$ the stationary state of the dynamics with regeneration target $a_n$ (so that $\varphi^{(n)}$ is the replacement channel $\Gamma \mapsto a_n$) — is well defined, and

$$
\|a_n - a^*\|_1 \leq \frac{q^n}{1 - q}\,\|a_1 - a_0\|_1, \qquad q = \frac{\kappa_{\max}}{\mu - L_{\mathcal{R}}} < 1,
$$

with one limit $a^*$ for every initial anchor: $a^*$ is the stationary state of the dynamics that regenerates toward $a^*$ itself.
:::

**Proof.** *Each iterate is defined.* $\mu > L_{\mathcal{R}}$ is the backbone dominance of [T-124c (3)](/docs/core/dynamics/evolution#теорема-единственность-нетривиального-аттрактора): for every target $a$ the dynamics has exactly one stationary state $\rho(a)$, and every trajectory reaches it at rate $c = \mu - L_{\mathcal{R}}$ in trace norm.

*The iteration contracts.* For targets $a, b$ the two generators differ by $\kappa(\Gamma)g_V(P)(a - b)$, whose trace norm is at most $\kappa_{\max}\|a - b\|_1$. Run the dynamics with target $a$ from $\rho(b)$; the difference $\Delta(\tau)$ from the constant solution $\rho(b)$ of the dynamics with target $b$ obeys, by the contraction estimate of T-124c (3) with this inhomogeneity, $\|\Delta(\tau)\|_1 \leq \int_0^\tau e^{-c(\tau - s)}\,\kappa_{\max}\|a - b\|_1\,ds \leq \kappa_{\max}\|a - b\|_1/c$. As $\tau \to \infty$ the trajectory reaches $\rho(a)$, so $\|\rho(a) - \rho(b)\|_1 \leq q\,\|a - b\|_1$.

*Banach.* $\mathcal{D}(\mathbb{C}^7)$ with the trace norm is complete; $a \mapsto \rho(a)$ is a contraction with constant $q < 1$, so it has one fixed point $a^*$, the iterates converge to it geometrically, and two towers started at $a_0, \tilde a_0$ approach each other as $q^n\|a_0 - \tilde a_0\|_1$. $\blacksquare$

*Constants.* $\kappa$ constant: $\lvert P(X) - P(Y)\rvert = \lvert\mathrm{Tr}\,(X + Y)(X - Y)\rvert \leq 2\|X - Y\|_1$ and $g_V = \mathrm{clamp}(7P - 2, 0, 1)$ give $L_{\mathcal{R}} \leq \kappa(1 + 2 \cdot 14) = 29\kappa$. Witness (`test_phi_tower_converges_only_under_backbone_dominance`): $\kappa = 0.1$, $\mu = 3.5$, $P(\sigma) > 3/7$, so $q \leq 1/6$; from $I/7$, $|0\rangle$ and a random pure anchor the towers meet to $10^{-10}$, each step contracts by at most $0.028$, and the limit has residual $< 10^{-10}$ with the gate open; the isolated counterexample of the box above is in the same check.

**Dependencies:** T-124c (3) [T] (backbone dominance: existence, uniqueness and rate of the stationary state), T-148 [T] (backbone term). Standard mathematics: Banach fixed-point theorem, the variation-of-constants estimate for a flow contracting in trace norm. (The dependencies read "T-39a (spectral gap), T-59, T-96 ($\kappa < \kappa_{\max}$), T-124c (attractor uniqueness)" until 2026-09-25; the uniqueness statement of T-124c is retracted, and T-96 bounds no $\kappa$.)
## Dynamical limits and spectral projectors {#теорема-φ-как-стационарное-распределение}

### Nonlinear basin retraction [T at convergence]

Let $F_t:D\to D$ be a continuous autonomous semiflow, $F_{t+s}=F_tF_s$, on an invariant domain of states. Suppose $r(x)=\lim_{t\to\infty}F_t(x)$ exists in $D$ for every $x\in D$. Then

$$
F_s(r(x))=\lim_{t\to\infty}F_s(F_t(x))
=\lim_{t\to\infty}F_{t+s}(x)=r(x).
$$

Thus $r(x)$ is an equilibrium and $r(r(x))=r(x)$. This proves a set-theoretic retraction onto equilibria [T]; it supplies no categorical adjunction. Continuity of $r$ requires additional hypotheses, for example locally uniform convergence; it may fail at basin boundaries. Periodic or recurrent attractors generally do not give a pointwise limit. A unique stationary state alone does not prove global convergence.

### Linear spectral formula, with the correct hypotheses {#27-спектральная-формула-для-φ-явное-вычисление}

**Theorem 2.3 (revised) [T].** Let $\mathcal L$ be a finite-dimensional **linear** GKSL generator. Its bounded CPTP semigroup has semisimple peripheral eigenvalues. The Cesàro limit

$$
\overline\Pi_0=\lim_{T\to\infty}\frac1T\int_0^T e^{t\mathcal L}\,dt
$$

exists, is CPTP and idempotent, and equals the spectral projector onto $\ker\mathcal L$. The ordinary limit $\lim_{t\to\infty}e^{t\mathcal L}$ equals this projector if there are **no nonzero purely imaginary eigenvalues**. If in addition the stationary space is one-dimensional with normalized state $\rho_0$, the projector is $X\mapsto\mathrm{Tr}(X)\rho_0$.

*Proof.* Jordan normal form: boundedness forbids nontrivial Jordan blocks on $\operatorname{Re}\lambda=0$; negative-real-part modes decay. Time averaging kills each nonzero imaginary frequency and leaves precisely the zero eigenspace. CPTP maps form a closed convex set, hence the averaged limit is CPTP. If $\lambda=i\omega\ne0$, $e^{i\omega t}$ does not converge, so the former sum over all $\operatorname{Re}\lambda=0$ was not an ordinary asymptotic limit. In the one-dimensional case trace preservation fixes the coefficient of $\rho_0$ to $\mathrm{Tr}(X)$. $\square$

For a diagonalizable $\mathcal L$, using Hilbert–Schmidt biorthogonal eigenoperators,

$$
\overline\Pi_0(X)=\sum_{a:\lambda_a=0}R_a\,\mathrm{Tr}(L_a^\dagger X),
\qquad\mathrm{Tr}(L_a^\dagger R_b)=\delta_{ab}.
$$

Diagonalizability is needed for this eigenvector formula, not for existence of the spectral projector. In computation use a nullspace or Schur decomposition with an explicitly checked spectral separation; checking only $|\operatorname{Re}\lambda|<\varepsilon$ incorrectly includes oscillatory modes. Hermitization/trace normalization cannot repair a wrong projector or certify complete positivity.

**Withdrawn [✗]: nonlinear Jacobian as self-model projector.** At a hyperbolic attracting equilibrium of a $C^1$ trace-preserving vector field, the Jacobian **on $\mathrm{Herm}_0(7)$** has all eigenvalues with negative real part; it has no zero mode. Trace conservation is a left-annihilation identity on an ambient extension, not a stationary right eigenvector of the tangent Jacobian. Primitivity of $\mathcal L_0$ says nothing by itself about the Jacobian spectrum of $\mathcal L_0+\mathcal R$. There is no linear superoperator $e^{t\mathcal L_\Omega}$ for a general nonlinear vector field. Its semiflow must be denoted $F_t$ and computed as such.

### Iteration and depth {#28-рефлексия-n-го-порядка-для-l3l4}

Define $M^{(n)}$ by ordinary composition, $M^{(0)}=\mathrm{id}$, and if useful define $\widehat R^{(n)}=F(M^{(n-1)}\Gamma,M^{(n)}\Gamma)$ using squared Uhlmann fidelity. This quantity is different from canonical $R=1/(7P)$ and from $R_M$ below. If $M$ is idempotent, $\widehat R^{(n)}=1$ for $n\geq2$; it cannot resolve higher levels by itself. Thresholds for L3/L4 or a maximum phenomenological depth require separate definitions and bridge hypotheses; the existence of iterates does not derive them.

## Fixed-point theorems {#3-теорема-о-существовании-неподвижной-точки}

**Theorem 3.1 [T].** A self-map of $\mathcal D(\mathcal H)$ contracting with factor $q<1$ in a specified complete norm has a unique fixed point and convergent iterates with error at most $q^n\|\rho-\rho_*\|$. This is Banach's theorem. Lemma 2.1 verifies the hypothesis in trace norm for fixed parameters. It does not verify it for adaptive $M_{\mathrm{coh}},M_s,M_J$.

**Theorem 3.2 (strengthened) [T].** Every continuous $M:\mathcal D(\mathcal H)\to\mathcal D(\mathcal H)$ has an **exact** fixed point by Brouwer's theorem. Continuity gives neither uniqueness nor convergence of iterations. No approximate fixed-point regularization is necessary in finite dimension.

**Correct contraction criterion (Theorem 3.3).** For a linear channel, one-step Frobenius contraction on states is equivalent to an operator norm $<1$ on the Hermitian traceless subspace (the largest singular value there), not merely eigenvalue moduli $<1$. Spectral radius $<1$ on that subspace ensures decay of powers, and eventually a power contracts; a nonnormal map can expand a distance in one step. This distinction also applies to stability Jacobians.

## Reflection and response {#4-связь-с-меры-рефлексии-r}

### Two distinct quantities

$$
R(\Gamma)=\frac1{7P}\in[1/7,1],\qquad
R_M(\Gamma)=1-\frac{\|\Gamma-M(\Gamma)\|_F^2}{P}.
$$

$R_M$ is also written $R_\varphi$ in the corpus. It measures normalized mismatch and is bounded above by one, but can be **negative**: for two orthogonal pure states with $M(\Gamma)$ equal to the other one, $R_M=-1$. It is not a probability unless an additional admissibility bound is imposed. At any fixed point $R_M=1$, while $R=1/(7P)$ is still controlled by purity. The model-independent consciousness measure $C=\Phi R$ does not become $\Phi$ merely because $R_M=1$.

Continuity at a fixed point gives $R_M\to1$. For a Frobenius contraction with factor $q<1$, $\Gamma_n=M^n\Gamma_0$ obeys

$$
1-R_M(\Gamma_n)
\leq\frac{q^{2n}}{P_{\min}}\|\Gamma_0-M\Gamma_0\|_F^2
\leq\frac{(1+q)^2q^{2n}}{P_{\min}}\|\Gamma_0-\Gamma_*\|_F^2,
\quad P_{\min}=1/N.
$$

These are conditional estimates (Theorems 4.1–4.2). There is no unconditional convergence theorem from primitivity of the linear dissipator for every nonlinear self-model.

### Derivative of a numerical self-model {#дф-производная}

For a differentiable $M$ along a state path, let $\Delta=\Gamma-M(\Gamma)$. The chain rule gives the exact identity

$$
\dot R_M=(1-R_M)\frac{\dot P}{P}
-\frac2P\langle\Delta,(I-DM)[\dot\Gamma]\rangle_F.
$$

**T-249 [T].** For the dissipative replacement family $M(\Gamma)=R\Gamma+(1-R)I/7$,

$$
DM[V]=RV-\frac{2}{7P^2}\langle\Gamma,V\rangle_F(\Gamma-I/7).
$$

*Proof.* Differentiate $R=1/(7P)$ using $DP[V]=2\langle\Gamma,V\rangle_F$. Both terms have trace zero. The family is unitarily equivariant. Its mismatch satisfies $R_M=1-(1-R)^3$ and therefore
$\dot R_M=-3(1-R)^2\dot P/(7P^2)$, also recovered by substitution into the chain rule. This family differs from $M_{\mathrm{coh}}$; its derivative must not be substituted for that of another family. $\square$

### Bandwidth bound {#теорема-полосы-rφ}

**T-250 [T at differentiability].** With $C_M(\Gamma)=\|I-DM_\Gamma\|_{F\to F}$,

$$
\left|\dot R_M-(1-R_M)\dot P/P\right|
\leq\frac{2}{\sqrt P}\sqrt{1-R_M}\,C_M(\Gamma)\|\dot\Gamma\|_F.
$$

*Proof.* Cauchy–Schwarz and $\|\Delta\|_F=\sqrt{P(1-R_M)}$. For the T-249 family, $C_M\leq(1-R)+2R\sqrt{1-R}$. $\square$

At constant $P$, putting $u=\sqrt{1-R_M}=\|\Delta\|_F/\sqrt P$ yields the rigorous path estimate

$$
|u(t_2)-u(t_1)|\leq\frac1{\sqrt P}
\int_{t_1}^{t_2}C_M(\Gamma(t))\|\dot\Gamma(t)\|_F\,dt.
$$

A constant outside the integral must be a uniform bound along the path. The norm formulation also handles $u=0$ without dividing by zero. Invariance under a group holds only when $M$ is equivariant under that group. The bound alone fixes neither sign nor a generic rate of change and does not derive a phenomenological interpretation such as ego dissolution.

### Learning and additional parameters {#механизмы-rφ}

For $M_\theta(\Gamma)=(1-k)\Gamma+k\rho_\theta$ at fixed $k$, a hypothesized alignment law $\dot\rho_\theta=2\eta(\bar\Gamma-\rho_\theta)$ stays in the state space and has the exact solution
$\rho_\theta(t)=(1-e^{-2\eta t})\bar\Gamma+e^{-2\eta t}\rho_\theta(0)$.
At fixed practiced $\bar\Gamma$, this gives
$R_{M_\theta}(\bar\Gamma)=1-k^2e^{-4\eta t}\|\bar\Gamma-\rho_\theta(0)\|_F^2/P$.
The learning law and its experiential reading are additional model assumptions [H]/[I]; the formula is [T within that law]. For time-varying parameters the derivative of the mismatch contains $\partial_\theta M\,\dot\theta$ as well as $D_\Gamma M\,\dot\Gamma$.

### Implicit numerical models {#дф-неявная}

**T-251 [T, explicit regularity].** Suppose $G(x,y)$ extends to a $C^1$ function on open neighborhoods in the trace-one affine spaces, the state space is invariant for $y\mapsto G(x,y)$, and $\|D_2G\|\leq q<1$. For each $x$ let $M(x)$ be its unique fixed point. Locally where the extension assumptions hold, the implicit function theorem gives

$$
DM=(I-D_2G)^{-1}D_1G=\sum_{n\geq0}(D_2G)^nD_1G,
\qquad\|DM\|\leq\frac{\|D_1G\|}{1-q}.
$$

*Proof.* Differentiate $y-G(x,y)=0$; $I-D_2G$ is invertible by the Neumann series. $\square$ Smoothness cannot be inferred from a support adjunction, from Bures continuity, or merely from writing a function on a closed convex set. This theorem differentiates a **numerical** fixed-point equation, not a logical support reflector.

### Discrimination bound, with sharp constants {#гейт-теорема}

**T-252 [T].** For any POVM and $\Delta=\Gamma-M\Gamma$,

$$
\mathrm{TV}(p_\Gamma,p_{M\Gamma})\leq\tfrac12\|\Delta\|_1,
\qquad\|\Delta\|_1\leq\sqrt{48/7}\|\Delta\|_F.
$$

The second constant is sharp on $\mathrm{Herm}_0(7)$. If positive and negative eigenvalues have multiplicities $p,q$ and common total magnitude $s$, Cauchy–Schwarz gives $\|\Delta\|_F^2\geq s^2(1/p+1/q)$ and $\|\Delta\|_1=2s$. Thus the ratio squared is at most $4pq/(p+q)\leq48/7$, attained by $\operatorname{diag}(4,4,4,-3,-3,-3,-3)$ up to scale. The POVM step is saturated by the projector on the positive spectrum.

For a decision rule whose true-state success is $A_D$, the corresponding success evaluated on the model obeys

$$
p_M\geq A_D-2\sqrt{3/7}\sqrt{P(1-R_M)}.
$$

Here a multi-hypothesis task requires this estimate statewise or averaged over its specified ensemble; a POVM on a single state does not define an ensemble accuracy by itself. If $A_D>1/K$, **strict** superiority $p_M>1/K$ is guaranteed by

$$
R_M>1-\frac7{12P}(A_D-1/K)^2.
$$

Equality gives only $p_M\geq1/K$. For $K=3$, $A_D=1$ the sufficient boundary varies with $P$ from $5/54$ to $32/81$ over $(2/7,3/7]$; this does not select a universal threshold $1/3$.

For the valid sector POVM $E_\pm=(\Pi_{ij}\pm X_{ij})/2$, $E_0=I-\Pi_{ij}$, the outcome shift is bounded by $|\Delta_{ij}|+|\Delta_{ii}+\Delta_{jj}|/2$. If $\gamma_{ij}\ne0$ and $R_{ij}:=1-|\Delta_{ij}|^2/|\gamma_{ij}|^2$, then $|\Delta_{ij}|=|\gamma_{ij}|\sqrt{1-R_{ij}}$ exactly. The amplitude and diagonal mismatch remain in the bound. Hence the former claim that this **derives** $R_{ij}\geq1/3$ is withdrawn [✗]; that working threshold needs a separate calibration/interpretation. No comparison of decision accuracy with canonical $R=1/(7P)$ follows from these mismatch bounds without an additional bridge.
## Categories, monads, and realization {#5-категорный-аспект}

A frozen CPTP channel is an endomorphism of a matrix algebra in the category of channels; it is not automatically an endofunctor or a natural transformation. Conjugation by an inverse channel defines a channel-category automorphism only for a specified reversible channel with CPTP inverse. A numerical state map $M$ need not act on morphisms at all.

The genuine support adjunction defines an **idempotent monad on $\mathcal E_{/G}$**, $T_G=i_GL_G$, with unit the image factorization and multiplication induced by the counit $L_Gi_G\simeq\mathrm{id}$. Its algebras are precisely $(-1)$-truncated objects over $G$, not density matrices satisfying an unrelated feedback equation.

For probabilistic mixing, the well-typed standard construction is the finite probability-distribution monad $\mathsf{Dist}_f$ on sets. A convex state space is its algebra via $(p_a,\rho_a)\mapsto\sum_ap_a\rho_a$. A linear channel preserves this convex structure; a general adaptive $M$ does not. The former expression $T(X)=\mathcal D(\mathbb C^{|X|})$ together with $T(T(X))$ and a density-matrix "support" was not a defined monad on Set. The former Theorem 5.1 identifying a single fixed density matrix with such an algebra is withdrawn [✗]. Channels alone also do not supply the stated 2-category of "natural transformations between channels"; a 2-categorical enhancement requires explicit hom-categories and composition laws.

A bridge from logical support to numerical self-modelling would have to specify a state representation, a readout/model category, and a realization functor with a compatibility statement. No such bridge is inferred from an adjunction merely by using the same symbol $\varphi$. Establishing one remains a research task [Pr].

## Scope and interpretation {#6-следствия-и-ограничения}

Existence, uniqueness, convergence, dynamical stability, and physical realization are different claims with separate hypotheses. A fixed point gives equality of a chosen map's input and output; interpreting this as accurate self-knowledge requires an independent error/readout model [I]. It need not be a thermodynamic equilibrium. Fixed-point equality makes regeneration vanish, but the other terms of the vector field may still move the state.

## Implementation requirements {#7-требования-к-реализации}

Specify the map and its parameters before testing its output. A neural state-to-state model may use $LL^\dagger/\mathrm{Tr}(LL^\dagger)$ with $L\ne0$ to ensure a valid state; this does not establish affinity, complete positivity as a linear operation, contraction, or correspondence with a logical reflector. For a neural CPTP channel, parameterize a Stinespring isometry or a positive Choi matrix with the trace-preservation constraint. Mixing a general neural output with $I/7$ contracts only if a separately proved Lipschitz bound $L$ gives $kL<1$.

A Hermitian $7\times7$ input has 49 real coordinates before the trace constraint and 48 independent ones: 7 real diagonal entries and 21 complex off-diagonal entries. A complex lower-triangular Cholesky factor with real diagonal likewise uses 49 real coordinates; enforce nonzero norm, for example by positive diagonal entries. A 28-real-coordinate network cannot represent all complex states.

## Operational algorithms {#операциональный-алгоритм}

```text
FUNCTION numerical_self_model(Gamma, alpha, anchor_kind):
    REQUIRE Gamma Hermitian, PSD, trace = 1; 0 <= alpha <= 1
    P := trace(Gamma * Gamma)
    R := 1 / (7 * P)
    c := (1 - alpha) / 3
    prediction := diag(Gamma) + c * (Gamma - diag(Gamma))
    IF anchor_kind == "coh": anchor := I / 7
    IF anchor_kind == "s":   anchor := Gamma * Gamma / P
    IF anchor_kind == "J":   anchor := u * u_dagger
    RETURN (1 - R) * prediction + R * anchor
    # State-preserving nonlinear map; parameters freeze only inside a channel step.

FUNCTION reflection_readouts(Gamma, M):
    P := trace(Gamma * Gamma)
    R_canonical := 1 / (7 * P)
    R_model := 1 - norm_F(Gamma - M(Gamma))^2 / P
    RETURN R_canonical, R_model  # Do not clip or identify them.
```

For a primitive **linear** generator, solve $\mathcal L\rho_0=0$ with $\mathrm{Tr}\rho_0=1$ and verify positivity, residual and uniqueness; return $X\mapsto\mathrm{Tr}(X)\rho_0$. For a nonlinear vector field, integrate from specified initial states and test residuals, invariant domains and basin dependence. A 49-by-49 Jacobian projection is not a general numerical self-model algorithm.

### Canonical reflection readout {#83-вычисление-меры-рефлексии-r}

The reduced seven-dimensional L2 screen uses $P>2/7$, $R_{\mathrm{canonical}}\geq1/3$ and $\Phi\geq1$. It is only a screen: the full differentiation condition requires a specified tensor extension and model of the E-subsystem. Omitting it does not certify the full L2 predicate. These are formal criteria [D], with empirical interpretation assessed independently.

## Regeneration and state preservation {#связь-с-регенерацией}

Given a numerical law $M$ and a nonnegative effective rate $a(\Gamma)=\kappa(\Gamma)g_V(P)$, define [D]

$$
\mathcal R(\Gamma)=a(\Gamma)(M(\Gamma)-\Gamma).
$$

For $0\leq h\,a(\Gamma)\leq1$, the explicit feedback step $(1-ha)\Gamma+haM(\Gamma)$ is a density matrix by convexity [T]. Its frozen realization is CPTP if a channel family has been specified, but the adaptive update is generally nonlinear. Combined with a linear CPTP flow this gives a positivity-preserving split scheme under the stated step restriction. A locally Lipschitz continuous vector field with this tangent-cone property preserves the finite-dimensional state set; existence and convergence still require their own hypotheses.

At $M(\Gamma)=\Gamma$ regeneration vanishes. Conversely it may also vanish where $a=0$. Along regeneration its exact purity derivative is

$$
\dot P\big|_{\mathcal R}=2a(\Gamma)\bigl(\mathrm{Tr}(\Gamma M(\Gamma))-P\bigr).
$$

The purity of the target alone does **not** determine this sign: a high-purity target orthogonal to a pure current state gives a negative initial derivative. For the unital target $M_{\mathrm{coh}}$ the overlap does not exceed $P$; the nonunital anchors require an actual overlap and stability analysis. With $g_V=\operatorname{clamp}(7P-2,0,1)$ regeneration vanishes at and below the purity threshold for every finite rate. Thus a viable target does not prove global invariance of the viable region. The living $M_J$ attractor and saddle boundary remain the explicit conditional result in [evolution](/docs/core/dynamics/evolution#теорема-живой-аттрактор-в-окне).

The exact amplitude is $\|\mathcal R\|_F=a\sqrt{P(1-R_M)}$, not $a\sqrt{P(1-R)}$ for an arbitrary model. Rates and feedback gates are dynamical specifications; a support adjunction fixes neither. A fixed-target replacement flow can have an independently proved BKM gradient interpretation; a moving target requires its derivative and does not inherit the fixed-target Lyapunov theorem automatically.

## Time-dependent models and octonionic interpretation {#октонионный-контекст}

For a continuous family $M_t$ uniformly contracting with factor $q<1$, each instantaneous fixed point exists uniquely and varies continuously. If $M_t$ is $C^1$ on an affine neighborhood, then

$$
\dot\Gamma_*(t)=(I-D_\Gamma M_t)^{-1}\partial_tM_t(\Gamma_*(t)).
$$

Continuity alone gives no derivative. An instantaneous fixed point is not necessarily a solution trajectory or an adiabatically tracked state.

Octonionic alternativity constrains octonion multiplication, not composition of arbitrary matrix-state maps: composition of $M$ is associative. The association of Fano lines with an octonionic product can structure chosen filters [D]/[I]; it does not make a CPTP or nonlinear self-model "nonassociative" or derive its anchor.

## Composite systems and local channel compilation {#тензорная-факторизация}

**Withdrawn [✗]: categorical derivation of tensor factorization.** In general $\mathrm{Sub}(A\times B)\not\simeq\mathrm{Sub}(A)\times\mathrm{Sub}(B)$, even in Set: the diagonal in a two-point square is not a Cartesian rectangle. Probabilistic conditional independence does not imply this lattice identity. Cartesian products in a topos and Hilbert tensor products are not interchangeable. The support adjunction therefore does not derive $M_{AB}=M_A\otimes M_B$; a tensor product of nonlinear state maps is not defined without extension data.

For a specified frozen local channel $\mathcal C_{A,\lambda}$ its spectator extension is, by definition,

$$
\widetilde{\mathcal C}_{A,\lambda}=\mathcal C_{A,\lambda}\otimes\mathrm{id}_B.
$$

For an adaptive local law choose $\lambda=\lambda(\rho_A)$, $\rho_A=\mathrm{Tr}_B\rho_{AB}$, and apply this frozen channel to the joint state. This defines an extension **relative to the chosen channel family**. Different compilations of the same numerical marginal law may act differently on correlations; the marginal state map alone does not ensure a unique extension.

**Marginal identity [T].** Trace preservation gives

$$
\mathrm{Tr}_A[(\mathcal C_{A,\lambda}\otimes\mathrm{id}_B)(\rho_{AB})]=\rho_B.
$$

*Proof.* Test against any $O_B$; the channel adjoint is unital, so $(\mathcal C_{A,\lambda}^*\otimes\mathrm{id})(I_A\otimes O_B)=I_A\otimes O_B$. Equality of all expectations proves the identity. It holds for each frozen parameter, hence also pointwise for the adaptive choice and a scalar multiple of the corresponding increment. $\square$

For fixed local channels, their tensor product is CPTP and compositions on separate factors commute. This is a statement about a specified product channel, not a categorical theorem forcing all composite models to factorize. The marginal identity alone does not prove relativistic no-signalling with arbitrary measurement updates: state-dependent feedback requires the explicit non-selective marginal prescription of [physical correspondence](/docs/proofs/physics/physics-correspondence#запрет-сигнализации). That dynamical prescription is distinct from the support reflector.

## Sources and dependencies

- Lurie, [*Higher Topos Theory*](https://arxiv.org/abs/math/0608040): truncation, slices and image factorization.
- [Kerodon, Corollary 7.1.4.28](https://kerodon.net/tag/02KE): a right adjoint preserves limits.
- Watrous, [*The Theory of Quantum Information*, chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.double.2.pdf): linear channels, Kraus representations and tensor extensions.
- [φ operator](/docs/core/operators/phi-operator): explicit $M_{\mathrm{coh}},M_s,M_J$ and anchor premises.
- [Evolution](/docs/core/dynamics/evolution): equilibria of the full vector field and their separate stability conditions.

<a id="1-введение-и-мотивация"></a>
<a id="31-основная-теорема"></a>
<a id="4-связь-с-мерой-рефлексии-r"></a>
