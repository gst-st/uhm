"""Evaluate a fixed, prospective two-source comparison. No simulated or fitted default input."""
import argparse
import csv
import json
from fractions import Fraction as Q
from itertools import product

ARMS = ('12', '13', '24', '34', '10', '1-minus2', '11', '22')
N = 6000
EPS = Q(1, 20)
ONE = (Q(-1), Q(1))

def band(numerator, missing):
    return (max(ONE[0], Q(numerator-missing, N)-EPS),
            min(ONE[1], Q(numerator+missing, N)+EPS))

def mul(x, y):
    vals = [a*b for a,b in product(x,y)]
    return min(vals), max(vals)

def sq(x):
    a,b=x
    return (Q(0) if a<=0<=b else min(a*a,b*b), max(a*a,b*b))

def meet(x,y):
    return max(x[0],y[0])<=min(x[1],y[1])

def evaluate(rows):
    sums = dict.fromkeys(ARMS,0)
    misses = sums.copy()
    seen = set()
    for row in rows:
        arm, slot, a, b = (row[k] for k in ('arm','slot','a','b'))
        key = (arm,int(slot))
        if arm not in sums or not 1<=key[1]<=N or key in seen:
            raise ValueError('invalid or repeated arm/slot')
        if a not in ('+','-','NA') or b not in ('+','-','NA'):
            raise ValueError('invalid binary/missing outcome')
        seen.add(key)
        if 'NA' in (a,b):
            misses[arm]+=1
        else:
            sums[arm]+=1 if a==b else -1
    if len(seen)!=len(ARMS)*N:
        raise ValueError('incomplete manifest; declare every missed trial explicitly')
    c = {k:band(sums[k],misses[k]) for k in ARMS}
    fail = []
    obligations = [
        ('zero reference', c['10'], (Q(0),Q(0))),
        ('reference reversal', c['12'], (-c['1-minus2'][1],-c['1-minus2'][0])),
        ('first self comparison', c['11'], (Q(0),Q(1))),
        ('second self comparison', c['22'], (Q(0),Q(1))),
        ('self/cross agreement', sq(c['12']), mul(c['11'],c['22'])),
        ('held-out four-source equality', mul(c['12'],c['34']),mul(c['13'],c['24']))]
    for label, x, y in obligations:
        if not meet(x,y):
            fail.append(label)
    ratio = None
    lo,hi = c['12']
    if not lo<=0<=hi:
        r = mul(mul(c['13'],c['24']),(1/hi,1/lo))
        ratio = [str(v) for v in r]
    return dict(missing=misses, correlations={k:[str(v) for v in ci] for k,ci in c.items()},
                predicted_34_from_calibration=ratio,failed=fail,
                decision='incompatible' if fail else 'not excluded')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('csv_file')
    args=parser.parse_args()
    with open(args.csv_file,newline='') as f:
        data=csv.DictReader(f)
        if data.fieldnames!=['arm','slot','a','b']:
            parser.error('expected columns arm,slot,a,b')
        print(json.dumps(evaluate(data),indent=2))
