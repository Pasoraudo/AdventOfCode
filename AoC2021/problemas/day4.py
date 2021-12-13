import numpy as np
from collections import Counter
import time


def parte1(numeros, tableros):
    for num in numeros:
        posiblesGanadores = []
        for t in tableros:
            for line in t:
                for n in line:
                    if n == num:
                        line[line.index(n)] = 'check'
                        posiblesGanadores.append(t)
        for t in posiblesGanadores:
            if comprobarSiGanado(t):
                return int(num) * sumAllUnmarked(t)

def parte2(numeros, tableros):
    for num in numeros:
        posiblesGanadores = []
        for t in tableros:
            for line in t:
                for n in line:
                    if n == num:
                        line[line.index(n)] = 'check'
                        posiblesGanadores.append(t)
        for t in posiblesGanadores:
            if comprobarSiGanado(t):
                if len(tableros) > 1:
                    tableros.remove(t)
                else:
                    return int(num) * sumAllUnmarked(tableros[0])


def sumAllUnmarked(t):
    sum = 0
    for line in t:
        for i in line:
             if i != 'check':
                sum += int(i)
    return sum


def comprobarSiGanado(t):
    lines = [Counter(line) for line in t]
    columns = [Counter(col) for col in np.transpose(t)]
    for i in lines:
        if i['check'] == 5:
            return True
    for i in columns:
        if i['check'] == 5:
            return True
    return False

def leerDatos():
    with open("./data/day4", 'r') as f:
        numeros = f.readline().split(',')
        tableros = []
        numTablero = -1
        for i in f.readlines():
            if i == '\n':
                tableros.append([])
                numTablero += 1
            else:
                tableros[numTablero].append(i.split())
    return numeros, tableros

def getStats():
    numeros, tableros = leerDatos()
    t1 = time.time()
    res_1 = parte1(numeros, tableros)
    t_parte1 = time.time() - t1
    t1 = time.time()
    res_2 = parte2(numeros, tableros)
    t_parte2 = time.time() - t1
    return res_1, t_parte1, res_2, t_parte2

def main():
    numeros, tableros = leerDatos()
    print('Los resultados del dia 4')
    print("Parte 1:", parte1(numeros, tableros))
    print("Parte 2:", parte2(numeros, tableros))
