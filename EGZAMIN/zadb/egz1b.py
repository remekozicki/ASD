



'''Remigiusz Kozicki
próba zakończona totalną porażką, nie rozumiem do końca zadania,
nie potrafie wykanać algorytmu.

Ale...

gdyby algorytm miał działać to sprawdzałbym poziom na jakim znajduje sie każdy wierzchołek
i czy jest liściem. mógłbym wtedy przejść po każdym wszystkich liściach  i usuwać te które są niżej 
tak gługo aż nie napotkamy innych liści na tym poziomie. wtedy sprawdzać czy jest jakiś liść wyżej któtry
nie pasuje do wysokości i czy po jego usunięciu dałoby to nam rozwiązanies

:(
'''

from egz1btesty import runtests

class Node:
  def __init__( self ):
    self.left = None    # lewe poddrzewo
    self.right = None   # prawe poddrzewo
    self.x = None       # pole do wykorzystania przez studentow


def create_graph(root,tab):
  if root != None:
    if root.left != None:
      tab[root.x[1]].append(root.left.x)
      tab[root.left.x[1]].append(root.x)
      create_graph(root.left,tab)
    
    if root.right != None:
      tab[root.x[1]].append(root.right.x)
      tab[root.right.x[1]].append(root.x)
      create_graph(root.right,tab)

def find_leaves(T):

  root = T
  idx = 0
  hight = -1
  v_count = 0
  maxi = -1

  def  high_tree(root,idx):
    nonlocal  hight,v_count
    if root.left == None and root.right == None:
      #liść
      root.x = [idx,v_count]
      
      hight = max(hight,idx)
      return 
    
    elif root.left != None and root.right == None:
      
      root.x = [idx,v_count]
      hight = max(hight,idx)
      v_count += 1
      idx += 1
      root = root.left
      high_tree(root,idx)

    
    elif root.left == None and root.right != None:
      root.x = [idx,v_count]

      hight = max(hight,idx)
      v_count += 1
      idx += 1
      root = root.right
      high_tree(root,idx)

    else:
      root.x = [idx,v_count]
      
      hight = max(hight,idx)
      idx += 1
      rootl = root.left
      rootr = root.right
      v_count += 1
      high_tree(rootl,idx)
      v_count += 1
      high_tree(rootr,idx)
  
  high_tree(root,idx)

  n = v_count + 1
  graph = [[] for _ in range(n)]
  hights = [0 for _ in range(hight+1)]

  create_graph(root,graph)

  

  return


# nie działa nie wiem dlaczego przez co nie jestem w stanie zrobic zadania dalej



def wideentall( T ):
    # tu prosze wpisac wlasna implementacje
    return find_leaves(T)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wideentall, all_tests = False )