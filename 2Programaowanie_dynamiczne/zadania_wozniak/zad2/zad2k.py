from zad2ktesty import runtests


def memorize(T):

    n = len(T)

    DP = [[None for i in range(n)] for j in range(n)]
    max_pali_len = 0

    for a in range(n):
        for b in range(a+1,n):
            # max_pali_len = max(max_pali_len, rec(T,DP,a,b))

            if max_pali_len < rec(T,DP,a,b):
                max_pali_len = rec(T,DP,a,b)
                best_a = a
                best_b = b
    sol = ''
    for i in range(best_a, best_b+1):
        sol += T[i]
    
    return sol
        
def rec(T,DP,a,b):

    if DP[a][b] != None:
        return DP[a][b]

    if a == b:
        return 1
    
    if a+1 == b:
        if T[a] == T[b]:
            return 2
        else:
            return 0
      
    else:
        if T[a] == T[b]:
            tmp = rec(T,DP,a+1,b-1)
            if tmp != 0:
                DP[a][b] = tmp +2

                return DP[a][b]

        return 0  


def palindrom( S ):
    #Tutaj proszę wpisać własną implementację
    return memorize(S)

runtests ( palindrom )