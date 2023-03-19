from kol3atesty import runtests

from queue import PriorityQueue


'''
Remigiusz Kozicki
zacowana słożoność to n^2, przez tworzenie reprezenatcji macierzowej w kórej łatwiej jest 
dodać połączenia teleportów. Robi to funkcja 'too_matrix()' tworząc połaczenia z godnie z tablicą E
a pomiędzy wierzchołkami z tablicy S towrzy połączenia o wadze 0. Tam gdzie nie ma połaczenia jest -1


Główną częścią algorytu jest kalsyczny algorytm Dijkstry ("Dixtra"), obliczający najkótrzą ćsieżkę
w grafie ważonym

'''

def too_matrix(S,E,n):

    G = [[-1 for _ in range(n)] for _ in range(n)]

    for v in E:
        # 1 wspłórzedna 2współrzedna odległość 
        x,y,w = v
        G[x][y] = w
        G[y][x] = w
    # uzupełnienie grafu o teleporty
    for i in S:
        for j in S:
            G[i][j] = 0
    
    return G

def Dixtra(E,S,n,a,b):
    G = too_matrix(S,E,n)

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

        for v in range(n):
            if not visited[v] and G[u][v] != -1:

                # releksacja z wykładu
                if distance[v] > distance[u] + G[u][v]:
                    distance[v] = distance[u] + G[u][v]
                    Q.put([distance[v],v])

    return None


def spacetravel( n, E, S, a, b ):
    # tu prosze wpisac wlasna implementacje
    return Dixtra(E,S,n,a,b)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )