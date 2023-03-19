'''sortowanie tablicy'''

def sort_tab(T):
    for i in range(len(T)):
        key = T[i]
        j = i-1
        while j >= 0 and T[j] > key:
            T[j + 1] = T[j]
            j -= 1
        T[j + 1] = key
    
    return T


tab = [ 1, 3, 10, 2, 5, 7, 0, 11]
print (sort_tab(tab))