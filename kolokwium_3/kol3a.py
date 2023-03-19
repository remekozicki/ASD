'''
Remigiusz Kozicki
szacowana złożoność to mlogn + S^2 gdzie S to długość listy S, tworze reprezentacje listy sąsiedztwa grafu nieskierowanego,
dodając połączenia pomędzy portalami z wagą 0. dzieje się to w funkcji "too_list()"


Główną częścią algorytu jest kalsyczny algorytm Dijkstry ("Dixtra"), obliczający najkótszą ścieżkę
w grafie ważonym

'''

from kol3atesty import runtests

from queue import PriorityQueue

def too_list(S,E,n):

    G = [[] for _ in range(n)]

    for v in E:
        # współrzedna "do", odległość 
        x,y,w = v
        G[x].append([y,w])
        G[y].append([x,w])
    # uzupełnienie grafu o teleporty
    for i in S:
        for j in S:
            if i != j:
                G[i].append([j,0])
                G[j].append([i,0])

    return G

def Dixtra(E,S,n,a,b):
    G = too_list(S,E,n)

    visited = [False for _ in range(n)]
    distance = [float('inf') for _ in range(n)]


    Q = PriorityQueue()

    start = [0,a] # aktualna przejechana odległość, aktualny wierzchołek 

    Q.put(start)

    distance[a] = 0

    while not Q.empty():

        d_u, u = Q.get()

        if u == b:
            return d_u
        
        visited[u] = True

        for v, d_v in G[u]:
            if not visited[v]:

                # releksacja z wykładu
                if distance[v] > distance[u] + d_v:
                    distance[v] = distance[u] + d_v
                    Q.put([distance[v],v])

    return None


def spacetravel( n, E, S, a, b ):
    # tu prosze wpisac wlasna implementacje
    return Dixtra(E,S,n,a,b)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )