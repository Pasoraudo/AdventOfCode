
def memory_game(data, prob):
    problemas = {1: 2020, 2: 30000000}
    j = 1
    ult = {}
    for i in data:
        ult[i] = [j, 0]
        j += 1
    last = 0
    while j <= problemas[prob]:
        if last not in ult:
            ult[last] = [j, 0]
            last = 0
        elif ult[last][1] == 0:
            last = 0
            ult[last] = [j, ult[last][0]]
        else:
            last = ult[last][0] - ult[last][1]
            if last not in ult:
                ult[last] = [j, 0]
            else:
                ult[last] = [j, ult[last][0]]
        j += 1
    return last

def memory_game2(data, prob):
    problems = {1: 2020, 2: 30000000}
    d = {num: index for index, num in enumerate(data, 1)}
    current = data[-1]
    index = len(data)
    while index <= problems[prob]:
        previous = d.get(current)
        d[current] = index
        current = index - previous if previous else 0
        index += 1
    return list(d.keys())[list(d.values()).index(problems[prob])]


def main():
    address = "./data/day15"
    file = open(address, "r")
    data = [*map(int, file.read().split(","))]
    file.close()
    problems = {1: memory_game2, 2: memory_game}
    prob = int(input("¿Problema 1 o 2?\n"))
    print("El resultado es: ", problems[prob](data, prob))