#!/usr/bin/env python3
"""П-ТЕНЕВЫЕ-МЕТКИ-1 (МАТ): чувствительность κ_OE/κ_OU к третьим
точкам канонических осевых прямых. Детерминировано (сид 20260807).
Оси хранения: [A,S,D,L,E,O,U] = индексы 0..6 (O=5, U=6)."""
import numpy as np

N = 7
AX = "ASDLEOU"
# канонические ОСЕВЫЕ прямые (трансляты QR(7) при U=6, O=7 → индексы)
FANO_AX = [(0,1,3),(1,2,4),(2,3,6),(3,4,5),(4,6,0),(6,5,1),(5,0,2)]
# абстрактный набор моста (контроль)
FANO_AB = [(0,1,2),(0,3,4),(0,5,6),(1,3,5),(1,4,6),(2,3,6),(2,4,5)]

def bibd_ok(lines):
    from itertools import combinations
    pairs = {}
    for t in lines:
        for a, b in combinations(sorted(t), 2):
            pairs[(a, b)] = pairs.get((a, b), 0) + 1
    return len(pairs) == 21 and set(pairs.values()) == {1}

def ops(lines):
    o = []
    for i in range(N):
        L = np.zeros((N, N)); L[i, i] = 1.0; o.append(L)
    for ln in lines:
        P = np.zeros((N, N))
        for m in ln: P[m, m] = 1.0
        o.append(P / np.sqrt(3))
    return o

def kappa(lam, o, gamma=1.0):
    rho = np.diag(lam); K = np.zeros((N, N))
    for L in o:
        M = L @ rho @ L.T; tr = np.trace(M)
        if tr < 1e-15: continue
        d = np.diag(M / tr - rho)
        K += (gamma * tr / N) * np.outer(d, d)
    return K

def sens(lam, o, i, j, eps=1e-6):
    """S_x = d kappa_ij / d lam_x вдоль центрированных направлений."""
    out = np.zeros(N)
    for x in range(N):
        v = -np.ones(N) / N; v[x] += 1.0          # e_x - u/7 (симплекс)
        K1 = kappa(lam + eps * v, o); K0 = kappa(lam - eps * v, o)
        out[x] = (K1[i, j] - K0[i, j]) / (2 * eps)
    return out

def third(lines, a, b):
    for t in lines:
        if a in t and b in t:
            return [x for x in t if x not in (a, b)][0]
    return None

def run(tag, lines):
    assert bibd_ok(lines), tag
    o = ops(lines)
    O, E, U = 5, 4, 6
    tOE, tOU = third(lines, O, E), third(lines, O, U)
    print(f"— {tag}: прямая(O,E)∋{AX[tOE]} · прямая(O,U)∋{AX[tOU]}")
    rng = np.random.default_rng(20260807)
    for (i, j, t3, nm) in [(O, E, tOE, "κ_OE"), (O, U, tOU, "κ_OU")]:
        u = np.ones(N) / N
        s0 = sens(u, o, i, j)
        others = [x for x in range(N) if x not in (i, j)]
        best0 = max(others, key=lambda x: abs(s0[x]))
        wins_max = 0; wins_min = 0; M = 300
        rng2 = np.random.default_rng(20260808)
        for _ in range(M):
            lam = rng2.dirichlet(np.ones(N))
            s = sens(lam, o, i, j)
            if max(others, key=lambda x: abs(s[x])) == t3:
                wins_max += 1
            if min(others, key=lambda x: abs(s[x])) == t3:
                wins_min += 1
        gap = s0[best0] - s0[t3]
        print(f"  {nm}: I/7 разрыв прочие−третья = {gap:+.6e} "
              f"(аналитика γ/189 = {1/189:+.6e}) · сид-20260808: "
              f"argmax побед {wins_max}/{M} · ЭКРАН argmin побед "
              f"{wins_min}/{M} ({100*wins_min/M:.0f}%)")

print("П-ТЕНЕВЫЕ-МЕТКИ-1 (сид 20260807, ε=1e-6, γ=1)")
run("КАНОНИЧЕСКИЕ осевые", FANO_AX)
run("АБСТРАКТНЫЕ (контроль)", FANO_AB)
