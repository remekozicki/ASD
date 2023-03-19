def memorise(p,S,f):
    m = 0
    n = S+1
    r = [[-1 for i in range(n)]for j in range(f)]
    return problem(p,S,r,f,m)

def problem(p,S,r,f,m):
    n = S+1
    if r[f-1][S] > 0:
        return r[f-1][S]

    if m == f:
        q = 0
    
    else:
        q = -1
    
        for i in range(n):
            w = p[m][i] + problem(p,S-i,r,f,m+1)
            q = max(q, w)
        
    r[m-1][S] = q
    return q


    
tab = [[0,5,15,40,80,90,95,98,100],[0,5,15,40,60,70,73,74,75],[0,4,26,40,45,50,51,52,53]]
print(memorise(tab,8,3))