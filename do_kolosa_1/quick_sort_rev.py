


def partition(A, p, r):
    x = A[r]
    i = p - 1 
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[j],A[i] = A[i], A[j]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1




def quick_sort(A, p, r):


    while p < r:
        pivot  = partition(A, p, r)
        quick_sort(A,p,pivot - 1)
        p = pivot + 1 
    

tab =[9,1,8,2,6,4,10]
print(tab)
quick_sort(tab, 0, len(tab)-1)
print(tab)