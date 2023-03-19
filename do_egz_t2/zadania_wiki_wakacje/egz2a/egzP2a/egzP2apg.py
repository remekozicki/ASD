


def quick_sort_recursion(T, start, end):

    if start < end:
        pivot = partition(T, start, end)
        quick_sort_recursion(T, start, pivot-1)
        quick_sort_recursion(T, pivot+1,end)

def quick_sort_while(T, p, r):

    while p < r:
        pivot = partition(T, p, r)
        quick_sort_recursion(T, p, pivot-1)
        p = pivot +1
    
    
    

def partition(T,p,r):
    x = T[r][1]
    i = p-1
    for j in range(p, r):
        if T[j][1] <= x:
            i+=1
            T[j],T[i] = T[i],T[j]
    T[i+1], T[r] = T[r], T[i+1]
    return i+1

def photo(T,m,k):
    quick_sort_while(T, 0, len(T)-1)
    T.reverse()
    n = len(T)
    Tab = [T[i] for i in range(n)]
    # Tab = [ None for i in range(n)]

    Start = [0 for _ in range(m)]
    End = [0 for _ in range(m)]
    e = -1
    s = k+m-1
    for i in range(m):
        Start[i] = e+1
        e += s
        End[i] = e
        s -= 1


    col = 0
    row = 0
    idx = 0

    while idx < n:
        if Start[row]+col <= End[row]:
            T[idx] = Tab[Start[row]+col]
            idx+=1
        row += 1

        if row == m or idx > End[row]:
            row = 0
            col += 1
       

m = 2 #Ilość rzędów
k = 2 #Ilość osób w najniższym rzędzie
T = [ (1001, 154),(1002, 176),(1003, 189),(1004, 165),(1005, 162) ]
photo(T,m,k)
print(T)