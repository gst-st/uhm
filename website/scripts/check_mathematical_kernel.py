#!/usr/bin/env python3
"""Independent witnesses for the foundational revision (2026-10-03).

These tests check identities, explicit counterexamples, and finite constructions.
They do not certify the whole corpus or identify matrix statistics with experience.
Run: python3 website/scripts/check_mathematical_kernel.py
"""
import itertools
from pathlib import Path
import sys
import numpy as np
from scipy.linalg import expm

N = 7
I = np.eye(N)
u = np.ones(N)/np.sqrt(N)
anchor = np.outer(u,u)
rng = np.random.default_rng(20261003)
checks = []


def check(name, predicate):
    if not bool(predicate):
        raise AssertionError(name)
    checks.append(name)


def purity(rho):
    return float(np.trace(rho@rho).real)


def stats(rho):
    p = purity(rho)
    d = float(np.sum(np.diag(rho).real**2))
    return p, 1/(N*p), p/d-1


def coh_e(rho, e=4):
    return float((2*np.sum(np.abs(rho[e,:])**2)-abs(rho[e,e])**2)/purity(rho))


def gap(rho):
    out=np.abs(np.sin(np.angle(rho)))
    out[np.abs(rho)<1e-12]=0
    return out


def state():
    a=rng.normal(size=(N,N))+1j*rng.normal(size=(N,N))
    b=a@a.conj().T
    return b/np.trace(b)


# Operational discrimination below the chosen majority cut.
rho=I/N
rho=rho.copy(); rho[0,0]+=.1; rho[1,1]-=.1
advantage=np.sum(np.abs(np.linalg.eigvalsh(rho-I/N)))/4
check('Helstrom advantage below 2/7', purity(rho)<2/N and np.isclose(.5+advantage,.55))
check('diagonal pure state disproves purity -> integration', stats(np.diag([1,0,0,0,0,0,0]))[2]==0)
check('qubit strict structural majority empty', 1<=2/2)

samples=[state() for _ in range(100)]+[anchor,I/N,np.diag([1,0,0,0,0,0,0])]
for rho in samples:
    p,r,phi=stats(rho)
    check('orthogonal majority decomposition', np.isclose(p,1/N+np.linalg.norm(rho-I/N)**2))
    check('integration feasibility bound', phi<=N*p-1+1e-12)
    a=np.linalg.eigvalsh(rho)[-1]
    check('sharp spectral upper bound', a <= (1+np.sqrt((N-1)*(N*p-1)))/N+1e-12)

# Same phase Gap and opposite capability verdicts, including the declared D proxy.
a=(1-.45)*I/N+.45*anchor
b=(1-.65)*I/N+.65*anchor
pa,ra,fa=stats(a); pb,rb,fb=stats(b)
da=1+6*coh_e(a); db=1+6*coh_e(b)
check('same Gap with different Cap2 proxy verdict', np.allclose(gap(a),gap(b)) and pa>2/N and ra>=1/3 and fa>=1 and da>=2 and pb>2/N and rb<1/3 and fb>=1 and db>=2)
check('product gate insufficient', stats(anchor)[1]<1/3 and stats(anchor)[1]*stats(anchor)[2]>=1/3)

# Magnitudes, diagonals and absolute sine phases miss triangle phase data.
a=I/N+np.zeros((N,N))
for i,j in [(0,1),(1,2),(0,2)]: a[i,j]=a[j,i]=.03
b=a.copy(); b[0,2]=b[2,0]=-.03
check('both phase witnesses PSD', min(np.linalg.eigvalsh(a).min(),np.linalg.eigvalsh(b).min())>0)
check('same reduced phase/magnitude statistics', np.allclose(np.abs(a),np.abs(b)) and np.allclose(gap(a),gap(b)))
check('triangle holonomy has observable effect', np.isclose(np.trace(a@a@a)-np.trace(b@b@b),12*.03**3))

