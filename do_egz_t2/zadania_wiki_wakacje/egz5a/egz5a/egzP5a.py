from egzP5atesty import runtests 


def field(T):
    n = len(T)
    maxi = -1

    for i in range(n):
        sum = T[i]
        idx = 1
        one  = True
        two = True
        while i + idx < n or i - idx >= 0:
            flag = False
            
            if one and i + idx < n and T[i + idx] >= T[i]:
                sum += T[i]
                flag = True
            
            else:
                one = False
            
            if two and i - idx >= 0 and T[i - idx] >= T[i]:
                sum += T[i]
                flag = True
            
            else:
                two = False
            
            if not flag:
                break
            
            
            idx += 1

        maxi = max(maxi,sum)
    
    return maxi

def liniowo_kurwa(T):
    n = len(T)
    tab = []

    



def inwestor ( T ):
    #tutaj proszę wpisać własną implementację 
    return field(T)

runtests ( inwestor, all_tests=True )