


from queue import PriorityQueue


def Dixtra(G,s,t):
    n = len(G)
    Q = PriorityQueue()
    visited = [[False for i in range(2)]for j in range(n)]
    distance = [[float('inf') for i in range(2)]for j in range(n)]
    distance[s][0] = 0
    distance[s][1] = 0
    Q.put([0,s,0]) # 0 - można, 1 - nie można
    
    while not Q.empty():

        dis, u, jump = Q.get()

        if u == t:
            return dis
            
        if not visited[u][jump]:
            visited[u][jump] = True 
        
            for v in range(n):
                
                if G[u][v] != 0:
                    val_1 = G[u][v]


                    if distance[v][0] > distance[u][jump] + val_1:
                        distance[v][0] = distance[u][jump] + val_1
                        Q.put([distance[v][0],v,0])
                    
                    if jump == 0: # moge skoczyć 
                        
                        for w in range(n):
                    
                            if G[v][w] != 0:
                                val_2 = G[v][w]                                
                                
                                if distance[w][1] > distance[u][jump] + max(val_1,val_2):
                                    distance[w][1] = distance[u][jump] + max(val_1,val_2)
                                    Q.put([distance[w][1],w,1])
    
    return None


graph = [[0, 1, 0, 0, 0],
         [1, 0, 1, 0, 0],
         [0, 1, 0, 7, 0],
         [0, 0, 7, 0, 8],
         [0, 0, 0, 8, 0]]

s = 0
t = 4

print(Dixtra(graph,s,t))