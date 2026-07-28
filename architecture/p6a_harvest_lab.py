#!/usr/bin/env python3
"""P6a harvest — мэтчинг пула OGDB против каталога Project Gutenberg.

Пререгистрация: architecture/RECON-TOTAL.md §П6 (P6a, поправки P6a-1/2).
Замороженные правила мэтчинга (P6a §1, P6a-2):
  * пул: OCCU ∈ {writer, journalist, novelist}, рождение ≤1900, DATE-UT есть;
  * автор каталога = OGDB: нормализованная диакритика ТОЛЬКО для сравнения,
    фамилия точно, данное имя точно (первое имя), год рождения ±1;
  * произведение мемуарно, если заголовок несёт замороженную лексему
    (fr/it/común, список ниже = дословно P6a-2);
  * язык текста ∈ {fr, it};
  * журнал: каждое решение — строка TSV (accept/reject + причина).

До заморозки мэтч-листа в ТЕКСТЫ не смотрим; допустим только счётчик слов.

run: python3 architecture/p6a_harvest_lab.py
"""
import csv
import gzip
import re
import sys
import unicodedata
from pathlib import Path

HERE = Path(__file__).parent
SCRATCH = Path("/private/tmp/claude-501/-Users-taaliman-projects-oldman"
               "-uhm-theory-holon/68c58c11-feac-47b5-952a-36ea41ddebe4"
               "/scratchpad")
OGDB = HERE / "data" / "ogdb-time.csv"
PG = SCRATCH / "pg_catalog.csv.gz"
OUT = HERE / "data" / "p6a_match_candidates.tsv"
JOURNAL = HERE / "data" / "p6a_match_journal.tsv"

# P6a-2, дословно (без регистра, подстрока заголовка)
MEMOIR_KEYS = [
    # fr
    "mémoire", "memoire", "souvenir", "autobiograph", "journal intime",
    "confessions", "ma vie", "mes années", "mes annees",
    # it
    "memorie", "ricordi", "autobiograf", "diario", "confessioni",
    "la mia vita",
    # común
    "memoir", "autobiography",
]


def norm(s: str) -> str:
    """Диакритика прочь — ТОЛЬКО для сравнения имён (P6a §1)."""
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z]", "", s.lower())


def load_pool():
    rows = list(csv.DictReader(open(OGDB, encoding="utf-8"), delimiter=";"))
    pool = []
    for r in rows:
        if r["OCCU"] not in ("writer", "journalist", "novelist"):
            continue
        ut = r["DATE-UT"].strip()
        if not ut or ut[:4] > "1900":
            continue
        pool.append({
            "ogid": r["OGID"], "fname": r["FNAME"], "gname": r["GNAME"],
            "year": int(ut[:4]), "occ": r["OCCU"], "gqid": r["GQID"].strip(),
            "cy": r["CY"],
        })
    return pool


def parse_pg_author(a: str):
    """'Doe, John, 1870-1932' -> (doe, john, 1870) — год может отсутствовать."""
    parts = [p.strip() for p in a.split(",")]
    if not parts:
        return None
    last = parts[0]
    first = parts[1] if len(parts) > 1 and not re.search(r"\d", parts[1]) else ""
    m = re.search(r"(\d{4})\s*[-–]", a)
    year = int(m.group(1)) if m else None
    return norm(last), norm(first.split()[0]) if first else "", year


def main():
    pool = load_pool()
    by_last = {}
    for p in pool:
        by_last.setdefault(norm(p["fname"]), []).append(p)
    print(f"pool: {len(pool)} writers; unique last names: {len(by_last)}")

    jn = open(JOURNAL, "w")
    jn.write("decision\togid\tpg_id\ttitle\treason\n")
    out = open(OUT, "w")
    out.write("ogid\tfname\tgname\tyear\tocc\tgqid\tcy\tpg_id\tlang\ttitle\n")
    n_author_hit = n_memoir = 0
    seen_pairs = set()
    with gzip.open(PG, "rt", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("Type") != "Text":
                continue
            lang = (row.get("Language") or "").strip()
            if lang not in ("fr", "it"):
                continue
            title = (row.get("Title") or "").replace("\n", " ")
            subjects = (row.get("Subjects") or "").lower()
            authors = (row.get("Authors") or "")
            for a in authors.split(";"):
                pa = parse_pg_author(a)
                if not pa:
                    continue
                last, first, year = pa
                for cand in by_last.get(last, []):
                    if year is None or abs(year - cand["year"]) > 1:
                        continue
                    gn = norm(cand["gname"].split()[0]) if cand["gname"] else ""
                    if gn and first and gn != first:
                        jn.write(f"reject\t{cand['ogid']}\t{row['Text#']}\t"
                                 f"{title[:60]}\tgiven-name mismatch "
                                 f"({first} vs {gn})\n")
                        continue
                    n_author_hit += 1
                    tl = title.lower()
                    # P6a-3(a): каталожная метка художественности
                    if "fiction" in subjects:
                        jn.write(f"reject\t{cand['ogid']}\t{row['Text#']}\t"
                                 f"{title[:60]}\tfiction-as-memoir (Subjects)\n")
                        continue
                    if not any(k in tl for k in MEMOIR_KEYS):
                        jn.write(f"reject\t{cand['ogid']}\t{row['Text#']}\t"
                                 f"{title[:60]}\tnot-memoir-title\n")
                        continue
                    key = (cand["ogid"], row["Text#"])
                    if key in seen_pairs:
                        continue
                    seen_pairs.add(key)
                    n_memoir += 1
                    jn.write(f"accept\t{cand['ogid']}\t{row['Text#']}\t"
                             f"{title[:60]}\tauthor+year+memoir-title\n")
                    out.write("\t".join([
                        cand["ogid"], cand["fname"], cand["gname"],
                        str(cand["year"]), cand["occ"], cand["gqid"],
                        cand["cy"], row["Text#"], lang, title[:120],
                    ]) + "\n")
    print(f"author-level hits (fr/it, year±1): {n_author_hit}")
    print(f"memoir-title matches: {n_memoir} -> {OUT.name}")
    jn.close()
    out.close()


if __name__ == "__main__":
    main()
