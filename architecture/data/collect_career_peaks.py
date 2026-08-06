#!/usr/bin/env python3
"""П-ПИКИ-СБОР (06.08): карьерные пики по уже сматченным QID корпуса
смертей (колонка 6 oracle_calib_deaths.tsv). Wikidata SPARQL батчами:
P166 (награда, квалификатор P585 point-in-time) и P39 (должность,
P580 start). Выход: career_peaks.tsv (ogid, qid, kind, date) +
журнал. Рейт-лимит: батч 150 QID, пауза 3 с, UA честный."""
import json, sys, time, urllib.parse, urllib.request

SRC = "oracle_calib_deaths.tsv"
OUT = "career_peaks.tsv"
LOG = "career_peaks_journal.tsv"
UA = "OzarResearch/1.0 (career peaks; contact: luxquant@gst.st)"
EP = "https://query.wikidata.org/sparql"

rows = []
for line in open(SRC):
    f = line.rstrip("\n").split("\t")
    if len(f) >= 6 and "wikidata.org/entity/Q" in f[5]:
        rows.append((f[0], f[5].rsplit("/", 1)[1]))
print(f"QID всего: {len(rows)}", flush=True)
qid2ogid = {}
for ogid, q in rows:
    qid2ogid.setdefault(q, ogid)
qids = list(qid2ogid)

out = open(OUT, "w")
log = open(LOG, "w")
total = 0
for i in range(0, len(qids), 150):
    batch = qids[i:i + 150]
    vals = " ".join(f"wd:{q}" for q in batch)
    sparql = f"""SELECT ?person ?kind ?date WHERE {{
      VALUES ?person {{ {vals} }}
      {{
        ?person p:P166 ?st . ?st pq:P585 ?date .
        BIND("award" AS ?kind)
      }} UNION {{
        ?person p:P39 ?st . ?st pq:P580 ?date .
        BIND("position" AS ?kind)
      }}
    }}"""
    url = EP + "?" + urllib.parse.urlencode(
        {"query": sparql, "format": "json"})
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=90) as r:
            data = json.load(r)
        n = 0
        for b in data["results"]["bindings"]:
            q = b["person"]["value"].rsplit("/", 1)[1]
            d = b["date"]["value"][:10]
            k = b["kind"]["value"]
            if d[:4].isdigit() and int(d[:4]) > 1800:
                out.write(f"{qid2ogid[q]}\t{q}\t{k}\t{d}\n")
                n += 1
        total += n
        log.write(f"batch {i//150}\tok\t{n}\n")
        print(f"batch {i//150}: +{n} (total {total})", flush=True)
    except Exception as e:
        log.write(f"batch {i//150}\tfail\t{e}\n")
        print(f"batch {i//150}: FAIL {e}", flush=True)
        time.sleep(10)
    time.sleep(3)
out.close(); log.close()
print(f"ИТОГО пиков: {total}", flush=True)
