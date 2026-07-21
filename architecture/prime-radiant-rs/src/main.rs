//! Prime Radiant — the golden-path navigator over Γ ∈ D(ℂ⁷).
//!
//!   prime-radiant             the TUI (ratatui)
//!   prime-radiant --selftest  headless: run the calibration battery + a
//!                             sample reading; exit code 1 if anything fails

mod calib;
mod holon;
mod interpret;
mod model;
mod navigate;
mod pair;
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

fn main() {
    let args: Vec<String> = std::env::args().collect();
    if args.iter().any(|a| a == "--selftest") {
        std::process::exit(selftest());
    }
    if let Err(e) = ui::run_tui() {
        eprintln!("tui error: {e}");
        std::process::exit(1);
    }
}
