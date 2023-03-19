

def get_max_min(A):
    min_l = float('inf')
    max_l = 0
    
    for i in range(len(A)):
        max_l = max(max_l,len(A[i]))
        min_l = min(min_l,len(A[i]))

    return max_l, min_l

def radix_string(A):
    n = len(A)
    x = len(A[0])

    for k in range(x-1,-1,-1):
        C = [0] * 26
        B = [0] * n

        for i in range(n):
            C[ord(A[i][k]) - 97] += 1
        
        for i in range(1,26):
            C[i] = C[i] + C[i - 1]

        for i in range(n):
            B[ C[ ord(A[i][k]) - 97] - 1] = A[i]
            C[ ord(A[i][k]) - 97] -= 1
        
        A = B
    
    return A

def buckets(A):
    n = len(A)
    max_val, min_val = get_max_min(A)

    diff = max_val - min_val

    B = [[] for i in range(diff + 1)]

    for i in range(n):
        index = int(len(A[i]) - min_val)
        B[index].append(A[i])

    for i in range(len(B)):
        if B[i] != []:
           B[i] = radix_string(B[i])
    
    A = B

    for i in range(1,len(B)):
        A[0] = merge(A[0],A[i])
    
    return A[0]

def merge(L,R):
    
    i = j = k =0
    res = [0] * (len(L) + len(R))
    while i < len(L) and j < len(R):
        x = 0
        while L[i][x] == R[j][x]:
            x += 1
        if L[i][x] < R[j][x]:
            res[k] = L[i]
            i += 1
        else:
            res[k] = R[j]
            j += 1
        k+=1
    while len(L) > i:
        res[k] = L[i]
        i += 1
        k += 1
    while len(R) > j:
        res[k] = R[j]
        j += 1
        k += 1
    
    return res

     
        



tab = ['ala','ul','kasia', 'piotrek','radek', 'gruby','ola', 'natalia','grzes','qn']
print(buckets(tab))






