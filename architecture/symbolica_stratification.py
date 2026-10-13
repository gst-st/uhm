# -*- coding: utf-8 -*-
"""Sample orbit ranks within spectral families; deliberately not a classification.

Spectral multiplicities classify unitary conjugacy only after eigenvalues are
specified. They do not classify the smaller G2 action. Even the same full-rank
spectrum [6,1] has orbit dimensions 6 and 11, certified by exact controls in
symbolica_frame_bundle.py. Random eigenframes supply numerical witnesses only.
The largest rank seen in six samples is not a proof of the generic maximum,
a stabilizer conjugacy classification, or absence of a global quotient section.
"""
import numpy as np
from symbolica_frame_bundle import (N, ALGEBRA_TOL, ORBIT_TOL, build_g2,
                                    orbit_dim, exact_controls)


def partitions(n, mx=None):
    if mx is None:
        mx = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, mx), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest


def sample_ranks(part, basis, rng, trials=6):
    """One positive spectrum, six random unitary frames; retain every seen rank."""
    eigs = np.concatenate([np.repeat(value, multiplicity)
                           for value, multiplicity in zip(np.linspace(1, 2, len(part)), part)])
    eigs /= eigs.sum()
    ranks = []
    for _ in range(trials):
        a = rng.standard_normal((N, N)) + 1j * rng.standard_normal((N, N))
        q, _ = np.linalg.qr(a)
        gamma = (q * eigs) @ q.conj().T
        assert np.allclose(np.linalg.eigvalsh(gamma), np.sort(eigs))
        ranks.append(orbit_dim(gamma, basis))
    return ranks


def main():
    if not __debug__:
        raise RuntimeError('Controls require enabled assertions; do not run with -O')
    basis, constraints, so7 = build_g2()
    exact_controls(basis, constraints, so7)
    rng = np.random.default_rng(7)
    print('G2 ORBIT-RANK SAMPLES: NOT THE FULL STRATIFICATION')
    print('Exact controls: real pure orbit 6; complex pure orbit 11; centre 0; distinct positive diagonal 14.')
    print('Equal full-rank [6,1] spectrum admits both orbit dimensions 6 and 11.')
    print('SVD tolerances:', ALGEBRA_TOL, ORBIT_TOL, '; seed: 7; six frames per spectrum')
    print('%-20s %-22s %-10s' % ('multiplicities', 'six witnessed ranks', 'rank Gamma'))
    all_ranks = set()
    count = 0
    for part in partitions(N):
        ranks = sample_ranks(part, basis, rng)
        all_ranks.update(ranks)
        count += 1
        print('%-20s %-22s %d' % (str(part), str(ranks), N))
    assert count == 15
    print('Sampled 15 multiplicity partitions, one positive spectrum each.')
    print('Numerical ranks witnessed by these samples:', sorted(all_ranks))
    print('The exact real-axis controls add orbit dimension 6, which the random')
    print('complex eigenframes can miss. Neither list is an exhaustive set of types.')
    print('No claim of a three-stratum quotient, a spectral classification,')
    print('a global-section obstruction, or a phenomenological calibration theorem.')


if __name__ == '__main__':
    main()
