#!/usr/bin/env python3
"""Проверяет, что каждая ссылка `T-nnn` разрешается строкой реестра статусов.

Корпус — это граф: двести с лишним теорем, и каждая страница ссылается на
чужие номера. Рёбра этого графа не проверял никто, и вот что нашлось при первом
прогоне 2026-07-28:

* **двадцать три ранних номера** (T-1…T-48) упоминаются в корпусе, но строк в
  реестре не имеют. Среди них несущие: **T-39 — 129 упоминаний**, T-42 — 90,
  T-38 — 28, T-48 — 26. Реестр при этом объявлял себя «Complete registry of all
  UHM results»;
* три номера внутри его собственного диапазона (T-167, T-168, T-169) не
  объявлены и не упоминаются — просто пропуск нумерации.

Восстановить формулировки ранних теорем нельзя: полного источника нет ни в
корпусе, ни в `math-foundations` (там T-42 значится как «G₂ ⊂ SO(7) ⊂ U(7)», а
в корпусе — «Uniqueness Theorem of Holonomic Representation», то есть номера
двух проектов не совпадают). Поэтому инструмент **сообщает**, а не сочиняет:
выдумать строку реестра значило бы подделать ту самую полноту, которой не было.

Что считается ссылкой: `T-nnn`, `T-nnn.k`, `T-nnnb` вне кода, формул и ссылок
Markdown. Маскирование берётся из `check_status_markers`, чтобы правило было
одно на оба инструмента.

Запуск из `website/`:
    python3 ../scripts/check_theorem_refs.py
    python3 ../scripts/check_theorem_refs.py --allow-early   # ранние не в счёт
Выход: 0 — все ссылки разрешаются, 1 — есть висячие.
"""
from __future__ import annotations

import collections
import glob
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_status_markers import mask  # noqa: E402

REGISTRY = "docs/reference/status-registry.md"
SOURCES = ["docs/**/*.md*"]
#: Строка реестра: `| T-123 | …` — возможно, жирная и/или зачёркнутая.
ROW_RE = re.compile(r"^\|\s*\*{0,2}~{0,2}T-(\d+)", re.M)
#: Ссылка на теорему: номер с возможным подномером `.k` или буквой.
REF_RE = re.compile(r"\bT-(\d{1,3})(?:\.\d+|[a-z])?\b")
#: Ниже этого номера — результаты, полученные до заведения реестра.
EARLY_BELOW = 50


def declared() -> set[int]:
    text = Path(REGISTRY).read_text(encoding="utf-8")
    return {int(m.group(1)) for m in ROW_RE.finditer(text)}


def referenced() -> tuple[collections.Counter, dict[int, collections.Counter]]:
    counts: collections.Counter = collections.Counter()
    where: dict[int, collections.Counter] = collections.defaultdict(
        collections.Counter)
    for pattern in SOURCES:
        for path in glob.glob(pattern, recursive=True):
            text = mask(Path(path).read_text(encoding="utf-8"))
            for m in REF_RE.finditer(text):
                n = int(m.group(1))
                counts[n] += 1
                where[n][path] += 1
    return counts, where


def main() -> int:
    allow_early = "--allow-early" in sys.argv
    have = declared()
    refs, where = referenced()
    lo, hi = min(have), max(have)
    gaps = [n for n in range(lo, hi + 1) if n not in have]
    dangling = sorted(n for n in refs if n not in have)
    early = [n for n in dangling if n < EARLY_BELOW]
    late = [n for n in dangling if n >= EARLY_BELOW]

    print(f"реестр: {len(have)} строк, T-{lo}..T-{hi}")
    print(f"корпус ссылается на {len(refs)} различных номеров")
    if gaps:
        unused = [n for n in gaps if not refs.get(n)]
        used = [n for n in gaps if refs.get(n)]
        print(f"\nпропуски внутри диапазона: {gaps}")
        print(f"   из них ни разу не упомянуты (просто неприсвоены): {unused}")
        if used:
            print(f"   УПОМЯНУТЫ, но строки нет: {used}")

    if late:
        print(f"\nВИСЯЧИЕ в рабочем диапазоне ({len(late)}) — это дефекты:")
        for n in late:
            top = ", ".join(f"{Path(p).name}×{c}"
                            for p, c in where[n].most_common(3))
            print(f"   T-{n}  ссылок {refs[n]}  {top}")

    if early:
        total = sum(refs[n] for n in early)
        print(f"\nРАННИЕ, вне реестра ({len(early)} номеров, {total} ссылок):")
        for n in early:
            top = ", ".join(f"{Path(p).name}×{c}"
                            for p, c in where[n].most_common(2))
            print(f"   T-{n:<3} ссылок {refs[n]:>4}  {top}")
        print("   Формулировки не восстанавливаются: полного источника нет.")
        print("   Инструмент сообщает, а не сочиняет — выдуманная строка")
        print("   реестра подделала бы полноту вместо того, чтобы её закрыть.")

    if late or (early and not allow_early):
        return 1
    print("\nвсе ссылки разрешаются")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
