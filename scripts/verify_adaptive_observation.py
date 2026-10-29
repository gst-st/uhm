#!/usr/bin/env python3
"""Exact finite witnesses for UHM instrument and phase-tangent scope.

These rational identities/counterexamples are not a proof of quantum dynamics,
Petz classification, physical gravity or a native Verum certificate.
"""
from fractions import Fraction as F
import json


def mat(rows):
    return [[F(x) for x in row] for row in rows]


def scale(c, a):
    return [[c*x for x in row] for row in a]


def add(a, b):
    return [[x+y for x, y in zip(r, s)] for r, s in zip(a, b)]


def mul(a, b):
    return [[sum(x*y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def dissipator(l, x):
    ll = mul(l, l)
    return add(mul(mul(l, x), l), scale(F(-1, 2), add(mul(ll, x), mul(x, ll))))


def rank(rows):
    rows = [list(map(F, row)) for row in rows]
    pivot = 0
    for column in range(len(rows[0])):
        selected = next((i for i in range(pivot, len(rows)) if rows[i][column]), None)
        if selected is None:
            continue
        rows[pivot], rows[selected] = rows[selected], rows[pivot]
        divisor = rows[pivot][column]
        rows[pivot] = [value/divisor for value in rows[pivot]]
        for i in range(pivot+1, len(rows)):
            factor = rows[i][column]
            rows[i] = [a-factor*b for a,b in zip(rows[i], rows[pivot])]
        pivot += 1
        if pivot == len(rows):
            break
    return pivot


def tomography(n):
    # Coordinates: n-1 diagonal entries, then real/imaginary off-diagonal pairs.
    # The last diagonal entry is minus the sum (trace-zero tangent).
    pairs = [(i,j) for i in range(n) for j in range(i+1,n)]
    width = n*n-1
    diagonal = [[F(i==j) if i<n-1 else F(-1) for j in range(n-1)]
                + [F(0)]*(2*len(pairs)) for i in range(n)]
    real, imaginary = [], []
    for k,(i,j) in enumerate(pairs):
        base = [(a+b)/2 for a,b in zip(diagonal[i],diagonal[j])]
        r, q = base.copy(), base.copy()
        r[n-1+k] = F(1)
        q[n-1+len(pairs)+k] = F(-1)
        real.append(r)
        imaginary.append(q)
    assert all(len(row)==width for row in diagonal+real+imaginary)
    return [rank(diagonal),rank(diagonal+real),rank(diagonal+real+imaginary)]


def main():
    eye = mat([[1, 0], [0, 1]])
    z = mat([[1, 0], [0, -1]])
    ps = [mat([[1, 0], [0, 0]]), mat([[0, 0], [0, 1]])]
    for i in range(2):
        for j in range(2):
            e = mat([[int((a,b)==(i,j)) for b in range(2)] for a in range(2)])
            assert add(dissipator(ps[0], e), dissipator(ps[1], e)) == scale(F(1,2), dissipator(z,e))
    rho = scale(F(1,2),eye)
    variances = []
    for instrument in [[(F(1), p) for p in ps], [(F(1,2), eye), (F(1,2), z)]]:
        variance = F(0)
        for weight, l in instrument:
            raw = mul(mul(l,rho),l)
            rate = trace(raw)
            jump = scale(1/rate,raw)
            variance += weight*rate*(jump[0][0]-rho[0][0])**2
        variances.append(variance)
    assert variances == [F(1,4),F(0)]
    purities = [sum(x*x for x in state) for state in [[F(1,7)]*7,[F(3,4)]+[F(1,24)]*6]]
    assert purities == [F(1,7),F(55,96)]
    assert purities[0]<F(2,7) and purities[1]>F(3,7)
    # X=i*x, L=i*l. No complex approximation is needed for the exact SLD equation.
    rho3 = mat([[F(1,3),0,F(1,12)],[0,F(1,3),0],[F(1,12),0,F(1,3)]])
    x = mat([[0,0,F(1,12)],[0,0,0],[-F(1,12),0,0]])
    l = scale(3,x)
    assert scale(F(1,2),add(mul(rho3,l),mul(l,rho3))) == x
    qfi = -trace(mul(rho3,mul(l,l)))
    norm = -trace(mul(x,x))
    assert rho3[0][1]==0 and qfi==F(1,24) and norm==F(1,72)
    assert norm/F(5,12)<=qfi<=norm/F(1,4)
    ranks = tomography(7)
    assert ranks == [6,27,48]
    print('проверок: 8')
    print(json.dumps({'status':'passed','arithmetic':'exact fractions','matrix_basis_cases':4,
        'same_generator_variances':list(map(str,variances)), 'purities':list(map(str,purities)),
        'charge_selected_pair_coherence':'0','charge_qfi':str(qfi),
        'charge_bounds':[str(norm/F(5,12)),str(norm/F(1,4))],
        'tomography_ranks':ranks},indent=2))


if __name__ == '__main__':
    main()
