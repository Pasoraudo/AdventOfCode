import queue
from abc import ABC, abstractmethod



class Grafo(ABC):

    @abstractmethod
    def __init__(self, esDirigido):
        self._esDirigido = esDirigido
        self._visitados = []
        self._ordenVisita = 0
        self._q = queue

    @abstractmethod
    def esDirigido(self):
        return self._esDirigido

    @abstractmethod
    def numVertices(self):
        pass

    @abstractmethod
    def numAristas(self):
        pass

    @abstractmethod
    def existeArista(self, i, j):
        pass

    @abstractmethod
    def pesoArista(self, i, j):
        pass

    @abstractmethod
    def insertarArista(self, i, j):
        pass

    @abstractmethod
    def insertarArista(self, i, j, peso):
        pass

    @abstractmethod
    def adyacentesDe(self, i):
        pass
