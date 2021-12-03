class Adyacente:

    def __init__(self, v, p):
        self.destino = v
        self.peso = p

    def getDestino(self):
        return self.destino

    def getPeso(self):
        return self.peso
    
    def __str__(self):
        return str(self.destino) + "(" + str(self.peso) + ")"