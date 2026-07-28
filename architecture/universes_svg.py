#!/usr/bin/env python3
"""Фигура «Три геометрические вселенные» для §83-бис (homoholograph.md).

Слева — решёточный мир цветка (A2: узлы + лунки, порядки 2·3·4·6);
в центре — пятикратный мир (пентаграмма, 2cos72° ∉ ℤ — вне решёток);
справа — семикратный конечно-проективный (плоскость Фано, PSL(2,7)).
Подпись: число, общее для вселенных, — не мост; мост — конструкция.

Выход: website/static/img/theory/universes-{en,ru}-{light,dark}.svg
"""
import math
import os

OUT = os.path.join(os.path.dirname(__file__), '..',
                   'website', 'static', 'img', 'theory')

PAL = {
    'light': dict(ink='#1c1e21', faint='#8a8f98', a='#0f766e',
                  b='#b45309', c='#4f46e5'),
    'dark': dict(ink='#e3e3e3', faint='#9aa0a6', a='#2dd4bf',
                 b='#fbbf24', c='#a5b4fc'),
}
TXT = {
    'ru': dict(t1='решётка (цветок): 2·3·4·6',
               t2='пятёрка: вне решёток',
               t3='семёрка: проективная (Fano)',
               n2='2cos(2π/5) ∉ ℤ',
               n3='7 точек = 7 прямых · PSL(2,7)',
               cap='число, общее для вселенных, — не мост; '
                   'мост обязан быть конструкцией'),
    'en': dict(t1='the lattice (the flower): 2·3·4·6',
               t2='five-fold: outside lattices',
               t3='seven-fold: projective (Fano)',
               n2='2cos(2π/5) ∉ ℤ',
               n3='7 points = 7 lines · PSL(2,7)',
               cap='a number shared across universes is not a bridge; '
                   'a bridge must be a construction'),
}


def text(x, y, s, color, size=14, anchor='middle', style=''):
    return (f'<text x="{x:.1f}" y="{y:.1f}" fill="{color}" '
            f'font-size="{size}" text-anchor="{anchor}" '
            f'font-family="system-ui, -apple-system, Segoe UI, sans-serif" '
            f'{style}>{s}</text>')


def build(lang, theme):
    p = PAL[theme]
    t = TXT[lang]
    W, H = 990, 360
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" '
             f'viewBox="0 0 {W} {H}">']

    # ── панель 1: решётка A2 + лунки ──
    cx1, cy1, a = 170, 165, 46
    e1 = (a, 0.0)
    e2 = (a / 2, a * math.sqrt(3) / 2)
    for u in range(-2, 3):
        for v in range(-2, 3):
            x = cx1 + u * e1[0] + v * e2[0]
            y = cy1 + u * e1[1] + v * e2[1]
            if abs(x - cx1) < 120 and abs(y - cy1) < 105:
                parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" '
                             f'fill="{p["a"]}"/>')
                # лунка треугольника
                hx = x + a / 2
                hy = y + a * math.sqrt(3) / 6
                if abs(hx - cx1) < 120 and abs(hy - cy1) < 105:
                    parts.append(f'<circle cx="{hx:.1f}" cy="{hy:.1f}" '
                                 f'r="2.6" fill="none" '
                                 f'stroke="{p["a"]}" stroke-width="1.2" '
                                 f'opacity="0.65"/>')
    parts.append(text(cx1, 315, t['t1'], p['ink'], 15, 'middle',
                      'font-weight="600"'))

    # ── панель 2: пентаграмма ──
    cx2, cy2, R2 = 495, 160, 92
    pts = [(cx2 + R2 * math.sin(2 * math.pi * k / 5),
            cy2 - R2 * math.cos(2 * math.pi * k / 5)) for k in range(5)]
    for k in range(5):
        x1, y1 = pts[k]
        x2, y2 = pts[(k + 2) % 5]
        parts.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" '
                     f'y2="{y2:.1f}" stroke="{p["b"]}" stroke-width="2.4"/>')
    for x, y in pts:
        parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" '
                     f'fill="{p["b"]}"/>')
    parts.append(text(cx2, 292, t['n2'], p['faint'], 13))
    parts.append(text(cx2, 315, t['t2'], p['ink'], 15, 'middle',
                      'font-weight="600"'))

    # ── панель 3: плоскость Фано ──
    cx3, cy3, R3 = 820, 175, 100
    v = [(cx3 + R3 * math.sin(2 * math.pi * k / 3),
          cy3 - R3 * math.cos(2 * math.pi * k / 3) + 18) for k in range(3)]
    mid = [((v[(k + 1) % 3][0] + v[(k + 2) % 3][0]) / 2,
            (v[(k + 1) % 3][1] + v[(k + 2) % 3][1]) / 2) for k in range(3)]
    cen = (cx3, cy3 + 18)
    # стороны и медианы
    for k in range(3):
        x1, y1 = v[k]
        x2, y2 = v[(k + 1) % 3]
        parts.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" '
                     f'y2="{y2:.1f}" stroke="{p["c"]}" stroke-width="2.2"/>')
        mx, my = mid[k]
        parts.append(f'<line x1="{v[k][0]:.1f}" y1="{v[k][1]:.1f}" '
                     f'x2="{mx:.1f}" y2="{my:.1f}" stroke="{p["c"]}" '
                     f'stroke-width="2.2"/>')
    # вписанная окружность через середины
    rin = math.dist(cen, mid[0])
    parts.append(f'<circle cx="{cen[0]:.1f}" cy="{cen[1]:.1f}" '
                 f'r="{rin:.1f}" fill="none" stroke="{p["c"]}" '
                 f'stroke-width="2.2"/>')
    for x, y in v + mid + [cen]:
        parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6" '
                     f'fill="{p["c"]}"/>')
    parts.append(text(cx3, 292 + 23, '', p['faint']))
    parts.append(text(cx3, 292, t['n3'], p['faint'], 13))
    parts.append(text(cx3, 315, t['t3'], p['ink'], 15, 'middle',
                      'font-weight="600"'))

    parts.append(text(W / 2, H - 12, t['cap'], p['ink'], 14))
    parts.append('</svg>')
    return '\n'.join(parts)


os.makedirs(OUT, exist_ok=True)
for lang in ('en', 'ru'):
    for theme in ('light', 'dark'):
        with open(os.path.join(OUT, f'universes-{lang}-{theme}.svg'), 'w',
                  encoding='utf-8') as f:
            f.write(build(lang, theme))
print('universes: 4 варианта записаны')
