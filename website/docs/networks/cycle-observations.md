---
title: What a closed route measures
description: How to compare transport around intersecting cycles and preserve an observable first arrival after grouping controls.
---

Send a distinguishable signal around a loop and compare its return with its prepared state at the same station. The returned transformation is the **holonomy** on the states the probe can distinguish. An experiment measuring only the return time can miss a change of state.

## One calibration for all cycles {#root}

Choose a reference station in each connected component and a reversible access route from it to every station being compared. For each oriented link, go out along the access route to its start, cross the link, and return along the reverse access route from its end. Tree access routes are one convenient choice. Parallel links and self-loops retain their identities.

[T] Two reversible connections on the same signal space are equivalent under local changes of frame exactly when **one** change of frame at the reference station intertwines all these loop transformations on every input. The construction recovers a frame at each station by going back along its first access transport, applying the common calibration, then going out along the second. The argument covers arbitrary vertex sets with supplied access routes and finite walks. It assumes that the specified reversible changes of signal coordinates are admissible. [Lean proof](https://github.com/gst-st/uhm/blob/main/website/research/operational-reconstruction/network/CyclicTransport.lean)

A three-colour test exposes the quantifier. At one station compare two loops. In the first network both exchange A and B. In the second, the first exchanges A and B and the second exchanges B and C. Each individual loop can be calibrated to match. Doing both in order returns every colour unchanged in the first network and takes A to C in the second. A detector blind to colour cannot run this test. Related work on general graphs uses a maximal tree to isolate loop variables. [Burbano and Bauer](https://arxiv.org/abs/2409.13812)

## Which internal loops can be removed? {#cells}

Group stations into cells, choose an internal access route from a representative to every member, and retain each crossing port. A coarse connection reproducing every fine transport up to changes of frame exists **if and only if** each internal loop acts as the identity on the probe. It suffices to check the internal edge loops built from the chosen routes. The proof also constructs the transport on every crossing port. Merging different crossing ports imposes further compatibility. Equality of transmission times alone gives no information about those internal transformations. [Criterion for transports and cell construction](https://github.com/gst-st/uhm/blob/main/website/research/operational-reconstruction/network/CyclicTransport.lean)

## First arrival with interference {#readout}

Consider a synchronous network in which every incoming link carries an additive transport and the receiver sums the arriving signals. Each link has one tick of delay, every receiver has finite input degree, and link operators can depend on their order along a route. At each tick the local update expands into a finite sum over walks, even with feedback. Each available binary phase control changes the sign on its assigned links. A route's signature records which switches it traverses an odd number of times.

[T] When doubling an amplitude can give zero only for zero amplitude, all switch settings are dark exactly when the amplitudes sum to zero **in every signature class at that tick**. The proof derives this from the local update and the Walsh transform. A decidable zero test gives an executable search over the settings. Comparing two control systems on the same timed routes and amplitudes, preservation of their signature partitions within each arrival tick suffices to preserve the first visible tick. Losing a distinction between co-arriving routes allows cancellation for suitable amplitudes. This requires repeatable preparation, independent operation of the declared controls and a detector resolving the signal from its baseline. [Lean proofs and executable detector](https://github.com/gst-st/uhm/blob/main/website/research/operational-reconstruction/network/RouteReadout.lean) · [Parity functions and the Walsh basis](https://arxiv.org/abs/2105.10386)

For example, two parallel links carry opposite amplitudes to a receiver with a return link to the source. With independent control of one outward link the signal appears on tick 1. When both links share one switch the receiver stays dark on every tick for every setting. The geometric lengths and gauge transformations need separate tests from the detector controls. [Comparing scales](../geometry/network-scales)
