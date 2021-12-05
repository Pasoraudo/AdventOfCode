def problema(lineas, parte):
    res = {}
    for linea in lineas:
        x1, y1, x2, y2 = extraerPuntos(linea)
        if x1 > x2:
            x1, y1, x2, y2 = intercambiar(x1, y1, x2, y2)
        if x2 != x1:
            p = (y2 - y1) / (x2 - x1)
        if x1 == x2 or y1 == y2:
            radar_lineal(x1, y1, x2, y2, res)
        elif parte == 2 and (p == 1 or p == -1):
            radar_diagonal(x1, y1, p, abs(x2 - x1) + 1, res)
    return sum([1 if i >= 2 else 0 for i in res.values()])


def extraerPuntos(linea):
    linea = linea.split(' -> ')
    x1 = int(linea[0].split(',')[0])
    y1 = int(linea[0].split(',')[1])
    x2 = int(linea[1].split(',')[0])
    y2 = int(linea[1].split(',')[1])
    return x1, y1, x2, y2


def intercambiar(x1, y1, x2, y2):
    aux = x2
    x2 = x1
    x1 = aux
    aux = y2
    y2 = y1
    y1 = aux
    return x1, y1, x2, y2

def radar_diagonal(x, y, p, n, res):
    for d in range(n):
        añadirPosicion(x + d, y + d * p, res)


def radar_lineal(x1, y1, x2, y2, res):
    for x in range(x1, x2 + 1):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            añadirPosicion(x, y, res)


def añadirPosicion(x, y, dic):
    k = str(int(x)) + ',' + str(int(y))
    if (k) not in dic.keys():
        dic[k] = 0
    dic[k] += 1


def main():
    with open("./data/day5", 'r') as f:
        data = f.read().split('\n')
    prob = int(input("¿Problema 1 o 2?\n"))
    print("El resultado es: ", problema(data, prob))
