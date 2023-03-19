

from collections import deque

def delete_useless(G,T):
    n = len(G)

    while True:
        wyjebane = 0
        for i in range(n):
            if len(G[i]) == 1 and i not in T:
                to_del = G[i][0]
                G[i].remove(to_del)
                G[to_del].remove(i)
                wyjebane+=1
        
        if wyjebane == 0:
            return G

def BFS(G,s):
    n = len(G)

    visited = [False for i in range(n)]
    distance = [0 for i in range(n)]
    parents = [None for i in range(n)]

    Q = deque()
    Q.append(s)
    visited[s] = True
    while len(Q) > 0:
        u = Q.popleft()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                distance[v] = distance[u] + 1
                parents[v] = u
                Q.append(v)
    max_val = 0
    for i in range(n):
        if max_val < distance[i]:
            max_val = distance[i]
            max_ind = i
    
    return max_ind , distance, parents


def package(G,T):
    G = delete_useless(G,T)
    i = 0
    while len(G[i]) == 0:
        i+=1
    
    s, _, _ = BFS(G,i)

    start , distance, parents = BFS(G,s)

    main_path = []
    while start != None:
        main_path.append(start)
        start = parents[start]
    leaves = []
    
    for i in range(len(G)):
        if len(G[i]) > 0 and i not in main_path:
            leaves.append(i)
    
    

    lenght = len(main_path)-1 + len(leaves)*2


    

    return lenght
    


graph = [
    [1],
    [0,2],
    [1,3,4,6],
    [2],
    [2,5],
    [4],
    [2,7,8,10],
    [6],
    [6,9],
    [8],
    [6,11],
    [10]
    ]

miasta = [0,4,6,7,11]

print(package(graph,miasta))



