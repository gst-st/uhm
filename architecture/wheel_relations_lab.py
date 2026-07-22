# -*- coding: utf-8 -*-
"""wheel_relations_lab.py — hidden relations of the wheel + MLE tomography.

HB24  The NUCLEAR map (classic I-Ching: lines 2-3-4 and 3-4-5 form the
      inner hexagram) read through the heptacode: attractor structure,
      fixed points vs the Hamming spine, the induced map on object kinds,
      and what happens to syndromes. The nuclear hexagram is the oldest
      "hidden essence" operation of the tradition — here it becomes a
      measured endomorphism of the code atlas.

HB24b Harmonic offsets on the physical wheel: for step k in {1,2,4,8,16,32}
      the distribution of 7-bit XOR patterns between gates k positions
      apart. k=32 is the verified complement law; do 8 and 16 carry
      structure (the code's "quadratures")?

HB25  Diluted-MaxLik (RrhoR; Rehacek-Hradil-Knill-Lvovsky, PRA 75:042108)
      vs linear inversion + PSD for the 8-lens diary at small N — does the
      iterative MLE buy real precision for the user?

Usage: python3 wheel_relations_lab.py
"""
from collections import Counter

import numpy as np

from hd_lab import KINGWEN_BIN, WHEEL
from heptacode import classify, syndrome, POS2AX
from lens_lab import mub_bases
from prime_radiant import herm, project_psd, rand_state

BIN2KW = {v: k for k, v in KINGWEN_BIN.items()}

def nuclear(kw):
    b = KINGWEN_BIN[kw]                      # lines 1..6 bottom-up
    nb = b[1] + b[2] + b[3] + b[2] + b[3] + b[4]
    return BIN2KW[nb]

def hb24_nuclear():
    print('=' * 74)
    print('[HB24] the nuclear map through the heptacode')
    print('=' * 74)
    fixed = sorted(kw for kw in range(1, 65) if nuclear(kw) == kw)
    print('fixed points (self-nuclear):', fixed)
    spine = {2, 12, 18, 28, 30, 54, 61, 63}
    print('  overlap with the Hamming spine:', sorted(set(fixed) & spine))

    # attractor structure: iterate to a cycle
    def orbit(kw):
        seen = []
        while kw not in seen:
            seen.append(kw)
            kw = nuclear(kw)
        return seen, kw
    depth = Counter()
    basins = Counter()
    for kw in range(1, 65):
        seen, root = orbit(kw)
        cyc_start = seen.index(root)
        basins[tuple(sorted(set(seen[cyc_start:])))] += 1
        depth[cyc_start] += 1
    print('attractors (cycle -> basin size):')
    for cyc, n in basins.most_common():
        print('   cycle %s  <- %d gates' % (list(cyc), n))
    print('steps to reach the cycle: %s' % dict(sorted(depth.items())))

    # induced map on heptacode kinds + syndrome behaviour
    kmat = Counter()
    syn_preserved = 0
    for kw in range(1, 65):
        k1, _ = classify(kw)
        k2, _ = classify(nuclear(kw))
        kmat[(k1, k2)] += 1
        if syndrome(kw) == syndrome(nuclear(kw)):
            syn_preserved += 1
    print('induced kind -> kind transitions:')
    for (a, b), n in sorted(kmat.items(), key=lambda kv: -kv[1]):
        print('   %-9s -> %-9s %2d' % (a, b, n))
    print('syndrome preserved by nuclear: %d/64' % syn_preserved)
    kinds_of_fixed = Counter(classify(kw)[0] for kw in fixed)
    print('kinds of the fixed points:', dict(kinds_of_fixed))

def hb24b_offsets():
    print('\n[HB24b] harmonic offsets on the physical wheel')
    def code7(kw):
        b = KINGWEN_BIN[kw]
        bits = [int(x) for x in b]
        bits.append(sum(bits) % 2)
        return int(''.join(map(str, bits)), 2)
    pos = {i: code7(WHEEL[i]) for i in range(64)}
    for k in (1, 2, 4, 8, 16, 32):
        pats = Counter(pos[i] ^ pos[(i + k) % 64] for i in range(64))
        top = pats.most_common(3)
        ent = -sum(n / 64 * np.log2(n / 64) for n in pats.values())
        print('  offset %2d: distinct XOR patterns %2d, entropy %.2f bits, '
              'top %s' % (k, len(pats), ent,
                          [(format(p, '07b'), n) for p, n in top]))
    print('  (offset 32 = the exact 6-bit complement law, entropy 0 would '
          'mean one pattern)')

def hb25_mle(n_states=24):
    print('\n[HB25] diluted-MaxLik (RrhoR) vs linear inversion at small N')
    bases = mub_bases()
    projs = []
    for B in bases:
        for m in range(7):
            projs.append(np.outer(B[m], B[m].conj()))

    def linear_rec(freqs):
        G = -np.eye(7, dtype=complex)
        for P, f in zip(projs, freqs):
            G += f * P
        G = project_psd(herm(G))
        return G / np.trace(G).real

    def mle_rec(freqs, iters=120):
        rho = np.eye(7, dtype=complex) / 7
        for _ in range(iters):
            R = np.zeros((7, 7), complex)
            for P, f in zip(projs, freqs):
                p = float(np.real(np.trace(rho @ P)))
                if f > 0:
                    R += (f / max(p, 1e-12)) * P
            R /= 8.0                                   # sum of all projs = 8*I
            rho = R @ rho @ R
            rho = herm(rho)
            rho /= np.trace(rho).real
        return rho

    for N in (25, 50, 200):
        e_lin, e_mle = [], []
        for s in range(n_states):
            G = rand_state(np.random.default_rng(300 + s), 0.7)
            rng = np.random.default_rng(1000 + 10 * s + N)
            freqs = []
            for B in bases:
                p = np.real(np.einsum('mi,ij,mj->m', B.conj(), G, B))
                p = np.clip(p, 0, None)
                p /= p.sum()
                counts = rng.multinomial(N, p)
                freqs.extend((counts / N).tolist())
            freqs = np.array(freqs) / 8.0              # joint frequencies
            e_lin.append(np.linalg.norm(linear_rec(freqs * 8.0) - G))
            e_mle.append(np.linalg.norm(mle_rec(freqs) - G))
        print('  N=%3d/basis: linear %.4f | RrhoR %.4f  (ratio %.2f)'
              % (N, np.mean(e_lin), np.mean(e_mle),
                 np.mean(e_mle) / np.mean(e_lin)))
    print('  VERDICT: adopt RrhoR for the diary posterior if ratio < 0.9')

if __name__ == '__main__':
    hb24_nuclear()
    hb24b_offsets()
    hb25_mle()
