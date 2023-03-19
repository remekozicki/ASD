
def load(P,DP,l1,l2,n,i):

    if i > n-1:
        return 0

    if DP[i][l1][l2] != None:
        return DP[i][l1][l2]
    
    if l1 < P[i] and l2 < P[i]:
        DP[i][l1][l2]
        return 0
    
    if l1 < P[i]:
        DP[i][l1][l2] = load(P,DP,l1,l2 - P[i], n ,i+1)
    
    if l2 < P[i]:
         DP[i][l1][l2] = load(P,DP,l1 - P[i],l2,n, i+1)
    
    else:
        w1= load(P,DP,l1 - P[i],l2,n, i+1)
        w2= load(P,DP,l1,l2 - P[i],n, i+1)
        # DP[i][l1][l2] = max( load(P,DP,l1,l2 - P[i],n, i+1) ,  load(P,DP,l1 - P[i],l2,n, i+1) ) + 1 
        DP[i][l1][l2] = max( w1 ,  w2 ) + 1 

    return DP[i][l1][l2]

def ferry(P,l1,l2):
    n = len(P)
    DP = [[[None for i in range(l2+1)]for j in range(l1+1)]for k in range(n)]
    # i = 0
    res = load(P,DP,l1,l2,n,0)
    i = 0
    n = len(P)
    sol1 = []
    sol2 = []

    while i < n and (l1 >= P[i] or l2 >= P[i]):
        if P[i] > l1: 
            w1 = 0
            w2 = 1
        
        elif P[i] > l2:
            w1 = 1
            w2 = 0
        
        else:
            w1 = load(P,DP,l1 - P[i],l2,n, i+1)
            w2 = load(P,DP,l1,l2 - P[i],n, i+1)
        
        if w1 > w2:
            sol1.append(i)
            l1 -= P[i]
        else:
            sol2.append(i)
            l2 -= P[i]
        i += 1
    
    if res - 1 in sol1:
        return sol1
    else:
        return sol2










T = [5, 6, 1, 3, 2, 4, 3, 5]
l1 = 8
l2 = 10

print(ferry(T,l1,l2))