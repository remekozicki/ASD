from zad11ktesty import runtests

def memorize(T):
    n = len(T)
    S = 0
    for i in range(n):
        S += T[i]
    
    DP = [[None for i in range(S+1)]for j in range(n)]
    
    i = 0
    p =0 
    res = rec(T,DP,S,p,i,n)

    return res

def rec(T,DP,S,p,i,n):
    
    if i == n-1:
        return abs(p - (S-p))

    if DP[i][p] != None:
        return DP[i][p]
    
    else:

        q = min( rec(T,DP,S,p + T[i],i+1,n),  rec(T,DP,S,p,i+1,n))
        DP[i][p] = q
        return q




def kontenerowiec(T):
    #Tutaj proszę wpisać własną implementację

    return memorize(T)

runtests ( kontenerowiec )
    