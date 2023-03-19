from zad3ktesty import runtests



def memorize(T,k):
    
    n = len(T)
    DP = [None for i in range(n)]
    min_val = float('inf')
    
    for i in range(n-k,n):

        min_val = min(min_val, rec(T,DP,i,k))
       
    return min_val

    # return rec(T,DP,0,k)

def rec(T,DP,i,k):

    if DP[i] != None:
        return DP[i]

    if i < k:
        return T[i]
    
    else:
        min_val = float('inf')
        
        for j in range(i-k, i):
            min_val= min( min_val, rec(T,DP,j,k) +T[i] ) 
        
        DP[i] = min_val

        return DP[i]






def ksuma( T, k ):
    #Tutaj proszę wpisać własną implementację
    return memorize(T,k)
    
runtests ( ksuma )