class Day8:

    def __init__(self, b):
        self.acum = 0
        self.boot_code = b
        self.pointer = 0

    def exec_boot_code(self):
        instructions = {"acc": self.acc, "jmp": self.jmp, "nop": self.nop}
        prev_instructions = [0]
        while self.pointer < len(self.boot_code):
            instructions[self.boot_code[self.pointer][0:3]]()
            self.pointer += 1
            if self.pointer in prev_instructions:
                break
            prev_instructions += [self.pointer]
        return self.acum

    def fixer(self, i):
        if self.boot_code[i][0:3] == "nop":
            self.boot_code[i] = self.boot_code[i].replace("nop", "jmp")
        elif self.boot_code[i][0:3] == "jmp":
            self.boot_code[i] = self.boot_code[i].replace("jmp", "nop")

    def acc(self):
        self.acum += int(self.boot_code[self.pointer][4:])

    def jmp(self):
        self.pointer += int(self.boot_code[self.pointer][4:]) - 1

    def nop(self):
        self.pointer += 0


def infinite_boot_code(instructions):
    day8 = Day8(instructions)
    day8.exec_boot_code()
    return day8.acum


def fix_boot_code(instructions):
    instruction_fixed = 0
    while True:
        day8 = Day8(instructions[:])
        day8.fixer(instruction_fixed)
        day8.exec_boot_code()
        instruction_fixed += 1
        if day8.pointer >= len(day8.boot_code):
            break
    return day8.acum


def main():
    address = "./data/day8"
    file = open(address, "r")
    instructions = file.read().split("\n")
    file.close()
    problems = {1: infinite_boot_code, 2: fix_boot_code}
    prob = int(input("¿Problema 1 o 2?\n"))
    print("El resultado es: ", problems[prob](instructions))