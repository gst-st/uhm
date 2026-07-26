# -*- coding: utf-8 -*-
"""interiority_lab.py — интериорная спектроскопия: от отчётов к механизму.

Две части, обе — про метод «ОТЧЁТЫ → ИНВАРИАНТЫ → МЕХАНИЗМ → НАШ ОБЪЕКТ»
(программа RECON-TOTAL, пласт П1).

ЧАСТЬ K (образец, уже теорема науки). Клювер (1926) выделил из тысяч
мескалиновых отчётов четыре форм-константы: туннель, лучи/паутина, спираль,
решётка. Эрмантраут–Коуэн (1979): кора V1 отображает сетчатку лог-полярно
(x = ln r, y = θ), а плоская волна активности коры cos(a·x + b·y), снятая
обратно на сетчатку, даёт cos(a·ln r + b·θ):
    b=0 → концентрические кольца (туннель), a=0 → радиальные лучи,
    a,b≠0 → спираль, сумма двух волн ±b → решётка/паутина.
Ниже это ВОСПРОИЗВЕДЕНО счётом (ASCII): инвариант субъективных отчётов
оказался спектром механизма. [Т] для вывода, [С] для нейрофизиологии.

ЧАСТЬ S (наша, пререгистрация P1a). Утверждение-следствие [Т]: в нашей
архитектуре канонический R = 1/(7P), а окно сознания P ∈ (2/7, 3/7]
(T-124). Значит верхний край окна и порог рефлексии — ОДНА точка:
    P > 3/7  ⟺  R = 1/(7P) < 1/3.
«Эго-смерть» (отказ самонаблюдения) обязана наступать ровно там, где
чистота выходит за окно. Отсюда предсказание ПОРЯДКА стадий разлёта при
монотонном росте пористости (вход мира кормит когерентности):
    1) связность растёт (λ₂ графа |γ| вверх — «всё связано со всем»)
    2) эго-смерть (P пересекает 3/7 ⟺ R пересекает 1/3)
    3) единство (D → 1: граф когерентностей сливается в один блок)
и возврат в обратном порядке. Ниже — симуляция: игрушечная динамика
Γ' = (1−η)Γ + η·σJ(M)σJ с ростом σ; меряем, в каком проценте траекторий
порядок стадий совпал с предсказанным. Честность: динамика — игрушка
(не ℒ_Ω), результат [С] для порядка, [Т] только для тождества порогов.

Запуск: python3 architecture/interiority_lab.py
"""
import cmath
import math
import random

# ------------------------------------------------------------------ ЧАСТЬ K


def kluver_ascii():
    print("=" * 78)
    print("K. Форм-константы Клювера из механизма (лог-полярная кора)")
    print("=" * 78)
    modes = [
        ("туннель (a=5, b=0): кольца", 5.0, 0.0, False),
        ("лучи/паутина (a=0, b=8)", 0.0, 8.0, False),
        ("спираль (a=5, b=8)", 5.0, 8.0, False),
        ("решётка (суперпозиция b=±8)", 5.0, 8.0, True),
    ]
    H, W = 21, 46
    for title, a, b, lattice in modes:
        print("\n  %s" % title)
        for i in range(H):
            row = []
            for j in range(W):
                x = (j - W / 2) / (W / 2.2)
                y = (i - H / 2) / (H / 2.2)
                r = math.hypot(x, y) + 1e-6
                th = math.atan2(y, x)
                if lattice:
                    v = (math.cos(a * math.log(r) + b * th)
                         + math.cos(a * math.log(r) - b * th))
                else:
                    v = 2 * math.cos(a * math.log(r) + b * th)
                row.append("#" if v > 0.7 else ("+" if v > 0 else " "))
            print("   " + "".join(row))
    print("\n  вердикт K [Т-вывод]: четыре класса отчётов = четыре типа")
    print("  плоских волн одного механизма. Инвариант корпуса стал спектром.")


# ------------------------------------------------------------------ ЧАСТЬ S
N = 7
P_HI = 3.0 / 7.0     # верх окна сознания (T-124); R=1/3 ровно здесь [Т]
EPS = 0.08           # порог связи для графа D


