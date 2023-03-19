


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



D = ['0', '100', '1100', '1101', '1111']
Q = ["", "1", "11", "0", "1101"]


# g = 'wwwwweee'
# print(g[-2:])
print(find_sufix(D,Q))