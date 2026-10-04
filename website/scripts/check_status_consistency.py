#!/usr/bin/env python3
"""СТАТУС ОДНОГО РЕЗУЛЬТАТА — ОДИН: прибор, читающий реестр как канон, а корпус как цитаты.

Дефект, ради которого написан прибор, назвал внешний аудитор 10.09.2026: у корпуса
нет МЕХАНИЗМА пропагации статусов. Признание в боксе при [T] в шапке ничего не
исправляет — оно создаёт второй дефект: страница утверждает и P, и ¬P, а
зависимая теорема и внешний читатель берут именно [T]-версию.

Прибор проверяет четыре правила:

  R1  СТАТУС. Всякая внутритекстовая пометка `T-n [X]` обязана согласоваться со
      статусом строки T-n в реестре. Реестр — канон.
  R2  ЛЕГЕНДА. Всякая страница, определяющая букву статуса, обязана определять её
      так же, как реестр. (Одна буква — одно значение.)
  R3  ОТОЗВАННОЕ. Отозванная формулировка не смеет появиться вне контекста
      отзыва (строка без маркера «отозвано / retracted / прежняя редакция»).
  R4  УСЛОВИЕ [C]. Строка реестра со статусом [C] обязана называть допущение.
  R7  ОПОРА НА ОТОЗВАННОЕ. Номер, отозванный реестром ЦЕЛИКОМ ([✗]), не смеет
      стоять в контексте опоры («by T-58», «из T-178», «(T-48a)», «conditional on»)
      без пометки отзыва в том же предложении, соседнем, в начале абзаца, в шапке
      врезки или в заголовке раздела. Цитату «T-n [T]» при [✗] ловит R1; R7 ловит
      опору БЕЗ буквы статуса.

ЧТЕНИЕ РЕЕСТРА. Наивный разбор («любая буква в скобках») ЛЖЁТ: строка
«— raised from [H]» называет ПРЕЖНИЙ статус, а не текущий, и прибор объявлял бы
законную цитату [T] расхождением. Отсюда три поправки: контексты повышения
(`raised from`, `повышен с`, `corrected from`) исключаются; зачёркнутые строки
(`~~…~~`) — это ретракции, они не канон; несколько строк с одним номером
(63 таких пары, реестр их объявляет) дают ОБЪЕДИНЕНИЕ допустимых статусов.

НЕ-T НОМЕРА (аудит A-84, 25.09.2026). Реестр держит ещё семейства `CC-n`
(`КК-n`) и `Pred n`; прежде прибор их не разбирал, и R1/R4 их не видели. Теперь
они классифицируются отдельно (свой долг R5x), цитаты и носители страницы
предсказаний сверяются правилом R1x, строки [C] — правилом R4x. Номера `C12`,
`H3`, `P2` не входят: эти буквы с цифрой в корпусе многозначны.

ХРАПОВИК. Числа расхождений сравниваются с базой ниже: расти им нельзя.
Уменьшил — обнови базу.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
LOCALES = {
    "en": (ROOT / "docs", "T"),
    "ru": (ROOT / "i18n/ru/docusaurus-plugin-content-docs/current", "Т"),
}

# ХРАПОВИК: после фундаментального согласования 03.10.2026 все базы равны нулю.
# Исторические комментарии ниже объясняют происхождение устранённого долга.
BASE_R1 = {"en": 0, "ru": 0}
# 44/49 → 43/48 (25.09.2026): кампания прецедентов назвала допущение у одной строки [C].
# 43/48 → 43/47 (25.09.2026): русской строке T-120b вернули фразу английской, называющую допущение.
# 43/47 → 43/46 (25.09.2026): русская строка T-151 переведена с английской — ушла пометка «C2 [С] → [Т]».
# 43/46 → 43/45 (25.09.2026): измерено после волны a9f3de9 (T-64 → [Г], строки C12/C13/C35 переписаны).
# 43/45 → 43/44 (25.09.2026): измерено после переформулировки T-119 … T-121 (русская строка [С] с названным условием).
BASE_R4 = {"en": 0, "ru": 0}
# R5: у скольких номеров нет машиночитаемой канонической записи статуса.
# Это и есть механизмический долг, названный аудитом 10.09.2026: пока он не нуль,
# пропагация статусов держится на руках. Расти ему нельзя.
BASE_DEBT = {"en": 0, "ru": 0}
# R6: сколько теорем [T] опираются на более слабую опору, не унаследовав её статус.
# 0 → 2 (25.09.2026) — не рост долга, а прозрение прибора: опоры читаются по реестру,
# окно в 60 строк снято. Названы оба: T-120 [T] на T-118 [C] (emergent-manifold) и
# теорема на T-190 [C] (fundamental-closures).
# 2 → 0 (25.09.2026): T-120 и T-121 понижены до [C], T-223 не пользуется ни T-120, ни T-190.
BASE_R6 = {"en": 0, "ru": 0}
# НЕ-T НОМЕРА (CC-n/КК-n, Pred n) — измерено 25.09.2026 на a61647d в миг прозрения.
# R1x — цитаты и носители страницы предсказаний против реестра; R4x — их строки [C]
# без названного допущения; долг R5x — номера без машиночитаемой записи статуса.
BASE_R1X = {"en": 0, "ru": 0}
# R4x 0 → 4: Pred 3 ([T]/[C]), Pred 7, Pred 11, Pred 15 — [C] в колонке статуса без
# названного допущения (в обеих локалях одни и те же четыре строки).
# 4 → 3 (26.09.2026): Pred 15 переформулировано — «[C at (MaxΦ)]» называет допущение.
BASE_R4X = {"en": 0, "ru": 0}
BASE_DEBTX = {"en": 0, "ru": 0}
# R7 — опора на ЦЕЛИКОМ отозванный номер без пометки отзыва рядом. Измерено 26.09.2026
# на c7900f5 в миг прозрения: 5/4 (en/ru) — T-58 в «Claim [C] … conditional on T-58»
# (dimension-e) и в строке реестра T-95 («rests on T-58 [C]»), T-58 «is itself [C]»
# (operationalization, en), T-178 в двух ссылках notation на «T-178–T-181».
# 5/4 → 0/0 (26.09.2026): все девять переопёрты на T-58′ или помечены отзывом.
BASE_R7 = {"en": 0, "ru": 0}

CYR2LAT = {"Т": "T", "С": "C", "Г": "H", "П": "P", "О": "D", "И": "I"}
WEAKER_OK = {"✗"}   # ретракция — не «более слабая опора», а снятие
STATUS_CHARS = "TCHPDIТСГПОИ✗"
# Дата между глаголом и предлогом («corrected 2026-09-25 from [T]», «исправлено
# 2026-09-25 с [Т]») — та же форма повышения: без неё строка Pred 7 читалась бы
# как [T] рядом со своим текущим [C] (аудит A-84, 25.09.2026).
_DATE = r"(?:\s+\d{4}-\d{2}-\d{2})?"
RAISED = re.compile(
    r"(raised" + _DATE + r" from|corrected" + _DATE + r" from|повышен[аоы]?" + _DATE + r" с"
    r"|исправлен[аоы]?" + _DATE + r" с|поднят[аоы]?" + _DATE + r" с"
    # Понижение называет прежний статус так же, как повышение: «The status had
    # earlier been lowered from [T]» в строке CC-5 делал её [C]+[T], и цитата
    # «CC-5 [T]» прошла бы молча.
    r"|lowered" + _DATE + r" from|downgraded" + _DATE + r" from|понижен[аоы]?" + _DATE + r" с)\s*\*{0,2}\[?[" + STATUS_CHARS + r"]\]?",
    re.I,
)
# «Old Fano bound retracted [✗]», «Butterfly A₅ отозвана [✗]» — снятая ПОД-ЧАСТЬ
# строки, а не статус самой строки. Не отличив одно от другого, прибор объявлял
# тринадцать законных цитат «T-77/T-80/T-86 [T]» расхождением.
RETRACTED_SUB = re.compile(
    r"(retracted|withdrawn|отозван[аоы]?|ретрактирован[аоы]?|снят[аоы]?)\s*\*{0,2}\[✗\]",
    re.I,
)
# «H3 [H] → CLOSED», «Г3 [Г] → ЗАКРЫТО» — статус выражен прозой, а не буквой
CLOSED = re.compile(r"\[[" + STATUS_CHARS + r"]\]\s*(→|->)\s*(CLOSED|ЗАКРЫТ[АОЫ]?)", re.I)
ROW = re.compile(r"^\|\s*\*{0,2}~{0,2}\s*(T-\d+(?:\.\d+)?[a-z]?|\d+[a-z]?)\s*~{0,2}\*{0,2}\s*\|(.*)$")
# НЕ-T НОМЕРА РЕЕСТРА (аудит A-84, 25.09.2026). Реестр держит ещё два семейства
# с собственной нумерацией: теоремы кибернетики когерентности `CC-n` (в русской
# локали `КК-n`) и реестр предсказаний `Pred n`. Образец `ROW` знал только T-номера,
# и шестнадцать строк CC/КК плюс сорок четыре Pred не читались вовсе: цитата
# «CC-5 [T]» при строке «[C at (HOL)]» прошла бы R1 молча, а R4 не видел их [C].
# Семейства однозначны: префикс не совпадает ни с чем в корпусе. Номера `C12`,
# `H3`, `P2` — нет: те же буквы с цифрой означают условия, гипотезы, принципы и
# шаги доказательств, и перенумерация «C32 (was C22)» их размывает; они сюда не
# входят. Канонический ключ одинаков в обеих локалях: `КК-n` → `CC-n`.
XROW = re.compile(r"^\|\s*\*{0,2}~{0,2}\s*(CC-\d+|КК-\d+|Pred \d+)\s*~{0,2}\*{0,2}\s*\|(.*)$")
XFAMILIES = ("CC", "Pred")
# Цитата не-T номера: «CC-5 [C at (HOL)]», «[КК-7](…) [Т]», «Pred 7 [C]».
XCITE = re.compile(
    r"(?<![\w-])(CC-\d+|КК-\d+|Pred \d+)(?:\]\([^)\s]*\))?\*{0,2}\s*\*{0,2}\[([" + STATUS_CHARS + r"])")
# Страница предсказаний пишет статус не цитатой, а носителем раздела:
# «### Prediction 7: …» → «:::info Prediction [C]» или «**Status:** [C] …».
PRED_HEAD = re.compile(r"^#{2,4}\s+(?:Prediction|Предсказание)\s+(\d+)\b")
PRED_CARRIER = re.compile(r"^(?::::\w+\s+(?:Prediction|Предсказание)|\*\*(?:Status|Статус):\*\*)")


def xkey(tid):
    """Канонический ключ не-T номера: `КК-5` и `CC-5` — один результат."""
    return "CC-" + tid[3:] if tid.startswith("КК-") else tid
# Токен статуса: [T], [Т/С], [T/sim], [T at …], [Т при …] — все формы, что в ходу.
TOKEN = re.compile(
    r"\[([" + STATUS_CHARS + r"])(?:/(?:sim|[" + STATUS_CHARS + r"]))?"
    r"(?:\s+(?:at|on|under|given|при|на)\b[^\]]*)?\]"
)


CONDITIONED = re.compile(
    r"\[[" + STATUS_CHARS + r"](?:/(?:sim|[" + STATUS_CHARS + r"]))?\s+(?:at|on|under|given|при|на)\b[^\]]*\]"
)


def status_letters(text):
    out = set()
    for m in TOKEN.finditer(text):
        out.add(norm(m.group(1)))
        second = m.group(0)
        for extra in re.findall(r"/([" + STATUS_CHARS + r"])\]", second):
            out.add(norm(extra))
    return out
# Цитата бывает и ССЫЛКОЙ: «[T-119](/docs/…) [T]». Прежний образец требовал букву
# сразу за номером и не видел ни одной цитаты-ссылки: три заголовка spacetime держали
# «T-119 [T]» при реестре [C], и R1 молчал (аудит A-37, 25.09.2026).
CITE = re.compile(r"\b(T-\d+(?:\.\d+)?[a-z]?)(?:\]\([^)\s]*\))?\*{0,2}\s*\*{0,2}\[([" + STATUS_CHARS + r"])\]")
LEGEND = re.compile(r"^-\s*\*\*\[([" + STATUS_CHARS + r"])\]\*\*\s*[—-]?\s*(.{3,110})")

# R3: формулировки, отозванные проходом согласования 10.09.2026.
RETRACTED = {
    "en": [
        "every unitary irreducible representation of a finite abelian group is isomorphic to the regular",
        "the unique $G_2$-covariant one",
        "**complete** $G_2$-covariance",
        "250+ formal results",
    ],
    "ru": [
        "всякое унитарное неприводимое представление конечной абелевой группы изоморфно регулярному",
        "единственного $G_2$-ковариантного",
        "**полная** $G_2$-ковариантность",
        "250+ формальных результатов",
    ],
}
RETRACTION_MARK = re.compile(
    r"retract|отозв|earlier draft|earlier version|прежн|ранее|errata|эррат|over-claim|завышени", re.I
)


def norm(ch):
    return CYR2LAT.get(ch, ch)


SECTION = re.compile(r"^#{2,3}\s+(?!~~)(.*)$")


def section_status(heading):
    """Статус раздела — только если заголовок называет РОВНО одну букву.

    «## Level 1: Impeccably Strict Theorems [T]» и «### Level [T]: Universal
    Property» наследуются; «## Postulates [P] and Definitions [D]» — нет:
    две буквы в заголовке не определяют статус строки.
    """
    letters = status_letters(heading)
    return next(iter(letters)) if len(letters) == 1 else None


def registry_rows(root, row=ROW):
    """Живые (не зачёркнутые) строки реестра по номеру, вместе со статусом СЕКЦИИ.

    Реестр кодирует статус двумя способами: буквой в самой строке и —
    для таблиц-указателей (`| 1 | Fano channel preserves coherences | … |`) —
    заголовком раздела («## Level 1: Impeccably Strict Theorems [T]»).
    Прибор, читавший только первый способ, объявлял 145 строк «без статуса»,
    хотя статус у них есть, просто вынесен на раздел. Это была ошибка прибора,
    а не долг корпуса, и она правится здесь.
    """
    text = (root / "reference/status-registry.md").read_text(encoding="utf-8")
    out, section = {}, None
    for line in text.split("\n"):
        head = SECTION.match(line.rstrip())
        if head:
            section = section_status(head.group(1))
            continue
        m = row.match(line)
        if not m or line.count("~~") >= 2:
            continue
        tid = m.group(1)
        if row is ROW:
            tid = tid if tid.startswith("T-") else "T-" + tid
        else:
            tid = xkey(tid)
        out.setdefault(tid, []).append((m.group(2), section))
    return out


def classify(root, row=ROW):
    """Каждому номеру — вид свидетельства о статусе.

    explicit  — статус читается машиной однозначно (одна живая строка, один статус);
    collision — ДВЕ СОДЕРЖАТЕЛЬНЫЕ строки с разными статусами: номер неоднозначен,
                и разрешается это только перенумерацией (дело автора);
    companion — вторая строка лежит в таблице БЕЗ статуса (внешняя опора, граф
                зависимостей): номер назван дважды, но не двусмыслен — реестр сам
                называет такие строки «companion» и считает их не долгом;
    implied   — статус выражен прозой («raised from [X]», «H3 [H] → CLOSED»), не буквой;
    absent    — буквы статуса нет вовсе.

    Только `explicit` годится в канон для правила R1. Остальные три — ДОЛГ:
    у результата нет машиночитаемой канонической записи, и ровно поэтому
    пропагация статусов в корпусе делается руками и разъезжается.
    """
    kinds, statuses = {}, {}
    for tid, bodies in registry_rows(root, row).items():
        per_row = []
        implied = False
        for body, section in bodies:
            if RAISED.search(body) or CLOSED.search(body):
                implied = True
            stripped = RETRACTED_SUB.sub(" ", CLOSED.sub(" ", RAISED.sub(" ", body)))
            found = status_letters(stripped)
            if not found and section:
                found = {section}        # статус унаследован от заголовка раздела
                implied = False
            if found:
                per_row.append(found)
        union = set().union(*per_row) if per_row else set()
        if not union:
            kinds[tid] = "implied" if implied else "absent"
        elif len(bodies) > 1 and (len(per_row) != len(bodies) or any(a != b for a in per_row for b in per_row)):
            # «Спутник» — строка из таблицы без собственного статуса (внешняя
            # опора, граф зависимостей). Номер при этом НЕ двусмыслен.
            statused = [s for _, s in bodies if s]
            kinds[tid] = "companion" if len(statused) < len(bodies) and len(set(statused)) <= 1 else "collision"
            statuses[tid] = union
        elif implied and not union:
            kinds[tid] = "implied"
        else:
            kinds[tid] = "explicit"
            statuses[tid] = union
    return kinds, statuses


def check_r1x(root, statuses, kinds):
    """R1 для не-T номеров: цитаты `CC-n`/`КК-n`/`Pred n` и носители страницы предсказаний.

    Цитата сверяется, как и у T-номеров, с объединением живых статусов строки.
    На странице предсказаний статус раздела «Prediction N» пишется первым
    носителем (`:::info Prediction [X]` или `**Status:** [X]`); расхождение —
    если ни одна его буква не входит в статусы строки `Pred N` реестра.
    """
    statuses = {t: v for t, v in statuses.items() if kinds.get(t) != "absent"}
    bad, seen_n = [], {"цитат": 0, "носителей": 0}
    for f in sorted(root.rglob("*.md*")):
        if f.name == "status-registry.md":
            continue
        pred, seen = None, False
        for i, line in enumerate(f.read_text(encoding="utf-8").split("\n"), 1):
            head = PRED_HEAD.match(line)
            if head:
                pred, seen = "Pred " + head.group(1), False
            elif line.startswith("#"):
                pred = None
            if pred and not seen and PRED_CARRIER.match(line):
                letters = status_letters(line)
                if letters:
                    seen = True
                    seen_n["носителей"] += pred in statuses
                    if pred in statuses and not (letters & statuses[pred]):
                        bad.append((f, i, pred, "/".join(sorted(letters)), sorted(statuses[pred])))
            if RETRACTION_MARK.search(line):
                continue
            for m in XCITE.finditer(line):
                tid, st = xkey(m.group(1)), norm(m.group(2))
                seen_n["цитат"] += tid in statuses
                if tid in statuses and st not in statuses[tid]:
                    bad.append((f, i, tid, st, sorted(statuses[tid])))
    return bad, seen_n


def check_r1(root, statuses, kinds):
    """Цитата обязана совпасть хотя бы с одной ЖИВОЙ строкой своего номера.

    Раньше прибор пропускал столкнувшиеся номера целиком — и тем прятал
    настоящие расхождения (так шесть цитат «T-80 [T]» стояли при строке
    «[C at T-64]»). Сверка с ОБЪЕДИНЕНИЕМ статусов строк даёт то же, что и
    прежде, для однозначных номеров, и ловит дефект у двусмысленных, не
    требуя выбирать между их строками.
    """
    statuses = {t: v for t, v in statuses.items() if kinds.get(t) != "absent"}
    bad = []
    for f in sorted(root.rglob("*.md*")):
        if f.name == "status-registry.md":
            continue
        for i, line in enumerate(f.read_text(encoding="utf-8").split("\n"), 1):
            if RETRACTION_MARK.search(line):
                continue
            for m in CITE.finditer(line):
                tid, st = m.group(1), norm(m.group(2))
                if tid in statuses and st not in statuses[tid]:
                    bad.append((f, i, tid, st, sorted(statuses[tid])))
    return bad


LEGEND_HEAD = re.compile(r"\bstatus\b|маркер|система маркировки|статус", re.I)

# Канонические синонимы значения каждой буквы. Прибор не сличает формулировки
# дословно (легенды бывают пояснительными) — он проверяет, что значение буквы на
# странице вообще принадлежит её смысловому полю, а не полю другой буквы.
SYNONYMS = {
    "T": r"теорем|доказ|theorem|proved|proven|rigorous",
    "C": r"услов|conditional",
    "H": r"гипотез|hypothes",
    "P": r"постулат|postulate",
    "D": r"определ|definition|конвенц|convention|соглашен|assigned",
    "I": r"интерпрет|interpretation|семантич|semantic|философ|philosoph",
}


def check_r2(root):
    """Легенда страницы против легенды реестра — по ключевому слову значения.

    Легендой считается только список букв, идущий сразу за заголовком легенды:
    иначе прибор ловит обычные перечни результатов, помеченных теми же буквами.
    """
    reg = {}
    reg_lines = (root / "reference/status-registry.md").read_text(encoding="utf-8").split("\n")
    for i, line in enumerate(reg_lines, 1):
        if not any(LEGEND_HEAD.search(x) for x in reg_lines[max(0, i - 7):i]):
            continue
        m = LEGEND.match(line.strip())
        if m and norm(m.group(1)) not in reg:
            reg[norm(m.group(1))] = m.group(2).replace("*", " ").strip().lower()
    bad = []
    for f in sorted(root.rglob("*.md*")):
        if f.name == "status-registry.md":
            continue
        lines = f.read_text(encoding="utf-8").split("\n")
        for i, line in enumerate(lines, 1):
            if not any(LEGEND_HEAD.search(x) for x in lines[max(0, i - 7):i]):
                continue
            m = LEGEND.match(line.strip())
            if not m:
                continue
            ch, meaning = norm(m.group(1)), m.group(2).replace("*", " ").strip().lower()
            if ch in SYNONYMS and not re.search(SYNONYMS[ch], meaning, re.I):
                bad.append((f, i, ch, meaning, reg.get(ch, "?")))
    return bad


def check_r3(root, loc):
    bad = []
    for f in sorted(root.rglob("*.md*")):
        for i, line in enumerate(f.read_text(encoding="utf-8").split("\n"), 1):
            if RETRACTION_MARK.search(line):
                continue
            for phrase in RETRACTED[loc]:
                if phrase in line:
                    bad.append((f, i, phrase))
    return bad


DEPS = re.compile(r"^\*\*(?:Dependencies|Зависимости)\*{0,2}:?\*{0,2}\s*(.*)$")
WEAKER = {"C", "D", "H", "P", "I"}
CARRIER = re.compile(r"^(?:#{2,6}\s|:::\w+\s|\*\*(?:Theorem|Теорема|Claim|Утверждение|Corollary|Следствие|Lemma|Лемма))")


DEP_REF = re.compile(r"\b(T-\d+(?:\.\d+)?[a-z]?)\b")


def check_r6(root, statuses, kinds):
    """[T] не смеет опираться на более слабую опору, не унаследовав её статус.

    Правило аудита 10.09.2026: метки [C]/[D]/[I]/[P] обязаны распространяться по
    зависимостям. Прибор читает строку «**Зависимости:** …», берёт статус
    ближайшего носителя выше (заголовок, врезка или жирная преамбула теоремы) и
    сверяет: если носитель объявлен [T], а среди опор есть слабее — это дефект.

    Слабость опоры читается ДВАЖДЫ: по букве, написанной в самой строке, и по
    РЕЕСТРУ (номер, у которого все живые статусы слабее [T]). Прежде прибор знал
    только букву в строке и искал носителя не дальше 60 строк — и 25.09.2026 не
    видел двух опор: T-120 [T] стоял на T-118 [C] (строка зависимостей в 90 строках
    от шапки), теорема на T-190 [C] — в 95 строках. Теперь носитель ищется до
    ближайшего заголовка без окна.
    """
    bad = []
    for f in sorted(root.rglob("*.md*")):
        lines = f.read_text(encoding="utf-8").split("\n")
        for i, line in enumerate(lines):
            m = DEPS.match(line.strip())
            if not m:
                continue
            dep = {s for _, s in re.findall(
                r"(T-\d+[a-z′']?)\]?(?:\([^)\s]*\))?\s*\**\[([" + STATUS_CHARS + r"])\]", m.group(1))}
            dep = {norm(x) for x in dep}
            weak = (dep & WEAKER) - WEAKER_OK
            for tid in set(DEP_REF.findall(m.group(1))):
                st = statuses.get(tid)
                if st and kinds.get(tid) == "explicit" and "T" not in st and (st & WEAKER):
                    weak |= st & WEAKER
            if not weak:
                continue
            own, carrier = None, None
            for j in range(i - 1, -1, -1):
                if CARRIER.match(lines[j]):
                    letters = status_letters(lines[j])
                    if letters:
                        own, carrier = letters, lines[j]
                        break
                    if lines[j].startswith("#"):
                        break
            if own == {"T"} and not CONDITIONED.search(carrier):
                bad.append((f, i + 1, sorted(weak), sorted(dep)))
    return bad


def check_r4(root, row=ROW):
    """Строки реестра со статусом [C] обязаны называть допущение."""
    names = re.compile(r"\[[CС]\s*(at|under|при|given|если)|условн|conditional|assumption|допущени|гипотез", re.I)
    bad = []
    text = (root / "reference/status-registry.md").read_text(encoding="utf-8").split("\n")
    for i, line in enumerate(text, 1):
        m = row.match(line)
        if not m or line.count("~~") >= 2:
            continue
        body = RAISED.sub(" ", m.group(2))
        if re.search(r"\*{0,2}\[[CС]\]", body) and not names.search(body):
            bad.append((i, m.group(1), body[:90]))
    return bad


# ---------------------------------------------------------------------------
# R7  ОПОРА НА ОТОЗВАННОЕ (26.09.2026).
#
# R1 ловит ЦИТАТУ со статусом («T-178 [T]» при реестре [✗]). Но опора редко
# пишется с буквой: «by T-48a», «из T-178», «(T-179)», «[T, T-175a]» — статуса
# нет, и R1 молчит, а читатель берёт отозванный результат за действующий.
# R7 читает реестр, составляет список ЦЕЛИКОМ отозванных номеров и ищет их
# в контексте опоры без пометки отзыва в пределах абзаца, врезки или раздела.
#
# Целиком отозванный номер — тот, у которого ВСЕ живые строки после снятия
# исторических контекстов («corrected from [T]», «previously … [✗]», «[T] → [✗]»
# до стрелки) и цитат ЧУЖИХ номеров («Replaced by T-58′ [T]») несут только [✗].
# Частично отозванные (снятая под-часть: «Old … formula retracted [✗]») сюда не
# входят — их опора законна. Ещё три семейства: номера из списков
# «*Retracted [✗]:* Lemma T-170'.1 …, T-170' as a theorem …», строки реестра
# «#n» (раздел «Level 4 … [✗]» и зачёркнутые строки «Retracted [✗]») и
# утверждения X1–X4 раздела «Retracted Statements [✗]». Номера C-n не входят
# (буквы с цифрой в корпусе многозначны, как и для R1x: C2 — и отозванная строка
# условий, и шаг вывода); целиком отозванных CC/КК в реестре на 26.09.2026 нет.
# ---------------------------------------------------------------------------
RID = r"[TТ]-\d+[a-z]?(?:['′]{1,2})?(?:\.\d+)?"
HIST = re.compile(
    r"(?:previously|earlier|formerly|was|ранее|прежде|было|бывш\w*)\s[^|;\]]{0,40}?\[✗\]"
    r"|\[[" + STATUS_CHARS + r"]\]\*{0,2}~{0,2}\s*(?:→|->)\s*", re.I)
FOREIGN_CITE = re.compile(r"(?:" + RID + r"|\b[CXН]\d+['′]?)\]?(?:\([^)\s]*\))?\*{0,2}\s*\*{0,2}\[[" + STATUS_CHARS + r"][^\]]*\]")
RETR_LIST = re.compile(r"\*(?:Retracted|Отозван[оаы]?) \[✗\]:\*(.*?)(?:\*(?:Status history|История статуса)|\s\|\s|$)")
RETR_SECTION = re.compile(r"^##\s+.*\[✗\]\s*$")
ROW_RETRACTED = re.compile(r"(?:Retracted|Отозван[аоы]?|Ретрактирован[аоы]?)\*{0,2}\s*\[✗\]", re.I)


REPLACED_BY = re.compile(r"(?:Replaced by|Replacement|Заменена?|Замена)\*{0,2}:?\s*\*{0,2}" + RID
                         + r"['′]?\*{0,2}\s*\*{0,2}\[[" + STATUS_CHARS + r"]\]", re.I)


#: Явный переход САМОЙ строки в [✗]: «[T] → [✗]», «corrected from [T] to [✗]».
#: «the former statement is corrected from [T] to [✗]» — переформулировка, не отзыв.
TO_RETRACTED = re.compile(
    r"(?<!former statement is )(?<!former statement )(?<!прежняя формулировка )(?<!прежнее утверждение )"
    r"(?:\[[TCHТСГ]\]\*{0,2}\s*(?:→|->)\s*\*{0,2}|(?:corrected|исправлен[аоы]?)\s+(?:from|с)\s+\[[TCHТСГ]\]\s+(?:to|на)\s+)\[✗\]")


def _row_letters(tid, body, section):
    if TO_RETRACTED.search(body):
        return {"✗"}
    body = RAISED.sub(" ", body)
    body = HIST.sub(" ", body)
    body = RETRACTED_SUB.sub(" ", body)          # снятая под-часть — не статус строки
    body = REPLACED_BY.sub(" ", body)            # «Replaced by T-58′ [T]» — статус замены
    # цитата ЧУЖОГО номера не статус строки; своя редакция («T-201′ [T]») — статус
    body = FOREIGN_CITE.sub(lambda m: m.group(0) if m.group(0).startswith(tid) else " ", body)
    found = status_letters(body)
    return found or ({section} if section else set())


def retracted_ids(root):
    """Номера, отозванные ЦЕЛИКОМ, с видом записи: {ключ: вид}."""
    text = (root / "reference/status-registry.md").read_text(encoding="utf-8")
    out = {}
    for tid, bodies in registry_rows(root).items():
        letters = [_row_letters(tid, b, s) for b, s in bodies]
        if letters and all(l == {"✗"} for l in letters):
            out[tid] = "строка"
    section_retracted = False
    for line in text.split("\n"):
        if line.startswith("## "):
            section_retracted = bool(RETR_SECTION.match(line.strip()))
            continue
        for m in RETR_LIST.finditer(line):
            span = re.sub(r"\([^()]*\)", " ", re.sub(r"\([^()]*\)", " ", m.group(1)))
            for item in re.split(r",\s+|\s+(?:and|и)\s+", span):
                im = re.match(r"\s*(?:the former |прежн\w+ )?(?:Lemma |Лемма |лемма )?(" + RID + r")(?![\w'′.])", item)
                if im:
                    out[im.group(1).replace("Т-", "T-")] = "список отзыва"
        cell = re.match(r"^\|\s*(~~)?(\d+|X\d+)(~~)?\s*\|", line)
        if not cell:
            continue
        num = cell.group(2)
        if num.startswith("X"):
            if section_retracted:
                out[num] = "утверждение"
        elif section_retracted or (cell.group(1) and ROW_RETRACTED.search(line)
                                   and not re.search(r"Raised to|Повышен|Resolved|Решено", line)):
            out["#" + num] = "строка реестра"
    return out


# Опора: слово-связка ПЕРЕД номером, статус без [✗] ПОСЛЕ него, глагол-вывод
# после него, скобочная ссылка «(T-178)» / «(by T-178)» и форма «[T, T-178]».
RELY_BEFORE = re.compile(
    r"(?:\b(?:by|from|via|using|uses|use of|per|according to|by virtue of|because of|thanks to|follows? from|"
    r"following|based on|rests? on|resting on|relies on|relying on|invoking|invokes|given|with|of|on|upon|in|"
    r"conditional on|depends on|decomposition|construction|equivalence|theorem|lemma)"
    r"|(?<![\w-])(?:по|из|согласно|в силу|благодаря|следует из|через|на основе|опирается на|опираясь на|"
    r"с опорой на|используя|использует|при|при условии|условии|дают|даёт|дает|на|в|от|"
    r"декомпозици\w*|конструкци\w*|эквивалентност\w*|теорем\w*|лемм\w*))"
    r"\s+(?:the\s+|теорем[аеыуой]+\s+|леммы?\s+|lemma\s+|theorem\s+|Theorem\s+|Lemma\s+|\*\*|\[)*$", re.I)
RELY_BRACKET = re.compile(r"\[[TCHТСГ](?:\s+at|\s+при)?,?\s*$|\(\s*(?:see\s+|см\.\s+|cf\.\s+)?$")
RELY_AFTER = re.compile(
    r"^(?:′|')?(?:\]\([^)\s]*\))?\*{0,2}\s*\*{0,2}\[[TCHPDIТСГПОИ][^\]]*\]"
    r"|^(?:\]\([^)\s]*\))?\*{0,2}[^\S\n]+(?:gives|yields|implies|shows|proves|guarantees|fixes|establishes|"
    r"даёт|дает|доказывает|показывает|гарантирует|фиксирует|обеспечивает|устанавливает)\b", re.I)
RETR_NEAR = re.compile(
    r"retract|withdraw|отозв|ретракт|\[✗\]|refuted|опроверг|снят[аоы]? \d{4}|"
    r"former (?:text|box|statement|claim|version|reading|row|derivation|proof)|"
    r"прежн\w* (?:текст|врезк|формулиров|утвержд|редакц|чтени|строк|вывод|доказ)|"
    r"over-claim|завышен|~~", re.I)
#: Пометка в начале абзаца покрывает абзац, только если называет ОТЗЫВ, а не
#: любую правку: «**Status errata 2026-09-10: [T] → [D].**» о своём результате не
#: помечает чужой номер, опору на который абзац называет ниже.
RETR_LEAD = re.compile(r"retract|withdraw|отозв|ретракт|\[✗\]|~~", re.I)
#: Объявление «ниже — отозванное»: «*Retracted [✗]:* the earlier derivation below»,
#: «The text below is the former derivation», «Текст ниже — прежний вывод». Покрывает
#: всё до конца врезки (если объявлено внутри неё) или до следующего заголовка.
#: «(see below)» — ссылка на одно место, а не объявление, и не покрывает.
RETR_BELOW = re.compile(
    r"(?:retract\w*|withdrawn|отозван\w*|ретракт\w*|former|earlier|прежн\w*|as a record|как запись)"
    r"[^.\n]{0,100}?(?<!see )(?<!see the )(?<!см\. )\b(?:below|ниже)\b"
    r"|\b(?:below|ниже)\b[^.\n]{0,40}?\b(?:is|are|—|-)\s+(?:the\s+)?(?:former|прежн\w*|retracted|отозван\w*)", re.I)
FENCE = re.compile(r"^\s*(```|~~~)")


def _blocks(lines):
    """Для каждой строки — её абзац, шапка её врезки и её заголовок.

    Окно пометки — абзац (подряд идущие непустые строки; строка таблицы — сама
    себе абзац), ШАПКА врезки («:::note Earlier statement (T-177, retracted [✗])»)
    и ближайший заголовок. Не вся врезка: в длинной врезке «(T-177, retracted)»
    в одном абзаце прощало опору «justified upstream in T-48a» в другом.
    """
    n = len(lines)
    para, head, adm = [None] * n, [None] * n, [None] * n
    cur_head, cur_adm = None, None
    for i, line in enumerate(lines):
        s = line.strip()
        if s.startswith("#"):
            cur_head = i
        if re.match(r"^:::\w", s):
            cur_adm = i
        elif s == ":::":
            cur_adm = None
        head[i], adm[i] = cur_head, cur_adm
    i = 0
    while i < n:
        s = lines[i].strip()
        if not s or s.startswith(":::"):
            i += 1
            continue
        if s.startswith("|"):
            para[i] = (i, i)
            i += 1
            continue
        j = i
        while j + 1 < n and lines[j + 1].strip() and not lines[j + 1].strip().startswith(("|", ":::", "#")):
            j += 1
        for k in range(i, j + 1):
            para[k] = (i, j)
        i = j + 1
    return para, head, adm


SENT_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-ZА-ЯЁ*_(\[\"«])")


def _mark_scope(lines, para, head, adm, i, m):
    """Где пометка отзыва засчитывается упоминанию.

    Предложение упоминания, начало его абзаца (формы «**Step 1 — [✗] retracted.**»,
    «*Retracted 2026-09-25 with T-48a …*»), шапка врезки и заголовок раздела.
    Зачёркнутый текст («~~… (T-48a [T])~~») помечен самим зачёркиванием.
    Прежде окном был весь абзац — и «Errata» о другом номере в начале длинного
    абзаца прощала фразу «the bridge it leans on, Morita equivalence T-58, is
    itself [C]» в его конце (operationalization, 26.09.2026).
    """
    line = lines[i]
    if line[:m.start()].count("~~") % 2 == 1:
        return "~~"
    starts = [0] + [x.end() for x in SENT_SPLIT.finditer(line)] + [len(line)]
    k = max(j for j, x in enumerate(starts) if x <= m.start())
    # предложение упоминания и по одному соседу: «… (T-48a, T-82). *Corrected:* T-48a is retracted»
    scope = line[starts[max(0, k - 1)]:starts[min(len(starts) - 1, k + 2)]]
    a, _b = para[i] or (i, i)
    lead = lines[a][:120]
    if RETR_LEAD.search(lead):
        scope += "\n" + lead
    if a < i:
        scope += "\n" + lines[i - 1][-200:]
    for k in (head[i], adm[i]):
        if k is not None:
            scope += "\n" + lines[k]
    # объявление «ниже — отозванное» выше по той же врезке или разделу
    top = adm[i] if adm[i] is not None else head[i]
    if top is not None and any(RETR_BELOW.search(lines[j]) for j in range(top, i)):
        scope += "\n[✗] (объявлено выше: ниже — отозванное)"
    return scope


def check_r7(root, retracted, excused=None, mentions=None):
    """Опора на целиком отозванный номер без пометки отзыва поблизости."""
    t_ids = sorted((k for k in retracted if k.startswith("T-")), key=len, reverse=True)
    rows = [k[1:] for k in retracted if k.startswith("#")]
    xs = [k for k in retracted if k.startswith("X")]
    alts = [re.escape(t).replace("T\\-", "[TТ]-").replace("'", "['′]").replace("′", "['′]") for t in t_ids]
    pat = []
    if alts:
        pat.append(r"(?<![\w-])(" + "|".join(alts) + r")(?![\w′'.]|\.\d)")
    if rows:
        pat.append(r"(?:(?<![\w#])#|\bNo\.?\s?|№\s?)(" + "|".join(rows) + r")(?![\w-])")
    if xs:
        pat.append(r"(?<![\w$\\_{^])(" + "|".join(xs) + r")(?![\w'′])")
    ID = re.compile("|".join(pat))
    bad, seen = [], {"упоминаний": 0, "опор": 0, "файлов": 0}
    for f in sorted(root.rglob("*.md*")):
        seen["файлов"] += 1
        lines = f.read_text(encoding="utf-8").split("\n")
        para, head, adm = _blocks(lines)
        in_fence = False
        for i, line in enumerate(lines):
            if FENCE.match(line):
                in_fence = not in_fence
                continue
            if in_fence or line.lstrip().startswith("#"):
                continue
            for m in ID.finditer(line):
                seen["упоминаний"] += 1
                if mentions is not None:
                    mentions.append((f, i + 1, line.strip()[:160]))
                before, after = line[max(0, m.start() - 60):m.start()], line[m.end():m.end() + 80]
                if not (RELY_BEFORE.search(before) or RELY_BRACKET.search(before) or RELY_AFTER.search(after)):
                    continue
                seen["опор"] += 1
                scope = _mark_scope(lines, para, head, adm, i, m)
                if RETR_NEAR.search(scope):
                    if excused is not None:
                        excused.append((f, i + 1, line.strip()[:200], RETR_NEAR.search(scope).group(0)))
                    continue
                tid = next(g for g in m.groups() if g)
                key = tid.replace("Т-", "T-").replace("′", "'")
                if (f, i + 1, key) not in {(b[0], b[1], b[2]) for b in bad}:
                    bad.append((f, i + 1, key, line.strip()[:160]))
    return bad, seen


def main():
    fail = False
    files_seen = 0
    for loc, (root, _letter) in LOCALES.items():
        kinds, statuses = classify(root)
        r1 = check_r1(root, statuses, kinds)
        r2 = check_r2(root)
        r3 = check_r3(root, loc)
        r4 = check_r4(root)
        r6 = check_r6(root, statuses, kinds)
        tally = {k: sum(1 for v in kinds.values() if v == k)
                 for k in ("explicit", "collision", "companion", "implied", "absent")}
        debt = tally["collision"] + tally["implied"] + tally["absent"]
        print(f"[{loc}] реестр: номеров {len(kinds)} — машиночитаемых {tally['explicit'] + tally['companion']}, "
              f"долг {debt} (двусмысленных номеров {tally['collision']}, прозой {tally['implied']}, "
              f"без буквы {tally['absent']}); спутников {tally['companion']} — не долг")
        if debt > BASE_DEBT[loc]:
            fail = True
            print(f"  R5 ДОЛГ КАНОНИЧЕСКОЙ ЗАПИСИ вырос: {debt} > базы {BASE_DEBT[loc]}")
        print(f"  R1 статус цитаты против реестра: расхождений {len(r1)} (база {BASE_R1[loc]})")
        for f, i, tid, st, reg in r1[:12]:
            print(f"     {f.relative_to(ROOT)}:{i}: {tid} цитирован [{st}], реестр даёт {reg}")
        if len(r1) > BASE_R1[loc]:
            fail = True
        print(f"  R2 легенда страницы против легенды реестра: расхождений {len(r2)}")
        for f, i, ch, m1, m2 in r2:
            print(f"     {f.relative_to(ROOT)}:{i}: [{ch}] — «{m1}» против «{m2}»")
        if r2:
            fail = True
        print(f"  R3 отозванная формулировка вне контекста отзыва: {len(r3)}")
        for f, i, ph in r3:
            print(f"     {f.relative_to(ROOT)}:{i}: «{ph[:70]}»")
        if r3:
            fail = True
        print(f"  R4 строки [C] без названного допущения: {len(r4)} (база {BASE_R4[loc]})")
        if len(r4) > BASE_R4[loc]:
            fail = True
            for i, tid, body in r4[:8]:
                print(f"     реестр:{i}: {tid} — {body}")
        print(f"  R6 [T] на более слабой опоре: {len(r6)} (база {BASE_R6[loc]})")
        for f, i, weak, dep in r6[:10]:
            print(f"     {f.relative_to(ROOT)}:{i}: опоры {dep}, слабее теоремы: {weak}")
        if len(r6) > BASE_R6[loc]:
            fail = True
        # не-T номера: CC/КК и Pred
        xkinds, xstat = classify(root, XROW)
        xtally = {k: sum(1 for v in xkinds.values() if v == k)
                  for k in ("explicit", "collision", "companion", "implied", "absent")}
        xdebt = xtally["collision"] + xtally["implied"] + xtally["absent"]
        fam = {f: sum(1 for t in xkinds if t.startswith(f)) for f in XFAMILIES}
        print(f"  НЕ-T номера реестра: {len(xkinds)} ("
              + ", ".join(f"{f} {n}" for f, n in fam.items())
              + f") — машиночитаемых {xtally['explicit'] + xtally['companion']}, долг {xdebt} "
              f"(двусмысленных {xtally['collision']}, прозой {xtally['implied']}, без буквы {xtally['absent']}; "
              f"база {BASE_DEBTX[loc]})")
        for t in sorted(t for t, k in xkinds.items() if k in ("collision", "implied", "absent")):
            print(f"     {t}: {xkinds[t]}")
        if xdebt > BASE_DEBTX[loc]:
            fail = True
        r1x, seen_x = check_r1x(root, xstat, xkinds)
        print(f"  R1x статус цитаты CC/Pred против реестра: осмотрено цитат {seen_x['цитат']}, "
              f"носителей предсказаний {seen_x['носителей']}; расхождений {len(r1x)} (база {BASE_R1X[loc]})")
        for f, i, tid, st, reg in r1x:
            print(f"     {f.relative_to(ROOT)}:{i}: {tid} цитирован [{st}], реестр даёт {reg}")
        if len(r1x) > BASE_R1X[loc]:
            fail = True
        r4x = check_r4(root, XROW)
        print(f"  R4x строки [C] CC/Pred без названного допущения: {len(r4x)} (база {BASE_R4X[loc]})")
        for i, tid, body in r4x:
            print(f"     реестр:{i}: {tid} — {body}")
        if len(r4x) > BASE_R4X[loc]:
            fail = True
        # R7: опора на целиком отозванный номер
        retracted = retracted_ids(root)
        r7, seen7 = check_r7(root, retracted)
        fam7 = {"строк реестра T": 0, "списков отзыва": 0, "строк #n": 0, "утверждений X": 0}
        for kind in retracted.values():
            fam7[{"строка": "строк реестра T", "список отзыва": "списков отзыва",
                  "строка реестра": "строк #n", "утверждение": "утверждений X"}[kind]] += 1
        print(f"  R7 опора на отозванное [✗] без пометки: отозванных номеров {len(retracted)} ("
              + ", ".join(f"{k} {v}" for k, v in fam7.items())
              + f"); осмотрено файлов {seen7['файлов']}, упоминаний {seen7['упоминаний']}, "
              f"из них в контексте опоры {seen7['опор']}; расхождений {len(r7)} (база {BASE_R7[loc]})")
        for f, i, tid, text in r7[:20]:
            print(f"     {f.relative_to(ROOT)}:{i}: {tid} — {text[:110]}")
        if len(r7) > BASE_R7[loc]:
            fail = True
        files_seen = max(files_seen, seen7["файлов"])
    # охват называется так, как его читает scripts/verify_gate.py
    print(f"файлов: {files_seen} (на локаль; реестр — канон)")
    print("правило: реестр — канон; одна буква — одно значение; отозванное не возвращается")
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main())
