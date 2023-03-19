'''problem plecakowy'''
# w wagi
# P ceny
# max waga B

def knapsack(W,P,B):
    n = len(W)
    F = [[0 for b in range(B+1)] for i in range(n)]
    
    
    for b in range(W[0],B+1):
        F[0][b] = P[0]
       
    for b in range(B+1):
      
        for i in range(1,n):
            F[i][b] = F[i-1][b]

            if b-W[i] >= 0:
                tmp = F[i-1][b-W[i]] +P[i]
                if F[i][b] < tmp:
                    F[i][b] = tmp

    
    
    return F

def print_solution(F,B,W):
    n = len(F) -1 
    S =[]
    while n > 0:
        if F[n][B] != F[n-1][B]:
            S.append(n)
            B -= W[n]
        n -= 1
    if B >= W[n]:
        S.append(n)
    return S




tab_w = [5,   10,  15,  8,  6,  15,  11]
tab_p = [60,  100,  120, 80,  30,  50,  100]
cap = 26
Sack = knapsack(tab_w,tab_p,cap)

print(Sack[len(tab_w)-1][cap])
print(print_solution(Sack,cap,tab_w))
