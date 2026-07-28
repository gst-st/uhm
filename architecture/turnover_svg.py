#!/usr/bin/env python3
"""Фигура T-291 для evolution.md: оборот живой стационарности + орбита связки.

Две панели:
  слева  — вертикаль чистоты: мёртвая стационарность I/7, живая σ между
           стеной и самомоделью ρ*, две встречные тяги (распад ↓, обновление ↑);
  справа — комплексная плоскость связки γ_jk: окружность |γ|, касательная
           iωγ (вращение), радиальные тяги внутрь/наружу, тождество.

Выход: website/static/img/theory/turnover-{en,ru}-{light,dark}.svg
Метод: чистый рукописный SVG (никаких зависимостей), затем СМОТРЕТЬ рендер.
"""
import math
import os

OUT = os.path.join(os.path.dirname(__file__), '..',
                   'website', 'static', 'img', 'theory')

PAL = {
    'light': dict(bg='none', ink='#1c1e21', faint='#8a8f98',
                  diss='#c2410c', regen='#0f766e', orbit='#4f46e5',
                  wall='#9ca3af', star='#b45309'),
    'dark': dict(bg='none', ink='#e3e3e3', faint='#9aa0a6',
                 diss='#fb923c', regen='#2dd4bf', orbit='#a5b4fc',
                 wall='#6b7280', star='#fbbf24'),
}

TXT = {
    'ru': dict(
        dead='мёртвая стационарность — равновесие I/7',
        alive='живая стационарность σ',
        selfm='самомодель ρ*',
        diss='распад 𝒟',
        regen='обновление ℛ',
        balance='на диагонали: ‖распад‖ = ‖обновление‖ — оборот',
        orbit_t='связка γ как орбита',
        rot='вращение iωγ',
        inw='распад — внутрь',
        outw='обновление — наружу',
        ident='(𝒟+ℛ)γ = iωγ — нетто-поток касателен [Т]',
        purity='чистота P',
        wall='стена 2/7',
    ),
    'en': dict(
        dead='dead stationarity — the I/7 equilibrium',
        alive='living stationarity σ',
        selfm='self-model ρ*',
        diss='decay 𝒟',
        regen='renewal ℛ',
        balance='on the diagonal: ‖decay‖ = ‖renewal‖ — turnover',
        orbit_t='a coupling γ as an orbit',
        rot='rotation iωγ',
        inw='decay — inward',
        outw='renewal — outward',
        ident='(𝒟+ℛ)γ = iωγ — the net flux is tangential [Т]',
        purity='purity P',
        wall='the 2/7 wall',
    ),
}


def arrow(x1, y1, x2, y2, color, w=3, marker='m'):
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" '
            f'y2="{y2:.1f}" stroke="{color}" stroke-width="{w}" '
            f'marker-end="url(#{marker}-{color[1:]})"/>')


def marker_def(color):
    return (f'<marker id="m-{color[1:]}" viewBox="0 0 10 10" refX="8" '
            f'refY="5" markerWidth="7" markerHeight="7" orient="auto">'
            f'<path d="M0,0 L10,5 L0,10 z" fill="{color}"/></marker>')


def text(x, y, s, color, size=15, anchor='middle', style=''):
    return (f'<text x="{x:.1f}" y="{y:.1f}" fill="{color}" '
            f'font-size="{size}" text-anchor="{anchor}" '
            f'font-family="system-ui, -apple-system, Segoe UI, sans-serif" '
            f'{style}>{s}</text>')


