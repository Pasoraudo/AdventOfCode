from copy import deepcopy


def seen_adjacent(seats, num_f, num_c, x, y):
    cont = 0
    for yi, xi in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        cy, cx = y + yi, x + xi
        while 0 <= cx < num_c and 0 <= cy < num_f and seats[cy][cx] == ".":
            cy, cx = cy + yi, cx + xi
        if 0 <= cx < num_c and 0 <= cy < num_f and seats[cy][cx] == "#":
            cont += 1
    return cont


def directly_adjacent(seats, num_f, num_c, x, y):
    res = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i == 0 and j == 0) and 0 <= y + j < num_f and 0 <= x + i < num_c:
                res += seats[y + j][x + i]
    return len(list(filter(is_hash, res)))


def is_hash(val):
    return '#' == val


def find_seat(seats, prob):
    i = 0
    while True:
        ant = seats[:]
        seats = seat_iteration(seats, prob)
        if ant == seats:
            break
        i += 1
    cont = 0
    for i in seats:
        cont += len(list(filter(is_hash, i)))
    return cont


def seat_iteration(seats, prob):
    res = deepcopy(seats)
    num_f, num_c = len(seats), len(seats[0])
    adjacents = {1: directly_adjacent, 2: seen_adjacent}
    tolerance = {1: 4, 2: 5}
    for x in range(num_c):
        for y in range(num_f):
            if seats[y][x] == '.':
                continue
            adj = adjacents[prob](seats, num_f, num_c, x, y)
            if seats[y][x] == '#' and adj >= tolerance[prob]:
                res[y][x] = 'L'
            elif seats[y][x] == 'L' and adj == 0:
                res[y][x] = '#'
    return res


def main():
    address = "./data/day11"
    file = open(address, "r")
    seats = [*map(list, file.read().splitlines())]
    file.close()
    prob = int(input("¿Problema 1 o 2?\n"))
    print(find_seat(seats, prob))