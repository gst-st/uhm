#!/usr/bin/env python3
"""Фигура «Закон границы бассейнов» для conscious-window.md (динамическое
чтение порога 2/7).

Слева: лог-лог P*−2/7 против g_d/ω₀ — быстрый режим (ω₀ = 80…640) ложится
на прямую закона C·g_d/ω₀ с C = 1.705 (замкнутая форма, ни одного фита);
средний режим (ω₀ = 20, 40) уходит вверх — седло покидает отрезок.
Справа: геометрия — отрезок [серое, ρ*], статическое седло на нём,
вращение уводит истинное седло с отрезка (63 % вне при ω₀=20), наклонённое
устойчивое многообразие возвращает пересечение с семейством вниз.

Числа — из NUMBERS-LEDGER (awakening_boundary_law.rs и Ньютон-седло),
не иллюстративные. Выход: website/static/img/theory/
boundary-{en,ru}-{light,dark}.svg
"""
import math
import os

OUT = os.path.join(os.path.dirname(__file__), '..',
                   'website', 'static', 'img', 'theory')

PAL = {
    'light': dict(ink='#1c1e21', faint='#8a8f98', law='#0f766e',
                  fast='#0f766e', mid='#c2410c', geo='#4f46e5',
                  grey='#6b7280'),
    'dark': dict(ink='#e3e3e3', faint='#9aa0a6', law='#2dd4bf',
                 fast='#2dd4bf', mid='#fb923c', geo='#a5b4fc',
                 grey='#9ca3af'),
}
TXT = {
    'ru': dict(
        t1='закон границы: P* − 2/7 = C·g_d/ω₀, C = 1.705 (без фитов)',
        law='замкнутая форма C(P_ρ)',
        fast='быстрый режим (ω₀ = 80…640)',
        mid='средний режим (ω₀ = 20, 40): седло уходит с отрезка',
        xl1='g_d/ω₀ (лог)',
        yl1='P* − 2/7 (лог)',
        t2='геометрия среднего режима (ω₀ = 20, числа замера)',
        seg='отрезок [серое, ρ*]',
        stat='статика: 0.2874',
        saddle='истинное седло: 0.3185 (63 % вне)',
        mani='наклон W^s',
        cross='граница: 0.2932',
        greyp='серое (P = 1/7)',
        rhop='ρ*',
    ),
    'en': dict(
        t1='the boundary law: P* − 2/7 = C·g_d/ω₀, C = 1.705 (zero fits)',
        law='closed form C(P_ρ)',
        fast='fast regime (ω₀ = 80…640)',
        mid='mid regime (ω₀ = 20, 40): the saddle leaves the segment',
        xl1='g_d/ω₀ (log)',
        yl1='P* − 2/7 (log)',
        t2='mid-regime geometry (ω₀ = 20, measured numbers)',
        seg='segment [grey, ρ*]',
        stat='statics: 0.2874',
        saddle='true saddle: 0.3185 (63 % off)',
        mani='W^s tilt',
        cross='boundary: 0.2932',
        greyp='grey (P = 1/7)',
        rhop='ρ*',
    ),
}

# ── числа реестра: (ω₀, g_d, P*−2/7)
FAST = [
    (80, .005, 1.18e-4), (80, .01, 2.29e-4), (80, .02, 4.50e-4),
    (80, .04, 8.96e-4),
    (160, .005, 5.4e-5), (160, .01, 1.07e-4), (160, .02, 2.15e-4),
    (160, .04, 4.30e-4),
    (320, .005, 2.7e-5), (320, .01, 5.3e-5), (320, .02, 1.07e-4),
    (320, .04, 2.14e-4),
    (640, .02, 1.07e-4), (640, .04, 2.14e-4),
]
MID = [
    (20, .005, 5.495e-3), (20, .01, 6.143e-3), (20, .02, 7.461e-3),
    (20, .04, 1.0193e-2),
    (40, .005, 6.20e-4), (40, .01, 8.65e-4), (40, .02, 1.356e-3),
    (40, .04, 2.349e-3),
]
C_LAW = 1.705

