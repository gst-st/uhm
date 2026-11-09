"""Exact polynomial certificates for the resource bounds in feedback.md. Requires SymPy."""
from itertools import product
from math import comb
import sympy as sp

d, p, y, mu = sp.symbols("d p y mu")
t = d - 1
D = 1 + t*y**2
g = mu + (1-mu)*t*y**3/D
q = (1+t*g)/d
p_from_y = (1+t*y)/d
y_from_p = (d*p-1)/t


def polynomial_in_p(expr):
    return sp.cancel(expr.subs(y, y_from_p)).expand()


def bernstein(expr, degree):
    power = sp.Poly(polynomial_in_p(expr), p)
    assert power.degree() <= degree
    return [sp.factor(sum(power.nth(k)*sp.Rational(comb(j, k), comb(degree, k))
                          for k in range(j+1))) for j in range(degree+1)]


def verify():
    # Coefficient comparisons here are polynomial identities, not a grid in d or mu.
    assert sp.gcd(sp.Poly(sp.cancel(q*D), y), sp.Poly(D, y)).degree() == 0
    expected_D = [d/t, d/(3*t), d/3, d]
    Ds = bernstein(D, 3)
    assert all(sp.cancel(a-b) == 0 for a, b in zip(Ds, expected_D))
    As = bernstein(q*D, 3)
    threshold = (2*d-3)/((d-1)*(d+3))
    assert sp.factor(As[2] - (d-1)*(d+3)*(mu-threshold)/(3*d)) == 0
    # For d>=3 and 0<=mu<=1 every other inequality 0<=Ai<=Di follows
    # from positivity at both endpoints. Verify coefficient signs in z=d-3.
    z = sp.symbols("z")
    def nonnegative(expr):
        num, den = sp.fraction(sp.factor(expr.subs(d,z+3)))
        return (all(c >= 0 for c in sp.Poly(num,z).all_coeffs()) and
                all(c >= 0 for c in sp.Poly(den,z).all_coeffs()) and den.subs(z,0)>0)
    for j in range(4):
        for u in [0,1]:
            if j != 2 or u == 1:
                assert nonnegative(As[j].subs(mu,u))
            assert nonnegative((Ds[j]-As[j]).subs(mu,u))
            assert nonnegative(d-Ds[j])
    # h(0)=1, h(1)=(d-1)/2. All quartic weights work even for zero gain.
    h = 1 + ((d-1)/2-1)*p_from_y
    for mass in (q*D*h,(1-q)*D*h,d*(d-1)/2-D*h):
        for a in bernstein(mass,4):
            for u in [0,1]:
                assert nonnegative(a.subs(mu,u))
    # Independent operational check: enumerate ordered binary outcomes on
    # the d=7 board (three independent input states). Preserve the failure branch.
    target = (165,74,228,1656)
    success = (294,98,588,1764)
    for Y in (sp.S.Zero,sp.Rational(1,2),sp.S.One):
        P = (1+6*Y)/7
        masses = [0,0,0]
        for bits in product((0,1), repeat=3):
            j = sum(bits)
            prob = P**j*(1-P)**(3-j)
            for i, weight in enumerate((target[j],success[j]-target[j],1764-success[j])):
                masses[i] += prob*weight/1764
        assert sum(masses) == 1
        assert masses[0]+masses[1] == (1+6*Y**2)/7
        assert masses[0]/(masses[0]+masses[1]) == q.subs({y:Y,d:7,mu:sp.Rational(1,2)})
    # Six distinct physical inputs suffice to rule out even a probabilistic
    # two-copy implementation with nonzero success on this ray. Columns are
    # coefficients of D_i * numerator(j) - A_i * success(j).
    rows = []
    for j in range(6):
        den = 7*(125+30*j*j)
        num = 4*(125+30*j*j)+18*j**3
        assert sp.Rational(num,den) == q.subs({y:sp.Rational(j,5),d:7,mu:sp.Rational(1,2)})
        rows.append([den*j**k for k in range(3)]+[-num*j**k for k in range(3)])
    det = sp.det(sp.Matrix(rows))
    assert det == -135025380000000000
    print("Exact cubic/quartic identities and endpoint signs in d-3 passed.")
    print("d=7, mu=1/2: three-copy branches normalized; two-copy determinant",det)


if __name__ == "__main__":
    if not __debug__:
        raise SystemExit("Run without -O to execute the symbolic checks.")
    verify()
