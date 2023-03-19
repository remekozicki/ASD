

'''
Remigiusz Kozicki
próbowałem podejść do problemyu dynamicznie. Uzzleżnić fukncje od ubiegającego czasu a zarazem
topniejąceg śniegu. skorzystralem z podpowiedzi wchodze tylko bramą zachodniav (dla tablicy w przykładzie zadanie daje taki sam wynik
jak gdzy zmieniamy wjazdy) 
zlożonośc zapewne N^2

program niestety przechodzi tylko 1 test aczkolwiek czuje że jestem blisko rozwiązania :(

'''



from egz1atesty import runtests



def zadanie(S):
    n = len(S)
    days = -1
    for i in range(n):
        days = max(days,S[i])
    
    DP = [[None for _ in range(days+1)] for _ in range(n)]

    # jade tylko z zachodu
    
    res = -1
    for i in range(n):
       
        S_cp = [S[k] for k in range(n)]
        for j in range(i):
            S_cp[j] = 0
        if S_cp[i] != 0:
            w = rec(S_cp,DP,i,n,days,days)
            res = max(res,w)
    
    return res

def rec(S,DP,idx,n,days,dleft):

    if dleft == 0:
        
        return 0
    
    if idx < n-1 and S[idx] == 0:
        rec(S,DP,idx+1,n,days,dleft)
    
    if DP[idx][dleft] != None:
        return DP[idx][dleft]
    
    maxi = 0
    val = S[idx] - (days - dleft)
    if val < 0:
        val = 0
    for i in range(idx+1,n):
        
        maxi = max(maxi,rec(S,DP,i,n,days,dleft-1))
    
    DP[idx][dleft] = maxi + val         
    return DP[idx][dleft]
        

def snow( S ):
    # tu prosze wpisac wlasna implementacje
    return zadanie(S)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = False )
