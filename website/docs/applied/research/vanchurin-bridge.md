---
sidebar_position: 18
title: The Learning Algorithm of a Holon
description: An exact bridge to Vanchurin's learning-dynamics programme — UHM fixes the free function g(κ) and lands on a = 1
---

# The Learning Algorithm of a Holon is Natural Gradient

Vanchurin's programme derives physical and biological law from learning
dynamics. It leaves one central quantity undetermined: the functional
relation $g(\kappa)$ between the metric tensor on trainable space and
the covariance of gradient noise, parametrised as a power law
$g=\kappa^{a}$ with three named regimes — $a=0$ (stochastic gradient),
$a=\tfrac12$ (efficient learning, Adam-like, conjectured to underlie
biological complexity) and $a=1$ (natural gradient, the "quantum
regime"). He states that direct empirical estimates of $\kappa$ remain
unavailable and calls obtaining them a formidable challenge.

In UHM this quantity is **not free**. Both factors are forced by the
axioms — $g$ by Axiom 2 (Bures is the unique monotone Riemannian
metric), $\kappa$ by the canonical dissipator whose Lindblad operators
are the atoms of the subobject classifier plus the seven Fano
projectors. Their relation is therefore a theorem, not a parameter:

$$
\kappa^{\uparrow\uparrow}_{\text{at}} \;=\; \frac{\gamma}{4N}\,g^{-1}
\qquad\Longleftrightarrow\qquad
\Pi\,g\,\kappa_{\text{at}}\,\Pi \;=\; \frac{\gamma}{4N}\,\Pi
$$

on the population sector of a holon of dimension $N=7$, where $\Pi$ is
the projector onto the tangent space. This is *verbatim* Vanchurin's own
criterion for $a=1$: substituting $a=1$ into his Eq. (7.5) gives
$g^{-1}=g^{-1}\kappa g^{-1}=\kappa^{\uparrow\uparrow}$. Hence

$$
a = 1 \quad\text{(natural gradient), exactly.}
$$

:::info Primary sources
Equation numbers throughout refer to:

- **[V1]** V. Vanchurin, *Geometric framework for biological evolution*,
  arXiv:2603.15198 — Eqs. (4.7), (6.3), (6.7)–(6.9), (7.1)–(7.6). This
  is the source of the $g(\kappa)$ programme in the form used here.
- **[V2]** V. Vanchurin, *Geometric Learning Dynamics*,
  arXiv:2504.14728, *Biological Cybernetics* (2026) — Eqs. (2.2),
  (2.8), (2.9), (5.5).

Two notational hazards, stated once. **[V1] uses $a$ for the learning
exponent and $\alpha$ as a coordinate index; [V2] uses $\alpha$ for the
exponent.** We follow [V1] and write $a$. And **his $\gamma$ is a
learning rate; our $\gamma$ is the dissipator rate** — they are
unrelated, and every $\gamma$ on this page is ours.
:::

Four further exact results follow. The canonical Fano layer multiplies
the metric-weighted noise trace by the universal rational factor
$11/9$ — independent of the state — so that the block layer carries
exactly $2/11$ of the noise, and it introduces a computable anisotropy.
Noise magnitude is tied to purity, $\operatorname{Tr}\kappa=
\frac{\gamma}{N}(1-P)$. The dissipator annihilates every diagonal
state, so on populations it is **pure noise without drift** — which is
what makes $\kappa$ a genuinely *centred* covariance in the sense of
his (7.4). And there is a strict **sector split**:
$\kappa^{\text{coh}}=0$ on the decohered manifold, where coherences
instead contract deterministically at $\lambda_{\text{deco}}=5\gamma/21$.

The central consequence for the learning-theoretic programme: UHM
predicts that a *viable* learning system implements **natural gradient
descent**, not the $a=\tfrac12$ regime conjectured for biological
complexity. Its efficiency comes not from a different exponent but from
the Fano-induced anisotropy of the noise and from confinement of purity
to the window $P\in(2/7,3/7]$. This is a sharp, falsifiable
disagreement, and §9 gives a **metric-free** test statistic for it,
together with the sample size it needs.

---

## 1. The two frameworks and their dictionary {#словарь}

Vanchurin's covariant learning framework (henceforth **VL**) is built
on: trainable variables $q$, a loss/fitness $\mathcal F$, a metric
$g_{\alpha r,\beta s}$ on trainable space, a noise covariance
$\kappa_{\alpha r,\beta s}=\langle\partial_\alpha\phi\,
\partial_\beta\phi\rangle$ (his 6.7), and the covariant update
$\dot q = g^{-1}\nabla\mathcal F$ (his 6.3). The learning algorithm is
*defined* by the functional relation $g(\kappa)$ (his 6.8–6.9).

UHM is built on five axioms: reality as an $\infty$-topos over density
matrices, the **Bures** Grothendieck topology, dimension $N=7$, a scale
$\omega_0$, and a Page–Wootters decomposition (the last derivable,
T-87). Its dynamics is the **triad** forced by LGKS-completeness
(T-57):

$$
\mathcal L_\Omega[\Gamma] = \underbrace{-i[H,\Gamma]}_{\text{Aut}}
+ \underbrace{\mathcal D_\Omega[\Gamma]}_{\text{Fano dissipator}}
+ \underbrace{\mathcal R[\Gamma]}_{\text{regeneration}} .
$$

The dictionary is exact on every line that matters:

| VL object | UHM object | Status of the link |
|---|---|---|
| trainable state $q$ | coherence matrix $\Gamma\in\mathcal D(\mathbb C^7)$ | structural |
| loss $-\mathcal F$ | free-energy functional $\mathcal F[\varphi;\Gamma]$ | T-39e (variational $\varphi$) |
| metric $g$ | **Bures/SLD metric** — *unique* monotone metric (Petz; T-187) | forced, not chosen |
| noise covariance $\kappa$ | covariance of one-step Kraus increments of $\mathcal D_\Omega$ | forced by T-41/T-59, **relative to the canonical Kraus resolution** (§7.2) |
| covariant descent $\dot q=g^{-1}\nabla\mathcal F$ | regeneration $\mathcal R$ toward $\rho_*$ | T-39f–h |
| emergent time = block index | $\tau\in\mathbb Z_7$ (Page–Wootters) | T-38b, T-87 |
| maximum-entropy identity $g^{-1}=c$ (his 4.7) | **derived here as a dynamical theorem** (§4) | this page |
| multi-level structure | fractal holon, contraction $c_F=1/3=1/\lvert\mathrm{QR}(7)\rvert$ | T-72, CC-5 |
| cellular network | Fano plane $\mathrm{PG}(2,2)$, *unique* optimal BIBD$(7,3,1)$ | T-41i |

---

## 2. Setup: the noise covariance of a holon {#постановка}

Let $\rho$ be the state of a holon and let the canonical dissipator
have Lindblad set

$$
\mathcal K \;=\;
\underbrace{\{L_k=|k\rangle\langle k|\}_{k=1}^{7}}_{\text{atomic}}
\;\cup\;
\underbrace{\Bigl\{L_p=\tfrac{1}{\sqrt3}\Pi_p\Bigr\}_{p\in\mathrm{PG}(2,2)}}_{\text{Fano}},
\qquad
\Pi_p=\sum_{i\in p}|i\rangle\langle i| .
$$

:::note Labelling invariance
Every result on this page depends on the line set only through the
design parameters $(v,k,r,b)=(7,3,3,7)$ — which axis-triples realise
the lines never enters. Axis-*labelled* corollaries (such as the
third-point screen quoted in §5) do require the canonical translate
set of the corpus, $\{1,2,4\}+k \pmod 7$ with $U=6,\,O=7$ — see
[selection rules](/docs/physics/gauge-symmetry/fano-selection-rules#каппа-по-подавленным).
:::


In the quantum-jump (unravelling) picture, during $dt$ a jump $e$ occurs
with probability $p_e=\frac{\gamma\,dt}{N}\operatorname{Tr}
(L_e\rho L_e^\dagger)$, taking $\rho$ to $\rho_e=L_e\rho L_e^\dagger/
\operatorname{Tr}(L_e\rho L_e^\dagger)$. Define the **noise covariance**
as the covariance of the one-step increment $\Delta_e=\rho_e-\rho$:

$$
\kappa \;:=\; \frac{1}{dt}\sum_{e} p_e\;\Delta_e\otimes\Delta_e .
$$

This is Vanchurin's $\kappa^{\alpha r,\beta s}$ with **raised**
indices — the covariance of *temporal changes*, his (7.4). The index
placement is load-bearing, and it is the one thing a reader should check
first: $\Delta_e$ is a tangent vector (a change in $\lambda$), so its
covariance is contravariant, and his (7.4) states exactly
$\kappa^{\uparrow\uparrow}=g^{-1}\kappa_{\downarrow\downarrow}g^{-1}
=\langle\dot q\dot q\rangle-\langle\dot q\rangle\langle\dot q\rangle$.
Get this backwards and the derived exponent flips sign.

His (7.4) is a **centred** covariance, while the definition above is a
second moment. They agree only if the mean increment vanishes — which
it does, exactly, and that is §7.1. Without it the bridge would not
close.

Restricted to a state diagonal in the canonical basis,
$\rho=\operatorname{diag}(\lambda)$, all objects live on the
**population sector**, the tangent space
$T=\{x\in\mathbb R^N:\mathbf 1^{\!\top}x=0\}$, with projector
$\Pi=I-\tfrac1N J$ where $J=\mathbf 1\mathbf 1^{\!\top}$.

### 2.1 Normalisation of the metric, stated explicitly {#нормировка}

Monotone metrics are defined only up to a normalisation convention, and
since the headline identity carries a numerical constant, the convention
must be pinned down rather than assumed. On commuting (diagonal)
perturbations every monotone metric is proportional to the classical
Fisher–Rao metric, so write

$$
g\big|_T \;=\; c_g\,\operatorname{diag}(1/\lambda),
\qquad
c_g=\tfrac14\ \text{(Bures)},\qquad c_g=1\ \text{(SLD-QFI = Fisher–Rao)} .
$$

The Bures value is $\tfrac14$, not $\tfrac12$: from
$D_B^2=2(1-F)=\tfrac12\sum_{jk}\lvert\langle j|d\rho|k\rangle\rvert^2/
(\lambda_j+\lambda_k)$, the diagonal terms have
$\lambda_j+\lambda_k=2\lambda_j$, giving
$D_B^2=\tfrac14\sum_j (d\lambda_j)^2/\lambda_j$. The SLD quantum Fisher
information is $4\times$ Bures and reduces to the classical Fisher
metric exactly (Braunstein–Caves; T-187 Char-III); it is the
normalisation used in the natural-gradient literature.

**What depends on $c_g$ and what does not.** The exponent $a=1$, the
Fano factor $11/9$, the noise–purity law and the effective rank are all
independent of $c_g$. Only the absolute constants move:

| quantity | Bures ($c_g=\tfrac14$) | SLD-QFI ($c_g=1$) |
|---|---|---|
| $\Pi g\kappa_{\text{at}}\Pi$ | $\frac{\gamma}{4N}\Pi=\frac{\gamma}{28}\Pi$ | $\frac{\gamma}{N}\Pi=\frac{\gamma}{7}\Pi$ |
| $\operatorname{Tr}(g\kappa_{\text{at}})$ | $\frac{3\gamma}{14}$ | $\frac{6\gamma}{7}$ |
| $\operatorname{Tr}(g\kappa_{\text{full}})$ | $\frac{11\gamma}{42}$ | $\frac{22\gamma}{21}$ |
| per mode | $\frac{11\gamma}{252}$ | $\frac{11\gamma}{63}$ |

Bures is quoted as primary, because that is what Axiom 2 forces. All
tests in §9 are stated so as not to depend on the choice.

### 2.2 A jump process, not a diffusion {#скачковый-процесс}

One more thing bounds what the bridge claims. VL's (6.6) posits white
noise, $\langle\phi\phi'\rangle=C\,\delta(t-t')$, which reads as a
diffusion; the unravelling above is a compound Poisson process whose
jumps are *not* small — each takes $\lambda$ to a corner $e_k$ of the
simplex. What the definition computes is therefore the
quadratic-variation rate, i.e. the noise *intensity*, and for a
zero-mean compound Poisson process the increment over a window
$\Delta t$ has covariance exactly $\kappa\,\Delta t$. So the
identification with his (7.4) is exact at the level of the second
cumulant and only there: the higher cumulants of a holon's jumps are not
Gaussian. Every prediction on this page is a second-moment statement,
which is why they survive; the practical consequence — increments must
be aggregated over windows long enough for the central limit theorem to
apply — is spelled out in §9.1.

---

## 3. The Kraus covariance is exactly multinomial {#теорема-мультиномиальность}

:::tip Theorem [Т]
For the atomic part of the canonical dissipator and any diagonal state
$\rho=\operatorname{diag}(\lambda)$,

$$
\kappa_{\text{at}} \;=\; \frac{\gamma}{N}\Bigl(
\operatorname{diag}(\lambda)-\lambda\lambda^{\!\top}\Bigr),
$$

i.e. exactly $\gamma/N$ times the covariance matrix of a single-trial
multinomial distribution with parameters $\lambda$.
:::

**Proof.** For $L_k=|k\rangle\langle k|$ we have $L_k\rho L_k^\dagger=
\lambda_k|k\rangle\langle k|$, hence $\operatorname{Tr}(L_k\rho
L_k^\dagger)=\lambda_k$, $p_k=\gamma\,dt\,\lambda_k/N$ and
$\rho_k=|k\rangle\langle k|$, so $\Delta_k=e_k-\lambda$ as a vector in
the population sector. Substituting,

$$
\kappa_{\text{at}}=\frac{\gamma}{N}\sum_k \lambda_k
(e_k-\lambda)(e_k-\lambda)^{\!\top}
=\frac{\gamma}{N}\Bigl[\sum_k\lambda_k e_ke_k^{\!\top}
-\lambda\lambda^{\!\top}-\lambda\lambda^{\!\top}
+\lambda\lambda^{\!\top}\Bigr],
$$

using $\sum_k\lambda_k=1$ and $\sum_k\lambda_k e_k=\lambda$. The bracket
is $\operatorname{diag}(\lambda)-\lambda\lambda^{\!\top}$. $\blacksquare$

*Machine check*: over 2000 random states (Dirichlet concentration
$\in[0.4,4]$), the residual is $2.78\times10^{-17}$.

The matrix $\operatorname{diag}\lambda-\lambda\lambda^{\!\top}$ is
simultaneously the single-trial multinomial covariance **and** the
**inverse** of the Fisher metric on the simplex. That coincidence is the
whole engine of §4, and saying so up front is more honest than deriving
it as though it were a surprise.

---

## 4. The exact natural-gradient identity {#теорема-натуральный-градиент}

On commuting perturbations the Bures/SLD metric reduces to $c_g$ times
the classical Fisher–Rao metric (§2.1).

:::tip Theorem (natural gradient) [Т]
On the tangent space $T$,

$$
\Pi\,g\,\kappa_{\text{at}}\,\Pi \;=\; \frac{\gamma}{4N}\,\Pi ,
\qquad\text{i.e.}\qquad
\kappa^{\uparrow\uparrow}_{\text{at}}=\frac{\gamma}{4N}\,g^{-1}
$$

exactly, in Bures normalisation. Substituting $a=1$ into Vanchurin's
(7.5) gives precisely $g^{-1}=g^{-1}\kappa g^{-1}=
\kappa^{\uparrow\uparrow}$. The holon therefore realises $a=1$:
**natural gradient descent.**
:::

**Proof.** By §3 and $g=c_g\operatorname{diag}(1/\lambda)$,

$$
g\,\kappa_{\text{at}}
=\frac{c_g\gamma}{N}\operatorname{diag}(1/\lambda)
\bigl(\operatorname{diag}\lambda-\lambda\lambda^{\!\top}\bigr)
=\frac{c_g\gamma}{N}\bigl(I-\mathbf 1\lambda^{\!\top}\bigr).
$$

Since $\Pi\mathbf 1=0$, the rank-one term is annihilated:
$\Pi(\mathbf 1\lambda^{\!\top})\Pi=(\Pi\mathbf 1)(\lambda^{\!\top}\Pi)=0$,
leaving $\Pi g\kappa_{\text{at}}\Pi=\frac{c_g\gamma}{N}\Pi$, which is
$\frac{\gamma}{4N}\Pi$ at $c_g=\tfrac14$. $\blacksquare$

**Why this settles the exponent.** VL's diagnostic (7.5) reads
$g^{-1}=\bigl(g^{-1}\kappa g^{-1}\bigr)^{a/(2a-1)}$, and he spells out
the two readable ends: $a=0\Rightarrow g^{-1}=I$ and $a=1\Rightarrow
g^{-1}=g^{-1}\kappa g^{-1}$. The theorem is the second of these, with a
constant. The constant carries units of rate — $\kappa$ has dimensions
of (state)$^2$/time while $g$ does not — so it fixes the time unit
exactly as his (6.8) implicitly does; the *functional* relation is
linear, which is what $a=1$ asserts.

*Machine check*: for 200 random states the spectrum of
$\Pi g\kappa_{\text{at}}\Pi$ is constant $=0.035714285714$
($=1/28=\gamma/4N$ at $\gamma=1$, $N=7$) with maximal spread
$8.33\times10^{-17}$; and
$\max\lvert\kappa^{\uparrow\uparrow}_{\text{at}}-\frac{\gamma}{4N}
g^{-1}\rvert=1.73\times10^{-17}$.

### 4.1 What this predicts about data {#предсказание-о-данных}

Combine the theorem with VL's own maximum-entropy identity (his 4.7,
$g^{-1}=c$ where $c$ is the **static** covariance of the population):

