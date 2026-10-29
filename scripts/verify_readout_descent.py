#!/usr/bin/env python3
"""Replay the conditional readout laws with the pinned Lean kernel.

This is independent mathematical replay, not a native Verum certificate, a
Rust refinement proof, or evidence of phenomenal experience. A negative control
passes only on the intended kernel-evaluated false claim, never on a tool error.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import signal
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1] / 'verification' / 'lean'
MODULE = ROOT / 'ReadoutDescent.lean'
PIN = ROOT / 'lean-toolchain'
FALSE = '`decide_cbv` failed: the proposition evaluates to `false`'
NEGATIVE = {
    'alias_invisible_after_action': 'first (swap (false, false)) = first (swap (false, true))',
    'section_repairs_missing_state':
        'induced projection swap (first (false, true)) = first (swap (false, true))',
    'availability_ignored':
        '(conditional (false, false)).map first = (conditional (false, true)).map first',
    'foreign_transport_commutes': 'first (swap (false, true)) = first (false, true)',
    'coarse_readout_injective': '(false, false) = (false, true)',
}


def fingerprint(path):
    raw = path.read_bytes()
    return {'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}


def run(*command):
    env = dict(os.environ, ELAN_TOOLCHAIN=PIN.read_text().strip())
    with subprocess.Popen(command, cwd=ROOT, env=env, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE, text=True,
                          start_new_session=os.name == 'posix') as process:
        try:
            stdout, stderr = process.communicate(timeout=60)
        except BaseException:
            try:
                if os.name == 'posix':
                    os.killpg(process.pid, signal.SIGKILL)
                else:
                    process.kill()
            except ProcessLookupError:
                pass
            process.communicate()
            raise
        return process.returncode, stdout, stderr


def check(path, negative=False):
    code, stdout, stderr = run('lean', '--json', str(path))
    diagnostics = [json.loads(line) for line in stdout.splitlines() if line.strip()]
    errors = [d for d in diagnostics if d['severity'] == 'error']
    if negative:
        valid = code == 1 and not stderr and len(errors) == 1 and errors[0]['data'].startswith(FALSE)
    else:
        valid = code == 0 and not stderr and not errors
    if not valid:
        raise RuntimeError(f'Unexpected proof/control outcome for {path}:\n{stdout}{stderr}')
    return {'source': fingerprint(path), 'returncode': code, 'diagnostics': diagnostics}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    if args.report and args.report.exists():
        raise ValueError('report already exists; do not overwrite evidence')
    sources = {str(p): fingerprint(p) for p in (MODULE, PIN, Path(__file__).resolve())}
    code, version, stderr = run('lean', '--version')
    if code or stderr or 'version 4.35.0' not in version:
        raise RuntimeError('pinned Lean 4.35.0 unavailable: ' + version + stderr)
    proof = MODULE.read_text()
    positive = check(MODULE)
    expected = re.findall(r'^#print axioms (\S+)$', proof, re.M)
    declarations = ['ReadoutDescent.' + name for name in
                    re.findall(r'^theorem (\w+)\b', proof, re.M)]
    if len(expected) != len(set(expected)) or set(expected) != set(declarations):
        raise RuntimeError('each theorem declaration must have exactly one axiom audit')
    audits = {}
    allowed = {'propext', 'Quot.sound'}
    for diagnostic in positive['diagnostics']:
        data = diagnostic['data']
        match = re.fullmatch(r"'([^']+)' (?:depends on axioms: \[([^\]]*)\]|does not depend on any axioms)", data)
        if match:
            name, axiom_text = match.groups()
            axioms = [] if not axiom_text else [x.strip() for x in axiom_text.split(',')]
            if name in audits or not set(axioms) <= allowed:
                raise RuntimeError('unexpected/duplicate axiom audit: ' + data)
            audits[name] = axioms
    if set(audits) != set(expected) or len(expected) != 16:
        raise RuntimeError('incomplete theorem axiom inventory')
    controls = {}
    with tempfile.TemporaryDirectory(prefix='uhm-readout-controls-') as directory:
        for name, claim in NEGATIVE.items():
            path = Path(directory) / (name + '.lean')
            path.write_text(proof + '\nopen ReadoutDescent\nexample : ' + claim + ' := by decide_cbv\n')
            controls[name] = check(path, negative=True)
    if any(fingerprint(Path(p)) != v for p, v in sources.items()):
        raise RuntimeError('proof sources changed during verification')
    report = {'status': 'passed', 'scope': __doc__, 'toolchain': version.strip(),
              'sources': sources, 'positive': positive, 'axiom_audits': audits,
              'negative_controls': controls}
    if args.report:
        with args.report.open('x') as output:
            output.write(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(f'проверок: {len(audits) + len(controls)}')
    print(f'PASS: {len(audits)} theorem axiom audits; {len(controls)} intended false controls')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
