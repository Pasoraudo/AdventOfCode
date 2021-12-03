import math


class Day10:

    def __init__(self, m):

        self.base = (0, 0)
        self.num_asteroids = 0
        self.map = m
        self.coordinates = 0

    @staticmethod
    def vector(point1, point2):

        return point2[1] - point1[1], point1[0] - point2[0]

    @staticmethod
    def angle(u, v):

        return math.acos(int((u[0] * v[0] + u[1] * v[1]) / int((math.sqrt(u[0] ** 2 + u[1] ** 2) * math.sqrt(v[0] ** 2 + v[1] ** 2))))) == 0

    @staticmethod
    def tapado(u, v):

        if u != (0, 0) and u != v and v != (0, 0):
            if u[0] * v[1] == u[1] * v[0]:
                if math.sqrt(u[0] ** 2 + u[1] ** 2) >= math.sqrt(v[0] ** 2 + v[1] ** 2):
                    if Day10.angle(u, v):
                        return True
        return False

    @staticmethod
    def num_asteroids_has(vectors):

        cont = -1
        for i in vectors:
            tapado = False
            for n in vectors:
                tapado = Day10.tapado(i, n)
                if tapado:
                    break
            if not tapado:
                #print("No está tapado", i)
                cont += 1
        return cont

    def decode(self):

        cont = 0
        vectors = []
        for i in self.map:
            for n in self.map:
                vectors.append(Day10.vector(i, n))
            asteroids = Day10.num_asteroids_has(vectors)
            if asteroids > self.num_asteroids:
                self.num_asteroids = asteroids
                self.base = self.map[cont]
                self.coordinates = cont
                print("Actualizando el número de asteroides de la nueva base con coordenadas", self.base, "y", self.num_asteroids, "asteroides detectables")
            vectors.clear()
            cont += 1

    @staticmethod
    def main():
        address = "./data/day10"
        file = open(address, "r")
        map = []
        aux = file.read().split()
        file.close()
        x = 0
        y = 0
        for i in aux:
            for n in i:
                if n == '#':
                    map.append((x, y))
                y += 1
            x += 1
            y = 0
        day10 = Day10(map)
        print("Escoja entre: ", "1 - Problema 1", "2 - Problema 2", "0 - Salir", sep="\n")
        pro = int(input())
        while pro != 0:
            if pro == 1:
                print("Ejecutando el primer problema")
                day10.decode()
                print("La nueva base se situa en las coordenadas", day10.base, "y se pueden detectar", day10.num_asteroids, "asteroides")
                break
            elif pro == 2:
                print("No se hacerlo XD")
                break
            else:
                print("Escoja entre el problema 1 o 2 o marca 0 para salir")
                pro = input()
