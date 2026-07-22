#!/usr/bin/env python3
"""
HD-LAB — the anatomy of the Human Design calculation machinery, computed.

What this is: Human Design (Ra Uru Hu, 1987) CLAIMS are esoteric, but its
CALCULATION is a well-defined deterministic map
    birth datetime --ephemeris--> 26 activations --wiring--> chart
and a well-defined map can be dissected with mathematics. This lab:

  [V] re-implements the engine independently and cross-verifies it against
      the open-source reference `pyhd` (github.com/ppo/pyhd, constants
      referenced to "The Definitive Book of Human Design" page numbers),
      investigating every divergence instead of averaging it away;
  [S1] computes the A PRIORI population statistics of the machinery itself
      (types, profiles, authorities, splits) from uniform random birth
      moments — no human data involved, pure celestial mechanics + wiring;
  [S2] computes the Kepler bias: per-gate activation probabilities are NOT
      uniform because the Sun dwells longer near aphelion;
  [S3] tests the combinatorial structure of the wiring against the I Ching
      binary code (King Wen binaries verified on 6 anchors):
      opposite-on-wheel = bitwise complement? channels vs Hamming distance?
      wheel adjacency structure? center↔trigram association? — with
      permutation p-values, printed whatever they are;
  [S4] the 9-center 36-channel multigraph: degrees and Laplacian spectrum;
  [S5] the 88° design arc: day-count and gate-shift distributions.

Honest scope, stated: everything here is about the MACHINERY (the map), not
about people. No psychological claim of HD is tested or endorsed; what the
lab CAN settle is which of HD's famous numbers are properties of the
calculation itself, and whether its wiring carries real combinatorial
structure. Requires: pyswisseph (Moshier mode, ~0.001° — line-accurate).

Provenance of constants: pyhd @ main (fetched 2026-07-22), verified against
the book page references embedded there; King Wen binaries derived from the
Unicode hexagram block via aarzilli/iching's value table and verified on
KW 1, 2, 11, 12, 63, 64.
"""
import json
import math
import random
import sys
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone

import swisseph as swe

swe.set_ephe_path(None)
FLAGS = swe.FLG_MOSEPH

# ============================== THE CONSTANTS ===============================
# The I Ching wheel: 64 gates counterclockwise from Gate 41 at 302.0
# (02°00'00" Aquarius). [Book p27-30; pyhd GATE_WHEEL_START_DEGREES]
WHEEL_START = 302.0
GATE_SEG = 360.0 / 64.0          # 5.625°
LINE_SEG = GATE_SEG / 6.0        # 0.9375°
WHEEL = [41, 19, 13, 49, 30, 55, 37, 63, 22, 36, 25, 17, 21, 51, 42, 3,
         27, 24, 2, 23, 8, 20, 16, 35, 45, 12, 15, 52, 39, 53, 62, 56,
         31, 33, 7, 4, 29, 59, 40, 64, 47, 6, 46, 18, 48, 57, 32, 50,
         28, 44, 1, 43, 14, 34, 9, 5, 26, 11, 10, 58, 38, 54, 61, 60]

# The 36 channels: (gateA, gateB) -> (centerA, centerB). [Book p30, 34-35]
CHANNELS = {
    (1, 8): ("G", "THROAT"), (2, 14): ("G", "SACRAL"), (3, 60): ("SACRAL", "ROOT"),
    (4, 63): ("AJNA", "HEAD"), (5, 15): ("SACRAL", "G"), (6, 59): ("SOLAR_PLEXUS", "SACRAL"),
    (7, 31): ("G", "THROAT"), (9, 52): ("SACRAL", "ROOT"), (10, 20): ("G", "THROAT"),
    (10, 34): ("G", "SACRAL"), (10, 57): ("G", "SPLENIC"), (11, 56): ("AJNA", "THROAT"),
    (12, 22): ("THROAT", "SOLAR_PLEXUS"), (13, 33): ("G", "THROAT"),
    (16, 48): ("THROAT", "SPLENIC"), (17, 62): ("AJNA", "THROAT"),
    (18, 58): ("SPLENIC", "ROOT"), (19, 49): ("ROOT", "SOLAR_PLEXUS"),
    (20, 34): ("THROAT", "SACRAL"), (20, 57): ("THROAT", "SPLENIC"),
    (21, 45): ("HEART", "THROAT"), (23, 43): ("THROAT", "AJNA"),
    (24, 61): ("AJNA", "HEAD"), (25, 51): ("G", "HEART"),
    (26, 44): ("HEART", "SPLENIC"), (27, 50): ("SACRAL", "SPLENIC"),
    (28, 38): ("SPLENIC", "ROOT"), (29, 46): ("SACRAL", "G"),
    (30, 41): ("SOLAR_PLEXUS", "ROOT"), (32, 54): ("SPLENIC", "ROOT"),
    (34, 57): ("SACRAL", "SPLENIC"), (35, 36): ("THROAT", "SOLAR_PLEXUS"),
    (37, 40): ("SOLAR_PLEXUS", "HEART"), (39, 55): ("ROOT", "SOLAR_PLEXUS"),
    (42, 53): ("SACRAL", "ROOT"), (47, 64): ("AJNA", "HEAD"),
}
CENTERS = ["HEAD", "AJNA", "THROAT", "G", "HEART", "SACRAL", "SOLAR_PLEXUS",
           "SPLENIC", "ROOT"]
