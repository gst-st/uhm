---
sidebar_position: 3
title: "Freedom of Will"
description: "Agency, effective alternatives, self-revision and the limits of mathematical measures"
slug: /consciousness/ethics-meaning/freedom
---

# Freedom, agency and the scope of the formal score

UHM reads agency within one world as an ontological and philosophical programme [I]. Its mathematical objects can model alternatives, policies and resources; they do not by themselves settle the philosophical debate about free will. Determinism, prediction, controllability and subjective choice are different questions.

## Terminality and alternatives

A terminal object satisfies $\operatorname{Map}(X,1)\simeq *$. This is a universal property in the selected category; it does not specify a physical goal, relaxation process or unique future. A contractible mapping space may be represented by many point sets, including a singleton. Their cardinality changes with the presentation, so it cannot define invariant freedom or prove a multiplicity of physically available trajectories.

For a locally Lipschitz autonomous vector field, the trajectory from a fixed initial state is unique. Controlled dynamics $\dot x=F(x,u)$ instead has trajectories indexed by admissible policies $u$. Meaningful alternatives require specifying the control set, observations, disturbances, resource constraints and outcome criterion. A category's higher morphisms do not supply those controls.

## A chosen Hessian score {#количественная-мера}

Let $V$ be a $C^2$ potential on a $d$-dimensional manifold, and let $x_*$ be a critical point. Define

$$
\mathrm{Freedom}_V(x_*):=1+\dim\ker\operatorname{Hess}_{x_*}V.
$$

This is a definition [D]. Rank-nullity gives $1\le\mathrm{Freedom}_V\le d+1$ [T]. At a critical point an invertible coordinate change transforms the Hessian by congruence, so its nullity is invariant. A symmetry preserving $V$ preserves the score at corresponding critical points. Neither invariance nor a potential is supplied by the name of a group alone.

**T-89 [T under the Morse–Bott hypothesis].** If the critical set is a smooth manifold and $V$ is Morse–Bott there, its tangent space is exactly the Hessian kernel. Thus the score is one plus its local dimension. Without that hypothesis, higher-order terms can remove all distinct neighbouring equilibria despite zero quadratic modes.

For example $V(x)=x^4$ has zero Hessian at 0 but only one local minimum. Conversely $V(x)=\|x\|^2$ is rotationally invariant and has a positive Hessian at its symmetric origin: symmetry does not force a zero Hessian. A saddle's negative directions are not zero modes, and a degenerate minimum need not have a positive-definite Hessian.

The trace-one Hermitian affine hull in dimension 7 has real dimension 48. Its full-rank state interior is a smooth domain, giving the score bound 49 there. At rank-deficient states the positive state space has a boundary; a smooth stratum or ambient extension must be specified before applying this Hessian argument. A separate six-dimensional diagonal model gives bound 7. The values at $I/7$, a pure anchor or a stationary state depend on the specified potential and domain; there are no universal values 7, 7, 1.

## What the score does not establish

No general CPTP monotonicity follows. A channel acts on states; a Hessian belongs to a chosen scalar function and tangent domain. A comparison requires specifying how both are transported. Even the Euclidean potential $V(x)=\|x\|^4$ has a zero Hessian at its origin and a positive Hessian elsewhere; replacing an input by that origin can increase nullity. Noninvertible channels need not preserve tangent dimension.

The logarithm $\log\mathrm{Freedom}_V$ is another selected scalar [D]. It is not a thermodynamic entropy without a supplied state-counting or probability model. Hessian nullity is not the number of trajectories, available choices, degrees of phenomenal agency or a clinical measure. Purity, Gap and a capability certificate do not determine it without a bridge.

## Effective alternatives under constraints {#operational-agency}

A positive account of agency begins with what an agent can actually change. In a finite-horizon model specify

$$
x_{t+1}=F(x_t,u_t,w_t),\qquad y_t=O(x_t),\qquad
u_t=\pi(y_0,u_0,\ldots,y_t).
$$

Here $x_t$ includes the relevant physical and memory state; $w_t$ is a disturbance; the policy $\pi$ uses only the available history. Fix an initial state, horizon $H$, allowed disturbance sequences $\mathsf W_H$, constraint set $K$, outcome readout $g:S\to Y$ and a time/resource budget $B$. Assume the declared executions exist. Let $\Pi_B$ contain precisely the permitted policies whose executions respect $K$ and the budget for every $w\in\mathsf W_H$. Policy computation and observation costs belong in that budget when material.

Each policy defines a **response function**, not just one favourable outcome:

$$
r_\pi:\mathsf W_H\to Y,\qquad
r_\pi(w)=g(x_H^{\pi,w}),\qquad
\mathcal A_B=\{r_\pi:\pi\in\Pi_B\}.
$$

The **operational repertoire** $\mathcal A_B$ is a definition **[D]**. Two policies are equivalent here exactly when they have the same response for every declared disturbance. More syntactic programs need not mean more effective alternatives. Both the observations and the outcome readout can hide distinctions; changing either changes the question.

