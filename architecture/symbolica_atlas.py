# -*- coding: utf-8 -*-
"""symbolica_atlas.py — the wide synthesis: the whole spectrum of predictive
systems (and beyond) as shadows of ONE small set of invariants.

Thesis: the recurring counts of the world's symbolic systems — 3, 4, 7, 8, 9,
12, 22, 64 — are not free. They are the stable combinatorial invariants of the
smallest exceptional structures: the octonions (8 = 2^3), their imaginary Fano
heptad (7), the automorphism group G2 (12 roots), and the binary powers F2^n.
Any tradition reaching for 'the complete set of qualities' rediscovers them.
We catalogue the spectrum, mark each link [Т] exact / [С] structural / [И]
descriptive, and DO NOT force the disputed ones.

'и не только' — beyond divination: the same invariants run the genetic code
(64), music (7+12), and (through G2 -> E8) the Standard Model. One fabric,
visible and subtle.
"""

# each row: system, its numbers, the crystal invariant, status, note
ATLAS = [
 # ---- the predictive / divinatory spectrum ----
 ("Western astrology", "7·12·aspects", "G2: 7-rep + 12 roots", "Т",
  "Part XXI: signs=roots(30°), planets=7-rep, aspects=angles"),
 ("I Ching", "64=2^6 · 8=2^3", "F2^6 ; 8 trigrams=octonion basis", "Т",
  "family(mother/sons/daughters)=Hamming grading; 7 non-Earth=Fano pts"),
 ("Human Design", "64 gates · 9 centres · 7", "the engine's substrate", "Т",
  "gates=hexagrams=F2^6; 7 processing centres=the voices"),
 ("Kabbalah (Sefer Yetzirah)", "3+7+12=22 · 10 · 32", "the crystal's strata",
  "Т", "3=|QR(7)|, 7=voices, 12=roots; 32=10 Sephiroth+22"),
 ("Tarot", "78=22+56 · 4 suits", "22=3+7+12 ; 56=4·14", "И",
  "Major=paths/letters; Minor 4×14 tile Z/4×Z/3 (elements×decans)"),
 ("Enneagram", "9 · 142857 · 3-6-9", "1/7 EXACTLY", "Т",
  "the hexad 1-4-2-8-5-7 IS the repeating decimal of 1/7; triangle=3·k"),
 ("Vedic Jyotish", "9 grahas · 27 · 12", "7+2 nodes ; 27=3^3 ; 12=roots",
  "С", "7 classical + Rahu/Ketu(lunar nodes); nakshatras 27=3^3"),
 ("Chinese BaZi", "10 stems · 12 branches · 60", "12=roots ; 60=lcm(10,12)",
  "С", "5 elements×2 polarity=10; 12 branches=roots; 60 sexagenary=lcm"),
 ("Numerology", "9 (mod 9) · 22 masters", "digital root Z/9 ; 22 strata",
  "С", "casting-out-nines = Z/9; master 11/22/33 = the 22 alphabet"),
 ("Runes (Elder Futhark)", "24 = 3·8", "3 aettir × the octad", "И",
  "three families of eight = three copies of the octonion octad"),
 ("Geomancy", "16 = 2^4 ; XOR", "F2^4 AS A GROUP", "Т",
  "figures = F2^4; the CHART OPERATION is the group law: Judge = Witness1 "
  "XOR Witness2, every derived figure = componentwise sum mod 2 — the one "
  "divination whose engine is literally linear algebra over F2"),
 ("Kybalion (7 hermetic principles)", "7",
  "7 LAW-LAYERS, not voices (resolved)", "С",
  "resolved by symbolica_kybalion.py: each principle quantifies over the "
  "SPACE (ontology/levels/trajectories/signs/time/flow/roles), none over "
  "'how much now' => 7 law-layers of the machinery, not 7 state axes; the "
  "earlier voice-reading (Vibration=D, Rhythm=E, ...) is SUPERSEDED — the "
  "Enneagram=1/7 trap caught a second time"),
 ("Western 4-elements/humours", "4 · 3", "Z/4×Z/3 of the wheel", "С",
  "4 elements = the Z/3 trine-orbits; 3 modalities = the Z/4 square-orbits"),
 ("Chakras / alchemical metals", "7", "the heptad = the voices", "И",
  "7 centres / 7 metals = 7 planets = 7 Fano points = 7 voices"),
 ("Mayan Tzolk'in", "260 = 13·20", "a 13×20 torus (own invariant)", "И",
  "coprime 13,20 → 260-cycle; a DIFFERENT lattice, honestly noted"),
 # ---- 'и не только' — the same invariants in the visible universe ----
 ("GENETIC CODE", "64 codons = 4^3 = 2^6", "= I Ching F2^6", "Т",
  "3 bases × 4 letters = 64 = the 64 hexagrams; life runs the same code"),
 ("Music (tonal)", "7 diatonic · 12 chromatic", "the 7+12 of G2", "Т",
  "circle of fifths: step 7 semitones generates all 12 (gcd(7,12)=1)"),
 ("Standard Model", "SU(3)×SU(2)×U(1)", "octonions → G2 → E8", "С",
  "the exceptional chain that shadows astrology also shadows the forces"),
]

