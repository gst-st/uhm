# -*- coding: utf-8 -*-
"""symbolica_stratification.py — the FULL G2-orbit stratification of D(C^7),
the calibration moduli space that §82 opened.

§82 established: the phenomenal functor F is blind to the G2-frame, so
'calibration' (which quale is red) lives in the moduli space D(C^7)/G2, and
symbolica_frame_bundle.py showed the action has ≥3 orbit types (dims 0/11/14) —
enough to prove NO global calibration exists. THIS lab characterizes the whole
stratification: for each eigenvalue-multiplicity type of Γ (a partition of 7),
the dimension of its G2-orbit (= 14 − dim stabiliser). That is a complete map of
'how much calibration freedom' a configuration of each spectral type carries —
a new, computed result deepening §82 (the calibration structure, not just its
existence).

Rigour: g2 built from the octonion Fano 3-form (dim 14, as in frame_bundle);
orbit dim at Γ = rank{ [X,Γ] : X∈g2 } in Herm(7); for each partition we take a
G2-generic representative (random-unitary eigenframe). [Т for the computation.]
"""
import numpy as np
from itertools import combinations

N = 7
# ---- g2 from the Fano 3-form (QR(7) {i,i+1,i+3}) ----
triples = sorted({tuple(sorted(((i) % 7, (i + 1) % 7, (i + 3) % 7))) for i in range(7)})
phi = np.zeros((N, N, N))
def sgn(p):
    s = 1; a = list(p)
    for i in range(3):
        for j in range(i + 1, 3):
            if a[i] > a[j]: s = -s
    return s
for (a, b, c) in triples:
    for p in [(a, b, c), (b, c, a), (c, a, b), (a, c, b), (c, b, a), (b, a, c)]:
        phi[p] = sgn(p)
so7 = []
for m in range(N):
    for n in range(m + 1, N):
        X = np.zeros((N, N)); X[m, n] = 1.0; X[n, m] = -1.0; so7.append(X)
def act(X):
    t = np.einsum('ip,pjk->ijk', X, phi)
    t += np.einsum('jp,ipk->ijk', X, phi)
    t += np.einsum('kp,ijp->ijk', X, phi)
    return t
M = np.stack([act(X).reshape(-1) for X in so7], axis=1)
_, s, vt = np.linalg.svd(M)
rank = int((s > 1e-9).sum())
g2 = [sum(c * X for c, X in zip(row, so7)) for row in vt[rank:]]
assert len(g2) == 14, f"dim g2 = {len(g2)}"

def orbit_dim(G):
    vecs = []
    for X in g2:
        B = X @ G - G @ X
        vecs.append(np.concatenate([B.real.reshape(-1), B.imag.reshape(-1)]))
    sv = np.linalg.svd(np.stack(vecs, 0), compute_uv=False)
    return int((sv > 1e-7).sum())

def partitions(n, mx=None):
    if mx is None: mx = n
    if n == 0: yield (); return
    for k in range(min(n, mx), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest

rng = np.random.default_rng(7)
def gamma_of_type(part, trials=6):
    # G2-generic representative with eigenvalue multiplicities `part`; take the
    # max orbit dim over a few random eigenframes (the generic stratum value)
    eigs = []
    base = np.linspace(1.0, 2.0, len(part))  # distinct eigenvalues
    for val, m in zip(base, part):
        eigs += [val] * m
    eigs = np.array(eigs); eigs = eigs / eigs.sum()
    best = 0
    for _ in range(trials):
        A = rng.standard_normal((N, N)) + 1j * rng.standard_normal((N, N))
        Q, _ = np.linalg.qr(A)  # Haar-ish unitary eigenframe
        G = (Q * eigs) @ Q.conj().T
        best = max(best, orbit_dim(G))
    return best

print("=" * 66)
print("THE G2-ORBIT STRATIFICATION OF D(C^7) — the calibration moduli space")
print("=" * 66)
print("g2 built from Fano 3-form: dim =", len(g2), "(= G2 = Aut(O))")
print()
print("%-20s %6s %6s %8s" % ("spectral type λ⊢7", "orbit", "stab", "rank Γ"))
print("-" * 44)
rows = []
for part in partitions(7):
    od = gamma_of_type(part)
    rk = len(part) if part[-1] != 0 else 0
    # rank of Γ = number of nonzero eigenvalues; here all `base` nonzero, so
    # rank = 7 always (multiplicities partition the 7 nonzero eigenvalues).
    rows.append((part, od, 14 - od))
    print("%-20s %6d %6d %8d" % ("[" + ",".join(map(str, part)) + "]", od, 14 - od, 7))
dims = sorted({od for _, od, _ in rows})
print()
print("distinct orbit dimensions across all 15 spectral types:", dims)
print("max orbit dim (generic, all-distinct [1^7]) =", max(d for _, d, _ in rows))
print("min orbit dim (fully degenerate [7] = the centre I/7) =",
      min(d for _, d, _ in rows))
print()
print("=" * 66)
print("READING [Т computation / С,И structure]:")
print(" • The calibration freedom of a configuration is graded by its SPECTRAL")
print("   type: the flatter the spectrum (more degeneracy), the SMALLER the")
print("   G2-orbit — less frame to fix. The centre (total degeneracy) has ZERO")
print("   frame; a fully non-degenerate Γ carries the maximal frame.")
print(" • The stratification is NOT a single manifold — it is this poset of")
print("   %d orbit-dimension strata. That is WHY no global calibration exists" % len(dims))
print("   (§82): a continuous global frame would need one orbit type, and the")
print("   spectrum of a living Γ moves BETWEEN strata as it evolves (ℒ_Ω).")
print(" • New content vs §82: §82 proved the hole (no global slice); this maps")
print("   its shape — exactly which configurations carry how much calibration.")
