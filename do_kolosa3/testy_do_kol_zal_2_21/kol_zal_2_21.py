




from queue import PriorityQueue



def Dixtra(G,s):

    n = len(G)

    visited = [False for i in range(n)]
    taken = [False for i in range(n)]
    distance = [float('inf') for i in range(n)]
    parent = [None for i in range(n)]

    Q = PriorityQueue()
    start = [0,s]
    Q.put(start)
    distance[s] = 0

    while not Q.empty():

        w_u , u = Q.get()
        visited[u] = True

        for v, w_v in G[u]:

            if not visited[v]:

                if distance[v] > distance[u] + w_v:
                    distance[v] = distance[u] + w_v
                    parent[v] = u
                
                if not taken[v]:
                    taken[v] = True
                    Q.put([distance[v],v]) 
    
    return distance

def find_paths(G,s,t):
    n = len(G)
    distance_s = Dixtra(G,s)
    distance_t = Dixtra(G,t)
    std = distance_s[t]

    counter = 0
    res_tab = []

    for u in range(n):
        for v,w in G[u]:
            if distance_s[u] + distance_t[v] + w == std:
                counter+=1
                res_tab.append([u,v])
    
    return res_tab, counter



# 0- wieszchołek, 1- waga 
G = [
    [ (1,2), (2,4)],
    [ (0,2),(3,11),(4,3)],
    [ (0,4),(3,13)],
    [ (1,11),(2,13),(5,17),(6,1)],
    [(1,3),(5,5)],
    [(3,17),(4,5),(7,7)],
    [(3,1),(7,3)],
    [(5,7),(6,3)]
    ]

s = 0
t = 7
# print(Dixtra(G,s))

tab, res = find_paths(G,s,t)

print(tab)
print('_______________________________')
print(res)