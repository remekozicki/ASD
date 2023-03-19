
def funkcja(S,V):
    vl = len(V)
    n = len(S)
    coins = -1
    for i in range(n):
        taken = [0 for _ in range(vl)]
        gone = [False for _ in range(vl)]

        tmp = 0
        for j in range(i,n):
            taken[S[j]-1]+=1
            
            if taken[S[j]-1] == 1:
                tmp += V[S[j]-1]
            elif not gone[S[j]-1]:
                tmp -= V[S[j]-1]*(taken[S[j]-1] - 1)
                gone[S[j]-1] = True
        
            coins = max(coins,tmp)
    return coins



S = [2, 3, 1, 1, 4, 1, 2, 4, 1]
V= [5, 3, 6, 6]

print(funkcja(S,V))