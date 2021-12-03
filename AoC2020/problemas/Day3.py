def trees_encountered(m):
    res = three_right_one_down(m, 1, 1)
    res *= three_right_one_down(m, 3, 1)
    res *= three_right_one_down(m, 5, 1)
    res *= three_right_one_down(m, 7, 1)
    res *= three_right_one_down(m, 1, 2)
    return res


def three_right_one_down(m, r, d):
    res = 0
    i = 0
    j = 0
    while j < len(m):
        if m[j][i] == '#':
            res += 1
        j += d
        i += r
        if i >= len(m[0]):
            i -= len(m[0])
    return res


def main():
    address = "./data/day3"
    file = open(address, "r")
    m = file.read().split("\n")
    file.close()
    prob = int(input("¿Problema 1 o 2?\n"))
    if prob == 1:
        print("El resultado es: ", three_right_one_down(m, 3, 1))
    elif prob == 2:
        print("El resultado es: ", trees_encountered(m))
