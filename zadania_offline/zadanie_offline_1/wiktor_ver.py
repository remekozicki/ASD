from zad1testy import Node, runtests


def selection_sort(T, k):  # O(n^2)

    for i in range(len(T) - 1):
        minIndex = i
        if (i + 1 + k) <= len(T):
            end = i + 1 + k
        else:
            end = len(T)
        for j in range(i + 1, end):
            if T[j].val < T[minIndex].val:
                minIndex = j

        T[i], T[minIndex] = T[minIndex], T[i]


def SortH(p, k):

    t = []
    q = p
    while q is not None:
        t.append(q)
        q = q.next

    selection_sort(t, k)
    #for i in range(len(t)):
        #print(t[i].val)

    p = t[0]
    p.next = None
    q = p
    for i in range(1, len(t)):
        t[i].next = None
        q.next = t[i]
        q = q.next

    return p


runtests( SortH )