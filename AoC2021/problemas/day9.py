import numpy as np
import time

def parte1(matriz):
    res = 0
    rows = matriz.shape[0]
    cols = matriz.shape[1]
    for x in range(rows):
        for y in range(cols):
            if menorQueAdyacentes(matriz, x, y):
                res += 1 + matriz[x, y]
    return res


def parte2(matriz):
    res = [0, 0, 0]
    rows = matriz.shape[0]
    cols = matriz.shape[1]
    visitadas = []
    for x in range(rows):
        for y in range(cols):
            c = cuenca(matriz, visitadas, x, y, rows, cols)
            if min(res) < c:
                res[res.index(min(res))] = c
    return res[0] * res[1] * res[2]


def cuenca(m, visitadas, x, y, rows, cols):
    if (x, y) in visitadas or m[x, y] == 9:
        return 0
    visitadas.append((x, y))
    res = 1
    if x < rows - 1:
        res += cuenca(m, visitadas, x + 1, y, rows, cols)
    if y < cols - 1:
        res += cuenca(m, visitadas, x, y + 1, rows, cols)
    if x > 0:
        res += cuenca(m, visitadas, x - 1, y, rows, cols)
    if y > 0:
        res += cuenca(m, visitadas, x, y - 1, rows, cols)
    return res


def menorQueAdyacentes(matriz, x, y):
    num = matriz[x, y]
    rows = matriz.shape[0]
    cols = matriz.shape[1]
    if x < rows - 1 and num >= matriz[x + 1, y]:
        return False
    elif y < cols - 1 and num >= matriz[x, y + 1]:
        return False
    elif x > 0 and num >= matriz[x - 1, y]:
        return False
    elif y > 0 and num >= matriz[x, y - 1]:
        return False
    return True

def leerDatos():
    with open("./data/day9", 'r') as f:
        data = np.matrix([[int(j) for j in i[:-1]] for i in f.readlines()])
    return data


def getStats():
    data = leerDatos()
    t1 = time.time()
    res_1 = parte1(data)
    t_parte1 = time.time() - t1
    t1 = time.time()
    res_2 = parte2(data)
    t_parte2 = time.time() - t1
    return res_1, t_parte1, res_2, t_parte2

"""
    El input debe tener un enter al final, en caso contrario salta un error
"""


def main():
    data = leerDatos()
    print('Los resultados del dia 9')
    print("Parte 1:", parte1(data))
    print("Parte 2:", parte2(data))
