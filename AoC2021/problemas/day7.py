import statistics as s
import matplotlib.pyplot as plt


def parte1(crabs):
    pos_h = int(s.median(crabs))
    return sum([abs(i - pos_h) for i in crabs])


def grafica_parte2(crabs):
    fig, ax = plt.subplots()
    x = []
    y = []
    for i in range(min(crabs), max(crabs) + 1):
        x.append(i)
        y.append(sum([sumatorio(crab, i) for crab in crabs]))
    ax.scatter(x, y)
    plt.show()


def parte2(crabs):
    pos_h = int(s.mean(crabs))
    encontrado = False
    while not encontrado:
        res = sum([sumatorio(crab, pos_h) for crab in crabs])
        siguiente = sum([sumatorio(crab, pos_h + 1) for crab in crabs])
        if res > siguiente:
            pos_h += 1
            continue
        anterior = sum([sumatorio(crab, pos_h - 1) for crab in crabs])
        if res > anterior:
            pos_h -= 1
            continue
        encontrado = True
    return res


def sumatorio(crab, pos_h):
    return int(abs(crab - pos_h) * (abs(crab - pos_h) + 1) / 2)

def main():
    with open("./data/day7", 'r') as f:
        data = [int (i) for i in f.read().split(',')]
    print('Los resultados del dia 7')
    print("Parte 1:", parte1(data))
    print("Parte 2:", parte2(data))
    #grafica_parte2(data)
