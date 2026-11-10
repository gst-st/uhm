---
sidebar_position: 2
title: Cross-entropy, feedback and variational inference
description: The exact minimum of the proposed feedback functional and the independent ingredients of variational inference.
---

## What the functional selects {#3-теорема-о-вариационной-характеризации}

Fix a density matrix $\Gamma$. For an output $\rho$ supported on its support, the von Neumann entropy and the quantum relative entropy satisfy

$$
S(\rho)+D(\rho\Vert\Gamma)=-\mathrm{Tr}(\rho\log\Gamma).
$$

The right side is linear in the output. Diagonalizing $\Gamma$ shows that its minimum is $-\log\lambda_{\max}(\Gamma)$. Equality holds precisely when the output is supported on the maximal eigenspace. The bound is attainable over all CPTP maps: discard the input and prepare any state on that space. This optimization cannot single out a feedback channel; even fixing the output for one input generally leaves its action on others undetermined. To select a channel one needs a task with independently specified observations, allowed resources and a rule for scoring different channels. [Resource cost of feedback](https://github.com/uhm-theory/holon/blob/main/website/research/operational-reconstruction/feedback.md)

## Two different optimization problems {#4-классический-предел-вывод-fep}

For diagonal input $p$ and output $q$, the functional becomes the cross-entropy $-\sum_i q_i\log p_i$. Its minimum lies on the most probable input symbol. Variational inference instead starts with a joint generative law $p(x,z)$, observed $x$ with $p(x)>0$, and a trial posterior $q(z)$. Its objective is

$$
F(q;x)=D(q\Vert p(\cdot\mid x))-\log p(x).
$$

With an unrestricted posterior family it is minimized by the posterior itself. For $p=(0.7,0.2,0.1)$ the first objective is about $0.357$ at a point mass and $0.802$ at $q=p$, in nats. Removing off-diagonal entries neither supplies a sensory observation nor selects the posterior. A bridge to active inference needs a generative law, interventions and a learning rule that can be compared on data.

## Spectral entropy on the state domain {#5-s_spec-vs-s_vn-обоснование-выбора}

For a positive operator of unit trace, all eigenvalues are nonnegative, so the sum $-\sum_i |\lambda_i|\log|\lambda_i|$ with $0\log0=0$ equals the von Neumann entropy. For a general operator it is not a state entropy. This identity gives no extremal characterization of the [self-model](../../core/operators/phi-operator).
