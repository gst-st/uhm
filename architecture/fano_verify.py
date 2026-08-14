import re, glob, math, itertools, collections
NUM2AX = {1:'A',2:'S',3:'D',4:'L',5:'E',6:'U',7:'O'}   # канон Фано
LINES_N = [sorted(((q-1+k)%7)+1 for q in (1,2,4)) for k in range(7)]
LINES_L = {frozenset(NUM2AX[n] for n in tri) for tri in LINES_N}
SECTORS = {frozenset('ASD'), frozenset('LEU')}
# BIBD(7,3,1)
pairs = collections.Counter()
for tri in LINES_N:
    for a, b in itertools.combinations(tri, 2):
        pairs[frozenset((a, b))] += 1
r = collections.Counter()
for tri in LINES_N:
    for x in tri: r[x] += 1
assert len(pairs) == 21 and set(pairs.values()) == {1}, "λ=1 broken"
assert set(r.values()) == {3}, "r=3 broken"
print(f"[Т] BIBD(7,3,1) OK: 21 пара λ=1, r=3; прямые буквами: "
      f"{sorted(''.join(sorted(s)) for s in LINES_L)}")
# фазы Фибоначчи по канон-номерам: F_k mod 7
F = {k: [1,1,2,3,5,8,13][k-1] % 7 for k in range(1,8)}
gap = lambda a, b: abs(math.sin(2*math.pi*(F[a]-F[b])/7))
cluster = sorted(NUM2AX[k] for k in F if F[k] == 1)
print(f"[Т] фазовый кластер (F_k=1): {{{','.join(cluster)}}}")
# средние Gap по прямым (канон): сверка с напечатанными
printed = {(1,2,4):0.650,(2,3,5):0.550,(3,4,6):0.846,(4,5,7):0.730,
           (5,6,1):0.289,(6,7,2):0.650,(7,1,3):0.730}
for tri in LINES_N:
    m = sum(gap(a,b) for a,b in itertools.combinations(tri,2))/3
    key = None
    for k in printed:
        if sorted(k) == tri: key = k
    ok = abs(m - printed[key]) < 0.0006
    print(f"  прямая {key} = {{{','.join(NUM2AX[n] for n in key)}}}: "
          f"движковый Gap={m:.3f} vs печать {printed[key]} "
          f"{'OK' if ok else '!!! РАСХОЖДЕНИЕ'}")
mean_all = sum(gap(a,b) for a,b in itertools.combinations(range(1,8),2))/21
print(f"  средний Gap по 21 паре: {mean_all:.5f} (печать 0.63509)")
# скан корпуса: все раскрытия {n,n,n}={буквы} и заявления прямых
bad = []
pat_num = re.compile(r"\\\{(\d),(\d),(\d)\\\}\s*=\s*\\\{([A-U,\s]+)\\\}")
pat_line = re.compile(
    r"(?:Fano line|прямая Фано|прямой Фано|линия Фано|Фано-лини[яию])"
    r"[^.]{0,60}?\$?\\?\{([ASDLEOU])[,\s]+([ASDLEOU])[,\s]+([ASDLEOU])\\?\}",
    re.I)
# СПИСОК прямых: фраза «семь прямых Фано» и далее перечисление троек.
# Одиночная pat_line ловила только ПЕРВУЮ тройку и спотыкалась о перенос
# строки — так семь неканоничных прямых в holarch §5 прошли мимо (07.08).
pat_list_head = re.compile(
    r"(?:seven Fano lines|Fano lines are|семь прямых Фано|"
    r"прямые Фано(?:\s+суть)?|Фано-прямые)", re.I)
pat_trio = re.compile(
    r"\\?\{\s*([ASDLEOU])\s*,\s*([ASDLEOU])\s*,\s*([ASDLEOU])\s*\\?\}")
import os
HERE = os.path.dirname(os.path.abspath(__file__))
roots = [os.path.join(HERE, "..", "website", "docs"),
         os.path.join(HERE, "..", "website", "i18n")]
