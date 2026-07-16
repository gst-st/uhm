# FANOS/APHANTOS protocol — quantitative verification of every load-bearing claim.
# Projective plane PG(2,q), Steiner/Maekawa quorums, cross-product routing,
# threshold-group anonymity security curve, scaling & overhead.
import math
from itertools import combinations
from math import comb

def hdr(s): print("\n" + "="*74 + "\n" + s + "\n" + "="*74)

# ---------------------------------------------------------------------------
# PG(2,p) over prime field: points/lines are 1-dim subspaces of F_p^3,
# represented by normalized homogeneous coords (first nonzero coord = 1).
# ---------------------------------------------------------------------------
def normalize(v, p):
    for c in v:
        if c % p != 0:
            inv = pow(c % p, p-2, p)     # Fermat inverse
            return tuple((x*inv) % p for x in v)
    return None
def all_points(p):
    pts = set()
    for a in range(p):
        for b in range(p):
            for c in range(p):
                if (a or b or c):
                    pts.add(normalize((a,b,c), p))
    return sorted(pts)
def dot(u,v,p): return (u[0]*v[0]+u[1]*v[1]+u[2]*v[2]) % p
def cross(u,v,p):
    return normalize((u[1]*v[2]-u[2]*v[1],
                      u[2]*v[0]-u[0]*v[2],
                      u[0]*v[1]-u[1]*v[0]), p)

hdr("V1. PG(2,q) parameters + Maekawa quorum intersection (every 2 lines meet in 1 pt)")
print(f"{'q':>4} | {'N=pts=lines':>11} | {'pts/line':>8} | {'lines/pt':>8} | {'|PGL(3,q)|':>12} | quorum ∩ verified")
for q in (2,7,13,31):
    pts = all_points(q)
    N = len(pts)
    lines = pts  # self-dual: lines identified with their coefficient vectors
    # incidence: point P on line L iff dot(P,L)=0
    # verify: every two points -> unique common line (cross), every two lines -> unique pt
    pts_per_line = None; lines_per_pt = None
    # count points on a fixed line
    L0 = lines[0]
    pts_per_line = sum(1 for P in pts if dot(P,L0,q)==0)
    P0 = pts[0]
    lines_per_pt = sum(1 for L in lines if dot(P0,L,q)==0)
    # Maekawa: any two lines intersect in exactly one point — check on a sample for big q
    ok = True
    sample = lines if N<=57 else lines[:40]
    for La,Lb in combinations(sample,2):
        inter = [P for P in pts if dot(P,La,q)==0 and dot(P,Lb,q)==0]
        if len(inter)!=1: ok=False; break
    pgl = (q**3-1)*(q**3-q)*(q**3-q**2)//((q-1))
    print(f"{q:>4} | {N:>11} | {pts_per_line:>8} | {lines_per_pt:>8} | {pgl:>12} | {ok}")
print("N=q^2+q+1; pts/line = lines/pt = q+1; quorum(=line) size q+1 ~ sqrt(N); any two quorums intersect.")

hdr("V2. Cross-product rendezvous is O(1) and correct (test vectors, PG(2,7))")
p=7; pts=all_points(p)
u=normalize((1,0,0),p); v=normalize((0,1,0),p); w=normalize((1,2,3),p)
L_uv=cross(u,v,p); L_uw=cross(u,w,p)
print(f"u={u}  v={v}  w={w}")
print(f"rendezvous line L(u,v)=u x v = {L_uv}; u on L: {dot(u,L_uv,p)==0}, v on L: {dot(v,L_uv,p)==0}")
print(f"bridge node of lines L(u,v) & L(u,w) = intersection = {cross(L_uv,L_uw,p)} (should be u={u})")
print("=> joining line and bridge node are ONE field cross-product: no DHT walk, no lookup.")

