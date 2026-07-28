#!/usr/bin/env python3
"""Фигура «Складка и замедление» для evolution.md (§ оборота, T-291).

Слева: порог жизни ω₀*(g_D) — прямая замкнутой формулы Λ*·g_D (луч без
вращения) и точки полной динамики выше неё; зазор = цена вращения
(×3.07 / ×1.93 / ×1.38 при g_D = 0.1 / 0.2 / 0.4).
Справа: критическое замедление — τ₁ₑ возврата растёт к складке
(0.010 при ω₀=500 → 0.260 у 1.1·ω₀*), ось ω₀ логарифмическая.

Числа — из NUMBERS-LEDGER (cycle_stationarity.rs), не иллюстративные.
Выход: website/static/img/theory/fold-{en,ru}-{light,dark}.svg
"""
import math
import os

OUT = os.path.join(os.path.dirname(__file__), '..',
                   'website', 'static', 'img', 'theory')

PAL = {
    'light': dict(ink='#1c1e21', faint='#8a8f98', ray='#0f766e',
                  dyn='#c2410c', tau='#4f46e5'),
    'dark': dict(ink='#e3e3e3', faint='#9aa0a6', ray='#2dd4bf',
                 dyn='#fb923c', tau='#a5b4fc'),
}
TXT = {
    'ru': dict(
        t1='порог жизни: ω₀* = Λ*·g_D × надбавка вращения',
        ray='луч без вращения: Λ*·g_D, Λ* = 50.5',
        dyn='полная динамика',
        sur='цена вращения',
        xl1='распад g_D',
        t2='критическое замедление у складки',
        xl2='насос ω₀ (лог)',
        yl2='τ₁ₑ возврата',
        fold='складка ω₀*',
    ),
    'en': dict(
        t1='the threshold of life: ω₀* = Λ*·g_D × rotation surcharge',
        ray='rotation-free ray: Λ*·g_D, Λ* = 50.5',
        dyn='full dynamics',
        sur='price of rotation',
        xl1='decay g_D',
        t2='critical slowing near the fold',
        xl2='pump ω₀ (log)',
        yl2='return τ₁ₑ',
        fold='the fold ω₀*',
    ),
}

# Числа реестра
GD = [0.1, 0.2, 0.4]
RAY = [5.05, 10.10, 20.20]
DYN = [15.50, 19.47, 27.81]
SUR = ['×3.07', '×1.93', '×1.38']
OM_STAR = 19.5
TAUS = [(OM_STAR * 1.1, 0.260), (OM_STAR * 1.5, 0.150),
        (100.0, 0.040), (500.0, 0.010)]


def text(x, y, s, color, size=14, anchor='middle', style=''):
    return (f'<text x="{x:.1f}" y="{y:.1f}" fill="{color}" '
            f'font-size="{size}" text-anchor="{anchor}" '
            f'font-family="system-ui, -apple-system, Segoe UI, sans-serif" '
            f'{style}>{s}</text>')


def build(lang, theme):
    p = PAL[theme]
    t = TXT[lang]
    W, H = 990, 400
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" '
             f'viewBox="0 0 {W} {H}">']

    # ── панель 1: ω₀*(g_D) ──
    x0, x1, y0, y1 = 70, 440, 320, 70
    sx = lambda g: x0 + (x1 - x0) * g / 0.45
    sy = lambda w: y0 - (y0 - y1) * w / 30.0
    parts.append(text((x0 + x1) / 2, 34, t['t1'], p['ink'], 15, 'middle',
                      'font-weight="600"'))
    parts.append(f'<line x1="{x0}" y1="{y0}" x2="{x1+10}" y2="{y0}" '
                 f'stroke="{p["faint"]}" stroke-width="1.5"/>')
    parts.append(f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y1-10}" '
                 f'stroke="{p["faint"]}" stroke-width="1.5"/>')
    for g in GD:
        parts.append(text(sx(g), y0 + 20, f'{g}', p['faint'], 12.5))
    parts.append(text((x0 + x1) / 2, y0 + 42, t['xl1'], p['faint'], 13))
    # луч формулы
    parts.append(f'<line x1="{sx(0):.1f}" y1="{sy(0):.1f}" '
                 f'x2="{sx(0.44):.1f}" y2="{sy(0.44*50.5):.1f}" '
                 f'stroke="{p["ray"]}" stroke-width="2.5"/>')
    parts.append(text(sx(0.30), sy(0.30 * 50.5) + 22, t['ray'], p['ray'],
                      13, 'middle'))
    # точки динамики + зазоры
    for g, r, d, s_ in zip(GD, RAY, DYN, SUR):
        parts.append(f'<line x1="{sx(g):.1f}" y1="{sy(r):.1f}" '
                     f'x2="{sx(g):.1f}" y2="{sy(d):.1f}" '
                     f'stroke="{p["dyn"]}" stroke-width="1.6" '
                     f'stroke-dasharray="3 3"/>')
        parts.append(f'<circle cx="{sx(g):.1f}" cy="{sy(r):.1f}" r="4.5" '
                     f'fill="{p["ray"]}"/>')
        parts.append(f'<circle cx="{sx(g):.1f}" cy="{sy(d):.1f}" r="5.5" '
                     f'fill="{p["dyn"]}"/>')
        parts.append(text(sx(g) + 10, sy(d) - 8, s_, p['dyn'], 13, 'start',
                          'font-weight="600"'))
    parts.append(text(sx(0.32), sy(27) - 14, t['dyn'], p['dyn'], 13.5))
    parts.append(text(sx(0.13) + 4, (sy(RAY[0]) + sy(DYN[0])) / 2 + 4,
                      t['sur'], p['dyn'], 12.5, 'start'))

    # ── панель 2: τ(ω₀), лог-ось ──
    a0, a1, b0, b1 = 560, 930, 320, 70
    lmin, lmax = math.log10(15), math.log10(600)
    ax = lambda w: a0 + (a1 - a0) * (math.log10(w) - lmin) / (lmax - lmin)
    ay = lambda v: b0 - (b0 - b1) * v / 0.30
    parts.append(text((a0 + a1) / 2, 34, t['t2'], p['ink'], 15, 'middle',
                      'font-weight="600"'))
    parts.append(f'<line x1="{a0}" y1="{b0}" x2="{a1+10}" y2="{b0}" '
                 f'stroke="{p["faint"]}" stroke-width="1.5"/>')
    parts.append(f'<line x1="{a0}" y1="{b0}" x2="{a0}" y2="{b1-10}" '
                 f'stroke="{p["faint"]}" stroke-width="1.5"/>')
    for w in [20, 50, 100, 200, 500]:
        parts.append(f'<line x1="{ax(w):.1f}" y1="{b0}" x2="{ax(w):.1f}" '
                     f'y2="{b0+6}" stroke="{p["faint"]}"/>')
        parts.append(text(ax(w), b0 + 22, f'{w}', p['faint'], 12))
    parts.append(text((a0 + a1) / 2, b0 + 42, t['xl2'], p['faint'], 13))
    parts.append(text(a0 - 40, (b0 + b1) / 2, t['yl2'], p['faint'], 13,
                      'middle', f'transform="rotate(-90 {a0-40} '
                                f'{(b0+b1)/2:.0f})"'))
    # складка
    parts.append(f'<line x1="{ax(OM_STAR):.1f}" y1="{b0}" '
                 f'x2="{ax(OM_STAR):.1f}" y2="{b1}" stroke="{p["dyn"]}" '
                 f'stroke-width="1.6" stroke-dasharray="6 5"/>')
    parts.append(text(ax(OM_STAR) + 6, b1 + 14, t['fold'], p['dyn'], 13,
                      'start'))
    # кривая τ
    pts = sorted(TAUS)
    path = 'M ' + ' L '.join(f'{ax(w):.1f} {ay(v):.1f}' for w, v in pts)
    parts.append(f'<path d="{path}" fill="none" stroke="{p["tau"]}" '
                 f'stroke-width="2.5"/>')
    for w, v in pts:
        parts.append(f'<circle cx="{ax(w):.1f}" cy="{ay(v):.1f}" r="5" '
                     f'fill="{p["tau"]}"/>')
        parts.append(text(ax(w) + 8, ay(v) - 10, f'{v:.3f}'.rstrip('0'),
                          p['tau'], 12.5, 'start'))
    parts.append('</svg>')
    return '\n'.join(parts)


os.makedirs(OUT, exist_ok=True)
for lang in ('en', 'ru'):
    for theme in ('light', 'dark'):
        with open(os.path.join(OUT, f'fold-{lang}-{theme}.svg'), 'w',
                  encoding='utf-8') as f:
            f.write(build(lang, theme))
print('fold: 4 варианта записаны')
