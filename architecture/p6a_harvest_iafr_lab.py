#!/usr/bin/env python3
"""P6a harvest, фронт 4б — Internet Archive advancedsearch (итальянская страта).

Замороженный запрос (P6a-6б): language ita ∧ mediatype texts ∧ title из
{memorie, ricordi, autobiografia, diario, confessioni}. У IA нет годов
жизни творца ⟹ для фамильно-именных совпадений год берём из Wikidata
(wbsearchentities «имя фамилия» → первый человек → P569); нет года —
reject «year unavailable» (консервативно). Журнал — каждое решение.

run: python3 architecture/p6a_harvest_ia_lab.py
"""
import csv
import json
import re
import time
import unicodedata
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).parent
OGDB = HERE / "data" / "ogdb-time.csv"
OUT = HERE / "data" / "p6a_match_iafr_candidates.tsv"
JOURNAL = HERE / "data" / "p6a_match_iafr_journal.tsv"
UA = {"User-Agent": "P6a-research/0.1 (preregistered study; max@gst.st)"}

Q = ('language:(fre) AND mediatype:(texts) AND (title:(mémoires) OR '
     'title:(souvenirs) OR title:(autobiographie) OR title:(confessions))')


def norm(s):
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z]", "", s.lower())


def fetch(url):
    req = urllib.request.Request(url, headers=UA)
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                return json.loads(r.read().decode())
        except Exception:
            time.sleep(3 * (attempt + 1))
    return {}


def ia_rows():
    page, out = 1, []
    while True:
        url = "https://archive.org/advancedsearch.php?" + urllib.parse.urlencode({
            "q": Q, "fl[]": ["identifier", "title", "creator"],
            "rows": "100", "page": str(page), "output": "json"}, doseq=True)
        d = fetch(url)
        docs = d.get("response", {}).get("docs", [])
        if not docs:
            return out
        out += docs
        page += 1
        time.sleep(0.5)


def wikidata_birth_year(name):
    """wbsearchentities по имени → первый человек с P569 → год."""
    url = ("https://www.wikidata.org/w/api.php?" + urllib.parse.urlencode({
        "action": "wbsearchentities", "search": name, "language": "it",
        "type": "item", "limit": "3", "format": "json"}))
    d = fetch(url)
    for hit in d.get("search", []):
        qid = hit.get("id")
        cu = ("https://www.wikidata.org/w/api.php?action=wbgetclaims"
              f"&entity={qid}&property=P569&format=json")
        wd = fetch(cu)
        for c in wd.get("claims", {}).get("P569", []):
            t = (c.get("mainsnak", {}).get("datavalue", {})
                 .get("value", {}).get("time", ""))
            m = re.match(r"[+-](\d{4})", t)
            if m:
                return int(m.group(1))
    return None


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

    docs = ia_rows()
    print("IA docs:", len(docs))
    jn = open(JOURNAL, "w")
    jn.write("decision\togid\tia_id\ttitle\tcreator\treason\n")
    out = open(OUT, "w")
    out.write("ogid\tfname\tgname\tyear\tocc\tgqid\tcy\tia_id\ttitle\tcreator\n")
    ycache, n = {}, 0
    seen = set()
    for d in docs:
        title = d.get("title", "")
        if isinstance(title, list):
            title = title[0] if title else ""
        creators = d.get("creator", [])
        if isinstance(creators, str):
            creators = [creators]
        ident = d.get("identifier", "")
        for cre in creators:
            # формы: «Sarfatti, Margherita» или «Margherita Sarfatti»
            if "," in cre:
                last, _, first = cre.partition(",")
            else:
                parts = cre.split()
                last, first = (parts[-1], " ".join(parts[:-1])) if parts \
                    else ("", "")
            cands = pool.get(norm(last), [])
            if not cands:
                continue
            fw = norm(first.split()[0]) if first.split() else ""
            for cand in cands:
                gn = norm(cand["gname"].split()[0]) if cand["gname"] else ""
                if gn and fw and gn != fw:
                    jn.write(f"reject\t{cand['ogid']}\t{ident}\t{title[:60]}"
                             f"\t{cre[:50]}\tgiven-name mismatch\n")
                    continue
                nm = f"{first.strip()} {last.strip()}".strip()
                # P6a-6б: у IA год часто инлайн («Prezzolini, Giuseppe,
                # 1882-») — он первичен; Wikidata только как fallback
                mI = re.search(r",\s*(1[6-9]\d{2})\s*[-–]", cre)
                if mI:
                    ay = int(mI.group(1))
                else:
                    if nm not in ycache:
                        ycache[nm] = wikidata_birth_year(nm)
                        time.sleep(0.3)
                    ay = ycache[nm]
                if ay is None:
                    jn.write(f"reject\t{cand['ogid']}\t{ident}\t{title[:60]}"
                             f"\t{cre[:50]}\tyear unavailable (wikidata)\n")
                    continue
                if abs(ay - cand["year"]) > 1:
                    jn.write(f"reject\t{cand['ogid']}\t{ident}\t{title[:60]}"
                             f"\t{cre[:50]}\tyear mismatch ({ay} vs "
                             f"{cand['year']})\n")
                    continue
                key = (cand["ogid"], ident)
                if key in seen:
                    continue
                seen.add(key)
                n += 1
                jn.write(f"accept\t{cand['ogid']}\t{ident}\t{title[:60]}"
                         f"\t{cre[:50]}\tcreator+wikidata-year\n")
                out.write("\t".join([
                    cand["ogid"], cand["fname"], cand["gname"],
                    str(cand["year"]), cand["occ"], cand["gqid"],
                    cand["cy"], ident, str(title)[:120], cre[:80]]) + "\n")
    print("matches:", n)
    jn.close()
    out.close()


if __name__ == "__main__":
    main()
