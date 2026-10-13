# -*- coding: utf-8 -*-
"""Calibration research: counts, variable orbit freedom and observation contracts.

G2 has dimension 14 and 12 roots, but its orbit at a state has dimension
14 - dim(stabilizer). Neither count makes 7+12 symbolic labels a coordinate
chart, nor identifies human qualia with an unobservable G2-frame. A fixed
measurement or action may break the kinematic symmetry. Environmental inputs
can be tested in a calibration model; no planetary/phenomenal bridge is proved.

This script shares exact finite orbit controls with symbolica_frame_bundle.py.
A separate numerical directional-derivative witness shows how a fixed population
observable can vary under a G2 generator. It makes no claim about qualia.
"""
import math
import numpy as np
from symbolica_frame_bundle import N, build_g2, orbit_dim, exact_controls


def main():
    if not __debug__:
        raise RuntimeError('Controls require enabled assertions; do not run with -O')
    roots = [(r * math.cos(k * math.pi / 6), r * math.sin(k * math.pi / 6))
             for k in range(12) for r in [1 if k % 2 == 0 else math.sqrt(3)]]
    short = sum(abs(math.hypot(*v) - 1) < 1e-12 for v in roots)
    assert len(roots) == 12 and short == 6
    basis, constraints, so7 = build_g2()
    p_real, p_complex = exact_controls(basis, constraints, so7)
    assert N * N - 1 == 48 and len(basis) == 14
    dimensions = [('centre I/7', np.eye(N) / N, 0),
                  ('real pure projector', p_real, 6),
                  ('fixed complex pure projector', p_complex, 11),
                  ('positive distinct diagonal', np.diag(np.arange(1, N + 1)) / 28, 14)]
    print('CALIBRATION: STRUCTURAL CONTROLS, NOT A PHENOMENAL THEOREM')
    print('G2 roots: 12 (six short, six long); Cartan rank: 2; Lie dimension: 14.')
    print('Framed density-state interior: 48 real coordinates.')
    for name, gamma, expected in dimensions:
        actual = orbit_dim(gamma, basis)
        assert actual == expected
        print('%-32s orbit=%2d stabilizer Lie dimension=%2d'
              % (name, actual, 14 - actual))

    # A fixed population observable q(Gamma)=Gamma[0,0] need not descend
    # to the kinematic quotient. Choose a nonzero generator coefficient,
    # not a semantic word or data label. Gamma remains strictly positive.
    x, j = max(((x, j) for x in basis for j in range(1, N)),
               key=lambda pair: abs(pair[0][0, pair[1]]))
    epsilon = 1 / 28
    gamma = np.eye(N) / N
    gamma[0, j] = gamma[j, 0] = epsilon
    assert np.min(np.linalg.eigvalsh(gamma)) > 0 and np.isclose(np.trace(gamma), 1)
    derivative = (x @ gamma - gamma @ x)[0, 0]
    assert np.isclose(derivative, 2 * epsilon * x[0, j]) and abs(derivative) > 1e-8
    print('Numerical fixed-observable witness: d/dt q(exp(tX) Gamma exp(-tX))')
    print('at t=0 is', float(derivative), ', not zero (chosen generator, fixed q).')
    print('A physical gauge requires retained observations, action domains and')
    print('dynamics to descend; conjugation symmetry of the carrier is insufficient.')
    print('The 7+12 symbol counts supply no coordinate chart or qualia identity.')
    print('Research hypothesis [I]: qualitative reports may constrain a relational')
    print('alignment. Test observations and interventions with unresolved symmetries')
    print('retained; environmental variables are optional empirical inputs [H].')
    print('No result here establishes that a planetary system fixes experience.')


if __name__ == '__main__':
    main()
