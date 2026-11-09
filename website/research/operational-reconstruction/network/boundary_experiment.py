"""Compare synchronous fine evolution with a measured boundary impulse response."""
from itertools import product


def multiply(matrix, state):
    return tuple(sum(a * b for a, b in zip(row, state)) for row in matrix)


def trials(steps=7):
    count = delayed = 0
    # A boundary port and two hidden ports. The hidden block ranges over
    # every signed 2x2 matrix with coefficients -1, 0, 1, including cycles.
    for entries in product((-1, 0, 1), repeat=4):
        hidden = [entries[:2], entries[2:]]
        for inject in [(1, 0), (1, 1)]:
            for detect in [(1, 1), (1, -1)]:
                fine = [(0, *detect), (inject[0], *hidden[0]), (inject[1], *hidden[1])]
                echo = []
                v = inject
                for _ in range(steps):
                    echo.append(sum(a*b for a, b in zip(detect, v)))
                    v = multiply(hidden, v)
                for initial in [(1, 0, 0), (0, 1, -1)]:
                    direct = [initial[0]]
                    reduced = [initial[0]]
                    marked = initial
                    free_hidden = initial[1:]
                    for tick in range(steps):
                        marked = multiply(fine, marked)
                        direct.append(marked[0])
                        # The delayed kernel starts at two ticks from injection:
                        # one into a hidden port, one back out to the boundary.
                        forced = sum(echo[k] * reduced[tick - 1 - k] for k in range(tick))
                        reduced.append(sum(a*b for a, b in zip(detect, free_hidden)) + forced)
                        free_hidden = multiply(hidden, free_hidden)
                    assert direct == reduced
                    delayed += any(v != 0 for v in echo[1:])
                    count += 1
    assert 0 < delayed < count
    print(f'{count} signed-network trials: full boundary records agree over {steps} updates; '
          f'{delayed} have a nonzero delayed kernel beyond the first return.')


if __name__ == '__main__':
    trials()
