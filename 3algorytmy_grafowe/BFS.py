#BFS

from collections import deque
from queue import Queue


def BFS( G , s, T):
    n = len(G)
    Q = deque()
    t = T
    Visited = [False for i in range(n)]

    Visited[s] = True

    Parents = [None for i in range(n)]

    Distance = [0 for i in range(n)]

    # szukanie najkrótszej ścieżki
    
    Q.append(s)
    
    while len(Q) > 0:

        u = Q.popleft()
        for v in G[u]:
            if not Visited[v]:
                Visited[v] = True
                Distance[v] = Distance[u] + 1
                Parents[v] = u
                Q.append(v)
        if Distance[t] != 0:
            break
    
    # Odtwarzanie najkrótszej ścieżki
    
    D = Distance[t]
    d = Distance[t]
    Path = [t]
    while d > 0:
        Path.append(Parents[t])
        t = Parents[t]
        d -= 1
    
    return Path

def BFS2(G,s,t):

    n = len(G)
    visited = [False for i in range(n)]
    distance = [0 for i in range(n)]
    parents = [None for i in range(n)]
    # distance[s] = 0

    Q = Queue()
    Q.put(s)

    while not Q.empty():
        u = Q.get()
        visited[u] = True

        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                distance[v] = distance[u] + 1
                parents[v] = u
                Q.put(v)
        
        if distance[t] != 0:
            break
    
    dis = distance[t]
    Path = []
    while dis >= 0:
        Path.append(t)
        t = parents[t]
        dis -=1
    return Path




G = [[1,2],[0,3],[0,4],[1,5,6],[2,7],[3,8],[3,8],[4,8],[5,6,7,9],[8,10,11],[9,12],[9,12],[10,11]] 
s = 0
t = 10
print(BFS(G,s,t))

print(BFS2(G,s,t))