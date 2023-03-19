

def create_dic(D,M):
    dict = {}
    for i in D:
        dict.update({M[i][1] :M[i][0]})
    return dict

def create_string(W,M):
    mors_str = ''
    for w_let in W:
        idx = ord(w_let) - 65
        mors = M[idx][1]
        mors_str += mors
    return mors_str

def titanic_sol(W,D,M):
    dict = create_dic(D,M)
    sos = create_string(W,M)
    n = len(sos)

    DP = [None for _ in range(n)]

    idx = n-1

    res = rec(DP,sos,dict,idx,n)
    return res

def rec(DP,sos,dict,idx,n):
    
    if idx == 0:
        DP[idx] = 1
        return 1
    
    
    if DP[idx] != None:
        return DP[idx]
    
    else:
        mini = float('inf')
        for i in range(1,5):
            if idx - i >= 0:
                cut = sos[idx-i:idx]
                if dict.get(cut) != None:
                    mini = min(mini,rec(DP,sos,dict,idx-i,n))
                    
        DP[idx] = mini + 1
        return DP[idx]
            
W = "SOS"
D = [0, 4, 13, 19, 25]
M = [('A', '.-'), ('B', '-...'), ('C', '-.-.'), ('D', '-..'), ('E', '.'), ('F', '..-.'),
('G', '--.'), ('H', '....'), ('I', '..'), ('J', '.---'), ('K', '-.-'), ('L', '.-..'),
('M', '--'), ('N', '-.'), ('O', '---'), ('P', '.--.'), ('Q', '--.-'), ('R', '.-.'), 
('S', '...'), ('T', '-'), ('U', '..-'), ('V', '...-'), ('W', '.--'), ('X', '-..-'),
('Y', '-.--'), ('Z', '--..')]
print(titanic_sol(W,D,M))
# print(ord('A'))
# print(chr(65))

# dict = create_dic(D,M)
# print(dict.get('.-'))




# tab = '...---...'
# n = len(tab)
# tab = [[9 for i in range(3)]for j in range(2)]
# print(tab)
