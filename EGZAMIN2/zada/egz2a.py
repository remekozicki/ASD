'''
Remigiusz Kozicki
klasyczne podejście n2
tworze tablice magazynów i patrze do którego moge jeszcze dodać transport
gdy dojde do ostatniego transportu zwracam indeks magazynu do którego trafił

'''
from egz2atesty import runtests

class Node:
  def __init__( self ):
    self.next = None 
    self.mag = 0  # prawe poddrzewo
    self.cap = 0

def drzewem(A,T):
    n = len(A)
    root = Node()
    head = root
    curr = head

    for i in range(n):
        if curr.cap + A[i] <= T:
            curr.cap += A[i]
        else:
            tmp = Node()
            curr.next = tmp
            mag = curr.mag
            curr = curr.next
            curr.mag = mag + 1
            curr.cap += A[i]
        curr = head
    return curr.mag

def run_and_sort(A, T):
    # index(A)
    n = len(A)
    tab = [0 for i in range(n)]
    for i in range(n):
        for j in range(n):
            if tab[j]+A[i] <= T:
                tab[j] += A[i]
                if i == n-1:
                    return j
                break


def coal(A, T):
    # tu prosze wpisac wlasna implementacje
    # return run_and_sort(A, T)
    return run_and_sort(A, T)



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(coal, all_tests=True)
