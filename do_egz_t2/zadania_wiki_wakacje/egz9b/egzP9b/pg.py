


def unique(T,R):
    n = len(T)
    for u in range(n):
        if T[u] != []:
            T[u].sort()
            idx = 0
            T[u][0] = [T[u][0],idx]
        
            for v in range(1,len(T[u])):

                if T[u][v] == T[u][v-1][0]:
                    idx += 1
                else:
                    idx = 0
                T[u][v] = [T[u][v],idx]

        if R[u] != []:
            R[u].sort()
            idx = 0
            R[u][0] = [R[u][0],idx]

            for v in range(1,len(R[u])):

                if R[u][v] == R[u][v-1][0]:
                    idx += 1
                else:
                    idx = 0
                R[u][v] = [R[u][v],idx]
        
          


def DFS(T,R):
    path = []
    unique(T,R)
    rec_dfs(T,R,0,path)
    return path

def rec_dfs(T,R,u,path):

    for i in range(len(T[u])):
        v = T[u][i]
        if v != None and not v in R[u]:
            T[u][i] = None
            rec_dfs(T,R,v[0],path)
    path.append(u)






# T = [
#     [1, 0, 2], #0
#     [2, 0], #1
#     [1, 0]  #2
#     ]
# R = [
#     [0],
#     [],
#     []
#     ]

T = [[1, 1, 4, 4], [3, 0, 1, 2, 4], [1, 0, 3], [0, 4, 3, 2], [2, 0, 4, 1, 3]]
R = [[4], [], [0], [3, 2], [3]]
print(DFS(T,R))

# def test():
#     tab = [0]
#     if False == tab[0]:
#         return True
#     else:
#         return False

# print(test())