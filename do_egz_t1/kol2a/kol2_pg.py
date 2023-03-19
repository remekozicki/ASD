

def reproces(P):
    n = len(P)
   
    P_cp = []
    for i in range(n):
        P_cp.append(P[i])

    P_cp.sort(key = lambda x: x[0])

    PP = [0]
    counter = 0
    for i in range(n):
        if P_cp[i][1] == False:
            counter+=1
        elif P_cp[i][1] == True:
            PP.append(counter)
    
    PP.append(counter)
            
    return PP


def zadanie(P,B):

    PP = reproces(P)
    n = len(PP)

    DP = [[None for i in range(2)]for j in range(n)]
    # 0 zaczynam od jacka
    # 1 zaczynam od marka

    J = rec(PP,B,n,DP,n-1,0)
    M = rec(PP,B,n,DP,n-1,1)

    return min(J,M)
  

def rec(PP,B,n,DP,idx,os):

    if idx < 0:
        return float('inf')
    
    if idx == 0:
        return 0

    if DP[idx][os] is not None:
        return DP[idx][os]

    mini = float('inf')
    
    for j in range(idx-3,idx):
        
        if os == 0:
            mini = min(mini, rec(PP,B,n,DP,j,1))
        
        else:
            mini = min(mini, rec(PP,B,n,DP,j,0) + (PP[idx]-PP[j]))
    
    DP[idx][os] = mini
    return mini


p = True
c  = False
P = [(1,c),(3,c),(4,c),(6,c),(8,c),(9,c),(11,c),(13,c),(16,c),(17,c),
           (2,p),(5,p),(7,p),(10,p),(12,p),(14,p),(15,p),(18,p)]

B = 20

print(zadanie(P,B))