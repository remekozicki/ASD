
# Remigiusz Kozicki

# program rozdziela stringi do bucketów pod względem ich długości
# nastepnie porównuje je ze soba i znajduje siłe o jendą mniej bo nie liczy siebie,
# stąd dodana jedynka w return w funkcji bucket.

# szacowana złożoność to O(N nlogn)



from kol1atesty import runtests


def get_max_min(T):
    min_val = float('inf')
    max_val = 0
    for i in range(len(T)):
        if len(T[i]) > max_val:
            max_val = len(T[i])
        if len(T[i]) < min_val:
            min_val = len(T[i])
    return min_val, max_val


def bucket(T):
    n = len(T)
    min_val, max_val = get_max_min(T)
    diff = max_val - min_val

    B = [[] for _ in range(diff+1)]

    for i in range(n):
        index = int(len(T[i]) - min_val)
        B[index].append(T[i])
    
    max_strong = 0
    
    for i in range(len(B)):
        compare= find_max_strong(B[i])
        if max_strong < compare:
            max_strong = compare
            
    
    return max_strong +1



def find_max_strong(T):
    n = len(T)
    strong_max = 0
    
    for i in range(n):
        if T[i] == 0:
            continue
        strong_tmp = 0
        for j in range(n):
            if i == j or T[j] == 0:
                continue
            if  T[i] == T[j]:
                strong_tmp += 1
                T[j] = 0
            elif T[i] == T[j][::-1]:
                strong_tmp += 1
                T[j] = 0
        
        if strong_max < strong_tmp:
            strong_max = strong_tmp
        T[i] = 0   
    
    return strong_max




def g(T):
    X = bucket(T)
    return X


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( g, all_tests=True )
