# mamy podaną tablice matrioszek. Każda ma wysokość (X) i szerokość (Y). Matrioszkę można włożyć w drugą, 
# jeżeli ma zaróno X i Y miejsze od wcześniejszej.
# Jaki jest najdłuższy ciąg matrioszek jakie można w siebie włożyc?


def LIS(T):
    n = len(T)
    F = [1 for i in range(n)]

    for i in range(n):
        for j in range(i):

            if T[i] > T[j]:

                F[i] = max(F[i],F[j]+1)
    return max(F)

def matrioszka(T):

    T.sort(key = lambda x: x[1])
    return LIS(T)



T = [[2,100],[20,30],[19,20],[1,99],[100,1],[10,15],[40,31]]

print(matrioszka(T))