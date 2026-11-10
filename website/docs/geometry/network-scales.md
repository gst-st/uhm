---
title: Distance at different scales
description: Exact and approximate tests for a common transport metric after hiding or grouping stations.
---

Number six stations around a ring A–P–Q–C–R–S–A and give every link one tick. The first impulse sent from A reaches C in 3 ticks in either direction around the ring. Hide P and Q from the display and the reading stays 3. Identify P and Q as a single relay with free switching and the coarse map promises 2 ticks. The unchanged A–S reading of 1 rules out correcting this discrepancy with a single clock factor.

## From the detector to a distance {#detector}

In a synchronous directed network, inject a Boolean pulse and let each station emit on the next tick whenever one of its incoming links was active. Each link has unit delay, each station has finitely many inputs, and there is no cancellation or congestion. Lean derives registration at tick $t$ exactly when a physical walk of that length exists. If there is an arrival in the observation window, the first registered tick is the global minimum. Silence through the last tick gives only a lower bound on any future arrival. This works with cycles, parallel links and disconnected stations. A finite distance on every ordered pair additionally requires reachability. A symmetric metric requires reciprocal minima and separation. [Detector and proof](https://github.com/gst-st/uhm/blob/main/website/research/operational-reconstruction/network/SignalNetwork.lean) · [Definition of the response metric](./response-metric)

## Hiding a station {#terminals}

Retain named terminals. Make a coarse passage for each physical trip from one terminal to the next with only hidden stations in its interior, keeping its complete cost. [T] Splitting any finite trip at its successive terminals and expanding each coarse passage back to its physical trip preserves **every attainable total cost** between terminals, even when trips revisit hidden stations. Keeping the cheapest such passages is enough for first delivery with nonnegative additive costs. Different polarisations can still take different routes. If their original delivery metrics agreed, their terminal metrics still agree. The theorem for attainable costs concerns the existence of trips. Coherent amplitudes also depend on which routes can interfere. [Exact reduction](https://github.com/gst-st/uhm/blob/main/website/research/operational-reconstruction/network/TerminalNetwork.lean) · [Work on exact terminal distances](https://arxiv.org/abs/1202.5675)

## When a hidden loop returns a signal {#memory}

A hidden network can be removed exactly while retaining the echo it sends back. Split its additive update into a measured boundary state $b$ and a hidden state $h$:
$$
b_{t+1}=A b_t+B h_t,\qquad h_{t+1}=C b_t+D h_t.
$$
Eliminating the hidden state gives the boundary echo kernel $K_j=BD^j C$. The input at tick $s$ returns through this kernel at tick $s+j+2$. An initially excited interior contributes the separate signal $BD^t h_0$ to the update at tick $t+1$. Evaluating this history reproduces the full boundary record and therefore every first arrival measured there. A cycle can keep returning a signal after arbitrarily many ticks. Even a permanently circulating internal signal can be invisible if its coupling back to the measured port vanishes.

A direct control compared the full three-port dynamics with the reduced history rule for 648 preparations over 7 updates. The boundary records agreed throughout. In 520 trials the kernel contained a delayed contribution beyond the first return. Arbitrarily controllable input histories permit testing each lag with a separate impulse. A window of exactly the last $L$ boundary inputs suffices for every such history iff $BD^jC=0$ on every input for every $j\ge L$, with initial preparation accounted for separately. This characterizes truncation of the input record. A finite recurrent state can encode an infinite echo tail. On a three-station ring the visible trace from one preparation is 1, 0, 0, 1, so a rule that updates only the current boundary value cannot reproduce even that single trace. [Exact boundary elimination](https://github.com/gst-st/uhm/blob/main/website/research/operational-reconstruction/network/BoundaryMemory.lean) · [Signed-network experiment](https://github.com/gst-st/uhm/blob/main/website/research/operational-reconstruction/network/boundary_experiment.py) · [Related work on projected dynamics and memory](https://arxiv.org/abs/2101.05873)

## Merging stations {#ports}

Now merge each block into a station. The coarse graph offers one passage whenever some pair of fine ports realizes it. To test what a person or detector at a **specified starting port** can actually reach, check each coarse step of cost $t$ from every possible starting port in its source block. There must be a fine trip from that very port to some port of the target block costing at most $t$. [T] This local condition is necessary and sufficient for the reachable blocks to agree at **every** time budget. If two probes agree on fine reachable balls and both pass the local test, they agree at the coarse scale. The test composes through further levels. A genuine merge cannot preserve distances between every pair of original points in a separated metric. [Port lifting and composition](https://github.com/gst-st/uhm/blob/main/website/research/operational-reconstruction/network/PortQuotient.lean)

Suppose any two ports of the same block can be connected in either direction within $D$ ticks. For an $m$-step coarse trip of cost $c$, with $m\ge1$ and freely chosen endpoints, a physical trip exists with cost at most
$$
c+(m-1)D.
$$
Fixing the start can add one more internal transfer. This bound is sharp **at arbitrarily large scales**. In a strip of two-port cells of diameter 1, local reciprocal links spanning up to three ticks contain cycles. Between cells 0 and $m$ the coarse minimum is $m$, while even the best choice of fine endpoints costs $2m-1$. A bound on cell diameter alone therefore gives no scale-independent bound on accumulated error. [Sharpness proof for every route length](https://github.com/gst-st/uhm/blob/main/website/research/operational-reconstruction/network/ScaleObstruction.lean)

## Comparing clocks and macroscopic limits {#limits}

For the same named ports, calibrate positive rational clock factors using one nonzero reference pair. Call the two raw time tables $F,C$ and their readings on that pair $F_0,C_0$. One global factor works exactly when every measured ordered pair satisfies
$$
C_0 F(i,j)=F_0 C(i,j).
$$
An operational equivalent is mutual simulation of every completed delivery in the calibrated budget. For approximate comparisons, convert units before composing errors. If $pF\le qC+a$ and $rC\le sH+b$, the composed error in $rpF\le qsH+ra+qb$ is charged per completed transmission.

A physical realization of a common factor works on every unit-delay Boolean signal network above. Insert a local pipeline of $k$ unit stages per station, with $k\ge1$. The last stage transmits to the first stage of the next station across the original links. An injection produces the original boundary trace on multiples of $k$ and silence at intervening ticks. Thus all finite first arrivals scale by $k$, with the observation horizon calibrated in the same units. [Local clock refinement](https://github.com/gst-st/uhm/blob/main/website/research/operational-reconstruction/network/ClockRefinement.lean)

For a family of scales let $U_n>0$ denote common ticks per macroscopic unit. Uniform agreement on a fixed set of terminal labels means that for every integer $k\ge1$, from some scale onward all terminal pairs satisfy $k|F_n-C_n|\le U_n$ in common ticks. [T] This is equivalent to two budget simulations with the corresponding tolerance. If one family approaches a reference distance table and the normalized differences vanish, the second approaches that table too. A positive distance in each finite network may still collapse to zero in the limit: a fixed one-tick separation divided by $n+1$ does exactly that. Obtaining a nondegenerate continuum geometry additionally requires choosing comparable ports across scales, proving convergence and separating the limiting points. [Calibration and scale theorems](https://github.com/gst-st/uhm/blob/main/website/research/operational-reconstruction/network/NetworkScale.lean)

The independent finite control covers all 624 connected, labelled four-station reciprocal graphs with each link absent or costing 1 or 2 ticks. Hiding either pair of stations preserved the remaining distances in all 3,744 cases. Merging a pair preserved every port's reachable balls in 432 of 3,744 cases. These are exhaustive counts for this finite family. [Executable comparison](https://github.com/gst-st/uhm/blob/main/website/research/operational-reconstruction/network/network_scale_experiment.py) · [Interference and cycle transport](../networks/cycle-observations)

[From refinements to a common nondegenerate metric](./common-limit)
