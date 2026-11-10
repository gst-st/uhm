"""Audit design support in public releases without analyzing participant outcomes.

Fetch once: python3 audit_open_data.py --fetch --cache /tmp/uhm-probe-public-inputs
Verify offline: python3 audit_open_data.py --cache /tmp/uhm-probe-public-inputs
Emit the structurally derived receipt instead: add --emit. Python standard library.
"""

import argparse
import collections
import csv
import hashlib
import io
import json
from pathlib import Path
import re
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET
import zipfile


HERE = Path(__file__).resolve().parent
SHA_1787 = 'ffbea891000d0d2b81f8780e57def420e4cb01a7'
SHA_3969 = '52f118f60c6c1d87d5bd9a31e1d6694f6edbd660'
ISHIKAWA = 'https://journals.plos.org/plosone/article/file?type=supplementary&id=info:doi/10.1371/journal.pone.0322537.s003'
LIMIT = 1_000_000


def sha256(b):
    return hashlib.sha256(b).hexdigest()


def checked(value, message):
    if not value:
        raise ValueError(message)


class InputCache:
    def __init__(self, root, fetch):
        self.root, self.fetch = root, fetch

    def get(self, name, url, digest=None):
        dest = self.root / name
        if not dest.exists():
            if not self.fetch:
                raise ValueError(f'missing {dest}; rerun with --fetch')
            with urlopen(Request(url, headers={'User-Agent': 'UHM-open-data-design-audit/1'}), timeout=30) as stream:
                data = stream.read(LIMIT + 1)
            checked(len(data) <= LIMIT, f'{url}: download exceeds metadata limit')
        else:
            checked(dest.stat().st_size <= LIMIT, f'{name}: unexpectedly large cached input')
            data = dest.read_bytes()
        if digest:
            checked(sha256(data) == digest, f'{name}: source SHA-256 differs')
        if not dest.exists():
            dest.parent.mkdir(parents=True, exist_ok=True)
            with dest.open('xb') as stream:
                stream.write(data)
        return data


def openneuro_questions(cache):
    root = 'OpenNeuroDatasets/ds001787'
    manifest_url = f'https://api.github.com/repos/{root}/git/trees/{SHA_1787}?recursive=1'
    raw = f'https://raw.githubusercontent.com/{root}/{SHA_1787}'
    tree = json.loads(cache.get('ds001787-tree.json', manifest_url))
    checked(tree.get('sha') == SHA_1787 and tree.get('truncated') is False, 'unexpected/incomplete ds001787 tree')
    selected = sorted((r for r in tree['tree'] if r['path'].endswith('_events.tsv')
                       or r['path'] in {'dataset_description.json', 'task-meditation_events.json'}),
                      key=lambda r: r['path'])
    inventory = ''.join(f"{r['path']}\t{r['sha']}\t{r['size']}\n" for r in selected).encode()
    inventory_digest = sha256(inventory)
    checked(inventory_digest == '12e4d76bbe3a9901b48af047a4bb0094688addcb20264e1cb56f766748b8d824',
            'inventory differs from pinned study snapshot')
    participants = set()
    types = collections.Counter()
    n_sessions = 0
    fields = ['onset', 'duration', 'trial_type', 'response_time', 'sample', 'value']
    for r in selected:
        path = r['path']
        data = cache.get('ds001787/' + path, raw+'/'+path)
        blob = hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
        checked(blob == r['sha'] and len(data) == r['size'], path+': invalid Git blob')
        if path == 'dataset_description.json':
            meta = json.loads(data)
        elif path == 'task-meditation_events.json':
            dictionary = json.loads(data)
        else:
            participants.add(path.split('/')[0])
            reader = csv.DictReader(io.StringIO(data.decode('utf-8-sig')), delimiter='\t')
            checked(reader.fieldnames == fields, path+': changed schema')
            # The actual ratings, reaction times and EEG values stay out of this audit.
            types.update(row['trial_type'] for row in reader)
            n_sessions += 1

    checked('first question' in dictionary['trial_type']['Levels']['stimulus'].lower()
            and '1, 2 or 3' in dictionary['trial_type']['Levels']['response'], 'question roles changed')
    return dict(dataset=meta['DatasetDOI'], license=meta['License'], commit=SHA_1787, tree=manifest_url,
                event_dictionary=raw+'/task-meditation_events.json', event_inventory_sha256=inventory_digest,
                paper='https://doi.org/10.1007/s00221-016-4811-5',
                design_source='https://sccn.ucsd.edu/~arno/mypapers/brandmeyer2016_author.pdf',
                subjects=len(participants), event_tables=n_sessions, columns=fields, event_type_counts=dict(types),
                design='Mantra meditation; randomized timing of probes; fixed depth, wandering, drowsiness order for the same preceding episode.',
                missing='No randomized reversal, single-probe/skip arm or three binary features of the same exhalation. A missing key press cannot stand in for an omitted question.')


