'''Radix Sort'''

def radix_sort(A,d):
    for k in range(1, d+1):
        
        power_10 = 1*(10**(k-1))
        C = [0]*10
        B = [0]*len(A)
        
        for i in range(len(A)):
            C[(A[i] % 10**k) // power_10] += 1
        
        for i in range(1,10):
            C[i] = C[i-1] + C[i]
        
        for j in range(len(A)-1,-1,-1):
            B[C[(A[j] % 10**k) // power_10] - 1] = A[j]
            C[(A[j] % 10**k) // power_10] = C[(A[j] % 10**k) // power_10] - 1
        
        A = B
    
    return A






tab  = [329,457,657,839,436,720,355]
res = radix_sort(tab,3)
print(res)