from collections import deque
from zad7ktesty import runtests 


def BFS(T, x0, y0):

    Q = deque()

    Q.append([1,y0])

    while Q:

        u = Q.popleft()

        if u[0] != x0 or u[1] != y0:
            T[x0][y0] += T[u[0]][u[1]]
            T[u[0]][u[1]] = 0

            if u[0] - 1 >= 0 and T[u[0]-1][u[1]] != 0:
                Q.append([u[0]-1,u[1]])

            if u[0] + 1 < len(T) and T[u[0]+1][u[1]] != 0:
                Q.append([u[0]+1,u[1]])
            
            if u[1] + 1 < len(T[0]) and T[u[0]][u[1]+1] != 0:
                Q.append([u[0],u[1]+1])
            
            if u[1] - 1 >= 0 and T[u[0]][u[1]-1] != 0:
                Q.append([u[0],u[1]-1])

def kanp_sack_memorize(cost,Z,l):
    n = len(cost)
    DP = [[None for i in range(l+1)]for j in range(len(cost)+1)]
    return knap_sack(cost,Z,l,DP,n)

def knap_sack(cost,Z,l,DP,n):

    if DP[n][l] != None:
        return DP[n][l]

    if n == 0 or l == 0:
        return 0
    
    if cost[n-1] <= l:
        DP[n][l] = max(   (Z[n-1] + knap_sack(cost,Z,l - cost[n-1], DP, n-1)), knap_sack(cost,Z,l,DP,n-1))
    
    else:
         DP[n][l] = knap_sack(cost,Z,l,DP,n-1)
    
    return DP[n][l]
# def knap_sack(cost,Z,l):
#     n = len(Z)

#     DP = [[0 for i in range(l+1)]for j in range(n)]

#     for b in range(cost[0],l+1):
#         DP[0][b] = Z[0]
    
#     for b in range(l+1):

#         for i in range(1,n):
#             DP[i][b] = DP[i-1][b]

#             if b - cost[i] >= 0:
#                 tmp = DP[i-1][b-cost[i]] + Z[i]
                
#                 if DP[i][b] < tmp:
#                     DP[i][b] = tmp
    
#     return DP[n-1][l]





def ogrodnik (T, D, Z, l):
    
    cost = []
    for i in D:
        BFS(T,0,i)
        cost.append(T[0][i])
    # print(cost)

    # return kanp_sack(cost,Z,l)
    return kanp_sack_memorize(cost,Z,l)

runtests( ogrodnik, all_tests=True )
