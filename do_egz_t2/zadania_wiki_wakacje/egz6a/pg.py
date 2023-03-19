res = ord('9') 
print(ord('0') )
print(ord('9') )
print(ord('a') )
print(ord('z') )

def merge_sort(T,idx):
    if len(T) > 1:
        mid = len(T) // 2
        L = T[:mid]
        R = T[mid:]
        
        merge_sort(L,idx)

        merge_sort(R,idx)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i][idx] > R[j][idx]:
                T[k] = L[i]
                i += 1
            else:
                T[k] = R[j]
                j += 1
            k += 1
        while len(L) > i:
            T[k] = L[i]
            i += 1
            k += 1
        while len(R) > j:
            T[k] = R[j]
            j += 1
            k += 1

def partition(T,p,r,idx):
    x = T[r][idx]
    i = p-1
    for j in range(p, r):
        if T[j][idx] >= x:
            i+=1
            T[j],T[i] = T[i],T[j]
    T[i+1], T[r] = T[r], T[i+1]
    return i+1

def quick_sort_recursion(T, start, end,idx):

    if start < end:
        pivot = partition(T, start, end,idx)
        quick_sort_recursion(T, start, pivot-1,idx)
        quick_sort_recursion(T, pivot+1,end,idx)


T = [3,4,1,8,2,0,10]
B = [(3, 1), (0, 1), (4, 2), (1, 2), (0, 1), (2, 4), (2, 4), (0, 3), (2, 4), (1, 0), (2, 1)]
merge_sort(B,1)
merge_sort(B,0)
quick_sort_recursion(B, 0, len(B)-1,1)
quick_sort_recursion(B, 0 , len(B)-1,0)
print(B)
