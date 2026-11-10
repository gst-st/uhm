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

def expected_ruler():
    cmp = lambda x, y: app('le', x, y)
    loc = lambda x: app('ruler', x)
    add = lambda x, y: app('plus', x, y)
    world = walk_world() + [('le', arrow('time', arrow('time', UNIVERSE))),
                            ('ruler', arrow('b', 'time')), ('s','b'), ('z','b'),
                            ('zero','time'), ('total','time')]
    walk = quantify(priced_walk_types(), app('M','z','total'))
    edge_bound = quantify([('i','b'), ('j','b'), ('d','time')],
                          arrow(app('edge','i','j','d'), cmp(loc('j'), add(loc('i'),'d'))))
    chain = quantify([(name,'time') for name in ['a','b0','c','d','t']],
                     arrow(cmp('a',add('b0','d')), arrow(cmp('b0',add('c','t')),
                           cmp('a',add('c',add('t','d'))))))
    return telescope(world + [('walk',walk), ('base',cmp(loc('s'),add(loc('s'),'zero'))),
                              ('link_bound',edge_bound), ('chain',chain)],
                     cmp(loc('z'),add(loc('s'),'total')))


def expected_limit():
    def function(domains, codomain):
        for domain in reversed(domains):
            codomain = arrow(domain,codomain)
        return codomain
    after = lambda n, t: app('after',n,t)
    common = lambda x, y: app('both',x,y)
    near = lambda e, a, b: app('close',e,a,b)
    finer = lambda e: app('half',e)
    sample = app('sample','p','n','x','y')
    ref = app('reference','n','x','y')
    target = app('target','x','y')
    stage_vars = [('a','scale'),('b','scale'),('n','scale')]
    left_right = [quantify(stage_vars, arrow(after('n',common('a','b')), after('n',side)))
                  for side in ('a','b')]
    types = [(name,UNIVERSE) for name in ('scale','precision','port','probe','value')]
    common_experiment = [('e','precision'),('n','scale'),('x','port'),('y','port')]
    with_probe = common_experiment[:2] + [('p','probe')] + common_experiment[2:]
    agree = quantify(with_probe, arrow(after('n',app('ready_probes','e')), near('e',sample,ref)))
    converge = quantify(common_experiment,
                        arrow(after('n',app('ready_ref','e')), near('e',ref,target)))
    twice = quantify([('e','precision'),('a','value'),('b','value'),('c','value')],
                     arrow(near(finer('e'),'a','b'),
                     arrow(near(finer('e'),'b','c'),near('e','a','c'))))
    binders = types + [('after',function(['scale','scale'],UNIVERSE)),
                       ('both',function(['scale','scale'],'scale')),
                       ('left',left_right[0]),('right',left_right[1]),
                       ('half',arrow('precision','precision')),
                       ('close',function(['precision','value','value'],UNIVERSE)),('twice',twice),
                       ('sample',function(['probe','scale','port','port'],'value')),
                       ('reference',function(['scale','port','port'],'value')),
                       ('target',function(['port','port'],'value')),
                       ('ready_probes',arrow('precision','scale')),
                       ('ready_ref',arrow('precision','scale')), ('agree',agree),('converge',converge)]
    late = after('n',common(app('ready_probes',finer('e')),app('ready_ref',finer('e'))))
    return telescope(binders + with_probe + [('late',late)], near('e',sample,target))


def expected_gap():
    pred = arrow('value', UNIVERSE)
    after = lambda n, start: app('after', n, start)
    def tail(start, test):
        return pi('n', 'scale', arrow(after('n',start), app(test,app('read','n'))))
    disjoint = pi('v','value',arrow(app('guard','v'),arrow(app('small','v'),'refute')))
    return telescope([('scale',UNIVERSE),('value',UNIVERSE),('refute',UNIVERSE),
                      ('after',arrow('scale',arrow('scale',UNIVERSE))),('read',arrow('scale','value')),
                      ('guard',pred),('small',pred),('gap_start','scale'),('zero_start','scale'),
                      ('common','scale'),('later_left',after('common','gap_start')),
                      ('later_right',after('common','zero_start')),('gap',tail('gap_start','guard')),
                      ('zero_tail',tail('zero_start','small')),('disjoint',disjoint)],'refute')


