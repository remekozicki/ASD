# This is the memoization approach of
# 0 / 1 Knapsack in Python in simple
# we can say recursion + memoization = DP
  
# driver code

def memorize(wt, val, W):
    n = len(wt)
    DP = [[-1 for i in range(W + 1)] for j in range(n)]
    leftw = W
    
    maxi = -1
    for i in range(n):
        if leftw - wt[i] >= 0:
            maxi = max(maxi, rec(wt, val, W, leftw, DP, n, i) )

    return maxi
  
  
def rec(wt, val, W, leftw ,DP, n,idx):
  
    
    if idx == n-1:
        if leftw - wt[idx] >= 0:
            DP[idx][leftw] = val[idx]
            return val[idx]
        else:
            DP[idx][leftw] = 0
            return 0

    
    if DP[idx][leftw] != -1:
        return DP[idx][leftw]
    maxi = -1
    
    for i in range(idx+1, n):
        if leftw - wt[i] >= 0:
            maxi = max(maxi,rec(wt, val, W, leftw - wt[idx], DP, n, i) )

    DP[idx][leftw] = maxi + val[idx]
    return DP[idx][leftw]
        
    
val = [60, 100, 120 ]
wt = [10, 20, 30 ]
W = 50

  
print(memorize(wt, val, W))