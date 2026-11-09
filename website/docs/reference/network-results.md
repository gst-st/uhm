---
title: Verified network results
description: Observation contracts, witnesses and proof scope for the three-site network.
---

| Result | Premises and witness | Checked conclusion |
|---|---|---|
| Cost of an intervention [T] | Decidable achievable costs, a finite witnessed budget per pair, zero-cost identity and separation, subadditive relay composition. A finite switch inhabits the contract. | Minimal delivery cost is a directed distance; symmetry is equivalent to reciprocal coverage. Common minima are equivalent to coverage in both directions across probe families. Lean: `triangleFromRelay`, `symmetricIffReciprocal`, `sameMetricIffCoverBoth`. |
| Local gauge action [T] | Invertible site frames, two oriented transporters and a particle on one of three sites. The quaternion example uses noncommuting frame changes. | Each transported move is an involution and commutes with the simultaneous site action on matter and links. The moves themselves depend on order. Lean: `movesRespectGauge`, `movesInvolutive`, `pathOrderMatters`. Verum checks cancellation of the middle frame on an arbitrary transmitted value. |
| First response [T] | Synchronous nearest-neighbour update, a quiet fixed baseline, distinguishable leading transmission. Two probes with different polarization updates instantiate the premises. | No earlier signal and exact front value in either direction. First arrival is invariant under invertible frame changes preserving the baseline. Lean: `measuredArrival`, `measuredReturn`, `impulseCovariant`, `firstFrameInvariant`. Verum replays all nine ordered pairs of the three-site Boolean support model. |
| Common shape [T] | Positive reciprocal segment times, additive endpoint time, one constant clock factor per probe. The measured examples are (2,3) versus (2,3), and (2,3) versus (2,4). | Vanishing reference minors are necessary and sufficient for one common ratio. Positive path distances satisfy separation, symmetry and the triangle inequality. Lean: `commonShape`, `reconstructedMetric`. |
| Controlled interference [T] | Two repeatable, linearly combined leading arms. The receiver distinguishes any nonzero mode. At least one arm is present. | The two opposite phase settings recover a visible first front. Four intensity settings recover two relative quadratures. Lean proves the coordinate identities over integer amplitudes and their real/imaginary components. Verum exhausts the finite sign model. |
| Physical universality [H] | Compare independently prepared probes with calibrated clocks and registered detection thresholds. | Extending the same geometry to physical matter and a continuum spacetime requires measured agreement and scaling laws. |

[Three-site experiment](../networks/three-node-transport) · [Response metric](../geometry/response-metric) · [Reproducible proof package](https://github.com/gst-st/uhm/tree/main/website/research/operational-reconstruction/network)
