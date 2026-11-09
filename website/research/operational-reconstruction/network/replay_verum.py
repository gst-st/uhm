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

# Independent type specifications. Bound names are lowered to native de Bruijn
# indices only after constructing the complete expected proposition.
UNIVERSE = {"Universe":{"Concrete":0}}

def app(function, *arguments):
    for argument in arguments:
        function = ('app', function, argument)
    return function

def pi(name, domain, body):
    return ('pi', name, domain, body)

def arrow(domain, body):
    return pi('_', domain, body)

def telescope(binders, conclusion):
    def lower(node, context):
        if isinstance(node, str):
            return {"Var":context[::-1].index(node)}
        if isinstance(node, dict):
            return node
        if node[0] == 'app':
            return {"App":[lower(node[1], context), lower(node[2], context)]}
        if node[0] == 'id':
            return identity(*(lower(part, context) for part in node[1:]))
        _, name, domain, body = node
        return {"Pi":[lower(domain, context), lower(body, context + [name])]}
    for name, domain in reversed(binders):
        conclusion = pi(name, domain, conclusion)
    return lower(conclusion, [])

def expected_relay():
    binders=[('time',UNIVERSE)]+[(f,arrow('time',UNIVERSE)) for f in ['ab','bc','ac']]
    binders.extend((x,'time') for x in ['left','right','shortest'])
    binders += [('total',arrow('time',arrow('time','time'))),
                ('le',arrow('time',arrow('time',UNIVERSE))),
                ('left_run',app('ab','left')),('right_run',app('bc','right')),
                ('relay',pi('t','time',pi('u','time',arrow(app('ab','t'),
                         arrow(app('bc','u'),app('ac',app('total','t','u'))))))),
                ('least',pi('t','time',arrow(app('ac','t'),app('le','shortest','t'))))]
    return telescope(binders, app('le','shortest',app('total','left','right')))

def expected_scale():
    predicate = arrow('time', UNIVERSE)
    def transfers(source, target):
        return pi('t', 'time', arrow(app(source, 't'), app(target, 't')))
    def least(predicate_name, minimum):
        return pi('t', 'time', arrow(app(predicate_name, 't'), app('le', minimum, 't')))
    antisym = pi('x', 'time', pi('y', 'time', arrow(app('le', 'x', 'y'),
                 arrow(app('le', 'y', 'x'), ('id', 'time', 'x', 'y')))))
    binders = [('time', UNIVERSE), ('fine', predicate), ('coarse', predicate),
               ('le', arrow('time', predicate)), ('f', 'time'), ('c', 'time'),
               ('fine_run', app('fine', 'f')), ('coarse_run', app('coarse', 'c')),
               ('project', transfers('fine', 'coarse')), ('realize', transfers('coarse', 'fine')),
               ('least_f', least('fine', 'f')), ('least_c', least('coarse', 'c')),
               ('antisym', antisym)]
    return telescope(binders, ('id', 'time', 'f', 'c'))

def expected_loop():
    first = app('u', 'x')
    second = app('v', first)
    moved = app('g', 'x')
    binders = [('a', UNIVERSE), ('b', UNIVERSE), ('g', arrow('a', 'b')),
               ('u', arrow('a', 'a')), ('v', arrow('a', 'a')),
               ('U', arrow('b', 'b')), ('V', arrow('b', 'b')), ('x', 'a'),
               ('hu', ('id', 'b', app('g', first), app('U', moved))),
               ('hv', ('id', 'b', app('g', second), app('V', app('g', first))))]
    return telescope(binders, ('id', 'b', app('g', second), app('V', app('U', moved))))

def quantify(binders, conclusion):
    for name, domain in reversed(binders):
        conclusion = pi(name, domain, conclusion)
    return conclusion

def priced_walk_types():
    # The free walk's eliminator may target *any* vertex/price-indexed
    # family. This telescope does not mention fine ports or local lifting.
    family = arrow('b', arrow('time', UNIVERSE))
    step = quantify([('i0','b'), ('j0','b'), ('t0','time'), ('d0','time')],
                    arrow(app('edge','i0','j0','d0'), arrow(app('M','i0','t0'),
                          app('M','j0',app('plus','t0','d0')))))
    rules = [('M',family), ('step',step), ('initial',app('M','s','zero'))]
    return rules

def walk_world():
    return [('b',UNIVERSE), ('time',UNIVERSE), ('edge',arrow('b',arrow('b',arrow('time',UNIVERSE)))),
            ('plus',arrow('time',arrow('time','time')))]

def expected_empty():
    rules = priced_walk_types()
    return telescope(walk_world()+[('s','b'),('zero','time')]+rules, app('M','s','zero'))

