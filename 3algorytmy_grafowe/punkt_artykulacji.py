# po usunięciu danego wirzchołka graf rozjebie sie na najwiecej składowych


def DFS(G,idx):

    n = len(G)

    visited = [False for i in range(n)]
    parent = [None for i in range(n)]

    visited[idx] = True

    if idx != 0:
        DFSrec(G,visited,parent,0,idx)
    else:
        DFSrec(G,visited,parent,1,idx)

    return visited

def DFSrec(G,visited,parent,u,idx):

    visited[u] = True

    for v in G[u]:
        if not visited[v]:
            parent[v] = u
            DFSrec(G, visited,parent,v,idx)

def check_visited(v):
    for i in v:
        if i == False:
            return False
        
    return True

def find_pa(T):
    n = len(T)
    count = 0
    for i in range(n):
        v = DFS(T,i)
        if not check_visited(v):
            count +=1
    
    return count

B = [[1,2,3,5] ,
    [0,4,5],
    [0,3],
    [0,2,6,7],
    [1,5],
    [1,4,0],
    [3,7],
    [3,6]]
print(find_pa(B))


