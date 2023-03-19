
def partition_cords(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j][0] <  x[0]:
            i += 1
            A[i], A[j] = A[j],A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def partition_range(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if (A[j][1] - A[j][0]) > (x[1] - x[0]):
            i += 1
            A[i], A[j] = A[j],A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1    

class Stack:
    def __init__(self) -> None:
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, data):
        return self.items.append(data)
    
    def pop(self):
        return self.items.pop()

def quick_sort_stack_cords(T, p, r):
    s = Stack()
    s.push((p,r))
    while not s.is_empty():
        p,r = s.pop()
        if p < r:
            pivot = partition_cords(T,p,r)
            if (pivot - p) < (r - pivot):
                s.push((pivot+1,r))
                s.push((p,pivot-1))
            else:
                s.push((p,pivot-1))
                s.push((pivot+1,r))

def quick_sort_stack_range(T, p, r):
    s = Stack()
    s.push((p,r))
    while not s.is_empty():
        p,r = s.pop()
        if p < r:
            pivot = partition_range(T,p,r)
            if (pivot - p) < (r - pivot):
                s.push((pivot+1,r))
                s.push((p,pivot-1))
            else:
                s.push((p,pivot-1))
                s.push((pivot+1,r))

def merge_sort_range(T):
    if len(T) > 1:
        mid = len(T) // 2
        L = T[:mid]
        R = T[mid:]
        # print("L:", L)
        # print("R:", R)
        merge_sort_range(L)

        merge_sort_range(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if (L[i][1]-L[i][0]) < (R[j][1] - R[j][0]) and L[i][0] <= R[j][0]:
                T[k] = L[i]
                i += 1
            else:
                T[k] = R[j]
                j += 1
            k += 1
        while len(L) > i:
            T[k] = L[i]
            i += 1
            k += 1
        while len(R) > j:
            T[k] = R[j]
            j += 1
            k += 1

def merge_sort_cords(T):
    if len(T) > 1:
        mid = len(T) // 2
        L = T[:mid]
        R = T[mid:]
        # print("L:", L)
        # print("R:", R)
        merge_sort_cords(L)

        merge_sort_cords(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i][0] <= R[j][0]:
                T[k] = L[i]
                i += 1
            else:
                T[k] = R[j]
                j += 1
            k += 1
        while len(L) > i:
            T[k] = L[i]
            i += 1
            k += 1
        while len(R) > j:
            T[k] = R[j]
            j += 1
            k += 1

def left(i):
    return (2 * i) + 1

def right(i):
    return (2 * i) + 2


def heapifymax(A, n, i):
    l = left(i)
    r = right(i )
    max_ind = i
    if l < n and A[l][0] > A[max_ind][0]:
        max_ind = l
    if r < n and A[r][0] > A[max_ind][0]:
        max_ind = r
    if max_ind != i:
        A[i], A[max_ind] = A[max_ind], A[i]
        heapifymax(A, n, max_ind) 

def build_heap_max(A):
    n = len(A)
    for i in range(n//2,-1,-1):
        heapifymax(A, n, i)
    print(A)

def heap_sort_max(A):
    n = len(A)
    build_heap_max(A)
    for i in range(n-1, 0 ,-1):
        A[0],A[i] = A[i], A[0]
        heapifymax(A, i, 0)
        
        

def contains(T):

    max_in = 0
    i = 0
    catch = 0
    while i < len(T)-1:
        max_tmp = 0
        for j in range(i+1, len(T)):
            if T[i][1] <= T[j][0]:
                break

            if T[i][0] <= T[j][0] and T[i][1] >= T[j][1]:
                max_tmp += 1

            else:
                catch = j

        if max_in < max_tmp:
            max_in = max_tmp
        
        if i < catch:
            i = catch
        else:
            i = j


    return max_in



def sort_przedzialy(tab):
    # quick_sort_stack_range(tab, 0 , len(tab)-1)
    # print(tab)
    merge_sort_cords(tab)

    print(tab)
    result = contains(tab)
    return result


tab = [(1, 5), (2, 8), (1, 6), (7, 8), (2, 7), (2, 4), (8, 9), (3, 4), (1, 5)]
sort_przedzialy(tab)
print(sort_przedzialy(tab))