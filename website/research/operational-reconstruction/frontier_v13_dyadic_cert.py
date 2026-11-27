"""
Deep Frontier v13 — Module 3: Certified Outward-Rounded Dyadic Interval Engine (`frontier_v13_dyadic_cert.py`, ZERO float64!)
==========================================================================================
Pure-Python arbitrary-precision exact integer bit-shift DyadicInterval calculus aligned 1-to-1
with Lean 4 `ConstructiveR` (0 Classical.choice, 0 sorry, {propext, Quot.sound} only).

ZERO imports of `math`, `numpy`, `scipy`, `mpmath`, or `decimal`!
Every single interval endpoint is an exact Python integer pair `(mant, exp)` representing
`mant * 2^exp`, with mathematically sound floor/ceil bit-shift outward rounding.

Certifies all 4 flagship frontier results from float64 [C] -> mathematically certified [T]:
  1. Super-F-40 & V12.1.B Spectral-Action Ghost Enclosures:
     - Sharp cutoff Theta(1-u): IR q=1 > 0, exact Krawczyk root q_* = sqrt(10/3), q=2 < 0,
       desingularized UV integral & certified zero sum-rule cancellation;
     - Smooth exponential chi(u) = e^-u & signed (1 - 0.6 u) e^-u (pure Dirac): certified
       order-4 Peano-Simpson quadrature, ghost root Krawczyk certificates, sum-rule enclosures;
     - Mixed SM, MSSM, CCvS (Chain A2, CCvS-FULL-R, CCvS-FULL-C signed): certified ghost zeros!
  2. F-36B Kallen-Lehmann Spectral Density Negativity (PV4 & PV6_esc):
     - Certified strict rho_2(s) < 0 at concrete s > 4 m_1^2 (PV4: s=32, 36; PV6_esc: s=25, 30)
       and Krawczyk-certified zero crossings s_*!
  3. 4D Deformed S^4 (partial beta_5) Regge-Schlafli 40x40 Hessian Inertia (10 neg / 30 pos):
     - Exact analytical 40x40 Hessian in DyadicInterval (ZERO finite-diff, ZERO eigvalsh!);
     - Certified BOTH via direct 256-bit interval LDL^T Sylvester Law of Inertia AND via
       zero-wrapping unit-triangular congruence M = U H U^T strict diagonal dominance
       (the exact certificate format replayable in Lean 4 without division!).
     - Verified on BOTH regular S^4 and an explicitly deformed S^4!
  4. R-18 Pi^0_1 Analytic Bounds (Lagarias n=1..60, Li off-line blowup, Mertens) &
     Chain A2 2-Loop Machacek-Vaughn Unification Window:
     - Lagarias H_n + exp(H_n) ln(H_n) > sigma(n) certified for every n = 2..60 (exact eq n=1);
     - Li off-line witness & Mertens identity certified in DyadicInterval;
     - Chain A2 1-loop exact AND 2-loop Machacek-Vaughn Picard-Lindelof order-6 interval
       Taylor + variational-ODE Krawczyk certification of M_PS, Lambda_NCG, and alpha_GUT^-1
       (incl. full continuum PDG +-1sigma interval alpha_s in [0.1171, 0.1189])!
"""

import sys
import time


# ==============================================================================
# 0. PURE-INTEGER EXACT UTILITIES (ZERO FLOAT, ZERO `math` MODULE)
# ==============================================================================

def isqrt_exact(n: int) -> int:
    """Pure-integer Newton square root with runtime postcondition s^2 <= n < (s+1)^2."""
    if n < 0:
        raise ValueError("isqrt_exact requires n >= 0")
    if n == 0:
        return 0
    x = 1 << ((n.bit_length() + 1) >> 1)
    while True:
        y = (x + n // x) >> 1
        if y >= x:
            assert x * x <= n < (x + 1) * (x + 1)
            return x
        x = y


def floor_div_pow2(m: int, s: int) -> int:
    """Exact floor(m / 2^s) for any integer m and s >= 0."""
    return m >> s if s > 0 else m


def ceil_div_pow2(m: int, s: int) -> int:
    """Exact ceil(m / 2^s) = -floor((-m) / 2^s) for any integer m and s >= 0."""
    return -((-m) >> s) if s > 0 else m


# ==============================================================================
# 1. EXACT ARBITRARY-PRECISION DYADIC RATIONALS `Dyadic(mant, exp) = mant * 2^exp`
# ==============================================================================

class Dyadic:
    __slots__ = ("mant", "exp")

    def __init__(self, mant: int, exp: int = 0):
        if mant == 0:
            self.mant = 0
            self.exp = 0
        else:
            # Canonical trailing-zero reduction: mant * 2^exp invariant
            tz = (mant & -mant).bit_length() - 1
            if tz > 0:
                mant >>= tz
                exp += tz
            self.mant = mant
            self.exp = exp

    def __repr__(self) -> str:
        return f"Dyadic({self.mant}, {self.exp})"

    def is_zero(self) -> bool:
        return self.mant == 0

    def sign(self) -> int:
        if self.mant > 0:
            return 1
        if self.mant < 0:
            return -1
        return 0

    def neg(self) -> "Dyadic":
        return Dyadic(-self.mant, self.exp)

    def abs(self) -> "Dyadic":
        return Dyadic(-self.mant if self.mant < 0 else self.mant, self.exp)

    def shift(self, k: int) -> "Dyadic":
        """Exact multiplication by 2^k."""
        if self.mant == 0:
            return D_ZERO
        return Dyadic(self.mant, self.exp + k)

    def msb_pos(self) -> int:
        """Exact floor(log2(|self|)) + 1 for self != 0: 2^(p-1) <= |self| < 2^p."""
        return (self.mant if self.mant > 0 else -self.mant).bit_length() + self.exp

    @staticmethod
    def cmp(a: "Dyadic", b: "Dyadic") -> int:
        sa, sb = a.sign(), b.sign()
        if sa != sb:
            return -1 if sa < sb else 1
        if sa == 0:
            return 0
        # Same sign: compare magnitude order first to avoid giant shifts
        pa, pb = a.msb_pos(), b.msb_pos()
        if pa != pb:
            mag_cmp = -1 if pa < pb else 1
            return mag_cmp if sa > 0 else -mag_cmp
        # Same bit-order: align exponents
        if a.exp >= b.exp:
            diff = a.exp - b.exp
            va = a.mant << diff
            vb = b.mant
        else:
            diff = b.exp - a.exp
            va = a.mant
            vb = b.mant << diff
        return -1 if va < vb else (1 if va > vb else 0)

    def __lt__(self, other: "Dyadic") -> bool:
        return Dyadic.cmp(self, other) < 0

    def __le__(self, other: "Dyadic") -> bool:
        return Dyadic.cmp(self, other) <= 0

    def __gt__(self, other: "Dyadic") -> bool:
        return Dyadic.cmp(self, other) > 0

    def __ge__(self, other: "Dyadic") -> bool:
        return Dyadic.cmp(self, other) >= 0

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Dyadic):
            return False
        return self.mant == other.mant and self.exp == other.exp

    def round_down(self, prec: int) -> "Dyadic":
        if self.mant == 0:
            return D_ZERO
        bl = (-self.mant if self.mant < 0 else self.mant).bit_length()
        if bl <= prec:
            return self
        s = bl - prec
        return Dyadic(floor_div_pow2(self.mant, s), self.exp + s)

    def round_up(self, prec: int) -> "Dyadic":
        if self.mant == 0:
            return D_ZERO
        bl = (-self.mant if self.mant < 0 else self.mant).bit_length()
        if bl <= prec:
            return self
        s = bl - prec
        return Dyadic(ceil_div_pow2(self.mant, s), self.exp + s)

    @staticmethod
    def add_directed(a: "Dyadic", b: "Dyadic", prec: int, up: bool) -> "Dyadic":
        if a.mant == 0:
            return b.round_up(prec) if up else b.round_down(prec)
        if b.mant == 0:
            return a.round_up(prec) if up else a.round_down(prec)
        # Ensure a.exp >= b.exp
        if a.exp < b.exp:
            a, b = b, a
        diff = a.exp - b.exp
        # Guard against huge exponent gap (e.g. 1 + 2^-10000)
        if diff <= prec + 64:
            res = Dyadic((a.mant << diff) + b.mant, b.exp)
            return res.round_up(prec) if up else res.round_down(prec)
        # Truncate b safely at e_cut = a.exp - (prec + 8)
        e_cut = a.exp - (prec + 8)
        s = e_cut - b.exp
        assert s > 0
        b_trunc = ceil_div_pow2(b.mant, s) if up else floor_div_pow2(b.mant, s)
        res = Dyadic((a.mant << (prec + 8)) + b_trunc, e_cut)
        return res.round_up(prec) if up else res.round_down(prec)

    @staticmethod
    def mul_directed(a: "Dyadic", b: "Dyadic", prec: int, up: bool) -> "Dyadic":
        if a.mant == 0 or b.mant == 0:
            return D_ZERO
        res = Dyadic(a.mant * b.mant, a.exp + b.exp)
        return res.round_up(prec) if up else res.round_down(prec)

    def to_decimal_str(self, digits: int = 12, up: bool = False) -> str:
        """100% pure-integer outward-rounded decimal string formatting (ZERO float!)."""
        scale = 10 ** digits
        scaled = self.mant * scale
        if self.exp >= 0:
            val = scaled << self.exp
        else:
            s = -self.exp
            val = ceil_div_pow2(scaled, s) if up else floor_div_pow2(scaled, s)
        neg = val < 0
        aval = -val if neg else val
        whole = aval // scale
        frac = aval % scale
        sign_str = "-" if neg else ""
        if digits == 0:
            return f"{sign_str}{whole}"
        return f"{sign_str}{whole}.{frac:0{digits}d}"


D_ZERO = Dyadic(0, 0)
D_ONE = Dyadic(1, 0)
D_NEG_ONE = Dyadic(-1, 0)


# ==============================================================================
# 2. CERTIFIED OUTWARD-ROUNDED DYADIC INTERVAL `DyadicInterval`
# ==============================================================================

DEFAULT_PREC = 160  # Default working precision (bits; ~48 decimal digits)


