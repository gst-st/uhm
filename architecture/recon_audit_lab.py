# -*- coding: utf-8 -*-
"""recon_audit_lab.py — honesty audit of the reverse-engineered core (corpus
Part XX §75) and a test for Fano structure in the coherence covariance.

Two questions, both settled by direct computation on a real population, not by
trusting the prose:

  Q1 (honesty).  §75 claims the interpretation space (7 levels + 7 gains +
     razlad + 21 coherences = 36 numbers) has participation ratio 17.3, with
     the 21 coherences alone carrying 16.6 and the 15-number diagonal 8.9.
     But the HD sensor is structurally blind on 8 of the 21 coherences
     (hb13), so at most 13 coherence columns can vary — a participation ratio
     of 16.6 on them is impossible. Recompute all three numbers honestly.

  Q2 (hidden pattern).  Do the live coherences' population covariance respect
     the theorem-forced Fano triads (prime_radiant.LINES, the corpus wiring)?

AUTHORITATIVE NUMBERS.  Corpus §75 describes the PRODUCTION engine (the Rust
core: v2 encoder, poristost gains, engine razlad). This lab uses the Python v1
`encode` and therefore its participation ratios differ from §75 (v1 gives
coh≈15.4 / diag≈9.6 / all≈19.0; §75's 16.6 / 8.9 / 17.3 are the v2 numbers,
reproduced exactly by core/examples/recon_dump.rs -> that CSV). Treat this
lab's Q1 as an independent v1 cross-check, not the corpus figure.

RESULT (robust across BOTH v1 and v2).  Q2 is a clean NULL: the population
covariance of the coherence STRENGTHS does not preferentially align to the
Fano triads — the canonical (corpus) labeling ranks mid-pack among the 30
Steiner relabelings (v1 p≈0.23, v2 p≈0.77). The Fano structure is the
theorem-forced WIRING topology (which 21 pairs exist, their 7 triads), not a
pattern in how strongly those pairs happen to co-vary. Recorded so the
distinction is not misread in either direction.

Run:  python3 recon_audit_lab.py
"""
import itertools

import numpy as np

from homoholograph import encode, PROC
from hd_lab import HDChart
from prime_radiant import AXES, IDX, LINES

N = 7
PAIRS = [(i, j) for i in range(N) for j in range(i + 1, N)]   # 21, fixed order
PAIR_NAME = {(i, j): AXES[i] + AXES[j] for (i, j) in PAIRS}


def population(n, y0=1920, y1=2020, seed=7):
    """A broad full-span population; times spread so channel coverage is as
    wide as the HD class allows."""
    rng = np.random.default_rng(seed)
    from datetime import datetime, timedelta
    t0 = datetime(y0, 1, 1)
    span = (datetime(y1, 1, 1) - t0).total_seconds()
    rows_coh, rows_lvl, rows_gain, rows_raz = [], [], [], []
    for _ in range(n):
        dt = t0 + timedelta(seconds=float(rng.uniform(0, span)))
        c = HDChart(dt)
        G = encode(c, "union")
        rows_coh.append([abs(G[i, j]) for (i, j) in PAIRS])
        rows_lvl.append([G[i, i].real for i in range(N)])
        # gain: open center -> 0.35 else 0.10 (the filter susceptibility)
        rows_gain.append([0.35 if PROC_INV[ax] not in c.centers else 0.10
                          for ax in AXES])
        # razlad: || personality - design ||_F
        rho = encode(c, "personality")
        bod = encode(c, "design")
        rows_raz.append(float(np.linalg.norm(rho - bod)))
    return (np.array(rows_coh), np.array(rows_lvl),
            np.array(rows_gain), np.array(rows_raz).reshape(-1, 1))


# center<-dimension inverse (voice -> center) for the open-center gain lookup
PROC_INV = {v: k for k, v in PROC.items()}


def participation_ratio(X, standardize=True):
    """PR = (Σλ)² / Σλ² of the covariance (or correlation) matrix of columns
    with nonzero variance. Zero-variance columns are dropped and counted."""
    sd = X.std(0)
    live = sd > 1e-9
    Xl = X[:, live]
    if Xl.shape[1] == 0:
        return 0.0, 0, int(live.sum())
    if standardize:
        Xl = (Xl - Xl.mean(0)) / Xl.std(0)
        M = np.corrcoef(Xl, rowvar=False)
    else:
        M = np.cov(Xl, rowvar=False)
    lam = np.clip(np.linalg.eigvalsh(M), 0, None)
    pr = (lam.sum() ** 2) / (lam ** 2).sum()
    above1 = int((lam > 1.0).sum())
    return float(pr), above1, int(live.sum())


def pc1_share(X):
    sd = X.std(0)
    Xl = X[:, sd > 1e-9]
    Xl = (Xl - Xl.mean(0)) / Xl.std(0)
    lam = np.sort(np.clip(np.linalg.eigvalsh(np.corrcoef(Xl, rowvar=False)),
                          0, None))[::-1]
    return float(lam[0] / lam.sum())


