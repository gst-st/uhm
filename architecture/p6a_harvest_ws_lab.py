#!/usr/bin/env python3
"""P6a harvest, фронт 2 — Wikisource FR/IT через MediaWiki API.

Стратегия (экономная): идём ОТ МЕМУАРНЫХ КАТЕГОРИЙ (сотни работ), а не от
1431 имени. Члены категорий → автор из заголовочного шаблона страницы →
мэтч с пулом OGDB по замороженным правилам P6a (§1: фамилия+первое имя,
диакритика нормализуется только для сравнения; год рождения ±1 — год
берём со страницы Auteur:/Autore:). Журнал — каждое решение.

Замороженные категории (операционализация P6a-2 на Wikisource, фронт 2):
  fr: Autobiographies, Mémoires, Journaux intimes, Souvenirs
  it: Autobiografie, Memorie, Diari

run: python3 architecture/p6a_harvest_ws_lab.py
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
OUT = HERE / "data" / "p6a_match_ws_candidates.tsv"
JOURNAL = HERE / "data" / "p6a_match_ws_journal.tsv"

CATS = {
    "fr": ["Catégorie:Autobiographies", "Catégorie:Mémoires",
           "Catégorie:Journaux intimes", "Catégorie:Souvenirs"],
    "it": ["Categoria:Autobiografie", "Categoria:Memorie",
           "Categoria:Diari"],
}
UA = {"User-Agent": "P6a-research/0.1 (preregistered study; contact: max@gst.st)"}


def api(lang, **params):
    params.update(action="query", format="json")
    url = (f"https://{lang}.wikisource.org/w/api.php?"
           + urllib.parse.urlencode(params))
    req = urllib.request.Request(url, headers=UA)
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read().decode())
        except Exception as e:
            if attempt == 2:
                raise
            time.sleep(2 * (attempt + 1))


def norm(s):
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z]", "", s.lower())


def cat_members(lang, cat):
    out, cont = [], {}
    while True:
        d = api(lang, list="categorymembers", cmtitle=cat, cmlimit=500,
                cmnamespace=0, **cont)
        out += [m["title"] for m in d["query"]["categorymembers"]]
        if "continue" not in d:
            return out
        cont = {"cmcontinue": d["continue"]["cmcontinue"]}


def batch_wikitext(lang, titles):
    """title -> первые 3000 знаков викитекста (шапка с author-полем)."""
    res = {}
    for i in range(0, len(titles), 50):
        chunk = titles[i:i + 50]
        d = api(lang, prop="revisions", rvprop="content", rvslots="main",
                titles="|".join(chunk))
        for page in d["query"].get("pages", {}).values():
            revs = page.get("revisions")
            if not revs:
                continue
            txt = revs[0].get("slots", {}).get("main", {}).get("*", "")
            res[page["title"]] = txt[:3000]
        time.sleep(0.3)
    return res


AUTH_RE = [
    re.compile(r"\|\s*auteur\s*=\s*(?:\[\[)?(?:Auteur:)?([^|\]\n{}]+)", re.I),
    re.compile(r"\|\s*autore\s*=\s*(?:\[\[)?(?:Autore:)?([^|\]\n{}]+)", re.I),
    re.compile(r"\{\{\s*[Aa]uteur\|([^|}]+)"),
]
PAGES_IDX = re.compile(r'<pages[^>]*\bindex\s*=\s*"([^"]+)"', re.I)


def author_of(wikitext):
    for rx in AUTH_RE:
        m = rx.search(wikitext)
        if m:
            a = m.group(1).strip()
            a = re.sub(r"\(.*?\)", "", a).strip()
            if a and not a.startswith("{{"):
                return a
    return None


def author_via_index(lang, wikitext, livre_cache):
    """ProofreadPage: шапка работы = <pages index="файл"/>; Auteur живёт на
    странице Livre:/Indice:. Fallback — префикс имени файла до « - »."""
    m = PAGES_IDX.search(wikitext)
    if not m:
        return None
    idx = m.group(1)
    ns = "Livre" if lang == "fr" else "Indice"
    key = (lang, idx)
    if key not in livre_cache:
        d = api(lang, prop="revisions", rvprop="content", rvslots="main",
                titles=f"{ns}:{idx}")
        txt = ""
        for page in d["query"].get("pages", {}).values():
            revs = page.get("revisions")
            if revs:
                txt = revs[0].get("slots", {}).get("main", {}).get("*", "")[:3000]
        livre_cache[key] = txt
        time.sleep(0.2)
    a = author_of(livre_cache[key])
    if a:
        return a
    if " - " in idx:
        return idx.split(" - ")[0].strip()
    return None


def author_year(lang, author):
    """Год рождения через Wikidata: шаблон {{Auteur}} данных не держит —
    Auteur:-страница даёт Q-id (pageprops), P569 = дата рождения."""
    ns = "Auteur" if lang == "fr" else "Autore"
    d = api(lang, prop="pageprops", titles=f"{ns}:{author}")
    qid = None
    for page in d["query"].get("pages", {}).values():
        qid = page.get("pageprops", {}).get("wikibase_item")
    if not qid:
        return None
    url = ("https://www.wikidata.org/w/api.php?action=wbgetclaims"
           f"&entity={qid}&property=P569&format=json")
    req = urllib.request.Request(url, headers=UA)
    try:
        wd = json.loads(urllib.request.urlopen(req, timeout=60).read())
    except Exception:
        return None
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

    jn = open(JOURNAL, "w")
    jn.write("decision\togid\tlang\twork\tauthor\treason\n")
    out = open(OUT, "w")
    out.write("ogid\tfname\tgname\tyear\tocc\tgqid\tcy\tlang\twork\tws_author\n")
    year_cache = {}
    n_works = n_auth = n_match = 0
    for lang, cats in CATS.items():
        works = set()
        for cat in cats:
            ms = cat_members(lang, cat)
            print(f"{lang} {cat}: {len(ms)}")
            works |= {t.split("/")[0] for t in ms if ":" not in t.split("/")[0]}
        works = sorted(works)
        n_works += len(works)
        wt = batch_wikitext(lang, works)
        livre_cache = {}
        for w in works:
            a = (author_of(wt.get(w, ""))
                 or author_via_index(lang, wt.get(w, ""), livre_cache))
            if not a:
                jn.write(f"skip\t\t{lang}\t{w[:60]}\t\tno-author-field\n")
                continue
            n_auth += 1
            # фамилия = последнее слово автора (fr порядок Given Family)
            parts = a.split()
            if not parts:
                continue
            lastn = norm(parts[-1])
            cands = pool.get(lastn, [])
            if not cands:
                continue
            key = (lang, a)
            if key not in year_cache:
                year_cache[key] = author_year(lang, a)
                time.sleep(0.2)
            ay = year_cache[key]
            for cand in cands:
                gn = norm(cand["gname"].split()[0]) if cand["gname"] else ""
                first = norm(parts[0]) if len(parts) > 1 else ""
                if gn and first and gn != first:
                    jn.write(f"reject\t{cand['ogid']}\t{lang}\t{w[:60]}\t{a}"
                             f"\tgiven-name mismatch\n")
                    continue
                if ay is None or abs(ay - cand["year"]) > 1:
                    jn.write(f"reject\t{cand['ogid']}\t{lang}\t{w[:60]}\t{a}"
                             f"\tyear mismatch ({ay} vs {cand['year']})\n")
                    continue
                n_match += 1
                jn.write(f"accept\t{cand['ogid']}\t{lang}\t{w[:60]}\t{a}"
                         f"\tcategory+author+year\n")
                out.write("\t".join([
                    cand["ogid"], cand["fname"], cand["gname"],
                    str(cand["year"]), cand["occ"], cand["gqid"],
                    cand["cy"], lang, w[:120], a]) + "\n")
    print(f"works: {n_works}; with author: {n_auth}; matches: {n_match}")
    jn.close()
    out.close()


if __name__ == "__main__":
    main()
