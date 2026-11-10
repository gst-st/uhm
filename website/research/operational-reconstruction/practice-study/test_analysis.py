"""Synthetic controls only. No participant observations are bundled."""
import csv
import itertools
import tempfile
import unittest
from collections import Counter
from pathlib import Path

import analysis as a


def complete_totals(phase_count, phase_follow, history_count, history_follow):
    n = a.PER_ARM * (a.TRIALS // len(a.QUERIES))
    proportions = [phase_count, phase_follow, history_count, history_follow]
    cells = itertools.product(a.QUERIES, a.ARMS)
    totals = {}
    for (query, arm), p in zip(cells, proportions):
        correct = round(n * p)
        totals[arm, query] = Counter(correct=correct, incorrect=n - correct)
    return totals


class FrozenAnalysis(unittest.TestCase):
    def test_quantitative_regions(self):
        cases = [
            ((.85, .85, .8, .55), 'supported'),
            ((.85, .85, .5, .5), 'incompatible'),
            ((.75, .95, .85, .55), 'incompatible'),
            ((.45, .45, .85, .55), 'inconclusive'),  # equal failures cannot support
            ((.85, .85, .66, .55), 'inconclusive'),
        ]
        for means, decision in cases:
            with self.subTest(means=means):
                output = a.confidence_decision(complete_totals(*means))
                self.assertEqual(output['decision'], decision)
                if decision == 'supported':
                    self.assertGreater(output['interaction_interval_from_joint_bounds'][0], 0)

    def test_missing_can_only_widen_bounds(self):
        totals = complete_totals(.85, .85, .8, .55)
        complete = a.confidence_decision(totals)
        for arm, outcome in [('count', 'correct'), ('follow', 'incorrect')]:
            counts = totals[arm, 'history']
            counts[outcome] -= 2000
            counts['no_answer'] += 2000
        missing = a.confidence_decision(totals)
        self.assertEqual(missing['decision'], 'inconclusive')
        lo, hi = complete['outcomes']['history']['simultaneous_confidence_interval']
        low, high = missing['outcomes']['history']['simultaneous_confidence_interval']
        self.assertLessEqual(low, lo)
        self.assertGreaterEqual(high, hi)
        self.assertAlmostEqual(a.plan()['design_alternative']['joint_support_probability_lower_bound'],
                               .8210330402482147)

    def test_missingness_can_make_equivalence_impossible(self):
        data = complete_totals(.85, .85, .80, .55)
        for arm in a.ARMS:
            data[arm,'phase']['correct'] -= 1000
            data[arm,'phase']['no_answer'] += 1000
        report = a.confidence_decision(data)
        self.assertFalse(report['phase_equivalence_possible_by_width'])
        self.assertEqual(report['decision'], 'inconclusive')

    def test_classification_requires_measured_truth(self):
        trial = a.Trial('history', 'inhale', 'even', 6)
        row = {'observed_phase': 'inhale', 'completed_exhales': '6', 'answer': 'even'}
        self.assertEqual(a.classify(trial, row), 'correct')
        self.assertEqual(a.classify(trial, {**row, 'answer': 'odd'}), 'incorrect')
        self.assertEqual(a.classify(trial, {**row, 'answer': ''}), 'no_answer')
        self.assertEqual(a.classify(trial, {**row, 'completed_exhales': ''}), 'unusable_record')
        self.assertEqual(a.classify(trial, {**row, 'observed_phase': ''}), 'unusable_record')
        for changed in ({'observed_phase': 'exhale'}, {'completed_exhales': '7'}, {'completed_exhales': '4'}):
            self.assertEqual(a.classify(trial, {**row, **changed}), 'target_mismatch')
        with self.assertRaises(ValueError):
            a.classify(trial, {**row, 'answer': 'inhale'})
        with self.assertRaises(ValueError):
            a.classify(trial, {**row, 'completed_exhales': '-1'})

    def test_schedule_and_record_validation(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'schedule.csv'
            with path.open('w', newline='') as stream:
                w = csv.writer(stream)
                w.writerow(['participant', 'trial', 'query', 'target_phase', 'target_parity'])
                for t, cell in enumerate(a.CELLS * a.REPETITIONS, 1):
                    w.writerow(['p1', t, *cell])
            original = path.read_text()
            self.assertEqual(len(a.read_schedule(path, {'p1': 'follow'})), a.TRIALS)
            for invalid in [original + original.splitlines()[-1] + '\n',
                            original.replace('p1,1,phase', 'p1,1,history'),
                            original.replace('p1,1,phase', 'p2,1,phase'),
                            original.replace('participant,trial', 'participant,participant')]:
                path.write_text(invalid)
                with self.assertRaises(ValueError):
                    a.read_schedule(path, {'p1': 'follow'})

    def test_complete_roster_with_empty_records_retains_every_person(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            roster, sched, obs = (root / name for name in ['roster.csv', 'schedule.csv', 'obs.csv'])
            with roster.open('w', newline='') as r, sched.open('w', newline='') as s:
                rw, sw = csv.writer(r), csv.writer(s)
                rw.writerow(['participant', 'arm'])
                sw.writerow(['participant', 'trial', 'query', 'target_phase', 'target_parity'])
                for arm in a.ARMS:
                    for i in range(a.PER_ARM):
                        p = f'{arm}{i:04}'
                        rw.writerow([p, arm])
                        for t, cell in enumerate(a.CELLS * a.REPETITIONS, 1):
                            sw.writerow([p, t, *cell])
            header = 'participant,trial,observed_phase,completed_exhales,answer\n'
            obs.write_text(header)
            output = a.analyze(roster, sched, obs)
            self.assertEqual(output['decision'], 'inconclusive')
            self.assertEqual(output['participants_without_any_row'], {arm: a.PER_ARM for arm in a.ARMS})
            self.assertEqual(output['outcomes']['phase']['simultaneous_confidence_interval'], [-1, 1])
            line = 'count0000,1,inhale,6,inhale\n'
            obs.write_text(header + line + line)
            with self.assertRaisesRegex(ValueError, 'duplicate observation'):
                a.analyze(roster, sched, obs)
            roster.write_text('participant,arm\np1,follow\n')
            with self.assertRaisesRegex(ValueError, 'frozen design'):
                a.read_roster(roster)


if __name__ == '__main__':
    unittest.main()
