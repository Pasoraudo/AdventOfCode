class Day9:

    def __init__(self, c, p, o):
        self.code = c
        self.pos = p
        self.output = o
        self.relativeBase = 0

    def intcode(self):

        opcode = {1: self.opcode_1, 2: self.opcode_2, 3: self.opcode_3, 4: self.opcode_4, 5: self.opcode_5,
                  6: self.opcode_6, 7: self.opcode_7, 8: self.opcode_8, 9: self.opcode_9, 99: self.opcode_99}
        while self.pos != -1:
            try:
                #print("Opcode: ", self.code[self.pos] % 10)
                opcode[self.code[self.pos] % 100]()
            except IndexError:
                self.code.extend([0] * 1000)

    def address(self, place):

         switcher = {
            1: 100,
            2: 1000,
            3: 10000
         }
         if self.code[self.pos] // switcher.get(place) % 10 == 0:
             return self.code[place + self.pos]
         elif self.code[self.pos] // switcher.get(place) % 10 == 1:
             return place + self.pos
         else:
             return self.relativeBase + self.code[place + self.pos]

    def opcode_1(self):
        self.code[self.address(3)] = self.code[self.address(1)] + self.code[self.address(2)]
        self.pos += 4

    def opcode_2(self):
        self.code[self.address(3)] = self.code[self.address(1)] * self.code[self.address(2)]
        self.pos += 4

    def opcode_3(self):
        self.code[self.address(1)] = self.output
        self.pos += 2

    def opcode_4(self):
        self.output = self.code[self.address(1)]
        self.pos += 2

    def opcode_5(self):
        if self.code[self.address(1)] != 0:
            self.pos = self.code[self.address(2)]
        else:
            self.pos += 3

    def opcode_6(self):
        if self.code[self.address(1)] == 0: self.pos = self.code[self.address(2)]
        else: self.pos += 3

    def opcode_7(self):
        if self.code[self.address(1)] < self.code[self.address(2)]: self.code[self.address(3)] = 1
        else: self.code[self.address(3)] = 0
        self.pos += 4

    def opcode_8(self):
        if self.code[self.address(1)] == self.code[self.address(2)]:
            self.code[self.address(3)] = 1
        else:
            self.code[self.address(3)] = 0
        self.pos += 4

    def opcode_9(self):
        self.relativeBase += self.code[self.address(1)]
        self.pos += 2

    def opcode_99(self):
        self.pos = -1

    @staticmethod
    def main():
        address = "./data/day9"
        file = open(address, "r")
        code = file.read().split(' ')
        file.close()
        code = list(map(int, code))
        day9 = Day9(code, 0, int(input("Introduce el par??metro de entrada: ")))
        day9.intcode()
        print("El resultado es: ", day9.output)