$$
\kappa^{\uparrow\uparrow}\;=\;\frac{\gamma}{4N}\;c .
$$

*The covariance of temporal changes is proportional to the static
covariance of the population, with the same shape and a single scalar of
proportionality that is a pure rate.* In [V1]'s own terms both sides are
the single-trial multinomial covariance: the abundant, already-measured
object ($c$, his 7.1) and the never-measured object
($\kappa^{\uparrow\uparrow}$, his 7.4) are predicted to be the same
matrix up to one number. For $N=7$ that is a 20-parameter shape
prediction with one free scalar; for a real genome it is enormously
over-determined. This — not the constant — is the practically useful
content of the identity.

:::note How deep is this, honestly
As mathematics the two theorems above are elementary: for the
multinomial family the Fisher metric is the inverse of the single-trial
covariance, a standard fact of information geometry. No depth is claimed
for the computation. The content is the **forcing**: UHM leaves no
freedom in either factor — $g$ by Axiom 2, and the noise by the Lindblad
set being the classifier atoms (T-41g–i) rather than a modelling choice.
VL's §4 imposes $g^{-1}=c$ by a maximum-entropy argument on the
population covariance (his 4.3–4.7: isotropic constraint $\Rightarrow$
spherical distribution $\Rightarrow$ covariance $\propto$ identity in
local coordinates); here the same identity emerges for the *dynamical*
noise without being postulated. The results in §5–§7 are not elementary
and carry the new content.
:::

