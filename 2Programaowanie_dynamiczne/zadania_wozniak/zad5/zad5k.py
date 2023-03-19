
'''
Dana jest talia N kart wyrażona poprzez tablicę A liczb naturalnych zawierającą wartości tych
kart. Można przyjąć, że talia posiada parzystą ilość kart. Karty zostały rozłożone na bardzo
szerokim stole w kolejności pojawiania się w tablicy. Dziekan poinformował Cię, że
podwyższy Ci ocenę z WDI o pół stopnia, jeżeli wygrasz z nim w pewną grę, polegającą na
braniu kart z jednego lub drugiego końca stołu na zmianę. Zakładając, że zaczynasz
rozgrywkę, musisz znaleźć jaką maksymalnie sumę wartości kart uda Ci się uzyskać.
Jednak, co ważne, musisz przyjąć, że dziekan jest osobą bardzo inteligentną i także będzie
grał w 100% na tyle optymalnie, na tyle to możliwe. Aby nie oddawać losu w ręce szczęścia
postanowiłeś, że napiszesz program, który zagwarantuje Ci wygraną (lub remis). Twój
algorytm powinien powiedzieć Ci, jaka jest maksymalna suma wartości kart, którą masz
szansę zdobyć grając z Garkiem.
Algorytm należy zaimplementować jako funkcję postaci:
def garek( A ):
...
która przyjmuje tablicę liczb naturalnych T i zwraca liczbę będącą maksymalną możliwą do
uzyskania sumą wartości kart.
'''

def garek_f(T):
    n = len(T)
    DP = [[None for i in range(n)]for j in range(n)]
    
    a = 0
    b = n-1
    
    res = rec(T,DP, a, b,n)
    return res[0]

def rec(T,DP,a,b,n) :

    if DP[a][b] != None:
        return DP[a][b]
    if a == b:
        return [T[a],0]
    if a+1 == b:
        return [max(T[a],T[b]),min(T[a],T[b])]
    
    else:

        if T[a] + rec(T,DP,a+1,b,n)[1] >  T[b] + rec(T,DP,a,b-1,n)[1]:
            q = [T[a] + rec(T,DP,a+1,b,n)[1],rec(T,DP,a+1,b,n)[0]]
        else:
            q = [T[b] + rec(T,DP,a,b-1,n)[1],rec(T,DP,a,b-1,n)[0]]
    
    DP[a][b] = q
    return q

  

from zad5ktesty import runtests

def garek ( A ):
    #Tutaj proszę wpisać własną implementację
    return garek_f(A)

runtests ( garek )