class DI:
    """Certified outward-rounded DyadicInterval [lo, hi] with invariant lo <= hi."""
    __slots__ = ("lo", "hi")

    def __init__(self, lo: Dyadic, hi: Dyadic):
        if lo > hi:
            raise AssertionError(f"Invalid DyadicInterval: {lo} > {hi}")
        self.lo = lo
        self.hi = hi

    @staticmethod
    def point(d: Dyadic) -> "DI":
        return DI(d, d)

    @staticmethod
    def from_int(n: int) -> "DI":
        d = Dyadic(n, 0)
        return DI(d, d)

    @staticmethod
    def from_ratio(p: int, q: int, prec: int = DEFAULT_PREC) -> "DI":
        if q == 0:
            raise ZeroDivisionError("Zero denominator")
        if q < 0:
            p, q = -p, -q
        if p == 0:
            return DI_ZERO
        # Shift so quotient has >= prec + 2 bits
        p_abs = -p if p < 0 else p
        r = max(0, q.bit_length() - p_abs.bit_length() + prec + 2)
        num = p << r
        # Python integer floor division `//` is exact Euclidean floor for q > 0!
        lo_m = num // q
        hi_m = -((-num) // q)
        lo = Dyadic(lo_m, -r).round_down(prec)
        hi = Dyadic(hi_m, -r).round_up(prec)
        return DI(lo, hi)

    @staticmethod
    def from_dec_str(s: str, prec: int = DEFAULT_PREC) -> "DI":
        """Parse exact decimal literal like '0.1180' or '91.1876' via pure int ratio."""
        s = s.strip()
        neg = False
        if s.startswith("-"):
            neg = True
            s = s[1:]
        elif s.startswith("+"):
            s = s[1:]
        if "." in s:
            whole, frac = s.split(".")
            p = int(whole + frac)
            q = 10 ** len(frac)
        else:
            p = int(s)
            q = 1
        if neg:
            p = -p
        return DI.from_ratio(p, q, prec)

    def round(self, prec: int) -> "DI":
        return DI(self.lo.round_down(prec), self.hi.round_up(prec))

    def neg(self) -> "DI":
        return DI(self.hi.neg(), self.lo.neg())

    def __neg__(self) -> "DI":
        return self.neg()

    def shift(self, k: int) -> "DI":
        return DI(self.lo.shift(k), self.hi.shift(k))

    def width(self, prec: int = DEFAULT_PREC) -> Dyadic:
        return Dyadic.add_directed(self.hi, self.lo.neg(), prec, up=True)

    def midpoint(self, prec: int = DEFAULT_PREC) -> Dyadic:
        # Any dyadic point in [lo, hi] (for Krawczyk center / bisection)
        s = Dyadic.add_directed(self.lo, self.hi, prec + 4, up=False).shift(-1)
        if s < self.lo:
            return self.lo
        if s > self.hi:
            return self.hi
        return s

    def abs_upper(self) -> Dyadic:
        a = self.lo.abs()
        b = self.hi.abs()
        return a if a >= b else b

    def abs_interval(self) -> "DI":
        if self.lo.mant >= 0:
            return self
        if self.hi.mant <= 0:
            return self.neg()
        return DI(D_ZERO, self.abs_upper())

    def contains_zero(self) -> bool:
        return self.lo.mant <= 0 <= self.hi.mant

    def strictly_pos(self) -> bool:
        return self.lo.mant > 0

    def strictly_neg(self) -> bool:
        return self.hi.mant < 0

    def contains(self, other: "DI") -> bool:
        return self.lo <= other.lo and other.hi <= self.hi

    def hull(self, other: "DI") -> "DI":
        lo = self.lo if self.lo <= other.lo else other.lo
        hi = self.hi if self.hi >= other.hi else other.hi
        return DI(lo, hi)

    def add(self, other: "DI", prec: int = DEFAULT_PREC) -> "DI":
        lo = Dyadic.add_directed(self.lo, other.lo, prec, up=False)
        hi = Dyadic.add_directed(self.hi, other.hi, prec, up=True)
        return DI(lo, hi)

    def sub(self, other: "DI", prec: int = DEFAULT_PREC) -> "DI":
        lo = Dyadic.add_directed(self.lo, other.hi.neg(), prec, up=False)
        hi = Dyadic.add_directed(self.hi, other.lo.neg(), prec, up=True)
        return DI(lo, hi)

    def mul(self, other: "DI", prec: int = DEFAULT_PREC) -> "DI":
        a, b, c, d = self.lo, self.hi, other.lo, other.hi
        # Fast sign-separated branches (identical to min/max of 4 corners, tighter work)
        if a.mant >= 0 and c.mant >= 0:
            return DI(Dyadic.mul_directed(a, c, prec, False), Dyadic.mul_directed(b, d, prec, True))
        if b.mant <= 0 and d.mant <= 0:
            return DI(Dyadic.mul_directed(b, d, prec, False), Dyadic.mul_directed(a, c, prec, True))
        if a.mant >= 0 and d.mant <= 0:
            return DI(Dyadic.mul_directed(b, c, prec, False), Dyadic.mul_directed(a, d, prec, True))
        if b.mant <= 0 and c.mant >= 0:
            return DI(Dyadic.mul_directed(a, d, prec, False), Dyadic.mul_directed(b, c, prec, True))
        # General 4-corner outward-rounded min/max (sound constructively by bilinear convexity!)
        p_lo = [
            Dyadic.mul_directed(a, c, prec, False),
            Dyadic.mul_directed(a, d, prec, False),
            Dyadic.mul_directed(b, c, prec, False),
            Dyadic.mul_directed(b, d, prec, False),
        ]
        p_hi = [
            Dyadic.mul_directed(a, c, prec, True),
            Dyadic.mul_directed(a, d, prec, True),
            Dyadic.mul_directed(b, c, prec, True),
            Dyadic.mul_directed(b, d, prec, True),
        ]
        lo = p_lo[0]
        for x in p_lo[1:]:
            if x < lo:
                lo = x
        hi = p_hi[0]
        for x in p_hi[1:]:
            if x > hi:
                hi = x
        return DI(lo, hi)

    def sqr(self, prec: int = DEFAULT_PREC) -> "DI":
        """Tighter exact squaring: x^2 >= 0 always when 0 in [lo, hi]."""
        if self.lo.mant >= 0:
            return DI(Dyadic.mul_directed(self.lo, self.lo, prec, False),
                      Dyadic.mul_directed(self.hi, self.hi, prec, True))
        if self.hi.mant <= 0:
            return DI(Dyadic.mul_directed(self.hi, self.hi, prec, False),
                      Dyadic.mul_directed(self.lo, self.lo, prec, True))
        m = self.abs_upper()
        return DI(D_ZERO, Dyadic.mul_directed(m, m, prec, True))

    def pow_nat(self, n: int, prec: int = DEFAULT_PREC) -> "DI":
        if n == 0:
            return DI_ONE
        if n == 1:
            return self
        if n == 2:
            return self.sqr(prec)
        # Monotonicity for odd n, symmetric >=0 for even n
        if n % 2 == 1:
            lo_i = DI.point(self.lo)
            hi_i = DI.point(self.hi)
            r_lo = DI_ONE
            r_hi = DI_ONE
            b_lo, b_hi = lo_i, hi_i
            k = n
            while k > 0:
                if k & 1:
                    r_lo = r_lo.mul(b_lo, prec)
                    r_hi = r_hi.mul(b_hi, prec)
                k >>= 1
                if k > 0:
                    b_lo = b_lo.mul(b_lo, prec)
                    b_hi = b_hi.mul(b_hi, prec)
            return DI(r_lo.lo, r_hi.hi)
        else:
            # Even n: power of |self|
            a = self.abs_interval()
            return a.pow_nat(n // 2, prec).sqr(prec)

    @staticmethod
    def _inv_pos_dyadic(d: Dyadic, prec: int) -> "DI":
        assert d.mant > 0
        r = d.mant.bit_length() + prec + 2
        num = 1 << r
        q_lo = num // d.mant
        q_hi = (num + d.mant - 1) // d.mant
        return DI(Dyadic(q_lo, -d.exp - r).round_down(prec),
                  Dyadic(q_hi, -d.exp - r).round_up(prec))

    def inv(self, prec: int = DEFAULT_PREC) -> "DI":
        if self.lo.mant > 0:
            lo = DI._inv_pos_dyadic(self.hi, prec).lo
            hi = DI._inv_pos_dyadic(self.lo, prec).hi
            return DI(lo, hi)
        if self.hi.mant < 0:
            return self.neg().inv(prec).neg()
        raise ZeroDivisionError(f"Division by interval containing 0: {self}")

    def div(self, other: "DI", prec: int = DEFAULT_PREC) -> "DI":
        return self.mul(other.inv(prec + 8), prec)

    @staticmethod
    def _sqrt_nonneg_dyadic(d: Dyadic, prec: int) -> "DI":
        if d.mant == 0:
            return DI_ZERO
        assert d.mant > 0
        bl = d.mant.bit_length()
        s_min = max(0, 2 * prec + 4 - bl)
        s = s_min if ((d.exp - s_min) & 1) == 0 else s_min + 1
        k = (d.exp - s) >> 1
        assert 2 * k + s == d.exp and s >= 0
        M = d.mant << s
        r = isqrt_exact(M)
        r_hi = r if r * r == M else r + 1
        return DI(Dyadic(r, k).round_down(prec), Dyadic(r_hi, k).round_up(prec))

    def sqrt(self, prec: int = DEFAULT_PREC) -> "DI":
        if self.lo.mant < 0:
            raise ValueError(f"sqrt of interval with negative endpoint: {self}")
        lo = DI._sqrt_nonneg_dyadic(self.lo, prec).lo
        hi = DI._sqrt_nonneg_dyadic(self.hi, prec).hi
        return DI(lo, hi)

    def fmt(self, digits: int = 12) -> str:
        return f"[{self.lo.to_decimal_str(digits, False)}, {self.hi.to_decimal_str(digits, True)}]"

    def __repr__(self) -> str:
        return f"DI{self.fmt(14)}"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, DI) and self.lo == other.lo and self.hi == other.hi

    # Convenient operator overloads at DEFAULT_PREC
    def __add__(self, other: "DI") -> "DI":
        return self.add(other, DEFAULT_PREC)

    def __sub__(self, other: "DI") -> "DI":
        return self.sub(other, DEFAULT_PREC)

    def __mul__(self, other: "DI") -> "DI":
        return self.mul(other, DEFAULT_PREC)

    def __truediv__(self, other: "DI") -> "DI":
        return self.div(other, DEFAULT_PREC)


DI_ZERO = DI(D_ZERO, D_ZERO)
DI_ONE = DI(D_ONE, D_ONE)


# ==============================================================================
# 3. CERTIFIED ELEMENTARY FUNCTIONS (`exp`, `log`, `pi`, `atan`, `acos`, `cos`)
# ==============================================================================

_CACHE_LN2: dict[int, DI] = {}
_CACHE_PI: dict[int, DI] = {}


def di_ln2(prec: int = DEFAULT_PREC) -> DI:
    if prec in _CACHE_LN2:
        return _CACHE_LN2[prec]
    wp = prec + 24
    # ln 2 = 2 * artanh(1/3) = 2 * sum_{j=0}^{N-1} 1 / ((2j+1) * 3^(2j+1)) + R_N
    # 0 <= R_N <= (9/4) / ((2N+1) * 3^(2N+1))
    s_lo = D_ZERO
    s_hi = D_ZERO
    pow3 = 3
    j = 0
    while True:
        denom = (2 * j + 1) * pow3
        term = DI.from_ratio(2, denom, wp)
        s_lo = Dyadic.add_directed(s_lo, term.lo, wp, False)
        s_hi = Dyadic.add_directed(s_hi, term.hi, wp, True)
        pow3 *= 9
        j += 1
        # Check certified remainder bound: 9 / (4 * (2j+1) * 3^(2j+1)) < 2^(-(wp - 6))
        if (4 * (2 * j + 1) * pow3) > (9 << (wp - 6)):
            rem_hi = DI.from_ratio(9, 4 * (2 * j + 1) * pow3, wp).hi
            s_hi = Dyadic.add_directed(s_hi, rem_hi, wp, True)
            break
    res = DI(s_lo.round_down(prec), s_hi.round_up(prec))
    _CACHE_LN2[prec] = res
    return res


def di_atan_inv_int(m: int, prec: int) -> DI:
    """Certified arctan(1/m) for integer m >= 2 via alternating Taylor series."""
    assert m >= 2
    wp = prec + 24
    s = DI_ZERO
    m2 = m * m
    pow_m = m
    j = 0
    while True:
        denom = (2 * j + 1) * pow_m
        term = DI.from_ratio(1, denom, wp)
        if j & 1:
            s = s.sub(term, wp)
        else:
            s = s.add(term, wp)
        pow_m *= m2
        j += 1
        # Exact alternating remainder: |R_j| <= 1 / ((2j+1) * m^(2j+1))
        next_denom = (2 * j + 1) * pow_m
        if next_denom > (1 << (wp - 6)):
            rem = DI.from_ratio(1, next_denom, wp).hi
            # Alternating series: if next term (j) is positive (j even), R_j in [0, rem]; else [-rem, 0]
            if j & 1:
                s = DI(Dyadic.add_directed(s.lo, rem.neg(), wp, False), s.hi)
            else:
                s = DI(s.lo, Dyadic.add_directed(s.hi, rem, wp, True))
            break
    return s.round(prec)


def di_pi(prec: int = DEFAULT_PREC) -> DI:
    if prec in _CACHE_PI:
        return _CACHE_PI[prec]
    wp = prec + 20
    # Machin's identity: pi = 16*atan(1/5) - 4*atan(1/239)
    a5 = di_atan_inv_int(5, wp).shift(4)
    a239 = di_atan_inv_int(239, wp).shift(2)
    res = a5.sub(a239, prec)
    _CACHE_PI[prec] = res
    return res


def _exp_point_nonneg(d: Dyadic, prec: int) -> DI:
    """Certified enclosure of exp(d) for exact Dyadic d >= 0."""
    if d.mant == 0:
        return DI_ONE
    assert d.mant > 0
    # Argument reduction: choose k >= 0 so r = d * 2^(-k) <= 1/4
    p = d.msb_pos()  # 2^(p-1) <= d < 2^p
    k = max(0, p + 2)
    r = d.shift(-k)
    assert r <= Dyadic(1, -2)
    wp = prec + k + 24
    r_i = DI.point(r)
    s = DI_ONE
    term = DI_ONE
    j = 1
    while True:
        term = term.mul(r_i, wp).div(DI.from_int(j), wp)
        s = s.add(term, wp)
        # Next term upper bound: term * r / (j+1); since 0 <= r <= 1/4, exp(xi) <= 2,
        # exact Lagrange remainder 0 <= R_j <= 2 * term_next <= 2 * (term * r / (j+1))
        next_term_hi = term.mul(r_i, wp).div(DI.from_int(j + 1), wp).hi
        rem_hi = next_term_hi.shift(1)
        if rem_hi < Dyadic(1, -(wp - 8)):
            s = DI(s.lo, Dyadic.add_directed(s.hi, rem_hi, wp, True))
            break
        j += 1
    # Square k times: (exp(r))^(2^k) = exp(d)
    for _ in range(k):
        s = s.sqr(wp)
    return s.round(prec)


def _exp_point(d: Dyadic, prec: int) -> DI:
    if d.mant == 0:
        return DI_ONE
    if d.mant > 0:
        return _exp_point_nonneg(d, prec)
    return _exp_point_nonneg(d.neg(), prec + 12).inv(prec)


def di_exp(I: DI, prec: int = DEFAULT_PREC) -> DI:
    """Certified exp(I) via monotonicity of exp."""
    if I.lo == I.hi:
        return _exp_point(I.lo, prec)
    lo = _exp_point(I.lo, prec).lo
    hi = _exp_point(I.hi, prec).hi
    return DI(lo, hi)


def _log_point_pos(d: Dyadic, prec: int) -> DI:
    """Certified enclosure of ln(d) for exact Dyadic d > 0 via artanh series."""
    assert d.mant > 0
    if d == D_ONE:
        return DI_ZERO
    wp = prec + 24
    # Normalize d = y * 2^k with y in [3/4, 3/2] => |t| = |(y-1)/(y+1)| <= 1/5
    bl = d.mant.bit_length()
    # y0 = d.mant * 2^(-(bl - 1)) in [1, 2)
    # Check if y0 >= 3/2 <=> 2 * d.mant >= 3 * 2^(bl - 1)
    if (d.mant << 1) >= (3 << (bl - 1)):
        k = d.exp + bl
    else:
        k = d.exp + bl - 1
    y = DI.point(d.shift(-k))
    t = y.sub(DI_ONE, wp).div(y.add(DI_ONE, wp), wp)
    t2 = t.sqr(wp)
    t_abs_hi = t.abs_upper()
    assert t_abs_hi <= Dyadic(1, -2)  # <= 1/4 (in fact <= 1/5)
    # ln(y) = 2 * sum_{j=0}^{N-1} t^(2j+1) / (2j+1) + R_N
    # |R_N| <= 2 * |t|^(2N+1) / ((2N+1) * (1 - t^2)) <= 4 * |t|^(2N+1) / (2N+1)
    s = DI_ZERO
    t_pow = t
    t_abs_pow = DI.point(t_abs_hi)
    t_abs_sq = t_abs_pow.sqr(wp)
    j = 0
    while True:
        denom = 2 * j + 1
        s = s.add(t_pow.div(DI.from_int(denom), wp), wp)
        t_pow = t_pow.mul(t2, wp)
        t_abs_pow = t_abs_pow.mul(t_abs_sq, wp)
        j += 1
        rem_hi = t_abs_pow.div(DI.from_int(2 * j + 1), wp).hi.shift(2)
        if rem_hi < Dyadic(1, -(wp - 8)):
            # s represents sum; multiply by 2 and add [-rem_hi, +rem_hi]
            s = s.shift(1)
            s = DI(Dyadic.add_directed(s.lo, rem_hi.neg(), wp, False),
                   Dyadic.add_directed(s.hi, rem_hi, wp, True))
            break
    if k != 0:
        s = s.add(DI.from_int(k).mul(di_ln2(wp), wp), wp)
    return s.round(prec)


def di_log(I: DI, prec: int = DEFAULT_PREC) -> DI:
    if I.lo.mant <= 0:
        raise ValueError(f"log of non-positive interval: {I}")
    if I.lo == I.hi:
        return _log_point_pos(I.lo, prec)
    lo = _log_point_pos(I.lo, prec).lo
    hi = _log_point_pos(I.hi, prec).hi
    return DI(lo, hi)


def _atan_small_interval(U: DI, prec: int) -> DI:
    """Certified arctan(U) for U subset [0, 1/4] via alternating Taylor series."""
    assert U.lo.mant >= 0 and U.hi <= Dyadic(1, -2)
    wp = prec + 20
    # Monotone increasing -> evaluate at endpoints for maximum tightness!
    def eval_pt(d: Dyadic) -> DI:
        if d.mant == 0:
            return DI_ZERO
        u = DI.point(d)
        u2 = u.sqr(wp)
        s = DI_ZERO
        upow = u
        j = 0
        while True:
            term = upow.div(DI.from_int(2 * j + 1), wp)
            s = s.sub(term, wp) if (j & 1) else s.add(term, wp)
            upow = upow.mul(u2, wp)
            j += 1
            rem_hi = upow.div(DI.from_int(2 * j + 1), wp).hi
            if rem_hi < Dyadic(1, -(wp - 8)):
                if j & 1:
                    s = DI(Dyadic.add_directed(s.lo, rem_hi.neg(), wp, False), s.hi)
                else:
                    s = DI(s.lo, Dyadic.add_directed(s.hi, rem_hi, wp, True))
                break
        return s

    if U.lo == U.hi:
        return eval_pt(U.lo).round(prec)
    return DI(eval_pt(U.lo).lo, eval_pt(U.hi).hi).round(prec)


def _atan_point(d: Dyadic, prec: int) -> DI:
    if d.mant == 0:
        return DI_ZERO
    if d.mant < 0:
        return _atan_point(d.neg(), prec).neg()
    wp = prec + 24
    # If d > 1, use atan(d) = pi/2 - atan(1/d)
    if d > D_ONE:
        inv_d = DI._inv_pos_dyadic(d, wp)
        # Apply 3 half-angle reductions: x -> x / (1 + sqrt(1 + x^2))
        u = inv_d
        for _ in range(3):
            u = u.div(DI_ONE.add(DI_ONE.add(u.sqr(wp), wp).sqrt(wp), wp), wp)
        at_inv = _atan_small_interval(u, wp).shift(3)
        return di_pi(wp).shift(-1).sub(at_inv, prec)
    u = DI.point(d)
    for _ in range(3):
        u = u.div(DI_ONE.add(DI_ONE.add(u.sqr(wp), wp).sqrt(wp), wp), wp)
    return _atan_small_interval(u, wp).shift(3).round(prec)


def di_atan(I: DI, prec: int = DEFAULT_PREC) -> DI:
    if I.lo == I.hi:
        return _atan_point(I.lo, prec)
    return DI(_atan_point(I.lo, prec).lo, _atan_point(I.hi, prec).hi)


def _acos_point(d: Dyadic, prec: int) -> DI:
    """Certified arccos(d) = pi/2 - arctan(d / sqrt(1 - d^2)) for |d| < 1."""
    assert D_NEG_ONE < d < D_ONE
    wp = prec + 24
    x = DI.point(d)
    arg = x.div(DI_ONE.sub(x.sqr(wp), wp).sqrt(wp), wp)
    return di_pi(wp).shift(-1).sub(di_atan(arg, wp), prec)


def di_acos(I: DI, prec: int = DEFAULT_PREC) -> DI:
    """Certified arccos(I) for I subset (-1, 1); arccos is strictly decreasing."""
    if not (D_NEG_ONE < I.lo and I.hi < D_ONE):
        raise ValueError(f"acos requires strict separation from +-1: {I}")
    if I.lo == I.hi:
        return _acos_point(I.lo, prec)
    lo = _acos_point(I.hi, prec).lo
    hi = _acos_point(I.lo, prec).hi
    return DI(lo, hi)


def di_cos_point(d: Dyadic, prec: int = DEFAULT_PREC) -> DI:
    """Certified cos(d) via binary angle halving + alternating Taylor series."""
    if d.mant == 0:
        return DI_ONE
    if d.mant < 0:
        d = d.neg()
    p = d.msb_pos()
    k = max(0, p + 2)
    r = DI.point(d.shift(-k))  # 0 < r <= 1/4
    wp = prec + 2 * k + 24
    r2 = r.sqr(wp)
    s = DI_ONE
    term = DI_ONE
    j = 1
    while True:
        term = term.mul(r2, wp).div(DI.from_int((2 * j - 1) * (2 * j)), wp)
        s = s.sub(term, wp) if (j & 1) else s.add(term, wp)
        j += 1
        rem_hi = term.mul(r2, wp).div(DI.from_int((2 * j - 1) * (2 * j)), wp).hi
        if rem_hi < Dyadic(1, -(wp - 8)):
            if j & 1:
                s = DI(Dyadic.add_directed(s.lo, rem_hi.neg(), wp, False), s.hi)
            else:
                s = DI(s.lo, Dyadic.add_directed(s.hi, rem_hi, wp, True))
            break
    # Angle doubling: cos(2 theta) = 2 cos^2(theta) - 1
    for _ in range(k):
        s = s.sqr(wp).shift(1).sub(DI_ONE, wp)
    return s.round(prec)


# ==============================================================================
# 4. AUTOMATIC ORDER-4 TAYLOR-JET INTERVAL ARITHMETIC & CERTIFIED SIMPSON QUADRATURE
# ==============================================================================

class Jet4:
    """Truncated Taylor series (c0, c1, c2, c3, c4) where ck = f^(k)(x) / k! over DI."""
    __slots__ = ("c", "prec")

    def __init__(self, c: tuple[DI, DI, DI, DI, DI], prec: int = DEFAULT_PREC):
        self.c = c
        self.prec = prec

    @staticmethod
    def var(x: DI, prec: int = DEFAULT_PREC) -> "Jet4":
        return Jet4((x, DI_ONE, DI_ZERO, DI_ZERO, DI_ZERO), prec)

    @staticmethod
    def const(v: DI, prec: int = DEFAULT_PREC) -> "Jet4":
        return Jet4((v, DI_ZERO, DI_ZERO, DI_ZERO, DI_ZERO), prec)

    def add(self, o: "Jet4") -> "Jet4":
        p = self.prec
        return Jet4(tuple(self.c[k].add(o.c[k], p) for k in range(5)), p)

    def sub(self, o: "Jet4") -> "Jet4":
        p = self.prec
        return Jet4(tuple(self.c[k].sub(o.c[k], p) for k in range(5)), p)

    def scale(self, s: DI) -> "Jet4":
        p = self.prec
        return Jet4(tuple(self.c[k].mul(s, p) for k in range(5)), p)

    def add_const(self, s: DI) -> "Jet4":
        p = self.prec
        return Jet4((self.c[0].add(s, p), self.c[1], self.c[2], self.c[3], self.c[4]), p)

    def mul(self, o: "Jet4") -> "Jet4":
        p = self.prec
        a, b = self.c, o.c
        out = []
        for k in range(5):
            acc = a[0].mul(b[k], p)
            for j in range(1, k + 1):
                acc = acc.add(a[j].mul(b[k - j], p), p)
            out.append(acc)
        return Jet4(tuple(out), p)

    def div(self, o: "Jet4") -> "Jet4":
        p = self.prec
        a, b = self.c, o.c
        inv_b0 = b[0].inv(p + 8)
        c = [a[0].mul(inv_b0, p)]
        for k in range(1, 5):
            acc = a[k]
            for j in range(1, k + 1):
                acc = acc.sub(b[j].mul(c[k - j], p), p)
            c.append(acc.mul(inv_b0, p))
        return Jet4(tuple(c), p)

    def sqrt(self) -> "Jet4":
        p = self.prec
        a = self.c
        c0 = a[0].sqrt(p)
        inv2c0 = c0.shift(1).inv(p + 8)
        c1 = a[1].mul(inv2c0, p)
        c2 = a[2].sub(c1.sqr(p), p).mul(inv2c0, p)
        c3 = a[3].sub(c1.mul(c2, p).shift(1), p).mul(inv2c0, p)
        c4 = a[4].sub(c1.mul(c3, p).shift(1), p).sub(c2.sqr(p), p).mul(inv2c0, p)
        return Jet4((c0, c1, c2, c3, c4), p)

    def exp(self) -> "Jet4":
        p = self.prec
        a = self.c
        c = [di_exp(a[0], p)]
        for k in range(1, 5):
            acc = DI_ZERO
            for j in range(1, k + 1):
                acc = acc.add(DI.from_int(j).mul(a[j], p).mul(c[k - j], p), p)
            c.append(acc.div(DI.from_int(k), p))
        return Jet4(tuple(c), p)

    def log(self) -> "Jet4":
        p = self.prec
        a = self.c
        inv_a0 = a[0].inv(p + 8)
        c = [di_log(a[0], p)]
        for k in range(1, 5):
            acc = DI_ZERO
            for j in range(1, k):
                acc = acc.add(DI.from_int(j).mul(c[j], p).mul(a[k - j], p), p)
            term = a[k].sub(acc.div(DI.from_int(k), p), p)
            c.append(term.mul(inv_a0, p))
        return Jet4(tuple(c), p)


def integrate_simpson_certified(
    point_fn,
    jet4_fn,
    a: Dyadic,
    b: Dyadic,
    n_panels: int,
    prec: int = DEFAULT_PREC,
) -> DI:
    """
    Constructive Peano-kernel certified composite Simpson quadrature on [a, b]:
      int_{x_k}^{x_{k+1}} f(x) dx in (h/6)(f(x_k) + 4 f(m_k) + f(x_{k+1})) - (h^5/120) * c4([x_k, x_{k+1}])
    where c4 = f^(4)/24 from exact Jet4 automatic differentiation.
    ZERO classical MVT, ZERO float64!
    """
    assert a < b and n_panels >= 1
    # Use exact dyadic grid when n_panels is a power of 2 and (b-a) is exact dyadic
    # For arbitrary n_panels, construct exact dyadic partition points x_0=a < x_1 < ... < x_n=b
    # (note: partition points only need to be monotone exact dyadics, NOT exactly equal width!)
    span = Dyadic.add_directed(b, a.neg(), prec + 16, up=False)
    xs: list[Dyadic] = [a]
    for k in range(1, n_panels):
        frac = DI.from_ratio(k, n_panels, prec + 16).lo
        xk = Dyadic.add_directed(a, Dyadic.mul_directed(span, frac, prec + 16, False), prec + 16, False)
        assert xs[-1] < xk < b
        xs.append(xk)
    xs.append(b)

    f_nodes = [point_fn(DI.point(xk), prec) for xk in xs]
    inv6 = DI.from_ratio(1, 6, prec + 8)
    inv120 = DI.from_ratio(1, 120, prec + 8)
    total = DI_ZERO
    for k in range(n_panels):
        xk, xk1 = xs[k], xs[k + 1]
        # Exact panel width h_k = xk1 - xk (use exact arithmetic by aligning)
        h_i = DI.point(xk1).sub(DI.point(xk), prec)
        # Note: Simpson requires exact midpoint (xk + xk1)/2! Compute exact midpoint:
        # Since xk and xk1 are dyadics, (xk + xk1)/2 is an EXACT dyadic!
        if xk.exp >= xk1.exp:
            mk_exact = Dyadic((xk.mant << (xk.exp - xk1.exp)) + xk1.mant, xk1.exp - 1)
        else:
            mk_exact = Dyadic(xk.mant + (xk1.mant << (xk1.exp - xk.exp)), xk.exp - 1)
        assert xk < mk_exact < xk1
        fm = point_fn(DI.point(mk_exact), prec)
        simp = h_i.mul(inv6, prec).mul(
            f_nodes[k].add(fm.shift(2), prec).add(f_nodes[k + 1], prec), prec
        )
        c4 = jet4_fn(Jet4.var(DI(xk, xk1), prec)).c[4]
        h5 = h_i.pow_nat(5, prec)
        rem = h5.mul(inv120, prec).mul(c4, prec)
        total = total.add(simp.sub(rem, prec), prec)
    return total


# ==============================================================================
# 5. CONSTRUCTIVE KRAWCZYK ROOT CERTIFIER (EXISTENCE + UNIQUENESS IN CReal!)
# ==============================================================================

def certify_root_krawczyk(
    f_val_fn,
    f_and_df_fn,
    a: Dyadic,
    b: Dyadic,
    target_bits: int = 100,
    prec: int = DEFAULT_PREC,
):
    """
    1. Certified interval bisection from opposite-sign endpoints [a, b] to width <= 2^(-target_bits);
    2. Constructive Krawczyk self-contraction verification on I = [c-r, c+r]:
       - Strict sign separation at endpoints: F([lo,lo]) and F([hi,hi]) strictly opposite signs;
       - Strict slope separation: 0 not in F'(I);
       - Contraction factor q = max|1 - Y * F'(I)| < 1 strictly;
       - Self-enclosure: |Y * F([c,c])| + q * r < r strictly!
    Feeds directly into `creal_banach_fixed_point` (R-14D in ConstructiveR.lean, 0 Classical.choice).
    """
    fa = f_val_fn(DI.point(a), prec)
    fb = f_val_fn(DI.point(b), prec)
    assert (fa.strictly_pos() and fb.strictly_neg()) or (fa.strictly_neg() and fb.strictly_pos()), (
        f"Endpoints do not certify strict sign change: f(a)={fa}, f(b)={fb}"
    )
    inc = fa.strictly_neg()  # True if f(a) < 0 < f(b)

    lo, hi = a, b
    fl_cur, fh_cur = fa, fb
    for it in range(target_bits + 20):
        w = Dyadic.add_directed(hi, lo.neg(), prec, True)
        if w <= Dyadic(1, -target_bits):
            break
        # Safeguarded secant + bisection (5x fewer quadrature evaluations, identical rigor!)
        mid = None
        if it % 3 != 2:
            y0 = fl_cur.midpoint(prec)
            y1 = fh_cur.midpoint(prec)
            dy = Dyadic.add_directed(y1, y0.neg(), prec, False)
            if dy.mant != 0:
                frac = DI.point(y0.neg()).div(DI.point(dy), 64).midpoint(64)
                if Dyadic(1, -3) < frac < Dyadic(7, -3):
                    cand = Dyadic.add_directed(
                        lo, Dyadic.mul_directed(w, frac, prec, False), prec, False
                    ).round_down(target_bits + 12)
                    if lo < cand < hi:
                        mid = cand
        if mid is None:
            if lo.exp >= hi.exp:
                mid = Dyadic((lo.mant << (lo.exp - hi.exp)) + hi.mant, hi.exp - 1)
            else:
                mid = Dyadic(lo.mant + (hi.mant << (hi.exp - lo.exp)), lo.exp - 1)
        fm = f_val_fn(DI.point(mid), prec)
        if fm.strictly_neg():
            if inc:
                lo, fl_cur = mid, fm
            else:
                hi, fh_cur = mid, fm
        elif fm.strictly_pos():
            if inc:
                hi, fh_cur = mid, fm
            else:
                lo, fl_cur = mid, fm
        else:
            # Midpoint straddles 0 (e.g. secant hit close to root within quadrature width!):
            # Shrink lo up toward mid and hi down toward mid independently before Krawczyk!
            l_hi = mid
            for _ in range(16):
                if Dyadic.add_directed(l_hi, lo.neg(), prec, True) <= Dyadic(1, -target_bits):
                    break
                m_l = Dyadic.add_directed(lo, l_hi, prec, False).shift(-1)
                fm_l = f_val_fn(DI.point(m_l), prec)
                if (inc and fm_l.strictly_neg()) or ((not inc) and fm_l.strictly_pos()):
                    lo = m_l
                else:
                    l_hi = m_l
            r_lo = mid
            for _ in range(16):
                if Dyadic.add_directed(hi, r_lo.neg(), prec, True) <= Dyadic(1, -target_bits):
                    break
                m_r = Dyadic.add_directed(r_lo, hi, prec, False).shift(-1)
                fm_r = f_val_fn(DI.point(m_r), prec)
                if (inc and fm_r.strictly_pos()) or ((not inc) and fm_r.strictly_neg()):
                    hi = m_r
                else:
                    r_lo = m_r
            break

    # Slightly inflate bracket by 4x if midpoint hit zero cleanly so Krawczyk has room
    if lo.exp >= hi.exp:
        c = Dyadic((lo.mant << (lo.exp - hi.exp)) + hi.mant, hi.exp - 1)
    else:
        c = Dyadic(lo.mant + (hi.mant << (hi.exp - lo.exp)), lo.exp - 1)
    r = Dyadic.add_directed(hi, lo.neg(), prec, True).shift(-1)
    # Round c to compact dyadic and ensure [c-r, c+r] contains [lo, hi]
    c = c.round_down(target_bits + 16)
    r1 = Dyadic.add_directed(hi, c.neg(), prec, True)
    r2 = Dyadic.add_directed(c, lo.neg(), prec, True)
    r = (r1 if r1 >= r2 else r2).round_up(32)
    # Ensure r >= 2^(-target_bits - 4)
    r_min = Dyadic(1, -(target_bits + 4))
    if r < r_min:
        r = r_min

    # Inflate slightly if needed until Krawczyk succeeds (usually succeeds on try 0)
    for _ in range(10):
        I_lo = Dyadic.add_directed(c, r.neg(), prec, False)
        I_hi = Dyadic.add_directed(c, r, prec, True)
        I_box = DI(I_lo, I_hi)
        fc, dfc = f_and_df_fn(DI.point(c), prec)
        _, dfI = f_and_df_fn(I_box, prec)
        assert not dfI.contains_zero(), f"Derivative enclosure contains 0 on {I_box}: {dfI}"
        Y_d = dfc.inv(prec).midpoint(prec).round_down(64)
        Y_i = DI.point(Y_d)
        q_int = DI_ONE.sub(Y_i.mul(dfI, prec), prec)
        q_bound = q_int.abs_upper()
        yfc_abs = Y_i.mul(fc, prec).abs_upper()
        k_rad = Dyadic.add_directed(yfc_abs, Dyadic.mul_directed(q_bound, r, prec, True), prec, True)
        if q_bound < D_ONE and k_rad < r:
            fl = f_val_fn(DI.point(I_lo), prec)
            fh = f_val_fn(DI.point(I_hi), prec)
            assert (fl.strictly_pos() and fh.strictly_neg()) or (fl.strictly_neg() and fh.strictly_pos())
            return {
                "box": I_box,
                "center": c,
                "radius": r,
                "Y": Y_d,
                "q_contr": q_bound,
                "k_rad": k_rad,
                "df_box": dfI,
                "f_lo": fl,
                "f_hi": fh,
            }
        r = r.shift(1)
    raise AssertionError(f"Krawczyk certification failed near {c}")


# ==============================================================================
# TARGET 1: SUPER-F-40 & V12.1.B SPECTRAL-ACTION GHOST ENCLOSURES
# ==============================================================================

def run_target1_spectral_action() -> dict:
    print("=" * 88)
    print("TARGET 1: Super-F-40 & V12.1.B Spectral-Action Ghost Enclosures (100% Integer Dyadics)")
    print("=" * 88)
    prec = 144
    checks = 0
    pi_i = di_pi(prec)
    pi2_i = pi_i.sqr(prec)

    # --- 1A. Sharp cutoff Theta(1 - u) ---
    c_96pi2 = DI.from_int(96).mul(pi2_i, prec)
    c_3_10 = DI.from_ratio(3, 10, prec)

    def d2_sharp_ir(q: DI, p: int = prec) -> DI:
        q2 = q.sqr(p)
        return q2.div(c_96pi2, p).mul(DI_ONE.sub(c_3_10.mul(q2, p), p), p)

    def d2_sharp_ir_and_df(q: DI, p: int = prec) -> tuple[DI, DI]:
        # f(q) = (1/(96 pi^2)) (q^2 - (3/10) q^4), f'(q) = (1/(96 pi^2)) (2 q - (6/5) q^3)
        q2 = q.sqr(p)
        val = q2.div(c_96pi2, p).mul(DI_ONE.sub(c_3_10.mul(q2, p), p), p)
        df = q.shift(1).sub(DI.from_ratio(6, 5, p).mul(q.mul(q2, p), p), p).div(c_96pi2, p)
        return val, df

    v_q1 = d2_sharp_ir(DI_ONE, prec)
    v_q2 = d2_sharp_ir(DI.from_int(2), prec)
    assert v_q1.strictly_pos(), f"Expected Delta_2^Theta(1) > 0, got {v_q1}"
    assert v_q2.strictly_neg(), f"Expected Delta_2^Theta(2) < 0, got {v_q2}"
    checks += 2

    # Krawczyk certificate around q_* = sqrt(10/3)
    k_sharp = certify_root_krawczyk(d2_sharp_ir, d2_sharp_ir_and_df, Dyadic(1, 0), Dyadic(2, 0), target_bits=100, prec=prec)
    qstar_ref = DI.from_ratio(10, 3, prec).sqrt(prec)
    # Verify exact root box lies strictly inside [1.82574185835, 1.82574185836] AND intersects sqrt(10/3)
    b_lo = DI.from_dec_str("1.82574185835", prec).lo
    b_hi = DI.from_dec_str("1.82574185836", prec).hi
    assert b_lo < k_sharp["box"].lo and k_sharp["box"].hi < b_hi
    assert k_sharp["box"].lo <= qstar_ref.hi and qstar_ref.lo <= k_sharp["box"].hi
    checks += 2

    # Certified zero sum rule for sharp cutoff via desingularized substitution u = 1 - t^2 (t in [0, 1]):
    # I_[0, 2] = int_0^2 Delta_2^Theta(q)/q^2 dq = +1/(80 pi^2)
    def sharp_ir_over_q2_pt(q: DI, p: int = prec) -> DI:
        return DI_ONE.sub(c_3_10.mul(q.sqr(p), p), p).div(c_96pi2, p)

    def sharp_ir_over_q2_jet(q: Jet4) -> Jet4:
        p = q.prec
        q2 = q.mul(q)
        return Jet4.const(DI_ONE, p).sub(q2.scale(DI.from_ratio(3, 10, p))).scale(c_96pi2.inv(p + 8))

    I_sh_ir = integrate_simpson_certified(sharp_ir_over_q2_pt, sharp_ir_over_q2_jet, D_ZERO, Dyadic(2, 0), 8, prec)
    exact_1_80pi2 = DI_ONE.div(DI.from_int(80).mul(pi2_i, prec), prec)
    assert I_sh_ir.lo <= exact_1_80pi2.hi and exact_1_80pi2.lo <= I_sh_ir.hi
    checks += 1

    # UV branch: int_2^inf Delta_2^Theta(q)/q^2 dq = int_0^1 t * Delta_2^Theta(2 / (1 - t^2)) dt
    # With u = 1 - t^2, v = 2 - t^2 in [1, 2], (1 - u^2)^(3/2) = t^3 * v^(3/2):
    # Delta_2^Theta(2/u) = (-45 + 60 u^2 - 16 u^6) / (120 pi^2 * ((6 + 4 u^2) t^3 v^(3/2) + (6 - 5 u^2)))
    c_120pi2 = DI.from_int(120).mul(pi2_i, prec)

    def sharp_uv_t_pt(t: DI, p: int = prec) -> DI:
        t2 = t.sqr(p)
        u = DI_ONE.sub(t2, p)
        u2 = u.sqr(p)
        u6 = u2.mul(u2.sqr(p), p)
        v = DI.from_int(2).sub(t2, p)
        v32 = v.mul(v.sqrt(p), p)
        t3 = t.mul(t2, p)
        num = t.mul(DI.from_int(-45).add(DI.from_int(60).mul(u2, p), p).sub(DI.from_int(16).mul(u6, p), p), p)
        den = c_120pi2.mul(
            DI.from_int(6).add(u2.shift(2), p).mul(t3, p).mul(v32, p).add(
                DI.from_int(6).sub(DI.from_int(5).mul(u2, p), p), p
            ), p
        )
        return num.div(den, p)

    def sharp_uv_t_jet(t: Jet4) -> Jet4:
        p = t.prec
        t2 = t.mul(t)
        u = Jet4.const(DI_ONE, p).sub(t2)
        u2 = u.mul(u)
        u6 = u2.mul(u2.mul(u2))
        v = Jet4.const(DI.from_int(2), p).sub(t2)
        v32 = v.mul(v.sqrt())
        t3 = t.mul(t2)
        num = t.mul(
            Jet4.const(DI.from_int(-45), p).add(u2.scale(DI.from_int(60))).sub(u6.scale(DI.from_int(16)))
        )
        den_in = (Jet4.const(DI.from_int(6), p).add(u2.scale(DI.from_int(4)))).mul(t3).mul(v32).add(
            Jet4.const(DI.from_int(6), p).sub(u2.scale(DI.from_int(5)))
        )
        return num.div(den_in.scale(c_120pi2))

    I_sh_uv = integrate_simpson_certified(sharp_uv_t_pt, sharp_uv_t_jet, D_ZERO, D_ONE, 64, prec)
    I_sh_tot = I_sh_ir.add(I_sh_uv, prec)
    assert I_sh_tot.contains_zero() and I_sh_tot.width(prec) < Dyadic(1, -30)
    checks += 1
    print(f"  [1A] Sharp cutoff Theta(1-u):")
    print(f"       Delta_2(1)     in {v_q1.fmt(14)}  (> 0 CERTIFIED [T])")
    print(f"       Delta_2(2)     in {v_q2.fmt(14)}  (< 0 CERTIFIED [T])")
    print(f"       Krawczyk root  q_* in {k_sharp['box'].fmt(24)}  (q_contr <= {k_sharp['q_contr'].to_decimal_str(6, True)} < 1 [T])")
    print(f"       Sum rule int_0^inf = I_IR + I_UV in {I_sh_tot.fmt(14)}  (0 in I, width <= {I_sh_tot.width(prec).to_decimal_str(12, True)} [T])")

    # --- 1B. Closed-form exponential chi(u) = e^-u & signed (1 - a u) e^-u (Pure Dirac & Mixed SM/MSSM/CCvS) ---
    # Using symmetry x <-> 1 - x: int_0^1 g(x(1-x) q^2) dx = 2 * int_0^{1/2} g(x(1-x) q^2) dx
    # For species mix (n0, nw, np, ng): effective coefficients (A, B, D):
    #   scalar: (1, 0, 0), weyl: (-1, 4, 0), proca: (-3, 0, 16), gauge: (-4, 0, 16)
    c_64pi2 = DI.from_int(64).mul(pi2_i, prec)
    c_half = Dyadic(1, -1)

    def mix_coeffs(n0: int, nw: int, np_: int, ng: int) -> tuple[int, int, int]:
        return (n0 - nw - 3 * np_ - 4 * ng, 4 * nw, 16 * np_ + 16 * ng)

    def make_exp_mixed_eval(n0: int, nw: int, np_: int, ng: int, a_c: DI | None = None, n_panels: int = 16):
        A_i, B_i, D_i = mix_coeffs(n0, nw, np_, ng)
        # Integrand in s = x(1-x) q^2:
        # For chi = e^-u (a_c is None):
        #   F(s) = -2 A (e^-s - 1) + B s e^-s - D s^2 e^-s
        #   F'(s) = (2 A + B) e^-s - (B + 2 D) s e^-s + D s^2 e^-s
        #   wait: check d/ds [-2A(e^-s - 1) + B s e^-s - D s^2 e^-s]:
        #         = 2 A e^-s + B (1 - s) e^-s - D (2s - s^2) e^-s
        #         = (2 A + B) e^-s - (B + 2 D) s e^-s + D s^2 e^-s!
        # For signed chi = (1 - a_c u) e^-u:
        #   h1(s)  = -2 A (e^-s - 1) + B s e^-s - D s^2 e^-s
        #   hp1(s) =  4 A (e^-s - 1) + (2 A - B) s e^-s - B s^2 e^-s + D s^3 e^-s
        #   F(s) = h1(s) + a_c * hp1(s)
        #        = (-2 A + 4 a_c A) (e^-s - 1) + (B + a_c (2A - B)) s e^-s + (-D - a_c B) s^2 e^-s + (a_c D) s^3 e^-s
        #   Write F(s) = c_e * (e^-s - 1) + (p1 s + p2 s^2 + p3 s^3) e^-s
        #   Then F'(s) = (p1 - c_e) e^-s + (2 p2 - p1) s e^-s + (3 p3 - p2) s^2 e^-s - p3 s^3 e^-s!
        if a_c is None:
            c_e = DI.from_int(-2 * A_i)
            p1 = DI.from_int(B_i)
            p2 = DI.from_int(-D_i)
            p3 = DI_ZERO
        else:
            c_e = DI.from_int(-2 * A_i).add(a_c.mul(DI.from_int(4 * A_i), prec), prec)
            p1 = DI.from_int(B_i).add(a_c.mul(DI.from_int(2 * A_i - B_i), prec), prec)
            p2 = DI.from_int(-D_i).sub(a_c.mul(DI.from_int(B_i), prec), prec)
            p3 = a_c.mul(DI.from_int(D_i), prec)
        dp0 = p1.sub(c_e, prec)
        dp1 = p2.shift(1).sub(p1, prec)
        dp2 = DI.from_int(3).mul(p3, prec).sub(p2, prec)
        dp3 = p3.neg()

        def eval_val(q: DI, p: int = prec) -> DI:
            q2 = q.sqr(p)
            def ig_pt(x: DI, pp: int) -> DI:
                s = x.mul(DI_ONE.sub(x, pp), pp).mul(q2, pp)
                ex = di_exp(s.neg(), pp)
                poly = p1.add(s.mul(p2.add(s.mul(p3, pp), pp), pp), pp).mul(s, pp)
                return c_e.mul(ex.sub(DI_ONE, pp), pp).add(poly.mul(ex, pp), pp)

            def ig_jet(x: Jet4) -> Jet4:
                pp = x.prec
                s = x.mul(Jet4.const(DI_ONE, pp).sub(x)).scale(q2)
                ex = s.scale(DI.from_int(-1)).exp()
                poly = s.mul(
                    Jet4.const(p1, pp).add(s.mul(Jet4.const(p2, pp).add(s.scale(p3))))
                )
                return ex.add_const(DI.from_int(-1)).scale(c_e).add(poly.mul(ex))

            # 2 * int_0^{1/2} (...) / (64 pi^2) = int_0^{1/2} (...) / (32 pi^2)
            # For large q (q >= 4), grade [0, 1/2] at x = 1/16 to resolve the e^{-q^2 x} boundary layer cleanly!
            if q.hi >= Dyadic(4, 0):
                x_cut = Dyadic(1, -4)  # exact 1/16
                p_bl = max(n_panels, 20)
                v1 = integrate_simpson_certified(ig_pt, ig_jet, D_ZERO, x_cut, p_bl, p)
                v2 = integrate_simpson_certified(ig_pt, ig_jet, x_cut, c_half, p_bl, p)
                tot_int = v1.add(v2, p)
            else:
                tot_int = integrate_simpson_certified(ig_pt, ig_jet, D_ZERO, c_half, n_panels, p)
            return tot_int.div(DI.from_int(32).mul(pi2_i, p), p)

        def eval_val_and_df(q: DI, p: int = prec) -> tuple[DI, DI]:
            val = eval_val(q, p)
            q2 = q.sqr(p)
            # d/dq F(x(1-x) q^2) = 2 q x(1-x) F'(x(1-x) q^2)
            def df_pt(x: DI, pp: int) -> DI:
                w = x.mul(DI_ONE.sub(x, pp), pp)
                s = w.mul(q2, pp)
                ex = di_exp(s.neg(), pp)
                fp = dp0.add(s.mul(dp1.add(s.mul(dp2.add(s.mul(dp3, pp), pp), pp), pp), pp), pp).mul(ex, pp)
                return w.mul(fp, pp)

            def df_jet(x: Jet4) -> Jet4:
                pp = x.prec
                w = x.mul(Jet4.const(DI_ONE, pp).sub(x))
                s = w.scale(q2)
                ex = s.scale(DI.from_int(-1)).exp()
                fp = (
                    Jet4.const(dp0, pp)
                    .add(s.mul(Jet4.const(dp1, pp).add(s.mul(Jet4.const(dp2, pp).add(s.scale(dp3))))))
                ).mul(ex)
                return w.mul(fp)

            if q.hi >= Dyadic(4, 0):
                x_cut = Dyadic(1, -4)
                p_bl = max(n_panels, 20)
                df_int = integrate_simpson_certified(df_pt, df_jet, D_ZERO, x_cut, p_bl, p).add(
                    integrate_simpson_certified(df_pt, df_jet, x_cut, c_half, p_bl, p), p
                )
            else:
                df_int = integrate_simpson_certified(df_pt, df_jet, D_ZERO, c_half, n_panels, p)
            df = q.shift(1).mul(df_int, p).div(DI.from_int(32).mul(pi2_i, p), p)
            return val, df

        return eval_val, eval_val_and_df

    # 1B(i). Pure Dirac chi(u) = e^-u:
    f_exp_d, fdf_exp_d = make_exp_mixed_eval(0, 2, 0, 0, None, n_panels=12)
    k_exp_d = certify_root_krawczyk(f_exp_d, fdf_exp_d, Dyadic(1, 0), Dyadic(4, 0), target_bits=60, prec=prec)
    # Certified zero sum rule for Dirac e^-u:
    # Exact tail theorem: int_Q^inf Delta_2^{e^-u}(q)/q^2 dq = -(1/(16 pi^2 Q)) * int_0^1 (1 - e^{-x(1-x)Q^2}) dx
    # And int_0^Q Delta_2^{e^-u}(q)/q^2 dq = +(1/(16 pi^2 Q)) * int_0^1 (1 - e^{-x(1-x)Q^2}) dx (exact FTC)!
    # Cross-check by certified quadrature on [0, Q=4] + exact certified tail on [4, inf):
    Q_cut = Dyadic(4, 0)
    # Integrand of int_0^Q: Delta_2^{e^-u}(q)/q^2 = (1/(16 pi^2)) * int_0^1 x(1-x) * (e^-s - 1 + 2 s e^-s)/s dx
    # Even simpler: swap order (exact Fubini) OR integrate directly in q on [1/2, 4] + [0, 1/2] using Taylor-desingularized psi(s):
    # Exact analytic Fubini antiderivative at Q=4 gives tail T(Q) = -(1/(16 pi^2 Q)) * 2 * int_0^{1/2} (1 - e^{-x(1-x) Q^2}) dx:
    def tail_exp_pt(x: DI, p: int) -> DI:
        s = x.mul(DI_ONE.sub(x, p), p).mul(DI.from_int(16), p)
        return DI_ONE.sub(di_exp(s.neg(), p), p)
    def tail_exp_jet(x: Jet4) -> Jet4:
        p = x.prec
        s = x.mul(Jet4.const(DI_ONE, p).sub(x)).scale(DI.from_int(16))
        return Jet4.const(DI_ONE, p).sub(s.scale(DI.from_int(-1)).exp())
    tail_factor = integrate_simpson_certified(tail_exp_pt, tail_exp_jet, D_ZERO, c_half, 32, prec).shift(1)
    I_exp_tail = tail_factor.neg().div(DI.from_int(16 * 4).mul(pi2_i, prec), prec)

    # Exact convergent alternating Beta-function series for int_0^Q Delta_2^{e^-u, Dirac}(q)/q^2 dq:
    #   int_0^1 [x(1-x)]^{m+1} dx = ((m+1)!)^2 / (2m+3)!, and (2m+1) cancels with int_0^Q q^{2m} dq = Q^{2m+1}/(2m+1),
    #   yielding I_{[0, Q]} = (1/(16 pi^2)) * sum_{m=0}^inf (-1)^m * (m+1)! / (2m+3)! * Q^{2m+1}!
    def dirac_exp_int_0_Q(Q_int: int, p: int = prec) -> DI:
        assert Q_int >= 1
        s = DI_ZERO
        fact_m1 = 1  # (m+1)!
        fact_2m3 = 6  # (2m+3)!
        q_pow = Q_int  # Q^(2m+1)
        q2 = Q_int * Q_int
        m = 0
        while True:
            term = DI.from_ratio(fact_m1 * q_pow, fact_2m3, p)
            s = s.sub(term, p) if (m & 1) else s.add(term, p)
            m += 1
            fact_m1 *= (m + 1)
            fact_2m3 *= (2 * m + 2) * (2 * m + 3)
            q_pow *= q2
            rem_hi = DI.from_ratio(fact_m1 * q_pow, fact_2m3, p).hi
            # Exact monotone-decreasing alternating-tail condition:
            # b_{m+1}/b_m = Q^2 / (2 * (2m + 5)) < 1, strictly decreasing in m!
            if q2 < 2 * (2 * m + 5) and rem_hi < Dyadic(1, -(p - 10)):
                if m & 1:
                    s = DI(Dyadic.add_directed(s.lo, rem_hi.neg(), p, False), s.hi)
                else:
                    s = DI(s.lo, Dyadic.add_directed(s.hi, rem_hi, p, True))
                break
        return s.div(DI.from_int(16).mul(pi2_i, p), p)

    I_exp_ir = dirac_exp_int_0_Q(4, prec)
    I_exp_tot = I_exp_ir.add(I_exp_tail, prec)
    assert I_exp_tot.contains_zero() and I_exp_tot.width(prec) < Dyadic(1, -30)
    checks += 2

    # 1B(ii). Signed cutoff chi(u) = (1 - 0.6 u) e^-u (Pure Dirac): positive in IR & UV, negative dip, TWO ghost zeros + sum rule!
    a06 = DI.from_ratio(3, 5, prec)
    f_s06_d, fdf_s06_d = make_exp_mixed_eval(0, 2, 0, 0, a06, n_panels=14)
    v_s06_ir = f_s06_d(DI.from_ratio(1, 2, prec), prec)
    v_s06_dip = f_s06_d(DI.from_int(3), prec)
    v_s06_uv = f_s06_d(DI.from_int(8), prec)
    assert v_s06_ir.strictly_pos() and v_s06_dip.strictly_neg() and v_s06_uv.strictly_pos()
    k_s06_1 = certify_root_krawczyk(f_s06_d, fdf_s06_d, Dyadic(1, -1), Dyadic(3, 0), target_bits=40, prec=prec)
    k_s06_2 = certify_root_krawczyk(f_s06_d, fdf_s06_d, Dyadic(3, 0), Dyadic(8, 0), target_bits=40, prec=prec)
    # Certified zero sum rule for signed (1 - a_c u) e^-u (a_c >= 0) via exact antiderivative Phi_{a_c}(q, x):
    def dirac_signed_int_0_Q(Q_int: int, a_num: int, a_den: int, p: int = prec) -> DI:
        assert Q_int >= 1 and a_num >= 0 and a_den > 0
        s = DI_ZERO
        fact_m1 = 1
        fact_2m3 = 6
        q_pow = Q_int
        q2 = Q_int * Q_int
        m = 0
        while True:
            c_num = a_den + a_num * (m - 1)
            term = DI.from_ratio(c_num * fact_m1 * q_pow, a_den * fact_2m3, p)
            s = s.sub(term, p) if (m & 1) else s.add(term, p)
            m += 1
            fact_m1 *= (m + 1)
            fact_2m3 *= (2 * m + 2) * (2 * m + 3)
            q_pow *= q2
            c_next = a_den + a_num * (m - 1)
            c_next2 = a_den + a_num * m
            rem_hi = DI.from_ratio(abs(c_next) * fact_m1 * q_pow, a_den * fact_2m3, p).hi
            # For a_c >= 0 and m >= 1: c_next > 0 and both (c_{k+1}/c_k) and Q^2/(2*(2k+5)) are
            # non-increasing in k, so certifying b_{m+1}/b_m < 1 certifies strict monotone decay for ALL k >= m!
            if (
                m >= 6
                and c_next > 0
                and c_next2 * q2 < c_next * 2 * (2 * m + 5)
                and rem_hi < Dyadic(1, -(p - 10))
            ):
                if m & 1:
                    s = DI(Dyadic.add_directed(s.lo, rem_hi.neg(), p, False), s.hi)
                else:
                    s = DI(s.lo, Dyadic.add_directed(s.hi, rem_hi, p, True))
                break
        return s.div(DI.from_int(16).mul(pi2_i, p), p)

    c_1m2a = DI.from_ratio(-1, 5, prec)
    def tail_s06_pt(x: DI, p: int) -> DI:
        s = x.mul(DI_ONE.sub(x, p), p).mul(DI.from_int(16), p)
        ex = di_exp(s.neg(), p)
        return c_1m2a.mul(DI_ONE.sub(ex, p), p).add(a06.mul(s, p).mul(ex, p), p)
    def tail_s06_jet(x: Jet4) -> Jet4:
        p = x.prec
        s = x.mul(Jet4.const(DI_ONE, p).sub(x)).scale(DI.from_int(16))
        ex = s.scale(DI.from_int(-1)).exp()
        return Jet4.const(DI_ONE, p).sub(ex).scale(c_1m2a).add(s.mul(ex).scale(a06))
    I_s06_ir = dirac_signed_int_0_Q(4, 3, 5, prec)
    I_s06_tail = integrate_simpson_certified(tail_s06_pt, tail_s06_jet, D_ZERO, c_half, 32, prec).shift(1).neg().div(
        DI.from_int(64).mul(pi2_i, prec), prec
    )
    I_s06_tot = I_s06_ir.add(I_s06_tail, prec)
    assert I_s06_tot.contains_zero() and I_s06_tot.width(prec) < Dyadic(1, -28)
    checks += 6

    # 1B(iii). Mixed SM, MSSM, CCvS Euclidean ghost zero enclosures (V12.1.B):
    mixed_specs = [
        ("SM (e^-u)",                 4,   45, 0, 12, None, Dyadic(1, -4),  Dyadic(1, 0),  10),
        ("MSSM xi=0 (e^-u)",          98,  61, 0, 12, None, Dyadic(1, 0),   Dyadic(4, 0),  16),
        ("PS Chain A2 (e^-u)",        68,  48, 0, 21, None, Dyadic(1, -2),  Dyadic(2, 0),  12),
        ("CCvS-FULL-R z1 (e^-u)",     140, 48, 0, 21, None, Dyadic(1, 0),   Dyadic(3, 0),  16),
        ("CCvS-FULL-R z2 (e^-u)",     140, 48, 0, 21, None, Dyadic(5, 0),   Dyadic(10, 0), 20),
        ("CCvS-FULL-C z1 (1-0.6u)",   200, 48, 0, 21, a06,  Dyadic(1, -1),  Dyadic(2, 0),  16),
        ("CCvS-FULL-C z2 (1-0.6u)",   200, 48, 0, 21, a06,  Dyadic(2, 0),   Dyadic(5, 0),  20),
        ("CCvS-FULL-C z3 (1-0.6u)",   200, 48, 0, 21, a06,  Dyadic(5, 0),   Dyadic(10, 0), 20),
    ]
    mixed_certs = {}
    for label, n0, nw, np_, ng, ac, qa, qb, npan in mixed_specs:
        fe, fdfe = make_exp_mixed_eval(n0, nw, np_, ng, ac, n_panels=npan)
        cert = certify_root_krawczyk(fe, fdfe, qa, qb, target_bits=48, prec=prec)
        mixed_certs[label] = cert
        checks += 1

    print(f"  [1B] Smooth e^-u & Signed (1 - 0.6 u) e^-u (Pure Dirac):")
    print(f"       Dirac e^-u:          q_*  in {k_exp_d['box'].fmt(16)} (q_contr <= {k_exp_d['q_contr'].to_decimal_str(6, True)}) [T]")
    print(f"       Dirac e^-u sum rule: I_[0,4] + I_[4,inf) in {I_exp_tot.fmt(14)} (0 in I [T])")
    print(f"       Dirac (1-0.6u)e^-u:  q1_* in {k_s06_1['box'].fmt(14)} (q_contr <= {k_s06_1['q_contr'].to_decimal_str(6, True)}), "
          f"q2_* in {k_s06_2['box'].fmt(14)} (q_contr <= {k_s06_2['q_contr'].to_decimal_str(6, True)}) [T]")
    print(f"       Signed sum rule:     I_[0,4] + I_[4,inf) in {I_s06_tot.fmt(14)} (0 in I [T])")
    print(f"  [1C] V12.1.B Mixed SM / MSSM / CCvS Certified Euclidean Ghost Zeros:")
    for label, cert in mixed_certs.items():
        print(f"       {label:26s}: q_* in {cert['box'].fmt(14)} (q_contr <= {cert['q_contr'].to_decimal_str(5, True)}) [T]")

    return {"checks": checks, "k_sharp": k_sharp, "k_exp_d": k_exp_d, "mixed_certs": mixed_certs}


# ==============================================================================
# TARGET 2: F-36B KALLEN-LEHMANN SPECTRAL DENSITY NEGATIVITY (PV4 & PV6_esc)
# ==============================================================================

def run_target2_kallen_lehmann() -> dict:
    print("\n" + "=" * 88)
    print("TARGET 2: F-36B Kallen-Lehmann Spectral Density Negativity (PV4 & PV6_esc)")
    print("=" * 88)
    prec = 144
    checks = 0
    pi_i = di_pi(prec)
    c_480pi = DI.from_int(480).mul(pi_i, prec)

    pv4 = [
        (DI.from_int(1), 1),
        (DI.from_int(-2), 2),
        (DI.from_ratio(9, 7, prec), 3),
        (DI.from_ratio(-2, 7, prec), 4),
    ]
    pv6_esc = [
        (DI.from_int(1), 1),
        (DI.from_int(-3), 2),
        (DI.from_ratio(827, 256, prec), 4),
        (DI.from_ratio(-1507, 1024, prec), 8),
        (DI.from_ratio(129, 512, prec), 16),
        (DI.from_ratio(-11, 1024, prec), 32),
    ]

    def rho2_eval(s: DI, pv, p: int = prec) -> DI:
        # Strictly evaluate on intervals that do not cross any threshold 4 m_i^2
        tot = DI_ZERO
        s2 = s.sqr(p)
        for ci, m in pv:
            thr = Dyadic(4 * m * m, 0)
            if s.lo > thr:
                m2 = DI.from_int(m * m)
                z = DI.from_int(4 * m * m).div(s, p)
                b = DI_ONE.sub(z, p).sqrt(p)
                b3 = b.mul(b.sqr(p), p)
                fac = DI.from_int(3).add(DI.from_int(8 * m * m).div(s, p), p)
                tot = tot.add(ci.mul(b3, p).mul(fac, p), p)
            else:
                assert s.hi <= thr, f"Interval {s} straddles threshold 4 m^2 = {4*m*m}"
        return tot.mul(s2, p).div(c_480pi, p)

    def rho2_and_df_16_36(s: DI, pv, p: int = prec) -> tuple[DI, DI]:
        # On (16, 36), ONLY i=0 (m=1) and i=1 (m=2) are active; differentiate via Jet4!
        assert Dyadic(16, 0) < s.lo and s.hi < Dyadic(36, 0), f"s={s} outside (16, 36) branch"
        # Term: c_i * s^2/(480 pi) * (1 - 4m^2/s)^(3/2) * (3 + 8m^2/s)
        #     = c_i / (480 pi) * (s - 4 m^2)^(3/2) * (3 s + 8 m^2) / sqrt(s)
        sj = Jet4.var(s, p)
        tot = Jet4.const(DI_ZERO, p)
        for ci, m in pv[:2]:
            d4 = sj.sub(Jet4.const(DI.from_int(4 * m * m), p))
            term = d4.mul(d4.sqrt()).mul(sj.scale(DI.from_int(3)).add_const(DI.from_int(8 * m * m))).div(sj.sqrt())
            tot = tot.add(term.scale(ci))
        tot = tot.scale(c_480pi.inv(p + 8))
        return tot.c[0], tot.c[1]

    # Concrete certified signs for PV4 (thresholds 4, 16, 36, 64)
    pv4_s5 = rho2_eval(DI.from_int(5), pv4)
    pv4_s20 = rho2_eval(DI.from_int(20), pv4)
    pv4_s32 = rho2_eval(DI.from_int(32), pv4)
    pv4_s36 = rho2_eval(DI.from_int(36), pv4)
    pv4_s50 = rho2_eval(DI.from_int(50), pv4)
    assert pv4_s5.strictly_pos() and pv4_s20.strictly_pos()
    assert pv4_s32.strictly_neg() and pv4_s36.strictly_neg() and pv4_s50.strictly_neg()
    checks += 5

    k_pv4 = certify_root_krawczyk(
        lambda s, p: rho2_eval(s, pv4, p),
        lambda s, p: rho2_and_df_16_36(s, pv4, p),
        Dyadic(20, 0), Dyadic(32, 0), target_bits=100, prec=prec,
    )
    checks += 1

    # Concrete certified signs for PV6_esc (thresholds 4, 16, 64, 256, 1024, 4096)
    pv6_s5 = rho2_eval(DI.from_int(5), pv6_esc)
    pv6_s20 = rho2_eval(DI.from_int(20), pv6_esc)
    pv6_s25 = rho2_eval(DI.from_int(25), pv6_esc)
    pv6_s30 = rho2_eval(DI.from_int(30), pv6_esc)
    pv6_s50 = rho2_eval(DI.from_int(50), pv6_esc)
    assert pv6_s5.strictly_pos() and pv6_s20.strictly_pos()
    assert pv6_s25.strictly_neg() and pv6_s30.strictly_neg() and pv6_s50.strictly_neg()
    checks += 5

    k_pv6 = certify_root_krawczyk(
        lambda s, p: rho2_eval(s, pv6_esc, p),
        lambda s, p: rho2_and_df_16_36(s, pv6_esc, p),
        Dyadic(20, 0), Dyadic(25, 0), target_bits=100, prec=prec,
    )
    checks += 1

    print(f"  [2A] PV4:     rho_2(5)  in {pv4_s5.fmt(12)} (>0), rho_2(32) in {pv4_s32.fmt(12)} (<0), rho_2(36) in {pv4_s36.fmt(12)} (<0) [T]")
    print(f"                Krawczyk zero crossing s_*^PV4 in {k_pv4['box'].fmt(24)} (q_contr <= {k_pv4['q_contr'].to_decimal_str(6, True)}) [T]")
    print(f"  [2B] PV6_esc: rho_2(5)  in {pv6_s5.fmt(12)} (>0), rho_2(25) in {pv6_s25.fmt(12)} (<0), rho_2(30) in {pv6_s30.fmt(12)} (<0) [T]")
    print(f"                Krawczyk zero crossing s_*^PV6 in {k_pv6['box'].fmt(24)} (q_contr <= {k_pv6['q_contr'].to_decimal_str(6, True)}) [T]")

    return {"checks": checks, "k_pv4": k_pv4, "k_pv6": k_pv6}


# ==============================================================================
# TARGET 3: 4D DEFORMED S^4 REGGE-SCHLAFLI HESSIAN INERTIA (10 NEG / 30 POS)
#           EXACT ANALYTICAL HESSIAN + INTERVAL LDL^T + U H U^T CONGRUENCE!
# ==============================================================================

def _invert_6x6_di(M: list[list[DI]], prec: int) -> list[list[DI]]:
    """Exact Gauss-Jordan inversion of a 6x6 symmetric matrix in DI with partial pivoting."""
    n = 6
    A = [[M[i][j] for j in range(n)] + [DI_ONE if i == j else DI_ZERO for j in range(n)] for i in range(n)]
    for col in range(n):
        # Choose pivot row with largest |lo/hi| strictly avoiding 0
        piv = -1
        best = D_ZERO
        for r in range(col, n):
            if not A[r][col].contains_zero():
                m_lo = A[r][col].lo.abs()
                m_hi = A[r][col].hi.abs()
                m_min = m_lo if m_lo <= m_hi else m_hi
                if m_min > best:
                    best = m_min
                    piv = r
        assert piv != -1, f"Singular 6x6 Cayley-Menger matrix at col {col}"
        if piv != col:
            A[col], A[piv] = A[piv], A[col]
        inv_p = A[col][col].inv(prec + 8)
        for j in range(col, 2 * n):
            A[col][j] = A[col][j].mul(inv_p, prec)
        for r in range(n):
            if r != col:
                fac = A[r][col]
                if not (fac.lo.mant == 0 and fac.hi.mant == 0):
                    for j in range(col, 2 * n):
                        A[r][j] = A[r][j].sub(fac.mul(A[col][j], prec), prec)
    return [[A[i][n + j] for j in range(n)] for i in range(n)]


def run_target3_s4_regge_hessian_inertia() -> dict:
    print("\n" + "=" * 88)
    print("TARGET 3: 4D S^4 (partial beta_5) Analytical Regge Hessian Inertia (ZERO float / ZERO eigvalsh!)")
    print("=" * 88)
    prec = 256  # 256-bit precision (~77 digits) kills 40x40 wrapping completely!
    checks = 0
    pi2 = di_pi(prec).shift(1)

    # Build partial beta_5 = S^4: 10V, 40E, 80T, 80Tet, 32 4-simplices
    edges_s4 = [(u, v) for u in range(10) for v in range(u + 1, 10) if u // 2 != v // 2]
    edge_idx = {e: idx for idx, e in enumerate(edges_s4)}
    tris_s4 = [
        (2 * a + sa, 2 * b + sb, 2 * c + sc)
        for a in range(5) for b in range(a + 1, 5) for c in range(b + 1, 5)
        for sa in (0, 1) for sb in (0, 1) for sc in (0, 1)
    ]
    tri_idx = {t: idx for idx, t in enumerate(tris_s4)}
    simplices4 = [
        (s0, 2 + s1, 4 + s2, 6 + s3, 8 + s4)
        for s0 in (0, 1) for s1 in (0, 1) for s2 in (0, 1) for s3 in (0, 1) for s4 in (0, 1)
    ]
    assert len(edges_s4) == 40 and len(tris_s4) == 80 and len(simplices4) == 32

    def analytical_hessian_neg_SR(L: list[DI], p: int = prec) -> tuple[DI, list[list[DI]]]:
        """
        EXACT analytical 40x40 Hessian H_{ef} = d^2(-S_R) / (dL_e dL_f) in DI!
        By the 4D Schlafli identity:
          g_e = -sum_{t sup e} (dA_t/dL_e) * eps_t
          H_{ef} = -sum_{t sup e,f} (d^2 A_t / (dL_e dL_f)) * eps_t
                   + sum_{sig sup e,f} sum_{t sub sig, t sup e} (dA_t/dL_e) * (d theta_{sig,t} / dL_f)
        ZERO finite-difference truncation error!
        """
        # 1. Precompute triangle areas, first derivs dA/dL_e, and second derivs d^2 A / (dL_e dL_f)
        areas: list[DI] = []
        tri_dA: list[dict[int, DI]] = []
        tri_d2A: list[dict[tuple[int, int], DI]] = []
        inv8 = DI.from_ratio(1, 8, p)
        inv4 = DI.from_ratio(1, 4, p)
        for t in tris_s4:
            es = (edge_idx[(t[0], t[1])], edge_idx[(t[0], t[2])], edge_idx[(t[1], t[2])])
            ls = [L[e] for e in es]
            l2 = [x.sqr(p) for x in ls]
            # 16 A^2 = 2(a^2 b^2 + b^2 c^2 + c^2 a^2) - (a^4 + b^4 + c^4)
            s_pair = l2[0].mul(l2[1], p).add(l2[1].mul(l2[2], p), p).add(l2[2].mul(l2[0], p), p).shift(1)
            s_4 = l2[0].sqr(p).add(l2[1].sqr(p), p).add(l2[2].sqr(p), p)
            a16_sq = s_pair.sub(s_4, p)
            assert a16_sq.strictly_pos()
            A = a16_sq.sqrt(p).shift(-2)
            invA = A.inv(p + 8)
            areas.append(A)
            # q_i = l_j^2 + l_k^2 - l_i^2
            qs = [
                l2[1].add(l2[2], p).sub(l2[0], p),
                l2[0].add(l2[2], p).sub(l2[1], p),
                l2[0].add(l2[1], p).sub(l2[2], p),
            ]
            dA_loc = [ls[i].mul(qs[i], p).mul(invA, p).mul(inv8, p) for i in range(3)]
            tri_dA.append({es[i]: dA_loc[i] for i in range(3)})
            d2_dict: dict[tuple[int, int], DI] = {}
            for i in range(3):
                # d^2 A / da^2 = (q_a - 2 a^2)/(8 A) - (dA/da)^2 / A
                val_ii = qs[i].sub(l2[i].shift(1), p).mul(invA, p).mul(inv8, p).sub(
                    dA_loc[i].sqr(p).mul(invA, p), p
                )
                d2_dict[(es[i], es[i])] = val_ii
                for j in range(i + 1, 3):
                    # d^2 A / (da db) = a b / (4 A) - (dA/da)(dA/db)/A
                    val_ij = ls[i].mul(ls[j], p).mul(invA, p).mul(inv4, p).sub(
                        dA_loc[i].mul(dA_loc[j], p).mul(invA, p), p
                    )
                    d2_dict[(es[i], es[j])] = val_ij
                    d2_dict[(es[j], es[i])] = val_ij
            tri_d2A.append(d2_dict)

        # 2. Loop over all 32 4-simplices: Cayley-Menger inverse W = M^-1, dihedral angles & exact d(theta)/dL_f
        theta_sum = [DI_ZERO for _ in range(80)]
        H = [[DI_ZERO for _ in range(40)] for _ in range(40)]
        for sig in simplices4:
            # Build 6x6 Cayley-Menger matrix M
            M = [[DI_ZERO for _ in range(6)] for _ in range(6)]
            for i in range(5):
                M[0][i + 1] = DI_ONE
                M[i + 1][0] = DI_ONE
            sig_edges: list[tuple[int, int, int]] = []  # (local_u, local_v, global_e)
            for i in range(5):
                for j in range(i + 1, 5):
                    e = edge_idx[(sig[i], sig[j])]
                    sig_edges.append((i, j, e))
                    l2 = L[e].sqr(p)
                    M[i + 1][j + 1] = l2
                    M[j + 1][i + 1] = l2
            W = _invert_6x6_di(M, p)

            # Diagonal entries P_i = -W[i+1][i+1] > 0
            P = [W[i + 1][i + 1].neg() for i in range(5)]
            for pi_val in P:
                assert pi_val.strictly_pos()
            sqrtP = [pi_val.sqrt(p) for pi_val in P]

            # Precompute hinge cosines, angles, and 1/sin(theta) for all 10 hinges (i < j) in sig
            hinges: list[tuple[int, int, int, DI, DI, DI]] = []  # (i, j, tid, c_ij, inv_sqrtPiPj, neg_inv_sin)
            for i in range(5):
                for j in range(i + 1, 5):
                    h_verts = tuple(sig[m] for m in range(5) if m != i and m != j)
                    tid = tri_idx[h_verts]
                    inv_sp = sqrtP[i].mul(sqrtP[j], p).inv(p + 8)
                    c_ij = W[i + 1][j + 1].mul(inv_sp, p)
                    th = di_acos(c_ij, p)
                    theta_sum[tid] = theta_sum[tid].add(th, p)
                    sin_th = DI_ONE.sub(c_ij.sqr(p), p).sqrt(p)
                    neg_inv_sin = sin_th.inv(p + 8).neg()
                    hinges.append((i, j, tid, c_ij, inv_sp, neg_inv_sin))

            # For each edge f = (u, v) in sig: dW/dL_f = -2 L_f (W[:, u+1] W[v+1, :] + W[:, v+1] W[u+1, :])
            for u, v, f_idx in sig_edges:
                m2Lf = L[f_idx].shift(1).neg()
                # Compute needed entries of dW/dL_f:
                # dW[a+1, b+1] = -2 L_f * (W[a+1, u+1]*W[v+1, b+1] + W[a+1, v+1]*W[u+1, b+1])
                dW_diag_ratio = []
                for a in range(5):
                    dWaa = m2Lf.mul(W[a + 1][u + 1].mul(W[v + 1][a + 1], p).shift(1), p)
                    # dWaa / Waa
                    dW_diag_ratio.append(dWaa.div(W[a + 1][a + 1], p))
                for i, j, tid, c_ij, inv_sp, neg_inv_sin in hinges:
                    dWij = m2Lf.mul(
                        W[i + 1][u + 1].mul(W[v + 1][j + 1], p).add(
                            W[i + 1][v + 1].mul(W[u + 1][j + 1], p), p
                        ), p
                    )
                    # dc_ij / dL_f = inv_sp * dWij - (1/2) * c_ij * (dWii/Wii + dWjj/Wjj)
                    dc_df = inv_sp.mul(dWij, p).sub(
                        c_ij.mul(dW_diag_ratio[i].add(dW_diag_ratio[j], p), p).shift(-1), p
                    )
                    dth_df = neg_inv_sin.mul(dc_df, p)
                    # Accumulate into H[e][f] for the 3 edges e of hinge triangle tid
                    for e_idx, dA_de in tri_dA[tid].items():
                        H[e_idx][f_idx] = H[e_idx][f_idx].add(dA_de.mul(dth_df, p), p)

        # 3. Deficit angles eps_t = 2 pi - theta_sum[t], S_R = sum A_t eps_t, and -sum (d^2 A_t) eps_t term
        eps = [pi2.sub(theta_sum[tid], p) for tid in range(80)]
        S_R = DI_ZERO
        for tid in range(80):
            S_R = S_R.add(areas[tid].mul(eps[tid], p), p)
            neg_eps = eps[tid].neg()
            for (e_idx, f_idx), d2val in tri_d2A[tid].items():
                H[e_idx][f_idx] = H[e_idx][f_idx].add(neg_eps.mul(d2val, p), p)

        # Verify Schlafli symmetry: H[i][j] intersects H[j][i] for every pair (i, j)!
        for i in range(40):
            for j in range(i + 1, 40):
                assert H[i][j].lo <= H[j][i].hi and H[j][i].lo <= H[i][j].hi, (
                    f"Schlafli symmetry failure at ({i},{j}): {H[i][j]} vs {H[j][i]}"
                )
                # Tighten by exact intersection (since true H_{ij} == H_{ji}!)
                lo_inter = H[i][j].lo if H[i][j].lo >= H[j][i].lo else H[j][i].lo
                hi_inter = H[i][j].hi if H[i][j].hi <= H[j][i].hi else H[j][i].hi
                sym_ij = DI(lo_inter, hi_inter)
                H[i][j] = sym_ij
                H[j][i] = sym_ij
        return S_R, H

    def certify_inertia_ldlt(H: list[list[DI]], p: int = prec):
        """
        Method A: Direct Interval LDL^T Sylvester Law of Inertia (with exact point L_mid extraction for Method B!).
        """
        n = len(H)
        A = [[H[i][j] for j in range(n)] for i in range(n)]
        L_int = [[DI_ONE if i == j else DI_ZERO for j in range(n)] for i in range(n)]
        pivots: list[DI] = []
        for k in range(n):
            dk = A[k][k]
            assert not dk.contains_zero(), f"Pivot {k} contains 0: {dk}"
            pivots.append(dk)
            inv_dk = dk.inv(p + 8)
            for i in range(k + 1, n):
                lik = A[i][k].mul(inv_dk, p)
                L_int[i][k] = lik
                # Diagonal update: A[i][i] - A[i][k]^2 / dk
                A[i][i] = A[i][i].sub(A[i][k].sqr(p).mul(inv_dk, p), p)
                for j in range(i + 1, n):
                    val = A[i][j].sub(lik.mul(A[j][k], p), p)
                    A[i][j] = val
                    A[j][i] = val
        n_neg = sum(1 for d in pivots if d.strictly_neg())
        n_pos = sum(1 for d in pivots if d.strictly_pos())
        assert n_neg + n_pos == n
        min_gap = min(min(d.lo.abs(), d.hi.abs()) for d in pivots)
        max_wid = max(d.width(p) for d in pivots)
        return n_neg, n_pos, pivots, L_int, min_gap, max_wid

    def certify_inertia_congruence_sdd(H: list[list[DI]], L_int: list[list[DI]], cert_bits: int = 40, p: int = 128):
        """
        Method B (Zero-Wrapping Lean 4 Replay Certificate!):
        Extract an exact unit lower-triangular dyadic matrix U = round(L_mid^{-1}, cert_bits)
        (with diagonal entries EXACTLY 1, so det(U) = 1 unconditionally!).
        Compute M = U * H * U^T in DI (pure add+mul, ZERO division!) and certify
        strict diagonal dominance: |M_{ii}|_lo > sum_{j != i} |M_{ij}|_hi for EVERY i = 0..39!
        """
        n = len(H)
        # Invert midpoint unit lower-triangular L_mid by forward substitution in exact dyadics
        L_mid = [[D_ONE if i == j else (L_int[i][j].midpoint(cert_bits + 16) if i > j else D_ZERO) for j in range(n)] for i in range(n)]
        U = [[D_ONE if i == j else D_ZERO for j in range(n)] for i in range(n)]
        for i in range(1, n):
            for j in range(i):
                # U[i][j] = -sum_{k=j}^{i-1} L_mid[i][k] * U[k][j]
                acc = D_ZERO
                for k in range(j, i):
                    prod = Dyadic.mul_directed(L_mid[i][k], U[k][j], cert_bits + 16, False)
                    acc = Dyadic.add_directed(acc, prod, cert_bits + 16, False)
                U[i][j] = acc.neg().round_down(cert_bits)

        # Round H to precision p and compute M = U * H * U^T in DI (pure add+mul!)
        H_r = [[H[i][j].round(p) for j in range(n)] for i in range(n)]
        # T = U * H_r (exploiting lower-triangularity of U: k <= i)
        T = [[DI_ZERO for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                acc = H_r[i][j]  # k = i since U[i][i] = 1
                for k in range(i):
                    if U[i][k].mant != 0:
                        acc = acc.add(DI.point(U[i][k]).mul(H_r[k][j], p), p)
                T[i][j] = acc
        # M = T * U^T (exploiting lower-triangularity of U: k <= j)
        M = [[DI_ZERO for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                acc = T[i][j]  # k = j since U[j][j] = 1
                for k in range(j):
                    if U[j][k].mant != 0:
                        acc = acc.add(T[i][k].mul(DI.point(U[j][k]), p), p)
                M[i][j] = acc
                M[j][i] = acc

        # Check strict diagonal dominance on ALL 40 rows!
        n_neg = 0
        n_pos = 0
        min_margin = None
        for i in range(n):
            d_i = M[i][i]
            assert not d_i.contains_zero(), f"Congruence diagonal M[{i},{i}] contains 0: {d_i}"
            if d_i.strictly_neg():
                n_neg += 1
                diag_lo = d_i.hi.neg()  # > 0, lower bound on |M_ii|
            else:
                n_pos += 1
                diag_lo = d_i.lo  # > 0, lower bound on |M_ii|
            off_sum = D_ZERO
            for j in range(n):
                if j != i:
                    off_sum = Dyadic.add_directed(off_sum, M[i][j].abs_upper(), p, True)
            margin = Dyadic.add_directed(diag_lo, off_sum.neg(), p, False)
            assert margin.mant > 0, f"Row {i} failed SDD: |M_ii|_lo={diag_lo} <= off_sum={off_sum}"
            if min_margin is None or margin < min_margin:
                min_margin = margin
        return n_neg, n_pos, min_margin

    # --- 3A. Regular S^4 (L_e = 1 for all 40 edges) ---
    L_reg = [DI_ONE for _ in range(40)]
    S_reg, H_reg = analytical_hessian_neg_SR(L_reg, prec)
    # Cross-check exact S_reg = 80 * (sqrt(3)/4) * (2 pi - 4 acos(1/4))
    S_reg_ref = DI.from_int(20).mul(DI.from_int(3).sqrt(prec), prec).mul(
        pi2.sub(di_acos(DI.point(Dyadic(1, -2)), prec).shift(2), prec), prec
    )
    assert S_reg.lo <= S_reg_ref.hi and S_reg_ref.lo <= S_reg.hi
    nn_reg_a, np_reg_a, piv_reg, L_reg_int, gap_reg, wid_reg = certify_inertia_ldlt(H_reg, prec)
    assert (nn_reg_a, np_reg_a) == (10, 30)
    nn_reg_b, np_reg_b, mrg_reg = certify_inertia_congruence_sdd(H_reg, L_reg_int, cert_bits=40, p=128)
    assert (nn_reg_b, np_reg_b) == (10, 30)
    # Ultra-compact 16-bit and 12-bit Lean 4 replay certificate tests!
    nn_reg_16, np_reg_16, mrg_reg_16 = certify_inertia_congruence_sdd(H_reg, L_reg_int, cert_bits=16, p=64)
    assert (nn_reg_16, np_reg_16) == (10, 30)
    nn_reg_12, np_reg_12, mrg_reg_12 = certify_inertia_congruence_sdd(H_reg, L_reg_int, cert_bits=12, p=64)
    assert (nn_reg_12, np_reg_12) == (10, 30)
    checks += 5

    # --- 3B. Explicitly Deformed S^4 (deterministic non-symmetric exact dyadic edge lengths!) ---
    # L_def[k] = 1 + ((19 * ((k+1)*7 % 19 - 9) + 13 * ((k+1)*11 % 13 - 6)) / 2^12)  (asymmetric exact dyadics!)
    L_def_dyad = [
        Dyadic(4096 + 19 * (((k + 1) * 7) % 19 - 9) + 13 * (((k + 1) * 11) % 13 - 6), -12)
        for k in range(40)
    ]
    L_def = [DI.point(d) for d in L_def_dyad]
    S_def, H_def = analytical_hessian_neg_SR(L_def, prec)
    nn_def_a, np_def_a, piv_def, L_def_int, gap_def, wid_def = certify_inertia_ldlt(H_def, prec)
    assert (nn_def_a, np_def_a) == (10, 30)
    nn_def_b, np_def_b, mrg_def = certify_inertia_congruence_sdd(H_def, L_def_int, cert_bits=40, p=128)
    assert (nn_def_b, np_def_b) == (10, 30)
    nn_def_16, np_def_16, mrg_def_16 = certify_inertia_congruence_sdd(H_def, L_def_int, cert_bits=16, p=64)
    assert (nn_def_16, np_def_16) == (10, 30)
    nn_def_12, np_def_12, mrg_def_12 = certify_inertia_congruence_sdd(H_def, L_def_int, cert_bits=12, p=64)
    assert (nn_def_12, np_def_12) == (10, 30)
    checks += 5

    print(f"  [3A] Regular S^4 (L_e = 1): S_R in {S_reg.fmt(12)}")
    print(f"       Method A (256-bit Interval LDL^T):          inertia = ({nn_reg_a}, 0, {np_reg_a}), min|pivot| >= {gap_reg.to_decimal_str(8, False)}, max_w <= {wid_reg.to_decimal_str(12, True)} [T]")
    print(f"       Method B (40b / 16b / 12b U H U^T SDD):     inertia = ({nn_reg_b}, 0, {np_reg_b}), min_SDD >= {mrg_reg.to_decimal_str(6, False)} (40b) / {mrg_reg_16.to_decimal_str(6, False)} (16b) / {mrg_reg_12.to_decimal_str(6, False)} (12b = 9.36 kb!) [T]")
    print(f"  [3B] Deformed S^4 (40 asymmetric dyadic edges in [{min(L_def_dyad).to_decimal_str(5, False)}, {max(L_def_dyad).to_decimal_str(5, True)}]): S_R in {S_def.fmt(12)}")
    print(f"       Method A (256-bit Interval LDL^T):          inertia = ({nn_def_a}, 0, {np_def_a}), min|pivot| >= {gap_def.to_decimal_str(8, False)}, max_w <= {wid_def.to_decimal_str(12, True)} [T]")
    print(f"       Method B (40b / 16b / 12b U H U^T SDD):     inertia = ({nn_def_b}, 0, {np_def_b}), min_SDD >= {mrg_def.to_decimal_str(6, False)} (40b) / {mrg_def_16.to_decimal_str(6, False)} (16b) / {mrg_def_12.to_decimal_str(6, False)} (12b = 9.36 kb!) [T]")

    return {"checks": checks, "S_reg": S_reg, "S_def": S_def, "mrg_reg": mrg_reg, "mrg_def": mrg_def}


# ==============================================================================
# TARGET 4: R-18 PI^0_1 ANALYTIC BOUNDS & CHAIN A2 2-LOOP UNIFICATION WINDOW
# ==============================================================================

def run_target4_r18_and_chain_a2() -> dict:
    print("\n" + "=" * 88)
    print("TARGET 4: R-18 Pi^0_1 Bounds (Lagarias/Li/Mertens) & Chain A2 2-Loop Certified ODE")
    print("=" * 88)
    prec = 144
    checks = 0

    # --- 4A. R-18 Lagarias inequality n = 1..60 (exact eq n=1, strict > for n=2..60) ---
    def sigma_nat(n: int) -> int:
        return sum(d for d in range(1, n + 1) if n % d == 0)

    H_n = DI_ZERO
    min_margin_n = None
    min_margin_val = None
    key_lagarias = {}
    for n in range(1, 61):
        H_n = H_n.add(DI.from_ratio(1, n, prec), prec)
        sig = sigma_nat(n)
        if n == 1:
            assert sig == 1 and H_n == DI_ONE
            checks += 1
        else:
            rhs = H_n.add(di_exp(H_n, prec).mul(di_log(H_n, prec), prec), prec)
            margin = rhs.sub(DI.from_int(sig), prec)
            assert margin.strictly_pos(), f"Lagarias failed at n={n}: sigma={sig}, rhs={rhs}"
            checks += 1
            if min_margin_val is None or margin.lo < min_margin_val.lo:
                min_margin_val = margin
                min_margin_n = n
            if n in (2, 4, 6, 12, 24, 36, 48, 60):
                key_lagarias[n] = (sig, rhs, margin)

    # --- 4B. R-18 Mertens 3 + 4 cos(theta) + cos(2 theta) >= 0 & Li off-line blowup witness ---
    for k in range(1, 13):
        th = DI.from_ratio(k, 7, prec).lo
        c1 = di_cos_point(th, prec)
        c2 = di_cos_point(th.shift(1), prec)
        mert = DI.from_int(3).add(c1.shift(2), prec).add(c2, prec)
        sq = DI_ONE.add(c1, prec).sqr(prec).shift(1)
        assert mert.lo <= sq.hi and sq.lo <= mert.hi and sq.lo.mant >= 0
    checks += 1

    # Li off-line witness: rho = 3/5 + 14 i (Re(rho) = 0.6 > 1/2), partner 1 - rho = 2/5 - 14 i:
    # |1 - 1/(1-rho)|^2 = 1 + (1 - 2*(2/5)) / ((2/5)^2 + 14^2) = 1 + (1/5) / (4904/25) = 1 + 5/4904 > 1!
    # Also verify for 1st Riemann zero rho_1 = 1/2 + i*gamma_1: Re(rho)=1/2 => |1 - 1/rho|^2 = 1 identically!
    # For off-line rho = 3/5 + 14 i, compute exact complex powers w = 1 - 1/rho, w' = 1 - 1/(1-rho) in DI
    # and certify an explicit integer m where the symmetric-pair contribution Re(2 - w^m - (w')^m) < 0 strictly!
    def c_mul(z1, z2, p=prec):
        return (z1[0].mul(z2[0], p).sub(z1[1].mul(z2[1], p), p),
                z1[0].mul(z2[1], p).add(z1[1].mul(z2[0], p), p))
    def c_li(re_z: DI, im_z: DI, p=prec):
        nrm = re_z.sqr(p).add(im_z.sqr(p), p)
        return (DI_ONE.sub(re_z.div(nrm, p), p), im_z.div(nrm, p))

    w_off = c_li(DI.from_ratio(3, 5, prec), DI.from_int(14), prec)
    wp_off = c_li(DI.from_ratio(2, 5, prec), DI.from_int(-14), prec)
    norm_wp = wp_off[0].sqr(prec).add(wp_off[1].sqr(prec), prec)
    assert norm_wp.sub(DI_ONE, prec).strictly_pos()  # |1 - 1/(1-rho)|^2 > 1 strictly!
    # Find smallest m where Re(2 - w^m - (w')^m) < 0 strictly (certified off-line Li violation!)
    zw = (DI_ONE, DI_ZERO)
    zwp = (DI_ONE, DI_ZERO)
    li_viol_m = None
    li_viol_val = None
    for m in range(1, 3000):
        zw = c_mul(zw, w_off, prec)
        zwp = c_mul(zwp, wp_off, prec)
        # Symmetric conjugate pair contributes 2 * (2 - Re(w^m) - Re((w')^m))
        contrib = DI.from_int(2).sub(zw[0], prec).sub(zwp[0], prec)
        if contrib.strictly_neg():
            li_viol_m = m
            li_viol_val = contrib
            break
    assert li_viol_m is not None
    checks += 2

    print(f"  [4A] R-18 Lagarias certified for ALL n = 1..60 (exact eq n=1, strict > for n=2..60) [T]:")
    print(f"       Tightest margin on 2..60: n={min_margin_n} (sigma={sigma_nat(min_margin_n)}, margin in {min_margin_val.fmt(8)})")
    print(f"       n=60 checkpoint: sigma(60)=168 vs RHS in {key_lagarias[60][1].fmt(10)} (margin in {key_lagarias[60][2].fmt(8)} > 0 [T])")
    print(f"  [4B] R-18 Mertens (12 pts) & Li off-line witness (rho = 0.6 + 14i):")
    print(f"       |1 - 1/(1-rho)|^2 in {norm_wp.fmt(12)} (> 1), certified Li negativity at m={li_viol_m}: Re(2 - w^m - w'^m) in {li_viol_val.fmt(8)} < 0 [T]")

    # --- 4C. Chain A2 Exact 1-Loop & Certified 2-Loop Machacek-Vaughn Picard-Lindelof Taylor ODE ---
    # Exact PDG 2024 inputs at M_Z = 91.1876 GeV (100% exact rational ratios, ZERO float!):
    ode_prec = 144
    pi_o = di_pi(ode_prec)
    four_pi = pi_o.shift(2)
    inv_16pi2 = DI.from_int(16).mul(pi_o.sqr(ode_prec), ode_prec).inv(ode_prec + 8)
    inv_16pi2_sq = inv_16pi2.sqr(ode_prec)

    M_Z = DI.from_dec_str("91.1876", ode_prec)
    alpha_em_inv = DI.from_dec_str("127.951", ode_prec)
    sin2_thW = DI.from_dec_str("0.23122", ode_prec)
    # Exact 1-loop & 2-loop SM beta coefficients
    b_SM = [DI.from_ratio(41, 10, ode_prec), DI.from_ratio(-19, 6, ode_prec), DI.from_int(-7)]
    B_SM = [
        [DI.from_ratio(199, 50, ode_prec), DI.from_ratio(27, 10, ode_prec), DI.from_ratio(44, 5, ode_prec)],
        [DI.from_ratio(9, 10, ode_prec),   DI.from_ratio(35, 6, ode_prec),  DI.from_int(12)],
        [DI.from_ratio(11, 10, ode_prec),  DI.from_ratio(9, 2, ode_prec),   DI.from_int(-26)],
    ]
    C_top_SM = [DI.from_ratio(17, 10, ode_prec), DI.from_ratio(3, 2, ode_prec), DI.from_int(2)]
    d_yt_SM = [DI.from_ratio(17, 20, ode_prec), DI.from_ratio(9, 4, ode_prec), DI.from_int(8)]
    c_yt_SM = DI.from_ratio(9, 2, ode_prec)

    # Exact Machacek-Vaughn Pati-Salam Chain A2 beta coefficients (S_122_C + S_1013_C):
    # Compute programmatically via exact integer/ratio arithmetic (matching verify_deep_frontier_v11.py!):
    def exact_ps_betas_a2(p: int):
        # Use exact scaled integer numerators over common denominator 24 to stay 100% exact!
        # Even simpler: exact DI.from_ratio from exact Python integer pairs (num, den)!
        def r_add(x, y):
            return (x[0] * y[1] + y[0] * x[1], x[1] * y[1])
        def r_mul(x, y):
            return (x[0] * y[0], x[1] * y[1])
        def r_red(x):
            a, b = x
            # Pure-int Euclid gcd
            ga, gb = (-a if a < 0 else a), (-b if b < 0 else b)
            while gb:
                ga, gb = gb, ga % gb
            return (a // ga, b // ga) if ga > 0 else (0, 1)

        C2G = [(4, 1), (2, 1), (2, 1)]
        b = [r_red(r_mul((-11, 3), C2G[i])) for i in range(3)]
        B = [[(0, 1) for _ in range(3)] for _ in range(3)]
        for i in range(3):
            B[i][i] = r_red(r_mul((-34, 3), r_mul(C2G[i], C2G[i])))
        weyls = [
            ((3, 1), (4, (1, 2), (15, 8)), (2, (1, 2), (3, 4)), (1, (0, 1), (0, 1))),
            ((3, 1), (4, (1, 2), (15, 8)), (1, (0, 1), (0, 1)), (2, (1, 2), (3, 4))),
        ]
        for mult, r4, rL, rR in weyls:
            rs = [r4, rL, rR]
            for i in range(3):
                d_oth = (rs[(i + 1) % 3][0] * rs[(i + 2) % 3][0], 1)
                Ti = r_red(r_mul(mult, r_mul(rs[i][1], d_oth)))
                b[i] = r_red(r_add(b[i], r_mul((2, 3), Ti)))
                for j in range(3):
                    if i == j:
                        coef = r_add(r_mul((10, 3), C2G[i]), r_mul((2, 1), rs[i][2]))
                    else:
                        coef = r_mul((2, 1), rs[j][2])
                    B[i][j] = r_red(r_add(B[i][j], r_mul(coef, Ti)))
        scalars = [
            ((1, 1), (1, (0, 1), (0, 1)), (2, (1, 2), (3, 4)), (2, (1, 2), (3, 4))),   # S_122_C
            ((1, 1), (10, (3, 1), (9, 2)), (1, (0, 1), (0, 1)), (3, (2, 1), (2, 1))),  # S_1013_C
        ]
        for fac, r4, rL, rR in scalars:
            rs = [r4, rL, rR]
            for i in range(3):
                d_oth = (rs[(i + 1) % 3][0] * rs[(i + 2) % 3][0], 1)
                Ti = r_red(r_mul(fac, r_mul(rs[i][1], d_oth)))
                b[i] = r_red(r_add(b[i], r_mul((1, 3), Ti)))
                for j in range(3):
                    if i == j:
                        coef = r_add(r_mul((2, 3), C2G[i]), r_mul((4, 1), rs[i][2]))
                    else:
                        coef = r_mul((4, 1), rs[j][2])
                    B[i][j] = r_red(r_add(B[i][j], r_mul(coef, Ti)))
        return (
            [DI.from_ratio(n, d, p) for n, d in b],
            [[DI.from_ratio(n, d, p) for n, d in row] for row in B],
            b, B,
        )

    b_A2, B_A2, b_A2_rat, B_A2_rat = exact_ps_betas_a2(ode_prec)
    assert b_A2_rat == [(-23, 3), (-3, 1), (11, 3)]
    C_top_PS = [DI.from_int(2), DI.from_int(2), DI.from_int(2)]
    d_yt_PS = [DI.from_ratio(15, 2, ode_prec), DI.from_ratio(9, 4, ode_prec), DI.from_ratio(9, 4, ode_prec)]
    c_yt_PS = DI.from_int(6)
    checks += 1

    # 4C(i). Exact 1-Loop Closed-Form Chain A2 Unification in DI:
    # Linear system in (t_PS, dt_PS = t_GUT - t_PS):
    #   1/a_i(t) = 1/a_i(0) - b_i * t / (2 pi)
    #   Matching: 1/a_4C(t_PS) = 1/a_3(t_PS), 1/a_2L = 1/a_2, 1/a_2R = (5/3)/a_1 - (2/3)/a_3
    #   Unification at t_GUT: 1/a_4C = 1/a_2L = 1/a_2R!
    a1_inv_0 = DI.from_ratio(3, 5, ode_prec).mul(alpha_em_inv, ode_prec).mul(DI_ONE.sub(sin2_thW, ode_prec), ode_prec)
    a2_inv_0 = alpha_em_inv.mul(sin2_thW, ode_prec)
    a3_inv_0 = DI.from_dec_str("0.1180", ode_prec).inv(ode_prec)
    # Using x = t_PS / (2 pi), y = dt_PS / (2 pi):
    #   Eq1 (a_4C^-1 = a_2L^-1): (b3_SM - b2_SM) x + (b4_A2 - b2L_A2) y = a3_inv_0 - a2_inv_0
    #   Eq2 (a_2R^-1 = a_2L^-1): ((5/3)b1_SM - (2/3)b3_SM - b2_SM) x + (b2R_A2 - b2L_A2) y = (5/3)a1_inv_0 - (2/3)a3_inv_0 - a2_inv_0
    m11 = b_SM[2].sub(b_SM[1], ode_prec)
    m12 = b_A2[0].sub(b_A2[1], ode_prec)
    r1 = a3_inv_0.sub(a2_inv_0, ode_prec)
    c53 = DI.from_ratio(5, 3, ode_prec)
    c23 = DI.from_ratio(2, 3, ode_prec)
    m21 = c53.mul(b_SM[0], ode_prec).sub(c23.mul(b_SM[2], ode_prec), ode_prec).sub(b_SM[1], ode_prec)
    m22 = b_A2[2].sub(b_A2[1], ode_prec)
    r2 = c53.mul(a1_inv_0, ode_prec).sub(c23.mul(a3_inv_0, ode_prec), ode_prec).sub(a2_inv_0, ode_prec)
    det_1l = m11.mul(m22, ode_prec).sub(m12.mul(m21, ode_prec), ode_prec)
    x_1l = r1.mul(m22, ode_prec).sub(m12.mul(r2, ode_prec), ode_prec).div(det_1l, ode_prec)
    y_1l = m11.mul(r2, ode_prec).sub(r1.mul(m21, ode_prec), ode_prec).div(det_1l, ode_prec)
    t_PS_1l = x_1l.mul(pi_o.shift(1), ode_prec)
    t_GUT_1l = x_1l.add(y_1l, ode_prec).mul(pi_o.shift(1), ode_prec)
    aGUT_inv_1l = a2_inv_0.sub(b_SM[1].mul(x_1l, ode_prec), ode_prec).sub(b_A2[1].mul(y_1l, ode_prec), ode_prec)
    assert t_PS_1l.strictly_pos() and y_1l.strictly_pos() and aGUT_inv_1l.strictly_pos()
    checks += 1

    # 4C(ii). Certified Order-6 Picard-Lindelof Interval Taylor & Variational-ODE Integrator (2-Loop Machacek-Vaughn)!
    # Autonomous 4D polynomial ODE dy/dt = f(y), y = [g1, g2, g3, yt], plus coupled variational ODE dv/dt = Df(y) v!
    def taylor_mul(a: list[DI], b: list[DI], deg: int, p: int) -> list[DI]:
        out = []
        for k in range(deg + 1):
            acc = a[0].mul(b[k], p)
            for j in range(1, k + 1):
                acc = acc.add(a[j].mul(b[k - j], p), p)
            out.append(acc)
        return out

    def eval_rhs_taylor(Y: list[list[DI]], deg: int, b_v, B_m, C_top, c_yt, d_yt, p: int) -> list[list[DI]]:
        # Compute g_i^2, g_i^3, yt^2 up to order deg
        g2 = [taylor_mul(Y[i], Y[i], deg, p) for i in range(3)]
        g3 = [taylor_mul(g2[i], Y[i], deg, p) for i in range(3)]
        yt2 = taylor_mul(Y[3], Y[3], deg, p)
        out: list[list[DI]] = []
        for i in range(3):
            br = [DI_ZERO for _ in range(deg + 1)]
            for k in range(deg + 1):
                acc = C_top[i].mul(yt2[k], p).neg()
                for j in range(3):
                    acc = acc.add(B_m[i][j].mul(g2[j][k], p), p)
                br[k] = acc.mul(inv_16pi2_sq, p)
            br[0] = br[0].add(b_v[i].mul(inv_16pi2, p), p)
            out.append(taylor_mul(g3[i], br, deg, p))
        br_y = []
        for k in range(deg + 1):
            acc = c_yt.mul(yt2[k], p)
            for j in range(3):
                acc = acc.sub(d_yt[j].mul(g2[j][k], p), p)
            br_y.append(acc.mul(inv_16pi2, p))
        out.append(taylor_mul(Y[3], br_y, deg, p))
        return out

    def eval_rhs_dual_taylor(
        Y: list[list[DI]], V: list[list[DI]], deg: int, b_v, B_m, C_top, c_yt, d_yt, p: int
    ) -> tuple[list[list[DI]], list[list[DI]]]:
        """Exact dual-Taylor evaluation returning (f(Y), Df(Y) * V) up to degree deg!"""
        def d_mul(a_p, b_p):
            a0, a1 = a_p
            b0, b1 = b_p
            ab = taylor_mul(a0, b0, deg, p)
            d1 = taylor_mul(a0, b1, deg, p)
            d2 = taylor_mul(a1, b0, deg, p)
            return ab, [d1[k].add(d2[k], p) for k in range(deg + 1)]

        dy = [(Y[i], V[i]) for i in range(4)]
        g2 = [d_mul(dy[i], dy[i]) for i in range(3)]
        g3 = [d_mul(g2[i], dy[i]) for i in range(3)]
        yt2 = d_mul(dy[3], dy[3])
        f_out: list[list[DI]] = []
        df_out: list[list[DI]] = []
        for i in range(3):
            br0 = [DI_ZERO for _ in range(deg + 1)]
            br1 = [DI_ZERO for _ in range(deg + 1)]
            for k in range(deg + 1):
                a0 = C_top[i].mul(yt2[0][k], p).neg()
                a1 = C_top[i].mul(yt2[1][k], p).neg()
                for j in range(3):
                    a0 = a0.add(B_m[i][j].mul(g2[j][0][k], p), p)
                    a1 = a1.add(B_m[i][j].mul(g2[j][1][k], p), p)
                br0[k] = a0.mul(inv_16pi2_sq, p)
                br1[k] = a1.mul(inv_16pi2_sq, p)
            br0[0] = br0[0].add(b_v[i].mul(inv_16pi2, p), p)
            r0, r1 = d_mul(g3[i], (br0, br1))
            f_out.append(r0)
            df_out.append(r1)
        by0, by1 = [], []
        for k in range(deg + 1):
            a0 = c_yt.mul(yt2[0][k], p)
            a1 = c_yt.mul(yt2[1][k], p)
            for j in range(3):
                a0 = a0.sub(d_yt[j].mul(g2[j][0][k], p), p)
                a1 = a1.sub(d_yt[j].mul(g2[j][1][k], p), p)
            by0.append(a0.mul(inv_16pi2, p))
            by1.append(a1.mul(inv_16pi2, p))
        ry0, ry1 = d_mul(dy[3], (by0, by1))
        f_out.append(ry0)
        df_out.append(ry1)
        return f_out, df_out

    def eval_rhs_point(y: list[DI], b_v, B_m, C_top, c_yt, d_yt, p: int) -> list[DI]:
        return [r[0] for r in eval_rhs_taylor([[yi] for yi in y], 0, b_v, B_m, C_top, c_yt, d_yt, p)]

    def eval_df_vec_point(y: list[DI], v: list[DI], b_v, B_m, C_top, c_yt, d_yt, p: int) -> list[DI]:
        _, dfv = eval_rhs_dual_taylor([[yi] for yi in y], [[vi] for vi in v], 0, b_v, B_m, C_top, c_yt, d_yt, p)
        return [r[0] for r in dfv]

    def eval_jacobian_norm_inf(Y: list[DI], b_v, B_m, C_top, c_yt, d_yt, p: int) -> Dyadic:
        """Certified upper bound on ||Df(Y)||_inf for Banach contraction verification h * L < 1."""
        g2 = [Y[i].sqr(p) for i in range(3)]
        yt2 = Y[3].sqr(p)
        max_row = D_ZERO
        for i in range(3):
            br = C_top[i].mul(yt2, p).neg()
            for j in range(3):
                br = br.add(B_m[i][j].mul(g2[j], p), p)
            br = br.mul(inv_16pi2_sq, p).add(b_v[i].mul(inv_16pi2, p), p)
            row_sum = D_ZERO
            for j in range(3):
                val = Y[i].mul(g2[i], p).mul(inv_16pi2_sq, p).mul(B_m[i][j], p).mul(Y[j], p).shift(1)
                if i == j:
                    val = val.add(DI.from_int(3).mul(g2[i], p).mul(br, p), p)
                row_sum = Dyadic.add_directed(row_sum, val.abs_upper(), p, True)
            val_yt = C_top[i].mul(Y[i].mul(g2[i], p), p).mul(Y[3], p).mul(inv_16pi2_sq, p).shift(1)
            row_sum = Dyadic.add_directed(row_sum, val_yt.abs_upper(), p, True)
            if row_sum > max_row:
                max_row = row_sum
        row_y = D_ZERO
        for j in range(3):
            v = inv_16pi2.mul(Y[3], p).mul(d_yt[j], p).mul(Y[j], p).shift(1)
            row_y = Dyadic.add_directed(row_y, v.abs_upper(), p, True)
        v_yy = DI.from_int(3).mul(c_yt, p).mul(yt2, p)
        for j in range(3):
            v_yy = v_yy.sub(d_yt[j].mul(g2[j], p), p)
        v_yy = v_yy.mul(inv_16pi2, p)
        row_y = Dyadic.add_directed(row_y, v_yy.abs_upper(), p, True)
        return row_y if row_y > max_row else max_row

    def ode_taylor_step(Y_cur: list[DI], h: DI, b_v, B_m, C_top, c_yt, d_yt, order: int = 6, p: int = ode_prec) -> list[DI]:
        """
        Certified Picard-Lindelof + Order-6 Taylor step on [t, t + h]:
          1) Find coarse enclosure Y_tilde satisfying Y_cur + [0, h] * f(Y_tilde) subset Y_tilde
             AND h * ||Df(Y_tilde)||_inf < 1 (proving unique exact solution y(t+s) in Y_tilde!);
          2) Compute exact Taylor coefficients y^[0..order-1] on Y_cur and remainder y^[order] on Y_tilde;
          3) Return y(t + h) in sum_{k=0}^{order-1} y^[k](Y_cur) h^k + y^[order](Y_tilde) h^order!
        """
        h_0h = DI(D_ZERO, h.hi)
        f0 = eval_rhs_point(Y_cur, b_v, B_m, C_top, c_yt, d_yt, p)
        eps_inf = DI(Dyadic(-1, -40), Dyadic(1, -40))
        Y_tilde = [Y_cur[i].add(h_0h.mul(f0[i], p).mul(DI.from_ratio(3, 2, p), p), p).add(eps_inf, p) for i in range(4)]
        verified = False
        for _ in range(12):
            f_t = eval_rhs_point(Y_tilde, b_v, B_m, C_top, c_yt, d_yt, p)
            P_t = [Y_cur[i].add(h_0h.mul(f_t[i], p), p) for i in range(4)]
            if all(Y_tilde[i].contains(P_t[i]) for i in range(4)):
                L_lip = eval_jacobian_norm_inf(Y_tilde, b_v, B_m, C_top, c_yt, d_yt, p)
                if Dyadic.mul_directed(h.hi, L_lip, p, True) < D_ONE:
                    Y_tilde = P_t
                    verified = True
                    break
            Y_tilde = [P_t[i].add(P_t[i].sub(Y_cur[i], p).mul(DI.from_ratio(1, 2, p), p), p).add(eps_inf, p) for i in range(4)]
        assert verified, "Picard-Lindelof a priori enclosure verification failed!"

        def build_coeffs(y0: list[DI], max_deg: int) -> list[list[DI]]:
            Y_c = [[y0[i]] for i in range(4)]
            for k in range(max_deg):
                fk = eval_rhs_taylor(Y_c, k, b_v, B_m, C_top, c_yt, d_yt, p)
                inv_k1 = DI.from_ratio(1, k + 1, p)
                for i in range(4):
                    Y_c[i].append(fk[i][k].mul(inv_k1, p))
            return Y_c

        Yc = build_coeffs(Y_cur, order - 1)
        Yt = build_coeffs(Y_tilde, order)
        h_pow = [DI_ONE]
        for _ in range(order):
            h_pow.append(h_pow[-1].mul(h, p))
        Y_next = []
        for i in range(4):
            acc = DI_ZERO
            for k in range(order):
                acc = acc.add(Yc[i][k].mul(h_pow[k], p), p)
            acc = acc.add(Yt[i][order].mul(h_pow[order], p), p)
            Y_next.append(acc)
        return Y_next

    def ode_dual_taylor_step(
        Y_cur: list[DI], V_cur: list[DI], h: DI, b_v, B_m, C_top, c_yt, d_yt, order: int = 6, p: int = ode_prec
    ) -> tuple[list[DI], list[DI]]:
        """
        Certified triangular Picard-Lindelof + Order-6 Dual-Taylor step on [t, t + h] for (y, v):
          dy/dt = f(y), dv/dt = Df(y) v.
        The SINGLE verified contraction h * ||Df(Y_tilde)||_inf < 1 simultaneously proves unique
        Banach fixed points for BOTH y(t) in Y_tilde AND the linear variational flow v(t) in V_tilde!
        """
        h_0h = DI(D_ZERO, h.hi)
        f0 = eval_rhs_point(Y_cur, b_v, B_m, C_top, c_yt, d_yt, p)
        eps_inf = DI(Dyadic(-1, -40), Dyadic(1, -40))
        Y_tilde = [Y_cur[i].add(h_0h.mul(f0[i], p).mul(DI.from_ratio(3, 2, p), p), p).add(eps_inf, p) for i in range(4)]
        ver_y = False
        for _ in range(12):
            f_t = eval_rhs_point(Y_tilde, b_v, B_m, C_top, c_yt, d_yt, p)
            P_t = [Y_cur[i].add(h_0h.mul(f_t[i], p), p) for i in range(4)]
            if all(Y_tilde[i].contains(P_t[i]) for i in range(4)):
                L_lip = eval_jacobian_norm_inf(Y_tilde, b_v, B_m, C_top, c_yt, d_yt, p)
                if Dyadic.mul_directed(h.hi, L_lip, p, True) < D_ONE:
                    Y_tilde = P_t
                    ver_y = True
                    break
            Y_tilde = [P_t[i].add(P_t[i].sub(Y_cur[i], p).mul(DI.from_ratio(1, 2, p), p), p).add(eps_inf, p) for i in range(4)]
        assert ver_y, "Dual Picard Y_tilde failed"

        # Linear variational Picard enclosure V_tilde (Lipschitz constant = ||Df(Y_tilde)||_inf, ALREADY < 1/h!)
        fv0 = eval_df_vec_point(Y_tilde, V_cur, b_v, B_m, C_top, c_yt, d_yt, p)
        V_tilde = [V_cur[i].add(h_0h.mul(fv0[i], p).mul(DI.from_ratio(3, 2, p), p), p).add(eps_inf, p) for i in range(4)]
        ver_v = False
        for _ in range(12):
            fv_t = eval_df_vec_point(Y_tilde, V_tilde, b_v, B_m, C_top, c_yt, d_yt, p)
            Q_t = [V_cur[i].add(h_0h.mul(fv_t[i], p), p) for i in range(4)]
            if all(V_tilde[i].contains(Q_t[i]) for i in range(4)):
                V_tilde = Q_t
                ver_v = True
                break
            V_tilde = [Q_t[i].add(Q_t[i].sub(V_cur[i], p).mul(DI.from_ratio(1, 2, p), p), p).add(eps_inf, p) for i in range(4)]
        assert ver_v, "Dual Picard V_tilde failed"

        def build_dual_coeffs(y0: list[DI], v0: list[DI], max_deg: int):
            Yc = [[y0[i]] for i in range(4)]
            Vc = [[v0[i]] for i in range(4)]
            for k in range(max_deg):
                fk, dfk = eval_rhs_dual_taylor(Yc, Vc, k, b_v, B_m, C_top, c_yt, d_yt, p)
                inv_k1 = DI.from_ratio(1, k + 1, p)
                for i in range(4):
                    Yc[i].append(fk[i][k].mul(inv_k1, p))
                    Vc[i].append(dfk[i][k].mul(inv_k1, p))
            return Yc, Vc

        Yc, Vc = build_dual_coeffs(Y_cur, V_cur, order - 1)
        Yt, Vt = build_dual_coeffs(Y_tilde, V_tilde, order)
        h_pow = [DI_ONE]
        for _ in range(order):
            h_pow.append(h_pow[-1].mul(h, p))
        Y_next, V_next = [], []
        for i in range(4):
            ay, av = DI_ZERO, DI_ZERO
            for k in range(order):
                ay = ay.add(Yc[i][k].mul(h_pow[k], p), p)
                av = av.add(Vc[i][k].mul(h_pow[k], p), p)
            ay = ay.add(Yt[i][order].mul(h_pow[order], p), p)
            av = av.add(Vt[i][order].mul(h_pow[order], p), p)
            Y_next.append(ay)
            V_next.append(av)
        return Y_next, V_next

    def run_ode_certified(y0: list[DI], T_len: DI, n_steps: int, b_v, B_m, C_top, c_yt, d_yt, p: int = ode_prec) -> list[DI]:
        h = T_len.div(DI.from_int(n_steps), p)
        y = y0
        for _ in range(n_steps):
            y = ode_taylor_step(y, h, b_v, B_m, C_top, c_yt, d_yt, order=6, p=p)
        return y

    sm_checkpoint_cache: dict[tuple[int, int, int, int, int], tuple[list[DI], list[DI] | None]] = {}
    t_sm_base = Dyadic(20, 0)  # Exact dyadic SM checkpoint t_base = 20.0 (strictly below all PDG +-1sigma Krawczyk boxes)!

    def get_sm_at_base(alpha_s_di: DI, sm_steps: int = 64) -> tuple[list[DI], list[DI] | None]:
        key = (alpha_s_di.lo.mant, alpha_s_di.lo.exp, alpha_s_di.hi.mant, alpha_s_di.hi.exp, sm_steps)
        if key not in sm_checkpoint_cache:
            a1_0 = DI.from_ratio(5, 3, ode_prec).div(alpha_em_inv.mul(DI_ONE.sub(sin2_thW, ode_prec), ode_prec), ode_prec)
            a2_0 = DI_ONE.div(alpha_em_inv.mul(sin2_thW, ode_prec), ode_prec)
            g1_0 = four_pi.mul(a1_0, ode_prec).sqrt(ode_prec)
            g2_0 = four_pi.mul(a2_0, ode_prec).sqrt(ode_prec)
            yt_0 = DI.from_dec_str("0.995", ode_prec)
            y0 = [g1_0, g2_0, four_pi.mul(alpha_s_di, ode_prec).sqrt(ode_prec), yt_0]
            if alpha_s_di.width(ode_prec) < Dyadic(1, -40):
                sm_checkpoint_cache[key] = (
                    run_ode_certified(y0, DI.point(t_sm_base), sm_steps, b_SM, B_SM, C_top_SM, c_yt_SM, d_yt_SM, ode_prec),
                    None,
                )
            else:
                # Exact FTC Mean-Value Variational Flow for continuum alpha_s in [a_lo, a_hi]:
                # Eliminates dissipative SM wrapping by tracking midpoint y(t; a_c) AND sensitivity
                # w(t; a_s) = dy/d(alpha_s), tightening via y(t; a_s) = y(t; a_c) + int_{a_c}^{a_s} w(t; xi) dxi!
                a_c = alpha_s_di.midpoint(ode_prec)
                d_alpha = DI(
                    Dyadic.add_directed(alpha_s_di.lo, a_c.neg(), ode_prec, False),
                    Dyadic.add_directed(alpha_s_di.hi, a_c.neg(), ode_prec, True),
                )
                y_mid = [g1_0, g2_0, four_pi.mul(DI.point(a_c), ode_prec).sqrt(ode_prec), yt_0]
                # Exact initial derivative d/d(alpha_s) sqrt(4 pi alpha_s) = 2 pi / sqrt(4 pi alpha_s)
                w_cur = [DI_ZERO, DI_ZERO, pi_o.shift(1).div(y0[2], ode_prec), DI_ZERO]
                y_cur = y0
                h_sm = DI.point(t_sm_base).div(DI.from_int(sm_steps), ode_prec)
                for _ in range(sm_steps):
                    y_mid = ode_taylor_step(y_mid, h_sm, b_SM, B_SM, C_top_SM, c_yt_SM, d_yt_SM, order=6, p=ode_prec)
                    y_raw, w_cur = ode_dual_taylor_step(y_cur, w_cur, h_sm, b_SM, B_SM, C_top_SM, c_yt_SM, d_yt_SM, order=6, p=ode_prec)
                    y_mv = [y_mid[i].add(w_cur[i].mul(d_alpha, ode_prec), ode_prec) for i in range(4)]
                    y_next = []
                    for i in range(4):
                        lo_i = y_raw[i].lo if y_raw[i].lo >= y_mv[i].lo else y_mv[i].lo
                        hi_i = y_raw[i].hi if y_raw[i].hi <= y_mv[i].hi else y_mv[i].hi
                        assert lo_i <= hi_i, "FTC mean-value and raw enclosure disjoint!"
                        y_next.append(DI(lo_i, hi_i))
                    y_cur = y_next
                sm_checkpoint_cache[key] = (y_cur, w_cur)
        return sm_checkpoint_cache[key]

    def chain_a2_eval_certified(
        t_PS_val: DI,
        alpha_s_di: DI,
        with_deriv: bool = False,
        with_as_deriv: bool = False,
        sm_steps: int = 64,
        ps_step_den: int = 4,
    ) -> dict:
        """
        Integrate SM 2-loop on [0, t_PS_val], match to G_422, integrate PS Chain A2 to g_4C = g_2L
        crossing with CERTIFIED Banach contraction on EVERY Picard box AND certified strict crossing
        velocity d(g_4C - g_2L)/dt < 0! If with_deriv=True, simultaneously propagates exact variational
        ODE v(t) = dy_PS/dt_PS to return certified enclosure of d(res)/d(t_PS)! If with_as_deriv=True
        (with_deriv=True), also propagates w(t) = dy_PS/d(alpha_s) to certify d(a_GUT^-1)/d(alpha_s)!
        """
        assert t_PS_val.lo >= t_sm_base
        y_base, w_base = get_sm_at_base(alpha_s_di, sm_steps=sm_steps)
        dt_from_base = DI.point(t_PS_val.lo).sub(DI.point(t_sm_base), ode_prec)
        w_ps_sm = w_base
        if dt_from_base.hi.mant > 0:
            if with_as_deriv:
                assert w_base is not None
                h_fb = dt_from_base.div(DI.from_int(4), ode_prec)
                y_ps_sm, w_ps_sm = y_base, w_base
                for _ in range(4):
                    y_ps_sm, w_ps_sm = ode_dual_taylor_step(y_ps_sm, w_ps_sm, h_fb, b_SM, B_SM, C_top_SM, c_yt_SM, d_yt_SM, order=6, p=ode_prec)
            else:
                y_ps_sm = run_ode_certified(y_base, dt_from_base, 4, b_SM, B_SM, C_top_SM, c_yt_SM, d_yt_SM, ode_prec)
        else:
            y_ps_sm = y_base
        if t_PS_val.lo < t_PS_val.hi:
            dt_ps = DI(D_ZERO, Dyadic.add_directed(t_PS_val.hi, t_PS_val.lo.neg(), ode_prec, True))
            f_sm0 = eval_rhs_point(y_ps_sm, b_SM, B_SM, C_top_SM, c_yt_SM, d_yt_SM, ode_prec)
            eps_s = DI(Dyadic(-1, -40), Dyadic(1, -40))
            Y_sm = [y_ps_sm[i].add(dt_ps.mul(f_sm0[i], ode_prec).mul(DI.from_ratio(3, 2, ode_prec), ode_prec), ode_prec).add(eps_s, ode_prec) for i in range(4)]
            ok_sm = False
            for _ in range(12):
                f_smt = eval_rhs_point(Y_sm, b_SM, B_SM, C_top_SM, c_yt_SM, d_yt_SM, ode_prec)
                P_sm = [y_ps_sm[i].add(dt_ps.mul(f_smt[i], ode_prec), ode_prec) for i in range(4)]
                if all(Y_sm[i].contains(P_sm[i]) for i in range(4)):
                    L_sm = eval_jacobian_norm_inf(Y_sm, b_SM, B_SM, C_top_SM, c_yt_SM, d_yt_SM, ode_prec)
                    if Dyadic.mul_directed(dt_ps.hi, L_sm, ode_prec, True) < D_ONE:
                        Y_sm = P_sm
                        ok_sm = True
                        break
                Y_sm = [P_sm[i].add(P_sm[i].sub(y_ps_sm[i], ode_prec).mul(DI.from_ratio(1, 2, ode_prec), ode_prec), ode_prec).add(eps_s, ode_prec) for i in range(4)]
            assert ok_sm, "Picard t_PS box enclosure/contraction failed"
            if with_as_deriv:
                assert w_ps_sm is not None
                fw_sm0 = eval_df_vec_point(Y_sm, w_ps_sm, b_SM, B_SM, C_top_SM, c_yt_SM, d_yt_SM, ode_prec)
                W_sm = [w_ps_sm[i].add(dt_ps.mul(fw_sm0[i], ode_prec).mul(DI.from_ratio(3, 2, ode_prec), ode_prec), ode_prec).add(eps_s, ode_prec) for i in range(4)]
                ok_wsm = False
                for _ in range(12):
                    fw_smt = eval_df_vec_point(Y_sm, W_sm, b_SM, B_SM, C_top_SM, c_yt_SM, d_yt_SM, ode_prec)
                    Q_sm = [w_ps_sm[i].add(dt_ps.mul(fw_smt[i], ode_prec), ode_prec) for i in range(4)]
                    if all(W_sm[i].contains(Q_sm[i]) for i in range(4)):
                        W_sm = Q_sm
                        ok_wsm = True
                        break
                    W_sm = [Q_sm[i].add(Q_sm[i].sub(w_ps_sm[i], ode_prec).mul(DI.from_ratio(1, 2, ode_prec), ode_prec), ode_prec).add(eps_s, ode_prec) for i in range(4)]
                assert ok_wsm, "Variational alpha_s Picard t_PS box enclosure failed"
                w_ps_sm = W_sm
            y_ps_sm = Y_sm

        # 2. Exact Pati-Salam tree-level matching at M_PS:
        g4_0 = y_ps_sm[2]
        g2L_0 = y_ps_sm[1]
        inv_g2R_sq = c53.div(y_ps_sm[0].sqr(ode_prec), ode_prec).sub(c23.div(y_ps_sm[2].sqr(ode_prec), ode_prec), ode_prec)
        assert inv_g2R_sq.strictly_pos()
        g2R_0 = inv_g2R_sq.inv(ode_prec).sqrt(ode_prec)
        y_ps0 = [g4_0, g2L_0, g2R_0, y_ps_sm[3]]

        v_cur = None
        w_cur = None
        if with_deriv:
            # Exact initial variational vector v(t_PS) = d/dt_PS [Phi_match(y_SM(t_PS))] - f_PS(y_ps0)!
            f_sm_m = eval_rhs_point(y_ps_sm, b_SM, B_SM, C_top_SM, c_yt_SM, d_yt_SM, ode_prec)
            f_ps_m = eval_rhs_point(y_ps0, b_A2, B_A2, C_top_PS, c_yt_PS, d_yt_PS, ode_prec)
            g1_3 = y_ps_sm[0].mul(y_ps_sm[0].sqr(ode_prec), ode_prec)
            g3_3 = y_ps_sm[2].mul(y_ps_sm[2].sqr(ode_prec), ode_prec)
            g2R_3 = g2R_0.mul(g2R_0.sqr(ode_prec), ode_prec)
            dg2R_dt = g2R_3.mul(
                c53.mul(f_sm_m[0].div(g1_3, ode_prec), ode_prec).sub(
                    c23.mul(f_sm_m[2].div(g3_3, ode_prec), ode_prec), ode_prec
                ), ode_prec
            )
            dphi_dt = [f_sm_m[2], f_sm_m[1], dg2R_dt, f_sm_m[3]]
            v_cur = [dphi_dt[i].sub(f_ps_m[i], ode_prec) for i in range(4)]
            if with_as_deriv:
                assert w_ps_sm is not None
                # Exact initial alpha_s variational vector w_PS(t_PS) = DPhi_match(y_SM) * w_SM (at fixed t_PS!)
                dg2R_das = g2R_3.mul(
                    c53.mul(w_ps_sm[0].div(g1_3, ode_prec), ode_prec).sub(
                        c23.mul(w_ps_sm[2].div(g3_3, ode_prec), ode_prec), ode_prec
                    ), ode_prec
                )
                w_cur = [w_ps_sm[2], w_ps_sm[1], dg2R_das, w_ps_sm[3]]

        # 3. Step in Pati-Salam while g_4C - g_2L stays strictly > 0, then bracket until strictly < 0!
        h_step = DI.from_ratio(1, ps_step_den, ode_prec)
        t_cur = t_PS_val
        y_cur = y_ps0
        assert y_cur[0].sub(y_cur[1], ode_prec).strictly_pos()
        dt_span = D_ZERO
        while True:
            if with_deriv:
                y_nxt, v_nxt = ode_dual_taylor_step(y_cur, v_cur, h_step, b_A2, B_A2, C_top_PS, c_yt_PS, d_yt_PS, order=6, p=ode_prec)
                w_nxt = ode_dual_taylor_step(y_cur, w_cur, h_step, b_A2, B_A2, C_top_PS, c_yt_PS, d_yt_PS, order=6, p=ode_prec)[1] if with_as_deriv else None
            else:
                y_nxt = ode_taylor_step(y_cur, h_step, b_A2, B_A2, C_top_PS, c_yt_PS, d_yt_PS, order=6, p=ode_prec)
                v_nxt = None
                w_nxt = None
            diff_nxt = y_nxt[0].sub(y_nxt[1], ode_prec)
            if diff_nxt.strictly_pos():
                y_cur = y_nxt
                v_cur = v_nxt
                w_cur = w_nxt
                t_cur = t_cur.add(h_step, ode_prec)
            elif diff_nxt.strictly_neg():
                dt_span = h_step.hi
                break
            else:
                y_end = y_nxt
                dt_span = h_step.hi
                for _ in range(10):
                    y_end = ode_taylor_step(y_end, h_step, b_A2, B_A2, C_top_PS, c_yt_PS, d_yt_PS, order=6, p=ode_prec)
                    dt_span = Dyadic.add_directed(dt_span, h_step.hi, ode_prec, True)
                    if y_end[0].sub(y_end[1], ode_prec).strictly_neg():
                        break
                assert y_end[0].sub(y_end[1], ode_prec).strictly_neg()
                break

        # 4. Refine crossing t_hit in [t_cur, t_cur + dt_span] via independent-endpoint certified bisection!
        is_pt = (alpha_s_di.width(ode_prec) < Dyadic(1, -40)) and (t_PS_val.width(ode_prec) < Dyadic(1, -40))
        inner_bi = 18 if is_pt else 10
        inner_nr = 8 if is_pt else 5
        dt_lo = D_ZERO
        dt_hi = dt_span
        dt_star = None
        for _ in range(inner_bi):
            dt_mid = Dyadic.add_directed(dt_lo, dt_hi, ode_prec, False).shift(-1)
            y_m = ode_taylor_step(y_cur, DI.point(dt_mid), b_A2, B_A2, C_top_PS, c_yt_PS, d_yt_PS, order=6, p=ode_prec)
            dm = y_m[0].sub(y_m[1], ode_prec)
            if dm.strictly_pos():
                dt_lo = dt_mid
            elif dm.strictly_neg():
                dt_hi = dt_mid
            else:
                dt_star = dt_mid
                break
        if dt_star is not None:
            l_hi = dt_star
            for _ in range(inner_nr):
                m_l = Dyadic.add_directed(dt_lo, l_hi, ode_prec, False).shift(-1)
                ym_l = ode_taylor_step(y_cur, DI.point(m_l), b_A2, B_A2, C_top_PS, c_yt_PS, d_yt_PS, order=6, p=ode_prec)
                if ym_l[0].sub(ym_l[1], ode_prec).strictly_pos():
                    dt_lo = m_l
                else:
                    l_hi = m_l
            r_lo = dt_star
            for _ in range(inner_nr):
                m_r = Dyadic.add_directed(r_lo, dt_hi, ode_prec, False).shift(-1)
                ym_r = ode_taylor_step(y_cur, DI.point(m_r), b_A2, B_A2, C_top_PS, c_yt_PS, d_yt_PS, order=6, p=ode_prec)
                if ym_r[0].sub(ym_r[1], ode_prec).strictly_neg():
                    dt_hi = m_r
                else:
                    r_lo = m_r

        # Rigorous enclosure of state (and variational states) at crossing time t_hit in [t_cur + dt_lo, t_cur + dt_hi]!
        if with_deriv:
            if dt_lo.mant > 0:
                y_lo, v_lo = ode_dual_taylor_step(y_cur, v_cur, DI.point(dt_lo), b_A2, B_A2, C_top_PS, c_yt_PS, d_yt_PS, order=6, p=ode_prec)
                w_lo = ode_dual_taylor_step(y_cur, w_cur, DI.point(dt_lo), b_A2, B_A2, C_top_PS, c_yt_PS, d_yt_PS, order=6, p=ode_prec)[1] if with_as_deriv else None
            else:
                y_lo, v_lo, w_lo = y_cur, v_cur, w_cur
        else:
            y_lo = ode_taylor_step(y_cur, DI.point(dt_lo), b_A2, B_A2, C_top_PS, c_yt_PS, d_yt_PS, order=6, p=ode_prec) if dt_lo.mant > 0 else y_cur
            v_lo = None
            w_lo = None
        y_hi = ode_taylor_step(y_cur, DI.point(dt_hi), b_A2, B_A2, C_top_PS, c_yt_PS, d_yt_PS, order=6, p=ode_prec)
        assert y_lo[0].sub(y_lo[1], ode_prec).strictly_pos() and y_hi[0].sub(y_hi[1], ode_prec).strictly_neg()
        dt_rem = DI(D_ZERO, Dyadic.add_directed(dt_hi, dt_lo.neg(), ode_prec, True))

        # Certified Picard enclosure + Banach contraction + STRICT crossing slope on [dt_lo, dt_hi]!
        f_lo = eval_rhs_point(y_lo, b_A2, B_A2, C_top_PS, c_yt_PS, d_yt_PS, ode_prec)
        eps_c = DI(Dyadic(-1, -40), Dyadic(1, -40))
        Y_cross = [y_lo[i].add(dt_rem.mul(f_lo[i], ode_prec).mul(DI.from_ratio(3, 2, ode_prec), ode_prec), ode_prec).add(eps_c, ode_prec) for i in range(4)]
        ok_cr = False
        f_cr = None
        for _ in range(12):
            f_cr = eval_rhs_point(Y_cross, b_A2, B_A2, C_top_PS, c_yt_PS, d_yt_PS, ode_prec)
            P_cr = [y_lo[i].add(dt_rem.mul(f_cr[i], ode_prec), ode_prec) for i in range(4)]
            if all(Y_cross[i].contains(P_cr[i]) for i in range(4)):
                L_cr = eval_jacobian_norm_inf(Y_cross, b_A2, B_A2, C_top_PS, c_yt_PS, d_yt_PS, ode_prec)
                if Dyadic.mul_directed(dt_rem.hi, L_cr, ode_prec, True) < D_ONE:
                    Y_cross = P_cr
                    f_cr = eval_rhs_point(Y_cross, b_A2, B_A2, C_top_PS, c_yt_PS, d_yt_PS, ode_prec)
                    ok_cr = True
                    break
            Y_cross = [P_cr[i].add(P_cr[i].sub(y_lo[i], ode_prec).mul(DI.from_ratio(1, 2, ode_prec), ode_prec), ode_prec).add(eps_c, ode_prec) for i in range(4)]
        assert ok_cr, "Picard crossing enclosure/contraction failed"
        # Constructive transversality at inner g_4C = g_2L crossing: d/dt(g_4C - g_2L) < 0 strictly on Y_cross!
        cross_slope = f_cr[0].sub(f_cr[1], ode_prec)
        assert cross_slope.strictly_neg(), f"Inner crossing slope not strictly negative: {cross_slope}"

        dres_dt = None
        daGUT_inv_das = None
        if with_deriv:
            # Certified variational enclosure V_cross over [dt_lo, dt_hi] (contraction L_cr * dt_rem < 1 ALREADY verified!)
            fv_lo = eval_df_vec_point(Y_cross, v_lo, b_A2, B_A2, C_top_PS, c_yt_PS, d_yt_PS, ode_prec)
            V_cross = [v_lo[i].add(dt_rem.mul(fv_lo[i], ode_prec).mul(DI.from_ratio(3, 2, ode_prec), ode_prec), ode_prec).add(eps_c, ode_prec) for i in range(4)]
            ok_vc = False
            for _ in range(12):
                fv_cr = eval_df_vec_point(Y_cross, V_cross, b_A2, B_A2, C_top_PS, c_yt_PS, d_yt_PS, ode_prec)
                Q_cr = [v_lo[i].add(dt_rem.mul(fv_cr[i], ode_prec), ode_prec) for i in range(4)]
                if all(V_cross[i].contains(Q_cr[i]) for i in range(4)):
                    V_cross = Q_cr
                    ok_vc = True
                    break
                V_cross = [Q_cr[i].add(Q_cr[i].sub(v_lo[i], ode_prec).mul(DI.from_ratio(1, 2, ode_prec), ode_prec), ode_prec).add(eps_c, ode_prec) for i in range(4)]
            assert ok_vc, "Variational Picard crossing enclosure failed"
            # Exact IFT derivative: dt_GUT/dt_PS = -(v_0 - v_1) / (f_0 - f_1)
            dtgut_dtps = V_cross[0].sub(V_cross[1], ode_prec).neg().div(cross_slope, ode_prec)
            # Exact outer shooting derivative: d(res)/dt_PS = (v_2 - v_0) + (f_2 - f_0) * (dt_GUT/dt_PS)
            dres_dt = V_cross[2].sub(V_cross[0], ode_prec).add(
                f_cr[2].sub(f_cr[0], ode_prec).mul(dtgut_dtps, ode_prec), ode_prec
            )
            if with_as_deriv:
                assert w_lo is not None
                fw_lo = eval_df_vec_point(Y_cross, w_lo, b_A2, B_A2, C_top_PS, c_yt_PS, d_yt_PS, ode_prec)
                W_cross = [w_lo[i].add(dt_rem.mul(fw_lo[i], ode_prec).mul(DI.from_ratio(3, 2, ode_prec), ode_prec), ode_prec).add(eps_c, ode_prec) for i in range(4)]
                ok_wc = False
                for _ in range(12):
                    fw_cr = eval_df_vec_point(Y_cross, W_cross, b_A2, B_A2, C_top_PS, c_yt_PS, d_yt_PS, ode_prec)
                    R_cr = [w_lo[i].add(dt_rem.mul(fw_cr[i], ode_prec), ode_prec) for i in range(4)]
                    if all(W_cross[i].contains(R_cr[i]) for i in range(4)):
                        W_cross = R_cr
                        ok_wc = True
                        break
                    W_cross = [R_cr[i].add(R_cr[i].sub(w_lo[i], ode_prec).mul(DI.from_ratio(1, 2, ode_prec), ode_prec), ode_prec).add(eps_c, ode_prec) for i in range(4)]
                assert ok_wc, "Variational alpha_s Picard crossing enclosure failed"
                # Exact 2x2 Cramer's rule IFT total derivative d(a_GUT^-1)/d(alpha_s) via g_2L* = g_4C*
                # (eliminates 13x g_4C cancellation: both terms in dt_GUT*/d(alpha_s) have identical sign!):
                w01 = W_cross[0].sub(W_cross[1], ode_prec)
                w02 = W_cross[0].sub(W_cross[2], ode_prec)
                v01 = V_cross[0].sub(V_cross[1], ode_prec)
                v20 = V_cross[2].sub(V_cross[0], ode_prec)
                dtgut_das_p = w01.neg().div(cross_slope, ode_prec)
                dres_das = W_cross[2].sub(W_cross[0], ode_prec).add(
                    f_cr[2].sub(f_cr[0], ode_prec).mul(dtgut_das_p, ode_prec), ode_prec
                )
                dtps_das_tot = dres_das.neg().div(dres_dt, ode_prec)
                dtgut_das_tot = w01.mul(v20, ode_prec).add(w02.mul(v01, ode_prec), ode_prec).div(
                    cross_slope.neg().mul(dres_dt, ode_prec), ode_prec
                )
                dg2L_das_tot = W_cross[1].add(V_cross[1].mul(dtps_das_tot, ode_prec), ode_prec).add(
                    f_cr[1].mul(dtgut_das_tot, ode_prec), ode_prec
                )
                g2L_3 = Y_cross[1].mul(Y_cross[1].sqr(ode_prec), ode_prec)
                daGUT_inv_das = four_pi.shift(1).neg().div(g2L_3, ode_prec).mul(dg2L_das_tot, ode_prec)

        t_gut = t_cur.add(DI(dt_lo, dt_hi), ode_prec)
        res = Y_cross[2].sub(Y_cross[0], ode_prec)
        a_gut_inv = four_pi.div(Y_cross[0].sqr(ode_prec), ode_prec)
        return {
            "res": res,
            "dres_dt": dres_dt,
            "daGUT_inv_das": daGUT_inv_das,
            "cross_slope": cross_slope,
            "t_gut": t_gut,
            "a_gut_inv": a_gut_inv,
            "Y_cross": Y_cross,
        }

    def certify_chain_a2_krawczyk(
        alpha_s_di: DI,
        t0_str: str,
        t1_str: str,
        bisect_iters: int = 10,
        narrow_iters: int = 4,
        sm_steps: int = 64,
        ps_step_den: int = 4,
    ) -> dict:
        """
        Full constructive variational-ODE Krawczyk certification for Chain A2 2-loop unification
        (works for BOTH point alpha_s AND continuum interval boxes alpha_s in [a_lo, a_hi]!):
          1) Brackets t_PS with strict opposite endpoint signs across ALL alpha_s in alpha_s_di;
          2) Evaluates exact variational-ODE derivative d(res)/d(t_PS) on the full box [t_a, t_b] x alpha_s_di;
          3) Verifies 0 not in d(res)/dt_PS, Krawczyk contraction q = |1 - Y * dres_dt| < 1,
             AND self-enclosure |Y * res(c)| + q * r < r — proving constructive existence & uniqueness
             of t_PS*(alpha_s) in [t_a, t_b] in CReal (0 Classical.choice, 0 LLPO)!
        """
        ta = DI.from_dec_str(t0_str, ode_prec).lo
        tb = DI.from_dec_str(t1_str, ode_prec).hi
        r0 = chain_a2_eval_certified(DI.point(ta), alpha_s_di, sm_steps=sm_steps, ps_step_den=ps_step_den)["res"]
        r1 = chain_a2_eval_certified(DI.point(tb), alpha_s_di, sm_steps=sm_steps, ps_step_den=ps_step_den)["res"]
        assert (r0.strictly_pos() and r1.strictly_neg()) or (r0.strictly_neg() and r1.strictly_pos()), (
            f"Outer bracket failed for alpha_s={alpha_s_di}: r0={r0}, r1={r1}"
        )
        inc_s = r0.strictly_neg()
        for _ in range(bisect_iters):
            tm = Dyadic.add_directed(ta, tb, ode_prec, False).shift(-1)
            rm = chain_a2_eval_certified(DI.point(tm), alpha_s_di, sm_steps=sm_steps, ps_step_den=ps_step_den)["res"]
            if rm.strictly_neg():
                if inc_s:
                    ta = tm
                else:
                    tb = tm
            elif rm.strictly_pos():
                if inc_s:
                    tb = tm
                else:
                    ta = tm
            else:
                # For continuum alpha_s box, narrow endpoints independently around straddling midpoint!
                l_hi = tm
                for _ in range(narrow_iters):
                    ml = Dyadic.add_directed(ta, l_hi, ode_prec, False).shift(-1)
                    rml = chain_a2_eval_certified(DI.point(ml), alpha_s_di, sm_steps=sm_steps, ps_step_den=ps_step_den)["res"]
                    if (inc_s and rml.strictly_neg()) or ((not inc_s) and rml.strictly_pos()):
                        ta = ml
                    else:
                        l_hi = ml
                r_lo = tm
                for _ in range(narrow_iters):
                    mr = Dyadic.add_directed(r_lo, tb, ode_prec, False).shift(-1)
                    rmr = chain_a2_eval_certified(DI.point(mr), alpha_s_di, sm_steps=sm_steps, ps_step_den=ps_step_den)["res"]
                    if (inc_s and rmr.strictly_pos()) or ((not inc_s) and rmr.strictly_neg()):
                        tb = mr
                    else:
                        r_lo = mr
                break

        # Branch A: Continuum parameter box -> Theorem 1.5(4) Monotone-Slope Richardson-Banach!
        # Since r(ta) < 0 < r(tb) and 0 < m <= dr/dt <= M on [ta, tb], T(t) = t - r(t)/M is
        # non-decreasing (T' = 1 - r'/M in [0, 1 - m/M]), maps [ta, tb] into [ta, tb]
        # (ta < T(ta) <= T(t) <= T(tb) < tb), and is a strict q = (1 - m/M)-contraction!
        # By creal_banach_fixed_point (0 Classical.choice, 0 LLPO), EVERY alpha_s in alpha_s_di
        # has a UNIQUE constructive CReal unification root t_PS*(alpha_s) in [ta, tb]!
        if not (alpha_s_di.width(ode_prec) < Dyadic(1, -40)):
            box_res = chain_a2_eval_certified(
                DI(ta, tb), alpha_s_di, with_deriv=True, with_as_deriv=True, sm_steps=sm_steps, ps_step_den=ps_step_den
            )
            df_box = box_res["dres_dt"]
            assert (inc_s and df_box.strictly_pos()) or ((not inc_s) and df_box.strictly_neg()), (
                f"Continuum Richardson-Banach derivative failed sign check: {df_box}"
            )
            daG_das = box_res["daGUT_inv_das"]
            assert daG_das is not None and daG_das.strictly_pos(), (
                f"Continuum monotonicity d(a_GUT^-1)/d(alpha_s) > 0 failed: {daG_das}"
            )
            m_d = df_box.lo if inc_s else df_box.hi.neg()
            M_d = df_box.hi if inc_s else df_box.lo.neg()
            assert D_ZERO < m_d and m_d <= M_d
            q_rb = DI_ONE.sub(DI.point(m_d).div(DI.point(M_d), ode_prec), ode_prec).hi
            assert q_rb < D_ONE
            return {
                "t_PS": DI(ta, tb),
                "t_gut": box_res["t_gut"],
                "a_gut_inv": box_res["a_gut_inv"],
                "dres_dt": df_box,
                "daGUT_inv_das": daG_das,
                "cross_slope": box_res["cross_slope"],
                "q_contr": q_rb,
                "k_rad": D_ZERO,
                "r": Dyadic.add_directed(tb, ta.neg(), ode_prec, True).shift(-1),
            }

        # Branch B: Point alpha_s -> Tight Centered Variational-ODE Krawczyk (Theorem 1.5(3))!
        c = Dyadic.add_directed(ta, tb, ode_prec, False).shift(-1).round_down(48)
        r1_d = Dyadic.add_directed(tb, c.neg(), ode_prec, True)
        r2_d = Dyadic.add_directed(c, ta.neg(), ode_prec, True)
        r = (r1_d if r1_d >= r2_d else r2_d).round_up(32)
        for _ in range(6):
            lo_k = Dyadic.add_directed(c, r.neg(), ode_prec, False)
            hi_k = Dyadic.add_directed(c, r, ode_prec, True)
            box_res = chain_a2_eval_certified(DI(lo_k, hi_k), alpha_s_di, with_deriv=True, sm_steps=sm_steps, ps_step_den=ps_step_den)
            cen_res = chain_a2_eval_certified(DI.point(c), alpha_s_di, with_deriv=True, sm_steps=sm_steps, ps_step_den=ps_step_den)
            df_box = box_res["dres_dt"]
            assert not df_box.contains_zero(), f"Outer shooting derivative straddles 0: {df_box}"
            Y_d = cen_res["dres_dt"].inv(ode_prec).midpoint(ode_prec).round_down(48)
            Y_i = DI.point(Y_d)
            q_contr = DI_ONE.sub(Y_i.mul(df_box, ode_prec), ode_prec).abs_upper()
            yfc_abs = Y_i.mul(cen_res["res"], ode_prec).abs_upper()
            k_rad = Dyadic.add_directed(yfc_abs, Dyadic.mul_directed(q_contr, r, ode_prec, True), ode_prec, True)
            if q_contr < D_ONE and k_rad < r:
                r_lo_k = chain_a2_eval_certified(DI.point(lo_k), alpha_s_di, sm_steps=sm_steps, ps_step_den=ps_step_den)["res"]
                r_hi_k = chain_a2_eval_certified(DI.point(hi_k), alpha_s_di, sm_steps=sm_steps, ps_step_den=ps_step_den)["res"]
                assert (r_lo_k.strictly_pos() and r_hi_k.strictly_neg()) or (
                    r_lo_k.strictly_neg() and r_hi_k.strictly_pos()
                )
                return {
                    "t_PS": DI(lo_k, hi_k),
                    "t_gut": box_res["t_gut"],
                    "a_gut_inv": box_res["a_gut_inv"],
                    "dres_dt": df_box,
                    "cross_slope": box_res["cross_slope"],
                    "q_contr": q_contr,
                    "k_rad": k_rad,
                    "r": r,
                }
            r = r.shift(1)
        raise AssertionError(f"Variational Krawczyk failed for alpha_s={alpha_s_di}")

    # Certify Chain A2 central value (alpha_s = 0.1180) with FULL variational-ODE Krawczyk!
    as_central = DI.from_dec_str("0.1180", ode_prec)
    kc_central = certify_chain_a2_krawczyk(as_central, "21.17", "21.20", bisect_iters=10, sm_steps=64, ps_step_den=4)
    M_PS_box = M_Z.mul(di_exp(kc_central["t_PS"], ode_prec), ode_prec)
    Lam_box = M_Z.mul(di_exp(kc_central["t_gut"], ode_prec), ode_prec)
    aGUT_inv_box = kc_central["a_gut_inv"]
    assert DI.from_dec_str("45.14", ode_prec).lo < aGUT_inv_box.lo
    assert aGUT_inv_box.hi < DI.from_dec_str("45.16", ode_prec).hi
    checks += 4

    # Certify PDG +-1sigma endpoints (0.1171 and 0.1189) AND the FULL CONTINUUM interval [0.1171, 0.1189]
    # partitioned into 9 contiguous exact rational subintervals [1171 + 2k, 1173 + 2k] / 10000 (k = 0..8)!
    kc_lo_ep = certify_chain_a2_krawczyk(DI.from_dec_str("0.1171", ode_prec), "21.22", "21.28", bisect_iters=6, sm_steps=48, ps_step_den=2)
    kc_hi_ep = certify_chain_a2_krawczyk(DI.from_dec_str("0.1189", ode_prec), "21.10", "21.16", bisect_iters=6, sm_steps=48, ps_step_den=2)
    aG_lo_s, aG_hi_s = kc_lo_ep["a_gut_inv"], kc_hi_ep["a_gut_inv"]
    checks += 2

    pdg_min_slope = None
    pdg_max_q = D_ZERO
    for k in range(9):
        a_lo_k = DI.from_ratio(1171 + 2 * k, 10000, ode_prec).lo
        a_hi_k = DI.from_ratio(1173 + 2 * k, 10000, ode_prec).hi
        as_sub = DI(a_lo_k, a_hi_k)
        # Tight exact integer-decimal search brackets tracking linear shift t_PS*(a_s) across [0.1171, 0.1189]:
        t_c_milli = 21246 - 14 * k
        t0_sub = f"{(t_c_milli - 120) // 1000}.{(t_c_milli - 120) % 1000:03d}"
        t1_sub = f"{(t_c_milli + 120) // 1000}.{(t_c_milli + 120) % 1000:03d}"
        kc_sub = certify_chain_a2_krawczyk(as_sub, t0_sub, t1_sub, bisect_iters=5, narrow_iters=3, sm_steps=48, ps_step_den=2)
        if kc_sub["q_contr"] > pdg_max_q:
            pdg_max_q = kc_sub["q_contr"]
        sl_lo = kc_sub["daGUT_inv_das"].lo
        pdg_min_slope = sl_lo if (pdg_min_slope is None or sl_lo < pdg_min_slope) else pdg_min_slope
        checks += 2  # Richardson-Banach existence/uniqueness + strict d(a_GUT^-1)/d(alpha_s) > 0!
    assert pdg_min_slope is not None and D_ZERO < pdg_min_slope
    # By constructive FTC (d(a_GUT^-1)/d(alpha_s) >= pdg_min_slope > 0 on ALL of [0.1171, 0.1189]):
    # forall alpha_s in [0.1171, 0.1189], a_GUT^-1(0.1171) <= a_GUT^-1(alpha_s) <= a_GUT^-1(0.1189)!
    pdg_hull_aG = DI(aG_lo_s.lo, aG_hi_s.hi)
    assert DI.from_dec_str("45.10", ode_prec).lo < pdg_hull_aG.lo and pdg_hull_aG.hi < DI.from_dec_str("45.20", ode_prec).hi
    checks += 1

    ln10 = di_log(DI.from_int(10), ode_prec)
    log10_MPS = kc_central["t_PS"].div(ln10, ode_prec).add(di_log(M_Z, ode_prec).div(ln10, ode_prec), ode_prec)
    log10_Lam = kc_central["t_gut"].div(ln10, ode_prec).add(di_log(M_Z, ode_prec).div(ln10, ode_prec), ode_prec)
    log10_MPS_1l = t_PS_1l.div(ln10, ode_prec).add(di_log(M_Z, ode_prec).div(ln10, ode_prec), ode_prec)
    log10_Lam_1l = t_GUT_1l.div(ln10, ode_prec).add(di_log(M_Z, ode_prec).div(ln10, ode_prec), ode_prec)

    print(f"  [4C] Chain A2 Exact 1-Loop & Certified 2-Loop Machacek-Vaughn Variational-ODE Krawczyk [T]:")
    print(f"       Exact 1-loop:  log10(M_PS) in {log10_MPS_1l.fmt(8)}, log10(Lam) in {log10_Lam_1l.fmt(8)}, a_GUT^-1 in {aGUT_inv_1l.fmt(8)}")
    print(f"       Cert 2-loop:   log10(M_PS) in {log10_MPS.fmt(8)}, log10(Lam) in {log10_Lam.fmt(8)}, a_GUT^-1 in {aGUT_inv_box.fmt(8)} [T]")
    print(f"                      M_PS in {M_PS_box.div(DI.from_int(10**11), ode_prec).fmt(6)} * 10^11 GeV, "
          f"Lam in {Lam_box.div(DI.from_int(10**15), ode_prec).fmt(6)} * 10^15 GeV")
    print(f"                      Inner crossing slope d(g4-g2L)/dt in {kc_central['cross_slope'].fmt(8)} (< 0); "
          f"Outer d(res)/dt_PS in {kc_central['dres_dt'].fmt(8)} (> 0), Krawczyk q <= {kc_central['q_contr'].to_decimal_str(6, True)} < 1 [T]")
    print(f"       PDG endpoints: a_s=0.1171 -> a_GUT^-1 in {aG_lo_s.fmt(6)} (q <= {kc_lo_ep['q_contr'].to_decimal_str(6, True)}); "
          f"a_s=0.1189 -> a_GUT^-1 in {aG_hi_s.fmt(6)} (q <= {kc_hi_ep['q_contr'].to_decimal_str(6, True)})")
    print(f"       PDG CONTINUUM: forall a_s in [0.1171, 0.1189] (9 Richardson-Banach sub-boxes, max q <= {pdg_max_q.to_decimal_str(6, True)} < 1, "
          f"min d(a_GUT^-1)/da_s >= {pdg_min_slope.to_decimal_str(4, False)} > 0):")
    print(f"                      a_GUT^-1(a_s) in {pdg_hull_aG.fmt(6)} subset [45.10, 45.20] [T]")

    return {
        "checks": checks,
        "aGUT_inv_box": aGUT_inv_box,
        "aG_lo_s": aG_lo_s,
        "aG_hi_s": aG_hi_s,
        "pdg_hull_aG": pdg_hull_aG,
        "kc_central": kc_central,
    }


# ==============================================================================
# TARGET 0: SOUNDNESS KERNEL TESTS & CONSTRUCTIVE LLPO OBSTRUCTION WITNESS
# ==============================================================================

def run_target0_kernel_and_llpo_obstruction() -> dict:
    print("=" * 88)
    print("TARGET 0: DyadicInterval Soundness Kernel & Constructive LLPO Obstruction Witness")
    print("=" * 88)
    prec = 144
    checks = 0

    # 1. Bilinear convexity multiplication across 0-straddling intervals (zero CReal sign-splitting!)
    I_a = DI(Dyadic(-3, -1), Dyadic(5, -2))  # [-1.5, 1.25]
    I_b = DI(Dyadic(-7, -2), Dyadic(3, -1))  # [-1.75, 1.5]
    P_ab = I_a.mul(I_b, prec)
    # Exact corners: (-1.5)*(-1.75)=2.625, (-1.5)*1.5=-2.25, 1.25*(-1.75)=-2.1875, 1.25*1.5=1.875
    assert P_ab.lo <= Dyadic(-9, -2) and Dyadic(21, -3) <= P_ab.hi
    checks += 1

    # 2. Certified Peano-Simpson quadrature on int_0^1 exp(x) dx = e - 1 and int_0^1 4/(1+x^2) dx = pi
    I_exp01 = integrate_simpson_certified(
        lambda x, p: di_exp(x, p), lambda x: x.exp(), D_ZERO, D_ONE, 16, prec
    )
    e_m1 = di_exp(DI_ONE, prec).sub(DI_ONE, prec)
    assert I_exp01.lo <= e_m1.hi and e_m1.lo <= I_exp01.hi and I_exp01.width(prec) < Dyadic(1, -24)

    I_pi01 = integrate_simpson_certified(
        lambda x, p: DI.from_int(4).div(DI_ONE.add(x.sqr(p), p), p),
        lambda x: Jet4.const(DI.from_int(4), x.prec).div(Jet4.const(DI_ONE, x.prec).add(x.mul(x))),
        D_ZERO, D_ONE, 32, prec,
    )
    pi_ref = di_pi(prec)
    assert I_pi01.lo <= pi_ref.hi and pi_ref.lo <= I_pi01.hi and I_pi01.width(prec) < Dyadic(1, -24)
    checks += 2

    # 3. Elementary identities: exp(log(7)) ~ 7, sqrt(2)^2 ~ 2, acos(1/2) ~ pi/3
    el7 = di_exp(di_log(DI.from_int(7), prec), prec)
    assert el7.lo <= Dyadic(7, 0) <= el7.hi and el7.width(prec) < Dyadic(1, -120)
    sq2 = DI.from_int(2).sqrt(prec).sqr(prec)
    assert sq2.lo <= Dyadic(2, 0) <= sq2.hi and sq2.width(prec) < Dyadic(1, -120)
    ac_half = di_acos(DI.point(Dyadic(1, -1)), prec)
    pi_over_3 = pi_ref.div(DI.from_int(3), prec)
    assert ac_half.lo <= pi_over_3.hi and pi_over_3.lo <= ac_half.hi and ac_half.width(prec) < Dyadic(1, -120)
    checks += 3

    # 4. Constructive LLPO countermodel f_alpha on [0, 1] (Theorem 1.C [X]):
    #    p_alpha = sum_{n>=0} (-1)^n alpha(n) 2^(-(n+2)) in [-1/4, 1/4]
    #    f_alpha(x) = 3x - 1 + p_alpha (x in [0, 1/3]), p_alpha (x in [1/3, 2/3]), 3x - 2 + p_alpha (x in [2/3, 1])
    #    Verify: for even spike n=20 (p = +2^-22 > 0), EVERY root lies in (0, 1/3) (< 1/2),
    #            for odd  spike n=21 (p = -2^-23 < 0), EVERY root lies in (2/3, 1) (> 1/2),
    #            while f_alpha(0) <= -3/4 < 0 < +3/4 <= f_alpha(1) in BOTH cases!
    def eval_llpo_f(x: DI, p_val: DI, p: int = prec) -> DI:
        t1 = DI.from_ratio(1, 3, p)
        t2 = DI.from_ratio(2, 3, p)
        if x.hi <= t1.lo:
            return DI.from_int(3).mul(x, p).sub(DI_ONE, p).add(p_val, p)
        if x.lo >= t2.hi:
            return DI.from_int(3).mul(x, p).sub(DI.from_int(2), p).add(p_val, p)
        if t1.hi <= x.lo and x.hi <= t2.lo:
            return p_val
        raise ValueError("Piecewise test point straddles kink")

    p_even = DI.point(Dyadic(1, -22))   # alpha(20) = 1
    p_odd  = DI.point(Dyadic(-1, -23))  # alpha(21) = 1
    for pv in (p_even, p_odd):
        assert eval_llpo_f(DI_ZERO, pv).hi <= Dyadic(-3, -2)  # <= -3/4 < 0
        assert eval_llpo_f(DI_ONE, pv).lo >= Dyadic(3, -2)    # >= +3/4 > 0
    # Even spike: f(x) > 0 strictly on [1/3, 1] -> root strictly < 1/3 < 1/2!
    assert eval_llpo_f(DI.point(Dyadic(1, -1)), p_even).strictly_pos()
    # Odd spike:  f(x) < 0 strictly on [0, 2/3] -> root strictly > 2/3 > 1/2!
    assert eval_llpo_f(DI.point(Dyadic(1, -1)), p_odd).strictly_neg()
    checks += 2

    print(f"  [0A] Core soundness tests: bilinear 0-straddling mul, exp(log 7), sqrt(2)^2, acos(1/2)=pi/3 [T]")
    print(f"  [0B] Peano-Simpson quadrature: int_0^1 e^x dx in {I_exp01.fmt(12)}, int_0^1 4/(1+x^2) dx in {I_pi01.fmt(12)} [T]")
    print(f"  [0C] Constructive LLPO obstruction f_alpha verified: even spike n=20 -> root < 1/3, odd spike n=21 -> root > 2/3 [X]\n")
    return {"checks": checks}


# ==============================================================================
# MAIN RUNNER + ZERO-FLOAT AUDIT
# ==============================================================================

def main():
    fast_mode = "--fast" in sys.argv[1:]
    t0 = time.perf_counter()
    # Audit: zero float/numerical library imports!
    for forbidden in ("math", "numpy", "scipy", "mpmath", "decimal"):
        assert forbidden not in sys.modules, f"Forbidden module loaded: {forbidden}"

    r0 = run_target0_kernel_and_llpo_obstruction()
    if fast_mode:
        r2 = run_target2_kallen_lehmann()
        r3 = run_target3_s4_regge_hessian_inertia()
        total_checks = r0["checks"] + r2["checks"] + r3["checks"]
    else:
        r1 = run_target1_spectral_action()
        r2 = run_target2_kallen_lehmann()
        r3 = run_target3_s4_regge_hessian_inertia()
        r4 = run_target4_r18_and_chain_a2()
        total_checks = r0["checks"] + r1["checks"] + r2["checks"] + r3["checks"] + r4["checks"]

    # Re-check forbidden modules after full run
    for forbidden in ("math", "numpy", "scipy", "mpmath", "decimal"):
        assert forbidden not in sys.modules, f"Forbidden module loaded: {forbidden}"

    dt = time.perf_counter() - t0
    mode_tag = " [FAST CI MODE]" if fast_mode else ""
    print("\n" + "=" * 88)
    print(f"FRONTIER v13 MODULE 3 (DYADIC CERTIFICATES){mode_tag}: {total_checks}/{total_checks} CHECKS PASSED (ZERO float64, ZERO math/numpy/scipy!) in {dt:.2f}s")
    print("=" * 88)


if __name__ == "__main__":
    main()
