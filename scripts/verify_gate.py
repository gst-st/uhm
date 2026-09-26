#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
verify_gate.py — единая дверь корпуса holon: все приборы разом, один код возврата.

Приборов было три, и запускались они порознь: проверить корпус целиком значило
помнить три команды, и ничто не требовало запустить все три. Половинчатая проверка
выглядит как проверка. Этот файл запускает всё и падает, если падает хоть что-нибудь.

Правило 0 дисциплины проверки (карта покрытия math-foundations §7.5b), применённое
к аппарату целиком, а не к отдельному прибору.
"""
import re
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
# Приборы делятся надвое по тому, ЧТО они читают. Четыре первых читают ИСХОДНИК;
# пятый — СОБРАННУЮ СТРАНИЦУ, то есть то, что видит читатель, и живёт он рядом с
# сайтом (website/scripts/), ибо без сборки бессмыслен. Между исходником и
# читателем стои́т разметка, и она умеет молча съедать смысл: сборка при этом
# рапортует об успехе.
TOOLS = ["check_theorem_refs.py", "check_status_markers.py",
         "check_mixed_names.py", "natal_startup_verify.py"]
# Шестой — страж согласованности статусов (website/scripts/check_status_consistency.py):
# читает ИСХОДНИК обеих локалей против реестра и сборки не требует; живёт рядом с
# сайтом по месту реестра. До 26.09.2026 вентиль его не звал, и его храповики
# (R1…R7, включая опору на отозванное) держались только ручным запуском.
SITE_TOOLS = [Path("website") / "scripts" / "render_lint.py",
              Path("website") / "scripts" / "check_status_consistency.py"]


# ОХВАТ. Прибор, не назвавший, сколько файлов он прочитал, объявляет чистым
# непрочитанное: сузься его обход на каталог — и «все приборы чисты» будет
# значить чистоту на РАЗНЫХ кусках. Здесь, в отличие от корпуса math-foundations,
# приборы читают РАЗНЫЕ деревья по существу (перевод, сайт, онтология), и потому
# равенства охватов требовать нельзя — требуется, чтобы каждый его НАЗЫВАЛ.
# Знаменатель бывает ДВУХ валют. Линтер читает корпус и называет ФАЙЛЫ;
# вычислительный свидетель корпуса не читает вовсе и называет ПРОВЕРКИ. Прежде
# вентиль знал одну валюту и писал свидетелю «охват не назван» при честном
# «TOTAL: 4/4 PASS» — правило требует НАЗВАТЬ знаменатель, а не назвать файлы.
def scope_of(out: str):
    m = (re.search(r"^файлов:? (\d+)", out or "", re.M)
         or re.search(r"просмотрено файлов:?\s+(\d+)", out or ""))
    if m:
        return int(m.group(1)), "файлов"
    m = (re.search(r"TOTAL:\s*\d+/(\d+)\s*PASS", out or "")
         or re.search(r"^проверок:? (\d+)", out or "", re.M))
    if m:
        return int(m.group(1)), "проверок"
    return None


#: приборы, которые корпус НЕ читают: это вычислительные свидетели, и охвата
#: файлов у них нет по существу, а не по недосмотру
NO_SCOPE = {"natal_startup_verify.py"}


def main() -> int:
    failed = []
    scope = {}
    unnamed = []
    for name in TOOLS:
        p = HERE / name
        if not p.exists():
            print(f"  {name:28}  НЕТ ФАЙЛА — это дефект, а не пропуск")
            failed.append(name)
            continue
        t0 = time.time()
        r = subprocess.run([sys.executable, str(p)], capture_output=True, text=True)
        n = scope_of(r.stdout)
        print(f"  {name:28}  EXIT={r.returncode}  {time.time() - t0:5.1f} с"
              + (f"  {n[1]} {n[0]}" if n is not None else "  охват не назван"))
        if n is None and name not in NO_SCOPE: unnamed.append(name)
        elif n is not None: scope[name] = f"{n[1]} {n[0]}"
        if r.returncode: failed.append(name)
    for rel in SITE_TOOLS:
        p = HERE.parent / rel
        if not p.exists():
            print(f"  {p.name:28}  НЕТ ФАЙЛА — это дефект, а не пропуск")
            failed.append(p.name)
            continue
        t0 = time.time()
        r = subprocess.run([sys.executable, str(p)], capture_output=True, text=True,
                           cwd=str(p.parent.parent))
        n = scope_of(r.stdout)
        print(f"  {p.name:28}  EXIT={r.returncode}  {time.time() - t0:5.1f} с"
              + (f"  {n[1]} {n[0]}" if n is not None else "  охват не назван"))
        if n is None and p.name not in NO_SCOPE: unnamed.append(p.name)
        elif n is not None: scope[p.name] = f"{n[1]} {n[0]}"
        if r.returncode:
            failed.append(p.name)
            print(r.stdout[-3000:])

    if scope:
        print("\nохват приборов: " + "; ".join(f"{k} — {v}" for k, v in scope.items()))
    if unnamed:
        print("ОХВАТ НЕ НАЗВАН: " + ", ".join(unnamed))
        print("  правило: прибор, молчащий об охвате, объявляет чистым непрочитанное")

    print()
    if failed:
        print(f"ВЕНТИЛЬ ЗАКРЫТ: упало приборов {len(failed)} из {len(TOOLS) + len(SITE_TOOLS)} — "
              + ", ".join(failed))
        return 1
    print(f"ВЕНТИЛЬ ОТКРЫТ: все {len(TOOLS) + len(SITE_TOOLS)} приборов чисты")
    return 0


if __name__ == "__main__":
    sys.exit(main())
