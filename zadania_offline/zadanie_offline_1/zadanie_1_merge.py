


class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


def insertion_sort(T):

    for i in range(1,len(T)):
        X = T[i]
        j = i - 1
        while j >= 0 and T[j].val > X.val:
            T[j+1] = T[j]
            j -= 1
        T[j+1] = X

def SotrH(p,k):

    T = []
    while p != None:
        tmp = p
        p = p.next
        tmp.next = None
        T.append(tmp)
    insertion_sort(T)


    g = Node(None)
    q = g
    
    for i in range(len(T)):
        q.next = T[i]
        q = q.next
    p = g.next
    return p
    
    


    




def add_to_list(self,x):
    new_el = Node(x)
    if self.head:
        p = self.head
        while p.next:
            p = p.next
        p.next = new_el
    else:
        self.head = new_el

def create_list(self, tab):
    for i in range(len(tab)):
        add_to_list(self, tab[i])

def print_list(self):
    tmp = self.head
    while tmp:
        print(tmp.val, '->', sep='', end='')
        tmp = tmp.next
    print()

l_list = LinkedList()
res = LinkedList()
tab = [2,1,4,3,6,5,7,8]
create_list(l_list,tab)
l_list.head = SotrH(l_list.head,0)
print_list(l_list)




