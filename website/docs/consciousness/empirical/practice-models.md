---
title: What would distinguish the models of practice?
description: Two prospective tests of conditional predictions about attention reports and accessible memory.
---

A person counting the breath can remember something that a person following it did not retain. Ordinary attention and memory already allow this. To test a further UHM claim we need the theory and its competitor to predict different answers to the **same withheld question**. Two candidate links from the coherence register to an instrument yield such tests. Their applicability to people remains open. [Earlier counting and following experiment](./breath-observers)

## Three questions about one exhalation {#reports}

After a marked exhalation, ask about attention during its early, middle or late third. Call the binary questions A, B and C. The scores record whether the participant's two reports agree. The respiratory trace locates the exhalation. It cannot determine what the participant experienced in any third. Randomize the questions and their order in both the counting and following arms. Include repeated questions, an actual middle question, a matched sham prompt and a silent middle interval. Keep silent, sham and unanswered questions distinct.

[H] Suppose these questions act on the same effective two-dimensional sector. Each yes/no outcome prepares its corresponding rank-one state, with a common identification of the two answer labels. Let $p_{AB},p_{BC},p_{AC}$ be agreement probabilities on the corresponding direct pairs. Positivity gives the testable inequality
$$
40(p_{AB}+p_{BC})\le 25p_{AC}+56.
$$
For example, if the two neighbouring probabilities are both 0.90, the general bound is $p_{AC}\ge 0.64$. A narrower hypothesis places all three question axes on a real plane and turns through the **same signed angle twice**. That hypothesis predicts the equality $p_{AC}=(2s-1)^2$ when both adjacent matches have probability $s$. Equal adjacent probabilities alone also permit turning back to the first axis. [Overlap bound](https://github.com/gst-st/uhm/blob/main/website/research/operational-reconstruction/network/PracticeOverlap.lean) · [Two-turn derivation](https://github.com/gst-st/uhm/blob/main/website/research/operational-reconstruction/network/PracticeHoldout.lean)

| Model fixed before the test | Direct A–C prediction at $s=0.90$ |
|---|---|
| Two equally directed turns, with B unmeasured | 0.64 |
| Two independent ordinary match/flip transitions | 0.82, from $s^2+(1-s)^2$ |
| Three pre-existing binary reports that asking never changes | At least 0.80, from $p_{AC}\ge p_{AB}+p_{BC}-1$ |
| Ordinary memory updated by each question | A six-state post-question register can reproduce the full two-dimensional reset model, including its 0.64. |

With heterogeneous participants, calibration uses products of adjacent match scores from disjoint prespecified blocks within each person. Squaring a pooled group mean changes the prediction. The analysis assumes stable within-person probabilities and conditional independence across those calibration blocks. Conceal the A–C readout during calibration, retain every assigned trial and compare the model residuals with their simultaneous uncertainty intervals. A noisy result spanning both predictions leaves the comparison open. One verified discordance on an identical repeated question contradicts the exact reset model with stable axes and error-free buttons. At the example calibration, an exact 0.64 conflicts with both passive storage and independent flips, while the six-label updating memory still predicts it. A causal history register can replay every consistent finite binary transcript table with a common finite denominator under adaptive questioning. [Classical replay](https://github.com/gst-st/uhm/blob/main/website/research/operational-reconstruction/network/PracticeModelComparison.lean) · [Protocol and scoring](https://github.com/gst-st/uhm/tree/main/website/research/operational-reconstruction/practice-comparison)

## Eight messages and a seven-dimensional register {#capacity}

In a separate cohort present one of eight equiprobable three-tone words during practice. After a fixed delay, randomly request the entire three-bit word or one of its positions. The source knows the correct word. Here success has an external reference.

[H] Suppose the **entire accessible record** of the random word at readout is a single seven-dimensional state, and the eight possible whole-word responses form one normalized measurement. The summed correct-discrimination weight is at most 7, so the mean whole-word success is at most $7/8=0.875$. A seven-label classical register also reaches this ceiling by merging two messages. An ordinary three-bit store retrieves all eight words exactly. Access to an external cue, a surviving sensory trace or another register changes the capacity premise. [Capacity proof and finite controls](https://github.com/gst-st/uhm/tree/main/website/research/operational-reconstruction/network)

For the competitor that decodes **one common triple** and answers single-bit queries from that triple, whole-word success is at least $p_1+p_2+p_3-2$. This uses the union bound and allows correlated bit errors. If the three marginal accuracies were 0.98, the predicted floor would be 0.94. Applying it across trials requires identical preparation and delay, independent late query selection and consistency of the decoding rule across query types. Test those predictions with uncertainty bounds. Reliable whole-word accuracy above 0.875 would challenge the complete single-register hypothesis under its stated conditions. A biological mechanism with ordinary three-bit memory already permits that outcome. [Design and alternative readouts](https://github.com/gst-st/uhm/tree/main/website/research/operational-reconstruction/practice-comparison)

## Can existing data decide? {#data}

We audited four public sources for the required assignments and responses. Each contains relevant human observations. Their designs answer different questions.

| Source | Measurements available | Contrast missing |
|---|---|---|
| OpenNeuro ds001787 | 24 participants, 40 event tables recording probes during mantra meditation. Depth, wandering and drowsiness are asked in fixed order. | Random probe timing does not counterbalance question order or provide the omitted-middle condition. [Dataset](https://openneuro.org/datasets/ds001787/versions/1.1.1) |
| Focused attention and open monitoring study | 27 completers, nine weekly observations per person, schedule-based training order. | Training order across weeks cannot identify report order within one exhalation. [Open supplement](https://doi.org/10.1371/journal.pone.0322537.s003) |
| OpenNeuro ds003969 | A breath-counting block followed by a tradition-specific exercise or more counting. | No randomized direct A–C versus A–B–C comparison. [Dataset](https://openneuro.org/datasets/ds003969/versions/1.0.0) |
| Breath-focus experience sampling | Bell, focus/wandering response, confidence and arousal ratings in sequence. | No reversed binary pairs or randomized omission. [Open project](https://osf.io/b6rn9/) |

None of these four sources supplies the eight equiprobable words, late randomized query and linked responses for the capacity test either. No human effect was estimated from them. The mathematical constraints and synthetic controls are ready for replay. An independent human trial is needed to test the proposed links to contemplation. [Source inventory and digests](https://github.com/gst-st/uhm/blob/main/website/research/operational-reconstruction/practice-comparison/open-data-receipt.json) · [Native Verum receipt](https://github.com/gst-st/uhm/blob/main/website/research/operational-reconstruction/network/verum-receipt.json)
