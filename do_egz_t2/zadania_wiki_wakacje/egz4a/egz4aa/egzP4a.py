from egzP4atesty import runtests 


def bridges(T):
    n = len(T)
    T.sort(key = lambda x: x[1])
    T.sort(key = lambda x: x[0])
    DP = [1 for i in range(n)]

    
    for i in range(1,n):
        for j in range(i):
            if T[i][1] >= T[j][1]:
                DP[i] = max(DP[i], DP[j]+1)
    
    return max(DP)

def binary_sol(T):
    n = len(T)
    T.sort(key = lambda x: x[1])
    T.sort(key = lambda x: x[0])

    tab = []
    tab.append(T[0])

    for i in range(1,n):

        if T[i][1] >= tab[len(tab)-1][1]:
            tab.append(T[i])
        
        else:
            idx = find_idx(tab,T[i][1])
            tab[idx] = T[i]
    
    return len(tab)


def find_idx(tab,x):
    L = 0
    P = len(tab)-1

    while L < P:
        mid = (L+P)//2

        if tab[mid][1] >= x:
            P = mid
        else:
            L = mid +1
    
    return P


def mosty ( T ):
    #tutaj proszę wpisać własną implementację 
    return binary_sol(T)
    

runtests ( mosty, all_tests=True )