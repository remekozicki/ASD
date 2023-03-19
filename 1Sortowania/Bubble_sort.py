'''Bubble sort n^2''' 

def better_bubble_sort(T):
    i = 0
    done = True
    while i < len(T) - 1 and done:
        j = 0
        done = False
        while j < len(T)-1-i:
            if T[j] > T[j+1]:
                T[j], T[j+1] = T[j+1], T[j]
                done = True
            j += 1
        i += 1
        print(T)

def bubble_sort(T):
    i = 0
    while i < len(T) - 1:
        j = 0
        while j < len(T)-1-i:
            if T[j] > T[j+1]:
                T[j], T[j+1] = T[j+1], T[j]
            j += 1
        i += 1
        print(T)


tab = [1,2,3,4,5]

better_bubble_sort(tab)
