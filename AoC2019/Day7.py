from Amplificator import *


class Day7:

    def __init__(self, mi, ma, c, p):
        self.min = mi
        self.max = ma
        self.code = c
        self.problema = p

    def machine(self, ini, end):
        amplificators = []
        res = 0
        while self.min <= self.max:
            phase = self.phases(ini, end)
            if phase[0] != -1:
                output = 0
                for i in range(5):
                    amplificators.append(Amplificator(self.code, phase[i]))
                i = 0
                while amplificators[4].pos != -1:
                    #print("Amplificador ", + i, " funcionando con input ", output, " y fase ", phase[i])
                    amplificators[i].output = output
                    amplificators[i].intcode()
                    output = amplificators[i].output
                    problemas = {1: self.problema_1, 2: self.problema_2}
                    switcher = {
                        1: amplificators[i].pos,
                        2: i
                    }
                    i += problemas[self.problema](switcher.get(self.problema))
                #print("El output correspondiente a ", min, " es ", output)
                if res < output:
                    res = output
                amplificators.clear()
        return res

    @staticmethod
    def problema_1(pos):
        if pos == -1:
            return 1
        return 0

    @staticmethod
    def problema_2(i):
        if i == 4:
            return -4
        return 1

    @staticmethod
    def num_decres(min, max):
        res = 0
        for i in range(min, max + 1):
            res += 10 ** (max - i) * i
        return res

    @staticmethod
    def num_aument(min, max):

        res = 0
        for i in range(max, min - 1, -1):
            res += 10 ** (i - min) * i
        return res

    def phases(self, ini, end):

        res = [0] * 5
        i = 0
        while i < end - ini + 1 and res[0] != -1:
            res[i] = (int(self.min / 10 ** i % 10))
            n = i + 1
            while n < end - ini + 1 and res[0] != -1:
                #print("Comprobando: " + str(i) + " y " + str(n))
                if self.min // 10 ** i % 10 == self.min // 10 ** n % 10:
                    res[0] = -1
                elif self.min // 10 ** i % 10 > end or self.min // 10 ** i % 10 < ini:
                    res[0] = -1
                n += 1
            i += 1
        self.min += 1
        return res

    @staticmethod
    def main():
        address = "./data/day7"
        file = open(address, "r")
        code = file.read().split(' ')
        file.close()
        code = list(map(int, code))
        print("Escoja entre: ", "1 - Problema 1", "2 - Problema 2", "0 - Salir", sep="\n")
        pro = int(input())
        while pro != 0:
            if pro == 1 or pro == 2:
                day7 = Day7(Day7.num_decres(pro * 5 - 5, pro * 5 - 1),
                            Day7.num_aument(pro * 5 - 5, pro * 5 - 1), code, pro)
                print("El resultado es: ", day7.machine(pro * 5 - 5, pro * 5 - 1))
                break
            else:
                print("Escoja entre el problema 1 o 2 o marca 0 para salir")
                pro = input()
