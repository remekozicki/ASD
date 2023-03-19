
from collections import deque


def get_ver(G):
    best_ver = -1

    for i in G:
        best_ver = max(best_ver, i[0], i[1])

    return best_ver

def to_matrix(G):
    n = get_ver(G)+1
    G_matirx = [[0 for i in range(n)] for j in range(n)]

    for v in G:
        i,j,w = v
        G_matirx[i][j] = w
    
    return G_matirx

def BFS(G,s,t,parent):
    n = len(G)
    

    visited = [False for i in range(n)]
    # parent = [None for i in range(n)]

    Q = deque()
    visited[s] = True
    Q.append(s)

    while len(Q) > 0:

        u = Q.popleft()

        for v in range(n):
            if (not visited[v]) and G[u][v] != 0:
                visited[v] = True
                parent[v] = u
                Q.append(v)
                if v == t:
                    return True
    
    return False


def Ford_Fulkerson(G,start,end):
    n = len(G)
    parent= [None for i in range(n)]


    max_flow = 0

    while BFS(G,start,end,parent):

        path_flow = float('inf')
        s = end
        while s != start:
            path_flow = min( path_flow, G[parent[s]][s] )
            s = parent[s]
        
        max_flow += path_flow

        v = end

        while v != start:
            u = parent[v]
            G[u][v] -= path_flow
            G[v][u] += path_flow
            v = u
    return max_flow


def All_together(G,s):
    n = get_ver(G)+1
    G_m = to_matrix(G)
    best_res = -1
    for t1 in range(n):
        for t2 in range(n):
            G_cp = [[G_m[i][j] for j in range(n)] for i in range(n)]
            if t1 != s and t2 != s and t1 != t2:
                bf1= Ford_Fulkerson(G_cp,s,t1)
                bf2 = Ford_Fulkerson(G_cp,s,t2)
                best_res = max(best_res, bf1+bf2 )
    
    return best_res





G = [(0,1,7),(0,3,3),(1,3,4),(1,4,6),(2,0,9),(2,3,7),(2,5,9),
(3,4,9),(3,6,2),(5,3,3),(5,6,4),(6,4,8)]

s=2

print(All_together(G,s))