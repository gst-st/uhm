# -*- coding: utf-8 -*-
"""hd_circuits_lab.py — контуры Human Design против структуры колеса, ЧЕСТНО.

HD делит 64 ворот на «контуры» (circuits) — групповую проводку с приписанными
темами: Интеграция (самосохранение), Знание (индивидуальная мутация),
Центрирование, Племенной/Эго (сделки и опека), Коллективная Логика (узор),
Коллективный Абстрактный (опыт). Пятый пункт аудита HD Red спрашивал:
несут ли контуры СТРУКТУРУ, которую наше колесо уже знает под другим именем?

Пререгистрированные вопросы:
  C1. Контуры ↔ ядерные корни. Ядерный корень (исток/голос-О/маятник) —
      функция ровно линий 3-4 [Т]. Согласованы ли 6 контуров (и 3 макро-
      семейства) с тремя корнями сильнее случайного? χ² + перестановочный p.
  C2. Контуры ↔ роды объектов. Наш атлас читает каждые ворота как объект
      (исток/пара/линия Фано/треугольник/голос). Согласованы ли контуры с
      родами? (Если да — «контур» окажется псевдонимом рода объекта.)
  C3. Контуры ↔ голосовой состав. Каждый контур несёт мешок голосов своих
      ворот (через atlas members); отличаются ли мешки контуров сильнее
      случайного? (Проверка «тем» контуров: мутация/сделка/узор.)

Таблица ворота→контур — каноническая (Ра Уру Ху; сверена по публичным
источникам школы, 4+16+2+14+14+14 = 64):
  Интеграция {10,20,34,57} · Знание {1,2,3,8,12,14,22,23,24,28,38,39,43,55,
  60,61} · Центрирование {25,51} · Племя/Эго {6,19,21,26,27,32,37,40,44,45,
  49,50,54,59} · Логика {4,5,7,9,15,16,17,18,31,48,52,58,62,63} ·
  Абстракт {11,13,29,30,33,35,36,41,42,46,47,53,56,64}.

Запуск: python3 architecture/hd_circuits_lab.py
"""
import random
from collections import Counter

KW_BITS = [
    0b111111, 0b000000, 0b010001, 0b100010, 0b010111, 0b111010, 0b000010,
    0b010000, 0b110111, 0b111011, 0b000111, 0b111000, 0b111101, 0b101111,
    0b000100, 0b001000, 0b011001, 0b100110, 0b000011, 0b110000, 0b101001,
    0b100101, 0b100000, 0b000001, 0b111001, 0b100111, 0b100001, 0b011110,
    0b010010, 0b101101, 0b011100, 0b001110, 0b111100, 0b001111, 0b101000,
    0b000101, 0b110101, 0b101011, 0b010100, 0b001010, 0b100011, 0b110001,
    0b011111, 0b111110, 0b011000, 0b000110, 0b011010, 0b010110, 0b011101,
    0b101110, 0b001001, 0b100100, 0b110100, 0b001011, 0b001101, 0b101100,
    0b110110, 0b011011, 0b110010, 0b010011, 0b110011, 0b001100, 0b010101,
    0b101010,
]

CIRCUITS = {
    "integration": {10, 20, 34, 57},
    "knowing": {1, 2, 3, 8, 12, 14, 22, 23, 24, 28, 38, 39, 43, 55, 60, 61},
    "centering": {25, 51},
    "tribal": {6, 19, 21, 26, 27, 32, 37, 40, 44, 45, 49, 50, 54, 59},
    "logic": {4, 5, 7, 9, 15, 16, 17, 18, 31, 48, 52, 58, 62, 63},
    "abstract": {11, 13, 29, 30, 33, 35, 36, 41, 42, 46, 47, 53, 56, 64},
}
MACRO = {
    "individual": CIRCUITS["integration"] | CIRCUITS["knowing"]
        | CIRCUITS["centering"],
    "tribal": CIRCUITS["tribal"],
    "collective": CIRCUITS["logic"] | CIRCUITS["abstract"],
}


def nuclear(kw):
    b = KW_BITS[kw - 1]
    line = lambda k: (b >> (k - 1)) & 1
    nb = line(2) | (line(3) << 1) | (line(4) << 2) \
        | (line(3) << 3) | (line(4) << 4) | (line(5) << 5)
    return KW_BITS.index(nb) + 1


def nuclear_root(kw):
    x = kw
    for _ in range(4):
        if x == 1:
            return "voice-O"
        if x == 2:
            return "source"
        if x in (63, 64):
            return "pendulum"
        x = nuclear(x)
    return "pendulum"


def chi2(part_a, part_b):
    """χ²-статистика двух разбиений 1..64 (словари gate->класс)."""
    gates = range(1, 65)
    ca = Counter(part_a[g] for g in gates)
    cb = Counter(part_b[g] for g in gates)
    cab = Counter((part_a[g], part_b[g]) for g in gates)
    x2 = 0.0
    for a, na in ca.items():
        for b, nb in cb.items():
            exp = na * nb / 64.0
            obs = cab.get((a, b), 0)
            x2 += (obs - exp) ** 2 / exp
    return x2


