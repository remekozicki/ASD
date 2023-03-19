def sumy(u,v):
    x_u,y_u = u
    x_v,y_v = v
    if y_u < x_v or y_v < x_u:
        a = b = 0
    
    elif x_u <= x_v:
        if y_u <= y_v:
            a = x_v
            b = y_u
        elif y_u > y_v:
            a = x_v
            b = y_v
    
    elif x_u > x_v:
        if y_u <= y_v:
            a = x_u
            b = y_u
        elif y_u > y_v:
            a = x_u
            b = y_v
    
    return a,b

print(sumy([2,4],[2,4]))