#!/usr/bin/env python3
"""P3c на страновом уровне — там, где хватает мощности.

Мировой уровень (`p3c_connectivity.py`) упёрся в сорок перекрывающихся окон:
связь после снятия тренда сильная (r = −0.612) и направлена ПРОТИВ селекции,
но честного блочного нуля не берёт (p = 0.084). Один из трёх названных
выходов — считать по странам, а не по годам.

Вопрос ставится острее и проверяется прямо: **если синхронность есть
селекция, то страна, теснее связанная с мировой экономикой, должна и падать
вместе со всеми** — её старт обязан чаще приходиться на общую волну.

  связность страны = корреляция её подушевого роста с мировой медианой;
  попадание в волну = сколько ДРУГИХ стран стартовало в ±2 года.

ИТОГ (2026-07-28): **r = −0.049, p = 0.543** на 156 стартах в 81 стране.
Связность не предсказывает попадание в волну НИКАК. Селекция через
экономическую связность не подтверждается и здесь — при вчетверо большей
выборке, чем на мировом уровне.

Что это НЕ значит: трансляция этим не доказана. Снята одна названная
причина, а прочие каналы селекции — медийный, идеологический, колониальные
сроки — не проверялись вовсе.

Оговорка о независимости: «попадание в волну» есть функция ГОДА, поэтому
старты одного года делят значение исхода; эффективная выборка меньше 156.
При r = −0.049 вывод от этого не меняется — нуль остаётся нулём, — но при
пограничном результате поправку пришлось бы делать.

Прогон: python3 architecture/p3c_country.py
"""
import csv, statistics as st, random
from collections import defaultdict, Counter
random.seed(20260728)
D="architecture/data/"
st_year={}
for row in csv.reader(open(D+"gwf_starts_matched.tsv"), delimiter="\t"):
    if row and not row[0].startswith("#"):
        st_year.setdefault(row[1], []).append(int(row[2]))
byc=defaultdict(dict)
for row in csv.reader(open(D+"wb_pcap_growth_matched.tsv"), delimiter="\t"):
    if row and not row[0].startswith("#"):
        try: byc[row[0]][int(row[1])]=float(row[2])
        except ValueError: pass
years=sorted({y for m in byc.values() for y in m})
world={y: st.median([m[y] for m in byc.values() if y in m]) for y in years
       if sum(1 for m in byc.values() if y in m) >= 10}
def pear(a,b):
    ma,mb=st.mean(a),st.mean(b)
    n=sum((x-ma)*(y-mb) for x,y in zip(a,b))
    d=(sum((x-ma)**2 for x in a)*sum((y-mb)**2 for y in b))**0.5
    return n/d if d>0 else 0.0
# все старты для подсчёта волны
allst=[y for v in st_year.values() for y in v]
cnt=Counter(allst)
rows=[]
for c, ys in st_year.items():
    m=byc.get(c, {})
    pairs=[(m[y], world[y]) for y in m if y in world]
    if len(pairs) < 15: continue
    conn=pear([a for a,_ in pairs], [b for _,b in pairs])
    for y in ys:
        # выравненность с волной: сколько ДРУГИХ стран стартовало в ±2 года
        near=sum(cnt.get(y+d,0) for d in (-2,-1,0,1,2)) - 1
        rows.append((c, y, conn, near))
print(f"стран со стартом и рядом роста: {len({r[0] for r in rows})} · стартов: {len(rows)}")
conn=[r[2] for r in rows]; near=[r[3] for r in rows]
print(f"связность с миром: медиана {st.median(conn):+.3f} "
      f"(от {min(conn):+.2f} до {max(conn):+.2f})")
print(f"выравненность с волной: медиана {st.median(near):.1f} соседей ±2 года")
r=pear(conn, near)
null=[]
for _ in range(20000):
    s=near[:]; random.shuffle(s); null.append(pear(conn, s))
p=sum(1 for v in null if abs(v)>=abs(r))/len(null)
print(f"\nсвязность страны ↔ попадание её старта в волну: r = {r:+.3f}, p = {p:.3f}")
print("  селекция предсказывает r > 0: кто теснее связан, тот падает вместе со всеми")
