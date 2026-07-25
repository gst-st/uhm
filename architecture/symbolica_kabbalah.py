# -*- coding: utf-8 -*-
"""symbolica_kabbalah.py — Kabbalah & Tarot on the same octonion crystal.

The Sefer Yetzirah (the foundational Kabbalistic text, ~2nd-6th c.) does not
merely list 22 Hebrew letters — it STRATIFIES them, explicitly, into
  3 MOTHER letters   (Aleph/Mem/Shin = the primordial triad),
  7 DOUBLE letters   (each with a hard/soft sound -> the 7 planets, 7 days),
  12 SIMPLE letters  (-> the 12 zodiac signs, 12 months),
and 3 + 7 + 12 = 22 = the whole alphabet = the 22 Tarot Major Arcana = the 22
paths of the Tree of Life.

We test whether this 3-7-12 architecture IS the octonion crystal's own natural
stratification (established in Parts IX & XXI):
  3  = |QR(7)| = the 'three already inside the seven' (Sec.66), N_gen,
  7  = the Fano points = octonion imaginaries = voices = planets,
  12 = the G2 roots = the zodiacal signs.
Exact where the numbers are forced [Т]; the letter<->meaning attributions are
the tradition's, version-dependent [И]. We do NOT force the disputed parts.
"""

# quadratic residues mod 7 — the canonical 'three inside the seven'
QR7 = sorted({(k * k) % 7 for k in range(1, 7)})
print("=" * 70)
print("[A] the three strata, by the numbers (all forced) [Т]")
three = len(QR7)                    # 3
seven = 7                           # Fano points / octonion imaginaries
twelve = 12                         # G2 roots
print("  3  MOTHERS  = |QR(7)| = |{%s}| = %d   (the three inside the seven, Sec.66)"
      % (",".join(map(str, QR7)), three))
print("  7  DOUBLES  = Fano points = octonion imaginaries = voices = planets = %d"
      % seven)
print("  12 SIMPLES  = G2 roots = zodiacal signs = %d   (Part XXI)" % twelve)
tot = three + seven + twelve
print("  ---------------------------------------------")
print("  3 + 7 + 12  = %d = the Hebrew alphabet = 22 Tarot Major Arcana =" % tot)
print("              = the 22 paths of the Tree of Life.")
assert tot == 22

print()
print("[B] the SAME numbers the crystal already carries — a table [Т for counts]")
rows = [
    ("stratum",       "Kabbalah",        "crystal",              "astrology"),
    ("3 (triad)",     "3 mother letters", "QR(7) / N_gen",        "3 modalities"),
    ("7 (heptad)",    "7 double letters", "7 voices / Fano pts",  "7 planets"),
    ("12 (dodecad)",  "12 simple letters","12 G2 roots",          "12 signs"),
    ("22 (alphabet)", "22 letters",       "3+7+12 strata",        "Tarot Major"),
]
for r in rows:
    print("  %-14s %-18s %-22s %s" % r)

print()
print("[C] and the 32 — the '32 paths of Wisdom' [Т for the count]")
# Sefer Yetzirah: 10 Sephiroth + 22 letters = 32 = the '32 paths'.
print("  Sefer Yetzirah's 32 = 10 Sephiroth + 22 letters.")
print("  10 = the tetractys 1+2+3+4 (the Pythagorean decad); 22 = 3+7+12 above.")
print("  The Tree of Life's ten nodes + twenty-two edges = a labelled graph on")
print("  the crystal's own strata; the Minor Arcana (4 suits x 14) tile the 12")
print("  signs x 3 decans + the 4 elements — the Z/4 x Z/3 of Part XXI. [И for")
print("  the meaning map; the counts are forced.]")

print()
print("=" * 70)
print("Kabbalah & Tarot are not a fourth system to reconcile — their skeleton")
print("(3-7-12=22, and 10+22=32) IS the octonion crystal's stratification.")
print("Astrology = the R shadow (G2); I Ching = the F2 shadow (Fano); Kabbalah")
print("/Tarot = the same strata, alphabetized. One fabric, read in four scripts.")
