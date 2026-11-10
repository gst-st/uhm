"""Reconstruct scored observation inputs from delivered cues and two blind belt readings."""
import argparse
from bisect import bisect_right
import csv
import os
from pathlib import Path
import sqlite3
import tempfile

from analysis import PARITIES, PHASES, QUERIES, TRIALS, member, natural, parity_of, rows

GUARD_MS = 150
ANSWER_WINDOW_MS = 5000
TARGET_COUNTS = frozenset((3, 4, 5, 6, 8, 9, 10, 11))
OUTPUT = ('participant', 'trial', 'observed_phase', 'completed_exhales', 'answer', 'elapsed_ms', 'reason')


def trial_key(row):
    person = row['participant']
    trial = natural(row['trial'], 'trial')
    if not person or person != person.strip() or not 1 <= trial <= TRIALS:
        raise ValueError(f'invalid trial key: {(person, trial)!r}')
    return person, trial


def targets(path):
    plan = {}
    for row in rows(path, ['participant', 'trial', 'query', 'target_phase', 'target_parity', 'target_n']):
        key = trial_key(row)
        if key in plan:
            raise ValueError(f'duplicate scheduled trial: {key!r}')
        query = member(row['query'], QUERIES, 'query')
        phase = member(row['target_phase'], PHASES, 'target_phase')
        parity = member(row['target_parity'], PARITIES, 'target_parity')
        n = natural(row['target_n'], 'target_n')
        if n not in TARGET_COUNTS or parity_of(n) != parity:
            raise ValueError(f'{key!r}: invalid target count/parity')
        plan[key] = (query, phase, n)
    if not plan:
        raise ValueError('empty schedule')
    return plan


def raw_rows(path, ids, landmark):
    columns = ['participant', 'trial', 'kind', 'timestamp_ms', 'rater' if landmark else 'value']
    for row in rows(path, columns):
        key = trial_key(row)
        if key not in ids:
            raise ValueError(f'{path}: unscheduled trial {key!r}')
        stamp = natural(row['timestamp_ms'], 'timestamp_ms')
        if stamp >= 2**63:
            raise ValueError(f'{path}: timestamp outside SQLite integer range')
        if landmark:
            kind = member(row['kind'], PHASES + ('artifact',), 'kind')
            rater = member(row['rater'], ('a', 'b'), 'rater')
            yield ids[key], rater, stamp, kind
        else:
            kind = member(row['kind'], ('anchor', 'cue', 'answer', 'end'), 'kind')
            value = row['value']
            if kind == 'answer':
                member(value, PHASES + PARITIES, 'answer')
            elif kind == 'cue':
                member(value, ('','unverified') + QUERIES, 'displayed query')
            elif value:
                raise ValueError(f'{path}: unexpected value for {kind!r} in {key!r}')
            yield ids[key], kind, stamp, value


def phase_and_count(marks, anchor, cue):
    """Only the bracket from the last onset at/before anchor to the first after cue is used."""
    if not marks:
        return None, 'missing_landmarks'
    onsets = [(t, kind) for t, kind in marks if kind in PHASES]
    times = [t for t, _ in onsets]
    start = bisect_right(times, anchor) - 1
    current = bisect_right(times, cue) - 1
    after = current + 1
    if start < 0 or after == len(times):
        return None, 'unbracketed'
    if any(kind == 'artifact' and times[start] <= t <= times[after] for t, kind in marks):
        return None, 'artifact'
    # Multiple onsets at one tick within the bracket fail even if bisect selected
    # only the later of two competing labels at the left edge.
    active = [(t, kind) for t, kind in onsets if times[start] <= t <= times[after]]
    if any(t1 == t2 or k1 == k2 for (t1, k1), (t2, k2) in zip(active, active[1:])):
        return None, 'nonalternating'
    if min(anchor-times[start], times[start+1]-anchor, cue-times[current], times[after]-cue) < GUARD_MS:
        return None, 'boundary_guard'
    if onsets[start][1] != 'inhale':
        return None, 'anchor_not_inhale'
    completed = sum(kind == 'inhale' for t, kind in active if anchor < t < cue)
    return (onsets[current][1], completed), 'ok'


