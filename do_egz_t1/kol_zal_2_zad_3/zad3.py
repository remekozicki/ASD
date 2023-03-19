from zad3testy import runtests


def zadanie(T,V,q,l):

    T.append(l)
    V.append(0)
    n = len(T)

    DP = [[None for i in range(q+1)] for i in range(n)]

    for i in range(n-1):
        if T[i+1] - T[i] > q:
            return []

    b = 0 # stan baku
    idx = 0 
    rec(T,V,DP,idx,l,q,n,b)

    b = 0
    idx = 0
    res = []
    while idx < n-1:
        dis = T[idx+1] - T[idx]
        
        if dis > b:
            res.append(idx)
            if b + V[idx] >= q:
                b = q
        
            else:
                b = b + V[idx]
            b -= dis
        
        else:
            if b + V[idx] >= q:
                b_n = q
                w1 = rec(T,V,DP,idx+1,l,q,n,q-dis) +1
        
            else:
                b_n = b + V[idx]
                w1 = rec(T,V,DP,idx+1,l,q,n,b_n-dis) +1
        
            w2 = rec(T,V,DP,idx+1,l,q,n,b-dis)

            if w2 > w1:
                res.append(idx)
                b = b_n - dis
            else:
                b -= dis
        idx += 1
    return res
                


  

def rec(T,V,DP,idx,l,q,n,b):

    if b < 0:
        return float('inf')
    
    if idx == n-1:
        return 0
    
    if DP[idx][b] != None:
        return DP[idx][b]

    dis = T[idx+1] - T[idx]

    # musze tankowac

    if dis > b:
        if b + V[idx] >= q:
           w1 = rec(T,V,DP,idx+1,l,q,n,q-dis) +1
        
        else:
            b_n = b + V[idx]
            w1 = rec(T,V,DP,idx+1,l,q,n,b_n-dis) +1
        
        DP[idx][b] = w1
        return w1
    
    # tankuje ale nie musze
    else:
        if b + V[idx] >= q:
           w1 = rec(T,V,DP,idx+1,l,q,n,q-dis) +1
        
        else:
            b_n = b + V[idx]
            w1 = rec(T,V,DP,idx+1,l,q,n,b_n-dis) +1
        
        #  nie tankuje lub 
        w2 = rec(T,V,DP,idx+1,l,q,n,b-dis)
    
    DP[idx][b] = min(w1,w2)
    return DP[idx][b]





def iamlate(T, V, q, l):
    """tu prosze wpisac wlasna implementacje"""
  
    return zadanie(T,V,q,l)


runtests( iamlate )