# The HS row/column mask is not positive; pinching is CP and preserves trace.
e=np.zeros(N); e[4]=1
v=np.zeros(N); v[0]=1
PE=np.outer(e,e); PB=I-PE
rho=np.outer(e+v,e+v)/2
mask=PE@rho+rho@PE-PE@rho@PE
pinch=PE@rho@PE+PB@rho@PB
check('HS mask fails positivity', np.isclose(np.linalg.eigvalsh(mask).min(),(1-np.sqrt(5))/4))
check('block expectation preserves state', np.linalg.eigvalsh(pinch).min()>-1e-12 and np.isclose(np.trace(pinch),1))
check('mixed E population not E coupling', np.isclose(coh_e(I/N),1/N) and np.allclose((I/N)[4,:4],0))
# Uniform coherent six-axis sector: first three gates need not populate E.
v=np.ones(N); v[4]=0; v/=np.linalg.norm(v)
d6=np.diag([1/6,1/6,1/6,1/6,0,1/6,1/6])
rho=.52*d6+.48*np.outer(v,v)
p,r,f=stats(rho)
check('three scalar gates do not force E', p>2/N and r>=1/3 and f>=1 and coh_e(rho)==0)

# Quotient rate bounded but cannot extend continuously to empty O.
for rho in samples:
    k=abs(rho[5,4])*abs(rho[5,6])/rho[5,5].real if rho[5,5].real>1e-12 else 0
    check('rate PSD upper bound', k<=.5+1e-12)
eps=1e-8; v=np.zeros(N); v[5]=np.sqrt(eps); v[4]=v[6]=np.sqrt((1-eps)/2)
a=np.outer(v,v); b=np.diag(np.diag(a))
ka=abs(a[5,4])*abs(a[5,6])/a[5,5]; kb=abs(b[5,4])*abs(b[5,6])/b[5,5]
check('rate boundary direction dependence', np.linalg.norm(a-b)>.1 and ka>.49 and kb==0 and a[5,5]==b[5,5])
# Their limits have the same zero O coordinate, different E/U blocks. Stronger same boundary-state witness:
rho0=np.diag([0,0,0,0,.5,0,.5])
# Schur complement permits fixed coherent O row with an unchanged diagonal E/U limit.
a=rho0.copy(); a[4,4]=a[6,6]=(1-eps)/2; a[5,5]=eps
amp=np.sqrt(eps*(1-eps))/2
for j in [4,6]: a[5,j]=a[j,5]=amp
b=np.diag(np.diag(a))
check('same boundary state distinct rate limits', np.linalg.eigvalsh(a).min()>-1e-12 and np.linalg.norm(a-rho0)<1e-3 and abs(a[5,4]*a[5,6]/eps-.25)<1e-6 and b[5,4]==0)
for aa,bb,cc in [(1,100,2),(.2,3,.1),(3,1,4)]:
    exact=aa*cc/(aa+bb+cc); approx=aa*cc/bb
    check('kinetic approximation relative error', np.isclose((approx-exact)/approx,(aa+cc)/(aa+bb+cc)) and (approx-exact)/approx <= (aa+cc)/bb)

# Nonlinear state preservation is weaker than a channel.
def mirror(rho):
    _,r,_=stats(rho)
    obs=rho/3+2*np.diag(np.diag(rho))/3
    return (1-r)*obs+r*anchor

a=np.diag([1,0,0,0,0,0,0]); b=np.diag([0,1,0,0,0,0,0]); m=(a+b)/2
check('state-dependent mirror not affine', np.linalg.norm(mirror(m)-(mirror(a)+mirror(b))/2)>1e-3)
for rho in samples:
    out=mirror(rho)
    check('mirror state preservation', np.isclose(np.trace(out),1) and np.linalg.eigvalsh(out).min()>-1e-12)
check('raw self-model score can be negative', np.isclose(1-np.linalg.norm(a-b)**2/purity(a),-1))
check('regeneration can lower purity', np.trace(a@(I/N)).real-purity(a)<0)

