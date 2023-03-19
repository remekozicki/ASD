

def sorting(O,C):
    n = len(O)
    trasa = [[0,0] for i in range(n)]
    for i in range(n):
        trasa[i][0],trasa[i][1] = O[i], C[i]
    trasa.sort(key = lambda x: x[0])
    O2 = []
    C2 = []
    for i in range(n):
        O2.append(trasa[i][0])
        C2.append(trasa[i][1])
    
    return O2, C2






def zadanie(O,C,T,L):
    O,C = sorting(O,C)
    n = len(O)
    DP = [[None, None] for j in range(n)]

    warunek = 1

    for idx in range(n):
        return rec(O,C,T,L,warunek,idx,n,DP)


def rec(O,C,T,L,warunek,idx,n,DP):

    if O[idx] >= L:
        DP[idx][warunek] = 0
        return 0

    if (O[idx] + T >= L) or (warunek and O[idx] + T*2 >= L):
        DP[idx][warunek] = C[idx]
        return C[idx] 
    
    mini = float('inf')
    
    for i in range(idx+1, n):
        
        if O[i] - O[idx] <= T:
            mini = min(mini, rec(O,C,T,L,warunek,i,n,DP))
        
        elif O[i] - O[idx] <= 2*T and warunek:
            mini = min(mini, rec(O,C,T,L,0,i,n,DP))
        
        else:
            break
    
    DP[idx][warunek] = mini + C[idx]
    return mini + C[idx]





O = [17,20,11,5,12]
C = [9,7,7,7,3]
T = 7
L = 25

print(zadanie(O,C,T,L))