def expected_append():
    rules = priced_walk_types()
    initial = [('s','b'),('zero','time'),('i','b'),('j','b'),('t','time'),('d','time')]
    walk = quantify(rules, app('M','i','t'))
    binders = walk_world()+initial+[('walk', walk),('passage',app('edge','i','j','d'))]+rules
    return telescope(binders, app('M','j',app('plus','t','d')))

def expected_lift():
    def port(vertex):
        return app('ports',vertex)
    def fine(i,j,t,x,y):
        return app('fine',i,j,t,x,y)
    world = walk_world()
    world.insert(2, ('ports', arrow('b', UNIVERSE)))
    world += [('fine',quantify([('i','b'),('j','b'),('t','time')],
                               arrow(port('i'),arrow(port('j'),UNIVERSE))))]
    endpoints = [('s','b'),('z','b'),('zero','time'),('total','time'),
                 ('x',port('s')),('answer',UNIVERSE)]
    walk = quantify(priced_walk_types(), app('M','z','total'))
    next_port = pi('p',port('j'),arrow(fine('i','j','d','y','p'),'r'))
    supply = quantify([('i','b'),('j','b'),('d','time'),('y',port('i')),('r',UNIVERSE)],
                      arrow(app('edge','i','j','d'),arrow(next_port,'r')))
    join = quantify([('i','b'),('j','b'),('k','b'),('t','time'),('d','time'),
                     ('a',port('i')),('y',port('j')),('p',port('k'))],
                    arrow(fine('i','j','t','a','y'),
                    arrow(fine('j','k','d','y','p'),fine('i','k',app('plus','t','d'),'a','p'))))
    finish = pi('p',port('z'),arrow(fine('s','z','total','x','p'),'answer'))
    return telescope(world+endpoints+[('walk',walk),('initial',fine('s','s','zero','x','x')),
                     ('supply',supply),('join',join),('finish',finish)],'answer')

LOGICAL_TYPES = {
    'middle_frame_cancels': expected_corner,
    'relay_triangle': expected_relay,
    'scale_minimum': expected_scale,
    'walk_empty': expected_empty,
    'walk_append': expected_append,
    'lift_priced_walk': expected_lift,
    'based_loop_composition': expected_loop,
}

SPECS = [
    ('Relay.vr','pi-id','relay_triangle',None,'right,left_run,right_run','right,right_run,left_run'),
    ('Reporting.vr','finite','indistinguishable',4,'else { next(report) }','else { report }'),
    ('Corners.vr','pi-id','middle_frame_cancels',None,'rewrite(cancel); reflexivity','reflexivity'),
    ('Arrival.vr','finite','paired_first_response',8,'|| bright(d,u,v,true)','&& bright(d,u,v,true)'),
    ('Arrival.vr','finite','middle_frame',32,'parity(v,turn),flip','v,flip'),
    ('Arrival.vr','finite','first_on_chain',9,'let c1 = w || e','let c1 = w && e'),
    ('Arrival.vr','finite','clock_minor',16,'delay_product(a,d),delay_product(b,c)','delay_product(a,c),delay_product(b,d)'),
    ('Arrival.vr','finite','center_readout',4,'bright(doublet,false,false,external_flip)','bright(false,false,false,external_flip)'),
    ('Coarsening.vr','pi-id','scale_minimum',None,'realize(c,coarse_run)','realize(f,fine_run)'),
    ('Coarsening.vr','pi-id','based_loop_composition',None,'rewrite(hu); reflexivity','reflexivity'),
    ('CycleControls.vr','finite','separate_conjugacies',3,'intertwines_at(Gauge.R,c,true)','intertwines_at(Gauge.R2,c,true)'),
    ('CycleControls.vr','finite','no_common_gauge',6,'Red,false) && intertwines_at','Red,false) || intertwines_at'),
    ('CycleControls.vr','finite','observe',4,'let p1 = a || (merged && c)','let p1 = a || c'),
    ('CycleControls.vr','finite','four_route_readout',8,'let bit = u && !lose_bit','let bit = u'),
    ('PortFold.vr','pi-id','walk_empty',None,'proof = initial;','proof = zero;'),
    ('PortFold.vr','pi-id','walk_append',None,'passage,walk(M,step,initial)','passage,initial'),
    ('PortFold.vr','pi-id','lift_priced_walk',None,'supply(i,j,d,y,answer,link','supply(i,j,d,x,answer,link'),
    ('CycleControls.vr','finite','boundary_needs_history',2,'let f2 = next_far(b1,n1,f1)','let f2 = f1'),
    ('CycleControls.vr','finite','refinement_read',48,'Port.B=>delay_a || delay_c','Port.B=>delay_a'),
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
            expect(j['statement']==LOGICAL_TYPES[name](),'unexpected named logical theorem: '+name)
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
