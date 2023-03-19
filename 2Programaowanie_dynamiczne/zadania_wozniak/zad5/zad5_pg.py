


def garek(T):
    n = len(T)
    DP = [[None for i in range(n)]for j in range(n)]
    
    a = 0
    b = n-1
    
    res = rec(T,DP, a, b,n)
    return res[0]

def rec(T,DP,a,b,n) :

    if DP[a][b] != None:
        return DP[a][b]
    if a == b:
        return [T[a],0]
    if a+1 == b:
        return [max(T[a],T[b]),min(T[a],T[b])]
    
    else:

        if T[a] + rec(T,DP,a+1,b,n)[1] >  T[b] + rec(T,DP,a,b-1,n)[1]:
            q = [T[a] + rec(T,DP,a+1,b,n)[1],rec(T,DP,a+1,b,n)[0]]
        else:
            q = [T[b] + rec(T,DP,a,b-1,n)[1],rec(T,DP,a,b-1,n)[0]]
    
    DP[a][b] = q
    return q

  


T = [8, 15, 3, 7]

print(garek(T))