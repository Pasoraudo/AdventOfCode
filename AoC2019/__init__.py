from Day5 import *
from Day7 import *
from Day9 import *
from Day10 import *
from Day11 import *


def __init__():

    days = {5: Day5.main, 7: Day7.main, 9: Day9.main, 10: Day10.main, 11: Day11.main}
    while True:
        try:
            day = int(input("Escoja el dia: "))
            if day == 0:
                break
            days[day]()
            break
        except KeyError:
            print("Escoja un dia válido o salga pulsando 0")
        except ValueError:
            print("Eso no es un número")
    print("FIN")


__init__()
