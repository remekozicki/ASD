'''Carl i Jesica mają synka. 
Chcemy podzielić zajęcia w taki sposób żeby każde z rodziców miałóo zadaie nie pokrywające się.
Jeślinie da się tak podzielić to zwracamy IMPOSIBLE a jak da to stringa np. CJJCCJ.
Krotki reprezentują czas poszątku i końca aktywnosci'''


def timetable(T):

    n = len(T)
    s_T = [[0,0,0] for i in range(n)]
    for i in range(n):
        s_T[i][0], s_T[i][1], s_T[i][2] = T[i][0],T[i][1],i
    
    s_T.sort(key = lambda x: x[0])

    last_C = -1
    last_J = -1
    
    T_T = [[0,0] for i in range(n)]

    for i in range(n):
        if s_T[i][0] >= last_C:
            
            last_C = s_T[i][1]
            T_T[i][0],T_T[i][1] = 'C', s_T[i][2]
        
        elif s_T[i][0] >= last_J:
            
            last_J = s_T[i][1]
            T_T[i][0],T_T[i][1] = 'J', s_T[i][2]
        
        else:
            return 'IMPOSSIBLE'
    T_T.sort(key = lambda x: x[1])

    sol = ''

    for i in T_T:
        sol += i[0]

    return sol

# def timetable(T):
#     n = len(T)

#     last_C = [float('inf'),-1]
#     last_J = [float('inf'),-1]
#     T_T = ''
#     for i in range(n):
#         if T[i][0] >= last_C[1] or T[i][1] <= last_C[0]:
#             last_C[0], last_C[1] = T[i][0],T[i][1]
#             T_T += 'C'
        
#         elif T[i][0] >= last_J[1] or T[i][1] <= last_J[0]:
#             last_J[0], last_J[1] = T[i][0],T[i][1]
#             T_T += 'J'
        
#         else:
#             return 'IMPOSSIBLE'
    
#     return T_T







T = [ [99,150], [1,100], [100,301],[150,250], [2,5]]

print(timetable(T))