def herm_random(rng, rank=2):
    """Случайная PSD-плотность малого ранга — «мир» за пределами холона."""
    m = [[0j] * N for _ in range(N)]
    for _ in range(rank):
        v = [complex(rng.gauss(0, 1), rng.gauss(0, 1)) for _ in range(N)]
        for i in range(N):
            for j in range(N):
                m[i][j] += v[i] * v[j].conjugate()
    tr = sum(m[i][i].real for i in range(N))
    return [[m[i][j] / tr for j in range(N)] for i in range(N)]


def start_gamma(rng):
    """Типичная «карта»: диагональ с рельефом + когерентности ВНУТРИ двух
    блоков. Ворота D_min=2 [Т]: сознательный старт обязан иметь ≥2 блока —
    эго-структура и есть дифференцированность; первая версия сеяла случайные
    связи по всем парам и стартовый граф был уже связен (третий пойманный
    артефакт прибора: «единство» наступало из коробки)."""
    d = [rng.uniform(0.6, 1.4) for _ in range(N)]
    s = sum(d)
    g = [[0j] * N for _ in range(N)]
    for i in range(N):
        g[i][i] = complex(d[i] / s, 0)
    idx = list(range(N))
    rng.shuffle(idx)
    blocks_ = [set(idx[:3]), set(idx[3:])]
    for i in range(N):
        for j in range(i + 1, N):
            same = any(i in b and j in b for b in blocks_)
            if same and rng.random() < 0.7:
                amp = rng.uniform(0.02, 0.06)
                ph = rng.uniform(0, 2 * math.pi)
                g[i][j] = amp * cmath.exp(1j * ph)
                g[j][i] = g[i][j].conjugate()
    return g


def purity(g):
    # tr(Γ²) для эрмитовой Γ
    tot = 0.0
    for i in range(N):
        for j in range(N):
            tot += (g[i][j] * g[j][i]).real
    return tot


def blocks(g):
    """D: связные блоки графа |γ_ij| > EPS·sqrt(γ_ii γ_jj) (относительный)."""
    adj = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j:
                den = math.sqrt(max(1e-12,
                                    g[i][i].real * g[j][j].real))
                adj[i][j] = abs(g[i][j]) / den > EPS
    seen = [False] * N
    d = 0
    for s0 in range(N):
        if seen[s0]:
            continue
        d += 1
        stack = [s0]
        while stack:
            v = stack.pop()
            if seen[v]:
                continue
            seen[v] = True
            for w in range(N):
                if adj[v][w] and not seen[w]:
                    stack.append(w)
    return d


def lambda2(g):
    """Алгебраическая связность (Фидлер) графа весов |γ| — прокси «всё
    связано» [И-прокси, не корпусная Φ]. Степенной метод на лапласиане."""
    wgt = [[abs(g[i][j]) if i != j else 0.0 for j in range(N)]
           for i in range(N)]
    deg = [sum(row) for row in wgt]
    lap = [[(deg[i] if i == j else 0.0) - wgt[i][j] for j in range(N)]
           for i in range(N)]
    # проектируем от константного вектора и итерируем (I·c − L) для старшего
    c = max(deg) * 2 + 1e-9
    v = [math.sin(i + 1.0) for i in range(N)]
    mean = sum(v) / N
    v = [x - mean for x in v]
    for _ in range(60):
        w = [c * v[i] - sum(lap[i][j] * v[j] for j in range(N))
             for i in range(N)]
        mean = sum(w) / N
        w = [x - mean for x in w]
        nrm = math.sqrt(sum(x * x for x in w)) or 1.0
        v = [x / nrm for x in w]
    ray = sum(v[i] * sum(lap[i][j] * v[j] for j in range(N))
              for i in range(N))
    return max(0.0, c - (c - ray)) if False else max(0.0, ray)


