"""Read first arrivals on growing periodic networks using only local transmission delays."""
from fractions import Fraction
from heapq import heappop, heappush


def first_arrivals(source, neighbours):
    settled = {}
    pending = [(0, source)]
    while pending:
        tick, station = heappop(pending)
        if station in settled:
            continue
        settled[station] = tick
        for target, delay in neighbours(station):
            if delay <= 0:
                raise ValueError('physical edge must have a positive delay')
            if target not in settled:
                heappush(pending, (tick + delay, target))
    return settled


def local_ring(weights):
    def edges(i):
        yield (i+1) % len(weights), weights[i]
        yield (i-1) % len(weights), weights[(i-1) % len(weights)]
    return edges


def ring_trials():
    # Offsets are integer relay delays; each cell has the same total cost four.
    max_gaps = []
    for cells in [8, 16, 32, 64]:
        left = [t for _ in range(cells) for t in (1, 3)]
        right = [t for i in range(cells) for t in ((3, 1) if i % 3 else (2, 2))]
        peak = 0
        for start in range(2*cells):
            a = first_arrivals(start, local_ring(left))
            b = first_arrivals(start, local_ring(right))
            peak = max(peak, max(abs(a[y]-b[y]) for y in a))
            for y in range(0, 2*cells, 2):
                if start % 2 == 0:
                    assert a[y] == b[y]
        assert 0 < peak <= 4
        max_gaps.append(Fraction(peak, 4*cells))
    print('Maximum pairwise discrepancy on rings (one turn = 1):',
          ', '.join(map(str, max_gaps)))


def torus(size, potential, diagonal_cost=None, shortcut=False):
    def edges(site):
        i, j = site
        moves = [(1, 0, 4), (-1, 0, 4), (0, 1, 4), (0, -1, 4)]
        if diagonal_cost is not None:
            moves.extend([(1, 1, diagonal_cost), (-1, -1, diagonal_cost)])
        for dx, dy, duration in moves:
            dest = ((i+dx) % size, (j+dy) % size)
            yield dest, duration + potential(*dest) - potential(i, j)
        if shortcut and site in ((0, 0), (size//2, 0)):
            yield ((size//2-i), 0), 1
    return edges


def torus_trials():
    peaks, direction_bias, shortcut_times = [], [], []
    pairs = 0
    for size in [8, 16, 32, 64]:
        origin, antipode = (0, 0), (size//2, 0)
        def bounded(i, j):
            return (i+2*j) % 3 - 1
        def macroscopic(i, j):
            return min(i, size-i)
        zero = lambda i, j: 0
        base = torus(size, zero)
        other = torus(size, bounded, diagonal_cost=8)
        drift = torus(size, macroscopic)
        reference, forward, drifting = (first_arrivals(origin, net) for net in [base, other, drift])
        unit = 4*size
        max_error = 0
        for x, arrival in reference.items():
            # Gradient corrections telescope even on the additional two-step diagonals.
            assert forward[x] == arrival + bounded(*x)-bounded(*origin)
            assert drifting[x] == arrival + macroscopic(*x)-macroscopic(*origin)
            max_error = max(max_error, abs(forward[x]-arrival))
        pairs += len(reference)
        peaks.append(Fraction(max_error, unit))
        back = first_arrivals(antipode, drift)[origin]
        assert drifting[antipode] + back == 2*reference[antipode]
        direction_bias.append(Fraction(drifting[antipode]-reference[antipode], unit))
        fast = first_arrivals(origin, torus(size, zero, shortcut=True))
        shortcut_times.append(Fraction(fast[antipode], unit))
        sequential = reference[(size//4, size//4)]
        simultaneous = first_arrivals(origin, torus(size, zero, diagonal_cost=4))
        assert 2*simultaneous[(size//4, size//4)] == sequential
        assert simultaneous[(size//4, 0)] == reference[(size//4, 0)]
    assert direction_bias == [Fraction(1, 8)]*4
    print(f'{pairs} torus receiver locations: bounded clock error {", ".join(map(str, peaks))}.')
    print('Identical constrained round trips, one-way bias:', ', '.join(map(str, direction_bias)))
    print('Antipodal first time with a one-tick physical shortcut:', ', '.join(map(str, shortcut_times)))


if __name__ == '__main__':
    ring_trials()
    torus_trials()
