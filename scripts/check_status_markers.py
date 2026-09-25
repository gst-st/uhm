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
    python3 ../scripts/check_status_markers.py --list     # скрытые маркеры построчно
Выход: 0 — чисто, 1 — есть нарушения. Скрытые маркеры (составные, в формуле,
ссылкой, в коде — аудит A-84) стоят под храповиком `BASE_HIDDEN`: выход 1 только
при росте сверх базы.
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
    # Пути от каталога скрипта: из чужого каталога прибор находил НОЛЬ файлов
    # и рапортовал «подозрительные: 0» — ноль дефектов при нулевом знаменателе
    # есть не чистота, а молчание. Ниже добавлена и проверка знаменателя.
    "en": str(Path(__file__).resolve().parent.parent / "website" / "docs" / "**" / "*.md*"),
    "ru": str(Path(__file__).resolve().parent.parent / "website" / "i18n" / "ru"
              / "docusaurus-plugin-content-docs" / "current" / "**" / "*.md*"),
}
# `[X]`, не являющееся ссылкой `[X](…)` и не определением ссылки `[X]:`.
#
# NB (ПРИБОР МОЛЧАЛ НА 138 МЕТКАХ): двоеточие исключалось БЕЗУСЛОВНО — «`[X]:`
# есть определение ссылки Markdown». Но определение ссылки стои́т только В
# НАЧАЛЕ СТРОКИ, а каноническая форма реестра статусов — ровно `[T]: описание`
# в середине строки. Исключающее правило проглотило собственную форму корпуса,
# и 138 меток чужой локали — кириллические Т/С/Г/О/И в английском реестре и
# латинские в русском, неразличимые на вид — проходили вентиль молча, при том
# что и таблицы глифов, и перевод, и маскировка работали верно. Словарь прибора
# был у́же корпуса не в том, что́ он знал, а в том, что́ он ИСКЛЮЧАЛ.
MARKER_RE = re.compile(r"\[([A-ZА-ЯЁ✗])\](?!\()")
#: Определение ссылки Markdown: `[X]:` в НАЧАЛЕ строки. Только оно и исключается.
LINKDEF_RE = re.compile(r"^\s{0,3}\[[A-ZА-ЯЁ✗]\]:", re.M)
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
#
# NB (ВСТАВКА С ВЛОЖЕННОЙ СКОБКОЙ): образец знал только плоское тело `{[^{}]*}` и
# не возвращал вставку, внутри которой стои́т ещё одна команда. Так
# `\textbf{[Т\;T\text{-}140]}` (interiority-hierarchy, дважды) оставался под
# маской целиком — вернулся только внутренний `\text{-}`, а кириллическая Т в
# английском корпусе была невидима (аудит A-84, 25.09.2026). Теперь допускается
# один уровень вложенных скобок.
TEXTCMD_RE = re.compile(
    r"\\(?:text|mathrm|mbox|textbf|textit|textsf)\{(?:[^{}]|\{[^{}]*\})*\}")


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


def scan(path: str, locale: str, seen: dict | None = None):
    """Возвращает список (строка, глиф, нужный глиф, вид).

    Если передан `seen`, в него набирается ЗНАМЕНАТЕЛЬ: сколько меток прибор
    вообще осмотрел и сколько из них квалифицированных. Без этого сводка
    печатала три числа НАРУШЕНИЙ («чужая локаль: 0, квалифицированные: 0,
    подозрительные: 0») рядом с числом файлов — и читались они как знаменатели.
    Разница существенна: квалифицированных меток в корпусе 606, а строка
    «квалифицированные: 0» говорила ровно обратное.
    """
    text = Path(path).read_text(encoding="utf-8")
    masked = mask(text)
    legal = EN_GLYPHS if locale == "en" else RU_GLYPHS
    out = []
    if seen is not None:
        seen["квалифицированных"] += len(QUALIFIED_RE.findall(masked))
        seen["меток"] += len(MARKER_RE.findall(masked))
    for m in QUALIFIED_RE.finditer(masked):
        ch, conn = m.group(1), m.group(3)
        want_ch = ch if ch in legal else translate(ch, locale)
        want_conn = CONNECTOR[locale]
        if (want_ch and want_ch != ch) or conn != want_conn:
            line = masked[: m.start()].count("\n") + 1
            out.append((line, f"{ch} {conn}", f"{want_ch} {want_conn}",
                        "квалифицированный"))
    linkdefs = {m.start() for m in LINKDEF_RE.finditer(masked)}
    for m in MARKER_RE.finditer(masked):
        ch = m.group(1)
        if ch in NOT_MARKERS or ch in legal:
            continue
        if any(abs(m.start() - d) <= 3 for d in linkdefs):
            continue          # настоящее определение ссылки в начале строки
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