def fano_test(coh):
    """Adjacency-controlled Fano test on the LIVE coherences. Within-triad
    coherence-pairs (share the triad's voices) vs between-triad ADJACENT pairs
    (also share exactly one voice) — so the contrast is Fano structure, not
    mere adjacency. Null: the 30 distinct Steiner labelings of the 7 voices."""
    C = np.corrcoef((coh - coh.mean(0)) / (coh.std(0) + 1e-12), rowvar=False)
    live = coh.std(0) > 1e-9
    live_pair = {PAIRS[k]: live[k] for k in range(21)}
    idx = {PAIRS[k]: k for k in range(21)}

    def edges_of(triad):
        a, b, cc = sorted(triad)
        return [(a, b), (a, cc), (b, cc)]

    def within_between(lines):
        within, between_adj = [], []
        line_of = {}
        for li, tri in enumerate(lines):
            for e in edges_of(tri):
                line_of[e] = li
        for p, q in itertools.combinations(PAIRS, 2):
            shared = len(set(p) & set(q))
            if shared != 1:
                continue                       # keep only adjacent edge-pairs
            if not (live_pair[p] and live_pair[q]):
                continue                       # both must be live
            same = line_of.get(p) is not None and line_of.get(p) == line_of.get(q)
            r = C[idx[p], idx[q]]
            (within if same else between_adj).append(r)
        return within, between_adj

    can_lines = [tuple(t) for t in LINES]
    w, b = within_between(can_lines)
    delta_can = (np.mean(w) - np.mean(b)) if w and b else float("nan")

    # enumerate the 30 distinct Steiner labelings from all voice permutations
    base = frozenset(frozenset(t) for t in LINES)
    seen = set()
    deltas = []
    for perm in itertools.permutations(range(7)):
        relabeled = frozenset(frozenset(perm[i] for i in t) for t in LINES)
        if relabeled in seen:
            continue
        seen.add(relabeled)
        lines = [tuple(sorted(s)) for s in relabeled]
        ww, bb = within_between(lines)
        if ww and bb:
            deltas.append((np.mean(ww) - np.mean(bb)))
    deltas = np.array(deltas)
    rank = int((deltas >= delta_can - 1e-12).sum())
    return delta_can, len(w), deltas, rank, len(seen)


def main():
    n = 3000
    print("=" * 78)
    print("RECON AUDIT — reverse-engineered core (§75) + Fano coherence test")
    print("population: %d union-Γ charts, 1920–2020, seed 7" % n)
    coh, lvl, gain, raz = population(n)

    # ---- Q1: participation ratios (honest recompute of §75) --------------
    diag = np.hstack([lvl, gain, raz])            # 7 + 7 + 1 = 15
    allm = np.hstack([diag, coh])                 # 36
    pr_c, a1_c, live_c = participation_ratio(coh)
    pr_d, a1_d, live_d = participation_ratio(diag)
    pr_a, a1_a, live_a = participation_ratio(allm)
    print("\n[Q1] EFFECTIVE DIMENSIONALITY (correlation-matrix PR):")
    print("  coherences   : PR=%.2f  live=%2d/21  eig>1=%d   (§75 said 16.6)"
          % (pr_c, live_c, a1_c))
    print("  diagonal(15) : PR=%.2f  live=%2d/15  eig>1=%d   (§75 said 8.9)"
          % (pr_d, live_d, a1_d))
    print("  all 36       : PR=%.2f  live=%2d/36  eig>1=%d   (§75 said 17.3)"
          % (pr_a, live_a, a1_a))
    print("  PC1 share of all-36: %.1f%%   (§75 said 16.5%%)"
          % (100 * pc1_share(allm)))
    # covariance-matrix variant (unstandardized), in case §75 used it
    prc_cov, _, _ = participation_ratio(coh, standardize=False)
    pra_cov, _, _ = participation_ratio(allm, standardize=False)
    print("  [cov-matrix variant] coherences PR=%.2f  all-36 PR=%.2f"
          % (prc_cov, pra_cov))

    # ---- blind-zone confirmation -----------------------------------------
    live = coh.std(0) > 1e-9
    dead = [PAIR_NAME[PAIRS[k]] for k in range(21) if not live[k]]
    print("\n  BLIND (zero-variance) coherences: %s  (%d dead)"
          % (dead, len(dead)))

    # ---- Q2: Fano structure ----------------------------------------------
    delta, nwithin, deltas, rank, ndistinct = fano_test(coh)
    print("\n[Q2] FANO TRIAD STRUCTURE (adjacency-controlled, live coherences):")
    print("  canonical Δ = within-triad − between-triad(adjacent) corr = %.4f"
          % delta)
    print("  live within-triad adjacent pairs used: %d of 21" % nwithin)
    print("  null: %d distinct Steiner labelings; canonical Δ rank = %d/%d"
          % (ndistinct, rank, len(deltas)))
    print("  null Δ: mean=%.4f sd=%.4f min=%.4f max=%.4f"
          % (deltas.mean(), deltas.std(), deltas.min(), deltas.max()))
    p = rank / len(deltas)
    print("  => canonical is in the top %.0f%% of Steiner labelings (p=%.3f)"
          % (100 * p, p))

    # the one fully-live triad: {S,O,U}
    C = np.corrcoef((coh - coh.mean(0)) / (coh.std(0) + 1e-12), rowvar=False)
    idx = {PAIRS[k]: k for k in range(21)}
    def tri_mean(letters):
        vs = sorted(IDX[x] for x in letters)
        es = [(vs[0], vs[1]), (vs[0], vs[2]), (vs[1], vs[2])]
        rs = [C[idx[e], idx[e2]] for e, e2 in itertools.combinations(es, 2)]
        return np.mean(rs)
    print("\n  fully-realizable triad {S,O,U} mean internal corr = %.4f"
          % tri_mean("SOU"))
    print("=" * 78)


if __name__ == "__main__":
    main()
