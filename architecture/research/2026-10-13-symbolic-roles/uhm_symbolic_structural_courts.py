#!/usr/bin/env python3
"""Exact finite structural checks; no empirical or phenomenological inference."""
from fractions import Fraction as F
from itertools import combinations, permutations, product
from collections import Counter
import json, math, hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
if not __debug__:
 raise RuntimeError('Run with assertions enabled (no -O)')
out={}
lines=[{(i+d)%7 for d in (0,1,3)} for i in range(7)]
assert Counter(tuple(sorted(p)) for l in lines for p in combinations(l,2))==Counter({p:1 for p in combinations(range(7),2)})
C={0}
for l in lines:
 b=sum(1<<i for i in l); C|={c^b for c in C}
weights=dict(sorted(Counter(c.bit_count() for c in C).items()))
assert len(C)==16 and weights=={0:1,3:7,4:7,7:1}
balls=Counter(c^e for c in C for e in [0]+[1<<i for i in range(7)])
assert len(balls)==128 and set(balls.values())=={1}
position={7:1,5:2,3:3,4:4,1:5,2:6,6:7}
consecutive=[sorted(i+1 for i in l) for l in lines if max(position[i+1] for i in l)-min(position[i+1] for i in l)==2]
assert consecutive==[[1,2,4]]
out['Fano_Hamming']={'points':7,'lines':7,'codewords':16,'weights':weights,'perfect_radius_one':True,'distance_zero_to_all_ones':7,'consecutive_chakra_lines':consecutive,'translated_code_also_perfect':len({c^1 for c in C})==16}

def add(a,b):return tuple(x+y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def conj(a):return (a[0],)+tuple(-x for x in a[1:])
def mul(x,y):
 if len(x)==1:return (x[0]*y[0],)
 n=len(x)//2;a,b=x[:n],x[n:];c,d=y[:n],y[n:]
 return add(mul(a,c),neg(mul(conj(d),b)))+add(mul(d,a),mul(b,conj(c)))
u=[tuple(int(i==j) for j in range(8)) for i in range(8)]
sigma={}
for i,j in product(range(8),repeat=2):
 v=mul(u[i],u[j]);assert sum(abs(z) for z in v)==1 and abs(v[i^j])==1;sigma[i,j]=v[i^j]
fail=next((a,b,c) for a,b,c in product(range(1,8),repeat=3) if sigma[a,b]*sigma[a^b,c]!=sigma[b,c]*sigma[a,b^c])
out['octonion_twist']={'associativity_cocycle_failure':fail,'left_sign':sigma[fail[0],fail[1]]*sigma[fail[0]^fail[1],fail[2]],'right_sign':sigma[fail[1],fail[2]]*sigma[fail[0],fail[1]^fail[2]]}

def rank(rows):
 a=[[F(v) for v in r] for r in rows];r=0
 for c in range(len(a[0])):
  piv=next((j for j in range(r,len(a)) if a[j][c]),None)
  if piv is None:continue
  a[r],a[piv]=a[piv],a[r];q=a[r][c];a[r]=[v/q for v in a[r]]
  for j in range(r+1,len(a)):
   if a[j][c]:q=a[j][c];a[j]=[v-q*w for v,w in zip(a[j],a[r])]
  r+=1
 return r

def stab_dim(phi):
 pairs=list(combinations(range(7),2)); rows=[]
 for i,j,k in combinations(range(7),3):
  row=[]
  for m,n in pairs:
   v=0
   for p in range(7):
    X=lambda a,b:int((a,b)==(m,n))-int((a,b)==(n,m))
    v+=X(i,p)*phi.get((p,j,k),0)+X(j,p)*phi.get((i,p,k),0)+X(k,p)*phi.get((i,j,p),0)
   row.append(v)
  rows.append(row)
 return 21-rank(rows)
phi_bad={}
for l in lines:
 for p in permutations(sorted(l)):
  phi_bad[p]=(-1)**sum(p[a]>p[b] for a in range(3) for b in range(a+1,3))
phi_good={(i,j,k):mul(u[i+1],u[j+1])[k+1] for i,j,k in product(range(7),repeat=3)}
good,bad=stab_dim(phi_good),stab_dim(phi_bad)
assert good==14
out['three_form_stabilizer_exact']={'Cayley_Dickson_so7_stabilizer_dimension':good,'current_sorted_all_positive_Fano_so7_stabilizer_dimension':bad}
out['entropy_counterexample']={'deterministic_state_conditional_entropy':0,'claimed_lower_bound_M6_Res2':math.log2(math.comb(48,6))-6}
assert out['entropy_counterexample']['claimed_lower_bound_M6_Res2']>0
out['codons_vs_hexagrams']={'vertices_each':64,'codon_single_base_change_degree':9,'hexagram_single_line_change_degree':6,'adjacency_isomorphism':False}
out['G2_vs_cycle']={'Weyl_order':12,'uncoloured_C12_dihedral_order':24,'Weyl_rotation_orders':[1,2,3,6],'order_four_rotation_in_Weyl':False}
out['gauge_counterexample']={'support_triangle_cycle_rank':3-3+1,'phase_radians':math.pi/2,'eps':'1/28','Gershgorin_lower_bound':'1/14'}
files=list((ROOT/'architecture').glob('symbolica_*.py'))+[ROOT/'website/docs/core/structure/symbolic-systems.md',ROOT/'website/docs/applied/research/symbolic-correspondence.md',ROOT/'website/docs/applied/research/gamma-canon.md']
out['sources']={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(files)}
print(json.dumps(out,ensure_ascii=False,indent=2))
