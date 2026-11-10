"""Sealed-manifest scores for uniform 3-bit word vs single-bit retrieval."""
import argparse
from collections import Counter
from fractions import Fraction as F
import csv
import json
import math
from pathlib import Path

from score import ARMS, Bounds, point, rows

PER_ARM = 1024
# All draws occur with replacement, independently of the fresh target, trial
# history and encoded state. The manifest's exact order is fixed before use.
INVERSE_CUE_PROBABILITY = {'all':2,'bit1':6,'bit2':6,'bit3':6}
TRIALS = 24
BITS = ('bit1','bit2','bit3')
WORDS = tuple(format(w,'03b') for w in range(8))
FAMILY, ALPHA = 8, F(1,20)
E_CUTOFF = FAMILY / ALPHA
CAP = F(7,8)
STATUSES = ('correct','wrong','no_row','invalid_delivery','missing_answer')


def capacity_key(row,people):
    p, text = row['participant'],row['trial']
    if p not in people or not text.isascii() or not text.isdecimal() or not 1<=int(text)<=TRIALS:
        raise ValueError(f'invalid or unscheduled key: {p!r}, {text!r}')
    return p,int(text)


def design(roster_file, manifest_file):
    people = {}
    for r in rows(roster_file, ['participant','arm']):
        p,arm = r['participant'],r['arm']
        if not p or p!=p.strip() or p in people or arm not in ARMS:
            raise ValueError('invalid randomized capacity roster')
        people[p] = arm
    if Counter(people.values()) != Counter({arm:PER_ARM for arm in ARMS}):
        raise ValueError(f'expected exactly {PER_ARM} independently randomized participants per arm')
    slots = {}
    slot_counts = Counter()
    for r in rows(manifest_file,['participant','trial','target','cue']):
        t = capacity_key(r,people)
        word,cue = r['target'],r['cue']
        if t in slots or word not in WORDS or cue not in INVERSE_CUE_PROBABILITY:
            raise ValueError(f'{t!r}: duplicate or malformed frozen target/cue')
        slots[t] = word,cue
        slot_counts[t[0]] += 1
    if any(slot_counts[p] != TRIALS for p in people):
        raise ValueError('each randomized person requires exactly 24 distinct frozen slots')
    return people,slots


def status_for(target, cue, delivered, prompted, answer):
    if delivered not in ('',*WORDS) or prompted not in ('',*INVERSE_CUE_PROBABILITY):
        raise ValueError('malformed delivery; use empty fields for unknown receipts')
    if answer and answer not in (*WORDS,'0','1'):
        raise ValueError('malformed physical answer')
    if delivered!=target or prompted!=cue:
        return 'invalid_delivery'
    if not answer:
        return 'missing_answer'
    if cue=='all':
        if answer not in WORDS:
            raise ValueError('whole-word response must carry three bits')
        truth = target
    else:
        if answer not in ('0','1'):
            raise ValueError('single-bit response must carry one bit')
        truth = target[BITS.index(cue)]
    return 'correct' if answer==truth else 'wrong'


def observed(path,people,slots):
    required = ['participant','trial','delivered_target','delivered_cue','answer']
    result = {}
    for row in rows(path, required):
        t = capacity_key(row,people)
        if t not in slots or t in result:
            raise ValueError(f'{t!r}: duplicate or unscheduled capacity record')
        result[t] = status_for(*slots[t],row['delivered_target'],row['delivered_cue'],row['answer'])
    return result


def participant_scores(cells):
    # Centered inverse-probability scores. The denominator always stays
    # at the number of assigned trials, even if this person got no bit-i cue.
    def accuracy(cue):
        w = F(INVERSE_CUE_PROBABILITY[cue], TRIALS)
        wrong = cells[cue,'wrong']
        unknown = sum(cells[cue,k] for k in ('no_row','missing_answer','invalid_delivery'))
        return Bounds(1-w*(wrong+unknown), 1-w*wrong)
    rates = {cue:accuracy(cue) for cue in INVERSE_CUE_PROBABILITY}
    z = rates['all']
    slack = z+point(2)-rates['bit1']-rates['bit2']-rates['bit3']
    return rates,slack


def radius(width):
    raw = width*math.sqrt(math.log(E_CUTOFF)/(2*PER_ARM))
    return F(math.ceil(raw*10**9),10**9)


