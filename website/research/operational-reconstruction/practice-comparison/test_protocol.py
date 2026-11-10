"""Synthetic allocation replay and tampering controls; no cohort outcomes."""
import csv
from collections import Counter
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

import capacity_score
import protocol
import score


class ProtocolTests(unittest.TestCase):
    def test_concealed_draws(self):
        secret = bytes(range(32))
        orders = list(protocol.schedule('order','P',secret))
        self.assertEqual(orders, list(protocol.schedule('order','P',secret)))
        for b in score.BLOCKS:
            self.assertEqual(Counter(seq for _,block,_,seq in orders if block==b), score.DESIGN)
        seen = []
        for i in range(20):
            data = list(protocol.schedule('capacity',str(i),secret))
            self.assertEqual(len(data),24)
            seen.extend(data)
        self.assertEqual({row[2] for row in seen},set(capacity_score.WORDS))
        self.assertNotEqual([row[3] for row in seen[:24]], [row[3] for row in seen[24:48]])
        self.assertNotEqual(Counter(row[3] for row in seen[:24]),
                            Counter(row[3] for row in seen[24:48]))

    def test_freeze_analysis_and_tampering(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            ids, secret, obs = (root / n for n in ('ids.csv','key','obs.csv'))
            secret.write_bytes(bytes(range(32)))
            for study, scorer, header in (
                ('order',score,'participant,block,trial,delivered,first,last'),
                ('capacity',capacity_score,'participant,trial,delivered_target,delivered_cue,answer')):
                with self.subTest(study=study):
                    n = scorer.PER_ARM
                    ids.write_text('participant\n'+''.join(f'X{i}\n' for i in range(2*n)))
                    dest = root/study
                    freeze = protocol.freeze(study,ids,secret,dest)
                    with (dest/'roster.csv').open() as f:
                        cells = Counter((r['arm'],r['buttons']) for r in csv.DictReader(f))
                    self.assertEqual(len(cells),4)
                    self.assertEqual(set(cells.values()),{n//2})
                    obs.write_text(header+'\n')
                    outcome = protocol.digest(obs)
                    result = protocol.analyze(dest,freeze,obs,outcome)
                    for arm in score.ARMS:
                        self.assertEqual(result['result']['arms'][arm]['without_any_row'],n)
                    with self.assertRaisesRegex(ValueError,'sealed observation'):
                        protocol.analyze(dest,freeze,obs,'0'*64)
                    with (dest/'manifest.csv').open('a') as f:
                        f.write('\n')
                    with self.assertRaisesRegex(ValueError,'allocation changed'):
                        protocol.analyze(dest,freeze,obs,outcome)
                    with self.assertRaisesRegex(ValueError,'pre-session'):
                        protocol.analyze(dest,'0'*64,obs,outcome)


if __name__=='__main__':
    unittest.main()
