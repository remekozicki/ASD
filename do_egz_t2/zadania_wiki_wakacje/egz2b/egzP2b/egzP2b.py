from egzP2btesty import runtests
from math import log10

def find_sufix(D,Q):
    d = len(D)
    q = len(Q)

    res = 1
    for i in range(q):
        count = 0
        if Q[i] == '':
            res *= d
        else:
            n = len(Q[i])
            for j in range(d):
                if D[j][-n:] == Q[i]:
                    count += 1
            res *= count
    
    wynik = log10(res)
    return wynik

def kryptograf( D, Q ):    
    #tutaj proszę wpisać własną implementację
    return find_sufix(D,Q)

# Zmień all_test na:
# 0 - Dla małych testów
# 1 - Dla złożoności akceptowalnej
# 2 - Dla złożoności dobrej
# 3 - Dla złożoności wzorcowej
runtests(kryptograf, all_tests = 0)