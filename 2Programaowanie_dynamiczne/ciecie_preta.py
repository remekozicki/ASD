'''problem najlepszego pociecia plęta'''

def memorise_cut(p, rod):
    r = [None for i in range(rod)]
    return cut_rod(p, rod, r)
    
def cut_rod(p, n, r):
    if r[n-1] != None:
        return 0
    if n == 0:
        q = 0
    else:
        q = -1
        for i in range(1,n+1):
            q = max(q, p[i-1] + cut_rod(p, n-i,r))
    r[n-1] = q
    return q


def short_cut_rod(p,rod):
    l = [0 for i in range(rod)]
    r= [0 for i in range(rod)]
    r[0] = 0
    for j in range(1,rod+1):
        q = -10000
        for i in range(1,j+1):
            tmp = p[i-1]+r[j-i-1]
            if q < tmp:
                q = tmp
                l[j-1] = i
        r[j-1] = q
    return r[rod-1],l


cost = [1,5,8,9,10,17,17,20,24,30]
rod = 7

print(memorise_cut(cost,rod))
# r,s = short_cut_rod(cost,rod)
# n = rod
# print(r)
# while n > 0:
#     print(s[n-1]) 
#     n -= s[n-1]
