# spojne skladowe

def DFS(G):
    n = len(G)

    visited = [None for i in range(n)]
   
    time_arr = [None for i in range(n)]

    time_v = 0

   


    def DFSrec (G, visited, v, time_arr):
        nonlocal time_v
        visited[v] = True

        for u in G[v]:
            if not visited[u]:
                
                DFSrec(G,visited, u, time_arr)
            
            #time_v += 1
        time_v += 1
        time_arr[v] = time_v
        
    
    for v in range(n):
        if not visited[v]:
            DFSrec(G,visited, v, time_arr)
    
    return time_arr


def new_graph(G):
    n = len(G)
    new_G = [[] for i in range(n)]

    for v in range(n):

        for u in G[v]:

            new_G[u].append(v)
    
    return new_G

def DFS_2(new_G, time_arr):

    n = len(new_G)

    visited = [False for i in range(n)]
    
    def DFSrec2(new_G,u,visited):

        visited[u] = True
        

        for v in new_G[u]:
            if not visited[v]:
                visited[v] = True
                DFSrec2(new_G,v,visited)
        
    counter = 0

    time_arr_mod = [[0,0] for i in range(n)]

    
    for i in range(n):
        time_arr_mod[i][0], time_arr_mod[i][1] = i, time_arr[i]
    
    time_arr_mod.sort(key = lambda x: x[1], reverse = True )
    print(time_arr_mod)
    
    for i in range(n):
        if not visited[time_arr_mod[i][0]]:
            u = time_arr_mod[i][0]

            DFSrec2(new_G,u,visited)
            counter += 1
            
    return counter
#------------------------------------------------------------------------
# zakładam ze graf jest spójny, wrazie czego mozna walnac dfs i sprawdzić czy visited jest OK
def trans_G(G):
    n = len(G)
    T = [[]for _ in range(n)]
    for u in range(n):
        for v in G[u]:
            T[v].append(u)
    return T

def DFS1(G):
    n = len(G)
    
    visited = [False for _ in range(n)]
    t_arr = [None for _ in range(n)]
    t_v = 0

    def DFS1rec(G, visited, t_arr, u):
        nonlocal t_v
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                # visited[v] = True
                DFS1rec(G,visited,t_arr,v)

        t_v += 1
        t_arr[u] = t_v

    for u in range(n):
        if not visited[u]:
            DFS1rec(G,visited,t_arr,u)
    return t_arr

def DFS2(G,t_all):
    n = len(G)

    visited = [False for _ in range(n)]

    def DFS2rec(G,visited,u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                # visited[v] = True
                DFS2rec(G,visited,v)
    
    count = 0
    for i in range(n):
        if not visited[t_all[i][0]]:
            u = t_all[i][0]
            DFS2rec(G,visited,u)
            count += 1
    return count
    
def spojne_skladow(G):
    # graf transponowany (odwracamy graf tak trzeba taki algorytm)
    n = len(G)
    T = trans_G(G)
    print(T)
    t_arr = DFS1(G)
    print(t_arr)
    t_all = [[None,None] for _ in range(n)]
    for i in range(n):
        t_all[i][0], t_all[i][1] = i, t_arr[i]

    t_all.sort(key = lambda x: x[1], reverse = True)
    print(t_all)

    res = DFS2(T,t_all)
    return res

graph = [[1, 4], [2], [0], [4, 6], [5], [3], [5], [8], [9], [5, 10], [7]]

new_G = (new_graph(graph))
print(new_G)
time_arr = (DFS(graph))
print(time_arr)
print(DFS_2(new_G,time_arr))
print(spojne_skladow(graph))