#!/usr/bin/env python3
"""P6a — АНАЛИЗ по пререгистрации (RECON-TOTAL §П6, P6a + поправки 1-6).

Замороженный дизайн:
  индексы (на 1000 слов): I_neg→N⁺, I_pos→E⁺, I_wei=(we−i)→A⁺, I_deont→C⁺,
  плюс метачерты: (Plasticity, I_pos, +), (Stability, I_neg, −) ⟹ m=6;
  TTR→O — ТОЛЬКО exploratory, в выводы не идёт.
  Агрегация: словово-взвешенное среднее по работам персоны.
  Тест: Spearman ρ; нуль = перестановки наталов ВНУТРИ ДЕКАДЫ рождения
  (2000×, xorshift, seed фиксирован); поправка Холма (m=6);
  held-out: случайные половины по ogid, seed=20260727.
  Частичный контроль длины: rank-partial по log(words) (доп. столбец).
  Рамка: ТЕСТ ВЕРХНЕЙ ГРАНИЦЫ — |ρ|₉₅ из перестановок = что исключаем.

Токенизация (заморожено): lowercase; апострофы разбивают токены; префиксы
элизии fr {j,l,d,m,t,s,n,c,qu} НЕ считаются словами КРОМЕ j→je, m→me
(закрытые классы: только словарные формы); буквенные токены [^\\W\\d_].

run: python3 architecture/p6a_analysis_lab.py
"""
import csv
import math
import re
import unicodedata
from pathlib import Path

HERE = Path(__file__).parent
D = HERE / "data"
TEXTS = D / "p6a_texts"
SEED = 20260727

ELISION_I = {"j"}   # j' → je (класс i)
ELISION_ME = {"m"}  # m' → me (класс i)


def load_lex():
    pos, neg = set(), set()
    for r in csv.DictReader(
            (l for l in open(D / "p6a_nrc_fr_it_frozen.tsv") if not l.startswith("#")),
            delimiter="\t"):
        if r["lang"] != "fr":
            continue
        if r["pos"] == "1":
            pos.add(r["word"])
        if r["neg"] == "1":
            neg.add(r["word"])
    cls = {"i": set(), "we": set(), "deont": set()}
    for r in csv.DictReader(
            (l for l in open(D / "p6a_closed_classes_frozen.tsv") if not l.startswith("#")),
            delimiter="\t"):
        if r["lang"] == "fr":
            cls[r["class"]].add(r["word"])
    return pos, neg, cls


def tokens(text):
    text = text.lower().replace("’", "'")
    out = []
    for raw in re.split(r"[^a-zà-ÿœæç']+", text):
        if not raw:
            continue
        parts = raw.split("'")
        for k, p in enumerate(parts):
            if not p:
                continue
            if k < len(parts) - 1 and len(p) <= 2:
                if p in ELISION_I:
                    out.append("je")
                elif p in ELISION_ME:
                    out.append("me")
                # прочие элизии (l', d', qu'…) словами не считаем
                continue
            out.append(p)
    return out


def indices(text, pos, neg, cls):
    tks = tokens(text)
    n = len(tks)
    if n == 0:
        return None
    c_pos = sum(1 for t in tks if t in pos)
    c_neg = sum(1 for t in tks if t in neg)
    c_i = sum(1 for t in tks if t in cls["i"])
    c_we = sum(1 for t in tks if t in cls["we"])
    c_de = sum(1 for t in tks if t in cls["deont"])
    ttr = len(set(tks)) / n
    k = 1000.0 / n
    return {"n": n, "I_pos": c_pos * k, "I_neg": c_neg * k,
            "I_wei": (c_we - c_i) * k, "I_deont": c_de * k, "TTR": ttr}


def spearman(x, y):
    def rank(v):
        s = sorted(range(len(v)), key=lambda i: v[i])
        r = [0.0] * len(v)
        i = 0
        while i < len(s):
            j = i
            while j + 1 < len(s) and v[s[j + 1]] == v[s[i]]:
                j += 1
            rr = (i + j) / 2.0
            for k2 in range(i, j + 1):
                r[s[k2]] = rr
            i = j + 1
        return r
    rx, ry = rank(x), rank(y)
    mx = sum(rx) / len(rx)
    my = sum(ry) / len(ry)
    sxy = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    sx = math.sqrt(sum((a - mx) ** 2 for a in rx))
    sy = math.sqrt(sum((b - my) ** 2 for b in ry))
    return sxy / (sx * sy) if sx > 0 and sy > 0 else 0.0


