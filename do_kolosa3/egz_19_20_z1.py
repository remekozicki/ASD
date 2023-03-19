'''
[2pkt.] Zadanie 1.
Szablon rozwiązania: zad1.py
Każdy nieskierowany, spójny i acyckliczny graf G = (V, E) możemy traktować jako drzewo. Ko-
rzeniem tego drzewa może być dowolny wierzchołek v ∈ V . Napisz funkcję best root(L), która
przyjmuje nieskierowany, spójny i acyckliczny graf G (reprezentowany w postaci listy sąsiedztwa) i
wybiera taki jego wierzchołek, by wysokość zakorzenionego w tym wierzchołku drzewa była możli-
wie najmniejsza. Jeśli kilka wierzchołków spełnia warunki zadania, funkcja może zwrócić dowolny z
nich. Wysokość drzewa definiujemy jako liczbę krawędzi od korzenia do najdalszego liścia. Uzasadnij
poprawność zaproponowanego algorytmu i oszacuj jego złożoność obliczeniową.
Funkcja best root(L) powinna zwrócić numer wierzchołka wybranego jako korzeń. Wierzchołki
numerujemy od 0. Argumentem best root(L) jest lista postaci:
L = [l0, l1, . . . , ln-1],
gdzie li to lista zawierająca numery wierzchołków będących sąsiadami i-tego wierzchołka. Można
przyjąć (bez weryfikacji), że lista opisuje graf spełniający warunki zadania. W szczególności, graf
jest spójny, acykliczny, oraz jeśli a ∈ lb to b ∈ la (graf jest nieskierowany). Nagłówek funkcji powinien
mieć postać:
def best_root(L):

'''


from queue import PriorityQueue
from turtle import distance


def too_krawendz(L):
    n = len(L)

    G = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in L[i]:
            G[i][j] = 1
    
    return G

def  Floyd_warshall(L):
    G = too_krawendz(L)
    n  = len(G)
    D = [[float('inf') for j in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                D[i][j] = 0
            else:
                if G[i][j] == 1:
                    D[i][j] = 1


    for k in range(n):
        for i in range(n):
            for j in range(n):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])
    
    
    min_val = float('inf')
    for i in range(n):
        if min_val >  max(D[i]):
            min_val = max(D[i])
            ind = i
    
    return ind

def BFS(L):
    n = len(L)
    min_val = float('inf')
    ind = None
    for w in range(n):
        visited = [False for i in range(n)]
        distance = [0 for i in range(n)]
        Q = PriorityQueue()
        Q.put(w)

        while not Q.empty():

            u = Q.get()

            for v in L[u]:
                if not visited[v]:
                    visited[v] = True
                    distance[v] = distance[u] + 1
                    Q.put(v)
        
        if min_val > max(distance):
            min_val = max(distance)
            ind = w

    return ind





L = [ [ 2 ],
[ 2 ],
[ 0, 1, 3],
[ 2, 4 ],
[ 3, 5, 6 ],
[ 4 ],
[ 4 ] ]

print(Floyd_warshall(L))
print(BFS(L))