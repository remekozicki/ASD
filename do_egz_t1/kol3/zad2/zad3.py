from zad3testy import runtests
from zad3EK    import edmonds_karp

def warshal(T):
    n = len(T)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                T[i][j] = min(T[i][j], T[i][k] + T[k][j])


def zadanie(T,K,D):
    n = len(T)
    for i in range(n):
        for j in range(n):
            if i != j and T[i][j] == 0:
                T[i][j] = float('inf')
    
    warshal(T)
    for i in range(n):
        for j in range(n):
            if T[i][j] < D:
                T[i][j] = 0
            elif  K[i] == 'G' and K[j] == 'B':
                T[i][j] = 1
            else:
                T[i][j] = 0
    t1 = [0 for i in range(n+2)]
    t2 = [0 for i in range(n+2)]

    T.append(t1)
    T.append(t2)

    for i in range(n):
        T[i].append(0)
        T[i].append(0)


    for i in range(n):
        if K[i] == 'G':
            T[n][i] = 1
        else:
            T[i][n+1] = 1
    res = edmonds_karp(T,n,n+1)
    return res


def BlueAndGreen(T, K, D):
    # tu prosze wpisac wlasna implementacje
    return zadanie(T,K,D)

runtests( BlueAndGreen ) 

