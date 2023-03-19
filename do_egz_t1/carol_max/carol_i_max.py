# Carol musi przewieźć pewne niebezpieczne substancje z laboratorium x do laboratorium y, podczas
# gdy Max musi zrobić to samo, ale w przeciwną stronę. Problem polega na tym, że jeśli substancje te
# znajdą się zbyt blisko siebie, to nastąpi reakcja w wyniku której absolutnie nic się nie stanie
# (ale szefowie Carol i Max nie chcą do tego dopuścić, by nie okazało się, że ich praca nie jest nikomu
# potrzebna). Zaproponuj, uzasadnij i zaimplementuj algorytm planujący jednocześnie trasy Carol i Maxa
# tak, by odległość między nimi zawsze wynosiła co najmniej d. Mapa połączeń dana jest jako graf
# nieskierowany, w którym każda krawędź ma dodatnią wagę (x i y to wierzchołki w tym grafie).
# W jednostce czasu Carol i Max pokonują dokładnie jedną krawędź. Jeśli trzeba, dowolne z nich może się
# w danym kroku zatrzymać (wówczas pozostaje w tym samym wierzchołku). Carol i Max nie mogą równocześnie
# poruszać się tą samą krawędzią (w przeciwnych kierunkach).
# Rozwiązanie należy zaimplementować w postaci funkcji:
# def keep_distance(M, x, y, d):
#     ...
# która przyjmuje numery wierzchołków x oraz y, minimalną odległość d i graf reprezentowany przez
# kwadratową, symetryczną macierz sąsiedztwa M. Wartość M[i][j] == M[j][i] to długość krawędzi między
# wierzchołkami i oraz j, przy czym M[i][j] == 0 oznacza brak krawędzi między wierzchołkami. W macierzy
# nie ma wartości ujemnych. Funkcja powinna zwrócić listę krotek postaci:
# [(x, y), (u[1], v[1]), (u[2], v[2]), ..., (u[k], v[k]), (y, x)]
# reprezentującą ścieżki Carol i Max. W powyższej liście element (u[i], v[i]) oznacza, że Carol znajduje
# się w wierzchołku u[i], zaś Max w wierzchołku v[i]. Można założyć, że rozwiązanie istnieje.

from queue import Queue
from testy import runtests

def Floyd_warshal(M):

    n = len(M)

    dis = [[float('inf') for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            if M[i][j] != 0:
                dis[i][j] = M[i][j]
    
    for i in range(n):
        dis[i][i] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dis[i][j] =  min(dis[i][j], dis[i][k] + dis[k][j])
    
    return dis

def BFS(G,start):
    n = len(G)
    visited = [False for _ in range(n)]
    parents = [None for _ in range(n)]

    Q = Queue()

    Q.put(start)

    while not Q.empty():
        u = Q.get()
        visited[u] = True

        for v in range(n):
            if G[u][v] != 0 and not visited[v]:
                visited[v] = True
                parents[v] = u
                Q.put(v)
    
    return parents


def create_graph(M,x,y,d):
    m =len(M)

    dis = Floyd_warshal(M)

    G = [[ 0 for _ in range(m*m)] for _ in range(m*m)]
    for i in range(m):
        for j in range(m):
            if i != j and dis[i][j] >= d:
                for u in range(m):
                    for v in range(m):
                        if u != v and dis[u][v] >= d:
                            if not (u == j and i == v):
                                if (i == u and M[j][v] != 0) or (j == v and M[i][u] != 0) or (M[i][u] != 0 and M[j][v] != 0):
                                    G[i*m+j][u*m+v] = 1
    
    
    start = x*m+y
    parents = BFS(G,start)

    res = []

    idx = y*m+x
    
    while idx != None:
        res.append([idx % m, idx // m])
        idx = parents[idx]
    
    return res


M = [[0,1,1,0],
    [1,0,0,1],
    [1,0,0,1],
    [0,1,1,0]]

x = 0
y = 3
d = 2

# x*n + y

runtests(create_graph)