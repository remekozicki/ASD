'''tablica A zawiera elementy ze zbioru B, gdzie |B|<= log(n)
parami różnych liczb
'''

from calendar import c
from math import log
from unittest import result



def binary_search(A,x):
    L = 0
    P = len(A) -1

    while L <= P:
        mid = (L+P) //2

        if A[mid][0] == x:
            return mid, None
        elif A[mid][0] > x:
            P = mid -1
        else:
            L = mid + 1
    else:
        return L, P


def zadanie(A):
    n = len(A)
    B = [[A[0],0]]
    
    for i in range(n):
        indexL, indexP = binary_search(B,A[i])
        if indexP != None:
            B = B[:indexP +1] + [[A[i],1]] + B[indexL:]

            
        else:
            B[indexL][1] += 1
    C = [0]*len(B)
    C[0] = B[0][1]
    for i  in range(1,len(B)):
        C[i] =  B[i][1] + B[i-1][1]
    
    j = 0
    for i in range(len(B)):
        while B[i][1] > 0:
            A[j] = B[i][0]
            j += 1
            B[i][1] -= 1
    return A
        


tab = [90,2,7,90,7,90,7,2]
print(zadanie(tab))
