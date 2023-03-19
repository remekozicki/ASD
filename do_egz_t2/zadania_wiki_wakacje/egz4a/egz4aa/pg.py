def bridges(T):
    n = len(T)
    T.sort(key = lambda x: x[1])
    T.sort(key = lambda x: x[0])
    DP = [None for i in range(n)]
    count = 0
    idx = -1
    B = -1
    res = rec(T,DP,n,idx,B,count)
    return res

def rec(T,DP,n,idx,B,count):

    if idx >= n-1:
        return count
    
    if DP[idx] != None:
        return DP[idx]
    
    else:
        maxi = -1
        for i in range(idx+1,n):
            if T[i][1] >= B:
                maxi = max(maxi,rec(T,DP,n,i,T[i][1],count+1),rec(T,DP,n,i,B,count))
            else:
                maxi = max(maxi,rec(T,DP,n,i,B,count))
        DP[idx] = maxi
        return DP[idx]

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

T = [(8, 1), (1, 2), (4, 3), (3, 4), (5, 5), (2, 6), (6, 7), (7, 8)]

print(binary_sol(T))