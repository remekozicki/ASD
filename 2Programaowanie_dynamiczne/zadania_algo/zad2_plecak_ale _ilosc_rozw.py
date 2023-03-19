

def memo(T,W_T,W,C_min):

    n = len(T)
 
    DP = [[[None for k in range(C_min)]for j in range(W+1)]for i in range(n+1)]

    i = n-1
    C = C_min
    return rec(T,W_T,DP,W,C_min,C,i,n)


def rec(T,W_T,DP,W,C_min,C,i,n):

    if i < 0:
        return 0
    
    elif DP[n][W][C] != None:
        return DP[n][W][C]
    
    elif C <= 0:
        return 1
    else:
        return C
    
    
    




T_val = [60, 100, 120, 40]
W_T = [10, 20, 30, 30 ]
W = 50
C_min = 100
