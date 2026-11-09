"""Audit the compiled proof environment, including private helpers and generated theorems."""
import argparse
import json
import os
from pathlib import Path
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parent

# Inspect the elaborated environment so a nested namespace, a private lemma
# or a change of Lean source formatting cannot hide a proof from this check.
INSPECT = """
open Lean Elab Command
run_cmd
  let env ← getEnv
  let modules : List Name := [MODULE_NAMES]
  for mod in modules do
    let some idx := env.getModuleIdx? mod | throwError "missing module {mod}"
    let mut checked : Nat := 0
    for (name, decl) in env.constants.toList do
      unless env.getModuleIdxFor? name == some idx do continue
      if decl.isAxiom then throwError "local axiom {name}"
      if decl.isTheorem then
        for ax in ← collectAxioms name do
          unless [`propext, ``Quot.sound].contains ax do
            throwError "{name} depends on {ax}"
        checked := checked+1
        if !isPrivateName name && !name.isInternal && !name.hasMacroScopes then
          logInfo m!"EXPORT {name}"
    if checked == 0 then throwError "no theorems in {mod}"
    logInfo m!"CLOSURES {mod} {checked}"
"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--replay-kernels', action='store_true',
                        help='also export the public theorem closures and replay external checkers')
    args = parser.parse_args()
    modules = sorted(p.stem for p in ROOT.glob('*.lean'))
    build = subprocess.run(['lake', 'build', *('+' + m for m in modules)], cwd=ROOT,
                           text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if build.returncode:
        raise RuntimeError(build.stdout)
    with tempfile.TemporaryDirectory() as tmp:
        audit = Path(tmp) / 'Audit.lean'
        audit.write_text('import Lean\n' + ''.join('import ' + m + '\n' for m in modules)
                         + INSPECT.replace('MODULE_NAMES', ', '.join('`' + m for m in modules)))
        proc = subprocess.run(['lake', 'env', 'lean', '-DwarningAsError=true', str(audit)],
                              cwd=ROOT, text=True, stdout=subprocess.PIPE)
        if proc.returncode:
            raise RuntimeError(proc.stdout)
        summary = {}
        public = []
        for line in proc.stdout.splitlines():
            if line.startswith('CLOSURES '):
                _, module, count = line.split()
                summary[module] = int(count)
            elif line.startswith('EXPORT '):
                public.append(line.removeprefix('EXPORT '))
        if set(summary) != set(modules) or not public:
            raise RuntimeError('incomplete Lean environment inventory')
        print(f'{sum(summary.values())} theorem closures in {len(modules)} modules '
              '(includes generated and private proofs); allowed: propext, Quot.sound', flush=True)
        if args.replay_kernels:
            export = Path(tmp) / 'proofs.ndjson'
            with export.open('wb') as out:
                subprocess.run(['lake', 'env', 'leanexport', *modules, '--', *sorted(public)],
                               cwd=ROOT, stdout=out, check=True)
            prefix = subprocess.check_output(['lake', 'env', 'lean', '--print-prefix'],
                                             cwd=ROOT, text=True).strip()
            binaries = Path(prefix) / 'bin'
            config = Path(tmp) / 'nanoda.json'
            config.write_text(json.dumps(dict(export_file_path=str(export), use_stdin=False,
                permitted_axioms=['propext', 'Quot.sound'], unpermitted_axiom_hard_error=True,
                num_threads=2, nat_extension=True, string_extension=True)))
            for name, command in [('leanchecker-paranoid', ['--silent', '--from-export', str(export)]),
                                  ('lean4lean', ['--import', str(export)]),
                                  ('nanoda_bin', [str(config)])]:
                subprocess.run([binaries / name, *command], cwd=tmp, check=True,
                               env={**os.environ, 'LEAN_ABORT_ON_PANIC': '1'})
                print(f'{name} accepted exported theorem closures', flush=True)


if __name__=='__main__':
    main()
