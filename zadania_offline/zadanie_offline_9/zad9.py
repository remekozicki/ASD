from zad9testy import runtests

from collections import deque

def get_ver(G):
    best_ver = -1

    for i in G:
        best_ver = max(best_ver, i[0], i[1])

    return best_ver

def BFS(G,s,t,parent):
    n = len(G)
    
    visited = [False for i in range(n)]
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

# standardowy fulkerson
def Ford_Fulkerson(G,start,end):
    n = len(G)
    parent= [None for i in range(n)]


    max_f = 0

    while BFS(G,start,end,parent):

        curr_f = float('inf')
        v = end
        while v != start:
            curr_f = min( curr_f, G[parent[v]][v] )
            v = parent[v]
        
        max_f += curr_f

        v = end

        while v != start:
            u = parent[v]
            G[u][v] -= curr_f
            G[v][u] += curr_f
            v = u
    return max_f


def All_together(G,s):
    n = get_ver(G)+1
  
    best_res = -1
    for t1 in range(n):
        for t2 in range(t1+1,n):
            if t1 != s and t2 != s and t1 != t2:
                G_cp = [[0 for j in range(n+1)] for i in range(n+1)]

                for v in G:
                    i,j,w = v
                    G_cp[i][j] = w
                # pomysł ze stworzeniem sztucznego wierzchołka z wykładu 
                G_cp[t1][n] = float('inf')
                G_cp[t2][n] = float('inf')

                FF = Ford_Fulkerson(G_cp,s,n)
                if best_res < FF:
                    best_res = FF
    
    return best_res


def maxflow( G,s ):
    # tu prosze wpisac wlasna implementacje
    return All_together(G,s)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxflow, all_tests = True )