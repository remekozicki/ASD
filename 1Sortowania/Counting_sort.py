'''Counting Sort'''


def counting_sort(A,k):
    C = [0]*(k+1)
    B = [0]*len(A)
    
    for i in range(len(A)):
        C[A[i]] += 1
    
    for i in range(1,k+1):
        C[i] = C[i-1] + C[i]
    
    for j in range(len(A)-1,-1,-1):
        B[C[A[j]] - 1] = A[j]
        C[A[j]] = C[A[j]] - 1
    
    return B









def counting2(T,k):
    n = len(T)
    C = [0 for i in range(k+1)]
    B = [0 for i in range(n)]

    for i in range(n):
        C[T[i]] += 1

    for i in range(1, k+1):
        C[i] += C[i-1]

    for i in range(n):

        B[C[T[i]]-1] = T[i]
        C[T[i]] -= 1 

    return B 
    


tab = [2,0,4,4,0,1,2,2,1,1,3]
print(counting_sort(tab,4))
print(counting2(tab,4))