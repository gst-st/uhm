#!/usr/bin/env python3
"""Exact finite structural-transfer controls. No symbolic-name lookup or training.

All generic functions act on integers, finite permutations, relations and graphs.
The report interprets only the explicitly selected structures. No Internet,
production mutation, probabilistic sampling, or machine-learning model is used.
"""
from collections import Counter
from itertools import combinations, permutations, product
from fractions import Fraction
from math import factorial, gcd, lcm, prod
from pathlib import Path
import argparse, hashlib, json, re, time

def arguments():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--synarc-root', type=Path,
                        default=Path(__file__).resolve().parents[3] / 'synarcai' / 'omega',
                        help='SYNARC checkout whose native Fano definitions are fingerprinted')
    parser.add_argument('--output', type=Path, default=Path(__file__).with_suffix('.json'),
                        help='JSON report path (default: next to this script)')
    return parser.parse_args()

def digest(path):
    raw = Path(path).read_bytes()
    return {'path': str(Path(path).resolve()), 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}

def lines_xor(dimension):
    return frozenset(frozenset((a, b, a ^ b)) for a, b in combinations(range(1, 1 << dimension), 2))

def graph_edges(dimension):
    return frozenset((x, x ^ (1 << bit)) for x in range(1 << dimension)
                     for bit in range(dimension) if x < (x ^ (1 << bit)))

def preserves_relation(mapping, relation):
    return frozenset(frozenset(mapping[x] for x in member) for member in relation) == relation

def preserves_graph(mapping, edges):
    return all(tuple(sorted((mapping[a], mapping[b]))) in edges for a, b in edges)

def linear_map(columns, dimension):
    out = []
    for value in range(1 << dimension):
        image = 0
        for i, column in enumerate(columns):
            if value & (1 << i): image ^= column
        out.append(image)
    return tuple(out)

def invertible_linear_maps(dimension):
    total = 1 << dimension
    return sorted({mapping for columns in product(range(1, total), repeat=dimension)
                   if len(set(mapping := linear_map(columns, dimension))) == total})

def coordinate_maps(dimension):
    return sorted({linear_map(tuple(1 << i for i in order), dimension)
                   for order in permutations(range(dimension))})

def permutation_order(mapping):
    seen = set(); lengths = []
    for start in range(len(mapping)):
        if start in seen: continue
        current = start; length = 0
        while current not in seen:
            seen.add(current); length += 1; current = mapping[current]
        assert current == start
        lengths.append(length)
    return lcm(*lengths)

def orbit(start, mapping):
    out = []; current = start
    while current not in out:
        out.append(current); current = mapping(current)
    assert current == start
    return out

def failure(mapping, relation):
    for member in sorted(map(sorted, relation)):
        image = sorted(mapping[x] for x in member)
        if frozenset(image) not in relation:
            return {'source': member, 'image': image}
    return None

def native_definition(root):
    axis_path = root / 'rust/crates/synarc-math/src/axis.rs'
    line_path = root / 'rust/crates/synarc-math/src/fano.rs'
    channel_path = root / 'rust/crates/synarc-math/src/channels.rs'
    axis = axis_path.read_text(); line = line_path.read_text()
    channels = channel_path.read_text()
    assert 'zip(fano::lines())' in channels
    assert 'd[a.index()] = 1.0' in channels
    assert 'Herm7::from_diagonal(d)' in channels
    block = re.search(r'pub enum Axis \{(.*?)\n\}', axis, re.S).group(1)
    index = {name: int(value) for name, value in re.findall(r'^\s*(\w+)\s*=\s*(\d+),', block, re.M)}
    assert sorted(index.values()) == list(range(7))
    by = re.search(r'pub\(crate\) const BY_FANO: \[Axis; N\] = \[(.*?)\];', axis, re.S).group(1)
    labels = re.findall(r'Axis::(\w+)', by)
    assert len(labels) == 7 and set(labels) == set(index)
    assert 'BY_FANO[(p + shift) % N]' in line
    assert 'Line(pick(0), pick(1), pick(3))' in line
    storage = [index[name] for name in labels]
    relation = frozenset(frozenset(storage[(p + s) % 7] for s in (0, 1, 3)) for p in range(7))
    return relation, {'scope': 'Local Rust constructor rule inspected and transcribed; no Rust execution or imported mathematical authority.',
                      'sources': [digest(p) for p in (axis_path, line_path, channel_path)],
                      'fano_number_minus_one_to_storage_index': storage,
                      'storage_lines': sorted(map(sorted, relation))}

