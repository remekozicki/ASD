
def sumy(u,v):
    x_u,y_u = u
    x_v,y_v = v
    if y_u < x_v or y_v < x_u:
        a = b = 0
    
    elif x_u <= x_v:
        if y_u <= y_v:
            a = x_v
            b = y_u
        elif y_u > y_v:
            a = x_v
            b = y_v
    
    elif x_u > x_v:
        if y_u <= y_v:
            a = x_u
            b = y_u
        elif y_u > y_v:
            a = x_u
            b = y_v
    
    return a,b


def zadanie(A,k):

    CP = []
    n = len(A)
    for i, x, in enumerate(A):
        CP.append([x[0],x[1],i])
    

    DP = [[None for i in range(k+1)] for j in range(n)]
    idx = 0

    a,b = rec(A,k,CP,DP,idx,n)
    maxi = b-a
    return maxi


def rec(A,k,CP,DP,idx,n):

    if k == 0:
        return A[idx]

    if n-k-1 > idx:
        return (0,0)
    
    if DP[idx][k] != None:
        return DP[idx][k]

    maxdiff = 0
    maxrange = (0,0)

    for i in range(idx+1,n):
        inter = sumy(A[i],rec(A,k-1,CP,DP,i,n))

        if inter[1] - inter[0] > maxdiff:
            maxdiff = inter[1] - inter[0]
            maxrange = inter
    
    DP[idx][k] = maxrange
    return maxrange


    



A = [(0,4),(1,10),(6,7),(2,8)]
k = 3

print(zadanie(A,k))