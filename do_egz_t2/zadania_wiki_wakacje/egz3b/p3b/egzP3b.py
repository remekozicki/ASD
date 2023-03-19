from egzP3btesty import runtests 
from queue import PriorityQueue


# def sum_luft(G):
#     n = len(G)

#     sum = 0
#     for v in range(n):
#         for u,dis in G[v]:
#             sum += dis
    
#     sum //= 2
#     return sum

# def Prima2(G,s):
#     n = len(G)
#     sum = sum_luft(G)
#     luft = 0

#     visited = [False for i in range(n)]
#     distance = [-1 for i in range(n)]
#     distance[s] = 0
#     parents = [None for i in range(n)]
#     MST = []
#     Q = PriorityQueue()
#     # waga(dis), wierzchołek
#     Q.put([0,0])
#     to_add = 0

#     while not Q.empty():
#         dis_u, u = Q.get()
#         visited[u] = True

#         for v,dis_v in G[u]:
           
#             if not visited[v]:
#                 if distance[v] <= dis_v:
#                     if distance[v] != -1:
#                         to_add = max(to_add,distance[v])
#                     distance[v] = dis_v
#                     parents[v] = u
#                     Q.put([dis_v*(-1),v])
    
#     for i in range(n):
#         luft += distance[i]
    
#     luft += to_add
#     res = sum - luft
    
#     return res

def sum_luft(G):
    n = len(G)
    new_G = [[] for i in range(n)]
    tab = []
    sum = 0
    for v in range(n):
        for u,dis in G[v]:
            if v < u:
                tab.append([v,u,dis])
            sum += dis
    
    sum //= 2
    return sum,tab




def Prima2(G,s):
    n = len(G)
    sum,tab = sum_luft(G)
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

def lufthansa ( G ):
    #tutaj proszę wpisać własną implementację 
    return Prima2(G,0) 

runtests ( lufthansa, all_tests=True)