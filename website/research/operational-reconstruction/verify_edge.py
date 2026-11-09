"""Finite T-355/T-358 checks and a conditional two-node construction. Run with python3.

The Fano orientation and Cartan entries reproduce fanoTriples7, cliffordGamma and
linkCartanGen in MathFoundations/ToposUHM/{OctonionSpinorCarrier,NetworkCausality}.lean.
All calculations use Python integers. A Gaussian coefficient is a (real, imag) pair.
"""

from itertools import product


def unit(n, i, j):
    return tuple(tuple(int((r, c) == (i, j)) for c in range(n)) for r in range(n))


def diagonal(entries):
    return tuple(tuple(x if i == j else 0 for j in range(len(entries)))
                 for i, x in enumerate(entries))


def multiply(a, b):
    columns = tuple(zip(*b))
    return tuple(tuple(sum(x * y for x, y in zip(row, col)) for col in columns)
                 for row in a)


def octonions():
    triples = [(1, 2, 4), (2, 3, 5), (3, 4, 6), (4, 5, 7),
               (5, 6, 1), (6, 7, 2), (7, 1, 3)]
    table = {}
    for i in range(8):
        table[0, i] = table[i, 0] = (1, i)
    for i in range(1, 8):
        table[i, i] = (-1, 0)
    for i, j, k in triples:
        for a, b, c in [(i, j, k), (j, k, i), (k, i, j)]:
            table[a, b], table[b, a] = (1, c), (-1, c)
    return triples, table


def check_one_node(triples, table):
    slots = range(8)
    left = []
    for i in slots:
        images = [table[i, c] for c in slots]
        left.append(tuple(tuple(sign if k == r else 0 for sign, k in images) for r in slots))
    # gamma_i = -L_i, so phi is minus the sum of the seven L_i L_j L_k.
    products = [multiply(multiply(left[i], left[j]), left[k]) for i, j, k in triples]
    numerator = tuple(tuple(int(i == j) - sum(t[i][j] for t in products)
                            for j in slots) for i in slots)
    assert numerator == diagonal((8, 0, 0, 0, 0, 0, 0, 0))
    projector = tuple(tuple(x // 8 for x in row) for row in numerator)
    for i, j in product(slots, repeat=2):
        assert multiply(multiply(left[i], projector), tuple(zip(*left[j]))) == unit(8, i, j)
    print("Fano multiplication: P = E00; all 64 matrix units generated.")

    cartans = [(0, 1, -1, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 1, -1, 0),
               (0, 0, 0, 0, 0, 1, 1, -2), (0, 1, 1, -2, 0, 0, 0, 0)]
    for a, h in enumerate(cartans):
        assert sum(h) == 0
        for b, k in enumerate(cartans):
            dot = sum(x * y for x, y in zip(h, k))
            assert dot > 0 if a == b else dot == 0
        witness = next(i for i in slots if h[i])
        matrix = diagonal(h)
        assert multiply(matrix, left[witness])[witness][0] == h[witness]
        assert multiply(left[witness], matrix)[witness][0] == 0
    assert [i for i in slots if all(h[i] == 0 for h in cartans)] == [0, 4]
    assert sum(t**2 * c**2 for t, c in zip(*cartans[:2])) == 0
    print("Lean Cartans: four intertwiners rejected; joint zero slots 0, 4; mixed trace 0.")


def check_two_nodes(table):
    # Choose u=e7. Each pair (a, b) spans a real plane with J=L_u,
    # J e_a=s e_b, J e_b=-s e_a. Then e_a - i s e_b is in W_(+i).
    u = 7
    flavours = [{u: (1, 0)}]
    remaining = set(range(1, u))
    while remaining:
        a = min(remaining)
        s, b = table[u, a]
        assert b != a and b in remaining and table[u, b] == (-s, a)
        flavours.append({a: (1, 0), b: (0, -s)})
        remaining.difference_update((a, b))
    assert len(flavours) == 4
    # Embed K = (F tensor 1) + (1 tensor F) in the actual 8-by-8 tensor basis.
    left = [{(i, 0): coeff for i, coeff in f.items()} for f in flavours]
    right = [{(0, i): coeff for i, coeff in f.items()} for f in flavours]
    vectors = left + right
    assert sum(len(v) for v in vectors) == len(set().union(*vectors))
    assert [{(j, i): c for (i, j), c in v.items()} for v in left] == right
    # On K, endpoint swap acts as X tensor I; colour matrix units act on flavours 1..3.
    swap = tuple(tuple(int(j == (i + 4) % 8) for j in range(8)) for i in range(8))
    t3 = (1,) * 4 + (-1,) * 4
    y = (-3, 1, 1, 1) * 2
    assert sum(y) == 0 and multiply(swap, diagonal(y)) == multiply(diagonal(y), swap)
    for a, b in product(range(1, 4), repeat=2):
        colour = tuple(tuple(int(i % 4 == a and j % 4 == b and i // 4 == j // 4)
                             for j in range(8)) for i in range(8))
        for generator in (swap, diagonal(t3), diagonal(y)):
            assert multiply(generator, colour) == multiply(colour, generator)
    colour3 = (0, 1, -1, 0) * 2
    assert sum(t**2 * c**2 for t, c in zip(t3, colour3)) == 4
    print("Encoded edge: 2 x (1 + 3), charges (-3,1,1,1) per endpoint; mixed trace 4.")

    # A kernel element acts scalarly on both irreps. On the singlet the weak
    # scalar equals z^3, so its determinant forces z^6=1. Use sixth-root exponents.
    kernel = {(c, w, z) for c, w, z in product((0, 2, 4), (0, 3), range(6))
              if (w - 3*z) % 6 == 0 and (c + w + z) % 6 == 0}
    assert kernel == {((-4*z) % 6, (3*z) % 6, z) for z in range(6)}
    print("Encoded action: central kernel Z/6.")

    # Fixed flavour, one excitation, three sites. A hopping generator kills the spectator.
    hop12 = ((0, 1, 0), (1, 0, 0), (0, 0, 0))
    hop23 = ((0, 0, 0), (0, 0, 1), (0, 1, 0))
    assert multiply(hop12, hop23) == unit(3, 0, 2)
    assert multiply(hop23, hop12) == unit(3, 2, 0)
    print("Adjacent edges: [X12, X23] = E13 - E31, so independent actions fail.")


if __name__ == "__main__":
    if not __debug__:
        raise SystemExit("Run without -O so the finite checks execute.")
    fano, multiplication = octonions()
    check_one_node(fano, multiplication)
    check_two_nodes(multiplication)
