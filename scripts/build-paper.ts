#!/usr/bin/env bun
/**
 * build-paper.ts — Build the UHM paper PDF or package for preprint servers
 *
 * Usage:
 *   bun scripts/build-paper.ts             Build PDF to paper/uhm-paper.pdf
 *   bun scripts/build-paper.ts --arxiv     Package tarball to paper/uhm-arxiv.tar.gz
 *   bun scripts/build-paper.ts --zenodo    Package directory paper/zenodo/
 *   bun scripts/build-paper.ts --help      Show usage
 *
 * PDF mode runs the full LaTeX build pipeline
 *   pdflatex -> bibtex -> pdflatex -> pdflatex
 * (three pdflatex passes + bibtex for cross-references, bibliography, TOC).
 *
 * arXiv mode produces a minimal LaTeX source tarball (main.tex, main.bbl,
 * references.bib, sections/*.tex, figures/*.tex) that arXiv's AutoTeX can
 * re-compile. The pre-compiled main.bbl is included because AutoTeX does
 * not always run BibTeX itself.
 *
 * Zenodo mode produces a deposit-ready folder paper/zenodo/ containing:
 *   - uhm-paper.pdf             (the primary viewable artefact)
 *   - uhm-paper-source.tar.gz   (full LaTeX source for reproducibility)
 *   - zenodo-metadata.json      (metadata payload for Zenodo's form / API)
 *   - README.md                 (build instructions for reviewers)
 * Zenodo assigns a permanent DOI on publication; no category gatekeeping,
 * no endorsement, works natively for interdisciplinary preprints.
 */

import { $ } from "bun";
import { existsSync, readdirSync } from "fs";
import path from "path";

const ROOT = path.resolve(import.meta.dir, "..");
const PAPER_DIR = path.join(ROOT, "paper");
const MAIN_TEX = "main.tex";
const OUTPUT_NAME = "uhm-paper";
const ARXIV_TARBALL = "uhm-arxiv.tar.gz";
const ZENODO_DIR_NAME = "zenodo";

// -------- CLI parsing --------
const args = process.argv.slice(2);
const FLAG_ARXIV = args.includes("--arxiv");
const FLAG_ZENODO = args.includes("--zenodo");
const FLAG_HELP = args.includes("--help") || args.includes("-h");
const KNOWN = new Set(["--arxiv", "--zenodo", "--help", "-h"]);
const UNKNOWN = args.filter((a) => !KNOWN.has(a));

function showUsage(): void {
  console.log(
    `
Usage: bun scripts/build-paper.ts [options]

Options:
  (no options)    Build the paper PDF to paper/${OUTPUT_NAME}.pdf
  --arxiv         Package an arXiv-ready tarball to paper/${ARXIV_TARBALL}
  --zenodo        Package a Zenodo-ready folder to paper/${ZENODO_DIR_NAME}/
  --help, -h      Show this help message

Preprint destinations:
  arXiv   — minimal LaTeX source tarball (AutoTeX recompiles on upload)
  Zenodo  — compiled PDF + source archive + metadata (permanent DOI, no gate)
`.trim(),
  );
}

// -------- Shared helpers --------
async function run(cmd: string, label: string): Promise<boolean> {
  console.log(`  ⏳ ${label}...`);
  const start = performance.now();
  const result = await $`cd ${PAPER_DIR} && ${cmd.split(" ")}`.quiet().nothrow();
  const elapsed = ((performance.now() - start) / 1000).toFixed(1);

  if (result.exitCode !== 0) {
    // pdflatex returns non-zero on warnings too — only stop on fatals
    const stderr = result.stderr.toString();
    const stdout = result.stdout.toString();
    const hasFatalError =
      stderr.includes("Fatal error") ||
      stdout.includes("No pages of output") ||
      stdout.includes("Emergency stop");
    if (hasFatalError) {
      console.error(`  ❌ ${label} failed (${elapsed}s)`);
      console.error(stderr.slice(0, 500));
      return false;
    }
  }

  console.log(`  ✅ ${label} (${elapsed}s)`);
  return true;
}

