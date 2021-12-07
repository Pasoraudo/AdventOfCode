import statistics as s


def parte1(crabs):
    posH = int(s.median(crabs))
    return sum([abs(i - posH) for i in crabs])


def parte2(crabs):
    posH = int(s.mean(crabs))
    return sum([i for i in [sum(range(1, abs(crab - posH)  + 1)) for crab in crabs]])


def main():
    with open("./data/day7", 'r') as f:
        data = [int (i) for i in f.read().split(',')]
    print('Los resultados del dia 7')
    print("Parte 1:", parte1(data.copy()))
    print("Parte 2:", parte2(data.copy()))
