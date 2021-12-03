from Grafo.Grafo import Grafo
from Grafo.Adyacente import Adyacente


class GrafoDirigido(Grafo):

    def __init__(self):
        super(True)
        self._numV = 0
        self._numA = 0
        self._elArray = []

    def numVertices(self):
        return self._numV

    def numAristas(self):
        return self._numA

    def existeArista(self, i, j):
        l = self._elArray[i]
        for n in l:
            if n.destino == j:
                return True
        return False

    def pesoArista(self, i, j):
        l = self._elArray[i]
        for n in l:
            if n.destino == j:
                return n.peso
        return 0

    def insertarArista(self, i, j):
        self.insertarArista(i, j, 1)

    def insertarArista(self, i, j, p):
        if not self.existeArista(i, j):
            self._elArray[i].append(Adyacente(j, p))
            self._numA += 1

    def adyacentesDe(self, i):
        return self._elArray[i]

    def esDirigido(self):
        return self._esDirigido