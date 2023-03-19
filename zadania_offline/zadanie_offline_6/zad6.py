
from collections import deque
from zad6testy import runtests

def path(Parents,T,D): 
    Path = [T]
    while D > 0:
        Path.append(Parents[T])
        T = Parents[T]
        D -= 1
    return Path

def BFS( G , s, T):
    
    # BFS z wykładu zrobiony na kolejce
    n = len(G)
    Q = deque()
    # t = T
    
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
        if Distance[T] != 0:
            break
    # Odtwarzanie najkrótszej ścieżki
    D = Distance[T]
    
    Path = path(Parents,T,D)

    # zmodyfikowny BFS który usuwa poszczególne krawędzie z Path i sprawdza czy scieżka się wydłużyła    
    for j in range(1,len(Path)):
        
        i = j-1
        
        Q = deque()
        
        Q.append(s)
       
        Visited = [False for i in range(n)]
        Visited[s] = True
        Distance = [0 for i in range(n)]
       
        while len(Q)>0:

            u = Q.popleft()
            
            for v in G[u]:
                
                if not Visited[v]:
                    
                    if (u == Path[i] and v == Path[j]) or (u == Path[j] and v == Path[i]):
                        continue
         
                    Visited[v] = True
                    Distance[v] = Distance[u] + 1
                    Q.append(v)
            
            if Distance[T] != 0:
                break
        
    # Distance[T] == 0 --> graf po usunięciu krawędzi stał się niespójny 
        if D < Distance[T] or Distance[T] == 0:
            return [Path[j],Path[i]]
    
    return None


def longer( G, s, t ):
    
    return BFS(G,s,t)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )
