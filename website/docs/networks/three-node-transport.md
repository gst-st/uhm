---
title: Gauge transport on three sites
description: A local change of frame, its operational test, and the roles of the middle site and the link registers.
---

A pulse travels from A through B to C. Each site has its own frame. A physical prediction must agree when an observer at B changes the coordinates used for **both** incident links. This operation has an exact realization, including for noncommuting frames.

## Transport and a competing action {#transport-test}

Let $U:A\to B$ and $V:B\to C$ be link maps. For invertible frame changes $g_i$, express each map in the new coordinates by $U'=g_B U g_A^{-1}$, $V'=g_C V g_B^{-1}$. Then
$$
V'U'=g_C VU g_A^{-1}.
$$
The middle frame cancels for every injected vector. Actions at the two endpoints of a single link commute as left and right composition. For unitary links, choosing $g_A=I,\ g_B=U^{-1},\ g_C=(VU)^{-1}$ sets both tree transporters to identity. A phase accumulated on an open path can be compared using endpoint references or an additional path.

A different experiment uses a single excitation shared by three sites. Its two hopping generators exchange neighbouring modes and annihilate the spectator mode. Apply the generators successively to the left basis vector. In one order the result is the right basis vector, in the other it is zero. Consequently, a faithful encoding that intertwines both generators cannot turn them into commuting actions on its invariant image. Independent edge doublets can be realized with a tensor factor per edge. This realization has two distinct incident ports at B. Selecting these physical degrees of freedom, their interactions and a Gauss constraint remains a model hypothesis.

**Protocol.** Inject a known polarization at A and record the output at C. Change both frame descriptions at B coherently, including the inverse on the outgoing link. The complete response is invariant at C with fixed endpoint frames. Changing only the incoming transporter is a physical intervention and can change the result. Unit quaternions give a finite noncommuting example acting unitarily on a two-component complex polarization. The exact example checks all time slices, including returns along the chain. [Proofs and source protocol](https://github.com/gst-st/uhm/tree/main/website/research/operational-reconstruction/network)

## Matter moving in the link field {#matter}

Give each configuration two link variables and a particle carrying a colour at one site. A forward move carries the colour through the link, the reverse move uses its inverse, and a move on an unoccupied bond fixes the particle. Each bond move is an involution. Lean proves on the full configuration that each move commutes with the simultaneous action at all three sites, including the shared middle site. The two moves can still have different outcomes when their order is reversed.

For a finite group the permutations extend linearly to unitaries. Averaging the site actions projects onto invariant states. Both moves and their sum preserve that space. With the eight unit quaternions as colours and link variables, each site has a nonempty invariant state obtained by uniformly superposing the configurations with the particle there. Transport exchanges these states. This is a finite gauge-compatible matter dynamics; the choice of gauge group and link degrees of freedom is input.

## Closing the loop {#loop}

Add a controlled direct arm from A to C with transporter $D$. Compare it with the two-link route, matched in arrival time and with a common coherent source and detector. The relative operator $W=D^\dagger VU$ transforms by conjugation at A. For unitary arms and normalized input $x$, the four intensities $I_s=\|Dx+sVUx\|^2$ give
$$
(I_{+1}-I_{-1})/4=\operatorname{Re}\langle x,Wx\rangle,\qquad
(I_{-i}-I_{+i})/4=\operatorname{Im}\langle x,Wx\rangle .
$$
Here intensities are in units of the calibrated single-arm intensity; a physical splitter/detector gain must be included consistently. A tomographically complete family of inputs recovers the operator in the chosen reference frame by polarization. A single input measures one matrix element. Incoherent path records suppress the interference term.

These comparisons establish kinematics and a three-site test. A dynamical gauge theory additionally needs allowed states on links, Gauss generators and an evolution preserving their constraints. The lattice transformation law and closed-loop observables have established precedents. [Wilson](https://doi.org/10.1103/PhysRevD.10.2445) · [Kogut and Susskind](https://doi.org/10.1103/PhysRevD.11.395) · [Measuring the response metric](../geometry/response-metric)
