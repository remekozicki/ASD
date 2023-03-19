from math import sqrt
from math import ceil


def create_graph(A):
    n = len(A)
    G = []

    for u in range(n):
        for v in range(u+1,n):
            
            x = ( A[u][0] - A[v][0] )**2
            y = ( A[u][1] - A[v][1] )**2
            val = sqrt(x+y)
            val = ceil(val) 

            G.append([u,v,val])
    G.sort(key = lambda x: x[2])
    return G




A =[(100, 100), (100, 200), (200, 100), (200, 200)]

print(create_graph(A))