import csv
with open("grid.txt", "r") as f:
    mapa = f.readlines()

for index in range(len(mapa)):
    mapa[index] = list(map(int, mapa[index].split(" ")))

start = (19, 0)
meta = (0, 19)


class Pole:

    def __init__(self, pozycja, rodzic, g=0):
        self.pozycja = pozycja
        self.rodzic = rodzic
        self.g = g
        self.fun = 0


def heurestyka(poz, g, cel):
    return g + ((poz[0] - cel[0]) ** 2 + (poz[1] - cel[1]) ** 2) ** (1 / 2)


def czyistnieje(punkt, lista):
    for i in lista:
        if i.pozycja == punkt:
            return True
    return False


def astar(punktstart, punktkonc, plansza):
    lista_o = []
    lista_z = []
    kroki = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    poczatek = Pole(punktstart, None)
    koniec = Pole(punktkonc, None)
    lista_z.append(poczatek)
    while lista_o is not None:
        for nastepna in kroki:

            nowapozycja = (lista_z[-1].pozycja[0] + nastepna[0], lista_z[-1].pozycja[1] + nastepna[1])

            if (nowapozycja[0] > (len(plansza) - 1)) or (nowapozycja[0] < 0) or (
                    nowapozycja[1] > (len(plansza[0]) - 1)) or nowapozycja[1] < 0:
                continue
            if plansza[nowapozycja[0]][nowapozycja[1]] != 0:
                continue
            if nowapozycja == poczatek.pozycja:
                continue
            if czyistnieje(nowapozycja, lista_z):
                continue
            if czyistnieje(nowapozycja, lista_o):
                continue
            nowy = Pole(nowapozycja, lista_z[-1], lista_z[-1].g)
            lista_o.append(nowy)
            lista_o[-1].g += 1
            lista_o[-1].fun = heurestyka(lista_o[-1].pozycja, lista_o[-1].g, koniec.pozycja)
        if len(lista_o) == 0:
            return 'BRAK SCIEZKI'
        minimum = lista_o[0]
        numer = 0
        for index, elem in enumerate(lista_o):

            if elem.fun < minimum.fun:
                minimum = elem
                numer = index
        lista_z.append(minimum)
        lista_o.pop(numer)
        for i in lista_z:
            if i.pozycja == koniec.pozycja:
                sciezka = []
                rodzic = lista_z[-1]
                while rodzic is not None:
                    sciezka.append(rodzic.pozycja)
                    rodzic = rodzic.rodzic
                return sciezka


droga = astar(start, meta, mapa)

if droga == 'BRAK SCIEZKI':
    print(droga)
else:
    for i in range(len(droga)):
        mapa[droga[i][0]][droga[i][1]] = 3
    for i in range(len(mapa)):
        print(mapa[i])
    with open("gridrozwiaz.txt", "w") as f:
        w = csv.writer(f, delimiter=' ', lineterminator='\n')
        w.writerows(mapa)
