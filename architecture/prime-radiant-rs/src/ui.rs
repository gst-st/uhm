//! The ratatui TUI: seven tabs — Holon dashboard, Atlas, Oracle, Pair,
//! Ensemble, Calibration, Help. Every number on screen is computed live by
//! the same core the selftest verifies.

use crate::calib::{run_calibration, Hypo};
use crate::holon::*;
use crate::interpret::read;
use crate::model::{model, DOMAINS};
use crate::navigate::*;
use crate::pair::*;
use crossterm::event::{self, Event, KeyCode, KeyEventKind};
use ratatui::layout::{Constraint, Direction, Layout, Rect};
use ratatui::style::{Color, Modifier, Style};
use ratatui::text::{Line, Span};
use ratatui::widgets::{Bar, BarChart, BarGroup, Block, Borders, Gauge, Paragraph, Row, Table, Tabs};
use ratatui::Frame;
use rand::rngs::StdRng;
use rand::SeedableRng;
use std::time::Duration;

const TABS: [&str; 8] = ["1 Holon", "2 Atlas", "3 Oracle", "4 Pair", "5 Ensemble", "6 Reading", "7 Calibration", "8 Help"];

pub struct App {
    pub tab: usize,
    pub g: CMat,
    pub rho: CMat,
    pub g_d: f64,
    pub kap_gain: f64,
    pub bold: bool,
    pub paused: bool,
    pub speed: usize, // ticks per frame
    pub tick_count: u64,
    pub dial_idx: usize,
    pub dial_theta: f64,
    // atlas
    pub atlas: Option<Vec<Vec<Cell>>>,
    pub atlas_gds: Vec<f64>,
    pub atlas_kaps: Vec<f64>,
    pub atlas_cur: (usize, usize),
    // oracle
    pub oracle_timid: Option<(f64, f64, f64)>,
    pub oracle_bold: Option<(f64, f64, f64)>,
    pub oracle_start: CMat,
    pub oracle_progress: Option<(bool, usize, usize, usize)>, // (bold, done, total, wins)
    pub oracle_rng: StdRng,
    // pair
    pub pair_g1: CMat,
    pub pair_g2: CMat,
    pub pair_eps: f64,
    // ensemble
    pub ens: Vec<CMat>,
    pub ens_ids: Vec<CMat>,
    pub ens_steps: u64,
    // calibration
    pub calib: Option<Vec<Hypo>>,
    pub domain_idx: usize,
    pub quit: bool,
}

impl App {
    pub fn new() -> Self {
        let rho = make_selfmodel(0.42);
        let mut rng = StdRng::seed_from_u64(11);
        let fog = rand_state(&mut rng, 0.30);
        let mut rp = StdRng::seed_from_u64(29);
        let (p1, p2) = (rand_state(&mut rp, 0.6), rand_state(&mut rp, 0.6));
        let mut re = StdRng::seed_from_u64(21);
        let ens: Vec<CMat> = (0..48).map(|_| rand_state(&mut re, 0.5)).collect();
        let ens_ids: Vec<CMat> = (0..48).map(|_| rand_selfmodel(&mut re, 0.42)).collect();
        App {
            tab: 0,
            g: fog.clone(),
            rho,
            g_d: 0.2,
            kap_gain: 1.0,
            bold: false,
            paused: false,
            speed: 4,
            tick_count: 0,
            dial_idx: 0,
            dial_theta: 0.15,
            atlas: None,
            atlas_gds: vec![0.05, 0.15, 0.25, 0.35, 0.45, 0.55, 0.65],
            atlas_kaps: vec![0.0, 0.2, 0.6, 1.0, 1.5, 2.0, 2.5, 3.0],
            atlas_cur: (2, 3),
            oracle_timid: None,
            oracle_bold: None,
            oracle_start: fog,
            oracle_progress: None,
            oracle_rng: StdRng::seed_from_u64(5),
            pair_g1: p1,
            pair_g2: p2,
            pair_eps: 1e-3,
            ens,
            ens_ids,
            ens_steps: 0,
            calib: None,
            domain_idx: 0,
            quit: false,
        }
    }

