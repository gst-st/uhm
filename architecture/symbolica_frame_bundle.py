# -*- coding: utf-8 -*-
"""G2 conjugation: orbit-rank witnesses and the precise frame obstruction.

The ranks are kinematics of a declared group action, not a model of qualia.
Varying stabilizers do not rule out an ordinary section of the orbit quotient:
SO(2) acting on R^2 has the continuous radius section r -> (r, 0).
A G-valued equivariant frame F(g.x)=gF(x) is a different object. It cannot exist
at a point with nontrivial stabilizer, in particular at Gamma=I/7 for G=G2.
Neither fact says that environmental or planetary data determine experience.

The Fano three-form and tangent map are shared with symbolica_stratification.
Small exact rational controls certify orbit dimensions 0, 6, 11 and 14; SVD probes
supply additional numerical witnesses, never a complete orbit classification.
"""
from fractions import Fraction
from itertools import combinations, permutations
import numpy as np

N = 7
ALGEBRA_TOL = 1e-9
ORBIT_TOL = 1e-8


def build_g2():
    """Return a numerical basis, its exact integer constraints, and so(7) basis."""
    triples = sorted({tuple(sorted(((i + d) % N for d in (0, 1, 3))))
                      for i in range(N)})
    assert len(triples) == 7
    phi = np.zeros((N, N, N), dtype=int)
    for line in triples:
        for p in permutations(line):
            phi[p] = (-1) ** sum(p[i] > p[j]
                                for i in range(3) for j in range(i + 1, 3))
    so7 = []
    for m, n in combinations(range(N), 2):
        x = np.zeros((N, N), dtype=int)
        x[m, n], x[n, m] = 1, -1
        so7.append(x)
    columns = []
    for x in so7:
        action = (np.einsum('ip,pjk->ijk', x, phi)
                  + np.einsum('jp,ipk->ijk', x, phi)
                  + np.einsum('kp,ijp->ijk', x, phi))
        columns.append(action.reshape(-1))
    constraints = np.stack(columns, axis=1)
    _, values, vt = np.linalg.svd(constraints, full_matrices=False)
    rank = int((values > ALGEBRA_TOL).sum())
    basis = [sum(c * x for c, x in zip(row, so7)) for row in vt[rank:]]
    assert len(basis) == 14
    return basis, constraints, so7


def commutator_columns(gamma, basis):
    columns = []
    for x in basis:
        b = x @ gamma - gamma @ x
        columns.append(np.concatenate((b.real.reshape(-1), b.imag.reshape(-1))))
    return np.stack(columns, axis=1)


def orbit_dim(gamma, basis):
    """Numerical tangent rank; tolerance is explicit, no stabilizer classification."""
    values = np.linalg.svd(commutator_columns(gamma, basis), compute_uv=False)
    return int((values > ORBIT_TOL).sum())


