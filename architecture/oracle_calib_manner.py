#!/usr/bin/env python3
"""П-ОРАКУЛ-КАЛИБ-3: род (P1196) и причина (P509) смерти для уже
смэтченных QID корпуса (oracle_calib_deaths*.tsv). Пререг написан ДО
этого сборщика. Батчи VALUES по 150 QID; выход TSV:
qid \t manner_qids \t manner_labels \t cause_qids \t cause_labels
Перезапуск безопасен (резюм по готовым qid в выходном файле).
"""
import json, sys, time, urllib.parse, urllib.request

SRC = [
    "/Users/taaliman/projects/oldman/uhm-theory/holon/architecture/data/oracle_calib_deaths.tsv",
]
OUT = "/Users/taaliman/projects/oldman/uhm-theory/holon/architecture/data/oracle_calib_manner.tsv"
UA = "OzarOracleCalib/0.1 (research; contact: taaliman@protonmail.com)"
BATCH = 150


def sparql(qids):
    vals = " ".join(f"wd:{q}" for q in qids)
    q = f"""SELECT ?p ?manner ?mannerLabel ?cause ?causeLabel WHERE {{
      VALUES ?p {{ {vals} }}
      OPTIONAL {{ ?p wdt:P1196 ?manner . }}
      OPTIONAL {{ ?p wdt:P509 ?cause . }}
      SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en". }}
    }}"""
    url = "https://query.wikidata.org/sparql?" + urllib.parse.urlencode(
        {"query": q, "format": "json"})
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=90) as r:
        return json.load(r)["results"]["bindings"]


def main():
    qids = []
    seen = set()
    for src in SRC:
        try:
            for line in open(src):
                f = line.rstrip("\n").split("\t")
                if len(f) >= 6 and f[5].startswith("http"):
                    q = f[5].rsplit("/", 1)[-1]
                    if q not in seen:
                        seen.add(q)
                        qids.append(q)
        except FileNotFoundError:
            pass
    done = set()
    try:
        for line in open(OUT):
            done.add(line.split("\t", 1)[0])
    except FileNotFoundError:
        pass
    todo = [q for q in qids if q not in done]
    print(f"qid всего {len(qids)}, к добору {len(todo)}", flush=True)
    of = open(OUT, "a")
    for i in range(0, len(todo), BATCH):
        batch = todo[i:i + BATCH]
        try:
            rows = sparql(batch)
        except Exception as e:
            print(f"err батч {i}: {str(e)[:80]} — сплю 30", flush=True)
            time.sleep(30)
            try:
                rows = sparql(batch)
            except Exception as e2:
                print(f"err повтор {i}: {str(e2)[:80]} — пропуск",
                      flush=True)
                continue
        acc = {}
        for r in rows:
            q = r["p"]["value"].rsplit("/", 1)[-1]
            a = acc.setdefault(q, [set(), set(), set(), set()])
            if "manner" in r:
                a[0].add(r["manner"]["value"].rsplit("/", 1)[-1])
                a[1].add(r.get("mannerLabel", {}).get("value", ""))
            if "cause" in r:
                a[2].add(r["cause"]["value"].rsplit("/", 1)[-1])
                a[3].add(r.get("causeLabel", {}).get("value", ""))
        for q in batch:
            a = acc.get(q, [set(), set(), set(), set()])
            of.write("\t".join([
                q,
                "|".join(sorted(a[0])), "|".join(sorted(x for x in a[1] if x)),
                "|".join(sorted(a[2])), "|".join(sorted(x for x in a[3] if x)),
            ]) + "\n")
        of.flush()
        print(f"[{min(i + BATCH, len(todo))}/{len(todo)}]", flush=True)
        time.sleep(2)
    print("DONE", flush=True)


if __name__ == "__main__":
    main()
