# -*- coding: utf-8 -*-
"""dictionary_permutation_lab.py — словарь центры→оси: вывод или конвенция?

Самая глубокая [И]-дыра теории (аудит 2026-07-27): смыслы семи осей входят
через словарь центры↔оси, который калиброван, а не выведен. Этот прибор
спрашивает СТРУКТУРУ: проводка каналов между центрами ФИКСИРОВАНА (36
каналов HD), кристалл осей ФИКСИРОВАН (7 линий Фано из октонионного
умножения). Словарь — биекция 7 процессинговых центров на 7 осей, одна из
7! = 5040. Насколько канонический словарь особен относительно всех
перестановок?

Метрики (только структурные, без семантики):
  F  = число линий Фано, все три ребра которых покрыты натальной проводкой
       (канонич. знание: реализуема 1 линия — S-O-U);
  T  = tyaga-множество: какие оси получают каналы от портов давления
       (HEAD/ROOT); канонич.: {S,L,E,D}; размер инвариантен, СОСТАВ — нет;
  B  = слепые пары (инвариант: 8 — не различает словари);
  R4 = сколько пар покрыто с максимальной кратностью (профиль кратностей —
       инвариант графа, но его РАСКЛАДКА по линиям Фано — нет):
       считаем взвешенную реализуемость линий (мин. кратность рёбер линии).

Вопросы:
  Q1. Где канонический словарь в распределении F по 5040? Экстремален ли?
  Q2. Есть ли Фано-структура у tyaga-множества (дополнение = линия?) и как
      часто это случается по перестановкам?
  Q3. Существуют ли словари с F существенно больше канонического — т.е.
      «упущенная» кристаллическая согласованность?

Честный исход любой: экстремальность ⟹ словарь структурно пришпилен [С];
типичность ⟹ словарь — конвенция [О], и это ДОКАЗАННАЯ конвенциональность.
"""
import itertools
import sys

sys.path.insert(0, "architecture")
from hd_lab import CHANNELS  # noqa: E402
from prime_radiant import LINES  # noqa: E402

AXES = "ASDLEOU"  # index 0..6
PROC = ["THROAT", "SPLENIC", "SACRAL", "AJNA", "SOLAR_PLEXUS", "HEART", "G"]
PORTS = {"HEAD", "ROOT"}
# канонический словарь движка (encoder.rs proc_dim)
CANON = {"THROAT": 0, "SPLENIC": 1, "SACRAL": 2, "AJNA": 3,
         "SOLAR_PLEXUS": 4, "HEART": 5, "G": 6}

# проводка на центрах: рёбра процессинг-процессинг и подводы порт-процессинг
proc_edges = []   # (center_a, center_b) с кратностью — список с повторами
port_feeds = []   # center, получающий канал от порта
for (ga, gb), (ca, cb) in CHANNELS.items():
    a_port, b_port = ca in PORTS, cb in PORTS
    if a_port and b_port:
        continue  # порт-порт (Head-Root каналов в HD нет, но на всякий)
    if a_port:
        port_feeds.append(cb)
    elif b_port:
        port_feeds.append(ca)
    else:
        proc_edges.append((ca, cb))

print("=" * 72)
print("проводка: %d процессинг-рёбер (с кратностями), %d подводов от портов"
      % (len(proc_edges), len(port_feeds)))

LINE_SET = [frozenset(l) for l in LINES]
# П5г: у гептакода СВОЯ разметка Фано (пара+синдром атласа v2); от корпусной
# отличается ровно свопом O<->U. F меряем против ОБЕИХ — «минимальность»
# против одной разметки оказывается ОПТИМАЛЬНОСТЬЮ против другой.
HEPT_LINES = [frozenset(l) for l in
              [(0, 1, 3), (0, 2, 6), (0, 4, 5), (1, 2, 4),
               (1, 5, 6), (2, 3, 5), (3, 4, 6)]]


def metrics(perm):
    """perm: dict center->axis index."""
    mult = {}
    for ca, cb in proc_edges:
        key = frozenset((perm[ca], perm[cb]))
        if len(key) == 2:
            mult[key] = mult.get(key, 0) + 1
    covered = set(mult)
    # F: линии, все 3 ребра покрыты
    F = sum(1 for ln in LINE_SET
            if all(frozenset(p) in covered
                   for p in itertools.combinations(ln, 2)))
    tyaga = frozenset(perm[c] for c in port_feeds)
    comp = frozenset(range(7)) - tyaga
    t_line = comp in LINE_SET
    return F, tyaga, t_line, len(covered)


def F_of(perm, lines):
    mult = set()
    for ca, cb in proc_edges:
        k = frozenset((perm[ca], perm[cb]))
        if len(k) == 2:
            mult.add(k)
    return sum(1 for ln in lines
               if all(frozenset(p) in mult
                      for p in itertools.combinations(ln, 2)))


