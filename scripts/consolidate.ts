#!/usr/bin/env bun
// Compatibility entry point; build-markdown.py owns the complete export policy.
import { copyFileSync } from "node:fs";
import { dirname, join } from "node:path";

const root = join(dirname(Bun.main), "..");
const run = Bun.spawnSync(["python3", join(root, "scripts/build-markdown.py")], {
  stdout: "inherit", stderr: "inherit",
});
if (run.exitCode !== 0) process.exit(run.exitCode);
copyFileSync(join(root, "output/markdown/uhm-en.md"),
  process.argv[2] || join(root, "docs-consolidated.md"));
