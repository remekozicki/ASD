

def create_graph(tab,a,b):
    G = [[0 for j in range(b-a+1)] for i in range(b-a+1)]

    for v in tab:
        if v[0] >= a and v[1] <= b:
            G[v[0]-a][v[1]-a] = 1
    return G


def check_range(tab,a,b):
    G = create_graph(tab,a,b)
    visited = [False for i in range(b-a+1)]
    DFS(G,visited,a,len(G))

    return visited[b-a]

def DFS(G,visited,a,n):

    visited[a] = True
    for i in range(n):
        if not visited[i] and G[a][i] == 1:
            DFS(G,visited,i,n)

tab = [[0, 2], [1, 3], [2, 4], [0, 3], [3, 5], [5, 6], [3, 4]]

print(check_range(tab,1,4))