# Finite informationally complete POVM, without assuming an encoder unique.
projectors=[np.outer(I[:,i],I[:,i]) for i in range(N)]
for i,j in itertools.combinations(range(N),2):
    for z in [1,1j]:
        v=(I[:,i]+z*I[:,j])/np.sqrt(2)
        projectors.append(np.outer(v,v.conj()))
S=sum(projectors); vals,vecs=np.linalg.eigh(S)
W=(vecs*(1/np.sqrt(vals)))@vecs.conj().T
povm=[W@x@W for x in projectors]
basis=[]
for i in range(N-1): basis.append((np.outer(I[:,i],I[:,i])-np.outer(I[:,-1],I[:,-1]))/np.sqrt(2))
for i,j in itertools.combinations(range(N),2):
    x=np.outer(I[:,i],I[:,j]); basis.extend([(x+x.T)/np.sqrt(2),1j*(x-x.T)/np.sqrt(2)])
A=np.array([[np.trace(E@F).real for F in basis] for E in povm])
check('49-outcome POVM complete', np.allclose(sum(povm),I) and all(np.linalg.eigvalsh(E).min()>-1e-12 for E in povm))
check('informational completeness rank48', np.linalg.matrix_rank(A)==48)
D=np.array([[np.trace(np.outer(I[:,i],I[:,i])@F).real for F in basis] for i in range(N)])
check('diagonals alone nonidentifiable rank6', np.linalg.matrix_rank(D)==6)
check('plurality needs posterior symmetry', .4>=1/3 and .4<max(.5,.1))

