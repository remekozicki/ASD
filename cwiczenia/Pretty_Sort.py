

def how_pretty(X):
    num = X
    A = [0]*10
    while X > 0:
        A[X % 10] += 1
        X //= 10

    single = 0
    multi = 0
    
    for i in range(len(A)):
        if A[i] == 1:
            single += 1
        elif A[i] > 1:
            multi += 1    
    return [num, single, multi]

def merge_sort(T):
    if len(T) > 1:
        mid = len(T) // 2
        L = T[:mid]
        R = T[mid:]
        
        merge_sort(L)

        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i][1] > R[j][1] or (L[i][1] == R[j][1] and L[i][2] <= R[j][2] ):
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

def pretty_sort(T):

    for i in range(len(T)):
        T[i] = how_pretty(T[i])
    merge_sort(T)

    # for i in range(len(T)):
    #     T[i] = T[i][0]
    

tab = [123, 455, 1266, 114577, 2344, 67333]
pretty_sort(tab)
print(tab)
    

    
