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

ЧТЕНИЕ РЕЕСТРА. Наивный разбор («любая буква в скобках») ЛЖЁТ: строка
«— raised from [H]» называет ПРЕЖНИЙ статус, а не текущий, и прибор объявлял бы
законную цитату [T] расхождением. Отсюда три поправки: контексты повышения
(`raised from`, `повышен с`, `corrected from`) исключаются; зачёркнутые строки
(`~~…~~`) — это ретракции, они не канон; несколько строк с одним номером
(63 таких пары, реестр их объявляет) дают ОБЪЕДИНЕНИЕ допустимых статусов.

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

# ХРАПОВИК: база расхождений на 10.09.2026 (после прохода согласования).
BASE_R1 = {"en": 0, "ru": 0}
BASE_R4 = {"en": 44, "ru": 49}
# R5: у скольких номеров нет машиночитаемой канонической записи статуса.
# Это и есть механизмический долг, названный аудитом 10.09.2026: пока он не нуль,
# пропагация статусов держится на руках. Расти ему нельзя.
BASE_DEBT = {"en": 30, "ru": 30}
# R6: сколько теорем [T] опираются на более слабую опору, не унаследовав её статус.
BASE_R6 = {"en": 0, "ru": 0}

CYR2LAT = {"Т": "T", "С": "C", "Г": "H", "П": "P", "О": "D", "И": "I"}
WEAKER_OK = {"✗"}   # ретракция — не «более слабая опора», а снятие
STATUS_CHARS = "TCHPDIТСГПОИ✗"
RAISED = re.compile(
    r"(raised from|corrected from|повышен[аоы]? с|исправлен[аоы]? с|поднят[аоы]? с)\s*\*{0,2}\[?[" + STATUS_CHARS + r"]\]?",
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
CITE = re.compile(r"\b(T-\d+(?:\.\d+)?[a-z]?)\s*\*{0,2}\[([" + STATUS_CHARS + r"])\]")
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


def registry_rows(root):
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
        m = ROW.match(line)
        if not m or line.count("~~") >= 2:
            continue
        tid = m.group(1)
        tid = tid if tid.startswith("T-") else "T-" + tid
        out.setdefault(tid, []).append((m.group(2), section))
    return out


def classify(root):
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
    for tid, bodies in registry_rows(root).items():
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


def check_r6(root):
    """[T] не смеет опираться на более слабую опору, не унаследовав её статус.

    Правило аудита 10.09.2026: метки [C]/[D]/[I]/[P] обязаны распространяться по
    зависимостям. Прибор читает строку «**Зависимости:** …», берёт статус
    ближайшего носителя выше (заголовок, врезка или жирная преамбула теоремы) и
    сверяет: если носитель объявлен [T], а среди опор есть слабее — это дефект.
    """
    bad = []
    for f in sorted(root.rglob("*.md*")):
        lines = f.read_text(encoding="utf-8").split("\n")
        for i, line in enumerate(lines):
            m = DEPS.match(line.strip())
            if not m:
                continue
            dep = {s for _, s in re.findall(r"(T-\d+[a-z′']?)\s*\**\[([" + STATUS_CHARS + r"])\]", m.group(1))}
            dep = {norm(x) for x in dep}
            weak = (dep & WEAKER) - WEAKER_OK
            if not weak:
                continue
            own = None
            for j in range(i - 1, max(-1, i - 60), -1):
                if CARRIER.match(lines[j]):
                    letters = status_letters(lines[j])
                    if letters:
                        own = letters
                        break
                    if lines[j].startswith("#"):
                        break
            if own == {"T"} and not CONDITIONED.search(lines[j]):
                bad.append((f, i + 1, sorted(weak), sorted(dep)))
    return bad


def check_r4(root):
    """Строки реестра со статусом [C] обязаны называть допущение."""
    names = re.compile(r"\[[CС]\s*(at|under|при|given|если)|условн|conditional|assumption|допущени|гипотез", re.I)
    bad = []
    text = (root / "reference/status-registry.md").read_text(encoding="utf-8").split("\n")
    for i, line in enumerate(text, 1):
        m = ROW.match(line)
        if not m or line.count("~~") >= 2:
            continue
        body = RAISED.sub(" ", m.group(2))
        if re.search(r"\*{0,2}\[[CС]\]", body) and not names.search(body):
            bad.append((i, m.group(1), body[:90]))
    return bad


def main():
    fail = False
    for loc, (root, _letter) in LOCALES.items():
        kinds, statuses = classify(root)
        r1 = check_r1(root, statuses, kinds)
        r2 = check_r2(root)
        r3 = check_r3(root, loc)
        r4 = check_r4(root)
        r6 = check_r6(root)
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
    print("правило: реестр — канон; одна буква — одно значение; отозванное не возвращается")
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main())
