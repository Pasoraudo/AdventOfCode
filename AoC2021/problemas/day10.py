import time


def parte1(input):
    inicio = ['(', '[', '{', '<']
    final = {'(': ')', '[': ']', '{': '}', '<': '>'}
    tValores = {')': 3, ']': 57, '}': 1197, '>': 25137}
    sum = 0
    for line in input:
        pila = []
        for c in line:
            if c in inicio:
                pila.append(c)
            else:
                p=final[pila.pop()]
                if c != p:
                    sum += tValores[c]
                    break
    return sum

def parte2(input):
    tValores = {'(': 1, '[': 2, '{': 3, '<': 4}
    aux = removeCorrupted(input)
    res = []
    for line in aux:
        sumaParcial = 0
        for i in reversed(line):
            sumaParcial = 5 * sumaParcial + tValores[i]
        res.append(sumaParcial)
    return sorted(res)[int(len(res)/2)]

def removeCorrupted(input):
    inicio = ['(', '[', '{', '<']
    final = {'(': ')', '[': ']', '{': '}', '<': '>'}
    aux = input.copy()
    res = []
    for line in aux:
        pila = []
        corrupta = False
        for c in line:
            if c in inicio:
                pila.append(c)
            else:
                if c != final[pila.pop()]:
                    input.remove(line)
                    corrupta = True
                    break
        if not corrupta:
            res.append(pila)
    return res

def leerDatos():
    with open("./data/day10", 'r') as f:
        data = [i for i in f.read().split('\n')]
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


def main():
    data = leerDatos()
    print('Los resultados del dia 10')
    print("Parte 1:", parte1(data))
    print("Parte 2:", parte2(data))