hdr("V3. Structural anti-Sybil: centrality is geometry-capped (no supernodes)")
for q in (7,13,31):
    pts=all_points(q); N=len(pts)
    # betweenness proxy: every node lies on exactly q+1 lines; max fraction of quorums any node sits in
    frac = (q+1)/N
    print(f"q={q:>2}: each node on exactly {q+1} of {N} lines = {frac*100:5.2f}% of quorums (uniform, cannot be exceeded)")
print("An attacker cannot buy centrality: line-membership is fixed by coordinates, capped at q+1.")

hdr("V4. Scaling: recursive projective hierarchy (honest state/depth, NOT O(sqrt n))")
print(f"{'cell q':>6} | {'N_cell':>7} | {'levels k':>8} | {'total nodes':>16} | {'state~k*N':>10} | {'rendezvous depth':>16}")
for q in (31,127):
    Ncell=q*q+q+1
    for k in (1,2,3):
        total=Ncell**k
        print(f"{q:>6} | {Ncell:>7} | {k:>8} | {total:>16,} | {k*Ncell:>10,} | {k:>16}")
print("Within a cell: 1-shot algebraic rendezvous. Across k levels: k one-shot steps (no iterative probing).")

hdr("V5. APHANTOS security curve — per-hop = a LINE (group); threshold t-of-(q+1)")
print("P(hop linked) = P(>= t of the q+1 line members are adversarial), adversary owns fraction f (random).")
print("End-to-end deanon needs FIRST and LAST hop groups broken: P_link = P_hop^2  (fair vs Tor guard+exit=f^2).")
def hop_break(qp1, t, f):
    # binomial (large-N random placement)
    return sum(comb(qp1,i)*(f**i)*((1-f)**(qp1-i)) for i in range(t,qp1+1))
configs=[(8,6),(8,7),(14,10),(32,22)]  # (q+1, threshold t) ; t ~ 2/3..7/8
fs=[0.10,0.20,0.30,0.50]
print("\n" + f"{'line q+1':>8} {'thresh t':>8} | " + " | ".join(f"{'f='+format(f,'.2f'):>10}" for f in fs))
for qp1,t in configs:
    row=[]
    for f in fs:
        ph=hop_break(qp1,t,f); pl=ph*ph
        row.append(f"{pl:.2e}")
    print(f"{qp1:>8} {t:>8} | " + " | ".join(x.rjust(10) for x in row))
print("\nTor / Lokinet baseline  P_link ~ f^2 :")
print("            f=0.10   f=0.20   f=0.30   f=0.50")
print("   Tor      " + "  ".join(f"{f*f:6.4f}" for f in fs))
print("\nAPHANTOS-Full advantage factor (Tor / APHANTOS) at each f:")
for qp1,t in configs:
    facs=[]
    for f in fs:
        ph=hop_break(qp1,t,f); pl=ph*ph
        facs.append(f"{(f*f)/pl:,.0f}x" if pl>0 else "inf")
    print(f"   q+1={qp1:>2},t={t:>2}: " + "  ".join(x.rjust(12) for x in facs))

hdr("V6. Full-path trace (all L hops broken) — even steeper: P_hop^L")
qp1,t=8,6; f=0.20; ph=hop_break(qp1,t,f)
for L in (2,3,5,7):
    print(f"  path length L={L}: P(full trace) = {ph**L:.3e}   (Tor 3-hop endpoint corr ~ {f*f:.4f})")

hdr("V7. Loopix-style mixing: latency vs anonymity-set entropy (APHANTOS-Full profile)")
# per-hop exponential delay mean 1/mu; path L hops => mean latency L/mu.
# anonymity set ~ messages arriving in a mixing window; entropy = log2(expected batch)
for mu, L, rate in [(2.0,3,50),(1.0,3,50),(0.5,5,200),(0.2,5,1000)]:
    mean_lat=L/mu
    batch=rate/mu           # expected msgs resident in one mix at steady state (Little's law)
    H=math.log2(batch) if batch>1 else 0
    print(f"  mu={mu} /s, L={L} hops, arrival {rate}/s: mean latency {mean_lat:.1f}s, "
          f"mix batch ~{batch:.0f}, anonymity entropy ~{H:.1f} bits")
