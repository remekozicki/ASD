
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



def counting_sort_multi(A):
    n = len(A)
    k = 2
    B = [0] * 10
    
    for i in range(n):
        B[A[i][k]] += 1
    
    for i in range(1,10):
        B[i] = B[i-1] + B[i]

    C = [0] * n

    for i in range(n):
        C[ B[ A[i][k]] -1 ] = A[i]
        B[ A[i][k]] -= 1
    
    return C

def counting_sort_sing(A):
    n = len(A)
    k = 1
    B = [0] * 10
    
    for i in range(n):
        B[A[i][k]] += 1
    
    for i in range(1,10):
        B[i] = B[i-1] + B[i]

    C = [0] * n

    for i in range(n):
        C[-B[ A[i][k] ]] = A[i]
        B[ A[i][k]] -= 1
    
    return C
    
def pretty_sort(T):

    for i in range(len(T)):
        T[i] = how_pretty(T[i])
    T = counting_sort_multi(T)
    T = counting_sort_sing(T)

    # for i in range(len(T)):
    #     T[i] = T[i][0]
    
    return T
    

tab = [123, 455, 1266, 114577, 2344, 67333]
tab = pretty_sort(tab)
print(tab)
    

    
