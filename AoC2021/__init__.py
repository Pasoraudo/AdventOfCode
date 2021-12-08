from AoC2021.problemas import day1, day2, day3, day4, day5, day6, day7, day8, day9, day10, day11, day12
def allDays(days):
    print('Ejecutando todos los dias...')
    for day in days.values():
        print('---------------------------')
        day.main()


if __name__ == '__main__':
    day = input("Escoja el dia: ")
    days = {'1': day1, '2': day2, '3': day3, '4': day4, '5': day5, '6': day6, '7': day7, '8': day8, '9': day9,
            '10': day10, '11': day11, '12': day12}
    #try:
    if day == 'all':
        allDays(days)
    else:
        days[day].main()
    #except KeyError:
     #   print("Ese dia no existe")
    print("-------------------------\n|          FIN          |\n-------------------------")