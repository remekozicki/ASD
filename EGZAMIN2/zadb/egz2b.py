'''
Remigiusz Kozicki
próba podejścia dynamicznego, na n2 dla każdych drzwi w konacie 0 puszczam rekurencyjnie 
szukanie najlepszego przejścia. w forach o range 4 obliczam złoto jakie można zabrać 
a nastepnie szukam najlepszego rozwiazania
niestey jest gdzieś błąd
jest to typowe dodejście dynamiczne
'''

from egz2btesty import runtests

from queue import PriorityQueue


def divide1(C):
    n = len(C)
    graph = [[]for _ in range(n)]

    for i in range(n):
        chest = C[i][0]
        for j in range(1,4):
            if C[i][j][1] != -1:
                gold = C[i][j][0]
                diff = chest - gold
                if diff <= 10:
                    
                    graph[i].append([diff,C[i][j][1]])
    
    return graph

def Dixtra(C):
    n = len(C)
    G = divide1(C)
    Q = PriorityQueue()
    visited = [False for i in range(n)]
    gold = [-float('inf') for i in range(n)]
    
   
    Q.put([0,0])
    
    gold[0] = 0

    while not Q.empty():
        
        u,_ = Q.get()
        
        
        if not visited[u]:
            visited[u] = True
            
            for diff,v in G[u]:
                
                if not visited[v]:
                    if (gold[v] < gold[u] + diff) and (gold[u] + diff >= 0):
                        gold[v] = gold[u] + diff
                        
                        Q.put([v,gold[v]])
    
    return max(gold[n-1],-1)



def divide(C):
    n = len(C)
    graph = [[]for _ in range(n)]

    for i in range(n):
        chest = C[i][0]
        for j in range(1,4):
            # if C[i][j][1] != -1:
            gold = C[i][j][0]
            diff = chest - gold
            if diff > 10:
                diff = 10
            graph[i].append([diff,C[i][j][1]])
    
    return graph

def dynamic(C):
    G = divide(C)
    n = len(C)
    DP = [-1 for _ in range(n)]
    

    res = rec(DP,G,n,0)
    return res

def rec(DP,G,n,idx):

    if idx == n-1:
        return 0
    
    if DP[idx] != -1:
        return DP[idx]

    for i in range(3):
        if G[idx][i][1] != -1:
            DP[idx] = max(DP[idx],rec(DP,G,n,G[idx][i][1]) + G[idx][i][0])
        
    return DP[idx]



def kurwa_mac(C):
    n = len(C)
    tab = [-float('inf') for _ in range(n)]

    tab[0] = 0

    for k in range(n-1):
        chest = C[k][0]
        
        for i in range(1,4):
            next_k = C[k][i][1]
            cost = C[k][i][0]
            diff = chest - cost
            if next_k != -1 and cost >= 0 and diff <= 10 and tab[k]+diff >= 0:
                tab[next_k] = max(tab[next_k],tab[k] + diff)
    
    return max(-1,tab[n-1])
            

def magic(C):
    # tu prosze wpisac wlasna implementacje

    return Dixtra(C)
    # return dynamic(C)
    # return kurwa_mac(C)



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(magic, all_tests=True)