# ---------------------------------------------------------------------------
# СКРЫТЫЕ МАРКЕРЫ (аудит A-84, 25.09.2026).
#
# Образец `MARKER_RE` знает ровно одну форму — одиночную букву в скобках `[Т]`,
# и `QUALIFIED_RE` — одну связку `[Т при …]` / `[T at …]`. Всё прочее прибор
# пропускал молча, и вентиль рапортовал «чужая локаль: 0» при сотнях кириллических
# букв в английском корпусе:
#   * СОСТАВНОЙ маркер — `[Т/sim]`, `[Т/И]`, `[С → Т]`, `[Т-structural]`,
#     `[Т via T-153a]`, `[И over Т]`: после буквы стоит не `]`, а разделитель;
#   * маркер ВНУТРИ ФОРМУЛЫ, в текстовой вставке `\textbf{[Т\;T\text{-}140]}`;
#   * маркер-ССЫЛКА `[Т](/docs/…)` — исключался как ссылка, а читатель видит букву;
#   * маркер В КОДЕ `` `[Т]` `` — маска кода прятала его, а на странице он виден.
# Эти формы не чинятся автоматически (в составных — проза, её переводит человек)
# и стоят под храповиком: база — измеренный долг, расти ему нельзя.
_G = "".join(sorted((EN_GLYPHS | RU_GLYPHS) - {"✗"}))
_LET = "A-Za-zА-Яа-яЁё"
#: `[` + буква статуса + РАЗДЕЛИТЕЛЬ (не `]`) + тело без скобок + `]`, не ссылка.
COMPOSITE_RE = re.compile(
    r"\[([" + _G + r"])(?=[/\s\\→\-*,;:(—–])[^\[\]\n]{0,120}\](?!\()")
#: Буква статуса, стоящая отдельно (не часть слова и не номер `T-64`).
_STANDALONE = re.compile(
    r"(?<![" + _LET + r"\d])([" + _G + r"])(?![" + _LET + r"\d])"
    r"(?!\s*(?:-|\\text\{-\})\s*\d)")
#: В русском корпусе латиница законно живёт в скобках как НЕ-маркер:
#: `[D-измерение]` (измерение голонома), `[C*-алгебра]`, `[H* = 0 …]`,
#: условие `(P)`. Поэтому там буква считается маркером только в голове скобки
#: или в цепочке `/` и `→`, и лишь когда за ней разделитель, а не `*`/`-`/`(`.
_RU_SLOT = re.compile(
    r"(?:(?<=^\[)|(?<=/)|(?<=/\s)|(?<=→)|(?<=→\s))([" + _G + r"])(?=\s*[/→\],;:]|\s)")
LINKMARK_RE = re.compile(r"\[([" + _G + r"])\]\(")
FENCE_RE = re.compile(r"```.*?```|~~~.*?~~~", re.S)
CODEMARK_RE = re.compile(r"`\[([" + _G + r"])\]`")
HIDDEN_KINDS = ("составной", "в формуле", "ссылкой", "в коде")
#: ХРАПОВИК скрытых маркеров: измерено 25.09.2026 на a61647d в миг прозрения.
#: EN: 180 кириллических букв в составных (31 файл; реестр — 26 из них), 2 в
#: формуле (interiority-hierarchy `\textbf{[Т\;T-140]}`), 3 ссылкой
#: (conscious-window, operationalization, lambda-budget), 102 в коде (6 файлов,
#: homoholograph — 81). RU: 1 ссылкой (coherence-cybernetics/theorems `[T](…)`).
#: Это не рост долга, а его название; долг только падает — опускайте базу вслед.
BASE_HIDDEN = {
    "en": {"составной": 180, "в формуле": 2, "ссылкой": 3, "в коде": 102},
    "ru": {"составной": 0, "в формуле": 0, "ссылкой": 1, "в коде": 0},
}


