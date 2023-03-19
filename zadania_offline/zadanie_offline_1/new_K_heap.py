

def left(i):
    return (2 * i) + 1

def right(i):
    return (2 * i) + 2
def parent(i):
    return (i-1)//2


    
def heapifymax(A, n, i):
    l = left(i)
    r = right(i )
    max_ind = i
    if l < n and A[l] > A[max_ind]:
        max_ind = l
    if r < n and A[r] > A[max_ind]:
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

def build_heap_max(A):
    n = len(A)
    for i in range(n//2,-1,-1):
        heapifymax(A, n, i)

def build_heap(A):
    n = len(A)
    for i in range(n//2,-1,-1):
        heapify(A, n, i)

def heapify(A, n, i):
    l = left(i)
    r = right(i )
    max_ind = i
    if l < n and A[l] < A[max_ind]:
        max_ind = l
    if r < n and A[r] < A[max_ind]:
        max_ind = r
    if max_ind != i:
        A[i], A[max_ind] = A[max_ind], A[i]
        heapify(A, n, max_ind) 

def heap_sort(A):
    n = len(A)
    build_heap(A)
    for i in range(n-1, 0 ,-1):
        A[0],A[i] = A[i], A[0]
        heapify(A, i, 0)
    

def problem(A,k):
    T = []
    n = len(A)
    heap = A[:k+1]
    build_heap(heap)
    for i in range(k+1,n):
        T.append(heap[0])
        heap[0] = A[i]
        #heap[-1] = A[i]
        #build_heap(heap)
        build_heap(heap)
    
    heap_sort_max(heap)
    
    for j in range(len(heap)):
        T.append(heap[j])
    return T
        

k = 6
tab = [9,10,8,7,6,5,3,4]
print(tab)
res = problem(tab,k)
print(res)
