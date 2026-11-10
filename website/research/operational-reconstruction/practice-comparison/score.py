"""Frozen six-contrast analysis. The independent unit is one randomized participant."""
import argparse
import csv
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction as F
import json
import math
from pathlib import Path

ARMS = ('count', 'follow')
PER_ARM = 2048
BLOCKS = (1, 2, 3, 4)
DESIGN = {'AB': 2, 'BA': 2, 'BC': 2, 'CB': 2, 'AC': 2, 'CA': 2,
          'AA': 1, 'BB': 1, 'CC': 1, 'ABC': 1, 'A-C': 1, 'A0C': 1}
TRIALS = sum(DESIGN.values())
ALPHA = 0.05
ENDPOINTS = {
    'equal_turn_residual': (-1, 2),
    'serial_flip_residual': (-1, 1),
    'passive_joint_slack': (-1, 2),
    'rank_one_slack': (F(-24,25), F(81,25)),
    'active_minus_sham': (-1, 1),
    'sham_minus_silent': (-1, 1),
}
FAMILY = len(ARMS) * len(ENDPOINTS)


@dataclass(frozen=True)
class Bounds:
    low: F
    high: F

    def __add__(self, other):
        return Bounds(self.low+other.low, self.high+other.high)

    def __sub__(self, other):
        return Bounds(self.low-other.high, self.high-other.low)

    def scaled(self, factor):
        if factor < 0:
            raise ValueError('expected nonnegative scale')
        return Bounds(self.low*factor, self.high*factor)

    def product(self, other):
        corners = [x*y for x in (self.low,self.high) for y in (other.low,other.high)]
        return Bounds(min(corners),max(corners))

    def as_list(self):
        return [float(self.low),float(self.high)]


def point(x):
    return Bounds(F(x),F(x))


def rows(path, required):
    with Path(path).open(newline='', encoding='utf-8-sig') as stream:
        reader = csv.DictReader(stream, strict=True)
        fields = reader.fieldnames or []
        if '' in fields or len(set(fields))!=len(fields) or not set(required)<=set(fields):
            raise ValueError(f'{path}: missing or duplicate header; expected {required}')
        for row in reader:
            if None in row or any(v is None for v in row.values()):
                raise ValueError(f'{path}:{reader.line_num}: wrong field count')
            yield row


def key(row, people):
    person = row['participant']
    if person not in people:
        raise ValueError(f'unknown participant {person!r}')
    def parse(name, maximum):
        s = row[name]
        if not s.isascii() or not s.isdecimal() or not 1 <= int(s) <= maximum:
            raise ValueError(f'{person}: invalid {name} {s!r}')
        return int(s)
    return person, parse('block',len(BLOCKS)), parse('trial',TRIALS)


def read_design(roster_file, manifest_file):
    people = {}
    for r in rows(roster_file, ['participant','arm']):
        p, arm = r['participant'], r['arm']
        if not p or p!=p.strip() or p in people or arm not in ARMS:
            raise ValueError('invalid randomized roster')
        people[p] = arm
    if Counter(people.values())!=Counter({arm:PER_ARM for arm in ARMS}):
        raise ValueError(f'expected exactly {PER_ARM} randomized people per arm')
    design = {}
    block_cells = {}
    for r in rows(manifest_file, ['participant','block','trial','sequence']):
        t = key(r,people)
        seq = r['sequence']
        if t in design or seq not in DESIGN:
            raise ValueError(f'duplicate slot or unknown sequence: {t!r}, {seq!r}')
        design[t] = seq
        block_cells.setdefault(t[:2],Counter())[seq] += 1
    for p in people:
        for block in BLOCKS:
            if block_cells.get((p,block))!=DESIGN:
                raise ValueError(f'{p} block {block}: incorrect frozen sequence quotas')
    return people, design


def read_records(obs_file, people, design):
    records = {}
    for row in rows(obs_file, ['participant','block','trial','delivered','first','last']):
        t = key(row,people)
        if t not in design or t in records:
            raise ValueError(f'unscheduled or duplicate observation {t!r}')
        x,y = row['first'], row['last']
        if x not in ('0','1','') or y not in ('0','1',''):
            raise ValueError(f'{t!r}: endpoint must be 0, 1, or blank')
        delivered = row['delivered']
        if delivered and delivered not in DESIGN:
            raise ValueError(f'{t!r}: unrecognized delivery code')
        if delivered != design[t]:
            records[t] = 'invalid_delivery'
        elif '' in (x,y):
            records[t] = 'missing_endpoint'
        else:
            records[t] = 'match' if x == y else 'mismatch'
    return records


def predictions(a_odd,a_even,b_odd,b_even):
    """Each product uses disjoint, prespecified sets of trials within a person."""
    def signed(x):
        return x.scaled(2)-point(1)
    product = signed(a_odd).product(signed(b_even)) + signed(a_even).product(signed(b_odd))
    u = product.scaled(F(1,2))
    return u, (point(1)+u).scaled(F(1,2))


