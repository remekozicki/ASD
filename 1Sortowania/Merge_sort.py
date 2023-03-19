'''merge sort'''


def merge_sort(T):
    if len(T) > 1:
        mid = len(T) // 2
        L = T[:mid]
        R = T[mid:]
        
        merge_sort(L)

        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
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
        
    

tab = [3,27,56,4,8]

print(tab)
merge_sort(tab)
print(tab)