**Expansion theorem [T].** If all other data are fixed and $\Pi_B\subseteq\Pi_{B'}$, then $\mathcal A_B\subseteq\mathcal A_{B'}$. For a fixed bounded utility $J:Y\to\mathbb R$, nonempty policy sets and nonempty $\mathsf W_H$,

$$
\sup_{\pi\in\Pi_B}\inf_{w\in\mathsf W_H}J(r_\pi(w))
\le
\sup_{\pi\in\Pi_{B'}}\inf_{w\in\mathsf W_H}J(r_\pi(w)).
$$

*Proof.* Every previously permitted policy remains available and has the same response. The supremum over a larger set cannot be smaller. $\square$

This gives a precise sense in which added resources or access can increase agency. Strict improvement requires a new response or a better guaranteed outcome; it does not follow merely from a larger budget. Richer observations preserve the old repertoire only when the old policy can be implemented by forgetting the extra observations within the permitted cost. Utility and constraints are declared evaluative premises, not values derived from set inclusion.

For example, two differently written policies implementing the same action at every reachable history add no response. A newly available intervention that changes an independently measured outcome may add one. A thermostat can also have distinct responses: the definition does not by itself establish intention, responsibility or experience.

## Self-revision and Autogeny {#self-revision}

Autogeny makes a further question explicit: can the agent revise the mechanism by which it forms and executes policies while preserving specified obligations? A useful record identifies the current program, its proposed replacement, the relevant invariants, the resources used and the observations that accept or reject the change. A fixed point of a self-map supplies none of this by itself.

A successful revision may expand $\mathcal A_B$, improve a declared objective or reduce the cost of an existing response. It can also narrow immediate choices to keep a long-term commitment. These are different improvements, so they should be reported separately. An optimisation result says which objective improved; deciding whether that objective deserves pursuit belongs to [ethical evaluation](/docs/consciousness/ethics-meaning/value-consciousness).

**Transport of a capability [T, conditional].** Suppose two implementations have a state map $h$, an action translation $a$, the same declared disturbances, related initial states and

$$
h(F_A(x,u,w))=F_B(h(x),a(u),w),\qquad
O_A(x)=O_B(h(x)),\qquad
g_A(x)=g_B(h(x)).
$$

Require these equalities on every relevant reachable transition, and require the translated policy to preserve the constraints and budget. The translation retains the source action history when the policy needs it; this memory and computation count towards the budget. It then has the same response function. Induction preserves the related states at each step; the last equality gives the same outcome.

This is the kind of commuting execution and resource contract used in Autogeny's typed realisations. It supplies a substantive comparison between embodiments. Equality after a forgetful projection, as in a selected MSFS/Diakrisis classification, does not automatically give an executable translation or preserve its price. The equations above, not the name of an equivalence, do the work.

A test on finitely many runs validates those runs. A universal certificate needs the stated transition proof or exhaustive verification of an effective finite model. Exhausting a search budget is not proof that the agent or architecture has no alternative.

## Responsibility and the experience of choice {#этические-следствия}

In a process account, reasons, commitments, attention and learned dispositions can be causally effective parts of the agent's state. To test responsiveness to reasons, specify an intervention on the represented information and check its consequences while controlling the other conditions. To study coercion, distinguish a restricted action set, altered information and threats that change the attainable consequences. These distinctions make responsibility discussable without reducing it to a Hessian or a random seed.

An ethical judgement additionally asks what the agent could know, which alternatives were accessible, what obligations applied and who would bear the consequences **[I/H]**. More control is not automatically more moral worth; lack of control does not erase another being's interests. A policy that can explain and revise its action provides evidence of a particular capability, not a proof that its explanation is true or its experience established.

Determinism is compatible with counterfactual comparisons between specified interventions. Stochasticity introduces possible outcomes, but possibility is not deliberate authorship. Neither fact settles the metaphysical dispute about free will. UHM can develop an embodied, resource-sensitive account of responsible action while keeping that philosophical commitment explicit **[I]**.

Spiritual practices may be investigated as changes in attention, habits, commitments and responsiveness. An association with reported autonomy or reduced compulsion requires its own observations. A spiritual concept of liberation is not thereby identified with $\dim\ker\operatorname{Hess}V$ or the cardinality of $\mathcal A_B$; see the [spiritual synthesis](/docs/consciousness/ethics-meaning/spiritual-synthesis).

## What this account makes possible {#что-мы-узнали}

The useful question becomes concrete: **which distinctions can this agent perceive, which policies can it execute, which outcomes can it affect, and which commitments survive self-revision?** The answer can grow through better representation, education, resources, cooperation and verifiable mechanisms of correction. Maintaining these possibilities across time connects agency with [meaning](/docs/consciousness/ethics-meaning/meaning) and [continuity](/docs/consciousness/ethics-meaning/death-continuity).

The [typed consequences](/docs/core/foundations/consequences#freedom-конечномерное) give the mathematical scope. The [control and viability model](/docs/core/dynamics/viability) specifies admissible actions and disturbances. The [premise ledger](/docs/reference/premises) separates these constructions from ontological interpretation.
