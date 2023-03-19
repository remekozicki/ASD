

class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

def left(i):
    return (2 * i) + 1

def right(i):
    return (2 * i) + 2

def parent(i):
    return (i - 1) // 2

def heapify(A, n, i):
    l = left(i)
    r = right(i )
    max_ind = i
    if l < n and A[l].val > A[max_ind].val:
        max_ind = l
    if r < n and A[r].val > A[max_ind].val:
        max_ind = r
    if max_ind != i:
        A[i], A[max_ind] = A[max_ind], A[i]
        heapify(A, n, max_ind) 

def build_heap(A):
    n = len(A)
    for i in range(parent(n-1),-1,-1):
        heapify(A, n, i)

def heap_sort(A):
    n = len(A)
    build_heap(A)
    for i in range(n-1,0,-1):
        A[0],A[i] = A[i], A[0]
        heapify(A, i, 0)

def SotrH(p,k):

    T = []
    while p != None:
        tmp = p
        p = p.next
        tmp.next = None
        T.append(tmp)
    heap_sort(T)


    g = Node(None)
    q = g
    
    for i in range(len(T)):
        q.next = T[i]
        q = q.next
    p = g.next
    
    


    




def add_to_list(self,x):
    new_el = Node(x)
    if self.head:
        p = self.head
        while p.next:
            p = p.next
        p.next = new_el
    else:
        self.head = new_el

def create_list(self, tab):
    for i in range(len(tab)):
        add_to_list(self, tab[i])

def print_list(self):
    tmp = self.head
    while tmp:
        print(tmp.val, '->', sep='', end='')
        tmp = tmp.next
    print()

l_list = LinkedList()
res = LinkedList()
tab = [1,5,4,1,5,45,20,5,1]
create_list(l_list,tab)
res.head = SotrH(l_list.head,0)
print_list(res)




