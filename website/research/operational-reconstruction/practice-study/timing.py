"""Prespecified descriptive timing comparator; it does not model all information a person can use."""
from collections import Counter
from analysis import PER_ARM, TRIALS, classify, key_of, natural, parity_of, read_roster, read_schedule, rows


def clock_diagnostic(roster_path, schedule_path, observations, baseline_path):
    roster = read_roster(roster_path)
    assignments = read_schedule(schedule_path, roster)
    calibration = {}
    for row in rows(baseline_path, ['participant','period_ms','inhale_ms']):
        p = row['participant']
        if p not in roster or p in calibration:
            raise ValueError('unknown or duplicate baseline participant')
        period, inhale = (natural(row[k], k) for k in ('period_ms','inhale_ms'))
        if not 0 < inhale < period:
            raise ValueError('invalid baseline period or inspiratory duration')
        calibration[p] = period, inhale
    scored, correct = Counter(), Counter()
    cells = {}
    seen = set()
    for row in rows(observations, ['participant','trial','observed_phase','completed_exhales','answer','elapsed_ms']):
        key = key_of(row, roster)
        if key in seen:
            raise ValueError('duplicate measurement')
        seen.add(key)
        p, _ = key
        trial = assignments[key]
        if trial.query != 'history' or p not in calibration or not row['elapsed_ms']:
            continue
        if classify(trial, row) not in ('correct','incorrect','no_answer'):
            continue
        elapsed = natural(row['elapsed_ms'],'elapsed_ms')
        period, inhale = calibration[p]
        # Both physical markers use the same requested latency after onset; it
        # cancels. During expiration, subtract the baseline inspiratory phase.
        remaining = max(0, elapsed - (inhale if row['observed_phase']=='exhale' else 0))
        predicted = parity_of((2*remaining + period)//(2*period))
        truth = parity_of(int(row['completed_exhales']))
        arm = roster[p]
        scored[arm] += 1
        correct[arm] += (predicted == truth)
        cells.setdefault((p, row['observed_phase'], predicted), Counter())[truth] += 1
    n = PER_ARM*(TRIALS//2)
    result = {}
    for arm in ('count','follow'):
        unknown = n-scored[arm]
        envelope = sum(max(counts.values()) for (p,_,_),counts in cells.items() if roster[p]==arm)
        result[arm] = {'scheduled':n,'observed':scored[arm],'correct':correct[arm],
            'duration_rule_fraction_bounds':[correct[arm]/n,(correct[arm]+unknown)/n],
            'empirical_class_ceiling_including_unknown_as_correct':(envelope+unknown)/n}
    return result
