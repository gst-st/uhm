"""Causal belt detector and probe controller. Outputs requests; score actual delivered markers."""
import argparse
from collections import deque
import csv
from dataclasses import dataclass
from pathlib import Path
from statistics import median_low
import sys

SAMPLE_MS = 10
CALIBRATION_SAMPLES = 6000
WINDOW = 10
DELAY_MS = 250
TIMEOUT_MS = 120_000


def amplitude(values):
    if len(values) != CALIBRATION_SAMPLES:
        raise ValueError('expected 60 s at 100 Hz of quiet baseline')
    values = sorted(values)
    span = values[9*(len(values)-1)//10] - values[(len(values)-1)//10]
    if span <= 0:
        raise ValueError('flat calibration')
    # Input to the detector is the 10-sample SUM, hysteresis one tenth of span.
    return max(1, (WINDOW*span+9)//10)


class Belt:
    """Rising voltage corresponds to chest expansion. Left-to-right, no future samples."""
    def __init__(self, threshold):
        if threshold <= 0:
            raise ValueError('nonpositive hysteresis')
        self.threshold = threshold
        self.recent = deque(maxlen=WINDOW)
        self.phase = None
        self.low = self.high = None
        self.last = None

    def sample(self, ms, value):
        if self.last is not None and ms != self.last + SAMPLE_MS:
            raise ValueError('belt dropout or non-monotonic timestamp')
        self.last = ms
        self.recent.append(value)
        if len(self.recent) < WINDOW:
            return None
        level = sum(self.recent)
        if self.low is None:
            self.low = self.high = level
        self.low, self.high = min(self.low, level), max(self.high, level)
        if self.phase != 'inhale' and level-self.low >= self.threshold:
            self.phase, self.high = 'inhale', level
        elif self.phase != 'exhale' and self.high-level >= self.threshold:
            self.phase, self.low = 'exhale', level
        else:
            return None
        return self.phase


def calibrate(values):
    """Freeze amplitude and a timing-only observer before the assigned practice."""
    threshold = amplitude(values)
    belt = Belt(threshold)
    onsets = [(i*SAMPLE_MS, phase) for i, v in enumerate(values)
              if (phase := belt.sample(i*SAMPLE_MS, v)) is not None]
    full = [(b-a, c-a) for (a,p), (b,q), (c,r) in zip(onsets, onsets[1:], onsets[2:])
            if (p,q,r) == ('inhale','exhale','inhale')]
    if len(full) < 4:
        raise ValueError('fewer than four usable baseline cycles')
    return threshold, median_low([c for _,c in full]), median_low([i for i,_ in full])


@dataclass(frozen=True)
class Marker:
    kind: str
    timestamp_ms: int


class TrialController:
    """One assigned probe. Feed physical acknowledgements back on the same timebase."""
    def __init__(self, target_n, target_phase):
        if target_n < 1 or target_phase not in ('inhale','exhale'):
            raise ValueError('invalid respiratory target')
        self.target = target_n, target_phase
        self.started = self.last = self.pending = self.awaiting = None
        self.anchored = self.done = False
        self.count = 0
        self.phase = None

    def update(self, ms, onset=None):
        if self.last is not None and ms <= self.last:
            raise ValueError('non-monotonic controller clock')
        self.last = ms
        if self.done:
            return None
        if self.started is None:
            self.started = ms
        if ms-self.started >= TIMEOUT_MS:
            self.done = True
            return Marker('timeout', ms)
        if onset is not None:
            if onset not in ('inhale','exhale') or onset == self.phase:
                raise ValueError('invalid online phase transition')
            self.phase = onset
            self.pending = None
            if self.anchored and onset == 'inhale':
                self.count += 1
            if self.awaiting is None:
                if not self.anchored and onset == 'inhale':
                    self.pending = Marker('anchor', ms+DELAY_MS)
                elif self.anchored and (self.count, onset) == self.target:
                    self.pending = Marker('cue', ms+DELAY_MS)
        if self.pending and ms >= self.pending.timestamp_ms:
            self.awaiting = Marker(self.pending.kind, ms)
            self.pending = None
            return self.awaiting
        return None

    def delivered(self, kind, ms):
        if self.done or self.awaiting is None or kind != self.awaiting.kind or ms < self.awaiting.timestamp_ms:
            raise ValueError('unexpected or early physical marker acknowledgement')
        # Asynchronous audio onset must be fed before subsequent belt samples.
        if ms < self.last:
            raise ValueError('late marker acknowledgement; preserve the missed trial')
        self.last = ms
        if kind == 'anchor':
            self.anchored = True
        else:
            self.done = True
        self.awaiting = None


def samples(path):
    with path.open(newline='') as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames != ['timestamp_ms','value']:
            raise ValueError('expected timestamp_ms,value')
        last = None
        for row in reader:
            t, v = int(row['timestamp_ms']), int(row['value'])
            if t < 0 or (last is not None and t != last+SAMPLE_MS):
                raise ValueError('invalid sample grid')
            last = t
            yield t, v


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('baseline', type=Path)
    parser.add_argument('--replay', type=Path, help='single trial belt recording; ideal zero actuator latency')
    parser.add_argument('--target-n', type=int)
    parser.add_argument('--target-phase', choices=('inhale','exhale'))
    args = parser.parse_args()
    try:
        th, period, inhale = calibrate([v for _,v in samples(args.baseline)])
        if args.replay is None:
            print('threshold,period_ms,inhale_ms')
            print(th, period, inhale, sep=',')
        else:
            if args.target_n is None or args.target_phase is None:
                parser.error('--replay requires --target-n and --target-phase')
            controller, belt = TrialController(args.target_n,args.target_phase), Belt(th)
            writer = csv.writer(sys.stdout, lineterminator='\n')
            writer.writerow(('request','timestamp_ms'))
            for t,v in samples(args.replay):
                marker = controller.update(t,belt.sample(t,v))
                if marker:
                    writer.writerow((marker.kind,t))
                    if marker.kind != 'timeout':
                        controller.delivered(marker.kind,t)
                if controller.done:
                    break
            if not controller.done:
                raise ValueError('record ended before probe or timeout')
    except (ValueError,OSError,csv.Error) as e:
        parser.exit(2,f'acquisition error: {e}\n')


if __name__ == '__main__':
    main()