canonF, canonT, canonTL, canonCov = metrics(CANON)
print("П5г: F(канон | корпусные линии) = %d; F(канон | гептакод-линии) = %d"
      % (F_of(CANON, LINE_SET), F_of(CANON, HEPT_LINES)))
print("канонический словарь: F=%d линий реализуемо; покрыто пар=%d; "
      "tyaga={%s}; дополнение tyaga — линия Фано: %s"
      % (canonF, canonCov, ",".join(sorted(AXES[i] for i in canonT)),
         canonTL))

# полный перебор 5040
from collections import Counter  # noqa: E402
distF = Counter()
distTL = Counter()
bestF = -1
best_perms = []
for p in itertools.permutations(range(7)):
    perm = {c: p[i] for i, c in enumerate(PROC)}
    F, tyaga, t_line, cov = metrics(perm)
    distF[F] += 1
    distTL[t_line] += 1
    if F > bestF:
        bestF, best_perms = F, [(perm.copy(), tyaga)]
    elif F == bestF and len(best_perms) < 3:
        best_perms.append((perm.copy(), tyaga))

print()
print("[Q1] распределение F по всем 5040 словарям:")
for f in sorted(distF):
    mark = "  <= КАНОН" if f == canonF else ""
    print("  F=%d: %4d словарей (%5.1f%%)%s"
          % (f, distF[f], 100.0 * distF[f] / 5040, mark))
share_ge = sum(v for k, v in distF.items() if k >= canonF) / 5040
print("  доля словарей с F >= канонического: %.1f%%" % (100 * share_ge))

print()
print("[Q2] дополнение tyaga-множества — линия Фано:")
print("  по перестановкам: %d/5040 (%.1f%%); у канона: %s"
      % (distTL[True], 100 * distTL[True] / 5040, canonTL))

print()
print("[Q3] максимум F=%d; примеры экстремальных словарей:" % bestF)
for perm, tyaga in best_perms:
    print("   " + ", ".join("%s->%s" % (c.split('_')[0][:6], AXES[perm[c]])
                            for c in PROC)
          + "  | tyaga={%s}" % ",".join(sorted(AXES[i] for i in tyaga)))

print()
print("[Q4] дистанция кристалл-оптимумов от канона (в транспозициях):")
def tdist(perm):
    # число транспозиций = 7 - число циклов перестановки canon^-1 * perm
    p = [None] * 7
    for c in PROC:
        p[CANON[c]] = perm[c]
    seen = [False] * 7
    cyc = 0
    for i in range(7):
        if not seen[i]:
            cyc += 1
            j = i
            while not seen[j]:
                seen[j] = True
                j = p[j]
    return 7 - cyc
d_at_max = Counter()
one_swap = []
for pt in itertools.permutations(range(7)):
    perm = {c: pt[i] for i, c in enumerate(PROC)}
    F, tyaga, t_line, cov = metrics(perm)
    if F == bestF:
        d = tdist(perm)
        d_at_max[d] += 1
        if d == 1:
            one_swap.append(perm)
for d in sorted(d_at_max):
    print("  дистанция %d: %d словарей с F=%d" % (d, d_at_max[d], bestF))
if one_swap:
    for perm in one_swap[:3]:
        sw = [(c, AXES[CANON[c]], AXES[perm[c]]) for c in PROC
              if perm[c] != CANON[c]]
        print("  ОДИН СВОП от канона: " + "; ".join(
            "%s: %s->%s" % (c, a2, b2) for c, a2, b2 in sw))
    print("  ЗАМЕЧАНИЕ: своп Heart<->G (O<->U) уже живёт в движке как")
    print("  DICT_VARIANTS №3 «Эго->U, G->O» — кристалл-оптимум был записан")
    print("  как гипотеза до этого прибора.")

print()
verdict_pinned = (share_ge < 0.05) or canonTL
print("вердикт:")
if share_ge >= 0.5 and not canonTL:
    print("  канонический словарь СТРУКТУРНО ТИПИЧЕН (F=%d достигается или"
          % canonF)
    print("  превышается %.0f%% перестановок; tyaga без Фано-структуры) ⟹"
          % (100 * share_ge))
    print("  словарь центры↔оси — КОНВЕНЦИЯ, закреплённая калибровкой [О];")
    print("  его оправдание — феноменологическая калибровка (HB01-12), не")
    print("  кристалл. Это ДОКАЗАННАЯ конвенциональность, дыра закрыта")
    print("  честным ответом «конвенция», а не «вывод».")
elif verdict_pinned:
    print("  канонический словарь ЭКСТРЕМАЛЕН/РЕДОК (доля F>=канон: %.1f%%,"
          % (100 * share_ge))
    print("  tyaga-дополнение-линия: %s) ⟹ есть структурное пришпиливание"
          % canonTL)
    print("  [С] — копать вывод дальше.")
else:
    print("  промежуточно: доля F>=канон = %.1f%%, tyaga-Фано = %s —"
          % (100 * share_ge, canonTL))
    print("  словарь не экстремален, но и не худший; честный статус [О/И]")
    print("  с числом на руках.")
