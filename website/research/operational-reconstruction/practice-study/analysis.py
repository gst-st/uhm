"""Frozen parallel-arm analysis. All randomized participants and scheduled trials enter."""
import argparse
import csv
import json
import math
from collections import Counter
from dataclasses import dataclass
from itertools import product
from pathlib import Path

ARMS = ('count', 'follow')
QUERIES = ('phase', 'history')
PHASES = ('inhale', 'exhale')
PARITIES = ('even', 'odd')
CELLS = tuple(product(QUERIES, PHASES, PARITIES))
REPETITIONS = 4
TRIALS = len(CELLS) * REPETITIONS
PER_ARM = 1400
ALPHA = 0.05
TAILS = 6
MARGIN = 0.10
PHASE_FLOOR = 0.65


def radii(n):
    """Hoeffding weights are 1/n per person, in one or in two arms."""
    log_budget = math.log(TAILS / ALPHA)
    return math.sqrt(log_budget / n), math.sqrt(log_budget / (2 * n))


def plan():
    difference_radius, arm_radius = radii(PER_ARM)
    # Design alternative with complete records, not an observed effect.
    phase_gap = MARGIN - difference_radius
    history_gap = 0.25 - MARGIN - difference_radius
    assay_gap = 0.85 - PHASE_FLOOR - arm_radius
    if min(phase_gap, history_gap, assay_gap) <= 0:
        power_bound = 0.0
    else:
        miss_equivalence = 2 * math.exp(-PER_ARM * phase_gap ** 2)
        miss_history = math.exp(-PER_ARM * history_gap ** 2)
        miss_assay = 2 * math.exp(-2 * PER_ARM * assay_gap ** 2)
        power_bound = max(0.0, 1 - miss_equivalence - miss_history - miss_assay)
    return {
        'participants_per_arm': PER_ARM,
        'scheduled_trials_per_person': TRIALS,
        'family_error': ALPHA,
        'one_sided_tails': TAILS,
        'difference_radius': difference_radius,
        'phase_arm_lower_radius': arm_radius,
        'phase_equivalence_margin': MARGIN,
        'history_minimum_advantage': MARGIN,
        'phase_assay_minimum': PHASE_FLOOR,
        'necessary_phase_unknown_fraction_sum_below': 2*MARGIN-2*difference_radius,
        'design_alternative': {
            'phase_count': 0.85, 'phase_follow': 0.85, 'history_difference': 0.25,
            'complete_records': True, 'joint_support_probability_lower_bound': power_bound,
        },
    }


def rows(path, required):
    """Extra named fields are metadata. Short/long rows and duplicate fields are errors."""
    with path.open(newline='', encoding='utf-8-sig') as stream:
        reader = csv.DictReader(stream, strict=True)
        fields = reader.fieldnames or []
        if not set(required) <= set(fields) or len(set(fields)) != len(fields) or '' in fields:
            raise ValueError(f'{path}: expected unique fields including {", ".join(required)}')
        for row in reader:
            if None in row or any(value is None for value in row.values()):
                raise ValueError(f'{path}:{reader.line_num}: wrong field count')
            yield row


def natural(value, field):
    if not value.isascii() or not value.isdecimal():
        raise ValueError(f'{field}: expected unsigned integer, got {value!r}')
    return int(value)


def member(value, allowed, field):
    if value not in allowed:
        raise ValueError(f'{field}: unexpected value {value!r}')
    return value


def key_of(row, roster):
    participant = row['participant']
    if participant not in roster:
        raise ValueError(f'unknown participant {participant!r}')
    trial = natural(row['trial'], 'trial')
    if not 1 <= trial <= TRIALS:
        raise ValueError(f'trial {trial} outside 1..{TRIALS}')
    return participant, trial


def read_roster(path, expected_per_arm=PER_ARM):
    roster = {}
    for row in rows(path, ['participant', 'arm']):
        person = row['participant']
        if not person or person != person.strip() or person in roster:
            raise ValueError(f'invalid or duplicate participant {person!r}')
        roster[person] = member(row['arm'], ARMS, 'arm')
    if Counter(roster.values()) != Counter({arm: expected_per_arm for arm in ARMS}):
        raise ValueError(f'frozen design requires exactly {expected_per_arm} randomized people per arm')
    return roster


@dataclass(frozen=True)
class Trial:
    query: str
    phase: str
    parity: str
    target_n: int | None


def parity_of(n):
    return PARITIES[n % 2]


def read_schedule(path, roster):
    schedule = {}
    cells = {person: Counter() for person in roster}
    for row in rows(path, ['participant', 'trial', 'query', 'target_phase', 'target_parity']):
        key = key_of(row, roster)
        if key in schedule:
            raise ValueError(f'duplicate scheduled trial {key!r}')
        query = member(row['query'], QUERIES, 'query')
        phase = member(row['target_phase'], PHASES, 'target_phase')
        parity = member(row['target_parity'], PARITIES, 'target_parity')
        target_n = None
        if 'target_n' in row:
            target_n = natural(row['target_n'], 'target_n')
            if parity != parity_of(target_n):
                raise ValueError(f'{key!r}: target count contradicts target parity')
        cells[key[0]][query, phase, parity] += 1
        schedule[key] = Trial(query, phase, parity, target_n)
    expected = Counter({cell: REPETITIONS for cell in CELLS})
    for person, design in cells.items():
        if design != expected:
            raise ValueError(f'{person!r}: unbalanced or incomplete frozen schedule')
    return schedule


