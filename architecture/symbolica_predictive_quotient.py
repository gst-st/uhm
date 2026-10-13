#!/usr/bin/env python3
"""Exact finite strong lumpability and its coarsest stable refinement.

This implements a known finite Markov-chain mechanism, not a new theorem or a
production integration. Inputs use fractions.Fraction, never floating-point
tolerances. Mathematical guarantees concern the supplied kernel only; estimation
error, distribution shift and predictive adequacy remain separate obligations.

Run this file to check all 216 three-state kernels on the {0, 1/2, 1} grid
against all five partitions and write the companion JSON report.
"""

import argparse
from collections import Counter
from dataclasses import asdict, dataclass, is_dataclass
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, product
from pathlib import Path
from time import monotonic
import json

Matrix = tuple[tuple[Fraction, ...], ...]
Partition = tuple[tuple[int, ...], ...]


def checked_kernel(kernel) -> Matrix:
    """Validate a square stochastic kernel, with the empty matrix explicit."""
    rows = tuple(tuple(row) for row in kernel)
    size = len(rows)
    for row in rows:
        if len(row) != size:
            raise ValueError("kernel must be square")
        if any(not isinstance(value, Fraction) for value in row):
            raise TypeError("kernel entries must be Fraction values")
        if any(value < 0 or value > 1 for value in row):
            raise ValueError("kernel entries must lie in [0, 1]")
        if sum(row, Fraction(0)) != 1:
            raise ValueError("each kernel row must sum exactly to one")
    return rows


def checked_partition(partition, size: int) -> Partition:
    """Require a disjoint nonempty-block cover of range(size), then canonicalize."""
    if type(size) is not int or size < 0:
        raise ValueError("state count must be a nonnegative integer")
    blocks = tuple(tuple(block) for block in partition)
    if any(not block for block in blocks):
        raise ValueError("partition blocks must be nonempty")
    states = [state for block in blocks for state in block]
    if any(type(state) is not int or not 0 <= state < size for state in states):
        raise ValueError("partition states must be integer indices in range")
    if len(states) != size or set(states) != set(range(size)):
        raise ValueError("partition must cover each state exactly once")
    return tuple(sorted(tuple(sorted(block)) for block in blocks))


def block_probabilities(kernel: Matrix, partition: Partition) -> Matrix:
    return tuple(tuple(sum((row[state] for state in block), Fraction(0))
                       for block in partition) for row in kernel)


@dataclass(frozen=True)
class Counterexample:
    source_block: tuple[int, ...]
    left_state: int
    right_state: int
    target_block: tuple[int, ...]
    left_probability: Fraction
    right_probability: Fraction


@dataclass(frozen=True)
class Lumping:
    partition: Partition
    quotient: Matrix | None
    counterexample: Counterexample | None

    @property
    def stable(self) -> bool:
        # The empty quotient is a stable result, not a failure sentinel.
        return self.counterexample is None


def analyze(kernel, partition) -> Lumping:
    """Check equality of block sums for every pair in each source block."""
    matrix = checked_kernel(kernel)
    blocks = checked_partition(partition, len(matrix))
    sums = block_probabilities(matrix, blocks)
    for block in blocks:
        for left, right in combinations(block, 2):
            for index, target in enumerate(blocks):
                if sums[left][index] != sums[right][index]:
                    return Lumping(blocks, None, Counterexample(
                        block, left, right, target, sums[left][index], sums[right][index]))
    quotient = tuple(sums[block[0]] for block in blocks)
    return Lumping(blocks, checked_kernel(quotient), None)


@dataclass(frozen=True)
class Refinement:
    partition: Partition
    quotient: Matrix
    history: tuple[Partition, ...]
    counterexamples: tuple[Counterexample, ...]

    @property
    def strict_iterations(self) -> int:
        return len(self.history) - 1

    @property
    def block_count_increase(self) -> int:
        return len(self.history[-1]) - len(self.history[0])


def refine(kernel, partition) -> Refinement:
    """Return the unique coarsest strongly lumpable refinement of a seed.

    If a stable partition R refines the current partition, equal probabilities
    into every R-block imply equal probabilities into each union of R-blocks.
    Thus every split made here preserves R's equalities. Induction shows that
    every stable refinement of the seed refines the output. Stability at exit
    and refinement of the seed prove coarseness and uniqueness.

    Each strict step increases the block count. With n states and k seed blocks,
    strict_iterations <= block_count_increase <= n-k. This is a finite bound,
    including the explicitly admitted empty n=k=0 case.
    """
    matrix = checked_kernel(kernel)
    blocks = checked_partition(partition, len(matrix))
    history = [blocks]
    failures = []
    while True:
        result = analyze(matrix, blocks)
        if result.stable:
            assert result.quotient is not None
            return Refinement(blocks, result.quotient, tuple(history), tuple(failures))
        assert result.counterexample is not None
        failures.append(result.counterexample)
        sums = block_probabilities(matrix, blocks)
        grouped = {}
        for old_block, states in enumerate(blocks):
            for state in states:
                signature = (old_block, sums[state])
                grouped.setdefault(signature, []).append(state)
        next_blocks = checked_partition(grouped.values(), len(matrix))
        assert len(next_blocks) > len(blocks)
        blocks = next_blocks
        history.append(blocks)


