



from collections import deque


def floyd_warshall(T):
    n = len(T)

    D = [[float('inf') for _ in range(n)] for _ in range(n)]

    for i in range(n):
        D[i][i] = 0
    
    for i in range(n):
        for j in range(n):
            if T[i][j] != 0:
                D[i][j] = T[i][j]
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                D[i][j] = min(D[i][j], D[i][k]+D[k][j])
    
    return D


def big_graph(T,D,C):

    FW = floyd_warshall(T)

    n = len(FW)

    G = [[0 for _ in range(n+2)]for _ in range(n+2)]

    pairs = []
    for i in range(n):
        for j in range(n):
            if FW[i][j] >= D and C[i] == 'B' and C[j] == 'G':
                G[0][i+1] = 1
                G[i+1][j+1] = 1
                G[j+1][n+1] = 1

    
    return G
    
    

def BFS(G,s,t,parent):

    n = len(G)
    visited = [False for i in range(n)]
    # parent = [None for i in range(n)]
    dis = [0 for i in range(n)]

    Queue = deque()

    Queue.append(s)
    visited[s] = True

    while len(Queue) > 0:

        u = Queue.popleft()

        for v in range(n):
            if (not visited[v]) and G[u][v] != 0:
                visited[v] = True
                parent[v] = u
                dis[v] = dis[u] + 1
                Queue.append(v)
                if v == t:
                    return True
    
  
    return False

def Fulkerson(G,start,end):
    n = len(G)
    parent= [None for i in range(n)]
    

    G_cp = [[G[i][j] for j in range(n)] for i in range(n)]


    max_flow = 0

    while BFS(G_cp,start,end,parent):

        path_flow = float('inf')
        s = end
        while s != start:
            path_flow = min( path_flow, G_cp[parent[s]][s] )
            s = parent[s]
        
        max_flow += path_flow

        v = end

        while v != start:
            u = parent[v]
            G_cp[u][v] -= path_flow
            G_cp[v][u] += path_flow
            v = u
      
    return max_flow


T = [
    [0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 0, 1],
    [1, 0, 1, 1, 0],
]
C = ['B', 'B', 'G', 'G', 'B']
D = 2
G = big_graph(T,D,C)
n = len(G)
print(Fulkerson(G,0,n-1))