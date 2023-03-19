
from queue import PriorityQueue

def sum_luft(G):
    n = len(G)
    new_G = [[] for i in range(n)]
    tab = []
    sum = 0
    for v in range(n):
        for u,dis in G[v]:
            if v < u:
                new_G[v].append([u,dis])
                tab.append([v,u,dis])
            sum += dis
    
    sum //= 2
    return sum,new_G,tab




def Prima2(G,s):
    n = len(G)
    sum, nG, tab= sum_luft(G)
    luft = 0

    visited = [False for i in range(n)]
    distance = [-1 for i in range(n)]
    distance[s] = 0
    parents = [None for i in range(n)]
    MST = []
    Q = PriorityQueue()
    # waga(dis), wierzchołek
    Q.put([0,0])
    to_add = 0

    while not Q.empty():
        dis_u, u = Q.get()
        visited[u] = True

        for v,dis_v in G[u]:
           
            if not visited[v]:
                if distance[v] <= dis_v:
                    # if distance[v] != -1:
                    #     to_add = max(to_add,distance[v])
                    distance[v] = dis_v
                    parents[v] = u
                    Q.put([dis_v*(-1),v])
    

    for i in range(1,n):
        MST.append([parents[i],i,distance[i]])
        luft += distance[i]
    tab.sort(key = lambda x: x[2],reverse=True)
    MST.sort(key = lambda x: x[2],reverse=True)


    i = 0
    m = len(MST)
    while i < m:
        if tab[i][2] == MST[i][2]:
            i+=1
        else:
            break
    to_add = tab[i][2]   

    luft += to_add
    res = sum - luft
    
    return res

# G = [
#       [(1, 15), (2, 5),  (3, 10)],
#       [(0, 15), (2, 8),  (4, 5),  (5, 12)],
#       [(0, 5),  (1, 8),  (3, 5),  (4, 6)],
#       [(0, 10), (2, 5),  (4, 2),  (5, 11)],
#       [(1, 5),  (2, 6),  (3, 2),  (5, 2)],
#       [(1, 12), (4, 2),  (3, 11)]]


G = [
      [(3, 12), (2, 8)],
      [(3, 4), (6, 5)],
      [(4, 9), (0, 8)],
      [(0, 12), (1, 4)],
      [(5, 8), (2, 9)],
      [(6, 2), (4, 8)],
      [(1, 5), (5, 2)]]
    
print(Prima2(G,0))