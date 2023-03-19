


def funkcja(T,S):

    n = len(T)
    tab = []
    last = -1
    for i in range(n):
        
        tab.append([T[i][0],T[i][1],S[i]]) # start , end, $
    
    tab.sort(key = lambda x: x[0])
   
    best = -1
    for i in range(n):
        best = max(best,tab[i][2])
        for j in range(i,n):
            if tab[i][1] < tab[j][0]:
                best = max(best, tab[i][2]+tab[j][2])
    
    return best







T = [ (0, 3), (4, 5), (1, 4) ]
S = [ 5000, 3000, 15000 ]
print(funkcja(T,S))