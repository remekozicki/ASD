from queue import PriorityQueue
from zad2testy import runtests

def dikstra(L,A,B):
    G = to_list(L)
    r = len(L)
    n = len(G)

    visited = [[[False for i in range(3)] for _ in range(4)] for i in range(n)]
    distance = [[[float('inf') for i in range(3)] for _ in range(4)] for i in range(n)]
    #visited = [[[False for i in range(4)] for _ in range(4)] for i in range(n)]

    Q = PriorityQueue()

    # 0 - dół 1 - prawo 2 - góra 3 - lewo
    # 0 - 60 1 - 40 2 - 30
    a = A[1] + A[0] * r
    b = B[1] + B[0] * r
    # u, turn, speed
    distance[a][1][0] = 0
    
    # dis, speed, turn, u
    start = [0,0,1,a]
    Q.put(start)

    while not Q.empty():

        dis, speed, turn, u = Q.get()

        if u == b:
            return dis
        
        if not visited[u][turn][speed]:
            visited[u][turn][speed] = True

            for v in G[u]:

                x_u = u % r
                y_u = u // r
                x_v = v % r
                y_v = v // r

                # turnToGo
                
                if x_u > x_v:
                    turnToGo = 2
                elif x_u < x_v:
                    turnToGo = 0
                elif y_u > y_v:
                    turnToGo = 3
                elif y_u < y_v:
                    turnToGo = 1
                
                # speed
                spin = 0
                if turn == turnToGo:
                    if speed < 2:
                        newspeed = speed + 1
                    else:
                        newspeed = speed 
                else:
                    newspeed = 0
                    spin = 45

                
                if newspeed == 0: value = 60
                elif newspeed == 1: value = 40
                elif newspeed == 2: value = 30
                value += spin
                # relax
                if not visited[v][turnToGo][newspeed]:
                    if distance[v][turnToGo][newspeed] > dis + value:
                        distance[v][turnToGo][newspeed] = dis + value
                        Q.put([distance[v][turnToGo][newspeed],newspeed,turnToGo,v])

    return None


def to_list(L):
    r = len(L)
    c = len(L[0])

    G = [[] for i in range(r * c)]

    for i in range(r):
        for j in range(c):
            if L[i][j] == ' ':
                if i+1 < r and L[i+1][j] == ' ':
                    G[i + j * r].append((i+1) + j *r)
                if i-1 > -1 and L[i-1][j] == ' ':
                    G[i + j * r].append((i-1) + j *r)
                if j+1 < c and L[i][j+1] == ' ':
                    G[i + j * r].append(i + (j+1) *r)
                if j-1 > -1 and L[i][j-1] == ' ':
                    G[i + j * r].append(i + (j-1) *r)
    return G

def robot( L, A, B ):
    """tu prosze wpisac wlasna implementacje"""
    return dikstra(L,A,B)

    
runtests( robot )


