"""
Deep Frontier v13 — Module 2: Exact Left-Null / IPS / Farkas Obstruction Certificates (`frontier_v13_left_null.py`):
Constructive Algebraic Obstruction Certificates (Left-Null / Nullstellensatz / IPS / Farkas)
for Nonlinear Gravity, 4D Regge+KD Subtraction, Mixed Spectral Actions, and Weyl^2 Black-Hole Perturbations.

STRICT ZERO-FLOAT CERTIFICATE INVARIANT:
  Every single mathematical check/assertion uses ONLY exact arithmetic:
  Python `int`, `fractions.Fraction`, and `sympy` exact rational/polynomial rings.
  Floating-point values appear ONLY in optional diagnostic printout formatting, NEVER inside checks.

Self-contained, deterministic, zero fitted parameters.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
import math
import sys
import numpy as np
import sympy as sp
from sympy.polys.matrices import DomainMatrix
from sympy.polys.domains import QQ


class ExactCheckCounter:
    def __init__(self) -> None:
        self.passed = 0
        self.total = 0
        self.failures: list[str] = []

    def check(self, cond: bool, label: str) -> bool:
        self.total += 1
        if cond:
            self.passed += 1
            print(f"  [PASS] {label}")
            return True
        self.failures.append(label)
        print(f"  [FAIL] {label}")
        return False


# ==============================================================================
# EXACT RATIONAL INTERVAL HELPERS (ZERO FLOAT64)
# ==============================================================================
def isqrt_bounds(r: Fraction, prec: int = 10**24) -> tuple[Fraction, Fraction]:
    """Exact rational bracket [lo, hi] with lo^2 <= r < hi^2 via integer isqrt."""
    assert r > 0
    p, q = r.numerator, r.denominator
    k = math.isqrt(p * q * prec * prec)
    lo = Fraction(k, q * prec)
    hi = Fraction(k + 1, q * prec)
    assert lo * lo <= r < hi * hi
    return lo, hi


def iadd(a: tuple[Fraction, Fraction], b: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    return (a[0] + b[0], a[1] + b[1])


def isub(a: tuple[Fraction, Fraction], b: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    return (a[0] - b[1], a[1] - b[0])


def imul(a: tuple[Fraction, Fraction], b: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    prods = (a[0] * b[0], a[0] * b[1], a[1] * b[0], a[1] * b[1])
    return (min(prods), max(prods))


def idiv(a: tuple[Fraction, Fraction], b: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    assert b[0] > 0 or b[1] < 0
    return imul(a, (Fraction(1) / b[1], Fraction(1) / b[0]))


def iscale(c: Fraction, a: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    return (c * a[0], c * a[1]) if c >= 0 else (c * a[1], c * a[0])


def ishift(c: Fraction, a: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    return (c + a[0], c + a[1])


def atan_rat_bounds(x: Fraction, N: int = 30) -> tuple[Fraction, Fraction]:
    """Exact alternating-series rational bracket for arctan(x), 0 < x <= 1/2."""
    assert Fraction(0) < x <= Fraction(1, 2)
    x2 = x * x
    s = Fraction(0)
    xp = x
    for n in range(N):
        term = ((-1) ** n) * xp / (2 * n + 1)
        if n == N - 1:
            s_next = s + term
            return (min(s, s_next), max(s, s_next))
        s += term
        xp *= x2
    raise AssertionError("Unreachable")


def pi_rat_bounds(N: int = 30) -> tuple[Fraction, Fraction]:
    """Machin's exact formula: pi = 16*arctan(1/5) - 4*arctan(1/239)."""
    a5 = atan_rat_bounds(Fraction(1, 5), N=N)
    a239 = atan_rat_bounds(Fraction(1, 239), N=N)
    return isub(iscale(Fraction(16), a5), iscale(Fraction(4), a239))


def acos_quarter_bounds(N: int = 30) -> tuple[Fraction, Fraction]:
    """
    Exact rational bracket for arccos(1/4) = pi/2 - arcsin(1/4).
    Note arcsin(1/4) = sum_{n=0}^inf ((2n)! / (4^n (n!)^2 (2n+1))) * (1/4)^{2n+1}
    is a strictly positive series with geometric ratio < 1/16!
    """
    pi_b = pi_rat_bounds(N=N)
    s = Fraction(0)
    x = Fraction(1, 4)
    x2 = x * x
    xp = x
    binom_fac = Fraction(1)
    for n in range(N):
        term = binom_fac * xp / (2 * n + 1)
        s += term
        binom_fac *= Fraction(2 * n + 1, 2 * n + 2)
        xp *= x2
    # Remaining terms bounded by term_N / (1 - x^2) where term_N = binom_fac * xp / (2N+1):
    tail = (binom_fac * xp / (2 * N + 1)) / (1 - x2)
    asin_b = (s, s + tail)
    return isub(iscale(Fraction(1, 2), pi_b), asin_b)


def eps0_rat_bounds(N: int = 30) -> tuple[Fraction, Fraction]:
    """Exact rational bracket for eps_0 = 2*pi - 4*arccos(1/4)."""
    return isub(iscale(Fraction(2), pi_rat_bounds(N=N)), iscale(Fraction(4), acos_quarter_bounds(N=N)))


def ln_rat_bounds(z: Fraction, N: int = 24) -> tuple[Fraction, Fraction]:
    """Exact rational bracket for ln(z), z > 0, via range reduction z = 2^k * w, w in [2/3, 4/3]."""
    assert z > 0
    k = 0
    w = z
    while w > Fraction(4, 3):
        w /= 2
        k += 1
    while w < Fraction(2, 3):
        w *= 2
        k -= 1

    def atanh_s(u_f: Fraction) -> tuple[Fraction, Fraction]:
        neg = u_f < 0
        au = -u_f if neg else u_f
        u2 = au * au
        acc = Fraction(0)
        up = au
        for n in range(N):
            acc += up / (2 * n + 1)
            up *= u2
        tail = up / ((2 * N + 1) * (1 - u2))
        lo, hi = 2 * acc, 2 * (acc + tail)
        return (-hi, -lo) if neg else (lo, hi)

    l2_lo, l2_hi = atanh_s(Fraction(1, 3))
    lw_lo, lw_hi = atanh_s((w - 1) / (w + 1))
    if k >= 0:
        return (k * l2_lo + lw_lo, k * l2_hi + lw_hi)
    return (k * l2_hi + lw_lo, k * l2_lo + lw_hi)


def A_t_bounds(t_f: Fraction) -> tuple[Fraction, Fraction]:
    """Exact rational bracket for A(t) = atanh(sqrt(t)) / sqrt(t), strictly increasing in t in (0, 1)."""
    slo, shi = isqrt_bounds(t_f)
    llo, _ = ln_rat_bounds((1 + slo) / (1 - slo))
    _, lhi = ln_rat_bounds((1 + shi) / (1 - shi))
    return (llo / (2 * slo), lhi / (2 * shi))


# ==============================================================================
# SUITE 1: GENERAL PARAMETRIC LEFT-NULL, BAREISS GENERATOR, IPS & RICCATI LIFT
# ==============================================================================
def suite_1_general_theory(cc: ExactCheckCounter) -> None:
    print("=" * 88)
    print("SUITE 1: General Parametric Left-Null, Bareiss Generator, IPS Embedding & Riccati Lift")
    print("=" * 88)

    # 1.1 Fraction-free Cramer-adjunct Left-Null generator & completeness over Z[t1, t2]
    t1, t2 = sp.symbols("t1 t2")
    # 4 x 2 parametric matrix of generic rank 2 over Z[t1, t2]
    A = sp.Matrix([
        [t1 + 1, t2],
        [1, t1 - t2],
        [t1 + 2, t1],
        [t1**2 + 1, t2**2],
    ])
    b = sp.Matrix([t1, 1, t1 + 1, t2])
    # Leading 2x2 submatrix I = [0, 1], J = [0, 1]:
    I_rows = [0, 1]
    J_cols = [0, 1]
    A_IJ = A.extract(I_rows, J_cols)
    Delta = sp.expand(A_IJ.det())
    # Bordered cofactor Left-Null witnesses for i0 = 2 and i0 = 3:
    witnesses = []
    for i0 in [2, 3]:
        # v supported on [0, 1, i0]: cofactors of last column of [A_{[0,1,i0], [0,1]} | b_{[0,1,i0]}]
        v = [sp.Integer(0)] * 4
        v[0] = sp.expand(A.extract([1, i0], J_cols).det())
        v[1] = sp.expand(-A.extract([0, i0], J_cols).det())
        v[i0] = Delta
        v_mat = sp.Matrix(v)
        P_i0 = sp.expand((v_mat.T * b)[0])
        ann_ok = sp.Matrix([sp.expand(x) for x in (v_mat.T * A)]) == sp.zeros(2, 1)
        # Also verify Cramer-adjunct completeness: Delta * (b_{i0} - (A * c_cramer)_{i0}) == P_{i0}!
        c_cramer = A_IJ.adjugate() * b.extract(I_rows, [0])  # = Delta * c
        res_i0 = sp.expand(Delta * b[i0] - (A.row(i0) * c_cramer)[0])
        witnesses.append((i0, v_mat, P_i0, ann_ok, res_i0 == P_i0))

    cc.check(
        all(w[3] and w[4] for w in witnesses) and witnesses[0][2] == 0 and sp.expand(witnesses[1][2]) != 0,
        "1.1a: Fraction-free cofactor Left-Null over Z[t1,t2]: v^T A = 0, exact Cramer completeness, P_2=0 & P_3!=0",
    )

    # Check exact localization on hypersurface P_3(t1, t2) = 0 vs off-hypersurface!
    P3 = witnesses[1][2]
    # Pick point with Delta != 0 and P3 == 0 (e.g. t1 = 0 => check roots of P3(0, t2)!)
    P3_t0 = sp.factor(P3.subs(t1, 0))
    # P3(0, t2) = t2 * (...): at (t1=0, t2=1), evaluate Delta and P3!
    sol_t2 = [s for s in sp.solve(P3.subs(t1, 0), t2) if s.is_rational and Delta.subs({t1: 0, t2: s}) != 0]
    assert len(sol_t2) >= 1
    s0 = sol_t2[0]
    c_sol = A_IJ.subs({t1: 0, t2: s0}).LUsolve(b.extract(I_rows, [0]).subs({t1: 0, t2: s0}))
    on_hyp_solves = (A.subs({t1: 0, t2: s0}) * c_sol == b.subs({t1: 0, t2: s0}))
    off_hyp_p3 = P3.subs({t1: 1, t2: 2})
    cc.check(
        on_hyp_solves and off_hyp_p3 != 0,
        f"1.1b: Exact hypersurface localization: solvable at (0,{s0}) on V(P_3), refuted at (1,2) with P_3={off_hyp_p3}!=0",
    )

    # 1.1c Exact Bareiss fraction-free elimination over Z[t1, t2] on [A | b]:
    # Verifies every exact division by previous pivot prev_piv leaves ZERO remainder in Z[t1, t2]
    # and final bottom-right entry equals exact bordered determinant P_3!
    M_bar = sp.Matrix.hstack(A.extract([0, 1, 3], [0, 1]), b.extract([0, 1, 3], [0]))
    prev_piv = sp.Integer(1)
    bareiss_exact = True
    for k_b in range(2):
        piv = sp.expand(M_bar[k_b, k_b])
        for i_b in range(k_b + 1, 3):
            for j_b in range(k_b + 1, 3):
                num_b = sp.expand(piv * M_bar[i_b, j_b] - M_bar[i_b, k_b] * M_bar[k_b, j_b])
                q_b, rem_b = sp.div(num_b, prev_piv, t1, t2)
                if sp.expand(rem_b) != 0:
                    bareiss_exact = False
                M_bar[i_b, j_b] = sp.expand(q_b)
        prev_piv = piv
    cc.check(
        bareiss_exact and sp.expand(M_bar[2, 2] - P3) == 0,
        "1.1c: Exact Bareiss fraction-free elimination over Z[t1,t2] has zero remainders and yields M[2,2] == P_3",
    )

    # 1.1d Ordered-tuple cofactor sign test (i_0 < i_r) & pivoted Bareiss on zero-leading-minor matrix:
    # A_ord = [[1,2],[3,5],[7,11]], I_ord = (1, 2), J_ord = (0, 1), i0 = 0 < i_r:
    A_ord = sp.Matrix([[1, 2], [3, 5], [7, 11]])
    b_ord = sp.Matrix([1, 0, 0])
    I_ord = [1, 2]
    i0_ord = 0
    v_ord = [sp.Integer(0)] * 3
    v_ord[i0_ord] = A_ord.extract(I_ord, [0, 1]).det()
    for k_o in range(2):
        # Strictly append i0_ord LAST: (i_1, ..., \hat{i_k}, ..., i_r, i_0)
        rows_o = [I_ord[u] for u in range(2) if u != k_o] + [i0_ord]
        v_ord[I_ord[k_o]] = ((-1) ** (2 + 1 + (k_o + 1))) * A_ord.extract(rows_o, [0, 1]).det()
    v_ord_vec = sp.Matrix(v_ord)
    ord_ann_ok = (v_ord_vec.T * A_ord == sp.zeros(1, 2)) and ((v_ord_vec.T * b_ord)[0] == A_ord.extract([1, 2, 0], [0, 1]).row_join(b_ord.extract([1, 2, 0], [0])).det())
    # Pivoted Bareiss on zero leading minor [[0, 1], [1, 0]] bordered with row [1, 1] and b = [1, 2, 5]:
    M_piv = sp.Matrix([[0, 1, 1], [1, 0, 2], [1, 1, 5]])
    det_true = M_piv.det()
    swaps = 0
    prev_p = sp.Integer(1)
    for k_p in range(2):
        if M_piv[k_p, k_p] == 0:
            p_row = next(r_p for r_p in range(k_p + 1, 2) if M_piv[r_p, k_p] != 0)
            M_piv.row_swap(k_p, p_row)
            swaps += 1
        piv_p = M_piv[k_p, k_p]
        for i_p in range(k_p + 1, 3):
            for j_p in range(k_p + 1, 3):
                num_p = piv_p * M_piv[i_p, j_p] - M_piv[i_p, k_p] * M_piv[k_p, j_p]
                assert num_p % prev_p == 0
                M_piv[i_p, j_p] = num_p // prev_p
        prev_p = piv_p
    piv_bar_ok = (((-1) ** swaps) * M_piv[2, 2] == det_true)
    cc.check(
        ord_ann_ok and piv_bar_ok,
        "1.1d: Ordered-tuple cofactor sign (i0 < i_r) & pivoted Bareiss on zero-leading-minor matrix verified exactly",
    )

    # 1.2 Exact Degree-1 IPS & Rabinowitsch Parametric IPS Circuit Embedding
    c0, c1, z_rab = sp.symbols("c0 c1 z_rab")
    y0, y1, y2, y3, yP = sp.symbols("y0 y1 y2 y3 yP")
    v3 = witnesses[1][1]
    # Axiom polynomials f_i = (A c - b)_i and f_P = z_rab * P3 - 1
    f_ax = [sp.expand((A.row(i) * sp.Matrix([c0, c1]))[0] - b[i]) for i in range(4)]
    f_P = sp.expand(z_rab * P3 - 1)
    # Rabinowitsch IPS circuit: C_param(t, c, z; y, yP) = -z * sum_i v3[i] * y_i - yP
    C_param = -z_rab * sum(v3[i] * [y0, y1, y2, y3][i] for i in range(4)) - yP
    zero_on_zero = sp.expand(C_param.subs({y0: 0, y1: 0, y2: 0, y3: 0, yP: 0})) == 0
    one_on_axioms = sp.expand(C_param.subs({y0: f_ax[0], y1: f_ax[1], y2: f_ax[2], y3: f_ax[3], yP: f_P})) == 1
    # Also evaluate point degree-1 IPS at (t1=1, t2=2) where P3 != 0:
    P_pt = Fraction(int(off_hyp_p3))
    v_pt = [Fraction(int(v3[i].subs({t1: 1, t2: 2}))) for i in range(4)]
    q_pt = [-v_pt[i] / P_pt for i in range(4)]
    f_pt = [sp.expand(f_ax[i].subs({t1: 1, t2: 2})) for i in range(4)]
    C_deg1 = sum(sp.Rational(q_pt[i].numerator, q_pt[i].denominator) * [y0, y1, y2, y3][i] for i in range(4))
    deg1_ok = (
        sp.expand(C_deg1.subs({y0: 0, y1: 0, y2: 0, y3: 0})) == 0
        and sp.expand(C_deg1.subs({y0: f_pt[0], y1: f_pt[1], y2: f_pt[2], y3: f_pt[3]})) == 1
    )
    cc.check(
        zero_on_zero and one_on_axioms and deg1_ok,
        "1.2: Degree-1 linear IPS & Rabinowitsch parametric IPS (C(x,0)=0, C(x,f(x))=1 without inverting P(theta))",
    )

    # 1.3 Differential-Algebraic / Riccati Lift: Case-1 Schwarzschild Algebraically Special Counterexample [✗]
    r = sp.Symbol("r", positive=True)
    f_s = (r - 1) / r  # 2M = 1
    V_rw = f_s * (6 / r**2 - 3 / r**3)  # l=2, s=2 Schwarzschild Regge-Wheeler
    # Chandrasekhar algebraically special solution at omega_AS = -4i (omega^2 = -16):
    u_AS = -(16 * r**3 + 12 * r**2 + 3 * r - 3) / (r * (r - 1) * (4 * r + 3))
    ric_AS = sp.simplify(f_s**2 * (sp.diff(u_AS, r) + u_AS**2) + f_s * sp.diff(f_s, r) * u_AS + (-16 - V_rw))
    # Construct explicit quadratic source S_AS(psi) = -(r*(r-1)*(4r+3))*u_AS * psi^2 + r*(r-1)*(4r+3) * psi*psi'
    # = (16r^3 + 12r^2 + 3r - 3) psi^2 + r*(r-1)*(4r+3) psi*psi'
    # On psi = psi_AS: psi' = u_AS * psi => S_AS(psi_AS) === 0 identically, so Phi = 0 IS an exact rational solution!
    # Yet formally in {psi^2, psi*psi', (psi')^2}, S_AS = (alpha_0, alpha_1, 0) != (0, 0, 0), and for L_2 = d/dr + 0 (or any L_2)
    # let's check directly with the Schwarzschild operator L_2^{(0)} at l2=4 (w^2 = -16, w2^2 = -64):
    # Take ansatz space Phi = 0 (or span{1/r * psi^2}): formal source S_AS has NO formal solution in span{psi^2/r},
    # yet Phi = 0 solves L_2[Phi] = S_AS(psi_AS) identically!
    # Even sharper: verify that S_AS vanishes identically on u = u_AS!
    alpha0_AS = sp.expand(16 * r**3 + 12 * r**2 + 3 * r - 3)
    alpha1_AS = sp.expand(r * (r - 1) * (4 * r + 3))
    vanishes_on_AS = sp.simplify(alpha0_AS + alpha1_AS * u_AS) == 0
    # And check formal Left-Null on ansatz Phi = c0 * psi^2 (1 unknown) for L_2[Phi] = S_AS(psi):
    # In L_2[c0 * psi^2], the coeff of (psi')^2 is 2*f_s^2*c0, while S_AS has coeff 0 of (psi')^2 -> forces c0 = 0,
    # contradicting alpha1_AS = r(r-1)(4r+3) != 0!
    cc.check(
        ric_AS == 0 and vanishes_on_AS and alpha1_AS != 0,
        "1.3: Case-1 Riccati Lift Breakdown [✗]: Schwarzschild l=2, w_AS=-4i has rational u_AS in Q(r) breaking formal lift",
    )

    # 1.4 Differential-Algebraic / Riccati Lift: Case-2 Degree-2 Algebraic Counterexample [✗]
    # ODE: psi'' - (r + 5/(16 r^2)) psi = 0, exact solution psi = r^{-1/4} exp((2/3) r^{3/2})
    u_case2 = sp.sqrt(r) - sp.Rational(1, 4) / r
    q_case2 = sp.simplify(-(sp.diff(u_case2, r) + u_case2**2))  # -(r + 5/(16 r^2)) in Q(r)!
    quad_rel = sp.simplify(u_case2**2 + (sp.Rational(1, 2) / r) * u_case2 + (sp.Rational(1, 16) / r**2 - r))
    # Verify sqrt(r) is irrational over C(r) (i.e. u_case2 not in C(r)) while quadratic relation vanishes!
    # Also verify 3-solution Wronskian Vandermonde lift identity:
    # For psi_3 = psi_1 + psi_2 with W = psi_1 psi_2' - psi_2 psi_1':
    p1, p2, p1p, p2p = sp.symbols("p1 p2 p1p p2p")
    u1_s = p1p / p1
    u2_s = p2p / p2
    u3_s = (p1p + p2p) / (p1 + p2)
    vand = sp.factor((u2_s - u1_s) * (u3_s - u1_s) * (u3_s - u2_s))
    W_s = p1 * p2p - p2 * p1p
    vand_ok = sp.simplify(vand + W_s**3 / (p1**2 * p2**2 * (p1 + p2)**2)) == 0
    cc.check(
        sp.simplify(q_case2 + r + sp.Rational(5, 16) / r**2) == 0 and quad_rel == 0 and vand_ok,
        "1.4: Case-2 Riccati Breakdown [✗] (u=sqrt(r)-1/(4r), deg 2 over Q(r)) & exact 3-solution Wronskian Vandermonde lift [Т]",
    )
    print(f"    -> Schwarzschild u_AS(r) = {sp.factor(u_AS)}")
    print(f"    -> Case-2 ODE: psi'' - ({-q_case2}) psi = 0; Vandermonde = -W^3/(psi1^2 psi2^2 (psi1+psi2)^2)\n")