def expected_surplus():
    cp = lambda a,b: app('le',a,b)
    plus = lambda a,b: app('plus',a,b)
    double = lambda value: app('twice',value)
    cost = lambda i: app('cost',i)
    reserve = lambda i: app('reserve',i)
    error = lambda i: app('error',i)
    nxt = lambda i: app('next',i)
    proof_family = arrow('level',arrow('time',UNIVERSE))
    step = quantify([('i','level'),('a','time')],arrow(app('refines','i'),
                    arrow(app('M','i','a'),app('M',nxt('i'),double('a')))))
    iterator = pi('M',proof_family,arrow(step,arrow(app('M','start','seed'),
                                                   app('M','stop','amplified'))))
    extend = pi('i','level',arrow(app('refines','i'),
                cp(double(cost('i')),plus(cost(nxt('i')),error('i')))))
    pay = pi('i','level',arrow(app('refines','i'),
                cp(plus(error('i'),reserve(nxt('i'))),double(reserve('i')))))
    doubled = quantify([(i,'time') for i in ('a','r','t')],arrow(cp(plus('a','r'),'t'),
                       cp(plus(double('a'),double('r')),double('t'))))
    translate = quantify([(i,'time') for i in ('a','e','r','z')],arrow(cp(plus('e','r'),'z'),
                         cp(plus(plus('a','r'),'e'),plus('a','z'))))
    trans = quantify([(i,'time') for i in ('a','b','c')],arrow(cp('a','b'),
                     arrow(cp('b','c'),cp('a','c'))))
    cancel = quantify([(i,'time') for i in ('a','b','e')],arrow(cp(plus('a','e'),plus('b','e')),
                      cp('a','b')))
    return telescope([('level',UNIVERSE),('time',UNIVERSE),('next',arrow('level','level')),
                      ('twice',arrow('time','time')),('plus',arrow('time',arrow('time','time'))),
                      ('le',arrow('time',arrow('time',UNIVERSE))),('cost',arrow('level','time')),
                      ('refines',arrow('level',UNIVERSE)),('reserve',arrow('level','time')),
                      ('error',arrow('level','time')),('start','level'),('stop','level'),
                      ('seed','time'),('amplified','time'),('iterate',iterator),
                      ('initial',cp(plus('seed',reserve('start')),cost('start'))),
                      ('extend',extend),('pay',pay),('doubled',doubled),('translate',translate),
                      ('trans',trans),('cancel',cancel)],cp(plus('amplified',reserve('stop')),cost('stop')))


def expected_round_trip():
    add = lambda x,y: app('plus',x,y)
    eq = lambda x,y: ('id','value',x,y)
    half_cancel = quantify([('a','value'),('b','value')],arrow(eq(add('a','a'),add('b','b')),
                          eq('a','b')))
    return telescope([('value',UNIVERSE),('plus',arrow('value',arrow('value','value'))),
                      ('half_cancel',half_cancel),('p','value'),('q','value'),('back_p','value'),
                      ('symmetric_p',eq('p','back_p')),('back_q','value'),
                      ('symmetric_q',eq('q','back_q')),('circuit',eq(add('p','back_p'),add('q','back_q')))],
                     eq('p','q'))


def expected_trace_projection():
    # The trace must work for every indexed invariant in universe 1:
    # transporting an arbitrary observable predicate lives at that universe.
    higher = {"Universe":{"Concrete":1}}
    family = arrow('state', arrow('value', higher))
    def transition(e, x):
        return app('step', e, x)
    def update(e, v):
        return app('update', e, v)
    def read(x):
        return app('read', x)
    advance = quantify([('e','event'), ('x','state'), ('v','value')],
                       arrow(app('M','x','v'), app('M', transition('e','x'), update('e','v'))))
    trace = pi('M', family, arrow(advance, arrow(app('M','start',read('start')),
                                                app('M','stop','recorded'))))
    local = quantify([('e','event'), ('x','state'), ('pred',arrow('value',UNIVERSE))],
                     arrow(app('pred',read(transition('e','x'))), app('pred',update('e',read('x')))))
    return telescope([('event',UNIVERSE), ('state',UNIVERSE), ('value',UNIVERSE),
                      ('step',arrow('event',arrow('state','state'))),
                      ('update',arrow('event',arrow('value','value'))),
                      ('read',arrow('state','value')), ('start','state'), ('stop','state'),
                      ('recorded','value'), ('trace',trace), ('local',local)],
                     ('id','value',read('stop'),'recorded'))


def expected_decoder_fibre():
    view = lambda x: app('reading',x)
    target = lambda x: app('target',x)
    decode = lambda x: app('decode',view(x))
    return telescope([('history',UNIVERSE), ('observation',UNIVERSE), ('answer',UNIVERSE),
                      ('reading',arrow('history','observation')), ('target',arrow('history','answer')),
                      ('decode',arrow('observation','answer')), ('x','history'), ('y','history'),
                      ('indistinguishable',('id','observation',view('x'),view('y'))),
                      ('left',('id','answer',target('x'),decode('x'))),
                      ('right',('id','answer',target('y'),decode('y')))],
                     ('id','answer',target('x'),target('y')))


