'''Quick sort'''



def divide(T, start, end):
    pivot = T[end]
    left = start  #lewa strona od początku
    right = end - 1 #prawa strona od końca minus ostatni element (pivot)

    while True:
        while left <= right and T[left] <= pivot:
            left += 1
        
        while left <= right and T[right] >= pivot:
            right -= 1
        
        if left <= right:
            T[left], T[right] = T[right], T[left]
        else:
            break
    
    T[left], T[end] = T[end], T[left]

    return left


def quick_sort_recursion(T, start, end):

    if start < end:
        pivot = divide(T, start, end)
        quick_sort_recursion(T, start, pivot-1)
        quick_sort_recursion(T, pivot+1,end)

def quick_sort_while(T, p, r):

    while p < r:
        pivot = divide(T, p, r)
        quick_sort_recursion(T, p, pivot-1)
        p = pivot +1

class Stack:
    def __init__(self) -> None:
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, data):
        return self.items.append(data)
    
    def pop(self):
        return self.items.pop()

def partition(T,p,r):
    x = T[r]
    i = p-1
    for j in range(p, r):
        if T[j] <= x:
            i+=1
            T[j],T[i] = T[i],T[j]
    T[i+1], T[r] = T[r], T[i+1]
    return i+1

def quick_sort_stack(T, p, r):
    s = Stack()
    s.push((p,r))
    while not s.is_empty():
        p,r = s.pop()
        if p < r:
            pivot = partition(T,p,r)
            if (pivot - p) < (r - pivot):
                s.push((pivot+1,r))
                s.push((p,pivot-1))
            else:
                s.push((p,pivot-1))
                s.push((pivot+1,r))



def get_pivot(T,start,end):
    x = T[end]
    i = start - 1
    for j in range(start, end):
        if T[j] <= x:
            i += 1
            T[j],T[i] = T[i],T[j]
    T[i+1], T[end] = T[end], T[i+1]
    return i+1



def quick_sort_rev(T,start,end):

    if start < end:
        pivot =  get_pivot(T,start,end)
        quick_sort_rev(T,start,pivot-1)
        quick_sort_rev(T,pivot+1,end)


tab =[9,1,8,2,6,4,10]
print(tab)
# quick_sort_stack(tab, 0, len(tab)-1)
quick_sort_rev(tab, 0, len(tab)-1)
print(tab)