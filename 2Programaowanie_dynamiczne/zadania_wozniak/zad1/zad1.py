

from zad1ktesty import runtests

def val(x):
    if x == '1':
         return -1
    else:
        return 1
        
def memorize(T):
    n = len(T)
    DP = [[None for i in range(n)] for j in range(n)]
    max_val = -1 
    for a in range(n):
        for b in range(a+1,n):
            max_val = max(max_val,problem(T, DP, a ,b )) 
    return max_val

def problem(T, DP, a, b ):
    n = len(T)
    
    if a == b:
        return val(T[a])
    
    if DP[a][b] != None:
        return DP[a][b]
    
    else:
        
        DP[a][b] = problem(T,DP,a,b-1) + val(T[b])

        return DP[a][b]

def roznica( S ):
    
    return memorize(S)

runtests ( roznica )