import numpy as np
import time


def parte1(m, steps):
    explosions = 0
    rows = m.shape[0]
    cols = m.shape[1]
    for i in range(steps):
        alreadyFlash = []
        for x in range(rows):
            for y in range(cols):
                if (x, y) not in alreadyFlash:
                    m[x, y] += 1
                if m[x, y] > 9 and (x, y) not in alreadyFlash:
                    alreadyFlash.append((x, y))
                    m[x, y] = 0
                    explosions += 1 + makeExplosion(m, x, y, alreadyFlash)
    return explosions

def makeExplosion(m, x, y, alreadyFlash):
    exlosions = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            xProv = x + i
            yProv = y + j
            if 0 <= xProv < m.shape[0] and 0 <= yProv < m.shape[1]:
                if (xProv, yProv) not in alreadyFlash:
                    m[xProv, yProv] += 1
                if m[xProv, yProv] > 9:
                    alreadyFlash.append((xProv, yProv))
                    m[xProv, yProv] = 0
                    exlosions += 1 + makeExplosion(m, xProv, yProv, alreadyFlash)
    return exlosions

def parte2(m):
    steps = 0
    rows = m.shape[0]
    cols = m.shape[1]
    while m.any():
        steps += 1
        alreadyFlash = []
        for x in range(rows):
            for y in range(cols):
                if (x, y) not in alreadyFlash:
                    m[x, y] += 1
                if m[x, y] > 9 and (x, y) not in alreadyFlash:
                    alreadyFlash.append((x, y))
                    m[x, y] = 0
                    makeExplosion(m, x, y, alreadyFlash)
    return steps

def leerDatos():
    with open("./data/day11", 'r') as f:
        data = np.matrix([[int(j) for j in i[:-1]] for i in f.readlines()])
    return data


def getStats():
    data = leerDatos()
    data2 = data.copy()
    t1 = time.time()
    res_1 = parte1(data, 100)
    t_parte1 = time.time() - t1
    t1 = time.time()
    res_2 = parte2(data2)
    t_parte2 = time.time() - t1
    return res_1, t_parte1, res_2, t_parte2

def main():
    data = leerDatos()
    print('Los resultados del dia 11')
    print("Parte 1:", parte1(data.copy(), 100))
    print("Parte 2:", parte2(data))