> **UHM proves, as a dynamical theorem, the identity that VL adopts as a
> maximum-entropy postulate — and simultaneously fixes the learning
> exponent that VL leaves open.**

---

## 5. The Fano correction is the universal factor 11/9 {#теорема-фано-множитель}

:::tip Theorem [Т]
With the full canonical dissipator (atomic + Fano) at matched
per-channel rate $\gamma/N$, for **every** state,

$$
\frac{\operatorname{Tr}\!\left(g\,\kappa_{\text{full}}\right)}
{\operatorname{Tr}\!\left(g\,\kappa_{\text{at}}\right)}
\;=\; 1+\frac29 \;=\; \frac{11}{9},
$$

independently of $\lambda$ and of $c_g$. Equivalently: the block layer
carries exactly $2/11$ of the total metric-weighted noise, at every
state. In Bures normalisation $\operatorname{Tr}(g\kappa_{\text{at}})=
\frac{3\gamma}{14}$ and $\operatorname{Tr}(g\kappa_{\text{full}})=
\frac{11\gamma}{42}$.
:::

**Proof.** For a Fano line $p$ with $s_p=\sum_{i\in p}\lambda_i$:
$L_p\rho L_p^\dagger=\tfrac13\operatorname{diag}(\lambda_i[i\in p])$,
$\operatorname{Tr}=s_p/3$, $p_e=\frac{\gamma dt}{N}\frac{s_p}{3}$, and
the post-jump vector is $u_p$ with $(u_p)_i=\lambda_i[i\in p]/s_p$.
Then

