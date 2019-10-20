with open("grid.txt", "r") as f:
    mapa = f.readlines()

for index in range(len(mapa)):
    mapa[index] = list(map(int, mapa[index].split(" ")))

start = (19, 0)
meta = (19, 2)


class Pole:

    def __init__(self, pozycja, rodzic):
        self.pozycja = pozycja
        self.rodzic = rodzic
        self.g = 0
        self.fun = 0


def heurestyka(poz, g, cel):
    return g + ((poz[0] - cel[0]) ** 2 + (poz[1] - cel[1]) ** 2) ** (1 / 2)


def astar(punktstart, punktkonc, plansza):
    lista_o = []
    lista_z = []
    poczatek = Pole(punktstart, None)
    koniec = Pole(punktkonc, None)
    lista_o.append(poczatek)
    while lista_o is not None:
        punkt = lista_o[0]
        indeks = 0
        for i, element in enumerate(lista_o):
            if element.fun < punkt.fun:
                punkt = element
                indeks = i

        lista_o.pop(indeks)
        lista_z.append(punkt)

        if punkt.pozycja == koniec.pozycja:
            sciezka = []
            rodzic = punkt
            while rodzic is not None:
                sciezka.append(rodzic.pozycja)
                rodzic = rodzic.rodzic
            return sciezka[::-1]

        dziecko = []
        for nastepna in [(-1, 0), (1, 0), (0, -1), (0, 1)]:

            nowapozycja = (punkt.pozycja[0] + nastepna[0], punkt.pozycja[1] + nastepna[1])

            if (nowapozycja[0] > (len(plansza) - 1)) or (nowapozycja[0] < 0) or (
                    nowapozycja[1] > (len(plansza[0]) - 1)) or nowapozycja[1] < 0:
                continue
            if plansza[nowapozycja[0]][nowapozycja[1]] != 0:
                continue
            nowe = Pole(nowapozycja, punkt)
            dziecko.append(nowe)

        for elem in dziecko:

            for z in lista_z:
                if elem == z:
                    continue
            elem.g = punkt.g + 1
            elem.fun = heurestyka(elem.pozycja, elem.g, punktkonc)

            for o in lista_o:
                if elem == o and elem.g > o.g:
                    continue

            lista_o.append(elem)


droga = astar(start, meta, mapa)
print(droga)


for i in range(len(droga)):
    mapa[droga[i][0]][droga[i][1]] = 3

for i in range(len(mapa)):
    print(mapa[i])