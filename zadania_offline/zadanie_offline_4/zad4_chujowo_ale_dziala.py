
from zad4testy import runtests


def memorize(T,p):

    n = len(T)

    DP = [[None for i in range(p+1)] for j in range(n+1)]


    T_s = []

    for i in range(n):
        T_s.append(T[i])
    
    T_s.sort(key = lambda x: x[2])

    i = n 

    res = fuc(T_s,DP,p,i)
   
    i = n

    sol = []

    while i > 0:
        
        if T_s[i-1][3] <= p:
            
            capacity_i = T_s[i-1][0] * ( T_s[i-1][2] - T_s[i-1][1] )
            
            w1 = fuc(T_s,DP,p,i-1)
            w2 = capacity_i + fuc(T_s,DP,p - T_s[i-1][3],prev(T_s,i-1))

            if w1 < w2:
                p -= T[i-1][3]
                sol.append(i-1)
                i = prev(T_s,i-1)
            else:
                i-=1
        
        else:
            i-=1
    
    big_sol = []
    
    for i in sol:
        
        for j in range(n):
            if T[j] == T_s[i]:
                big_sol.append(j)

    big_sol.sort()
    
    return big_sol

def prev(T_s,i):
    j = i
    while j >= 0 and T_s[i][1] <= T_s[j][2]:
        j -= 1
    return j + 1

def fuc(T_s,DP,p,i):

    if i == 0 or p == 0:
        return 0
    
    if DP[i][p] != None:
        return DP[i][p]
    
    # j = i - 1
    # while j >= 0 and T_s[i-1][1] <= T_s[j][2]:
    #     j -= 1
    # j+=1
   
    
    capacity_i = T_s[i-1][0] * ( T_s[i-1][2] - T_s[i-1][1] )

    if T_s[i-1][3] <= p:
        DP[i][p] = max( fuc(T_s,DP,p,i-1), capacity_i + fuc(T_s,DP,p - T_s[i-1][3], prev(T_s,i-1)) )
        return DP[i][p]
    
    elif T_s[i-1][3] > p:
        DP[i][p] = fuc(T_s,DP,p,i-1)
        return DP[i][p]


def select_buildings(T,p):
    

    return memorize(T,p)

runtests( select_buildings )

