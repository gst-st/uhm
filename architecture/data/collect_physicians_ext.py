#!/usr/bin/env python3
"""П-EU-ВРАЧИ-ВНЕШ-1 + П-УЧИТЕЛЯ-1: внешние выборки.
Собирает ДВЕ профессии: врачей (Q39631) и УЧИТЕЛЕЙ (Q37226) —
вторые для прямой проверки гипотезы владельца «учителями рождаются»,
которую прокси «профессии слова» не подтвердил (П-ЛИНИЯ-ЦЕЛЕНИЯ-1).
Собирает врачей ВНЕ покрытия OGDB (US/CA/AU/JP/GB) с датой рождения
дневной точности. Часов нет ⟹ полдень-прокси (оговорка пререга: шум
Луны размывает сигнал К НУЛЮ, поэтому выживший сигнал СИЛЬНЕЕ).
Пишет TSV: qid, name, date, country. Возобновляемо (журнал батчей).
"""
import json, sys, time, urllib.parse, urllib.request, pathlib

ROOT = pathlib.Path(__file__).parent
PROF = {"Q39631": "physician", "Q37226": "teacher"}
OUT = ROOT / "physicians_ext.tsv"
LOG = ROOT / "physicians_ext_journal.tsv"
EP = "https://query.wikidata.org/sparql"
UA = "ozar-research/1.0 (research; contact via repo)"
COUNTRIES = ["Q30", "Q16", "Q408", "Q17", "Q145"]  # US CA AU JP GB

Q = """SELECT ?p ?pLabel ?dob ?c WHERE {
  ?p wdt:P106 wd:%s ; wdt:P569 ?dob ; wdt:P27 wd:%s .
  FILTER(DATATYPE(?dob) = xsd:dateTime)
  FILTER(YEAR(?dob) >= 1850 && YEAR(?dob) <= 1995)
  BIND(wd:%s AS ?c)
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
} LIMIT %d OFFSET %d"""


def run(prof, country, limit, offset):
    q = Q % (prof, country, country, limit, offset)
    url = EP + "?" + urllib.parse.urlencode({"query": q, "format": "json"})
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=180) as r:
        return json.load(r)["results"]["bindings"]


def main():
    seen = set()
    if OUT.exists():
        for ln in OUT.read_text().splitlines():
            seen.add(ln.split("\t")[0])
    n_new = 0
    with OUT.open("a") as f, LOG.open("a") as lg:
        for prof in PROF:
          for c in COUNTRIES:
            off = 0
            while off < 4000:
                try:
                    rows = run(prof, c, 500, off)
                except Exception as e:
                    lg.write(f"{prof}\t{c}\t{off}\terr\t{e}\n"); lg.flush()
                    time.sleep(30); off += 500; continue
                if not rows:
                    break
                for b in rows:
                    qid = b["p"]["value"].rsplit("/", 1)[-1]
                    if qid in seen:
                        continue
                    dob = b["dob"]["value"][:10]
                    if dob.endswith("-01-01"):      # годовая точность
                        continue
                    seen.add(qid)
                    f.write(f"{qid}\t{b['pLabel']['value']}\t{dob}\t{c}\t{PROF[prof]}\n")
                    n_new += 1
                f.flush()
                lg.write(f"{prof}\t{c}\t{off}\tok\t{len(rows)}\n"); lg.flush()
                off += 500
                time.sleep(2)
    print(f"собрано новых: {n_new}; всего в файле: {len(seen)}")


if __name__ == "__main__":
    main()