def refines(finer, coarser, size: int) -> bool:
    fine = checked_partition(finer, size)
    coarse = checked_partition(coarser, size)
    block_of = {state: index for index, block in enumerate(coarse) for state in block}
    return all(len({block_of[state] for state in block}) == 1 for block in fine)


def partitions(size: int):
    """Enumerate each set partition once, via restricted-growth strings."""
    if type(size) is not int or size < 0:
        raise ValueError("state count must be a nonnegative integer")
    if size == 0:
        yield ()
        return
    labels = [0] * size

    def visit(position, maximum):
        if position == size:
            yield tuple(tuple(i for i, label in enumerate(labels) if label == group)
                        for group in range(maximum + 1))
            return
        for label in range(maximum + 2):
            labels[position] = label
            yield from visit(position + 1, max(maximum, label))

    yield from visit(1, 0)


def pushforward(distribution, partition):
    return tuple(sum((distribution[state] for state in block), Fraction(0))
                 for block in partition)


def advance(distribution, kernel):
    return tuple(sum((distribution[i] * kernel[i][j] for i in range(len(kernel))), Fraction(0))
                 for j in range(len(kernel)))


def expect_rejection(function, *arguments):
    try:
        function(*arguments)
    except (TypeError, ValueError):
        return
    raise AssertionError("malformed exact input was accepted")