async function checkPrereqs(): Promise<void> {
  if (!existsSync(path.join(PAPER_DIR, MAIN_TEX))) {
    console.error(`❌ ${MAIN_TEX} not found in ${PAPER_DIR}`);
    process.exit(1);
  }
  const which = await $`which pdflatex`.quiet().nothrow();
  if (which.exitCode !== 0) {
    console.error(
      "❌ pdflatex not found. Install TeX Live (e.g. `brew install --cask mactex`)",
    );
    process.exit(1);
  }
}

/**
 * Read the page count from pdflatex's .log file. Modern pdflatex compresses
 * the PDF Pages object into a FlateDecode stream, so scanning the .pdf for
 * /Count <N> does not work. The .log file, on the other hand, always ends
 * with a human-readable line such as
 *   "Output written on uhm-paper.pdf (60 pages, 1154617 bytes)."
 * This must be called BEFORE cleanup() removes the .log file.
 */
async function countPagesFromLog(jobname: string): Promise<number> {
  const logPath = path.join(PAPER_DIR, `${jobname}.log`);
  if (!existsSync(logPath)) return 0;
  const text = await Bun.file(logPath).text();
  const match = text.match(/Output written on [^\s(]+\s*\((\d+) pages?/);
  return match ? parseInt(match[1], 10) : 0;
}

/**
 * Remove LaTeX build artefacts for both jobnames (`uhm-paper.*` and `main.*`).
 * Does NOT touch `.tex`/`.bib`/`.pdf` sources or packaged outputs.
 */
async function cleanup(): Promise<number> {
  const jobnames = [OUTPUT_NAME, "main"];
  const extensions = [
    "aux",
    "log",
    "out",
    "toc",
    "lof",
    "lot",
    "bbl",
    "blg",
    "bcf",
    "run.xml",
    "fls",
    "fdb_latexmk",
    "synctex.gz",
    "nav",
    "snm",
    "vrb",
  ];

  let cleaned = 0;
  for (const jobname of jobnames) {
    for (const ext of extensions) {
      const file = path.join(PAPER_DIR, `${jobname}.${ext}`);
      if (existsSync(file)) {
        await $`rm ${file}`.quiet().nothrow();
        cleaned++;
      }
    }
  }
  return cleaned;
}

/**
 * Collect the explicit list of source files (sections/*.tex + figures/*.tex),
 * sorted, relative to PAPER_DIR. Used by both arXiv and Zenodo packaging.
 */
function collectSourceFiles(): { sections: string[]; figures: string[] } {
  const sections = readdirSync(path.join(PAPER_DIR, "sections"))
    .filter((f) => f.endsWith(".tex"))
    .sort()
    .map((f) => `sections/${f}`);

  const figures = readdirSync(path.join(PAPER_DIR, "figures"))
    .filter((f) => f.endsWith(".tex"))
    .sort()
    .map((f) => `figures/${f}`);

  return { sections, figures };
}

// -------- PDF build mode --------
async function buildPdf(): Promise<string> {
  console.log("\n📄 Building UHM paper\n");
  console.log(`  Source: ${PAPER_DIR}/${MAIN_TEX}`);
  console.log(`  Output: ${PAPER_DIR}/${OUTPUT_NAME}.pdf\n`);

  await checkPrereqs();

  const pdflatex = `pdflatex -interaction=nonstopmode -jobname=${OUTPUT_NAME} ${MAIN_TEX}`;
  const bibtex = `bibtex ${OUTPUT_NAME}`;

  if (!(await run(pdflatex, "Pass 1/4 (aux generation)"))) process.exit(1);
  if (!(await run(bibtex, "BibTeX (bibliography)"))) {
    console.log("  ⚠️  BibTeX warnings (non-fatal, continuing)");
  }
  if (!(await run(pdflatex, "Pass 2/4 (bibliography)"))) process.exit(1);
  if (!(await run(pdflatex, "Pass 3/4 (cross-references)"))) process.exit(1);

  const pdfPath = path.join(PAPER_DIR, `${OUTPUT_NAME}.pdf`);
  if (!existsSync(pdfPath)) {
    console.error("\n❌ PDF not generated");
    process.exit(1);
  }

  const size = await Bun.file(pdfPath).size;
  // Read pages BEFORE cleanup() — the .log file is about to be removed.
  const pages = await countPagesFromLog(OUTPUT_NAME);

  console.log(`\n✅ Paper built successfully`);
  console.log(`   📄 ${pdfPath}`);
  console.log(`   📐 ${pages} pages, ${(size / 1024 / 1024).toFixed(1)} MB`);

  return pdfPath;
}

// -------- arXiv packaging mode --------
async function buildArxiv(): Promise<void> {
  console.log("\n📦 Packaging arXiv tarball\n");
  console.log(`  Source: ${PAPER_DIR}/${MAIN_TEX}`);
  console.log(`  Output: ${PAPER_DIR}/${ARXIV_TARBALL}\n`);

  await checkPrereqs();

  // Use the DEFAULT jobname (`main`) so bibtex writes main.bbl — that is the
  // file arXiv's AutoTeX will look for when it re-compiles main.tex.
  const pdflatex = `pdflatex -interaction=nonstopmode ${MAIN_TEX}`;
  const bibtex = "bibtex main";

  if (!(await run(pdflatex, "Pass 1/3 (aux generation)"))) process.exit(1);
  if (!(await run(bibtex, "BibTeX (bibliography)"))) {
    console.log("  ⚠️  BibTeX warnings (non-fatal, continuing)");
  }
  if (!(await run(pdflatex, "Pass 2/3 (verify with .bbl)"))) process.exit(1);

  const bblPath = path.join(PAPER_DIR, "main.bbl");
  if (!existsSync(bblPath)) {
    console.error("❌ main.bbl not generated — arXiv upload would fail");
    process.exit(1);
  }

  const { sections, figures } = collectSourceFiles();
  const files = [
    "main.tex",
    "main.bbl",
    "references.bib",
    ...sections,
    ...figures,
  ];

  for (const f of files) {
    if (!existsSync(path.join(PAPER_DIR, f))) {
      console.error(`❌ Missing file: ${f}`);
      process.exit(1);
    }
  }

  const tarballPath = path.join(PAPER_DIR, ARXIV_TARBALL);
  if (existsSync(tarballPath)) {
    await $`rm ${tarballPath}`.quiet();
  }

  console.log(`  ⏳ Creating tarball (${files.length} files)...`);
  const tarResult =
    await $`cd ${PAPER_DIR} && tar -czf ${ARXIV_TARBALL} ${files}`
      .quiet()
      .nothrow();

  if (tarResult.exitCode !== 0) {
    console.error("❌ tar command failed");
    console.error(tarResult.stderr.toString());
    process.exit(1);
  }

  const tarSize = await Bun.file(tarballPath).size;
  console.log(
    `  ✅ Created ${ARXIV_TARBALL} (${(tarSize / 1024).toFixed(0)} KB)`,
  );

  const cleaned = await cleanup();
  const mainPdf = path.join(PAPER_DIR, "main.pdf");
  if (existsSync(mainPdf)) await $`rm ${mainPdf}`.quiet().nothrow();
  if (cleaned > 0) console.log(`   🧹 Cleaned ${cleaned} auxiliary files`);

  console.log(`\n✅ arXiv package ready`);
  console.log(`   📦 ${tarballPath}`);
  console.log(`   📄 ${files.length} files, ${(tarSize / 1024).toFixed(0)} KB`);
  console.log(`\n📋 Submission checklist:`);
  console.log(`   1. Upload ${ARXIV_TARBALL} at https://arxiv.org/submit`);
  console.log(`   2. Primary category: math-ph (Mathematical Physics)`);
  console.log(`   3. Cross-list: gr-qc, q-bio.NC, physics.hist-ph, cs.AI`);
  console.log(`   4. License: CC BY 4.0 recommended`);
  console.log(`   5. Verify the arXiv-compiled preview (~60 pages, 10 figures)`);
}

// -------- Zenodo packaging mode --------
async function buildZenodo(): Promise<void> {
  console.log("\n📦 Packaging Zenodo deposit\n");
  const zenodoDir = path.join(PAPER_DIR, ZENODO_DIR_NAME);
  console.log(`  Source: ${PAPER_DIR}/${MAIN_TEX}`);
  console.log(`  Output: ${zenodoDir}/\n`);

  // Step 1: Build the PDF (shared with pdf mode). This produces
  // paper/uhm-paper.pdf and runs the full 3x pdflatex + bibtex pipeline.
  const pdfPath = await buildPdf();

  // Step 2: Assemble the source tarball. Zenodo does NOT re-compile LaTeX,
  // so we do not need main.bbl here — Zenodo just archives the files.
  // We include main.tex, references.bib, sections/, figures/, so that any
  // reviewer with pdflatex + bibtex can reproduce the PDF from scratch.
  const { sections, figures } = collectSourceFiles();
  const sourceFiles = [
    "main.tex",
    "references.bib",
    ...sections,
    ...figures,
  ];

  for (const f of sourceFiles) {
    if (!existsSync(path.join(PAPER_DIR, f))) {
      console.error(`❌ Missing file: ${f}`);
      process.exit(1);
    }
  }

  // Step 3: Prepare the zenodo/ output directory (clean re-create).
  if (existsSync(zenodoDir)) {
    await $`rm -rf ${zenodoDir}`.quiet();
  }
  await $`mkdir -p ${zenodoDir}`.quiet();

  // Copy the compiled PDF
  const pdfDest = path.join(zenodoDir, `${OUTPUT_NAME}.pdf`);
  await $`cp ${pdfPath} ${pdfDest}`.quiet();

  // Create the source tarball inside zenodo/
  const sourceTarballName = `${OUTPUT_NAME}-source.tar.gz`;
  const sourceTarballPath = path.join(zenodoDir, sourceTarballName);
  console.log(`\n  ⏳ Creating source archive (${sourceFiles.length} files)...`);
  const tarResult =
    await $`cd ${PAPER_DIR} && tar -czf ${sourceTarballPath} ${sourceFiles}`
      .quiet()
      .nothrow();
  if (tarResult.exitCode !== 0) {
    console.error("❌ tar command failed");
    console.error(tarResult.stderr.toString());
    process.exit(1);
  }
  const sourceTarSize = await Bun.file(sourceTarballPath).size;
  console.log(
    `  ✅ Created ${sourceTarballName} (${(sourceTarSize / 1024).toFixed(0)} KB)`,
  );

  // Write zenodo-metadata.json (compatible with Zenodo REST API /deposit)
  const metadata = buildZenodoMetadata();
  const metadataPath = path.join(zenodoDir, "zenodo-metadata.json");
  await Bun.write(metadataPath, JSON.stringify(metadata, null, 2) + "\n");
  console.log(`  ✅ Wrote zenodo-metadata.json`);

  // Write README.md describing the deposit
  const readmePath = path.join(zenodoDir, "README.md");
  await Bun.write(readmePath, buildZenodoReadme());
  console.log(`  ✅ Wrote README.md`);

  // Step 4: Cleanup LaTeX build artefacts (not the zenodo/ folder)
  const cleaned = await cleanup();
  if (cleaned > 0) console.log(`   🧹 Cleaned ${cleaned} auxiliary files`);

  // Report
  const pdfSize = await Bun.file(pdfDest).size;
  console.log(`\n✅ Zenodo deposit ready`);
  console.log(`   📁 ${zenodoDir}/`);
  console.log(`      ${OUTPUT_NAME}.pdf             (${(pdfSize / 1024 / 1024).toFixed(1)} MB — primary viewable)`);
  console.log(`      ${sourceTarballName}      (${(sourceTarSize / 1024).toFixed(0)} KB — source archive)`);
  console.log(`      zenodo-metadata.json       (Zenodo form / API payload)`);
  console.log(`      README.md                  (reviewer build instructions)`);

  console.log(`\n📋 Submission checklist:`);
  console.log(`   1. Visit https://zenodo.org/deposit/new`);
  console.log(`   2. Upload both files:`);
  console.log(`        - ${OUTPUT_NAME}.pdf (main, viewable)`);
  console.log(`        - ${sourceTarballName} (source archive)`);
  console.log(`   3. Copy fields from zenodo-metadata.json into the form`);
  console.log(`      (title, authors, abstract, keywords, license, related ids)`);
  console.log(`   4. Upload type: Publication → Preprint`);
  console.log(`   5. License: Creative Commons Attribution 4.0 International (CC-BY-4.0)`);
  console.log(`   6. Publish → Zenodo assigns a permanent DOI immediately`);
  console.log(`   7. Add the DOI to holon.sh and any future citations`);
}

/**
 * Zenodo metadata payload — compatible with the REST API `/api/deposit/depositions`
 * and also usable as a field-by-field reference for the web upload form.
 * Only the `metadata` object is the payload; the rest is informational.
 */
function buildZenodoMetadata(): Record<string, unknown> {
  const abstract = `
<p>This paper presents the Unitary Holonomic Monism (UHM) — a mathematical
theory that derives consciousness, quantum mechanics, general relativity, and
the Standard Model structure from a single primitive: the coherence matrix
Γ ∈ D(ℂ⁷). The theory rests on four axioms (Ω⁷) grounded in the Fano plane
and octonion algebra, all four of which are derived as theorems (T-186,
T-187), from which over 180 further theorems follow.</p>

<p>The central result is that consciousness, defined as the internal aspect
of a coherent self-modelling system, is a necessary condition for survival.
The regeneration mechanism opposing entropic decay draws its strength from
E-coherence, proving that philosophical zombies are dynamically impossible
(No-Zombie Theorem). UHM derives specific numerical thresholds: critical
purity P_crit = 2/7, reflection threshold R_th = 1/3, integration threshold
Φ_th = 1, and tricritical exponents α = 1/2, β = 1/4, γ = 1, ν = 1/2,
δ = 5 for the consciousness phase transition. No other theory of
consciousness predicts critical exponents.</p>

<p>The applied layer, Coherence Cybernetics, translates the formalism into
measurable quantities: a 7-dimensional stress tensor, hedonic valence, and
sensorimotor coupling. The theory makes 22 falsifiable predictions, each
with an experimental protocol and explicit falsification criterion. Specific
implications are derived for artificial general intelligence and ethics.
Phase I (digital validation) requires no laboratory equipment. The complete
formalisation is open at https://holon.sh.</p>
`.trim();

  return {
    metadata: {
      title:
        "The Unitary Holonomic Monism (UHM): Deriving Consciousness, Quantum Mechanics, and Spacetime from a Single Primitive",
      upload_type: "publication",
      publication_type: "preprint",
      description: abstract,
      creators: [
        {
          name: "Sereda, Max",
          affiliation: "Independent researcher",
        },
      ],
      keywords: [
        "consciousness",
        "hard problem of consciousness",
        "two-aspect monism",
        "coherence matrix",
        "Fano plane",
        "octonions",
        "phase transition",
        "tricritical exponents",
        "self-observation",
        "No-Zombie theorem",
        "integrated information",
        "falsifiable predictions",
        "coherence cybernetics",
        "artificial general intelligence",
        "consciousness ethics",
        "quantum mechanics",
        "general relativity",
        "spectral triples",
        "noncommutative geometry",
        "category theory",
      ],
      language: "eng",
      license: "CC-BY-4.0",
      access_right: "open",
      related_identifiers: [
        {
          relation: "isDocumentedBy",
          identifier: "https://holon.sh",
          scheme: "url",
          resource_type: "publication-other",
        },
      ],
      version: "1.0.0",
      notes:
        "60 pages, 10 figures, 3 appendices, 22 falsifiable predictions. " +
        "Source tarball and compiled PDF are included. Full formalisation " +
        "at https://holon.sh.",
    },
  };
}

/**
 * Zenodo README shown to reviewers who download the deposit. Short,
 * reproducible, and self-contained.
 */
function buildZenodoReadme(): string {
  return `# Unitary Holonomic Monism (UHM) — Zenodo deposit

**Title.** The Unitary Holonomic Monism (UHM): Deriving Consciousness, Quantum
Mechanics, and Spacetime from a Single Primitive.

**Author.** Max Sereda (independent researcher).

**Full documentation.** https://holon.sh

## Deposit contents

| File | Purpose |
|------|---------|
| \`${OUTPUT_NAME}.pdf\` | Compiled paper (60 pages, 10 figures, 3 appendices) |
| \`${OUTPUT_NAME}-source.tar.gz\` | Full LaTeX source (main.tex + sections/ + figures/ + references.bib) |
| \`zenodo-metadata.json\` | Zenodo metadata (title, abstract, keywords, license, authors) |
| \`README.md\` | This file |

## Reproducing the PDF from source

\`\`\`bash
tar -xzf ${OUTPUT_NAME}-source.tar.gz
cd ${OUTPUT_NAME}-source        # (or wherever tar extracted)
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
\`\`\`

Requires a TeX Live 2023+ installation with \`pdflatex\`, \`bibtex\`, and the
standard \`tikz\`, \`pgfplots\`, \`natbib\`, \`hyperref\`, and \`tcolorbox\`
packages. All figures are self-contained TikZ / pgfplots — no external
images are needed.

## Abstract

The paper presents the Unitary Holonomic Monism, a mathematical theory that
derives consciousness, quantum mechanics, general relativity, and the
Standard Model structure from a single primitive — the coherence matrix
$\\Gamma \\in \\mathcal{D}(\\mathbb{C}^{7})$. The theory rests on four axioms
grounded in the Fano plane and octonion algebra, all four of which are
derived as theorems. From these axioms over 180 further theorems follow,
including the No-Zombie theorem (consciousness is a necessary condition for
survival), the critical purity threshold $P_{\\text{crit}} = 2/7$, the
tricritical critical exponents $(\\alpha, \\beta, \\gamma, \\nu, \\delta) =
(1/2, 1/4, 1, 1/2, 5)$, the SAD ceiling at 3, and the Einstein field
equations from the same axioms. The applied layer (Coherence Cybernetics)
delivers 22 falsifiable predictions, each with an experimental protocol
and a falsification criterion.

## Licence

Creative Commons Attribution 4.0 International (CC-BY-4.0).
`;
}

// -------- Entrypoint --------
async function main(): Promise<void> {
  if (FLAG_HELP) {
    showUsage();
    return;
  }
  if (UNKNOWN.length > 0) {
    console.error(`❌ Unknown argument(s): ${UNKNOWN.join(" ")}\n`);
    showUsage();
    process.exit(2);
  }
  if (FLAG_ARXIV && FLAG_ZENODO) {
    console.error("❌ Cannot combine --arxiv and --zenodo in a single run.\n");
    showUsage();
    process.exit(2);
  }

  if (FLAG_ARXIV) {
    await buildArxiv();
    return;
  }
  if (FLAG_ZENODO) {
    await buildZenodo();
    return;
  }

  // Default: PDF build (matches previous behaviour)
  await buildPdf();
  const cleaned = await cleanup();
  if (cleaned > 0) console.log(`   🧹 Cleaned ${cleaned} auxiliary files`);
}

main().catch((err) => {
  console.error("❌ Unexpected error:", err);
  process.exit(1);
});
