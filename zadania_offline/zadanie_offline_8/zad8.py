from zad8testy import runtests

from math import ceil
from math import sqrt

class Node:

    def __init__(self,val):
        
        self.parent = self
        self.val = val
        self.rank = 0

def find(x):
    if x.parent != x:
        x.parent = find(x.parent)
    
    return x.parent

def union(x,y):
    x = find(x)
    y = find(y)

    if x == y:
        return
    
    if x.rank > y.rank:
        y.parent = x
    
    elif y.rank > x.rank:
        x.parent = y
    
    else:
        y.parent = x
        x.rank += 1

def Kruskal_MST(G,A):
    
    n = len(G)
    result = []

    vertices = len(A)-1

    Tab_node = []

    for i in range(vertices +1):
        Tab_node.append(Node(i))
    
    e = i = 0
    while e < vertices and i < len(G):

        u, v, w = G[i]
        x = find(Tab_node[u])
        y = find(Tab_node[v])

        if x != y:
            e += 1
            result.append(G[i])
            union(Tab_node[u],Tab_node[v])
        i+=1
        
    return result

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

def find_best_high(A):
    n_A = len(A)
   
    G = create_graph(A)

    result = Kruskal_MST(G,A)

    best_res = abs(result[-1][2]-result[0][2])

    G.pop(0)
    
    while len(G) >= n_A - 1:
        
        result = Kruskal_MST(G,A)
        if len(result) != n_A-1:
            break
        
        else:
            if best_res > abs(result[-1][2]-result[0][2]):
                best_res = abs(result[-1][2]-result[0][2])

        G.pop(0)

    return best_res

def highway( A ):
    # tu prosze wpisac wlasna implementacje
    return find_best_high(A)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( highway, all_tests = True )