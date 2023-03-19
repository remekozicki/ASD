

# def to_matrix(L):
#     row = len(L)
#     col = len(L[0])
#     G =  [[0 for i in range(col)] for j in range(row)]
#     for i in range(row):
#         for j in range(col):
#             if L[i][j] == ' ':
#                 G[i][j] = 1
#     return G

from queue import PriorityQueue


def Dixtra(G,A,B):
    row = len(G)
    col = len(G[0])

    visited = [[[[False for _ in range(4)] for _ in range(4)] for _ in range(col)]for _ in range(row)]
    movement = [[[[float('inf')for _ in range(4)] for _ in range(4)] for _ in range(col)]for _ in range(row)]
    j,i = A
    for k in range(4):
        for l in range(4):
            movement[i][j][k][l] = 0

    Q = PriorityQueue()

    # rotation: 0-up, 1-right, 2-down, 3-left
    # status: 0-0s, 1-60s, 2-40s,3-30
    # time,cords,last status ,curr rotation
    map_stat = [45,60,40,30]
    Q.put(0,A,0,1)
   

    while not Q.empty():

        rob = Q.get()

        time ,cords, stat, rot = rob
        x,y = cords

        if cords == B:
            return time
        
        if not visited[x][y][stat][rot]:
            visited[x][y][stat][rot] = True

            if rot == 0:
                if G[x-1][y] == ' ':
                    if movement[x-1][y][stat+1][rot] > movement[x][y][stat][rot] + 



 









L = [
    'XXXXXXXXXX',
    'X X      X',
    'X XXXXXX X',
    'X        X',
    'XXXXXXXXXX',
    ]

