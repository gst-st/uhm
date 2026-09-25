#!/usr/bin/env python3
"""Проверяет, что каждая ссылка `T-nnn` разрешается строкой реестра статусов.

Корпус — это граф: двести с лишним теорем, и каждая страница ссылается на
чужие номера. Рёбра этого графа не проверял никто, и вот что нашлось при первом
прогоне 2026-07-28:

* **ранние номера** (T-1…T-49) упоминаются в корпусе, но строк в реестре не
  имеют — при первом прогоне их насчитывалось двадцать три, а после того, как
  буква стала частью имени (см. REF_RE), стало **пятьдесят четыре имени и 421
  ссылка**: прежняя редакция считала T-39 и T-39a за один номер, отчего «T-39 —
  129 упоминаний» оказалось суммой двух разных результатов. Реестр при этом
  объявлял себя «Complete registry of all UHM results»;
* три номера внутри его собственного диапазона (T-167, T-168, T-169) не
  присвоены — просто пропуск нумерации. Реестр объявляет это строкой
  «Skipped numbers / Пропущенные номера», которую читает SKIP_RE: без неё
  прибор ловил реестр на его же объявлении, считая единственное упоминание
  «этих номеров нет» за ссылку на несуществующий номер.

Второй прогон, после починки имени (2026-08-25), нашёл в рабочем диапазоне
восемнадцать висячих имён — тринадцать из них были настоящими результатами с
формулировкой и доказательством, но без строки реестра (T-53a–d о времени,
T-98a, T-100a, T-107a–c, T-108a о сенсомоторике, T-221.1–.3 о no-go-теоремах), а
две — опечатками (T-257a и T-301a, у которых нет и никогда не было источника;
одна из ссылок на «T-257a» вела на якорь #t-257). Строки написаны, опечатки
исправлены, рабочий диапазон чист. Найдено это, что важно, ЧУЖИМ прибором:
gateway_lint корпуса math-foundations сообщил, что цитируемая им T-129a реестром
не покрыта, — своему прибору она была невидима по построению.

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

# Пути считаются от каталога скрипта, а не от текущего: прибор, работающий
# только из website/ и падающий трассировкой из корня, проверяет не корпус,
# а привычку запускающего. Собственный каталог у скрипта есть всегда.
_SITE = Path(__file__).resolve().parent.parent / "website"
REGISTRY = str(_SITE / "docs" / "reference" / "status-registry.md")
SOURCES = [str(_SITE / "docs" / "**" / "*.md*")]
#: Строка реестра: `| T-123 | …` или `| T-123a | …` — возможно, жирная и/или зачёркнутая.
ROW_RE = re.compile(r"^\|\s*\*{0,2}~{0,2}T-(\d+(?:\.\d+|[a-z])?)", re.M)
#: Объявленный пропуск нумерации. Реестр называет номера, которые НЕ присвоены;
#: без такой строки прибор ловил реестр на его же объявлении: единственные
#: «ссылки» на T-167..T-169 — это фраза, сообщающая, что их нет.
SKIP_RE = re.compile(r"^(?:\*\*)?(?:Skipped numbers|Пропущенные номера)[^\n]*", re.M)
#: Объявление раннего диапазона. Пока реестр объявляет его машинно-читаемо,
#: ранние номера — известный и названный пробел, а не дефект: код возврата
#: обязан отличать «объявлено» от «обнаружено». Без этой строки прибор выходил
#: с единицей ВСЕГДА, а код возврата, который никогда не ноль, ничего не значит.
EARLY_RE = re.compile(r"^(?:\*\*)?(?:Early numbers|Ранние номера)[^\n]*", re.M)
#: Объявление опор без формулировки. Реестр вправе признать их открытым долгом —
#: но признать ЯВНО и поимённо, а не молчанием: пока строки нет, прибор красен.
GHOST_RE = re.compile(r"^(?:\*\*)?(?:Unstated supports|Опоры без формулировки)[^\n]*", re.M)
#: Ссылка на теорему: номер с возможным подномером `.k` или буквой.
#: БУКВА — ЧАСТЬ ИМЕНИ, а не украшение. Прежняя редакция брала только цифры
#: (`int(m.group(1))`), и потому T-129a была для неё неотличима от T-129: ссылка
#: на следствие «разрешалась» строкой базовой теоремы, а собственная строка
#: следствия, даже будь она написана, просто повторно добавляла бы 129. Найдено
#: это не здесь, а СНАРУЖИ: gateway_lint соседнего корпуса math-foundations
#: сообщил, что цитируемая им T-129a реестром не покрыта, — своему прибору она
#: была невидима по построению. После починки в рабочем диапазоне открылось
#: двенадцать таких имён (38 ссылок), а «T-39 — 129 упоминаний» из шапки этого
#: файла оказалось суммой T-39 и T-39a, двух разных результатов.
# Четыре цифры, а не три: реестр доходит до T-325, и потому ЛЮБОЙ четырёхзначный
# номер заведомо висячий — но прежний шаблон не видел его ВОВСЕ, и опечатка
# «T-1000» проходила молча. Подлог T-9999 прошёл мимо прибора именно так.
REF_RE = re.compile(r"\bT-(\d{1,4}(?:\.\d+|[a-z])?)\b")
# Кириллическая «Т» неотличима на вид от латинской «T», но не совпадает с ней
# ни в одном сравнении. Ссылок вида «Т-nnn» кириллицей в корпусе было 57 в 29
# файлах — REF_RE их не видел, и потому они не проверялись на разрешимость
# вовсе: указывай такая ссылка на несуществующий номер, прибор бы промолчал.
HOMOGLYPH_RE = re.compile(r"\bТ-(\d{1,3})(?:\.\d+|[a-z])?\b")
#: Ниже этого номера — результаты, полученные до заведения реестра.
EARLY_BELOW = 50


def base(ident: str) -> int:
    """Числовая часть имени: `129a` → 129. Порядок — по ней, имя — целиком."""
    return int(re.match(r"\d+", ident).group())


#: Второй формат строки реестра: в таблицах «Level 1..6» номер стои́т в столбце
#: «#» БЕЗ префикса «T-» («| 40b | R_th = 1/3 [T]: …»). Прежняя редакция этого
#: не знала и потому объявляла беспризорными 177 строк — в том числе пять из
#: шести номеров, которые аудит успел записать в «опоры без формулировки».
#: Голое число засчитывается только внутри таблицы, чья шапка начинается с «#»:
#: иначе счётчик любой другой таблицы сошёл бы за номер теоремы.
def declared() -> set[str]:
    text = Path(REGISTRY).read_text(encoding="utf-8")
    out = {m.group(1) for m in ROW_RE.finditer(text)}
    numbered_table = False
    for line in text.split("\n"):
        if not line.startswith("|"):
            if line.startswith("#"):
                numbered_table = False
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if cells and cells[0] in ("#", "№"):
            numbered_table = True
            continue
        if re.match(r"^\|\s*[-: ]+\|", line):
            continue
        if numbered_table and cells:
            m = re.match(r"^\*{0,2}~{0,2}(\d{1,3}(?:\.\d+|[a-z])?)$",
                         cells[0].strip("*~ "))
            if m:
                out.add(m.group(1))
    return out


def skipped() -> set[str]:
    """Номера, которые реестр объявил непри­своенными."""
    text = Path(REGISTRY).read_text(encoding="utf-8")
    out: set[str] = set()
    for line in SKIP_RE.finditer(text):
        out |= {m.group(1) for m in re.finditer(r"T-(\d+(?:\.\d+|[a-z])?)", line.group())}
    return out


HOMOGLYPHS: collections.Counter = collections.Counter()


def registry_only() -> list[tuple[str, int]]:
    """Номера, на которые ссылается САМ реестр, не имея под ними строки и не
    встречаясь больше нигде в корпусе.

    Это иной род пробела, чем «ранний номер»: ранний просто цитируется, а эти
    номера реестр ИСПОЛЬЗУЕТ — повышает на них статусы («Raised to [C at
    T-4.2]»), строит цепи вывода («AP → c>0 → T-41b → T-11 → T-12 → T-13»),
    ссылается на них как на доказанное («[T]+[I]: K = 3 derived from triadic
    decomposition [T-40a, 40b]»). Формулировки под этими метками нет нигде —
    даже на страницах, куда ведут сами ссылки. Опора, которой не видно, хуже
    названного пробела: пробел честен, а опора обещает.
    """
    reg = Path(REGISTRY)
    regt = reg.read_text(encoding="utf-8")
    rows = declared()
    inside: collections.Counter = collections.Counter()
    outside: set[str] = set()
    for pattern in SOURCES:
        for path in glob.glob(pattern, recursive=True):
            text = mask(Path(path).read_text(encoding="utf-8"))
            names = {m.group(1) for m in REF_RE.finditer(text)}
            if Path(path) == reg:
                inside.update(names)
            else:
                outside |= names
    skips = skipped()
    early_decl = {m.group(1) for line in EARLY_RE.finditer(regt)
                  for m in re.finditer(r"T-(\d{1,3}(?:\.\d+|[a-z])?)", line.group())}
    ghosts = [k for k in inside
              if k not in outside and k not in rows and k not in skips
              and k not in early_decl]
    return sorted(((k, inside[k]) for k in ghosts),
                  key=lambda x: (base(x[0]), x[0]))


def referenced() -> tuple[collections.Counter, dict[str, collections.Counter]]:
    counts: collections.Counter = collections.Counter()
    where: dict[str, collections.Counter] = collections.defaultdict(
        collections.Counter)
    for pattern in SOURCES:
        for path in glob.glob(pattern, recursive=True):
            text = mask(Path(path).read_text(encoding="utf-8"))
            for m in REF_RE.finditer(text):
                n = m.group(1)
                counts[n] += 1
                where[n][path] += 1
            for m in HOMOGLYPH_RE.finditer(text):
                HOMOGLYPHS[path] += 1
    return counts, where


def main() -> int:
    allow_early = "--allow-early" in sys.argv
    have = declared()
    skips = skipped()
    early_declared = bool(EARLY_RE.search(Path(REGISTRY).read_text(encoding="utf-8")))
    refs, where = referenced()
    bases = {base(x) for x in have}
    lo, hi = min(bases), max(bases)
    gaps = [n for n in range(lo, hi + 1) if n not in bases]
    ref_bases = {base(x) for x in refs}
    dangling = sorted((x for x in refs if x not in have and x not in skips),
                      key=lambda x: (base(x), x))
    early = [n for n in dangling if base(n) < EARLY_BELOW]
    late = [n for n in dangling if base(n) >= EARLY_BELOW]

    print(f"реестр: {len(have)} номеров (различных имён), T-{lo}..T-{hi}")
    print(f"корпус ссылается на {len(refs)} различных номеров")

    # ЧИСЛО РЕЕСТРА, ПРОИЗНЕСЁННОЕ ПРОЗОЙ, ПРОТИВ САМОГО РЕЕСТРА.
    # Корпус называл свой реестр в двух местах — «273 теоремы реестра» и «269
    # теорем реестра», — и оба числа отстали: реестр давно больше. Никто этого не
    # видел, потому что числа помнились, а не считались. Правило перенесено из
    # math-foundations (инвариант 46 линтера строгости): состояние реестра
    # СЧИТАЕТСЯ по реестру, а не произносится по памяти.
    # Заявка живёт на ДВУХ языках и в ДВУХ локалях: «273 registry theorems» в
    # docs/ и «273 теоремы реестра» в i18n/ru/. Прибор, знающий один язык,
    # объявил бы чистой половину корпуса — тот же порок одного формата.
    SIZE_RE = re.compile(r"(\d{2,4})\s+(?:registry\s+(?:theorems|entries)"
                         r"|(?:теорем\w*|строк\w*|номеров|имён)\s+реестра)")
    _trees = [_SITE / "docs",
              _SITE / "i18n" / "ru" / "docusaurus-plugin-content-docs" / "current"]
    said_bad = []
    for _tree in _trees:
        if not _tree.is_dir():
            continue
        for f in sorted(_tree.rglob("*.md*")):
            for ln, line in enumerate(f.read_text(encoding="utf-8").split("\n"), 1):
                for m in SIZE_RE.finditer(line):
                    if int(m.group(1)) != len(have):
                        said_bad.append((f"{f.relative_to(_SITE)}:{ln}", m.group(0)))
    if said_bad:
        print(f"\nЧИСЛО РЕЕСТРА, ПРОИЗНЕСЁННОЕ ПРОЗОЙ, РАЗОШЛОСЬ С РЕЕСТРОМ: {len(said_bad)}")
        for loc, said in said_bad:
            print(f"   {loc}: «{said}» — в реестре {len(have)}")
        print("   правило: число реестра считается прибором, а не помнится текстом")
    if HOMOGLYPHS:
        total = sum(HOMOGLYPHS.values())
        print(f"\nКИРИЛЛИЧЕСКАЯ «Т» В НОМЕРЕ ТЕОРЕМЫ: {total} в {len(HOMOGLYPHS)} файлах")
        for path, k in HOMOGLYPHS.most_common(10):
            print(f"   {Path(path).name}: {k}")
        print("   такая ссылка НЕ ПРОВЕРЯЕТСЯ: она неотличима на вид и не совпадает")
        print("   с латинской ни в одном сравнении — и потому невидима этой проверке")
    if gaps:
        skip_bases = {base(x) for x in skips}
        unused = [n for n in gaps if n not in ref_bases or n in skip_bases]
        used = [n for n in gaps if n in ref_bases and n not in skip_bases]
        print(f"\nпропуски внутри диапазона: {gaps}")
        print(f"   из них не присвоены (объявлено реестром либо ни разу не упомянуты): {unused}")
        if used:
            print(f"   УПОМЯНУТЫ, но строки нет: {used}")

    if late:
        print(f"\nВИСЯЧИЕ в рабочем диапазоне ({len(late)}) — это дефекты:")
        for n in late:
            top = ", ".join(f"{Path(p).name}×{c}"
                            for p, c in where[n].most_common(3))
            print(f"   T-{n:<7} ссылок {refs[n]:>3}  {top}")

    if early:
        total = sum(refs[n] for n in early)
        print(f"\nРАННИЕ, вне реестра ({len(early)} номеров, {total} ссылок):")
        for n in early:
            top = ", ".join(f"{Path(p).name}×{c}"
                            for p, c in where[n].most_common(2))
            print(f"   T-{n:<7} ссылок {refs[n]:>4}  {top}")
        print("   Формулировки не восстанавливаются: полного источника нет.")
        print("   Инструмент сообщает, а не сочиняет — выдуманная строка")
        print("   реестра подделала бы полноту вместо того, чтобы её закрыть.")

    ghosts = registry_only()
    regtext = Path(REGISTRY).read_text(encoding="utf-8")
    ghost_declared = {m.group(1) for line in GHOST_RE.finditer(regtext)
                      for m in re.finditer(r"T-(\d{1,3}(?:\.\d+|[a-z])?)", line.group())}
    undeclared_ghosts = [g for g in ghosts if g[0] not in ghost_declared]
    if ghosts:
        print(f"\nОПОРА БЕЗ ФОРМУЛИРОВКИ ({len(ghosts)}): реестр ссылается на эти номера,")
        print("   строки под ними не имеет, и нигде в корпусе они больше не встречаются —")
        print("   в том числе на страницах, куда ведут сами ссылки:")
        for k, n in ghosts:
            print(f"   T-{k:<7} упоминаний в реестре {n}")

        if undeclared_ghosts:
            print("   НЕ ОБЪЯВЛЕНЫ реестром: "
                  + ", ".join("T-" + g[0] for g in undeclared_ghosts))
        else:
            print("   все они объявлены реестром как открытый долг")

    if late or undeclared_ghosts or said_bad:
        return 1
    if early and not (allow_early or early_declared):
        return 1
    if early:
        print("\nранний диапазон объявлен реестром — это названный пробел, не дефект")
    # Знаменатель обязателен: «все ссылки разрешаются» без числа сравнений —
    # не чистота, а молчание. Правило 2 дисциплины проверки (карта покрытия §7.5b
    # корпуса math-foundations).
    print(f"проверено ссылок {sum(refs.values())} на {len(refs)} различных номеров; "
          f"объявлено в реестре {len(have)}; висячих в рабочем диапазоне {len(late)}")
    print("все ссылки, кроме объявленного раннего диапазона, разрешаются")

    # --- СЧЁТ О СЕБЕ: проза реестра обязана сходиться с самим реестром ---
    # Прибор считал 392 строки и печатал это число — но с ПРОЗОЙ, которая тут же
    # рядом говорит «the registry holds 392 rows spanning T-1..T-325», не сверял
    # никто. Проверено подлогом: «399» вместо «392» проходило вентиль молча.
    # Число, произнесённое о себе, стареет тише всех прочих: оно верно в день
    # написания и остаётся выглядеть верным навсегда. Сверяются ОБЕ локали —
    # русская страница правится отдельно от английской и расходится с ней сама
    # собой, без чьего-либо умысла.
    self_bad, self_seen = [], 0
    nums_all = sorted({base(x) for x in have})
    want = {"строк": len(have), "низ": nums_all[0], "верх": nums_all[-1]}
    # NB (ПЕРВАЯ РЕДАКЦИЯ ЛОВИЛА НЕ ТО): шаблон диапазона брал ЛЮБОЕ «T-a–T-b»
    # на странице и объявлял расхождением всякое содержательное упоминание вроде
    # «T-112–T-113». Диапазон засчитывается только там, где он ЧАСТЬ ЗАЯВКИ О
    # СЕБЕ, — то есть в окне сразу за счётом строк. Страж, ловящий чужое, хуже
    # отсутствующего: его выключают целиком.
    ROWS_RE = re.compile(r"\*\*(\d{2,4})\s+(?:rows|строк[аи]?)")
    SPAN_RE = re.compile(r"T-(\d{1,3})\s*(?:\.\.|–|—|-)\s*T-(\d{1,3})")
    # ПУТЬ СТРАНИЦЫ БЕРЁТСЯ ОТ _SITE, А НЕ ОТ КОРНЯ РЕПОЗИТОРИЯ. Прежде здесь
    # стояли пути вида «website/docs/…», тогда как прибор, по собственной же
    # шапке, запускается ИЗ website/ — и обе страницы не находились. Страж
    # печатал «ПРОПУСК: страницы нет» и «ПУСТО: ни одной заявки не найдено»,
    # то есть НЕ СВЕРЯЛ НИЧЕГО, а вентиль при этом стоял красным по причине,
    # не имеющей отношения к корпусу. Остальной прибор давно берёт пути от
    # _SITE; расходились только эти две строки.
    PAGES = (str(_SITE / "docs" / "reference" / "status-registry.md"),
             str(_SITE / "i18n" / "ru" / "docusaurus-plugin-content-docs" /
                 "current" / "reference" / "status-registry.md"))
    for page in PAGES:
        fp = Path(page)
        if not fp.exists():
            print(f"  ПРОПУСК: {page} — страницы нет, счёт о себе не сверен")
            self_bad.append((page, "страница отсутствует", "", ""))
            continue
        txt = fp.read_text(encoding="utf-8")
        for m in ROWS_RE.finditer(txt):
            self_seen += 1
            if int(m.group(1)) != want["строк"]:
                self_bad.append((page, "строк", int(m.group(1)), want["строк"]))
            win = txt[m.end(): m.end() + 160]
            sp = SPAN_RE.search(win)
            if sp:
                self_seen += 1
                got = (int(sp.group(1)), int(sp.group(2)))
                if got != (want["низ"], want["верх"]):
                    self_bad.append((page, "диапазон", f"T-{got[0]}..T-{got[1]}",
                                     f"T-{want['низ']}..T-{want['верх']}"))
    print(f"счёт реестра о себе: сверено заявок {self_seen} на {len(PAGES)} "
          f"страницах (строк {want['строк']}, диапазон T-{want['низ']}..T-{want['верх']}); "
          f"расходится {len(self_bad)}")
    for b in self_bad:
        print(f"  РАСХОЖДЕНИЕ: {b[0]} — «{b[1]}» сказано {b[2]}, реестр даёт {b[3]}")
    if self_seen == 0:
        print("  ПУСТО: ни одной заявки не найдено — шаблоны разошлись с текстом")
        self_bad.append(("—", "знаменатель пуст", 0, 1))
    # --- ОДИН НОМЕР — ОДНА ФОРМУЛИРОВКА ---
    # Реестр пишет строки в нескольких таблицах, и нумерация у них СКВОЗНАЯ:
    # Level 1 идёт 1..48 с буквенными вариантами, Level 2 продолжает 39..52,
    # Level 3 — 53..90. Оттого номера 39..52 стоя́т сразу в двух живых таблицах
    # под РАЗНЫМИ формулировками, и цитата такого номера двусмысленна: читатель
    # не знает, на какую из двух он сослался. Прибор не решает, какая верна —
    # это дело автора корпуса, — но обязан назвать число и не дать ему расти
    # молча. Зачёркнутые строки и раздел снятых результатов не в счёт: там
    # переиспользование номера объявлено.
    coll = collections.defaultdict(list)
    _regt = Path(REGISTRY).read_text(encoding="utf-8")
    sec = ""
    for i, line in enumerate(_regt.split("\n"), 1):
        if line.startswith("#"):
            sec = line.strip("# ").strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not cells or not re.fullmatch(r"~{0,2}\*{0,2}(T-)?\d{1,3}[a-z]?\*{0,2}~{0,2}", cells[0]):
            continue
        struck = cells[0].startswith("~~") or (len(cells) > 1 and cells[1].startswith("~~"))
        if struck or "Retracted" in sec:
            continue
        body = cells[1] if len(cells) > 1 else ""
        coll[re.sub(r"[~*]|T-", "", cells[0])].append((sec, re.sub(r"[^a-zа-я0-9]", "", body.lower())[:60]))
    #: Таблицы-СПУТНИКИ перечисляют не соперничающую формулировку, а сведения О
    #: том же результате: внешнюю опору («Goderis–Verbeure–Vets 1989») или сводку
    #: универсального свойства. Номер, встреченный в такой паре, не двусмыслен —
    #: он просто назван дважды. Смешивать эти два случая нельзя: первая редакция
    #: этой проверки смешала и объявила 60 там, где всего 63, а настоящих 35.
    COMPANION = ("Framework-conditional", "Universal Property")
    dup = {k: v for k, v in coll.items() if len({b for _, b in v}) > 1}
    real = [k for k, v in dup.items()
            if not any(any(c in s for c in COMPANION) for s, _ in v)]
    D_ALL = re.compile(r"\*\*(\d{1,3})\*\* (?:номеров несут по две живые строки"
                       r"|numbers carry two live rows)")
    #: Число стои́т ВНУТРИ того же жирного пролёта, что и слова, — «**настоящих
    #: столкновений 35**», — и шаблон, искавший «**» после слов, не совпадал.
    D_REAL = re.compile(r"(?:настоящих столкновений|genuine collisions)[:\s]{1,3}(\d{1,3})")
    said_all, said_real = D_ALL.search(_regt), D_REAL.search(_regt)
    print(f"файлов {len(sorted(set(glob.glob(SOURCES[0], recursive=True))))}")
    print(f"один номер — одна формулировка: всего {len(dup)}, настоящих {len(real)}"
          + (f"; объявлено {said_all.group(1)}" if said_all else "; всего не объявлено")
          + (f" и {said_real.group(1)}" if said_real else " и настоящих не объявлено"))
    for got, said, name in ((len(dup), said_all, "всего"), (len(real), said_real, "настоящих")):
        if said is None:
            print(f"  реестр обязан назвать «{name}» сам — молчание успехом не считается")
            self_bad.append((REGISTRY, f"столкновения ({name}) не объявлены", got, "—"))
        elif int(said.group(1)) != got:
            print(f"  РАСХОЖДЕНИЕ «{name}»: объявлено {said.group(1)}, посчитано {got}")
            self_bad.append((REGISTRY, f"столкновения ({name})", int(said.group(1)), got))

    # --- СТРОКА РЕЕСТРА ПРОТИВ СВОЕЙ ЖЕ СТРАНИЦЫ ---
    # Строка реестра ссылается на раздел, где результат доказан. Если раздел с тех
    # пор получил ИСПРАВЛЕНИЕ, а строка о нём молчит, реестр объявляет верным то,
    # что страница уже отменила. Так и было со строкой T-151: она держала «direct
    # consequence of T-129», тогда как её раздел несёт «the earlier unconditional
    # derivation was invalid» с явным контрпримером.
    #
    # Две ловушки на пути, обе прожиты при постройке этой проверки.
    # ПЕРВАЯ — ОМОНИМ: слово «retraction» в этом корпусе чаще математическое
    # (ретракция симплекса на рог, ретракция OP² ⟶ CP⁶), и проба по СЛОВУ дала
    # два ложных срабатывания. Редакционную ретракцию опознаём по ФОРМЕ ВРЕЗКИ.
    # ВТОРАЯ — ГРАНИЦА РАЗДЕЛА: обрыв по «\n## » тянул раздел T-188 на тринадцать
    # тысяч знаков и захватывал исправление СОСЕДНЕЙ теоремы. Граница берётся по
    # уровню самого заголовка: раздел кончается на первом заголовке того же или
    # старшего уровня.
    RET_PAGE = re.compile(r":::(?:warning|danger|caution)\s+(?:Correction|Retraction)[^\n]*"
                          r"|^#{1,6}[^\n]*\bRetraction\b[^\n]*$"
                          r"|\*\*Retracted\*\*|\[\u2717\]", re.I | re.M)
    RET_ROW = re.compile(r"corrected|retract|reframed|repaired|clarified|scope\b"
                         r"|stratified|\[\u2717\]|Former\s+\w+\s*\[", re.I)
    ROW_LINK = re.compile(r"\]\(/docs/([^)#]+)#([^)]+)\)")
    ROW_NUM = re.compile(r"^\|\s*\*{0,2}(T-[0-9]+[a-z]?)\*{0,2}\s*\|([^\n]*)$", re.M)
    stale, seen_anchor, seen_ret = [], 0, 0
    for _num, _rest in ROW_NUM.findall(_regt):
        _m = ROW_LINK.search(_rest)
        if not _m:
            continue
        _f = _SITE / "docs" / (_m.group(1) + ".md")
        if not _f.exists():
            continue
        _t = _f.read_text(encoding="utf-8", errors="ignore")
        _i = _t.find("{#" + _m.group(2) + "}")
        if _i < 0:
            continue
        seen_anchor += 1
        _ls = _t.rfind("\n", 0, _i) + 1
        _lvl = len(re.match(r"#*", _t[_ls:]).group(0)) or 6
        _nxt = re.compile(r"^#{1,%d} " % _lvl, re.M).search(_t, _i + 1)
        _seg = _t[_i: _nxt.start() if _nxt else len(_t)]
        _r = RET_PAGE.search(_seg)
        if _r:
            seen_ret += 1
            if not RET_ROW.search(_rest):
                stale.append((_num, _m.group(1), " ".join(_r.group(0).split())[:80]))
    print(f"строка реестра против своей страницы: якорных разделов {seen_anchor}, "
          f"из них с редакционным исправлением {seen_ret}; строк, о нём молчащих: {len(stale)}")
    for _n, _p, _r in stale:
        print(f"  {_n} → {_p}: раздел несёт «{_r}», строка молчит")
    if stale:
        print("  правило: строка реестра не вправе объявлять верным то, "
              "что её собственная страница отменила")
        self_bad.append((REGISTRY, "строка молчит об исправлении своей страницы",
                         len(stale), 0))

    # === ССЫЛКА, НАЗВАННАЯ ЧУЖИМ КОРПУСОМ, ОБЯЗАНА ВЕСТИ В НЕГО ============
    # Подпись ссылки есть обещание читателю: «math-foundations» значит, что
    # клик приведёт в math-foundations. Найдено живьём: две ссылки, подписанные
    # «math-foundations, Part XVIII, Thm. 11.6/11.8», вели на корень
    # diakrisis.gst.st — узел чужого корпуса, скопированный из соседней ссылки.
    # Ни один прибор этого не видел: адрес разрешается, страница существует,
    # и лишь ПОДПИСЬ говорит не о том месте.
    #
    # Шов имеет две стороны, и стережёт каждую та, что ссылается.
    HOSTS = {"math-foundations": "math-foundations", "diakrisis": "diakrisis"}
    LINK = re.compile(r"\[([^\]\n]{1,120})\]\((https?://[^)\s]+)\)")
    link_seen, link_named, link_bad = 0, 0, []
    for _path in sorted(set(glob.glob(SOURCES[0], recursive=True))):
        _txt = mask(open(_path, encoding="utf-8").read())
        for _m in LINK.finditer(_txt):
            link_seen += 1
            _label, _url = _m.group(1).lower(), _m.group(2).lower()
            _host = _url.split("//", 1)[1].split("/", 1)[0]
            for _name, _needle in HOSTS.items():
                if _name in _label:
                    link_named += 1
                    if _needle not in _host:
                        link_bad.append((_path, _m.group(1)[:60], _host))
                    break
    print(f"подпись ссылки против её узла: внешних ссылок {link_seen}, "
          f"из них названных чужим корпусом {link_named}; расходится {len(link_bad)}")
    for _p, _lab, _h in link_bad:
        print(f"  {_p}: «{_lab}» ведёт на {_h}")
    if link_bad:
        print("  правило: подпись ссылки есть обещание читателю о том, куда он попадёт")
        self_bad.append(("ссылки", "подпись против узла", len(link_bad), 0))

    # --- ОБРАЩЕНИЕ ПО ИМЕНИ БЕЗ АДРЕСА (храповик) ---------------------------
    # Прибор до сих пор разрешал ссылки ПО НОМЕРУ (`T-96`) и молчал о ссылках
    # ПО ИМЕНИ: «по теореме Банаха», «by Girard's theorem». Имя не номер,
    # разрешать нечего — и потому такие обращения не проверял никто.
    #
    # Почему имя опаснее номера: номер, которого нет, виден сразу, а имя
    # выглядит убедительно всегда — у всякого знаменитого имени есть теорема,
    # и читатель достраивает нужную сам. В соседнем корпусе math-foundations
    # тот же просев дал 18 настоящих находок на 45 обращений, и они оказались
    # не косметикой: одна ссылка была ПРИПИСАНА НЕ ТОМУ (обратимость каналов
    # выдавалась за теорему Ульмана, который о подъёме очищений); другая звала
    # лемму, доказанную внутри чужого доказательства и не имевшую номера;
    # третья звала теорему, которой в корпусе НЕ БЫЛО ВОВСЕ.
    #
    # ЗАМЕР ЗДЕСЬ, а не перенос чужого числа: 371 файл, 85 обращений по имени
    # (53 русских, 32 английских), из них 64 без адреса. Править разом 64
    # места чужой прозы — значит рисковать той самой ошибкой приписки, от
    # которой прибор и стережёт. Потому храповик: долг НАЗВАН числом и не
    # растёт. Опускать базу по мере починки — руками и осознанно.
    #
    # Адресом считается ссылка markdown, номер реестра T-N, параграф, глава
    # или номер вида N.M в окне вокруг обращения.
    NAME_RU = re.compile(r"(?:по|из|согласно|в силу|применяя)\s+"
                         r"(?:теорем\w+|лемм\w+|формул\w+|принцип\w+)\s+"
                         r"((?:фон\s+)?[А-ЯЁ][а-яё]+(?:[-\u2013\u2014][А-ЯЁ][а-яё]+)*)")
    NAME_EN = re.compile(r"\bby\s+(?:the\s+)?([A-Z][a-z]+(?:[-\u2013][A-Z][a-z]+)*)"
                         r"(?:'s)?\s+(?:theorem|lemma|principle|formula)\b")
    NAME_ADDR = re.compile(r"\]\(|T-\d+|§\d|\d+\.\d+|Глав[аеы]\s+\d|[Cc]h\.\s*\d")
    NAME_BASE = 60          # 64 → 62 (25.09: кампания прецедентов дописала адреса); 62 → 60 (25.09: пропагация хвостов дала адреса); опускать руками, не поднимать
    name_seen = 0
    name_bad = []
    _paths = set()
    for _pat in (str(_SITE / "docs" / "**" / "*.md*"),
                 str(_SITE / "i18n" / "ru" / "**" / "*.md*")):
        _paths.update(glob.glob(_pat, recursive=True))
    for _path in sorted(_paths):
        _t = Path(_path).read_text(encoding="utf-8", errors="ignore")
        for _rx in (NAME_RU, NAME_EN):
            for _m in _rx.finditer(_t):
                name_seen += 1
                if NAME_ADDR.search(_t[max(0, _m.start() - 80):_m.end() + 140]):
                    continue
                name_bad.append((_path, _t[:_m.start()].count("\n") + 1,
                                 _m.group(0).replace("\n", " ")))
    print(f"обращение по имени: всего {name_seen}, без адреса {len(name_bad)} "
          f"(база храповика {NAME_BASE})")
    if len(name_bad) > NAME_BASE:
        print(f"  ХРАПОВИК: безадресных обращений стало больше базы "
              f"({len(name_bad)} > {NAME_BASE})")
        for _p, _ln, _w in name_bad[-12:]:
            print(f"  {_p}:{_ln}: «{_w}» — имя названо, адрес нет")
        print("  правило: имя не заменяет адреса; либо адрес, либо довод на месте")
        self_bad.append(("имена", "обращение без адреса", len(name_bad), NAME_BASE))
    elif len(name_bad) < NAME_BASE:
        print(f"  храповик можно опустить: было {NAME_BASE}, стало {len(name_bad)}")

    if self_bad:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
