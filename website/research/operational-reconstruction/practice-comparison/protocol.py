"""Generate concealed schedules and bind both analyses to independent, time-stamped hashes."""
import argparse
import csv
import hashlib
import hmac
import json
from pathlib import Path
import re
import shutil
import tempfile

import score

HERE = Path(__file__).resolve().parent
PROOFS = ('PracticeModelComparison.lean', 'PracticeHoldout.lean', 'PracticeOverlap.lean',
          'SevenReadout.lean', 'PracticeComparison.vr', 'PracticeRivals.vr',
          'CapacityBudget.vr', 'CapacityControls.vr')
SCHEMAS = {'order': ('participant', 'block', 'trial', 'sequence'),
           'capacity': ('participant', 'trial', 'target', 'cue')}


def digest(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def version(study):
    base = [HERE / f for f in ('README.md', 'protocol.py', 'score.py', 'capacity_score.py')]
    base.extend(HERE.parent / 'network' / f for f in PROOFS)
    return {'design': study, 'version': 1, 'source_sha256': {p.name: digest(p) for p in base}}


def tag(secret, *parts):
    payload = json.dumps(parts, separators=(',', ':'), ensure_ascii=True).encode('ascii')
    return hmac.digest(secret, payload, 'sha256')


def schedule(study, person, secret):
    if study == 'order':
        cells = [(seq, i) for seq, n in score.DESIGN.items() for i in range(n)]
        for block in score.BLOCKS:
            cells_ranked = sorted(cells, key=lambda cell: tag(secret, study, 'slot', person, block, *cell))
            for trial, (seq, _) in enumerate(cells_ranked, 1):
                yield person, block, trial, seq
    else:
        import capacity_score
        for trial in range(1, capacity_score.TRIALS + 1):
            # Domain-separated draws. Rejection avoids bias from 256 mod 6.
            counter = 0
            while True:
                byte = tag(secret, study, 'cue', person, trial, counter)[0]
                if byte < 252:
                    break
                counter += 1
            cue = ('all', 'all', 'all', 'bit1', 'bit2', 'bit3')[byte % 6]
            word = tag(secret, study, 'stimulus', person, trial)[0] & 7
            yield person, trial, format(word, '03b'), cue


def write_csv(path, header, records):
    with path.open('x', encoding='utf-8', newline='') as stream:
        writer = csv.writer(stream, lineterminator='\n')
        writer.writerow(header)
        writer.writerows(records)


def freeze(study, participants, keyfile, dest):
    import capacity_score
    expected = score.PER_ARM if study == 'order' else capacity_score.PER_ARM
    secret = keyfile.read_bytes()
    if len(secret) != 32:
        raise ValueError('expected a fresh secret of exactly 32 random bytes')
    ids_digest = digest(participants)
    ids = [r['participant'] for r in score.rows(participants, ['participant'])]
    if (len(set(ids)) != 2 * expected or len(ids) != 2 * expected or
            any(not re.fullmatch(r'[A-Za-z0-9_\-]+', p) for p in ids)):
        raise ValueError(f'expected {2 * expected} unique ASCII pseudonyms')
    ids.sort()
    ranked = sorted(ids, key=lambda p: tag(secret, study, 'arm', p))
    count = set(ranked[:expected])
    reverse = set()
    for arm in (ranked[:expected], ranked[expected:]):
        reverse.update(sorted(arm, key=lambda p: tag(secret, study, 'buttons', p))[:expected // 2])
    manifest = version(study)
    dest.mkdir(mode=0o700, exist_ok=False)
    write_csv(dest/'roster.csv', ('participant','arm','buttons'),
              ((p, 'count' if p in count else 'follow', 'reverse' if p in reverse else 'standard') for p in ids))
    write_csv(dest/'manifest.csv', SCHEMAS[study],
              (slot for p in ids for slot in schedule(study, p, secret)))
    if digest(participants) != ids_digest:
        raise ValueError('enrolment file changed during allocation')
    manifest.update(participants=ids_digest, secret=hashlib.sha256(secret).hexdigest(),
                    roster=digest(dest/'roster.csv'), schedule=digest(dest/'manifest.csv'))
    lock = dest/'lock.json'
    lock.write_text(json.dumps(manifest, sort_keys=True, indent=2)+'\n')
    return digest(lock)


def analyze(dest, prior_hash, observations, outcome_hash):
    # Score private copies of precisely the bytes that were committed.
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        for name in ('lock.json','roster.csv','manifest.csv'):
            shutil.copyfile(dest/name, root/name)
        if digest(root/'lock.json') != prior_hash:
            raise ValueError('pre-session allocation commitment mismatch')
        lock = json.loads((root/'lock.json').read_text())
        study = lock['design']
        if (study not in SCHEMAS or any(lock.get(k) != v for k,v in version(study).items()) or
            lock['roster'] != digest(root/'roster.csv') or lock['schedule'] != digest(root/'manifest.csv')):
            raise ValueError('design version, source or allocation changed after commitment')
        shutil.copyfile(observations, root/'observations.csv')
        if digest(root/'observations.csv') != outcome_hash:
            raise ValueError('sealed observation hash mismatch')
        if study == 'order':
            scorer = score
        else:
            import capacity_score as scorer
        result = scorer.analyze(root/'roster.csv', root/'manifest.csv', root/'observations.csv')
        return {'prior_sha256': prior_hash, 'observations_sha256': outcome_hash, 'result': result}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='cmd', required=True)
    lock = commands.add_parser('freeze')
    lock.add_argument('study', choices=SCHEMAS)
    for name in ('participants','keyfile','dest'):
        lock.add_argument(name, type=Path)
    run = commands.add_parser('analyze')
    run.add_argument('dest', type=Path)
    run.add_argument('prior_hash')
    run.add_argument('observations', type=Path)
    run.add_argument('outcome_hash')
    args = parser.parse_args()
    try:
        if args.cmd == 'freeze':
            print(freeze(args.study, args.participants, args.keyfile, args.dest))
        else:
            print(json.dumps(analyze(args.dest, args.prior_hash, args.observations, args.outcome_hash),
                             sort_keys=True, indent=2, allow_nan=False))
    except (OSError, KeyError, csv.Error, ValueError) as exc:
        parser.exit(2, f'protocol error: {exc}\n')


if __name__ == '__main__':
    main()
