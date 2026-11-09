"""Enumerate four-station networks and compare physical delivery with changes of scale."""
from heapq import heappop, heappush
from itertools import combinations, product
from math import inf


def distances(graph):
    """Physical first delivery by a positive-delay event queue, one injection per source."""
    result = {}
    for source in graph:
        queue = [(0, source)]
        times = {}
        while queue:
            tick, station = heappop(queue)
            if station in times:
                continue
            times[station] = tick
            for end, delay in graph[station].items():
                if end not in times:
                    heappush(queue, (tick + delay, end))
        result[source] = times
    return result


def hide(graph, stations):
    """Splice paths through the hidden station at their actual cost (first delivery)."""
    reduced = {x: links.copy() for x, links in graph.items()}
    for h in stations:
        exits = reduced.pop(h)
        for x, links in reduced.items():
            if h not in links:
                continue
            approach = links.pop(h)
            for y, leaving in exits.items():
                if y != x:
                    links[y] = min(links.get(y, inf), approach + leaving)
    return reduced


def merge(graph, block):
    reduced = {block[x]: {} for x in graph}
    for x, links in graph.items():
        coarse = reduced[block[x]]
        for y, cost in links.items():
            dest = block[y]
            if dest != block[x]:
                coarse[dest] = min(coarse.get(dest, inf), cost)
    return reduced


def block_arrival(fine, block, x, dest):
    return min(fine[x][z] for z in fine if block[z] == dest)


def main():
    # Every labelled reciprocal graph on four vertices with each edge absent,
    # or carrying one or two ticks. Restrict the statistics to connected graphs.
    vertices = range(4)
    pairs = tuple(combinations(vertices, 2))
    connected = cyclic = retained = partitions = lifts = 0
    for costs in product(range(3), repeat=len(pairs)):
        graph = {x: {} for x in vertices}
        for (a, b), weight in zip(pairs, costs):
            if weight:
                graph[a][b] = graph[b][a] = weight
        fine = distances(graph)
        if len(fine[0]) != len(vertices):
            continue
        connected += 1
        cyclic += sum(bool(c) for c in costs) >= len(vertices)
        for i, j in pairs:
            reduced = distances(hide(graph, [i, j]))
            reverse_order = distances(hide(graph, [j, i]))
            assert reduced == reverse_order
            assert all(t == fine[x][y] for x, row in reduced.items() for y, t in row.items())
            retained += 1

            block = {x: i if x == j else x for x in vertices}
            quotient = merge(graph, block)
            coarse = distances(quotient)
            local_test = all(block_arrival(fine, block, x, dest) <= cost
                             for x in vertices for dest, cost in quotient[block[x]].items())
            all_balls = all(coarse[block[x]][dest] == block_arrival(fine, block, x, dest)
                            for x in vertices for dest in quotient)
            assert local_test == all_balls
            lifts += all_balls
            partitions += 1
            # Repeat a merge and compare with direct projection of physical links.
            next_block = {v: min(quotient) if v == max(quotient) else v for v in quotient}
            assert merge(quotient, next_block) == merge(graph, {x: next_block[block[x]] for x in vertices})
    assert 0 < lifts < partitions and 0 < cyclic < connected
    print(f'{connected} connected networks ({cyclic} cyclic); {retained} terminal eliminations; '
          f'{lifts}/{partitions} one-pair mergers preserve every reachable ball; '
          f'{partitions} direct vs successive contractions agree.')


if __name__ == '__main__':
    main()
