import time


def parte1(input):
    hPos = 0
    depth = 0
    for i in input:
        if i[0] == 'forward':
            hPos += int(i[1])
        elif i[0] == 'down':
           depth += int(i[1])
        elif i[0] == 'up':
            depth -= int(i[1])
    return hPos * depth

def parte2(input):
    hPos = 0
    depth = 0
    aim = 0
    for i in input:
        x = int(i[1])
        if i[0] == 'forward':
            hPos += x
            depth += aim * x
        elif i[0] == 'down':
            aim += x
        elif i[0] == 'up':
            aim -= x
    return hPos * depth


def leerDatos():
    with open("./data/day2", 'r') as f:
        data = [line[:-1].split(' ') for line in f.readlines()]
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
    data = leerDatos()
    print('Los resultados del dia 2')
    print("Parte 1:", parte1(data))
    print("Parte 2:", parte2(data))
