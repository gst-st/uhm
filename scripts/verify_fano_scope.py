#!/usr/bin/env python3
"""Exact 3x3 Sylvester solves inside a full-rank 7x7 state; no eigensolvers."""
from fractions import Fraction as F
import json

def solve(a,b):
    n=len(b)
    m=[list(map(F,row))+[F(value)] for row,value in zip(a,b)]
    for c in range(n):
        r=next(i for i in range(c,n) if m[i][c])
        m[c],m[r]=m[r],m[c]
        pivot=m[c][c]
        m[c]=[x/pivot for x in m[c]]
        for i in range(n):
            if i!=c:
                factor=m[i][c]
                m[i]=[x-factor*y for x,y in zip(m[i],m[c])]
    return [row[-1] for row in m]

def sylvester(a,x):
    n=len(a)
    coeff=[]
    for i in range(n):
        for j in range(n):
            coeff.append([sum((a[i][k] if (r,s)==(k,j) else 0)+
                              (a[k][j] if (r,s)==(i,k) else 0)
                              for k in range(n)) for r in range(n) for s in range(n)])
    y=solve(coeff,[v for row in x for v in row])
    y=[y[i*n:(i+1)*n] for i in range(n)]
    assert all(sum(a[i][k]*y[k][j]+y[i][k]*a[k][j] for k in range(n))==x[i][j]
               for i in range(n) for j in range(n))
    return y

def audit(c, edges):
    assert all(0 <= i < 3 and 0 <= j < 3 and i != j for i,j in edges)
    a=F(1,7)
    rho=[[a if i==j else c if (i,j) in edges or (j,i) in edges else F(0)
          for j in range(7)] for i in range(7)]
    # Strict diagonal dominance proves positive definiteness for these real
    # symmetric examples; the single-edge c=a/2 case also satisfies it.
    assert all(rho[i][i]>sum(abs(rho[i][j]) for j in range(7) if i!=j) for i in range(7))
    block=[row[:3] for row in rho[:3]]
    def norm(delta):
        x=[row[:3] for row in delta[:3]]
        y=sylvester(block,x)
        # g_B(X,X)=1/2 Tr[X (L_rho+R_rho)^-1 X].
        return F(1,2)*sum(x[i][j]*y[j][i] for i in range(3) for j in range(3)) + sum(delta[i][i]**2/(4*a) for i in range(3,7))
    def contribution(indices,weight):
        p=sum(rho[i][i] for i in indices)
        delta=[[rho[i][j]/p*(i in indices and j in indices)-rho[i][j]
                for j in range(7)] for i in range(7)]
        return F(1,7)*weight*p*norm(delta)  # gamma=1, rate gamma/N.
    atomic=sum(contribution({i},F(1)) for i in range(7))
    lines=[{(k+j)%7 for j in (0,1,3)} for k in range(7)]
    fano=sum(contribution(line,F(1,3)) for line in lines)
    return dict(coherence=str(c),edges=edges,atomic=str(atomic),fano=str(fano),
                full_over_atomic=str((atomic+fano)/atomic))

print('проверок: 1')
single=audit(F(1,14),[(0,1)])
assert F(single['atomic'])==F(133,588) and single['full_over_atomic']=='11/9'
assert F(single['fano'])==F(133,2646)
assert F(single['atomic'])!=F(3,14)
assert F(single['atomic'])+F(single['fano'])!=F(11,42)
print(json.dumps({'status':'passed','arithmetic':'Fraction; verified Sylvester equations',
                  'single_edge':single},indent=2))
