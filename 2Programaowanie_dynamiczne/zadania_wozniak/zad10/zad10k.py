from zad10ktesty import runtests

def get_sol(N, D):
    x = 1
    val = D[N]-1
    sol = []
    ind = N

    while x*x <= ind:
        if D[ind-x*x] == val:
            sol.append(x)
            ind -= x*x
            # x = 1
            val -= 1
        else:
            x+=1

    return sorted(sol)

def problem(N,res):
    
    if res[N] != None:
        return res[N]
    
    if N == 0:
        q = 0
    
    else:
        q = float('inf')
        
        R = int(N**0.5)
        
        for j in range(1,R+1):

            q = min(q, problem(N - (j**2), res) + 1)
    
    res[N] = q
    return q

def dywany ( N ):
    res = [None for i in range(N+1)]
    problem(N,res)
    print(res[-1])
    return get_sol(N,res)

runtests( dywany )

