def XMAS(l):
    i = 0
    while True:
        not_found = preamble(l[i:(25 + i)], l[25 + i])
        if not not_found:
            return l[25 + i]
        if i >= len(l) - 25:
            break
        i += 1
    return "Fallo"


def contiguous_list_sum(l):
    res = 0
    for i in l:
        res += i
    return res


def preamble(l, valor):
    i = 0
    while i < len(l):
        j = i + 1
        while j < len(l):
            if l[i] + l[j] == valor:
                return True
            j += 1
        i += 1
    return False


def XMAS_encryption_breaker(l):
    invalid_number = XMAS(l)
    len_contiguous_list = 2
    found = False
    while not found:
        i = 0
        while i < len(l):
            if contiguous_list_sum(l[i:len_contiguous_list + i]) == invalid_number:
                return min(l[i:len_contiguous_list + i]) + max(l[i:len_contiguous_list + i])
            i += 1
        len_contiguous_list += 1


def main():
    address = "./data/day9"
    file = open(address, "r")
    entrada = file.read().split()
    file.close()
    l = []
    for i in entrada:
        l.append(int(i))
    problems = {1: XMAS, 2: XMAS_encryption_breaker}
    prob = int(input("¿Problema 1 o 2?\n"))
    print("El resultado es: ", problems[prob](l))
