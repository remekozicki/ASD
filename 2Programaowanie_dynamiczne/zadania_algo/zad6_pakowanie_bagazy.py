'''
Jedziemy na wakacje, w trip w chuj. Jedziemy na dwie bryki.
Chcemy żeby nasze fury dobrze sie prowadziły na serpentynach, więc chcemy żeby nasze bagaże były rozłożone
nie jednolicie(N/2) do każdego samochodu. czy da się tak zrobić?

łączna waga bagaży N

'''


def zadanie(T):
    n = len(T)
    W = 0
    for i in T:
        W += i
    if W % 2 != 0:
        return False

    DP = [[None for i in range(W+1)] for j in range(n)]
    i = 0
    p = 0
    if 0 == rec(T,DP,W,i,p,n):
        return True
    else: return False



def rec(T,DP,W,i,p,n):

    if i >= n-1:
        return abs((W//2) - p)
    
    if DP[i][p] != None:
        return DP[i][p]
    
    else:

        DP[i][p] = min( rec(T,DP,W,i+1,p+T[i],n),  rec(T,DP,W,i+1,p,n))
        return DP[i][p]

T = [2,1,5,6,1,3]
print(zadanie(T))