

def memorize(T):
    n = len(T)
    S = 0
    for i in range(n):
        S += T[i]
    
    DP = [[None for i in range(S)]for j in range(n)]
    
    i = 0
    p1 = p2 = 0
    res = rec(T,DP,S,p1,p2,i,n)

    return res

def rec(T,DP,S,i,p1,p2,n):
    
    if i >= n:
        return abs(p1 - p2)

    if DP[i][p1] != None:
        return DP[i][p1]
    
    else:

        q = min( rec(T,DP,S,p1 + T[i],p2,i+1,n),  rec(T,DP,S,p1,p2 + T[i ],i+1,n))
        DP[i][p1] = q
        return q







T = [1,6,5,11]

print(memorize(T))