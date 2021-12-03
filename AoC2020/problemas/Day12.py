class Ship:
    def __init__(self):
        self.pos = [1, 10]
        self.ship = [0, 0]
        self.dir = 'E'

    def navigation_computer(self, inst):
        self.pos = [0, 0]
        instructions = {'N': self.north, 'S': self.south, 'E': self.east, 'W': self.west,
                        'L': self.left, 'R': self.right, 'F': self.forward}
        for i in inst:
            instructions[i[0]](int(i[1:]))
        return abs(self.pos[0]) + abs(self.pos[1])

    def relative_navigation_computer(self, inst):
        instructions = {'N': self.north, 'S': self.south, 'E': self.east, 'W': self.west,
                        'L': self.relative_left, 'R': self.relative_right, 'F': self.relative_forward}
        for i in inst:
            instructions[i[0]](int(i[1:]))
        return abs(self.ship[0]) + abs(self.ship[1])

    def north(self, val):
        self.pos[0] += val

    def south(self, val):
        self.pos[0] -= val

    def east(self, val):
        self.pos[1] += val

    def west(self, val):
        self.pos[1] -= val

    def left(self, val):
        num_to_coor = ['N', 'W', 'S', 'E']
        coor_to_num = {'N': 0, 'W': 1, 'S': 2, 'E': 3}
        self.dir = num_to_coor[int((coor_to_num[self.dir] + int(val / 90)) % 4)]

    def right(self, val):
        num_to_coor = ['N', 'W', 'S', 'E']
        coor_to_num = {'N': 0, 'W': 1, 'S': 2, 'E': 3}
        self.dir = num_to_coor[int((coor_to_num[self.dir] - int(val / 90)) % 4)]

    def forward(self, val):
        instructions = {'N': self.north, 'S': self.south, 'E': self.east, 'W': self.west}
        instructions[self.dir](val)

    def relative_forward(self, val):
        self.ship[0] += val * self.pos[0]
        self.ship[1] += val * self.pos[1]

    def relative_right(self, val):
        for i in range(int(val / 90)):
            aux = self.pos[0]
            self.pos[0] = -self.pos[1]
            self.pos[1] = aux

    def relative_left(self, val):
        for i in range(int(val / 90)):
            aux = self.pos[0]
            self.pos[0] = self.pos[1]
            self.pos[1] = -aux


def main():
    address = "./data/day12"
    file = open(address, "r")
    inst = file.read().split()
    file.close()
    ship = Ship()
    problems = {1: ship.navigation_computer, 2: ship.relative_navigation_computer}
    prob = int(input("¿Problema 1 o 2?\n"))
    print("El resultado es: ", problems[prob](inst))