    pub fn step(&mut self) {
        if !self.paused {
            let gain = if self.bold { 3.0 * self.kap_gain } else { self.kap_gain };
            for _ in 0..self.speed {
                self.g = tick(&self.g, &self.rho, 0.01, self.g_d, gain);
                self.tick_count += 1;
            }
            if self.tab == 4 {
                for _ in 0..1 {
                    self.ens = self
                        .ens
                        .iter()
                        .zip(self.ens_ids.iter())
                        .map(|(g, id)| tick_std(g, id))
                        .collect();
                    self.ens_steps += 1;
                }
            }
        }
        // chunked oracle
        if let Some((bold, done, total, wins)) = self.oracle_progress {
            let chunk = 3usize.min(total - done);
            let mut w = wins;
            for d in 0..chunk {
                let (p, _, _) = solitaire(&self.oracle_start, &self.rho, 1, 70, bold, 5 + (done + d) as u64);
                if p > 0.5 {
                    w += 1;
                }
            }
            let nd = done + chunk;
            if nd >= total {
                let res = (w as f64 / total as f64, 0.0, f64::NAN);
                if bold {
                    self.oracle_bold = Some(res);
                } else {
                    self.oracle_timid = Some(res);
                }
                self.oracle_progress = None;
            } else {
                self.oracle_progress = Some((bold, nd, total, w));
            }
        }
    }

    pub fn on_key(&mut self, code: KeyCode) {
        match code {
            KeyCode::Char('q') => self.quit = true,
            KeyCode::Tab => self.tab = (self.tab + 1) % TABS.len(),
            KeyCode::Char(c @ '1'..='8') => self.tab = c as usize - '1' as usize,
            KeyCode::Char(' ') => self.paused = !self.paused,
            KeyCode::Char('+') | KeyCode::Char('=') => self.speed = (self.speed + 1).min(64),
            KeyCode::Char('-') => self.speed = self.speed.saturating_sub(1).max(1),
            KeyCode::Char('b') => self.bold = !self.bold,
            KeyCode::Char('m') => {
                self.domain_idx = (self.domain_idx + 1) % DOMAINS.len();
                let mdl = model(DOMAINS[self.domain_idx]);
                self.g_d = mdl.g_d;
                self.kap_gain = mdl.kap_gain;
            }
            KeyCode::Char('r') => {
                let mut rng = StdRng::seed_from_u64(11);
                self.g = rand_state(&mut rng, 0.30);
                self.tick_count = 0;
            }
            KeyCode::Char('s') => {
                self.g = source();
                self.tick_count = 0;
            }
            KeyCode::Char('[') => self.dial_idx = (self.dial_idx + 20) % 21,
            KeyCode::Char(']') => self.dial_idx = (self.dial_idx + 1) % 21,
            KeyCode::Char(',') => {
                let (i, j) = dial_pairs()[self.dial_idx];
                self.g = dial(&self.g, i, j, -self.dial_theta);
            }
            KeyCode::Char('.') => {
                let (i, j) = dial_pairs()[self.dial_idx];
                self.g = dial(&self.g, i, j, self.dial_theta);
            }
            _ => {}
        }
        match self.tab {
            1 => match code {
                KeyCode::Left => self.atlas_cur.1 = self.atlas_cur.1.saturating_sub(1),
                KeyCode::Right => self.atlas_cur.1 = (self.atlas_cur.1 + 1).min(self.atlas_kaps.len() - 1),
                KeyCode::Up => self.atlas_cur.0 = self.atlas_cur.0.saturating_sub(1),
                KeyCode::Down => self.atlas_cur.0 = (self.atlas_cur.0 + 1).min(self.atlas_gds.len() - 1),
                KeyCode::Enter => {
                    self.g_d = self.atlas_gds[self.atlas_cur.0];
                    self.kap_gain = self.atlas_kaps[self.atlas_cur.1];
                }
                KeyCode::Char('a') => {
                    self.atlas = Some(phase_atlas(&self.atlas_gds, &self.atlas_kaps, 400, &self.rho));
                }
                _ => {}
            },
            2 => match code {
                KeyCode::Char('t') => {
                    self.oracle_start = self.g.clone();
                    self.oracle_progress = Some((false, 0, 60, 0));
                }
                KeyCode::Char('o') => {
                    self.oracle_start = self.g.clone();
                    self.oracle_progress = Some((true, 0, 60, 0));
                }
                _ => {}
            },
            3 => match code {
                KeyCode::Char('e') => self.pair_eps = (self.pair_eps / 2.0).max(1e-5),
                KeyCode::Char('E') => self.pair_eps = (self.pair_eps * 2.0).min(3e-3),
                KeyCode::Char('n') => {
                    let mut rp = StdRng::seed_from_u64(self.tick_count.wrapping_mul(97) + 1);
                    self.pair_g1 = rand_state(&mut rp, 0.6);
                    self.pair_g2 = rand_state(&mut rp, 0.6);
                }
                _ => {}
            },
            4 => {
                if code == KeyCode::Char('n') {
                    let mut re = StdRng::seed_from_u64(self.tick_count.wrapping_mul(31) + 7);
                    self.ens = (0..48).map(|_| rand_state(&mut re, 0.5)).collect();
                    self.ens_ids = (0..48).map(|_| rand_selfmodel(&mut re, 0.42)).collect();
                    self.ens_steps = 0;
                }
            }
            6 => {
                if code == KeyCode::Char('c') {
                    self.calib = Some(run_calibration());
                }
            }
            _ => {}
        }
    }

