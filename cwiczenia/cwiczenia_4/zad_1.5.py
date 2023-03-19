'''mamy tablice kolrorów gdzie na każdej pozycji jest nr. odpowiadający kolorowi, i jest k kolorów.
należy znaleś najkrótszy odcinek zawierający wszystekie kolory
'''


def find_colours(A,k):

    C = [0]*k
    colors = k

    l = 0
    r = 0
    min_len = len(A)+1
    
    while r < len(A):
        
        tmp_min_len = 0
        
        while colors > 0:
            if r >= len(A):
                break
            if C[A[r]] == 0:
                colors -= 1
        
            C[A[r]] += 1
            r += 1
        tmp_min_len = r - l
        
        while colors < k :
        
            if C[A[l]] == 1:
                C[A[l]] = 0
                colors += 1
                l +=1
                break
        
            C[A[l]] -= 1
            l += 1
            tmp_min_len -= 1
        
        
        if tmp_min_len < min_len:
            min_len = tmp_min_len
            l_min = l
            r_min = r
        
        # if min_len == k:
        #     return l_min, r_min, min_len
    
    return l_min, r_min, min_len
    






tab = [1,1,1,1,1,1,1,1,1]
print(find_colours(tab,4))

