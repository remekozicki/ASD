
from turtle import distance


def create_turns():
    # x, y
    T = [[1,0], #G
        [-1,0], #D
        [0,1]]  #P
    return T


def dym(L):
    n = len(L)

    DP  = [[-1 for _ in range(n)]for _ in range(n)]
    turns = create_turns()
    x = 0
    y = 0
    res = rec(L,DP,turns,n,x,y)
    return res

def rec(L,DP,turns,n,x,y):

    if x == n-1 and y == n-1:
        return 0
    
    if DP[x][y] != -1:
        return DP[x][y]
    
    maxi = -1
    for i in range(3):
        tx = x + turns[i][0]
        ty = y + turns[i][1]
        if tx >= 0 and tx < n and ty >= 0 and ty < n-1 and L[tx][ty] != '#':
            maxi = max(maxi, rec(L,DP,turns,n,tx,ty)+1)
    DP[x][y] = maxi
    return DP[x][y]
        
def DFS(L):

    n = len(L)
    visited = [[False for _ in range(n)] for _ in range(n)]
    distance = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if L[i][j] == '#':
                visited[i][j] = True
    
    turn = create_turns()
    x = 0
    y = 0
    rec(L,visited,distance,x,y,n)
    return distance[n-1][n-1]

def rec(L,visited,distance,x,y,n):

    visited[x][y] = True

    if x + 1 < n and not visited[x+1][y]:
        distance[x+1][y] = distance[x][y] + 1
        rec(L,visited,distance,x+1,y,n)

    if x - 1 > -1 and not visited[x-1][y]:
        distance[x-1][y] = distance[x][y] + 1
        rec(L,visited,distance,x-1,y,n)
        
    if y + 1 < n and not visited[x][y+1]:
        distance[x][y+1] = distance[x][y] + 1
        rec(L,visited,distance,x,y+1,n)


    




        
L = [ '....',
    '..#.',
    '..#.',
    '....']

print(DFS(L))







