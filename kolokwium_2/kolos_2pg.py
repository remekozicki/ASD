
from queue import PriorityQueue


def memorize(O,C,T,L):
    n = len(O)
    DP = [[None for i in range(n)]for i in range(L)]
    #1 to kilometry, 0 to cena za dany parking
    trasa = [[0,0] for i in range(n)]
    #starujemy z miejsca 0 zatem polejne punkty na trasie zaczynają sie od 1
    for i in range(n):
        trasa[i][1],trasa[i][0] = O[i], C[i]
    
    trasa.sort(key = lambda x: x[1])
    j = 0
    T_max = False
    w_min = min(trasa)
    min_cost = 0
    
    
    start_p = 0
    while j < n and L - start_p > T:
        # Q_s = PriorityQueue()
        
        i = j
        
        # Q_s.put(trasa[j])
        # Q_m.put(trasa[j])
        w1 = [float('inf'),0]
        
        while trasa[i][1] - start_p <= T:
            if w1[0] > trasa[i][0]:
               w1 = trasa[i]
               best_i = i
            i+=1
            

        w2 = [float('inf'),0]   
        if not T_max:
            k = j
            # Q_m = PriorityQueue()
            while trasa[k][1] - start_p <= T*2:
                if w2[0] > trasa[k][0]:
                    w2 = trasa[k]
                    best_k = k
                k += 1
        
        curr_min = min(w1,w2)

        if w2[0] < w1[0] and w2[0] == w_min[0]:
            min_cost += w2[0]
            T_max = True
            j = best_k
        else:
            min_cost += w1[0]
            j = best_i
        start_p = trasa[j][1]
    
    return min_cost



O = [17,20,11,5,12]
C = [9,7,7,7,3]
T = 7
L = 25

print(memorize(O,C,T,L))