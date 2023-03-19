'''Sortowanie kopcowe'''


def left(i):
    return (2 * i) + 1

def right(i):
    return (2 * i) + 2

def parent(i):
    return (i-1) // 2

def heapify(A, n, i):
    l = left(i)
    r = right(i )
    max_ind = i
    if l < n and A[l] > A[max_ind]:
        max_ind = l
    if r < n and A[r] > A[max_ind]:
        max_ind = r
    if max_ind != i:
        A[i], A[max_ind] = A[max_ind], A[i]
        heapify(A, n, max_ind) 

def build_heap(A):
    n = len(A)
    for i in range(parent(n-1),-1,-1):
        heapify(A, n, i)
    print(A)

def heap_sort(A,k):
    n = len(A)
    
    build_heap(A)
    for i in range(n-1,0,-1):
        A[0],A[i] = A[i], A[0]
        heapify(A, n, 0)


def build_small_heap(A,k):
    n = len(A)
    
    T_k = A[-k-1:] 
    heap_sort(T_k,k)     
    
    for i in range(n-1,0,-1):
        if i < k+1:
            
        A[i],T_k[0] = T_k[0], A[i - (k+1)]
        heap_sort(T_k,k)






k = 2
tab = [1, 0, 3, 4, 2, 6, 5]
print(tab)
build_small_heap(tab,k)
print(tab)