    pub fn current_model(&self) -> crate::model::Model {
        model(DOMAINS[self.domain_idx])
    }
}

fn heat_color(v: f64, vmax: f64) -> Color {
    let t = (v / vmax.max(1e-9)).clamp(0.0, 1.0);
    let r = (30.0 + 200.0 * t * t) as u8;
    let g = (30.0 + 160.0 * t) as u8;
    let b = (60.0 + 195.0 * (1.0 - (1.0 - t).powi(2))) as u8;
    Color::Rgb(r, g, b)
}

fn sigma_color(v: f64) -> Color {
    if v >= 1.0 {
        Color::Red
    } else if v >= 0.8 {
        Color::LightRed
    } else if v >= 0.5 {
        Color::Yellow
    } else {
        Color::Green
    }
}

pub fn draw(f: &mut Frame, app: &App) {
    let outer = Layout::default()
        .direction(Direction::Vertical)
        .constraints([Constraint::Length(1), Constraint::Min(5), Constraint::Length(1)])
        .split(f.area());
    let tabs = Tabs::new(TABS.iter().map(|t| Line::from(*t)))
        .select(app.tab)
        .highlight_style(Style::default().fg(Color::Cyan).add_modifier(Modifier::BOLD));
    f.render_widget(tabs, outer[0]);

    match app.tab {
        0 => draw_holon(f, outer[1], app),
        1 => draw_atlas(f, outer[1], app),
        2 => draw_oracle(f, outer[1], app),
        3 => draw_pair(f, outer[1], app),
        4 => draw_ensemble(f, outer[1], app),
        5 => draw_reading(f, outer[1], app),
        6 => draw_calib(f, outer[1], app),
        _ => draw_help(f, outer[1]),
    }

    let status = format!(
        " tick {}  model: {}  gD={:.2} κ={:.1}{}  speed {}  {}  |  m model · space pause · b bold · [ ] , . dial · r fog · s Source · q quit",
        app.tick_count,
        app.current_model().name,
        app.g_d,
        app.kap_gain,
        if app.bold { "×3 BOLD" } else { "" },
        app.speed,
        if app.paused { "PAUSED" } else { "RUN" }
    );
    f.render_widget(
        Paragraph::new(status).style(Style::default().fg(Color::DarkGray)),
        outer[2],
    );
}

