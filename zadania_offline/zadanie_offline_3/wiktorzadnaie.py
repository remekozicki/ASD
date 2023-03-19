from zad3testy import runtests

def insertion_sort(T):

    for i in range(len(T)):
        X = T[i]
        j = i - 1
        while j >= 0 and T[j] > X:
            T[j+1] = T[j]
            j -= 1
        T[j+1] = X


def SortTab(T,P):
    
    a = min(T)
    b = max(T)

    buckets = [[] for _ in range(len(T) + 1)]

    for i in range(len(T)):
        index = int(((T[i] - a) / (b - a)) * len(T))
        buckets[index].append(T[i])
    
    x = 0
    for i in range(len(T) + 1):
        for j in range(len(buckets[i])):
            T[x] = buckets[i][j]
            x += 1

    insertion_sort(T)

    return T


runtests( SortTab )