MOTORS = {"SACRAL", "ROOT", "SOLAR_PLEXUS", "HEART"}   # [Book p116]
DESIGN_ARC = 88.0                                       # [Book; pyhd]

# King Wen -> binary (line1..line6 bottom-up, yang=1); anchors verified.
KINGWEN_BIN = {1:"111111",2:"000000",3:"100010",4:"010001",5:"111010",6:"010111",
 7:"010000",8:"000010",9:"111011",10:"110111",11:"111000",12:"000111",
 13:"101111",14:"111101",15:"001000",16:"000100",17:"100110",18:"011001",
 19:"110000",20:"000011",21:"100101",22:"101001",23:"000001",24:"100000",
 25:"100111",26:"111001",27:"100001",28:"011110",29:"010010",30:"101101",
 31:"001110",32:"011100",33:"001111",34:"111100",35:"000101",36:"101000",
 37:"101011",38:"110101",39:"001010",40:"010100",41:"110001",42:"100011",
 43:"111110",44:"011111",45:"000110",46:"011000",47:"010110",48:"011010",
 49:"101110",50:"011101",51:"100100",52:"001001",53:"001011",54:"110100",
 55:"101100",56:"001101",57:"011011",58:"110110",59:"010011",60:"110010",
 61:"110011",62:"001100",63:"101010",64:"010101"}

BODIES = [("Sun", swe.SUN, 0.0), ("Earth", swe.SUN, 180.0),
          ("Moon", swe.MOON, 0.0), ("NNode", swe.TRUE_NODE, 0.0),
          ("SNode", swe.TRUE_NODE, 180.0), ("Mercury", swe.MERCURY, 0.0),
          ("Venus", swe.VENUS, 0.0), ("Mars", swe.MARS, 0.0),
          ("Jupiter", swe.JUPITER, 0.0), ("Saturn", swe.SATURN, 0.0),
          ("Uranus", swe.URANUS, 0.0), ("Neptune", swe.NEPTUNE, 0.0),
          ("Pluto", swe.PLUTO, 0.0)]

# =============================== THE ENGINE =================================
def jd_of(dt):
    h = dt.hour + dt.minute / 60 + dt.second / 3600
    return swe.julday(dt.year, dt.month, dt.day, h)

def lon_of(jd, body):
    return swe.calc_ut(jd, body, FLAGS)[0][0]