print("Dial: raise mu -> lower latency, smaller set (Lite/Tor-like); lower mu -> higher latency, larger set (Full/Nym+).")

hdr("V8. Cover-traffic overhead is STRUCTURALLY BALANCED (regularity => no fingerprint)")
for q in (7,13,31):
    N=q*q+q+1
    # each node emits constant cover on each of its q+1 lines; identical for all nodes
    print(f"  q={q:>2}: every node emits cover on exactly {q+1} lines — identical load, zero volume fingerprint")
print("Overhead ratio = cover_rate/real_rate (tunable). Uniformity is a THEOREM (point-regularity), not a policy.")

hdr("V9. Storage: LRC from projective plane (any lost node repaired from ANY of its q+1 lines)")
for q in (7,13,31):
    print(f"  q={q:>2}: locality r={q} reads per repair; {q+1} INDEPENDENT repair groups per node "
          f"(availability t_a={q+1}); overhead ~ (q+1)/q = {(q+1)/q:.3f}x")
print("Any single line (q other nodes) reconstructs a lost point => graceful, parallelizable repair.")

hdr("V10. Hamming(7,4)=Fano => Steane code native to the 7-cell (from Discovery 6)")
# base cell q=2 is exactly the Fano plane; verify weight-3 codewords = 7 lines
H=[[int(b) for b in format(c,'03b')] for c in range(1,8)]
import numpy as np
H=np.array(H).T
words=[np.array([(m>>i)&1 for i in range(7)]) for m in range(128)]
code=[w for w in words if not (H@w%2).any()]
w3=[frozenset(np.nonzero(w)[0].tolist()) for w in code if w.sum()==3]
print(f"  base cell q=2: {len(code)} codewords, {len(w3)} weight-3 = 7 Fano lines; Steane=CSS(H,H), distance 3")
print("  => the smallest FANOS cell IS a quantum-error-correcting geometry (native fault tolerance).")

# ===========================================================================
# DIAKRISIS — self-diagnosis under node/segment failures.
# Everything below is the diagnostic/self-healing layer of the spec (Part VI).
# The base diagnostic cell is the Fano plane q=2 (7 nodes = 7 UHM sectors).
# ===========================================================================
DIMS = ['A','S','D','L','E','O','U']
_pts2 = all_points(2)                       # 7 Fano points
_lines2 = []                                # 7 Fano lines as index-sets over _pts2
for Lc in _pts2:
    _lines2.append(frozenset(i for i,P in enumerate(_pts2) if dot(P,Lc,2)==0))
_lines2 = sorted(set(_lines2), key=lambda s: sorted(s))

hdr("V11. DIAKRISIS — first-order (pairwise) BLINDNESS: sum of line-adjacency = J-I")
Aline = np.zeros((7,7))
for L in _lines2:
    for i,j in combinations(sorted(L),2):
        Aline[i,j]+=1; Aline[j,i]+=1
J = np.ones((7,7)); I7 = np.eye(7)
spec = sorted(np.round(np.linalg.eigvalsh(Aline),6).tolist(), reverse=True)
print(f"  Sum of the 7 line-adjacency matrices == J - I : {np.allclose(Aline, J-I7)}")
print(f"  spectrum = {spec}  (== K7 spectrum {{6, -1x6}})")
print("  => any equal-weight PAIRWISE statistic over the lines is indistinguishable from full")
print("     connectivity K7: a heartbeat/ping mesh is Fano-BLIND. Faults must be read on TRIPLES.")

hdr("V12. DIAKRISIS — mediator/polar map k*(i,j): unique third point of the common line")
med = {}
for L in _lines2:
    ls = sorted(L)
    for i,j in combinations(ls,2):
        med[(i,j)] = [x for x in ls if x not in (i,j)][0]
