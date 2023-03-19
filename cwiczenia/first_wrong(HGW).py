'''HGW o co chodzi'''

def binary_search(T):
    X = 6
    L = 0
    P = len(T) - 1
    while L < P:
        m = (L+P) //2
        if T[m] == m:
            L = m+1
        else:
            P = m

    if T[P] == P:
        return P+1
    else:
        return P

tab = [1,3,5,6,7,9]
print(tab)
print(binary_search(tab))