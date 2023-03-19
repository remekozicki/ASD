def partition(A,p,r):
    X = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= X:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def select(A, k, p, r):
    if p == r:
        return A[p]
    
    if p < r:
        q = partition(A,p,r)
        if q == k:
            return A[q]
        elif q < k:
            return select(A, k, q + 1, r)
        else:
            return select(A, k, p, q - 1)


tab = [2,1,5,6,7,3,6,9,5,10]

print(select(tab,1,0,len(tab)-1))