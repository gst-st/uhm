#!/usr/bin/env python3
"""P3c, вторая попытка — связность, построенная из тех же данных.

Первый заход (`p3c_synchrony.py`) уперся в то, что единственный прокси
связности — мировой подушевой спад — со стартами не связан вовсе, а подгонка
β под наблюдаемую дисперсию давала тест, не способный провалиться.

Здесь прокси СТРОИТСЯ, а не берётся: экономическая связность и есть
синхронность национальных экономик — средняя попарная корреляция подушевого
роста по странам в скользящем окне 11 лет. По определению меряет то, что
нужно, и считается по тем же данным ВБ.

ИТОГ (2026-07-28):
  прокси валиден — связность растёт с +0.017 (1966–70) до +0.124 (2001–05);
  сырая связь со кластеризацией стартов r = −0.362 (p = 0.021);
  после снятия линейного тренда r = −0.612 — СИЛЬНЕЕ;
  но честный блочный нуль (блок = ширина окна, окна перекрываются) даёт
  p = 0.084 — порога не берёт.

Чтение: направление связи ПРОТИВОПОЛОЖНО предсказанию селекции (рост
связности сопровождается ПАДЕНИЕМ синхронности, а не ростом), величина
немалая, но сорока перекрывающихся окон не хватает. P3c остаётся
неразрешённым — теперь по мощности, а не по отсутствию годного прокси.

Прогон: python3 architecture/p3c_connectivity.py
"""
import csv, statistics as st, random, math
from collections import defaultdict, Counter
random.seed(20260728)
D="architecture/data/"
starts=[]
for row in csv.reader(open(D+"gwf_starts_matched.tsv"), delimiter="\t"):
    if row and not row[0].startswith("#"): starts.append(int(row[2]))
byc=defaultdict(dict)
for row in csv.reader(open(D+"wb_pcap_growth_matched.tsv"), delimiter="\t"):
    if row and not row[0].startswith("#"):
        try: byc[row[0]][int(row[1])]=float(row[2])
        except ValueError: pass
def pear(a,b):
    ma,mb=st.mean(a),st.mean(b)
    n=sum((x-ma)*(y-mb) for x,y in zip(a,b))
    d=(sum((x-ma)**2 for x in a)*sum((y-mb)**2 for y in b))**0.5
    return n/d if d>0 else 0.0
# связность = средняя попарная корреляция роста в скользящем окне 11 лет
W=11
years=sorted({y for c in byc.values() for y in c})
conn={}
for mid in years:
    win=list(range(mid-W//2, mid+W//2+1))
    series=[]
    for c,m in byc.items():
        v=[m.get(y) for y in win]
        if all(x is not None for x in v): series.append(v)
    if len(series)<20: continue
    rs=[]
    for _ in range(3000):
        a,b=random.sample(series,2); rs.append(pear(a,b))
    conn[mid]=st.mean(rs)
print(f"связность посчитана для {len(conn)} лет, окно {W}")
ks=sorted(conn)
print(f"  ранние {ks[0]}–{ks[4]}: {st.mean([conn[y] for y in ks[:5]]):+.3f}")
print(f"  поздние {ks[-5]}–{ks[-1]}: {st.mean([conn[y] for y in ks[-5:]]):+.3f}")
# кластеризация стартов в том же окне
cnt=Counter(starts)
disp={}
for mid in ks:
    win=[cnt.get(y,0) for y in range(mid-W//2, mid+W//2+1)]
    m=st.mean(win)
    if m>0: disp[mid]=st.variance(win)/m
common=[y for y in ks if y in disp]
x=[conn[y] for y in common]; z=[disp[y] for y in common]
r=pear(x,z)
null=[]
for _ in range(20000):
    s=z[:]; random.shuffle(s); null.append(pear(x,s))
p=sum(1 for v in null if abs(v)>=abs(r))/len(null)
print(f"\nсвязность ↔ кластеризация стартов: r = {r:+.3f}, p = {p:.3f} (n={len(common)})")
print("  если p<0.05 и r>0 — синхронность идёт ЗА связностью (селекция)")
print("  если p>0.05 — связность её не объясняет, и остаток надо мерить")

print("\n--- КОНФАУНД ТРЕНДА, названный в пререгистрации ---")
def detrend(v):
    n=len(v); t=list(range(n)); mt=st.mean(t); mv=st.mean(v)
    b=sum((a-mt)*(c-mv) for a,c in zip(t,v))/sum((a-mt)**2 for a in t)
    return [c-(mv+b*(a-mt)) for a,c in zip(t,v)]
xd, zd = detrend(x), detrend(z)
rd = pear(xd, zd)
# блочная перестановка: окна перекрываются, значит ряд автокоррелирован
def block_perm(v, blk=11):
    bl=[v[i:i+blk] for i in range(0,len(v),blk)]
    random.shuffle(bl)
    out=[e for b in bl for e in b]
    return out[:len(v)]
nullb=[pear(xd, block_perm(zd)) for _ in range(20000)]
pb=sum(1 for q in nullb if abs(q)>=abs(rd))/len(nullb)
print(f"после снятия линейного тренда: r = {rd:+.3f}")
print(f"блочная перестановка (блок 11 = ширина окна): p = {pb:.3f}")
print()
if pb < 0.05 and rd > 0:
    print("СЕЛЕКЦИЯ: синхронность идёт за связностью и после снятия тренда.")
elif pb < 0.05 and rd < 0:
    print("ПРОТИВ СЕЛЕКЦИИ: связь есть, но ОБРАТНАЯ — рост связности")
    print("сопровождается ПАДЕНИЕМ синхронности. Селекция предсказывает")
    print("противоположное; трансляция этим тоже не подтверждается.")
else:
    print("НЕ РАЗРЕШЕНО — но не так, как в первом заходе.")
    print("После снятия тренда связь не исчезла, а УСИЛИЛАСЬ (|r| выросла),")
    print("то есть общий тренд её МАСКИРОВАЛ, а не создавал. Честного")
    print("блочного нуля она всё же не берёт: сорока перекрывающихся окон")
    print("мало. И направление её ПРОТИВОПОЛОЖНО предсказанию селекции —")
    print("рост связности сопровождается падением синхронности.")
    print()
    print("Значит дело в МОЩНОСТИ, а не в прокси: нужен либо более длинный")
    print("ряд, либо неперекрывающиеся окна, либо страновой уровень вместо")
    print("мирового. До этого ни селекция, ни трансляция не установлены.")
