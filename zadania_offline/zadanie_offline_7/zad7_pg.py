

from collections import deque


# def linear_form(G):
#     n = len(G)

#     G_l = [[] for i in range(n)]

#     for i in range(n):
#         #NORTH
#         for N in G[i][0]:
#             tmp = [N,'N']
#             G_l[i].append(tmp)
        
#         #SOUTH
#         for S in G[i][1]:
#             tmp  = [S,'S']
#             G_l[i].append(tmp)
#     return G_l

# def hamilton_cycyle(G_l):
#     n = len(G_l)
    
#     path = deque()
#     visited = [False for i in range(n)]
#     parents = [None for i in range(n)]
    
#     parents[0] = None
#     path.append(0)
   
#     for i in range(n):
#         u = i
#         if  not visited[u]:
#             ham_cyc_rec(G_l, u, visited, parents,path)
    
#     last = path[len(path)-1]

#     for i in (G_l[last]):
#         if i[0] == 0:
#             path.append(0)
#             return True, path
#     else:
#         return False, None

        

# def ham_cyc_rec(G_l,u,visited, parents,path):
#     if len(path) == len(G_l):
#         return True
#     visited[u] = True
#     for v in G_l[u]:

#         if not visited[v[0]]:
#             visited[v[0]] = True
#             parents[v[0]] = u
#             path.append(v[0])

#             if ham_cyc_rec(G_l,v[0],visited, parents,path):
#                 return True
            
#             else:
#                 visited[v[0]] = False
#                 parents[v[0]] = None
#                 path.pop()
    
#     return False


def hamilton_cycyle(G):
    n = len(G)
    
    path = []
    
    visited = [False for i in range(n)]
    # parents = [None for i in range(n)]
    
    # parents[0] = None
    path.append(0)
   
    u = 0
    visited[u] = True
    
    gate = 0 #północ - 0, południe - 1
    
    if ham_cyc_rec(G, u, visited,path,gate):
        if path[0] in G[path[len(G)-1]][gate]:
            # path.append(path[-1])
            return path
    else:
        return None
    
   

    
def ham_cyc_rec(G,u,visited,path, gate):
    
    if len(path) == len(G):
        return True
    
    
    for v in G[u][gate]:


        if not visited[v]:
            
            visited[v] = True
            # parents[v] = [u,gate]
            path.append(v)
            
            if u in G[v][0]:
                gate = 1
            
            elif u in G[v][1]:
                gate = 0

            if ham_cyc_rec(G,v,visited,path,gate):
                return True
            
            
            visited[v] = False
            # parents[v[0]] = None
            path.pop()

    return False



G = [ ([1],[3,4,6]),      
            ([2],[0]), 
            ([3],[1]),  
            ([0,4,6],[2]),
            ([5],[3,6,0]),
            ([6],[4]),
            ([0,3,4],[5]) ]

# G_lin = linear_form(G)
print(hamilton_cycyle(G))