def integer_rank(matrix):
    """Exact Q-rank of an integer matrix; reject noninteger input, never round it."""
    assert np.all(np.isfinite(matrix)) and np.all(matrix == np.trunc(matrix))
    rows = [[Fraction(int(x)) for x in row] for row in matrix if np.any(row)]
    if not rows:
        return 0
    rank = 0
    for column in range(len(rows[0])):
        pivot = next((j for j in range(rank, len(rows)) if rows[j][column]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        divisor = rows[rank][column]
        rows[rank] = [x / divisor for x in rows[rank]]
        for j in range(rank + 1, len(rows)):
            multiplier = rows[j][column]
            if multiplier:
                rows[j] = [x - multiplier * y for x, y in zip(rows[j], rows[rank])]
        rank += 1
    return rank


def exact_controls(basis, constraints, so7):
    """rank(B|ker A)=rank([A;B])-rank(A), all entries exactly integral here."""
    algebra_rank = integer_rank(constraints)
    assert 21 - algebra_rank == 14
    axis = np.zeros(N, dtype=complex)
    axis[0] = 1
    complex_axis = axis.copy()
    complex_axis[1] = 2j
    real_numerator = np.outer(axis, axis.conj())
    complex_numerator = np.outer(complex_axis, complex_axis.conj())
    fixtures = [('centre (unnormalized I)', np.eye(N), 0),
                ('real axis pure projector', real_numerator, 6),
                ('complex pure numerator', complex_numerator, 11),
                ('positive distinct diagonal numerator', np.diag(np.arange(1, N + 1)), 14)]
    for name, numerator, expected in fixtures:
        b = commutator_columns(numerator, so7)
        actual = integer_rank(np.vstack((constraints, b))) - algebra_rank
        assert actual == expected, (name, actual, expected)
        assert orbit_dim(numerator, basis) == expected
    p_real = real_numerator
    p_complex = complex_numerator / 5
    for p, expected in ((p_real, 6), (p_complex, 11)):
        assert np.allclose(p @ p, p) and np.isclose(np.trace(p), 1)
        assert orbit_dim(p, basis) == expected
    # Same full-rank [6,1] eigenvalue multiplicities, different orbit dimensions.
    # [X, I/14 + P/2] = [X,P]/2, so the rank equality is also exact analytically.
    a = np.eye(N) / 14 + p_real / 2
    b = np.eye(N) / 14 + p_complex / 2
    assert np.allclose(np.linalg.eigvalsh(a), np.linalg.eigvalsh(b))
    assert np.min(np.linalg.eigvalsh(a)) > 0 and np.isclose(np.trace(a), 1)
    assert orbit_dim(a, basis) == 6 and orbit_dim(b, basis) == 11
    return p_real, p_complex


def main():
    if not __debug__:
        raise RuntimeError('Controls require enabled assertions; do not run with -O')
    basis, constraints, so7 = build_g2()
    p_real, p_complex = exact_controls(basis, constraints, so7)
    rng = np.random.default_rng(7)

    def random_state(rank=None):
        a = rng.standard_normal((N, N)) + 1j * rng.standard_normal((N, N))
        h = a @ a.conj().T
        if rank is not None:
            values, vectors = np.linalg.eigh(h)
            values[:-rank] = 0
            h = (vectors * values) @ vectors.conj().T
        return h / np.trace(h).real

    print('G2 CONJUGATION: WITNESSES, NOT AN ORBIT CLASSIFICATION')
    print('Exact integer constraints: dim g2 = 14; exact orbit controls = 0, 6, 11, 14')
    print('SVD tolerances:', ALGEBRA_TOL, ORBIT_TOL, '; random seed: 7')
    rows = [('centre I/7', np.eye(N) / N),
            ('real axis pure projector', p_real),
            ('fixed complex pure projector', p_complex),
            ('sampled complex pure projector', random_state(rank=1)),
            ('sampled rank-3 state', random_state(rank=3)),
            ('sampled full-rank state', random_state())]
    witnessed = set()
    for name, gamma in rows:
        dimension = orbit_dim(gamma, basis)
        witnessed.add(dimension)
        print('%-36s orbit rank=%2d stabilizer Lie dimension=%2d'
              % (name, dimension, 14 - dimension))
    assert 0 in witnessed and 6 in witnessed and 11 in witnessed
    print('Numerically witnessed orbit dimensions:', sorted(witnessed))
    print('Different dimensions imply different orbit types; equal dimensions')
    print('do not identify stabilizer conjugacy classes or exhaust the types.')
    print('Same positive spectrum [6,1]: exact orbit ranks 6 and 11.')
    print('Ordinary section counterexample: SO(2) on R^2, s(r)=(r,0).')
    print('Equivariant G-valued frame: F(g.x)=gF(x) is impossible at I/7,')
    print('since g fixes I/7 and left multiplication fixes no group element.')
    print('No conclusion about ordinary global sections for this G2 quotient,')
    print('or about human qualia / environmental calibration, follows from ranks.')


if __name__ == '__main__':
    main()
