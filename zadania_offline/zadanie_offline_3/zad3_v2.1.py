from zad3testy import runtests


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

def SortTab(T,P):
    quick_sort_stack(T,0,len(T)-1)
    
    return T

runtests( SortTab )


