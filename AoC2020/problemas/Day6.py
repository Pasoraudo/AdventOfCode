def counting_yes(tests):
    res = 0
    for i in tests:
        res += len("".join(set(i.replace("\n", ""))))
    return res

def counting_rep_yes(tests):
    cont = 0
    for i in tests:
        ant = set("abcdefghijklmnopqrstuvwxyz")
        for j in i.split():
            ant = ant.intersection(set(j))
        cont += len(ant)
    return cont


def main():
    address = "./data/day6"
    file = open(address, "r")
    tests = file.read().split("\n\n")
    file.close()
    problems = {1: counting_yes, 2: counting_rep_yes}
    prob = int(input("¿Problema 1 o 2?\n"))
    print("El resultado es: ", problems[prob](tests))