$$
\kappa_{\text{F}}=\frac{\gamma}{N}\sum_{p}\frac{s_p}{3}
\,(u_p-\lambda)(u_p-\lambda)^{\!\top}.
$$

The metric-weighted quadratic form evaluates in closed form:

$$
(u_p-\lambda)^{\!\top}g\,(u_p-\lambda)
=c_g\Bigl[\sum_{i\in p}\lambda_i\Bigl(\tfrac1{s_p}-1\Bigr)^{2}
+\sum_{i\notin p}\lambda_i\Bigr]
=c_g\Bigl[\frac{(1-s_p)^2}{s_p}+(1-s_p)\Bigr]
=\frac{c_g(1-s_p)}{s_p}.
$$

Hence

$$
\operatorname{Tr}(g\kappa_{\text F})
=\frac{\gamma}{N}\sum_p\frac{s_p}{3}\cdot\frac{c_g(1-s_p)}{s_p}
=\frac{c_g\gamma}{3N}\sum_p(1-s_p)
=\frac{c_g\gamma}{3N}\bigl(b-r\bigr),
$$

where $b=7$ is the number of lines and $\sum_p s_p=r\sum_i\lambda_i=r=3$
because every point lies on exactly $r=3$ lines (BIBD$(7,3,1)$).
Therefore $\operatorname{Tr}(g\kappa_{\text F})=\frac{4c_g\gamma}{21}$,
while $\operatorname{Tr}(g\kappa_{\text{at}})=\frac{c_g\gamma}{N}(N-1)=
\frac{18c_g\gamma}{21}$. The ratio is $4/18=2/9$ and the total factor
$11/9$, with **no dependence on $\lambda$ and no dependence on $c_g$**.
$\blacksquare$

*Machine check*: 300 random states, ratio
$\in[1.222222222222,\,1.222222222222]$, deviation from $11/9$ at most
$4.4\times10^{-16}$; block fraction $2/11=0.181818181818$.

**General BIBD form.** For a design $(v,k,1)$ on $v=N$ points with $b$
blocks and replication $r$, the same computation gives

$$
\frac{\operatorname{Tr}(g\kappa_{\text{blocks}})}
{\operatorname{Tr}(g\kappa_{\text{at}})}=\frac{b-r}{k\,(v-1)} .
$$

Verified on three designs — $\mathrm{PG}(2,2)\,(7,3,1)\to\frac{7-3}
{3\cdot6}=\frac29$ (dev. $1.4\times10^{-16}$),
$\mathrm{AG}(2,3)\,(9,3,1)\to\frac13$ (dev. $1.7\times10^{-16}$),
$\mathrm{PG}(2,3)\,(13,4,1)\to\frac3{16}$ (dev. $5.6\times10^{-17}$).
One caveat the general form hides: the block layer is separately
trace-preserving only when $r=k$, since $\sum_p L_p^\dagger L_p=
\frac rk I$. This holds for $(7,3,1)$ and $(13,4,1)$ but fails for
$(9,3,1)$, where $r/k=4/3$ and the channel must be renormalised. The
Fano plane is thus doubly distinguished: optimal *and* self-normalising.

**Anisotropy.** While the trace ratio is universal, the *spectrum* of
$\Pi g\kappa_{\text{full}}\Pi$ is isotropic only at the maximally mixed
state, where it equals $\frac{11}{9}\cdot\frac{\gamma}{4N}$ in all six
directions. Away from it the spectrum spreads, in units of
$\gamma/4N$:

| state | spectrum | anisotropy |
|---|---|---|
| $I/7$ | $\{\tfrac{11}9\}^{\times6}$ | $1.0000$ |
| $\lambda=(\tfrac12,\tfrac1{12}^{\times6})$, $P=\tfrac7{24}$ | $\{\tfrac{13}{12},\tfrac{13}{12},\tfrac{11}9,\tfrac{11}9,\tfrac{11}9,\tfrac32\}$ | $1.3846$ |
| $P=\tfrac5{14}$ (window centre), $\lambda=(\tfrac47,\tfrac1{14}^{\times6})$ | $\{\tfrac{16}{15},\tfrac{16}{15},\tfrac{11}9,\tfrac{11}9,\tfrac{11}9,\tfrac{23}{15}\}$ | $1.4375$ |