fn draw_holon(f: &mut Frame, area: Rect, app: &App) {
    let cols = Layout::default()
        .direction(Direction::Horizontal)
        .constraints([Constraint::Length(38), Constraint::Min(30)])
        .split(area);

    // --- left: |Γ| heatmap ---
    let vmax = app
        .g
        .a
        .iter()
        .map(|v| v.norm())
        .fold(0.0f64, f64::max);
    let mut lines: Vec<Line> = Vec::new();
    let mut header = vec![Span::raw("    ")];
    for j in 0..N {
        header.push(Span::styled(format!(" {}  ", AXES[j]), Style::default().fg(Color::Cyan)));
    }
    lines.push(Line::from(header));
    for i in 0..N {
        let mut spans = vec![Span::styled(format!(" {}  ", AXES[i]), Style::default().fg(Color::Cyan))];
        for j in 0..N {
            let v = app.g[(i, j)].norm();
            spans.push(Span::styled("    ", Style::default().bg(heat_color(v, vmax))));
        }
        lines.push(Line::from(spans));
        lines.push(Line::from(""));
    }
    let (di, dj) = dial_pairs()[app.dial_idx];
    lines.push(Line::from(format!(
        " dial plane: ({},{})  θ={:.2}   degraded lines: {}",
        AXES[di], AXES[dj], app.dial_theta, degraded_lines(&app.g, 5e-3)
    )));
    f.render_widget(
        Paragraph::new(lines).block(Block::default().borders(Borders::ALL).title(" |Γ| — the chord ")),
        cols[0],
    );

    // --- right: observables + window gauge + σ-panel ---
    let right = Layout::default()
        .direction(Direction::Vertical)
        .constraints([
            Constraint::Length(6),
            Constraint::Length(3),
            Constraint::Min(9),
        ])
        .split(cols[1]);
    let ob = observables(&app.g);
    let obs_text = vec![
        Line::from(format!(
            " P = {:.4}   R = 1/(7P) = {:.4}   Φ = {:.4}", ob.p, ob.r, ob.phi
        )),
        Line::from(format!(
            " C = Φ·R = {:.4}   S = {:.4}   D_diff = e^S = {:.3}", ob.c, ob.s, ob.d_diff
        )),
        Line::from(format!(" Coh_E = {:.4}   κ₀ = {:.4}  (κ_boot = 1/7)", ob.coh_e, kappa0(&app.g))),
        Line::from(Span::styled(
            format!(
                " {}   window (2/7, 3/7] = (0.2857, 0.4286]",
                if ob.viable { "VIABLE — inside the window" } else { "outside the window" }
            ),
            Style::default().fg(if ob.viable { Color::Green } else { Color::Red }),
        )),
    ];
    f.render_widget(
        Paragraph::new(obs_text).block(Block::default().borders(Borders::ALL).title(" observables ")),
        right[0],
    );
    let frac = ((ob.p - 1.0 / 7.0) / (1.0 - 1.0 / 7.0)).clamp(0.0, 1.0);
    f.render_widget(
        Gauge::default()
            .block(Block::default().borders(Borders::ALL).title(" P: grey 1/7 → wall 2/7 → window → 3/7 "))
            .ratio(frac)
            .gauge_style(Style::default().fg(if ob.viable { Color::Green } else { Color::Yellow })),
        right[1],
    );
    let sp = stress_panel(&app.g);
    let sig_lines: Vec<Line> = (0..N)
        .map(|k| {
            let v = sp[k];
            let w = ((v.clamp(-0.5, 1.5) + 0.5) / 2.0 * 24.0) as usize;
            Line::from(vec![
                Span::styled(format!(" σ_{} ", AXES[k]), Style::default().fg(Color::Cyan)),
                Span::styled(format!("{:+.2} ", v), Style::default().fg(sigma_color(v))),
                Span::styled("█".repeat(w), Style::default().fg(sigma_color(v))),
            ])
        })
        .collect();
    f.render_widget(
        Paragraph::new(sig_lines).block(
            Block::default()
                .borders(Borders::ALL)
                .title(" σ-panel (T-92): viable ⇔ every bar < 1 "),
        ),
        right[2],
    );
}

fn draw_atlas(f: &mut Frame, area: Rect, app: &App) {
    let mut lines: Vec<Line> = Vec::new();
    lines.push(Line::from(
        " a: compute atlas · arrows: cursor · Enter: set (gD, κ) for the holon",
    ));
    lines.push(Line::from(""));
    let mut hdr = vec![Span::raw("  gD\\κ  ")];
    for k in &app.atlas_kaps {
        hdr.push(Span::styled(format!("{:5.1}", k), Style::default().fg(Color::Cyan)));
    }
    lines.push(Line::from(hdr));
    match &app.atlas {
        Some(rows) => {
            for (ri, row) in rows.iter().enumerate() {
                let mut spans = vec![Span::styled(
                    format!("  {:4.2}  ", app.atlas_gds[ri]),
                    Style::default().fg(Color::Cyan),
                )];
                for (ci, cell) in row.iter().enumerate() {
                    let (txt, color) = match cell {
                        Cell::Grey => ("  ·  ", Color::DarkGray),
                        Cell::Window => ("  W  ", Color::Green),
                        Cell::Crystal => ("  #  ", Color::Blue),
                    };
                    let style = if (ri, ci) == app.atlas_cur {
                        Style::default().fg(Color::Black).bg(Color::Yellow)
                    } else {
                        Style::default().fg(color)
                    };
                    spans.push(Span::styled(txt, style));
                }
                lines.push(Line::from(spans));
            }
            lines.push(Line::from(""));
            lines.push(Line::from(" · grey (P ≤ 2/7)   W window   # crystal (P > 3/7)"));
            lines.push(Line::from(" the κ=0 column is all grey: no supply, no being"));
        }
        None => lines.push(Line::from(" (press 'a' — ~1 s of computation)")),
    }
    f.render_widget(
        Paragraph::new(lines).block(
            Block::default()
                .borders(Borders::ALL)
                .title(" phase atlas: the Goldilocks band of being "),
        ),
        area,
    );
}

