---
title: Distance from the first response
description: When independent probes measure the same travel-time metric, and how an interference control recovers a hidden first arrival.
---

Prepare one localized pulse. Record the first tick at which a receiver can distinguish its signal from the quiet baseline. Repeat with a second probe and in the reverse direction. This experiment measures a travel-time geometry relative to the available clocks, propagation and detection operations.

## A metric from registered actions {#protocol}

Start with stations and a decidable record of which transmission protocols can deliver a distinguishable signal in each integer number of ticks. For each ordered pair require one achievable budget. A bounded scan finds the minimum. A physical realization is a switch with an idle operation and a one-tick transfer to any distinct station. Relay closure means two registered transfers can be joined at a total cost at most the sum of their costs, including any reset or preparation at the relay.

[T] In this model the minimum cost satisfies the triangle inequality. If only identical stations communicate at zero cost and can do so, it separates points. Symmetry holds exactly when every achievable transfer has a return protocol of no greater cost. Two probe families in common units yield identical minima exactly when each can deliver between the same endpoints at no greater cost than any registered transfer of the other. These are criteria for the actual protocol catalogue. Incomplete sampling gives upper bounds on minima; an untried transmission cannot be recorded as impossible. Direction-dependent switching costs give a competing model. This construction requires a clock and a composition rule and assumes no spatial metric. The relation between cost composition and generalized metric spaces was developed by [Lawvere](https://raw.githubusercontent.com/mattearnshaw/lawvere/master/pdfs/1973-metric-spaces-generalized-logic-closed-categories.pdf). [Constructive proof](https://github.com/uhm-theory/holon/blob/main/website/research/operational-reconstruction/network/ProtocolMetric.lean)

## A chain with visible fronts {#chain}

Assume a synchronous local update with one tick of memory: the next signal at cell $j$ depends on the previous signals at $j-1,j,j+1$, and three quiet inputs stay quiet. On a newly reached cell the incoming pulse propagates to a distinguishable signal. Internal states, rotations and later scattering may differ between probes. With source $o$, cells $j>o+n$ remain quiet at tick $n$. At $j=o+n$ the entire signal is the ordered composition of the $n$ leading transmissions. The proof is induction on the actual update; reflection of the coordinate gives the reverse-direction result.

Consequently different locally calibrated probes with visible fronts and a common tick on the same chain measure the cell distance. A family of invertible site frames preserving the quiet baseline preserves the first tick. For visible stations A, B, C in order, let the measured reciprocal segment times be $l,r>0$. The endpoint reading is $l+r$, and these three readings satisfy the metric axioms. This also gives a test of the assumed order: B lies between the two endpoints of the unique longest pair in this model.

**Example.** Two probes with different polarization transport on a chain with hidden cells measured the same matrix, in ticks,
$$
\begin{pmatrix}0&2&5\\2&0&3\\5&3&0\end{pmatrix}.
$$
Clocks with different constant rates require a further test. For each probe $s$, measure $L_s,R_s$, both reverses and the independent end-to-end reading. Check reciprocity and additivity. Relative to a reference probe $0$, a common positive shape up to one scale per probe exists exactly when
$$
L_sR_0=R_sL_0\quad\text{for every }s.
$$
A competitor giving segment times $(2,3)$ and $(2,4)$ has a nonzero minor of magnitude 2. One clock conversion cannot reconcile both bonds. Absolute distance still needs a choice of units. Finite observations establish a result only for the tested probes and model class. [Lean proofs, Verum checks and executable experiment](https://github.com/gst-st/uhm/tree/main/website/research/operational-reconstruction/network)

## Interference on tied routes {#interference}

On a triangle, the direct arm can have the same delay as the two-link route. Let their leading amplitudes be $a,b$. In one setting the first signal can disappear even with perfect links. Register two otherwise identical runs, reversing the physical phase of one arm in the second run. The two leading readings are $a+b,a-b$. Both can vanish simultaneously only if both arms are silent. In a Hilbert detector,
$$
\|a+b\|^2+\|a-b\|^2=2(\|a\|^2+\|b\|^2).
$$
Before the propagation front both settings are quiet. Together the settings recover its arrival tick for either probe, even when the uncontrolled trace stays dark. This requires repeatable preparation, coherent recombination, a controllable relative phase, and detection of the nonzero output modes. A change of description at B cannot replace the physical intervention. [Three-site transport](../networks/three-node-transport)

## What the readings select {#scope}

The larger of the two registered intensities is at least $S=\|a\|^2+\|b\|^2$. This lower bound is sharp: for orthogonal unit amplitudes both intensities equal 2. If the absolute intensity error per setting is at most $e$ and $S>2e$, a threshold strictly between $e$ and $S-e$ separates the leading tick from the quiet ticks. Detector gain and noise must be calibrated in the same units.

The same links can produce different apparent arrival times for different matter. Take a direct-arm transporter $-I$ and an indirect transporter $I$ in $SU(2)$. On the fundamental doublet the two leading amplitudes cancel. In the conjugation representation the central sign acts trivially, so they add. The paired test recovers the same tick for both. Here the sign reversal is a calibrated physical phase applied to one arm **after** its action on the probe. A change of the gauge frame or a central transformation that acts trivially on that probe cannot supply this control.

The result establishes a reciprocal discrete travel-time metric under the stated propagation law. It can be falsified by a probe-dependent delay ratio, asymmetric propagation, an endpoint reading incompatible with the chain, or an unobserved leading mode. In a Hamiltonian network continuous-time amplitudes can be nonzero arbitrarily early; the measurable short-time power, a detection threshold and an exact discrete first tick are different quantities. The continuum limit, spacetime signature and coupling of geometry to matter require independent dynamics and scaling evidence. [Szigeti et al. on short-time quantum walks](https://arxiv.org/abs/1905.03914)
