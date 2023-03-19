#Dixtra

from queue import PriorityQueue



def Dixtra(G,start):
    n = len(G)

    Q = PriorityQueue()
    visited = [False for i in range(n)]
    parent = [None for i in range(n)]
    distance = [float('inf') for i in range(n)]
    
   
    Q.put([0,start])
    
    distance[start] = 0

    while not Q.empty():
        
        ver_u = Q.get()
        d_u,u = ver_u
        
        if not visited[u]:
            visited[u] = True
            
            for ver_v in G[u]:
                v,d_v = ver_v
                if not visited[v]:
                    if (distance[v] > distance[u] + d_v):
                        distance[v] = distance[u] + d_v
                        parent[v] = u
                        Q.put([distance[v],v])
                    
           
                    
                
        
    return distance,parent



def dixtra_rev(G,start):

    Q = PriorityQueue()

    visited  = [False for i in range(len(G))]
    distance  = [float('inf') for i in range(len(G))]
    parents  = [None for i in range(len(G))]

    distance[start] = 0

    Q.put([0,start])

    while not Q.empty():
        dis_u , u = Q.get()

        if  not visited[u]:
            visited[u] = True

            for v, dis_v in G[u]:
                if not visited[v]:
                    if distance[v] > distance[u] + dis_v:
                        distance[v] = distance[u] + dis_v
                        parents[v] = u
                        Q.put([distance[v],v])
    return distance,parents



# 0 - ver, 1 - distance
# graph = [ [(1,1),(7,2)], [(0,1),(2,2),(4,3)], [(1,2),(3,5)], [(2,5),(6,1)], [(1,3),(5,3),(7,1)], [(4,3),(6,8),(8,1)], [(3,1),(5,8),(8,4)],
#          [(0,2),(4,1),(8,7)],[(5,1),(6,4),(7,7)]]

graph = [
    [(1, 1)],
    [(0, 1), (2, 2), (3, 3)],
    [(1, 2), (3, 1), (4, 5)],
    [(1, 3), (2, 1), (4, 1)],
    [(2, 5), (3, 1)]
]

D,P = (Dixtra(graph,1))
print(D)
print(P)
D1,P1 = (dixtra_rev(graph,1))
print(D1)
print(P1)