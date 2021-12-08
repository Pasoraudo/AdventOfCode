def parte1(input):
    return 0

def parte2(input):
    return 0


def main():
    with open("./data/day11", 'r') as f:
        data = [int (i) for i in f.read().split(',')]
    print('Los resultados del dia 11')
    print("Parte 1:", parte1(data))
    print("Parte 2:", parte2(data))