class XS:
    def __init__(self, seed):
        self.s = seed & 0xFFFFFFFFFFFFFFFF or 0x9E3779B97F4A7C15

    def next(self):
        self.s ^= (self.s << 13) & 0xFFFFFFFFFFFFFFFF
        self.s ^= self.s >> 7
        self.s ^= (self.s << 17) & 0xFFFFFFFFFFFFFFFF
        return self.s

    def shuffle_within(self, idx, groups):
        by = {}
        for i in idx:
            by.setdefault(groups[i], []).append(i)
        perm = list(idx)
        for g, members in by.items():
            m = list(members)
            for i in range(len(m) - 1, 0, -1):
                j = self.next() % (i + 1)
                m[i], m[j] = m[j], m[i]
            for src, dst in zip(members, m):
                perm[src] = dst
        return perm


def main():
    pos, neg, cls = load_lex()
    print(f"lexicon fr: pos={len(pos)} neg={len(neg)} "
          f"i={len(cls['i'])} we={len(cls['we'])} deont={len(cls['deont'])}")
    wc = list(csv.DictReader(open(D / "p6a_wordcounts.tsv"), delimiter="\t"))
    per = {}
    for r in wc:
        if int(r["words"]) < 1000:
            continue
        t = (TEXTS / r["file"]).read_text(encoding="utf-8", errors="replace")
        ix = indices(t, pos, neg, cls)
        if ix is None:
            continue
        per.setdefault(r["ogid"], []).append(ix)
    # агрегат: словово-взвешенное среднее; фильтр персоны ≥10k слов суммарно
    agg = {}
    for og, xs in per.items():
        W = sum(x["n"] for x in xs)
        if W < 10000:
            continue
        agg[og] = {k: sum(x[k] * x["n"] for x in xs) / W
                   for k in ("I_pos", "I_neg", "I_wei", "I_deont", "TTR")}
        agg[og]["W"] = W
    print(f"persons with >=10k words: {len(agg)}")

    natal = {r["ogid"]: r for r in csv.DictReader(open(D / "p6a_natal.csv"))}
    ogids = sorted(set(agg) & set(natal))
    print(f"analysis set: N={len(ogids)}")
    decade = {og: og.split("-")[-3][:3] for og in ogids}  # 'YYY' из года

    PAIRS = [("N", "I_neg", +1), ("E", "I_pos", +1), ("A", "I_wei", +1),
             ("C", "I_deont", +1), ("plasticity", "I_pos", +1),
             ("stability", "I_neg", -1)]
    print("\n=== PREREGISTERED (m=6, Holm; null: within-decade perms) ===")
    results = []
    for trait, ix, sign in PAIRS:
        x = [float(natal[og][trait]) for og in ogids]
        y = [agg[og][ix] for og in ogids]
        rho = spearman(x, y)
        xs = XS(SEED)
        idx = list(range(len(ogids)))
        groups = [decade[og] for og in ogids]
        cnt = 0
        NP = 2000
        absr = []
        for _ in range(NP):
            pm = xs.shuffle_within(idx, groups)
            rp = spearman([x[i] for i in pm], y)
            absr.append(abs(rp))
            if abs(rp) >= abs(rho):
                cnt += 1
        p = cnt / NP
        absr.sort()
        rho95 = absr[int(0.95 * NP)]
        results.append((trait, ix, sign, rho, p, rho95))
    results_p = sorted(results, key=lambda r: r[4])
    m = len(results)
    print(f"{'pair':28}{'rho':>8}{'p_perm':>9}{'Holm':>7}{'|rho|95':>9}")
    for rank, (trait, ix, sign, rho, p, rho95) in enumerate(results_p):
        holm = min(1.0, p * (m - rank))
        exp = "+" if sign > 0 else "-"
        print(f"{trait}~{ix}({exp}){'':6}\t{rho:8.3f}{p:9.4f}{holm:7.3f}"
              f"{rho95:9.3f}")

    print("\n=== held-out halves (seed fixed) ===")
    xs = XS(SEED)
    idx = list(range(len(ogids)))
    for i in range(len(idx) - 1, 0, -1):
        j = xs.next() % (i + 1)
        idx[i], idx[j] = idx[j], idx[i]
    half = len(idx) // 2
    for name, sel in (("H1", idx[:half]), ("H2", idx[half:])):
        row = []
        for trait, ix, sign, *_ in PAIRS:
            x = [float(natal[ogids[i]][trait]) for i in sel]
            y = [agg[ogids[i]][ix] for i in sel]
            row.append(f"{trait}:{spearman(x, y):+.2f}")
        print(name, " ".join(row))

    print("\n=== promised supplement: length-partial (| log W), same null ===")
    import math as _m

    def _pear(a2, b2):
        ma = sum(a2) / len(a2)
        mb = sum(b2) / len(b2)
        num = sum((p2 - ma) * (q2 - mb) for p2, q2 in zip(a2, b2))
        da = _m.sqrt(sum((p2 - ma) ** 2 for p2 in a2))
        db = _m.sqrt(sum((q2 - mb) ** 2 for q2 in b2))
        return num / (da * db) if da > 0 and db > 0 else 0.0

    def _rank(v):
        s2 = sorted(range(len(v)), key=lambda i: v[i])
        r2 = [0.0] * len(v)
        i = 0
        while i < len(s2):
            j = i
            while j + 1 < len(s2) and v[s2[j + 1]] == v[s2[i]]:
                j += 1
            rr = (i + j) / 2.0
            for k2 in range(i, j + 1):
                r2[s2[k2]] = rr
            i = j + 1
        return r2

    def _partial(x2, y2, z2):
        rx, ry, rz = _rank(x2), _rank(y2), _rank(z2)
        rxy, rxz, ryz = _pear(rx, ry), _pear(rx, rz), _pear(ry, rz)
        den = _m.sqrt((1 - rxz ** 2) * (1 - ryz ** 2))
        return (rxy - rxz * ryz) / den if den > 0 else 0.0

    logW = [_m.log(agg[og]["W"]) for og in ogids]
    part = []
    for trait, ix, sign in PAIRS:
        x = [float(natal[og][trait]) for og in ogids]
        y = [agg[og][ix] for og in ogids]
        rp = _partial(x, y, logW)
        xs = XS(SEED)
        idx = list(range(len(ogids)))
        groups = [decade[og] for og in ogids]
        cnt = 0
        NP = 2000
        for _ in range(NP):
            pm = xs.shuffle_within(idx, groups)
            if abs(_partial([x[i] for i in pm], y, logW)) >= abs(rp):
                cnt += 1
        part.append((trait, ix, rp, cnt / NP))
    part_s = sorted(part, key=lambda r: r[3])
    for k2, (trait, ix, rp, pv) in enumerate(part_s):
        holm = min(1.0, pv * (len(part) - k2))
        print(f"{trait}~{ix}|logW\t{rp:+.3f}  p={pv:.4f}  Holm={holm:.3f}")
    print("verdict unchanged by design: primary = raw Spearman; this column")
    print("is the preregistered length control (registered 2026-07-27).")

    print("\n=== exploratory (NOT in conclusions) ===")
    x = [float(natal[og]["O"]) for og in ogids]
    y = [agg[og]["TTR"] for og in ogids]
    print(f"O~TTR rho={spearman(x, y):+.3f}")
    with open(D / "p6a_indices.tsv", "w") as f:
        f.write("ogid\tW\tI_pos\tI_neg\tI_wei\tI_deont\tTTR\n")
        for og in ogids:
            a = agg[og]
            f.write(f"{og}\t{a['W']}\t{a['I_pos']:.3f}\t{a['I_neg']:.3f}"
                    f"\t{a['I_wei']:.3f}\t{a['I_deont']:.3f}\t{a['TTR']:.4f}\n")
    print("\nindices -> p6a_indices.tsv")


if __name__ == "__main__":
    main()