def reconstruct(key, target, events, raters):
    """Return all assigned trials; keep consensus truth even on timeouts and target mismatches."""
    query, phase, count = target
    record = dict.fromkeys(OUTPUT, '')
    record['participant'], record['trial'] = key
    if not events and not any(raters.values()):
        record['reason'] = 'no_acquisition'
        return record
    # An impossible timestamp ordering or mismapped button is an import error.
    times = [events[k][0] for k in ('anchor', 'cue', 'answer', 'end') if k in events]
    for earlier, later in zip(times, times[1:]):
        if earlier > later:
            raise ValueError(f'{key!r}: out-of-order event times')
    if 'answer' in events:
        member(events['answer'][1], PHASES if query == 'phase' else PARITIES, 'answer')
    for needed in ('anchor', 'cue'):
        if needed not in events:
            record['reason'] = 'missing_' + needed
            return record
    anchor, cue = events['anchor'][0], events['cue'][0]
    if cue <= anchor:
        raise ValueError(f'{key!r}: cue must follow anchor')
    record['elapsed_ms'] = cue-anchor
    if events['cue'][1] and events['cue'][1] != query:
        record['reason'] = 'wrong_or_unverified_question'
        return record
    reason = 'no_answer'
    if 'answer' in events:
        answer_time, answer = events['answer']
        if answer_time <= cue:
            raise ValueError(f'{key!r}: answer must follow cue')
        if answer_time - cue <= ANSWER_WINDOW_MS:
            record['answer'] = answer
            reason = 'ok'
        else:
            reason = 'late_answer'
    observations = []
    for rater in ('a', 'b'):
        result, quality = phase_and_count(raters[rater], anchor, cue)
        if result is None:
            record['reason'] = f'{quality}_{rater}'
            return record
        observations.append(result)
    if observations[0] != observations[1]:
        record['reason'] = 'rater_disagreement'
        return record
    record['observed_phase'], record['completed_exhales'] = observations[0]
    record['reason'] = 'target_mismatch' if observations[0] != (phase, count) else reason
    return record


def measure(schedule_file, events_file, landmarks_file, out_file):
    """Accept arbitrarily interleaved raw rows; disk-backed grouping bounds memory per trial."""
    schedule_file, events_file, landmarks_file, out_file = map(Path, (schedule_file, events_file, landmarks_file, out_file))
    if out_file.resolve() in {p.resolve() for p in (schedule_file, events_file, landmarks_file)}:
        raise ValueError('output would replace an input')
    plan = targets(schedule_file)
    ids = {key: i for i, key in enumerate(plan)}
    with tempfile.TemporaryDirectory() as tmp:
        db = sqlite3.connect(Path(tmp) / 'recorder.sqlite')
        staged = None
        try:
            db.execute('CREATE TABLE events (trial INTEGER, kind TEXT, ms INTEGER, value TEXT, PRIMARY KEY(trial,kind)) WITHOUT ROWID')
            db.execute('CREATE TABLE marks (trial INTEGER, rater TEXT, ms INTEGER, kind TEXT, PRIMARY KEY(trial,rater,ms,kind)) WITHOUT ROWID')
            try:
                db.executemany('INSERT INTO events VALUES (?,?,?,?)', raw_rows(events_file, ids, False))
                db.executemany('INSERT INTO marks VALUES (?,?,?,?)', raw_rows(landmarks_file, ids, True))
            except sqlite3.IntegrityError as err:
                raise ValueError('duplicate event kind or duplicate annotation in a trial') from err
            with tempfile.NamedTemporaryFile(mode='w', newline='', encoding='utf-8', dir=out_file.parent,
                                             suffix='.csv', delete=False) as output:
                staged = Path(output.name)
                writer = csv.DictWriter(output, fieldnames=OUTPUT)
                writer.writeheader()
                for key, target in plan.items():
                    trial = ids[key]
                    events = {k: (t,v) for k,t,v in db.execute('SELECT kind,ms,value FROM events WHERE trial=?', (trial,))}
                    raters = {'a': [], 'b': []}
                    for rater, t, kind in db.execute('SELECT rater,ms,kind FROM marks WHERE trial=? ORDER BY rater,ms,kind', (trial,)):
                        raters[rater].append((t,kind))
                    writer.writerow(reconstruct(key, target, events, raters))
            os.replace(staged, out_file)
        finally:
            db.close()
            if staged is not None:
                staged.unlink(missing_ok=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    for field in ('schedule', 'events', 'landmarks', 'observations'):
        parser.add_argument(field, type=Path)
    options = parser.parse_args()
    try:
        measure(options.schedule, options.events, options.landmarks, options.observations)
    except (ValueError, csv.Error, OSError) as err:
        parser.exit(2, f'{err}\n')