W, H = 900, 430


def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;')


def text(x, y, s, color, size=13, anchor='middle', style=''):
    return (f'<text x="{x:.1f}" y="{y:.1f}" fill="{color}" '
            f'font-size="{size}" text-anchor="{anchor}" '
            f'font-family="system-ui,sans-serif" {style}>{esc(s)}</text>')


def make(lang, theme):
    p = PAL[theme]
    tx = TXT[lang]
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" '
         f'height="{H}" viewBox="0 0 {W} {H}">']

    # ═══ левая панель: лог-лог
    x0, y0, x1, y1 = 70, 60, 430, 380
    lx = lambda v: x0 + (math.log10(v) - math.log10(6e-6)) / \
        (math.log10(4e-3) - math.log10(6e-6)) * (x1 - x0)
    ly = lambda v: y1 - (math.log10(v) - math.log10(1.5e-5)) / \
        (math.log10(2.5e-2) - math.log10(1.5e-5)) * (y1 - y0)
    s.append(f'<rect x="{x0}" y="{y0}" width="{x1-x0}" height="{y1-y0}" '
             f'fill="none" stroke="{p["faint"]}" stroke-width="1"/>')
    # сетка декад
    for d in range(-5, -2):
        v = 10 ** d
        if 6e-6 < v < 4e-3:
            s.append(f'<line x1="{lx(v):.1f}" y1="{y0}" x2="{lx(v):.1f}" '
                     f'y2="{y1}" stroke="{p["faint"]}" stroke-width="0.5" '
                     f'opacity="0.5"/>')
            s.append(text(lx(v), y1 + 16, f'1e{d}', p['faint'], 11))
    for d in range(-4, -1):
        v = 10 ** d
        if 1.5e-5 < v < 2.5e-2:
            s.append(f'<line x1="{x0}" y1="{ly(v):.1f}" x2="{x1}" '
                     f'y2="{ly(v):.1f}" stroke="{p["faint"]}" '
                     f'stroke-width="0.5" opacity="0.5"/>')
            s.append(text(x0 - 8, ly(v) + 4, f'1e{d}', p['faint'], 11,
                          'end'))
    # прямая закона
    xa, xb = 8e-6, 8e-4
    s.append(f'<line x1="{lx(xa):.1f}" y1="{ly(C_LAW*xa):.1f}" '
             f'x2="{lx(xb):.1f}" y2="{ly(C_LAW*xb):.1f}" '
             f'stroke="{p["law"]}" stroke-width="2.2"/>')
    s.append(text(lx(2.2e-5), ly(C_LAW * 2.2e-5) - 12, tx['law'],
                  p['law'], 12, 'middle',
                  f'transform="rotate(-33 {lx(2.2e-5):.0f} '
                  f'{ly(C_LAW*2.2e-5)-12:.0f})"'))
    # точки
    for w0, gd, y in FAST:
        s.append(f'<circle cx="{lx(gd/w0):.1f}" cy="{ly(y):.1f}" r="4" '
                 f'fill="{p["fast"]}" opacity="0.9"/>')
    for w0, gd, y in MID:
        s.append(f'<rect x="{lx(gd/w0)-3.5:.1f}" y="{ly(y)-3.5:.1f}" '
                 f'width="7" height="7" fill="{p["mid"]}" opacity="0.9"/>')
    s.append(text((x0 + x1) / 2, 36, tx['t1'], p['ink'], 14))
    s.append(text((x0 + x1) / 2, y1 + 36, tx['xl1'], p['faint'], 12))
    s.append(text(24, (y0 + y1) / 2, tx['yl1'], p['faint'], 12, 'middle',
                  f'transform="rotate(-90 24 {(y0+y1)/2:.0f})"'))
    # легенда
    s.append(f'<circle cx="{x0+16}" cy="{y0+18}" r="4" fill="{p["fast"]}"/>')
    s.append(text(x0 + 26, y0 + 22, tx['fast'], p['ink'], 12, 'start'))
    s.append(f'<rect x="{x0+12.5}" y="{y0+32.5}" width="7" height="7" '
             f'fill="{p["mid"]}"/>')
    s.append(text(x0 + 26, y0 + 41, tx['mid'], p['ink'], 12, 'start'))

    # ═══ правая панель: геометрия
    gx, gy = 490, 60
    gw, gh = 380, 320
    # отрезок [grey, rho*]: диагональ
    ax, ay = gx + 30, gy + gh - 40   # grey
    bx, by = gx + gw - 40, gy + 40   # rho*
    s.append(f'<line x1="{ax}" y1="{ay}" x2="{bx}" y2="{by}" '
             f'stroke="{p["grey"]}" stroke-width="2"/>')
    s.append(f'<circle cx="{ax}" cy="{ay}" r="6" fill="{p["grey"]}"/>')
    s.append(text(ax, ay + 22, tx['greyp'], p['faint'], 12))
    s.append(f'<circle cx="{bx}" cy="{by}" r="6" fill="{p["ink"]}"/>')
    s.append(text(bx, by - 12, tx['rhop'], p['ink'], 13))
    s.append(text((ax + bx) / 2 + 52, (ay + by) / 2 + 44, tx['seg'],
                  p['faint'], 12))
    # точки на отрезке: статика (t=0.55), пересечение границы (t=0.62)
    def seg_pt(t):
        return ax + (bx - ax) * t, ay + (by - ay) * t
    sx, sy = seg_pt(0.52)
    s.append(f'<circle cx="{sx:.0f}" cy="{sy:.0f}" r="5" fill="none" '
             f'stroke="{p["law"]}" stroke-width="2"/>')
    s.append(text(sx + 10, sy + 18, tx['stat'], p['law'], 12, 'start'))
    cxp, cyp = seg_pt(0.635)
    s.append(f'<circle cx="{cxp:.0f}" cy="{cyp:.0f}" r="5" '
             f'fill="{p["mid"]}"/>')
    s.append(text(cxp + 10, cyp + 16, tx['cross'], p['mid'], 12, 'start'))
    # истинное седло — вне отрезка (вверх-влево от точки t=0.72)
    tx0, ty0 = seg_pt(0.72)
    sadx, sady = tx0 - 90, ty0 - 58
    s.append(f'<circle cx="{sadx:.0f}" cy="{sady:.0f}" r="6" '
             f'fill="{p["geo"]}"/>')
    s.append(text(sadx + 6, sady - 14, tx['saddle'], p['geo'], 12, 'end'))
    # пунктир смещения седла
    s.append(f'<line x1="{tx0:.0f}" y1="{ty0:.0f}" x2="{sadx:.0f}" '
             f'y2="{sady:.0f}" stroke="{p["geo"]}" stroke-width="1.2" '
             f'stroke-dasharray="4 4" opacity="0.7"/>')
    # W^s: кривая из седла к пересечению с отрезком
    s.append(f'<path d="M {sadx-70:.0f} {sady-52:.0f} Q {sadx:.0f} '
             f'{sady:.0f} {cxp:.0f} {cyp:.0f}" fill="none" '
             f'stroke="{p["geo"]}" stroke-width="2.2" opacity="0.9"/>')
    s.append(text(sadx - 78, sady - 62, tx['mani'], p['geo'], 12, 'start'))
    s.append(text(gx + gw / 2, 36, tx['t2'], p['ink'], 14))

    s.append('</svg>')
    return '\n'.join(s)


os.makedirs(OUT, exist_ok=True)
for lang in ('ru', 'en'):
    for theme in ('light', 'dark'):
        path = os.path.join(OUT, f'boundary-{lang}-{theme}.svg')
        with open(path, 'w') as f:
            f.write(make(lang, theme))
        print('written', path)
