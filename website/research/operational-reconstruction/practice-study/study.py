"""Bind allocation, probe order and analysis to externally recorded pre-outcome commitments."""
import argparse
import csv
from collections import Counter
import hashlib
import hmac
import json
from pathlib import Path
import shutil
import tempfile

import analysis
from measure import measure
from timing import clock_diagnostic

HERE = Path(__file__).resolve().parent
SITE = HERE.parents[2]
COUNTS = {'even': (4, 6, 8, 10), 'odd': (3, 5, 9, 11)}
PROTOCOL = 'breath-observers/1'
PILOT_PER_ARM = 20
PILOT_UNKNOWN_MAX = 6
SOURCES = [HERE / name for name in ('study.py', 'analysis.py', 'measure.py', 'acquisition.py', 'timing.py', 'README.md')]
SOURCES += [HERE.parent / 'network' / name for name in ('BreathPractice.lean', 'PracticeChannels.lean', 'BreathPractice.vr', 'BreathTrace.vr', 'PracticeDecision.lean', 'PracticeDecision.vr')]


def digest(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def code_hashes():
    return {str(path.relative_to(SITE)): digest(path) for path in SOURCES}


def tag(secret, *values):
    # Canonical, separated fields protect the independence of the two keyed orders.
    return hmac.digest(secret, json.dumps(values, separators=(',', ':')).encode('ascii'), 'sha256')


def trials_for(person, secret):
    slots = [(q, phase, parity, count) for q, phase, parity in analysis.CELLS for count in COUNTS[parity]]
    return sorted(slots, key=lambda slot: tag(secret, 'probe-order', person, *slot))


def write_csv(path, fields, data):
    with path.open('x', encoding='utf-8', newline='') as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerow(fields)
        writer.writerows(data)


def lock(ids_path, key_path, directory, *, pilot=False):
    per_arm = PILOT_PER_ARM if pilot else analysis.PER_ARM
    id_digest = digest(ids_path)
    secret = key_path.read_bytes()
    if len(secret) != 32:
        raise ValueError('expected exactly 32 random bytes in the allocation key')
    ids = sorted(r['participant'] for r in analysis.rows(ids_path, ['participant']))
    if len(ids) != 2 * per_arm or len(set(ids)) != len(ids):
        raise ValueError('one unique ID per randomized participant is required')
    if any(not p or p.strip() != p or not p.isascii() or not p.replace('-', '').replace('_', '').isalnum() for p in ids):
        raise ValueError('use pseudonymous ASCII IDs containing letters, digits, hyphens or underscores')
    ranked = sorted(ids, key=lambda p: tag(secret, 'allocation', p))
    count_arm = set(ranked[:per_arm])
    # Concealed, balanced button order within each assigned practice.
    reversed_buttons = set()
    for group in (ranked[:per_arm], ranked[per_arm:]):
        reversed_buttons.update(sorted(group, key=lambda p: tag(secret,'buttons',p))[:len(group)//2])
    source_digests = code_hashes()
    directory.mkdir(mode=0o700, exist_ok=False)
    # Publish the commitment last; an incomplete allocation has no valid manifest.
    roster, schedule = (directory / name for name in ('roster.csv', 'schedule.csv'))
    write_csv(roster, ('participant','arm','buttons'),
              ((p,'count' if p in count_arm else 'follow','reversed' if p in reversed_buttons else 'normal') for p in ids))
    write_csv(schedule, ('participant', 'trial', 'query', 'target_phase', 'target_parity', 'target_n'),
              ((p, trial, *slot) for p in ids for trial, slot in enumerate(trials_for(p, secret), 1)))
    if digest(ids_path) != id_digest:
        raise ValueError('enrolment file changed during allocation')
    manifest = dict(protocol=PROTOCOL, stage='pilot' if pilot else 'confirmatory', sources=source_digests, key_sha256=hashlib.sha256(secret).hexdigest(),
                    participant_file=id_digest, roster=digest(roster), schedule=digest(schedule))
    path = directory / 'manifest.json'
    path.write_text(json.dumps(manifest, sort_keys=True, indent=2)+'\n', encoding='utf-8')
    return digest(path)


def verify(directory, published, *, pilot=False):
    path = directory / 'manifest.json'
    if digest(path) != published:
        raise ValueError('manifest differs from the externally recorded pre-session commitment')
    manifest = json.loads(path.read_bytes())
    if manifest['stage'] != ('pilot' if pilot else 'confirmatory'):
        raise ValueError('protocol stage mismatch')
    if (manifest['protocol'] != PROTOCOL or manifest['sources'] != code_hashes() or
            manifest['schedule'] != digest(directory/'schedule.csv') or manifest['roster'] != digest(directory/'roster.csv')):
        raise ValueError('protocol, executable analysis or assignments changed after commitment')


def results_commit(files):
    # Use role names rather than local paths; same bytes must be usable after transfer.
    return hashlib.sha256(json.dumps({name: digest(path) for name, path in files.items()},
                                    sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def verify_raw(index, root, copied, known):
    archived = set()
    for row in analysis.rows(index, ['participant', 'sha256']):
        person, sha = row['participant'], row['sha256']
        if person not in known or person in archived:
            raise ValueError('invalid raw trace index participant')
        if len(sha)!=64 or any(c not in '0123456789abcdef' for c in sha):
            raise ValueError('invalid raw trace SHA-256')
        path = root / sha
        if not path.stat().st_size or digest(path) != sha:
            raise ValueError('raw trace archive mismatch')
        archived.add(person)
    for role in ('events','landmarks','baseline'):
        if any(r['participant'] not in archived for r in analysis.rows(copied[role], ['participant'])):
            raise ValueError(f'{role}: no archived acquisition for recorded participant')


def pilot_qc(roster, schedule, observations):
    plan = analysis.read_schedule(schedule, roster)
    missing = Counter(roster[p] for (p,_), t in plan.items() if t.query == 'phase')
    seen = set()
    for r in analysis.rows(observations, ['participant','trial','reason']):
        t = analysis.key_of(r, roster)
        if t in seen or t not in plan:
            raise ValueError('duplicate or unscheduled feasibility trial')
        seen.add(t)
        if plan[t].query == 'phase' and r['reason'] == 'ok':
            missing[roster[t[0]]] -= 1
    # Sort counts so no named arm/score is released in the feasibility report.
    return {'unknown_phase_in_anonymous_groups': sorted(missing.values()),
            'phase_slots_per_group': PILOT_PER_ARM*16,
            'quality_gate_passed': max(missing.values()) <= PILOT_UNKNOWN_MAX}


def decode_events(source, destination, registry, schedule, roster):
    """Decode retained physical button edges only after the record lock."""
    mapping = {r['participant']: analysis.member(r['buttons'], ('normal','reversed'), 'buttons')
               for r in analysis.rows(registry, ['participant','buttons'])}
    plan = analysis.read_schedule(schedule, roster)
    fields = ('participant','trial','kind','timestamp_ms','value')

    def decoded():
        for row in analysis.rows(source, fields):
            key = analysis.key_of(row, roster)
            if row['kind'] == 'cue':
                row['value'] = analysis.member(row['value'], ('',) + analysis.QUERIES, 'displayed query') or 'unverified'
            if row['kind'] == 'answer':
                button = analysis.member(row['value'], ('left','right'), 'physical button')
                index = (button == 'right') ^ (mapping[key[0]] == 'reversed')
                choices = analysis.PHASES if plan[key].query == 'phase' else analysis.PARITIES
                row['value'] = choices[index]
            yield tuple(row[k] for k in fields)
    write_csv(destination, fields, decoded())


def score(directory, published, records_hash, files, raw_directory, *, pilot=False):
    verify(directory, published, pilot=pilot)
    registry = directory/'roster.csv'
    schedule = directory/'schedule.csv'
    known = analysis.read_roster(registry, PILOT_PER_ARM if pilot else analysis.PER_ARM)
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        copied = {role: Path(shutil.copyfile(path, tmp / (role+'.csv'))) for role, path in files.items()}
        if results_commit(copied) != records_hash:
            raise ValueError('data differ from the independently locked pre-unblinding records')
        verify_raw(copied['raw_index'], raw_directory, copied, known)
        out = tmp / 'observations.csv'
        decoded = tmp/'button-labels.csv'
        decode_events(copied['events'], decoded, registry, schedule, known)
        measure(schedule, decoded, copied['landmarks'], out)
        if pilot:
            result = pilot_qc(known, schedule, out)
        else:
            result = analysis.analyze(registry, schedule, out)
            result['adjudication_reasons'] = dict(Counter(r['reason'] for r in analysis.rows(out, ['reason'])))
            result['duration_only'] = clock_diagnostic(registry, schedule, out, copied['baseline'])
        verify(directory, published, pilot=pilot)
        return {**result, 'protocol_commitment': published, 'record_commitment': records_hash,
                'adjudicated_sha256': digest(out)}


def main():
    args = argparse.ArgumentParser(description=__doc__)
    sub = args.add_subparsers(required=True, dest='cmd')
    for command in ('lock','pilot-lock'):
        alloc = sub.add_parser(command)
        for name in ('participants','key','directory'):
            alloc.add_argument(name,type=Path)
    sub.add_parser('plan')
    for command in ('records-digest','analyze','pilot-qc'):
        parser = sub.add_parser(command)
        if command != 'records-digest':
            parser.add_argument('directory', type=Path)
            parser.add_argument('protocol_hash')
            parser.add_argument('records_hash')
        for name in ('events', 'landmarks', 'baseline', 'raw_index'):
            parser.add_argument(name,type=Path)
        if command != 'records-digest':
            parser.add_argument('raw_directory', type=Path)
    opt = args.parse_args()
    try:
        if opt.cmd in ('lock','pilot-lock'):
            print(lock(opt.participants, opt.key, opt.directory, pilot=opt.cmd=='pilot-lock'))
        elif opt.cmd == 'plan':
            print(json.dumps(analysis.plan(), indent=2))
        else:
            files = {role: getattr(opt, role) for role in ('events','landmarks','baseline','raw_index')}
            if opt.cmd == 'records-digest':
                print(results_commit(files))
            else:
                print(json.dumps(score(opt.directory, opt.protocol_hash, opt.records_hash, files, opt.raw_directory, pilot=opt.cmd=='pilot-qc'),
                                 indent=2, sort_keys=True, allow_nan=False))
    except (KeyError, OSError, ValueError, csv.Error) as err:
        args.exit(2, f'study error: {err}\n')


if __name__ == '__main__':
    main()
