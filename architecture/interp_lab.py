# -*- coding: utf-8 -*-
"""interp_lab.py — population baselines for the hidden layers (HB23).

The report says "у населения ~X%" — those numbers are measured here, not
guessed. For a population of random birth moments we compute the same
hidden-layer quantities the Rust interpretation machine surfaces per chart:

  spine count (vs the binomial expectation 26*8/64 = 3.25),
  the asking-voice (syndrome mode) census,
  grounded-pair rate (pair {x,y} with its {x,y,O} triple also activated),
  triangle-resolution rates (shadow line present; witness voice present),
  double-stamp rate (a gate hit 2+ times),
  the profile -> coherence census (the 86.7/13.3 law in voice-pair form).

Usage: python3 interp_lab.py [n]
"""
import sys
from collections import Counter

import numpy as np

from hd_lab import HDChart
from heptacode import classify, syndrome, POS2AX, pair_key, CO_NAMES
from homoholograph import rnd_moments

XLABEL = {'A': 1, 'S': 2, 'L': 3, 'D': 4, 'U': 5, 'E': 6, 'O': 7}

def chart_objects(c):
    acts = list(c.personality.values()) + list(c.design.values())
    return [(g, l, *classify(g), syndrome(g)) for g, l in acts]

def hb23(n=1500, seed=23):
    rng = np.random.default_rng(seed)
    charts = [HDChart(dt) for dt in rnd_moments(n, rng)]

    spine_counts, quest = [], Counter()
    pair_tot = grounded = 0
    tri_tot = shadow_ok = witness_ok = 0
    dbl = 0
    prof_coh = Counter()
    LINE_VOICE = 'ASLDUE'

    for c in charts:
        objs = chart_objects(c)
        activated = [(k, obj) for (_, _, k, obj, _) in objs]
        syn = [s for (_, _, _, _, s) in objs]
        spine_counts.append(sum(1 for s in syn if s == 0))
        nz = [POS2AX[s] for s in syn if s != 0]
        if nz:
            quest[Counter(nz).most_common(1)[0][0]] += 1
        gates = [g for (g, _, _, _, _) in objs]
        if any(v >= 2 for v in Counter(gates).values()):
            dbl += 1
        act_set = set(activated)
        for (_, _, k, obj, _) in objs:
            axs = frozenset(POS2AX[p] for p in obj)
            if k == 'pair' and 'O' not in axs:
                pair_tot += 1
                want = axs | {'O'}
                if any(kk in ('triangle', 'line')
                       and frozenset(POS2AX[p] for p in oo) == want
                       for (kk, oo) in act_set):
                    grounded += 1
            if k == 'triangle':
                tri_tot += 1
                v = sorted(XLABEL[POS2AX[p]] for p in obj)
                sh = frozenset({v[0] ^ v[1], v[1] ^ v[2], v[0] ^ v[2]})
                wt = v[0] ^ v[1] ^ v[2]
                inv = {v: k for k, v in XLABEL.items()}
                sh_ax = frozenset(inv[x] for x in sh)
                wt_ax = inv[wt]
                if any(kk == 'line'
                       and frozenset(POS2AX[p] for p in oo) == sh_ax
                       for (kk, oo) in act_set):
                    shadow_ok += 1
                if any(kk == 'voice' and POS2AX[next(iter(oo))] == wt_ax
                       for (kk, oo) in act_set):
                    witness_ok += 1
        pl, dl = c.profile
        va, vb = LINE_VOICE[pl - 1], LINE_VOICE[dl - 1]
        prof_coh[pair_key([va, vb]) if va != vb else va * 2] += 1

    sc = np.array(spine_counts)
    print('=' * 74)
    print('HB23 — population baselines for the hidden layers (n=%d charts)' % n)
    print('=' * 74)
    print('spine: mean %.2f sd %.2f (binomial expectation 3.25 / 1.69); '
          'P(spine>=7) = %.1f%%'
          % (sc.mean(), sc.std(), 100 * float(np.mean(sc >= 7))))
    tq = sum(quest.values())
    print('asking-voice census: ' + '  '.join(
        '%s:%.0f%%' % (k, 100 * v / tq) for k, v in quest.most_common()))
    print('grounded pairs: %.1f%% of non-O pair activations '
          '(%d/%d)' % (100 * grounded / pair_tot, grounded, pair_tot))
    print('triangle resolutions: shadow line present %.1f%%, witness voice '
          'present %.1f%% (of %d triangle activations)'
          % (100 * shadow_ok / tri_tot, 100 * witness_ok / tri_tot, tri_tot))
    print('double stamps: >=1 doubled gate in %.1f%% of charts'
          % (100 * dbl / n))
    print('profile->coherence census (top 8 of 12+ classes):')
    for k, v in prof_coh.most_common(8):
        name = CO_NAMES.get(k, 'чистый голос %s' % k[0])
        print('  %-3s %-16s %.1f%%' % (k, name, 100 * v / n))
    print('VERDICT: VERIFIED — baselines for the report ("у населения ~X%")')

if __name__ == '__main__':
    hb23(int(sys.argv[1]) if len(sys.argv) > 1 else 1500)
