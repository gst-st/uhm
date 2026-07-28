#!/usr/bin/env python3
"""P6a — скачивание текстов замороженного мэтч-листа (веха P6a-FREEZE).

Дисциплина пререгистрации: до заморозки индексов единственный допустимый
взгляд в текст — СЧЁТЧИК СЛОВ. Этот скрипт качает, считает слова и пишет
`p6a_wordcounts.tsv`; содержимое текстов дальше счётчика не показывается.

Источники:
  pg      https://www.gutenberg.org/cache/epub/{id}/pg{id}.txt (+.utf8)
  ws      https://ws-export.wmcloud.org/?lang=fr&format=txt&page={title}
  gallica https://gallica.bnf.fr/{ark}/texteBrut  (OCR)
  ia      https://archive.org/download/{id}/{id}_djvu.txt

Тексты кладутся в data/p6a_texts/ (НЕ коммитить: чужие тексты; Моруа —
не公 домен, недоступность честно журналится).

run: python3 architecture/p6a_download_lab.py
"""
import csv
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).parent
POOL = HERE / "data" / "p6a_pool_final.tsv"
TEXTS = HERE / "data" / "p6a_texts"
WC = HERE / "data" / "p6a_wordcounts.tsv"
JOURNAL = HERE / "data" / "p6a_download_journal.tsv"
UA = {"User-Agent": "P6a-research/0.1 (preregistered study; max@gst.st)"}


def fetch(url, binary=False):
    req = urllib.request.Request(url, headers=UA)
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=180) as r:
                b = r.read()
                return b if binary else b.decode("utf-8", errors="replace")
        except Exception as e:
            err = str(e)[:80]
            time.sleep(4 * (attempt + 1))
    return None if not binary else None


def url_of(src, ref):
    if src == "pg":
        return [f"https://www.gutenberg.org/cache/epub/{ref}/pg{ref}.txt",
                f"https://www.gutenberg.org/cache/epub/{ref}/pg{ref}.txt.utf8"]
    if src == "ws":
        t = urllib.parse.quote(ref.replace(" ", "_"))
        return [f"https://ws-export.wmcloud.org/?lang=fr&format=txt&page={t}",
                # fallback: Gallica ark того же издания (WS-экспорт капризен)
                "https://gallica.bnf.fr/ark:/12148/bpt6k215323r.texteBrut"]
    if src == "gallica":
        return [f"{ref}.texteBrut"]
    if src == "ia":
        return [f"https://archive.org/download/{ref}/{ref}_djvu.txt"]
    return []


def words(text):
    return len(re.findall(r"[^\W\d_]+", text, re.UNICODE))


def main():
    TEXTS.mkdir(exist_ok=True)
    rows = [r for r in csv.DictReader(
        (l for l in open(POOL, encoding="utf-8") if not l.startswith("#")),
        delimiter="\t")]
    jn = open(JOURNAL, "w")
    jn.write("status\togid\tsource\tref\tbytes\twords\tnote\n")
    wc = open(WC, "w")
    wc.write("ogid\tsource\tref\tfile\twords\n")
    ok = fail = 0
    for i, r in enumerate(rows):
        src, ref = r["source"], r["ref"]
        fname = re.sub(r"[^A-Za-z0-9._-]", "_", f"{r['ogid']}__{src}__{ref}")[:120] + ".txt"
        path = TEXTS / fname
        if path.exists():
            t = path.read_text(encoding="utf-8", errors="replace")
            w = words(t)
            wc.write(f"{r['ogid']}\t{src}\t{ref}\t{fname}\t{w}\n")
            jn.write(f"cached\t{r['ogid']}\t{src}\t{ref}\t{len(t)}\t{w}\t\n")
            ok += 1
            continue
        got = None
        for u in url_of(src, ref):
            got = fetch(u)
            if got and len(got) > 2000:
                break
            got = None
        if got is None:
            jn.write(f"fail\t{r['ogid']}\t{src}\t{ref}\t0\t0\tunavailable\n")
            fail += 1
            print(f"[{i+1}/{len(rows)}] FAIL {src}:{ref}", flush=True)
            time.sleep(1)
            continue
        path.write_text(got, encoding="utf-8")
        w = words(got)
        wc.write(f"{r['ogid']}\t{src}\t{ref}\t{fname}\t{w}\n")
        jn.write(f"ok\t{r['ogid']}\t{src}\t{ref}\t{len(got)}\t{w}\t\n")
        ok += 1
        print(f"[{i+1}/{len(rows)}] ok {src}:{ref} words={w}", flush=True)
        time.sleep(1.2)
    jn.close()
    wc.close()
    print(f"done: ok={ok} fail={fail}")


if __name__ == "__main__":
    main()
