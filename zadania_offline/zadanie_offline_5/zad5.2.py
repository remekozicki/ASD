def greedy_frog(T):
    
    n = len(T)
    S = []
    

    S.append(0)

    i = 0
    e = T[0]
    
    while i < n and e < n:
        tmp_e = 0
        max_j  = 0
        for j in range(1, e):

            if tmp_e < T[j+i]:
                tmp_e = T[j+i]
                max_j = j
        
        i += max_j
        S.append(i)
        e += tmp_e - max_j
        n -= i
    
    return S


T = [3, 0, 2, 1, 0, 2, 5, 0]

print(greedy_frog(T))