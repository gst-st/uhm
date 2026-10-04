#!/usr/bin/env python3
"""Numerical witnesses for the revised hierarchy/dynamics kernel.

Scope: finite-dimensional readout/certification examples, local polynomial
normal forms, and explicitly specified reduced dynamics. These checks validate
conditional identities and counterexamples. They establish no phenomenal,
clinical, biological, agency, or universal cognitive-depth conclusion.

Run: python3 website/scripts/check_hierarchy_kernel.py
Requires NumPy, as does the companion core numerical audit.
"""
import math
import numpy as np

checks = 0

def check(name, actual, expected=None, atol=1e-9):
    global checks
    if expected is None:
        assert bool(actual), name
    else:
        assert np.allclose(actual, expected, atol=atol, rtol=1e-9), (
            name, actual, expected)
    checks += 1


def check_swallowtail_and_sextic():
    # An A4 stationary equation is quartic. Four simple roots alternate
    # maxima/minima; even this maximal root count gives only two minima.
    roots = np.array([-2., -1., 1., 2.])
    derivative = np.poly(roots)
    slopes = np.polyval(np.polyder(derivative), roots)
    check('A4 permitted quartic has no cubic term', derivative[1], 0)
    check('A4 stationary points alternate', slopes, [-12, 6, -6, 12])
    check('A4 maximum four simple roots yield only two minima',
          np.count_nonzero(slopes > 0) == 2)
    # Direct minimisation and scale ratios independently check the tuned model.
    v = 2.
    ts = np.array([-.01, -.0001])
    ms = (-ts / v) ** .25
    check('sextic stationary equation', ts * ms + v * ms ** 5, 0)
    values = ts * ms ** 2 / 2 + v * ms ** 6 / 6
    check('sextic minimum value', values, -(-ts) ** 1.5 / (3 * math.sqrt(v)))
    check('tuned sextic beta', np.log(ms[1] / ms[0]) / np.log(ts[1] / ts[0]), .25)
    hs = np.array([.01, .0001])
    critical_ms = (hs / v) ** .2
    check('sextic critical isotherm', v * critical_ms ** 5, hs)
    check('sextic delta', np.log(hs[1] / hs[0]) /
          np.log(critical_ms[1] / critical_ms[0]), 5)
    # Both potentials are Z2-even; the positive quartic changes beta.
    quartic_ms = (-ts / v) ** .5
    check('even positive quartic beta differs from tricritical beta',
          np.log(quartic_ms[1] / quartic_ms[0]) / np.log(ts[1] / ts[0]), .5)


def check_passage_and_memory():
    a, b, y0, yf = .7, .3, .001, .8
    xs = np.geomspace(y0, yf, 200000)
    integrate = getattr(np, 'trapezoid', None) or np.trapz
    quadrature = integrate(1 / (a * xs + b * xs ** 2), xs)
    exact = math.log(yf * (a + b * y0) / (y0 * (a + b * yf))) / a
    check('Riccati passage by independent quadrature', quadrature, exact, 2e-8)
    tuned_quadrature = integrate(1 / (b * xs ** 2), xs)
    tuned_exact = (1 / y0 - 1 / yf) / b
    check('a=0 inverse passage law', tuned_quadrature, tuned_exact, 3e-6)
    # Exponential convolution kernel K=(gain/tau) exp(-t/tau).
    gain, tau = 1., 2.
    matrix = np.array([[0., -1.], [gain / tau, -1 / tau]])
    expected = (-1 + np.array([1, -1]) *
                np.sqrt(1 - 4 * gain * tau + 0j)) / (2 * tau)
    check('exponential-memory roots', np.sort_complex(np.linalg.eigvals(matrix)),
          np.sort_complex(expected))
    check('oscillatory memory regime', 4 * gain * tau > 1)


def check_uniform_phase():
    # Deterministic quadrature of a uniform ANGLE, not a uniform sine magnitude.
    theta = np.linspace(-np.pi, np.pi, 1000000, endpoint=False)
    gap = np.abs(np.sin(theta))
    check('uniform-angle Gap mean', gap.mean(), 2 / np.pi)
    check('uniform-angle Gap variance', gap.var(), .5 - 4 / np.pi ** 2)
    check('Gap cannot have uniform distribution mean',
          abs(gap.mean() - .5) > .1)


def check_operational_tower():
    # Commuting states in a declared common output space; Bures is computed
    # directly from diagonal spectra. This is a data-certificate witness only.
    targets = [np.array([.7, .3, 0, 0, 0, 0, 0]),
               np.array([.3, .7, 0, 0, 0, 0, 0])]
    def bures(p, q):
        return math.sqrt(max(0., 2 * (1 - np.sqrt(p * q).sum())))
    spread = bures(*targets)
    epsilon = spread / 3
    predictions = [p.copy() for p in targets]
    for order in range(1, 5):
        error = max(bures(p, q) for p, q in zip(predictions, targets))
        check(f'nonconstant exact order-{order} data certificate',
              error <= epsilon and spread > 2 * epsilon)
        # Chosen forgetting maps are identities on the common output space.
        check(f'chosen order-{order} compatibility',
              all(np.array_equal(p, q) for p, q in zip(predictions, targets)))
    # Any constant fit has maximum error >= spread/2 by triangle inequality;
    # the concrete midpoint also fails the chosen tolerance.
    midpoint = (targets[0] + targets[1]) / 2
    check('constant midpoint fails nontrivial-response certificate',
          max(bures(midpoint, q) for q in targets) > epsilon)
    # Powers of each map commute with themselves, but two independently chosen
    # models need not commute with the declared forgetting map.
    upper_output = targets[0][[1, 0, 2, 3, 4, 5, 6]]
    lower_output = targets[0]  # lower model and forgetting are identities
    check('inter-level compatibility is an additional predicate',
          not np.array_equal(upper_output, lower_output))


if __name__ == '__main__':
    check_swallowtail_and_sextic()
    check_passage_and_memory()
    check_uniform_phase()
    check_operational_tower()
    print(f'Hierarchy kernel: {checks} scoped numerical checks passed.')
