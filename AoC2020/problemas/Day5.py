def dec_boarding_pass(boarding_pass):
    row_f = 0
    row_b = 127
    column_l = 0
    column_r = 7
    for i in boarding_pass:
        if i == "F":
            row_b -= (row_b - row_f + 1) / 2
        elif i == "B":
            row_f += (row_b - row_f + 1) / 2
        elif i == "L":
            column_r -= (column_r - column_l + 1) / 2
        else:
            column_l += (column_r - column_l + 1) / 2
    return row_f * 8 + column_l


def find_boarding_passes(boarding_passes):
    res = 0
    for i in boarding_passes:
        aux = dec_boarding_pass(i)
        if aux > res:
            print(i, ": ", aux)
            res = aux
    return res


def find_my_seat(boarding_passes):
    IDs = []
    for i in boarding_passes:
        IDs.append(dec_boarding_pass(i))
    IDs.sort()
    seat = IDs[0]
    while seat in IDs:
        seat += 1
    return seat

def main():
    address = "./data/day5"
    file = open(address, "r")
    boarding_passes = file.read().split("\n")
    file.close()
    problems = {1: find_boarding_passes, 2: find_my_seat}
    prob = int(input("¿Problema 1 o 2?\n"))
    print("El resultado es: ", problems[prob](boarding_passes))
