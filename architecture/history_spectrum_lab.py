# -*- coding: utf-8 -*-
"""history_spectrum_lab.py — П8/P8a: есть ли у истории полоса культурного холона?

Пререгистрация: RECON-TOTAL §П8 (H1 saeculum 60–100 лет, H2 Кондратьев
40–60, H3 сцепление пандемия→революция [0,+10], H4 негативный контроль
8–15 лет; ДВА нуля — gap-shuffle и локальный джиттер; p = max, Холм m=4).

Метод: точечный процесс дат → нормированная периодограмма Ломба–Скаргла
на сетке периодов; статистика полосы = МАКСИМУМ мощности внутри полосы.
Нули: N1 = перестановка наблюдённых интервалов + случайная посадка окна;
N2 = локальный джиттер ±7 лет (порядок и тренд плотности сохранены).

run: python3 architecture/history_spectrum_lab.py
"""
import csv
import math
import random
from pathlib import Path

HERE = Path(__file__).parent
PH = HERE / "data" / "p7_phases.csv"
SEED = 20260727
NP = 2000
JIT = 7.0

BANDS = [("H1 saeculum 60-100", 60.0, 100.0),
         ("H2 Кондратьев 40-60", 40.0, 60.0),
         ("H4 контроль 8-15", 8.0, 15.0)]


def load():
    ev = {}
    for r in csv.DictReader(open(PH)):
        y, m = r["date"].split("-")[:2]
        t = int(y) + (int(m) - 0.5) / 12.0
        ev.setdefault(r["tag"], []).append(t)
    ev["all"] = sorted(ev["war"] + ev["rev"] + ev["pan"])
    for k in ev:
        ev[k] = sorted(ev[k])
    return ev


def lomb_power(times, period):
    """Нормированная мощность Ломба–Скаргла для точечного процесса:
    ряд = единичные импульсы, центрированные (среднее вычтено)."""
    w = 2.0 * math.pi / period
    n = len(times)
    # τ-сдвиг Ломба
    s2 = sum(math.sin(2 * w * t) for t in times)
    c2 = sum(math.cos(2 * w * t) for t in times)
    tau = math.atan2(s2, c2) / (2 * w)
    cs = sum(math.cos(w * (t - tau)) for t in times)
    sn = sum(math.sin(w * (t - tau)) for t in times)
    cc = sum(math.cos(w * (t - tau)) ** 2 for t in times)
    ss = sum(math.sin(w * (t - tau)) ** 2 for t in times)
    p = 0.0
    if cc > 1e-9:
        p += cs * cs / cc
    if ss > 1e-9:
        p += sn * sn / ss
    return p / n


def band_stat(times, lo, hi, steps=60):
    return max(lomb_power(times, lo + (hi - lo) * k / (steps - 1))
               for k in range(steps))


def null_gap(times, rng, tmin, tmax):
    gaps = [b - a for a, b in zip(times, times[1:])]
    rng.shuffle(gaps)
    span = sum(gaps)
    start = rng.uniform(tmin, max(tmin, tmax - span))
    out = [start]
    for g in gaps:
        out.append(out[-1] + g)
    return out


def null_jitter(times, rng):
    return sorted(t + rng.uniform(-JIT, JIT) for t in times)


def main():
    ev = load()
    tmin = min(ev["all"]) - 5
    tmax = max(ev["all"]) + 5
    print("каталоги: " + ", ".join(f"{k}={len(v)}" for k, v in ev.items()))
    print(f"нули: gap-shuffle и джиттер ±{JIT:.0f} лет, {NP} ресемплов\n")
    rows = []
    for series in ("all", "war", "rev", "pan"):
        ts = ev[series]
        for name, lo, hi in BANDS:
            obs = band_stat(ts, lo, hi)
            r1 = random.Random(SEED)
            r2 = random.Random(SEED + 1)
            c1 = sum(1 for _ in range(NP)
                     if band_stat(null_gap(ts, r1, tmin, tmax), lo, hi) >= obs)
            c2 = sum(1 for _ in range(NP)
                     if band_stat(null_jitter(ts, r2), lo, hi) >= obs)
            p1, p2 = c1 / NP, c2 / NP
            rows.append((series, name, obs, p1, p2, max(p1, p2)))
            print(f"{series:4} {name:22} P={obs:5.2f}  p_gap={p1:.3f}  "
                  f"p_jit={p2:.3f}  p={max(p1, p2):.3f}")

    print("\n[H3] сцепление: пандемия → революция в окне [0,+10] лет")
    pan, rev = ev["pan"], ev["rev"]
    obs = sum(1 for p in pan for r in rev if 0.0 <= r - p <= 10.0)
    r1 = random.Random(SEED + 2)
    r2 = random.Random(SEED + 3)
    def count(pp, rr):
        return sum(1 for p in pp for r in rr if 0.0 <= r - p <= 10.0)
    c1 = sum(1 for _ in range(NP)
             if count(pan, null_gap(rev, r1, tmin, tmax)) >= obs)
    c2 = sum(1 for _ in range(NP)
             if count(pan, null_jitter(rev, r2)) >= obs)
    p1, p2 = c1 / NP, c2 / NP
    print(f"  пар в окне: {obs};  p_gap={p1:.3f}  p_jit={p2:.3f}  "
          f"p={max(p1, p2):.3f}")

    print("\nХолм (m=4) по ЗАЯВЛЕННЫМ гипотезам на объединённом потоке:")
    claim = [(n, p) for (s, n, _o, _a, _b, p) in rows
             if s == "all"] + [("H3 пандемия→революция", max(p1, p2))]
    claim.sort(key=lambda x: x[1])
    m = len(claim)
    for k, (n, p) in enumerate(claim):
        print(f"  {n:24} p={p:.3f} -> Holm={min(1.0, p * (m - k)):.3f}")


if __name__ == "__main__":
    main()