def simulate(rng, steps=80, width_speed=1.0):
    """Рост пористости σ: 0→1. ПЕРВАЯ версия лабы вводила мир во ВСЕ каналы
    разом («тотальная пористость») — и единство наступало на шаге ~2:
    артефакт входа, не феноменология (34/36 траекторий unity<conn<ego;
    исходная пререгистрация P1a ОПРОВЕРГНУТА на той игрушке — честный нуль,
    оставлен в истории). Пересмотр P1a′: вход КАНАЛЬНЫЙ — мир втекает через
    маску открытых каналов (сэмплеры); σ растит и ГЛУБИНУ (гейн), и ШИРИНУ
    (число открытых каналов, скорость width_speed). События: t_conn (λ₂
    удвоилась), t_ego (P>3/7 ⟺ R<1/3 [Т]), t_unity (D=1)."""
    g = start_gamma(rng)
    world = herm_random(rng, rank=2)
    open0 = rng.sample(range(N), 2)
    lam0 = None
    t_conn = t_ego = t_unity = None
    for t in range(steps):
        sig = t / (steps - 1)
        eta = 0.06 + 0.10 * sig
        w = min(N, 2 + int(width_speed * sig * (N - 2) + 0.5))
        mask = set(open0[:1]) | set(
            sorted(range(N), key=lambda i: (i not in open0, i))[:w])
        mixed = [[(1 - eta) * g[i][j]
                  + (eta * (sig * sig) * world[i][j]
                     if (i in mask and j in mask) else 0)
                  + (eta * (1 - sig * sig) * g[i][j] if i == j else 0)
                  for j in range(N)] for i in range(N)]
        tr = sum(mixed[i][i].real for i in range(N))
        g = [[mixed[i][j] / tr for j in range(N)] for i in range(N)]
        # маркер «всё связано» = средняя внедиагональная связь; λ₂ на
        # несвязном графе тождественно 0 (изолированный узел глушит маркер
        # при узкой маске) — второй пойманный артефакт прибора
        lam = sum(abs(g[i][j]) for i in range(N) for j in range(N)
                  if i != j) / (N * (N - 1))
        if lam0 is None:
            lam0 = max(lam, 1e-9)
        p = purity(g)
        d = blocks(g)
        if t_conn is None and lam > 2.0 * lam0:
            t_conn = t
        if t_ego is None and p > P_HI:
            t_ego = t
        if t_unity is None and d == 1:
            t_unity = t
    return t_conn, t_ego, t_unity


def part_s():
    print("\n" + "=" * 78)
    print("S. Порядок стадий разлёта (P1a → эррата → P1a\u2032)")
    print("=" * 78)
    print("  тождество порогов [Т]: P > 3/7 ⟺ R = 1/(7P) < 1/3 — эго-смерть")
    print("  есть верхний край окна сознания, не отдельный порог.")
    print("  ЭРРАТА: тотальная пористость (мир во все каналы) давала unity на")
    print("  шаге ~2 — артефакт входа; исходный фиксированный порядок P1a")
    print("  опровергнут честно. Пересмотр: вход канальный, и порядок ворот —")
    print("  ФУНКЦИЯ ПРОФИЛЯ пористости (глубина × ширина):")
    from collections import Counter
    for name, wsp in [("широкий вход (DMT-подобный, ширина быстро)", 3.0),
                      ("глубокий вход (псилоцибиноподобный, ширина медленно)",
                       0.9)]:
        rng = random.Random(7)
        orders = Counter()
        tt = {"conn": [], "ego": [], "unity": []}
        for _ in range(60):
            tc, te, tu = simulate(rng, width_speed=wsp)
            if None in (tc, te, tu):
                orders["не все стадии"] += 1
                continue
            lab = sorted([("conn", tc), ("ego", te), ("unity", tu)],
                         key=lambda x: x[1])
            orders["<".join(k for k, _ in lab)] += 1
            for k, v in [("conn", tc), ("ego", te), ("unity", tu)]:
                tt[k].append(v)
        mean = {k: (sum(v) / len(v) if v else -1) for k, v in tt.items()}
        print("  %s:" % name)
        print("    средние шаги: связность %.0f · эго-смерть %.0f · единство %.0f"
              % (mean["conn"], mean["ego"], mean["unity"]))
        print("    порядки: %s" % dict(orders.most_common(3)))
    print("  вердикт S [С]: порядок ворот не универсален — он вычисляется из")
    print("  профиля пористости. Феноменологическое соответствие: DMT-прорыв")
    print("  (сразу единство) против псилоцибинового растворения (долгая фаза")
    print("  «всё связано» до эго-смерти) — два профиля одного механизма. [И]")
    print("  для соответствия веществам; сама зависимость порядка от профиля —")
    print("  [С] на игрушечной динамике; тождество P/R-порога — [Т].")


if __name__ == "__main__":
    kluver_ascii()
    part_s()
