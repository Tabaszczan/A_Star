with open("grid.txt", "r") as f:
    mapa = f.readlines()

for index in range(len(mapa)):
    mapa[index] = list(map(int, mapa[index].split(" ")))

start = (3, 5)
meta = (0, 0)


class Pole:

    def __init__(self, pozycja, rodzic, g=0):
        self.pozycja = pozycja
        self.rodzic = rodzic
        self.g = g
        self.fun = 0


def heurestyka(poz, g, cel):
    return g + ((poz[0] - cel[0]) ** 2 + (poz[1] - cel[1]) ** 2) ** (1 / 2)


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
            nowy = Pole(nowapozycja, lista_z[-1], lista_z[-1].g)
           # for i in lista_o:
              #  if i.pozycja == nowy.pozycja:
            lista_o.append(nowy)
            lista_o[-1].g += 1
            lista_o[-1].fun = heurestyka(lista_o[-1].pozycja, lista_o[-1].g, koniec.pozycja)
        minimum = lista_o[-1]
        for i in lista_o:
            if i.fun < minimum.fun:
                minimum = i
        lista_z.append(minimum)
        for i in lista_o:
            if i.pozycja == koniec.pozycja:
                sciezka = []
                for i in lista_z:
                   sciezka.append(i.pozycja)
                return sciezka[::-1]


print(astar(start, meta, mapa))