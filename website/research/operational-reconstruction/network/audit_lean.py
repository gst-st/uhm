"""Ask Lean for the actual transitive axiom set of each local proved declaration."""
from pathlib import Path
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parent
MODULES = ('Transport','Matter','Response','Network','ProtocolMetric','Reports')


def main():
    names = [name for mod in MODULES for name in re.findall(r'^theorem (\w+)',(ROOT/(mod+'.lean')).read_text(),re.M)]
    if not names or len(set(names)) != len(names):
        raise RuntimeError('missing or ambiguous network declarations')
    subprocess.run(['lake','build'],cwd=ROOT,stdout=subprocess.DEVNULL,check=True)
    with tempfile.TemporaryDirectory() as directory:
        source=Path(directory)/'Audit.lean'
        source.write_text('import Network\n'+''.join('#print axioms OperationalNetwork.'+n+'\n' for n in names))
        proc=subprocess.run(['lake','env','lean','-DwarningAsError=true',str(source)],
                            cwd=ROOT,text=True,capture_output=True,check=True)
    for n in names:
        key="'OperationalNetwork."+n+"' "
        verdicts=[line[len(key):] for line in proc.stdout.splitlines() if line.startswith(key)]
        if verdicts==['does not depend on any axioms']:
            continue
        if len(verdicts)!=1 or not (matches:=re.fullmatch(r'depends on axioms: \[([^\]]+)\]',verdicts[0])):
            raise RuntimeError((n,verdicts))
        if set(matches.group(1).split(', '))-{'propext','Quot.sound'}:
            raise RuntimeError((n,verdicts))
    print(len(names),'Lean theorem dependency closures checked; allowed: propext, Quot.sound')


if __name__=='__main__':
    main()
