from collections import deque


def BFS(G,s,t,parent):

    n = len(G)
    visited = [False for i in range(n)]
    # parent = [None for i in range(n)]
    dis = [0 for i in range(n)]

    Queue = deque()

    Queue.append(s)
    visited[s] = True

    while len(Queue) > 0:

        u = Queue.popleft()

        for v,dis in G[u]:
            if (not visited[v]):
                visited[v] = True
                parent[v] = u
                dis[v] = dis[u] + 1
                Queue.append(v)
                if v == t:
                    return True
    
  
    return False

def Fulkerson(G,start,end):
    n = len(G)
    parent= [None for i in range(n)]

    G_cp = [[G[i][1]] for i in range(n)]


    max_flow = 0

    while BFS(G_cp,start,end,parent):

        path_flow = float('inf')
        s = end
        while s != start:
            path_flow = min( path_flow, G_cp[parent[s]][s] )
            s = parent[s]
        
        max_flow += path_flow

        v = end

        while v != start:
            u = parent[v]
            G_cp[u][v] -= path_flow
            G_cp[v][u] += path_flow
            v = u
    
    for i in range(n):
        print(G_cp[i])   
    return max_flow


def get_rooms(T):
    n = len(T)
    best = -1
    for i in range(n):
        best = max(best, T[i][0],T[i][1],T[i][2])
    
    return best+1


def create_G(T):
    r = get_rooms(T)
    n = len(T)
    G = [[] for i in range(n + r + 2)] # dwa dodatkowe wieszchołki start i end 
    
    for k in range(r):
        G[n + r + 1].append([k+n,float('inf')])
    
    for i in range(n):
        for j in range(len(T[i])):
            if T[i][j] != None:
                G[i].append([T[i][j]+n,1])
        G[n + r].append([i,float('inf')])
        


T = [(2, 3, None), (0, 1, 3), (0, 2, None), (1, 3, 4), (2, 3, None)]



