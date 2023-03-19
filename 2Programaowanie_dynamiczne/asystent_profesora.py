def asystent(T):
    n = len(T)
    F = [[0 for i in range(n)]for i in range(n)]
    pre_sum = [0]*n
    pre_sum[0] = T[0]
    for i in range(1,n):
        pre_sum[i] = pre_sum[i-1]+T[i]
    
    for i in range(n-1):
        F[i][i+1] = abs(T[i]+T[i+1])
    
    for l in range(2,n):
        for i in range(n-l+1):
            j = i+l
            if j >= n:
                break
            else:
                w = min(F[i][j-1],F[i+1][j])
                F[i][j] = max( abs(pre_sum[n-1]) , w)

    return F[0][n-1]

T = [1,-5,2,-1]
print(asystent(T))