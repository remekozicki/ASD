# po usunięciu danego wirzchołka graf rozjebie sie na najwiecej składowych


def DFS(G):

    n = len(G)

    visited = [False for i in range(n)]
    parent = [None for i in range(n)]


    def DFSrec(G,visited,parent,u):

        visited[u] = True

        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                DFSrec(G, visited,parent,v)

    best_res = 0
    for u in range(n):
        counter = 0
        if not visited[u]:
            DFSrec(G,visited,parent,u)
            for i in parent:
                if i == u:
                    counter += 1
        best_res = max(best_res, counter)
        

