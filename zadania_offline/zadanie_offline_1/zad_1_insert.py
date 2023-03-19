from zad1testy import Node, runtests





def insertion_sort(T):
    
    for i in range(1, len(T)):
        X = T[i]
        j = i - 1
        while j >= 0 and T[j].val > X.val:
            T[j+1] = T[j]
            j -= 1
        T[j+1] = X

 

def SortH(p,k):
    T = []
    while p != None:
        tmp = p
        p = p.next
        tmp.next = None
        T.append(tmp)
    insertion_sort(T)


    g = Node()
    g.val = None
    q = g
    
    for i in range(len(T)):
        q.next = T[i]
        q = q.next
    p = g.next
    return p



runtests( SortH ) 
