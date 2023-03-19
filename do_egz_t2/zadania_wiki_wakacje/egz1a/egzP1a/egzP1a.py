from egzP1atesty import runtests 
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
def titanic( W, M, D ):
    #tutaj proszę wpisać własną implementację
    return titanic_sol(W,D,M)

runtests ( titanic, recursion=False)