def gate_line(lon):
    x = (lon - WHEEL_START) % 360.0
    gi = int(x // GATE_SEG)
    line = int((x % GATE_SEG) // LINE_SEG) + 1
    return WHEEL[gi], line

def design_jd(birth_jd):
    """Solve sun(jd) = sun(birth) - 88° (Newton on the solar arc)."""
    target = (lon_of(birth_jd, swe.SUN) - DESIGN_ARC) % 360.0
    jd = birth_jd - 88.135
    for _ in range(6):
        pos, _ = swe.calc_ut(jd, swe.SUN, FLAGS | swe.FLG_SPEED)
        diff = (pos[0] - target + 180.0) % 360.0 - 180.0
        jd -= diff / pos[3]
    return jd

def imprint(jd):
    """13 activations at a moment: {name: (gate, line)}."""
    out = {}
    cache = {}
    for name, body, off in BODIES:
        if body not in cache:
            cache[body] = lon_of(jd, body)
        g, l = gate_line((cache[body] + off) % 360.0)
        out[name] = (g, l)
    return out

class HDChart:
    def __init__(self, dt):
        bjd = jd_of(dt)
        djd = design_jd(bjd)
        self.personality = imprint(bjd)
        self.design = imprint(djd)
        self.design_days = bjd - djd
        self.gates = {g for g, _ in self.personality.values()} | \
                     {g for g, _ in self.design.values()}
        self.channels = [c for c in CHANNELS if c[0] in self.gates and c[1] in self.gates]
        self.centers = set()
        for c in self.channels:
            self.centers.update(CHANNELS[c])
        # connected components of the defined-center graph
        adj = defaultdict(set)
        for c in self.channels:
            a, b = CHANNELS[c]
            adj[a].add(b)
            adj[b].add(a)
        comps, seen = [], set()
        for v in self.centers:
            if v in seen:
                continue
            comp, stack = set(), [v]
            while stack:
                x = stack.pop()
                if x in comp:
                    continue
                comp.add(x)
                stack.extend(adj[x] - comp)
            seen |= comp
            comps.append(comp)
        self.components = comps

    def _connected(self, a, targets):
        for comp in self.components:
            if a in comp:
                return any(t in comp for t in targets)
        return False

    @property
    def type(self):
        """The book algorithm [p116, 123, 129-137]. NOTE: for Manifesting
        Generator the motor set INCLUDES the Sacral (channel 20-34 alone
        makes an MG) — pyhd uses non-sacral motors here, which misclassifies
        pure 20-34 charts as pure Generators; we follow the book and count
        the divergence in the verification."""
        if not self.centers:
            return "Reflector"
        throat_to_motor = self._connected("THROAT", MOTORS)
        if "SACRAL" in self.centers:
            return "ManifestingGenerator" if throat_to_motor else "Generator"
        return "Manifestor" if throat_to_motor else "Projector"

    @property
    def profile(self):
        return (self.personality["Sun"][1], self.design["Sun"][1])

    @property
    def authority(self):
        if not self.centers:
            return "Lunar"
        if "SOLAR_PLEXUS" in self.centers:
            return "SolarPlexus"
        if "SACRAL" in self.centers:
            return "Sacral"
        if "SPLENIC" in self.centers:
            return "Splenic"
        pairs = {frozenset(CHANNELS[c]) for c in self.channels}
        if frozenset(("HEART", "THROAT")) in pairs:
            return "EgoManifested"
        if frozenset(("HEART", "G")) in pairs:
            return "EgoProjected"
        if frozenset(("G", "THROAT")) in pairs:
            return "SelfProjected"
        return "Outer"

# ============================ [V] VERIFICATION ==============================
def verify_vs_pyhd(pyhd_path, n=300, seed=1):
    sys.path.insert(0, pyhd_path)
    from pyhd.chart import Chart as PChart
    rng = random.Random(seed)
    agree = dict(gates=0, channels=0, centers=0, profile=0, type=0)
    known_divergence = 0
    mism = []
    for i in range(n):
        dt = datetime(1930, 1, 1, tzinfo=timezone.utc) + \
             timedelta(seconds=rng.randrange(0, int(70 * 365.25 * 86400)))
        mine = HDChart(dt)
        theirs = PChart(dt)
        tg = sorted(int(g._name_[1:]) for g in theirs.gates)
        tc = sorted(tuple(int(x) for x in c._name_[1:].split("_")) for c in theirs.channels)
        import re as _re
        tprof = tuple(int(x) for x in _re.findall(r"\d", str(theirs.profile))[:2])
        tlabel = str(theirs.type)
        tmain = {"Manifestor": "Manifestor", "Pure Generator": "Generator",
                 "Manifesting Generator": "ManifestingGenerator",
                 "Reflector": "Reflector"}.get(tlabel, "Projector")
        agree["gates"] += sorted(mine.gates) == tg
        agree["channels"] += sorted(mine.channels) == tc
        agree["centers"] += len(mine.centers) == theirs.num_centers
        agree["profile"] += mine.profile == tprof
        if mine.type == tmain:
            agree["type"] += 1
        else:
            if mine.type == "ManifestingGenerator" and tmain == "Generator":
                known_divergence += 1
            else:
                mism.append((dt.isoformat(), mine.type, tlabel))
    return agree, known_divergence, mism, n

# ========================== [S1] POPULATION PRIOR ===========================
def population_prior(n=20000, seed=2, y0=1920, y1=2020):
    rng = random.Random(seed)
    span = int((y1 - y0) * 365.25 * 86400)
    types = Counter()
    profiles = Counter()
    auth = Counter()
    ncenters = Counter()
    nchan = Counter()
    splits = Counter()
    month_types = defaultdict(Counter)
    for _ in range(n):
        dt = datetime(y0, 1, 1, tzinfo=timezone.utc) + timedelta(seconds=rng.randrange(span))
        ch = HDChart(dt)
        types[ch.type] += 1
        profiles[ch.profile] += 1
        auth[ch.authority] += 1
        ncenters[len(ch.centers)] += 1
        nchan[len(ch.channels)] += 1
        splits[len(ch.components)] += 1
        month_types[dt.month][ch.type] += 1
    return dict(types=types, profiles=profiles, auth=auth, ncenters=ncenters,
                nchan=nchan, splits=splits, month_types=month_types, n=n)

# ============================ [S2] KEPLER BIAS ==============================
def kepler_gate_bias(year0=2000, years=4):
    """Sun's per-gate dwell probability, EXACT: gate-boundary crossing times
    via Newton on the solar longitude (no sampling noise)."""
    dwell = Counter()
    jd = swe.julday(year0, 1, 1, 0.0)
    # find the first boundary ahead
    def cross_time(jd_guess, target_lon):
        j = jd_guess
        for _ in range(8):
            pos, _ = swe.calc_ut(j, swe.SUN, FLAGS | swe.FLG_SPEED)
            diff = (pos[0] - target_lon + 180.0) % 360.0 - 180.0
            j -= diff / pos[3]
        return j
    lon = lon_of(jd, swe.SUN)
    x = (lon - WHEEL_START) % 360.0
    gi = int(x // GATE_SEG)
    t_prev = cross_time(jd, (WHEEL_START + gi * GATE_SEG) % 360.0)
    total = 0.0
    for k in range(64 * years):
        gi2 = (gi + k) % 64
        boundary = (WHEEL_START + ((gi2 + 1) % 64) * GATE_SEG) % 360.0
        t_next = cross_time(t_prev + 4.0, boundary)
        dwell[WHEEL[gi2]] += t_next - t_prev
        total += t_next - t_prev
        t_prev = t_next
    return {g: dwell[g] / total for g in range(1, 65)}

# ============================ [S3] CODE STRUCTURE ===========================
def hamming(a, b):
    return sum(x != y for x, y in zip(KINGWEN_BIN[a], KINGWEN_BIN[b]))

def code_structure(perms=20000, seed=3):
    rng = random.Random(seed)
    res = {}
    # (a) opposite on wheel = bitwise complement?
    comp = sum(1 for i in range(32)
               if hamming(WHEEL[i], WHEEL[i + 32]) == 6)
    res["opposite_complement"] = (comp, 32)
    # (b) channels vs Hamming distance
    chan_d = [hamming(a, b) for a, b in CHANNELS]
    all_pairs = [(a, b) for a in range(1, 65) for b in range(a + 1, 65)]
    all_d = [hamming(a, b) for a, b in all_pairs]
    mean_chan = sum(chan_d) / len(chan_d)
    mean_all = sum(all_d) / len(all_d)
    ge = 0
    for _ in range(perms):
        samp = rng.sample(all_d, len(chan_d))
        if abs(sum(samp) / len(samp) - mean_all) >= abs(mean_chan - mean_all):
            ge += 1
    res["channels_hamming"] = (mean_chan, mean_all, Counter(chan_d), (ge + 1) / (perms + 1))
    # (c) wheel adjacency distances vs random circular arrangement
    adj_d = [hamming(WHEEL[i], WHEEL[(i + 1) % 64]) for i in range(64)]
    mean_adj = sum(adj_d) / 64
    ge = 0
    for _ in range(perms // 10):
        w = WHEEL[:]
        rng.shuffle(w)
        m = sum(hamming(w[i], w[(i + 1) % 64]) for i in range(64)) / 64
        if abs(m - mean_all) >= abs(mean_adj - mean_all):
            ge += 1
    res["wheel_adjacency"] = (mean_adj, Counter(adj_d), (ge + 1) / (perms // 10 + 1))
    # (d) center <-> trigram association (mutual information vs permuted)
    gate_center = {}
    for (a, b), (ca, cb) in CHANNELS.items():
        gate_center.setdefault(a, ca)
        gate_center.setdefault(b, cb)
    gates_all = sorted(gate_center)
    lower = {g: KINGWEN_BIN[g][:3] for g in gates_all}
    def mi(assign):
        joint = Counter((assign[g], lower[g]) for g in gates_all)
        pc = Counter(assign[g] for g in gates_all)
        pt = Counter(lower[g] for g in gates_all)
        n = len(gates_all)
        s = 0.0
        for (c, t), k in joint.items():
            p = k / n
            s += p * math.log2(p / (pc[c] / n * pt[t] / n))
        return s
    mi0 = mi(gate_center)
    ge = 0
    vals = list(gate_center.values())
    for _ in range(perms // 10):
        rng.shuffle(vals)
        if mi(dict(zip(gates_all, vals))) >= mi0:
            ge += 1
    res["center_trigram_mi"] = (mi0, (ge + 1) / (perms // 10 + 1))
    return res

# ============================ [S4] CENTER GRAPH =============================
def center_graph():
    deg = Counter()
    edges = Counter()
    for (a, b), (ca, cb) in CHANNELS.items():
        deg[ca] += 1
        deg[cb] += 1
        edges[frozenset((ca, cb))] += 1
    # Laplacian of the simple support graph (multiplicity as weight)
    idx = {c: i for i, c in enumerate(CENTERS)}
    L = [[0.0] * 9 for _ in range(9)]
    for e, w in edges.items():
        a, b = tuple(e)
        L[idx[a]][idx[a]] += w
        L[idx[b]][idx[b]] += w
        L[idx[a]][idx[b]] -= w
        L[idx[b]][idx[a]] -= w
    # eigenvalues via numpy if available
    try:
        import numpy as np
        ev = sorted(float(x) for x in np.linalg.eigvalsh(np.array(L)))
    except Exception:
        ev = []
    return deg, edges, ev

# ============================ [S5] DESIGN ARC ===============================
def design_arc_stats(n=2000, seed=4):
    rng = random.Random(seed)
    days = []
    shifts = []
    for _ in range(n):
        dt = datetime(1940, 1, 1, tzinfo=timezone.utc) + \
             timedelta(seconds=rng.randrange(int(60 * 365.25 * 86400)))
        bjd = jd_of(dt)
        djd = design_jd(bjd)
        days.append(bjd - djd)
        gb, _ = gate_line(lon_of(bjd, swe.SUN))
        gd, _ = gate_line(lon_of(djd, swe.SUN))
        ib, idx_d = WHEEL.index(gb), WHEEL.index(gd)
        shifts.append((ib - idx_d) % 64)
    return days, Counter(shifts)

# ================================== MAIN ====================================
def main():
    print("HD-LAB — the machinery of Human Design, computed")
    print("=" * 72)

    pyhd_path = None
    for cand in sys.argv[1:]:
        pyhd_path = cand
    if pyhd_path:
        print("\n[V] cross-verification against pyhd (independent implementations):")
        agree, known, mism, n = verify_vs_pyhd(pyhd_path)
        for k, v in agree.items():
            print(f"    {k:9} agreement: {v}/{n}")
        print(f"    known divergence (20-34 MG-vs-Generator, book p123 vs pyhd bug): {known}")
        if mism:
            print(f"    UNEXPLAINED mismatches: {len(mism)}: {mism[:5]}")
        else:
            print("    unexplained mismatches: 0")

    print("\n[S1] the a priori population statistics of the machinery itself")
    print("     (20,000 uniform random UTC moments, 1920-2020 — no human data):")
    pop = population_prior()
    n = pop["n"]
    claimed = {"Generator": 37.0, "ManifestingGenerator": 33.0, "Projector": 21.0,
               "Manifestor": 8.0, "Reflector": 1.0}
    print("     type                    computed    community-claimed")
    for t in ["Generator", "ManifestingGenerator", "Projector", "Manifestor", "Reflector"]:
        c = 100.0 * pop["types"][t] / n
        se = 100.0 * math.sqrt(c / 100 * (1 - c / 100) / n)
        print(f"     {t:22} {c:6.2f}% ±{se:.2f}     {claimed[t]:5.1f}%")
    print("     authorities:", {k: f"{100*v/n:.1f}%" for k, v in pop["auth"].most_common()})
    print("     defined centers histogram:", dict(sorted(pop["ncenters"].items())))
    print("     splits (components):", dict(sorted(pop["splits"].items())))
    top_prof = pop["profiles"].most_common(6)
    print("     top profiles:", [(f"{a}/{b}", f"{100*v/n:.1f}%") for (a, b), v in top_prof])
    occ = sorted(pop["profiles"])
    fam2 = [(p, (p - 1 + 2) % 6 + 1) for p in range(1, 7)]
    fam3 = [(p, (p - 1 + 3) % 6 + 1) for p in range(1, 7)]
    w2 = sum(pop["profiles"][f] for f in fam2) / n
    w3 = sum(pop["profiles"][f] for f in fam3) / n
    frac = (DESIGN_ARC / LINE_SEG) % 1.0
    print(f"     THE PROFILE LAW: {len(occ)} profiles occur (of 36 possible) = "
          f"{{(p, p+2), (p, p+3) mod 6}};")
    print(f"     measured weights {100*w2:.1f}% / {100*w3:.1f}% vs the arithmetic "
          f"prediction {100*frac:.1f}% / {100*(1-frac):.1f}%")
    print(f"     (the whole profile system is the fractional part of "
          f"88°/0.9375° = {DESIGN_ARC/LINE_SEG:.4f} lines)")
    mt = pop["month_types"]
    gen_rate = {m: 100.0 * (mt[m]["Generator"] + mt[m]["ManifestingGenerator"]) /
                max(1, sum(mt[m].values())) for m in range(1, 13)}
    mn, mx = min(gen_rate, key=gen_rate.get), max(gen_rate, key=gen_rate.get)
    print(f"     seasonal effect on Generator+MG rate: min {gen_rate[mn]:.1f}% (month {mn}) "
          f"max {gen_rate[mx]:.1f}% (month {mx})")

    print("\n[S2] the Kepler bias: the Sun's per-gate dwell probability")
    kb = kepler_gate_bias()
    mean_p = 1 / 64
    dev = {g: (p - mean_p) / mean_p for g, p in kb.items()}
    lo = min(dev, key=dev.get)
    hi = max(dev, key=dev.get)
    print(f"     uniform would be 1.5625% per gate; computed spread:")
    print(f"     min gate {lo}: {100*kb[lo]:.3f}% ({100*dev[lo]:+.1f}%)   "
          f"max gate {hi}: {100*kb[hi]:.3f}% ({100*dev[hi]:+.1f}%)")
    print("     (the mandala is NOT sampled uniformly: aphelion gates are more likely)")

    print("\n[S3] combinatorial structure of the wiring vs the I Ching code:")
    cs = code_structure()
    c, tot = cs["opposite_complement"]
    print(f"     opposite-on-wheel = bitwise complement: {c}/{tot} pairs")
    mc, ma, hist, p = cs["channels_hamming"]
    print(f"     channel-pair Hamming distance: mean {mc:.3f} vs population {ma:.3f} "
          f"(perm. p = {p:.4f}); histogram {dict(sorted(hist.items()))}")
    madj, ahist, p2 = cs["wheel_adjacency"]
    print(f"     wheel-adjacent Hamming distance: mean {madj:.3f} "
          f"(perm. p = {p2:.4f}); histogram {dict(sorted(ahist.items()))}")
    mi0, p3 = cs["center_trigram_mi"]
    print(f"     center<->lower-trigram mutual information: {mi0:.3f} bits "
          f"(perm. p = {p3:.4f})")

    print("\n[S4] the 9-center / 36-channel multigraph:")
    deg, edges, ev = center_graph()
    print("     degrees:", dict(deg.most_common()))
    print("     distinct center-pairs wired:", len(edges), "of C(9,2)=36 possible")
    if ev:
        print(f"     Laplacian spectrum: {[round(x, 3) for x in ev]}")
        print(f"     algebraic connectivity (Fiedler) = {ev[1]:.3f}")

    print("\n[S5] the 88° design arc:")
    days, shifts = design_arc_stats()
    print(f"     day-count: min {min(days):.2f}  mean {sum(days)/len(days):.2f}  "
          f"max {max(days):.2f}  (varies with orbital eccentricity)")
    print(f"     design-Sun sits {sorted(shifts.items())} wheel-gates behind birth-Sun")
    print("\nHD-LAB: every number above is computed, none is quoted.")

if __name__ == "__main__":
    main()