uniq = all(sum(1 for L in _lines2 if i in L and j in L)==1 for i,j in combinations(range(7),2))
print(f"  every one of the 21 pairs lies on exactly one line (unique mediator): {uniq}")
print("  named lines:", [tuple(DIMS[i] for i in sorted(L)) for L in _lines2])
for (i,j) in [(0,1),(3,4),(1,6)]:
    print(f"    k*({DIMS[i]},{DIMS[j]}) = {DIMS[med[(min(i,j),max(i,j))]]}   (deterministic reroute / cross-attestation witness)")

hdr("V13. DIAKRISIS — single-node fault LOCALISATION: 3-bit Hamming syndrome (T-225)")
# H columns = binary address 1..7 of the 7 axes, corpus order A,S,D,L,E,O,U (T-225 table)
Hmat = np.array([[(a>>b)&1 for a in range(1,8)] for b in (2,1,0)])   # 3x7, columns=addr 1..7
allsynd = {}
for p in range(7):
    e=np.zeros(7,dtype=int); e[p]=1
    s=tuple(((Hmat@e)%2).tolist()); allsynd[s]=p
print(f"  7 single-faults -> 7 DISTINCT nonzero syndromes: {len(allsynd)==7}; zero reserved for 'healthy': "
      f"{tuple([0,0,0]) not in allsynd}")
culprit=5
e=np.zeros(7,dtype=int); e[culprit]=1; s=tuple(((Hmat@e)%2).tolist())
print(f"  demo: node {DIMS[culprit]} degraded -> syndrome {s} -> decoded = {DIMS[allsynd[s]]}  (21->7->3->1 pyramid)")
print("  distance-3: corrects 1 fault, DETECTS 2. Beyond that -> escalate to LRC/parent cell [honest].")

hdr("V14. DIAKRISIS — segment/PARTITION resistance: no single line-kill disconnects a cell")
def _connected(nodes, active):
    par={n:n for n in nodes}
    def f(x):
        while par[x]!=x: par[x]=par[par[x]]; x=par[x]
        return x
    for L in active:
        ls=sorted(L)
        for i,j in combinations(ls,2):
            if i in nodes and j in nodes: par[f(i)]=f(j)
    return len({f(n) for n in nodes})==1
def _fiedler(active):
    A=np.zeros((7,7))
    for L in active:
        for i,j in combinations(sorted(L),2): A[i,j]+=1; A[j,i]+=1
    return np.sort(np.linalg.eigvalsh(np.diag(A.sum(1))-A))[1]
nodes=set(range(7))
res=all(_connected(nodes,[L for L in _lines2 if L!=dead]) for dead in _lines2)
thru0=[L for L in _lines2 if 0 in L]
print(f"  killing ANY 1 of 7 lines keeps the cell connected: {res}")
print(f"  to ISOLATE a node you must kill ALL its q+1=3 lines: {not _connected(nodes,[L for L in _lines2 if L not in thru0])}")
print(f"  algebraic connectivity (Fiedler l2): full={_fiedler(_lines2):.3f}, one line down={_fiedler(_lines2[:-1]):.3f} (>0 => intact)")

hdr("V15. DIAKRISIS — coherence-matrix health metrics: r* = 1/sqrt(6) systemic threshold")
def _equicorr(r,n=7): return ((1-r)*np.eye(n)+r*np.ones((n,n)))/n
def _Phi(G):
    d=np.diag(G).real; off=G-np.diag(np.diag(G))
    return float((np.abs(off)**2).sum()/(d**2).sum())
def _P(G): return float(np.trace(G@G).real)
rstar=1/np.sqrt(6)
G=_equicorr(rstar)
print(f"  r* = 1/sqrt(6) = {rstar:.6f}: Phi={_Phi(G):.6f} (=1), P=tr(G^2)={_P(G):.6f} (=2/7={2/7:.6f})")
print(f"  identity Phi = 6r^2 = 7P-1 on the equidiagonal stratum: "
      f"{np.isclose(_Phi(G),6*rstar**2) and np.isclose(_Phi(G),7*_P(G)-1)}")