def perm_p(part_a, part_b, n=20000, seed=7):
    """Перестановочный p: часто ли случайная переклейка классов part_b даёт
    χ² не меньше наблюдённого."""
    obs = chi2(part_a, part_b)
    gates = list(range(1, 65))
    labels = [part_b[g] for g in gates]
    rng = random.Random(seed)
    hits = 0
    for _ in range(n):
        rng.shuffle(labels)
        pb = {g: labels[i] for i, g in enumerate(gates)}
        if chi2(part_a, pb) >= obs:
            hits += 1
    return obs, (hits + 1) / (n + 1)


def main():
    print("=" * 78)
    print("hd_circuits_lab — контуры HD против структуры колеса")
    print("=" * 78)
    circ = {}
    for name, gs in CIRCUITS.items():
        for g in gs:
            circ[g] = name
    macro = {}
    for name, gs in MACRO.items():
        for g in gs:
            macro[g] = name
    assert len(circ) == 64 and len(macro) == 64, "таблица не покрывает 64"

    roots = {g: nuclear_root(g) for g in range(1, 65)}
    print("\nC1. Контуры ↔ ядерные корни")
    x2, p = perm_p(circ, roots)
    print("  6 контуров × 3 корня: χ²=%.1f, перестановочный p=%.3f" % (x2, p))
    x2m, pm = perm_p(macro, roots)
    print("  3 семейства × 3 корня: χ²=%.1f, p=%.3f" % (x2m, pm))
    tbl = Counter((macro[g], roots[g]) for g in range(1, 65))
    for fam in MACRO:
        row = [tbl.get((fam, r), 0) for r in ("source", "voice-O", "pendulum")]
        print("    %-11s исток %2d · голос-О %2d · маятник %2d"
              % (fam, *row))
    verdict = ("СВЯЗЬ ЕСТЬ — контуры частично дублируют корневую разметку"
               if min(p, pm) < 0.01 else
               "связи НЕ видно — контуры ортогональны ядерным корням")
    print("  вердикт C1 [С]: %s (порог p<0.01)." % verdict)

    print("\nC2. Контуры ↔ роды объектов атласа")
    # роды объектов: восстановим по весу Хэмминга кода ворот — не наш атлас,
    # а честная структурная прокси: 64 = 1+21+35+7 в движке; здесь берём
    # четыре рода по весу: 0/6 (полюса), 1/5 (голоса), 2/4 (пары+), 3 (середина)
    weight_kind = {}
    for g in range(1, 65):
        w = bin(KW_BITS[g - 1]).count("1")
        weight_kind[g] = {0: "pole", 6: "pole", 1: "near-pole",
                          5: "near-pole", 2: "mid", 4: "mid", 3: "center"}[w]
    x2w, pw = perm_p(circ, weight_kind)
    print("  6 контуров × 4 весовых рода: χ²=%.1f, p=%.3f" % (x2w, pw))
    print("  вердикт C2 [С]: %s (порог p<0.01)."
          % ("контуры чувствуют вес кода" if pw < 0.01
             else "к весу кода контуры слепы"))

    print("\nC3. Контуры ↔ голосовой состав (через линии-голоса)")
    # мешок голосов ворот = его единичные линии в LINE_VOICE-разметке
    LINE_VOICE = "ASLDUE"
    def bag(gs):
        c = Counter()
        for g in gs:
            b = KW_BITS[g - 1]
            for k in range(6):
                if (b >> k) & 1:
                    c[LINE_VOICE[k]] += 1
        return c
    obs_dev = 0.0
    for name, gs in CIRCUITS.items():
        b = bag(gs)
        total = sum(b.values()) or 1
        # отклонение мешка от равномерного профиля
        obs_dev += sum(abs(b.get(v, 0) / total - 1 / 6) for v in LINE_VOICE)
    rng = random.Random(11)
    gates = list(range(1, 65))
    hits = 0
    N = 5000
    sizes = [len(gs) for gs in CIRCUITS.values()]
    for _ in range(N):
        rng.shuffle(gates)
        dev = 0.0
        i = 0
        for sz in sizes:
            b = bag(gates[i:i + sz])
            i += sz
            total = sum(b.values()) or 1
            dev += sum(abs(b.get(v, 0) / total - 1 / 6) for v in LINE_VOICE)
        if dev >= obs_dev:
            hits += 1
    p3 = (hits + 1) / (N + 1)
    print("  суммарное отклонение голосовых мешков: %.3f, p=%.3f"
          % (obs_dev, p3))
    print("  вердикт C3 [С]: %s (порог p<0.01)."
          % ("контуры несут голосовой рельеф" if p3 < 0.01
             else "голосовые мешки контуров неотличимы от случайной нарезки"))

    print("\n" + "=" * 78)
    print("Итог: контуры — их сильнейшая групповая структура; выше — есть ли")
    print("у неё двойник в нашем колесе. Любой из трёх нулей — тоже результат:")
    print("он значит, что «контур» — независимый слой проводки (каналы), а не")
    print("переименование известной решётки. [С] на фиксированных ансамблях.")


if __name__ == "__main__":
    main()
