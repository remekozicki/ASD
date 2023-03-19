


from queue import PriorityQueue


def divide(C):
    n = len(C)
    graph = [[]for _ in range(n)]

    for i in range(n):
        chest = C[i][0]
        for j in range(1,4):
            if C[i][j][1] != -1:
                gold = C[i][j][0]
                diff = chest - gold
                if diff > 10:
                    diff = 10
                graph[i].append([diff,C[i][j][1]])
    
    return graph

def Dixtra(C):
    n = len(C)
    G = divide(C)
    Q = PriorityQueue()
    visited = [False for i in range(n)]
    gold = [-float('inf') for i in range(n)]
    
   
    Q.put([0,0])
    
    gold[0] = 0

    while not Q.empty():
        
        u,_ = Q.get()
        
        
        if not visited[u]:
            visited[u] = True
            
            for diff,v in G[u]:
                
                if not visited[v]:
                    if (gold[v] < gold[u] + diff) and (gold[u] + diff >= 0):
                        gold[v] = gold[u] + diff
                        
                        Q.put([v,gold[v]])
    
    if gold[n-1] >= 0:
        return gold[n-1]
    else:
        return -1

    

C = [[8, [6, 3], [4, 2], [7, 1]],  # 0
     [22, [12, 2], [21, 3], [0, -1]],  # 1
     [9, [11, 3], [0, -1], [7, -1]],  # 2
     [15, [0, -1], [1, -1], [0, -1]]]  # 3
    
C = [[2, [5, 1], [1, 6], [1, 8]], 
[2, [7, 2], [1, 4], [1, 2]], 
[89, [91, 3], [75, 8], [84, 6]], 
[8, [6, 4], [10, 6], [7, 5]], 
[4, [5, 5], [1, 7], [3, 5]], 
[10, [11, 6], [0, 6], [4, 6]], 
[1, [0, 7], [0, 7], [6, 7]], 
[57, [51, 8], [45, 8], [50, 8]], 
[2, [6, 9], [7, 9], [0, 9]], 
[6, [3, -1], [8, -1], [1, -1]]]

print(Dixtra(C))