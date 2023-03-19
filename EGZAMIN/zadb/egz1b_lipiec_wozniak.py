'''Szymon Woźniak
Okej, już wytłumaczę, bo dużo się tu dzieje. Zaczę od tego, że na początku nie zdawałem sobie sprawy, że drzewo zawsze jest
ukorzenione, stąd też w moim kodzie pojawia się "i = 0" oraz dalej odwołania do i. Są to pozostałości pętli, która tutaj
występowała wcześniej. Okej. Teraz tak. Zaczynam od przerobienia wszystkiego na graf. Funkcja goThrough oblicza ile jest w 
tym grafie wierzchołków. Następnie funkcja goThroughMakeGraph zamienia wszystko na graf nieskierowany (stwierdziłem, że
w ten sposób będzie mi się dużo wygodniej pracowało - a nie psuje to złożoności obliczeniowej programu.). Okej, teraz tak.
Po stworzeniu grafu wywołuję na nim DFS, który ma za zadanie dla każdego wierzchołka wypisać jego "stopień wysokości" w drzewie.
Do tego wykorzystuję tablicę VALS2. Dodatkowo w tablicy VALS przetrzymuję, ile jest wierzchołków NA DANYM poziomie. Następnie
I pętla wylicza na podstawie VALS poziom, który będzie najlepszym do wzięcia pod uwagę (żeby było najszersze) i do odcięcia
od niego liści. Oczywiscie bierze pod uwagę także to, że wysokość też ma być jak największa w elifie. II pętla zajmuje się
tym aby w ZŁOŻONOŚCI LINIOWEJ posortować/ułożyć wierzchołki od największego stopnia wysokości do najmniejszego. Następnie
III pętla de facto składa się z dwóch pętl. Pierwsza z nich przypisuje LEVELBELOW True do wierzchołków o wyliczonym maxxie,
czyli stopniu wysokości który chcemy brać pod uwagę. Druga z nich "leci alternatywami do góry", aby każdy wierzchołek "wiedzial",
czy poniżej niego znajduje się jakiś wierzchołek o wyliczonym maxxie. Jeżeli wierzchołek wie, że taki jest, nie można go "odcinać".
Jeżeli wie, że nie ma, to będziemy musieli odciąć jego krawędź (tą, która do niego prowadzi). Następnie w sekcji
BFS tj. "finalizacji", zaczynam schodzić powoli w dół drzewa. Jak napotykam LEVELBELOW False, to odcinam to i nie schodzę już
tam dalej (ponieważ odcięcie odcina też całe drzewo) i zwiększam ilość odciętych krawędzi o 1. Następnie zwracam liczbę
wszystkich odciętych krawędzi i jest to koniec wykonywania algorytmu. Złożoność mojego algorytmu wynosi O(n). Wszystkie pętle
są maksymalnie liniowe, a BFS będąc zależnym od V+E wciąż jest liniowy. CKD.
'''

from egz1btesty import runtests
from collections import deque

class Node:
  def __init__( self ):
    self.left = None    # lewe poddrzewo
    self.right = None   # prawe poddrzewo
    self.x = None       # pole do wykorzystania przez studentow

vCount = 0

def goThrough(T):
  global vCount 

  if T.x is None:
    T.x = vCount
    vCount += 1 
    if T.left is not None:
      goThrough(T.left)
    if T.right is not None:
      goThrough(T.right)

def goThroughMakeGraph(G, T):
  if T is not None:
    if T.left is not None:
      G[T.x].append(T.left.x)
      G[T.left.x].append(T.x)
      goThroughMakeGraph(G, T.left)
    if T.right is not None:
      G[T.x].append(T.right.x)
      G[T.right.x].append(T.x)
      goThroughMakeGraph(G, T.right)

def DFS(G, V, VALS, VALS2, i, s):
  V[i] = True 
  VALS[s] += 1
  VALS2[i] = s

  for nb in G[i]:
    if not V[nb]:
      DFS(G, V, VALS, VALS2, nb, s+1)

def wideentall( T ):
    global vCount
    vCount = 0
    if T is not None:
      goThrough(T)
    G = [[] for _ in range(vCount)]
    if T is not None:
      goThroughMakeGraph(G, T)

    i = 0
    V = [False for _ in range(vCount)]
    VALS = [0 for _ in range(vCount)]
    VALS2 = [0 for _ in range(vCount)]

    DFS(G, V, VALS, VALS2, i, 0)

    maxx = 0
    maxxLevel = 0

    #I pętla
    for j in range(vCount):
      if VALS[j] > maxx:
        maxx = VALS[j]
        maxxLevel = j 
      elif VALS[j] == maxx:
        maxxLevel = j

    #II "pętla"
    FILL = [[] for _ in range(vCount)]
    for k in range(vCount):
      FILL[VALS2[k]].append(k)
    FILLS = []
    for k in range(vCount):
      for nb in FILL[k]:
        FILLS.append(nb)
    FILLS = FILLS[::-1]

    #III "pętla"
    LEVELBELOW = [False for _ in range(vCount)]
    for k in range(vCount):
      if VALS2[k] == maxxLevel:
        LEVELBELOW[k] = True 

    for k in range(vCount):
      for nb in G[FILLS[k]]:
        if VALS2[nb] < VALS2[FILLS[k]]:
          LEVELBELOW[nb] = LEVELBELOW[nb] or LEVELBELOW[FILLS[k]]

    #SEKCJA BFS - finalizacja
    count2 = 0
      
    Q = deque()
    Q.append(i)

    V2 = [False for _ in range(vCount)]

    while Q:
      v = Q.popleft()
      V2[v] = True 

      for nb in G[v]:
        if not V2[nb]:
          if LEVELBELOW[nb] == False:
            count2 += 1 
          else:
            Q.append(nb)

    return count2

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wideentall, all_tests = False )