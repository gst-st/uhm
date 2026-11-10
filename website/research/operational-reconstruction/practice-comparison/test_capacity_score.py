"""Synthetic target delivery and finite-sample controls; no human responses."""
from collections import Counter
import csv
from fractions import Fraction as F
from pathlib import Path
from itertools import product
import random
import tempfile
import unittest

import capacity_score as c


def fixture(root, mode):
    roster, manifest, records = [root/name for name in ('roster.csv','manifest.csv','records.csv')]
    # This seeded model is only a fixture; prospective allocation uses a
    # concealed independently generated key in the study's allocation system.
    rng = random.Random(210)
    cues = [q for q,n in {'all':12,'bit1':4,'bit2':4,'bit3':4}.items() for _ in range(n)]
    with roster.open('w',newline='') as rf, manifest.open('w',newline='') as mf, records.open('w',newline='') as of:
        rw,mw,ow = csv.writer(rf),csv.writer(mf),csv.writer(of)
        rw.writerow(['participant','arm'])
        mw.writerow(['participant','trial','target','cue'])
        ow.writerow(['participant','trial','delivered_target','delivered_cue','answer'])
        for arm in c.ARMS:
            for person in range(c.PER_ARM):
                p = f'{arm}{person}'
                rw.writerow([p,arm])
                all_count = 0
                rng.shuffle(cues)
                for t, cue in enumerate(cues,1):
                    word = rng.choice(c.WORDS)
                    mw.writerow((p,t,word,cue))
                    if mode == 'empty':
                        continue
                    if cue=='all':
                        all_count += 1
                        success = arm == 'count' or all_count <= 10+person%2
                        answer = word if success else ('1' if word[0]=='0' else '0')+word[1:]
                    else:
                        answer = word[c.BITS.index(cue)]
                    ow.writerow((p,t,word,cue,answer))
    return roster,manifest,records