# Утверждение «эта тройка — прямая» СНИМАЕТСЯ, если рядом отрицание
# или если глагол говорит о ПЕРЕСЕЧЕНИИ, а не о принадлежности.
NEG = re.compile(r"\b(no|No|NO|nor|neither|not)\b|\bне\b|\bни\b", re.U)
XSECT = re.compile(r"meet|intersect|пересека|встреча|касает", re.I)
def scan_text(s, p, bad):
    """Сканирует один текст. Находки пишет в bad; возвращает счётчики."""
    n_num = n_line = n_skip = 0
    for m in pat_num.finditer(s):
        n_num += 1
        tri = sorted(int(x) for x in m.group(1, 2, 3))
        letters = frozenset(re.findall(r"[ASDLEOU]", m.group(4)))
        want = frozenset(NUM2AX[n] for n in tri)
        if letters != want:
            bad.append((p, m.group(0), f"канон: {sorted(want)}"))
    for m in pat_line.finditer(s):
        n_line += 1
        trio = frozenset(m.group(1, 2, 3))
        if trio in LINES_L:
            continue
        frag = m.group(0)
        before = s[max(0, m.start() - 70):m.start()]
        # отрицание перед фразой («no Fano line lies within…», «не лежит»)
        # либо речь о пересечении («lines meeting the 3-sector»)
        if NEG.search(before) or NEG.search(frag) or XSECT.search(frag):
            n_skip += 1
            continue
        tag = "СЕКТОР, не прямая" if trio in SECTORS \
              else "НЕ прямая канона"
        bad.append((p, frag[:90], tag))
    for mh in pat_list_head.finditer(s):
        tail = s[mh.end():mh.end() + 320]
        trios = [frozenset(t.group(1, 2, 3)) for t in pat_trio.finditer(tail)]
        if len(trios) < 3:
            continue
        n_line += len(trios)
        for trio in trios:
            if trio in LINES_L:
                continue
            tag = "СЕКТОР, не прямая" if trio in SECTORS \
                  else "НЕ прямая канона (в списке прямых)"
            bad.append((p, mh.group(0) + " … " + "".join(sorted(trio)), tag))
    return n_num, n_line, n_skip


def _probe(text, name):
    found = []
    scan_text(text, "<canary:" + name + ">", found)
    return bool(found)


# ---------------------------------------------------------------------------
# НЕГАТИВНЫЙ КОНТРОЛЬ. Урок 07.08: верификатор печатал «нарушений нет», пока на
# публичной странице стояли четыре неканоничные прямые. «Зелено» ничего не
# значит, пока не доказано, что прибор ловит заведомо неверный вход.
# ---------------------------------------------------------------------------
CANARIES = [
    ("сектор как прямая",  r"The Fano line $\{L,E,U\}$ carries the spine."),
    ("сектор как прямая (ru)", r"Прямая Фано $\{A,S,D\}$ несёт хребет."),
    ("неканоничная тройка", r"the Fano line $\{D,L,O\}$ is associative"),
    ("список прямых", r"the seven Fano lines are $\{A,S,L\}$, $\{D,L,O\}$, "
                      r"$\{L,E,U\}$, $\{A,E,O\}$, $\{A,D,U\}$, $\{S,D,E\}$, $\{S,O,U\}$"),
    ("раскрытие номеров", r"$\{3,4,6\} = \{D,L,O\}$"),
]
missed = [nm for nm, tx in CANARIES if not _probe(tx, nm)]
if missed:
    print("!!! НЕГАТИВНЫЙ КОНТРОЛЬ ПРОВАЛЕН — прибор НЕ ловит: " + ", ".join(missed))
    print("    Всё, что печатается ниже, ничего не значит, пока это не исправлено.")
    raise SystemExit(2)
print(f"[контроль] прибор поймал все {len(CANARIES)} заведомо неверных входов")

n_num = n_line = n_skip = 0
for root in roots:
    for path in glob.glob(root + "/**/*.md", recursive=True):
        txt = open(path, encoding="utf-8", errors="ignore").read()
        a, b, c = scan_text(txt, path, bad)
        n_num += a; n_line += b; n_skip += c
print(f"скан: раскрытий номера→буквы {n_num}, заявлений прямых {n_line}, снято отрицанием/пересечением {n_skip}")
if bad:
    print(f"!!! НАРУШЕНИЙ: {len(bad)}")
    for p, frag, why in bad[:15]:
        short = p.split("/website/")[-1]
        print(f"  {short}: «{frag}» → {why}")
else:
    print("НАРУШЕНИЙ НЕТ: все раскрытия и заявления прямых каноничны")