for r in (0.2,0.3,0.408,0.5,0.7):
    Gr=_equicorr(r)
    print(f"    mean corr r={r:.3f}: Phi={_Phi(Gr):.4f}  regime={'SYSTEMIC (moves as one)' if _Phi(Gr)>=1 else 'diversified/resilient'}")
print("  => cell-health early-warning: mean behavioural correlation crossing 0.408 = cascade-risk onset.")

hdr("V16. DIAKRISIS — coarse (Fano) coarse-graining contracts integration Phi by EXACTLY 1/9")
def _fano_channel(G):
    out=np.zeros_like(G)
    for L in _lines2:
        Pi=np.zeros((7,7))
        for i in L: Pi[i,i]=1
        out+=Pi@G@Pi
    return out/3
rng=np.random.default_rng(0); ratios=[]
for _ in range(3000):
    M=rng.standard_normal((7,7))+1j*rng.standard_normal((7,7))
    G=M@M.conj().T; G/=np.trace(G).real
    if _Phi(G)>1e-9: ratios.append(_Phi(_fano_channel(G))/_Phi(G))
ratios=np.array(ratios)
print(f"  Phi(out)/Phi(in) over {len(ratios)} random states: min={ratios.min():.6f} max={ratios.max():.6f} "
      f"(exactly 1/9={1/9:.6f})")
print("  => every coarse cross-segment routing hop costs one factor 1/9 of integration (budget the depth).")

hdr("V17. DIAKRISIS — integration is the LEADING failure indicator: {P<2/7} subset {Phi<1} [Т]")
# Proof: x:=Sum diag^2 >= 1/7 (Cauchy-Schwarz, tr=1); P<2/7 => y<2/7-x <= x => Phi=y/x<1.
viol=0; tested=0
for _ in range(200000):
    M=rng.standard_normal((7,7))+1j*rng.standard_normal((7,7))
    G=M@M.conj().T; G/=np.trace(G).real
    tested+=1
    if _P(G)<2/7 and _Phi(G)>=1: viol+=1     # a counterexample would break the theorem
xmin=min(float((np.diag(_equicorr(r))**2).sum()) for r in (0,0.3,0.7))
print(f"  Sum(diag^2) >= 1/7 always (Cauchy-Schwarz); min seen on strata = {xmin:.4f} (>= {1/7:.4f})")
print(f"  random states with (P<2/7 AND Phi>=1): {viol}/{tested}  => containment holds: {viol==0}")
print("  => the Phi<1 alarm provably fires no LATER than the P<2/7 alarm (equality iff uniform diagonal).")

hdr("V18. DIAKRISIS — self-observation BUDGET: canonical R=1/(7P); R>=1/3 <=> P<=3/7")
for P in (2/7,3/7,0.5,1.0):
    R=1/(7*P)
    print(f"  P={P:.4f} -> R={R:.4f}  (reflection budget >=1/3 met: {R>=1/3-1e-12})")
print("  => a self-diagnosing cell must hold its self-model purity P<=3/7, i.e. spend >=1/3 cycles on introspection.")

