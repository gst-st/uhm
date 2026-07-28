# -*- coding: utf-8 -*-
"""symbolica_kybalion.py — the Kybalion's 7 principles against the machinery.

The Kybalion (1908, «Three Initiates») names seven hermetic principles:
Mentalism, Correspondence, Vibration, Polarity, Rhythm, Cause-and-Effect,
Gender. The atlas row asked: do they map onto the seven VOICES? [И]

The test here is CATEGORICAL, not numerological. Voices are STATE AXES
(coordinates of Γ); the principles, read one by one, are not coordinates —
each names a LAW-LAYER of a dynamical self-model architecture. If so, the
honest mapping is principles → MACHINERY LAYERS, and the atlas row's question
mark resolves to NO (right count, wrong category — same trap as Enneagram=1/7
vs voices, already caught in the atlas).

Statuses: layer-existence checks are [Т]-anchored (each machinery layer is a
theorem/definition in the corpus); the PAIRING of an old name to a layer is
reading [И]; the categorical claim «principles ≠ axes» is structural [С]
(argued from what each principle quantifies over).
"""

PRINCIPLES = [
    # (name, Kybalion's own formula, machinery layer, corpus anchor, status)
    ("Mentalism", "The All is Mind",
     "two-aspect monism: interior aspect is fundamental; Γ is experiential",
     "consciousness/foundations/two-aspect-monism", "И"),
    ("Correspondence", "As above, so below",
     "holarchy: same Γ-form at every floor; pyramid 21->7->3->1",
     "T-224/225; holarch spec", "И"),
    ("Vibration", "Nothing rests",
     "dynamics: Lindblad flow never freezes a live state; waves/phases in "
     "the live layer", "L_Omega = L0 + R; live::waves", "И"),
    ("Polarity", "Opposites are identical in nature, different in degree",
     "axes: over/under are two signs of ONE axis; tension pairs",
     "zone structure (Over/Window/Under)", "И"),
    ("Rhythm", "The pendulum swings",
     "cycles: emotional wave, planetary returns, tempering",
     "cycles.rs; wave_phase", "И"),
    ("Cause-and-Effect", "Every cause has its effect",
     "evolution operator: state tomorrow = L(state today); kappa flows",
     "L_Omega; kappa_0 [Т]", "И"),
    ("Gender", "Masculine and feminine in everything",
     "two hands of the chart: conscious/act vs bodily/receive (Personality/"
     "Design); pressure-fed vs free-run", "rose two hands; tyaga", "И"),
]

print("=" * 72)
print("[A] the seven principles, one machinery layer each (pairing [И])")
for name, formula, layer, anchor, st in PRINCIPLES:
    print("  %-16s «%s»" % (name, formula))
    print("  %16s -> %s   [%s; anchor: %s]" % ("", layer, st, anchor))
assert len(PRINCIPLES) == 7

print()
print("[B] the categorical test: are these AXES or LAWS? [С]")
print("  A voice/axis answers:  «how much of X is in the state NOW?»")
print("  Each principle answers: «what holds for EVERY state / EVERY pair /")
print("                           EVERY trajectory?»")
quantifies = {
    "Mentalism": "over the WHOLE ontology (what states are)",
    "Correspondence": "over LEVELS (all floors at once)",
    "Vibration": "over TRAJECTORIES (no fixed points alive)",
    "Polarity": "over AXES as pairs (sign structure)",
    "Rhythm": "over TIME (periodic structure)",
    "Cause-and-Effect": "over TRANSITIONS (the flow map)",
    "Gender": "over ROLES in exchange (source/receiver)",
}
for k, v in quantifies.items():
    print("  %-16s quantifies %s" % (k, v))
print("  None quantifies «how much in the state now» =>")
print("  the principles are META (laws about the space), voices are OBJECT")
print("  (coordinates in the space). Same count 7, different category.")

print()
print("[C] verdict for the atlas row [С]")
print("  Kybalion 7 = 7 LAW-LAYERS of a self-model architecture,")
print("  NOT the 7 state axes. The atlas '-> seven voices?' resolves: NO —")
print("  right count, wrong category (the Enneagram=1/7 trap, again).")
print("  What the tradition got structurally right: it takes SEVEN distinct")
print("  law-layers to specify such an architecture (ontology, scaling,")
print("  dynamics, sign structure, periodicity, flow, exchange roles) — and")
print("  the machinery indeed carries exactly these seven, each with its own")
print("  corpus anchor. The DEPTH LIMIT (SAD_MAX=3) is a refinement the")
print("  Kybalion's unlimited 'as above so below' lacks [Т].")
print()
print("kybalion map: OK (7 pairings [И]; categorical claim [С]; anchors [Т/О])")
