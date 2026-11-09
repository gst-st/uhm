"""End-to-end finite response of reciprocal, unit-quaternion links, exact over Z."""
from itertools import product


ONE = (1,0,0,0)
I = (0,1,0,0)
J = (0,0,1,0)
ZERO = (0,0,0,0)


def multiply(x, y):
    a,b,c,d = x
    e,f,g,h = y
    return (a*e-b*f-c*g-d*h, a*f+b*e+c*h-d*g,
            a*g-b*h+c*e+d*f, a*h+b*g-c*f+d*e)


def inverse(unit):
    assert sum(a*a for a in unit)==1
    a,b,c,d = unit
    return (a,-b,-c,-d)


def negate(x):
    return tuple(-a for a in x)


def add(x, y):
    return tuple(a+b for a,b in zip(x,y))


def check_matter():
    group = (ONE,I,J,multiply(I,J))
    group += tuple(negate(x) for x in group)
    times = {(x,y):multiply(x,y) for x,y in product(group,repeat=2)}
    inv = {x:inverse(x) for x in group}
    assert set(times.values())==set(group)
    def act(g,s):
        u,v,i,x=s
        return times[g[1],times[u,inv[g[0]]]],times[g[2],times[v,inv[g[1]]]],i,times[g[i],x]
    def move(k,s):
        u,v,i,x=s
        link=(u,v)[k]
        if i==k:
            return u,v,k+1,times[link,x]
        if i==k+1:
            return u,v,k,times[inv[link],x]
        return s
    generators = [tuple(g if k==j else ONE for k in range(3))
                  for g in (I,J) for j in range(3)]
    for i in range(3):
        basis = {(u,v,i,x) for u,v,x in product(group,repeat=3)}
        orbit = {act(g,(ONE,ONE,i,ONE)) for g in product(group,repeat=3)}
        assert basis==orbit
        for s in basis:
            for k in (0,1):
                assert move(k,move(k,s))==s
                for g in generators:
                    assert act(g,move(k,s))==move(k,act(g,s))
    seed=(ONE,ONE,0,ONE)
    assert move(1,move(0,seed)) != move(0,move(1,seed))
    print('Q8 matter: 1536 configurations, 6 local generators, 2 reversible moves; 3 invariant orbit sums.')


def response(edges, sites, source, horizon, pulse=ONE):
    history = [{s: pulse if s==source else ZERO for s in sites}]
    for _ in range(horizon):
        current = history[-1]
        nxt = dict.fromkeys(sites, ZERO)
        for a,b,u in edges:
            nxt[b] = add(nxt[b],multiply(u,current[a]))
            nxt[a] = add(nxt[a],multiply(inverse(u),current[b]))
        history.append(nxt)
    return history


def read_first(history, detectors):
    return tuple(next((n for n,row in enumerate(history) if row[i]!=ZERO),None)
                 for i in detectors)


def check_chain():
    stations = ('A','B','C')
    chain = ('A','p','B','q','r','C')
    clocks = []
    for frames in ((ONE,)*5,(I,J,I,J,J)):
        edges = list(zip(chain,chain[1:],frames))
        changes = dict(zip(chain,(J,I,negate(I),J,ONE,I)))
        moved = [(a,b,multiply(changes[b],multiply(u,inverse(changes[a]))))
                 for a,b,u in edges]
        readings = []
        for site in stations:
            raw = response(edges,chain,site,7)
            changed = response(moved,chain,site,7,pulse=changes[site])
            assert all(changed[n][j]==multiply(changes[j],raw[n][j])
                       for j in chain for n in range(8))
            readings.append(read_first(raw,stations))
        clocks.append(readings)
    assert clocks[0]==clocks[1]==[(0,2,5),(2,0,3),(5,3,0)]
    assert multiply(I,J)!=multiply(J,I)
    # An extra relay on the second bond gives the second probe an incompatible shape.
    paths = [chain,('A','p','B','q','r','s','C')]
    pairs = []
    for line in paths:
        edges = [(a,b,ONE) for a,b in zip(line,line[1:])]
        middle = response(edges,line,'B',len(line))
        pairs.append(read_first(middle,('A','C')))
    (a,b),(c,d) = pairs
    assert a*d-b*c == 2
    print('Two probes, nine ordered arrivals each:',clocks[0])
    print('Nonproportional measured bond times:',pairs,'minor',a*d-b*c)


def check_triangle():
    sites = ('A','B','C','delay')
    # A delayed direct arm and a two-link arm meet at C on tick two.
    for direct in (ONE,negate(ONE),I,J):
        for u,v in product((ONE,I,J), repeat=2):
            path = multiply(v,u)
            arrivals = []
            for flip in (False, True):
                edge = negate(direct) if flip else direct
                edges = [('A','delay',ONE),('delay','C',edge),('A','B',u),('B','C',v)]
                raw = response(edges,sites,'A',2)
                assert raw[0]['C']==raw[1]['C']==ZERO
                arrivals.append(raw[2]['C'])
                assert raw[2]['C']==add(edge,path)
            assert any(w!=ZERO for w in arrivals)
            assert sum(a*a for w in arrivals for a in w)==4
    edges = [('A','delay',ONE),('delay','C',negate(ONE)),('A','B',ONE),('B','C',ONE)]
    assert read_first(response(edges,sites,'A',8),('C',))==(None,)
    # The same central holonomy in two matter representations. The nonzero
    # probe is the imaginary quaternion I. Ad(-1) acts trivially on it.
    adjoint_direct = multiply(negate(ONE),multiply(I,inverse(negate(ONE))))
    doublet_direct = multiply(negate(ONE),I)
    assert add(adjoint_direct,I)==(0,2,0,0) and add(doublet_direct,I)==ZERO
    assert add(negate(doublet_direct),I)==(0,2,0,0)
    print('36 pairs of unitary route settings; two physical phases recover tick 2.')
    print('Destructive control: C stays dark through tick 8 with one setting.')


if __name__ == '__main__':
    if not __debug__:
        raise SystemExit('Use Python without -O to run the exact controls.')
    check_matter()
    check_chain()
    check_triangle()
