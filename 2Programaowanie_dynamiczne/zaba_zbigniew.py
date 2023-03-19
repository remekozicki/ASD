def moemorize(T,V,l,q):
    
    n = len(T)
    DP = [[None for i in range(l+1)]for j in range(n)]
    i = n-1 # kolejna stacja
    m = l - T[n-1]
    
    res = dynamic_frog(T,V,DP,i,m,l,q)
    # return res
    bak = q
    if q < l-T[n-1]:
        return []
    for i in range(1,n):
        bak -= T[i] - T[i-1]
        if bak < 0:
            return []
        bak += V[i]
        if bak > q:
            bak = q
    
    

    i = n-1 # kolejna stacja
    m = l - T[n-1]

    sol = [0]
    m = l - T[n-1]
    while  i > 1:
        w1 = dynamic_frog (T,V,DP,i-1, m + (T[i]-T[i-1]),l,q )
        w2 = dynamic_frog(T,V,DP,i-1, max(m-V[i],0) + (T[i]-T[i-1]),l,q)
        sol.append(min(w1,w2))
        m = T[i] - T[i-1]
        i-=1
    return sorted(sol)



    
def dynamic_frog(T,V,DP,i,m,l,q):
    

    if m > q:
        return float('inf')

    if i == 0:
        # wazne
        if m > V[i]:
            DP[i][m] = float('inf')
        else:
            DP[i][m] = 1
            return 1
    

    if DP[i][m] != None:
        return DP[i][m]
    
    else:

        nie_bierz = dynamic_frog (T,V,DP,i-1, m + (T[i]-T[i-1]),l,q )

        bierz =  dynamic_frog(T,V,DP,i-1, max(m-V[i],0) + (T[i]-T[i-1]),l,q)

        roz = min(  nie_bierz,  bierz ) +1

        DP[i][m] = roz
        return roz
    






T = [0,1,2] # ogległości poszczególych stacji od początku drogi
V = [2,1,5] # ilośc paliwa na poszczególnych stacjach
l = 4 # długość drogi 
q = 2 # pojemnioość baku
# V = [2,1,5,2,5,3]
# T = [0,1,2,4,6,8]
# l = 10
# q = 2       
print(moemorize(T,V,l,q))