'''select sort'''

def select_sort(T):
    for i in range(len(T)-1):
        key = i
        j = i + 1
        while j < len(T):
            if T[key] > T[j]:
                key = j
            j += 1
        T[i], T[key] = T[key], T[i]
        print(T)




tab = [2,1,4,3,6,5,7,8]
select_sort(tab)
print(tab)