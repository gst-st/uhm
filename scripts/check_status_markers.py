#!/usr/bin/env python3
"""Проверяет и приводит в порядок маркеры статуса по всему корпусу.

Правило одно: **английский корпус несёт латинские маркеры, русский —
кириллические**, ровно те, что объявлены в легендах обоих реестров статусов и
собраны в `scripts/status_markers.py`.

Что здесь непросто и почему нельзя обойтись заменой строк:

* синтаксис маркера `[X]` совпадает с меткой органа (`**[A]** арифметический
  этаж` в прайм-радианте) и с аргументом оператора в формуле
  (`\\mathbb{E}[V]`, `\\mathcal{D}^\\dagger[Q]`). Всё это перечислено в
  `NOT_MARKERS` и не трогается;
* `[X](…)` — ссылка Markdown, `[X]:` — определение ссылки; не маркеры;
* внутри блоков кода, внутри `` `код` `` и внутри формул `$…$` / `$$…$$`
  маркеров не бывает, и правка там опасна. Эти области маскируются до разбора;
* `[O]` (латинская O) и `[Д]` встречаются вместо `[D]` и `[О]` — их правка
  объявлена в `SUSPECT` и делается только с ключом `--fix-suspect`.

Запуск из `website/`:
    python3 ../scripts/check_status_markers.py            # отчёт
    python3 ../scripts/check_status_markers.py --fix      # привести локали
    python3 ../scripts/check_status_markers.py --fix --fix-suspect
Выход: 0 — чисто, 1 — есть нарушения.
"""
from __future__ import annotations

import glob
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from status_markers import (  # noqa: E402
    EN_GLYPHS, NOT_MARKERS, RU_GLYPHS, SUSPECT, translate,
)

LOCALES = {
    "en": "docs/**/*.md*",
    "ru": "i18n/ru/docusaurus-plugin-content-docs/current/**/*.md*",
}
# `[X]`, не являющееся ссылкой `[X](…)` и не определением ссылки `[X]:`
MARKER_RE = re.compile(r"\[([A-ZА-ЯЁ✗])\](?![(:])")
# Квалифицированная форма: `[Т при кинетике]`, `[C at α=2/3]`. Глиф и связка
# механичны, а текст квалификатора — проза, и его переводит человек.
QUALIFIED_RE = re.compile(r"\[([A-ZА-ЯЁ])(\s+)(at|при)(\s[^\]\n]{1,80})\]")
CONNECTOR = {"en": "at", "ru": "при"}
# области, где маркеров не бывает и правка опасна
MASK_RE = re.compile(
    r"```.*?```"        # блок кода
    r"|~~~.*?~~~"       # он же альтернативным забором
    r"|`[^`\n]*`"       # код в строке
    r"|\$\$.*?\$\$"     # выключная формула
    r"|\$[^$\n]*\$",    # формула в строке
    re.S,
)


# Внутри формулы `[X]` — как правило аргумент оператора (`\mathbb{E}[V]`), но
# внутри текстовой вставки `\text{…}` это обычная проза, и маркер там —
# настоящий маркер. Без этого исключения восемь маркеров чужой локали прятались
# в формулах навсегда: инструмент их не видел ни разу.
TEXTCMD_RE = re.compile(r"\\(?:text|mathrm|mbox|textbf|textit)\{[^{}]*\}")


def mask(text: str) -> str:
    """Заменяет опасные области пробелами, сохраняя смещения и переносы.

    Текстовые вставки внутри формул из-под маски ВОЗВРАЩАЮТСЯ: там проза.
    """
    out = list(text)
    for m in MASK_RE.finditer(text):
        for i in range(m.start(), m.end()):
            if out[i] != "\n":
                out[i] = " "
    masked = "".join(out)
    # вернуть содержимое \text{…}, попавшее под маску формул
    restored = list(masked)
    for m in TEXTCMD_RE.finditer(text):
        for i in range(m.start(), m.end()):
            restored[i] = text[i]
    return "".join(restored)