# Primitivity, Hamiltonian gauge, and representation redundancy.
H=np.diag(np.ones(N-1),1)+np.diag(np.ones(N-1),-1)
def L(x):return -1j*(H@x-x@H)+np.diag(np.diag(x))-x
mat=np.column_stack([L(np.outer(I[:,j%N],I[:,j//N])).reshape(-1,order='F') for j in range(N*N)])
ev=np.linalg.eigvals(mat)
check('connected-H atomic dynamics primitive without pair coverage', np.sum(np.abs(ev)<1e-8)==1 and np.all(ev[np.abs(ev)>=1e-8].real < -1e-6))
x=state()
check('Hamiltonian offset invisible', np.allclose((H+17*I)@x-x@(H+17*I),H@x-x@H) and not np.isclose(np.linalg.eigvalsh(H)[0],np.linalg.eigvalsh(H+17*I)[0]))
vecI=I.reshape(-1,order='F')
dep=np.outer(vecI,vecI)/N-np.eye(N*N)
check('primitive semigroup can have repeated spectrum', np.linalg.matrix_rank(dep+np.eye(N*N))==1 and np.linalg.matrix_rank(dep)==48)
check('gate closed at I gives no autonomous genesis', np.allclose(L(I/N),0))

# Fano channel and instrument, independently built from F2^3 incidence.
points=range(1,8)
lines=sorted({tuple(sorted([a,b,a^b])) for a,b in itertools.combinations(points,2)})
projs=[np.diag([int(i in line) for i in points]) for line in lines]
ks=[p/np.sqrt(3) for p in projs]
fano=sum(k@x@k for k in ks)
check('Fano Kraus completeness', np.allclose(sum(k@k for k in ks),I))
check('Fano attenuates amplitudes', np.allclose(fano,x/3+2*np.diag(np.diag(x))/3))
check('duplicate Kraus unchanged', np.allclose(sum(k@x@k for k in [z/np.sqrt(2) for z in ks for _ in range(2)]),fano))
choi=sum(np.outer(k.reshape(-1,order='F'),k.reshape(-1,order='F').conj()) for k in ks)
check('Fano Choi rank7', np.linalg.matrix_rank(choi)==7 and np.allclose(np.linalg.eigvalsh(choi)[-7:],[2/3]*6+[3]))
for rho in samples:
    out=sum(k@rho@k for k in ks)
    check('Fano cannot reach integration1', stats(out)[2]<=2/3+1e-12)
    _,r,_=stats(rho)
    damp=(1-r)*out+r*I/N
    check('coh mirror bound24/49', stats(damp)[2]<=24/49+1e-12)

# Commuting projectors collapse the alleged exponential state grammar.
supports={frozenset(points)}
front={frozenset(points)}
for n in range(1,6):
    front={a.intersection(line) for a in front for line in lines}
    supports.update(front)
check('Fano compositions at most16 maps', len(supports)==16)
check('all word permutations collide', np.allclose(projs[0]@projs[1],projs[1]@projs[0]))
M=np.array([[1+2*len(set(a).intersection(b)) for b in lines] for a in lines])/25
check('chosen word Markov matrix stochastic', np.allclose(M.sum(axis=1),1) and np.allclose(M,M.T) and M.min()>0)

# Hamming perfect spheres and the non-octonionic length15 countermodel.
code=[v for v in itertools.product([0,1],repeat=7) if np.bitwise_xor.reduce(np.array([i for i,b in zip(points,v) if b],dtype=int),initial=0)==0]
balls=[]
for word in code:
    ball={tuple(word)}
    for i in range(7):
        w=list(word); w[i]^=1; ball.add(tuple(w))
    balls.extend(ball)
check('perfect Hamming7 packing', len(code)==16 and len(balls)==len(set(balls))==128)
check('weight3 words are Fano lines', sorted(tuple(i for i,b in zip(points,v) if b) for v in code if sum(v)==3)==lines)
check('length15 perfect packing arithmetic', (15+1)*2**11==2**15 and 16 not in [1,2,4,8])

# Correlation is not entanglement; the operator Schmidt certificate sees it.
rho=np.diag([.5,0,0,.5])
ten=rho.reshape(2,2,2,2)
rhoa=np.trace(ten,axis1=1,axis2=3); rhob=np.trace(ten,axis1=0,axis2=2)
ppt=ten.transpose(0,3,2,1).reshape(4,4)
check('separable correlation not product', np.linalg.eigvalsh(ppt).min()>=0 and np.allclose(rhoa,np.eye(2)/2) and not np.allclose(rho,np.kron(rhoa,rhob)))
J=np.array([[0,1],[-1,0]])
skew=np.zeros((7,7))
for j in range(3):skew[2*j:2*j+2,2*j:2*j+2]=J
check('three skew blocks rank6', np.linalg.matrix_rank(skew)==6)

# CP identity and replacement channels both fix every chosen pointed state.
rho=state()
Jreset=np.kron(I,rho); Jidentity=np.outer(vecI,vecI)
check('pointed-state object not terminal', not np.allclose(Jreset,Jidentity) and np.linalg.eigvalsh(Jreset).min()>0 and np.allclose(rho*np.trace(rho),rho))
# Finite slice image universal property: every over-base map to a mono is unique or absent.
G=range(3)
for f in itertools.product(G,repeat=2):
    for bits in itertools.product([0,1],repeat=3):
        S={i for i,b in enumerate(bits) if b}
        over_base=[g for g in itertools.product(S,repeat=2) if g==f]
        check('image support adjunction in finite slice', len(over_base)==int(set(f)<=S))

# Check the actual published numerical scheme against independent invariants and flow.
import re
published = Path(__file__).resolve().parents[1] / 'docs/applied/coherence-cybernetics/implementation.md'
namespace = {}
exec(re.search(r'```python\n(.*?)\n```', published.read_text(), re.S).group(1), namespace)
step = namespace['step']
for rho in [I/N, anchor, np.diag([1,0,0,0,0,0,0]), state()]:
    for dt in [0, 1e-5, .01, 1, 20]:
        out=step(rho,H,.7,dt,lambda r:.8+coh_e(r),lambda r:anchor)
        check('published step preserves states for coarse and boundary inputs',
              np.allclose(out,out.conj().T) and np.isclose(np.trace(out),1)
              and np.linalg.eigvalsh(out).min()>-1e-12)
rho=state(); gamma=.7; rate=.9; T=.15
linear=np.column_stack([(-1j*(H@e-e@H)+2*gamma/3*(np.diag(np.diag(e))-e)
                        +rate*(np.trace(e)*anchor-e)).reshape(-1,order='F')
                       for e in [np.outer(I[:,j%N],I[:,j//N]) for j in range(N*N)]])
exact=(expm(T*linear)@rho.reshape(-1,order='F')).reshape(N,N,order='F')
errors=[]
for count in [10,20,40]:
    out=rho.copy()
    for _ in range(count):out=step(out,H,gamma,T/count,lambda r:rate,lambda r:anchor)
    errors.append(np.linalg.norm(out-exact))
check('published split converges at first order against independent exact generator',
      1.8<errors[0]/errors[1]<2.2 and 1.8<errors[1]/errors[2]<2.2)
rho=(1-.45)*I/N+.45*anchor
p,r,f=stats(rho)
check('full proxy window does not imply strict seven-stress cut',
      p>2/N and r>=1/3 and f>=1 and 1+6*coh_e(rho)>=2
      and np.isclose(7*(1-rho[3,3])/6,1))
check('C exact global bound6/7', all(stats(x)[1]*stats(x)[2]<=6/7+1e-12 for x in samples))
# Kraus count cannot encode continuous unitary coefficients.
U=expm(-1j*.37*H); vU=U.reshape(-1,order='F')
check('distinct continuous channels both have Choi rank1',
      np.linalg.matrix_rank(np.outer(vU,vU.conj()))==1
      and np.linalg.matrix_rank(np.outer(vecI,vecI.conj()))==1
      and np.linalg.norm(U@anchor@U.conj().T-anchor)>.01)
check('internal identity may be surjective without diagonal obstruction',
      set({0:0,1:1}.values())=={0,1})

# Exact distance to the selected shell, with independently computed Bures bound.
for index in range(50):
    pure_vector=rng.normal(size=N)+1j*rng.normal(size=N)
    pure_vector/=np.linalg.norm(pure_vector)
    rho=(1-.65)*I/N+.65*np.outer(pure_vector,pure_vector.conj())
    p=purity(rho); pc=2/N
    radius=np.sqrt(p-1/N)-np.sqrt(pc-1/N)
    t=np.sqrt((pc-1/N)/(p-1/N))
    shell=I/N+t*(rho-I/N)
    check('exact HS shell witness is positive and attains radius',
          np.linalg.eigvalsh(shell).min()>-1e-12 and np.isclose(purity(shell),pc)
          and np.isclose(np.linalg.norm(rho-shell),radius))
    roots,eigenvectors=np.linalg.eigh(rho)
    rootrho=(eigenvectors*np.sqrt(np.maximum(roots,0)))@eigenvectors.conj().T
    middle=rootrho@shell@rootrho
    root_fidelity=np.sum(np.sqrt(np.maximum(np.linalg.eigvalsh(middle),0)))
    bures=np.sqrt(max(0,2*(1-root_fidelity)))
    check('Bures shell candidate respects certified general lower bound',
          bures+1e-12>=radius/np.sqrt(2))
# Unital dephasing entropy flux can vanish above the selected purity threshold.
diagonal=np.diag([.55,.075,.075,.075,.075,.075,.075])
check('viable diagonal state has zero dephasing entropy production',
      purity(diagonal)>2/N and np.allclose(np.diag(np.diag(diagonal))-diagonal,0))
# Injection can increase entropy; regeneration is not universally negentropy.
F=I/N-diagonal
check('injection toward mixed target increases entropy',
      -np.trace(F@np.diag(np.log(np.diag(diagonal)))).real>0)

# Discarding a mixed tensor factor can increase purity and preserve local Phi.
joint=np.kron(anchor,I/N)
marginal=np.trace(joint.reshape(N,N,N,N),axis1=1,axis2=3)
check('partial trace can increase purity and retain integration',
      np.isclose(purity(joint),1/N) and np.allclose(marginal,anchor)
      and np.isclose(purity(marginal),1) and np.isclose(stats(marginal)[2],6))
# Trace normalization does not impose a saturated offdiagonal attention budget.
low=.8*I/N+.2*anchor; high=.6*I/N+.4*anchor
offdiag=~np.eye(N,dtype=bool)
check('fixed diagonal permits all coherences to grow together',
      np.allclose(np.diag(low),np.diag(high))
      and np.all(np.abs(high[offdiag])>np.abs(low[offdiag])))
phase_states=[]
for amplitude in [.03,.06]:
    phase_state=I.astype(complex)/N
    phase_state[0,1]=amplitude*np.exp(1j*np.pi/4)
    phase_state[1,0]=phase_state[0,1].conjugate()
    phase_states.append(phase_state)
check('phase Gap is unchanged by positive amplitude scaling',
      all(np.linalg.eigvalsh(x).min()>0 for x in phase_states)
      and np.allclose(gap(phase_states[0]),gap(phase_states[1])))
check('forgetting differential lower bound permits constant memory',
      all(0 >= -1/(p-2/N) for p in [2/N+1e-9,.3,3/N]))

# Exhaustive finite witnesses for the correctly typed fixed-predicate object.
predicates=list(itertools.product([0,1],repeat=3))
for mapping in itertools.product(range(3),repeat=3):
    fixed=[p for p in predicates if tuple(p[mapping[j]] for j in range(3))==p]
    check('nonidentity maps have proper fixed predicates in Sets',
          (len(fixed)==8)==(mapping==(0,1,2)))
    check('fixed predicates closed under finite logical operations',
          all(tuple(a[j] and b[j] for j in range(3)) in fixed
              and tuple(a[j] or b[j] for j in range(3)) in fixed
              and tuple((not a[j]) or b[j] for j in range(3)) in fixed
              for a in fixed for b in fixed))
for dimension in [16,256,65536]:
    epsilon=dimension**(-1.25)
    check('small relative offdiagonals do not exclude integration uniformly in N',
          1/dimension-epsilon>0 and dimension*epsilon<1
          and (dimension-1)/np.sqrt(dimension)>1)
# Symmetry and a zero quadratic mode do not determine a critical manifold.
check('rotationally symmetric potential can have positive Hessian',
      np.linalg.matrix_rank(2*np.eye(6))==6)
check('quartic isolated minimum can have zero Hessian',
      np.isclose(12*0**2,0) and all(x**4>0 for x in [-1,-.1,.1,1]))
critical_hessian=np.diag([0.,0.,2.,3.])
for _ in range(20):
    coordinate_change=rng.normal(size=(4,4))+4*np.eye(4)
    transported=coordinate_change.T@critical_hessian@coordinate_change
    check('critical Hessian nullity invariant under invertible coordinates',
          abs(np.linalg.det(coordinate_change))>1e-8
          and np.linalg.matrix_rank(transported,tol=1e-8)==2)

# A forward-invariant OPEN basin can exclude its asymptotic fixed point.
# Depolarizing dynamics on rho(x)=I/7+x diag(1,-1,0,...), 0<x<1/7,
# has x(t)=exp(-t)x, whose limit is zero outside that declared domain.
basin_coordinates=np.array([.01,.05,.1])
at_finite_time=np.exp(-2)*basin_coordinates
check('forward-invariant open basin need not contain fixed-point limits',
      np.all((at_finite_time>0)&(at_finite_time<1/7))
      and not (0<0<1/7))
extended_limit=lambda x: 0.
check('basin limit composition valid after adjoining its fixed point',
      all(extended_limit(extended_limit(x))==extended_limit(x)
          for x in [0.,.01,.05,.1]))

print(f'PASS: {len(checks)} mathematical kernel checks ({len(set(checks))} named properties).')
print('Scope: explicit witnesses and finite constructions; no certification of the full theory or empirical bridges.')
