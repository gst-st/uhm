#!/usr/bin/env python3
"""Фигура «Аккорд» для evolution.md: гребёнка частот Бора H_EFF.

21 связка → 10 различных частот; вырождения связывают связки в «хоры»,
бьющиеся в один такт. Высота линии = размер хора; над линией — имена пар.
Подпись: частоты — устройство (одни на всех), амплитуды — личность.

Выход: website/static/img/theory/chord-{en,ru}-{light,dark}.svg
"""
import os
from collections import defaultdict

OUT = os.path.join(os.path.dirname(__file__), '..',
                   'website', 'static', 'img', 'theory')

H_EFF = [0.0, 0.6, 1.0, 1.6, 3.0, 2.0, 2.4]
AX = 'ASDLEOU'

PAL = {
    'light': dict(ink='#1c1e21', faint='#8a8f98', bar='#4f46e5',
                  hi='#0f766e'),
    'dark': dict(ink='#e3e3e3', faint='#9aa0a6', bar='#a5b4fc',
                 hi='#2dd4bf'),
}
TXT = {
    'ru': dict(title='аккорд устройства: 21 связка, 10 частот',
               x='частота Бора ω = |λᵢ − λⱼ|',
               y='размер хора',
               note='частоты — устройство, одни на всех; какие струны звучат '
                    'и как громко — личность (самомодель)'),
    'en': dict(title='the chord of the design: 21 couplings, 10 frequencies',
               x='Bohr frequency ω = |λᵢ − λⱼ|',
               y='choir size',
               note='the frequencies are the design, the same for everyone; '
                    'which strings sound, and how loudly — the person '
                    '(the self-model)'),
}


def text(x, y, s, color, size=14, anchor='middle', style=''):
    return (f'<text x="{x:.1f}" y="{y:.1f}" fill="{color}" '
            f'font-size="{size}" text-anchor="{anchor}" '
            f'font-family="system-ui, -apple-system, Segoe UI, sans-serif" '
            f'{style}>{s}</text>')


def build(lang, theme):
    p = PAL[theme]
    t = TXT[lang]
    groups = defaultdict(list)
    for i in range(7):
        for j in range(i + 1, 7):
            w = round(abs(H_EFF[i] - H_EFF[j]), 10)
            groups[w].append(AX[i] + AX[j])
    freqs = sorted(groups)

    W, H = 990, 400
    x_l, x_r = 90, 940
    y_base, y_unit = 300, 42
    sx = lambda w: x_l + (x_r - x_l) * w / 3.0

    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" '
             f'viewBox="0 0 {W} {H}">']
    parts.append(text(x_l - 20, 28, t['title'], p['ink'], 16,
                      'start', 'font-weight="600"'))
    # оси
    parts.append(f'<line x1="{x_l-20}" y1="{y_base}" x2="{x_r+20}" '
                 f'y2="{y_base}" stroke="{p["faint"]}" stroke-width="1.5"/>')
    for w in [0, 1, 2, 3]:
        parts.append(f'<line x1="{sx(w)}" y1="{y_base}" x2="{sx(w)}" '
                     f'y2="{y_base+7}" stroke="{p["faint"]}"/>')
        parts.append(text(sx(w), y_base + 26, f'{w}', p['faint'], 13))
    parts.append(text((x_l + x_r) / 2, y_base + 52, t['x'], p['faint'], 13.5))
    parts.append(text(x_l - 44, y_base - 1.5 * y_unit, t['y'], p['faint'],
                      13, 'middle',
                      f'transform="rotate(-90 {x_l-44} '
                      f'{y_base-1.5*y_unit:.0f})"'))
    # гребёнка
    for w in freqs:
        chorus = groups[w]
        n = len(chorus)
        x = sx(w)
        color = p['hi'] if n >= 3 else p['bar']
        parts.append(f'<line x1="{x:.1f}" y1="{y_base}" x2="{x:.1f}" '
                     f'y2="{y_base - n*y_unit:.1f}" stroke="{color}" '
                     f'stroke-width="6" stroke-linecap="round"/>')
        for k, pair in enumerate(sorted(chorus)):
            parts.append(text(x, y_base - n * y_unit - 12 - 17 * (
                len(chorus) - 1 - k), pair, color, 13.5, 'middle',
                'font-weight="600"' if n >= 3 else ''))
        parts.append(text(x, y_base - 8, '', color))
    parts.append(text((x_l + x_r) / 2, H - 12, t['note'], p['ink'], 13.5))
    parts.append('</svg>')
    return '\n'.join(parts)


os.makedirs(OUT, exist_ok=True)
for lang in ('en', 'ru'):
    for theme in ('light', 'dark'):
        with open(os.path.join(OUT, f'chord-{lang}-{theme}.svg'), 'w',
                  encoding='utf-8') as f:
            f.write(build(lang, theme))
print('chord: 4 варианта записаны')
