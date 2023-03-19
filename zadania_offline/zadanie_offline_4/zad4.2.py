def fuc(T_s,DP,p,i):

    if i == 0 or p == 0:
        return 0
    
    if DP[i][p] != None:
        return DP[i][p]
    
    j = i - 1
    while j >= 0 and T_s[i-1][1] <= T_s[j][2]:
        j -= 1
    j+=1
    
    capacity_i = T_s[i-1][0] * ( T_s[i-1][2] - T_s[i-1][1] )

    if T_s[i-1][3] <= p:
        DP[i][p] = max( fuc(T_s,DP,p,i-1), capacity_i + fuc(T_s,DP,p - T_s[i-1][3],j) )
        return DP[i][p]
    
    elif T_s[i-1][3] > p:
        DP[i][p] = fuc(T_s,DP,p,i-1)
        return DP[i][p]

def memorize(T,p):

    n = len(T)

    DP = [[None for i in range(p+1)] for j in range(n+1)]


    T_s = []

    for i in range(n):
        T_s.append(T[i])
    
    T_s.sort(key = lambda x: x[2])

    i = n 

    res = fuc(T_s,DP,p,i)
   
    i = len(T)

    sol = []

    while i > 0:
        
        if T_s[i-1][3] <= p:
            
            j = i - 1
            while j >= 0 and T_s[i-1][1] <= T_s[j][2]:
                j -= 1
            j+=1
            
            capacity_i = T_s[i-1][0] * ( T_s[i-1][2] - T_s[i-1][1] )
            
            w1 = fuc(T_s,DP,p,i-1)
            w2 = capacity_i + fuc(T_s,DP,p - T_s[i-1][3],j)

            if w1 > w2:
                i-=1
            else:
                p -= T[i-1][3]
                sol.append(i-1)
                i = j
        else:
            i-=1
    
    big_sol = []
    for i in sol:
        j = n - 1
        while j >= 0 and T_s[i] != T[j]:
            j-=1
        if j < 0:
            continue
        else:
            big_sol.append(j)
    big_sol.sort()
    return big_sol



T = [ (2, 1, 5, 3),
(3, 7, 9, 2),
(2, 8, 11, 1) ]
p = 5
memorize(T,p)