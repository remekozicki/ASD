
def memorise(T,p):
    max_val = p
    n = len(T)
    r = [[0 for i in range(p+1)] for j in range(n)]
    return buildings(T,p,r,i)

def buildings(T,p,r,i):

    n = len(T)

    if r[n-1][p] > 0:
        return r[n-1][p]
    
    if p == 0:
        q = 0
    
    else:
        
        for i in range() 
    
