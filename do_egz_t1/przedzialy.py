


def sorting(I):
    II = []

    for i,v in enumerate(I):
        x,y = v
        II.append([x,y,i])

    II.sort(key = lambda x: x[0])

    return II

def zadanie(I,x,y):

    n = len(I)
    DP = [False for _ in range(n)]

    II = sorting(I) 
    i = 0
    while II[i][0] < x:
        i+=1
    
    while II[i][0] == x:
        DP[II[i][2]] = rec(II,DP,i,x,y,n)

        i+=1
    res = []
    for i in range(n):
        if DP[i]:
            res.append(i)
    
    return res

    
def rec(II,DP,idx,x,y,n):

    if II[idx][1] == y:
        DP[II[idx][2]] = True
        return True



    for i in range(idx+1,n):
        if II[i][0] > II[idx][1]:
            break
        
        else:
            if II[i][0] == II[idx][1]:
                res = rec(II,DP,i,x,y,n)
                
                if not DP[II[i][2]]:
                    DP[II[i][2]] = res
    
    
    return DP[II[i][2]]


            

I = [[3,4],[2,5],[1,3],[4,6],[1,4]]

x = 1
y = 6

print( zadanie(I,x,y))