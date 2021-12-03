from collections import Counter as count


def reverse(n):
    return ''.join(['1' if i == '1' else '0' for i in n])


def parte1(data):
    num = [count(i) for i in zip(*data)]
    res = ['1' if i.get('1') > i.get('0') else '0' for i in num]
    gamma = int(''.join(res), 2)
    print(res)
    epsilon = int(reverse(res), 2)
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
