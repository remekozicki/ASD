
def create_graph(T):
    n = len(T)
    G = [[]for i in range(n)]
    for a in range(n):
        for b in range(n):
            if T[a][b] == 1:
                G[a].append(b)
            if T[a][b] == 2:
                G[b].append(a)
    
    return G

def DFS(T):
    n = len(T)
    G = create_graph(T)

    visited = [False for i in range(n)]
    sort_task = []

    for u in range(n):
        if not visited[u]:
            DFSrec(G,u,visited, sort_task,n)
    
    sort_task.reverse()
    return sort_task


def DFSrec(G,u,visited,sort_task,n):
    visited[u] = True

    for v in G[u]:
        if not visited[v]:
            DFSrec(G,v,visited,sort_task,n)
    
    sort_task.append(u)

T = [[0, 2, 1, 1], [1, 0, 1, 1], [2, 2, 0, 1], [2, 2, 2, 0]]


print(DFS(T))