def plan():
    return {'participants_per_arm':PER_ARM,'slots':TRIALS,'independent_cue_probabilities':{q:1/w for q,w in INVERSE_CUE_PROBABILITY.items()},
            'target_draws':'independent equiprobable words; no retrospective balancing',
            'directional_tests_in_family':FAMILY,'family_error':float(ALPHA),'whole_word_cap':float(CAP),
            'fixed_horizon_e_threshold':int(E_CUTOFF),'n_per_e_product':PER_ARM,
            'centered_ipw_score_ranges':{'all':[-1,1],'each_bit':[-5,1],'slack':[-2,6]},
            'lower_whole_word_radius':float(radius(2)),'upper_shared_word_slack_radius':float(radius(8)),
            'assumptions':['independent people; all randomized participants included',
                           'fresh uniform 3-bit label and independent, concealed later query drawn with replacement',
                           'capacity null counts every accessible carrier and side channel',
                           'shared-word null reads the same pre-query decoded word for all four query types']}


def evidence(factors):
    # Multiplying rational frequencies keeps the decision exact even when the
    # product is too small or large to represent in floating-point arithmetic.
    product_value = F(1)
    for value,multiplicity in factors.items():
        product_value *= value ** multiplicity
    return {'log_e':math.log(product_value.numerator)-math.log(product_value.denominator),
            'crosses_threshold':product_value >= E_CUTOFF}


def analyze(roster_file, manifest_file, obs_file):
    people,slots = design(roster_file,manifest_file)
    records = observed(obs_file,people,slots)
    total = {arm: {cue:point(0) for cue in (*INVERSE_CUE_PROBABILITY,'slack')} for arm in ARMS}
    tallies = {arm:{cue:Counter() for cue in INVERSE_CUE_PROBABILITY} for arm in ARMS}
    targets = {arm:{cue:Counter() for cue in INVERSE_CUE_PROBABILITY} for arm in ARMS}
    absent = Counter()
    factors = {arm: {'capacity':Counter(), 'shared':Counter()} for arm in ARMS}
    for p,arm in people.items():
        cells = Counter()
        any_row = False
        for t in range(1,TRIALS+1):
            key = p,t
            word,cue = slots[key]
            status = records.get(key,'no_row')
            cells[cue,status] += 1
            targets[arm][cue][word] += 1
            tallies[arm][cue][status] += 1
            any_row |= key in records
        absent[arm] += not any_row
        rates,slack = participant_scores(cells)
        factors[arm]['capacity'][1+(rates['all'].low-CAP)/2] += 1
        factors[arm]['shared'][1-slack.high/8] += 1
        for cue,bounds in {**rates,'slack':slack}.items():
            total[arm][cue] = total[arm][cue] + bounds
    arms = {}
    for arm in ARMS:
        bounds = {name:b.scaled(F(1,PER_ARM)) for name,b in total[arm].items()}
        z_lower = max(F(0),bounds['all'].low-radius(2))
        slack_upper = max(F(-1),min(F(3),bounds['slack'].high+radius(8)))
        counts_by_cue = {q:sum(tallies[arm][q].values()) for q in INVERSE_CUE_PROBABILITY}
        tested = {q:tallies[arm][q]['correct']+tallies[arm][q]['wrong'] > 0
                  for q in INVERSE_CUE_PROBABILITY}
        ev_dimension = evidence(factors[arm]['capacity'])
        ev_shared = evidence(factors[arm]['shared'])
        arms[arm] = {
            'randomized':PER_ARM,'without_any_row':absent[arm],
            'sample_completion_bounds':{name:v.as_list() for name,v in bounds.items()},
            'simultaneous_lower_word_accuracy':float(z_lower),
            'simultaneous_upper_shared_word_slack':float(slack_upper),
            'has_observed_score_per_cue':tested, 'scheduled_counts':counts_by_cue,
            'hoeffding_excludes_dimension':tested['all'] and z_lower>CAP,
            'hoeffding_excludes_shared_word':all(tested.values()) and slack_upper<0,
            'dimension_e_test':ev_dimension,'shared_word_e_test':ev_shared,
            'exclude_dimension_at_most_seven':tested['all'] and (z_lower>CAP or ev_dimension['crosses_threshold']),
            'exclude_single_shared_decoded_word':all(tested.values()) and (slack_upper<0 or ev_shared['crosses_threshold']),
            'outcomes':{cue:{k:t[k] for k in STATUSES} for cue,t in tallies[arm].items()},
            'scheduled_targets':{cue:{w:t[w] for w in WORDS} for cue,t in targets[arm].items()},
        }
    return {'arms':arms,'plan':plan()}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--plan',action='store_true')
    parser.add_argument('files',nargs='*',type=Path,metavar='CSV')
    args=parser.parse_args()
    if args.plan and not args.files:
        result=plan()
    elif not args.plan and len(args.files)==3:
        try:
            result=analyze(*args.files)
        except (ValueError,OSError,csv.Error) as err:
            parser.exit(2,f'capacity score error: {err}\n')
    else:
        parser.error('select --plan or give roster.csv manifest.csv observations.csv')
    print(json.dumps(result,indent=2,sort_keys=True,allow_nan=False))


if __name__=='__main__':
    main()
