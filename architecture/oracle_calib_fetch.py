#!/usr/bin/env python3
"""П-ОРАКУЛ-КАЛИБ, сборщик корпуса-1: даты смерти для OGDB-рождений.

Мэтч: Wikidata SPARQL по ТОЧНОЙ дате рождения (P569 = день) →
кандидаты с labels/aliases; фамилия OGDB (нормализованная) должна
входить в label. Смерть = P570 (точность день). Подвыборка старта
3000 человек, seed=20260801 (PREREG-ORACLE.md §КАЛИБ). Журнал
каждого решения — TSV. Перезапуск безопасен (резюм по журналу).
"""
import csv, json, os, random, re, sys, time, unicodedata, urllib.parse
import urllib.request

SRC = "/Users/taaliman/projects/oldman/uhm-theory/holon/architecture/data/ogdb-time.csv"
OUT = "/Users/taaliman/projects/oldman/uhm-theory/holon/architecture/data/oracle_calib_deaths.tsv"
JOURNAL = "/Users/taaliman/projects/oldman/uhm-theory/holon/architecture/data/oracle_calib_journal.tsv"
WDQS = "https://query.wikidata.org/sparql"
UA = "OzarOracleCalib/0.1 (research; contact: taaliman@protonmail.com)"
SEED = 20260801
SAMPLE = 3000

def norm(s: str) -> str:
    s = unicodedata.normalize("NFD", s or "")
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z]", "", s.lower())

def sparql(day: str):
    q = f"""
SELECT ?p ?pLabel ?alias ?dod WHERE {{
  ?p wdt:P569 ?dob . hint:Prior hint:rangeSafe true .
  FILTER(?dob >= "{day}T00:00:00Z"^^xsd:dateTime &&
         ?dob < "{day}T23:59:59Z"^^xsd:dateTime)
  ?p wdt:P31 wd:Q5 .
  OPTIONAL {{ ?p wdt:P570 ?dod . }}
  OPTIONAL {{ ?p skos:altLabel ?alias .
              FILTER(LANG(?alias) IN ("en","fr","it","de","nl")) }}
  SERVICE wikibase:label {{ bd:serviceParam wikibase:language
    "en,fr,it,de,nl". }}
}} LIMIT 400"""
    url = WDQS + "?" + urllib.parse.urlencode(
        {"query": q, "format": "json"})
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)["results"]["bindings"]

def main():
    rows = list(csv.DictReader(open(SRC), delimiter=";"))
    random.seed(SEED)
    sample = random.sample(rows, min(SAMPLE, len(rows)))
    # Фаза 2 (ORACLE_PHASE=2): вторая непересекающаяся подвыборка для
    # реплики (PREREG §КАЛИБ). random.sample(rows, 6000) НЕ расширяет
    # sample(rows, 3000) префиксно, поэтому дополнение сэмплируется
    # отдельно, seed+1; первая подвыборка воспроизведена выше точно.
    if os.environ.get("ORACLE_PHASE") == "2":
        first = {r["OGID"] for r in sample}
        rest = [r for r in rows if r["OGID"] not in first]
        random.seed(SEED + 1)
        sample = random.sample(rest, min(SAMPLE, len(rest)))
    done = set()
    try:
        for line in open(JOURNAL):
            done.add(line.split("\t", 1)[0])
    except FileNotFoundError:
        pass
    jf = open(JOURNAL, "a")
    of = open(OUT, "a")
    n_hit = n_miss = n_err = 0
    for i, row in enumerate(sample):
        ogid = row["OGID"]
        if ogid in done:
            continue
        day = (row["DATE"] or "")[:10]
        fam = norm(row["FNAME"])
        if not day or not fam:
            jf.write(f"{ogid}\tskip\tno-date-or-name\n")
            continue
        try:
            cands = sparql(day)
        except Exception as e:
            n_err += 1
            jf.write(f"{ogid}\terr\t{str(e)[:60]}\n")
            jf.flush()
            time.sleep(5)
            continue
        # кандидат подходит, если фамилия входит в label/alias
        best = None
        for c in cands:
            names = [c.get("pLabel", {}).get("value", ""),
                     c.get("alias", {}).get("value", "")]
            if any(fam and fam in norm(x) for x in names):
                dod = c.get("dod", {}).get("value", "")
                if dod:
                    best = (c["p"]["value"], dod[:10],
                            c.get("pLabel", {}).get("value", ""))
                    break
        if best:
            n_hit += 1
            of.write(f"{ogid}\t{row['DATE-UT']}\t{row['LG']}\t"
                     f"{row['LAT']}\t{best[1]}\t{best[0]}\t{best[2]}\n")
            jf.write(f"{ogid}\thit\t{best[1]}\n")
        else:
            n_miss += 1
            jf.write(f"{ogid}\tmiss\tcands={len(cands)}\n")
        of.flush(); jf.flush()
        if (i + 1) % 50 == 0:
            print(f"[{i+1}/{len(sample)}] hit={n_hit} miss={n_miss} "
                  f"err={n_err}", flush=True)
        time.sleep(1.2)  # вежливость WDQS
    print(f"DONE hit={n_hit} miss={n_miss} err={n_err}")

if __name__ == "__main__":
    main()
