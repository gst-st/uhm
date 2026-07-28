# -*- coding: utf-8 -*-
"""phase_from_lag_lab.py — П9/P9a: восстановима ли ФАЗА связки из лид-лага?

Пререгистрация: RECON-TOTAL §П9. Утверждение, которое проверяем: 21
фазовая компонента Γ, объявленная феноменально невидимой (§84), на деле
измерима из ВРЕМЕННОГО РЯДА чек-инов — потому что фаза связки есть
«кто ведёт, кто отвечает», а это лид-лаг.

Генеративная модель (честно [С], названа целиком): семь оценок —
дискретизованное наблюдение линейного процесса Орнштейна–Уленбека
    dx = −(S + A)x dt + σ dW,
S симметричная (релаксация к своему), A антисимметричная (ротация между
голосами — «ведёт/отвечает»). Наблюдаем y_t = round(clip(5 + k·x_t, 0, 10)) —
ровно то, что человек ставит в /checkin.

Оценщик: Â ∝ антисимметричная часть лаг-1 ковариации,
    M = C(1)·C(0)⁻¹ ,  Â_est = −(M − Mᵀ)/2 (первый порядок по dt).
Метрики: (1) доля пар с ВЕРНЫМ ЗНАКОМ лид-лага (главная — продукту нужен
знак, не величина); (2) корреляция Спирмена величин |A| истина↔оценка;
(3) кривая объёма по числу дней 30/60/90/180/365; (4) НУЛЬ: перемешивание
дней (разрушает лаг, сохраняет распределения) — доля верных знаков
обязана падать к 50%.

run: python3 architecture/phase_from_lag_lab.py
"""
import numpy as np

N = 7
RNG = np.random.default_rng(20260727)
DT = 1.0        # один день — один шаг
SIGMA = 1.0
K_SCALE = 2.0   # шкала оценок: x≈±2.5 → 0..10 с центром 5
DAYS = [30, 60, 90, 180, 365]
TRIALS = 40


def make_truth(rng, a_strength=0.35):
    """S: положительно определённая релаксация; A: антисимметричная ротация.

    Дрейф НОРМИРУЕТСЯ: спектральный радиус B ≤ 0.5/сут — иначе явная схема
    неустойчива, ряд взрывается, а округление 0–10 маскирует взрыв
    клиппингом (артефакт пойман первым прогоном 2026-07-27: «без
    округления» выходило ХУЖЕ округлённого — верный признак поломки).
    """
    q = rng.normal(size=(N, N))
    S = q @ q.T / N + np.eye(N) * 0.6
    r = rng.normal(size=(N, N)) * a_strength
    A = (r - r.T) / 2
    B = S + A
    rad = max(abs(np.linalg.eigvals(B)))
    scale = 0.5 / rad
    return S * scale, A * scale


SUB = 20  # подшагов в сутки: dt_sub = 1/20 ⟹ ||B||·dt ≪ 1


def simulate(S, A, days, rng, round_it=True):
    B = S + A
    dt = DT / SUB
    x = np.zeros(N)
    # прогрев до стационарности
    for _ in range(200 * SUB):
        x = x - B @ x * dt + SIGMA * np.sqrt(dt) * rng.normal(size=N)
    out = np.empty((days, N))
    for t in range(days):
        for _ in range(SUB):
            x = x - B @ x * dt + SIGMA * np.sqrt(dt) * rng.normal(size=N)
        out[t] = x
    sd = out.std(axis=0)
    sd[sd < 1e-9] = 1.0
    y = 5.0 + K_SCALE * out / sd  # шкала: ±2σ укладывается в 0–10
    if round_it:
        y = np.clip(np.rint(y), 0, 10)
    return y


def estimate_A(y):
    z = y - y.mean(axis=0)
    C0 = z[:-1].T @ z[:-1] / max(1, len(z) - 1)
    C1 = z[1:].T @ z[:-1] / max(1, len(z) - 1)
    try:
        M = C1 @ np.linalg.pinv(C0)
    except np.linalg.LinAlgError:
        return np.zeros((N, N))
    return -(M - M.T) / 2


def sign_hit(Atrue, Aest, top=None):
    iu = np.triu_indices(N, 1)
    t, e = Atrue[iu], Aest[iu]
    if top is not None:
        idx = np.argsort(-np.abs(t))[:top]
        t, e = t[idx], e[idx]
    ok = np.sign(t) == np.sign(e)
    return ok.mean()


def spearman(a, b):
    ra = np.argsort(np.argsort(a))
    rb = np.argsort(np.argsort(b))
    ra = ra - ra.mean()
    rb = rb - rb.mean()
    d = np.sqrt((ra ** 2).sum() * (rb ** 2).sum())
    return float((ra * rb).sum() / d) if d > 0 else 0.0


def main():
    print("П9/P9a — фаза из лид-лага, валидация на синтетике")
    print(f"модель: OU dx=-(S+A)x dt+σdW, наблюдение = round(clip(5+2x,0,10))")
    print(f"{TRIALS} испытаний на точку; N=7 голосов, 21 пара\n")
    print(f"{'дней':>5} {'знак все21':>11} {'знак топ-7':>11} "
          f"{'ρ|A|':>7} {'НУЛЬ(шафл)':>11}")
    iu = np.triu_indices(N, 1)
    for days in DAYS:
        hits, hits_top, rhos, nulls = [], [], [], []
        for k in range(TRIALS):
            rng = np.random.default_rng(20260727 + k)
            S, A = make_truth(rng)
            y = simulate(S, A, days, rng)
            Ae = estimate_A(y)
            hits.append(sign_hit(A, Ae))
            hits_top.append(sign_hit(A, Ae, top=7))
            rhos.append(spearman(np.abs(A[iu]), np.abs(Ae[iu])))
            ysh = y[rng.permutation(len(y))]
            nulls.append(sign_hit(A, estimate_A(ysh)))
        print(f"{days:5d} {np.mean(hits):10.1%} {np.mean(hits_top):11.1%} "
              f"{np.mean(rhos):7.2f} {np.mean(nulls):10.1%}")

    print("\nбез округления (потолок метода — сколько теряет шкала 0–10):")
    for days in (90, 365):
        hits, hits_top = [], []
        for k in range(TRIALS):
            rng = np.random.default_rng(20260727 + k)
            S, A = make_truth(rng)
            y = simulate(S, A, days, rng, round_it=False)
            Ae = estimate_A(y)
            hits.append(sign_hit(A, Ae))
            hits_top.append(sign_hit(A, Ae, top=7))
        print(f"{days:5d} {np.mean(hits):10.1%} {np.mean(hits_top):11.1%}")

    print("\nслабая ротация (A×0.5 — консервативный человек):")
    for days in (90, 180, 365):
        hits, hits_top = [], []
        for k in range(TRIALS):
            rng = np.random.default_rng(20260727 + k)
            S, A = make_truth(rng, a_strength=0.175)
            y = simulate(S, A, days, rng)
            Ae = estimate_A(y)
            hits.append(sign_hit(A, Ae))
            hits_top.append(sign_hit(A, Ae, top=7))
        print(f"{days:5d} {np.mean(hits):10.1%} {np.mean(hits_top):11.1%}")


if __name__ == "__main__":
    main()
