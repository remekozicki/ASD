'''two pointers (metoga gąsienicowa)'''



def two_pointers(T):
    i = 0
    j = 0
    x = 9

    while j < len(T):

        if T[j] - T[i] < x:
            j += 1
        elif T[j] - T[i] > x:
            i += 1
        else:
            print( T[j]," - " ,T[i],"= ",x,)
            break
    else: print("nie ma takiej różnicy")



tab = [1,5,8,10,12,15,16]

two_pointers(tab)