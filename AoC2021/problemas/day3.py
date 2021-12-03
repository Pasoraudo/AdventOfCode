from collections import Counter


def reverse(n):
    return ''.join(['0' if i == '1' else '1' for i in n])


def parte1(data):
    num = [Counter(i) for i in zip(*data)]
    res = ['1' if i.get('1') > i.get('0') else '0' for i in num]
    gamma = int(''.join(res), 2)
    epsilon = int(reverse(res), 2)
    return gamma * epsilon


def parte2(data):
    num = ['']*len(data[0])
    for i in data:
        for j in range(len(data[0])):
            num[j] += i[j]
    c = [Counter(i) for i in num]
    aux = ['1' if x['1'] >= x['0'] else '0' for x in c]
    co = ''.join(['0' if x['0'] <= x['1'] else '1' for x in c])



def main():
    address = "./data/day3"
    file = open(address, "r")
    data = file.read().split("\n")
    file.close()
    problems = {1: parte1, 2: parte2}
    prob = int(input("¿Problema 1 o 2?\n"))
    print("El resultado es: ", problems[prob](data))
