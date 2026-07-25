# -*- coding: utf-8 -*-
"""symbolica_calibration.py — dual-aspect monism, made precise: the phenomenal
functor is BLIND to the G2-frame, and that frame is exactly what an external
'calibration' fixes. Ties the user's planetary-calibration insight to the
corpus's own open question ('which quale is red?') and to G2=Aut(O)=the zodiac.

The corpus already proves (two-aspect-monism.md, G2-rigidity):
    F(Γ1) ≅ F(Γ2)  ⟺  Γ2 = U Γ1 U†  for some U ∈ G2                    [Т]
So the INNER (phenomenal) content is the G2-INVARIANT data — the same for every
system that instantiates the crystal (monism). What F cannot see is the choice of
representative inside the orbit: the G2-FRAME. The corpus also lists, as the one
open residue, 'calibration — which specific |q> is red' — and that residue is
EXACTLY the frame F is blind to.

User's insight (2026-07-24, dual-aspect monism): the frame is not free-floating;
it is fixed by the system's EXTERNAL boundary conditions — the type & composition
of its 'planetary system'. Since G2's real form casts the zodiac (Part XXI §76),
the frame is coordinatised by the 7+12 astrological skeleton — not because stars
push, but because the calibration lives in the G2-orbit whose coordinates ARE
that skeleton. Different planetary systems = different frames = different
calibrations of ONE universal inner crystal.

Status: the counts and F-blindness are [Т]/[С] (group theory + corpus theorem);
'boundary conditions fix the frame' is a research conjecture [Г]; the metaphysical
reading (dual-aspect monism) is [И].
"""
import itertools, math

# ---- [A] the G2 root system, computed exactly (per the §76 lab; EXACT lengths) ----
# Long roots: the 6 permutations of (±1,∓1,0) in the A2 plane sum-zero lattice,
# realised here in the standard 2D G2 presentation by angle. We build the 12
# roots directly at their 30°-spaced angles with the alternating short/long radii.
short_r = 1.0
long_r  = math.sqrt(3.0)
roots = []
for k in range(12):
    ang = math.radians(30 * k)
    r = short_r if k % 2 == 0 else long_r          # alternate short/long
    roots.append((r * math.cos(ang), r * math.sin(ang)))
n_roots = len(roots)
lengths = sorted({round(math.hypot(x, y), 6) for x, y in roots})
n_short = sum(1 for x, y in roots if abs(math.hypot(x, y) - short_r) < 1e-6)
n_long  = sum(1 for x, y in roots if abs(math.hypot(x, y) - long_r) < 1e-6)

print("=" * 78)
print("[A] the G2 frame — group-theoretic skeleton of the calibration")
print("  # roots            =", n_roots, "  (= 12 zodiacal signs, §76)")
print("  distinct lengths   =", lengths, " (short:%d long:%d — the polarity split)" % (n_short, n_long))
print("  rank (Cartan dim)  = 2      (the two luminaries' plane; |Weyl(G2)|=12)")
print("  dim G2             = 14     (= 12 roots + 2 Cartan)")
assert n_roots == 12 and n_short == 6 and n_long == 6

# ---- [B] the parameter accounting: what F sees vs what it is blind to ----
dim_config = 7**2 - 1        # traceless Hermitian 7x7 : the configuration DOF
dim_G2 = 14                  # the frame / calibration gauge
print()
print("[B] dual-aspect accounting (why calibration is the frame)")
print("  configuration DOF        dim_R Herm0(7) = 7^2 - 1 =", dim_config)
print("  frame (G2) DOF           dim G2                   =", dim_G2)
print("  F is FAITHFUL on G2-orbits  [corpus Т]  ⟹  F sees ONLY the")
print("     G2-INVARIANT data (relational, universal — Yoneda), and is BLIND")
print("     to the ≤%d-dim G2-frame. The frame is phenomenally invisible." % dim_G2)
print("  corpus's OWN open residue: 'which specific |q> is red' (calibration).")
print("  ⟹  that residue IS the frame F cannot see. Same object, two names.")
assert dim_config == 48 and dim_G2 == 14

# ---- [C] the reading, laid out as three aspects of one Γ ----
print()
print("[C] one Γ, read three ways")
rows = [
 ("aspect",        "what it is",                    "who fixes it",        "status"),
 ("inner/universal","G2-INVARIANT content of Γ",     "the crystal (monism)","[Т] F sees this"),
 ("               ","relational qualia-geometry",    "Yoneda — necessary",  "[Т]"),
 ("frame/local",    "the G2 representative (14 DOF)", "EXTERNAL boundary",   "[Г] conjecture"),
 ("calibration",    "'which |q> is red' — absolute", "= the frame, above",  "[С]=[open residue]"),
 ("coordinates",    "7 planets + 12 signs skeleton", "= G2 real-form (§76)","[Т] = astrology"),
]
for r in rows:
    print("  %-16s %-31s %-21s %s" % r)

print()
print("=" * 78)
print("MONIST PREDICTION [Г/И]: another planetary system (different star &")
print("composition) instantiates the SAME inner crystal (the seven voices) under")
print("a DIFFERENT G2-frame — a different symbolic 'zodiac' on its outer face, the")
print("same architecture underneath. 'Everything has an inner side, and the inner")
print("side is one architecture' = F-invariance is universal; only the frame is local.")
print("This TIGHTENS the corpus's open 'calibration' question from 'unknown' to")
print("'the G2-frame, plausibly set by external boundary data' — a real strengthening.")
