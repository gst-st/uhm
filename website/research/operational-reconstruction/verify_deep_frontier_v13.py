"""
Deep Frontier Verification Suite v13 — Unified Runner (`verify_deep_frontier_v13.py`):
  Module 1 (`frontier_v13_null_cone.py`, 24/24 checks):
    Wall 1 Stratum C null-cone quantization audit, 4D multi-harmonic divergence & Riemann
    summation-order obstructions (`A1.4A-C`), species-cutoff split (`A1.5`), bare-vs-induced
    symplectic degeneracy no-go (`A1.7`), exact 1-loop 4D Schwarzschild Sen `C_log` sign
    trichotomy (`A1.8-A1.10`), finite Type `I_{d(A)}` deepening of `T-348` (`A1.11-A1.12`),
    and Lorentzian cobordism realizations of `B4` `CM-1/2/4` (`A1.13-A1.17`).
  Module 2 (`frontier_v13_left_null.py`, 31/31 checks, 0% float64, zero math/numpy/scipy):
    Choice-free parametric Left-Null / Bareiss / IPS / Farkas obstruction certificates:
    4D Regge+KD `B_5` Bose-Mesner 40x40 & 45x45 flat-(1,5) split, pure-integer `F-36A`
    all-ratio PV certificates, zero-float `V12.1.B6` scalar thresholds, and higher-curvature
    `alpha Weyl^2` / 4th-order Stelle exact Bezout zero-exception refutations (Models B1/B2).
  Module 3 (`frontier_v13_dyadic_cert.py`, 142/142 checks, 0% float64, 0 math/numpy/scipy):
    Pure-integer outward-rounded dyadic interval certificates aligned with Lean 4
    `ConstructiveR` (`DyadicIntervalCert`): `Super-F-40` & `V12.1.B` spectral-action ghost
    enclosures, `F-36B` Kallen-Lehmann negativity to 25 digits, exact analytical 4D deformed
    `S^4` Regge-Schlafli 40x40 inertia `(10, 0, 30)` via 12-bit zero-division `U[H]U^T`,
    `R-18` Lagarias/Li/Mertens bounds, and full continuum PDG +/-1sigma 2-loop `Chain A2`
    variational-ODE Krawczyk + Richardson-Banach certification.

Default execution runs all 3 modules in isolated subprocesses (`197/197` checks, `fitted_parameters = 0`).
Pass `--fast` for a fast CI subset (Module 1 full + Module 2 full + Module 3 Targets 0, 2, 3 = `85/85`).

Run with:
  PYTHONDONTWRITEBYTECODE=1 python3 -B verify_deep_frontier_v13.py
  PYTHONDONTWRITEBYTECODE=1 python3 -B verify_deep_frontier_v13.py --fast
"""

from __future__ import annotations

import os
from pathlib import Path
import re
import subprocess
import sys
import time


HERE = Path(__file__).resolve().parent

MODULES = (
    ("Module 1: Null-Cone QG, Sen C_log, Type I T-348 & B4", "frontier_v13_null_cone.py", 24, 24),
    ("Module 2: Exact Left-Null / IPS / Farkas Certificates", "frontier_v13_left_null.py", 31, 31),
    ("Module 3: Pure-Integer Dyadic Interval Certificates", "frontier_v13_dyadic_cert.py", 142, 30),
)

COUNT_RE = re.compile(r"(\d+)/(\d+)\s+(?:checks|CHECKS)\s+(?:PASSED|passed)")


def run_module(title: str, filename: str, expected_checks: int, fast: bool) -> tuple[bool, int, int, float]:
    script_path = HERE / filename
    cmd = [sys.executable, "-B", str(script_path)]
    if fast and filename == "frontier_v13_dyadic_cert.py":
        cmd.append("--fast")

    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"

    print("=" * 90)
    print(f"RUNNING {title} ({filename}{' --fast' if fast and filename == 'frontier_v13_dyadic_cert.py' else ''})")
    print("=" * 90, flush=True)

    t0 = time.perf_counter()
    proc = subprocess.run(cmd, env=env, capture_output=True, text=True)
    dt = time.perf_counter() - t0

    if proc.stdout:
        print(proc.stdout, end="" if proc.stdout.endswith("\n") else "\n")
    if proc.stderr:
        print(proc.stderr, file=sys.stderr, end="" if proc.stderr.endswith("\n") else "\n")

    matches = COUNT_RE.findall(proc.stdout or "")
    if matches:
        passed, total = int(matches[-1][0]), int(matches[-1][1])
    else:
        passed, total = 0, expected_checks

    ok = (proc.returncode == 0) and (passed == total) and (total == expected_checks)
    if not ok:
        print(
            f"[FAIL] {filename}: returncode={proc.returncode}, parsed={passed}/{total}, expected={expected_checks}",
            file=sys.stderr,
        )
    return ok, passed, total, dt


def main() -> int:
    fast = "--fast" in sys.argv[1:]
    t_start = time.perf_counter()

    total_passed = 0
    total_checks = 0
    all_ok = True
    results = []

    for title, filename, full_n, fast_n in MODULES:
        expected = fast_n if fast else full_n
        ok, passed, total, dt = run_module(title, filename, expected, fast)
        results.append((filename, ok, passed, total, dt))
        total_passed += passed
        total_checks += total
        all_ok = all_ok and ok

    total_dt = time.perf_counter() - t_start
    mode_str = " [FAST CI MODE]" if fast else ""
    print("=" * 90)
    print(f"DEEP FRONTIER v13 UNIFIED SUMMARY{mode_str}:")
    for filename, ok, passed, total, dt in results:
        tag = "PASS" if ok else "FAIL"
        print(f"  [{tag}] {filename:<30s} {passed:3d}/{total:<3d}  ({dt:6.2f}s)")
    print("-" * 90)
    print(
        f"TOTAL: {total_passed}/{total_checks} CHECKS PASSED "
        f"(fitted_parameters = 0, total runtime {total_dt:.2f}s)"
    )
    print("=" * 90)
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
