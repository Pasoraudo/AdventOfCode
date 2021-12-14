import numpy as np


def parte1(coordenadas, folds):
    maxy, maxx = 0, 0
    for y, x in coordenadas:
        if maxy < y:
            maxy = y
        if maxx < x:
            maxx = x
    sx, sy = maxx + 1, maxy + 1
    print(sx, sy)
    res = np.zeros(shape=(sx, sy))
    for y, x in coordenadas:
        res[x, y] = 1
    for fold in folds:
        num = int(fold[2:])
        if fold[:1] == 'x':
            sy = num
            aux = np.zeros(shape=(sx, sy))
            for x in range(sx):
                for y in range(num):
                    if res[x, y] != 0:
                        aux[x, y] = res[x, y]
                    if res[x, num + y + 1] != 0:
                        aux[x, num - y - 1] += res[x, num + y + 1]
        else:
            sx = num + 1
            aux = np.zeros(shape=(sx, sy))
            for x in range(num):
                for y in range(sy):
                    if res[x, y] != 0:
                        aux[x, y] = res[x, y]
                    if res[num + x + 1, y] != 0:
                        aux[num - x - 1, y] = res[num + x + 1, y]
        res = aux
        count = 0
        for line in res:
            for i in line:
                if i != 0:
                    count += 1

        print(count)
    np.savetxt("./data/salida", res, fmt="%d")
    return count


def parte2(data):
    return 0


def leerDatos():
    with open("./data/day13", 'r') as f:
        data = f.read().split('\n\n')
        coordenadas = [(int(i.split(',')[0]), int(i.split(',')[1])) for i in data[0].split('\n')]
        folds = [i[11:] for i in data[1].split('\n')]
    return coordenadas, folds


def main():
    coordenadas, folds = leerDatos()
    print('Los resultados del dia 11')
    print("Parte 1:", parte1(coordenadas, folds))
    print("Parte 2:", parte2(coordenadas))