def questionnaire_panel(cache):
    digest = 'de1ffcc6ba5624476cce17c760fac68e534d6e999371925fe32d15b093c2fd71'
    data = cache.get('ishikawa-s003.docx', ISHIKAWA, digest)
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    with zipfile.ZipFile(io.BytesIO(data)) as package:
        info = package.getinfo('word/document.xml')
        checked(info.file_size < 4_000_000, 'unexpected DOCX table size')
        dom = ET.fromstring(package.read(info))
    counts = collections.defaultdict(set)

    def field(cell):
        return ''.join(node.text or '' for node in cell.findall('.//w:t', ns)).strip()

    for table in dom.findall('.//w:tbl', ns):
        rows = table.findall('w:tr', ns)
        header = [field(cell) for cell in rows[0].findall('w:tc', ns)]
        if 'Participant' not in header or 'Time' not in header:
            continue
        for row in rows[1:]:
            cells = row.findall('w:tc', ns)
            person, group, time = (field(cells[header.index(col)]) for col in ('Participant', 'Group', 'Time'))
            bucket = counts[group, int(time)]
            checked(person and person not in bucket, 'repeated/missing subject in a group/wave')
            bucket.add(person)
        break
    else:
        raise ValueError('SFMS participant table absent')
    groups = sorted({g for g, _ in counts})
    waves = sorted({t for _, t in counts})
    return dict(supplement='https://doi.org/10.1371/journal.pone.0322537.s003', sha256=digest,
                paper='https://doi.org/10.1371/journal.pone.0322537', license='CC BY (PLOS article and supplement)',
                columns=header, groups=groups, time_values=waves, participants_per_wave={
                    group: [len(counts[group, t]) for t in waves] for group in groups},
                participant_rows=sum(map(len, counts.values())), participants=len(set.union(*counts.values())),
                methods='Nonrandom assignment by schedule, 33 started, 6 dropped out, 27 completed; 4 weeks per practice.',
                missing='Weekly SFMS scores. Weeks 0, 4, 8 are Time 1, 5, 9. No within-exhalation question order, reports or randomized omission.')


def ancillary(cache):
    raw = f'https://raw.githubusercontent.com/OpenNeuroDatasets/ds003969/{SHA_3969}'
    checked_files = {}
    for name, expected in [('README', 'b630a63a51c2cd2421fbec2a29848e812c45f057'),
                           ('dataset_description.json', 'bfbdaaca6ea6b3e9383a348c9fdfbca0df4ada0f')]:
        b = cache.get('ds003969/'+name, raw+'/'+name)
        checked(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest() == expected, 'ds003969 source changed')
        checked_files[name] = b
    meta = json.loads(checked_files['dataset_description.json'])
    checked(b'first meditation block is a breath counting meditation' in checked_files['README'], 'unexpected block design')

    readme_url = 'https://osf.io/download/u58re/'
    digest = 'eb3ef35ccc6a52cea5f0dea82e946a34c935892e2cdfc05aaf31e57eea4eafc3'
    readme = cache.get('b6rn9-readme.txt', readme_url, digest)
    checked(all(marker in readme for marker in [b'100 = Bell sound', b'101 = Breath focus answer',
             b'102 = Mind wandering answer', b'The two subsequent triggers']), 'unexpected b6rn9 events')
    node = json.loads(cache.get('b6rn9-node.json', 'https://api.osf.io/v2/nodes/b6rn9/'))['data']
    lic = node['relationships']['license']['data']['id']
    checked(lic == '563c1cf88c5e4a3877f9e96c', 'changed OSF license')
    license_url = f'https://api.osf.io/v2/licenses/{lic}/'
    license_name = json.loads(cache.get('b6rn9-license.json', license_url))['data']['attributes']['name']
    return [
        dict(dataset=meta['DatasetDOI'], license=meta['License'], commit=SHA_3969, design_source=raw+'/README',
             missing='First meditation block is always breath counting. Second is tradition-specific, or counting for controls. Thinking/meditation starting order does not reverse short questions.'),
        dict(dataset='https://osf.io/b6rn9/', paper='https://pubmed.ncbi.nlm.nih.gov/33289167/',
             license=license_name, design_source=readme_url, readme_sha256=digest,
             missing='Bell, binary focus/wandering, then confidence (1–7) and arousal (1–5). Fixed series; no reversed binary attention questions or skipped-middle branch.'),
    ]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cache', type=Path, required=True)
    parser.add_argument('--fetch', action='store_true', help='download absent public files into the external cache')
    parser.add_argument('--emit', action='store_true', help='write JSON to stdout instead of comparing with the committed receipt')
    args = parser.parse_args()
    checkout = next(p for p in HERE.parents if (p/'.git').exists()) if any((p/'.git').exists() for p in HERE.parents) else HERE
    if args.cache.resolve().is_relative_to(checkout):
        parser.error('choose a cache outside the checkout')
    inputs = InputCache(args.cache, args.fetch)
    receipt = dict(audited_on='2026-11-10', purpose='Design support only; no human effect estimated.',
                   fixed_probes=openneuro_questions(inputs), training_order=questionnaire_panel(inputs),
                   other_practice_sources=ancillary(inputs))
    if args.emit:
        print(json.dumps(receipt, indent=2, ensure_ascii=False))
    else:
        checked(receipt == json.loads((HERE/'open-data-receipt.json').read_bytes()), 'design audit receipt differs')
        print('4 public designs verified; 40 EEG event tables and 243 questionnaire rows inspected without scoring responses')


if __name__ == '__main__':
    main()