def scan_hidden(path: str, locale: str):
    """Скрытые маркеры чужой локали: (строка, фрагмент, глиф, нужный, вид)."""
    text = Path(path).read_text(encoding="utf-8")
    masked = mask(text)
    raw_mask = MASK_RE.sub(lambda m: re.sub(r"[^\n]", " ", m.group(0)), text)
    legal = EN_GLYPHS if locale == "en" else RU_GLYPHS
    out = []

    def line_of(pos):
        return text.count("\n", 0, pos) + 1

    qualified = {m.start() for m in QUALIFIED_RE.finditer(masked)}
    for m in COMPOSITE_RE.finditer(masked):
        if m.start() in qualified:
            continue          # связка `при`/`at` — дело QUALIFIED_RE
        body = m.group(0)
        finder = _STANDALONE if locale == "en" else _RU_SLOT
        bad = [g.group(1) for g in finder.finditer(body)
               if g.group(1) not in legal and translate(g.group(1), locale)]
        if not bad:
            continue
        kind = "в формуле" if raw_mask[m.start()] == " " else "составной"
        for ch in bad:
            out.append((line_of(m.start()), body, ch, translate(ch, locale), kind))
    for m in LINKMARK_RE.finditer(masked):
        ch = m.group(1)
        if ch not in legal and translate(ch, locale):
            out.append((line_of(m.start()), m.group(0) + "…", ch,
                        translate(ch, locale), "ссылкой"))
    unfenced = FENCE_RE.sub(lambda m: re.sub(r"[^\n]", " ", m.group(0)), text)
    for m in CODEMARK_RE.finditer(unfenced):
        ch = m.group(1)
        if ch not in legal and translate(ch, locale):
            out.append((line_of(m.start()), m.group(0), ch,
                        translate(ch, locale), "в коде"))
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
    linkdefs = {m.start() for m in LINKDEF_RE.finditer(masked)}
    for m in MARKER_RE.finditer(masked):
        ch = m.group(1)
        if ch in NOT_MARKERS or ch in legal:
            continue
        if any(abs(m.start() - d) <= 3 for d in linkdefs):
            continue          # настоящее определение ссылки в начале строки
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

    listing = "--list" in args      # скрытые маркеры построчно, а не по файлам
    over = []                        # храповики скрытых маркеров, пробитые ростом
    grand = {"чужая локаль": 0, "подозрительное": 0, "квалифицированный": 0}
    seen = {"меток": 0, "квалифицированных": 0}
    touched = 0
    scanned = 0
    for locale, pattern in LOCALES.items():
        files = sorted(glob.glob(pattern, recursive=True))
        # Знаменатель обязан быть назван: «0 дефектов» при 0 просмотренных файлов
        # неотличимо от чистоты, и именно так прибор молчал, запущенный не оттуда.
        if not files:
            print(f"ОШИБКА: локаль {locale} — не найдено НИ ОДНОГО файла по {pattern}")
            return 1
        per_locale = []
        scanned += len(files)
        for path in files:
            hits = scan(path, locale, seen)
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
        # скрытые маркеры: под храповиком, список печатается целиком
        hidden = {k: [] for k in HIDDEN_KINDS}
        for path in files:
            for line, frag, ch, want, kind in scan_hidden(path, locale):
                hidden[kind].append((path, line, frag, ch, want))
        for kind in HIDDEN_KINDS:
            got, base = len(hidden[kind]), BASE_HIDDEN[locale][kind]
            nfiles = len({p for p, *_ in hidden[kind]})
            verdict = "РОСТ ДОЛГА" if got > base else (
                "ниже базы — опустите базу" if got < base else "= базе")
            print(f"   скрытые «{kind}»: {got} в {nfiles} файлах "
                  f"(база {base}; {verdict})")
            if got > base:
                over.append(f"{locale}/{kind}: {got} > {base}")
            if got and (listing or got > base):
                for path, line, frag, ch, want in hidden[kind]:
                    rel = Path(path).relative_to(Path(__file__).resolve().parent.parent)
                    print(f"      {rel}:{line}: {frag}  [{ch}]→[{want}]")
            elif got:
                per_file = {}
                for path, *_ in hidden[kind]:
                    per_file[path] = per_file.get(path, 0) + 1
                for path, n in sorted(per_file.items(), key=lambda x: -x[1]):
                    rel = Path(path).relative_to(Path(__file__).resolve().parent.parent)
                    print(f"      {rel}: ×{n}")

    print(f"\nпросмотрено файлов: {scanned}; осмотрено меток {seen['меток']}, "
          f"из них квалифицированных {seen['квалифицированных']}")
    print(f"НАРУШЕНИЙ — чужая локаль: {grand['чужая локаль']}; "
          f"в квалифицированных: {grand['квалифицированный']}; "
          f"подозрительных: {grand['подозрительное']}")
    if seen["меток"] == 0:
        print("ЗНАМЕНАТЕЛЬ ПУСТ: ни одной метки не осмотрено — "
              "это не чистота, а молчание")
        return 1
    if kinds:
        print(f"исправлено вхождений: {touched}")
        return 0
    if over:
        print("СКРЫТЫЕ МАРКЕРЫ — РОСТ ДОЛГА: " + "; ".join(over))
        return 1
    return 1 if sum(grand.values()) else 0


if __name__ == "__main__":
    raise SystemExit(main())