def participant_scores(slots):
    """Slots are (block, sequence, agreement) with None denoting an unknown score."""
    cells = Counter()
    for block, seq, result in slots:
        cells[block,seq,result] += 1

    def rate(sequences, blocks=BLOCKS):
        n = sum(DESIGN[seq] for seq in sequences)*len(blocks)
        known_yes = sum(cells[block,seq,1] for block in blocks for seq in sequences)
        unknown = sum(cells[block,seq,None] for block in blocks for seq in sequences)
        return Bounds(F(known_yes,n),F(known_yes+unknown,n))

    ab, bc, ac = ('AB','BA'), ('BC','CB'), ('AC','CA')
    a, b, z = rate(ab), rate(bc), rate(ac)
    a_odd, a_even = rate(ab,(1,3)), rate(ab,(2,4))
    b_odd, b_even = rate(bc,(1,3)), rate(bc,(2,4))
    u, serial = predictions(a_odd,a_even,b_odd,b_even)
    active, sham, silent = (rate([s]) for s in ('ABC','A-C','A0C'))
    primary = {
        'equal_turn_residual': z-u,
        'serial_flip_residual': z-serial,
        'passive_joint_slack': z+point(1)-(a+b),
        'rank_one_slack': z+point(F(56,25))-(a+b).scaled(F(8,5)),
        'active_minus_sham': active-sham,
        'sham_minus_silent': sham-silent,
    }
    diagnostics = {s:rate([s]) for s in DESIGN}
    diagnostics.update({
        'adjacent_a':a, 'adjacent_b':b, 'direct_z':z, 'a_minus_b':a-b,
        'AB_minus_BA':rate(['AB'])-rate(['BA']), 'BC_minus_CB':rate(['BC'])-rate(['CB']),
        'AC_minus_CA':rate(['AC'])-rate(['CA']), 'a_odd_minus_even':a_odd-a_even,
        'b_odd_minus_even':b_odd-b_even,
        'z_odd_minus_even':rate(ac,(1,3))-rate(ac,(2,4)),
        'individual_cross_product_u':u,
    })
    return primary, diagnostics


def radius(lo,hi):
    # Two tails per contrast, 12 simultaneous intervals under the frozen design.
    raw = float(hi-lo)*math.sqrt(math.log(2*FAMILY/ALPHA)/(2*PER_ARM))
    return F(math.ceil(raw*10**9), 10**9)


def analyze(roster_file, manifest_file, obs_file):
    people, design = read_design(roster_file,manifest_file)
    records = read_records(obs_file,people,design)
    sums = {arm:{} for arm in ARMS}
    gaps = {arm: {s:Counter() for s in DESIGN} for arm in ARMS}
    nobody = Counter()
    known_part = Counter()
    for p,arm in people.items():
        slots = []
        any_row = any_known = False
        for block in BLOCKS:
            for trial in range(1,TRIALS+1):
                t = (p,block,trial)
                seq = design[t]
                status = records.get(t, 'no_row')
                scored = status in ('match','mismatch')
                slots.append((block,seq,int(status=='match') if scored else None))
                any_row |= t in records
                any_known |= scored
                gaps[arm][seq][status] += 1
        nobody[arm] += not any_row
        known_part[arm] += any_known
        primary, diagnostic = participant_scores(slots)
        for name, bounds in {**primary,**diagnostic}.items():
            sums[arm][name] = sums[arm].get(name,point(0)) + bounds
    by_arm = {}
    for arm in ARMS:
        estimates = {name:b.scaled(F(1,PER_ARM)) for name,b in sums[arm].items()}
        primary = {}
        for name,(lo,hi) in ENDPOINTS.items():
            bounds = estimates.pop(name)
            r = radius(lo,hi)
            interval = Bounds(max(F(lo),bounds.low-r),min(F(hi),bounds.high+r))
            sign = ('below_zero' if interval.high < 0 else
                    'above_zero' if interval.low > 0 else 'includes_zero')
            primary[name] = {'sample_completion_bounds':bounds.as_list(),
                             'simultaneous_interval':interval.as_list(),'sign':sign}
        repeats = [gaps[arm][q] for q in ('AA','BB','CC')]
        different = sum(c['mismatch'] for c in repeats)
        observed = different + sum(c['match'] for c in repeats)
        by_arm[arm] = {
            'exact_projective_repeat': {
                'observed':observed, 'discordant':different,
                'status':('contradicted' if different else
                          'no_observed_contradiction' if observed else 'unobserved')},

            'randomized':PER_ARM, 'without_any_row':nobody[arm],
            'with_any_observed_agreement':known_part[arm], 'primary':primary,
            'descriptive_completion_bounds':{k:v.as_list() for k,v in estimates.items()},
            'outcome_counts':{s:{k:c[k] for k in ('match','mismatch','no_row','missing_endpoint','invalid_delivery')}
                              for s,c in gaps[arm].items()},
        }
    return {'arms':by_arm,'plan':plan()}


def plan():
    return {'people_per_arm':PER_ARM,'blocks':len(BLOCKS),'trials_per_block':TRIALS,
            'sequence_counts_per_block':DESIGN, 'family_error':ALPHA,
            'two_sided_intervals':FAMILY,'rounding':'radii rounded up to 1e-9',
            'range_and_radius':{name:[float(lo),float(hi),float(radius(lo,hi))]
                                for name,(lo,hi) in ENDPOINTS.items()}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--plan',action='store_true')
    parser.add_argument('files',type=Path,nargs='*',metavar='CSV',
                        help='randomization roster, prior manifest, locked endpoint records')
    args = parser.parse_args()
    if args.plan and not args.files:
        result = plan()
    elif not args.plan and len(args.files)==3:
        try:
            result = analyze(*args.files)
        except (OSError,csv.Error,ValueError) as error:
            parser.exit(2,f'score error: {error}\n')
    else:
        parser.error('select --plan or supply exactly three CSV files')
    print(json.dumps(result,indent=2,sort_keys=True,allow_nan=False))


if __name__=='__main__':
    main()
