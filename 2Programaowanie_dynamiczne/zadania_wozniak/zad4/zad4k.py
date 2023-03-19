from zad4ktesty import runtests
'''
Dany jest ciąg binarny tj. zer oraz jedynek S. Proszę znaleźć taki SPÓJNY fragment tego
ciągu, w którym różnica pomiędzy ilością zer, a jedynek, będzie jak największa. Jeżeli w
ciągu występują same jedynki, należy założyć, że rozwiązaniem jest -1
Algorytm należy zaimplementować jako funkcję postaci:
def roznica( S ):
...
która przyjmuje ciąg S i zwraca wyliczoną największą osiągalną różnicę.


'''

def King_Falisz(T):

    n = len(T)

    DP = [[None for i in range(n)]for j in range(n)]
    DP[0][0] = 0

    for i in range(0,n):
        
        for j in range(0,n):
            if i == j == 0:
                continue
            
            p = q = float('inf')
            
            if j-1 >=0 :
                q = T[i][j] + DP[i][j-1]
            if i-1 >= 0:
                p = T[i][j] + DP[i-1][j] 

            DP[i][j] = min(q,p)
    
    return DP[n-1][n-1]


def falisz ( T ):
    #Tutaj proszę wpisać własną implementację
    return King_Falisz(T)

runtests ( falisz )
