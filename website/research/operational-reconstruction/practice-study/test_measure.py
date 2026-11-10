import csv
import tempfile
import unittest
from pathlib import Path

import measure as m


def regular_belt():
    return [(i*500, 'inhale' if i % 2 == 0 else 'exhale') for i in range(11)]


class MeasureTests(unittest.TestCase):
    def setUp(self):
        self.target = ('history', 'inhale', 3)
        self.events = {'anchor': (200,''), 'cue': (3250,''), 'answer': (3450,'odd')}
        self.marks = {'a': regular_belt(), 'b': regular_belt()}

    def observe(self):
        return m.reconstruct(('P',1), self.target, self.events, self.marks)

    def test_registered_anchor_and_query(self):
        self.assertEqual(self.observe(), dict(participant='P', trial=1, observed_phase='inhale',
                                             completed_exhales=3, answer='odd', elapsed_ms=3050, reason='ok'))
        self.target = ('phase','exhale',3)
        self.events.update(cue=(3750,''), answer=(3800,'exhale'))
        self.assertEqual(self.observe()['observed_phase'], 'exhale')
        self.assertEqual(self.observe()['completed_exhales'], 3)

    def test_agreement_is_on_physiology_independently_of_target(self):
        self.target = ('history', 'inhale', 5)
        row = self.observe()
        self.assertEqual((row['completed_exhales'], row['reason']), (3,'target_mismatch'))
        self.marks['b'] = [x for x in self.marks['b'] if x[0] not in (1000,1500)]
        row = self.observe()
        self.assertEqual((row['observed_phase'], row['completed_exhales'], row['reason']), ('','','rater_disagreement'))

    def test_different_displayed_question_is_not_scored(self):
        self.events['cue'] = (3250,'phase')
        row = self.observe()
        self.assertEqual((row['reason'],row['answer']), ('wrong_or_unverified_question',''))

    def test_buffer_coverage_and_guard(self):
        marks = regular_belt()
        self.assertEqual(m.phase_and_count(marks, 150, 3150), (('inhale',3),'ok'))
        for anchor, cue in [(149,3250),(351,3250),(200,3149),(200,3351),(200,3500)]:
            self.assertEqual(m.phase_and_count(marks,anchor,cue), (None,'boundary_guard'))
        self.assertEqual(m.phase_and_count(marks[1:],200,3250), (None,'unbracketed'))
        self.assertEqual(m.phase_and_count(marks[:-4],200,3250), (None,'unbracketed'))
        self.assertEqual(m.phase_and_count(marks,750,3250), (None,'anchor_not_inhale'))

    def test_artifacts_and_malformed_phase_sequence(self):
        marks = regular_belt()
        self.assertEqual(m.phase_and_count(sorted(marks+[(20,'artifact')]),200,3250), (None,'artifact'))
        self.assertEqual(m.phase_and_count(sorted(marks+[(3600,'artifact')]),200,3250), (('inhale',3),'ok'))
        self.assertEqual(m.phase_and_count(marks[:1]+marks[2:],200,3250), (None,'nonalternating'))
        self.assertEqual(m.phase_and_count(sorted(marks+[(0,'exhale')]),200,3250), (None,'nonalternating'))

    def test_missing_timeout_and_impossible_order(self):
        self.events['answer'] = (8250,'even')
        self.assertEqual(self.observe()['answer'], 'even')
        self.events['answer'] = (8251,'even')
        row = self.observe()
        self.assertEqual((row['answer'],row['reason'],row['completed_exhales']), ('','late_answer',3))
        del self.events['answer']
        self.assertEqual(self.observe()['reason'],'no_answer')
        self.events['answer'] = (3200,'odd')
        with self.assertRaises(ValueError):
            self.observe()
        self.events.pop('anchor')
        self.events.pop('answer')
        self.assertEqual(self.observe()['reason'],'missing_anchor')

    def test_rater_or_events_absent(self):
        self.marks['a'] = []
        row = self.observe()
        self.assertEqual((row['answer'], row['reason'], row['completed_exhales']), ('odd','missing_landmarks_a',''))
        del self.events['cue']
        row = self.observe()
        self.assertEqual((row['reason'],row['elapsed_ms']), ('missing_cue',''))

    def test_file_pipeline_unsorted_no_fabrication_and_atomicity(self):
        with tempfile.TemporaryDirectory() as tmp:
            plan, events, marks, out = [Path(tmp)/s for s in ['plan.csv','events.csv','marks.csv','out.csv']]
            plan.write_text('participant,trial,query,target_phase,target_parity,target_n\nP,1,history,inhale,odd,3\nP,2,phase,inhale,even,4\n')
            body = 'participant,trial,kind,timestamp_ms,value\nP,1,answer,3450,odd\nP,1,anchor,200,\nP,1,cue,3250,\n'
            events.write_text(body)
            header = 'participant,trial,rater,kind,timestamp_ms\n'
            annotations = ''.join(f'P,1,{r},{kind},{t}\n' for t,kind in reversed(regular_belt()) for r in ['b','a'])
            marks.write_text(header + annotations)
            m.measure(plan,events,marks,out)
            with out.open(newline='') as f:
                a,b = csv.DictReader(f)
            self.assertEqual((a['completed_exhales'],a['reason']), ('3','ok'))
            self.assertEqual((b['completed_exhales'],b['answer'],b['reason']), ('','','no_acquisition'))
            original = out.read_bytes()
            for extra in ['P,1,anchor,300,\n','P,15,anchor,10,\n','P,2,cue,-2,\n',
                          'P,2,anchor,400,\nP,2,cue,390,\n']:
                events.write_text(body+extra)
                with self.assertRaises(ValueError):
                    m.measure(plan,events,marks,out)
                self.assertEqual(out.read_bytes(),original)
            events.write_text(body)
            marks.write_text(header+annotations+'P,1,b,inhale,0\n')
            with self.assertRaisesRegex(ValueError,'duplicate'):
                m.measure(plan,events,marks,out)
            with self.assertRaisesRegex(ValueError,'replace an input'):
                m.measure(plan,events,marks,events)


if __name__ == '__main__':
    unittest.main()
