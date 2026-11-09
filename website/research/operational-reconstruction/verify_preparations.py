"""Operational separation of real product tests, global tests and complete positivity."""
from fractions import Fraction as F
from itertools import product

def kron(a, b):
    return [[u*v for u in row for v in col] for row in a for col in b]

def expect(a, b):
    return sum(x*b[j][i] for i,row in enumerate(a) for j,x in enumerate(row))

def verify():
    J = [[0,-1],[1,0]]
    I = [[1,0],[0,1]]
    K = kron(J,J)
    ident = kron(I,I)
    states = [[[F(ident[i][j]+sign*K[i][j],4) for j in range(4)] for i in range(4)]
              for sign in [1,-1]]
    for state in states:
        # Twice each state is an orthogonal projector, establishing positivity.
        assert all(sum(2*state[i][k]*state[k][j] for k in range(4))==state[i][j]
                   for i,j in product(range(4),repeat=2))
        assert expect(state,ident)==1
    basis = [[[1,0],[0,0]],[[0,0],[0,1]],[[0,1],[1,0]]]
    for e,f in product(basis, repeat=2):
        assert expect(kron(e,f),states[0])==expect(kron(e,f),states[1])
    assert [2*expect(states[0],s) for s in states]==[1,0]
    bell = [1,0,0,1]
    antisym = [0,1,-1,0]
    # Bell / sqrt(2) and antisym / sqrt(2); transpose the second local index.
    negative = sum(F(antisym[2*i+j]*bell[2*i+l]*bell[2*k+j]*antisym[2*k+l],4)
                   for i,j,k,l in product(range(2),repeat=4))
    assert negative == F(-1,2)
    print("Two rebits: 9 product basis tests agree; global test gives 1 vs 0.")
    print("Single-system transpose: partial Bell expectation", negative)

if __name__ == "__main__":
    if not __debug__:
        raise SystemExit("Run without -O to execute exact checks.")
    verify()
