from zad3testy import runtests





from queue import PriorityQueue



def Dixtra(G,s):

    n = len(G)

    visited = [False for i in range(n)]
    taken = [False for i in range(n)]
    distance = [float('inf') for i in range(n)]
    parent = [None for i in range(n)]

    Q = PriorityQueue()
    start = [0,s]
    Q.put(start)
    distance[s] = 0

    while not Q.empty():

        w_u , u = Q.get()
        visited[u] = True

        for v, w_v in G[u]:

            if not visited[v]:

                if distance[v] > distance[u] + w_v:
                    distance[v] = distance[u] + w_v
                    parent[v] = u
                
                if not taken[v]:
                    taken[v] = True
                    Q.put([distance[v],v]) 
    
    return distance

def find_paths(G,s,t):
    n = len(G)
    distance_s = Dixtra(G,s)
    distance_t = Dixtra(G,t)
    std = distance_s[t]
    if std == float('inf'):
        return 0
    counter = 0
    res_tab = []

    for u in range(n):
        for v,w in G[u]:
            if distance_s[u] + distance_t[v] + w == std:
                counter+=1
                res_tab.append([u,v])
    
    return counter


def paths(G,s,t):
    """tu prosze wpisac wlasna implementacje"""
    return find_paths(G,s,t)

    
runtests( paths )


