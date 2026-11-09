"""Elaborate registered source, replay native judgments and require semantic mutation failures."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parent
def digest(data):
    return hashlib.sha256(data).hexdigest()

def expect(ok, message):
    if not ok:
        raise ValueError(message)

def identity(carrier, lhs, rhs):
    return {"Id":{"ty":carrier,"lhs":lhs,"rhs":rhs}}

def expected_corner():
    """Independent named telescope for congruence through the outgoing transporter."""
    ctx = []
    domains = []
    var = lambda name: {"Var":ctx[::-1].index(name)}
    def app(f, x):
        return {"App":[var(f),x]}
    def bind(name, domain):
        domains.append(domain)
        ctx.append(name)
    for ty in ['A','B','C']:
        bind(ty,{"Universe":{"Concrete":0}})
    for f, a, b in [('u','A','B'),('v','B','C'),('turn','B','B'),('back','B','B')]:
        domain = var(a)
        ctx.append('_')
        codomain = var(b)
        ctx.pop()
        bind(f,{"Pi":[domain,codomain]})
    bind('x',var('A'))
    def mid():
        return app('u',var('x'))
    def turned():
        return app('back',app('turn',mid()))
    bind('cancel',identity(var('B'),turned(),mid()))
    result = identity(var('C'),app('v',turned()),app('v',mid()))
    for domain in reversed(domains):
        result = {"Pi":[domain,result]}
    return result

def expected_relay():
    """Translate a separately specified telescope, in named dependent-arrow notation."""
    U = {"Universe":{"Concrete":0}}
    def app(f,*args):
        for a in args:
            f=('app',f,a)
        return f
    def pi(name,a,b):
        return ('pi',name,a,b)
    def arrow(a,b):
        return pi('_',a,b)
    binders=[('time',U)]+[(f,arrow('time',U)) for f in ['ab','bc','ac']]
    binders.extend((x,'time') for x in ['left','right','shortest'])
    binders += [('total',arrow('time',arrow('time','time'))),
                ('le',arrow('time',arrow('time',U))),
                ('left_run',app('ab','left')),('right_run',app('bc','right')),
                ('relay',pi('t','time',pi('u','time',arrow(app('ab','t'),
                         arrow(app('bc','u'),app('ac',app('total','t','u'))))))),
                ('least',pi('t','time',arrow(app('ac','t'),app('le','shortest','t'))))]
    expr=app('le','shortest',app('total','left','right'))
    for name,ty in reversed(binders):
        expr=pi(name,ty,expr)
    def lower(node,ctx):
        if isinstance(node,str):
            return {"Var":ctx[::-1].index(node)}
        if isinstance(node,dict):
            return node
        if node[0]=='app':
            return {"App":[lower(node[1],ctx),lower(node[2],ctx)]}
        _,name,ty,body=node
        return {"Pi":[lower(ty,ctx),lower(body,ctx+[name])]}
    return lower(expr,[])

SPECS = [
    ('Relay.vr','pi-id','relay_triangle',None,'right,left_run,right_run','right,right_run,left_run'),
    ('Reporting.vr','finite','indistinguishable',4,'else { next(report) }','else { report }'),
    ('Corners.vr','pi-id','middle_frame_cancels',None,'rewrite(cancel); reflexivity','reflexivity'),
    ('Arrival.vr','finite','paired_first_response',8,'|| bright(d,u,v,true)','&& bright(d,u,v,true)'),
    ('Arrival.vr','finite','middle_frame',32,'parity(v,turn),flip','v,flip'),
    ('Arrival.vr','finite','first_on_chain',9,'let c1 = w || e','let c1 = w && e'),
    ('Arrival.vr','finite','clock_minor',16,'delay_product(a,d),delay_product(b,c)','delay_product(a,c),delay_product(b,d)'),
    ('Arrival.vr','finite','center_readout',4,'bright(doublet,false,false,external_flip)','bright(false,false,false,external_flip)'),
]

def replay(checker, profile, source, theorem):
    request = dict(profile='verum-source-'+profile+'/1', source=source, declaration=theorem)
    cmd = subprocess.run([checker,'--worker'],input=json.dumps(request),text=True,
                         capture_output=True,check=True,timeout=90)
    report = json.loads(cmd.stdout)
    expect(report['source']['sha256']==digest(source.encode()),'source digest mismatch')
    expect(report['source']['declaration']==theorem,'wrong declaration')
    return report

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('checker',type=Path,help='verum-source-replay binary')
    p.add_argument('--report',type=Path)
    args=p.parse_args()
    checker=args.checker.resolve(strict=True)
    receipt={'binary_sha256':digest(checker.read_bytes()), 'declarations':[]}
    for filename,profile,name,cases,old,new in SPECS:
        source=(ROOT/filename).read_text()
        actual=replay(checker,profile,source,name)
        expect(actual['status']=='verified' and actual['native']['accepted'],str(actual.get('diagnostic')))
        j=actual['judgment']
        expect(j['statement']==j['certificate']['claimed_type'],'certificate binds another type')
        if cases is None:
            oracle = expected_corner if name=='middle_frame_cancels' else expected_relay
            expect(j['statement']==oracle(),'unexpected named logical theorem')
        else:
            imp=actual['implementation']
            expect(imp['input_cases']==cases and imp['requires_count']==0 and imp['ensures_count']==1,
                   'incomplete finite contract')
        expect(source.count(old)==1,'ambiguous mutation')
        bad=replay(checker,profile,source.replace(old,new),name)
        reason=bad['diagnostic']['code']
        expect(bad['status']=='rejected' and not bad.get('judgment') and
               reason==('type_mismatch' if cases else 'ill_typed_source'),'negative control accepted or skipped')
        if cases:
            expect(bad.get('native') and not bad['native']['accepted'],'negative bypassed native adjudication')
        receipt['declarations'].append(dict(name=name,profile=profile,cases=cases,
              source_sha256=actual['source']['sha256'],checker=actual['native']['checker'],
              statement_sha256=digest(json.dumps(j['statement'],sort_keys=True,separators=(',',':')).encode()),
              mutation_rejected=reason))
        print(name,'verified;',cases or 'parametric','; altered obligation rejected')
    if args.report:
        args.report.write_text(json.dumps(receipt,indent=2)+'\n')

if __name__=='__main__':
    main()
