'''operacje na wskaźnikach'''
from unittest import result


class LinkedList:
    def __init__(self):
        self.head = None

class Node:
    def __init__(self,val = None):
        self.next = None
        self.val = val

'''2.a  wstawianie do posortowanej listy'''

def insert(l, N):
    p = l
    
    while l.next != None and l.next.val <= N.val:
        l = l.next
    temp = l.next
    l.next = N
    N.next = temp
    
    return p
'''2.b usuwanie max z listy'''

def delete_max(l):
    max_l = l

    while l.next != None:
        if max_l.next.val < l.next.val:
            max_l = l
        l = l.next
    result = max_l.next
    max_l.next = max_l.next.next
    return result
'''2.c sortowanie przez wstawienie'''

def insort(l):
    new_l = Node(None)

    while l.next != None:
        K = l.next
        l.next = l.next.next
        insert(new_l, K)
    l.next = new_l.next
    return l.next

'''2.c.2 sortowanie przez wybór'''

def select_sort(l):
    s = Node(None)
    while l.next != None:
        x = delete_max(l)
        x.next = s.next
        s.next = x
    l.next = s.next
    return l.next

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
    tmp = self
    while tmp:
        print(tmp.val, '->', sep='', end='')
        tmp = tmp.next
    print()

l_list = LinkedList()

tab = [1,4,3,5,8,7,9,11,10,0]

create_list(l_list, tab)
print_list(l_list.head)
g = Node(None)
g.next = l_list.head
note = Node(0)
#l_list.head = insert(g, note)
#print_list(l_list)
#deleted = delete_max(l_list.head)
#print(deleted.val)
# insort_res = insort(g)
# print_list(insort_res)
selsort_res = select_sort(g)
print_list(selsort_res)
