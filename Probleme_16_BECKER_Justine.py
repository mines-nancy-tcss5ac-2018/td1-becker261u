from math import*

def solve(n):
    x=(2**n)
    X=str(x)
    S=0
    for i in range(len(X)):
            S+=int(X[i])
    return S

assert solve(15)==26

print(solve(1000))