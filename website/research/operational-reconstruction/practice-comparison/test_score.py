"""Synthetic fixed-design and mathematical controls. No human records."""
import csv
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import tempfile
import unittest

import score as s


def slots():
    return [(b,q,None) for b in s.BLOCKS for q,n in s.DESIGN.items() for _ in range(n)]


def complete_stat(data):
    return {k:v.low for k,v in s.participant_scores(data)[0].items()}


def write_design(root):
    roster, manifest = root/'roster.csv', root/'manifest.csv'
    with roster.open('w',newline='') as r, manifest.open('w',newline='') as m:
        rw, mw = csv.writer(r), csv.writer(m)
        rw.writerow(['participant','arm'])
        mw.writerow(['participant','block','trial','sequence'])
        order = [q for q,n in s.DESIGN.items() for _ in range(n)]
        for arm in s.ARMS:
            for i in range(s.PER_ARM):
                person = f'{arm}{i}'
                rw.writerow([person,arm])
                for b in s.BLOCKS:
                    mw.writerows((person,b,t,q) for t,q in enumerate(order,1))
    return roster, manifest


class ComparisonTests(unittest.TestCase):
    def test_exact_model_arithmetic_and_heterogeneity(self):
        def homogeneous(a):
            u,m = s.predictions(*([s.point(a)]*4))
            self.assertEqual((u.low,m.low),(u.high,m.high))
            return u.low,m.low
        close,serial = homogeneous(F(9,10))
        self.assertEqual((close,serial),(F(16,25),F(41,50)))
        a, b = homogeneous(F(4,5)), homogeneous(F(1))
        mean = tuple((x+y)/2 for x,y in zip(a,b))
        self.assertEqual(mean,(F(17,25),F(21,25)))
        self.assertNotEqual(mean,(close,serial))

    def test_signed_cross_product_uses_opposite_halves(self):
        data = [(b,q,int(b in (1,3))) for b,q,_ in slots()]
        primary, diag = s.participant_scores(data)
        self.assertEqual(diag['individual_cross_product_u'],s.point(-1))
        self.assertEqual(diag['a_odd_minus_even'],s.point(1))
        self.assertEqual(diag['adjacent_a'],s.point(F(1,2)))
        self.assertEqual(primary['equal_turn_residual'],s.point(F(3,2)))
        self.assertEqual(primary['serial_flip_residual'],s.point(F(1,2)))

    def test_every_missing_bound_has_a_completion(self):
        content = [(b,q,int((i+b)%3 == 0)) for i,(b,q,_) in enumerate(slots())]
        mask = [(1,'AB'),(2,'BC'),(1,'AC'),(3,'ABC'),(4,'A-C'),(2,'A0C')]
        indexes = [next(i for i,(b,q,_) in enumerate(content) if (b,q)==mark) for mark in mask]
        incomplete = content.copy()
        for i in indexes:
            b,q,_ = content[i]
            incomplete[i] = b,q,None
        bounds = s.participant_scores(incomplete)[0]
        extrema = {name:[] for name in bounds}
        for fill in product((0,1),repeat=len(indexes)):
            data = incomplete.copy()
            for i,bit in zip(indexes,fill):
                b,q,_ = data[i]
                data[i] = b,q,bit
            for name,number in complete_stat(data).items():
                extrema[name].append(number)
        for name,values in extrema.items():
            with self.subTest(name=name):
                self.assertEqual(bounds[name],s.Bounds(min(values),max(values)))

    def test_no_data_retains_every_assigned_person(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            roster, plan = write_design(root)
            obs = root/'obs.csv'
            obs.write_text('participant,block,trial,delivered,first,last\ncount0,1,1,AB,1,\ncount0,1,2,BC,1,1\ncount0,1,3,,1,0\n')
            out = s.analyze(roster,plan,obs)
            for arm in s.ARMS:
                result = out['arms'][arm]
                self.assertEqual(result['without_any_row'],s.PER_ARM-(arm=='count'))
                self.assertEqual(result['with_any_observed_agreement'],0)
                for name,(low,high) in s.ENDPOINTS.items():
                    claim = result['primary'][name]
                    self.assertEqual(claim['sample_completion_bounds'],[float(low),float(high)])
                    self.assertEqual(claim['simultaneous_interval'],[float(low),float(high)])
                    self.assertEqual(claim['sign'],'includes_zero')
            self.assertEqual(out['arms']['count']['outcome_counts']['AB']['missing_endpoint'],1)
            self.assertEqual(out['arms']['count']['outcome_counts']['AB']['invalid_delivery'],1)
            self.assertEqual(out['arms']['count']['outcome_counts']['BA']['invalid_delivery'],1)
            self.assertEqual(out['arms']['count']['exact_projective_repeat']['status'],'unobserved')
            with obs.open('a') as f:
                f.write('count0,1,13,AA,1,0\ncount0,1,14,AA,1,0\n')
            checked = s.analyze(roster,plan,obs)
            self.assertEqual(checked['arms']['count']['exact_projective_repeat'],
                             {'observed':1,'discordant':1,'status':'contradicted'})

    def test_wrong_manifest_duplicates_and_invalid_buttons(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            roster, manifest = write_design(root)
            people, design = s.read_design(roster,manifest)
            with manifest.open('a') as stream:
                stream.write('count0,1,1,AB\n')
            with self.assertRaisesRegex(ValueError,'duplicate'):
                s.read_design(roster,manifest)
            obs = root/'obs.csv'
            header = 'participant,block,trial,delivered,first,last\n'
            for body in ('count0,1,1,AB,yes,0\n','count0,1,19,AB,1,1\n',
                         'count0,1,1,AB,1,1\ncount0,1,1,AB,1,1\n','new,1,1,AB,0,0\n'):
                obs.write_text(header+body)
                with self.assertRaises(ValueError):
                    s.read_records(obs,people,design)

    def test_finite_sample_radii(self):
        self.assertEqual(s.FAMILY,12)
        self.assertEqual(s.radius(*s.ENDPOINTS['rank_one_slack']),F(163059125,10**9))
        self.assertEqual(s.radius(*s.ENDPOINTS['serial_flip_residual']),F(77647203,10**9))


if __name__=='__main__':
    unittest.main()
