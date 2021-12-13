from AoC2021.problemas import day1, day2, day3, day4, day5, day6, day7, day8, day9, day10, day11, day12
import time

def allDays(days):
    nombres = ['Sonar Sweep', 'Dive!', 'Binary Diagnostic', 'Giant Squid', 'Hydrothermal Venture', 'Lanternfish',
               'The Treachery of Whales', 'Seven Segment Search', 'Smoke Basin', 'Syntax Scoring', 'Dumbo Octopuses']
    tiempoTotal = 0
    año, dia, parte, nombre, resultado, tiempo = 'Año', 'Día', 'Parte', 'Nombre', 'Resultado', 'Tiempo(ms)'
    print("{:<5} {:<4} {:<6} {:<30} {:<20} {:<6}".format(año, dia, parte, nombre, resultado, tiempo))
    año = '2021'
    for dia in range(1, len(nombres) + 1):
        res_1, t_parte1, res_2, t_parte2 = days[str(dia)].getStats()
        tiempoTotal += t_parte1 + t_parte2
        print("{:<5} {:<4} {:<6} {:<30} {:<20} {:<6}".format(año, dia, 1, nombres[dia - 1], res_1, round(t_parte1 * 1000, 3)))
        print("{:<5} {:<4} {:<6} {:<30} {:<20} {:<6}".format(año, dia, 2, nombres[dia - 1], res_2, round(t_parte2 * 1000, 3)))
    print('Resuelto', len(nombres) * 2, 'problemas en', round(tiempoTotal, 3), 'segundos.')

def medirTiempo(func):
    t1 = time.time()
    func()
    return time.time() - t1

if __name__ == '__main__':
    day = input("Escoja el dia: ")
    days = {'1': day1, '2': day2, '3': day3, '4': day4, '5': day5, '6': day6, '7': day7, '8': day8, '9': day9,
            '10': day10, '11': day11}
    if day == 'all':
        allDays(days)
    else:
        days[day].main()
    print("-------------------------\n|          FIN          |\n-------------------------")