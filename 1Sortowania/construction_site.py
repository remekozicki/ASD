

def get_max_min(T):
    mini = float('inf')
    maxi = -1

    for i in range(len(T)):
        maxi = max(maxi,len(T[i]))
        mini = min(mini,len(T[i]))
    
    return maxi, mini

def radix_sort(A):
    k = len(A[0])
    n = len(A)

    for j in range(k-1,-1,-1):
        C = [0 for _ in range(26)]
        B = [None for _ in range(n)]

        for i in range(n):
            C[ord(A[i][j]) - 97] += 1
        
        for i in range(1,26):
            C[i] += C[i-1]

        for i in range(n-1,-1,-1):
            B[C[ord(A[i][j])-97]-1] = A[i]
            C[ord(A[i][j])-97] -= 1
        
        A = B
    
    return A
        

def merge(L,R):
    l = r = 0
    res = []
    while l < len(L) and r < len(R):
        idx = 0

        while L[l][idx] == R[r][idx]:
            idx += 1
        
        if L[l][idx] < R[r][idx]:
            res.append(L[l])
            l += 1
        
        else:
            res.append(R[r])
            r += 1
    
    while l < len(L):
            res.append(L[l])
            l += 1
        
    while r < len(R):
            res.append(R[r])
            r += 1
    
    return res
        
    


def buckets(T):
    n = len(T)

    maxi, mini = get_max_min(T)
    diff = maxi - mini
    B = [[] for i in range(diff+1)]

    for i in range(n):
        idx = len(T[i]) - mini
        B[idx].append(T[i])
    
    for i in range(len(B)):
        if B[i] != []:
            B[i] = radix_sort(B[i])

    
    for i in range(1,len(B)):
        if B[i] != []:
            B[0] = merge(B[0],B[i])
    return B[0]




tab = ['ala','ul','kasia', 'piotrek','radek', 'gruby','ola', 'natalia','grzes','qn']
print(buckets(tab))