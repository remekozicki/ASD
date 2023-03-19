def binary_search(A,x):
    n = len(A)

    L = 0
    R = n - 1

    while L <= R:
        mid = (L+R) // 2

        if A[mid] == x:
            return mid

        if A[mid] > x:
            R = mid - 1
        
        else:
            L = mid +1 
    else:
        return False
            
tab = [2,1,4,3,6,5,7,8]
print(binary_search(tab,0))