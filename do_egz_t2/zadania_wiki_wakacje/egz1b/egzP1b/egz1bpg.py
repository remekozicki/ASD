
from queue import PriorityQueue



def get_len(G):
    ver = -1
    for i in G:
        ver = max(ver,i[0],i[1])
    return ver + 1 

def change_graph(G):
    n = get_len(G)
    N_G = [[] for _ in range(n)]

    for i in G:
        N_G[i[0]].append([i[1],i[2]])
        N_G[i[1]].append([i[0],i[2]])

    
    return N_G

def dixtra_3(G,D,L):

    nG = change_graph(G)
    n = len(nG)

    visited = [[False for _ in range(5)] for _ in range(n)]
    distance = [[float('inf') for _ in range(5)] for _ in range(n)]
    for i in range(5):
        distance[D][i] = 0

    # visited = [False for _ in range(n)]

    Q = PriorityQueue()

    Q.put([0,D,0])
    
    while not Q.empty():

        dis_u, u, count = Q.get()

        if u == L and count == 4:
            return distance[u][count]
        
        if not visited[u][count]:
            visited[u][count] = True
            

            for v, dis_v in nG[u]:
                if count + 1 <= 4:
                    if distance[v][count+1] > distance[u][count] + dis_v:
                        distance[v][count+1] = distance[u][count] + dis_v
                        Q.put([distance[v][count+1],v,count+1])
    
    return None


G = [
    (0, 1, 9), (0, 2, 1),
    (1, 2, 2), (1, 3, 8),
    (1, 4, 3), (2, 4, 7),
    (2, 5, 1), (3, 4, 7),
    (4, 5, 6), (3, 6, 8),
    (4, 6, 1), (5, 6, 1)
]

D = 0
L = 6
print(dixtra_3(G,D,L))