def scan(path: str, locale: str):
    """Возвращает список (строка, глиф, нужный глиф, вид)."""
    text = Path(path).read_text(encoding="utf-8")
    masked = mask(text)
    legal = EN_GLYPHS if locale == "en" else RU_GLYPHS
    out = []
    for m in QUALIFIED_RE.finditer(masked):
        ch, conn = m.group(1), m.group(3)
        want_ch = ch if ch in legal else translate(ch, locale)
        want_conn = CONNECTOR[locale]
        if (want_ch and want_ch != ch) or conn != want_conn:
            line = masked[: m.start()].count("\n") + 1
            out.append((line, f"{ch} {conn}", f"{want_ch} {want_conn}",
                        "квалифицированный"))
    for m in MARKER_RE.finditer(masked):
        ch = m.group(1)
        if ch in NOT_MARKERS or ch in legal:
            continue
        line = masked[: m.start()].count("\n") + 1
        if ch in SUSPECT:
            _, fix = SUSPECT[ch]
            want = fix if fix and fix in legal else translate(fix, locale) if fix else None
            out.append((line, ch, want, "подозрительное"))
            continue
        want = translate(ch, locale)
        if want and want != ch:
            out.append((line, ch, want, "чужая локаль"))
    return out


def apply_fix(path: str, locale: str, kinds: set[str]) -> int:
    """Правит только вне замаскированных областей. Возвращает число замен."""
    text = Path(path).read_text(encoding="utf-8")
    masked = mask(text)
    legal = EN_GLYPHS if locale == "en" else RU_GLYPHS
    edits = []          # (позиция, длина, чем заменить)
    if "квалифицированный" in kinds:
        for m in QUALIFIED_RE.finditer(masked):
            ch, sp, conn = m.group(1), m.group(2), m.group(3)
            want_ch = ch if ch in legal else translate(ch, locale)
            want_conn = CONNECTOR[locale]
            if not want_ch:
                continue
            if want_ch == ch and conn == want_conn:
                continue
            edits.append((m.start(1), len(ch) + len(sp) + len(conn),
                          f"{want_ch}{sp}{want_conn}"))
    for m in MARKER_RE.finditer(masked):
        ch = m.group(1)
        if ch in NOT_MARKERS or ch in legal:
            continue
        if ch in SUSPECT:
            if "подозрительное" not in kinds:
                continue
            _, fix = SUSPECT[ch]
            if not fix:
                continue
            want = fix if fix in legal else translate(fix, locale)
        else:
            if "чужая локаль" not in kinds:
                continue
            want = translate(ch, locale)
        if want and want != ch:
            edits.append((m.start(1), 1, want))
    if not edits:
        return 0
    # правки идут с конца, иначе длины сдвинут последующие смещения
    result = text
    for pos, length, want in sorted(edits, reverse=True):
        result = result[:pos] + want + result[pos + length:]
    Path(path).write_text(result, encoding="utf-8")
    return len(edits)


def main() -> int:
    args = set(sys.argv[1:])
    kinds = set()
    if "--fix" in args:
        kinds.add("чужая локаль")
        kinds.add("квалифицированный")
    if "--fix-suspect" in args:
        kinds.add("подозрительное")

    grand = {"чужая локаль": 0, "подозрительное": 0, "квалифицированный": 0}
    touched = 0
    for locale, pattern in LOCALES.items():
        files = sorted(glob.glob(pattern, recursive=True))
        per_locale = []
        for path in files:
            hits = scan(path, locale)
            if hits:
                per_locale.append((path, hits))
                for _, _, _, kind in hits:
                    grand[kind] += 1
        print(f"== {locale}: файлов {len(files)}, "
              f"с нарушениями {len(per_locale)}")
        for path, hits in per_locale[:12]:
            kinds_here = {}
            for _, ch, want, kind in hits:
                kinds_here.setdefault((ch, want, kind), 0)
                kinds_here[(ch, want, kind)] += 1
            desc = ", ".join(f"[{ch}]→[{want}] ×{n} ({kind})"
                             for (ch, want, kind), n in sorted(kinds_here.items()))
            print(f"   {path}: {desc}")
        if len(per_locale) > 12:
            print(f"   … и ещё {len(per_locale) - 12} файлов")
        if kinds:
            for path, _ in per_locale:
                touched += apply_fix(path, locale, kinds)

    print(f"\nчужая локаль: {grand['чужая локаль']}   "
          f"квалифицированные: {grand['квалифицированный']}   "
          f"подозрительные: {grand['подозрительное']}")
    if kinds:
        print(f"исправлено вхождений: {touched}")
        return 0
    return 1 if sum(grand.values()) else 0


if __name__ == "__main__":
    raise SystemExit(main())
