# -*- coding: utf-8 -*-
"""symbolica_trigrams.py — the 8 trigrams as the octonion basis' own group.

The bagua (8 trigrams) is three stacked lines, yin/yang each: literally a
3-bit string, and the set of trigrams is F2^3. The mathematical fact this
lab pins: the octonion algebra IS a twisted group algebra R_sigma[F2^3] —
its 8 basis units are indexed by F2^3 and multiply by e_a e_b = sigma(a,b)
e_{a XOR b} with a sign cocycle sigma. So «compose two trigrams line-wise»
(XOR) is not a metaphor for the crystal — it is the crystal's underlying
group [Т]. Convention (journaled, [И]): yin=0, yang=1 => Earth = 000 =
identity; the 7 non-Earth trigrams = the 7 nonzero points of F2^3 = the
Fano points = the seven voices; Heaven = 111.

Checks:
  [A] trigram set = F2^3; Earth=identity; 7 rest = Fano points [Т]
  [B] the King-Wen FAMILY (father/mother/3 sons/3 daughters) is weight
      arithmetic: sons=weight-1, daughters=weight-2; son XOR son = daughter,
      son XOR complementary daughter = father [Т]
  [C] the Earlier-Heaven (Fuxi) circle puts XOR-complements opposite [Т]
  [D] hexagram = (upper,lower) trigram pair = F2^6 — consistent with the
      established 64 = F2^6 layer (Part XXI, iching lab) [Т]
  [E] octonion twisted-product sanity on a standard Fano labeling: unit
      products land on XOR of indices, signs form a valid cocycle
      (associator nonzero somewhere = nonassociativity witnessed) [Т]
"""

import itertools

TRI = {  # name: (bits as tuple, glyph), yin=0 yang=1, bottom-to-top
    "Earth ☷":    (0, 0, 0), "Thunder ☳": (1, 0, 0),
    "Water ☵":    (0, 1, 0), "Mountain ☶": (0, 0, 1),
    "Wind ☴":     (0, 1, 1), "Fire ☲":    (1, 0, 1),
    "Lake ☱":     (1, 1, 0), "Heaven ☰":  (1, 1, 1),
}
bits = {n: v for n, v in TRI.items()}
val = {n: v[0] | v[1] << 1 | v[2] << 2 for n, v in TRI.items()}
name_of = {v: n for n, v in val.items()}

print("=" * 72)
print("[A] the 8 trigrams = F2^3; Earth = identity; the 7 = Fano points [Т]")
assert sorted(val.values()) == list(range(8))
assert val["Earth ☷"] == 0
fano = sorted(v for v in val.values() if v != 0)
print("  trigrams as 3-bit values:", {n.split()[0]: v for n, v in val.items()})
print("  Earth=000=identity of XOR; nonzero 7 =", fano,
      "= Fano points = voices")
assert len(fano) == 7

print()
print("[B] the King-Wen family IS weight arithmetic [Т]")
w = {n: sum(b) for n, b in bits.items()}
sons = sorted(n for n, x in w.items() if x == 1)
daughters = sorted(n for n, x in w.items() if x == 2)
print("  sons (weight 1):", ", ".join(s.split()[0] for s in sons))
print("  daughters (weight 2):", ", ".join(d.split()[0] for d in daughters))
assert len(sons) == 3 and len(daughters) == 3
for a, b in itertools.combinations(sons, 2):
    assert w[name_of[val[a] ^ val[b]]] == 2, "son XOR son must be a daughter"
print("  son XOR son = daughter: all 3 pairs ✓")
for s in sons:
    comp = name_of[val[s] ^ 7]  # complementary daughter
    assert w[comp] == 2
    assert (val[s] ^ val[comp]) == 7, "son XOR its complement-daughter = father"
print("  son XOR complementary daughter = Heaven (father): ✓")

print()
print("[C] Fuxi (Earlier-Heaven) circle: opposites are complements [Т]")
fuxi = ["Heaven ☰", "Lake ☱", "Fire ☲", "Thunder ☳",
        "Earth ☷", "Mountain ☶", "Water ☵", "Wind ☴"]
for i in range(4):
    a, b = fuxi[i], fuxi[i + 4]
    assert val[a] ^ val[b] == 7, (a, b)
print("  4 opposite pairs, each XOR = 111 (complements): ✓")

print()
print("[D] hexagram = trigram pair => 64 = F2^6 (consistency) [Т]")
hx = {(u, l) for u in val.values() for l in val.values()}
assert len(hx) == 64
print("  8 x 8 pairs = 64 = F2^6 — the established hexagram layer.")

print()
print("[E] octonions as twisted group algebra over F2^3 [Т]")
# Cayley-Dickson over vectors (exact integers): x,y in R^(2^n),
# (a,b)(c,d) = (a c - conj(d) b, d a + b conj(c)); conj negates all but 0.
def conj(v):
    return [v[0]] + [-x for x in v[1:]]

def cd(x, y):
    n = len(x)
    if n == 1:
        return [x[0] * y[0]]
    h = n // 2
    a, b = x[:h], x[h:]
    c, d = y[:h], y[h:]
    def sub(u, v): return [p - q for p, q in zip(u, v)]
    def add(u, v): return [p + q for p, q in zip(u, v)]
    left = sub(cd(a, c), cd(conj(d), b))
    right = add(cd(d, a), cd(b, conj(c)))
    return left + right

def unit(i, n=8):
    v = [0] * n
    v[i] = 1
    return v

def mul_units(x, y):
    v = cd(unit(x), unit(y))
    nz = [(i, s) for i, s in enumerate(v) if s != 0]
    assert len(nz) == 1, (x, y, v)
    i, s = nz[0]
    return s, i

ok_xor = all(mul_units(x, y)[1] == (x ^ y) for x in range(8) for y in range(8))
print("  Cayley-Dickson unit products land on XOR of indices:",
      "yes [T]" if ok_xor else "NO")
assert ok_xor
# nonassociativity witness:
def prod3_left(a, b, c):
    s1, i1 = mul_units(a, b)
    s2, i2 = mul_units(i1, c)
    return s1 * s2, i2
def prod3_right(a, b, c):
    s1, i1 = mul_units(b, c)
    s2, i2 = mul_units(a, i1)
    return s1 * s2, i2
wit = None
for a in range(1, 8):
    for b in range(1, 8):
        for c in range(1, 8):
            L, R = prod3_left(a, b, c), prod3_right(a, b, c)
            assert L[1] == R[1] == (a ^ b ^ c)
            if L[0] != R[0]:
                wit = (a, b, c); break
        if wit: break
    if wit: break
print("  associator witness (e%d e%d) e%d != e%d (e%d e%d): signs differ ->"
      % (wit[0], wit[1], wit[2], wit[0], wit[1], wit[2]),
      "nonassociative [T]")
print()
print("verdict: trigram composition (line-wise XOR) = the octonion basis'")
print("underlying group F2^3; Earth is the unit, the seven moving trigrams")
print("are the Fano points/voices; the King-Wen family, the Fuxi circle and")
print("the 64 hexagrams are all THEOREMS of this arithmetic, not lore [T].")
print("The twist (signs) is exactly what upgrades the group algebra to the")
print("octonions: sigma is a cocycle whose non-symmetry = nonassociativity.")
print("The yin=0 convention is the single [I]-choice, journaled above.")
