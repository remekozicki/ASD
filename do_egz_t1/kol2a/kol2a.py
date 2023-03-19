from kol2atesty import runtests


def new_tab(P):
    n = len(P)
    PP = []
    for i in range(n):
        PP.append([P[i][0],P[i][1],i])
    PP.sort(key = lambda x: x[0])
    
    return PP

def zadanie(P,B):
    k = 3
    PP = new_tab(P)
    n = len(PP)
    DP = [[[None for _ in range(2)]for _ in range(k)]for _ in range(n)]
    os = 0 # 0 jacek, 1 marek
    idx = 0
   # return rec(PP,DP,k-1,os,idx,n)

    idx = 0
    k = 2
    os = 0
    res = []

    while idx < n:

        if PP[idx][1]:
            if k == 0:
                res.append(PP[idx][2])
                k = 2
                os = (os+1)%2
            
            else:
                w1 = rec(PP,DP,k-1,os,idx+1,n)
                w2 =  rec(PP,DP,2,(os+1)%2,idx+1,n)
                if w1 > w2:
                    res.append(PP[idx][2])
                    k = 2
                    os = (os+1)%2
                
                else:
                    k -=1
        idx+=1
    return res
                


def rec(PP,DP,k,os,idx,n):

    if idx == n:
        return 0
    
    if DP[idx][k][os] != None:
        return DP[idx][k][os]
    
    else:
        if PP[idx][1]:
            if k == 0:
                DP[idx][k][os] = rec(PP,DP,2,(os+1)%2,idx+1,n)
            
            else:
                DP[idx][k][os] = min( rec(PP,DP,k-1,os,idx+1,n), rec(PP,DP,2,(os+1)%2,idx+1,n) )
        else:
            DP[idx][k][os] = rec(PP,DP,k,os,idx+1,n) + os

    
    return DP[idx][k][os]

def drivers( P, B ):
    # tu prosze wpisac wlasna implementacje
    return zadanie(P,B)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( drivers, all_tests =True )