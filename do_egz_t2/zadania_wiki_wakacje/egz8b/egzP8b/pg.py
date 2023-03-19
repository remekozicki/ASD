



def warshall(G):

    n = len(G)

    dis = [[float('inf') for i in range(n)]for j in range(n)]

    for i in range(n):
        dis[i][i] = 0

    for u in range(n):
        for v, w in G[u]:
            dis[u][v] = w

    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if dis[i][j] > dis[i][k] + dis[k][j]:
                    dis[i][j] = dis[i][k] + dis[k][j]
    
    return dis

def read(G,P):

    dis = warshall(G)
    res = 0
    for i in range(1,len(P)):
        res += dis[P[i-1]][P[i]]
    
    return res


            


G = [
        [(1, 3), (2, 3)],
        [(0, 3), (4, 4)],
        [(0, 3), (3, 1), (4, 4)],
        [(2, 1), (4, 2)],
        [(1, 4), (2, 4), (3, 2)]
      ]
P = [0, 3, 4]

print(read(G,P))