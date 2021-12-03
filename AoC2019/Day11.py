from Robot import *

class Day11:

    @staticmethod
    def main():
        address = "./data/day11"
        file = open(address, "r")
        code = file.read().split(',')
        file.close()
        code = list(map(int, code))
        print(code)
        robot = Robot(code, 0)
        robot.intcode()
        print("El resultado es: ", robot.cont)
