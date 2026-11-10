"""Protocol controls, with exact synthetic counts, never empirical evidence."""
import unittest
from itertools import chain
from reference_trial import ARMS, N, evaluate

def rows(values, miss=()):
    for arm in ARMS:
        for i in range(1,N+1):
            yield dict(arm=arm,slot=str(i),a='+',b='NA' if arm in miss
                       else '+' if i <= values[arm] else '-')

class Protocol(unittest.TestCase):
    # Source strengths 1, 1, 1/2, -1/2; agreement counts including the blinded pair.
    counts=dict(zip(ARMS,[6000,4500,1500,2250,3000,0,6000,6000],strict=True))

    def test_heldout(self):
        ref=evaluate(rows(self.counts))
        self.assertEqual(ref['failed'],[])
        bad=evaluate(rows({**self.counts,'34':5000}))
        self.assertEqual(bad['failed'],['held-out four-source equality'])
        self.assertEqual(bad['predicted_34_from_calibration'],ref['predicted_34_from_calibration'])

    def test_censor_and_zero(self):
        r=evaluate(rows({**self.counts,'12':N//2},miss=ARMS))
        self.assertEqual(r['failed'],[])
        self.assertIsNone(r['predicted_34_from_calibration'])
        self.assertEqual(r['missing']['12'],N)
        self.assertEqual(r['correlations']['12'],['-1','1'])

    def test_manifest(self):
        sample=rows(self.counts)
        first=next(sample)
        with self.assertRaisesRegex(ValueError,'repeated'):
            evaluate(chain([first,first],sample))
        with self.assertRaisesRegex(ValueError,'incomplete'):
            evaluate([first])

if __name__=='__main__':
    unittest.main()
