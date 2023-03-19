from egzP8btesty import runtests

def warshall(G):

    n = len(G)

    dis = [[float('inf') for i in range(n)]for j in range(n)]

    for i in range(n):
        dis[i][i] = 0

    for u in range(n):
        for v, w in G[u]:
            dis[u][v] = w
            

    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i != j:
                    dis[i][j] = min(dis[i][j],dis[i][k] + dis[k][j])
    
    return dis

def read(G,P):

    dis = warshall(G)
    res = 0
    for i in range(1,len(P)):
        res += dis[P[i-1]][P[i]]
    
    return res

def robot( G, P ):
    #Tutaj proszę wpisać własną implementację
    return read(G,P)
    
runtests(robot, all_tests = True)