fn draw_oracle(f: &mut Frame, area: Rect, app: &App) {
    let mut lines = vec![
        Line::from(" t: run 60 timid deals from the CURRENT Γ · o: run 60 bold deals (25% κ-boosts)"),
        Line::from(" the deal decides nothing — it MEASURES the basin (horizon 70 ticks)"),
        Line::from(""),
    ];
    if let Some((bold, done, total, wins)) = app.oracle_progress {
        lines.push(Line::from(format!(
            " running {} decks: {}/{}  wins so far {}",
            if bold { "BOLD" } else { "timid" },
            done,
            total,
            wins
        )));
    }
    if let Some((p, _, _)) = app.oracle_timid {
        lines.push(Line::from(Span::styled(
            format!(" timid decks:  p_golden = {:5.1}%   (± {:.1}% binomial)", 100.0 * p, 100.0 * (p * (1.0 - p) / 60.0).sqrt()),
            Style::default().fg(Color::Yellow),
        )));
    }
    if let Some((p, _, _)) = app.oracle_bold {
        lines.push(Line::from(Span::styled(
            format!(" bold decks:   p_golden = {:5.1}%   (± {:.1}% binomial)", 100.0 * p, 100.0 * (p * (1.0 - p) / 60.0).sqrt()),
            Style::default().fg(Color::Green),
        )));
    }
    if let (Some((pt, _, _)), Some((pb, _, _))) = (app.oracle_timid, app.oracle_bold) {
        lines.push(Line::from(""));
        lines.push(Line::from(format!(
            " fortune favours the bold: Δp = {:+.1}%  — because basins do",
            100.0 * (pb - pt)
        )));
    }
    f.render_widget(
        Paragraph::new(lines).block(Block::default().borders(Borders::ALL).title(" the Dee solitaire oracle ")),
        area,
    );
}

fn draw_pair(f: &mut Frame, area: Rect, app: &App) {
    let pg = pair_gain(&app.pair_g1, &app.pair_g2, 0, 4, 1, 5, app.pair_eps);
    let p1 = purity(&app.pair_g1);
    let p2 = purity(&app.pair_g2);
    let lines = vec![
        Line::from(" n: new random pair · e/E: bridge ε down/up"),
        Line::from(""),
        Line::from(format!(" P₁ = {:.4}   P₂ = {:.4}   product P₁P₂ = {:.4}", p1, p2, p1 * p2)),
        Line::from(format!(" bridge (A↔E)⊗(S↔O), ε = {:.1e}", app.pair_eps)),
        Line::from(""),
        Line::from(format!(" ΔP measured   = {:+.3e}", pg.d_p)),
        Line::from(format!("   linear term  = {:+.3e}", pg.linear)),
        Line::from(format!("   2ε²|γ|² term = {:+.3e}   (law residual {:.1e})", pg.quadratic,
            (pg.d_p - pg.linear - pg.quadratic).abs())),
        Line::from(format!(" PSD min eig   = {:+.1e}", pg.psd_min)),
        Line::from(Span::styled(
            format!(" reduced-state change |dΓ₁|,|dΓ₂| ≤ {:.1e}  — the gain lives in the BOND", pg.reduced_delta),
            Style::default().fg(Color::Green),
        )),
        Line::from(""),
        Line::from(" T-77: the increment of connection is never negative, and it is stored"),
        Line::from(" in the bond itself — neither member holds it (H47–H49)."),
    ];
    f.render_widget(
        Paragraph::new(lines).block(Block::default().borders(Borders::ALL).title(" pair space D(C⁴⁹): the bond ")),
        area,
    );
}

