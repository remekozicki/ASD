'''Bucket Sort'''
def insertion_sort(T):

    for i in range(len(T)):
        X = T[i]
        j = i - 1
        while j >= 0 and T[j] > X:
            T[j+1] = T[j]
            j -= 1
        T[j+1] = X

def bucket_sort(A):
    n = len(A)
    B = [[] for _ in range(n+1)]
    div = max(A)
    for i in range(n):
        index = int(A[i] / div * n)
        B[index].append(A[i])
    
    for j in range(len(B)):
        insertion_sort(B[j])

    result = []
    for i in range(len(B)):
        for j in range(len(B[i])):
            result.append(B[i][j])
    return result

    
def bucket_sort_range(A, x, y):
    n = len(A)
    B = [[] for _ in range(n+1)]
    
    for i in range(n):
        index = int((A[i] -x) / (y - x) * n)
        B[index].append(A[i])
    
    for j in range(len(B)):
        insertion_sort(B[j])

    result = []
    for i in range(len(B)):
        for j in range(len(B[i])):
            result.append(B[i][j])
    return result
    
    
    
        
tab = [19.5, 18.2, 18.5, 16.2, 8.4, 19.2, 11.8, 14.3, 5.1, 10.4, 7.8, 6.2, ]
res = bucket_sort_range(tab, 5, 20)
print(res)
        
    








