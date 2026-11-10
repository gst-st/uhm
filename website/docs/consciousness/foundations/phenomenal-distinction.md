---
title: "Experience, access and the limits of comparison"
description: "Which distinctions can be recovered from action and observation? A criterion, a countermodel and an experiment with competing outcomes."
---

# Experience, access and the limits of comparison

Someone learning to notice the instant an image changes may gain a new distinction, a new word for a familiar distinction, or a better memory for the previous image. These are different achievements. The first-person encounter is the starting point for phenomenology. The scientist additionally needs a way to tell those possibilities apart.

## What a protocol identifies {#access}

Specify the actions an investigator or practitioner can take and the readings they can obtain. A reading may be an immediate comparison, a later description, a movement or an instrument signal. Two states are operationally equivalent when every permitted finite sequence of actions followed by any permitted reading has the same result. Agreement now need not survive an intervention.

**Criterion.** An attribution can be recovered exactly from these classes if and only if it is constant on each class. When it exists, the decoder is unique on the classes. In one direction any decoder must give one answer for one class; in the other, evaluating the attribution on a representative is independent of that choice. The theorem is about the *existence* of a decoder for a given attribution. It supplies neither the attribution nor a learning algorithm. It concerns a deterministic system; with noisy participants one must specify distributions, error rates, repeated measures and the population to which an estimate transfers.

In [Autogeny](https://github.com/old8man/math-foundations/blob/main/lean4-mf-kernel/MathFoundations/Autogeny/ActionObservation.lean) the equivalence is constructed from actions and is preserved by their continuation. The proof uses that very construction: `finiteProbeCriterion`. In [Diakrisis](https://diakrisis.gst.st/12-actic/06-actic-theorems) an act of distinction is available to the person performing it; the formal comparison of a practice with its description requires a witness (122.T). [MSFS](https://github.com/gst-st/msfs/blob/main/paper-en/paper.tex) requires comparisons to respect composition before equivalence can be transported across realisations. For a psychological experiment this has a concrete consequence: translating the answers at rest does not validate the translation after distraction or after a delayed question.

A sharp counterexample is `noHiddenDecoder`: extend any nonempty system by an extra bit, keep it across every action and let no reading consult it. Even unlimited choice of finite probes cannot recover it. Calling the bit “experience” would change nothing about the experiment. This does not establish an unconscious double or imply that real experience is causally silent. It tells the researcher exactly what to add: a coupling to an independently measurable consequence, with a competing explanation for that consequence.

## What survives a change of vocabulary {#translation}

Take two catalogues describing the **same episodes**. Each name has a recorded example. Suppose two episodes receive the same name in the first catalogue exactly when they receive the same name in the second. Then there is one and only one translation compatible with all the paired examples; its inverse exists. To translate a name, take its example and read the other catalogue. The agreement condition makes the result independent of which example was selected (`sameDistinctions`). A single pair grouped together on one side and distinguished on the other refutes exact translation.

This recovers the *pattern of distinctions*. Swapping both colour names preserves every same/different judgement. An independent common stimulus can anchor names to stimuli; it does not certify that two people feel the same quality. Comparisons between contemplative traditions therefore require common tasks and exemplars, including mixed or ambiguous episodes. Agreement in a finite sample supports a sampled correspondence, not equality of all possible experience.

For three vocabularies there is also a check on transfer. Learn A→B, B→C and A→C on separate training records; freeze all maps. On each new episode compare the direct and indirect C names and independently record the actual A, B and C names. Every disagreement of the two routes requires at least one of the three translations to be wrong on that episode. So the number of route disagreements is at most the sum of their error counts (`transferTriangle`), even if the errors are dependent. Conversely, eight route disagreements and at most two errors on each of the first two edges force **at least four** direct A→C errors on the same episodes. Perfect route agreement alone proves no accuracy: two routes can agree on the same wrong name. This tests transfer of distinctions, not the presence of experience.

## Which problem is being solved? {#questions}

| Question | Evidence the programme can seek | What remains open |
|---|---|---|
| What a person can distinguish | Repeated comparisons with new examples, new response assignments and held-out interventions | Whether an inaccessible quality has changed |
| How experience persists through time | Immediate and delayed probes with attention and memory rivals | A chain of matching reports does not establish identity of the subject |
| Whether parts form one subject | Manipulate coupling while matching local responses; test whether joint predictions transfer | Joint information alone does not count subjects |
| Whether a machine feels | Apply the same intervention and decoder tests, including failure controls | Even a perfect learned decoder certifies the tested capacity; identifying this with feeling requires a further bridge |
| Why there is experience at all | State the proposed bridge and the independent difference it predicts | Neither an operational quotient nor a threshold in a seven-dimensional register entails existence of experience |

## A test where the answers can differ {#experiment}

Use two gratings moving in opposite directions, one to each eye. Before the test, calibrate an eye-movement decoder on unambiguous physical alternations in a separate block. Fix the time window, minimum detectable effect, calibration error allowance, missing-data rule and exclusion criteria before opening the rivalry data.

Randomly cue attention towards one grating or give a neutral cue. During the fixed interval record gaze, without requesting an action. Only afterwards randomly reveal which button corresponds to which direction and request the last dominant direction; offer a mixed/undecided response. Include replay trials with the same cues and late key assignments. Train and test on separate blocks and use participants, not individual gaze samples, as the independent replication units.

Define one signed contrast for both predictions. Score pre-key gaze towards the cued grating (towards a randomly assigned target on neutral trials); in each presentation mode subtract the neutral mean from the cued mean. Let $\Delta$ be this effect during rivalry minus the matched effect during replay. The **response-only model** allows a bias in the later answer but requires $|\Delta|\le\varepsilon$. The **specified sensory-selection rival** requires $\Delta\ge\delta>\varepsilon$. Fix both bounds independently before testing: the tolerance applies to the difference of effects, including uncertainty of both terms. A change in button reports alone cannot select the sensory model. A replicated shift outside tolerance rejects the response-only model as specified; gaze-specific attention, motor and calibration-transfer alternatives still require separate controls. Intervals spanning both predictions are inconclusive. Neither outcome measures the presence of feeling directly. This is a proposed experiment, not a result obtained on people.

Eye movements and pupil size have already been compared with active reports in [binocular rivalry](https://pubmed.ncbi.nlm.nih.gov/24478356/). That work supplies feasible readouts; it does not validate this contrast. The [practice comparison](/docs/consciousness/empirical/practice-models) addresses a different rival: whether what looks like a newly gained distinction can instead be explained by retention of the last question.

Proofs: [access and translation](https://github.com/gst-st/uhm/blob/main/website/research/operational-reconstruction/network/PhenomenalAccess.lean), [application to the Autogeny dynamics](https://github.com/gst-st/uhm/blob/main/website/research/operational-reconstruction/ActionAccess.lean), [native control cases](https://github.com/gst-st/uhm/blob/main/website/research/operational-reconstruction/network/AccessControls.vr).
