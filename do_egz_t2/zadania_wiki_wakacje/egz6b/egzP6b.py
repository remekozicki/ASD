from egzP6btesty import runtests 
def map_moves():
    Dic  = {"UL" : 0,
        "LU" : 1,
        "LD" : 2,
        "DL" : 3,
        "DR" : 4,
        "RD" : 5,
        "RU" : 6,
        "UR" : 7
        }
    # piersza to pionowo deruga to poziomo
    Moves = [(-1,-2),
            (-2,-1),
            (-2,1),
            (-1,2),
            (1,2),
            (2,1),
            (2,-1),
            (1,-2)
            ]
    
    return Dic, Moves

def knight_jump(M):
    DC, MV = map_moves()
    
    x = y = 0
    lights = {}
    
    lights.update({f'{x},{y}':(x,y)})
    
    for step in M:
        idx = DC.get(step)
        sx,sy = MV[idx]
        x += sx
        y += sy

        tmp = lights.get(f'{x},{y}')
        if tmp:
            lights.pop(f'{x},{y}')
        else:
            lights.update({f'{x},{y}':(x,y)})
    
    return len(lights)




def jump ( M ):
    #tutaj proszę wpisać własną implementację
    return  knight_jump(M)
    
runtests(jump, all_tests = True)