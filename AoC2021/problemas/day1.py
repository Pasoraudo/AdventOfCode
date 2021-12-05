def parte1(input):
    count = 0
    for i in range(len(input) - 1):
        if input[i + 1] > input[i]:
            count += 1
    return count


def parte2(input):
    count = 0
    for i in range(len(input)):
        if sum(input[i+1:i+4]) > sum(input[i:i+3]):
            count += 1
    return count


def main():
    with open("./data/day1", 'r') as f:
        data = [int(i) for i in f.readlines()]
    print('Los resultados del dia 1')
    print("Parte 1:", parte1(data))
    print("Parte 2:", parte2(data))
