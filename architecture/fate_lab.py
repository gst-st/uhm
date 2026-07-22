# -*- coding: utf-8 -*-
"""fate_lab.py — HB29/29b: the population's dynamical fates.

HB29 (raw rho0 target): 98.7% grey — the NATAL self-model is too diffuse to
regenerate a pattern into the window; a living self-model (the diary) is
required. Scientific in itself, non-discriminative as a verdict.
HB29b (sharpened target, this file): dominant mode of rho0 blended to the
working purity 0.42 -> 42.7% grey / 57.3% window / 0% dense; by type:
Projector 63% window, Generator 60%, MG 57%, Manifestor 42%, Reflector 0%
(the degenerate Phi=0 prior cannot be sharpened - the lunar mirror lives by
reflection, not by its own sharpness).

For random birth moments: build the v2 prior (union) and the self-model
rho0 (Personality), run the canonical L_Omega tick 700 steps, classify the
attractor: grey (P<=2/7) / window (2/7..3/7] / dense (P>3/7). Baselines for
the report's "dynamical fate" layer; split by type and spine share.

Usage: python3 fate_lab.py [n]
"""
import sys
import numpy as np
from hd_lab import HDChart
from homoholograph import rnd_moments
from heptacode import classify, syndrome, POS2AX
from prime_radiant import herm, project_psd, purity, phi_exact, tick

D = 7
AXES = 'ASDLEOU'
ALPHA, BETA = 0.8, 0.12

def mu_of(body):
    b = body.split('.')[-1]
    return 2.0 if b in ('Sun', 'Earth') else 1.0

def encode_acts(acts):
    w = np.zeros(D)
    G = np.zeros((D, D), complex)
    for body, (kw, line) in acts.items():
        mu = mu_of(body)
        kind, obj = classify(kw)
        idx = sorted(AXES.index(POS2AX[p]) for p in obj)
        th = np.pi * line / 3.0
        if kind == 'voice':
            w[idx[0]] += mu
        elif kind == 'pair':
            i, j = idx
            G[i, j] += BETA * mu * np.exp(1j * th)
            G[j, i] = np.conj(G[i, j])
            w[i] += mu / 2
            w[j] += mu / 2
        elif kind in ('line', 'triangle'):
            for a in range(3):
                for b in range(a + 1, 3):
                    i, j = idx[a], idx[b]
                    G[i, j] += BETA * mu / 3 * np.exp(1j * th)
                    G[j, i] = np.conj(G[i, j])
            for i in idx:
                w[i] += mu / 3
    ws = w.sum()
    for i in range(D):
        G[i, i] += (1 - ALPHA) / D + (ALPHA * w[i] / ws if ws > 0 else 0)
    G = project_psd(herm(G))
    return G / np.trace(G).real

def main(n=300):
    rng = np.random.default_rng(29)
    from collections import Counter, defaultdict
    fates = Counter()
    by_type = defaultdict(Counter)
    pinf_all = []
    spine_hi, spine_lo = [], []
    for dt in rnd_moments(n, rng):
        c = HDChart(dt)
        union = {('P.' + k): v for k, v in c.personality.items()}
        union.update({('D.' + k): v for k, v in c.design.items()})
        G = encode_acts(union)
        rho0 = encode_acts(dict(c.personality))
        # sharpen: dominant mode of rho0 blended to working purity 0.42
        wv, V = np.linalg.eigh(rho0)
        v = V[:, np.argmax(wv)]
        proj = np.outer(v, v.conj())
        best, bd = None, 9
        for a in np.linspace(0.05, 0.95, 91):
            r = a * proj + (1 - a) * np.eye(D) / D
            d = abs(purity(r) - 0.42)
            if d < bd:
                bd, best = d, r
        rho = best / np.trace(best).real
        for _ in range(700):
            G = tick(G, rho)
        P = purity(G)
        pinf_all.append(P)
        fate = 'grey' if P <= 2/7 else ('window' if P <= 3/7 else 'dense')
        fates[fate] += 1
        by_type[c.type][fate] += 1
        sp = sum(1 for g, _ in list(c.personality.values())
                 + list(c.design.values()) if syndrome(g) == 0)
        (spine_hi if sp >= 5 else spine_lo).append(P)
    print('=' * 70)
    print('HB29b — fates with the SHARPENED self-model (n=%d, 700 ticks)' % n)
    print('=' * 70)
    tot = sum(fates.values())
    for k in ('grey', 'window', 'dense'):
        print('  %-7s %5.1f%%' % (k, 100 * fates[k] / tot))
    print('  P_inf: mean %.4f sd %.4f range [%.3f, %.3f]'
          % (np.mean(pinf_all), np.std(pinf_all),
             np.min(pinf_all), np.max(pinf_all)))
    print('  by type:')
    for t, ctr in sorted(by_type.items()):
        s = sum(ctr.values())
        print('    %-22s ' % t + ' '.join(
            '%s %.0f%%' % (k, 100 * ctr[k] / s)
            for k in ('grey', 'window', 'dense')))
    if spine_hi and spine_lo:
        print('  P_inf | spine>=5: %.4f vs spine<5: %.4f'
              % (np.mean(spine_hi), np.mean(spine_lo)))
    print('VERDICT: baselines for the «динамическая судьба» layer')

if __name__ == '__main__':
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 300)
