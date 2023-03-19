from zad7testy import runtests

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
        if path[-1] in G[0][1]:
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


def droga( G ):
    # tu prosze wpisac wlasna implementacje
    return hamilton_cycyle(G)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( droga, all_tests = True )