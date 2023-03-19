from zad2testy import runtests

def DFSrec(G,visited,parent,u,n):

    visited[u] = True

    for v in range(n):
        if not visited[v] and G[u][v] != 0:
            parent[v] = u
            DFSrec(G, visited,parent,v,n)


def DFS(G):

    n = len(G)

    visited = [False for i in range(n)]
    parent = [None for i in range(n)]

    best_res = -1
    for u in range(n):
        counter = 0
        visited = [False for i in range(n)]
        parent = [None for i in range(n)]
        DFSrec(G,visited,parent,u,n)
        
        for i in parent:
            if i == u:
                counter += 1
        
        if best_res < counter and counter > 1:
            best_res = counter
            res = u
    
    if best_res == -1:
        return None
    return res
        
def breaking(G):
    # tu prosze wpisac wlasna implementacje
    return DFS(G)


runtests( breaking )