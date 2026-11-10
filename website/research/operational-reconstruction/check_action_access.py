"""Compile the actual action-observation bridge against an independently built Math Foundations."""
import argparse
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parent
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('kernel', type=Path, help='math-foundations/lean4-mf-kernel checkout (built)')
args = parser.parse_args()
network = ROOT / 'network'
subprocess.run(['lake', 'build', '+PhenomenalAccess'], cwd=network, check=True)
# lake supplies the external package's own dependencies. Pass local paths as
# positional arguments rather than interpolating paths into shell source.
subprocess.run(['lake', 'env', 'sh', '-c',
                'export LEAN_PATH="$1:$LEAN_PATH"; exec lean -DwarningAsError=true "$2"',
                'check-access', str(network / '.lake/build/lib/lean'), str(ROOT / 'ActionAccess.lean')],
               cwd=args.kernel.resolve(), check=True)
