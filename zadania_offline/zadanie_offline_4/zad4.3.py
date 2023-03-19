

def memorize(T,P):
    n = len(T)
    F = [[-1 for i in range(P+1)]for j in range(n)]
    p = 0
    sT = [0]*n
    for i in range(n):
        sT[i] = T[i]
    sT.sort(key = lambda tup: tup[2])
    a = sT[n-1][1]
    return solution(sT,P,F,n)


def solution(sT,P,F,n):

    if F[n-1][P] > -1:
        return F[n][P]
    
    if P == 0 or n == 0:
        return 0
    
    if sT[n-1][3] <= P:
        F[n-1][P] = max((sT[n-1][0]*(sT[n-1][2]-sT[n-1][1])) + solution(sT, P - sT[n-1][3], F, n - 1))
    
    elif sT[n-1][3] > P:
        F[n-1][P] = solution(sT, P - sT[n-1][3], F, n - 1)

    return F[n-1][P]


T = [ (2, 1, 5, 3),
(3, 7, 9, 2),
(2, 8, 11, 1) ]
p = 5

memorize(T,p)




    









