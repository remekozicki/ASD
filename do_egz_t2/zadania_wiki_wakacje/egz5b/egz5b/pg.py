

def create_G(B):
    tab = []
    b = len(B)
    n = -1
    for i in range(b):
        B[i] = ([min(B[i][0],B[i][1]),max(B[i][0],B[i][1])])
        n = max(n,B[i][0],B[i][1])
    
    B.sort(key = lambda x: x[1])
    B.sort(key = lambda x: x[0])
    
    n+=1
    G = [[]for i in range(n)]

    G[B[0][0]].append(B[0][1])
    G[B[0][1]].append(B[0][0])

    for i in range(1,b):
        if B[i-1] != B[i]:
            G[B[i][0]].append(B[i][1])
            G[B[i][1]].append(B[i][0])


    return G

def DFS(G,idx):
    
    n = len(G)

    visited = [False for i in range(n)]
    # parents = [[None] for i in range(n)]

    visited[idx] = True
    if idx != 0:
        rec_DFS(G,visited,0)
    else:
        rec_DFS(G,visited,1)
    
    for i in range(n):
        if not visited[i]:
            return False
    
    return True


def rec_DFS(G,visited,u):
    visited[u] = True
    for v in G[u]:
        if not visited[v]:
            rec_DFS(G,visited,v)



    
def zip_f(B):
    G = create_G(B)
    n = len(G)

    count = 0
    for i in range(n):
        if not DFS(G,i):
            count+=1
    
    return count




B = [(3, 1), (0, 1), (4, 2), (1, 2), (0, 1), (2, 4), (2, 4), (0, 3), (2, 4), (1, 0), (2, 1)]
print(zip_f(B))