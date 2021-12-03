from AoC2020.problemas import Day1, Day6, Day3, Day13, Day15, Day4, Day9, Day17, Day10, Day5, Day2, Day11, Day14, \
    Day16, Day12, Day7, Day8, Day18

if __name__ == '__main__':
    day = int(input("Escoja el dia: "))
    days = {1: Day1, 2: Day2, 3: Day3, 4: Day4, 5: Day5, 6: Day6, 7: Day7, 8: Day8,9: Day9, 10: Day10,
            11: Day11, 12: Day12, 13: Day13, 14: Day14, 15: Day15, 16: Day16, 17: Day17, 18: Day18}
    try:
        days[day].main()
    except KeyError:
        print("Ese dia no existe")
    print("-------------------------\n|          FIN          |\n-------------------------")
