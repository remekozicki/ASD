'''mnożenie macierzy'''


def matrix_multiply(p):
    n = len(p)
    m = [[-1 for i in range(n)]for j in range(n)]
    s = [[-1 for i in range(n-1)]for j in range(1,n)]
    for i in range(n):
        m[i][i] = 0
    for l in range(1,n):
        for i in range(n-l):
            j = i + l
            m[j][i] = float('inf')
            for k in range(i,j):
                q = m[i][k] + m[k+1][j] + (p[i][0]*p[])




tab = [(1,2),(2,3),(3,4),(4,5),(5,6),(6,5)]