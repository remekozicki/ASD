'''Zadanie 2. Mamy n żołnierzy różnego wzrostu i nieuporządkowaną tablicę, w której
podano wzrosty żołnierzy. Żołnierze zostaną ustawieni na placu w szeregu malejąco względem
wzrostu. Proszę zaimplementować funkcję:
section(T,p,q)
która zwróci tablicę ze wzrostami żołnierzy na pozycjach od p do q włącznie. Użyty algorytm
powinien być możliwie jak najszybszy. Proszę w rozwiązaniu umieścić 1-2 zdaniowy opis
algorytmu oraz proszę oszacować jego złożoność czasową.
'''


def insertion_sort(T):

    for i in range(len(T)):
        X = T[i]
        j = i - 1
        while j >= 0 and T[j] > X:
            T[j+1] = T[j]
            j -= 1
        T[j+1] = X

def bucket_hight(A):
    n = len(A)
    a = 100
    b = 300
    B = [[] for i in range(n)]

    for i in range(n):
        index = int((A[i] - a) / (b - a) * n)
        B[index].append(A[i])

    for i in range(len(B)):
        insertion_sort(B[i])

    res = []

    for i in range(len(B)):
        for j in range(len(B[i])):
            res.append(B[i][j])
    
    return res


tab = [156,170,219,185,192,187,181,178,152,220,205,180]
print(bucket_hight(tab))