fn draw_ensemble(f: &mut Frame, area: Rect, app: &App) {
    let rows = Layout::default()
        .direction(Direction::Vertical)
        .constraints([Constraint::Length(6), Constraint::Min(6)])
        .split(area);
    let ps: Vec<f64> = app.ens.iter().map(purity).collect();
    let mean = ps.iter().sum::<f64>() / ps.len() as f64;
    let var = ps.iter().map(|p| (p - mean).powi(2)).sum::<f64>() / ps.len() as f64;
    let mut dsum = 0.0;
    let mut cnt = 0;
    for i in 0..app.ens.len().min(12) {
        for j in (i + 1)..app.ens.len().min(12) {
            dsum += app.ens[i].sub(&app.ens[j]).frob_norm();
            cnt += 1;
        }
    }
    let text = vec![
        Line::from(format!(" {} holons, personal ρ*ᵢ · steps {} · n: reinit", app.ens.len(), app.ens_steps)),
        Line::from(format!(" WHERE: mean P = {:.4}, std = {:.4}  (compresses — predictable)", mean, var.sqrt())),
        Line::from(format!(" WHO:   mean pairwise |Γᵢ−Γⱼ| = {:.3}   (stays distinct — identity survives)",
            dsum / cnt.max(1) as f64)),
        Line::from(" psychohistory for ensembles; navigation for persons — the freedom kernel forbids a point oracle"),
    ];
    f.render_widget(
        Paragraph::new(text).block(Block::default().borders(Borders::ALL).title(" ensemble (psychohistory limit) ")),
        rows[0],
    );
    // histogram of P over [1/7, 0.5]
    let bins = 16usize;
    let mut hist = vec![0u64; bins];
    for &p in &ps {
        let t = ((p - 1.0 / 7.0) / (0.5 - 1.0 / 7.0)).clamp(0.0, 0.999);
        hist[(t * bins as f64) as usize] += 1;
    }
    let labels: Vec<String> = (0..bins)
        .map(|b| format!("{:.2}", 1.0 / 7.0 + (b as f64 + 0.5) / bins as f64 * (0.5 - 1.0 / 7.0)))
        .collect();
    let bars: Vec<Bar> = hist
        .iter()
        .zip(labels.iter())
        .map(|(&v, l)| {
            let in_window = {
                let x: f64 = l.parse().unwrap_or(0.0);
                x > P_CRIT && x <= P_UPPER
            };
            Bar::default()
                .value(v)
                .label(Line::from(l.clone()))
                .style(Style::default().fg(if in_window { Color::Green } else { Color::Gray }))
        })
        .collect();
    f.render_widget(
        BarChart::default()
            .block(Block::default().borders(Borders::ALL).title(" P distribution (green = the window) "))
            .bar_width(4)
            .bar_gap(1)
            .data(BarGroup::default().bars(&bars)),
        rows[1],
    );
}

fn draw_reading(f: &mut Frame, area: Rect, app: &App) {
    let mdl = app.current_model();
    let r = read(&app.g, &mdl);
    let mut lines: Vec<Line> = Vec::new();
    lines.push(Line::from(Span::styled(
        format!(" {}", r.verdict),
        Style::default().add_modifier(Modifier::BOLD),
    )));
    lines.push(Line::from(format!(" application model: {}  (m to cycle)", mdl.name)));
    lines.push(Line::from(""));
    lines.push(Line::from(Span::styled(" populations — who is loud:", Style::default().fg(Color::Cyan))));
    for p in &r.populations {
        lines.push(Line::from(format!("   {}", p)));
    }
    lines.push(Line::from(""));
    lines.push(Line::from(Span::styled(" carrying coherences — the signal between the voices:", Style::default().fg(Color::Cyan))));
    for c in &r.carrying {
        lines.push(Line::from(format!("   {}", c)));
    }
    for c in &r.faint {
        lines.push(Line::from(Span::styled(format!("   {}", c), Style::default().fg(Color::DarkGray))));
    }
    lines.push(Line::from(""));
    lines.push(Line::from(format!(" strongest line: {}", r.strongest_line)));
    lines.push(Line::from(Span::styled(format!(" {}", r.pain), Style::default().fg(Color::Yellow))));
    lines.push(Line::from(""));
    for chunk in r.hierarchy_note.split(". ") {
        lines.push(Line::from(Span::styled(format!(" {}", chunk), Style::default().fg(Color::DarkGray))));
    }
    f.render_widget(
        Paragraph::new(lines)
            .wrap(ratatui::widgets::Wrap { trim: false })
            .block(Block::default().borders(Borders::ALL).title(" Reading (the П2 protocol): Γ interpreted in the current model ")),
        area,
    );
}