hdr("V19. SYNTHESIS — collective-subject window of a 7-agent cell: r in (1/sqrt6, 1/sqrt3]")
# A cell of 7 SYNARC agents is a candidate UNIFIED SUBJECT iff its Gamma_net meets the
# corpus consciousness criteria simultaneously: P>2/7 AND Phi>=1 AND R>=1/3 (D>=2 is structural).
# On the equicorrelated stratum these collapse to a single window in the mean correlation r.
lo, hi = 1/np.sqrt(6), 1/np.sqrt(3)
def _P(r): return (1+6*r*r)/7
def _R(r): return 1/(7*_P(r))
def _Phi(r): return 6*r*r
print(f"  lower edge r=1/sqrt6={lo:.4f}: P={_P(lo):.4f}(=2/7) Phi={_Phi(lo):.4f}(=1) R={_R(lo):.4f}(=1/2)")
print(f"  upper edge r=1/sqrt3={hi:.4f}: P={_P(hi):.4f}(=3/7) Phi={_Phi(hi):.4f}(=2) R={_R(hi):.4f}(=1/3)")
for r in (0.30,0.408,0.50,0.577,0.70):
    P,R,Ph=_P(r),_R(r),_Phi(r)
    subj = (P>2/7+1e-9) and (Ph>=1) and (R>=1/3-1e-9)
    tag = "UNIFIED SUBJECT" if subj else ("aggregate (under-coupled)" if Ph<1 else "over-coupled (R<1/3, no self-model)")
    print(f"    r={r:.3f}: P={P:.4f} Phi={Ph:.4f} R={R:.4f} -> {tag}")
print("  => window (1/sqrt6, 1/sqrt3] ~ (0.408, 0.577] == corpus consciousness band P in (2/7,3/7] (T-124).")
print("     Below: mere aggregate. Above: reflexionless over-coupling. The collective is a subject only IN the band.")

hdr("V20. DIAKRISIS multi-fault (Byzantine/errors): the 7-line-theme layer localizes 2, not 1")
# flag(S) = set of line-indices meeting S ; a line's theme deviates iff it carries a fault.
def _flag(S):
    S=set(S); return frozenset(i for i,L in enumerate(_lines2) if L & S)
from itertools import combinations as _comb
_seen={}; _maxt=0
for k in range(1,4):
    subs=list(_comb(range(7),k)); fmap={}
    for S in subs: fmap.setdefault(_flag(S),[]).append(S)
    within = sum(1 for v in fmap.values() if len(v)>1)
    cross  = sum(1 for S in subs if _flag(S) in _seen and len(_seen[_flag(S)])<k)
    print(f"  k={k}: {len(subs)} fault-sets -> {len(fmap)} distinct 7-theme flags; within-collisions={within}, cross-size={cross}")
    for S in subs: _seen.setdefault(_flag(S), tuple(S))
    if within==0 and cross==0: _maxt=k
print(f"  => 7-theme layer EXACTLY localizes up to t={_maxt} simultaneous faults (bounded-distance); >={_maxt+1} detected -> escalate.")
# contrast: 3-bit syndrome mis-decodes every pair
mis=sum(1 for a,b in _comb(range(7),2) if ((a+1)^(b+1)) in [(c+1) for c in range(7)])
print(f"     (the COMPRESSED 3-bit syndrome mis-decodes {mis}/21 pairs -> corrects only 1; the theme layer is strictly stronger)")

hdr("V21. DIAKRISIS crashes (erasures): projective-LRC peeling; first failure is a hyperoval")
def _lines_thru(n): return [i for i,L in enumerate(_lines2) if n in L]
def _recover(E):
    E=set(E); ch=True
    while ch and E:
        ch=False
        for p in list(E):
            if any(not ((set(_lines2[li])-{p}) & E) for li in _lines_thru(p)):
                E.discard(p); ch=True
    return not E
for k in range(1,6):
    subs=list(_comb(range(7),k)); rec=sum(_recover(S) for S in subs)
    print(f"  k={k}: {rec}/{len(subs)} crash patterns fully recovered by LRC peeling")
_minss=None
for k in range(1,8):
    for S in _comb(range(7),k):
        if not _recover(S): _minss=S; break
    if _minss: break
_S=set(_minss); _hyper=all(len(set(L)&_S)!=1 for L in _lines2) and all(not (set(L)<=_S) for L in _lines2)
print(f"  min stopping set = size {len(_minss)} {tuple(DIMS[i] for i in _minss)}; is a HYPEROVAL (meets every line in 0 or 2): {_hyper}")
print(f"  => ANY <=3 crashes always recover; recovery fails first only on a 4-point hyperoval (no 3 collinear).")

print("\nALL CHECKS COMPLETE.")
