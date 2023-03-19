'''insertion sort'''



def insertion_sort(T):

    for i in range(len(T)):
        X = T[i]
        j = i - 1
        while j >= 0 and T[j] > X:
            T[j+1] = T[j]
            j -= 1
        T[j+1] = X
        print(T)







def insertion_s_rev(tab):
    n = len(tab)
    for i in range(1,n):
        x = tab[i]
        j = i-1
        while j >= 0 and tab[j] > x:
            tab[j+1] = tab[j]
            j-=1
        tab[j+1] = x






tab = [2,1,4,3,6,5,2,8]
print(insertion_sort(tab))