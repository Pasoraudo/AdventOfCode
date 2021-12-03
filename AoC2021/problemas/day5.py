def main():
    address = "./data/day5"
    file = open(address, "r")
    data = file.read().split("\n")
    file.close()
    print(data)
    print("hola")
    #problems = {1: parte1, 2: parte1}
    prob = int(input("¿Problema 1 o 2?\n"))
    #print("El resultado es: ", problems[prob](data))
