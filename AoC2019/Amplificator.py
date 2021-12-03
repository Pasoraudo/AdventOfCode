class Amplificator:

    def __init__(self, c, p):
        self.pos = 0
        self.phase = p
        self.output = 0
        self.code = c
        self.phaseSetting = False
        self.end = False

    def intcode(self):

        error = False
        self.end = False
        opcode = {1: self.opcode_1, 2: self.opcode_2, 3: self.opcode_3, 4: self.opcode_4, 5: self.opcode_5,
                  6: self.opcode_6, 7: self.opcode_7, 8: self.opcode_8, 99: self.opcode_99}
        while self.pos != -1 and not error and not self.end:
            try:
                #print("Opcode: ", self.code[self.pos] % 100, " en la posición: ", self.pos)
                opcode[self.code[self.pos] % 100]()
            except():
                print("Error con el opcode ", self.code[self.pos] % 100)
                error = True

    def address(self, place):

         switcher = {
            1: 100,
            2: 1000,
            3: 10000,
         }
         if self.code[self.pos] // switcher.get(place) % 10 == 0:
             return self.code[place + self.pos]
         else:
             return place + self.pos

    def opcode_1(self):
        self.code[self.address(3)] = self.code[self.address(1)] + self.code[self.address(2)]
        self.pos += 4

    def opcode_2(self):
        self.code[self.address(3)] = self.code[self.address(1)] * self.code[self.address(2)]
        self.pos += 4

    def opcode_3(self):
        if not self.phaseSetting:
            self.code[self.address(1)] = self.phase
            self.phaseSetting = True
        else:
            self.code[self.address(1)] = self.output
        self.pos += 2

    def opcode_4(self):
        self.output = self.code[self.address(1)]
        self.end = True
        self.pos += 2

    def opcode_5(self):
        if self.code[self.address(1)] != 0:
            self.pos = self.code[self.address(2)]
        else:
            self.pos += 3

    def opcode_6(self):
        if self.code[self.address(1)] == 0:
            self.pos = self.code[self.address(2)]
        else:
            self.pos += 3

    def opcode_7(self):
        if self.code[self.address(1)] < self.code[self.address(2)]:
            self.code[self.address(3)] = 1
        else:
            self.code[self.address(3)] = 0
        self.pos += 4

    def opcode_8(self):
        if self.code[self.address(1)] == self.code[self.address(2)]:
            self.code[self.address(3)] = 1
        else:
            self.code[self.address(3)] = 0
        self.pos += 4

    def opcode_99(self):
        self.pos = -1
