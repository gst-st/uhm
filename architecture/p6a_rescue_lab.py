#!/usr/bin/env python3
"""P6a — спасение текстов после антибота Gallica («Vérification de sécurité»).

Работы ЗАМОРОЖЕНЫ (P6a-FREEZE); источник текста — инструментальный выбор,
не выборка ⟹ законно брать копию ТОЙ ЖЕ работы из IA (идентификаторы уже
в data/p6a_match_iafr_candidates.tsv) или повторять Gallica с паузами.

Шаги: (1) файлы-заглушки (маркер «Vérification de sécurité») — удалить;
(2) для каждой недостающей работы: IA-кандидат того же ogid с ≥2 общими
титульными токенами → {id}_djvu.txt; (3) остаток — Gallica retry с паузой
20 с; (4) пересчитать p6a_wordcounts.tsv по факту файлов.

run: python3 architecture/p6a_rescue_lab.py
"""
import csv
import re
import time
import unicodedata
import urllib.request
from pathlib import Path

HERE = Path(__file__).parent
TEXTS = HERE / "data" / "p6a_texts"
POOL = HERE / "data" / "p6a_pool_final.tsv"
IAFR = HERE / "data" / "p6a_match_iafr_candidates.tsv"
WC = HERE / "data" / "p6a_wordcounts.tsv"
JOURNAL = HERE / "data" / "p6a_download_journal.tsv"
UA = {"User-Agent": "P6a-research/0.1 (preregistered study; max@gst.st)"}
JUNK = "Vérification de sécurité"


def fetch(url, tries=3, base=6):
    req = urllib.request.Request(url, headers=UA)
    for a in range(tries):
        try:
            with urllib.request.urlopen(req, timeout=180) as r:
                return r.read().decode("utf-8", errors="replace")
        except Exception:
            time.sleep(base * (a + 1))
    return None


def toks(s):
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    stop = {"les", "la", "le", "de", "des", "du", "un", "une", "et", "d",
            "l", "a", "en", "sur", "mes", "ma", "mon"}
    return {w for w in re.findall(r"[a-z]{3,}", s)} - stop


def words(t):
    return len(re.findall(r"[^\W\d_]+", t, re.UNICODE))


def fname_of(r):
    return re.sub(r"[^A-Za-z0-9._-]", "_",
                  f"{r['ogid']}__{r['source']}__{r['ref']}")[:120] + ".txt"


def main():
    pool = [r for r in csv.DictReader(
        (l for l in open(POOL, encoding="utf-8") if not l.startswith("#")),
        delimiter="\t")]
    ia = [r for r in csv.DictReader(open(IAFR), delimiter="\t")]
    jn = open(JOURNAL, "a")

    # 1) выкинуть заглушки
    junked = 0
    for f in TEXTS.glob("*.txt"):
        head = f.read_text(encoding="utf-8", errors="replace")[:2000]
        if JUNK in head:
            f.unlink()
            junked += 1
    print("junk pages removed:", junked)

    # 2)+3) добрать недостающее
    for r in pool:
        path = TEXTS / fname_of(r)
        if path.exists():
            continue
        got = None
        # IA-копия той же работы
        tt = toks(r["title"])
        best = None
        for c in ia:
            if c["ogid"] != r["ogid"]:
                continue
            common = len(tt & toks(c["title"]))
            if common >= 2 and (best is None or common > best[0]):
                best = (common, c["ia_id"])
        if best:
            got = fetch(f"https://archive.org/download/{best[1]}/"
                        f"{best[1]}_djvu.txt")
            if got and len(got) > 5000 and JUNK not in got[:2000]:
                jn.write(f"rescued-ia\t{r['ogid']}\t{r['source']}\t"
                         f"{best[1]}\t{len(got)}\t{words(got)}\t"
                         f"IA copy of same frozen work\n")
                print(f"rescued via IA: {r['ogid']} <- {best[1]} "
                      f"({words(got)} w)", flush=True)
            else:
                got = None
        # Gallica retry с паузой
        if got is None and r["source"] == "gallica":
            time.sleep(20)
            got = fetch(f"{r['ref']}.texteBrut", tries=2, base=25)
            if got and JUNK in got[:2000]:
                got = None
            if got and len(got) > 5000:
                jn.write(f"rescued-gallica\t{r['ogid']}\tgallica\t"
                         f"{r['ref']}\t{len(got)}\t{words(got)}\tslow retry\n")
                print(f"rescued via Gallica retry: {r['ogid']} "
                      f"({words(got)} w)", flush=True)
        if got:
            path.write_text(got, encoding="utf-8")
        else:
            jn.write(f"still-missing\t{r['ogid']}\t{r['source']}\t"
                     f"{r['ref']}\t0\t0\t\n")
            print(f"still missing: {r['ogid']} {r['title'][:40]}", flush=True)

    # 4) пересчёт wordcounts по факту
    with open(WC, "w") as w:
        w.write("ogid\tsource\tref\tfile\twords\n")
        for r in pool:
            path = TEXTS / fname_of(r)
            if path.exists():
                t = path.read_text(encoding="utf-8", errors="replace")
                w.write(f"{r['ogid']}\t{r['source']}\t{r['ref']}\t"
                        f"{path.name}\t{words(t)}\n")
    jn.close()
    print("rescue done")


if __name__ == "__main__":
    main()
