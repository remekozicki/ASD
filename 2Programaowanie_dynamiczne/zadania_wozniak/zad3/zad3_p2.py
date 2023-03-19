from zad3ktesty import runtests



def ksum(T,k):

    n = len(T)

    DP = [None for _ in range(n)]

    minval = float('inf')

    for idx in range(k):

        minval = min(minval, rec(T,k,DP,idx,n))
    
    return minval

def rec(T,k,DP,idx,n):
    
    if idx == n-1:
        return T[idx]

    if idx + k > n-1:
        return T[idx]

    if DP[idx] != None:
        return DP[idx]

    mini = float('inf')
    for i in range(idx+1,idx+k+1):

        mini = min(mini, rec(T,k,DP,i,n) + T[idx])

    DP[idx] = mini
    return mini




def ksuma( T, k ):
    #Tutaj proszę wpisać własną implementację
    return ksum(T,k)
    
runtests ( ksuma )