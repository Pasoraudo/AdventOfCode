def l_jolts_diferences(jolts):
    num_ones, num_threes = 0, 1
    ant = 0
    for i in jolts:
        if i - ant == 1:
            num_ones += 1
        elif i - ant == 3:
            num_threes += 1
        ant = i
    return num_ones * num_threes


def distinct_ways_arrange_aux(jolts):
    return distinct_ways_arrange(jolts, 1, 0, 0, 1)


def distinct_ways_arrange(jolts, n1, n2, n3, i):
    if i > jolts[-1]:
        return n1
    n = n1 + n2 + n3
    if i not in jolts:
        n = 0
    return distinct_ways_arrange(jolts, n, n1, n2, i + 1)


def main():
    address = "./data/day10"
    file = open(address, "r")
    jolts = file.read().split()
    file.close()
    jolts = list(map(int, jolts))
    jolts = sorted(jolts)
    problems = {1: l_jolts_diferences, 2: distinct_ways_arrange_aux}
    prob = int(input("¿Problema 1 o 2?\n"))
    print("El resultado es: ", problems[prob](jolts))