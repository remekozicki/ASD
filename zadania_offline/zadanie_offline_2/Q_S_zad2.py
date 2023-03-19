from zad2testy import runtests


def partition_range(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if (A[j][1] - A[j][0]) >= (x[1] - x[0]):
            i += 1
            A[i], A[j] = A[j],A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1   



class Stack:
    def __init__(self) -> None:
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, data):
        return self.items.append(data)
    
    def pop(self):
        return self.items.pop()


def quick_sort_stack_range(T, p, r):
    s = Stack()
    s.push((p,r))
    while not s.is_empty():
        p,r = s.pop()
        if p < r:
            pivot = partition_range(T,p,r)
            if (pivot - p) < (r - pivot):
                s.push((pivot+1,r))
                s.push((p,pivot-1))
            else:
                s.push((p,pivot-1))
                s.push((pivot+1,r))

       
def stabile_quick_sort_cord(T):

    if len(T) <= 1:
        return T

    else:
        mid = len(T) // 2
        pivot = T[mid]

        small, big = [], []

        for i, val in enumerate(T):
            if i != mid:
                if val[0] < pivot[0]:
                    small.append(val)
                elif val[0] > pivot[0]:
                    big.append(val)

                else:
                    if i < mid:
                        small.append(val)
                    else:
                        big.append(val)
        return stabile_quick_sort_cord(small) + [pivot] + stabile_quick_sort_cord(big)

def is_in_range_other(T):
    max_in = 0
    i = 0
    while i < len(T)-1:
        catch = 0
        max_tmp = 0
        for j in range(i+1, len(T)):
            if T[i][1] <= T[j][0]:
                break

            if T[i][0] <= T[j][0] and T[i][1] >= T[j][1]:
                max_tmp += 1

            elif catch == 0:
                catch = j

        if max_in < max_tmp:
            max_in = max_tmp
        
        if i < catch:
            i = catch
        else:
            i = j


    return max_in


def depth(L):
    quick_sort_stack_range(L, 0 , len(L)-1) 
    
    L = stabile_quick_sort_cord(L)

    
    result = is_in_range_other(L)
    return result


runtests( depth ) 
