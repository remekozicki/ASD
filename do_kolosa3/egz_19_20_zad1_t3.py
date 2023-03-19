'''
Pewna kraina składa się z wysp pomiędzy którymi istnieją połączenia lotnicze, promowe oraz mosty.
Pomiędzy dwoma wyspami istnieje co najwyżej jeden rodzaj połączenia. Koszt przelotu z wyspy
na wyspę wynosi 8B, koszt przeprawy promowej wynosi 5B, za przejście mostem trzeba wnieść
opłatę 1B. Poszukujemy trasy z wyspy A na wyspę B, która na kolejnych wyspach zmienia środek
transportu na inny oraz minimalizuje koszt podróży.
Dana jest tablica G, określająca koszt połączeń pomiędzy wyspami. Wartość 0 w macierzy
oznacza brak bezpośredniego połączenia. Proszę zaimplementować funkcję islands( G, A, B )
zwracającą minimalny koszt podróży z wyspy A na wyspę B. Jeżeli trasa spełniająca warunki zadania
nie istnieje, funkcja powinna zwrócić wartość None.

'''



from queue import PriorityQueue

# 0- samolot, 1 - prom, 2 - most
def islands(G,A,B):

    n = len(G)

    visited = [[False,False,False] for i in range(n)]
    costs = [[float('inf'),float('inf'),float('inf')] for i in range(n)]
    
    for i in range(3):
        #visited[A][i] = True
        costs[A][i] = 0

    Q = PriorityQueue()
    Q.put([0,A,0])
    Q.put([0,A,1])
    Q.put([0,A,2])

    while not Q.empty():

        cost, u, trans = Q.get()

        if u == B:
            return cost
        
        if not visited[u][trans]:
            visited[u][trans] = True

            for v in range(n):
                for i in range(3):
                    if i != trans and G[u][v] != 0 and not visited[v][i]:
                        if costs[v][i] > costs[u][trans] + G[u][v]:
                            costs[v][i] = costs[u][trans] + G[u][v]
                            Q.put([costs[v][i], v, i])
    return None




G1 = [ [0,5,1,8,0,0,0 ],
        [5,0,0,1,0,8,0 ],
        [1,0,0,8,0,0,8 ],
        [8,1,8,0,5,0,1 ],
        [0,0,0,5,0,1,0 ],
        [0,8,0,0,1,0,5 ],
        [0,0,8,1,0,5,0 ] ]

print(islands(G1, 5, 2))