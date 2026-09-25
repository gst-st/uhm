#!/usr/bin/env python3
"""ЧТО ВИДИТ ЧИТАТЕЛЬ: прибор, читающий СОБРАННУЮ страницу, а не исходник.

Прежние приборы корпуса читают ИСХОДНИК. Ни один не читал собранную страницу — а
между исходником и читателем стои́т разметка, и она умеет молча съедать смысл:
математика внутри обратных кавычек печатается долларами,
незакрытая врезка уходит на страницу словом `:::note`, якорь заголовка —
фигурными скобками, непарное выделение — звёздочками. Всё это проходит сборку
без единого предупреждения: `npm run build` рапортует SUCCESS.

Прибор читает `build/**/*.html`, снимает теги и смотрит на ВИДИМЫЙ текст.

Гасятся: `<pre>`, `<code>` (там разметка цитируется намеренно — и это снимает
нужду в перечне исключений), `<script>`, `<style>` и `<annotation>` внутри
KaTeX (там лежит исходный TeX формулы, а не то, что видно).

СВЕЖЕСТЬ. Сборка старше исходников есть отсутствие свидетельства, а не чистота:
прибор в этом случае ПАДАЕТ и говорит, чего не хватает. Прибор, молчащий на
устаревших данных, хуже отсутствующего — он выдаёт незнание за проверку.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
BUILD = ROOT / "build"
DOCS = ROOT / "docs"
# ОХВАТ: страницы этого сайта пишутся и в `.md`, и в `.mdx`. Образец `*.md`
# видел 177 файлов там, где их 178, — и страница `coherence-matrix.mdx` была
# невидима проверке свежести: правь её посреди сборки, и прибор смолчит.
# Расхождение нашлось сверкой охвата между приборами, а не чтением кода.
# ОТМЕТКА СВЕЖЕСТИ. Сперва ею была `build/index.html` — и она ЛГАЛА. Страница
# пишется в САМОМ КОНЦЕ сборки, а исходники читаются в начале; правка, сделанная
# ПОСРЕДИ сборки, оказывается новее исходников, но старее итоговой страницы — и
# прибор объявлял свежим то, чего в сборке нет. Поймано на живом: правка в 17:59
# не попала в страницу, дописанную в 18:05, а прибор смолчал.
# Верная отметка — то, что пишется РАНЬШЕ чтения исходников: `.docusaurus`
# перезаписывается при загрузке содержимого, до всякой компиляции. Всё, что новее
# её, в сборку могло не попасть — и прибор обязан считать это несвежим. Ошибка
# при этом сдвинута в безопасную сторону: правка между загрузкой и компиляцией
# будет объявлена несвежей, хотя и попала, — лишний прогон дешевле ложной чистоты.
# Признаком ЗАВЕРШЁННОСТИ служит не какая-то одна страница, а САМАЯ ПОЗДНЯЯ из
# собранных: на многоязычном сайте локали собираются по очереди, `.docusaurus`
# переписывается каждой из них, и корневая `index.html` оказывается старше
# загрузки последней локали — прибор объявлял бы оборванной законченную сборку.
LOADED = ROOT / ".docusaurus" / "globalData.json"

DROP = re.compile(
    r"<pre\b.*?</pre>|<code\b.*?</code>|<script\b.*?</script>"
    r"|<style\b.*?</style>|<annotation\b.*?</annotation>", re.S | re.I)
TAGS = re.compile(r"<[^>]+>")
#: КАРТОЧКА ПОРОЖДЁННОГО УКАЗАТЕЛЯ категории. Её текст берётся из `description`
#: шапки документа, а при его отсутствии — из ПЕРВОГО АБЗАЦА, и печатается
#: ПРОСТЫМ ТЕКСТОМ, без разметки: документ, начинающийся врезкой с формулой,
#: показывает читателю «$\varepsilon \dashv \alpha$» буквально. Проверка стои́т
#: здесь, а не в братском корпусе одном, потому что прибор у двух корпусов один
#: и логика его обязана быть одна; в этом корпусе порождённых указателей пока
#: нет — проверка держится ПОДЛОГОМ, а не молчанием (правило 25).
#: КАВЫЧКИ ВОКРУГ ЗНАЧЕНИЯ АТРИБУТА НЕОБЯЗАТЕЛЬНЫ: минификатор их снимает, и
#: образец, требующий кавычек, молча перестаёт видеть — найдено при переносе
#: прибора в третий корпус, где сборка минифицирует разметку.
CARD = re.compile(r"<article[^>]*class=\"?[^\"'>]*card[^\"'>]*\"?[^>]*>(.*?)</article>", re.S | re.I)
CARD_MARKUP = re.compile(r"\$|\\[a-zA-Z]{2,}|\*\*|`")
#: собственные имена корпуса со звёздочками — имена теорем, а не разметка
OWN_NAMES = re.compile(r"T-2f\*{1,3}")


#: ВАЛЮТА — НЕ МАТЕМАТИКА: «$50-500M/год … $2-20M/год» даёт пару долларов, между
#: которыми нет ни одной команды TeX. Отличие точное и проверяемое: у валюты ОБА
#: доллара начинают число, у невыведенной формулы — хотя бы один открывает
#: выражение. Гасится по признаку, а не по списку глав.
def _currency(vis: str, m: "re.Match") -> bool:
    return vis[m.start() + 1:m.start() + 2].isdigit() and vis[m.end():m.end() + 1].isdigit()

CHECKS = (
    ("сырая пара долларов", re.compile(r"\$[^$\n]{2,80}\$"), _currency),
    ("невыведенная команда TeX", re.compile(r"\\[a-zA-Z]{3,}"), None),
    ("фенс врезки в тексте", re.compile(r":::[a-zа-я]*"), None),
    ("якорь заголовка в тексте", re.compile(r"\{#[A-Za-z0-9_-]+\}"), None),
    # Одиночная звёздочная пара — часть ИМЕНИ: «T-2f**» есть теорема Diakrisis,
    # и разметка её не съела. Порча выглядит иначе — как ПАРА пар, то есть
    # незакрывшееся выделение: «**некорректно**» внутри \text{} формулы.
    # Порча не имеет пробела вплотную к звёздочкам («**некорректно**»), а имя —
    # имеет («T-2f** : тонкие…»): пробел и различает их.
    ("незакрывшееся выделение", re.compile(r"\*\*(?!\s)[^*\n]{1,60}(?<!\s)\*\*"), None),
)

# Оглавление страницы («На этой странице») собирается разметкой ОТДЕЛЬНО от тела,
# и встроенный сборщик оглавления сводил формулу заголовка к её ГОЛОМУ TeX без
# разделителей — читатель видел «\\mathrm{Cl}(0, 0) = K». Порча была не корпуса,
# а связки заголовок–оглавление, и была СИСТЕМНОЙ; её чинит `plugins/remark-toc-katex.js`,
# собирающий значение строки оглавления заново из того же заголовка. База опущена
# до нуля: храповик из отступающего стал держащим — вырасти порче он не даёт.
# Считается по ВИДИМОМУ тексту ссылки, а не по её размётке: отрисованная KaTeX
# формула несёт свой же исходный TeX в узле <annotation>, и прибор, читающий
# размётку целиком, принял бы починенное оглавление за нечиненое.
TOC_LINK = re.compile(r'''<a[^>]*class="?[^"'>]*table-of-contents__link[^"'>]*"?[^>]*>(.*?)</a>''', re.S)
TOC_TEX = re.compile(r"\\[a-zA-Z]{3,}")
TOC_BASELINE = 0


def visible(html: str) -> str:
    return TAGS.sub(" ", DROP.sub(" ", html))


FENCE = re.compile(r"^(:{3,})(\w*)")


RU_DOCS = ROOT / "i18n" / "ru" / "docusaurus-plugin-content-docs" / "current"
INLINE_MATH = re.compile(r"(?<![\\$])\$(?!\$)(.+?)(?<![\\$])\$(?!\$)")


def pipe_in_table_math(roots):
    """ПРЕДПОЛЁТ ПО ИСХОДНИКУ: вертикальная черта внутри `$…$` в строке таблицы.

    Таблица GFM делит строку на ячейки РАНЬШЕ, чем разбирается формула: модуль
    `$|\\mathrm{QR}(7)|$` в строке реестра разрезает ячейку, доллары расходятся
    по разным ячейкам, и хвост строки печатается формулой — сборка успешна.
    25.09.2026 так дважды уходили в TeX строки реестра (T-265 и T-38b, по 29 и 2
    невыведенных команды на локаль), и оба раза это видела лишь сборка.
    Модуль в таблице пишется `\\lvert…\\rvert`. Проверяются обе локали; строки
    внутри блоков кода и формульных блоков `$$` таблицей не считаются.
    """
    bad = []
    for root in roots:
        for f in sorted(root.rglob("*.md*")):
            code = display = False
            for i, line in enumerate(f.read_text(encoding="utf-8").split("\n"), 1):
                s = line.strip()
                if s.startswith("```"):
                    code = not code
                    continue
                if not code and s == "$$":
                    display = not display
                    continue
                if code or display or not s.startswith("|"):
                    continue
                for m in INLINE_MATH.finditer(line):
                    if re.search(r"(?<!\\)\|", m.group(1)):
                        bad.append((f, i, m.group(1)[:60]))
    return bad


#: Строка-разделитель GFM во всех формах: `| --- |`, `|:--|`, `|-|`, `--- | ---`,
#: с пробелами и без, с выравниванием `:` с любой стороны.
TABLE_SEP = re.compile(r"^\|?\s*:?-+:?\s*(?:\|\s*:?-+:?\s*)*\|?\s*$")
#: Фенс блока кода: ``` или ~~~ (три и больше), закрывается тем же знаком не короче.
CODE_FENCE = re.compile(r"^(`{3,}|~{3,})")
INLINE_CODE = re.compile(r"`[^`\n]*`")


def _row_like(s: str) -> bool:
    """Похожа ли строка на строку таблицы: начинается и кончается чертой и
    делится хотя бы на две ячейки ВНЕ формул и кода. Так строка `$$`-блока
    `|ψ⟩ = α|0⟩ + β|1⟩` и модуль `|x|` в прозе строкой таблицы не считаются."""
    if not (s.startswith("|") and s.rstrip().endswith("|")):
        return False
    bare = INLINE_CODE.sub(" ", INLINE_MATH.sub(" ", s))
    return len(re.findall(r"(?<!\\)\|", bare)) >= 3


def headerless_table_rows(roots, *, files=None):
    """ПРЕДПОЛЁТ ПО ИСХОДНИКУ: блок строк таблицы без шапки и разделителя.

    GFM признаёт таблицу только по паре «шапка + строка-разделитель». Строки
    `| … | … |`, стоящие ДО шапки или отделённые от своей таблицы пустой строкой,
    таблицей не становятся: читатель видит абзац с буквальными «|», а сборка
    рапортует успех. 25.09.2026 так печатались 33 строки EN-реестра T-293…T-325:
    они стояли между заголовком «Level [C]: Sensorimotor Theory» и шапкой
    таблицы (дрейф EN от RU с 06.08, acbf65b; аудит A-93).

    Черновой детектор давал 158 срабатываний, и ложными были: строки внутри
    выключных формул `$$ … $$` (`|ψ⟩ = …`), внутри блоков кода и разделители
    непривычной формы (`|:--|`, `|-|`). Здесь: коды и `$$`-блоки пропускаются
    (блок `$$` отслеживается по нечётному числу `$$` в строке — так верно
    читаются и `$$` на отдельной строке, и `$$\\begin{…}`, и однострочная
    `$$ x $$`); строкой таблицы считается лишь строка, начатая и законченная
    чертой, с двумя и более ячейками вне формул и кода; разделитель — любой
    формы GFM. Нарушение — прогон подряд идущих строк таблицы, в котором до
    первой строки-разделителя больше одной строки (лишние стоят без шапки) или
    разделителя нет вовсе. Возвращает (файл, первая строка, число строк, образец).
    """
    bad = []
    paths = files if files is not None else [
        f for root in roots for f in sorted(root.rglob("*.md*"))]
    for f in paths:
        lines = pathlib.Path(f).read_text(encoding="utf-8").split("\n")
        fence, display = None, False
        run = []                                    # [(номер, строка)]

        def close_run():
            if not run:
                return
            sep = next((k for k, (_, s) in enumerate(run) if TABLE_SEP.match(s)), None)
            if sep is None:
                orphans = run
            elif sep >= 2:
                orphans = run[:sep - 1]             # всё до шапки
            else:
                orphans = []
            if orphans:
                bad.append((f, orphans[0][0], len(orphans), orphans[0][1][:70]))
            run.clear()

        for i, line in enumerate(lines, 1):
            s = re.sub(r"^(?:\s*>)*\s*", "", line)   # цитата и отступ списка
            m = CODE_FENCE.match(s)
            if fence:
                if m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence):
                    fence = None
                continue
            if m:
                close_run()
                fence = m.group(1)
                continue
            if not display and s.count("$$") % 2 == 1:
                close_run()
                display = True
                continue
            if display:
                if s.count("$$") % 2 == 1:
                    display = False
                continue
            if run and (TABLE_SEP.match(s) and "|" in s or _row_like(s)):
                run.append((i, s))
            elif _row_like(s):
                run.append((i, s))
            else:
                close_run()
        close_run()
    return bad


#: ХРАПОВИК «строк таблицы без шапки»: измерено 25.09.2026 на a61647d — 11 блоков
#: (EN 5, RU 6), все подтверждены собранной страницей (буквальные «|» в тексте):
#: notation.md ×4 в каждой локали — HTML-комментарий `<!-- DRY … -->` посреди
#: таблицы рвёт её, и строки под ним печатаются абзацем (строки 39, 43, 295, 298);
#: status-registry.md C32…C36 — пять строк после врезки о перенумерации, без шапки
#: (EN 829, RU 827); axiom-septicity.md (RU 1183) — четыре строки таблицы Розена
#: после врезки «Омонимия символа Φ». Долг только падает — опускайте базу вслед.
#: 11 → 0 (25.09.2026): комментарии DRY вынесены над шапкой таблиц notation.md,
#: у C32…C36 реестра своя шапка, врезка о Φ в RU axiom-septicity — после таблицы (как в EN).
HEADERLESS_BASE = 0


def fence_nesting(docs: pathlib.Path):
    """ПРЕДПОЛЁТ ПО ИСХОДНИКУ: вложенная врезка тем же числом двоеточий.

    Docusaurus закрывает врезку ПЕРВЫМ же `:::`, поэтому `:::warning`, внутри
    которой стоит `:::danger`, разваливается молча: сборка успешна, а лишний
    фенс печатается читателю как текст. Внешняя врезка обязана иметь двоеточий
    БОЛЬШЕ внутренней (`::::warning` вокруг `:::danger`).

    Проверка читает ИСХОДНИК и потому отвечает за секунду — тогда как та же
    находка через собранные страницы стоит полной пересборки. Это не замена
    чтению сборки, а его дешёвый предпролог: здесь ловится ровно один класс
    порчи, зато до того, как он попадёт в вывод.
    """
    bad = []
    for f in sorted(docs.rglob("*.md*")):
        stack = []
        for i, line in enumerate(f.read_text(encoding="utf-8").split("\n"), 1):
            m = FENCE.match(line)
            if not m:
                continue
            colons, word = len(m.group(1)), m.group(2)
            if word:
                if stack and colons >= stack[-1][0]:
                    bad.append((f, i, f"{colons}× внутри {stack[-1][0]}× (открыта строкой {stack[-1][1]})"))
                stack.append((colons, i))
            elif stack:
                if colons != stack[-1][0]:
                    bad.append((f, i, f"{colons}× закрывает {stack[-1][0]}×"))
                stack.pop()
            else:
                bad.append((f, i, "закрытие без открытия"))
        for colons, i in stack:
            bad.append((f, i, f"врезка {colons}× не закрыта"))
    return bad


def main() -> int:
    # ОХВАТ НАЗЫВАЕТСЯ ПЕРВЫМ. Прежде прибор при всяком раннем отказе (сборки нет,
    # сборка устарела) уходил, не назвав ни одного числа, и вентиль справедливо
    # писал «охват не назван» поверх настоящей находки. Молчание об охвате —
    # отдельный порок, и смешивать его с падением по делу не следует.
    print(f"файлов {len(list(DOCS.rglob('*.md*')))}")
    nesting = fence_nesting(DOCS)
    print(f"вложенность врезок (по исходнику): нарушений {len(nesting)}")
    for f, i, why in nesting[:10]:
        print(f"  {f.relative_to(ROOT)}:{i}: {why}")
    if nesting:
        print("  правило: внешняя врезка — больше двоеточий, чем внутренняя; иначе фенс уходит в текст")
        return 1
    pipes = pipe_in_table_math((DOCS, RU_DOCS))
    print(f"черта внутри формулы в строке таблицы (по исходнику, обе локали): нарушений {len(pipes)}")
    for f, i, body in pipes[:10]:
        print(f"  {f.relative_to(ROOT)}:{i}: ${body}$")
    if pipes:
        print("  правило: модуль в таблице — \\lvert…\\rvert; черта делит ячейку раньше формулы")
        return 1
    orphans = headerless_table_rows((DOCS, RU_DOCS))
    print(f"строки таблицы без шапки (по исходнику, обе локали): блоков {len(orphans)} "
          f"(база {HEADERLESS_BASE}), строк {sum(n for _, _, n, _ in orphans)}")
    for f, i, n, body in orphans:
        print(f"  {f.relative_to(ROOT)}:{i}: {n} стр. — {body}")
    if len(orphans) > HEADERLESS_BASE:
        print("  правило: строки таблицы идут под шапкой и разделителем, без пустой строки,"
              " врезки или комментария между ними — иначе печатаются абзацем с «|»")
        return 1
    if len(orphans) < HEADERLESS_BASE:
        print(f"  БАЗА ХРАПОВИКА УСТАРЕЛА: опустите HEADERLESS_BASE до {len(orphans)}")
        return 1
    if not BUILD.exists():
        print("СБОРКИ НЕТ: каталог build/docs отсутствует")
        print("  правило: отсутствие свидетельства не есть чистота — соберите `npm run build`")
        return 1
    pages = list(BUILD.rglob("*.html"))
    if not pages:
        print("СБОРКИ НЕТ: собранных страниц не найдено")
        print("  правило: отсутствие свидетельства не есть чистота — соберите `npm run build`")
        return 1
    newest_page = max(p.stat().st_mtime for p in pages)
    if not LOADED.exists():
        print("ОТМЕТКИ ЗАГРУЗКИ НЕТ: каталог .docusaurus отсутствует")
        print("  правило: без отметки свежесть недоказуема — соберите заново")
        return 1
    stamp = LOADED
    if newest_page < LOADED.stat().st_mtime:
        print("СБОРКА НЕ ДОВЕДЕНА ДО КОНЦА: страницы старше загрузки содержимого")
        print("  правило: прибор читает вывод завершившейся сборки, а не оборванной")
        return 1
    stale = [f for f in DOCS.rglob("*.md*") if f.stat().st_mtime > stamp.stat().st_mtime]
    if stale:
        print(f"СБОРКА СТАРШЕ ИСХОДНИКОВ: новее отметки {stamp.name} — файлов {len(stale)}")
        for f in sorted(stale)[:10]:
            print(f"  {f.relative_to(DOCS)}")
        print("  правило: прибор, молчащий на устаревших данных, выдаёт незнание за проверку")
        return 1

    pages, chars, toc_tex, toc_files = 0, 0, 0, set()
    found = {name: [] for name, _, _ in CHECKS}
    cards = []
    for f in sorted(BUILD.rglob("*.html")):
        raw = f.read_text(errors="replace")
        # оглавление вырезается из тела и считается отдельно
        toc_here = 0
        for m_toc in TOC_LINK.finditer(raw):
            toc_here += len(TOC_TEX.findall(visible(m_toc.group(1))))
        if toc_here:
            toc_tex += toc_here
            toc_files.add(f.relative_to(BUILD).as_posix())
        raw = TOC_LINK.sub(" ", raw)
        vis = visible(raw)
        pages += 1
        chars += len(vis)
        for m_card in CARD.finditer(raw):
            ctext = " ".join(TAGS.sub(" ", m_card.group(1)).split())
            if CARD_MARKUP.search(OWN_NAMES.sub(" ", ctext)):
                cards.append((f.relative_to(BUILD).as_posix(), ctext[:110]))
        vis = OWN_NAMES.sub(" ", vis)
        for name, pat, skip in CHECKS:
            for m in pat.finditer(vis):
                if skip is not None and skip(vis, m):
                    continue
                frag = vis[max(0, m.start() - 40):m.end() + 40]
                found[name].append((f.relative_to(BUILD).as_posix(),
                                    " ".join(frag.split())[:110]))

    bad = 0
    if cards:
        bad += len(cards)
        print(f"\nКАРТОЧКА УКАЗАТЕЛЯ ПОКАЗЫВАЕТ РАЗМЕТКУ — {len(cards)}:")
        for loc, frag in cards[:12]:
            print(f"  {loc}: …{frag}…")
        print("  правило: документу, начинающемуся формулой или врезкой,"
              " описание в шапке обязательно")
    for name, _, _ in CHECKS:
        hits = found[name]
        if hits:
            bad += len(hits)
            print(f"\n{name.upper()} — {len(hits)}:")
            for loc, frag in hits[:12]:
                print(f"  {loc}: …{frag}…")
            if len(hits) > 12:
                print(f"  …и ещё {len(hits) - 12}")

    if toc_tex > TOC_BASELINE:
        bad += 1
        print(f"\nМАТЕМАТИКА В ЗАГОЛОВКАХ ВЫРОСЛА: {toc_tex} против базы {TOC_BASELINE}")
        print("  правило: храповик затягивается, но не отпускается")
    elif toc_tex < TOC_BASELINE:
        bad += 1
        print(f"\nБАЗА ХРАПОВИКА УСТАРЕЛА: мест {toc_tex}, а записано {TOC_BASELINE}")
        print(f"  правило: опустите TOC_BASELINE до {toc_tex} — храповик обязан быть тугим")
    print(f"\nфайлов {sum(1 for _ in DOCS.rglob('*.md*'))}; "
          f"страниц {pages}; видимых знаков {chars}; "
          f"сырого TeX в оглавлениях {toc_tex} (база {TOC_BASELINE}) "
          f"в {len(toc_files)} страницах; "
          + "; ".join(f"{name} {len(found[name])}" for name, _, _ in CHECKS))
    print("правило: сборка молчит о разметке, съевшей смысл — читает её только этот прибор")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
