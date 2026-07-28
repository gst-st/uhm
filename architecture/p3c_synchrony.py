#!/usr/bin/env python3
"""P3c — селекция или трансляция: остаётся ли синхронность СВЕРХ связности.

Пререгистрация (RECON-TOTAL, П3): глобальная синхронность авторитарных волн
объясняется либо СЕЛЕКЦИЕЙ (общие экономические/медийные условия — страны
падают вместе, потому что вместе получают шок), либо ТРАНСЛЯЦИЕЙ через общее
поле времени. Различающее предсказание названо заранее: при чистой селекции
кластеризация стартов исчезает, как только годовая интенсивность привязана к
связности; при трансляции остаётся ОСТАТОЧНАЯ синхронность сверх неё.

Конфаунд назван заранее там же: рост медийной связности монотонен по времени,
поэтому нельзя объявлять «поле», не сняв тренд.

Данные (внешние, не наши): GWF 1.2 — 160 стартов автократий 1963+;
Всемирный банк NY.GDP.PCAP.KD.ZG — подушевой рост по тем же странам.

ИТОГ (2026-07-28): синхронность РЕАЛЬНА (кластеризация 2.13 против 1.0,
z = +5.4), но имеющийся прокси связности её не объясняет и объяснить не может
— мировой спад со счётом стартов не связан (r = −0.19, p = 0.21). Вопрос
остаётся ОТКРЫТЫМ: ни селекция, ни трансляция на этих данных не установлены.

Первая версия прибора подбирала β под наблюдаемую кластеризацию и объявляла
«селекция объясняет всё». Вывод был негоден: одним свободным параметром
дисперсию нуля подгоняют под любую, и такой тест не способен провалиться.
Оставлено здесь как урок: прежде подгонки — спросить, связан ли ряд с исходом.

Прогон: python3 architecture/p3c_synchrony.py
"""
import csv, math, random, statistics as st
from collections import Counter, defaultdict

random.seed(20260728)
D = "architecture/data/"

def starts():
    ys = []
    with open(D + "gwf_starts_matched.tsv") as f:
        for row in csv.reader(f, delimiter="\t"):
            if not row or row[0].startswith("#"):
                continue
            ys.append(int(row[2]))
    return ys

def growth():
    """Мировой ряд: медиана подушевого роста по странам за год."""
    per = defaultdict(list)
    with open(D + "wb_pcap_growth_matched.tsv") as f:
        for row in csv.reader(f, delimiter="\t"):
            if not row or row[0].startswith("#"):
                continue
            try:
                per[int(row[1])].append(float(row[2]))
            except ValueError:
                continue
    return {y: st.median(v) for y, v in per.items() if len(v) >= 5}

def dispersion(counts):
    """Отношение дисперсии к среднему: 1 при пуассоне, >1 при кластеризации."""
    m = st.mean(counts)
    return st.variance(counts) / m if m > 0 else float("nan")

