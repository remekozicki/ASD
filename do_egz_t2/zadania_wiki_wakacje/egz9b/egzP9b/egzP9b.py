from egzP9btesty import runtests

def unique(T,R):
    n = len(T)
    for u in range(n):
        if T[u] != []:
            T[u].sort()
            idx = 0
            T[u][0] = [T[u][0],idx]
        
            for v in range(1,len(T[u])):

                if T[u][v] == T[u][v-1][0]:
                    idx += 1
                else:
                    idx = 0
                T[u][v] = [T[u][v],idx]

        if R[u] != []:
            R[u].sort()
            idx = 0
            R[u][0] = [R[u][0],idx]

            for v in range(1,len(R[u])):

                if R[u][v] == R[u][v-1][0]:
                    idx += 1
                else:
                    idx = 0
                R[u][v] = [R[u][v],idx]
        
          


def DFS(T,R):
    path = []
    unique(T,R)
    rec_dfs(T,R,0,path)
    return path

def rec_dfs(T,R,u,path):

    for i in range(len(T[u])):
        v = T[u][i]
        if v != None and not v in R[u]:
            T[u][i] = None
            rec_dfs(T,R,v[0],path)
    path.append(u)

def dyrektor( G, R ):
	#Tutaj proszę wpisać własną implementację 
	return DFS(G,R)
	
runtests(dyrektor, all_tests=False)
