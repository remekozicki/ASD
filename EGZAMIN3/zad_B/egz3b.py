from egz3btesty import runtests

'''
Remigiusz Kozicki
złożonośc w którą celowałem to O(n^2)
podejście DFS 
tablica zapamiętująca (DP) jest nxn

traktuje labitynt jako graf i przechodze go DFS sprawdzając czy moge iśc do danej komnaty czy nie 
komnaty które sa oznaczone '#' ustawiam odrazu na odwidzone
w tablicy distance zwiększam pokoleji dystanse względem poprzeniego wiezszchołka(komnaty)

wydaje mi sie że pomysł jest całkiem dobry i ciekawy jednak przechodzi tylko 2 testy

próbowałem wcześniej dynamicznie jednak nie działało w ogóle :)s
'''

def create_turns():
    # x, y
    T = [[1,0], #G
        [-1,0], #D
        [0,1]]  #P
    return T

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
        

def maze( L ):
    # tu prosze wpisac wlasna implementacje
    return DFS(L)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = False )