def encode(value):
    if isinstance(value, Fraction):
        return str(value)
    if is_dataclass(value):
        return encode(asdict(value))
    if isinstance(value, dict):
        return {str(key): encode(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [encode(item) for item in value]
    return value


def run_controls():
    f = Fraction
    assert list(partitions(0)) == [()]
    assert len(list(partitions(1))) == 1
    assert len(list(partitions(3))) == 5
    empty = refine((), ())
    assert empty.partition == () and empty.quotient == () and empty.strict_iterations == 0
    assert analyze((), ()).stable
    assert refine(((f(1),),), ((0,),)).quotient == ((f(1),),)
    assert checked_partition(((2,), (1, 0)), 3) == ((0, 1), (2,))

    malformed_kernels = [((f(0),),), ((f(2),),), ((f(-1), f(2)), (f(0), f(1))),
                         ((f(1), f(0)),), ((1,),), ((1.0,),)]
    for kernel in malformed_kernels:
        expect_rejection(checked_kernel, kernel)
    malformed_partitions = [(((),), 0), ((), 1), (((0, 0),), 1), (((1,),), 1),
                            (((0,), (1,)), 3), (((True,),), 1), (((-1,),), 1)]
    for partition, size in malformed_partitions:
        expect_rejection(checked_partition, partition, size)

    unstable = ((f(0), f(0), f(1)), (f(0), f(1), f(0)), (f(0), f(0), f(1)))
    example_seed = ((0, 1), (2,))
    failed = analyze(unstable, example_seed)
    assert not failed.stable and failed.counterexample is not None
    repaired = refine(unstable, example_seed)
    assert repaired.partition == ((0,), (1,), (2,))
    nonidentical_rows = ((f(1, 2), f(0), f(1, 2)), (f(0), f(1, 2), f(1, 2)),
                        (f(1, 4), f(1, 4), f(1, 2)))
    stable = analyze(nonidentical_rows, example_seed)
    assert stable.quotient == ((f(1, 2), f(1, 2)), (f(1, 2), f(1, 2)))
    assert nonidentical_rows[0] != nonidentical_rows[1]

    chain = tuple(tuple(f(int(j == min(i + 1, 3))) for j in range(4)) for i in range(4))
    cascading = refine(chain, ((0, 1, 2), (3,)))
    assert cascading.history == (((0, 1, 2), (3,)), ((0, 1), (2,), (3,)), ((0,), (1,), (2,), (3,)))
    assert cascading.strict_iterations == cascading.block_count_increase == 2

    rows = [tuple(f(value, 2) for value in row) for row in product(range(3), repeat=3) if sum(row) == 2]
    choices = list(partitions(3))
    assert len(rows) == len(set(rows)) == 6
    cases = stable_seeds = failure_witnesses = stable_refinement_comparisons = 0
    distribution_steps = 0
    iteration_counts = Counter()
    for kernel in product(rows, repeat=3):
        all_results = {partition: analyze(kernel, partition) for partition in choices}
        for seed in choices:
            cases += 1
            initial = all_results[seed]
            stable_seeds += initial.stable
            if not initial.stable:
                witness = initial.counterexample
                assert witness is not None and witness.left_state in witness.source_block
                assert witness.right_state in witness.source_block
                assert witness.source_block in seed and witness.target_block in seed
                assert witness.left_probability == sum((kernel[witness.left_state][i] for i in witness.target_block), f(0))
                assert witness.right_probability == sum((kernel[witness.right_state][i] for i in witness.target_block), f(0))
                assert witness.left_probability != witness.right_probability
                failure_witnesses += 1
            result = refine(kernel, seed)
            assert refines(result.partition, seed, 3)
            assert analyze(kernel, result.partition).stable
            assert result.quotient == analyze(kernel, result.partition).quotient
            assert 0 <= result.strict_iterations <= result.block_count_increase <= 3 - len(seed)
            iteration_counts[result.strict_iterations] += 1
            assert refine(kernel, result.partition).partition == result.partition
            for candidate, diagnosis in all_results.items():
                if diagnosis.stable and refines(candidate, seed, 3):
                    assert refines(candidate, result.partition, 3)
                    stable_refinement_comparisons += 1
            # Check PC=CQ operationally, then several compositions, starting at
            # each point distribution. This uses independent distribution code.
            for state in range(3):
                raw = tuple(f(int(i == state)) for i in range(3))
                coarse = pushforward(raw, result.partition)
                for _ in range(4):
                    raw = advance(raw, kernel)
                    coarse = advance(coarse, result.quotient)
                    assert coarse == pushforward(raw, result.partition)
                    distribution_steps += 1
    assert cases == 216 * 5 == 1080
    assert stable_seeds + failure_witnesses == cases
    return {
        'exhaustive': {'states': 3, 'entry_grid': ['0', '1/2', '1'], 'stochastic_rows': len(rows),
                       'kernels': len(rows) ** 3, 'partitions_per_kernel': len(choices), 'seed_cases': cases,
                       'stable_seeds': stable_seeds, 'counterexamples_rechecked': failure_witnesses,
                       'all_stable_refinements_compared': stable_refinement_comparisons,
                       'strict_iteration_histogram': dict(sorted(iteration_counts.items())),
                       'point_distribution_steps_checked': distribution_steps,
                       'checks': ['all finite partitions enumerated', 'counterexample arithmetic',
                                  'output stability', 'refinement of seed', 'coarsest among every stable refinement',
                                  'idempotence', 'n-k bound', 'distribution pushforward commutes with transitions']},
        'empty_case': {'result': empty, 'meaning': 'The empty 0x0 kernel has no rows to normalize and the empty partition is stable. This does not provide a probability distribution on an empty state space.'},
        'rejected_malformed_cases': len(malformed_kernels) + len(malformed_partitions),
        'counterexample_and_repair': {'kernel': unstable, 'seed': example_seed, 'diagnosis': failed, 'refinement': repaired},
        'stable_with_different_rows': {'kernel': nonidentical_rows, 'seed': ((0, 1), (2,)), 'diagnosis': stable},
        'multi_iteration_example': {'kernel': chain, 'seed': ((0, 1, 2), (3,)), 'refinement': cascading},
    }


def main():
    if not __debug__:
        raise RuntimeError("run this exact control with assertions enabled, without -O")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path(__file__).with_suffix('.json'))
    arguments = parser.parse_args()
    started = monotonic()
    controls = run_controls()
    source = Path(__file__).resolve()
    report = {
        'status': 'passed', 'mechanism': 'Known finite strong lumpability and coarsest stable partition refinement',
        'novelty_claim': False, 'production_integration_claim': False,
        'arithmetic': 'fractions.Fraction; exact row normalization and block sums; no tolerance',
        'scope': 'The exact supplied finite stochastic kernel and complete seed partition only. An estimated kernel remains uncertain; these checks do not prove its statistical accuracy, stationarity or out-of-sample adequacy.',
        'proof': {'split_signature': '(old block index, probabilities into every old block)',
                  'coarseness': 'Any stable refinement R of the seed refines every iterate, because an old block is a union of R-blocks and probabilities into those R-blocks agree. The stable limit is therefore the unique coarsest stable refinement of the seed.',
                  'termination': 'Every strict iteration increases the number of blocks. Strict iterations <= total block-count increase <= n-k for n states and k initial blocks.',
                  'transport': 'Writing C for the state-to-block indicator matrix and Q for the quotient kernel, PC=CQ. This transports every initial distribution and every finite transition horizon.'},
        'script': {'path': str(source), 'bytes': source.stat().st_size, 'sha256': sha256(source.read_bytes()).hexdigest()},
        'runtime_seconds': monotonic() - started,
        **controls,
    }
    arguments.output.write_text(json.dumps(encode(report), ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'status': 'passed', 'output': str(arguments.output), 'seconds': report['runtime_seconds'], **controls['exhaustive']}))


if __name__ == '__main__':
    main()
