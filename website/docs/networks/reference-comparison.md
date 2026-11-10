---
title: What can two independent probes identify?
description: A sign invisible to repeated observations, its relative measurement and a test without fitting.
---

## From records to a state {#records}

If two sources give identical records, ask what the laboratories may *bring* to the comparison. A fresh copy from the unknown source and a specimen prepared by a separately calibrated source need not carry the same information. In the [definition of an operational state](../core/foundations/operational-processes), a change in available preparations or joint instruments changes the family of tests. Substitution remains valid for each fixed family.

## A constructible example {#pair}

Consider a real two-level register in each of two laboratories. Set $J=\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)$, $K=J\otimes J$, and $\rho(t)=(I+tK)/4$, $-1\le t\le1$. Since $K$ is symmetric, traceless and squares to the identity, these are positive, normalized states. They belong to a specified model. Preparing the endpoints does not require a prerecorded joint outcome: use a private fair bit to choose correlated or anticorrelated local eigenstates of $X$ and $Z$, then apply a coherent controlled bit flip. With the usual control-first convention it sends $X\otimes Z$ to $K$, so correlated inputs give the positive endpoint. The inverse gate and the same two local measurements read the sign. A classical bit flip controlled by an already measured register is a different instrument. Mixing the endpoints gives the full interval. [Circuit proof](https://github.com/gst-st/uhm/blob/main/website/research/operational-reconstruction/network/RebitExperiment.lean)

On one copy every pair of real symmetric local effects misses the sign. The reason persists on **any finite number** of independent copies, even when a laboratory jointly measures all its own wires: transpose all indices of the first laboratory. It sends every $t_i$ to $-t_i$ and leaves its symmetric effect fixed. The full contraction is unchanged; the argument extends term by term to separable effects. This covers comparisons with all source signs reversed together. It does not cover a fixed oriented reference, a coherent interaction *between* the laboratories at readout, or local complex effects measuring the imaginary axis. There is no physical partial-transpose gate in the proof. [Exact finite-copy proof](https://github.com/gst-st/uhm/blob/main/website/research/operational-reconstruction/network/ReferenceOrientation.lean)

## What the reference measures {#reference}

Bring an independent preparation $\rho(r)$. Each laboratory can now measure the symmetric involution $J\otimes J$ on its **own two wires** and report a sign. With outcomes $A,B\in\{-1,+1\}$ the individual means vanish and the joint law is

$$
\mathbb E[AB]=t\,r,\qquad \Pr(A=a,B=b)=(1+ab\,t r)/4.
$$

Thus two copies of the same unknown give $t^2$: one can see the magnitude but still cannot tell the signs apart. A calibrated $r\ne0$ gives signed contrast; reversing the reference reverses it, and a zero reference removes it. No common absolute sign can be inferred from relative comparisons alone. For example, at $t=3/5$ the agreement probabilities with $r=3/5,-3/5,0$ are respectively $17/25,8/25,1/2$. These are theoretical probabilities, not measurements. In Lean the matrix identities use exact integer numerators for arbitrary rational parameters; finite polynomials extend them to real parameters.

## Network prediction without a fitted state {#network}

Take sources with nonzero contrasts as vertices and reproducible signed comparisons as edges. In a connected component with reciprocal edges a consistent sign per source exists **exactly when** every closed walk has positive sign. Choose a root convention and transport it along a measured path. Two different paths disagree precisely when their closed return has negative sign. Changing the root convention flips every sign in that component. A tree alone always fits; reserve at least one closing edge for a test. A zero or unresolved sign does not orient an edge. This operational use of [Harary’s balance criterion](https://doi.org/10.1307/mmj/1028989917) also applies to nonquantum sources. [Constructive proof](https://github.com/gst-st/uhm/blob/main/website/research/operational-reconstruction/network/ComparisonNetwork.lean)

For strength as well as sign, independently produced sources in this model predict $C_{ij}=t_i t_j$. Then $C_{12}C_{34}=C_{13}C_{24}$, including zeros. Three pairings constrain the fourth before it is observed. Sign consistency alone does not imply this stronger identity. Dependence of the two emissions, setting-dependent detector response or drift can break the factorization.

## An experiment that could fail {#trial}

Freeze four source settings, a sign-reversed and a zero reference, detector labels, timing and pairing before collecting data. Draw two emissions independently, even in self comparisons; do not split or clone one emission. Use disjoint calibration and validation trials. Randomly interleave all settings with a committed schedule, blind the observers, and seal the fourth-pair outcomes until the prediction is fixed. Keep one row per scheduled trial, including missing outcomes on either side. Qualify the coherent gate and the source independence separately; pooled counts cannot certify either.

The [fixed analysis](https://github.com/gst-st/uhm/blob/main/website/research/operational-reconstruction/network/reference_trial.py) accepts eight arms of 6,000 trials each. Three calibration correlations constrain the held-out fourth; other arms test a neutral reference, sign reversal and two self comparisons. Outcomes are bounded by one in magnitude. For independent trials the simultaneous Hoeffding error probability at radius $1/20$ is at most $16\exp(-6000/800)<0.01$. Each missing product is allowed either sign; no conditioning on detection. Disjoint product intervals reject the factorized model. If the denominator interval includes zero the ratio gives no prediction; the division-free test still applies. Overlap is inconclusive. This design has no collected UHM observations.

A classical source can also draw a hidden sign with mean $t_i$. Two independent signs have mean product $t_i t_j$. Reporting a shared fair bit on one side and that bit times the product on the other reproduces the **entire binary joint law** for this menu, provided the comparison device has access to both signs. [Native controls](https://github.com/gst-st/uhm/blob/main/website/research/operational-reconstruction/network/ReferenceControls.vr) check this rule. Success would support this law of comparison; choosing a physical carrier requires additional interventions that also constrain this rival's wiring. Failure after qualification would rule out the factorization within the stated errors. Neither outcome alone selects complex quantum mechanics, seven dimensions or a theory of everything.

Real quantum theory and the failure of local tomography are established antecedents: [Hardy and Wootters](https://arxiv.org/abs/1005.4870). The distinction between real and complex local measurements also has [optical experiments](https://arxiv.org/abs/2007.14847). The test above specifies which claim about the UHM network can actually be decided with its own preparations and readout.
