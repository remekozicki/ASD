from math import inf
from queue import PriorityQueue

from zad2testy import runtests


def robot( L, A, B ):
    G = makeGraph(L)
    #print(G)
    options = [[45, 60, 40, 30] for _ in range(4)]

    #0 - dół 1 - prawo 2 - góra 3 - lewo
    #0 - 45 1 - 60 2 - 40 3 - 30
    d = Dijkstra(G, A[0] + A[1] * len(L), options)
    b = B[0] + B[1] * len(L)
    minimum = inf

    for i in range(4):
        for j in range(4):
            minimum = min(minimum, d[i][j][b])

    print(d)
    return minimum

def Dijkstra(G, a, options):
    d = [[[inf for _ in range(len(G))] for _ in range(4)]for _ in range(4)]
    visited = [[[False for _ in range(len(G))] for _ in range(4)]for _ in range(4)]
    parents = [[[-1 for _ in range(len(G))] for _ in range(4)]for _ in range(4)]
    q = PriorityQueue()

    # 0 - dół 1 - prawo 2 - góra 3 - lewo
    # 0 - 45 1 - 60 2 - 40 3 - 30
    #speed, turn, u
    d[0][1][a] = 0
    q.put((0, a, 1, 0))

    while not q.empty():
        _, u, turn, speed = q.get()

        if not visited[speed][turn][u]:
            for v in G[u]:
                x_u = u % len(G)
                y_u = u // len(G)
                x_v = v % len(G)
                y_v = v // len(G)

                sideToGo = 0

                if x_v > x_u:
                    sideToGo = 0
                elif x_v < x_u:
                    sideToGo = 2
                elif y_v > y_u:
                    sideToGo = 1
                elif y_v < y_u:
                    sideToGo = 3

                newSpeed = speed
                if turn == sideToGo:
                    if speed < 3: newSpeed += 1
                else:
                    newSpeed = 0

                value = 45
                if newSpeed == 1: value = 60
                elif newSpeed == 2: value = 40
                elif newSpeed == 3: value = 30

                if relax(d, parents, u, v, speed, turn, newSpeed, sideToGo, value):
                    q.put((d[newSpeed][sideToGo][v], v, sideToGo, newSpeed))

        visited[speed][turn][u] = True
    return d

def relax(d, parent, u, v, u_speed, u_turn, v_speed, v_turn, value):
    if d[v_speed][v_turn][v] > d[u_speed][u_turn][u] + value:
        d[v_speed][v_turn][v] = d[u_speed][u_turn][u] + value
        parent[v_speed][v_turn][v] = u
        return True
    return False

def makeGraph(L):
    G = [[] for _ in range(len(L) * len(L[0]))]
    n = len(L)

    for i in range(len(L)):
        for j in range(len(L[i])):
            if L[i][j] == ' ':
                if i + 1 < len(L) and L[i + 1][j] == ' ':
                    G[i + j * n].append((i + 1) + j * n)
                if i - 1 >= 0 and L[i - 1][j] == ' ':
                    G[i + j * n].append((i - 1) + j * n)
                if j + 1 < len(L[i]) and L[i][j + 1] == ' ':
                    G[i + j * n].append(i + (j + 1) * n)
                if i - 1 >= 0 and L[i][j - 1] == ' ':
                    G[i + j * n].append(i + (j - 1) * n)

    return G
    
runtests( robot )


