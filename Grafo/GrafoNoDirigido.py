from Grafo.GrafoDirigido import GrafoDirigido


class GrafoNoDirigido(GrafoDirigido):

    def __init__(self):
        super()
        self._esDirigido = False

    def insertarArista(self, u, v):
        if not self.existeArista(u, v):
            super.insertarArsita(u, v, 1)
            super.insertarArsita(v, u, 1)
            self.numA += 1

    def insertarArista(self, u, v, p):
        if not self.existeArista(u, v):
            super.insertarArsita(u, v, p)
            super.insertarArsita(v, u, p)
            self.numA += 1

    def interseccion(self, g):
        res = GrafoNoDirigido(self.numV)
        cont = 0
        for i in self.elArray:
            cont += 1
            for j in i:
                dest = j.getDestino()
                if g.existeArista(cont, dest):
                    res.insertarArista(cont, dest)
        return res

    @staticmethod
    def suma():
        print("hola")