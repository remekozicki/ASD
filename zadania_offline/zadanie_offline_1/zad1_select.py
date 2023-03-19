from zad1testy import Node, runtests

# modyfikacja algorytmu sortowania przez wybieranie z ćwiczeń 
def k_select_sort(T, k):  

    for i in range(len(T)-1):
        key = i
        if (i + k + 1) <= len(T):  # sprawdzany jest przypadek gdy i + k + 1 jest długości tablicy T,
            end = i + k + 1        # w tym przypadek gdy k+1 == len(T) i sortowanie przebeiga po całej tablicy na raz 
        else:
            end = len(T)
        j = i + 1
        while j < end: 
            if T[key].val > T[j].val:
                key = j
            j = j + 1
        T[i], T[key] = T[key], T[i]
            


 

def SortH(p,k):
    T = []
    while p != None:
        tmp = p
        p = p.next
        tmp.next = None
        T.append(tmp)
    k_select_sort(T,k)


    g = Node()
    g.val = None
    q = g
    
    for i in range(len(T)):
        q.next = T[i]
        q = q.next
    p = g.next
    return p
   


runtests( SortH ) 
