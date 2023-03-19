from collections import deque


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
    bridge = [0,0]
    bridge_counter = 0
    while len(Q) > 0:

        u = Q.popleft()
        # jak najdziemy pojedyncze połączenie to zwracamy i git
        if len(Q) == 0:
            bridge[bridge_counter] = u
            bridge_counter += 1
        else:
            bridge_counter = 0
        
        if bridge_counter == 2:
            return bridge
        
        for v in G[u]:
            if not Visited[v]:
                Visited[v] = True
                Distance[v] = Distance[u] + 1
                Parents[v] = u
                Q.append(v)
        
    # Odtwarzanie najkrótszej ścieżki
    D = Distance[t]
    d = Distance[t]
    Path = [t]
    while d > 0:
        Path.append(Parents[t])
        t = Parents[t]
        d -= 1
    # HGW co tu sie bedzie dzialo próbuje odcinac poszczególne krawędzi i może zadziała
    Q2 = deque()
    
    Visited2 = [False for i in range(n)]

    Visited2[T] = True
    Q2.append(T)

    while len(Q2) > 0:

        u = Q2.popleft()
        to_compare = []
        
        for v in G[u]:
            if not Visited2[v]:
                Visited2[v] = True
                to_compare.append([Distance[v],v])
                Q2.append(v)
                
                
        min_val = min(to_compare)
        counter = 0
        
        for i in to_compare:
            if i[0] == min_val[0]:
                counter += 1
        
        if counter == 1:
            return [u, min_val[1]]
            
            
    
    return None


# G = [ [1,2],[0,3],[0,4],[1,5,6],[2,7],[3,8],[3,8],[4,8],[5,6,7,9],[8,10,11],[9,12],[9,12],[10,11]]
G = [[1, 2], [0, 2], [0, 1]]
print(BFS(G,0,2))


