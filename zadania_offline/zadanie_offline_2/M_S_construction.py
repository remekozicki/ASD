'''merge sort'''


def merge_sort_range(T):
    if len(T) > 1:
        mid = len(T) // 2
        L = T[:mid]
        R = T[mid:]
        # print("L:", L)
        # print("R:", R)
        merge_sort_range(L)

        merge_sort_range(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if (L[i][1]-L[i][0]) < (R[j][1] - R[j][0]):
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
        # print("sorted:", T)
        
def merge_sort_cords(T):
    if len(T) > 1:
        mid = len(T) // 2
        L = T[:mid]
        R = T[mid:]
        # print("L:", L)
        # print("R:", R)
        merge_sort_cords(L)

        merge_sort_cords(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i][0] < R[j][0]:
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
        # print("sorted:", T)

def is_in_range_other(T):
    max_in = 0
    i = 0
    while i < len(T)-1:
        catch = 0
        max_tmp = 0
        for j in range(i+1, len(T)):
            if T[i][1] <= T[j][0]:
                break

            if T[i][0] <= T[j][0] and T[i][1] >= T[j][1]:
                max_tmp += 1

            elif catch == 0:
                catch = j

        if max_in < max_tmp:
            max_in = max_tmp
        
        if i < catch:
            i = catch
        else:
            i = j


    return max_in


def problem(T):
    merge_sort_range(T)
    # print(T)
    merge_sort_cords(T)
    print(T)
    result = is_in_range_other(T)
    return result



tab = [(1, 5), (2, 8), (1, 6), (7, 8), (2, 7), (2, 4), (8, 9), (3, 4), (1, 5)]

# print(tab)
print(problem(tab))




