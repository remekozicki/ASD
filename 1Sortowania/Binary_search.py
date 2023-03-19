'''binary search'''

def binary_search(T, x):
    L = 0
    P = len(T) - 1

    while L <= P:
        mid = (L+P) //2

        if T[mid] == x:
            return mid 
        elif T[mid] > x:
            P = mid - 1
        else:
            L = mid + 1
    else:
        return "chujnia nie ma XDDD" 

tab = [1,2,4,6,8,9,10]
print(binary_search(tab, 11))