'''Pewien podróżnik chce przebyć trasę z punktu A
do punktu B. Niestety jego samochód spala dokładnie jeden litr paliwa na jeden kilometr trasy. W baku mieści
się dokładnie D litrów paliwa. Trasa jest reprezentowana jako graf, gdzie wierzchołki to miasta a krawędzie to
łączące je drogi. Każda krawędź ma długość w kilometrach (przedstawioną jako licza naturalna). W każdym
wierzchołku jest stacja benzynowa, z daną ceną za litr paliwa. Proszę podać algorytm znajdujący trasę z
punktu A do punktu B o najmniejszym koszcie. Proszę uzasadnić poprawność algorytmu.'''




from queue import PriorityQueue


def dijikstra_tank(G,P,B,a,b):
    n = len(G)
    Q = PriorityQueue()

    visited = [[False for _ in range(B)] for _ in range(n)]
    costs = [[float('inf') for _ in range(B)] for _ in range(n)]

    start = (0,a,0)
    costs[a][0] = 0

    Q.put(start)

    while not Q.empty():

        u = Q.get()
        x,y,z = u

        if y == b:
            return x

        if not visited[y][z]:
            visited[y][z] = True
            i = 0

            while i+z <= B:
                for v in G[y]:
                     if v[1] <= i+z and costs[v[0]][i+z-v[1]] > x + i*P[y]:
                        costs[v[0]][i+z - v[1]] = x + i*P[y]
                        Q.put((x + i*P[y], v[0], i+z - v[1]))
                i+=1
    return None


G = [
    [(1,3),(4,2),(3,3)],    # 0
    [(0,3),(3,4),(2,5)],    # 1
    [(1,5),(3,2),(7,1)],    # 2
    [(0,3),(1,4),(2,2),(6,4)],  # 3
    [(0,2),(5,3)],      # 4
    [(4,3),(6,4),(8,3)]   ,  # 5
    [(5,4),(3,4),(8,2),(7,3)],  # 6
    [(2,1),(6,3),(8,1)], # 7
    [(5,3),(6,2),(7,1)]  #8

]
P = [1,3,2,2,2,2,4,4,3]

print(dijikstra_tank(G, P, 5, 0, 8))
        