class CapacityTests(unittest.TestCase):
    def test_right_word_and_bit_after_actual_delivery(self):
        self.assertEqual(c.status_for('001','all','001','all','001'),'correct')
        self.assertEqual(c.status_for('001','all','001','all','101'),'wrong')
        for cue,answer in zip(c.BITS,'001'):
            self.assertEqual(c.status_for('001',cue,'001',cue,answer),'correct')
        self.assertEqual(c.status_for('001','bit2','001','bit2',''),'missing_answer')
        for word,cue in (('101','bit2'),('','bit2'),('001',''),('001','all')):
            self.assertEqual(c.status_for('001','bit2',word,cue,'0'),'invalid_delivery')
        with self.assertRaises(ValueError):
            c.status_for('111','all','111','all','1')
        with self.assertRaises(ValueError):
            c.status_for('100','bit1','1X0','bit1','1')

    def test_no_data_never_excludes(self):
        with tempfile.TemporaryDirectory() as td:
            files=fixture(Path(td),'empty')
            with files[-1].open('a') as f:
                f.write('count0,1,,,0\n')
            arms=c.analyze(*files)['arms']
            for arm,r in arms.items():
                self.assertEqual(r['without_any_row'],c.PER_ARM-(arm=='count'))
                self.assertEqual(r['sample_completion_bounds']['all'],[0,1])
                self.assertEqual(r['sample_completion_bounds']['slack'],[-1,3])
                self.assertFalse(r['exclude_single_shared_decoded_word'])
                self.assertFalse(r['exclude_dimension_at_most_seven'])
                self.assertEqual(sum(v['invalid_delivery'] for v in r['outcomes'].values()),int(arm=='count'))

    def test_independent_bits_and_incompatible_shared_readout(self):
        with tempfile.TemporaryDirectory() as td:
            out=c.analyze(*fixture(Path(td),'assigned'))['arms']
            register=out['count']
            self.assertEqual(register['sample_completion_bounds']['all'],[1,1])
            self.assertTrue(register['hoeffding_excludes_dimension'])
            self.assertTrue(register['dimension_e_test']['crosses_threshold'])
            self.assertFalse(register['exclude_single_shared_decoded_word'])
            contextual=out['follow']
            # Half the subjects have ten and half eleven whole-word hits out of
            # twelve, while all single bits are right. This is exactly -1/8.
            self.assertEqual(contextual['sample_completion_bounds']['slack'],[-.125,-.125])
            self.assertFalse(contextual['hoeffding_excludes_shared_word'])
            self.assertTrue(contextual['shared_word_e_test']['crosses_threshold'])
            self.assertTrue(contextual['exclude_single_shared_decoded_word'])
            self.assertFalse(contextual['exclude_dimension_at_most_seven'])

    def test_hoeffding_and_e_boundaries(self):
        self.assertEqual(c.radius(2), F(99561282,10**9))
        self.assertEqual(c.radius(8), F(398245128,10**9))
        self.assertTrue(c.evidence(Counter({F(5,4):1,F(2):7}))['crosses_threshold'])
        self.assertFalse(c.evidence(Counter({F(5,4)-F(1,10**20):1,F(2):7}))['crosses_threshold'])

    def test_unbalanced_manifest_without_any_bit_queries_is_retained(self):
        with tempfile.TemporaryDirectory() as td:
            roster,manifest,obs=fixture(Path(td),'empty')
            text = manifest.read_text()
            for bit in c.BITS:
                text = text.replace(','+bit+'\n',',all\n')
            manifest.write_text(text)
            result = c.analyze(roster,manifest,obs)['arms']['follow']
            self.assertEqual(result['scheduled_counts']['bit1'],0)
            self.assertEqual(result['scheduled_counts']['all'],24*c.PER_ARM)
            self.assertEqual(result['sample_completion_bounds']['all'],[-1,1])
            self.assertEqual(result['sample_completion_bounds']['bit1'],[1,1])
            self.assertFalse(result['exclude_single_shared_decoded_word'])
            # The same finite randomization law allows an entirely unobserved,
            # all-bit schedule. The constant IPW offset cannot testify to an
            # actual word measurement: abstain when the apparatus read none.
            manifest.write_text(text.replace(',all\n',',bit2\n'))
            result = c.analyze(roster,manifest,obs)['arms']['count']
            self.assertEqual(result['sample_completion_bounds']['all'],[1,1])
            self.assertTrue(result['dimension_e_test']['crosses_threshold'])
            self.assertFalse(result['exclude_dimension_at_most_seven'])

    def test_centered_ipw_with_individual_negative_bit_score(self):
        cells = Counter({('bit1','wrong'):24})
        rates,slack = c.participant_scores(cells)
        self.assertEqual(rates['bit1'],c.point(-5))
        self.assertEqual(rates['all'],c.point(1))
        self.assertEqual(slack,c.point(6))
        cells = Counter({('all','wrong'):24})
        rates,slack = c.participant_scores(cells)
        self.assertEqual(rates['all'],c.point(-1))
        self.assertEqual(slack,c.point(-2))

    def test_iid_query_oracle_recovers_all_four_counterfactual_means(self):
        for outcomes in product((0,1),repeat=4):
            targets = dict(zip(c.INVERSE_CUE_PROBABILITY,outcomes))
            average = Counter()
            average_slack = F(0)
            for cue,w in c.INVERSE_CUE_PROBABILITY.items():
                # Repeat a single possible fine-scale outcome 24 times. The
                # estimator is affine in slot totals, so averaging these four
                # terms with their true randomization weights tests its law.
                status = 'correct' if targets[cue] else 'wrong'
                rate,slack=c.participant_scores(Counter({(cue,status):24}))
                for q,r in rate.items():
                    average[q] += r.low / w
                average_slack += slack.low / w
            self.assertEqual(dict(average),targets)
            self.assertEqual(average_slack,targets['all']+2-sum(targets[q] for q in c.BITS))

    def test_invalid_roster_manifest_and_duplicate_record(self):
        with tempfile.TemporaryDirectory() as td:
            files=fixture(Path(td),'empty')
            registry,slots=c.design(files[0],files[1])
            with files[2].open('a') as f:
                f.write('count0,1,,,\ncount0,1,,,\n')
            with self.assertRaisesRegex(ValueError,'duplicate'):
                c.observed(files[2],registry,slots)
            with files[1].open('a') as f:
                f.write('count0,1,000,all\n')
            with self.assertRaisesRegex(ValueError,'duplicate'):
                c.design(*files[:2])
            files[0].write_text('participant,arm\ncount0,count\n')
            with self.assertRaisesRegex(ValueError,'1024'):
                c.design(*files[:2])


if __name__ == '__main__':
    unittest.main()
