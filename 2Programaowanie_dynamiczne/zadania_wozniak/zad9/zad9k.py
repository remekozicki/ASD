'''
Dana jest tablica P z długościami samochodów (w umownej jednostce) które oczekują w
kolejce, aby wjechać na prom. Pierwszy oczekujący samochód znajduje się pod zerowym
indeksem. Prom ma dwa pokłady (górny i dolny) o długościach odpowiednio wyrażonych
jako g i d. Zakładamy, że pojazdy mogą parkować "zderzak w zderzak" tj. bez zachowania
odstępów między sobą. Każdy pojazd może wjechać na dowolnie wybrany z pokładów,
jednak nie może wyprzedzić poprzedzających go samochodów. Niestety nie zawsze znajdzie
się miejsce dla kolejnego samochodu. W takiej sytuacji kierowca ostatniego pojazdu,
któremu udało się wjechać na prom, zgodnie z tradycją musi zamknąć wjazd oraz sporządzić
listę obecności pojazdów TYLKO na swoim pokładzie w kolejności wjazdu pojazdów na ten
pokład (W szczególności kierowca ten będzie ostatnim na liście obecności). Jako informatyk
pracujący w biurze portowym, zostałeś poproszony o napisanie programu, który wskaże jak
należy wpuszczać samochody na prom (tj. który samochód skierować na który pokład), aby
ich łączna ilość na promie była jak największa.
Algorytm należy zaimplementować jako funkcję postaci:
def prom( P, g, d ):
...
która przyjmuje tablicę długości pojazdów P = [p1, p2, ..., pn] oraz długości pokładów g oraz
d, a zwraca posortowaną tablicę indeksów pojazdów znajdujących się na liście obecności.
'''


from zad9ktesty import runtests
from math import inf

def prom(P, g, d):
    return []

runtests ( prom )