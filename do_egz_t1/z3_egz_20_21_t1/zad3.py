from zad3testy import runtests

def zadanie (A,k):
    n = len(A)
    DP = [[None for j in range(k+1)] for i in range(n)]
    
    maxi = -1
    for i in range(n):
        a,b = A[i]
        maxi = max(maxi, rec(A,k-1,i,DP,a,b,n))
    
    return maxi

def rec(A,k,idx,DP,a,b,n):
   
    if k == 0:
        DP[idx][k] = b-a
        return b-a
    
    if idx == n:
        return 0
    
    if DP[idx][k] != None:
        return DP[idx][k]


    maxi = -1
    
    for i in range(idx+1, n):

        if A[i][0] <= a and A[i][1] >= b:
            maxi = max(maxi, rec(A,k-1,i,DP,a,b,n))
            
        elif  A[i][0] > a and A[i][1] < b:
            maxi = max(maxi, rec(A,k-1,i,DP,A[i][0],A[i][1],n))

        elif A[i][0] > a and A[i][0] < b:
            maxi = max(maxi, rec(A,k-1,i,DP,A[i][0],b,n))

        elif A[i][1] < b and A[i][1] > a:
            maxi = max(maxi, rec(A,k-1,i,DP,a,A[i][1],n))
    
    DP[idx][k] = maxi
    return maxi
    
def kintersect( A, k ):
  """Miejsce na Twoją implementację"""
  print("remek",zadanie (A,k))
  return []

runtests( kintersect )