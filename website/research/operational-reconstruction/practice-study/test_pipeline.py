"""Independent synthetic acquisitions and a complete, sealed no-data analysis."""
from collections import Counter
import csv
from pathlib import Path
import tempfile
import unittest

import acquisition
import analysis
import measure
import study
from timing import clock_diagnostic


def value_at(ms):
    phase = ms % 3000
    return min(phase, 3000-phase)


class Pipeline(unittest.TestCase):
    def test_controller_against_independent_belt_landmarks(self):
        baseline = [value_at(t) for t in range(0,60000,10)]
        threshold, period, inhale = acquisition.calibrate(baseline)
        self.assertEqual((period, inhale), (3000,1500))
        for n in (3,11):
            for phase in ('inhale','exhale'):
                with self.subTest(n=n,phase=phase):
                    ctrl, belt = acquisition.TrialController(n,phase), acquisition.Belt(threshold)
                    receipts = {}
                    for t in range(0,50000,10):
                        marker = ctrl.update(t,belt.sample(t,value_at(t)))
                        if marker:
                            # A real interface would obtain delivery from audio loopback.
                            ctrl.delivered(marker.kind,t+2)
                            receipts[marker.kind] = t+2
                        if ctrl.done:
                            break
                    marks = [(m, ('inhale' if m%3000==0 else 'exhale')) for m in range(0,52000,1500)]
                    result = measure.phase_and_count(marks,receipts['anchor'],receipts['cue'])
                    self.assertEqual(result,((phase,n),'ok'))

    def test_acquisition_guards(self):
        with self.assertRaises(ValueError):
            acquisition.calibrate([3]*6000)
        belt = acquisition.Belt(3)
        belt.sample(0,10)
        with self.assertRaises(ValueError):
            belt.sample(20,5)
        ctrl = acquisition.TrialController(3,'inhale')
        ctrl.update(0,'inhale')
        self.assertEqual(ctrl.update(250).kind,'anchor')
        with self.assertRaises(ValueError):
            ctrl.delivered('cue',251)
        self.assertEqual(ctrl.update(120000).kind,'timeout')

    def test_timing_reader_uses_measured_duration(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            ids, key = root/'ids', root/'key'
            study.write_csv(ids,['participant'],((f'p{i}',) for i in range(2*analysis.PER_ARM)))
            key.write_bytes(bytes(range(32)))
            run = root/'lock'
            published = study.lock(ids,key,run)
            with (run/'schedule.csv').open() as stream:
                trial = next(r for r in csv.DictReader(stream) if r['query']=='history')
            target = int(trial['target_n'])
            elapsed = 4000*(target+1) + (2000 if trial['target_phase']=='exhale' else 0)
            study.write_csv(root/'obs',['participant','trial','observed_phase','completed_exhales','answer','elapsed_ms'],
                [[trial['participant'],trial['trial'],trial['target_phase'],target,'',elapsed]])
            study.write_csv(root/'base',['participant','period_ms','inhale_ms'],[[trial['participant'],4000,2000]])
            diag = clock_diagnostic(run/'roster.csv',run/'schedule.csv',root/'obs',root/'base')
            self.assertEqual(sum(v['observed'] for v in diag.values()),1)
            self.assertEqual(sum(v['correct'] for v in diag.values()),0)
            study.verify(run,published)
            with (run/'schedule.csv').open('a') as out:
                out.write('\n')
            with self.assertRaises(ValueError):
                study.verify(run,published)

    def test_sealed_analysis_with_one_archived_trial(self):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            ids, key, run = tmp/'ids', tmp/'key', tmp/'run'
            study.write_csv(ids, ['participant'], ((f'synthetic{i}',) for i in range(2*analysis.PER_ARM)))
            key.write_bytes(bytes(reversed(range(32))))
            sha = study.lock(ids,key,run)
            roster = analysis.read_roster(run/'roster.csv')
            with (run/'schedule.csv').open() as stream:
                row = next(csv.DictReader(stream))
            person, trial = row['participant'], row['trial']
            n = int(row['target_n'])
            anchor = 250
            cue = anchor+n*3000+(1500 if row['target_phase']=='exhale' else 0)
            label = row['target_phase'] if row['query']=='phase' else row['target_parity']
            buttons = next(r['buttons'] for r in analysis.rows(run/'roster.csv',['participant','buttons'])
                           if r['participant']==person)
            answer = 'right' if ((label in ('exhale','odd')) ^ (buttons=='reversed')) else 'left'
            files = {k:tmp/(k+'.csv') for k in ['events','landmarks','baseline','raw_index']}
            study.write_csv(files['events'],['participant','trial','kind','timestamp_ms','value'],
                [(person,trial,k,t,v) for k,t,v in [('anchor',anchor,''),('cue',cue,row['query']),('answer',cue+300,answer)]])
            study.write_csv(files['landmarks'],['participant','trial','rater','kind','timestamp_ms'],
                ((person,trial,r,'inhale' if m%3000==0 else 'exhale',m)
                 for r in ('a','b') for m in range(0,cue+3000,1500)))
            study.write_csv(files['baseline'],['participant','period_ms','inhale_ms'],[(person,3000,1500)])
            raw = tmp/'raw'
            raw.mkdir()
            bundle = tmp/'synthetic-trace'
            bundle.write_bytes(b'synthetic integrity fixture, no human records')
            content_digest = study.digest(bundle)
            bundle.rename(raw/content_digest)
            study.write_csv(files['raw_index'],['participant','sha256'],[(person,content_digest)])
            locked = study.results_commit(files)
            res = study.score(run,sha,locked,files,raw)
            self.assertEqual(res['decision'],'inconclusive')
            self.assertEqual(res['adjudication_reasons'],{'ok':1,'no_acquisition':89599})
            self.assertEqual(res['participants_without_any_row'][roster[person]],analysis.PER_ARM-1)
            self.assertEqual(res['outcomes'][row['query']]['arms'][roster[person]]['counts']['correct'],1)
            with self.assertRaises(ValueError):
                study.score(run,sha,'0'*64,files,raw)
            (raw/content_digest).write_bytes(b'changed')
            with self.assertRaises(ValueError):
                study.score(run,sha,locked,files,raw)

    def test_distinct_pilot_and_masked_feasibility_gate(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            ids, key, run = root/'pilot-ids', root/'key', root/'pilot'
            study.write_csv(ids, ['participant'], ((f'pilot{i}',) for i in range(2*study.PILOT_PER_ARM)))
            key.write_bytes(bytes(32))
            sha = study.lock(ids,key,run,pilot=True)
            with self.assertRaisesRegex(ValueError, 'stage'):
                study.verify(run,sha)
            roster = analysis.read_roster(run/'roster.csv',study.PILOT_PER_ARM)
            plan = analysis.read_schedule(run/'schedule.csv',roster)
            rows = [[p,t,'ok'] for p,t in plan]
            indices = [i for i,(p,t) in enumerate(plan) if plan[p,t].query=='phase' and roster[p]=='count']
            for i in indices[:6]:
                rows[i][2] = 'no_answer'
            f = root/'obs'
            study.write_csv(f,['participant','trial','reason'],rows)
            report = study.pilot_qc(roster,run/'schedule.csv',f)
            self.assertEqual(report,{'unknown_phase_in_anonymous_groups':[0,6],
                                     'phase_slots_per_group':320,'quality_gate_passed':True})
            f.unlink()
            rows[indices[6]][2] = 'late_answer'
            study.write_csv(f,['participant','trial','reason'],rows)
            self.assertFalse(study.pilot_qc(roster,run/'schedule.csv',f)['quality_gate_passed'])
            f.unlink()
            study.write_csv(f,['participant','trial','reason'],[])
            empty = study.pilot_qc(roster,run/'schedule.csv',f)
            self.assertEqual(empty['unknown_phase_in_anonymous_groups'],[320,320])

    def test_target_balance_and_wrap(self):
        layout = study.trials_for('synthetic', bytes(32))
        self.assertEqual(len(layout),32)
        self.assertEqual(Counter((q,p,y) for q,p,y,_ in layout), Counter({cell:4 for cell in analysis.CELLS}))
        for q,p in [(q,p) for q in analysis.QUERIES for p in analysis.PHASES]:
            selected = [(y,n) for query,phase,y,n in layout if (q,p)==(query,phase)]
            self.assertEqual(sum(n for y,n in selected if y=='even'),sum(n for y,n in selected if y=='odd'))
            self.assertEqual({n for _,n in selected},set(measure.TARGET_COUNTS))


if __name__ == '__main__':
    unittest.main()
