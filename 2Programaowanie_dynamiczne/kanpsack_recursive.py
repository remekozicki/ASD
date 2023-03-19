# This is the memoization approach of
# 0 / 1 Knapsack in Python in simple
# we can say recursion + memoization = DP
  
# driver code
val = [60, 100, 120 ]
wt = [10, 20, 30 ]
W = 50
n = len(val)
  
def memorize(wt, val, W):
    n = len(wt)
    t = [[-1 for i in range(W + 1)] for j in range(n + 1)]
    return knapsack(wt, val, W, t,n)
  
  
def knapsack(wt, val, W, t, n):
  
    
    if n == 0 or W == 0:
        return 0
    if t[n][W] != -1:
        return t[n][W]
  
    
    if wt[n-1] <= W:
        t[n][W] = max(val[n-1] + knapsack(wt, val, W-wt[n-1], t,n-1),knapsack(wt, val, W,t, n-1))
        return t[n][W]
    elif wt[n-1] > W:
        t[n][W] = knapsack(wt, val, W,t, n-1)
        return t[n][W]
  
  
print(memorize(wt, val, W))