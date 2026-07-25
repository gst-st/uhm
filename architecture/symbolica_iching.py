# -*- coding: utf-8 -*-
"""symbolica_iching.py — the I Ching on the same octonion crystal.

Human Design (the engine's whole substrate) is built FROM the I Ching: 64 gates
= 64 hexagrams. So the I Ching is not a distant analogy — it is the foundation.
Here we show its combinatorics ARE the octonion / Fano structure (the F2 shadow,
same as the seven voices), rigorously:

  [A] the 8 trigrams = F2^3 (three yin/yang lines = three bits).
  [B] the I Ching's own 'family' (father, mother, 3 sons, 3 daughters) = the
      Hamming-WEIGHT grading of F2^3 (yang-line count), exactly.
  [C] the 7 non-Earth trigrams = the 7 Fano points; their XOR-triples = the 7
      Fano lines = the octonion imaginary triples = the voice coherences' skeleton.
  [D] 64 hexagrams = F2^3 x F2^3 = F2^6 = the 64 gates: two trigrams, upper and
      lower, the two octonion shadows stacked.

Structural claims [Т]; the meaning-level trigram<->voice reading is [И].
"""

# --- the eight trigrams as 3-bit patterns (bottom line = bit0) --------------
# name: (bits b0 b1 b2, yang-count, family role, image)
TRI = {
    "Kun  地 Earth":    (0b000, "mother"),
    "Gen  山 Mountain": (0b001, "youngest son"),
    "Kan  水 Water":    (0b010, "middle son"),
    "Xun  風 Wind":     (0b011, "eldest daughter"),
    "Zhen 雷 Thunder":  (0b100, "eldest son"),
    "Li   火 Fire":     (0b101, "middle daughter"),
    "Dui  澤 Lake":     (0b110, "youngest daughter"),
    "Qian 天 Heaven":   (0b111, "father"),
}

def popcount(n):
    return bin(n).count("1")

print("=" * 70)
print("[A]+[B]  8 trigrams = F2^3 ; the I Ching FAMILY = Hamming weight")
print("  %-18s bits  yang  family" % "trigram")
for name, (bits, role) in sorted(TRI.items(), key=lambda kv: popcount(kv[1][0])):
    print("  %-18s %s   %d    %s" % (name, format(bits, "03b"), popcount(bits), role))
print("  -> weight 0 = mother (all yin), weight 3 = father (all yang),")
print("     weight 1 = the 3 SONS, weight 2 = the 3 DAUGHTERS. The millennia-old")
print("     'family of trigrams' IS the yang-line-count grading of F2^3. [Т]")

print()
print("[C]  the 7 non-Earth trigrams = the 7 FANO POINTS (Earth=0 is the origin)")
pts = [b for _, (b, _) in TRI.items() if b != 0]        # 7 nonzero = Fano points
# Fano lines = XOR-triples {a, b, a^b}
lines = set()
for a in pts:
    for b in pts:
        if a < b:
            lines.add(tuple(sorted((a, b, a ^ b))))
print("  7 points:", sorted(pts), " -> %d Fano lines (XOR-triples):" % len(lines))
name_of = {b: n.split()[0] for n, (b, _) in TRI.items()}
role_of = {b: r for _, (b, r) in TRI.items()}
for ln in sorted(lines):
    fam = "+".join(role_of[x].split()[0] for x in ln)     # son/daughter/father
    print("   {%s}   (%s)" % (", ".join(name_of[x] for x in ln), fam))
print("  -> these are exactly the octonion imaginary triples = the Fano lines =")
print("     the skeleton of the 21 voice-coherences (Part IX). [Т]")

print()
print("[D]  64 hexagrams = F2^3 x F2^3 = F2^6 = the 64 Human Design gates")
print("  every hexagram is an upper trigram over a lower trigram: a point of")
print("  F2^3 x F2^3. HD reads planets into these 64; the engine's whole")
print("  substrate lives on two stacked octonion shadows. [Т]")

print()
print("=" * 70)
print("The I Ching is not analogous to the crystal — it is the crystal's own")
print("F2 shadow, the same one the seven voices live on. Astrology is the R")
print("shadow (G2), the I Ching / HD / voices are the F2 shadow (Fano/PSL(2,7)):")
print("one octonion algebra, three faces.")
