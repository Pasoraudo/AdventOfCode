from collections import Counter


def parte1(data):
    num = [Counter(i) for i in zip(*data)]
    res = [1 if  i.get('1') > i.get('0') else 0 for i in num]
    gamma = 0; epsilon = 0
    p = len(data[0]) - 1
    for i in num:
        if i.get('1') > i.get('0'):
            gamma += pow(2, p)
        else:
            epsilon += pow(2, p)
        p -= 1
    return gamma * epsilon


def parte2(data):
    return 0

def main():
    address = "./data/day3"
    file = open(address, "r")
    data = file.read().split("\n")
    file.close()
    print(data)
    problems = {1: parte1, 2: parte2}
    prob = int(input("¿Problema 1 o 2?\n"))
    print("El resultado es: ", problems[prob](data))
