class Arista():

    def __init__(self, u, v, p):
        self.origen = u
        self.destino = v
        self.peso = p

    def __cmp__(self, other):
        return self.peso - other.peso

    def getOrigen(self):
        return self.origen

    def getDestino(self):
        return self.destino

    def getPeso(self):
        return self.peso
