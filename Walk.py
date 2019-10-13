with open("grid.txt", "r") as f:
    mapa = f.readlines()
for i in range(len(mapa)):
    mapa[i] = list(map(int, mapa[i].split(" ")))

start = [19, 0]
meta = [0, 19]


class Pole:
    def __init__(self, pozycja, rodzic):
        self.pozycja = pozycja
        self.rodzic = rodzic
        self.fun = 0


def heurestyka(poz, cel):
    return 1 + ((poz[0] - cel[0]) ** 2 + (poz[1] - cel[1]) ** 2) ** (1 / 2)


def astar(punktstart, punktkonc, plansza):
    lista_o = []
    lista_z = []
    poczatek = Pole(punktstart, None)
    koniec = Pole(punktkonc, None)
    lista_z.append(poczatek)
    while len(lista_z) > 0:
        lista_o.append(lista_z[0])
        lista_o[0].pozycja[0] -= 1
        lista_o[0].rodzic = lista_z[0]
        lista_o[0].fun = heurestyka(lista_o[0].pozycja, punktkonc)
        print(lista_o[0].fun)
    if poczatek == koniec:
        print("udalo sie")


astar(start, meta, mapa)