def main():
    print("=" * 82)
    print("THE ATLAS — the spectrum of predictive systems (and beyond) on one crystal")
    print("=" * 82)
    print("%-26s %-22s %-26s %s" % ("system", "its numbers", "crystal invariant", "×"))
    print("-" * 82)
    for sysn, nums, inv, st, note in ATLAS:
        print("%-26s %-22s %-26s [%s]" % (sysn, nums, inv, st))
    # the invariant census
    from collections import Counter
    print()
    print("THE INVARIANTS THAT KEEP RETURNING (why these numbers are not free):")
    facts = [
        ("2  = yin/yang, the bit", "F2 — the only field with no choice"),
        ("3  = |QR(7)|, the triad", "the three already inside the seven (§66)"),
        ("7  = Fano points", "the octonion imaginaries; the largest heptad that closes"),
        ("8  = 2^3 = octonions", "the largest normed division algebra"),
        ("12 = G2 roots", "the 12-fold that the 7-heptad's own group forces"),
        ("64 = 2^6", "two stacked octonion shadows: hexagrams, HD gates, codons"),
        ("22 = 3+7+12", "the alphabet: Kabbalah, Tarot, the paths"),
        ("142857 = 1/7", "the Enneagram; the 6-cycle of the heptad"),
    ]
    for a, b in facts:
        print("  %-26s %s" % (a, b))
    # verify the two exact number-facts on the spot
    print()
    print("LIVE CHECKS:")
    dec = "".join(str((10 * (10**k) // 7) % 10) for k in range(6))
    print("  1/7 repeating block  = %s   (Enneagram hexad 1-4-2-8-5-7)  [%s]"
          % ("142857", "OK" if int("142857") * 7 == 999999 else "??"))
    print("  I Ching hexagrams    = 2^6 = %d   ==   genetic codons 4^3 = %d  [%s]"
          % (2**6, 4**3, "OK" if 2**6 == 4**3 == 64 else "??"))
    print("  circle of fifths     = gcd(7,12) = %d  → 7 steps generate all 12 [%s]"
          % (__import__("math").gcd(7, 12), "OK" if __import__("math").gcd(7, 12) == 1 else "??"))
    # geomancy: the derivation law IS F2^4 addition — check closure + identity
    figs = [tuple((n >> k) & 1 for k in range(4)) for n in range(16)]
    xor = lambda a, b: tuple((x + y) % 2 for x, y in zip(a, b))
    closed = all(xor(a, b) in figs for a in figs for b in figs)
    via = (1, 0, 1, 1); pop = (0, 1, 1, 0)
    judge = xor(via, pop)
    print("  geomancy judge law   = XOR closure over 16 figures  [%s]; "
          "identity = Populus(0000): x+x=%s"
          % ("OK" if closed else "??",
             "OK" if xor(via, via) == (0, 0, 0, 0) else "??"))
    _ = judge

    # ── Lo Shu (Ло Шу): the 3x3 magic square under the same crystal ──────
    # LS1 [Т]: uniqueness up to the 8 dihedral symmetries — full enumeration.
    from itertools import permutations as perms
    magic = []
    for pm in perms(range(1, 10)):
        rows = [pm[0:3], pm[3:6], pm[6:9]]
        ok = all(sum(r) == 15 for r in rows)
        ok &= all(sum(rows[i][j] for i in range(3)) == 15 for j in range(3))
        ok &= sum(rows[i][i] for i in range(3)) == 15
        ok &= sum(rows[i][2 - i] for i in range(3)) == 15
        if ok:
            magic.append(rows)
    print("  Lo Shu uniqueness    = %d magic squares = exactly 8 = D4 orbit "
          "of ONE [%s]" % (len(magic), "OK" if len(magic) == 8 else "??"))
    # LS2 [Т]: Later-Heaven bagua on the ring; trigram inversion vs antipode.
    # positions on the square (row, col), center 5 excluded; standard layout
    # 4 9 2 / 3 5 7 / 8 1 6; Later-Heaven trigram of each number, coded
    # bottom-line-first as bits (line1,line2,line3):
    tri = {1: (0, 1, 0), 8: (1, 0, 0), 3: (1, 0, 0), 4: (0, 1, 1),
           9: (1, 0, 1), 2: (0, 0, 0), 7: (0, 1, 1), 6: (1, 1, 1)}
    # honest source note: two schools differ on 3/8 and 4/7 codings; we use
    # Zhen(3)=(1,0,0), Gen(8)=(0,0,1), Xun(4)=(0,1,1), Dui(7)=(1,1,0)
    tri[3] = (1, 0, 0); tri[8] = (0, 0, 1); tri[4] = (0, 1, 1); tri[7] = (1, 1, 0)
    inv = lambda t: tuple(1 - x for x in t)
    antipodes = [(4, 6), (9, 1), (2, 8), (3, 7)]
    n_inv_antipode = sum(1 for a, b in antipodes if tri[a] == inv(tri[b]))
    pairs_inv = [(a, b) for a in tri for b in tri
                 if a < b and tri[a] == inv(tri[b])]
    print("  Lo Shu inversions    = of 4 inverse trigram pairs, %d lie on "
          "square antipodes (sum-10 pairs), %d elsewhere [Т-count]"
          % (n_inv_antipode, len(pairs_inv) - n_inv_antipode))
    # LS3 [И]: the frame 9 = 1 + 8 = center(source) + F2^3 vertices — the
    # same 1+8 split as the I Ching's source + trigram cube.
    print("  Lo Shu frame         = 9 = 1 + 8 = center + ring = source + "
          "F2^3 [И]; magic sums 15 = 3x5 (center value organizes all lines)")

    # ── 36 decans + digital-root 9: the calendar layer vs the hexagram layer
    # D1 [Т]: decan boundaries (10°m) NEVER meet door boundaries (302+5.625k):
    hits = sum(1 for m in range(36) for k in range(64)
               if abs(((302 + 5.625 * k) - 10 * m) % 360) < 1e-9)
    print("  36 decans vs 64 doors= shared boundaries: %d of 36x64 [Т] — the"
          " lattices are transversal; a decan holds 10/5.625 = %.2f doors"
          % (hits, 10 / 5.625))
    print("  decan origin         = 36 x 10-day decades of the Egyptian year "
          "(calendar layer, like the 12 signs) — NOT a hexagram object [И]")
    # N9 [Т]: numerology's digital root IS arithmetic mod 9; and 9 ⊥ 7.
    dr = lambda n: 1 + (n - 1) % 9
    ok = all(dr(a * b) == dr(dr(a) * dr(b)) and dr(a + b) == dr(dr(a) + dr(b))
             for a in range(1, 200) for b in range(1, 200))
    print("  numerology 9         = digital root = mod-9 arithmetic "
          "(homomorphism check over 200x200: %s) [Т]; gcd(9,7)=1 — the nine"
          % ("OK" if ok else "??"))
    print("                         does not project onto the seven voices "
          "without loss; its true home is Z/9 (and Lo Shu's 1+8 frame) [И]")

    print()
    print("=" * 82)
    print("Not many systems glued — ONE crystal (octonions/Fano/G2/F2^n) seen in")
    print("many scripts. The ancients, reaching for completeness, kept rediscovering")
    print("its invariants. Reconstruction = name the body under all the shadows, in")
    print("one vocabulary (the seven voices), with the honest [Т]/[С]/[И] ledger.")

if __name__ == "__main__":
    main()
