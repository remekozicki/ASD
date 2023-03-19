

def dominance(P):
    n = len(P)
     
    PP = []
    for i,a in enumerate(P):
        x,y = a
        PP.append([x,y,i])
    
    PP.sort(key = lambda x: x[1]) # po y
    PP.sort(key = lambda x: x[0]) # po x
    
    S = [PP[0][2]]
    
    for i in range(1,n):
        x , y, idx = PP[i]
        flag = True
        for j in range(len(S)):
            if P[S[j]][0] <= x and P[S[j]][1] <= y:
                flag = False
        if flag:
            S.append(idx)    
 
    
    return S

P = [[2,2], [1,1], [2.5,0.5], [3,2], [0.5,3]]

print(dominance(P))