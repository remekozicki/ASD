from zad3testy import runtests

 # tu prosze wpisac wlasna implementacje

def get_max_min(P):
    min_val = float('inf')
    max_val = 0
    
    for i in range(len(P)):
    
        if P[i][0] < min_val:
            min_val = P[i][0]
    
        if P[i][1] > max_val:
            max_val = P[i][1]
    
    return min_val, max_val

def insertion_sort(T):

    for i in range(len(T)):
        X = T[i]
        j = i - 1
        
        while j >= 0 and T[j] > X:
            T[j+1] = T[j]
            j -= 1
        
        T[j+1] = X


def bucket_sort(A,P):
    n = len(A)
    min_val, max_val = get_max_min(P)
    diff = max_val - min_val
    
    B = [[] for _ in range(diff + 1)]

    for i in range(n):
        index = int(A[i] - min_val)
        B[index].append(A[i])
    
    for j in range(len(B)):
        if len(B[j]) == []:
            continue

        elif len(B[j]) < 500:
            insertion_sort(B[j])

        else:
           B[j] = bucket_sort(B[j])
    
    result = []

    for i in range(len(B)):
        for j in range(len(B[i])):
            result.append(B[i][j])
    
    return result

def SortTab(A,P):
    
    res = bucket_sort(A,P)
    return res
    
runtests( SortTab )