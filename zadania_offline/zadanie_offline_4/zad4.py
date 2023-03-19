from zad4testy import runtests

def knapsack(T,P):
    n = len(T)
    F = [[0 for b in range(P+1)] for i in range(n)]
    sT = [0]*n
    for i in range(n):
        sT[i] = T[i]
    sT.sort(key = lambda tup: tup[2])

    for i in range(n):

        for j in range(sT[i][3],P+1):

            F[i][j] = sT[i][0]*(sT[i][2]-sT[i][1])

    for i in range(1,n):

        for p in range(sT[i][3],P+1):
                q = p - sT[i][3]
                max_val = 0
                for k in range(i-1,-1,-1):

                    if sT[i][1]  > sT[k][2]:
                        max_val = max(max_val,F[k][q])
                F[i][p] += max_val

    return F, sT

def find_solution(F,T,P,sT):
    q = 0
    S = []
    
    for i in range(len(T)):
        tmp = F[i][P]
        if q < tmp:
            q = tmp
            index = i

    while P > 0 and index >= 0:

        S.append(index)

        too_find = F[index][P] - sT[index][0]*(sT[index][2]-sT[index][1])
        if too_find <= 0:
            break
        P -= sT[index][3]
        i = index
        
        while sT[index][1] <= sT[i][2]:
            i -= 1
            if i < 0:
                break
        while P >= 0 and i >= 0 and F[i][P] != too_find:
            i -= 1
            if i < 0:
                break
        index = i
    
    for i in range(len(S)):

        for j in range(len(T)):

            if T[j] == sT[S[i]]:
                S[i] = j
                break
    return S

def select_buildings(T,p):
    sack ,sT = knapsack(T,p)

    return(find_solution(sack, T,p, sT))






runtests( select_buildings )