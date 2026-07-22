//! Prime Radiant — the golden-path navigator over Γ ∈ D(ℂ⁷).
//!
//!   prime-radiant             the TUI (ratatui)
//!   prime-radiant --selftest  headless: run the calibration battery + a
//!                             sample reading; exit code 1 if anything fails

mod calib;
mod demo;
mod estimator;
mod holon;
mod interpret;
mod model;
mod navigate;
mod pair;
mod sensor_git;
mod ui;

use holon::*;
use navigate::*;

fn selftest() -> i32 {
    println!("PRIME RADIANT (rust) — selftest: every symbol earns its number\n");
    let hs = calib::run_calibration();
    let mut failed = 0;
    for h in &hs {
        let mark = match h.pass {
            Some(true) => "ok ",
            Some(false) => {
                failed += 1;
                "REF"
            }
            None => "···",
        };
        println!("  {} [{}] {}  ({})", h.id, mark, h.claim, h.evidence);
    }
    let passed = hs.iter().filter(|h| h.pass == Some(true)).count();
    println!("\n  {} hypotheses: {} VERIFIED, {} REFUTED", hs.len(), passed, failed);

    // cross-language anchor: the deterministic attractor from the scrambled Source
    let rho = make_selfmodel(0.42);
    let p_star = attractor_p(0.2, 1.0, 2000, &rho);
    println!(
        "  deterministic attractor from the Source: P* = {:.4} (python reference ≈ 0.321; window (0.2857, 0.4286])",
        p_star
    );

    // a sample reading in the Mind model
    let mut rng = <rand::rngs::StdRng as rand::SeedableRng>::seed_from_u64(11);
    let mut g = rand_state(&mut rng, 0.30);
    for _ in 0..400 {
        g = tick_std(&g, &rho);
    }
    let mdl = model::model(model::Domain::Mind);
    let r = interpret::read(&g, &mdl);
    println!("\n  sample reading (Mind model), after 400 ticks from fog:");
    println!("    {}", r.verdict);
    println!("    strongest line: {}", r.strongest_line);
    println!("    {}", r.pain);

    if failed == 0 && p_star > P_CRIT && p_star <= P_UPPER {
        println!("\n  SELFTEST PASSED");
        0
    } else {
        println!("\n  SELFTEST FAILED");
        1
    }
}

const USAGE: &str = "prime-radiant                     the TUI (ratatui)
prime-radiant --selftest          headless verification battery
prime-radiant demo blind          blind axis-diagnosis through the 7 lines (confusion matrix)
prime-radiant demo calibration    the oracle's predictions vs fresh realizations (Brier)
prime-radiant demo bench          navigation benchmark vs baselines (same starts)
prime-radiant demo maxim          «no own goal → part of another's» — decomposed and measured
prime-radiant demo estimator      the [K] organ: track a hidden holon through noise (vs baselines)
prime-radiant sense-git [--repo P] [--window N]   the domain sensor: a git repo as an external system
prime-radiant checkup --scores 7,5,4,6,3,2,5 [--coh AE=0.4,OU=-0.2] [--model mind|team|llm|market|universal]";

fn main() {
    let args: Vec<String> = std::env::args().collect();
    if args.iter().any(|a| a == "--selftest") {
        std::process::exit(selftest());
    }
    if args.iter().any(|a| a == "--help" || a == "-h") {
        println!("{}", USAGE);
        return;
    }
    if args.get(1).map(|s| s.as_str()) == Some("demo") {
        match args.get(2).map(|s| s.as_str()) {
            Some("blind") => demo::blind_diagnosis(200, 71),
            Some("calibration") => demo::oracle_calibration(6, 40, 72),
            Some("bench") => demo::navigate_bench(30, 73),
            Some("maxim") => demo::maxim(74),
            Some("estimator") => demo::estimator_demo(),
            _ => println!("{}", USAGE),
        }
        return;
    }
    if args.get(1).map(|s| s.as_str()) == Some("sense-git") {
        let mut repo = ".".to_string();
        let mut win = 20usize;
        let mut i = 2;
        while i < args.len() {
            match args[i].as_str() {
                "--repo" => {
                    i += 1;
                    repo = args.get(i).cloned().unwrap_or(".".into());
                }
                "--window" => {
                    i += 1;
                    win = args.get(i).and_then(|v| v.parse().ok()).unwrap_or(20);
                }
                _ => {}
            }
            i += 1;
        }
        if let Err(e) = sensor_git::run(&repo, win) {
            eprintln!("sensor error: {e}");
            std::process::exit(2);
        }
        return;
    }
    if args.get(1).map(|s| s.as_str()) == Some("checkup") {
        if let Err(e) = demo::run_checkup_cli(&args[2..]) {
            eprintln!("checkup error: {e}\n{}", USAGE);
            std::process::exit(2);
        }
        return;
    }
    if let Err(e) = ui::run_tui() {
        eprintln!("tui error: {e}");
        std::process::exit(1);
    }
}
