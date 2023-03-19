from zad1testy import Node, runtests


def left(i):
    return (2 * i) + 1

def right(i):
    return (2 * i) + 2

def heapifymax(A, n, i):
    l = left(i)
    r = right(i )
    max_ind = i
    if l < n and A[l].val > A[max_ind].val:
        max_ind = l
    if r < n and A[r].val > A[max_ind].val:
        max_ind = r
    if max_ind != i:
        A[i], A[max_ind] = A[max_ind], A[i]
        heapifymax(A, n, max_ind) 

def heap_sort_max(A):
    n = len(A)
    build_heap_max(A)
    for i in range(n-1, 0 ,-1):
        A[0],A[i] = A[i], A[0]
        heapifymax(A, i, 0)

# funkcje z dopiskiem "MAX" sortują kopcem maksymalnym 
# i wykorzystywane są do sortowania k+1 ostatnich elementów które zostają w kopcu.
def build_heap_max(A):
    n = len(A)
    for i in range(n//2,-1,-1):
        heapifymax(A, n, i)

def heapify(A, n, i):
    l = left(i)
    r = right(i )
    max_ind = i
    if l < n and A[l].val < A[max_ind].val:
        max_ind = l
    if r < n and A[r].val < A[max_ind].val:
        max_ind = r
    if max_ind != i:
        A[i], A[max_ind] = A[max_ind], A[i]
        heapify(A, n, max_ind) 

def build_heap(A):
    n = len(A)
    for i in range((n-1)//2,-1,-1):
        heapify(A, n, i)

def heap_sort(A):
    n = len(A)
    
    for i in range(n-1,-1,-1):
        A[0],A[i] = A[i], A[0]
        heapify(A, n, 0)
# sortowanie przez wstawianie się najszybrze dla k == 1 dlatego jest wykorzystywany dla tego przypadku
def insertion_sort(T):

    for i in range(1,len(T)):
        X = T[i]
        j = i - 1
        while j >= 0 and T[j].val > X.val:
            T[j+1] = T[j]
            j -= 1
        T[j+1] = X
 

def SortH(p,k):

# likedlist'a jest "cięta" na osobne Node'y i zapisywana w tablicy,
# gdyż tablicę łatwiej posortować "heap_sort'em" ze względu na dostępność elementów  
    T = []
    while p != None:
        tmp = p
        p = p.next
        tmp.next = None
        T.append(tmp)
# strażnik do kórego bedziemy przypinać posortowane Node'y  
    g = Node()
    g.val = None
    q = g
# insertion dla k == 1
    if k == 1:
        insertion_sort(T)
        for i in range(len(T)):
            q.next = T[i]
            q = q.next
        p = g.next
        return p
# heap sort dla k != 1
    n = len(T)
    heap = T[:k+1]
    build_heap(heap)
    for i in range(k+1,n):
        q.next = heap[0]
        q = q.next
        heap[0] = T[i]
        build_heap(heap)
    heap_sort_max(heap)

# przypinanie posortowanych elementów z tablicy do strażnika
    for j in range(len(heap)):
        q.next = heap[j]
        q = q.next
    p = g.next
    return p

runtests( SortH ) 