KNOWN = ('correct', 'incorrect')
UNKNOWN = ('no_row', 'unusable_record', 'target_mismatch', 'no_answer')
STATUSES = KNOWN + UNKNOWN


def classify(trial, row):
    answer = member(row['answer'], ('',) + (PHASES if trial.query == 'phase' else PARITIES), 'answer')
    phase = member(row['observed_phase'], ('',) + PHASES, 'observed_phase')
    count = natural(row['completed_exhales'], 'completed_exhales') if row['completed_exhales'] else None
    if row.get('reason') == 'no_acquisition':
        if phase or count is not None or answer:
            raise ValueError('empty acquisition marked with observations')
        return 'no_row'
    if not phase or count is None:
        return 'unusable_record'
    parity = parity_of(count)
    if phase != trial.phase or parity != trial.parity or (trial.target_n is not None and count != trial.target_n):
        return 'target_mismatch'
    if not answer:
        return 'no_answer'
    truth = phase if trial.query == 'phase' else parity
    return 'correct' if answer == truth else 'incorrect'


def confidence_decision(totals):
    """Equal trial counts give each person equal weight under every missing-data completion."""
    per_query = PER_ARM * (TRIALS // len(QUERIES))
    diff_radius, arm_radius = radii(PER_ARM)
    results = {}
    intervals = {}
    phase_lower = {}
    for query in QUERIES:
        arms = {}
        means = {}
        for arm in ARMS:
            counts = totals[arm, query]
            if sum(counts.values()) != per_query:
                raise ValueError(f'{arm}/{query}: incomplete denominator')
            lo = counts['correct'] / per_query
            hi = (per_query - counts['incorrect']) / per_query
            means[arm] = lo, hi
            arms[arm] = {'observed_mean_bounds': [lo, hi],
                         'counts': {s: counts[s] for s in STATUSES}}
            if query == 'phase':
                phase_lower[arm] = max(0.0, lo - arm_radius)
        lo = means['count'][0] - means['follow'][1]
        hi = means['count'][1] - means['follow'][0]
        interval = [max(-1.0, lo - diff_radius), min(1.0, hi + diff_radius)]
        results[query] = {'arms': arms, 'difference_count_minus_follow_bounds': [lo, hi],
                          'simultaneous_confidence_interval': interval}
        intervals[query] = interval

    plo, phi = intervals['phase']
    hlo, hhi = intervals['history']
    assay_pass = all(x > PHASE_FLOOR for x in phase_lower.values())
    if -MARGIN < plo and phi < MARGIN and hlo > MARGIN and assay_pass:
        decision = 'supported'
    elif phi <= -MARGIN or plo >= MARGIN or hhi <= MARGIN:
        decision = 'incompatible'
    else:
        decision = 'inconclusive'
    missing_width = sum((bounds[1] - bounds[0]) for bounds in
                        (results['phase']['arms'][arm]['observed_mean_bounds'] for arm in ARMS))
    return {'phase_equivalence_possible_by_width': missing_width + 2*diff_radius < 2*MARGIN,
            'decision': decision, 'phase_assay_passed': assay_pass,
            'phase_arm_simultaneous_lower_bounds': phase_lower, 'outcomes': results,
            'interaction_interval_from_joint_bounds': [hlo - phi, hhi - plo]}


def analyze(roster_file, schedule_file, observed_file):
    roster = read_roster(roster_file)
    schedule = read_schedule(schedule_file, roster)
    seen = {}
    for row in rows(observed_file, ['participant', 'trial', 'observed_phase', 'completed_exhales', 'answer']):
        key = key_of(row, roster)
        if key in seen:
            raise ValueError(f'duplicate observation {key!r}')
        seen[key] = classify(schedule[key], row)
    totals = {(arm, q): Counter() for arm in ARMS for q in QUERIES}
    for key, trial in schedule.items():
        totals[roster[key[0]], trial.query][seen.get(key, 'no_row')] += 1
    reported = {person for (person, _), status in seen.items() if status != 'no_row'}
    absent = Counter(arm for person, arm in roster.items() if person not in reported)
    return {**confidence_decision(totals), 'plan': plan(),
            'participants_without_any_row': {arm: absent[arm] for arm in ARMS}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--plan', action='store_true')
    parser.add_argument('files', metavar='CSV', nargs='*', type=Path,
                        help='randomization roster, frozen schedule, adjudicated observations')
    args = parser.parse_args()
    if args.plan and not args.files:
        result = plan()
    elif not args.plan and len(args.files) == 3:
        try:
            result = analyze(*args.files)
        except (OSError, ValueError, csv.Error) as error:
            parser.exit(2, f'analysis error: {error}\n')
    else:
        parser.error('choose --plan or supply exactly roster.csv schedule.csv observations.csv')
    print(json.dumps(result, indent=2, sort_keys=True, allow_nan=False))


if __name__ == '__main__':
    main()
