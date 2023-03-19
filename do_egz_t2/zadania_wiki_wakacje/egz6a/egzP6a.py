from egzP6atesty import runtests 

def partition(T,p,r,idx):
    x = T[r][idx]
    i = p-1
    for j in range(p, r):
        if T[j][idx] >= x:
            i+=1
            T[j],T[i] = T[i],T[j]
    T[i+1], T[r] = T[r], T[i+1]
    return i+1

def quick_sort_recursion(T, start, end,idx):

    if start < end:
        pivot = partition(T, start, end,idx)
        quick_sort_recursion(T, start, pivot-1,idx)
        quick_sort_recursion(T, pivot+1,end,idx)


def how_many(word):
    n = len(word)
    letters = 0
    numbers = 0
    for i in range(n):
        if ord(word[i]) <= 57:
            numbers += 1
        elif ord(word[i]) >= 97:
            letters += 1
    
    return letters, numbers, n



def fill_tab(H,s):
    n = len(H)
    tab = []

    for i  in range(n):
        let, num, l = how_many(H[i])
        tab.append([H[i],let,l,num]) # 0 word, 1 let, 2 num, 3 len
    
    for i in range(1,3):
        quick_sort_recursion(tab,0,n-1 ,i)
    
    return tab[s-1][0]
    



def google ( H, s ):
    #tutaj proszę wpisać własną implementację
    return fill_tab(H,s)


runtests ( google, all_tests=True )