from zad5testy import runtests

from queue import PriorityQueue


def greedy_frog_heap(T):

    n = len(T)

    S = []
    S.append(0)

    more_inf = [[0,0]for j in range(n)]
    for i in range(n):
        more_inf[i][0] = T[i]
        more_inf[i][1] = i
    
    E = T[0]
    i = 0
    max_i = 0
    Q = PriorityQueue()
    
    while i+E < n-1:
        
        step = 0
        for j in range(i+1,i+E+1):
            
            if more_inf[j][0] == 0:
                step += 1
                continue

            else:
                
                tmp = more_inf[j][0]*(-1), more_inf[j][1]
                Q.put(tmp)
                step +=1
                
        
        max_item = Q.get()
        S.append(max_item[1])
        i = j
        E = E - step + max_item[0]*-1

    S.sort() 
    return S

def plan(T):
    
    return greedy_frog_heap(T)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )