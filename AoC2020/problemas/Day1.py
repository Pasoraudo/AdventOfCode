def two_entries(lis):
    for i in lis:
        for j in lis:
            if i + j == 2020:
                return i * j


def three_entries(lis):
    for i in lis:
        for j in lis:
            for t in lis:
                if i + j + t == 2020:
                    return i * j * t


def main():
    address = "./data/day1"
    file = open(address, "r")
    lis = file.read().split("\n")
    file.close()
    lis = list(map(int, lis))
    problems = {1: two_entries, 2: three_entries}
    prob = int(input("¿Problema 1 o 2?\n"))
    print("El resultado es: ", problems[prob](lis))
