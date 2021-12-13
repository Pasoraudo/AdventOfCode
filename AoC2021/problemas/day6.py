from collections import Counter
import time


def problema(fishs, nDays):
    numFishs = Counter(fishs)
    for day in range(nDays):
        aux = {}
        for d in numFishs:
            if d != 0:
                if d - 1 not in aux.keys():
                    aux[d - 1] = 0
                aux[d - 1] += numFishs[d]
            else:
                if 6 not in aux.keys():
                    aux[6] = 0
                aux[6] += numFishs[0]
                if 8 not in aux.keys():
                    aux[8] = 0
                aux[8] += numFishs[0]
        numFishs = aux.copy()
        #print('After day', day + 1, ':', numFishs)
    return sum(numFishs.values())


def getStats():
    data = leerDatos()
    data2 = data.copy()
    t1 = time.time()
    res_1 = problema(data, 80)
    t_parte1 = time.time() - t1
    t1 = time.time()
    res_2 = problema(data2, 256)
    t_parte2 = time.time() - t1
    return res_1, t_parte1, res_2, t_parte2

def leerDatos():
    with open("./data/day6", 'r') as f:
        data = [int(i) for i in f.read().split(',')]
    return data


def main():
    data = leerDatos()
    print('Los resultados del dia 6')
    print("Parte 1:", problema(data.copy(), 80))
    print("Parte 2:", problema(data, 256))
