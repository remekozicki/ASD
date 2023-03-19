

from queue import PriorityQueue


def Dixtra(G,start):
    n = len(G)
    
    visited = [False for i in range(n)]
    distance = [float('inf') for i in range(n)]
    parent = [None for i in range(n)]

    Q = PriorityQueue()

    distance[start] = 0
    Q.put([0,start])

    while not Q.empty():

        ver_u = Q.get()
        d_u, u = ver_u

        visited[u] = True

        for ver_v in G[u]:
            v, d_v = ver_v

            if distance[v] > distance[u] + d_v:
                distance[v] = distance[u] + d_v
                parent[v] = u
            
            if not visited[v]:
                Q.put([distance[v],v])
        
    return distance, parent


graph = [
    [(1, 1)],
    [(0, 1), (2, 2), (3, 3)],
    [(1, 2), (3, 1), (4, 5)],
    [(1, 3), (2, 1), (4, 1)],
    [(2, 5), (3, 1)]
]

D,P = (Dixtra(graph,1))
print(D)
print(P)