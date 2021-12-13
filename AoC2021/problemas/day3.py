from collections import Counter
import time


def reverse(n):
    return ['0' if i == '1' else '1' for i in n]


def parte1(data):
    num = [Counter(i) for i in zip(*data)]
    res = ['1' if i.get('1') > i.get('0') else '0' for i in num]
    gamma = int(''.join(res), 2)
    epsilon = int(''.join(reverse(res)), 2)
    return gamma * epsilon


def parte2(data):
    oxygen = oxygenGenerator(data.copy())
    co = coGenerator(data.copy())
    return int(oxygen, 2) * int(co, 2)

def generator(input, func):
    pos = 0
    while(len(input) > 1):
        num = {'0': 0, '1': 0}
        for i in input:
            num[i[pos]] += 1
        masComun = '1' if func(num['1'], num['0']) else '0'
        aux = input.copy()
        for i in aux:
            if i[pos] != masComun:
                input.remove(i)
        pos += 1
    return input[0]

def oxygenGenerator(oxygen):
    return generator(oxygen, lambda a, b: a >= b)

def coGenerator(co):
    return generator(co, lambda a, b: a < b)

def leerDatos():
    with open("./data/day3", 'r') as f:
        data = f.readlines()
    return data

def getStats():
    t1 = time.time()
    res_1 = parte1(leerDatos())
    t_parte1 = time.time() - t1
    t1 = time.time()
    res_2 = parte2(leerDatos())
    t_parte2 = time.time() - t1
    return res_1, t_parte1, res_2, t_parte2

def main():
    address = "./data/day3"
    file = open(address, "r")
    data = file.read().split("\n")
    file.close()
    print('Los resultados del dia 3')
    print("Parte 1:", parte1(data))
    print("Parte 2:", parte2(data))
