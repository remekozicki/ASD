from egz3atesty import runtests
"""
Remigius Kozicki

próba wykonania algorytmu O(nlogn), złożoność bierze się z funkcji sort()
do tablicy road O(2n) (zatem chyba nie psuje to złożoności :)) dodaje początki
i końce przedziałów odpowiednio oznaczone (zielony komentarz)
nastepnie sortuje po wartościach odpowiadającyh przedział to zwiekszam count,
a jeśli kończy to biore największą watość z res lub count 
res przechowuje najlepszy wynik jaki został osiągniety
następnie zmniejszam count zatem bo w danym miejscu skonczył mi sie przedział odpaów zatem tam juz nie pada śnieg w danym dniu
niestety jeden z testów różni sie o 1 od poprawnego wyniku i nie znam przyczyny,
gdzyż wydaje mi się że rozumowanie mam poprawne :)
"""

def create_road(I):
    n = len(I)
    road = []
    for i in range(n):
        road.append([I[i][0],0]) #0 początek
        road.append([I[i][1],1]) #1 koniec
    road.sort()
    return road

def highway(T,I):
    n = len(I)
    
    road = create_road(I)
    
    count = 0
    res = 0

    for i in range(len(road)):
        
        if road[i][1] == 0:
            count += 1
        if road[i][1] == 1:
            res = max(res,count)
            count -= 1
    return res


def snow( T, I ):
    # tu prosze wpisac wlasna implementacje
    return highway(T,I)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