The first row is checked to $1.78\times10^{-15}$ against the exact
fractions; each spectrum sums to $6\cdot\frac{11}9=\frac{22}3$, as the
universal trace requires. **The Fano layer is therefore what turns exact
natural gradient into an anisotropic, preconditioned natural
gradient** — the structural analogue of the adaptive preconditioners
(Adam/AdaBelief, his 6.9) that VL associates with $a=\tfrac12$, but
obtained without leaving $a=1$.

**Per-axis refinement: the third-point screen (2026-08-07).** The block
layer does one more exact thing that the trace cannot see: it *screens*
the third point of each line. The sensitivity of the population
covariance $\kappa_{ij}$ to $\lambda_x$ is suppressed, relative to every
axis outside the pair, precisely when $x$ is the third point of the line
through $(i,j)$ — at $I/7$ by exactly $\gamma/189$, analytic and
machine-confirmed to six digits in both $\kappa_{OE}$ and
$\kappa_{OU}$; for an abstract line set the screen moves to *its* third
points, as labelling invariance demands. On random states the third
point is the least-sensitive outside axis in $\approx92\%$ of cases.
Corpus statement and proof sketch:
[the $\kappa_0$ suppression corollary](/docs/physics/gauge-symmetry/fano-selection-rules#каппа-по-подавленным);
instrument `shadow_marks.py` alongside the reproduction script.


---

## 6. Noise magnitude is fixed by purity {#теорема-шум-чистота}

:::tip Theorem [Т]
$\operatorname{Tr}\kappa_{\text{at}}=\frac{\gamma}{N}(1-P)$ and
$\operatorname{Tr}\kappa_{\text{at}}^2=\frac{\gamma^2}{N^2}
(P+P^2-2S_3)$, where $P=\operatorname{Tr}\rho^2$ is the purity and
$S_3=\sum_i\lambda_i^3$. Neither depends on the metric normalisation.
:::

**Proof.** Immediate from §3:
$\operatorname{Tr}[\operatorname{diag}\lambda-\lambda\lambda^{\!\top}]=
\sum_i\lambda_i-\sum_i\lambda_i^2=1-P$; and
$\operatorname{Tr}[(\operatorname{diag}\lambda-\lambda\lambda^{\!\top})^2]
=P-2S_3+P^2$ by expanding the square and using
$\operatorname{Tr}(\operatorname{diag}\lambda\cdot\lambda\lambda^{\!\top})
=S_3$ and $\operatorname{Tr}(\lambda\lambda^{\!\top}\lambda
\lambda^{\!\top})=P^2$. $\blacksquare$

Consequences inside the UHM viability structure (all with $\gamma=1$,
$N=7$):

| State | $P$ | $\operatorname{Tr}\kappa_{\text{at}}$ |
|---|---|---|
| maximally mixed $I/7$ | $1/7$ | $6/49=0.122449$ |
| viability threshold $P_{\text{crit}}$ | $2/7$ | $5/49=0.102041$ |
| centre of the conscious window | $5/14$ | $9/98=0.091837$ |
| upper edge of the window | $3/7$ | $4/49=0.081633$ |

So the conscious window $P\in(2/7,3/7]$ — derived in UHM from
independent considerations (T-124) — corresponds to a **learning-noise
band** $\operatorname{Tr}\kappa\in[4\gamma/49,\,5\gamma/49)$. In VL
language: a viable learner is one whose gradient noise sits in a narrow
band; too much noise (high entropy, $P\to1/7$) and structure dissolves;
too little ($P\to1$) and the learner freezes at a fixed point. This is
the same "Goldilocks" statement VL conjectures for the origin of life,
but here it is a *derived* interval with explicit endpoints — and, being
metric-free, it is the most directly testable of the predictions.

---

## 7. Zero drift, and the sector split {#теорема-секторное-расщепление}

### 7.1 The dissipator is pure noise on populations {#нулевой-снос}

:::tip Theorem [Т]
The canonical dissipator annihilates every diagonal state:
$\mathcal D_\Omega[\operatorname{diag}\lambda]=0$, equivalently
$\sum_e p_e\Delta_e=0$. Hence the second moment *is* the centred
covariance of his (7.4), and all population drift is carried by
$\mathcal R$.
:::

**Proof.** $\sum_k L_k\rho L_k^\dagger=\operatorname{diag}\lambda=\rho$
and $\sum_p L_p\rho L_p^\dagger=\tfrac13\sum_p
\operatorname{diag}(\lambda_i[i\in p])=\tfrac13\cdot3\lambda=\rho$,
since each point lies on $r=3$ lines; and $\sum_k\operatorname{Tr}
(L_k\rho L_k^\dagger)=\sum_p\operatorname{Tr}(L_p\rho L_p^\dagger)=1$.
So $\sum_e p_e\Delta_e=\frac{\gamma}{N}(2\rho-2\rho)=0$. $\blacksquare$

*Machine check*: $\max\lvert\sum_e p_e\Delta_e\rvert=3.64\times10^{-17}$
over 200 states, and $\max\lvert\mathcal L_{\text{full}}
[\operatorname{diag}\lambda]\rvert=0.00$ exactly.

This is the clean structural match to VL's Langevin split: his (6.3)
carries the deterministic ascent and (6.5)–(6.6) the zero-mean noise. In
UHM the split is not modelled but forced by the triad — $\mathcal R$ is
the drift, $\mathcal D_\Omega$ is the noise, and they do not overlap on
the population sector.

### 7.2 What the Fano layer is, and is not {#область-действия-фано}

:::tip Theorem [Т]
The full canonical dissipator equals total dephasing at rate
$5\gamma/21$: its $49\times49$ generator has spectrum exactly
$\{0^{\times7},(-5\gamma/21)^{\times42}\}$, and it coincides identically
with the atomic-only dissipator at rescaled rate $5\gamma/3$.
:::

*Machine check*: atomic spectrum
$\{0^{\times7},(-\gamma/7)^{\times42}\}$, full spectrum
$\{0^{\times7},(-5\gamma/21)^{\times42}\}$, and
$\max\lvert\mathcal L_{\text{full}}(\gamma)-\mathcal L_{\text{at}}
(5\gamma/3)\rvert=2.78\times10^{-17}$.

:::warning $\kappa$ is not unravelling-invariant, and the Fano layer is invisible in the master equation
Two different Kraus resolutions of the *same* generator give different
$\kappa$. So $\kappa$ is well defined only *relative to* the canonical
Kraus resolution, and that the classifier atoms and the seven Fano
projectors are the physical channels is an **ontological commitment** of
UHM (L-unification, T-41g–i), not a consequence of the dynamics. A
reader who rejects that commitment keeps §3, §4, §6 and §7.1, and loses
§5.

The same fact fixes the correct operational statement of the $11/9$
factor, which any experiment must respect:

- at matched **per-channel** rate $\gamma/N$: ratio $=11/9$ — this is
  the comparison of a seven-channel and a fourteen-channel holon;
- at matched **generator** (i.e. matched observed decoherence rate,
  $\gamma_{\text{at}}=5\gamma/3$): ratio $=11/15$ — this is the
  comparison of two resolutions of one physical process.

Both are exact. Quoting $11/9$ for the second comparison would be wrong.
:::

### 7.3 The sector split {#расщепление-секторов}

:::tip Theorem [Т]
All fourteen canonical Lindblad operators are diagonal in the classifier
basis. Hence **on the decohered manifold** (diagonal $\rho$) every
increment $\Delta_e$ is diagonal and $\kappa^{\text{coh}}=0$ exactly,
while coherences contract deterministically at
$\lambda_{\text{deco}}=\frac{5\gamma}{3N}=\frac{5\gamma}{21}$ (T-59,
confirmed by the $49\times49$ superoperator above).
:::

**Proof.** $L_k=|k\rangle\langle k|$ and $L_p=\Pi_p/\sqrt3$ are
diagonal; conjugation of a diagonal $\rho$ by a diagonal operator is
diagonal; hence $\rho_e$ and $\Delta_e$ are diagonal, so all
contributions lie in the population sector. $\blacksquare$

*Off the decohered manifold this is only approximate*, and the honest
statement is quadratic suppression rather than identical vanishing: with
coherences of size $c$ inserted into an otherwise diagonal state,
$\max\lvert\kappa^{\text{coh}}\rvert=1.079\times10^{-4}$ at $c=0.02$ and
$2.698\times10^{-3}$ at $c=0.10$ — a ratio of $25.0$ for a factor $5$ in
$c$, i.e. exactly $O(c^2)$. Since the coherences themselves decay at
$5\gamma/21$, $\kappa^{\text{coh}}$ decays at $10\gamma/21$. The
decohered manifold is the attractor, so $\kappa^{\text{coh}}\to0$
always; it is not identically zero everywhere.

**Interpretation, and a genuine tension with VL.** UHM predicts a
**two-sector structure**: a *population sector* with stochastic,
natural-gradient learning ($a=1$, anisotropic through Fano), and a
*coherence sector* that is noiseless and purely deterministic at
$5\gamma/21$.

VL calls $a=1$ the "quantum regime" because it yields Schrödinger-like
dynamics on the trainables from a discrete shift symmetry [V2]. In UHM
the $a=1$ sector is the *population* (diagonal) sector — the classical
degrees of freedom — while literal quantum coherence lives in the sector
where $\kappa$ vanishes. These are two different senses of "quantum",
and conflating them would be the easiest way to overclaim agreement.
What UHM actually says is that both are present and complementary:
emergent unitary $\tau$-dynamics on populations (Page–Wootters,
T-38b/T-87) *and* a strictly separate coherence sector. That is a
refinement of his dichotomy rather than a restatement of it, and the
sector split is the part that is independently falsifiable.

---

## 8. Effective rank for a holon {#эффективный-ранг}

VL notes that empirical genotype covariance spectra decay as a power law
with effective rank $r_{\text{eff}}=\zeta(\alpha)^2/\zeta(2\alpha)$ (his
7.3) of order $10^2$ against $\dim(g)\sim10^9$. For a holon the same
quantity has an exact closed form. With $r_{\text{eff}}=
(\operatorname{Tr}\kappa)^2/\operatorname{Tr}\kappa^2$ over the
population sector, §6 gives immediately

$$
r_{\text{eff}}=\frac{(1-P)^2}{P+P^2-2S_3},\qquad S_3=\sum_i\lambda_i^3 ,
$$

verified to $6.66\times10^{-15}$ against the numerical spectrum on 300
random states.

:::warning The effective rank is not a function of purity alone
This is a two-moment identity, and it makes explicit that
$r_{\text{eff}}$ depends on $S_3$ as well as $P$. At equal purity:

| $P$ | one dominant $+$ six equal | two dominant $+$ five equal |
|---|---|---|
| $1/7$ | $6.0000$ (maximum, $=N-1$) | — |
| $2/7$ | $4.2247$ | $3.0854$ |
| $5/14$ | $27/7=3.8571$ | $2.1858$ |
| $3/7$ | $3.5931$ | $1.5047$ |

A search over all $\lambda$ with $P\in(2/7,3/7]$ gives
$r_{\text{eff}}\in[1.4719,\,4.1262]$, the upper end rising to $4.2247$
as $P\to2/7^+$ along the one-dominant family. So the viable band
compresses $r_{\text{eff}}$ to $\approx60$–$70\%$ of maximum *only along
the one-dominant family*; over the whole window it can fall to
$\approx25\%$. The falsifiable statement is the closed form, which is
stronger than any interval: it ties two measured moments of $\kappa$ to
two measured moments of the state, with no free parameter beyond
$\gamma$.
:::

---

## 9. Predictions and how to falsify them {#предсказания}

All statements below are consequences of the results above; none is
fitted. The column "needs $g$?" matters in practice: predictions that do
not require estimating a metric are immune to the normalisation question
of §2.1 and are much easier to measure.

| # | Prediction | Value | Needs $g$? | Test |
|---|---|---|---|---|
| **P1** | Learning exponent of a viable holon | $a=1$ exactly (natural gradient), **not** $a=\tfrac12$ | no | Sphericity of $\kappa^{\uparrow\uparrow}$ — §9.1 |
| **P2** | Shape identity with the static covariance | $\kappa^{\uparrow\uparrow}=\frac{\gamma}{4N}c$ (with his 4.7) | no | Compare the covariance of temporal changes with the static population covariance; predicted equal up to one scalar |
| **P3** | Universal Fano factor | $11/9$ at matched per-channel rate; $11/15$ at matched generator; block fraction $2/11$ | yes | Resolve the same process at site and block level, holding the declared normalisation fixed |
| **P4** | Noise–purity law | $\operatorname{Tr}\kappa=\frac{\gamma}{N}(1-P)$; viable band $[4\gamma/49,5\gamma/49)$ | no | Zero-intercept regression of $\operatorname{Tr}\hat\kappa$ on $1-\hat P$; slope $=\gamma/N$ |
| **P5** | Second moment / effective rank | $r_{\text{eff}}=\frac{(1-P)^2}{P+P^2-2S_3}$ exactly | no | Two moments of $\hat\kappa$ against two moments of the state |
| **P6** | Sector split | $\kappa^{\text{coh}}=0$ on the decohered manifold, $O(\lVert\rho_{\text{coh}}\rVert^2)$ off it; coherences decay at $5\gamma/21$ | no | Interferometry / process tomography |
| **P7** | Absolute normalisation | $\operatorname{Tr}(g\kappa_{\text{full}})=\frac{11\gamma}{42}$ (Bures) or $\frac{22\gamma}{21}$ (SLD-QFI) | yes | Fixes $\gamma$ from one measurement, then over-determines the rest |
| **P8** | Network topology of the "cellular" layer | For $N=7$ with complete pairwise coverage the coordinating design is **forced** to be $\mathrm{PG}(2,2)$; it is also the design for which the block layer is self-normalising ($r=k$) | no | Any $N=7$ architecture claiming optimal pairwise coordination must reproduce Fano incidence |

### 9.1 The metric-free discriminator, and the sample size it needs {#дискриминатор}

VL's (7.5) degenerates at $a=\tfrac12$: the exponent $a/(2a-1)$
diverges, and indeed $\kappa^{\uparrow\uparrow}=g^{1/a-2}=I$ carries no
information about $g$ at all. That degeneracy is exactly what makes a
clean test possible, because the two hypotheses make *opposite* shape
claims about a single measured object:

- $a=\tfrac12$ $\Longrightarrow$ $\kappa^{\uparrow\uparrow}$ is
  **spherical** on $T$ (all six eigenvalues equal);
- $a=1$ $\Longrightarrow$ $\kappa^{\uparrow\uparrow}\propto
  \operatorname{diag}\lambda-\lambda\lambda^{\!\top}$, fully computable
  from the measured $\lambda$.

Neither requires estimating $g$. The statistic is the classical
sphericity (Mauchly) likelihood ratio on the whitened estimate,

$$
T=-M\ln\frac{\det{}_T A}{\bigl(\operatorname{Tr}A/6\bigr)^{6}},
\qquad A=\Sigma_0^{-1/2}\,\hat\kappa\,\Sigma_0^{-1/2},
\qquad \mathrm{df}=\tfrac{d(d+1)}2-1=20 ,
$$

with $\Sigma_0=\Pi$ to test $a=\tfrac12$ and $\Sigma_0=
\operatorname{diag}\lambda-\lambda\lambda^{\!\top}$ to test $a=1$. The
theory supplies the separating power exactly:
$\Delta(\lambda)=6\ln(\text{AM}/\text{GM})$ of the eigenvalues of
$\kappa^{\uparrow\uparrow}$, giving $\Delta=0$ at $I/7$ and $0.8159$,
$1.0465$, $1.2384$ at $P=2/7$, $5/14$, $3/7$.

:::danger Two practical warnings, both measured rather than asserted
**The asymptotic sample size is a mirage.** The naive
$M\gtrsim\text{ncp}/\Delta$ gives $M\gtrsim17$–$26$, but at those sizes
the $\chi^2_{20}$ calibration fails badly: the simulated size of a
nominal $5\%$ test is $10.0\%$ at $M=25$, $8.0\%$ at $M=50$, $6.1\%$ at
$M=100$, $5.5\%$ at $M=200$. Power at $M=100$ is $100\%$ everywhere in
the window ($77.3\%$, $88.2\%$, $93.1\%$ at $M=25$ for $P=2/7$, $5/14$,
$3/7$). **Use $M\approx100$ independent windows**; below $M\approx50$
the test is anti-conservative and should not be reported.

**Increments must be aggregated.** A single idealised jump has only
seven outcomes, so $\hat\kappa=\operatorname{diag}\hat p-
\hat p\lambda^{\!\top}-\lambda\hat p^{\!\top}+\lambda\lambda^{\!\top}$
is parametrised by six numbers rather than twenty-one and is not
Wishart; the $\mathrm{df}=20$ calibration does not apply to it.
Aggregate over windows with $\Lambda\Delta t\gg1$, where
$\Lambda=2\gamma/N$ is the total jump rate, so the central limit theorem
applies; the window covariance is then exactly $\kappa\,\Delta t$
(Campbell). Because $\kappa$ is state-dependent, the window must sit
between two timescales, $1/\Lambda\ll\Delta t\ll\tau_{\text{drift}}$;
whether such a window exists in a given system is an empirical question
about the ratio of regeneration to dissipation rates.
:::

Note finally that the discriminating power **vanishes at the maximally
mixed state** ($\Delta=0$): there, $a=1$ and $a=\tfrac12$ are
indistinguishable in principle. The test needs a state away from
uniformity — and the viability window $P\in(2/7,3/7]$ is precisely where
UHM says a conscious holon sits. The theory therefore predicts that the
systems it claims as holons are exactly the systems in which its own
central claim is measurable.

**The sharpest disagreement.** VL conjectures that biological
complexity — and possibly the origin of life — corresponds to the
intermediate regime $a=\tfrac12$, the "efficient learning" regime of
Adam/AdaBelief (his 6.9). UHM says: a viable learner sits at $a=1$ with
an anisotropic preconditioner supplied by the Fano layer, and its
sophistication is carried by the *anisotropy* and the *purity window*,
not by the exponent. Both claims live in the same measurable object;
§9.1 decides between them with of order a hundred windows of data.

:::note Level-matching caveat
The derivation is at the level of a holon's internal state dynamics.
Applying it to population genetics assumes that an evolving population
is itself a holon — which is exactly what UHM's scale-invariance theorem
(T-72, with contraction $c_F=1/3$) asserts, but which remains a bridge
assumption **[И]** rather than a theorem about biology. If the
identification is rejected, P1 still stands for physical holons and for
engineered learning systems built on the UHM core.
:::

---

## 10. What each framework gives the other {#взаимный-вклад}

**UHM → VL.**

1. *Determination of the free function.* $g(\kappa)$ is no longer a
   modelling choice: $a=1$ with the exact constants above.
2. *Derivation of the maxent postulate's dynamical counterpart.* The
   relation $g^{-1}\propto\kappa^{\uparrow\uparrow}$ — his $a=1$
   condition (7.5), for him a modelling choice among three — is here a
   theorem. It is the *dynamical* analogue of the *static* identity
   $g^{-1}=c$ that his §4 obtains by a maximum-entropy argument;
   granting that static identity as well, the two together give the
   sharp form $\kappa^{\uparrow\uparrow}=\frac{\gamma}{4N}c$, which
   relates a routinely measured object to an unmeasured one.
3. *A preferred basis.* VL inherits einselection's open question ("why
   this interaction?"); UHM fixes the basis as the atoms of the subobject
   classifier, rigid up to $G_2=\operatorname{Aut}(\mathbb O)$ (T-42a),
   with the seven directions functionally unique (7/7 minimality).
4. *A forced network.* The "cellular network" that coordinates agents
   is, at $N=7$ with complete pairwise coverage and optimal block size,
   uniquely the Fano plane (T-41c, T-41i) — which is moreover the case
   $r=k$ in which the block layer needs no renormalisation.
5. *A ceiling on self-reference.* The $P_{\text{crit}}$ ladder across
   levels gives $\mathrm{SAD}_{\max}=3$: a self-learning system cannot
   nest reflection indefinitely — a structural limit absent from VL.
6. *A reason why learning never completes.* Lawvere incompleteness
   (T-55: $\mathrm{Th}_{\text{UHM}}\subsetneq\Omega$) implies a permanent
   gap between the state and its self-model; in UHM this gap is the
   source of a positive vacuum energy (T-71). A self-learning universe
   is, provably, a universe that cannot finish learning itself.

**VL → UHM.**

1. *An operational reading of $\mathcal R$*: regeneration as covariant
   gradient ascent on fitness, with the loss identified as negative
   Malthusian fitness — a bridge to measurable biology. UHM returns the
   favour by proving the drift/noise split (§7.1) that his Langevin form
   assumes.
2. *An experimental target*: his proposal to measure the covariance of
   temporal changes is precisely the measurement that tests P1–P5, and
   his (7.5) supplies the criterion in a form UHM can meet exactly.
3. *A macroscopic derivation route*: the cell/agent split of the
   *Self-Learning Universe* (memory-cost vs processing-cost) is a
   physically motivated variational principle whose UHM counterpart —
   Gap curvature $\lVert\mathrm{Curv}\rVert^2=\omega_0^2
   \lVert\gamma_{ij}\rVert^2\mathrm{Gap}^2$ (T-73) and $V_{\text{Gap}}$
   from the spectral action (T-74) — can be compared term by term.

---

## 11. Reproducibility {#воспроизводимость}

Every number on this page is printed by
`internal/vanchurin-bridge/full_predictions.py` (deterministic, seeds
20260806 / 20260807 / 20260808; NumPy + SciPy); the metric
normalisation runs as its own §0 block inside the same script, and the
per-axis third-point screen of §5 is printed by its companion
`shadow_marks.py` (seeds 20260807 / 20260808).

| § | Check | Result |
|---|---|---|
| 0 | Bures $=\tfrac14$ Fisher on the commuting sector | $0.2499727756$ at $\varepsilon=10^{-5}$ |
| 1 | Multinomial identity, 2000 random states | $2.78\times10^{-17}$ |
| 2 | Natural-gradient identity, 200 random states; both normalisations; his (7.5) | spread $8.33\times10^{-17}$; $1.73\times10^{-17}$ |
| 3 | Fano factor, 300 random states; anisotropy; three BIBDs | $4.4\times10^{-16}$; $1.78\times10^{-15}$; $\le1.7\times10^{-16}$ |
| 4 | Both noise moments at four reference states | exact match |
| 5 | $49\times49$ generator; $\mathcal L_{\text{full}}(\gamma)=\mathcal L_{\text{at}}(5\gamma/3)$; $\kappa^{\text{coh}}$ on and off the diagonal | $\{0^{\times7},(-5\gamma/21)^{\times42}\}$; $2.78\times10^{-17}$; $O(c^2)$ |
| 6 | $r_{\text{eff}}$ closed form; window range | $6.66\times10^{-15}$; $[1.4719,4.1262]$ |
| 7 | Zero drift | $3.64\times10^{-17}$; $0.00$ |
| 8 | Sphericity test: separating power, simulated size and power; Campbell window identity | $M\approx100$ |
| 9 | Third-point screen (`shadow_marks.py`): $I/7$ gap $\equiv\gamma/189$; outside-axis argmin share | six digits; $91$–$96\%$ |

A condensed statement of this bridge, set against Deutsch's many-worlds
programme, is §2.9 of [Many-Worlds (Everett–Deutsch) and
UHM](/docs/physics/quantum-mechanics/many-worlds).

Corpus cross-references: T-41 (Fano channel family), T-42a
($G_2$-rigidity), T-55 (Lawvere incompleteness), T-57 (triadic
completeness), T-59 ($\lambda_{\text{deco}}=5\gamma/21$), T-71 (vacuum
energy), T-72 (scale invariance), T-73/T-74 (Gap curvature, spectral
action), T-87 (A5 derivable), T-124 (conscious window), T-187 (why
Bures). Registry rows: T-293, T-294, T-295; the per-axis screen lives under T-298.

---

## 12. Summary {#резюме}

Vanchurin's framework asks: *which learning algorithm does nature
implement?* UHM answers, without adjustable parameters:

$$
\kappa^{\uparrow\uparrow}_{\text{at}}=\frac{\gamma}{4N}\,g^{-1}
\;\Longrightarrow\;
a=1,
\qquad
\frac{\operatorname{Tr}(g\kappa_{\text{full}})}
{\operatorname{Tr}(g\kappa_{\text{at}})}=\frac{11}{9},
\qquad
\operatorname{Tr}\kappa=\frac{\gamma}{N}(1-P),
$$

$$
r_{\text{eff}}=\frac{(1-P)^2}{P+P^2-2S_3},
\qquad
\kappa^{\text{coh}}\big|_{\text{diag}}=0 .
$$

Nature — at the level of a viable holon — performs **natural gradient
descent on the Bures geometry, preconditioned by the Fano design, in a
purity band that keeps its effective rank well below maximum, on a
sector strictly complementary to the one where quantum coherence
lives.**

The first of these is measurable without ever estimating a metric, and
needs about a hundred windows of data. If the covariance of temporal
changes is ever measured the way Vanchurin proposes, these are the
numbers to compare against.