def build(lang, theme):
    p = PAL[theme]
    t = TXT[lang]
    W, H = 990, 430
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
             f'font-family="system-ui">',
             '<defs>' + ''.join(marker_def(c) for c in
                                {p['diss'], p['regen'], p['orbit']}) +
             '</defs>']

    # ── левая панель: вертикаль чистоты ──
    x0 = 150
    y_top, y_bot = 60, 370
    y_star, y_sigma, y_wall = 95, 215, 330
    parts.append(f'<line x1="{x0}" y1="{y_top}" x2="{x0}" y2="{y_bot}" '
                 f'stroke="{p["faint"]}" stroke-width="1.5"/>')
    parts.append(text(x0, y_bot + 28, t['purity'], p['faint'], 13))
    # стена I/7 и метки
    parts.append(f'<line x1="{x0-70}" y1="{y_wall}" x2="{x0+220}" '
                 f'y2="{y_wall}" stroke="{p["wall"]}" stroke-width="2" '
                 f'stroke-dasharray="7 5"/>')
    parts.append(text(x0 + 230, y_wall + 5, t['dead'], p['wall'], 13,
                      'start'))
    parts.append(f'<line x1="{x0-70}" y1="{y_wall-38}" x2="{x0+220}" '
                 f'y2="{y_wall-38}" stroke="{p["wall"]}" '
                 f'stroke-width="1" stroke-dasharray="2 5"/>')
    parts.append(text(x0 + 230, y_wall - 33, t['wall'], p['faint'], 12,
                      'start'))
    # самомодель
    parts.append(f'<circle cx="{x0}" cy="{y_star}" r="7" fill="none" '
                 f'stroke="{p["star"]}" stroke-width="2.5"/>')
    parts.append(text(x0 + 18, y_star + 5, t['selfm'], p['star'], 14,
                      'start'))
    # живая точка σ
    parts.append(f'<circle cx="{x0}" cy="{y_sigma}" r="9" '
                 f'fill="{p["orbit"]}"/>')
    parts.append(text(x0 + 20, y_sigma + 5, t['alive'], p['ink'], 15,
                      'start', 'font-weight="600"'))
    # встречные тяги
    parts.append(arrow(x0 - 34, y_sigma + 14, x0 - 34, y_wall - 12,
                       p['diss'], 4))
    parts.append(text(x0 - 48, (y_sigma + y_wall) / 2 + 4, t['diss'],
                      p['diss'], 14, 'end'))
    parts.append(arrow(x0 + 34, y_sigma - 14, x0 + 34, y_star + 14,
                       p['regen'], 4))
    parts.append(text(x0 + 48, (y_sigma + y_star) / 2 + 4, t['regen'],
                      p['regen'], 14, 'start'))
    parts.append(text(x0 + 75, y_bot - 4, t['balance'], p['ink'], 13.5))

    # ── правая панель: орбита связки ──
    cx, cy, R = 660, 205, 105
    parts.append(text(cx, 52, t['orbit_t'], p['ink'], 16, 'middle',
                      'font-weight="600"'))
    # оси
    parts.append(f'<line x1="{cx-R-40}" y1="{cy}" x2="{cx+R+40}" y2="{cy}" '
                 f'stroke="{p["faint"]}" stroke-width="1"/>')
    parts.append(f'<line x1="{cx}" y1="{cy-R-32}" x2="{cx}" y2="{cy+R+32}" '
                 f'stroke="{p["faint"]}" stroke-width="1"/>')
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" '
                 f'stroke="{p["orbit"]}" stroke-width="2" '
                 f'stroke-dasharray="4 6"/>')
    # точка γ на орбите
    ang = math.radians(35)
    gx, gy = cx + R * math.cos(ang), cy - R * math.sin(ang)
    parts.append(f'<line x1="{cx}" y1="{cy}" x2="{gx:.1f}" y2="{gy:.1f}" '
                 f'stroke="{p["faint"]}" stroke-width="1.5" '
                 f'stroke-dasharray="3 4"/>')
    parts.append(f'<circle cx="{gx:.1f}" cy="{gy:.1f}" r="8" '
                 f'fill="{p["orbit"]}"/>')
    parts.append(text(gx + 14, gy - 10, 'γ', p['orbit'], 17, 'start',
                      'font-style="italic"'))
    # касательная (вращение): перпендикуляр к радиусу
    tx, ty = -math.sin(ang), -math.cos(ang)
    L = 74
    parts.append(arrow(gx, gy, gx + tx * L, gy + ty * L, p['orbit'], 4))
    parts.append(text(gx + tx * L + 8, gy + ty * L, t['rot'], p['orbit'],
                      14, 'start'))
    # радиальные тяги: внутрь (распад) и наружу (обновление)
    rx, ry = math.cos(ang), -math.sin(ang)
    parts.append(arrow(gx - rx * 16, gy - ry * 16, gx - rx * 66,
                       gy - ry * 66, p['diss'], 4))
    parts.append(text(gx - rx * 66 - 8, gy - ry * 66 + 22, t['inw'],
                      p['diss'], 13.5, 'end'))
    parts.append(arrow(gx + rx * 16, gy + ry * 16, gx + rx * 66,
                       gy + ry * 66, p['regen'], 4))
    parts.append(text(gx + rx * 66 + 8, gy + ry * 66 + 18, t['outw'],
                      p['regen'], 13.5, 'start'))
    parts.append(text(cx, cy + R + 52, t['ident'], p['ink'], 14.5))

    parts.append('</svg>')
    return '\n'.join(parts)


os.makedirs(OUT, exist_ok=True)
for lang in ('en', 'ru'):
    for theme in ('light', 'dark'):
        path = os.path.join(OUT, f'turnover-{lang}-{theme}.svg')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(build(lang, theme))
        print('записан', os.path.relpath(path, OUT + '/../../..'))