def expected_interaction():
    le = lambda a, b: app('le', a, b)
    lt = lambda a, b: app('lt', a, b)
    sub = lambda a, b: app('sub', a, b)
    def values(*names):
        return [(name, 'value') for name in names]
    relation = arrow('value', arrow('value', UNIVERSE))
    trans = quantify(values('a', 'b', 'c'), arrow(lt('a','b'), arrow(lt('b','c'), lt('a','c'))))
    positive = quantify(values('a','b'), arrow(lt('a','b'), lt('zero', sub('b','a'))))
    monotone = quantify(values('a','b','c','d'), arrow(le('a','c'), arrow(le('d','b'),
                        le(sub('a','b'),sub('c','d')))))
    low, true, high = sub('hlo','phi'), sub('history','phase'), sub('hhi','plo')
    finish = arrow(lt('zero',low), arrow(le(low,true), arrow(le(true,high),'result_type')))
    binders = [('value',UNIVERSE),('result_type',UNIVERSE),('le',relation),('lt',relation),
               ('sub',arrow('value', arrow('value','value')))] + values('zero','margin')
    binders += [('trans_lt',trans),('positive_difference',positive),('sub_order',monotone)]
    binders += values('plo','phase','phi','hlo','history','hhi')
    binders += [('phase_floor',le('plo','phase')),('phase_ceiling',le('phase','phi')),
                ('history_floor',le('hlo','history')),('history_ceiling',le('history','hhi')),
                ('phase_inner',lt('phi','margin')),('history_outer',lt('margin','hlo')),
                ('consume',finish)]
    return telescope(binders, 'result_type')


LOGICAL_TYPES = {
    'middle_frame_cancels': expected_corner,
    'relay_triangle': expected_relay,
    'scale_minimum': expected_scale,
    'walk_empty': expected_empty,
    'walk_append': expected_append,
    'lift_priced_walk': expected_lift,
    'based_loop_composition': expected_loop,
    'ruler_on_walk': expected_ruler,
    'shared_limit_modulus': expected_limit,
    'exclude_zero_tail': expected_gap,
    'dyadic_surplus': expected_surplus,
    'reciprocal_round_trip': expected_round_trip,
    'trace_projection': expected_trace_projection,
    'faithful_decoder_fibre': expected_decoder_fibre,
    'interaction_interval': expected_interaction,
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
    ('Continuum.vr','pi-id','ruler_on_walk',None,'link_bound(i,j,d,link),prefix','prefix,link_bound(i,j,d,link)'),
    ('Continuum.vr','pi-id','shared_limit_modulus',None,'y,right(ready_probes','y,left(ready_probes'),
    ('Continuum.vr','pi-id','exclude_zero_tail',None,'zero_tail(common,later_right)','zero_tail(common,later_left)'),
    ('Continuum.vr','pi-id','dyadic_surplus',None,'twice(reserve(i)),pay(i,cert)','twice(reserve(i)),extend(i,cert)'),
    ('PeriodicControls.vr','finite','periodic_arrival',16,'let d1 = c0 || e0 || (bypass && a0)','let d1 = c0 || e0'),
    ('PeriodicControls.vr','finite','dyadic_threshold',32,'let d3 = c2 != (!a2 && !b2)','let d3 = !c2'),
    ('Continuum.vr','pi-id','reciprocal_round_trip',None,'induction symmetric_p; exact(half_cancel','exact(half_cancel'),
    ('PeriodicControls.vr','finite','reserve_arithmetic',64,'let paid = r || (!r_next && !e)','let paid = r || !e'),
    ('PeriodicControls.vr','finite','square_read',8,'let d1 = b0 || c0 || (diagonal && a0)','let d1 = b0 || c0'),
    ('BreathTrace.vr','pi-id','trace_projection',None,'pred(update(e,w)),local(e,x,pred,h)','pred(w),local(e,x,pred,h)'),
    ('BreathTrace.vr','pi-id','faithful_decoder_fibre',None,'rewrite(indistinguishable); reflexivity','reflexivity'),
    ('BreathPractice.vr','finite','count_step',40,'Ordinal.Nine=>Ordinal.Z','Ordinal.Nine=>Ordinal.Nine'),
    ('BreathPractice.vr','finite','paired_items',80,'track(n,true,false)','track(n,true,true)'),
    ('BreathPractice.vr','finite','missed_updates',40,'if miss_second { first }','if miss_first { first }'),
    ('BreathPractice.vr','finite','reset_alignment',20,'next_count(Ordinal.Z) } else { Ordinal.Z','Ordinal.Z } else { Ordinal.Z'),
    ('BreathPractice.vr','finite','nuisance_leak',8,'if leak { !first_cue }','if leak { first_cue }'),
    ('BreathPractice.vr','finite','cue_increases_ceiling',81,'let second = greater_mass(e1,o1)','let second = greater_mass(e0,o0)'),
    ('BreathTrace.vr','pi-id','interaction_interval',None,'history_floor,phase_ceiling)','history_floor,phase_floor)'),
    ('PracticeDecision.vr','finite','completion_range',12,'proposed == finish_record(r,true)','proposed == finish_record(r,false)'),
    ('PracticeDecision.vr','finite','joint_gate',243,'Position.Above=>higher(floor_follow)','Position.Above=>!lower(floor_follow)'),
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