def main():
    if not __debug__:
        raise RuntimeError('This research script requires enabled assertions; do not run with -O')
    args = arguments()
    started = time.monotonic()
    lines = lines_xor(3); edges3 = graph_edges(3)
    gl3 = invertible_linear_maps(3)
    incidence = [(0,) + p for p in permutations(range(1, 8))
                 if preserves_relation((0,) + p, lines)]
    assert len(gl3) == 168 == len(incidence)
    assert set(incidence) == set(gl3)
    assert len(lines) == 7 and all(len(x) == 3 for x in lines)
    assert all(sum(a in line and b in line for line in lines) == 1 for a, b in combinations(range(1, 8), 2))
    cube3 = [p for p in permutations(range(8)) if preserves_graph(p, edges3)]
    assert len(cube3) == 48
    both = [p for p in gl3 if preserves_graph(p, edges3)]
    coord3 = coordinate_maps(3)
    assert set(both) == set(coord3) and len(both) == 6
    assert {p for p in cube3 if p[0] == 0} == set(coord3)
    edge_colour = lambda p: all((p[x] ^ p[x ^ (1 << i)]) == (1 << i) for x in range(8) for i in range(3))
    coloured = [p for p in cube3 if edge_colour(p)]
    assert len(coloured) == 8 and len([p for p in coloured if p[0] == 0]) == 1
    non_cube = next(p for p in gl3 if p not in both)
    broken_edge = next((a, b) for a, b in sorted(edges3)
                       if tuple(sorted((non_cube[a], non_cube[b]))) not in edges3)
    translation = tuple(x ^ 1 for x in range(8))
    assert translation in cube3 and translation not in gl3 and translation[0] != 0

    native, native_report = native_definition(args.synarc_root)
    embeddings = [p for p in permutations(range(1, 8))
                  if frozenset(frozenset(p[x] for x in member) for member in native) == lines]
    assert len(embeddings) == 168
    native_report.update(storage_index_to_xor_point=list(embeddings[0]),
                         all_storage_to_xor_isomorphisms=len(embeddings),
                         distinguished_isomorphism=False)
    native_report['naive_storage_plus_one_preserves_lines'] = frozenset(frozenset(x + 1 for x in member) for member in native) == lines
    assert native_report['naive_storage_plus_one_preserves_lines'] is False

    # All generated cube-6 automorphisms are tested. The proof in the companion
    # note explains why these 64*6! candidates exhaust the automorphism group;
    # the script does not enumerate 64! permutations or GL(6,2).
    edges6 = graph_edges(6); coord6 = coordinate_maps(6); cube6 = set()
    for p in coord6:
        for offset in range(64):
            mapping = tuple(x ^ offset for x in p)
            assert preserves_graph(mapping, edges6)
            cube6.add(mapping)
    assert len(cube6) == 64 * factorial(6) == 46080
    ordered_linear = []
    for left in gl3:
        for right in gl3:
            mapping = tuple(left[x & 7] | (right[x >> 3] << 3) for x in range(64))
            if preserves_graph(mapping, edges6): ordered_linear.append(mapping)
    assert len(ordered_linear) == 36
    assert len(set(ordered_linear)) == 36
    intermix = linear_map((1, 2, 8, 4, 16, 32), 6)
    assert intermix in cube6
    assert intermix[4] == 8  # changes the ordered component allocation
    lifted = tuple(non_cube[x & 7] | ((x >> 3) << 3) for x in range(64))
    assert not preserves_graph(lifted, edges6)
    assert all(lifted[x ^ y] == (lifted[x] ^ lifted[y]) for x in range(64) for y in range(64))

    moduli = (3, 4); modulus = prod(moduli)
    assert gcd(*moduli) == 1
    crt = [(x % 3, x % 4) for x in range(modulus)]
    assert len(set(crt)) == modulus
    assert all((4 * a + 9 * b) % 12 == x for x, (a, b) in enumerate(crt))
    assert all(crt[(x + y) % 12] == ((crt[x][0] + crt[y][0]) % 3, (crt[x][1] + crt[y][1]) % 4)
               for x in range(12) for y in range(12))
    assert all(crt[(x * y) % 12] == ((crt[x][0] * crt[y][0]) % 3, (crt[x][1] * crt[y][1]) % 4)
               for x in range(12) for y in range(12))
    assert orbit((0, 0), lambda x: ((x[0] + 1) % 3, (x[1] + 1) % 4)) == crt

    line = tuple(sorted(next(iter(sorted(lines, key=lambda x: tuple(sorted(x)))))))
    complement = tuple(x for x in range(1, 8) if x not in line)
    stabilizer = [p for p in gl3 if {p[x] for x in line} == set(line)]
    assert len(stabilizer) == 24
    restrictions = {tuple(p[x] for x in complement) for p in stabilizer}
    assert restrictions == set(permutations(complement))  # faithful S4 action
    orders = dict(sorted(Counter(permutation_order(p) for p in stabilizer).items()))
    assert orders == {1: 1, 2: 9, 3: 8, 4: 6}
    assert not any(permutation_order(p) == 12 for p in gl3)
    cross = set(product(line, complement))
    assert {(p[line[0]], p[complement[0]]) for p in stabilizer} == cross
    mapping = list(range(8))
    for group in (line, complement):
        for i, x in enumerate(group): mapping[x] = group[(i + 1) % len(group)]
    mapping = tuple(mapping)
    cross_cycle = orbit((line[0], complement[0]), lambda x: (mapping[x[0]], mapping[x[1]]))
    assert permutation_order(mapping) == 12 and len(cross_cycle) == 12 and set(cross_cycle) == cross
    assert not preserves_relation(mapping, lines)
    partition_orders = Counter()
    partition_order12 = []
    for a in permutations(line):
        for b in permutations(complement):
            p = list(range(8))
            for x, y in zip(line + complement, a + b): p[x] = y
            order = permutation_order(tuple(p)); partition_orders[order] += 1
            if order == 12:
                assert not preserves_relation(p, lines)
                partition_order12.append(p)
    assert sum(partition_orders.values()) == 144 and len(partition_order12) == 12

    all_line_controls = []
    for selected in sorted(lines, key=lambda x: tuple(sorted(x))):
        group = [p for p in gl3 if {p[x] for x in selected} == selected]
        distribution = dict(sorted(Counter(permutation_order(p) for p in group).items()))
        assert len(group) == 24 and distribution == orders
        all_line_controls.append({'line': sorted(selected), 'stabilizer_order': len(group), 'element_orders': distribution})

    # A positive control against overgeneralizing the permutation obstruction.
    # Exponents represent exact powers of a primitive 12th root, not floats.
    # U has exponent4 on the 3-block, exponent3 on the 4-block. Thus Ad_U
    # multiplies every oriented cross coherence by exponent1, period12, and
    # commutes with ALL diagonal line projectors. It does not permute pairs.
    charges = {x: (4 if x in line else 3) for x in range(1, 8)}
    phase_actions = [tuple((k * (charges[a] - charges[b])) % 12 for a in range(1, 8) for b in range(1, 8))
                     for k in range(12)]
    assert len(set(phase_actions)) == 12
    assert all(phase_actions[(k + n) % 12] == tuple((a + b) % 12 for a, b in zip(phase_actions[k], phase_actions[n]))
               for k in range(12) for n in range(12))
    assert all((charges[a] - charges[b]) % 12 == 1 for a, b in cross)
    assert all((charges[a] - charges[b]) % 12 == 0 for a, b in product(line, line))
    assert all((charges[a] - charges[b]) % 12 == 0 for a, b in product(complement, complement))
    assert all((charges[a] - charges[a]) % 12 == 0 for selected in lines for a in selected)
    # Closed phase products are unchanged: the vertex charges telescope.
    assert all(((charges[a] - charges[b]) + (charges[b] - charges[c])
                + (charges[c] - charges[a])) % 12 == 0
               for a, b, c in product(range(1, 8), repeat=3))
    intersections = Counter(tuple(sorted(a & b)) for a, b in combinations(lines, 2))
    assert intersections == Counter({(x,): 3 for x in range(1, 8)})
    diagonal, modulus = Fraction(1, 7), Fraction(1, 14)
    eigenvalues = [diagonal + modulus, diagonal - modulus] + [diagonal] * 5
    assert sum(eigenvalues) == 1 and all(x > 0 for x in eigenvalues)

    report = {
        'status': 'passed', 'method': 'Exact finite enumeration and integer arithmetic; all asserts enabled.',
        'runtime_seconds': time.monotonic() - started, 'script': digest(__file__),
        'native_definition': native_report,
        'three_bit_structures': {
            'points_nonzero': list(range(1, 8)), 'lines': sorted(map(sorted, lines)),
            'linear_candidates': 7 ** 3, 'invertible_linear_maps': len(gl3),
            'all_nonzero_point_permutations_checked': factorial(7), 'all_line_automorphisms': len(incidence),
            'linear_equals_incidence_automorphisms': True, 'cube_permutations_checked': factorial(8),
            'cube_automorphisms': len(cube3), 'zero_fixed_cube_automorphisms': len(both),
            'line_and_hamming_preserving_maps': both,
            'cube_edge_colours_fixed': len(coloured), 'cube_edge_colours_and_zero_fixed': 1,
            'counterexample_line_preserving_not_cube': {'mapping_on_0_to_7': non_cube, 'edge': broken_edge,
                                                       'image': [non_cube[x] for x in broken_edge]},
            'counterexample_cube_preserving_not_linear': {'mapping_on_0_to_7': translation, 'image_of_zero': translation[0]},
            'linear_order_histogram': dict(sorted(Counter(permutation_order(p) for p in gl3).items())),
        },
        'ordered_pair_structures': {
            'cardinality': 64, 'encoding': 'x = first_component + 8 * second_component',
            'cube_dimension': 6, 'cube_edges': len(edges6), 'cube_automorphisms_checked': len(cube6),
            'cube_zero_fixed_automorphisms': len(coord6),
            'ordered_block_linear_maps_checked': len(gl3) ** 2,
            'ordered_block_linear_and_hamming_preserving': len(ordered_linear),
            'unordered_block_linear_and_hamming_preserving': 2 * len(ordered_linear),
            'all_GL6_maps_enumerated': False, 'GL6_order_from_independent_basis_formula': prod(64 - (1 << k) for k in range(6)),
            'counterexample_linear_not_hamming': {'mapping_on_0_to_63': lifted},
            'counterexample_cube_not_ordered_blocks': {'bit_permutation': [0, 1, 3, 2, 4, 5], 'input': 4, 'output': intermix[4]},
            'scope': 'Ordered binary-coordinate representation and single-coordinate-change adjacency only; no traditional names or ordering inferred.',
        },
        'coprime_cycle': {
            'modulus': 12, 'moduli': moduli, 'map': crt, 'inverse': '(4*a + 9*b) mod 12',
            'addition_pairs_checked': 144, 'multiplication_pairs_checked': 144,
            'clock_step': '(a,b) -> (a+1 mod 3,b+1 mod 4)',
            'clock_graph_degree': 2, 'cartesian_cycle_product_graph_degree': 4,
            'scope': 'Exact residues and chosen cycle origin/orientation; interpretation labels are separate.',
        },
        'line_complement': {
            'line': line, 'complement': complement, 'cross_pairs': sorted(cross),
            'line_stabilizer_order': len(stabilizer), 'complement_action_is_all_S4_and_faithful': True,
            'stabilizer_element_orders': orders, 'stabilizer_transitive_on_cross_pairs': True,
            'all_seven_line_stabilizers': all_line_controls,
            'partition_permutations_checked': 144, 'partition_order_histogram': dict(sorted(partition_orders.items())),
            'partition_order12_count': len(partition_order12), 'order12_preserving_fano_count': 0,
            'counterexample_clock_not_fano': {'point_mapping_on_0_to_7': mapping, 'cross_pair_cycle': cross_cycle,
                                             'broken_line': failure(mapping, lines)},
            'scope': 'No order-12 clock induced on cross-pairs by one Fano point automorphism; not a prohibition of an external clock, weaker bridge, or other dynamics.',
        },
        'positive_phase_clock_control': {
            'representation': 'U = zeta12^4 * P_line + zeta12^3 * (I-P_line); zeta12 primitive',
            'point_charges_mod12': charges, 'distinct_conjugation_actions': len(set(phase_actions)),
            'all144_composition_pairs_checked': True, 'all_seven_fano_projectors_preserved_pointwise': True,
            'oriented_line_to_complement_coherence_phase_step_mod12': 1,
            'within_block_coherence_phase_step_mod12': 0,
            'positive_density_example': 'I7/7 + (zeta12^k E_ab + zeta12^(-k) E_ba)/14, a in line, b in complement',
            'exact_density_eigenvalues': list(map(str, eigenvalues)),
            'all21_projector_pair_intersections': [{'point': point[0], 'multiplicity': count}
                                                  for point, count in sorted(intersections.items())],
            'unitary_normalizer': {'formula': 'U(1)^7 semidirect GL(3,2)',
                                   'target': 'Set of seven diagonal rank-three Fano line projectors only',
                                   'not_claimed_preserved': ['oriented three-form', 'octonion multiplication', 'complete UHM dynamics'],
                                   'finite_premises': {'all_projector_pairs_checked': 21, 'all_rank_one_point_projectors_generated': 7,
                                                       'all_point_permutations_checked': factorial(7), 'permitted_permutations': 168},
                                   'status': 'Analytic consequence explained in companion note; finite projector-incidence premise exhaustively checked, continuous unitary group not enumerated.',
                                   'global_phase_quotient': 'U(1)^6 semidirect GL(3,2)'},
            'observability': {
                'diagonal_projector_expectations': 'constant',
                'all_closed_phase_products': 'constant by telescoping vertex charges; all343 triangle charge sums checked',
                'two_fixed_frame_observables': ['X_ab = E_ab + E_ba', 'Y_ab = i*(E_ab - E_ba)'],
                'expectations': ['cos(2*pi*k/12)/7', 'sin(2*pi*k/12)/7'],
                'scope': 'The pair of quadratures distinguishes all12 states in a fixed frame; quotienting by arbitrary diagonal rephasing identifies this whole orbit.'},
            'scope': 'A mathematical 12-periodic state channel preserving all diagonal Fano projectors only, with no assertion about an oriented three-form, octonion multiplication or full UHM dynamics; not a 12-cycle of cross-pair positions, not evidence that symbolic meanings are learned or physically instantiated.',
        },
    }
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'status': report['status'], 'output': str(args.output), 'seconds': report['runtime_seconds'],
                      'GL3': len(gl3), 'AutQ3': len(cube3), 'intersection': len(both),
                      'AutQ6': len(cube6), 'line_stabilizer': len(stabilizer), 'order12_fano': 0}))

if __name__ == '__main__':
    main()
