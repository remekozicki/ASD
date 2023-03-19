

def King_Falisz(T):
    n = len(T)
    DP = [[None for i in range(n)] for j in range(n)]
    
    DP[0][0] = 0
    
    i = j = n-1
    return rec(T,DP,i,j,n)

def rec(T,DP,i,j,n):

    if DP[i][j] != None:
        return DP[i][j]
    
    else:

        if j-1 >= 0 and i-1 >= 0:
            q = min(  (T[i][j]+rec(T,DP,i-1,j,n)), T[i][j]+ rec(T,DP,i,j-1,n)   )

        elif j-1 < 0:
            q = T[i][j]+ rec(T,DP,i-1,j,n)
        
        elif i-1 < 0:
            q = T[i][j] + rec(T,DP,i,j-1,n)
       
        
    DP[i][j] = q
    return q
        

   

    
    

T = [
    [0, 5, 4, 3],
    [2, 1, 3, 2],
    [8, 2, 5, 1],
    [4, 3, 2, 0]
    ]

print(King_Falisz(T))




