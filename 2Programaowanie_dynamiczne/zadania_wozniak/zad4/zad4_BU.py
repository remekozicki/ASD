

def King_Falisz(T):

    n = len(T)

    DP = [[None for i in range(n)]for j in range(n)]
    DP[0][0] = 0

    for i in range(0,n):
        
        for j in range(0,n):
            if i == j == 0:
                continue
            
            p = q = float('inf')
            
            if j-1 >=0 :
                q = T[i][j] + DP[i][j-1]
            if i-1 >= 0:
                p = T[i][j] + DP[i-1][j] 

            DP[i][j] = min(q,p)
    
    return DP[n-1][n-1]

            









T = [
    [0, 5, 4, 3],
    [2, 1, 3, 2],
    [8, 2, 5, 1],
    [4, 3, 2, 0]
    ]

print(King_Falisz(T))
