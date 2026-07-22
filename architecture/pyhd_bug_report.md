# Bug report for `ppo/pyhd` — ready to file upstream

*Prepared 2026-07-22 during an independent cross-verification of the Human
Design calculation machinery (two independent engines, 300 random datetimes).
All numbers below are reproducible; the diff is one line.*

---

**Title:** Manifesting Generator misclassified as Pure Generator when the only
motor–throat link is channel 20–34 (Sacral–Throat)

**Summary.** `Chart.type` computes the throat connection against
`NON_SACRAL_MOTOR_CENTERS` only:

```python
has_throat_connection = self.is_connected(Centers.THROAT, NON_SACRAL_MOTOR_CENTERS)
```

For a chart whose only motor-to-throat connection is the channel **20–34
(Sacral–Throat)** — the textbook Manifesting-Generator channel (*The
Definitive Book of Human Design*, p. 123: “Manifesting Generator: A Motor
Center connected to Throat”, with the Sacral listed among the four motors on
p. 116) — `has_throat_connection` is `False`, and the chart falls through to
`Types.PURE_GENERATOR`.

**Expected.** Sacral defined **and** any motor (including the Sacral itself)
connected to the Throat ⇒ `MANIFESTING_GENERATOR`.

**Impact.** In a Monte-Carlo sweep of 300 uniform random UTC datetimes
(1930–2000), 25 charts (≈ 8%) were affected — every one of them a
20–34-mediated case; an independent reimplementation following the book
agreed with `pyhd` on gates, channels, center counts and profiles **300/300**
and diverged on types **only** in these 25 cases.

**Suggested fix** (one line):

```python
has_throat_connection = self.is_connected(Centers.THROAT, MOTOR_CENTERS)
```

(The Manifestor branch is unaffected: when the Sacral is undefined, the motor
set effectively reduces to the non-sacral three.)

**Repro.** Any datetime whose chart defines 20–34 with no other motor–throat
channel; e.g. sample dates are easy to find by sweeping — in our sweep the
first occurrence was within the first dozen random draws. A minimal check:

```python
from datetime import datetime, timezone
from pyhd.chart import Chart
# pick any datetime where gates 20 and 34 are both activated and no other
# motor-throat channel is defined; Chart.type returns PURE_GENERATOR,
# expected MANIFESTING_GENERATOR per book p.123.
```

**Secondary observation** (separate, minor): in `Chart.type`, the
projector-subtype branches test `if not other_defined_centers:` where
`other_defined_centers` is a *generator expression* — always truthy, so the
condition is always `False` and the subtype logic is unreachable as written.

*Thanks for the library — the page-referenced constants made independent
verification a pleasure.*
