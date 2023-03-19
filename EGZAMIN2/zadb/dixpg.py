
def divide(C):
    n = len(C)
    graph = [[]for _ in range(n)]

    for i in range(n):
        chest = C[i][0]
        for j in range(1,4):
            # if C[i][j][1] != -1:
            gold = C[i][j][0]
            diff = chest - gold
            if diff > 10:
                
                graph[i].append([diff,C[i][j][1]])
    
    return graph

def dynamic(C):
    G = divide(C)
    n = len(C)
    DP = [-1 for _ in range(n)]
    

    res = rec(DP,G,n,0)
    return res

def rec(DP,G,n,idx):

    if idx == n-1:
        return 0
    
    if DP[idx] != -1:
        return DP[idx]

    for i in range(3):
        if G[idx][i][1] != -1:
            DP[idx] = max(DP[idx],rec(DP,G,n,G[idx][i][1]) + G[idx][i][0])
        
    return DP[idx]

C = [[8, [6, 3], [4, 2], [7, 1]],  # 0
     [22, [12, 2], [21, 3], [0, -1]],  # 1
     [9, [11, 3], [0, -1], [7, -1]],  # 2
     [15, [0, -1], [1, -1], [0, -1]]]  # 3


# C = [[2, [5, 1], [1, 6], [1, 8]], 
# [2, [7, 2], [1, 4], [1, 2]], 
# [89, [91, 3], [75, 8], [84, 6]], 
# [8, [6, 4], [10, 6], [7, 5]], 
# [4, [5, 5], [1, 7], [3, 5]], 
# [10, [11, 6], [0, 6], [4, 6]], 
# [1, [0, 7], [0, 7], [6, 7]], 
# [57, [51, 8], [45, 8], [50, 8]], 
# [2, [6, 9], [7, 9], [0, 9]], 
# [6, [3, -1], [8, -1], [1, -1]]]
# wynik 11
print(dynamic(C))
