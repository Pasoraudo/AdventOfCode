from AoC2021.problemas import day1, day2, day3, day4, day5

if __name__ == '__main__':
    day = int(input("Escoja el dia: "))
    days = {1: day1, 2: day2, 3: day3, 4: day4, 5: day5}
    try:
        days[day].main()
    except KeyError:
        print("Ese dia no existe")
    print("-------------------------\n|          FIN          |\n-------------------------")