'''Dana jest dwuwymiarowa tablica T o rozmiarach N x N wypełniona liczbami naturalnymi (liczby
są parami różne). Proszę zaimplementować funkcję Median(T), która przekształca tablicę T , tak
aby elementy leżące pod główną przekątną nie były większe od elementów na głównej przekątnej,
a elementy leżące nad główną przekątną nie były mniejsze od elementów na głównej przekątnej.
Algorytm powinien być jak najszybszy oraz używać jak najmniej pamięci ponad tę, która potrzebna
jest na przechowywanie danych wejściowych (choć algorytm nie musi działać w miejscu). Proszę
podać złożoność czasową i pamięciową zaproponowanego algorytmu.
'''



def partition(A,p,r):

    X = A[r]
    i = p-1
    for j in range(p,r):
        if A[j] <= X:
            i+=1
            A[i], A[j] = A[j], A[i]
    A[j+1], A[r] = A[r], A[j+1]
    return i + 1


def quick_select(T,k,p,r):
    if p == r:
        return T[p]
    
    if p < r:
        q = partition(T,p,r)
        if q == k:
            return T[q]
        elif q < k:
            return quick_select(T,k,q+1,r)
        else:
            return quick_select(T,k,p,q-1) 