fn draw_calib(f: &mut Frame, area: Rect, app: &App) {
    match &app.calib {
        None => {
            f.render_widget(
                Paragraph::new(" press 'c' to run the battery (~2 s): every symbol earns its number")
                    .block(Block::default().borders(Borders::ALL).title(" categorical calibration ")),
                area,
            );
        }
        Some(hs) => {
            let passed = hs.iter().filter(|h| h.pass == Some(true)).count();
            let failed = hs.iter().filter(|h| h.pass == Some(false)).count();
            let rows: Vec<Row> = hs
                .iter()
                .map(|h| {
                    let (mark, color) = match h.pass {
                        Some(true) => ("ok", Color::Green),
                        Some(false) => ("REF", Color::Red),
                        None => ("···", Color::DarkGray),
                    };
                    Row::new(vec![
                        h.id.to_string(),
                        mark.to_string(),
                        h.claim.to_string(),
                        h.evidence.clone(),
                    ])
                    .style(Style::default().fg(color))
                })
                .collect();
            let table = Table::new(
                rows,
                [
                    Constraint::Length(4),
                    Constraint::Length(4),
                    Constraint::Percentage(55),
                    Constraint::Percentage(35),
                ],
            )
            .header(Row::new(vec!["id", "", "claim", "evidence"]).style(Style::default().add_modifier(Modifier::BOLD)))
            .block(Block::default().borders(Borders::ALL).title(format!(
                " calibration: {} hypotheses — {} VERIFIED, {} REFUTED ",
                hs.len(),
                passed,
                failed
            )));
            f.render_widget(table, area);
        }
    }
}

fn draw_help(f: &mut Frame, area: Rect) {
    let text = vec![
        Line::from(" PRIME RADIANT — the golden-path navigator over Γ ∈ D(C⁷)"),
        Line::from(""),
        Line::from(" 1 Holon      live Γ heatmap, observables P R Φ C S D_diff, σ-panel, window gauge"),
        Line::from(" 2 Atlas      the (dissipation, supply) basin map; Enter sets the holon's params"),
        Line::from(" 3 Oracle     the Dee solitaire: p_golden of timid vs bold decks from the current Γ"),
        Line::from(" 4 Pair       D(C⁴⁹): the T-77 bond — ΔP law live, reduced states untouched"),
        Line::from(" 5 Ensemble   psychohistory: WHERE compresses, WHO stays distinct"),
        Line::from(" 6 Reading    the П2 interpretation: named populations, carrying coherences, prescription"),
        Line::from(" 7 Calibration  the hypothesis battery — press c"),
        Line::from(" m            cycle the application model: Universal · Mind · Team · LLM agent · Market"),
        Line::from(""),
        Line::from(" global: space pause · +/- speed · b bold (κ×3) · [ ] choose dial · , . rotate"),
        Line::from("         r reset to fog · s reset to the Source · q quit"),
        Line::from(""),
        Line::from(" every number on screen is computed by the same core `--selftest` verifies;"),
        Line::from(" the physics: one tick  Γ ← U[Γ + dt(g_D(I/7−Γ) + κ(ρ*−Γ))]U,  κ = 1.2(1+8·Coh_E)"),
        Line::from(" solve et coagula — the dissolver and the binder — and the dials to choose the chord."),
    ];
    f.render_widget(
        Paragraph::new(text).block(Block::default().borders(Borders::ALL).title(" help ")),
        area,
    );
}

pub fn run_tui() -> std::io::Result<()> {
    let mut terminal = ratatui::init();
    let mut app = App::new();
    loop {
        app.step();
        terminal.draw(|f| draw(f, &app))?;
        if event::poll(Duration::from_millis(50))? {
            if let Event::Key(key) = event::read()? {
                if key.kind == KeyEventKind::Press {
                    app.on_key(key.code);
                }
            }
        }
        if app.quit {
            break;
        }
    }
    ratatui::restore();
    Ok(())
}
