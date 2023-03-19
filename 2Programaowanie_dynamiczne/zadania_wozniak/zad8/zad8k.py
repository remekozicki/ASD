from zad8ktesty import runtests 
def memorize(s,t):
    
    DP = [[-1 for i in range(len(s))]for j in range(len(t))]
    
    if s[0] != t[0]:
        DP[0][0] = 1
    else:
        DP[0][0] = 0
    
  
    for i in range(1,len(s)):
        if t[0] != s[i]:
            DP[0][i] = DP[0][i-1] +1
        else:   
            DP[0][i] = i
    
    
    for i in range(1,len(t)):
        if s[0] != t[i]:
                DP[i][0] = DP[i-1][0] + 1 
        else:
            DP[i][0] = i

    
    for i in range(1,len(s)):
        for j in range(1,len(t)):

            if s[i] == t[j]:
                DP[j][i] = DP[j-1][i-1]
            
            else:
                w1 = DP[j-1][i-1]
                w2 = DP[j][i-1]
                w3 = DP[j-1][i]
                q = min(w1,w2,w3) + 1
                DP[j][i] = q
    
    return DP[len(t)-1][len(s)-1]
    
    
def napraw ( s, t ):
    # print(s)
    # print(t)
    return memorize(s,t)

runtests ( napraw )