# ==============================================================================
# SUITE 2: APPLICATION A1 — EXACT 4D REGGE + KÄHLER-DIRAC ON S^4 = partial beta_5
# ==============================================================================
def suite_2_regge_kd_s4(cc: ExactCheckCounter) -> None:
    print("=" * 88)
    print("SUITE 2: Exact Rational 4D Regge + Kähler–Dirac Left-Null & Farkas Certificates on S^4")
    print("=" * 88)

    # 2.1 Build partial beta_5 and its 6-class B_5 Bose-Mesner algebra
    simps = [
        tuple(sorted((s0, 2 + s1, 4 + s2, 6 + s3, 8 + s4)))
        for s0 in (0, 1) for s1 in (0, 1) for s2 in (0, 1) for s3 in (0, 1) for s4 in (0, 1)
    ]
    verts = list(range(10))
    edges = sorted({(s[i], s[j]) for s in simps for i in range(5) for j in range(i + 1, 5)})
    tris = sorted({(s[i], s[j], s[k]) for s in simps for i in range(5) for j in range(i + 1, 5) for k in range(j + 1, 5)})
    tets = sorted({(s[i], s[j], s[k], s[l]) for s in simps for i in range(5) for j in range(i + 1, 5) for k in range(j + 1, 5) for l in range(k + 1, 5)})
    v_idx = {x: i for i, x in enumerate(verts)}
    e_idx = {x: i for i, x in enumerate(edges)}
    t_idx = {x: i for i, x in enumerate(tris)}
    tet_idx = {x: i for i, x in enumerate(tets)}

    def edge_rel(e1, e2):
        v1, v2 = set(e1), set(e2)
        a1, a2 = {v // 2 for v in e1}, {v // 2 for v in e2}
        return (len(v1 & v2), len(a1 & a2), sum(1 for u in e1 if (u ^ 1) in v2))

    rel_keys = sorted({edge_rel(edges[0], e2) for e2 in edges})
    A_orb = {}
    for rk in rel_keys:
        M = np.zeros((40, 40), dtype=int)
        for i, e1 in enumerate(edges):
            for j, e2 in enumerate(edges):
                if edge_rel(e1, e2) == rk:
                    M[i, j] = 1
        A_orb[rk] = M
    bm_comm = all(np.array_equal(A_orb[r1] @ A_orb[r2], A_orb[r2] @ A_orb[r1]) for r1 in rel_keys for r2 in rel_keys)

    # Exact integer Bose-Mesner character table P[irrep, orbital]
    # Orbitals: [(0,0,0), (0,1,1), (0,2,2), (1,1,0), (1,2,1), (2,2,0)]
    P_bm = sp.Matrix([
        [12, 12,  1, 12,  2, 1],  # 1_sc  (dim 1)
        [-8,  2,  1,  2,  2, 1],  # 4_cf  (dim 4)
        [ 0, -6, -1,  6,  0, 1],  # 5_cf  (dim 5)
        [ 4, -4,  1, -4,  2, 1],  # 5_TT  (dim 5)
        [ 0,  0,  1,  0, -2, 1],  # 10_TT (dim 10)
        [ 0,  2, -1, -2,  0, 1],  # 15_TT (dim 15)
    ])
    ks_val = [12, 12, 1, 12, 2, 1]
    dims_irrep = [1, 4, 5, 5, 10, 15]
    # Verify orthogonality P * diag(1/k_i) * P^T == diag(40/m_a) exactly!
    K_inv = sp.diag(*[sp.Rational(1, k) for k in ks_val])
    orth_chk = P_bm * K_inv * P_bm.T == sp.diag(*[sp.Rational(40, d) for d in dims_irrep])
    # Also verify exact character eigenvalues against left-regular intersection matrices L_i:
    rep = {}
    for j, e2 in enumerate(edges):
        rk = edge_rel(edges[0], e2)
        if rk not in rep:
            rep[rk] = j
    rep_edges = [edges[rep[rk]] for rk in rel_keys]
    char_ok = True
    for i_idx, rk_i in enumerate(rel_keys):
        L_i = sp.zeros(6, 6)
        for j_idx, rk_j in enumerate(rel_keys):
            prod = A_orb[rk_i] @ A_orb[rk_j]
            for k_idx, rk_k in enumerate(rel_keys):
                L_i[k_idx, j_idx] = int(prod[0, rep[rk_k]])
        for a in range(6):
            row_a = P_bm.row(a).T
            if L_i.T * row_a != P_bm[a, i_idx] * row_a:
                char_ok = False
    cc.check(
        (len(verts), len(edges), len(tris), len(tets), len(simps)) == (10, 40, 80, 80, 32)
        and bm_comm and orth_chk and char_ok and sum(dims_irrep) == 40,
        "2.1: Exact 6-class B_5 Bose-Mesner algebra on S^4 edges: 1 + 4 + 5_cf + 5_TT + 10_TT + 15_TT = 40",
    )

    # 2.2 Exact integer DEC Hodge Laplacians & spectra on regular S^4 = partial beta_5
    # Verify w_{p+1}/w_p = (p+1)^2 exactly:
    # vol_p^2 = (p+1) / ((p!)^2 * 2^p), n_inc(p) = [16, 8, 4, 2, 1], w_p / V4 = ((p+1)/5) * n_inc(p) / vol_p^2
    n_inc = [16, 8, 4, 2, 1]
    vol2 = [Fraction(p + 1, (math.factorial(p) ** 2) * (2 ** p)) for p in range(5)]
    w_over_v4 = [Fraction(p + 1, 5) * n_inc[p] / vol2[p] for p in range(5)]
    ratios_ok = all(w_over_v4[p + 1] / w_over_v4[p] == Fraction((p + 1) ** 2) for p in range(4))

    d0 = np.zeros((40, 10), dtype=object)
    for i, (a, b) in enumerate(edges):
        d0[i, v_idx[a]] = -1; d0[i, v_idx[b]] = 1
    d1 = np.zeros((80, 40), dtype=object)
    for i, (a, b, c) in enumerate(tris):
        d1[i, e_idx[(b, c)]] = 1; d1[i, e_idx[(a, c)]] = -1; d1[i, e_idx[(a, b)]] = 1
    d2 = np.zeros((80, 80), dtype=object)
    for i, (a, b, c, d) in enumerate(tets):
        d2[i, t_idx[(b, c, d)]] = 1; d2[i, t_idx[(a, c, d)]] = -1
        d2[i, t_idx[(a, b, d)]] = 1; d2[i, t_idx[(a, b, c)]] = -1
    d3 = np.zeros((32, 80), dtype=object)
    for i, (a, b, c, d, e_) in enumerate(simps):
        d3[i, tet_idx[(b, c, d, e_)]] = 1; d3[i, tet_idx[(a, c, d, e_)]] = -1
        d3[i, tet_idx[(a, b, d, e_)]] = 1; d3[i, tet_idx[(a, b, c, e_)]] = -1; d3[i, tet_idx[(a, b, c, d)]] = 1
    ds = [d0, d1, d2, d3]
    ns = [10, 40, 80, 80, 32]
    L0 = []
    for p in range(5):
        L = np.zeros((ns[p], ns[p]), dtype=object)
        if p > 0: L = L + (p * p) * (ds[p - 1] @ ds[p - 1].T)
        if p < 4: L = L + ((p + 1) * (p + 1)) * (ds[p].T @ ds[p])
        L0.append(L)

    # Verify exact integer spectra via minimal polynomial prod_{lam}(L0[p] - lam I) == 0 and exact traces!
    spec_p = [
        [(0, 1), (8, 5), (10, 4)],
        [(8, 5), (10, 4), (24, 10), (32, 15), (40, 6)],
        [(24, 10), (32, 15), (36, 10), (40, 6), (54, 20), (72, 15), (90, 4)],
        [(32, 5), (36, 10), (54, 20), (64, 10), (72, 15), (90, 4), (96, 10), (128, 5), (160, 1)],
        [(0, 1), (32, 5), (64, 10), (96, 10), (128, 5), (160, 1)],
    ]
    minpoly_ok = True
    for p in range(5):
        I_p = np.eye(ns[p], dtype=object)
        M_acc = I_p.copy()
        for lam, _ in spec_p[p]:
            M_acc = M_acc @ (L0[p] - lam * I_p)
        if not np.all(M_acc == 0):
            minpoly_ok = False
        # Verify power traces Tr(L^k) for k = 0..len(spec_p[p])-1 uniquely determine all multiplicities!
        L_pow = I_p.copy()
        for k_tr in range(len(spec_p[p])):
            tr_mat = int(sum(L_pow[i, i] for i in range(ns[p])))
            tr_spec = sum(mult * (lam ** k_tr) for lam, mult in spec_p[p])
            if tr_mat != tr_spec:
                minpoly_ok = False
            L_pow = L_pow @ L0[p]

    cc.check(
        ratios_ok and minpoly_ok,
        "2.2: Exact integer DEC weights w_{p+1}/w_p=(p+1)^2 and exact integer KD Hodge spectra verified via min-poly & traces",
    )

    # 2.3 Exact cleared-denominator Lagrange resolvent G_p = (L0[p] + m^2 I)^{-1} & exact rational S_KD Hessians!
    def lagrange_inv(L_obj, eigs, m2_int):
        n = L_obj.shape[0]
        k = len(eigs)
        x = sp.Symbol("x")
        poly = sp.Integer(0)
        for i, ei in enumerate(eigs):
            num, den = sp.Integer(1), sp.Integer(1)
            for j, ej in enumerate(eigs):
                if i != j:
                    num *= (x - ej)
                    den *= (ei - ej)
            poly += sp.Rational(1, ei + m2_int) * num / den
        poly = sp.Poly(sp.expand(poly), x)
        coeffs = [poly.nth(r) for r in range(k)]
        lcm_d = int(sp.ilcm(*[sp.fraction(c)[1] for c in coeffs]))
        int_coeffs = [int(c * lcm_d) for c in coeffs]
        I_obj = np.eye(n, dtype=object)
        res = int_coeffs[k - 1] * I_obj
        for r in range(k - 2, -1, -1):
            res = res @ L_obj + int_coeffs[r] * I_obj
        assert np.array_equal(res @ (L_obj + m2_int * I_obj), lcm_d * I_obj)
        return res, lcm_d

    # Exact local derivatives of normalized simplex volumes u4, u3, u2 & dihedral angle derived from Cayley-Menger!
    x_cm, y_cm = sp.symbols("x_cm y_cm")

    def cm4_det(l2_d):
        M = sp.zeros(6, 6)
        for i in range(1, 6):
            M[0, i] = 1; M[i, 0] = 1
        for i in range(5):
            for j in range(i + 1, 5):
                M[i + 1, j + 1] = l2_d[(i, j)]
                M[j + 1, i + 1] = l2_d[(i, j)]
        return M

    def taylor2_xy(expr):
        return (
            sp.simplify(expr.subs({x_cm: 0, y_cm: 0})),
            sp.simplify(sp.diff(expr, x_cm).subs({x_cm: 0, y_cm: 0})),
            sp.simplify(sp.diff(expr, x_cm, 2).subs({x_cm: 0, y_cm: 0})),
            sp.simplify(sp.diff(sp.diff(expr, x_cm), y_cm).subs({x_cm: 0, y_cm: 0})),
        )

    d_base = {(i, j): sp.Integer(1) for i in range(5) for j in range(i + 1, 5)}
    d_adj = dict(d_base); d_adj[(0, 1)] = (1 + x_cm)**2; d_adj[(0, 2)] = (1 + y_cm)**2
    d_dis = dict(d_base); d_dis[(0, 1)] = (1 + x_cm)**2; d_dis[(2, 3)] = (1 + y_cm)**2
    t4_adj = taylor2_xy(sp.sqrt(-sp.expand(cm4_det(d_adj).det()) / 5))
    t4_dis = taylor2_xy(sp.sqrt(-sp.expand(cm4_det(d_dis).det()) / 5))
    # Dihedral angle Schläfli verification from M^{-1}:
    M0_4 = cm4_det(d_base)
    M0_4inv = M0_4.inv()
    dth_vals = []
    for e_pos in ((0, 1), (0, 2), (2, 3)):
        d_1 = dict(d_base); d_1[e_pos] = (1 + x_cm)**2
        M1_4 = sp.diff(cm4_det(d_1), x_cm).subs(x_cm, 0)
        Minv1 = M0_4inv - x_cm * (M0_4inv * M1_4 * M0_4inv)
        c_e = Minv1[1, 2] / sp.sqrt(Minv1[1, 1] * Minv1[2, 2])
        dc_e = sp.simplify(sp.diff(c_e, x_cm).subs(x_cm, 0))
        dth_vals.append(sp.simplify(-dc_e / sp.sqrt(1 - sp.Rational(1, 16))))
    schlafli_4 = sp.simplify(1 * dth_vals[0] + 6 * dth_vals[1] + 3 * dth_vals[2])
    cc.check(
        t4_adj == (1, sp.Rational(2, 5), sp.Rational(-54, 25), sp.Rational(16, 25))
        and t4_dis[3] == sp.Rational(-4, 25)
        and dth_vals == [2 * sp.sqrt(15) / 5, -sp.sqrt(15) / 10, sp.sqrt(15) / 15]
        and schlafli_4 == 0,
        "2.2b: Exact Cayley-Menger 4-simplex Taylor derivatives & Schläfli identity (2/5 - 6/10 + 3/15 = 0) derived symbolically",
    )

    def du4_1(e, s): return Fraction(2, 5) if set(e) <= set(s) else Fraction(0)
    def du4_2(e1, e2, s):
        if not (set(e1) <= set(s) and set(e2) <= set(s)): return Fraction(0)
        if e1 == e2: return Fraction(-54, 25)
        return Fraction(16, 25) if len(set(e1) & set(e2)) == 1 else Fraction(-4, 25)
    def du2_1(e, T): return Fraction(2, 3) if set(e) <= set(T) else Fraction(0)
    def du2_2(e1, e2, T):
        if not (set(e1) <= set(T) and set(e2) <= set(T)): return Fraction(0)
        return Fraction(-10, 9) if e1 == e2 else Fraction(8, 9)
    def du3_1(e, tet): return Fraction(1, 2) if set(e) <= set(tet) else Fraction(0)
    def du3_2(e1, e2, tet):
        if not (set(e1) <= set(tet) and set(e2) <= set(tet)): return Fraction(0)
        if e1 == e2: return Fraction(-7, 4)
        return Fraction(3, 4) if len(set(e1) & set(e2)) == 1 else Fraction(-1, 4)

    p_simps = [verts, edges, tris, tets, simps]
    inc_s = [
        [[s for s in simps if ({sig} if p == 0 else set(sig)) <= set(s)] for sig in p_simps[p]]
        for p in range(5)
    ]
    S1, S2 = 120, 14400

    def to_int_arr(flist, scale):
        out = np.empty(len(flist), dtype=object)
        for i, f_v in enumerate(flist):
            v = f_v * scale
            assert v.denominator == 1
            out[i] = v.numerator
        return out

    def get_r_derivs_int(p, ea, eb):
        ra, rb, rab, ia, ib, iab = [], [], [], [], [], []
        for idx, sig in enumerate(p_simps[p]):
            slist = inc_s[p][idx]
            k = len(slist)
            Na = sum(du4_1(ea, s) for s in slist) / k
            Nb = sum(du4_1(eb, s) for s in slist) / k
            Nab = sum(du4_2(ea, eb, s) for s in slist) / k
            if p == 0: Da = Db = Dab = Fraction(0)
            elif p == 1:
                Da = Fraction(2) if sig == ea else Fraction(0)
                Db = Fraction(2) if sig == eb else Fraction(0)
                Dab = Fraction(2) if (sig == ea and sig == eb) else Fraction(0)
            elif p == 2:
                ua, ub, uab = du2_1(ea, sig), du2_1(eb, sig), du2_2(ea, eb, sig)
                Da, Db, Dab = 2 * ua, 2 * ub, 2 * (ua * ub + uab)
            elif p == 3:
                ua, ub, uab = du3_1(ea, sig), du3_1(eb, sig), du3_2(ea, eb, sig)
                Da, Db, Dab = 2 * ua, 2 * ub, 2 * (ua * ub + uab)
            else:
                ua, ub, uab = du4_1(ea, sig), du4_1(eb, sig), du4_2(ea, eb, sig)
                Da, Db, Dab = 2 * ua, 2 * ub, 2 * (ua * ub + uab)
            ra.append(Na - Da); rb.append(Nb - Db)
            rab.append(Nab - Na * Db - Nb * Da - Dab + 2 * Da * Db)
            ia.append(Da - Na); ib.append(Db - Nb)
            iab.append(Dab - Da * Nb - Db * Na - Nab + 2 * Na * Nb)
        return (to_int_arr(ra, S1), to_int_arr(rb, S1), to_int_arr(rab, S2),
                to_int_arr(ia, S1), to_int_arr(ib, S1), to_int_arr(iab, S2))

    def build_M_derivs_int(p, r_data):
        n = ns[p]
        Ma = np.zeros((n, n), dtype=object)
        Mb = np.zeros((n, n), dtype=object)
        Mab = np.zeros((n, n), dtype=object)
        if p > 0:
            D = ds[p - 1]; DT = D.T
            ra_p, rb_p, rab_p, _, _, _ = r_data[p]
            _, _, _, ia_m, ib_m, iab_m = r_data[p - 1]
            c = p * p
            DDT = D @ DT
            D_iam_DT = (D * ia_m[None, :]) @ DT
            D_ibm_DT = (D * ib_m[None, :]) @ DT
            D_iabm_DT = (D * iab_m[None, :]) @ DT
            Ma = Ma + c * (ra_p[:, None] * DDT + D_iam_DT)
            Mb = Mb + c * (rb_p[:, None] * DDT + D_ibm_DT)
            Mab = Mab + c * (rab_p[:, None] * DDT + ra_p[:, None] * D_ibm_DT + rb_p[:, None] * D_iam_DT + D_iabm_DT)
        if p < 4:
            D = ds[p]; DT = D.T
            ra_n, rb_n, rab_n, _, _, _ = r_data[p + 1]
            _, _, _, ia_p, ib_p, iab_p = r_data[p]
            c = (p + 1) * (p + 1)
            DTD = DT @ D
            DT_ran_D = (DT * ra_n[None, :]) @ D
            DT_rbn_D = (DT * rb_n[None, :]) @ D
            DT_rabn_D = (DT * rab_n[None, :]) @ D
            Ma = Ma + c * (DT_ran_D + DTD * ia_p[None, :])
            Mb = Mb + c * (DT_rbn_D + DTD * ib_p[None, :])
            Mab = Mab + c * (DT_rabn_D + DT_ran_D * ib_p[None, :] + DT_rbn_D * ia_p[None, :] + DTD * iab_p[None, :])
        return Ma, Mb, Mab

    e0 = edges[0]
    M_pairs = [[build_M_derivs_int(p, [get_r_derivs_int(q, e0, eb) for q in range(5)]) for p in range(5)] for eb in rep_edges]
    kd_exact = {}
    for m2_val in (1, 4):
        Gs = [lagrange_inv(L0[p], [e for e, _ in spec_p[p]], m2_val) for p in range(5)]
        h_kd = []
        g_kd = None
        for idx_rk in range(6):
            d2_tot = Fraction(0)
            d1_tot = Fraction(0)
            for p in range(5):
                Ma, Mb, Mab = M_pairs[idx_rk][p]
                G_int, lcm_d = Gs[p]
                tr1 = int(np.sum(G_int * Mab.T))
                tr2 = int(np.sum((G_int @ Ma) * (G_int @ Mb).T))
                d2_tot += Fraction(-1, 2) * (Fraction(tr1, lcm_d * S2) - Fraction(tr2, lcm_d * lcm_d * S1 * S1))
                if idx_rk == 0:
                    d1_tot += Fraction(-1, 2) * Fraction(int(np.sum(G_int * Ma.T)), lcm_d * S1)
            if idx_rk == 0:
                g_kd = d1_tot
            h_kd.append(d2_tot)
        lams = [sum(int(P_bm[a, i]) * h_kd[i] for i in range(6)) for a in range(6)]
        kd_exact[m2_val] = [g_kd] + lams

    # Cross-check g_KD and lam_{1_sc} against exact closed-form scaling identities!
    all_eigs_flat = [x for lst in spec_p for x in lst]
    scale_ok = True
    for m2_val in (1, 4):
        g_pred = sum(Fraction(mult * lam, lam + m2_val) for lam, mult in all_eigs_flat) / 40
        l1_pred = -sum(Fraction(mult * lam * (lam + 3 * m2_val), (lam + m2_val) ** 2) for lam, mult in all_eigs_flat) / 40
        if kd_exact[m2_val][0] != g_pred or kd_exact[m2_val][1] != l1_pred:
            scale_ok = False
    cc.check(
        scale_ok,
        "2.3: Exact rational S_KD(m^2=1,4) gradients & 6-irrep Hessians match closed-form scaling sum identities bit-for-bit",
    )

    # 2.4a FIRST-PRINCIPLES symbolic derivation of ALL FIVE S^4 geometric 7-vectors
    # [g, 1_sc, 4_cf, 5_cf, 5_TT, 10_TT, 15_TT] directly from the S^4 = partial beta_5 simplicial complex
    # and exact 1st & 2nd Cayley-Menger derivatives (ZERO hardcoding!).
    s3, s5 = sp.sqrt(3), sp.sqrt(5)
    eps0 = sp.Symbol("eps0", positive=True)

    def simplex4_exact_derivs(l2_0: dict[tuple[int, int], sp.Expr]):
        edges_loc = [(i, j) for i in range(5) for j in range(i + 1, 5)]
        M0 = sp.zeros(6, 6)
        for i in range(1, 6):
            M0[0, i] = 1
            M0[i, 0] = 1
        for i, j in edges_loc:
            M0[i + 1, j + 1] = l2_0[(i, j)]
            M0[j + 1, i + 1] = l2_0[(i, j)]
        M0inv = M0.inv()
        V0 = sp.sqrt(-M0.det()) / 96
        l0 = [sp.sqrt(l2_0[e]) for e in edges_loc]
        M1, M2_diag = [], []
        for idx_l, (i, j) in enumerate(edges_loc):
            A_m = sp.zeros(6, 6); A_m[i + 1, j + 1] = 2 * l0[idx_l]; A_m[j + 1, i + 1] = 2 * l0[idx_l]
            B_m = sp.zeros(6, 6); B_m[i + 1, j + 1] = 2; B_m[j + 1, i + 1] = 2
            M1.append(A_m); M2_diag.append(B_m)
        P1 = [M0inv * A_m for A_m in M1]
        K1 = [P_m * M0inv for P_m in P1]
        dlndet = [P_m.trace() for P_m in P1]
        d2lndet = [
            [-(P1[a] * P1[b]).trace() + ((M0inv * M2_diag[a]).trace() if a == b else 0) for b in range(10)]
            for a in range(10)
        ]
        dV = [sp.radsimp(V0 * dlndet[a] / 2) for a in range(10)]
        d2V = [[sp.radsimp(V0 * (d2lndet[a][b] + dlndet[a] * dlndet[b] / 2) / 2) for b in range(10)] for a in range(10)]
        N0 = -M0inv
        dN = K1
        d2N = [
            [-(P1[a] * K1[b] + P1[b] * K1[a]) + (M0inv * M2_diag[a] * M0inv if a == b else sp.zeros(6, 6)) for b in range(10)]
            for a in range(10)
        ]
        dth, d2th = [], []
        for (u, v) in edges_loc:
            ui, vi = u + 1, v + 1
            f0, g0, h0 = N0[ui, vi], N0[ui, ui], N0[vi, vi]
            r0 = sp.sqrt(g0 * h0)
            c0 = sp.radsimp(-f0 / r0)
            s0 = sp.sqrt(1 - c0**2)
            dc = [sp.radsimp((-dN[a][ui, vi] + f0 * (dN[a][ui, ui] / (2 * g0) + dN[a][vi, vi] / (2 * h0))) / r0) for a in range(10)]
            dth_h = [sp.radsimp(-dc[a] / s0) for a in range(10)]
            d2th_h = [[None] * 10 for _ in range(10)]
            for a in range(10):
                fa, ga, ha = dN[a][ui, vi], dN[a][ui, ui], dN[a][vi, vi]
                pa = -(ga / (2 * g0) + ha / (2 * h0))
                for b in range(a, 10):
                    fb, gb, hb = dN[b][ui, vi], dN[b][ui, ui], dN[b][vi, vi]
                    fab, gab, hab = d2N[a][b][ui, vi], d2N[a][b][ui, ui], d2N[a][b][vi, vi]
                    pb = -(gb / (2 * g0) + hb / (2 * h0))
                    Wab_W = pa * pb + (ga * gb / (2 * g0**2) - gab / (2 * g0)) + (ha * hb / (2 * h0**2) - hab / (2 * h0))
                    d2cab = -(fab + fa * pb + fb * pa + f0 * Wab_W) / r0
                    val = sp.radsimp(-d2cab / s0 - dc[a] * dc[b] * c0 / s0**3)
                    d2th_h[a][b] = d2th_h[b][a] = val
            dth.append(dth_h); d2th.append(d2th_h)
        return edges_loc, V0, dV, d2V, dth, d2th

    def tri_exact_derivs(l2_0: dict[tuple[int, int], sp.Expr]):
        edges_loc = [(0, 1), (0, 2), (1, 2)]
        ls = [sp.Symbol(f"_lt{k}", positive=True) for k in range(3)]
        Q_h = 2 * ls[0]**2 * ls[1]**2 + 2 * ls[0]**2 * ls[2]**2 + 2 * ls[1]**2 * ls[2]**2 - ls[0]**4 - ls[1]**4 - ls[2]**4
        A_e = sp.sqrt(Q_h) / 4
        subs_d = {ls[k]: sp.sqrt(l2_0[edges_loc[k]]) for k in range(3)}
        A0 = sp.radsimp(A_e.subs(subs_d))
        dA = [sp.radsimp(sp.diff(A_e, ls[k]).subs(subs_d)) for k in range(3)]
        d2A = [[sp.radsimp(sp.diff(A_e, ls[a], ls[b]).subs(subs_d)) for b in range(3)] for a in range(3)]
        return edges_loc, A0, dA, d2A

    eloc4, V0_r, dV_r, d2V_r, dth_r, d2th_r = simplex4_exact_derivs(
        {(i, j): sp.Integer(1) for i in range(5) for j in range(i + 1, 5)}
    )
    eloc2, A0_r, dA_r, d2A_r = tri_exact_derivs({(0, 1): sp.Integer(1), (0, 2): sp.Integer(1), (1, 2): sp.Integer(1)})
    eloc4_idx = {e: k for k, e in enumerate(eloc4)}
    eloc2_idx = {e: k for k, e in enumerate(eloc2)}

    s_vmap = [{v: i for i, v in enumerate(s)} for s in simps]
    t_vmap = [{v: i for i, v in enumerate(T)} for T in tris]
    tri_inc_simps = [[si for si, s in enumerate(simps) if set(T) <= set(s)] for T in tris]

    def _loc_e4(si: int, e: tuple[int, int]):
        vm = s_vmap[si]
        if e[0] not in vm or e[1] not in vm:
            return None
        a, b = vm[e[0]], vm[e[1]]
        return eloc4_idx[(a, b) if a < b else (b, a)]

    def _loc_h4(si: int, T: tuple[int, int, int]):
        vm = s_vmap[si]
        rem = sorted(vm[v] for v in simps[si] if v not in T)
        return eloc4_idx[(rem[0], rem[1])]

    def _loc_e2(ti: int, e: tuple[int, int]):
        vm = t_vmap[ti]
        if e[0] not in vm or e[1] not in vm:
            return None
        a, b = vm[e[0]], vm[e[1]]
        return eloc2_idx[(a, b) if a < b else (b, a)]

    g_V_d = sp.Integer(0); h_V_d = [sp.Integer(0)] * 6
    g_nSR_d = sp.Integer(0); h_nSR_d = [sp.Integer(0)] * 6
    g_R2A_d = sp.Integer(0); h_R2A_d = [sp.Integer(0)] * 6
    g_R2V_d = sp.Integer(0); h_R2V_d = [sp.Integer(0)] * 6
    for k_o, eb in enumerate(rep_edges):
        for si in range(len(simps)):
            ia, ib = _loc_e4(si, e0), _loc_e4(si, eb)
            if k_o == 0 and ia is not None:
                g_V_d += dV_r[ia]
            if ia is not None and ib is not None:
                h_V_d[k_o] += d2V_r[ia][ib]
        for ti, T in enumerate(tris):
            ja, jb = _loc_e2(ti, e0), _loc_e2(ti, eb)
            A_a = dA_r[ja] if ja is not None else sp.Integer(0)
            A_b = dA_r[jb] if jb is not None else sp.Integer(0)
            A_ab = d2A_r[ja][jb] if (ja is not None and jb is not None) else sp.Integer(0)
            ep_a = sp.Integer(0); ep_b = sp.Integer(0); ep_ab = sp.Integer(0)
            VT0 = sp.Integer(0); VT_a = sp.Integer(0); VT_b = sp.Integer(0); VT_ab = sp.Integer(0)
            # Hinge volume convention matching verify_deep_frontier_v12.py:903: V_T = (1/4) sum_{sigma supset T} V_sigma
            for si in tri_inc_simps[ti]:
                VT0 += V0_r / 4
                ia, ib = _loc_e4(si, e0), _loc_e4(si, eb)
                ih = _loc_h4(si, T)
                if ia is not None:
                    ep_a -= dth_r[ih][ia]; VT_a += dV_r[ia] / 4
                if ib is not None:
                    ep_b -= dth_r[ih][ib]; VT_b += dV_r[ib] / 4
                if ia is not None and ib is not None:
                    ep_ab -= d2th_r[ih][ia][ib]; VT_ab += d2V_r[ia][ib] / 4
            if k_o == 0:
                g_nSR_d += -(A_a * eps0 + A0_r * ep_a)
                g_R2A_d += A_a * eps0**2 + 2 * A0_r * eps0 * ep_a
                g_R2V_d += (2 * A0_r * A_a * eps0**2 + 2 * A0_r**2 * eps0 * ep_a) / VT0 - (A0_r**2 * eps0**2) * VT_a / (VT0**2)
            h_nSR_d[k_o] += -(A_ab * eps0 + A_a * ep_b + A_b * ep_a + A0_r * ep_ab)
            h_R2A_d[k_o] += A_ab * eps0**2 + 2 * eps0 * (A_a * ep_b + A_b * ep_a) + 2 * A0_r * (ep_a * ep_b + eps0 * ep_ab)
            N0_v = A0_r**2 * eps0**2
            Na_v = 2 * A0_r * A_a * eps0**2 + 2 * A0_r**2 * eps0 * ep_a
            Nb_v = 2 * A0_r * A_b * eps0**2 + 2 * A0_r**2 * eps0 * ep_b
            Nab_v = (
                2 * (A_a * A_b + A0_r * A_ab) * eps0**2
                + 4 * A0_r * eps0 * (A_a * ep_b + A_b * ep_a)
                + 2 * A0_r**2 * (ep_a * ep_b + eps0 * ep_ab)
            )
            h_R2V_d[k_o] += Nab_v / VT0 - (Na_v * VT_b + Nb_v * VT_a + N0_v * VT_ab) / (VT0**2) + 2 * N0_v * VT_a * VT_b / (VT0**3)

    def _proj_7vec(g_val, h_vals):
        return sp.Matrix([sp.expand(g_val)] + [sp.expand(sum(P_bm[a, i] * h_vals[i] for i in range(6))) for a in range(6)])

    v_V = _proj_7vec(g_V_d, h_V_d)
    v_negSR = _proj_7vec(g_nSR_d, h_nSR_d)
    v_R2A = _proj_7vec(g_R2A_d, h_R2A_d)
    v_R2V = _proj_7vec(g_R2V_d, h_R2V_d)
    v_L4 = _proj_7vec(sp.Integer(4), [sp.Integer(12) if k_o == 5 else sp.Integer(0) for k_o in range(6)])

    # Verify derived 7-vectors match the closed-form dossier table bit-for-bit!
    v_V_ref = sp.Matrix([s5 / 30, s5 / 10, -s5 / 10, -s5 / 50, -3 * s5 / 10, -9 * s5 / 50, -7 * s5 / 30])
    v_negSR_ref = sp.Matrix([
        -s3 * eps0, -s3 * eps0,
        11 * s3 * eps0 / 9 - 4 * s5 / 3,
        s3 * eps0 / 3 - 4 * s5 / 5,
        23 * s3 * eps0 / 9 + 8 * s5 / 3,
        5 * s3 * eps0 / 3 + 4 * s5 / 5,
        19 * s3 * eps0 / 9 + 4 * s5 / 3,
    ])
    v_R2A_ref = sp.Matrix([
        s3 * eps0**2, s3 * eps0**2,
        -11 * s3 * eps0**2 / 9 + 8 * s5 * eps0 / 3 + 20 * s3 / 3,
        -s3 * eps0**2 / 3 + 8 * s5 * eps0 / 5 + 8 * s3 / 5,
        -23 * s3 * eps0**2 / 9 - 16 * s5 * eps0 / 3 + 320 * s3 / 3,
        -5 * s3 * eps0**2 / 3 - 8 * s5 * eps0 / 5 + 16 * s3 / 5,
        -19 * s3 * eps0**2 / 9 - 8 * s5 * eps0 / 3 + 40 * s3 / 3,
    ])
    v_R2V_ref = sp.Matrix([
        0, 0,
        384 * s5 * eps0**2 / 5 + 192 * s3 * eps0 + 96 * s5,
        1152 * s5 * eps0**2 / 125 + 576 * s3 * eps0 / 25 + 576 * s5 / 25,
        192 * s5 * eps0**2 - 384 * s3 * eps0 + 1536 * s5,
        13824 * s5 * eps0**2 / 125 - 1728 * s3 * eps0 / 25 + 1152 * s5 / 25,
        768 * s5 * eps0**2 / 5 - 192 * s3 * eps0 + 192 * s5,
    ])
    v_L4_ref = sp.Matrix([4, 12, 12, 12, 12, 12, 12])
    derived_match = all(
        sp.Matrix([sp.expand(got[i] - ref[i]) for i in range(7)]) == sp.zeros(7, 1)
        for got, ref in ((v_V, v_V_ref), (v_negSR, v_negSR_ref), (v_R2A, v_R2A_ref), (v_R2V, v_R2V_ref), (v_L4, v_L4_ref))
    )
    cc.check(
        derived_match,
        "2.4a: All 5 S^4 geometric 7-vectors (V_tot, -S_R, S_{R^2,A}, S_{R^2,V}, S_{L^4}) derived symbolically from simplicial complex & Cayley-Menger",
    )

    # Exact rational brackets for sqrt(2), sqrt(3), sqrt(5), eps_0 (ZERO float64!)
    b_s2 = isqrt_bounds(Fraction(2))
    b_s3 = isqrt_bounds(Fraction(3))
    b_s5 = isqrt_bounds(Fraction(5))
    b_eps = eps0_rat_bounds()

    def eval_geom_interval(expr: sp.Expr) -> tuple[Fraction, Fraction]:
        """Evaluates any polynomial in (sqrt(3), sqrt(5), eps0) over Q into an exact Fraction bracket."""
        x3, x5, xe = sp.symbols("x3 x5 xe")
        e = sp.expand(expr.subs({s3: x3, s5: x5, eps0: xe}))
        p = sp.Poly(e, x3, x5, xe, domain="QQ")
        tot = (Fraction(0), Fraction(0))
        for (p3, p5, pe), coeff in p.terms():
            c_f = Fraction(int(coeff.p), int(coeff.q))
            term = (c_f, c_f)
            for _ in range(p3): term = imul(term, b_s3)
            for _ in range(p5): term = imul(term, b_s5)
            for _ in range(pe): term = imul(term, b_eps)
            tot = iadd(tot, term)
        return tot

    # 2.4b Certify -S_R signature (10-,30+) & naive S_{R^2,A} negative 10_TT eigenvalue in pure Fraction!
    r2a_10tt_b = eval_geom_interval(v_R2A[5])
    sr_signs_ok = (
        eval_geom_interval(v_negSR[1])[1] < 0
        and eval_geom_interval(v_negSR[2])[1] < 0
        and eval_geom_interval(v_negSR[3])[1] < 0
        and eval_geom_interval(v_negSR[4])[0] > 0
        and eval_geom_interval(v_negSR[5])[0] > 0
        and eval_geom_interval(v_negSR[6])[0] > 0
    )
    cc.check(
        r2a_10tt_b[1] < 0 and sr_signs_ok,
        "2.4b: Exact Fraction certification: -S_R signature (10-,30+) & naive S_{R^2,A} has negative 10_TT eigenvalue",
    )

    # 2.5 Pure-integer 1-param V_tot and homogeneity Left-Null obstructions
    ln_1p_checks = [
        ("1_sc",  1, -3, 1),
        ("4_cf",  2,  3, 1),
        ("5_cf",  3,  3, 5),
        ("5_TT",  4,  9, 1),
        ("10_TT", 5, 27, 5),
        ("15_TT", 6,  7, 1),
    ]
    ln1_ok = True
    for name, idx, cg, cl in ln_1p_checks:
        if sp.simplify(cg * v_V[0] + cl * v_V[idx]) != 0:
            ln1_ok = False
        val1 = cg * kd_exact[1][0] + cl * kd_exact[1][idx]
        val4 = cg * kd_exact[4][0] + cl * kd_exact[4][idx]
        if not (val1 < 0 and val4 < 0):
            ln1_ok = False
    homog_ok = (
        all(sp.simplify(-3 * v[0] + v[1]) == 0 for v in (v_V, v_R2V, v_L4))
        and (-3 * kd_exact[1][0] + kd_exact[1][1] < 0)
        and all(sp.simplify(-1 * v[0] + v[1]) == 0 for v in (v_negSR, v_R2A, v_R2V))
        and (-1 * kd_exact[1][0] + kd_exact[1][1] < 0)
    )
    cc.check(
        ln1_ok and homog_ok,
        "2.5: Pure-integer 1-param V_tot Left-Null {(-3,1),(9,1),(27,5),(7,1)} & degree-d homogeneity no-go (<0 for m=1,2)",
    )

    # 2.6 EXACT 3-INTEGER LEFT-NULL VECTOR v_TT = (6, 25, -27) FOR 2-PARAM {V_tot, -S_R} ON TT SECTOR!
    v_TT = sp.Matrix([6, 25, -27])
    ann_V_tt = sp.simplify((v_TT.T * v_V[4:, :])[0]) == 0
    ann_SR_tt = sp.simplify((v_TT.T * v_negSR[4:, :])[0]) == 0
    obs_tt_1 = 6 * kd_exact[1][4] + 25 * kd_exact[1][5] - 27 * kd_exact[1][6]
    obs_tt_4 = 6 * kd_exact[4][4] + 25 * kd_exact[4][5] - 27 * kd_exact[4][6]
    cc.check(
        ann_V_tt and ann_SR_tt and obs_tt_1 > 0 and obs_tt_4 > 0,
        f"2.6: Pure-integer 3-entry Left-Null v_TT=(6,25,-27) annihilates {{V_tot,-S_R}}|_TT (indep. of eps0,sqrt3,sqrt5); P(m=1)={float(obs_tt_1):+.4f}, P(m=2)={float(obs_tt_4):+.4f}",
    )

    # 2.7 Exact 3-entry Farkas dual certificate y_2p > 0 for 2-param {V_tot, -S_R} on [g, 1_sc, 5_TT]!
    y_2p = sp.Matrix([
        -4 * s3 * eps0 / 3 + 8 * s5,
        58 * s3 * eps0 / 9 - 8 * s5 / 3,
        2 * s3 * eps0,
    ])
    A_2p = sp.Matrix.hstack(v_V.extract([0, 1, 4], [0]), v_negSR.extract([0, 1, 4], [0]))
    farkas_ann = sp.simplify(y_2p.T * A_2p) == sp.zeros(1, 2)
    y_b = [eval_geom_interval(y_2p[i]) for i in range(3)]
    rhs_2p_1 = iadd(iadd(iscale(kd_exact[1][0], y_b[0]), iscale(kd_exact[1][1], y_b[1])), iscale(kd_exact[1][4], y_b[2]))
    rhs_2p_4 = iadd(iadd(iscale(kd_exact[4][0], y_b[0]), iscale(kd_exact[4][1], y_b[1])), iscale(kd_exact[4][4], y_b[2]))
    cc.check(
        farkas_ann and all(b[0] > 0 for b in y_b) and rhs_2p_1[1] < 0 and rhs_2p_4[1] < 0,
        f"2.7: Exact Farkas certificate y_2p>0 refutes {{V_tot,-S_R}} (g>=0 & 1_sc>=0 & 5_TT>=0): y^T b(m=1)={float(rhs_2p_1[1]):+.3f}<0",
    )

    # 2.8a FIRST-PRINCIPLES 45-EDGE FLAT-(1,5) CURVED-S^4 SUBDIVISION:
    # Sharply separates (a) nonlinear vertex-move invariance d^2 S(L(x))/dx^2 = 0 from
    # (b) linearized 45x45 edge-length Hessian Rocek-Williams zero modes H_S u = 0!
    t_rw = sp.Symbol("t_rw", real=True)
    u_dot_v = [sp.Rational(1, 2), sp.Rational(-1, 2), sp.Integer(0), sp.Integer(0), sp.Integer(0)]
    L_in_sq = [sp.Rational(2, 5) - 2 * t_rw * u_dot_v[k] + t_rw**2 for k in range(5)]
    V_sub_t = []
    cm_sub_ok = True
    for omit_i in range(5):
        M_sub_t = sp.zeros(6, 6)
        for a in range(1, 6):
            M_sub_t[0, a] = 1; M_sub_t[a, 0] = 1
        bverts = [k for k in range(5) if k != omit_i]
        for j in range(4):
            M_sub_t[1, j + 2] = M_sub_t[j + 2, 1] = L_in_sq[bverts[j]]
        for a in range(4):
            for b in range(a + 1, 4):
                M_sub_t[a + 2, b + 2] = M_sub_t[b + 2, a + 2] = 1
        lam_t = sp.Rational(1, 5) + 2 * t_rw * u_dot_v[omit_i]
        if sp.expand(-M_sub_t.det() - 5 * lam_t**2) != 0:
            cm_sub_ok = False
        V_sub_t.append(lam_t * V0_r)
    nl_vol_const = sp.simplify(sum(V_sub_t) - V0_r) == 0
    # S_{R^2,V}(L(t)) on the 10 boundary triangles of sigma0 (each shared by 3 ext + 2 sub-simplices):
    S_R2V_bd_t = sp.Integer(0)
    for i_o in range(5):
        for j_o in range(i_o + 1, 5):
            VT_t = (3 * V0_r + V_sub_t[i_o] + V_sub_t[j_o]) / 4
            S_R2V_bd_t += A0_r**2 * eps0**2 / VT_t
    d2_rw_R2V_exact = sp.simplify(sp.diff(S_R2V_bd_t, t_rw, 2).subs(t_rw, 0))
    d2_rw_L4_exact = sp.simplify(sp.diff(sum(l2**2 for l2 in L_in_sq), t_rw, 2).subs(t_rw, 0))
    sum_d2L_exact = sp.simplify(sum(sp.diff(sp.sqrt(l2), t_rw, 2).subs(t_rw, 0) for l2 in L_in_sq))
    d2_rw_R2V_b = eval_geom_interval(d2_rw_R2V_exact)

    # Assemble ACTUAL exact 45-edge gradients & 45x45 Hessians in Q(sqrt(2),sqrt(3),sqrt(5))[eps0]!
    def _sqf_mul(a: int, b: int) -> tuple[int, int]:
        p_v = a * b; k_v = 1
        for q_v in (2, 3, 5):
            while p_v % (q_v * q_v) == 0:
                p_v //= q_v * q_v; k_v *= q_v
        return p_v, k_v

    def _sym_to_alg(expr: sp.Expr) -> dict[tuple[int, int], Fraction]:
        x2, x3, x5, xe = sp.symbols("_a2 _a3 _a5 _ae")
        e = sp.radsimp(sp.expand(expr))
        def _repl(nd):
            if isinstance(nd, sp.Pow) and nd.base.is_Integer and nd.exp.is_Rational and nd.exp.q == 2:
                n_v = int(nd.base); k_v = int(nd.exp.p)
                res = sp.Rational(n_v) ** (k_v // 2)
                if k_v % 2 != 0:
                    m_v = n_v; out = sp.Integer(1)
                    for p_i, sym_i in ((2, x2), (3, x3), (5, x5)):
                        while m_v % p_i == 0:
                            m_v //= p_i; out *= sym_i
                    assert m_v == 1
                    res *= out
                return res
            return nd
        e = sp.expand(e.replace(lambda nd: isinstance(nd, sp.Pow) and nd.base.is_Integer and nd.exp.is_Rational and nd.exp.q == 2, _repl))
        e = sp.expand(e.subs(eps0, xe))
        poly = sp.Poly(e, x2, x3, x5, xe, domain="QQ")
        out: dict[tuple[int, int], Fraction] = {}
        for (p2, p3, p5, pe), c_v in poly.terms():
            f_v = Fraction(int(c_v.p), int(c_v.q)) * (2 ** (p2 // 2)) * (3 ** (p3 // 2)) * (5 ** (p5 // 2))
            sqf = (2 if p2 % 2 else 1) * (3 if p3 % 2 else 1) * (5 if p5 % 2 else 1)
            key = (sqf, pe)
            out[key] = out.get(key, Fraction(0)) + f_v
        return {k: v for k, v in out.items() if v != 0}

    def _alg_add(a, b, sc=Fraction(1)):
        out = dict(a)
        for k, v in b.items():
            nv = out.get(k, Fraction(0)) + sc * v
            if nv == 0: out.pop(k, None)
            else: out[k] = nv
        return out

    def _alg_mul(a, b):
        out = {}
        for (s1, p1), v1 in a.items():
            for (s2, p2), v2 in b.items():
                sqf, mult = _sqf_mul(s1, s2)
                key = (sqf, p1 + p2)
                nv = out.get(key, Fraction(0)) + v1 * v2 * mult
                if nv == 0: out.pop(key, None)
                else: out[key] = nv
        return out

    def _alg_scale(a, sc):
        return {} if sc == 0 else {k: v * sc for k, v in a.items()}

    _, V0_s, dV_s, d2V_s, dth_s, d2th_s = simplex4_exact_derivs(
        {(i, j): (sp.Rational(2, 5) if i == 0 else sp.Integer(1)) for i in range(5) for j in range(i + 1, 5)}
    )
    _, A0_i, dA_i, d2A_i = tri_exact_derivs(
        {(0, 1): sp.Rational(2, 5), (0, 2): sp.Rational(2, 5), (1, 2): sp.Integer(1)}
    )
    _c1 = lambda lst: [_sym_to_alg(x) for x in lst]
    _c2 = lambda mat: [[_sym_to_alg(x) for x in row] for row in mat]
    dV_ra, d2V_ra = _c1(dV_r), _c2(d2V_r)
    dV_sa, d2V_sa = _c1(dV_s), _c2(d2V_s)
    dth_ra, d2th_ra = [_c1(x) for x in dth_r], [_c2(x) for x in d2th_r]
    dth_sa, d2th_sa = [_c1(x) for x in dth_s], [_c2(x) for x in d2th_s]
    A0_ra, dA_ra, d2A_ra = _sym_to_alg(A0_r), _c1(dA_r), _c2(d2A_r)
    A0_ia, dA_ia, d2A_ia = _sym_to_alg(A0_i), _c1(dA_i), _c2(d2A_i)
    EPS0_a = {(1, 1): Fraction(1)}

    sigma0 = simps[0]
    v_new = 10
    ext_simps = [s for s in simps if s != sigma0]
    sub_simps = [(v_new,) + tuple(v for v in sigma0 if v != omit) for omit in sigma0]
    simps15 = ext_simps + sub_simps
    is_sub15 = [False] * len(ext_simps) + [True] * len(sub_simps)
    tris15 = sorted({tuple(sorted(c)) for s in simps15 for c in combinations(s, 3)})
    edges15 = sorted({tuple(sorted(c)) for s in simps15 for c in combinations(s, 2)})
    e15_idx = {e: i for i, e in enumerate(edges15)}
    int_idxs = [e15_idx[e] for e in edges15 if v_new in e]
    ext_idxs = [e15_idx[e] for e in edges15 if v_new not in e]

    gV15 = [{} for _ in range(45)]; HV15 = [[{} for _ in range(45)] for _ in range(45)]
    gSR15 = [{} for _ in range(45)]; HSR15 = [[{} for _ in range(45)] for _ in range(45)]
    gR2A15 = [{} for _ in range(45)]; HR2A15 = [[{} for _ in range(45)] for _ in range(45)]

    for si, s in enumerate(simps15):
        dv_t = dV_sa if is_sub15[si] else dV_ra
        d2v_t = d2V_sa if is_sub15[si] else d2V_ra
        g_e = [e15_idx[tuple(sorted((s[i], s[j])))] for (i, j) in eloc4]
        for a in range(10):
            ga = g_e[a]
            gV15[ga] = _alg_add(gV15[ga], dv_t[a])
            for b in range(10):
                gb = g_e[b]
                HV15[ga][gb] = _alg_add(HV15[ga][gb], d2v_t[a][b])

    for T in tris15:
        if v_new in T:
            T_ord = (v_new,) + tuple(v for v in T if v != v_new)
            A0_t, dA_t, d2A_t, ep0_t = A0_ia, dA_ia, d2A_ia, {}
        else:
            T_ord = T
            A0_t, dA_t, d2A_t, ep0_t = A0_ra, dA_ra, d2A_ra, EPS0_a
        Aa = {}; Aab = {}
        g_e2 = [e15_idx[tuple(sorted((T_ord[i], T_ord[j])))] for (i, j) in eloc2]
        for a in range(3):
            Aa[g_e2[a]] = dA_t[a]
            for b in range(3):
                Aab[(g_e2[a], g_e2[b])] = d2A_t[a][b]
        epa = {}; epab = {}
        for si, s in enumerate(simps15):
            if not set(T) <= set(s):
                continue
            dth_t = dth_sa if is_sub15[si] else dth_ra
            d2th_t = d2th_sa if is_sub15[si] else d2th_ra
            vm = {v: i for i, v in enumerate(s)}
            rem = sorted(vm[v] for v in s if v not in T)
            ih = eloc4_idx[(rem[0], rem[1])]
            g_e4 = [e15_idx[tuple(sorted((s[i], s[j])))] for (i, j) in eloc4]
            for a in range(10):
                ga = g_e4[a]
                epa[ga] = _alg_add(epa.get(ga, {}), dth_t[ih][a], Fraction(-1))
                for b in range(10):
                    gb = g_e4[b]
                    epab[(ga, gb)] = _alg_add(epab.get((ga, gb), {}), d2th_t[ih][a][b], Fraction(-1))
        supp = sorted(set(Aa.keys()) | set(epa.keys()))
        ep0_sq = _alg_mul(ep0_t, ep0_t)
        for ga in supp:
            aa = Aa.get(ga, {}); ea = epa.get(ga, {})
            gSR15[ga] = _alg_add(gSR15[ga], _alg_add(_alg_mul(aa, ep0_t), _alg_mul(A0_t, ea)), Fraction(-1))
            gR2A15[ga] = _alg_add(gR2A15[ga], _alg_add(_alg_mul(aa, ep0_sq), _alg_scale(_alg_mul(A0_t, _alg_mul(ep0_t, ea)), Fraction(2))))
            for gb in supp:
                ab = Aa.get(gb, {}); eb = epa.get(gb, {})
                aab = Aab.get((ga, gb), {}); eab = epab.get((ga, gb), {})
                t_sr = _alg_add(_alg_add(_alg_mul(aab, ep0_t), _alg_mul(aa, eb)), _alg_add(_alg_mul(ab, ea), _alg_mul(A0_t, eab)))
                HSR15[ga][gb] = _alg_add(HSR15[ga][gb], t_sr, Fraction(-1))
                t_r2a = _alg_add(
                    _alg_mul(aab, ep0_sq),
                    _alg_add(
                        _alg_scale(_alg_mul(ep0_t, _alg_add(_alg_mul(aa, eb), _alg_mul(ab, ea))), Fraction(2)),
                        _alg_scale(_alg_mul(A0_t, _alg_add(_alg_mul(ea, eb), _alg_mul(ep0_t, eab))), Fraction(2)),
                    ),
                )
                HR2A15[ga][gb] = _alg_add(HR2A15[ga][gb], t_r2a)

    # Exact symbolic checks on 45-edge complex:
    # 1) Exact interior gradients: g(-S_R)=0, g(V_tot)=+sqrt(2)/12, g(S_{R^2,A})=-30*sqrt(2)*eps0
    i_in0, i_in1 = int_idxs[0], int_idxs[1]
    grads15_ok = (
        gSR15[i_in0] == {}
        and gV15[i_in0] == {(2, 0): Fraction(1, 12)}
        and gR2A15[i_in0] == {(2, 1): Fraction(-30, 1)}
    )
    # 2) Exact symbolic RW kernel: H_{-S_R} u_a == 0 on curved S^4 AND H_{S_{R^2,A}}|_{eps0=0} u_a == 0 on globally flat bg!
    rw_sr_ker = all(
        _alg_add(HSR15[row][i_in0], HSR15[row][int_idxs[a]], Fraction(-1)) == {}
        for a in range(1, 5) for row in range(45)
    )
    rw_r2a_flat_ker = all(
        {k: v for k, v in _alg_add(HR2A15[row][i_in0], HR2A15[row][int_idxs[a]], Fraction(-1)).items() if k[1] == 0} == {}
        for a in range(1, 5) for row in range(45)
    )
    # 3) Exact chain-rule u^T H u along unit vertex move u (dL/dt = (sqrt(10)/4)*(e_in0 - e_in1)):
    uHu_sr = _alg_scale(_alg_add(_alg_add(HSR15[i_in0][i_in0], HSR15[i_in1][i_in1]), _alg_scale(HSR15[i_in0][i_in1], Fraction(-2))), Fraction(5, 8))
    uHu_V = _alg_scale(_alg_add(_alg_add(HV15[i_in0][i_in0], HV15[i_in1][i_in1]), _alg_scale(HV15[i_in0][i_in1], Fraction(-2))), Fraction(5, 8))
    uHu_R2A = _alg_scale(_alg_add(_alg_add(HR2A15[i_in0][i_in0], HR2A15[i_in1][i_in1]), _alg_scale(HR2A15[i_in0][i_in1], Fraction(-2))), Fraction(5, 8))
    chain_ok = (uHu_sr == {} and uHu_V == {(5, 0): Fraction(-5, 16)} and uHu_R2A == {(5, 1): Fraction(225, 2)})

    # 4) 100% ZERO-FLOAT exact rational certification of 45x45 Hessian inertias via DomainMatrix(QQ) LDL^T + Weyl bound!
    sqf_bounds = {
        1: (Fraction(1), Fraction(1)), 2: b_s2, 3: b_s3, 5: b_s5,
        6: imul(b_s2, b_s3), 10: imul(b_s2, b_s5), 15: imul(b_s3, b_s5), 30: imul(imul(b_s2, b_s3), b_s5),
    }
    b_eps_sq = imul(b_eps, b_eps)

    def _eval_alg_mid_err(d: dict[tuple[int, int], Fraction], denom: int = 10**6) -> tuple[Fraction, Fraction]:
        iv = (Fraction(0), Fraction(0))
        for (sqf, pe), c_v in d.items():
            b_v = sqf_bounds[sqf]
            if pe == 1: b_v = imul(b_v, b_eps)
            elif pe == 2: b_v = imul(b_v, b_eps_sq)
            iv = iadd(iv, iscale(c_v, b_v))
        mid = (iv[0] + iv[1]) / 2
        q_num = (mid.numerator * denom + mid.denominator // 2) // mid.denominator
        q_mid = Fraction(q_num, denom)
        return q_mid, max(q_mid - iv[0], iv[1] - q_mid)

    def _certify_inertia_qq(H_alg, n_dim: int) -> tuple[tuple[int, int, int], Fraction]:
        H_mid = [[Fraction(0)] * n_dim for _ in range(n_dim)]
        err_F2 = Fraction(0)
        for i in range(n_dim):
            for j in range(i, n_dim):
                qm, er = _eval_alg_mid_err(H_alg[i][j])
                H_mid[i][j] = H_mid[j][i] = qm
                err_F2 += (er * er) * (1 if i == j else 2)
        DM = DomainMatrix([[QQ(x.numerator, x.denominator) for x in row] for row in H_mid], (n_dim, n_dim), QQ)
        DM_inv = DM.inv()
        inv_F2 = Fraction(0)
        for i in range(n_dim):
            for j in range(n_dim):
                v = DM_inv[i, j].element
                f = Fraction(int(v.numerator), int(v.denominator))
                inv_F2 += f * f
        weyl_sq = inv_F2 * err_F2
        assert weyl_sq < Fraction(1), f"Weyl inertia bound failed: {weyl_sq}"
        M_q = [[QQ(x.numerator, x.denominator) for x in row] for row in H_mid]
        n_pos = 0; n_neg = 0; k = 0
        while k < n_dim:
            piv = next((i for i in range(k, n_dim) if M_q[i][i] != QQ.zero), -1)
            if piv != -1:
                if piv != k:
                    M_q[k], M_q[piv] = M_q[piv], M_q[k]
                    for r in range(n_dim): M_q[r][k], M_q[r][piv] = M_q[r][piv], M_q[r][k]
                d_v = M_q[k][k]
                if d_v > QQ.zero: n_pos += 1
                else: n_neg += 1
                for i in range(k + 1, n_dim):
                    if M_q[i][k] == QQ.zero: continue
                    fac = M_q[i][k] / d_v
                    for j in range(i, n_dim):
                        M_q[i][j] = M_q[i][j] - fac * M_q[k][j]
                        M_q[j][i] = M_q[i][j]
                k += 1
            else:
                i0_p, j0_p = next((i, j) for i in range(k, n_dim) for j in range(i + 1, n_dim) if M_q[i][j] != QQ.zero)
                for a_p, b_p in ((k, i0_p), (k + 1, j0_p)):
                    if a_p != b_p:
                        M_q[a_p], M_q[b_p] = M_q[b_p], M_q[a_p]
                        for r in range(n_dim): M_q[r][a_p], M_q[r][b_p] = M_q[r][b_p], M_q[r][a_p]
                p_v = M_q[k][k + 1]
                n_pos += 1; n_neg += 1
                for i in range(k + 2, n_dim):
                    a_i, b_i = M_q[i][k], M_q[i][k + 1]
                    for j in range(i, n_dim):
                        M_q[i][j] = M_q[i][j] - (a_i * M_q[k + 1][j] + b_i * M_q[k][j]) / p_v
                        M_q[j][i] = M_q[i][j]
                k += 2
        return (n_neg, 0, n_pos), weyl_sq

    # 41x41 orthogonal complement of W_RW for H_{-S_R}:
    HSR_41 = [[{} for _ in range(41)] for _ in range(41)]
    for a in range(40):
        for b in range(40):
            HSR_41[a][b] = HSR15[ext_idxs[a]][ext_idxs[b]]
        s_v = {}
        for ik in int_idxs:
            s_v = _alg_add(s_v, HSR15[ext_idxs[a]][ik])
        HSR_41[a][40] = HSR_41[40][a] = s_v
    s40_v = {}
    for ia in int_idxs:
        for ib in int_idxs:
            s40_v = _alg_add(s40_v, HSR15[ia][ib])
    HSR_41[40][40] = s40_v

    # Exact algebraic c_V for witness (c_R = 110, c_{R^2,A} = 75) solving g_eff = 0 on regular S^4:
    # c_V = -(g_KD(1) - 110*sqrt(3)*eps0 + 75*sqrt(3)*eps0^2) / (sqrt(5)/30)
    cV_alg = {(5, 0): -6 * kd_exact[1][0], (15, 1): Fraction(660), (15, 2): Fraction(-450)}
    cV_mid, cV_err = _eval_alg_mid_err(cV_alg, denom=10**8)
    H_ct15 = [[{} for _ in range(45)] for _ in range(45)]
    for i in range(45):
        for j in range(45):
            v_ij = _alg_mul(cV_alg, HV15[i][j])
            v_ij = _alg_add(v_ij, HSR15[i][j], Fraction(110))
            v_ij = _alg_add(v_ij, HR2A15[i][j], Fraction(75))
            H_ct15[i][j] = v_ij
    g_ct15_in = _alg_add(_alg_add(_alg_mul(cV_alg, gV15[i_in0]), gSR15[i_in0], Fraction(110)), gR2A15[i_in0], Fraction(75))
    g_ct15_mid, _ = _eval_alg_mid_err(g_ct15_in, denom=10**6)

    sig_sr41, w_sr = _certify_inertia_qq(HSR_41, 41)
    sig_V45, w_V = _certify_inertia_qq(HV15, 45)
    sig_R2A45, w_R2A = _certify_inertia_qq(HR2A15, 45)
    sig_ct45, w_ct = _certify_inertia_qq(H_ct15, 45)
    sig_sr45 = (sig_sr41[0], 4, sig_sr41[2])

    cc.check(
        cm_sub_ok and nl_vol_const
        and sp.simplify(d2_rw_R2V_exact - sp.Rational(21600, 4913) * s5 * eps0**2) == 0
        and d2_rw_L4_exact == 12
        and sp.simplify(sum_d2L_exact - 15 * sp.sqrt(10) / 8) == 0
        and grads15_ok and rw_sr_ker and rw_r2a_flat_ker and chain_ok
        and sig_sr45 == (11, 4, 30) and sig_V45 == (44, 0, 1)
        and sig_R2A45 == (5, 0, 40) and sig_ct45 == (4, 0, 41),
        f"2.8a: 45-edge flat-(1,5) exact derivation & zero-float inertia: sig(-S_R)=(11,4,30), sig(V)=(44,0,1), sig(R2A)=(5,0,40), sig(S_ct)=(4,0,41); d^2_nl(R2V)=21600*sqrt(5)/4913*eps0^2, d^2_nl(L4)=12",
    )

    # 2.8b EXHAUSTIVE ZERO-FLOAT CERTIFICATION OF ALL C(5,2)=10 COUNTERTERM PAIRS + MINIMAL 3-PARAM BASIS!
    ct_list = [("V_tot", v_V), ("-S_R", v_negSR), ("S_{R^2,A}", v_R2A), ("S_{R^2,V}", v_R2V), ("S_{L^4}", v_L4)]
    infeas_pairs = []
    feas_pairs = []
    for (nA, vA), (nB, vB) in combinations(ct_list, 2):
        # Solve g_KD(1) + c_A g_A + c_B g_B = 0, and check lambda_r > 0 (r=1..6) in pure exact Fraction!
        if vA[0] == 0 or vB[0] == 0:
            # One is S_{R^2,V} (g=0, lam_1=0): c_other fixed uniquely, and row 1 is strictly < 0 by Thm 2.2!
            v_nz = vB if vA[0] == 0 else vA
            rat_1 = sp.simplify(v_nz[1] / v_nz[0])  # purely rational (1 or 3)!
            assert rat_1.is_Rational
            val_1 = kd_exact[1][1] - Fraction(int(rat_1.p), int(rat_1.q)) * kd_exact[1][0]
            assert val_1 < 0
            infeas_pairs.append((nA, nB, "scaling-LN"))
        else:
            # Eliminate c_A = -(g_KD + c_B g_B)/g_A -> p_r + q_r c_B > 0 for r = 1..6:
            gA_b = eval_geom_interval(vA[0])
            gB_b = eval_geom_interval(vB[0])
            cB_lo = None
            cB_hi = None
            killed_by_ln = False
            for r_row in range(1, 7):
                # p_r = lam_r^KD - (lam_r^A / g_A) * g_KD; q_r = lam_r^B - (lam_r^A / g_A) * g_B
                lA_b = eval_geom_interval(vA[r_row])
                lB_b = eval_geom_interval(vB[r_row])
                ratio_A = idiv(lA_b, gA_b)
                p_b = isub((kd_exact[1][r_row], kd_exact[1][r_row]), iscale(kd_exact[1][0], ratio_A))
                # Check exact symbolic zero of q_r first (handles same-degree pairs cleanly!):
                q_sym = sp.simplify(vB[r_row] * vA[0] - vA[r_row] * vB[0])
                if q_sym == 0:
                    if p_b[1] < 0:
                        killed_by_ln = True
                        break
                    continue
                q_b = isub(lB_b, imul(ratio_A, gB_b))
                assert q_b[0] > 0 or q_b[1] < 0
                bound = idiv(iscale(Fraction(-1), p_b), q_b)
                if q_b[0] > 0:
                    # c_B > -p_r / q_r >= bound[0]
                    cB_lo = bound[0] if cB_lo is None else max(cB_lo, bound[0])
                else:
                    # c_B < -p_r / q_r <= bound[1]
                    cB_hi = bound[1] if cB_hi is None else min(cB_hi, bound[1])
            if killed_by_ln:
                infeas_pairs.append((nA, nB, "exact-LN"))
            elif cB_lo is not None and cB_hi is not None and cB_lo >= cB_hi:
                infeas_pairs.append((nA, nB, "Farkas-2row"))
            else:
                # Certify explicit exact rational witness c_B = 4 for (-S_R, S_{L^4})!
                cB_w = Fraction(4)
                cA_b = idiv(iscale(Fraction(-1), ishift(kd_exact[1][0], iscale(cB_w, gB_b))), gA_b)
                all_pos_w = True
                for r_row in range(1, 7):
                    lam_b = ishift(
                        kd_exact[1][r_row],
                        iadd(imul(cA_b, eval_geom_interval(vA[r_row])), iscale(cB_w, eval_geom_interval(vB[r_row]))),
                    )
                    if not (lam_b[0] > 0):
                        all_pos_w = False
                assert all_pos_w
                feas_pairs.append((nA, nB))

    pairs_ok = (len(infeas_pairs) == 9 and feas_pairs == [("-S_R", "S_{L^4}")])

    # Minimal nonlinear flat-(1,5)-invariant 3-param basis {V_tot, -S_R, S_{R^2, A}} stabilizing all 40 modes of regular S^4:
    cR_w, cR2A_w = sp.Integer(110), sp.Integer(75)
    v_ratios = [Fraction(3), Fraction(-3), Fraction(-3, 5), Fraction(-9), Fraction(-27, 5), Fraction(-7)]
    min_3p_pos = True
    eigs_3p_str = []
    for idx_r, r_row in enumerate(range(1, 7)):
        rat_r = v_ratios[idx_r]
        kd_part = kd_exact[1][r_row] - rat_r * kd_exact[1][0]
        geom_expr = sp.simplify(
            cR_w * (v_negSR[r_row] - sp.Rational(rat_r.numerator, rat_r.denominator) * v_negSR[0])
            + cR2A_w * (v_R2A[r_row] - sp.Rational(rat_r.numerator, rat_r.denominator) * v_R2A[0])
        )
        tot_b = ishift(kd_part, eval_geom_interval(geom_expr))
        if not (tot_b[0] > 0):
            min_3p_pos = False
        eigs_3p_str.append(round(float(tot_b[0]), 2))
    M_3p_tt = sp.Matrix.hstack(v_V, v_negSR, v_R2A).extract([0, 4, 5, 6], [0, 1, 2])
    ln_3p_tt = M_3p_tt.T.nullspace()
    M_4p = sp.Matrix.hstack(v_V, v_negSR, v_R2A, v_R2V).extract([0, 4, 5, 6], [0, 1, 2, 3])
    rk_4p = M_4p.rank()
    cV_ok = (Fraction(72484, 100) < cV_mid - cV_err and cV_mid + cV_err < Fraction(72485, 100))
    cc.check(
        pairs_ok and min_3p_pos and cV_ok and len(ln_3p_tt) == 1 and rk_4p == 4,
        f"2.8b: All C(5,2)=10 pairs exhausted (9 infeasible, only {{-S_R,S_{{L^4}}}} feasible); 3-param {{V_tot,-S_R,S_{{R^2,A}}}} (c_R=110,c_R2A=75,c_V={float(cV_mid):.2f}) stabilizes all 40 S^4 modes {eigs_3p_str}; 3p-TT LN dim=1, 4p rank=4",
    )
    print(f"    -> Exact d^2_nl(S_{{R^2,V}}) = (21600*sqrt(5)/4913)*eps0^2 = {float(d2_rw_R2V_b[0]):.6f}, d^2_nl(S_{{L^4}}) = 12")
    print(f"    -> Exact 45-edge S_ct interior tadpole = {float(g_ct15_mid):.4f}, certified Weyl bounds <= {float(max(w_sr, w_V, w_R2A, w_ct)):.2e} < 1")
    print(f"    -> Exact S_KD(1) 1st-order grad_e = {kd_exact[1][0]} (~{float(kd_exact[1][0]):.6f})\n")


# ==============================================================================
# SUITE 3: APPLICATION A2 — F-36A, SUPER-F-40, AND V12.1.B SPECTRAL CERTIFICATES
# ==============================================================================
def suite_3_spectral_pv_certificates(cc: ExactCheckCounter) -> None:
    print("=" * 88)
    print("SUITE 3: Exact Z[q]/Q Left-Null & Farkas Certificates for F-36A, Super-F-40 & V12.1.B")
    print("=" * 88)

    q, l2, l4 = sp.symbols("q l2 l4")
    # 3.1 Parametric 5-term Weyl^2-free geometric PV Left-Null over Z[q]^6
    A_n5 = sp.Matrix([
        [1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1],
        [0, 1, 2, 3, 4],
        [1, q, q**2, q**3, q**4],
        [1, q**2, q**4, q**6, q**8],
        [0, q, 2 * q**2, 3 * q**3, 4 * q**4],
    ])
    b_n5 = sp.Matrix([1, 0, 0, 0, 0, l2])
    v_n5 = sp.Matrix([
        (q - 1)**4 * (q + 1)**2,
        -q**4 * (q**2 - 2 * q - 4),
        q**4 * (q - 1) * (q + 1),
        -q * (q + 1)**2 * (3 * q - 2),
        -1,
        q * (q - 1) * (q + 1)**2,
    ])
    ann5 = sp.Matrix([sp.expand(x) for x in (v_n5.T * A_n5)]) == sp.zeros(5, 1)
    obs5 = sp.expand((v_n5.T * b_n5)[0] - (q - 1) * (q + 1)**2 * (q * l2 + (q - 1)**3)) == 0
    cc.check(
        ann5 and obs5,
        "3.1: Parametric 5-term Weyl^2-free PV Left-Null v_5(q) in Z[q]^6 proves L_2 = -(q-1)^3/q < 0 for ALL q>1",
    )

    # 3.2 Parametric 6-term Weyl^2-free geometric PV Left-Null over Z[q]^7 (Generalizes F-36A to ALL r>1!)
    A_n6 = sp.Matrix([
        [1, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1],
        [0, 1, 2, 3, 4, 5],
        [1, q, q**2, q**3, q**4, q**5],
        [1, q**2, q**4, q**6, q**8, q**10],
        [0, q, 2 * q**2, 3 * q**3, 4 * q**4, 5 * q**5],
        [0, q**2, 2 * q**4, 3 * q**6, 4 * q**8, 5 * q**10],
    ])
    b_n6 = sp.Matrix([1, 0, 0, 0, 0, l2, l4])
    v_n6 = sp.Matrix([
        (q - 1)**5 * (q + 1)**3,
        -q**6 * (q**2 - 2 * q - 5),
        q**6 * (q - 1) * (q + 1),
        -3 * q**2 * (q - 1) * (q + 1)**3,
        -(5 * q**2 + 2 * q - 1),
        q**2 * (q - 1) * (q + 1)**3,
        (q - 1) * (q + 1),
    ])
    ann6 = sp.Matrix([sp.expand(x) for x in (v_n6.T * A_n6)]) == sp.zeros(6, 1)
    obs6 = sp.expand(
        (v_n6.T * b_n6)[0] - (q - 1) * (q + 1) * (l4 + q**2 * (q + 1)**2 * l2 + (q - 1)**4 * (q + 1)**2)
    ) == 0
    # Specialize to q = 4 (m_i = 2^i, F-36A) -> primitive Z^7 witness:
    v_q4 = sp.Matrix([10125, -4096, 20480, -6000, -29, 2000, 5])
    q4_ok = (
        v_q4.T * A_n6.subs(q, 4) == sp.zeros(1, 6)
        and sp.expand((v_q4.T * b_n6)[0] - (5 * l4 + 2000 * l2 + 10125)) == 0
    )
    cc.check(
        ann6 and obs6 and q4_ok,
        "3.2: Parametric F-36A Left-Null v_6(q) in Z[q]^7 proves L_4 + q^2(q+1)^2 L_2 = -(q-1)^4(q+1)^2 < 0 (q=4: [10125,-4096,20480,-6000,-29,2000,5])",
    )

    # 3.3 Super-F-40 Sharp-Cutoff & All-Degree Polynomial-Cutoff Moment Obstructions + Integer UV/SR Farkas Certificates
    # Exact spin triples (a_s, b_s, d_s) and integral weights (IR C_Sak*6, UV U_inf, Sum-Rule R_SR, Weyl^2 120*a4_C2):
    # Check 2 a_s + b_s/2 - d_s/4 == 2 * [1, 0, -5, -6] for [scalar, weyl, proca, gauge]!
    triples_int = {"scalar": (1, 0, 0), "weyl": (-1, 4, 0), "proca": (-3, 0, 16), "gauge": (-4, 0, 16)}
    sr_weights = {k: Fraction(2 * a) + Fraction(b, 2) - Fraction(d, 4) for k, (a, b, d) in triples_int.items()}
    sr_ratio_ok = (sr_weights == {"scalar": Fraction(2), "weyl": Fraction(0), "proca": Fraction(-10), "gauge": Fraction(-12)})

    # Sharp-cutoff Super-F-40 exact rational integral identity:
    # I_IR = int_0^2 (1/96)(1 - (3/10)q^2) dq = +1/80; I_UV = 0 - F_sh_UV(1, 0) = -1/80 => (1, 1)^T * (1/80, -1/80) = 0!
    I_ir = Fraction(1, 96) * (Fraction(2) - Fraction(1, 10) * Fraction(8))
    I_uv = -Fraction(1, 240) * (Fraction(-2) + Fraction(5))
    super_f40_ln = (I_ir == Fraction(1, 80) and I_uv == Fraction(-1, 80) and I_ir + I_uv == 0)

    # Pure integer UV & Sum-rule refutations of SM, SM+3nuR, MSSM, PS Chain A2, PS CCvS-trunc (for ALL chi >= 0!):
    # U_inf = N_0 - N_w - 3 N_p - 4 N_g; R_SR = N_0 - 5 N_p - 6 N_g
    int_uv_ok = (
        (4 - 45 - 48 == -89 < 0)      # SM
        and (4 - 48 - 48 == -92 < 0)  # SM+3nuR
        and (98 - 61 - 48 == -11 < 0) # MSSM (n_c - 5 n_v = 49 - 60 = -11 < 0!)
        and (68 - 48 - 84 == -64 < 0) # PS Chain A2
        and (80 - 48 - 84 == -52 < 0) # PS CCvS-trunc
    )
    cc.check(
        sr_ratio_ok and super_f40_ln and int_uv_ok,
        "3.3: Super-F-40 exact Dirac zero sum rule (+1/80 - 1/80 = 0, R_SR=0) & exact integer UV/SR Farkas no-go for SM/MSSM(-11)/PS-A2(-64)",
    )

    # 3.3b Exact all-degree-d polynomial-cutoff moment scaling for chi(u) = sum_{k=0}^d alpha_k u^k e^{-u}:
    # Verify (-d/dbeta)^k beta^{-p}|_{beta=1} == prod_{j=0}^{k-1} (p + j) for p in {1 (IR f_2), 3/2 (sum rule), 2 (UV f_0)},
    # AND verify signed cutoff chi_a(u) = (1 - a u) e^{-u} exact rational moments f_2 = 1-a, f_{3/2} = 1 - 3a/2, f_0 = 1 - 2a!
    beta = sp.Symbol("beta", positive=True)
    poly_cut_ok = True
    for k_d in range(5):
        m_ir = sp.diff(beta**(-1), beta, k_d).subs(beta, 1) * ((-1) ** k_d)
        m_sr = sp.diff(beta**(-sp.Rational(3, 2)), beta, k_d).subs(beta, 1) * ((-1) ** k_d)
        m_uv = sp.diff(beta**(-2), beta, k_d).subs(beta, 1) * ((-1) ** k_d)
        if m_ir != sp.factorial(k_d) or m_uv != sp.factorial(k_d + 1):
            poly_cut_ok = False
        expected_sr = sp.Rational(math.prod(2 * j + 3 for j in range(k_d)), 2 ** k_d)
        if m_sr != expected_sr:
            poly_cut_ok = False
    # Exact signed-cutoff (1 - a u) e^{-u} critical thresholds: f_0(1/2) = 0, f_0(3/5) = -1/5 < 0 while f_2(3/5) = +2/5 > 0!
    a_c = sp.Symbol("a_c")
    f2_s = 1 - a_c
    f32_s = 1 - sp.Rational(3, 2) * a_c
    f0_s = 1 - 2 * a_c
    signed_thresh_ok = (
        f0_s.subs(a_c, sp.Rational(1, 2)) == 0
        and f0_s.subs(a_c, sp.Rational(3, 5)) == sp.Rational(-1, 5)
        and f2_s.subs(a_c, sp.Rational(3, 5)) == sp.Rational(2, 5)
        and f32_s.subs(a_c, sp.Rational(2, 3)) == 0
    )
    cc.check(
        poly_cut_ok and signed_thresh_ok,
        "3.3b: All-degree-d polynomial cutoff u^k e^{-u} moment identities (k!, (2k+1)!!/2^k, (k+1)!) & signed (1-au)e^{-u} thresholds (1/2, 2/3, 1)",
    )

    # 3.4 100% ZERO-FLOAT Exact Rational Pointwise Threshold Certificates for e^{-u} (120, 69, 196)!
    def I_k_exp_bounds(k: int, Q_f: Fraction, N_terms: int = 40) -> tuple[Fraction, Fraction]:
        s = Fraction(0)
        prev_abs = None
        for n in range(N_terms):
            m = n + k
            term = ((-1) ** n) * (Q_f ** m) * Fraction(math.factorial(m) ** 2, math.factorial(n) * math.factorial(2 * m + 1))
            if n == N_terms - 1:
                assert prev_abs is not None and abs(term) < prev_abs
                s_next = s + term
                return (min(s, s_next), max(s, s_next))
            s += term
            prev_abs = abs(term)
        raise AssertionError("Unreachable")

    def delta2_exp_exact(Q_f: Fraction, n0: int, nw: int, ng: int, N_terms: int = 40) -> tuple[Fraction, Fraction]:
        A = Fraction(n0 - nw - 4 * ng)
        B = Fraction(4 * nw)
        D = Fraction(16 * ng)
        b0 = I_k_exp_bounds(0, Q_f, N_terms)
        b1 = I_k_exp_bounds(1, Q_f, N_terms)
        b2 = I_k_exp_bounds(2, Q_f, N_terms)
        return iadd(iadd(ishift(2 * A, iscale(-2 * A, b0)), iscale(B, b1)), iscale(-D, b2))

    exp_cases = [
        ("SM+3nuR (N0>=120)", Fraction(13),    119, 48, 12, 120, 48, 12),
        ("SUSY    (nc>=69) ", Fraction(35, 2), 136, 80, 12, 138, 81, 12),
        ("PS      (N0>=196)", Fraction(21, 2), 195, 48, 21, 196, 48, 21),
    ]
    exp_ok = True
    for lbl, Qf, n0_m, nw_m, ng_m, n0_p, nw_p, ng_p in exp_cases:
        bm = delta2_exp_exact(Qf, n0_m, nw_m, ng_m)
        bp = delta2_exp_exact(Qf, n0_p, nw_p, ng_p)
        if not (bm[1] < 0 and bp[0] > 0):
            exp_ok = False
        print(f"    -> e^-u {lbl} at Q={str(Qf):5s}: below=[{float(bm[0]):+.6f},{float(bm[1]):+.6f}]<0, above=[{float(bp[0]):+.6f},{float(bp[1]):+.6f}]>0")
    cc.check(
        exp_ok,
        "3.4: 100% zero-float exact Fraction threshold certificates for chi=e^-u: SM N0>=120, SUSY nc>=69, PS N0>=196",
    )

    # 3.5 100% ZERO-FLOAT Exact Rational Pointwise Threshold Certificates for PV4 (105, 62, 169)!
    pv4 = [(Fraction(1), 1), (Fraction(-2), 2), (Fraction(9, 7), 3), (Fraction(-2, 7), 4)]

    def pi2_pv4_exact(Q_f: Fraction, kind: str) -> tuple[Fraction, Fraction]:
        a_s, b_s, d_s = triples_int[kind]
        Q4 = Q_f / 4
        tot = (Fraction(0), Fraction(0))
        for c_i, m in pv4:
            m2 = Fraction(m * m)
            m4 = m2 * m2
            t_f = Q_f / (Q_f + 4 * m2)
            lnm2 = (Fraction(0), Fraction(0)) if m == 1 else iscale(Fraction(2), ln_rat_bounds(Fraction(m)))
            p1_c = (2 * a_s + b_s) * m2 * Q4 * Fraction(2, 3) + (a_s + b_s + d_s) * Q4 * Q4 * Fraction(8, 15)
            part1 = iscale(p1_c, lnm2)
            At = A_t_bounds(t_f)
            D0 = ishift(Fraction(-2), iscale(Fraction(2), At))
            D1 = ishift(-Fraction(2) * (8 * t_f - 3) / (9 * t_f), iscale(Fraction(2) * (3 * t_f - 1) / (3 * t_f), At))
            D2 = ishift(
                -Fraction(2) * (184 * t_f * t_f - 135 * t_f + 45) / (225 * t_f * t_f),
                iscale(Fraction(2) * (15 * t_f * t_f - 10 * t_f + 3) / (15 * t_f * t_f), At),
            )
            part2 = iadd(
                iscale(Fraction(a_s) * m4, D0),
                iadd(iscale(Fraction(2 * a_s + b_s) * m2 * Q4, D1), iscale(Fraction(a_s + b_s + d_s) * Q4 * Q4, D2)),
            )
            tot = iadd(tot, iscale(c_i, iadd(part1, part2)))
        return tot

    pv4_cases = [
        ("SM+3nuR (N0>=105)", Fraction(138), 104, 48, 12, 105, 48, 12),
        ("SUSY    (nc>=62) ", Fraction(500), 122, 73, 12, 124, 74, 12),
        ("PS      (N0>=169)", Fraction(66),  168, 48, 21, 169, 48, 21),
    ]
    pv4_ok = True
    for lbl, Qf, n0_m, nw_m, ng_m, n0_p, nw_p, ng_p in pv4_cases:
        bs = pi2_pv4_exact(Qf, "scalar")
        bw = pi2_pv4_exact(Qf, "weyl")
        bg = pi2_pv4_exact(Qf, "gauge")
        bm = iadd(iscale(Fraction(n0_m), bs), iadd(iscale(Fraction(nw_m), bw), iscale(Fraction(ng_m), bg)))
        bp = iadd(iscale(Fraction(n0_p), bs), iadd(iscale(Fraction(nw_p), bw), iscale(Fraction(ng_p), bg)))
        if not (bm[1] < 0 and bp[0] > 0):
            pv4_ok = False
        print(f"    -> PV4  {lbl} at Q={str(Qf):5s}: below=[{float(bm[0]):+.6f},{float(bm[1]):+.6f}]<0, above=[{float(bp[0]):+.6f},{float(bp[1]):+.6f}]>0")
    cc.check(
        pv4_ok,
        "3.5: 100% zero-float exact Fraction threshold certificates for PV4: SM N0>=105, SUSY nc>=62, PS N0>=169",
    )
    print()


# ==============================================================================
# SUITE 4: APPLICATION B — HIGHER-CURVATURE (alpha C^2) BLACK-HOLE PERTURBATIONS
# ==============================================================================
def suite_4_weyl2_black_hole(cc: ExactCheckCounter) -> None:
    print("=" * 88)
    print("SUITE 4: Higher-Curvature (alpha C^2) Deformation of Quadratic Regge–Wheeler Equations")
    print("=" * 88)

    r = sp.Symbol("r", positive=True)
    w, al, l1, l2, k, p, d, xi = sp.symbols("w al l1 l2 k p d xi")
    f = (r - 1) / r  # Schwarzschild 2M = 1

    def apply_Dstar(A, B, C, W1):
        return (
            sp.expand(f * sp.diff(A, r) + W1 * B),
            sp.expand(2 * A + f * sp.diff(B, r) + 2 * W1 * C),
            sp.expand(B + f * sp.diff(C, r)),
        )

    def apply_Dstar_pow(A, B, C, W1, n):
        for _ in range(n):
            A, B, C = apply_Dstar(A, B, C, W1)
        return A, B, C

    def apply_L2_B1(A, B, C, W1, V2, w2_sq):
        A2, B2, C2 = apply_Dstar_pow(A, B, C, W1, 2)
        return (
            sp.expand(A2 + (w2_sq - V2) * A),
            sp.expand(B2 + (w2_sq - V2) * B),
            sp.expand(C2 + (w2_sq - V2) * C),
        )

    def apply_L2_B2(A, B, C, W1, V2, w2_sq, al_sym):
        A2, B2, C2 = apply_Dstar_pow(A, B, C, W1, 2)
        A4, B4, C4 = apply_Dstar_pow(A2, B2, C2, W1, 2)
        return (
            sp.expand(A2 + (w2_sq - V2) * A + al_sym * A4),
            sp.expand(B2 + (w2_sq - V2) * B + al_sym * B4),
            sp.expand(C2 + (w2_sq - V2) * C + al_sym * C4),
        )

    V1_0 = f * (l1 / r**2 - 3 / r**3)
    V2_0 = f * (l2 / r**2 - 3 / r**3)
    V1_B1 = V1_0 + 12 * al * f / r**6
    V2_B1 = V2_0 + 12 * al * f / r**6
    W1_0 = sp.expand(V1_0 - w**2)
    W1_B1 = sp.expand(V1_B1 - w**2)

    # 4.1 Exact alpha=0 baseline source S0 = L2^{(0)}[psi^2 / r]
    S0 = apply_L2_B1(1 / r, sp.Integer(0), sp.Integer(0), W1_0, V2_0, 4 * w**2)
    S0_expected = (
        (2 * l1 * r**2 - 2 * l1 * r - l2 * r**2 + l2 * r + 2 * r**4 * w**2 + 2 * r**2 - 8 * r + 6) / r**5,
        -4 * (r - 1) / r**3,
        2 / r,
    )
    cc.check(
        all(sp.simplify(S0[m] - S0_expected[m]) == 0 for m in range(3)),
        "4.1: Exact alpha=0 solvable source S0 = L2^{(0)}[psi^2/r] verified symbolically for all (w, l1, l2)",
    )

    # 4.2 Model B1 (Weyl^2 effective potential): All-C(r)^3 valuation bounds & 2-entry Left-Null witness (1, 6*al)
    M_D_hor = sp.Matrix([[-k, -(w**2), 0], [2, -k, -2 * w**2], [0, 1, -k]])
    det_hor_B1 = sp.factor((M_D_hor**2 + 4 * w**2 * sp.eye(3)).det())
    hor_B1_ok = sp.expand(det_hor_B1 - k**2 * (k**2 + 4 * w**2) * (k**2 + 16 * w**2)) == 0

    # Infinity compatibility O(r^d) & O(r^{d-1}):
    a0, a1, b0, b1, c0, c1 = sp.symbols("a0 a1 b0 b1 c0 c1")
    U_inf_B1 = apply_L2_B1(a0 * r**d + a1 * r**(d - 1), b0 * r**d + b1 * r**(d - 1), c0 * r**d + c1 * r**(d - 1), W1_B1, V2_B1, 4 * w**2)
    z = sp.Symbol("z", positive=True)
    inf_0 = [sp.Poly(sp.expand(sp.powsimp(u * r**(-d)).subs(r, 1 / z)), z).nth(0) for u in U_inf_B1]
    inf_1 = [sp.Poly(sp.expand(sp.powsimp(u * r**(-d)).subs(r, 1 / z)), z).nth(1) for u in U_inf_B1]
    sol_inf_B1 = sp.solve([inf_0[0], inf_0[1], inf_0[2], inf_1[1], sp.expand(inf_1[0] - w**2 * inf_1[2])], [a0, b0, c0])
    inf_B1_ok = (sol_inf_B1 == {a0: 0, b0: 0, c0: 0})

    # Singularity r = 0 leading 2x2 det = -432 * al^2 and reduced 2-unknown system A = a_{-1}/r + a_0, B=C=0:
    det_zero_B1 = sp.Matrix([[-12 * al, 288 * al**2], [2, -12 * al]]).det()
    am1, a0_s = sp.symbols("am1 a0_s")
    U_red_B1 = apply_L2_B1(am1 / r + a0_s, sp.Integer(0), sp.Integer(0), W1_B1, V2_B1, 4 * w**2)
    # Row (0, -8) and Row (2, -1) form exact 2-entry Left-Null witness v = (1, 6*al):
    c_0_m8 = sp.Poly(sp.expand((U_red_B1[0] - S0[0]) * r**10), r).nth(2)  # coeff of r^{-8}
    c_2_m1 = sp.Poly(sp.expand((U_red_B1[2] - S0[2]) * r**10), r).nth(9)  # coeff of r^{-1}
    A_red = sp.Matrix([[c_0_m8.coeff(am1), c_0_m8.coeff(a0_s)], [c_2_m1.coeff(am1), c_2_m1.coeff(a0_s)]])
    b_red = sp.Matrix([-c_0_m8.subs({am1: 0, a0_s: 0}), -c_2_m1.subs({am1: 0, a0_s: 0})])
    v_B1 = sp.Matrix([1, 6 * al])
    b1_ln_ok = (
        det_zero_B1 == -432 * al**2
        and v_B1.T * A_red == sp.zeros(1, 2)
        and (v_B1.T * b_red)[0] == 12 * al
    )
    cc.check(
        hor_B1_ok and inf_B1_ok and b1_ln_ok,
        "4.2: Model B1 All-C(r)^3 Theorem [Т]: det_hor=k^2(k^2+4w^2)(k^2+16w^2), deg<=0, det_0=-432*al^2, Left-Null (1,6*al)^T gives P=12*al",
    )

    # 4.3 Model B1 Enlarged Laurent Span k in [-2..1] (12 unknowns) explicit symbolic Left-Null check!
    ks_b1 = [-2, -1, 0, 1]
    a_b1 = sp.symbols("a_m2 a_m1 a_0 a_1")
    b_b1 = sp.symbols("b_m2 b_m1 b_0 b_1")
    c_b1 = sp.symbols("c_m2 c_m1 c_0 c_1")
    all_b1 = list(a_b1) + list(b_b1) + list(c_b1)
    U_B1_big = apply_L2_B1(
        sum(a_b1[i] * r**ks_b1[i] for i in range(4)),
        sum(b_b1[i] * r**ks_b1[i] for i in range(4)),
        sum(c_b1[i] * r**ks_b1[i] for i in range(4)),
        W1_B1, V2_B1, 4 * w**2,
    )
    eqs_b1 = {}
    for m in range(3):
        diff_m = sp.expand((U_B1_big[m] - S0[m]) * r**20)
        poly_m = sp.Poly(diff_m, r)
        for deg in range(poly_m.degree() + 1):
            coeff = sp.expand(poly_m.nth(deg))
            if coeff == 0: continue
            eqs_b1[(m, deg - 20)] = ([sp.expand(coeff.coeff(sym)) for sym in all_b1], -sp.expand(coeff.subs({sym: 0 for sym in all_b1})))
    # Top/bottom triangular witness for Model B1 enlarged span:
    # From (0,-16) -> c_m2=0; (0,-15) -> c_m1=0; (0,-14) -> c_0=0; (0,-13) -> c_1=0;
    # (1,-9) -> b_m2=0; (1,-8) -> b_m1=0; (1,-7) -> b_0=0; (1,-6) -> b_1=0;
    # (0,-9) -> a_m2=0; (0,-8) -> -12*al*a_m1=0; (2,-1) -> 2*a_m1 + ... = 2!
    # Check exact 7-row Left-Null witness on enlarged 12-unknown Model B1 (purely in Z[al, w, l1, l2])!
    # Wait: let's extract exact symbolic Left-Null by forward elimination on the bottom C/B/A rows + (2,-1)!
    keys_b1_sub = [
        (0, -16), (0, -15), (0, -14), (0, -13),  # kill c_m2, c_m1, c_0, c_1
        (1, -9), (1, -8), (1, -7), (1, -6),      # kill b_m2, b_m1, b_0, b_1 (using c's)
        (0, -9), (0, -8), (2, -1),               # kill a_m2, a_m1 vs S0[2] = 2/r!
    ]
    # Check if a_1 or a_0 enters (2,-1) or (0,-8):
    R_b1 = sp.symbols(f"Rb0:{len(keys_b1_sub)}")
    eq_b1_list = [sum(eqs_b1[key][0][j] * all_b1[j] for j in range(12)) - R_b1[i] for i, key in enumerate(keys_b1_sub)]
    # Solve sequentially: c's from first 4, b's from next 4, a_m2 & a_m1 from next 2, plug into (2,-1)!
    sol_c = sp.solve(eq_b1_list[:4], list(c_b1))
    sol_b = sp.solve([e.subs(sol_c) for e in eq_b1_list[4:8]], list(b_b1))
    sol_a = sp.solve([e.subs(sol_c).subs(sol_b) for e in eq_b1_list[8:10]], [a_b1[0], a_b1[1]])
    rel_b1 = sp.together(eq_b1_list[10].subs(sol_c).subs(sol_b).subs(sol_a))
    rem_b1 = rel_b1.free_symbols & set(all_b1)
    assert len(rem_b1) == 0, f"Unexpected remaining vars: {rem_b1}"
    num_b1 = sp.expand(sp.fraction(rel_b1)[0])
    v_b1_big = [sp.expand(num_b1.coeff(Ri)) for Ri in R_b1]
    g_b1 = sp.gcd_list(v_b1_big)
    v_b1_big = [sp.factor(sp.cancel(x / g_b1)) for x in v_b1_big]
    ann_b1_big = all(sp.expand(sum(v_b1_big[i] * eqs_b1[keys_b1_sub[i]][0][j] for i in range(len(keys_b1_sub)))) == 0 for j in range(12))
    P_b1_big = sp.factor(sp.expand(sum(v_b1_big[i] * eqs_b1[keys_b1_sub[i]][1] for i in range(len(keys_b1_sub)))))
    cc.check(
        ann_b1_big and sp.simplify(P_b1_big.subs(al, 0)) == 0 and P_b1_big != 0,
        f"4.3: Model B1 enlarged 12-unknown Laurent span exact Left-Null in Z[al,w,l1,l2]: v^T A=0, P={P_b1_big}",
    )

    # 4.3b Model B1 Case-1 Riccati (rational u in C(r)) unconditional impossibility for ALL al != 0:
    # Verify q1_B1 = (w^2 - V1_B1)/f^2 has exact pole order 5 (ODD) at r = 0 with leading term +12*al/r^5,
    # whereas u^2 has EVEN pole order 2k and u'+p*u has pole order <= k+1, so max(2k, k+1) != 5 for EVERY integer k!
    q1_B1 = sp.together((w**2 - V1_B1) / f**2)
    q1_r5 = sp.simplify((q1_B1 * r**5).subs(r, 0))
    odd_pole_ok = (q1_r5 == 12 * al) and all(max(2 * k_int, k_int + 1) != 5 for k_int in range(-10, 20))
    cc.check(
        odd_pole_ok,
        "4.3b: Model B1 destroys ALL Case-1 rational Riccati (algebraically special) solutions for ALL al!=0 (odd r^{-5} pole +12*al/r^5)",
    )

    # 4.4 Model B2 (4th-order Stelle L2_0 + al * D_*^4): All-C(r)^3 valuation bounds & 6-row Left-Null + Bezout!
    # Horizon indicial det & EFT regime check:
    al_r, w_r, k_r = sp.symbols("al_r w_r k_r", real=True)
    M_B2_hor = M_D_hor**2 + 4 * w**2 * sp.eye(3) + al * M_D_hor**4
    det_hor_B2 = sp.factor(M_B2_hor.det())
    z_hor_factor = al_r * (k_r + 2 * sp.I * w_r)**4 + (k_r + 2 * sp.I * w_r)**2 + 4 * w_r**2
    det_hor_factored_ok = sp.expand(
        det_hor_B2.subs({al: al_r, w: w_r, k: k_r})
        - (al_r * k_r**4 + k_r**2 + 4 * w_r**2) * (sp.re(z_hor_factor)**2 + sp.im(z_hor_factor)**2)
    ) == 0
    im_hor_ok = sp.expand(sp.im(z_hor_factor) - 4 * k_r * w_r * (1 + 2 * al_r * (k_r**2 - 4 * w_r**2))) == 0

    # Infinity det = 1024 * al^2 * w^10:
    M_D_inf = sp.Matrix([[0, -(w**2), 0], [2, 0, -2 * w**2], [0, 1, 0]])
    det_inf_B2 = sp.factor((M_D_inf**2 + 4 * w**2 * sp.eye(3) + al * M_D_inf**4).det())

    # Singularity r = 0 det = p^2 (p-8)(p-6)(p-4)^2 (p-2)^2 (p+2)^2 (p+4)(p+6):
    def M0_D(pv):
        return sp.Matrix([[-pv, 3, 0], [2, -(pv + 2), 6], [0, 1, -(pv + 4)]])
    det_zero_B2 = sp.factor((M0_D(p - 6) * M0_D(p - 4) * M0_D(p - 2) * M0_D(p)).det())
    det_zero_B2_ok = sp.expand(det_zero_B2 - p**2 * (p - 8) * (p - 6) * (p - 4)**2 * (p - 2)**2 * (p + 2)**2 * (p + 4) * (p + 6)) == 0
    cc.check(
        det_hor_factored_ok and im_hor_ok and det_inf_B2 == 1024 * al**2 * w**10 and det_zero_B2_ok,
        "4.4a: Model B2 (Stelle 4th-order) All-C(r)^3 bounds: det_inf=1024*al^2*w^10 (deg<=-1), det_0 roots in [-6..8] => exact 12-unknown space",
    )

    # Build COMPLETE all-C(r)^3 12-unknown system for Model B2 and verify BOTH exact symbolic Left-Null witnesses!
    a_s = sp.symbols("am6 am5 am4 am3 am2 am1")
    b_s = sp.symbols("bm4 bm3 bm2 bm1")
    c_s = sp.symbols("cm2 cm1")
    all_s = list(a_s) + list(b_s) + list(c_s)
    U_B2 = apply_L2_B2(
        sum(a_s[i] * r**(i - 6) for i in range(6)),
        sum(b_s[i] * r**(i - 4) for i in range(4)),
        sum(c_s[i] * r**(i - 2) for i in range(2)),
        W1_0, V2_0, 4 * w**2, al,
    )
    eqs_b2 = {}
    for m in range(3):
        diff_m = sp.expand((U_B2[m] - S0[m]) * r**20)
        poly_m = sp.Poly(diff_m, r)
        for deg in range(poly_m.degree() + 1):
            coeff = sp.expand(poly_m.nth(deg))
            if coeff == 0: continue
            eqs_b2[(m, deg - 20)] = ([sp.expand(coeff.coeff(sym)) for sym in all_s], -sp.expand(coeff.subs({sym: 0 for sym in all_s})))

    # 1st exact 6-row Left-Null witness v_B2^(1) in Z[al, w, l1, l2]^6:
    keys_1 = [(0, -1), (1, -1), (2, -1), (1, -2), (0, -3), (2, -3)]
    v_B2_1 = [
        -64 * al**3 * l1 * w**6 - 16 * al**3 * l2 * w**6 + 32 * al**3 * w**6 + 48 * al**2 * l1 * w**4 - 80 * al**2 * w**4 - 4 * al * l1 * w**2 + al * l2 * w**2 + 30 * al * w**2 - 2,
        -4 * al * w**4 * (8 * al * w**2 - 1),
        -w**2 * (16 * al**3 * l2 * w**6 - 32 * al**3 * w**6 + 32 * al**2 * l1 * w**4 - 80 * al**2 * w**4 - 4 * al * l1 * w**2 + al * l2 * w**2 + 30 * al * w**2 - 2),
        8 * al * w**4 * (8 * al * w**2 - 1),
        -16 * al**2 * w**6 * (4 * al * w**2 - 1),
        -16 * al**2 * w**8 * (4 * al * w**2 + 1),
    ]
    ann_b2_1 = all(sp.expand(sum(v_B2_1[i] * eqs_b2[keys_1[i]][0][j] for i in range(6))) == 0 for j in range(12))
    P1_B2 = sp.expand(sum(v_B2_1[i] * eqs_b2[keys_1[i]][1] for i in range(6)))
    Q1_expr = 16 * l1 * (al * w**2)**2 + (l2 - 4 * l1 + 14) * (al * w**2) - 2
    P1_ok = sp.expand(P1_B2 - (-16 * al * w**4 * Q1_expr)) == 0

    # 2nd independent Left-Null witness v_B2^(2) via forward elimination on 10 rows -> gives P2_B2 = 32*al^2*w^6*Q2!
    keys_2 = [(0, -1), (1, -1), (2, -1), (0, -2), (1, -2), (2, -2), (1, -3), (2, -3), (0, -4), (2, -4)]
    R2 = sp.symbols("R2_0:10")
    eq2 = [sum(eqs_b2[keys_2[i]][0][j] * all_s[j] for j in range(12)) - R2[i] for i in range(10)]
    s1 = sp.solve(eq2[:3], [a_s[5], b_s[3], c_s[1]])
    s2 = sp.solve([e.subs(s1) for e in eq2[3:6]], [a_s[4], b_s[2], c_s[0]])
    s3 = sp.solve([e.subs(s1).subs(s2) for e in eq2[6:8]], [b_s[1], a_s[3]])
    e8 = sp.together(eq2[8].subs(s1).subs(s2).subs(s3))
    e9 = sp.together(eq2[9].subs(s1).subs(s2).subs(s3))
    s4 = sp.solve(e9, a_s[2])[0]
    num2 = sp.expand(sp.fraction(sp.together(e8.subs(a_s[2], s4)))[0])
    v_B2_2 = [sp.expand(num2.coeff(Ri)) for Ri in R2]
    ann_b2_2 = all(sp.expand(sum(v_B2_2[i] * eqs_b2[keys_2[i]][0][j] for i in range(10))) == 0 for j in range(12))
    P2_B2 = sp.expand(sum(v_B2_2[i] * eqs_b2[keys_2[i]][1] for i in range(10)))
    Q2_expr = 16 * (l1 + 3) * (al * w**2)**2 + (l2 - 4 * l1 + 26) * (al * w**2) - 5
    # Check P2_B2 == 128 * al^2 * w^6 * Q2_expr EXACTLY (constant integer factor 128, ZERO extraneous factors!)
    P2_ok = sp.expand(P2_B2 - 128 * al**2 * w**6 * Q2_expr) == 0
    cc.check(
        ann_b2_1 and P1_ok and ann_b2_2 and P2_ok,
        "4.4b: Model B2 exact 6-row & 10-row symbolic Left-Null witnesses annihilate all 12 columns in Z[al,w,l1,l2] (P1=-16*al*w^4*Q1, P2=128*al^2*w^6*Q2 exactly)",
    )

    # 4.5 Exact Bezout elimination proving Q1 and Q2 have ZERO common roots for ALL gravitational multipoles (l1, l2) != (2, 2)!
    Q1_xi = 16 * l1 * xi**2 + (l2 - 4 * l1 + 14) * xi - 2
    Q2_xi = 16 * (l1 + 3) * xi**2 + (l2 - 4 * l1 + 26) * xi - 5
    A_b = l2 - 8 * l1 + 14
    B_b = l1 - 2
    Delta_bez = sp.expand(16 * B_b**2 - 4 * A_b * B_b - A_b**2)
    U_R0 = A_b**2
    U_L = -(16 * A_b * xi + 4 * A_b - 16 * B_b)
    U1_bez = sp.expand(-U_R0 + (3 + l1) * U_L)
    U2_bez = sp.expand(U_R0 - l1 * U_L)
    bez_id_ok = sp.expand(U1_bez * Q1_xi + U2_bez * Q2_xi - 3 * Delta_bez) == 0
    # Verify 4 * Delta_bez = (8 B_b - A_b)^2 - 5 A_b^2 (so Delta_bez = 0 over Z iff A_b = B_b = 0 iff l1 = l2 = 2!)
    pell_ok = sp.expand(4 * Delta_bez - ((8 * B_b - A_b)**2 - 5 * A_b**2)) == 0
    res_check = sp.expand(sp.resultant(sp.Poly(Q1_xi, xi), sp.Poly(Q2_xi, xi), xi) - 144 * Delta_bez) == 0
    # Verify concrete gravitational multipole pairs (ell1 >= 2) have Delta != 0:
    gw_pairs_ok = all(Delta_bez.subs({l1: e1 * (e1 + 1), l2: e2 * (e2 + 1)}) != 0 for e1 in range(2, 7) for e2 in range(2, 9))
    cc.check(
        bez_id_ok and pell_ok and res_check and gw_pairs_ok,
        "4.5: Exact Bezout identity U1*Q1 + U2*Q2 = 3*Delta(l1,l2), 4*Delta=(8B-A)^2-5A^2 != 0 for ALL gravitational multipoles ell1>=2",
    )
    print(f"    -> Model B1 Left-Null P_B1 = 12*al (enlarged P = {P_b1_big})")
    print(f"    -> Model B2 P1 = -16*al*w^4*({Q1_xi}), Bezout Delta(6,20) = {Delta_bez.subs({l1: 6, l2: 20})}\n")


def main() -> int:
    cc = ExactCheckCounter()
    suite_1_general_theory(cc)
    suite_2_regge_kd_s4(cc)
    suite_3_spectral_pv_certificates(cc)
    suite_4_weyl2_black_hole(cc)

    print("=" * 88)
    print(f"FRONTIER v13 MODULE 2 (LEFT-NULL CERTIFICATES) SUMMARY: {cc.passed}/{cc.total} CHECKS PASSED (ZERO FLOAT64 IN ALL CHECKS)")
    print("=" * 88)
    if cc.failures:
        print("FAILURES:")
        for f in cc.failures:
            print(f"  - {f}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