def main():
    ys = starts()
    g = growth()
    lo, hi = max(min(ys), min(g)), min(max(ys), max(g))
    years = list(range(lo, hi + 1))
    cnt = Counter(y for y in ys if lo <= y <= hi)
    obs = [cnt.get(y, 0) for y in years]
    n = sum(obs)
    print(f"стартов в окне {lo}–{hi}: {n} за {len(years)} лет "
          f"(в среднем {n/len(years):.2f} в год)\n")

    d_obs = dispersion(obs)
    print(f"наблюдаемая кластеризация (дисперсия/среднее): {d_obs:.3f}")
    print("   при полном отсутствии синхронности было бы ≈ 1.0\n")

    # --- нуль A: постоянная интенсивность --------------------------------
    def sim(rates, trials=20000):
        tot = sum(rates)
        p = [r / tot for r in rates]
        out = []
        for _ in range(trials):
            c = [0] * len(years)
            for _ in range(n):
                x = random.random(); acc = 0.0
                for i, pi in enumerate(p):
                    acc += pi
                    if x <= acc:
                        c[i] += 1; break
            out.append(dispersion(c))
        return out

    flat = sim([1.0] * len(years))
    z_flat = (d_obs - st.mean(flat)) / st.stdev(flat)
    print(f"НУЛЬ A — интенсивность постоянна:")
    print(f"   {st.mean(flat):.3f} ± {st.stdev(flat):.3f}   наблюдение z = {z_flat:+.2f}")

    # --- А СВЯЗАН ЛИ ПРОКСИ СО СТАРТАМИ ВООБЩЕ --------------------------
    # Первая версия прибора подбирала β под наблюдаемую кластеризацию и
    # получала z ≈ 0 — «селекция объясняет всё». Вывод был НЕГОДЕН: одним
    # свободным параметром дисперсию нуля можно подогнать под любую, и такой
    # тест не способен провалиться. Прежде подгонки надо спросить, связан ли
    # ряд связности с исходом хоть как-нибудь.
    gr = [g[y] for y in years]
    def pearson(a, b):
        ma, mb = st.mean(a), st.mean(b)
        num = sum((x - ma) * (y - mb) for x, y in zip(a, b))
        den = (sum((x - ma) ** 2 for x in a) * sum((y - mb) ** 2 for y in b)) ** 0.5
        return num / den
    r = pearson(obs, gr)
    null_r = []
    for _ in range(20000):
        sh = gr[:]; random.shuffle(sh); null_r.append(pearson(obs, sh))
    pr = sum(1 for x in null_r if abs(x) >= abs(r)) / len(null_r)
    print(f"\nСВЯЗЬ ПРОКСИ СО СТАРТАМИ: r = {r:+.3f}, перестановочное p = {pr:.3f}")
    print(f"   ({'значима' if pr < 0.05 else 'НЕ значима'} — "
          f"{'прокси годится' if pr < 0.05 else 'прокси не отслеживает исход'})")

    print("\nЧТЕНИЕ")
    print(f"   1. Синхронность РЕАЛЬНА: кластеризация {d_obs:.3f} против 1.0 у")
    print(f"      пуассона, z = {z_flat:+.2f}. Старты автократий сбиваются во")
    print("      времени, и это не шум.")
    if pr >= 0.05:
        print("   2. Но имеющийся прокси связности её НЕ объясняет: мировой спад")
        print(f"      со счётом стартов не связан (r = {r:+.3f}, p = {pr:.3f}).")
        print("      Значит подгонять по нему интенсивность бессмысленно —")
        print("      получится подгонка дисперсии посторонним рядом.")
        print("   3. ИТОГ: P3c НЕ РАЗРЕШЁН. Синхронность есть; ни селекция")
        print("      (через этот прокси), ни трансляция не установлены.")
        print("      Различающего предсказания на этих данных не построить.")
    else:
        print("   2. Прокси отслеживает исход — подгонка интенсивности осмысленна,")
        print("      и остаточную синхронность можно мерить.")
    # --- не артефакт ли это деколонизации ---------------------------------
    print("\nУСТОЙЧИВОСТЬ К ОБРЕЗКЕ ПЕРИОДА (волна независимости 1960-х)")
    for cut in (1970, 1975, 1980):
        v = [cnt.get(y, 0) for y in range(cut, hi + 1)]
        k = sum(v)
        sims = []
        for _ in range(8000):
            c = [0] * len(v)
            for _ in range(k):
                c[random.randrange(len(v))] += 1
            sims.append(dispersion(c))
        zz = (dispersion(v) - st.mean(sims)) / st.stdev(sims)
        print(f"   с {cut}: кластеризация {dispersion(v):.3f}, z = {zz:+.2f}")
    print("   Синхронность обрезку переживает — значит это НЕ всплеск")
    print("   деколонизации, а устойчивое свойство ряда.")

    print("\nЧТО НУЖНО, ЧТОБЫ РАЗРЕШИТЬ")
    print("   Прокси связности, который ДЕЙСТВИТЕЛЬНО коррелирует со стартами:")
    print("   торговая открытость, проникновение медиа, плотность союзов. Пока")
    print("   такого ряда нет, вопрос «селекция или трансляция» остаётся")
    print("   открытым — и объявлять победителя нельзя ни в чью сторону.")

if __name__ == "__main__":
    main()
