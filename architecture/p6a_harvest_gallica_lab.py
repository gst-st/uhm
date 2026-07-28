#!/usr/bin/env python3
"""P6a harvest, фронт 3 — Gallica (BnF) через SRU.

Замороженный запрос (P6a-5): dc.title any «mémoires souvenirs
autobiographie confessions» AND dc.language=fre AND dc.type=monographie.
Творец приходит в форме «Фамилия, Имя (1815-1896). Роль» — год рождения
инлайн, роль фильтруем «Auteur du texte». Мэтч пула — правила P6a §1
(фамилия+первое имя, диакритика только для сравнения, год ±1). Журнал —
только рассмотренные пары (фамилия совпала); полный дамп творцов не
пишем (21k+ записей).

run: python3 architecture/p6a_harvest_gallica_lab.py
"""
import csv
import re
import time
import unicodedata
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).parent
OGDB = HERE / "data" / "ogdb-time.csv"
OUT = HERE / "data" / "p6a_match_gallica_candidates.tsv"
JOURNAL = HERE / "data" / "p6a_match_gallica_journal.tsv"
UA = {"User-Agent": "P6a-research/0.1 (preregistered study; max@gst.st)"}

QUERY = ('(dc.title any "mémoires souvenirs autobiographie confessions") '
         'and (dc.language all "fre") and (dc.type all "monographie")')

CRE_RE = re.compile(r"^\s*([^,(]+),\s*([^(]*?)\s*\((\d{4})[^)]*\)\.?\s*(.*)$")


def norm(s):
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z]", "", s.lower())


def page(start):
    url = "https://gallica.bnf.fr/SRU?" + urllib.parse.urlencode({
        "operation": "searchRetrieve", "version": "1.2", "query": QUERY,
        "maximumRecords": "50", "startRecord": str(start)})
    req = urllib.request.Request(url, headers=UA)
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                return r.read().decode()
        except Exception:
            time.sleep(3 * (attempt + 1))
    return ""


def records(xml):
    """(title, [creators], ark) по записям страницы."""
    out = []
    for rec in xml.split("<srw:record>")[1:]:
        title = re.search(r"<dc:title>([^<]+)</dc:title>", rec)
        creators = re.findall(r"<dc:creator>([^<]+)</dc:creator>", rec)
        ark = re.search(r"<dc:identifier>(https://gallica[^<]+)</dc:identifier>",
                        rec)
        out.append((title.group(1) if title else "",
                    creators, ark.group(1) if ark else ""))
    return out


def main():
    rows = list(csv.DictReader(open(OGDB, encoding="utf-8"), delimiter=";"))
    pool = {}
    for r in rows:
        if r["OCCU"] not in ("writer", "journalist", "novelist"):
            continue
        ut = r["DATE-UT"].strip()
        if not ut or ut[:4] > "1900":
            continue
        pool.setdefault(norm(r["FNAME"]), []).append({
            "ogid": r["OGID"], "fname": r["FNAME"], "gname": r["GNAME"],
            "year": int(ut[:4]), "occ": r["OCCU"], "gqid": r["GQID"].strip(),
            "cy": r["CY"],
        })

    jn = open(JOURNAL, "w")
    jn.write("decision\togid\tark\ttitle\tcreator\treason\n")
    out = open(OUT, "w")
    out.write("ogid\tfname\tgname\tyear\tocc\tgqid\tcy\tark\ttitle\tcreator\n")
    total = None
    start, n_match, seen = 1, 0, set()
    while True:
        xml = page(start)
        if total is None:
            m = re.search(r"numberOfRecords>(\d+)<", xml)
            total = int(m.group(1)) if m else 0
            print("total records:", total)
        recs = records(xml)
        if not recs:
            break
        for title, creators, ark in recs:
            for cre in creators:
                m = CRE_RE.match(cre)
                if not m:
                    continue
                last, first, year, role = m.groups()
                if "auteur du texte" not in role.lower():
                    continue
                cands = pool.get(norm(last), [])
                if not cands:
                    continue
                for cand in cands:
                    gn = (norm(cand["gname"].split()[0])
                          if cand["gname"] else "")
                    fw = norm(first.split()[0]) if first.split() else ""
                    if gn and fw and gn != fw:
                        jn.write(f"reject\t{cand['ogid']}\t{ark}\t"
                                 f"{title[:60]}\t{cre[:60]}\t"
                                 f"given-name mismatch\n")
                        continue
                    if abs(int(year) - cand["year"]) > 1:
                        jn.write(f"reject\t{cand['ogid']}\t{ark}\t"
                                 f"{title[:60]}\t{cre[:60]}\t"
                                 f"year mismatch ({year} vs "
                                 f"{cand['year']})\n")
                        continue
                    key = (cand["ogid"], ark)
                    if key in seen:
                        continue
                    seen.add(key)
                    n_match += 1
                    jn.write(f"accept\t{cand['ogid']}\t{ark}\t{title[:60]}"
                             f"\t{cre[:60]}\tcreator+year+memoir-title\n")
                    out.write("\t".join([
                        cand["ogid"], cand["fname"], cand["gname"],
                        str(cand["year"]), cand["occ"], cand["gqid"],
                        cand["cy"], ark, title[:120], cre[:80]]) + "\n")
        start += 50
        if start > total:
            break
        if (start // 50) % 40 == 0:
            print(f"...page {start//50}/{(total+49)//50}, matches so far: "
                  f"{n_match}", flush=True)
        time.sleep(1.0)
    print("matches:", n_match)
    jn.close()
    out.close()


if __name__ == "__main__":
    main()
