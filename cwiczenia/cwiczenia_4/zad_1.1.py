'''algorytm sortujący n-elementową tablice z liczbami z zakresu {0,...,n^2-1}'''

from tkinter import N


def to_sysytem(X,n):
    
    new_X = [0,0]
    i = 1
    while X > 0:
        new_X[i] = X % n
        X //= n
        i -= 1
    return new_X

def radix_i_chuj(A):
    
    n = len(A)

    for k in range(1,-1,-1):

        C = [0]*n
        B = [0]*n

        for i in range(n):
            val = to_sysytem(A[i],n)
            B[val[k]] += 1
        
        
        for i in range(1,n):
            B[i] = B[i-1] + B[i]

        for i in range(n-1,-1,-1):
            val = to_sysytem(A[i],n)
            C[B[val[k]]-1] = A[i]
            B[val[k]] -= 1
        A = C
    return A


tab = [54, 23, 74, 21, 24, 9, 21, 56, 86, 91, 120, 32, 53]

print(radix_i_chuj(tab))
