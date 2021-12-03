def passwords(lis):
    res = 0
    for i in lis:
        rang = i[0].split("-")
        num = i[2].count(i[1][0])
        if int(rang[0]) <= num <= int(rang[1]):
            res += 1
    return res


def passwords_two(lis):
    res = 0
    for i in lis:
        rang = i[0].split("-")
        letter = i[1][0]
        if letter == i[2][int(rang[0]) - 1]:
            if letter != i[2][int(rang[1]) - 1]:
                res += 1
        elif letter == i[2][int(rang[1]) - 1]:
            if letter != i[2][int(rang[0]) - 1]:
                res += 1
    return res


def main():
    address = "./data/day2"
    file = open(address, "r")
    lis = []
    aux = file.read().split("\n")
    file.close()
    for i in aux:
        lis += [i.split(" ")]
    problems = {1: passwords, 2: passwords_two}
    prob = int(input("¿Problema 1 o 2?\n"))
    print("El resultado es: ", problems[prob](lis))
