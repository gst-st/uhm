"""Exact finite witnesses for G3 and G5b. Run with Python 3, standard library only."""

from fractions import Fraction
from itertools import combinations


def check_dense_site():
    # Subalgebras of M₂(C), encoded by their Pauli bases. C*(X) and C*(Z)
    # intersect in the scalars. Inclusion of the basis sets gives the order.
    scalar = frozenset({"I"})
    contexts = [scalar, scalar | {"X"}, scalar | {"Z"}]
    covers = 0
    for context in contexts:
        below = [v for v in contexts if v <= context]
        for size in range(len(below) + 1):
            for chosen in combinations(below, size):
                sieve = set(chosen)
                if any(v <= w and v not in sieve for w in sieve for v in below):
                    continue
                dense = all(any(w <= v for w in sieve) for v in below)
                assert dense == (scalar in sieve)
                covers += dense
    assert covers == 5

    # The two characters of each nonscalar context agree on the scalar cover.
    for observable in ("X", "Z"):
        characters = [{"I": 1, observable: sign} for sign in (-1, 1)]
        restrictions = [{key: c[key] for key in scalar} for c in characters]
        assert characters[0] != characters[1] and restrictions[0] == restrictions[1]
    print("Dense site: 3 actual contexts, 5 dense sieves; scalar covers fail spectral separation.")


LINES = [(i, (i + 1) % 7, (i + 3) % 7) for i in range(7)]


def check_fano_readout():
    incidence = [[int(i in line) for i in range(7)] for line in LINES]
    for i in range(7):
        for j in range(7):
            gram = sum(row[i] * row[j] for row in incidence)
            assert gram == 2 * (i == j) + 1
    # For K_l = Π_l/√3, q = Bp/3. Testing the inverse on every vertex of
    # the probability simplex establishes it for all populations by affinity.
    for j in range(7):
        q = [Fraction(row[j], 3) for row in incidence]
        assert sum(q) == 1
        recovered = [(3 * sum(row[i] * prob for row, prob in zip(incidence, q)) - 1) / 2
                     for i in range(7)]
        assert recovered == [int(i == j) for i in range(7)]
    print("Fano readout: BᵀB = 2I + 11ᵀ; all 7 simplex vertices reconstructed exactly.")


# Matrix entries below are Gaussian integers divided by the common trace 84.
DENOMINATOR = 84


def multiply(z, w):
    a, b = z
    c, d = w
    return (a * c - b * d, a * d + b * c)


def active_entry(i, j):
    if i == j:
        return (12, 0)
    if (i, j) == (0, 1):
        return (0, 1)
    if (i, j) == (1, 0):
        return (0, -1)
    return (1, 0)


def expectation(state, terms, effect_denominator=1):
    # Each term gives (i, j, numerator of E_ij); tr(Eρ) uses ρ_ji.
    products = [multiply(z, state[j][i]) for i, j, z in terms]
    assert sum(im for _, im in products) == 0
    return Fraction(sum(re for re, _ in products), DENOMINATOR * effect_denominator)


def check_phase_pair():
    rho = [[active_entry(i, j) for j in range(7)] for i in range(7)]
    conjugate = [[(re, -im) for re, im in row] for row in rho]
    for state in (rho, conjugate):
        assert sum(state[i][i][0] for i in range(7)) == DENOMINATOR
        for i, row in enumerate(state):
            for j, (re, im) in enumerate(row):
                assert (re, -im) == state[j][i]
            # Hermiticity and strictly positive Gershgorin lower bounds give
            # positive definiteness. |Re z| + |Im z| is an upper bound for |z|.
            radius = sum(abs(re) + abs(im) for j, (re, im) in enumerate(row) if i != j)
            assert row[i][0] - radius > 0

    for line_index, (i, j, k) in enumerate(LINES):
        products = [multiply(multiply(s[i][j], s[j][k]), s[k][i]) for s in (rho, conjugate)]
        assert products == ([(0, 1), (0, -1)] if line_index == 0 else [(1, 0), (1, 0)])

    # Node basis is e₀, e₁, ..., e₇; the active index i embeds as i+1.
    # 0 ⊕ ρ is trace-one and PSD in dimension 8, full rank on its active block.
    embedded = []
    for state in (rho, conjugate):
        embedded.append([[(0, 0)] * 8] + [[(0, 0)] + row for row in state])
    # Coordinate projectors and the projectors onto (e_i+e_j)/√2 span
    # all real symmetric 8×8 observables, including every real Mermin–Peres effect.
    for i in range(8):
        probe = [(i, i, (1, 0))]
        assert expectation(embedded[0], probe) == expectation(embedded[1], probe)
    for i, j in combinations(range(8), 2):
        probe = [(k, l, (1, 0)) for k in (i, j) for l in (i, j)]
        assert expectation(embedded[0], probe, 2) == expectation(embedded[1], probe, 2)

    quadrature = [(1, 2, (0, 1)), (2, 1, (0, -1))]
    means = [expectation(s, quadrature) for s in embedded]
    assert means == [Fraction(1, 42), Fraction(-1, 42)]
    # The positive-eigenvalue projector is |v><v| for v=(e₁−i e₂)/√2.
    # Its Born probability is the quadratic form v*ρv.
    phase_projector = [(1, 1, (1, 0)), (2, 2, (1, 0))] + quadrature
    probabilities = [expectation(s, phase_projector, 2) for s in embedded]
    assert probabilities == [Fraction(13, 84), Fraction(11, 84)]
    print(f"Phase pair: opposite first Fano angles; 36 real probes agree in 8D; "
          f"quadrature means {means[0]}, {means[1]} (gap {means[0] - means[1]}); "
          f"positive-outcome probabilities {probabilities[0]}, {probabilities[1]}.")


if __name__ == "__main__":
    if not __debug__:
        raise SystemExit("Run without -O to enable the exact checks.")
    check_dense_site()
    check_fano_readout()
    check_phase_pair()
