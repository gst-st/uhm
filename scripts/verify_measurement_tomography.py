#!/usr/bin/env python3
"""Exact witnesses and executable checks for measurement.md section 6.4.

No native builds, statistical coverage simulation or Lean/Verum proof claims.
Run with OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 <this file>.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import importlib.util
import math
import unittest

import numpy as np


SOURCE = Path(__file__).resolve().parents[1] / "website/static/code/gamma_tomography.py"
SPEC = importlib.util.spec_from_file_location("gamma_tomography", SOURCE)
gt = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(gt)


class ExactWitnesses(unittest.TestCase):
    def test_sample_centering_breaks_unbiased_pair_numerator(self):
        expectation = F(0)
        for a, b in product([F(-1), F(1)], repeat=2):
            mean = (a + b) / 2
            expectation += ((a - mean) * (b - mean)) ** 2 / 4
        self.assertEqual(expectation, F(1, 2))
        self.assertNotEqual(expectation, F(1))  # population variance squared

    def test_ratio_bias_need_not_be_negative(self):
        # iid +/-e1, +/-3e2, with probabilities9/20,9/20,1/20,1/20.
        # Zero mean, M=diag(9/10,9/10), population purity1/2.
        dist = [(F(9, 20), (F(s), F(0))) for s in [-1, 1]]
        dist += [(F(1, 20), (F(0), F(3 * s))) for s in [-1, 1]]
        pair_mean = F(0)
        ratio_mean = F(0)
        for (pa, a), (pb, b) in product(dist, repeat=2):
            kernel = sum(x * y for x, y in zip(a, b)) ** 2
            trace = (sum(x*x for x in a) + sum(x*x for x in b)) / 2
            pair_mean += pa * pb * kernel
            ratio_mean += pa * pb * kernel / trace**2
            X = np.zeros((2, 7))
            X[0, :2], X[1, :2] = a, b
            self.assertAlmostEqual(gt.purity_pair_ratio(X), float(kernel / trace**2))
        self.assertEqual(pair_mean, F(81, 50))  # Tr(M^2), numerator unbiased
        self.assertEqual(ratio_mean, F(41, 50))
        self.assertEqual(ratio_mean - F(1, 2), F(8, 25))

    def test_operator_normalization_counterexample_and_valid_bound(self):
        M = [F(94, 100)] + [F(1, 100)] * 6
        t = F(1, 100)
        A = [M[0]] + [x + t for x in M[1:]]
        error = max(abs(a / sum(A) - m / sum(M)) for a, m in zip(A, M))
        self.assertEqual(error, F(141, 2650))
        self.assertGreater(error, 2 * t / sum(M))
        self.assertLessEqual(error, 8 * t / sum(M))

    def test_distinct_quadruples_unbiased_for_covariance_numerator(self):
        # A nonzero mean tests genuine covariance rather than second moment.
        outcomes = [(F(1, 3), F(1)), (F(2, 3), F(4))]
        mean = sum(p*x for p, x in outcomes)
        variance = sum(p*(x-mean)**2 for p, x in outcomes)
        expectation = F(0)
        for a, b, c, d in product(outcomes, repeat=4):
            weight = a[0] * b[0] * c[0] * d[0]
            expectation += weight * ((a[1]-b[1])*(c[1]-d[1]))**2 / 4
        self.assertEqual(expectation, variance**2)


class ReferenceImplementation(unittest.TestCase):
    def setUp(self):
        self.ratings = np.vstack((np.eye(7), np.eye(7))) + 2

    def test_complex_second_moment_keeps_phase_orientation(self):
        x = np.array([1, 1j, 0, 0, 0, 0, 0], dtype=complex)
        expected = np.outer(x, x.conj())
        np.testing.assert_array_equal(gt.sigma_hat(x[None, :]), expected)
        self.assertEqual(gt.sigma_hat(x[None, :])[0, 1], -1j)
        np.testing.assert_allclose(gt.gamma_hat(x[None, :]), expected / 2)

    def test_centering_translation_and_pair_plugin_identity(self):
        out = gt.analyse(self.ratings, center=True)
        shifted = gt.analyse(self.ratings + 5, center=True)
        np.testing.assert_allclose(out["Gamma"], shifted["Gamma"], atol=1e-14)
        self.assertAlmostEqual(out["P_plugin"], 1 / 6)
        self.assertAlmostEqual(out["P_pair_ratio"], 4 / 39)
        self.assertLess(out["P_pair_ratio"], 1 / 7)  # no hidden clipping
        self.assertAlmostEqual(out["R_plugin"], 1 / (7 * out["P_plugin"]))
        self.assertIsNone(out["confidence"])
        self.assertEqual(out["target"], "normalized_covariance")

    def test_point_functionals_share_one_matrix(self):
        out = gt.analyse(self.ratings, center=True)
        self.assertAlmostEqual(out["P_plugin"], np.trace(out["Gamma"] @ out["Gamma"]).real)
        self.assertAlmostEqual(out["Phi_plugin"], gt.integration(out["Gamma"]))
        self.assertAlmostEqual(out["Coh_E_plugin"], gt.coh_E(out["Gamma"]))

    def test_pair_ratio_complex_oracle_and_scale_invariance(self):
        rng = np.random.default_rng(43)
        X = rng.normal(size=(9, 7)) + 1j * rng.normal(size=(9, 7))
        trace = sum(np.vdot(x, x).real for x in X) / len(X)
        off = sum(abs(np.vdot(a, b))**2 for i, a in enumerate(X)
                  for j, b in enumerate(X) if i != j)
        expected = off / (len(X) * (len(X)-1) * trace**2)
        for scale in [1e-100, 1.0, 1e100]:
            with self.subTest(scale=scale):
                self.assertAlmostEqual(gt.purity_pair_ratio(X * scale), expected)

    def test_centered_constant_is_undefined_at_any_sample_count(self):
        for count in [1, 2, 14, 100]:
            with self.subTest(count=count), self.assertRaises(ValueError):
                gt.analyse(np.full((count, 7), 8), center=True)

    def test_constant_uncentered_moment_is_a_different_target(self):
        out = gt.analyse(np.full((14, 7), 8))
        self.assertEqual(out["target"], "normalized_second_moment")
        self.assertAlmostEqual(out["P_plugin"], 1)
        self.assertIsNone(out["confidence"])

    def test_centering_cannot_request_iid_confidence(self):
        with self.assertRaisesRegex(ValueError, "centering"):
            gt.analyse(self.ratings, center=True, iid_norm2_bound=100)

    def test_constant_energy_does_not_grant_confidence(self):
        X = np.zeros((40, 7))
        X[:20, 0] = np.tile([1, -1], 10)
        X[20:, 1] = np.tile([1, -1], 10)
        np.testing.assert_array_equal(np.sum(X**2, axis=1), np.ones(40))
        self.assertIsNone(gt.analyse(X)["confidence"])

    def test_short_iid_region_is_explicitly_uninformative(self):
        region = gt.iid_confidence_region(np.eye(7), B=1)
        self.assertEqual(region["purity_interval"], (1 / 7, 1))
        self.assertEqual(region["gamma_operator_radius"], 1)
        self.assertTrue(region["state_available"])

    def test_zero_observed_trace_has_full_region_and_no_matrix_center(self):
        region = gt.iid_confidence_region(np.zeros((2, 7)), B=1)
        self.assertFalse(region["state_available"])
        self.assertIsNone(region["gamma_operator_radius"])
        self.assertEqual(region["purity_interval"], (1 / 7, 1))

    def test_iid_region_solves_bernstein_inequality(self):
        X = np.zeros((8192, 7))
        X[:, 0] = 1
        region = gt.iid_confidence_region(X, B=1, delta=0.05)
        t = region["moment_operator_radius"]
        log_tail = math.log(14) - len(X) * t*t / (2 + 4*t/3)
        self.assertLessEqual(log_tail, math.log(0.05) + 1e-12)
        self.assertGreater(region["population_trace_lower"], 0)
        self.assertLess(region["gamma_operator_radius"], 1)

    def test_budget_is_sufficient_not_the_previous_unit_constant(self):
        B, tau, eps, delta = 2.0, 0.5, 0.2, 0.05
        count = gt.bernstein_N(B, tau, eps, delta)
        t = tau * eps / 8
        log_tail = math.log(14) - count * t*t / (2*B*B + 4*B*t/3)
        self.assertLessEqual(log_tail, math.log(delta))
        self.assertLess(7*t, tau)  # normalized matrix exists on the good event
        old_budget = B*B / (tau*tau*eps*eps) * math.log(14/delta)
        self.assertGreater(count, old_budget)

    def test_invalid_population_contract_is_rejected(self):
        for B, delta in [(0, .05), (-1, .05), (math.inf, .05),
                         (math.nan, .05), (1, 0), (1, 1), (1, math.nan)]:
            with self.subTest(B=B, delta=delta), self.assertRaises(ValueError):
                gt.iid_confidence_region(np.eye(7), B, delta)
        with self.assertRaisesRegex(ValueError, "violates"):
            gt.iid_confidence_region(2 * np.eye(7), B=1)

    def test_invalid_observation_is_rejected(self):
        for X in [np.zeros((0, 7)), np.zeros((2, 6)), np.zeros(7),
                  np.full((2, 7), math.nan), np.full((2, 7), math.inf)]:
            with self.subTest(shape=X.shape), self.assertRaises(ValueError):
                gt.analyse(X)

    def test_unsupported_confidence_api_has_no_compatibility_fallback(self):
        for name in ["ci_halfwidth", "n_eff", "tau_corr_batch_means", "purity_unbiased"]:
            self.assertFalse(hasattr(gt, name), name)
        with self.assertRaises(TypeError):
            gt.analyse(self.ratings, series=np.ones(len(self.ratings)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
